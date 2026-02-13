---
title: Power BI Data description
slug: power-bi-data-description
type: guides
product_area: Settings
sub_area: ""
audience:
  - admin
tags: []
status: published
source_legacy_path: legacy/0106_Welcome to Zooza.html
source_language: en
needs_screenshot_replacement: false
last_converted: 2026-02-11
intercom_id: 13728613
intercom_sync: false
---

# Power BI Data description

At the moment Zooza provides all kinds of static data about programmes, bookings or instructors containing the entire company history. You can explore the following tables:


1. Attendance
2. Programmes
3. Sessions
4. Labels
5. Orders
6. Places
7. Bookings
8. Schedules
9. Instructor rates
10. Instructor rates types

## Attendance


The attendance table records a detailed history of each participant’s attendance for a session. Each row represents a single attendance instance linked to a specific booking. Key information captured in this table includes session type (standard, make-up session), attendance status, records whether the upcoming session notification email was sent to this attendance record.

![Screenshot](../../assets/images/customizing-widgets-01.png)

Tip: To assemble a complete view of each participant’s journey, join Attendance with table Bookings, Schedules, Programmes or Sessions.


## Programmes


The Programmes table serves as the central repository for all programme configurations and options. Each record represents a distinct programme and is identified by a unique id, which can be used to link to related tables (e.g., Schedules, Bookings, Sessions, Attendance). Key columns include information from tiles in the application:

1. Price and payment
2. Online registration
3. Settings
4. Make-up sessions
5. Feedback
6. Auto-enrollment
7. Trial
8. Boolean flag 0/1 whether the programme uses additional fields

## Sessions


The Sessions table stores every session instance - both scheduled and deleted - along with its core details and calculated participation metrics. Each row represents one session occurrence and is keyed by id. Key columns include :

1. Session status (scheduled/deleted/unplanned)
2. Date & Time
3. Location
4. Instructor details including payroll settings
5. Static session details - any additional settings visible in the session’s detail view, such as programme, class, session name, description, capacity, etc.
6. Attendance metrics (calculated number of participants, number of cancellations, waitlists,...)

## Labels


Labels applied to highlight programmes, classes, or bookings appear in this table and it contains all information just like in Zooza’s Labels section.

![Screenshot](../../assets/images/customizing-widgets-01.png)

Tip: We recommend joining it with a schedules table with __calc__public__labels.


## Orders


This table lists every order (purchased product) processed in Zooza- complete with payment details and user information—and, when an order is placed during programme booking, its corresponding booking id appears in the payments_managed_by column, so you will want to join it with the Bookings table.

## Places


This table provides all active and inactive Zooza locations with their static details and is ideal for regional overviews when joined with the Schedules and Sessions tables.

## Bookings


This table captures every aspect of a booking—payment details and schedules, client and programme information, trial workflows, business order indicators, and any custom fields—and includes calculated metrics such as payment status, attendance and cancellation counts, unused make-up sessions, and other key summary values.

## Schedules


The Schedules table stores every detail visible in the class detail view, including:

1. Class Details: name, date & time, duration, instructor, and location
2. Capacity & Booking: class capacity, total bookings, trial bookings, and waitlist count
3. Pricing & Payments: programme price, payment settings, and debt summary (total issued, paid, and outstanding balance)
4. All settings visible in settings tile in Zooza (online registration, class properties, etc.)
5. Performance Metrics: average feedback score and session count
6. Instructor details including rates

![Screenshot](../../assets/images/customizing-widgets-01.png)

Tip: Because it aggregates both static settings and dynamic metrics, you can join Schedules with any related table—by schedule_id, course_id, instructor_id, or place_id—to build a complete view.

## Instructor rates

This table records instructor rates—including a recalculated unit_amount (per-minute rate for consistency across varying durations)—and is referenced by the Schedules and Sessions tables.

![Screenshot](../../assets/images/customizing-widgets-01.png)

Tip: Join on trainer_rate_type and trainer_id with the Instructor Rates Types and Schedules tables.

## Instructor rates types


This table lists all instructor rate types used in payout reports and is best joined with the Instructor Rates table.
