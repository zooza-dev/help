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
last_converted: "2026-08-07"
---

# Change the language in Zooza

Zooza has two separate language settings that work independently:

| Setting | What it controls |
|---|---|
| **Admin panel language** | The language of the Zooza admin interface (menus, buttons, labels) |
| **Application Communication Language** | The language of client-facing content — booking widgets, confirmation emails, and client portal |

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

## Change the client-facing language (widgets and emails)

> **Careful — this is the one people change by mistake.** The language setting in **Settings** is not your own interface language. It is the language Zooza uses towards your **clients**: their emails and the booking widget. Changing it because the admin panel is in the wrong language will switch your clients' communication instead, and leave your panel exactly as it was. To change your own view, use the Dashboard switcher described above.

This setting controls what language your clients see when they register, receive confirmation emails, or access their Client Profile.

1. Go to **Settings → Company information** (or **General settings**).
2. Find **Application Communication Language**.
3. Select the language your clients use.
4. Save.

This affects:
- Automatic system emails (booking confirmation, payment reminders, etc.).
- The Client Profile interface.

### The embedded widget is different — it follows your website

**A widget embedded on your own site takes its language from the website it sits in, not from this setting.**

If your booking form or calendar shows English day names when you expected Romanian, Slovak or Hungarian, the fix is on your website, not in Zooza: make sure the page declares the right language. Changing **Application Communication Language** will not correct it, because the widget never reads that setting.

This is worth checking first, because the symptom looks exactly like a Zooza language problem — days of the week in English, texts like "The class will start…" instead of "Grupa va începe…".

> **Custom email templates** override the system language. If you have edited a confirmation email template in Slovak, clients will receive the Slovak version regardless of this setting.

---

## The admin panel is in the wrong language after setup

If the interface appeared in an unexpected language when you first logged in, click the Zooza logo to open the Dashboard and use the language switcher at the bottom of the page.

If the interface is unreadable, the logo is the safest thing to click — it always returns you to the Dashboard, and the switcher sits at the bottom of that page regardless of the language it is currently showing.

Do **not** go into Settings to fix this. That changes the language your clients receive, not your own.

---

## The widget is in a different language than expected

If the booking form or Client Profile appears in the wrong language for your clients:

1. Check **Application Communication Language** in **Settings → Company information** (see above).
2. If you have multiple widgets set up (via **Publish**), each widget uses the account-level language — there is no per-widget language override.
3. If your clients use multiple languages (e.g. EN and FR), consider whether separate programme variants with language-specific templates would work better.

---

## Related

- [Message templates](message-templates.md) — customizing the language and content of automatic emails.
- [Publish (Widgets)](../reference/publish-widgets.md) — managing your booking form and client portal widgets.
