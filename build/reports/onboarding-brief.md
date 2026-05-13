# Onboarding Brief — Ultimate Zooza Onboarding Flow

**Date:** 12 May 2026
**Purpose:** Spec for building the onboarding sequence — in-app checklist, help content order, and onboarding emails. Inputs: core-workflows.md, Thinksmart process table (Kate), WhatsApp onboarding journeys (Anna/Kate/Dom).

---

## Who this is for

**Primary:** Owner/admin of a children's activity or education business migrating from Thinksmart (or from a spreadsheet/paper system). Typically:
- 1–4 classes, 10–60 clients per class
- Term-based (8–12 sessions) or monthly rolling subscription
- Usually some combination of card payments, direct debit, and bank transfers
- Usually runs trials before full enrolment
- Often has 1–3 instructors who need access for attendance only
- May or may not need invoices (depends on country)

**Secondary:** Franchise operator setting up their first location (higher urgency, more decisions upfront).

---

## The key insight: two types of onboarding decisions

Before someone can get clients through the door, they face two kinds of setup:

1. **Decisions** — choices that are hard to undo later (payment model, GoCardless vs Stripe, whether to use trials). Getting these wrong costs time.
2. **Configuration** — mechanical setup that's low-risk (add location, add instructor, create a class). Easy to redo.

The onboarding flow should force the **decisions first**, then make the configuration feel easy.

---

## The big decision: how you collect money

This is the most consequential choice and the one most people are unprepared for. It determines everything downstream.

```
How will clients pay?
├── Stripe (card online) → client pays at booking or via payment link
│     └── Most businesses combine this with bank transfer for clients who prefer it
├── Bank transfer → clients send money to your account
│     ├── Manual: you record each payment yourself on the booking
│     └── Automatic matching: connect GoCardless or set up email notifications
│           Zooza matches incoming transfers to bookings by variable symbol — no manual entry
└── No online payment — invoices only
      └── Zooza generates invoices; clients pay by transfer; you record manually
```

> **GoCardless in Zooza has two roles:** (1) **Direct debit** — Zooza pulls payment directly from a client's bank account via GoCardless mandate. (2) **Inbound payment matching** — Zooza connects to your bank account (via GoCardless Bank Data API or email notifications from your bank) and automatically pairs incoming bank transfers to the right bookings using the variable symbol. If you take bank transfers and want to save time on manual recording, inbound matching is the right tool.

**Variations this creates downstream:**
- Stripe → refund can be processed via Zooza; card payments are automatic
- Bank transfer + manual → you record each payment on the booking
- Bank transfer + GoCardless inbound → automatic matching; unmatched payments need periodic review
- Invoicing → invoice profile setup + optional Xero connection

---

## Phase 1: Before you go live (Day 1–7)

### Everyone does these — regardless of payment method

| Step | What to do | KB article | Time |
|------|-----------|-----------|------|
| 1 | Add your location(s) and venue details | [Settings → Locations] | 5 min |
| 2 | Create your first programme — set name, payment type, price | [creating-a-programme.md] | 10 min |
| 3 | Add a class inside the programme — day, time, instructor, capacity | [creating-a-class.md] | 5 min |
| 4 | Preview your booking page — check it looks right before sharing | — | 5 min |
| 5 | Do a test booking yourself — go through the client experience | [admin-vs-self-service.md] | 10 min |

> **Critical concept to install at step 2:** Programme → Class → Session. The hierarchy is not obvious. Admin must understand that the programme sets the rules, the class sets the schedule. See [programme-class-session-definition.md].

### Payment setup — fork by method

**If using Stripe:**
| Step | What to do | KB article |
|------|-----------|-----------|
| P1 | Connect Stripe in Settings → Integrations | [inbound-payments-setup.md] |
| P2 | Set whether you want to collect payment at booking or send a link later | [price-and-payment-setup.md] |

