---
title: "Orders and Products FAQ"
description: "There is no dedicated report for unpaid product orders, but you can filter the orders list directly."
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
last_converted: "2026-08-30"
related_articles: ["invoice-profiles-and-bank-accounts","creating-entry-passes","selling-products-during-booking","dynamic-tags"]
---

# Orders and Products FAQ

## Where can I see unpaid product orders?

There is no dedicated report for unpaid product orders, but you can filter the orders list directly.

1. Go to **Orders**.
2. Open the advanced search panel.
3. Set `payment_status` to **unpaid** and `status` to **not deleted**.

This gives you a filtered view of all outstanding product orders. Unpaid product orders do not appear in the booking-level debt notifications, so you need to check the orders list separately.

## Do product order confirmations include a QR payment code?

Yes. The order confirmation email carries the same pay-by-square QR code that booking
emails do, so a customer paying by bank transfer scans it instead of typing the IBAN,
amount and variable symbol by hand. The variable symbol is the order number.

For the code to render:

- The order must have an outstanding balance.
- Your invoice profile must have a valid **IBAN** (not a basic account number) **and a SWIFT code** — the QR does not appear until the SWIFT is filled in. See [Invoice profiles and bank accounts](../setup/invoice-profiles-and-bank-accounts.md).

If the QR tag shows as plain text in the sent email instead of rendering, open the
template, delete the dynamic tag and re-type it — invisible characters pasted in from
elsewhere stop the tag being recognised.

## How do I track whether a purchased entry pass has been used?

Entry passes are tracked through the orders list and the client record. For details on creating and configuring entry passes, see [Creating entry passes](../guides/creating-entry-passes.md).

1. Go to **Clients** and search for the client by email.
2. Open their profile and look at their orders.
3. Each entry pass order shows a code, the number of remaining entries (if it is a visits-based pass), and the expiration date.

An entry pass code can only be used once. When all entries are consumed or the pass expires, it cannot be reused. The expiration period is set on the product configuration (e.g., 12 months from purchase).

If a client purchased the entry pass from a different email address than the one on file, search by the purchasing email to locate the order.

## Can I extend the expiry date on a purchased entry pass or gift voucher?

No. The expiry date on a purchased entry pass or gift voucher **cannot be changed by an admin** from the Orders screen. The expiration field is read-only — it displays the date but does not allow editing.

If a client needs their expiry extended, contact Zooza support with the order number. Support can adjust the expiry date on the backend.

To avoid this situation in the future, set a longer expiry period on the product configuration before clients purchase it. The expiry period is defined on the product itself (e.g., 12 months from purchase) and applies to all future purchases — it cannot be changed retroactively in bulk.

## Which dynamic tags work in order confirmation emails?

Order emails resolve their own set of tags — fewer than a booking email, but the ones
that matter for getting paid now work:

| Available in order emails | Not available |
|---|---|
| `QR_CODE`, `VARIABLE_SYMBOL` | `ORDER_SUMMARY`, `SEGMENTS_SUMMARY` |
| `PAYMENT_STATUS`, `DEBT`, `PAID`, `CURRENT_BALANCE` | Booking-specific tags — class name, session date and time |
| `PRODUCT_NAME`, `COMPANY`, `COMPANY_LOGO`, `WIDGET_PROFILE_URL` | Anything tied to a registration rather than an order |

A tag that does not apply to an order is skipped rather than breaking the email — but
it also produces nothing, so it will simply be missing from what the customer reads.

Booking-related tags do not apply to standalone product orders at all: an order has no
class and no session, so there is nothing for those tags to resolve against.

## How do I restore a deleted order?

Deleting an order also releases the product stock/capacity tied to it. If you need to restore a deleted order:

1. Contact Zooza support with the order number.
2. Support can restore the order and its line items on the backend.

Once restored, verify that the product quantities and payment status are correct. To avoid accidental deletions, remove individual line items from an order instead of deleting the entire order.

> **Note:** The self-service **Trash** screen (Settings → Tools → Trash) covers registrations, sessions, and classes — but not orders. Deleted orders require support to restore.

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

## Related

- [Selling products during booking](../guides/selling-products-during-booking.md) — add product offers to the booking flow
- [Multi-day event with product offer](../guides/multi-day-event-with-product-offer.md) — combine events with product sales
