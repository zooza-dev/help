---
title: "Online and Hybrid Classes"
description: "Online delivery is a setting on a **Class** or **Session**, not a different programme type. You set up the Programme exactly as you would for an..."
slug: "online-and-hybrid-classes"
type: "business-model"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: ["business-model", "online", "hybrid", "zoom", "google-meet", "webinar", "livestream", "virtual"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-04-09"
---

# Online and Hybrid Classes

## This guide is for you if

- You run classes fully online — clients join via Zoom, Google Meet, or another video platform
- You run hybrid classes — some clients attend in person, others join online at the same time
- You run webinars or live workshops with a large audience and no physical venue
- You want the meeting link to appear automatically in confirmation emails and session reminders — without sending it manually each time
- This applies on top of any business model: group blocks, subscriptions, individual lessons, or drop-in

---

## Online classes are not a separate programme type

Online delivery is a setting on a **Class** or **Session**, not a different programme type. You set up the Programme exactly as you would for an in-person equivalent — the only difference is that the venue is replaced by (or supplemented with) a meeting link.

This means all the payment models, trial flows, and booking setups from the other business model guides apply. You just add the online meeting layer on top.

---

## Setting up a fully online class

### 1. Create a virtual location

Go to **Settings → Locations** and create a location called "Online" (or "Zoom", "Virtual classroom", whatever suits your brand). You do not need a physical address.

Assign this location to the Class. This is what clients see when they look up where the class takes place.

### 2. Add the meeting link to the Class

In the Class settings, add the **online meeting URL** — your Zoom, Google Meet, or Teams link. This is the link that will be included automatically in emails.

If your meeting link is the same every week (a permanent Zoom room), add it once at Class level. If the link changes per session (e.g. you generate a new Zoom link each week), add it at Session level instead.

### 3. Include the link in email templates

Zooza does not add the meeting link to emails automatically — you need to add the dynamic tag to your email templates once.

In your **session reminder** template, add:

- `*|ONLINE_MEETING_LINK|*` — renders as a clickable "Join meeting" link (class-level link)
- `*|EVENT_ONLINE_MEETING_LINK|*` — renders as a clickable link for the specific session (use this if links vary per session)

You can also use `*|HAS_ONLINE_MEETING|*` as a conditional — so the link section only appears when a meeting is attached, and does not show for in-person sessions if you use the same template for both.

Once the template is updated, every session reminder going forward includes the link automatically. No manual sending.

See [Dynamic tags](../guides/dynamic-tags.md) for the full tag reference.

---

## Hybrid classes — in-person and online at the same time

A hybrid class has both a physical venue and an online meeting link. The same session, two ways to attend.

Setup:
- Assign a real **location** to the Class (the physical venue)
- Also add the **online meeting URL** to the Class
- In your session reminder template, include both the venue information (`*|PLACE_NAME|*`, `*|PLACE_DIRECTIONS|*`) and the meeting link (`*|ONLINE_MEETING_LINK|*`)

Clients who attend in person see the venue. Clients joining online see the link. Both get the same reminder — all the relevant information is there.

**Capacity** — Zooza tracks one capacity per class. If you want to limit online and in-person spots separately, create two separate Classes under the same Programme: one for in-person, one for online. Clients choose at booking which format they want.

---

## Webinars and large online events

For a one-off online event — a webinar, a live workshop, a Q&A session — use the **One-off event** programme type rather than an ongoing group class.

- **Programme type:** *One-off event*
- Add the session date and the meeting link
- Set capacity if you want to limit attendance
- Price: free (registration fee of 0) or paid

The booking flow is the same as any other programme — clients register, pay if required, and receive a confirmation with the meeting link via the session reminder template.

For recurring webinar series (e.g. a monthly live session), use *Booking for the full programme duration* and generate sessions monthly. Add the meeting link at session level if each webinar has a different link.

---

## Per-session meeting links

If your meeting link changes every session — common when generating Zoom links on demand — add the link at **Session level** rather than Class level:

1. Go to the Class → Sessions
2. Open a specific session
3. Add the meeting URL for that session

Use `*|EVENT_ONLINE_MEETING_LINK|*` in the reminder template to pull the session-specific link. If both a class-level and session-level link exist, the session-level link takes priority.

---

## What Zooza does not support (for this model)

| Limitation | Workaround |
|---|---|
| Automatically generating Zoom links and attaching them to sessions | Generate the link in Zoom/Meet and paste it into the session manually |
| Native video streaming inside Zooza | Use an external platform (Zoom, Meet, Teams) and share the link via dynamic tags |
| Separate capacity limits for online vs in-person within one class | Create two separate Classes: one for in-person, one for online |

---

## Common mistakes

- **Not adding the meeting link to the reminder template** — clients register and receive a confirmation, but no link. They email you the day before asking how to join. Add `*|EVENT_ONLINE_MEETING_LINK|*` to the session reminder template before you go live.
- **Using a class-level link when links change per session** — if you generate a new Zoom link every week, the class-level link becomes outdated. Use session-level links and `*|EVENT_ONLINE_MEETING_LINK|*`.
- **No virtual location set** — without a location on the class, the booking confirmation and calendar entry look incomplete. Create a simple "Online" location and assign it.
