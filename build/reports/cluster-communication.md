# Communication Cluster -- Support Conversation Analysis

**Source:** `build/reports/ingest-condensed.jsonl`
**Filter:** tags containing `communication`, `notification`, `emails`, `whatsapp`, `dynamic tags`, or `text`
**Records matched:** 37
**Date range:** 2025-11-07 to 2026-02-10

---

## Frequency Table by Sub-category

| Sub-category | Count | Description |
|---|---|---|
| Dynamic tags not populating / wrong data | 10 | Tags in email templates render blank, show wrong values, or pull data from wrong source |
| Email delivery failures | 6 | Emails not arriving (full inbox, spam, rejected) |
| Notification timing and scheduling | 5 | When notifications fire, changing send time, premature reminders |
| Email template setup and customization | 5 | Creating/selecting custom templates, system vs. user templates, per-course templates |
| Session reminder misconfiguration | 3 | Reminder emails with broken unsubscribe links, wrong session info |
| Payment reminder emails (content/logic) | 3 | Clients receiving reminders despite having paid, confusing reminder wording |
| WhatsApp integration | 1 | Inquiry about WhatsApp for Business availability |
| Email language / translation | 1 | System does not translate user-composed emails |
| Suspicious / phishing email from system | 1 | Client received email that appeared to come from system but was phishing |
| Client messages not visible in system | 1 | Inbound client messages silently dropped by engine |
| Widget button label / UI text | 1 | Request to change button text in client-facing profile widget |

---

## Specific Questions Customers Asked

### Dynamic Tags

1. Why does the dynamic tag `COURSE_TIME` show the wrong time for a make-up (replacement) lesson? It pulls from the primary group, not the rescheduled session.
2. Why did the dynamic tag `QR_CODE` not render in the confirmation email while other tags populated correctly?
3. Dynamic tags in emails sent during a ~60-minute service outage were blank. How do we resend corrected emails?
4. Why does `COURSE_DATE_DAY` / `COURSE_TIME` show incorrect info when the course uses blocks? The tag pulls from the first session in the group, not the block the client registered for.
5. Why are dynamic tags not populated in order confirmation emails? (Answer: dynamic tags do not work for orders, only registrations.)
6. The notification template for waiting-list spot availability used the wrong tag (`COURSE_NAME` instead of `EVENT_COURSE`). How to fix?
7. Is there a dynamic tag for the online meeting link assigned to a group, so it can be included in email templates? (Answer: not yet, planned.)
8. Can a dynamic tag for block-specific dates be created so that clients in different blocks receive the correct session info?

### Email Delivery

9. Emails to a client are not arriving. What is wrong? (Answer: recipient mailbox is full -- `inbox out of storage space`.)
10. System is not sending emails to certain clients. (Answer: same full-inbox issue; client must clear mailbox or change address.)
11. A client's email provider (seznam.cz) marks Zooza emails as spam. How to resolve? (Answer: client likely flagged as spam; they must whitelist the sender.)
12. I cannot send an email from the app -- it fails with a validation error. (Answer: bug in email address validation; fixed in app update, clear cache.)
13. Client says they are not receiving any system emails (login codes, confirmations, notifications). Where to start troubleshooting?
14. After account deactivation, clients still received notifications. Why?

### Notification Timing and Scheduling

15. Payment reminder notifications are sent at midnight. Can the send time be changed? (Answer: not configurable; notifications are processed overnight.)
16. Can we add a third payment reminder notification? (Answer: no, but a "pre-payment" (zeroth) notification before the payment obligation is created can be enabled, giving effectively three touchpoints.)
17. Why did a session reminder go out for a course that no longer has any active groups? (Answer: groups existed at send time but were deleted afterward.)
18. How do automated payment reminders work when using payment templates? When exactly does the reminder fire?
19. Why are session reminder notifications sometimes delayed? (Answer: they are queued and processed in batches; check the event notifications report page.)

### Email Templates

