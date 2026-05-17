---
title: "Payment not received in Zooza — troubleshooting"
description: "A client paid but the payment hasn't appeared in Zooza. Work through this checklist to diagnose the most common causes for GoCardless and email-notification matching."
slug: "payment-not-received"
type: "troubleshooting"
product_area: "Payments"
audience: ["admin"]
tags: ["payments", "gocardless", "payment-matching", "email-notifications", "troubleshooting", "inbound-payments"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-05-13"
---

# Payment not received in Zooza

A client has paid but the payment hasn't appeared in Zooza. Before contacting support, work through the checks below — most cases are caused by a misconfigured email address, a broken GoCardless connection, or a payment sitting in the unmatched queue.

## Step 1: Identify your matching method

Go to **Settings → Billing profiles** and check which method is active for the relevant billing profile:

- **GoCardless** — Zooza collects payments via direct debit; GoCardless notifies Zooza automatically.
- **Email notification matching** — your bank emails a transaction notification to a unique Zooza address; Zooza parses it and matches the payment.

Follow the relevant section below, then check [General checks](#general-checks) regardless of method.

---

## GoCardless

### 1. Check the GoCardless connection in your bank

Log in to your internet banking and go to **Third-party apps**, **Connected services**, or **Authorised partners** (the exact location varies by bank). Confirm that GoCardless is still listed and authorised. Banks occasionally revoke third-party access without warning — if GoCardless is missing or shows as disconnected, you need to re-authorise it from within Zooza.

### 2. Check the GoCardless connection in Zooza

Go to **Settings → Billing profiles** and check the GoCardless status for the relevant profile. If it shows an error or disconnected state, reconnect the integration.

### 3. Check the client's mandate status

> This step applies to **direct debit** only. If you are using GoCardless for wire transfer matching, skip to Step 4.

Open the client's profile in Zooza and find their GoCardless mandate. It should be **Active**. A cancelled or expired mandate means no payments can be collected — the client needs to re-sign before any new collection can proceed.

### 4. Check the payment status in GoCardless

Log in to your GoCardless account and locate the payment. GoCardless payments move through several states before funds reach Zooza:

| Status | Meaning |
|--------|---------|
| Pending submission | Not yet sent to the bank |
| Submitted | Sent to the bank, awaiting confirmation |
| Confirmed | Collected, payout pending |
| Paid out | Funds sent to your account |
| Failed | Collection failed — see the failure reason in GoCardless |

Payments typically take **2–5 business days** to reach **Paid out** status. If the status is **Failed**, the failure reason shown in GoCardless will indicate next steps (for example, insufficient funds or a cancelled mandate).

---

## Email notification matching

### 1. Verify the Zooza email address in your bank

Go to **Settings → Billing profiles** and copy the Zooza-generated notification email address for the relevant profile. Then log in to your internet banking and find the payment notification rule. Confirm the destination address **exactly matches** the Zooza address — a single character difference means Zooza never receives the email.

### 2. Check if other transactions are being matched

Go to **Payments → Received payments** and check whether other recent bank transfers are appearing. If yes, the setup is working and the issue is specific to this one payment. If no recent transfers are visible, the email pipeline is broken entirely — likely an address mismatch or a bank-side issue.

### 3. Check the unmatched payments queue

In **Payments → Received payments**, filter for unmatched or unresolved payments. The payment may have arrived but failed to match because the variable symbol (VS) was missing, incorrectly formatted, or placed differently in the email.

### 4. Check the ignore list and AI rules

Payments can be moved to an ignored state — either manually or by an AI rule. Check **Payments → Received payments** for the payment and look at its status. Also review **Payments → Received payments → AI Rules & Filters** to confirm no rule is excluding this type of payment.

### 5. Add your own email to the notification rule

If your internet banking supports multiple recipients for payment notifications, add your own email address as an additional recipient alongside the Zooza address. This lets you confirm independently whether the bank is actually sending notifications.

If your copy of the notification doesn't arrive either, the bank is not sending the emails at all — contact your bank. Do not assume the problem is with Zooza until you have confirmed the bank is actually sending the notification.

---

## General checks

These apply regardless of which matching method you use:

- **Bank account** — confirm in **Settings → Billing profiles** that the IBAN shown matches the account the client paid into. If the client paid into a different account, Zooza won't see the payment.
- **Client profile** — check the client doesn't have a duplicate profile. The payment may have matched to a different profile.
- **View filters** — check whether a date range or programme filter in the Payments view is hiding the payment from your current view.

---

## Still not resolved?

1. **Contact your bank** — if the notification is not arriving at either the Zooza address or your own email address, the bank is not sending it. The bank must resolve this on their side.
2. **Contact Zooza support** — describe which steps you have already checked and forward the original bank notification email if you have one. Zooza support can verify on their side whether the notification was received at all — whether it came via email, a direct GoCardless bank connection, or a partner-based connection. This lets support confirm whether the problem is with delivery (the bank or GoCardless never sent it) or with processing (Zooza received it but could not match it).

---

## Related articles

- [Email-notification payment matching](../setup/email-payment-notifications.md)
- [GoCardless connection lifecycle](../guides/gocardless-connection-lifecycle.md)
- [Payment pairing](../guides/payment-pairing.md)
