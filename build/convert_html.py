#!/usr/bin/env python3
"""
Convert legacy Zooza HTML KB articles to semantic Markdown.
Usage: python3 build/convert_html.py <file_id> <slug> <type> <product_area> [sub_area]
       python3 build/convert_html.py --batch <batch_file.tsv>

Reads legacy/<file_id>_Welcome to Zooza.html
Writes content/<type>/<slug>.md
"""

import re
import sys
import os
from html import unescape

LEGACY_DIR = os.path.join(os.path.dirname(__file__), "..", "legacy")
CONTENT_DIR = os.path.join(os.path.dirname(__file__), "..", "content")


def strip_html(html_str):
    """Remove all HTML tags, return plain text."""
    return unescape(re.sub(r"<[^>]+>", "", html_str)).strip()


def extract_article_body(html):
    """Extract the article content div."""
    m = re.search(
        r'<div\s+class="description\s+KbDetailLtContainer__description"[^>]*>(.*)',
        html, re.DOTALL,
    )
    if not m:
        return ""
    body = m.group(1)
    for end_marker in [
        '<div class="KbDetailLtContainer__updateTime"',
        '<div class="KbDetailLtContainer__review"',
        "<style data-css-purify",
    ]:
        idx = body.find(end_marker)
        if idx > 0:
            body = body[:idx]
    return body.strip()


def extract_source_url(html):
    m = re.search(r"href='(https://support\.zooza\.online/portal/en/kb/articles/[^']+)'", html)
    return m.group(1) if m else ""


def extract_title(html):
    m = re.search(r'data-id="article_Title"[^>]*>(.*?)</h1>', html, re.DOTALL)
    if m:
        t = re.sub(r"<[^>]+>", "", m.group(1))
        return unescape(t).replace("\n", " ").strip()
    return "Untitled"


