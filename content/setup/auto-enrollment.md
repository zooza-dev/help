---
title: "Auto-enrollment"
description: "Auto-enrollment is used for efficient programme enrollment for existing clients with a pre-filled booking form."
slug: "auto-enrollment"
type: "setup"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: ["booking", "class", "client", "import", "location", "payment", "programme", "session", "widget"]
status: "published"
source_legacy_path: "legacy/0057_Welcome to Zooza.html"
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-11"
---

# Auto-enrollment

Auto-enrollment is used for efficient programme enrollment for existing clients with a pre-filled booking form. This allows the client to receive priority enrollment in a new period (for class programmes) or to select a new date for individual sessions, so that you can arrange further continuation via Zooza.


1. Priority enrollment for existing clients, whom you want to offer programmes before displaying them on your website. 
2. In this case, we recommend disabling online registration for these programmes (in the programme settings, *Online Registration*) or performing a bulk edit also in the* Online Registration* tile and disabling *Online Registration *only for the new classes you wish to offer priority enrollment to.
 ![Screenshot](../../assets/images/auto-enrollment-01.png)

In the case of individual programmes, this feature lets you arrange the start of the next class with the client without manually preparing the class beforehand, exactly according to their preferences.

![Screenshot](../../assets/images/auto-enrollment-02.png)


To successfully use auto-enrolment, you need to have created an offer of programmes and classes before activating the settings.

Auto-enrollment is configured in 2 places:


1. At the programme level in tile *Auto-enrollment*
2. At the class level in the *Settings* tile

## 1. At the programme level


First, you need to set which programmes and classes you want to offer clients for enrollment in the new period.


1. Open the settings of the selected programme.
 ![Screenshot](../../assets/images/auto-enrollment-03.png)
2. In *Auto-enrollment* tile click on *Edit*
 ![Screenshot](../../assets/images/auto-enrollment-04.png)
3. Select the type of offer:
4. *Suggest classes *- for group classes and follow-up programmes
5. *Duplicate current class* - ideal for individual clients.
 ![Screenshot](../../assets/images/auto-enrollment-05.png)

Enter how many days before the end of the current term the system should notify clients.


![Screenshot](../../assets/images/auto-enrollment-06.png)

![Screenshot](../../assets/images/client-import-01.png)

Note: If you have manually set the class end date to a different day, the system will use this manual date instead of the last scheduled date.


## Suggest classes


If you have class ccourses and would like to offer existing clients the option to enroll before opening booking to new clients, select the *Suggest Classes* type of auto*-*enrollment


1. Define the offer:
2. Billing period
3. Filter specific programmes (All programmes, Only the billing period the client enrolled for, Selected programmes only)
4. Age restriction - e.g. offer only for children within a selected age range at the time of booking – enter months or years

![Screenshot](../../assets/images/client-import-03.png)

Attention! Only programmes with an age restriction filled in under *Extra Fields* will be included in the offer.

1. Distance (set the maximum distance in km from the location where the client is currently enrolled)
 ![Screenshot](../../assets/images/auto-enrollment-09.png)


 2. Finally, select classes you want to include in the auto-enrolment.


![Screenshot](../../assets/images/auto-enrollment-10.png)

## Duplicate current class


This option allows the client to choose when they want to start the next class – especially suitable for individual sessions. Details on how this option works on client's side can be found in the *Client View *section of this manual.

*

![Screenshot](../../assets/images/auto-enrollment-11.png)


*


## At the class level


If the auto-enrolment functionality is active and you need to add another class to the programme (or simply want to expand the list of classes for auto-enrolment), open the *Settings *tile. There you will find a checkbox to add the selected class to the auto-enrolment offer.

![Screenshot](../../assets/images/auto-enrollment-12.png)

![Screenshot](../../assets/images/client-import-01.png)

Note: If the programme does not have auto-enrolment enabled, the application will notify you and even if the checkbox is selected, this setting will be ignored.

## Tracking responses

After invitations are sent, monitor who accepted, declined, or has not yet responded in the **Auto-enrolment responses** page or via the Bookings list filter.

See: [Monitoring auto-enrolment responses](../guides/auto-enrolment-responses.md)

## Troubleshooting — classes not appearing in the offer

If clients see fewer classes than expected, or a newly created class is missing from the auto-enrolment offer, work through these checks in order:

**1. Class-level checkbox not enabled**
The most common cause. Each class must be individually opted in.
Go to the class → **Settings** tile → enable **Include in auto-enrolment**. This must be done for every new class you add after the programme-level setting is saved.

**2. Programme filter is set to "Selected programmes only"**
If you chose *Selected programmes only* when configuring the offer, new programmes are not included automatically. Return to the programme's **Auto-enrollment** tile, edit the offer, and add the new programme to the selection list.

**3. Age restriction filter is active**
If you set an age restriction on the offer, only programmes that have an age range defined under **Extra Fields** will appear. Programmes without an age restriction are silently excluded. Either remove the age filter or add the age range to the programme's Extra Fields.

**4. Distance filter is too narrow**
If you set a distance limit, classes at venues beyond that radius won't appear. Increase the distance or remove the limit.

**5. The offer is for a different billing period**
If the offer is filtered to a specific billing period, only programmes in that period appear. A newly created programme in a different billing period won't show.

### Offering a different programme at continuation (e.g. BBS → TBS)

Auto-enrolment can offer clients a completely different programme — not just the same one. Use the **Selected programmes only** filter and manually add the target programme (e.g. TBS) to the offer list on the source programme (BBS). Clients enrolled in BBS will see TBS classes in their auto-enrolment invitation.
