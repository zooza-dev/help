# Support Cluster: Non-Payment Topics

Analysis of 177 customer support conversations covering courses, groups, calendar, instructors, clients, attendance, profiles, orders, roles, settings, services, products, holidays, exports, login, onboarding, and untagged tickets.

Source: `build/reports/ingest-condensed.jsonl` (Oct 2025 -- Feb 2026)

---

## Frequency Table by Sub-Category

| Sub-Category | Count | Notes |
|---|---|---|
| **Course & Group Setup** | 22 | Deleting, archiving, copying, moving groups between courses |
| **Attendance & Replacements (Make-up Lessons)** | 18 | Replacement hours logic, attendance states, cross-company replacements |
| **Calendar Display & Filtering** | 12 | Missing sessions, name display, filtering by billing period, widget calendar vs. app calendar |
| **Client Management & Data** | 14 | Changing client data, merging clients, creating clients manually, client not found |
| **Profile / Parent Portal** | 16 | Login issues, GDPR consents blocking access, profile widget confusion, cache problems |
| **Role & Permission Setup** | 10 | Main instructor role limits, receptionist role, hiding pay rates, restricting transfers |
| **Instructor Management** | 9 | Deactivating instructor accounts, substitute instructors, instructor rates, instructor unavailability requests |
| **Notifications & Automations** | 14 | Missing reschedule confirmations, wrong notifications, reminder timing, morning reminders sent in error |
| **Orders & Products** | 8 | Unpaid product orders, QR codes on product orders, voucher/pass tracking, service reset |
| **Registration Transfers & Copies** | 10 | Transfer search UX, payment preservation during transfer, copying registration errors |
| **Widgets & Publish Settings** | 10 | Embed code filtering, interest collection form, booking form 404, capacity display |
| **Payment Schedules & Membership** | 8 | Membership plan creation, installment display mismatch, retroactive membership slowness |
| **Extra Fields & Forms** | 4 | Key-value mismatch in extra fields, adding custom fields to registration form |
| **Holidays & Public Holidays** | 3 | Incorrect public holidays in system, holiday region settings per location |
| **Exports** | 2 | Export date range inversion, .numbers format issues on Mac |
| **Login & Account** | 6 | Account deletion, account verification, instructor login after email change |
| **Onboarding & Sales** | 10 | Pre-sales inquiries, onboarding follow-ups, partnership proposals, pilot setup |
| **Blocks (Term Segments)** | 3 | Block capacity limits, attendance hidden when block changes, block display in registration |
| **Services** | 2 | Service reset feature, zero-stock display for services |
| **Misc / Unclassifiable** | 6 | Spam, security emails, internal forwarding, non-Zooza issues |

---

## Questions Customers Asked (Generalized, English)

### Course & Group Setup

1. How do I bulk-delete courses that have no registrations or groups?
2. How do I move a group from one programme/course to another?
3. When copying a group, an error appears because the original had a deleted payment schedule. How to fix?
4. A group with online registration enabled does not appear on the website. What is wrong?
5. How do I archive a course and what happens to groups inside it?
6. How do I change the price for new registrations without affecting existing ones?
7. Why does the "interest collection" (group interested) form not work on my course?
8. Sessions disappeared from a course this week -- what happened? (Related to holiday auto-skip.)
9. How do I set up an event (e.g. a gala/ball) as a purchasable item in Zooza?
10. Why does the group show as ending when it still has active sessions?

### Attendance & Replacements

1. A student was marked "did not attend" instead of "excused" -- replacement hours were not generated. What is the correct attendance state?
2. Replacement hours between different franchise companies stopped working. How to troubleshoot?
3. After changing the block on a group, attendance records for previous blocks disappear or show "hidden". Why?
4. How do I add an individual make-up session for a student without moving them out of their regular group?
5. Can a student re-enroll onto the session they previously cancelled from, after already booking a replacement?
6. What does the "extra capacity for replacements" setting (e.g. +1) mean at the global vs. group level?
7. Sessions with no attendance requirement still show as "unclosed attendance" on the Dashboard. Can this be fixed?
8. How does the "did not come" attendance state get set automatically (e.g., when client logs in after the cancellation window)?
9. Can I allow adding a payment note in the attendance view even when the registration is only partially paid?

