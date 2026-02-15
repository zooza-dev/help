---
title: "Replacement Hours FAQ"
slug: "replacement-hours-faq"
type: "faq"
product_area: "Calendar"
sub_area: ""
audience: ["admin"]
tags: []
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-13"
---

# Replacement Hours FAQ

## How do replacement hours work?

When a child misses a session and the absence is properly recorded, the system generates a replacement credit on the registration. The parent can then use this credit to book a make-up session in another compatible group (same programme, matching age range) through their Parent Portal profile.

Replacement hours must be enabled per programme. Go to **Programmes** → select the programme → **Settings** → **Replacement hours** to configure them.

## What attendance state triggers a replacement credit?

Only the **"Unsubscribed"** (excused/cancelled) state generates a replacement credit. If a child is marked as **"Did not attend"** (no-show), no replacement credit is created. This is by design — the system distinguishes between a planned absence (unsubscribed in advance) and an unexcused no-show.

If a replacement was not generated after a missed session, check whether the attendance state is "Did not attend" instead of "Unsubscribed". An admin can correct the state in the session's attendance view.

## How does the "extra capacity for replacements" setting work?

There are two levels for this setting:

1. **Global setting** — Go to **Settings** → **Replacement hours**. The `Extra capacity for replacement hours` value (e.g. 1) applies to every group across all programmes. This means each group allows that many additional spots beyond its normal capacity for replacement bookings.

2. **Per-group setting** — On the group detail page, the replacement hours tile shows a per-group extra capacity value. You can choose whether this value **replaces** the global setting or **adds to** it.

If the per-group value is 0 and set to "add to global", the global setting applies unchanged. To remove extra capacity from a specific group, set the per-group value to 0 and choose "replace global setting".

## What is the 4-day rule for replacement availability?

Groups that have not yet started do not appear as replacement options. The system only makes a group available for replacement bookings **4 days before the group's start date**. This prevents replacement students from occupying capacity that should be reserved for full-paying registrations.

If you create a one-off group specifically for make-up sessions, set the group start date close to the session date. Otherwise the session will not appear as a replacement option.

<!-- REVIEW: The 4-day rule was described as a fixed value implemented at franchise request. It may become configurable in the future. -->

## How do cross-company (franchise) replacements work?

Franchise networks can allow replacement bookings across branches operated by different legal entities. When enabled, a parent sees available sessions from other branches in the same franchise in their replacement options.

Cross-company replacements follow the same rules as regular replacements (capacity, 4-day rule, programme match). If replacements between branches stop working, check that:

- The franchise linking is still active between the companies.
- The rules (such as the 4-day rule) are applied consistently across branches.
- The target groups have available capacity.

Contact Zooza support if cross-company replacements were previously working but have stopped — the configuration may need to be re-verified.

## Can replacement credits carry over to the next billing period?

Yes, depending on your settings. Go to **Settings** → **Replacement hours** to choose one of three expiration modes:

1. **Credits expire at the end of the group** — credits are valid only within the current group/term.
2. **Credits carry over** — credits transfer to the next billing period automatically.
3. **Credits expire after a set number of days** — you define how many days a credit remains valid.

Options 2 and 3 allow credits to be used across billing periods. This setting can also be overridden per programme.

## How do I delete or expire a replacement credit?

Go to the registration detail page. Scroll to the **Credits** section at the bottom. Click **Show all credits** to see every credit on that registration. Find the replacement credit you want to remove, click the **More** button next to it, and either:

- Change the expiration date to a past date (to let it expire), or
- Click the **Delete** button to remove it entirely.

## Why can't a parent see replacement options in their profile?

Check these common causes:

1. **Attendance state** — The absence must be recorded as "Unsubscribed", not "Did not attend".
2. **Group has not started** — Replacement options only appear for groups that start within 4 days or have already begun.
3. **No available capacity** — All compatible sessions may be full (including the extra capacity allowance).
4. **Replacement hours disabled** — Verify that replacements are enabled on the programme. Go to **Programmes** → select the programme → **Settings** → **Replacement hours**.
5. **Display limit** — The system limits the replacement list to approximately 200 options. If there are many available sessions, the displayed set may vary between requests and some specific sessions may not always appear.
6. **Cancellation window** — If the parent is looking at a session that starts within the configured cut-off time (e.g. less than 1 hour before the session), the option will no longer be available.

## How does the "sign back up for this session" button work?

When a parent unsubscribes from a session, a **"Sign back up for this session"** button appears in their profile next to that session. This allows them to re-enroll on the original session they cancelled from.

If the parent had already booked a replacement for that session, clicking this button cancels the replacement and puts the child back on the original session. The button works automatically when replacement hours are enabled — there is no separate setting to activate it.

The button only works if there is still available capacity on the original session at the time the parent clicks it. If the session has filled up since they left, the system will inform them that the session is full.

## Can a student re-enroll on the same session they cancelled from?

Yes. The parent can use the **"Sign back up for this session"** button in their profile. If a replacement was already booked, it is automatically cancelled when the parent re-enrolls on the original session.

## Where is the replacement-hour waiting list?

When all sessions with available capacity are taken, parents can join a **waiting list** (queue) for specific sessions. When a spot opens up, the system sends a notification to the parent with a link. The parent must click the link to confirm their spot — it is not automatically assigned.

The waiting list is fully automated. You can enable or disable it per programme. Go to **Programmes** → select the programme → **Settings** → **Replacement hours** and look for the `Make-up sessions waitlist` option.

<!-- REVIEW: Confirm the exact setting name and location — referenced as being in programme replacement settings. -->

## Why was a replacement not generated after a missed session?

The most common reason is that the child's attendance was set to **"Did not attend"** (no-show) instead of **"Unsubscribed"** (excused). Only the "Unsubscribed" state creates a replacement credit.

Other reasons include:

- Replacement hours are not enabled on the programme.
- The credit was generated but already expired based on your expiration settings.
- The session itself was not properly tracked (e.g. attendance tracking is disabled on the group).

To fix a missing credit, change the attendance state from "Did not attend" to "Unsubscribed" on the affected session. The system should then generate the replacement credit.
