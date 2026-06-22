---
title: "FastPay Direct Debit FAQ"
description: "Answers to common questions about collecting UK BACS Direct Debit payments with FastPay in Zooza — mandates, pushes, reconciliation, and refunds."
slug: "fastpay-faq"
type: "faq"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: ["fastpay", "direct-debit", "bacs", "mandate", "reconciliation"]
status: "published"
related_articles: ["fastpay-direct-debit", "integrations-hub", "gocardless-faq"]
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-06-19"
---

# FastPay Direct Debit FAQ

## Why don't I see FastPay in my integrations?

FastPay collects by **UK BACS**, so it is only available to UK companies. In other regions it shows as *Not available in your region*. If you are in the UK and still don't see it, contact support.

## Do I set up the mandate, or does the customer do it in their bank?

Neither happens automatically. The customer completes a **paper Direct Debit Instruction (DDI)** and returns it to **you**. You then **key it into the FastPay portal**, which lodges the mandate. Zooza and the FastPay API do **not** create mandates — Zooza stores the bank details and reference, and submits the collections.

## How is FastPay different from GoCardless?

GoCardless authorises the mandate online and charges in **real time** via its API. FastPay is **batch-based**: mandates are set up on paper, and you push a **monthly collection file** that FastPay processes over **2–3 working days**. Zooza then reconciles the outcomes. See [Collect Direct Debit payments with FastPay](../guides/fastpay-direct-debit.md).

## I pushed a collection but the payments still say "pending". Is something wrong?

No. BACS settles **2–3 working days** after submission, so charges stay **pending** until then. Zooza polls FastPay daily and updates each charge to **collected** or **failed** automatically — you don't need to do anything.

## What happens when a collection fails or bounces?

Zooza marks that charge as **failed** and sends you a **system message** in your admin inbox with the bounce reason. The other charges in the same batch are unaffected. You can also see failed charges under **FastPay batches**.

## Can I push the same period twice?

**No — and you should never try.** FastPay does **not** detect duplicate files, so re-submitting the same collection would charge every customer again. Zooza blocks a second push for a period that has already been submitted.

## Why does Zooza warn me about my Mandate ID Format?

BACS references must be **18 characters or fewer**, uppercase letters and digits, and unique. If your format would generate a reference that breaks these rules, Zooza warns you when you **save the course settings**, so the problem is caught before any booking is taken. (SEPA allows up to 35 characters, so a format that worked for ERSTE may be too long for BACS.)

## How do I refund a FastPay payment?

FastPay has **no refund API**. Process the refund **manually in the FastPay portal**, then correct the payment in Zooza. See [Payment correction vs refund](../guides/payment-correction-vs-refund.md).

## A customer cancelled their Direct Debit at their bank. Do I need to update Zooza?

No. Zooza detects when a mandate is reported **Cancelled** or **Expired**, **deactivates** it so it's skipped in future collections, and notifies you with a system message.

## Does FastPay collect automatically every month?

Not yet. In this release the monthly collection is a **manual push** — each period you set the date range, preview the batch, and **Submit** it. Automatic monthly scheduling is planned for a later release.

## Where do the customer's bank details come from?

From one of two places: the **registration widget** (the customer enters their UK bank details at booking — the recommended path), or **you** entering them on the mandate when a paper form arrives. Both store the sort code, account number, and account-holder name that FastPay needs.
