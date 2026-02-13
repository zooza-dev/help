# Cluster: Registrations, Widgets, Replacements, Trials, Blocks & Terms

**Source:** `build/reports/ingest-condensed.jsonl` (362 total conversations)
**Filter:** tags containing registrations, registration, registration form, widgets, replacements, replacements from other companies, trial, trials, late_registration, transfer, portal, blocks, terms, open_course
**Matching records:** 95 conversations
**Date range:** 2025-10-30 to 2026-02-11

---

## Tag frequency

| Tag | Count |
|-----|-------|
| widgets | 23 |
| replacements | 19 |
| registrations | 16 |
| registration | 9 |
| terms | 7 |
| blocks | 7 |
| portal | 6 |
| trial | 5 |
| replacements from other companies | 3 |
| transfer | 3 |
| trials | 3 |
| late_registration | 2 |
| registration form | 2 |
| open_course | 1 |

Note: a single conversation often carries multiple tags, so totals exceed 95.

---

## Sub-category breakdown

| Sub-category | Count | Description |
|---|---|---|
| **Replacement hours -- general** | 14 | Booking, viewing, or managing replacement (make-up) lessons |
| **Widget embedding & configuration** | 12 | Embedding registration forms, calendars, profiles, and video widgets on websites |
| **Registration management** | 10 | Creating, copying, moving, or deleting registrations |
| **Replacement hours -- cross-company** | 5 | Using replacements across franchise branches / different legal entities |
| **Widget display & capacity** | 6 | How occupancy, availability, and capacity show in public widgets |
| **Blocks configuration** | 6 | Setting up and managing blocks (sub-periods within a group) |
| **Terms / sessions management** | 5 | Creating, editing, cancelling individual terms; holiday handling |
| **Trial lesson setup & workflow** | 5 | Configuring trial lessons, converting trials to full registrations |
| **Portal access** | 4 | Customer support portal access and login; parent profile access |
| **Client profile widget** | 4 | Profile widget issues -- tabs, login, GDPR consent loop |
| **Transfer between groups** | 4 | Moving registrations between groups or classes |
| **Late registration pricing** | 3 | Pro-rata pricing for registrations that start mid-course |
| **Registration form customization** | 3 | Filtering courses in the form, embed code issues, capacity display |
| **Registration data & search** | 3 | Searching deleted registrations, participant vs. buyer, notes mismatch |
| **Payment on registration** | 3 | Payment schedules on registrations, linking product payments, debt editing |
| **Communication tied to registrations** | 3 | Confirmation emails not sent on copied registrations, dynamic tags with blocks |
| **Open course / drop-in** | 2 | Unsubscribe deadlines for open courses; unwanted session reminder emails |
| **Attendance & replacements interaction** | 2 | "No-show" vs. "unsubscribed" affecting replacement eligibility; attendance hiding on block change |
| **Replacement credits & expiration** | 2 | Deleting or expiring replacement credits; transferring credits across billing periods |

---

## Specific customer questions (generalized, English)

### Replacement hours

1. Why can a client not see available replacement slots in their profile for a specific group?
2. Replacement hours between franchise branches (different legal entities) stopped working -- how to debug?
3. A client confirmed a replacement through the system, but it was not actually booked. Why?
4. How does the "extra capacity for replacements" setting work (global vs. per-group)?
5. Replacements are not available because the group has not started yet -- what is the 4-day rule?
6. How do I delete or expire a replacement credit that was created by mistake?
7. Can replacement credits carry over to the next billing period / trimester?
8. How does the "sign back up for this session" button work in the client profile?
9. Why does the profile filter for replacements not narrow down to a single instructor?
10. Why can a client not mark attendance for a cross-company replacement in the calendar?
11. Where is the replacement-hour waiting list (queue) and how does it notify clients?
12. Client was in "no-show" state instead of "unsubscribed" -- system did not grant a replacement credit. Is that expected?

### Widgets (embedding & configuration)

13. Registration form shows all courses instead of the filtered subset -- embed code has wrong delimiter (comma vs. semicolon).
14. How do I hide the number of registered children on a specific session from the public calendar?
15. Calendar widget shows that a session has free spots after someone unsubscribes -- is that visible to everyone?
16. How to configure the calendar widget to show group capacity instead of per-session capacity?
17. Widget not loading because website cookies block Zooza scripts -- how to whitelist?
18. WordPress plugin duplicates the registration form on the page -- how to fix?
19. How to set the base URL in widget/publish settings so that dynamic tag links point to the correct pages?
20. Embedded schedule widget shows dates as text instead of a calendar grid -- where is that setting?
21. A group does not appear in the schedule widget on the website -- timing / cache issue.
22. Profile widget tabs (attendance, payments) stopped responding -- was a bug, fixed with a reload.
23. Video widget redirects to blog page instead of playing inline -- publish page URL misconfigured.
24. How to set up HTTPS links when copying course URLs from the app?
25. After account deactivation, are widgets still accessible to existing clients?

### Registrations

26. How to add a child (participant) who is different from the buyer (parent) during manual registration?
27. How to change the participant on an existing registration?
28. How to copy a registration to a new term / group -- "Continue" button not working.
29. How to search for deleted registrations and restore them?
30. Client records show notes with a mismatched course name and date -- display bug.
31. Can a second email address be added to a registration for notifications or profile access?
32. When copying a registration manually, the system does not auto-send a confirmation email -- is that expected?
33. How to register a client on a single session in a different group without creating a full new registration (via attendance)?
34. What do the registration "tabs" (linked registrations, buyer vs. client labels) mean?
35. How to give a divorced parent separate access to the same child's registration?
36. Billable terms set only at the group level prevented payment schedule creation on a registration.

