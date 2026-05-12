# Terminology Inconsistencies

**Generated:** 2026-05-11
**Files scanned:** 231 (up from 174 on 2026-03-14)
**Total terms tracked:** 26

---

## Summary

| Metric | Count |
|--------|-------|
| Terms tracked | 26 |
| Terms fully resolved | 5 |
| Terms with active non-canonical usage | 12 |
| Terms with no inconsistencies | 9 |
| New terms added this scan | 1 (inbound payment) |
| Files with mixed terminology | 68+ |

---

## Status by term

| Canonical | Non-canonical count | Files affected | Status |
|-----------|---------------------|----------------|--------|
| booking | 526 | 104 | 🔴 High — bulk cleanup needed |
| class | 141 | 68 | 🔴 High — bulk cleanup needed |
| session (lesson) | 102 | 15 | 🟡 Partial — domain exceptions apply |
| programme | 79 | 30 | 🟡 Partial — priority files identified |
| client | 41 | 20 | 🟡 Partial — mostly API reference files |
| booking form | 60 | 42 | 🟡 Partial — legacy articles |
| venue (vs location) | 327 | 57 | ⚠️ Context-dependent — do not bulk replace |
| payment template / payment plan | 54 | 21 | ✅ Distinct concepts — no action needed |
| make-up session | 14 | 3 | 🟡 Small — 1 priority file |
| attendance states | 10 | 2 | 🟡 Small |
| cancel session | 10 | 9 | 🟡 Small |
| instructor | 7 | 2 | 🟢 Near-resolved |
| auto-enrolment | 1 | 1 | 🟢 Near-resolved |
| log in | 0 | 0 | ✅ Resolved |
| entry pass | 0 | 0 | ✅ Resolved |
| lead collection | 0 | 0 | ✅ Resolved |
| Pay-as-you-go | 0 | 0 | ✅ Resolved |
| transfer | 0 | 0 | ✅ Resolved |
| copy | 0 | 0 | ✅ Resolved |
| trial | 0 | 0 | ✅ Resolved |
| inbound payment | 44 | 22 | ℹ️ New — variants acceptable, monitor |

---

## Mixed usage by file — top offenders

### booking → registration (526 occurrences, 104 files)

This is the largest remaining inconsistency. 'registration' appears because:
1. It is part of the feature name 'Online Registration' (keep)
2. It is part of UI labels like 'registration widget' (keep)
3. It appears in dynamic tag names like `*|REGISTRATION_DATE|*` (keep)
4. It survives in legacy-converted articles not yet cleaned

Priority files to clean:
- `guides/edit-payment-on-booking.md` — estimated 17×
- `guides/blocks-configuration.md` — estimated 10×
- `guides/replacement-hours-complete.md` — high count
- `faq/registration-and-booking-faq.md` — slug stays, prose cleanup needed

**Rule:** Replace 'registration' → 'booking' everywhere except: 'Online Registration' (feature), 'registration widget', 'registration fee', dynamic tag names containing REGISTRATION.

---

### class → group (141 occurrences, 68 files)

'group' persists in business-models/ articles and some guides. Two distinct situations:

**Legitimate uses (do not replace):**
- 'group activities' — product naming in business-models/ directory
- 'target group' / 'age group' — email targeting context
- 'Group capacity' — widget capacity setting
- 'Group classes' — UI label for multi-client class type
- `guides/king-of-a-group.md` — feature name in title/slug (slug stable; replace prose uses)

**Replace in prose:**
- `business-models/children-group-activities-block.md` (11×)
- `business-models/adult-language-school.md` (11×)
- `business-models/index.md` (9×)
- `faq/programmes-timetables-sessions-faq.md` (7×)
- `business-models/children-group-activities-subscription.md` (7×)

---

### session → lesson (102 occurrences, 15 files)

**Domain-legitimate uses (preserve):**
- `business-models/individual-lessons.md` (15×) — about lesson-format businesses; 'lesson' is the industry term
- `business-models/adult-language-school.md` (8×) — same
- `business-models/index.md` (6×) — listing lesson as a business model type

