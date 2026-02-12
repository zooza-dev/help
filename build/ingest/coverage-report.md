# Support Ticket vs KB Coverage Analysis

**Generated:** 2026-02-11
**Source:** Cases__1 7.csv (Zoho Desk export)
**Total tickets:** 3,276
**Questions/requests analyzed:** 2,347 (bugs/outages excluded: 929)
**KB articles:** 86

## Executive Summary

| Status | Topics | Est. ticket mentions |
|--------|--------|-----------------------|
| **True gaps (no KB article)** | 4 | ~140 |
| **Depth gaps (article too thin for volume)** | 4 | ~350 |
| **False positive matches** | 3 | ~130 |
| **Well covered** | 33 | ~1,070 |

**~26% of question tickets** (estimated ~620) hit topics where the KB either has no article or an article too shallow to actually help.

## KB Coverage by Product Area

| Product Area | KB Articles | Ticket topics | True gaps | Depth gaps |
|---|---|---|---|---|
| Bookings | 6 | 5 | 0 | 1 (make-up lessons) |
| Calendar | 1 | 2 | 1 | 1 (only holiday-settings) |
| Classes | 5 | 1 | 0 | 0 |
| Clients | 5 | 5 | 0 | 0 |
| Communication | 11 | 7 | 0 | 0 |
| Orders | 1 | 2 | 0 | 0 |
| Payments | 18 | 7 | 0 | 1 (troubleshooting) |
| Programmes | 19 | 4 | 1 | 0 |
| Settings | 17 | 10 | 1 | 0 |
| Widgets | 3 | 1 | 0 | 1 (troubleshooting) |

## True Gaps — No KB article at all

### 1. Attendance tracking (35 tickets)
- **Product area:** Programmes
- **What people ask:** How to mark attendance, attendance reports, linking attendance to payments
- **Sample subjects:** "how to add a student to a different course for a replacement lesson", "nahradne hodiny", "Kalendar"

### 2. Login & account access (30 tickets)
- **Product area:** Settings
- **Incorrectly matched to:** `how-to-clear-your-cache` (clearing browser cache ≠ login help)
- **What people ask:** Password reset, can't log in, account access, inviting users

### 3. Calendar management (47+9 = ~56 tickets combined)
- **Product area:** Calendar
- **Incorrectly matched to:** `holiday-settings` (covers only holidays, not general calendar)
- **What people ask:** Event scheduling, daily view, rescheduling, calendar display issues
- **Only 1 KB article** for the entire Calendar product area

### 4. General class/group setup (~53 tickets)
- **Product area:** Classes
- **Incorrectly matched to:** `blocks-creation` (covers only blocks feature, not class management broadly)
- **What people ask:** Creating groups, setting capacity, assigning instructors, pricing

## Depth Gaps — Article exists but too shallow for ticket volume

### 1. Make-up lessons / replacements (144 tickets)
- **Current coverage:** Q7 in `common-booking-scenarios` (one paragraph)
- **Problem:** 144 tickets is the 3rd-highest topic. A one-line FAQ answer is insufficient.
- **Need:** Dedicated guide covering: creating make-ups, assignment logic, client portal workflow, expiry rules, credit system

### 2. Widget troubleshooting (94 tickets)
- **Current coverage:** 3 articles (customizing-widgets, deploying-zooza-on-website, zooza-sites)
- **Problem:** Articles cover setup/customization but not troubleshooting (widget not displaying, form errors, mobile issues)
- **Need:** Troubleshooting guide for widget display issues, embed problems, responsive design

### 3. Payment troubleshooting (~60 tickets estimated)
- **Current coverage:** 18 payment articles cover setup, templates, integrations
- **Problem:** No troubleshooting content — failed payments, declined cards, refund workflow, reconciliation
- **Need:** Payment troubleshooting guide covering common error states and recovery

### 4. Registration form troubleshooting (54 tickets)
- **Current coverage:** `online-registration` covers setup
- **Problem:** No troubleshooting — form not showing, validation errors, submission failures
- **Need:** Registration form troubleshooting guide

## False Positive Matches (corrected)

