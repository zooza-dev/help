---
title: "Prepare your programmes for the new school year"
description: "A step-by-step checklist to roll over your Zooza programmes, classes, billing periods, and bookings at the end of a term or school year."
slug: "prepare-new-school-year"
type: "guides"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: ["programme", "class", "new season", "school year", "copy", "billing period", "auto-enrolment", "term transition"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-08-07"
related_articles: ["copy-programme-and-class", "new-programme-existing-clients", "auto-enrollment", "billing-periods", "archive-or-delete-programme"]
---

# Prepare your programmes for the new school year

Use this checklist at the end of each school year or term to roll your programmes forward in Zooza. The order matters — set up the structure before copying clients.

## Step 1 — Review what's continuing and what's ending

Go through your active programmes and classes and decide:

- Which **classes** run again next year (same programme, new dates)?
- Which **programmes** stay as-is but need new billing periods?
- Which **programmes or classes** are finished and should be archived?

It helps to do this in a spreadsheet or notes before touching anything in Zooza.

## Step 2 — Create new billing periods (if you use them)

If your classes are organised by term blocks (billing periods), set up the new year's periods before you create any new classes.

1. Go to **Settings → Billing Periods**.
2. Add a billing period for each term block in the new year (e.g. September–December, January–April, May–June).
3. Save each period.

The billing periods must exist before you can assign them to classes. See [Billing Periods](../setup/billing-periods.md) for full setup details.

## Step 3 — Copy your continuing classes

For each class that runs again in the new year:

1. Open the programme and find the class.
2. Click **Copy** on the class.
3. Update the class name (remove "Copy" suffix, add year or term label if useful).
4. Set the new **start date** — Zooza will shift the session schedule automatically.
5. Assign the new **billing period** if applicable.
6. Preview the new sessions to confirm dates.
7. Decide whether to **copy bookings**:
   - **Yes, copy bookings** — use this when most clients are continuing. You can delete individual bookings afterwards for anyone not returning.
   - **No, start empty** — use this when you want clients to re-enrol via the widget.

> **Copying bookings ≠ transferring bookings.** Copied bookings start clean — no payment history, make-up credits, or attendance carry over. The original booking stays accessible to the client. If you need to move a client while keeping their payment history, use Transfer instead.

See [Copy a programme or class](copy-programme-and-class.md) for the full copy walkthrough.

## Step 4 — Set up auto-enrolment (optional)

If you want clients to be offered auto-continuation at the end of the current billing period:

1. Open the class.
2. Go to **Class Settings → Auto-enrolment**.
3. Enable **Auto-enrolment** and set how many days before the period end date the continuation email fires.
4. Choose whether continuation is automatic (opt-out) or requires client confirmation (opt-in).

The continuation email fires N days before the billing period **end date**, not based on session count or attendance. See [Auto-enrolment](../setup/auto-enrollment.md).

## Step 5 — Archive or deactivate finished classes

For classes and programmes that are not continuing:

- **Archive** a programme or class to hide it from the admin list without deleting data. Clients still see their booking history.
- **Disable online registration** on any class you want to stop accepting new enrolments for.
- Do not delete classes unless you are certain the data is no longer needed.

See [Archive or delete a programme](archive-or-delete-programme.md).

## Step 6 — Update widget visibility

If you use the booking widget on your website:

1. Check that new classes have **Online Registration** enabled (so they appear in the widget).
2. Check that finished or full classes have **Online Registration** disabled (so they no longer appear).

This is controlled per class under **Class Settings → Online Registration → Show in online registration**.

## Step 7 — Set up or update payment templates

If prices change for the new year, update or create new payment templates:

1. Go to **Settings → Payment Templates**.
2. Create new templates for the new year's pricing if needed.
3. Activate the correct template on each programme under **Programme Settings → Payment**.

See [Payment templates](../guides/payment-templates-creation.md) for the three-step activation flow.

## Step 8 — Communicate with clients

Once your new classes are ready, let your clients know:

- Send a **bulk email** from **Communication → Compose** to active clients announcing new enrolments.
- If you copied bookings, no extra communication is strictly needed — clients will receive their usual automated confirmation. But a personal note about the new year goes a long way.
- If you're running auto-enrolment, the system emails clients automatically — make sure the template text is up to date.

## Quick reference

| Task | Where in Zooza |
|------|----------------|
| Add billing periods | Settings → Billing Periods |
| Copy a class | Programmes → open class → Copy |
| Enable auto-enrolment | Class Settings → Auto-enrolment |
| Archive a class | Class settings → Archive |
| Update widget visibility | Class Settings → Online Registration |
| Create payment templates | Settings → Payment Templates |
| Send client announcement | Communication → Compose |

## Related

- [Copy a programme or class](copy-programme-and-class.md)
- [Billing Periods](../setup/billing-periods.md)
- [Auto-enrolment](../setup/auto-enrollment.md)
- [Archive or delete a programme](archive-or-delete-programme.md)
- [Payment templates](../guides/payment-templates-creation.md)
- [New programme with existing clients](new-programme-existing-clients.md)
