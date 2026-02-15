#!/usr/bin/env python3
"""Apply terminology normalization from dictionary.json to all content/*.md files."""

import json
import os
import re
import sys
from datetime import date

BASE = os.path.join(os.path.dirname(__file__), "..")
DICT_PATH = os.path.join(BASE, "build", "terminology", "dictionary.json")
CONTENT_DIR = os.path.join(BASE, "content")
LOG_PATH = os.path.join(BASE, "build", "terminology", "normalize-log.md")

# Additional preserve patterns (natural English, not Zooza terms)
GLOBAL_PRESERVE = [
    r"of course",
    r"Of course",
    r"of Course",  # just in case
    r"sign up",
    r"Sign up",
    r"Sign Up",
    r"signs up",
    r"signing up",
    r"signed up",
]


def load_dictionary():
    with open(DICT_PATH, "r") as f:
        return json.load(f)


def find_content_files():
    files = []
    for root, _, filenames in os.walk(CONTENT_DIR):
        for fn in sorted(filenames):
            if fn.endswith(".md") and not fn.startswith("_"):
                files.append(os.path.join(root, fn))
    return sorted(files)


def split_document(text):
    """Split document into frontmatter and body, preserving structure."""
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            end += 3
            return text[:end], text[end:]
    return "", text


def normalize_frontmatter_title(frontmatter, terms):
    """Apply terminology rules to the title field in frontmatter."""
    m = re.search(r'^(title:\s*["\']?)(.+?)(["\']?\s*)$', frontmatter, re.MULTILINE)
    if not m:
        return frontmatter, 0
    original_title = m.group(2)
    title = original_title
    count = 0
    for term_key, term_data in terms.items():
        for rule in term_data.get("replace_rules", []):
            pattern = rule["from"]
            replacement = rule["to"]
            new_title, n = re.subn(pattern, replacement, title)
            if n > 0:
                # Check global preserves
                skip = False
                for gp in GLOBAL_PRESERVE:
                    if gp in title:
                        skip = True
                        break
                if not skip:
                    title = new_title
                    count += n
    if title != original_title:
        frontmatter = frontmatter[:m.start(2)] + title + frontmatter[m.end(2):]
    return frontmatter, count


def protect_zones(body):
    """Find code blocks and inline code, return list of (start, end) ranges to skip."""
    zones = []
    # Fenced code blocks
    for m in re.finditer(r"```[\s\S]*?```", body):
        zones.append((m.start(), m.end()))
    # Inline code
    for m in re.finditer(r"`[^`\n]+`", body):
        zones.append((m.start(), m.end()))
    # Image references ![...](...)
    for m in re.finditer(r"!\[[^\]]*\]\([^)]*\)", body):
        zones.append((m.start(), m.end()))
    # Obsidian-style image references ![[...]]
    for m in re.finditer(r"!\[\[[^\]]*\]\]", body):
        zones.append((m.start(), m.end()))
    # Link URLs [text](URL) - protect just the URL part
    for m in re.finditer(r"\]\([^)]*\)", body):
        zones.append((m.start(), m.end()))
    return zones


def in_protected_zone(pos, match_len, zones):
    """Check if a position falls within any protected zone."""
    end = pos + match_len
    for zs, ze in zones:
        if pos >= zs and end <= ze:
            return True
        if pos < ze and end > zs:
            return True
    return False


def apply_rule(body, rule, zones):
    """Apply a single replacement rule. Returns (new_body, count)."""
    pattern = rule["from"]
    replacement = rule["to"]
    mode = rule.get("mode", "all")
    preserve_list = rule.get("preserve", [])

    count = 0
    # Find all matches
    matches = list(re.finditer(pattern, body))
    if not matches:
        return body, 0

    # Process in reverse order to maintain positions
    for m in reversed(matches):
        start, end = m.start(), m.end()

        # Skip if in protected zone
        if in_protected_zone(start, end - start, zones):
            continue

        # Smart mode: check if match is part of a preserved phrase
        if mode == "smart" and preserve_list:
            skip = False
            context_start = max(0, start - 50)
            context_end = min(len(body), end + 50)
            context = body[context_start:context_end]
            for phrase in preserve_list:
                # Find ALL occurrences of the phrase in context
                search_start = 0
                while True:
                    phrase_pos = context.find(phrase, search_start)
                    if phrase_pos == -1:
                        break
                    abs_phrase_start = context_start + phrase_pos
                    abs_phrase_end = abs_phrase_start + len(phrase)
                    if start >= abs_phrase_start and end <= abs_phrase_end:
                        skip = True
                        break
                    search_start = phrase_pos + 1
                if skip:
                    break
            if skip:
                continue

        # Check global preserves
        skip_global = False
        context_start = max(0, start - 20)
        context_end = min(len(body), end + 20)
        context = body[context_start:context_end]
        for gp in GLOBAL_PRESERVE:
            search_start = 0
            while True:
                gp_pos = context.find(gp, search_start)
                if gp_pos == -1:
                    break
                abs_gp_start = context_start + gp_pos
                abs_gp_end = abs_gp_start + len(gp)
                if start >= abs_gp_start and end <= abs_gp_end:
                    skip_global = True
                    break
                search_start = gp_pos + 1
            if skip_global:
                break
        if skip_global:
            continue

        body = body[:start] + replacement + body[end:]
        count += 1
        # Recalculate zones offset if replacement length differs
        diff = len(replacement) - (end - start)
        if diff != 0:
            zones = [(zs + diff if zs > start else zs, ze + diff if ze > start else ze) for zs, ze in zones]

    return body, count


