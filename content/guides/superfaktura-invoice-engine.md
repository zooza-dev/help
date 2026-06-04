---
title: "Connect SuperFaktura as Your Invoice Engine"
description: "Configure Zooza to generate and push invoices directly into your SuperFaktura account — available for SK and CZ companies."
slug: "superfaktura-invoice-engine"
type: "setup"
product_area: "Settings"
sub_area: ""
audience: ["admin"]
tags: ["invoicing", "invoice-engine", "superfaktura", "settings", "integration", "SK", "CZ"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-06-04"
related_articles: ["invoice-buyer-data", "vat-management", "price-and-payment-setup"]
---

# Connect SuperFaktura as Your Invoice Engine

Zooza can generate invoices and push them directly into **SuperFaktura** (available at `moja.superfaktura.sk` for Slovakia, `moje.superfaktura.cz` for the Czech Republic). Once connected, Zooza creates the invoice in SuperFaktura at the moment a payment is processed — no manual exporting required.

> **Availability:** SuperFaktura is available for Slovak and Czech companies only.

## Prerequisites

- An active SuperFaktura account (SK or CZ).
- Your SuperFaktura **API email** and **API key** (found in your SuperFaktura account under **Nástroje / Tools → API access**).

## Setting up the connection

1. In Zooza, go to **Settings → Invoice Settings**.
2. In the **Invoice Engine** section, select **SuperFaktura** from the dropdown.
3. Fill in the credential fields:

   | Field | Required | Description |
   |---|---|---|
   | Email | Yes | The email address you use to log in to SuperFaktura |
   | API key | Yes | The API key from SuperFaktura → Tools → API access |
   | Company ID | No | Only needed if your SuperFaktura user manages multiple company accounts |
   | Region | No | `SK` (Slovakia, default) or `CZ` (Czech Republic) |

4. Click **Save**.

Zooza will now send invoices to SuperFaktura whenever an invoice is generated for a payment.

## How invoices are created in SuperFaktura

- **Invoice data** — Zooza fills in the buyer details, line items (course/service), VAT rate per line, currency, payment method, and due date.
- **Invoice number** — controlled by the **Invoice Number Template** you configure in Zooza (Settings → Invoice Settings → Number format). The number is passed verbatim to SuperFaktura.
- **Paid status** — if the payment is fully paid at invoice-generation time, SuperFaktura marks the invoice as paid inline. No separate payment-sync step.
- **Multi-line invoices** — if your account uses multi-line invoicing (e.g., one line per course component), each line is sent as a separate `InvoiceItem` in SuperFaktura.

## Invoice number format

Use the **Invoice Number Template** field in Zooza to define your format. Common examples:

| Template | Result |
|---|---|
| (blank) | Uses the order ID as the number |
| `{N}` | Sequential counter: 1, 2, 3… |
| `{YYYY}/{N}` | Year-prefixed: 2026/1, 2026/2… |
| `ZOOZA/{YYYY}/{MM}/{N}` | Custom prefix with year and month |

The number is sent to SuperFaktura exactly as rendered — SuperFaktura will use it verbatim rather than assigning its own sequence.

## API key security

- When you load the invoice settings after saving, the API key is displayed as `********` for security.
- To update the key, type a new value in the field and save. Saving the masked value (`********`) unchanged does not overwrite the stored key.

## Troubleshooting

**Invoice not appearing in SuperFaktura:**
- Verify the API email and API key are correct (copy them fresh from SuperFaktura → Nástroje → API access).
- Check that the region matches your SuperFaktura account (SK vs CZ).
- If you manage multiple companies in SuperFaktura, add the correct Company ID.

**Wrong invoice number format:**
- The number template in Zooza controls the format. Adjust it under Settings → Invoice Settings → Number format.

**Currency mismatch:**
- Zooza sends the currency from the payment. Ensure your SuperFaktura account supports that currency.
