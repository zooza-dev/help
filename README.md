# Zooza Knowledge Base (Docs-as-Code)

This repo is the **source of truth** for Zooza’s help content.

## Goals
- Convert legacy HTML (+ assets) into clean, **English-only** Markdown.
- Store canonical docs in `content/`.
- Generate **model-agnostic** agent exports (JSONL) from the same canonical docs.
- Keep vendor/platform targets as **generated adapters** (optional).

## Quick start
1. Put the legacy export into:
   - `legacy/html/` (HTML files)
   - `legacy/assets/` (images/screenshots/attachments)
2. Run conversion (Claude Code custom command):
   - `kb:convert`
3. Validate:
   - `kb:validate`
4. Build agent export:
   - `kb:export`

## Repo structure
- `legacy/` — raw, mixed-language input + generated inventory/map (do not hand-edit)
- `content/` — canonical **English** Markdown (hand-editable after conversion)
- `assets/` — normalized images/attachments referenced by Markdown
- `build/` — generated intermediates, reports, and exports (do not hand-edit)
- `scripts/` — pipeline helpers (conversion, validation, export)
- `.claude/commands/` — Claude Code custom commands (kb:convert, kb:validate, kb:export)

## Conventions
- URLs follow: `/help/<product-area>/<slug>`
- FAQs are stored separately under `content/faq/`
- Screenshots may be Slovak temporarily (you plan to redo them later).
  - Conversion will **not** block on Slovak screenshots.
  - Conversion will flag pages likely needing screenshot replacement.

See `claude.md` for the full conversion contract.
