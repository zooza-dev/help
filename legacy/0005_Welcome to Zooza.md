# Welcome to Zooza

**URL:** https://support.zooza.online/portal/en/kb/articles/dynamic-tags

---

Dynamic tags

When creating templates, we’ve created a feature that will speed up 
communication with your customers. In order to make the automatic 
communication effective and at the same time still relevant, i.e. with 
specific information about the course, the time and the location of the 
group your client has subscribed to, we use so-called dynamic tags. 
These help to pull the right information into the email.

You can also use them and if you want to add some information to one 
of the templates, you can select a dynamic tag via the Tags icon in the 
text formatting panel. When you click on the icon, you will see a full 
list of dynamic tags with their explanation for better navigation and to
 minimize any mistakes.

Attention!

 Some dynamic tags can only be applied to certain 
templates, so care must be taken when selecting the template and the 
tags themselves.

For registrations

Each email that is sent for a specific registration allows you to 
dynamically fill in customer data through dynamic tags. At the time the 
email is sent, zooza replaces these tags with specific values.

Dynamic tag

Definition

Example

*|COURSE_PRICE|*

Course price The current price for the course is always used. If the
 group has its own price, the price for the group shall be used

20,00 €

*|REGISTRATION_VALUE|*

The value of the registration at the time of its creation. If the 
amount due on a registration changes, for example due to discounts or a 
payment plan, this amount indicates the original full amount – the value
 of the registration derived from its group.

20,00 €

*|AFFILIATE_ID|*

ID of the partner who facilitated the registration

12345

*|REGISTRATION_ID|*

Registration number

12345

*|REGISTRATION_STATUS|*

Registration status

registered

*|REGISTRATION_FEE|*

Registration fee. If it is not listed on the registration, it is made up from the course.

30 €

*|VARIABLE_SYMBOL|*

Variable symbol used for payment. As a rule, this is the registration number.

12345

*|COMPANY|*

Your company name

My company Ltd.

*|COURSE_PLACE|*

The place where the course takes place. The name is composed of room and location data

Big hall, Free time center, 323 Green Lane, Edinburgh

*|COURSE_PLACE_ID|*

Location ID

123

*|COURSE_ROOM_ID|*

Room ID

456

*|COURSE_PID|*

Unique combination of location and room

123_456

*|COURSE_NAME|*

Course name – group name

Exercising with babies – MINI1

*|COURSE_DATE_DAY|*

Day of the course

Monday

*|COURSE_SUMMARY|*

Start time of the course together with the date

13. 5. 13.9.2023 at 15:00

*|COURSE_TIME|*

Course start time

14:00

*|COURSE_PAYMENT|*

Course price derived from registration. If there is no amount on the registration, the price on the course is made up.

135 €

*|CURRENT_BALANCE|*

The current balance on the client’s account – his registration. The balance can be both plus and minus.

-30 €

*|SCHEDULE_DURATION|*

Course duration in hours

15:00

*|SCHEDULE_NAME|*

Group name (without course name)

Butterflies, tuesdays at 17:00

*|SCHEDULED_AT_DATE|*

Communicates the date when the installment (debt) is due on the registration.

10

*|FIRST_NAME|*

Client name

John

*|QR_CODE|*

Applies only under the following conditions: amount due entered on 
registration, IBAN and SWIFT code entered on the course/company.

Picture with QR code

*|IBAN|*

The bank account to which the customer should make the payment. If specified at the course level, this value is used

GB54BARC20039545449825

*|COURSE_DATE_START_END|*

Start and end date of the course

14. 5. 2022 – 14. 8. 2022

*|COURSE_TRAINER|*

Lecturer’s name

John Winslow

*|USER_ID|*

Customer User ID

12345

*|WIDGET_VIDEO_URL|*

Url address to view the video

https://www.zooza.sk/video?token=12345

*|WIDGET_PROFILE_URL|*

Url address to view profile

https://www.zooza.sk/profil?token=12345

*|EF_DOB|*

Extra field – date of birth

13. 4. 2000

