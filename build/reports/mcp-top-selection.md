# Zooza MCP — Final Selection: Top 30 Tools + 30 Skills/Artifacts

**Goal:** Make Zooza the place where it's easy to:
- 🎯 **Make an offer** — find prospects, run trials, convert, win back
- 💰 **Collect money** — chase payments, fix billing, close the month
- ⚙️ **Run daily business** — cancel, transfer, attend, reschedule
- 👁 **See what's happening** — reports, alerts, revenue gaps

**Next step:** API feasibility check → developer spec  
**Date:** 2026-05-22

---

## How to read this

Each tool has:
- `entity` — what Zooza object it operates on
- `inputs` — what the agent needs to ask / infer
- `output` — what it returns or does
- `evidence` — ticket/conversation count that justifies it
- `pillar` — which business goal it serves

---

## TOP 30 TOOLS

### 🎯 PILLAR 1 — Make an offer (6 tools)

---

#### T01 · `get_programme_booking_link`
| | |
|---|---|
| **Entity** | Programme |
| **Inputs** | programme name or ID |
| **Output** | Public registration URL + QR code + embed code |
| **Evidence** | Intercom ★★ "where is the registration form link" — repeated |
| **Why** | Every sales conversation starts with "send me the link" |

---

#### T02 · `list_unconverted_trials`
| | |
|---|---|
| **Entity** | Booking |
| **Inputs** | time range (default: last 30 days) · filter: programme / location |
| **Output** | List: client name, contact, trial date, programme, days since trial |
| **Evidence** | Intercom: 1 convo · WhatsApp: Kate, Anna · direct revenue signal |
| **Why** | These are warm leads. Every unconverted trial = lost registration fee |

---

#### T03 · `get_auto_enrolment_responses`
| | |
|---|---|
| **Entity** | Programme |
| **Inputs** | programme · term |
| **Output** | Table: client · group · status (confirmed / pending / declined) · response date |
| **Evidence** | Intercom explicit gap (2026-03-17) — this screen does not exist in Zooza today |
| **Why** | Admin can't run rebooking without knowing who confirmed. Blocked every term |

---

#### T04 · `report_non_renewals`
| | |
|---|---|
| **Entity** | Booking |
| **Inputs** | source term · target term |
| **Output** | List of lapsed clients: name, contact, how many terms active, last class |
| **Evidence** | WhatsApp: Anna, Kate, Dom every term · Intercom: orders cluster |
| **Why** | Win-back campaign input. High-intent clients who just didn't re-register |

---

#### T05 · `get_class_waiting_list`
| | |
|---|---|
| **Entity** | Class |
| **Inputs** | class / group |
| **Output** | Ordered list: client name, contact, days waiting, child age |
| **Evidence** | Zoho: 34 tickets (waitlist) · Kate (full Sunday class) · Anna (many full classes) |
| **Why** | When a spot opens, admin needs this list immediately to call or promote |

---

#### T06 · `report_capacity_overview`
| | |
|---|---|
| **Entity** | Class |
| **Inputs** | filter: programme / location / age group |
| **Output** | All groups: occupancy %, free spots, waiting list count, revenue potential |
| **Evidence** | Kate, Anna — couldn't see which groups had space without clicking through each |
| **Why** | Sell where you have room. Stop selling where you're full |

---

### 💰 PILLAR 2 — Collect money (9 tools)

---

#### T07 · `send_payment_reminder`
| | |
|---|---|
| **Entity** | Booking |
| **Inputs** | filter: class / programme / all unpaid · message text or template · channel: email / SMS |
| **Output** | Message sent to N clients · list of recipients with amount due |
| **Evidence** | Zoho: Payments #1 (208 tickets) · Intercom ★★★ "where are reminder settings" · Anna weekly |
| **Why** | Most common revenue action. Currently: export → email → manual. Should be one command |

---

#### T08 · `set_payment_plan`
| | |
|---|---|
| **Entity** | Booking |
| **Inputs** | booking ID · plan: instalments, interval, first due date, amounts |
| **Output** | Payment plan set · amounts confirmed · client notified |
| **Evidence** | Zoho: 124 tickets · WhatsApp: Kate/Anna — Michal set these manually repeatedly |
| **Why** | Every new registration with instalments needs this. No bulk option today |

