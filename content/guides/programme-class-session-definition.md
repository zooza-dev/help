---
title: "Programmes, classes, and sessions explained"
description: "Understand how Zooza's three-layer structure works — what each layer controls, what changes cascade, and which layer to edit for common tasks."
slug: "programme-class-session-definition"
type: "guides"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: ["programme", "class", "session", "hierarchy", "structure", "cascade", "edit", "timetable"]
status: "published"
source_legacy_path: "legacy/0048_Welcome to Zooza.html"
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-05-11"
---

# Programmes, classes, and sessions explained

Zooza organises everything in three layers. Understanding what each layer does — and what happens when you edit one — will save you a lot of confusion.

```
PROGRAMME
  └── CLASS
        └── SESSION
```

Think of it like a school:

- The **programme** is a subject — Maths, Swimming, Ballet. It sets the rules: who can enrol, how payment works, whether trials are allowed.
- The **class** is a specific group running that subject — Monday 9am, Wednesday 4pm. It defines the schedule, location, instructor, and capacity.
- The **session** is a single lesson — Monday 6 January 9am. It's the individual occurrence where you record attendance and handle cancellations.

---

## What each layer controls

| | Programme | Class | Session |
|--|-----------|-------|---------|
| Name and description | ✅ | ✅ | — |
| Payment model (term / drop-in / one-off) | ✅ | — | — |
| Price | ✅ reference | ✅ actual | — |
| Booking form settings | ✅ | — | — |
| Trial settings | ✅ | — | — |
| Make-up session rules | ✅ | — | — |
| Day and time | — | ✅ | ✅ override |
| Location | — | ✅ | ✅ override |
| Instructor | — | ✅ | ✅ override |
| Capacity | — | ✅ | — |
| Attendance | — | — | ✅ |
| Cancellation | — | — | ✅ |

---

## What cascades — and what doesn't

This is the part that surprises most new users.

**Changes at Programme level** apply to all future enrolments but do not automatically update existing bookings. If you change the price at programme level, clients who already booked keep their original price.

**Changes at Class level** apply to all sessions in that class by default — but only if you haven't already overridden individual sessions. You choose the scope when saving.

**Changes at Session level** apply to that one occurrence only. They do not affect other sessions in the class.

### Scope selector — always check before saving

When you edit an instructor, time, or price at Class or Session level, Zooza asks you to confirm the scope:

- **This session only** — e.g. a one-off substitute instructor
- **All upcoming sessions in this class** — e.g. a permanent instructor change
- **All sessions including past ones** — use rarely, only for corrections

If you don't see this prompt, check that you're editing at the right layer (see below).

---

## Which layer to edit — quick reference

| What you want to do | Where to go |
|--------------------|-------------|
| Change how clients pay (monthly, per term, per session) | **Programme** → Settings |
| Change the price for a new term | **Class** → Edit → Price |
| Change the price for one client only | **Booking** → Edit payment |
| Change the instructor permanently | **Class** → Edit → Instructor → All upcoming sessions |
| Change the instructor for one class only | **Session** → Edit → Instructor → This session only |
| Change the class time permanently | **Class** → Edit → Time → All upcoming sessions |
| Move a single session to a different time | **Session** → Edit → This session only |
| Cancel one lesson | **Session** → Cancel session |
| Cancel the whole class | **Class** → Archive or end date |
| Enable or disable trials | **Programme** → Settings → Trials |
| Enable or disable make-up sessions | **Programme** → Settings → Make-up sessions |
| Change who can see this programme online | **Programme** → Online booking on/off |

---

## Common mistakes

**Editing the wrong layer and wondering why it didn't save**
If you change the instructor in the *Timetable* view but nothing updates in the *Sessions* view — or vice versa — you likely edited at the wrong level. The Timetable shows Class-level data. Sessions are individual occurrences. Check which one you opened.

**Changing price at Programme level expecting it to update existing bookings**
It won't. Programme-level price is a reference for new enrolments. To update an existing client's price, go to their Booking and edit the payment directly.

**Cancelling a session and expecting all future sessions to cancel too**
Session cancellation affects one occurrence. To end the class entirely, set an end date on the Class or archive it.

**Editing a session and not seeing the scope selector**
Some fields (like instructor rate) don't have a scope selector — they apply to the class, not the session. If you're editing from inside a single session and the field is greyed out, edit from the Class instead.

---

## Billing periods

Billing periods are an optional layer above Programmes. They let you group programmes into semesters or school years — useful if you want to carry over make-up credits between terms, or run reports per period.

You don't need billing periods to run Zooza. Most businesses add them once they've been running for a term or two and want cleaner reporting.

---

## API note

If you're building on the Zooza API, the field names differ from the app labels:

| App label | API field |
|-----------|-----------|
| Programme | `course` |
| Class | `schedule` |
| Session | `event` |

See the [developer docs concepts page](https://docs.zooza.online/concepts) for full mapping.

---

## Related guides

- [Create a programme](creating-a-programme.md)
- [Create a class](creating-a-class.md)
- [Edit sessions in programmes](edit-sessions-in-programmes.md)
- [Change instructor](change-instructor.md)
- [Getting started with Zooza](../setup/getting-started-with-zooza.md)
