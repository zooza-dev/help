#!/usr/bin/env python3
"""Work out which app screen each KB image is supposed to show.

    python3 scripts/screenshots/image_index.py            # report to build/app-map/image-index.md
    python3 scripts/screenshots/image_index.py --area settings

For every image referenced from content/, read the context around it — the
section heading, the alt text, and the nearest "Go to Settings → …" cue above
it — and match that against the screens in build/app-map/app-map.yml. The
result is a manifest proposal: which images can be recaptured from a known
route, which are dialogs (need a click), and which the tool cannot place.

Why: 1 001 images are referenced from the KB, 54 articles still carry the
Slovak screenshots from the February conversion, and the hand-written manifest
has 8 entries. Nobody is going to place 1 000 images by hand; this places the
easy majority and leaves a short list.
"""

import argparse
import glob
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "build", "app-map")
IMG = re.compile(r"!\[([^\]]*)\]\((\.\./\.\./assets/images/([^)\s\"]+))[^)]*\)")
CUE = re.compile(r"Settings → ([A-Za-z&' -]+?)(?: → ([A-Za-z&' -]+?))?(?:\*\*|[.,;:)|`\]]|$| →)")
HEADING = re.compile(r"^(#{1,4})\s+(.*)")
FRONT = re.compile(r"^---\n(.*?)\n---", re.S)
DIALOG_WORDS = re.compile(r"\b(dialog|modal|form|add|create|edit|new)\b", re.I)


def load_screens():
    import yaml
    doc = yaml.safe_load(open(os.path.join(OUT, "app-map.yml"), encoding="utf-8"))
    by_leaf = {}
    for s in doc["screens"]:
        leaf = s["menu"].split(" → ")[-1].lower()
        if s.get("area", "settings") == "settings":
            by_leaf[leaf] = s
        else:
            by_leaf["programme:" + leaf] = s     # programme tiles are looked up with the prefix
    # the names the KB used before the menu was renamed — still useful for placing old images
    aliases = {"programme:price and payment": "programme:price and payment", "programme:online registration": "programme:online booking",
               "programme:auto-enrollment": "programme:auto-enrolment", "programme:retention": "programme:auto-enrolment",
               "team": "access", "users": "access", "locations": "venues", "places": "venues",
               "payments": "payment settings", "payment templates": "payment schedule templates",
               "billing profiles": "invoice profiles", "invoice settings": "invoices",
               "notifications": "notification center", "holidays": "custom holidays"}
    for a, leaf in aliases.items():
        if leaf in by_leaf:
            by_leaf.setdefault(a, by_leaf[leaf])
    return by_leaf


def load_cards():
    """screen id -> [(card title, opened-by label or None)] from the deep crawl."""
    import json
    out = {}
    for f in glob.glob(os.path.join(OUT, "screens", "*.json")):
        d = json.load(open(f, encoding="utf-8"))
        cards = []
        for c in d["cards"]:
            t = c["title"]
            via = None
            if " › " in t:
                via, t = t.split(" › ", 1)
            cards.append((t, via, c.get("route")))
        out[d["id"]] = cards
    return out


STOP = {"the", "a", "an", "of", "for", "and", "in", "on", "to", "with", "settings", "setting", "screenshot", "page", "tab",
        "section", "card", "showing", "shows", "view", "list", "zooza", "your", "you", "is", "are", "at", "by"}


def tokens(text):
    return {w for w in re.findall(r"[a-z]+", text.lower()) if w not in STOP and len(w) > 2}


def guess_card(cards, heading, alt):
    """Best card by word overlap between the image's context and the card title. None when nothing overlaps."""
    want = tokens(f"{heading} {alt}")
    best, score = None, 0
    for title, via, route in cards:
        have = tokens(title) | (tokens(via) if via else set())
        n = len(want & have)
        if n > score:
            best, score = (title, via, route), n
    return best if score >= 1 else None


def by_leaf_title(by_leaf, screen_id):
    for s in by_leaf.values():
        if s["id"] == screen_id:
            return s["title"]
    return ""


