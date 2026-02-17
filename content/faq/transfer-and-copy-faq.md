---
title: "Transfer and Copy FAQ"
slug: "transfer-and-copy-faq"
type: "faq"
product_area: "Bookings"
sub_area: ""
audience: ["admin", "staff"]
tags: ["transfer", "copy", "move"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-17"
intercom_id: 13738683
intercom_sync: false
---

<!-- Synonyms: move booking, move client, relocate booking, presunúť klienta, kopírovať registráciu, presun registrácie -->

# Transfer and Copy FAQ

For a step-by-step walkthrough with screenshots, see [Transfer and copy bookings](../guides/transfer-and-copy-bookings.md).

## How do I transfer (move) a booking to another class?

Open the booking detail and click **Transfer** (in the Class card). The wizard lets you select the target class using filters (programme, location, instructor, day). Select **Transfer to another class**, review payments, and submit.

The original booking moves to the new class. The client gets the remaining sessions in the target class.

## What is the difference between Transfer and Copy?

- **Transfer** moves the booking — the original booking no longer exists in the old class.
- **Copy** creates a new booking in the target class — the original booking stays in the old class unchanged.

Use Transfer when the client is switching classes. Use Copy when the client wants to continue in a new term, or when they want an additional class alongside the current one.

## What happens to the payment schedule during a transfer?

By default, the transfer dialog may apply the payment schedule from the target class. To keep the original payment schedule unchanged, tick **Do not change payments** before confirming.

If you forget to tick this option, the system silently replaces the payment schedule with the one configured on the target class. This is the most common mistake during transfers.

## What settings carry over when copying a booking?

When you copy a booking, the participant and client information carries over. However, **payment schedules do not copy**. The new booking receives the payment schedule configured on the target class.

Always review the payment details on the new booking after copying. If a different price or schedule is needed, adjust it manually.

## How do I copy bookings from one term to the next?

Open the booking you want to carry forward and click **Copy booking**. Select the target class for the new term, review the payment setup, and submit.

Copied bookings do not automatically send a confirmation email to the client. Check **Send confirmation email** during the process if you want the client to receive payment instructions.

Make-up credits and attendance history stay with the original booking. The copied booking starts clean.

## How do I fix a wrong payment schedule applied during a transfer?

If you forgot to tick **Do not change payments** and the system applied the target class's payment schedule:

1. Open the transferred booking.
2. Go to the **Payments** section.
3. Manually adjust the owed amount to match the correct value.
4. If a payment template was applied, remove or replace it with the correct one.

Check the booking logs to verify what happened. If the transfer log shows a debt amount that does not match expectations, the payment schedule was overwritten during the transfer.

## The search only shows class names, not programme names. How do I find the right class?

The search field searches by **class name**, not by programme name. If you type the programme name (e.g. "Baby 1"), the search may return no results.

To find the correct class:

1. Leave the search field empty or type part of the class name (e.g. the day of the week, time, or location).
2. Use the **Programme**, **Location**, or **Instructor** filter to narrow results.
3. If unsure of the class name, open the target programme in a separate tab and check the class names listed there.

## Can I transfer a trial booking to a different session?

You do not need a full transfer for this. There are two approaches:

1. **If make-up sessions are enabled on the programme** — the client can unsubscribe from the trial session in their profile and rebook onto a different available session themselves.
2. **Manual method (admin)** — open the trial booking, go to attendance, and use the **Add to session** button. Select the desired session and enrol the client. This keeps the trial booking in its original class but adds attendance to a session in another class or time.

A full transfer is also possible but usually unnecessary for a single trial session.

## How do I move a client to a "collection bin" or holding class?

Create a dedicated class with no sessions or a minimal schedule to serve as a holding area. Then transfer the booking into that class:

1. Open the client's current booking and click **Transfer**.
2. Search for and select the holding class.
3. Tick **Do not change payments** to avoid applying a payment schedule from the holding class.
4. Confirm the transfer.

When the client is ready to rejoin, transfer them out of the holding class into the appropriate active class.

## Can external instructors transfer or copy bookings?

No. External instructors have attendance-only access. Only admins, owners, and standard instructors can transfer or copy bookings.

## Related

- [Transfer and copy bookings — full guide](../guides/transfer-and-copy-bookings.md)
- [Bookings List Reference](../reference/bookings-list.md)
- [New Programme with Existing Clients](../guides/new-programme-existing-clients.md)
