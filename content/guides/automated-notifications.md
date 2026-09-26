---
title: "Automated notifications overview"
description: "Zooza sends automated emails to clients based on events — booking created, session approaching, payment due, and so on."
slug: "automated-notifications"
type: "guides"
product_area: "Communication"
sub_area: "Email"
audience: ["admin"]
tags: ["notifications", "email", "automation", "reminders", "templates", "opt-out"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-09-26"
related_articles: ["message-templates", "dynamic-tags", "pay-as-you-go-programme", "pay-as-you-go-faq", "entry-pass-client-view"]
---


# Automated notifications overview

Zooza sends automated emails to clients based on events — booking created, session approaching, payment due, and so on. This guide covers all notification types, where each is configured, and how clients or admins can turn them off.

## Key concepts

**Templates vs. automation steps**

Every automated notification uses an email template. Templates are editable in **Communication → Templates** (owner access required). Some system-level notifications (login link, unknown user) use fixed system templates that cannot be edited.

Automation steps (for bookings, trials, waitlist) can be toggled on or off individually per programme in **Programmes → programme → Automations**.

**Transactional vs. marketing emails**

- **Transactional** — booking confirmations, payment reminders, session reminders. Clients cannot opt out from these through Zooza. Admins can disable them at the programme level.
- **Marketing / promotional** — manually composed emails that the admin marks as promotional when sending. Clients who have **Send promotional emails** unchecked on their profile will not receive these.

---

## Client opt-out mechanisms

There are three ways a client can opt out of specific notification types. All other notifications are transactional and cannot be opted out from.

| Mechanism | What it turns off | How |
|---|---|---|
| **Unsubscribe link in session reminder email** | Session reminders and session-change notifications for that booking | Client clicks `TURN_OFF_EVENT_NOTIFICATIONS_URL` link in the email → sets reminder opt-out on that registration |
| **Unsubscribe link in upcoming events digest** | Upcoming session digest emails for that booking | Client clicks `TURN_OFF_UPCOMING_EVENTS_NOTIFICATIONS_URL` link in the email |
| **Feedback unsubscribe link** | Feedback/rating request emails | Client clicks unsubscribe link in feedback email |

> **Admin toggle for session reminders:** The reminder opt-out can also be toggled by the admin in the booking/registration detail → **Options** tab → **Reminder**. Client preference takes precedence — if a client has opted out, the admin turning it back on only applies until the client opts out again.

**Marketing messages** are controlled per client via **Clients → client → Notes and preferences → Send promotional emails** checkbox. Both the admin and the client (via client portal) can manage this.

---

## Notification types by category

### Registration and booking confirmations

| Notification | Trigger | Config location | Editable? |
|---|---|---|---|
| **Booking confirmation** | Client completes a full programme booking | Programmes → Automations → Bookings (on by default; can be toggled off) | Yes |
| **Late booking confirmation** | Client books a programme already in progress | Programmes → Automations → Late Bookings | Yes |
| **Pay-as-you-go booking confirmation** | Client books into an open/pay-as-you-go session | Automatic | Yes |
| **Single event booking confirmation** | Client books a one-off event | Automatic | Yes |
| **Guest booking confirmation** | Client enrols as a guest | Automatic | Yes |
| **Imported booking confirmation** | Client is imported (bulk import) | Automatic on import | Yes |
| **Import invitation** | Client is imported into Zooza for the first time; admin is prompted during import whether to send | Manual trigger during import | Yes |
| **Lead collection confirmation** | Client books via a lead-collection widget | Automatic | Yes |
| **Sessions booked** | Client books several sessions at once on an open programme — one email listing them all instead of one per session | Automatic | Yes — **Sessions booked** in Communication → Templates |

No client opt-out exists for any booking confirmation. Admins can disable the automation step per programme.

> **Sessions booked** only appears in the Templates list for providers who run
> open (pay-as-you-go) programmes — nothing on a full-duration or one-off
> programme sends it. It is a transactional confirmation: it is sent by the
> system, cannot be composed by hand, and carries no unsubscribe link. Its only
> content tag is <code>&#42;&#124;BOOKED_SESSIONS&#124;&#42;</code>, which
> renders the whole list of sessions the client just booked — the course, date,
> time, venue and instructor are inside that block and are not available as
> separate tags on this template.

---

### Trial workflow

All trial emails are configured at **Programmes → programme → Automations → Trials**. Each step can be toggled on or off independently.

| Notification | Trigger | Client opt-out? |
|---|---|---|
| **Trial booking confirmation** | Client books a trial class | No |
| **Trial ended — booking link** | Attendance recorded on the last trial session | No |
| **Trial follow-up (1st / 2nd)** | No full booking made N days after trial (timing configurable) | No |
| **Trial lead lost** | Trial manually marked as lost | No |

---

### Waitlist

| Notification | Trigger | Config location | Client opt-out? |
|---|---|---|---|
| **Waitlist confirmation** | Client placed on waitlist | Programmes → Automations → Waitlist | No |
| **Waitlist — space opened** | A spot opens and client is next | Programmes → Online Booking → Edit → Auto waitlist notification toggle | No |

---

### Session reminders and schedule changes

| Notification | Trigger | Config location | Client opt-out? |
|---|---|---|---|
| **Session reminder** | Before an upcoming session (timing configurable) | Programmes → Online Booking → Edit → Send event notifications toggle; template selectable | **Yes** — unsubscribe link in email, or admin toggles per booking (Options tab → Reminder) |
| **Session booking reminder** | A client on an open programme has not booked any upcoming session (weekly) | Programmes → Online Booking → Edit → Upcoming events notifications toggle | **Yes** — unsubscribe link in email, or admin toggles per booking (Options tab → Reminder) |
| **Session changed** | Session details modified by admin (time, venue, instructor, status) | Automatic when session is edited | **Yes** — same as session reminder opt-out |
| **Signed up for open session** | Client enrols in a specific pay-as-you-go session | Automatic | No |

#### The session booking reminder on open programmes

On an open (pay-as-you-go) programme, signing up is not the same as having a
seat: the client still has to go into their profile and book individual
sessions. Many never take that second step — they register, sometimes buy a
pack of entry passes, and then nothing happens.

The reminder that used to be a plain daily list of tomorrow's sessions is now
aimed at exactly those clients. Once a week, a client who has **no upcoming
booked session** gets one email built from their own situation, with a
**Book** button for each suggested session:

| The client's situation | What the email leads with |
|---|---|
| Has entry passes, plenty left | Their balance and validity, plus sessions to book |
| Has passes expiring within 14 days | Use them before they expire |
| Has 2 or fewer passes left | Sessions to book, plus a gentle top-up link |
| Has an unpaid entry-pass order | Pay the order first — with the order number and amount |
| Passes expired unused in the last 30 days | Welcome back, plus a top-up |
| Has no passes at all | Book or buy passes (on a passes-only programme, buy first) |

Sessions are suggested from the client's usual slot where the class has one —
their regular Monday, or both days on a twice-weekly class — otherwise the
soonest session with a free place.

Two things worth knowing:

- **Clicking Book never books anything.** The link logs the client in and opens
  their session picker with that session pre-selected; they still confirm it
  themselves. So a mail client that pre-loads links cannot hold a place or spend
  a pass.
- **Clients who already booked are never nudged.** The check runs again at send
  time, so a client who booked an hour earlier drops out.

**It stops on its own.** Three weekly reminders with no response, then a
30-day pause, then one last reminder — about four emails over two months. After
that Zooza stops nudging that registration. Booking a session starts it again
automatically.

#### Restarting reminders that stopped themselves

Open the booking and look at the **Communication** card. If Zooza gave up on
this registration it says so, and offers **Start reminders again**.

If the client has turned reminders off themselves, the card says that instead
and shows **no button** — restarting would send nothing, because a reminder
needs both the client's consent and an active reminder state. Change
**Reminder** on the **Options** tab first if that is what you intend; be aware
you are overriding the client's own choice.

---

### Cancellations

| Notification | Trigger | Client opt-out? |
|---|---|---|
| **Cancellation confirmation** | Client cancelled from a session | No |
| **Scheduled cancellation** | Cancellation scheduled in advance | No |
| **Scheduled cancellation confirmed** | Scheduled cancellation processed | No |
| **Automatic deletion** | Unpaid booking auto-deleted after payment reminder deadline | No (configured via Programmes → Settings → Price and payment → Payment Reminders → Delete unpaid registrations) |

---

### Payment notifications

**Global payment notification settings** — configured at **Settings → Billing & Payments → Payment settings** (account level, applies to all programmes):

| Setting | What it controls |
|---|---|
| **Notify before a scheduled payment is issued** | Whether clients are notified before a scheduled payment is created; configurable N days in advance |
| **Send notification after manual payment entry** | Whether a payment confirmation is sent when admin manually records a payment |
| **Send notification after file import** | Whether a payment confirmation is sent after a CSV payment import |
| **Text of the payment confirmation** | Custom text appended to every payment confirmation email |

**Per-programme payment reminders** (overdue/missed payments) — configured at **Programmes → programme → Settings → Price and payment → Payment Reminders**:

| Notification | Trigger | Client opt-out? |
|---|---|---|
| **Payment received** | Payment confirmed (online, manual entry, or file import) | No |
| **Upcoming payment** | Scheduled payment due soon (timing: N days before creation, set globally) | No |
| **Missed payment** | Payment due date passed unpaid | No |
| **Offline payment reminder** | Offline/manual payment due soon | No |
| **Offline payment missed** | Offline payment deadline passed | No |
| **New payment entry created** | Payment record created | No |
| **Client invoice generated** | Invoice created for client | No |
| **Discount code** | Discount code assigned to client | No |
| **First payment reminder** | First automated debt reminder | No |
| **Second payment reminder** | Second automated debt reminder | No |

---

### Retention (auto-enrolment)

| Notification | Trigger | Config location | Client opt-out? |
|---|---|---|---|
| **Retention notification** | Configurable number of days before the programme ends | Programmes → Automations → Auto-enrolment → timing and message settings | No (client can ignore the link) |

---

### Feedback and rating requests

| Notification | Trigger | Config location | Client opt-out? |
|---|---|---|---|
| **Feedback — during programme** | After the 4th session of an ongoing programme | Programmes → Settings → Feedback → "During programme" toggle | Yes — unsubscribe link in email |
| **Feedback — after programme** | After programme ends | Programmes → Settings → Feedback → "After programme" toggle | Yes — unsubscribe link in email |

---

### Make-up and reschedule requests (custom replacement)

These are transactional status updates — no opt-out exists.

| Notification | Trigger |
|---|---|
| **Make-up request created** | Client creates a custom make-up session request |
| **Make-up request accepted** | Admin approves the request |
| **Make-up request rejected** | Admin rejects the request (reason included) |
| **Make-up request cancelled** | Client cancels their own request |
| **Reschedule request accepted** | Admin accepts client's reschedule request |
| **Reschedule request rejected** | Admin rejects reschedule request (reason included) |
| **Reschedule request cancelled** | Request cancelled |

---

### Orders and account

| Notification | Trigger | Editable? |
|---|---|---|
| **Shop order confirmation** | Client completes a shop order | Yes |
| **Login / password** | Login link or password reset requested | No (system) |
| **Unknown user** | Login attempted for unrecognised email | No (system) |
| **Client data change request processed** | Admin processes a data-change request | No (system) |

---

## Admin configuration summary

| What you want to do | Where to go |
|---|---|
| Edit any notification template | **Communication → Templates** |
| Disable booking/trial/waitlist automation step | **Programmes → programme → Automations** |
| Enable/disable session reminders | **Programmes → programme → Online Booking → Edit → Send event notifications** |
| Configure global payment notification toggles (before payment creation, after manual entry, after import) | **Settings → Billing & Payments → Payment settings** |
| Configure payment reminders and auto-deletion for overdue payments | **Programmes → programme → Settings → Price and payment → Payment Reminders** |
| Enable/disable feedback requests | **Programmes → programme → Settings → Feedback** |
| Toggle session reminders for one specific booking | **Booking/registration detail → Options tab → Reminder** |
| Stop marketing emails for one client | **Clients → client → Notes and preferences → Send promotional emails** |

## Send a one-off email for a specific session

In addition to automatic notifications, you can send a custom one-off email for a particular session — useful when you need to communicate something specific, such as "bring your workbook to today's class."

1. Go to the **Sessions** tab or the **Classes** tab and find the session date.
2. Click on the session to open its detail.
3. Open the **Automation** tile.
4. Choose **Send email before** or **Send email after** the session.
5. Set the timing offset (e.g. 1 hour after), write the subject and message, and save.

The email is sent automatically to all enrolled clients based on the timing you set. Each session can have its own individual message independent of the programme-level notification templates.
