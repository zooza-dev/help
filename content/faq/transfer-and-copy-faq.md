---
title: "Transfer and Copy FAQ"
slug: "transfer-and-copy-faq"
type: "faq"
product_area: "Bookings"
sub_area: ""
audience: ["admin"]
tags: ["transfer", "copy"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-15"
---

# Transfer and Copy FAQ

## How do I transfer a booking from one class to another?

Open the booking detail for the participant you want to move. Click **Transfer** to open the transfer dialog. Use the search field to find the target class, then select it. The dialog lets you configure several options before confirming:

1. Choose whether to keep the existing payment schedule or apply a new one.
2. Choose whether to send a confirmation notification to the client.
3. Confirm the transfer.

If you are transferring multiple participants within the same booking, you need to repeat the search for each participant. The search field does not currently remember the previous selection between participants.

## What happens to the payment schedule during a transfer?

By default, the transfer dialog may apply the payment schedule from the target class. To keep the original payment schedule unchanged, make sure to tick **Do not change payments** before confirming the transfer.

If you forget to tick this option, the system silently replaces the payment schedule with the one configured on the target class. This is the most common mistake during transfers.

## The transfer search only shows group names, not course names. How do I find the right group?

The transfer search field searches by **group name**, not by course (programme) name. If you type the course name (e.g. "Baby 1"), the search may return no results because that is the course name, not the group name.

To find the correct group:

1. Leave the search field empty or type part of the group name (e.g. the day of week, time, or location).
2. Use the instructor filter to narrow results if you know who teaches the target class.
3. If you are unsure of the group name, open the target programme in a separate tab and check the group names listed there.

<!-- REVIEW: A day-of-week filter for the transfer search has been requested and may be added in a future release. -->

## How do I copy bookings from one term to the next?

To continue a client into a new term (billing period), use the **Copy** function on the booking detail. This creates a new booking in the target class with the same participant and client data.

1. Open the booking you want to carry forward.
2. Click **Copy** (or **Continue**, depending on context).
3. Select the target class for the new term.
4. Review the new booking and confirm.

Note that copied bookings do not automatically send a confirmation email to the client. If you need the client to receive a confirmation, send it manually after copying.

## What settings carry over when copying a booking?

When you copy a booking, the participant and client information carries over. However, **payment schedules do not copy**. The new booking receives the payment schedule configured on the target class.

This means you should review the payment details on the new booking after copying. If a different price or schedule is needed, adjust it manually on the new booking.

<!-- REVIEW: A bug was reported where copying a booking incorrectly double-counted a block in the price calculation. This was fixed, but verify pricing after copy if blocks are in use. -->

## How do I fix a wrong payment schedule applied during a transfer?

If you forgot to tick **Do not change payments** and the system applied the target class's payment schedule:

1. Open the transferred booking.
2. Go to the payment section of the booking detail.
3. Manually adjust the owed amount to match the correct value.
4. If a payment template was applied, remove or replace it with the correct one.

You can verify what happened by checking the booking logs. If the transfer log shows a debt amount that does not match what you expected, it confirms that the payment schedule was overwritten during the transfer.

## Can I transfer a trial booking to a different session?

You do not need a full transfer for this. There are two approaches:

1. **If make-up lessons are enabled on the programme** -- the client can unsubscribe from the trial session in their profile and rebook onto a different available session themselves.
2. **Manual method (admin)** -- open the trial booking, go to attendance, and use the **Add to session** button at the top. Select the desired session from the list and enrol the client. This keeps the trial booking in its original class but adds attendance to a session in another class or time.

A full transfer of the booking to a different class is also possible but is usually unnecessary for a single trial session. If you do transfer, be aware that blocks and capacity settings may interact with trials in unexpected ways.

## How do I move a client to a "collection bin" or lead group?

Create a dedicated group that acts as a holding area (sometimes called a "collection bin" or lead group). Then transfer the booking into that group:

1. Set up a group with no sessions or a minimal schedule to serve as your collection bin.
2. Open the client's current booking and click **Transfer**.
3. Search for and select the collection bin group.
4. Tick **Do not change payments** to avoid applying a payment schedule from the collection bin.
5. Confirm the transfer.

This approach lets you keep the client's data and booking history while removing them from an active class. When the client is ready to rejoin, transfer them out of the collection bin into the appropriate class.

<!-- REVIEW: Transferring registrations between franchise accounts (offline to online) within a network is planned for Q1 2026. Until then, cancel the original booking (do not delete it) to preserve payment history. -->
