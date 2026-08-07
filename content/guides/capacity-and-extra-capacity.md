---
title: "Capacity vs extra capacity — who can take which seat"
description: "Three parts of Zooza read class capacity differently. Learn which seats the booking form, make-up sessions and trials can each take, and where the numbers are set."
slug: "capacity-and-extra-capacity"
type: "guides"
product_area: "Classes"
sub_area: ""
audience: ["admin"]
tags: ["capacity", "trials", "make-up", "booking", "class", "programme"]
related_articles: ["trial-sessions", "make-up-sessions-faq", "replacement-hours-complete", "trials-faq", "class-detail"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-08-07"
---

# Capacity vs extra capacity — who can take which seat

A class has two capacity numbers, and three different parts of Zooza read them differently. That is the whole model:

| Who is booking | Reads **Capacity** | Reads **Extra capacity** |
|---|---|---|
| A client on the booking form | Yes | No |
| A make-up (replacement) booking | Yes | Yes |
| A trial booking | Your choice | Your choice |

Read that table twice — almost every "why can't they book?" and "why did we end up over capacity?" question comes from it.

- **The booking form only ever sees Capacity.** Extra capacity is invisible to a paying client signing up. This is what stops a class being oversold.
- **Make-up sessions see both.** A client claiming a replacement can land in an extra seat when the main capacity is full.
- **Trials are the one you configure.** You decide whether trials compete for real seats or are confined to the extra ones.

## Reserving seats for trials and make-ups

Because the booking form ignores extra capacity, you can hold seats back without hiding them from the people who should get them.

Say a room fits 7 children. Instead of setting capacity to 7:

1. Set **Capacity = 5**.
2. Set **Extra capacity = 2**.

You now sell 5 places, and the remaining 2 are reachable only by trials and make-ups. The room still fills to 7.

Extra capacity is set per class and can be changed at any time, including in bulk across classes. A common pattern is to run 5 + 2 through the enrolment window and then move to 7 + 0 in September, once the class is full and you no longer need to court new families.

## Where each number lives

The two numbers are set in different places, which is the most common reason people cannot find them.

**Capacity** — on the class:

1. Go to **Programmes** → open the programme → open the class.
2. In the class settings, set **Class capacity**.
3. Save.

**Extra capacity** — in the make-up session settings, not in the Trial settings:

- **Globally:** **Team & Settings → Make-up sessions → Additional slots in classes**. This applies to every class in every programme.
- **Per class:** open the class → **Make-up sessions** tile. You can choose whether the class value **replaces** the global one or **adds** to it.

> The **Trial** tile only chooses *whether* trials may use extra capacity. It never contains the number itself. If you are looking for a field to type a number into inside the Trial settings, there isn't one — that is expected, not a missing setting.

## Choosing how trials use capacity

In **Programme → Settings → Trial → Session capacity**:

- **Current available capacity** — trials draw on capacity *and* extra capacity together. If an enrolled client cancels, that freed main seat becomes available to a trial.
- **Extra capacity** — trials are confined to the extra seats. Main capacity stays reserved for paying enrolments even when it is not full.

Pick **Extra capacity** if you never want a trial to occupy a seat you could sell. Pick **Current available capacity** if filling the room matters more than protecting the seat.

### Several people booking the same trial slot

If trials are set to **Current available capacity** and the class has room, nothing stops multiple families booking the same trial session. To limit it, set **Session capacity** to **Extra capacity** and keep the extra number small — a session disappears from the booking form once its available trial seats are gone.

## Related settings that also hold seats

- **Reserve a seat for a trial participant** (make-up settings) blocks make-up bookings from taking the seat a trial participant is expected to convert into.
- **Limit number of registrations** in the class's advanced settings is *not* capacity. It caps how many people a single booking may register — used for things like birthday parties. Set to 1, it hides the class from the booking form entirely. See [Class detail](../reference/class-detail.md).

## Related

- [Trial sessions](../setup/trial-sessions.md) — full trial configuration, including *Sessions shown in form*.
- [Make-up sessions FAQ](../faq/make-up-sessions-faq.md) — how extra capacity interacts with the 4-day rule and credit expiry.
- [Make-up sessions — complete guide](replacement-hours-complete.md)
