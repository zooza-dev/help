#!/usr/bin/env python3
"""
SEO & AI readiness check for the Zooza Help KB.

Runs before every export. Checks:
  1. Meta description — exists, 50–160 chars
  2. Title length — 10–70 chars
  3. Tags — non-empty
  4. Image alt text — not empty, not generic ("Screenshot" alone)
  5. No Obsidian syntax remaining (![[...]])
  6. FAQ pages have a JSON-LD schema file in static/schema/faq/
  7. AI files — static/llms.txt and static/robots.txt exist

Output: build/reports/seo-report.md
Exit code: 0 if no errors (warnings OK), 1 if any errors.

Usage:
    python3 scripts/seo_check.py
    python3 scripts/seo_check.py --strict   # warnings also fail
"""

import os
import re
import sys
import json
import yaml
from pathlib import Path
from datetime import date

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = REPO_ROOT / "content"
STATIC_DIR = REPO_ROOT / "static"
SCHEMA_DIR = STATIC_DIR / "schema" / "faq"
REPORT_PATH = REPO_ROOT / "build" / "reports" / "seo-report.md"

STRICT = "--strict" in sys.argv

# Alt text patterns that are too generic to be useful
GENERIC_ALT_RE = re.compile(
    r"^(screenshot|image|img|photo|picture|bild|foto|screenshot\s*[-—]\s*)?$",
    re.IGNORECASE,
)
# Min useful alt length (after stripping "Screenshot — " prefix)
ALT_MIN_CHARS = 10

# Description bounds
DESC_MIN = 50
DESC_MAX = 160

# Title bounds
TITLE_MIN = 10
TITLE_MAX = 70

# Obsidian embed syntax
OBSIDIAN_RE = re.compile(r"!\[\[.+?\]\]")

# Inline image: ![alt](path)
IMG_RE = re.compile(r"!\[([^\]]*)\]\([^)]+\)")


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except Exception:
        fm = {}
    return fm if isinstance(fm, dict) else {}, text[m.end():]


def extract_auto_description(body: str) -> str:
    """Mirror of build_docusaurus.py's extract_description."""
    body = re.sub(r"^# .+\n+", "", body.strip())
    for para in body.split("\n\n"):
        para = para.strip()
        if not para or para.startswith("#") or para.startswith("![") or para.startswith("|"):
            continue
        # Strip HTML comments, markdown
        clean = re.sub(r"<!--.*?-->", "", para, flags=re.DOTALL)
        clean = re.sub(r"[*_`]", "", clean)
        clean = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", clean)
        clean = clean.replace("\n", " ").strip()
        if len(clean) > 10:
            return clean[:157] + "..." if len(clean) > 160 else clean
    return ""


def check_alt_text(body: str) -> tuple[list[str], list[str]]:
    """Return (errors, warnings) for images with missing/generic alt text.

    errors:   empty alt text — blocks SEO entirely, must fix
    warnings: generic-only alt ("Screenshot", "Screenshot — short") — should fix
    """
    errors = []
    warnings = []
    for m in IMG_RE.finditer(body):
        alt = m.group(1).strip()
        core = re.sub(r"^screenshot\s*[-—]\s*", "", alt, flags=re.IGNORECASE).strip()
        if not alt:
            errors.append(f"image missing alt text: `{m.group(0)[:60]}`")
        elif GENERIC_ALT_RE.match(core) or len(core) < ALT_MIN_CHARS:
            warnings.append(f"alt text too generic: `{alt}`")
    return errors, warnings


