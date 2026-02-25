---
title: "Programmes, Timetables and Sessions FAQ"
slug: "programmes-timetables-sessions-faq"
type: "faq"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: []
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-15"
intercom_id: 13728496
intercom_sync: false
---

# Programmes, Timetables and Sessions FAQ

## What is the difference between programmes, timetables, and sessions?

- **Programme (Programme)** — the top-level entity (e.g., "Beginners Swimming"). It holds pricing, settings, and automation rules.
- **Timetable (Class/Class)** — a specific scheduled class within a programme (e.g., "Monday 9:00 AM at Main Hall"). It defines the recurring pattern, location, and instructor.
- **Sessions** — individual occurrences of a class (e.g., "Monday 6 January 9:00 AM"). Sessions are generated from the timetable and can be edited individually.

Changes made at the **timetable** level (e.g., assigning an instructor) do not always cascade to existing individual sessions. You may need to update sessions separately using bulk edit.

## How do I assign an instructor to sessions?

Assigning an instructor at the timetable level applies to future sessions. For existing sessions, use the **bulk edit** feature:

1. Go to the class detail.
2. Select the sessions you want to change.
3. Use bulk edit to assign the instructor.

## How do I change the time of a class?

You cannot change the time directly in the timetable settings for existing sessions. Instead:

1. Open the class detail.
2. Select the sessions that need the time change.
3. Use **bulk edit** to update the time.

You can choose whether to send a notification to parents about the change.

## How do I move a class to a different programme?

Open the class detail, go to **Settings / Edit → Other settings**, and change the programme from the dropdown. Save and refresh.

## How do I copy a class?

You can duplicate a class to create a similar one at a different time or location. When copying, double-check that all settings (price, payment methods, extra fields) have carried over correctly — some settings may need to be re-applied.

## How do I add a new class to an existing programme?

Go to the programme overview and click **New Class**. Fill in the class name, billing period, location, instructor, capacity, and session schedule. If the class should have a different price than the programme, enter it in the price step — otherwise the programme price applies automatically. For a full walkthrough, see [Creating a class](../guides/creating-a-class.md).

## What is the difference between a Fixed Period class and a Lead Collection class?

A **Fixed Period** class has scheduled sessions with specific dates and times — this is the standard class type for courses, terms, and camps. A **Lead Collection** class has no sessions initially — it is used to collect interest from potential clients before you finalise the schedule. Once you add sessions to a lead collection class, it becomes a regular fixed period class. See [Lead collection](../guides/lead-collection.md) for details.

## Can I set a different price for each class in the same programme?

Yes. When creating or editing a class, you can enter a class-level price that overrides the programme price. This is useful when different levels, locations, or time slots have different pricing. If you leave the class price empty, the programme price applies. See [Creating a class](../guides/creating-a-class.md).

## What do the financial numbers on the class tile mean?

Each class tile shows three financial figures (recalculated every 30 minutes):

- **Paid debt** — total amount already paid across all bookings.
- **Issued debt** — total debt created from all booking types (including late bookings and waiting list).
- **Balance** — current account status (difference between issued and paid).

## How do I hide a class from online registration?

In the class settings, you can toggle visibility for the online booking form. This keeps the class in the system for internal management but hides it from the public booking page.

## Why do changes I make not appear immediately?

Zooza uses browser caching to speed up page loading. When you create or edit something (like a location or class), the change may take a moment to appear. A quick browser refresh (Cmd+R on Mac, Ctrl+R on Windows) usually resolves this.

## How do I bulk-delete courses that have no bookings or classes?

Admins cannot bulk-delete courses directly from the application interface. To delete courses that have no registrations or classes (groups), you must send a list of course IDs to Zooza support, who will remove them from the database on your behalf.

Before requesting deletion:

1. Verify that each course has **no active registrations** and **no groups** attached.
2. If a course still contains groups with historical registrations you want to preserve, move those groups to an archive course first (via group settings — change the programme).
3. Compile the course IDs (visible in the URL when viewing a course, e.g., `#courses/6455`) and send them to support.

Courses that still contain registrations or groups cannot be deleted — they must be archived instead. <!-- REVIEW: confirm whether self-service course deletion is planned -->

## After rescheduling sessions, holiday-skip rules no longer apply — why?

When you create a class, Zooza generates sessions that respect your holiday and public-holiday skip settings. However, if you later **bulk-reschedule** those sessions to a different weekday or time, the system treats this as a manual override and **does not re-apply** the holiday-skip rules to the new dates.

This means sessions may land on public holidays or school vacation days after rescheduling.

**What to do after rescheduling:**

1. Open the class detail and review all rescheduled sessions.
2. Manually cancel or remove any sessions that fall on holidays or vacation days.
3. Add replacement sessions on valid dates if needed to maintain the correct total count.

The system displays a warning when you perform a bulk reschedule, reminding you to check the resulting dates. The admin who performs the change is responsible for verifying that the new session dates are correct.

<!-- REVIEW: Zooza support has acknowledged this as a known limitation and is evaluating whether holiday rules can be re-applied automatically after rescheduling. -->

## How do I change the price for new bookings without affecting existing ones?

Price changes on a programme or class apply **only to new registrations**. Existing registrations keep the price that was set at the time the client registered.

To update the price for future bookings:

1. Go to the programme or class settings.
2. Change the price to the new amount.
3. Save.

All new registrations (including clients who convert from a trial) will use the updated price. Clients who registered before the change retain their original price — their payment schedule is not recalculated.

If you need to adjust the price for an existing registration, you must edit the payment on that registration manually. See [Edit payment on booking](../guides/edit-payment-on-booking.md) for details.
