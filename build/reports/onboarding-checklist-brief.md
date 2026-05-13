# Onboarding Checklist & Daily Ops Quick Reference — Product Brief

**Date:** 13 May 2026
**For:** Dev team + content agent
**Context:** In-app onboarding for new admins migrating from Thinksmart or starting fresh. Reference: `build/reports/onboarding-brief.md` for full user journey context.

---

## Design principle

Two distinct UX components — do not conflate them:

| Component | What it is | UX pattern | Lives where |
|-----------|-----------|------------|-------------|
| **Setup checklist** | One-time setup tasks, tracked per account | Progressing checklist with completion state | Right panel (Todos-style), shown on new accounts only |
| **Daily ops quick reference** | Persistent shortcuts to common operations | Non-tracked list of links + one-liners | Right panel (collapsed section) or dashboard widget |

---

## Component 1: Setup checklist

### When to show
- Trigger: account created (or: 0 bookings + < 7 days old)
- Auto-dismiss: when all required items are checked OR admin clicks "I'm done setting up"
- Never show to: instructor role (they have a separate, simpler onboarding)

### Completion tracking
- Each item has a **completion trigger** (app event that auto-marks it done)
- Admin can also manually tick any item
- Progress shown as `5 / 9 complete` counter
- Items marked **Required** block the "I'm done" dismiss until complete
- Items marked **Optional** can be skipped

### Ordering — dependencies matter

Items must be presented in this order (later items depend on earlier ones):

| # | Item | One-liner in UI | Required? | Completion trigger | Help article |
|---|------|----------------|-----------|-------------------|--------------|
| 1 | Add a location | Where your classes take place | Required | Location created | `setup/creating-a-location.md` |
| 2 | Create your first programme | Set the name, type, and payment method | Required | Programme created | `guides/creating-a-programme.md` |
| 3 | Add a class to the programme | Day, time, capacity, and instructor | Required | Class created with at least 1 session | `guides/creating-a-class.md` |
| 4 | Set up how you collect payments | Stripe, bank transfer, or invoicing | Required | Payment method connected OR invoice profile saved | `guides/inbound-payments.md` |
| 5 | Publish your booking link | Copy and share the link to start getting registrations | Required | Publish section opened | `guides/customizing-widgets.md` |
| 6 | Do a test booking | Go through the process your clients will experience | Required | ≥1 booking exists | `guides/admin-vs-self-service.md` |
| 7 | Add an instructor | Give them access to mark attendance | Optional | Instructor added to Team | `guides/managing-instructors.md` |
| 8 | Enable trials | Let clients book a free or paid try-out before enrolling | Optional | Trial enabled on any programme | `setup/trial-sessions.md` |
| 9 | Set up booking form fields | Collect extra info from clients at registration (e.g. emergency contact) | Optional | At least 1 additional field added | `guides/additional-fields.md` |

### Notes for devs

- Items 1–3 have a strict dependency chain — consider disabling item 3 until item 2 is done, and item 5 until item 3 is done.
- Item 4 (payment setup) branches by method:
  - Stripe → link to Stripe connection
  - Bank transfer + GoCardless → link to GoCardless inbound setup
  - Invoicing only → link to invoice profile setup
  - The checklist does not need to branch; just link to the general `inbound-payments.md` guide which covers all paths.
- Item 5 (publish) completion trigger could be: admin visits the Publish section OR copies the booking link.
- Item 6 (test booking) is complete when ≥1 booking exists on any class.
- Items 7–9 are optional — present them with a distinct visual state (e.g., greyed out or a different icon).

---

## Component 2: Daily ops quick reference

### When to show
- Always visible on the dashboard / right panel for admin role
- Never show to instructor role

### What it is
Not a checklist — this is a **persistent quick-access widget**. No completion tracking. No dismissal. Always there.

### Items

| # | Action | One-liner | Where in app | Help article |
|---|--------|-----------|--------------|--------------|
| 1 | Enrol a client | Add a client to a class — manually or send them a link to register themselves | Clients → New booking OR share booking link | `guides/creating-a-booking.md` + `guides/admin-vs-self-service.md` |
| 2 | Transfer a client | Move a client to a different class or time slot | Open booking → Transfer | `guides/transfer-and-copy-bookings.md` |
| 3 | Mark attendance | Mark who showed up to a session | Sessions → select session → Attendance | `guides/instructor-attendance-management.md` |
| 4 | Send an email to a class | Message all clients in a class at once | Communication → Send message | `guides/sending-email-sms.md` |
| 5 | Cancel a session | Cancel one session and optionally offer a make-up | Calendar → select session → Cancel | `guides/edit-sessions-in-programmes.md` |
| 6 | Record a payment | Log a cash or bank transfer payment on a booking | Open booking → Payments → Add payment | `guides/edit-payment-on-booking.md` |
| 7 | Copy a class for a new term | Duplicate a class structure for the next term | Activities → Classes → Copy | `guides/copy-programme-and-class.md` |
| 8 | Offer a make-up session | Give a client a replacement for a missed session | Open booking → Attendance → Book session | `guides/custom-replacement-lessons.md` |

### Notes for devs

- This is a static list — no interaction tracking needed.
- Consider collapsing it by default on mobile (small screen) and expanding on desktop.
- Items can be rendered as: **title** (bold link) + one-liner text + arrow to help article.
- Future iteration: personalise based on what the admin actually uses (e.g. hide "record payment" for Stripe-only users).

---

## Content gaps — articles that need to be created or improved

| Gap | Impact | Suggested article |
|-----|--------|------------------|
| `creating-a-location.md` exists but may lack screenshots for Setup step 1 — verify | Medium | Review `setup/creating-a-location.md` |
| No dedicated "how to share your booking link" article — currently only in `customizing-widgets.md` | Medium | Could be a short guide or a section in `admin-vs-self-service.md` |
| `inbound-payments.md` covers GoCardless but does not clearly fork by payment method at the top | High | Add a decision table at the top: "choose your path: Stripe / bank transfer / invoicing" |
| `additional-fields.md` — confirm it covers the setup flow, not just reference | Low | Review |
| No article explaining what the client sees after they register (client-side experience, Parent Zone) | High | `guides/parent-zone-guide.md` — flagged in `onboarding-brief.md` as missing |

---

## Open questions for devs

1. **Persistence:** Does the Setup checklist state persist per user or per account? (If the owner checks it done on web, is it also done on mobile?)
2. **Completion triggers:** Which events are available as triggers? (e.g. can we listen for "first booking created" or "Stripe connected"?)
3. **Role visibility:** Confirmed that instructors do not see the Setup checklist or Daily ops panel?
4. **Dismissal:** Can admin permanently dismiss the Setup checklist? Or does it auto-disappear after all Required items are done?
5. **Right panel:** Is the Setup checklist a separate tab from Todos, or does it live inside the same panel? (See screenshot — right panel currently shows Todos with 4 items.)

---

## What the instructor sees (separate track)

Instructors get neither the Setup checklist nor the Daily ops panel. Their onboarding is a separate, simpler flow:

1. Log in
2. Add Zooza to phone home screen
3. Find your sessions
4. Mark attendance

Reference: `guides/managing-instructors.md`, `guides/zooza-101-instructors.md` (if exists).

---

*Brief by Michal Dodok / Claude Code, 13 May 2026*
*Inputs: onboarding-brief.md, core-workflows.md, screenshot of current Zooza dashboard (uk.zooza.app)*
