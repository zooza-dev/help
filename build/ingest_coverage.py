#!/usr/bin/env python3
"""Step 2: Compare ticket topics vs KB coverage.

Loads build/ingest/topic-summary.json and content/ KB index,
matches topics to articles, identifies gaps, outputs coverage-report.md.

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

# Keyword overrides: topic keywords → KB slug substrings
TOPIC_KB_KEYWORDS = {
    "Payment issues": ["payment", "billing", "outstanding", "discount", "vat"],
    "Make-up lessons / replacements": ["booking", "make-up", "common-booking", "replacement"],
    "Communication & notifications": ["communication", "email", "sms", "notification", "message", "whatsapp"],
    "Widget setup & customization": ["widget", "deploying", "sites", "customizing"],
    "Registration / booking flow": ["registration", "booking", "enrollment", "online-registration"],
    "Registration form configuration": ["registration", "online-registration", "form"],
    "Payment schedules & plans": ["payment-template", "billing-period", "payment-schedule"],
    "Parent portal & profiles": ["parent-portal", "parent-profile", "portal", "profile"],
    "Billing periods / terms": ["billing-period", "term", "payment-template"],
    "Calendar management": ["calendar", "holiday", "event"],
    "Notifications": ["notification", "automatic-event", "reminder"],
    "Groups / classes": ["class", "block", "group", "course-setting", "edit-events"],
    "Email sending": ["sending-email", "email", "message-template"],
    "Invoicing integrations": ["invoice", "xero", "abra", "szamlazz", "smartbill"],
    "Attendance tracking": ["attendance"],
    "Course / programme setup": ["course", "programme", "getting-started", "open-course", "summer-camp"],
    "Instructor management": ["instructor", "lecturer", "substitution", "working-hours", "change-instructor"],
    "General settings": ["setting", "user-role", "network"],
    "Client management": ["client", "import", "persona", "data-correction"],
    "Login & access": ["login", "access", "user-role", "cache"],
    "GTC / GDPR consents": ["gtc", "gdpr", "consent"],
    "Dynamic tags in messages": ["dynamic-tag"],
    "GoCardless direct debit": ["gocardless"],
    "Transfer between courses": ["transfer", "booking"],
    "Parent portal": ["parent-portal", "portal"],
    "SMS messaging": ["sms", "sending-email-sms"],
    "WhatsApp integration": ["whatsapp"],
    "Reports & analytics": ["power-bi", "report"],
    "Discounts & promo codes": ["discount"],
    "Trial lessons": ["trial"],
    "Waiting list": ["waiting", "interested"],
    "Products / merchandise": ["product", "selling"],
    "Documents management": ["document"],
    "Data export": ["export", "power-bi"],
    "Data import": ["import", "client-import"],
}


def load_kb_index():
    """Extract title, slug, product_area, and H2 headings from all KB articles."""
    articles = []
    for root, _dirs, files in os.walk(CONTENT_DIR):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            path = Path(root) / fname
            text = path.read_text(encoding="utf-8")

            # Parse frontmatter
            m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
            if not m:
                continue
            fm = m.group(1)

            title = ""
            slug = ""
            product_area = ""
            doc_type = ""
            tags_list = []

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
                tagm = re.match(r'tags:\s*\[(.+?)\]', line)
                if tagm:
                    tags_list = [t.strip().strip('"').strip("'")
                                 for t in tagm.group(1).split(",")]

            # Extract H2 headings
            body = text[m.end():]
            h2s = re.findall(r"^## (.+)$", body, re.MULTILINE)

            articles.append({
                "path": str(path.relative_to(REPO_ROOT)),
                "title": title,
                "slug": slug,
                "product_area": product_area,
                "type": doc_type,
                "tags": tags_list,
                "h2_headings": h2s,
            })
    return articles


def match_topic_to_articles(topic_name, product_area, articles):
    """Find KB articles matching a topic. Returns list of matching article dicts."""
    matches = []
    keywords = TOPIC_KB_KEYWORDS.get(topic_name, [])

    # Fallback: derive keywords from topic name
    if not keywords:
        keywords = [w.lower() for w in topic_name.replace("/", " ").split()
                     if len(w) > 3 and w not in ("the", "and", "for", "with")]

    for art in articles:
        score = 0
        slug_lower = art["slug"].lower()
        title_lower = art["title"].lower()
        tags_lower = [t.lower() for t in art["tags"]]
        h2_text = " ".join(art["h2_headings"]).lower()

        # Product area match
        if art["product_area"] == product_area:
            score += 1

        # Keyword matching against slug, title, tags, headings
        for kw in keywords:
            if kw in slug_lower:
                score += 3
            if kw in title_lower:
                score += 2
            if any(kw in t for t in tags_lower):
                score += 2
            if kw in h2_text:
                score += 1

        if score >= 3:
            matches.append({**art, "_score": score})

    # Sort by relevance
    matches.sort(key=lambda x: x["_score"], reverse=True)
    return matches


def main():
    print("Loading topic summary...")
    with open(TOPIC_SUMMARY, "r", encoding="utf-8") as f:
        summary = json.load(f)

    print("Indexing KB articles...")
    articles = load_kb_index()
    print(f"  {len(articles)} articles indexed")

    # Group articles by product_area
    pa_articles = defaultdict(list)
    for art in articles:
        pa_articles[art["product_area"]].append(art)

    # Match each topic
    topics = summary["topics"]
    covered = []
    gaps = []
    partial = []

    for topic in topics:
        name = topic["topic"]
        pa = topic["product_area"]
        count = topic["ticket_count"]
        matches = match_topic_to_articles(name, pa, articles)

        entry = {
            "topic": name,
            "product_area": pa,
            "ticket_count": count,
            "sample_subjects": topic.get("sample_subjects", []),
            "matching_articles": [
                {"title": m["title"], "slug": m["slug"], "score": m["_score"]}
                for m in matches[:5]
            ],
        }

        if not matches:
            gaps.append(entry)
        elif len(matches) <= 1 and matches[0]["_score"] < 5:
            partial.append(entry)
        else:
            covered.append(entry)

    # Sort gaps by ticket count (highest first)
    gaps.sort(key=lambda x: x["ticket_count"], reverse=True)
    partial.sort(key=lambda x: x["ticket_count"], reverse=True)

    # --- Generate Markdown report ---
    lines = []
    lines.append("# Support Ticket Coverage Analysis")
    lines.append("")
    lines.append(f"**Generated:** 2026-02-11")
    lines.append(f"**Source:** {summary['source']}")
    lines.append(f"**Total tickets:** {summary['total_tickets']}")
    lines.append(f"**Questions/requests analyzed:** {summary['questions_requests']}")
    lines.append(f"**Bugs/outages excluded:** {summary['bugs_outages']}")
    lines.append("")

    # Summary stats
    total_gap_tickets = sum(g["ticket_count"] for g in gaps)
    total_partial_tickets = sum(p["ticket_count"] for p in partial)
    total_covered_tickets = sum(c["ticket_count"] for c in covered)

    lines.append("## Summary")
    lines.append("")
    lines.append(f"| Status | Topics | Total ticket mentions |")
    lines.append(f"|--------|--------|-----------------------|")
    lines.append(f"| **Gap (no KB article)** | {len(gaps)} | {total_gap_tickets} |")
    lines.append(f"| **Partial (weak match)** | {len(partial)} | {total_partial_tickets} |")
    lines.append(f"| **Covered** | {len(covered)} | {total_covered_tickets} |")
    lines.append("")

    # KB coverage by product area
    lines.append("## KB Coverage by Product Area")
    lines.append("")
    lines.append("| Product Area | KB Articles | Ticket topics mapped | Gap topics |")
    lines.append("|---|---|---|---|")
    all_product_areas = sorted(set(
        [t["product_area"] for t in topics] +
        list(pa_articles.keys())
    ))
    for pa in all_product_areas:
        n_articles = len(pa_articles.get(pa, []))
        n_topics = sum(1 for t in topics if t["product_area"] == pa)
        n_gaps = sum(1 for g in gaps if g["product_area"] == pa)
        lines.append(f"| {pa} | {n_articles} | {n_topics} | {n_gaps} |")
    lines.append("")

    # Gaps
    lines.append("## Gaps — Topics with NO matching KB article")
    lines.append("")
    if gaps:
        for g in gaps:
            lines.append(f"### {g['topic']}  ({g['ticket_count']} tickets)")
            lines.append(f"- **Product area:** {g['product_area']}")
            if g["sample_subjects"]:
                lines.append(f"- **Sample questions:**")
                for s in g["sample_subjects"][:3]:
                    if s:
                        lines.append(f"  - {s}")
            lines.append("")
    else:
        lines.append("*No gaps found.*\n")

    # Partial coverage
    lines.append("## Partial Coverage — Topics with weak KB match")
    lines.append("")
    if partial:
        for p in partial:
            art_info = ""
            if p["matching_articles"]:
                art_info = f" → closest: `{p['matching_articles'][0]['slug']}`"
            lines.append(f"### {p['topic']}  ({p['ticket_count']} tickets){art_info}")
            lines.append(f"- **Product area:** {p['product_area']}")
            if p["sample_subjects"]:
                lines.append(f"- **Sample questions:**")
                for s in p["sample_subjects"][:3]:
                    if s:
                        lines.append(f"  - {s}")
            lines.append("")
    else:
        lines.append("*No partial matches found.*\n")

    # Well-covered topics
    lines.append("## Well-Covered Topics")
    lines.append("")
    lines.append("| Topic | Tickets | Top KB article |")
    lines.append("|---|---|---|")
    for c in sorted(covered, key=lambda x: x["ticket_count"], reverse=True):
        top_art = c["matching_articles"][0]["slug"] if c["matching_articles"] else "—"
        lines.append(f"| {c['topic']} | {c['ticket_count']} | `{top_art}` |")
    lines.append("")

    # Priority recommendations
    lines.append("## Priority Recommendations")
    lines.append("")
    lines.append("High-impact KB articles to write, ranked by ticket volume:")
    lines.append("")
    priority_items = gaps + [p for p in partial if p["ticket_count"] >= 30]
    priority_items.sort(key=lambda x: x["ticket_count"], reverse=True)
    for i, item in enumerate(priority_items[:10], 1):
        status = "GAP" if item in gaps else "PARTIAL"
        lines.append(f"{i}. **{item['topic']}** — {item['ticket_count']} tickets "
                      f"[{status}] (product area: {item['product_area']})")
    lines.append("")

    report = "\n".join(lines)
    out_path = OUT_DIR / "coverage-report.md"
    out_path.write_text(report, encoding="utf-8")
    print(f"\nWrote {out_path} ({os.path.getsize(out_path)} bytes)")

    # Also save structured data for LLM step
    structured = {
        "gaps": gaps,
        "partial": partial,
        "covered": [{"topic": c["topic"], "ticket_count": c["ticket_count"],
                      "top_match": c["matching_articles"][0]["slug"] if c["matching_articles"] else None}
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
