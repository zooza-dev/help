#!/usr/bin/env python3
"""Extract Zooza terminology dictionary from content/ Markdown files."""

import re
import os
import json
import glob
from collections import defaultdict, Counter
from datetime import date

CONTENT_DIR = "content"
OUTPUT_DIR = "build/terminology"

# Known synonym clusters: canonical -> [variants]
SYNONYM_CLUSTERS = {
    "programme": ["course"],
    "class": ["group", "timetable"],
    "session": ["event", "lesson"],
    "booking": ["registration"],
    "client": ["customer"],
    "instructor": ["lecturer", "teacher", "tutor", "trainer"],
    "make-up session": ["replacement lesson", "catch-up lesson", "make-up lesson"],
    "Client Profile": ["Parent Portal", "Parent Zone", "Parent Profile", "parent portal"],
    "payment template": ["payment plan"],
    "billing period": ["term"],
    "trial": ["guest"],
    "log in": ["sign in"],
    "cancel session": ["sign out", "unregister", "unsubscribe"],
    "booking form": ["registration form"],
    "lead collection": ["group interested", "collecting basket", "interest group"],
    "Pay-as-you-go": ["open course", "open programme", "open booking"],
    "linked classes": ["group connection", "class connection"],
    "entry pass": ["voucher", "season pass", "season ticket", "permanent pass", "punch card"],
    "Cancelled": ["Unsubscribed", "unsubscribed"],
}

# Build reverse lookup: variant -> canonical
VARIANT_TO_CANONICAL = {}
for canonical, variants in SYNONYM_CLUSTERS.items():
    VARIANT_TO_CANONICAL[canonical.lower()] = canonical
    for v in variants:
        VARIANT_TO_CANONICAL[v.lower()] = canonical

# Category hints
CATEGORY_HINTS = {
    "programme": "core_concept", "class": "core_concept", "session": "core_concept",
    "booking": "core_concept", "client": "core_concept",
    "instructor": "role", "admin": "role", "Class King": "role",
    "trial": "status", "waitlist": "status", "cancelled": "status",
    "active": "status", "deleted": "status", "valid": "status",
    "payment plan": "payment", "billing period": "payment",
    "outstanding amount": "payment", "discount": "payment", "refund": "payment",
    "invoice": "payment", "VAT": "payment", "direct debit": "payment",
    "Parent Zone": "ui_element", "dashboard": "ui_element", "widget": "ui_element",
    "make-up session": "core_concept",
    "log in": "action", "cancel session": "action",
    "booking form": "ui_element",
    "lead collection": "core_concept",
    "Pay-as-you-go": "core_concept",
    "linked classes": "core_concept",
    "entry pass": "core_concept",
    "Cancelled": "ui_element",
    "Client Profile": "ui_element",
    "GoCardless": "integration", "Stripe": "integration", "Xero": "integration",
    "Power BI": "integration", "Abra Flexi": "integration", "Szamlazz": "integration",
    "SmartBill": "integration",
}

# Words to search for (case-insensitive variants)
SEARCH_TERMS = set()
for canonical, variants in SYNONYM_CLUSTERS.items():
    SEARCH_TERMS.add(canonical.lower())
    for v in variants:
        SEARCH_TERMS.add(v.lower())

# Additional Zooza-specific terms to track
EXTRA_TERMS = [
    "programme", "class", "session", "booking", "registration", "client", "customer",
    "instructor", "lecturer", "teacher", "tutor", "trainer",
    "course", "group", "timetable", "event", "lesson",
    "payment plan", "payment template", "payment schedule",
    "billing period", "term fee",
    "trial", "guest", "waitlist", "waiting list",
    "make-up session", "make-up lesson", "replacement lesson", "catch-up lesson", "make-up class",
    "Client Profile", "Parent Zone", "parent portal", "Parent Portal", "Parent Profile",
    "admin", "Class King",
    "GoCardless", "Stripe", "Xero", "Power BI", "Abra Flexi", "SmartBill", "Szamlazz",
    "widget", "dashboard", "calendar",
    "direct debit", "bank transfer", "refund", "invoice",
    "outstanding amount", "discount", "discount code", "VAT",
    "attendance", "capacity", "enrol", "enroll", "register", "cancel",
    "notification", "reminder", "template",
    "persona", "extra field", "custom field",
    "block", "semester",
    "log in", "sign in", "login",
    "cancel session", "sign out", "unregister", "unsubscribe",
    "booking form", "registration form",
    "lead collection", "group interested", "collecting basket", "interest group",
    "Pay-as-you-go", "open course", "open programme", "open booking",
    "linked classes", "group connection", "class connection",
    "entry pass", "voucher", "season pass", "season ticket", "permanent pass", "punch card",
]


