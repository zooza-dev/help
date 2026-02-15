# Validation Report

**Generated:** 2026-02-15
**Scope:** All `.md` files in `content/` (including `_shared/doc-template.md`)
**Total files checked:** 135

## Summary

| Check | Status | Issues |
|---|---|---|
| Required frontmatter fields | PASS | 0 |
| Unique slugs | PASS | 0 |
| Unique intercom_id values | PASS | 0 |
| Exactly one H1 per doc | PASS | 0 |
| No skipped heading levels | FAIL | 1 file, 3 occurrences |
| Broken internal .md links | PASS | 0 (but 31 legacy external links remain) |
| Missing referenced assets | FAIL | Obsidian-style image refs in 2 files (17 refs) |
| Empty headings | WARN | 5 files, 14 empty `##` headings |

**Overall: FAIL** (heading level skips and unresolved Obsidian image references)

---

## 1. Required Frontmatter Fields

**Status: PASS**

All 135 files contain the required frontmatter fields: `title`, `slug`, `type`, `product_area`, `audience`, `status`, `source_language`, `needs_screenshot_replacement`, `last_converted`.

No issues found.

---

## 2. Unique Slugs

**Status: PASS**

All 135 slugs are unique across the knowledge base. No duplicates found.

---

## 3. Unique intercom_id Values

**Status: PASS**

All `intercom_id` values are unique. No duplicates found.

127 files have an `intercom_id` set. 8 files do not have one (field is optional per spec):

- `content/_shared/doc-template.md`
- `content/faq/blocks-faq.md`
- `content/faq/gocardless-faq.md`
- `content/faq/make-up-sessions-faq.md`
- `content/faq/orders-and-products-faq.md`
- `content/faq/pay-as-you-go-faq.md`
- `content/faq/roles-and-permissions-faq.md`
- `content/guides/creating-entry-passes.md`

---

## 4. Exactly One H1 Per Doc

**Status: PASS**

All 135 files contain exactly one `# H1` heading in the body (after frontmatter). No files have zero or multiple H1 headings.

---

## 5. No Skipped Heading Levels

**Status: FAIL -- 1 file, 3 occurrences**

| File | Line | Issue |
|---|---|---|
| `content/guides/gocardless-direct-debit-mandates.md` | 26 | H2 -> H4 skip: `#### Quick step-by-step` (parent is `## Link existing Direct Debit mandates`) |
| `content/guides/gocardless-direct-debit-mandates.md` | 62 | H2 -> H4 skip: `#### Option A: Apply a payment template to the whole class (recommended)` (parent is `## Create payment plans`) |
| `content/guides/gocardless-direct-debit-mandates.md` | 74 | H2 -> H4 skip: `#### Option B: Create payment plans manually per booking (Guide)` (parent is `## Create payment plans`) |

All three occurrences are in the same file. The file jumps from `##` (H2) directly to `####` (H4), skipping H3 entirely.

Note: The reference files (`payments-dashboard.md`, `bookings-list.md`, `products-list.md`, `services-list.md`, `clients-list.md`, `publish-widgets.md`) use H4 headings correctly nested under H3 headings. These are valid and are NOT violations.

---

## 6. Internal Link Checks

### 6a. Internal .md Links

**Status: PASS**

All relative `.md` links (e.g., `[text](../guides/blocks-creation.md)`) resolve to existing files within `content/`.

### 6b. Legacy External Links (informational)

**Status: WARN -- 31 references to `support.zooza.online`**

The following files still contain links to the legacy support portal (`https://support.zooza.online/...`) instead of internal `.md` links. These are not broken (the external URLs may still work) but should eventually be converted to internal links:

| File | Count |
|---|---|
| `content/guides/blocks-creation.md` | 1 |
| `content/guides/course-group-lesson-definition.md` | 3 |
| `content/guides/course-settings.md` | 4 |
| `content/guides/course-settings-tile.md` | 2 |
| `content/guides/customizing-widgets.md` | 1 |
| `content/guides/edit-events-in-courses.md` | 1 |
| `content/guides/individual-lessons-group-interested.md` | 2 |
| `content/guides/individual-lessons-with-free-lesson.md` | 1 |
| `content/guides/individual-sessions.md` | 3 |
| `content/guides/multi-day-event-with-product-offer.md` | 2 |
| `content/guides/payment-pairing.md` | 3 |
| `content/guides/summer-camps-creation.md` | 1 |
| `content/faq/common-booking-scenarios.md` | 1 |
| `content/setup/getting-started-with-zooza.md` | 2 |
| `content/setup/smartbill-invoices.md` | 1 |
| `content/setup/szamlazz-invoices.md` | 1 |

