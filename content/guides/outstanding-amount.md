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

**3. Are billable sessions configured consistently?**
If **Billable sessions** is set to a number, that number must match the sessions actually marked billable at session level. Set it to 12 with no sessions marked, and the price has nothing to calculate from.

If every session is paid, you do not need billable sessions at all — leave the feature alone rather than setting it to the session count. See [Billable sessions](billable-sessions.md).

**4. With per-session pricing, how many sessions were in the future?**
Per-session pricing multiplies the unit price by the sessions still ahead **at the moment of registration**. If the sessions had not been generated yet, or all sat in the past, the result is 0 — and it stays 0 afterwards, because of the rule at the top of this page.

**5. Check `Balance` against `Outstanding`.**
They mean different things. `Balance: 0` means fully settled. An outstanding amount of 0 with no payment plan means nothing was ever owed. If you see the second on a new booking where every setting looks right, stop and contact support with the class link, the registration link, and the amount you expected — this is the point where it stops being a configuration question.
