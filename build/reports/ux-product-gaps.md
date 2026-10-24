# UX & Product Gaps — Franchise Readiness

**Date:** 10 May 2026
**Context:** Based on 160-day Turtle Tots onboarding analysis + franchise acquisition goal.

---

## The paradigm shift nobody explains

Zooza works fundamentally differently from manual tools and legacy systems like Thinksmart:

| Old way (Thinksmart / manual) | Zooza way |
|-------------------------------|-----------|
| Admin does things *for* clients | Admin sets rules, system executes |
| Admin sends rebooking emails manually | System sends automated notifications |
| Admin creates trials for walk-ins | Clients book trials themselves via portal |
| Admin tracks sibling discounts per-person | Discount rules apply automatically |
| Admin adjusts payment when class is cancelled | Compensation rules trigger automatically |

**This shift is never communicated during onboarding.**  
New operators don't trust the automation — so they try to do things manually — which breaks the automation — which confirms their distrust.

Breaking this loop is as important as fixing individual product gaps.

---

## Gap map

### How to read this

- **Frequency:** daily / weekly / per-term / once (migration/setup)
- **Blocked:** who can't do their job (Admin / Instructor / Client / Head Office)
- **Type:** what kind of fix is needed
  - `Product` — requires engineering
  - `UX` — interaction/flow redesign, no new functionality needed
  - `Content` — help docs, in-app guidance, onboarding material
  - `Paradigm` — user needs to understand the rule-based model, not just how to click
- **Franchise blocker:** is this a dealbreaker for pitching a large franchise? `Critical / High / Medium / Low`

---

## Priority 1 — Franchise dealbreakers

These gaps mean a franchise with 50 locations cannot operate Zooza without a dedicated support person at Zooza HQ.

---

### G1 — Term rebooking: no bulk copy-to-next-term

| | |
|--|--|
| **Frequency** | Per term (3–4× per year) |
| **Blocked** | Admin |
| **Type** | Product |
| **Franchise blocker** | Critical |

**What happens now:** Michal manually copies all classes, then adjusts 100+ booking prices individually. Anna cannot do this independently.

**What's needed:** "Start new term" wizard — select source term, copy structure + pricing, apply price adjustment rules, preview, confirm. Bulk email notification to all affected clients.

**Paradigm note:** This is the clearest example of Thinksmart's "one button job" vs. Zooza's multi-layer manual process. For a franchise with 50 locations doing 3 resets/year = 150 manual operations where Michal is the bottleneck.

---

### G2 — Refunds: no bulk flow, Stripe Express limitations

| | |
|--|--|
| **Frequency** | Monthly (individual), occasionally bulk (cancellations) |
| **Blocked** | Admin |
| **Type** | Product |
| **Franchise blocker** | Critical |

**What happens now:** Admin goes to Stripe, issues refunds one by one. Express accounts can't hold negative balance → timing issues → double payments. No Zooza-native refund UI.

**What's needed:**
1. Refund action inside Zooza booking view (triggers Stripe behind the scenes)
2. Bulk refund: select bookings → apply refund reason → execute
3. Clear guidance on Express vs. Standard account tradeoffs at setup

**Paradigm note:** Clients expect money back via the platform. When it fails, they blame the franchisee, not Stripe.

---

### G3 — Programme / Timetable / Sessions: three layers, no clear contract

| | |
|--|--|
| **Frequency** | Daily (any structural change) |
| **Blocked** | Admin |
| **Type** | UX + Content |
| **Franchise blocker** | Critical |

**What happens now:** Admin edits in one layer, change doesn't propagate. Same data (instructor, time, price) editable from 3+ places with different cascading behaviour. Admin doesn't know which layer to use.

**What's needed:**
1. Clear visual hierarchy in the UI: Programme (template) → Class (schedule) → Session (occurrence)
2. Explicit propagation prompts: "You changed the instructor at Programme level. Apply to all future sessions? [Yes / No / Choose]"
3. Onboarding concept page: "Understanding Zooza structure" — before the user touches anything