---

#### T09 · `bulk_change_payment_template`
| | |
|---|---|
| **Entity** | Booking |
| **Inputs** | filter: group / programme · new payment template |
| **Output** | Template applied to N bookings · summary · warnings on amount changes |
| **Evidence** | WhatsApp: Kate (days resolving billing blocks) · Dom (mandate migration) |
| **Why** | Term switch = template change on 30+ registrations. Currently 30+ manual edits |

---

#### T10 · `show_unmatched_payments`
| | |
|---|---|
| **Entity** | Payment |
| **Inputs** | time range · filter: GoCardless / bank transfer / Stripe |
| **Output** | List of unmatched payments · amount · suggested booking match where detectable |
| **Evidence** | Zoho: 68 tickets · WhatsApp: Kate (months), Anna (Xero mismatch), Dom (wrong gateway) |
| **Why** | Money in the system the admin doesn't know about. Revenue leak |

---

#### T11 · `get_gocardless_status`
| | |
|---|---|
| **Entity** | Settings / Payment |
| **Inputs** | (none) |
| **Output** | Status: active / expired / expiring soon · expiry date · mandate count · reconnect link if needed |
| **Evidence** | Intercom P1 · Zoho: 34 tickets · Kate (multiple 90-day cycles), Dom |
| **Why** | Silent failure every 90 days. Admin finds out when payments stop. Zero warning today |

---

#### T12 · `add_manual_payment`
| | |
|---|---|
| **Entity** | Booking |
| **Inputs** | booking ID · amount · date · method (cash / bank transfer / card) · generate invoice? |
| **Output** | Payment recorded · balance updated · invoice generated (if requested) |
| **Evidence** | Zoho: Payments 208 · WhatsApp: Anna, Kate, Dom — daily operation |
| **Why** | Daily operation for schools not on GoCardless. Currently navigating through 3 screens |

---

#### T13 · `generate_invoice_batch`
| | |
|---|---|
| **Entity** | Invoice |
| **Inputs** | date range · format: PDF / XML / CSV · filter: programme / payment method |
| **Output** | Batch file download · summary: count, total, period |
| **Evidence** | Zoho: 117 tickets · Anna (Xero weekly), Dom (accountant blocked 2 weeks) |
| **Why** | Monthly accountant handover. Currently 20–40 min manual navigation |

---

#### T14 · `apply_session_credit_bulk`
| | |
|---|---|
| **Entity** | Booking |
| **Inputs** | class · session date · credit amount (auto = 1 session price, or manual) |
| **Output** | Credit applied to N bookings · summary of adjustments |
| **Evidence** | Zoho: 26 tickets · Dom (bank holidays), Anna (pool closures — 30+ clients) |
| **Why** | When admin cancels a class, clients are owed a credit. No bulk option today |

---

#### T15 · `initiate_refund`
| | |
|---|---|
| **Entity** | Booking / Payment |
| **Inputs** | booking ID · amount (full or partial) · reason |
| **Output** | Refund initiated via Stripe · booking marked as refunded · client notified |
| **Evidence** | WhatsApp: Anna (100+ refunds, all done manually in Stripe) · Dom, Kate |
| **Why** | Currently: open Stripe, find payment, refund, manually update Zooza. Completely outside system |

---

### ⚙️ PILLAR 3 — Daily business (9 tools)

---

#### T16 · `bulk_cancel_sessions`
| | |
|---|---|
| **Entity** | Session |
| **Inputs** | date · instructor filter (optional) · notify clients? · offer make-up? · message text |
| **Output** | N sessions cancelled · make-up tokens activated · 1 message per affected client |
| **Evidence** | Zoho: Calendar 52 · Intercom: 2 convos · Anna, Kate |
| **Why** | Currently: open each session, cancel, notify. 5–15 min clicking for one day |

---

