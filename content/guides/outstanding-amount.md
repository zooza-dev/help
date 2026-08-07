---
title: "Outstanding amount — why it does not follow price changes"
description: "The amount a booking owes is fixed when the booking is created and never recalculates. Learn why, and what to check when a booking shows zero or the wrong amount."
slug: "outstanding-amount"
type: "guides"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: ["billing", "booking", "client", "communication", "import", "payment", "programme", "session"]
related_articles: ["billable-sessions", "edit-payment-on-booking", "payment-correction-vs-refund", "price-and-payment-setup", "payment-pairing"]
status: "published"
source_legacy_path: "legacy/0095_Welcome to Zooza.html"
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-08-07"
---

# Outstanding amount — why it does not follow price changes

When a booking is created, Zooza works out what that client owes and stores it on the booking. This figure is the **outstanding amount**, and it is what Zooza uses to decide whether the booking is paid.

**It is calculated once, at the moment the booking is created, and never recalculates.**

Changing the price on a class or programme afterwards does not touch bookings that already exist. That is deliberate. If the outstanding amount tracked the current price, every historical booking would flip to unpaid the moment you adjusted a price for next term, because the payments already recorded would no longer match.

The consequence is worth stating plainly: **the outstanding amount does not have to match the current price of the class.** A booking created when the class cost €180 still owes €180 after you raise the price to €270.

## Changing what an existing booking owes

Price changes only reach new bookings. To change an existing one, edit the payment on that booking directly — see [Edit payment on booking](edit-payment-on-booking.md). For a whole class of bookings, do it as a deliberate bulk operation rather than expecting a price change to propagate.

## What is not the outstanding amount

It has nothing to do with reimbursements. It is not arrears, not a dunning figure, and it carries no interest. It is simply the amount you expect the client to pay for that booking.

## Troubleshooting: a booking shows 0 or the wrong amount

Work through these in order.

**1. Was the booking created before the price was set?**
The most common cause by far. If the class was free — or the price had not been entered yet — when the client registered, the booking stored 0 and kept it. Check when the booking was created against when you set the price.

**2. Is the class price actually set, or set to 0?**
A class price of **0 is treated as "not set"**, and Zooza falls back to the programme price. This means you cannot make one class free inside a paid programme by typing 0 into it. To run a genuinely free class, either set the whole programme to 0, or put that class in its own programme priced at 0.

**3. Does the class have a paid-sessions counter with no paid sessions behind it?**
This is the most common cause of a price of exactly 0 on an otherwise correct setup.

If the class says it has, for example, **13 billable sessions**, but not one session is marked as billable, Zooza has nothing to multiply — so the price comes out as 0. The counter and the sessions have to agree.

Two ways out, and you only need one:

- **Mark the sessions as billable** — you can do this now, in bulk, from the sessions list.
- **Reset the counter on the class** to 0, so the price is calculated from all sessions.

If every session is paid, do not use billable sessions at all. The feature exists to *exclude* sessions from the price; setting it equal to the session count adds a way to get it wrong for no benefit. See [Billable sessions](billable-sessions.md).

> Worth checking if you used the AI assistant to set up classes. It has been known to fill in the paid-sessions counter without being asked, which produces exactly this symptom across a whole term of classes at once.

**4. With per-session pricing, how many sessions were in the future?**
Per-session pricing multiplies the unit price by the sessions still ahead **at the moment of registration**. If the sessions had not been generated yet, or all sat in the past, the result is 0 — and it stays 0 afterwards, because of the rule at the top of this page.

**5. Is 0 actually correct?**

Several perfectly normal setups produce an outstanding amount of 0, and this is the step people skip. Before treating it as a fault, check whether there is genuinely anything to pay *yet*:

- **The class is lead collection.** There is no schedule and no billing period, so nothing is owed. This is by design — see [Lead collection](lead-collection.md).
- **The programme is pay-as-you-go.** Enrolling in the class costs nothing; the client is charged per session as they book. An outstanding amount of 0 on the registration itself is the expected state.
- **The payment falls due later.** With a template billing on, say, the 1st of the month, a client who registers after that date owes nothing until the next cycle.
- **The pro-rata window contains no sessions.** If the class starts later and there is no session between today and the first billing date, the aliquot calculation has nothing to charge for — correctly returning 0.

**6. If it is genuinely wrong, it is a configuration question, not a fault.**

An outstanding amount that should not be 0 is almost always traceable to one of three places. Work through them in this order:

| Check | What to look for |
|---|---|
| **Programme type** | Does the type charge at enrolment at all? Pay-as-you-go and lead collection do not. |
| **Payment template** | Is one active, does it match the collection mode, and when does it first bill? |
| **Class / group settings** | Price set and not 0, and the billable-session counter consistent with the sessions (step 3 above). |

Between those three you will find it. Contact support with the class and registration links only once you have ruled all three out — and say which you checked, because that is what turns it into a five-minute answer rather than a diagnosis from scratch.
