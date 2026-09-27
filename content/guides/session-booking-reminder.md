---
title: "The session booking reminder"
description: "How Zooza nudges open-programme clients who signed up but booked no session, what each version of the email says, when it stops, and how to restart it."
slug: "session-booking-reminder"
type: "guides"
product_area: "Communication"
sub_area: "Email"
audience: ["admin"]
tags: ["notifications", "email", "reminders", "pay-as-you-go", "entry pass", "session booking"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-09-27"
related_articles: ["automated-notifications", "pay-as-you-go-programme", "pay-as-you-go-faq", "entry-pass-client-view", "creating-entry-passes"]
---

# The session booking reminder

On an open (pay-as-you-go) programme, signing up is not the same as having a
seat. The client still has to go into their profile and book individual
sessions, and many never take that second step — they register, sometimes buy a
pack of entry passes, and then nothing happens. Those passes and that intention
go to waste, and you lose the customer without ever hearing from them.

The reminder that used to be a plain daily list of tomorrow's sessions is now
aimed at exactly those clients.

## Who gets it, and when

Once a week, a client with **no upcoming booked session** on an open programme
gets one email, with a **Book** button beside each suggested session.

Nobody else gets it. The check runs again at send time, so a client who booked
an hour earlier drops out of that week's send.

## What the email says

It is built from that client's own situation, so no two recipients necessarily
get the same message:

| The client's situation | What the email leads with |
|---|---|
| Has entry passes, plenty left | Their balance and validity, plus sessions to book |
| Has passes expiring within 14 days | Use them before they expire |
| Has 2 or fewer passes left | Sessions to book, plus a gentle top-up link |
| Has an unpaid entry-pass order | Pay the order first — with the order number and amount |
| Passes expired unused in the last 30 days | Welcome back, plus a top-up |
| Has no passes at all | Book or buy passes (on a passes-only programme, buy first) |

Sessions are suggested from the client's usual slot where the class has one —
their regular Monday, or both days on a twice-weekly class — otherwise the
soonest session with a free place.

**Clicking Book never books anything.** The link logs the client in and opens
their session picker with that session pre-selected; they still confirm it
themselves. A mail client that pre-loads links therefore cannot hold a place or
spend a pass on the client's behalf.

## It stops on its own

Three weekly reminders with no response, then a 30-day pause, then one last
reminder — about four emails over two months. After that Zooza stops nudging
that registration.

Booking a session starts it again automatically, so a client who comes back
after a quiet spell is nudged again if they later lapse.

## Restarting reminders that stopped themselves

Open the booking and look at the **Communication** card. If Zooza gave up on
this registration it says so, and offers **Start reminders again**.

If the client has turned reminders off themselves, the card says that instead
and shows **no button**. That is deliberate: a reminder needs both the client's
consent and an active reminder state, so restarting would send nothing. Change
**Reminder** on the booking's **Options** tab first if that is what you intend —
and be aware you are overriding the client's own choice.

## Turning it off for a whole class

The reminder is the **Upcoming events notifications** toggle on the class:
**Programmes → your programme → Online Booking → Edit**. Switching it off stops
the reminder for everybody in that class.

## Editing the wording

The template is **Session Reminder** in **Communication → Templates**. You edit
the greeting and the signature around the tag
<code>&#42;&#124;UPCOMING&#95;EVENTS&#124;&#42;</code>; the tag itself renders the
whole personalised block — balance, suggested sessions, and the right **Book**,
**Pay** or **Buy** button — and Zooza decides its content per client. If you
delete the tag, Zooza appends the block anyway rather than send an email with
nothing to act on.

You can override the subject with a single line, but it then applies to every
version of the email, including the ones whose default subject was written for
a different situation.

## Related

- [Automated notifications overview](automated-notifications.md) — every automatic email and where it is configured
- [Pay-as-you-go programme](pay-as-you-go-programme.md) — how open programmes work
- [Pay-as-you-go FAQ](../faq/pay-as-you-go-faq.md) — sign-ups, bookings and who has booked nothing
- [Entry pass — client view](entry-pass-client-view.md) — what the client does after they click Book
