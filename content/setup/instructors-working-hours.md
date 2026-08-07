---
title: "Instructors working hours"
description: "In the Instructors section, instructors can manage their working time. If they define their working hours and possible absences, this data will then..."
slug: "instructors-working-hours"
type: "setup"
product_area: "Settings"
sub_area: ""
audience: ["admin"]
tags: ["booking", "cancellation", "discount", "instructor", "role", "settings"]
status: "published"
source_legacy_path: "legacy/0066_Welcome to Zooza.html"
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-11"
---

# Instructors working hours

In the *Instructors *section, instructors can manage their working time. If they define their working hours and possible absences, this data will then be taken into account by the system when scheduling terms.

![In the Instructors section, instructors can manage their working time. If they define...](../../assets/images/allowing-multiple-registration-03.png)

Example: Alice works Tuesdays to Fridays from 9:00 to 16:00 with an hour lunch break.

## 1. Setting working hours

- In the application, she clicks on the *Add Availability* button
- As the type selects *Working Hours*
- Selects a date range. In our example we choose 4th. January to 7th. January.
- As the time range selects 9:00 to 16:00
- She activates repetition at a weekly frequency. Depending on how long such working hours will be valid, the number of repetitions will be chosen.

![She activates repetition at a weekly frequency. Depending on how long such working...](../../assets/images/lecturers-working-hours-02.png)

- On the calendar in the app, availability will be displayed as follows:

![On the calendar in the app, availability will be displayed as follows](../../assets/images/lecturers-working-hours-03.png)

## Step 2 - Lunch break

- Since Alice goes out for lunch in the middle of the day, she needs to tell the system that she doesn't work then.
- Again clicks the *Add Availability* button
- This time she selects the *Absence* option and enters the same data as before, except that the time period will be from 11:30 to 12:30
- She chooses the name of this absence: lunch break.
- The resulting calendar will look like this:

![The resulting calendar will look like this](../../assets/images/lecturers-working-hours-04.png)

## How availability works when creating terms

From now on, when scheduling terms, the app will inform the admin that Alice is unavailable for appointments at lunchtime.

![From now on, when scheduling terms, the app will inform the admin that Alice is...](../../assets/images/lecturers-working-hours-05.png)

## An instructor's holiday is not a company holiday

These are two different settings and choosing the wrong one is a common mistake.

| What you want | Where it goes |
|---|---|
| One instructor is away (holiday, illness, a term abroad) | **Instructors → their profile → Working hours →** add an **Absence** for that date range |
| Your whole business is closed (summer break, public holiday, a company event) | **Team & Settings → General → Custom holidays** |

An **Absence** only removes that person from scheduling. Sessions still exist and other instructors can still be assigned to them.

A **Custom holiday** blocks the dates for everyone, and only affects sessions generated *after* it is created — see [Custom holidays](../guides/custom-holidays.md).

> If an instructor asks how to register their summer holiday, send them to their own **Working hours**, not to Settings. Instructors do not usually have access to the company holiday settings, and even if they do, entering their personal holiday there would close the business for everyone.

## Mass deleting of availability/absences

Since the availability of instructors can change frequently in the application, you have the option of mass deletion. This allows you to edit faster.

1. In the instructor's details under *Working hours*, click *Activate*.
 ![In the instructor's details under Working hours, click Activate](../../assets/images/lecturers-working-hours-06.png)
2. Select the availability/absences you want to delete by clicking on them and click on the *Delete selected availability* button.

![Select the availability/absences you want to delete by clicking on them and click on...](../../assets/images/lecturers-working-hours-07.png)

![Select the availability/absences you want to delete by clicking on them and click on...](../../assets/images/discount-code-01.png)

Note: You can only do a mass deletion within one month. If you move to the next month, your previous withdrawal will be cancelled
