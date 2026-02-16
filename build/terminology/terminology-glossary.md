# Zooza Terminology Glossary

Reference table of canonical Zooza terms and their deprecated synonyms.
Generated: 2026-02-16 | Source: `build/terminology/dictionary.json`

---

## Core Concepts

| Canonical term              | Replaces (do not use)                                                                                  | Exceptions / notes                                        |
| --------------------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------- |
| **programme**               | course                                                                                                 | —                                                         |
| **class**                   | group, timetable                                                                                       | Keep "target group", "age group"                          |
| **session**                 | event, lesson                                                                                          | Keep "paid event", "multi-day event"                      |
| **booking**                 | registration                                                                                           | Keep "online registration", "registration fee"            |
| **client**                  | customer                                                                                               | —                                                         |
| **instructor**              | lecturer, teacher, trainer, tutor                                                                      | —                                                         |
| **make-up session**         | replacement lesson, replacement hour, catch-up lesson, catch-up session, make-up lesson, make-up class | "replacement credit" → "make-up credit"                   |
| **entry pass**              | voucher, season pass, season ticket, permanent pass, punch card                                        | Keep "discount voucher", "gift voucher"                   |
| **lead collection class**   | group interested, group – interested, class interested, interest group, collecting basket              | The *Interested* class type in the app                    |
| **linked classes**          | group connection, class connection                                                                     | Verb form: "link classes"                                 |
| **Pay-as-you-go programme** | open course, open programme                                                                            | Keep "open bookings" (booking status, not programme type) |

## UI Elements

| Canonical term | Replaces (do not use) | Notes |
|---|---|---|
| **Client Profile** | Parent Portal, Parent Zone, Parent Profile | Works for parents and non-parent clients |
| **booking form** | registration form | "online registration" is kept as feature name |

## Actions / Verbs

| Canonical term     | Replaces (do not use)             | Exceptions                                  |
| ------------------ | --------------------------------- | ------------------------------------------- |
| **log in**         | sign in                           | Keep "sign up" (= register/book)            |
| **cancel session** | sign out, unregister, unsubscribe | Keep "unsubscribe from email/notifications" |

## Attendance States

| Canonical state | Replaces |
|---|---|
| **Will attend** | — |
| **Attended** | — |
| **Cancelled** | Unsubscribed |
| **Did not attend** | Absent |

## Payment Terms

| Canonical term | Notes |
|---|---|
| **payment template** | Config/settings object. Do NOT merge with "payment plan" |
| **payment plan** | Applied instance on a booking. Distinct from template |

---

## Quick Reference: Slug Renames

Old slugs are redirected (301) to new canonical slugs.

| Old slug | New slug |
|---|---|
| course-group-lesson-definition | programme-class-session-definition |
| course-settings | programme-settings |
| course-settings-tile | programme-settings-tile |
| edit-events-in-courses | edit-sessions-in-programmes |
| new-course-existing-clients | new-programme-existing-clients |
| individual-lessons-climbing-wall | individual-sessions-climbing-wall |
| individual-lessons-group-interested | individual-sessions-lead-collection |
| individual-lessons-with-free-lesson | individual-sessions-with-free-session |
| trial-lessons | trial-sessions |
| automatic-event-notification | automatic-session-notification |
| edit-event-notification-template | edit-session-notification-template |
| send-email-after-event | send-email-after-session |
| viewing-billable-events | viewing-billable-sessions |
| registration-and-booking-faq | booking-faq |
| allowing-multiple-registration | allowing-multiple-booking |
| business-registration | business-booking |
| edit-payment-on-registration | edit-payment-on-booking |
| late-registrations | late-bookings |
| linked-registrations | linked-bookings |
| payment-tile-on-registration | payment-tile-on-booking |
| selling-products-during-registration | selling-products-during-booking |
| types-of-registrations | types-of-bookings |
| online-registration | *(unchanged — preserved)* |
| lecturer-substitution | instructor-substitution |
| two-lecturers-per-group | two-instructors-per-class |
| lecturers-working-hours | instructors-working-hours |
| how-to-create-paid-events | *(unchanged — "paid event" preserved)* |
| multi-day-event-with-product-offer | *(unchanged — "multi-day event" preserved)* |

---

## Navigation Menu Names (Style Guide)

Use these exact names when referring to Zooza main navigation:

Programmes | Classes | Calendar | Bookings | Orders | Clients | Payments | Settings | Widgets | Communication
