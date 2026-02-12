#!/usr/bin/env python3
"""Step 1: Pre-process Zoho Desk CSV into a compact topic summary.

Reads ../help_ingest/Cases__1 7.csv, filters to questions/requests,
groups by category + tags, and outputs build/ingest/topic-summary.json.

Zero LLM tokens — pure local processing.
"""

import csv
import json
import os
import re
from collections import Counter, defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = REPO_ROOT.parent / "help_ingest" / "Cases__1 7.csv"
OUT_DIR = REPO_ROOT / "build" / "ingest"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Classifications that count as "questions / requests" (not bugs/outages)
QUESTION_CLASSIFICATIONS = {
    "Request - General question",
    "Question - How to set up?",
    "Issue - Requirement to test a set up",
    "- select classification -",
    "- choose one -",
    "Consultation Session (Paid)",
    "Consultation Session Paid",
}

# Zoho Category → KB product_area
CATEGORY_MAP = {
    "Payments": "Payments",
    "Courses": "Programmes",
    "Clients": "Clients",
    "Settings": "Settings",
    "Communication": "Communication",
    "Calendar": "Calendar",
    "Lecturers": "Settings",
    "Products": "Orders",
    "Documents": "Settings",
}

# Tag → canonical topic name + KB product_area
TAG_TOPIC_MAP = {
    "payments": ("Payment issues", "Payments"),
    "replacements": ("Make-up lessons / replacements", "Bookings"),
    "communication": ("Communication & notifications", "Communication"),
    "widgets": ("Widget setup & customization", "Widgets"),
    "registrations": ("Registration / booking flow", "Bookings"),
    "registration form": ("Registration form configuration", "Bookings"),
    "payment_schedules": ("Payment schedules & plans", "Payments"),
    "registration": ("Registration / booking flow", "Bookings"),
    "profile": ("Parent portal & profiles", "Clients"),
    "terms": ("Billing periods / terms", "Payments"),
    "calendar": ("Calendar management", "Calendar"),
    "notification": ("Notifications", "Communication"),
    "groups": ("Groups / classes", "Classes"),
    "emails": ("Email sending", "Communication"),
    "invoices": ("Invoicing integrations", "Payments"),
    "attendance": ("Attendance tracking", "Programmes"),
    "courses": ("Course / programme setup", "Programmes"),
    "lecturers": ("Instructor management", "Settings"),
    "settings": ("General settings", "Settings"),
    "clients": ("Client management", "Clients"),
    "login": ("Login & access", "Settings"),
    "consents": ("GTC / GDPR consents", "Settings"),
    "dynamic tags": ("Dynamic tags in messages", "Communication"),
    "gocardless": ("GoCardless direct debit", "Payments"),
    "transfer": ("Transfer between courses", "Bookings"),
    "portal": ("Parent portal", "Clients"),
    "sms": ("SMS messaging", "Communication"),
    "whatsapp": ("WhatsApp integration", "Communication"),
    "reports": ("Reports & analytics", "Settings"),
    "discount": ("Discounts & promo codes", "Payments"),
    "trial": ("Trial lessons", "Programmes"),
    "waiting_list": ("Waiting list", "Bookings"),
    "products": ("Products / merchandise", "Orders"),
    "documents": ("Documents management", "Settings"),
    "export": ("Data export", "Settings"),
    "import": ("Data import", "Clients"),
}

# Bug-related tags to exclude from topic analysis
BUG_TAGS = {"bug", "maybe_bug", "outage", "issue"}


def load_tickets():
    """Load CSV and return list of dicts."""
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def is_question(row):
    """Return True if the ticket is a question/request, not a bug."""
    cls = row.get("Classifications", "").strip()
    # If classification is empty, include it (unclassified)
    if not cls:
        return True
    return cls in QUESTION_CLASSIFICATIONS


def extract_tags(row):
    """Return list of cleaned tags."""
    raw = row.get("Tags", "").strip()
    if not raw:
        return []
    return [t.strip().lower() for t in raw.split(",") if t.strip()]


def clean_subject(subj):
    """Remove Re:/Fwd: prefixes and clean up subject line."""
    subj = re.sub(r"^(Re|Fwd|FW|Odp|Přepos):\s*", "", subj, flags=re.IGNORECASE)
    subj = re.sub(r"^(Re|Fwd|FW|Odp|Přepos):\s*", "", subj, flags=re.IGNORECASE)
    return subj.strip()


def main():
    print(f"Loading CSV from {CSV_PATH}")
    rows = load_tickets()
    print(f"Total tickets: {len(rows)}")

    # Filter to questions/requests
    questions = [r for r in rows if is_question(r)]
    bugs = [r for r in rows if not is_question(r)]
    print(f"Questions/requests: {len(questions)}")
    print(f"Bugs/outages (excluded): {len(bugs)}")

    # --- Topic extraction by tags ---
    topic_tickets = defaultdict(list)  # topic_name → [subjects]
    topic_counts = Counter()
    topic_product_area = {}

    for row in questions:
        tags = extract_tags(row)
        subj = clean_subject(row.get("Subject", ""))
        category = row.get("Category", "").strip()

        # Map tags to topics
        mapped_any = False
        for tag in tags:
            if tag in BUG_TAGS:
                continue
            if tag in TAG_TOPIC_MAP:
                topic_name, pa = TAG_TOPIC_MAP[tag]
                topic_counts[topic_name] += 1
                topic_product_area[topic_name] = pa
                if len(topic_tickets[topic_name]) < 10:
                    topic_tickets[topic_name].append(subj)
                mapped_any = True

        # If no tag mapped, use category
        if not mapped_any and category:
            pa = CATEGORY_MAP.get(category, "Settings")
            topic_name = f"{category} (general)"
            topic_counts[topic_name] += 1
            topic_product_area[topic_name] = pa
            if len(topic_tickets[topic_name]) < 10:
                topic_tickets[topic_name].append(subj)

    # --- Category frequency (all questions) ---
    cat_counts = Counter()
    for row in questions:
        cat = row.get("Category", "").strip()
        if cat:
            cat_counts[cat] += 1

    # --- Language distribution ---
    lang_counts = Counter(r.get("Language", "").strip() or "unknown" for r in questions)

    # --- Channel distribution ---
    channel_counts = Counter(r.get("Channel", "").strip() or "unknown" for r in questions)

    # --- Build output ---
    topics_sorted = []
    for topic_name, count in topic_counts.most_common():
        topics_sorted.append({
            "topic": topic_name,
            "product_area": topic_product_area[topic_name],
            "ticket_count": count,
            "sample_subjects": topic_tickets[topic_name][:5],
        })

    output = {
        "generated": "2026-02-11",
        "source": str(CSV_PATH.name),
        "total_tickets": len(rows),
        "questions_requests": len(questions),
        "bugs_outages": len(bugs),
        "language_distribution": dict(lang_counts.most_common()),
        "channel_distribution": dict(channel_counts.most_common()),
        "category_counts": dict(cat_counts.most_common()),
        "topics": topics_sorted,
    }

    out_path = OUT_DIR / "topic-summary.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nWrote {out_path} ({os.path.getsize(out_path)} bytes)")
    print(f"\nTop 15 topics:")
    for t in topics_sorted[:15]:
        print(f"  {t['ticket_count']:4d}  [{t['product_area']:15s}]  {t['topic']}")


if __name__ == "__main__":
    main()
