#!/usr/bin/env python3
"""Rename slugs, filenames, and update all internal links to use canonical terminology."""

import os
import re
import sys
import yaml
from datetime import date

BASE = os.path.join(os.path.dirname(__file__), "..")
CONTENT_DIR = os.path.join(BASE, "content")
REDIRECTS_PATH = os.path.join(CONTENT_DIR, "_redirects.yml")

# Slug rename rules: applied in order to slug segments (hyphen-separated words)
# Format: (old_word, new_word, preserve_compounds)
# preserve_compounds: list of hyphenated compounds that should NOT be renamed
SLUG_WORD_RULES = [
    ("course", "programme", []),
    ("courses", "programmes", []),
    ("group", "class", ["target-group", "age-group"]),
    ("groups", "classes", ["target-groups", "age-groups"]),
    ("lesson", "session", []),
    ("lessons", "sessions", []),
    ("event", "session", ["paid-event", "paid-events", "multi-day-event"]),
    ("events", "sessions", ["paid-events", "multi-day-events"]),
    ("registration", "booking", ["online-registration"]),
    ("registrations", "bookings", []),
    ("customer", "client", []),
    ("customers", "clients", []),
    ("lecturer", "instructor", []),
    ("lecturers", "instructors", []),
    ("teacher", "instructor", []),
    ("teachers", "instructors", []),
]

# Special full-slug overrides (when simple word replacement isn't enough)
SLUG_OVERRIDES = {
    "registration-and-booking-faq": "booking-faq",
    "individual-lessons-group-interested": "individual-sessions-lead-collection",
}


def rename_slug(old_slug):
    """Apply terminology rules to a slug."""
    if old_slug in SLUG_OVERRIDES:
        return SLUG_OVERRIDES[old_slug]

    new_slug = old_slug
    for old_word, new_word, preserves in SLUG_WORD_RULES:
        # Check if slug contains a preserved compound
        skip = False
        for compound in preserves:
            if compound in new_slug:
                # Check if the word we'd replace is part of this compound
                # e.g. "event" in "paid-event" or "multi-day-event"
                parts = compound.split("-")
                if old_word in parts:
                    skip = True
                    break
        if skip:
            continue

        # Replace as whole hyphen-delimited word
        # Handle start, middle, end, and standalone
        new_slug = re.sub(
            r'(?<![a-z])' + re.escape(old_word) + r'(?![a-z])',
            new_word,
            new_slug,
        )

    return new_slug


def find_content_files():
    """Find all .md files in content/."""
    files = []
    for root, _, filenames in os.walk(CONTENT_DIR):
        for fn in sorted(filenames):
            if fn.endswith(".md") and not fn.startswith("_"):
                files.append(os.path.join(root, fn))
    return sorted(files)


def get_frontmatter_field(text, field):
    """Extract a frontmatter field value."""
    m = re.search(rf'^{field}:\s*["\']?([^"\'\n]+)["\']?', text, re.MULTILINE)
    return m.group(1).strip() if m else None


def set_frontmatter_field(text, field, value):
    """Set a frontmatter field value, preserving quoting style."""
    def replacer(m):
        prefix = m.group(1)
        quote = m.group(2) or ""
        end_quote = m.group(4) or ""
        return f"{prefix}{quote}{value}{end_quote}"

    pattern = rf'^({field}:\s*)(["\']?)([^"\'\n]+)(["\']?)'
    return re.sub(pattern, replacer, text, count=1, flags=re.MULTILINE)


def update_links_in_file(filepath, rename_map):
    """Update internal .md links in a file based on rename map."""
    with open(filepath, "r") as f:
        content = f.read()

    original = content
    for old_filename, new_filename in rename_map.items():
        # Match markdown links: [text](path/old_filename.md) or [text](path/old_filename.md#anchor)
        content = content.replace(old_filename, new_filename)

    if content != original:
        with open(filepath, "w") as f:
            f.write(content)
        return True
    return False


