---
title: "How to create paid events?"
slug: "how-to-create-paid-events"
type: "guides"
product_area: "Classes"
sub_area: ""
audience: ["admin"]
tags: []
status: "published"
source_legacy_path: "legacy/0044_Welcome to Zooza.html"
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-11"
intercom_id: 13725819
intercom_sync: false
---

# How to create paid events?

The paid appointments functionality is a way for Zooza to “know” how many appointments in a group should be paid. For various reasons, sometimes the dates in a group do not match the number of paid dates. For example:

- In a full course – add a “Free of charge
lesson/event” to the schedule as a credit for “cancelled” lessons. This
increases the number of events within the group and when Zooza
calculates the unit price, it uses all these events and has no way of
knowing that a particular event is free/unpaid.
- In language school – custom replacement lessons also create more events in the group than originally set by the admin.

In other words, paid events are a contract between company and
customer, where you agree that the client will pay for e.g. 12 lessons.
Whether the group has 4 or 20 lessons, the price always applies to 12
lessons.

The point of this functionality is as follows: clients can have a
different number of lessons in a group than what is actually paid for.

## How to set it up?

Setting up paid events needs to be synchronized at three levels: course, group and lesson.

1. In *Courses* section of > *Price and Payment* section there is a field – *Billable events*. By filling out this setting it will make it the default value for all groups within the course.
 ![Screenshot](../../assets/images/how-to-create-paid-events-01.png)
2. In *Groups* > *Price and Payment* – *Billable Events* -the same setting as in the course, but if the field is populated in a
group, it will override the setting on the course. This allows groups to
 have an individual number of billable events.

![Screenshot](../../assets/images/discount-code-01.png)

Attention! If a course has billable events set and the setting on the group is 0,
it will always use the course value That means if a course has billable
events set to 12, groups within this course cannot have 0 such events.

![Screenshot](../../assets/images/how-to-create-paid-events-03.png)

 3. In Lessons/events section:

1. mark events as *Billable* when creating them

![Screenshot](../../assets/images/how-to-create-paid-events-04.png)

1. in Event detail open Event settings and find a field called *Billable *event
 ![Screenshot](../../assets/images/how-to-create-paid-events-05.png)
 ![Screenshot](../../assets/images/how-to-create-paid-events-06.png)

![Screenshot](../../assets/images/allowing-multiple-registration-04.png)


Should you decide to change the setting during the course you need to
keep in mind that it is not enough to just increase the number of paid
terms on the course/group, but also to increase the price of the
course/group so that the price is correctly budgeted per unit.

## How does it work?

In order for the setup to work correctly, it needs to be done at all
levels. This means that if you want to have 10 billable events in the
course, you need to have 10 events marked as billable at the event level
 as well.

In case of adding terms to a group, if you have the number of
billable events set to 5 on the group/course level and you click on
repeat, the number in the *Repetition frequency* field will automatically be preset to 5 (as an indication that there are 5 billable events missing from the group).

![Screenshot](../../assets/images/how-to-create-paid-events-08.png)

![Screenshot](../../assets/images/allowing-multiple-registration-04.png)


After you set up billable events, you will see a checkbox at the
appointment level that allows you to set all newly created appointments
as billable or not billable. You can adjust the settings by clicking on
the “money pile” icon.

![Screenshot](../../assets/images/how-to-create-paid-events-10.png)

## Calculation of the unit price of the event

When a group has set up billable events, the unit price for the group
 is calculated using that setting instead of the total number of events
in the group. This only applies to continuous courses. One-off and Open
courses are already predefined by the unit price.

How to view and work with billable events read manual called [Viewing/Tracking billable events](viewing-billable-events.md)
