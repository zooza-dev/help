#!/usr/bin/env python3
"""
Fix generic alt text in Markdown articles.
Replaces ![Screenshot](...) and other generic alts with context-derived descriptions.
Uses the nearest heading + preceding text to build a meaningful alt string.

Usage:
  python3 scripts/fix_alt_text.py            # process all fixable articles
  python3 scripts/fix_alt_text.py --dry-run  # preview changes only
  python3 scripts/fix_alt_text.py content/setup/trial-sessions.md  # single file
"""

import re
import sys
import textwrap
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
CONTENT_DIR = REPO_ROOT / "content"

GENERIC_ALTS = {
    "screenshot",
    "add item",
    "image",
    "img",
    "",
}

# Max chars for generated alt text
ALT_MAX = 90


def is_generic(alt: str) -> bool:
    return alt.strip().lower() in GENERIC_ALTS


def slugify_filename(name: str) -> str:
    """trial-lessons-04 -> trial lessons"""
    # Strip trailing number(s)
    name = re.sub(r"-\d+$", "", name)
    return name.replace("-", " ").strip()


def extract_context(lines: list[str], img_line_idx: int) -> dict:
    """Return nearest heading and preceding sentence/list-item for an image line."""
    heading = ""
    preceding = ""

    # Walk backwards to find heading and last meaningful text line
    for i in range(img_line_idx - 1, -1, -1):
        line = lines[i].strip()

        # Skip blank lines and other images
        if not line or line.startswith("!["):
            continue

        # Capture nearest heading (first one we hit going backwards)
        if re.match(r"^#{1,3}\s", line):
            heading = re.sub(r"^#+\s*", "", line).strip()
            break

        # Capture the last non-empty, non-heading text line as preceding context
        if not preceding and not line.startswith("|") and not line.startswith("---"):
            preceding = line

    return {"heading": heading, "preceding": preceding}


def build_alt(ctx: dict, filename_stem: str) -> str:
    """Build a concise, descriptive alt string from context."""
    heading = ctx["heading"]
    preceding = ctx["preceding"]

    # Strip markdown bold/italic/code from preceding
    preceding_clean = re.sub(r"[*_`]", "", preceding)
    # Strip inline markdown links [label](url) → label
    preceding_clean = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", preceding_clean)
    # Strip any remaining ](...) fragments (link continuations spanning lines)
    preceding_clean = re.sub(r"\]\([^)]*\)", "", preceding_clean)
    # Remove list markers: "1.", "-", "*"
    preceding_clean = re.sub(r"^\s*(\d+\.|[-*])\s*", "", preceding_clean).strip()
    # Remove blockquote markers
    preceding_clean = re.sub(r"^>+\s*", "", preceding_clean).strip()
    # Remove leading Note:, Tip:, etc.
    preceding_clean = re.sub(r"^(Note|Tip|Warning|Important):\s*", "", preceding_clean, flags=re.IGNORECASE).strip()
    # Remove leading parentheses (fragment starts)
    preceding_clean = preceding_clean.lstrip("([").strip()
    # Strip trailing punctuation and brackets
    preceding_clean = preceding_clean.rstrip(".,;:([")

    # Use preceding text if it's long enough to be meaningful
    if len(preceding_clean) >= 20:
        alt = preceding_clean
    elif heading:
        alt = heading
    else:
        # Fallback: readable filename
        alt = slugify_filename(filename_stem).capitalize()

    # Trim to ALT_MAX chars at a word boundary
    if len(alt) > ALT_MAX:
        alt = textwrap.shorten(alt, width=ALT_MAX, placeholder="...")

    return alt.strip()


def process_file(path: Path, dry_run: bool = False) -> int:
    """Fix generic alt text in one file. Returns number of replacements made."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    changes = 0

    new_lines = []
    for idx, line in enumerate(lines):
        # Match: ![<anything>](../../assets/images/<filename>)
        match = re.match(
            r'^(.*?)'                          # leading text
            r'!\[([^\]]*)\]'                   # alt text
            r'\((../../assets/images/([^)]+))\)'  # path + filename
            r'(.*)',                            # trailing text (title etc)
            line.rstrip("\n")
        )
        if match and is_generic(match.group(2)):
            prefix = match.group(1)
            full_path = match.group(3)
            filename = match.group(4)
            suffix = match.group(5)

            stem = Path(filename).stem
            ctx = extract_context([l.rstrip("\n") for l in lines], idx)
            new_alt = build_alt(ctx, stem)

            new_line = f'{prefix}![{new_alt}]({full_path}){suffix}\n'
            new_lines.append(new_line)
            changes += 1

            if dry_run:
                print(f"  [{path.relative_to(REPO_ROOT)}:{idx+1}]")
                print(f"    OLD: ![{match.group(2)}]")
                print(f"    NEW: ![{new_alt}]")
        else:
            new_lines.append(line if line.endswith("\n") else line + "\n")

    if not dry_run and changes:
        path.write_text("".join(new_lines), encoding="utf-8")

    return changes


def get_fixable_articles() -> list[Path]:
    """Articles with generic alt text but NOT pending screenshot replacement."""
    fixable = []
    for md in sorted(CONTENT_DIR.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        # Skip if needs_screenshot_replacement: true
        fm_match = re.search(r"needs_screenshot_replacement:\s*(true|false)", text)
        if fm_match and fm_match.group(1) == "true":
            continue
        # Skip archived/draft
        status_match = re.search(r"\bstatus:\s*\"?(published|archived|draft)\"?", text)
        if status_match and status_match.group(1) != "published":
            continue
        # Include if it has generic alt text on an image
        if re.search(r'!\[(Screenshot|Add item|Image|Img|)\]\(../../assets/images/', text, re.IGNORECASE):
            fixable.append(md)
    return fixable


def main():
    dry_run = "--dry-run" in sys.argv
    targets = [Path(a) for a in sys.argv[1:] if not a.startswith("--")]

    if not targets:
        targets = get_fixable_articles()

    total = 0
    for path in targets:
        count = process_file(path, dry_run=dry_run)
        if count:
            verb = "Would fix" if dry_run else "Fixed"
            print(f"{verb}: {count:3d} images  {path.relative_to(REPO_ROOT)}")
            total += count

    print(f"\n{'Would replace' if dry_run else 'Replaced'}: {total} generic alt texts across {len([p for p in targets if process_file(p, dry_run=True) > 0] if dry_run else [])} articles")
    if not dry_run and total:
        print("Run export_all.py to regenerate exports.")


if __name__ == "__main__":
    main()
