# Zooza — Core Business Workflows

**Date:** 10 May 2026  
**Purpose:** Top 15 activities every class-based business does in Zooza.  
Used for: onboarding priorities, contextual Actions menus, help docs structure, product backlog.

---

## Data sources

| Source | Volume | Period |
|--------|-------:|--------|
| **Zoho tickets** — categorized support cases | 3,276 cases | 2024–2025 |
| **Intercom clusters** — processed conversation clusters | ~100 convos across 13 topic clusters | Feb–Apr 2026 |
| **WhatsApp** — Anna/Turtle Tots, Kate/babyballet, Dom/Wee Kicks | ~2,500 messages | Dec 2025–May 2026 |

**Zoho category breakdown** (tickets with category assigned):

| Category | Tickets | Maps to |
|----------|--------:|---------|
| Payments | 208 | W07, W08, W10, W11, W13 |
| Courses | 199 | W01, W12 |
| Clients | 142 | W03, W06 |
| Settings | 137 | W08, W14, W15 |
| Communication | 73 | W09 |
| Calendar | 52 | W04, W05 |
| Lecturers | 30 | W15 |

Note: ~2,400 Zoho cases have no category assigned (older tickets, pre-categorization). Numbers above are the categorized subset only — actual volume is higher.

---

## How to read this

- **Frequency** — how often a typical operator does this
- **Who** — Admin (owner/manager) · Instructor · Both
- **Entry point** — where in the app this starts
- **Evidence** — ticket/conversation counts from real support data

---

## W01 — Set up a programme and class

**"I want to run a new course. Where do I start?"**

| | |
|--|--|
| **Frequency** | Once per programme, then per term |
| **Who** | Admin |
| **Entry point** | Programmes → New programme |
| **Evidence** | Zoho: Courses/199 tickets · Intercom: Programy a kurzy cluster/13 convos · WhatsApp: Anna, Kate, Dom all hit this in week 1 |

**Steps:**
1. Create programme — set name, type (term / drop-in / single event), payment model, price
2. Add class inside the programme — set day, time, location, instructor, capacity
3. Sessions are auto-generated from the class schedule
4. Enable online booking
5. Copy and share the booking link

**What breaks today:** Users don't know the order (Programme → Class → Sessions). They start from the wrong place. Payment model options are labelled in system language, not business language.

---

## W02 — Manage a trial

**"A new client wants to try the class before committing."**

| | |
|--|--|
| **Frequency** | Weekly |
| **Who** | Admin (setup) · Client (self-books) |
| **Entry point** | Client books via public booking link · Admin monitors in Bookings |
| **Evidence** | Zoho: Rezervácie a kapacita (within Courses/199) · Intercom: Rezervácie a kapacita cluster/5 convos · WhatsApp: Anna (50+ clients blocked), Kate (overbooking) |

**Steps:**
1. Client finds the class online and selects "Trial"
2. System holds a capacity spot and sends confirmation
3. Client attends — instructor marks "Attended" in the register
4. System automatically sends the parent a link to enrol
5. Parent completes enrolment (and payment) via Parent Portal
6. If trial is missed → status becomes "Trial lost" → admin reschedules manually

**What breaks today:** Admin cannot create a trial manually (walk-ins, phone enquiries). Rescheduling "Trial lost" requires a multi-step workaround. "Class full" appears for trials even when enrolled clients try to pay.

---

## W03 — Enrol a client manually

**"A parent called me. I want to add them directly."**

| | |
|--|--|
| **Frequency** | Weekly |
| **Who** | Admin |
| **Entry point** | Clients → select client → Create booking · OR Bookings → Create booking |
| **Evidence** | Zoho: Clients/142 tickets · Intercom: Klienti a kontakty cluster/5 convos, "Ako pridať klienta manuálne?" · WhatsApp: Kate, Dom |

**Steps:**
1. Find or create the client profile
2. Create a booking — select programme and class
3. Set payment method (card link / GoCardless / manual)
4. Send payment link to parent

**What breaks today:** Entry point is not obvious. Kate spent sessions looking for "how to add a client manually." The Create button is buried per-section. No single "Add client + booking" flow.