def strip_frontmatter(content):
    """Remove YAML frontmatter."""
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            return content[end + 3:]
    return content


def strip_images(content):
    """Remove image references."""
    return re.sub(r'!\[[^\]]*\]\([^)]*\)', '', content)


def extract_bold_terms(content):
    """Extract **bold** terms."""
    return re.findall(r'\*\*([^*]+)\*\*', content)


def extract_code_terms(content):
    """Extract `code` terms."""
    return re.findall(r'`([^`]+)`', content)


def extract_headings(content):
    """Extract H1/H2/H3 text."""
    return re.findall(r'^#{1,3}\s+(.+)$', content, re.MULTILINE)


def count_term(text, term):
    """Count case-insensitive whole-word occurrences of term in text."""
    # For multi-word terms, just do case-insensitive search
    pattern = r'\b' + re.escape(term) + r'(?:s|es)?\b'
    return len(re.findall(pattern, text, re.IGNORECASE))


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Collect all content files
    md_files = sorted(glob.glob(f"{CONTENT_DIR}/**/*.md", recursive=True))
    md_files = [f for f in md_files if "/_shared/" not in f and not f.endswith("_redirects.yml")]

    # Per-file data
    file_texts = {}
    file_bold = {}
    file_code = {}
    file_headings = {}

    for fpath in md_files:
        with open(fpath) as f:
            raw = f.read()
        text = strip_images(strip_frontmatter(raw))
        slug = os.path.basename(fpath).replace(".md", "")
        file_texts[slug] = text
        file_bold[slug] = extract_bold_terms(text)
        file_code[slug] = extract_code_terms(text)
        file_headings[slug] = extract_headings(text)

    # Track all terms: term_key -> {occurrences, files, is_bold, is_code, is_heading}
    term_data = defaultdict(lambda: {
        "occurrences": 0,
        "files": set(),
        "bold_count": 0,
        "code_count": 0,
        "heading_count": 0,
    })

    all_terms = set(t.lower() for t in EXTRA_TERMS)

    for term in all_terms:
        for slug, text in file_texts.items():
            count = count_term(text, term)
            if count > 0:
                term_data[term]["occurrences"] += count
                term_data[term]["files"].add(slug)

            # Check bold
            for bt in file_bold[slug]:
                if term.lower() in bt.lower():
                    term_data[term]["bold_count"] += 1

            # Check code
            for ct in file_code[slug]:
                if term.lower() in ct.lower():
                    term_data[term]["code_count"] += 1

            # Check headings
            for ht in file_headings[slug]:
                if term.lower() in ht.lower():
                    term_data[term]["heading_count"] += 1

    # Build dictionary
    dictionary = {"terms": {}, "extracted_at": str(date.today()), "source_file_count": len(md_files)}

    # Process synonym clusters
    cluster_stats = {}  # canonical -> {variant -> {count, files}}
    for canonical, variants in SYNONYM_CLUSTERS.items():
        all_variants = [canonical.lower()] + [v.lower() for v in variants]
        cluster_stats[canonical] = {}
        for v in all_variants:
            if v in term_data and term_data[v]["occurrences"] > 0:
                cluster_stats[canonical][v] = {
                    "count": term_data[v]["occurrences"],
                    "files": sorted(term_data[v]["files"]),
                }

    # Add clustered terms to dictionary
    for canonical, variants_data in cluster_stats.items():
        if not variants_data:
            continue
        all_files = set()
        total_occ = 0
        found_variants = []
        for v, vdata in variants_data.items():
            found_variants.append(v)
            total_occ += vdata["count"]
            all_files.update(vdata["files"])

        category = CATEGORY_HINTS.get(canonical, "core_concept")
        dictionary["terms"][canonical] = {
            "canonical": canonical,
            "variants_found": sorted(found_variants),
            "occurrences": total_occ,
            "files": sorted(all_files)[:20],  # Cap at 20 for readability
            "file_count": len(all_files),
            "category": category,
            "context": "both",
            "notes": "",
        }

    # Add non-clustered terms
    clustered_terms = set()
    for canonical, variants in SYNONYM_CLUSTERS.items():
        clustered_terms.add(canonical.lower())
        for v in variants:
            clustered_terms.add(v.lower())

    for term, data in sorted(term_data.items()):
        if term in clustered_terms:
            continue
        if data["occurrences"] == 0:
            continue
        category = "unknown"
        for hint_term, hint_cat in CATEGORY_HINTS.items():
            if term.lower() == hint_term.lower():
                category = hint_cat
                break

        dictionary["terms"][term] = {
            "canonical": term,
            "variants_found": [term],
            "occurrences": data["occurrences"],
            "files": sorted(data["files"])[:20],
            "file_count": len(data["files"]),
            "category": category,
            "context": "both",
            "notes": "",
            "found_in_bold": data["bold_count"],
            "found_in_code": data["code_count"],
            "found_in_headings": data["heading_count"],
        }

    # Write dictionary
    with open(f"{OUTPUT_DIR}/dictionary.json", "w") as f:
        json.dump(dictionary, f, indent=2)

    # Generate inconsistency report
    lines = ["# Terminology Inconsistencies", "",
             f"**Extracted:** {date.today()}", f"**Files scanned:** {len(md_files)}", ""]

    # Summary
    total_terms = len(dictionary["terms"])
    cluster_count = len([c for c in cluster_stats if cluster_stats[c]])
    mixed_files = set()

    for canonical, variants_data in cluster_stats.items():
        if len(variants_data) > 1:
            for v, vdata in variants_data.items():
                for f in vdata["files"]:
                    # Check if this file uses multiple variants
                    file_variants = [vv for vv, vvd in variants_data.items() if f in vvd["files"]]
                    if len(file_variants) > 1:
                        mixed_files.add(f)

    unknown_terms = [t for t, d in dictionary["terms"].items() if d.get("category") == "unknown"]

    lines.append("## Summary")
    lines.append(f"- Total terms extracted: {total_terms}")
    lines.append(f"- Synonym clusters: {cluster_count}")
    lines.append(f"- Files with mixed terminology: {len(mixed_files)}")
    lines.append(f"- New/unknown terms for review: {len(unknown_terms)}")
    lines.append("")

    # Variant frequency table
    lines.append("## Variant frequency")
    lines.append("")
    lines.append("| Canonical | Variant | Count | Files |")
    lines.append("|---|---|---|---|")
    for canonical, variants_data in sorted(cluster_stats.items()):
        for v, vdata in sorted(variants_data.items(), key=lambda x: -x[1]["count"]):
            is_canonical = " *" if v == canonical.lower() else ""
            lines.append(f"| {canonical} | {v}{is_canonical} | {vdata['count']} | {len(vdata['files'])} files |")
    lines.append("")

    # Mixed usage by file
    lines.append("## Mixed usage by file")
    lines.append("")
    for slug in sorted(mixed_files):
        lines.append(f"### {slug}.md")
        for canonical, variants_data in sorted(cluster_stats.items()):
            file_variants = {vv: vvd for vv, vvd in variants_data.items() if slug in vvd["files"]}
            if len(file_variants) > 1:
                parts = []
                for vv, vvd in file_variants.items():
                    # Recount for this specific file
                    cnt = count_term(file_texts[slug], vv)
                    parts.append(f'"{vv}" ({cnt}x)')
                lines.append(f"- Uses {' and '.join(parts)} — canonical: **{canonical}**")
        lines.append("")

    # Top terms by frequency
    lines.append("## Top terms by frequency")
    lines.append("")
    lines.append("| Term | Category | Occurrences | Files |")
    lines.append("|---|---|---|---|")
    sorted_terms = sorted(dictionary["terms"].items(), key=lambda x: -x[1]["occurrences"])
    for term, data in sorted_terms[:40]:
        lines.append(f"| {data['canonical']} | {data.get('category', '?')} | {data['occurrences']} | {data['file_count']} |")
    lines.append("")

    # Unknown terms
    if unknown_terms:
        lines.append("## Unknown terms (need review)")
        lines.append("")
        for t in sorted(unknown_terms):
            d = dictionary["terms"][t]
            sample_files = ", ".join(d["files"][:3])
            lines.append(f"- **{t}** ({d['occurrences']}x in {d['file_count']} files) — e.g. {sample_files}")
        lines.append("")

    with open(f"{OUTPUT_DIR}/inconsistencies.md", "w") as f:
        f.write("\n".join(lines))

    # Print summary
    print(f"Terms extracted: {total_terms}")
    print(f"Synonym clusters with data: {cluster_count}")
    print(f"Files with mixed terminology: {len(mixed_files)}")
    print(f"Unknown terms: {len(unknown_terms)}")
    print(f"\nOutput: {OUTPUT_DIR}/dictionary.json")
    print(f"Report: {OUTPUT_DIR}/inconsistencies.md")


if __name__ == "__main__":
    main()
