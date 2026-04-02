#!/usr/bin/env python3
"""
Fetch Intercom conversations AND tickets incrementally into ../help_ingest/intercom/

Usage:
    python3 scripts/fetch_intercom.py           # fetch since last watermark
    python3 scripts/fetch_intercom.py --all     # fetch all (ignores watermark)
    python3 scripts/fetch_intercom.py --days 7  # fetch last N days

Token: set INTERCOM_TOKEN in .env or environment.
"""

import os
import sys
import json
import time
import argparse
from datetime import datetime, timezone, timedelta
from pathlib import Path

try:
    import requests
except ImportError:
    print("Missing: pip install requests")
    sys.exit(1)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # .env optional

# --- Config ---
INGEST_DIR = Path(__file__).parent.parent.parent / "help_ingest" / "intercom"
WATERMARK_FILE = Path(__file__).parent / ".intercom_watermark"
API_BASE = "https://api.intercom.io"
PAGE_SIZE = 150  # max allowed


def get_token() -> str:
    token = os.environ.get("INTERCOM_TOKEN", "")
    if not token:
        print("ERROR: INTERCOM_TOKEN not set. Add it to .env or export it.")
        sys.exit(1)
    return token


def fetch_conversations(token: str, created_after: int) -> list[dict]:
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "Intercom-Version": "2.11",
    }
    conversations = []
    url = f"{API_BASE}/conversations"
    params = {
        "per_page": PAGE_SIZE,
        "sort_field": "created_at",
        "sort_order": "asc",
    }

    # Use search endpoint for date filtering
    search_url = f"{API_BASE}/conversations/search"
    body = {
        "query": {
            "operator": "AND",
            "value": [
                {
                    "field": "created_at",
                    "operator": ">",
                    "value": created_after,
                }
            ]
        },
        "pagination": {"per_page": PAGE_SIZE}
    }

    page = 1
    while True:
        print(f"  Fetching page {page}...", end=" ", flush=True)
        resp = requests.post(search_url, headers=headers, json=body)
        if resp.status_code != 200:
            print(f"\nERROR {resp.status_code}: {resp.text[:200]}")
            break

        data = resp.json()
        batch = data.get("conversations", [])
        conversations.extend(batch)
        print(f"{len(batch)} conversations")

        # Pagination
        pages = data.get("pages", {})
        next_cursor = pages.get("next", {})
        if not next_cursor or not batch:
            break

        body["pagination"] = next_cursor
        page += 1
        time.sleep(0.5)  # rate limit courtesy

    return conversations


def fetch_conversation_detail(token: str, conv_id: str) -> dict:
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "Intercom-Version": "2.11",
    }
    url = f"{API_BASE}/conversations/{conv_id}"
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        return resp.json()
    return {}


def fetch_tickets(token: str, created_after: int) -> list[dict]:
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "Intercom-Version": "2.11",
    }
    search_url = f"{API_BASE}/tickets/search"
    body = {
        "query": {
            "operator": "AND",
            "value": [
                {
                    "field": "created_at",
                    "operator": ">",
                    "value": created_after,
                }
            ]
        },
        "pagination": {"per_page": PAGE_SIZE}
    }

    tickets = []
    page = 1
    while True:
        print(f"  [tickets] Fetching page {page}...", end=" ", flush=True)
        resp = requests.post(search_url, headers=headers, json=body)
        if resp.status_code == 404:
            print("tickets endpoint not available (feature not enabled)")
            break
        if resp.status_code != 200:
            print(f"\nERROR {resp.status_code}: {resp.text[:200]}")
            break

        data = resp.json()
        batch = data.get("tickets", [])
        tickets.extend(batch)
        print(f"{len(batch)} tickets")

        pages = data.get("pages", {})
        next_cursor = pages.get("next", {})
        if not next_cursor or not batch:
            break

        body["pagination"] = next_cursor
        page += 1
        time.sleep(0.5)

    return tickets


def fetch_ticket_detail(token: str, ticket_id: str) -> dict:
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "Intercom-Version": "2.11",
    }
    url = f"{API_BASE}/tickets/{ticket_id}"
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        return resp.json()
    return {}


def save_conversation(conv: dict, date_str: str):
    out_dir = INGEST_DIR / date_str
    out_dir.mkdir(parents=True, exist_ok=True)
    conv_id = conv.get("id", "unknown")
    out_file = out_dir / f"conversation-{conv_id}.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(conv, f, ensure_ascii=False, indent=2)


def save_ticket(ticket: dict, date_str: str):
    out_dir = INGEST_DIR / date_str
    out_dir.mkdir(parents=True, exist_ok=True)
    ticket_id = ticket.get("id", "unknown")
    out_file = out_dir / f"ticket-{ticket_id}.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(ticket, f, ensure_ascii=False, indent=2)


def read_watermark() -> int:
    if WATERMARK_FILE.exists():
        return int(WATERMARK_FILE.read_text().strip())
    # Default: 90 days ago
    return int((datetime.now(timezone.utc) - timedelta(days=90)).timestamp())


def write_watermark(ts: int):
    WATERMARK_FILE.write_text(str(ts))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="Fetch all (ignore watermark)")
    parser.add_argument("--days", type=int, help="Fetch last N days")
    args = parser.parse_args()

    token = get_token()

    if args.all:
        created_after = 0
        print("Fetching ALL conversations (no watermark)")
    elif args.days:
        created_after = int((datetime.now(timezone.utc) - timedelta(days=args.days)).timestamp())
        print(f"Fetching last {args.days} days")
    else:
        created_after = read_watermark()
        dt = datetime.fromtimestamp(created_after, tz=timezone.utc)
        print(f"Fetching since {dt.strftime('%Y-%m-%d %H:%M UTC')} (watermark)")

    print(f"Output: {INGEST_DIR}\n")

    # --- Conversations ---
    conversations = fetch_conversations(token, created_after)
    print(f"\nConversations fetched: {len(conversations)}")

    newest_ts = created_after
    for i, conv in enumerate(conversations):
        conv_id = conv.get("id", "unknown")
        created = conv.get("created_at", 0)
        date_str = datetime.fromtimestamp(created, tz=timezone.utc).strftime("%Y-%m-%d")

        print(f"  [{i+1}/{len(conversations)}] detail {conv_id}...", end=" ", flush=True)
        detail = fetch_conversation_detail(token, conv_id)
        if detail:
            conv = detail
        print("ok")
        time.sleep(0.3)

        save_conversation(conv, date_str)
        if created > newest_ts:
            newest_ts = created

    # --- Tickets ---
    print("\nFetching tickets...")
    tickets = fetch_tickets(token, created_after)
    print(f"Tickets fetched: {len(tickets)}")

    for i, ticket in enumerate(tickets):
        ticket_id = ticket.get("id", "unknown")
        created = ticket.get("created_at", 0)
        date_str = datetime.fromtimestamp(created, tz=timezone.utc).strftime("%Y-%m-%d")

        print(f"  [{i+1}/{len(tickets)}] ticket detail {ticket_id}...", end=" ", flush=True)
        detail = fetch_ticket_detail(token, ticket_id)
        if detail:
            ticket = detail
        print("ok")
        time.sleep(0.3)

        save_ticket(ticket, date_str)
        if created > newest_ts:
            newest_ts = created

    if newest_ts == created_after:
        print("\nNothing new.")
        return

    write_watermark(newest_ts + 1)
    print(f"\nSaved to {INGEST_DIR}")
    print(f"Watermark updated to {datetime.fromtimestamp(newest_ts, tz=timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")


if __name__ == "__main__":
    main()
