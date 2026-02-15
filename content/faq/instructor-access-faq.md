---
title: "Instructor Access and Roles FAQ"
slug: "instructor-access-faq"
type: "faq"
product_area: "Settings"
sub_area: ""
audience: ["admin"]
tags: []
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-15"
intercom_id: 13728491
intercom_sync: false
---

# Instructor Access and Roles FAQ

## How do instructors log in to Zooza?

Instructors go to your Zooza app URL (e.g., `asia.zooza.app`), enter their email address, and receive a secure login link by email. There is no password — they click the link to access the system.

## An instructor did not receive the invitation email — what should I do?

1. Check that the email address is correct in **Settings → Team**.
2. Try sending a new invitation.
3. Ask the instructor to check their spam/junk folder.
4. If using a corporate email, there may be delivery delays.

Note: Instructors do not need a formal invitation to log in. If they are listed as an instructor in the system, they can go to the Zooza app URL and request a login link with their email.

## What can instructors see and do?

Instructor access depends on their role:

- **Standard instructor** — sees only their own classes in the Calendar view. Can mark attendance.
- **Lead instructor** — can see other instructors' classes and the wider timetable. Useful for cover planning and coordination.

Instructors do not have access to payment details, reports, or full booking management.

## How do I change instructor permissions?

Go to **Settings → Team**, select the instructor, and adjust their role. If you want all instructors to see each other's classes (e.g., for a small team that covers for each other), set them as lead instructors.

## How do I add Zooza to a phone as an app?

Zooza works as a web app. To make it behave like a native app on mobile:

1. Open the Zooza URL in the phone's browser (Safari on iPhone, Chrome on Android).
2. Tap the share/menu button.
3. Select **Add to Home Screen**.

This creates an app icon that opens Zooza directly without the browser navigation bar.

## How do I deactivate an instructor's account without losing data?

Do not delete the instructor account. Instead, change their role to **Inactive instructor** in **Settings → Team**. This prevents the instructor from logging in but preserves all historical data — their attendance records, session assignments, and instructor reports remain intact.

If you delete the account, all data linked to that instructor is permanently lost and cannot be recovered. Always switch to the Inactive role first. You can find the role selector on the instructor's profile in **Settings → Team**.

## A substitute instructor cannot send emails to students on the session they cover — is this by design?

Email and communication access depends on the instructor's role. By default, **external instructors** have very limited permissions — they can mark attendance on sessions they are assigned to (including as a substitute) but cannot send emails or SMS to clients.

If you need a substitute instructor to communicate with students, they must hold at least the **Instructor** role, which grants the right to send emails and SMS to their own clients. Alternatively, the **Main instructor** role provides broader communication access across all clients. <!-- REVIEW: Confirm whether a substitute assigned to a single session inherits client communication rights for that session, or whether role-level permissions always apply. -->

You can adjust roles at any time in **Settings → Team**.

## How do instructor rate types work (per-session, per-student, per-hour)?

Zooza supports flexible rate types for calculating instructor compensation. When creating a rate in **Settings → Instructors**, you define the rate name and its duration in minutes. The three common configurations are:

- **Per-session (one-time)** — a flat amount paid for each session the instructor teaches, regardless of duration or number of students.
- **Per-hour** — an amount based on the session duration. Set the rate duration to 60 minutes.
- **Per-student** — <!-- REVIEW: Confirm whether per-student rates are natively supported or require manual calculation via the instructor report. -->

Each rate is created once and then assigned a monetary value per instructor — so the same rate (e.g., "Group Session") can pay different amounts to different instructors. You assign the rate to a class in the class settings, and it automatically applies to all sessions in that class, including for a second instructor if one is assigned.

To view calculated compensation, go to **Instructors → [select instructor] → Instructor report** and choose a date range.
