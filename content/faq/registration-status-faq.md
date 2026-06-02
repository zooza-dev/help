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
last_converted: "2026-05-15"
---

# Registration statuses — what each one means

## Status overview

| Status | What it means | Capacity held? | Client receives emails? |
|---|---|---|---|
| **Enrolled** | Active registration — client is attending | Yes | Yes |
| **Pending** | Registration submitted but not yet confirmed (e.g. waiting for payment or admin approval) | Yes | Limited |
| **Awaiting payment** | Registration is active but a payment is overdue | Yes | Payment reminders |
| **Waiting list** | Class is full; client is queued for a spot | No (or minimal) | Notification when spot opens |
| **Trial started** | Client booked a trial session | Depends on settings | Trial follow-ups |
| **Trial lost** | Trial closed without enrolment | No | None |
| **Cancelled** | Registration was cancelled; record still exists | No | None |
| **Deleted (Trash)** | Moved to Trash; recoverable within 30 days | No | None |

---

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

**Awaiting payment** means the registration is active and the client is attending, but one or more scheduled payments are overdue.

This status does **not** automatically cancel the booking. Whether the booking gets cancelled for non-payment depends on your programme's **payment reminder and auto-delete settings**.

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