**If using bank transfer (manual recording):**
| Step | What to do | KB article |
|------|-----------|-----------|
| P1 | Add your bank account details to Settings → Billing | [inbound-payments-setup.md] |
| P2 | For each payment received: open the booking, add payment manually | [edit-payment-on-booking.md] |
| P3 | Optionally import a CSV bank statement to match payments in bulk | [csv-payment-import.md] |

**If using bank transfer + GoCardless inbound (automatic matching):**
| Step | What to do | KB article |
|------|-----------|-----------|
| P1 | Connect GoCardless inbound in Settings → Payments → Inbound → Setup | [inbound-payments-setup.md] |
| P2 | Add your IBAN — Zooza uses it to match incoming transfers to bookings automatically | [payment-pairing.md] |
| P3 | Review any unmatched payments in Payments → Inbound → Unmatched | [payment-pairing.md] |

**If using invoicing:**
| Step | What to do | KB article |
|------|-----------|-----------|
| P1 | Set up your invoice profile (company name, VAT, logo) | Settings → Billing → Invoice Profile |
| P2 | Choose when invoices are auto-generated (on registration, on payment, on demand) | [downpayment-split-invoicing.md] + [automatic-payment-reminders.md] |
| P3 | Optionally connect Xero | [xero-integration.md] |

### If you run trials (most do):
| Step | What to do | KB article |
|------|-----------|-----------|
| T1 | Enable trials in Programme → Settings → Trial | [trial-sessions.md] |
| T2 | Set trial type: free or paid, 1 or 2 sessions | [trial-sessions.md] |
| T3 | Understand: clients book their own trials — you cannot create a trial manually | [trials-daily-business.md] ⚠️ |
| T4 | Decide if trials hold a capacity spot (reserve seat setting) | [trials-daily-business.md] |

### Add instructors (if applicable):
| Step | What to do | KB article |
|------|-----------|-----------|
| I1 | Add instructor via Settings → Team | [managing-instructors.md] |
| I2 | Choose role: Instructor (attendance + limited access) or Main instructor (more) | [managing-instructors.md] |
| I3 | Share the instructor guide with them | [zooza-101-instructors.md] |

**Before you open bookings — self-check:**
- [ ] Programme exists with correct payment type
- [ ] At least one class with sessions scheduled
- [ ] Payment method connected and tested
- [ ] Trial settings confirmed (if using trials)
- [ ] Test booking completed successfully
- [ ] Booking link ready to share

---

## Phase 2: First clients (Day 7–21)

### If using trials:

| Step | What happens | Who acts | KB article |
|------|-------------|---------|-----------|
| 1 | Client books trial online via your booking link | Client | — |
| 2 | You receive a notification. Client is in your bookings with status "Trial started" | System | — |
| 3 | Instructor marks attendance at the end of trial | Instructor | [instructor-attendance-management.md] |
| 4 | If attended: system auto-sends parent a link to complete full enrolment | System | — |
| 5 | If not attended: mark as Trial Lost and optionally reschedule | Admin | [trials-daily-business.md] |
| 6 | If trial is at capacity: client sees "class full" — understand this is correct | Admin | [trials-daily-business.md] |

> **Common mistake:** Admin expects to create trials on behalf of clients. This is by design — clients must book themselves. Send the booking link.

### If directly enrolling (no trial):

| Step | What happens | Who acts | KB article |
|------|-------------|---------|-----------|
| 1 | Share booking link — client registers and pays online | Client | [admin-vs-self-service.md] |
| OR | Create booking manually in Bookings → New | Admin | [creating-a-booking.md] |
| 2 | Record payment if they paid offline (cash / bank transfer) | Admin | [edit-payment-on-booking.md] |

### Recording first payments:

**Stripe:** Payment collected automatically at booking — nothing to do.

**Bank transfer + GoCardless inbound:** Payment arrives in your bank account; GoCardless matches it to the booking automatically. Check Payments → Inbound → Unmatched for any that didn't match.