#### T17 · `transfer_booking`
| | |
|---|---|
| **Entity** | Booking |
| **Inputs** | booking ID · target class · carry payment balance: yes/no |
| **Output** | Booking moved · payment plan adjusted · client notified |
| **Evidence** | Zoho: 64 tickets · Intercom: 2 explicit convos · Kate, Anna, Dom |
| **Why** | Weekly operation. Payment balance resets on transfer today — requires manual fix after |

---

#### T18 · `duplicate_booking`
| | |
|---|---|
| **Entity** | Booking |
| **Inputs** | source booking · target class/term · reset payment? |
| **Output** | New booking created · client notified · booking link returned |
| **Evidence** | Zoho: 43 tickets · Intercom: 2 convos · term rebooking foundation |
| **Why** | Core of term rebooking. No way to copy only confirmed registrations today |

---

#### T19 · `bulk_mark_attendance`
| | |
|---|---|
| **Entity** | Session |
| **Inputs** | session ID · list of client statuses (attended / absent / cancelled) |
| **Output** | Attendance saved for N clients · make-up tokens issued for cancellations |
| **Evidence** | Zoho: Calendar/attendance 80 · Anna, Kate (teachers marking after class on paper) |
| **Why** | Daily operation. Mobile UX broken today — instructors can't use it during class |

---

#### T20 · `get_makeup_credits`
| | |
|---|---|
| **Entity** | Make-up / Booking |
| **Inputs** | filter: client / class / programme / location · status: active / used / expired |
| **Output** | List: client, credits, expiry, programme, location |
| **Evidence** | Zoho: 227 tickets — **#1 dataset cluster** · Anna, Kate |
| **Why** | Largest pain point by volume. No bulk view exists today. Every inquiry = manual |

---

#### T21 · `show_makeup_report_by_location`
| | |
|---|---|
| **Entity** | Make-up |
| **Inputs** | location · time range |
| **Output** | Summary: credits issued / used / expired per location + per programme |
| **Evidence** | Intercom P1 critical gap — this report does not exist in Zooza · 3 convos in 1 day |
| **Why** | Multi-location schools need this weekly. Team produces custom export manually today |

---

#### T22 · `resend_client_access`
| | |
|---|---|
| **Entity** | Client |
| **Inputs** | client email or name |
| **Output** | New portal access link / PIN sent · delivery confirmation |
| **Evidence** | Zoho: 54 tickets · WhatsApp: all 3 clients — "annoying weekly task" |
| **Why** | Parent can't log in → calls admin → admin spends 5 min finding resend option |

---

#### T23 · `calculate_prorata`
| | |
|---|---|
| **Entity** | Booking |
| **Inputs** | client · class · join date · full term price (auto-detected or manual) |
| **Output** | Pro-rata amount · registration created with correct amount · payment link |
| **Evidence** | WhatsApp: Kate (aliquot errors), Anna (Ramadan, 7-week pro-rata) · Zoho: 2 |
| **Why** | No native late-joiner flow. Michal calculated and created manually every time |

---

#### T24 · `bulk_update_programmes`
| | |
|---|---|
| **Entity** | Programme |
| **Inputs** | filter (programme list or "all in term") · settings to change: trial / auto-enrolment / visibility / make-up / down payment / aliquot |
| **Output** | N programmes updated · change summary |
| **Evidence** | WhatsApp: Anna (asked Michal to set up all programmes at once) · Kate |
| **Why** | Term setup = same settings on 10–20 programmes. Currently one-by-one |

---

### 👁 PILLAR 4 — Visibility (6 tools)

---

#### T25 · `report_unpaid_clients`
| | |
|---|---|
| **Entity** | Booking |
| **Inputs** | filter: programme / class / date range · threshold: amount / days overdue |
| **Output** | Table: client · class · amount · due date · days overdue · last contact |
| **Evidence** | Zoho: Payments 208 — #1 category · feeds directly into T07 |
| **Why** | Foundation of the payment chase workflow. Who owes what |

---

#### T26 · `report_missing_revenue`
| | |
|---|---|
| **Entity** | Class / Programme |
| **Inputs** | filter: programme / location / term |
| **Output** | Gap analysis: max capacity × price vs actual revenue — per group and total |
| **Evidence** | Strategic signal. Feeds into sales and scheduling decisions |
| **Why** | Shows exactly where the business is leaving money on the table |

