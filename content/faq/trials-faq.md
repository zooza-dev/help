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
last_converted: "2026-02-12"
intercom_id: 13725614
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

1. Customer registers for a trial and receives a confirmation.
2. Customer receives a reminder before the trial session.
3. The teacher marks attendance after the trial.
4. The system automatically sends a booking link offering full enrolment.
5. Follow-up messages encourage enrolment.
6. If the offer is not used, the trial is marked as **Trial Lost**.

## Why does it say "class full" when a trial customer tries to enrol?

Trial bookings count towards class capacity. When the customer finishes their trial and tries to enrol in the same class, the system may show "class full" because their trial seat is still counted. If you see this happening consistently, contact support — it may be a calculation issue that needs a fix on the backend.

## Can an admin manually create a trial booking?

No. Trial bookings can only be created by parents through the online booking form. As an admin, you can only create standard enrolments. If needed, you can go through the booking form on behalf of a parent as a workaround.

## How do I handle a customer who wants to change their trial date?

If a parent can't make their booked trial, you can update their attendance in the system — mark the original session as absent and rebook them into a different session. This is managed through the booking detail.

## What happens when a customer cancels a trial?

If a customer cancels a trial, the system will follow the configured automation. You can manually change the status to **Trial Lost**, but this will not trigger automatic follow-up emails unless you explicitly choose to send one at that moment.

## Does teacher attendance tracking affect trials?

Yes. Tracking attendance is important because it triggers the trial-to-enrolment automation. When a teacher marks a trial attendee as "attended", it triggers the system to send the enrolment offer.
