# kb:export-normalize — Pre-export content cleanup and validation

## Purpose
Clean and validate all `content/` files so they are ready for `kb:export`. This is a pre-flight step that catches problems that would corrupt or pollute the JSONL/web output without breaking the export script itself.

Run this before `kb:export` whenever new content has been added or edited.

## When to run
- Before pushing to staging or production
- After a batch of new articles or edits
- When user says "normalize export", "clean for export", or "pre-export check"

## Pipeline position
```
write content → kb:export-normalize → kb:export → commit JSONL
```

## What it checks and fixes

### 1. Obsidian syntax — block
Scan all `content/**/*.md` for `![[...]]` image references.
- If found: **stop and instruct the user to run `python3 scripts/fix_obsidian_images.py`** before continuing.
- Never auto-fix this — the script does the copy + rename + delete atomically.

### 2. Strip internal-only HTML comments from export output
The following comment types are for authors only and must NOT appear in the JSONL or web export:
- `<!-- Synonyms: ... -->` — SEO/intent keywords block at top of file
- `<!-- REVIEW: ... -->` — internal review notes
- `<!-- SCREENSHOT NEEDED: ... -->` — placeholder notes
- `<!-- FROM SPEC: ... -->` — traceability comments

**Action:** When generating the export (not the source files), strip these comments from chunk text. The source `.md` files are NOT modified — only the export output is cleaned.

> **Important:** Do NOT strip `<!-- -->` comments that are semantic (e.g. custom MDX components or valid HTML). Only strip the four patterns listed above.

### 3. Frontmatter completeness
For every `status: published` article, verify all required frontmatter fields are present and non-empty:
- `title`, `slug`, `type`, `product_area`, `audience`, `status`, `last_converted`

Flag articles missing any field. Do NOT auto-fill — list them for human review.

### 4. Broken internal links
Scan all `[text](../path/to/file.md)` references in `content/`.
- Check that the target `.md` file exists.
- Report broken links with file name and line number.
- Do not auto-fix — report only.

### 5. Missing image files
For every `![alt](../../assets/images/filename.png)` reference:
- Check that `assets/images/filename.png` exists.
- Report missing images.

### 6. Empty alt text on images
Flag any `![]()` image references with empty alt text.
- Report file and line number.
- Do not auto-fill alt text — report for human attention.

### 7. Duplicate slugs
Check that every `slug:` value across all `content/**/*.md` is unique.
- Report any duplicates.

### 8. needs_screenshot_replacement flag
List all articles with `needs_screenshot_replacement: true`.
- These are publishable but flagged — include them in the report so the user knows which screenshots are still needed.
- Do NOT block export for these.

### 9. Draft articles in export
Warn (do not block) if any `status: draft` articles are present. Draft articles are excluded from export by the export script, but it's useful to know they exist.

## Output

### Console summary (always)
```
kb:export-normalize complete

✅ Obsidian syntax: none found
✅ Frontmatter: all complete (85 articles)
⚠️  Broken links: 2 found (see report)
✅ Missing images: none
⚠️  Empty alt text: 3 images (see report)
✅ Duplicate slugs: none
📋 needs_screenshot_replacement: 8 articles flagged
📋 Draft articles: 2 (excluded from export)

Ready to run kb:export? Fix warnings first or run with --force to export anyway.
```

### Written report: `build/reports/export-normalize-report.md`

```markdown
# Export Normalize Report

**Generated:** YYYY-MM-DD
**Articles scanned:** N
**Blockers:** N (must fix before export)
**Warnings:** N (can export with --force)

## ❌ Blockers

### Obsidian syntax found
- `content/guides/some-guide.md:42` — `![[Pasted image 20260402...png]]`
  Fix: run `python3 scripts/fix_obsidian_images.py`

## ⚠️ Warnings

### Broken internal links
- `content/guides/inbound-payments.md:88` → `../guides/gocardless.md` (file not found)
- `content/faq/payments-and-billing-faq.md:142` → `../setup/billing-and-invoicing.md#multi-line-invoices` (anchor not verified)

### Empty alt text
- `content/guides/additional-fields.md:111` — `![](../../assets/images/additional-fields-01.png)`

## 📋 Needs screenshot replacement
- `content/guides/bulk-network-transfer.md`
- `content/guides/booking-form-attendee-selection.md`
- `content/setup/billing-and-invoicing.md`
(8 total — screenshots can be replaced after initial publish)

## 📋 Draft articles (excluded from export)
- `content/guides/some-draft.md` — status: draft
```

## Flags

| Flag | Behaviour |
|------|-----------|
| `--force` | Skip warnings, still block on Obsidian syntax |
| `--fix-alttext` | Auto-add filename as alt text for empty-alt images (last resort) |
| `--report-only` | Run all checks, write report, do not block or modify anything |

## Done definition
Complete when:
- All checks have run
- Console summary printed
- `export-normalize-report.md` written
- If blockers exist: tell the user to fix them before running `kb:export`
- If no blockers: confirm ready to run `kb:export`