---

## W04 — Mark attendance

**"Class is starting. I need to know who's here."**

| | |
|--|--|
| **Frequency** | Every class (daily/weekly) |
| **Who** | Instructor · Admin |
| **Entry point** | Calendar → click session → Attendance · OR Sessions → select session |
| **Evidence** | Zoho: Calendar/52 tickets, "Dochadzka" subjects · Intercom: Lekcie a rozvrh cluster/13 convos · WhatsApp: Anna, Kate (teachers printing paper registers) |

**Steps:**
1. Open today's class in Calendar or Sessions
2. For each client: tap Attended / Did not attend / Cancelled
3. If cancelled → optionally offer a make-up session
4. Save

**What breaks today:** Register requires scrolling on phone between classes. Instructors have ~60 seconds between classes. Teachers mark attendance after class, not during — data becomes inaccurate. No dedicated instructor view (simple, fast, offline-capable).

---

## W05 — Cancel a session and offer make-up

**"We can't run Monday's class. What do I do?"**

| | |
|--|--|
| **Frequency** | Weekly |
| **Who** | Admin |
| **Entry point** | Calendar → click session → Cancel session |
| **Evidence** | Zoho: Calendar/52 tickets, "Náhradné hodiny" in subjects (multiple) · Intercom: Lekcie a rozvrh/13 convos — make-up sessions = 7% of all support · WhatsApp: Anna, Kate |

**Steps:**
1. Open the session in the Calendar
2. Cancel the session (choose scope: this session only)
3. System notifies all enrolled clients
4. Admin enables make-up availability — clients book their own replacement slot via Parent Portal
5. Admin monitors make-up usage in the make-up sessions report

**What breaks today:** Scope of cancellation (this session vs all sessions) is not clearly asked. Notifications go out but clients don't always understand what "make-up" means. Make-up report doesn't filter by location (Intercom P1 critical gap).

---

## W06 — Transfer a client to a different class

**"This client wants to move from Monday to Wednesday."**

| | |
|--|--|
| **Frequency** | Weekly |
| **Who** | Admin |
| **Entry point** | Bookings → find booking → Transfer |
| **Evidence** | Zoho: Clients/142 tickets · Intercom: Objednávky cluster/4 convos + Rezervácie a kapacita/5 convos, "Ako skopírovať/presunúť registráciu?" · WhatsApp: Anna, Kate, Dom |

**Steps:**
1. Open the client's booking
2. Use Transfer function — select destination class
3. Choose what to transfer: registration only, or registration + payment balance
4. Confirm — client receives notification of the change

**What breaks today:** Transfer option is not surfaced prominently on the booking detail. Users search for it under wrong section. Payment balance carry-over behaviour is unclear.

---

## W07 — Process a payment manually

**"This client paid by bank transfer. I need to record it."**

| | |
|--|--|
| **Frequency** | Daily / weekly |
| **Who** | Admin |
| **Entry point** | Bookings → find booking → Add payment |
| **Evidence** | Zoho: Payments/208 tickets — #1 category · Intercom: Platby a faktúry cluster/11 convos · WhatsApp: Anna, Kate, Dom — daily issue |

**Steps:**
1. Find the client's booking
2. Open payment detail
3. Click "Add payment" → enter amount, date, method (cash / bank transfer / card)
4. System marks the booking as paid and generates an invoice

**What breaks today:** Payment status is unreadable ("-£1,468 Outstanding"). "Add payment" button exists but users don't find it confidently. Cash/bank transfer payments are not distinguished from card payments in reports.

---

## W08 — Send a payment reminder

**"Several clients haven't paid yet. I want to chase them."**

| | |
|--|--|
| **Frequency** | Weekly / monthly |
| **Who** | Admin |
| **Entry point** | Bookings → filter by payment status → Send email · OR automatic reminders in Settings |
| **Evidence** | Zoho: Settings/137 tickets + Communication/73 tickets · Intercom: Notifikácie a emaily/10 convos, "Kde nastaviť emailové pripomienky?" · WhatsApp: Anna |

