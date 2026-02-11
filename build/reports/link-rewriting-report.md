# Link Rewriting Report

**Date:** 2026-02-11

## Summary

- **Files processed:** 85
- **Files updated:** 27
- **Total links rewritten:** 47

## Results

Successfully rewrote 47 legacy internal links from the format:
- `https://support.zooza.online/portal/en/kb/articles/SLUG`
- `/portal/en/kb/articles/SLUG`

To relative `.md` paths based on the redirect mappings in `content/_redirects.yml`.

### Example Conversions

| Original Link | Rewritten To | Context File |
|--------------|--------------|--------------|
| `https://support.zooza.online/portal/en/kb/articles/payment-templates-creation` | `payment-templates-creation.md` | `content/guides/automatic-payment-reminders.md` |
| `https://support.zooza.online/portal/en/kb/articles/online-registration` | `../setup/online-registration.md` | `content/guides/course-settings.md` |
| `https://support.zooza.online/portal/en/kb/articles/trial` | `../setup/trial-lessons.md` | `content/guides/course-settings.md` |
| `https://support.zooza.online/portal/en/kb/articles/auto-enrollment` | `../setup/auto-enrollment.md` | `content/guides/course-settings.md` |

## Unmapped Legacy Slugs

The following legacy slugs were referenced in content files but not found in `content/_redirects.yml`:

1. `replacement-lessons` (referenced in `course-settings.md`)
2. `creating-events-in-groups` (referenced in multiple files)
3. `course-creation` (referenced in multiple files)
4. `group-creation` (referenced in `course-group-lesson-definition.md`)
5. `delete-archive-courses` (referenced in `course-settings-tile.md`)
6. `labels-and-extra-fields` (referenced in multiple files)
7. `setting-the-price-on-a-course` (referenced in `course-settings.md`)
8. `attendance-setup` (referenced in `course-settings.md`, `multi-day-event-with-product-offer.md`)
9. `copy-courses-groups` (referenced in `payment-tile-on-registration.md`)
10. `billing-settings` (referenced in `getting-started-with-zooza.md`)
11. `invoicing` (referenced in `trial-lessons.md`)

### Action Required

These unmapped slugs indicate either:
1. Missing redirects that need to be added to `content/_redirects.yml`
2. Legacy content that hasn't been converted yet
3. Content that was removed/archived and needs no redirect

**Recommendation:** Review these unmapped slugs and either:
- Add corresponding redirects if the content exists under a new slug
- Create the missing content if needed
- Remove the links if the content is obsolete

## Files Updated

The following 27 files had links rewritten:

1. `content/guides/automatic-payment-reminders.md` (1 link)
2. `content/guides/blocks-creation.md` (1 link)
3. `content/guides/course-group-lesson-definition.md` (1 link)
4. `content/guides/course-settings-tile.md` (1 link)
5. `content/guides/course-settings.md` (6 links)
6. `content/guides/customizing-widgets.md` (1 link)
7. `content/guides/documents.md` (2 links)
8. `content/guides/edit-payment-on-registration.md` (1 link)
9. `content/guides/how-to-create-paid-events.md` (1 link)
10. `content/guides/individual-lessons-climbing-wall.md` (2 links)
11. `content/guides/individual-lessons-group-interested.md` (3 links)
12. `content/guides/individual-lessons-with-free-lesson.md` (2 links)
13. `content/guides/individual-sessions.md` (2 links)
14. `content/guides/linked-registrations.md` (1 link)
15. `content/guides/multi-day-event-with-product-offer.md` (2 links)
16. `content/guides/payment-tile-on-registration.md` (3 links)
17. `content/guides/summer-camps-creation.md` (1 link)
18. `content/guides/trials-daily-business.md` (1 link)
19. `content/guides/types-of-registrations.md` (1 link)
20. `content/guides/user-roles.md` (1 link)
21. `content/guides/zooza-101-instructors.md` (1 link)
22. `content/setup/abra-flexi-invoices.md` (1 link)
23. `content/setup/deploying-zooza-on-website.md` (1 link)
24. `content/setup/getting-started-with-zooza.md` (6 links)
25. `content/setup/online-registration.md` (1 link)
26. `content/setup/power-bi-integration.md` (2 links)
27. `content/setup/trial-lessons.md` (1 link)

## Technical Details

### Script Location
`/Users/michaldodok/help/build/rewrite_links.py`

### Pattern Matching
The script uses regex to find markdown links matching:
```
[link_text](https://support.zooza.online/portal/en/kb/articles/SLUG)
[link_text](/portal/en/kb/articles/SLUG)
```

### Path Resolution
For each matched link:
1. Extract legacy slug from URL
2. Look up new slug and product area from redirects
3. Find actual .md file in content/ subdirectories
4. Compute relative path from current file to target file
5. Replace with relative .md path

### Relative Path Examples
- Same directory: `file.md`
- Parent directory: `../setup/file.md`
- Nested: `../faq/topic.md`
