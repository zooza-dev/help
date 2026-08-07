---
title: "Share a course or class registration link"
description: "Use the Share button to copy, open, or email a registration link for a course or class to prospective clients."
slug: "share-course-link"
type: "guides"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: ["sharing", "registration-link", "email", "widget"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-08-07"
related_articles: ["customizing-widgets", "creating-entry-passes"]
---

# Share a course or class registration link

The **Share** button on courses and classes lets you copy, open, or email a registration link directly from the admin panel — without leaving Zooza.

## Where to find the Share button

The Share button appears in two places:

- **Course or class detail** — in the action bar at the top of the page.
- **Classes list** — on each class card in the list view.

It replaces the old "Copy link" control.

## Using the Share modal

Click **Share** to open the sharing modal. Work through the sections in order:

### 1. Choose a widget

If your account has more than one booking widget, select which widget the registration link should point to. The link is rebuilt to open that specific widget.

If you only have one widget, this step is skipped automatically.

### 2. Copy or open the link

- **Copy link** — copies the registration URL to your clipboard. Paste it anywhere: email client, WhatsApp, social media post.
- **Open link** — opens the registration page in a new browser tab so you can preview it before sharing.

### 3. Create a custom link

Generate a personalised registration link (e.g. with a referral parameter or a pre-filled discount code). This works the same as the previous custom-link feature.

A custom link also works as a **private link**: it can point to a class that is **not** open for online booking, and anyone holding the link can still book it. Use this to fill a class quietly, to reopen a closed class for one family, or to invite a specific group before public registration starts.

## Sharing a product

Products have the same pair of buttons, in the same place:

1. Go to **Products & Services → Products**.
2. Open the product.
3. Use **Open** or **Copy** at the top of the product detail.

**Copy** gives you the product's own checkout link — send it by email, WhatsApp, or anywhere else. This is how you sell a gift voucher or an entry pass to someone who is not booking a class.

> **There is no dynamic tag for a product link.** Tags such as `*|BOOKING_URL|*` produce a booking link for a class, never a product. Paste the copied product URL into the email body as plain text instead.

When you paste a link into a message template, remember that dynamic tags need the asterisks on both sides — `*|FIRST_NAME|*` renders, `|FIRST_NAME|` does not.

### 4. Share by email

Send the registration link directly to email addresses without leaving Zooza.

1. Type one or more email addresses in the recipients field.
2. Press **Enter** or **Tab** after each address to add it as a chip.
3. Click **Send**.

Zooza sends each recipient a branded email with a **Register** button linking to the class registration page. The email is sent from a Zooza no-reply address — recipients cannot reply to it.

**Limits and anti-spam rules:**

| Rule | Detail |
|---|---|
| Maximum recipients per send | 10 |
| Non-customer rate limit | 1 shared-link email per email address per 24 hours |
| Existing clients (your customers) | Exempt from the 24-hour limit |
| Rejected batch behaviour | If any address has already received a shared link in the last 24 hours, **the entire batch is rejected** — no emails are sent. Remove the flagged address(es) and try again. |

> **Why the 24-hour cap?** The share-by-email feature is for reaching specific prospective clients. The cap prevents accidental or repeated spam to people who haven't asked to hear from you.

**Email template:** The shared-link email uses a fixed system template and cannot be customised per company. It includes your company name and branding.

## Related

- [Customizing widgets](customizing-widgets.md) — configure which widget the link points to
- [Creating entry passes](creating-entry-passes.md) — sell a pass alongside sharing the class link
