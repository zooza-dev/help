#!/usr/bin/env python3
"""Topical overlap: which parts of the KB answer the same question in different words.

Jaccard over shingles only finds copy-paste. This finds the rest: TF-IDF cosine
over unigrams+bigrams, computed section-to-section and doc-to-doc, with the
inverted index keeping it to the pairs that actually share rare terms.
"""
import json, os, re, glob, html, math, argparse, collections

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CONTENT = os.path.join(REPO, "content")
sys_path = None

STOP = set("""a an the and or but if then than that this these those is are was were be been being am
to of in on at by for with from as it its you your we our they their he she his her him them
do does did doing not no nor so such can could will would should shall may might must need
i me my mine there here what which who whom whose when where why how all any both each few more most
other some only own same too very just also into over under again further once up down out off
click select choose open go set add new use using used want like see also make sure
page screen field button menu tab option list item row name value date time day days
zooza you'll it's don't doesn't won't can't""".split())

def norm_words(t):
    t = re.sub(r"```.*?```", " ", t, flags=re.S)
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).lower()
    t = re.sub(r"[^a-z0-9€]+", " ", t)
    return [w for w in t.split() if w not in STOP and len(w) > 2]

def terms(words):
    out = collections.Counter(words)
    for i in range(len(words)-1):
        out[words[i] + "_" + words[i+1]] += 1
    return out

def frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    fm = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"')
    return fm, text[end+4:]

def sections(body):
    out, cur_h, cur_l, buf = [], "(top)", 1, []
    for line in body.splitlines():
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            out.append((cur_l, cur_h, "\n".join(buf)))
            cur_l, cur_h, buf = len(m.group(1)), m.group(2).strip(), []
        else:
            buf.append(line)
    out.append((cur_l, cur_h, "\n".join(buf)))
    return out

def build(units):
    """units: [{'tf': Counter, ...}] -> adds normalised tf-idf vectors."""
    N = len(units)
    df = collections.Counter()
    for u in units:
        for t in u["tf"]:
            df[t] += 1
    for u in units:
        v = {}
        for t, c in u["tf"].items():
            if df[t] < 2 or df[t] > N * 0.35:    # unique noise / boilerplate
                continue
            v[t] = (1 + math.log(c)) * math.log(N / df[t])
        nrm = math.sqrt(sum(x*x for x in v.values())) or 1.0
        u["v"] = {t: x/nrm for t, x in v.items()}
    return units

def top_pairs(units, thresh, same_doc_ok=False, key="doc"):
    inv = collections.defaultdict(list)
    for i, u in enumerate(units):
        for t, w in u["v"].items():
            inv[t].append((i, w))
    acc = collections.defaultdict(float)
    for t, lst in inv.items():
        if len(lst) > 60:
            continue
        for a in range(len(lst)):
            for b in range(a+1, len(lst)):
                i, wi = lst[a]; j, wj = lst[b]
                if not same_doc_ok and units[i][key] == units[j][key]:
                    continue
                acc[(i, j) if i < j else (j, i)] += wi*wj
    return sorted(((s, i, j) for (i, j), s in acc.items() if s >= thresh), reverse=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sec-thresh", type=float, default=0.33)
    ap.add_argument("--doc-thresh", type=float, default=0.30)
    ap.add_argument("--min-words", type=int, default=30)
    ap.add_argument("--out", default=os.path.join(REPO, "build", "reports", "kb-topics.json"))
    a = ap.parse_args()

    docs, secs = [], []
    for f in sorted(glob.glob(os.path.join(CONTENT, "**", "*.md"), recursive=True)):
        if os.path.basename(f).startswith("_"):
            continue
        fm, body = frontmatter(open(f, encoding="utf-8").read())
        if fm.get("status") not in (None, "published"):
            continue
        rel = os.path.relpath(f, REPO)
        w = norm_words(body)
        docs.append({"doc": rel, "slug": fm.get("slug",""), "type": fm.get("type",""),
                     "area": fm.get("product_area",""), "title": fm.get("title",""),
                     "related": fm.get("related_articles",""), "nw": len(w), "tf": terms(w)})
        for lvl, head, text in sections(body):
            sw = norm_words(text)
            if len(sw) < a.min_words:
                continue
            secs.append({"doc": rel, "head": head, "lvl": lvl, "type": fm.get("type",""),
                         "area": fm.get("product_area",""), "nw": len(sw), "tf": terms(sw)})

    build(docs); build(secs)
    print(f"docs {len(docs)}  sections {len(secs)}")

    dp = top_pairs(docs, a.doc_thresh)
    sp = top_pairs(secs, a.sec_thresh)
    print(f"doc pairs >= {a.doc_thresh}: {len(dp)}")
    print(f"section pairs >= {a.sec_thresh}: {len(sp)}")

    out = {
      "doc_pairs": [{"sim": round(s,3),
                     "a": {k: docs[i][k] for k in ("doc","slug","type","area","title","nw","related")},
                     "b": {k: docs[j][k] for k in ("doc","slug","type","area","title","nw","related")},
                     "terms": sorted(set(docs[i]["v"]) & set(docs[j]["v"]),
                                     key=lambda t: -(docs[i]["v"][t]*docs[j]["v"][t]))[:12]}
                    for s,i,j in dp],
      "sec_pairs": [{"sim": round(s,3),
                     "a": {k: secs[i][k] for k in ("doc","head","type","area","nw")},
                     "b": {k: secs[j][k] for k in ("doc","head","type","area","nw")},
                     "terms": sorted(set(secs[i]["v"]) & set(secs[j]["v"]),
                                     key=lambda t: -(secs[i]["v"][t]*secs[j]["v"][t]))[:12]}
                    for s,i,j in sp],
    }
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    json.dump(out, open(a.out,"w"), ensure_ascii=False, indent=1)
    print("->", a.out)

if __name__ == "__main__":
    main()
