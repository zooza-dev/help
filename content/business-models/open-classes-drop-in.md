---
title: "Open Classes and Drop-in — Pay-as-you-go and Entry Passes"
description: "In a block or subscription model, the client enrols and Zooza signs them up for every session automatically."
slug: "open-classes-drop-in"
type: "business-model"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: ["business-model", "drop-in", "pay-as-you-go", "entry-pass", "fitness", "yoga", "open-classes", "permanentka"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-04-09"
---

# Open Classes and Drop-in — Pay-as-you-go and Entry Passes

## This guide is for you if

- You run classes where clients choose which sessions to attend — no fixed weekly commitment
- Clients pay per session, or buy a pass (e.g. 10 sessions, monthly unlimited) and draw it down
- Your schedule is open: a new client can join any week without signing up for a full term
- Examples: yoga studios, pilates, fitness classes, martial arts open sessions, adult dance, climbing walls, swimming for adults

---

## The core concept: enrol once, choose sessions freely

In a block or subscription model, the client enrols and Zooza signs them up for every session automatically. In a drop-in model it works the other way: the client enrols in the programme once, then picks the sessions they want to attend from their parent portal. They only pay for what they book.

This gives clients flexibility. For you, it means less predictable attendance — but entry passes solve most of that by getting payment upfront.

---

## Two ways to handle payment

### Option A — Pay per session (no pass)

The simplest setup. Every time a client books a session, a payment obligation is created for that session price. If they cancel, the obligation resets to zero.

Good for occasional clients or when you want zero friction to try a class. Not great for revenue predictability.

### Option B — Entry passes (recommended)

Clients buy a pass upfront — either a **visits-based pass** (e.g. 10 sessions) or a **credit-based pass** (e.g. €50 credit). Each session they book deducts one visit or the session price from their balance.

This is the equivalent of a gym card or permanentka. Clients commit money upfront; you get predictable revenue. Passes can have a validity period (e.g. 3 months to use 10 sessions).

Two pass types:
- **Entry pass** — sells a fixed number of entries. Client buys 10 sessions, each booking uses 1 entry.
- **Prepaid credit** — sells a monetary balance. Client buys €50 credit, each session costs €12 and is deducted from the balance.

Choose based on how you think about your pricing — by visits or by money.

---

## Recommended setup

### 1. Create the Programme

Go to **Programmes → New Programme**.

- **Programme type:** *Pay-as-you-go* — this is the key difference from a block or subscription programme. Clients self-select sessions; they are not auto-enrolled.
- **Target audience:** *Group Classes* (or *1-to-1 classes* for individual drop-in sessions)
- **Unit price:** set the standard per-session price — this is what a client pays if they have no pass

### 2. Create Classes

Each class type or time slot is a **Class** under the Programme. A yoga studio running morning and evening classes would have two Classes — not two Programmes.

If you offer multiple disciplines (yoga, pilates, kickbox), you can either:
- Put them all under one Programme — clients browse all sessions in one place
- Create separate Programmes per discipline — cleaner separation, separate pricing

### 3. Generate Sessions

Sessions for open classes typically run on an ongoing basis — generate them in batches, e.g. 3 months at a time. Clients see upcoming sessions in their portal and book the ones they want.

### 4. Set up entry passes

Go to **Products → Create New Product** and set up your pass options. Common setups:

| Pass type | Example | Notes |
|---|---|---|
| Single session | €15 per class | No pass needed — just the unit price |
| 10-session pass | 10 entries for €120 (save €30) | Discounted vs paying per session |
| Monthly unlimited | Credit of €80, valid 30 days | Client buys monthly, attends as often as they want |
| Annual pass | Credit of €700, valid 12 months | Best value, high upfront commitment |

After creating the pass product, assign it to the relevant Programme or Class. See [Creating entry passes](../guides/creating-entry-passes.md).

### 5. Let clients buy passes and book sessions

Clients purchase a pass through the booking flow or directly from their portal. Once they have a pass, they browse upcoming sessions and book the ones they want — the pass balance deducts automatically.

Clients without a pass pay per session at booking.

---

## Managing a mixed client base

Most open-class businesses have a mix: some clients on passes, some paying per session, some on a monthly subscription alongside drop-in. Zooza handles all three in parallel under the same Programme.

- **Pass clients:** buy a pass, self-book sessions, balance tracked automatically
- **Per-session clients:** book and pay individually each time
- **Subscription clients:** if you also offer a fixed monthly fee for unlimited access, set that up as a separate Programme with *Membership* price type and link the same Classes — the client enrols in the subscription Programme and attends sessions from the open schedule

---

## Cancellation and no-shows

When a client cancels a session they booked with a pass, the entry or credit is returned to their balance. If they simply do not show up without cancelling, the session is counted as attended and the balance is not returned.

Set a **cancellation deadline** in Programme settings — e.g. clients must cancel at least 12 hours before the session to get their credit back. This protects your capacity planning.

---

## What Zooza does not support (for this model)

| Limitation | Workaround |
|---|---|
| Automatically expiring a pass on a specific calendar date | Set a validity period (number of days from purchase) on the pass |
| Selling passes directly from your website without a booking | Passes are purchased as part of the booking flow |
| Capping how many sessions per week a client can book on an unlimited pass | Not available — manage manually if needed |

---

## Common mistakes

- **Using a block Programme instead of Pay-as-you-go** — in a block Programme, Zooza enrols the client in every session. For open classes where clients choose, you need Pay-as-you-go. The client experience is completely different.
- **Not setting a cancellation deadline** — without a deadline, clients can cancel 5 minutes before a session and reclaim their credit. Your instructor shows up to an empty room.
- **Creating a new Programme for each class type** — if your yoga and pilates classes share the same pricing and pass structure, one Programme with multiple Classes is cleaner. Only split into separate Programmes when pricing or registration form requirements differ.
- **Not setting pass validity** — an open-ended pass means a client who bought 10 sessions two years ago can still use them. Set a validity period that matches your business model.
