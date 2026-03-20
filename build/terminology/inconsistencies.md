# Terminology Inconsistencies

> Generated: 2026-03-14
> Scanner: kb:standardizer full rescan
> Files scanned: 174
> Source: `content/` (all subdirectories)

---

## Summary

| Metric | Value |
|---|---|
| Total source files scanned | 174 |
| Total canonical clusters tracked | 19 |
| Clusters with active conflicts | 9 |
| Clusters fully resolved (0 non-canonical) | 10 |
| Files with mixed terminology | 28 |
| Unknown / new terms flagged | 5 |
| New dictionary entries added this run | 6 |

---

## Resolved clusters (no action needed)

These clusters have zero non-canonical occurrences in the current corpus:

| Canonical | Status |
|---|---|
| lead collection | Clean — 48× correctly used across 23 files |
| Pay-as-you-go | Clean — 99× correctly used across 27 files |
| linked classes | Clean — no variants found |
| entry pass | Clean — 123× correctly used across 15 files |
| trial | Clean — 376× correctly used across 40 files |
| transfer | Clean — 164× correctly used across 40 files |
| copy | Clean — 13× correctly used across 6 files |
| billing period | Clean — 61× correctly used; "term" as generic English is not misuse |

---

## Active conflicts — mixed usage by file

### 1. programme (canonical) vs. course (deprecated)

**Status:** 51 non-canonical occurrences across 18 files. Down from 474 in Feb 2026 scan.

| File | Uses "course" (×) | Notes |
|---|---|---|
| `guides/programme-settings.md` | 13 | All in asset image filenames (`course-settings-*.png`) — prose is clean; filename rename not required |
| `guides/price-and-payment-setup.md` | 6 | Heading "Course fee vs Membership" + table cell "Course fee" — should become "Term payment vs Membership" |
| `faq/programmes-timetables-sessions-faq.md` | 7 | "bulk-delete courses" procedural section (lines 176–186) — needs full rewrite using "programmes" |
| `guides/programme-class-session-definition.md` | 1 | "type of course" in body — should be "type of programme" |
| `guides/blocks-creation.md` | 1 | "type of course" — should be "type of programme" |
| `guides/automated-notifications.md` | 2 | "During course" / "After course" toggle labels — may be verbatim UI text; verify before replacing |
| `guides/blocks-configuration.md` | 1 | "full course or a specific block" — replace with "full programme" |
| `guides/customizing-widgets.md` | 1 | "course offerings" — replace with "programme offerings" |
| `guides/individual-sessions-lead-collection.md` | 1 | "given course" — replace with "given programme" |
| `guides/new-programme-existing-clients.md` | 1 | "Of course" (idiomatic expression) — do NOT replace |
| `guides/user-roles.md` | 2 | "Of course" (×2, idiomatic) — do NOT replace |
| `guides/automatic-payment-reminders-detailed.md` | 1 | "Of course" (idiomatic) — do NOT replace |

**Action:** Rewrite procedural uses. Skip idiomatic "of course" and image filenames.

---

### 2. class (canonical) vs. group (deprecated)

**Status:** 104 non-canonical occurrences across 32 files. Not all are errors — see protected uses below.

Protected uses (do not replace):
- "Group classes" — UI label for multi-client class type (contrasts with "1-to-1 class")
- "group capacity" / "Group capacity" — widget capacity setting name
- "Group Session" — instructor rate type label
- Synonym comments in FAQ files

| File | Uses "group" (×) | Notes |
|---|---|---|
| `guides/king-of-a-group.md` | 12 | File name and feature title uses legacy "king of a group" — verify current UI term |
| `faq/trials-faq.md` | 9 | Several prose uses of "group" meaning "class" — replaceable |
| `troubleshooting/widget-embedding.md` | 9 | "group capacity" (protected UI label) — do not replace |
| `faq/programmes-timetables-sessions-faq.md` | 3 | "Group classes" (protected), other uses replaceable |
| `guides/individual-sessions-lead-collection.md` | 5 | "individual group" should be "individual class" |
| `guides/instructor-attendance-management.md` | 3 | "whole group" should be "whole class" |
| `faq/locations-and-venues-faq.md` | 3 | Synonym comments only |
| `guides/two-instructors-per-class.md` | 4 | Mix of protected "Group Session" rate label and replaceable "group" prose |

