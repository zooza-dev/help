# Spec Audit — Undocumented User-Facing Features (Mar–Jul 2026)

**Audit date:** 2026-08-07
**Repos scanned:** api-v1, app, widgets-v1 — specs/implemented/2026-03* through 2026-07*
**Total specs reviewed:** ~200 across three repos
**Methodology:** Read spec files for ambiguous cases; checked KB coverage via keyword grep against content/

---

## Priority 1 — High impact, no KB coverage (write now)

### 1. Membership (PAYG) segment-based pricing
**Specs:** API-20260620-001 · APP-20260620-001 · widgets-v1/2026-06-21  
**What it does for the admin:** When setting up a pay-as-you-go (membership) payment schedule, admins can now configure a price table keyed by the number of schedule segments (blocks) a client selects — e.g. "1 block = €50/month, 2 blocks = €80, 3 = €100". The system automatically charges the correct tier based on which blocks the client chose. Previously PAYG billed a flat rate regardless of how many segments were selected.  
**What it does for the client:** A client who selects fewer blocks gets charged less per period automatically, with proration restricted to sessions in their chosen segments.  
**Suggested article type:** Guide  
**Suggested path:** `content/guides/payg-segment-pricing.md`  
**Article should cover:** Where to configure in the Payment schedule editor; how the price table entries work (money values, not multipliers); how to read the widget-side price display; fallback when no table is configured; interaction with prorated first payments; why per-segment discounts are gone in PAYG mode.

---

### 2. Refunds report
**Specs:** API-20260624-001 · APP-20260624-001  
**What it does for the admin:** A new dedicated **Payments → Refunds** report page shows all refunds as a row-level, paged, date-filterable list — the outbound mirror of the inbound payments list. Exportable to XLSX. This is for reconciliation and accounting ("how much did we refund this month?").  
**Existing KB article:** `content/guides/recording-an-administrative-refund.md` covers *recording* a single refund; `content/faq/administrative-refund-faq.md` answers related questions. Neither covers the Refunds *report* screen.  
**Suggested article type:** Reference (short)  
**Suggested path:** Add a new section to `content/reference/reports-dashboard.md` or create `content/guides/refunds-report.md`  
**Article should cover:** Where to find the Refunds report (Payments → Refunds); what data it shows (one row per refund: date, client, amount, method, registration); date range filter; export to XLSX; difference from the administrative-refund workflow.

---

### 3. Event attendees report (rescheduled / substituted / cancelled sessions)
**Specs:** API-20260509-003 · APP-20260509-003 · API-20260509-002 · API-20260509-001  
**What it does for the admin:** A new **Reports → Sessions** section with three entry points: Rescheduled, Substituted, Cancelled. Each view shows one row per (registration × disrupted session) — answering "which clients had their May sessions rescheduled?" and "export the list of clients whose sessions were cancelled". Includes an XLSX export. The Reports menu was also reorganised (Bookings and Trials now appear as direct sidebar entries; Make-up sessions moved from Calendar to Reports).  
**Suggested article type:** Guide + update reference  
**Suggested path:** `content/guides/event-attendees-report.md`  
**Article should cover:** How to access (Reports → Sessions → Rescheduled / Substituted / Cancelled); what one row means (client + registration + the specific disrupted session); filter options (date range, class, billing period, trainer, venue); XLSX export; difference from the session-level view in Calendar; the Reports menu reorganisation (breadcrumb change for Make-up sessions). Note: existing `content/reference/reports-dashboard.md` likely needs updating to reflect the new Reports menu IA.

---

### 4. Share course / class by email
**Specs:** APP-20260716-003 · API-20260717-001  
**What it does for the admin:** The "Copy link" button on courses and classes (both list and detail views) has been replaced by a **Share** button. The Share modal lets admins: pick which widget to link to (when multiple exist), copy or open the link, create a custom link, and — new — type in up to 10 email addresses to send the registration link directly to. Recipients do not need to be existing clients.  
**Suggested article type:** Guide  
**Suggested path:** `content/guides/share-course-link.md`  
**Article should cover:** Where the Share button appears; how to use each option (copy, open, custom link, email); the 10-recipient cap; anti-spam note (each address can receive at most one share email per 24 hours from the same company); what the email looks like to recipients.

---

