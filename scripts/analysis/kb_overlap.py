#!/usr/bin/env python3
"""Corpus-wide duplication and overlap map for content/.

Three passes, each answering a different question:

  1. SECTION PAIRS   - which two H2/H3 sections across the KB say the same thing
  2. PARAGRAPH CLONES- which exact/near-exact paragraphs appear in several files
  3. HEADING CLONES  - which headings are repeated across files

Similarity is Jaccard over word 4-shingles of the normalised text, which
survives rewording better than diffing and does not care about ordering.
"""
import json, os, re, sys, glob, html, argparse, collections, itertools

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CONTENT = os.path.join(REPO, "content")

STOP = set("""a an the and or but if then than that this these those is are was were be been being
to of in on at by for with from as it its it's you your we our they their he she his her
do does did not no nor so such can could will would should may might must i me my
there here what which who whom when where why how all any both each few more most other some
only own same too very just also into over under again further once up down out off""".split())

def norm(t):
    t = re.sub(r"`[^`]*`", " ", t)
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t).lower()
    t = re.sub(r"[^a-z0-9→&€ ]+", " ", t)
    return [w for w in t.split() if w not in STOP and len(w) > 1]

def shingles(words, k=4):
    if len(words) < k:
        return {" ".join(words)} if words else set()
    return {" ".join(words[i:i+k]) for i in range(len(words)-k+1)}

def jac(a, b):
    if not a or not b:
        return 0.0
    i = len(a & b)
    return i / (len(a) + len(b) - i)

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
    """[(level, heading, text)] - text under each heading, H1 preamble included."""
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

def load():
    docs = []
    for f in sorted(glob.glob(os.path.join(CONTENT, "**", "*.md"), recursive=True)):
        if os.path.basename(f).startswith("_"):
            continue
        text = open(f, encoding="utf-8").read()
        fm, body = frontmatter(text)
        if fm.get("status") not in (None, "published"):
            continue
        rel = os.path.relpath(f, REPO)
        docs.append({"path": rel, "slug": fm.get("slug", ""), "type": fm.get("type", ""),
                     "area": fm.get("product_area", ""), "title": fm.get("title", ""),
                     "related": fm.get("related_articles", ""),
                     "last": fm.get("last_converted", ""),
                     "body": body, "sections": sections(body),
                     "words": len(body.split())})
    return docs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-words", type=int, default=35, help="ignore sections shorter than this")
    ap.add_argument("--thresh", type=float, default=0.30)
    ap.add_argument("--out", default=os.path.join(REPO, "build", "reports", "kb-overlap.json"))
    a = ap.parse_args()

    docs = load()
    print(f"docs: {len(docs)}  words: {sum(d['words'] for d in docs):,}")

    # ---- pass 1: section pairs
    secs = []
    for d in docs:
        for lvl, head, text in d["sections"]:
            w = norm(text)
            if len(w) < a.min_words:
                continue
            secs.append({"doc": d["path"], "slug": d["slug"], "type": d["type"],
                         "area": d["area"], "head": head, "lvl": lvl,
                         "nw": len(w), "sh": shingles(w)})
    print(f"sections >= {a.min_words} words: {len(secs)}")

    # invert shingles so we only compare sections that share something
    inv = collections.defaultdict(list)
    for i, s in enumerate(secs):
        for sg in s["sh"]:
            inv[sg].append(i)
    cand = collections.Counter()
    for sg, idxs in inv.items():
        if len(idxs) > 40:          # boilerplate shingle, skip
            continue
        for i, j in itertools.combinations(sorted(idxs), 2):
            if secs[i]["doc"] != secs[j]["doc"]:
                cand[(i, j)] += 1
    pairs = []
    for (i, j), shared in cand.items():
        if shared < 4:
            continue
        s = jac(secs[i]["sh"], secs[j]["sh"])
        if s >= a.thresh:
            pairs.append({"sim": round(s, 3), "shared": shared,
                          "a": {"doc": secs[i]["doc"], "head": secs[i]["head"], "nw": secs[i]["nw"],
                                "type": secs[i]["type"], "area": secs[i]["area"]},
                          "b": {"doc": secs[j]["doc"], "head": secs[j]["head"], "nw": secs[j]["nw"],
                                "type": secs[j]["type"], "area": secs[j]["area"]}})
    pairs.sort(key=lambda p: -p["sim"])
    print(f"section pairs over {a.thresh}: {len(pairs)}")

    # ---- pass 2: paragraph clones
    para = collections.defaultdict(list)
    for d in docs:
        for block in re.split(r"\n\s*\n", d["body"]):
            b = block.strip()
            if b.startswith(("#", "|", "---", ">", "<!--")) or len(b.split()) < 12:
                continue
            key = " ".join(norm(b))
            if len(key.split()) < 10:
                continue
            para[key].append(d["path"])
    clones = [{"n": len(set(v)), "docs": sorted(set(v)), "text": k[:300]}
              for k, v in para.items() if len(set(v)) > 1]
    clones.sort(key=lambda c: (-c["n"], -len(c["text"])))
    print(f"paragraphs appearing in >1 doc: {len(clones)}")

    # ---- pass 3: heading clones
    heads = collections.defaultdict(list)
    for d in docs:
        for lvl, head, text in d["sections"]:
            if lvl in (2, 3) and head != "(top)":
                heads[re.sub(r"[^a-z0-9 ]", "", head.lower()).strip()].append((d["path"], head))
    hclones = [{"key": k, "n": len({p for p, _ in v}), "where": sorted({p for p, _ in v}),
                "forms": sorted({h for _, h in v})}
               for k, v in heads.items() if len({p for p, _ in v}) > 1]
    hclones.sort(key=lambda h: -h["n"])
    print(f"headings used in >1 doc: {len(hclones)}")

    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    json.dump({"pairs": pairs, "clones": clones, "headings": hclones,
               "docs": [{k: v for k, v in d.items() if k not in ("body", "sections")} for d in docs]},
              open(a.out, "w"), ensure_ascii=False, indent=1)
    print("->", a.out)

if __name__ == "__main__":
    main()
