---
title: "Payment templates creation"
slug: "payment-templates-creation"
type: "guides"
product_area: "Payments"
sub_area: ""
audience: ["admin"]
tags: []
status: "published"
source_legacy_path: "legacy/0086_Welcome to Zooza.html"
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-11"
---

# Payment templates creation

![Screenshot](../../assets/images/allowing-multiple-registration-03.png)

Within the payment templates, you have several options on how to use them for your courses and clients. Please refer to [the instructions for](http://zooza.online/sk/support/druhy-platieb-za-kurz/) more information.

## Usage


For a practical application of the different payment types, here are some examples.

## Language courses


I am an organizer of language courses that last the whole school year, i.e. from September to June of the following year. I want to allow clients to pay for the course monthly, semi-annually, or in one lump sum for the entire year, as it suits them according to their means. I want to provide an incentive discount for paying in advance for the entire course. For such a course I will set up the following templates:

1. Periodic payment in advance with no discount – monthly. It will be used for regular monthly payments for the course, which will go out to the client on the day of the month that you can choose.
2. Periodic payment in advance with a smaller discount – semi-annually. It will be used to pay for the course in two installments. If the client chooses this payment, he will have a discount of, for example, 5% on the course, which will be automatically calculated from the price of the course.
3. One-time payment in advance with a larger discount. It will be used to pay for the course for its entire duration, i.e. the whole year. If the client chooses this payment, he will have a discount of, for example, 10% on the course, which will be automatically calculated from the price of the course.

## Children courses


I am an organizer of exercises for children, which have a duration of one semester. I want to allow parents to pay for the course in 3 instalments or in one lump sum for the whole duration of the course, as it suits whom. I want to provide an incentive discount for paying in advance for the entire course. I also want them to have the option of a discount if they have and register more children. For such a course I will set up the following templates:

1. One-time payment with discount. It will be used to pay for the entire duration of the course if the parent registers only one child. I will set a smaller incentive discount, for example 3%.
2. One-time payment Siblings with a discount of, for example, 20%. It will be used to pay for the entire duration of the course, in case a parent registers more than one child. The discount is automatically calculated from the price for 2x course price You need to set up the option to add a person at the course level – online registration.
3. Periodic payment for a fixed number of installments without discount. It will be used for payment divided into 3 equal parts, in case the parent registers only one child. Here I have no reason to give a discount.
4. Periodic payment for a fixed number of installments, Siblings with a discount of, for example, 10%. It will be used for payment divided into 3 equal parts, in case a parent registers more than one of his/her children. The discount is automatically calculated from the price for 2x course price and divided into 3 parts. You need to set up the option to add a person at the course level – online registration.

## Set up payment templates

In order to set up payments on a course, you need to create payment templates first. To set them up, proceed as follows:

- Click on the Settings tab in the left menu and then click on the Payments

![Screenshot](../../assets/images/payment-templates-creation-02.jpg)
- To add a new payment template, click the Add button at the top of the screen and fill in the required parameters for the template

![Screenshot](../../assets/images/payment-templates-creation-03.png)
- Select one of the options as required:
- One-time payment – you have the option to set up a one-time payment for the course.For example, if a client chooses a course that lasts half a year, but
does not want to pay monthly, they choose to pay for the entire course
at once.For such a payment you can give a discount either none, in EUR or as a percentage.

![Screenshot](../../assets/images/payment-templates-creation-04.png)
- Periodic pre-paid payment – you have the option to set whether the course can be paid gradually, i.e. in frequency.Here you select from the options – Monthly, Quarterly, Semi-annually,
Annually, After N terms (the number of terms after which the next
installment for the course will be issued), Fixed number of installments
 (the number of installments into which the price for the course will be
 divided).The course provider has the option to grant a discount for this type of payment either none, in EUR or as a percentage.

![Screenshot](../../assets/images/payment-templates-creation-05.png)

- Periodic payment paid in arrears according to attendance
- This option allows you to charge clients based on their actual attendance. The system creates and sends instalments only after the client has attended the required number of sessions, depending on the frequency you set.There are two possible modes:

1) Periodic frequency (e.g., monthly)

When using a time-based frequency:

