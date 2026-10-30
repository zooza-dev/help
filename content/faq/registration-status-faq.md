---
title: "Registration statuses — what each one means"
description: "A complete reference for every registration status in Zooza: what it means, when it is set automatically, and what to do when a status seems wrong."
slug: "registration-status-faq"
type: "faq"
product_area: "Bookings"
sub_area: ""
audience: ["admin"]
tags: ["registration", "booking", "status", "pending", "awaiting-payment", "cancelled", "lost", "active"]
status: "published"
related_articles: ["trash-and-restore", "trials-daily-business", "auto-cancel-unpaid-registrations"]
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-10-30"
---

# Registration statuses — what each one means

## Status overview

| Status | What it means | Capacity held? | Client receives emails? |
|---|---|---|---|
| **Enrolled** | Active registration — client is attending | Yes | Yes |
| **Pending** | Registration submitted but not yet confirmed (e.g. waiting for payment or admin approval) | Yes | Limited |
| **Awaiting payment** | Registration is active; a payment is due but within the grace period | Yes | Payment reminders |
| **No debt** | Registration is free — nothing is owed, ever | Yes | None |
| **Waiting list** | Class is full; client is queued for a spot | No (or minimal) | Notification when spot opens |
| **Trial started** | Client booked a trial session | Depends on settings | Trial follow-ups |
| **Trial lost** | Trial closed without enrolment | No | None |
| **Cancelled** | Registration was cancelled; record still exists | No | None |
| **Deleted (Trash)** | Moved to Trash; recoverable within 30 days | No | None |

---

## The booking header tells you whether it is actually running

Since the end of October 2026 the top of a booking carries a plain-language state, which
is a different question from its payment status. A booking can be fully paid and still
not be running.

| Header says | What it means | What to do |
|---|---|---|
| **Active** | The booking is running now | Nothing |
| **Not started yet** | The class has not begun | Nothing — this is normal before term |
| **Finished** | The class is over | Nothing |
| **Not active** | *"The class or programme is archived, so this booking no longer runs."* | If that is wrong, unarchive the class |
| **Lead collection, class not started yet** | *"This class collects leads and is not running yet."* | Enrol them into a running class, or activate this one |

Where something can be done about it, the header offers it. A booking sitting on a class
with room shows *"A slot is free in this class. Enroll to confirm the booking, or move it
to another class."* One with no room shows *"No free slot in this class right now."* And a
finished trial shows *"Enroll to continue"* with the warning that **changing the status
does not enrol anybody** — the thing admins most often get wrong here.

The header also shows **Paid via booking** when another booking in a
[linked group](../guides/linked-bookings.md) is paying for this one, and a **Book a
session** action where that applies.

> **Read the header before the status.** Most "the client says they are enrolled but
> nothing is happening" questions are answered by it in one line, usually *Not active* on
> a class somebody archived.

### Every action moved into the header

The same rebuild took the actions off the Registration card and put them in the header,
where the most useful one for the current state is the main button. On a booking waiting
for a trial date that is **Choose trial date**; on most others it is **Enrol**.

The rest — **Copy**, **Transfer to another class**, **Network transfer**, **Cancel**,
**Delete** — are beside it or under **More**. **Change status is always under More**,
never a main button, which is the single most common "the button has disappeared"
report since the change. The booking's sections became tabs at the same time.

> If a colleague describes a button that is no longer where they remember it, this is
> almost certainly why. Nothing was removed.

## What does "Pending" mean?

**Pending** means the registration has been submitted but is waiting for something before it becomes fully active. Common triggers:

- The client started the booking form but has not yet paid the required deposit or first instalment.
- The programme requires admin approval before confirming the booking.
- An import created the registration without a completed payment flow.

**What to do with Pending registrations:**

- If the client has paid: check whether the payment was matched to the correct booking. An unmatched payment may leave the registration stuck in Pending.
- If the client has not paid: the registration will either resolve itself when payment arrives, or it will be automatically deleted after the grace period (if auto-delete is enabled in your programme settings).
- If you want to confirm it manually: open the booking → **Change status → Enrolled**.

---

## What does "Awaiting payment" mean?

**Awaiting payment** means the registration is active and a payment is due, but the client is still within the grace period — the payment is not yet overdue. This is an informational state, not a warning: the client is not in arrears yet. In the client-facing profile widget it shows in **blue** (not orange) to reflect this.

The status moves to **Unpaid** (or triggers a payment reminder) when the grace period passes without payment.

This status does **not** automatically cancel the booking. Whether the booking gets cancelled for non-payment depends on your programme's **payment reminder and auto-delete settings**.

## A booking exists but nothing was paid — did something go wrong?

Almost certainly not. **The payment follows the booking, because the booking has to exist
before there is anything to pay for.** The parent fills in the form, the booking is
created, and only then are they sent to the payment step. If their card fails, or they
get distracted and close the tab, the booking is still there — which is what you want,
because they can come back and pay without filling the form in again.

So an unpaid booking on your list is not evidence of a broken checkout. It is a parent
who has not finished yet.

**There is no setting that refuses to create the booking until payment succeeds.** What
you control is what happens next: payment reminders, and whether unpaid bookings are
deleted automatically after a while. Both are set per programme — see
[Automatic payment reminders](../guides/automatic-payment-reminders.md).

