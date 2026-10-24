---
title: "Blocks (Term Segments) FAQ"
description: "Blocks let you divide the sessions within a class into smaller logical units. Common use cases:"
slug: "blocks-faq"
type: "faq"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: ["attendance", "block", "booking", "class", "client", "communication", "import", "location", "onboarding", "payment", "programme", "role", "session", "trial"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-10-24"
related_articles: ["blocks-configuration","blocks-creation","trial-sessions","price-and-payment-setup"]
---

# Blocks (Sessions Segments) FAQ

## What are blocks and when should I use them?

Blocks let you divide the sessions within a class into smaller logical units. Common use cases:

- **Booking by interest** -- the client picks a specific block (e.g. certain dates or a particular month) during booking instead of enrolling for the full programme.
- **Time-period billing** -- split a long programme (e.g. a full school year) into semesters, quarters, or camps and issue payments separately per block.

Blocks are created when you add sessions to a class. You choose whether to create a new block or assign sessions to an existing one. For step-by-step setup, see the [Blocks creation guide](../guides/blocks-creation.md).

## Can I set capacity limits per block independently from the class?

Block capacity inherits from the class capacity. If your class capacity is 12, each block can hold up to 12 bookings. However, clients who register for the **entire programme** occupy a spot in every block. This can lead to a block exceeding its intended capacity. For example:

- A class has capacity 12 and two blocks.
- 11 clients register for the entire programme and 1 client registers for Block 1 only.
- A 12th client registers for the entire programme -- Block 1 now has 13 occupied spots.

Full-programme bookings take priority. To avoid this, disable the "enrol for the entire class period" option in your programme's online registration settings so clients can only register for individual blocks.

## What happens to attendance records when I change a student's block?

When you change a student's block assignment, attendance records for the previous block are marked as **Hidden** in the system. The attendance data is not deleted, but it is no longer visible in the booking detail and shows only the label "Hidden" instead of the original status (e.g. "Attended").

This makes it difficult to verify how many sessions a student attended before the change. If you need to preserve this information, export or note the attendance data before changing the block.

<!-- REVIEW: Product team may add a feature to retain visible attendance history across block changes. Check for updates. -->

## Why do dynamic tags show wrong dates or times for block-based programmes?

Dynamic tags such as `COURSE_DATE_DAY` and `COURSE_TIME` pull their values from the first session in the class as a whole, not from the client's specific block. If a client is enrolled in a later block (e.g. starting in April instead of January), the confirmation email may display the wrong date or time.

**Workaround:** Replace `COURSE_DATE_DAY` and `COURSE_TIME` with the `ORDER_SUMMARY` tag in your email templates. `ORDER_SUMMARY` includes the correct block-specific details for each booking. You can edit the booking confirmation template at **Communication -> Templates -> Confirmation of booking**.

## Can I offer trials on some blocks but not others?

Yes. Open the block and you will find **Offer trial lessons for this block** directly
under **Allow online booking**. Set it to No and that block's dates stop appearing as
bookable trial dates.

**The two toggles are independent.** A block can be open for normal registration and
closed for trials, or the other way round — trials only, registration closed.
Switching one does not touch the other. This is what lets you run, say, blocks A and D
for registration while offering B and C as trial dates.

Three things worth knowing:

- **The class-level trial setting is still the master switch.** If the programme does
  not offer trials at all, no block-level toggle brings them back. The block toggle
  narrows the offer within a programme that already has trials on.
- **A new block inherits the class's trial setting**, so you only touch it when you
  want that block to differ.
- **Nothing changed for existing blocks.** When this shipped, every block already in
  place took on whatever its class was doing, so no setup silently changed behaviour.

### A date that sits in two blocks

One session can belong to two blocks at once. If the blocks disagree, **the permissive
one wins**: the session stays bookable as a trial if *any* block it belongs to has
trials on. It drops out only when it belongs to blocks and *none* of them allow trials.

A session that belongs to no block at all is unaffected and stays trial-eligible.
## Why the class looked overbooked, and what changed in October 2026

A class with blocks has never had one meaningful capacity figure. A class set to 10 with two blocks can legitimately hold twenty bookings — ten in each — so a class-level number of 10 beside 18 bookings looks like an error and is not one.

Two changes on 20 October make this readable:

- **The classes list now shows capacity per block** rather than one class-level figure that was never representative.
- **The bookings tile lists the blocks a client is enrolled in**, instead of the class start and end dates. For anyone selling by block that is the useful fact — which days this family actually comes.

If you have been mentally dividing the class number by the number of blocks, you can stop.

## My days do not have the same number of sessions — Tuesdays 35, Saturdays 34

Price the blocks separately. A class running three days a week does not have one session count, so a single class-level price charges the Saturday people for a session that does not exist.

Make each day its own block. On the block, under **Price and payment**:

| Field | What it does |
|---|---|
| **Price per session (optional)** | Overrides the programme's unit price for this block only. Leave it at 0 to use the programme's. |
| **Registration fee (optional)** | Same idea for the joining fee. |

Both fields show you what the programme currently charges underneath — *"Unit price on the programme is: £10.00"* — so you can see what you are overriding before you type.

The same card carries **Allow online booking** and **Offer trial lessons for this block**, which are per block rather than per class. A block you are not selling yet can be switched off without touching the others.

> **Do not try to fix this with the class price and a discount.** The class figure cannot be right for three different session counts at once, and anything you subtract on top has to be recalculated every time a date moves.

## Charging less when somebody books more than one block

Separate from the per-block price, and the thing to reach for when a family takes two days a week rather than one.

On a **membership** payment template, the **Block pricing** button opens *Price per number of blocks*. You set the membership price for **each number of blocks a customer selects**:

- **1 block** — one price
- **2 blocks** — another price, usually less than double

**Leave a row at 0 and that count is charged the full price.** The template tells you how many you have configured — *"0 of 2 set"* — so you can see at a glance whether anything is actually overridden.

This is how you give a multi-day discount without creating a second programme or a discount code. A parent picking Tuesday alone pays the single-block price; the same parent adding Saturday pays whatever you set for two, automatically.

> It sits on the payment template, not on the class, so one template can carry the pricing for every class that uses it.

## How do trials and blocks share capacity?

Separate from who can book: a trial booking reserves a spot in the **entire class**,
because the system does not know which block the trial client will eventually join.
Paying clients enrol into specific blocks. Zooza prioritises the paying booking, which
can put an individual session temporarily over capacity.

Configure trials to use **extra capacity** only, in the programme's trial settings —
then trials never consume seats reserved for paying clients.

## Can I filter bookings by block?

Yes, on the bookings list — but read the result carefully, because **it shows only the
people who chose that block**.

Whole-course bookings are not in it. Someone registered for the entire class is enrolled
in every session rather than in any one block, so a block filter has nothing to match them
on. Filter a class by its Tuesday block and eleven block bookings appear while the
full-year children do not — and that is the filter working, not failing.

The two are genuinely different modes of registration, priced by different rules: blocks
carry their own price and discounts, a whole-course booking is calculated as one. No
single filter spans both.

**If you need one list of everyone attending on a given day**, work from the session or
the class rather than the block — the attendance for a session includes both kinds of
booking, because both kinds of client are in the room.

The booking export still does not include a block column. To check one client, open the
booking and look at the **Class** tile, which shows their current block; for numbers per
block, the class detail view has block occupancy.

## Why did previously created blocks disappear from the admin view after editing?

This can happen temporarily after blocks are created or modified, particularly when the application is in the process of updating. The blocks typically reappear after a short time or after a browser refresh. If blocks are still missing after refreshing:

1. Open the class detail and check whether the sessions still have block labels assigned.
2. If sessions show no block label, use **bulk edit** on the sessions to reassign them to the correct block.

Note that even when blocks are not visible in the admin view, they may still appear correctly in the public booking form. If the issue persists beyond a few hours, contact support with the class number.

## Can I restrict clients to select only one block (exclusive block selection)?

No. Zooza does not currently support exclusive block selection — there is no setting that prevents a client from enrolling in more than one block within the same class.

If you need clients to choose exactly one block, the recommended approach is:

1. Create a separate class (or even a separate programme) for each block option.
2. Clients enrol in one class, which corresponds to one block.
3. This gives full capacity control and prevents multi-block enrolment by design.

This is more setup work upfront but avoids the complexity of enforcing a single-block rule in the booking form.
