---
title: "Stripe Integration FAQ"
slug: "stripe-payments-faq"
type: "faq"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: ["payments"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-12"
intercom_id: 13728499
intercom_sync: false
---

# Stripe Integration FAQ

## What type of Stripe account does Zooza use?

Zooza connects via Stripe Connect. Depending on the setup, you may have a **Stripe Express** account (managed through Zooza) or a **Standard** account. Express accounts have limited dashboard access but all payment management functions are available within Zooza.

## I can only see a limited Stripe Express dashboard — where are my full reports?

The long-term approach is to manage payments directly in Zooza rather than through Stripe's dashboard. All reports, refund options, and payment data are available within the Zooza application.

If you need the full Stripe dashboard, try navigating directly to `dashboard.stripe.com` in your browser while logged in — this may show your main Stripe account rather than the Express view.

## Is Apple Pay / Google Pay supported?

Yes. Apple Pay and Google Pay are supported through Stripe. You need to enable them in your Stripe payment method settings. Once enabled, clients will see these options on mobile devices during checkout.

## How do I test payments before going live?

You can test the full payment flow by creating a booking yourself as a client. Use the public booking link, complete the booking, and make a test payment. Remember to:

1. Delete the test bookings afterwards.
2. Restore any prices you changed during testing.
3. Verify that all classes have the correct payment methods enabled.

## Where can I see payment reports for my accountant?

Payment reports are available in Zooza under **Reports**. For accounting purposes, the recommended approach is to use Zooza's reports and invoicing integration (Xero, etc.) rather than relying on Stripe's dashboard directly.
