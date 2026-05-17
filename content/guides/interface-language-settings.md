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
last_converted: "2026-05-15"
---

# Change the language in Zooza

Zooza has two separate language settings that work independently:

| Setting | What it controls |
|---|---|
| **Admin panel language** | The language of the Zooza admin interface (menus, buttons, labels) |
| **Application Communication Language** | The language of client-facing content — booking widgets, confirmation emails, and client portal |

---

## Change the admin panel language

The admin panel language is set per user account — each admin can have a different language.

1. Click your **profile icon** or name in the top-right corner of the admin panel.
2. Select **Account settings** (or **Profile**).
3. Find the **Language** field and choose your preferred language.
4. Save.

The admin panel reloads in the selected language immediately. This does not affect what clients see.

> **Available admin languages:** Slovak, Czech, English, Hungarian, Romanian, and others depending on your account setup.

---

## Change the client-facing language (widgets and emails)

This setting controls what language your clients see when they register, receive confirmation emails, or access their Client Profile.

1. Go to **Settings → Company information** (or **General settings**).
2. Find **Application Communication Language**.
3. Select the language your clients use.
4. Save.

This affects:
- The booking form widget on your website.
- Automatic system emails (booking confirmation, payment reminders, etc.).
- The Client Profile interface.

> **Custom email templates** override the system language. If you have edited a confirmation email template in Slovak, clients will receive the Slovak version regardless of this setting.

---

## The admin panel is in the wrong language after setup

If the interface appeared in an unexpected language when you first logged in:

1. Follow the steps above to change the admin panel language in your profile settings.
2. If you cannot find the language option or the interface is unreadable, try navigating directly to the settings page.

The language selection is stored in your user profile — it does not reset unless you clear your browser data or log in from a new device for the first time.

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
