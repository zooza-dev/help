#!/usr/bin/env python3
"""Step 2: Compare ticket features vs KB coverage.

Loads build/ingest/topic-summary.json (feature extraction from full text),
matches features to KB articles with manual curated mapping,
identifies gaps, outputs coverage-report.md.

Zero LLM tokens — pure local processing.
"""

import json
import os
import re
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TOPIC_SUMMARY = REPO_ROOT / "build" / "ingest" / "topic-summary.json"
CONTENT_DIR = REPO_ROOT / "content"
OUT_DIR = REPO_ROOT / "build" / "ingest"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Manual curated mapping: feature_id → list of KB slugs that cover it
# "well" = article directly addresses this topic
# Empty list = no coverage (gap)
FEATURE_KB_MAP = {
    # --- Payments ---
    "payment-schedules": {
        "coverage": "good",
        "articles": ["payment-templates-creation", "billing-periods"],
    },
    "payment-pairing": {
        "coverage": "good",
        "articles": ["payment-pairing"],
    },
    "invoices": {
        "coverage": "good",
        "articles": ["xero-integration", "abra-flexi-invoices", "szamlazz-invoices", "smartbill-invoices"],
    },
    "discounts": {
        "coverage": "good",
        "articles": ["discount-code", "discount-types"],
    },
    "refunds": {
        "coverage": "gap",
        "articles": [],
        "note": "No refund/credit note workflow article. Only passing mentions.",
    },
    "outstanding-payments": {
        "coverage": "good",
        "articles": ["outstanding-amount"],
    },
    "gocardless": {
        "coverage": "good",
        "articles": ["gocardless-direct-debit-mandates"],
    },
    "payments-general": {
        "coverage": "partial",
        "articles": ["payment-options", "payment-tile-on-registration", "edit-payment-on-registration",
                      "payment-labels-drawers", "zooza-billing-payments"],
        "note": "Setup covered well, but no troubleshooting (failed payments, recovery, declined cards).",
    },
    "pricing": {
        "coverage": "partial",
        "articles": ["payment-options", "payment-templates-creation"],
        "note": "Price config is spread across multiple articles. No single 'how to set pricing' guide.",
    },

    # --- Courses / Programmes ---
    "courses": {
        "coverage": "good",
        "articles": ["course-settings", "course-settings-tile", "course-group-lesson-definition",
                      "open-course-creation", "summer-camps-creation", "getting-started-with-zooza",
                      "new-course-existing-clients"],
    },
    "groups-classes": {
        "coverage": "partial",
        "articles": ["blocks-creation", "edit-events-in-courses", "two-lecturers-per-group"],
        "note": "blocks-creation covers blocks only. No general 'create a group/class' guide.",
    },
    "blocks-terms": {
        "coverage": "partial",
        "articles": ["blocks-creation", "billing-periods"],
        "note": "Blocks covered. Term/semester lifecycle not clearly documented.",
    },
    "instructors": {
        "coverage": "good",
        "articles": ["zooza-101-instructors", "change-instructor", "lecturer-substitution",
                      "lecturers-working-hours", "instructor-rate-reward"],
    },
    "capacity": {
        "coverage": "partial",
        "articles": ["course-settings", "allowing-multiple-registration"],
        "note": "Capacity is a setting inside course config, not its own article. Common question deserves explicit section.",
    },

    # --- Registrations / Bookings ---
    "registrations": {
        "coverage": "good",
        "articles": ["online-registration", "types-of-registrations", "linked-registrations",
                      "late-registrations", "business-registration", "allowing-multiple-registration"],
    },
    "replacements-makeups": {
        "coverage": "depth-gap",
        "articles": ["common-booking-scenarios"],
        "note": "144+ tickets. Only Q7 in FAQ mentions make-ups (one paragraph). Needs dedicated guide.",
    },
    "transfers": {
        "coverage": "partial",
        "articles": ["common-booking-scenarios"],
        "note": "Transfers mentioned briefly in booking scenarios. No step-by-step guide.",
    },
    "waiting-list": {
        "coverage": "good",
        "articles": ["group-interested", "individual-lessons-group-interested"],
    },
    "trial-lessons": {
        "coverage": "good",
        "articles": ["trial-lessons", "trials-daily-business", "individual-lessons-with-free-lesson"],
    },
    "registration-form": {
        "coverage": "partial",
        "articles": ["online-registration", "customizing-widgets"],
        "note": "Setup covered. No troubleshooting (form not showing, validation errors).",
    },

    # --- Calendar ---
    "calendar": {
        "coverage": "depth-gap",
        "articles": ["holiday-settings"],
        "note": "134 tickets vs 1 article that only covers holidays. No calendar views, scheduling, rescheduling guide.",
    },
    "schedule": {
        "coverage": "gap",
        "articles": [],
        "note": "No schedule/timetable management article.",
    },
    "holidays": {
        "coverage": "good",
        "articles": ["holiday-settings"],
    },
    "lessons-events": {
        "coverage": "partial",
        "articles": ["edit-events-in-courses", "how-to-create-paid-events", "viewing-billable-events"],
        "note": "Event editing covered. No general 'managing lessons' overview.",
    },

    # --- Clients ---
    "clients": {
        "coverage": "good",
        "articles": ["data-correction-change-client", "personas", "client-import"],
    },
    "parent-portal": {
        "coverage": "good",
        "articles": ["parent-portal-101", "parent-profile-dashboard"],
    },
    "profiles-accounts": {
        "coverage": "good",
        "articles": ["parent-profile-dashboard", "parent-portal-101"],
    },
    "data-import": {
        "coverage": "good",
        "articles": ["client-import"],
    },
    "data-export": {
        "coverage": "partial",
        "articles": ["power-bi-integration", "power-bi-data-description"],
        "note": "Power BI covered. No guide for simple CSV/Excel export.",
    },

    # --- Communication ---
    "email-messages": {
        "coverage": "good",
        "articles": ["sending-email-sms", "send-email-after-event", "message-templates",
                      "company-logo-email", "emails-in-primary-inbox"],
    },
    "notifications": {
        "coverage": "good",
        "articles": ["notifications-center", "automatic-event-notification",
                      "edit-event-notification-template", "automatic-payment-reminders"],
    },
    "message-templates": {
        "coverage": "good",
        "articles": ["message-templates", "edit-event-notification-template", "template-title"],
    },
    "dynamic-tags": {
        "coverage": "good",
        "articles": ["dynamic-tags"],
    },
    "whatsapp": {
        "coverage": "good",
        "articles": ["whatsapp-integration", "whatsapp-faq", "whatsapp-troubleshooting"],
    },
    "sms": {
        "coverage": "partial",
        "articles": ["sending-email-sms"],
        "note": "SMS mentioned alongside email. No dedicated SMS setup/troubleshooting.",
    },

    # --- Attendance ---
    "attendance": {
        "coverage": "gap",
        "articles": [],
        "note": "115 tickets. Zero KB articles. Major gap.",
    },

    # --- Login & access ---
    "login-access": {
        "coverage": "gap",
        "articles": [],
        "note": "Closest is how-to-clear-your-cache which is not login help. Need: password reset, account access, inviting users.",
    },

    # --- Widgets ---
    "widgets": {
        "coverage": "partial",
        "articles": ["customizing-widgets", "deploying-zooza-on-website", "zooza-sites"],
        "note": "Setup/deployment covered. No troubleshooting (widget not showing, mobile issues).",
    },

    # --- Settings ---
    "consents-gdpr": {
        "coverage": "good",
        "articles": ["setting-gtc-gdpr-consents"],
    },
    "documents": {
        "coverage": "good",
        "articles": ["documents"],
    },
    "branding": {
        "coverage": "partial",
        "articles": ["company-logo-email", "customizing-widgets"],
        "note": "Logo in email covered. No general branding/theme guide.",
    },
    "user-roles": {
        "coverage": "good",
        "articles": ["user-roles"],
    },
    "reports-analytics": {
        "coverage": "good",
        "articles": ["power-bi-integration", "power-bi-data-description"],
    },
}


