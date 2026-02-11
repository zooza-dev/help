#!/usr/bin/env python3
"""Deploy content to Intercom Help Center.

Syncs content/ articles into Intercom Help Center collections/sections/articles.
Uses stable external IDs (slug) so reruns are idempotent (update, not duplicate).

Env vars:
  INTERCOM_ACCESS_TOKEN       — required
  INTERCOM_API_BASE_URL       — default https://api.intercom.io
  INTERCOM_HELP_CENTER_ID     — optional (for multi-center workspaces) [not used here]
  INTERCOM_API_VERSION        — optional (default: 2.9)

Usage:
  python scripts/deploy/intercom_help_center.py [--dry-run] [--limit N]
"""

import argparse
import json
import logging
import os
import re
import sys
import time
from pathlib import Path

import yaml

try:
    import requests
except ImportError:
    print("ERROR: 'requests' package required. Install: pip install requests", file=sys.stderr)
    sys.exit(1)

logger = logging.getLogger(__name__)

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
CONTENT_DIR = ROOT_DIR / "content"
MAP_FILE = ROOT_DIR / "build" / "exports" / "targets" / "intercom" / "intercom-map.json"

# Help Center endpoints accept Intercom-Version values like 2.9 / Unstable.
API_VERSION = os.environ.get("INTERCOM_API_VERSION", "2.9")

MAX_RETRIES = 3
RETRY_BACKOFF = 2  # seconds, doubled each retry


class IntercomClient:
    """Thin wrapper around Intercom REST API with retry logic."""

    def __init__(self, token: str, base_url: str = "https://api.intercom.io"):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Intercom-Version": API_VERSION,
        })

    def _request(self, method: str, path: str, **kwargs) -> dict:
        url = f"{self.base_url}{path}"
        backoff = RETRY_BACKOFF
        last_resp = None

        for attempt in range(MAX_RETRIES + 1):
            resp = self.session.request(method, url, **kwargs)
            last_resp = resp

            if resp.status_code == 429:
                wait = backoff * (2 ** attempt)
                logger.warning("Rate limited, waiting %ds (attempt %d)", wait, attempt + 1)
                time.sleep(wait)
                continue

            if resp.status_code >= 500:
                wait = backoff * (2 ** attempt)
                logger.warning("Server error %d, retrying in %ds", resp.status_code, wait)
                time.sleep(wait)
                continue

            if resp.status_code >= 400:
                # Helpful debug (Intercom usually returns JSON error bodies)
                body = resp.text.strip()
                logger.error("Intercom API error %s %s -> %d: %s", method, path, resp.status_code, body[:2000])

            resp.raise_for_status()
            if resp.status_code == 204:
                return {}
            return resp.json()

        # Should not usually reach here, but keep a useful error if we do.
        if last_resp is not None:
            body = last_resp.text.strip()
            logger.error("Intercom API final failure %s %s -> %d: %s", method, path, last_resp.status_code, body[:2000])
            last_resp.raise_for_status()
        return {}

    def get(self, path, **kwargs):
        return self._request("GET", path, **kwargs)

    def post(self, path, **kwargs):
        return self._request("POST", path, **kwargs)

    def put(self, path, **kwargs):
        return self._request("PUT", path, **kwargs)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return {}, text
    return yaml.safe_load(m.group(1)) or {}, text[m.end():]


def md_to_html_simple(body: str) -> str:
    """Convert Markdown to HTML for Intercom articles."""
    try:
        import markdown as md_lib
        converter = md_lib.Markdown(extensions=["tables", "fenced_code"])
        return converter.convert(body)
    except ImportError:
        logger.warning("'markdown' package not found; uploading raw Markdown")
        return f"<pre>{body}</pre>"


def load_map() -> dict:
    if MAP_FILE.exists():
        return json.loads(MAP_FILE.read_text(encoding="utf-8"))
    return {"collections": {}, "sections": {}, "articles": {}}


def save_map(mapping: dict):
    MAP_FILE.parent.mkdir(parents=True, exist_ok=True)
    MAP_FILE.write_text(json.dumps(mapping, indent=2, ensure_ascii=False), encoding="utf-8")


def collect_docs() -> list[dict]:
    """Read all content/*.md files and return doc metadata + HTML body."""
    docs = []
    for md_path in sorted(CONTENT_DIR.rglob("*.md")):
        if "/_shared/" in str(md_path) or md_path.name.startswith("_"):
            continue
        text = md_path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        slug = fm.get("slug")
        if not slug:
            continue
        docs.append({
            "slug": slug,
            "title": fm.get("title", slug),
            "type": fm.get("type", "guides"),
            "product_area": fm.get("product_area", ""),
            "sub_area": fm.get("sub_area", ""),
            "status": fm.get("status", "published"),
            "tags": fm.get("tags", []),
            "html_body": md_to_html_simple(body),
        })
    return docs


