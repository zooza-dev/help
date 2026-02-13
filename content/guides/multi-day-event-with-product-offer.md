---
title: "Multi-day event with product offer"
slug: "multi-day-event-with-product-offer"
type: "guides"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: []
status: "published"
source_legacy_path: "legacy/0019_Welcome to Zooza.html"
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-11"
intercom_id: 13728577
intercom_sync: false
---

# Multi-day event with product offer

![Screenshot](../../assets/images/blocks-creation-07.png)


Programme - for a period with two classes, where several people can sign up on one form

![Screenshot](../../assets/images/individual-lessons-climbing-wall-02.png)

Example: A multi-day event/camp where the whole family can sign up. There are 2 turnuses available. Possibility of booking, transport, meal, accommodation for individual days with specific criteria (e.g.: allergies, one-way transport only, vegetarian diet,...).

Client

Admin

Instructor

Client

| Before booking |
|---|
| |
| During booking |
| Selects a programme/class from the menu, fills in the details and submits the form |
| After booking creation |
| Receives a notification that the
booking has been completed and a request to confirm the
booking (from the system's side, this is a confirmation of entering
 the correct email address) |
| After registartion confirmation |
| Notification is automatically sent with all the information about the programme with the option to log in to the profile - email template: Booking confirmation along with a summary of the ordered items and the resulting price |
| On the session/session |
| |

Admin

| Before booking |
|---|
| Creates a programme of type Ongoing - [MANUAL](https://support.zooza.online/portal/en/kb/articles/course-creation)Creates 2 classes - for each tour with dates, with a date equal to one day of the eventIn the *Online registration - Booking Options *section, set the permission for multiple bookings for the programme, where set the max. number of bookings per form filling - 6 and decide on the payment management on the registrant - [MANUAL](allowing-multiple-registration.md)In the *Online registration - Late bookings *set the option OffIn the *Online registration - Communication *uncheck to send automatic session remindersIn the programme details under *Extra Fields*, expand the registration form to include extra fields:: Date of birthChild's full nameAddressBusiness nameTax IDVATIdentification (birth) numberExtra field 1 - dancer's/other parent's emailExtra field 2 - email of dancer/other parentExtra field 3 - How did you hear about us?Set class capacityIn the *Price and Payment *section, leave the price at 0 and set the payment options to Cash/Transfer to accountCreate a new Custom template for the confirmation email -Booking Confirmation (Term programme)Add communication template at programme level - [MANUAL](message-templates.md)In *Online Registration - Communication* - set the signatureCreate new services in the *Services *section with options and prices, where each question (accommodation, meals, insurance) equals one service and each service item equals one answer to a question that has a price assigned to itCreate a product in the *Products *section, without a price, in which add all services as items for saleAdd the product to the class level and set the option - *Make available* in the registration form |
| |
| During booking |
| |
| After booking creation |
| |
| After booking confirmation |
| Booking is automatically flagged with the status - Valid programme registrationIf the booking is above the class capacity it is automatically tagged with the status - On the waiting list (hourglass icon) and requires individual administrationThe booking debt is calculated based on the service items orderedOn the booking detail, a summary of all ordered service items for all participants who have been completed in one form is displayedAn order is created under a separate number in the* Orders *section that contains all ordered service items and is linked to the registrationThe price for the order is managed on the booking and thus for proper automatic payment pairing it should also be paid with the booking's variable symbol (due to the Manage Payments setting on the registrant) |
| |
| On the session/session |
| |

Instructor

| Before booking |
|---|
| |
| |
| During booking |
| |
| After booking creation |
| |
| After booking confirmation |
| |
| |
| On the session/session |
| Takes attendance on the session - [MANUAL](https://support.zooza.online/portal/en/kb/articles/attendance-setup) |
