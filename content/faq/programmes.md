---
title: "FAQ — Programmes"
description: "Programmes can be deleted from Programme Settings — soft delete with 30-day Trash recovery. Use Archive to hide without removing data."
slug: "faq-programmes"
type: "faq"
product_area: "Programmes"
audience: ["admin"]
tags: ["programme", "class", "archive", "delete", "venue", "price", "rename", "trial", "auto-continuation"]
status: "published"
last_converted: "2026-03-14"
---

# FAQ — Programmes

---

## Can I delete a Programme?

Yes. Admins with the **edit_course** permission can delete a programme directly from **Programme Settings → Edit → Delete programme**.

Deletion is a **soft delete** — the programme moves to **Settings → Tools → Trash** and can be restored within 30 days. After 30 days it is permanently removed.

If you want to hide the programme without losing any data, use **Archive** instead — it is reversible at any time.

See [Archive or delete a programme](../guides/archive-or-delete-programme.md) for the full walkthrough.

---

## How do I archive a Programme?

1. Go to **Programmes** and click the Programme name.
2. Go to **Programme Settings → Edit**.
3. Tick **Archive** and click **Save**.

The Programme disappears from your active list. To find it later, use the **Archived** filter in the Programmes list.

To restore: open the archived Programme, go to Programme Settings → Edit, uncheck **Archive**, and save.

---

## Can I delete a Class (class)?

A Class with active bookings cannot be deleted. You can:

- **Archive it** — hides it from the active list, bookings remain intact.
- **Transfer bookings** to another Class first, then delete the empty Class.

---

## Can I remove a location (venue) from a Class?

No. A Class always requires a Venue — it cannot be left blank.

The solution is to create a **placeholder Venue** in **Settings → Locations** (e.g. name it "Online", "TBD", or anything neutral). Assign this placeholder to the Class. Whatever name you give it is what clients will see.

Do not delete the original Venue from Settings if it is used by other Classes.

---

## Can I rename a Programme?

Yes. Go to the Programme, open **Programme Settings → Edit**, change the name, and save. All settings and bookings remain unchanged.

---

## How does Class pricing work? What if Programme and Class have different prices?

Price hierarchy:

- If a **Class has a price set** (any value other than 0) → the Class price is used, overriding the Programme price.
- If a **Class has no price set** → the Programme price is used.
- **Important edge case:** Setting `0` at Class level is treated as "not set" — the system falls back to the Programme price. You cannot make a single Class free by setting 0 at Class level if the Programme has a price.

**To make a specific Class free (0 €):**

1. Set the Programme price to 0, then manage different prices at Class level — or
2. Move the Class into a separate Programme with no price, and set 0 at Class level — or
3. Use the **Zooza Trial** feature, which has its own independent price (can be 0), separate from Programme pricing entirely.

---

## What is the difference between a Zooza Trial and a manually created "trial session"?

These are completely different things:

**Zooza Trial (feature):**
- A dedicated functionality in Zooza that makes specific Classes available for prospective clients to try.
- Has its own booking form, its own price (can be 0 €), and its own automated follow-up flow.
- Tracks status: Trial Started → Trial Won / Trial Lost.
- Published separately via the widget.
- After attendance is recorded, the client automatically receives an invitation to enrol.

**Manually created session (not using the Trial feature):**
- A regular Session that an admin created and named "trial" or "demo".
- No automated tracking, no automated follow-up, no Trial status.
- Pricing follows normal Class/Programme rules.

If you are unsure which applies to your setup, check whether there is a dedicated Trial form/funnel set up in your account.

---

## How does Auto-enrolment work?

Auto-enrolment is a Zooza feature that contacts clients before their current Class ends and invites them to re-enrol.

How it works:
1. A configurable number of days before the Class end date, the client receives a notification.
2. The client receives a **personalised link** leading to their Client Profile.
3. From there, they select which Class they want to continue into.
4. Once confirmed, a new booking is created for the selected Class.

**Important:** No booking is created automatically. The client must actively open the link and confirm their choice. If they do not respond, nothing happens.

> For Trials: auto-enrolment is triggered when the instructor records attendance on the last Trial session.

## I sent auto-enrolment invitations before adding future classes — can I resend them?

No. Auto-enrolment invitations are not re-sent automatically when you later update the available classes. The system sends the invitation once, at the configured number of days before the class ends.

**What you can do:**

1. Add the future classes to the auto-enrolment settings (Programme → Automations → Auto-enrolment → Edit → select the classes to offer).
2. Manually contact the clients who expressed interest via **Communication → Send Email** — select the relevant class or bookings as the target, and include a direct link to the new class.

Clients who have already received the invitation and visited their Client Profile will see the updated class list the next time they open the link, as long as the invitation link is still valid.

---

## Where can I see who accepted, declined, or has not yet responded to an auto-enrolment invitation?

There are two places:

**1. Auto-enrolment responses page** — Go to **Programmes → Auto-enrolment responses** (`/#retention_responses`). This shows every invited client with their response status (Accepted / Declined / Not decided yet), any note they left when declining, and a **Reviewed** tracking flag.

**2. Bookings list** — Go to **Bookings** and use the **Auto-enrolment** filter in the sidebar. Options: All / Auto-enrolment Accepted / Auto-enrolment Declined / Not decided yet.

Use the Bookings list when you need bulk export or bulk email. Use the responses page when you want to work through responses one by one and track what you have already acted on.

See also: [Monitoring auto-enrolment responses](../guides/auto-enrolment-responses.md)

---

## What does "Mark as reviewed" do on the Auto-enrolment responses screen?

It is an admin bookkeeping flag. Go to **Programmes → Auto-enrolment responses** (`/#retention_responses`). Each client row shows a **Reviewed** column (Yes / No). Clicking **Mark as reviewed** sets that row to Yes.

It has no effect on the client or their booking. It is purely for your own tracking — so you can work through the list and record which responses you have already acted on, without accidentally processing the same one twice.

---

## A client accepted auto-enrolment — does a booking get created automatically?

No. Accepting the invitation is the client's signal that they want to continue — it does not create a new booking automatically.

To complete their enrolment, either:

- Let the client complete the booking themselves via their invitation link (they select the class and confirm), or
- Create the booking for them manually: open their current booking → **Copy booking** → select the new class.

---

## Can I copy only the clients who accepted auto-enrolment into a new class?

Not in one click, but the workflow is straightforward:

1. Go to **Bookings** and filter by **Auto-enrolment: Auto-enrolment Accepted** and the relevant Programme / Class.
2. Review the list — these are the clients who confirmed they want to continue.
3. For each client, open their booking and use **Copy booking** to place them into the new class.

Alternatively, if you want to move all accepted clients at once, use **Bookings → Bulk actions** after filtering.

---

## What link should I send parents to sign up after a trial?

Send them to the **specific Class or Programme page**, not to the general class list or client portal.

A direct link to the specific Class gives parents the schedule, pricing, and enrolment form in one place with no extra steps.

The client portal is for existing clients managing bookings — it is not a good entry point for new sign-ups.

You can also use the `*|BOOKING_URL|*` dynamic tag in trial follow-up emails to generate a pre-filled personalised booking link.

---

## Is the first month's payment reduced if a client joins mid-month?

This depends on your **aliquot setting**:

- **Aliquot ON** — the first payment is automatically reduced based on the number of remaining sessions in the month. The client pays a pro-rata amount.
- **Aliquot OFF** — the client pays the full monthly amount regardless of when they join.

You can also use the **"Include Initial Full Scheduled Payment"** setting to control whether the client pays the pro-rata amount only, or the pro-rata amount plus one full period upfront.
