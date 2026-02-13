---
title: "Send Email"
slug: "communication-send-email"
type: "reference"
product_area: "Communication"
sub_area: "Email"
audience: ["admin"]
tags: ["reference", "ui-reference", "communication", "email"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-13"
---

# Send Email

The Send Email screen lets you compose and send email messages to clients. Use it to send bulk announcements, class-specific messages, or individual emails.

> **Navigation:** Go to **Communication** → **Send email**.

![Send email](../../assets/images/reference/communication-send-email.png)

## Step 1: Target Class

### Send Message

Choose who receives the email:

| Option | Description |
|---|---|
| **To all clients with an active booking** | Sends to all clients in the selected billing class with status "Enrolled". |
| **To all clients** | Sends to all clients regardless of bookings or billing periods. |
| **To a specific class** | Sends to all clients in the selected class with status "Enrolled". |
| **To a single recipient** | Sends to a single email address only. |
| **To selected bookings** | Sends to a manually selected set of bookings. |

### Choose Who You Want to Send the Message To

| Option | Description |
|---|---|
| **Clients** | Message is sent to each client just once. If the client has multiple bookings, merge fields specific to a booking (such as `COURSE_PRICE` or `VARIABLE_SYMBOL`) cannot be used. Best for general announcements. |
| **Individual bookings** | Message is sent to each booking that meets the criteria. If a client has multiple bookings, they will receive one email per booking. Best for messages about specific bookings. |

### Settings

| Field | Description |
|---|---|
| `Promotional message` | Check **Yes** if you do not want to send this message to clients who have unsubscribed from promotional messages. |
| `Send email also to users with additional access to booking` | Check **Yes** to also send to users with shared access to the booking. |
| `Billing period` | Dropdown to select the billing period (e.g. "Ongoing Classes"). |

### Recipients

Shows the count and list of recipients matching your criteria.

| Column | Description |
|---|---|
| `Name` | Client (parent) name. |
| `Child` | Child name associated with the booking. |
| **Remove** | Remove the recipient from this send. |

Use **Show recipients** / **Hide recipients** to toggle the recipient list.

Click **Continue** to proceed to the Message step.

## Step 2: Message

Compose the email content. This step uses the rich text editor (same as the template editor — see [Template Editor](communication-message-templates.md#template-editor)).

## Step 3: Summary

Review recipients, message content, and settings before sending.

## Step 4: Finish

Confirm and send the email. Zooza processes the send and shows a confirmation.

## Related

- [Communication Dashboard](communication-dashboard.md) — main communication hub.
- [Message Templates Reference](communication-message-templates.md) — manage reusable templates.
- [Sending Email/SMS Guide](../guides/sending-email-sms.md) — step-by-step instructions.
- [Dynamic Tags Guide](../guides/dynamic-tags.md) — available merge fields for templates.
- [Email Communication FAQ](../faq/email-communication-faq.md) — common email questions.
