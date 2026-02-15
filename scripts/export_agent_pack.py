#!/usr/bin/env python3
"""Generate JSONL agent pack exports from content/ directory.

Outputs:
  build/exports/agent/canonical.jsonl — all content chunked by H2/H3
  build/exports/agent/faq.jsonl       — FAQ-specific records
"""

import json
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = REPO_ROOT / "content"
OUTPUT_DIR = REPO_ROOT / "build" / "exports" / "agent"
MAX_CHUNK = 1600
OVERLAP = 150


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML frontmatter and return (metadata, body)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("---", 3)
    if end == -1:
        return {}, text
    fm_text = text[3:end].strip()
    body = text[end + 3:].strip()
    meta = {}
    for line in fm_text.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.match(r'^(\w[\w_]*)\s*:\s*(.+)$', line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            # Parse arrays
            if val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                if inner:
                    meta[key] = [v.strip().strip('"').strip("'") for v in inner.split(",")]
                else:
                    meta[key] = []
            # Parse booleans
            elif val.lower() in ("true", "false"):
                meta[key] = val.lower() == "true"
            # Parse integers
            elif re.match(r'^\d+$', val):
                meta[key] = int(val)
            # Strip quotes
            elif (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                meta[key] = val[1:-1]
            else:
                meta[key] = val
    return meta, body


def split_by_headings(body: str) -> list[tuple[str, str]]:
    """Split body into (heading_path, text) chunks by H2/H3 headings."""
    lines = body.split("\n")
    chunks = []
    current_heading = "(intro)"
    current_lines = []

    for line in lines:
        h2_match = re.match(r'^## (.+)$', line)
        h3_match = re.match(r'^### (.+)$', line)

        if h2_match or h3_match:
            # Flush current chunk
            text = "\n".join(current_lines).strip()
            if text:
                chunks.append((current_heading, text))
            current_heading = (h2_match or h3_match).group(1).strip()
            current_lines = [line]
        else:
            current_lines.append(line)

    # Flush last chunk
    text = "\n".join(current_lines).strip()
    if text:
        chunks.append((current_heading, text))

    return chunks


def further_split(text: str, max_size: int, overlap: int) -> list[str]:
    """Split text that exceeds max_size into smaller pieces with overlap."""
    if len(text) <= max_size:
        return [text]

    pieces = []
    paragraphs = re.split(r'\n\n+', text)
    current = ""

    for para in paragraphs:
        if current and len(current) + len(para) + 2 > max_size:
            pieces.append(current.strip())
            # Keep overlap from end of current
            if overlap > 0 and len(current) > overlap:
                current = current[-overlap:] + "\n\n" + para
            else:
                current = para
        else:
            current = (current + "\n\n" + para).strip() if current else para

    if current.strip():
        pieces.append(current.strip())

    return pieces


def build_url(meta: dict) -> str:
    """Build the URL path for a doc."""
    product_area = meta.get("product_area", "").lower()
    slug = meta.get("slug", "")
    return f"/help/{product_area}/{slug}"


def process_file(filepath: Path) -> list[dict]:
    """Process a single markdown file into export records."""
    text = filepath.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)

    if not meta.get("slug"):
        return []
    if meta.get("status") == "archived":
        return []

    rel_path = str(filepath.relative_to(REPO_ROOT))
    url = build_url(meta)
    base_record = {
        "doc_id": meta["slug"],
        "title": meta.get("title", ""),
        "url": url,
        "type": meta.get("type", ""),
        "product_area": meta.get("product_area", ""),
        "sub_area": meta.get("sub_area", ""),
        "tags": meta.get("tags", []),
        "audience": meta.get("audience", []),
        "status": meta.get("status", "published"),
    }

    # Strip REVIEW comments from body
    body = re.sub(r'<!--\s*REVIEW:.*?-->', '', body, flags=re.DOTALL).strip()

    chunks = split_by_headings(body)
    records = []

    for heading, chunk_text in chunks:
        # Further split if too large
        pieces = further_split(chunk_text, MAX_CHUNK, OVERLAP)
        for i, piece in enumerate(pieces):
            record = dict(base_record)
            record["heading_path"] = heading
            record["source_path"] = rel_path
            record["text"] = piece
            if len(pieces) > 1:
                record["chunk_part"] = i + 1
            records.append(record)

    return records


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Collect all content files (excluding _shared and _ prefixed files)
    all_files = sorted(CONTENT_DIR.rglob("*.md"))
    content_files = [
        f for f in all_files
        if "_shared" not in f.parts
        and not f.name.startswith("_")
    ]

    faq_files = [f for f in content_files if "/faq/" in str(f)]
    non_faq_files = [f for f in content_files if "/faq/" not in str(f)]

    # Generate canonical.jsonl (all content)
    canonical_records = []
    for f in content_files:
        canonical_records.extend(process_file(f))

    canonical_path = OUTPUT_DIR / "canonical.jsonl"
    with open(canonical_path, "w", encoding="utf-8") as out:
        for rec in canonical_records:
            out.write(json.dumps(rec, ensure_ascii=False) + "\n")

    # Generate faq.jsonl (FAQ content only)
    faq_records = []
    for f in faq_files:
        faq_records.extend(process_file(f))

    faq_path = OUTPUT_DIR / "faq.jsonl"
    with open(faq_path, "w", encoding="utf-8") as out:
        for rec in faq_records:
            out.write(json.dumps(rec, ensure_ascii=False) + "\n")

    # Summary
    print(f"Content files processed: {len(content_files)}")
    print(f"  - FAQ files: {len(faq_files)}")
    print(f"  - Non-FAQ files: {len(non_faq_files)}")
    print(f"canonical.jsonl: {len(canonical_records)} chunks")
    print(f"faq.jsonl: {len(faq_records)} chunks")
    print(f"Output: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
