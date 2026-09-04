---
title: "Change the language in Zooza"
description: "How to change the admin panel language, the client-facing widget and email language, and what to do if the language is set incorrectly after setup."
slug: "interface-language-settings"
type: "guides"
product_area: "Settings"
sub_area: ""
audience: ["admin"]
tags: ["language", "locale", "settings", "widget", "email", "admin panel"]
status: "published"
related_articles: ["message-templates", "customizing-widgets", "publish-widgets"]
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-09-04"
---

# Change the language in Zooza

Language in Zooza is decided in three separate places, and they work independently:

| What | Set where |
|---|---|
| **Admin panel** — menus, buttons, labels you see | **Settings → My profile**, or the bottom of the **Dashboard**. Personal to you |
| **Notifications, emails and WhatsApp** your clients receive | **Settings → General** — Application Communication Language. Company-wide |
| **Booking form, calendar and parent zone** embedded on your site | **Your own website's** language setting — parents can switch it themselves on the widget's own language switcher |

Mixing up the second and third is the most common language problem, so if you only
read one thing, read [Which setting controls what](#which-setting-controls-what--the-short-version).

---

## Change the language you see Zooza in

Two routes to the same setting — use whichever you reach first:

- **Settings → My profile**, in the **Application Communication Language** card.
- **The Dashboard**, at the very bottom of the page. Click the **Zooza logo** top-left to get there, then scroll down.

The admin panel reloads in the selected language immediately, and the choice is **yours alone** — every person on the account picks their own.

> **The same label sits in two places and means two different things — this is the trap.** The card on **your profile** sets *your* language. The setting of the same name in **Settings → General** sets the language Zooza writes to *parents* in. Changing the second because your own menus are wrong switches every notification, email and WhatsApp your clients get, and leaves your screen exactly as it was.

> **Available admin languages:** Slovak, Czech, English, Hungarian, Romanian, and others depending on your account setup.

---

## Change the language Zooza uses towards parents

This is the company-wide setting. It governs everything Zooza sends to parents and to people registering.

1. Go to **Settings → General** (**Company information**).
2. Find **Application Communication Language**.
3. Select the language your clients use.
4. Save.

It covers **notifications, email text and WhatsApp messages** — booking confirmations, payment reminders, session notifications — and the templates they are built from.

> **Not your own menus.** If Zooza shows *you* the wrong language, this is the wrong setting — see [Change the language you see Zooza in](#change-the-language-you-see-zooza-in) above.

### The embedded widget and parent zone take their language from your website

**A widget embedded on your own site — the booking form, the calendar, the parent
zone — takes its language from your website, not from the setting above.** Whatever
language your site is set to is the language the widget comes up in.

If the widget shows English day names when you expected Romanian, Slovak or
Hungarian, look at your website's language setting. This is worth checking before
anything else, because the symptom looks exactly like a Zooza language problem: days
of the week in English, texts like "The class will start…" instead of
"Grupa va începe…".

**For parents who need a different language, the switcher is on the widget itself.**
The widget can carry its own language switcher, and a parent uses that to change the
language for themselves. It is not driven by your website's own language switcher —
those are two unrelated controls, and switching the site does not switch the widget.

> **Custom email templates** override the system language. If you have edited a confirmation email template in Slovak, clients will receive the Slovak version regardless of this setting.

---

## Zooza is in the wrong language for me after setup

If the interface came up in an unexpected language when you first logged in, fix it on your own profile or at the bottom of the Dashboard — both are described above.

**If the interface is unreadable, the logo is the safest thing to click.** It always returns you to the Dashboard whatever language the menus are in, and the switcher sits at the bottom of that page.

Do **not** reach for **Settings → General**. That one changes the language your clients receive, not yours.

---

## Which setting controls what — the short version

Three separate things, three separate places. Almost every language question is
someone reaching for the wrong one of the three.

| What is in the wrong language | Where to change it |
|---|---|
| The admin panel you are looking at | **Settings → My profile**, or the bottom of the **Dashboard** |
| The booking form, calendar or parent zone on your site | **Your website's language setting**. A parent who needs another language switches it on the widget's own language switcher |
| Notifications, emails and WhatsApp your clients receive | **Settings → General** — Application Communication Language |

> **The widget and the emails are not the same setting.** Changing the
> communication language because the booking form is in the wrong language leaves
> the form exactly as it was, and quietly switches the language of every email your
> clients receive. Fix the widget on your website; fix the emails in Settings.

If your clients genuinely use two languages, the answer is the widget's own language
switcher, which lets each parent pick for themselves. Pair it with
language-specific message templates so the emails match what they booked in.

---

## Related

- [Message templates](message-templates.md) — customizing the language and content of automatic emails.
- [Publish (Widgets)](../reference/publish-widgets.md) — managing your booking form and client portal widgets.
