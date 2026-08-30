---
title: "Charge a monthly membership fee"
description: "Set a group to pay the same amount every month regardless of how many sessions fall in it — the order the settings have to be done in, and why it fails otherwise."
slug: "membership-fee-setup"
type: "guides"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: ["membership", "payment-templates", "monthly", "recurring", "pricing", "clubs"]
related_articles: ["price-and-payment-setup", "payment-templates-creation", "payg-segment-pricing", "membership-subscription-setup"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: true
last_converted: "2026-08-30"
---

# Charge a monthly membership fee

"I want group K4 to pay 35 € a month" is one of the most common things people try to set up, and one of the most common to get stuck on. It fails in a way that gives no clue why: the Membership option is there, you select it, and nothing behaves.

The reason is almost always the same, and it is the order the two settings have to be done in.

## The order matters

**A membership fee needs a membership payment template, and the template has to exist first.**

A payment template is created *as* a membership template — that is a property of the template, chosen when you make it. An ordinary payment template will not drive a membership fee no matter what you set on the programme.

So:

1. **Create the template first.** Go to **Team & Settings → Billing → Payments** and create a payment template as a **membership** template. Choose its frequency — monthly, half-yearly or yearly — and any discount, at the moment you create it.
2. **Then set the programme.** Go to **Programmes → the programme → Settings → Price and Payment**, choose scheduled payments, and set the price type to **Membership**.
3. **Attach the template** to the programme.
4. **Check the booking form.** Open it as a client would and confirm the option appears with the right amount.

If you did it the other way round and it is not working, the template is what to look at — not the programme.

## Is a membership actually what you want?

Membership charges **the same amount every period, whatever the session count**. Four sessions in October, five in November, still 35 €.

If instead you have a **total** for the year and want it spread over months, that is a **programme fee**, not a membership — the template divides a calculated total rather than charging a flat sum. See [Price and payment setup](price-and-payment-setup.md) for the comparison.

Two things that follow from the difference:

- **A membership has no total.** What a client ends up paying depends on how long they stay.
- **Your legal form is irrelevant.** Becoming an association or a non-profit is not a reason to switch to membership. Plenty of associations charge a programme fee. Pick the model that matches how you bill.

## One programme, one payment type

**You cannot mix membership and programme fee inside a single programme.** The
payment type is set on the programme and applies to every class in it. There is no
per-class override, so a programme cannot hold one class charging a monthly
membership and another charging a course fee.

When you need both, **split them into two programmes** — one for each payment model.
That is a normal way to run an account, not a workaround. The only thing to watch is
distribution: two programmes mean two places to share from, so be deliberate about
which link goes to which parents.

### Before you split, check whether blocks fit better

If parents are really enrolling for the whole year and you just want the money in
two or three instalments, splitting into separate programmes is the wrong tool.
Keep one programme, put the sessions into [blocks](blocks-creation.md), and let
parents sign up once for the year while Zooza collects per block. You get one
registration and one class list instead of three.

Split into separate programmes when the **payment model** genuinely differs. Use
blocks when only the **collection schedule** differs.

## Frequency and discounts

Both are set on the template, not the programme:

- **Frequency** — monthly, half-yearly, yearly.
- **Discount** — attach one to the template if paying for a longer period should cost less. The discount applies to the first scheduled payment for a membership, unlike a programme fee where it spreads across all of them.

You can have as many templates as you need, and the same one can serve several programmes. You do not create a template per group.

## When it still does not appear for clients

Work down this list:

1. **Is the template a membership template?** The first thing to check, always.
2. **Is it active on the programme?** Under **Price and Payment → Payment Frequency**, a template can be active or inactive.
3. **Is it visible to clients?** Active is not the same as visible — that is a separate switch on the template itself.
4. **Does the class have sessions?** A class with none has no billing period, so there are no payment options to show.

See [Price and payment setup](price-and-payment-setup.md#the-payment-step-is-blank-on-the-booking-form) for the full version of that check.