### 5. Bulk retention operations on the bookings search
**Specs:** API-20260609-001 · APP-20260609-001  
**What it does for the admin:** A new **Operations** button on the bookings search page lets admins bulk-set or bulk-remove the retention flag for all registrations matching the current search filters (not just the displayed page). Includes a dry-run preview ("this will affect N bookings") before applying. Also controls whether to send the retention notification email immediately to those registrations.  
**Existing KB article:** `content/setup/retention.md` documents per-programme retention setup and the automatic cron flow. It has no mention of bulk manual operations.  
**Suggested article type:** New section in the retention guide  
**Suggested path:** Add a "Manually adjust retention" section to `content/setup/retention.md`  
**Article should cover:** Where the Operations button is (Bookings → search for registrations → Operations); two operations (Set in retention / Remove from retention); dry-run preview; notification modes (don't notify / notify those not yet notified / notify all); when you'd use this (correcting cron outcomes, triggering retention for a cohort the rules missed).

---

### 6. Printable calendar — configurable multi-layout export
**Specs:** API-20260703-002 · APP-20260703-001  
**What it does for the admin:** The downloadable PDF calendar (Calendar → Print) now offers four layout options: **Week per room**, **Board**, **Per day**, and **Compact**. You can select one or more layouts, choose which locations and rooms to include, and all selected sections render into a single PDF. Previously a single fixed layout. Empty weeks no longer crash.  
**Suggested article type:** Guide or update existing Calendar reference  
**Suggested path:** Create `content/guides/printable-calendar.md` or add a section to `content/reference/calendar.md`  
**Article should cover:** How to open the print dialog (Calendar → Print / export); the four layout options and what each shows; selecting locations and rooms; combining multiple layouts in one PDF; when to use each layout (single-venue vs multi-venue operators).

---

## Priority 2 — Medium impact or partial coverage (update existing)

### 7. Agreement consent versioning — "Require clients to consent again" checkbox
**Specs:** APP-20260722-001 · API-20260722-001  
**Gap in existing KB:** `content/faq/consents-and-agreements-faq.md` and `content/setup/setting-gtc-gdpr-consents.md` both state that when you update consent text "you will need to contact clients separately — Zooza does not automatically prompt existing clients to re-consent." **This is now outdated.** The new feature adds a "Require clients to consent again" checkbox in the agreement editor. Ticking it (with a confirmation step) mints a new consent version and queues a re-consent prompt for all clients who accepted the previous wording.  
**What to update:** In both files, replace the "contact clients separately" language with:
- How the checkbox works (unticked by default, requires confirmation when ticked)
- What "new version" means for existing consent records and GDPR audit trail
- What happens to clients (re-prompted at next booking or login, depending on consent type)
- The irreversible nature of version minting  
**Files to edit:**  
- `/Users/michaldodok/help/content/setup/setting-gtc-gdpr-consents.md` — add "Updating consent text" section  
- `/Users/michaldodok/help/content/faq/consents-and-agreements-faq.md` — update the versioning FAQ answer

---

### 8. Direct debit mandate triage view
**Specs:** APP-20260714-001 · API-20260714-001  
**Gap in existing KB:** `content/guides/gocardless-direct-debit-mandates.md` covers the legacy migration flow (linking imported mandates). The Mandates tab in Payments → Direct Debit has been significantly reworked into a filterable list showing: payment progress per mandate, offline-charge capability, triage filters (Needs attention / Not collecting offline), and a per-mandate recalculate button. Same offline-charge columns now appear on the per-registration Payment plan tab.  
**Existing KB article:** `content/guides/gocardless-direct-debit-mandates.md` — this guide only covers "Migration" (linking mandates). A new section or standalone article is needed for day-to-day mandate management.  
**What to add:** New section "Monitoring and troubleshooting mandates" in the GoCardless article or a separate `gocardless-mandate-health.md`. Cover: what the mandate listing shows; "Needs attention" filter definition (mandate can charge but isn't); "Not collecting offline" filter; recalculate button; how to read the Payment plan offline-charge columns.

---

### 9. Editable notes on the bookings list tiles
**Specs:** APP-20260522-001  
**Gap in existing KB:** No KB article covers the note widgets on registration tiles. Admins can now edit four note fields inline from the bookings list, without opening the registration detail:
- **Company note** (internal admin note visible to all admins)
- **Internal note** (personal note per user, shared across all their registrations)
- **Customer note** (the note the client submitted during booking)
- **Public note** (a note visible to the client in their profile)

A pencil icon opens a small edit modal for each note.  
**Suggested action:** Add a "Editing notes from the bookings list" section to `content/reference/bookings-list.md`.

---

### 10. Payment notification settings — review comments need resolution
**Specs:** API-20260507-001 · APP-20260507-003  
**Partial coverage:** `content/guides/automatic-payment-reminders.md` has a section on the notification master switch and cooldown. However the file contains `<!-- REVIEW -->` comment blocks flagging two things to verify:
1. The exact UI label for the cooldown months field in Settings → Billing → Payments.
2. Whether there is an audit log or indicator when a notification is suppressed by cooldown.

These should be resolved by reviewing the actual UI and updating the article. The payment settings page (Settings → Billing → Payments) was also reorganised — verify the guide's navigation instructions match the current layout (cards: Scheduled-payment notifications / Payment confirmations / Client-facing payment terms).

---

## Priority 3 — Minor / niche (low urgency)

### 11. Szamlazz — custom invoice number prefix
**Spec:** API-20260423-001  
**What it does:** Admins using Számlázz.hu can now configure a custom prefix for invoice numbers generated by Zooza. Previously, the invoice number series was controlled only by Számlázz itself.  
**Action:** Add one line to `content/setup/szamlazz-invoices.md` under the "Invoice numbers" or "Settings" section.

### 12. Course-level media attachments (videos, documents, URLs)
**Spec:** API-20260407-002 (api-v1 + app + widgets-v1 handoffs)  
**What it does:** Admins can now attach videos, documents, and URLs at the **programme (course) level**, not just at the schedule or session level. Course-level media appears across all classes in that programme in the client widget.  
**Gap:** `content/guides/documents.md` covers schedule and session levels. It needs a note that the same attachment types work at the programme level too, and that course-level media appears in the client profile widget for all classes under that programme.

### 13. QR code downpayment merge variable
**Spec:** API-20260319-001  
**What it does:** A new merge variable `*|QR_CODE_DOWNPAYMENT|*` is available in email templates for use when a registration requires a downpayment. Inserts a QR code image for the downpayment amount.  
**Action:** Add one row to the merge variables table in `content/guides/dynamic-tags.md`.

### 14. Loyalty rule name field
**Spec:** API-20260503-001  
**What it does:** Loyalty discount rules now have a **Name** field — previously rules were only identified by their position in the list. Makes rule management clearer when multiple rules exist.  
**Action:** Note in `content/guides/loyalty-sibling-discount.md` or the loyalty FAQ that rules can be named.

### 15. Billing period date range in class creation
**Spec:** API-20260702-001 · APP-20260702-001 (simple wizard)  
**What it does:** When creating a class and selecting a billing period, admins can now specify an explicit start and end date range (rather than always spanning the full billing period). Relevant for classes that start or end mid-term.  
**Action:** Minor note in `content/guides/blocks-creation.md` or the class creation guide.

### 16. Auto-enrolment age from extra fields (date of birth)
**Spec:** API-20260611-001  
**What it does:** The age filter in auto-enrolment rules can now draw the date of birth from the standard date-of-birth extra field, not just a manually-specified date. Minor enhancement that matters for operators using auto-enrolment with children's programmes.  
**Action:** Update `content/setup/auto-enrollment.md` if it mentions how age is sourced.

---

## Already covered (confirmed)

| Feature | KB article(s) |
|---|---|
| Custom holidays (create/edit/delete company holidays) | `content/guides/custom-holidays.md`, `content/faq/holiday-management-faq.md` |
| Cross-network registration transfer | `content/guides/bulk-network-transfer.md`, `content/faq/transfer-and-copy-faq.md` |
| Convert registered / waitlist → trial | `content/guides/trials-daily-business.md` (section: "How to convert an existing booking to trial status") |
| Extra fields 1–15 + citizenship field | `content/guides/additional-fields.md` ("up to 15 custom fields"; citizenship listed) |
| Ad hoc (one-off) scheduled payment | `content/guides/ad-hoc-scheduled-payment.md` |
| Payment plan history + admin note | `content/guides/ad-hoc-scheduled-payment.md` (section: "Payment plan history") |
| Slack integration | `content/setup/slack-integration.md`, `content/guides/zooza-in-slack.md`, `content/faq/slack-faq.md` |
| Todos task list | `content/guides/todos.md`, `content/faq/todos-faq.md` |
| Auto-cancel unpaid registrations | `content/guides/auto-cancel-unpaid-registrations.md` |
| Scheduled registration cancellation + merge vars | `content/guides/scheduled-registration-cancellation.md` |
| Email template image uploads | `content/guides/email-template-images.md` |
| Daily calendar swimlanes (room view) | `content/guides/daily-calendar-swimlanes.md` |
| Session document attachments | `content/guides/session-document-attachments.md` |
| Superfaktura invoice engine | `content/guides/superfaktura-invoice-engine.md` |
| Payment notification master switch + cooldown | `content/guides/automatic-payment-reminders.md` (partial — see P2 item 10) |
| WhatsApp setup and integration | `content/setup/whatsapp-integration.md`, `content/troubleshooting/whatsapp-troubleshooting.md` |
| Google Reviews module | `content/setup/collecting-google-reviews.md` |
| Invoice profiles & bank accounts | `content/setup/invoice-profiles-and-bank-accounts.md` |
| E-invoicing mandates (SK 2027 / Peppol) | `content/setup/e-invoicing-mandates.md` |
| FastPay direct debit | `content/guides/fastpay-direct-debit.md`, `content/faq/fastpay-faq.md` |
| Invoice buyer data management | `content/guides/invoice-buyer-data.md` |
| Administrative refund for online payments | `content/guides/recording-an-administrative-refund.md` |
| Trash and restore (soft-delete) | `content/guides/trash-and-restore.md` |
| Retention (per-programme setup + FAQ) | `content/setup/retention.md` |
| Szamlazz invoice integration | `content/setup/szamlazz-invoices.md` |
| Payment settings overhaul (page reorganisation) | `content/guides/automatic-payment-reminders.md` (navigation paths already updated) |
| Email templates redesign (search/filter) | `content/reference/communication-message-templates.md` |
| Communication menu dispersal | `content/reference/app-navigation-map.md` (navigation covered) |

---

## Internal only (skipped)

The following were classified as non-user-facing and require no KB articles:

**Backend / infrastructure:**
- JWT/auth internals (jwt-region-binding, jwt-issuance-tracking, auth-app-pin-login-and-jwt-bearer, login-requested-event-pin-cleanup)
- Database migrations only (inbound-payment-benchmarks, scheduled-payment-adjustments-ledger, payment-deduplication, payment-dedup-analytics-rules, payment-deduplication-redesign)
- Worker systems (client-import-worker-system, inbound-payment-staging-reaper, async-box-backed-export-pipeline)
- Materialized views / caching (materialized-views-attendance-listing-tile, schedule-bare-place-name-materialization, attendance-waitlist-materialization-fix, mcp-feedback-state)
- Event dispatcher / system message stream infrastructure (event-dispatcher, system-message-stream)
- Invoice engine internals (invoice-engine-error-handling, multi-line-foundation/activation/cleanup, zooza-invoice-engine foundation phases)

**Data plumbing / API internals:**
- Role-scoped extra fields contract, generic-engine-options-keys, company-entitlements-endpoint
- Bulk-network-transfer-endpoint (API endpoint backing a UI already documented)
- Events-preview-endpoint, events-data-owner-export (internal to the API layer)
- Payment-dedup-analytics-rules, deterministic-payment-ignore-filters
- Single-schedule-event-attendance-sync, replacement-booking-capacity-race
- Participant-merge-preserve-relationships, ad-hoc-relationship-and-role-repair
- Person-extra-fields-sync-hardening, buyer-only-extra-fields-validation (server-side validation hardening)
- Currency-not-propagated-manual-orders, profile-widget-order-value-double-counts (bug fixes)
- Reminders-exclude-archived-courses, schedules-exclude-archived-courses (silent behaviour fix)
- Event-capacity-stale-on-delete, order-item-add-debt-itemization-divergence (bug fixes)
- Account-level-statement-source, inbound-reconciliation-account-level (reconciliation internals)
- Customer-file-access-enrollment-scope (internal security scoping)
- Event-summary-last-editor (minor data field)
- Payg-maybe-add-payment-schedule-end (internal calculation)

**Frontend component / framework work (no new user feature):**
- Combobox adoption, input-combobox-design, filter-v2-component-migration, card-loader-v2, action-toolbar-component, ajax-button-enhancements, toast-system, requirejs-error-recovery, api-client-hardening, page-layout-migration, error-success-feedback-sweep, input-version-empty-state-sweep, label-component-redesign, finish-legacy-css-z2-migration
- Right-sidebar-bundle-orchestrator, unified-right-sidebar-shell, mobile-sidebar-routes, entity-cache-layer, unified-entity-cache-migration, calendar-prep-material-library
- Registrations-page-redesign, registrations-tile-prototype (internal redesign — nav paths covered in KB)
- Schedule-list-rendered-callback, registration-widget-rollup-migration, registration-mvvm-refactor
- Extract-agreements-to-shared-module, extract-stripe-connect-payments-module (code extraction)
- Componentize-create-place, componentize-create-trainer

**MCP / AI-internal tooling:**
- mcp-feedback-state, mcp-model-performance-page, mcp-promo-tips, mcp-page-surface-editing-capability, llm-pairer-call-tightening, import-payment-pairer (AI/LLM pipeline internals)

**Ops / data-correction tools:**
- Matko-makeup-eligibility-tester, matko-replacement-eligibility-diagnostic (internal diagnostic tools)
- User-data-correction-risk-automation, data-correction-intent-and-async-verdict (internal admin tools)
- Ops-recalculate-dob-age-materializations (internal recalculation job)
- Changelog-v2 + changelog-v2-page (internal changelog infrastructure)
- Block-inactive-companies (internal company state management)

---

*Generated 2026-08-07. Next spec audit recommended after the next changelog release.*
