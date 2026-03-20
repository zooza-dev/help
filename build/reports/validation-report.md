# Validation Report
**Run:** 2026-03-14
**Files checked:** 175
**Errors:** 3
**Warnings:** 0

## Errors (must fix)

### Missing frontmatter

- `content/glossary/terminology-review.md` — missing: `tags`

### Duplicate slugs

None.

### Multiple H1

None.

### Broken internal links

- `content/setup/billing-and-invoicing.md:99` — links to `../faq/gocardless-integration-faq.md` (file not found; correct path is `../faq/gocardless-faq.md`)
- `content/setup/billing-and-invoicing.md:183` — links to `../setup/vat-management.md` (file not found; correct path is `../guides/vat-management.md`)

### Missing assets

None.

## Warnings (should fix)

### Skipped heading levels

None detected.

## Notes

- `content/glossary/terminology-review.md` is marked `status: "draft"` and carries all other required fields, but the `tags:` key is absent entirely (not just empty). All other 174 files carry the full required frontmatter set. Several files use `tags: []` (empty list); that counts as present.
- `content/setup/billing-and-invoicing.md` has two broken cross-links in its **Related** section. The file `faq/gocardless-integration-faq.md` does not exist; the correct file is `faq/gocardless-faq.md`. The file `setup/vat-management.md` does not exist; VAT management lives at `guides/vat-management.md`.
- All 175 files have exactly one H1 heading.
- No duplicate slugs were found across all 175 files.
- All heading hierarchies were valid — no H3 jumping directly from H1, no H4 jumping directly from H2, etc.
- All image asset references resolved successfully. Both `assets/images/` (flat) and `assets/images/reference/` (subdirectory used by reference docs) were checked.
- All same-directory `.md` relative links (e.g. `programme-settings.md`, `user-roles.md`) were verified as valid within their respective directories.
- The old validation report (2026-02-15) listed 53 missing assets; all of those images now exist on disk.

## Summary

| Check | Pass | Fail |
|---|---|---|
| Frontmatter complete | 174 | 1 |
| Unique slugs | 175 | 0 |
| Single H1 | 175 | 0 |
| Heading levels | 175 | 0 |
| Internal links | 173 | 2 |
| Assets present | 175 | 0 |
