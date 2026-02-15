#!/usr/bin/env python3
"""Validate the knowledge base in content/ and write a report."""

import os
import re
import yaml
from collections import defaultdict
from pathlib import Path

CONTENT_DIR = Path("/Users/michaldodok/help/content")
REPO_ROOT = Path("/Users/michaldodok/help")

REQUIRED_FM = [
    "title", "slug", "type", "product_area", "audience",
    "status", "source_language", "needs_screenshot_replacement", "last_converted"
]


def parse_frontmatter(text):
    """Parse YAML frontmatter from markdown text."""
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
    if not m:
        return None, text
    try:
        fm = yaml.safe_load(m.group(1))
        body = text[m.end():]
        return fm if isinstance(fm, dict) else None, body
    except Exception:
        return None, text


def main():
    # Collect all md files (skip _shared)
    md_files = sorted([p for p in CONTENT_DIR.rglob("*.md") if "/_shared/" not in str(p)])

    results = {
        "total": len(md_files),
        "no_frontmatter": [],
        "missing_fm": [],
        "duplicate_slugs": [],
        "duplicate_intercom": [],
        "h1_issues": [],
        "heading_skips": [],
        "broken_links": [],
        "missing_assets": [],
    }

    slug_map = defaultdict(list)
    intercom_map = defaultdict(list)

    for fpath in md_files:
        rel = str(fpath.relative_to(REPO_ROOT))
        text = fpath.read_text(encoding="utf-8", errors="replace")

        # 1. Frontmatter check
        fm, body = parse_frontmatter(text)
        if fm is None:
            results["no_frontmatter"].append(rel)
        else:
            missing = [f for f in REQUIRED_FM if f not in fm]
            if missing:
                results["missing_fm"].append((rel, missing))

            if "slug" in fm:
                slug_map[fm["slug"]].append(rel)
            if "intercom_id" in fm and fm["intercom_id"] is not None:
                intercom_map[fm["intercom_id"]].append(rel)

        # 4. H1 count
        h1_lines = [l for l in body.split("\n") if re.match(r'^# [^#]', l)]
        if len(h1_lines) != 1:
            results["h1_issues"].append((rel, len(h1_lines)))

        # 5. Heading level skips
        headings = []
        for line in body.split("\n"):
            m2 = re.match(r'^(#{1,6})\s', line)
            if m2:
                headings.append(len(m2.group(1)))
        for i in range(1, len(headings)):
            if headings[i] > headings[i - 1] + 1:
                results["heading_skips"].append(
                    (rel, f"Jump from H{headings[i-1]} to H{headings[i]}")
                )
                break

        # 6. Internal .md links
        for m3 in re.finditer(r'\[([^\]]*)\]\(([^)]+\.md(?:#[^)]*)?)\)', text):
            link_target = m3.group(2).split("#")[0]
            if link_target.startswith("http"):
                continue
            resolved = (fpath.parent / link_target).resolve()
            if not resolved.exists():
                results["broken_links"].append((rel, link_target))

        # 7. Asset references
        for m4 in re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)', text):
            asset_path = m4.group(2)
            if asset_path.startswith("http"):
                continue
            resolved = (fpath.parent / asset_path).resolve()
            if not resolved.exists():
                results["missing_assets"].append((rel, asset_path))

    # 2. Duplicate slugs
    for slug, files in slug_map.items():
        if len(files) > 1:
            results["duplicate_slugs"].append((slug, files))

    # 3. Duplicate intercom_ids
    for iid, files in intercom_map.items():
        if len(files) > 1:
            results["duplicate_intercom"].append((iid, files))

    # Build report
    lines = []
    lines.append("# Validation Report")
    lines.append("")
    lines.append("**Generated:** 2026-02-15")
    lines.append("")

    fail_count = (
        len(results["no_frontmatter"])
        + len(results["missing_fm"])
        + len(results["duplicate_slugs"])
        + len(results["duplicate_intercom"])
        + len(results["h1_issues"])
        + len(results["heading_skips"])
        + len(results["broken_links"])
        + len(results["missing_assets"])
    )

    overall = "PASS" if fail_count == 0 else "FAIL"

    lines.append("## Summary")
    lines.append("")
    lines.append(f"- **Total docs checked:** {results['total']}")
    lines.append(f"- **Total issues found:** {fail_count}")
    lines.append(f"- **Overall status:** {overall}")
    lines.append("")

    # Section 1: Frontmatter
    lines.append("## 1. Required Frontmatter")
    lines.append("")
    if results["no_frontmatter"] or results["missing_fm"]:
        if results["no_frontmatter"]:
            lines.append(
                f"### Docs with no frontmatter ({len(results['no_frontmatter'])})"
            )
            lines.append("")
            for f in results["no_frontmatter"]:
                lines.append(f"- `{f}`")
            lines.append("")
        if results["missing_fm"]:
            lines.append(
                f"### Docs with missing frontmatter fields ({len(results['missing_fm'])})"
            )
            lines.append("")
            for f, fields in results["missing_fm"]:
                lines.append(f"- `{f}` — missing: {', '.join(fields)}")
            lines.append("")
    else:
        lines.append("All docs have complete required frontmatter.")
        lines.append("")

    # Section 2: Unique slugs
    lines.append("## 2. Unique Slugs")
    lines.append("")
    if results["duplicate_slugs"]:
        lines.append(f"**{len(results['duplicate_slugs'])} duplicate slug(s) found:**")
        lines.append("")
        for slug, files in results["duplicate_slugs"]:
            lines.append(f"- Slug `{slug}` used by:")
            for f in files:
                lines.append(f"  - `{f}`")
        lines.append("")
    else:
        lines.append("All slugs are unique.")
        lines.append("")

    # Section 3: Unique intercom_id
    lines.append("## 3. Unique Intercom IDs")
    lines.append("")
    if results["duplicate_intercom"]:
        lines.append(
            f"**{len(results['duplicate_intercom'])} duplicate intercom_id(s) found:**"
        )
        lines.append("")
        for iid, files in results["duplicate_intercom"]:
            lines.append(f"- intercom_id `{iid}` used by:")
            for f in files:
                lines.append(f"  - `{f}`")
        lines.append("")
    else:
        lines.append("All intercom_id values are unique.")
        lines.append("")

    # Section 4: H1 count
    lines.append("## 4. Exactly One H1 Per Doc")
    lines.append("")
    if results["h1_issues"]:
        lines.append(
            f"**{len(results['h1_issues'])} doc(s) with incorrect H1 count:**"
        )
        lines.append("")
        for f, count in results["h1_issues"]:
            lines.append(f"- `{f}` — found {count} H1 heading(s)")
        lines.append("")
    else:
        lines.append("All docs have exactly one H1.")
        lines.append("")

    # Section 5: Heading skips
    lines.append("## 5. No Skipped Heading Levels")
    lines.append("")
    if results["heading_skips"]:
        lines.append(
            f"**{len(results['heading_skips'])} doc(s) with heading level skips:**"
        )
        lines.append("")
        for f, detail in results["heading_skips"]:
            lines.append(f"- `{f}` — {detail}")
        lines.append("")
    else:
        lines.append("No heading level skips found.")
        lines.append("")

    # Section 6: Broken internal links
    lines.append("## 6. Broken Internal Links")
    lines.append("")
    if results["broken_links"]:
        lines.append(
            f"**{len(results['broken_links'])} broken internal link(s) found:**"
        )
        lines.append("")
        for f, link in results["broken_links"]:
            lines.append(f"- `{f}` — link to `{link}`")
        lines.append("")
    else:
        lines.append("No broken internal links found.")
        lines.append("")

    # Section 7: Missing assets
    lines.append("## 7. Missing Referenced Assets")
    lines.append("")
    if results["missing_assets"]:
        lines.append(f"**{len(results['missing_assets'])} missing asset(s) found:**")
        lines.append("")
        for f, asset in results["missing_assets"]:
            lines.append(f"- `{f}` — references `{asset}`")
        lines.append("")
    else:
        lines.append("All referenced assets exist.")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"**Overall: {overall}**")

    report = "\n".join(lines)

    report_path = Path("/Users/michaldodok/help/build/reports/validation-report.md")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report, encoding="utf-8")
    print(report)
    print("\n\n--- REPORT WRITTEN ---")


if __name__ == "__main__":
    main()
