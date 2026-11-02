#!/usr/bin/env python3
"""Which KB screenshots are most likely to be lying, ranked.

    python3 scripts/screenshots/image_audit.py                 # report to build/reports/image-audit.md
    python3 scripts/screenshots/image_audit.py --top 40        # print the worst 40 to stdout
    python3 scripts/screenshots/image_audit.py --area Payments # one product area

`image_index.py` answers "which screen is this image of?". This answers the
question that comes first: "which images should we reshoot at all?" — because
nobody is going to reshoot a thousand.

Three signals, each cheap and each independently meaningful:

1. **Age.** When the image was first committed (git), not the file mtime, which
   every checkout rewrites.
2. **Drift.** The article's `last_converted` minus the image's date. An article
   rewritten in October carrying a February picture is the strongest signal we
   have: someone checked the words recently and did not look at the picture.
3. **Churn.** Whether the screen it belongs to has shipped changes lately —
   taken from the implemented specs in the sibling repos, so it reflects what
   the developers actually touched rather than a list kept by hand.

Nothing here opens a browser. The output is a shoot list for a human.
"""

import argparse
import collections
import datetime as dt
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CONTENT = os.path.join(ROOT, "content")
OUT = os.path.join(ROOT, "build", "reports", "image-audit.md")
SIBLINGS = [("api-v1", os.path.join(ROOT, "..", "api-v1")),
            ("app", os.path.join(ROOT, "..", "app")),
            ("widgets-v1", os.path.join(ROOT, "..", "widgets-v1"))]

IMG = re.compile(r"!\[([^\]]*)\]\(\.\./\.\./assets/images/([^)\s\"]+)")
FRONT = re.compile(r"^---\n(.*?)\n---", re.S)

# A screen that shipped changes recently is worth reshooting even if its picture
# is not especially old. Each area is matched against spec titles and filenames.
AREA_WORDS = {
    "Bookings": ["registration", "booking", "linking", "linked", "cancellation"],
    "Payments": ["payment", "invoice", "refund", "debt", "instal", "billing", "loyalty", "discount"],
    "Programmes": ["course", "programme", "trial", "retention", "enrol", "block"],
    "Classes": ["schedule", "class", "session", "capacity", "shared"],
    "Calendar": ["event", "session", "attendance", "calendar", "make-up", "replacement"],
    "Clients": ["client", "person", "contact", "lead"],
    "Settings": ["settings", "company", "network", "access", "team", "info tab"],
    "Communication": ["email", "template", "notification", "whatsapp", "sms", "message"],
    "Widgets": ["widget", "booking form", "profile", "publish"],
    "Orders": ["order", "product", "entry pass", "service"],
}


def run(args, cwd=ROOT):
    try:
        out = subprocess.run(args, cwd=cwd, capture_output=True, check=True)
        return out.stdout.decode("utf-8", "replace")
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        return ""


def image_first_seen():
    """basename -> date (YYYY-MM-DD) the file was first committed."""
    log = run(["git", "log", "--diff-filter=A", "--reverse",
               "--format=@%ad", "--date=short", "--name-only", "--", "assets/images/"])
    seen, date = {}, None
    for line in log.splitlines():
        if line.startswith("@"):
            date = line[1:].strip()
        elif line.strip().startswith("assets/images/") and date:
            seen.setdefault(os.path.basename(line.strip()), date)
    return seen


def recent_spec_words(days):
    """Words from specs implemented in the sibling repos in the last `days` days."""
    since = (dt.date.today() - dt.timedelta(days=days)).isoformat()
    words = collections.Counter()
    for name, path in SIBLINGS:
        if not os.path.isdir(path):
            continue
        run(["git", "fetch", "origin", "main", "-q"], cwd=path)
        log = run(["git", "log", f"--since={since}", "--format=", "--name-only",
                   "origin/main", "--", "specs/implemented/"], cwd=path)
        for line in log.splitlines():
            base = os.path.basename(line.strip()).lower()
            if base.endswith(".md"):
                for w in re.split(r"[^a-z]+", base):
                    if len(w) > 3:
                        words[w] += 1
    return words


def churning_areas(words, keep=4):
    """The areas the developers have been busiest in, as a ranked shortlist.

    An absolute threshold is useless here: in a normal quarter every area has
    some spec activity, so everything scores and the signal disappears. What
    is worth knowing is which areas moved MORE than the others, so we keep the
    top few and return their scores for the report to show its working.
    """
    scored = []
    for area, keys in AREA_WORDS.items():
        score = sum(words[k] for key in keys for k in key.split() if k in words)
        if score:
            scored.append((score, area))
    scored.sort(reverse=True)
    return {area: score for score, area in scored[:keep]}


