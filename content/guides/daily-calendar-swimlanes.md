---
title: "Daily Calendar — Room Swimlane View"
description: "The daily overview calendar now shows rooms as horizontal swimlanes with a time-based axis, a sticky horizontal scrollbar, and quick session actions — making it easy to see your whole day at a glance."
slug: "daily-calendar-swimlanes"
type: "guides"
product_area: "Calendar"
sub_area: ""
audience: ["admin"]
tags: ["calendar", "session", "daily", "view", "rooms"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-06-04"
related_articles: ["calendar-bulk-actions", "edit-sessions-in-programmes"]
---

# Daily Calendar — Room Swimlane View

The daily overview (`Calendar → Daily`) has been redesigned as a proper calendar view. Rooms now appear as horizontal swimlanes (rows) with the hours of the day across the top, making it far easier to spot scheduling conflicts, gaps, and parallel activity across your spaces.

## What changed

| Before | After |
|---|---|
| Plain data table | Time-based calendar with room swimlanes |
| Horizontal scrollbar hidden at page bottom | Scrollbar always visible — pinned to viewport bottom |
| Date changed by typing | Previous/next day arrows + Today button |
| All filters always visible | Mobile: filters collapse into a filter drawer |

## Reading the swimlane view

The time axis reads like a ruler:
- **Thick vertical lines** mark each full hour.
- **Light dotted lines** mark 15-minute intervals.
- Each session tile is positioned and sized to match its exact start time and duration.

### Overlapping sessions

When two or more sessions occupy the same room at the same time, the room's swimlane grows taller and the sessions stack into sub-lanes — each tile keeps its horizontal position along the time axis.

### Short sessions (≤ 15 minutes)

Very short sessions appear as clipped tiles. Hover over a tile on desktop, or tap it on mobile, to reveal the full session information, attendees, and a link to the event detail.

## Navigating the day

Use the date navigation bar at the top of the calendar:

- **← Previous day** / **Next day →** arrows step the view one day at a time.
- **Today** button jumps directly to today's date.
- Changing the date automatically reloads the sessions for that day.

## Scrolling

The swimlane grid can be scrolled both horizontally (through the day's hours) and vertically (through the rooms). Key scroll behaviours:

- The **room-name column on the left** stays frozen while scrolling horizontally — you always know which row belongs to which room.
- The **time header at the top** stays frozen while scrolling vertically.
- The **horizontal scrollbar is always visible at the bottom of your screen**, even when you're at the top of a very long list of rooms. You do not need to scroll to the bottom of the page to scroll the calendar sideways.

## Filters

**On desktop:** Place, Attendance, and Attendance Type filters are shown inline above the calendar.

**On mobile:** The filter icon (with a badge showing the number of active filters) opens a filter drawer where you can adjust Place, Attendance, and Attendance Type.

Some filters still require you to select a place before the swimlane view renders — the empty state will prompt you if no place has been chosen.

## Clicking sessions

Each session tile is a link:
- Click **the tile** to open the event detail page.
- Click an **attendee row** within the tile to open that client's registration.
- If the tile is clipped (narrow), hover or tap to see all attendees before clicking.
