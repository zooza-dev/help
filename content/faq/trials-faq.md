---
title: "Trial Classes FAQ"
slug: "trials-faq"
type: "faq"
product_area: "Bookings"
sub_area: ""
audience: ["admin"]
tags: ["registrations"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-15"
intercom_id: 13728500
intercom_sync: false
---

# Trial Classes FAQ

<!-- Synonyms: trial automation, check trial status, verify trial automation active, enroll after trial, manual enrollment trial, payment after trial, trial booking detail, trial timeline, trial won trial lost, skúšobná hodina automatizácia, ako skontrolovať stav skúšobnej hodiny, zápis po skúšobnej hodine, platba po skúšobnej hodine, ako zistiť či je aktívna automatizácia skúšobná hodina, trial vyhrany trial prehraný, próbaóra automatizáció, próbaóra státusz ellenőrzés, regisztráció próbaóra után, fizetés próbaóra után, automatizáció aktív-e, zkušební hodina automatizace, stav zkušební hodiny, zápis po zkušební hodině, platba po zkušební hodině -->

## How do I set up trial classes?

Trials are configured per programme. Go to **Programme → Settings → Trial** to enable them, and **Programme → Automations → Trials** to configure the rules.

You can set:

1. Whether the trial is free or paid.
2. How many trial sessions are offered (usually one).
3. Whether trial dates are shown on the booking form (and how many days ahead).
4. Whether trial bookings count towards class capacity.
5. Whether a trial booking temporarily holds a spot in the class.

## What is the trial-to-enrolment flow?

The full automated flow is:

1. Client registers for a trial and receives a confirmation.
2. Client receives a reminder before the trial session.
3. The instructor marks attendance after the trial.
4. The system automatically sends a booking link offering full enrolment.
5. Follow-up messages encourage enrolment.
6. If the offer is not used, the trial is marked as **Trial Lost**.

## Why does it say "class full" when a trial client tries to enrol?

Trial bookings count towards class capacity. When the client finishes their trial and tries to enrol in the same class, the system may show "class full" because their trial seat is still counted. If you see this happening consistently, contact support — it may be a calculation issue that needs a fix on the backend.

## Can an admin manually create a trial booking?

No. Trial bookings can only be created by parents through the online booking form. As an admin, you can only create standard enrolments. If needed, you can go through the booking form on behalf of a parent as a workaround.

## How do I handle a client who wants to change their trial date?

If a parent can't make their booked trial, you can update their attendance in the system — mark the original session as absent and rebook them into a different session. This is managed through the booking detail.

## What happens when a client cancels a trial?

If a client cancels a trial, the system will follow the configured automation. You can manually change the status to **Trial Lost**, but this will not trigger automatic follow-up emails unless you explicitly choose to send one at that moment.

## Does instructor attendance tracking affect trials?

Yes. Tracking attendance is important because it triggers the trial-to-enrolment automation. When a instructor marks a trial attendee as "attended", it triggers the system to send the enrolment offer.

## Trials and blocks cause overbooking — what is happening?

This is a known limitation when a class uses both trial lessons and blocks (sub-periods within a group) at the same time.

When a client books a trial, the system can reserve a spot in the **group-wide** capacity. However, block capacity is calculated **per block**. Because the system does not know which specific block the trial client will eventually join, it cannot accurately reserve a per-block seat. In practice this means:

1. A trial booking may fill a session slot at the group level.
2. A paying client then registers for a specific block in the same group.
3. The system prioritises the paying client (confirmed revenue) over the trial (non-binding), which can push the session over its per-block capacity.

**Workaround:** Go to **Programme → Settings → Trial** and configure trial bookings to use **extra capacity** only. This ensures that trial reservations never consume spots intended for paying clients. The trial client is added on top of the normal capacity limit instead of inside it.

If you prefer to keep the current setting, you will need to manage overbooking manually — for example, by contacting the trial client and moving them to a different session that still has available spots. <!-- REVIEW: confirm "extra capacity" setting label matches current UI -->

## Can a client who finished a trial register again for a full course in the same class?

Yes. Once the trial process reaches a final state, the client can register for a full paid course in the same class. The exact flow depends on the trial status:

1. **Trial ended (Trial Won / Trial Lost):** Open the registration detail. You will see a **Start registration** button. Click it to convert the trial into a full paid booking. The client can also do this themselves through the enrolment link sent by the trial automation.
2. **Trial still in progress:** If the trial registration is still active (for example, in "Trial Started" state), the system will **not** allow a new registration with the same email into the same group. The trial must first reach a final state — either "Trial Won" or "Trial Lost" — before a new registration is possible.

To move a trial to a final state manually, change the registration status to **Trial Lost** (or **Trial Won** if they attended). After that, either use the **Start registration** button on the existing registration or have the client go through the booking form again.

## How do I check whether a client is currently in a trial?

Open the booking detail for that client. If the booking is a trial, you will see a **trial timeline** showing the current status and upcoming steps — for example:

- Trial started (booking creation date)
- Trial session date
- Booking link sent (date the enrolment offer was sent)
- First follow-up email sent
- Second follow-up scheduled
- Will be marked as Trial Lost (if no action)

The current step is highlighted so you can see exactly where in the process the client is.

> **Note:** If automation is not active for that programme, you will only see the trial session date and current status — no scheduled notification dates will be shown.

## How do I check whether trial automation is active for a programme?

1. Go to **Programmes** and open the programme.
2. Click the **Settings** tile → **Edit** → scroll to the **Trial** section. This shows whether trials are enabled and the trial type.
3. To see the automation rules, go to the programme's **Automations** tile → **Trials**. Here you can see and configure:
   - Whether an enrolment link is sent automatically after the trial session
   - The number of days before the first and second follow-up
   - Whether to automatically change status to Trial Lost after no response
   - Whether to send a notification when the status changes to Trial Lost

If the automation is not configured, no emails are sent automatically after the trial session ends.

## What happens after the last trial session?

Attendance must be recorded for the automation to trigger. Once the instructor marks the trial client as attended on the session detail, the system:

1. Sends the client a booking link to register for the full programme (if automation is active).
2. Sends follow-up emails after the configured number of days if the client has not registered.
3. Marks the trial as **Trial Lost** if no registration follows after the configured period.

If automation is not set up, nothing is sent automatically — you need to enrol the client manually.

## How do I manually enrol a client after their trial?

1. Open the trial booking detail.
2. Click **Enrol**.
3. Select the class you want to enrol them in.
4. Set the payment amount (or select a payment template — the system offers templates configured for the class).
5. Confirm. The trial status changes to **Trial Won** and a new standard booking is created.

> **Note:** When you enrol manually, the client receives a confirmation email. They then go to their **Client Profile** to complete payment — either by card, by setting up a GoCardless mandate, or by following bank transfer instructions. The payment instructions email is only sent if you trigger it manually.

## How does the client complete payment after enrolment?

After enrolment (whether self-registered or admin-enrolled), the client receives a confirmation email. To complete payment, they:

1. Open the link in the confirmation email to access their **Client Profile**.
2. Go to the **Payments** section of their profile.
3. Choose the payment method: card payment, GoCardless direct debit mandate, or bank transfer.

For bank transfer, they use the payment details (variable symbol and account number) shown in their profile. The payment is then matched automatically or manually by the admin.

If the client does not receive the confirmation email or cannot find payment instructions, you can resend the notification from the booking detail.

## Can I resend a follow-up trial email using an edited template?

Yes. You can manually send a follow-up email to trial clients at any time, and choose which template to use — including a template you recently edited.

1. Go to **Communication** and select the target group of clients (e.g. clients with a trial in a specific programme).
2. Click **Send message**. 
3. Click **Change email template** to select a different template.
   ![Change email template button in Communication](../../assets/images/trials-faq-01.png)
4. Pick your edited template from the list, or make further edits before sending.
   ![Template selection dropdown](../../assets/images/trials-faq-02.png)
5. Send.

The email goes out using the wording from the template you selected, not the default automation template.

You can manage all templates — including editing and saving custom versions — under **Communication → Templates**.
