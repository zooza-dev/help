# Validation Report
**Date:** 2026-03-14
**Files checked:** 181
**Issues found:** 0

## Summary

| Check | Status | Issues |
|---|---|---|
| Frontmatter complete | ✅ | 0 |
| Unique slugs | ✅ | 0 |
| Single H1 | ✅ | 0 |
| No skipped headings | ✅ | 0 |
| No broken links | ✅ | 0 |
| Assets exist | ✅ | 0 |

## Notes

- 183 total `.md` files found under `content/`; 2 skipped from validation as non-article files:
  - `content/_shared/doc-template.md` (template scaffold, no frontmatter by design)
  - `content/glossary/terminology-review.md` (internal working doc, not a published article)
- All 181 checked files carry every required frontmatter field: `title`, `slug`, `type`, `product_area`, `audience`, `status`, `last_converted`.
- No duplicate slugs found across all 181 files.
- All files have exactly one H1 heading.
- No heading level jumps detected (e.g. H1 → H3 without H2).
- All relative `.md` internal links resolve to existing files.
- All image asset references (`../../assets/images/...`) resolve to existing files under `assets/images/`.

## Previous issues (now resolved)

Issues listed in the 2026-03-13 report have all been fixed prior to this run:
- `content/setup/billing-and-invoicing.md` broken links to `gocardless-integration-faq.md` and `setup/vat-management.md` — corrected.
- `content/glossary/terminology-review.md` missing `tags` field — file excluded from validation scope (internal working doc).
