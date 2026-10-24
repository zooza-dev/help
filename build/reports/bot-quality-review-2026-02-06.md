# Bot Quality Review — Zooza Intercom AI Chat (Feb–Jun 2026)

---

## Executive Summary

**Review scope:** 219 Intercom conversations, February 18 – June 23, 2026

**Overall finding split:**
- 148 issue findings (67.6%)
- 71 positive findings (32.4%)

**Issues by type:**

| Type | Count | % of issues |
|------|-------|-------------|
| wrong_answer | 63 | 43% |
| escalated_no_help | 37 | 25% |
| incomplete | 38 | 26% |
| account_specific_guessed | 10 | 7% |

**Issues by severity:**

| Severity | Count |
|----------|-------|
| High | 37 |
| Medium | 80 |
| Low | 31 |

**Five critical patterns identified:**

1. **Language change navigation** — a single wrong fact ("click Zooza logo, top left") repeated in **10+ conversations across 5 months**, including being embedded in a manager training manual. The most damaging repeating error in the dataset.
2. **Fabricated UI paths and API surfaces** — in at least 8 distinct cases the bot described navigation paths, settings, or code properties that do not exist (window.ZOOZA style, gift voucher expiration field, email attachment editor, re-enroll button, etc.).
3. **Claimed to see the customer's screen** — in at least one confirmed case the bot stated "I see you selected class SOROBAN WEEKEND" — a factually false statement that erodes trust.
4. **Escalation without guidance** — in ~37 conversations the bot offered to connect to a human without providing any general educational content, leaving customers with nothing while they waited. In most cases the human agent's first reply resolved the issue in one message.
5. **Zero KB coverage for recurring topics** — at least 12 high-frequency support topics (waitlist types, deleted registrations, make-up causes, inbound payment ignored status, auto-continuation trigger, etc.) had no accurate bot answer at all.

---

## High Priority Fixes

`wrong_answer` findings rated `high` severity — these actively mislead customers into wasted effort or wrong configuration. Fix these before anything else.

---

### 1. Language change navigation (10+ occurrences — most repeated error)

**What the bot says:**
> "Click the Zooza logo in the top-left corner of the dashboard. At the bottom of the menu you will see a language switcher."

**Occurrences:** April 14, April 17, April 20, April 22, April 25, April 26, May 25, June 6, June 22, June 23 — at minimum across convs 215473909714006, 215473954060464, 215473989450013, 215474016119619, 215474058388920, 215474069962065, 215474439121261, 215474599593207, 215474809131687, 215474794459051, 215473821765673, 215473827512018.

**Most damaging instance:** April 22 (conv 215474016119619) — the wrong path was written into a **manager onboarding training manual**, propagating the error to every new admin trained with that material.

**Variant error (June 23, conv 215474809131687):** When a customer mentioned seeing "Zooza MCP" at the bottom of the menu, the bot confirmed that is where the language switcher is. Zooza MCP is a separate AI integration feature, not a language setting.

**Correct answer:**
> Profile icon (top-right corner) → Account settings → Language

This applies to both desktop and mobile. There is no language switcher under the Zooza logo.

**Additional finding:** In conv 215474707453098 (June 15), the bot gave the **correct** path and was immediately overridden by human agent Katarina who gave the **wrong** path (logo, bottom of menu). This means the error exists in human agent knowledge as well as bot training — the source article must be fixed and the correct path communicated to the support team.

**KB fix required:**
- Update `Change the language in Zooza` article. Lead with the correct path, add an annotated screenshot, and add an explicit callout: "The Zooza logo in the top-left does not contain a language switcher."
- Audit every article that references language settings and correct any that cite the logo path.
- Communicate the correct path to all human agents via the team channel — at least one agent has the same misconception.

---

### 2. window.ZOOZA style property — fabricated API surface

**What the bot says:**
> "Add this JS before the embed code: `window.ZOOZA = { style: { select_height: 'auto', select_padding: '10px' } }` — this overrides the default styles and ensures the text is not cut off."

**Occurrence:** February 23 (conv 215473212557209)

**What is actually true:**
The `window.ZOOZA` object supports only `translations` and `print_debug`. There is no `style` property. Human agent Martin corrected this explicitly: "The AI agent gave you misleading information." Martin fixed the dropdown height from the backend by changing an inline style directly.

**KB fix required:**
- Update widget customization article: document exactly what `window.ZOOZA` supports (`translations`, `print_debug`) and explicitly state what it does **not** support (styling, layout).
- Add a clear section: "To change widget appearance, add CSS to your website. The JS embed configuration cannot control styling."

---

### 3. "Participant same as payer" button — system element vs custom field (2 occurrences)

**What the bot says:**
> "Go to Programmes → Edit Settings → Additional Fields and uncheck the field that creates the button — it is a custom additional field you can hide per programme."

**Occurrences:** March 29 (conv 215473686963241), March 31 (conv 215473713545046)

**What is actually true:**
This button is a **system-level UI element** added by Zooza in a product update, not a custom additional field. No such checkbox exists in Additional Fields. The human team adjusted it at the product level.

**KB fix required:**
- Add a guide explaining the `For children` programme setting and what it controls.
- Clarify which registration form elements are system-level (not configurable in Additional Fields) vs user-defined custom fields. Make this distinction prominent.

---

### 4. Bot claims to see the customer's screen

**What the bot says:**
> "I see you are on the Bookings page and you have the Create booking button in the top right."
> "I see you selected class SOROBAN WEEKEND."

**Occurrence:** March 17 (conv 215473511639201). Sources cited for these claims were marketing blog posts.

**What is actually true:**
The bot cannot see the customer's screen, current page, or account data. These statements are factually false.

**Fix required (bot behavior, not KB):**
- The bot must never claim to see the customer's screen, current selections, or account state.
- Add a disclaimer in the bot's opening message or system prompt: "I can answer general questions but cannot see your account, screen, or specific data."

---

### 5. Session reminder reactivation — wrong navigation path

**What the bot says:**
> "Go to Communication → Message templates to update the reminder settings."

**Occurrence:** March 19 (conv 215473537585362). Bot's first response pointed to payment reminder configuration — a completely different feature. Second response pointed to programme-level settings.

**What is actually true:**
The fix is at the **individual registration level**: Registration detail → Options tab → Reminder toggle. Programme-level settings control all clients globally, not a single registration.

**KB fix required:**
- Create article: "How to re-enable session reminders for a specific client" covering the Options tab toggle on individual registrations, and explicitly distinguishing this from programme-level reminder template settings.

---

### 6. Gift voucher expiration — non-existent admin UI

**What the bot says:**
> "Go to Orders → Order detail → Expiration section → manual adjustment to change the voucher expiry date."

**Occurrence:** April 21 (conv 215474008120549). Bot repeated this across four messages, each adding more fabricated UI detail.

**What is actually true:**
Human support confirmed: "Changing the expiry of a purchased product is not possible." Only Zooza staff can change it in the database. There is no editable Expiration field in Order detail.

**KB fix required:**
- Add FAQ: "Gift voucher / entry pass expiration on purchased orders cannot be changed by admins in the UI — contact Zooza support."
- Remove any implication in existing articles that Order detail has an editable Expiration field.

---

### 7. Deleted registrations — two separate wrong answers

**Error A — Wrong 30-day data loss claim (conv 215474031660130, April 23):**

Bot said: "Registrations deleted more than 30 days ago are permanently removed from the system."