### Calendar Display & Filtering

1. Calendar on our website shows a free slot when a client cancels, but the group is still full. Can it show group capacity instead of session capacity?
2. Names are not displaying on calendar sessions -- is this a connectivity issue?
3. Instructor names are missing from the calendar on one franchise account. Why?
4. Archived courses still appear in calendar filters. Can they be hidden?
5. How does the calendar widget handle cancelled/rescheduled sessions visible to logged-in clients?
6. The receptionist role shows a daily calendar view only. Can we get a weekly view?
7. Why do inactive billing periods appear in the calendar filter dropdown?

### Client Management & Data

1. How do I create a new client manually (not through the registration form)?
2. How do I change the client (parent) on an existing registration?
3. A client has two accounts (duplicate). How do I merge them or move payments?
4. How do I find a client who purchased a voucher and check if it has been used?
5. A client's emails are bouncing because their mailbox is full. How does Zooza handle this?
6. I need to change a client's email address. Can I do it myself or does support need to do it?
7. Is the phone number visible on the session attendance screen? How do I customize which client fields are shown?
8. How does Customer ID work across franchise accounts when transferring a child?

### Profile / Parent Portal

1. Clients cannot log in to their profile -- they do not receive the login code.
2. After accepting GDPR consents, the page keeps returning to the consent screen. What is happening?
3. A client sees outdated data (old replacement options) in their profile. How to clear cache?
4. The profile widget on our website confuses clients -- they think it is a separate system. How to explain?
5. Clients see their own cancellations in the calendar but others do not. Is this correct?
6. The "sign back onto this session" button in the parent profile does not work. What conditions are required?
7. How does a Google Meet link work within the client profile for online sessions?

### Roles & Permissions

1. Which role should I assign to an instructor who also handles replacement bookings with clients?
2. Can I hide instructor pay rates from the "main instructor" role so they cannot see colleagues' rates?
3. The main instructor role cannot see Courses in the left menu after an architecture change. Is this expected?
4. How do I restrict a role so the user cannot transfer registrations?
5. Which role allows calendar access but not financial data visibility?
6. How do I properly adjust permissions for roles in Settings > Team > Access?
7. When deactivating a departing instructor, should I delete or just change their role to preserve data?

### Instructor Management

1. How do I delete/deactivate an instructor's account?
2. A substitute instructor cannot send emails to students on the session they are covering. Is this by design?
3. When setting a rate for a second instructor on a session, the system shows "false" instead of the payout. Why?
4. The system sends instructor unavailability approval requests to the wrong person. Who controls the recipient?
5. How do instructor rate types work (e.g., per-session, per-student, per-hour)?

### Notifications & Automations

1. Why did clients not receive a confirmation email after rescheduling a session themselves?
2. The system sent an incorrect notification (morning reminder instead of upcoming-session notice) to clients. What happened?
3. Can I change the time of day when payment reminders are sent? (Currently sent at midnight.)
4. How do I control whether session reminder notifications are enabled/disabled per course?
5. Emails sent from the calendar view go to waitlisted clients too. Should they be excluded?
6. How do trial lesson automations work (auto-send registration link after trial ends)?
7. A client was sent an SMS meant for all active clients by mistake. How did that happen?

### Orders & Products

1. Where can I see unpaid product orders? There is no dedicated report for product payment status.
2. Can a QR payment code be added to product order emails (like it exists for course registrations)?
3. How do I track whether a purchased voucher/pass has been used?
4. How do I restore a deleted order to recover product capacity?
5. Dynamic tags do not populate in order-related email templates. Is this expected?
6. How does the "reset sales" button on services work?

### Registration Transfers & Copies

1. When transferring a registration between groups, the search field does not remember the previous filter. Can this be improved?
2. During a transfer, I forgot to check "Do not change payments" and the system applied a new payment schedule. How to fix?
3. When copying a registration, the price was calculated incorrectly (a block was counted twice). Is this a bug?
4. The transfer search field searches by group name, not course name. This is confusing.
5. How do I transfer a trial registration to a different session time?

