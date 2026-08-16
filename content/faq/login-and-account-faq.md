---
title: "Login and Account FAQ"
description: "Account deletion must be handled by Zooza support. Contact support@zooza.online and request account deletion."
slug: "login-and-account-faq"
type: "faq"
product_area: "Settings"
sub_area: ""
audience: ["admin"]
tags: ["login", "account"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-08-07"
---

# Login and Account FAQ

## How do I delete my Zooza account entirely?

Account deletion must be handled by Zooza support. Contact support@zooza.online and request account deletion. Once processed, all data associated with the account is removed. If you decide to return later, you can create a new account.

<!-- REVIEW: Confirm whether self-service account deletion is planned or if support-only is the permanent approach. -->

## How do I change the email I use to log in?

Go to **Settings → Team**, open the profile, replace the email address and save. From then on that person logs in with the new address — they enter it on the login page and request a link or code. There is no password to change.

**You do not have to replace it.** You can add a second access with the other email instead, and keep both working. That is the better option when:

- you want to keep the old address reachable while people get used to the new one,
- the two addresses are really two people who have been sharing one login,
- you are moving from a personal address to a business one and do not want to lose access mid-way.

Give each person their own login wherever you can. Permissions and the activity record are tied to the account, so a shared login makes both meaningless — see [Can multiple team members share one login?](#can-multiple-team-members-share-one-login) below.

## After changing an instructor's email, they cannot log in — what is the process?

When you update an instructor's email address in **Settings → Team**, the instructor must log in again using the new email:

1. Go to your Zooza app URL (e.g., `yourbusiness.zooza.app`).
2. Enter the **new** email address.
3. Click the login link that arrives by email.

No separate invitation is needed. The instructor simply requests a new login link with the corrected email. If the link does not arrive, check that the email address is spelled correctly in **Settings → Team** and ask the instructor to check their spam folder.

## A new account was created but not verified — how does verification work?

When a new business account is created in Zooza, it goes through a verification step before it becomes fully active. During verification, the Zooza team reviews the account details and approves it. If your account is stuck in an unverified state, contact support@zooza.online — they can check the status and approve it manually.

<!-- REVIEW: Clarify whether verification is automatic (email confirmation) or manual (Zooza team review) for all account types. The support data suggests manual approval is involved at least for network accounts. -->

## A client keeps creating new accounts on zooza.online instead of logging in through our website — what should I do?

This happens when a client goes to `zooza.online` (the main Zooza website) and creates a standalone account instead of using the registration or profile widget embedded on your website.

To prevent this:

- Direct clients to **your website** for registration and profile access, not to zooza.online.
- Embed the Zooza profile widget on your site so clients can log in and manage bookings from there.
- If a client already created a separate account on zooza.online, contact Zooza support to resolve duplicate accounts.

There is no way to block clients from visiting zooza.online directly, so clear communication about where to register is important.

## How do parents log in to their profile?

Zooza uses a **passwordless, token-based login**. Parents do not set or use a password. The process is:

1. The parent opens the profile widget on your website (or goes to your Zooza app URL).
2. They enter their email address.
3. Zooza sends a one-time login code to that email.
4. The parent enters the code to access their profile.

If a parent reports not receiving the code, ask them to check their spam folder. Login codes are sent almost instantly under normal conditions. There is no password to reset — every login uses a fresh email code.

## A client requested a login link twice and now the first link doesn't work — why?

Zooza uses single-use login tokens. Each time a client requests a new login link (PIN code), the **previous link is immediately invalidated**. Only the most recent link is valid.

This often happens when a client:
- Clicks "send login link" twice in quick succession
- Waits too long and requests a second link while the first is still in their inbox

**Solution:** Ask the client to use only the **most recent email** they received from Zooza and ignore any earlier login emails. If the second link also expired, they simply request a new one — there is no lockout.

## Can multiple team members share one login?

No. Each team member should have their own account with an individual email address. Shared logins create problems with audit trails, permissions, and notifications. To add team members:

1. Go to **Settings → Team**.
2. Add each person with their own email address.
3. Assign the appropriate role (owner, admin, instructor, etc.).

Each team member then logs in with their own email using the same passwordless login link process.

## How do I change the app language for admins or instructors?

1. Click your **profile icon** or name in the **top-right corner** of the Zooza admin panel.
2. Select **Account settings** (or **Profile**).
3. Find the **Language** field and choose your preferred language.
4. Save.

The interface reloads in the selected language immediately. Each admin and instructor can set their own preferred language independently — this does not affect the client-facing widgets or emails.

> **Note:** The Zooza logo in the top-left corner does **not** contain a language switcher. The correct path is always via the profile icon in the **top-right**.

Available languages: Slovak, English, Czech, Hungarian, Romanian.

For more detail — including how to change the language of client-facing widgets and emails — see [Change the language in Zooza](../guides/interface-language-settings.md).

## How do I switch Zooza to dark mode?

Zooza does not have an independent dark/light mode setting. The app follows your **browser's or operating system's theme preference**. If your browser or OS is set to dark mode, Zooza will appear in dark mode automatically.

To change the theme: update your system display settings (macOS: System Settings → Appearance; Windows: Settings → Personalisation → Colours) or your browser's appearance settings. The change takes effect immediately in Zooza without needing to refresh.

## How do I create a test or sandbox Zooza account?

Zooza does not provide a dedicated sandbox environment, but you can set up a separate test account using the **Try for FREE** flow on the Zooza website.

1. Go to the Zooza sign-up page and register a new free account.
2. Use a name that makes it clear the account is for testing — for example, "Playground", "Test account", or include your name: "ELA playground".
3. Use a different email address from your main account (or a sub-address like `yourname+test@domain.com` if your provider supports it).

The free account gives you access to the full Zooza feature set up to the Free plan limit (up to 10 active clients). This is enough to test programme setup, booking forms, payment flows, email templates, and widget embedding without affecting your live account data.

> Keep the test account separate — do not connect it to live payment providers (Stripe, GoCardless) unless you are specifically testing payment integrations. Use the test/sandbox modes of those providers in your playground account.

## Is there a Zooza mobile app to download?

Zooza is a web application — there is no native app to download from the App Store or Google Play. You access it through a browser at **zooza.app**. This is intentional:

- **No installation required** — parents and instructors can open the app immediately on any device or browser without going through an app store.
- **Always up to date** — web updates deploy instantly. There is no "please update your app" friction.
- **Works everywhere** — any phone, tablet, or desktop with a modern browser.
- **Lower barrier for clients** — asking clients to install a native app creates friction. A link they click in an email just works.

You can add it to your phone's home screen so it behaves like an app:

**iPhone (Safari):**
1. Open zooza.app in Safari.
2. Tap the share icon (square with an arrow pointing up).
3. Tap **Add to Home Screen**.

**Android (Chrome):**
1. Open zooza.app in Chrome.
2. Tap the three-dot menu (top right).
3. Tap **Add to Home screen**.

The icon will appear on your home screen and the app will open in full-screen mode.

## Related

- [Getting started with Zooza](../setup/getting-started-with-zooza.md) — initial setup and orientation
- [How to clear your cache](../troubleshooting/how-to-clear-your-cache.md) — fix display issues by clearing browser cache
- [App navigation map](../reference/app-navigation-map.md) — overview of the Zooza interface
- [Getting help and support](../guides/getting-help-and-support.md) — how to contact Zooza support
