---
title: "Getting Started with Zooza"
slug: "getting-started-with-zooza"
type: "setup"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: []
status: "published"
source_legacy_path: "legacy/0015_Welcome to Zooza.html"
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-11"
---

# Getting Started with Zooza

![Screenshot](../../assets/images/customizing-widgets-01.png)

From First Login to Everyday Use

This guide is for owners and admins of children’s activity businesses (clubs, classes, franchises) who want to:

- get their first programme live,
- let parents book and pay online,
- and avoid creating a setup they’ll regret later.

You don’t need to be “techy”. If you follow this guide, in about 30-60 minutes you will:

- understand how Zooza thinks about your classes,
- create your first programme, timetable, and sessions,
- connect payments and invoicing,
- test the full journey as a parent,
- learn what to do with bookings in day-to-day situations.

1. How Zooza thinks about your business

## First, the mental model. Everything in Zooza is built on a few key blocks.

### Core structure

- Programme (Programme / Product)What you sell.Example: “WeeOnes – 15 months to 2 years”
- Timetable (Class / Class)A specific instance of the programme –place, instructor(s), and capacity.Example: “City Pool, Laura – max 10 children”
- SessionA single date in a timetable.Example: “Monday 10:00 on 10 March, 17 March, 24 March…”

### People & bookings

- Client (Parent)One email address representing a parent. They can manage multiple children.
- Booking / RegistrationA child enrolled in one timetable, with payments, attendance and communication attached.

You can imagine it like this:

![Screenshot](../../assets/images/individual-lessons-climbing-wall-02.png)

Programme → Timetable → Sessionsand on each timetable you have Bookings from Clients (Parents).

All reporting, payments, reminders and automations in Zooza use this structure.

If you need more detail, see: Glossary of Key Terms (at the end of this article).

2. Do these steps first inside your Zooza account