def html_to_markdown(html):
    """Convert article body HTML to clean Markdown."""

    # ── Phase 1: Structural conversions (order matters) ────────────────

    # 1a. Convert toc_anchors H1s to H2 (Zooza uses H1 for sections)
    html = re.sub(
        r'<h1[^>]*class="toc_anchors"[^>]*>(.*?)</h1>',
        lambda m: f'\n\n## {strip_html(m.group(1))}\n\n',
        html, flags=re.DOTALL,
    )
    # 1b. Convert remaining heading tags
    for lvl in range(6, 1, -1):
        html = re.sub(
            rf"<h{lvl}[^>]*>(.*?)</h{lvl}>",
            lambda m, l=lvl: f'\n\n{"#" * l} {strip_html(m.group(1))}\n\n',
            html, flags=re.DOTALL,
        )

    # 2. Callout boxes (colored divs) → blockquotes
    # Match the pattern: styled div with bg-color, optional icon img, then content
    callout_colors = {
        r"189,\s*229,\s*214": "Tip",     # green
        r"255,\s*198,\s*151": "Note",     # orange
        r"252,\s*177,\s*177": "Warning",  # red
        r"179,\s*205,\s*224": "",          # blue (info, no label)
    }
    for rgb_pat, label in callout_colors.items():
        prefix = f"**{label}:** " if label else ""
        # Try to match the whole callout div
        html = re.sub(
            rf'<div[^>]*style="[^"]*background-color:\s*rgb\({rgb_pat}\)[^"]*"[^>]*>'
            r'(?:\s*<img[^>]*>)?\s*(?:</div>\s*)?<div>(.*?)</div>(?:\s*</div>)?',
            lambda m, p=prefix: f'\n\n> {p}{strip_html(m.group(1))}\n\n',
            html, flags=re.DOTALL,
        )

    # 3. Images → Markdown image syntax
    html = re.sub(
        r'<img[^>]*src="([^"]+)"[^>]*/?>',
        lambda m: f'\n\n![Screenshot]({m.group(1)})\n\n',
        html,
    )

    # 4. Links
    html = re.sub(
        r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>',
        lambda m: f'[{strip_html(m.group(2))}]({m.group(1)})' if strip_html(m.group(2)) else '',
        html, flags=re.DOTALL,
    )

    # 5. Bold/italic (before list processing so they're clean inside items)
    html = re.sub(r"<b[^>]*>(.*?)</b>", r"**\1**", html, flags=re.DOTALL)
    html = re.sub(r"<strong[^>]*>(.*?)</strong>", r"**\1**", html, flags=re.DOTALL)
    html = re.sub(r"<i[^>]*>(.*?)</i>", r"*\1*", html, flags=re.DOTALL)
    html = re.sub(r"<em[^>]*>(.*?)</em>", r"*\1*", html, flags=re.DOTALL)

    # 6. Tables → Markdown tables
    def convert_table(m):
        thtml = m.group(0)
        rows = re.findall(r"<tr[^>]*>(.*?)</tr>", thtml, re.DOTALL)
        if not rows:
            return ""
        md_rows = []
        for row in rows:
            cells = re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", row, re.DOTALL)
            md_cells = [strip_html(c).replace("|", "\\|") for c in cells]
            md_rows.append("| " + " | ".join(md_cells) + " |")
        if len(md_rows) >= 1:
            ncols = max(r.count("|") - 1 for r in md_rows)
            md_rows.insert(1, "|" + "|".join(["---"] * ncols) + "|")
        return "\n\n" + "\n".join(md_rows) + "\n\n"

    html = re.sub(r"<table[^>]*>.*?</table>", convert_table, html, flags=re.DOTALL)

    # 7. Lists (most complex part)
    # Process ordered lists from innermost to outermost
    def convert_ol(m, indent=0):
        inner = m.group(1)
        # Find li items (non-greedy, handle nested ol)
        items = []
        # Use a simple state machine to find top-level li items
        depth = 0
        current = ""
        i = 0
        while i < len(inner):
            # Check for <li
            li_open = re.match(r'<li[^>]*>', inner[i:])
            li_close = inner[i:].startswith('</li>')
            ol_open = re.match(r'<ol[^>]*>', inner[i:])
            ol_close = inner[i:].startswith('</ol>')

            if li_open and depth == 0:
                current = ""
                i += li_open.end()
                depth = 1
                continue
            elif li_close and depth == 1:
                items.append(current)
                current = ""
                depth = 0
                i += 5
                continue
            elif ol_open:
                depth += 1
            elif ol_close:
                depth -= 1

            if depth >= 1:
                current += inner[i]
            i += 1

        if current.strip() and depth >= 1:
            items.append(current)

        md_items = []
        prefix = "   " * indent
        for idx, item in enumerate(items, 1):
            # Check for nested ol
            nested_match = re.search(r'<ol[^>]*>(.*)</ol>', item, re.DOTALL)
            if nested_match:
                # Split: before ol, the ol itself
                before_ol = item[:nested_match.start()]
                # Clean the item text
                item_text = strip_html(before_ol).strip()
                if item_text:
                    md_items.append(f"{prefix}{idx}. {item_text}")
                # Process nested list with increased indent
                nested_items = re.findall(r"<li[^>]*>(.*?)</li>", nested_match.group(1), re.DOTALL)
                for ni, nitem in enumerate(nested_items, 1):
                    ntext = strip_html(nitem).strip()
                    if ntext:
                        md_items.append(f"{prefix}   {ni}. {ntext}")
            else:
                # Handle images inside list items
                img_matches = list(re.finditer(r'\n\n!\[Screenshot\]\([^)]+\)\n\n', item))
                if img_matches:
                    # Get text before first image
                    text_before = item[:img_matches[0].start()]
                    item_text = strip_html(text_before).strip()
                    if item_text:
                        md_items.append(f"{prefix}{idx}. {item_text}")
                    # Add images with indent
                    for img_m in img_matches:
                        md_items.append(f"{prefix}   {img_m.group(0).strip()}")
                    # Get text after last image
                    text_after = item[img_matches[-1].end():]
                    after_clean = strip_html(text_after).strip()
                    if after_clean:
                        md_items.append(f"{prefix}   {after_clean}")
                else:
                    item_text = strip_html(item).strip()
                    if item_text:
                        md_items.append(f"{prefix}{idx}. {item_text}")

        return "\n\n" + "\n".join(md_items) + "\n\n"

    # Process ol tags (up to 5 nesting levels)
    for _ in range(5):
        new_html = re.sub(r"<ol[^>]*>(.*?)</ol>", convert_ol, html, flags=re.DOTALL)
        if new_html == html:
            break
        html = new_html

    # Handle unordered lists
    def convert_ul(m):
        inner = m.group(1)
        items = re.findall(r"<li[^>]*>(.*?)</li>", inner, re.DOTALL)
        md_items = []
        for item in items:
            text = strip_html(item).strip()
            if text:
                md_items.append(f"- {text}")
        return "\n\n" + "\n".join(md_items) + "\n\n"

    for _ in range(5):
        new_html = re.sub(r"<ul[^>]*>(.*?)</ul>", convert_ul, html, flags=re.DOTALL)
        if new_html == html:
            break
        html = new_html

    # ── Phase 2: Clean remaining HTML ──────────────────────────────────

    html = re.sub(r"<br\s*/?>", "\n", html)
    html = re.sub(r"<p[^>]*>", "\n\n", html)
    html = re.sub(r"</p>", "\n\n", html)
    html = re.sub(r"</?div[^>]*>", "\n", html)
    html = re.sub(r"</?figure[^>]*>", "", html)
    html = re.sub(r"</?span[^>]*>", "", html)
    html = re.sub(r"</?font[^>]*>", "", html)
    html = re.sub(r"<[^>]+>", "", html)
    html = unescape(html)

    # ── Phase 3: Post-processing cleanup ───────────────────────────────

    lines = html.split("\n")
    cleaned = []
    for line in lines:
        # Remove zero-width spaces and other invisible chars
        line = line.replace("\u200b", "").replace("\u00a0", " ")
        # Collapse multiple spaces
        line = re.sub(r"  +", " ", line)
        # Strip trailing whitespace
        line = line.rstrip()
        cleaned.append(line)

    result = "\n".join(cleaned)

    # Remove empty bold/italic markers
    result = re.sub(r"\*\*\s*\*\*", "", result)
    result = re.sub(r"\*\s*\*(?!\*)", "", result)
    # Fix bold/italic with embedded newlines
    result = re.sub(r"\*\*\n+\*\*", "", result)

    # Collapse excessive blank lines
    result = re.sub(r"\n{4,}", "\n\n", result)
    # Remove blank lines that are just spaces
    result = re.sub(r"\n +\n", "\n\n", result)

    # Fix heading formatting: ensure blank line before and after
    result = re.sub(r"([^\n])\n(#{2,} )", r"\1\n\n\2", result)
    result = re.sub(r"(#{2,} [^\n]+)\n([^\n#])", r"\1\n\n\2", result)

    return result.strip()


