---
title: "Franchise and Multi-location Networks"
description: "Each franchise location is a separate Zooza account (company). They manage their own programmes, classes, clients, and payments independently."
slug: "franchise-network"
type: "business-model"
product_area: "Settings"
sub_area: ""
audience: ["admin"]
tags: ["business-model", "franchise", "network", "multi-location", "royalties", "hq"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-04-09"
---

# Franchise and Multi-location Networks

> **Feature overview:** See [Franchise and multi-location features](https://www.zooza.online/features/franchises/) on zooza.online.

## This guide is for you if

- You operate multiple branches or franchise locations under one brand
- Each location runs independently — its own classes, clients, instructors, and payments — but you need visibility across all of them from a central place
- You want to standardise how programmes, pricing, or communications are set up across the network
- You need to track royalties, revenue, and enrolments per location from HQ
- Examples: children's activity franchises with regional licensees, language school chains, sports club networks with multiple city branches

---

## How Zooza models a franchise network

Each franchise location is a **separate Zooza account** (company). They manage their own programmes, classes, clients, and payments independently. The franchisor connects these accounts into a **Network** — a shared layer that gives HQ read-access to reporting across all companies and enables cross-company features like client transfers.

This means:
- Franchisees have full autonomy in their day-to-day operations
- HQ sees aggregated and per-branch metrics without having to log into each account separately
- Clients can move between branches without losing their history

---

## What HQ can do in the Network

### Reporting — Network Application

The Network Application is the HQ dashboard. It shows enrolments, payments, revenue, cancellations, and sessions across the entire network — filterable by company, location, product, and time period.

Key metrics available:
- **New enrolments** and **active enrolments** per branch
- **Received payments** and **net revenue** (after discounts and refunds)
- **Unpaid debt** — outstanding balances across the network
- **Royalties** — calculated per your network's defined rules
- **Sessions scheduled** and **sessions with attendance recorded**

You can toggle between **Companies view** (aggregated per franchisee) and **Places view** (aggregated per physical location). Useful when one franchisee runs multiple venues.

See [Network Application](../guides/network-application.md) for the full reporting reference.

### Standardising product codes

To compare like-for-like across branches — e.g. "Ballet Beginners" at Branch A vs the same programme at Branch B — HQ assigns **product codes** to programmes. These codes unify how different branches' programmes appear in network reports, even if the local names differ slightly.

### Transferring clients between branches

When a client moves city, or a branch closes and clients need to be migrated, use **Bulk Network Transfer** to move registrations from one company to another in a single action.

- Select the registrations to transfer, choose the target company, and preview the result before confirming
- The original registrations can be cancelled immediately or held until the target branch accepts
- Ineligible registrations (already transferred, wrong status) are skipped automatically — they do not block the rest

See [Bulk Network Transfer](../guides/bulk-network-transfer.md).

---

## What franchisees manage themselves

Each branch handles:
- Their own **programmes, classes, and sessions**
- Their own **clients and bookings**
- Their own **payment gateway** (Stripe, GoCardless, or bank transfer — each branch connects their own account)
- Their own **instructors and locations**
- Their own **communication templates** — unless HQ has defined standards and shared them

---

## Standardising communications across the network

Zooza does not currently push email templates automatically from HQ to all franchisees. The practical approach:

1. HQ defines the standard templates in one account (or a reference account)
2. Templates are copied into each franchisee account manually — or one person with access to all accounts does the rollout
3. Franchisees can then customise tone and local details while keeping the structure consistent

This is worth doing for the key automated emails: trial confirmation, trial follow-up, full registration confirmation, and session reminders. Getting these consistent across the network protects the brand voice.

---

## Payment setup per branch

Each franchisee connects their own payment gateway. For UK networks using GoCardless Direct Debit:

- Each branch sets up their own GoCardless account and connects it to their Zooza account
- Parents set up a Direct Debit mandate once — payments are pulled automatically from then on
- HQ sees the payment status for each branch in the Network Application but does not control the collection

For branches using Stripe: same principle — each branch has their own Stripe account connected to their Zooza account.

See [GoCardless Direct Debit](../guides/gocardless-direct-debit-mandates.md).

---

## Royalties

If your franchise model includes royalty fees, the Network Application can calculate and display royalties per branch based on rules you define. The exact calculation formula is set up at network level. Contact Zooza support to configure this for your network.

---

## What Zooza does not support (for this model)

| Limitation | Workaround |
|---|---|
| Pushing programme templates or settings from HQ to all branches automatically | Set up in one account, copy manually across branches |
| HQ collecting payments on behalf of franchisees and splitting them | Each branch collects payments independently via their own gateway |
| A single client account that works across all branches seamlessly | Clients have accounts per branch; transfers move the booking record between companies |
| Automatically applying a network-wide price change across all branches | Update each branch account manually |

---

## Common mistakes

- **Each franchisee creating their own network setup independently** — the network connection is set up once by Zooza, not by individual franchisees. If branches are not appearing in your Network Application, contact support to add them.
- **Not assigning product codes** — without product codes, the same programme appears under different names across branches and you cannot compare like-for-like in reports. Assign codes early, before the network grows.
- **Letting each branch name their programmes differently with no standard** — "Ballet Beginners", "Beginners Ballet", "Beg. Ballet Level 1" are three different products in reports unless you unify them with product codes.
- **Assuming HQ can push settings to branches** — HQ has read access to reporting and can initiate transfers. Day-to-day configuration still lives in each branch account. Plan for a rollout process when you want to standardise something network-wide.
