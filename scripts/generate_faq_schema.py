#!/usr/bin/env python3
"""
Generate FAQ schema (JSON-LD) for all FAQ content files.
Output: static/schema/faq/{slug}.json

Each FAQ page gets a FAQPage schema with all its Q&A pairs extracted.
The Docusaurus theme (or a custom head injection) can reference these files
to enable Google rich snippets for FAQ pages.

Usage:
    python3 scripts/generate_faq_schema.py
    python3 scripts/generate_faq_schema.py --dry-run
"""

import os
import re
import sys
import json
import yaml

CONTENT_DIR = os.path.join(os.path.dirname(__file__), "..", "content")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "static", "schema", "faq")
BASE_URL = "https://help.zooza.online"

AREA_SLUG = {
    "Dashboard": "dashboard", "Programmes": "programmes", "Classes": "classes",
    "Calendar": "calendar", "Bookings": "bookings", "Orders": "orders",
    "Clients": "clients", "Payments": "payments", "Settings": "settings",
    "Widgets": "widgets", "Communication": "communication",
}

DRY_RUN = "--dry-run" in sys.argv


def parse_frontmatter(content):
    if not content.startswith("---"):
        return {}, content
    end = content.find("\n---", 3)
    if end == -1:
        return {}, content
    try:
        fm = yaml.safe_load(content[3:end]) or {}
    except Exception:
        fm = {}
    return fm, content[end + 4:]


def clean_text(text):
    """Strip markdown syntax from answer text for schema."""
    # Remove HTML comments
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    # Remove images
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    # Inline links → text
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    # Bold/italic
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    # Code
    text = re.sub(r"`([^`]+)`", r"\1", text)
    # Tables — collapse to single space
    text = re.sub(r"\|[^\n]+\|", "", text)
    # Blockquotes
    text = re.sub(r"^>+\s?", "", text, flags=re.MULTILINE)
    # Normalize whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_qa_pairs(body):
    """Extract ## headings as questions and following text as answers."""
    pairs = []
    # Split on ## headings (questions)
    sections = re.split(r"^(## .+)$", body, flags=re.MULTILINE)
    # sections: [preamble, heading1, body1, heading2, body2, ...]
    for i in range(1, len(sections) - 1, 2):
        question = sections[i].lstrip("#").strip()
        answer_raw = sections[i + 1] if i + 1 < len(sections) else ""
        # Stop at ### sub-sections or Related
        answer_raw = re.split(r"^## ", answer_raw, flags=re.MULTILINE)[0]
        # Skip "Related" heading if it's the question
        if question.lower() in ("related", "see also"):
            continue
        answer = clean_text(answer_raw)
        if answer and len(answer) > 20:
            pairs.append({"question": question, "answer": answer})
    return pairs


def generate_schema(title, url, qa_pairs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "name": title,
        "url": url,
        "mainEntity": [
            {
                "@type": "Question",
                "name": q["question"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": q["answer"]
                }
            }
            for q in qa_pairs
        ]
    }


def main():
    faq_dir = os.path.join(CONTENT_DIR, "faq")
    processed = 0
    skipped = 0

    for fname in sorted(os.listdir(faq_dir)):
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(faq_dir, fname)
        with open(fpath) as f:
            content = f.read()

        fm, body = parse_frontmatter(content)
        if fm.get("status") in ("draft", "archived"):
            skipped += 1
            continue

        slug = fm.get("slug", fname.replace(".md", ""))
        title = fm.get("title", slug)
        product_area = fm.get("product_area", "Settings")
        area_slug = AREA_SLUG.get(product_area, product_area.lower())
        url = f"{BASE_URL}/{area_slug}/{slug}"

        qa_pairs = extract_qa_pairs(body)
        if not qa_pairs:
            skipped += 1
            continue

        schema = generate_schema(title, url, qa_pairs)
        out_path = os.path.join(OUTPUT_DIR, f"{slug}.json")

        if DRY_RUN:
            print(f"[dry-run] {slug}: {len(qa_pairs)} Q&A pairs → {out_path}")
        else:
            os.makedirs(OUTPUT_DIR, exist_ok=True)
            with open(out_path, "w") as f:
                json.dump(schema, f, indent=2, ensure_ascii=False)
            processed += 1
            print(f"  {slug}: {len(qa_pairs)} Q&A pairs")

    if not DRY_RUN:
        print(f"\nDone: {processed} FAQ schema files written to static/schema/faq/")
        print(f"Skipped: {skipped} (draft/archived/no Q&A)")
        print(f"\nIntegration: In your Docusaurus theme, add a <script type='application/ld+json'>")
        print(f"that loads the matching schema file for each FAQ page.")


if __name__ == "__main__":
    main()
