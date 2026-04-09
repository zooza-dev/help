---
title: "Registration and Booking FAQ"
description: "Every programme in Zooza has a public booking page. Your main booking URL is yourbrand.zooza.online. You can also share direct links to specific classes:"
slug: "registration-and-booking-faq"
type: "faq"
product_area: "Bookings"
sub_area: ""
audience: ["admin"]
tags: ["registrations", "bookings"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-17"
---

# Registration and Booking FAQ

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

## How do I add a participant (child) who is different from the buyer (parent) during manual registration?

Zooza distinguishes between the **buyer** (the person who pays, typically the parent) and the **participant** (the person who attends, typically the child). When creating a manual registration:

1. Open the booking form and enter the buyer's details (the parent's name, email, and phone number).
2. In the participant section, select or create the child who will attend. Make sure you do not leave the participant set to the same person as the buyer unless the buyer is also the attendee.
3. Confirm the booking. The buyer receives payment-related communication, while the participant is linked to the class schedule and attendance.

If you need to change the participant on an existing registration, open the booking detail and update the participant field. The **Bookings** list shows labels for both buyer and participant so you can verify the assignment is correct.

<!-- REVIEW: confirm exact UI field names for buyer/participant selection on manual registration -->

## Can I search for and restore deleted bookings?

Yes. Deleted bookings are not permanently removed from the system. To find them:

1. Go to **Bookings**.
2. Open the advanced search filters.
3. Change the **Status** filter to **Deleted**.

This displays all previously deleted bookings. You can open any deleted booking to review its details. To restore a deleted booking, open its detail and change the status back to the appropriate active status (e.g., **Registered**).

<!-- REVIEW: confirm whether restore is a direct status change or requires re-creation -->

## Can I add a second email address to a booking for notifications?

Yes. You can add an additional email address on any booking so that a second person (e.g., the other parent) receives session reminders and notifications.

1. Open the booking detail.
2. Click **Additional settings** on the left side panel.
3. Scroll down to the email fields. There are two separate fields:
   - One for **notifications** (session reminders and communication).
   - One for **profile access** (allows the second email holder to view the client profile).
4. Enter the second email address in the appropriate field and save.

This is useful when divorced or separated parents both need visibility into the child's schedule, or when a different family member handles day-to-day logistics.

> **Warning:** If you collect a secondary email address via an **extra field** on the booking form (e.g., Additional field 1), that value is **not** automatically transferred to the system's secondary email field. Extra fields are text-only data collection and are not linked to system notification fields. You must manually copy the email from the extra field into the booking's **Additional settings** → secondary email field for the second parent to actually receive notifications.

## What does the "Date of last registration update" field mean in exports?

The **Date of last registration update** column reflects the timestamp of the most recent change to that registration record — not necessarily any specific event like a cancellation.

It updates whenever **any** field on the registration changes, including:

- payment status changes (paid, partially paid, refunded)
- cancellation or deletion of the registration
- restoring a previously cancelled registration
- changes to notes, assigned class, instructor, or other fields

**Practical implications:**

- If a registration has status `deleted` or `cancelled`, the date shown is **not guaranteed to be the cancellation date** — it is the date of the last change, which may have happened after the cancellation (e.g. a payment adjustment).
- To find the exact cancellation date for a cancelled registration, use the dedicated **Cancellation date** field in the export if available, rather than relying on the last-update timestamp.
- If you are filtering exports for cancelled registrations and need accurate timing, cross-reference the registration status column with the cancellation date column rather than the last-update column.

---

## How do I hide a class from the public booking page and share a private link instead?

Use this when you have classes that should not be publicly listed — for example, school partnership sessions, invite-only groups, or franchise-internal classes.

**Step 1 — Disable public visibility for the class:**

1. Go to **Programmes** → open the programme → select the **Class**.
2. Open **Settings → Online Registration**.
3. Uncheck `Display in catalogue` (or disable `Allow online booking` to also block booking from direct links).
4. Save.

The class will no longer appear in your public booking widget or booking page catalogue.

**Step 2 — Share a private direct link:**

1. Go to **Programmes** → open the programme → select the **Class**.
2. In the class listing, click **Copy link** (or use the **Customize** option to pre-fill specific details).
3. Share the link directly with the relevant group (e.g. via email or WhatsApp to the school contact).

Parents who receive the direct link can still register — the class is hidden from the public catalogue but bookable via the private URL.

> **Note:** If you want to prevent *any* online booking (not just public listing), disable `Allow online booking` rather than just `Display in catalogue`. Admins can still create bookings manually from the admin panel regardless of this setting.

## Why is my programme not showing on the booking page?

Both `Allow online booking` and `Display in catalogue` must be enabled for a programme to appear on your public booking page.

1. Go to **Programmes** → select the programme → **Edit Settings**.
2. Open the **Online Booking** tile.
3. Verify that `Allow online booking` is toggled **on**.
4. Verify that `Display in catalogue` is checked.
5. Save the settings.

If only one of these is enabled, the programme will not be visible to clients. `Allow online booking` controls whether the programme accepts registrations, while `Display in catalogue` controls whether it appears in the website menu and booking form list.
