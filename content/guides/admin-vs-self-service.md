---
title: "When to enrol clients yourself vs. send them a booking link"
description: "Understand when to use the admin booking flow and when to send clients your online booking link — and why Zooza is designed around client self-registration."
slug: "admin-vs-self-service"
type: "guides"
product_area: "Bookings"
sub_area: ""
audience: ["admin"]
tags: ["booking", "self-service", "registration", "admin", "booking link", "onboarding", "paradigm"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-05-11"
---

# When to enrol clients yourself vs. send them a booking link

One of the most common questions from new Zooza users is: *"Why can't I just add clients to a class myself? Why do I have to send them a link?"*

The short answer: you *can* enrol clients manually. But Zooza is designed around a different model — one where you set the rules and clients manage themselves. Understanding when each approach is right will save you a lot of admin time.

---

## The core difference

| | You enrol the client | Client self-registers |
|--|---------------------|----------------------|
| **Who does the work** | You | The client |
| **Client receives** | Notification of their booking | Full registration journey: form, confirmation, payment |
| **Payment collected** | You add it manually afterwards | Collected automatically on booking |
| **Consent and data** | You type in their details | Client enters their own details and accepts terms |
| **Best for** | Bulk transfers, exceptions, correcting mistakes | All normal new registrations |

---

## When to use the booking link (most of the time)

Send clients your online booking link for:

- **New registrations** — any first-time client joining a class
- **Trials** — clients must book trials themselves (admin cannot create trial bookings manually)
- **Term renewals** — if using auto-enrolment, clients receive a link to confirm their spot
- **Re-enrolments** — returning clients signing up for a new term

The booking link handles everything: form submission, payment collection, confirmation email, and consent. You don't need to do anything until the booking appears in your list.

**How to find your booking link:**
Go to the Programme → click the booking link icon or copy the URL shown on the class tile. See [Share your booking link](booking-form-settings.md) for details.

---

## When to enrol a client manually

Some situations genuinely require admin action:

**Bulk term transfers (copy bookings)**
When starting a new term, you can copy all existing bookings from the old class to the new one in one step. This is the recommended approach for term rollovers — not sending everyone a link.
See [Run a term reset](term-rebooking-guide.md).

**Corrections and exceptions**
- A client paid offline (bank transfer, cash) and you need to create their booking immediately
- A client's booking was cancelled by mistake and needs to be reinstated
- You're onboarding a group of clients simultaneously from a spreadsheet (use [Client import](client-import.md))

**Back-office entries**
- Creating a booking for a client who has no internet access or cannot complete the form themselves
- Adding a staff member, instructor, or internal test booking

**What manual enrolment doesn't do:**
When you create a booking manually, payment is *not* collected automatically. You'll need to record any payment separately on the booking. The client also won't go through the booking form — so any custom questions you've added won't be answered.

---

## What happens if you do everything manually

Some operators start by manually creating every booking — especially those migrating from systems where admin controlled everything. This works, but it creates more work, not less:

- You have to manually record every payment
- You have to manually send confirmation emails
- You have to handle every re-registration at term end
- Clients don't learn to use the portal themselves — so they contact you for everything

Zooza is designed to reduce this. The goal is: clients self-register, payments run automatically, you step in only for exceptions.

---

## The one thing you cannot do manually: create a trial

Trial bookings must be submitted by the client via the booking form. You cannot create a trial on behalf of a client.

If a client wants to try a class but can't use the form:
1. Send them the booking link directly.
2. If they still can't book, create a regular booking (not a trial) and convert it to trial status afterwards — see [Convert an existing booking to trial](trials-daily-business.md#how-to-convert-an-existing-booking-to-trial-status).

---

## Summary: the decision

```
New client wants to join?
  └── Is it a trial? → Send booking link (required)
  └── Is it a normal registration?
        └── Will they book themselves? → Send booking link (preferred)
        └── Exception / bulk / no internet? → Create manually, add payment separately
```

---

## Related guides

- [Create a booking manually](creating-a-booking.md)
- [Run a term reset — move all clients to a new term](term-rebooking-guide.md)
- [Manage trial bookings](trials-daily-business.md)
- [Import clients from a spreadsheet](client-import.md)
- [Booking form settings](booking-form-settings.md)