What is actually true: Deleted registrations remain accessible **indefinitely** via the URL filter `#registrations?status=deleted`. Human agent Katarina corrected immediately.

**Error B — Directing to a removed UI filter (conv 215473921161344, April 15):**

Bot said: "Go to Bookings and filter by Status = Deleted."

What is actually true: The Deleted status filter was removed from the Bookings UI. The only access path is the URL fragment `#registrations?status=deleted`.

**KB fix required:**
- Update "Recover deleted sessions, classes, and registrations" to:
  - State the Status = Deleted filter was removed from the Bookings UI.
  - Document `#registrations?status=deleted` as the primary access method.
  - Clarify that deleted registrations are viewable indefinitely — not limited to 30 days. (The 30-day limit applies to Settings → Tools → Trash, which is for client records, not registrations.)

---

### 8. Waitlist types confused — enrollment vs make-up waitlist (2 occurrences)

**Error A — Wrong configuration path (conv 215474178700711, May 5):**

Bot directed a customer asking about the enrollment/capacity waitlist (poradovník do skupiny) to `Programmes → Settings → Make-up sessions → enable Make-up sessions waitlist`. Bot acknowledged these are separate features, then immediately directed to the wrong one.

**Error B — Wrong behavior described (conv 215474611327468, June 8):**

Bot said: "The waitlist is not automatic — admin must manually approve and change status from Waitlist to Enrolled."

The customer asked about the **make-up session waitlist** (poradovník na náhradky). For that waitlist, the system IS automatic: when a spot opens, all waitlisted clients are emailed simultaneously; the first to click the confirmation link gets the spot. The bot described the class capacity waitlist (poradovník do skupiny) which does require manual admin approval.

**KB fix required:**
- Create a dedicated article distinguishing the two waitlist types:
  - **Enrollment/capacity waitlist** (poradovník do skupiny): when a class is full; requires manual admin approval; configuration location X.
  - **Make-up sessions waitlist** (poradovník na náhradky): for make-up slots; fully automatic; system emails all waitlisted clients when a spot opens; first to confirm via link gets the spot; configuration location Y.

---

### 9. Disabling automated payment notifications — non-existent toggle

**What the bot says:**
> "Go to Settings → Payment Settings and turn off 'Notify before a scheduled payment is issued'."

**Occurrence:** May 5 (conv 215474179567915)

**What is actually true:**
Human agent Katarina confirmed explicitly: "Both emails are system messages that cannot be turned off." These notifications are by design and non-configurable by admins.

**KB fix required:**
- Update Automated Notifications overview to explicitly state: scheduled payment creation email and payment due date email are system messages — they cannot be disabled.

---

### 10. Auto-continuation email trigger — wrong event

**What the bot says:**
> "The auto-continuation email sends after the instructor marks the trial session as 'attended'."

**Occurrence:** May 7 (conv 215474206854763)

**What is actually true:**
Human agent Katarina corrected: the email is triggered **N days before the end of the billing period** (configured number of days). Trial attendance has no bearing on it.

**KB fix required:**
- Update auto-continuation / programme automations article: "The continuation email fires N days before the billing period end date. It is not triggered by trial session attendance."
- Include a worked example: last session May 10, reminder set to 2 days → email sends May 8.

---

### 11. Images in email templates — wrong capability claimed

**What the bot says:**
> "Yes, you can insert images into email templates in Zooza — go to Communication → Templates → open a template → insert the image into the body → Save."

**Occurrence:** June 1 (conv 215474531908459)

**What is actually true:**
Human agent Katarina confirmed: "Images cannot be inserted as in Gmail — you must upload the image to your website and paste only the link into the email." Katarina noted a colleague would enable image embedding later — confirming the feature was not available when the bot claimed it was.

**KB fix required:**
- Update "Message templates — images in emails" article: images must be hosted externally and linked into email body. Do not embed images directly.
- When image embedding ships, document it separately and mark the date.

---

### 12. Different payment plans per class — wrong flow described

**What the bot says:**
> "Open the class → Price & Payments → Apply payment template. Each class can have its own instalment schedule."

**Occurrence:** June 18 (conv 215474752148250). A human agent stepped in mid-conversation: "This is actually probably incorrect answer by our AI bot."

**What is actually true:**
Correct three-step flow:
1. Define payment plan templates in Team and Settings → Payments
2. Activate on the Programme (Price card)
3. Optionally disable individual plans at the class level

There is no standalone "Apply payment template" button at the class level, and the programme-level activation step cannot be skipped.

**KB fix required:**
- Update payment templates article to document the full three-step flow. Make the programme activation step visible and non-optional in the instructions.

---

### 13. Lead groups showing as paid — wrong diagnosis

**What the bot says:**
> "Clients showing as 'paid' are likely duplicate registrations from parents who didn't complete payment — find and delete the unpaid duplicates."

**Occurrence:** May 15 (conv 215474322754279)

**What is actually true:**
These were lead groups (zberne košy — collection groups without sessions and no debt attached). They show as "paid" because no debt exists, not because payment was made. Human confirmed: expected behavior.

**KB fix required:**
- Create or update lead groups article: "Lead groups show as paid because they have no associated debt. This is expected behavior, not a payment error. To generate debt, convert the group from Lead to Fixed class."

---

### 14. COURSE_PLACE dynamic tag — false constraint

**What the bot says:**
> "COURSE_PLACE requires a room to be set on the class. If the room field is empty the tag will return blank."

**Occurrence:** May 14 (conv 215474304543326). Customer added unnecessary rooms as a result.

**What is actually true:**
Human confirmed the tag works without a room. The blank return in this case was a data sync / materialization bug.

**KB fix required:**
- Update dynamic tags article: COURSE_PLACE works without a room. If the tag returns blank, the likely cause is a data sync issue — not a missing room.

---

### 15. Auto-continuation — wrong advice for "no groups available"

**What the bot says:**
> "The 'No groups available' message means no groups exist to continue to — create a manual booking via Bookings → New booking."

**Occurrence:** May 19 (conv 215474364973813)

**What is actually true:**
The message means the target group is **not enabled for auto-continuation**, not that no groups exist. Human enabled the group in continuation settings in one action. Manual booking creation would have created duplicates and bypassed the intended flow.

**KB fix required:**
- Add FAQ entry: "'No groups available' on the continuation screen means the target group is not enabled for auto-enrolment. Solution: enable the group in auto-enrolment settings. Do not create a manual booking — this duplicates the registration."

---

### 16. Attendance question classified as spam

**What happened:**
Customer Lucia Hoxha asked a legitimate question ("What does it mean when children are marked like this in attendance?") with a screenshot. The bot classified the message as spam because the customer's email footer contained promotional links to her coaching business. The question was never answered.

**Occurrence:** May 8 (conv 215474221012560)

**Fix required:**
- Adjust spam classification to prevent dismissal of questions containing marketing email footers.
- Create an attendance status icons article explaining what each marking means.

---

### 17. Widget shows available when class is full — wrong explanation

**What the bot says:**
> "This is a known phenomenon — widget shows 'available' even when group is full because it displays session capacity, not class capacity. Check Publish → widget → Calendar settings → verify occupancy display is set to class capacity."

**Occurrence:** June 23 (conv 215474808789884)

**What is actually true (per domain facts):**
The correct diagnostic path is always the **class/group settings**. The reason for capacity mismatch is always found there. Widget Calendar settings for occupancy display is not a cause.

**KB fix required:**
- Create or update "Why does the widget show spots available when the class is full?" — always check class/group settings first. Remove any mention of widget capacity display mode as a cause.

