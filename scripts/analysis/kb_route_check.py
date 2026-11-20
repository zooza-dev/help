#!/usr/bin/env python3
"""Check every navigation cue in content/ against the generated app map.

A cue whose last segment names a real screen must state that screen's real
menu path. Anything else is drift: either the route is stale, or the label
belongs to a different screen with the same name.
"""
import re, os, glob, json, collections

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MAP = os.path.join(REPO, "build", "app-map", "app-map.yml")
CONTENT = os.path.join(REPO, "content")

txt = open(MAP, encoding="utf-8").read()
screens = []
for b in re.split(r"\n- id: ", txt)[1:]:
    d = {"id": b.splitlines()[0].strip()}
    for k in ("menu", "title", "route", "area"):
        m = re.search(rf"^\s*{k}: (.*)$", b, re.M)
        if m:
            d[k] = m.group(1).strip()
    screens.append(d)

by_title = collections.defaultdict(list)
for s in screens:
    if s.get("title"):
        by_title[s["title"].lower()].append(s)

ARROW = re.compile(r"((?:\*\*)?[A-Z][\w &'/()\.\-]{1,34}(?:\*\*)?(?:\s*(?:→|->|›|»)\s*(?:\*\*)?[A-Za-z][\w &'/()\.\-]{1,34}(?:\*\*)?)+)")
def clean(s):
    return re.sub(r"\s+", " ", s.replace("**", "").replace("`", "").strip(" .,:;"))

# segments that only describe how you got somewhere, not a menu item
NAVY = re.compile(r"^(go to|open|open the|the|select|select the|click|click the|choose|a |an )", re.I)

rows, ok, drift, ambiguous = [], 0, [], []
for f in sorted(glob.glob(os.path.join(CONTENT, "**", "*.md"), recursive=True)):
    rel = os.path.relpath(f, REPO)
    for i, line in enumerate(open(f, encoding="utf-8").read().splitlines(), 1):
        for m in ARROW.finditer(line):
            parts = [clean(p) for p in re.split(r"→|->|›|»", m.group(1)) if clean(p)]
            if len(parts) < 2:
                continue
            dest = parts[-1]
            cands = by_title.get(dest.lower())
            if not cands:
                continue
            stated = " → ".join(parts)
            # strip leading verbs for comparison
            core = [p for p in parts if not NAVY.match(p)]
            core_s = " → ".join(core)
            menus = {c["menu"] for c in cands if c.get("menu")}
            hit = any(core_s.lower() == mm.lower() or mm.lower().endswith(core_s.lower()) for mm in menus)
            rec = {"doc": rel, "line": i, "stated": stated, "core": core_s,
                   "dest": dest, "menus": sorted(menus),
                   "ids": sorted(c["id"] for c in cands)}
            if hit:
                ok += 1
            elif len(menus) > 1:
                ambiguous.append(rec)
            else:
                drift.append(rec)
            rows.append(rec)

print(f"cues naming a known screen: {len(rows)}   conforming: {ok}   drift: {len(drift)}   ambiguous: {len(ambiguous)}")
out = os.path.join(REPO, "build", "reports", "kb-routes.json")
json.dump({"drift": drift, "ambiguous": ambiguous}, open(out, "w"), ensure_ascii=False, indent=1)

agg = collections.Counter((d["dest"], d["core"], d["menus"][0] if d["menus"] else "") for d in drift)
print("\nmost common wrong routes:")
for (dest, core, real), n in agg.most_common(25):
    print(f'  {n:3d}x  "{core}"   ->  real: "{real}"')
print("->", out)
