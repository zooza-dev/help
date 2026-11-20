#!/usr/bin/env python3
"""BM25 over the exported KB chunks, to ask: could the answer have been found?

Not the bot's own retriever, but close enough to separate the two failures that
need completely different fixes:
    the KB does not contain the answer      -> write it
    the KB contains it and ranks it nowhere -> intent keywords / wording
"""
import json, os, re, math, collections, html

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CHUNKS = os.path.join(REPO, "build", "exports", "agent", "canonical.jsonl")
FAQ = os.path.join(REPO, "build", "exports", "agent", "faq.jsonl")

STOP = set("""a an the and or but if then than that this these those is are was were be been being am
to of in on at by for with from as it its you your we our they their them he she his her
do does did doing not no nor so such can could will would should shall may might must need
i me my there here what which who whom when where why how all any both each few more most
other some only own same too very just also into over under again further once up down out off
hi hello hey please thanks thank thankyou regards dear""".split())

def toks(t):
    t = re.sub(r"<[^>]+>", " ", t or "")
    t = html.unescape(t).lower()
    t = re.sub(r"[^a-z0-9áäčďéíľĺňóôŕšťúýžěřůõăâîșț€]+", " ", t)
    return [w for w in t.split() if w not in STOP and len(w) > 2]

class BM25:
    def __init__(self, docs, k1=1.4, b=0.72):
        self.docs = docs
        self.tf = [collections.Counter(toks(d["text"] + " " + d.get("title",""))) for d in docs]
        self.len = [sum(c.values()) or 1 for c in self.tf]
        self.avg = sum(self.len)/len(self.len)
        self.df = collections.Counter()
        for c in self.tf:
            for t in c:
                self.df[t] += 1
        self.N = len(docs)
        self.inv = collections.defaultdict(list)
        for i, c in enumerate(self.tf):
            for t, f in c.items():
                self.inv[t].append((i, f))
        self.k1, self.b = k1, b
    def search(self, q, n=5):
        qt = toks(q)
        sc = collections.defaultdict(float)
        for t in set(qt):
            if t not in self.inv:
                continue
            idf = math.log(1 + (self.N - self.df[t] + 0.5)/(self.df[t] + 0.5))
            for i, f in self.inv[t]:
                d = f*(self.k1+1)/(f + self.k1*(1 - self.b + self.b*self.len[i]/self.avg))
                sc[i] += idf*d
        top = sorted(sc.items(), key=lambda kv: -kv[1])[:n]
        return [(self.docs[i], round(s, 2)) for i, s in top]

def load():
    docs = []
    for path in (CHUNKS, FAQ):
        if not os.path.exists(path):
            continue
        for line in open(path, encoding="utf-8"):
            r = json.loads(line)
            docs.append({"title": r.get("title",""), "slug": r.get("doc_id",""),
                         "url": r.get("url",""), "head": r.get("heading_path","") or "",
                         "type": r.get("type",""),
                         "text": r.get("text") or "", "src": os.path.basename(path)})
    return docs

if __name__ == "__main__":
    import sys
    idx = BM25(load())
    print(f"indexed {idx.N} chunks")
    for q in sys.argv[1:]:
        print(f"\nQ: {q}")
        for d, s in idx.search(q):
            print(f"  {s:6.2f}  {d['slug']} :: {d['head'][:70]}")
