---
title: "Manually push a scheduled payment to offline charge"
description: "If a processed scheduled payment was never automatically sent to offline charging, use the manual push action on the payment detail page to re-queue it."
slug: "offline-charge-manual-push"
type: "troubleshooting"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: ["payments", "offline-charge", "scheduled-payments", "direct-debit", "stripe", "recovery"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: true
last_converted: "2026-09-27"
related_articles: ["global-payments", "fastpay-direct-debit", "gocardless-faq", "payment-templates-creation", "payments-and-billing-faq"]
---

# Manually push a scheduled payment to offline charge

When a payment plan uses offline charging (Stripe card or GoCardless Direct Debit), Zooza normally sends each scheduled payment to the charge queue automatically when it is processed. Occasionally, a payment can end up in **processed** status without being enqueued — for example, if offline charging was temporarily disabled at the moment of processing. In that case, the payment never gets charged and no error is surfaced to the client.

This page explains how to detect this situation and push the payment manually.

---

## Symptoms

- A scheduled payment shows status **Processed** on the payment plan.
- The expected charge has not appeared on the client's card or bank account.
- No error was shown when the payment was processed.

---

## Check the payment detail

1. Open the client's booking.
2. Go to the booking's **Payment plan** tab.
3. Find the payment with **Processed** status and click **More** to open the detail page.
4. In the **Payment Info** card, look for one of two indicators:
   - **"Push to offline charge queue"** button — the payment was never queued; you can push it now.
   - **"This payment is in the offline charge queue."** notice — the payment is already queued; wait for the charge to process.

If neither indicator appears, offline charging may not be enabled on this payment plan. Check the parent payment plan settings.

---

## Push the payment manually

1. On the scheduled payment detail page, click **Push to offline charge queue**.
2. Zooza verifies that the client still has a valid card or direct debit mandate on file.
3. If verification passes, the payment is added to the offline charge queue. The button disappears and the "in queue" notice appears.
4. The existing offline charging process picks up the payment and attempts the charge. You can monitor the result in the charge log.

![Screenshot — offline charge manual push](../../assets/images/offline-charge-manual-push-01.png)

---

## The charge log — what actually happened

The scheduled payment's detail carries a **charge log** listing every attempt
Zooza made, what each one came back with, and whether another retry is planned.
Use it before pushing anything: a payment that has already failed three times
for "card declined" will fail a fourth time, and the log names the reason.

It appears on a payment that is in the offline queue. It covers both charging
engines, so a Global Payments charge and a legacy one are described in the same
words.

> The log was unreachable between March and 23 September 2026 — the component
> was still there, nothing linked to it. If you looked for it during that time
> and concluded your payments were not being retried, the retries were happening;
> only the record of them was missing.

**Read the queue state as a job, not as money.** A payment can report that its
charge job is `processing` or even `succeeded` while the question "has this been
paid" is answered somewhere else entirely — on the instalment and the order. The
legacy charging process never wrote a completion row at all, so a settled
instalment showing `processing` is normal and not a fault. Always take paid or
unpaid from the payment itself.

The **push** button follows what the server says is possible rather than what the
screen can guess, so it no longer offers a push on a payment that has already
been charged.

---

## Error messages

| Error | Meaning | Action |
|---|---|---|
| **Offline charging is no longer enabled on this payment plan** | The payment plan's offline charge setting was turned off. | Re-enable offline charging on the payment plan, then try again. |
| **This payment is already in the offline charge queue** | Another push already enqueued it. | Wait for the charge to complete. Refresh the page. |
| **Only processed payments can be pushed** | The payment is in a different status (scheduled, cancelled, etc.). | No action needed — only processed payments can be pushed. |
| **No offline charge provider on file** | The client's card or mandate is missing. | Ask the client to update their payment method via their profile. |
| **Card or mandate is no longer available** | The card expired or the mandate was cancelled since processing. | Ask the client to update their payment method, then try again. |

---

## Related

- [GoCardless Direct Debit](../guides/gocardless-direct-debit-mandates.md)
- [Payment schedules](../guides/ad-hoc-scheduled-payment.md)
