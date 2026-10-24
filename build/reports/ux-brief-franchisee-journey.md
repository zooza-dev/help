# UX Brief — Franchisee First-Day Journey

**Date:** 10 May 2026
**Scope:** In-app UX improvements — no new features required unless noted.
**Goal:** A franchisee understands how Zooza works *by using it*, not by reading docs or asking support.
**Baseline evidence:** 3 WhatsApp onboarding conversations (Turtle Tots, babyballet Dubai, Wee Kicks), 160–270 days each.

---

## The one principle this brief is built on

> Understanding must come from using the app, not from reading documentation.

Every UX fix below follows this: the app explains itself at the moment the user needs it, in context, in the right words.

---

## The mental model Zooza needs to install

Before a franchisee touches anything, they need one mental model in their head:

```
PROGRAMME          ← the rules (what is this class, how it's paid, who it's for)
  └── CLASS        ← the schedule (when does it run, where, who teaches)
        └── SESSION  ← the occurrence (one specific date, attendance, cancellation)
```

And one paradigm shift:

> "You set the rules. The system runs them. Clients manage themselves."

Neither of these is currently communicated anywhere in the app.

---

## Journey map: Day 1 to first client booked

---

### Moment 1 — First login: empty account

**What they see now:**  
Dashboard. Probably empty or near-empty. No obvious start point.

**Problem:**  
No "what to do first" signal. Users click around randomly. Anna clicked into Classes before creating a Programme.

**Fix — Empty state onboarding checklist:**  
When the account has zero programmes, show a persistent setup checklist in the dashboard:

```
Getting started with Zooza

□ 1. Create your first programme
□ 2. Add a class with sessions
□ 3. Set up your payment method (Stripe / GoCardless)
□ 4. Check your booking page
□ 5. Share your booking link with your first clients

Each step unlocks the next.
```

Each item is clickable and takes them to the right place. The checklist stays visible (dismissible) until all 5 are done.

**Type:** Empty state / new component  
**Size:** Medium

---

### Moment 2 — Navigation: three equal siblings

**What they see now:**  
Left nav shows:
```
Activities
  > Programmes
  > Classes
  > Sessions
  > Calendar
```

**Problem:**  
Programmes, Classes, Sessions appear as flat equals. A new user has no idea these are nested. The first instinct is to click "Classes" (feels like the main thing). But Classes require a Programme first — they land in an empty list with no explanation.

This is the single most disorienting moment in the first 10 minutes.

**Fix — Reflect hierarchy in the nav:**

Option A (minimal change): Indent Classes and Sessions visually under Programmes:
```
Activities
  > Programmes
      Classes
      Sessions
  > Calendar
```

Option B (better): Collapse Classes and Sessions out of the top-level nav. Access them *through* Programmes (drill-down). Top nav only shows:
```
Activities
  > Programmes
  > Calendar
```
When inside a Programme: tabs for Classes → Sessions.

Option B matches the mental model. Option A is a lighter change with meaningful impact.

**Type:** Navigation restructure  
**Size:** Option A = Small. Option B = Medium.

---

### Moment 3 — Creating a Programme: what am I setting up?

**What they see now:**  
A form with:
- Programme type: "One-off event" / "Booking for the full programme duration" / "Pay-as-you-go"
- Target audience
- How do you want to collect payments? "One payment" / "In scheduled payments"
- Booking fee
- Total price

**Problems:**
1. "Booking for the full programme duration" — what does that mean? Is this monthly? Per term?
2. Payment method is asked before the user understands what they're setting up
3. "Total price" at Programme level — does this cascade to Classes? Unknown.
4. No explanation of what a Programme *is* in context

**Fix 1 — Rename payment types with plain language + example:**

| Current label | Proposed label | Sub-label |
|--------------|----------------|-----------|
| One-off event | Single event | A workshop, trial day, or one-time class |
| Booking for the full programme duration | Term / block booking | Clients pay once for the whole period |
| Pay-as-you-go | Drop-in / session-by-session | Clients book and pay per session |

**Fix 2 — Add a one-line context note at the top of the form:**
> "A programme is a container for your classes. It sets the rules — payment model, who it's for, whether trials are allowed. You'll add specific class schedules inside it."

**Fix 3 — "Total price" field label:**  
Change to: `"Total price charged to clients"` with sub-label: `"This is a reference price. You'll confirm the price when you add each class."`

