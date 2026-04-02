#!/usr/bin/env python3
"""
Convert raw Intercom JSON conversations to clean text for kb:intake analysis.

Usage:
    python3 scripts/preprocess_intercom.py              # process all unprocessed
    python3 scripts/preprocess_intercom.py --date 2026-03-14  # specific date

Reads from:  ../help_ingest/intercom/YYYY-MM-DD/conversation-*.json
Writes to:   ../help_ingest/intercom-processed/YYYY-MM-DD.md  (one file per day)
"""

import sys
import json
import re
import argparse
from datetime import datetime
from pathlib import Path

INGEST_RAW = Path(__file__).parent.parent.parent / "help_ingest" / "intercom"
INGEST_OUT = Path(__file__).parent.parent.parent / "help_ingest" / "intercom-processed"


def clean_html(text: str) -> str:
    """Strip basic HTML tags."""
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<p[^>]*>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</p>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&lt;", "<", text)
    text = re.sub(r"&gt;", ">", text)
    return text.strip()


def extract_messages(conv: dict) -> list[dict]:
    """Extract message thread from conversation."""
    messages = []

    # Opening message
    source = conv.get("source", {})
    if source:
        body = clean_html(source.get("body", "") or "")
        author = source.get("author", {})
        role = "customer" if author.get("type") == "user" else "agent"
        if body:
            messages.append({"role": role, "text": body})

    # Conversation parts (replies)
    parts = conv.get("conversation_parts", {}).get("conversation_parts", [])
    for part in parts:
        part_type = part.get("part_type", "")
        body = clean_html(part.get("body", "") or "")
        if not body:
            continue
        author = part.get("author", {})
        author_type = author.get("type", "")

        if author_type in ("bot", "admin"):
            role = "agent"
        elif author_type == "user":
            role = "customer"
        else:
            continue  # skip system notes

        messages.append({"role": role, "text": body})

    return messages


def format_conversation(conv: dict, conv_id: str) -> str:
    """Format a single conversation as readable markdown."""
    created = conv.get("created_at", 0)
    date_str = datetime.fromtimestamp(created).strftime("%Y-%m-%d %H:%M") if created else "unknown"

    tags = [t.get("name", "") for t in conv.get("tags", {}).get("tags", [])]
    tag_str = ", ".join(tags) if tags else "—"

    messages = extract_messages(conv)
    if not messages:
        return ""

    lines = [
        f"## Conversation {conv_id}",
        f"**Date:** {date_str}  |  **Tags:** {tag_str}",
        "",
    ]

    for msg in messages:
        prefix = "**Customer:**" if msg["role"] == "customer" else "**Support:**"
        lines.append(f"{prefix} {msg['text']}")
        lines.append("")

    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def extract_ticket_messages(ticket: dict) -> list[dict]:
    """Extract message thread from a ticket."""
    messages = []

    # Opening message from ticket_parts or source
    source = ticket.get("source", {})
    if source:
        body = clean_html(source.get("body", "") or "")
        author = source.get("author", {})
        role = "customer" if author.get("type") in ("user", "contact") else "agent"
        if body:
            messages.append({"role": role, "text": body})

    # ticket_parts (replies/notes)
    parts = ticket.get("ticket_parts", {}).get("ticket_parts", [])
    for part in parts:
        body = clean_html(part.get("body", "") or "")
        if not body:
            continue
        author = part.get("author", {})
        author_type = author.get("type", "")
        if author_type in ("bot", "admin"):
            role = "agent"
        elif author_type in ("user", "contact"):
            role = "customer"
        else:
            continue

        messages.append({"role": role, "text": body})

    return messages


def format_ticket(ticket: dict, ticket_id: str) -> str:
    """Format a single ticket as readable markdown."""
    created = ticket.get("created_at", 0)
    date_str = datetime.fromtimestamp(created).strftime("%Y-%m-%d %H:%M") if created else "unknown"

    ticket_type = ticket.get("ticket_type", {}).get("name", "ticket") if ticket.get("ticket_type") else "ticket"
    state = ticket.get("state", "—")

    messages = extract_ticket_messages(ticket)
    if not messages:
        return ""

    lines = [
        f"## Ticket {ticket_id}",
        f"**Date:** {date_str}  |  **Type:** {ticket_type}  |  **State:** {state}",
        "",
    ]

    for msg in messages:
        prefix = "**Customer:**" if msg["role"] == "customer" else "**Support:**"
        lines.append(f"{prefix} {msg['text']}")
        lines.append("")

    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def process_date(date_str: str) -> int:
    """Process all conversations and tickets for a given date. Returns count."""
    raw_dir = INGEST_RAW / date_str
    if not raw_dir.exists():
        return 0

    conv_files = sorted(raw_dir.glob("conversation-*.json"))
    ticket_files = sorted(raw_dir.glob("ticket-*.json"))
    if not conv_files and not ticket_files:
        return 0

    INGEST_OUT.mkdir(parents=True, exist_ok=True)
    out_file = INGEST_OUT / f"{date_str}.md"

    total = len(conv_files) + len(ticket_files)
    blocks = [
        f"# Intercom — {date_str}",
        f"*{len(conv_files)} conversations, {len(ticket_files)} tickets*",
        "",
    ]

    processed = 0

    for f in conv_files:
        try:
            conv = json.loads(f.read_text(encoding="utf-8"))
            conv_id = f.stem.replace("conversation-", "")
            block = format_conversation(conv, conv_id)
            if block:
                blocks.append(block)
                processed += 1
        except Exception as e:
            print(f"  WARNING: {f.name}: {e}")

    for f in ticket_files:
        try:
            ticket = json.loads(f.read_text(encoding="utf-8"))
            ticket_id = f.stem.replace("ticket-", "")
            block = format_ticket(ticket, ticket_id)
            if block:
                blocks.append(block)
                processed += 1
        except Exception as e:
            print(f"  WARNING: {f.name}: {e}")

    out_file.write_text("\n".join(blocks), encoding="utf-8")
    return processed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", help="Process specific date (YYYY-MM-DD)")
    args = parser.parse_args()

    if args.date:
        dates = [args.date]
    else:
        if not INGEST_RAW.exists():
            print(f"No raw data at {INGEST_RAW}")
            sys.exit(1)
        dates = sorted([d.name for d in INGEST_RAW.iterdir() if d.is_dir()])

    total = 0
    for date_str in dates:
        count = process_date(date_str)
        if count:
            print(f"  {date_str}: {count} conversations → intercom-processed/{date_str}.md")
            total += count

    print(f"\nDone. {total} conversations preprocessed.")
    print(f"Output: {INGEST_OUT}")
    print("\nNext step: run kb:intake to analyze for KB gaps.")


if __name__ == "__main__":
    main()
