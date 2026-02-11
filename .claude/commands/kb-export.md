# kb:export

Generate model-agnostic agent exports from canonical Markdown in `content/`.

## Outputs
- `build/exports/agent/canonical.jsonl`
- `build/exports/agent/faq.jsonl`

## Rules
- Chunk by headings (H2/H3).
- Include metadata: `doc_id` (use slug), title, url, type, product_area, tags, audience, heading_path.
- Enforce max chunk size and add small overlap.
