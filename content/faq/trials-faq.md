---
title: "Trial Classes FAQ"
slug: "trials-faq"
type: "faq"
product_area: "Bookings"
sub_area: ""
audience: ["admin"]
tags: ["registrations"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-15"
intercom_id: 13728500
intercom_sync: false
---

# Trial Classes FAQ

## How do I set up trial classes?

Trials are configured per programme. Go to **Programme → Settings → Trial** to enable them, and **Programme → Automations → Trials** to configure the rules.

You can set:

1. Whether the trial is free or paid.
2. How many trial sessions are offered (usually one).
3. Whether trial dates are shown on the booking form (and how many days ahead).
4. Whether trial bookings count towards class capacity.
5. Whether a trial booking temporarily holds a spot in the class.

## What is the trial-to-enrolment flow?

The full automated flow is:

1. Client registers for a trial and receives a confirmation.
2. Client receives a reminder before the trial session.
3. The instructor marks attendance after the trial.
4. The system automatically sends a booking link offering full enrolment.
5. Follow-up messages encourage enrolment.
6. If the offer is not used, the trial is marked as **Trial Lost**.

## Why does it say "class full" when a trial client tries to enrol?

Trial bookings count towards class capacity. When the client finishes their trial and tries to enrol in the same class, the system may show "class full" because their trial seat is still counted. If you see this happening consistently, contact support — it may be a calculation issue that needs a fix on the backend.

## Can an admin manually create a trial booking?

No. Trial bookings can only be created by parents through the online booking form. As an admin, you can only create standard enrolments. If needed, you can go through the booking form on behalf of a parent as a workaround.

## How do I handle a client who wants to change their trial date?

If a parent can't make their booked trial, you can update their attendance in the system — mark the original session as absent and rebook them into a different session. This is managed through the booking detail.

## What happens when a client cancels a trial?

If a client cancels a trial, the system will follow the configured automation. You can manually change the status to **Trial Lost**, but this will not trigger automatic follow-up emails unless you explicitly choose to send one at that moment.

## Does instructor attendance tracking affect trials?

Yes. Tracking attendance is important because it triggers the trial-to-enrolment automation. When a instructor marks a trial attendee as "attended", it triggers the system to send the enrolment offer.

## Trials and blocks cause overbooking — what is happening?

This is a known limitation when a class uses both trial lessons and blocks (sub-periods within a group) at the same time.

When a client books a trial, the system can reserve a spot in the **group-wide** capacity. However, block capacity is calculated **per block**. Because the system does not know which specific block the trial client will eventually join, it cannot accurately reserve a per-block seat. In practice this means:

1. A trial booking may fill a session slot at the group level.
2. A paying client then registers for a specific block in the same group.
3. The system prioritises the paying client (confirmed revenue) over the trial (non-binding), which can push the session over its per-block capacity.

**Workaround:** Go to **Programme → Settings → Trial** and configure trial bookings to use **extra capacity** only. This ensures that trial reservations never consume spots intended for paying clients. The trial client is added on top of the normal capacity limit instead of inside it.

If you prefer to keep the current setting, you will need to manage overbooking manually — for example, by contacting the trial client and moving them to a different session that still has available spots. <!-- REVIEW: confirm "extra capacity" setting label matches current UI -->

## Can a client who finished a trial register again for a full course in the same class?

Yes. Once the trial process reaches a final state, the client can register for a full paid course in the same class. The exact flow depends on the trial status:

1. **Trial ended (Trial Won / Trial Lost):** Open the registration detail. You will see a **Start registration** button. Click it to convert the trial into a full paid booking. The client can also do this themselves through the enrolment link sent by the trial automation.
2. **Trial still in progress:** If the trial registration is still active (for example, in "Trial Started" state), the system will **not** allow a new registration with the same email into the same group. The trial must first reach a final state — either "Trial Won" or "Trial Lost" — before a new registration is possible.

To move a trial to a final state manually, change the registration status to **Trial Lost** (or **Trial Won** if they attended). After that, either use the **Start registration** button on the existing registration or have the client go through the booking form again.
