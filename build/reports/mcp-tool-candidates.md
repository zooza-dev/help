# Zooza MCP Server — Tool Candidates

**Method:** Bottom-up from real support data. Every tool traces to a specific pain point evidenced across sources.  
**Sources:** Zoho (3,276 tickets) · Intercom (~170 conversations) · WhatsApp (Kate/babyballet, Anna/Turtle Tots, Dom/Wee Kicks)  
**Date:** 2026-05-22

---

## How to read this document

Each tool entry shows:
- **Pain point** — what the admin had to do manually (the problem, not the feature)
- **Evidence** — ticket counts and sources that confirm this is real
- **Trigger** — how the admin would phrase it
- **Inputs / Output** — what the agent needs and what it does
- **Value** — ⏱ time saving · 👁 visibility · 💰 revenue impact

Tools are ordered within each tier by evidence strength.

---

## Priority tiers

| Tier | Criteria |
|------|----------|
| **Tier 1** | 50+ Zoho tickets OR confirmed across all 3 sources — build first |
| **Tier 2** | 20–49 Zoho tickets OR confirmed in 2 sources — high value |
| **Tier 3** | Under 20 tickets OR single source but clearly articulated — good to have |

---

## Tier 1 — Build first

---

### T1-01 · Show make-up credit status by client / location

**Pain point:** Admins cannot see which clients have unused make-up credits, how many, or when they expire. Every inquiry requires opening each client record individually. There is no location-level or programme-level view.

**Evidence:**
- Zoho: **227 tickets** — single largest cluster in the dataset (tagged: replacement, náhradná hodina, make-up)
- Intercom: 2 conversations — confusion between "replacement" and "credit transfer"; no bulk view
- WhatsApp: Kate (clients asking her directly instead of self-serving), Anna (parents confused)
- Intercom P1 critical gap: location-level make-up report doesn't exist in Zooza — team produces manual custom exports on request

**Trigger:** *"Show me all unused make-up credits for the Tuesday Ballet group"*  
*"How many make-up sessions does Jana Nováková still have?"*

| | |
|---|---|
| **Inputs** | filter: client / group / programme / location · status: unused / used / expired |
| **Output** | list of clients with credit count, expiry date, programme, location |
| **Value** | 👁 visibility |

---

### T1-02 · Set payment plan on registration

**Pain point:** Setting or correcting a payment schedule on a registration is done individually per booking. Michal regularly did this for clients who couldn't navigate the settings. Incorrect payment plans caused wrong balances, confusion, and follow-up support.

**Evidence:**
- Zoho: **124 tickets** — tagged: payment_schedules, splátkový kalendár, instalment
- Intercom: 1 conversation (billing period setup)
- WhatsApp: Kate (days resolving billing period blocks), Anna (payment template applied incorrectly), Michal manually set plans for new registrations repeatedly

**Trigger:** *"Set a 4-instalment payment plan on Peter Kováč's registration in the Monday group"*

| | |
|---|---|
| **Inputs** | client · registration / booking ID · payment plan (instalments, interval, first due date, amount) |
| **Output** | payment plan set · client notified · confirmation of amounts |
| **Value** | ⏱ time saving |

---

### T1-03 · Generate and export invoice batch

**Pain point:** Admins can't bulk-download invoices. They need to export individual invoices or use XML export that is hard to find. Monthly accountant handover requires 20–40 minutes of manual navigation.

**Evidence:**
- Zoho: **117 tickets** — tagged: faktura, invoice, XML export, doklady
- Intercom: 1 conversation ("how to download all invoices at once in XML format")
- WhatsApp: Anna (weekly Xero reconciliation blocked by invoice access), Dom (accountant blocked 2 weeks)

**Trigger:** *"Export all invoices from March for my accountant"*

| | |
|---|---|
| **Inputs** | date range · format (PDF / XML / CSV) · filter: programme / payment method |
| **Output** | batch file download · summary: count, total amount, period |
| **Value** | ⏱ time saving |

---

### T1-04 · Show active registrations report

**Pain point:** Generating a clean list of all active registrations with payment status requires navigating Reports & Insights, setting filters, and exporting — a process most admins ask support to explain. Different export types (Clients vs Registrations) return different row counts and confuse admins.

