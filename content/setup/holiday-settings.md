---
title: "Holiday settings"
slug: "holiday-settings"
type: "setup"
product_area: "Calendar"
sub_area: ""
audience: ["admin"]
tags: []
status: "published"
source_legacy_path: "legacy/0020_Welcome to Zooza.html"
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-15"
intercom_id: 13728800
intercom_sync: false
---

# Holiday settings

You must have the correct region filled in for each location in order for the app to automatically pull in vacations correctly.

## General settings

1. You can make the settings in the main *Settings*, under *Places.*
 ![Screenshot](../../assets/images/holiday-settings-01.png)

1. When adding a new location or editing an existing one, select a
region from the menu. The offer is updated on the basis of the company
region you entered in the application when creating an account in the
application. If you would like to change this region, please feel free
to contact us via chat on this page or by email at [support@zooza.online](mailto:support@zooza.online).
 ![Screenshot](../../assets/images/holiday-settings-02.png)

1. After selecting the region, click *the Save* button at the bottom of the page.

## Regional holidays

Holidays are different for each state, city and region. That’s why we
 went to a detailed solution where you can set a region for each
location you run your programmes in.

Based on this setting, the holidays of the specific region will be
automatically added to your app. You will see the specific dates of the
holidays at the level of inserting sessions into the class, where you will
be reminded that the dates are during the holidays. You can choose to:

- keep these terms, if you are running your programmes also during the holidays
- delete these terms manually by clicking on the *Bin icon*
- skip these terms automatically by clicking on the *Skip Holidays* and *Skip School breaks* checkboxes

![Screenshot](../../assets/images/holiday-settings-03.png)

## Setting different regions for multiple locations

If your business operates across multiple districts or regions (for example, a franchise with locations in different cities), each location can have its own region assigned independently. This is important because school holidays and public holidays often differ by region.

1. Go to **Settings** > **Places**.
2. Click on each location to open its detail.
3. In the `Region` field, select the correct district or region for that specific location.
4. Click **Save**.

Repeat for every location. Sessions generated for classes at each location will respect only the holidays of that location's assigned region.

> **Important:** If a location has no region set, the system cannot determine which holidays apply. This commonly happens with online courses or newly added locations. Always verify that every location -- including online or virtual ones -- has a region assigned.

<!-- REVIEW: Confirm whether online/virtual locations inherit the company-level region or default to no region when left blank. Support case suggests they default to no region. -->

## Rescheduling sessions and holiday rules

When you bulk-reschedule existing sessions (for example, moving all sessions from one day of the week to another), holiday-skip rules are **not** re-applied. The system treats bulk rescheduling as a manual override of already-created sessions.

This means sessions may land on public holidays or school breaks after rescheduling, even if the original sessions correctly skipped those dates.

**After any bulk reschedule, you must:**

1. Open the class and review all rescheduled sessions in the session list.
2. Check whether any sessions now fall on a holiday or school break.
3. Delete or move any unwanted sessions manually using the **Bin icon** or by rescheduling individual sessions.

> **Tip:** The system displays a warning when you perform a bulk reschedule reminding you to verify the resulting sessions. Do not skip this step.

<!-- REVIEW: Verify the exact wording of the in-app warning shown during bulk rescheduling. Support mentioned "danu hlasku sme dali aj do systemu" (we added a message to the system). -->

## External holiday data and accuracy

Zooza uses an external service to provide public holiday and school break data for each region. This data can sometimes be outdated or incorrect. Known issues include:

- Dates that are no longer public holidays still appearing in the system (for example, September 1 or November 17 in Slovakia).
- School break durations that do not match the current academic calendar for your specific region.

**If you suspect holiday data is wrong:**

1. Compare the holidays shown in Zooza against an official government or school calendar for your region.
2. Contact Zooza support at [support@zooza.online](mailto:support@zooza.online) to request a correction.
3. In the meantime, manually add or remove affected sessions in your classes.

> **Note:** Zooza is actively working on improving holiday data reliability. When the external service is unavailable or outdated, the team updates holiday records manually in the database.
