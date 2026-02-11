# Deploying to Intercom

Two deployment targets are supported:

1. **Help Center** — publishes articles visible to customers
2. **Fin Content Library** — feeds content to the Fin AI agent

Both are manual-only (workflow_dispatch). Deployments are idempotent: reruns update existing items, not create duplicates.

## Secrets

Configure these in **Settings → Secrets and variables → Actions**:

| Secret | Required | Description |
|--------|----------|-------------|
| `INTERCOM_ACCESS_TOKEN` | Yes | Intercom API token with Help Center + AI Content permissions |
| `INTERCOM_API_BASE_URL` | No | Default: `https://api.intercom.io`. Set for regional APIs (EU/AU) |
| `INTERCOM_HELP_CENTER_ID` | No | Only needed for multi-Help Center workspaces |
| `INTERCOM_FIN_CONTENT_IMPORT_SOURCE_ID` | No | Auto-created if missing; set to reuse an existing source |
| `INTERCOM_FIN_DEFAULT_AUDIENCE` | No | Default: `all` |

### Getting an API token

1. Go to **Intercom → Settings → Integrations → Developer Hub**
2. Create or select an app
3. Generate an access token with these scopes:
   - `Read and write help center content`
   - `Read and write AI content` (for Fin)

## Recommended first run

1. Go to **Actions → Deploy to Intercom**
2. Click **Run workflow** with:
   - `dry_run`: **true**
   - `limit`: **5**
   - `deploy_help_center`: true
   - `deploy_fin`: true
3. Review the logs — no API writes are made
4. Run again with `dry_run: false` and `limit: 5` to test with real data
5. Once confident, run with `limit: 0` (all articles)

## Running locally

```bash
pip install pyyaml markdown jinja2 requests

# First, generate exports
python scripts/export/export_all.py

# Help Center (dry run)
INTERCOM_ACCESS_TOKEN=your-token python scripts/deploy/intercom_help_center.py --dry-run --limit 5

# Fin Content Library (dry run)
INTERCOM_ACCESS_TOKEN=your-token python scripts/deploy/intercom_fin_content.py --dry-run --limit 5
```

## How it works

### Help Center deploy

1. Reads all `content/**/*.md` files
2. For each unique `product_area`, ensures an Intercom collection exists
3. For each doc type within a collection, ensures a section exists
4. Creates or updates articles using the slug as a stable identifier
5. Saves Intercom IDs to `build/exports/targets/intercom/intercom-map.json`

### Fin Content Library deploy

1. Reads `build/exports/agent/canonical.jsonl` and `faq.jsonl`
2. Ensures a Content Import Source exists (or uses the one from env)
3. Creates or updates External Pages using `doc_id:heading_path` as external_id
4. Saves Intercom IDs to `build/exports/targets/intercom/fin-content-map.json`

**Fallback**: If the AI Content APIs are not available in your workspace, Fin automatically indexes Help Center articles. Deploying to Help Center alone is sufficient.

## Mapping files

The deploy scripts store remote IDs locally so reruns can update rather than duplicate:

- `build/exports/targets/intercom/intercom-map.json` — Help Center IDs
- `build/exports/targets/intercom/fin-content-map.json` — Fin Content IDs

These files should be committed to the repo or stored as workflow artifacts for persistence across runs.
