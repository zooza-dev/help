---
title: "Roles and Permissions FAQ"
slug: "roles-and-permissions-faq"
type: "faq"
product_area: "Settings"
sub_area: ""
audience: ["admin"]
tags: ["roles", "permissions", "access", "team"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-13"
intercom_id: 13738682
intercom_sync: false
---

# Roles and Permissions FAQ

## What roles are available in Zooza and what can each do?

Zooza offers six predefined roles with different levels of access:

- **Owner** — full access to all features and settings.
- **Assistant** — broad administrative access including programmes, classes, calendar, clients, bookings, and limited payments (can add payments but cannot adjust prices, issue invoices, or manage payment templates). Can add team members and locations in Settings.
- **Main instructor** — can view and edit all classes and sessions across instructors, manage attendance, see their own clients and bookings, upload documents, and communicate with their clients. Cannot access Programmes, Programme Settings, or the Settings section.
- **Instructor** — can take attendance on their own classes, view their own clients and bookings, add payments, and communicate with their clients. Does not have access to other administrative sections.
- **External instructor** — attendance-only access. Can see their calendar sessions and record attendance. Cannot see client contact details, move or copy bookings, or work with payments.
- **Receptionist** — limited to viewing the current day's sessions, recording attendance (arrived/absent), and adding cash payments. Cannot see client contact details, move bookings, or communicate with clients.

For the full comparison table, go to **Settings --> Team --> Access** and refer to the role matrix displayed below the add-user form. See also: [User roles](../guides/user-roles.md).

## Which role should I assign to an instructor who also handles bookings?

Use the **Instructor** role. This role allows the person to view their own clients and bookings, add payments, and communicate with clients — in addition to taking attendance. If the person also needs to edit sessions across all instructors (e.g., reschedule or reassign sessions), use the **Main instructor** role instead.

The **External instructor** role is not suitable here because it restricts the user to attendance only.

## How do I hide instructor pay rates from other team members?

Only the **Owner** and **Assistant** roles can see instructor pay rates and payout reports. If you have a team member who should not see colleagues' rates, assign them the **Main instructor** role or lower. The Main instructor role does not have access to rate amounts in settings or to payout summaries for other instructors.

## Can I create custom roles with specific permissions?

No. Zooza uses predefined roles. You cannot create custom roles or add individual permissions to an existing role. Each role is a fixed package of access rights.

There are a few toggleable settings under **Settings --> Team --> Settings** that let you fine-tune instructor-level behaviour — for example, whether instructors can see client details, send messages, create substitutions, or manage their own availability. These apply globally to all instructor roles.

## The Main instructor role cannot see Programmes — is this expected?

Yes. The Main instructor role does not have access to Programmes or Programme Settings in the left-hand menu. This is by design — the Main instructor can view and edit individual classes and sessions but cannot modify programme-level configuration.

If the person needs access to Programmes, consider assigning the **Assistant** role instead.

## Which role gives calendar access but hides financial data?

The **Main instructor** role can be configured this way. By default, Main instructors may see a Payments tab. To hide it, go to **Settings --> Team --> Settings** and uncheck the option that allows main instructors to see the Payments section.

Note: even with the Payments section hidden, Main instructors can still see payment logs on individual bookings. The setting hides the dedicated Payments dashboard, received-payments view, and financial graphs.

The **Receptionist** role also hides financial data, but it only provides a daily calendar view (not the full weekly/monthly calendar) and has very limited functionality overall. <!-- REVIEW: Confirm whether receptionist daily view has been updated to show class names, as referenced in support conversation about calendar improvements. -->

## How do I change permissions for an existing role?

You cannot edit the permissions of a role itself — roles are predefined. However, you can change which role is assigned to a team member:

1. Go to **Settings --> Team --> Access**.
2. Select the team member.
3. Change their role from the dropdown.
4. Save.

To adjust global instructor-level settings (e.g., whether instructors can send messages or see client details), go to **Settings --> Team --> Settings**.

## When deactivating an instructor, should I delete or change their role?

Change the role to **Inactive instructor** — do not delete the user. Setting a user to Inactive removes their ability to log in but preserves all historical data: attendance records, session assignments, and payout history remain intact.

If you delete the user instead, you may lose the association between that instructor and their past sessions. In some cases, a deleted user cannot be restored without contacting Zooza support.

To deactivate:

1. Go to **Settings --> Team --> Access**.
2. Select the departing instructor.
3. Change their role to **Inactive instructor**.
4. Save.
