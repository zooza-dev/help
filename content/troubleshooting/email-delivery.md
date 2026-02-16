---
title: "Email Delivery Troubleshooting"
slug: "email-delivery-troubleshooting"
type: "troubleshooting"
product_area: "Communication"
sub_area: "Email"
audience: ["admin"]
tags: ["email", "delivery", "spam", "bounce"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-13"
intercom_id: 13738721
intercom_sync: false
---

# Email Delivery Troubleshooting

A client says they did not receive an email from Zooza. This guide walks you through how to verify delivery, identify common causes, and resolve the issue.

## Step 1: Check if the email was sent

1. Open the client's registration or booking.
2. Go to the **Communication** tab.
3. Look for the email in the sent email log.

If the email appears in the log, it was sent from Zooza successfully. The problem is on the recipient's side.

If the email does not appear in the log, the system did not send it. Common reasons:

- The registration was created manually or copied. Copied and manual registrations do **not** trigger automatic confirmation emails. You must send the email manually from the **Communication** tab.
- The notification template is not assigned to the programme. Check **Programme Settings** > **Online Registration** > **Notifications**.

## Step 2: Verify the recipient email address

1. Open the client's profile.
2. Confirm the email address is correct and has no typos.
3. If there is a warning icon or error indicator next to the email address, the system has previously failed to deliver to that address.

If the address is wrong, update it and resend the email.

## Step 3: Identify the delivery failure

When Zooza sends an email but it does not arrive, the cause is almost always on the recipient's side. These are the most common failures.

### Recipient mailbox is full

**Symptom:** The system shows a bounce message such as "The recipient's inbox is out of storage space."

**Solution:**
1. Contact the client and ask them to free up space in their mailbox or switch to a different email address.
2. Once the mailbox issue is resolved, resend the email from the **Communication** tab.

### Spam or junk filter on recipient side

**Symptom:** The email was sent (visible in sent logs) but the client cannot find it in their inbox.

**Solution:**
1. Ask the client to check their **Spam**, **Junk**, **Promotions**, or **Updates** folder.
2. If found there, ask the client to mark the email as "Not spam" and move it to their primary inbox.
3. Ask the client to add the Zooza sending address (`@zooza.app`) to their contacts or whitelist.

For Gmail users specifically, emails from new senders may land in the Promotions or Updates tab. The more the client interacts with Zooza emails (opens, replies, moves to Primary), the more likely future emails will arrive in the Primary inbox.

### Email provider blocking

**Symptom:** Emails consistently fail for clients using a specific provider (e.g., seznam.cz, corporate Outlook/Exchange servers).

Some email providers apply aggressive filtering. For example, seznam.cz has been observed marking Zooza emails as spam even when the client did not flag them manually.

**Solution:**
1. Ask the client to check their spam folder and whitelist the sender address.
2. If the provider continues to block emails, ask the client to use an alternative email address (e.g., Gmail).

<!-- REVIEW: Corporate Outlook/Exchange environments may have server-level filtering that individual users cannot override. In those cases, the client's IT department would need to whitelist the sending domain. -->

### Email marked as unwanted by recipient

**Symptom:** Zooza's email delivery provider reports that the recipient previously marked emails from Zooza as spam or unwanted.

When a recipient marks an email as spam, the email provider remembers this and may silently reject future emails.

**Solution:**
1. Contact the client and ask them to remove the spam flag on Zooza emails.
2. Ask them to whitelist the Zooza sending address.
3. Zooza support can remove the client from the provider's suppression list on our side. Contact support if the problem persists after the client has whitelisted the address.

## Step 4: What you can do as an admin

| Action | How |
|---|---|
| Resend an email | Go to the registration's **Communication** tab and resend the email manually. |
| Ask client to whitelist sender | Tell the client to add `@zooza.app` to their contacts or safe senders list. |
| Ask client to check spam folder | Direct them to look in Spam, Junk, Promotions, or Updates folders. |
| Change client email address | If the address is invalid or permanently bouncing, update it on the client's profile and resend. |

## What Zooza cannot do

- **Override recipient-side filtering.** If the client's email provider blocks or filters the email, Zooza cannot force delivery.
- **Deliver to full mailboxes.** The client must free up space or change their email address.
- **Control where emails land.** Whether an email appears in Primary, Promotions, or Spam is determined by the recipient's email provider, not by Zooza.

## Suspicious or phishing emails

If a client reports receiving a suspicious email that appears to come from Zooza:

1. Go to the registration's **Communication** tab and check the sent email logs.
2. If the email does **not** appear in the logs, it was **not** sent by Zooza. This is likely a phishing attempt.
3. Advise the client not to click any links in the suspicious email and to delete it.
4. If the email **does** appear in the logs, it is legitimate. The client can safely interact with it.

## When to contact Zooza support

Contact support if:

- The sent email log confirms the email was sent, the client's mailbox is not full, and the client still cannot find it after checking spam folders.
- You see a persistent delivery failure for multiple clients on the same email provider.
- A client reports a phishing email and you need help verifying its origin.
- You need a client removed from the email provider's suppression list after they previously marked Zooza emails as spam.

## See also

- [Email and Communication FAQ](../faq/email-communication-faq.md)
- [Receiving Emails from Zooza in Primary Inbox](emails-in-primary-inbox.md)
- [Sending Emails and SMS to Clients](../guides/sending-email-sms.md)
