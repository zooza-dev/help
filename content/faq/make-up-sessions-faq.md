---
title: "Make-up Sessions FAQ"
slug: "make-up-sessions-faq"
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
intercom_id: 13738260
intercom_sync: false
---

# Make-up Sessions FAQ

## How do make-up sessions work?

When a child misses a session and the absence is properly recorded, the system generates a make-up credit on the booking. The parent can then use this credit to book a make-up session in another compatible class (same programme, matching age range) through their Client Profile.

Make-up sessions must be enabled per programme. Go to **Programmes** → select the programme → **Settings** → **Make-up sessions** to configure them.

## What attendance state triggers a make-up credit?

Only the **"Cancelled"** attendance state generates a make-up credit. If a child is marked as **"Did not attend"** (no-show), no make-up credit is created. This is by design — the system distinguishes between a planned absence (cancel in advance) and an unexcused no-show.

If a make-up credit was not generated after a missed session, check whether the attendance state is "Did not attend" instead of "Cancelled". An admin can correct the state in the session's attendance view.

## How does the "extra capacity for make-up sessions" setting work?

There are two levels for this setting:

1. **Global setting** — Go to **Settings** → **Make-up sessions**. The `Extra capacity for replacement hours` value (e.g. 1) applies to every class across all programmes. This means each class allows that many additional spots beyond its normal capacity for make-up bookings.

2. **Per-class setting** — On the class detail page, the make-up sessions tile shows a per-class extra capacity value. You can choose whether this value **replaces** the global setting or **adds to** it.

If the per-class value is 0 and set to "add to global", the global setting applies unchanged. To remove extra capacity from a specific class, set the per-class value to 0 and choose "replace global setting".

## What is the 4-day rule for make-up session availability?

Classes that have not yet started do not appear as make-up options. The system only makes a class available for make-up bookings **4 days before the class's start date**. This prevents make-up students from occupying capacity that should be reserved for full-paying bookings.

If you create a one-off class specifically for make-up sessions, set the class start date close to the session date. Otherwise the session will not appear as a make-up option.

<!-- REVIEW: The 4-day rule was described as a fixed value implemented at franchise request. It may become configurable in the future. -->

## How do cross-company (franchise) make-up bookings work?

Franchise networks can allow make-up bookings across branches operated by different legal entities. When enabled, a parent sees available sessions from all linked branches in their make-up options.

Setting up cross-company replacements has three steps:

1. **Link the companies** — go to **Settings** → **Replacement lessons** → **Cooperate with a company**, enter the other branch's email, and send an invitation. The other branch must approve.
2. **Enable on the programme** — open the programme → **Replacement lessons** → **Edit** → check **Allow replacement lessons from other companies**.
3. **Configure restrictions** — set the conditions under which clients from other branches can book at your sessions.

Cross-company make-up bookings follow the same rules as regular make-up bookings (capacity, 4-day rule, programme match). The restriction settings control **incoming** replacements — they define when clients from another branch can use sessions at your company.

