#!/usr/bin/env python3
"""Why did a human have to step in?

Reads the triaged human-reply conversations and, for each, assembles the
evidence needed to name the cause: what was asked, whether the bot tried,
what it cited, what the human actually said, and whether the KB could have
answered it at all (BM25 probe over the exported chunks).
"""
import json, os, re, sys, argparse, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_retrieval import BM25, load

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

ASK_HUMAN = re.compile(r"\b(talk to|speak to|speak with|real person|human|agent|support team|someone from|kontaktovat|clovek|živ[ýy] člov|operátor)\b", re.I)
ACCOUNT_ACTION = re.compile(r"\b(I(?:'ve| have)? (?:fixed|corrected|refunded|deleted|restored|changed|updated|added|removed|re-?sent|resent|re-?issued|cancelled|merged|imported)|we(?:'ve| have) (?:fixed|corrected|deployed|released|pushed)|opravil|opravili|nastavil|nastavili|zmenil|zmazal|poslal|pridal|som to)\b", re.I)
BUG = re.compile(r"\b(bug|chyba|nefunguje|doesn'?t work|not working|error|broken|rozbit|zlyhal|fails?|failed|can'?t (?:see|open|load)|nejde)\b", re.I)
PROMISE = re.compile(r"\b(we(?:'ll| will) (?:add|look|check|fix|release|deploy)|I(?:'ll| will) (?:check|look|ask|pass|forward)|pozriem|pozrieme|skontrolujem|dame vediet|dáme vedieť|nahlásim)\b", re.I)
ASKS_FOR_DETAIL = re.compile(r"\b(could you (?:send|share|give)|can you (?:send|share|tell)|which (?:booking|client|class)|screenshot|poslat|pošlete|posli|aký|ktor[ýá])\b", re.I)

def clip(t, n=700):
    t = re.sub(r"\s+", " ", t or "").strip()
    return t[:n] + ("…" if len(t) > n else "")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--human", default=os.path.join(REPO, "build", "intake", "month", "human.json"))
    ap.add_argument("--out", default=os.path.join(REPO, "build", "reports", "human-why.json"))
    ap.add_argument("--md", default=os.path.join(REPO, "build", "reports", "human-why.md"))
    a = ap.parse_args()

    rows = json.load(open(a.human))
    idx = BM25(load())
    out = []
    for r in rows:
        turns = r["turns"]
        cust = [t for t in turns if t[0] == "customer"]
        bots = [t for t in turns if t[0] == "bot"]
        hums = [t for t in turns if t[0] == "human" and len(t[2]) > 30]
        if not hums:
            continue
        first_human_at = next(i for i, t in enumerate(turns) if t[0] == "human" and len(t[2]) > 30)
        bot_before = [t for t in turns[:first_human_at] if t[0] == "bot"]
        cust_before = [t for t in turns[:first_human_at] if t[0] == "customer"]
        q = " \n".join(t[2] for t in cust_before[:3]) or (cust[0][2] if cust else "")
        hits = idx.search(q, 4) if q.strip() else []
        htxt = " ".join(t[2] for t in hums)
        out.append({
            "id": r["id"], "day": r["day"], "state": r.get("state"),
            "n_cust": len(cust), "n_bot": len(bots), "n_human": len(hums),
            "bot_tried": len(bot_before) > 0,
            "bot_turns_before": len(bot_before),
            "cited": r.get("sources") or [],
            "resolution_state": r.get("resolution_state"),
            "cust_after_bot": r.get("cust_after_bot"),
            "tags": r.get("tags") or [],
            "flags": sorted({k for k, rx in (("asked_for_human", ASK_HUMAN), ("bug_words", BUG))
                             if rx.search(q)} |
                            {k for k, rx in (("human_did_action", ACCOUNT_ACTION),
                                             ("human_promised", PROMISE),
                                             ("human_asked_detail", ASKS_FOR_DETAIL))
                             if rx.search(htxt)}),
            "question": clip(q, 900),
            "bot_said": clip(" ".join(t[2] for t in bot_before), 500),
            "human_said": clip(htxt, 900),
            "kb_hits": [{"slug": d["slug"], "head": d["head"][:70], "score": s} for d, s in hits],
        })
    out.sort(key=lambda r: r["day"])
    json.dump(out, open(a.out, "w"), ensure_ascii=False, indent=1)

    with open(a.md, "w", encoding="utf-8") as f:
        f.write(f"# Human interventions — {out[0]['day']} to {out[-1]['day']}\n\n{len(out)} conversations\n\n")
        for r in out:
            f.write(f"\n## `{r['id']}` {r['day']}  "
                    f"[bot tried: {'yes' if r['bot_tried'] else 'NO'}; cust turns {r['n_cust']}; flags: {', '.join(r['flags']) or '-'}]\n\n")
            f.write(f"**Q** {r['question']}\n\n")
            if r["bot_said"]:
                f.write(f"**Bot** {r['bot_said']}\n\n")
            if r["cited"]:
                f.write(f"*cited:* {', '.join(x for x in r['cited'] if x)}\n\n")
            f.write(f"**Human** {r['human_said']}\n\n")
            f.write("*KB probe:* " + "; ".join(f"{h['slug']}::{h['head']} ({h['score']})" for h in r["kb_hits"]) + "\n")
    print(f"{len(out)} conversations -> {a.md}")
    print("bot tried first:", sum(1 for r in out if r["bot_tried"]), " / human answered cold:", sum(1 for r in out if not r["bot_tried"]))
    print("flags:", collections.Counter(f for r in out for f in r["flags"]))

if __name__ == "__main__":
    main()
