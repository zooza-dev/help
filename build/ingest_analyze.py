#!/usr/bin/env python3
"""Step 1: Pre-process Zoho Desk CSV into a compact topic summary.

Reads ../help_ingest/Cases__1 7.csv, filters to setup/usage questions only,
extracts product features from Subject + Description text (SK/CZ/EN),
and outputs build/ingest/topic-summary.json.

Zero LLM tokens — pure local processing.
"""

import csv
import json
import os
import re
from collections import Counter, defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = REPO_ROOT.parent / "help_ingest" / "Cases__1 7.csv"
OUT_DIR = REPO_ROOT / "build" / "ingest"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Only setup/usage classifications (strict — no unclassified, no bugs)
SETUP_CLASSIFICATIONS = {
    "Request - General question",
    "Question - How to set up?",
    "Issue - Requirement to test a set up",
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

# Feature patterns: regex → (feature_id, display_name, product_area)
# Patterns match across Slovak, Czech, and English
FEATURE_PATTERNS = [
    # --- Payments ---
    (r"splátk|splátkový|payment.?schedul|splatkovy",
     "payment-schedules", "Payment schedules & instalment plans", "Payments"),
    (r"párovania|párovanie|parovanie|payment.?pair",
     "payment-pairing", "Payment pairing / matching", "Payments"),
    (r"faktúr|faktur|invoice|doklad",
     "invoices", "Invoicing & invoice integrations", "Payments"),
    (r"zľava|zlava|discount|promo|kupón|kupon",
     "discounts", "Discounts & promo codes", "Payments"),
    (r"vratenie|vrátenie|refund|dobropis|credit.?note|storno.?poplat",
     "refunds", "Refunds & credit notes", "Payments"),
    (r"pohľadáv|nedoplat|outstanding|dlh|nedoplatok",
     "outstanding-payments", "Outstanding amounts / debt", "Payments"),
    (r"gocardless|direct.?debit|inkaso",
     "gocardless", "GoCardless / direct debit", "Payments"),
    (r"(?<!registračn.)(?:platby|platba|payment|plateb|platieb)(?!.{0,10}šabloň)",
     "payments-general", "Payments (general setup & config)", "Payments"),

    # --- Courses / Programmes ---
    (r"lektor|instructor|učiteľ|ucitel|lecturer",
     "instructors", "Instructor / lecturer management", "Settings"),
    (r"kapacit|capacity|(?:počet |pocet )?míst|(?:počet |pocet )?miest",
     "capacity", "Capacity & participant limits", "Programmes"),
    (r"skupin|group|trieda|class(?!ifi)",
     "groups-classes", "Groups & classes setup", "Classes"),
    (r"blok(?!ov)|block|semester|polrok",
     "blocks-terms", "Blocks & terms / semesters", "Classes"),
    (r"kurz|course|programme|program(?!.{0,5}area)",
     "courses", "Course / programme setup", "Programmes"),

    # --- Registrations / Bookings ---
    (r"náhrad|nahrad|replacement|make.?up|zastup",
     "replacements-makeups", "Make-up / replacement lessons", "Bookings"),
    (r"presun|transfer|presunutie|přesun",
     "transfers", "Transfers between courses", "Bookings"),
    (r"čakacia|waiting.?list|čekací|záujemci|zaujemci|interested",
     "waiting-list", "Waiting list & interested", "Bookings"),
    (r"trial|skúšob|skusob|pokusn",
     "trial-lessons", "Trial lessons", "Programmes"),
    (r"formulár|formular|registra.{0,5}form",
     "registration-form", "Registration form config", "Widgets"),
    (r"registráci|registraci|registrace|registration|prihlás|prihlas(?!en.{0,5}(na|do) systém)",
     "registrations", "Registration & booking flow", "Bookings"),

    # --- Calendar ---
    (r"sviat|holiday|prázdnin|prazdnin|voľno|volno",
     "holidays", "Holidays & days off", "Calendar"),
    (r"rozvrh|schedule|timetable",
     "schedule", "Schedule / timetable", "Calendar"),
    (r"kalendár|kalendar|calendar",
     "calendar", "Calendar views & management", "Calendar"),
    (r"(?:hodiny|hodina|lesson|event|udalost|událost)(?!.{0,5}náhrad)",
     "lessons-events", "Lessons & events management", "Calendar"),

    # --- Clients ---
    (r"portál|portal|rodič|rodic|parent(?!.{0,5}dir)",
     "parent-portal", "Parent portal & self-service", "Clients"),
    (r"profil|profile|účet|ucet|account|konto",
     "profiles-accounts", "Client profiles & accounts", "Clients"),
    (r"import(?!ant)",
     "data-import", "Data import", "Clients"),
    (r"export",
     "data-export", "Data export & reports", "Settings"),
    (r"klient|client|zákazník|zakaznik|customer",
     "clients", "Client management (general)", "Clients"),

    # --- Communication ---
    (r"notifikáci|notifikaci|notification|upozorneni|upozornění",
     "notifications", "Notifications & alerts", "Communication"),
    (r"šablón|sablon|template(?!.{0,5}title)|vzor",
     "message-templates", "Message templates", "Communication"),
    (r"dynamick|dynamic.?tag|značk|znack",
     "dynamic-tags", "Dynamic tags in messages", "Communication"),
    (r"whatsapp",
     "whatsapp", "WhatsApp integration", "Communication"),
    (r"\bsms\b",
     "sms", "SMS messaging", "Communication"),
    (r"email|mail|správ|sprav|message(?!.{0,5}template)",
     "email-messages", "Email & messaging", "Communication"),

    # --- Attendance ---
    (r"dochádzk|dochadzk|attendance|prezenc|účast|ucast",
     "attendance", "Attendance tracking", "Programmes"),

    # --- Login & access ---
    (r"login|(?:prihlás|prihlas).{0,10}(?:systém|system|zooza|účet|ucet|kont)|heslo|password|prístup.{0,5}(?:do|k)|pristup.{0,5}(?:do|k)|nevie.{0,10}(?:prihlásiť|prihlasit|dostať|dostat)",
     "login-access", "Login & account access", "Settings"),

    # --- Widgets ---
    (r"widget|embed|iframe|web.?stránk|web.?strank|website",
     "widgets", "Widgets & website embedding", "Widgets"),

    # --- Settings ---
    (r"súhlas|suhlas|gdpr|consent|vop|obchodn.?podmien",
     "consents-gdpr", "GTC / GDPR consents", "Settings"),
    (r"dokument|document|príloha|priloha|attachment",
     "documents", "Documents & attachments", "Settings"),
    (r"logo|brand|farb|color|vzhľad|vzhlad|design",
     "branding", "Branding & visual customization", "Settings"),
    (r"rola|(?:user.?)?role|oprávnen|opravnen|permission|práva.{0,5}(?:užívateľ|uzivatel|user)",
     "user-roles", "User roles & permissions", "Settings"),
    (r"report|štatist|statist|analytic|power.?bi|prehľad|prehlad|dashboard",
     "reports-analytics", "Reports & analytics", "Settings"),
    (r"cena|ceny|price|pricing|cenník|cennik",
     "pricing", "Pricing & fee setup", "Payments"),
]


def strip_html(html):
    """Remove HTML tags and entities."""
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"&[a-z]+;", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def clean_subject(subj):
    """Remove Re:/Fwd: prefixes."""
    subj = re.sub(r"^(Re|Fwd|FW|Odp|Přepos):\s*", "", subj, flags=re.IGNORECASE)
    subj = re.sub(r"^(Re|Fwd|FW|Odp|Přepos):\s*", "", subj, flags=re.IGNORECASE)
    return subj.strip()


def main():
    print(f"Loading CSV from {CSV_PATH}")
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    print(f"Total tickets: {len(rows)}")

    # Filter: only setup/usage questions (strict)
    questions = [r for r in rows if r.get("Classifications", "").strip() in SETUP_CLASSIFICATIONS]
    excluded = len(rows) - len(questions)
    print(f"Setup/usage questions: {len(questions)}")
    print(f"Excluded (bugs, outages, unclassified): {excluded}")

    # Extract features from Subject + Description full text
    feature_counts = Counter()
    feature_subjects = defaultdict(list)
    feature_meta = {}  # feature_id → (display_name, product_area)
    tickets_matched = 0
    tickets_unmatched = 0

    for row in questions:
        subj_raw = row.get("Subject", "")
        subj = clean_subject(subj_raw)
        desc = strip_html(row.get("Description", ""))
        combined = (subj + " " + desc).lower()

        matched_features = set()
        for pattern, feat_id, display_name, product_area in FEATURE_PATTERNS:
            if re.search(pattern, combined, re.IGNORECASE):
                matched_features.add(feat_id)
                feature_meta[feat_id] = (display_name, product_area)

        if matched_features:
            tickets_matched += 1
        else:
            tickets_unmatched += 1

        for feat_id in matched_features:
            feature_counts[feat_id] += 1
            if len(feature_subjects[feat_id]) < 8:
                feature_subjects[feat_id].append(subj[:120])

    print(f"\nTickets with feature match: {tickets_matched}")
    print(f"Tickets without match: {tickets_unmatched}")

    # Category and language stats
    cat_counts = Counter(r.get("Category", "").strip() or "uncategorized" for r in questions)
    lang_counts = Counter(r.get("Language", "").strip() or "unknown" for r in questions)
    channel_counts = Counter(r.get("Channel", "").strip() or "unknown" for r in questions)

    # Build output
    features_sorted = []
    for feat_id, count in feature_counts.most_common():
        display_name, product_area = feature_meta[feat_id]
        features_sorted.append({
            "feature_id": feat_id,
            "topic": display_name,
            "product_area": product_area,
            "ticket_count": count,
            "sample_subjects": feature_subjects[feat_id][:5],
        })

    output = {
        "generated": "2026-02-11",
        "source": str(CSV_PATH.name),
        "method": "full-text feature extraction from Subject + Description (SK/CZ/EN patterns)",
        "filter": "setup/usage questions only (Request, How to set up, Requirement to test)",
        "total_tickets": len(rows),
        "setup_questions": len(questions),
        "excluded": excluded,
        "tickets_with_feature_match": tickets_matched,
        "tickets_without_match": tickets_unmatched,
        "language_distribution": dict(lang_counts.most_common()),
        "channel_distribution": dict(channel_counts.most_common()),
        "category_counts": dict(cat_counts.most_common()),
        "features": features_sorted,
    }

    out_path = OUT_DIR / "topic-summary.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nWrote {out_path} ({os.path.getsize(out_path)} bytes)")
    print(f"\nTop 20 product features (by ticket count):")
    for t in features_sorted[:20]:
        print(f"  {t['ticket_count']:4d}  [{t['product_area']:15s}]  {t['topic']}")


if __name__ == "__main__":
    main()