---

#### T27 · `report_revenue_by_location`
| | |
|---|---|
| **Entity** | Payment |
| **Inputs** | date range · filter: location |
| **Output** | Revenue breakdown: collected / outstanding / invoiced per location |
| **Evidence** | Dom (franchise master view) · management reporting need |
| **Why** | Multi-location and franchise operations need location-level P&L |

---

#### T28 · `get_email_automation_overview`
| | |
|---|---|
| **Entity** | Programme / Communication |
| **Inputs** | programme · optionally: event trigger |
| **Output** | Map: trigger → template name → sends at → channel (email/SMS) → active/inactive |
| **Evidence** | Zoho: 74 tickets · Intercom: 3 convos ★★★ "where are the reminder settings" · Kate |
| **Why** | Every "my client didn't get an email" ticket requires this investigation manually |

---

#### T29 · `show_payment_mismatches`
| | |
|---|---|
| **Entity** | Booking / Payment |
| **Inputs** | filter: programme / class |
| **Output** | Bookings where amount charged ≠ expected (wrong template, aliquot error, manual override) |
| **Evidence** | Zoho: 23 tickets · WhatsApp: Kate (aliquot errors — multiple sessions) |
| **Why** | Catch pricing errors before clients notice. Pro-rata and template bugs surface here |

---

#### T30 · `find_duplicate_clients`
| | |
|---|---|
| **Entity** | Client |
| **Inputs** | filter: programme / date range |
| **Output** | List of suspected duplicates: client name, email, registration count, created dates |
| **Evidence** | WhatsApp: Anna (15+ duplicates, "82 bookings but 172 clients") · Kate (test data) |
| **Why** | No duplicate detection today. Inflates client counts, causes billing confusion |

---

---

## TOP 30 SKILLS + ARTIFACTS

### Skills — 15 compound workflows

---

#### SK01 · `cancel_day`
| | |
|---|---|
| **Pillar** | ⚙️ Daily business |
| **Trigger** | *"Klára is sick tomorrow — cancel all her sessions, offer make-up, notify parents"* |
| **Steps** | 1. Find sessions for the day/instructor · 2. Cancel all · 3. Issue make-up tokens · 4. Send one message per affected client |
| **Tools** | T16 + T20 + `send_message_to_session_clients` |
| **Time saved** | 15–30 min → 30 sec |

---

#### SK02 · `prepare_new_term`
| | |
|---|---|
| **Pillar** | ⚙️ Daily business + 🎯 Make an offer |
| **Trigger** | *"Set up Summer 2026 from Winter 2025 — copy, enable trial, auto-enrolment, online booking"* |
| **Steps** | 1. Copy programme structure · 2. Apply settings (trial / auto-enrolment / online) · 3. Set payment templates · 4. Generate booking links · 5. Return checklist |
| **Tools** | T24 + T08 + T09 + T01 |
| **Time saved** | 2–4 hours → 10 min |

---

#### SK03 · `run_term_rebooking`
| | |
|---|---|
| **Pillar** | ⚙️ Daily business + 💰 Collect money |
| **Trigger** | *"Copy all confirmed registrations from Winter 2025 to Summer 2026 and send invitations"* |
| **Steps** | 1. Fetch auto-enrolment responses (T03) · 2. Duplicate confirmed bookings (T18) · 3. Set payment plans · 4. Send invitation with payment link |
| **Tools** | T03 + T18 + T08 + `send_bulk_email` |
| **Time saved** | 1–2 hours → 5 min |

---

#### SK04 · `end_of_term_cleanup`
| | |
|---|---|
| **Pillar** | ⚙️ Daily business + 🎯 Make an offer |
| **Trigger** | *"Wrap up Winter 2025 — archive empty groups, send win-back to non-renewals"* |
| **Steps** | 1. Identify non-renewals (T04) · 2. Find empty groups · 3. Archive empty groups · 4. Send win-back message |
| **Tools** | T04 + `archive_class` + `send_bulk_email` |
| **Time saved** | 45–60 min → 5 min |

---

