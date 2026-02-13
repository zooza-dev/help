#!/usr/bin/env python3
"""Update YAML frontmatter in content/*.md files with Intercom article IDs."""

import os
import re
from pathlib import Path

CONTENT_DIR = Path("/Users/michaldodok/help/content")

# Title -> Intercom ID mapping from deploy log
TITLE_ID_MAP = {
    "Attendance and Catch-up Classes FAQ": 13727552,
    "Common Booking Scenarios": 13727556,
    "Discounts and Sibling Pricing FAQ": 13727557,
    "Email and Communication FAQ": 13727558,
    "Instructor Access and Roles FAQ": 13727559,
    "Locations and Venues FAQ": 13727560,
    "Onboarding and Launch FAQ": 13727561,
    "Parent Portal FAQ": 13727562,
    "Payments and Billing FAQ": 13727564,
    "Programmes, Timetables and Sessions FAQ": 13727565,
    "Registration and Booking FAQ": 13727566,
    "Stripe Integration FAQ": 13727567,
    "Trial Classes FAQ": 13727568,
    "Orders": 13727720,
    "Payments": 13727722,
    "Products": 13727723,
    "Programme Automations": 13727727,
    "Programme Settings": 13727729,
    "Programmes List": 13727731,
    "Publish (Widgets)": 13727735,
    "Reports": 13727736,
    "Services": 13727737,
    "Sessions List": 13727738,
    "Settings": 13727739,
    "Abra Flexi Invoice Management System": 13727741,
    "Add the Zooza app to your phone\u2019s desktop": 13727742,
    "Add the Zooza app to your phone's desktop": 13727742,
    "Auto-enrollment": 13727745,
    "Setting up billing periods": 13727749,
    "Collecting the reason for cancelling the lesson": 13727750,
    "Company logo in email communication": 13727752,
    "Deploying Zooza app on your website": 13727754,
    "Getting Started with Zooza": 13727756,
    "Holiday settings": 13727757,
    "Setting the rate/reward for instuctors": 13727760,
    "Lecturers working hours": 13727762,
    "Online registration": 13727765,
    "Power BI integration": 13727770,
    "Setting GTC, GDPR and other consents": 13727771,
    "Smartbill - invoice management": 13727773,
    "Szamlazz Invoice Management": 13727774,
    "Trial lessons": 13727779,
    "WhatsApp Integration & Usage (Beta)": 13727781,
    "Xero Integration in Zooza: Setup & Invoice Management": 13727782,
    "Zooza Sites": 13727785,
    "Receiving e-mails from Zooza in Primary Inbox": 13727787,
    "How to Clear Your Cache": 13727788,
    "WhatsApp troubleshooting": 13727789,
}

# Track results
updated = []
already_up_to_date = []
unmatched_files = []
unmatched_mappings = set(TITLE_ID_MAP.keys())
id_assignments = {}  # id -> list of files


def extract_frontmatter_title(text):
    """Extract the title from YAML frontmatter."""
    m = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if not m:
        return None
    fm = m.group(1)
    tm = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
    if tm:
        return tm.group(1)
    return None


def update_frontmatter(text, intercom_id):
    """Update or add intercom_id and intercom_sync in frontmatter."""
    m = re.match(r'^(---\s*\n)(.*?)(\n---)', text, re.DOTALL)
    if not m:
        return text, False

    prefix = m.group(1)
    fm = m.group(2)
    suffix = m.group(3)
    body = text[m.end():]

    changed = False

    # Handle intercom_id
    id_pattern = re.compile(r'^intercom_id:\s*.*$', re.MULTILINE)
    if id_pattern.search(fm):
        old = id_pattern.search(fm).group(0)
        new_line = f"intercom_id: {intercom_id}"
        if old.strip() != new_line:
            fm = id_pattern.sub(new_line, fm)
            changed = True
    else:
        fm += f"\nintercom_id: {intercom_id}"
        changed = True

    # Handle intercom_sync
    sync_pattern = re.compile(r'^intercom_sync:\s*.*$', re.MULTILINE)
    if sync_pattern.search(fm):
        old = sync_pattern.search(fm).group(0)
        new_line = "intercom_sync: false"
        if old.strip() != new_line:
            fm = sync_pattern.sub(new_line, fm)
            changed = True
    else:
        fm += "\nintercom_sync: false"
        changed = True

    return prefix + fm + suffix + body, changed


def main():
    md_files = []
    for root, dirs, files in os.walk(CONTENT_DIR):
        dirs[:] = [d for d in dirs if d != '_shared']
        for f in files:
            if f.endswith('.md') and not f.startswith('_'):
                md_files.append(Path(root) / f)

    md_files.sort()

    for fpath in md_files:
        text = fpath.read_text(encoding='utf-8')
        title = extract_frontmatter_title(text)
        if not title:
            continue

        if title in TITLE_ID_MAP:
            iid = TITLE_ID_MAP[title]
            unmatched_mappings.discard(title)
            # Also discard the alternate apostrophe variant
            if title == "Add the Zooza app to your phone\u2019s desktop":
                unmatched_mappings.discard("Add the Zooza app to your phone's desktop")
            elif title == "Add the Zooza app to your phone's desktop":
                unmatched_mappings.discard("Add the Zooza app to your phone\u2019s desktop")

            id_assignments.setdefault(iid, []).append(str(fpath))

            new_text, changed = update_frontmatter(text, iid)
            if changed:
                fpath.write_text(new_text, encoding='utf-8')
                updated.append((str(fpath), title, iid))
            else:
                already_up_to_date.append((str(fpath), title, iid))
        else:
            unmatched_files.append((str(fpath), title))

    # Print report
    print("=" * 70)
    print("INTERCOM ID UPDATE REPORT")
    print("=" * 70)

    print(f"\nFiles updated: {len(updated)}")
    for fpath, title, iid in updated:
        print(f"  {iid}  {title}")
        print(f"         {fpath}")

    print(f"\nAlready up to date: {len(already_up_to_date)}")
    for fpath, title, iid in already_up_to_date:
        print(f"  {iid}  {title}")

    print(f"\nUnmatched mappings (no file found): {len(unmatched_mappings)}")
    for title in sorted(unmatched_mappings):
        print(f"  - {title}")

    print(f"\nContent files without mapping: {len(unmatched_files)}")
    for fpath, title in unmatched_files:
        rel = str(Path(fpath).relative_to(CONTENT_DIR))
        print(f"  {rel}: {title}")

    # Duplicate ID check
    dupes = {k: v for k, v in id_assignments.items() if len(v) > 1}
    if dupes:
        print(f"\nDUPLICATE ID WARNINGS: {len(dupes)}")
        for iid, files in dupes.items():
            print(f"  ID {iid} assigned to:")
            for f in files:
                print(f"    - {f}")
    else:
        print("\nNo duplicate IDs detected.")

    print()


if __name__ == "__main__":
    main()
