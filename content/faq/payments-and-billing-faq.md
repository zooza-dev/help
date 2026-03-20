---
title: "Payments and Billing FAQ"
slug: "payments-and-billing-faq"
type: "faq"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: ["payments"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-13"
---

# Payments and Billing FAQ

## Where do I find invoices?

There are two different types of invoices in the Zooza context:

**Client invoices** — invoices generated for your clients (for their bookings):
Go to **Sales & Payments** → **Invoices**. You can filter by date, search by client, and download individual invoices or the full batch as a ZIP.

**Zooza subscription invoices** — invoices for your own Zooza subscription (what you pay Zooza):
Go to **Settings** → **Subscription** → **Manage subscription** → **Details** → **Invoices**. This opens the billing portal where past invoices can be downloaded.

## How do I resend an invoice to a client?

When you generate an invoice, it is automatically emailed to the client. If you need to resend it (for example, after making a correction):

1. Open the booking.
2. Click the pencil icon next to the invoice.
3. Check **Send invoice to client via email**.
4. Save.

The updated invoice is sent to the client's email address on record.

## How do I download all invoices at once?

Go to **Sales & Payments** → **Invoices**. Apply any filters you need (date range, etc.), then click **Download all**. This downloads all filtered invoices as a single ZIP file.

For bulk XML export or API-based access, use the Zooza API (`GET /v1/customer_invoices` and `GET /v1/customer_invoices/download`). Contact support or see the developer documentation for details.

## What does a negative balance mean on a booking?

The balance shows the difference between what the client should pay and what they actually paid.

- **0** = fully paid.
- **Negative amount** = payment was not completed or failed. The client needs to finish payment via their Client Profile.

A negative balance does not necessarily mean "overpaid" — it means there is an outstanding amount.

## What happens when a client registers but does not pay?

The booking is created even if the payment fails or is skipped. This ensures you still capture the lead. The parent can complete the payment later via their Client Profile.

You can configure **payment reminders** per programme to automatically follow up with unpaid clients. After a set number of reminders, the system can auto-remove the booking.

## How do payment reminders work?

Payment reminders are configured per programme under the payment settings. You set:

- How many reminders to send.
- The interval between reminders.
- Whether the system should automatically cancel the booking after all reminders expire.

Go to **Programme → Settings → Price** to configure this.

## How do I issue a refund?

Refunds are handled directly in Zooza:

1. Go to **Bookings → Detail → Payments**.
2. Select the transaction.
3. Click **Refund** (full or partial).

The refund is processed through Stripe automatically. You do not need to log into Stripe separately.

## How does monthly billing (aliquot) work?

When a parent joins mid-month, the system can calculate a prorated first payment based on the remaining sessions in that month. This is called **aliquot** billing.

- **Aliquot ON:** First payment is adjusted for the number of sessions remaining. Subsequent months are the full fixed amount.
- **Aliquot OFF:** Every payment is always the same fixed monthly amount, regardless of when the client joins.

Choose the option that fits your business model. Most clients prefer aliquot OFF for simplicity during launch, and turn it ON later.

## Can I retrospectively generate invoices?

Yes. You can disable automatic invoice generation during launch, accept bookings and payments, and then generate invoices later once your accounting settings (e.g., VAT rates in Xero) are fully configured.

## How do I handle a client who forgot to use a discount code?

Instead of refunding, the easiest approach is to reduce the next instalment by the discount amount and send the client a quick note explaining the adjustment. This is simpler than editing past payments.

## How do I mark a booking as paid when payment was received outside the system?

If a client paid by direct bank transfer or you credited them manually, you can adjust the payment status in their booking detail. Go to **Bookings → Detail → Payments** and record the manual payment to clear the outstanding balance.

## When should I use "Edit payment" vs "Refund"?

Use **Edit payment** for corrections — for example, when the amount is wrong or a payment was assigned to the wrong booking. Use **Refund** only when you are actually returning money to the client.

Using **Refund** incorrectly (e.g., to zero out a manual entry) creates phantom transactions that appear in your financial reports and distort totals. If you need to correct or move a payment between bookings, a debt correction is the preferred approach.

<!-- REVIEW: Support tickets confirm "Edit payment" is accessed via the transaction list → More → Edit payment. Verify current UI label matches. -->

## What happens to payment schedules when I copy bookings to a new term?

Payment schedules are **not** automatically carried over when you copy bookings to a new term. Because the client did not go through the booking form and select a payment template, the system does not assign one.

After copying bookings, you must manually apply the correct payment template to each booking. Without this step, the system calculates the price as the base rate multiplied by the number of sessions, which may differ from the expected instalment amount.

<!-- REVIEW: Bulk activation of payment templates after copy is requested frequently — check if a bulk-apply feature has been added. -->

## How does pro-rata (aliquot) pricing work for late bookings?

When a client registers after the term has started and aliquot pricing is enabled, the system calculates the price as:

**remaining sessions ÷ total sessions × full price**

This adjusted price is then split according to the active payment template (e.g., monthly instalments). Zooza supports four calculation methods — session-based, day-based, no value, and full price — each suited to different business models.

For full configuration details and common scenarios, see [Late bookings (pro-rata management)](../guides/late-bookings.md).

## Why does the payments dashboard only show 10 unpaid bookings?

The **Unpaid Bookings** widget on the Payments dashboard displays only the first 10 unpaid bookings as a quick overview. It is not intended to show every outstanding balance.

To see the full list of unpaid bookings:

1. Go to **Bookings**.
2. Use the status or payment filter to show only unpaid or partially paid bookings.
3. The filtered list shows all matching bookings with full pagination.

## How do I set up a Netflix-style recurring membership?

For ongoing memberships where clients pay monthly and stay enrolled indefinitely (e.g., football club, dance studio, gym), use the **Membership** price type with automatic late booking approval.

1. Set the programme price type to **Membership**.
2. Under **Late bookings**, select **Automatically confirmed**.
3. Set `Aliquot price calculation` to **Full programme price**.
4. Uncheck `Include Initial Full Scheduled Payment` so new joiners are not charged a full instalment immediately on top of their first scheduled payment.
5. Create a monthly payment template with `Day of the month when the payment is due` set to **0** (charges on the same day each month that the client joined).

For the full step-by-step guide, see [Membership Subscription Setup](../guides/membership-subscription-setup.md).

## Why does the QR code in my payment email not work?

The QR code in payment emails pulls recipient details from your **billing profile**. If the profile name does not match the bank account holder name, some banking apps will reject or fail to process the QR code when scanned.

To fix this:

1. Go to **Settings → Billing Profiles**.
2. Open the relevant billing profile.
3. Verify that the **account holder name** and **IBAN** match your actual bank account details exactly.
4. Save and resend the payment notification to the client.

For full details on billing profiles, see [Billing and invoicing](../setup/billing-and-invoicing.md).

## How do I set up billing profiles and invoicing?

Go to **Settings** → **Billing**. There you can enable automatic invoice generation, set up your default billing profile (company name, IBAN, address), and create additional profiles for multi-entity businesses. Each programme can be assigned a specific billing profile. For the full setup guide, see [Billing and invoicing](../setup/billing-and-invoicing.md).

## Can I generate an invoice manually for a single booking?

Yes. Open the booking detail, click **Show payments**, and in the **Invoices** section click **Generate invoice**. Select the billing profile to use and confirm. The invoice is generated immediately and emailed to the client. This works regardless of whether automatic invoice generation is enabled.

## What is the difference between automatic and manual invoice generation?

**Automatic** — Zooza generates an invoice every time a payment status changes to "paid" on a booking. A single booking can produce multiple invoices if the client pays in instalments. **Manual** — you generate invoices one at a time from the booking detail. You can use both: leave automatic generation off during setup, and generate invoices manually or enable it later.

## Does Zooza support credit notes or debit notes?

- **Credit note** (reduces the original invoice — e.g. correcting an overcharge, issuing a partial refund on an invoice)
- **Debit note** (increases the original invoice — e.g. charging an additional amount not included originally)

Zooza does not have a dedicated **credit note** or **debit note** button. What is available depends entirely on which invoicing system you use:

| Invoicing system | Fix a wrong invoice | Credit note | Debit note |
|---|---|---|---|
| **Zooza built-in** | Edit the invoice (date, period, description only) — does not change the payment | Not supported | Not supported — increase the debt on the booking instead |
| **Xero** | Edit or void in Xero directly; create a credit note in Xero | Supported in Xero | Supported in Xero |
| **Abra Flexi** | Edit or delete in Abra Flexi | Supported in Abra Flexi | Supported in Abra Flexi |
| **Smartbill** | Edit or delete in Smartbill | Supported in Smartbill | Supported in Smartbill |
| **Számlázz** | Cannot modify — issue a cancellation (storno) invoice and reissue a new one | Storno invoice in Számlázz | Not applicable — issue a new invoice |

> **Important:** Changes made to invoices in external systems (Xero, Abra Flexi, Smartbill, Számlázz) are **not synchronised back to Zooza**. Zooza always keeps the original invoice reference it generated.

### To fix a wrong invoice — general process

1. Identify which invoicing system you use (**Settings → Billing → Invoice Settings**).
2. If using **Zooza built-in**: click the pencil icon next to the invoice on the booking detail. You can correct the period, date, payment method, and description. This does not change the payment amount.
3. If using an **external system**: open the invoice in that system and apply the correction there (edit, void, credit note, or storno — depending on the system). The corrected version will not appear in Zooza.
4. If the payment amount itself needs to change, adjust the debt on the booking in Zooza separately — see [Edit payment on booking](../guides/edit-payment-on-booking.md).

### To increase the amount owed (debit note equivalent)

Zooza does not issue debit notes. To charge a client an additional amount:

1. Open the booking detail.
2. Adjust the outstanding debt manually — see [Edit payment on booking](../guides/edit-payment-on-booking.md).
3. If an invoice is required for the additional amount, generate a new invoice for that booking once the additional payment is recorded.

## What happens to a client's scheduled payment when I cancel a session?

It depends on the payment type:

- **Pay-as-you-go** — the system automatically removes the payment obligation for that session. The client's next scheduled payment is reduced by the session unit price. No action is needed from you.
- **Fixed monthly / instalment plan** — cancelling a session does not automatically reduce the client's payment. Use **Adjust session payments** from the Calendar bulk edit to manually credit the affected clients. See [Session payment adjustments](../guides/session-payment-adjustments.md).

In both cases, the client is **not notified automatically** when their payment amount changes due to an adjustment.

## Can I manually credit or debit a client's scheduled payment?

Yes. Open the booking, go to **Payment plan**, and click on the specific scheduled payment. In the **Adjustments** section, enter a positive amount (credit — reduces what they owe) or a negative amount (debit — increases what they owe), add a description, and click **Save**.

For the full walkthrough, see [Session payment adjustments](../guides/session-payment-adjustments.md).

## Can I credit multiple clients at once after cancelling a session?

Yes, using bulk edit in the Calendar:

1. Go to **Calendar** and select the cancelled sessions.
2. Click **Bulk edit** → check **Adjust session payments**.
3. Select **Credit sessions**, set the amount, and confirm.

Zooza applies the credit to the next scheduled payment for each affected client. See [Session payment adjustments](../guides/session-payment-adjustments.md).

## What if a client has no upcoming scheduled payment when I apply a bulk credit?

If a client's payment plan has already ended or all their scheduled payments have been processed, the adjustment cannot be applied and is skipped for that client. You will need to handle any compensation for those clients manually (e.g. by recording a manual payment or issuing a refund).

## Can I reverse a manual payment adjustment?

Yes. In the **Adjustments** list on the payment detail, click **Reverse** next to the adjustment. A new entry with the opposite amount is created. The original adjustment remains visible in the list for the audit trail.

You can only reverse manual adjustments. Automatic adjustments (generated by session bookings or cancellations in Pay-as-you-go) are managed by the system.

## Can I use multiple billing profiles for different programmes?

Yes. Go to **Settings** → **Billing** → **Other billing profiles** and click **Add**. Each profile has its own company details, IBAN, and invoice numbering. Assign a profile to a programme in **Programme** → **Settings** → **Price and Payment** → **Invoicing**. If no profile is assigned, the default billing profile is used.
