# Zooza MCP — Full Tool / Skill / Artifact Catalog

**Purpose:** Complete inventory to select from. Every tool follows one entity.  
**Method:** Entity-first. Every entity gets full CRUD + its business-specific operations.  
**Format:** `R` = read/query · `W` = write/action · ★★★ high evidence · ★★ medium · ★ low  
**Date:** 2026-05-22

---

## Contents

1. [Programmes](#1-programmes)
2. [Classes (Groups)](#2-classes-groups)
3. [Sessions](#3-sessions)
4. [Clients](#4-clients)
5. [Bookings / Registrations](#5-bookings--registrations)
6. [Payments & Billing](#6-payments--billing)
7. [Make-up / Replacement Credits](#7-make-up--replacement-credits)
8. [Calendar & Attendance](#8-calendar--attendance)
9. [Instructors](#9-instructors)
10. [Communication & Notifications](#10-communication--notifications)
11. [Services & Products (Upsell)](#11-services--products-upsell)
12. [Business Reports](#12-business-reports)
13. [Settings & Configuration](#13-settings--configuration)
14. [Skills — Compound Workflows](#14-skills--compound-workflows)
15. [Artifacts — Reusable Outputs](#15-artifacts--reusable-outputs)
16. [Top 30 Tools](#top-30-tools)
17. [Top 30 Skills + Artifacts](#top-30-skills--artifacts)

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
| B-22 | `pause_booking` | W | Temporarily suspend a booking to next term (no native feature today) | ★★ WhatsApp Dom/Anna |
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

| # | Tool | R/W | Description | Evidence |
|---|------|-----|-------------|----------|
| INS-01 | `list_instructors` | R | All instructors with classes, schedule, role | ★★★ |
| INS-02 | `get_instructor` | R | Profile, assigned classes, upcoming sessions | ★★ |
| INS-03 | `create_instructor` | W | Add new instructor; set name, email, role, send invite | ★★★ Zoho Lecturers 30 |
| INS-04 | `update_instructor` | W | Update details, role permissions | ★★ |
| INS-05 | `assign_instructor_to_class` | W | Assign an instructor to a class (all future sessions) | ★★★ |
| INS-06 | `set_session_instructor` | W | Override instructor for a specific session only | ★★★ |
| INS-07 | `get_instructor_schedule` | R | Full schedule for a period with session counts | ★★ |

---

## 10. Communication & Notifications

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

---

## 11. Services & Products (Upsell)

| # | Tool | R/W | Description | Evidence |
|---|------|-----|-------------|----------|
| SRV-01 | `list_services` | R | All available add-on services / upsell products | ★★ |
| SRV-02 | `create_service` | W | Create a new service (e.g. uniform, exam fee, insurance) | ★★ WhatsApp Kate/Anna |
| SRV-03 | `add_service_to_booking` | W | Add a service purchase to a client's booking | ★★ |
| SRV-04 | `get_service_orders` | R | All orders for a specific service | ★★ |
| SRV-05 | `create_product` | W | Create a physical product (size variants, price) | ★★ WhatsApp Kate (ballet shoes) |
| SRV-06 | `get_product_inventory` | R | Stock levels per product/variant | ★★ |

---

## 12. Business Reports

Visibility queries that answer "what is happening in my business right now."

| # | Tool | R/W | Description | Evidence |
|---|------|-----|-------------|----------|
| REP-01 | `report_unpaid_clients` | R | All clients with outstanding balance: amount, days overdue, last contact | ★★★ Zoho 208 |
| REP-02 | `report_trial_pipeline` | R | Trials in last N days: attended / not attended / converted / lost | ★★★ 💰 |
| REP-03 | `report_non_renewals` | R | Clients from last term not registered in the new term | ★★★ 💰 |
| REP-04 | `report_empty_groups` | R | Classes with zero or very low enrolment — candidates for consolidation or removal | ★★★ |
| REP-05 | `report_missing_revenue` | R | Capacity utilisation gap: max revenue vs actual — per programme / location | ★★★ 💰 |
| REP-06 | `report_revenue_by_location` | R | Revenue breakdown per location for a period | ★★★ |
| REP-07 | `report_revenue_by_instructor` | R | Revenue per instructor (for commission, performance) | ★★ |
| REP-08 | `report_capacity_overview` | R | All groups: occupancy %, free spots, waitlist | ★★★ |
| REP-09 | `report_makeup_by_location` | R | Make-up credits: issued / used / expired per location | ★★★ Intercom P1 |
| REP-10 | `report_attendance_by_class` | R | Attendance rate per class and per client for a period | ★★★ Zoho 80 |
| REP-11 | `report_financial_summary` | R | Revenue, invoiced, collected, outstanding for a period | ★★★ |
| REP-12 | `report_gocardless_health` | R | All GoCardless mandates: active / expiring / failed | ★★★ |
| REP-13 | `report_unmatched_payments` | R | Payments without a matching booking (see PAY-01) | ★★★ Zoho 68 |
| REP-14 | `report_auto_enrolment_status` | R | Confirmed / pending / declined per programme (see P-17) | ★★★ |
| REP-15 | `report_consents_missing` | R | Clients who have not signed required consents | ★★ |

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
| SET-09 | `get_stripe_status` | R | Stripe connection health, account type (Standard vs Express), balance | ★★★ WhatsApp Kate/Anna/Dom |
| SET-10 | `set_registration_form` | W | Configure fields, remove registration fee, set consent text | ★★ Intercom |

---

## 14. Skills — Compound Workflows

Skills combine multiple tools into a single guided operation. The agent asks only for what it needs, then executes the sequence.

| # | Skill | Tools used | Trigger phrase | Time saved |
|---|-------|-----------|----------------|------------|
| SK-01 | **cancel_day** | S-05 + MU-04 + COM-07 | *"Cancel all sessions tomorrow, instructor is sick, offer make-up"* | 15–30 min |
| SK-02 | **prepare_new_term** | P-15 + C-10 + P-04/05/08/12 + COM-01 | *"Set up Summer 2026 from Winter 2025"* | 2–4 hours |
| SK-03 | **run_term_rebooking** | P-17 + B-06 + COM-01 | *"Copy confirmed registrations to the new term and send invitations"* | 1–2 hours |
| SK-04 | **end_of_term_cleanup** | REP-03 + C-11 + P-16 + COM-01 | *"Wrap up Winter 2025 — archive empty groups and chase non-renewals"* | 45–60 min |
| SK-05 | **chase_unpaid** | REP-01 + COM-01/02 + PAY-13 | *"Send reminders to everyone who hasn't paid this term"* | 20–40 min |
| SK-06 | **handle_instructor_absence** | CAL-08 + S-07 + MU-04 + COM-07 | *"Klára is sick today — find a substitute and notify parents"* | 20–30 min |
| SK-07 | **convert_trial_to_enrolment** | CL-13 + B-03 + PAY-08 + COM-03 | *"Find all unregistered trial clients and send them an enrolment offer"* | 30 min |
| SK-08 | **setup_family_sibling_discount** | CL-10 + B-02 + B-19 | *"Apply the sibling discount to the Novák family — they have two kids"* | 10–15 min |
| SK-09 | **onboard_new_programme** | P-01(check) + P-07/08/04/12 + C-03 + PAY-07/08 + P-03 | *"Create Ballet Junior, set up payment, trial, first group, get me the booking link"* | 30–60 min |
| SK-10 | **monthly_financial_close** | REP-13 + PAY-01 + PAY-06 + REP-11 | *"Generate last month's invoices and show me what's unmatched"* | 30–45 min |
| SK-11 | **setup_make_up_policy_bulk** | P-08 + C-12 | *"Enable make-up sessions on all programmes for Summer 2026"* | 20–30 min |
| SK-12 | **handle_full_refund_event** | B-24 + PAY-10 + B-05/B-04 + COM-03 | *"The pool is closed for 3 weeks — refund or credit all affected clients"* | 1–3 hours |
| SK-13 | **late_joiner_registration** | B-21 + B-03 + PAY-08 + COM-03 | *"Register Jana mid-term, calculate her pro-rata price, send payment link"* | 10–15 min |
| SK-14 | **missing_revenue_sweep** | REP-02 + REP-03 + REP-04 + REP-05 | *"Show me where I'm leaving money on the table this term"* | — |
| SK-15 | **gocardless_health_check** | PAY-03 + PAY-01 + PAY-04 | *"Check if my GoCardless is working and if there's anything unmatched"* | — |

---

## 15. Artifacts — Reusable Outputs

Artifacts are structured outputs the agent can generate, save, and re-use. They are not one-off query results — they are named, versioned documents that can be scheduled, shared, or triggered automatically.

| # | Artifact | Format | Generated by | Use case |
|---|----------|--------|-------------|----------|
| ART-01 | **Unpaid Clients List** | Table (CSV / inline) | REP-01 | Weekly debt chase; share with finance |
| ART-02 | **Trial Pipeline Report** | Table | REP-02 | Weekly sales review |
| ART-03 | **Non-Renewals Report** | Table | REP-03 | End-of-term win-back campaign |
| ART-04 | **Empty Groups Report** | Table | REP-04 | Group consolidation decision |
| ART-05 | **Missing Revenue Report** | Summary + table | REP-05 | Pricing and capacity decisions |
| ART-06 | **Revenue by Location** | Table / chart data | REP-06 | Monthly management report |
| ART-07 | **Revenue by Instructor** | Table | REP-07 | Commission calculation |
| ART-08 | **Capacity Overview** | Table | REP-08 | Sales decisions, waiting list management |
| ART-09 | **Make-up Credits Report** | Table | MU-07 + MU-08 | Operational tracking by location |
| ART-10 | **Invoice Batch** | PDF / XML / CSV | PAY-06 | Accountant handover (monthly) |
| ART-11 | **Attendance Report** | Table | REP-10 | Client engagement, instructor performance |
| ART-12 | **Auto-Enrolment Responses** | Table | REP-14 | Pre-rebooking decision list |
| ART-13 | **Email Automation Map** | Structured list | COM-05 | Onboarding check, debugging |
| ART-14 | **Session Cancellation Summary** | Summary | SK-01 | After bulk cancellation — proof/audit |
| ART-15 | **New Term Setup Checklist** | Checklist | SK-02 | Confirm all settings before going live |
| ART-16 | **GoCardless Health Report** | Status card | REP-12 | Monthly check; trigger alert |
| ART-17 | **Financial Summary** | Summary | REP-11 | Management report; investor update |
| ART-18 | **Consent Audit** | Table | REP-15 | GDPR compliance check |
| ART-19 | **Message Template Library** | List | COM-08 | Reuse across communication actions |
| ART-20 | **Client Profile Card** | Structured view | CL-01 + B-11 + MU-02 + CL-08 | Support conversation context |

---

## Top 30 Tools

Selected by: evidence strength × frequency × manual effort eliminated.

| Rank | ID | Tool | Why top 30 |
|------|----|------|------------|
| 1 | MU-01 | `get_makeup_credits` | 227 Zoho tickets — #1 dataset; daily visibility gap |
| 2 | PAY-13 / COM-04 | `send_payment_reminder` | Payments = #1 Zoho category (208); weekly action |
| 3 | B-08 | `set_payment_plan` | 124 Zoho; every new registration with instalments |
| 4 | PAY-06 | `generate_invoice_batch` | 117 Zoho; monthly accountant handover |
| 5 | B-02 | `list_bookings` | Foundation for almost all other tools |
| 6 | COM-05 | `get_email_automation_overview` | 74 Zoho + 3 Intercom; navigation nightmare today |
| 7 | B-05 | `transfer_booking` | 64 Zoho + 2 Intercom; weekly; payment reset bug |
| 8 | CL-07 | `resend_client_access` | 54 Zoho; daily parent portal failures |
| 9 | PAY-01 | `show_unmatched_payments` | 68 Zoho; money in system admin can't see |
| 10 | PAY-03 | `get_gocardless_status` | Intercom P1; 90-day silent expiry |
| 11 | S-05 | `bulk_cancel_sessions` | Zoho 52; weekly; 15–30 min manual today |
| 12 | P-17 | `get_auto_enrolment_responses` | Intercom explicit gap; critical before term rebooking |
| 13 | B-06 | `duplicate_booking` | 43 Zoho; term rebooking foundation |
| 14 | CAL-03 | `bulk_mark_attendance` | Zoho 80; daily; mobile UX broken today |
| 15 | REP-01 | `report_unpaid_clients` | Core financial visibility; feeds payment reminder |
| 16 | REP-02 | `report_trial_pipeline` | Direct revenue signal; unconverted = lost £ |
| 17 | REP-03 | `report_non_renewals` | Term end; win-back; direct revenue |
| 18 | MU-07 | `show_makeup_report_by_location` | Doesn't exist in Zooza today; Intercom P1 |
| 19 | P-14 | `bulk_update_programmes` | 1 command instead of 30 manual changes |
| 20 | C-12 | `bulk_update_classes` | Same — capacity, instructor, visibility at scale |
| 21 | PAY-09 | `bulk_change_payment_template` | Kate: days of manual work; per-term |
| 22 | B-21 | `calculate_prorata` | WhatsApp Kate/Anna repeatedly; no native flow |
| 23 | B-10 | `add_manual_payment` | Zoho 208; daily cash/bank transfer recording |
| 24 | PAY-10 | `initiate_refund` | Anna 100+ refunds; currently Stripe only |
| 25 | B-19 | `apply_sibling_discount` | Zoho 28; no automation today |
| 26 | CL-05 | `find_duplicate_clients` | Anna 15+; no detection today |
| 27 | COM-03 | `resend_confirmation_email` | Zoho 12 + bulk failure; weekly |
| 28 | REP-05 | `report_missing_revenue` | Capacity × price gap = direct £ signal |
| 29 | C-09 | `get_class_waiting_list` | Zoho 34; visibility before promoting |
| 30 | PAY-11 | `apply_session_credit_bulk` | Zoho 26; cancelled class → credit for whole group |

---

## Top 30 Skills + Artifacts

| Rank | Type | ID | Name | Why |
|------|------|----|------|-----|
| 1 | Skill | SK-02 | **prepare_new_term** | 2–4 hours saved; highest per-use impact |
| 2 | Skill | SK-01 | **cancel_day** | Weekly; 15–30 min; most visible to clients |
| 3 | Skill | SK-05 | **chase_unpaid** | Direct revenue recovery; weekly |
| 4 | Artifact | ART-01 | **Unpaid Clients List** | Foundation for SK-05; weekly use |
| 5 | Skill | SK-03 | **run_term_rebooking** | 1–2 hours saved per term; critical path |
| 6 | Artifact | ART-12 | **Auto-Enrolment Responses** | Must-have before SK-03 |
| 7 | Skill | SK-07 | **convert_trial_to_enrolment** | Direct revenue; pipeline management |
| 8 | Artifact | ART-02 | **Trial Pipeline Report** | Input for SK-07; weekly |
| 9 | Skill | SK-04 | **end_of_term_cleanup** | Combines archiving + win-back |
| 10 | Artifact | ART-03 | **Non-Renewals Report** | Input for end-of-term and win-back |
| 11 | Skill | SK-15 | **gocardless_health_check** | P1 silent failure prevention |
| 12 | Artifact | ART-16 | **GoCardless Health Report** | Monthly proactive check |
| 13 | Skill | SK-10 | **monthly_financial_close** | Accountant handover; monthly |
| 14 | Artifact | ART-10 | **Invoice Batch** | Output of SK-10; monthly |
| 15 | Artifact | ART-17 | **Financial Summary** | Management report; monthly |
| 16 | Skill | SK-13 | **late_joiner_registration** | Pro-rata + booking in one flow |
| 17 | Artifact | ART-09 | **Make-up Credits Report** | Intercom P1 gap; weekly operations |
| 18 | Skill | SK-11 | **setup_make_up_policy_bulk** | Per-term; saves 20–30 min setup |
| 19 | Artifact | ART-08 | **Capacity Overview** | Sales decisions; where to sell more |
| 20 | Artifact | ART-05 | **Missing Revenue Report** | Strategic; capacity × price gap |
| 21 | Skill | SK-09 | **onboard_new_programme** | End-to-end setup in one flow |
| 22 | Artifact | ART-15 | **New Term Setup Checklist** | Output of SK-02; audit trail |
| 23 | Skill | SK-06 | **handle_instructor_absence** | Weekly; substitution + client notification |
| 24 | Artifact | ART-11 | **Attendance Report** | Client engagement; instructor performance |
| 25 | Skill | SK-08 | **setup_family_sibling_discount** | Removes manual per-family work |
| 26 | Artifact | ART-13 | **Email Automation Map** | Visibility; debugging; onboarding |
| 27 | Skill | SK-12 | **handle_full_refund_event** | Crisis scenario; pool/venue closure |
| 28 | Artifact | ART-04 | **Empty Groups Report** | Operational; consolidation decision |
| 29 | Skill | SK-14 | **missing_revenue_sweep** | Strategic; trial + non-renewals + capacity |
| 30 | Artifact | ART-20 | **Client Profile Card** | Support context; booking + payment + credits |

---

*Total catalog: ~120 tools · 15 skills · 20 artifacts*  
*Top selection: 30 tools + 30 skills/artifacts*  
*All tools trace to a real entity in the Zooza data model*  
*Last updated: 2026-05-22*