def main():
    dry_run = "--dry-run" in sys.argv

    files = find_content_files()
    print(f"{'DRY RUN — ' if dry_run else ''}Scanning {len(files)} files for slug renames\n")

    # Phase 1: Build rename map
    rename_map = {}  # old_filename → new_filename
    file_renames = []  # (old_path, new_path, old_slug, new_slug)

    for filepath in files:
        with open(filepath, "r") as f:
            text = f.read()

        slug = get_frontmatter_field(text, "slug")
        if not slug:
            continue

        new_slug = rename_slug(slug)
        if new_slug == slug:
            continue

        old_filename = os.path.basename(filepath)
        new_filename = new_slug + ".md"
        new_path = os.path.join(os.path.dirname(filepath), new_filename)

        rename_map[old_filename] = new_filename
        file_renames.append((filepath, new_path, slug, new_slug))
        relpath = os.path.relpath(filepath, BASE)
        new_relpath = os.path.relpath(new_path, BASE)
        print(f"  RENAME: {relpath} → {new_relpath}")
        print(f"          slug: {slug} → {new_slug}")

    print(f"\n{len(file_renames)} files to rename\n")

    if not file_renames:
        print("Nothing to rename.")
        return

    if dry_run:
        # Show what links would be updated
        print("Links that would be updated:")
        for filepath in files:
            with open(filepath, "r") as f:
                content = f.read()
            for old_fn, new_fn in rename_map.items():
                if old_fn in content:
                    relpath = os.path.relpath(filepath, BASE)
                    print(f"  {relpath}: {old_fn} → {new_fn}")
        print("\nDRY RUN complete. Run without --dry-run to apply.")
        return

    # Phase 2: Update slug in frontmatter and rename files
    for old_path, new_path, old_slug, new_slug in file_renames:
        with open(old_path, "r") as f:
            text = f.read()

        text = set_frontmatter_field(text, "slug", new_slug)

        with open(old_path, "w") as f:
            f.write(text)

        os.rename(old_path, new_path)

    # Phase 3: Update all internal links in all content files
    # Re-scan because files have been renamed
    all_files = find_content_files()
    links_updated = 0
    for filepath in all_files:
        if update_links_in_file(filepath, rename_map):
            links_updated += 1
            relpath = os.path.relpath(filepath, BASE)
            print(f"  LINKS UPDATED: {relpath}")

    # Phase 4: Add redirects
    new_redirects = []
    for old_path, new_path, old_slug, new_slug in file_renames:
        # Determine product area from the file's directory for URL
        with open(new_path, "r") as f:
            text = f.read()
        product_area = get_frontmatter_field(text, "product_area")
        doc_type = get_frontmatter_field(text, "type")

        # Build URL paths
        if product_area:
            area_slug = product_area.lower().replace(" ", "-")
        else:
            area_slug = doc_type or "guides"

        old_url = f"/help/{area_slug}/{old_slug}"
        new_url = f"/help/{area_slug}/{new_slug}"

        new_redirects.append({
            "from": old_url,
            "to": new_url,
            "status": 301,
        })

    # Also update existing redirects that point to old slugs
    with open(REDIRECTS_PATH, "r") as f:
        redirects_text = f.read()

    for old_fn, new_fn in rename_map.items():
        old_slug = old_fn.replace(".md", "")
        new_slug = new_fn.replace(".md", "")
        # Update "to:" targets in redirects
        redirects_text = redirects_text.replace(f"/{old_slug}", f"/{new_slug}")

    # Append new redirects
    redirects_text += f"\n# Slug renames ({date.today().isoformat()})\n"
    for r in new_redirects:
        redirects_text += f'\n  - from: "{r["from"]}"\n    to: "{r["to"]}"\n    status: {r["status"]}\n'

    with open(REDIRECTS_PATH, "w") as f:
        f.write(redirects_text)

    print(f"\nDONE:")
    print(f"  {len(file_renames)} files renamed")
    print(f"  {links_updated} files with updated links")
    print(f"  {len(new_redirects)} redirects added to _redirects.yml")


if __name__ == "__main__":
    main()
