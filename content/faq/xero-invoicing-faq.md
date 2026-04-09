---
title: "Xero Integration FAQ"
description: "Yes. You can switch off automatic invoice generation so invoices are not sent to clients until your Xero settings (e."
slug: "xero-invoicing-faq"
type: "faq"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: ["invoices", "xero", "stripe", "reconciliation", "stripe-standard"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-12"
---

# Xero Integration FAQ

## Can I disable automatic invoice generation temporarily?

Yes. You can switch off automatic invoice generation so invoices are not sent to clients until your Xero settings (e.g., VAT rates) are fully configured. Clients will still receive payment confirmations.

## Can I generate invoices retroactively?

Yes. After you have finalized your Xero settings, you can go through existing bookings and generate invoices for all past payments. This allows you to launch bookings first and sort out invoicing later.

## My invoices show "tax exempt" — how do I fix VAT settings?

VAT rates are managed in your Xero account. Make sure the correct tax rate is set up in Xero, then re-sync the connection in Zooza under **Settings → Invoice Profiles**. After syncing, invoices will reflect the correct VAT rate.

## Where do I manage Xero connection settings?

Go to **Settings → Invoice Profiles** in Zooza. From there you can sync or re-sync your Xero connection and configure invoice settings.

## Do invoices get marked as paid automatically?

Zooza can automatically mark invoices as paid in Xero when the corresponding payment is received through Stripe. This feature needs to be enabled — contact support if it is not working on your account.

---

## Stripe + Xero reconciliation

### How do individual Zooza payments relate to what arrives in my bank account?

Stripe collects individual customer payments and pays them out to your bank in **bulk** (typically daily or weekly, after deducting fees). This creates a mismatch in Xero: many individual paid invoices, but one bulk bank transfer.

The correct way to handle this in Xero is with a **Stripe Clearing account**:

1. **Zooza → Xero:** Each payment creates an invoice in Xero and marks it as paid. The payment is credited to your *Stripe Clearing* account (not directly to your main bank account).
2. **Stripe → Bank:** When Stripe pays out, you record a bank transfer *from* the Stripe Clearing account *to* your main bank account.
3. **Result:** The Stripe Clearing account nets to zero after each payout. Any remaining balance = funds collected by Stripe but not yet paid out.

This means reconciliation happens at two levels:
- **Zooza / Xero** — individual customer payments, matched to invoices
- **Stripe payout summary** — what Stripe actually transferred to your bank (use this to reconcile the Stripe Clearing account against your bank statement)

### Where do I find the Stripe payout summary?

Go to your Stripe account → **Balance** section. For Stripe Standard accounts this is at [dashboard.stripe.com](https://dashboard.stripe.com) → **Balances**. The monthly payout summary shows total payouts and the period balance — use this to verify your Stripe Clearing account balance in Xero at month-end.

### What is the difference between Stripe Express and Stripe Standard?

Zooza supports both Stripe Express and Stripe Standard connections. The difference matters mainly for reporting access:

| | Stripe Express | Stripe Standard |
|---|---|---|
| Payment processing | ✓ | ✓ |
| Payout summary reports | Via Stripe Express dashboard | Via full Stripe dashboard |
| VAT invoices for Stripe fees | Limited (platform-dependent) | Available under Settings → Compliance and Documents |
| Recommended for | Simple setups | Companies needing full reporting and VAT invoices for fees |

If your accountant needs VAT invoices for Stripe processing fees, use **Stripe Standard**. To switch, disconnect the current Stripe connection in Zooza (**Settings → Integrations → Stripe**) and reconnect with your Standard account.

### The invoice date in Xero doesn't match the booking date — is that correct?

Yes, this is by design. Zooza generates invoices based on the **payment received date**, not the booking creation date. If a payment was received in December but the invoice was generated in January, the invoice date will be in January with a December payment date. You can adjust the invoice date manually in Xero if needed.

### Will I get duplicate receipts if Xero also pulls a bank or Stripe feed?

This depends on how the bank account is configured in your Invoice Profile. If set up correctly, there are no duplicates — but you need to understand the two-layer flow:

**Layer 1 — Zooza payment sync (individual level):**
Each customer payment → Zooza creates a paid invoice in Xero → payment credited to your **Stripe Clearing account** in Xero (not your main bank account directly).

**Layer 2 — Bank feed or Stripe payout (bulk level):**
Stripe pays out to your bank in bulk → your bank feed (or manual entry) records one bulk transfer → you match this to the **Stripe Clearing account** in Xero, not to individual invoices.

**Result:** No duplication. The two layers work at different levels — individual invoices vs. bulk payouts — and are reconciled against the same clearing account from opposite sides.

**What causes duplication:**
Duplication occurs if you also connect Stripe directly as a bank account feed in Xero and let it import individual Stripe transactions. This creates the same transactions twice — once from Zooza, once from the Stripe feed. **If you use Zooza's payment sync, do not connect Stripe as a separate bank feed in Xero.**

### Should I use Zooza payment sync or Xero's bank feed — which is the source of truth?

Use one approach, not both:

**Option A — Zooza as source of truth (recommended for most companies)**
- Zooza reports each payment to Xero in real time and marks invoices as paid.
- Your bank feed (Stripe or bank) reconciles bulk payouts against the Stripe Clearing account.
- Zooza + Xero = individual invoice records. Bank feed = payout verification only.
- Best for: companies that want client-level payment tracking and automatic reconciliation.

**Option B — Xero bank feed as source of truth**
- Payments flow into Xero via Stripe or bank feed directly.
- Invoices are matched to bank transactions manually in Xero.
- Zooza payment sync is turned off or not used.
- Best for: companies with an existing Xero workflow they don't want to change.

Most companies using Zooza + Xero use Option A. It keeps client payment data, booking status, and accounting in sync automatically.