**Steps:**
1. Filter bookings by "Outstanding" or "Overdue" payment status
2. Select all → Send email (bulk)
3. OR: configure automatic payment reminders in Settings (sends X days before/after due date)

**What breaks today:** "Where are the automatic reminder settings?" is a ★★★ Intercom question. The setting exists but is not findable. Manual bulk reminder and automatic reminder are two separate flows — users don't know both exist.

---

## W09 — Send a bulk email to a class

**"I need to tell all Monday clients that parking is changing."**

| | |
|--|--|
| **Frequency** | Weekly |
| **Who** | Admin |
| **Entry point** | Classes → select class → Send email · OR Bookings → filter → Send email |
| **Evidence** | Zoho: Communication/73 tickets · Intercom: Notifikácie a emaily/10 convos · WhatsApp: Kate (regular use), Anna |

**Steps:**
1. Go to the class (or filter bookings by class)
2. Select all clients
3. Compose and send email

**What breaks today:** Two entry points (from Classes and from Bookings) behave slightly differently. Users don't know which to use. Email history is hard to find after sending.

---

## W10 — Handle a GoCardless issue

**"A client's payment didn't come through. GoCardless shows an error."**

| | |
|--|--|
| **Frequency** | Monthly (individual) · Every 90 days (reconnection) |
| **Who** | Admin |
| **Entry point** | Booking → Payment detail → GoCardless status |
| **Evidence** | Zoho: Payments/208 tickets (GoCardless subjects visible) · Intercom: Platby a faktúry/11 convos, GoCardless = 8 conversations = P1 critical, Nastavenia/6 convos · WhatsApp: Dom (mandate cancelled silently), Kate |

**Steps:**
1. Check payment status in the booking — see GoCardless connection status
2. If expired (happens every 90 days): click "Reconnect GoCardless" → client receives a new mandate request
3. If failed payment: retry or switch to alternative payment method

**What breaks today:** GoCardless expires silently every 90 days with no warning. Admin finds out when payments stop. The reconnect flow is not surfaced proactively. This is the single highest-repeat support topic in Intercom.

---

## W11 — Apply a discount

**"This family has two kids. They get a sibling discount."**

| | |
|--|--|
| **Frequency** | Weekly (new registrations) |
| **Who** | Admin |
| **Entry point** | Booking → Apply discount · OR Settings → Discount codes |
| **Evidence** | Zoho: Payments/208 (discount subjects present) + Settings/137 · Intercom: Platby a faktúry/11 convos, "Ako nastaviť súrodenecké zľavy?" · WhatsApp: Anna (manual per-family codes), Kate |

**Steps:**
1. Find the booking
2. Apply a discount code, or manually reduce the amount due
3. For sibling discount: create a unique code per family (current workaround)

**What breaks today:** No automated sibling discount rule. Discount codes apply to the cart total (both kids), not one child. Admin must create a unique code per family manually. This does not scale for franchises.

---

## W12 — Run term rebooking (auto-enrolment)

**"New term starts next month. I need to roll all clients over."**

| | |
|--|--|
| **Frequency** | Per term (3–4× per year) |
| **Who** | Admin |
| **Entry point** | Programmes → select programme → Copy / Auto-enrolment |
| **Evidence** | Zoho: Courses/199 tickets · Intercom: Programy a kurzy/13 convos, Objednávky/4 convos, "Ako skopírovať len potvrdené registrácie?" · WhatsApp: Anna (Michal spent 2+ hrs manually), Kate, Dom |

**Steps:**
1. Set up the new term's class structure (currently: manual)
2. Run auto-enrolment — copy confirmed registrations from current term to new term
3. Clients receive an email to confirm and pay for the new term
4. Handle non-renewals

**What breaks today:** Step 1 (new class structure) is entirely manual — requires creating all classes from scratch or using Copy, then adjusting dates and prices. Anna needed Michal to do this for her. No "copy term structure + adjust dates" wizard exists.

---

## W13 — Process a refund

**"A client cancelled. I need to give them money back."**