**Action:** Replace "group" → "class" in prose where it means the scheduling unit. Preserve protected UI labels listed above.

---

### 3. booking (canonical) vs. registration (deprecated)

**Status:** 187 non-canonical occurrences across 52 files. Many protected.

Protected instances: "online registration" (feature name), "registration fee", "registration widget".

| File | Uses "registration" (×) | Priority |
|---|---|---|
| `guides/edit-payment-on-booking.md` | 17 | HIGH — all replaceable |
| `setup/online-registration.md` | 17 | LOW — mostly protected (feature name) |
| `guides/replacement-hours-complete.md` | 14 | MEDIUM — mix |
| `guides/blocks-configuration.md` | 10 | HIGH — mostly replaceable |
| `faq/registration-and-booking-faq.md` | 13 | MEDIUM — FAQ title intentional; body replaceable |
| `guides/payment-tile-on-booking.md` | 8 | HIGH — replaceable |
| `guides/selling-products-during-booking.md` | 6 | HIGH — replaceable |
| `guides/payment-templates-creation.md` | 6 | MEDIUM |
| `guides/summer-camps-creation.md` | 7 | MEDIUM |
| `guides/automated-notifications.md` | 3 | MEDIUM |

**Action:** Run normalizer with smart preserves. Prioritise guides/edit-payment-on-booking.md, guides/payment-tile-on-booking.md, and guides/selling-products-during-booking.md.

---

### 4. client (canonical) vs. customer (deprecated)

**Status:** 17 non-canonical occurrences across 11 files. Nearly clean.

| File | Uses "customer" (×) | Notes |
|---|---|---|
| `glossary/terminology-review.md` | 6 | Intentional deprecated-term listing — keep |
| `reference/programme-settings.md` | 2 | Verbatim UI field label "Keep customer in auto-enrollment for N days" — keep until UI updated |
| `reference/bookings-list.md` | 1 | UI label context |
| `reference/settings-hub.md` | 1 | May be UI text |
| Other files | ~7 | Replaceable prose |

**Action:** Replace prose uses. Leave verbatim UI field strings pending UI update confirmation.

---

### 5. make-up session (canonical) vs. replacement variants (deprecated)

**Status:** 22 non-canonical occurrences across 6 files.

| File | Variant | Count | Notes |
|---|---|---|---|
| `guides/replacement-hours-complete.md` | replacement hour/hours | 9 | File title uses deprecated term — consider slug rename to `make-up-sessions-complete.md` with redirect |
| `glossary/terminology-review.md` | replacement session | 4 | Intentional deprecated listing — keep |
| `glossary/index.md` | replacement session | 2 | Intentional deprecated listing — keep |
| `guides/custom-replacement-lessons.md` | replacement lesson | 4 | Body replaceable; filename uses deprecated term — this file covers a distinct feature (custom/1-to-1 replacements), so "replacement lesson" may be intentional branding |
| `guides/automated-notifications.md` | replacement session | 1 | Replaceable |
| `faq/make-up-sessions-faq.md` | replacement session/lesson | 2 | Replaceable |

**Action:** Replace prose in `replacement-hours-complete.md` and `faq/make-up-sessions-faq.md`. Consider slug rename for `replacement-hours-complete.md`. Glossary entries intentional — keep.

---

### 6. auto-enrolment (canonical) vs. auto-continuation / auto-enrollment

**Status:** Three terms in active use.

| Term | Count | Files | Status |
|---|---|---|---|
| auto-enrolment | 20 | 7 | Canonical (British spelling) |
| auto-enrollment | 29 | 7 | American spelling — slug `setup/auto-enrollment.md` must stay stable |
| auto-continuation | 10 | 3 | Legacy — replace in prose |

Files with `auto-continuation` requiring action:

| File | Count | Action |
|---|---|---|
| `faq/programmes.md` | 7 | Replace "Auto-continuation" with "auto-enrolment" in headings and body |
| `guides/automated-notifications.md` | 2 | Rename section "Retention (auto-continuation)" → "Auto-enrolment notifications" |
| `glossary/index.md` | 1 | Rename "### Auto-continuation" heading → "### Auto-enrolment" |

Files mixing American/British spelling:

| File | Notes |
|---|---|
| `reference/programme-settings.md` | Mix of both — standardise body prose to British; keep verbatim UI field label if needed |
| `setup/auto-enrollment.md` | Slug stays; body prose should use "auto-enrolment" |

**Action:** Replace "auto-continuation" in prose. Standardise to British "auto-enrolment" in body text. Slug `auto-enrollment.md` is stable.

---

### 7. instructor (canonical) vs. trainer (deprecated)

**Status:** 3 new occurrences in `guides/custom-holidays.md`.

| File | Variant | Count | Notes |
|---|---|---|---|
| `guides/custom-holidays.md` | trainer / Trainer | 3 | Two instances + "Trainer availability" subheading — verify if UI label before replacing |
| `guides/instructor-substitution.md` | lecturer (image filenames) | 5 | Asset filenames only (`lecturer-substitution-*.png`) — alt text clean; filenames need not be renamed |
| `guides/two-instructors-per-class.md` | lecturer | 1 | In legacy external URL — do not modify link target |

**Action:** Replace "trainer" → "instructor" in `custom-holidays.md` prose. Flag "Trainer availability" for UI verification.

---

### 8. Client Profile (canonical) vs. parent portal (deprecated)

**Status:** 5 non-canonical occurrences across 4 files.

| File | Variant | Count | Notes |
|---|---|---|---|
| `faq/trials-faq.md` | parent portal | 3 | Lines 145, 147, 149 — all replaceable |
| `guides/replacement-hours-complete.md` | parent portal | 1 | Explanatory parenthetical "(the parent portal)" — can be removed |
| `guides/client-profile-101.md` | parent portal | 1 | In synonym comment `<!-- Synonyms: ... parent portal ... -->` — intentional |

**Action:** Replace in `faq/trials-faq.md` (3×). Remove parenthetical in `replacement-hours-complete.md`.

---

### 9. term payment (canonical) vs. course fee / term fee (deprecated)

**Status:** NEW cluster. 12 replaceable non-canonical occurrences (25 total minus glossary intentionals).

| Canonical | Variant | Count | Files |
|---|---|---|---|
| term payment | course fee / Course fee | 6 | `guides/price-and-payment-setup.md` |
| term payment | term fee / Term Fee | 6 | `setup/getting-started-with-zooza.md` |

**Action:** In `guides/price-and-payment-setup.md`, rename section "Course fee vs Membership" → "Term payment vs Membership". Replace "Course fee" with "Term payment". In `setup/getting-started-with-zooza.md`, replace "Term Fee" with "term payment".

---

## Variant frequency table

| Canonical | Variant | Count | Key Files |
|---|---|---|---|
| booking | registration | 187 | edit-payment-on-booking.md, replacement-hours-complete.md, blocks-configuration.md |
| class | group | 104 | king-of-a-group.md, trials-faq.md, widget-embedding.md |
| programme | course | 51 | programme-settings.md (filenames only), price-and-payment-setup.md, programmes-timetables-sessions-faq.md |
| auto-enrolment | auto-enrollment (American) | 29 | auto-enrollment.md (slug stable), programme-settings.md |
| auto-enrolment | auto-continuation | 10 | programmes.md, automated-notifications.md |
| make-up session | replacement hour/lesson/session | 22 | replacement-hours-complete.md, custom-replacement-lessons.md |
| session | lesson | 11 | glossary entries (intentional), make-up-sessions-faq.md |
| session | event | 24 | mostly legitimate context (local event, custom holiday) |
| client | customer | 17 | programme-settings.md (UI label), terminology-review.md (intentional) |
| term payment | course fee | 6 | price-and-payment-setup.md |
| term payment | term fee | 6 | getting-started-with-zooza.md |
| instructor | trainer | 3 | custom-holidays.md |
| Client Profile | parent portal | 5 | trials-faq.md, replacement-hours-complete.md |

