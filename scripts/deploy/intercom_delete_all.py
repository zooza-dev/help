#!/usr/bin/env python3
"""Delete ALL articles from Intercom Help Center.

This is a destructive, one-time cleanup tool.
After running, all articles must be re-deployed from scratch.

Env vars:
  INTERCOM_ACCESS_TOKEN  — required

Usage:
  python scripts/deploy/intercom_delete_all.py [--dry-run] [--yes]
"""

import argparse
import logging
import os
import sys
import time

try:
    import requests
except ImportError:
    print("ERROR: 'requests' package required. Install: pip install requests", file=sys.stderr)
    sys.exit(1)

logger = logging.getLogger(__name__)

API_VERSION = os.environ.get("INTERCOM_API_VERSION", "2.9")


class IntercomClient:
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
        for attempt in range(4):
            resp = self.session.request(method, url, **kwargs)
            if resp.status_code == 429:
                wait = 2 ** (attempt + 1)
                logger.warning("Rate limited, waiting %ds", wait)
                time.sleep(wait)
                continue
            if resp.status_code >= 500:
                wait = 2 ** (attempt + 1)
                logger.warning("Server error %d, retrying in %ds", resp.status_code, wait)
                time.sleep(wait)
                continue
            if resp.status_code == 404:
                return None
            if resp.status_code == 204:
                return {}
            resp.raise_for_status()
            return resp.json()
        resp.raise_for_status()
        return {}

    def get(self, path, **kwargs):
        return self._request("GET", path, **kwargs)

    def delete(self, path, **kwargs):
        return self._request("DELETE", path, **kwargs)


def list_all_articles(client: IntercomClient) -> list[dict]:
    """Fetch all articles using cursor pagination."""
    articles = []
    starting_after = None

    while True:
        params = {"per_page": 50}
        if starting_after:
            params["starting_after"] = starting_after

        data = client.get("/articles", params=params)
        if not data:
            break

        batch = data.get("data", [])
        articles.extend(batch)

        pages = data.get("pages") or {}
        nxt = pages.get("next") or {}
        starting_after = nxt.get("starting_after")
        if not starting_after:
            break

    return articles


def main():
    parser = argparse.ArgumentParser(description="Delete ALL Intercom Help Center articles")
    parser.add_argument("--dry-run", action="store_true", help="List articles without deleting")
    parser.add_argument("--yes", action="store_true", help="Skip confirmation prompt")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    token = os.environ.get("INTERCOM_ACCESS_TOKEN")
    if not token:
        logger.error("INTERCOM_ACCESS_TOKEN not set")
        sys.exit(1)

    base_url = os.environ.get("INTERCOM_API_BASE_URL", "https://api.intercom.io")
    client = IntercomClient(token, base_url)

    logger.info("Fetching all articles...")
    articles = list_all_articles(client)
    logger.info("Found %d articles in Intercom", len(articles))

    if not articles:
        logger.info("Nothing to delete.")
        return

    # Show what will be deleted
    for a in sorted(articles, key=lambda x: x.get("id", 0)):
        logger.info("  [%s] %s", a.get("id"), a.get("title", "(no title)"))

    if args.dry_run:
        logger.info("DRY RUN — no articles deleted. Would delete %d articles.", len(articles))
        return

    if not args.yes:
        confirm = input(f"\nDelete ALL {len(articles)} articles? Type 'DELETE' to confirm: ")
        if confirm.strip() != "DELETE":
            logger.info("Aborted.")
            return

    deleted = 0
    failed = 0
    for a in articles:
        aid = a.get("id")
        title = a.get("title", "(no title)")
        try:
            client.delete(f"/articles/{aid}")
            deleted += 1
            logger.info("Deleted [%s] %s", aid, title)
        except Exception as e:
            failed += 1
            logger.error("Failed to delete [%s] %s: %s", aid, title, e)

    logger.info("Done. Deleted: %d, Failed: %d", deleted, failed)


if __name__ == "__main__":
    main()
