---
title: "GoCardless Connection Lifecycle"
slug: "gocardless-connection-lifecycle"
type: "guides"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: ["gocardless"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: true
last_converted: "2026-02-13"
---

# GoCardless Connection Lifecycle

GoCardless connects your bank account to Zooza so that incoming payments are automatically forwarded for matching. This guide explains how the connection works over time, how to monitor it, how to renew it, and what to do when things go wrong.

For quick answers, see [GoCardless FAQ](../faq/gocardless-faq.md).

## How the bank connection works

GoCardless acts as a bridge between your bank and Zooza. After you authorize GoCardless in your internet banking, it periodically reads incoming transactions and sends them to Zooza. Zooza then matches each transaction to a booking using the variable symbol.

Key characteristics:

- GoCardless syncs transactions **once per day**. There can be up to a 24-hour delay between a payment arriving in your bank and appearing in Zooza.
- The connection is authorized through your internet banking, not through Zooza directly.
- Zooza cannot access your bank account on its own. GoCardless is the intermediary.

## The 90-day expiry cycle

For security reasons, banks limit GoCardless connections to approximately **90 days**. This is a requirement imposed by the bank, not by Zooza or GoCardless.

The lifecycle follows this pattern:

1. You authorize GoCardless in your internet banking.
2. Transactions flow automatically for up to 90 days.
3. The connection expires. Transaction data stops flowing.
4. You must re-authorize GoCardless to restart the cycle.

After each renewal, the 90-day countdown resets.

<!-- REVIEW: Some banks may use different expiry periods. 90 days is the standard for Slovak banks. Confirm whether other European banks use the same period. -->

### What happens when the connection expires

When the 90-day window closes:

- GoCardless stops receiving transaction data from your bank.
- Zooza stops receiving new payments for automatic matching.
- Payments still arrive in your bank account normally -- they just are not forwarded to Zooza.
- Any unmatched payments remain unmatched until you either renew the connection or pair them manually.

Zooza sends an email notification before your connection expires. If you miss this notification, you may not realize the connection has lapsed until you notice unmatched payments.

## Checking connection status

Zooza does not display the exact expiry date of your GoCardless connection. To check the current status:

1. Log in to your **internet banking**.
2. Navigate to the section where third-party service connections are managed (the exact location varies by bank).
3. Look for the GoCardless connection entry. It will show whether the connection is active and when it expires.

<!-- REVIEW: Add a screenshot showing where to find GoCardless connection status in a typical internet banking interface. -->

**Tip:** After each renewal, set a calendar reminder for 85 days later so you can renew before the connection expires.

## Renewing an expired connection

### Option A: Renew from Zooza

1. Go to **Settings -> Billing profiles**.
2. Open your default billing profile.
3. Click the logo of your bank to start the GoCardless authorization flow.
4. You will be redirected to your internet banking.
5. Confirm that you authorize GoCardless to access your account.
6. After confirmation, you are returned to Zooza. The connection is now active for another 90 days.

### Option B: Renew from internet banking

1. Log in to your **internet banking**.
2. Find the GoCardless connection in your account or service settings.
3. Re-authorize or extend the connection.

After renewal, verify that payments begin appearing in Zooza within 24 hours. Check a recent transaction to confirm the data is flowing.

## Bank-specific issues and workarounds

### Slovenska sporitelna (SLSP)

<!-- REVIEW: SLSP outage was reported in late 2025. GoCardless confirmed it was a bank-side issue (HTTP 500 errors). The issue was eventually resolved, but recurrence is possible. Update this section if the situation changes. -->

In late 2025, SLSP experienced a prolonged outage where the bank stopped sending transaction data to GoCardless entirely. All GoCardless API requests to SLSP returned server errors. This was confirmed as a bank-side problem, not a Zooza or GoCardless configuration issue.

During the outage, Zooza support recommended the following workaround:

1. **Remove the GoCardless connection** in your internet banking (George) to prevent duplicate transactions once the issue is resolved.
2. **Import payments manually via CSV** as a temporary measure:
   - Export transactions from George (internet banking).
   - Go to **Payments -> Import payments** in Zooza.
   - Import the CSV file. Export one day at a time to avoid duplicates.
3. Alternatively, **switch to email-notification pairing** (see the next section) for a permanent fix that does not depend on GoCardless.

The SLSP issue was eventually resolved. However, if you use SLSP, consider switching to email-notification pairing for more reliable long-term operation.

### Tatra Banka

Tatra Banka has experienced occasional service outages that temporarily prevent GoCardless from receiving transaction data. These are typically short-lived. If payments from Tatra Banka stop appearing in Zooza:

1. Check the Tatra Banka website or internet banking for service announcements.
2. Verify that your GoCardless connection has not expired (check the 90-day window).
3. If the bank confirms an outage, wait for the service to be restored. Transactions should resume automatically.

<!-- REVIEW: Confirm whether Tatra Banka issues are limited to GoCardless or also affect email-notification pairing (b-mail). -->

## Switching to email-notification pairing

If you want to avoid the 90-day renewal cycle, you can switch from GoCardless to email-notification pairing. With this method, your bank sends a notification email for each incoming payment to a special Zooza email address. Zooza processes these emails in near real-time.

### Why switch

| | GoCardless | Email notification |
|---|---|---|
| **Sync frequency** | Once per day | Near real-time (minutes) |
| **Renewal required** | Every 90 days | No |
| **Bank compatibility** | Depends on GoCardless support | Any bank with email notifications |

### How to switch

1. **Remove the GoCardless connection** in your internet banking. This prevents duplicate transactions once both methods are active.
2. Go to **Settings -> Billing profiles** in Zooza. Find the notification email address associated with your IBAN. The address is constructed from your IBAN (for example, if your IBAN is `SK1234567890123456`, the format is shown in your billing profile settings).
3. **Set up email notifications** in your internet banking. Configure your bank to send incoming payment notifications to the Zooza-generated email address.
4. **Monitor the first payment** to confirm transactions arrive in Zooza correctly.

**Important:** After switching, your bank will no longer send payment notification emails to your personal email address. All notifications are routed to Zooza instead.

## Troubleshooting: connection expired without notice

If you discover that payments have not been matching and suspect your GoCardless connection has expired:

1. **Check the last matched payment.** Go to **Payments** in Zooza and look at the most recent automatically paired payment. The date of this payment gives you a rough idea of when the connection stopped.
2. **Renew the connection** using either Option A or Option B described above.
3. **Handle the gap period.** Payments received during the gap were not forwarded to Zooza. You have two options:
   - **Wait for GoCardless to backfill.** After renewal, GoCardless may sync recent transactions that were missed. Check within 24 hours.
   - **Import payments manually via CSV.** Export transactions from your internet banking for the gap period and import them into Zooza at **Payments -> Import payments**. Export one day at a time to avoid duplicates.
4. **Pair unmatched payments manually** if automatic matching did not resolve all of them. Go to the unmatched payments list and pair each one by variable symbol.

<!-- REVIEW: Confirm whether GoCardless backfills missed transactions after reconnection, or whether manual import is always required for the gap period. -->

## Best practices: monitoring connection health

- **Set a calendar reminder.** After each renewal, create a reminder for 85 days later. This gives you a 5-day buffer before expiry.
- **Watch for the Zooza notification email.** Zooza sends a reminder before your connection expires. Make sure these emails are not going to spam.
- **Check the payments dashboard regularly.** If you notice that no new payments have appeared for several days, your connection may have expired.
- **Consider email-notification pairing.** If renewing every 90 days is inconvenient or if your bank has known GoCardless issues, email-notification pairing eliminates the renewal cycle entirely.
- **Keep GoCardless and email-notification pairing mutually exclusive.** Do not run both methods on the same bank account at the same time. This causes duplicate transactions in Zooza.
