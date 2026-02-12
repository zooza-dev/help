#!/usr/bin/env python3
"""Deploy agent-ready content into Intercom Fin Content Library.

Uses the Intercom AI Content APIs to push external pages for Fin AI agent.
Falls back gracefully if AI Content APIs are not available.

Env vars:
  INTERCOM_ACCESS_TOKEN                   — required
  INTERCOM_API_BASE_URL                   — default https://api.intercom.io
  INTERCOM_FIN_CONTENT_IMPORT_SOURCE_ID   — optional; created if missing
  INTERCOM_FIN_DEFAULT_AUDIENCE           — optional; e.g. "all"

Usage:
  python scripts/deploy/intercom_fin_content.py [--dry-run] [--limit N]
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
AGENT_EXPORT_DIR = ROOT_DIR / "build" / "exports" / "agent"
MAP_FILE = ROOT_DIR / "build" / "exports" / "targets" / "intercom" / "fin-content-map.json"

API_VERSION = "2.11"
MAX_RETRIES = 3
RETRY_BACKOFF = 2


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

    def _request(self, method: str, path: str, **kwargs) -> dict | None:
        url = f"{self.base_url}{path}"
        backoff = RETRY_BACKOFF
        for attempt in range(MAX_RETRIES + 1):
            resp = self.session.request(method, url, **kwargs)
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
            if resp.status_code == 404:
                return None
            resp.raise_for_status()
            if resp.status_code == 204:
                return {}
            return resp.json()
        resp.raise_for_status()
        return {}

    def get(self, path, **kwargs):
        return self._request("GET", path, **kwargs)

    def post(self, path, **kwargs):
        return self._request("POST", path, **kwargs)

    def put(self, path, **kwargs):
        return self._request("PUT", path, **kwargs)

    def delete(self, path, **kwargs):
        return self._request("DELETE", path, **kwargs)


def load_map() -> dict:
    if MAP_FILE.exists():
        return json.loads(MAP_FILE.read_text(encoding="utf-8"))
    return {"content_import_source_id": None, "external_pages": {}}


def save_map(mapping: dict):
    MAP_FILE.parent.mkdir(parents=True, exist_ok=True)
    MAP_FILE.write_text(json.dumps(mapping, indent=2, ensure_ascii=False), encoding="utf-8")


def load_jsonl(path: Path) -> list[dict]:
    records = []
    if path.exists():
        for line in path.read_text(encoding="utf-8").strip().splitlines():
            if line.strip():
                records.append(json.loads(line))
    return records


def ensure_content_import_source(client: IntercomClient, mapping: dict,
                                  dry_run: bool) -> str | None:
    """Ensure a Content Import Source exists for this repo."""
    # Check env override
    source_id = os.environ.get("INTERCOM_FIN_CONTENT_IMPORT_SOURCE_ID")
    if source_id:
        mapping["content_import_source_id"] = source_id
        return source_id

    if mapping.get("content_import_source_id"):
        return mapping["content_import_source_id"]

    if dry_run:
        logger.info("[DRY-RUN] Would create Content Import Source 'zooza-help-kb'")
        return None

    # Try to create
    try:
        resp = client.post("/ai/content_import_sources", json={
            "name": "zooza-help-kb",
            "url": "https://help.zooza.com",
        })
        if resp and "id" in resp:
            source_id = resp["id"]
            mapping["content_import_source_id"] = source_id
            logger.info("Created Content Import Source -> %s", source_id)
            return source_id
    except Exception as e:
        logger.warning(
            "Could not create Content Import Source: %s. "
            "AI Content APIs may not be available. "
            "Fallback: deploy Help Center articles instead — Fin indexes those automatically.",
            e,
        )
        return None


def sync_external_page(client: IntercomClient, source_id: str | None,
                       record: dict, mapping: dict,
                       default_audience: str, dry_run: bool):
    """Create or update an External Page in Fin Content Library."""
    external_id = f"{record['doc_id']}:{record.get('heading_path', '')}"
    # Sanitize for use as ID
    external_id = re.sub(r"[^a-zA-Z0-9_:-]", "_", external_id)[:200]

    title_parts = [record["title"]]
    hp = record.get("heading_path", "")
    if hp and hp != "(intro)":
        title_parts.append(hp)
    title = " — ".join(title_parts)

    payload = {
        "title": title,
        "body": record["text"],
        "url": f"https://help.zooza.com{record['url']}",
        "external_id": external_id,
        "locale": "en",
    }
    if source_id:
        payload["source_id"] = source_id

    if external_id in mapping["external_pages"]:
        page_id = mapping["external_pages"][external_id]
        if dry_run:
            logger.info("[DRY-RUN] Would update external page '%s' (id=%s)", title[:60], page_id)
            return
        try:
            client.put(f"/ai/content/external_pages/{page_id}", json=payload)
            logger.info("Updated external page '%s'", title[:60])
        except Exception as e:
            logger.warning("Failed to update page %s: %s", page_id, e)
    else:
        if dry_run:
            logger.info("[DRY-RUN] Would create external page '%s'", title[:60])
            return
        try:
            resp = client.post("/ai/content/external_pages", json=payload)
            if resp and "id" in resp:
                mapping["external_pages"][external_id] = resp["id"]
                logger.info("Created external page '%s' -> %s", title[:60], resp["id"])
        except Exception as e:
            logger.warning("Failed to create page '%s': %s", title[:60], e)


def main():
    parser = argparse.ArgumentParser(description="Deploy to Intercom Fin Content Library")
    parser.add_argument("--dry-run", action="store_true", help="Log actions without making API calls")
    parser.add_argument("--limit", type=int, default=0, help="Max records to process (0=all)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    token = os.environ.get("INTERCOM_ACCESS_TOKEN")
    if not token:
        logger.error("INTERCOM_ACCESS_TOKEN not set")
        sys.exit(1)

    base_url = os.environ.get("INTERCOM_API_BASE_URL", "https://api.intercom.io")
    default_audience = os.environ.get("INTERCOM_FIN_DEFAULT_AUDIENCE", "all")

    client = IntercomClient(token, base_url)
    mapping = load_map()

    source_id = ensure_content_import_source(client, mapping, args.dry_run)

    if source_id is None and not args.dry_run:
        logger.warning(
            "No Content Import Source available. "
            "Fin can still use Help Center articles directly. "
            "Deploy via intercom_help_center.py instead."
        )
        sys.exit(0)

    # Load JSONL records
    canonical = load_jsonl(AGENT_EXPORT_DIR / "canonical.jsonl")
    faq = load_jsonl(AGENT_EXPORT_DIR / "faq.jsonl")
    all_records = canonical + faq

    if args.limit:
        all_records = all_records[:args.limit]

    logger.info("Processing %d records (dry_run=%s)", len(all_records), args.dry_run)

    for record in all_records:
        sync_external_page(client, source_id, record, mapping, default_audience, args.dry_run)

    if not args.dry_run:
        save_map(mapping)
        logger.info("Mapping saved to %s", MAP_FILE)

    logger.info("Done. Processed %d records.", len(all_records))


if __name__ == "__main__":
    main()
