#!/usr/bin/env python3
"""Run the full KB export pipeline.

Order:
  1. SEO & AI readiness check      (scripts/seo_check.py)
  2. FAQ JSON-LD schema generation  (scripts/generate_faq_schema.py)
  3. Web export                     (scripts/export/build_web.py)
  4. Agent JSONL export             (scripts/export/build_agent_exports.py)

Exits with code 1 if the SEO check finds errors (warnings are non-blocking).
Pass --skip-seo to bypass the SEO check (e.g. during local iteration).

Usage:
    python3 scripts/export/export_all.py
    python3 scripts/export/export_all.py --skip-seo
    python3 scripts/export/export_all.py --strict-seo   # warnings also block
"""

import logging
import subprocess
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
SCRIPTS_DIR = ROOT_DIR / "scripts"

SKIP_SEO = "--skip-seo" in sys.argv
STRICT_SEO = "--strict-seo" in sys.argv

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_agent_exports import build_agent_exports
from build_web import build_web


def run_script(script: Path, extra_args: list[str] = None) -> int:
    """Run a Python script as a subprocess and return its exit code."""
    cmd = [sys.executable, str(script)] + (extra_args or [])
    result = subprocess.run(cmd, cwd=str(ROOT_DIR))
    return result.returncode


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    # ── Step 1: SEO check ────────────────────────────────────────────────────
    if SKIP_SEO:
        print("SEO check: skipped (--skip-seo)")
    else:
        print("\n── Step 1: SEO & AI readiness check ──")
        seo_args = ["--strict"] if STRICT_SEO else []
        rc = run_script(SCRIPTS_DIR / "seo_check.py", seo_args)
        if rc != 0:
            print("\n✗ SEO check failed — fix errors before exporting.")
            print("  Run with --skip-seo to bypass (not recommended for production).")
            sys.exit(1)

    # ── Step 2: FAQ JSON-LD schemas ──────────────────────────────────────────
    print("\n── Step 2: FAQ JSON-LD schema generation ──")
    rc = run_script(SCRIPTS_DIR / "generate_faq_schema.py")
    if rc != 0:
        print("✗ FAQ schema generation failed.")
        sys.exit(1)

    # ── Step 3: Web export ───────────────────────────────────────────────────
    print("\n── Step 3: Web export ──")
    web_stats = build_web()
    print(f"  Web: {web_stats['total_docs']} docs, {web_stats['published']} published")

    # ── Step 4: Agent JSONL export ───────────────────────────────────────────
    print("\n── Step 4: Agent JSONL export ──")
    agent_stats = build_agent_exports()
    print(f"  Agent: canonical={agent_stats['canonical_records']}, faq={agent_stats['faq_records']}")

    print("\n✓ All exports complete.")


if __name__ == "__main__":
    main()