def iter_all_pages(client: IntercomClient, path: str, per_page: int = 50, params: dict | None = None):
    """Cursor pagination for Intercom list endpoints.

    Uses pages.next.starting_after from the response.
    """
    starting_after = None
    params = dict(params or {})

    while True:
        req_params = dict(params)
        req_params["per_page"] = per_page
        if starting_after:
            req_params["starting_after"] = starting_after

        data = client.get(path, params=req_params)
        for item in data.get("data", []):
            yield item

        pages = data.get("pages") or {}
        nxt = pages.get("next") or {}
        next_cursor = nxt.get("starting_after")
        if not next_cursor:
            break
        starting_after = next_cursor
        per_page = int(nxt.get("per_page", per_page))


def ensure_collection(client: IntercomClient, name: str, mapping: dict, dry_run: bool) -> str | None:
    """Ensure a Help Center collection exists. Returns collection ID."""
    if name in mapping["collections"]:
        return mapping["collections"][name]

    if dry_run:
        logger.info("[DRY-RUN] Would create collection: %s", name)
        return None

    data = client.get("/help_center/collections")
    for col in data.get("data", []):
        if col.get("name") == name:
            cid = col["id"]
            mapping["collections"][name] = cid
            logger.info("Found existing collection '%s' -> %s", name, cid)
            return cid

    resp = client.post("/help_center/collections", json={"name": name})
    cid = resp["id"]
    mapping["collections"][name] = cid
    logger.info("Created collection '%s' -> %s", name, cid)
    return cid


def find_section_id(client: IntercomClient, collection_id: str, name: str) -> str | None:
    """Find a section by name under a given collection."""
    for sec in iter_all_pages(client, "/help_center/sections", per_page=50):
        if str(sec.get("parent_id")) == str(collection_id) and sec.get("name") == name:
            return sec.get("id")
    return None


def ensure_section(client: IntercomClient, name: str, collection_id: str | None,
                   mapping: dict, dry_run: bool) -> str | None:
    """Ensure a section exists within a collection. Returns section ID."""
    if not collection_id:
        return None

    key = f"{collection_id}:{name}"
    if key in mapping["sections"]:
        return mapping["sections"][key]

    if dry_run:
        logger.info("[DRY-RUN] Would create section '%s' in collection %s", name, collection_id)
        return None

    existing_id = find_section_id(client, collection_id, name)
    if existing_id:
        mapping["sections"][key] = existing_id
        logger.info("Found existing section '%s' -> %s", name, existing_id)
        return existing_id

    resp = client.post("/help_center/sections", json={
        "name": name,
        "parent_id": collection_id,
    })
    sid = resp["id"]
    mapping["sections"][key] = sid
    logger.info("Created section '%s' -> %s", name, sid)
    return sid


def sync_article(client: IntercomClient, doc: dict, section_id: str | None,
                 mapping: dict, dry_run: bool):
    """Create or update a Help Center article."""
    slug = doc["slug"]
    state = "published" if doc["status"] == "published" else "draft"

    payload = {
        "title": doc["title"],
        "body": doc["html_body"],
        "state": state,
    }
    if section_id:
        payload["parent_id"] = section_id
        payload["parent_type"] = "section"

    if slug in mapping["articles"]:
        article_id = mapping["articles"][slug]
        if dry_run:
            logger.info("[DRY-RUN] Would update article '%s' (id=%s)", doc["title"], article_id)
            return
        client.put(f"/articles/{article_id}", json=payload)
        logger.info("Updated article '%s' (id=%s)", doc["title"], article_id)
    else:
        if dry_run:
            logger.info("[DRY-RUN] Would create article '%s'", doc["title"])
            return
        resp = client.post("/articles", json=payload)
        mapping["articles"][slug] = resp["id"]
        logger.info("Created article '%s' -> %s", doc["title"], resp["id"])


def main():
    parser = argparse.ArgumentParser(description="Deploy to Intercom Help Center")
    parser.add_argument("--dry-run", action="store_true", help="Log actions without making API calls")
    parser.add_argument("--limit", type=int, default=0, help="Max articles to process (0=all)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    token = os.environ.get("INTERCOM_ACCESS_TOKEN")
    if not token:
        logger.error("INTERCOM_ACCESS_TOKEN not set")
        sys.exit(1)

    base_url = os.environ.get("INTERCOM_API_BASE_URL", "https://api.intercom.io")
    client = IntercomClient(token, base_url)
    mapping = load_map()

    docs = collect_docs()
    if args.limit:
        docs = docs[:args.limit]

    logger.info("Processing %d docs (dry_run=%s, Intercom-Version=%s)", len(docs), args.dry_run, API_VERSION)

    for doc in docs:
        area = doc["product_area"] or "General"
        collection_id = ensure_collection(client, area, mapping, args.dry_run)
        section_id = None
        if doc["type"]:
            section_id = ensure_section(client, doc["type"].capitalize(), collection_id, mapping, args.dry_run)
        sync_article(client, doc, section_id, mapping, args.dry_run)

    if not args.dry_run:
        save_map(mapping)
        logger.info("Mapping saved to %s", MAP_FILE)

    logger.info("Done. Processed %d articles.", len(docs))


if __name__ == "__main__":
    main()
