---
title: "Retention"
description: "Retention is a Zooza feature that automatically sends a re-engagement link to clients whose trial was lost or whose booking was cancelled."
slug: "retention"
type: "setup"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: ["retention", "re-engagement", "trial lost", "churn", "win-back"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-08-07"
---

# Retention

Retention is a Zooza feature that automatically sends a re-engagement link to clients whose trial was lost or whose booking was cancelled. It gives clients a time-limited opportunity to return without the admin having to follow up manually.

**When Retention triggers:**

- A trial is marked as **Trial Lost**
- A booking is **cancelled** (by admin or client)

After either of these events, the system sends the client a message with a link to re-enrol. The link remains active for a configurable number of days.

**Retention is separate from:**

- **Trial automation** — handles the period *during and immediately after* a trial (reminders, enrolment link, Trial Lost trigger). Retention starts *after* Trial Lost.
- **Loyalty program** — rewards active clients with points and benefits. Retention targets clients who already left.

## Setting up Retention

Retention is configured per programme.

1. Go to **Programmes** and open the programme.
2. Click **Settings** and scroll to the **Retention** tile.
3. Click **Edit**.
4. Set the number of days the re-engagement link remains active (default: **30 days**).
5. Optionally add a custom note — this text appears alongside the re-engagement link in the message to the client.
6. Click **Save**.

Repeat for each programme where you want Retention active.

> **Note:** Retention must be configured on each programme individually. There is no global on/off switch.

## What the client receives

When a trial is lost or a booking is cancelled, the client receives a message with a link. Clicking the link opens a booking flow (or direct enrolment page, depending on your programme setup) where they can re-enrol.

The link expires after the number of days you configured. Once expired, the client cannot use it to re-enrol.

If you added a custom note in the Retention settings, it appears with the link in the message.

## Tracking retention

Zooza does not have a dedicated Retention report. To track whether a client returned through the retention link:

- Check the client's booking history — if they re-enrolled after a cancellation or Trial Lost event, a new booking will appear.
- In **Reports → Trials**, you can see which trials resulted in Trial Lost, giving you a starting point to check follow-up enrolments manually.

## Common questions

### Does Retention work if the client's trial was lost automatically?

Yes. Whether Trial Lost was set manually by an admin or triggered automatically (e.g. by a trial automation rule), the Retention link is sent in either case.

### Can I disable Retention for one programme but keep it on for others?

Yes. Because Retention is configured per programme, you can set different day limits or disable it entirely on specific programmes by leaving the retention days at 0 (or not configuring it).

### What happens if the client re-enrolls before the link expires?

The booking is created normally. The retention link is consumed — the client cannot use the same link a second time.

### Can I resend the retention link manually?

Not directly. The link is sent automatically at the moment of Trial Lost or cancellation. If a client missed it or the link expired, you can re-send a manual re-engagement message via **Communication → Compose** with a link to your booking page or client profile.

### Does Retention apply to clients who cancelled themselves (not the admin)?

Yes. Retention triggers on both admin-initiated and client-initiated cancellations.

---

> **SK:** Retencia je nastavenie na úrovni kurzu. Keď je trial stratený alebo registrácia zrušená, klient dostane odkaz na opätovné prihlásenie. Konfigurácia: **Kurzy → Nastavenia → Retencia → Upraviť** — zadáte počet dní (predvolene 30) a voliteľnú poznámku. Retencia sa líši od Loyalty programu (ten odmieňa aktívnych klientov) a od trial automatizácie (tá riadi priebeh trialu, nie to, čo príde po jeho strate).

## Manually adjusting retention

The automated retention cron runs based on the programme settings you define. When you need to set or remove the retention flag manually — for example, to correct a cohort the cron missed, or to trigger retention early for a group of clients — use the **Operations** button on the Bookings list.

**How to bulk-adjust retention:**

1. Go to **Clients → Bookings**.
2. Use the filters to narrow the list to the registrations you want to affect (e.g. by programme, class, status).
3. Click **Operations**.
4. Choose **Set in retention** or **Remove from retention**.
5. A dry-run preview shows how many registrations will be affected. Review the count before confirming.
6. Choose whether to send the retention notification email:
   - **Don't notify** — flag only, no email sent.
   - **Notify those not yet notified** — sends to clients who have not yet received a retention email.
   - **Notify all** — sends to every registration in the selection regardless of prior notifications.
7. Confirm to apply.

> **Note:** The Operations button applies to **all registrations matching the current filters**, not just the registrations visible on screen. Check your filters carefully before confirming.

## Related

- [Trial sessions](trial-sessions.md) — setting up and managing trials
- [Loyalty Program](../guides/loyalty-program.md) — rewarding active clients with points
- [Collecting reason for cancelling](collecting-reason-for-cancelling.md) — capture why clients leave
