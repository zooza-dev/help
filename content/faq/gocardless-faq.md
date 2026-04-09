---
title: "GoCardless Integration FAQ"
description: "Open the booking detail and scroll to the Payments tile. Click Show payments to expand it."
slug: "gocardless-faq"
type: "faq"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: ["gocardless"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-13"
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

<!-- REVIEW: SLSP issue was reported in late 2025; confirm whether it has been fully resolved before removing this note. -->

**Slovenska sporitelna (SLSP)** experienced a prolonged outage in late 2025 where the bank stopped sending transaction data to GoCardless entirely. All GoCardless requests to SLSP returned server errors. This was a bank-side issue, not a Zooza configuration problem. The issue was eventually resolved, but SLSP users are recommended to consider switching to email-notification pairing for more reliable operation.

If you use SLSP and experience pairing issues, try the email-notification method as described in the next question.

Other banks generally work well with GoCardless. If you notice payments are not arriving in Zooza, first check your GoCardless connection status in your internet banking before contacting support.

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
