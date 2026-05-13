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
- **Manual only** — admins tick each item themselves. No automatic detection.
- Progress shown as `5 / 9 complete` counter
- Items marked **Required** block the "I'm done" dismiss until ticked
- Items marked **Optional** can be skipped

### Ordering — dependencies matter

Items must be presented in this order (later items depend on earlier ones):

| # | Item | One-liner in UI | Required? | Help article |
|---|------|----------------|-----------|--------------|
| 1 | Add a location | Where your classes take place | Required | `setup/creating-a-location.md` |
| 2 | Create your first programme | Set the name, type, and payment method | Required | `guides/creating-a-programme.md` |
| 3 | Add a class to the programme | Day, time, capacity, and instructor | Required | `guides/creating-a-class.md` |
| 4 | Set up how you collect payments | Stripe, bank transfer, or invoicing | Required | `guides/inbound-payments.md` |
| 5 | Publish your booking link | Copy and share the link to start getting registrations | Required | `guides/customizing-widgets.md` |
| 6 | Do a test booking | Go through the process your clients will experience | Required | `guides/admin-vs-self-service.md` |
| 7 | Add an instructor | Give them access to mark attendance | Optional | `guides/managing-instructors.md` |
| 8 | Enable trials | Let clients book a free or paid try-out before enrolling | Optional | `setup/trial-sessions.md` |
| 9 | Set up booking form fields | Collect extra info from clients at registration (e.g. emergency contact) | Optional | `guides/additional-fields.md` |

### Notes for devs

- All items are **manually ticked** by the admin. No auto-detection.
- Items 1–3 have a strict dependency chain — consider disabling item 3 until item 2 is done, and item 5 until item 3 is done.
- Item 4 (payment setup): the checklist does not need to branch by payment method; just link to the general `inbound-payments.md` guide which covers all paths.
- Items 7–9 are optional — present them with a distinct visual state (e.g., greyed out or a different icon).

---

## Component 2: Daily ops quick reference

### When to show
- Always visible on the dashboard / right panel for admin role
- Never show to instructor role

### What it is
Not a checklist — this is a **persistent quick-access widget**. No completion tracking. No dismissal. Always there.

### Items

Items ordered by actual support frequency (source: Intercom analysis, Feb–Apr 2026, ~135 real conversations).

| #   | Action                                     | One-liner                                                                                                             | Where in app                                       | Help article                                                            | Intercom freq |
| --- | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ----------------------------------------------------------------------- | ------------- |
| 1   | Archive or delete a programme / class      | **Delete** — it was a mistake or you'll never need it again. **Archive** — no longer on sale, but keep the data. | Activities → Programmes → open programme → Archive / Delete | `guides/archive-or-delete-programme.md`                                 | ★★★★          |
| 2   | Find and download invoices                 | Export invoices for your accountant — individually or in bulk                                                         | Sales & Payments → Invoices                        | `guides/where-to-find.md` → Invoices                                    | ★★★           |
| 3   | Make-up sessions                           | Set a make-up rule at programme level, or manage individually in the client's attendance — add a replacement date when they miss a session | Programme → Settings → Make-up OR Open booking → Attendance | `faq/make-up-sessions-faq.md`                                           | ★★★           |
| 4   | Transfer or copy a client to another class | Move a client to a different class or duplicate their booking for a new term                                          | Open booking → Transfer                            | `guides/transfer-and-copy-bookings.md`                                  | ★★★           |
| 5   | Set up and track incoming payments         | Decide how you want to collect and track payments — Stripe, bank transfer (manual or auto-matched), or direct debit | Sales & Payments → Payments → Inbound              | `guides/inbound-payments.md`                                            | ★★★           |
| 6   | Turn off or adjust payment reminders       | Change when clients receive payment notification emails, or turn them off                                             | Settings → Billing → Payments                      | `guides/automatic-payment-reminders.md`                                 | ★★★           |
| 7   | Find where your make-up session summary is | See a report of all make-up sessions across your classes                                                              | Calendar → Make-up sessions                        | `guides/where-to-find.md` → Reports                                     | ★★★           |
| 8   | Share your booking link                    | Get the link or form to share with clients so they can register online                                                | Publish section                                    | `guides/admin-vs-self-service.md`                                       | ★★            |
| 9   | Enrol a client manually                    | Add a client to a class directly from the admin side                                                                  | Clients → New booking                              | `guides/creating-a-booking.md`                                          | ★★            |
| 10  | Mark attendance                            | Mark who showed up to a session                                                                                       | Sessions → select session → Attendance             | `guides/instructor-attendance-management.md`                            | ★★            |
| 11  | Send a bulk email to a class               | Message all clients in a class at once                                                                                | Communication → Send message                       | `guides/sending-email-sms.md`                                           | ★★            |
| 12  | Cancel a session                           | Cancel one session and optionally offer a make-up                                                                     | Calendar → select session → Cancel                 | `guides/edit-sessions-in-programmes.md`                                 | ★★            |
| 13  | Record a manual payment                    | Log a cash or bank transfer payment on a booking                                                                      | Open booking → Payments → Add payment              | `guides/edit-payment-on-booking.md`                                     | ★★            |
| 14  | Copy a class for a new term                | Duplicate a class structure for the next term (term rebooking)                                                        | Activities → Classes → Copy                        | `guides/copy-programme-and-class.md` + `guides/term-rebooking-guide.md` | ★★            |
| 15  | Set up a sibling discount                  | Give a discount to clients who have multiple children enrolled                                                        | Sales & Payments → Discounts                       | `guides/loyalty-sibling-discount.md`                                    | ★★            |
| 16  | Set up an instructor substitute            | Assign a different instructor to a session when the regular one is unavailable                                        | Activities → Sessions → Edit                       | `guides/instructor-substitution.md`                                     | ★★            |

