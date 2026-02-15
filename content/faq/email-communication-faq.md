---
title: "Email and Communication FAQ"
slug: "email-communication-faq"
type: "faq"
product_area: "Communication"
sub_area: "Email"
audience: ["admin"]
tags: ["email"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-13"
intercom_id: 13728490
intercom_sync: false
---

# Email and Communication FAQ

## What is the difference between "Trial Booking Completed" and "Confirmation of Booking" emails?

- **Trial Booking Completed** — sent immediately after a parent books a trial class. It confirms the trial booking.
- **Confirmation of Booking** — sent after a parent completes a full programme enrolment (not a trial).

These are separate templates that serve different stages of the client journey.

## What dynamic tags can I use in emails?

Common dynamic tags:

- `*|FIRST_NAME|*` — parent's first name.
- `*|EF_FULL_NAME|*` — child's full name.
- `*|BOOKING_URL|*` — pre-filled booking form link.
- `*|WIDGET_PROFILE_URL|*` — secure direct-login link to the parent's profile.

The full tag list is available via the **Tags** button in the email editor. Some tags only work in specific template types (e.g., session tags only in session notifications).

## Do dynamic tags work in email subject lines?

Yes, but with limitations. Some tags may not populate in certain template types. Test your email before sending to a large class.

## Why does my email lose formatting when sent?

When composing emails in Zooza, the editor preserves formatting (paragraphs, bold, etc.). If the sent email appears as a single block of text, you may be pasting plain text without the correct line breaks. Use the built-in editor's formatting tools rather than pasting from external sources.

## Where do replies to Zooza emails go?

Replies go directly into the Zooza application. The reply-to address is system-managed and routes to your Zooza inbox.

## Can I use a custom sending domain for emails?

Custom sending domains are available for specific plans. Contact your Zooza account manager to discuss options.

## How do I send an email to all clients at a specific location?

Go to **Bookings**, filter by the relevant class or location, and use the bulk communication option. You can also go to **Communication** for broader email sends, though the filtering options differ from the bookings view.

## How do I set up class reminder emails for parents?

Class reminders are part of the automated email flow. They are configured per programme under the communication/automation settings. Typically, a reminder is sent the day before the scheduled session.

## Can I get an email notification when a new booking or trial comes in?

Yes. Admin notifications are configured in the system settings. You receive an email whenever a new booking (including trials) is created.

## Why do dynamic tags show wrong data for replacement or block-based lessons?

Tags like `COURSE_TIME` and `COURSE_DATE_DAY` pull their values from the primary group's first session, not from the replacement session or the specific block the client registered for. This is a known limitation. For block-based courses, use the `ORDER_SUMMARY` tag instead, which includes the correct session details for the client's specific block.

<!-- REVIEW: A dedicated dynamic tag for block-specific dates has been requested but is not yet available. Monitor for product updates. -->

## Why did my client not receive the confirmation email for a manual or copied registration?

Copied and manually created registrations do **not** trigger automatic confirmation emails. This is by design. To send a confirmation, go to the registration's **Communication** tab and send the confirmation email manually.

## What is the difference between system templates and user templates?

- **System templates** (e.g., payment confirmation, login code) are built into Zooza and cannot be edited. They appear under the "System communications" section in the template selector.
- **User templates** are custom templates you create. They appear under the "User templates" section in the template selector.

These are listed in separate dropdown sections. If you cannot find your custom template, make sure you are looking under **User templates**, not under system or saved communication templates.

## How do I troubleshoot emails not arriving for a specific client?

1. Go to the registration's **Communication** tab and check the sent email logs to confirm whether the email was sent by Zooza.
2. Common causes for non-delivery:
   - The client's mailbox is full (e.g., "inbox out of storage space" bounce).
   - The client's email provider is filtering Zooza emails as spam.
   - The client previously marked a Zooza email as unwanted.
3. Ask the client to whitelist your sending address and check their spam/junk folder.

Zooza cannot override recipient-side filtering. If the logs confirm the email was sent, the issue is on the recipient's side.
