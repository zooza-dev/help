#!/usr/bin/env python3
"""
Rewrite legacy internal links in all content/*.md files.

Converts legacy URLs like:
- https://support.zooza.online/portal/en/kb/articles/SLUG
- /portal/en/kb/articles/SLUG

To relative .md paths based on content/_redirects.yml mappings.
"""

import os
import re
from pathlib import Path
from typing import Dict, Tuple, Union

# Base paths
REPO_ROOT = Path(__file__).parent.parent
CONTENT_DIR = REPO_ROOT / "content"
REDIRECTS_FILE = CONTENT_DIR / "_redirects.yml"


def load_redirects() -> Dict[str, Tuple[str, str]]:
    """
    Load redirects from _redirects.yml and build a mapping.

    Returns:
        Dict mapping legacy slug to (new_slug, product_area)
        Example: {"whatsapp-integration-usage-beta": ("whatsapp-integration", "communication")}
    """
    with open(REDIRECTS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    mapping = {}

    # Simple YAML parsing for our specific format
    # Looking for patterns like:
    #   - from: "/portal/en/kb/articles/SLUG"
    #     to: "/help/AREA/NEW-SLUG"

    from_pattern = r'from:\s*"(/portal/en/kb/articles/[^"]+)"'
    to_pattern = r'to:\s*"(/help/[^"]+)"'

    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]

        # Look for "from:" line
        from_match = re.search(from_pattern, line)
        if from_match:
            from_path = from_match.group(1)

            # Look for corresponding "to:" line (should be next non-empty line)
            j = i + 1
            while j < len(lines) and j < i + 3:  # Look ahead max 3 lines
                to_match = re.search(to_pattern, lines[j])
                if to_match:
                    to_path = to_match.group(1)

                    # Extract legacy slug from: /portal/en/kb/articles/SLUG
                    legacy_slug_match = re.search(r'/portal/en/kb/articles/([^/]+)$', from_path)
                    if legacy_slug_match:
                        legacy_slug = legacy_slug_match.group(1)

                        # Extract new slug and product area from: /help/AREA/SLUG
                        new_path_match = re.search(r'/help/([^/]+)/([^/]+)$', to_path)
                        if new_path_match:
                            product_area = new_path_match.group(1)
                            new_slug = new_path_match.group(2)

                            mapping[legacy_slug] = (new_slug, product_area)
                    break
                j += 1
        i += 1

    return mapping


def find_content_file(slug: str, product_area: str) -> Union[Path, None]:
    """
    Find the actual .md file for a given slug and product area.

    The file could be in content/guides/, content/setup/, content/faq/, etc.
    We search all subdirectories under content/ for a file matching the slug.
    """
    # Try exact match first in common directories
    for subdir in ['guides', 'setup', 'faq', 'troubleshooting', 'payments']:
        candidate = CONTENT_DIR / subdir / f"{slug}.md"
        if candidate.exists():
            return candidate

    # If not found, search all .md files in content/
    for md_file in CONTENT_DIR.glob("**/*.md"):
        if md_file.stem == slug and md_file.name != "_redirects.yml":
            return md_file

    return None


def compute_relative_path(from_file: Path, to_file: Path) -> str:
    """
    Compute relative path from one .md file to another.

    Example:
        from_file: content/guides/foo.md
        to_file: content/setup/bar.md
        returns: ../setup/bar.md
    """
    return os.path.relpath(to_file, from_file.parent)


def rewrite_links_in_file(file_path: Path, slug_mapping: Dict[str, Tuple[str, str]]) -> int:
    """
    Rewrite legacy links in a single markdown file.

    Returns:
        Number of links rewritten
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    links_rewritten = 0

    # Pattern 1: https://support.zooza.online/portal/en/kb/articles/SLUG
    # Pattern 2: /portal/en/kb/articles/SLUG
    # Both can appear in markdown links: [text](URL) or plain URLs

    # Combined pattern to match both in markdown link format
    pattern = r'\[([^\]]+)\]\((https://support\.zooza\.online)?/portal/en/kb/articles/([^)]+)\)'

    def replace_link(match):
        nonlocal links_rewritten
        link_text = match.group(1)
        legacy_slug = match.group(3)

        # Look up the new slug and product area
        if legacy_slug not in slug_mapping:
            # Keep original if we don't have a mapping
            print(f"  ⚠️  No mapping found for legacy slug: {legacy_slug}")
            return match.group(0)

        new_slug, product_area = slug_mapping[legacy_slug]

        # Find the actual .md file
        target_file = find_content_file(new_slug, product_area)
        if not target_file:
            print(f"  ⚠️  Could not find file for slug: {new_slug} (area: {product_area})")
            return match.group(0)

        # Compute relative path
        relative_path = compute_relative_path(file_path, target_file)

        links_rewritten += 1
        return f"[{link_text}]({relative_path})"

    content = re.sub(pattern, replace_link, content)

    # Only write if content changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

    return links_rewritten


def main():
    print("=" * 60)
    print("Rewriting legacy internal links in content/*.md files")
    print("=" * 60)
    print()

    # Load redirect mappings
    print("Loading redirects from content/_redirects.yml...")
    slug_mapping = load_redirects()
    print(f"  ✓ Loaded {len(slug_mapping)} redirect mappings")
    print()

    # Find all .md files in content/
    md_files = [
        f for f in CONTENT_DIR.glob("**/*.md")
        if f.name not in ['_redirects.yml', 'doc-template.md']
    ]
    print(f"Found {len(md_files)} markdown files to process")
    print()

    # Process each file
    total_links_rewritten = 0
    files_updated = 0

    for md_file in sorted(md_files):
        relative_path = md_file.relative_to(REPO_ROOT)
        links_rewritten = rewrite_links_in_file(md_file, slug_mapping)

        if links_rewritten > 0:
            files_updated += 1
            total_links_rewritten += links_rewritten
            print(f"  ✓ {relative_path}: {links_rewritten} link(s) rewritten")

    print()
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"Files processed:      {len(md_files)}")
    print(f"Files updated:        {files_updated}")
    print(f"Total links rewritten: {total_links_rewritten}")
    print()

    if files_updated == 0:
        print("✓ No legacy links found or all links already converted!")
    else:
        print("✓ Link rewriting complete!")


if __name__ == "__main__":
    main()
