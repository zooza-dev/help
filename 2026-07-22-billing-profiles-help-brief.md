# Help writing brief — Billing profiles & bank accounts (invoice-profile model rebuild)

**Trigger:** merged to `main` 2026-07-21 (commits `34529c6a` → `e14ab75e`, ~113 commits / 160 files).
This is the largest billing change Zooza has shipped — it replaces the whole "invoice profile"
model. Expect a multi-article release, not a single guide.

**Repo layout:** api-v1 is at `../api-v1/` from this repo. All paths below are relative to `../api-v1/`.

**Audience:** owners/admins of companies that invoice — especially **multi-entity** accounts
(more than one legal entity / IBAN under one Zooza company) and anyone using inbound bank-statement
pairing or GoCardless bank data.

---

## What changed, in one paragraph (for orientation — do not copy into an article)

An "invoice profile" used to be a single row carrying a legal identity *and* one IBAN, picked by
seven different inconsistent cascades depending on which screen you were on. It is now split in two:
a **billing profile** (the legal entity — name, address, tax IDs, invoice engine) which can own
**several bank accounts** (IBAN/SWIFT/holder, each optionally bound to a statement feed). One
resolver decides which profile applies everywhere — invoicing, payment instructions in emails,
the widget, inbound pairing and reporting all now agree. Overrides can be set at
schedule / course / registration / product / order level, with explicit inherit-vs-override
semantics. Two new reports appear: **per-profile Issued/Received** and an **attribution
discrepancy report** with correction actions.

---

## Read these, in this order

### Tier 1 — required, the core model (read fully)

| File | What you get from it |
|---|---|
| `specs/implemented/2026-07-06-invoice-billing-model-build-shadow.md` | API-20260706-001. The new model: `billing_profiles`, `bank_accounts`, override columns, the resolver, the received-stamp. **Implemented.** Mostly internal — read for vocabulary, not for user copy. |
| `specs/implemented/2026-07-06-invoice-billing-model-cutover.md` | API-20260706-002. **The most important file for you.** This is where all user-visible behaviour lands: what resolves where, the two intended behaviour changes, per-profile reporting, discrepancy report + re-attribution. **Implemented.** |
| `handoffs/outbox/2026-07-06-api-v1-to-app-billing-profiles-rebuild.md` | Status `agreed`. Describes the **UI as agreed with the app team** — profile/account management, override pickers, reporting screens, discrepancy screen. Closest thing to a screen inventory. |

### Tier 2 — required for full coverage

| File | What you get from it |
|---|---|
| `specs/specs/2026-07-11-multi-entity-attribution-lifecycle.md` | The multi-entity story: the three attributions (Received / Issued / Resolved), the predictive discrepancy report, and the correction toolkit gated by the invoice "freeze ratchet". Ships **with** the rebuild, same branch. Explains *why* an admin would ever see a discrepancy. |
| `specs/implemented/2026-07-09-account-level-statement-source.md` | API-20260709-001. Inbound bank-statement email parsing moved from profile → **bank account**. Each account gets its own `inbound_email` + statement source (`bank_email` / `gc_bank_data` / none). **Implemented.** Directly affects the inbound-payments setup guide. |
| `handoffs/outbox/2026-07-11-api-v1-to-app-multi-entity-attribution-lifecycle.md` | App-side UI agreement for the attribution/correction screens. |

### Tier 3 — context / do NOT document yet

| File | Why |
|---|---|
| `specs/in_progress/2026-07-10-gc-bank-data-on-bank-accounts-decommission-legacy-table.md` | GoCardless bank-data feed moves onto `bank_accounts`. **`in_progress`** — behaviour change: a GC authorisation now activates the feed on the account that already holds that IBAN, under its existing profile, instead of moving it. Affects `guides/gocardless-connection-lifecycle.md`. Hold until implemented. |
| `specs/specs/2026-07-15-billing-migration-ops.md` | API-20260715-001. Fleet migration tooling (preflight, chunked backfill, `billing_migrate`, self-driving cron). **Internal ops only — nothing user-facing. Do not write an article.** Read only to understand *why* companies switch over on different dates. |
| `specs/specs/2026-07-06-invoice-billing-model-decommission.md` | API-20260706-003, Phase 3. Purely internal drops + renames, **not started**. No user impact ever. Ignore. |

