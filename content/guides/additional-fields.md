---
title: "Additional fields on the booking form"
slug: "additional-fields"
type: "guides"
product_area: "Programmes"
sub_area: ""
audience: ["admin"]
tags: ["additional-fields", "extra-fields", "booking-form", "date-of-birth", "age-restriction", "custom-fields"]
status: "published"
source_legacy_path: "legacy/html/labels-and-extra-fields.html"
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-17"
intercom_id: 13762570
intercom_sync: false
---

<!-- Synonyms: extra fields, custom fields, booking form fields, date of birth, age restriction, child's name, address field, business fields, ďalšie polia, extra polia, dátum narodenia, vekové obmedzenie -->

# Additional fields on the booking form

Additional fields let you collect extra information from clients during booking — such as a child's date of birth, address, allergies, or business invoicing details. You configure them per programme in the **Additional Fields** tile.

> **Navigation:** Go to **Programmes** → select a programme → **Edit Settings** → **Additional Fields**.

## Enabling additional fields

1. Open the programme's settings.
2. Click **Edit** on the **Additional Fields** tile.
3. Check **Extend booking form with additional fields**.
4. Configure the fields you need (see below).
5. Save.

Once enabled, the selected fields appear on the booking form for this programme.

> **Note:** Additional fields are configured at the programme level. If you use the same fields across multiple programmes, configure one programme first and then use **Copy programme** to duplicate the settings.

## Built-in fields

These fields are ready to use — you just enable them and optionally set a custom label.

| Field | Description | Notes |
|---|---|---|
| **Date of birth** | Client's or child's date of birth. | Can be used for age restriction (see below). |
| **Child's full name** | Full name of the child (for children's programmes). | Shown when the "For children" setting is active. |
| **Address** | Client's address. | Choose **Simple** (single text field) or **Structured** (street, city, zip code as separate fields). |
| **Number of occupied slots** | How many slots the booking occupies. | Useful for events like birthday parties where one booking takes multiple spots. |
| **Identification (birth) number** | National identification number. | Region-specific field. |

### Business fields

These fields are used for business invoicing. When one or more business fields are active, the booking form shows an option to register as a company. See [Business booking](business-booking.md) for the full workflow.

| Field | Description |
|---|---|
| **Business name** | Company name. |
| **Business address** | Company address. |
| **Business ID** | Company registration number. |
| **Tax ID** | Tax identification number. |
| **VAT** | VAT identification number. |

## Custom fields (Additional field 1–5)

You can add up to 5 custom fields. Each custom field has:

- **Name** — the label displayed on the booking form (required).
- **Type** — **Text** (free-text input) or **Choice** (dropdown picker).
- **Mandatory** — whether the field must be filled in before the client can submit the form.

### Choice fields (key-value picker)

When you select the **Choice** type, you define a list of options. Each option has:

- **Key** — a short code used in data exports (e.g., `beginner`, `intermediate`, `advanced`).
- **Value** — the text displayed to the client on the form (e.g., "Beginner", "Intermediate", "Advanced").

This is useful when you need structured data for reporting — the key ensures consistent values in exports regardless of the display text.

To configure a choice field:

1. Set the field type to **Choice**.
2. Click **Add option**.
3. Enter the key and value for each option.
4. Repeat for all options.
5. Save.

## Age restriction

The date of birth field can be used to restrict bookings by age. When enabled, clients whose child does not meet the age criteria cannot complete the booking.

### Setting up age restriction

1. Enable the **Date of birth** field.
2. Expand the age restriction options.
3. Choose the restriction method:
   - **By date of birth** — specify a minimum and/or maximum date of birth.
   - **By age** — specify a minimum and/or maximum age in years.
4. Save.

### Age restriction with waiting list

When a client's child does not meet the age criteria:

- The booking form shows a message explaining the restriction.
- If a **waiting list** is enabled for the programme, the client can join the waiting list instead of being rejected outright. This is useful for children who will reach the required age soon — they are added to the waiting list and can be enrolled when they qualify.

## Dynamic tags for additional fields

Additional field values can be used in email templates via dynamic tags. This lets you personalise confirmation emails and other communications.

| Tag | Field |
|---|---|
| <code>&#42;&#124;EF_DOB&#124;&#42;</code> | Date of birth |
| <code>&#42;&#124;EF_FULL_NAME&#124;&#42;</code> | Full name |
| <code>&#42;&#124;EF_ADDRESS&#124;&#42;</code> | Address |
| <code>&#42;&#124;EF_BUSINESS_NAME&#124;&#42;</code> | Business name |
| <code>&#42;&#124;EF_BUSINESS_ADDRESS&#124;&#42;</code> | Business address |
| <code>&#42;&#124;EF_BUSINESS_ID&#124;&#42;</code> | Business ID |
| <code>&#42;&#124;EF_TAX_ID&#124;&#42;</code> | Tax ID |
| <code>&#42;&#124;EF_VAT&#124;&#42;</code> | VAT ID |

For the full list of dynamic tags, see [Dynamic tags](dynamic-tags.md).

## What additional fields look like on the form

When additional fields are enabled, they appear below the standard booking form fields (name, email, phone). Business fields appear in a separate section that is shown when the client selects the "Register as company" option.

Custom choice fields appear as dropdown menus. Mandatory fields are marked with an asterisk (*).

## Related

- [Programme Settings Reference](../reference/programme-settings.md) — full field reference for the Additional Fields tile.
- [Business booking](business-booking.md) — registering bookings for companies.
- [Customizing widgets](customizing-widgets.md) — how extra fields appear on the booking widget.
- [Dynamic tags](dynamic-tags.md) — using field values in email templates.
- [Allowing multiple booking](allowing-multiple-booking.md) — collecting data from multiple attendees.
- [Personas](personas.md) — how Personas replaces extra fields for attendee tracking.
