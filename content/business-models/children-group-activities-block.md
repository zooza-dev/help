---
title: "Children's Group Activities — Block / Term Model"
description: "Three levels. You need all three before a parent can book."
slug: "children-group-activities-block"
type: "business-model"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: ["business-model", "children", "group", "blocks", "term", "trial", "pro-rata"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-04-09"
---

# Children's Group Activities — Block / Term Model

## This guide is for you if

- You run weekly group classes for children and sell them in fixed blocks or school terms
- Parents pay for a set number of sessions — either upfront or in instalments spread across the term
- You offer a trial class before full enrolment
- You run multiple groups in parallel: different age bands, levels, or venues
- Examples: baby swimming, toddler movement, children's dance, language clubs, STEM groups

---

## How Zooza models your business

Three levels. You need all three before a parent can book.

| Zooza concept | What it means for you |
|---|---|
| **Programme** | The offer — e.g. "Toddler Swim", "Mini Movers". Holds the rules: price, payment type, registration form, trial settings. |
| **Class** | A specific group — e.g. "Monday 9:30, beginners, City Pool". Has its own capacity and instructor. |
| **Session** | A single class date — e.g. Monday 9:30 on 5 May. Attendance and make-up lessons live here. |

The most common setup mistake: people look for the price on the Class, or look for the instructor on the Programme. **Price lives on the Programme. Instructor and venue live on the Class.** If something is not showing where you expect it, check which level you are editing.

---

## Recommended setup

### 1. Create the Programme

Go to **Programmes → New Programme**.

Select the **Programme type:**
- **Booking for the full programme duration** — the child is automatically enrolled in every session. Make-up lessons are available. This is the right type for a block or term model.
- *One-off event* — for a single session: a workshop, taster day. Not suitable for a recurring term.
- *Pay-as-you-go* — clients self-select individual sessions. Use only if you want open drop-in booking.

For a children's block course: select **Booking for the full programme duration**, set **Target audience** to *Group Classes*, and tick **For children**.

**Registration fee** — if you charge a one-off enrolment fee, add it here. It is collected on top of the course price at the moment of first booking. Do not remove it when returning clients re-enrol — use a discount code instead (see [Discount codes](../guides/discount-code.md)). That way new clients always pay it, and returning clients get a code.

### 2. Set the price and payment

Under **How do you want to collect payments?** choose one of:

**Option A — One-off payment**
Parents pay the full block price in a single transaction at registration. Simple, no instalment logic. Works well when you open registrations before the term starts and want payment upfront.

**Option B — Term payment + Unit price** *(recommended if clients can join mid-term)*
- Set a **Unit price** (price per session)
- When a parent registers, Zooza counts the remaining sessions and calculates their total automatically — pro-rata without any manual work
- Add a payment template if you want the total split into monthly instalments (see [Payment templates](../guides/payment-templates-creation.md))

> Term payment means the client always knows the full amount they owe. It is fixed from the moment they book. Membership (the other price type) repeats indefinitely and has no fixed end. For a block course, use Term payment.

### 3. Create Classes

For each group — age band × location × time slot — create a **Class** under the Programme:

- Assign the **instructor**
- Set the **venue**
- Set the **capacity**

To create similar groups quickly, copy an existing Class. The copy inherits the Programme but you adjust time, instructor, and venue.

### 4. Generate Sessions

Inside each Class, go to Sessions and generate the term:

- **Simple mode**: set start date, end date, and the weekly day/time. Zooza builds the full list.
- **Advanced mode**: skip bank holidays or school holidays automatically. Always review the output — school holiday data may not be accurate for every area.

Delete any individual sessions that fall on a venue closure or special date. Do this before you publish.

### 5. Set up the trial

Enable **Trial** in Programme settings and set the trial price (free or a small deposit).

The trial creates a separate registration. After the session, the conversion flow runs automatically:
1. *Trial registration confirmed* — sent immediately
2. *Trial ended — join us* — sent after the session. Add a **Join now** button using the dynamic tag `*|BOOKING_URL|*` to link straight to the booking form
3. *Full registration confirmed* — sent once they complete payment

You do not chase parents manually. If they do not convert within the grace period, the trial registration is removed.

---

## Payment flow for parents

1. Parent opens the booking link — either a direct class link or the general programme page
2. They fill in the form: child's name, consents, any custom fields you added
3. They pay the block price (plus registration fee if applicable)
4. Confirmation email lands in their inbox
5. Automatic session reminders go out before each class — enabled by default

Always share the **class-specific link** when directing a parent to a particular group. Copy it from the Class detail page. The class link pre-fills their selection; the Programme link shows all available classes, which can be overwhelming.

---

## Re-enrolment (new term)

When a term ends and you open the next one:

1. Create new Classes and Sessions under the same Programme, or copy existing Classes
2. Use **Auto-enrolment** to invite the current group: Class → Auto-enrolment → send invitation
3. Clients who confirm are copied into the new class and still need to pay for the new term
4. Clients who do not respond can be followed up or removed at the end of your deadline

See [Auto-enrolment responses](../guides/auto-enrolment-responses.md).

---

## Make-up lessons

Missed sessions are tracked automatically. Parents book a make-up slot themselves from the parent portal — no admin needed on your side. See [Replacement hours](../guides/replacement-hours-complete.md).

---

## Sibling discount

Set up a sibling discount under **Loyalty → Sibling discount**. It applies automatically when a second child from the same account enrols. For siblings on separate parent accounts, apply the discount manually on the booking. See [Sibling discount](../guides/loyalty-sibling-discount.md).

---

## What Zooza does not support (for this model)

| Limitation | Workaround |
|---|---|
| Automatically waiving the registration fee for returning clients | Use a discount code (e.g. `RETURNING`) for 100% off the registration fee |
| Retroactively adjusting a block price after booking | Edit the payment manually on the booking |
| Auto-detecting siblings across separate parent accounts | Apply the sibling discount manually |

---

## Common mistakes

- **Looking for the price on the Class** — price lives on the Programme. The Class only holds capacity and instructor.
- **Publishing before you have reviewed the session list** — parents can see the class as soon as it is live. Generate sessions, check the dates, then publish.
- **Sending the Programme link instead of the Class link** — the Programme link shows every class and location. If you want a parent to go to one specific group, use the Class link.
- **Enabling both one-off and scheduled payment without guidance** — two payment options that look similar will confuse parents. Pick one and enable only that.
- **No payment reminder grace period set** — if a parent registers without paying, Zooza sends reminders automatically, but only if the grace period is configured. Check Programme → Price & Payment → payment reminder settings before you go live.
