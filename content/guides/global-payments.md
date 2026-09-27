---
title: "Accept card payments with Global Payments"
description: "Connect one or more Global Payments merchant accounts and decide which billing profile bills through which account, so the money lands in the entity that issued the invoice."
slug: "global-payments"
type: "guides"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: ["global-payments", "card-payments", "payment-gateway", "billing-profile", "integrations", "refunds"]
status: "published"
related_articles: ["integrations-hub", "invoice-profiles-and-bank-accounts", "price-and-payment-setup", "stripe-payments-faq", "offline-charge-manual-push"]
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: true
last_converted: "2026-09-27"
---

# Accept card payments with Global Payments

**Global Payments** is a card gateway you can use instead of, or alongside,
Stripe. It is available to companies in the **EU and EEA**.

What makes it different from every other gateway in Zooza: you can connect
**several merchant accounts** and say which one each billing profile bills
through. A company that invoices under two legal entities can settle each
entity's card payments into that entity's own merchant account.

## Connect an account

Go to **Settings → Integrations → Global Payments**. The page has two cards:
**Connections** and **Billing profile routing**.

In **Connections**, add a connection with three things:

| Field | What to enter |
|---|---|
| **Label** | Your own name for this merchant account — it is what you will pick from in the routing table, so name it after the entity or the site, not "GP 1". |
| **App ID** | From Global Payments. |
| **App Key** | From Global Payments. |

Zooza validates the credentials against Global Payments as you save, so a typo
fails immediately rather than at the first real payment.

Once saved:

- The **App ID is masked** and the **App Key is never shown again**. Keep your
  own copy. To change a key later, use **rotate** — it replaces the key without
  disturbing anything the connection is already doing.
- The row shows the merchant id, the connection's status, when it was last
  validated, and the last error if validation failed. **Re-validate** re-checks
  it on demand.
- **The first connection you add becomes the fallback** automatically.

## Route billing profiles to accounts

The **Billing profile routing** card lists every billing profile with a
connection to bill through. Leave a profile unset and it uses the fallback.

This is the part worth understanding properly, because the two halves are
decided separately:

- The **billing profile** decides **who issues the invoice**.
- The **Global Payments connection** decides **which merchant account receives
  the money**.

Nothing forces them to agree. A profile you never mapped quietly bills through
the fallback, so a multi-entity company can end up invoicing from one entity and
settling into another — legally messy, and invisible unless you look. Zooza
therefore shows the routing rather than blocking it: every row names its
**effective account**, and a profile reached through the fallback says so instead
of showing a blank you have to interpret.

Check the whole table after you add a second merchant account. That is the moment
a routing that used to be trivially correct stops being so.

### Rebinding a profile does not move existing cards

A stored card belongs to the merchant account that captured it, and so does a
scheduled instalment already armed against it. Point a billing profile at a
different connection and **new** payments follow the new account; saved cards and
instalments already in flight stay with the old one. Zooza warns you when the
connection you are moving away from is still in use.

## Where you see the chosen account

On a programme's or product's price card, the online-card section names the
merchant account that will actually receive the money and the invoice profile
that decided it. If that account was reached by fallback while other accounts
exist, it says so as a warning and names the reason — this is the case worth
catching before you take payments, not after.

With a single connection the notice is suppressed: there is nothing to get wrong.

The **Integrations** hub shows Global Payments with a **connection count** rather
than a connected/not-connected badge, because "connected" is not a yes or no
once a company runs several merchant accounts.

## Refunds

Refunds through Global Payments work from the booking's payments screen in the
same way as any other provider.

## Deleting a connection

Zooza refuses to delete a connection that is still the fallback or still has
billing profiles bound to it. Move the profiles first and nominate a different
fallback, then delete.

## Related

- [Integrations hub](../setup/integrations-hub.md) — every integration and its status
- [Invoice profiles and bank accounts](../setup/invoice-profiles-and-bank-accounts.md) — what a billing profile decides
- [Price and payment setup](price-and-payment-setup.md) — choosing the payment method on a programme
- [Automatic charges and the manual push](../troubleshooting/offline-charge-manual-push.md) — what happened on a scheduled charge