### Tier 4 — reference material (grep, don't read cover to cover)

| File | Use for |
|---|---|
| `docs/domain/invoice-profiles.md` | The invariants — what must be true regardless of implementation. Good source for glossary entries. |
| `docs/domain/invoicing.md`, `docs/domain/payments-core.md`, `docs/domain/inbound-payments.md` | Surrounding subsystems these articles must stay consistent with. |
| `docs/test-coverage/billing-profiles-bank-accounts-crud.md` | Exact CRUD rules and validation messages for profiles/accounts. |
| `docs/test-coverage/billing-overrides-nested.md` | Override/inherit behaviour, including the sticky-across-moves rule. |
| `docs/test-coverage/billing-reports-per-profile.md` | What the Issued/Received report actually contains. |
| `docs/test-coverage/billing-discrepancies-reattribution.md` | Every discrepancy type and every correction action. |
| `docs/test-coverage/billing-invoicing-repoint.md`, `billing-display-widget-repoint.md`, `billing-pairing-gc-repoint.md` | Per-consumer behaviour after cutover — what changed on invoices, in emails/widget, in pairing. |
| `postman/collections/billing-profiles-bank-accounts.postman_collection.json` | Exact field names/shapes (profile + account). |
| `postman/collections/billing-overrides-nested.postman_collection.json` | Where override pickers live in the API. |
| `postman/collections/billing-reports-per-profile.postman_collection.json` | Report parameters and output. |
| `postman/collections/billing-discrepancies-reattribution.postman_collection.json` | Discrepancy + re-attribution payloads. |

**Endpoints** (for the reference section): `billing_profiles.php`, `billing_reports.php`,
`billing_discrepancies.php`, and the override fields added to `courses.php`, `schedules.php`,
`registrations.php`, `products.php`, `orders.php`.

**New error keys** users may hit (all localised by the API):
`iban_already_used_by_profile`, `billing_resolver_not_reconciled`,
`cannot_delete_default_bank_account`, `cannot_delete_default_profile`.

---

## Proposed articles

### 1. `content/setup/billing-profiles-and-bank-accounts.md` — **new, the main setup guide**
The new model end to end: profile = legal entity, account = IBAN; create/edit a profile; add several
accounts to one profile; pick a default account; bind a statement source to an account. Include the
**duplicate-IBAN rule**: the same IBAN cannot sit on two profiles in one company — new writes are
rejected; pre-existing duplicates are grandfathered and shown in the discrepancy report.
Include: you cannot delete the default profile or a profile's default account.

### 2. `content/guides/billing-profile-overrides.md` — **new**
Which profile applies where, and how to override it. Cover: unset = **inherit** (and the UI shows
the inherited value and where it comes from); set = **explicit override**, which is **sticky** —
moving a booking to another class does **not** clear it. Cover the levels: programme / class /
booking, plus product / order for e-commerce. Cover the exception: a booking whose payments are
managed by another booking cannot hold its own override.

### 3. `content/guides/billing-per-profile-reports.md` — **new**
The **Issued** (invoiced turnover, net + gross) and **Received** (cash) reports per profile per
period. **Critical caveat to state plainly:** Received data exists only from *that company's
switchover date* onward — there is no history before it. The article must show where the reporting
start date is displayed rather than implying full history.

### 4. `content/guides/billing-discrepancies.md` — **new**
For multi-entity accounts only. Explain the three attributions in plain language — where the money
landed, where the turnover was declared, where the booking resolves today — and what a mismatch
means. Then the corrections: re-attribute a payment, regenerate an invoice on another profile,
split a bulk payment, acknowledge/dismiss. Explain that available actions **narrow once an invoice
is frozen** (issued/exported/period closed). State clearly that single-entity companies never see
this screen.

