---
title: "Booking FAQ"
slug: "booking-faq"
type: "faq"
product_area: "Bookings"
sub_area: ""
audience: ["admin"]
tags: ["registrations"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-17"
intercom_id: 13728498
intercom_sync: true
---

# Booking FAQ

## How do I generate a booking link to send to my clients?

Every programme in Zooza has a public booking page. Your main booking URL is `yourbrand.zooza.online`. You can also share direct links to specific classes:

- **Full list** — `yourbrand.zooza.online/booking/` lets clients choose from all available classes.
- **Programme-specific** — add `?course_id=X` to guide clients to a specific programme.
- **Class-specific** — add `?course_id=X&schedule_id=Y&place_id=Z` to pre-fill a specific class.

Share these links via email, WhatsApp, or your website.

## Why are clients creating duplicate bookings?

This usually happens when a parent starts the booking, doesn't complete payment, and then tries again. Zooza warns them that a booking already exists, but some parents confirm and create a second one.

To handle duplicates:

1. Go to **Bookings** and identify the unpaid duplicate.
2. Delete the unpaid booking (the one without a completed payment).
3. Always check the child's name and date of birth to confirm it's truly a duplicate.

The system doesn't block repeat bookings because sometimes a parent legitimately needs to register a second child.

## How do I delete test bookings?

Go to **Bookings**, find the test booking, open its detail, and change the status to **Deleted**. This completely removes the booking. The data is still available under the "Deleted bookings" filter for reference.

## What is the difference between deleting and cancelling a booking?

- **Cancellation** — used when a booking was active (the child was attending), but the family decides to stop. It ends the booking, frees the spot, but keeps the full history.
- **Deletion** — used when you want to completely remove the booking (e.g., test entries, accidental duplicates).

## Can clients register multiple children at once?

Yes. During booking, there is an **Add another child** button. When a parent adds a second child, the price doubles accordingly. If clients report seeing unexpected higher prices, they may have accidentally clicked this button — refreshing the page resets it.

## How do I move a client from one class to another?

Open the booking detail, and in the settings you can change the assigned class. It's a few clicks — select the new class from the dropdown and save.

## How do I handle pro-rata bookings for partial terms?

Zooza calculates pro-rata prices automatically when a client joins a class that has already started. Go to **Programmes** → **Settings** → **Price and Payment** → **Advanced settings** and configure the **Late bookings** mode and **Aliquot price calculation** method. The system can calculate the reduced price based on remaining sessions or remaining days in the billing period.

For a full walkthrough of all options, see [Late bookings (pro-rata management)](../guides/late-bookings.md).

## Can I manually create a booking on behalf of a client?

Yes. You can go through the booking form on behalf of a parent. This is a workaround — the recommended flow is for parents to book online themselves. Note that trial bookings cannot be created manually by an admin; only standard enrolments.

## What does the client list show — why are there more entries than expected?

The **Clients** list shows all entities: both parents and children. So if you have 90 bookings, the client count may appear higher because each parent and each child is listed separately. Use the **Bookings** or **Reports** section for accurate booking counts.