def articles():
    """Every published article -> (path, product_area, last_converted, [images])."""
    out = []
    for dirpath, _, names in os.walk(CONTENT):
        for n in sorted(names):
            if not n.endswith(".md"):
                continue
            p = os.path.join(dirpath, n)
            with open(p, encoding="utf-8") as fh:
                text = fh.read()
            m = FRONT.match(text)
            if not m:
                continue
            front = m.group(1)

            def field(key):
                f = re.search(rf"^{key}:\s*\"?([^\"\n]*)\"?", front, re.M)
                return f.group(1).strip() if f else ""

            imgs = [(alt, os.path.basename(src)) for alt, src in IMG.findall(text)]
            if imgs:
                out.append((os.path.relpath(p, ROOT), field("product_area"),
                            field("last_converted"), field("needs_screenshot_replacement"),
                            field("status"), imgs))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--area", help="limit to one product_area")
    ap.add_argument("--top", type=int, default=0, help="print the worst N to stdout")
    ap.add_argument("--churn-days", type=int, default=120,
                    help="how far back to look for shipped specs (default 120)")
    args = ap.parse_args()

    first = image_first_seen()
    hot = churning_areas(recent_spec_words(args.churn_days))
    today = dt.date.today()

    all_articles = articles()

    # "Unused" has to mean unused by ANY article, not just the published ones.
    # Draft and archived articles are still in the repo and still want their
    # pictures; on the first run 33 of 132 "unused" files were referenced by
    # unpublished articles, and deleting them would have been a quiet loss.
    referenced = {img for _, _, _, _, _, imgs in all_articles for _, img in imgs}
    unused_candidates = set(first) - referenced

    rows, flagged, undated = [], 0, 0
    for path, area, converted, needs, status, imgs in all_articles:
        if status != "published":
            continue
        if args.area and area != args.area:
            continue
        for alt, img in imgs:
            added = first.get(img)
            if not added:
                undated += 1
                continue
            age = (today - dt.date.fromisoformat(added)).days
            drift = 0
            if converted:
                try:
                    drift = (dt.date.fromisoformat(converted) - dt.date.fromisoformat(added)).days
                except ValueError:
                    drift = 0
            # Score: age matters, an article rewritten past its picture matters more,
            # a churning area matters most because we KNOW the screen moved.
            score = age / 30.0 + max(drift, 0) / 15.0 + (12 if area in hot else 0)
            if needs == "true":
                score += 8
                flagged += 1
            rows.append((score, age, drift, added, converted, area, path, img, alt))

    rows.sort(reverse=True)
    unused = sorted(i for i in unused_candidates
                    if os.path.exists(os.path.join(ROOT, "assets", "images", i)))

    # An article is the unit of work: you open a screen once and shoot everything
    # on it. Rank articles by their worst image, and show how many they carry.
    per_article = collections.defaultdict(list)
    for r in rows:
        per_article[r[6]].append(r)
    ranked = sorted(per_article.items(), key=lambda kv: -max(r[0] for r in kv[1]))

    lines = [f"# Screenshot audit — {today.isoformat()}", "",
             f"{len(rows)} images on {len(per_article)} published articles, ranked by how likely",
             "they are to be out of date. A high score is where to look first, not proof.", "",
             "**The three signals.** How old the picture is; how long the article went on being",
             "rewritten *after* the picture was taken (somebody checked the words and not the",
             "screen); and whether the developers have been changing that part of the product.", ""]

    if hot:
        busiest = ", ".join(f"**{a}** ({n})" for a, n in hot.items())
        lines += [f"Busiest areas in the last {args.churn_days} days of shipped specs: {busiest}.",
                  "The number is how often that area's vocabulary appears in spec filenames — a",
                  "rough proxy for 'this screen moved recently', not a count of changes.", ""]
    if flagged:
        lines += [f"{flagged} image(s) are on articles already marked "
                  "`needs_screenshot_replacement: true`, and are pushed up.", ""]

    lines += ["## Shoot list, by article", "",
              "Work down it. Each row is one screen-shooting session.", "",
              "| # | Article | Area | Images | Oldest | Rewritten after | Score |",
              "|---:|---|---|---:|---:|---:|---:|"]
    for i, (path, rs) in enumerate(ranked[:60], 1):
        worst = max(r[0] for r in rs)
        oldest = max(r[1] for r in rs)
        drift = max(r[2] for r in rs)
        lines.append(f"| {i} | `{os.path.basename(path)}` | {rs[0][5]} | {len(rs)} | "
                     f"{oldest // 30} mo | {(str(drift // 30) + ' mo') if drift > 45 else '—'} | "
                     f"{worst:.0f} |")

    lines += ["", "<details><summary>Every image, worst first</summary>", "",
              "| Score | Age | Area | Article | Image |", "|---:|---:|---|---|---|"]
    for score, age, drift, added, conv, area, path, img, _ in rows[:300]:
        lines.append(f"| {score:.0f} | {age // 30} mo | {area} | "
                     f"`{os.path.basename(path)}` | `{img}` |")
    lines += ["", "</details>"]

    if undated:
        lines += ["", f"> {undated} image reference(s) have no git history — added in the working "
                      "tree and not committed, or a broken path. `validate_kb.py` catches the "
                      "genuinely missing ones."]

    if unused:
        lines += ["", "## Images nothing links to", "",
                  f"{len(unused)} file(s) in `assets/images/` are referenced by no article at "
                  "all — published, draft or archived. Usually the previous version of a picture "
                  "that was replaced.", ""]
        lines += [f"- `{i}`" for i in unused[:150]]
        if len(unused) > 150:
            lines.append(f"- …and {len(unused) - 150} more")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")

    print(f"{len(rows)} images across {len(per_article)} articles")
    print(f"  busiest areas: {', '.join(hot) or 'none detected'}")
    print(f"  marked needs_screenshot_replacement: {flagged}")
    print(f"  referenced by nothing: {len(unused)}")
    print(f"  report: {os.path.relpath(OUT, ROOT)}")
    if args.top:
        print()
        for i, (path, rs) in enumerate(ranked[:args.top], 1):
            print(f"  {i:>3}. {max(r[0] for r in rs):5.0f}  {len(rs):>3} img  "
                  f"{max(r[1] for r in rs)//30:>3} mo  {rs[0][5]:<14} {os.path.basename(path)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
