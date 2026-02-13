#!/usr/bin/env python3
"""Update content frontmatter and intercom-map.json with new Intercom article IDs."""

import os
import re
import json
from pathlib import Path

CONTENT_DIR = Path("/Users/michaldodok/help/content")
MAP_FILE = Path("/Users/michaldodok/help/build/exports/targets/intercom/intercom-map.json")

ARTICLE_MAPPINGS = {
    "Attendance and Catch-up Classes FAQ": 13728486,
    "Common Booking Scenarios": 13728488,
    "Discounts and Sibling Pricing FAQ": 13728489,
    "Email and Communication FAQ": 13728490,
    "Instructor Access and Roles FAQ": 13728491,
    "Locations and Venues FAQ": 13728492,
    "Onboarding and Launch FAQ": 13728493,
    "Parent Portal FAQ": 13728494,
    "Payments and Billing FAQ": 13728495,
    "Programmes, Timetables and Sessions FAQ": 13728496,
    "Registration and Booking FAQ": 13728498,
    "Stripe Integration FAQ": 13728499,
    "Trial Classes FAQ": 13728500,
    "Orders": 13728664,
    "Payments": 13728665,
    "Products": 13728668,
    "Programme Automations": 13728686,
    "Programme Settings": 13728705,
    "Programmes List": 13728714,
    "Publish (Widgets)": 13728723,
    "Reports": 13728729,
    "Services": 13728738,
    "Sessions List": 13728741,
    "Settings": 13728746,
    "Abra Flexi Invoice Management System": 13728755,
    "Add the Zooza app to your phone's desktop": 13728760,
    "Auto-enrollment": 13728767,
    "Setting up billing periods": 13728773,
    "Collecting the reason for cancelling the lesson": 13728777,
    "Company logo in email communication": 13728781,
    "Deploying Zooza app on your website": 13728789,
    "Getting Started with Zooza": 13728795,
    "Holiday settings": 13728800,
    "Setting the rate/reward for instuctors": 13728816,
    "Lecturers working hours": 13728824,
    "Online registration": 13728839,
    "Power BI integration": 13728862,
    "Setting GTC, GDPR and other consents": 13728871,
    "Smartbill - invoice management": 13728879,
    "Szamlazz Invoice Management": 13728889,
    "Trial lessons": 13728913,
    "WhatsApp Integration & Usage (Beta)": 13728920,
    "Xero Integration in Zooza: Setup & Invoice Management": 13728935,
    "Zooza Sites": 13728943,
    "Receiving e-mails from Zooza in Primary Inbox": 13728947,
    "How to Clear Your Cache": 13728949,
    "WhatsApp troubleshooting": 13728951,
}

COLLECTION_MAPPINGS = {
    "Calendar": 18457477,
    "Bookings": 18438525,
    "Payments": 18438531,
    "Communication": 18427319,
    "Settings": 18438536,
    "Widgets": 18438544,
    "Programmes": 18438540,
}

# Log order: collections and sections interleaved
LOG_ORDER = [
    ("collection", "Calendar", 18457477),
    ("section", "Faq", 18457478),
    ("collection", "Bookings", 18438525),
    ("section", "Faq", 18438526),
    ("collection", "Payments", 18438531),
    ("section", "Faq", 18457480),
    ("collection", "Communication", 18427319),
    ("section", "Faq", 18427355),
    ("collection", "Settings", 18438536),
    ("section", "Faq", 18457485),
    ("collection", "Widgets", 18438544),
    ("section", "Faq", 18457486),
    ("collection", "Programmes", 18438540),
    ("section", "Faq", 18457490),
    ("section", "Reference", 18458137),
    ("section", "Reference", 18458144),
    ("section", "Reference", 18458186),
    ("section", "Setup", 18458195),
    ("section", "Setup", 18458202),
    ("section", "Setup", 18458204),
    ("section", "Setup", 18458209),
    ("section", "Setup", 18427970),
    ("section", "Setup", 18458213),
    ("section", "Setup", 18458217),
    ("section", "Troubleshooting", 18458246),
    ("section", "Troubleshooting", 18427971),
]

