# kb:export

Generate all exports from canonical Markdown in `content/`.

## How to run

```bash
pip install pyyaml markdown jinja2
python scripts/export/export_all.py
```

## Outputs

### Agent exports (`build/exports/agent/`)
- `canonical.jsonl` — all non-FAQ content chunked by H2/H3
- `faq.jsonl` — FAQ content from `content/faq/`

### Web export (`build/exports/web/`)
- Static HTML site with index and per-article pages
- Assets copied from `assets/`

## Rules
- Chunk by headings (H2/H3).
- Include metadata: `doc_id` (slug), title, url, type, product_area, sub_area, tags, audience, status, heading_path, source_path.
- Max chunk size ~1600 chars with ~150 char overlap.
- Web pages at `/help/<product-area>/<slug>/`.
- Internal `.md` links rewritten to HTML equivalents in web export.
