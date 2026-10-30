---
title: "Instructor Access and Roles FAQ"
description: "Instructors log in at your regional Zooza address, enter their email, and get a secure login link. What to check when the email never arrives."
slug: "instructor-access-faq"
type: "faq"
product_area: "Settings"
sub_area: ""
audience: ["admin"]
tags: ["attendance", "booking", "client", "communication", "import", "instructor", "loyalty", "onboarding", "payment", "role", "session", "settings"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-10-30"
related_articles: ["login-and-account-faq","managing-instructors","user-roles","role-selection-guide"]
---

# Instructor Access and Roles FAQ

## How do instructors log in to Zooza?

Instructors go to your regional Zooza app URL — `zooza.app` for Europe, `uk.zooza.app` for the UK, `asia.zooza.app` for the Middle East and Asia — enter their email address, and receive a secure login link by email. There is no password — they click the link to access the system.

If an instructor says the email never arrives, check these two things before anything else:

1. **They are on the right regional address.** Requesting a link on the wrong one never produces an email. See [Which address do we log in at?](login-and-account-faq.md#which-address-do-we-log-in-at)
2. **They are using the exact address listed for them** in **Settings → General → Access**. A link is only ever sent to an address that already has access — a personal address the person prefers, or one with a typo, produces nothing.

If both are right and it still does not arrive, send Zooza support the instructor's name and the address they are trying, and the login attempt can be traced.

## An instructor did not receive the invitation email — what should I do?

1. Check that the email address is correct in **Settings → General → Access**.
2. Try sending a new invitation.
3. Ask the instructor to check their spam/junk folder.
4. If using a corporate email, there may be delivery delays.

Note: Instructors do not need a formal invitation to log in. If they are listed as an instructor in the system, they can go to the Zooza app URL and request a login link with their email.

## What can instructors see and do?

Instructor access depends on their role:

- **Standard instructor** — sees only their own classes in the Calendar view. Can mark attendance.
- **Lead instructor** — can see other instructors' classes and the wider timetable. Useful for cover planning and coordination.

Instructors do not have access to payment details, reports, or full booking management.

## An instructor says they can't find "Activities → Classes" — only "Calendar" is visible

This is expected. Instructors with limited roles (Standard instructor, External instructor, Receptionist) only see **Activities → Calendar** in the left-hand menu. The **Classes** list under Activities is only available to Owners, Assistants, and Main instructors.

This means that guide steps like "Go to Activities → Classes → select sessions → Bulk edit" cannot be performed by a standard instructor. If an instructor needs to change session times, reschedule sessions, or bulk-edit, an admin or main instructor must do it on their behalf.

If the instructor should have access to the Classes list, change their role to **Main instructor** in **Settings → General → Access**.

## How do I change instructor permissions?

Go to **Settings → General → Access**, select the instructor, and adjust their role. If you want all instructors to see each other's classes (e.g., for a small team that covers for each other), set them as lead instructors.

## How do I add Zooza to a phone as an app?

Zooza works as a web app. To make it behave like a native app on mobile:

1. Open the Zooza URL in the phone's browser (Safari on iPhone, Chrome on Android).
2. Tap the share/menu button.
3. Select **Add to Home Screen**.

This creates an app icon that opens Zooza directly without the browser navigation bar.

## How do I deactivate an instructor's account without losing data?

Do not delete the instructor account. Instead, change their role to **Inactive instructor** in **Settings → General → Access**. This prevents the instructor from logging in but preserves all historical data — their attendance records, session assignments, and instructor reports remain intact.

If you delete the account, all data linked to that instructor is permanently lost and cannot be recovered. Always switch to the Inactive role first. You can find the role selector on the instructor's profile in **Settings → General → Access**.

## A substitute instructor cannot send emails to students on the session they cover — is this by design?

Email and communication access depends on the instructor's role. By default, **external instructors** have very limited permissions — they can mark attendance on sessions they are assigned to (including as a substitute) but cannot send emails or SMS to clients.

If you need a substitute instructor to communicate with students, they must hold at least the **Instructor** role, which grants the right to send emails and SMS to their own clients. Alternatively, the **Main instructor** role provides broader communication access across all clients.

You can adjust roles at any time in **Settings → General → Access**.

## Why can't an instructor send an email from the session or group view?

This is a permissions limitation by role, not a bug.

When an instructor opens a session detail and tries to send a message to attendees, the option is restricted based on their role:

| Role | Can send email/SMS to clients |
|---|---|
| **External instructor** | No |
| **Instructor** | Yes — to clients enrolled in their own classes |
| **Lead instructor** | Yes — to clients enrolled in classes they can see |
| **Manager / Owner** | Yes — unrestricted |

If a lektor (instructor) reports they cannot find the email option on a session or group, check their role in **Settings → General → Access**. The most common fix is upgrading them from **External instructor** to **Instructor**.

**Important:** Role changes apply immediately — the instructor does not need to log out and back in.

> **SK:** Ak lektor hlási, že nemôže odoslať email z termínu alebo skupiny, skontrolujte jeho rolu v **Nastavenia → Tím**. Externý lektor nemá právo posielať správy klientom. Zmeňte rolu na **Lektor** a prístup sa sprístupní okamžite.

## How do instructor rates work, and why do the totals have odd decimals?

A rate is three things, set in **Settings → Other → Instructors rates**: a **Name**, a **Duration
in minutes**, and whether **Rate is fixed**. That last switch is the one that decides
everything about how pay is calculated, and it is the answer to the decimals question.

**Rate is fixed — off (the default).** The amount is a rate *for that duration*, so Zooza
converts it to a per-minute figure and pays the time actually taught. It is exact to the
minute, which is also why it produces decimals: a €20 rate across four sessions can total
**€79.99** rather than €80. Nothing is wrong — it is the rounding of a per-minute rate,
and it will match the real taught time to the cent.

**Rate is fixed — on.** The amount is paid per session, whatever its length. An hour and
two hours both pay the same. Totals stay round.

Which you want is a business decision, not a technical one. Providers who pay by the hour
want it off and should accept the decimals. Providers who pay per lesson — and who do not
top up when a lesson overruns — want it on.

> **Still seeing odd totals after 30 October 2026?** The calculation was rebuilt at the
> end of October to fix exactly this. To pick it up on an existing rate you have to
> re-save it: open the instructor's profile, expand the rate card, click **Save**, then
> recalculate the report. It has to be done once per instructor.

**The amount does not vary with the number of students.** A rate is an amount, a duration
and the fixed flag — there is no per-head multiplier. If you pay per student, work it out
from the instructor report rather than expecting Zooza to calculate it.

Each rate is created once and then given a monetary value per instructor, so the same rate
(say "Group Session") can pay different amounts to different people. You assign it to a
class in the class settings and it applies to every session in that class, including for a
second instructor.

To see what has been earned, go to **Instructors → [instructor] → Instructor report** and
choose a date range.

## Can one instructor take payments while another cannot?

No. **Allow instructors to see financial information** in **Settings → General → Access**
is company-wide: switch it on and every instructor can see client money and add payments;
switch it off and none of them can. There is no per-person and no per-class version of it.

Nor does promoting somebody help. The **main instructor** role does not come with payment
visibility — several providers have tried that route expecting it to, and it does not work
that way.

So the choice is the blunt one: either all your instructors handle money or none do. If
you need one person taking cash at the door, the usual answer is to give that person an
**assistant** or **receptionist** role rather than an instructor one, and accept that they
then see more than just their own class.

> **Tell us if this is wrong for you.** The setting is company-wide because every provider
> we have seen so far does it all-or-nothing. A real case for per-instructor or per-class
> payment access is worth sending to support — that is how the setting would get split.

## An archived class is still appearing in the instructor's report — why?

This is expected behaviour. Archiving a class preserves its full history — the instructor report still shows sessions from the archived class because those sessions happened and the instructor was paid for them.

If you want the archived class to stop appearing in **future** instructor report periods, delete the remaining future sessions before archiving. Past sessions will continue to appear in historical reports and cannot be removed from the log.

## Related

- [Two instructors per class](../guides/two-instructors-per-class.md) — assign a main and assistant instructor to a class
- [User roles](../guides/user-roles.md) — full breakdown of all roles and their permissions
- [Instructor working hours](../setup/instructors-working-hours.md) — configure availability windows per instructor
- [Instructor rate and reward](../setup/instructor-rate-reward.md) — set up compensation rates
- [Instructor substitution](../guides/instructor-substitution.md) — manage cover and substitute instructors
