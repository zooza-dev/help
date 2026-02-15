---
title: "Orders and Products FAQ"
slug: "orders-and-products-faq"
type: "faq"
product_area: "Orders"
sub_area: ""
audience: ["admin"]
tags: ["orders", "products", "vouchers", "services"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-13"
---

# Orders and Products FAQ

## Where can I see unpaid product orders?

There is no dedicated report for unpaid product orders, but you can filter the orders list directly.

1. Go to **Orders**.
2. Open the advanced search panel.
3. Set `payment_status` to **unpaid** and `status` to **not deleted**.

This gives you a filtered view of all outstanding product orders. Unpaid product orders do not appear in the booking-level debt notifications, so you need to check the orders list separately.

## Can I add a QR payment code to product order emails?

Yes. QR payment codes are supported in order-related emails. For the QR code to generate correctly:

- The order must have an outstanding balance.
- Your invoice profile must include a valid IBAN (not a basic bank account number).

If the QR code tag appears as plain text in the sent email instead of rendering, open the email template, delete the dynamic tag, and re-type it. Invisible characters or formatting artefacts can prevent the system from recognising the tag.

<!-- REVIEW: QR codes in order emails were initially limited to Slovakia. This was fixed — confirm the fix is still live and applies to all regions. -->

## How do I track whether a purchased entry pass has been used?

Entry passes are tracked through the orders list and the client record. For details on creating and configuring entry passes, see [Creating entry passes](../guides/creating-entry-passes.md).

1. Go to **Clients** and search for the client by email.
2. Open their profile and look at their orders.
3. Each entry pass order shows a code, the number of remaining entries (if it is a visits-based pass), and the expiration date.

An entry pass code can only be used once. When all entries are consumed or the pass expires, it cannot be reused. The expiration period is set on the product configuration (e.g., 12 months from purchase).

If a client purchased the entry pass from a different email address than the one on file, search by the purchasing email to locate the order.

## Why don't dynamic tags work in order confirmation emails?

Dynamic tags (such as `{client_name}` or `{QR_CODE}`) are not fully supported in order-related email templates. This is a known limitation. When the system does not recognise a tag or has no value for it in the order context, the tag either remains as plain text or is silently removed.

If you need to personalise order emails, keep the template text generic and avoid booking-specific tags. Booking-related tags (e.g., class name, session time) do not apply to standalone product orders.

## How do I restore a deleted order?

Deleting an order also releases the product stock/capacity tied to it. If you need to restore a deleted order:

1. Contact Zooza support with the order number.
2. Support can restore the order and its line items on the backend.

Once restored, verify that the product quantities and payment status are correct. To avoid accidental deletions, remove individual line items from an order instead of deleting the entire order.

<!-- REVIEW: There is no self-service restore for deleted orders as of Feb 2026. Confirm whether a UI-level restore has been added. -->

## What does the "reset sales" button on services do?

The **Reset sales** button on a service clears all current sales data and stock counters, so you can reuse the service for a new selling period.

- After resetting, the service starts fresh with zero sold units and full stock.
- Historical statistics (sales before the reset) are preserved in reports and remain visible to clients who previously purchased the service under past bookings.

Use this when you want to offer the same service (e.g., a seasonal pass or a consumable item) in a new term without creating a duplicate service entry.

## How do I link a product payment to a booking?

When a client purchases a product during the booking flow, the product payment should automatically be linked to the booking. If the product payment appears on the order but not on the booking, the cause is usually a missing setting.

1. Go to **Programme → Settings → Price & Payments → Advanced settings**.
2. Enable the option to link product payments to the booking.
3. Save.

If a payment is already mislinked, you can fix it manually:

1. Open the order and unlink it from the booking.
2. Re-link the order to the same booking.
3. When prompted, choose to have the payment managed by the booking.
4. Save. The payment should now appear on the booking record.