### 5. `content/setup/inbound-payments-setup.md` — **update**
The statement-source binding moved from profile to **bank account**. Each account now has its own
inbound email address and its own source. Rework the setup steps and the screenshots.

### 6. `content/setup/billing-and-invoicing.md` + `content/setup/invoicing-overview.md` — **update**
Replace "invoice profile" terminology, point at the new guides, and reflect that invoicing now uses
the resolved profile everywhere.

### 7. `content/faq/payments-and-billing-faq.md` — **update / extend**
Q&A for the migration questions: why does my invoice now show a different entity; why did the IBAN
in a payment email change; why can't I reuse this IBAN; why does Received start in July; my booking
is paid by a sibling booking, why is there no profile picker.

### 8. `content/glossary/` — **update**
Retire "invoice profile" as the primary term; add **billing profile** and **bank account**.
Keep "invoice profile" as an alias with a redirect (see `content/_redirects.yml`).

### 9. `content/guides/gocardless-connection-lifecycle.md` — **hold**
Will need updating when the GC decommission (Tier 3) lands. Add a `<!-- REVIEW -->` marker now.

---

## The two intended behaviour changes — must be documented, users will notice

Both are in `2026-07-06-invoice-billing-model-cutover.md`. Do not bury them.

1. **Managed payments follow the payer.** When a booking's payments are managed by another booking,
   invoicing and payment instructions now resolve under the *paying* booking's profile. Previously
   these could diverge.
2. **Product profile now wins everywhere.** Until now the booking widget honoured a product's
   invoice profile but invoicing quietly used the company default. After switchover the product's
   profile is used for invoicing too.

Neither is a bug fix users requested — frame them as "these now agree", and note that every affected
company was enumerated and reconciled before switchover.

---

## Rollout framing — important for tone

Companies do **not** all switch on the same day. Each company is migrated individually and only once
its data reconciles clean, driven by the ops tooling in API-20260715-001. Articles should avoid
"from version X" phrasing and instead say "once your account has been switched to the new billing
model" — and point at where the switchover date is visible (the reporting start date).

---

## Screenshot shot-list (Michal to paste)
1. Settings → **Billing profiles** list (multi-entity company, 2+ profiles).
2. **Profile detail** — identity fields + its list of bank accounts, default marked.
3. **Add / edit bank account** form (IBAN, SWIFT, holder) + duplicate-IBAN rejection message.
4. **Statement source** picker on an account (bank email / GoCardless) + the account's inbound email address.
5. Class (or programme) settings → **billing profile picker showing an inherited value** and where it's inherited from.
6. The same picker with an **explicit override** set.
7. **Issued** report per profile, with the reporting start date visible.
8. **Received** report per profile.
9. **Discrepancy report** list with at least one mismatch row.
10. A **re-attribution / correction** dialog.
11. Booking with managed payments — picker **absent** (for the FAQ answer).

---

## Decision rules applied
- **Document now:** API-20260706-001 (vocabulary only), **-002** (the substance), API-20260709-001,
  and API-20260711 multi-entity attribution — all implemented and merged to `main`.
- **Defer:** API-20260710-001 (GoCardless decommission, `in_progress`) — behaviour change not live.
- **Never document:** API-20260706-003 (Phase 3, internal) and API-20260715-001 (ops tooling).
- **Verify before publish:** every screen named here lives in the **app**, agreed via handoff, not
  built by api-v1. Confirm actual labels and navigation against the live app before moving articles
  from `draft` → `published`. Mark every assumed label with `<!-- REVIEW -->`.
- **Terminology:** run `/audit-terminology` after drafting — "invoice profile" appears across many
  existing articles and must be swept consistently.

## State to stamp when published
Set `docs_version` + `docs_communicated` on:
- `specs/implemented/2026-07-06-invoice-billing-model-build-shadow.md`
- `specs/implemented/2026-07-06-invoice-billing-model-cutover.md`
- `specs/implemented/2026-07-09-account-level-statement-source.md`

(all three are currently empty)
