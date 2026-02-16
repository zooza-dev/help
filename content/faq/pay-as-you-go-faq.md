---
title: "Pay-as-you-go FAQ"
slug: "pay-as-you-go-faq"
type: "faq"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: ["pay-as-you-go", "entry pass", "linked classes", "session booking"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-15"
intercom_id: 13738680
intercom_sync: false
---

# Pay-as-you-go FAQ

## What is a Pay-as-you-go programme?

A Pay-as-you-go programme is a flexible membership where clients register once and then pick individual sessions to attend. They only pay for the sessions they book. It is ideal for fitness studios, leisure classes, and any offering where clients want to choose their own schedule.

See the full guide: [Pay-as-you-go programme](../guides/pay-as-you-go-programme.md).

## How does pricing work?

The **unit price** is the price per session. When you create the programme, you set a default unit price. You can also override it per class if different classes have different rates. Each time a client books a session, a payment obligation equal to the unit price is created.

## Can a client register for the same session twice?

No. Duplicate bookings for the same session are blocked by the system. A client can only be registered for a given session once.

## How does a client book a session?

Clients book sessions in two ways:

1. **From their profile** — After logging in on your website, they go to their programme, click **Book date**, and select from available sessions.
2. **From the calendar widget** — If you have a calendar widget on your website, clients can browse and book sessions directly.

## What happens when a client cancels a session?

When a client cancels a session:

- The session is removed from their attendance.
- The payment obligation for that session is cancelled (debt is reset to zero).
- If they used an entry pass, the entry or credit is returned.

The client receives a notification email confirming the cancellation.

## What is an entry pass?

An entry pass is a prepaid product that gives clients a set number of visits. Each time they book a session, one entry is deducted. Entry passes are created as products and assigned to programmes or classes.

See the full guide: [Creating entry passes](../guides/creating-entry-passes.md).

## What is the difference between an entry pass and prepaid credit?

- **Entry pass** — Visits-based. The client buys a number of entries (e.g. 10 sessions).
- **Prepaid credit** — Money-based. The client buys a credit amount (e.g. 50 EUR), and the session price is deducted from the balance each time.

Both work the same way during booking. Choose based on whether you want to sell by visit count or monetary value.

## Do I need entry passes for Pay-as-you-go?

No. Entry passes are optional. Without them, clients simply pay per session at the unit price. Entry passes are useful when you want to offer bulk discounts (e.g. 10 sessions for the price of 8) or when you want clients to prepay.

## What does "Require a valid entry pass" do?

This is an attendance setting on the programme. When enabled, clients must have a valid (non-expired, non-exhausted) entry pass to book a session. Without a valid pass, the system blocks them from registering for sessions.

## Can an entry pass be used if the order is unpaid?

Yes, if you enable the **Redeem if unpaid** setting on the programme. This allows clients to use their entry pass even before they have paid for it. This is useful for clients who pay by bank transfer where payment confirmation takes time.

## How do I offer entry passes in both the client profile and the booking form?

A single product cannot appear in both locations due to the mandatory/optional setting. To work around this:

1. Create a **mandatory** product (appears in client profile).
2. Create a separate **optional** product with the same value and price (appears in booking form).

See [Creating entry passes — Two-product setup](../guides/creating-entry-passes.md#two-product-setup-for-dual-availability) for details.

## Can I use one entry pass across multiple classes?

Yes, if the classes are linked. When you link classes within a programme, a single entry pass covers all linked classes. The client can book sessions from any class in the pool.

See: [Linked classes](../guides/linked-classes.md).

## How does the client see available sessions?

Clients see available sessions in two places:

1. **Profile** — After logging in, they navigate to their programme and click **Book date** to see all upcoming sessions with availability.
2. **Calendar widget** — If embedded on your website, the calendar shows all available sessions.

## What are linked classes and when do I need them?

Linked classes connect multiple classes within a Pay-as-you-go programme so clients can pick sessions from any of the linked classes. Use them when:

- You offer multiple class types (e.g. yoga + pilates) under one membership.
- You run the same class at different locations or with different instructors.
- You want one entry pass to cover multiple classes.

See the full guide: [Linked classes](../guides/linked-classes.md).