**Bank transfer (manual):**
| Step | What to do | KB article |
|------|-----------|-----------|
| 1 | When payment arrives in your bank, find the booking | — |
| 2 | Open booking → Payments → Add payment → enter amount, date, method: Bank transfer | [edit-payment-on-booking.md] |
| 3 | System marks as paid and generates invoice if invoicing is on | — |

---

## Phase 3: First month — core operations

These are the things that happen regularly once clients are enrolled.

### Weekly:

| What | KB article | Notes |
|------|-----------|-------|
| Mark attendance | [instructor-attendance-management.md] | Instructor does this, or admin if no instructor access |
| Handle trial results (attend/lost/reschedule) | [trials-daily-business.md] | |
| Transfer a client to different class | [transfer-and-copy-bookings.md] | When a client wants to change slot |
| Cancel one session, offer make-up | [custom-replacement-lessons.md] | Session-level cancel, not booking cancel |
| Send bulk email to a class | [sending-email-sms.md] | Announcements, schedule changes |

### Monthly:

| What | KB article | Notes |
|------|-----------|-------|
| Chase unpaid clients | [automatic-payment-reminders.md] | Set up auto-reminders once — they run themselves |
| Record bank transfer payments | [edit-payment-on-booking.md] | Only for bank transfer users |
| Process a refund | [stripe-refund-guide.md] · [recording-an-administrative-refund.md] | Stripe: refund via Zooza or directly in Stripe dashboard. Bank transfer: return money from your bank, then record admin refund in Zooza |
| Apply sibling discount / discount code | [loyalty-sibling-discount.md] · [discount-code.md] | |
| Download payment report for accountant | [where-to-find.md] → Reports section | |

### If using GoCardless inbound — periodic check:
| What | KB article |
|------|-----------|
| Review unmatched payments in Payments → Inbound → Unmatched | [payment-pairing.md] |
| Re-pair any transfers Zooza couldn't match automatically | [payment-pairing.md] |

---

## Phase 4: End of first term (Month 2–3)

| Step | What to do | KB article |
|------|-----------|-----------|
| 1 | Set up new term's class structure (copy old class, adjust dates) | [term-rebooking-guide.md] |
| 2 | Adjust pricing for new term if changed | [term-rebooking-guide.md] |
| 3 | Roll clients over — copy bookings OR send auto-enrolment invite | [term-rebooking-guide.md] |
| 4 | Handle non-renewals — cancel bookings of clients not continuing | [term-rebooking-guide.md] |
| 5 | Archive old classes once empty | [archive-or-delete-programme.md] |
| 6 | Generate end-of-term report for accountant | Reports → filter by term dates |

---

## Phase 5: Accountant handoff

| What to export | Where | Format | Notes |
|---------------|-------|--------|-------|
| Invoices | Sales & Payments → Invoices | PDF / XML | Monthly |
| Payments received | Reports → Payments | CSV | By date range |
| Client list | Reports → Clients | CSV | Periodic |
| Xero export | Reports → Xero | Direct sync | If Xero connected |

> Most accountants want invoices monthly. Set up a calendar reminder to export on the 1st of each month.

---

## Instructor onboarding (parallel track)

Instructors are a separate, simpler track. They don't need to go through phases 1–5.

**What they need to do:**
1. Receive login invitation from admin (or go to zooza.app and enter their email)
2. Add Zooza to their phone home screen — [add-zooza-app-to-phone.md]
3. Find their sessions on the dashboard
4. Mark attendance

**What they do NOT need:**
- Payment setup
- Programme creation
- Any of phases 1–5

**Send instructors:** [zooza-101-instructors.md] — covers everything they need.

**Admin note:** Instructors see a different, limited interface. They cannot find "Programmes" or "Clients" in the menu unless you give them a higher role. This is normal. See [managing-instructors.md].

---

## Decision matrix: what applies to you

