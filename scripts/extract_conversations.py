#!/usr/bin/env python3
"""
Extract, filter, and anonymize Zoho support conversations for KB gap analysis.

Filters: Oct 2025+ tickets, excludes bugs.
Strips HTML, removes PII, outputs clean JSONL.
"""

import csv
import json
import re
import sys
import os
from html.parser import HTMLParser
from datetime import datetime
from collections import defaultdict

csv.field_size_limit(sys.maxsize)

INGEST_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'help_ingest')
CASES_CSV = os.path.join(INGEST_DIR, 'Cases__1 7.csv')
THREADS_CSV = os.path.join(INGEST_DIR, 'zoho_threads', 'Threads__2.csv')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'build', 'reports')

DATE_CUTOFF = '2025-10-01'

BUG_CLASSIFICATIONS = [
    'Bug ::',
    'Bug::',
]

# PII patterns
EMAIL_RE = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')
PHONE_RE = re.compile(r'(?:\+?\d{1,4}[\s-]?)?\(?\d{1,4}\)?[\s-]?\d{2,4}[\s-]?\d{2,4}[\s-]?\d{0,4}')
# Common Zooza team emails to keep
ZOOZA_EMAILS = {'support@zooza.online', 'katka@zooza.online', 'info@zooza.online',
                'support@zooza.zohodesk.com', 'hello@zooza.online'}


class HTMLTextExtractor(HTMLParser):
    """Strip HTML tags, keep text content."""
    def __init__(self):
        super().__init__()
        self.result = []
        self.skip = False

    def handle_starttag(self, tag, attrs):
        if tag in ('style', 'script'):
            self.skip = True
        if tag == 'br':
            self.result.append('\n')
        if tag in ('p', 'div', 'li', 'tr'):
            self.result.append('\n')

    def handle_endtag(self, tag):
        if tag in ('style', 'script'):
            self.skip = False

    def handle_data(self, data):
        if not self.skip:
            self.result.append(data)

    def get_text(self):
        return ''.join(self.result)


def strip_html(html_content):
    """Convert HTML to plain text."""
    if not html_content:
        return ''
    extractor = HTMLTextExtractor()
    try:
        extractor.feed(html_content)
    except Exception:
        return html_content
    text = extractor.get_text()
    # Clean up excessive whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()


def strip_reply_chain(text):
    """Remove quoted reply chains to save tokens."""
    lines = text.split('\n')
    result = []
    for line in lines:
        # Stop at reply chain markers
        if re.match(r'^\s*----\s*on\s', line, re.I):
            break
        if re.match(r'^\s*On\s.*wrote:', line):
            break
        if re.match(r'^\s*From:', line) and 'zooza' not in line.lower():
            break
        if line.strip().startswith('>'):
            continue
        result.append(line)
    return '\n'.join(result).strip()


def anonymize(text):
    """Remove PII from text while keeping Zooza team references."""
    if not text:
        return ''
    # Replace non-Zooza emails
    def replace_email(m):
        email = m.group(0).lower()
        if email in ZOOZA_EMAILS:
            return email
        return '[EMAIL]'
    text = EMAIL_RE.sub(replace_email, text)

    # Replace phone numbers (but not short numbers that might be IDs)
    def replace_phone(m):
        num = m.group(0)
        digits = re.sub(r'\D', '', num)
        if len(digits) >= 9:
            return '[PHONE]'
        return num
    text = PHONE_RE.sub(replace_phone, text)

    # Remove common signature patterns
    text = re.sub(r'(?i)(s pozdravom|s úctou|best regards|kind regards|regards)[\s,]*\n.*$',
                  '[SIGNATURE_REMOVED]', text, flags=re.MULTILINE | re.DOTALL)

    return text


def is_bug(classification):
    """Check if classification indicates a bug report."""
    if not classification:
        return False
    return any(classification.startswith(prefix) for prefix in BUG_CLASSIFICATIONS)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Step 1: Load and filter cases
    print("Loading cases...")
    cases = {}
    skipped_date = 0
    skipped_bug = 0
    total = 0

    with open(CASES_CSV, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += 1
            created = row.get('Created Time', '')
            if created < DATE_CUTOFF:
                skipped_date += 1
                continue
            classification = row.get('Classifications', '')
            if is_bug(classification):
                skipped_bug += 1
                continue

            case_id = row['ID']
            cases[case_id] = {
                'case_id': case_id,
                'subject': row.get('Subject', ''),
                'category': row.get('Category', ''),
                'classification': classification,
                'created': created,
                'status': row.get('Status', ''),
                'language': row.get('Language', ''),
                'tags': [t.strip() for t in (row.get('Tags', '') or '').split(',') if t.strip()],
                'threads': []
            }

    print(f"Cases: {total} total, {skipped_date} before cutoff, {skipped_bug} bugs, {len(cases)} kept")

    # Step 2: Load threads for filtered cases
    print("Loading threads...")
    thread_count = 0
    matched = 0

    with open(THREADS_CSV, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        # Skip the template row
        next(reader, None)
        for row in reader:
            thread_count += 1
            ticket_id = row.get('Ticket id', '')
            if ticket_id not in cases:
                continue

            content = row.get('Thread Content', '')
            plain_text = strip_html(content)
            plain_text = strip_reply_chain(plain_text)
            plain_text = anonymize(plain_text)

            if not plain_text or len(plain_text) < 10:
                continue

            # Truncate very long messages to save tokens
            if len(plain_text) > 2000:
                plain_text = plain_text[:2000] + '... [TRUNCATED]'

            is_private = row.get('Is Private', '') == 'true'
            from_addr = row.get('From', '')
            thread_type = row.get('Thread Status', '')

            # Determine if this is from customer or support
            from_zooza = any(z in from_addr.lower() for z in ['zooza', 'zohodesk'])
            role = 'support' if from_zooza else 'customer'

            cases[ticket_id]['threads'].append({
                'date': row.get('Sent Date And Time', ''),
                'role': role,
                'content': plain_text,
                'is_private': is_private,
                'direction': thread_type,
            })
            matched += 1

    print(f"Threads: {thread_count} total, {matched} matched to filtered cases")

    # Step 3: Remove private threads and cases with no threads
    for case_id in list(cases.keys()):
        case = cases[case_id]
        # Remove private/internal threads
        case['threads'] = [t for t in case['threads'] if not t['is_private']]
        # Remove cases with no public threads
        if not case['threads']:
            del cases[case_id]

    # Sort threads within each case by date
    for case in cases.values():
        case['threads'].sort(key=lambda t: t.get('date', ''))

    print(f"Final: {len(cases)} cases with public threads")

    # Step 4: Write JSONL
    output_path = os.path.join(OUTPUT_DIR, 'ingest-conversations.jsonl')
    with open(output_path, 'w', encoding='utf-8') as f:
        for case in sorted(cases.values(), key=lambda c: c['created']):
            f.write(json.dumps(case, ensure_ascii=False) + '\n')

    print(f"Written to {output_path}")

    # Step 5: Quick stats
    categories = defaultdict(int)
    classifications = defaultdict(int)
    for case in cases.values():
        categories[case['category']] += 1
        classifications[case['classification']] += 1

    print("\nBy category:")
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"  {cat or '(empty)'}: {count}")

    print("\nBy classification:")
    for cls, count in sorted(classifications.items(), key=lambda x: -x[1]):
        print(f"  {cls or '(empty)'}: {count}")


if __name__ == '__main__':
    main()