#### SK05 · `chase_unpaid`
| | |
|---|---|
| **Pillar** | 💰 Collect money |
| **Trigger** | *"Send reminders to all clients who haven't paid this term"* |
| **Steps** | 1. Fetch unpaid clients (T25) · 2. Segment by overdue days · 3. Send reminder with amount and payment link |
| **Tools** | T25 + T07 |
| **Time saved** | 20–40 min → 2 min |

---

#### SK06 · `handle_instructor_absence`
| | |
|---|---|
| **Pillar** | ⚙️ Daily business |
| **Trigger** | *"Anna can't teach today — find a substitute for her 10:00 and 11:00 and notify the parents"* |
| **Steps** | 1. List Anna's sessions today · 2. Show available instructors · 3. Assign substitute · 4. Notify enrolled parents |
| **Tools** | `get_instructor_schedule` + `set_session_instructor` + `send_message_to_session_clients` |
| **Time saved** | 20–30 min → 3 min |

---

#### SK07 · `convert_trial_to_enrolment`
| | |
|---|---|
| **Pillar** | 🎯 Make an offer |
| **Trigger** | *"Find all trial clients from the last month who haven't registered yet and send them an offer"* |
| **Steps** | 1. Fetch unconverted trials (T02) · 2. Compose offer message · 3. Send with booking link |
| **Tools** | T02 + T01 + `send_bulk_email` |
| **Time saved** | 30 min → 2 min + direct revenue |

---

#### SK08 · `setup_family_sibling_discount`
| | |
|---|---|
| **Pillar** | 💰 Collect money + ⚙️ Daily business |
| **Trigger** | *"The Novák family has two kids — apply the sibling discount to both registrations"* |
| **Steps** | 1. Find sibling bookings · 2. Verify same parent account · 3. Apply discount to both · 4. Confirm adjusted amounts |
| **Tools** | `get_sibling_clients` + `apply_sibling_discount` |
| **Time saved** | 10–15 min → 1 min |

---

#### SK09 · `onboard_new_programme`
| | |
|---|---|
| **Pillar** | 🎯 Make an offer + ⚙️ Daily business |
| **Trigger** | *"Create Ballet Junior — set up the payment plan, enable trial, add the first Monday group, give me the booking link"* |
| **Steps** | 1. Create programme · 2. Set payment template · 3. Enable trial · 4. Create first class · 5. Enable online booking · 6. Return booking link |
| **Tools** | T24 + T08 + `create_class` + T01 |
| **Time saved** | 30–60 min → 5 min |

---

#### SK10 · `monthly_financial_close`
| | |
|---|---|
| **Pillar** | 💰 Collect money |
| **Trigger** | *"Generate last month's invoices and show me what's unmatched"* |
| **Steps** | 1. Show unmatched payments (T10) · 2. Generate invoice batch (T13) · 3. Return financial summary |
| **Tools** | T10 + T13 + `report_financial_summary` |
| **Time saved** | 30–45 min → 3 min |

---

#### SK11 · `setup_make_up_policy_bulk`
| | |
|---|---|
| **Pillar** | ⚙️ Daily business |
| **Trigger** | *"Enable make-up sessions on all programmes for Summer 2026 with the standard settings"* |
| **Steps** | 1. List programmes without make-up · 2. Apply make-up settings to all · 3. Confirm |
| **Tools** | T24 |
| **Time saved** | 20–30 min → 1 min |

---

#### SK12 · `handle_refund_event`
| | |
|---|---|
| **Pillar** | 💰 Collect money |
| **Trigger** | *"The pool is closed for 3 weeks — credit or refund all affected clients in Monday and Wednesday groups"* |
| **Steps** | 1. Identify affected bookings · 2. Calculate credit (sessions × price) · 3. Apply credit or initiate refund · 4. Notify all affected clients |
| **Tools** | T14 + T15 + `send_bulk_email` |
| **Time saved** | 1–3 hours → 10 min |

---

#### SK13 · `late_joiner_registration`
| | |
|---|---|
| **Pillar** | 🎯 Make an offer + 💰 Collect money |
| **Trigger** | *"Register Jana mid-term, calculate her pro-rata price, send her the payment link"* |
| **Steps** | 1. Calculate pro-rata (T23) · 2. Create booking · 3. Set payment plan · 4. Send confirmation + payment link |
| **Tools** | T23 + T08 + `create_booking` |
| **Time saved** | 10–15 min → 2 min |

