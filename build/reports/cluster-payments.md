# Payment-Related Support Conversations -- Cluster Analysis

**Source:** `build/reports/ingest-condensed.jsonl`
**Filter criteria:** Tags containing `payments`, `payment_schedules`, `payment_correction`, `payment_reminders`, `gocardless`, `billing_profile`, `invoices`, `price`, `prorata`, `rounding`; plus untagged conversations with clear payment subject matter.
**Date range:** 2025-10-02 to 2026-02-11
**Total matching conversations:** 46

---

## Frequency Table by Sub-Category

| Sub-Category | Count | Share |
|---|---|---|
| GoCardless / bank connection issues | 9 | 20% |
| Payment schedule setup & configuration | 8 | 17% |
| Payment pairing / matching failures | 7 | 15% |
| Payment correction / refund / manual adjustment | 5 | 11% |
| Billing profile / account setup | 4 | 9% |
| Payment reminders & notifications | 4 | 9% |
| Invoice generation & editing | 3 | 7% |
| Price display / pro-rata / rounding | 3 | 7% |
| Course price & late registration pricing | 2 | 4% |
| QR code on payment emails | 1 | 2% |

---

## Specific Questions Customers Asked

### GoCardless / Bank Connection Issues
1. How do I renew the GoCardless bank connection when it expires? (multiple banks, recurring 90-day expiry)
2. Payments are not pairing because GoCardless connection to SLSP (Slovenska sporitelna) failed -- what do I do?
3. How do I switch from GoCardless pairing to email-based notification pairing for faster processing?
4. GoCardless syncs only once daily; is there a faster alternative? (Answer: email notification pairing is near-realtime)
5. SLSP bank stopped working with GoCardless entirely -- what is the workaround? (Bulk notification sent to affected customers)
6. My bank account did not pair correctly with GoCardless; how do I fix it?

### Payment Schedule Setup & Configuration
1. How do I set up a payment schedule (splatkovy kalendar) on a specific registration?
2. Payment templates are not visible to clients in the registration form -- why? (Answer: templates must be marked "visible to clients")
3. After copying registrations to a new semester, no payment schedule was applied -- how to fix? (Answer: manually apply schedule post-copy)
4. Why does the system calculate installments from the registration date rather than the group start date?
5. Why was a membership installment generated for a month with only one session?
6. The payment anniversary date was accidentally set to the 10th instead of the 1st -- how does this affect installments?
7. How do I activate payment schedules in bulk for copied registrations?
8. How do I set up a payment schedule for individual lessons with variable pricing?

### Payment Pairing / Matching Failures
1. Payments from Revolut are not auto-matched because the variable symbol is in the "Reference" field, not the standard field. (Fix: algorithm now checks the note/reference field)
2. Why are payments from Tatra Banka not appearing in Zooza? (Answer: check b-mail notification settings in internet banking)
3. System shows "payment pairing not configured" even though it is configured. (Bug -- fixed)
4. Payment was received while registration was in "Late registration" status and was not matched. Why?
5. Semi-annual payments arrive before the debt is created, so auto-pairing fails. Can debt creation timing be adjusted?
6. How do I manually pair a payment that the system could not match?
7. Payments appear paired in bank but not reflected in Zooza after a system outage.

### Payment Correction / Refund / Manual Adjustment
1. How do I zero out (correct) a manually entered payment? (Answer: use "Edit payment" not "Refund")
2. Is it better to do a refund or a debt correction when moving a payment between registrations? (Answer: debt correction is preferred)
3. How do I correct a payment when the system double-counted a block during registration copy? (Bug fix applied; manual correction needed)
4. A payment was auto-assigned to a registration that nobody assigned -- how did this happen?
5. How do I fix a wrongly returned amount on a course?

### Billing Profile / Account Setup
1. How do I change the default billing profile (IBAN) for a course? I cannot edit the existing one. (Answer: set the preferred profile as default in settings)
2. Some registrations are still using the wrong billing profile despite the course-level setting being correct. Why?
3. How do I set up billing profile pairing with GoCardless for the first time?
4. Where do I update my company address in the billing profile?

