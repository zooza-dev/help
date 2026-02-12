# Support Ticket vs Knowledge Base — Coverage Report

**Generated:** 2026-02-11
**Method:** Full-text feature extraction from Subject + Description (SK/CZ/EN)
**Filter:** Setup & usage questions only (bugs/outages excluded)
**Source:** Cases__1 7.csv
**Total tickets:** 3,276
**Setup/usage questions analyzed:** 1,705
**Excluded:** 1,571

## Executive Summary

| Coverage level | Features | Ticket mentions | Action |
|---|---|---|---|
| **Gap** (no article) | 4 | 246 | Write new article |
| **Depth gap** (article too thin) | 2 | 285 | Expand existing |
| **Partial** (setup only, no troubleshooting) | 12 | 1179 | Add troubleshooting / expand |
| **Well covered** | 25 | 3097 | No action needed |

> **36% of feature mentions** (1,710 out of 4,807) hit under-served topics.

## Coverage by Product Area

| Product Area | KB articles | Gap features | Depth-gap features | Partial features |
|---|---|---|---|---|
| Bookings | 6 | 0 | 1 | 1 |
| Calendar | 1 | 1 | 1 | 1 |
| Classes | 5 | 0 | 0 | 2 |
| Clients | 5 | 0 | 0 | 0 |
| Communication | 11 | 0 | 0 | 1 |
| Orders | 1 | 0 | 0 | 0 |
| Payments | 18 | 1 | 0 | 2 |
| Programmes | 19 | 1 | 0 | 1 |
| Settings | 17 | 1 | 0 | 2 |
| Widgets | 3 | 0 | 0 | 2 |

## Gaps — No KB article at all

### Attendance tracking (115 mentions)
- **Product area:** Programmes
- **Issue:** 115 tickets. Zero KB articles. Major gap.
- **Sample questions:**
  - Dochadzka - viditelnost udajov
  - PODNET dochadzka
  - Statistika

### Schedule / timetable (77 mentions)
- **Product area:** Calendar
- **Issue:** No schedule/timetable management article.
- **Sample questions:**
  - Sorting the groups after name
  - Kalendar
  - Nezobrazuje klientke registracny formular na webe

### Login & account access (41 mentions)
- **Product area:** Settings
- **Issue:** Closest is how-to-clear-your-cache which is not login help. Need: password reset, account access, inviting users.
- **Sample questions:**
  - Zakaznicka sa nevie dostat do profilu
  - pripomienky na presunutý termín nechodia
  - Dobry den, klient Anton Duran sa nevie prihlasit, stale mu vyhadzuje, ze prihlasenie sa nepodarilo.

### Refunds & credit notes (13 mentions)
- **Product area:** Payments
- **Issue:** No refund/credit note workflow article. Only passing mentions.
- **Sample questions:**
  - Permanentky - připisování a odečítání částek manuálně?
  - Platby - nespárování a další postřehy, otázky
  - Storno podmienky zmena vety

## Depth Gaps — Article exists but too thin

### Make-up / replacement lessons (151 mentions)
- **Product area:** Bookings
- **Current articles:** `common-booking-scenarios`
- **Issue:** 144+ tickets. Only Q7 in FAQ mentions make-ups (one paragraph). Needs dedicated guide.
- **Sample questions:**
  - statistika omluvených a náhradních hodin
  - Ahoj, keď sa klient odhlasuje z náhradnej hodiny dostane túto hlášku aj keď máme povolené, aby sa z náhradnej hodiny odh
  - test Prosim neviem nastavit nahradne hodiny na kurze

### Calendar views & management (134 mentions)
- **Product area:** Calendar
- **Current articles:** `holiday-settings`
- **Issue:** 134 tickets vs 1 article that only covers holidays. No calendar views, scheduling, rescheduling guide.
- **Sample questions:**
  - BB lektor/kalendar vyvoj
  - Kalendar
  - Kopírovanie skupiniek

## Partial Coverage — Setup documented, troubleshooting missing

### Groups & classes setup (310 mentions)
- **Product area:** Classes
- **Current articles:** `blocks-creation`, `edit-events-in-courses`, `two-lecturers-per-group`
- **Issue:** blocks-creation covers blocks only. No general 'create a group/class' guide.

### Payments (general setup & config) (291 mentions)
- **Product area:** Payments
- **Current articles:** `payment-options`, `payment-tile-on-registration`, `edit-payment-on-registration`, `payment-labels-drawers`, `zooza-billing-payments`
- **Issue:** Setup covered well, but no troubleshooting (failed payments, recovery, declined cards).

### Lessons & events management (182 mentions)
- **Product area:** Calendar
- **Current articles:** `edit-events-in-courses`, `how-to-create-paid-events`, `viewing-billable-events`
- **Issue:** Event editing covered. No general 'managing lessons' overview.

### Capacity & participant limits (101 mentions)
- **Product area:** Programmes
- **Current articles:** `course-settings`, `allowing-multiple-registration`
- **Issue:** Capacity is a setting inside course config, not its own article. Common question deserves explicit section.

### Pricing & fee setup (77 mentions)
- **Product area:** Payments
- **Current articles:** `payment-options`, `payment-templates-creation`
- **Issue:** Price config is spread across multiple articles. No single 'how to set pricing' guide.

