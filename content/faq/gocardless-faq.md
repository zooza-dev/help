---
title: "GoCardless Integration FAQ"
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

## What is the difference between GoCardless pairing and email-notification pairing?

Zooza supports two methods for automatic payment matching:

| Feature | GoCardless | Email notification |
|---|---|---|
| **How it works** | GoCardless reads transactions directly from your bank via API | Your bank sends a notification email for each incoming payment to a special Zooza email address |
| **Sync speed** | Typically once per day | Near real-time (within minutes) |
| **Renewal required** | Yes, every 90 days | No, works indefinitely once configured |
| **Bank compatibility** | Depends on GoCardless bank support | Works with any bank that supports email notifications for incoming payments |

Email-notification pairing is generally faster and does not require periodic renewal. However, when using email notifications, your bank will no longer send payment notification emails to your personal email address -- they go exclusively to the Zooza-generated address.

## Which banks have known issues with GoCardless?

<!-- REVIEW: SLSP issue was reported in late 2025; confirm whether it has been fully resolved before removing this note. -->

**Slovenska sporitelna (SLSP)** experienced a prolonged outage in late 2025 where the bank stopped sending transaction data to GoCardless entirely. All GoCardless requests to SLSP returned server errors. This was a bank-side issue, not a Zooza configuration problem. The issue was eventually resolved, but SLSP users are recommended to consider switching to email-notification pairing for more reliable operation.

If you use SLSP and experience pairing issues, try the email-notification method as described in the next question.

Other banks generally work well with GoCardless. If you notice payments are not arriving in Zooza, first check your GoCardless connection status in your internet banking before contacting support.

## How do I switch from GoCardless to email-notification pairing?

1. **Remove the GoCardless connection** in your internet banking to prevent duplicate transactions once both methods are active.
2. **Find your Zooza notification email address.** It is constructed from your IBAN. For example, if your IBAN is `SK1234567890123456`, the notification email will be in the format shown in your billing profile settings.
3. **Set up email notifications** in your internet banking. Configure your bank to send incoming payment notifications to the Zooza-generated email address.
4. **Monitor the first payment** to confirm transactions are arriving in Zooza correctly.

After switching, you no longer need to renew any connection every 90 days. Note that payment notification emails from your bank will no longer arrive in your personal inbox -- they are routed directly to Zooza instead.

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
