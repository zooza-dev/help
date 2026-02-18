---
title: "Client Profile FAQ"
slug: "client-profile-faq"
type: "faq"
product_area: "Widgets"
sub_area: ""
audience: ["admin"]
tags: ["widgets", "client-profile", "parent-portal"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-15"
intercom_id: 13728494
intercom_sync: true
---

# Client Profile FAQ

## How do clients log into the Client Profile?

Clients go to your profile URL (e.g., `yourbrand.zooza.online/customer-portal/`), enter their email address, and receive a secure login link (token) by email. There is no password — each login sends a fresh email link.

## A client says they are not receiving the login email — what should I do?

Check the following:

1. Confirm the email address matches what is registered in Zooza.
2. Ask the client to check their spam/junk folder.
3. Try sending the login email again from the admin side.
4. If using a corporate or Outlook email, there may be filtering delays — the email usually arrives within a few minutes.

If the issue persists, contact support to check the email delivery logs.

## What can clients see and do in the Client Profile?

Clients can:

- View their active bookings and upcoming sessions.
- Complete outstanding payments.
- Book catch-up / make-up sessions (if enabled).
- View their attendance history.
- Access trial-to-enrolment offers.

If a client has an outstanding balance, the first thing they see is a prompt to complete payment.

## A client booked a trial but cannot see it in their profile — why?

There are two possibilities:

1. The client submitted an **enquiry form** instead of a trial booking. Enquiries do not create a booking — they wait for admin follow-up. Check the enquiries filter in the bookings section.
2. The trial booking exists but the profile display may not be immediately obvious. Direct the client to scroll down or check their email for the confirmation link.

## How do clients book catch-up / make-up sessions?

When a session is cancelled or the client marks an absence, the system can offer catch-up options. The client sees available make-up sessions in their profile and can select one. Catch-up availability depends on real capacity — if no suitable session with space is available, the option will not appear.

## A client keeps seeing the GDPR consent screen in a loop — what is happening?

This is a known issue where the consent acceptance does not persist. It is usually caused by browser cookies or privacy settings blocking Zooza storage. Ask the client to:

1. Clear their browser cache and cookies.
2. Try a different browser (e.g., switch from Safari to Chrome).
3. Disable strict cookie blocking or tracking protection for the profile domain.

If the issue persists after all three steps, contact Zooza support — there may be a platform-side fix required.

<!-- REVIEW: Multiple support conversations confirm this is a recurring issue (GDPR consent loop). No permanent server-side fix documented yet. -->

## A client sees outdated data (old make-up options, old schedule) in their profile — how to fix?

Ask the client to clear their browser cache or open the profile in a private/incognito window. The profile caches data locally in the browser.

On mobile, they can also try fully closing and reopening the browser app.

As an admin, there is no server-side cache to clear — the stale data is stored on the client's device.

## A client is confused because they went to zooza.online instead of your profile — what should I do?

Direct clients to your specific profile URL (e.g., `your-brand.zooza.online` or your website widget), not to `zooza.online`. If they create an account on `zooza.online` directly, it may not link to your data.

To prevent this, include your direct login link in all client-facing communications. You can use the `WIDGET_PROFILE_URL` dynamic tag in your email or message templates to automatically insert the correct URL.

## What conditions are needed for the "Sign back up for this session" button to appear?

The button appears when all of the following conditions are met:

1. The client previously cancelled the session.
2. The session has not yet occurred.
3. There is available capacity in the session.
4. The re-enrollment window has not expired.

If any of these conditions is not met, the button will not appear. Check session capacity and timing if a client reports the button is missing.

<!-- REVIEW: Re-enrollment window duration is configurable per programme — confirm exact setting location in programme settings. -->

## How do I pay an outstanding balance in the Client Profile?

Go to the **Payments** section in your profile, open the unpaid item, and click to continue to the payment gateway (if online payment is enabled by your provider). If your provider uses bank transfers, you will see the payment instructions instead. After payment, the status updates automatically.

## How do I switch between my children in the profile?

At the top of the Client Profile, you see your family members (children or attendees). Click a name or avatar to switch. Sections like bookings and sessions change per child, while some sections (orders, family-level discounts) are shared and stay the same.

## Where can I see my remaining entry pass entries?

Your entry pass status is shown on the home page of the Client Profile and in the **Benefits** section. You can see the pass name, remaining entries, and expiration date. For details, see [Entry pass — client view](../guides/entry-pass-client-view.md).

## Why do I not see a make-up session option?

Make-up sessions only appear when:

1. Your provider has enabled make-up sessions for the programme.
2. You have cancelled or missed a session.
3. There is an available session with free capacity in the allowed time window.

If none of these conditions are met, the make-up option does not appear. Contact your provider if you believe you should have a make-up available.

## Why does some data not change when I switch between children?

Some sections in the Client Profile are shared across the family — they are tied to the parent account, not to a specific child. This includes family-level orders, some discounts, and payments that are not linked to one child. This is normal behaviour.

## Can I share my booking with another parent or family member?

Yes. In the booking details, you can share access with another person (e.g., another parent, a grandparent). They will receive notifications and updates related to the booking. See the **Sharing a booking** section in [Client Profile 101](../guides/client-profile-101.md).

## Can I download invoices from the Client Profile?

If your provider enables invoicing, invoices are available in the payments or orders section of the Client Profile. Open the relevant payment or order and look for a download option. Not all providers enable this feature — contact your provider if you do not see invoices.

## The profile looks different from what I expected — is something wrong?

The Client Profile is embedded on your provider's website and usually matches their branding (colours and style). If you accessed `zooza.online` directly instead of your provider's website, you may not see the correct data. Use the login link from your provider's email or website instead.
