---
title: "Client Management FAQ"
slug: "client-management-faq"
type: "faq"
product_area: "Clients"
sub_area: ""
audience: ["admin"]
tags: ["clients", "data-correction", "merge", "email"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-13"
intercom_id: 13738258
intercom_sync: false
---

# Client Management FAQ

## How do I create a new client manually (not through booking)?

Zooza does not have a standalone "Add client" button. A client record is created automatically when a booking is made. To create a client manually:

1. Go to the booking form and create a new booking on behalf of the client (choose any class).
2. Fill in the client's name and email address during the booking process.
3. If you only need the client record and not the booking, delete the booking afterwards. The client profile remains in the system.

This is the only way to create a client without the parent registering themselves through the online form.

## How do I change the client (parent) on an existing booking?

Changing the client on a booking reassigns that single booking to a different parent. It does not change the client's personal data across all their bookings.

1. Open the booking detail.
2. Click **Change Client**.
3. In the `Client` field, enter the email or name of the new client and click **Search**.
4. Select the correct client from the results and confirm.

The new client must already exist in the system (they must have at least one booking of any status). Communication history tied to the booking is preserved because it is linked to the booking number, not the email address.

See also: [Data Correction or Change Client](../guides/data-correction-change-client.md).

## A client has duplicate accounts -- how do I merge them?

Duplicates occur when a parent registers with two different email addresses, or when an admin creates a second record by mistake.

1. Go to **Clients** and open one of the duplicate client profiles.
2. Navigate to **Family & Connections** and click **Manage**.
3. Select the duplicate profiles you want to merge.
4. Click **Merge profiles**.

Merging combines the booking history and family connections from both profiles into one. You cannot undo a merge, so verify the records carefully before proceeding.

<!-- REVIEW: Confirm whether payments and communication history are fully preserved after a merge, or whether any manual reconciliation is needed. -->

## How do I change a client's email address?

You cannot edit a client's email address directly. Email changes go through a formal request process:

1. Go to **Clients** and open the client's profile.
2. Click **Data correction**.
3. Click **New Request** and fill in the new email address in the `New data entry` field.
4. Click **Submit**.

The Zooza team reviews and processes the request, usually within 2 business days. You receive a notification email when the request is approved or rejected.

A request may be rejected if the new email already belongs to a different client in the system, or if the details do not match the existing record. If you need to assign a booking to a completely different person (not just fix a typo), use **Change Client** on the booking instead.

## How does Client ID work across franchise accounts?

Each client profile can have a `Custom customer ID` field, which you set manually in the client detail. This is a free-text identifier you define for your own tracking purposes (e.g. an internal reference number).

When a child transfers between franchise accounts (separate Zooza companies), the child may exist as a different client record in each account. The Client ID does not sync automatically across franchise accounts. Each franchise manages its own client database independently.

<!-- REVIEW: Confirm whether cross-franchise child transfers create a linked record or a fully independent duplicate. -->

## Can I add a second email address for notifications on a booking?

Yes. You can add an additional email address that receives session reminders for a specific booking. This is useful when separated parents both need to receive notifications about their child's sessions.

1. Open the booking detail.
2. In the booking settings, find **Additional email for reminders before sessions**.
3. Enter the second email address.

This additional email receives session reminder notifications only. It does not receive payment reminders or other booking-level communications. The second email can also be added by the client themselves through their Client Profile.

> **Warning:** If you collect a secondary email address via an **extra field** on the booking form (e.g., Additional field 1), that value is **not** automatically transferred to the system's secondary email field. Extra fields are text-only data collection and are not linked to system notification fields. You must manually copy the email from the extra field into the booking's **Additional settings** → secondary email field for the second parent to actually receive notifications.

## How do I give a divorced parent separate access to the same child?

Zooza supports this through a combination of guest access and additional notification emails:

1. **Guest access to the booking** -- In the booking detail settings, use **Guest access to the booking** to grant a second parent read access via their email address. This lets them view the booking without needing a separate account.
2. **Additional email for reminders** -- Add the second parent's email in the **Additional email for reminders before sessions** field so they receive session notifications independently.

Both parents do not need separate Zooza accounts. The primary client (the parent who created the booking) retains full control, while the second parent gets visibility through guest access and reminder emails.

<!-- REVIEW: Confirm the exact scope of guest access -- does it include viewing attendance and payment status, or only session schedule? -->

## Where can I see which fields are visible to instructors on the attendance screen?

The fields visible to instructors on the attendance screen are determined by the instructor's role and your account settings. By default, instructors see the attendee's name and basic session details.

Whether additional fields like phone number or email are shown depends on the role assigned to the instructor in **Settings** > **Team** > **Access**. The standard instructor role has limited visibility and does not show client contact details on the attendance screen. If you need instructors to see phone numbers or other client data, check the permissions for their assigned role.

Go to **Settings** > **Team** to review which roles have access to client contact information.

<!-- REVIEW: Confirm exact settings path for controlling which client fields are visible on the instructor attendance view. This may require a role with elevated permissions rather than a per-field toggle. -->
