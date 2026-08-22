---
title: "Discounts and Sibling Pricing FAQ"
description: "Go to Sales & Payments → Discounts in the left navigation menu."
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
last_converted: "2026-06-01"
---


# Discounts and Sibling Pricing FAQ

## Where do I find discount codes and discounts?

Go to **Sales & Payments → Discounts** in the left navigation menu.

The Discounts page has four sections:

- **Discount codes** — create and manage codes that clients enter during checkout.
- **Discounts** — a list of all discounts that have been used, with client names and amounts.
- **Free sessions** — credits for free sessions granted to specific clients.
- **Payment templates with discount** — payment templates that include a built-in percentage discount.

## How do I set up a discount code?

Go to **Sales & Payments → Discounts → Discount codes** and click **Create**. You can configure: You can configure:

- **Code name** — what the client enters (e.g., "SIBLING15").
- **Discount type** — percentage or absolute amount.
- **Usage limits** — single-use or unlimited.
- **Programme/location restrictions** — limit to specific programmes or locations.

Enable the discount code field on your booking form so clients can enter it during checkout.

## How do sibling discounts work?

Use the built-in **Sibling Discount**. Go to **Sales & Payments → Loyalty Programme → Sibling Discount**, add at least one rule, and switch it on — it will not enable without a rule.

Each rule is a tier:

| Field | What it does |
|---|---|
| **From child** | Which child the tier starts at — 2nd, 3rd, 4th or 5th |
| **Discount type** | **Percentage** or **Fixed amount** |
| **Discount** | The value. Percentages must be between 1 and 100 |

So "the second child at 50% off" is one rule: *from 2nd child, percentage, 50*. Add another tier if the third child should get more.

### How to count children

This is the setting that decides what "second child" actually means, and it is worth getting right:

- **Per programme** — the count restarts in each programme. Two children in two different programmes are each a first child, and neither gets a discount.
- **Per billing period** — children are counted together within a term.
- **Across all programmes** — every child the family has with you counts, wherever they are booked.

You can also limit the discount to **selected programmes** rather than all of them.

> **Only registrations with Registered status count.** Waitlist and trial registrations are not included in the child count, so a family whose second child is still on the waiting list does not get the discount yet.

Each tier must have a unique child number, and deleting the last rule switches the sibling discount off.

## Can a client add a discount code after they have already booked?

Yes. A client who forgot the code at checkout does not need you to fix it for them.

When they return to their profile to pay an outstanding balance, the payment screen shows a discount code field. It works in two steps:

1. **Validate** — they enter the code and see what the new total would be. Nothing is committed yet.
2. **Apply** — the discount is committed, the amount due drops, and the payment request is reissued.

They then pay the reduced amount as normal.

**When the field does not appear:**

- The booking is **paid in full**. The field only shows while there is an outstanding balance.
- The order is not a **course** registration — product and shop orders are not covered.
- You have switched discounts off on the widget.

**Two rules worth knowing:**

- **Different codes stack.** A client can apply a second, different code on top of the first.
- **The same code cannot be applied twice.** A repeat attempt is rejected with a message.

> There is no undo. Once a code is applied to a registration it cannot be removed from the client side, so a mistaken code has to be corrected on the payment itself. See [Edit payment on booking](../guides/edit-payment-on-booking.md).

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

Rounding is a setting on the **payment template** itself. It applies only when the template formula calculates the instalment amount (i.e., programme price divided by number of instalments). The sequence is:

1. The system takes the programme/class price.
2. It splits the amount according to the template rules (e.g., monthly instalments).
3. The resulting value is rounded according to the template's rounding setting (e.g., round down to the nearest whole number).

If you enter a **custom fixed amount** directly on a booking's payment schedule, that amount still passes through the template's rounding rule. To avoid unwanted rounding:

- **Option A:** Create a separate payment template with rounding set to **none** and use it whenever you need to assign a custom exact amount.
- **Option B:** Adjust the rounding setting on your existing template to a precision that suits your needs (e.g., round to two decimal places instead of whole numbers). <!-- REVIEW — confirm available rounding precision options in current UI -->

Go to **Settings → Payment settings** and open the relevant payment template to review or change its rounding configuration.
