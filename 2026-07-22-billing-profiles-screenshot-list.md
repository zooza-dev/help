# Screenshot shot-list — invoice profiles & bank accounts rebuild

Derived from: `2026-07-22-billing-profiles-help-brief.md`, verified against what is **actually built**
in the app (`app` repo, `origin/main` @ 266bfa23, 2026-07-21) — not just what the API supports.

**Terminology in every caption and alt text: "invoice profile" and "bank account".**
Never "billing profile" — that is API/data-model naming only (agreed constraint, handoff
`api-v1-to-app-20260706-001`, Decision Summary).

---

## Prerequisites before shooting

- A **company armed for the new UI** — `billing_ui_v2` must be true (all UI-relevant consumers armed
  via `__zooza__ops.php?action=billing_resolver`). Otherwise every screen renders in legacy mode and
  the screenshots are worthless.
- The company must be **multi-entity**: 2+ invoice profiles, one of them with **2+ bank accounts**.
- Set up in advance:
  - one class (schedule) with an **explicit** invoice-profile override,
  - one programme (course) with **descendants that override** (so the downward-impact panel appears),
  - one case where the **profile and the bank account resolve at different levels**,
  - one booking whose payments are **managed by another booking**,
  - one bank account with the **email statement source**, one with **GoCardless**.

---

## A. Invoice profiles & bank accounts — `Settings → Invoice profiles` (`#settings/invoice_profiles`)

For article: `content/setup/billing-profiles-and-bank-accounts.md` (new) + updates to
`content/setup/billing-and-invoicing.md`.

| # | Shot | Must show |
|---|---|---|
| A1 | Invoice profiles **list** in v2 mode | 2+ profiles; no legacy IBAN/SWIFT columns |
| A2 | **Profile detail** with the Bank accounts card | identity fields + 2+ accounts, IBAN / SWIFT / holder, **default marker**, feed status per row |
| A3 | **Add / edit** a bank account (inline row open) | the three fields being edited |
| A4 | **Duplicate-IBAN rejection** toast | localized error, same IBAN already on another profile |
| A5 | **Set default** + delete-default rejection toast | "you must set another default first" case |
| A6 | **Per-account QR preview** | the QR shown for a chosen account, not the profile |
| A7 | *(optional)* profile with **no accounts** — empty state | the add action |

## B. Statement sources per account — `Payments → Inbound → Setup` (`#payments/inbound/setup`)

For article: `content/setup/inbound-payments-setup.md` (rework — the binding moved profile → account).

| # | Shot | Must show |
|---|---|---|
| B1 | Inbound hub in v2 — **account-oriented** list | accounts as rows, per-account Change toggle, link back to their profile |
| B2 | Statement source picker on **one account** | bank email vs GoCardless vs none |
| B3 | Account with **email source active** | the account's **own inbound email address** (per account, not per profile) |
| B4 | Account with **GoCardless feed** connected | feed status / reconnect action at account level |

> The existing shots `inbound-setup-current-setup.png` and `inbound-setup-cash-bank-transfer.png` show
> the old **per-profile** layout and must be re-shot.

## C. Which profile applies + overrides — the `billing_override_picker` (UI label "Invoice profile")

For article: `content/guides/billing-profile-overrides.md` (new). Mounted at three places.

| # | Shot | Must show |
|---|---|---|
| C1 | **Programme** settings → Invoicing card, **inherited** state | chain strip `Default profile → Programme`, "inherits ↑", outcome line naming the resolved profile and level |
| C2 | **Class** detail settings card, **explicit override** set | chain with the override row highlighted + "Reset to inherit" |
| C3 | Chain where **profile and bank account resolve at different levels** | two separate highlights — e.g. profile from the default, account from the programme |
| C4 | **Booking** payments panel with the picker | full chain Default → Programme → Class → Booking |
| C5 | **Downward impact** notice on a programme | "N classes and M bookings below use their own invoice profile" + the Reset action |
| C6 | Reset-descendants **confirm dialog** | the exact counts being reset |
| C7 | Booking with **managed payments** | static "billing follows {booking}" note, **no picker** — needed for the FAQ answer |
| C8 | *(optional)* classes list filtered to **own override** | the review filter result |
| C9 | *(if wired)* **warn + confirm** when switching profile with open debt | the warning text |

---

## Not shootable yet — do not plan articles around these

| Brief shot | Why |
|---|---|
| Issued report per profile | **Phase ③ reporting screens are not built in the app.** API endpoints exist; there is no screen. |
| Received report per profile | same |
| Discrepancy report list | **Phase ④ — app spec `APP-20260711-001` is status `spec`, unimplemented** (branch `feature-invoice-attribution` contains the spec only). |
| Re-attribution / correction dialog | same |

Consequence: brief articles **#3 (per-profile reports)** and **#4 (discrepancies)** are **held** until
the app ships phases ③/④. Everything else in the brief can be written now.
