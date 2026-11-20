#!/usr/bin/env python3
"""Navigation-cue consistency: every "Settings → X → Y" in content/, grouped.

Two kinds of inconsistency matter:
  SAME DESTINATION, DIFFERENT ROUTE - the last segment is identical but the
      path leading to it differs, so one of them is wrong or stale.
  SAME ROUTE, DIFFERENT CASING/WORDING - cosmetic drift that still makes the
      KB look unreliable and breaks exact-match retrieval.
"""
import re, os, glob, json, collections, html

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CONTENT = os.path.join(REPO, "content")
ARROW = re.compile(r"((?:\*\*)?[A-Z][\w &'/()\.\-]{1,34}(?:\*\*)?(?:\s*(?:→|->|›|»)\s*(?:\*\*)?[A-Za-z][\w &'/()\.\-]{1,34}(?:\*\*)?)+)")

def clean(seg):
    s = seg.replace("**", "").replace("`", "").strip(" .,:;")
    s = re.sub(r"\s+", " ", s)
    return s

rows = []
for f in sorted(glob.glob(os.path.join(CONTENT, "**", "*.md"), recursive=True)):
    txt = open(f, encoding="utf-8").read()
    rel = os.path.relpath(f, REPO)
    for i, line in enumerate(txt.splitlines(), 1):
        for m in ARROW.finditer(line):
            parts = [clean(p) for p in re.split(r"→|->|›|»", m.group(1))]
            parts = [p for p in parts if p]
            if len(parts) < 2:
                continue
            rows.append({"doc": rel, "line": i, "path": parts, "raw": " → ".join(parts)})

print(f"navigation cues: {len(rows)} in {len({r['doc'] for r in rows})} docs")

# same last segment, different full path
by_dest = collections.defaultdict(set)
where = collections.defaultdict(list)
for r in rows:
    key = r["path"][-1].lower()
    by_dest[key].add(r["raw"])
    where[(key, r["raw"])].append(f'{r["doc"].replace("content/","")}:{r["line"]}')

conflicts = {k: sorted(v) for k, v in by_dest.items() if len(v) > 1}
print(f"destinations reached by more than one stated route: {len(conflicts)}")

# casing drift on the same segment
seg_forms = collections.defaultdict(collections.Counter)
for r in rows:
    for p in r["path"]:
        seg_forms[p.lower()][p] += 1
drift = {k: dict(v) for k, v in seg_forms.items() if len(v) > 1}
print(f"segments written more than one way: {len(drift)}")

out = os.path.join(REPO, "build", "reports", "kb-paths.json")
json.dump({"rows": rows, "conflicts": conflicts, "drift": drift,
           "where": {f"{k[0]}||{k[1]}": v for k, v in where.items()}},
          open(out, "w"), ensure_ascii=False, indent=1)
print("->", out)
