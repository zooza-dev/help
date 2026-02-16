---
title: "Dynamic tags"
slug: "dynamic-tags"
type: "guides"
product_area: "Communication"
sub_area: "Email"
audience: ["admin"]
tags: ["email"]
status: "published"
source_legacy_path: "legacy/0005_Welcome to Zooza.html"
source_language: "en"
needs_screenshot_replacement: true
last_converted: "2026-02-13"
intercom_id: 13728547
intercom_sync: true
---

# Dynamic tags

When creating templates, Zooza provides dynamic tags to speed up communication with your clients. These tags pull specific information -- such as programme name, time, and location -- into emails automatically, keeping communication relevant without manual effort.

You can add dynamic tags via the **Tags** icon in the text formatting panel. Clicking the icon shows a full list of dynamic tags with explanations.

> **Attention!** Some dynamic tags can only be applied to certain templates. Take care when selecting the template and the tags.

![Dynamic tags panel](../../assets/images/dynamic-tags-panel.png "Dynamic tags panel in template editor")

## For bookings

Each email sent for a specific booking allows you to dynamically fill in client data. At the time the email is sent, Zooza replaces these tags with specific values.

| Dynamic tag                                                 | Definition                                                                                 | Example                                               |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------- |
| <code>&#42;&#124;COURSE_PRICE&#124;&#42;</code>                     | Current programme price. If the class has its own price, the class price is used.          | 20.00 EUR                                             |
| <code>&#42;&#124;REGISTRATION_VALUE&#124;&#42;</code>               | Value of the booking at the time of creation. Shows the original full amount.              | 20.00 EUR                                             |
| <code>&#42;&#124;AFFILIATE_ID&#124;&#42;</code>                     | ID of the partner who facilitated the booking                                              | 12345                                                 |
| <code>&#42;&#124;REGISTRATION_ID&#124;&#42;</code>                  | Booking number                                                                             | 12345                                                 |
| <code>&#42;&#124;REGISTRATION_STATUS&#124;&#42;</code>              | Booking status                                                                             | registered                                            |
| <code>&#42;&#124;REGISTRATION_FEE&#124;&#42;</code>                 | Registration fee. If not listed on the booking, it is taken from the programme.            | 30 EUR                                                |
| <code>&#42;&#124;VARIABLE_SYMBOL&#124;&#42;</code>                  | Variable symbol used for payment. Typically the booking number.                            | 12345                                                 |
| <code>&#42;&#124;COMPANY&#124;&#42;</code>                          | Your company name                                                                          | My company Ltd.                                       |
| <code>&#42;&#124;COURSE_PLACE&#124;&#42;</code>                     | Programme location. Composed of room and location data.                                    | Big hall, Free time center, 323 Green Lane, Edinburgh |
| <code>&#42;&#124;COURSE_PLACE_ID&#124;&#42;</code>                  | Location ID                                                                                | 123                                                   |
| <code>&#42;&#124;COURSE_ROOM_ID&#124;&#42;</code>                   | Room ID                                                                                    | 456                                                   |
| <code>&#42;&#124;COURSE_PID&#124;&#42;</code>                       | Unique combination of location and room                                                    | 123_456                                               |
| <code>&#42;&#124;COURSE_NAME&#124;&#42;</code>                      | Programme name -- class name                                                               | Exercising with babies -- MINI1                       |
| <code>&#42;&#124;COURSE_DATE_DAY&#124;&#42;</code>                  | Day of the programme                                                                       | Monday                                                |
| <code>&#42;&#124;COURSE_SUMMARY&#124;&#42;</code>                   | Start time of the programme together with the date                                         | 13. 5. -- 13.9.2023 at 15:00                          |
| <code>&#42;&#124;COURSE_TIME&#124;&#42;</code>                      | Programme start time                                                                       | 14:00                                                 |
| <code>&#42;&#124;COURSE_PAYMENT&#124;&#42;</code>                   | Programme price derived from booking. If none on booking, the programme price is used.     | 135 EUR                                               |
| <code>&#42;&#124;CURRENT_BALANCE&#124;&#42;</code>                  | Current balance on the client's booking. Can be positive or negative.                      | -30 EUR                                               |
| <code>&#42;&#124;SCHEDULE_DURATION&#124;&#42;</code>                | Programme duration in hours                                                                | 15:00                                                 |
| <code>&#42;&#124;SCHEDULE_NAME&#124;&#42;</code>                    | Class name (without programme name)                                                        | Butterflies, tuesdays at 17:00                        |
| <code>&#42;&#124;SCHEDULED_AT_DATE&#124;&#42;</code>                | Date when the instalment (debt) is due on the booking                                      | 10                                                    |
| <code>&#42;&#124;FIRST_NAME&#124;&#42;</code>                       | Client name                                                                                | John                                                  |
| <code>&#42;&#124;QR_CODE&#124;&#42;</code>                          | QR code for payment. Requires: amount due on booking, IBAN and SWIFT on programme/company. | Picture with QR code                                  |
| <code>&#42;&#124;IBAN&#124;&#42;</code>                             | Bank account for payment. If specified at the programme level, that value is used.         | GB54BARC20039545449825                                |
| <code>&#42;&#124;COURSE_DATE_START_END&#124;&#42;</code>            | Start and end date of the programme                                                        | 14. 5. 2022 -- 14. 8. 2022                            |
| <code>&#42;&#124;COURSE_TRAINER&#124;&#42;</code>                   | Instructor's name                                                                          | John Winslow                                          |
| <code>&#42;&#124;USER_ID&#124;&#42;</code>                          | Client user ID                                                                             | 12345                                                 |
| <code>&#42;&#124;WIDGET_VIDEO_URL&#124;&#42;</code>                 | URL to view the video                                                                      | `https://www.zooza.sk/video?token=12345`              |
| <code>&#42;&#124;WIDGET_PROFILE_URL&#124;&#42;</code>               | URL to view profile                                                                        | `https://www.zooza.sk/profil?token=12345`             |
| <code>&#42;&#124;EF_DOB&#124;&#42;</code>                           | Extra field -- date of birth                                                               | 13. 4. 2000                                           |
| <code>&#42;&#124;EF_FULL_NAME&#124;&#42;</code>                     | Extra field -- full name                                                                   | John Winslow                                          |
| <code>&#42;&#124;EF_ADDRESS&#124;&#42;</code>                       | Extra field -- address                                                                     | 65 Wood Lane, Bristol                                 |
| <code>&#42;&#124;EF_BUSINESS_NAME&#124;&#42;</code>                 | Extra field -- company name                                                                | Zooza                                                 |
| <code>&#42;&#124;EF_BUSINESS_ADDRESS&#124;&#42;</code>              | Extra field -- company address                                                             | 65 Wood Lane, Bristol                                 |
| <code>&#42;&#124;EF_BUSINESS_ID&#124;&#42;</code>                   | Extra field -- ID number                                                                   | 123456                                                |
| <code>&#42;&#124;EF_TAX_ID&#124;&#42;</code>                        | Extra field -- TIN                                                                         | 1234546                                               |
| <code>&#42;&#124;EF_VAT&#124;&#42;</code>                           | Extra field -- VAT ID number                                                               | 123456                                                |
| <code>&#42;&#124;IS_BUSINESS_ORDER&#124;&#42;</code>                | Whether a booking is on a company or not                                                   | 1                                                     |
| <code>&#42;&#124;TURN_OFF_EVENT_NOTIFICATIONS_URL&#124;&#42;</code> | URL to turn off morning notifications. Works only in the Morning Reminders template.       |                                                       |
| <code>&#42;&#124;CANCELED_CONFIRMATION_URL&#124;&#42;</code>        | URL for opting out from the term. Works only in the Morning Reminders template.            |                                                       |
| <code>&#42;&#124;ALLOW_REPLACEMENTS&#124;&#42;</code>               | Whether make-up sessions are available for the booking                                     | 1                                                     |
| <code>&#42;&#124;FULL_NAME&#124;&#42;</code>                        | Client's full name                                                                         | Raymond Robbins                                       |
| <code>&#42;&#124;EVENT_NAME&#124;&#42;</code>                       | Name of the term (not the programme or class). Available for term reminder only.           | Individual session, Cambridge                         |
| <code>&#42;&#124;EVENT_DATE&#124;&#42;</code>                       | Date of the term. Available for term reminder only.                                        | 14. 5. 2021                                           |
| <code>&#42;&#124;EVENT_PLACE&#124;&#42;</code>                      | Venue of the term. Works only in the Morning Reminders template.                           | Big hall, Free time center, 323 Green Lane, Edinburgh |
| <code>&#42;&#124;EVENT_DATE_DAY&#124;&#42;</code>                   | Day of the term. Available for term reminder only.                                         | Monday                                                |
| <code>&#42;&#124;EVENT_TIME&#124;&#42;</code>                       | Term time. Available for term reminder only.                                               | 14:30                                                 |
| <code>&#42;&#124;EVENT_COURSE&#124;&#42;</code>                     | Programme name for the term. Available for term reminder only.                             | Summer camp 07/2023                                   |
| <code>&#42;&#124;EVENT_TRAINER&#124;&#42;</code>                    | Main instructor name at the session level. Available for upcoming session notification.    | Suzan Winslow                                         |
| <code>&#42;&#124;DEFAULT_COURSE_PRICE&#124;&#42;</code>             | Programme price if class price is 0; otherwise the class price.                            | 34.43 EUR                                             |
| <code>&#42;&#124;DEBT&#124;&#42;</code>                             | Debt value on booking. If no debt, displays the same as `DEFAULT_COURSE_PRICE`.            | 100 EUR                                               |
| <code>&#42;&#124;DUE_DATE&#124;&#42;</code>                         | Due date for payment                                                                       | 33 EUR                                                |