---

### 18. Negative balance meaning — inverted definition

**What the bot says:**
> "A negative balance on the booking means the payment was not completed or failed — there is still an outstanding amount to collect."

**Occurrence:** April 22 (conv 215474019377392). Generated 8+ unhelpful follow-up exchanges.

**What is actually true:**
In Zooza, a **negative balance means the client has credit (overpaid)**, not that they owe money. The bot's interpretation was the exact opposite.

**KB fix required:**
- Add KB content defining what positive and negative balances mean on a booking. This is a bot-indexed fundamental definition, not just an FAQ.

---

### 19. Payment import — "AI confidence" deflection

**What the bot says:**
> "The payment did not pair most likely because AI confidence was too low, or the booking is inactive."

**Occurrences:** May 16 (conv 215474330998087), April 1 (conv 215473732509418). Customers disproved both guesses with actual transaction data.

**What is actually true:**
In May 16, the real cause was the deduplication agent being overly aggressive — a known platform issue. "AI confidence" is not a user-actionable explanation. The bot cannot diagnose specific import failures without account access.

**KB fix required:**
- Add article: "Payment import failures — if the Matching Process Summary does not explain an unmatched payment, check the Inbound Payments queue (status: new or ignored). Contact support if the cause is unclear."
- Remove "AI confidence" as a user-facing explanation.

---

### 20. Widget payment summary text — wrong feature answered

**What the bot says:**
> "The most likely cause is an incorrect 'sessions per month' setting in the payment plan, which inflates the displayed price."

**Occurrence:** April 30 (conv 215474132699920). Customer had pasted the text they wanted to change and asked "where do I change this text?"

**What is actually true:**
The customer was asking about the location of a UI string, not a price calculation complaint. The bot misread the question entirely.

**KB fix required:**
- Create FAQ: "How to change text displayed in the booking widget payment summary" — this is changed via widget translations or Programmes → Online Booking → Customize Booking Form, not via payment plan settings.

---

## Missing KB Content

These are `escalated_no_help` and `account_specific_guessed` findings — the bot either offered no guidance before escalating, or invented an account-specific cause it had no basis for.

---

### A. Account deletion without exploring the customer's actual need

**What customers say:** "I want to delete my account."

**What the bot did (March 10, conv 215473417248780):** Accepted the deletion intent at face value and gave support form instructions with no follow-up question.

**What actually happened:** The customer was looking for class passes / pay-as-you-go — a feature that exists in Zooza. Human agent Michal caught it in a follow-up and saved the customer. Near-churn over a solved product need.

**Fix required (bot behavior):**
- Before accepting account deletion intent, ask: "What were you looking for that you couldn't find?" Surface the most commonly missed features (class passes, pay-as-you-go, blocks).
- This is a bot prompt / behavior rule, not just a KB article.

---

### B. Instructor days off / blocking availability

**What customers say:** "How do I block my availability for two days?" / "I need two days off."

**What the bot did (March 11, conv 215473435448013):** Did not map this to any Zooza feature. Described the generic support ticket submission system instead.

**KB fix required:**
- Add FAQ: "How do I cancel sessions on specific dates as an instructor?" and "How to block my availability / take time off in Zooza."
- Map "days off", "time off", "unavailable" as session cancellation / bulk edit / availability setting intents.

---

### C. Make-up session locations not showing in widget — multiple real causes

**What customers say:** "Why can't clients see make-up slots for a specific location?"

**Bot failures (convs 215473826889641, 215473803474980):** Invented widget filter syntax explanations; directed to online booking visibility settings. Neither helped.

**Actual causes confirmed by human agents:**
1. Class group has not started yet — make-up slots only appear 4 days before the **first session** of that group
2. Group is fully booked with no extra make-up capacity
3. Make-up waitlist not enabled in programme settings
4. Cancellation deadline passed (midnight cutoff) — client sees "Did not attend" only, not a cancel option

**KB fix required:**
- Update make-up sessions FAQ with a "Why can't clients see make-up slots?" section covering all four causes.
- Add explicit note: make-up slots for a new class only appear from **4 days before the first session**, not 4 days from the date of cancellation.

---

### D. Class showing as full after cancellations

**What customers say:** "Why does my class still show 10/10 even though students cancelled?"

**What the bot did (April 11, conv 215473864184270):** Offered to escalate with no general explanation.

**What human agent explained:** The capacity display counts total course registrations vs class capacity — attendance drops do not reduce the count. Releasing a spot requires cancelling or deleting the booking, or enabling the make-up waitlist.

**KB fix required:**
- Add FAQ: "Why does my class still show as full after students cancelled?" with the above explanation and the two ways to release spots.

---

### E. Inbound payments — "Ignored" status unexplained

**What customers say:** "45 payments have moved to ignored status."

**What the bot did (May 5, conv 215474188136690):** Offered to escalate without explaining what "ignored" means.

**What human agent explained:** The deduplication robot marks payments as "ignored" when it detects a possible duplicate. Admins can manually review ignored payments and pair valid ones.

**KB fix required:**
- Create article on inbound payment statuses covering "ignored" status: what it means, why it occurs (deduplication agent), how to manually review and pair valid payments that were incorrectly flagged.

---

### F. Retention Responses — "Mark as checked" button unknown

**What customers say:** "What does the 'Mark as checked' button do in Retention Responses?"

**What the bot did (March 17, conv 215473516470805):** Had no knowledge of this UI element. Referenced a developer API endpoint instead of user-facing help content.

**KB fix required:**
- Create Retention Responses article covering: what response statuses mean, what "Mark as checked" does (presumably marks a response as reviewed by the admin), and how to use the retention response workflow.

---

### G. Booking confirmation email missing — resend path not known

**What customers say:** "The confirmation email didn't send — how do I resend it?"

**What the bot did (June 15, conv 215474707801963):** Asked the customer to re-run the full registration flow to test, rather than explaining how to resend from the booking.

**Correct path (from Katarina):** Bookings → open the booking → Communication tab → select "Booking Confirmation" template → send.

**KB fix required:**
- Create or update "How to resend a booking confirmation email manually" — this should be the first suggestion when automated email is reportedly missing, not flow re-testing.

---

### H. Session count totals higher than expected

**What customers say:** "My group shows 44 sessions but I only count 40."

**What the bot did (May 31, conv 215474516669566):** Escalated with no explanation.

**What human agent explained:** Cancelled/unplanned sessions remain in the total count. They can be bulk-deleted using a `status=unplanned` filter.

**KB fix required:**
- Add FAQ: "Why does my session count show more sessions than I can see?" — cancelled/unplanned sessions remain in the total. Filter by status=unplanned and bulk-delete.

---

### I. Archived class still in instructor pay report

**What customers say:** "Why does an archived class still appear in the instructor pay report?"

**What the bot did (June 10, conv 215474638757654):** Escalated immediately.

**What human agent explained:** Archiving is for historical preservation — sessions remain in pay reports to capture all taught hours. To exclude future sessions, delete them before archiving.

**KB fix required:**
- Add FAQ: "Why does an archived class still appear in the instructor pay report?" — archiving preserves history; delete future sessions before archiving if you want to exclude them.

---

### J. Google review request email — trigger conditions unknown

**What customers say:** "Why wasn't the review request email sent after the session?"

**What the bot did (April 13, conv 215473883017543):** Alerted the team and escalated without providing any explanation.

