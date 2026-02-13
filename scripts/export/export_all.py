#!/usr/bin/env python3
"""Run all export pipelines: web site + agent JSONL + Intercom map.

Usage:
    python scripts/export/export_all.py
"""

import json
import logging
import re
import sys
from pathlib import Path

import yaml

# Ensure project root is importable
sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_agent_exports import build_agent_exports
from build_web import build_web

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
CONTENT_DIR = ROOT_DIR / "content"
MAP_FILE = ROOT_DIR / "build" / "exports" / "targets" / "intercom" / "intercom-map.json"


def build_intercom_map():
    """Generate intercom-map.json from frontmatter intercom_id values.

    This map is committed to the repo so the deploy script can find
    existing articles without relying on ephemeral CI state.
    """
    logger = logging.getLogger(__name__)
    mapping = {"collections": {}, "sections": {}, "articles": {}}

    for md_path in sorted(CONTENT_DIR.rglob("*.md")):
        if "/_shared/" in str(md_path) or md_path.name.startswith("_"):
            continue
        text = md_path.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        if not m:
            continue
        fm = yaml.safe_load(m.group(1)) or {}
        slug = fm.get("slug")
        intercom_id = fm.get("intercom_id")
        if slug and intercom_id:
            mapping["articles"][slug] = intercom_id

    MAP_FILE.parent.mkdir(parents=True, exist_ok=True)
    MAP_FILE.write_text(json.dumps(mapping, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    count = len(mapping["articles"])
    logger.info("Intercom map: %d articles with IDs -> %s", count, MAP_FILE)
    return count


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    logger = logging.getLogger(__name__)

    logger.info("=== Building web export ===")
    web_stats = build_web()
    print(f"Web:   {web_stats['total_docs']} docs, {web_stats['published']} published")

    logger.info("=== Building agent exports ===")
    agent_stats = build_agent_exports()
    print(f"Agent: canonical={agent_stats['canonical_records']}, faq={agent_stats['faq_records']}")

    logger.info("=== Building Intercom map ===")
    map_count = build_intercom_map()
    print(f"Intercom map: {map_count} articles with IDs")

    print("\nAll exports complete.")


if __name__ == "__main__":
    main()
