---
title: "Refunds: recording one, and requests from clients"
description: "How an administrative refund differs from a real Stripe refund, when to use each, and how to handle refund requests clients raise when they cancel."
slug: "administrative-refund-faq"
type: "faq"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: ["payments", "refund", "stripe", "administrative"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-10-30"
related_articles: ["stripe-payments-faq", "payments-and-billing-faq", "cancellation-reasons", "edit-payment-on-booking", "scheduled-registration-cancellation"]
---

# Administrative Refund FAQ

## What is an administrative refund?

An administrative refund is a record in Zooza that a payment has been returned to a client, without triggering a real refund through Stripe or any other payment gateway. It creates a negative transaction on the booking to reflect that the income has been reduced.

## When should I use an administrative refund instead of a real Stripe refund?

Use an administrative refund when:

- You returned the money outside Zooza — for example via bank transfer, cash, or as a credit on another invoice.
- Stripe is no longer connected to your account and you cannot trigger a gateway refund.
- You want to record the return now but handle the actual money movement separately.

If Stripe is connected and you want Zooza to send the money back through Stripe automatically, leave the **Administrative refund only** checkbox unticked — that triggers a real gateway refund.

## Does the administrative refund actually send money back to the client?

No. An administrative refund only creates a record in Zooza. You are responsible for returning the money through whatever channel you agreed with the client (bank transfer, cash, etc.).

## Will the client be notified about the administrative refund?

No automatic notification is sent for an administrative refund. If you want the client to know, contact them separately.

## Does the refund reduce the client's outstanding debt automatically?

No. The refund reduces recorded income on the booking (it appears as a negative transaction), but it does not automatically change the total charge or outstanding balance. After recording the refund, review the booking and adjust the debt manually if needed:

- If the client now owes less, edit the total charge on the booking's **Payments** tab.
- If no further balance adjustment is needed (e.g. the client simply overpaid), no action is required.

## What happens if Stripe is disconnected?

When the Stripe gateway is not connected to your Zooza account, the refund dialog shows: *"Gateway refund is currently not available. You can record an administrative refund."* In this case only the administrative record option is available. The refund is still saved immediately in Zooza.

## Can I issue a partial administrative refund?

Yes. In the refund dialog, enter any amount up to the original payment amount. Zooza prevents you from refunding more than the original payment (minus any refunds already issued).

## Can I refund the same payment multiple times?

Yes, as long as the total refunded amount does not exceed the original payment amount. Each refund creates a separate negative transaction.

## How do I find administrative refunds in reports?

Administrative refunds appear in the same payment reports as gateway refunds — as negative transactions reducing total income. If you need to distinguish them (for accounting purposes), contact Zooza support — the underlying data includes a `source` field that identifies each refund as `administrative` or `gateway`.

## Can I undo an administrative refund?

No. Once recorded, an administrative refund cannot be deleted. If you made an error, contact Zooza support or add a correcting manual payment to offset the negative transaction, and add a note explaining the adjustment.

## Can clients ask for a refund themselves?

Yes, if you let them. **Settings → General → Allow refund requests** lets a client
request a refund when they cancel an eligible session. It is off unless you turn it on.

**A request does not move any money.** It is a conversation with a record, not an
automatic payout — read that twice before switching it on, because the wording matters
to clients.

**What happens:**

1. The client cancels an eligible session and asks for a refund, giving a **reason** and
   a **requested amount**.
2. A **Refund request** banner appears on the booking detail, with **Approve** and
   **Deny**.
3. On **Approve** you confirm the **Amount to refund** — prefilled from your refund
   policy, and capped: you cannot approve more than the maximum Zooza shows. You can add
   a **note for the client**, which goes into the email.
4. **You still issue the refund yourself** through your payment provider. Approving
   records your decision and emails the client; it does not touch Stripe or GoCardless.
5. On **Deny**, the client is emailed and **the request cannot be reopened** — denying is
   final.

Requests are **Pending**, **Approved** or **Denied**, and resolved ones stay on the
booking under **Resolved refund requests**, so there is a record of who asked for what
and what you decided.

> **Two emails you can rewrite.** *Refund request – approved* and *Refund request –
> denied* are templates under **Communication → Templates**, carrying the approved
> amount and your note. The note tag is wrapped in a conditional, so a decision you made
> without a note does not send an empty paragraph.

**The gap to close before you switch it on:** approving creates an expectation and does
not create a payment. If nobody on your team then issues the refund in Stripe, the client
has an email saying yes and no money. Decide who owns that step first.

## A client cancelled their registration — can Zooza automatically keep a percentage as a cancellation fee?

Zooza does not have a built-in cancellation penalty feature. If your policy is to retain a portion of the payment when a client cancels early (for example, keeping 20% and refunding 80%), you need to calculate the retained amount manually and then:

1. Issue a **partial refund** (via Stripe refund or administrative refund) for the amount you are returning to the client.
2. Adjust the outstanding amount on the booking to reflect the retained amount.

The client sees the refund on their side. The retained portion remains as income in your Zooza records. There is no automated way to set a percentage rule — it must be calculated and applied per booking.

> **Terminology note:** "Storno poplatok" (SK) or "cancellation fee" refers to money you keep from a client who cancels. In Zooza, you handle this through the refund flow — issue a partial refund for what you return, and the rest is implicitly retained.

## Related

- [Recording an Administrative Refund for an Online Payment](../guides/recording-an-administrative-refund.md) — step-by-step guide.
- [Payment Correction vs Refund](../guides/payment-correction-vs-refund.md) — when to correct a record versus issue a refund.