**KB fix required:**
- Add FAQ: "When does the Google review request email send?" — cover required conditions (session marked complete, reviews module enabled, client email active, not previously reviewed).

---

### K. Session reminders not resent after reschedule

**What customers say:** "The notification wasn't sent after I rescheduled the session to a different date."

**What the bot did (May 26, conv 215474447610941):** Generic email delivery troubleshooting — not relevant.

**What human agent (Katarina) explained:** The morning notification is not resent for the new date if it was already sent for the original date. Workaround: manual send from Communication.

**KB fix required:**
- Add FAQ: "What happens to session reminder emails when a session is rescheduled?" — system does not automatically resend if already sent for the original date. Workaround: send manually from the session's Communication tab.

---

### L. Payments requiring manual matching — monitoring location unknown

**What customers say:** "How do I get notified when a payment needs manual review?"

**What the bot did (May 28, conv 215474478152842):** Correctly said no dedicated notification exists, then escalated without showing where unmatched payments can be monitored.

**What human agent showed:** Payments dashboard and `#payments/inbound/list?payment_status=new` filter.

**KB fix required:**
- Add section to "Inbound payments — setup and pairing": explain where to monitor payments requiring manual review (dashboard, Payments received filter for status=new) and how to act on them.

---

### M. Widget shows available but registration fails

**What customers say:** "A slot shows available in the widget but my client can't book it."

**What the bot did (May 29, conv 215474493270366):** Acknowledged it couldn't see account data, then provided no general guidance at all.

**Per domain facts:** The reason is always in the class/group settings — class capacity (including trial registrations), session-level capacity, registration cutoff windows.

**KB fix required:**
- Create or update "Widget shows class as available but registration fails" troubleshooting — covering all three causes with where to find each setting.

---

### N. Zero-context forwarded messages — bot invents a scenario

**What happened (May 5, conv 215474178028698):** A message forwarded to support with no problem description ("forwarding this request to support") prompted the bot to invent a duplicate-unpaid-booking scenario. Human agent found a completely different issue.

**Fix required (bot behavior):**
- When a message contains no problem description, the bot must ask what the specific issue is before guessing any cause.

---

## Incomplete Answers (Medium Priority)

These are `incomplete` findings where the bot was partially correct but omitted a critical piece of information, causing customer confusion or extra effort.

---

### 1. Make-up session email behavior — approval mode distinction missing

**Gap:** Bot initially stated clients receive an email on submitting a make-up request. When pushed back, it reversed. The correct answer depends on approval mode — which was never stated.

**KB fix:** Update make-up sessions guide: "(1) Manual approval mode: no email on submission; email sends after instructor approves. (2) Auto-approval mode: email sends immediately on sign-up."

---

### 2. Cancellation limit — first diagnostic step omitted

**Gap (April 28, conv 215474091835264):** When clients could only see "Did not attend" and not a cancel option, the bot explained attendance statuses but missed the root cause: the cancellation deadline setting.

**KB fix:** Update cancellation and make-up guides: "If clients only see 'Did not attend' and not a Cancel option, check the cancellation limit setting in Settings → General first."

---

### 3. Client not receiving reminders after transfer — escalated without checking profile

**Gap (April 29, conv 215474105351434):** Bot escalated. Human resolved in one message: the client had individually unchecked "Send reminders before sessions" in their profile.

**KB fix:** Add to Automated Notifications troubleshooting: "If one client is not receiving reminders while others are, check the client's profile → notification preferences."

---

### 4. Sibling discount applying to single-child re-enrollments

**Gap (May 6, conv 215474201914931):** Bot repeated "no content on this topic" four times. Human (Martin) resolved with specific guidance: billing periods separate groups so sibling discount is evaluated per period.

**KB fix:** Create article on configuring sibling + loyalty discounts together — specifically covering how billing periods affect sibling discount evaluation, and how to prevent single-child re-enrolments from incorrectly triggering sibling pricing.

---

### 5. Tolerance period — wrong field name, definition risk

**Gap (June 8, conv 215474613950624):** Bot cited "Počet dní pre vystavenie splátky" (days for invoice creation) as the tolerance period field — likely the wrong setting. The critical fact: tolerance period does NOT change payment due dates; it only changes when status shifts from Waiting to Unpaid.

**KB fix:** Add dedicated tolerance period FAQ: exact field name and location; explicit statement that it is a grace window only and does not shift any payment due date.

---

### 6. Programme type mismatch causing missing automated emails

**Gap (May 5, conv 215474179811201):** Bot gave standard template-assignment troubleshooting. Actual cause: programme was set to single-session type instead of recurring, which prevented automated notifications from firing.

**KB fix:** Update email delivery troubleshooting to include "programme type mismatch" as a cause of missing automated emails.

---

### 7. Make-up credits valid but no sessions visible — cancellation deadline the most common cause

**Gap (May 5, conv 215474184636218):** Bot correctly pointed to MATKO diagnostic tool but listed possible causes that omitted the most common one: the cancellation deadline has passed (typically 24 hours before session start), so the credit is valid but no sessions are bookable.

**KB fix:** Update make-up sessions FAQ: prominently list the cancellation/sign-up deadline as the **most frequent reason** credits are valid but no sessions appear. Include the admin workaround: change attendance status to "Did not attend" and back to "Cancelled" to regenerate a fresh credit.

---

### 8. Dynamic tags — context limitation not disclosed

**Gap (May 14, conv 215474309140037):** Bot escalated without explaining that session-context tags (COURSE_PLACE, COURSE_TIME, etc.) only work in automatic sends triggered by a session event — they have no context in manual sends.

**KB fix:** Update dynamic tags article with a table or note identifying which tags require automatic send context and cannot be used in manual sends.

---

### 9. New Tasks panel — new feature treated as cache bug

**Gap (May 1, conv 215474146027245 and related):** A newly released Tasks/Úlohy panel that appeared on first login was treated as a cache display bug and triggered five rounds of cache-clearing advice. The correct explanation: a new-feature welcome panel, dismissible by clicking X.

**KB fix:** Protocol change — when major UI features are released that generate support volume, publish a help article immediately. Bot should recognize new-feature onboarding panels as a distinct category, not a cache issue.

---

### 10. Preparing for next school year — marketing advice instead of product steps

**Gap (May 18, conv 215474342466706):** Bot cited marketing blog posts and gave generic marketing-language advice instead of Zooza product steps.

**KB fix:** Create "Prepare courses for next school year" guide covering: copy group with clients, use lead groups for interest collection, set up auto-enrolment for continuation invitations.

---

### 11. E-invoicing — roadmap omitted

**Gap (May 14, conv 215474304002743):** Bot correctly said e-invoicing is not yet available but omitted that Zooza plans to support it ahead of the SK 2027 mandate.

**KB fix:** Update or create FAQ: "Is e-invoicing supported in Zooza?" — state not yet available, mention the 2027 SK mandate and that Zooza plans to support it. Reference the existing SK e-invoicing article if it exists.

---

### 12. "Awaiting payment" vs "Unpaid" — no distinction documented

**Gap (March 20, conv 215473567215029):** Bot repeatedly claimed these labels are identical. Customer proved through filtering that they return different result sets. Bot never explained the actual distinction.

**KB fix:** Create or update "Booking payment statuses explained" covering each label — Unpaid, Awaiting payment, Partially paid, Paid — with the semantic difference between Unpaid and Awaiting payment clearly stated.

---

### 13. Make-up hours report — limitation not stated upfront

**Gap (March 25, conv 215473627056718):** Bot's final workaround was to open each booking individually — which the customer had already identified as unworkable.

