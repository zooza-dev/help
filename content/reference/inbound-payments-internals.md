---
title: "Inbound payments — technical reference"
slug: "inbound-payments-internals"
type: "reference"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: ["inbound-payments", "pairing-algorithm", "llm", "variable-symbol", "delegation-chain", "ignore-filter", "candidate-validation", "reference"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-04-02"
---

# Inbound payments — technical reference

> **Purpose of this document:** Full technical context for the inbound payment pairing system. Use this when answering detailed support questions about why a payment was or was not paired, how the AI evaluation works, or how to configure business rules and filters effectively. For the admin-facing setup guide, see [Inbound payments — setup and pairing](../guides/inbound-payments.md).

---

## System overview

Inbound payments ingests bank transfers from three sources (GoCardless, bank email, CSV), parses each into a standardised format, runs a deterministic pairing algorithm, applies ignore filters, and then uses an LLM layer for duplicate detection and pairing validation. The result is either automatic pairing (payment recorded on a registration) or a manual review queue.

Every payment eventually reaches one of four statuses:

| Status | Meaning |
|--------|---------|
| `staging` | Saved, awaiting LLM evaluation |
| `new` | LLM returned "manual" or pairing failed — waiting for admin action |
| `paired` | Accepted and written to the payments ledger |
| `ignore` | Not a Zooza payment — filtered, LLM-decided, or admin-ignored |

---

## Ingestion channels

### GoCardless (open banking)

GoCardless is used here as a **bank account data reader**, not a payment gateway. It holds an open banking consent from the company, polls the company's bank for new transactions, and forwards each transaction to Zooza as it appears.

The company ID is known from the integration setup — no IBAN lookup is needed.

**Consent expiry (PSD2):** The consent expires after a bank-defined period (commonly 90 days). When it expires, transaction notifications stop silently — Zooza does not alert the company. This is a common cause of "payments stopped arriving" support tickets. The fix is to reconnect via the GoCardless authorisation flow.

### Bank email (encoded address)

Zooza generates a unique per-billing-profile email address:
`payments.inb.{bank}.{hmac-encoded-company-and-profile-id}@zooza.app`

When an email arrives, the system decodes the company ID and billing profile ID from the address and verifies the HMAC signature to prevent spoofing. This eliminates the shared-IBAN ambiguity of the legacy email approach.

**Supported banks:** Tatra Banka, VÚB, SLSP, UniCredit, Prima Banka, FIO (SK), ČSOB (SK+CZ), Raiffeisenbank CZ, FIO CZ, Komerční banka CZ. Each has a bank-specific parser for its email format.

### Bank email (legacy, IBAN-based)

Older integration: bank email arrives at a generic address; the system identifies the company by matching the beneficiary IBAN against `companies`, `courses`, and `invoice_profiles` tables (in that order, first match wins).

**Known limitation:** Two companies sharing the same IBAN causes misassignment. The encoded email system was introduced to solve this.

### CSV import

Maximum 100 rows per import. Each row is deduplicated by SHA-256 hash of immutable fields (`posting_date`, `amount`, `currency`, `payers_iban`, `information_for_beneficiary`). Duplicate hashes are silently skipped.

---

## Parsing and normalisation

Regardless of source, every payment is normalised to the same fields:

| Field | Notes |
|-------|-------|
| IBAN (beneficiary) | Normalised — no spaces, standard country prefix |
| Amount | Always stored as positive float; handles comma decimals and non-breaking spaces |
| Payer's IBAN | Normalised |
| Variable symbol | Extracted from dedicated field → structured remittance info → free-text scan for numeric sequences |
| Note | Raw payment description |
| Transaction ID | Required for deduplication; a payment without one is rejected |
| Company ID | From integration context (GoCardless) or decoded from email address |

---

## Pairing algorithm (6 steps, deterministic)

The pairer runs before the LLM. Its job is to find a candidate order. It does not record a payment — it only proposes a match.

### Step 1: Assign to company

Already handled during ingestion (GoCardless, encoded email, IBAN lookup). If company assignment fails, the payment is discarded entirely.

### Step 2: Duplicate check

If a payment with the same `transaction_id` + `provider` already exists, the new one is rejected as a duplicate before saving.

### Step 3: Match by variable symbol → registration

Look up a registration by the variable symbol (= order/registration ID). If found, proceed to candidate validation (step 6).

### Step 4: Match by variable symbol → product order

If no registration found, look up a product order with the same ID. If found, proceed to candidate validation.

### Step 5: Match by custom customer ID

If neither registration nor product order matched, try treating the variable symbol as a custom customer ID:

1. Find a user whose `custom_customer_id` matches the variable symbol (minimum 3 characters; if numeric, must be > 0).
2. Load up to 100 active registrations (status: registered or pre-registered) for that user, newest first.
3. Resolve delegation chains for each (see below).
4. Deduplicate resolved candidates.
5. Validate each with **strict rules** (see step 6). First valid candidate wins.

This path is less certain than direct variable symbol matching, so validation is stricter.

### Step 6: Candidate validation

| Check | Rule | On failure |
|-------|------|------------|
| Order status | Registration: must be `registered` or `trial`. Order: must not be `deleted`. | Reject candidate |
| Payment status (direct match) | Must be: paid, overpaid, or awaiting_payment | Continue (lenient) |
| Payment status (customer ID match) | Must be: unpaid, partially_paid, downpayment variants, final_payment variants, no_debt, awaiting_payment | Reject immediately |
| Schedule end date | If schedule ended > 3 months ago | Reject candidate |
| Amount vs balance | Payment larger than balance | Flagged (may still pass) |

The stricter payment status rules for customer ID matching exist because the match is less certain — a broad accept list would cause false pairings.

---

## Payment delegation chains

Some registrations have `payments_managed_by` set — they delegate payment management to another registration. Example: a family registration that handles payment for multiple child registrations.

When a candidate registration is found, the system follows the chain:

```
Reg A (payments_managed_by → Reg B) → Reg B (payments_managed_by → Reg C) → Reg C (self-managed)
```

The payment is paired to the terminal node (Reg C). Safety limits:
- Maximum chain depth: 10.
- Circular reference detection: if the chain loops, the candidate is rejected.
- If any registration in the chain cannot be loaded, the candidate is rejected.

---

## Ignore filters (deterministic, pre-LLM)

Filters run **before** the LLM call. If a filter matches, the payment is immediately set to `ignore` and the LLM is not called (saves cost).

**A filter matches when:**
- Payer's IBAN matches exactly (required), AND
- Note regex matches (optional)

Both conditions must hold if the regex is set.

**Safeguards — a filter is automatically deactivated if:**
- It would match > 30% of all payments in the last 90 days (too broad), OR
- It would block > 50% of already-paired payments (catching real Zooza payments), OR
- It accumulates 3 or more false positives (user pairs a payment the filter ignores)

**False positive tracking:** When a user manually pairs a payment that was filtered-ignored, the filter's false positive counter increments. At 3, the filter deactivates. This prevents overly aggressive filters from silently blocking real payments.

Maximum 50 active filters per company.

---

## LLM evaluation

### Purpose

The LLM has two jobs:
1. **Duplicate detection** (primary) — identify if the same payment has already been processed.
2. **Pairing confirmation** (secondary) — when the pairer found a match, confirm it; when it didn't, flag for manual review.

The LLM is not a replacement for the pairer. The pairer handles the majority. The LLM adds a safety layer.

### Context the LLM receives (7 sections)

| Section | Content |
|---------|---------|
| **1. Incoming payment** | ID, amount, currency, date, payer IBAN, note, variable symbol, origin, pairer's suggestion |
| **2. Candidate** | If found: customer name, course/product name, status, payment status, balance, debt, payment schedule details. If not found: "No candidate found." |
| **3. Money received** | All real payments already recorded on the candidate (last 12 months). Credit-type transactions only: credit, credit_via_transfer, direct_debit, stripe, cardpay. Per entry: date, amount, type, source IBAN, note. |
| **4. Other registrations** | Up to 10 other registrations for the same customer: ID, course, status, balance, payment plan. Helps spot if the payment belongs to a different booking. |
| **5. Other unpaired payments** | Up to 10 other unpaired payments at this company: ID, amount, payer IBAN, variable symbol, status, date, note. Critical for spotting duplicates. |
| **6. Past overrides** | Last 5 user corrections of LLM decisions for this customer: what the LLM decided, what the user chose instead, their note. Lets the LLM learn from past mistakes per customer. |
| **7. Rules** | Global system rules + company-specific rules, grouped by type (dedup, ignore, pairing). Written in natural language. Company rules override system rules when conflicting. |

### Decision outputs

| Decision | When | Confidence threshold |
|----------|------|---------------------|
| `pair` | Payment belongs to the candidate. No duplicate evidence. | ≥ 0.85 (≥ 0.90 when variable symbol matches directly) |
| `ignore` | Duplicate of an already-processed payment — LLM identifies which. | ≥ 0.80 |
| `manual` | Ambiguous, multiple possible targets, low confidence. | < 0.80 |

**Core principle — trust the pairer:** When the pairer says "pair" and there is no duplicate evidence, the LLM confirms with "pair". The LLM does not second-guess the pairer's order selection (the pairer is deterministic and more reliable). The LLM's main job in the "pair" case is to check there is no duplicate.

**Duplicate heuristics:** A payment is likely a duplicate when Section 3 (Money Received) or Section 5 (Unpaired Payments) shows a payment with same/similar amount + same payer IBAN arriving within a short window for the same order.

### What happens after the LLM decides

**`pair`:**
- The pairer's matched order ID is used (not the LLM's, in case they differ — the pairer is more reliable for order selection).
- `pair_payment()` is called to create the ledger entry.
- On success → status `paired`. On failure (e.g. booking deleted in the meantime) → status `new`.

