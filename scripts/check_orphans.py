#!/usr/bin/env python3
"""Find published articles that nothing links to.

A new article is invisible unless a hub, an overview or a related article
points at it. Search and the AI assistant both lean on those links, so an
orphan is not merely untidy -- it is a page nobody will be sent to.

Cost of not having this: Google Forms shipped with its own guide on
2026-08-16 and was absent from the integrations hub, and Shared sessions
was absent from the settings hub, because adding an article does not
update the pages that should point at it.

    python3 scripts/check_orphans.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"

# Pages that are meant to be entry points rather than link targets.
ENTRY_POINTS = {"index", "glossary", "terminology-review"}


def frontmatter(text):
    out = {}
    if not text.startswith("---"):
        return out
    for line in text.split("---", 2)[1].splitlines():
        m = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return out


def main():
    docs = {}
    for path in sorted(CONTENT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        fm = frontmatter(text)
        if fm.get("status") != "published":
            continue
        slug = fm.get("slug") or path.stem
        docs[slug] = {"path": path, "title": fm.get("title", slug), "text": text}

    linked = set()
    for slug, doc in docs.items():
        for target in re.findall(r"\]\([^)]*?([a-z0-9-]+)\.md[)#]", doc["text"]):
            if target != slug:                      # a self-link is not an inbound link
                linked.add(target)
        for target in re.findall(r'related_articles:\s*\[([^\]]*)\]', doc["text"]):
            for t in re.findall(r'"([^"]+)"', target):
                if t != slug:
                    linked.add(t)

    orphans = [
        (slug, d) for slug, d in docs.items()
        if slug not in linked and slug not in ENTRY_POINTS
    ]

    if not orphans:
        print(f"Orphan check: ✓ every one of {len(docs)} published articles is linked from somewhere")
        return 0

    print(f"Orphan check: {len(orphans)} of {len(docs)} published articles have no inbound link\n")
    for slug, d in sorted(orphans):
        print(f"  {d['path'].relative_to(ROOT)}")
        print(f"      {d['title']}")
    print(
        "\nLink each from the hub, overview or related article people would arrive from —\n"
        "settings-hub, integrations-hub, the product-area FAQ, or related_articles."
    )
    return 0        # a report, not a gate


if __name__ == "__main__":
    sys.exit(main())