1. Log in & find your accountsGo to [Zooza Accesss](https://www.zooza.online/access/)and log in with your email.
2. Add your venues (Zooza > Settings > Locations)Add all locations you use: pools, halls, studios, classrooms.
3. You will reuse these when creating timetables.
4. Invite your team (Zooza > Settings > Access)Add your team members (owners, admins, instructors).
5. Assign roles and permissions.
6. [Guide: Roles & Permissions](../guides/user-roles.md)
7. Set up your billing profile (Zooza > Settings > Billing)Add your company name, address, company ID, IBAN and other details.
8. If you use Billing software (e.g. Xero), you can keep billing details in your billing software and connect it to Zooza.
9. [Guide: How Invoicing Works](https://support.zooza.online/portal/en/kb/articles/billing-settings)
10. Decide your main payment modelDo you think mostly in:Terms (Autumn / Spring / block of weeks), or
11. Term Fee (paid monthly, one-off, quarterly, after/before N sessions...)
12. Ongoing membership (rolling weekly classes), or
13. Pay-per-session / drop in?
14. This will help you pick the right payment template in the next steps.

![Screenshot](../../assets/images/customizing-widgets-01.png)

TipIf you are unsure, start with Term Fee (price per term, split into instalments).You can refine and add more payment models later.

3. Create your first Programme, Timetable and Sessions

## Now we’ll set up your first real offering.

### 3.1 Create a Programme

In your Live account:

1. Go to Programmes. (Zooza > Programmes)
2. Click Create Programme.
3. Fill in:Name (e.g. “Dance for Tots – 2–3 years”)
4. Description for parents
5. Set your price:choose One-off, Term Fee, Membership, or Per session,
6. define the main price (you can adjust or add discounts later).

### 3.2 Add a Timetable (Class / Class)

1. Inside the programme, go to Timetables / Classes.
2. Click Add Timetable.
3. Set:Location / venue
4. Instructor
5. Capacity (max children)

Example:
“City Pool, Laura – max 10 children

### 3.3 Generate Sessions

1. From the timetable, choose Add Sessions.
2. Select the date range (term / block).
3. Confirm the list of dates (sessions).

You should now see a calendar of sessions for that timetable.


You can create multiple timetables with sessions under the same programme (e.g. Monday 10:00, Wednesday 16:00).


At this point, you have:

- 1 Programme,
- at least 1 Timetable,
- a list of Sessions in your calendar.

4. Connect payments & invoicing

## Next, connect how money flows.

### 4.1 Connect your payment gateway

Go to Zooza > Settings > Payments:

1. Stripe (card payments)Connect your existing Stripe account.
2. Use Stripe for single payments or instalments by card.
3. GoCardless (direct debit)Connect your GoCardless account.
4. Use it for recurring direct debit (great for memberships and monthly term fees).
5. If you prefer bank transfers, you can still: (Zooza > Setting > Billing > Billing Profiles > Pair Bank Account) (For EU&UK banks)

- generate payment requests with bank details / QR codes,
- record payments manually, or
- enable automatic matching with your bank (where supported).

### 4.2 Set your payment templates

In Payment Templates, create or adjust:

- Monthly template (for memberships or term split into months)
- Per term template
- Per session or block template

This tells Zooza:

- when to create payment requests,
- for which amounts,
- how to show them to parents.

![Screenshot](../../assets/images/customizing-widgets-01.png)

Tip – Payment templates

Zooza comes with default payment templates (monthly, per term, per session), so you can start using them straight away. If you later want to change how often parents are charged or how many instalments you use, go to Zooza → Settings → Payments → Payment templates and edit or create your own template there.

5. Test the journey as a parent

## Before inviting real parents, experience Zooza from their perspective.

### 5.1 Open your booking link or demo page (your onboarding team can share it).

### 5.2 Register as a parent

1. Use a different email address than your work/admin email.
2. Choose the programme and timetable you created.
3. Fill in the form:your details,
4. child’s details,
5. consents.
6. Select a payment option (card, direct debit, bank, trial – depending on your setup).
7. Submit the booking.

### 5.3 Check what happens next

As the parent, you should receive:

- Booking confirmation email (and PIN code if used),
- Access to the Parent Portal / Parent Portal – with:upcoming sessions,
- payment overview,
- invoices (after payment).

As the admin, you should see:

- new Client (parent) in CRM,
- new Booking in that timetable,
- a Payment Request (and invoice when paid).

If something doesn’t look right

- Don’t worry. This is why we use the Playground first.
- Adjust your templates, pricing, or settings.
- Only when you are happy with the experience, move to Live.

### 5.4 Check your messages

Zooza > Communication > Templates


Before going fully live, make sure your messages sound like “you”.


- Go to your message templates:Booking confirmation (PIN code)
- Booking confirmation
- Session reminder
- Trial flow messages (if you use trials)

Zooza allows HTML, emojis, coloured buttons, branded footers.

If you want help to brand your templates, contact our support.

6. Go live: Share links or embed on your website

## Once you’re happy with the flow, it’s time to let real parents in.

### 6.1 Share booking links

For each programme or timetable, you can:

- copy a direct booking link and share it:in WhatsApp classes,
- by email,
- on social media,
- on posters / QR codes.

### 6.2 Embed Zooza on your website


Zooza > Teams&Settings > Publish


Use Zooza’s Immersive Booking Engine™ to:

- embed booking forms directly on your own website,
- keep parents on your site from first click to payment.

Common options:

- WordPress plugin for Zooza, or
- JavaScript embed using your website builder.

If you need support, send your web developer our integration guides.

8. What Zooza does on autopilot

## Once your setup is in place, Zooza runs a lot of work automatically for you.

### 8.1 Payments & billing automation

Purpose: Collect payments and keep billing up to date without manual chasing.

- After a new booking:Zooza creates Payment Requests based on your payment template.
- The parent:pays by card / direct debit, or
- receives instructions for bank transfer (and optional QR code).

You can define:

- when debt appears (e.g. 15 days before due date),
- when reminders are sent,
- when to retry charges.

After payment:

- an invoice is generated automatically via:your connected invoicing software (e.g. Xero), or
- Zooza Invoicer.

All billing sessions sync with reports and client cards.

### 8.2 Booking & communication automation

Purpose: Keep parents informed without manual emails.

For each programme, you can have:

- Booking confirmation email
- PIN code message (if used)
- Session reminders (e.g. a day before each class)
- Unpaid reminders and optional auto-cancellation for unpaid bookings

All templates can be customised per programme.

### 8.3 Late booking & pro-rata management

Purpose: Handle new clients who join mid-term or mid-billing cycle fairly.

You can define:

- how late bookings are approved:auto-approve,
- hide full classes,
- manual approval (pending until admin confirms).

how pro-rata is calculated:

- based on remaining sessions,
- based on remaining days,
- full term fee,
- or no charge.

You can also:

- add the next billing cycle to the partial payment (optional),
- notify admins about each late booking,
- customise confirmation messages for late sign-ups.

### Learn more

### 8.4 Waitlist automation

Purpose: Keep interested parents in your funnel even when classes are full.

- When capacity is reached, Zooza switches to waitlist mode automatically.
- Parents can join the waitlist and receive a confirmation message.
- When a space opens you can send invitations manually

You can enable/disable waitlists per timetable.

### 8.5 Retention & re-enrolment

Purpose: Keep children enrolled from one term to the next with minimal effort.

At a set number of days before the end of a term:

- Zooza sends invite emails with a direct booking link to the next term / timetable.
- Parents click a pre-filled form, confirm, and continue.
- You define:which future timetables are offered,
- the message content,
- the timing.

You can turn retention automation ON/OFF per programme.


[Learn more](auto-enrollment.md)

### 8.6 Trial automation

Purpose: Convert trials into full enrolments without manual follow-up.

Booking the trial

1. Parent visits the booking form and sees available trial timetables.
2. Parent selects the trial date(s) and submits the booking.
3. Zooza sends a trial confirmation email with all details.

(You can also manage trials manually if you prefer to assign sessions yourself.)

Attending the trial

- Before the session, a reminder is sent (if enabled).
- Instructor marks attendance and can:add a short note,
- choose which timetable the child should continue in (or keep the same).

If no timetable is selected, Zooza uses the one attended during trial.

Programme enrolment

After the last trial session is marked as attended:

- Zooza can send a unique booking link for full enrolment.
- When the parent completes the form:the trial status becomes “Trial Won”,
- a new full enrolment is created, linked to the trial.

If there is no reaction:

- You can enable:first follow-up email,
- second follow-up email,
- and finally mark the trial as “Trial Lost”.

Each message template and delay can be configured per programme.


[Learn more](trial-lessons.md)

7. Everyday life: common booking scenarios

## Once you are live, you’ll handle typical situations every week.

Here are the main ones and what to do in Zooza.

All actions start from Bookings → Detail of a specific booking.

### 7.1 How do I delete a booking?

Use when: The client will not start at all, or it is a duplicate.

Steps:

- Go to Bookings → Detail → Change status to “Deleted”.

What happens:

- The spot is freed.
- You still keep the data in CRM (you can filter by “Deleted bookings”).

### 7.2 How do I pause a booking?

Use when: A client takes a break for a defined period (holiday, illness, etc.).

Steps:

- Go to Bookings → Detail → Payments → Payment Plan.
- Update the next scheduled payment date.

What happens:

- No new payments are generated during the pause.
- Billing restarts automatically after the pause date.

### 7.3 How do I cancel a booking?

Use when: The client is leaving and won’t return to that timetable.

Steps:

- Go to Bookings → Detail → Change status to “Cancelled”.

What happens:

- The spot is freed for another client.
- History and payments stay in the system.
- You can reactivate the booking later if needed.

### 7.4 How does the waitlist work?

Use when: A timetable is full, but new parents are still interested.

How it works:

- When a class reaches capacity, Zooza shows “Class full – Join Waitlist”.
- New bookings go into Waitlist status.
- When a place opens:you can invite from the waitlist manually, or
- enable automatic invites (in settings).

Steps:

- Check Bookings → Detail → Status = Waitlist.

What happens:

- No leads are lost; you retain interest even when full.

### 7.5 What is a trial booking?

Use when: You allow parents to attend a trial before committing.

- Trial bookings have status “Trial”.
- After the trial, you can convert to a full enrolment.

Steps:

- Check Bookings → Detail → Status = Trial.

[Learn more](../guides/trials-daily-business.md)

### 7.6 How do refunds work?

Use when: You need to return money (full or partial).

Steps:

- Go to Bookings → Detail → Payments.
- Select the transaction.
- Choose Process refund.

What happens:

- For Stripe: money is sent back to the client’s card.
- For other methods (e.g. GoCardless, bank transfer): you may need to process refund manually in your bank and record it in Zooza.

### 7.7 How do I handle missed classes?

Use when: Child misses one or more sessions and you want to adjust payments or offer replacement.

Options:

1. Adjust future paymentsGo to Booking → Payments → Installment details.
2. Adjust the next payment amount manually.
3. Offer make-up sessionsEnable Make-Up Sessions rules at programme level.
4. Parents can book replacement sessions via Parent Portal (if allowed by capacity and rules).

8. What Zooza does on autopilot

## Once your setup is in place, Zooza runs a lot of work automatically for you.

### 8.1 Payments & billing automation

Purpose: Collect payments and keep billing up to date without manual chasing.

- After a new booking:
Zooza creates Payment Requests based on your payment template.
- The parent:
pays by card / direct debit, or
- receives instructions for bank transfer (and optional QR code).

You can define:

- when debt appears (e.g. 15 days before due date),
- when reminders are sent,
- when to retry charges.

After payment:

- an invoice is generated automatically via:
your connected invoicing software (e.g. Xero), or
- Zooza Invoicer.

All billing sessions sync with reports and client cards.

[Learn More](https://support.zooza.online/portal/en/kb/articles/billing-settings)

### 8.2 Booking & communication automation

Purpose: Keep parents informed without manual emails.

For each programme, you can have:

- Booking confirmation email
- PIN code message (if used)
- Session reminders (e.g. a day before each class)
- Unpaid reminders and optional auto-cancellation for unpaid bookings

All templates can be customised per programme.

### 8.3 Late booking & pro-rata management

Purpose: Handle new clients who join mid-term or mid-billing cycle fairly.

You can define:

- how late bookings are approved:
auto-approve,
- hide full classes,
- manual approval (pending until admin confirms).

how pro-rata is calculated:

- based on remaining sessions,
- based on remaining days,
- full term fee,
- or no charge.

You can also:

- add the next billing cycle to the partial payment (optional),
- notify admins about each late booking,
- customise confirmation messages for late sign-ups.

[Learn More](../guides/late-registrations.md)

### 8.4 Waitlist automation

Purpose: Keep interested parents in your funnel even when classes are full.

- When capacity is reached, Zooza switches to waitlist mode automatically.
- Parents can join the waitlist and receive a confirmation message.
- When a space opens:
you can send invitations manually, or
- enable auto-invite rules.

You can enable/disable waitlists per timetable.

### 8.5 Retention & re-enrolment

Purpose: Keep children enrolled from one term to the next with minimal effort.

At a set number of days before the end of a term:

- Zooza sends invite emails with a direct booking link to the next term / timetable.
- Parents click a pre-filled form, confirm, and continue.
- You define:
which future timetables are offered,
- the message content,
- the timing.

You can turn retention automation ON/OFF per programme.

### Learn More

### 8.6 Trial automation

Purpose: Convert trials into full enrolments without manual follow-up.

Booking the trial

1. Parent visits the booking form and sees available trial timetables.
2. Parent selects the trial date(s) and submits the booking.
3. Zooza sends a trial confirmation email with all details.

(You can also manage trials manually if you prefer to assign sessions yourself.)

Attending the trial

- Before the session, a reminder is sent (if enabled).
- Instructor marks attendance and can:
add a short note,
- choose which timetable the child should continue in (or keep the same).

If no timetable is selected, Zooza uses the one attended during trial.

Programme enrolment

After the last trial session is marked as attended:

- Zooza can send a unique booking link for full enrolment.
- When the parent completes the form:
the trial status becomes “Trial Won”,
- a new full enrolment is created, linked to the trial.

If there is no reaction:

- You can enable:
first follow-up email,
- second follow-up email,
- and finally mark the trial as “Trial Lost”.

Each message template and delay can be configured per programme.

[Learn More](trial-lessons.md)

9. Next steps & where to get help

## Once you complete this guide, you should:

- have at least one Programme → Timetable → Sessions configured,
- be able to take payments using your chosen model,
- understand how to handle day-to-day scenarios,
- know which automations are already working for you.

From here, we recommend:

- Reviewing all key message templates and adding your branding.
- Setting up retention / re-enrolment for your main programmes.
- Exploring WhatsApp integration if you want to complement email with messaging.
- Looking at reports to track attendance, payments and class capacity.

If you get stuck at any point:

- reach out from inside the app, or
- email our support team — we’ll happily review your setup and suggest the best way to structure your programmes, timetables, payments and automations.

10. Glossary of Key Terms

## Programme (Programme / Product)

A product created once, e.g. “WeeOnes – 15 months to 2 years”.

Timetable (Class / Class) A specific instance of a programme, e.g. “Monday 10:00” class with set capacity.

Session A single occurrence or date within a timetable.

Client (Parent) A unique email address representing a parent who can manage multiple children’s bookings.

Booking / Booking The process of enrolling in a programme; connected to a specific client and timetable.

Term Fee Total amount a client commits to pay for a programme over a term or school year.

Debt The amount owed by the client, automatically generated based on your payment plan.

Payment Requests Requests created by Zooza for upcoming payments (card, direct debit, or bank transfer).

Client Profile / Parent Portal / Parent Portal The parent’s space with live updates about classes, payments, and attendance.

Make-Up Session
 A replacement session parents can book themselves under your rules.
