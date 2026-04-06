# Knowledge Base Validation Report

**Date:** 2026-04-06
**Tool:** kb:validate

## Summary

| Metric | Count |
|---|---|
| Files checked | 198 |
| Files with issues | 0 |
| Total errors | 0 |
| Total warnings | 0 |

| Check | Result |
|---|---|
| Missing required frontmatter fields | **None found** |
| Duplicate slugs | **None found** |
| H1 violations (missing or multiple) | **None found** |
| Heading level skips | **None found** |
| Broken internal links | **None found** |
| Missing referenced assets | **None found** |

**Status: PASS**

---

## Issues by Category

### 1. Missing Required Frontmatter Fields

None found. All 198 files have all required fields: `title`, `slug`, `type`, `product_area`, `audience`, `status`, `last_converted`.

> **Note:** 19 files use multiline YAML list format for `audience` (e.g. `audience:\n  - admin`). This is valid YAML and was previously flagged as a false positive by the automated check. No action needed.

---

### 2. Duplicate Slugs

None found.

---

### 3. H1 Violations

None found. All 198 files have exactly one `#` heading.

---

### 4. Heading Level Skips

None found.

---

### 5. Broken Internal Links

None found. 3 broken links fixed in this run:

| File | Was | Fixed to |
|---|---|---|
| `content/guides/inbound-payments.md` | `./billing-and-invoicing.md` | `../setup/billing-and-invoicing.md` |
| `content/guides/inbound-payments.md` | `./gocardless.md` | `./gocardless-direct-debit-mandates.md` |
| `content/guides/invoice-buyer-data.md` | `./billing-and-invoicing.md` | `../setup/billing-and-invoicing.md` |

---

### 6. Missing Referenced Assets

None found. All image paths resolve to existing files in `assets/images/`.
