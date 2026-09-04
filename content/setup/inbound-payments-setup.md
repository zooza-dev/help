---
title: "Set up how Zooza collects money from clients"
description: "The Inbound Payments Setup wizard configures which payment channels are active and connects bank statement reading for each bank account."
slug: "inbound-payments-setup"
type: "setup"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: ["inbound-payments", "setup", "gocardless", "stripe", "bank-transfer", "online-card", "direct-debit", "bank-statement"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-09-04"
related_articles: ["invoice-profiles-and-bank-accounts", "inbound-payments", "payment-pairing", "gocardless-connection-lifecycle", "billing-and-invoicing"]
---

# Set up how Zooza collects money from clients

The **Inbound Payments Setup** wizard configures three things at once:

1. Which payment channels (online card, direct debit, cash / bank transfer) are available and which are enabled by default on new programmes
2. Which providers are connected for each channel (Stripe, GoCardless, Tatra Banka, etc.)
3. How Zooza reads your bank statements for each bank account — so incoming bank transfers are automatically matched to bookings

> **Navigation:** Settings → Billing & Payments → Payment collection setup  
> **Permission:** Owner role (or assistant with `allow_assistant_to_manage_payments`)

---

## Current setup — what you see first

When you open **Settings → Billing & Payments → Payment collection setup**, the first screen shows your current configuration at a glance.

![Payment collection setup: the three payment channels, the reconciliation rule, and the per-account statement feed table](../../assets/images/payment-collection-setup.png)

![Inbound Payments Setup — current setup screen with the three channel tiles and bank statement status](../../assets/images/inbound-setup-current-setup.png)

The screen has two sections:

**Top — the three channels:**

| Tile | What it shows |
|---|---|
| **Online card payment** | Whether card payment is the default for new programmes, and a **Configure** button |
| **Direct debit** | Whether direct debit is the default for new programmes, and a **Configure** button |
| **Cash / bank transfer** | Whether cash is the default, plus a summary of how many accounts are connected |

**Bottom — bank statement reading, one row per bank account:**

> *Each bank account can read incoming payments from its statements. Set up a statement feed per account.*

![Bank statement reading table listing each bank account with its invoice profile, source and status](../../assets/images/inbound-bank-statement-reading-per-account.png)

The table lists every bank account in the company:

| Column | What it shows |
|---|---|
| `Account number (IBAN)` | The account the money arrives on |
| `Account holder name` | The name registered with the bank |
| `Invoice profile` | The legal entity this account belongs to — click through to the profile |
| `Source` | Which method reads this account's statements, or *Not collecting bank transfers* |
| `Status` | The connection state, e.g. **No statement feed** |

**This is per account, not per profile.** An entity with two IBANs has two rows and two independent connections — one can read via GoCardless while the other uses email notifications, or one may not be connected at all.

From here you can:
- Set or change the **source** on an account (GoCardless Bank Data or email notifications)
- Reconnect an expired GoCardless connection
- Open the account's invoice profile
- Re-run the full wizard tour

---

## Running the wizard for the first time

If no setup has been completed yet, clicking **Setup** in the Inbound menu launches the wizard automatically starting from the intro step.

### Step 1 — Intro

![Inbound setup wizard intro screen — "You can use every channel at once"](../../assets/images/inbound-setup-intro.png)

The intro explains the key concept: **all three channels can be active at the same time**. They are not mutually exclusive. Most companies use two or three simultaneously.

The on/off switches for each channel live on individual programme settings pages. What the wizard configures here are the **defaults for new programmes** — existing programmes are not changed.

Click **Start tour** to walk through each channel.

---

### Step 2 — Online card payment

![Inbound setup wizard — online card payment step showing providers and default toggle](../../assets/images/inbound-setup-online-card.png)

The online card step shows which card payment providers are available in your region:

| Provider | How it works |
|---|---|
| **CardPay — Tatra banka** | Managed by Zooza — no additional setup required (SK/CZ only) |
| **Stripe (via Zooza)** | Managed by Zooza — no additional setup required |
| **Stripe Connect** | Your own Stripe account — click **Open integration** to connect |

**Enable by default on new programmes** — when turned on, every new programme will have online card payment active from the start. You can always change this per programme later.

**Default provider for new programmes** — if multiple providers are connected, pick which one to use on new programmes by default.

Click **Next** to continue.

---

### Step 3 — Direct debit

![Inbound setup wizard — direct debit step showing GoCardless provider and default toggle](../../assets/images/inbound-setup-direct-debit.png)

Direct debit lets you collect payments on a schedule — the client signs a mandate once, and Zooza charges them automatically on the agreed dates. Payouts land in your merchant account on GoCardless's schedule.

**GoCardless** is the direct debit provider. Click **Open integration** to go through the GoCardless onboarding if you have not connected it yet.

**Enable by default on new programmes** — turn this on if most of your programmes use direct debit as the primary payment method.

Click **Next** to continue.

---

### Step 4 — Cash / bank transfer

![Inbound setup wizard — cash and bank transfer step with bank statement reading options](../../assets/images/inbound-setup-cash-bank-transfer.png)

This step covers both **cash paid in person** and **client bank transfers** — they share one toggle on each programme because from Zooza's perspective, both result in a payment you confirm manually or auto-reconcile from bank statements.

> **Important:** Cash and bank transfer cannot be turned on independently per programme — they use the same switch. If you enable "cash" on a programme, it covers both methods.

**Bank statement reading per bank account:**

Each bank account can read its statements via one of two methods:

| Method | Best for |
|---|---|
| **GoCardless Bank Data** | Widest coverage — 2,500+ European banks. Requires reconnection every ~90 days (PSD2). |
| **Email parser** | Faster notifications (per-transaction emails). Requires bank support. Supported banks: Tatra Banka, VÚB, SLSP, UniCredit, Prima Banka, FIO (SK), ČSOB (SK/CZ), Raiffeisenbank CZ, FIO CZ, Komerční banka CZ. |

To configure an account, click its row. You will be guided to:
1. Pick a method (GoCardless or email parser)
2. Select your bank
3. Complete the connection (OAuth flow for GoCardless, or forward your bank's notification emails to the address Zooza generates)

Each account gets **its own** email address for the parser, so a statement always identifies which IBAN it belongs to.

**Enable by default on new programmes** — turn this on if your clients primarily pay by bank transfer.

Click **Next** to finish.

---

### Step 5 — Done

![Inbound setup wizard — completion screen showing channel defaults summary](../../assets/images/inbound-setup-done.png)

The final screen confirms your channel defaults:

- Online card payment — default ON or OFF for new programmes
- Direct debit — default ON or OFF for new programmes
- Cash / bank transfer — default ON or OFF for new programmes

> **Existing programmes are not affected.** The defaults apply only to programmes created from this point forward. To change settings on an existing programme, go to the programme's settings page.

Click **Back to Inbound hub** to return to the Inbound section, or **Re-run wizard** to go through the steps again.

---

## Bank connection expiry warning on the dashboard

GoCardless Bank Data connections expire periodically — typically every 90 days under PSD2 rules. This applies to most European banks. When a connection is about to expire or has expired, **Zooza shows a warning banner on the main dashboard**.

![Dashboard warning banner — "Bank connection needs reconnection" with the affected account and a Reconnect button](../../assets/images/inbound-payments-setup-01.png)

The banner shows which bank connection needs attention and offers two actions:

- **Reconnect** — opens the GoCardless authorisation flow immediately to renew the connection
- **Open Inbound hub** — navigates to the Inbound setup screen where you can see every bank account and its connection status

> **Do not ignore this warning.** Once the connection expires, Zooza stops receiving new bank transactions. Payments will still arrive at your bank but will not be automatically matched to bookings until you reconnect.

To reconnect manually at any time (before the warning appears), go to **Settings → Billing & Payments → Payment collection setup** and reconnect the affected bank account in the **Bank statement reading** table.

---

## Frequently asked questions

**Does running the wizard again change my existing programme settings?**

No. The wizard only updates the **defaults for new programmes**. Re-running it does not touch any existing programme's payment configuration.

**Can I use multiple payment channels at the same time?**

Yes. All three channels can be active simultaneously. Most companies use a combination — for example, online card and bank transfer enabled by default, with direct debit enabled only on selected subscription programmes.

**What happens if I switch a bank account from GoCardless to email notifications?**

The previous GoCardless connection stays in place but stops being used for that account. You can switch back at any time. Each account has one active source at a time, and switching one account does not affect the others on the same invoice profile.

**My bank is not in the email parser list — what do I do?**

Use GoCardless Bank Data instead (it covers 2,500+ banks). If your bank supports email notifications and you would like Zooza to add a parser for it, contact support via the in-app chat.

---

## Related

- [Inbound payments — setup and pairing](../guides/inbound-payments.md) — how automatic payment matching works day to day
- [Inbound payments — technical reference](../reference/inbound-payments-internals.md) — algorithm details and AI evaluation
- [GoCardless direct debit mandates](../guides/gocardless-direct-debit-mandates.md) — collecting direct debits from clients (separate from bank reading)
- [Set up invoice profiles and bank accounts](./invoice-profiles-and-bank-accounts.md) — the entities and accounts these connections belong to
- [Billing and invoicing](./billing-and-invoicing.md) — invoice generation and numbering
