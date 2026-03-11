#!/usr/bin/env python3
"""Run all export pipelines: web site + agent JSONL.

Usage:
    python scripts/export/export_all.py
"""

import logging
import sys
from pathlib import Path

# Ensure project root is importable
sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_agent_exports import build_agent_exports
from build_web import build_web


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    logger = logging.getLogger(__name__)

    logger.info("=== Building web export ===")
    web_stats = build_web()
    print(f"Web:   {web_stats['total_docs']} docs, {web_stats['published']} published")

    logger.info("=== Building agent exports ===")
    agent_stats = build_agent_exports()
    print(f"Agent: canonical={agent_stats['canonical_records']}, faq={agent_stats['faq_records']}")

    print("\nAll exports complete.")


if __name__ == "__main__":
    main()
