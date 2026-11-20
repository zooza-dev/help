#!/usr/bin/env python3
"""Where two articles cover the same ground and disagree.

Takes the similar section pairs from kb-topics.json and looks inside them for
the three kinds of disagreement that actually reach a customer:

  POLARITY - one says a thing can be done, the other says it cannot
  NUMBER   - the same quantity stated as two different figures
  ROUTE    - the same destination reached by two different menu paths
"""
import json, os, re, collections

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TOPICS = os.path.join(REPO, "build", "reports", "kb-topics.json")

def body(doc, head):
    t = open(os.path.join(REPO, doc), encoding="utf-8").read()
    out, cur, buf = {}, "(top)", []
    for line in t.splitlines():
        m = re.match(r"^#{1,4}\s+(.*)$", line)
        if m:
            out.setdefault(cur, []).append("\n".join(buf)); cur = m.group(1).strip(); buf = []
        else:
            buf.append(line)
    out.setdefault(cur, []).append("\n".join(buf))
    return "\n".join(out.get(head, []))

NEG = re.compile(r"\b(cannot|can't|can not|is not|isn't|does not|doesn't|do not|don't|never|no longer|not possible|impossible|unable|there is no|has no)\b", re.I)
POS = re.compile(r"\b(you can|it is possible|yes[,.]|can be|is possible|able to|always|will be)\b", re.I)
NUM = re.compile(r"(?<![\w.])(\d{1,4})\s*(days?|hours?|minutes?|months?|weeks?|%|€|eur)\b", re.I)
ARROW = re.compile(r"((?:\*\*)?[A-Z][\w &'/()\.\-]{1,30}(?:\*\*)?(?:\s*→\s*(?:\*\*)?[A-Za-z][\w &'/()\.\-]{1,30}(?:\*\*)?)+)")

def verbs(txt):
    """lemma-ish action phrases, to see whether the two texts talk about the same action"""
    return set(re.findall(r"\b(create|delete|cancel|transfer|move|refund|archive|export|import|book|pay|send|edit|change|add|remove|assign|enable|disable|restore|merge|split)\w*\b", txt.lower()))

d = json.load(open(TOPICS))
rows = []
for p in d["sec_pairs"]:
    if p["sim"] < 0.33:
        continue
    ta, tb = body(p["a"]["doc"], p["a"]["head"]), body(p["b"]["doc"], p["b"]["head"])
    if not ta or not tb:
        continue
    flags = []
    # polarity: same action word, opposite modality
    shared_v = verbs(ta) & verbs(tb)
    na, nb = bool(NEG.search(ta)), bool(NEG.search(tb))
    pa, pb = bool(POS.search(ta)), bool(POS.search(tb))
    if shared_v and ((na and pb and not nb) or (nb and pa and not na)):
        flags.append("POLARITY")
    # numbers
    sa = {(n, u.lower().rstrip("s")) for n, u in NUM.findall(ta)}
    sb = {(n, u.lower().rstrip("s")) for n, u in NUM.findall(tb)}
    ua = {u for _, u in sa} & {u for _, u in sb}
    for u in ua:
        va = {n for n, uu in sa if uu == u}
        vb = {n for n, uu in sb if uu == u}
        if va != vb and not (va & vb):
            flags.append(f"NUMBER:{u} {sorted(va)} vs {sorted(vb)}")
    # routes to the same destination
    ra = {" → ".join(x.strip(" *`") for x in re.split("→", m.group(1))) for m in ARROW.finditer(ta)}
    rb = {" → ".join(x.strip(" *`") for x in re.split("→", m.group(1))) for m in ARROW.finditer(tb)}
    dest = collections.defaultdict(set)
    for r in ra | rb:
        dest[r.split("→")[-1].strip().lower()].add(r)
    for k, v in dest.items():
        if len(v) > 1 and any(x in ra for x in v) and any(x in rb for x in v):
            flags.append(f"ROUTE:{k}")
    if flags:
        rows.append({"sim": p["sim"], "flags": sorted(set(flags)),
                     "a": f'{p["a"]["doc"]} :: {p["a"]["head"]}',
                     "b": f'{p["b"]["doc"]} :: {p["b"]["head"]}'})

rows.sort(key=lambda r: (-len(r["flags"]), -r["sim"]))
print(f"pairs with a possible disagreement: {len(rows)}\n")
for r in rows:
    print(f'{r["sim"]:.2f} {",".join(r["flags"])}')
    print(f'   A {r["a"].replace("content/","")}')
    print(f'   B {r["b"].replace("content/","")}')
out = os.path.join(REPO, "build", "reports", "kb-contradictions.json")
json.dump(rows, open(out, "w"), ensure_ascii=False, indent=1)
print("\n->", out)