**`ignore`:** Status set to `ignore`. The `duplicate_of` field records which payment this duplicates.

**`manual`:** Status set to `new`. Appears in the manual review dashboard.

### Fallback (LLM unavailable)

If the LLM times out, fails, or returns an invalid response:
- If the pairer had a suggested match: fall back to pairer → auto-pair.
- Otherwise: status `new`.

If AI is disabled at the company level, the pairer's result is used directly without any LLM call.

There is no scenario where a payment gets permanently stuck — every path ends in auto-pair or manual review.

---

## Payment acceptance — what gets written to the ledger

When a payment is accepted (automatically or manually), these things happen:

1. A new `payments` table entry is created:
   - Transaction type: `credit_via_transfer`
   - Payment method: `transfer`
   - Original amount, payer IBAN, and note from the inbound payment
   - Origin: `inbound`

2. The registration/order's payment status is recalculated.

3. If fully paid and auto-invoice is enabled → invoice is generated.

4. Payment confirmation email sent to client (if configured).

5. Inbound payment record updated: status `paired`, `payment_id` set, `paired_automatically` flag set.

Once paired, the inbound payment record no longer appears in the unpaired view. The `payments` table entry represents it everywhere (registration detail, reports, exports).

---

## Automatic filter creation (LLM-assisted)