1. When attendance is recorded, the system creates an instalment scheduled for the next anniversary date of the frequency (e.g., next month).
2. Each time attendance is marked as *“attended”*, the amount on that instalment increases.
3. When the instalment’s scheduled date arrives, it is processed during the nightly job and the client receives the payment request. At this moment, the registration receives the corresponding outstanding balance.
4. If the client does not attend any session within the chosen frequency period (e.g., no attendance in a whole month), no instalment is generated.

2) After N sessions (e.g., payment after every 2 sessions)
A When using a frequency based on a number of attended sessions:

1. When attendance is recorded, the system creates an instalment scheduled one year ahead.*(This is only a placeholder date — it will be adjusted once the required number of attendances is reached.)*

1. Each time an attendance is marked as *“attended”*, the amount on that instalment increases.

1. When the required number of attended sessions (N) is reached, the instalment is rescheduled to “today” and will be processed during the nightly job. At this moment, the registration receives the outstanding balance.

1. If the required number of attendances is reached multiple times on the same day(example: frequency = every 2 sessions, and 4 sessions are recorded in one day),then multiple instalments will be created on that same day.

![Screenshot](../../assets/images/payment-templates-creation-06.png)

Save the template by clicking the *Save button.*

![Screenshot](../../assets/images/allowing-multiple-registration-03.png)

Note: If you use discounted payment templates, you can find a clear list of them in the Payments - Discounts section.

![Screenshot](../../assets/images/payment-templates-creation-08.png)

## Other template settings, template activation in courses


In the payment settings, you can edit individual templates, set their
visibility to customers/tutors or delete a template. You can also
quickly and easily activate the template on the courses of your choice.
To change and modify the template or activate it on the course, please follow these steps:


- V zozname platobných šablón kliknite na ikonu pera vedľa šablóny, ktorú chcete upravovať

![Screenshot](../../assets/images/payment-templates-creation-09.png)

- In template editing you have the option to set the visibility of the template, i.e. what group of people will be able to use this template – Customers, Lecturers or both.1. Customers – you choose the option to have the template visible to customers directly when they register on your site. 2. Lecturers – visibility for lecturers means that the lecturer will also be able to assign registrations to a given template

![Screenshot](../../assets/images/payment-templates-creation-10.png)

- Below in the courses section you have a list of your courses and for each of them you can activate or deactivate the template

![Screenshot](../../assets/images/payment-templates-creation-11.png)

- When you make changes to the template, we recommend that you *Sync Settings.* This will ensure that any changes made to the template will also be
reflected in courses and groups where it has already been activated.

![Screenshot](../../assets/images/discount-code-01.png)

Note: If you have changed template settings, these
will not automatically be transferred to the courses where the template
is applied. If you want all courses to have their installment calendars
set according to this version of the template, synchronize their
settings. The system also keeps alerting you

![Screenshot](../../assets/images/payment-templates-creation-13.png)

- Then *Save* the changes. Alternatively, you also have the option of using the *Delete* template

These payment templates created can then be used and inserted into your new or existing courses/groups.

## Insert payment templates into a course/group

The created payment templates need to be inserted into newly created or
already existing courses. The templates created in this way can be
combined in the courses according to your wishes and needs. This means
that you can use multiple payment templates for one course.

## Insert templates into courses


To insert templates into courses, do the following:


- In the list of courses, click on the name of the course in which you want to add a template or check the activation of the selected templates
- In the *Price *and *Payment *section, click the *Edit *button

![Screenshot](../../assets/images/payment-templates-creation-14.png)
- Below in the *Payment Frequency* section you can see which payment templates you have *Active* and which *Inactive*. *Active* payment templates are the ones highlighted in colour (yellow background under the text, blue knob)

![Screenshot](../../assets/images/payment-templates-creation-15.png)

1. If you wish to activate the template, click on the white *Active* button
2. If you wish to deactivate the template, click on the white *Inactive* button

## Within creating a new group

This selection of templates will appear in the menu when you create a
 group for the course, where you again have the option to decide whether
 or not to enable this payment option. To activate the template on the
group, click on the white *Active* button.

![Screenshot](../../assets/images/payment-templates-creation-16.png)

Then save your selection by clicking *Create*.

## When inserting into an existing group. Edit payment templates in existing groups

