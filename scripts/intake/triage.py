#!/usr/bin/env python3
"""Triage Intercom conversations in a date window into human-reply vs bot-only,
carrying ai_agent signals (resolution_state, content_sources, last_answer_type).

Defaults reproduce the original July 2026 intake run. The weekly job passes its
own window via --start/--end.
"""
import json, glob, re, html, collections, os, sys, argparse
from datetime import datetime, timezone

_REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

_ap = argparse.ArgumentParser()
_ap.add_argument("--start", default="2026-06-24", help="first day of window (YYYY-MM-DD, inclusive)")
_ap.add_argument("--end", default="2026-08-06", help="last day of window (YYYY-MM-DD, inclusive)")
_ap.add_argument("--ingest", default="/Users/michaldodok/help_ingest/intercom")
_ap.add_argument("--out", default=os.path.join(_REPO, "build", "intake"))
_args = _ap.parse_args()

ING = _args.ingest
OUT = _args.out
START, END = _args.start, _args.end
os.makedirs(OUT, exist_ok=True)

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


def last_activity(c):
    """When this conversation was last touched, not when it was opened.

    A conversation opened before the window and answered inside it belongs to
    this week -- that human answer is the thing the intake exists to find.
    Filtering on created_at dropped it, and folder names are created_at, so the
    folder cannot be trusted either.

    Deliberately NOT updated_at: that moves when anyone closes, snoozes or tags
    a conversation, so a bulk close would drag a month-old thread into this week
    and bury the real ones. The last actual message is what "last communication"
    means.
    """
    stamps = [c.get("created_at") or 0]
    for part in (c.get("conversation_parts") or {}).get("conversation_parts", []):
        if part.get("body"):                       # a message, not a state change
            stamps.append(part.get("created_at") or 0)
    return max(stamps)


def conversation_files():
    """Every conversation on disk, wherever it was filed."""
    return sorted(glob.glob(os.path.join(ING, "*", "conversation-*.json")))


rows = []
for f in conversation_files():
    c = json.load(open(f))
    touched = last_activity(c)
    day = datetime.fromtimestamp(touched, timezone.utc).strftime("%Y-%m-%d")
    if not (START <= day <= END):
        continue
    cid = c.get("id")
    ts = datetime.fromtimestamp(touched, timezone.utc).strftime("%Y-%m-%d %H:%M")
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
        "id": cid, "date": ts, "day": day, "file": f,
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


# Cold outreach that lands in the support inbox. It always looks like
# B_no_kb_source -- the bot cites nothing because there is nothing to cite --
# so without this it dominates the highest-risk bucket.
SPAM = re.compile(
    r"(upvote\.network|launchbuff|launchstag|krispitech|product hunt|"
    r"free listing|permanent backlink|packages from \$|\$\d+/upvote|"
    r"we (?:spotted|came across|found your product)|SEO-indexed)",
    re.I,
)


def is_spam(r):
    for role, _, text in r.get("turns", []):
        if role == "customer" and SPAM.search(text or ""):
            return True
    return False


def bucket(r):
    if is_spam(r):
        return "F_spam"
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
