---
title: "Children's Group Activities — Monthly Subscription Model"
description: "Parents go through a two-stage journey:"
slug: "children-group-activities-subscription"
type: "business-model"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: ["business-model", "children", "group", "subscription", "membership", "monthly", "recurring", "trial", "registration-fee"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-04-09"
---

# Children's Group Activities — Monthly Subscription Model

## This guide is for you if

- You run weekly group classes for children and charge a flat monthly fee
- Parents pay the same amount every month regardless of how many sessions fall in that month
- You charge a one-off registration fee when a child joins for the first time
- You offer a trial class before full membership starts
- Examples: ballet, gymnastics, football clubs, baby music, toddler yoga — any activity where membership is ongoing and classes repeat week after week

---

## How this model works in Zooza

Parents go through a two-stage journey:

1. **Trial** — one session at a reduced or free price. No commitment yet.
2. **Full membership** — recurring monthly payment, starting from the agreed date.

Zooza handles both stages with automated emails between them. Your job is to set up the Programme once and let the funnel run.

---

## Recommended setup

### 1. Create the Programme

Go to **Programmes → New Programme**.

- **Programme type:** *Booking for the full programme duration* — children are enrolled in every session automatically
- **Target audience:** *Group Classes*
- **For children:** tick Yes

### 2. Set up pricing

Under **How do you want to collect payments?** select *In scheduled payments*, then:

- **Price type:** *Membership* — a fixed fee charged repeatedly, regardless of the number of sessions in the month. This is the right choice when your price is "X per month", not "X per session" or "X per term".
- **Registration fee:** set the one-off enrolment fee here. It is charged at the time of the first booking and added on top of the first monthly payment. If you want returning clients to skip this fee, do not remove it from the Programme — use a discount code instead (see [Discount codes](../guides/discount-code.md)).
- **Unit price:** leave this at 0 for a pure membership. You only need a unit price if you want pro-rata calculation for mid-month joiners.

> Membership means the client pays the same amount whether there are 4 sessions or 5 in a given month. Parents know what to expect. You know what you'll collect.

### 3. Set up the trial

Enable **Trial** in Programme settings:

- Set the trial price (free, or a small deposit)
- The trial creates a separate registration — the child attends one session, and then the conversion flow begins automatically

The automated email sequence after a trial:
1. *Trial registration confirmed* — sent immediately on sign-up
2. *Trial ended — join us* — sent after the trial session. Include a **Join now** button using the dynamic tag `*|BOOKING_URL|*` — this links directly to the full membership booking form, pre-filled for that class
3. *Full registration confirmed* — sent once they complete the membership booking and payment

You do not need to chase parents manually. If they do not convert within your grace period, the trial registration is removed automatically.

### 4. Create Classes and Sessions

For each weekly group, create a **Class** under the Programme:

- Assign the **instructor** and **venue**
- Set the **capacity**
- Generate **Sessions**: go to the Class → Sessions → generate. Use *Advanced mode* to skip bank holidays or school holidays if needed. Always review the output before publishing.

Sessions repeat indefinitely for a membership model — you generate them in batches (e.g. per school term or per calendar year) and regenerate when needed.

---

## Managing existing clients (switching from another system)

If you are migrating clients from a different booking system:

1. Send existing clients the direct class booking link
2. Ask them to register and complete the first payment themselves — this creates their profile in Zooza and sets up the recurring mandate
3. If they have already paid a registration fee with you previously, give them a discount code that waives it (e.g. `EXISTING` for 100% off the registration fee)
4. Once they complete the booking, their monthly payments run automatically from that point

> Do not register them manually unless you have a specific reason to. Self-registration is cleaner: the parent sets up their own payment method, and there is no ambiguity about mandate ownership.

---

## Payment collection methods

| Method | Notes |
|---|---|
| **Stripe (card)** | Apple Pay and Google Pay work automatically once enabled in Stripe settings |
| **GoCardless (Direct Debit)** | Parents set up a mandate once; payments are pulled automatically each month. See [GoCardless setup](../guides/gocardless-direct-debit-mandates.md) |
| **Bank transfer** | Manual pairing required. Zooza matches incoming payments by reference. See [Payment pairing](../guides/payment-pairing.md) |

## When to charge — billing date options

Two approaches to when the monthly payment fires:

**Netflix-style (anniversary billing)**
Each parent pays on the anniversary of their sign-up date — if they joined on the 14th, they pay on the 14th every month. Payments spread across the month, cash flow is steady, no single "billing day" spike.

**Fixed billing date**
Everyone pays on the same day (e.g. the 1st of the month). Simpler to communicate to parents, easier to reconcile. Mid-month joiners pay a pro-rata amount for the first partial month, then switch to the fixed date from the next month.

> If you start with anniversary billing and later want to move everyone to a fixed date, that requires manual adjustment per booking. Decide before you launch.

---

## What happens when a parent does not pay

1. Zooza sends an automatic payment reminder
2. If no payment after the grace period, the booking is flagged as unpaid
3. The parent can complete payment themselves by logging into their **parent portal** — the option stays available there
4. You can also send a manual nudge from Bookings → select the booking → Send email

Set the grace period in Programme → Price & Payment → payment reminder settings.

---

## Re-enrolment and class continuity

Memberships do not have a fixed end date — they continue until cancelled. When you run a new school term:

- If the class continues with the same group, nothing changes. Existing members stay enrolled.
- If you are creating new classes for the new term, use **Auto-enrolment** to invite the current group. See [Auto-enrolment responses](../guides/auto-enrolment-responses.md).
- Members who do not re-confirm can be removed at the end of the term.

---

## Make-up lessons

Missed sessions are tracked automatically. Parents book make-up slots themselves from the parent portal — no admin needed. See [Replacement hours](../guides/replacement-hours-complete.md).

---

## Sibling discount

Set up a sibling discount under Loyalty settings. It applies automatically when a second child from the same account enrols. For siblings registered under different parent emails, apply the discount manually on the booking. See [Sibling discount](../guides/loyalty-sibling-discount.md).

---

## What Zooza does not support (for this model)

| Limitation | Workaround |
|---|---|
| Automatically pausing a membership (e.g. for holidays) | Cancel the booking and re-enrol when the child returns; or adjust the payment manually for that month |
| Charging a different price mid-month for late joiners | Set a unit price and use Term payment instead of Membership |
| Applying a franchise-wide template to all sub-accounts automatically | Set up templates at HQ level, then copy them into franchise accounts manually |

---

## Common mistakes

- **Setting Price type to Term payment instead of Membership** — Term payment has a fixed end date and splits a known total into instalments. Membership repeats indefinitely. If your clients pay "per month forever", use Membership.
- **Removing the registration fee instead of using a discount code for returning clients** — if you remove the fee from the Programme, new clients skip it too. Always use a discount code for exceptions.
- **Not testing the full booking flow before sending links to clients** — register as a test parent, complete a trial, convert to membership, check the emails. This takes 10 minutes and catches most setup issues before they reach real parents.
- **Sending the Programme link instead of the Class link** — if a parent needs to go to a specific group, copy the link from the Class detail. The Programme link shows all classes and locations, which can be overwhelming.
