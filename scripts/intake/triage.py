#!/usr/bin/env python3
"""Triage Intercom conversations 2026-06-24 -> 2026-08-06 into human-reply vs bot-only,
carrying ai_agent signals (resolution_state, content_sources, last_answer_type)."""
import json, glob, re, html, collections, os, sys
from datetime import datetime, timezone

ING = "/Users/michaldodok/help_ingest/intercom"
OUT = "/private/tmp/claude-501/-Users-michaldodok-help/b787eb73-e2ac-4fc3-8dcc-cf32a857708a/scratchpad"
START, END = "2026-06-24", "2026-08-06"

HUMAN_NAMES = {"Martin Rapavý", "Tech Support", "Katarína Babiaková"}
BOT_NAMES = {"Zooza Support", "Zooza Assistant", "Fin", "bot"}
# automated admin notes that are not real human answers
NOISE = re.compile(r"(Jira issue creation failed|\[Jira for Intercom|your ticket\s+has been received|Zooza Assistant will try to help)", re.I)


def strip(h_):
    if not h_:
        return ""
    t = re.sub(r"<br\s*/?>", "\n", h_)
    t = re.sub(r"</p>", "\n\n", t)
    t = re.sub(r"<li>", "\n- ", t)
    t = re.sub(r"<[^>]+>", "", t)
    return html.unescape(t).strip()


def dirs():
    for d in sorted(os.listdir(ING)):
        if START <= d <= END and os.path.isdir(os.path.join(ING, d)):
            yield d


rows = []
for d in dirs():
    for f in sorted(glob.glob(os.path.join(ING, d, "conversation-*.json"))):
        c = json.load(open(f))
        cid = c.get("id")
        ts = datetime.fromtimestamp(c.get("created_at", 0), timezone.utc).strftime("%Y-%m-%d %H:%M")
        src = c.get("source") or {}
        sa = src.get("author") or {}
        turns = []
        first_q = strip(src.get("body"))
        if first_q and sa.get("type") in ("user", "lead"):
            turns.append(("customer", sa.get("name"), first_q))
        for p in (c.get("conversation_parts") or {}).get("conversation_parts", []):
            a = p.get("author") or {}
            body = strip(p.get("body"))
            if not body:
                continue
            at, an = a.get("type"), a.get("name")
            if at in ("user", "lead"):
                role = "customer"
            elif at == "bot" or an in BOT_NAMES:
                role = "bot"
            elif at == "admin":
                role = "noise" if NOISE.search(body) else "human"
            else:
                role = "other"
            turns.append((role, an, body))

        human_turns = [t for t in turns if t[0] == "human" and len(t[2]) > 30]
        ai = c.get("ai_agent") or {}
        cs = (ai.get("content_sources") or {}).get("content_sources", []) or []
        rating = c.get("conversation_rating") or {}
        # customer re-ask signal: >=2 customer turns after first bot reply
        cust_after_bot = 0
        seen_bot = False
        for r, _, _ in turns:
            if r == "bot":
                seen_bot = True
            elif r == "customer" and seen_bot:
                cust_after_bot += 1

        rows.append({
            "id": cid, "date": ts, "day": d, "file": f,
            "has_human": bool(human_turns),
            "n_human": len(human_turns),
            "resolution_state": ai.get("resolution_state"),
            "last_answer_type": ai.get("last_answer_type"),
            "n_sources": len(cs),
            "sources": [s.get("title") for s in cs],
            "source_types": sorted({s.get("content_type") for s in cs}),
            "rating": rating.get("rating"),
            "rating_remark": rating.get("rating_remark"),
            "state": c.get("state"),
            "cust_after_bot": cust_after_bot,
            "tags": [t.get("name") for t in (c.get("tags") or {}).get("tags", [])],
            "turns": turns,
        })

json.dump(rows, open(os.path.join(OUT, "triage.json"), "w"), ensure_ascii=False, indent=1)

hum = [r for r in rows if r["has_human"]]
bot = [r for r in rows if not r["has_human"]]
print(f"TOTAL {len(rows)}  |  human-reply {len(hum)}  |  bot-only {len(bot)}")
print()
print("bot-only resolution_state:", dict(collections.Counter(r["resolution_state"] for r in bot)))
print("bot-only last_answer_type:", dict(collections.Counter(r["last_answer_type"] for r in bot)))
print("bot-only ratings:", dict(collections.Counter(r["rating"] for r in bot if r["rating"])))
print()


def bucket(r):
    if r["resolution_state"] in ("routed_to_team", "abandoned"):
        return "A_hard_signal"
    if r["rating"] is not None and r["rating"] <= 3:
        return "A_hard_signal"
    if r["n_sources"] == 0:
        return "B_no_kb_source"
    if r["cust_after_bot"] >= 2:
        return "C_reask"
    if r["resolution_state"] == "confirmed_resolution":
        return "E_confirmed"
    return "D_assumed_with_kb"


bk = collections.Counter(bucket(r) for r in bot)
print("bot-only buckets:")
for k in sorted(bk):
    print(f"  {k:22s} {bk[k]}")

for r in bot:
    r["bucket"] = bucket(r)
json.dump(bot, open(os.path.join(OUT, "bot_only.json"), "w"), ensure_ascii=False, indent=1)
json.dump(hum, open(os.path.join(OUT, "human.json"), "w"), ensure_ascii=False, indent=1)

# most-cited KB sources among bot-only
cite = collections.Counter()
for r in bot:
    for s in r["sources"]:
        cite[s] += 1
print("\ntop cited sources (bot-only):")
for k, v in cite.most_common(20):
    print(f"  {v:3d}  {k}")