1. Select a group. In the *Payment Frequency* section, click the *Add Template* button. You will only see the ones that are activated on the course.
 ![Screenshot](../../assets/images/payment-templates-creation-17.png)

1. When you click on the *pen icon*, you will be presented with the option to activate/deactivate the template. Then click on the pipe icon and the *Save *button at the end of the screen to confirm the changes you have made.
 ![Screenshot](../../assets/images/payment-templates-creation-18.png)

1. To delete a template from the group, click on the trash icon.

1. You can use the arrow keys to change the order of the templates and
set them as you want them to appear in the registration form.
 ![Screenshot](../../assets/images/payment-templates-creation-19.png)

1. This selection of payment options will then be displayed in the registration form on your website as follows:
 ![Screenshot](../../assets/images/payment-templates-creation-20.png)

The client has to choose one of the offered options and the final price
for the course is recalculated according to the client’s choice, if it
is affected by this choice (if a discount has been set in the template).

![Screenshot](../../assets/images/discount-code-01.png)

Note: If a client registers for a course that has already started and you have set up manual approval for late registrations in the course settings, the payment type will not appear on their
registration. Such registrations are marked as late by the application
and require manual editing. 

1. Adjust the amount owed as needed or add a compliant payment template to your registration
2. Manually change the registration status to Registered

## Payment templates on registration

- Select the registration you want to edit.
- Under *Payments*, click *View Payments*

![Screenshot](../../assets/images/payment-templates-creation-22.jpg)

- In the *Installment Plan *section, click *Create *(if no installment plan has been set up on the registration) or *Change *(if an installment plan has already been set up on the registration).

![Screenshot](../../assets/images/payment-templates-creation-23.png)

- This will open the settings for creating a payment plan. Select the
options that suit you and click continue. If you enter a value in the
Registration Fee field, it will be applied as part of the first
instalment – so the first instalment will be increased by the value of
the registration fee.

![Screenshot](../../assets/images/payment-templates-creation-24.png)

- Click the *Select* button next to the template you want to
apply. Zooza will show you what the repayment amount is, how many
repayments will be incurred, what the discount is and what the final
amount paid by the customer is after all repayments have been made. Then
 click *Continue*

![Screenshot](../../assets/images/payment-templates-creation-25.png)

- In the next step, check your settings and click *Continue*

![Screenshot](../../assets/images/payment-templates-creation-26.png)

- To apply the payment plan to a given registration, confirm your selection by clicking on the *Finish* button.

![Screenshot](../../assets/images/payment-templates-creation-27.png)

![Screenshot](../../assets/images/allowing-multiple-registration-03.png)

The payment schedule entered in this way will be automatically reflected in the client's profile and invoices for payments will be issued and notifications for payments will also be sent to the client based on this schedule.

### How to delete payment template on registration?

1. You can delete the set instalment plan on the regisdtration by clicking on the *Partial payments overview* button.
 ![Screenshot](../../assets/images/payment-templates-creation-29.png)

1. Then click the *Delete* button. The registration reverts to a no-payment status.

![Screenshot](../../assets/images/payment-templates-creation-30.png)

## Payment Plan Preview


If you have multiple registrations with active payment templates, use the *Payments - Installments Overview* section for a better overview of the next installments issued.

![Screenshot](../../assets/images/allowing-multiple-registration-03.png)

This way you can quickly and easily track all active payments from the date you have selected.


For a quick search, you can use the filter that allows you to enter:


1. Client - to search for a specific client,
2. Status - you select whether the installments are scheduled or processed,
3. Scheduled Date - search for installments by date.


This way you can quickly and easily keep track of all active payments.

![Screenshot](../../assets/images/payment-templates-creation-32.png)

## Apply a payment template to the whole class

For each class/group, you can apply the payment template in one go:

1. Open the Class
 ![Screenshot](../../assets/images/payment-templates-creation-33.png)

2. Go to Price & Payments
3. Click Apply payment template
4. Set the amount (based on that class pricing)
5. Choose the start date (example: 1 January 2026)
 ![Screenshot](../../assets/images/payment-templates-creation-34.png)
6. Select which bookings/registrations it applies to (usually All)
 ![Screenshot](../../assets/images/payment-templates-creation-35.png)
7. Confirm and continue