---

#### SK14 · `missing_revenue_sweep`
| | |
|---|---|
| **Pillar** | 👁 Visibility |
| **Trigger** | *"Show me where I'm leaving money on the table this term"* |
| **Steps** | 1. Trial pipeline (T02) · 2. Non-renewals (T04) · 3. Capacity gaps (T06) · 4. Missing revenue report (T26) · 5. Summary with recommended actions |
| **Tools** | T02 + T04 + T06 + T26 |
| **Time saved** | Analysis that didn't happen → 2 min |

---

#### SK15 · `gocardless_health_check`
| | |
|---|---|
| **Pillar** | 💰 Collect money |
| **Trigger** | *"Is my GoCardless working? Is there anything unmatched?"* |
| **Steps** | 1. Check GC status (T11) · 2. Show unmatched payments (T10) · 3. Alert if expiry within 14 days |
| **Tools** | T11 + T10 |
| **Time saved** | Prevents revenue loss from silent 90-day expiry |

---

### Artifacts — 15 reusable outputs

| # | Artifact | Format | Pillar | Generated by | Use |
|---|----------|--------|--------|-------------|-----|
| A01 | **Unpaid Clients List** | Table | 💰 | T25 | Weekly chase input |
| A02 | **Trial Pipeline Report** | Table | 🎯 | T02 | Weekly sales review |
| A03 | **Non-Renewals Report** | Table | 🎯 | T04 | End-of-term win-back |
| A04 | **Auto-Enrolment Responses** | Table | ⚙️ | T03 | Pre-rebooking decision |
| A05 | **Capacity Overview** | Summary | 🎯 | T06 | Where to sell more |
| A06 | **Missing Revenue Report** | Summary | 👁 | T26 | Strategic planning |
| A07 | **Make-up Credits Report** | Table | ⚙️ | T21 | Weekly ops by location |
| A08 | **Invoice Batch** | PDF/XML | 💰 | T13 | Accountant handover |
| A09 | **Financial Summary** | Summary | 💰 | SK10 | Management report |
| A10 | **Revenue by Location** | Table | 👁 | T27 | Multi-location P&L |
| A11 | **GoCardless Health Card** | Status | 💰 | T11 | Monthly proactive check |
| A12 | **Email Automation Map** | List | 👁 | T28 | Debug + onboarding |
| A13 | **New Term Setup Checklist** | Checklist | ⚙️ | SK02 | Go-live audit |
| A14 | **Session Cancellation Summary** | Summary | ⚙️ | SK01 | Audit trail |
| A15 | **Client Profile Card** | View | ⚙️ | `get_client` + T20 + T25 | Support context |

---

## Summary view — 30+30 by pillar

| Pillar | Tools | Skills | Artifacts |
|--------|-------|--------|-----------|
| 🎯 Make an offer | T01–T06 | SK02, SK07, SK09, SK13, SK14 | A02, A03, A04, A05 |
| 💰 Collect money | T07–T15 | SK05, SK08, SK10, SK12, SK15 | A01, A08, A09, A10, A11 |
| ⚙️ Daily business | T16–T24 | SK01, SK03, SK04, SK06, SK11 | A04, A07, A13, A14, A15 |
| 👁 Visibility | T25–T30 | SK14 | A06, A10, A12 |

---

## What comes next: API feasibility check

For each of the 30 tools, the API agent will check:

1. **Does the endpoint exist?** → `ready`
2. **Endpoint exists but missing a field/filter?** → `needs parameter`
3. **Endpoint exists but no write access?** → `read-only gap`
4. **No endpoint — would need a new one?** → `needs endpoint`
5. **Requires 2+ endpoints combined?** → `compound — note which`

API spec location: `../api-v1/docs/`

---

*Tools: 30 · Skills: 15 · Artifacts: 15 · Total: 60 items*  
*Ready for API feasibility check*  
*Last updated: 2026-05-22*
