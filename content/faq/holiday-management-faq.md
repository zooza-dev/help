---
title: "Holiday and Term Management FAQ"
description: "When creating sessions for a class, Zooza shows you which dates fall on holidays or school breaks based on the region assigned to that location."
slug: "holiday-management-faq"
type: "faq"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: ["holidays", "terms", "make-up", "pause", "attendance"]
status: "published"
related_articles: ["make-up-sessions-faq", "edit-payment-on-booking", "payment-correction-vs-refund", "holiday-settings", "custom-holidays", "managing-sessions-in-a-class"]
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-08-07"
---

# Holiday and Term Management FAQ

## How do I set up public holidays so sessions are automatically skipped?

When creating sessions for a class, Zooza shows you which dates fall on holidays or school breaks based on the region assigned to that location. You have three options:

1. **Keep the sessions** if you run programmes during holidays.
2. **Delete individual sessions manually** by clicking the bin icon next to each holiday date.
3. **Skip automatically** by checking the **Skip Holidays** and/or **Skip School Breaks** checkboxes before generating sessions.

These checkboxes are available in the session creation screen when you add sessions to a class. For the system to know which dates are holidays, the location must have a region assigned (see next question).

See also: [Holiday settings](../setup/holiday-settings.md)

## I cannot find the Skip Holidays checkbox anywhere

It is in **Advanced** session planning. Basic planning does not offer it.

When you create a class, the **Sessions** heading has two tabs — **Basic** and **Advanced**:

1. Open the class → **Sessions** → **Add sessions**.
2. Switch to the **Advanced** tab.
3. Click **Create sessions** and set the sessions to repeat.
4. The **Skip Holidays** and **Skip School Breaks** checkboxes appear once repetition is defined.

Advanced planning is also where you cover schedules that vary within one class — for example Mondays with one instructor for 45 minutes and Tuesdays with another for 60 minutes.

> Nothing has been removed. The option was never in the class settings screen itself; it belongs to session generation, which is why it appears only at the point where dates are produced.

## Can I apply holiday skipping to sessions I already created?

No. Holiday rules run once, at generation time, and there is no way to re-apply them afterwards. This is deliberate — activities for very young children often run straight through the holidays, so Zooza never removes dates on its own.

To clean up sessions that already landed on holidays:

1. Go to **Activities → Sessions**.
2. Filter to the dates that fall on the holiday period.
3. Select them and either **bulk delete** (if they were created by mistake) or **bulk move** them to replacement dates.

Bulk moving is usually the better option for a class that is already sold, because deleting sessions can change what clients owe.

## How do I set holiday regions per location?

Each location must have a region assigned so that the correct public holidays and school breaks apply.

1. Go to **Settings > Places**.
2. Open the location you want to configure (or create a new one).
3. In the location detail, select the appropriate **Region** from the dropdown.
4. Click **Save**.

The region determines which national holidays and regional school breaks Zooza applies. If your company operates in multiple regions (e.g., different states or districts), assign the correct region to each location individually.

<!-- REVIEW: The region dropdown options are populated based on the company-level country setting chosen during account creation. Changing the company-level country requires contacting support. -->

## The system treats certain dates as holidays that are no longer official holidays. How do I fix this?

Zooza uses an external service to maintain its holiday database. Occasionally, that service may be slow to update or may contain outdated entries (for example, dates that were once public holidays but have since been removed from the official calendar).

If you notice incorrect holiday dates:

1. Contact Zooza support via chat or email at [support@zooza.online](mailto:support@zooza.online).
2. Provide the specific dates that are incorrectly marked as holidays and the country or region affected.
3. The Zooza team will verify and correct the entries in the database.

<!-- REVIEW: As of early 2026, the external holiday service has had reliability issues. Zooza has manually corrected the database for known discrepancies and is evaluating alternative data sources. -->

## Spring holidays are configured as 3 weeks but we only need 1 week for our region. How do I narrow the range?

Spring (and other regional) school breaks can vary by district or state. If the system applies a wider break window than your region observes, the most likely cause is an incorrect region setting on your location.

1. Go to **Settings > Places** and open the affected location.
2. Check the **Region** field. Make sure it matches the specific district or region your location operates in (e.g., "Bratislava Region" rather than a broader national setting).
3. Save and then verify the session creation screen to confirm only the correct break dates are flagged.

If the region is already correct but the break dates are still wrong, contact Zooza support. The holiday data may need a manual correction for your region.

## After rescheduling sessions to a different weekday, holiday-skip rules no longer apply. Why?

When you use bulk edit to move existing sessions (for example, shifting all sessions forward by several days or changing the weekday), the system treats this as a manual override. Holiday-skip rules are applied only at the time of initial session creation, not retroactively after manual changes.

This means that if you reschedule sessions and the new dates happen to fall on a public holiday or school break, the system will not automatically remove them.

**What to do after rescheduling:**

1. After any bulk session move, review the updated session list in the class detail.
2. Manually delete or cancel any sessions that now fall on holidays.
3. If you need to regenerate sessions from scratch (with holiday skipping re-applied), delete the affected sessions and create new ones using the session creation screen with the **Skip Holidays** / **Skip School Breaks** checkboxes enabled.

## We have no holidays for our region, or some are missing

Then enter them yourself as custom holidays. That is what the feature is for.

Public and school holidays come from an external database. It has been reliable, but we increasingly get reports that it does not carry every holiday for every region — which is exactly why entering your own was added.

The order to work through:

1. **Set the region on the location** — Settings → Places → open the place → **Region**. Without it, Zooza does not know which national and regional holidays apply, and none will be offered.
2. **Generate sessions and look at the highlighted dates.** If your region's holidays appear, you are done.
3. **If dates are missing or wrong, add them under Team & Settings → General → Custom holidays.** Enter the date ranges you want skipped. They then behave exactly like public holidays when you generate sessions.

Custom holidays belong to your account only and are never shared with other companies, so you can add whatever your business actually observes — a local festival, a venue closure, a week you simply do not run.

> Also tell us at [support@zooza.online](mailto:support@zooza.online) if a national holiday is genuinely missing for your region. Your custom holiday fixes your account today; a report gets it fixed for everyone.

## What are custom holidays and how are they different from public holidays?

Public and school holidays are synced automatically from national calendars based on your location's region. You cannot edit or delete them.

Custom holidays are holidays you create yourself — for example, a company retreat, a local event, or an unplanned closure. They belong to your Zooza account and are never shared with other accounts. They can be created, edited, and deleted at any time by an admin with the `manage_places` role.

Both types work the same way for scheduling: sessions created within a holiday period are skipped automatically.

See [Custom holidays](../guides/custom-holidays.md) for step-by-step instructions.

## Can I create a holiday that applies only to some of my locations, not all?

Yes. When creating a custom holiday, set the scope to **Region-specific** and select the regions where the holiday applies. Only sessions at locations assigned to those regions will be skipped.

For a closure that affects all your locations, set the scope to **Company-wide**.

## I created a custom holiday but my existing sessions still appear on those dates. Why?

Custom holidays (like all holiday settings) only affect session creation going forward. Sessions that were already generated before the holiday was created are not automatically removed.

To fix this:

1. Go to the class detail and review the session list for dates that fall within the holiday period.
2. Delete or cancel the individual sessions manually using the bin icon.

## Do custom holidays affect cancellation deadlines?

Yes. Custom holidays count as holidays for the **Block cancellations on weekends and holidays** setting. If a cancellation deadline would fall on a custom holiday, it is moved to the previous working day — the same way it works for public holidays.

## Can I edit or delete a custom holiday after it has been saved?

Yes. Go to **Settings** > **Custom Holidays**, find the holiday, and use the edit (pencil) or delete (bin) icon.

Keep in mind:
- Editing dates or scope does not automatically add or remove sessions that have already been created.
- Deleting a custom holiday does not restore any sessions that were skipped because of it.

## The national calendar has incorrect holiday dates. Can I work around this with a custom holiday?

Partially. You can create a custom holiday to block out dates that are missing from the national calendar (for example, a local closure not covered by the external data source). However, custom holidays add to the existing data — they do not override or remove incorrect entries from the national calendar.

For incorrect national holiday data, contact Zooza support at [support@zooza.online](mailto:support@zooza.online) so the underlying data can be corrected.

## How do I cancel a single session and notify only the affected clients?

1. Open the class detail and find the session you want to cancel.
2. Click on the session to open its detail.
3. Cancel or delete the session.
4. When prompted, choose to **send a notification** to clients. The notification is sent only to clients who are registered (enrolled) in that specific session.

Clients who are on the waiting list or registered in other sessions of the same class are not notified.

<!-- REVIEW: Confirm the exact UI flow for cancelling a single session and the notification prompt options. The steps above are based on standard session management patterns described in support conversations. -->

## A client is going on holiday — how do I manage their enrolment while they are away?

There is no automatic pause or freeze feature. Depending on what you and the client agreed, you have these options:

**Option A: Cancel the specific sessions for that client (make-up credits)**

1. Open the client's booking and go to the **Attendance** tab.
2. For each session they will miss, set the attendance state to **Cancelled** (not "Did not attend").
3. If your programme has make-up sessions enabled, each cancelled session generates a make-up credit. The client can use these credits to attend a session in a different week.

This is the most common approach for programmes that run continuous classes (subscriptions or term bookings). The client keeps their enrolment and billing is unaffected.

> Only the **"Cancelled"** state generates a make-up credit. "Did not attend" does not. See [Make-up sessions FAQ](make-up-sessions-faq.md) for details.

**Option B: Apply a manual discount or credit to the booking**

If your programme does not use make-ups and the client is paying for weeks they will miss, you can apply a manual credit or payment correction directly on the booking.

For how to adjust a payment, see [Edit payment on booking](../guides/edit-payment-on-booking.md) and [Payment correction vs refund](../guides/payment-correction-vs-refund.md).

**Option C: Cancel and re-register after the break**

For longer absences, it may be simpler to:
1. Cancel (not delete) the booking before the break.
2. Re-register the client after the holiday.

This fully removes them from the class during the break and releases their capacity spot. Billing stops. Any existing payment plan ends and will need to be recreated on re-registration.

## Sessions disappeared from my programme. What happened?

If sessions vanished unexpectedly, the most common cause is **holiday auto-skip**. When sessions were initially created with the **Skip Holidays** or **Skip School Breaks** option enabled, any dates that fall within the configured holiday or break window are excluded automatically.

Other possible causes:

- **A team member cancelled or deleted them.** Check the session activity log in the class detail to see if another admin or instructor removed sessions.
- **The location region was changed**, which may have shifted which dates are treated as holidays, causing sessions to be retroactively flagged. <!-- REVIEW: Verify whether changing a location region affects already-created sessions or only future session generation. -->

**To investigate:**

1. Go to the class detail and check the session list. Look for gaps in the expected schedule.
2. If sessions were skipped due to holidays, you can manually add them back by creating individual sessions on the missing dates.
3. If you suspect an error, contact Zooza support with the class link so they can check the session creation and deletion history in the database.
