# Spec Review Report

**Generated:** 2026-05-11
**Specs reviewed:** 95 (api-implemented: 83, api-in_progress: 2, business-specs: 10)
**KB articles scanned:** 231

---

## Summary

| Spec ID | Title | Status | KB Coverage | KB Gaps | Action |
|---------|-------|--------|-------------|---------|--------|
| API-20260422-002 | Todos | implemented | ✅ Full | — | None |
| API-20260425-001 | Slack integration | implemented | ✅ Full | — | None |
| API-20260428-001 | Awaiting payment / invoice_due_days | implemented | ✅ Full | — | None |
| API-20260420-001 | Downpayment invoice split | implemented | ✅ Full | — | None |
| API-20260422-001 | Manual push to offline queue | implemented | ✅ Full | — | None |
| API-20260408-001 | Bulk message queue & tracking | implemented | ✅ Full | — | None |
| API-20260421-001 | Scheduled cancellation merge vars | implemented | ✅ Full | CANCELLATION_SCHEDULED + CANCELLATION_DATE in dynamic-tags.md | None |
| BS-widget-person-rebooking | Widget person selection / rebooking | implemented | ✅ Full | — | None |
| BS-loyalty-program | Loyalty program (all phases) | implemented | ✅ Full | 7 articles | None |
| API-20260425-002 | Dashboard announcement events (real-time) | implemented | ✅ N/A | Backend-only, no user-facing behaviour | None |
| API-20260427-001 | Preset avatar selection | implemented | ✅ N/A | Minor UI change, no KB article needed | None |
| API-20260507-001 | Scheduled payment notification config | implemented | 🟡 Partial | Master switch + cooldown not documented | **Update article** |
| API-20260505-002 | Customer profile consents overview | implemented | ❌ Missing | No article covers client-side consent view or PDF download | **New article** |
| API-20260503-002 | Hide segmented schedule dates (widget option) | implemented | 🟡 Partial | Option not in widget config guide | **Update article** |
| API-20260501-001 | Widget list display options (grid/select) | in_progress | ⏳ Upcoming | — | Flag when shipped |
| API-20260506-001 | Ad-hoc payment auto-process past dates | in_progress | ⏳ Upcoming | Will need update to ad-hoc-scheduled-payment.md | Flag when shipped |

---

## Detailed Reviews

### API-20260507-001: Scheduled payment notification configuration

**Spec:** `../api-v1/specs/implemented/2026-05-07-scheduled-payment-notification-config.md`
**KB coverage:** Partial — `automatic-payment-reminders.md` and `automatic-payment-reminders-detailed.md` exist but cover only the reminder timing logic. The master switch and cooldown settings are not mentioned anywhere in the KB.

#### Gaps in KB (what to document)

1. **Master switch** — `Settings → Billing → Payments` now has a "Send scheduled payment notifications" toggle. When off, no scheduled payment email fires (pre-notice, at-creation, overdue all silenced). Post-charge confirmation is unaffected. This is a major admin-facing control that needs clear documentation.
2. **Cooldown setting** — When master switch is on, a "cooldown" period (in months) can suppress the at-creation email for Stripe stored card and GoCardless mandate customers when a previous payment in the same series was processed within that window. Bank-transfer customers always notify; first payment in a series always notifies.
3. **Where to find it** — Settings → Billing → Payments (this path is currently not in the where-to-find.md article either).

#### Affected KB articles
- `content/guides/automatic-payment-reminders.md` — add section: "Turn off scheduled payment notifications / control duplicate emails"
- `content/guides/where-to-find.md` — add "Scheduled payment notification settings" to the Settings table

#### Questions for dev
- What is the exact label in Settings UI for the cooldown field?
- Is there a UI indicator when cooldown suppresses a notification (for audit/troubleshooting)?

#### Terminology
- Spec uses correct terminology throughout.

---

### API-20260505-002: Customer profile — agreements overview & PDF download

**Spec:** `../api-v1/specs/implemented/2026-05-05-customer-profile-consents-overview.md`
**KB coverage:** Missing — no KB article documents the client-facing consents view in the Parent Zone / customer profile.

#### Gaps in KB (what to document)

1. **Where clients find their consents** — a "My data & consents" section in the customer profile / Parent Zone where clients can see every consent/agreement they've given to the company.
2. **What's shown** — list of all agreements (platform-level Zooza agreements + company agreements + course-specific agreements), whether each was accepted or declined, latest version per agreement.
3. **PDF download** — clients can download a single self-contained PDF summarising all their consents. Generated on demand (not stored).
4. **Admin context** — admins should know this exists so they can tell clients how to find their consent history when asked.

