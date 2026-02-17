---
title: "Discounts and Sibling Pricing FAQ"
slug: "discounts-and-sibling-pricing-faq"
type: "faq"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: ["payments"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-17"
intercom_id: 13728489
intercom_sync: false
---

# Discounts and Sibling Pricing FAQ

## How do I set up a discount code?

Go to **Payments → Discounts** and create a new code. You can configure:

- **Code name** — what the client enters (e.g., "SIBLING15").
- **Discount type** — percentage or absolute amount.
- **Usage limits** — single-use or unlimited.
- **Programme/location restrictions** — limit to specific programmes or locations.

Enable the discount code field on your booking form so clients can enter it during checkout.

## How do sibling discounts work?

There is no built-in automatic sibling detection yet. Currently, sibling discounts are handled manually using one of these approaches:

- **Discount code approach:** Create a single-use coupon and share it with parents who have multiple children. The parent applies it to the second child's booking.
- **Percentage split:** If the discount should apply to one child out of two registered together, use half the percentage (e.g., 7.5% instead of 15%) since the code applies to the entire order total.
- **Manual adjustment:** Register both children, then manually adjust the payment amount on one booking.

## Does a discount code apply per child or per order?

Discount codes apply to the **entire order total**, not per child. If a parent registers two children in one checkout, the discount is calculated on the combined amount. This means it gets split across both children, which can look different depending on how the booking was done.

## Can I use percentage discounts with monthly memberships?

For monthly memberships (recurring payments), percentage discounts do not work because there is no fixed total order value. Use **absolute discounts** instead (e.g., 50 AED off instead of 10%).

## How can I waive a registration fee for existing members?

Create a one-time discount code equal to the registration fee amount (e.g., code "MEMBER" for 100 AED off). Share it with existing clients when they re-register. They enter it during checkout, and the registration fee is deducted from their first payment.

## How do I set a fixed price that ignores pro-rata for late joiners?

Go to **Programmes** → select the programme → **Settings** → **Price and Payment** → **Advanced settings**. Set the **Aliquot price calculation** to **Full programme price**. With this setting, every late booking is charged the full price regardless of when the client joins.

You can also adjust the calculated amount manually on each booking before confirming it, if you need a case-by-case override instead of a blanket rule.

The system does not support date-based automatic switching (e.g., full price for the first two weeks, then pro-rata after that). If you need that behaviour, manually toggle the setting at the appropriate time.

For a full walkthrough of all pro-rata options, see [Late bookings (pro-rata management)](../guides/late-bookings.md).

## The payment template rounds my custom price down — how do I avoid this?

Rounding is a setting on the **payment template** itself. It applies only when the template formula calculates the instalment amount (i.e., course price divided by number of instalments). The sequence is:

1. The system takes the programme/class price.
2. It splits the amount according to the template rules (e.g., monthly instalments).
3. The resulting value is rounded according to the template's rounding setting (e.g., round down to the nearest whole number).

If you enter a **custom fixed amount** directly on a booking's payment schedule, that amount still passes through the template's rounding rule. To avoid unwanted rounding:

- **Option A:** Create a separate payment template with rounding set to **none** and use it whenever you need to assign a custom exact amount.
- **Option B:** Adjust the rounding setting on your existing template to a precision that suits your needs (e.g., round to two decimal places instead of whole numbers). <!-- REVIEW — confirm available rounding precision options in current UI -->

Go to **Settings → Payment settings** and open the relevant payment template to review or change its rounding configuration.
