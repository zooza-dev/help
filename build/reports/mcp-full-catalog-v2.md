# Zooza MCP — Complete Catalog v2

**Version:** 2.1  
**Date:** 2026-05-23  
**Method:** Full client journey, bottom-up from evidence. New client → first sale → daily ops → business intelligence.  
**Format:** `R` = read/query · `W` = write/action · ★★★ high evidence · ★★ medium · ★ low  
**Change from v1:** +80 tools · +10 skills · +10 artifacts. New sections: Foundation, Onboarding, Loyalty, Integrations.

---

## Contents

F. [Foundation Prerequisites](#f-foundation-prerequisites) — **NEW**
0. [Account & Onboarding](#0-account--onboarding) — **NEW**
1. [Programmes](#1-programmes)
2. [Classes (Groups)](#2-classes-groups)
3. [Sessions](#3-sessions)
4. [Clients](#4-clients)
5. [Bookings / Registrations](#5-bookings--registrations)
6. [Payments & Billing](#6-payments--billing)
7. [Make-up / Replacement Credits](#7-make-up--replacement-credits)
8. [Calendar & Attendance](#8-calendar--attendance)
9. [Instructors](#9-instructors) — **expanded: rates, performance, payroll**
10. [Communication & Notifications](#10-communication--notifications) — **expanded: automation, WhatsApp**
11. [Services & Products (Upsell)](#11-services--products-upsell) — **expanded: upsell intelligence**
12. [Business Reports & Intelligence](#12-business-reports--intelligence) — **expanded: churn, LTV, forecast**
13. [Settings & Configuration](#13-settings--configuration)
14. [Loyalty & Rewards](#14-loyalty--rewards) — **NEW**
15. [Integrations & Health Checks](#15-integrations--health-checks) — **NEW**
16. [Skills — Compound Workflows](#16-skills--compound-workflows) — **expanded: 25 skills**
17. [Artifacts — Reusable Outputs](#17-artifacts--reusable-outputs) — **expanded: 30 artifacts**
18. [Selection Guide: The Wow 30+30](#18-selection-guide-the-wow-3030)

---

## F. Foundation Prerequisites

Structural entities that must exist before any operational tool works. Handled by the `first_sale_setup` skill (SK-01) for new operators. For existing operators these are already in place.

**Philosophy:** use defaults wherever possible. The agent asks only for the minimum required input. After creation, it tells the operator what defaults were applied and offers to adjust.

| # | Tool | R/W | Creates | Required inputs | Default applied | API status |
|---|------|-----|---------|----------------|-----------------|-----------|
| F-01 | `create_location` | W | Venue / studio | Name, address | — | ✅ READY — `places.php` |
| F-02 | `create_instructor` | W | Staff member | Name, email, role | Role: instructor | ✅ READY — `users.php` |
| F-03 | `create_programme` | W | Programme (course) | Name, type, price | Trial: off · Auto-enrol: off · Public: on · Aliquot: off | ✅ READY — `courses.php` |
| F-04 | `create_class` | W | Recurring group | Day, time, instructor, capacity | Location: first available | ✅ READY — `schedules.php` |
| F-05 | `create_payment_template` | W | Billing model | Type (termly/monthly/instalment), amount, due dates | — | ❌ MISSING — `payment_schedules_templates.php` exists but is empty |
| F-06 | `set_billing_period` | W | Term dates | Start date, end date, session count | Holidays: none | ✅ READY — `billing_periods.php` |
| F-07 | `setup_stripe` | W | Payment connection (card) | — | Returns OAuth URL; operator completes in browser | ⚠️ PARTIAL — OAuth callback exists; needs initiation endpoint |
| F-08 | `setup_gocardless` | W | Payment connection (direct debit) | — | Returns OAuth URL; operator completes in browser | ⚠️ PARTIAL — OAuth callback exists; needs initiation endpoint |
| F-09 | `verify_payment_setup` | R | — (health check) | — | — | ✅ READY — composite of existing status checks |

**Sessions (F-10 omitted):** Auto-generated from F-04 (`create_class`). No separate tool needed.

**Products and services:** NOT in the foundation tier. They are feature prerequisites only for upsell tools — a complete business runs without them. The agent prompts for product/service creation contextually when the operator first uses an upsell tool.

### Payment gateway note

Stripe and GoCardless both require OAuth browser redirect. The agent cannot complete this autonomously. The flow is:

1. Agent calls `setup_stripe` or `setup_gocardless` → returns OAuth URL
2. *"Open this link and connect your account. Come back when done."*
3. Agent calls `verify_payment_setup` → confirms connection active

The agent must pause and wait for the operator's confirmation before proceeding past this step.

---

## 0. Account & Onboarding

The first 72 hours. A new operator needs to go from "I just signed up" to "I have a booking link on my website and my first client can pay." Every broken step here is a lost customer.

| # | Tool | R/W | Description | Evidence |
|---|------|-----|-------------|----------|
| OB-01 | `get_account_readiness_score` | R | Checklist + score: payment connected? programme created? class has sessions? booking link works? email configured? | ★★★ Onboarding FAQ — "What should I check before going live?" |
| OB-02 | `run_prelaunch_audit` | R | Scan all classes in a programme for inconsistent settings: missing payment methods, mismatched prices, form fields that differ, test bookings not deleted | ★★★ Onboarding FAQ — #1 pre-live question |
| OB-03 | `get_widget_embed_code` | R | Return the `<iframe>` embed snippet + QR code + direct booking URL for any programme or class | ★★★ Intercom ★★ |
| OB-04 | `setup_branding` | W | Set organisation logo, brand colour, custom domain for widget | ★★ |
| OB-05 | `create_demo_programme` | W | Create a sandboxed test programme with zero-price booking; clean up test data after | ★★ Onboarding FAQ |
| OB-06 | `migrate_clients_bulk` | W | Create bookings for existing clients migrating from another system; optionally apply a fee-waiver discount code | ★★★ Onboarding FAQ — "Migrate from another system" |
| OB-07 | `check_settings_consistency` | R | Compare settings across all classes within a programme — surface anything that differs (price, payment method, form fields, trial enabled) | ★★★ Kate/Anna both hit inconsistency issues |
| OB-08 | `get_booking_page_url` | R | Return the brand-level booking page URL (e.g. `yourbrand.zooza.online/booking/`) plus all individual class links | ★★★ |
| OB-09 | `first_steps_summary` | R | Narrative summary of what is set up, what is missing, and the recommended next 3 actions before going live | ★★★ new operator daily pain |

---

## 1. Programmes

The top-level container. Settings here cascade down to all classes and sessions.

| # | Tool | R/W | Description | Evidence |
|---|------|-----|-------------|----------|
| P-01 | `list_programmes` | R | List all programmes with status, term, active registrations, revenue | ★★★ |
| P-02 | `get_programme` | R | Full detail: settings, classes, stats, booking link | ★★★ |
| P-03 | `get_programme_booking_link` | R | Return the public registration URL for a programme | ★★★ Intercom ★★ |
| P-04 | `set_programme_trial` | W | Enable/disable trial sessions; set trial price, capacity, duration | ★★ |
| P-05 | `set_programme_auto_enrolment` | W | Enable auto-continuation; set target group or "same group" | ★★★ |
| P-06 | `set_programme_aliquot` | W | Enable/disable pro-rata pricing for late joiners; set calculation method | ★★ |
| P-07 | `set_programme_down_payment` | W | Set registration fee amount; enable/disable for new vs returning clients | ★★ |
| P-08 | `set_programme_make_up_policy` | W | Enable make-up sessions; set expiry (days/term), max credits per term | ★★★ |
| P-09 | `set_programme_capacity` | W | Set max registrations; set overbooking rules | ★★ |
| P-10 | `set_programme_extra_fields` | W | Add/remove custom registration form fields; set required/optional | ★★ Intercom |
| P-11 | `set_programme_payment_template` | W | Assign a payment template (billing model) to a programme | ★★★ |
| P-12 | `set_programme_visibility` | W | Set public/private/unlisted; enable/disable online booking | ★★★ Intercom |
| P-13 | `set_programme_consents` | W | Configure consent fields (T&C, photo/video); set mandatory/optional | ★★ |
| P-14 | `bulk_update_programmes` | W | Apply any setting from P-04 to P-13 across multiple programmes at once | ★★★ |
| P-15 | `copy_programme` | W | Copy programme structure (without registrations) for a new term | ★★★ |
| P-16 | `archive_programme` | W | Archive a programme; warns if active registrations or unpaid invoices exist | ★★★ Intercom #1 |
| P-17 | `get_auto_enrolment_responses` | R | Show confirmed / pending / declined per programme and target group | ★★★ Intercom explicit gap |

---

## 2. Classes (Groups)

One class = one recurring group within a programme (e.g. "Monday 10:00 Ballet Tiny Tots").

| # | Tool | R/W | Description | Evidence |
|---|------|-----|-------------|----------|
| C-01 | `list_classes` | R | List classes with capacity, occupancy, instructor, location, next session | ★★★ |
| C-02 | `get_class` | R | Full detail: sessions, enrolled clients, waiting list, payment status | ★★★ |
| C-03 | `create_class` | W | Create a new class under a programme; set schedule, instructor, location, capacity | ★★★ |
| C-04 | `update_class` | W | Change time, instructor, location, capacity, public/private on a class | ★★★ Intercom |
| C-05 | `set_class_instructor` | W | Assign or change instructor; choose scope: all / future / from date | ★★★ |
| C-06 | `set_class_capacity` | W | Change max spots; optionally notify waiting list if capacity increases | ★★ |
| C-07 | `set_class_visibility` | W | Make class public / private / hidden from registration | ★★ |
| C-08 | `get_class_roster` | R | Full list of enrolled clients with status, payment, attendance rate | ★★★ |
| C-09 | `get_class_waiting_list` | R | Ordered waiting list with days waiting and contact details | ★★★ Zoho 34 |
| C-10 | `copy_class` | W | Duplicate a class (structure only) to same or different programme | ★★★ |
| C-11 | `archive_class` | W | Archive a class; warns if active registrations remain | ★★★ |
| C-12 | `bulk_update_classes` | W | Apply setting changes across multiple classes at once | ★★★ |
| C-13 | `get_class_capacity_overview` | R | Visual summary: full / nearly full / has space — across all classes | ★★★ |

---

## 3. Sessions

Individual occurrences of a class. Created automatically from the class schedule.

| # | Tool | R/W | Description | Evidence |
|---|------|-----|-------------|----------|
| S-01 | `list_sessions` | R | List sessions for a class or date range; filter by status | ★★★ |
| S-02 | `get_session` | R | Detail: enrolled clients, attendance status, notes, instructor | ★★★ |
| S-03 | `create_session` | W | Create a one-off session (not recurring); set date, time, instructor | ★★ |
| S-04 | `cancel_session` | W | Cancel one session; optionally notify clients and/or offer make-up | ★★★ |
| S-05 | `bulk_cancel_sessions` | W | Cancel all sessions on a date (or by instructor); notify clients; offer make-up | ★★★ Zoho 52 |
| S-06 | `reschedule_session` | W | Move a session to a different date/time; notify enrolled clients | ★★★ |
| S-07 | `set_session_instructor` | W | Override instructor for a specific session (substitution) | ★★★ |
| S-08 | `add_session_note` | W | Internal note on a session (visible to admin/instructor only) | ★★ |
| S-09 | `add_session_parent_message` | W | Message sent to all enrolled parents about this session | ★★ |
| S-10 | `get_sessions_for_day` | R | All sessions happening on a given date across all classes | ★★★ |

---

## 4. Clients

CRM entity within an account. One client = one child (or adult student). Parent/guardian is the account contact.

| # | Tool | R/W | Description | Evidence |
|---|------|-----|-------------|----------|
| CL-01 | `get_client` | R | Full profile: contact, consents, children, bookings, payment history, communication log | ★★★ |
| CL-02 | `list_clients` | R | List with filter: programme, group, status, unpaid, no booking, trial only | ★★★ |
| CL-03 | `create_client` | W | Create a new client record; set contact, children, consents | ★★★ Intercom |
| CL-04 | `update_client` | W | Update contact info, consents, notes | ★★ |
| CL-05 | `find_duplicate_clients` | R | Identify clients with same name or email who have multiple records | ★★★ WhatsApp Anna 15+ |
| CL-06 | `merge_clients` | W | Merge two client records; consolidate bookings, payments, history | ★★ |
| CL-07 | `resend_client_access` | W | Resend portal login link or PIN to client | ★★★ Zoho 54 |
| CL-08 | `get_client_consents` | R | Show all consent records for a client (T&C, photo/video, marketing) | ★★ Intercom |
| CL-09 | `update_client_consents` | W | Update consent status; log change with timestamp | ★★ |
| CL-10 | `get_sibling_clients` | R | Find all children under the same parent/account | ★★★ |
| CL-11 | `get_client_communication_log` | R | Full history of emails, SMS sent to this client | ★★ |
| CL-12 | `list_clients_without_booking` | R | Clients in the system with no active booking (leads, lapsed) | ★★★ 💰 |
| CL-13 | `list_clients_with_trial_only` | R | Clients who only have a trial registration and no full enrolment | ★★★ 💰 |
| CL-14 | `get_client_engagement_score` | R | Composite score from attendance rate, payment timeliness, communication response — low score = at risk | ★★★ new |
| CL-15 | `get_client_lifetime_value` | R | Total paid across all terms, programmes, services; tenure; average term value | ★★★ new 💰 |
| CL-16 | `create_manual_trial` | W | Admin creates a trial booking (walk-in, phone enquiry) — not possible through portal today | ★★★ W02 gap |
| CL-17 | `reschedule_trial` | W | Reschedule a "Trial lost" booking to a new date without creating a new registration | ★★★ W02 gap |

---

## 5. Bookings / Registrations

The core transactional record. One booking = one client in one class for one term.

| # | Tool | R/W | Description | Evidence |
|---|------|-----|-------------|----------|
| B-01 | `get_booking` | R | Full detail: status, payment plan, credits, attendance, documents, notes | ★★★ |
| B-02 | `list_bookings` | R | List with rich filter: status, payment status, class, programme, date, instructor | ★★★ |
| B-03 | `create_booking` | W | Create a manual registration; set client, class, payment plan, amount | ★★★ Zoho |
| B-04 | `cancel_booking` | W | Cancel a registration; optionally refund or leave credit | ★★★ |
| B-05 | `transfer_booking` | W | Move registration to a different class; option to carry payment balance | ★★★ Zoho 64 |
| B-06 | `duplicate_booking` | W | Copy registration to another class/term (same client) | ★★★ Zoho 43 |
| B-07 | `update_booking_status` | W | Change status: trial / enrolled / auto-enrolled / suspended / cancelled | ★★★ |
| B-08 | `set_payment_plan` | W | Set or replace the payment plan on a booking | ★★★ Zoho 124 |
| B-09 | `apply_credit` | W | Apply a monetary credit to reduce the next payment | ★★★ Zoho 26 |
| B-10 | `add_manual_payment` | W | Record a cash or bank transfer payment; generate invoice | ★★★ Zoho Payments 208 |
| B-11 | `get_payment_history` | R | All payments made on a booking with dates, method, amount | ★★★ |
| B-12 | `set_attendance` | W | Mark attended / absent / cancelled for a client on a session | ★★★ Zoho Calendar 52 |
| B-13 | `get_attendance_summary` | R | Attendance rate for a client across sessions in a term | ★★★ |
| B-14 | `generate_document` | W | Generate invoice / confirmation / receipt for a booking | ★★★ Zoho 117 |
| B-15 | `resend_document` | W | Re-send confirmation or invoice email to client | ★★★ |
| B-16 | `add_booking_note` | W | Internal note on a booking; visible to admin only | ★★ |
| B-17 | `set_booking_notifications` | W | Enable / disable specific notification types for this booking | ★★ Intercom |
| B-18 | `send_message_to_client` | W | Send a direct email or SMS to a specific booking's client | ★★★ |
| B-19 | `apply_sibling_discount` | W | Apply sibling discount across all bookings in a family | ★★★ Zoho 28, WhatsApp |
| B-20 | `get_booking_debt_status` | R | Current financial status: paid / overdue / overpaid / credit / no debt | ★★★ |
| B-21 | `calculate_prorata` | W | Calculate and apply pro-rata amount for a mid-term joiner | ★★★ WhatsApp Kate/Anna |
| B-22 | `pause_booking` | W | Temporarily suspend a booking (no-native-feature today); set resume date | ★★ WhatsApp Dom/Anna |
| B-23 | `bulk_update_bookings` | W | Apply setting or status change across multiple bookings at once | ★★★ |
| B-24 | `list_bookings_by_debt_status` | R | All bookings filtered by financial status (overdue / unpaid / credit) | ★★★ Zoho 208 |

---

## 6. Payments & Billing

| # | Tool | R/W | Description | Evidence |
|---|------|-----|-------------|----------|
| PAY-01 | `show_unmatched_payments` | R | Incoming payments not paired to any booking | ★★★ Zoho 68 |
| PAY-02 | `match_payment_to_booking` | W | Manually pair an unmatched payment to a booking | ★★★ |
| PAY-03 | `get_gocardless_status` | R | Connection health, expiry date, active mandates, reconnect link if needed | ★★★ Intercom P1 |
| PAY-04 | `reconnect_gocardless` | W | Trigger re-authentication flow for expired GoCardless connection | ★★★ |
| PAY-05 | `show_payment_mismatches` | R | Bookings where amount charged differs from expected (aliquot errors, wrong template) | ★★★ Zoho 23 |
| PAY-06 | `generate_invoice_batch` | W | Bulk generate and export invoices for a period (PDF / XML / CSV) | ★★★ Zoho 117 |
| PAY-07 | `create_payment_template` | W | Create a new billing template (termly / membership / one-off / instalment) | ★★★ |
| PAY-08 | `assign_payment_template` | W | Assign a payment template to a programme or class | ★★★ |
| PAY-09 | `bulk_change_payment_template` | W | Change payment template across all bookings in a group/programme | ★★★ WhatsApp Kate |
| PAY-10 | `initiate_refund` | W | Initiate a refund via Stripe; mark booking as refunded in Zooza | ★★★ WhatsApp Anna 100+ |
| PAY-11 | `apply_session_credit_bulk` | W | Apply a credit (cancelled session) to next payment for all bookings in a class | ★★★ Zoho 26 |
| PAY-12 | `create_discount_code` | W | Create a promo/discount code with type, value, validity, restrictions | ★★ Zoho 28 |
| PAY-13 | `send_payment_reminder` | W | Send payment reminder to unpaid clients; filter by class/programme/all | ★★★ Zoho 208 |
| PAY-14 | `list_billing_periods` | R | Show configured billing periods / blocks for a group or programme | ★★ WhatsApp Kate |
| PAY-15 | `set_billing_period` | W | Create or update a billing period block for a group | ★★ |

---

## 7. Make-up / Replacement Credits

The single largest Zoho cluster (227 tickets). Needs its own entity space.

| # | Tool | R/W | Description | Evidence |
|---|------|-----|-------------|----------|
| MU-01 | `get_makeup_credits` | R | All active make-up credits: client, group, expiry — filterable by location | ★★★ Zoho 227 P1 |
| MU-02 | `get_makeup_credits_for_client` | R | Make-up credit balance and history for a specific client | ★★★ |
| MU-03 | `apply_makeup_credit` | W | Book a client into a make-up session using their credit | ★★★ |
| MU-04 | `add_makeup_credit` | W | Manually add a make-up credit to a client's booking | ★★★ |
| MU-05 | `expire_makeup_credits` | W | Manually expire credits for a client or programme (e.g. end of term) | ★★ |
| MU-06 | `transfer_makeup_credit` | W | Transfer a make-up credit from one booking to another (sibling, new term) | ★★ Intercom |
| MU-07 | `show_makeup_report_by_location` | R | Summary: credits issued / used / expired per location — **doesn't exist in Zooza today** | ★★★ Intercom P1 gap |
| MU-08 | `show_makeup_report_by_programme` | R | Same but grouped by programme | ★★★ |

---

## 8. Calendar & Attendance

| # | Tool | R/W | Description | Evidence |
|---|------|-----|-------------|----------|
| CAL-01 | `get_calendar` | R | Calendar view for a day/week with sessions, instructor, location, capacity | ★★★ |
| CAL-02 | `get_session_register` | R | Attendance register for a session: enrolled clients, status, notes | ★★★ Zoho Calendar 52 |
| CAL-03 | `bulk_mark_attendance` | W | Mark attended/absent for multiple clients in one session | ★★★ |
| CAL-04 | `set_session_substitution` | W | Assign a substitute instructor for a session | ★★★ |
| CAL-05 | `add_session_internal_note` | W | Internal note on a session (not visible to clients) | ★★ |
| CAL-06 | `add_session_client_alert` | W | Alert/note visible on the client card for that session | ★★ |
| CAL-07 | `send_message_to_session_clients` | W | Send message to all parents/clients enrolled in a specific session | ★★★ |
| CAL-08 | `get_instructor_day_schedule` | R | All sessions for an instructor on a given day | ★★★ |

---

## 9. Instructors

Expanded. Now includes rates, payroll calculation, performance analytics, and substitution tracking.

| # | Tool | R/W | Description | Evidence |
|---|------|-----|-------------|----------|
| INS-01 | `list_instructors` | R | All instructors with classes, schedule, role | ★★★ |
| INS-02 | `get_instructor` | R | Profile, assigned classes, upcoming sessions, rate settings | ★★ |
| INS-03 | `create_instructor` | W | Add new instructor; set name, email, role, send invite | ★★★ Zoho Lecturers 30 |
| INS-04 | `update_instructor` | W | Update details, role permissions | ★★ |
| INS-05 | `assign_instructor_to_class` | W | Assign an instructor to a class (all future sessions) | ★★★ |
| INS-06 | `set_session_instructor` | W | Override instructor for a specific session only | ★★★ |
| INS-07 | `get_instructor_schedule` | R | Full schedule for a period with session counts | ★★ |
| INS-08 | `set_instructor_rate` | W | Set hourly / 45-min / performance rate for an instructor; set rate per class | ★★★ KB: instructor-rate-reward |
| INS-09 | `get_instructor_report` | R | Sessions taught, hours worked, sessions substituted, cancellations, total remuneration for a period | ★★★ KB: instructor-rate-reward |
| INS-10 | `calculate_instructor_payroll` | W | Sum rates × sessions for all instructors for a period; export as payroll table | ★★★ new — monthly pain |
| INS-11 | `set_cancellation_compensation` | W | Set what % of rate to pay when a session is cancelled (default 100%) | ★★ KB: instructor-rate-reward |
| INS-12 | `get_substitution_log` | R | History of who substituted for whom, cost of substitutions, frequency | ★★★ new |
| INS-13 | `report_instructor_performance` | R | Per-instructor: avg attendance rate, client retention rate, no-show rate, revenue associated, sessions taught | ★★★ new 💰 |
| INS-14 | `compare_instructors` | R | Side-by-side comparison of all instructors on: retention, attendance, revenue, hours, substitution frequency | ★★★ new — high wow factor |
| INS-15 | `get_instructor_working_hours` | R | Configured availability/working hours for scheduling | ★★ KB: instructors-working-hours |

---

## 10. Communication & Notifications

Expanded. Includes automation sequences, preview, communication calendar, WhatsApp, stats.

| # | Tool | R/W | Description | Evidence |
|---|------|-----|-------------|----------|
| COM-01 | `send_bulk_email` | W | Email all clients in a class / programme / custom filter | ★★★ Zoho 73 |
| COM-02 | `send_bulk_sms` | W | SMS to a filtered group | ★★ Zoho 29 |
| COM-03 | `resend_confirmation_email` | W | Resend booking confirmation to a client | ★★★ Zoho 12, WhatsApp Anna |
| COM-04 | `send_payment_reminder` | W | Payment reminder to unpaid clients (see PAY-13) | ★★★ |
| COM-05 | `get_email_automation_overview` | R | Map of all automated messages for a programme: trigger → template → timing | ★★★ Zoho 74, Intercom 3 |
| COM-06 | `reactivate_session_reminders` | W | Re-enable session reminders for a client that disabled them | ★★ Intercom explicit |
| COM-07 | `save_message_template` | W | Save a message as a reusable template | ★★ |
| COM-08 | `list_message_templates` | R | All saved message templates | ★★ |
| COM-09 | `get_sms_delivery_status` | R | Delivery status for a recent SMS send | ★★ Zoho 29 |
| COM-10 | `check_email_delivery` | R | Delivery log for a specific client or bulk send | ★★★ WhatsApp Anna |
| COM-11 | `setup_automation_sequence` | W | Configure triggered email chain for a programme: welcome → session reminder → payment due → trial follow-up | ★★★ Zoho 74 Intercom 3 |
| COM-12 | `preview_automation_email` | R | Preview what a specific triggered email looks like for a programme | ★★ |
| COM-13 | `get_communication_calendar` | R | Timeline of all emails/SMS scheduled to go out this week/month per programme | ★★★ new — visibility |
| COM-14 | `send_whatsapp_message` | W | Send via WhatsApp Business integration to a client or group | ★★★ WhatsApp KB FAQ |
| COM-15 | `get_communication_stats` | R | Open rates, click rates, delivery rates per recent send or template | ★★ |

---

## 11. Services & Products (Upsell)

Expanded. Includes upsell intelligence and bulk service offers.

| # | Tool | R/W | Description | Evidence |
|---|------|-----|-------------|----------|
| SRV-01 | `list_services` | R | All available add-on services / upsell products | ★★ |
| SRV-02 | `create_service` | W | Create a new service (e.g. uniform, exam fee, insurance, birthday party slot) | ★★ WhatsApp Kate/Anna |
| SRV-03 | `add_service_to_booking` | W | Add a service purchase to a client's booking | ★★ |
| SRV-04 | `get_service_orders` | R | All orders for a specific service | ★★ |
| SRV-05 | `create_product` | W | Create a physical product (size variants, price) | ★★ WhatsApp Kate ballet shoes |
| SRV-06 | `get_product_inventory` | R | Stock levels per product/variant | ★★ |
| SRV-07 | `report_product_sales` | R | Which services/products sold, by programme and location | ★★ new |
| SRV-08 | `bulk_offer_service` | W | Offer a service to all clients in a class/programme via email (e.g. end-of-year showcase tickets) | ★★★ new 💰 |
| SRV-09 | `get_upsell_opportunities` | R | Clients enrolled in programme A who are not in programme B that fits their profile | ★★★ new 💰 |
| SRV-10 | `apply_loyalty_discount` | W | Apply loyalty reward (points/discount) to a booking or service purchase | ★★ |

---

## 12. Business Reports & Intelligence

Significantly expanded. Moves from operational reports (what happened) to intelligence (what should I do next).

### Operational Reports

| # | Tool | R/W | Description | Evidence |
|---|------|-----|-------------|----------|
| REP-01 | `report_unpaid_clients` | R | All clients with outstanding balance: amount, days overdue, last contact | ★★★ Zoho 208 |
| REP-02 | `report_trial_pipeline` | R | Trials in last N days: attended / not attended / converted / lost | ★★★ 💰 |
| REP-03 | `report_non_renewals` | R | Clients from last term not registered in the new term | ★★★ 💰 |
| REP-04 | `report_empty_groups` | R | Classes with zero or very low enrolment — candidates for consolidation or removal | ★★★ |
| REP-05 | `report_missing_revenue` | R | Capacity utilisation gap: max revenue vs actual — per programme / location | ★★★ 💰 |
| REP-06 | `report_revenue_by_location` | R | Revenue breakdown per location for a period | ★★★ |
| REP-07 | `report_revenue_by_instructor` | R | Revenue associated per instructor (for commission, performance, programme value) | ★★★ |
| REP-08 | `report_capacity_overview` | R | All groups: occupancy %, free spots, waitlist | ★★★ |
| REP-09 | `report_makeup_by_location` | R | Make-up credits: issued / used / expired per location | ★★★ Intercom P1 |
| REP-10 | `report_attendance_by_class` | R | Attendance rate per class and per client for a period | ★★★ Zoho 80 |
| REP-11 | `report_financial_summary` | R | Revenue, invoiced, collected, outstanding for a period | ★★★ |
| REP-12 | `report_gocardless_health` | R | All GoCardless mandates: active / expiring / failed | ★★★ |
| REP-13 | `report_unmatched_payments` | R | Payments without a matching booking (see PAY-01) | ★★★ Zoho 68 |
| REP-14 | `report_auto_enrolment_status` | R | Confirmed / pending / declined per programme (see P-17) | ★★★ |
| REP-15 | `report_consents_missing` | R | Clients who have not signed required consents | ★★ |

### Intelligence Reports

| # | Tool | R/W | Description | Evidence |
|---|------|-----|-------------|----------|
| REP-16 | `report_at_risk_clients` | R | Clients showing churn signals: attendance dropping 3+ weeks + payment late + no communication response | ★★★ new — proactive 💰 |
| REP-17 | `report_client_ltv` | R | Lifetime value per client: total paid, number of terms, average term value, programmes they've been in | ★★★ new 💰 |
| REP-18 | `report_revenue_forecast` | R | Expected revenue for next 30/60/90 days based on active bookings, payment plans, and historical payment rates | ★★★ new 💰 |
| REP-19 | `report_top_performing_classes` | R | Classes ranked by: revenue, retention rate, attendance rate, referrals — find your winners | ★★★ new |
| REP-20 | `report_instructor_comparison` | R | Side-by-side instructor performance: client retention, avg attendance, no-shows, hours, revenue per session | ★★★ new — high demand |
| REP-21 | `report_seasonal_trends` | R | 12-month rolling: revenue, enrolments, attendance by month — identify seasonality, growth | ★★★ new |
| REP-22 | `report_franchise_overview` | R | All locations in one view: revenue, occupancy, retention, outstanding — for franchise owners | ★★★ Dom explicit need |
| REP-23 | `report_registration_lifecycle` | R | Funnel: enquiry → trial → active → lapsed → churned — with numbers and conversion rates per programme | ★★★ new 💰 |
| REP-24 | `report_churn_signals` | R | Clients where: last payment was late AND attendance dropped AND no reply to last email — all three together | ★★★ new — preventive |
| REP-25 | `report_upsell_opportunities` | R | Clients in programme A, not in programme B, within matching age/location profile | ★★★ new 💰 |

---

## 13. Settings & Configuration

| # | Tool | R/W | Description | Evidence |
|---|------|-----|-------------|----------|
| SET-01 | `get_account_settings` | R | Overview of all account-level settings | ★★ |
| SET-02 | `set_cancellation_policy` | W | Configure client self-cancellation limits (how many days before) | ★★★ |
| SET-03 | `set_auto_invoice_generation` | W | Turn on/off automatic invoice creation per payment | ★★ WhatsApp Anna |
| SET-04 | `set_custom_holidays` | W | Define custom non-session dates for a location or programme | ★★ WhatsApp Dom |
| SET-05 | `set_makeup_account_credit` | W | Configure whether make-up credit goes to account or booking | ★★ |
| SET-06 | `set_user_role` | W | Assign/change role for an admin or instructor | ★★★ Intercom |
| SET-07 | `list_payment_templates` | R | All configured payment templates with programmes they're assigned to | ★★★ |
| SET-08 | `set_waiting_list_policy` | W | Configure auto-promotion rules when spot opens | ★★ |
| SET-09 | `get_stripe_status` | R | Stripe connection health, account type, balance | ★★★ WhatsApp Kate/Anna/Dom |
| SET-10 | `set_registration_form` | W | Configure fields, remove registration fee, set consent text | ★★ Intercom |

---

## 14. Loyalty & Rewards

Zooza has a built-in loyalty module. Currently underused by operators — not visible without knowing it exists.

| # | Tool | R/W | Description | Evidence |
|---|------|-----|-------------|----------|
| LOY-01 | `get_client_loyalty_status` | R | Points balance, current tier, available rewards for a client | ★★★ KB: loyalty-faq |
| LOY-02 | `report_loyalty_overview` | R | All clients with loyalty status: points, tier, last activity | ★★ |
| LOY-03 | `award_loyalty_points` | W | Manually add points to a client (e.g. referral reward, long-term retention bonus) | ★★ |
| LOY-04 | `configure_loyalty_programme` | W | Set earning rules (points per booking, per referral), tier thresholds, reward types | ★★ |

---

## 15. Integrations & Health Checks

All external integrations in one place. Proactive health monitoring prevents silent failures.

| # | Tool | R/W | Description | Evidence |
|---|------|-----|-------------|----------|
| INT-01 | `check_stripe_health` | R | Connection status, last successful payment, balance, Express vs Standard account type, any failed charges | ★★★ WhatsApp Kate/Anna/Dom |
| INT-02 | `check_gocardless_health` | R | Mandate statuses, connection expiry date, any mandates expiring in next 30 days, reconnect URL | ★★★ Intercom P1 — 90-day silent expiry |
| INT-03 | `check_xero_sync` | R | Last sync date, invoices not synced, mismatches between Zooza and Xero | ★★★ WhatsApp Anna — Xero/Stripe mismatch |
| INT-04 | `get_power_bi_export` | R | Generate a data package (registrations, payments, attendance) formatted for Power BI | ★★ KB: power-bi-integration |
| INT-05 | `check_whatsapp_connection` | R | WhatsApp Business API connection status; last message sent; any delivery failures | ★★ KB: whatsapp-faq |

---

## 16. Skills — Compound Workflows

Skills combine multiple tools. The agent asks only what it needs, executes the sequence, returns an artifact.

### Setup & Launch

| # | Skill | Tools used | Trigger phrase | Time saved |
|---|-------|-----------|----------------|------------|
| SK-01 | **first_sale_setup** | OB-09 + P-03 + P-04 + P-11 + C-03 + OB-03 | *"I just set up my account, help me create my first programme and get a booking link for my website"* | 1–2 hours |
| SK-02 | **launch_ready** | OB-01 + OB-02 + OB-07 + INT-01 + INT-02 | *"Am I ready to go live? Check everything."* | 30–45 min |
| SK-03 | **onboard_new_programme** | P-07/08/04/12 + C-03 + PAY-07/08 + P-03 + OB-03 | *"Create Ballet Junior, set up payment, trial, first group, get me the booking link"* | 30–60 min |

### Term Management

| # | Skill | Tools used | Trigger phrase | Time saved |
|---|-------|-----------|----------------|------------|
| SK-04 | **prepare_new_term** | P-15 + C-10 + P-04/05/08/12 + COM-01 | *"Set up Summer 2026 from Winter 2025"* | 2–4 hours |
| SK-05 | **term_readiness_check** | OB-02 + SET-07 + P-17 + REP-14 | *"Is the new term fully configured and ready to accept bookings?"* | 20–30 min |
| SK-06 | **run_term_rebooking** | P-17 + B-06 + COM-01 | *"Copy confirmed registrations to the new term and send invitations"* | 1–2 hours |
| SK-07 | **end_of_term_cleanup** | REP-03 + C-11 + P-16 + COM-01 | *"Wrap up Winter 2025 — archive empty groups and chase non-renewals"* | 45–60 min |
| SK-08 | **setup_make_up_policy_bulk** | P-08 + C-12 | *"Enable make-up sessions on all programmes for Summer 2026"* | 20–30 min |

### Daily Operations

| # | Skill | Tools used | Trigger phrase | Time saved |
|---|-------|-----------|----------------|------------|
| SK-09 | **daily_briefing** | CAL-01 + REP-01 + MU-01 + INT-02 + REP-24 | *"Morning. What do I need to know today?"* | 15 min/day × every day |
| SK-10 | **cancel_day** | S-05 + MU-04 + COM-07 | *"Cancel all sessions tomorrow, instructor is sick, offer make-up"* | 15–30 min |
| SK-11 | **handle_instructor_absence** | CAL-08 + S-07 + MU-04 + COM-07 | *"Klára is sick today — find a substitute and notify parents"* | 20–30 min |
| SK-12 | **late_joiner_registration** | B-21 + B-03 + PAY-08 + COM-03 | *"Register Jana mid-term, calculate her pro-rata price, send payment link"* | 10–15 min |
| SK-13 | **setup_family_sibling_discount** | CL-10 + B-02 + B-19 | *"Apply the sibling discount to the Novák family — they have two kids"* | 10–15 min |
| SK-14 | **respond_to_absence_request** | B-01 + MU-02 + B-22 + B-05 | *"Jana says she can't attend for 3 weeks — what are her options?"* | 10–15 min |

### Revenue & Money

| # | Skill | Tools used | Trigger phrase | Time saved |
|---|-------|-----------|----------------|------------|
| SK-15 | **chase_unpaid** | REP-01 + COM-01/02 + PAY-13 | *"Send reminders to everyone who hasn't paid this term"* | 20–40 min |
| SK-16 | **monthly_financial_close** | REP-13 + PAY-01 + PAY-06 + REP-11 | *"Generate last month's invoices and show me what's unmatched"* | 30–45 min |
| SK-17 | **gocardless_health_check** | INT-02 + PAY-01 + PAY-04 | *"Check if my GoCardless is working and if there's anything unmatched"* | — proactive prevention |
| SK-18 | **handle_full_refund_event** | B-24 + PAY-10 + B-05/04 + COM-03 | *"The pool is closed for 3 weeks — refund or credit all affected clients"* | 1–3 hours |
| SK-19 | **calculate_instructor_payroll** | INS-09 + INS-10 + INS-12 | *"Calculate what I owe each instructor for May"* | 30–45 min |

### Growth & Intelligence

| # | Skill | Tools used | Trigger phrase | Time saved |
|---|-------|-----------|----------------|------------|
| SK-20 | **convert_trial_to_enrolment** | CL-13 + B-03 + PAY-08 + COM-03 | *"Find all unregistered trial clients and send them an enrolment offer"* | 30 min |
| SK-21 | **run_win_back_campaign** | REP-03 + CL-12 + COM-01 | *"Find everyone from last term who hasn't come back and send them a personal email"* | 30–45 min |
| SK-22 | **run_churn_prevention** | REP-24 + CL-14 + COM-01 | *"Find clients at risk of leaving and reach out personally"* | 20–30 min |
| SK-23 | **missing_revenue_sweep** | REP-02 + REP-03 + REP-04 + REP-05 + REP-25 | *"Show me where I'm leaving money on the table this term"* | — strategic |
| SK-24 | **upsell_campaign** | SRV-09 + SRV-08 + COM-01 | *"Find clients who might want to add Saturday Gymnastics and send them an offer"* | 30 min |
| SK-25 | **franchise_weekly_report** | REP-22 + REP-08 + REP-11 + REP-12 | *"Give me a weekly overview of all locations"* | 45–60 min |

---

## 17. Artifacts — Reusable Outputs

Artifacts are named, structured outputs. They can be scheduled, shared, or used as input to another skill.

### Setup & Readiness

| # | Artifact | Format | Generated by | Cadence |
|---|----------|--------|-------------|---------|
| ART-01 | **Pre-Launch Readiness Checklist** | Checklist | SK-02, OB-01 | On demand (new account) |
| ART-02 | **New Term Setup Checklist** | Checklist | SK-05, SK-04 | Per term |
| ART-03 | **Email Automation Map** | Structured list | COM-05 | On demand / setup |
| ART-04 | **Settings Consistency Report** | Table | OB-02, OB-07 | Pre-launch / after bulk change |

### Daily Operations

| # | Artifact | Format | Generated by | Cadence |
|---|----------|--------|-------------|---------|
| ART-05 | **Daily Briefing** | Summary + actions | SK-09 | Every morning |
| ART-06 | **Session Cancellation Summary** | Summary | SK-10 | After bulk cancellation |
| ART-07 | **Communication Calendar** | Timeline | COM-13 | Weekly |
| ART-08 | **Make-up Credits Report** | Table | MU-07 + MU-08 | Weekly |
| ART-09 | **Capacity Overview** | Table | REP-08 | Weekly / on demand |
| ART-10 | **Attendance Report** | Table | REP-10 | Per term |

### Revenue & Finance

| # | Artifact | Format | Generated by | Cadence |
|---|----------|--------|-------------|---------|
| ART-11 | **Unpaid Clients List** | Table | REP-01 | Weekly |
| ART-12 | **Unmatched Payments List** | Table | PAY-01 | Weekly |
| ART-13 | **Invoice Batch** | PDF / XML | PAY-06 | Monthly |
| ART-14 | **Financial Summary** | Summary | REP-11 | Monthly |
| ART-15 | **Revenue by Location** | Table | REP-06 | Monthly |
| ART-16 | **Revenue Forecast** | Projection table | REP-18 | Monthly |
| ART-17 | **Instructor Payroll Report** | Table | SK-19, INS-10 | Monthly |

### Growth & Intelligence

| # | Artifact | Format | Generated by | Cadence |
|---|----------|--------|-------------|---------|
| ART-18 | **Trial Pipeline Report** | Table | REP-02 | Weekly |
| ART-19 | **Auto-Enrolment Responses** | Table | REP-14, P-17 | Pre-rebooking |
| ART-20 | **Non-Renewals Report** | Table | REP-03 | End of term |
| ART-21 | **Missing Revenue Report** | Summary + table | REP-05 | Monthly |
| ART-22 | **Registration Funnel Report** | Funnel | REP-23 | Per term |
| ART-23 | **At-Risk Clients Report** | Table | REP-16, REP-24 | Weekly |
| ART-24 | **Seasonal Trends Report** | Chart data | REP-21 | Quarterly |

### Performance

| # | Artifact | Format | Generated by | Cadence |
|---|----------|--------|-------------|---------|
| ART-25 | **Instructor Performance Report** | Table | INS-13, INS-14, REP-20 | Per term |
| ART-26 | **Top Performing Classes Report** | Ranked table | REP-19 | Per term |
| ART-27 | **Franchise Location Overview** | Dashboard | SK-25, REP-22 | Weekly |
| ART-28 | **Client Profile Card** | Structured view | CL-01 + B-11 + MU-02 + CL-08 + CL-14 + CL-15 | On demand |
| ART-29 | **Client Lifetime Value Report** | Table | REP-17, CL-15 | Quarterly |
| ART-30 | **GoCardless Health Report** | Status card | INT-02, REP-12 | Monthly / alert |

---

## 18. Selection Guide: The Wow 30+30

Tools and skills that will **impress from first contact**. Selection criteria:
1. High evidence (real pain from Zoho/Intercom/WhatsApp)
2. Either: saves 30+ minutes of manual work per use, OR gives visibility that doesn't exist today
3. Covers the new client journey — not just existing operators

### New → First week wow tools

| Priority | Tool | Why it wows |
|----------|------|------------|
| ★ NEW | `OB-01 get_account_readiness_score` | First thing a new user needs — am I ready to accept bookings? |
| ★ NEW | `OB-03 get_widget_embed_code` | Copy-paste → website has a booking form in 2 minutes |
| ★ NEW | `OB-02 run_prelaunch_audit` | Catches inconsistent settings before clients see them |
| ★ NEW | `CL-16 create_manual_trial` | Walk-in client? Admin creates a trial immediately |
| ★ NEW | `INS-14 compare_instructors` | Which instructor has the best retention? Nobody can answer this today |

### Daily operations wow tools

| Priority | Tool | Why it wows |
|----------|------|------------|
| ★★★ | `MU-01 get_makeup_credits` | 227 Zoho tickets — still doesn't exist as a clean view |
| ★★★ | `PAY-13 send_payment_reminder` | 208 Zoho tickets — weekly manual work, auto-done |
| ★★★ | `S-05 bulk_cancel_sessions` | 52 Zoho — instructor sick → 1 command → all notified |
| ★★★ | `CAL-03 bulk_mark_attendance` | 80 Zoho — instructors on paper today |
| ★★★ | `B-05 transfer_booking` | 64 Zoho — parent wants Monday → Wednesday |
| ★★★ | `PAY-01 show_unmatched_payments` | 68 Zoho — money in the system nobody can see |
| ★★★ | `INT-02 check_gocardless_health` | Intercom P1 — 90-day silent expiry |
| ★★★ | `B-21 calculate_prorata` | Kate/Anna every time — repeated manual calculation |
| ★★★ | `CL-07 resend_client_access` | 54 Zoho — parent portal failures, daily |
| ★★★ | `PAY-10 initiate_refund` | Anna 100+ refunds in Stripe — now done inside Zooza |

### Growth & visibility wow tools

| Priority | Tool | Why it wows |
|----------|------|------------|
| ★★★ | `REP-18 report_revenue_forecast` | No operator knows what they'll collect next month |
| ★★★ | `REP-23 report_registration_lifecycle` | Full funnel: trial → active → lapsed → churned |
| ★★★ | `REP-16 report_at_risk_clients` | Proactive — catch churn before it happens |
| ★★★ | `INS-13 report_instructor_performance` | Attendance + retention + revenue per instructor — nobody has this |
| ★★★ | `REP-05 report_missing_revenue` | "You have €4,200 of empty spots this term" |
| ★★★ | `REP-03 report_non_renewals` | Who was here last term but isn't back yet |
| ★★★ | `MU-07 show_makeup_report_by_location` | Doesn't exist in Zooza today — Intercom P1 |
| ★★★ | `SRV-09 get_upsell_opportunities` | Find clients for Saturday Gymnastics from Ballet register |
| ★★★ | `P-17 get_auto_enrolment_responses` | Critical before every rebooking — currently no screen |
| ★★★ | `REP-22 report_franchise_overview` | Dom's entire business in one view |

### Wow Skills (top 10 of 25)

| # | Skill | One-line why |
|---|-------|-------------|
| SK-01 | **first_sale_setup** | New operator → booking link in 10 minutes |
| SK-09 | **daily_briefing** | Every morning: what needs attention today |
| SK-10 | **cancel_day** | Instructor sick → 1 message → everything handled |
| SK-04 | **prepare_new_term** | 2–4 hours → 5-minute conversation |
| SK-06 | **run_term_rebooking** | 134 clients copied + invited in one go |
| SK-20 | **convert_trial_to_enrolment** | Find unconverted trials → send offer → collect money |
| SK-21 | **run_win_back_campaign** | Lapsed clients → personalized email in minutes |
| SK-22 | **run_churn_prevention** | At-risk clients flagged + contacted before they leave |
| SK-23 | **missing_revenue_sweep** | Where are you leaving money? One answer |
| SK-19 | **calculate_instructor_payroll** | End of month → payroll table → done |

### Wow Artifacts (top 10 of 30)

| # | Artifact | Why operators will love it |
|---|----------|--------------------------|
| ART-05 | **Daily Briefing** | Every morning, no searching |
| ART-11 | **Unpaid Clients List** | Chase list ready, updated, actionable |
| ART-18 | **Trial Pipeline Report** | Who tried and hasn't enrolled yet = money waiting |
| ART-22 | **Registration Funnel Report** | Full lifecycle visibility per programme |
| ART-23 | **At-Risk Clients Report** | Churn prevention: fix before they leave |
| ART-16 | **Revenue Forecast** | Know what's coming in next month |
| ART-25 | **Instructor Performance Report** | Data for hard conversations and good decisions |
| ART-08 | **Make-up Credits Report** | Intercom P1 — finally exists |
| ART-30 | **GoCardless Health Report** | Never wake up to silent payment failure again |
| ART-29 | **Client Lifetime Value Report** | Who are your most valuable clients |

---

## Summary counts

| Category | v1 | v2 |
|----------|----|----|
| Onboarding tools | 0 | 9 |
| Programme tools | 17 | 17 |
| Class tools | 13 | 13 |
| Session tools | 10 | 10 |
| Client tools | 13 | 17 |
| Booking tools | 24 | 24 |
| Payment tools | 15 | 15 |
| Make-up tools | 8 | 8 |
| Calendar tools | 8 | 8 |
| Instructor tools | 7 | 15 |
| Communication tools | 10 | 15 |
| Services/products | 6 | 10 |
| Business reports | 15 | 25 |
| Settings | 10 | 10 |
| Loyalty | 0 | 4 |
| Integrations | 0 | 5 |
| **Total tools** | **~156** | **~205** |
| Skills | 15 | 25 |
| Artifacts | 20 | 30 |
| **Grand total** | **~191** | **~260** |

---

*Sources: Zoho 3,276 tickets · Intercom 170 conversations · WhatsApp Kate/Anna/Dom · Zooza KB (40+ articles) · core-workflows.md (15 workflows)*  
*New client journey mapped from: onboarding-launch-faq, getting-started-with-zooza, instructor-rate-reward, trials-faq, loyalty-faq*  
*Last updated: 2026-05-23*