def convert_file(file_id, slug, doc_type, product_area, sub_area=""):
    filename = f"{file_id}_Welcome to Zooza.html"
    filepath = os.path.join(LEGACY_DIR, filename)

    if not os.path.exists(filepath):
        print(f"ERROR: {filepath} not found", file=sys.stderr)
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    title = extract_title(html)
    body_html = extract_article_body(html)

    if not body_html:
        print(f"WARNING: No article body found in {filename}", file=sys.stderr)
        return False

    body_md = html_to_markdown(body_html)

    # Escape title quotes for YAML
    yaml_title = title.replace('"', '\\"')

    fm = f'''---
title: "{yaml_title}"
slug: "{slug}"
type: "{doc_type}"
product_area: "{product_area}"
sub_area: "{sub_area}"
audience: ["admin"]
tags: []
status: "published"
source_legacy_path: "legacy/{filename}"
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-02-11"
---'''

    md = f"{fm}\n\n# {title}\n\n{body_md}\n"

    output_dir = os.path.join(CONTENT_DIR, doc_type)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{slug}.md")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"OK: {filename} -> content/{doc_type}/{slug}.md")
    return True


def run_batch(batch_file):
    """Process a TSV batch file: file_id<TAB>slug<TAB>type<TAB>product_area<TAB>sub_area"""
    ok = 0
    fail = 0
    with open(batch_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 4:
                print(f"SKIP: bad line: {line}", file=sys.stderr)
                continue
            fid, slug, dtype, parea = parts[0], parts[1], parts[2], parts[3]
            sarea = parts[4] if len(parts) > 4 else ""
            if convert_file(fid, slug, dtype, parea, sarea):
                ok += 1
            else:
                fail += 1
    print(f"\nBatch done: {ok} OK, {fail} failed")


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "--batch":
        run_batch(sys.argv[2])
    elif len(sys.argv) >= 5:
        fid = sys.argv[1]
        slug = sys.argv[2]
        dtype = sys.argv[3]
        parea = sys.argv[4]
        sarea = sys.argv[5] if len(sys.argv) > 5 else ""
        success = convert_file(fid, slug, dtype, parea, sarea)
        sys.exit(0 if success else 1)
    else:
        print("Usage: python3 convert_html.py <file_id> <slug> <type> <product_area> [sub_area]")
        print("       python3 convert_html.py --batch <batch_file.tsv>")
        sys.exit(1)
