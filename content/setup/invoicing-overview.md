---
title: "Invoicing in Zooza — Overview"
description: "Zooza tracks payments and can generate invoices for course registrations and product purchases."
slug: "invoicing-overview"
type: "setup"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: ["invoicing", "invoice-engine", "billing", "xero", "fakturoid", "abra-flexi", "smartbill", "szamlazz", "oblio", "multi-line", "credit-note", "pohoda", "omega", "export"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-03-25"
---

# Invoicing in Zooza — Overview

Zooza tracks payments and can generate invoices for course registrations and product purchases. Every account comes with built-in invoicing — no setup required to get started. If you use your own accounting system, you can connect it as an **invoice engine** and invoices will appear there automatically.

---

## How invoicing works

When a payment is recorded in Zooza, the following happens:

1. Zooza collects all payment data (who paid, how much, for what, billing period).
2. The data is sent to the connected **invoice engine** (built-in by default).
3. The engine assigns an official invoice number and generates a PDF.
4. Zooza stores the PDF and sends it to the client by email (if notifications are enabled).

An **invoice engine** is the invoicing or accounting service where the actual invoice document is created. Zooza handles the data; the engine handles the document.

---

## Built-in invoicing (no setup needed)

Every Zooza account includes built-in invoicing. It works immediately — no credentials, no third-party account required.

What you do need to configure:
- Your **Invoice Profile** (company name, address, tax IDs, IBAN) — this is the "From" section on every invoice.

See [Billing and invoicing](./billing-and-invoicing.md) for how to set up your Invoice Profile.

---

## Connecting your own accounting system

If you want invoices to appear directly in your accounting or ERP system, go to **Settings → Billing → Invoice Settings** (or open `/#settings/invoice_profiles`) and select your engine.

The engines available to you depend on your country and account configuration.

- [Fakturoid](./fakturoid-invoices.md) — CZ / SK
- [ABRA Flexi](./abra-flexi-invoices.md) — CZ / SK
- [Xero](./xero-integration.md) — International
- [Számlázz.hu](./szamlazz-invoices.md) — Hungary
- [SmartBill](./smartbill-invoices.md) — Romania
- [Oblio](./oblio-invoices.md) — Romania

### Engine comparison

| Engine | Market | Setup | Payment sync |
|---|---|---|---|
| Built-in | All | None — automatic | No |
| Fakturoid | CZ / SK | Connect once (OAuth) | Partial |
| ABRA Flexi | CZ / SK | Username + password + server URL | No |
| Xero | International | Connect (OAuth) + account codes | Full |
| Számlázz.hu | Hungary | Paste API token | Partial (pre-paid) |
| SmartBill | Romania | Email + API token + CIF | No |
| Oblio | Romania | Email + API token + document series | No |

---

## Exporting invoices to your accounting software

If you use accounting software that doesn't have a live connection but can import data (e.g. Pohoda, Omega, SAP, MRP), you can export invoice data as a file and import it manually.

Go to **Settings → Integrations** to see which accounting export formats are available for your region.

See [Integrations](./integrations-hub.md) for the full list.

---

## Invoice Profiles

An **Invoice Profile** is the "From" section on the invoice — your company name, address, tax IDs, and IBAN.

- Every company has a **default profile** used unless you override it.
- You can create **multiple profiles** (e.g. different billing entities or bank accounts).
- Profiles can be assigned per **course** — if none is set on the course, the company default is used.
- For **products**, the company default profile is always used (no per-product assignment).

Go to [Billing and invoicing](./billing-and-invoicing.md) to manage profiles.

---

## Generating invoices

Invoices can be generated in two ways:

**Automatic** — Zooza generates an invoice every time a payment is recorded. Enable this under **Settings → Billing → Automatic invoice generation**.

**Manual** — Open any booking, go to the **Payments** tile, and click **Generate invoice**. Works even when automatic generation is off.

A single booking can have multiple invoices over time (e.g. one per instalment). Each invoice covers a billing period — from the day after the previous invoice ended, to the current date.

See [Billing and invoicing](./billing-and-invoicing.md) for the full workflow.

---

## Multi-line invoices

By default, Zooza generates a **single-line invoice** — one line item showing the total amount.

**Multi-line invoices** show an itemised breakdown: course payment, registration fee, discount, credit — each as a separate line. This is available on all engines.

Multi-line activates automatically when you configure **transaction type mappings** in the Invoice Settings. No mappings = single-line (default behaviour, nothing changes).

See [Multi-line invoices](./billing-and-invoicing.md#multi-line-invoices) for how to set this up.

---

## What Zooza doesn't do

| Topic | What to expect |
|---|---|
| **Credit notes / correction invoices** | Zooza does not generate credit notes. If you need to issue a correction invoice, do it directly in your accounting system (Xero, Fakturoid, etc.). |
| **Editing invoices after creation** | You can edit the period, date, and description on built-in invoices. Invoices in external systems must be edited there — changes do not sync back to Zooza. |
| **Invoice deletion** | Invoices cannot be deleted in Zooza. Void or cancel them in your accounting system if needed. |
| **PDF for Xero invoices** | Zooza links to the invoice in Xero but does not store a local PDF copy. |
| **Payment sync for most engines** | Only Xero (full), Fakturoid (partial), and Számlázz.hu (partial) sync payments back to the external system. Other engines track payments in Zooza only. |

---

## Your accounting system isn't listed?

If your system isn't supported yet, contact us — we can discuss adding an integration. Reach out via the in-app chat or your account manager.

---

## Related

- [Billing and invoicing](./billing-and-invoicing.md) — Invoice Profiles, IBAN, auto/manual generation
- [Invoice buyer data](../guides/invoice-buyer-data.md) — managing orderer details and regenerating invoices
- [Invoices list](../reference/invoices-list.md) — browsing and downloading invoices
- [Multi-line invoices](./billing-and-invoicing.md#multi-line-invoices) — itemised invoice breakdown
- [Integrations](./integrations-hub.md) — accounting export formats (Pohoda, Omega, SAP)
- [Payments and Billing FAQ](../faq/payments-and-billing-faq.md) — common questions
