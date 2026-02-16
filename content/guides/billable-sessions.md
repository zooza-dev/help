---
title: "Billable sessions"
slug: "billable-sessions"
type: "guides"
product_area: "Classes"
sub_area: ""
audience: ["admin"]
tags: ["billing", "payments"]
status: "published"
source_legacy_path: "legacy/0044_Welcome to Zooza.html"
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-16"
intercom_id: 13728565
intercom_sync: true
---

# Billable sessions

In programmes using the **Booking for the full programme duration** type, a client pays for all sessions in the class when they book. However, the actual number of sessions in a class may not always match the number the client should pay for. The **billable sessions** feature lets you separate paid sessions from unpaid ones within a single booking.

This is purely a billing feature — it has nothing to do with attendance. It controls how the booking price is calculated.

## When to use billable sessions

- **Free bonus session** — You add an extra session to a class as a credit for a previously cancelled session. Without billable sessions, Zooza would divide the total price across all sessions (including the free one), lowering the unit price incorrectly.
- **Make-up sessions** — A client books a make-up session in a class. This adds a session to the class that should not affect the price calculation for existing bookings.

In both cases, the class ends up with more sessions than originally planned. Billable sessions tell Zooza: "the client pays for X sessions, regardless of how many sessions actually exist in the class."

## How to set it up

Billable sessions are configured at three levels: programme, class, and session.

### 1. Programme level (default for all classes)

1. Go to **Programmes** → select the programme → **Edit Settings**.
2. Open the **Price and Payment** tile.
3. Set the **Billable sessions** field to the number of sessions that should be paid for.

This value becomes the default for all classes within the programme.

![Billable sessions setting on programme](../../assets/images/how-to-create-paid-events-01.png "Billable sessions field in Programme Price and Payment settings")

### 2. Class level (override per class)

1. Go to **Classes** → select the class → **Price and Payment**.
2. Set the **Billable sessions** field.

If a class has its own value, it overrides the programme-level setting. This allows individual classes to have a different number of billable sessions.

![Billable sessions setting on class](../../assets/images/discount-code-01.png "Billable sessions field in Class Price and Payment settings")

> **Important:** If the programme has billable sessions set (e.g. 12) and the class value is 0, the programme value is used. You cannot set a class to 0 billable sessions when the programme has a non-zero value.

![Billable sessions override example](../../assets/images/how-to-create-paid-events-03.png "Class-level override of billable sessions")

### 3. Session level (mark individual sessions)

Each session must also be marked as billable or not billable:

1. **When creating sessions** — check the **Billable** checkbox.

   ![Billable checkbox when creating sessions](../../assets/images/how-to-create-paid-events-04.png "Billable checkbox on session creation")

2. **On an existing session** — open the session detail → **Session settings** → toggle the **Billable session** field.

   ![Billable session toggle in session detail](../../assets/images/how-to-create-paid-events-05.png "Billable session field in session settings")
   ![Billable session detail](../../assets/images/how-to-create-paid-events-06.png "Session detail showing billable status")

## How it works

For the setup to work correctly, all three levels must be aligned. If you set 10 billable sessions on the programme, you need exactly 10 sessions marked as billable at the session level.

### Adding sessions to a class

When you add sessions to a class that has billable sessions configured, the **Repetition frequency** field automatically pre-fills with the number of missing billable sessions. For example, if the class should have 5 billable sessions but only has 2 marked, the field suggests 3.

![Repetition frequency pre-fill](../../assets/images/how-to-create-paid-events-08.png "Repetition frequency field pre-filled based on billable sessions")

### Billable toggle on new sessions

Once billable sessions are configured, a checkbox appears when creating new sessions, letting you mark them as billable or not. You can also toggle the billable status using the billing icon on existing sessions.

![Billable toggle icon](../../assets/images/how-to-create-paid-events-10.png "Billing icon to toggle billable status on sessions")

## Unit price calculation

When billable sessions are set on a class, Zooza calculates the unit price (price per session) using the billable session count instead of the total number of sessions.

**Example:** A class costs 120 EUR and has 15 sessions total, but only 12 are billable. The unit price is 120 / 12 = 10 EUR per session (not 120 / 15 = 8 EUR).

This applies only to programmes using **Booking for the full programme duration**. Pay-as-you-go programmes already use a fixed unit price per session.

### Changing billable sessions mid-programme

If you change the number of billable sessions during a running programme, you must also update the programme/class price accordingly. Otherwise the unit price calculation will be incorrect.

## Related

- [Tracking billable sessions](viewing-billable-sessions.md) — how to view and monitor billable session status across classes.
