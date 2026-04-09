---
title: "Adult Language School — Groups, Individual Lessons, and Corporate Clients"
description: "Most language schools serve a mix of these:"
slug: "adult-language-school"
type: "business-model"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: ["business-model", "language", "adults", "corporate", "individual", "groups", "term", "invoice"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-04-09"
---

# Adult Language School — Groups, Individual Lessons, and Corporate Clients

## This guide is for you if

- You run language courses for adults — group classes, individual lessons, or both
- Some clients are private individuals; others are companies paying for their employees
- You run fixed-term courses (e.g. one semester) and/or ongoing individual sessions sold in packages
- You need to issue invoices — either to individuals or to companies with full billing details
- Examples: language schools, corporate language training providers, private language tutors scaling to a team of instructors

---

## The three client types you will encounter

Most language schools serve a mix of these:

| Client type | How they book | How they pay | Invoice to |
|---|---|---|---|
| **Private individual** | Registers online, pays by card | Card (Stripe) or bank transfer | Their personal details |
| **Corporate — employee pays** | Employee registers online | Card or bank transfer | Company details (employee provides them at booking) |
| **Corporate — company pays** | You create the booking manually | Invoice sent to the company | Company: name, address, VAT/Tax ID |

Each type needs a slightly different setup. The good news: Zooza handles all three from the same Programme.

---

## Programme structure for a language school

### Group courses — term model

A group course runs for a fixed term (e.g. September–January, 16 weeks). Each level is a **Programme**. Each specific group — a particular day, time, and level — is a **Class**.

- Programme: "Intermediate English — Autumn 2026"
- Classes: "Monday 18:00 group", "Wednesday 19:30 group"

Set the Programme type to *Booking for the full programme duration*. Use **Term payment** with a Unit price per session — this gives you automatic pro-rata for students who join mid-term.

If your groups run continuously without a defined end date, use **Membership** price type with a monthly fee instead. See [Monthly subscription model](./children-group-activities-subscription.md) — the setup is identical for adults.

### Individual lessons — package model

Private clients buy a package of sessions (e.g. 10 lessons). The setup is the same as for any individual lesson provider.

Set the Programme type to *Booking for the full programme duration*, target audience *1-to-1 classes*. Sell packages using **One-off payment** for the full package, or **Term payment** split into two instalments for longer engagements.

See [Individual lessons](./individual-lessons.md) for the full setup.

---

## Corporate clients — enabling company invoices

When a company pays for their employee's lessons, the invoice must go to the company, not the individual.

Enable **Business booking** on the Programme:

1. Go to Programme → **Extra fields**
2. Enable at least one of: Company name, Business address, Business ID, Tax ID, VAT number
3. On the booking form, the client sees an option to enrol as a company — they click it and fill in the company details

Any booking with company details filled in is automatically flagged as a **Business Booking** in the system. When you generate an invoice, it uses the company details as the billing address instead of the individual's details.

See [Business booking](../guides/business-booking.md).

### When the company books and pays directly (not the employee)

For larger corporate contracts — where the HR or training manager registers multiple employees and receives one invoice for all of them — create the bookings manually:

1. Create a booking for each employee from the admin panel
2. Link all bookings together so they share a single payment (one invoice, one bank transfer reference)
3. Send the invoice to the company

Use **Linked bookings** to bundle multiple employee registrations under one payment. The company receives one invoice covering all employees, with one payment reference. See [Linked bookings](../guides/linked-bookings.md).

---

## Invoicing

Language schools almost always need to issue invoices — especially for corporate clients. Make sure your invoicing is configured before you go live.

Key steps:
1. Fill in your **billing profile** in Settings → Invoice profiles — your company name, address, and Tax/VAT ID
2. Connect **Xero** if you use it for accounting (Settings → Integrations) — invoices sync automatically
3. For corporate bookings, the invoice pulls the company details the client entered at booking

If a corporate client needs the invoice in a specific format (e.g. with a purchase order number), use the **extra fields** to collect that at booking and include it in the invoice template.

---

## Placement tests and level assessment

Zooza does not have a built-in placement test. The common approach:

- Use a **trial session** or **lead collection class** to register interest before the term starts
- Run your placement test outside Zooza (Google Form, email, in person)
- Once you know the student's level, assign them to the correct group manually

If you want to collect basic self-assessment information at registration, add a custom **extra field** (e.g. a dropdown: Beginner / Elementary / Intermediate / Advanced). This is visible on the booking record and in exports.

---

## Managing a group of corporate employees

When a company sends 6 employees to the same group course:

1. Each employee registers individually (or you create bookings manually for all of them)
2. Link all 6 bookings together — one master booking receives the total payment
3. Issue one invoice to the company for the full amount
4. Attendance and progress are tracked per individual booking — you can see who attended which session

If an employee leaves mid-course and is replaced by a new one, transfer the original booking to the new employee. See [Transfer and copy bookings](../guides/transfer-and-copy-bookings.md).

---

## What Zooza does not support (for this model)

| Limitation | Workaround |
|---|---|
| Built-in placement tests or level assessment | Collect self-assessment via extra fields; run tests externally |
| Automatic invoicing directly to a company email without employee involvement | Create the booking manually and send the invoice from admin |
| Progress tracking or lesson notes visible to the corporate client | Use the Documents feature to attach notes or progress reports to a booking |

---

## Common mistakes

- **Not enabling Business booking fields before launch** — if a corporate client tries to register and there is no company field on the form, they cannot provide their billing details. Enable it before you open registrations.
- **Creating a separate Programme for each corporate client** — one Programme per course level, regardless of who pays. The corporate vs individual distinction is handled at the booking level, not the Programme level.
- **Forgetting to link employee bookings** — if 6 employees book separately, you end up with 6 separate invoices and 6 separate payment references. Link the bookings before you issue the invoice.
- **Issuing invoices before the billing profile is complete** — invoices generated without your company's VAT or Tax ID may not be legally valid in your jurisdiction. Fill in the billing profile first.
