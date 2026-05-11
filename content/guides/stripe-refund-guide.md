---
title: "Refund a Stripe payment — step by step"
description: "How to refund a client who paid via Stripe: process through Zooza (recommended) or directly in Stripe dashboard, and what to do in Zooza afterwards."
slug: "stripe-refund-guide"
type: "guides"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: ["payments", "refund", "stripe", "cancellation"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-05-11"
---

# Refund a Stripe payment — step by step

When a client paid online via Stripe and you need to return the money, you have two options: refund through Zooza (which handles Stripe automatically), or go to Stripe directly and then record the refund in Zooza. Both produce the same end result for the client — money back to their card.

**Recommended: use Zooza.** It keeps your records in sync automatically.

---

## Option 1 — Refund through Zooza (recommended)

This is the standard flow. Zooza sends the refund instruction to Stripe and records everything automatically.

1. Go to **Clients** → open the client's booking.
2. Scroll to the **Payments** section.
3. Click on the Stripe transaction you want to refund.
4. Click **Refund payment**.
5. Enter the amount — full amount or a partial amount.
6. Make sure the **Administrative refund only** checkbox is **unticked**. If it's ticked, Zooza will record a refund entry but won't send anything to Stripe.
7. Click **OK**.

**What happens next:**
- Zooza sends the refund to Stripe immediately.
- Stripe processes it and returns the money to the client's original card. This typically takes **5–10 business days** to appear on the client's bank statement.
- A negative transaction appears in the Payments section of the booking.
- The booking's recorded income is reduced by the refund amount.

**The booking status does not change automatically.** If the client is cancelling, update the booking status to **Cancelled** separately.

---

## Option 2 — Refund in Stripe dashboard directly

Use this if:
- The Zooza refund button fails with an error
- Stripe's connection to Zooza has been interrupted
- You need to refund a payment you can't locate inside Zooza

### Step A — Issue the refund in Stripe

1. Log in to your Stripe dashboard at [dashboard.stripe.com](https://dashboard.stripe.com).
2. Go to **Payments** in the left menu.
3. Search for the payment by client name, email, or amount.
4. Open the payment and click **Refund**.
5. Enter the amount (full or partial) and select a reason.
6. Click **Refund**.

Stripe processes the refund and the money returns to the client's card within 5–10 business days.

### Step B — Record the refund in Zooza

Stripe refunds issued outside Zooza are **not automatically reflected in Zooza**. You must record them manually, or your booking records will show income that has already been returned.

1. Go to the client's booking in Zooza.
2. Open the Stripe payment transaction.
3. Click **Refund payment**.
4. Enter the same amount you refunded in Stripe.
5. Tick **Administrative refund only** — this records the refund in Zooza without sending a second instruction to Stripe.
6. Click **OK**.

This creates a negative transaction in Zooza that matches what you did in Stripe. Both systems now show the same state.

---

## After the refund: update the booking

Issuing the refund (by either method) only changes the payment record. It doesn't automatically adjust the client's outstanding balance or booking status. Check what applies:

| Situation | What to do next |
|-----------|----------------|
| Client is cancelling completely | Change booking status to **Cancelled** |
| Client overpaid and you're returning the excess | No booking change needed — refund record is sufficient |
| Client is entitled to a partial refund (e.g. missed sessions) | After refunding, edit the total charge on the booking to reduce the amount owed going forward |
| Recurring GoCardless payment — not Stripe | See [GoCardless refund process](gocardless-connection-lifecycle.md) — the steps are different |

---

## Partial refunds

You can refund any amount up to the original payment. To issue a partial refund, enter the specific amount in the refund dialog instead of the full amount.

If you need to refund in multiple instalments (e.g. returning money over two months), each instalment is a separate refund action. The total across all refunds cannot exceed the original payment.

---

## Common problems

**The Refund button is greyed out or missing**
- The payment may have been made too long ago — Stripe only allows refunds within a certain period (typically up to 90 days, though this varies).
- The payment may already have been fully refunded.
- Your Stripe account may need to be reconnected — go to **Settings → Integrations → Stripe** to check.

**The refund shows in Stripe but not in Zooza**
You issued the refund directly in Stripe. Follow [Step B above](#step-b--record-the-refund-in-zooza) to record it in Zooza.

**The client says they haven't received the money**
Stripe refunds take 5–10 business days to appear on a card statement. If it's been longer, log in to Stripe and check the refund status on the original payment. If Stripe shows it as completed, the client should contact their bank.

---

## Related guides

- [Recording an administrative refund](recording-an-administrative-refund.md) — when to use an administrative refund vs. a real Stripe refund
- [Payment correction vs refund](payment-correction-vs-refund.md) — when to edit a payment record vs. issue a refund
- [GoCardless connection lifecycle](gocardless-connection-lifecycle.md) — managing GoCardless mandates and payments