**Type:** Label changes + contextual copy  
**Size:** Small

---

### Moment 4 — Creating a Class: where am I in the hierarchy?

**What they see now:**  
Form title: `ADD A NEW CLASS`  
No indication of which Programme this class belongs to.

**Problem:**  
The user is inside a Programme, creating a class — but the form gives no confirmation of this. After a few classes, users lose track of which class belongs to which programme. Anna regularly couldn't find the right class to edit.

**Fix 1 — Add a breadcrumb above the form:**
```
Programmes > Turtle Tots (5–7 yrs) > Add a new class
```

**Fix 2 — Price field context:**  
Current: `"Total price: 10,00€, Registration fee (optional): 0,00€"`  
This appears at the bottom of the form with no explanation.

Change to:  
```
Price for this class

Class fee      [___]    What clients pay to join this class for its full duration
Registration fee [___]  Optional one-time fee charged when they first sign up (separate from class fee)
Billable sessions [___] Leave empty to charge for all sessions. Set a number to limit billing to fewer sessions than scheduled.
```

**Fix 3 — "Sessions to create: 1" counter:**  
This counter updates live as the user sets dates. It's useful but tiny and unlabelled.  
Change to: `"This will create [N] sessions"` — larger, in plain English, above the Create button.

**Type:** Breadcrumb (small) + label changes (small)  
**Size:** Small–Medium

---

### Moment 5 — Changing an instructor: which scope?

**What they see now:**  
Instructor panel on a class or session:
```
INSTRUCTORS
Main: Reed Jasmine    Instructor's Rate: Not Set    Additional Instructors: Not Set
[Edit]
```

**Problem:**  
After clicking Edit and saving, users don't know if this change applied to:
- This session only
- All upcoming sessions in this class
- All classes in this programme

Anna spent weeks confused about why instructor changes didn't persist. The edit form gives no scope selector.

**Fix — Add scope selector to the instructor edit form:**

```
Change instructor for:
  ○ This session only  (3 March 2026)
  ● All upcoming sessions in this class
  ○ All sessions including past ones
```

Default: "All upcoming sessions in this class" (covers 90% of use cases).

Same pattern should apply to: time changes, cancellations, price changes at class level.

This one fix resolves the single most common confusion in the codebase.

**Type:** New UI component in existing form  
**Size:** Medium

---

### Moment 6 — Classes list: the word "Groups"

**What they see now:**  
Page title: `Groups \`  
Nav label: `Classes`

Two different words for the same thing.

**Problem:**  
Every user has to learn that "Groups" = "Classes" in Zooza. Kate asked about this. Dom asked about this. It adds cognitive load to every interaction.

**Fix:**  
Pick one word. Use it everywhere. Recommendation: **Classes** (matches user's mental model, matches the nav).

If "Groups" is the internal technical term, keep it in the DB — but never show it to the admin user.

**Type:** Terminology consistency  
**Size:** Small (label changes across the app)

---

### Moment 7 — Classes list: financial columns nobody understands

**What they see now:**  
Class list columns: `Paid Debt | Issued Debt | Balance`

These are three numbers. A new user reads them as:
- Paid Debt = money already paid? Or debt that's been paid off?
- Issued Debt = total debt issued? Or invoices sent?
- Balance = what's left?

**Problem:**  
The terminology is accounting-internal. "Debt" has a negative connotation in everyday language. "Issued debt" means nothing to a non-accountant.

**Fix — Rename columns:**

| Current | Proposed | Meaning |
|---------|----------|---------|
| Issued Debt | Total charged | Total amount clients have been billed |
| Paid Debt | Collected | Amount actually paid |
| Balance | Outstanding | Amount still owed |

Or as a single status badge per client row instead of three numbers (see Moment 8).

**Type:** Label change  
**Size:** Small

---

### Moment 8 — Payment status: "-£1,468.00 Outstanding"

**What they see now:**  
In the attendance/session view for a client:
```
PAYMENT
⚠ Outstanding
-£1,468.00
[Add payment]
```

**Problem:**  
"-£1,468.00" reads as a negative number — which most people interpret as "they overpaid" or "there's credit". But "Outstanding" says they owe money. The minus sign is confusing in this context.

From Anna: *"I'm not a stupid person but honestly Zooza makes me feel like I am!!"* — directly about this screen.

**Fix — Replace raw numbers with a human-readable status badge:**

```
💰 £1,468 due      [Add payment]      Last payment: —
```

Or for a paid client:
```
✅ Paid            [View payments]    Last payment: £230 on 3 Jan
```

Or for an overpaid client:
```
💚 £115 credit on account             Last payment: £345 on 15 Feb
```

The rule: a non-accountant should be able to answer "has this client paid?" in under 3 seconds.

Keep the detailed ledger accessible (expand or separate tab) — but the headline is always plain English.

**Type:** Status component redesign  
**Size:** Medium

---

### Moment 9 — Capacity: "class full" that isn't

**What they see now:**  
When a class is at capacity, clients (and enrolled parents completing payment) see:  
`"Class full"`

**Problem:**  
Enrolled clients who haven't yet paid see "class full" when they try to complete their payment. They think they've lost their spot. They panic. They contact the franchisee. The franchisee contacts Michal.

This happens because trial bookings hold capacity spots — an invisible system behaviour.

**Fix 1 — Two different "full" messages:**

For completely new registrations:  
`"This class is full. Add yourself to the waitlist and we'll let you know if a spot opens up."`

For clients who are already registered:  
`"You're already enrolled in this class. Log in to your Parent Portal to complete your payment."`

**Fix 2 — Admin capacity display:**  
Current: capacity number, no breakdown  
Proposed: `"8/10 spots filled (6 enrolled + 2 trials)"`

This is all visible information — just not surfaced clearly.

**Type:** Error message copy (small) + capacity display (small)  
**Size:** Small

---

### Moment 10 — After class setup: where's the booking link?

**What they see now:**  
After creating a class, user lands back on the class detail or class list. No obvious next step.

**Problem:**  
The most critical thing after setup is: "how do my clients register?" Users search for a booking link, can't find it, ask support. Anna had to ask on Day 1.

**Fix — "Your class is ready" confirmation screen:**

After successful class creation:
```
✅ Class created — Monday Seahorse (9am), starting 5 Jan

