# Exports

The export pipeline generates two outputs from `content/` Markdown files.

## Web export (`build/exports/web/`)

A minimal static HTML site with:

- **Index page** at `/help/index.html` — navigation grouped by product area and doc type
- **Article pages** at `/help/<product-area>/<slug>/index.html`
- **Assets** copied to `/help/assets/`
- Internal `.md` links rewritten to HTML equivalents

### Build locally

```bash
pip install pyyaml markdown jinja2
python scripts/export/build_web.py
```

Output lands in `build/exports/web/`. Open `build/exports/web/help/index.html` in a browser.

## Agent export (`build/exports/agent/`)

Model-agnostic JSONL files for RAG / AI agent ingestion:

- **`canonical.jsonl`** — all non-FAQ content, chunked by H2/H3 headings
- **`faq.jsonl`** — FAQ content from `content/faq/`

Each record contains:

| Field | Description |
|-------|-------------|
| `doc_id` | Slug (unique identifier) |
| `title` | Document title |
| `url` | Canonical URL `/help/<area>/<slug>` |
| `type` | guides, setup, payments, troubleshooting, faq |
| `product_area` | From taxonomy |
| `sub_area` | Optional (e.g., Email, WhatsApp) |
| `tags` | List of tags |
| `audience` | Target audience(s) |
| `status` | published, draft, archived |
| `heading_path` | Section heading breadcrumb |
| `source_path` | Source file path in repo |
| `text` | Chunk text (~1600 chars max, ~150 overlap) |
| `chunk_index` | Present when a section is split into multiple chunks |

### Build locally

```bash
pip install pyyaml
python scripts/export/build_agent_exports.py
```

### Ingesting into other RAG systems

The JSONL files are designed to be portable:

1. **OpenAI Assistants / GPTs** — upload `canonical.jsonl` as a file for retrieval
2. **Pinecone / Weaviate / Qdrant** — index each record; use metadata fields for filtering
3. **LangChain / LlamaIndex** — load with a JSONL document loader
4. **Custom pipelines** — parse line-by-line with `json.loads()`

## Run all exports

```bash
pip install pyyaml markdown jinja2
python scripts/export/export_all.py
```

## GitHub Actions

Trigger the **Export docs** workflow manually from the Actions tab. It produces a downloadable artifact with all exports.