**Replace in general context:**
- `setup/trial-sessions.md` (28×) — high count; likely uses 'lesson' where 'session' is correct
- `guides/custom-replacement-lessons.md` (9×) — slug stays, prose 'replacement lesson' → 'make-up session'
- `guides/replacement-hours-complete.md` (6×)
- `glossary/terminology-review.md` (3×) — intentional deprecation listing, keep

---

### programme → course (79 occurrences, 30 files)

'course' persists primarily in:
- `guides/programme-settings.md` (13×) — priority cleanup
- `guides/loyalty-sibling-discount.md` (8×) — loyalty articles introduced course language
- `business-models/adult-language-school.md` (7×) — VERIFY: 'course' is the industry term for language schools; confirm whether to keep or replace
- `setup/invoicing-overview.md` (6×) — setup articles
- `reference/inbound-payments-internals.md` (4×) — verbatim API field name; preserve

---

### client → customer (41 occurrences, 20 files)

**Preserve (do not replace):**
- `reference/inbound-payments-internals.md` (9×) — verbatim API terminology: 'customer ID', GoCardless customer object
- `reference/programme-settings.md` (3×) — UI label 'Keep customer in auto-enrollment'
- `guides/loyalty-returning-customer.md` — slug (stable), 'returning customer' in frontmatter tags

**Replace in prose:**
- `guides/loyalty-program.md:44` — "refer new customers" → "refer new clients"
- `guides/loyalty-program.md` (3× total)
- `guides/loyalty-returning-customer.md` (body text, not slug/frontmatter)
- `faq/xero-invoicing-faq.md` (3×)
- `faq/client-profile-faq.md` (2×)
- `setup/fakturoid-invoices.md` (2×), `setup/abra-flexi-invoices.md` (2×), `setup/szamlazz-invoices.md` (1×)

---

### make-up session → replacement lesson/hour (14 occurrences, 3 files)

Small — only 3 files remain:
- `guides/replacement-hours-complete.md` (6×) — priority; legacy article
- `guides/custom-replacement-lessons.md` (9×) — slug stays stable, prose needs updating
- `glossary/terminology-review.md` — intentional, keep

---

### venue vs location

**Do not bulk-replace.** 'location' has 327 occurrences across 57 files — it is used legitimately in:
- Navigation paths: "Settings → Locations"
- Dynamic tags: `*|LOCATION|*`
- Feature names: "Locations" settings section
- `faq/locations-and-venues-faq.md` (uses both deliberately)

Replace 'location' → 'venue' only when referring to the physical place entity in prose description.

---

## New term notes

### inbound payment (new entry)

- 'payment matching' and 'payment pairing' are both used (44 occurrences, 22 files).
- Both variants are acceptable — they describe the process accurately.
- Primary canonical: **inbound payment** (matches the UI: Payments → Inbound).
- Key distinction to enforce: GoCardless in Zooza = inbound payment matching. NOT direct debit mandates. Ensure no article conflates the two.

---

## Specific fixes needed

| File | Issue | Fix |
|------|-------|-----|
| `guides/loyalty-program.md:44` | "refer new customers" | → "refer new clients" |
| `guides/loyalty-program.md:9` | tag: "returning customer" | tag is acceptable; body prose fix only |
| `setup/trial-sessions.md` | 28× 'lesson' — review context | Replace general 'lesson' → 'session'; keep if domain-specific |
| `faq/trials-faq.md` | 3× 'parent portal' | → 'Client Profile' |
| `guides/replacement-hours-complete.md` | 6× 'replacement hour/lesson' | → 'make-up session' |
| `guides/programme-settings.md` | 13× 'course' | → 'programme' |
| `guides/custom-holidays.md` | 3× 'trainer' | → 'instructor' (check 'Trainer availability' for UI label) |

---

## Resolved since last scan (2026-03-14)

| Term | Was | Now | Notes |
|------|-----|-----|-------|
| log in | 29 non-canonical occurrences | 0 | Fully resolved |
| auto-enrolment | 10 auto-continuation + 29 auto-enrollment | 1 remaining | Near-resolved |
| make-up session | 22 | 14 | Reduced |
| Client Profile | 5 non-canonical | 5 | Unchanged — same 4 files |