**Evidence:**
- Zoho: **90 tickets** — tagged: report, export, registrations overview
- Intercom: 1 explicit conversation ("generate a report of all active registrations")
- WhatsApp: Anna ("I have 178 clients but 344 registrations — which is correct?"), Kate, Dom (routine)

**Trigger:** *"Show me all active registrations in the Summer 2026 programme with payment status"*

| | |
|---|---|
| **Inputs** | filter: programme / group / date range / payment status |
| **Output** | table: client name · group · status · amount due · last payment date |
| **Value** | 👁 visibility |

---

### T1-05 · Show email automation overview

**Pain point:** Admins don't know which automated emails fire, when, and to whom. Every time an email doesn't arrive or arrives at the wrong time, support must manually walk through Programme Settings → Communication → Message Templates. This is a navigation problem, not a configuration problem.

**Evidence:**
- Zoho: **74 tickets** — tagged: notification, email, email templates, automatické emaily
- Intercom: 3 conversations — session reminder settings location (★★★), trial email timing, payment reminder settings (★★★)
- WhatsApp: Kate (days configuring email templates; "which template fires for trial vs. full enrolment?")

**Trigger:** *"What automated emails does a client receive after signing up for a trial in the Ballet programme?"*

| | |
|---|---|
| **Inputs** | programme · optionally: event trigger (trial booked / payment made / session cancelled) |
| **Output** | list of automated messages: trigger → template name → sends at → channel (email/SMS) |
| **Value** | 👁 visibility |

---

### T1-06 · Transfer client between groups (with payment balance)

**Pain point:** Transferring a client between groups is a common weekly operation. The Transfer function exists but is hard to find, and payment balances often reset after transfer — requiring a second manual correction. Multiple clients escalated to support specifically because they couldn't find the Transfer button.

**Evidence:**
- Zoho: **64 tickets** — tagged: transfer, presun, move client
- Intercom: 2 explicit conversations ("how do I move a client?"; "help with Transfer function")
- WhatsApp: Kate (payment balance reset after transfer, multiple instances), Anna (between-programme moves), Dom

**Trigger:** *"Move Jana Nováková from the Monday 10:00 group to Wednesday 11:00, keep her payments"*

| | |
|---|---|
| **Inputs** | client · source group · target group · carry over payment balance (yes/no) |
| **Output** | booking transferred · payment plan adjusted · client notified |
| **Value** | ⏱ time saving |

---

### T1-07 · Resend client portal access / login PIN

**Pain point:** The parent portal uses PIN-based login. Verification codes frequently don't arrive (email delivery, spam filter). When a parent can't log in they contact the studio admin, who must navigate to the client record and resend access manually.

**Evidence:**
- Zoho: **54 tickets** — tagged: prihlasovanie, login, PIN, nefunguje prihlasovanie, portal access
- WhatsApp: all three clients (Kate, Anna, Dom) — repeated occurrences, described as "annoying weekly task"
- Intercom: handled by AI agent but not resolved (language mismatch noted)

**Trigger:** *"Resend the login link to Jana Nováková — she can't access the parent portal"*

| | |
|---|---|
| **Inputs** | client email or name |
| **Output** | new access link / PIN sent to client · confirmation |
| **Value** | ⏱ time saving |

---

### T1-08 · Show unmatched / ignored payments

**Pain point:** Incoming bank payments (via GoCardless, bank transfer, Stripe) sometimes fail to match to a registration. These sit as "unmatched" or get marked "ignored." Admins have no dashboard view — they discover it only when a client complains about balance discrepancy.

**Evidence:**
- Zoho: **68 tickets** — tagged: párovanie, nespárování, unmatched, payment pairing
- Intercom: 3 conversations (GoCardless vs email notification confusion; FIO bank pairing delay)
- WhatsApp: Kate (months of unmatched GoCardless payments), Anna (Xero vs Zooza mismatch), Dom (wrong gateway collected money)

**Trigger:** *"Show me all payments that came in but weren't matched to any registration"*

| | |
|---|---|
| **Inputs** | time range · filter: GoCardless / bank transfer / Stripe |
| **Output** | list of unmatched payments · amount · client name (if detectable) · suggested match where possible |
| **Value** | 👁 visibility · 💰 revenue |

