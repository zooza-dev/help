---
title: "Automatic reminders for payment schedule"
slug: "automatic-payment-reminders"
type: "guides"
product_area: "Communication"
sub_area: "Email"
audience: ["admin"]
tags: ["payments", "email"]
status: "published"
source_legacy_path: "legacy/0003_Welcome to Zooza.html"
source_language: "en"
needs_screenshot_replacement: true
last_converted: "2026-02-13"
intercom_id: 13728511
intercom_sync: false
---

# Automatic reminders for payment schedule

If the client has selected payment with a payment template in the booking or you have set it up manually, they will always be informed of this obligation in time -- automatically by the application. Reminders are sent as email notifications. Learn how to set up payment templates in the [payment templates manual](payment-templates-creation.md).

## Reminder 1: Upcoming payment notification

Informs the client that an instalment payment will be due on their programme booking in a few days (depending on the setup).

1. The reminder must be enabled in **Settings --> Payments**, where you can specify the number of days before the payment is created when the notification should be sent.

![Payment reminder settings](../../assets/images/payment-reminder-settings.png "Payment reminder settings")

2. The notification before the payment is created is sent according to the formula:
   **Due date - Number of days due - Number of days before payment creation**

3. You can edit the text in **Communication --> Message Templates**, under the template titled: **Upcoming Payment Notification**.

4. To communicate the date when the payment will be created, use the dynamic tag: `SCHEDULED_AT_DATE`

## Reminder 2: Payment created notification

Informs the client that a new instalment debt has been created on their booking. The date when the payment is posted and the notification sent follows the formula: **Due Date - Number of days due**.

1. Set the payment due date in **Settings --> Payments**, where you can specify the number of days.

![Payment due date settings](../../assets/images/payment-due-date-settings.png "Payment due date settings")

2. Customize the text in **Communication --> Message Templates**, under the template named: **Call for payment**.

3. To communicate the due date, use the dynamic tag: `DUE_DATE`

## Reminder 3: Overdue payment notification

Informs the client that the booking has not been paid by the due date.

1. It is sent on the due date if the booking is in an unpaid/partially paid status.
2. Edit the text in **Communication --> Message Templates**, under the template titled: **Notification of outstanding payment**.
3. To communicate the due date, use the dynamic tag: `DUE_DATE`

## Understanding the three notification types

Clients often confuse these three notifications. Here is a clear distinction:

| Notification | When it is sent | Purpose | Template name |
|---|---|---|---|
| **Upcoming payment** | Before the debt is created (configurable days) | Informational — tells the client a payment will be due soon | Upcoming Payment Notification |
| **Payment created** | When the instalment debt is posted | Action required — tells the client to pay | Call for payment |
| **Overdue payment** | On or after the due date, if unpaid | Urgent — the payment is past due | Notification of outstanding payment |

### Common confusion: "I already paid but got a reminder"

This happens when:

1. The client paid **before** the debt was created (e.g., after receiving the "upcoming payment" notification).
2. The payment was received by the bank but **auto-pairing has not yet processed** it (GoCardless syncs once daily; email-notification pairing is near real-time).
3. The system sent the next scheduled notification before the payment was matched.

The client sees what looks like an overdue notice, but it was actually the "upcoming" or "payment created" notification for a future instalment. The wording of these notifications should clearly distinguish them.

### Notification timing

All payment notifications are processed in a **nightly batch**. This means:

- Notifications may arrive in the early morning hours (e.g., midnight to 6 AM).
- The send time is **not configurable** per programme or globally.
- If this timing causes client complaints, consider adding a note in your notification template explaining that the email was generated automatically overnight.

<!-- REVIEW: Notification send time is not configurable as of Feb 2026. Monitor for any changes to this. -->

### The "zeroth" notification (pre-payment)

You can enable a notification that is sent **before** the first instalment is created. This gives the client advance notice that they will receive a payment request soon. It acts as a fourth touchpoint in addition to the three reminders above.

Enable this in **Programme → Settings → Price and payments → Payment reminder settings**.

<!-- REVIEW: Confirm the exact setting name and location for enabling the zeroth notification. -->
