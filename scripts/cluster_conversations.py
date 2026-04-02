#!/usr/bin/env python3
"""
Cluster Intercom conversations by topic using keyword matching + Claude API.

Usage:
    python3 scripts/cluster_conversations.py

Reads from:  ../help_ingest/intercom-processed/*.md
Writes to:   ../help_ingest/intercom-clusters/
             - report.md       (human-readable summary)
             - clusters.json   (machine-readable)
             - <topic>/        (symlinks or copies per topic)
"""

import os
import sys
import json
import re
from pathlib import Path
from collections import defaultdict

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

try:
    import anthropic
except ImportError:
    print("Missing: pip3 install anthropic")
    sys.exit(1)

INGEST_PROCESSED = Path(__file__).parent.parent.parent / "help_ingest" / "intercom-processed"
CLUSTERS_DIR = Path(__file__).parent.parent.parent / "help_ingest" / "intercom-clusters"

# Topic taxonomy aligned with KB product areas
TOPICS = [
    "registrácia a účet",
    "prihlásenie a prístup",
    "programy a kurzy",
    "lekcie a rozvrh",
    "rezervácie a kapacita",
    "platby a faktúry",
    "objednávky",
    "klienti a kontakty",
    "notifikácie a emaily",
    "widget a integrácia na web",
    "nastavenia",
    "technický problém / bug",
    "iné",
]


def parse_conversations_from_md(md_path: Path) -> list[dict]:
    """Parse individual conversations from a daily .md file."""
    text = md_path.read_text(encoding="utf-8")
    convs = []

    # Split by ## Conversation
    blocks = re.split(r"(?=^## Conversation )", text, flags=re.MULTILINE)
    for block in blocks:
        if not block.strip() or not block.startswith("## Conversation"):
            continue
        # Extract ID
        id_match = re.match(r"## Conversation (\S+)", block)
        conv_id = id_match.group(1) if id_match else "unknown"

        # Extract date
        date_match = re.search(r"\*\*Date:\*\* ([^\s|]+)", block)
        date = date_match.group(1) if date_match else md_path.stem

        # Extract messages
        messages = []
        for m in re.finditer(r"\*\*(Customer|Support):\*\* (.+?)(?=\*\*(?:Customer|Support):\*\*|^---|\Z)",
                             block, re.DOTALL | re.MULTILINE):
            role = m.group(1).lower()
            text = m.group(2).strip()
            if text:
                messages.append(f"{role.upper()}: {text[:300]}")

        if messages:
            convs.append({
                "id": conv_id,
                "date": date,
                "source_file": md_path.name,
                "preview": "\n".join(messages[:4]),  # first 4 messages
            })

    return convs


def cluster_batch(client, conversations: list[dict]) -> list[dict]:
    """Ask Claude to assign topics to a batch of conversations."""
    topics_list = "\n".join(f"- {t}" for t in TOPICS)

    items = []
    for i, c in enumerate(conversations):
        items.append(f"[{i}] ID:{c['id']} ({c['date']})\n{c['preview']}\n")

    prompt = f"""Priraď každej konverzácii jednu tému zo zoznamu.

TÉMY:
{topics_list}

KONVERZÁCIE:
{'---'.join(items)}

Odpovedz VÝHRADNE ako JSON array v tomto formáte (jeden záznam na konverzáciu):
[{{"idx": 0, "topic": "téma zo zoznamu", "summary": "1 veta čo riešil zákazník"}}]

Žiadny iný text okrem JSON."""

    resp = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}]
    )

    text = resp.content[0].text.strip()
    # Extract JSON array
    match = re.search(r'\[.*\]', text, re.DOTALL)
    if match:
        return json.loads(match.group())
    return []


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set in .env")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    # Load all conversations
    md_files = sorted(INGEST_PROCESSED.glob("*.md"))
    if not md_files:
        print(f"No files in {INGEST_PROCESSED}")
        sys.exit(1)

    print(f"Loading conversations from {len(md_files)} daily files...")
    all_convs = []
    for f in md_files:
        batch = parse_conversations_from_md(f)
        all_convs.extend(batch)

    print(f"Total: {len(all_convs)} conversations\n")

    # Cluster in batches of 10
    BATCH = 10
    results = []
    for i in range(0, len(all_convs), BATCH):
        batch = all_convs[i:i+BATCH]
        print(f"Clustering {i+1}–{min(i+BATCH, len(all_convs))}...", end=" ", flush=True)
        try:
            batch_results = cluster_batch(client, batch)
            for r in batch_results:
                idx = r.get("idx", 0)
                if idx < len(batch):
                    conv = batch[idx]
                    results.append({
                        "id": conv["id"],
                        "date": conv["date"],
                        "source_file": conv["source_file"],
                        "topic": r.get("topic", "iné"),
                        "summary": r.get("summary", ""),
                    })
            print(f"ok ({len(batch_results)} assigned)")
        except Exception as e:
            print(f"ERROR: {e}")
            # Fallback: assign "iné"
            for conv in batch:
                results.append({**conv, "topic": "iné", "summary": ""})

    # Group by topic
    by_topic = defaultdict(list)
    for r in results:
        by_topic[r["topic"]].append(r)

    # Save clusters.json
    CLUSTERS_DIR.mkdir(parents=True, exist_ok=True)
    clusters_file = CLUSTERS_DIR / "clusters.json"
    clusters_file.write_text(json.dumps(by_topic, ensure_ascii=False, indent=2), encoding="utf-8")

    # Save per-topic files
    for topic, convs in by_topic.items():
        safe_name = re.sub(r"[^\w\s-]", "", topic).strip().replace(" ", "-")
        topic_file = CLUSTERS_DIR / f"{safe_name}.md"
        lines = [f"# Téma: {topic}", f"*{len(convs)} konverzácií*", ""]
        for c in sorted(convs, key=lambda x: x["date"]):
            lines.append(f"## {c['date']} — konverzácia {c['id']}")
            lines.append(f"*{c['summary']}*")
            lines.append(f"Zdroj: `{c['source_file']}`")
            lines.append("")
        topic_file.write_text("\n".join(lines), encoding="utf-8")

    # Write report.md
    report_lines = [
        "# Intercom — prehľad tém",
        f"*{len(all_convs)} konverzácií celkom*",
        "",
        "| Téma | Počet | Súbor |",
        "|------|------:|-------|",
    ]
    for topic in sorted(by_topic.keys(), key=lambda t: -len(by_topic[t])):
        count = len(by_topic[topic])
        safe_name = re.sub(r"[^\w\s-]", "", topic).strip().replace(" ", "-")
        report_lines.append(f"| {topic} | {count} | [{safe_name}.md]({safe_name}.md) |")

    report_lines += ["", "## Konverzácie podľa témy", ""]
    for topic in sorted(by_topic.keys(), key=lambda t: -len(by_topic[t])):
        report_lines.append(f"### {topic} ({len(by_topic[topic])})")
        for c in by_topic[topic]:
            report_lines.append(f"- **{c['date']}** {c['summary']}")
        report_lines.append("")

    report_file = CLUSTERS_DIR / "report.md"
    report_file.write_text("\n".join(report_lines), encoding="utf-8")

    print(f"\n--- VÝSLEDOK ---")
    for topic in sorted(by_topic.keys(), key=lambda t: -len(by_topic[t])):
        print(f"  {len(by_topic[topic]):3d}x  {topic}")
    print(f"\nReport: {report_file}")


if __name__ == "__main__":
    main()
