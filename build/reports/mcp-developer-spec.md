# Zooza MCP — Developer Specification

**Status:** Ready for implementation  
**Date:** 2026-05-22  
**Prepared by:** Product analysis (Zoho 3,276 tickets · Intercom 170 convos · WhatsApp Kate/Anna/Dom)

---

## Overview

This document defines the 30 MCP tools + 30 skills/artifacts for the Zooza MCP server.  
Each tool has been checked against the existing PHP API (`api-v1/`).

**Feasibility legend:**
- `✅ READY` — existing endpoint, implementable now
- `⚠️ PARTIAL` — endpoint exists, missing filter/bulk/field
- `❌ MISSING` — no endpoint, needs to be built

**Build order:** Ready tools first → Partial (small gaps) → Missing (new endpoints)

---

## API Feasibility Summary

| Ready | Partial | Missing |
|-------|---------|---------|
| 10 tools | 12 tools | 8 tools |

---

## TOP 30 TOOLS — Full Spec with Feasibility

---

### 🎯 PILLAR 1 — Make an offer

---

#### T01 · `get_programme_booking_link`
**Trigger:** *"Give me the registration link for Ballet Junior"*

| | |
|---|---|
| **Entity** | Programme |
| **Input** | `programme_id` (or name to fuzzy-match) |
| **Output** | `{ url: string, qr_code_url: string, embed_code: string }` |
| **API file** | `courses.php` |
| **Feasibility** | ❌ MISSING |
| **What's needed** | New GET endpoint: `GET /courses/{id}/booking_link` — return the public widget URL for a course |
| **Evidence** | Intercom ★★ "where is the registration form link" |

---

#### T02 · `list_unconverted_trials`
**Trigger:** *"Who came to a trial in the last 30 days and hasn't registered yet?"*

| | |
|---|---|
| **Entity** | Booking / Registration |
| **Input** | `days` (default 30) · `programme_id?` · `location_id?` |
| **Output** | `[{ client_name, email, phone, trial_date, programme, days_since_trial }]` |
| **API file** | `registrations.php` |
| **Feasibility** | ⚠️ PARTIAL |
| **What's needed** | Add filter: `status=trial_ended&no_active_registration=true` to GET /registrations (trial status tracking exists, cross-check missing) |
| **Evidence** | Intercom: 1 convo · WhatsApp: Kate, Anna · direct revenue |

---

#### T03 · `get_auto_enrolment_responses`
**Trigger:** *"Show me who confirmed continuation for Summer 2026"*

