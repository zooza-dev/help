---
title: "Late bookings"
slug: "late-bookings"
type: "guides"
product_area: "Bookings"
sub_area: ""
audience: ["admin"]
tags: []
status: "published"
source_legacy_path: "legacy/0016_Welcome to Zooza.html"
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-15"
intercom_id: 13728572
intercom_sync: true
---

# Late bookings

## Late booking: automatic approval, full price for the whole programme

Klient


Admin

Klient

| Before booking |
|---|
| |
| During booking |
| Selects a programme/class from the menu and fills in the details |
| After booking creation |
| Receives a notification that the
booking has been completed and a request to confirm the
booking (from the system's side, this is a confirmation of entering
 the correct email address) |
| After booking confirmation |
| Notification is automatically sent
with all programme information with the option to log in to the profile -
email template: Booking confirmation |

Admin

| Before booking |
|---|
| Allow late registrationsSelect a courseClick on *Online registration*In the *Late bookings* section select *Automatically confirmed*Price calculation - Full programme price |
| |
| During booking |
| |
| After booking creation |
| |
| After booking confirmation |
| The booking is automatically flagged with the status - Late booking (snail icon)Price is set in full amount = price per programme/class or full installment amount |

## Late booking: manual approval, price aliquot

Klient


Admin

Klient

| Before booking |
|---|
| |
| During booking |
| Selects a programme/class from the menu and fills in the detailsAt the end of the form, the client
is notified by a message that he/she is registering for a class that has
 already started and that he/she will be informed of the class
assignment |
| After booking creation |
| Receives a notification that the
booking has been completed and a request to confirm the
booking (from the system's side, this is a confirmation of entering
 the correct email address) |
| After booking confirmation |
| A notification will be sent
notifying the client that the booking has been completed and that
the client will be contacted with more information once he/she has been
placed in a class |
| Manual booking approval |
| When the confirmation email is sent,
 a notification will arrive with all the programme information with the
option to log in to the profile and payment instructions - email
template: booking confirmationBoth status and payment details will be displayed in the client's profile |
| Manual disapproval/cancellation of booking |
| Information will only arrive in case
 of individual communication from the admin - application does not
automatically send anything |

Admin

| Before booking |
|---|
| Allow late registrationsSelect a courseClick on *Online registration*In the *Late bookings* section select *Automatically confirmed*Price calculation - Automatically calculated |
| |
| During booking |
| |
| After booking creation |
| |
| After booking confirmation |
| The booking is automatically flagged with the status - Late booking (snail icon) |
| Manual booking approval |
| View bookings in the class Select or search for Late bookings using the filterAfter clicking on booking, check the automatically calculated debt on the booking - overwrite in the details if necessaryPrice is calculated as an aliquot = For Programme Fees, the price per programme/class times the number of remaining eventsFor Membership, the price of the first installment is calculated by the number of days remaining in the current period plus one full future periodAfter clicking on booking, change the status to Registered - valid booking for the courseIf you would like to send a confirmation notification check the box Send confirmation email |
| |
| Manual disapproval/cancellation of booking |
| View bookings in the groupSelect or search for Late bookings using the filterOnce you click on a booking, change the status to Cancelled Booking (during the programme) You send cancellation information individually via send email/SMS to booking |

## Late booking: manual approval, full price for the whole programme

Klient


Admin

Klient

| Before booking |
|---|
| |
| During booking |
| Selects a programme/class from the menu to fill in the detailsAt the end of the form, the client is notified by a message that he/she is registering for a class that has already started and that he/she will be informed of the class assignment |
| After booking creation |
| Receives a notification that the
booking has been completed and a request to confirm the
booking (from the system's side, this is a confirmation of entering
 the correct email address) |
| After booking confirmation |
| A notification will be sent notifying the client that the booking has been completed and that the client will be contacted with more information once he/she has been placed in a class |
| Manual booking approval |
| When the confirmation email is sent, a notification will arrive with all the programme information with the option to log in to the profile and payment instructions - email template: booking confirmationBoth status and payment details will be displayed in the client's profile |
| Manual disapproval/cancellation of booking |
| Information will only arrive in case of individual communication from the admin - application does not automatically send anything |

Admin

| Before booking |
|---|
| Allow late bookings


Select a programme


Click on *Online registration*


In the *Late bookings* section select *Automatically confirmed*


Price calculation - Full programme price |
| |
| During booking |
| |
| After booking creation |
| |
| After booking confirmation |
| The booking is automatically flagged with the status - Late booking (snail icon) |
| Manual booking approval |
| View bookings in the class


 Select or search for Late bookings using the filter


After clicking on the booking, change the status to Registered - valid booking for the programme


If you would like to send a confirmation notification check the box *Send confirmation email*


 Price is set at the full amount - Amount = price per programme/class or full payment |
| |
| Manual disapproval/cancellation of booking |
| View bookings in the class


Select or search for Late bookings using the filter


Once you click on a booking, change the status to Cancelled Booking (during the programme)


 You send cancellation information individually via send email/SMS to booking |

## Payment schedule for late registrations

When a client registers after the programme has started and manual approval is enabled, the payment schedule (instalment plan) is **not** applied automatically — even if the client selected one during registration.

To apply a payment schedule to a late registration:

1. Open the booking detail and go to the **Payments** section.
2. In the **Instalment Plan** area (top-right), click **Create** and follow the wizard to select a payment template.
3. Change the booking status to **Registered** on the same day.