---

## Files with mixed terminology — priority list (28 files)

| File | Conflicts | Priority |
|---|---|---|
| `guides/replacement-hours-complete.md` | registration (14×) + replacement hour (9×) + parent portal (1×) | HIGH |
| `faq/programmes-timetables-sessions-faq.md` | course (7×) + registration (3×) + group (3×) | HIGH |
| `guides/price-and-payment-setup.md` | course fee (6×) | HIGH |
| `guides/edit-payment-on-booking.md` | registration (17×) | HIGH |
| `setup/getting-started-with-zooza.md` | term fee (6×) | MEDIUM |
| `guides/automated-notifications.md` | auto-continuation (2×) + registration (3×) | MEDIUM |
| `faq/programmes.md` | auto-continuation (7×) | MEDIUM |
| `guides/blocks-configuration.md` | registration (10×) | MEDIUM |
| `faq/trials-faq.md` | group (9×) + parent portal (3×) | MEDIUM |
| `guides/payment-tile-on-booking.md` | registration (8×) | MEDIUM |
| `guides/selling-products-during-booking.md` | registration (6×) | MEDIUM |
| `guides/custom-holidays.md` | trainer (3×) | LOW |
| `guides/king-of-a-group.md` | group (12×, structural) | LOW — needs product discussion |
| `guides/custom-replacement-lessons.md` | replacement lesson (4×) | LOW |
| `glossary/index.md` | auto-continuation (1×, heading) | LOW |

---

## Unknown terms (need product review)

### 1. "trainer availability" — `guides/custom-holidays.md`
**Context:** "Custom holidays automatically appear as conflicts in trainer availability." (2×)
**Question:** Is "Trainer availability" a named UI section in the app? If yes, preserve verbatim. If not, use "instructor availability."

### 2. "king of a group" — `guides/king-of-a-group.md`
**Context:** A feature where one designated booking controls the class schedule. 12× "group" in this file.
**Question:** Is "king of a group" still the current UI feature name? If renamed, update slug (add redirect).

### 3. "retention" — `guides/automated-notifications.md`
**Context:** Section heading "Retention (auto-continuation)". Not found elsewhere as standalone term.
**Question:** Is "retention" used in any Zooza UI screen? If not, rename section to "Auto-enrolment notifications".

### 4. "Guest" as booking status — `reference/payments-dashboard.md`, `reference/communication-message-templates.md`
**Context:** Bookings can have "Guest" status (total revenue includes "Enrolled" and "Guest" statuses). Template "Booking as guest done" = enrolling as a guest to a full programme.
**Note:** This "guest" is distinct from "guest access to a booking" (second parent view-only access) and "guest instructor" (external role). These three uses of "guest" are not synonyms.
**Recommendation:** Add "Guest (booking status)" as a new dictionary entry. Clarify disambiguation in relevant docs.

### 5. "timetable" — scoped ambiguity
**Context:** Used 61× across 17 files. Deprecated as a synonym for "class" but actively used in Auto-Enrolment UI ("Timetables in Auto-Enrolment" section in `reference/programme-settings.md`).
**Recommendation:** Add scoped rule — deprecated when meaning a Class entity; preserved when referring to the Auto-Enrolment timetable picker UI component.

---

## Changelog (since last scan 2026-02-15, 130 files)

| Change | Detail |
|---|---|
| Files scanned | 130 → 174 (+44 new files) |
| New dictionary entries added | venue, term payment, trial, transfer, copy, billing period |
| Updated entries | instructor (trainer variant + preserve rules), auto-enrolment (split from auto-continuation, American spelling), make-up session (replacement session variant), class (Group classes + group capacity preserves), session (One-off Event preserve) |
| All counts refreshed | Occurrence counts updated to 174-file corpus state |
| Resolved clusters confirmed clean | lead collection, Pay-as-you-go, linked classes, entry pass, trial, transfer, copy |
| payment template conflict noted | terminology-review.md lists "payment template" as deprecated → "Payment Plan", but both are active distinct concepts. Flagged for product decision before normalizer runs. |
