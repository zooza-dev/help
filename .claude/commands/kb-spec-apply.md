# kb:spec-apply — Apply spec review findings to the knowledge base

## Purpose
Read the structured action list from `kb:spec-review` and apply it to the knowledge base:
create new articles, update existing ones, and add FAQ entries — all based on what the specs describe.

## Prerequisites
- Run `kb:spec-review` first to generate `build/reports/spec-review-actions.yml`
- The corresponding spec files must be accessible in `../api-v1/docs/` or `../app/docs/`

## When to run
- After `kb:spec-review` has been completed and the review report has been approved
- When the user says "apply spec" or "spec apply"

## Inputs
- `build/reports/spec-review-actions.yml` — structured action list from spec-review
- The original spec files (for content extraction)
- `content/` — existing KB articles
- `build/terminology/dictionary.json` — canonical terminology
- `taxonomy.yml` — product areas, doc types

## Process

### Step 1 — Load actions
Parse `spec-review-actions.yml`. For each spec entry, process `new_articles` and `update_articles`.

### Step 2 — Create new articles
For each entry in `new_articles`:

1. Read the source spec file and extract content from `source_sections`.
2. Create a new Markdown file at `suggested_path` with:
   - Full frontmatter (title, slug, type, product_area, audience, tags, status: published)
   - Content structured from the spec's key topics
   - Written in KB style guide tone (short sentences, "Go to X → Y" navigation cues)
   - All terminology normalized to canonical terms (check against `dictionary.json`)
3. Add `<!-- FROM SPEC: spec_id -->` comment at the top of the body for traceability.
4. Add `<!-- REVIEW: [specific question] -->` comments where the spec is ambiguous or missing user-facing detail.
5. Include screenshots placeholder if UI elements are described: `<!-- SCREENSHOT NEEDED: description of what to capture -->`

### Step 3 — Update existing articles
For each entry in `update_articles`:

**action: "add_questions"** (for FAQ articles)
- Read the existing FAQ file
- Append new Q&A entries at the end (before any closing section)
- Each question gets an `## ` heading
- Answer text derived from the spec, written in KB style
- Add `<!-- FROM SPEC: spec_id -->` for traceability
- Add `<!-- REVIEW: -->` where answer needs human verification

**action: "add_section"** (for guides/reference)
- Read the existing article
- Find the appropriate insertion point (based on logical flow)
- Insert a new `## ` or `### ` section with the content
- Keep existing content untouched
- Add `<!-- FROM SPEC: spec_id -->` for traceability

**action: "update_section"** (for existing sections that need changes)
- Read the existing section
- Merge new information from the spec
- Preserve existing content that's still valid
- Add `<!-- REVIEW: Updated from spec_id — verify this matches current UI -->`

### Step 4 — Normalize terminology
Run all new/updated content through the canonical terminology rules:
- Replace non-canonical terms from the spec (course→programme, group→class, etc.)
- Check against `build/terminology/dictionary.json`

### Step 5 — Set sync flags
For every file created or modified:
- Set `intercom_sync: true` in frontmatter
- Update `last_converted` to today's date

### Step 6 — Generate apply log
Write `build/reports/spec-apply-log.md`:

```markdown
# Spec Apply Log

**Run:** 2026-02-16
**Actions processed:** N
**Articles created:** N
**Articles updated:** N
**Review items:** N

## Created articles

### content/guides/payment-resolution.md
- **From spec:** BS-001
- **Title:** Resolving unmatched payments
- **Sections:** 3
- **Review items:** 2

## Updated articles

### content/faq/payments-faq.md
- **From spec:** BS-001
- **Action:** Added 2 new Q&A entries
- **Review items:** 1

## Review items (need human attention)

1. `content/guides/payment-resolution.md:25` — REVIEW: Where exactly is the resolution queue in the UI?
2. `content/guides/payment-resolution.md:42` — SCREENSHOT NEEDED: Payment resolution list view
3. `content/faq/payments-faq.md:85` — REVIEW: Confirm notification behaviour for unmatched payments
```

### Step 7 — Unanswered questions
If `spec-review-actions.yml` contains `questions_for_dev` that have not been answered:
- Do NOT guess or fabricate answers
- Add `<!-- REVIEW: Waiting for dev answer — [question] -->` in the KB article
- List all unanswered questions in the apply log

## Content rules

### Writing style
- Follow the KB style guide: short sentences, imperative, "Go to X → Y"
- Use canonical Zooza menu names: Programmes, Classes, Calendar, Bookings, Orders, Clients, Payments, Settings, Widgets, Communication
- Do not invent features — only document what the spec describes
- When the spec describes API/backend behaviour, translate it to user-facing language

### What NOT to do
- Do not delete or rewrite existing content that isn't related to the spec
- Do not change slugs or filenames of existing articles
- Do not remove existing `<!-- REVIEW -->` comments
- Do not write content for `questions_for_dev` that haven't been answered

### Traceability
Every piece of content derived from a spec must have a `<!-- FROM SPEC: spec_id -->` comment so we can trace what came from which spec and update it when specs change.

## Output
- Created/updated files in `content/`
- `build/reports/spec-apply-log.md` — changelog
- Console summary of actions taken

## Done definition
Complete when:
- All actions from `spec-review-actions.yml` have been processed
- New articles created with proper frontmatter and content
- Existing articles updated with new sections/questions
- All content uses canonical terminology
- `intercom_sync: true` set on all modified files
- Apply log written
- No fabricated content — only spec-sourced information
