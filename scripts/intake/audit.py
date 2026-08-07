#!/usr/bin/env python3
"""Coverage audit: disposition of every one of the 281 conversations."""
import json, os, re

OUT = "/private/tmp/claude-501/-Users-michaldodok-help/b787eb73-e2ac-4fc3-8dcc-cf32a857708a/scratchpad"
REPO = "/Users/michaldodok/help"

rows = json.load(open(os.path.join(OUT, "triage.json")))

# every conversation id cited anywhere in the two reports
cited = set()
for f in ["build/reports/intercom-july-2026-review.md",
          "build/reports/intercom-july-2026-bot-only.md"]:
    txt = open(os.path.join(REPO, f)).read()
    cited |= set(re.findall(r"\b(2154\d{11})\b", txt))

SPAM = re.compile(r"promotional|spam|irrelevant to (customer )?support", re.I)

buckets = {}
unaccounted = []

for r in rows:
    cid = str(r["id"])
    turns = r["turns"]
    cust = [t for t in turns if t[0] == "customer" and len(t[2].strip()) > 30]
    bot = [t for t in turns if t[0] == "bot"]
    human = [t for t in turns if t[0] == "human" and len(t[2].strip()) > 30]

    if cid in cited:
        d = "1 · nález v reporte"
    elif not cust and not human:
        d = "2 · len potvrdenie ticketu, žiadna otázka"
    elif bot and any(SPAM.search(b[2]) for b in bot) and not human:
        d = "3 · spam / obchodná ponuka"
    elif r["resolution_state"] == "confirmed_resolution" and not human:
        d = "4 · klient potvrdil, bot stačil"
    elif not cust and human:
        d = "5 · e-mailové vlákno, riešené mimo chatu"
    elif r["cust_after_bot"] <= 1 and not human and r["n_sources"] > 0:
        d = "6 · jednoduchá otázka, bot odpovedal z KB"
    else:
        d = "7 · NEZARADENÉ — skontrolovať"
        unaccounted.append(r)

    buckets.setdefault(d, []).append(cid)

print(f"SPOLU: {len(rows)} konverzácií | citovaných v reportoch: {len(cited)}\n")
for k in sorted(buckets):
    print(f"{k:46s} {len(buckets[k]):3d}")

print(f"\n{'='*70}\nNEZARADENÉ ({len(unaccounted)}) — tieto treba pozrieť ručne:\n")
for r in unaccounted:
    q = next((t[2] for t in r["turns"] if t[0] == "customer" and len(t[2].strip()) > 30), "")
    q = " ".join(q.split())[:150]
    print(f"{r['id']}  {r['date']}  human={'A' if any(t[0]=='human' for t in r['turns']) else 'N'}"
          f"  reask={r['cust_after_bot']}  res={r['resolution_state']}")
    print(f"    {q}\n")

json.dump([r["id"] for r in unaccounted], open(os.path.join(OUT, "unaccounted.json"), "w"))
