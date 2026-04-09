---
title: "Individual Lessons — 1-to-1 Model"
description: "Group classes have a fixed timetable that many clients share. Individual lessons do not — each client has their own private schedule with their instructor."
slug: "individual-lessons"
type: "business-model"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: ["business-model", "individual", "1-to-1", "language", "tutoring", "personal-training", "packages", "pay-as-you-go"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-04-09"
---

# Individual Lessons — 1-to-1 Model

## This guide is for you if

- You offer private one-to-one lessons: one instructor, one student per session
- Clients book their own schedule — dates and times vary per client
- You sell lessons in packages (e.g. 10 lessons prepaid) or per session
- You offer a free first session before the client commits to a package
- Examples: private language tutoring, personal training, individual music lessons, one-to-one swimming coaching, private dance coaching

---

## How individual lessons work differently in Zooza

Group classes have a fixed timetable that many clients share. Individual lessons do not — each client has their own private schedule with their instructor. Zooza handles this by letting you create a private class per client (or per instructor), where you add sessions as they are agreed.

There is no public timetable for individual lessons. Instead you collect interest first, then build the private plan behind the scenes.

---

## Recommended setup

### 1. Create the Programme

Go to **Programmes → New Programme**.

- **Programme type:** *Booking for the full programme duration* — the client commits to the package, not to individual session slots
- **Target audience:** *1-to-1 classes*
- **For children:** tick Yes if applicable (changes the wording on the booking form)

Give the Programme a name clients will recognise — e.g. "Private English Lessons" or "Personal Training". This is what appears on the booking form.

### 2. Set the price

Two common approaches:

**Package pricing (recommended)**
Sell a fixed bundle of sessions — e.g. 10 lessons for €200. The client pays for the package upfront (or in instalments).

- Set the **Unit price** (price per session) and the number of sessions in the term
- Zooza calculates the total; you collect it as a one-off payment or in instalments via a payment template

**Per-session pricing**
The client pays for each session as they attend, with no upfront commitment.

- Set **Programme type** to *Pay-as-you-go* instead
- Each session the client books creates a payment obligation
- If they cancel, the payment obligation resets to zero
- Good for clients who want maximum flexibility, but harder to predict revenue

> Most language schools and personal trainers use package pricing. It commits the client, simplifies billing, and means fewer individual transactions to track.

### 3. Collect interest before setting a schedule

Individual lesson clients often cannot commit to a fixed weekly slot until they have spoken to the instructor. Use Zooza to collect their registration first, then build the schedule.

- Create a **Class** under the Programme without adding sessions yet — this gives you a booking record and a client profile without showing a public timetable
- The client registers their interest online
- Once you agree a schedule with them, add the sessions manually to their private class

This is also useful if your instructors have variable availability — no need to publish anything until it is confirmed.

### 4. Free first session

If you offer a free trial or introductory session before the client buys a package:

- Enable **Trial** in Programme settings and set the trial price to 0
- The trial creates a separate registration — after the session, the automated follow-up email fires
- Use `*|BOOKING_URL|*` in the follow-up email to link directly to the package booking form
- Once the client books the package, their sessions continue in the same class

Alternatively, include one free session inside the package itself — e.g. "11 sessions, you pay for 10". Set this up using a discount or by adjusting the package session count.

### 5. Schedule sessions

Once you have agreed dates with the client, add sessions to their private class:

- Go to the Class → Sessions → add sessions individually or in a batch
- Each session has its own date, time, and instructor
- Sessions do not need to follow a fixed weekly pattern — add them as and when they are agreed

If the same instructor works with multiple clients, create a separate private Class per client under the same Programme. The instructor sees all their sessions in the calendar.

---

## Payment options for packages

| Approach | How to set it up | When to use it |
|---|---|---|
| **Full upfront** | One-off payment for the full package price | Client commits and pays everything at booking |
| **Instalments** | Term payment split into monthly payments via a payment template | Package spans several months, client prefers to spread the cost |
| **Per session** | Pay-as-you-go programme type | Client wants no upfront commitment; you charge after each session |

See [Payment templates](../guides/payment-templates-creation.md).

---

## Tracking sessions and remaining lessons

For package clients, you need to know how many sessions they have used and how many remain.

Mark each session as attended or missed in the Sessions view. The full attendance history is visible on the client's booking. For a 10-session package, count attended sessions against the total — the booking shows you the picture.

---

## Make-up lessons

If a client misses a session, you can offer a make-up. For individual lessons this is usually a manually scheduled replacement session — add it to their class at a new date. Automated make-up credit works best for group classes. For 1-to-1, manual scheduling is the norm.

---

## What Zooza does not support (for this model)

| Limitation | Workaround |
|---|---|
| Clients self-booking individual session slots from a shared instructor calendar | Add sessions manually after agreeing a time with the client |
| Automatic detection of instructor availability for self-scheduling | Not available — schedule sessions manually |
| Rolling over unused sessions from one package to the next automatically | Adjust the block balance manually when a new package is purchased |

---

## Common mistakes

- **Creating one shared class for all individual clients** — each client should have their own private class. Mixing clients in one class makes attendance tracking and billing impossible to follow.
- **Publishing the class publicly before confirming the schedule** — individual lesson classes should stay invisible to the public. Set visibility to *hidden* or *admin only* until you are ready.
- **Using Membership price type for packages** — Membership charges a recurring fee indefinitely. For a 10-session package, use One-off payment or Term payment with a defined end point, not Membership.
- **Skipping the trial flow** — if you always do a free first session informally, consider setting it up as a proper trial in Zooza. It creates a record, triggers the follow-up email automatically, and makes the conversion to a paid package traceable.
