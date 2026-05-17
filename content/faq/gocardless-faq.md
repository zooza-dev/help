---
title: "GoCardless Integration FAQ"
description: "Open the booking detail and scroll to the Payments tile. Click Show payments to expand it."
slug: "gocardless-faq"
type: "faq"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: ["gocardless", "direct-debit", "mandate", "offline-charge", "payment-matching"]
status: "published"
related_articles: ["gocardless-direct-debit-mandates", "offline-charge-manual-push", "email-payment-notifications"]
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-05-13"
---

# GoCardless Integration FAQ

## How do I check if a client has an active GoCardless mandate?

Open the booking detail and scroll to the **Payments** tile. Click **Show payments** to expand it. In the payment section, look for the **SEPA Direct Debit** tile. It shows:

- **Active** — Yes or No
- **Mandate ID** — the unique GoCardless mandate reference
- **Provider** — GoCardless

If the SEPA Direct Debit tile shows **Active: Yes**, the mandate is in place and direct debits will be collected automatically according to the payment schedule.

If the tile is missing or shows **Active: No**, the client has not yet completed the GoCardless authorization flow (or the mandate was cancelled). In that case, the client needs to re-authorize via their Client Profile.

## How does GoCardless bank connection work with Zooza?

GoCardless is a third-party service that connects your bank account to Zooza. Once connected, GoCardless automatically reads incoming transactions from your bank and sends them to Zooza for payment matching.

To set it up:

1. Go to **Settings → Billing profiles**.
2. Open your default billing profile.
3. Click the logo of your bank to initiate the GoCardless connection.
4. You will be redirected to your internet banking, where you authorize GoCardless to access your account.

After authorization, incoming payments are automatically forwarded to Zooza and matched against bookings using the variable symbol.

## Why did my GoCardless connection expire?

For security reasons, banks limit GoCardless connections to approximately **90 days**. After this period, your bank stops sending transaction data to GoCardless, and Zooza can no longer automatically match payments.

You will receive an email notification from Zooza before your connection expires. If you miss the renewal window, payments will stop appearing in Zooza until you reconnect.

## How do I renew an expired GoCardless connection?

1. Log in to your **internet banking**.
2. Find the GoCardless connection in your account settings (the exact location depends on your bank).
3. Re-authorize the connection.

Alternatively, you can initiate the reconnection from Zooza:

1. Go to **Settings → Billing profiles**.
2. Open your default billing profile.
3. Click your bank logo to start the authorization flow again.

After renewal, the 90-day countdown restarts.

## What are the options for automatic payment matching?

Zooza supports three methods for matching bank payments to bookings:

| Feature | GoCardless | Email notification | CSV import |
|---|---|---|---|
| **How it works** | Reads transactions from your bank via API | Bank emails Zooza for each incoming payment | You upload a bank statement export manually |
| **Sync speed** | Once per day | Near real-time (minutes) | Manual — whenever you run the import |
| **Renewal required** | Yes, every 90 days | No | No |
| **Bank compatibility** | Depends on GoCardless support | Any bank with email notifications | Any bank that exports CSV statements |
| **Best for** | Ongoing automation | Ongoing automation (faster) | Catching up after outages, or banks with no live integration |

For most users, **email-notification pairing** is the best combination of speed and low maintenance. **CSV import** is useful as a fallback when automatic methods are unavailable or when you need to import payments from a specific past period.

## What is the difference between GoCardless pairing and email-notification pairing?

See the comparison table in the question above. In summary:

- GoCardless syncs once per day and requires re-authorization every 90 days.
- Email-notification pairing is near real-time and works indefinitely without renewal.
- Both are fully automatic once configured.

When using email notifications, your bank sends payment emails to the Zooza-generated address instead of your personal inbox.

## Which banks have known issues with GoCardless?

No banks have known ongoing issues with GoCardless at this time.

If you notice payments are not arriving in Zooza, first check your GoCardless connection status in your internet banking before contacting support.

## How do I set up email-notification payment matching?

For the full step-by-step setup, see [Email-notification payment matching](../setup/email-payment-notifications.md).

In summary:

1. Go to **Settings → Billing** → open the billing profile → **Edit**.
2. Fill in your **IBAN** and select your bank from the dropdown.
3. Zooza generates a unique notification email address for your profile.
4. In your internet banking, set the email for incoming payment notifications to the Zooza-generated address.

