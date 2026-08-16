---
title: "Two classes in one room — shared capacity"
description: "When two classes run in the same room at the same time, glue them into a shared session so the room's real capacity is respected and it never double-books."
slug: "shared-room-gluing"
type: "guides"
product_area: "Classes"
sub_area: ""
audience: ["admin"]
tags: ["shared-room", "capacity", "gluing", "attendance", "venue", "priority-registration", "delayed-start"]
related_articles: ["capacity-and-extra-capacity", "priority-registration", "delayed-start-registration", "calendar"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: true
last_converted: "2026-08-16"
---

# Two classes in one room — shared capacity

Some schools run more than one class in the same room at the same time. The usual case is splitting returning students from newcomers: one class for existing students who booked the whole term, another for people dropping in, both in the same hall on the same Monday evening.

Zooza normally treats each class's capacity separately, which is wrong here — two classes of ten in a room that holds ten will let you book twenty people into ten places.

**Gluing** ties those sessions together so the room's real capacity is what counts.

## What gluing does

Sessions that happen **in the same place at the same time** are joined into one shared session. Zooza works this out itself, per date, and it survives you regenerating sessions — there is no list of links to maintain.

Once glued:

- The **room's capacity** applies across all the classes in it, not each class separately.
- The **attendance register** shows everyone in the room, with each person tagged by the class they belong to.
- **Availability is calculated per date**, because the two kinds of booking do not occupy seats the same way.

## Setting it up

You create a **glue set** — the classes that may share a room — and membership in that set is the opt-in. A class not in the set is never glued.

1. Create a glue set and give it a name.
2. Add the classes that share the room.
3. Optionally narrow the match with two conditions:
   - **Same instructor** — only glue when it is the same person. Uses the class's original instructor, so booking a substitute does not un-glue the session.
   - **Same date** — only glue sessions falling on the same date.
4. Save.

**Same place and overlapping time are always required** and are not optional switches. Only genuinely concurrent, co-located sessions ever glue — you cannot glue two classes that are in different rooms or at different times.

There is no session-by-session builder. You say which classes may share a room; Zooza matches the individual dates.

## Reviewing what actually glued

The glued-sessions view shows which sessions joined into which shared session, grouped by date. It is read-only on purpose — it reflects what *is* glued rather than letting you hand-pick, so it cannot drift from reality.

Each glued session shows its **effective capacity**, taken from its own room, and you can override that for a single date when needed — a shared session in a smaller room for one week, say.

## Why the free places look lower than the class capacity

This is the thing to understand before you go looking for a bug.

The two kinds of booking hold seats differently:

- A client booked for **the whole term** holds a seat on **every** glued date. They are coming each week, so their place is reserved each week.
- A client booking a **single session** holds a seat on **that one date** only.

So a room with ten places and six whole-term students has four places on every date — and those four are the only ones drop-ins can take. The class itself may say capacity ten; the shared session says four.

The per-date view makes this explicit, showing the room capacity alongside what is actually free on each date. **Read the per-date number, not the class capacity**, when you are deciding whether someone fits.

## How it interacts with other settings

- **[Priority registration](priority-registration.md)** — a returning-student class can open before the newcomer class in the same room. Gluing is what stops the second class from selling places the first one is holding.
- **[Delayed start](delayed-start-registration.md)** — when a shared room is full now but frees up later, a delayed start is offered against the *shared* capacity, not the individual class's.
- **[Extra capacity](capacity-and-extra-capacity.md)** — make-up and trial places also draw on the shared pool once sessions are glued.

## Troubleshooting

**Two classes are in the same room but did not glue.** Check that both are in the glue set, that the sessions genuinely overlap in time, and that the venue is the same record on both — two venues with the same name are two different places.

**A substitute instructor un-glued a session.** It should not. Matching uses the class's original instructor, so a substitution does not break the glue. If it did, check whether the instructor was changed on the class rather than assigned as a substitute for that session.

**The class shows free places but a booking is refused.** The class capacity is not the limit here — the shared session is. Open the per-date availability for that date.
