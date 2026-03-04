---
title: "Locations and Venues FAQ"
slug: "locations-and-venues-faq"
type: "faq"
product_area: "Settings"
sub_area: ""
audience: ["admin"]
tags: []
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-12"
intercom_id: 13728492
intercom_sync: false
---

<!-- Synonyms: remove location from course, remove location from class, remove location from group, change location on class, unset location, no location, location not set, lokalita kurzu, zmeniť lokalitu, odstrániť lokalitu zo skupiny -->

# Locations and Venues FAQ

## Can I remove a location from a class (course/group)?

Location is a required field on a class — you cannot leave it blank. You can only **replace** it with a different location.

If you want to remove or unset the location (e.g. the venue is not confirmed yet, or classes moved online), create a placeholder location and assign it:

1. Go to **Settings → Locations** and create a new location with a placeholder name, for example:
   - `TBD` / `To be announced`
   - `Online`
   - `Various venues`
2. Go to the class, open its settings, and change the location to the placeholder.

> **Note:** When someone asks how to "remove a location from a course", they typically mean a class or group (not a programme). Location is set on the **class**, not on the programme. Go to the class settings to change it.

## How do I add a new location?

Go to **Settings → Locations** and create a new entry. Provide the location name, address, and optionally a map pin. The location will become available when creating or editing classes.

## I edited a location name but it still shows the old name on the booking form — why?

Zooza uses browser caching to speed up page loading. After editing a location, do a hard refresh (Cmd+R on Mac, Ctrl+R on Windows). The update may also take a moment to appear on the public booking form, especially on pages with heavy content.

## How do I delete a location / venue?

Before deleting a location, make sure there are no active classes or sessions assigned to it. The correct process is:

1. Delete or reassign all classes linked to that venue.
2. Then delete the venue itself.

If you delete a venue while classes are still linked to it, those classes may show errors or unexpected behaviour.

## Can I create a location without a physical address?

Yes. For sessions like birthday parties at a client's home, you can create a location with a descriptive name (e.g., "Party at client's home") without a specific address. The map will not be shown to clients if no address is set.

## Each location has an internal ID — where can I find it?

Location IDs (Place IDs) are used internally for things like booking links and email templates. They are not prominently displayed in the interface. Contact support if you need to reference a specific Place ID for custom links or templates.