| | |
|--|--|
| **Frequency** | Monthly · Occasionally bulk (cancellation events) |
| **Who** | Admin |
| **Entry point** | Stripe dashboard (not Zooza) |
| **Evidence** | Zoho: Payments/208 tickets · Intercom: Platby a faktúry/11 convos · WhatsApp: Anna (100+ refunds, 1-month crisis), Kate (manual workarounds), Dom |

**Steps:**
1. Find the payment in Stripe
2. Issue a refund from Stripe
3. Manually mark the booking as refunded in Zooza (no sync)

**What breaks today:** No refund action inside Zooza. Admin must switch to Stripe. No bulk refund. Stripe Express accounts have balance limitations that cause timing issues. Zooza doesn't reflect Stripe refund status automatically.

---

## W14 — Generate and download invoices / reports

**"My accountant needs the invoices from last month."**

| | |
|--|--|
| **Frequency** | Monthly |
| **Who** | Admin |
| **Entry point** | Reports & Insights → select export type |
| **Evidence** | Zoho: Settings/137 tickets, "Ako stiahnuť faktúry XML" in subjects · Intercom: Platby a faktúry/11 convos, "Kde nájdem faktúry?" ★★★ · WhatsApp: Anna (Xero/Stripe mismatch), Dom (accountant blocked 2 weeks) |

**Steps:**
1. Go to Reports & Insights
2. Filter by date range and export type (invoices / registrations / clients / payments)
3. Download (CSV, XML, PDF depending on type)

**What breaks today:** "Kde nájdem faktúry?" is ★★★ — the section exists but users don't find it. Export columns are not labelled (Intercom: "Čo je stĺpec AU?"). Clients export vs. registrations export are in different places and produce different results — users don't know which to use.

---

## W15 — Set up a new instructor or location

**"I hired a new teacher. I need to add them to the system."**

| | |
|--|--|
| **Frequency** | Occasional |
| **Who** | Admin |
| **Entry point** | Team & Settings → Instructors · OR Team & Settings → Locations |
| **Evidence** | Zoho: Lecturers/30 tickets + Settings/137 · Intercom: Nastavenia/6 convos, "Kde nastaviť rolu pre lektorku?" · WhatsApp: Kate (invite email not received, instructor saw full admin) |

**Steps:**
1. Go to Team & Settings
2. Add instructor — name, email, invite to app (for attendance access)
3. Assign instructor to classes
4. Add location — name, address, map link

