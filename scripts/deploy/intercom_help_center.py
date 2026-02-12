#!/usr/bin/env python3
"""Deploy content to Intercom Help Center.

Syncs content/ articles into Intercom Help Center collections/sections/articles.
Uses stable external IDs (slug) so reruns are idempotent (update, not duplicate).

Adds CDN asset rewriting:
- Upload assets separately (your GH Action FTP step)
- Rewrite <img src="..."> and <a href="..."> pointing at local assets to absolute CDN URLs

Env vars:
  INTERCOM_ACCESS_TOKEN       — required
  INTERCOM_API_BASE_URL       — default https://api.intercom.io
  INTERCOM_HELP_CENTER_ID     — optional (for multi-center workspaces) [not used here]
  INTERCOM_API_VERSION        — optional (default: 2.9)
  KB_CDN_BASE_URL             — optional (default: https://cdn.zooza.sk/assets/kb)

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
from urllib.parse import urlparse

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

# Your CDN base (must NOT end with slash). Example:
#   https://cdn.zooza.sk/assets/kb
KB_CDN_BASE_URL = os.environ.get("KB_CDN_BASE_URL", "https://cdn.zooza.sk/assets/kb").rstrip("/")

MAX_RETRIES = 3
RETRY_BACKOFF = 2  # seconds, doubled each retry


class IntercomClient:
    """Thin wrapper around Intercom REST API with retry logic."""

    def __init__(self, token: str, base_url: str = "https://api.intercom.io"):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Intercom-Version": API_VERSION,
            }
        )
        self._cached_author_id: int | None = None

    def _request(self, method: str, path: str, **kwargs) -> dict:
        url = f"{self.base_url}{path}"
        backoff = RETRY_BACKOFF
        last_resp = None

        for attempt in range(MAX_RETRIES + 1):
            resp = self.session.request(method, url, **kwargs)
            last_resp = resp

            if resp.status_code == 429:
                wait = backoff * (2**attempt)
                logger.warning("Rate limited, waiting %ds (attempt %d)", wait, attempt + 1)
                time.sleep(wait)
                continue

            if resp.status_code >= 500:
                wait = backoff * (2**attempt)
                logger.warning("Server error %d, retrying in %ds", resp.status_code, wait)
                time.sleep(wait)
                continue

            if resp.status_code >= 400:
                # Helpful error logging before raising
                try:
                    logger.error(
                        "Intercom API error %s %s -> %s: %s",
                        method,
                        path,
                        resp.status_code,
                        resp.text,
                    )
                except Exception:
                    pass

            resp.raise_for_status()

            if resp.status_code == 204:
                return {}
            return resp.json()

        if last_resp is not None:
            last_resp.raise_for_status()
        return {}

    def get(self, path, **kwargs):
        return self._request("GET", path, **kwargs)

    def post(self, path, **kwargs):
        return self._request("POST", path, **kwargs)

    def put(self, path, **kwargs):
        return self._request("PUT", path, **kwargs)

    def get_default_author_id(self) -> int:
        """
        Articles require author_id (must be a teammate/admin in the workspace).
        Prefer /me, fallback to /admins.
        """
        if self._cached_author_id is not None:
            return self._cached_author_id

        me = self.get("/me")
        me_id = me.get("id")
        if me_id is not None:
            self._cached_author_id = int(me_id)
            return self._cached_author_id

        admins = self.get("/admins")
        data = admins.get("data") or []
        if not data:
            raise RuntimeError(
                "Could not determine author_id: /me had no id and /admins returned no admins."
            )

        self._cached_author_id = int(data[0]["id"])
        return self._cached_author_id


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return {}, text
    return yaml.safe_load(m.group(1)) or {}, text[m.end() :]


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
        docs.append(
            {
                "slug": slug,
                "title": fm.get("title", slug),
                "type": fm.get("type", "guides"),
                "product_area": fm.get("product_area", ""),
                "sub_area": fm.get("sub_area", ""),
                "status": fm.get("status", "published"),
                "tags": fm.get("tags", []),
                "html_body": md_to_html_simple(body),
                "source_path": str(md_path),
                "intercom_id": fm.get("intercom_id"),
                "intercom_sync": fm.get("intercom_sync", True),
            }
        )
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


def ensure_section(
    client: IntercomClient,
    name: str,
    collection_id: str | None,
    mapping: dict,
    dry_run: bool,
) -> str | None:
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

    resp = client.post(
        "/help_center/sections",
        json={
            "name": name,
            "parent_id": collection_id,
        },
    )
    sid = resp["id"]
    mapping["sections"][key] = sid
    logger.info("Created section '%s' -> %s", name, sid)
    return sid


# ---------- CDN rewrite helpers ----------

def _is_absolute_url(u: str) -> bool:
    try:
        p = urlparse(u)
        return p.scheme in ("http", "https") and bool(p.netloc)
    except Exception:
        return False


def _strip_known_prefixes(u: str) -> str:
    """Normalize a local asset URL to a relative path under assets/.

    Inputs we see in practice:
      ../../assets/images/x.png
      ../assets/images/x.png
      /assets/images/x.png
      assets/images/x.png
      ./assets/images/x.png
    Output:
      images/x.png
    """
    u = u.strip()

    # drop query/hash (we generally don't need them for cdn objects; keep if you want)
    base, _, frag = u.partition("#")
    base, _, query = base.partition("?")
    u = base

    u = u.replace("\\", "/")

    # remove leading ./ or ../ segments
    u = re.sub(r"^(\./)+", "", u)
    u = re.sub(r"^(\.\./)+", "", u)

    # remove leading slash
    u = u.lstrip("/")

    # if it contains assets/ somewhere, keep from there
    m = re.search(r"(?:^|/)(assets/)(.*)$", u)
    if m:
        rest = m.group(2)  # path inside assets/
        return rest.lstrip("/")

    # if it doesn't mention assets/ but is still relative, leave as-is
    return u.lstrip("/")


def rewrite_assets_to_cdn(html: str, cdn_base_url: str) -> tuple[str, list[str]]:
    """Rewrite local asset references in HTML to absolute CDN URLs.

    Rewrites:
      <img src="...">  -> cdn_base_url/<relative_under_assets>
      <a href="...">   -> same (for links to images/pdf/etc)

    Returns (rewritten_html, warnings)
    """
    warnings: list[str] = []

    # src/href attributes, double or single quotes
    attr_re = re.compile(r"""(?P<attr>\b(?:src|href)\s*=\s*)(?P<q>['"])(?P<val>[^'"]+)(?P=q)""", re.IGNORECASE)

    def repl(m: re.Match) -> str:
        attr = m.group("attr")
        q = m.group("q")
        val = m.group("val").strip()

        # Leave absolute URLs, mailto, tel, anchors, data URIs
        low = val.lower()
        if (
            _is_absolute_url(val)
            or low.startswith("mailto:")
            or low.startswith("tel:")
            or low.startswith("data:")
            or low.startswith("#")
        ):
            return f"{attr}{q}{val}{q}"

        # Only rewrite things that look like they are assets references
        # (assets/... or contains /assets/ or relative with ../assets)
        if "assets/" not in val.replace("\\", "/"):
            return f"{attr}{q}{val}{q}"

        rel = _strip_known_prefixes(val)
        new_url = f"{cdn_base_url}/{rel}"

        return f"{attr}{q}{new_url}{q}"

    rewritten = attr_re.sub(repl, html)

    # warn if any remaining <img src> is not absolute (common Intercom rejection)
    img_src_re = re.compile(r"""<img\b[^>]*\bsrc\s*=\s*['"]([^'"]+)['"]""", re.IGNORECASE)
    for src in img_src_re.findall(rewritten):
        if not (_is_absolute_url(src) or src.lower().startswith("data:")):
            warnings.append(f"Non-absolute <img src> remains: {src}")

    return rewritten, warnings


def sync_article(
    client: IntercomClient,
    doc: dict,
    section_id: str | None,
    mapping: dict,
    dry_run: bool,
    author_id: int | None,
):
    """Create or update a Help Center article."""
    slug = doc["slug"]
    state = "published" if doc["status"] == "published" else "draft"

    # Rewrite assets in HTML body to CDN URLs
    body_html = doc["html_body"]
    body_html, warnings = rewrite_assets_to_cdn(body_html, KB_CDN_BASE_URL)
    for w in warnings:
        logger.warning("Doc %s (%s): %s", slug, doc.get("source_path", "?"), w)

    payload = {
        "title": doc["title"],
        "body": body_html,
        "state": state,
    }

    if author_id is not None:
        payload["author_id"] = int(author_id)

    if section_id:
        payload["parent_id"] = section_id
        payload["parent_type"] = "section"

    article_id = doc.get("intercom_id") or mapping["articles"].get(slug)

    if article_id:
        if dry_run:
            logger.info("[DRY-RUN] Would update article '%s' (id=%s)", doc["title"], article_id)
            return
        client.put(f"/articles/{article_id}", json=payload)
        mapping["articles"][slug] = article_id
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
        docs = docs[: args.limit]

    logger.info(
        "Processing %d docs (dry_run=%s, Intercom-Version=%s, KB_CDN_BASE_URL=%s)",
        len(docs),
        args.dry_run,
        API_VERSION,
        KB_CDN_BASE_URL,
    )

    author_id = None
    if not args.dry_run:
        author_id = client.get_default_author_id()
        logger.info("Using author_id=%s", author_id)

    skipped = 0
    synced = 0
    for doc in docs:
        # Skip articles that have an Intercom ID and are not flagged for sync
        if doc.get("intercom_id") and not doc.get("intercom_sync", True):
            logger.info("Skipping '%s' (id=%s, intercom_sync=false)", doc["title"], doc["intercom_id"])
            skipped += 1
            continue

        area = doc["product_area"] or "General"
        collection_id = ensure_collection(client, area, mapping, args.dry_run)

        section_id = None
        if doc["type"]:
            section_id = ensure_section(client, doc["type"].capitalize(), collection_id, mapping, args.dry_run)

        sync_article(client, doc, section_id, mapping, args.dry_run, author_id)
        synced += 1

    if not args.dry_run:
        save_map(mapping)
        logger.info("Mapping saved to %s", MAP_FILE)

    logger.info("Done. Synced %d articles, skipped %d (intercom_sync=false).", synced, skipped)


if __name__ == "__main__":
    main()