**Paradigm note:** This is the deepest mental model mismatch. Operators think in terms of "a class" — Zooza has three different things that look like "a class". Until this is named and explained, everything else is confusing.

---

### G4 — Migration: no structured process for term-based, monthly, or PAYG clients

| | |
|--|--|
| **Frequency** | Once (but once = the whole deal) |
| **Blocked** | Admin + Head Office |
| **Type** | Content + Product |
| **Franchise blocker** | Critical |

**What happens now:** Migration is a 100-day WhatsApp thread. No documented process. No tooling. Every migration is bespoke.

**What's needed:**
1. Migration playbook document (per client type: term / monthly / PAYG)
2. Client import tool with balance carry-over
3. Decision tree: "When to go live" — don't launch until these 8 things are set up
4. Dedicated pre-launch checklist that Admin completes *before* any client touches the system

**Paradigm note:** The migration window is when trust is established or destroyed. A structured, predictable migration process is itself a sales argument.

---

## Priority 2 — Daily operation blockers

These don't kill the franchise deal but will cause ongoing churn and reliance on support.

---

### G5 — Attendance register: too slow for in-class use

| | |
|--|--|
| **Frequency** | Daily (every class) |
| **Blocked** | Instructor |
| **Type** | UX + Product |
| **Franchise blocker** | High |

**What happens now:** Register requires scrolling, class-switching is slow. Instructors have ~60 seconds between classes. Result: attendance marked after class, data unreliable.

**What's needed:** Dedicated instructor attendance view — full-screen, large tap targets, one class visible at a time, swipe to next class. Offline-capable. No login friction.

**Paradigm note:** Instructors are not admins. They need a tool, not a system. A separate instructor interface (or mode) would make this clear.

---

### G6 — Payment status: unreadable without system knowledge

| | |
|--|--|
| **Frequency** | Daily |
| **Blocked** | Admin |
| **Type** | UX |
| **Franchise blocker** | High |

**What happens now:** Balance field shows "-1155 AED". This requires knowing that "-" means overpaid or pending, not owed. Booking + Transactions + Balance must be read together. Non-expert users cannot interpret this.

**What's needed:** Single, plain-language payment status per booking:
- ✅ Paid — AED 1,155 received on 3 Jan
- ⏳ Awaiting payment — AED 1,155 due
- 🔴 Overdue — AED 577 since 15 Dec
- 💚 Overpaid — AED 115 credit on account

**Paradigm note:** This is a trust issue. Operators need to be able to answer "has this client paid?" in 2 seconds, not reconstruct a ledger.

---

### G7 — Capacity and "class full" experience

| | |
|--|--|
| **Frequency** | Daily (booking flow) |
| **Blocked** | Client (self-service) |
| **Type** | UX + Product |
| **Franchise blocker** | High |

**What happens now:** Enrolled clients see "class full" when trying to complete payment (because trials count toward capacity). Clients contact admin in panic. Admin contacts Michal.

**What's needed:**
1. "Class full" message must differentiate: "No new spots available" vs. "You're already enrolled — go to Parent Portal to manage your booking"
2. Clear capacity display for admin: spots used / total, broken down by confirmed / trial / reserved
3. Catch-up availability: document the 4-day rule prominently, or make it configurable

**Paradigm note:** Clients in Zooza are expected to use the Parent Portal. This is never communicated to them at enrolment. They don't know it exists.

---

### G8 — Trial management: admin cannot create or reschedule manually

| | |
|--|--|
| **Frequency** | Weekly |
| **Blocked** | Admin |
| **Type** | Product |
| **Franchise blocker** | High |

**What happens now:** Trials can only be initiated by clients online. Admin cannot create a trial for a walk-in or phone enquiry. Rescheduling "trial lost" requires a multi-step workaround through Attendance → Book session → change status.

**What's needed:**
1. Admin ability to create a trial booking for a client
2. One-click trial reschedule from the booking view
3. Clear status flow: Trial booked → Trial attended / Trial lost → Enrolled / Not enrolled

**Paradigm note:** In rule-based Zooza, trials are automated. But real-world businesses have walk-ins and phone calls. Admin needs an override without breaking the automation.

