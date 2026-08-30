---
title: "Zooza Glossary"
slug: "glossary"
type: "glossary"
product_area: "Settings"
audience: ["admin", "client"]
tags: ["glossary", "terminology", "definitions"]
status: "published"
last_converted: "2026-08-30"
---

# Zooza Glossary

This glossary explains the terms used across Zooza. Some terms differ depending on whether you are managing your business (admin view) or your clients are booking through your website (client view).

---

## A

### Attendee
The person who physically attends sessions. May differ from the Client — for example, a parent (Client) who books on behalf of their child (Attendee). For adult learners, the Client and Attendee are the same person.

---

### Aliquot
A reduced price for a client who joins after a programme has already started, calculated from the sessions they will actually attend rather than the full run. Requires a price per session, so Zooza has something to count.

### Application Communication Language
The language Zooza writes to your clients in — automatic emails and the message templates behind them. Set in **Settings → General**.

> **Not the same as your own view.** The admin panel language is switched at the bottom of the Dashboard. And an embedded booking form or calendar takes its language from your website, not from this setting.

### Awaiting payment
A booking that is confirmed but not yet paid, inside the grace period you allow. It becomes *Unpaid* when that window expires. See [Debt](#debt).

---

## B

### Billable session
A session that counts towards the total used for price calculation in Programme or Class settings. Marking a session as non-billable (for example, public holidays) excludes it from the price formula. This is a pricing setting only, not an attendance feature.

### Booking
**Admin view:** A client's formal commitment to attend a Class. Creates a payment obligation.
**Client view:** See [Enrolment](#enrolment).

> Formerly called: *Registration*

---

### Block
A separately purchasable segment of sessions within one Class — Mondays-only, Tuesdays-only, or a January run inside a longer term. Each Block has its own price, and clients buy only the ones they need.

Each Block also decides for itself whether it is offered for online booking and whether it is offered for trials — two independent settings.

> Internally called: *segment*, *schedule segment* — not used in the app or in help content.

---

## C

### Class
A scheduled class within a Programme, typically differentiated by day/time, level, or location. One Class contains multiple Sessions.

> Also referred to as: *Group*, *Groups* (in localised app versions, e.g. Romanian: *Grupă*)
> Formerly called: *Class*, *Timetable*

### Client
The person who holds the account, pays, and manages bookings. Identified by email address. A Client may book on behalf of family members (Attendees).

### Client Profile
The self-service dashboard where clients manage their bookings, payments, and family members. Accessed via email link — no password required.

### Copy
Duplicate a booking to a different Class, Class, or Programme. The original booking remains unchanged. A new booking is created in the target Class.

**Copy vs Transfer:** Copy keeps the original booking; [Transfer](#transfer) removes it.

---

### Cancel (registration)
Ending a booking while keeping the record. The client stops attending; the booking stays visible and can be set back to active. Distinct from deleting it.

### Cancel vs. Archive vs. Delete
Three different things people reach for interchangeably:

- **Cancel** — the client stops attending; the record stays.
- **Archive** — hide something finished from your active lists, keeping every booking, payment and attendance record. Reversible any time.
- **Delete** — move it to [Trash](#trash), recoverable for 30 days, permanent after that.

For a class that has run, archive. Deleting a class does not delete its bookings — it leaves them with no class attached.

### Cancellation fee
An amount retained when a client cancels, rather than refunding in full.

### Credit
An amount held on a booking for the client to use later. Comes in several kinds — a make-up session credit, a discount credit created from an overpayment, an entry pass, a gift voucher — all listed together on the booking under **Credits and make-up sessions**.

> Do not confuse a booking credit with an [Entry pass](#entry-pass). Both are called "credit" in conversation; they are managed in different places.

---

## D

### Debt
The outstanding amount a client owes for a booking. A negative balance means the client has overpaid (credit). Recalculated automatically.

---

### Down payment
A deposit taken at booking, with the rest collected later. Set per programme.

---

## E

### Enrolment
**Client view:** A client's registration for a Class. The same record as a [Booking](#booking) — "Enrolment" is the term used in the client portal and booking widget.
**Admin view:** See [Booking](#booking).

### Entry pass
A prepaid bundle granting access to a set number of sessions (visits-based) or a credit amount (money-based). Used with Pay-as-you-go programmes.

> Also known as: *Credit pass*, *Visit pass*

---

## F

### Feedback
Structured feedback collected from clients after sessions or at the end of a programme.

> Formerly called: *Programme feedback*

### Free credits
An allowance granted to a specific booking that lets the client attend extra sessions without paying.

**Free credits vs Make-up sessions:** Free credits are granted by an admin as an allowance. [Make-up sessions](#make-up-session) are earned automatically when a client cancels a session before the deadline.

---

## I

### Inbound payment
A bank transfer received from a client that the system automatically attempts to match (pair) to the correct booking. Inbound payments arrive via GoCardless bank account data, bank email notifications, or CSV import. Once matched, the payment is recorded on the booking and the status changes to Paired.

> **GoCardless note:** In the inbound payments context, GoCardless reads transactions from your bank account (open banking). This is separate from GoCardless as a direct debit processor. The client still pays by normal bank transfer — GoCardless only detects it.

### Invoice
A document issued to a client confirming a payment received for a booking or product purchase. In Zooza, invoices are generated per billing period and sent to the client by email as a PDF. Invoices are created by the connected invoice engine.

### Invoice Engine
The external invoicing or accounting service that creates the actual invoice document. Zooza collects payment data and sends it to the engine, which assigns an invoice number and generates a PDF. Zooza includes a built-in engine (no setup required); companies can also connect their own accounting system (Xero, Fakturoid, ABRA Flexi, SmartBill, Számlázz.hu, Oblio).

### Invoice buyer
The entity recorded as the recipient (orderer) on an invoice — their name, address, and company/tax details. The invoice buyer may differ from the client who registered. For example, a parent registers a child but needs the invoice in their company name. Zooza stores invoice buyer profiles per client and reuses them across bookings.

### Invoice Profile
The "From" section on an invoice — a legal entity with your company name, address and tax IDs (Business ID, Tax ID, VAT number), plus its invoice numbering. A company can have multiple Invoice Profiles, one per billing entity, and one of them is the default. The bank account is a separate entity that belongs to the profile — see *Bank account*. A profile is resolved down the chain Default profile → Programme → Class → Booking (and via the product for orders); the lowest level that sets one wins.

> Formerly called: *Billing profile*

### Bank account
One IBAN belonging to exactly one Invoice Profile, with its SWIFT code and account holder name. A profile can hold several bank accounts and marks one as its default. The account is what payment instructions, QR codes and bank-statement matching use, and each account has its own statement connection (GoCardless or email notifications). The same IBAN cannot be used on two Invoice Profiles in one company.

### Invoice Line Types (multi-line)
A configuration within an Invoice Profile that splits invoice amounts into separate lines per transaction type (e.g. Course Payment, Registration Fee, Discount). When at least one line type is enabled, multi-line invoicing is active. When no types are configured, a single-line invoice is generated.

---

### Instructor
A person who teaches sessions and holds a login with a role that limits what they see. An instructor is not a Client, even when they also book classes.

---

## L

### Lead Collection
A class with no sessions, used to gather interest before a schedule exists. No debt is created and no price is shown. Add sessions and it becomes an ordinary class automatically.

### Location
A place where sessions happen. Holds the address and the region that decides which public holidays and school breaks apply.

### Loyalty Program
Automatic discounts based on who the client already is — sibling discounts, returning-customer pricing, referrals — applied at booking rather than by handing out codes.

---

## M

### Make-up session
A make-up session a client can attend after cancelling a scheduled session in advance (before the cancellation deadline). The make-up credit is generated automatically on cancellation.

> Also known as: *Make-up session*

### Membership
An ongoing programme type with a recurring fixed charge and no fixed end date (monthly, quarterly, etc.).

> Also known as: *Subscription*

---

## N

### Network transfer
Moving one or more client bookings from one company to another company within the same Zooza franchise network. Used when a client switches branches or when a location is being closed. Available in bulk via **Bookings → Bulk action → Network transfer**.

> Not to be confused with: [Transfer (booking)](#transfer) — which moves a booking within the same company.

---

## O

### One-off Event
A single session on a specific date with no repeating schedule. Used for workshops, lectures, consultations, or special events.

> Formerly called: *One-time programme*, *Registration for one session*

---

## P

### Pay-as-you-go
A flexible programme type where clients book and pay for individual sessions rather than committing to a full term.

> Formerly called: *Open programme*, *Open registration*

### Payment Plan
The configuration that defines when and how often a client is billed for a booking — one-time, monthly, quarterly, by-block, and so on.

> Formerly called: *Payment schedule*, *Scheduled payments*, *Invoice profile*

### Private class
**Client view:** A class with a single attendee (individual/private session).
**Admin view:** See [1-to-1 class](#1-to-1-class).

### Programme
The top-level container for an activity type. Holds pricing, payment settings, booking form configuration, and scheduling rules. One Programme contains multiple Classes.

**Admin view:** Programme
**Client view:** Class

> Also referred to as: *Course*, *Courses* (in localised app versions, e.g. Romanian: *Curs*)
> Formerly called: *Programme*

---

### Payment template
A reusable rule for how a price is collected: the frequency, the number of instalments, the due day, any discount. Created once and attached to any number of programmes.

A template's **type** is chosen when you create it and cannot be changed afterwards — a membership fee needs a template made as a membership template.

> Not the same as a [Payment Plan](#payment-plan), which is the actual schedule of amounts and dates on one client's booking.

### Pending
A booking submitted but not yet confirmed by you.

### Public booking page
A plain page generated automatically for every account, listing everything open for registration, at `zooza.site/your-account-name/register` — with `/calendar` for the schedule. No setup and no cost.

Copy the exact address from the **Share** button in the Classes list rather than typing it. Accounts outside Europe carry their region: `zooza.site/uk/…`, `zooza.site/asia/…`.

> A bridge until Zooza is embedded on your own website, not a replacement for it. Distinct from **Zooza Sites**, the paid product with its own domain and templates.

---

## R

### Reference number
A unique identifier included with bank transfer payments, used to automatically match incoming payments to the correct client booking.

> Formerly called: *Variable symbol*

---

### Refund
Money genuinely returned to a client, recorded as its own transaction. Use it only when funds actually leave your account — correcting a wrong record is a different action, and using Refund for it creates a phantom transaction in your reports.

### Revenue
What you have earned, as distinct from what has been paid. A booking can be revenue before the money arrives.

---

## S

### Session
A single scheduled meeting within a Class, with a specific date and time. Attendance is recorded at session level.

> Also referred to as: *Lesson*, *Lessons* (in localised app versions, e.g. Romanian: *Lecție*)

### Stripe Clearing Account
A bank account in Xero (or another accounting system) used as an intermediary between individual Zooza invoice payments and Stripe bulk payouts. When a client pays via Stripe, the payment is recorded against this clearing account in Xero. When Stripe pays out to your bank, the bulk transfer is matched against the same clearing account. This approach prevents double-counting and allows individual invoice-level tracking alongside bulk bank reconciliation.

### Stripe Express vs Stripe Standard
Two types of Stripe accounts supported by Zooza. Both process payments identically. Stripe Standard gives the company owner direct access to the full Stripe dashboard, payout reporting, and VAT invoices for Stripe fees. Stripe Express is a simplified account managed via the Stripe Express dashboard with limited access to some reports. Companies needing accountant-level access and VAT fee invoices should use Stripe Standard.

### Payment Sync
The automatic process by which Zooza sends payment records to the connected invoice engine (e.g. Xero, Fakturoid, Számlázz.hu) after an invoice is created. In Xero, this marks each invoice as paid and records the individual payment as a transaction against the bank account code configured in the Invoice Profile. Not all engines support payment sync — see [Invoicing overview](../setup/invoicing-overview.md) for a comparison.

---

## T

### Term Payment
A payment covering a specific term or billing period.

> Formerly called: *Programme fee*

### Transfer
Move a booking from one Class, Class, or Programme to another. The original booking ends and a new booking is created in the target Class.

**Transfer vs Copy:** Transfer moves the booking (original ends); [Copy](#copy) duplicates it (original stays).

### Trial
A Zooza feature that makes specific Classes available for prospective clients to try before committing to full enrolment. Trial automates the journey from the first session through to enrolment. Each Trial has its own price (can be free), its own booking form, and is published separately via the widget. Status is tracked: Trial Started → Trial Won or Trial Lost.

> Not to be confused with a regular Session that has been manually named "trial session" — those have no automation.

---

### Trash
Where deleted registrations, classes, sessions and cancelled scheduled payments go. Restorable for **30 days** from **Settings → Tools → Trash**; permanently gone after that.

---

## A (features)

### Auto-enrolment
A feature that contacts clients before their current Class ends and invites them to re-enrol for the next period. The client receives a personalised link, opens their Client Profile, and selects which Class to continue into. No booking is created automatically — the client must actively confirm.

---

## V

### Venue
The physical location where sessions take place.

> Formerly called: *Place*, *Location*

---

## W

### Widget
The embeddable booking interface placed on your website. Widgets use client-facing terminology throughout (for example, "Class" instead of "Programme", "Enrolment" instead of "Booking").

---

### Waiting list
A queue for something not currently available. Zooza has two, and they are separate features: the **class waiting list** for a full class, approved by you by hand; and the **make-up waiting list** for a full make-up slot, which resolves automatically.

There is no switch called "waiting list". To stop the class queue, set the programme to hide a class once it reaches full capacity.

> Slovak: *poradovník* — used for both, so always establish which one is meant.

### Widget key
The identifier tying an embedded widget on your website back to your account, found in **Team & Settings → Publish → Widget** and already included in the embed code.

> **Not a REST API key.** Embedding the booking form, calendar or client profile needs no API key at all.

---

## 1

### 1-to-1 class
A class with a single attendee (individual or private session).

**Admin view:** 1-to-1 class
**Client view:** Private class

> Formerly called: *Individual class*