def load_kb_index():
    """Extract title, slug, product_area from all KB articles."""
    articles = []
    for root, _dirs, files in os.walk(CONTENT_DIR):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            path = Path(root) / fname
            text = path.read_text(encoding="utf-8")
            m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
            if not m:
                continue
            fm = m.group(1)

            title = slug = product_area = doc_type = ""
            for line in fm.splitlines():
                tm = re.match(r'title:\s*"(.+?)"', line)
                if tm:
                    title = tm.group(1)
                sm = re.match(r'slug:\s*"(.+?)"', line)
                if sm:
                    slug = sm.group(1)
                pm = re.match(r'product_area:\s*"(.+?)"', line)
                if pm:
                    product_area = pm.group(1)
                tym = re.match(r'type:\s*"(.+?)"', line)
                if tym:
                    doc_type = tym.group(1)

            articles.append({
                "path": str(path.relative_to(REPO_ROOT)),
                "title": title,
                "slug": slug,
                "product_area": product_area,
                "type": doc_type,
            })
    return articles


def main():
    print("Loading topic summary...")
    with open(TOPIC_SUMMARY, "r", encoding="utf-8") as f:
        summary = json.load(f)

    print("Indexing KB articles...")
    articles = load_kb_index()
    print(f"  {len(articles)} articles indexed")

    features = summary["features"]

    # Classify features
    gaps = []
    depth_gaps = []
    partial = []
    covered = []

    for feat in features:
        fid = feat["feature_id"]
        mapping = FEATURE_KB_MAP.get(fid)

        if not mapping:
            # No mapping defined — treat as unknown
            gaps.append({**feat, "coverage": "unmapped", "note": "No coverage mapping defined."})
            continue

        cov = mapping["coverage"]
        note = mapping.get("note", "")
        kb_slugs = mapping["articles"]

        entry = {
            **feat,
            "coverage": cov,
            "kb_articles": kb_slugs,
            "note": note,
        }

        if cov == "gap":
            gaps.append(entry)
        elif cov == "depth-gap":
            depth_gaps.append(entry)
        elif cov == "partial":
            partial.append(entry)
        else:
            covered.append(entry)

    gaps.sort(key=lambda x: x["ticket_count"], reverse=True)
    depth_gaps.sort(key=lambda x: x["ticket_count"], reverse=True)
    partial.sort(key=lambda x: x["ticket_count"], reverse=True)
    covered.sort(key=lambda x: x["ticket_count"], reverse=True)

    # KB articles by product area
    pa_articles = defaultdict(list)
    for art in articles:
        pa_articles[art["product_area"]].append(art)

    # --- Generate report ---
    L = []
    L.append("# Support Ticket vs Knowledge Base — Coverage Report")
    L.append("")
    L.append(f"**Generated:** 2026-02-11")
    L.append(f"**Method:** Full-text feature extraction from Subject + Description (SK/CZ/EN)")
    L.append(f"**Filter:** Setup & usage questions only (bugs/outages excluded)")
    L.append(f"**Source:** {summary['source']}")
    L.append(f"**Total tickets:** {summary['total_tickets']:,}")
    L.append(f"**Setup/usage questions analyzed:** {summary['setup_questions']:,}")
    L.append(f"**Excluded:** {summary['excluded']:,}")
    L.append("")

    # Summary
    total_gap = sum(g["ticket_count"] for g in gaps)
    total_depth = sum(d["ticket_count"] for d in depth_gaps)
    total_partial = sum(p["ticket_count"] for p in partial)
    total_covered = sum(c["ticket_count"] for c in covered)

    L.append("## Executive Summary")
    L.append("")
    L.append("| Coverage level | Features | Ticket mentions | Action |")
    L.append("|---|---|---|---|")
    L.append(f"| **Gap** (no article) | {len(gaps)} | {total_gap} | Write new article |")
    L.append(f"| **Depth gap** (article too thin) | {len(depth_gaps)} | {total_depth} | Expand existing |")
    L.append(f"| **Partial** (setup only, no troubleshooting) | {len(partial)} | {total_partial} | Add troubleshooting / expand |")
    L.append(f"| **Well covered** | {len(covered)} | {total_covered} | No action needed |")
    L.append("")
    underserved = total_gap + total_depth + total_partial
    pct = (underserved / (underserved + total_covered)) * 100 if (underserved + total_covered) > 0 else 0
    L.append(f"> **{pct:.0f}% of feature mentions** ({underserved:,} out of {underserved + total_covered:,}) "
             f"hit under-served topics.")
    L.append("")

    # Product area summary
    L.append("## Coverage by Product Area")
    L.append("")
    L.append("| Product Area | KB articles | Gap features | Depth-gap features | Partial features |")
    L.append("|---|---|---|---|---|")
    all_pas = sorted(set(
        [f["product_area"] for f in features] + list(pa_articles.keys())
    ))
    for pa in all_pas:
        n_art = len(pa_articles.get(pa, []))
        n_gap = sum(1 for g in gaps if g["product_area"] == pa)
        n_depth = sum(1 for d in depth_gaps if d["product_area"] == pa)
        n_partial = sum(1 for p in partial if p["product_area"] == pa)
        if n_gap or n_depth or n_partial or n_art:
            L.append(f"| {pa} | {n_art} | {n_gap} | {n_depth} | {n_partial} |")
    L.append("")

    # === GAPS ===
    L.append("## Gaps — No KB article at all")
    L.append("")
    for g in gaps:
        L.append(f"### {g['topic']} ({g['ticket_count']} mentions)")
        L.append(f"- **Product area:** {g['product_area']}")
        L.append(f"- **Issue:** {g.get('note', 'No coverage')}")
        if g.get("sample_subjects"):
            L.append(f"- **Sample questions:**")
            for s in g["sample_subjects"][:3]:
                if s:
                    L.append(f"  - {s}")
        L.append("")

    # === DEPTH GAPS ===
    L.append("## Depth Gaps — Article exists but too thin")
    L.append("")
    for d in depth_gaps:
        slugs = ", ".join(f"`{s}`" for s in d.get("kb_articles", []))
        L.append(f"### {d['topic']} ({d['ticket_count']} mentions)")
        L.append(f"- **Product area:** {d['product_area']}")
        L.append(f"- **Current articles:** {slugs}")
        L.append(f"- **Issue:** {d.get('note', '')}")
        if d.get("sample_subjects"):
            L.append(f"- **Sample questions:**")
            for s in d["sample_subjects"][:3]:
                if s:
                    L.append(f"  - {s}")
        L.append("")

    # === PARTIAL ===
    L.append("## Partial Coverage — Setup documented, troubleshooting missing")
    L.append("")
    for p in partial:
        slugs = ", ".join(f"`{s}`" for s in p.get("kb_articles", []))
        L.append(f"### {p['topic']} ({p['ticket_count']} mentions)")
        L.append(f"- **Product area:** {p['product_area']}")
        L.append(f"- **Current articles:** {slugs}")
        L.append(f"- **Issue:** {p.get('note', '')}")
        L.append("")

    # === COVERED ===
    L.append("## Well-Covered Features")
    L.append("")
    L.append("| Feature | Mentions | Key KB articles |")
    L.append("|---|---|---|")
    for c in covered:
        slugs = ", ".join(f"`{s}`" for s in c.get("kb_articles", [])[:3])
        L.append(f"| {c['topic']} | {c['ticket_count']} | {slugs} |")
    L.append("")

    # === PRIORITY RECOMMENDATIONS ===
    L.append("## Priority: New articles to write")
    L.append("")
    L.append("Ranked by ticket volume. Each line = one new article needed.")
    L.append("")

    # Merge gaps + depth_gaps + high-volume partial
    priorities = []
    for g in gaps:
        priorities.append(("GAP", g))
    for d in depth_gaps:
        priorities.append(("DEPTH", d))
    for p in partial:
        if p["ticket_count"] >= 50:
            priorities.append(("PARTIAL", p))
    priorities.sort(key=lambda x: x[1]["ticket_count"], reverse=True)

    L.append("| # | Feature | Mentions | Status | Product area | Suggested action |")
    L.append("|---|---|---|---|---|---|")
    for i, (status, item) in enumerate(priorities, 1):
        if status == "GAP":
            action = "Write new article"
        elif status == "DEPTH":
            action = "Expand existing → dedicated guide"
        else:
            action = "Add troubleshooting section"
        L.append(f"| {i} | **{item['topic']}** | {item['ticket_count']} | {status} | "
                 f"{item['product_area']} | {action} |")
    L.append("")

    report = "\n".join(L)
    out_path = OUT_DIR / "coverage-report.md"
    out_path.write_text(report, encoding="utf-8")
    print(f"\nWrote {out_path} ({os.path.getsize(out_path)} bytes)")

    # Save structured data
    structured = {
        "gaps": gaps,
        "depth_gaps": depth_gaps,
        "partial": partial,
        "covered": [{"feature_id": c["feature_id"], "topic": c["topic"],
                      "ticket_count": c["ticket_count"], "kb_articles": c.get("kb_articles", [])}
                     for c in covered],
        "kb_articles": [{"title": a["title"], "slug": a["slug"], "product_area": a["product_area"]}
                         for a in articles],
    }
    struct_path = OUT_DIR / "coverage-structured.json"
    with open(struct_path, "w", encoding="utf-8") as f:
        json.dump(structured, f, indent=2, ensure_ascii=False)
    print(f"Wrote {struct_path} ({os.path.getsize(struct_path)} bytes)")


if __name__ == "__main__":
    main()
