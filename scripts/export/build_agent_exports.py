#!/usr/bin/env python3
"""Generate model-agnostic agent export JSONL from content/ Markdown files.

Outputs:
  build/exports/agent/canonical.jsonl  — all non-FAQ content
  build/exports/agent/faq.jsonl        — FAQ content from content/faq/
"""

import json
import logging
import os
import re
import sys
from pathlib import Path

import yaml

logger = logging.getLogger(__name__)

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
CONTENT_DIR = ROOT_DIR / "content"
OUTPUT_DIR = ROOT_DIR / "build" / "exports" / "agent"
MAX_CHARS = 1600
OVERLAP_CHARS = 150


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and return (metadata, body)."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return {}, text
    fm = yaml.safe_load(m.group(1)) or {}
    return fm, text[m.end():]


def slugify_area(area: str) -> str:
    return area.lower().replace(" ", "-")


def split_by_headings(body: str) -> list[tuple[str, str]]:
    """Split markdown body into sections by H2/H3.

    Returns list of (heading_path, text) tuples.
    """
    lines = body.split("\n")
    sections: list[tuple[str, str]] = []
    current_h2: str | None = None
    current_h3: str | None = None
    current_lines: list[str] = []

    def flush():
        if current_lines:
            text = "\n".join(current_lines).strip()
            if text:
                parts = [p for p in [current_h2, current_h3] if p]
                heading_path = " > ".join(parts) if parts else "(intro)"
                sections.append((heading_path, text))

    for line in lines:
        h2 = re.match(r"^## (.+)$", line)
        h3 = re.match(r"^### (.+)$", line)
        if h2:
            flush()
            current_h2 = h2.group(1).strip()
            current_h3 = None
            current_lines = [line]
        elif h3:
            flush()
            current_h3 = h3.group(1).strip()
            current_lines = [line]
        else:
            current_lines.append(line)

    flush()
    return sections


def chunk_text(text: str, max_chars: int = MAX_CHARS, overlap: int = OVERLAP_CHARS) -> list[str]:
    """Split text into chunks respecting max size with overlap."""
    if len(text) <= max_chars:
        return [text]

    chunks: list[str] = []
    paragraphs = re.split(r"\n\n+", text)
    current = ""

    for para in paragraphs:
        if len(para) > max_chars:
            if current.strip():
                chunks.append(current.strip())
                current = ""
            # Split oversized paragraph by lines
            buf = ""
            for line in para.split("\n"):
                if buf and len(buf) + len(line) + 1 > max_chars:
                    chunks.append(buf.strip())
                    buf = line
                else:
                    buf = buf + "\n" + line if buf else line
            if buf.strip():
                chunks.append(buf.strip())
            continue

        if current and len(current) + len(para) + 2 > max_chars:
            chunks.append(current.strip())
            # Create overlap from tail of previous chunk
            if len(current) > overlap:
                tail = current[-overlap:]
                space = tail.find(" ")
                if space > 0:
                    tail = tail[space + 1:]
                current = tail + "\n\n" + para
            else:
                current = para
        else:
            current = current + "\n\n" + para if current else para

    if current.strip():
        chunks.append(current.strip())
    return chunks


def process_file(filepath: Path) -> list[dict]:
    """Process a single Markdown file into JSONL records."""
    text = filepath.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)

    slug = fm.get("slug")
    if not slug:
        logger.warning("Skipping %s: no slug in frontmatter", filepath)
        return []

    product_area = fm.get("product_area", "")
    url = f"/help/{slugify_area(product_area)}/{slug}"
    rel_path = str(filepath.relative_to(ROOT_DIR))

    # Strip the H1
    body = re.sub(r"^# .+\n*", "", body, count=1)

    sections = split_by_headings(body)
    records: list[dict] = []

    for heading_path, section_text in sections:
        chunks = chunk_text(section_text)
        for i, chunk in enumerate(chunks):
            if len(chunk.strip()) < 20:
                continue
            record = {
                "doc_id": slug,
                "title": fm.get("title", ""),
                "url": url,
                "type": fm.get("type", ""),
                "product_area": product_area,
                "sub_area": fm.get("sub_area", ""),
                "tags": fm.get("tags", []),
                "audience": fm.get("audience", []),
                "status": fm.get("status", "published"),
                "heading_path": heading_path,
                "source_path": rel_path,
                "text": chunk,
            }
            if len(chunks) > 1:
                record["chunk_index"] = i
            records.append(record)

    return records


def build_agent_exports() -> dict:
    """Main entry point. Returns stats dict."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    canonical_records: list[dict] = []
    faq_records: list[dict] = []

    for md_path in sorted(CONTENT_DIR.rglob("*.md")):
        if "/_shared/" in str(md_path):
            continue
        if md_path.name.startswith("_"):
            continue

        rel = md_path.relative_to(CONTENT_DIR)
        if str(rel).startswith("faq/"):
            faq_records.extend(process_file(md_path))
        else:
            canonical_records.extend(process_file(md_path))

    canonical_path = OUTPUT_DIR / "canonical.jsonl"
    with open(canonical_path, "w", encoding="utf-8") as f:
        for rec in canonical_records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    faq_path = OUTPUT_DIR / "faq.jsonl"
    with open(faq_path, "w", encoding="utf-8") as f:
        for rec in faq_records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    all_records = canonical_records + faq_records
    stats = {
        "canonical_records": len(canonical_records),
        "faq_records": len(faq_records),
        "max_chunk_chars": max((len(r["text"]) for r in all_records), default=0),
        "avg_chunk_chars": (
            sum(len(r["text"]) for r in all_records) // max(len(all_records), 1)
        ),
        "over_limit": sum(1 for r in all_records if len(r["text"]) > MAX_CHARS),
    }

    logger.info(
        "Agent export: canonical=%d, faq=%d, max=%d, avg=%d, over=%d",
        stats["canonical_records"],
        stats["faq_records"],
        stats["max_chunk_chars"],
        stats["avg_chunk_chars"],
        stats["over_limit"],
    )
    return stats


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    stats = build_agent_exports()
    print(f"canonical.jsonl: {stats['canonical_records']} records")
    print(f"faq.jsonl:       {stats['faq_records']} records")
    print(
        f"Max chunk: {stats['max_chunk_chars']} chars, "
        f"Avg: {stats['avg_chunk_chars']} chars, "
        f"Over {MAX_CHARS}: {stats['over_limit']}"
    )


if __name__ == "__main__":
    main()
