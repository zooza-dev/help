---
title: "Add instructors and manage their access"
description: "How to add instructors to Zooza, choose the right role, understand what they can see and do, and set them up for day one."
slug: "managing-instructors"
type: "guides"
product_area: "Settings"
sub_area: ""
audience: ["admin"]
tags: ["instructor", "role", "access", "permissions", "team", "onboarding", "mobile"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-05-11"
---

# Add instructors and manage their access

## How to add an instructor

1. Go to **Settings → Team**.
2. Click **Add**.
3. Enter the instructor's name and email address.
4. Select a role (see [role guide below](#which-role-to-choose)).
5. Click **Add new user**.

The instructor receives a login link by email. They don't need a password — they enter their email on the Zooza login page and receive a link each time.

> **Use real email addresses only.** Any email address you add gains access to your account. Do not use placeholder addresses.

---

## What instructors see — and what they don't

This is the most important thing to understand before you onboard your first instructor.

**Instructors do not see the same navigation as you.** Their view is limited based on their role. A standard instructor logs in and sees:

```
Dashboard     (upcoming sessions only — no statistics)
Calendar      (their own classes only)
Instructor    (their own profile and reports)
Menu          (limited — no Programmes, no Payments, no full Settings)
```

An admin sees the full navigation including Programmes, Clients, Bookings, Payments, Reports, and Settings.

**The most common confusion:** You follow a guide that says "Go to Activities → Classes" — your instructor tries to do the same and sees nothing. This is expected. Standard instructors don't have access to the Classes list. If they need it, change their role to **Main instructor**.

---

## Which role to choose

| Role | What they can do | Best for |
|------|-----------------|----------|
| **Instructor** | Mark attendance on their own classes. View their own clients and bookings. Send emails/SMS to their own clients. Add payments. See their taught hours. | Most instructors |
| **External instructor** | Mark attendance only — no access to clients, payments, or communication. | Cover staff, substitutes, or anyone you want to restrict to attendance only |
| **Main instructor** | Everything Instructor can do, plus: see all instructors' classes, edit sessions (time, instructor, location), upload documents. | Senior instructors, team leads |
| **Receptionist** | Can see bookings and clients, manage attendance across all classes, and process payments. Cannot edit programmes or settings. | Front desk / admin support |
| **Assistant** | Full operational access: programmes, classes, bookings, payments, client data. Cannot change owner-level settings. | Business manager or studio coordinator |
| **Owner** | Full access to everything including settings, billing, and integrations. | You — and anyone who should have full control |

**If you're unsure, start with Instructor.** You can change the role at any time without losing any data.

---

## What instructors do on day one

Once added, share these two resources with each instructor:

1. **Login guide** — [Zooza 101 for instructors](zooza-101-instructors.md) — covers login, marking attendance, mobile setup
2. **Mobile setup** — [Add Zooza to your phone's home screen](../setup/add-zooza-app-to-phone.md)

The most critical step is marking attendance. Make sure they know:
- Their upcoming sessions appear on the dashboard immediately after login
- Quick view (top-right toggle in any session) is the fastest way to mark attendance on mobile
- They only see classes they are assigned to as the main or substitute instructor

---

## Instructor attendance settings

You control how much detail instructors see when marking attendance. Go to **Settings → Team → [instructor name]** to configure:

| Setting | What it controls |
|---------|-----------------|
| **Attendance report type** | Full report (client details, payment status, consents) or limited view (names only) |
| **Client visibility** | Whether instructors can see client contact details |
| **Communication access** | Whether instructors can send emails and SMS |
| **Substitution management** | Whether instructors can arrange their own cover |

These settings apply per-instructor, so you can give more detail to senior instructors and restrict newer ones.

---

## Common instructor problems and fixes

**"My instructor says they can't find Classes in the menu"**
Expected. Standard instructors and External instructors don't see the Classes list. If they need it, change their role to **Main instructor** in **Settings → Team**.

**"My instructor can't send emails to clients"**
Email access requires at least the **Instructor** role. External instructors cannot send messages. Change their role, or have an admin send the email on their behalf.

**"My instructor can't see a class they should be teaching"**
Check that the instructor is assigned to that class. Go to the class → **Details** → **Instructor** and confirm the assignment. An instructor only sees classes where they are listed as main or substitute instructor.

**"My instructor didn't receive the login email"**
- Confirm the email address is correct in **Settings → Team**
- Ask them to check spam
- They can also go to the Zooza app URL, enter their email, and request a new login link at any time — no invitation needed

**"I need to remove an instructor without losing their history"**
Don't delete the account. Change their role to **Inactive** in **Settings → Team**. This blocks login but keeps all attendance records, session history, and reports intact.

---

## Related guides

- [Zooza 101 for instructors](zooza-101-instructors.md) — send this to new instructors
- [Attendance management for instructors](instructor-attendance-management.md) — detailed attendance guide for instructors
- [Instructor substitution](instructor-substitution.md) — managing cover when an instructor can't teach
- [Two instructors per class](two-instructors-per-class.md) — assign a main and assistant instructor
- [Instructor rates and pay](../setup/instructor-rate-reward.md) — set up compensation
- [User roles](user-roles.md) — full permissions table for all roles