### Transfers between courses (59 mentions)
- **Product area:** Bookings
- **Current articles:** `common-booking-scenarios`
- **Issue:** Transfers mentioned briefly in booking scenarios. No step-by-step guide.

### Registration form config (50 mentions)
- **Product area:** Widgets
- **Current articles:** `online-registration`, `customizing-widgets`
- **Issue:** Setup covered. No troubleshooting (form not showing, validation errors).

### Data export & reports (29 mentions)
- **Product area:** Settings
- **Current articles:** `power-bi-integration`, `power-bi-data-description`
- **Issue:** Power BI covered. No guide for simple CSV/Excel export.

### Blocks & terms / semesters (29 mentions)
- **Product area:** Classes
- **Current articles:** `blocks-creation`, `billing-periods`
- **Issue:** Blocks covered. Term/semester lifecycle not clearly documented.

### Widgets & website embedding (19 mentions)
- **Product area:** Widgets
- **Current articles:** `customizing-widgets`, `deploying-zooza-on-website`, `zooza-sites`
- **Issue:** Setup/deployment covered. No troubleshooting (widget not showing, mobile issues).

### SMS messaging (17 mentions)
- **Product area:** Communication
- **Current articles:** `sending-email-sms`
- **Issue:** SMS mentioned alongside email. No dedicated SMS setup/troubleshooting.

### Branding & visual customization (15 mentions)
- **Product area:** Settings
- **Current articles:** `company-logo-email`, `customizing-widgets`
- **Issue:** Logo in email covered. No general branding/theme guide.

## Well-Covered Features

| Feature | Mentions | Key KB articles |
|---|---|---|
| Registration & booking flow | 586 | `online-registration`, `types-of-registrations`, `linked-registrations` |
| Client management (general) | 514 | `data-correction-change-client`, `personas`, `client-import` |
| Course / programme setup | 448 | `course-settings`, `course-settings-tile`, `course-group-lesson-definition` |
| Email & messaging | 426 | `sending-email-sms`, `send-email-after-event`, `message-templates` |
| Client profiles & accounts | 185 | `parent-profile-dashboard`, `parent-portal-101` |
| Parent portal & self-service | 123 | `parent-portal-101`, `parent-profile-dashboard` |
| Instructor / lecturer management | 120 | `zooza-101-instructors`, `change-instructor`, `lecturer-substitution` |
| GTC / GDPR consents | 110 | `setting-gtc-gdpr-consents` |
| Invoicing & invoice integrations | 80 | `xero-integration`, `abra-flexi-invoices`, `szamlazz-invoices` |
| Message templates | 78 | `message-templates`, `edit-event-notification-template`, `template-title` |
| Payment schedules & instalment plans | 64 | `payment-templates-creation`, `billing-periods` |
| Reports & analytics | 57 | `power-bi-integration`, `power-bi-data-description` |
| Notifications & alerts | 55 | `notifications-center`, `automatic-event-notification`, `edit-event-notification-template` |
| Outstanding amounts / debt | 51 | `outstanding-amount` |
| Payment pairing / matching | 43 | `payment-pairing` |
| Dynamic tags in messages | 30 | `dynamic-tags` |
| User roles & permissions | 28 | `user-roles` |
| Documents & attachments | 24 | `documents` |
| Trial lessons | 19 | `trial-lessons`, `trials-daily-business`, `individual-lessons-with-free-lesson` |
| Holidays & days off | 18 | `holiday-settings` |
| Data import | 14 | `client-import` |
| GoCardless / direct debit | 9 | `gocardless-direct-debit-mandates` |
| Discounts & promo codes | 9 | `discount-code`, `discount-types` |
| Waiting list & interested | 4 | `group-interested`, `individual-lessons-group-interested` |
| WhatsApp integration | 2 | `whatsapp-integration`, `whatsapp-faq`, `whatsapp-troubleshooting` |

## Priority: New articles to write

Ranked by ticket volume. Each line = one new article needed.

| # | Feature | Mentions | Status | Product area | Suggested action |
|---|---|---|---|---|---|
| 1 | **Groups & classes setup** | 310 | PARTIAL | Classes | Add troubleshooting section |
| 2 | **Payments (general setup & config)** | 291 | PARTIAL | Payments | Add troubleshooting section |
| 3 | **Lessons & events management** | 182 | PARTIAL | Calendar | Add troubleshooting section |
| 4 | **Make-up / replacement lessons** | 151 | DEPTH | Bookings | Expand existing → dedicated guide |
| 5 | **Calendar views & management** | 134 | DEPTH | Calendar | Expand existing → dedicated guide |
| 6 | **Attendance tracking** | 115 | GAP | Programmes | Write new article |
| 7 | **Capacity & participant limits** | 101 | PARTIAL | Programmes | Add troubleshooting section |
| 8 | **Schedule / timetable** | 77 | GAP | Calendar | Write new article |
| 9 | **Pricing & fee setup** | 77 | PARTIAL | Payments | Add troubleshooting section |
| 10 | **Transfers between courses** | 59 | PARTIAL | Bookings | Add troubleshooting section |
| 11 | **Registration form config** | 50 | PARTIAL | Widgets | Add troubleshooting section |
| 12 | **Login & account access** | 41 | GAP | Settings | Write new article |
| 13 | **Refunds & credit notes** | 13 | GAP | Payments | Write new article |