PROGRAMME_WORDS = re.compile(r"\b(programme|program|course)\b", re.I)
AREA_HINTS = [   # (regex on heading+alt+filename+article, screen id) — coarse placement when no cue matches
    (re.compile(r"\bnew document\b|\bdocument settings\b|\bupload(ing)? (a )?(document|file)\b", re.I), "files.add_new"),
    (re.compile(r"\bdynamic document\b", re.I), "files.dynamic_document"),
    (re.compile(r"\bdocuments?\b.*\b(library|list|documents\.md)\b|\bdocuments-\d", re.I), "files.list"),
    (re.compile(r"\b(session detail|session's detail|open the session)\b", re.I), "sessions.detail"),
    (re.compile(r"\bsessions? list\b|\bsessions-list\b", re.I), "sessions.list"),
    (re.compile(r"\bclass detail\b|\bclass settings\b|\bschedules-detail\b", re.I), "classes.detail"),
    (re.compile(r"\bclasses list\b|\bclasses-list\b", re.I), "classes.list"),
    (re.compile(r"\bautomations?\b", re.I), "programmes.automations"),
    (re.compile(r"\b(new|create|creating) (a )?programme\b|\bprogramme-creat", re.I), "programmes.create"),
    (re.compile(r"\bprogramme settings\b|\bprogramme-settings\b", re.I), "programmes.settings"),
    (re.compile(r"\bprogrammes? list\b|\bprogrammes-list\b", re.I), "programmes.list"),
]