For the full setup walkthrough, admin views, and reporting, see the [Cross-company replacements](../guides/replacement-hours-complete.md#cross-company--franchise-replacements) section in the Replacement Hours guide.

## Can make-up credits carry over to the next billing period?

Yes, depending on your settings. Go to **Settings** → **Make-up sessions** to choose one of three expiration modes:

1. **Credits expire at the end of the class** — credits are valid only within the current class/term.
2. **Credits carry over** — credits transfer to the next billing period automatically.
3. **Credits expire after a set number of days** — you define how many days a credit remains valid.

Options 2 and 3 allow credits to be used across billing periods. This setting can also be overridden per programme.

## How do I delete or expire a make-up credit?

Go to the booking detail page. Scroll to the **Credits** section at the bottom. Click **Show all credits** to see every credit on that booking. Find the make-up credit you want to remove, click the **More** button next to it, and either:

- Change the expiration date to a past date (to let it expire), or
- Click the **Delete** button to remove it entirely.

## Why can't a parent see make-up options in their profile?

Check these common causes:

1. **Attendance state** — The absence must be recorded as "Cancelled", not "Did not attend".
2. **Class has not started** — Make-up options only appear for classes that start within 4 days or have already begun.
3. **No available capacity** — All compatible sessions may be full (including the extra capacity allowance).
4. **Make-up sessions disabled** — Verify that make-up sessions are enabled on the programme. Go to **Programmes** → select the programme → **Settings** → **Make-up sessions**.
5. **Display limit** — The system limits the make-up session list to approximately 200 options. If there are many available sessions, the displayed set may vary between requests and some specific sessions may not always appear.
6. **Cancellation window** — If the parent is looking at a session that starts within the configured cut-off time (e.g. less than 1 hour before the session), the option will no longer be available.

## How does the "sign back up for this session" button work?

When a parent cancels a session, a **"Sign back up for this session"** button appears in their profile next to that session. This allows them to re-enroll on the original session they cancelled from.

If the parent had already booked a make-up session, clicking this button cancels the make-up booking and puts the child back on the original session. The button works automatically when make-up sessions are enabled — there is no separate setting to activate it.

The button only works if there is still available capacity on the original session at the time the parent clicks it. If the session has filled up since they left, the system will inform them that the session is full.

## Can a student re-enroll on the same session they cancelled from?

Yes. The parent can use the **"Sign back up for this session"** button in their profile. If a make-up session was already booked, it is automatically cancelled when the parent re-enrolls on the original session.

## Where is the make-up session waiting list?

When all sessions with available capacity are taken, parents can join a **waiting list** (queue) for specific sessions. When a spot opens up, the system sends a notification to the parent with a link. The parent must click the link to confirm their spot — it is not automatically assigned.

The waiting list is fully automated. You can enable or disable it per programme. Go to **Programmes** → select the programme → **Settings** → **Make-up sessions** and look for the `Make-up sessions waitlist` option.

<!-- REVIEW: Confirm the exact setting name and location — referenced as being in programme make-up session settings. -->

## How do I set a cancellation deadline for sessions?

Go to **Settings** → **Programmes** and enable **Set a limit for cancelling a scheduled session**. You can choose between two limit types:

- **Fixed time** — cut-off is a specific hour on the day before the session.
- **Relative time** — cut-off is a number of hours before the session starts (e.g. 12 hours).

This is a global setting — it applies to all programmes in your account.

## Can clients still cancel after the cancellation deadline?

Yes, if you enable **Allow cancellations after the limit** in **Settings** → **Programmes**. When a client cancels after the deadline:

- The session slot is freed up for others.
- No make-up credit is generated.
- The attendance record shows **Did not attend**.

If this option is disabled, clients cannot cancel at all after the deadline and will see the instructions text you configured.

## What happens with the cancellation limit over weekends?

If you enable **Block cancellations on weekends and holidays**, the cancellation deadline for Monday sessions shifts to **Friday at midnight**. This prevents clients from using the weekend to cancel sessions that would otherwise require a working-day notice.

## Why does a session not appear as a make-up option even though it has capacity?

The most likely reason is the **time restriction for offering a regular make-up session** setting. For example, if this is set to 1 hour, a session starting at 3:00 PM disappears from make-up options after 2:00 PM — even if it still has free spots.

Check the value in **Settings** → **Programmes** → **Time restriction in hours for offering a regular make-up session**.

## What is the difference between a standard make-up session and a custom replacement lesson?

A **standard make-up session** works by filling a vacant spot in another scheduled class. The client picks from sessions that already exist and have available capacity.

A **custom replacement lesson** lets the client propose a specific date and time to their instructor. The instructor checks their availability and approves or declines the request. If approved, a new session is created automatically.

Custom replacement lessons are designed for individual or specialist sessions (piano lessons, personal training, counselling) where signing into someone else's class is not practical.

See [Custom replacement lessons](../guides/custom-replacement-lessons.md) for setup and workflow.

## Can I use custom replacement lessons for group classes?

Yes, but it is unusual. Custom replacement lessons are primarily designed for 1-to-1 or individual sessions where the replacement needs to happen with a specific instructor at a specific time. For group classes, standard make-up sessions (based on vacant spots) are usually more practical.

## Can a client cancel a custom replacement request after submitting it?

Yes. The client can cancel their request at any point before the instructor has confirmed it. Once the instructor approves, the session is created and the client is enrolled — at that point, the normal cancellation rules apply.

## What happens if the instructor declines a custom replacement request?

The instructor must provide a reason for the decline. The client receives an email notification with the reason. The client can then submit a new request with a different date or time.

## Why was a make-up credit not generated after a missed session?

The most common reason is that the child's attendance was set to **"Did not attend"** (no-show) instead of **"Cancelled"**. Only the "Cancelled" state creates a make-up credit.

Other reasons include:

- Make-up sessions are not enabled on the programme.
- The credit was generated but already expired based on your expiration settings.
- The session itself was not properly tracked (e.g. attendance tracking is disabled on the class).

To fix a missing credit, change the attendance state from "Did not attend" to "Cancelled" on the affected session. The system should then generate the make-up credit.