| | |
|---|---|
| **Entity** | Registration retention |
| **Input** | `course_id` · `status?` (confirmed / pending / declined) |
| **Output** | `[{ client_name, group, status, responded_at }]` |
| **API file** | `registration_retention_responses.php` |
| **Feasibility** | ✅ READY |
| **Endpoint** | `GET /registration_retention_responses?course_id={id}&status={status}` |
| **Evidence** | Intercom explicit gap (screen doesn't exist in UI today) |

---

#### T04 · `report_non_renewals`
**Trigger:** *"Who was in Winter 2025 but hasn't signed up for Summer 2026?"*

| | |
|---|---|
| **Entity** | Registration |
| **Input** | `source_course_id` · `target_course_id` |
| **Output** | `[{ client_name, email, phone, terms_active, last_class_date }]` |
| **API file** | `registrations.php`, `reports.php` |
| **Feasibility** | ⚠️ PARTIAL |
| **What's needed** | New report: `GET /reports/non_renewals?from_course={id}&to_course={id}` — compare active registrations across two courses |
| **Evidence** | WhatsApp: Anna, Kate, Dom every term |

---

#### T05 · `get_class_waiting_list`
**Trigger:** *"Who's on the waiting list for Monday Ballet?"*

| | |
|---|---|
| **Entity** | Class |
| **Input** | `schedule_id` (class/group ID) |
| **Output** | `[{ position, client_name, email, phone, child_age, days_waiting }]` |
| **API file** | `availability_requests.php` |
| **Feasibility** | ❌ MISSING |
| **What's needed** | `GET /availability_requests?schedule_id={id}` — ordered by created_at |
| **Evidence** | Zoho: 34 tickets (waitlist) · Kate, Anna |

---

#### T06 · `report_capacity_overview`
**Trigger:** *"Where do I have free spots? Where am I full?"*

| | |
|---|---|
| **Entity** | Class |
| **Input** | `programme_id?` · `location_id?` · `age_group?` |
| **Output** | `[{ class_name, capacity, enrolled, free_spots, waiting_list_count, occupancy_pct }]` sorted by occupancy |
| **API file** | `courses.php`, `reports.php` |
| **Feasibility** | ⚠️ PARTIAL |
| **What's needed** | New report: `GET /reports/capacity_overview` — aggregate schedules with registration counts and waiting list counts |
| **Evidence** | Kate (full Sunday class), Anna (many full classes) |

---

### 💰 PILLAR 2 — Collect money

---

#### T07 · `send_payment_reminder`
**Trigger:** *"Send a reminder to all unpaid clients in the Monday group"*

| | |
|---|---|
| **Entity** | Booking |
| **Input** | `filter: { schedule_id?, course_id?, status: "unpaid" }` · `message: string` · `channel: "email"\|"sms"` |
| **Output** | `{ sent_count: N, recipients: [{ name, email, amount_due }] }` |
| **API file** | `mass_emails.php` |
| **Feasibility** | ✅ READY |
| **Endpoint** | `POST /mass_emails` with recipient filter by payment status |
| **Evidence** | Zoho: Payments #1 (208 tickets) · Intercom ★★★ |

---

#### T08 · `set_payment_plan`
**Trigger:** *"Set a 4-instalment plan on Jana's registration"*

| | |
|---|---|
| **Entity** | Booking |
| **Input** | `order_id` · `template_id?` · `custom: { instalments, interval_days, first_due_date, amounts[]? }` |
| **Output** | `{ updated: true, plan_summary: [{ due_date, amount }] }` |
| **API file** | `payment_schedules_orders.php` |
| **Feasibility** | ✅ READY |
| **Endpoint** | `PUT /payment_schedules_orders/{id}` |
| **Evidence** | Zoho: 124 tickets · WhatsApp: Kate/Anna |

---

#### T09 · `bulk_change_payment_template`
**Trigger:** *"Switch all Monday group registrations to the Summer 2026 termly template"*

| | |
|---|---|
| **Entity** | Booking |
| **Input** | `filter: { schedule_id?, course_id? }` · `template_id` |
| **Output** | `{ updated_count: N, warnings: [{ order_id, issue }] }` |
| **API file** | `payment_schedules_templates.php`, `payment_schedules_orders.php` |
| **Feasibility** | ⚠️ PARTIAL |
| **What's needed** | `payment_schedules_templates.php` is currently empty — implement; add bulk endpoint `POST /payment_schedules_orders/bulk_update` with filter + template_id |
| **Evidence** | WhatsApp: Kate (days of work), Dom |

---

#### T10 · `show_unmatched_payments`
**Trigger:** *"Show me payments that came in but weren't matched to any booking"*

| | |
|---|---|
| **Entity** | Payment |
| **Input** | `from_date` · `to_date` · `method?: "gocardless"\|"bank"\|"stripe"` |
| **Output** | `[{ payment_id, amount, date, method, payer_name?, suggested_match? }]` |
| **API file** | `inbound_payments.php` |
| **Feasibility** | ✅ READY |
| **Endpoint** | `GET /inbound_payments?analytics=true&matched=false` |
| **Evidence** | Zoho: 68 tickets · WhatsApp: Kate, Anna, Dom |

---

#### T11 · `get_gocardless_status`
**Trigger:** *"Is my GoCardless connection working?"*

| | |
|---|---|
| **Entity** | Settings / Integration |
| **Input** | (none — account-level) |
| **Output** | `{ status: "active"\|"expired"\|"expiring_soon", expires_at: date, mandate_count: N, reconnect_url?: string }` |
| **API file** | `direct_debit_mandates.php` |
| **Feasibility** | ❌ MISSING |
| **What's needed** | `GET /direct_debit_mandates/health` — return connection status, expiry date, active mandate count, reconnect link if needed |
| **Evidence** | Intercom P1 · Zoho: 34 tickets · Kate, Dom |

---

#### T12 · `add_manual_payment`
**Trigger:** *"Jana paid by bank transfer — mark her as paid"*

| | |
|---|---|
| **Entity** | Payment |
| **Input** | `order_id` · `amount` · `date` · `method: "cash"\|"bank_transfer"\|"card"` · `generate_invoice?: bool` |
| **Output** | `{ payment_id, balance_after, invoice_id? }` |
| **API file** | `payments.php` |
| **Feasibility** | ✅ READY |
| **Endpoint** | `POST /payments` |
| **Evidence** | Zoho: Payments 208 · daily operation |

---

#### T13 · `generate_invoice_batch`
**Trigger:** *"Export all invoices from March for my accountant"*

| | |
|---|---|
| **Entity** | Invoice |
| **Input** | `from_date` · `to_date` · `format: "pdf"\|"xml"\|"csv"` · `course_id?` |
| **Output** | Download URL for batch file + `{ count: N, total_amount, period }` |
| **API file** | `customer_invoices.php`, `invoices.php` |
| **Feasibility** | ⚠️ PARTIAL |
| **What's needed** | Bulk download exists; needs `POST /invoices/batch_generate` to generate missing invoices for a period before download |
| **Evidence** | Zoho: 117 tickets · Anna (Xero), Dom (accountant blocked) |

---

#### T14 · `apply_session_credit_bulk`
**Trigger:** *"Cancel Thursday's session and credit everyone in that class"*

| | |
|---|---|
| **Entity** | Booking / Credit |
| **Input** | `schedule_id` · `session_date` · `amount?: number (default: 1 session price)` |
| **Output** | `{ credited_count: N, amount_per_client, total_credited }` |
| **API file** | `credits.php` |
| **Feasibility** | ⚠️ PARTIAL |
| **What's needed** | Individual credit creation exists; add `POST /credits/bulk` with `{ schedule_id, session_date, amount }` |
| **Evidence** | Zoho: 26 tickets · Dom (holidays), Anna (pool closure) |

---

#### T15 · `initiate_refund`
**Trigger:** *"Refund Jana — she cancelled and paid by card"*

| | |
|---|---|
| **Entity** | Payment |
| **Input** | `order_id` · `amount?: number (default: full)` · `reason?: string` |
| **Output** | `{ refund_id, amount, status, booking_status_after }` |
| **API file** | `payments.php` |
| **Feasibility** | ✅ READY |
| **Endpoint** | `POST /payments/{id}/refunds` — Stripe refund + booking status update |
| **Evidence** | WhatsApp: Anna (100+ refunds, all done in Stripe today) |

---

### ⚙️ PILLAR 3 — Daily business

---

#### T16 · `bulk_cancel_sessions`
**Trigger:** *"Cancel all sessions tomorrow, instructor is sick"*

| | |
|---|---|
| **Entity** | Session (Event) |
| **Input** | `date` · `trainer_id?` · `schedule_id?` · `notify_clients: bool` · `offer_makeup: bool` · `message?: string` |
| **Output** | `{ cancelled_count: N, notified_count: N, makeup_tokens_issued: N }` |
| **API file** | `events.php` |
| **Feasibility** | ⚠️ PARTIAL |
| **What's needed** | Individual cancellation exists; add `POST /events/bulk_cancel` with `{ date, trainer_id?, notify: bool, offer_makeup: bool }` |
| **Evidence** | Zoho: Calendar 52 · Intercom: 2 convos · Anna, Kate |

---

#### T17 · `transfer_booking`
**Trigger:** *"Move Jana from Monday to Wednesday, keep her payments"*

| | |
|---|---|
| **Entity** | Booking |
| **Input** | `order_id` · `target_schedule_id` · `carry_balance: bool` |
| **Output** | `{ new_order_id, payment_plan_preserved: bool, client_notified: bool }` |
| **API file** | `registrations.php`, `network_transfers.php` |
| **Feasibility** | ✅ READY |
| **Endpoint** | `POST /registrations/network_transfer` — supports bulk via params |
| **Evidence** | Zoho: 64 tickets · Intercom: 2 convos · Kate, Anna, Dom |

---

#### T18 · `duplicate_booking`
**Trigger:** *"Copy Jana's registration to the Summer 2026 group"*

| | |
|---|---|
| **Entity** | Booking |
| **Input** | `order_id` · `target_schedule_id` · `reset_payment: bool` |
| **Output** | `{ new_order_id, booking_link }` |
| **API file** | `registrations.php` |
| **Feasibility** | ✅ READY |
| **Endpoint** | `POST /registrations/{id}?action=copy` with target schedule |
| **Evidence** | Zoho: 43 tickets · Intercom: 2 convos · term rebooking |

---

#### T19 · `bulk_mark_attendance`
**Trigger:** *"Mark attendance for today's 10:00 Ballet session"*

| | |
|---|---|
| **Entity** | Session / Attendance |
| **Input** | `event_id` · `attendances: [{ order_id, status: "attended"\|"absent"\|"cancelled" }]` |
| **Output** | `{ saved_count: N, makeup_tokens_issued: N }` |
| **API file** | `attendance.php` |
| **Feasibility** | ❌ MISSING |
| **What's needed** | `PUT /attendance/bulk` with event_id and array of `{ order_id, status }` — individual note endpoint exists, bulk does not |
| **Evidence** | Zoho: 80 tickets · Anna, Kate (teachers marking on paper) |

---

#### T20 · `get_makeup_credits`
**Trigger:** *"Show all unused make-up credits in the Dubai Marina location"*

| | |
|---|---|
| **Entity** | Credit |
| **Input** | `location_id?` · `schedule_id?` · `client_id?` · `status: "active"\|"used"\|"expired"` |
| **Output** | `[{ client_name, credit_count, expiry_date, programme, location }]` |
| **API file** | `credits.php` |
| **Feasibility** | ✅ READY |
| **Endpoint** | `GET /credits?location_id={id}&status=active` |
| **Evidence** | Zoho: 227 tickets — #1 cluster · Anna, Kate |

---

#### T21 · `show_makeup_report_by_location`
**Trigger:** *"Give me a summary of make-up credits by location this term"*

| | |
|---|---|
| **Entity** | Credit |
| **Input** | `location_id?` · `from_date` · `to_date` |
| **Output** | `[{ location, issued, used, expired, active }]` grouped by location and programme |
| **API file** | `credits.php`, `reports.php` |
| **Feasibility** | ⚠️ PARTIAL |
| **What's needed** | `GET /reports/makeup_summary?group_by=location` — aggregate credits data (individual credits fetchable, summary endpoint missing) |
| **Evidence** | Intercom P1 — doesn't exist in UI today |

---

#### T22 · `resend_client_access`
**Trigger:** *"Jana can't log into the parent portal — resend her access"*

| | |
|---|---|
| **Entity** | Client |
| **Input** | `person_id` or `email` |
| **Output** | `{ sent: true, channel: "email"\|"sms", message: "Access link sent to jana@..." }` |
| **API file** | `users.php`, `persons.php` |
| **Feasibility** | ⚠️ PARTIAL |
| **What's needed** | Login code request endpoint exists; add `POST /persons/{id}/resend_access` that sends a fresh login link |
| **Evidence** | Zoho: 54 tickets · all 3 WhatsApp clients |

---

#### T23 · `calculate_prorata`
**Trigger:** *"Jana joins Monday Ballet from 12 May. There are 6 sessions left. What does she pay?"*

| | |
|---|---|
| **Entity** | Booking |
| **Input** | `schedule_id` · `join_date` · `full_price?: number` |
| **Output** | `{ prorata_amount, remaining_sessions, full_sessions, calculated_at }` — optionally: create booking with that amount |
| **API file** | `orders.php`, `billing_periods.php` |
| **Feasibility** | ❌ MISSING |
| **What's needed** | `POST /orders/calculate_prorata` with `{ schedule_id, join_date }` — return prorata amount + optionally create booking |
| **Evidence** | WhatsApp: Kate, Anna (repeated manual calculations) |

---

#### T24 · `bulk_update_programmes`
**Trigger:** *"Enable trial and auto-enrolment on all Summer 2026 programmes"*

| | |
|---|---|
| **Entity** | Programme |
| **Input** | `course_ids: []` or `filter: { term, location_id }` · `settings: { trial_enabled?, auto_enrolment?, visibility?, makeup_enabled?, down_payment? }` |
| **Output** | `{ updated_count: N, changes_summary }` |
| **API file** | `courses.php` |
| **Feasibility** | ⚠️ PARTIAL |
| **What's needed** | Single course update exists; add `PUT /courses/bulk` with `{ ids: [], settings: {} }` |
| **Evidence** | WhatsApp: Anna (asked Michal to set up all programmes at once) |

---

### 👁 PILLAR 4 — Visibility

---

#### T25 · `report_unpaid_clients`
**Trigger:** *"Show me everyone who hasn't paid this term"*

| | |
|---|---|
| **Entity** | Booking / Payment |
| **Input** | `course_id?` · `schedule_id?` · `min_days_overdue?: number` · `min_amount?: number` |
| **Output** | `[{ client_name, email, phone, class, amount_due, due_date, days_overdue }]` |
| **API file** | `reports.php` |
| **Feasibility** | ✅ READY |
| **Endpoint** | `GET /reports/outstanding_payments` with period filters |
| **Evidence** | Zoho: Payments 208 #1 · feeds T07 |

---

#### T26 · `report_missing_revenue`
**Trigger:** *"Where am I leaving money on the table?"*

| | |
|---|---|
| **Entity** | Programme / Class |
| **Input** | `course_id?` · `location_id?` · `term` |
| **Output** | `[{ class_name, capacity, enrolled, free_spots, price_per_client, potential_revenue, actual_revenue, gap }]` |
| **API file** | `reports.php` |
| **Feasibility** | ❌ MISSING |
| **What's needed** | `GET /reports/revenue_gap` — join schedules × capacity × price × active registrations |
| **Evidence** | Strategic report · capacity + pricing data available |

---

#### T27 · `report_revenue_by_location`
**Trigger:** *"How much did each location bring in this month?"*

| | |
|---|---|
| **Entity** | Payment |
| **Input** | `from_date` · `to_date` · `location_id?` |
| **Output** | `[{ location_name, collected, outstanding, invoiced, refunded }]` |
| **API file** | `reports.php` |
| **Feasibility** | ⚠️ PARTIAL |
| **What's needed** | `payments_summary` exists; add `group_by=location` parameter |
| **Evidence** | Dom (franchise master view) · management reporting |

---

#### T28 · `get_email_automation_overview`
**Trigger:** *"What emails does a client get after booking a trial in Ballet?"*

| | |
|---|---|
| **Entity** | Programme / Communication |
| **Input** | `course_id` · `trigger?: string` |
| **Output** | `[{ trigger_event, template_name, sends_after, channel, active }]` ordered by timeline |
| **API file** | `email_templates.php`, `settings_notifications.php` |
| **Feasibility** | ⚠️ PARTIAL |
| **What's needed** | Notification configs exist per course; add `GET /email_templates/automation_map?course_id={id}` that assembles the full trigger chain |
| **Evidence** | Zoho: 74 tickets · Intercom: 3 convos ★★★ |

---

#### T29 · `show_payment_mismatches`
**Trigger:** *"Show me bookings where the charged amount doesn't match what it should be"*

| | |
|---|---|
| **Entity** | Booking / Payment |
| **Input** | `course_id?` · `schedule_id?` |
| **Output** | `[{ client_name, order_id, expected_amount, actual_amount, difference, likely_cause }]` |
| **API file** | `payments.php`, `payment_schedules_orders.php` |
| **Feasibility** | ❌ MISSING |
| **What's needed** | `GET /reports/payment_mismatches` — compare expected (from template/aliquot) vs actual charged per order |
| **Evidence** | Zoho: 23 tickets · WhatsApp: Kate (aliquot errors) |

---

#### T30 · `find_duplicate_clients`
**Trigger:** *"Do I have any duplicate client records?"*

| | |
|---|---|
| **Entity** | Client |
| **Input** | `course_id?` · `match_by: "email"\|"name"\|"both"` |
| **Output** | `[{ person_ids: [], name, email, registration_count, created_dates }]` |
| **API file** | `persons.php` |
| **Feasibility** | ❌ MISSING |
| **What's needed** | `GET /persons/duplicates?match_by=email` — group persons by normalized email/name, return suspected duplicates |
| **Evidence** | WhatsApp: Anna (15+ duplicates) · Kate (test data) |

---

---

## TOP 30 SKILLS — Spec

Skills combine multiple tools. Executed as guided agent workflows.

| # | Skill | Trigger | Tools | Est. time saved |
|---|-------|---------|-------|----------------|
| SK01 | `cancel_day` | *"Cancel all sessions tomorrow, instructor sick"* | T16 + T20 + COM | 15–30 min |
| SK02 | `prepare_new_term` | *"Set up Summer 2026 from Winter 2025"* | T24 + T08 + T09 + T01 | 2–4 hours |
| SK03 | `run_term_rebooking` | *"Copy confirmed registrations to Summer 2026"* | T03 + T18 + T08 + COM | 1–2 hours |
| SK04 | `end_of_term_cleanup` | *"Wrap up Winter 2025 — archive empties, chase non-renewals"* | T04 + archive + COM | 45–60 min |
| SK05 | `chase_unpaid` | *"Send reminders to everyone who hasn't paid"* | T25 + T07 | 20–40 min |
| SK06 | `handle_instructor_absence` | *"Anna can't teach today — substitute and notify"* | CAL + T16 + COM | 20–30 min |
| SK07 | `convert_trial_to_enrolment` | *"Find unregistered trials and send them an offer"* | T02 + T01 + COM | 30 min |
| SK08 | `setup_sibling_discount` | *"Apply sibling discount to the Novák family"* | siblings + B-19 | 10–15 min |
| SK09 | `onboard_new_programme` | *"Create Ballet Junior with payment, trial, first group"* | T24 + T08 + C-03 + T01 | 30–60 min |
| SK10 | `monthly_financial_close` | *"Generate last month's invoices, show unmatched"* | T10 + T13 + REP | 30–45 min |
| SK11 | `setup_makeup_policy_bulk` | *"Enable make-up on all Summer 2026 programmes"* | T24 | 20–30 min |
| SK12 | `handle_refund_event` | *"Pool closed 3 weeks — credit or refund affected clients"* | T14 + T15 + COM | 1–3 hours |
| SK13 | `late_joiner_registration` | *"Register Jana mid-term with pro-rata price"* | T23 + T08 + T12 | 10–15 min |
| SK14 | `missing_revenue_sweep` | *"Show me where I'm leaving money on the table"* | T02 + T04 + T06 + T26 | — |
| SK15 | `gocardless_health_check` | *"Is my GoCardless working? Any unmatched?"* | T11 + T10 | — |

---

## TOP 15 ARTIFACTS — Spec

Artifacts are named, reusable outputs generated by tools or skills.

| # | Artifact | Generated by | Format | Pillar | Refresh |
|---|----------|-------------|--------|--------|---------|
| A01 | **Unpaid Clients List** | T25 | Table | 💰 | Weekly |
| A02 | **Trial Pipeline Report** | T02 | Table | 🎯 | Weekly |
| A03 | **Non-Renewals Report** | T04 | Table | 🎯 | End of term |
| A04 | **Auto-Enrolment Responses** | T03 | Table | ⚙️ | Pre-rebooking |
| A05 | **Capacity Overview** | T06 | Summary | 🎯 | On demand |
| A06 | **Missing Revenue Report** | T26 | Summary | 👁 | Monthly |
| A07 | **Make-up Credits Report** | T21 | Table | ⚙️ | Weekly |
| A08 | **Invoice Batch** | T13 | PDF/XML | 💰 | Monthly |
| A09 | **Financial Summary** | SK10 | Summary | 💰 | Monthly |
| A10 | **Revenue by Location** | T27 | Table | 👁 | Monthly |
| A11 | **GoCardless Health Card** | T11 | Status | 💰 | Monthly/alert |
| A12 | **Email Automation Map** | T28 | List | 👁 | On demand |
| A13 | **New Term Setup Checklist** | SK02 | Checklist | ⚙️ | Per term |
| A14 | **Session Cancellation Summary** | SK01 | Summary | ⚙️ | Per event |
| A15 | **Client Profile Card** | T20+T25+CL-01 | View | ⚙️ | On demand |

---

## Build roadmap

### Phase 1 — Ship with existing API (10 tools, 0 new endpoints)

All ✅ READY:

| Tool | Endpoint |
|------|----------|
| T03 | `GET /registration_retention_responses` |
| T07 | `POST /mass_emails` |
| T08 | `PUT /payment_schedules_orders/{id}` |
| T10 | `GET /inbound_payments?matched=false` |
| T12 | `POST /payments` |
| T15 | `POST /payments/{id}/refunds` |
| T17 | `POST /registrations/network_transfer` |
| T18 | `POST /registrations/{id}?action=copy` |
| T20 | `GET /credits?location_id={id}&status=active` |
| T25 | `GET /reports/outstanding_payments` |

---

### Phase 2 — Small API additions (12 tools, 12 endpoints to extend)

All ⚠️ PARTIAL — existing endpoint + 1 parameter or bulk mode:

| Tool | What to add |
|------|------------|
| T02 | Filter: `status=trial_ended&no_active_registration=true` on GET /registrations |
| T04 | New: `GET /reports/non_renewals?from_course&to_course` |
| T06 | New: `GET /reports/capacity_overview` |
| T09 | Implement `payment_schedules_templates.php` + `POST /payment_schedules_orders/bulk_update` |
| T13 | Add: `POST /invoices/batch_generate` |
| T14 | Add: `POST /credits/bulk` |
| T16 | Add: `POST /events/bulk_cancel` |
| T21 | Add: `GET /reports/makeup_summary?group_by=location` |
| T22 | Add: `POST /persons/{id}/resend_access` |
| T24 | Add: `PUT /courses/bulk` |
| T27 | Add: `group_by=location` param to existing payments_summary |
| T28 | Add: `GET /email_templates/automation_map?course_id` |

---

### Phase 3 — New endpoints (8 tools)

All ❌ MISSING — new endpoint required:

| Tool | New endpoint | Complexity |
|------|-------------|------------|
| T01 | `GET /courses/{id}/booking_link` | Low |
| T05 | `GET /availability_requests?schedule_id={id}` | Low |
| T11 | `GET /direct_debit_mandates/health` | Low |
| T19 | `PUT /attendance/bulk` | Low |
| T23 | `POST /orders/calculate_prorata` | Medium |
| T26 | `GET /reports/revenue_gap` | Medium |
| T29 | `GET /reports/payment_mismatches` | Medium |
| T30 | `GET /persons/duplicates` | Medium |

---

## Summary counts

| Category | Count |
|----------|-------|
| Tools | 30 |
| Skills | 15 |
| Artifacts | 15 |
| **Total** | **60** |
| API ready now | 10 tools |
| Needs small addition | 12 tools |
| Needs new endpoint | 8 tools |

---

*Sources: Zoho 3,276 tickets · Intercom 170 conversations · WhatsApp Kate/babyballet + Anna/Turtle Tots + Dom/Wee Kicks*  
*API checked against: `api-v1/` PHP codebase*  
*Last updated: 2026-05-22*
