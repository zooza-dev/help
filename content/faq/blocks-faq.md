---
title: "Blocks (Term Segments) FAQ"
slug: "blocks-faq"
type: "faq"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: []
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-13"
intercom_id: 13738257
intercom_sync: false
---

# Blocks (Term Segments) FAQ

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

Full-programme bookings take priority. To avoid this, disable the "register for the entire programme" option in your programme's online registration settings so clients can only register for individual blocks.

## What happens to attendance records when I change a student's block?

When you change a student's block assignment, attendance records for the previous block are marked as **Hidden** in the system. The attendance data is not deleted, but it is no longer visible in the booking detail and shows only the label "Hidden" instead of the original status (e.g. "Attended").

This makes it difficult to verify how many sessions a student attended before the change. If you need to preserve this information, export or note the attendance data before changing the block.

<!-- REVIEW: Product team may add a feature to retain visible attendance history across block changes. Check for updates. -->

## Why do dynamic tags show wrong dates or times for block-based programmes?

Dynamic tags such as `COURSE_DATE_DAY` and `COURSE_TIME` pull their values from the first session in the class as a whole, not from the client's specific block. If a client is enrolled in a later block (e.g. starting in April instead of January), the confirmation email may display the wrong date or time.

**Workaround:** Replace `COURSE_DATE_DAY` and `COURSE_TIME` with the `ORDER_SUMMARY` tag in your email templates. `ORDER_SUMMARY` includes the correct block-specific details for each booking. You can edit the booking confirmation template at **Communication -> Templates -> Booking done**.

## How do trials interact with blocks?

When trial sessions and blocks are used on the same class, a capacity conflict can occur. A trial booking reserves a spot in the **entire class** because the system cannot determine which block the trial client will ultimately join. Meanwhile, paying clients can register for specific blocks. The system prioritises paying bookings over trials, which may result in temporary over-capacity on individual sessions.

To reduce this issue, configure trial bookings to use **extra capacity** only (in the programme's trial session settings). This ensures trials do not consume spots reserved for paying clients.

<!-- REVIEW: There is currently no way to assign a trial to a specific block. Monitor for future feature updates. -->

## Can I filter bookings by block?

Filtering bookings by block directly in the booking list is not yet fully supported. Block occupancy statistics are available in the class detail view, where you can see how many clients are enrolled in each block.

<!-- REVIEW: Block-based filtering and block column in booking exports were requested in Jan 2026. Check whether these have been shipped. -->

## Why did previously created blocks disappear from the admin view after editing?

This can happen temporarily after blocks are created or modified, particularly when the application is in the process of updating. The blocks typically reappear after a short time or after a browser refresh. If blocks are still missing after refreshing:

1. Open the class detail and check whether the sessions still have block labels assigned.
2. If sessions show no block label, use **bulk edit** on the sessions to reassign them to the correct block.

Note that even when blocks are not visible in the admin view, they may still appear correctly in the public booking form. If the issue persists beyond a few hours, contact support with the class number.