---

### G9 — Sibling discount: no automated rule

| | |
|--|--|
| **Frequency** | Weekly (new registrations) |
| **Blocked** | Admin |
| **Type** | Product |
| **Franchise blocker** | Medium |

**What happens now:** No sibling discount rule exists. Workaround: unique 7.5% discount code per parent (to avoid 15% applying to both kids in one cart). Manual, error-prone, doesn't scale.

**What's needed:** Discount rule: "Apply X% to lowest-priced booking when same account has 2+ bookings." Configurable per programme or globally.

---

### G10 — Instructor assignments: changes don't cascade

| | |
|--|--|
| **Frequency** | Weekly |
| **Blocked** | Admin |
| **Type** | UX + Product |
| **Franchise blocker** | Medium |

**What happens now:** Instructor changed in Sessions view doesn't update Timetable. Changed in Timetable doesn't propagate to past sessions. No clear indication of where the "source of truth" is.

**What's needed:** Instructor edit with explicit scope selector: "Change for this session only / all future sessions / all sessions in this class."

---

## Priority 3 — Accounting & reporting

These are not daily issues but become blockers at month-end or during audits.

---

### G11 — Stripe Express: VAT invoices not available

| | |
|--|--|
| **Frequency** | Monthly (accounting) |
| **Blocked** | Admin + Accountant |
| **Type** | Product + Process |
| **Franchise blocker** | High (for VAT-registered businesses) |

**What happens now:** Stripe Express accounts don't provide processing fee invoices. Accountant needs these for VAT returns. 2-week blocker for Turtle Tots.

**What's needed:**
1. Pre-sales checklist: "Are you VAT registered? → You need Stripe Standard, not Express."
2. Or: Zooza generates a fee summary export that satisfies most accountants.

---

### G12 — Xero integration: invoice date = payment date, not booking date

| | |
|--|--|
| **Frequency** | Monthly |
| **Blocked** | Accountant |
| **Type** | Product |
| **Franchise blocker** | Medium |

**What happens now:** Invoices generated with booking creation date. Accountant needs payment received date for accrual accounting. Required manual regeneration of ~250 invoices.

**What's needed:** Invoice date = payment date (configurable or default). This is a standard accounting requirement.

---

## Summary: what needs to ship before franchise pitch

| # | Gap | Type | Must-have for pitch |
|---|-----|------|-------------------|
| G1 | Term rebooking wizard | Product | ✅ Yes |
| G2 | Zooza-native refund UI + bulk | Product | ✅ Yes |
| G3 | Programme/Class/Session UX clarity | UX + Content | ✅ Yes |
| G4 | Migration playbook + pre-launch checklist | Content | ✅ Yes |
| G5 | Instructor attendance view | UX | ✅ Yes |
| G6 | Readable payment status | UX | ✅ Yes |
| G7 | "Class full" UX + capacity display | UX | ✅ Yes |
| G8 | Admin trial creation + reschedule | Product | Should have |
| G9 | Sibling discount rule | Product | Should have |
| G10 | Instructor cascade edit | UX | Nice to have |
| G11 | Stripe Express VAT invoice solution | Product/Process | ✅ Yes (VAT markets) |
| G12 | Xero invoice date fix | Product | Nice to have |

---

## What can be done without engineering

Several gaps are fixable through content and UX copy alone — no product changes needed:

- **G3 (partial):** "Understanding Zooza structure" guide — Programme vs. Class vs. Session explained before first use
- **G4 (partial):** Migration playbook, pre-launch checklist
- **G6 (partial):** In-app tooltip explaining what the balance field means
- **G7 (partial):** Better error message copy on "class full"
- **G7 (partial):** Document the 4-day catch-up rule prominently
- **Paradigm shift:** One-page "How Zooza is different" — the rule-based model, what automation exists, what clients are expected to do themselves

These should ship first because they're fast and reduce support load immediately.

---

*Source: Anna/Turtle Tots WhatsApp analysis + franchise readiness framing, 10 May 2026*