---

### T1-09 · GoCardless health check

**Pain point:** GoCardless connection expires silently every 90 days. Zooza shows no expiry warning. Admins find out only when payments stop arriving — often days or weeks later. Reconnecting requires navigating to the correct settings screen which most admins can't find without support.

**Evidence:**
- Zoho: **34 tickets** — tagged: GoCardless, mandát, reconnect, GC expiry (subset of 68 above, GoCardless-specific)
- Intercom: 2 explicit conversations ("how do I check if GoCardless is active?"; "what is the difference between GoCardless and bank email pairing?") — **Intercom P1**
- WhatsApp: Kate (multiple 90-day expiry cycles, months without sync), Dom (mandate migration)

**Trigger:** *"Is my GoCardless connection working?"*

| | |
|---|---|
| **Inputs** | (none) |
| **Output** | status: active / expired / expiring soon · expiry date · number of active mandates · if expiring within 14 days → alert + direct link to reconnect |
| **Value** | 👁 visibility · 💰 revenue |

---

### T1-10 · Copy term structure and registrations

**Pain point:** End-of-term rebooking requires manually recreating the group structure for the new term, then copying registrations. Admins reported spending 2+ hours on this. There is no native way to copy only the registrations that confirmed continuation — all or nothing.

**Evidence:**
- Zoho: **43 tickets** — tagged: kopírovanie, copy group, copy programme, term rollover
- Intercom: 2 rich conversations — "copy registrations to new course" (2026-03-02); "copy only registrations that confirmed continuation" (2026-03-23, confirmed as missing feature)
- WhatsApp: Michal spent 2+ hours doing this manually for Anna; Kate and Dom both required help

**Trigger:** *"Set up Summer 2026 — copy all confirmed registrations from Winter 2025 into the new groups"*

| | |
|---|---|
| **Inputs** | source term · target term · filter: confirmed only / all active |
| **Output** | N registrations copied · new booking links generated · admins can review before sending invitations |
| **Value** | ⏱ time saving |

---

### T1-11 · Send payment reminder to unpaid clients

**Pain point:** Chasing unpaid registrations requires filtering by payment status, identifying clients, and composing a message. Automatic reminders exist but the setting is so hard to find that it was a top-3 Intercom question. Manual bulk reminders require navigating two separate flows.