## Conditioning tags

You can use conditional tags in templates. For example, if you accept business orders, you can add a conditional block to confirm to the client that you are recording their booking as a business and will send them an invoice shortly.

| Tag name | Definition | Application |
|---|---|---|
| `IF` | If the condition is true | <code>&#42;&#124;IF:BUSINESS_ORDER&#124;&#42;</code> Content <code>&#42;&#124;END:IF&#124;&#42;</code> |
| `ELSE` | Otherwise | <code>&#42;&#124;IF:BUSINESS_ORDER&#124;&#42;</code> content if yes <code>&#42;&#124;ELSE:&#124;&#42;</code> content if not <code>&#42;&#124;END:IF&#124;&#42;</code> |
| `ELSEIF` | Or if | <code>&#42;&#124;IF:BUSINESS_ORDER&#124;&#42;</code> content if yes <code>&#42;&#124;ELSEIF:REGISTRATION_STATUS=registered&#124;&#42;</code> content if status <code>&#42;&#124;ELSE:&#124;&#42;</code> content if not <code>&#42;&#124;END:IF&#124;&#42;</code> |
| `IFNOT` | If it is not | <code>&#42;&#124;IFNOT:BUSINESS_ORDER&#124;&#42;</code> Content <code>&#42;&#124;END:IF&#124;&#42;</code> |

