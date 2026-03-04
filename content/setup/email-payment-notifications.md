---
title: "Email-notification payment matching"
slug: "email-payment-notifications"
type: "setup"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: ["payments", "bank", "payment-matching", "email-notifications", "IBAN", "bank-transfer"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-03-03"
intercom_id:
intercom_sync: false
---

<!-- Synonyms: email payment matching, bank email notifications, payment notification email, automatic payment matching, pair bank account, bank pairing, párovanie platieb, párovanie bankového účtu, email notifikácie platieb, automatické párovanie platieb, banková notifikácia, fizetési értesítő email, automatikus fizetés párosítás, banki értesítő email -->

# Email-notification payment matching

Email-notification pairing is a faster, lower-maintenance alternative to GoCardless for automatic payment matching. Instead of a periodic API connection, your bank sends an email notification to a unique Zooza-generated address each time a payment arrives. Zooza reads the notification and automatically matches the payment to the correct booking using the payment reference.

**Advantages over GoCardless:**

- Near real-time matching (within minutes, vs. up to 24 hours with GoCardless)
- No 90-day renewal required — works indefinitely once configured
- Works with banks that do not support GoCardless

> **Note:** Email-notification pairing is not available for every bank. Availability depends on whether your bank's notification emails contain structured payment reference data. See [My bank is not in the list](#my-bank-is-not-in-the-list) if your bank does not appear in the selector.

## Prerequisites

- Your billing profile must have a valid IBAN configured.
- Your bank must support sending email notifications for incoming payments.

## Step 1 — Set your IBAN and select your bank

1. Go to **Settings → Billing**.
2. Open the billing profile you want to configure (default or additional).
3. Click **Edit**.
4. Fill in your **IBAN** (bank account number in international format).
5. In the **Bank** field, select your bank from the dropdown.
   - If your bank appears → continue to [Step 2](#step-2--find-your-zooza-notification-email).
   - If your bank is not listed → see [My bank is not in the list](#my-bank-is-not-in-the-list).
6. Click **Save**.

## Step 2 — Find your Zooza notification email

Once a supported bank is selected and the IBAN is saved, Zooza generates a unique email address for your billing profile. This address is displayed in the billing profile settings.

Copy this email address — you will paste it into your bank settings in the next step.

## Step 3 — Set the notification email in your bank

Log in to your internet banking and find the setting for **email notifications for incoming payments**. The exact location depends on your bank — it is usually under account settings, notifications, or alerts.

Set the recipient email address for payment notifications to the Zooza-generated address you copied in Step 2.

From this point, every incoming payment triggers an email to Zooza. Zooza reads the notification and automatically matches the payment to the correct booking using the payment reference.

> **Important:** Your bank will send payment notification emails to the Zooza address instead of your personal inbox. You will no longer receive individual payment notification emails yourself. Other bank emails (statements, login confirmations) are unaffected.

## My bank is not in the list

If your bank does not appear in the Zooza bank selector, contact support to have it evaluated for addition.

**To request support for your bank:**

1. Contact Zooza support and ask for the test notification email address for your bank.
2. In your internet banking, temporarily set the payment notification email to the address provided by support.
3. Wait for a real payment to arrive (or make a small test transfer to your account).
4. Note the **exact date and time** the payment arrived in your account and send it to support.
5. The team will analyze the notification and confirm whether your bank can be added to the supported list.
6. Once added, follow Steps 1–3 above to complete the setup with your generated Zooza email address.

> Not every bank can be supported — this depends on whether the bank's notification emails include structured payment reference data. Zooza support will confirm feasibility.

## Related

- [GoCardless Integration FAQ](../faq/gocardless-faq.md) — comparison of GoCardless vs email-notification pairing, troubleshooting.
- [Billing and invoicing](../setup/billing-and-invoicing.md) — how to configure billing profiles and IBAN.