*|EF_FULL_NAME|*

Extra field – full name

John Winslow

*|EF_ADDRESS|*

Extra field – Address

65 Wood Lane, Bristol

*|EF_BUSINESS_NAME|*

Extra field – Company name

Zooza

*|EF_BUSINESS_ADDRESS|*

Extra field – Company address

65 Wood Lane, Bristol

*|EF_BUSINESS_ID|*

Extra field – ID number

123456

*|EF_TAX_ID|*

Extra field – TIN

1234546

*|EF_VAT|*

Extra field – VAT ID number

123456

*|IS_BUSINESS_ORDER|*

The tag that determines whether a registration is on company or not

1

*|TURN_OFF_EVENT_NOTIFICATIONS_URL|*

Url address to turn off morning notifications. This tag only works in the Morning Reminders template

 

*|CANCELED_CONFIRMATION_URL|*

Url address for opting-out from the term. This tag only works in the Morning Reminders template

 

*|ALLOW_REPLACEMENTS|*

Indicates whether replacement hours are available for registration

1

*|FULL_NAME|*

Client’s full name

Raymond Robbins

*|EVENT_NAME|*

Name of the term (does not include the name of the course or the 
name of the group). The tag is only available for term reminder and 
reminder of upcoming terms.

Individual lesson, Cambridge

*|EVENT_DATE|*

Date of the term (only available for reminder of the terms)

14. 5. 2021

*|EVENT_PLACE|*

Venue of the term

This tag only works in the Morning Reminders template

Big hall, Free time center, 323 Green Lane, Edinburgh

*|EVENT_DATE_DAY|*

Day of the term (available for term reminder only)

Monday

*|EVENT_TIME|*

Term time (available for term reminder only)

14:30

*|EVENT_COURSE|*

The name of the course in which the term is located. The tag is only available for term reminder and reminder of upcoming terms.

Summer camp 07/2023

*|EVENT_TRAINER|*

It contains the name of the lecturer (main), which is specified at 
the lesson/event level. Available for the upcoming lesson/event 
notification email template.

Suzan Winslow

*|DEFAULT_COURSE_PRICE|*

The value of the Course price if the group price is equal to 0, if not, the Group price is displayed

34,43 €

*|DEBT|*

Debt registration value. But if there is no debt on the registration, it will display the same as the DEFAULT_COURSE_PRICE tag

100 €

*|DUE_DATE|*

Communicates the due date for payment

33 €

Conditioning tags

You can also use conditional tags in your templates. For example, if 
you accept business orders, you can add a conditional block to your 
template to confirm to the customer that you are recording their 
registration as a business and will send them an invoice shortly.

Tag name

Definition

Application

IF

If the condition is true

*|IF:BUSINESS_ORDER|*

Content

*|END:IF|*

ELSE

so then.

*|IF:BUSINESS_ORDER|*

content if yes

*|ELSE:|*

content if not

*|END:IF|*

ELSEIF

Or if

*|IF:BUSINESS_ORDER|*

content if yes

*|ELSEIF:REGISTRATION_STATUS=registered|*

content if registration status

*|ELSE:|*

content if not

*|END:IF|*

IFNOT

if it is not

*|IFNOT:BUSINESS_ORDER|*

Content

*|END:IF|*

Conditioning tags

Tag

Definition

=

Equals

!=

It does not equal

>

Larger

<

Smaller

>=

Larger or equal

<=

Smaller or equal

Operators

Updated:

 

1 year ago

Helpful?

Previous

Next

 

 

On this page

For registrations

Conditioning tags

Follow

Subscribe to receive notifications from this article.

Automatic notifications

WhatsApp Integration & Usage (Beta)

Automatic reminders for payment schedule

Edit automatic notifications of an upcoming event

Dynamic tags

Automatic notification of an upcoming event

Related 

Articles

Automatic communication to clients / Message templates

Sending email/SMS to clients

Edit automatic notifications of an upcoming event

WhatsApp Integration & Usage (Beta)

Automatic notification of an upcoming event