def main():
    errors: list[str] = []
    warnings: list[str] = []

    # Collect published docs
    md_files = sorted([
        p for p in CONTENT_DIR.rglob("*.md")
        if "/_shared/" not in str(p)
    ])

    # Per-doc checks
    doc_issues: dict[str, dict] = {}  # path -> {errors: [], warnings: []}

    for fpath in md_files:
        rel = str(fpath.relative_to(REPO_ROOT))
        text = fpath.read_text(encoding="utf-8", errors="replace")
        fm, body = parse_frontmatter(text)

        if not fm or fm.get("status") in ("draft", "archived"):
            continue

        doc_errors: list[str] = []
        doc_warnings: list[str] = []

        slug = fm.get("slug", "")
        doc_type = fm.get("type", "")

        # 1. Title
        title = fm.get("title", "")
        if not title:
            doc_errors.append("missing title")
        elif len(title) < TITLE_MIN:
            doc_warnings.append(f"title too short ({len(title)} chars, min {TITLE_MIN}): `{title}`")
        elif len(title) > TITLE_MAX:
            doc_warnings.append(f"title too long ({len(title)} chars, max {TITLE_MAX}): `{title[:50]}…`")

        # 2. Description
        desc = fm.get("description", "")
        if not desc:
            desc = extract_auto_description(body)
            if not desc:
                doc_errors.append("no description in frontmatter and could not auto-extract one")
            elif len(desc) < DESC_MIN:
                doc_warnings.append(f"auto-extracted description too short ({len(desc)} chars, min {DESC_MIN})")
            elif len(desc) > DESC_MAX:
                doc_warnings.append(f"auto-extracted description too long ({len(desc)} chars, max {DESC_MAX})")
            else:
                doc_warnings.append(f"description missing from frontmatter (auto-extracted: `{desc[:80]}…`)")
        else:
            if len(desc) < DESC_MIN:
                doc_warnings.append(f"description too short ({len(desc)} chars, min {DESC_MIN})")
            elif len(desc) > DESC_MAX:
                doc_warnings.append(f"description too long ({len(desc)} chars, max {DESC_MAX})")

        # 3. Tags
        tags = fm.get("tags", [])
        if not tags:
            doc_warnings.append("no tags defined")

        # 4. Image alt text
        # Empty alt = always an error (blocks screen readers + SEO entirely).
        # Generic alt ("Screenshot") = warning on all docs; if screenshot replacement
        # is pending, annotate the warning accordingly.
        alt_errors, alt_warnings = check_alt_text(body)
        needs_replace = fm.get("needs_screenshot_replacement", False)
        for e in alt_errors:
            doc_errors.append(e)
        for w in alt_warnings:
            if needs_replace:
                doc_warnings.append(f"{w} (screenshot replacement pending)")
            else:
                doc_warnings.append(w)

        # 5. Obsidian syntax
        obsidian_matches = OBSIDIAN_RE.findall(body)
        if obsidian_matches:
            doc_errors.append(
                f"Obsidian syntax remaining: {obsidian_matches[0]!r}"
                + (f" (+{len(obsidian_matches)-1} more)" if len(obsidian_matches) > 1 else "")
            )

        # 6. FAQ schema
        if doc_type == "faq" and slug:
            schema_file = SCHEMA_DIR / f"{slug}.json"
            if not schema_file.exists():
                doc_errors.append(f"FAQ JSON-LD schema missing: static/schema/faq/{slug}.json")
            else:
                # Validate schema has mainEntity entries
                try:
                    schema = json.loads(schema_file.read_text())
                    entities = schema.get("mainEntity", [])
                    if not entities:
                        doc_warnings.append("FAQ schema has no mainEntity Q&A entries")
                except Exception:
                    doc_errors.append("FAQ schema JSON is invalid")

        if doc_errors or doc_warnings:
            doc_issues[rel] = {"errors": doc_errors, "warnings": doc_warnings}

    # 7. AI / global files
    global_errors: list[str] = []
    global_warnings: list[str] = []

    for ai_file in ["llms.txt", "robots.txt", "sitemap.xml"]:
        p = STATIC_DIR / ai_file
        if not p.exists():
            # sitemap is generated by Docusaurus, so just warn
            if ai_file == "sitemap.xml":
                global_warnings.append(f"static/{ai_file} not found (generated at build time — OK)")
            else:
                global_errors.append(f"static/{ai_file} missing — required for SEO and AI crawlers")

    # ── Write report ──────────────────────────────────────────────────────────

    total_docs = sum(1 for p in CONTENT_DIR.rglob("*.md") if "/_shared/" not in str(p))
    total_errors = sum(len(v["errors"]) for v in doc_issues.values()) + len(global_errors)
    total_warnings = sum(len(v["warnings"]) for v in doc_issues.values()) + len(global_warnings)
    docs_with_errors = sum(1 for v in doc_issues.values() if v["errors"])
    docs_with_warnings = sum(1 for v in doc_issues.values() if v["warnings"] and not v["errors"])

    overall = "PASS" if total_errors == 0 else "FAIL"
    if STRICT and total_warnings > 0:
        overall = "FAIL"

    lines = [
        "# SEO & AI Readiness Report",
        "",
        f"**Generated:** {date.today()}",
        "",
        "## Summary",
        "",
        f"- **Total docs checked:** {total_docs}",
        f"- **Docs with errors:** {docs_with_errors}",
        f"- **Docs with warnings only:** {docs_with_warnings}",
        f"- **Total errors:** {total_errors}",
        f"- **Total warnings:** {total_warnings}",
        f"- **Overall:** {overall}",
        "",
        "## Checks performed",
        "",
        "| Check | Rule |",
        "|---|---|",
        "| Title length | 10–70 chars |",
        "| Meta description | 50–160 chars (frontmatter preferred; auto-extracted as fallback) |",
        "| Tags | At least one tag required |",
        "| Image alt text | Non-empty, non-generic, ≥10 meaningful chars |",
        "| Obsidian syntax | No `![[...]]` remaining |",
        "| FAQ JSON-LD schema | `static/schema/faq/{slug}.json` must exist for type=faq |",
        "| AI files | `static/llms.txt` and `static/robots.txt` must exist |",
        "",
    ]

    if global_errors or global_warnings:
        lines += ["## Global issues", ""]
        for e in global_errors:
            lines.append(f"- **ERROR:** {e}")
        for w in global_warnings:
            lines.append(f"- **WARN:** {w}")
        lines.append("")

    if total_errors == 0 and total_warnings == 0:
        lines += ["## All checks passed", "", "No issues found.", ""]
    else:
        if docs_with_errors > 0:
            lines += ["## Errors (must fix before export)", ""]
            for rel, v in sorted(doc_issues.items()):
                if v["errors"]:
                    lines.append(f"### `{rel}`")
                    for e in v["errors"]:
                        lines.append(f"- **ERROR:** {e}")
                    lines.append("")

        if total_warnings > 0:
            lines += ["## Warnings (recommended fixes)", ""]
            for rel, v in sorted(doc_issues.items()):
                if v["warnings"]:
                    lines.append(f"### `{rel}`")
                    for w in v["warnings"]:
                        lines.append(f"- WARN: {w}")
                    lines.append("")

    lines += [f"---", f"", f"**Overall: {overall}**", ""]

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")

    # ── Console output ────────────────────────────────────────────────────────
    status_icon = "✓" if overall == "PASS" else "✗"
    print(f"SEO check: {status_icon} {overall} — {total_errors} errors, {total_warnings} warnings across {total_docs} docs")
    if total_errors > 0:
        print(f"  Report: {REPORT_PATH}")
    if total_warnings > 0 and total_errors == 0:
        print(f"  Warnings written to: {REPORT_PATH}")

    return 0 if overall == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
