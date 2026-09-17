---
title: "Contact form and contacts FAQ"
description: "Answers about the Zooza contact form (lead capture) and Contacts: missing test enquiries, allowed domains, notifications, spam, GDPR and converting to a client."
slug: "contact-form-and-contacts-faq"
type: "faq"
product_area: "Clients"
sub_area: ""
audience: ["admin"]
tags: ["contact form", "lead capture", "contacts", "enquiries", "faq", "widget", "spam", "gdpr"]
related_articles: ["contact-form-lead-capture", "contact-form-setup", "custom-contact-fields", "contact-form-on-your-website", "working-with-contacts", "contact-form-campaign-tracking", "lead-collection"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-09-17"
---

# Contact form and contacts FAQ

## What is the difference between a contact, a client and a lead collection class?

A **contact** is a person who enquired, through the contact form on your website or added by hand. They have no login and no booking, and they do not appear in the Clients list. A **client** is someone with a booking or a client account. A **lead collection class** is a class without sessions inside an existing programme; registering for it creates a booking, not a contact. Use the contact form to collect interest before anything exists, and lead collection when the programme exists and you only lack the timetable. See [Contact form (lead capture)](../guides/contact-form-lead-capture.md) and [Lead collection](../guides/lead-collection.md).

## Where do I find the contact form and the contacts?

- The enquiries: **Clients → Contacts**.
- What the form asks: **Team & Settings → General → Contact forms**.
- Your own questions: **Team & Settings → General → Custom contact fields**.
- The embed code and allowed domains: **Team & Settings → Publish**, your widget, the **Contact form** row.

## I sent a test enquiry and it is not in Contacts

Check these in order:

1. **Clients → Contacts → Spam.** Test enquiries sent within three seconds of the page loading, containing several links, or with the same text in every field are treated as spam. Click **Not spam** to rescue it, and send the next test the way a real person would.
2. **More than five enquiries in an hour from the same email address** are dropped without a trace. Wait, or use another address.
3. **Team & Settings → General → Contact forms**, the **Form on your website** card. If it says **Blocked domain**, the page is not on an allowed website. Click **Allow**.

The thank-you message appears in all of these cases, so the form looking fine is not proof the enquiry arrived.

## The form does not load on my website

The website must be on the widget's domain, on the domain of the widget's contact form `URL`, or in its **Additional domains**. Subdomains are covered automatically, other domains are not. Open **Team & Settings → General → Contact forms** and look at the **Form on your website** card: it names the blocked domain and offers **Allow**. A staging site on another domain and a local copy of the site each need their own entry. See [Put the contact form on your website](../setup/contact-form-on-your-website.md).

## Can I put two contact forms on one page?

No. One contact form per page. The second placeholder shows a notice instead of a form. Use one form per page, and as many pages as you like.

## Does the WordPress plugin shortcode work for the contact form?

No. Paste the embed code into a **Custom HTML** block on the page.

## Who is emailed when an enquiry arrives?

Everyone listed under **New contact enquiry** in **Notification center**, plus the addresses in the form's **Also notify** list. The email contains the name, contact details, message, custom field answers and campaign, with a link to the contact. Replying to the email answers the enquirer directly.

## The visitor did not receive the automatic reply

Check that **Send an automatic reply** is on in the form configuration, and that the enquiry had an email address. A contact receives at most one automatic reply per 24 hours, so a second test from the same address gets none. Enquiries rescued from Spam more than an hour after they were sent get none either.

## Can I change the text of the automatic reply?

Yes. Edit **Contact form - automatic reply** in **Communication → Templates**. It can use the visitor's first name and the form name. To send different text from one form, make a copy of the template as a variant and select it in that form's **Automatic reply template**. See [Message templates](../guides/message-templates.md).

## Can I add a contact to a class directly?

Not from the contact. Click **Convert to client** first, then create their booking as usual. Zooza creates the client from the contact's name, email and phone, without sending them anything.

## The contact is already my client

Zooza matched the enquiry's email address to one of your clients and linked them. The contact shows **Existing client** and a link to open the client. If the person used a different email address, use **Link to client** and pick them.

## What happens when the same person sends the form again?

The enquiry is added to the same contact as a second timeline entry, matched by email address. Details that were empty are filled in from the new enquiry. Nothing is overwritten. The contact's status does not change. If the form asks for phone only, matching uses the phone number.

## Can I see which campaign a contact came from?

Yes. Each enquiry records the page, the referrer, the UTM parameters and the Meta and Google click ids. Filter Contacts by **UTM source**, **UTM medium** or **UTM campaign**. See [Track campaigns and conversions](../guides/contact-form-campaign-tracking.md).

## Can I count enquiries as conversions in Meta Pixel or Google Analytics?

Yes. The widget fires `zooza_event_contact_form_submitted` to Google Tag Manager, GA4 and Meta Pixel when an enquiry is accepted. Use it as your lead conversion. Nothing needs to be pasted into Zooza. See [Track campaigns and conversions](../guides/contact-form-campaign-tracking.md).

## Can instructors see contacts?

Anyone who can view clients can view contacts. Editing contacts, notes, to-dos, spam rescue and conversion need the permission to edit clients. Setting up forms, fields and the widget needs the permission to edit company settings. See [Roles and permissions FAQ](roles-and-permissions-faq.md).

## Can I export contacts to CSV?

Not yet. Contacts also have no bulk actions yet.

## Can I change a custom field's type or key?

No. The key and type are fixed once the field is created, so that earlier answers keep their meaning. Create a new field instead and archive the old one. Labels and option labels can be changed at any time. See [Custom contact fields](../setup/custom-contact-fields.md).

## How do I delete a contact for a GDPR request?

Open the contact and click **Erase contact**. This permanently deletes the contact with its enquiries, notes and labels. If the contact was converted, the client is not deleted; handle the client separately.

## Why is there a "Marketing consent" on the contact?

It shows *Yes* when the person accepted a consent in the **Marketing** category on the form. Categories are set per consent in **Consents & Agreements**. Use it to decide who may receive newsletters.

## Can I change the wording of the form, such as the Send button?

The button, the standard field labels and the validation messages are changed per page with a small script before the widget, the same way as for the booking form. Custom field labels, consent texts and the success message are edited in the form configuration. See [Put the contact form on your website](../setup/contact-form-on-your-website.md#match-your-websites-look-and-wording).

## Related

- [Contact form (lead capture): turn website enquiries into contacts](../guides/contact-form-lead-capture.md)
- [Set up a contact form](../setup/contact-form-setup.md)
- [Custom contact fields](../setup/custom-contact-fields.md)
- [Put the contact form on your website](../setup/contact-form-on-your-website.md)
- [Work with contacts and enquiries](../guides/working-with-contacts.md)
- [Track campaigns and conversions from the contact form](../guides/contact-form-campaign-tracking.md)
