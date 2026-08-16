---
title: "Membership prices by number of blocks selected"
description: "Set different membership prices depending on how many blocks (segments) a client picks — one configurable price table per payment frequency."
slug: "payg-segment-pricing"
type: "guides"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: ["membership", "pay-as-you-go", "blocks", "segments", "pricing", "payment-schedules"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-08-07"
related_articles: ["pay-as-you-go-programme", "blocks-creation"]
---

# Membership prices by number of blocks selected

When a programme uses **pay-as-you-go (membership)** pricing and has blocks (segments), you can set a different monthly, quarterly, or yearly price depending on **how many blocks** a client selects — for example:

- 1 block → €50 / month
- 2 blocks → €80 / month
- 3 blocks → €100 / month

Clients see the correct price update live as they choose their blocks in the booking widget.

> **This applies to membership (pay-as-you-go) pricing only.** Course-fee programmes handle partial block selection differently and have their own discount card.

## How block pricing works

The price depends on the **count** of blocks selected, not on which specific blocks. Selecting "Mondays + Wednesdays" and selecting "Mondays + Fridays" both count as 2 blocks and cost the same.

Each payment frequency (monthly, quarterly, yearly) has its **own independent price table**, so you can configure a deeper discount for clients who commit to a quarterly or yearly payment.

If a client selects a block count with no configured price, they are charged the base full-schedule price.

## Setting up block pricing

Block pricing is configured on the class's **Prices** screen.

1. Open the class, go to the **Prices** tab.
2. Find the **pay-as-you-go** payment frequency card (monthly, quarterly, or yearly).
3. Click **Block pricing** — this opens the pricing editor.
4. Enter a money amount for each block count (1 block, 2 blocks, …). Leave a row blank to fall back to the full price for that count.
5. Click **Save**.

Repeat for each payment frequency where you want different prices per block count.

> **Note:** Each price you enter must be **equal to or lower than** the base (full-schedule) price for that frequency. Zooza will reject a tier that exceeds the base price.

### Base price vs. block pricing

The base price (the "Period amount" on the payment frequency card) still determines what clients who select **all blocks** — or who don't select any — are charged. Block pricing rows are applied only when a client picks a subset.

## What clients see

In the booking widget, the displayed period price updates live as a client ticks or unticks blocks. No page refresh is needed. The price shown is always the one from your configured table for that count of blocks.

The client does not see any "discount" line — the block-count price is simply their membership price.

## Proration (if enabled)

When proration by sessions is active on the programme, the prorated first-period amount is calculated from the sessions inside the selected blocks only, not from the full schedule. This means a client who selects fewer blocks also gets a lower prorated first payment.

**The block-count price applies to that first partial payment too.** A client who takes three blocks keeps their three-block rate from the very first payment — the multi-block price is not withheld until the first full period. Sessions you marked non-billable are left out of it as well.

> If a partial first month ever looks *more* expensive than a full one, that is not how it should behave. Check the block-count table on the programme and contact support.

Proration by days is not affected by block selection.

## Notes on per-block individual discounts

In earlier versions of Zooza, individual blocks in a membership schedule could carry their own discount. That configuration has been removed from the admin interface and from the booking widget. Existing stored values are kept for historical course-fee compatibility, but for membership (pay-as-you-go) programmes only the count-based table above applies.

## Related

- [Pay-as-you-go programme](pay-as-you-go-programme.md) — how to set up a membership programme
- [Blocks / segments](blocks-creation.md) — how to configure blocks within a class
- [Pay-as-you-go FAQ](../faq/pay-as-you-go-faq.md) — common questions about membership pricing
