#!/usr/bin/env python3
"""Generate agent export JSONL from content/ Markdown files."""

import json
import os
import re
import glob

CONTENT_DIR = os.path.join(os.path.dirname(__file__), "..", "content")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "exports", "agent")
MAX_CHARS = 1600
OVERLAP_CHARS = 150


def parse_frontmatter(text):
    """Extract YAML frontmatter as a dict (simple parser, no PyYAML needed)."""
    fm = {}
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return fm, text
    raw = m.group(1)
    body = text[m.end():]
    for line in raw.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()
        # Parse arrays
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1]
            items = [v.strip().strip('"').strip("'") for v in inner.split(",") if v.strip()]
            fm[key] = items
        # Parse booleans
        elif val.lower() == "true":
            fm[key] = True
        elif val.lower() == "false":
            fm[key] = False
        # Strip quotes
        elif (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            fm[key] = val[1:-1]
        else:
            fm[key] = val
    return fm, body


def slugify_area(area):
    return area.lower().replace(" ", "-")


def split_by_headings(body):
    """Split markdown body into sections by H2/H3 headings.
    Returns list of (heading_path, text) tuples."""
    lines = body.split("\n")
    sections = []
    current_h2 = None
    current_h3 = None
    current_lines = []

    def flush():
        if current_lines:
            text = "\n".join(current_lines).strip()
            if text:
                path_parts = []
                if current_h2:
                    path_parts.append(current_h2)
                if current_h3:
                    path_parts.append(current_h3)
                heading_path = " > ".join(path_parts) if path_parts else "(intro)"
                sections.append((heading_path, text))

    for line in lines:
        h2_match = re.match(r"^## (.+)$", line)
        h3_match = re.match(r"^### (.+)$", line)

        if h2_match:
            flush()
            current_h2 = h2_match.group(1).strip()
            current_h3 = None
            current_lines = [line]
        elif h3_match:
            flush()
            current_h3 = h3_match.group(1).strip()
            current_lines = [line]
        else:
            current_lines.append(line)

    flush()
    return sections


def split_large_block(text, max_chars):
    """Split a single large block (e.g. a table) by lines."""
    lines = text.split("\n")
    chunks = []
    current = ""
    for line in lines:
        if current and len(current) + len(line) + 1 > max_chars:
            chunks.append(current.strip())
            current = line
        else:
            current = current + "\n" + line if current else line
    if current.strip():
        chunks.append(current.strip())
    return chunks


def chunk_text(text, max_chars, overlap_chars):
    """Split text into chunks respecting max size with overlap."""
    if len(text) <= max_chars:
        return [text]

    chunks = []
    paragraphs = re.split(r"\n\n+", text)
    current = ""

    for para in paragraphs:
        # If a single paragraph exceeds max, split it by lines
        if len(para) > max_chars:
            if current.strip():
                chunks.append(current.strip())
                current = ""
            sub_chunks = split_large_block(para, max_chars)
            chunks.extend(sub_chunks)
            continue

        if current and len(current) + len(para) + 2 > max_chars:
            chunks.append(current.strip())
            # Overlap: take last N chars of current chunk
            if len(current) > overlap_chars:
                overlap = current[-overlap_chars:]
                # Try to start overlap at a word boundary
                space_idx = overlap.find(" ")
                if space_idx > 0:
                    overlap = overlap[space_idx + 1:]
                current = overlap + "\n\n" + para
            else:
                current = para
        else:
            current = current + "\n\n" + para if current else para

    if current.strip():
        chunks.append(current.strip())

    return chunks


def process_file(filepath, is_faq=False):
    """Process a single Markdown file into JSONL records."""
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    fm, body = parse_frontmatter(text)
    if not fm.get("slug"):
        return []

    slug = fm["slug"]
    title = fm.get("title", "")
    doc_type = fm.get("type", "")
    product_area = fm.get("product_area", "")
    tags = fm.get("tags", [])
    audience = fm.get("audience", [])
    url = f"/help/{slugify_area(product_area)}/{slug}"

    # Remove the H1 line from body
    body = re.sub(r"^# .+\n*", "", body, count=1)

    sections = split_by_headings(body)
    records = []

    for heading_path, section_text in sections:
        chunks = chunk_text(section_text, MAX_CHARS, OVERLAP_CHARS)
        for i, chunk in enumerate(chunks):
            # Skip near-empty chunks (< 20 chars of real content)
            if len(chunk.strip()) < 20:
                continue
            record = {
                "doc_id": slug,
                "title": title,
                "url": url,
                "type": doc_type,
                "product_area": product_area,
                "tags": tags,
                "audience": audience,
                "heading_path": heading_path,
            }
            if len(chunks) > 1:
                record["chunk_index"] = i
            record["text"] = chunk
            records.append(record)

    return records


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Canonical: all content files except _shared and faq
    canonical_records = []
    faq_records = []

    for md_path in sorted(glob.glob(os.path.join(CONTENT_DIR, "**", "*.md"), recursive=True)):
        # Skip _shared template
        if "/_shared/" in md_path:
            continue
        # Skip _redirects
        if md_path.endswith("_redirects.yml"):
            continue

        rel = os.path.relpath(md_path, CONTENT_DIR)
        if rel.startswith("faq/"):
            faq_records.extend(process_file(md_path, is_faq=True))
        else:
            canonical_records.extend(process_file(md_path))

    # Write canonical.jsonl
    canonical_path = os.path.join(OUTPUT_DIR, "canonical.jsonl")
    with open(canonical_path, "w", encoding="utf-8") as f:
        for rec in canonical_records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    # Write faq.jsonl
    faq_path = os.path.join(OUTPUT_DIR, "faq.jsonl")
    with open(faq_path, "w", encoding="utf-8") as f:
        for rec in faq_records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    print(f"canonical.jsonl: {len(canonical_records)} records")
    print(f"faq.jsonl:       {len(faq_records)} records")

    # Stats
    max_len = max((len(r["text"]) for r in canonical_records + faq_records), default=0)
    avg_len = sum(len(r["text"]) for r in canonical_records + faq_records) // max(len(canonical_records) + len(faq_records), 1)
    over = sum(1 for r in canonical_records + faq_records if len(r["text"]) > MAX_CHARS)
    print(f"Max chunk: {max_len} chars, Avg: {avg_len} chars, Over {MAX_CHARS}: {over}")


if __name__ == "__main__":
    main()