20. The system payment-confirmation email is generic. Can it be customized per course? (Answer: it is a system email and cannot be changed, but you can set up card-only payment and attach a custom communication template to the course.)
21. How do I create and use a custom email template for a specific course's registration confirmation?
22. Why can I not select my custom template when sending an email? (Answer: user-created templates are under "User templates," not "Saved communication templates" -- different dropdown entry point.)
23. A registration confirmation email was not sent for a copied (manual) registration. Why? (Answer: copied registrations do not trigger automatic confirmation; it must be sent manually.)
24. Where in the system can I review which emails were sent to a client and verify that dynamic tags rendered correctly? (Answer: check sent emails on the registration's communication tab; note that in the sent view, tags may display in raw form even if delivered correctly.)

### Payment Reminders (Content / Logic)

25. Clients received a payment reminder even though they already paid. Why? (Answer: the notification was a "future installment" notice sent before the installment was created, not a late-payment reminder. The timing mismatch occurs when auto-pairing has not yet processed the bank transaction.)
26. A payment reminder email contains a sentence we never added. Where did it come from? (Answer: it is a course-level setting for pre-start payment tracking; it can be disabled in Course > Price and payments settings.)
27. Can we disable the "you will receive a payment request" pre-notification entirely? (Answer: system rework in progress to give control over this.)

### Session Reminders

28. The unsubscribe/cancel link in the session reminder email does not work. (Answer: the template had an incorrect dynamic tag for the link; support corrected it.)
29. Session reminder shows the wrong location (online vs. physical). How is the location determined? (Answer: it comes from the session-level location setting; if one session is online, its reminder will show online.)

### WhatsApp

30. Is WhatsApp for Business integration available? (Answer: limited beta, offered free to selected customers; will be part of Zooza Pro package after general release.)

### Other

31. Zooza does not translate the text of emails composed by the admin. Only system/template strings are localized. Is auto-translation planned?
32. A client received a suspicious email that appeared to come from the system. Was it actually sent by Zooza? (Answer: no, it was a phishing attempt; the email was not in Zooza's sent logs.)
33. Inbound messages from a client are not showing in the system. (Answer: the message engine drops unrecognized attachments or content flagged as unsafe.)
34. Can the button label "Sign back up for this session" in the client profile widget be changed?

---

## Recurring Patterns and Issues

### 1. Dynamic tags are the top pain point
Ten of 37 conversations involve dynamic tags rendering incorrectly or not at all. Root causes fall into three buckets:
- **Tag/source mismatch:** `COURSE_TIME`, `COURSE_DATE_DAY`, and `COURSE_PLACE` pull from the primary group or its first session, which is wrong for replacement lessons, blocks, or multi-session courses.
- **Service outages:** A dynamic-tag rendering outage (Jan 21-22, 2026) generated at least four separate tickets across different customers.
- **Incorrect tag in template:** Admins (or initial setup) place the wrong tag in a template (e.g., `COURSE_NAME` instead of `EVENT_COURSE`), and the error is only noticed when clients complain.

**KB gap:** There is no clear reference doc explaining which dynamic tags are available, what data source each pulls from, and known limitations (e.g., blocks, orders, replacements).

### 2. Email deliverability confusion
Six tickets relate to emails "not arriving." In every resolved case, the cause was on the recipient side (full mailbox, spam filter, email marked as unwanted). Customers do not know how to verify delivery from the Zooza side or how to advise their clients.

**KB gap:** A troubleshooting guide for email delivery (check sent logs, common bounce reasons, whitelisting instructions) would reduce ticket volume.

### 3. Notification timing is not configurable
Multiple customers asked to change when payment reminders and session reminders are sent (e.g., not at midnight). The answer is consistently "not available." This is a recurring feature request.

### 4. Template selection UX is confusing
Customers struggle to find their own custom templates vs. system templates. The distinction between "Saved communication templates" and "User templates" is not intuitive.

### 5. Copied/manual registrations do not trigger automatic emails
When an admin copies a registration or creates one manually, the system does not send a confirmation email automatically. This catches customers off guard.

### 6. Payment reminder logic is misunderstood
Customers confuse the "upcoming installment" pre-notification with a "late payment" reminder. When a client has already paid but auto-pairing has not yet run, they receive what looks like a dunning email. This causes client frustration.

---

## Recommendations for KB Content

1. **Create or expand:** `content/guides/dynamic-tags.md` -- add a complete tag reference table with data source, supported contexts (registration, order, replacement), and known limitations.
2. **Create:** `content/troubleshooting/email-delivery.md` -- step-by-step guide for verifying delivery, common bounce codes, whitelisting, spam filter advice.
3. **Expand:** `content/guides/message-templates.md` -- clarify system vs. user templates, where each appears in the UI, and how to assign templates to specific courses.
4. **Expand:** `content/guides/automatic-payment-reminders.md` -- explain the difference between pre-payment notification, payment-due notification, and late-payment reminder; clarify timing.
5. **Add FAQ entries:**
   - "Why do dynamic tags show wrong data for replacement lessons?"
   - "Why did my client not receive the confirmation email for a manual registration?"
   - "Why does the payment reminder go out even though the client already paid?"