### Comparison operators

| Tag | Definition |
|---|---|
| `=` | Equals |
| `!=` | Does not equal |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |

## Known limitations and troubleshooting

### Tags in make-up sessions

When a client books a make-up session, tags like `COURSE_TIME`, `COURSE_DATE_DAY`, and `COURSE_PLACE` pull data from the **primary class's first session**, not the make-up session. This means the email may show incorrect time, day, or location for the make-up.

**Workaround:** Use `ORDER_SUMMARY` instead — it includes the correct session details for the specific booking context.

### Tags in block-based programmes

For programmes using blocks (term segments), `COURSE_DATE_DAY` and `COURSE_TIME` pull from the first session in the class, which may not match the client's enrolled block.

**Workaround:** Use `ORDER_SUMMARY` to display the correct block-specific information. A dedicated block-specific date tag is not yet available.

<!-- REVIEW: Monitor for a dedicated block-specific dynamic tag — it has been requested by multiple customers. -->

### Tags in order confirmation emails

Dynamic tags are **not fully supported** in order (product purchase) confirmation emails. Tags like `COURSE_NAME`, `COURSE_TIME`, etc. will not populate because orders are not linked to a specific class or session.

Only basic client tags (`FIRST_NAME`, `FULL_NAME`, etc.) work in order emails.

### Tags in subject lines

Most dynamic tags work in email subject lines, but some may not populate in certain template types. Always test your email before sending to a large class.

### Tag rendering outages

In rare cases, the dynamic tag rendering service may experience temporary outages, causing tags to appear as blank in sent emails. If you notice blank tags in recently sent emails:

1. Check **Communication → Sent emails** to verify which emails were affected.
2. Contact support to confirm whether a service issue occurred.
3. Resend affected emails after the issue is resolved.