### Widgets & Publish Settings

1. The embed code on my website shows all courses instead of a filtered set. How do I fix the filter syntax?
2. Clicking "Buy" on a product in the profile widget leads to a 404. Where is the URL mismatch?
3. How do I hide the number of enrolled children per session from the public widget?
4. How do I change the base URL used in dynamic tags within the widget/publish settings?
5. Interest collection (group interested) widget does not appear even though it is enabled. What setting am I missing?

### Holidays & Public Holidays

1. The system treats certain dates (e.g., 1 Sep, 17 Nov) as public holidays, but they are no longer holidays. Can this be corrected?
2. How do I set holiday/vacation region per location so that only the correct regional holidays apply?
3. Spring holidays are configured as 3 weeks but we only need 1 week for our region. How to narrow it?

### Exports

1. I exported invoices but the file was empty because I swapped the from/to dates. The system did not warn me.
2. Export files open incorrectly in Apple Numbers. Using Google Sheets resolves the formatting.

### Login & Account

1. After correcting an instructor's email address, they did not receive a login link. What is the process?
2. How do I delete my Zooza account entirely?
3. A new account was created but not verified. How does verification work?
4. A client keeps creating new accounts on zooza.online instead of logging in through our website widget.

### Blocks (Term Segments)

1. Can I set capacity limits per block independently from the group capacity?
2. When I change a student's block assignment, their attendance for previous blocks shows as "hidden". Why?
3. New registrations do not show block assignment in the registration detail view.

---

## Common Patterns and Recurring Issues

### 1. Replacement Hours (Make-up Lessons) Are the Top Pain Point Outside Payments
Replacement logic is complex: attendance state must be "excused" (not "did not attend") to generate a replacement. Cross-franchise replacements require matching location/settings. The "extra capacity" setting is misunderstood. Several tickets stem from clients unable to book replacements in their profile due to state or capacity mismatches.

### 2. Role and Permission Confusion Is Widespread
Admins struggle to find the right role for instructors, assistants, and managers. Common friction: "main instructor" role changed over time, some menu items (like Courses) were removed, and there is no granular permission editor -- roles are predefined packages. Hiding pay-rate visibility from certain roles is frequently requested but not supported.

### 3. Calendar and Widget Display Mismatches
The calendar widget shows per-session capacity while admins expect per-group capacity. Archived courses appearing in filters, missing instructor names, and sessions vanishing due to holiday auto-skip all cause confusion. The distinction between what a logged-in client sees vs. a public visitor is not well understood.

### 4. Notification Reliability and Timing
Several tickets report clients not receiving expected notifications after rescheduling. One incident involved a system bug sending the wrong notification type. The inability to control the time-of-day for payment reminders (they go out at midnight) is a repeated complaint.

### 5. Transfer and Copy Workflows Have UX Gaps
The transfer dialog resets filters between participants, the search works on group names (not course names), and forgetting to check "Do not change payments" silently applies a new payment schedule. A copying bug double-counted a block in the price.

### 6. Profile and Login Access Issues Are Frequent
GDPR consent loops, cache-related display problems, and clients failing to receive login codes are the main profile issues. Clients sometimes confuse zooza.online (the SaaS homepage) with their school's profile widget.

### 7. Holiday Configuration Is Region-Dependent but Not Obvious
Holidays are tied to location region settings. If a location does not have the correct region assigned, the wrong holiday calendar applies, causing sessions to be skipped unexpectedly.

### 8. Extra Fields and Form Customization
Key-value mismatches in extra fields (displayed value differs from stored value) and confusion about where to configure extra fields (course-level settings) appear multiple times.

### 9. Orders/Products Module Is Less Mature
No dedicated unpaid-orders report, dynamic tags do not work in order emails, and QR codes were missing from product purchases (since added). Admins treat products as secondary to registrations and struggle to find order data.

### 10. Onboarding and Pre-Sales Follow-Up
Multiple tickets are onboarding nudges (account created but not configured). Pre-sales questions focus on: family accounts, credits/memberships, age restrictions, multi-location support, and available currencies.