When a user ignores a payment and requests a filter, the LLM designs the filter:

1. Input to LLM: ignored payment details (IBAN, note, amount, variable symbol) + existing active filters.
2. LLM outputs: IBAN pattern (exact) + optional note regex (extracted from the note — e.g. "IKEA" from "IKEA BRATISLAVA NAKUP 12345").
3. LLM rejects filter creation if: the payment looks like a legitimate order payment (has a valid variable symbol) OR an existing filter already covers it.
4. System validates coverage before activating (same 30%/50% limits as all filters).

**What the LLM is told NOT to put in filter patterns:** variable symbols, transaction IDs, dates, amounts. These change per transaction and would make filters brittle or too narrow.

---

## Business rules — context and format

Rules are natural language text included verbatim in the LLM's context (Section 7). They do not require regex or code — they are plain instructions.

**Scope:** System rules (global, apply to all companies) can be overridden by company rules. When conflicting, company rules win.

**Types:**

| Type | What it affects | Example |
|------|----------------|---------|
| `dedup` | Duplicate detection logic | "Payments from IBAN SK12... arriving within 3 days with the same amount are duplicates." |
| `ignore` | When to ignore regardless of match | "All payments from IBAN CZ98... are rent — ignore." |
| `pairing` | How to match | "Variable symbols starting with 9 are product orders, not course registrations." |

Maximum 10 active rules per company. Rules take effect immediately on the next payment — no restart required.

---

## Common support scenarios

**"Why was this payment not paired automatically?"**

Work through this checklist:
1. Did the client use the correct reference number? Open the inbound payment and check the variable symbol field.
2. Was the booking active when the payment arrived? Cancelled or deleted bookings cannot receive payments.
3. Did the payment schedule expire more than 3 months ago? The validator rejects these.
4. Is the amount larger than the balance? This triggers extra scrutiny.
5. Did an ignore filter match by accident? Check the `ignore` status reason.
6. Has the GoCardless consent expired? Check the connected accounts page.

**"A client paid twice by mistake — how do I handle the duplicate?"**

The LLM should catch duplicates automatically. If it didn't (e.g. the payments arrived too far apart), manually ignore the duplicate inbound payment. If the duplicate was already paired and recorded, you need to issue a refund or credit via the booking's payment section.

**"Payments from a known non-client keep appearing"**

Create an ignore filter. Either trigger it by ignoring one payment and clicking "Create filter", or create it manually in Settings → Payments → Inbound Payments → Ignore Filters. Use the exact payer IBAN plus a note pattern if needed.

**"A payment was incorrectly ignored by a filter"**

Manually pair the payment from the manual review queue (status `New`). Each time you do this, the filter's false positive counter increments. After 3, the filter is automatically deactivated.

**"The LLM paired to the wrong registration"**

This should be rare when variable symbols are used correctly. If it happens:
- Manually correct the pairing from the booking detail.
- Add a business rule that explains the pattern to prevent recurrence.
- The correction is logged in the override history and included in future LLM context for this customer.

---

## Related

- [Inbound payments — setup and pairing](../guides/inbound-payments.md) — admin-facing guide
- [Payments and Billing FAQ](../faq/payments-and-billing-faq.md)
- [Billing and invoicing](../setup/billing-and-invoicing.md) — billing profiles and IBAN