| Your setup | Extra steps required |
|-----------|---------------------|
| Stripe only | Phase 1 Stripe setup → Phase 3 Stripe refund guide |
| Bank transfer only (manual) | Phase 1 bank setup → manual payment recording in Phase 3 |
| Bank transfer + GoCardless inbound | Phase 1 GoCardless inbound setup → periodic unmatched review |
| Mixed (Stripe + bank transfer) | Both Stripe and bank transfer setup → both payment recording flows |
| Invoicing required | Invoice profile setup → optional Xero connection |
| Trials enabled | Phase 2 trial flow → understand admin can't create trials |
| Term-based | Full Phase 4 (term rebooking) |
| Monthly rolling | No term rebooking — use rolling payment templates instead |
| Franchise / network | Franchise network setup applies additionally → [franchise-network.md] |

---

## What's missing from KB to fully support this onboarding

| Gap | Status | Suggested article |
|-----|--------|------------------|
| "Choose your payment method" decision guide — Stripe vs. bank transfer vs. GoCardless inbound — what's right for my business? | ❌ Missing | `content/setup/choose-payment-method.md` |
| Monthly rolling subscriptions — how to set this up vs. term-based | 🟡 Partial — subscription FAQ exists but no setup guide | `content/setup/monthly-subscription-setup.md` |
| Client-side experience — what clients see when they register, pay, and manage their booking in the Parent Zone | ❌ Missing | `content/guides/parent-zone-guide.md` |
| "End of term" checklist — single page with the 5 steps an admin does before each new term | 🟡 Covered in term-rebooking-guide.md but could be a standalone checklist | — |

---

## Onboarding email/message sequence (suggested)

If building an automated onboarding email sequence, these are the key moments:

| Day | Trigger | Message content | KB link |
|-----|---------|-----------------|---------|
| 0 | Account created | Welcome + "start here" checklist link | getting-started-with-zooza.md |
| 1 | After first programme created | "Add your first class" prompt | creating-a-class.md |
| 2 | After first class created | "Connect your payment method" prompt | inbound-payments-setup.md |
| 3 | After payment connected | "Share your booking link" — copy it + test it | — |
| 7 | 7 days in, if no booking yet | "Here's how to get your first client in" | admin-vs-self-service.md |
| 14 | After first client enrolled | "Set up automatic payment reminders so you don't have to chase" | automatic-payment-reminders.md |
| 21 | If GoCardless inbound connected | "Check for any unmatched bank transfers in Payments → Inbound" | payment-pairing.md |
| 30 | 30 days in | "Monthly report for your accountant" | where-to-find.md → Reports |
| 60 | If term-based | "Preparing for your term end — what to do now" | term-rebooking-guide.md |

---

## Differences from the Thinksmart model (migration context)

For clients migrating from Thinksmart specifically, these are the biggest mental-model shifts:

| Thinksmart way | Zooza way | Where documented |
|---------------|-----------|-----------------|
| Admin creates every booking manually | Clients self-register via booking link; admin creates only exceptions | [admin-vs-self-service.md] |
| Admin creates trial manually | Client books their own trial; admin just monitors | [trials-daily-business.md] |
| Bank transfer matching done manually in spreadsheet | Zooza connects to your bank (via GoCardless or email notifications) and auto-pairs incoming transfers to bookings by variable symbol | [payment-pairing.md] |
| Term reset = admin manually moves everyone | Copy bookings in bulk or use auto-enrolment; clients confirm themselves | [term-rebooking-guide.md] |
| Refund handled in payment provider only | Refund can be processed via Zooza (Stripe) or recorded as admin record (all methods) | [stripe-refund-guide.md] · [recording-an-administrative-refund.md] |
| Programme = flat structure | Programme → Class → Session hierarchy; each layer has different scope | [programme-class-session-definition.md] |

---

*Based on: Thinksmart process table (Kate), WhatsApp onboarding conversations (Anna/Kate/Dom), core-workflows.md*
*Brief by Claude Code / Michal Dodok, 12 May 2026*