def guess_screen(by_leaf, cue, heading, alt, filename, programme_ctx=False):
    """Return (screen, how) — how says which signal placed it, so the report is checkable."""
    if cue:
        first, second = cue
        for cand in (second, first):
            if not cand:
                continue
            key = ("programme:" if programme_ctx else "") + cand.lower()
            if key in by_leaf:
                return by_leaf[key], f"cue: {'Programme → ' if programme_ctx else ''}Settings → {first}" + (f" → {second}" if second else "")
    hay = f"{heading} {alt} {filename.replace('-', ' ').replace('_', ' ')}"
    for rx, sid in AREA_HINTS:
        if rx.search(hay):
            for scr in by_leaf.values():
                if scr["id"] == sid:
                    return scr, f"hint: {sid}"
    hay = hay.lower()
    programme_ish = bool(PROGRAMME_WORDS.search(hay)) or programme_ctx
    hits = [(len(leaf), leaf) for leaf in by_leaf if not leaf.startswith("programme:") and leaf in hay and len(leaf) > 4]
    tile_hits = [(len(leaf), leaf) for leaf in by_leaf if leaf.startswith("programme:") and leaf[10:] in hay and len(leaf) > 14]
    # a tile name in the text beats a Settings page name only when the text is about a programme
    if tile_hits and (programme_ish or not hits):
        leaf = max(tile_hits)[1]
        return by_leaf[leaf], f"text: '{leaf}'"
    if hits:
        leaf = max(hits)[1]
        return by_leaf[leaf], f"text: '{leaf}'"
    return None, ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--area", default="settings", help="only images whose article or context mentions this area")
    ap.add_argument("--manifest", action="store_true", help="also write a capture.py manifest for the placed images")
    ap.add_argument("--flagged-only", action="store_true", help="manifest: only images in articles flagged needs_screenshot_replacement")
    ap.add_argument("--screens", help="manifest: only screens whose id starts with one of these comma-separated prefixes")
    args = ap.parse_args()
    by_leaf = load_screens()
    cards = load_cards()

    rows = []
    for f in sorted(glob.glob(os.path.join(ROOT, "content", "**", "*.md"), recursive=True)):
        if "/glossary/" in f:
            continue
        text = open(f, encoding="utf-8").read()
        fm = FRONT.match(text)
        flagged = bool(fm and re.search(r"needs_screenshot_replacement:\s*true", fm.group(1)))
        lines = text.split("\n")
        heading, last_cue = "", None
        for i, line in enumerate(lines):
            h = HEADING.match(line)
            if h:
                heading = h.group(2)
            c = CUE.search(line)
            if c:
                last_cue = (c.group(1).strip(), (c.group(2) or "").strip())
                cue_line = i
                before = "\n".join(lines[max(0, i - 2): i]) + line[: c.start()]
                cue_programme = bool(PROGRAMME_WORDS.search(before[-160:]))
            for m in IMG.finditer(line):
                alt, rel, name = m.group(1), m.group(2), m.group(3)
                cue = last_cue if last_cue and i - cue_line <= 25 else None
                ctx = f"{heading} {alt} {name} {os.path.basename(f)}".lower()
                area_words = {"settings": ["settings"], "programmes": []}.get(args.area, [args.area])
                if area_words and not any(w in ctx for w in area_words) and not cue:
                    continue
                screen, how = guess_screen(by_leaf, cue, heading, alt, name, cue is not None and cue_programme)
                card = guess_card(cards.get(screen["id"], []), heading, alt) if screen else None
                dialog = bool(card and card[1]) or (bool(DIALOG_WORDS.search(f"{alt} {heading}")) and screen is not None)
                rows.append({
                    "image": name, "article": os.path.relpath(f, ROOT), "line": i + 1,
                    "heading": heading, "alt": alt, "flagged": flagged,
                    "screen": screen["id"] if screen else "", "route": screen["route"] if screen else "",
                    "how": how, "kind": "dialog" if dialog else ("screen" if screen else "unplaced"),
                    "card": card[0] if card else "", "via": (card[1] or "") if card else "",
                    "sub_route": (card[2] or "") if card else "",
                    "exists": os.path.exists(os.path.join(ROOT, "assets", "images", name)),
                })

    placed = [r for r in rows if r["screen"]]
    path = os.path.join(OUT, f"image-index-{args.area}.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(f"# Image → screen index ({args.area})\n\n")
        fh.write(f"{len(rows)} images in scope, {len(placed)} placed on a mapped screen, "
                 f"{sum(1 for r in rows if r['kind']=='dialog')} of those look like dialogs, "
                 f"{sum(1 for r in rows if r['flagged'])} sit in articles flagged for Slovak screenshots, "
                 f"{sum(1 for r in rows if not r['exists'])} missing on disk.\n\n")
        fh.write("| image | article | screen | card (via) | kind | placed by | alt |\n|---|---|---|---|---|---|---|\n")
        for r in sorted(rows, key=lambda r: (r["screen"] or "~", r["article"])):
            card = (r["card"] + (f" (via {r['via']})" if r["via"] else "")) if r["card"] else "—"
            fh.write(f"| `{r['image']}` | {r['article']}:{r['line']} | {r['screen'] or '—'} | {card} | {r['kind']} | {r['how']} | {r['alt'][:60]} |\n")
    print(f"{len(rows)} images, {len(placed)} placed, {sum(1 for r in placed if r['card'])} with a card guess -> {path}")
    if args.manifest:
        import yaml
        shots, seen = [], set()
        prefixes = tuple(args.screens.split(",")) if args.screens else None
        for r in sorted(placed, key=lambda r: (r["screen"], r["image"])):
            if r["image"] in seen:
                continue
            if args.flagged_only and not r["flagged"]:
                continue
            if prefixes and not r["screen"].startswith(prefixes):
                continue
            seen.add(r["image"])
            shot = {"image": r["image"], "route": r["sub_route"] or r["route"],
                    "assert": r["card"] or by_leaf_title(by_leaf, r["screen"]), "status": "proposed"}
            if r["via"] and not r["sub_route"]:
                shot["click"] = r["via"]
            if r["card"]:
                shot["card"] = r["card"]
                old = os.path.join(ROOT, "assets", "images", r["image"])
                if os.path.exists(old):
                    from PIL import Image
                    w, h = Image.open(old).size
                    if w / h <= 1.35:   # the current picture is a close-up, not a page
                        shot["card_only"] = True
            shot["note"] = f"{r['article']}:{r['line']} — {r['alt'][:100]}"
            shots.append(shot)
        mpath = os.path.join(OUT, f"manifest-{args.area}.yml")
        with open(mpath, "w", encoding="utf-8") as fh:
            fh.write("# Generated by image_index.py --manifest. Review, then:\n")
            fh.write(f"#   python3 scripts/screenshots/capture.py --manifest {os.path.relpath(mpath, ROOT)}\n")
            yaml.safe_dump({"base": "https://uk.zooza.app/", "shots": shots}, fh, allow_unicode=True, sort_keys=False, width=120)
        print(f"{len(shots)} shots -> {mpath}")
    by_screen = {}
    for r in placed:
        by_screen.setdefault(r["screen"], []).append(r)
    for sid, rs in sorted(by_screen.items(), key=lambda kv: -len(kv[1])):
        print(f"  {sid:38} {len(rs):3} images  ({sum(1 for r in rs if r['kind']=='dialog')} dialog-ish, "
              f"{sum(1 for r in rs if r['flagged'])} flagged)")
    print(f"  {'(unplaced)':38} {len(rows)-len(placed):3}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
