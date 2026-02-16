---
title: "Holiday and Term Management FAQ"
slug: "holiday-management-faq"
type: "faq"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: ["holidays", "terms"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-15"
intercom_id: 13738677
intercom_sync: false
---

# Holiday and Term Management FAQ

## How do I set up public holidays so sessions are automatically skipped?

When creating sessions for a class, Zooza shows you which dates fall on holidays or school breaks based on the region assigned to that location. You have three options:

1. **Keep the sessions** if you run programmes during holidays.
2. **Delete individual sessions manually** by clicking the bin icon next to each holiday date.
3. **Skip automatically** by checking the **Skip Holidays** and/or **Skip School Breaks** checkboxes before generating sessions.

These checkboxes are available in the session creation screen when you add sessions to a class. For the system to know which dates are holidays, the location must have a region assigned (see next question).

See also: [Holiday settings](../setup/holiday-settings.md)

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

## How do I cancel a single session and notify only the affected clients?

1. Open the class detail and find the session you want to cancel.
2. Click on the session to open its detail.
3. Cancel or delete the session.
4. When prompted, choose to **send a notification** to clients. The notification is sent only to clients who are registered (enrolled) in that specific session.

Clients who are on the waiting list or registered in other sessions of the same class are not notified.

<!-- REVIEW: Confirm the exact UI flow for cancelling a single session and the notification prompt options. The steps above are based on standard session management patterns described in support conversations. -->

## Sessions disappeared from my course. What happened?

If sessions vanished unexpectedly, the most common cause is **holiday auto-skip**. When sessions were initially created with the **Skip Holidays** or **Skip School Breaks** option enabled, any dates that fall within the configured holiday or break window are excluded automatically.

Other possible causes:

- **A team member cancelled or deleted them.** Check the session activity log in the class detail to see if another admin or instructor removed sessions.
- **The location region was changed**, which may have shifted which dates are treated as holidays, causing sessions to be retroactively flagged. <!-- REVIEW: Verify whether changing a location region affects already-created sessions or only future session generation. -->

**To investigate:**

1. Go to the class detail and check the session list. Look for gaps in the expected schedule.
2. If sessions were skipped due to holidays, you can manually add them back by creating individual sessions on the missing dates.
3. If you suspect an error, contact Zooza support with the class link so they can check the session creation and deletion history in the database.