#### Suggested new article
- `content/guides/client-consent-overview.md` — "How clients can view and download their consents"
- Product area: Clients / Bookings
- Audience: admin (to explain to clients) + client-facing

#### Questions for dev
- What is the exact menu path in the Parent Zone / customer profile?
- Is the PDF download button visible only to the client, or can admin also generate it from the admin side?
- Are "not accepted" opt-in consents shown alongside accepted ones, or only accepted?

#### Terminology
- Spec uses "customer" → canonical: **client**
- "agreements" = consents in the KB — either term is acceptable; "consents" is more user-friendly

---

### API-20260503-002: Hide segmented schedule dates (widget option)

**Spec:** `../api-v1/specs/implemented/2026-05-03-hide-segmented-schedule-dates-option.md`
**KB coverage:** Partial — widget configuration is covered in `customizing-widgets.md` but the `hide_segmented_schedule_dates` option is not mentioned.

#### Gaps in KB

1. The new option "Hide dates for classes with multiple segments" in widget settings is not documented. Users who see this option will have no explanation of what it does.
2. Affects widget admins setting up registration widgets for classes with segments (Blocks).

#### Affected KB articles
- `content/guides/customizing-widgets.md` — add the `hide_segmented_schedule_dates` option under registration widget options

#### Terminology
- "schedule" (spec) = **class** (KB canonical)
- "segments" (spec) = **blocks** (KB canonical) — verify this mapping before documenting

---

### API-20260501-001: Registration widget list display options (in_progress)

**Spec:** `../api-v1/specs/in_progress/2026-05-01-registration-widget-list-display-options.md`
**Status:** Not yet shipped — do not document yet.

**Flag:** When implemented, update `content/guides/customizing-widgets.md` to add the `course_list_display` (select/grid) and `course_list_columns` (1–4) options under registration widget settings. This is a significant UX change for widget admins — the grid view gives clients a visual card-style programme browser instead of a dropdown.

---

### API-20260506-001: Ad-hoc payment auto-process past dates (in_progress)

**Spec:** `../api-v1/specs/in_progress/2026-05-06-ad-hoc-payment-auto-process-past-dates.md`
**Status:** Not yet shipped — do not document yet.

**Flag:** When implemented, update `content/guides/ad-hoc-scheduled-payment.md` to note that ad-hoc scheduled payments with a past due date are **processed immediately and silently** on creation — no customer notification fires. This prevents admin confusion ("I added a past-dated payment but it doesn't show as processed").

---

## What's already well covered

The following recently-implemented features have adequate KB documentation:

| Feature | KB articles |
|---------|-------------|
| Todos (personal task list) | `guides/todos.md`, `faq/todos-faq.md` |
| Slack integration | `setup/slack-integration.md`, `guides/zooza-in-slack.md`, `faq/slack-faq.md` |
| Awaiting payment status / invoice_due_days | `guides/automatic-payment-reminders.md` (documented May 2026) |
| Downpayment split invoicing | `setup/downpayment-split-invoicing.md` |
| Manual push to offline queue | `troubleshooting/offline-charge-manual-push.md` |
| Bulk email queue & tracking | `guides/bulk-email-send-tracking.md` |
| Scheduled cancellation merge vars | `guides/dynamic-tags.md` (CANCELLATION_SCHEDULED, CANCELLATION_DATE documented) |
| Loyalty program (sibling, returning, referral) | 7 articles in `guides/` + `faq/loyalty-faq.md` |
| Widget person rebooking | `guides/returning-client-booking-widget.md` |

---

## Terminology issues found in specs

| Spec term | Canonical KB term | Occurrences |
|-----------|-------------------|-------------|
| `customer` | **client** | BS-loyalty, API-20260505 |
| `course` | **programme** | Throughout API specs — intentional (internal API field name), documented in programme-class-session-definition.md |
| `schedule` | **class** | Throughout API specs — intentional (internal API field name) |
| `agreements` | **consents** | API-20260505 — both terms are acceptable; "consents" preferred in KB |

---

## Priority order for KB actions

| Priority | Action | Effort |
|----------|--------|--------|
| P1 | Update `automatic-payment-reminders.md` — add master switch + cooldown | Small |
| P1 | New article: client consent overview (Parent Zone) | Small–Medium |
| P2 | Update `customizing-widgets.md` — add hide_segmented_schedule_dates option | Small |
| P3 | Update `where-to-find.md` — add scheduled payment notification settings path | Tiny |
| When shipped | Update `customizing-widgets.md` — grid/list display option for registration widget | Small |
| When shipped | Update `ad-hoc-scheduled-payment.md` — past-dated auto-process behaviour | Tiny |