### Payment Reminders & Notifications
1. Can I change the time payment reminders are sent? They currently arrive at midnight. (Answer: not configurable; sent in nightly batch)
2. How do I configure the "zero-th" notification (before debt creation)?
3. Clients received payment reminders even though they already paid -- why? (Answer: the notification was about an upcoming installment, not overdue debt)
4. A customer wants to disable the "you will receive a payment request" pre-notification because it confuses clients.

### Invoice Generation & Editing
1. How do I change the customer name on an already-generated invoice? (Answer: edit the invoice via the registration detail)
2. Can I delete an invoice from the system? (Answer: no, but you can edit it; use a credit note in your accounting)
3. I need a refund of a payment made after contract termination -- how to process it?

### Price Display / Pro-rata / Rounding
1. Rounding on the payment template rounds down (e.g., 742.50 to 742). How do I avoid this when entering a custom price? (Answer: rounding applies only when using the template formula)
2. How does the system calculate the pro-rata price for late registrations?
3. The pro-rata settings on courses were changed unexpectedly -- what happened? (Answer: no system-side change; user-side configuration issue)

### Course Price & Late Registration Pricing
1. How do I set a fixed price for a course (no pro-rata reduction for late joiners)?
2. Where do I change the price displayed to clients during registration?

### QR Code on Payment Emails
1. The QR code in the payment email does not work when scanned -- it does not fill in the correct recipient name. (Answer: check billing profile name setting)

---

## Common Patterns and Recurring Issues

### 1. GoCardless Connection Lifecycle Is Poorly Understood
The 90-day expiry of GoCardless bank connections generates repeated support tickets. Customers do not know when their connection will expire, how to renew it, or where to check its status. The SLSP (Slovenska sporitelna) outage in late 2025 was a systemic issue that required proactive outreach and workaround documentation (switching to email-based pairing).

### 2. Payment Pairing Relies on Fragile Assumptions
Auto-pairing fails when: (a) the variable symbol is placed in a non-standard field (Revolut, foreign banks), (b) the payment arrives before the debt is created (common with semi-annual billing), (c) bank notification services have outages (Tatra Banka, SLSP). Customers often do not understand the difference between GoCardless-based and email-notification-based pairing.

### 3. Payment Schedules After Bulk Copy Are a Major Pain Point
When registrations are copied from one semester to another, payment schedules are not automatically applied. Admins must manually re-apply templates to each registration, which is error-prone and time-consuming. Several tickets stem from confusion about what happens to payment settings during copy/transfer operations.

### 4. Rounding and Pro-Rata Logic Causes Confusion
Customers expect to enter exact amounts and are surprised when the template's rounding rules override their input. The pro-rata calculation for late registrations is not transparent to admins -- they do not always know what price the system will show or charge.

### 5. Payment Reminders Cause Customer Friction
The nightly batch sending time (midnight) is seen as unprofessional. The "upcoming payment" notification is frequently confused with an "overdue payment" reminder by both admins and their end clients, leading to unnecessary complaints and manual work.

### 6. Invoice Editing Limitations
Admins frequently need to change the payer name on invoices (e.g., one parent registers, the other parent needs the invoice for a tax deduction). The current workflow requires a client data change request before regenerating the invoice, which is too slow.

### 7. Correction vs. Refund Distinction Is Unclear
Multiple tickets show admins using "Refund" when they should use "Edit payment" (correction). This creates incorrect data in financial reports. The UI does not sufficiently guide admins toward the correct action.

---

## KB Coverage Assessment

The following topics appear **well-covered** in existing KB content:
- Payment templates creation (`content/guides/payment-templates-creation.md`)
- Payment pairing (`content/guides/payment-pairing.md`)
- GoCardless setup (`content/guides/gocardless-direct-debit-mandates.md`)
- Payment reminders (`content/guides/automatic-payment-reminders.md`)

The following topics have **gaps or need enhancement**:
- GoCardless connection renewal/expiry lifecycle (no dedicated guide)
- Email-notification-based pairing as GoCardless alternative (only partially covered)
- Payment schedule behavior during registration copy/transfer (not documented)
- Rounding rules and pro-rata calculation details (not clearly documented)
- Correction vs. refund decision guide (no guide exists)
- Invoice editing limitations and workarounds (minimal coverage)
- Payment reminder timing and notification types explained (FAQ only, not detailed)
