---
title: "Parent Portal FAQ"
slug: "parent-portal-faq"
type: "faq"
product_area: "Widgets"
sub_area: ""
audience: ["admin"]
tags: ["widgets"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-13"
intercom_id: 13728494
intercom_sync: false
---

# Parent Portal FAQ

## How do parents log into the Parent Portal?

Parents go to your portal URL (e.g., `yourbrand.zooza.online/customer-portal/`), enter their email address, and receive a secure login link (token) by email. There is no password — each login sends a fresh email link.

## A parent says they are not receiving the login email — what should I do?

Check the following:

1. Confirm the email address matches what is registered in Zooza.
2. Ask the parent to check their spam/junk folder.
3. Try sending the login email again from the admin side.
4. If using a corporate or Outlook email, there may be filtering delays — the email usually arrives within a few minutes.

If the issue persists, contact support to check the email delivery logs.

## What can parents see and do in the Parent Portal?

Parents can:

- View their active bookings and upcoming sessions.
- Complete outstanding payments.
- Book catch-up / make-up classes (if enabled).
- View their child's attendance history.
- Access trial-to-enrolment offers.

If a parent has an outstanding balance, the first thing they see is a prompt to complete payment.

## A parent booked a trial but cannot see it in the portal — why?

There are two possibilities:

1. The parent submitted an **enquiry form** instead of a trial booking. Enquiries do not create a booking — they wait for admin follow-up. Check the enquiries filter in the bookings section.
2. The trial booking exists but the portal display may not be immediately obvious. Direct the parent to scroll down or check their email for the confirmation link.

## How do parents book catch-up / make-up classes?

When a session is cancelled or the parent marks an absence, the system can offer catch-up options. The parent sees available catch-up sessions in their portal and can select one. Catch-up availability depends on real capacity — if no suitable session with space is available, the option will not appear.

## A parent keeps seeing the GDPR consent screen in a loop — what is happening?

This is a known issue where the consent acceptance does not persist. It is usually caused by browser cookies or privacy settings blocking Zooza storage. Ask the parent to:

1. Clear their browser cache and cookies.
2. Try a different browser (e.g., switch from Safari to Chrome).
3. Disable strict cookie blocking or tracking protection for the portal domain.

If the issue persists after all three steps, contact Zooza support — there may be a platform-side fix required.

<!-- REVIEW: Multiple support conversations confirm this is a recurring issue (GDPR consent loop). No permanent server-side fix documented yet. -->

## A parent sees outdated data (old replacement options, old schedule) in their portal — how to fix?

Ask the parent to clear their browser cache or open the portal in a private/incognito window. The portal caches data locally in the browser.

On mobile, they can also try fully closing and reopening the browser app.

As an admin, there is no server-side cache to clear — the stale data is stored on the parent's device.

## A parent is confused because they went to zooza.online instead of our portal — what should I do?

Direct parents to your specific portal URL (e.g., `your-brand.zooza.online` or your website widget), not to `zooza.online`. If they create an account on `zooza.online` directly, it may not link to your school's data.

To prevent this, include your direct login link in all parent-facing communications. You can use the `WIDGET_PROFILE_URL` dynamic tag in your email or message templates to automatically insert the correct URL.

## What conditions are needed for the "Sign back up for this session" button to appear?

The button appears when all of the following conditions are met:

1. The client previously unsubscribed from the session.
2. The session has not yet occurred.
3. There is available capacity in the session.
4. The re-enrollment window has not expired.

If any of these conditions is not met, the button will not appear. Check session capacity and timing if a parent reports the button is missing.

<!-- REVIEW: Re-enrollment window duration is configurable per programme — confirm exact setting location in programme settings. -->