**When it is worth a closer look:** many parents in a row stopping at the same point.
That is usually the payment page rather than the booking — a card gateway not finishing,
or a site served over `http://`, which Stripe refuses. See
[Stripe payments FAQ](stripe-payments-faq.md).

## What does "No debt" mean?

**No debt** means the registration is completely free — no payment has ever been or will ever be owed on it. The Payments tab is hidden in the client profile widget for these registrations because there is nothing to pay or display. If accessed directly, the payments screen shows an informational "nothing to pay" state instead of a payment list.

**If the status did not change after the client paid:**

1. Check if the payment was matched — go to the booking → **Payments** and confirm the payment shows as received.
2. If GoCardless or email-notification matching is used, there may be a sync delay of up to 24 hours.
3. If the payment is not matched, match it manually from the Payments screen.

---

## Why is a registration still "Awaiting payment" after GoCardless collected it?

GoCardless Direct Debit and GoCardless bank reading (inbound matching) are two separate systems:

- **Direct Debit:** Zooza pulls money from the client's account automatically. This requires an active mandate AND offline charging enabled on the payment plan.
- **Bank reading (inbound):** GoCardless reads your business bank account and forwards incoming transfers. This syncs once per day.

If the payment was collected via Direct Debit but the status has not updated, the collection may still be processing (typically 2–3 business days for SEPA Direct Debit to settle). If it has been longer than 5 days, check the payment in your GoCardless dashboard.

---

## What does "Cancelled" mean — and is it the same as deleted?

No. **Cancelled** and **Deleted** are different:

| | Cancelled | Deleted (Trash) |
|---|---|---|
| Where to find it | Registrations list — use status filter "Cancelled" | Settings → Tools → Trash |
| Can it be undone? | Yes — change status back to Enrolled | Yes — within 30 days |
| Permanently gone? | No (unless you delete it afterwards) | After 30 days |

A cancelled registration still exists in the system and can be reactivated. A deleted registration is in the Trash and needs to be restored from there.

See [Recover deleted registrations, classes, and sessions](../guides/trash-and-restore.md) for the full restore workflow.

---

## A registration disappeared — where is it?

**It has not been destroyed.** A registration cannot be permanently removed from Zooza — even a deleted one stays visible, so it is always possible to trace what happened to it. Start from that, because it makes the search short.

Almost every report of vanishing registrations turns out to be an automation:

1. Check the **Trash** and the deleted-registrations view — see [Recover deleted registrations](../guides/trash-and-restore.md).
2. Check your **unpaid-booking automation**. If it cancels or deletes unpaid registrations, one that was paid late, or paid manually after the automation ran, will already have been acted on. See [Auto-cancel unpaid registrations](../guides/auto-cancel-unpaid-registrations.md).
3. Check whether a **waitlist automation** moved it rather than removed it — see [Waiting list FAQ](waiting-list-faq.md).

If you report this to support, send **one concrete registration** rather than a description. The history on a single booking shows what acted on it and when, and that answers it in one step.



If a registration is no longer visible in the Bookings list, check in this order:

1. **Status filter** — change the filter to **All statuses**. It may be there as Cancelled, Pending, or Lost.
2. **Trash** — go to **Settings → Tools → Trash**. It may have been deleted and is recoverable within 30 days.
3. **Different class** — the client may have been transferred. Search by client name across all classes.
4. **Auto-deleted** — if the programme has auto-delete for non-paying registrations enabled and the grace period passed, the registration may have been automatically removed. Check the Trash first.

---

## Can I change a registration status manually?

Yes. Open the booking detail and click **Change status**. Available transitions depend on the current status:

- Enrolled → Cancelled
- Pending → Enrolled (to confirm manually)
- Trial started → Trial won / Trial lost / Trial attended
- Cancelled → Enrolled (to reactivate)

Not all status changes are available in all directions. If you cannot find the transition you need, use **Transfer** (to move to a different class) or contact Zooza support.

---

## Related

- [Recover deleted registrations](../guides/trash-and-restore.md) — restore from Trash.
- [Manage trial bookings](../guides/trials-daily-business.md) — trial status workflow.
- [Automatically cancel unpaid registrations](../guides/auto-cancel-unpaid-registrations.md) — how auto-delete for non-payment works.

## What a waiting-list or late booking looks like to the parent

Changed on 19 October 2026, and worth knowing because the old behaviour generated support tickets.

A booking that is **waitlisted**, or a **late booking** still waiting for you to confirm it, is not an enrolment yet. Until that date it looked exactly like one in the parent's profile — it sat among their current classes with nothing but a payment badge, and the class page then half-worked: no sessions listed on a class that had forty, and a make-up tile reading "undefined".

Now:

- **On their dashboard**, the booking carries a status badge next to the payment badge, so the parent can see their place is not confirmed.
- **On the class page**, a notice at the top says in plain words what state the booking is in and what happens next.
- **Only the tabs that have data are shown** — Overview and Detail. Attendance and Payments are not offered, because there is nothing in them yet.

Nothing changes on your side: confirm the late booking, or move them off the waiting list, and the parent gets the full view.
