# Onboarding Findings — Turtle Tots Dubai (Anna)

**Period:** 3 Dec 2025 – 11 May 2026 (160 days)
**Context:** Migration from Thinksmart. ~250 customers, multiple venues, 2 franchise sub-accounts (Standard + Express).
**Source:** WhatsApp support chat (~1 000+ messages), analysed 10 May 2026.

---

## The core finding

After 160 days of live operation, Anna still cannot run Zooza independently.
She knows the product exists — she just doesn't know where things live or why they work the way they do.

> *"I should be able to do this all myself by now but it is not intuitive... The main problem is that I have to rely on you to do everything."*
> — Anna, 4 May 2026

> *"I'm not a stupid person but honestly Zooza makes me feel like I am!!"*
> — Anna, 27 Jan 2026

This is not a user capability problem. It is a product onboarding problem.

---

## What Anna was trying to do

Standard franchise operator tasks — the things she needs to do every week:

- Set up programmes, classes, sessions, instructors, venues
- Manage bookings and capacity
- Run attendance registers during class
- Handle trials → enrolment flow
- Apply sibling discounts
- Process refunds and adjustments
- Reset terms (rebooking)
- Report to her accountant (Xero + Stripe)

None of these are exotic. They are the baseline daily workflow.

---

## Where she got stuck — by workflow

### 1. Programme / Class / Session structure

**The problem:** Zooza has three editing layers (Programme → Timetable → Sessions) that look similar but behave independently. Changes in one don't cascade as expected.

**What Anna experienced:**
- Instructor updated in Sessions, not reflected in Timetable
- Price not inherited when adding a session to a programme
- Class time editable from Calendar *or* Timetable *or* Sessions detail — different behaviour in each
- "There are so many versions of nearly the same option and several places where you can edit things"

**What Thinksmart did:** Edit once, applies everywhere.

**Impact:** Every structural change requires knowing which layer to use. Anna learned this through trial and error, live, with 250 customers.

---

### 2. Capacity and "class full"

**The problem:** Trial bookings count toward class capacity. When a class is "full" (trials included), the booking flow shows "class full" — even to customers who are already enrolled and trying to complete payment.

**What Anna experienced:**
- 12 Jan: *"Nearly everyone this weekend who enrolled in trial is now not able to book directly as it says full but they are one of the class count... it is really hard to keep track of"*
- Multiple customers contacted Anna saying they couldn't book — she had to investigate each one manually
- Catch-up classes: invisible to customers until 4 days before class (protects new enrolment, but undocumented)

**Impact:** ~50+ customer support messages about booking failures. Anna spent significant time debugging each one.

---

### 3. Refunds

**The problem:** No bulk refund flow in Zooza. Refunds go through Stripe. Stripe Express accounts can't hold a negative balance — pending refunds auto-release when balance becomes positive, causing timing issues.

**What Anna experienced:**
- April 30: 100+ customers needed refunds after cancellations
- Stripe Express had no balance → refunds queued → auto-released at wrong time → some customers received double payments
- *"I have over 100 customers who will need refunds and to do it manually by bank transfer is just not an option"*
- *"I feel like I am losing the respect of my customers — they think my business cannot afford to pay them back"*

**Impact:** 1-month refund crisis. Customer trust damaged. Required Michal's direct intervention.

---

### 4. Term rebooking

**The problem:** No bulk copy-all-to-next-term function. Every term reset requires manual class setup + manual price adjustments + Michal's involvement.

**What Anna experienced:**
- March 2026: Michal spent 2+ hours manually copying all classes for the summer term
- Separately adjusted 100+ booking prices for different venue pricing tiers
- *"On the old software it is a one button job"*

**Impact:** Anna cannot run a term reset independently. Blocks franchise scalability.

---

### 5. Attendance register

**The problem:** The attendance register requires significant scrolling, especially on phone. Instructors have ~1 minute between classes.

**What Anna experienced:**
- *"Our old booking software had a very quick tick list with all names together in a small list... it was much easier"*
- Teachers do attendance after class instead of during — accuracy suffers
- Michal committed to simplify by early March 2026; not delivered by 11 Mar

**Impact:** Instructors not using the register during class. Attendance data unreliable.

---

### 6. Sibling discounts

**The problem:** No automated sibling discount rule. Workaround: per-parent discount codes at 7.5% (instead of 15%) to avoid double-application on two-child carts.

**What Anna experienced:**
- Dec 12: *"If they sign up two kids then they will get 15% on both children... but it's only meant to be on one"*
- Required unique discount code created per parent
- Multiple incorrect charges resolved manually

**Impact:** Every new family with siblings = manual intervention.

---

### 7. Payment status UI

**The problem:** Balance field shows raw figures like "-1155 AED" without explanation. Booking + Transactions + Balance must be read together to understand payment state.

**What Anna experienced:**
- Jan 27: *"I'm not a stupid person but honestly Zooza makes me feel like I am!! ... the split of booking + transactions + balance..."*
- Michal acknowledged the UI is confusing and flagged it to the team

**Impact:** Anna cannot confidently read a customer's payment status. Every ambiguous case goes to Michal.

---

### 8. Trial management

**The problem:** Trials cannot be created manually by admin — only customers can book them online. Rescheduling a "trial lost" requires a multi-step workaround (Attendance → Book session → change status back).

**What Anna experienced:**
- Jan 31: *"It said trial lost for some reason... I tried to mark it as trial not started... then it tried to enrol the customer fully... I don't know how to do it"*
- Admin cannot manually create a trial for walk-in customers

**Impact:** Trial management is Michal-dependent. Anna cannot handle trial edge cases independently.

---

## Mental model mismatch (Thinksmart vs. Zooza)

| User expectation | Zooza reality |
|-----------------|---------------|
| Edit once → applies everywhere | Three layers, partial independence |
| One-button term rebooking | Manual class + price setup each term |
| Payment is: amount owed / amount paid | Booking + Transactions + Balance = one story |
| Refund = click refund | Stripe flow, no bulk option |
| Trial = admin creates it | Trial = customer self-books online only |
| Discount = % off second child | Discount code on cart total, manual per-parent |

---

## Emotional trajectory

| Phase | Signal |
|-------|--------|
| **Day 1** | *"I cannot launch with this... I have 250 customers and this could all turn very messy"* |
| **Day 55** | *"I'm not a stupid person but honestly Zooza makes me feel like I am!!"* |
| **Day 57** | *"I'm sorry I'm thinking this software might be too much for me and my customers!"* |
| **Day 59** | *"I'm sorry for complaining and I'm sure it's my fault"* |
| **Day 90** | *"I think I just need to get used to how it works"* (resignation) |
| **Day 152** | *"I really feel that you need to simplify the front end for the business owner"* |

The arc: panic → self-doubt → resignation → still dependent.

---

## What this means for franchise acquisition

A large international franchise with 50–100 franchisees will face Anna's problems multiplied across every location, with no Michal available for each one.

The current support model does not scale. The product needs to get the operator to independence, not just to "working with help".

**The bar for franchise readiness:**
1. Operator can run a term reset without Michal
2. Operator can handle refunds without Stripe intervention
3. Instructor can mark attendance in 60 seconds during class
4. Operator can read payment status without calling support
5. Migration can be explained in a document, not in a 100-day WhatsApp thread

None of these are currently true.

---

*Source: WhatsApp Chat — Turtle Tots Dubai × Zooza, analysed 10 May 2026*
*Analysis by Claude Code / Michal Dodok*