def update_intercom_sync(frontmatter):
    """Set intercom_sync: true in frontmatter."""
    if "intercom_sync:" in frontmatter:
        return re.sub(r"intercom_sync:\s*(true|false)", "intercom_sync: true", frontmatter)
    elif "intercom_id:" in frontmatter:
        # Add intercom_sync after intercom_id
        return re.sub(
            r"(intercom_id:\s*\d+)",
            r"\1\nintercom_sync: true",
            frontmatter,
        )
    return frontmatter


def main():
    dry_run = "--dry-run" in sys.argv
    dictionary = load_dictionary()
    terms = dictionary.get("terms", {})
    files = find_content_files()

    print(f"{'DRY RUN — ' if dry_run else ''}Normalizing {len(files)} files with {len(terms)} term clusters\n")

    # Stats
    total_replacements = 0
    files_modified = 0
    files_skipped = 0
    replacements_by_rule = {}  # "from -> to" => {count, files}
    file_changes = {}  # filename => [(from, to, count)]
    review_items = []

    for filepath in files:
        with open(filepath, "r") as f:
            original = f.read()

        frontmatter, body = split_document(original)
        zones = protect_zones(body)

        file_replacements = []
        file_total = 0

        # Normalize title in frontmatter
        frontmatter, title_count = normalize_frontmatter_title(frontmatter, terms)
        if title_count > 0:
            file_total += title_count
            file_replacements.append(("title (frontmatter)", "normalized", title_count))

        for term_key, term_data in terms.items():
            rules = term_data.get("replace_rules", [])
            for rule in rules:
                new_body, count = apply_rule(body, rule, zones)
                if count > 0:
                    body = new_body
                    zones = protect_zones(body)  # Recalculate zones after changes
                    file_total += count

                    rule_key = f"{rule['from']} → {rule['to']}"
                    if rule_key not in replacements_by_rule:
                        replacements_by_rule[rule_key] = {"count": 0, "files": set()}
                    replacements_by_rule[rule_key]["count"] += count
                    replacements_by_rule[rule_key]["files"].add(os.path.basename(filepath))

                    file_replacements.append((rule["from"], rule["to"], count))

        if file_total > 0:
            relpath = os.path.relpath(filepath, BASE)
            filename = os.path.basename(filepath)
            file_changes[filename] = file_replacements
            files_modified += 1
            total_replacements += file_total

            if not dry_run:
                new_frontmatter = update_intercom_sync(frontmatter)
                with open(filepath, "w") as f:
                    f.write(new_frontmatter + body)

            print(f"  {'WOULD MODIFY' if dry_run else 'MODIFIED'}: {relpath} ({file_total} replacements)")
        else:
            files_skipped += 1

    # Write log
    log_lines = [
        "# Normalize Log\n",
        f"**Run:** {date.today().isoformat()}",
        f"**Mode:** {'DRY RUN' if dry_run else 'APPLIED'}",
        f"**Files scanned:** {len(files)}",
        f"**Files modified:** {files_modified}",
        f"**Total replacements:** {total_replacements}",
        f"**Skipped (already canonical):** {files_skipped}",
        "",
        "## Replacements by rule\n",
        "| From | To | Count | Files |",
        "|---|---|---|---|",
    ]

    for rule_key, data in sorted(replacements_by_rule.items(), key=lambda x: -x[1]["count"]):
        parts = rule_key.split(" → ")
        from_pat = parts[0].replace("\\b", "")
        to_term = parts[1]
        log_lines.append(f"| {from_pat} | {to_term} | {data['count']} | {len(data['files'])} files |")

    log_lines.append("")
    log_lines.append("## Modified files\n")

    for filename, changes in sorted(file_changes.items()):
        log_lines.append(f"### {filename}")
        for from_pat, to_term, count in changes:
            clean_from = from_pat.replace("\\b", "")
            log_lines.append(f"- `{clean_from}` → `{to_term}` ({count}x)")
        log_lines.append("")

    log_text = "\n".join(log_lines) + "\n"

    if not dry_run:
        os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
        with open(LOG_PATH, "w") as f:
            f.write(log_text)

        # Update dictionary with timestamp
        dictionary["last_normalized"] = date.today().isoformat()
        with open(DICT_PATH, "w") as f:
            json.dump(dictionary, f, indent=2, ensure_ascii=False)
            f.write("\n")

    print(f"\n{'DRY RUN SUMMARY' if dry_run else 'DONE'}:")
    print(f"  {files_modified} files modified, {total_replacements} total replacements")
    print(f"  {files_skipped} files skipped (already canonical)")
    if not dry_run:
        print(f"  Log written to {LOG_PATH}")


if __name__ == "__main__":
    main()
