---
title: "Track campaigns and conversions from the contact form"
description: "See which Meta or Google campaign each enquiry came from, tag enquiries with hidden fields, and count enquiries as conversions in GTM, GA4 and Meta Pixel."
slug: "contact-form-campaign-tracking"
type: "guides"
product_area: "Widgets"
sub_area: ""
audience: ["admin"]
tags: ["contact form", "lead capture", "campaigns", "utm", "meta pixel", "google tag manager", "conversions", "attribution", "marketing"]
related_articles: ["contact-form-lead-capture", "contact-form-setup", "contact-form-on-your-website", "working-with-contacts", "custom-contact-fields", "customizing-widgets"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-09-17"
---

# Track campaigns and conversions from the contact form

If you pay for ads, you want two answers: which campaign each enquiry came from, and how many enquiries each campaign produced. The [contact form](contact-form-lead-capture.md) gives you both without extra setup. Every enquiry records where the visitor came from, and the widget tells your analytics tools when a form is shown and sent.

## What every enquiry records

| Recorded | Where it comes from |
|---|---|
| Page | The address of the page the form was sent from |
| Referrer | The page the visitor came from, as reported by the browser |
| UTM source, medium, campaign, term, content | The `utm_` parameters in the page address |
| Meta click id | The `fbclid` parameter Meta adds to ad links |
| Google click id | The `gclid` parameter Google Ads adds to ad links |

You see these on the contact's timeline under the enquiry, and you filter the Contacts list by **UTM source**, **UTM medium** and **UTM campaign**.

## A campaign, step by step

Say you run a Meta campaign for autumn swimming lessons.

1. Create a page on your website with the contact form and a short pitch. Keep the form to a name, email or phone, and one question such as *Child's age*.
2. Point the ad at that page with UTM parameters in the link, for example `https://www.example.com/swimming?utm_source=meta&utm_medium=paid&utm_campaign=autumn-swimming`.
3. In the form configuration, set the **Contact owner** to whoever follows up, add a **Label** such as *Autumn 2026*, and switch on **Create a to-do for each enquiry**. See [Set up a contact form](../setup/contact-form-setup.md).
4. Launch. Each enquiry arrives as a contact with `utm_campaign = autumn-swimming`, the label, an owner and a to-do.
5. In **Clients → Contacts**, filter by **UTM campaign** to see the campaign's contacts and how many are **Converted**. That is your cost per enquiry and per client, next to the ad spend in Meta.

The same works for Google Ads, newsletters and partner links. Anything that can carry `utm_` parameters in its link is attributed.

## When the visitor arrives on one page and sends the form on another

Campaign parameters are read from the address of the page where the form is sent. If the ad leads to your home page and the visitor sends the form from your contact page three days later, the parameters are gone by then.

Switch on **Remember where the visitor first came from** in the form configuration. The widget then stores the campaign parameters in the visitor's browser the first time it loads with them, and attaches them to the enquiry later. The first campaign wins. Choose how long to remember them with **Remember for (days)**, 1 to 90. Only the campaign parameters are stored, no personal data.

Two things to know:

- This stores data in the visitor's browser, which most cookie consent managers treat as marketing tracking. Turn it on only if your website asks for that consent.
- Parameters are captured only on pages where the contact form is embedded. If your ads land on a page without the form, put the form there too, or link the ad to the page with the form.

## Tag enquiries with a hidden field

Hidden fields let you attach information to an enquiry without asking the visitor. Create a [custom contact field](../setup/custom-contact-fields.md), add it to the form, mark it **Hidden** and choose where its value comes from.

**One form, several location pages.** Create a field `location`, source **Embed code attribute**, source name `location`. On each page, add the value to the embed code:

```html
<div data-zooza-widget='contact' data-zooza-id='YOUR_WIDGET_KEY'
     data-zooza-field-location='london'></div>
```

Every enquiry now carries its location, and each manager filters Contacts by their own.

**A campaign variant that UTM does not cover.** Source **URL parameter** with source name `ref` reads `?ref=flyer-spring` from the page address. Print different links on different flyers.

**A fixed value per configuration.** Source **Fixed value** stamps every enquiry from that configuration, for example `website` on your main form and `open-day` on the form used at the open day.

## Count enquiries as conversions in GTM, GA4 and Meta Pixel

The widget fires three events on the page. They go to Google Tag Manager's data layer, to GA4 and to Meta Pixel, whichever of them is already installed on your website. There is nothing to set up in Zooza and nowhere to paste a pixel. If your site has no tag manager, the events do nothing.

| Event | Fires when |
|---|---|
| `zooza_event_contact_form_view` | The form is shown to the visitor, once per page load |
| `zooza_event_contact_form_submit_start` | The visitor clicks send and the form passes validation |
| `zooza_event_contact_form_submitted` | Zooza has accepted the enquiry, just before the thank-you message or the redirect |

Use `zooza_event_contact_form_submitted` as your lead conversion. Each event carries `zooza_contact_form_id`, the number of the configuration, so you can tell forms on different pages apart. No name, email, phone or message is ever included.

- **Google Tag Manager**: create a **Custom Event** trigger with the event name and attach your GA4 event tag or Google Ads conversion tag to it.
- **GA4 with gtag**: the event arrives as a custom event of that name. Mark it as a conversion in GA4.
- **Meta Pixel**: the event arrives as a custom event of that name. In Events Manager, create a custom conversion from it, or map it to the standard *Lead* event.

If the configuration redirects the visitor to a thank-you page, the redirect happens right after the event fires. Tags that must fire on the conversion should use the event trigger, not a page view of the thank-you page. This is the same mechanism the booking form uses; see [Tracking conversions](customizing-widgets.md#tracking-conversions-meta-pixel-google-analytics).

**Spam enquiries fire the events too.** Zooza gives spam the same thank-you response as a genuine enquiry so that bots cannot tell the difference, and the widget cannot tell either. Expect a small gap between conversions counted on the page and contacts in Zooza.

## Marketing consent

Attribution tells you where a contact came from. Consent tells you what you may do next. Give one of your contact form consents the category **Marketing** in **Consents & Agreements**, add it to the form, and every contact who accepts it shows **Marketing consent: Yes** with the date. Contacts who did not accept it should not receive newsletters, however they found you.

## Related

- [Contact form (lead capture): turn website enquiries into contacts](contact-form-lead-capture.md)
- [Set up a contact form](../setup/contact-form-setup.md)
- [Put the contact form on your website](../setup/contact-form-on-your-website.md)
- [Work with contacts and enquiries](working-with-contacts.md)
- [Custom contact fields](../setup/custom-contact-fields.md)
- [Customizing widgets](customizing-widgets.md)
