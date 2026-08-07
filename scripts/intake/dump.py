#!/usr/bin/env python3
import json, os, textwrap
OUT = "/private/tmp/claude-501/-Users-michaldodok-help/b787eb73-e2ac-4fc3-8dcc-cf32a857708a/scratchpad"

def clip(s, n=1400):
    s = " ".join(s.split()) if len(s) > n * 2 else s
    return s if len(s) <= n else s[:n] + " …[trunc]"

def render(rows, title, path, maxlen=1400):
    L = [f"# {title}", f"*{len(rows)} conversations*", ""]
    for r in rows:
        L.append(f"## {r['date']} — conv {r['id']}  [{r.get('bucket','human')}]")
        meta = f"res={r['resolution_state']} src={r['n_sources']} reask={r['cust_after_bot']} state={r['state']}"
        if r["tags"]:
            meta += f" tags={r['tags']}"
        L.append(f"`{meta}`")
        if r["sources"]:
            L.append("sources: " + "; ".join(x for x in r["sources"] if x))
        L.append("")
        for role, name, body in r["turns"]:
            if role == "noise":
                continue
            tag = {"customer": "**CUSTOMER**", "bot": "_bot_", "human": f"**HUMAN ({name})**", "other": "other"}[role]
            L.append(f"{tag}: {clip(body, maxlen)}")
            L.append("")
        L.append("---\n")
    open(os.path.join(OUT, path), "w").write("\n".join(L))
    print(path, len(rows), os.path.getsize(os.path.join(OUT, path)) // 1024, "KB")

hum = json.load(open(os.path.join(OUT, "human.json")))
bot = json.load(open(os.path.join(OUT, "bot_only.json")))

render(hum, "Human-agent replies (gold standard) 2026-06-24 → 2026-08-06", "PH2_human.md")

for b in ["A_hard_signal", "B_no_kb_source", "C_reask", "D_assumed_with_kb", "E_confirmed"]:
    rows = [r for r in bot if r["bucket"] == b]
    if rows:
        render(rows, f"Bot-only — {b}", f"PH3_{b}.md")
