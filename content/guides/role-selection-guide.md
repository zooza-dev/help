---
title: "Role Selection Guide"
slug: "role-selection-guide"
type: "guides"
product_area: "Settings"
sub_area: ""
audience:
  - admin
tags:
  - roles
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: true
last_converted: "2026-02-13"
---

# Role Selection Guide

Zooza uses **predefined role packages** to control what each team member can see and do. You cannot create custom roles or assign individual permissions — each role is a fixed set of access rights. This guide helps you choose the right role for each person on your team.

For a detailed description of each role's capabilities, see [User roles](user-roles.md). For common questions, see [Roles and Permissions FAQ](../faq/roles-and-permissions-faq.md) and [Instructor Access FAQ](../faq/instructor-access-faq.md).

## Role comparison table

The table below shows what each role can access. A checkmark means full access, a tilde (~) means partial or limited access, and a dash means no access.

| Capability | Owner | Assistant | Main instructor | Instructor | External instructor | Receptionist |
|---|---|---|---|---|---|---|
| **Dashboard** | Full stats | Today's sessions | Today's sessions | Today's sessions | Today's sessions | Today's sessions |
| **Calendar** | Full | Full (all instructors) | Full (all instructors) | Own sessions only | Own sessions only | Daily view only |
| **Programmes** | Full | Full (create, edit, copy) | — | — | — | — |
| **Classes** | Full | Full (create, edit, copy) | View and edit all | Own classes only | — | — |
| **Sessions** | Full | Full (edit, cancel, notify) | Edit all (time, instructor, cancel) | View own | View own | Current day only |
| **Bookings** | Full | Full (edit, move, copy) | Own clients only | Own clients only | View only (limited) | View only (no move/copy) |
| **Clients** | Full | Full | Own clients only | Own clients only | No contact details | No contact details |
| **Attendance** | Full | Full report | Full report | Full or limited (configurable) | Record only | Arrived / Did not arrive |
| **Payments dashboard** | Full | Limited (no invoices, no imports) | Configurable (can be hidden) | — | — | — |
| **Add payment** | Yes | Yes | Yes | Yes | — | Yes (cash only) |
| **Adjust price / refund** | Yes | — | — | Yes (discount, refund, amount) | — | — |
| **Communication** | Full | Full (all clients, email + SMS) | Own clients only | Own clients only | Configurable | — |
| **Email templates** | Create and edit | View only (cannot create) | — | — | — | — |
| **Documents & Products** | Full | Add and assign | Upload and assign to classes | — | — | — |
| **Instructors / Team** | Full | View all, manage data and rates | — | Own working hours only | — | — |
| **Reports** | Full | — | — | — | — | — |
| **Settings** | Full | Limited (add team member, location, billing period; no payment templates) | — | — | — | — |
| **Pay rates visibility** | See all | See all | Cannot see | Cannot see | Cannot see | Cannot see |

<!-- REVIEW: Confirm whether Main instructor "Adjust price / refund" is truly unavailable. The user-roles guide says they can "manage client payments" but does not specify price adjustment. Support conversations suggest they have limited payment management. -->

## Common team scenarios

Use these recommendations to match roles to real-world job functions.

### Solo business owner

**Recommended role:** Owner

You need full access to every feature — programmes, payments, reports, settings, and communication. There is only one Owner role per account.

### Office manager or admin assistant

**Recommended role:** Assistant

An office manager who handles day-to-day administration — creating programmes, managing bookings, pairing payments, adding team members — should use the Assistant role. The Assistant has broad access but cannot:

- See statistical reports on the dashboard
- Create or edit email templates
- Edit payment templates
- Issue or manage invoices
- Import payments
- Adjust prices, grant discounts, or refund payments

### Head instructor who manages the schedule

**Recommended role:** Main instructor

A senior instructor who coordinates the timetable, reassigns sessions to other instructors, and uploads materials should use the Main instructor role. This role can edit sessions across all instructors but cannot access Programmes, Programme Settings, or the Settings section.

If the person also needs to manage programmes or add team members, consider the Assistant role instead.

### Regular instructor

**Recommended role:** Instructor

A standard instructor who teaches their own classes, records attendance, communicates with their own clients, and occasionally handles payments. The Instructor role provides enough access for day-to-day teaching responsibilities without exposing administrative or financial data from other instructors.

