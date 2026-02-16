---
title: "Membership Subscription Setup"
slug: "membership-subscription-setup"
type: "guides"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: ["membership", "subscription", "recurring-payments", "setup"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-15"
intercom_id: 13738703
intercom_sync: false
---

# Membership Subscription Setup

This guide explains how to set up an ongoing, never-ending membership programme — sometimes called a "Netflix-style" subscription. Clients enrol once, pay monthly on a recurring basis, and stay enrolled until they cancel. This model is common for football clubs, dance studios, gyms, and martial arts schools.

## Prerequisites

- A programme already created in Zooza.
- At least one class (timetable) assigned to the programme.
- A payment method configured (e.g., Stripe, bank transfer).

## Step 1: Set the price type to Membership

1. Go to **Programmes** → select the programme → **Edit Settings**.
2. Open the **Price and Payment** tile.
3. Set `Price type for programme` to **Membership**.
4. Enter the monthly membership price in the `Unit price` field.
5. Save.

Membership pricing charges a fixed amount at a recurring interval, rather than dividing a total term price into instalments.

## Step 2: Configure late bookings as automatically confirmed

Since this is an ongoing programme with no fixed start date, every new registration is technically a "late booking." You want these to be approved instantly without admin intervention.

1. In the same **Price and Payment** tile, expand **Advanced settings**.
2. In the `Late bookings` section, select **Automatically confirmed**.
3. Save.

This ensures new clients are enrolled immediately and can start attending right away.

## Step 3: Set aliquot price to Full programme price

To charge every new client the same fixed monthly amount regardless of when they join:

1. In **Advanced settings**, set `Aliquot price calculation` to **Full programme price**.
2. Save.

This prevents the system from calculating a pro-rata first payment based on remaining days in the month.

## Step 4: Uncheck Include Initial Full Scheduled Payment

By default, Zooza generates an immediate full instalment when a client books. For a subscription model, you typically want the first payment to follow the normal billing schedule instead.

1. In **Advanced settings**, uncheck `Include Initial Full Scheduled Payment`.
2. Save.

With this unchecked, the client's first payment is generated according to the payment template schedule — not as an extra upfront charge.

## Step 5: Create a monthly payment template

The payment template controls when and how often clients are billed.

1. Go to the programme's **Payment templates** section.
2. Click **Add new template**.
3. Set the payment frequency to **Monthly**.
4. Set `Day of the month when the payment is due` to **0**.
5. Save.

Setting the day to **0** means the payment is due on the same calendar day each month that the client originally enrolled. For example, if a client registers on the 15th, their payments are due on the 15th of every subsequent month.

<!-- TODO: Add screenshot of payment template settings (assets/images/membership-payment-template-settings.png) -->

## Summary of settings

| Setting | Value |
|---|---|
| Price type | **Membership** |
| Late bookings | **Automatically confirmed** |
| Aliquot price calculation | **Full programme price** |
| Include Initial Full Scheduled Payment | **Unchecked** |
| Payment template frequency | **Monthly** |
| Day of the month when payment is due | **0** |

## How it works for clients

1. The client visits your booking page and selects the membership programme.
2. They fill in their details and complete the booking.
3. The booking is automatically confirmed (no admin approval needed).
4. Their first scheduled payment is generated according to the payment template.
5. Each month, a new payment is automatically scheduled on their billing day.
6. The client continues attending until they or the admin cancels the booking.

## Cancellation

To end a membership:

1. Go to **Bookings** and find the client's booking.
2. Change the booking status to **Cancelled**.
3. Outstanding scheduled payments are removed. Payments already received are not affected.

## Related

- [Late Bookings](late-bookings.md) — detailed explanation of late booking modes and the Include Initial Full Scheduled Payment setting.
- [Payment Options](payment-options.md) — configuring payment methods and templates.
- [Programme Settings Reference](../reference/programme-settings.md) — full reference for all programme settings.
- [Payments and Billing FAQ](../faq/payments-and-billing-faq.md) — common payment questions.
