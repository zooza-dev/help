---
title: "Camps — Day Camps, Week Camps, Holiday Programmes"
description: "A weekly class runs indefinitely or for a term — clients enrol and attend every week."
slug: "camps"
type: "business-model"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: ["business-model", "camps", "summer-camp", "holiday", "one-off", "children", "week-long"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-04-09"
---

# Camps — Day Camps, Week Camps, Holiday Programmes

## This guide is for you if

- You run short intensive programmes — day camps, week camps, holiday workshops
- Each camp is a standalone event: it has a defined start and end, and clients book for the full duration
- You run multiple camps across a season (e.g. one week per school holiday period)
- You may run different themed camps at the same time or across different locations
- Examples: summer dance camps, sports day camps, language holiday intensives, STEM holiday programmes, multi-activity holiday clubs

---

## How camps differ from regular courses

A weekly class runs indefinitely or for a term — clients enrol and attend every week. A camp is a self-contained block with a fixed start and end. The client buys access to that block, not a recurring commitment.

In Zooza, each camp week (or camp theme) is a **Class** under a shared **Programme**. The Programme holds your pricing and settings. Each Class is one specific camp — its own dates, location, instructor, and capacity.

This means you set up the Programme once, then create a new Class for every camp you run. Summer 2026 Week 1 is one Class. Summer 2026 Week 2 is another. Same Programme, different Classes.

---

## Recommended setup

### 1. Create the Programme

Go to **Programmes → New Programme**.

- **Programme type:** *Booking for the full programme duration* — clients enrol for the whole camp, not individual days
- **Target audience:** *Group Classes*
- **For children:** tick Yes if applicable

Name the Programme after the camp brand — e.g. "Summer Dance Camp" or "Holiday Sports Club". This is what clients see on the booking form.

**Registration fee** — most camps do not charge a separate enrolment fee on top of the camp price. If you do, set it here. Otherwise leave it at 0.

**Make-up lessons** — disable these for camps. A missed day in a camp week cannot be made up in the same way as a missed weekly class. Turn make-up settings off in Programme settings.

### 2. Set the price

Most camps use a simple **one-off payment** — the client pays the full camp price at booking. No instalments, no recurring charges.

Under **How do you want to collect payments?** select *One-off payment* and set the camp price.

If you want to offer an early-bird discount or sibling discount, set those up separately under Loyalty or as discount codes. See [Discount codes](../guides/discount-code.md) and [Sibling discount](../guides/loyalty-sibling-discount.md).

**Deposit + balance (recommended for higher-priced camps)**
If your camp costs enough that parents hesitate to pay the full amount upfront, a deposit model works well: collect a small deposit at booking to secure the place, then charge the remaining balance closer to the camp date.

Set this up using *In scheduled payments → Term payment* with a payment template that has two payments:
1. First payment: the deposit amount — charged immediately at booking
2. Second payment: the remaining balance — charged on a date you set (e.g. 2 weeks before the camp starts)

Zooza sends automatic payment reminders for the second payment so you do not need to chase parents manually. Make sure the reminder schedule is configured in the payment template before you publish.

See [Payment templates](../guides/payment-templates-creation.md).

### 3. Create a Class for each camp

Each specific camp — a particular week, theme, or location — is a Class under the Programme.

Go to the Programme → **New Class** and fill in:
- **Name:** if the theme changes week to week, name it (e.g. "Week 1 — Space Theme"). If all weeks are identical, leave blank — the class will use the Programme name and distinguish itself by dates.
- **Location**
- **Instructor**
- **Capacity**

To create your second and third camp quickly, use **Copy** on the first Class. The copy inherits all settings — you only adjust the dates, location, and instructor.

### 4. Add sessions

For a Monday–Friday day camp, add 5 sessions per Class — one per day.

Go to Class → Sessions → Add sessions:
- Set the **start date** (Monday of camp week)
- Set the **time** and **duration** (e.g. 8:00, 480 minutes for an 8-hour day)
- Set **repeat** to 5 (Mon–Fri)
- If the exact start and end time does not matter (e.g. parents just need to know the date, not the hour), mark the session as **All day** — it shows on the calendar without a specific time slot

Zooza generates all 5 sessions. Review and confirm.

**Attendance tracking** — for most camps you do not need to record attendance session by session. Camps are typically an all-or-nothing commitment: the child is there for the week. You can leave attendance tracking disabled, or simply not mark it. If you do need to track daily attendance (e.g. for safeguarding or billing purposes), the instructor can mark each day from the instructor view.

For detailed session creation options see [Summer camps creation](../guides/summer-camps-creation.md).

### 5. Collect extra information at booking

Camps usually need more data than a regular class — allergies, emergency contacts, t-shirt size, swimming ability. Add these as **extra fields** in Programme settings → Additional fields.

These fields appear on the booking form and are stored on each booking record. You can export them to a spreadsheet before the camp starts.

---

## Running multiple camps in parallel

If you run two different camps at the same time (e.g. a dance camp and a sports camp), create a separate **Programme** for each. They have different prices, different settings, and different registration forms.

If you run the same camp at two different locations simultaneously, those are two **Classes** under the same Programme — same price and settings, different venue and instructor.

---

## Selling out and waiting lists

Set the **capacity** on each Class. When a camp is full, Zooza stops accepting bookings automatically.

If you want to collect interest after a camp sells out, you can keep the Class visible but switch it to lead collection mode — clients register their interest and you contact them if a space opens. See [Lead collection](../guides/lead-collection.md).

---

## Re-using last year's camp

At the start of a new season, copy the entire Programme or individual Classes from the previous year. Update the dates and prices — everything else carries over. You do not need to rebuild from scratch.

---

## What Zooza does not support (for this model)

| Limitation | Workaround |
|---|---|
| Booking individual days within a camp week (e.g. Monday and Wednesday only) | Use Blocks to create day-specific access options within one Class. See [Blocks configuration](../guides/blocks-configuration.md) |
| Automatically applying an early-bird price after a deadline | Switch the price manually or use a time-limited discount code |
| Combining a camp with a weekly class in a single booking | These are separate bookings — the client books the camp and the class independently |

---

## Common mistakes

- **Creating a new Programme for every single camp week** — one Programme per camp type, one Class per week. Not one Programme per week. Your settings would need updating every time.
- **Leaving make-up lessons enabled** — make-up logic does not apply to camps. A child who misses Tuesday of camp week cannot claim a make-up session the following month. Disable it.
- **Not setting capacity** — without a capacity limit, Zooza accepts unlimited bookings. Always set the capacity before you publish.
- **Forgetting extra fields** — you find out two days before the camp that you do not have allergy information for half the children. Set up additional fields before you open registrations.
- **Sending parents the Programme link instead of the Class link** — if you have multiple camp weeks running, the Programme link shows all of them. Send parents the specific Class link for the week you are promoting.
