---
title: "Attendance and Catch-up Classes FAQ"
slug: "attendance-and-catchups-faq"
type: "faq"
product_area: "Calendar"
sub_area: ""
audience: ["admin"]
tags: []
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-13"
intercom_id: 13728486
intercom_sync: false
---

# Attendance and Catch-up Classes FAQ

## How do instructors mark attendance?

Instructors log in to Zooza (via `zooza.app`), open their **Calendar**, and select the current session. They see a list of registered children and mark each as "attended" or "absent". Attendance can be marked from both mobile and desktop.

Tip: Instructors should add Zooza to their phone's home screen so it works like a native app.

## Can an admin mark attendance on behalf of a instructor?

Yes. As an admin, go to **Calendar**, select the session, and mark attendance for any class — including past sessions. Admins can see all classes, while instructors only see their own.

## How do catch-up / make-up classes work?

When a child misses a session (marked as absent or session was cancelled), the system can offer a make-up session. The parent selects from available catch-up sessions in their Parent Portal.

Catch-up availability is based on:

- Real class capacity — there must be space in the alternative session.
- Programme match — the catch-up must be within a compatible programme/age group.

If no suitable session is available, the parent will not see a catch-up option.

## Why can't a parent see catch-up options?

Check these common causes:

1. The absence was not properly recorded — the session needs to be marked as "Cancelled" or the child as "Absent" in attendance.
2. There are no sessions with available capacity in a compatible class.
3. The catch-up window may have expired based on your automation settings.

As an admin, you can verify and trigger the catch-up option by toggling the attendance status (e.g., "Will attend" → "Cancelled" again).

## What do the attendance numbers mean on the calendar?

On the calendar view, you may see numbers like "12/15" and "4":

- **12/15** — the number of enrolled children vs. total class capacity.
- **4** — how many are actually booked into that specific session (including trials).

Hover over the numbers for a detailed breakdown.

## Is attendance tracking important for automations?

Yes. Marking attendance triggers automations — especially for trials. When a instructor marks a trial attendee as "attended", the system automatically sends the enrolment offer to the parent.

## What is the difference between "Did not attend" and "Unsubscribed" for replacement credits?

Only the **Unsubscribed** (excused/cancelled) attendance state generates a replacement credit. The **Did not attend** (no-show) state does NOT grant a replacement. This is by design — clients who simply do not show up without cancelling in advance are not eligible for make-up sessions.

If a client contacts you saying they did not receive a replacement credit, check the attendance record for that session. If it shows "Did not attend" instead of "Unsubscribed", that is why no credit was generated. You can manually change the state to "Unsubscribed" if the absence was legitimately excused.

## What does the "extra capacity for replacements" setting do?

This setting allows more students into a session than the standard group capacity, specifically for replacement (make-up) bookings. For example, if a group has a capacity of 10 and the extra capacity is set to +1, up to 11 students can attend that session — 10 regular plus 1 replacement.

You can configure this setting at two levels:

1. **Global (Programme level)** — Go to the Programme **Settings** and set the extra capacity value. This applies to all groups within the programme.
2. **Per group** — On the group detail, override the global value. You can choose to **replace** the global value entirely or **add to** the group's own capacity.

<!-- REVIEW: Confirm exact navigation path for per-group extra capacity setting — may be under group detail or group settings tab. -->

## How does the system automatically set "Did not attend" status?

If a client does not cancel before the session and does not check in (i.e., the instructor does not mark them as attended), the system automatically marks them as **Did not attend** after the session ends. The exact timing depends on the session end time.

This automatic status does NOT generate a replacement credit. Only the **Unsubscribed** state — where the client actively cancels before the session — creates a replacement credit.

## Sessions with no attendance requirement show as "unclosed attendance" on the Dashboard — how do I fix this?

This happens when sessions have attendance tracking enabled but nobody has marked attendance for them. The Dashboard flags these as "unclosed" because the system expects attendance to be recorded.

To resolve this, you have two options:

1. **Mark attendance** for those sessions — open each session from the Calendar and record who attended.
2. **Disable attendance tracking** on the group if attendance is not needed for those particular sessions. This prevents the Dashboard from flagging them.

<!-- REVIEW: Confirm exact setting location for disabling attendance tracking per group — likely under group settings or programme settings. -->