**What breaks today:** Instructors access the app via the same login as admin — no dedicated instructor mode with limited view. Teachers see the full admin interface, which is overwhelming. Instructor invite email sometimes not received (Kate's experience). Map links must be added manually in email templates (not pulled from location record automatically).

---

## Summary: frequency × support burden

| # | Workflow | Frequency | Zoho tickets | Intercom convos | WhatsApp | Automated today? |
|---|---------|-----------|-------------|----------------|---------|-----------------|
| W01 | Set up programme + class | Per term | Courses/199 | 13 | Anna, Kate, Dom | No |
| W02 | Manage a trial | Weekly | within Courses | 5 | Anna, Kate | Partial |
| W03 | Enrol client manually | Weekly | Clients/142 | 5 | Kate, Dom | No |
| W04 | Mark attendance | Daily | Calendar/52 | 13 | Anna, Kate | No |
| W05 | Cancel session + make-up | Weekly | Calendar/52 | 13 | Anna, Kate | Partial |
| W06 | Transfer client | Weekly | Clients/142 | 9 | Anna, Kate, Dom | Partial |
| W07 | Process manual payment | Daily/weekly | Payments/208 🥇 | 11 | Anna, Kate, Dom | No |
| W08 | Send payment reminder | Weekly | Settings/137 + Comm/73 | 10 | Anna | Yes (if configured) |
| W09 | Send bulk email | Weekly | Communication/73 | 10 | Kate | No |
| W10 | Handle GoCardless | Monthly/90-day | Payments/208 🥇 | 8 | Dom, Kate | No (silent expiry) |
| W11 | Apply discount | Weekly | Payments+Settings | 11 | Anna, Kate | No |
| W12 | Term rebooking | Per term | Courses/199 | 17 | Anna, Kate, Dom | Partial |
| W13 | Process refund | Monthly | Payments/208 🥇 | 11 | Anna (100+), Kate | No |
| W14 | Download invoices / reports | Monthly | Settings/137 | 11 | Anna, Dom | No |
| W15 | Set up instructor / location | Occasional | Lecturers/30 | 6 | Kate | No |

🥇 = top Zoho category (Payments/208 covers W07, W10, W11, W13 combined)

---

---

## Content mapping & coverage status

For each workflow: linked articles + coverage verdict + what's missing.

**Legend:**
- ✅ GOOD — well covered, edge cases present
- 🟡 NEEDS WORK — article exists but gaps
- 🔴 THIN — very short or missing key context
- ❌ MISSING — no article exists

---

| Workflow | Primary articles | FAQs | Status | Gap / what to fix |
|---------|-----------------|------|--------|-------------------|
| **W01** Setup programme + class | [creating-a-programme](/content/guides/creating-a-programme.md) · [creating-a-class](/content/guides/creating-a-class.md) · [programme-class-session-definition](/content/guides/programme-class-session-definition.md) · [getting-started-with-zooza](/content/setup/getting-started-with-zooza.md) | [programmes-timetables-sessions-faq](/content/faq/programmes-timetables-sessions-faq.md) | 🟡 NEEDS WORK | `programme-class-session-definition.md` is only 58 lines — no explanation of cascade behavior (what happens when you edit one layer). Most-needed addition. |
| **W02** Manage a trial | [trial-sessions](/content/setup/trial-sessions.md) · [trials-daily-business](/content/guides/trials-daily-business.md) | [trials-faq](/content/faq/trials-faq.md) | 🟡 NEEDS WORK | `trials-daily-business.md` covers steps but not *why* admin can't create trials manually, and doesn't explain the two-step "trial lost" reschedule clearly. |
| **W03** Enrol client manually | [creating-a-booking](/content/guides/creating-a-booking.md) · [types-of-bookings](/content/guides/types-of-bookings.md) · [business-booking](/content/guides/business-booking.md) | [registration-and-booking-faq](/content/faq/registration-and-booking-faq.md) | 🟡 NEEDS WORK | No clear article explaining "when should admin enrol vs. send client a booking link?" — the paradigm shift article. |
| **W04** Mark attendance | [admin-attendance-management](/content/guides/admin-attendance-management.md) · [instructor-attendance-management](/content/guides/instructor-attendance-management.md) · [zooza-101-instructors](/content/guides/zooza-101-instructors.md) | [attendance-and-catchups-faq](/content/faq/attendance-and-catchups-faq.md) | ✅ GOOD | No dedicated "quick guide for instructors on phone" — the existing article covers desktop flow well. |
| **W05** Cancel session + make-up | [custom-replacement-lessons](/content/guides/custom-replacement-lessons.md) · [replacement-hours-complete](/content/guides/replacement-hours-complete.md) · [calendar-bulk-actions](/content/guides/calendar-bulk-actions.md) | [make-up-sessions-faq](/content/faq/make-up-sessions-faq.md) · [attendance-and-catchups-faq](/content/faq/attendance-and-catchups-faq.md) | ✅ GOOD | Scope selector (this session vs. all) not explained. Make-up report by location is missing (Intercom P1). |
| **W06** Transfer client | [transfer-and-copy-bookings](/content/guides/transfer-and-copy-bookings.md) · [bulk-network-transfer](/content/guides/bulk-network-transfer.md) | [transfer-and-copy-faq](/content/faq/transfer-and-copy-faq.md) | ✅ GOOD | What happens to payment balance after transfer is not explicitly addressed. |
| **W07** Process manual payment | [inbound-payments](/content/guides/inbound-payments.md) · [edit-payment-on-booking](/content/guides/edit-payment-on-booking.md) · [outstanding-amount](/content/guides/outstanding-amount.md) · [payment-correction-vs-refund](/content/guides/payment-correction-vs-refund.md) | [payments-and-billing-faq](/content/faq/payments-and-billing-faq.md) | ✅ GOOD | Payment status UI readability is a product gap, not a docs gap. Articles are solid. |
| **W08** Send payment reminder | [automatic-payment-reminders](/content/guides/automatic-payment-reminders.md) · [automatic-payment-reminders-detailed](/content/guides/automatic-payment-reminders-detailed.md) | [payments-and-billing-faq](/content/faq/payments-and-billing-faq.md) | ✅ GOOD | Discoverability issue (users can't find the setting) — docs exist, nav is the problem. |
| **W09** Send bulk email | [sending-email-sms](/content/guides/sending-email-sms.md) · [bulk-email-send-tracking](/content/guides/bulk-email-send-tracking.md) · [dynamic-tags](/content/guides/dynamic-tags.md) | [email-communication-faq](/content/faq/email-communication-faq.md) | ✅ GOOD | — |
| **W10** Handle GoCardless | [gocardless-connection-lifecycle](/content/guides/gocardless-connection-lifecycle.md) · [gocardless-direct-debit-mandates](/content/guides/gocardless-direct-debit-mandates.md) · [payment-pairing](/content/guides/payment-pairing.md) | [gocardless-faq](/content/faq/gocardless-faq.md) | ✅ GOOD | GoCardless lifecycle article covers silent expiry well. In-app proactive warning is a product gap, docs can't fix it. |
| **W11** Apply discount | [discount-code](/content/guides/discount-code.md) · [discount-types](/content/guides/discount-types.md) · [loyalty-sibling-discount](/content/guides/loyalty-sibling-discount.md) | [discounts-and-sibling-pricing-faq](/content/faq/discounts-and-sibling-pricing-faq.md) | ✅ GOOD | No automated sibling discount rule — product gap. The manual workaround is documented. |
| **W12** Term rebooking | [new-programme-existing-clients](/content/guides/new-programme-existing-clients.md) · [copy-programme-and-class](/content/guides/copy-programme-and-class.md) · [auto-enrolment-responses](/content/guides/auto-enrolment-responses.md) | — | 🟡 NEEDS WORK | Coverage is fragmented across 3+ articles. No single end-to-end "run your term reset" guide. Users get lost between articles. |
| **W13** Process refund | [recording-an-administrative-refund](/content/guides/recording-an-administrative-refund.md) · [payment-correction-vs-refund](/content/guides/payment-correction-vs-refund.md) | [administrative-refund-faq](/content/faq/administrative-refund-faq.md) · [stripe-payments-faq](/content/faq/stripe-payments-faq.md) | 🟡 NEEDS WORK | Admin refund is well covered. Stripe refund flow (how to go to Stripe, what to click, what to do in Zooza after) is likely thin. |
| **W14** Download invoices / reports | [billing-and-invoicing](/content/setup/billing-and-invoicing.md) · [invoicing-overview](/content/setup/invoicing-overview.md) · [documents](/content/guides/documents.md) | — | 🟡 NEEDS WORK | Articles exist but "Kde nájdem faktúry?" is ★★★ in Intercom — navigation discoverability, not content gap. Consider adding a "where to find X in Zooza" reference page. |
| **W15** Setup instructor / location | [creating-a-location](/content/setup/creating-a-location.md) · [user-roles](/content/guides/user-roles.md) · [zooza-101-instructors](/content/guides/zooza-101-instructors.md) | [instructor-access-faq](/content/faq/instructor-access-faq.md) · [roles-and-permissions-faq](/content/faq/roles-and-permissions-faq.md) | ✅ GOOD | No dedicated article for "what instructors see vs. what admins see" — instructor limited view not described. |

---

## Priority content fixes (before franchise pitch)

| Priority | Fix | Article to update or create |
|----------|-----|----------------------------|
| 🔴 P1 | Expand cascade behavior explanation | Update `programme-class-session-definition.md` — add "what editing each layer affects" section |
| 🔴 P1 | End-to-end term rebooking guide | Create `term-rebooking-guide.md` — merge W12 fragments into one flow |
| 🟠 P2 | Trials: manual creation & trial lost reschedule | Update `trials-daily-business.md` — add "admin can't create manually" box + reschedule decision tree |
| 🟠 P2 | Paradigm shift article | Create `admin-vs-self-service.md` — "when to enrol clients yourself vs. send them a link" |
| 🟠 P2 | Stripe refund step-by-step | Update or create — "how to issue a refund via Stripe and what to do in Zooza after" |
| 🟡 P3 | "Where to find X" reference page | Create `where-to-find.md` — quick navigation guide (invoices, reminders, GoCardless, booking link) |
| 🟡 P3 | Instructor mobile quick guide | Create `instructor-quick-start.md` — attendance on phone, what instructors see |

---

## Onboarding sequence

Recommended learning path for a new franchisee — week by week.

### Before go-live (Week 1)

These must be done before any client touches the system:

1. **W15** — Add locations and instructors → [creating-a-location](/content/setup/creating-a-location.md) · [user-roles](/content/guides/user-roles.md)
2. **W01** — Set up first programme and class → [getting-started-with-zooza](/content/setup/getting-started-with-zooza.md) · [creating-a-programme](/content/guides/creating-a-programme.md) · [creating-a-class](/content/guides/creating-a-class.md)
3. **Payment gateway** — Connect Stripe or GoCardless → [inbound-payments-setup](/content/setup/inbound-payments-setup.md)
4. **W02** — Understand how trials work before first client books → [trial-sessions](/content/setup/trial-sessions.md)
5. **Test** — Walk through the booking flow as a client before sharing the link → [getting-started-with-zooza](/content/setup/getting-started-with-zooza.md)

### First clients (Week 1–2)

6. **W03** — Enrol first client manually or share booking link → [creating-a-booking](/content/guides/creating-a-booking.md)
7. **W04** — Mark attendance in first class → [admin-attendance-management](/content/guides/admin-attendance-management.md) · [instructor-attendance-management](/content/guides/instructor-attendance-management.md)
8. **W07** — Record first payment → [inbound-payments](/content/guides/inbound-payments.md)

### Month 1 — Core operations

9. **W05** — Cancel a session and offer make-up → [custom-replacement-lessons](/content/guides/custom-replacement-lessons.md)
10. **W08** — Set up automatic payment reminders → [automatic-payment-reminders](/content/guides/automatic-payment-reminders.md)
11. **W09** — Send first bulk email to a class → [sending-email-sms](/content/guides/sending-email-sms.md)
12. **W06** — Transfer a client to a different class → [transfer-and-copy-bookings](/content/guides/transfer-and-copy-bookings.md)

### Month 2–3 — Advanced operations

13. **W11** — Set up discounts (sibling, loyalty) → [loyalty-sibling-discount](/content/guides/loyalty-sibling-discount.md) · [discount-code](/content/guides/discount-code.md)
14. **W10** — Understand GoCardless lifecycle before first 90-day expiry → [gocardless-connection-lifecycle](/content/guides/gocardless-connection-lifecycle.md)
15. **W13** — Process first refund → [recording-an-administrative-refund](/content/guides/recording-an-administrative-refund.md)
16. **W14** — Generate monthly report for accountant → [invoicing-overview](/content/setup/invoicing-overview.md)

### Term end

17. **W12** — Run term rebooking for all clients → [new-programme-existing-clients](/content/guides/new-programme-existing-clients.md) · [copy-programme-and-class](/content/guides/copy-programme-and-class.md)

---

## Implications

**Most broken at highest frequency:** W04 (attendance — daily), W07 (manual payment — daily/weekly), W10 (GoCardless — silent monthly failure).

**Biggest franchise scalability blockers:** W01 (setup complexity), W12 (term rebooking = manual), W13 (refunds = no Zooza UI).

**Fixable through UX without new features:** W03 (better entry point), W04 (instructor view), W07 (payment status clarity), W08 (reminder settings discoverability), W14 (invoices discoverability).

**Requires product work:** W10 (GoCardless proactive warning), W11 (sibling discount rule), W12 (term wizard), W13 (refund UI).

---

*Source: Intercom analysis April 2026 + WhatsApp conversations Anna/Kate/Dom + KB content audit*  
*Compiled: 10 May 2026*
