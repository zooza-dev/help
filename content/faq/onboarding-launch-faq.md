---
title: "Onboarding and Launch FAQ"
slug: "onboarding-launch-faq"
type: "faq"
product_area: "Settings"
sub_area: ""
audience: ["admin"]
tags: []
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-12"
---

# Onboarding and Launch FAQ

## I have interested clients — how do I get them registered in Zooza?

There are three ways to bring clients into Zooza. The right one depends on your situation:

### 1. Share a booking link (recommended)

Every class in Zooza has a public booking link. Clients click the link, fill in their details, and pay online — no admin involvement needed.

To get the link:
1. Go to **Programmes** → open the programme → open the class.
2. Copy the **booking link** from the class detail (look for the share/copy icon).

You can also share your main booking page (`yourbrand.zooza.online/booking/`) where clients choose from all available classes.

Send the link via email, WhatsApp, Instagram, or any channel you use.

### 2. Embed the booking form on your website

If you have a website, you can embed the Zooza booking form so clients register without leaving your page. See [Deploying Zooza on a website](../setup/deploying-zooza-on-website.md) and [Customising widgets](../guides/customizing-widgets.md).

### 3. Add clients manually (admin creates the booking)

If a client cannot or will not book online, you can create the booking for them:

1. Go to **Bookings** → **New booking** (or use the booking form on their behalf).
2. Fill in the client's name, email, and the class they are joining.
3. Set up payment manually after the booking is created.

See [Creating a booking](../guides/creating-a-booking.md) for step-by-step instructions.

> **Note:** Trial bookings cannot be created manually by an admin. Only standard enrolments and manual registrations.

## How do I create a demo or test class?

A demo class is useful when you want to test the full booking flow before going live, or show a potential client or team member how Zooza works without affecting real data.

1. Go to **Programmes** → create a new programme (e.g., name it "Demo" or "Test").
2. Add a class with a session or two.
3. Set the price to 0 or use a test payment method so no real charges occur.
4. Use the booking link to go through the registration yourself, or add a test booking manually.
5. When done, delete the test bookings: open each booking → set status to **Deleted**.

You can keep the demo programme for internal use or archive it when you no longer need it.

> **Tip:** If you only need to test the booking form experience (what the client sees), you can also use the [Widget preview](../guides/customizing-widgets.md) without creating an actual booking.

## What should I check before sending booking links to clients?

Before going live, verify that:

1. **All classes** have the correct payment methods enabled (card, Apple Pay, etc.).
2. **Pricing** is set correctly on every class (especially after testing — prices may have been changed during test payments).
3. **Booking forms** are consistent across all classes (same buttons, same fields, same client journey).
4. **Extra fields** (e.g., medical conditions, gender) are configured the same way across programmes, unless intentionally different.
5. **Test bookings** are deleted so they don't skew your data.
6. **Booking links** are tested end-to-end — complete a test booking yourself to see what clients will experience.

## How do I migrate existing clients from another system to Zooza?

For clients already in your old system:

1. Send them a Zooza booking link to re-register.
2. If they should not pay the registration fee again, create a discount code for the fee amount (e.g., code "MEMBER" for the full registration fee).
3. Once registered, they are set up with recurring payments in Zooza.

This is a one-time transition process. After the migration, all new clients follow the standard Zooza flow.

## Can I launch bookings before my invoicing is fully set up?

Yes. You can disable automatic invoice generation, start accepting bookings and payments, and generate invoices retroactively once your accounting settings are finalized.

## What should I do if clients report inconsistent experiences?

Check that all classes within each programme have the same settings:

- Payment methods (card, Apple Pay, etc.)
- Button labels (Enroll vs. Book)
- Extra fields and consent options
- Price and billing configuration

Inconsistencies usually happen when settings were adjusted during testing and not fully aligned before launch.

## How do I handle the first billing cycle?

The first billing cycle often needs special attention:

- If the first month has fewer sessions than usual, decide whether to use **aliquot billing** (prorated) or a **fixed monthly amount**.
- Most clients prefer to turn aliquot off for the initial launch so every payment is the same amount, then enable it later for mid-term joiners.
- Double-check the first payment amounts on a few test bookings before going live.

## How do I sell products (merchandise, party packages) through Zooza?

Products are managed under **Products / Services**. You can:

- Add items with descriptions, prices, and variants (e.g., sizes).
- Offer products during booking as add-ons.
- Create separate one-off bookings for sessions like birthday parties — set up a new programme/class for the session and share the booking link with the client.

For birthday parties or one-off sessions, create a new programme (e.g., "Sessions / Specials"), add one class with the session date, and share the generated booking link.
