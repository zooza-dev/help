---
title: "Bulk email send tracking"
slug: "bulk-email-send-tracking"
type: "guides"
product_area: "Communication"
sub_area: "Email"
audience: ["admin"]
tags: ["email", "bulk", "queue", "progress", "tracking", "cancel"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: true
last_converted: "2026-04-10"
---

# Bulk email send tracking

When you send an email to a large group of clients, Zooza processes it as a **message job** in the background. You can track progress, see delivery results, and cancel a send that is still in progress.

## How bulk sending works

1. You compose and configure the send as usual (see [Sending Email/SMS](sending-email-sms.md)).
2. When you confirm, Zooza counts the exact recipient list and creates a job.
3. Sends to **100 or more recipients** require your approval before any emails are dispatched.
4. Once approved, sending runs in the background in chunks.
5. Progress updates automatically — no need to stay on the page.

> Sends under 100 recipients are approved automatically and start immediately.

## Approval gate

For large sends, Zooza shows you the exact recipient count before sending starts.

![Screenshot — approval gate](../../assets/images/bulk-email-approval-gate.png)

| Element | Description |
|---|---|
| Recipient count | Exact number of recipients in this send — locked at job creation, not re-queried. |
| **Approve** | Start sending. Zooza begins processing in the background. |
| **Cancel** | Abandon the send. No emails are dispatched. |

> The recipient count shown at approval is the count that will actually be sent — it cannot change after the job is created.

## Job statuses

| Status | What it means |
|---|---|
| **Pending approval** | Job created. Waiting for you to click Approve. No emails sent yet. |
| **Queued** | Approved, but another send for your account is already active. This send will start automatically when the active one finishes. |
| **Sending** | Actively processing and dispatching emails. |
| **Completed** | All recipients processed. Check Sent and Failed counts for the result. |
| **Cancelled** | Send was cancelled. Emails already dispatched before cancellation were delivered. |
| **Failed** | A job-level error stopped the send. Contact support if this happens. |

## Progress view

While a send is running, the progress view shows:

![Screenshot — bulk send progress view](../../assets/images/bulk-email-progress-view.png)

| Field | Description |
|---|---|
| **Sent** | Recipients successfully handed off to the mail gateway. |
| **Failed** | Recipients that could not be processed (e.g. missing email address). |
| **Skipped** | Recipients excluded during processing (e.g. duplicate email within the same send). |

## Queue — one active send at a time

Only one bulk send can be active per account at a time.

If you start a second send while the first is still running, the second send enters the queue. It starts automatically as soon as the first one completes — no action needed from you.

The progress view shows the queue position if your send is waiting:

> *"Your send is queued. Sending will start automatically when the current send finishes."*

## Cancelling a send

You can cancel a send that is **Pending approval**, **Queued**, or **Sending**.

1. Open the progress view for the active send.
2. Click **Cancel**.

Emails already dispatched before you cancelled were delivered and cannot be recalled. Unsent chunks are stopped immediately.

## Send history

You can review past sends and their results from the Communication section.

![Screenshot — send history list](../../assets/images/bulk-email-send-history.png)

Each entry shows the job status, recipient count, sent count, failed count, and the date the send was created.

## Related

- [Send Email Reference](../reference/communication-send-email.md) — full UI reference for the send flow.
- [Sending Email/SMS Guide](sending-email-sms.md) — step-by-step instructions.
- [Email Communication FAQ](../faq/email-communication-faq.md) — common questions.
