---
title: "Priority registration for returning customers"
description: "Open a term to your existing students before the public, decided by who they are rather than by a link you have to send out."
slug: "priority-registration"
type: "guides"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: ["priority-registration", "returning-customers", "enrolment", "term", "waiting-list", "loyalty", "booking-form"]
related_articles: ["booking-widget-faq", "auto-enrolment-responses", "term-rebooking-guide", "share-course-link"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: true
last_converted: "2026-08-16"
---

# Priority registration for returning customers

Priority registration opens a term to your existing students first, and to everyone else later — or never. Eligibility is decided by **who the person is**, not by a link you have to send out.

This is the mechanism for protecting returning students' places before new customers can book.

## How it differs from what you may already use

Zooza has two older ways to give existing students a head start. They solve different problems:

| | What it does | When it fits |
|---|---|---|
| **Auto-enrolment** | Offers each existing booking a place in the next term, which they accept or decline | You know exactly who should continue and into which class |
| **Share link** | An unlisted link that exposes one class | A small, hand-picked group you can email |
| **Priority registration** | A window where any eligible customer can book a class that is closed to the public | You want returning students to choose freely, without sending anyone a link |

The practical difference is the last column. With a share link you decide who gets it; with priority registration Zooza decides who qualifies, and the customer browses and books normally.

## Setting it up

Priority registration is configured on the **programme**, and it applies to the whole term.

1. Open the programme and enable priority registration.
2. Set when the priority window opens. You can either give an offset — *"four weeks before the term starts"* — or enter an explicit date. An offset fills in the date for you, and you can still edit it.
3. Set when the class opens to the public, the same way. **Leave it empty if the term is only ever for returning students.**
4. Optionally narrow who qualifies (see below).
5. Save.

> **Dates are anchored to the start of the term**, not to each class. An offset resolves against the earliest class start in the billing period, so every class in the term opens together. That is usually what you want — a parent with two children in different classes should not face two different opening dates.

### Excluding individual classes

A programme with priority registration on does not force it onto every class. Each class can be individually excluded from the window, so a new class aimed at newcomers can open publicly while the rest of the term is reserved.

## Who qualifies

By default: **any existing customer of yours who is logged in.** Someone who has never booked with you does not qualify, and neither does a visitor who is not signed in.

You can narrow that further, and the conditions combine — a customer must satisfy all of them:

- **Programmes** — only people who attended particular programmes.
- **Terms** — only people who were enrolled in a particular billing period.
- **Venues** — only people at particular locations.
- **Age** — only children within an age band.

Leaving the audience empty means every existing customer qualifies.

Eligibility is worked out by Zooza, not by the booking form. There is no setting that lets a visitor claim eligibility for themselves.

## What customers see

**Before they log in**, a class in its priority window does not appear on the booking form at all. It is not shown as full or as closed — it is simply absent.

**Once they log in**, the list is fetched again and the class appears if they qualify. Logging in happens inline on the booking form, without leaving the page — see [the login step](../faq/booking-widget-faq.md#the-booking-form-now-asks-people-to-log-in--can-they-still-book-without-an-account).

Eligible customers also see the open window on their profile dashboard, with a button to register — so they do not have to remember to check.

## When the class opens to the public

If you set a public date, Zooza flips the class overnight on that date. You can also open it early by hand.

The flip happens **once and in one direction**. Once a class is public it stays public; nothing reverts it to the priority window.

If you set no public date, the class stays restricted to eligible customers for the whole term.

## Troubleshooting

**A parent says the class is not on the list.** Ask whether they are logged in. This is the most common report, and it is the feature working as designed — the class is invisible to anonymous visitors.

**A returning customer is logged in but still cannot see it.** Check the audience conditions on the programme. They combine, so a customer who attended the right programme but at a different venue will not qualify.

**The class did not open to the public.** Check that a public date is set. A programme configured before priority registration existed is not managed by the nightly flip, so a class from an older term will not open on its own.

## Related

- [Booking widget FAQ](../faq/booking-widget-faq.md) — the login step on the booking form.
- [Auto-enrolment responses](auto-enrolment-responses.md) — offering places directly instead.
- [Share a class link](share-course-link.md) — an unlisted link for a hand-picked group.
- [Delayed start](delayed-start-registration.md) — letting clients join a term late rather than waitlist them.
- [Shared room capacity](shared-room-gluing.md) — when the returning-student and newcomer classes share a room.