**Evidence:**
- Zoho: Payments is the **#1 category — 208 tickets** (covers payment chasing, overdue, outstanding)
- Intercom: ★★★ "where are the automatic reminder settings?" — appeared in 3 conversations
- WhatsApp: Anna (regular weekly task), Kate (set up automatic reminders but couldn't find the screen)

**Trigger:** *"Send a payment reminder to everyone in the Tuesday group who hasn't paid yet"*

| | |
|---|---|
| **Inputs** | filter: group / programme / all · message text or saved template · channel: email / SMS |
| **Output** | message sent to N clients · list of recipients with amount due |
| **Value** | ⏱ time saving · 💰 revenue |

---

## Tier 2 — High value

---

### T2-01 · Cancel full day and notify clients

**Pain point:** Cancelling a day when an instructor is sick requires opening each session individually, cancelling, and notifying clients one by one. Clients receive separate emails per session rather than one clear message.

**Evidence:**
- Zoho: Calendar category — **52 tickets**
- Intercom: 2 conversations (cancellation scope confusion; what happens to student if session cancelled and they don't attend)
- WhatsApp: Anna (pool venue closures, bank holidays), Kate

**Trigger:** *"Cancel all sessions tomorrow — instructor is sick. Offer make-up to everyone."*

| | |
|---|---|
| **Inputs** | date · instructor filter (optional) · notification text or template · offer make-up (yes/no) |
| **Output** | N sessions cancelled · make-up tokens activated · one message sent per affected client |
| **Value** | ⏱ time saving |

---

### T2-02 · Show auto-enrolment responses

**Pain point:** When auto-enrolment runs, there is no single screen showing who confirmed continuation, who is pending, and who declined. Admins manually check individual registrations or ask support.

**Evidence:**
- Intercom: **2 rich conversations** — one explicitly confirmed this screen doesn't exist (2026-03-17); one asked how to copy only confirmed continuations (2026-03-23)
- Zoho: 4 tickets (retencia tag) — low ticket count because clients don't know the term
- WhatsApp: Michal needed this data to execute term rebooking for Anna

**Trigger:** *"Show me who has confirmed continuation for the Summer term in the Ballet programme"*

| | |
|---|---|
| **Inputs** | programme · term |
| **Output** | table: client · group · response status (confirmed / pending / declined) · response date |
| **Value** | 👁 visibility |

---

### T2-03 · Apply session credit to next payment

**Pain point:** When a class is cancelled (bank holiday, illness, venue closure), the studio owes clients a credit on their next payment. This must be applied manually per registration — there is no bulk credit action.

**Evidence:**
- Zoho: **26 tickets** — tagged: kredit, credit, cancelled session credit
- WhatsApp: Dom (Christmas holidays, bank holiday credits), Anna (pool venue cancellations requiring credits across 30+ clients)

**Trigger:** *"Cancel Thursday 15 May and reduce everyone's next payment in that group by one session"*

| | |
|---|---|
| **Inputs** | group · session date · credit amount (auto = 1 session price, or manual override) |
| **Output** | credit applied to N registrations · summary of adjustments |
| **Value** | ⏱ time saving |

---

### T2-04 · Show waiting list

**Pain point:** When a class is full, clients go on a waiting list. Admins can't easily see who is waiting, in what order, or when spots opened. Manually promoting a client from waitlist to registered requires several steps.

**Evidence:**
- Zoho: **34 tickets** — tagged: poradovník, waiting_list, waitlist, waiting
- Intercom: 1 conversation (collecting interest without opening for bookings — confirms waitlist UX problem)
- WhatsApp: Kate (full Sunday Tinies class), Anna (multiple full classes)

**Trigger:** *"Who is on the waiting list for Wednesday Ballet? A spot just opened."*

| | |
|---|---|
| **Inputs** | group |
| **Output** | ordered waiting list · days waiting · contact · optionally: promote first-in-line to registered |
| **Value** | 👁 visibility · 💰 revenue |

---

### T2-05 · Resend confirmation email to client

**Pain point:** Clients contact the studio when they don't receive a booking confirmation. The admin must locate the client, navigate to their registration, and trigger a manual resend. In one case (Anna, Asia region), an entire batch failed and Michal resent hundreds of confirmations manually.

**Evidence:**
- Zoho: **12 tickets** tagged: neodoslané, re-send, confirmation not received
- Intercom: 1 conversation (trial automation email not firing after trial was attended)
- WhatsApp: Anna (bulk confirmation failure — full day of manual resends), Kate

**Trigger:** *"Jana Nováková didn't receive her booking confirmation — resend it"*

| | |
|---|---|
| **Inputs** | client · registration (optional — auto-detected) |
| **Output** | confirmation email resent · delivery confirmed |
| **Value** | ⏱ time saving |

---

### T2-06 · Find duplicate registrations

**Pain point:** Parents re-register when their first booking wasn't confirmed, or admins create test registrations during setup. There is no duplicate detection. Cleaning up requires reviewing registrations one by one.

**Evidence:**
- WhatsApp: Anna (15+ duplicates during onboarding; "I have 82 bookings but 172 clients in CRM"), Kate (test registrations), Dom
- Zoho: within broader registration cluster (~295 tickets) but no dedicated tag

**Trigger:** *"Show me clients who have more than one active registration in the same group"*

| | |
|---|---|
| **Inputs** | filter: programme / group / date range |
| **Output** | list of suspected duplicates · client name · registration dates · amounts · which to keep |
| **Value** | 👁 visibility |

---

### T2-07 · Calculate and apply pro-rata for late registration

**Pain point:** Clients joining mid-term pay only for remaining sessions. The calculation and application is manual — Michal did this repeatedly for both Kate and Anna. No native "late joiner" flow exists.

**Evidence:**
- WhatsApp: Kate (aliquot errors, multi-session problem-solving), Anna (Ramadan absence, 7-week pro-rata)
- Zoho: **2 tickets** tagged 'aliquot' (underrepresented because clients don't know the term)

**Trigger:** *"Jana joins the Monday group from 12 May. There are 6 sessions left. Calculate her price and create the registration."*

| | |
|---|---|
| **Inputs** | client · group · join date · full term price (auto-detected or manual) |
| **Output** | pro-rata amount calculated · registration created with correct amount · client sent payment link |
| **Value** | ⏱ time saving |

---

### T2-08 · Show unconverted trials

**Pain point:** Clients who attended a trial but never registered are invisible without an export. There is no native "trial pipeline" view showing attended → pending → converted.

**Evidence:**
- Intercom: 1 conversation (how to copy a lead from a trial class to another class)
- Zoho: within bookings cluster (6 tickets) 
- WhatsApp: Kate (ThinkSmart trialists switching to Zooza), Anna (trial-to-enrolment bug causing frustration)

**Trigger:** *"Who came to a trial in the last 30 days and hasn't registered yet?"*

| | |
|---|---|
| **Inputs** | time range · filter: programme / location |
| **Output** | list of unconverted trials · days since trial · client contact · programme |
| **Value** | 👁 visibility · 💰 revenue |

---

### T2-09 · Reactivate session reminders for a client

**Pain point:** Clients can accidentally or intentionally disable session reminders on their profile. When they start missing classes and ask "I'm not getting reminders," the admin must navigate to the client record and find the notification toggle.

**Evidence:**
- Intercom: **1 explicit conversation** — "how to reactivate disabled lesson reminders for a client" (2026-03-19)
- Zoho: within 74 notification tickets

**Trigger:** *"Turn session reminders back on for Jana Nováková — she says she stopped getting them"*

| | |
|---|---|
| **Inputs** | client |
| **Output** | session reminders reactivated · confirmation |
| **Value** | ⏱ time saving |

---

### T2-10 · Bulk payment template change on registrations

**Pain point:** When switching from monthly membership to termly billing (or any template change), the admin must update every registration individually. At 30+ registrations this takes 30–60 minutes.

**Evidence:**
- Zoho: within 124 payment_schedules tickets
- WhatsApp: Kate (days resolving billing period blocks), Dom (mandate migration required template change across all registrations)

**Trigger:** *"Switch all registrations in the Monday Ballet group from monthly to the new Summer 2026 termly template"*

| | |
|---|---|
| **Inputs** | filter: group / programme · new payment template |
| **Output** | template applied to N registrations · summary of changes · warning if any registration had a different amount |
| **Value** | ⏱ time saving |

---

### T2-11 · Show group capacity overview

**Pain point:** Admins have no single view showing which groups are full, nearly full, or have space. They check classes one by one or rely on memory. This affects sales decisions and waiting list management.

**Evidence:**
- Zoho: within bookings cluster (34 waiting list tickets + broader capacity questions)
- WhatsApp: Kate (full Sunday Tinies class, overbooked when extra capacity unlocked), Anna (many full classes — couldn't see which had space)

**Trigger:** *"Where do I have free spots this week? Which groups have a waiting list?"*

| | |
|---|---|
| **Inputs** | filter: programme / location / age group |
| **Output** | groups sorted by occupancy · free spots · waiting list count |
| **Value** | 👁 visibility · 💰 revenue |

---

## Tier 3 — Good to have

These are evidenced but lower frequency or higher implementation complexity.

| ID | Tool | Pain point | Evidence |
|----|------|------------|----------|
| T3-01 | `apply_sibling_discount` | Sibling discount applied per-family manually — no automation | WhatsApp: Kate, Anna; Intercom: 1 convo |
| T3-02 | `pause_registration` | No native pause/defer feature — Michal handled manually | WhatsApp: Dom (Christmas), Anna (pool closure) |
| T3-03 | `archive_programme` | Admins can't find archive function, confuse it with delete | Intercom: **5 convos** — top Intercom topic; Kate, Anna |
| T3-04 | `archive_group` | Same as above at group level | Intercom: 1 convo; Kate, Anna |
| T3-05 | `show_payment_mismatches` | Registrations where amount charged ≠ expected price | Zoho: 23 tickets; WhatsApp: Kate |
| T3-06 | `set_user_role` | Instructor role setup — can't find setting | Intercom: 1 explicit convo; Zoho: within 137 settings tickets |
| T3-07 | `create_oneoff_event` | One-off events / birthday parties — no dedicated flow | WhatsApp: Dom; Zoho: 17 tickets |
| T3-08 | `show_refund_status` | Refunds done in Stripe, not reflected in Zooza | WhatsApp: Anna (100+ refunds), Dom |
| T3-09 | `check_sms_delivery` | SMS not sending — no delivery status visible | Zoho: 29 tickets |
| T3-10 | `send_bulk_email_to_group` | Bulk email to a class — two entry points confuse admins | Zoho: Communication 73 tickets; Intercom: 10 convos |
| T3-11 | `change_group_time` | Change class time on future sessions | Intercom: 1 convo; Kate |
| T3-12 | `change_group_instructor` | Reassign instructor on group or sessions | WhatsApp: Anna; Intercom: 1 convo |
| T3-13 | `create_discount_code` | Create and assign discount code | Intercom: 1 convo; Zoho: 28 tickets |
| T3-14 | `show_network_revenue_summary` | Franchise master view — per-franchisee revenue | WhatsApp: Dom |
| T3-15 | `show_booking_link` | "Where is the registration form link?" — ★★ Intercom | Intercom: 2 convos; Zoho: within registration 295 |
| T3-16 | `validate_registration_pricing` | Catch wrong prices before clients see them | Zoho: 23; WhatsApp: Kate |
| T3-17 | `generate_invoice_for_booking` | Send a generated invoice to a client | Intercom: 1 convo |
| T3-18 | `set_billing_period_for_group` | Configure term billing period blocks | WhatsApp: Kate (days); Intercom: 1 convo |
| T3-19 | `bulk_enable_auto_enrolment` | Enable auto-continuation on multiple groups at once | WhatsApp: Anna (asked for bulk setup) |
| T3-20 | `bulk_enable_trial` | Enable trial on multiple courses at once | WhatsApp: Anna |

---

## Backlog — not MCP tools, but real gaps

These appeared in the data but are product gaps, not things an MCP tool can solve:

| Gap | Evidence | Why it's a product gap |
|-----|----------|----------------------|
| Attendance mobile UI — too slow during a live class | WhatsApp: Anna, Kate (all instructors) | UX problem, not a data action |
| Sibling discount automation rule | Zoho: 28; WhatsApp: Kate, Anna | Requires a new pricing rule engine |
| GoCardless proactive expiry warning (in-app) | Intercom P1 | Requires in-app notification system |
| Refund action inside Zooza (not Stripe) | WhatsApp: Anna (100+ refunds) | Requires Stripe API write access |
| Full-name field in exports | Zoho: ZOOZA-4666 | Schema change |
| Auto-promote from waiting list when spot opens | WhatsApp: Kate, Anna | Automated trigger, not agent action |
| Xero native sync | WhatsApp: Anna (weeks of reconciliation) | Third-party integration |

---

## Summary: evidence ranking

| Rank | Tool | Zoho tickets | Intercom | WhatsApp |
|------|------|-------------|----------|----------|
| 1 | T1-01 show_makeup_credits | **227** | 2 | Kate, Anna |
| 2 | Payments (all payment tools) | **208** | 11 | all 3 |
| 3 | T1-02 set_payment_plan | **124** | 1 | Kate, Anna, Michal |
| 4 | T1-03 generate_invoice_batch | **117** | 1 | Anna, Dom |
| 5 | T1-04 show_active_registrations | **90** | 1 | all 3 |
| 6 | T1-05 show_email_automation | **74** | 3 | Kate |
| 7 | T1-06 transfer_client | **64** | 2 | Kate, Anna, Dom |
| 8 | T1-07 resend_client_access | **54** | — | all 3 |
| 9 | T1-08 show_unmatched_payments | **68** | 3 | Kate, Anna, Dom |
| 10 | T1-09 gocardless_health | **34** | 2 | Kate, Dom |

---

*Sources: Zoho 3,276 tickets · Intercom ~170 conversations · WhatsApp Kate/Anna/Dom*  
*Generated bottom-up from support data — every tool traces to a real admin pain point*  
*Last updated: 2026-05-22*
