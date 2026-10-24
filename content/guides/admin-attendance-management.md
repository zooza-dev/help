---
title: "Managing client attendance — admin"
description: "Set or change attendance for any client on any session, read the enrolment states Zooza sets by itself, and work out why a session vanished from a client's record."
slug: "admin-attendance-management"
type: "guides"
product_area: "Calendar"
sub_area: ""
audience: ["admin", "staff"]
tags: ["attendance", "admin", "make-up", "cancelled", "session", "calendar", "booking", "transfer"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-10-24"
related_articles: ["instructor-attendance-management","make-up-sessions-faq","transfer-and-copy-bookings","cancellation-log","matko-replacement-diagnostic"]
---

# Managing client attendance as Admin

Admins and instructors (with full report permission) can set or change attendance for any client on any session — including sessions in the past. There are no restrictions on when or how many times attendance can be updated.

## Two ways to reach attendance

### Via Calendar

Go to **Calendar** and click a session. This is the fastest way to mark a whole class at once, and the screen was rebuilt in October 2026.

![The session screen: status, date, actions, and the tile row showing will attend, will not attend, trial bookings, make-up sessions and available slots](../../assets/images/session-screen-overview.png)

The top of the screen tells you where you are before you touch anything:

- **The counts** — will attend, will not attend, trial bookings, make-up sessions and available slots, with **Details** to expand them.
- **Where this session sits** — *65. session of 198*, with arrows to the session either side. You can work through a term without going back to the calendar.
- **A holiday badge** when the date falls in a school break you have configured.
- **Actions** — Add/Edit substitution, Cancel/Reschedule session, Message the class, and Edit.

### Quick view and Full view

The **Attendance** card has two modes, switched top right.

- **Quick view** — names and the four attendance buttons, nothing else. What you want with a room in front of you.
- **Full view** — adds a column per piece of information: the attendee with their date of birth and age, what they owe with **Add payment**, their attendance, and space for personal feedback.

**Mark all as attended** is at the top of both, and the running count — *Attended 1/9* — sits under it.

> **The payment column follows the instructor financial-visibility setting.** Where instructors are not allowed to see client money, it is not on their register either. See [User roles](user-roles.md#keeping-client-money-off-instructors-screens).

### Putting the register in the order you want

By default the list is in booking order, newest first — which is the one order
nobody calls a name out in. **Sort** at the top of the Attendance card changes it:

| Sort by | Use it for |
|---|---|
| **Newest first** (default), **Oldest first** | Who joined when — useful on a class that is still filling up. |
| **Attendee A→Z**, **Attendee Z→A** | Calling the register. This is the alphabetical order by the child's name. |
| **Client A→Z**, **Client Z→A** | Alphabetical by the parent instead — the right one when you are chasing paperwork rather than marking a room. |
| **Balance: lowest first**, **Balance: highest first** | Who owes the most. Pair it with Full view so the amount is on screen beside the name. |

The order is yours, not the class's: it is how you see the list, and it changes
nothing for anyone else.


### Via Booking

Go to **Bookings**, open a client's booking. Look for the **Attendance** tab or section within the booking detail. This shows the full session-by-session attendance record for that one booking.

![Screenshot — admin attendance management](../../assets/images/admin-attendance-management-02.png)

Use this view when you need to manage or review one specific client's attendance history.

> **If you don't see an Attendance tab in the booking detail**, use the Calendar route instead: go to **Calendar**, click the session, switch to **Full view**, and find the client in the list. This view is always available regardless of how the booking detail is laid out.

## Attendance states

Each session row shows four state buttons:

| State | Meaning |
|---|---|
| **Will attend** | Default state — the client is enrolled and the session is upcoming or not yet marked. |
| **Attended** | The client was present at the session. |
| **Cancelled** | The client cancelled in advance. If make-up sessions are enabled, a **Choose make-up session** button appears. |
| **Did not attend** | The client did not show up and did not cancel. No make-up credit is generated. |

Click any button to set or change the state. The change takes effect immediately. You can change it again at any time, including for past sessions.

![A session register with four attendance buttons per person: will attend, attended, cancelled, did not attend, each highlighting in its own colour](../../assets/images/session-attendance-four-states.png)

> **Watch the middle two.** The order on screen is *Will attend · Attended · Cancelled · Did not attend*, so **Cancelled sits between the green tick and the red cross** and is easy to hit by mistake. It is not a neutral button: it records a planned absence, which on a programme with make-ups issues the client a credit and takes them off this session. If somebody vanished from your register after a stray click, that is almost always what happened — set them back to Attended and delete the credit it created.

### Choosing what Full view shows

The icon beside the Quick view / Full view toggle opens the layout editor.

![The attendance card in layout mode: tiles for attendee, payment, attendance, address, slots, internal note and labels, with a column selector and a drop area](../../assets/images/session-attendance-customise-tiles.png)

Each piece of information is a tile you can move, resize with the column selector, or remove with the bin. Anything you take out goes back to the **Drop widgets here** strip at the bottom and can be dragged in again. Beyond the obvious ones there are **Address**, **Slots**, **Internal note** and **Labels**, and a **Buyer** toggle for showing the paying parent rather than the attending child.

**Save** keeps your layout, **Reset to default** puts it back. It is worth a minute: a swimming school wants the address off and the internal note up, a music school wants the opposite.

## How a client gets onto a session in the first place

Most "the client disappeared from attendance" questions are really about this, so it is worth knowing before you go looking for a bug.

1. **While the class runs**, the client is held against every session in it — on the assumption they will come. This is an expectation, not an attendance record.
2. **At midnight the day before a session**, Zooza enrols them on it for real, unless they have already cancelled.
3. **From then on the session carries a record** — will attend, attended, cancelled or did not attend — and that record is what you see and change.

So a session in the far future and a session tomorrow are not in the same state, even though both show the client. A cancellation, or a make-up credit being spent, changes which sessions carry a record and which do not.


## When a session is set to Cancelled

Setting a session to **Cancelled** unlocks additional options:

- **Choose make-up session** — opens a list of upcoming sessions the client can be logged in to as a make-up.
- **Go to Make-up Session** — jumps directly to the make-up session already selected (if one was chosen).
- **Reason for cancelling** — select from available reasons (or leave as "Not specified"). This is for internal tracking.
- **Personal feedback (visible to parent)** — leave a note that the client can see in their profile.

![Screenshot — admin attendance management](../../assets/images/admin-attendance-management-03.png)

![Screenshot — admin attendance management](../../assets/images/admin-attendance-management-07.png)

## Choosing a make-up session

After clicking **Choose make-up session**, a list of upcoming sessions appears — filtered to sessions with available capacity from the same programme (or linked programmes, if cross-company make-ups are configured).

![Screenshot — admin attendance management](../../assets/images/admin-attendance-management-04.png)

You can filter by **Date**, **Programme**, or **Instructor**. Each row shows the date, time, class, location, instructor, and number of free slots. Click **Log in** to assign the make-up.

Once confirmed, the original session shows the cancelled status with a link to the make-up, and the make-up session shows the client as logged in.

## Book a session (from the Attendance tab)

In the booking's **Attendance** tab, the **Book a session** button at the top lets you add any upcoming session from the class to the client's attendance record. This is used when you want to manually enrol the client into a specific session — for example, a make-up or an extra session — without going through the session picker.
![Screenshot — admin attendance management](../../assets/images/admin-attendance-management-05.png)
![Screenshot — admin attendance management](../../assets/images/admin-attendance-management-06.png)
## Attendance after transferring a student to a different class

When you move a student from one class to another (via **Transfer** or **Copy**), their historical attendance does not move with them. Here is what happens:

| What | Where it goes |
|---|---|
| Attendance records from the **original class** | Stay on the **original booking** — linked to the original class |
| Attendance in the **new class** | Starts fresh from the date of transfer — no history |
| Make-up credits earned in the original class | Remain on the original booking; may or may not be usable in the new class depending on programme settings |

### What "Transferred" means on a session

After you move a client between classes, the session detail in the **new** class may list them under **Transferred** rather than with everyone else.

This is cosmetic. It records that the client was not in the group from the start — nothing about their booking, payment or attendance is different because of it. It does not need fixing and it does not go away.

### Why the client no longer shows on some sessions in the old class

In the class they left, the client stays only on the sessions where they have an **attendance record**. Sessions with no record are hidden automatically, so the old class stops listing them for dates they were never really going to attend.

That is why a client can look as though they vanished from a class mid-term: they did not, the sessions without a record are simply not shown.

**To take a client off a session they should not be on**, hide their attendance record for it. The session then drops out of their record the same way.

### Finding a session that is hidden, and putting it back

A hidden record is not deleted — it is still on the booking, just not in the list you are looking at. The **Attendance** tab shows only the four live states by default: will attend, attended, cancelled and did not attend. Anything else — a record that was deleted or ignored, or a place on a waiting list — is left out.

To see them:

1. Open the booking and go to the **Attendance** tab.
2. Use the **Attendance type** filter above the list. Every state that actually has records on this booking appears as an option, with the number of records in brackets.
3. Pick the state you are missing. Those sessions appear in the list, and you can put the record back from there.

> **Read the counter next to the filter.** It shows how many records are being listed out of how many exist on the booking — `18/24` means six are there and not being shown. If the two numbers match, nothing is hidden and the session you are looking for was never on this booking.

The filter only appears when the booking has records in more than one state, so on a straightforward booking you will not see it at all.


**How to find the original attendance after a transfer:**

1. Go to **Bookings** and search for the client.
2. Look for the **original (closed or cancelled) booking** — there may be two bookings for the same client: the old one and the new one.
3. Open the original booking and go to the **Attendance** tab to see the full session history.

> The attendance records are not deleted — they are just on a different booking. If you only look at the new booking, you will see a fresh start.

**Year-end attendance across multiple classes:**

If a student changed classes mid-year, there is no single view that combines their attendance from both classes. You need to check each booking separately and add up the counts manually. This is a current limitation — there is no built-in cross-class attendance report for a single student.

---

## Related

- [Attendance management for instructors](instructor-attendance-management.md) — instructor-specific dashboard and calendar views.
- [Make-up session — complete guide](replacement-hours-complete.md) — how make-up credits are earned and configured.
- [King of a class](king-of-a-group.md) — delegating attendance management to one client.
- [Make-up sessions FAQ](../faq/make-up-sessions-faq.md)
