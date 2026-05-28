# Zooza MCP Server — Complete Product Specification

**Version:** 1.0  
**Date:** 2026-05-23  
**Status:** Ready for implementation review  
**Prepared by:** Product (bottom-up from Zoho 3,276 tickets · Intercom ~170 conversations · WhatsApp Kate/Anna/Dom)

---

## 1. What This Is

The Zooza MCP (Model Context Protocol) server exposes Zooza's business data and operations to AI agents. An operator connects their AI assistant (Claude, ChatGPT, or any MCP-compatible agent) to Zooza and can then manage their entire class-based business through natural language conversation.

**The agent can:**
- Query business data and generate reports
- Take actions (cancel sessions, send reminders, process payments)
- Chain multiple operations into guided workflows
- Produce named, reusable artifacts (reports, checklists, summaries)

**Who uses it:**
- Owners and admins of class-based activity businesses (dance schools, swim schools, gymnastics clubs, etc.)
- Franchise managers overseeing multiple locations
- Operators migrating from another system who need to run from day one

**What it is not:** A replacement for the Zooza UI. It is an additional interface layer for operators who prefer conversation over clicking, and for AI-native workflows that are impossible in a traditional UI (e.g. cross-entity intelligence reports, automated chaining of 5+ steps in one response).

---

## 2. Why We Built This: Evidence from Customer Data

### Why bottom-up, not top-down

The initial tool list for this spec was drafted by the product team based on operator suggestions. It was discarded. A bottom-up analysis of all three customer data sources produced a fundamentally different priority order — with make-up credits (227 Zoho tickets) as the absolute #1 pain point, which was entirely absent from the operator-suggested list.

**Rule:** every tool in this spec traces to a documented customer pain point. If it doesn't, it doesn't belong here.

### Zoho Tickets — 3,276 cases, 2024–2025

| Category | Tickets | Primary pain |
|----------|--------:|-------------|
| Make-up / replacement sessions | 227 | No clean visibility of credit balance per location |
| Payments | 208 | Recording manual payments, reminders, unmatched, payment plan setup |
| Courses / Programmes | 199 | Setup confusion, term copy, booking link location |
| Clients | 142 | Portal access failures, transfers, duplicates |
| Settings | 137 | Payment templates, automation config |
| Communication | 73 | Automated email setup, bulk email, delivery failures |
| Calendar / Sessions | 52 | Session cancellation, attendance recording |
| Lecturers | 30 | Adding instructors, role assignment |

> **Note:** ~2,400 of the 3,276 tickets have no category assigned (pre-categorisation tickets). The numbers above are conservative — actual volume per category is likely 3–5× higher.

### Intercom — ~170 conversations, Feb–Apr 2026

