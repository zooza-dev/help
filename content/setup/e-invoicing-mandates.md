---
title: "Government e-invoicing mandates and Zooza"
description: "What mandatory e-invoicing means, whether the Slovak 2027 rule affects your courses, and how to handle B2B invoices alongside Zooza."
slug: "e-invoicing-mandates"
type: "setup"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: ["invoicing", "invoices", "billing", "vat", "compliance", "e-invoicing", "peppol", "digital-postman", "iso-27001", "slovakia", "czech-republic", "hungary"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-09-25"
related_articles: ["invoicing-overview", "billing-and-invoicing", "vat-management", "payments-and-billing-faq", "e-invoicing-faq"]
---

# Government e-invoicing mandates and Zooza

Several countries are introducing mandatory **structured e-invoicing** — most notably Slovakia from 1 January 2027. This page explains what those rules cover, whether they affect the invoices you issue from Zooza, and what to do if they do.

**Short answer:** Zooza itself does not issue structured e-invoices. If you need them, the invoices have to be issued by an **invoicing service that supports e-invoicing** — connected to Zooza as your invoice engine. Tell us which service you use and we can look at adding it. For invoices to individual clients (B2C), which is most course invoicing, no mandate applies and nothing changes.

> **This is general information, not tax or legal advice.** Rules and dates change. Confirm your own obligations with your accountant or tax advisor.
>
> Last reviewed: September 2026, against the Slovak Financial Administration's guidance of 11 September 2026.

---

## What "e-invoicing" means in a mandate

In everyday language, an electronic invoice is any invoice that is not printed. In the legal sense used by these mandates, it means something much narrower.

| An e-invoice under the mandate **is** | An e-invoice under the mandate **is not** |
|---|---|
| A structured, machine-readable file (`EN 16931`, in practice Peppol BIS 3.0 UBL XML) | A PDF invoice sent by email |
| Delivered over a certified network (Peppol) through an accredited provider | A scan or photo of a paper invoice |
| Accompanied by invoice data reported to the tax authority | An invoice downloaded from a portal |

Two separate obligations are often bundled together:

- **E-invoicing** — the format and the transport of the invoice itself.
- **E-reporting** — sending invoice data to the tax authority, close to real time.

Slovakia's 2027 rules introduce both. Hungary has had reporting (RTIR) for years without mandating an invoice format.

---

## What Zooza does today

Zooza generates **PDF invoices** — either through a built-in engine or through the accounting system you have connected as an [invoice engine](./invoicing-overview.md).

Zooza does **not** currently:

- generate structured `EN 16931` / Peppol XML invoices,
- send invoices over the Peppol network,
- report invoice data to any tax authority.

We are following the legislation in the countries we operate in. If this changes, this page will be updated.

---

## Does this affect me?

| Country | Who must issue structured e-invoices | For which transactions | From when |
|---|---|---|---|
| **Slovakia** | VAT-registered businesses (sole traders and companies alike) | **B2B and B2G only — B2C is excluded.** Also excluded: simplified invoices up to EUR 100, cash-register (eKasa) receipts up to EUR 400, and VAT-exempt supplies | 1 Jan 2027 (cross-border 1 Jul 2030) |
| **Czech Republic** | No domestic obligation yet; B2G runs through the NEN platform | B2B and B2C remain voluntary | Domestic B2B 1 Jan 2035, cross-border 1 Jul 2030 |
| **Hungary** | VAT-registered businesses — **data reporting only** (RTIR), no mandatory invoice format | B2B, B2C, intra-EU, export | Reporting in force since 2018/2021 |
| **EU (ViDA)** | All businesses issuing cross-border intra-EU B2B invoices | Cross-border intra-EU B2B | 1 Jul 2030 |

One extra Slovak rule worth knowing: from 2027 every business — including those not registered for VAT — must be able to **receive** an e-invoice, even if it never has to issue one. See [Every Slovak business must be able to receive e-invoices](#every-slovak-business-must-be-able-to-receive-e-invoices) below.

---

## How Slovak e-invoicing works in practice

The rules below come from the Slovak Financial Administration's guidance. They matter if the mandate applies to you, and the first one applies to every Slovak business.

### Every Slovak business must be able to receive e-invoices

From 1 January 2027, every legal entity and every self-employed person in Slovakia — **whether or not they are registered for VAT** — must be able to receive e-invoices. Consumers are not affected. In practice this means registering with a certified delivery provider, known as a **digital postman** (*digitálny poštár*). The official list is published by the Financial Administration at [vpds.financnasprava.sk](https://vpds.financnasprava.sk/). Many invoicing systems already include a digital postman; check with yours. Low-cost web apps exist where you simply download incoming invoices.

### What a digital postman does

A digital postman is a provider accredited by the Financial Administration that delivers e-invoices over the Peppol network and reports the invoice data to the tax authority on the sender's and the recipient's behalf. Your invoicing system hands the invoice to your postman; the postman delivers it and reports it. You do not report anything yourself.

### Choosing a provider: ISO/IEC 27001 from 1 July 2027

From **1 July 2027**, every digital postman must hold an **ISO/IEC 27001** certificate. This is an international standard for information security management: an independent auditor verifies, and re-verifies every year, that the provider has proper processes for access control, incident handling, backups and business continuity. It is the only independent evidence that your invoice data is safe with them. When choosing a provider:

- Prefer one that already holds ISO/IEC 27001 or has published a certification plan.
- Check that the certificate belongs to the same company you sign the contract with.
- Prefer the provider your invoicing system already works with.

A provider without the certificate may lose the right to operate after 1 July 2027, and you would have to migrate.

### The recipient's tax ID (DIČ) is the delivery address

E-invoices are delivered to an address built from the recipient's **DIČ** (tax identification number), not their IČO or VAT number. Without a DIČ an e-invoice cannot be delivered. If you invoice businesses, make sure their DIČ is recorded in their billing details.

### If the recipient cannot receive

If the recipient has no digital postman, the invoice is not delivered and your provider reports an error. Your legal obligation is still met, because you handed the invoice to your provider and the data reached the Financial Administration. Do not resend the invoice through the provider. Ask the recipient to register with a digital postman, and with their agreement you may send them the same invoice by e-mail.

### What counts as the invoice

For transactions under the mandate, the structured XML file is the invoice and must be archived for 10 years. A PDF is only a visual copy; it may be attached, but it is not the tax document. For everything outside the mandate — consumers, non-VAT payers, exempt supplies — a PDF remains a valid invoice.

### Corrections and credit notes

Credit notes and corrective invoices follow the same rules and the same 15-day deadline. The Financial Administration recommends issuing a credit note and a new invoice rather than editing the original. There is no "reject" message in the network; disputes are settled between the parties with a credit note.

### Timeline

| Date | What happens |
|---|---|
| 2026 | Voluntary period. E-invoices can be sent when both parties have a digital postman. |
| 1 January 2027 | Mandatory e-invoicing for Slovak VAT payers invoicing Slovak businesses and public bodies. Every Slovak business must be able to receive. |
| 1 July 2027 | Every digital postman must hold ISO/IEC 27001. |
| 1 July 2030 | Cross-border invoices join the regime (EU ViDA). |

A draft amendment from May 2026 proposes a penalty-free period from 1 January to 31 March 2027. It had not been adopted as of September 2026, and the obligations would apply regardless.

---

## Most course providers are not affected

The mandates cover business-to-business and business-to-government invoicing. An invoice for a course fee, issued to a parent or participant as a private individual, is a **consumer (B2C) invoice** — and B2C is explicitly excluded from the Slovak mandate.

If every invoice you issue from Zooza goes to an individual, there is nothing you need to do.

You may be affected if you:

- are **VAT-registered in Slovakia** and invoice companies — corporate training, an employer paying for an employee's place, a company covering several places — from 1 January 2027;
- invoice **public bodies** such as schools or municipalities (B2G);
- issue **cross-border invoices to businesses in other EU countries**, from 1 July 2030.

---

## What to do if it affects you

1. **Confirm the split with your accountant.** Work out which of your invoices are B2B or B2G, and whether the volume justifies a separate process.
2. **Use an invoicing service that supports e-invoicing.** This is the key step. Structured e-invoices must be issued and sent through an accredited provider (a Peppol access point) — in Slovakia the Financial Administration accredits these providers. Zooza's built-in invoicing cannot do this, so the document has to come from a service that can.
3. **Ask that service what they support and when.** Compliance follows the system that issues the invoice, not Zooza. If you already use a connected accounting system as your invoice engine — Fakturoid, ABRA Flexi, Xero, Számlázz.hu, SmartBill, Oblio — ask them directly about their e-invoicing plans.
4. **Tell us which service you need.** If the service that handles your e-invoicing is not yet available as a Zooza invoice engine, contact us through the in-app chat or your account manager. We can look at adding it as an integration, so invoices keep flowing from Zooza instead of being issued by hand. Knowing which services our customers actually need is what lets us prioritise.
5. **Keep using Zooza for course invoices to individuals** as you do today. Nothing changes for them.
6. **Check that you can receive e-invoices** if you are a Slovak business — this applies even to non-VAT payers.

---

## Will Zooza support e-invoicing?

Zooza will not become a Peppol provider itself. Because course invoicing is overwhelmingly B2C, the current mandates leave most Zooza accounts outside their scope, and Slovakia's technical channel is itself due to move to a Peppol-based model.

The realistic route is the one Zooza already uses for accounting systems: **you invoice through a service that handles e-invoicing, and Zooza connects to it as an invoice engine.** So if you need this:

- Tell us **which service** you use or plan to use for e-invoicing.
- Tell us **which country and which transaction types** are affected for you (SK B2B, B2G, cross-border EU).

Reach us through the in-app chat or your account manager. Requests like these are how we decide which integrations to build next — see [Your accounting system isn't listed?](./invoicing-overview.md#your-accounting-system-isnt-listed) in the invoicing overview.

---

## Related

- [Invoicing in Zooza — Overview](./invoicing-overview.md) — invoice engines, what Zooza generates, what it does not
- [Billing and invoicing](./billing-and-invoicing.md) — automatic and manual invoice generation, numbering
- [VAT management](../guides/vat-management.md) — VAT rates, invoice profiles, booking-level VAT
- [E-invoicing FAQ](../faq/e-invoicing-faq.md) — short answers about the Slovak 2027 rules
- [Payments and Billing FAQ](../faq/payments-and-billing-faq.md) — common invoicing questions
