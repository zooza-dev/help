# Knowledge Base Gap Analysis

**Generated:** 2026-02-13
**Source data:** 362 anonymized support conversations (Oct 2025 – Feb 2026), compared against 16 FAQ files (98 Q&A pairs) and ~80 guides/setup/reference docs.

---

## Executive Summary

Analysis of 5 months of support conversations reveals **12 major topic gaps** and **15+ existing articles needing expansion**. The top support drivers — replacement hours, dynamic tags, payment pairing, widgets, and role permissions — are either undocumented or only partially covered.

**Impact estimate:** Closing these gaps could deflect ~40–50% of "how-to" and "general question" tickets to self-service (FAQ, Fin AI chat, help articles).

---

## Part 1: Missing FAQ Topics (No Coverage)

### Priority 1 — High Volume, No FAQ

| # | Proposed FAQ | Tickets | Product Area | Rationale |
|---|---|---|---|---|
| 1 | **Replacement Hours FAQ** | 32+ | Calendar | Top non-payment pain point. No FAQ exists. Covers: eligibility rules, cross-company replacements, capacity, credit expiry, "sign back up" button. |
| 2 | **GoCardless FAQ** | 9 | Payments | 90-day connection expiry, bank-specific issues (SLSP, Tatra), renewal process, email-pairing alternative. Existing guide covers setup only, not lifecycle. |
| 3 | **Roles and Permissions FAQ** | 10 | Settings | Which role for which use case, hiding pay rates, menu visibility by role. Existing FAQ covers instructor login only, not role selection. |
| 4 | **Blocks (Term Segments) FAQ** | 9 | Programmes | Capacity per block, interaction with trials, dynamic tags, attendance visibility after block change. Completely undocumented. |
| 5 | **Orders and Products FAQ** | 8 | Orders | Unpaid order tracking, QR codes on product emails, voucher/pass management, dynamic tags not working in orders. Zero FAQ coverage for Orders product area. |
| 6 | **Client Management FAQ** | 14 | Clients | Manual client creation, changing client on registration, merging duplicates, email changes. Zero FAQ coverage for Clients product area. |

### Priority 2 — Medium Volume, No FAQ

| # | Proposed FAQ | Tickets | Product Area | Rationale |
|---|---|---|---|---|
| 7 | **Transfer and Copy FAQ** | 10 | Bookings | Transfer search UX, payment preservation, filter behavior, copy errors. Not in existing booking FAQ. |
| 8 | **Holiday and Term Management FAQ** | 8 | Programmes | Regional holiday settings, rescheduling impact, session cancellation. |
| 9 | **Login and Account FAQ** | 6 | Settings | Account deletion, verification, instructor login after email change, client creating accounts on wrong site. |

---

## Part 2: Existing FAQs Needing Expansion

| FAQ File | Current Q&A | Missing Questions from Support Data | Priority |
|---|---|---|---|
| **payments-and-billing-faq.md** | 8 | Payment correction vs. refund; payment schedule after copy/transfer; pro-rata calculation details; QR code troubleshooting | HIGH |
| **email-communication-faq.md** | 9 | Dynamic tags for replacements/blocks; manual registration skips confirmation email; template selection UX (system vs user); email delivery troubleshooting | HIGH |
| **attendance-and-catchups-faq.md** | 6 | "Excused" vs "did not attend" → replacement generation; extra capacity setting; cross-company replacement rules; no-show auto-marking | HIGH |
| **parent-portal-faq.md** | 5 | GDPR consent loop issue; cache clearing; "sign back up" button requirements; profile vs zooza.online confusion | HIGH |
| **registration-and-booking-faq.md** | 9 | Participant vs buyer on manual registration; second email on registration; viewing deleted registrations | MEDIUM |
| **programmes-timetables-sessions-faq.md** | 8 | Holiday skip after rescheduling; blocks interaction; session time display for 60+ min sessions | MEDIUM |
| **whatsapp-faq.md** | 4 | Beta status update; WhatsApp for Business availability | LOW |
| **instructor-access-faq.md** | 5 | Deactivating vs deleting instructor; substitute instructor email limits; rate type explanation | MEDIUM |
| **discounts-and-sibling-pricing-faq.md** | 5 | Late registration pro-rata override; fixed price ignoring pro-rata | MEDIUM |
| **trials-faq.md** | 7 | Trials + blocks capacity conflict; re-registration after trial in same group | MEDIUM |
| **waiting-list-faq.md** | 4 | Replacement-hour waiting list (queue); notification behavior | LOW |

---

## Part 3: Missing Guides (New Articles Needed)

| # | Proposed Guide | Type | Product Area | Content Scope |
|---|---|---|---|---|
| 1 | **GoCardless Connection Lifecycle** | guide | Payments | Renewal process, 90-day expiry, bank-specific quirks, switching to email-pairing |
| 2 | **Payment Correction vs Refund Decision Guide** | guide | Payments | When to use edit vs refund, impact on reports, step-by-step for common scenarios |
| 3 | **Replacement Hours Complete Guide** | guide | Calendar | Eligibility rules, capacity settings, cross-company setup, credit management, parent portal view |
| 4 | **Blocks Configuration Guide** | guide | Programmes | Setup, capacity, interaction with trials/dynamic-tags/attendance, known limitations |
| 5 | **Widget Embedding Troubleshooting** | troubleshooting | Widgets | Cookie/consent issues, WordPress plugin, filter syntax, HTTPS, base URL config |
| 6 | **Email Delivery Troubleshooting** | troubleshooting | Communication | Check sent logs, bounce codes, whitelisting, spam filter advice |
| 7 | **Role Selection Guide** | guide | Settings | Decision matrix: which role for which team member, what each role can see/do, hiding financial data |

