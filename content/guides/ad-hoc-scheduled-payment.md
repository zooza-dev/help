---
title: "Add a one-off scheduled payment"
slug: "ad-hoc-scheduled-payment"
type: "guides"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: ["payment", "payment plan", "scheduled payment", "bulk", "registration", "late fee"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: true
last_converted: "2026-04-10"
---

# Add a one-off scheduled payment

You can add a one-off (ad hoc) scheduled payment to an existing payment plan — for example a late fee, a partial top-up, or a custom agreed amount. This can be done for a single registration or in bulk across multiple registrations in a class.

---

## Add a payment to a single registration

Use this when you need to add an extra charge to one client's payment plan.

1. Go to **Bookings** and open the registration.
2. Go to the **Payment plan** tab.
3. Click **Add scheduled payment** in the Payment overview card.

   ![Screenshot — ad hoc scheduled payment](../../assets/images/ad-hoc-scheduled-payment-01.png)

4. Fill in the payment details:

   | Field | Notes |
   |---|---|
   | **Amount** | Enter a **negative** value (e.g. `-50`). Positive values are rejected. |
   | **Scheduled at** | Date the payment is due. Defaults to today. |
   | **Note** | Label for this payment. Defaults to "Extra payment". |

5. Optionally expand **Advanced** to set:

   | Field | Notes |
   |---|---|
   | **Due date** | Date after which an overdue reminder can be sent. |
   | **Notify at** | Date to send a payment reminder notification. |
   | **Discount**, **Schedule discount**, **Loyalty discount** | Discount amounts applied to this payment. |

6. Click **Save**.

The new payment appears in the scheduled payments table at its chronological position.

> **Note:** The **Add payment** button on the booking detail (price card) records a received payment — it is a different action. This guide covers scheduling a future payment obligation.

---

## Add a payment to multiple registrations (bulk)

Use this when you need to add the same extra charge to several clients in a class at once — for example a late registration fee.

1. Go to the **Class detail** page.
2. In the **Price and Payment** card, click **Add payment**.

   ![Screenshot — ad hoc scheduled payment](../../assets/images/ad-hoc-scheduled-payment-02.png)

3. **Step 1 — Configure:** Fill in the payment fields (same fields as the individual form above).

   ![Screenshot — ad hoc scheduled payment](../../assets/images/ad-hoc-scheduled-payment-03.png)

   > Fields left empty will use each registration's own payment contract defaults. Different registrations in the same class may have different contracts.

4. Click **Continue**.

5. **Step 2 — Select:** Choose which registrations to include. Only registrations with an active payment plan are shown.

   ![Screenshot — ad hoc scheduled payment](../../assets/images/ad-hoc-scheduled-payment-04.png)

   > If some registrations are not shown, it means they do not have an active payment plan and cannot receive a scheduled payment.

6. Click **Go**.

7. **Step 3 — Processing:** Zooza applies the payment to each selected registration in sequence. Each row shows its status (queued → done / error). Errors on individual registrations do not stop the rest of the batch.

   ![Screenshot — ad hoc scheduled payment](../../assets/images/ad-hoc-scheduled-payment-05.png)

---

## Payment plan history

The payment plan page now shows a history of previous payment plans for each registration, below the active plan.

![Screenshot — ad hoc scheduled payment](../../assets/images/ad-hoc-scheduled-payment-06.png)

Each historical entry shows:

| Field | Description |
|---|---|
| **Template** | Name of the payment plan template that was used. |
| **Created** | Date the plan was created and by whom. |
| **Replaced** | Date the plan was replaced (and by whom, if available). |
| **Payments** | How many payments were completed out of the total (e.g. "3 / 10"). |

Click a historical entry to expand it and see the full scheduled payments table from that plan (read-only).

### Admin note

Both the active plan and historical plans have an editable **Admin note** field — use it to record context such as why a plan was changed or what was agreed with the client.

1. Click **Edit** next to the note field.
2. Type your note and press Enter or click away to save.

![Screenshot — ad hoc scheduled payment](../../assets/images/ad-hoc-scheduled-payment-07.png)
![Screenshot — ad hoc scheduled payment](../../assets/images/ad-hoc-scheduled-payment-08.png)
---

## Related

- [Payment tile on booking](payment-tile-on-booking.md) — overview of the payment card on a registration.
- [Payment options](payment-options.md) — types of payments and how they work.
- [Payments and billing FAQ](../faq/payments-and-billing-faq.md) — common questions.
