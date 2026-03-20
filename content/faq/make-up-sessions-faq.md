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

1. **Link the companies** — go to **Settings** → **Make-up session** → **Cooperate with a company**, enter the other branch's email, and send an invitation. The other branch must approve.
2. **Enable on the programme** — open the programme → **Make-up session** → **Edit** → check **Allow make-up session from other companies**.
3. **Configure restrictions** — set the conditions under which clients from other branches can book at your sessions.

Cross-company make-up bookings follow the same rules as regular make-up bookings (capacity, 4-day rule, programme match). The restriction settings control **incoming** replacements — they define when clients from another branch can use sessions at your company.

For the full setup walkthrough, admin views, and reporting, see the [Cross-company replacements](../guides/replacement-hours-complete.md#cross-company--franchise-replacements) section in the Make-up Sessions guide.

## Can make-up credits carry over to the next billing period?

Yes. Go to **Settings** → **Make-up sessions** → **General Settings** and choose one of three expiration modes under **Make-up sessions behavior**:

| Mode | Behavior |
|---|---|
| **Set transferred make-up sessions** | When the class ends, unused credits up to your set limit are carried over to the next period with a new expiration date. Credits beyond the limit are voided. |
| **All make-up sessions expire at the end of the class** | All unused credits are voided when the class ends. |
| **All make-up sessions expire after the preset number of days** | The class end date has no effect — credits expire based only on the number of days set. |

**Additional settings (when using transferred make-up sessions):**

- **Maximum number of transferred make-up sessions between billing periods** — how many credits can be carried into the next period. Set to `0` to disable the carry-over entirely.
- **Number of days to use transferred make-up sessions** — how long after the class ends the transferred credits remain usable.
- **Default expiration of credits (in days)** — applies to all make-up credits from the date the credit is created (default: 90 days).
- **Additional slots in classes** — extra capacity in sessions reserved specifically for make-up bookings (global setting; can be overridden per class).

## How do I delete or expire a make-up credit?

Go to the booking detail page. Scroll to the **Credits** section at the bottom. Click **Show all credits** to see every credit on that booking. Find the make-up credit you want to remove, click the **More** button next to it, and either:

- Change the expiration date to a past date (to let it expire), or
- Click the **Delete** button to remove it entirely.

## A client says make-up sessions are not showing up. Where do I start?

In almost every case this is a settings issue, not a bug. Work through this checklist:

### 1. Check the attendance state

The absence must be recorded as **"Cancelled"**, not **"Did not attend"**. Only "Cancelled" generates a make-up credit. If the state is wrong, fix it in the session's attendance view and the credit will appear.

### 2. Check that make-up sessions are enabled on the programme

Go to **Programmes** → select the programme → **Settings** → **Make-up sessions**. If this is off, no options appear for any client in that programme.

### 3. Understand the display limit

The system shows only the **first few dozen compatible sessions** in the client's make-up list. This is the most common reason a specific session is not visible — it exists and has capacity, but it is not in the displayed set because there are too many options overall.

**Fix:** Reduce the number of sessions offered as make-up options so the right ones appear. You can do this by:

- Narrowing the make-up session offer in programme settings (limit which classes qualify).
- Setting tighter time restrictions (see setting 5 below).
- Setting extra capacity to 0 on classes that should not appear as make-up options.

### 4. Check available capacity

Even if extra capacity is set globally, individual classes can override it. Go to the class detail → **Make-up sessions** tile. Check the per-class extra capacity value and whether it adds to or replaces the global setting.

If both the class is at its normal capacity limit and the extra capacity is 0, no make-up spots are available and the session will not appear.

### 5. Check the time restriction for regular make-up sessions

Go to **Settings** → **Programmes** → **Time restriction in hours for offering a regular make-up session**. If this is set to e.g. 2 hours, any session starting in less than 2 hours is hidden from the make-up list — even if it has free spots.

### 6. Check the 4-day rule

Classes that have not yet started only appear as make-up options **4 days before the class start date**. If a class starts next month, it will not appear in the list today.

### 7. Check the cancellation deadline

If the client is trying to cancel and book a make-up within the configured cut-off window, the option will not be available.

---

## Why can't a parent see make-up options in their profile?

Check these common causes:

1. **Attendance state** — The absence must be recorded as "Cancelled", not "Did not attend".
2. **Display limit** — The system shows only the first few dozen compatible sessions. If there are many options available, some specific sessions may not appear. Narrow the scope in programme settings or reduce extra capacity on irrelevant classes.
3. **No available capacity** — All compatible sessions may be full (including the extra capacity allowance).
4. **Make-up sessions disabled** — Verify that make-up sessions are enabled on the programme. Go to **Programmes** → select the programme → **Settings** → **Make-up sessions**.
5. **Class has not started** — Make-up options only appear for classes that start within 4 days or have already begun.
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

## What is the difference between a standard make-up session and a custom make-up session?

A **standard make-up session** works by filling a vacant spot in another scheduled class. The client picks from sessions that already exist and have available capacity.

A **custom make-up session** lets the client propose a specific date and time to their instructor. The instructor checks their availability and approves or declines the request. If approved, a new session is created automatically.

Custom make-up session are designed for individual or specialist sessions (piano sessions, personal training, counselling) where signing into someone else's class is not practical.

See [Custom make-up session](../guides/custom-replacement-lessons.md) for setup and workflow.

## Can I use custom make-up session for group classes?

Yes, but it is unusual. Custom make-up session are primarily designed for 1-to-1 or individual sessions where the replacement needs to happen with a specific instructor at a specific time. For group classes, standard make-up sessions (based on vacant spots) are usually more practical.

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