**P1 critical gaps** (issues that generate the most repeat contacts):
- **GoCardless silent expiry every 90 days** — operators discover failure only when payments stop. No warning, no proactive notification in Zooza.
- **Make-up credits: no location filter** — operators managing multiple venues cannot see credits per location. Doesn't exist in the UI today.
- **Auto-enrolment responses: no dedicated screen** — confirmed/pending/declined responses exist in the API but no admin view.
- **"Where are my automated email settings?"** — ★★★ most-repeated Intercom question. The setting exists but is not findable.
- **Programme archiving confusion** — top reason for opening Intercom (#1 category in processed clusters).

### WhatsApp — Kate (babyballet Dubai), Anna (Turtle Tots), Dom (Wee Kicks)

Three real operators, 4,600+ messages, Dec 2025 – May 2026.

| Operator | Primary pain clusters |
|----------|-----------------------|
| **Kate** | Bulk operations (setting up 20+ classes manually), pro-rata calculations, bulk payment template changes, billing period management |
| **Anna** | Refunds (100+ via Stripe, outside Zooza), transfer requests, duplicate client records (15+), Xero/Stripe reconciliation |
| **Dom** | Franchise-level visibility, GoCardless mandate cancellations (silent), unmatched bank payments, end-of-term multi-location cleanup |

---

## 3. Architecture Decisions

### 3.1 — Single MCP server, not multiple

**Decision:** One `zooza-mcp` server, permission scoping via API token.

**Reasoning:** The most valuable parts of this spec are compound Skills — workflows that chain tools from multiple entity domains (sessions + credits + communication, or bookings + payments + reports). If tools live in separate servers, cross-domain skills require the agent to manage multiple server connections. This adds implementation complexity, latency, and failure surface.

**Permission model:** Different token scopes control access level:
- `admin` token: full read + write access
- `instructor` token: attendance write + own schedule read
- `read-only` token: reports and queries only (for franchisors, accountants)

### 3.2 — Two-tier architecture: Foundation + Operations

**Foundation tier (F-tier):** Tools that create the structural entities Zooza needs before any operational tool works. These are run once (or rarely) and follow a guided sequence.

**Operational tier (O-tier):** The 30 Wow Tools. These operate on the structure the F-tier created.

An operator who has never set up Zooza runs the Foundation tier first. An existing operator goes straight to the operational tier.

### 3.3 — Default setup: ask only when no default exists

When creating structural entities, Zooza has sensible defaults for most settings. The agent should:
1. Use defaults silently for non-critical settings
2. Ask only for the minimum required inputs (name, price, schedule, instructor)
3. State what defaults were applied and offer to change them after creation

Example: `create_programme` asks for name + price + type. Everything else (trial: off, auto-enrolment: off, aliquot: off, visibility: public) uses defaults. The agent says: *"Created Ballet Junior. Trial sessions are off by default — want to enable them?"*

This prevents the 30-questions onboarding experience that causes drop-off.

### 3.4 — Payment gateway: agent guides, operator clicks

Stripe and GoCardless both require OAuth browser redirect. An AI agent cannot complete OAuth autonomously — it requires the operator to click a link and authenticate in their browser.

**MCP flow:**
1. `setup_stripe` → returns Stripe Connect onboarding URL
2. Operator opens URL in browser, completes OAuth
3. `verify_payment_setup` → confirms connection is active and returns status

The agent explicitly tells the operator: *"Open this link, connect your Stripe account, then come back and I'll verify everything is working."*

GoCardless follows the same pattern. The agent should also proactively check connection status (every 90 days it expires silently) via `check_gocardless_health`.

### 3.5 — Tool vs Skill vs Artifact

**Tool:** One atomic operation. One API call. One responsibility. Can be used standalone or as a step in a Skill.

**Skill:** A compound workflow. The agent sequences multiple tools, makes decisions based on intermediate results, asks clarifying questions only when needed, and produces a final summary. The operator triggers a Skill with a single natural-language phrase.

**Artifact:** A named, structured output. Can be generated on demand, scheduled, or produced as a by-product of a Skill. Can be shared, downloaded, or used as input to another Skill.

---

## 4. The Client Journey This Covers

```
Day 1           Week 1          Month 1–3        Per term         Ongoing
   │               │                │                │                │
Foundation     First sale       Daily ops       Term cycle       Intelligence
F01–F09        T01–T09          T10–T25          SK05–SK07        T26–T30
SK01–SK02      SK09             SK03–SK04        SK08–SK14        SK14–SK15
A01            A04, A06         A02–A03          A08–A09, A11     A13–A15
```

---

## 5. Foundation Prerequisites (F-tier)

These must exist before any operational tool works. The `first_sale_setup` Skill (SK01) walks a new operator through the entire F-tier in one guided conversation.

| # | Tool | Creates | Required inputs | Default applied |
|---|------|---------|----------------|-----------------|
| F01 | `create_location` | Venue/studio | Name, address | — |
| F02 | `create_instructor` | Staff member | Name, email, role | Role: instructor |
| F03 | `create_programme` | Programme (course) | Name, type, price | Trial: off · Auto-enrol: off · Public: on |
| F04 | `create_class` | Recurring group | Day, time, instructor, capacity | Location: first available |
| F05 | `create_payment_template` | Billing model | Type (termly/monthly/instalment), amount, due dates | — |
| F06 | `set_billing_period` | Term dates | Start date, end date, session count | Holidays: none |
| F07 | `setup_stripe` | Payment connection | — (returns OAuth URL, operator completes in browser) | — |
| F08 | `setup_gocardless` | Direct debit connection | — (returns OAuth URL, operator completes in browser) | — |
| F09 | `verify_payment_setup` | — (health check) | — | — |

**Products and services** are not in the F-tier. They are feature prerequisites only for upsell tools — an operator can run a fully functioning business without creating a single product or service. The agent will prompt for them contextually when the operator tries to use an upsell tool.

**Sessions** are not in the F-tier. They are auto-generated from the class schedule when F04 (`create_class`) runs.

**API status of F-tier:**
- F01–F04, F06: ✅ READY (courses.php, schedules.php, places.php, billing_periods.php all have POST)
- F05: ❌ MISSING — `payment_schedules_templates.php` exists but is empty; implementation required
- F07–F08: ⚠️ PARTIAL — OAuth callback flow exists; needs a dedicated initiation endpoint returning the URL
- F09: ✅ READY — can use existing Stripe/GoCardless status endpoints

---

## 6. The 30 Wow Tools

Organised by the client journey stage where each tool first becomes relevant.

---

### 🚀 New client — first 7 days

---

#### T01 · `get_account_readiness_score`
**Trigger:** *"Am I ready to accept my first booking?"*

| | |
|---|---|
| **Inputs** | none |
| **Output** | `{ score: 0–100, ready: bool, blocking: [items], suggestions: [items] }` — structured checklist |
| **API file** | new: `account.php` or `onboard.php` |
| **Feasibility** | ❌ MISSING — `GET /account/readiness` |
| **Evidence** | Onboarding FAQ ★★★ — "What should I check before going live?" is the #1 pre-launch question |
| **Why it wows** | First thing a new operator needs. Not a settings page — a verdict. Green means go. |

---

#### T02 · `run_prelaunch_audit`
**Trigger:** *"Check my settings before I go live"*

| | |
|---|---|
| **Inputs** | `programme_id?` (if omitted: all programmes) |
| **Output** | `[{ class_name, issue_type, current_value, expected_value }]` — every inconsistency found |
| **API file** | new: `GET /courses/{id}/audit` |
| **Feasibility** | ❌ MISSING |
| **Evidence** | Onboarding FAQ ★★★ · Kate and Anna both had inconsistent class settings post-launch |
| **Why it wows** | Catches the "Monday class has card payment, Tuesday class doesn't" problem before 40 parents see it |

---

#### T03 · `get_widget_embed_code`
**Trigger:** *"Give me the code to put the booking form on my website"*

| | |
|---|---|
| **Inputs** | `programme_id?` · `class_id?` (omit for full booking page) |
| **Output** | `{ iframe_html: string, direct_url: string, qr_code_url: string }` |
| **API file** | widgets.php / courses.php |
| **Feasibility** | ⚠️ PARTIAL — widget exists; need `GET /courses/{id}/widget_config` returning the embed snippet |
| **Evidence** | Intercom ★★ — "where do I get the code for my website?" |
| **Why it wows** | Copy-paste → website has a live booking form in 2 minutes |

---

#### T04 · `get_programme_booking_link`
**Trigger:** *"Give me the registration link for Ballet Junior"*

| | |
|---|---|
| **Inputs** | `programme_id` (or name to fuzzy-match) |
| **Output** | `{ url: string, qr_code_url: string }` |
| **API file** | courses.php |
| **Feasibility** | ❌ MISSING — `GET /courses/{id}/booking_link` |
| **Evidence** | Intercom ★★ — "where is the registration link?" is weekly |
| **Why it wows** | The link is buried 3 levels deep in the UI. This makes it immediate. |

---

#### T05 · `create_manual_trial`
**Trigger:** *"A parent just called, add them for a trial on Thursday"*

| | |
|---|---|
| **Inputs** | `client_id` (or create inline) · `class_id` · `session_date` |
| **Output** | `{ booking_id, confirmation_sent: bool }` |
| **API file** | registrations.php |
| **Feasibility** | ⚠️ PARTIAL — registration POST exists; trial status handling needs explicit support for admin-created trials |
| **Evidence** | W02 documented gap ★★★ — "Trial bookings cannot be created manually by an admin" (from KB) |
| **Why it wows** | Walk-ins, phone calls, WhatsApp enquiries — all converted to a real booking in one step |

---

### 🎯 Make an offer

---

#### T06 · `report_trial_pipeline`
**Trigger:** *"Who came to a trial in the last 30 days but hasn't enrolled?"*

| | |
|---|---|
| **Inputs** | `days` (default 30) · `programme_id?` |
| **Output** | `[{ client_name, email, phone, trial_date, programme, days_since_trial, status }]` |
| **API file** | registrations.php, reports.php |
| **Feasibility** | ⚠️ PARTIAL — trial status exists; cross-check "no active enrolment" needs new filter |
| **Evidence** | Intercom 1 convo · WhatsApp Kate/Anna — direct revenue signal |
| **Why it wows** | Every unconverted trial = money on the table. This makes the list visible and actionable. |

---

#### T07 · `report_non_renewals`
**Trigger:** *"Who was in Winter 2025 but hasn't signed up for Summer 2026?"*

| | |
|---|---|
| **Inputs** | `source_programme_id` · `target_programme_id` |
| **Output** | `[{ client_name, email, phone, terms_active, last_class_date }]` |
| **API file** | reports.php |
| **Feasibility** | ❌ MISSING — `GET /reports/non_renewals?from_course={id}&to_course={id}` |
| **Evidence** | WhatsApp: Anna, Kate, Dom — every end of term without exception |
| **Why it wows** | Win-back is cheaper than acquisition. This makes the list instantly available. |

---

#### T08 · `get_class_waiting_list`
**Trigger:** *"Who's on the waiting list for Monday Ballet?"*

| | |
|---|---|
| **Inputs** | `schedule_id` |
| **Output** | `[{ position, client_name, email, phone, child_age, days_waiting }]` |
| **API file** | availability_requests.php |
| **Feasibility** | ❌ MISSING — `GET /availability_requests?schedule_id={id}` ordered by created_at |
| **Evidence** | Zoho: 34 tickets · Kate/Anna — always asked before opening a new group |
| **Why it wows** | Shows exactly how much demand exists to justify opening a new class |

---

#### T09 · `get_upsell_opportunities`
**Trigger:** *"Which of my Ballet parents could I offer Saturday Gymnastics to?"*

| | |
|---|---|
| **Inputs** | `source_programme_id` · `target_programme_id` · `age_range?` · `location_id?` |
| **Output** | `[{ client_name, email, phone, child_age, enrolled_in, not_enrolled_in }]` |
| **API file** | reports.php (new) |
| **Feasibility** | ❌ MISSING — `GET /reports/upsell_opportunities` |
| **Evidence** | WhatsApp: Kate (multiple programmes, same clients) · direct revenue |
| **Why it wows** | Cross-sell list in 5 seconds. Something a traditional UI will never do. |

---

### 💰 Collect money

---

#### T10 · `send_payment_reminder`
**Trigger:** *"Send a reminder to all unpaid clients in the Monday group"*

| | |
|---|---|
| **Inputs** | `filter: { schedule_id?, programme_id?, overdue_days? }` · `message?: string` · `channel: email\|sms` |
| **Output** | `{ sent_count: N, recipients: [{ name, email, amount_due }] }` |
| **API file** | mass_emails.php |
| **Feasibility** | ✅ READY — `POST /mass_emails` with payment status filter |
| **Evidence** | Zoho Payments #1 (208 tickets) · Intercom ★★★ — weekly pain for every operator |

---

#### T11 · `set_payment_plan`
**Trigger:** *"Set a 3-instalment plan on Jana's registration"*

| | |
|---|---|
| **Inputs** | `order_id` · `template_id?` · `custom: { instalments, interval_days, first_due_date }` |
| **Output** | `{ updated: true, plan_summary: [{ due_date, amount }] }` |
| **API file** | payment_schedules_orders.php |
| **Feasibility** | ✅ READY — `PUT /payment_schedules_orders/{id}` |
| **Evidence** | Zoho: 124 tickets · WhatsApp: Kate/Anna |

---

#### T12 · `add_manual_payment`
**Trigger:** *"Jana paid by bank transfer — mark her as paid"*

| | |
|---|---|
| **Inputs** | `order_id` · `amount` · `date` · `method: cash\|bank_transfer\|card` · `generate_invoice?: bool` |
| **Output** | `{ payment_id, balance_after, invoice_id? }` |
| **API file** | payments.php |
| **Feasibility** | ✅ READY — `POST /payments` |
| **Evidence** | Zoho Payments #1 (208) · daily operation for every operator |

---

#### T13 · `show_unmatched_payments`
**Trigger:** *"Show me payments that came in but weren't matched to any booking"*

| | |
|---|---|
| **Inputs** | `from_date` · `to_date` · `method?: gocardless\|bank\|stripe` |
| **Output** | `[{ payment_id, amount, date, method, payer_name?, suggested_match? }]` |
| **API file** | inbound_payments.php |
| **Feasibility** | ✅ READY — `GET /inbound_payments?matched=false` |
| **Evidence** | Zoho: 68 tickets · WhatsApp: Kate, Anna, Dom — "money in the system nobody can see" |

---

#### T14 · `initiate_refund`
**Trigger:** *"Refund Jana — she cancelled and paid by card"*

| | |
|---|---|
| **Inputs** | `order_id` · `amount?: number (default: full)` · `reason?: string` |
| **Output** | `{ refund_id, amount, status, booking_status_after }` |
| **API file** | payments.php |
| **Feasibility** | ✅ READY — `POST /payments/{id}/refunds` |
| **Evidence** | WhatsApp: Anna — 100+ refunds all done manually in Stripe, outside Zooza |

---

#### T15 · `check_gocardless_health`
**Trigger:** *"Is my GoCardless working?"*

| | |
|---|---|
| **Inputs** | none (account-level) |
| **Output** | `{ status: active\|expired\|expiring_soon, expires_at, mandate_count, reconnect_url? }` |
| **API file** | direct_debit_mandates.php |
| **Feasibility** | ❌ MISSING — `GET /direct_debit_mandates/health` |
| **Evidence** | Intercom P1 — 8 conversations = highest repeat rate · Zoho: 34 tickets · Kate, Dom — silent 90-day expiry |
| **Why it wows** | The single highest-cost silent failure in Zooza. Proactive check prevents revenue loss. |

---

#### T16 · `generate_invoice_batch`
**Trigger:** *"Export all invoices from March for my accountant"*

| | |
|---|---|
| **Inputs** | `from_date` · `to_date` · `format: pdf\|xml\|csv` · `programme_id?` |
| **Output** | Download URL + `{ count: N, total_amount, period }` |
| **API file** | customer_invoices.php, invoices.php |
| **Feasibility** | ⚠️ PARTIAL — bulk download exists; needs `POST /invoices/batch_generate` to pre-generate missing invoices |
| **Evidence** | Zoho: 117 tickets · Anna (Xero blocked) · Dom (accountant blocked 2 weeks) |

---

### ⚙️ Daily operations

---

#### T17 · `bulk_cancel_sessions`
**Trigger:** *"Cancel all sessions tomorrow, instructor is sick"*

| | |
|---|---|
| **Inputs** | `date` · `instructor_id?` · `schedule_id?` · `notify: bool` · `offer_makeup: bool` · `message?: string` |
| **Output** | `{ cancelled_count: N, notified_count: N, makeup_tokens_issued: N }` |
| **API file** | events.php |
| **Feasibility** | ⚠️ PARTIAL — individual cancel exists; needs `POST /events/bulk_cancel` |
| **Evidence** | Zoho Calendar: 52 tickets · WhatsApp: Anna, Kate — 15–30 min manual today |

---

#### T18 · `bulk_mark_attendance`
**Trigger:** *"Mark attendance for today's 10:00 Ballet session"*

| | |
|---|---|
| **Inputs** | `event_id` · `attendances: [{ order_id, status: attended\|absent\|cancelled }]` |
| **Output** | `{ saved_count: N, makeup_tokens_issued: N }` |
| **API file** | attendance.php |
| **Feasibility** | ❌ MISSING — `PUT /attendance/bulk` (individual note endpoint exists, bulk does not) |
| **Evidence** | Zoho: 80 tickets · Anna, Kate — teachers marking on paper today |

---

#### T19 · `transfer_booking`
**Trigger:** *"Move Jana from Monday to Wednesday, keep her payments"*

| | |
|---|---|
| **Inputs** | `order_id` · `target_schedule_id` · `carry_balance: bool` |
| **Output** | `{ new_order_id, payment_plan_preserved: bool, client_notified: bool }` |
| **API file** | network_transfers.php |
| **Feasibility** | ✅ READY — `POST /registrations/network_transfer` |
| **Evidence** | Zoho: 64 tickets · Intercom: 2 convos · Kate, Anna, Dom |

---

#### T20 · `duplicate_booking`
**Trigger:** *"Copy Jana's registration to the Summer 2026 group"*

| | |
|---|---|
| **Inputs** | `order_id` · `target_schedule_id` · `reset_payment: bool` |
| **Output** | `{ new_order_id, booking_link }` |
| **API file** | registrations.php |
| **Feasibility** | ✅ READY — `POST /registrations/{id}?action=copy` |
| **Evidence** | Zoho: 43 tickets · Intercom: 2 convos |

---

#### T21 · `get_makeup_credits`
**Trigger:** *"Show all unused make-up credits in Dubai Marina"*

| | |
|---|---|
| **Inputs** | `location_id?` · `schedule_id?` · `client_id?` · `status: active\|used\|expired` |
| **Output** | `[{ client_name, credit_count, expiry_date, programme, location }]` |
| **API file** | credits.php |
| **Feasibility** | ✅ READY — `GET /credits?status=active&location_id={id}` |
| **Evidence** | Zoho: 227 tickets — absolute #1 cluster · Anna, Kate — daily visibility gap |

---

#### T22 · `resend_client_access`
**Trigger:** *"Jana can't log into the parent portal — resend her access"*

| | |
|---|---|
| **Inputs** | `person_id` or `email` |
| **Output** | `{ sent: true, channel: email\|sms }` |
| **API file** | persons.php |
| **Feasibility** | ⚠️ PARTIAL — login code exists; needs `POST /persons/{id}/resend_access` |
| **Evidence** | Zoho: 54 tickets · all three WhatsApp clients |

---

#### T23 · `calculate_prorata`
**Trigger:** *"Jana joins Monday Ballet from 12 May. There are 6 sessions left. What does she pay?"*

| | |
|---|---|
| **Inputs** | `schedule_id` · `join_date` · `full_price?: number` |
| **Output** | `{ prorata_amount, remaining_sessions, full_sessions, calculated_at }` |
| **API file** | orders.php, billing_periods.php |
| **Feasibility** | ❌ MISSING — `POST /orders/calculate_prorata` |
| **Evidence** | WhatsApp: Kate, Anna — repeated manual calculation every single time a late joiner appears |

---

#### T24 · `get_auto_enrolment_responses`
**Trigger:** *"Show me who confirmed continuation for Summer 2026"*

| | |
|---|---|
| **Inputs** | `programme_id` · `status?: confirmed\|pending\|declined` |
| **Output** | `[{ client_name, group, status, responded_at }]` |
| **API file** | registration_retention_responses.php |
| **Feasibility** | ✅ READY — `GET /registration_retention_responses?course_id={id}&status={status}` |
| **Evidence** | Intercom: explicit gap — "this screen doesn't exist in the UI today" |

---

#### T25 · `apply_sibling_discount`
**Trigger:** *"Apply the sibling discount to the Novák family — they have two kids"*

| | |
|---|---|
| **Inputs** | `parent_person_id` · `discount_type: percentage\|fixed` · `discount_value` |
| **Output** | `{ updated_bookings: N, discount_applied: [{ child_name, booking_id, discount }] }` |
| **API file** | coupons.php, orders.php |
| **Feasibility** | ⚠️ PARTIAL — coupon system exists; family linking + bulk application needs dedicated flow |
| **Evidence** | Zoho: 28 tickets · WhatsApp: Anna (manual per-family codes) |

---

### 👁 Business intelligence

---

#### T26 · `report_revenue_forecast`
**Trigger:** *"What will I collect next month?"*

| | |
|---|---|
| **Inputs** | `months: 1\|2\|3` (default 1) · `programme_id?` · `location_id?` |
| **Output** | `{ expected_revenue, active_bookings, payment_plans_due: [{ month, amount }], confidence: low\|medium\|high }` |
| **API file** | reports.php (new) |
| **Feasibility** | ❌ MISSING — `GET /reports/revenue_forecast` |
| **Evidence** | No operator in our dataset knows their expected next-month revenue. Pure intelligence gap. |
| **Why it wows** | First time an operator can answer "what's coming in" without a spreadsheet |

---

#### T27 · `report_at_risk_clients`
**Trigger:** *"Who is likely to leave soon?"*

| | |
|---|---|
| **Inputs** | `programme_id?` · `location_id?` · `threshold?: { attendance_drop_weeks: 3, payment_days_late: 14 }` |
| **Output** | `[{ client_name, email, risk_score, signals: [dropping_attendance, late_payment, no_comms_reply] }]` |
| **API file** | reports.php (new) |
| **Feasibility** | ❌ MISSING — `GET /reports/at_risk_clients` |
| **Evidence** | Preventive — no current tooling. Churn costs 5× more than retention. |
| **Why it wows** | Moves operator from reactive (client left) to proactive (client is leaving) |

---

#### T28 · `report_instructor_performance`
**Trigger:** *"Which instructor has the best client retention?"*

| | |
|---|---|
| **Inputs** | `term?` · `location_id?` |
| **Output** | `[{ instructor_name, avg_attendance_rate, client_retention_rate, no_show_rate, sessions_taught, revenue_associated }]` sorted by retention |
| **API file** | trainer_rates.php, reports.php (new aggregation) |
| **Feasibility** | ⚠️ PARTIAL — individual instructor reports exist (KB: instructor-rate-reward); cross-instructor performance comparison endpoint missing |
| **Evidence** | No operator in our data can answer "which instructor is best" with data today |
| **Why it wows** | Hard conversations become data-driven. Good decisions on class assignments. |

---

#### T29 · `report_missing_revenue`
**Trigger:** *"Where am I leaving money on the table?"*

| | |
|---|---|
| **Inputs** | `programme_id?` · `location_id?` · `term` |
| **Output** | `[{ class_name, capacity, enrolled, free_spots, price_per_session, potential_revenue, actual_revenue, gap }]` |
| **API file** | reports.php (new) |
| **Feasibility** | ❌ MISSING — `GET /reports/revenue_gap` |
| **Evidence** | Strategic report · data all available, aggregation missing |
| **Why it wows** | "You have €4,200 of empty spots this term" is a sentence that pays for the MCP server |

---

#### T30 · `report_registration_lifecycle`
**Trigger:** *"Show me the full funnel — from trial to churned"*

| | |
|---|---|
| **Inputs** | `programme_id?` · `from_date` · `to_date` |
| **Output** | `{ enquiry: N, trial_booked: N, trial_attended: N, enrolled: N, active: N, lapsed: N, churned: N, conversion_rate: % }` |
| **API file** | reports.php (new) |
| **Feasibility** | ❌ MISSING — `GET /reports/registration_lifecycle` |
| **Evidence** | No operator has this view today. Required for intelligent business decisions. |
| **Why it wows** | Funnel view changes how operators think about their business. Not just "how many registered" but "where are they falling off" |

---

## 7. The 15 Skills

| #    | Skill                          | Trigger                                               | Tools chained                        | Time saved   |
| ---- | ------------------------------ | ----------------------------------------------------- | ------------------------------------ | ------------ |
| SK01 | **first_sale_setup**           | *"Help me set up my first programme and get it live"* | F01–F09 + T03 + T04                  | 1–2 hours    |
| SK02 | **launch_ready**               | *"Am I ready to go live? Check everything."*          | T01 + T02 + T03 + T15                | 30–45 min    |
| SK03 | **daily_briefing**             | *"What do I need to know today?"*                     | Calendar + T13 + T21 + T15 + T27     | 15 min/day   |
| SK04 | **cancel_day**                 | *"Cancel all sessions tomorrow, instructor is sick"*  | T17 + T21 + COM                      | 15–30 min    |
| SK05 | **prepare_new_term**           | *"Set up Summer 2026 from Winter 2025"*               | copy_programme + T24 + bulk_settings | 2–4 hours    |
| SK06 | **run_term_rebooking**         | *"Copy confirmed registrations to Summer 2026"*       | T24 + T20 + COM                      | 1–2 hours    |
| SK07 | **end_of_term_cleanup**        | *"Wrap up Winter 2025"*                               | T07 + archive + COM                  | 45–60 min    |
| SK08 | **chase_unpaid**               | *"Send reminders to everyone who hasn't paid"*        | REP-01 + T10                         | 20–40 min    |
| SK09 | **convert_trial_to_enrolment** | *"Find unregistered trials and send them an offer"*   | T06 + T04 + COM                      | 30 min       |
| SK10 | **run_win_back_campaign**      | *"Find everyone from last term who hasn't come back"* | T07 + COM                            | 30–45 min    |
| SK11 | **run_churn_prevention**       | *"Find clients at risk of leaving and reach out"*     | T27 + COM                            | 20–30 min    |
| SK12 | **late_joiner_registration**   | *"Register Jana mid-term with pro-rata price"*        | T23 + create_booking + T11 + COM     | 10–15 min    |
| SK13 | **monthly_financial_close**    | *"Generate last month's invoices and reconcile"*      | T13 + T16 + REP-11                   | 30–45 min    |
| SK14 | **missing_revenue_sweep**      | *"Where am I leaving money on the table?"*            | T06 + T07 + T08 + T29 + T09          | — strategic  |
| SK15 | **gocardless_health_check**    | *"Is my GoCardless working?"*                         | T15 + T13 + PAY-04                   | — preventive |

---

## 8. The 15 Artifacts

| # | Artifact | Cadence | Generated by | Why operators will use it |
|---|----------|---------|-------------|--------------------------|
| A01 | **Pre-Launch Readiness Checklist** | Once (new operator) | SK02, T01 | Confidence before going live. Every gap is named and actionable. |
| A02 | **Daily Briefing** | Every morning | SK03 | Today's sessions + alerts + unpaid + at-risk. Zero searching. |
| A03 | **Unpaid Clients List** | Weekly | REP-01 | Input for payment reminder. Who owes what, how long overdue. |
| A04 | **Trial Pipeline Report** | Weekly | T06 | Who tried and hasn't enrolled. Revenue waiting to be collected. |
| A05 | **Make-up Credits Report** | Weekly | T21 + MU-07 | By location and programme. Intercom P1 — doesn't exist in Zooza today. |
| A06 | **Capacity Overview** | Weekly | REP-08 | Free spots × price = open revenue. Where to push sales. |
| A07 | **At-Risk Clients Report** | Weekly | T27 | Churn signals before they become cancellations. |
| A08 | **Auto-Enrolment Responses** | Pre-rebooking | T24 | Confirmed/pending/declined. The decision list before SK06. |
| A09 | **New Term Setup Checklist** | Per term | SK05 | Formal confirmation that all settings are correct before launch. |
| A10 | **Session Cancellation Summary** | Ad-hoc | SK04 | After bulk cancel: who was notified, how many credits issued. Audit trail. |
| A11 | **Invoice Batch** | Monthly | T16 | PDF/XML/CSV for accountant. Monthly deliverable. |
| A12 | **Financial Summary** | Monthly | SK13 | Revenue · collected · outstanding · refunds. Management report. |
| A13 | **Revenue Forecast** | Monthly | T26 | Expected income for next 30/60/90 days. No operator has this today. |
| A14 | **Instructor Performance Report** | Per term | T28 | Retention + attendance + revenue per instructor. Data for hard decisions. |
| A15 | **Registration Funnel Report** | Per term | T30 | Trial → active → lapsed → churned. Business health at a glance. |

---

## 9. Build Roadmap

### Phase 0 — Foundation tier (before anything else)

| Tool | API status | What's needed |
|------|-----------|--------------|
| F01–F04, F06 | ✅ READY | No changes needed |
| F05 `create_payment_template` | ❌ | Implement `payment_schedules_templates.php` (file exists, is empty) |
| F07–F08 payment OAuth | ⚠️ | Add `POST /payment_integrations/stripe/setup` and `/gocardless/setup` returning OAuth URL |
| F09 `verify_payment_setup` | ✅ READY | Compose from existing status endpoints |

---

### Phase 1 — Operational tools ready now (0 new endpoints)

| Tool | Endpoint |
|------|----------|
| T10 `send_payment_reminder` | `POST /mass_emails` |
| T11 `set_payment_plan` | `PUT /payment_schedules_orders/{id}` |
| T12 `add_manual_payment` | `POST /payments` |
| T13 `show_unmatched_payments` | `GET /inbound_payments?matched=false` |
| T14 `initiate_refund` | `POST /payments/{id}/refunds` |
| T19 `transfer_booking` | `POST /registrations/network_transfer` |
| T20 `duplicate_booking` | `POST /registrations/{id}?action=copy` |
| T21 `get_makeup_credits` | `GET /credits?status=active` |
| T24 `get_auto_enrolment_responses` | `GET /registration_retention_responses` |

---

### Phase 2 — Small API additions (extend existing endpoints)

| Tool | What to add |
|------|------------|
| T03 `get_widget_embed_code` | `GET /courses/{id}/widget_config` returning embed snippet |
| T05 `create_manual_trial` | Explicit `trial` status support on `POST /registrations` for admin-created trials |
| T06 `report_trial_pipeline` | Filter `status=trial_ended&no_active_registration=true` on GET /registrations |
| T16 `generate_invoice_batch` | `POST /invoices/batch_generate` to pre-generate missing invoices before bulk download |
| T17 `bulk_cancel_sessions` | `POST /events/bulk_cancel` with `{ date, instructor_id?, notify, offer_makeup }` |
| T22 `resend_client_access` | `POST /persons/{id}/resend_access` |
| T25 `apply_sibling_discount` | `POST /orders/apply_sibling_discount` linking siblings and applying discount across family |
| T28 `report_instructor_performance` | `GET /reports/instructor_performance?term={id}` aggregating existing trainer rate data |

---

### Phase 3 — New endpoints required

| Tool | New endpoint | Complexity |
|------|-------------|------------|
| T01 `get_account_readiness_score` | `GET /account/readiness` | Medium |
| T02 `run_prelaunch_audit` | `GET /courses/{id}/audit` | Medium |
| T04 `get_programme_booking_link` | `GET /courses/{id}/booking_link` | Low |
| T07 `report_non_renewals` | `GET /reports/non_renewals` | Medium |
| T08 `get_class_waiting_list` | `GET /availability_requests?schedule_id={id}` | Low |
| T09 `get_upsell_opportunities` | `GET /reports/upsell_opportunities` | Medium |
| T15 `check_gocardless_health` | `GET /direct_debit_mandates/health` | Low |
| T18 `bulk_mark_attendance` | `PUT /attendance/bulk` | Low |
| T23 `calculate_prorata` | `POST /orders/calculate_prorata` | Medium |
| T26 `report_revenue_forecast` | `GET /reports/revenue_forecast` | High |
| T27 `report_at_risk_clients` | `GET /reports/at_risk_clients` | High |
| T29 `report_missing_revenue` | `GET /reports/revenue_gap` | Medium |
| T30 `report_registration_lifecycle` | `GET /reports/registration_lifecycle` | High |

---

## 10. Feasibility Summary

| Status | Count | Notes |
|--------|------:|-------|
| ✅ READY — ship now | 9 tools | Phase 1 |
| ⚠️ PARTIAL — small addition | 8 tools | Phase 2 |
| ❌ MISSING — new endpoint | 13 tools | Phase 3 |
| **Total** | **30** | |

Foundation tier: 5 READY · 1 MISSING implementation · 2 PARTIAL (OAuth) · 1 READY composite

---

## 11. API Gap Specs

Individual idea specs have been filed in `api-v1/specs/ideas/` for each group of missing endpoints:

- `2026-05-23-mcp-bulk-operations.md` — bulk cancel, bulk attendance, bulk credits
- `2026-05-23-mcp-reporting-intelligence.md` — all new report endpoints
- `2026-05-23-mcp-client-booking-utilities.md` — prorata, waiting list, access resend
- `2026-05-23-mcp-account-health.md` — account readiness, GoCardless health, prelaunch audit

---

## 12. Full Catalog Reference

The complete inventory of ~205 tools, 25 skills, and 30 artifacts (including items not in the top 30) is maintained at:

`help/build/reports/mcp-full-catalog-v2.md`

Use the catalog when extending Phase 2/3 scope or evaluating additional tools for future releases.

---

*Evidence sources: Zoho 3,276 tickets (2024–2025) · Intercom ~170 conversations (Feb–Apr 2026) · WhatsApp Kate/babyballet + Anna/Turtle Tots + Dom/Wee Kicks (Dec 2025–May 2026)*  
*KB sources: onboarding-launch-faq · getting-started-with-zooza · instructor-rate-reward · trials-faq · core-workflows (W01–W15)*  
*API checked against: `api-v1/` PHP codebase (141 endpoint files)*  
*Last updated: 2026-05-23*
