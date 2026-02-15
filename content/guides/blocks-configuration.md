---
title: "Blocks Configuration and Management"
slug: "blocks-configuration"
type: "guides"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: ["blocks"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: true
last_converted: "2026-02-13"
---

# Blocks Configuration and Management

This guide covers the configuration, capacity behaviour, and known interactions of blocks in Zooza. For step-by-step instructions on creating blocks and setting up pricing, see the [Blocks creation guide](blocks-creation.md). For quick answers, see the [Blocks FAQ](../faq/blocks-faq.md).

## What are blocks

Blocks let you divide the sessions within a class into smaller logical units. Instead of treating all sessions in a class as a single enrolment period, you split them into named segments that clients can register for individually or as a whole.

## Two main use cases

### Booking by interest

Clients pick one or more blocks during registration based on preference -- for example, a specific month, a set of dates on selected days, or a particular accommodation option at a camp. Each block represents a distinct offering within the same class.

Typical examples:

- Dance school with Monday and Wednesday blocks in the same class, where clients choose their preferred day.
- Summer camp with weekly blocks (Week 1, Week 2, etc.), where families pick which weeks to attend.
- Training programme with beginner, intermediate, and advanced blocks running in parallel under one instructor.

### Time-period billing

A long-running programme (such as a full school year) is split into billing periods -- semesters, quarters, or trimesters. Clients register for the entire programme but receive separate payment requests per block. In this scenario, blocks may not be visible to clients during registration; they serve as an internal administrative tool.

## Setting up blocks on a class

Blocks are created when you add sessions to a class. During session creation, you choose whether to assign sessions to a new block or to an existing one. For the full creation procedure, see the [Blocks creation guide](blocks-creation.md).

After creating blocks, configure the following settings.

### Enable online registration per block

Blocks are not automatically visible in the booking form. To allow clients to register for a specific block:

1. Go to the class detail.
2. Open the **Price and Payment** tile.
3. Click on the block you want to make public.
4. Check **Enable online registration**.
5. Click **Save**.

Repeat for each block you want clients to see. Leave blocks unchecked if they are for internal use only (e.g. billing-period splits where clients register for the full programme).

### Set pricing per block

Each block can have its own price. In the **Price and Payment** tile:

1. Open the block.
2. Choose whether the price is calculated from the unit price (based on number of sessions) or is a fixed amount for the entire block.
3. Optionally set a discount (absolute or percentage). The discount applies only to the specific block, not to the class as a whole.
4. Below the list of blocks, configure the **Discount** and **Block Discount Multiplier** fields to control when the discount is active.

### Assign a payment template

For block-based billing, use the **Periodic Prepayment** template with a payment frequency of **By Block**. This creates a payment request before each block starts. See [Payment templates creation](payment-templates-creation.md) for detailed instructions.

If blocks are only an organizational division (e.g. parallel running classes at the same time), a standard payment frequency (monthly, quarterly, one-time) is sufficient.

### Attach products to specific blocks

You can offer different products in different blocks:

1. In the class detail, click **Change** in the **Products** tile.
2. Add the desired products, then click **Setup** on each product.
3. Enable the product for the booking form.
4. Select which blocks should offer the product, then click **Save**.

## Capacity management with blocks

Block capacity inherits from the class capacity. If a class has capacity 12 and two blocks, each block can hold up to 12 clients.

However, clients who register for the **entire programme** occupy a spot in every block. This can push individual blocks over the intended capacity.

**Example:**

- Class capacity: 12, with Block A and Block B.
- 11 clients register for the entire programme (occupying spots in both blocks).
- 1 client registers for Block A only.
- A 12th client registers for the entire programme.
- Block A now has 13 occupied spots (11 full-programme + 1 block-only + 1 new full-programme).

The system prioritises full-programme (paying) registrations over block-only ones.

### How to prevent over-capacity on blocks

Disable the "register for the entire programme" option in your programme's online registration settings. When only block-level registration is allowed, the class capacity applies independently to each block.

### Capacity display in the booking form

The registration form may display capacity based on the class as a whole rather than per block. This can confuse clients -- for example, showing "3/12" when those 3 clients are spread across different blocks. A technical update was deployed in early 2026 so that when blocks are configured, the booking form and calendar tile display per-block capacity instead of group-wide capacity.

<!-- REVIEW: Confirm that the per-block capacity display fix (deployed ~Feb 2026) is stable and applies to all widget types (calendar, schedule, registration form). -->

## How blocks interact with other features

### Trials

When trial sessions and blocks are used on the same class, a capacity conflict can occur. A trial booking reserves a spot in the **entire class** because the system cannot determine which block the trial client will ultimately join. Meanwhile, paying clients register for specific blocks.

In practice this means:

1. Trial bookings may temporarily fill session capacity.
2. A paying client can still register for the full course or a specific block.
3. The system prioritises the paying client, even if this causes temporary over-capacity.

**Workaround:** Configure trial bookings to use **extra capacity** only (in the programme's trial session settings at **Programme -> Settings -> Trial**). This ensures trials do not consume spots reserved for paying clients.

There is currently no way to assign a trial to a specific block. The trial client must decide which block to join only after converting to a full registration.

<!-- REVIEW: There is no way to assign a trial to a specific block. Monitor for future feature updates. -->

### Dynamic tags

Dynamic tags such as `COURSE_DATE_DAY` and `COURSE_TIME` pull their values from the first session in the class as a whole, not from the client's specific block. If a client is enrolled in a later block (e.g. starting in April when the first session is in January), the confirmation email may display the wrong date or time.

**Workaround:** Replace `COURSE_DATE_DAY` and `COURSE_TIME` with the `ORDER_SUMMARY` tag in your email templates. `ORDER_SUMMARY` includes block-specific details for each booking. If you name your blocks descriptively (e.g. "Mondays 17:00"), the client receives accurate information.

Edit the booking confirmation template at **Communication -> Templates -> Booking done**.

<!-- REVIEW: No block-specific dynamic tags exist yet. Check whether dedicated block date/time tags have been introduced. -->

### Attendance

When you change a student's block assignment on a registration, attendance records for the previous block are marked as **Hidden**. The data is not deleted, but the booking detail displays only the label "Hidden" instead of the original status (e.g. "Attended").

This makes it difficult to verify how many sessions a student attended before the change. If you need to preserve this information, export or note the attendance data before changing the block.

Sessions that belong to blocks the client is not registered for are also marked as **Hidden** in the attendance tile and are not visible to the client.

<!-- REVIEW: Product team may add a feature to retain visible attendance history across block changes. Check for updates. -->

### Transfers

When you transfer a registration between classes, block assignments on the new class may not be set correctly automatically. After a transfer:

1. Open the transferred registration's booking detail.
2. Check the **Class** tile to verify which blocks the client is assigned to.
3. If the block assignment is wrong, change it manually via the attendance view.

Note: You cannot use the transfer function to move a client between blocks within the same class. Instead, change the block directly in the attendance view. If attendance tracking is disabled on the class, enable it temporarily, make the block change, then disable it again if needed.

### Registration form capacity display

The registration form may show overall class capacity (e.g. "8/12") rather than per-block capacity. Clients may see "full" when only one block is full but others still have space. The per-block capacity display fix was deployed in early 2026, but verify this is working correctly for your setup.

<!-- REVIEW: Confirm per-block capacity display is stable across all widget types. -->

## Known limitations

| Limitation | Workaround |
|---|---|
| No block-specific dynamic tags for date and time | Use `ORDER_SUMMARY` tag and name blocks descriptively |
| Trials cannot be assigned to a specific block | Use extra capacity for trials; manage manually if over-capacity occurs |
| Attendance history is hidden after block change | Export attendance data before changing a client's block |
| Full-programme registrations can push individual blocks over capacity | Disable "register for entire programme" in online registration settings |
| Block-based filtering of registrations is limited | Check block occupancy in the class detail view |
| Payment templates do not dynamically calculate price based on selected blocks for all template types | Use **Periodic Prepayment with By Block frequency** for block-based billing; for other template types, set prices manually |
| Cannot transfer within the same class between blocks | Change block assignment directly in the attendance view |

<!-- REVIEW: Block filtering and block column in booking exports were requested in Jan 2026. Check whether these have been shipped. -->

## Best practices

1. **Name blocks descriptively.** Use names like "January -- Mondays 17:00" or "Week 1 (1--5 July)" so that the `ORDER_SUMMARY` tag in emails gives clients useful information.

2. **Decide early whether clients register per block or for the full programme.** If per-block registration is your model, disable the "register for entire programme" option to avoid capacity conflicts.

3. **Use the Periodic Prepayment template with By Block frequency** when blocks represent billing periods. Use standard frequencies (monthly, quarterly) when blocks are only an organizational split.

4. **Keep block structures simple.** The more complex the block setup, the more edge cases arise with capacity, dynamic tags, and transfers. Simpler rules lead to fewer support issues.

5. **Check block occupancy in the class detail** before and after peak registration periods. Block-level statistics were added in early 2026.

6. **Avoid combining trials with blocks on the same class** unless you configure trials to use extra capacity. The capacity conflict between group-wide trial reservations and per-block limits is the most common source of over-capacity issues.

7. **Export attendance before changing a client's block** if you need to preserve the attendance history for reporting or verification.

8. **Use `ORDER_SUMMARY` instead of `COURSE_DATE_DAY` and `COURSE_TIME`** in all email templates for block-based programmes to ensure clients receive correct date and time information.

## Related resources

- [Blocks creation guide](blocks-creation.md) -- step-by-step creation, pricing, products, and visual overview
- [Blocks FAQ](../faq/blocks-faq.md) -- quick answers to common questions
- [Payment templates creation](payment-templates-creation.md) -- setting up Periodic Prepayment with By Block frequency
- [Dynamic tags](dynamic-tags.md) -- full list of available tags and their behaviour
