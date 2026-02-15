---
title: "Payments and Billing FAQ"
slug: "payments-and-billing-faq"
type: "faq"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: ["payments"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-13"
intercom_id: 13728495
intercom_sync: true
---

# Payments and Billing FAQ

## What does a negative balance mean on a booking?

The balance shows the difference between what the client should pay and what they actually paid.

- **0** = fully paid.
- **Negative amount** = payment was not completed or failed. The client needs to finish payment via their Client Profile.

A negative balance does not necessarily mean "overpaid" — it means there is an outstanding amount.

## What happens when a client registers but does not pay?

The booking is created even if the payment fails or is skipped. This ensures you still capture the lead. The parent can complete the payment later via their Client Profile.

You can configure **payment reminders** per programme to automatically follow up with unpaid clients. After a set number of reminders, the system can auto-remove the booking.

## How do payment reminders work?

Payment reminders are configured per programme under the payment settings. You set:

- How many reminders to send.
- The interval between reminders.
- Whether the system should automatically cancel the booking after all reminders expire.

Go to **Programme → Settings → Price** to configure this.

## How do I issue a refund?

Refunds are handled directly in Zooza:

1. Go to **Bookings → Detail → Payments**.
2. Select the transaction.
3. Click **Refund** (full or partial).

The refund is processed through Stripe automatically. You do not need to log into Stripe separately.

## How does monthly billing (aliquot) work?

When a parent joins mid-month, the system can calculate a prorated first payment based on the remaining sessions in that month. This is called **aliquot** billing.

- **Aliquot ON:** First payment is adjusted for the number of sessions remaining. Subsequent months are the full fixed amount.
- **Aliquot OFF:** Every payment is always the same fixed monthly amount, regardless of when the client joins.

Choose the option that fits your business model. Most clients prefer aliquot OFF for simplicity during launch, and turn it ON later.

## Can I retrospectively generate invoices?

Yes. You can disable automatic invoice generation during launch, accept bookings and payments, and then generate invoices later once your accounting settings (e.g., VAT rates in Xero) are fully configured.

## How do I handle a client who forgot to use a discount code?

Instead of refunding, the easiest approach is to reduce the next instalment by the discount amount and send the client a quick note explaining the adjustment. This is simpler than editing past payments.

## How do I mark a booking as paid when payment was received outside the system?

If a client paid by direct bank transfer or you credited them manually, you can adjust the payment status in their booking detail. Go to **Bookings → Detail → Payments** and record the manual payment to clear the outstanding balance.

## When should I use "Edit payment" vs "Refund"?

Use **Edit payment** for corrections — for example, when the amount is wrong or a payment was assigned to the wrong booking. Use **Refund** only when you are actually returning money to the client.

Using **Refund** incorrectly (e.g., to zero out a manual entry) creates phantom transactions that appear in your financial reports and distort totals. If you need to correct or move a payment between bookings, a debt correction is the preferred approach.

<!-- REVIEW: Support tickets confirm "Edit payment" is accessed via the transaction list → More → Edit payment. Verify current UI label matches. -->

## What happens to payment schedules when I copy bookings to a new term?

Payment schedules are **not** automatically carried over when you copy bookings to a new term. Because the client did not go through the booking form and select a payment template, the system does not assign one.

After copying bookings, you must manually apply the correct payment template to each booking. Without this step, the system calculates the price as the base rate multiplied by the number of sessions, which may differ from the expected instalment amount.

<!-- REVIEW: Bulk activation of payment templates after copy is requested frequently — check if a bulk-apply feature has been added. -->

## How does pro-rata (aliquot) pricing work for late bookings?

When a client registers after the term has started and aliquot pricing is enabled, the system calculates the price as:

**remaining sessions ÷ total sessions × full price**

This adjusted price is then split according to the active payment template (e.g., monthly instalments). The calculated pro-rata price may not always be visible to the client during booking, depending on your programme settings.

<!-- REVIEW: Confirm whether the pro-rata price is shown on the booking form or only after booking is completed. -->

## Why does the QR code in my payment email not work?

The QR code in payment emails pulls recipient details from your **billing profile**. If the profile name does not match the bank account holder name, some banking apps will reject or fail to process the QR code when scanned.

To fix this:

1. Go to **Settings → Billing Profiles**.
2. Open the relevant billing profile.
3. Verify that the **account holder name** and **IBAN** match your actual bank account details exactly.
4. Save and resend the payment notification to the client.