---

## Part 4: Existing Guides Needing Updates

| Guide | What to Add | Priority |
|---|---|---|
| **dynamic-tags.md** | Complete tag reference table with data source per tag, supported contexts (registration vs order vs replacement), known limitations with blocks | HIGH |
| **automatic-payment-reminders.md** | Distinguish pre-payment/due/overdue notifications; explain timing (nightly batch); document the "zeroth" notification | HIGH |
| **message-templates.md** | System vs user templates; where each appears in UI; assigning templates to courses; manual registration email behavior | HIGH |
| **payment-pairing.md** | Revolut/reference-field matching; timing issues (payment before debt); email-notification pairing as alternative | HIGH |
| **gocardless-direct-debit-mandates.md** | Connection renewal, expiry warnings, bank-specific issues | HIGH |
| **payment-templates-creation.md** | Behavior during registration copy; "visible to clients" flag; anniversary date impact | MEDIUM |
| **late-registrations.md** | Pro-rata calculation transparency; fixed-price override option | MEDIUM |
| **holiday-settings.md** | Region-per-location setup; rescheduling impact on holiday rules | MEDIUM |
| **customizing-widgets.md** | Filter syntax (comma vs semicolon); consent/cookie handling; capacity display (session vs group) | MEDIUM |
| **user-roles.md** | Updated role capabilities; menu visibility changes; hide pay rates workaround | MEDIUM |

---

## Part 5: Content Optimized for AI / SEO / Fin Chat

### Recommendations for All New and Updated Content

1. **Standalone Q&A pairs** — Each FAQ answer should be self-contained (no "see above"). Fin AI retrieves individual chunks, not full pages.

2. **Keyword-rich H2/H3 headings** — Use the exact phrasing customers use:
   - "How do replacement hours work" (not "Make-up lesson policy")
   - "GoCardless connection expired" (not "Bank integration renewal")
   - "Payment reminder sent at midnight" (not "Notification timing")

3. **Decision tables** — For topics with multiple paths (correction vs refund, role selection), use comparison tables. These render well in AI retrieval and web search snippets.

4. **Step-by-step with UI references** — Use bold for buttons, code for field names, "Go to X → Y" navigation. This is how Fin presents answers.

5. **Screenshot opportunities** — Flag where a screenshot would reduce support load:
   - Payment pairing configuration screen
   - GoCardless connection status page
   - Role permission settings
   - Block configuration on a group
   - Dynamic tags reference (in-app location)
   - Widget embed code generator
   - Replacement hours settings

---

## Part 6: Proposed New Topic List (Prioritized)

### Tier 1 — Create First (highest ticket deflection)

1. `content/faq/replacement-hours-faq.md` — 12 Q&A pairs
2. `content/faq/gocardless-faq.md` — 6 Q&A pairs
3. `content/faq/roles-and-permissions-faq.md` — 7 Q&A pairs
4. `content/faq/blocks-faq.md` — 6 Q&A pairs
5. `content/faq/client-management-faq.md` — 8 Q&A pairs
6. `content/faq/orders-and-products-faq.md` — 6 Q&A pairs
7. `content/guides/replacement-hours-complete.md` — comprehensive guide
8. `content/guides/payment-correction-vs-refund.md` — decision guide
9. `content/troubleshooting/widget-embedding.md` — troubleshooting
10. `content/troubleshooting/email-delivery.md` — troubleshooting

### Tier 2 — Expand Existing (quick wins)

11. Expand `payments-and-billing-faq.md` (+4 Q&A)
12. Expand `email-communication-faq.md` (+4 Q&A)
13. Expand `attendance-and-catchups-faq.md` (+4 Q&A)
14. Expand `parent-portal-faq.md` (+4 Q&A)
15. Update `dynamic-tags.md` (tag reference table)
16. Update `automatic-payment-reminders.md` (notification types)
17. Update `payment-pairing.md` (edge cases)

### Tier 3 — Create Later

18. `content/faq/transfer-and-copy-faq.md`
19. `content/faq/holiday-management-faq.md`
20. `content/faq/login-and-account-faq.md`
21. `content/guides/gocardless-lifecycle.md`
22. `content/guides/blocks-configuration.md`
23. `content/guides/role-selection.md`

---

## Appendix: Data Summary

| Metric | Value |
|---|---|
| Total cases analyzed | 362 |
| Date range | Oct 2025 – Feb 2026 |
| Classification breakdown | General question: 153, Setup test: 80, How-to: 61, Other: 68 |
| Top tags | payments (29), communication (28), widgets (23), replacements (19), registrations (16) |
| Existing FAQ files | 16 (98 Q&A pairs) |
| Proposed new FAQ files | 9 |
| Proposed new guides | 7 |
| Existing articles to update | 15+ |
| Estimated new Q&A pairs | ~65 |