### Freelance or guest instructor

**Recommended role:** External instructor

A freelance, substitute, or guest instructor whose only task is to show up and record attendance. The External instructor role intentionally restricts access:

- Cannot see client contact details (email, phone)
- Cannot move or copy bookings
- Cannot add or manage payments
- Can write internal notes on session details
- Can be allowed to send messages if configured in global instructor settings

### Front desk or receptionist

**Recommended role:** Receptionist

A temporary worker or front-desk assistant who checks clients in and collects cash payments. The Receptionist role is the most restricted:

- Sees only a daily view of sessions (not the full calendar)
- Can record attendance as arrived or absent (no alternate session selection)
- Can add a cash payment but cannot adjust, refund, or assign payment templates
- Cannot see client contact details
- Cannot communicate with clients
- Can register walk-in clients for pay-as-you-go programmes

<!-- REVIEW: As of Feb 2026, the receptionist daily view now shows class/group names — confirmed in support conversation. Verify this is reflected in the UI. -->

## What each role cannot see — key restrictions

Understanding what a role **cannot** do is often more important than what it can do.

| Role | Key restrictions |
|---|---|
| **Assistant** | No statistical reports, no invoice management, no payment template editing, no price adjustments or refunds |
| **Main instructor** | No Programmes menu, no Programme Settings, no Settings section, no pay-rate visibility for colleagues |
| **Instructor** | No access outside own clients/classes, no administrative sections, no reports |
| **External instructor** | No client contact details, no booking management, no payments, no documents |
| **Receptionist** | Daily view only, no client contact details, no booking moves/copies, no communication, no calendar navigation |

## How to change a team member's role

1. Go to **Settings --> Team --> Access**.
2. Select the team member you want to update.
3. Change their role from the dropdown menu.
4. Click **Save**.

Role changes take effect immediately. The team member will see their updated menu and permissions the next time they load the app.

## Deactivating vs. deleting team members

When a team member leaves, **do not delete their account**. Instead, change their role to **Inactive instructor**.

| Action | What happens |
|---|---|
| **Set to Inactive** | The user loses login access. All historical data is preserved — attendance records, session assignments, and payout history remain intact. You can reactivate the user later if needed. |
| **Delete the user** | The association between the user and their past sessions may be lost. In some cases, a deleted user cannot be restored without contacting Zooza support. |

To deactivate a departing team member:

1. Go to **Settings --> Team --> Access**.
2. Select the departing team member.
3. Change their role to **Inactive instructor**.
4. Click **Save**.

If you accidentally deleted a user, contact Zooza support to request reactivation. Support can restore the account and re-link it to historical data.

## Tips for franchise and multi-location setups

<!-- REVIEW: Multi-location role behaviour is inferred from support conversations. Confirm the following points with the product team. -->

- Roles are assigned **per account**. If your franchise has separate Zooza accounts for each location, a person needs a separate user record in each account.
- An instructor who works at multiple locations needs to be added as a team member in each account with the appropriate role.
- When deactivating an instructor across multiple locations, remember to set them to Inactive in **every** account where they are listed.
- The Receptionist role is well-suited for location managers who need to check clients in and add payments but should not have access to programme configuration or financial reports.
- If a location manager needs broader access (e.g., editing the timetable, communicating with all clients), use the Assistant role for that location's account.

## Configurable instructor settings

While roles themselves are fixed, you can fine-tune some instructor-level behaviours for all instructor roles at once. Go to **Settings --> Team --> Settings** to configure:

- Whether instructors can see client contact details
- Whether instructors can send messages (email/SMS) to clients
- Whether instructors can create substitutions on sessions
- Whether instructors can manage their own availability
- How instructors see the attendance report (full or limited)
- Whether Main instructors can see the Payments section

These settings apply globally — they affect all users with an instructor-type role (Instructor, Main instructor, External instructor).

## Related resources

- [User roles](user-roles.md) — detailed description of each role's capabilities
- [Roles and Permissions FAQ](../faq/roles-and-permissions-faq.md) — common questions about roles and access
- [Instructor Access FAQ](../faq/instructor-access-faq.md) — instructor login and access questions
