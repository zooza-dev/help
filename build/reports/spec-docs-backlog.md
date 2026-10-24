# Spec documentation backlog

Generated: 2026-08-07
Source: api-v1/specs/implemented/ — specs with docs_communicated: "" (user-facing only)

## New articles needed

| # | Spec | Feature | Status |
|---|---|---|---|
| 1 | 2026-06-05-fastpay-direct-debit-provider.md | FastPay direct debit (UK BACS) — setup guide | [x] done — articles existed (fastpay-direct-debit.md + fastpay-faq.md), specs stamped |
| 2 | 2026-06-03-invoice-engine-superfaktura.md | SuperFaktura integration | [x] done — superfaktura-invoice-engine.md exists, spec stamped |
| 3 | 2026-06-24-refunds-report-endpoint-and-export.md | Refunds report & export | [x] done — section in reports-dashboard.md, spec to stamp |
| 4 | 2026-06-20-membership-segment-pricing.md | Membership segment pricing | [x] done — payg-segment-pricing.md exists, spec to stamp |
| 5 | 2026-07-17-share-link-email-endpoint.md | Share registration link by email | [x] done — share-course-link.md has "Share by email" section, spec to stamp |

## Update existing articles

| # | Spec | Feature | Target article | Status |
|---|---|---|---|---|
| 6 | 2026-07-16-course-listing-filters.md | Course catalog filter UI (payment model, features) | content/guides/ course listing or search | [ ] MISSING |
| 7 | 2026-07-03-printable-calendar-revamp.md | Printable calendar — multi-layout, localisation | content/guides/ printable-calendar | [ ] MISSING |
| 8 | 2026-07-02-billing-period-date-range.md | Billing period date range → auto-fills class wizard | content/setup/billing-periods.md | [ ] MISSING |
| 9 | 2026-06-11-auto-enrolment-age-from-extra-fields.md | Auto-enrolment age-source from extra fields | content/setup/auto-enrollment.md | [x] done — already covered, spec to stamp |
| 10 | 2026-06-10-admin-makeup-cancel-reissue-credit.md | Cancel make-up → re-issues credit (not re-seat) | content/guides/replacement-hours-complete.md | [x] done — already covered, spec to stamp |
| 11 | 2026-06-09-bulk-retention-operations.md | Bulk set/unset retention on registrations | content/setup/retention.md | [x] done — already covered, spec to stamp |
| 12 | 2026-06-03-email-template-image-uploads.md | Upload images directly in email template editor | content/guides/email-template-images.md | [x] done — full article exists, spec to stamp |
| 13 | 2026-06-02-event-document-attachments.md | Multi-upload documents to sessions, publish timing | content/guides/session-document-attachments.md | [x] done — full article exists, spec to stamp |
| 14 | 2026-06-26-widget-coupon-existing-registration.md | Apply coupon on widget payment screen (existing reg) | content/guides/discount-code.md | [ ] MISSING — needs new FAQ/section |
| 15 | 2026-05-29-trial-followup-todos.md | Trial attendance creates follow-up todo | content/setup/trial-sessions.md | [ ] MISSING — needs section in trial-sessions.md |
| 16 | 2026-07-15-async-box-backed-export-pipeline.md | Async exports — Exports listing + notification | content/guides/ (exports article) | [ ] MISSING — needs new article |
| 17 | 2026-07-14-direct-debit-mandate-contract-enrichment.md | Mandate list shows payment schedule + triage status | content/guides/ (direct debit mandates) | [ ] MISSING |
| 18 | 2026-07-06-invoice-billing-model-cutover.md | Per-profile reporting, multi-bank-account resolution | content/setup/invoice-profiles-and-bank-accounts.md | [x] done — already covered, spec to stamp |
| 19 | 2026-07-03-user-data-correction-risk-automation.md | Data correction auto-resolve (risk-free requests) | content/guides/data-correction-change-client.md | [ ] MISSING — needs section on auto-resolve |
| 20 | 2026-06-11-course-online-provider-connection-validation.md | Error when saving course with disconnected provider | content/ (Stripe/GoCardless setup) | [ ] MISSING |
| 21 | 2026-06-05-direct-debit-scheme-bacs-validation.md | DD_SETUP_INSTRUCTIONS merge var + BACS validation | content/guides/dynamic-tags.md | [ ] MISSING — needs entry in dynamic-tags.md |

## FAQ entries needed

| # | Spec | Feature | Target FAQ | Status |
|---|---|---|---|---|
| 22 | 2026-06-26-schedules-exclude-archived-courses.md | Archived-course schedules hidden from pickers | content/faq/programmes-timetables-sessions-faq.md | [ ] todo |
| 23 | 2026-06-23-installment-first-due-date-ignores-after-registration-setting.md | First installment due date respects "X days after registration" | content/faq/payments-and-billing-faq.md | [ ] todo |
| 24 | 2026-06-01-replacement-booking-capacity-race.md | User-facing error when make-up session is full | content/faq/make-up-sessions-faq.md | [ ] todo |

## Closed / already done

| # | Spec | Notes |
|---|---|---|
| ✓ | API-20260516-001 (Reviews module) | collecting-google-reviews.md + google-reviews-faq.md — handoff needs closing |
| ✓ | 2026-06-03-email-template-image-uploads.md | email-template-images.md already exists (created June 4, 2026) — verify and close |