### Blocks

37. Where can I check occupancy / capacity of individual blocks within a group?
38. When I changed blocks on a group, previously created blocks disappeared from the admin view but still showed in the registration form.
39. When a client's block is changed on a registration, attendance records for the old block are hidden -- can they be preserved?
40. Filtering registrations by block is not yet possible -- when will it be available?
41. Dynamic tags (e.g., COURSE_DATE_DAY) pull data from the first term in the group, which is incorrect when the client is enrolled in a different block.
42. Trials and blocks used simultaneously cause over-capacity because trial reserves a spot in the whole group while blocks limit per-block.

### Terms / sessions

43. Session time display in the profile was incorrect for sessions over 60 minutes.
44. A holiday / public-holiday term appeared even though the course was set to skip holidays -- root cause was manual rescheduling that lost the holiday rules.
45. How do I cancel a single term and notify only the affected clients?
46. When terms are rescheduled from one weekday to another mid-course, do holiday-skip settings still apply?
47. Instructor-linked label on a cancelled term shows incorrectly.

### Trials

48. How to move a trial-state registration to a different session (hide original, add new via attendance)?
49. Can a client who finished a trial register again for a full course in the same group?
50. Trial registration age restriction prevented a slightly-out-of-range child from booking -- can admins override?
51. How to convert a trial from "trial ended" to a full paid registration ("Start registration" button)?
52. Trials + blocks capacity conflict: trial reserves a seat in the whole group, but block capacity is per-block, leading to overbooking.

### Transfer between groups

53. Transfer filter limits results -- request to add day-of-week filter for easier group selection.
54. Cannot transfer a registration to a group that has attendance tracking disabled -- workaround: enable attendance first.
55. After a transfer, block assignments on the new group were incorrect, causing wrong price calculation.
56. How to move a client from an active group to a "collection bin" / lead group?

### Late registration / pro-rata

57. How does the aliquot (pro-rata) price calculation work for registrations created after the course start?
58. System calculates remaining price on late registrations but does not display it to the client -- is that intentional?
59. How to set a fixed price that ignores pro-rata for late joiners?

### Registration form

60. Registration form capacity showed "full" based on the whole group instead of per-block -- misleading for block-based courses.
61. A test registration went through without issues but the customer reported a capacity error -- could not reproduce.

### Open course / drop-in

62. Client could not unsubscribe from an open-course session within the allowed window -- unsubscribe deadline settings explained.
63. After a test purchase of a single lesson, all clients received an erroneous reminder email.

### Portal access

64. How to access the Zooza support portal and view submitted tickets?
65. How to reset the support portal password?
66. Profile widget: GDPR consent loop -- accepting consents does not persist, blocking profile access.
67. GoCardless bank pairing visible inside customer portal / profile billing area.

### Payment on registration

68. Product price did not link to the registration payment -- hidden setting in Price & Payments > Advanced.
69. When unpairing and re-pairing an order payment to a registration, the paid amount did not update until the flow was completed correctly.
70. Feature request: allow admins to edit the outstanding debt amount directly on a registration.

---

## Common patterns and recurring issues

### 1. Replacement hours are the top pain point
Replacement (make-up) lessons generate the most support volume in this cluster. The most frequent issues are:
- Clients not seeing available replacement slots (often due to capacity limits, the 4-day-before-start rule, or "no-show" vs. "unsubscribed" status).
- Cross-company / cross-franchise replacements failing due to rule mismatches.
- The "sign back up for this session" button behavior being unclear.
- Admins wanting to manually delete or expire replacement credits.

### 2. Widget embedding is error-prone
Customers struggle with:
- Incorrect embed code syntax (delimiters, duplicate script tags from WordPress plugin).
- Cookies / consent banners blocking Zooza scripts.
- Mismatched base URLs causing broken links in emails and widgets.
- Confusion between session-level and group-level capacity display in calendars.

### 3. Blocks are a newer, under-documented feature
Several tickets reveal that blocks (sub-periods within a group) interact poorly with:
- Trials (capacity conflict between group-wide trial seat and per-block limits).
- Dynamic tags in email templates (tags pull from the first term, not the client's block).
- Transfers (block assignments not updating correctly after a move).
- Admin visibility (block occupancy stats and per-block registration filtering were missing at the time).

### 4. Manual registration workflows have hidden steps
When admins copy or create registrations manually, they often miss:
- Sending the confirmation email (not automatic for manual/copied registrations).
- Setting participant vs. buyer correctly.
- Linking product payments to the registration (hidden advanced setting).

### 5. Holiday / term management after rescheduling is fragile
When terms are bulk-rescheduled to a different weekday, the original holiday-skip rules are not re-applied, leading to sessions on public holidays. Customers expect the system to re-validate holidays after any schedule change.

### 6. Late registration pricing is misunderstood
Admins are unclear on whether pro-rata pricing is displayed to the client or only calculated internally. Some want a fixed-price override for late joiners.

### 7. Cross-cutting theme: franchise / multi-branch complexity
Many issues (replacements across companies, transfer filters, block rules) stem from franchise networks where multiple legal entities share a system. These setups amplify configuration complexity.
