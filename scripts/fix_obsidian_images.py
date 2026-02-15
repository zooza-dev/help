#!/usr/bin/env python3
"""
Fix Obsidian-style image references in Markdown files.

Finds all ![[Pasted image ...]] references in content/, moves the image
files to assets/images/ with descriptive kebab-case names, replaces the
Obsidian syntax with standard Markdown, and deletes the originals.

Usage:
    python3 scripts/fix_obsidian_images.py [--dry-run]
"""

import os
import re
import sys
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = REPO_ROOT / "content"
ASSETS_DIR = REPO_ROOT / "assets" / "images"

# Pattern to match Obsidian image embeds: ![[Pasted image 20260215170502.png]]
OBSIDIAN_RE = re.compile(r'!\[\[([^\]]+\.(png|jpg|jpeg|gif|svg|webp))\]\]', re.IGNORECASE)


def find_image_file(filename):
    """Search for the image file in repo root and common locations."""
    candidates = [
        REPO_ROOT / filename,
        CONTENT_DIR / filename,
        REPO_ROOT / "attachments" / filename,
    ]
    # Also search recursively (slower, last resort)
    for c in candidates:
        if c.exists():
            return c
    # Glob search
    for match in REPO_ROOT.rglob(filename):
        if "assets/images" not in str(match):
            return match
    return None


def slugify_image_name(md_file, original_name, context_line):
    """Generate a descriptive kebab-case filename based on the markdown file and context."""
    # Base name from the markdown file (e.g., pay-as-you-go-programme)
    md_stem = md_file.stem

    # Extract a number suffix from the original (e.g., 20260215170502 -> 01, 02, etc.)
    # We use a counter per file instead
    ext = Path(original_name).suffix.lower()

    return md_stem, ext


def process_file(md_path, dry_run=False):
    """Process a single markdown file for Obsidian image references."""
    text = md_path.read_text(encoding="utf-8")
    matches = list(OBSIDIAN_RE.finditer(text))

    if not matches:
        return 0

    md_stem = md_path.stem
    rel_assets = os.path.relpath(ASSETS_DIR, md_path.parent)
    changes = []
    counter = 1

    for match in matches:
        original_name = match.group(1)
        ext = Path(original_name).suffix.lower()

        # Generate descriptive name
        new_name = f"{md_stem}-{counter:02d}{ext}"
        counter += 1

        # Find the source image
        source = find_image_file(original_name)

        if source:
            dest = ASSETS_DIR / new_name
            if not dry_run:
                ASSETS_DIR.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, dest)
                print(f"  COPY: {source.name} -> assets/images/{new_name}")
            else:
                print(f"  [DRY] COPY: {source.name} -> assets/images/{new_name}")

            # Build standard markdown reference
            alt_text = f"Screenshot — {md_stem.replace('-', ' ')}"
            new_ref = f"![{alt_text}]({rel_assets}/{new_name})"

            changes.append((match.group(0), new_ref, source))
        else:
            print(f"  WARN: Image not found: {original_name}")
            # Still replace the syntax but mark as missing
            new_ref = f"<!-- IMAGE MISSING: {original_name} -->"
            changes.append((match.group(0), new_ref, None))

    # Apply replacements
    new_text = text
    for old, new, _ in changes:
        new_text = new_text.replace(old, new, 1)

    if not dry_run and new_text != text:
        md_path.write_text(new_text, encoding="utf-8")

    # Delete source images (only after successful replacement)
    if not dry_run:
        deleted_sources = set()
        for _, _, source in changes:
            if source and source not in deleted_sources:
                source.unlink()
                print(f"  DELETE: {source}")
                deleted_sources.add(source)

    return len(changes)


def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("=== DRY RUN MODE ===\n")

    print(f"Scanning {CONTENT_DIR} for Obsidian image references...\n")

    total_fixes = 0
    for md_path in sorted(CONTENT_DIR.rglob("*.md")):
        fixes = process_file(md_path, dry_run=dry_run)
        if fixes > 0:
            print(f"  {md_path.relative_to(REPO_ROOT)}: {fixes} image(s) fixed\n")
            total_fixes += fixes

    if total_fixes == 0:
        print("No Obsidian image references found. All clean!")
    else:
        print(f"\nTotal: {total_fixes} image(s) {'would be' if dry_run else ''} fixed.")


if __name__ == "__main__":
    main()
