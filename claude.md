# Claude Code instructions — Zooza KB conversion

Date baseline: 2026-02-11

This repository converts a legacy HTML knowledge base into a clean, English-only Markdown knowledge base,
then generates model-agnostic agent exports.

## Ingest folder
When the user says **"ingest"**, look up `../help_ingest/` (sibling directory to this repo) for reference material.
This folder contains raw inputs (e.g. chat exports, support tickets, feature notes) that should be
compared against or merged into the knowledge base in `content/`.
- If the user says "ingest chats" → look for chat-related files/folders in `../help_ingest/`.
- If the user says "ingest X" → look for files/folders matching X in `../help_ingest/`.
- Always compare ingest material against existing `content/` to identify gaps, outdated info, or new topics.

## Sibling repos (specs)
When the user asks for **"API spec"**, **"App spec"**, or **"Widget spec"**, look in these sibling directories:
- **API spec** → `../api-v1/docs/`
- **App spec** → `../app/docs/`
- **Widget spec** → `../widgets-v1/docs/`

Do not search for these paths — they are fixed. Use them directly.

## Non-negotiables
1. **Source of truth is `content/`** (English-only).
2. **Do not edit files under `legacy/`** except generating `manifest.json` and `content-map.yml`.
3. **Do not hand-edit files under `build/`** (generated).
4. Conversion must be **idempotent**:
   - Re-running conversion should not produce random diffs.
   - Use mapping files (`legacy/content-map.yml`) to keep paths and slugs stable.
5. **Do not block on screenshots** being Slovak; flag instead.

## Repo layout
- `legacy/html/` — input HTML
- `legacy/assets/` — input images/screenshots/attachments
- `content/` — canonical Markdown output (English)
- `assets/` — normalized images/attachments referenced by Markdown
- `build/normalized/` — intermediate Markdown (debuggable)
- `build/reports/` — conversion reports
- `build/exports/agent/` — JSONL agent pack exports

## Output URL scheme
All docs should be routable to: `/help/<product-area>/<slug>`
- `product_area` must match `taxonomy.yml`.
- `slug` is kebab-case, stable, unique.

## Required frontmatter (every doc)
Add YAML frontmatter:
```yaml
---
title: "..."
slug: "kebab-case"
type: "guides|setup|payments|troubleshooting|faq"
product_area: "Programmes|Classes|Calendar|Bookings|Orders|Clients|Payments|Settings|Widgets|Communication"
sub_area: ""            # optional (Email|WhatsApp)
audience: ["admin"]     # one or more from taxonomy.yml
tags: ["..."]
status: "published"     # draft|published|archived
source_legacy_path: "legacy/html/..."
source_language: "en|sk|mixed"
needs_screenshot_replacement: true|false
last_converted: "2026-02-11"
intercom_id: 12345678        # optional — Intercom article ID (set by kb:sync-ids)
intercom_sync: true           # optional — true=needs deploy, false=skip (set by kb:sync-ids)
---
```

## Conversion pipeline (kb:convert)
Perform these steps in order.

### Step A — Inventory legacy content
1. Crawl `legacy/html/` for `.html/.htm`.
2. For each file:
   - extract title (`<title>` or first `<h1>`)
   - detect language: `en`, `sk`, or `mixed`
   - list internal links to other legacy pages
   - list asset references (`img src`, `a href` to files)
3. Write `legacy/manifest.json` with the inventory.

### Step B — Create/refresh content map (stable slugs + paths)
Create `legacy/content-map.yml` entries for each legacy page:
- `legacy_path`
- `new_path` (under `content/<type>/...`)
- `slug`
- `type`
- `product_area`
- `sub_area` (optional)
- `status` (default `published` unless clearly obsolete)

Rules:
- Prefer product-area grouping based on page content and UI navigation.
- If unclear, default to `product_area: Settings` or `product_area: Payments` based on keywords.
- Slugs must be unique; if collision, add a short disambiguator.

### Step C — Extract main article body (strip chrome)
When converting HTML:
- Remove nav/sidebars/footers, cookie banners, search boxes, “related articles” widgets.
- Keep only the article content, including headings, lists, tables, callouts, and images.

### Step D — Translate to English (if needed)
If `source_language` is `sk` or `mixed`:
- Translate Slovak text to English.
- Preserve:
  - code blocks
  - URLs
  - emails
  - IDs/tokens
  - button/field names where they are already English in the UI
- Keep tone concise and instructional.
- Do not invent features.

### Step E — Convert to Markdown (semantic)
Markdown rules:
- Exactly one `#` H1 (from title).
- No heading level jumps.
- Procedures must be ordered lists.
- Buttons use **bold**; field names use `code`.
- Tables:
  - Keep as Markdown tables if small and readable.
  - Convert to definition-style bullets if large/complex.
- Rewrite legacy internal links to new repo-relative `.md` links using `legacy/content-map.yml`.

### Step F — Normalize assets
- **Always download remote images**: If HTML sources reference remote/external image URLs (e.g., CDN-hosted screenshots), download them to `assets/images/` with descriptive kebab-case filenames. Never leave remote URLs in the final Markdown.
- Copy/rename images into `assets/images/` (kebab-case).
- Update Markdown image paths to point to normalized local assets (e.g., `../../assets/images/filename.png`).
- Add **English alt text** for all images.
- If a screenshot is Slovak UI, set `needs_screenshot_replacement: true` but keep it.

### Step G — Split long pages
Split if:
- > 1200 words, OR
- > 8 H2 headings, OR
- multiple major workflows

When splitting:
- Keep an overview parent (if needed) and create child pages per workflow/H2 group.
- Ensure each page remains coherent and navigable.

### Step H — Extract FAQs into separate docs
If a page contains an FAQ section (English or Slovak):
- Extract into `content/faq/<topic>.md` (English).
- Replace original section with a short “See also” link (if configured).

### Step I — Generate redirects
Create `content/_redirects.yml` mapping old legacy paths/URLs to new `/help/...` URLs.
- Use stable mapping from `legacy/content-map.yml`.

### Step J — Write conversion report
Write `build/reports/conversion-report.md` containing:
- counts: pages processed, translated, split, faq extracted
- broken links found
- missing assets
- pages flagged `needs_screenshot_replacement`

## Validation (kb:validate)
Validation must fail if:
- any doc in `content/` is missing required frontmatter
- duplicate slugs exist
- duplicate `intercom_id` values exist (each ID must be unique across all docs)
- internal Markdown links are broken
- referenced assets are missing
- a doc has multiple H1 or skipped heading levels

Write a summary to `build/reports/validation-report.md`.

## Agent export (kb:export)
Generate `build/exports/agent/canonical.jsonl`:
- chunk by H2/H3 sections
- include metadata: title, slug, url, type, product_area, tags, audience, heading_path
- cap chunk size (~1600 chars) with small overlap (~150 chars)

Generate `build/exports/agent/faq.jsonl` from `content/faq/`:
- each Q/A becomes a record if feasible; otherwise store as section chunks.

## Style guide (English)
- Use short sentences.
- Prefer “Go to X → Y” navigation cues.
- Avoid marketing language.
- Be consistent with menu names: Programmes, Classes, Calendar, Bookings, Orders, Clients, Payments, Settings, Widgets, Communication.
