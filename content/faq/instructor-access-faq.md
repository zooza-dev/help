---
title: "Instructor Access and Roles FAQ"
description: "Instructors go to your Zooza app URL (e.g., asia.zooza.app), enter their email address, and receive a secure login link by email."
slug: "instructor-access-faq"
type: "faq"
product_area: "Settings"
sub_area: ""
audience: ["admin"]
tags: ["attendance", "booking", "client", "communication", "import", "instructor", "loyalty", "onboarding", "payment", "role", "session", "settings"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-15"
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

## An instructor says they can't find "Activities → Classes" — only "Calendar" is visible

This is expected. Instructors with limited roles (Standard instructor, External instructor, Receptionist) only see **Activities → Calendar** in the left-hand menu. The **Classes** list under Activities is only available to Owners, Assistants, and Main instructors.

This means that guide steps like "Go to Activities → Classes → select sessions → Bulk edit" cannot be performed by a standard instructor. If an instructor needs to change session times, reschedule sessions, or bulk-edit, an admin or main instructor must do it on their behalf.

If the instructor should have access to the Classes list, change their role to **Main instructor** in **Settings → Team**.

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

If you need a substitute instructor to communicate with students, they must hold at least the **Instructor** role, which grants the right to send emails and SMS to their own clients. Alternatively, the **Main instructor** role provides broader communication access across all clients.

You can adjust roles at any time in **Settings → Team**.

## Why can't an instructor send an email from the session or group view?

This is a permissions limitation by role, not a bug.

When an instructor opens a session detail and tries to send a message to attendees, the option is restricted based on their role:

| Role | Can send email/SMS to clients |
|---|---|
| **External instructor** | No |
| **Instructor** | Yes — to clients enrolled in their own classes |
| **Lead instructor** | Yes — to clients enrolled in classes they can see |
| **Manager / Owner** | Yes — unrestricted |

If a lektor (instructor) reports they cannot find the email option on a session or group, check their role in **Settings → Team**. The most common fix is upgrading them from **External instructor** to **Instructor**.

**Important:** Role changes apply immediately — the instructor does not need to log out and back in.

> **SK:** Ak lektor hlási, že nemôže odoslať email z termínu alebo skupiny, skontrolujte jeho rolu v **Nastavenia → Tím**. Externý lektor nemá právo posielať správy klientom. Zmeňte rolu na **Lektor** a prístup sa sprístupní okamžite.

## How do instructor rate types work (per-session, per-student, per-hour)?

Zooza supports flexible rate types for calculating instructor compensation. When creating a rate in **Settings → Instructors**, you define the rate name and its duration in minutes. The three common configurations are:

- **Per-session (one-time)** — a flat amount paid for each session the instructor teaches, regardless of duration or number of students.
- **Per-hour** — an amount based on the session duration. Set the rate duration to 60 minutes.
- **Per-student** — <!-- REVIEW: Confirm whether per-student rates are natively supported or require manual calculation via the instructor report. -->

Each rate is created once and then assigned a monetary value per instructor — so the same rate (e.g., "Group Session") can pay different amounts to different instructors. You assign the rate to a class in the class settings, and it automatically applies to all sessions in that class, including for a second instructor if one is assigned.

To view calculated compensation, go to **Instructors → [select instructor] → Instructor report** and choose a date range.

## Related

- [Two instructors per class](../guides/two-instructors-per-class.md) — assign a main and assistant instructor to a class
- [User roles](../guides/user-roles.md) — full breakdown of all roles and their permissions
- [Instructor working hours](../setup/instructors-working-hours.md) — configure availability windows per instructor
- [Instructor rate and reward](../setup/instructor-rate-reward.md) — set up compensation rates
- [Instructor substitution](../guides/instructor-substitution.md) — manage cover and substitute instructors