| Topic | Tickets | Matched to | Why it's wrong |
|---|---|---|---|
| Login & access | 30 | `how-to-clear-your-cache` | Cache clearing ≠ login/access help |
| Calendar management | 47 | `holiday-settings` | Holidays ≠ general calendar |
| General settings | 43 | `holiday-settings` | Holiday settings is calendar-specific |

## Well-Covered Topics

| Topic | Tickets | Top KB article(s) | Confidence |
|---|---|---|---|
| Payment issues (setup) | 167 | 18 Payments articles | High |
| Registration / booking flow | 151 | `online-registration` + 5 Bookings articles | High |
| Communication & notifications | 96 | 11 Communication articles | High |
| Payment schedules & plans | 71 | `billing-periods`, `payment-templates-creation` | High |
| Billing periods / terms | 59 | `billing-periods` | High |
| Parent portal & profiles | 58 | `parent-portal-101`, `parent-profile-dashboard` | High |
| Course / programme setup | 49 | 19 Programmes articles | High |
| Notifications | 48 | `automatic-event-notification`, `notifications-center` | High |
| Invoicing integrations | 42 | 4 invoice-specific articles | High |
| Email sending | 41 | `sending-email-sms`, `message-templates` | High |
| Instructor management | 38 | 6 lecturer/instructor articles | High |
| Client management | 33 | `client-import`, `data-correction-change-client` | High |
| GTC / GDPR consents | 26 | `setting-gtc-gdpr-consents` | High |
| Parent portal | 26 | `parent-portal-101` | High |
| GoCardless direct debit | 22 | `gocardless-direct-debit-mandates` | High |
| Transfer between courses | 21 | `common-booking-scenarios` | Medium |
| Reports & analytics | 21 | `power-bi-integration` | High |
| Dynamic tags | 21 | `dynamic-tags` | Medium |
| Trial lessons | 15 | `trial-lessons`, `trials-daily-business` | High |
| Waiting list | 14 | `group-interested` | High |

## Priority Recommendations — New articles to write

### Tier 1: High impact (>50 tickets each)

| # | Suggested title | Product area | Type | Tickets | Scope |
|---|---|---|---|---|---|
| 1 | **Make-up lessons: Complete workflow** | Bookings | guides | 144 | Setup, assignment, portal access, expiry, credit system |
| 2 | **Payment troubleshooting** | Payments | troubleshooting | ~60 | Failed payments, declined cards, refunds, recovery |
| 3 | **Registration form troubleshooting** | Bookings | troubleshooting | 54 | Form display issues, validation errors, submission failures |
| 4 | **Calendar management guide** | Calendar | guides | ~56 | Events, scheduling, rescheduling, daily/weekly views |

### Tier 2: Medium impact (20-50 tickets)

| # | Suggested title | Product area | Type | Tickets | Scope |
|---|---|---|---|---|---|
| 5 | **Widget troubleshooting** | Widgets | troubleshooting | ~40 | Display issues, mobile, embed problems |
| 6 | **Attendance tracking** | Programmes | guides | 35 | Marking attendance, reports, linking to payments |
| 7 | **Login & account access** | Settings | troubleshooting | 30 | Password reset, lockout, browser compatibility |
| 8 | **Class/group setup guide** | Classes | guides | ~25 | Creating groups, capacity, pricing, instructor assignment |

### Tier 3: Quick wins (existing articles to expand)

| Article to expand | Action needed |
|---|---|
| `common-booking-scenarios` | Fix broken link in Q7, expand or redirect to new make-up guide |
| `holiday-settings` | Rename/reframe as one of multiple Calendar articles |
| `how-to-clear-your-cache` | Keep but write separate login article — don't rely on this as "login help" |

## Verification Notes

These spot-checks confirm the gaps are real questions, not mis-tagged bugs:
- **Attendance:** "how to add a student to a different course for a replacement lesson", "nahradne hodiny" — genuine how-to questions
- **Login:** Subjects reference password reset, access problems — not outage reports
- **Calendar:** Mix of scheduling questions and display/view questions — not bugs about broken calendar
