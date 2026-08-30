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
last_converted: "2026-08-30"
---

# Change the language in Zooza

Language in Zooza is decided in three separate places, and they work independently:

| What | Set where |
|---|---|
| **Admin panel** — menus, buttons, labels you see | The switcher at the bottom of the **Dashboard** |
| **Emails and message templates** your clients receive | **Settings → General** — Application Communication Language |
| **Booking form, calendar and parent zone** embedded on your site | **Your own website's** language setting — parents can switch it themselves on the widget's own language switcher |

Mixing up the second and third is the most common language problem, so if you only
read one thing, read [Which setting controls what](#which-setting-controls-what--the-short-version).

---

## Change the admin panel language

The language switcher is on the **Dashboard**, at the bottom of the page.

1. Click the **Zooza logo** in the top-left corner to open the Dashboard (the app home page).
2. Scroll to the **bottom** of the Dashboard.
3. Choose your language in the switcher.

The admin panel reloads in the selected language immediately.

> **It is not in your profile.** Opening your profile shows only your first name, surname, phone number and nickname — there is no language field there. If you have been looking in the profile and finding nothing, that is why.

> **This does not change anything your clients see.** It only affects your own view of the admin panel. The language of emails and the booking widget is a separate setting — see the next section, and read it before changing anything, because the two are easy to confuse.

> **Available admin languages:** Slovak, Czech, English, Hungarian, Romanian, and others depending on your account setup.

---

## Change the language of emails and templates

> **Careful — this is the one people change by mistake.** The language setting in **Settings** is not your own interface language, and it is not the widget's either. It is the language Zooza writes to your **clients** in. Changing it because the admin panel is in the wrong language will switch your clients' communication instead, and leave your panel exactly as it was. To change your own view, use the Dashboard switcher described above.

1. Go to **Settings → General** (**Company information**).
2. Find **Application Communication Language**.
3. Select the language your clients use.
4. Save.

This affects the automatic system emails — booking confirmation, payment reminders,
session notifications — and the message templates they are built from.

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

## The admin panel is in the wrong language after setup

If the interface appeared in an unexpected language when you first logged in, click the Zooza logo to open the Dashboard and use the language switcher at the bottom of the page.

If the interface is unreadable, the logo is the safest thing to click — it always returns you to the Dashboard, and the switcher sits at the bottom of that page regardless of the language it is currently showing.

Do **not** go into Settings to fix this. That changes the language your clients receive, not your own.

---

## Which setting controls what — the short version

Three separate things, three separate places. Almost every language question is
someone reaching for the wrong one of the three.

| What is in the wrong language | Where to change it |
|---|---|
| The admin panel you are looking at | The switcher at the bottom of the **Dashboard** |
| The booking form, calendar or parent zone on your site | **Your website's language setting**. A parent who needs another language switches it on the widget's own language switcher |
| Emails and message templates your clients receive | **Settings → General** — Application Communication Language |

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