---

## 7. Referenced Assets

### 7a. Obsidian-style Image References (unresolved)

**Status: FAIL -- 2 files, 17 Obsidian-style image references**

These files use Obsidian wiki-link syntax (`![[filename.png]]`) instead of standard Markdown image syntax (`![alt](path)`). These references do not resolve to any asset and will not render in standard Markdown viewers.

#### `content/guides/creating-entry-passes.md` (10 references)

| Line | Reference |
|---|---|
| 31 | `![[Pasted image 20260215171140.png]]` |
| 32 | `![[Pasted image 20260215171825.png]]` |
| 33 | `![[Pasted image 20260215171914.png]]` and `![[Pasted image 20260215171927.png]]` |
| 36 | `![[Pasted image 20260215172133.png]]` |
| 38 | `![[Pasted image 20260215172156.png]]` |
| 47 | `![[Pasted image 20260215174403.png]]` |
| 48 | `![[Pasted image 20260215174429.png]]` |
| 57 | `![[Pasted image 20260215173842.png]]` |
| 58 | `![[Pasted image 20260215174014.png]]` |
| 70 | `![[Pasted image 20260215174056.png]]` |

#### `content/guides/pay-as-you-go-programme.md` (7 references)

| Line | Reference |
|---|---|
| 52 | `![[Pasted image 20260215165730.png]]` |
| 75 | `![[Pasted image 20260215165923.png]]` |
| 84 | `![[Pasted image 20260215165910.png]]` |
| 102 | `![[Pasted image 20260215170502.png]]` |
| 105 | `![[Pasted image 20260215170651.png]]` |
| 108 | `![[Pasted image 20260215170543.png]]` |
| 113 | `![[Pasted image 20260215170432.png]]` |

**Note:** The corresponding `Pasted image *.png` files exist in the repo root (`/Users/michaldodok/help/`) but have NOT been moved to `assets/images/` and are not referenced with correct relative paths. They need to be renamed to kebab-case, moved to `assets/images/`, and the Markdown references updated to standard syntax.

### 7b. Standard Markdown Image References

**Status: PASS**

All standard Markdown image references (`![alt](../../assets/images/...)`) resolve to existing files in the `assets/` directory. The 38 missing assets from the previous validation (2026-02-13) have all been resolved.

---

## 8. Empty Headings (informational)

**Status: WARN -- 5 files, 14 empty `##` headings**

Empty headings (`##` with no text after the `##` marker) create invisible structural elements and should be removed or replaced with content.

| File | Lines with empty `##` | Count |
|---|---|---|
| `content/guides/client-profile-101.md` | 32, 45, 59, 71, 83, 95, 107, 118 | 8 |
| `content/guides/individual-sessions.md` | 58, 100, 169 | 3 |
| `content/guides/discount-code.md` | 33 | 1 |
| `content/guides/selling-products-during-registration.md` | 106 | 1 |
| `content/guides/client-profile-dashboard.md` | 37 | 1 |

---

## Result: FAIL

**2 blocking categories:**

1. **Heading level skips** -- 3 violations in `content/guides/gocardless-direct-debit-mandates.md` (H2 -> H4, missing H3).
2. **Obsidian-style image references** -- 17 unresolved `![[...]]` references across 2 files (`content/guides/creating-entry-passes.md` and `content/guides/pay-as-you-go-programme.md`). Source images exist in repo root but need normalization into `assets/images/` with standard Markdown syntax.

**Non-blocking warnings:**

- 14 empty `##` headings across 5 files (cosmetic but affects document structure).
- 31 legacy external links to `support.zooza.online` should eventually be converted to internal `.md` links.
- 8 files do not have an `intercom_id` (field is optional per spec).