### Notes for devs

- This is a static list — no interaction tracking needed.
- Consider collapsing it by default on mobile and expanding on desktop.
- Items render as: **title** (bold link) + one-liner text + arrow to help article.
- Item 1 (archive/delete) is the single biggest support driver — prioritise its discoverability and make the delete vs. archive distinction clear in the UI.
- Future iteration: personalise based on payment method (e.g. hide inbound payments item for Stripe-only accounts).
- Source data: Intercom support analysis Feb–Apr 2026, `build/reports/intercom-analysis-report.md`.

---

## Content gaps — articles that need to be created or improved

Source: Intercom analysis (★ = support frequency) + logical audit.

| Gap | Intercom signal | Impact | Suggested article / action |
|-----|----------------|--------|---------------------------|
| No dedicated "archive or delete programme/class" guide — admins search for "delete" but the action is "archive" | ★★★★ | High | `guides/archive-or-delete-programme.md` — explain archive vs delete, when each applies |
| GoCardless renewal flow not documented as a standalone how-to — buried in `inbound-payments.md` | ★★★ | High | Add a dedicated section "Renewing your GoCardless connection" with step-by-step |
| Notifications overview missing — admins can't find where payment reminders are controlled | ★★★ | High | `guides/where-to-find.md` already updated with path; consider `guides/notification-settings-overview.md` |
| Make-up session summary / bulk report — Intercom shows this is a top ★★★ question | ★★★ | High | Document where the make-up sessions report is; flag the known gap (no filter by location — product issue) |
| No dedicated "how to share your booking link" — currently only in `customizing-widgets.md` | ★★ | Medium | Add dedicated section in `guides/admin-vs-self-service.md` |
| `inbound-payments.md` does not clearly fork by payment method at the top | ★★★ | High | Add decision table: Stripe / bank transfer / invoicing paths |
| No article on export — what's in "Clients export" vs "Registrations export" | ★★ | Medium | Add to `guides/where-to-find.md` or create `guides/export-guide.md` |
| `creating-a-location.md` — verify screenshots present for Setup step 1 | Low | Low | Review |
| `additional-fields.md` — confirm it covers setup flow, not just reference | Low | Low | Review |
| No article explaining what the client sees after registering (Client Profile / Parent Zone) | — | High | `guides/parent-zone-guide.md` — flagged in `onboarding-brief.md` as missing |

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
*Inputs: onboarding-brief.md, core-workflows.md, intercom-analysis-report.md, screenshot of current Zooza dashboard (uk.zooza.app)*