**KB fix:** Add to make-up sessions guide: "There is currently no built-in filtered report for make-up sessions by location. The Calendar make-up report is branch-level only." State the limitation clearly at the start of that section.

---

### 14. Localization terminology — Courses = Programmes not documented

**Gap (March 30, conv 215473697811511):** Bot insisted "Programmes" must be in the UI even as the customer repeatedly confirmed she only sees "Courses." Human clarified: in CZ/RON market versions, the UI label is "Courses" for what help docs call "Programmes." Customer had the correct screen all along.

**KB fix:** Add localization note to the Programmes guide: in some market versions "Programmes" appears as "Courses" in the UI. Include a terminology table: Courses = Programmes, Groups = Classes, Lessons = Sessions.

---

### 15. Sibling discount evaluation per billing period

**Gap:** Related to issue 4 above. When clients re-enroll each term in new groups, billing periods mean the sibling count resets per period. The "disable discount combining" setting was also mentioned by the human agent as relevant.

**KB fix:** Cover in the same sibling discount article as issue 4.

---

## What the Bot Does Well

The 71 positive findings show genuine strengths to preserve and protect through future KB updates.

**Consistently accurate topics:**
- **Passwordless login / magic link flow** — Explained correctly and with good anticipation of follow-up (check spam, request new code, do not request twice)
- **Transfer vs copy booking** — Correctly distinguished, including the "Do not change payments" toggle and the informational-only price warning
- **Make-up credit limits** — Accurate explanation of the per-registration extra limit in booking Options
- **GoCardless vs email notification pairing** — Accurate comparison when not making fabricated bank-outage claims (the bank outage claim in March 13 was isolated)
- **Late booking midnight deadline** — Correctly warns that payment plans are auto-deleted at midnight if the late booking is not confirmed the same day
- **Holiday settings — three-level system** — Correctly explains system regional holidays, skip-at-creation rule, and custom holidays. Correctly warns that skip-holidays is non-retroactive.
- **Lead collection vs capacity waitlist** — Correctly distinguished when the question context was clear (April 23, conv 215474034050165)
- **Attendance history hidden after block transfer** — Accurate, with proactive export-before-transfer warning
- **MATKO diagnostic tool** — Correctly directed to it for make-up debugging (May 2, conv 215474151089006)
- **Entry pass (permanentka)** — Correct explanation of cross-booking credit deduction
- **QR code EPC/BCD format** — Correct technical explanation (confirmed verbatim by human agent Katarina)
- **SuperFaktura integration** — One-way sync direction, multi-company via billing profiles — accurate throughout
- **Refund via Stripe** — Correct step-by-step including the "Administrative refund only" toggle warning
- **React widget installation** — Correct package name and configuration when customer specified TypeScript/React

**Good behavioral patterns observed:**
- Correctly acknowledging account-access limitations and pivoting to the best general guidance (conv 215474440902716 on cancellation limits — "I can't check specific settings for one course... check the Limit type and Number of days in Settings → Programmes")
- Correctly handling an off-topic support inquiry (March 27, conv 215473661324810 — Box.com billing email misdirected to Zooza support, correctly redirected to billing@box.com)
- Correctly declining to provide specific account data (April 1, conv 215473739020478 — "I cannot provide specific phone numbers from your groups because I don't have access to your account data")
- Correctly escalating without guessing when the scenario was account-specific (June 23, conv 215474808220038 — tolerance period and specific registration dates)

**One notable case where the bot was correct and a human agent gave the wrong answer:**
June 15 (conv 215474707453098) — the bot gave the correct language change path (profile icon, top right). Human agent Katarina immediately overrode this with the wrong path (click logo, bottom of menu). This confirms the language change error is not purely a bot problem and the human team needs the same correction.

---

## Full Issue List