If your bank is not in the dropdown, see [My bank is not in the list](../setup/email-payment-notifications.md#my-bank-is-not-in-the-list).

## How do I switch from GoCardless to email-notification pairing?

1. **Remove the GoCardless connection** in your internet banking to prevent duplicate transactions once both methods are active.
2. Go to **Settings → Billing** → open your billing profile → **Edit** → select your bank and save.
3. **Copy the Zooza-generated notification email address** shown in the billing profile settings.
4. **Set up email notifications** in your internet banking — configure your bank to send incoming payment notifications to the Zooza-generated address.
5. **Monitor the first payment** to confirm transactions are arriving in Zooza correctly.

After switching, you no longer need to renew any connection every 90 days. Payment notification emails from your bank will no longer arrive in your personal inbox — they are routed directly to Zooza instead.

For full setup details, see [Email-notification payment matching](../setup/email-payment-notifications.md).

## Why are payments not auto-matching even though GoCardless is connected?

There are several possible causes:

- **Expired connection.** Your 90-day GoCardless authorization has lapsed. Check the connection status in your internet banking and renew it.
- **Bank-side issue.** Your bank may have a temporary outage or technical problem with the GoCardless API. Contact support if the issue persists.
- **Incorrect account pairing.** The GoCardless connection may not have linked to the correct bank account. Verify in your internet banking that GoCardless is connected to the same account as your Zooza billing profile IBAN.
- **Variable symbol in a non-standard field.** Some banks (e.g., Revolut) place the variable symbol in the "Reference" field rather than the standard variable-symbol field. Zooza checks the reference/note fields as well, but edge cases may still occur.
- **Payment arrived before the debt was created.** If a client pays before Zooza generates the instalment, there is no debt to match against. The payment will remain unmatched until a corresponding debt exists.

If none of the above applies, contact Zooza support with the specific transaction details (variable symbol, amount, date) so the team can investigate.

## How often does GoCardless sync transactions?

GoCardless typically syncs transactions **once per day**. This means there can be a delay of up to 24 hours between when a payment arrives in your bank account and when it appears in Zooza.

If you need faster matching, consider switching to **email-notification pairing**, which processes payments in near real-time as soon as your bank sends the notification email.

## A client has an active mandate but GoCardless has not collected a payment from their account. What should I check?

GoCardless can be used in two distinct ways in Zooza — make sure you are troubleshooting the right one:

- **Bank reading (inbound matching):** GoCardless reads your business bank account and forwards incoming transfers to Zooza. This is for matching bank transfers that clients send manually.
- **Direct Debit collection:** Zooza sends a collection request to GoCardless, which then pulls the payment directly from the client's bank account. This requires an active mandate on the client's booking AND a payment plan with offline charging enabled.

If the client has an active mandate but no collection has happened, check:

1. **Is offline charging enabled on the payment plan?**
   Open the booking → **Payments** → **Payment plan**. The plan must have offline charging (GoCardless Direct Debit) selected. If it shows a different payment method or offline charging is off, collections will never trigger automatically.

2. **Is the payment in "Processed" status?**
   Collections only run on payments that have moved to **Processed** status. If the payment is still **Scheduled**, it has not yet been processed — check whether the scheduled date has passed.

3. **Was the processed payment queued for collection?**
   A payment can reach "Processed" status without being sent to the GoCardless collection queue (for example, if offline charging was temporarily disabled at the time of processing). Open the payment detail (click **More** next to the payment) and look for a **"Push to offline charge queue"** button. If present, click it to enqueue the collection manually.

4. **Is the mandate still valid?**
   On the booking's payment tile, check the **SEPA Direct Debit** section. If it shows **Active: No** or the mandate ID is missing, the client's authorization has lapsed or been cancelled. Ask the client to re-authorize via their Client Profile.

For step 3 in detail, see [Manually push a scheduled payment to offline charge](../troubleshooting/offline-charge-manual-push.md).

## Why does payment matching redirect me to a registration instead of an order?

When you click to match a transaction, Zooza resolves the variable symbol and navigates to the matching record. If the variable symbol belongs to an **Order** (product purchase) but the system takes you to a **Registration**, it means the same variable symbol exists on both records — which can happen when an order was created from a registration.

To match a payment to an order specifically:

1. Go to **Orders** (not Bookings) and find the order using the client's name or the variable symbol.
2. Open the order detail.
3. In the **Payments** tile, click **Match payment** and select the transaction from the list.

Matching from the Orders section ensures the payment is applied to the order balance, not the registration balance.

> If you match a payment via the registration and the order balance remains unpaid, the client will still receive payment reminders for the order. Always match at the correct record level.

## A transaction does not appear in the matching list. What should I do?

If a bank transaction arrived in your account but is not showing in the Zooza matching list, work through these checks:

1. **GoCardless sync delay.** GoCardless syncs once per day. If the payment arrived recently, wait up to 24 hours and check again.
2. **Already matched.** The transaction may have been automatically matched to another booking. Search for the variable symbol in **Bookings** to confirm.
3. **No matching debt.** Zooza only shows transactions that have a corresponding open debt. If the client paid before a scheduled payment was generated, the transaction will stay unmatched until the debt exists.
4. **Connection expired.** If your GoCardless connection lapsed, transactions from that period may be missing. After renewing the connection, use **CSV import** to back-fill the missing transactions.
5. **Wrong bank account.** The transaction may have arrived in a different bank account than the one connected to your Zooza billing profile. Check the IBAN in **Settings → Billing profiles**.

If none of the above explains it, contact Zooza support with the transaction date, amount, and variable symbol.