# Build section mappings from log order (each section belongs to most recently seen collection)
SECTION_MAPPINGS = []
current_collection_id = None
for entry in LOG_ORDER:
    if entry[0] == "collection":
        current_collection_id = entry[2]
    elif entry[0] == "section":
        SECTION_MAPPINGS.append((current_collection_id, entry[1], entry[2]))


def parse_frontmatter(content):
    """Parse YAML frontmatter. Returns (fm_str, body_str, metadata_dict)."""
    match = re.match(r'^---\n(.*?)\n---\n?(.*)', content, re.DOTALL)
    if not match:
        return None, content, {}
    fm_str = match.group(1)
    body = match.group(2)
    metadata = {}
    for line in fm_str.split('\n'):
        m = re.match(r'^title:\s*["\']?(.*?)["\']?\s*$', line)
        if m:
            metadata['title'] = m.group(1)
        m = re.match(r'^slug:\s*["\']?(.*?)["\']?\s*$', line)
        if m:
            metadata['slug'] = m.group(1)
    return fm_str, body, metadata


def update_frontmatter(fm_str, intercom_id):
    """Add or update intercom_id and intercom_sync in frontmatter."""
    lines = fm_str.split('\n')
    new_lines = [l for l in lines
                 if not re.match(r'^intercom_id:', l) and not re.match(r'^intercom_sync:', l)]
    new_lines.append(f'intercom_id: {intercom_id}')
    new_lines.append('intercom_sync: false')
    return '\n'.join(new_lines)


def main():
    md_files = []
    for root, dirs, files in os.walk(CONTENT_DIR):
        rel = os.path.relpath(root, CONTENT_DIR)
        parts = Path(rel).parts
        if any(p.startswith('_') for p in parts):
            continue
        for f in files:
            if f.endswith('.md'):
                md_files.append(os.path.join(root, f))
    md_files.sort()

    files_updated = []
    files_already_ok = []
    unmatched_articles = set(ARTICLE_MAPPINGS.keys())
    article_map = {}

    for filepath in md_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        fm_str, body, metadata = parse_frontmatter(content)
        if fm_str is None:
            continue

        title = metadata.get('title', '')
        slug = metadata.get('slug', '')

        if title in ARTICLE_MAPPINGS:
            intercom_id = ARTICLE_MAPPINGS[title]
            unmatched_articles.discard(title)

            has_correct_id = f'intercom_id: {intercom_id}' in fm_str
            has_sync_false = 'intercom_sync: false' in fm_str

            if has_correct_id and has_sync_false:
                files_already_ok.append(filepath)
                if slug:
                    article_map[slug] = intercom_id
                continue

            new_fm = update_frontmatter(fm_str, intercom_id)
            new_content = f'---\n{new_fm}\n---\n{body}'

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

            files_updated.append(filepath)
            if slug:
                article_map[slug] = intercom_id

    # Build intercom-map.json
    intercom_map = {"collections": {}, "sections": {}, "articles": {}}

    for name, cid in sorted(COLLECTION_MAPPINGS.items()):
        intercom_map["collections"][name] = cid

    for parent_id, section_name, section_id in SECTION_MAPPINGS:
        key = f"{parent_id}:{section_name}"
        intercom_map["sections"][key] = section_id

    for slug in sorted(article_map.keys()):
        intercom_map["articles"][slug] = article_map[slug]

    with open(MAP_FILE, 'w', encoding='utf-8') as f:
        json.dump(intercom_map, f, indent=2, sort_keys=False)
        f.write('\n')

    # Summary
    print("=" * 60)
    print("INTERCOM ID UPDATE SUMMARY")
    print("=" * 60)

    print(f"\nFiles updated: {len(files_updated)}")
    for fp in files_updated:
        print(f"  {fp}")

    print(f"\nFiles already up to date: {len(files_already_ok)}")
    for fp in files_already_ok:
        print(f"  {fp}")

    print(f"\nUnmatched article titles (no matching .md file): {len(unmatched_articles)}")
    for t in sorted(unmatched_articles):
        print(f"  - {t}")

    print(f"\nintercom-map.json entries:")
    print(f"  Collections: {len(COLLECTION_MAPPINGS)}")
    print(f"  Sections:    {len(SECTION_MAPPINGS)}")
    print(f"  Articles:    {len(article_map)}")
    print(f"\nDone.")


if __name__ == "__main__":
    main()