Your clients can now register online.

[Copy booking link]   [Preview booking page]   [Back to programme]
```

Or if the booking link appears on the Programme card — add a tooltip/label making it obvious: `"Share this link with clients to let them register online"`

**Type:** Post-action confirmation screen or tooltip  
**Size:** Small–Medium

---

## Summary: what this unlocks

| Fix | Moment it hits | Prevents |
|-----|---------------|---------|
| Empty state checklist | Day 1, first login | Clicking randomly, wrong start point |
| Nav hierarchy | Day 1, first 10 min | Classes → Sessions confusion, "where is my class" |
| Programme form labels | Day 1, first form | Wrong payment model selected, can't explain to franchisees |
| Class breadcrumb | Day 1+ | Lost inside hierarchy, editing wrong programme's class |
| Scope selector on edit | Week 1–2 | Instructor/price/time changes not cascading as expected |
| "Groups" → "Classes" | Every day | Cognitive overhead, basic navigation confusion |
| Financial column labels | Every day | "Paid Debt" misread, support call per confused client |
| Payment status badge | Every day | "-£1,468" confusion, "is this client paid?" answered instantly |
| Capacity message split | Weekly | Enrolled parents panicking about "class full" |
| Post-setup booking link | Day 1 | "How do I share this with clients?" support question |

---

## What's NOT here

These gaps require engineering (new functionality), not UX:
- Term rebooking wizard (G1)
- Zooza-native refund flow (G2)
- Sibling discount rules (G9)
- Waitlist feature (N3 from cross-validation)

The fixes above are UX/copy/component changes. Most can be shipped without touching business logic.

---

## Prioritisation for franchise pitch

**Ship first (highest signal/effort ratio):**
- Moment 2 (nav hierarchy — Option A)
- Moment 5 (scope selector on instructor/time/price edit)
- Moment 8 (payment status badge)
- Moment 9 (capacity message copy)

**Ship second:**
- Moment 1 (empty state checklist)
- Moment 6 (Groups → Classes terminology)
- Moment 7 (financial column labels)
- Moment 10 (post-setup booking link)

**Ship third:**
- Moment 3 + 4 (Programme and Class form improvements)

---

*Based on: Anna (Turtle Tots), Kate (babyballet Dubai), Dom (Wee Kicks) — 3 independent client onboarding conversations*  
*UX brief by Claude Code / Michal Dodok, 10 May 2026*