> **Important:** At midnight, the system runs an automatic validation of payment schedules. Only schedules linked to bookings with **Registered** status are confirmed. If the booking remains in **Late registration** status, any manually applied payment schedule is automatically removed. Always approve the booking and change its status to **Registered** before the end of the day.

## Understanding pro-rata (aliquot) pricing

When a client registers after a programme has already started, Zooza can automatically calculate a reduced price based on how many sessions remain. This is called **aliquot** (pro-rata) pricing.

### How the calculation works

The system uses a simple formula:

**Remaining sessions / Total sessions x Full price = Pro-rata price**

For example, if a programme has 20 sessions at a full price of 200 EUR and a client joins when 12 sessions remain, the calculated price is:

12 / 20 x 200 = **120 EUR**

The calculation method depends on the payment type:

- **Programme fee (term payment):** The price is calculated as the full programme price multiplied by the ratio of remaining sessions to total sessions.
- **Membership (recurring payments):** The first instalment is calculated based on the number of days remaining in the current billing period. Subsequent instalments are charged at the full amount.

<!-- REVIEW: Confirm whether the pro-rata price is displayed to the client on the booking form or only calculated after the booking is completed. Support conversations suggest it may only be visible to admins. -->

### Configuring aliquot pricing on a programme

1. Go to **Programmes** and select the programme.
2. Click **Edit Settings**.
3. Open the **Price and Payment** tile.
4. Expand **Advanced settings**.
5. In the `Aliquot price calculation` field, select **Automatically calculated**.
6. Save the settings.

When set to **Automatically calculated**, the system computes the pro-rata price for every late booking. The admin can still overwrite the calculated amount on individual bookings before approving them.

### Checking and overwriting the calculated price

1. Open the class and filter bookings by **Late booking** status.
2. Click on the booking.
3. Review the automatically calculated debt amount shown on the booking detail.
4. If the amount needs adjustment, edit the debt value directly in the booking detail.
5. Change the booking status to **Registered** to confirm.

## Fixed-price override (no pro-rata)

If you want all clients to pay the same amount regardless of when they join, use the **full programme price** option instead of aliquot pricing.

### Switching to fixed price

1. Go to **Programmes** and select the programme.
2. Click **Edit Settings**.
3. Open the **Price and Payment** tile.
4. Expand **Advanced settings**.
5. In the `Aliquot price calculation` field, select **Full programme price**.
6. Save the settings.

With this setting, every late booking is charged the full programme or class price. No automatic reduction is applied.

### Include Initial Full Scheduled Payment

When using **Membership** pricing with scheduled payments, the `Include Initial Full Scheduled Payment` checkbox controls whether the system generates an immediate full instalment at the time of booking, in addition to the regular payment schedule.

- **Checked (default):** The client is charged a full scheduled payment immediately upon booking, plus their regular recurring payments going forward. Use this when you want to collect the first period upfront.
- **Unchecked:** The client's first payment follows the normal payment template schedule. No additional upfront charge is generated. Use this for Netflix-style memberships where clients simply start paying on the next billing cycle.

To configure:

1. Go to **Programmes** → select the programme → **Edit Settings**.
2. Open the **Price and Payment** tile.
3. Expand **Advanced settings**.
4. Check or uncheck `Include Initial Full Scheduled Payment`.
5. Save the settings.

### When to use fixed price vs. pro-rata

| Scenario | Recommended setting |
|---|---|
| Clients join a few sessions late and expect a reduced fee | Automatically calculated (pro-rata) |
| Programme content is the same regardless of join date (e.g., membership, drop-in) | Full programme price |
| You want to manually set each late joiner's price | Automatically calculated, then overwrite per booking |

<!-- REVIEW: The system does not support automatic date-based switching between full price and pro-rata (e.g., "charge full price for the first 2 sessions, then switch to pro-rata"). Admins must change the setting manually when needed. Confirm this is still the case. -->

## FAQ: Common questions about late booking pricing

**Q: What does "aliquot" mean?**
A: Aliquot is a proportional calculation. In Zooza, it means the system divides the full price by the total number of sessions, then multiplies by the remaining sessions. The result is a fair, pro-rated price for clients who join after the programme starts.

**Q: Where do I configure aliquot pricing?**
A: Go to **Programmes** → select the programme → **Edit Settings** → **Price and Payment** → **Advanced settings** → `Aliquot price calculation`.

**Q: Can the system automatically switch from full price to pro-rata after a certain date?**
A: No. The system applies whichever setting is currently active. To switch, you must manually change the `Aliquot price calculation` setting on the programme at the time you want the change to take effect.

**Q: Is the pro-rata price visible to clients during booking?**
A: The calculated price may not always be shown on the booking form. Clients typically see the price after the booking is completed or when payment instructions are sent. Check your programme's late booking flow (automatic vs. manual approval) to understand when the price is communicated.

<!-- REVIEW: Verify whether the pro-rata price is displayed during the booking form step for automatically approved late bookings. -->

**Q: What happens if I change the aliquot setting mid-term?**
A: The change applies only to new late bookings created after the setting is changed. Existing bookings keep their original calculated price.

## Related

- [Programme Settings Reference](../reference/programme-settings.md) -- Price and Payment tile, Advanced settings.
- [Programme Automations](../reference/programme-automations.md) -- Late Booking Automations flow.
- [Payment Options](payment-options.md) -- configuring payment methods and templates.
- [Payments and Billing FAQ](../faq/payments-and-billing-faq.md) -- common payment questions including pro-rata pricing.