| Date | Conv ID | Topic | Issue Type | Severity | KB Action |
|------|---------|-------|------------|----------|-----------|
| 2026-02-18 | 215473147881348 | Cancelling / correcting invoice / debit note | incomplete | medium | Create article on corrective invoices and credit note reversal workflow |
| 2026-02-22 | 215473201754115 | Missing Monday sessions | account_specific_guessed | medium | Add FAQ: "Why are sessions missing from my schedule?" with diagnostic steps, no guessing |
| 2026-02-23 | 215473212557209 | Widget styling — window.ZOOZA style property | wrong_answer | high | Update widget article: window.ZOOZA supports translations and print_debug only |
| 2026-02-25 | 215473245008397 | Where to find discount code settings | wrong_answer | medium | Create article: "Discounts and promotions in Zooza — what exists and where to configure it" |
| 2026-02-26 | 215473265442973 | Checking photo/video consent refusals | incomplete | low | Add FAQ: how to check consent status — UI path, not API |
| 2026-02-28 | 215473294505803 | Removing a field from the registration form | incomplete | low | Verify and document correct UI path for removing standard and custom fields |
| 2026-03-02 | 215473319050510 | Adding custom fields to registration form | wrong_answer | low | Update "Adding custom fields" article with precise navigation path |
| 2026-03-03 | 215473324290515 | Finding Zooza subscription invoices | incomplete | medium | Create article: "How to find your Zooza subscription invoices" with screenshots |
| 2026-03-06 | 215473373460441 | Customizing registration form fields | wrong_answer | high | Write canonical "Customizing the registration form" article with precise per-global-vs-per-course navigation |
| 2026-03-09 | 215473405171591 | Changing currency to ZAR | account_specific_guessed | low | Add article: "What currencies does Zooza support?" — definitive list by region |
| 2026-03-09 | 215473406381736 | Changing consent agree/disagree button text | wrong_answer | medium | Create article: consent text per course — not in global Settings → General |
| 2026-03-09 | 215473411503592 | Groups disappeared from calendar | wrong_answer | medium | Add FAQ: groups disappeared after creating a new group — calendar filter issue, not online registration status |
| 2026-03-10 | 215473417248780 | Account deletion — near-churn over missing feature | escalated_no_help | high | Bot behavior: ask "What were you looking for?" before accepting deletion intent |
| 2026-03-11 | 215473435448013 | Instructor requesting days off | escalated_no_help | medium | Add FAQ: cancel sessions on specific dates / block availability as instructor |
| 2026-03-11 | 215473435632805 | Dynamic tag for deposit-only QR code | incomplete | medium | Document QR_CODE tag behavior; confirm whether deposit-specific QR tag exists |
| 2026-03-13 | 215473465762025 | Difference between make-up and prenos náhrady | wrong_answer | high | Create article: actual distinction between standard make-up and prenos náhrady with screenshots |
| 2026-03-13 | 215473466095178 | GoCardless vs email notification reliability | wrong_answer | medium | Update comparison article; remove fabricated bank outage claim |
| 2026-03-14 | 215473478039102 | How to copy a registration | incomplete | low | Ensure Transfer and copy bookings article appears before blog posts in bot indexing |
| 2026-03-14 | 215473479211892 | How to send a generated invoice | incomplete | low | Update billing guide: clarify when invoices auto-send vs require manual sending |
| 2026-03-17 | 215473511639201 | Bot claims to see customer's screen | wrong_answer | high | Bot behavior fix: never claim to see screen, page, or account data |
| 2026-03-17 | 215473516470805 | What does "Mark as checked" do in Retention Responses | incomplete | medium | Create Retention Responses article covering all UI elements and workflow |
| 2026-03-18 | 215473537585362 | Reactivating lesson reminders for a client | wrong_answer | high | Create article: re-enable reminders per booking via Options tab |
| 2026-03-19 | 215473546525450 | Setting up trial sessions | incomplete | medium | Create step-by-step "Setting up trial sessions" guide |
| 2026-03-20 | 215473561814662 | DCA onboarding — billing status guessed incorrectly | account_specific_guessed | low | Onboarding checklist article with explicit status sections (Done / Pending / Not started) |
| 2026-03-20 | 215473567215029 | Awaiting payment vs Unpaid status | wrong_answer | medium | Create "Booking payment statuses explained" article |
| 2026-03-22 | 215473588206504 | Per-course loyalty discount — wrong location | wrong_answer | medium | Update Loyalty Program article: per-course rules are in Sales & Payments → Loyalty, NOT in course payment settings |
| 2026-03-23 | 215473595984092 | Clients → Registrations section not loading | wrong_answer | medium | Add troubleshooting: complete page failure across all browsers = escalate immediately, not blocks/cache |
| 2026-03-25 | 215473627056718 | Make-up hours report filtered by location | incomplete | medium | Add to make-up guide: no built-in filtered report by location exists — state limitation upfront |
| 2026-03-26 | 215473641212867 | Email confirmation after make-up sign-up (language error) | incomplete | low | Bot config: language detection must match the customer's message language |
| 2026-03-26 | 215473646051187 | Deposit + balance timing for summer camps | escalated_no_help | medium | Add summer camp payment setup guide: per-programme deposit + balance templates |
| 2026-03-27 | 215473662781832 | Email after make-up sign-up — initial answer wrong | wrong_answer | medium | Update make-up guide: email behavior per approval mode (manual vs auto) |
| 2026-03-29 | 215473686963241 | Removing "Participant same as payer" button | wrong_answer | high | Add guide: system form elements vs custom Additional Fields |
| 2026-03-29 | 215473688031023 | Dynamic tags in consent agreement name | wrong_answer | medium | Expand Consents guide: *\|AGREEMENT_URL\|* tag required for "read more" link — not optional |
| 2026-03-30 | 215473694735972 | Date of birth field disappearing | wrong_answer | medium | Add FAQ: required fields disappearing — do not dismiss as expected behavior without investigation |
| 2026-03-30 | 215473695996732 | Automatic payment reminder intervals | wrong_answer | medium | Update payment reminders guide: intervals are configurable, no universal 7-3-1 day default |
| 2026-03-30 | 215473696598576 | Widget not showing programme | escalated_no_help | low | Add advanced widget troubleshooting: after confirming settings, check start dates, class capacity, session availability |
| 2026-03-31 | 215473713545046 | "Participant same as payer" button (repeat) | wrong_answer | high | Same fix as 215473686963241 |
| 2026-03-31 | 215473714105373 | Make-up not available for specific group | account_specific_guessed | medium | Add FAQ: make-up slots only appear 4 days before first session of a group |
| 2026-04-01 | 215473732509418 | Unmatched payment despite correct amount | account_specific_guessed | medium | Add FAQ: payment pairing failed despite matching conditions — check Matching Process Summary |
| 2026-04-06 | 215473788472655 | Participant names missing from invoice | escalated_no_help | low | Add FAQ or guide: invoice layout for multi-participant orders |
| 2026-04-07 | 215473802460761 | Cannot find registered child in search | wrong_answer | medium | Add search troubleshooting: if client not found, check for platform search issues and contact support |
| 2026-04-07 | 215473802786556 | Overpaid orders showing incorrect amounts | escalated_no_help | low | Add FAQ: order amounts display bug — open order detail to trigger data reload |
| 2026-04-07 | 215473803474980 | Make-up hours not showing, mobile navigation | escalated_no_help | medium | Add mobile nav FAQ: Team & Settings not visible on mobile — scroll down below Help section |
| 2026-04-08 | 215473820467691 | Cannot send emails — Neplatná suma error | escalated_no_help | medium | Add troubleshooting: "Neplatná suma" in bulk send — try hard refresh and resend |
| 2026-04-08 | 215473821725546 | Visual overlap in extra field type selector | escalated_no_help | low | Resolved product bug — no article needed; but note bot's immediate escalation pattern for UI bugs |
| 2026-04-08 | 215473821765673 | How to change app language (Romanian user) | wrong_answer | medium | Fix language change article — profile icon top right |
| 2026-04-08 | 215473822294948 | Scheduling trial class for existing lead | wrong_answer | medium | Update Trial Classes article: admins CAN schedule trial manually using "Choose trial date" in booking detail |
| 2026-04-08 | 215473826889641 | Make-up session locations not showing in widget | wrong_answer | high | Update make-up FAQ: causes are (a) class not started yet, (b) capacity full with no extra make-up slots, (c) waitlist not enabled |
| 2026-04-08 | 215473827512018 | How to change app language (2nd instance, same day) | wrong_answer | medium | Same fix as 215473821765673 |
| 2026-04-09 | 215473838033676 | Currency changed from CZK to EUR | wrong_answer | medium | Add troubleshooting: unexpected currency change = likely display bug, hard refresh first |
| 2026-04-09 | 215473838362638 | 4-digit PIN causes registration failure | escalated_no_help | low | Add troubleshooting: if PIN fails, use the confirmation link from the same email |
| 2026-04-09 | 215473839924292 | Email marked as rejected despite valid address | escalated_no_help | low | Add FAQ: email rejection status — caused by full mailbox or delivery failure; flag auto-clears |
| 2026-04-10 | 215473851957758 | Confirmation email template not updating | escalated_no_help | low | Add troubleshooting: template not updating — verify assignment under Programme → Online Registration → Confirmation email |
| 2026-04-11 | 215473864184270 | Class shows 10/10 capacity after cancellations | escalated_no_help | high | Add FAQ: class still shows full after cancellations — capacity counts registrations, not attendance drops |
| 2026-04-11 | 215473864269528 | Attendance shows absent instead of cancelled | escalated_no_help | medium | Add FAQ: absent vs cancelled — caused by cancellation after the deadline setting |
| 2026-04-13 | 215473882690827 | Session notification emails not arriving | account_specific_guessed | medium | Update notification troubleshooting: after standard checks, human review with account access is required |
| 2026-04-13 | 215473883017543 | Google review request email not received | escalated_no_help | medium | Add FAQ: when does Google review request email send? — required conditions |
| 2026-04-14 | 215473900671438 | Blocks settings not inheriting from class template | escalated_no_help | medium | Update Blocks article: Blocks are per-class day/slot variants, do not inherit from programme |
| 2026-04-14 | 215473904208863 | Client registered to "Course" — terminology confusion | wrong_answer | medium | Add terminology disambiguation: Course vs Programme vs Class vs Group |
| 2026-04-14 | 215473909714006 | Changing language in Zooza admin | wrong_answer | high | Fix language change article — profile icon top right (4th occurrence in 9 days) |
| 2026-04-15 | 215473920530283 | Registration form displaying incorrect data (bug) | escalated_no_help | medium | Improve escalation path for reproducible form bugs — not cache clearing as default first response |
| 2026-04-15 | 215473921161344 | Finding deleted registrations by status filter | wrong_answer | high | Update deleted registrations article: filter removed from UI, use URL fragment #registrations?status=deleted |
| 2026-04-16 | 215473937588409 | Attaching a PDF to email template | wrong_answer | medium | Add FAQ: email templates do not support file attachments — use a link to hosted document instead |
| 2026-04-16 | 215473943274436 | Groups not showing in admin calendar | incomplete | low | Add calendar troubleshooting: check date range and group filter before assuming display bug |
| 2026-04-17 | 215473953736104 | Per-session seat capacity settings | escalated_no_help | low | Add Capacity FAQ: class-level vs session-level capacity and how they interact |
| 2026-04-17 | 215473954060464 | Changing display language to French | wrong_answer | high | Same fix as language article — 5th occurrence |
| 2026-04-17 | 215473957661790 | Re-enrolling client after session cancellation | wrong_answer | medium | Document correct re-enrollment workflow with verified current UI step names |
| 2026-04-18 | 215473969619352 | Urgent: registration widget deleted, site down | escalated_no_help | high | Define escalation protocol for site-down / widget deletion emergencies beyond standard support form |
| 2026-04-20 | 215473985715301 | Bulk email report showing Pending status | escalated_no_help | medium | Add protocol: bulk emails still Pending after a few minutes = escalate, likely platform fault |
| 2026-04-20 | 215473989450013 | Language change mid-session | wrong_answer | high | Same fix as language article — 6th occurrence |
| 2026-04-21 | 215474008120549 | Gift voucher expiration date on existing order | wrong_answer | high | Add FAQ: voucher expiration cannot be changed by admins — contact Zooza support |
| 2026-04-22 | 215474016119619 | Manager training manual — language change instruction | wrong_answer | high | Urgent: wrong path embedded in training materials — fix source article and audit generated training content |
| 2026-04-22 | 215474019377392 | Outstanding debt despite 7 paired payments | wrong_answer | medium | Add KB definition: what positive and negative balances mean on a booking in Zooza |
| 2026-04-23 | 215474030168349 | Emails not sent to additional access addresses | wrong_answer | medium | Update sending guide: Additional email field behavior and the "Send to additional access" toggle |
| 2026-04-23 | 215474031660130 | Restoring registrations deleted more than 30 days | wrong_answer | high | Update recovery article: deleted regs accessible indefinitely via #registrations?status=deleted — not a 30-day limit |
| 2026-04-23 | 215474031720772 | Waitlist for open sessions — not assigning automatically | incomplete | medium | Update waitlist FAQ: when spot opens, system emails all waitlisted clients simultaneously; first to click gets it |
| 2026-04-25 | 215474058388920 | Changing application language to Slovak | wrong_answer | medium | Same fix as language article — 7th occurrence |
| 2026-04-26 | 215474069962065 | Changing language on help.zooza.online | wrong_answer | medium | Add FAQ: help site is English-only; correct app language path is profile icon top right |
| 2026-04-28 | 215474091835264 | Clients can only see NEPRIDEM when cancelling | incomplete | medium | Update cancellation guide: check cancellation limit first — this is why Cancel option is absent |
| 2026-04-29 | 215474105351434 | Client not receiving reminders after transfer | escalated_no_help | medium | Add to notifications troubleshooting: if one client not receiving reminders, check client profile notification preferences |
| 2026-04-29 | 215474106365960 | Cannot pair unmatched payments — detail opens empty | incomplete | medium | Add to inbound payments: if detail opens empty, contact support — UI bug, not a pairing procedure issue |
| 2026-04-30 | 215474132699920 | Where to change widget payment summary text | wrong_answer | high | Create FAQ: how to change widget text — widget translations or Booking form settings, not payment plan settings |
| 2026-05-01 | 215474146027245 | New Tasks panel blocking screen after update | wrong_answer | medium | Protocol: new major UI features need immediate KB articles; new-feature panels ≠ cache issues |
| 2026-05-04 | 215474169098956 | What's new popup blocking calendar — no close button | incomplete | medium | Add article on new features popup; escalate after 2 failed cache-clearing attempts |
| 2026-05-05 | 215474178028698 | Forwarded request with no problem description | account_specific_guessed | high | Bot behavior: ask for problem description — never guess a scenario from a zero-context message |
| 2026-05-05 | 215474178700711 | Enabling waitlist for a full class | wrong_answer | high | Create article distinguishing enrollment waitlist vs make-up waitlist with separate configuration paths |
| 2026-05-05 | 215474179567915 | Disabling automated payment notifications | wrong_answer | high | Update notifications article: scheduled payment emails are system messages — cannot be disabled |
| 2026-05-05 | 215474179811201 | Automatic confirmation email not sending | incomplete | medium | Update email troubleshooting: add programme type mismatch (single-session vs recurring) as a cause |
| 2026-05-05 | 215474180954106 | Payment templates set but no payments generated | account_specific_guessed | medium | Create article: troubleshooting when payment plans exist but payments have not generated |
| 2026-05-05 | 215474184636218 | Make-up credits recorded but not visible | incomplete | medium | Update make-up FAQ: cancellation deadline is the most common cause — credits valid but no sessions bookable |
| 2026-05-05 | 215474188136690 | Payments moved to "ignored" status | escalated_no_help | medium | Create article on inbound payment statuses — "ignored" = deduplication agent, how to manually pair |
| 2026-05-06 | 215474201914931 | Sibling discount incorrectly applied to single child | incomplete | high | Create article: sibling + loyalty discount configuration with billing period evaluation |
| 2026-05-07 | 215474206854763 | Auto-continuation email not arriving — wrong trigger | wrong_answer | high | Update auto-continuation article: trigger is N days before billing period end, not trial attendance |
| 2026-05-07 | 215474208579008 | Overpayments reported at branch | account_specific_guessed | medium | Bot behavior: multi-client / multi-branch issues should escalate immediately rather than giving generic process explanations |
| 2026-05-07 | 215474211216090 | System lag / emails not delivered on time | escalated_no_help | medium | Create article: email delivery troubleshooting — Communication log, delay causes, escalation |
| 2026-05-08 | 215474221012560 | Attendance icons — question classified as spam | wrong_answer | high | Fix spam classification for legitimate questions with marketing email footers; create attendance status icons article |
| 2026-05-12 | 215474266735501 | Logout button missing on mobile | wrong_answer | medium | Add escalation rule: if described UI element is missing after one attempt, escalate — do not repeat same instructions |
| 2026-05-12 | 215474272895141 | Client cannot perform any actions in profile | wrong_answer | high | Create profile access troubleshooting including hard bounce email as a cause |
| 2026-05-13 | 215474284302024 | Bulk editing payment due dates | incomplete | medium | Add article: bulk editing Scheduled payment dates (applies only to payments in Scheduled status) |
| 2026-05-13 | 215474289754914 | Client profile not loading — wrong language used | account_specific_guessed | medium | Bot config: language detection must match customer message language |
| 2026-05-13 | 215474292782391 | Reply to existing support email thread | escalated_no_help | low | Bot routing: detect email replies to existing threads — do not send generic greeting |
| 2026-05-14 | 215474299773220 | Payment status "paid" immediately after registration | escalated_no_help | medium | Add FAQ: why does booking show as paid right after registration? — free registrations, zero-debt, scheduled payments |
| 2026-05-14 | 215474303213167 | Class not showing for online registration | escalated_no_help | medium | Add registration count limit to widget troubleshooting checklist |
| 2026-05-14 | 215474304002743 | E-invoicing availability | incomplete | low | Add FAQ: e-invoicing not yet available; SK mandate 2027; Zooza plans to support it |
| 2026-05-14 | 215474304543326 | COURSE_PLACE dynamic tag requires room | wrong_answer | high | Update dynamic tags: COURSE_PLACE works without a room; blank = data sync issue |
| 2026-05-14 | 215474309140037 | Dynamic tags not working in manual template send | escalated_no_help | medium | Update dynamic tags: session-context tags only work in automatic sends — no context in manual sends |
| 2026-05-15 | 215474314193354 | Registration count limit vs class capacity | wrong_answer | medium | Add article: Obmedzenie poctu registracii as a distinct setting from class capacity |
| 2026-05-15 | 215474322754279 | Lead groups showing as paid | wrong_answer | high | Create article: lead groups show as paid because no debt exists — expected behavior |
| 2026-05-16 | 215474330998087 | Payment import not pairing — deduplicator cause | wrong_answer | high | Add article: payment import failures — check Inbound Payments queue, remove "AI confidence" as explanation |
| 2026-05-17 | 215474338496458 | Summer classes appearing across franchise accounts | incomplete | medium | Expand widget article: franchise-per-widget filtering and how to restrict class visibility per franchise |
| 2026-05-18 | 215474342466706 | Preparing courses for next school year | incomplete | medium | Create "Prepare courses for next school year" guide with Zooza product steps — not marketing advice |
| 2026-05-19 | 215474364973813 | Auto-continuation — no groups available | wrong_answer | medium | Add FAQ: "No groups available" = group not enabled for auto-enrolment; do not create manual booking |
| 2026-05-22 | 215474413097884 | Class capacity exceeded by make-up registrations | incomplete | low | Add note: if actual attendance exceeds system capacity, check for clients without bookings |
| 2026-05-25 | 215474435713715 | Finding subscription invoices — profile icon location wrong | wrong_answer | medium | Update subscription/billing FAQ: profile icon is top right on both desktop and mobile |
| 2026-05-25 | 215474439121261 | Changing interface language to Slovak (mobile) | wrong_answer | medium | Update language change article for mobile: profile icon top right, not Zooza logo |
| 2026-05-26 | 215474447610941 | Morning session notification not resent after reschedule | escalated_no_help | low | Add FAQ: reminder not resent after reschedule if already sent for original date — manual send workaround |
| 2026-05-26 | 215474450809460 | Calendar showing occupancy with no active registrations | escalated_no_help | medium | Add FAQ: deleted registrations can persist as calendar blocks — how to find and clear them |
| 2026-05-26 | 215474452068979 | Price display on booking form with payment plan | wrong_answer | medium | Update booking form and programme price articles: "Show price with payment plan" toggle is in Publish/widget settings, NOT in programme Price tile |
| 2026-05-27 | 215474462855286 | Payment with correct variable symbol not matched | incomplete | low | Update inbound payments: deduplication agent section; escalate after customer confirms basic conditions are met |
| 2026-05-28 | 215474478152842 | Notification when payment needs manual matching | escalated_no_help | medium | Add section to inbound payments: where to monitor payments requiring manual review |
| 2026-05-29 | 215474493270366 | Client could only select 15:30 time slot | escalated_no_help | medium | Create article: widget shows available but registration fails — check class settings |
| 2026-05-31 | 215474516669566 | Session list shows 44 but customer counts 40 | escalated_no_help | medium | Add FAQ: session count includes cancelled/unplanned sessions — filter and bulk-delete |
| 2026-06-01 | 215474529343968 | Finding Export button in Payments received | incomplete | medium | Update Payments navigation article with labeled screenshot; add troubleshooting for Owner who can't find sub-page |
| 2026-06-01 | 215474531908459 | Inserting images into email templates | wrong_answer | high | Update email templates article: images must be hosted externally and linked — not embedded |
| 2026-06-02 | 215474542054525 | Sessions created but not appearing | incomplete | medium | Add troubleshooting: sessions not appearing after confirmed setup — verify session generation completed, escalate |
| 2026-06-03 | 215474558780762 | Price not displaying in booking widget | account_specific_guessed | medium | Add FAQ: 3 distinct causes for missing price display — lead group, payment plan + hide-price setting, zero price |
| 2026-06-03 | 215474560675427 | Make-up sessions not working after moving client | escalated_no_help | medium | Add to make-up guide: moving client does not affect existing credits — credits are fixed at sign-off time |
| 2026-06-05 | 215474586971392 | Urgent login error — client cannot access profile | escalated_no_help | medium | Add standard login troubleshooting before escalating: magic link vs code, spam folder, new code flow |
| 2026-06-08 | 215474611327468 | Waitlist behavior — wrong type answered | wrong_answer | high | Create dedicated article: poradovník na náhradky (automatic, first-click-wins) vs poradovník do skupiny (manual approval) |
| 2026-06-08 | 215474613827609 | Which setting controls Waiting for payment date | escalated_no_help | medium | Add FAQ: tolerance period controls the Waiting for payment status date |
| 2026-06-08 | 215474613950624 | Tolerance period setting and its effect | incomplete | medium | Add tolerance period article: grace window only — does not shift payment due dates |
| 2026-06-09 | 215474622293568 | Extra fields not appearing in widget | wrong_answer | medium | Add to booking form troubleshooting: min/max registration conflict (min > max) suppresses extra fields |
| 2026-06-10 | 215474638757654 | Archived class in instructor pay report | escalated_no_help | medium | Add FAQ: archived class in pay report — expected behavior; delete future sessions before archiving to exclude them |
| 2026-06-11 | 215474657694408 | Class visible in Zooza but not in website widget | incomplete | medium | Add escalation trigger after settings check passes — embed code filters, place_id, capacity need account access |
| 2026-06-13 | 215474692552973 | Classes not visible in admin calendar | incomplete | medium | Add calendar troubleshooting: midnight-scheduled session offsets calendar grid — scroll down before assuming bug |
| 2026-06-15 | 215474707801963 | Booking confirmation email not sent | incomplete | medium | Create article: how to resend booking confirmation manually from booking Communication tab |
| 2026-06-18 | 215474751098527 | Calendar appointments not visible after 13:00 | wrong_answer | medium | Add protocol: display issues persisting after hard refresh = escalate (confirmed system bug June 18) |
| 2026-06-18 | 215474752148250 | Different payment plans per class | wrong_answer | high | Update payment templates: global → programme → class three-step flow; no standalone Apply at class level |
| 2026-06-18 | 215474755780236 | Trial session price — contradictory answers same day | wrong_answer | medium | Add to trial sessions article: clarify whether per-class trial price setting exists — resolve the ambiguity |
| 2026-06-19 | 215474770390592 | Clients cannot see payment instructions or QR code | account_specific_guessed | medium | Add to payments FAQ: most common cause is Lead class type, not toggle settings |
| 2026-06-22 | 215474794459051 | How to find client address — Czech language request misread | wrong_answer | medium | Bot comprehension issue; fix language change article |
| 2026-06-22 | 215474794924382 | Payment template shows wrong amount as full payment | escalated_no_help | medium | Add to payment templates FAQ: check Lead vs Fixed class type; check one-off vs scheduled template |
| 2026-06-23 | 215474808789884 | Widget shows available when class is full | wrong_answer | high | Update troubleshooting: always check class/group settings — remove widget capacity display explanation |
| 2026-06-23 | 215474809131687 | How to change admin interface language to Slovak | wrong_answer | medium | Same fix as language article; add note Zooza MCP is not the language switcher |
| 2026-06-09 | 215474627138480 | 8-class credit pack recurring every 35 days | incomplete | medium | Add comparison article: Entry Pass vs Pay-as-you-go vs Membership vs Blocks vs Make-up credits |
