---
title: "Run a term reset — move all clients to a new term"
description: "A step-by-step guide for setting up a new term, copying your class structure, rolling clients over, handling price changes, and archiving the old classes."
slug: "term-rebooking-guide"
type: "guides"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: ["term", "rebooking", "copy", "auto-enrolment", "new season", "programme", "class", "transfer", "payment"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-05-11"
---

# Run a term reset — move all clients to a new term

At the end of each term, you need to set up new classes and give existing clients the chance to re-enrol. This guide covers the full process from start to finish.

> **Before you start:** Decide whether to do this yourself or invite clients to self-enrol. Both approaches work — see [Which approach to use](#which-approach-to-use) below.

---

## Which approach to use

| | Admin copies bookings | Auto-enrolment invite |
|--|----------------------|-----------------------|
| **What it does** | You copy all bookings to the new class in bulk. Clients start the term automatically. | You invite clients to confirm their own spot via a pre-filled link. |
| **Best for** | Classes where nearly everyone continues | Classes with high churn or where clients need to choose a new time slot |
| **Client action required** | None (or just payment) | Clients must click the link and confirm |
| **Risk** | You may copy clients who don't actually continue | Clients who don't click don't get enrolled — you'll need to follow up |

Most businesses use **admin copies bookings** for the main group, then clean up non-renewals afterwards. Auto-enrolment is useful when you're offering clients a choice of new time slots.

---

## Step 1 — Set up the new class structure

Before you can enrol anyone, the new term's classes need to exist.

### Option A: Copy an existing class (recommended)

1. Go to **Programmes** and open the programme.
2. Find the class you want to copy and click **Copy**.
3. Set the new start date — Zooza shifts all sessions forward by the same gap, keeping the same day of week and time.
4. Review the session list in the preview and adjust any sessions that fall on holidays.
5. Set capacity, instructor, and location if they're changing.
6. Click **Create**.

> See [Copy a programme or class](copy-programme-and-class.md) for full details on copy options.

### Option B: Create a new class from scratch

Use this if the term structure is significantly different from the previous one.

1. Inside the programme, click **New class**.
2. Set the dates, time, location, and instructor.
3. Review the generated session list.

> See [Create a class](creating-a-class.md) for the full walkthrough.

### Adjust prices for the new term

If your prices are changing, edit the price on the new class before enrolling anyone:

1. Open the new class.
2. Go to the **Price** tile and click **Edit**.
3. Update the price.
4. Save — this sets the price for all new bookings on this class.

> Changing the price on the class does **not** affect existing bookings from previous terms. It only applies to new enrolments in this class.

---

## Step 2 — Roll clients over

### Approach A: Admin copies bookings in bulk

1. Open the **old class** (the one that's ending).
2. Click **Copy** on the class.
3. Under **Copy bookings**, enable the option to copy existing bookings.
4. Select **Only confirmed bookings** to exclude trials and cancelled registrations.
5. Review the list — deselect any clients you know are not continuing.
6. Confirm.

**What happens:**
- Each client gets a new booking on the new class.
- The new booking starts clean — no payment history, no make-up credits from the old term.
- The old booking remains intact and accessible to the client in their profile.
- Clients receive a notification that they've been enrolled in the new class.

> **Note:** If a client has already paid for the new term in advance (e.g. via bank transfer), add their payment manually to the new booking after copying. Do not transfer payment history — start clean and record fresh.

### Approach B: Send auto-enrolment invite

Use this when clients need to choose their new slot, or you want them to actively confirm before they're enrolled.

1. Create the new classes first (Step 1).
2. Go to **Programme** → **Auto-enrolment** → **Edit**.
3. Select the new classes you want to offer.
4. Choose **Suggest classes** for group programmes.
5. Go to the old class → **Bookings** → select all active bookings → **Send auto-enrolment**.
6. Clients receive a pre-filled email with a link to complete their enrolment.

> See [Auto-enrolment responses](auto-enrolment-responses.md) for how to track who has and hasn't responded.

---

## Step 3 — Handle non-renewals

After copying bookings, some clients won't be continuing. Deal with them promptly so your capacity shows correctly.

1. Go to the new class → **Bookings**.
2. Find clients who have confirmed they're not returning.
3. Open each booking and click **Cancel booking** or change the status to **Cancelled**.

If you're using auto-enrolment and a client hasn't responded by your deadline:
- Either enrol them manually and send a reminder, or
- Leave them unenrolled and mark their old booking as closed.

---

## Step 4 — Communicate to clients

Clients enrolled via admin copy receive an automatic notification. You may want to send an additional email with:
- New term dates and any schedule changes
- Updated price if it changed
- Payment instructions (especially if you use bank transfer or GoCardless)
- How to cancel if they're not continuing

Go to the new class → **Bookings** → **Send email** to reach all enrolled clients at once.

> See [Send email to a class](sending-email-sms.md) for the full guide.

---

## Step 5 — Archive the old class

Once the old term has ended and all clients are on the new one:

1. Open the old class.
2. Click **Archive** (or set an end date in the past).
3. The class disappears from your active view but remains in the history.

Do not delete classes that have payment records — archiving is the right action. Clients can still see their old booking and payment history in their profile.

> See [Archive or delete a programme](archive-or-delete-programme.md) for details.

---

## Common questions

**Can I copy only some bookings, not all?**
Yes — when copying a class with bookings, you can deselect individual clients from the list before confirming.

**What happens to make-up credits from the old term?**
Make-up credits stay on the old booking. They don't transfer to the new booking automatically. If you want to honour them in the new term, contact support or handle it by adjusting the payment on the new booking manually.

**A client paid for the old and new term together — what do I do?**
Record their old-term payment on the old booking and their new-term payment on the new booking. Don't try to split or move payment records between terms — start fresh on each booking.

**Can I change the price for just one client?**
Yes — after copying bookings, open that client's individual booking and edit the payment amount directly. This doesn't affect other clients' prices.

**My class has multiple groups (e.g. different levels). Do I need to copy each one separately?**
Yes — copy each class individually. This takes a few minutes but gives you full control over which clients move to which level.

**I use GoCardless. Will payment mandates carry over?**
GoCardless mandates are linked to the client, not the booking. When you create a new booking for a client, their existing mandate applies automatically if it's still active. Check that mandates haven't expired (they last 90 days from last use) before the first payment runs. See [GoCardless connection lifecycle](gocardless-connection-lifecycle.md).

---

## Related guides

- [Copy a programme or class](copy-programme-and-class.md)
- [Transfer and copy bookings](transfer-and-copy-bookings.md)
- [Auto-enrolment responses](auto-enrolment-responses.md)
- [Archive or delete a programme](archive-or-delete-programme.md)
- [Send email to a class](sending-email-sms.md)
- [GoCardless connection lifecycle](gocardless-connection-lifecycle.md)
