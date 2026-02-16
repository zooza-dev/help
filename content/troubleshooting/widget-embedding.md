---
title: "Widget Embedding Troubleshooting"
slug: "widget-embedding-troubleshooting"
type: "troubleshooting"
product_area: "Widgets"
sub_area: ""
audience: ["admin"]
tags: ["widgets", "embedding", "website", "wordpress", "calendar", "profile"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: true
last_converted: "2026-02-13"
intercom_id: 13738722
intercom_sync: false
---

# Widget Embedding Troubleshooting

This guide covers common problems when embedding Zooza widgets on your website, along with their causes and solutions.

For initial setup instructions, see [Deploying Zooza on your website](../setup/deploying-zooza-on-website.md). For customization options, see [Customizing widgets](../guides/customizing-widgets.md).

## Widget not loading on website

### Cookie or consent banner blocking Zooza scripts

**Problem:** The widget does not render on the page at all. The page area where the widget should appear is blank.

**Cause:** Your website's cookie consent banner or privacy tool is blocking the Zooza JavaScript from executing. Zooza widgets require scripts to load, and consent managers often categorize third-party scripts as non-essential by default.

**Solution:**

1. Open your cookie consent or privacy tool settings (e.g. CookieBot, OneTrust, or your CMS cookie plugin).
2. Add Zooza script domains to the whitelist or mark them as "necessary" or "functional" scripts.
3. Test the page in an incognito browser window to confirm the widget loads after accepting cookies.

<!-- REVIEW: Exact Zooza script domain(s) to whitelist should be confirmed with the dev team. -->

### WordPress plugin duplicate rendering

**Problem:** The registration form, calendar, or another widget appears two or three times on the same page.

**Cause:** The Zooza WordPress plugin automatically injects the widget at the bottom of the page you configure in its settings. If you also manually paste embed code (HTML snippet or shortcode) onto the same page, the widget renders multiple times.

**Solution:**

1. Choose one method only: either use the WordPress plugin **or** use embed code, not both on the same page.
2. If you use the WordPress plugin, do not add any Zooza embed code or shortcode to that page.
3. If you need advanced filtering (e.g. showing only specific programmes), disable the plugin and use embed code instead. You can generate filtered embed code from **Publish** in Zooza.
4. For advanced integration and CSS customization, refer to the developer documentation at `https://docs.zooza.online`.

### HTTPS vs HTTP mismatch

**Problem:** Links copied from Zooza open with `http://` instead of `https://`, causing security warnings or broken pages.

**Cause:** The widget publish settings stored the original page URL with `http://`. Even after your website migrated to HTTPS, the server retained the old protocol in its database.

**Solution:**

1. Go to **Settings** > **Publish** in Zooza.
2. Open the widget settings for each widget type (booking form, calendar, profile, etc.).
3. Verify that the URL field uses `https://`.
4. If the URL already shows `https://` but links still use `http://`, edit the URL field (add a character, save, then revert and save again) to force a database update.

## Widget shows wrong courses or all courses

### Filter syntax issues (comma vs semicolon delimiters)

**Problem:** The embed code on your website displays all programmes instead of the filtered subset you configured.

**Cause:** The filter parameters in the embed code use incorrect delimiters. Zooza expects a specific separator (semicolon or comma depending on the parameter) and mismatched delimiters cause the filter to be ignored.

**Solution:**

1. Go to **Publish** > **Embed code** in Zooza.
2. Click **Customize embed code** below the code snippet.
3. Select the specific programmes and locations you want to display.
4. Click **Copy** and replace the old code on your website with the newly generated code.
5. Do not manually edit filter parameters in the embed code. Always regenerate the code using the Zooza configurator to avoid syntax errors.

### Programme not appearing due to booking/catalogue settings

**Problem:** A programme does not appear on the booking page or in the widget, even though it has active classes with available capacity.

**Cause:** The programme has either `Allow online booking` or `Display in catalogue` disabled (or both). Both settings must be enabled for the programme to appear on your public booking page and widgets.

**Solution:**

1. Go to **Programmes** → select the programme → **Edit Settings**.
2. Open the **Online Booking** tile.
3. Verify that `Allow online booking` is toggled **on**.
4. Verify that `Display in catalogue` is checked.
5. Save and refresh your website.

> **Tip:** `Allow online booking` controls whether the programme accepts online registrations. `Display in catalogue` controls whether it appears in the booking form list and website menu. Both must be on.

### Embed code parameter errors

**Problem:** Manually edited embed code does not filter correctly, or the widget shows unexpected results.

**Cause:** Parameters such as `course_id`, `place_id`, or `schedule_id` were entered incorrectly, or stale IDs reference archived or deleted programmes.

**Solution:**

1. Regenerate the embed code from **Publish** > **Embed code** > **Customize embed code**.
2. Verify that the programme and location IDs in the code match active items in your Zooza account.
3. After pasting the new code, hard-refresh the page (Ctrl+F5 on Windows, Cmd+Shift+R on Mac) to clear cached scripts.

## Capacity display issues

### Session vs group capacity confusion

**Problem:** The calendar widget shows free spots on a session even though the group is full. New clients attempt to register for spots that are only temporarily available due to cancellations.

**Cause:** By default, the calendar widget displays per-session capacity (how many people are attending that specific session). When a client cancels a single session, that session shows a free spot even if the group itself has no open registrations. This capacity is intended for make-up (replacement) lessons, not new sign-ups.

**Solution:**

1. If you do not use blocks, Zooza now displays group capacity instead of session capacity by default. Verify your widget is using the latest behaviour.
2. To control the capacity display, go to **Publish** > select your widget > **Calendar** settings and check the occupancy display option.
3. If you use blocks, the calendar shows per-session capacity by design, because block-based courses manage capacity at the session level.

<!-- REVIEW: Group vs session capacity display toggle was deployed in Jan 2026. Confirm exact setting location and label. -->

### Archived items appearing in filters

**Problem:** Archived courses or inactive billing periods still appear in the calendar widget filters.

**Cause:** Archived courses are hidden from most admin views but may still appear in public widget filter dropdowns if they were not fully removed from the widget configuration.

**Solution:**

1. Go to **Publish** > **Embed code** > **Customize embed code**.
2. Explicitly select only the active programmes and locations.
3. Regenerate and replace the embed code on your website.

## Widget links broken

### Base URL misconfiguration in publish settings

**Problem:** Links in emails or within widgets (e.g. "View profile", "Register here") lead to the wrong page or a 404 error.

**Cause:** The base URL configured in **Publish** > widget settings does not match the actual URL where the widget is deployed on your website. Zooza uses these URLs to generate all outbound links in emails and notifications.

**Solution:**

1. Go to **Settings** > **Publish** in Zooza.
2. For each widget (booking form, profile, calendar, videos, sales form), verify the URL matches the exact page where that widget is embedded on your website.
3. Save changes.
4. If your domain recently changed, update all widget URLs immediately. Until updated, all email links to clients will point to the old domain.

> **Important:** If you do not enter the correct URL for each widget, links in client emails (registration confirmations, session reminders, payment notifications) will not work.

### 404 on product purchase links

**Problem:** Clicking **Buy** on a product in the profile widget leads to a 404 page.

**Cause:** The sales form (order/checkout widget) URL is not configured in the publish settings, or no page with the sales form widget exists on your website.

**Solution:**

1. Create a page on your website for the sales/checkout form if one does not exist.
2. Embed the sales form widget on that page using embed code from **Publish** > **Sales form**.
3. Go to **Publish** > widget settings and enter the URL of the sales form page.
4. Save and test by clicking a product purchase link from the profile widget.

## Profile widget issues

### Tabs not responding (cache/reload)

**Problem:** The profile widget tabs (Attendance, Payments, Videos, Files, Detail) do not respond when clicked. The view stays on the Overview tab.

**Cause:** This can be caused by a temporary bug, a stale cached version of the widget scripts, or JavaScript conflicts with other scripts on the page.

**Solution:**

1. Ask the client to hard-refresh the page (Ctrl+F5 on Windows, Cmd+Shift+R on Mac).
2. If the issue persists, test in an incognito/private browser window to rule out cache.
3. If the problem is widespread across multiple clients, contact Zooza support. A previous incident of this type was resolved with a server-side fix.

### GDPR consent loop blocking profile access

**Problem:** After accepting GDPR consents, the page returns to the consent screen instead of opening the profile. Parents cannot access their profile at all.

**Cause:** This can happen with older client accounts (e.g. those imported during onboarding). The consent acceptance may not persist due to a data format mismatch on the account.

**Solution:**

1. Ask the affected client to clear their browser cache and try again.
2. If the loop persists, contact Zooza support with the affected client's email address. Support can refresh the affected account records on the server side.

### Video widget redirecting instead of playing inline

**Problem:** Clicking a video in the profile or on a video page redirects to a blog post or a different page instead of playing the video inline.

**Cause:** The video widget page URL in publish settings is misconfigured or missing entirely. When Zooza cannot find the correct video widget page, it falls back to a default redirect.

**Solution:**

1. Create a dedicated page on your website for the video widget if one does not exist.
2. Embed the video widget on that page using embed code from **Publish** > **Videos**.
3. Go to **Publish** > widget settings and enter the correct URL for the video page.
4. Save and test by opening a video from the client profile.

> **Note:** The video widget must be deployed on your website even if you only want clients to view videos through their profile. Without it, video links will not work.

## Calendar widget issues

### Group not appearing in the schedule widget

**Problem:** A newly created group does not show up in the calendar/schedule widget on your website.

**Cause:** There can be a short delay (typically a few minutes) between publishing a group in Zooza and it appearing on the website widget. Browser caching can extend this delay.

**Solution:**

1. Wait a few minutes after creating or publishing the group.
2. Hard-refresh the website page (Ctrl+F5 on Windows, Cmd+Shift+R on Mac).
3. Verify the group has online registration enabled: go to the group settings and check that online registration is turned on.
4. If using filtered embed code, verify the new group's programme is included in the filter.

### Schedule widget showing text instead of calendar grid

**Problem:** The schedule/calendar widget shows session dates as a text list instead of a visual calendar grid.

**Cause:** The calendar widget display mode is set to text view instead of calendar/grid view in the widget settings.

**Solution:**

1. Go to **Publish** > select your widget > **Calendar** settings.
2. Change the display format from text to calendar/grid view.
3. Save changes and refresh the page on your website.

## Widgets still accessible after account deactivation

**Problem:** After deactivating your Zooza account, clients can still access the profile widget and attempt to log in.

**Cause:** Widgets embedded on your website remain functional as long as the embed code is present on the page. Account deactivation stops notifications and new registrations, but existing widget code still renders and clients can reach the login screen.

**Solution:**

1. Remove all Zooza embed code and widget scripts from your website pages.
2. If using the WordPress plugin, deactivate and uninstall it.
3. Once the widget code is removed, the URLs become inactive and clients can no longer access the forms.

## Website down -- temporary redirect to Zooza Sites

**Problem:** Your website is temporarily offline and clients cannot access registration forms or their profile.

**Cause:** When your website is down, all widget pages become unreachable. Email links sent to clients also stop working because they point to your website.

**Solution:**

1. Contact Zooza support to request a temporary redirect to a Zooza Sites page (e.g. `zooza.site/your-business-name`).
2. Zooza support can update the widget URLs so that all outgoing emails point to the temporary Zooza Sites page.
3. Once your website is back online, contact support again to revert the URLs to your original domain.

## General troubleshooting tips

- **Always regenerate embed code** from the Zooza configurator rather than manually editing HTML parameters.
- **Test in incognito mode** to rule out browser cache and cookie issues.
- **Check publish settings** whenever links in emails or widgets lead to wrong pages. Go to **Settings** > **Publish** and verify every URL.
- **Widget design customization** is handled via CSS on your website. Refer to `https://docs.zooza.online` for available CSS classes and overrides.
- **One widget per page:** Avoid placing multiple instances of the same widget type on a single page.
