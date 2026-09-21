#!/usr/bin/env python3
"""Check the KB's "Settings → …" navigation cues against the app's real menu.

    python3 scripts/check_nav.py            # report drift
    python3 scripts/check_nav.py --strict   # exit 1 on drift (for the pipeline)

The real menu comes from build/app-map/app-map.yml, generated from the app's
source by scripts/screenshots/app_map.py build. A cue is checked only when it
is the company-level Settings — anything preceded by "Programme", "programme",
"class" or "the programme" within a few words is the programme's own Settings
tab, which has a different menu and is left alone.

Why this exists: on 2026-09-19 the KB pointed readers at Settings → Team,
Settings → Locations and Settings → Payments — 40-odd cues for screens the
menu calls Access, Venues and Payment settings. Nobody had noticed because
each article was right when it was written; the menu moved under it.
"""

import argparse
import glob
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
APP_MAP = os.path.join(ROOT, "build", "app-map", "app-map.yml")

CUE = re.compile(r"Settings → ([A-Za-z&' -]+?)(?: → ([A-Za-z&' -]+?))?(?=\*\*|[.,;:)|`\]\n]| →|$)")
PROGRAMME_CONTEXT = re.compile(r"(programme|program|class|course|the item|widget)[\s\S]{0,60}$", re.I)
# "Programme → Settings → X" / "Programme Settings → X": X must be a tile. Only this tight form is checked;
# the loose context above merely stops a programme-level cue being judged against the company menu.
TILE_CONTEXT = re.compile(r"(programme|program|course)\**\s*(→|>)?\s*\**\s*$", re.I)
CLASS_CONTEXT = re.compile(r"\bclass\**\s*(→|>)\s*\**\s*$", re.I)
# Somebody else's Settings menu: the browser, Claude Desktop, Vimeo, an accounting package.
THIRD_PARTY = re.compile(r"(Chrome|Firefox|Safari|Edge|browser|Claude|Vimeo|ABRA|Xero|SuperFaktura|Stripe|GoCardless|Google)", re.I)
# Screens a cue may legitimately name that are not Settings subpages — sidebar
# siblings under "Team & Settings" and the top-level groups themselves.
# Cards on a subpage that articles name as if they were a level of their own — fine.
ALLOWED_CARDS = {"account information", "settings for programmes", "company logo"}
ALLOWED_LEAVES = {"General", "Billing & Payments", "Other", "Tools", "Integrations", "Publish",
                  "Instructors", "Widgets", "Zooza AI", "My profile"}


def load_menu():
    import yaml
    doc = yaml.safe_load(open(APP_MAP, encoding="utf-8"))
    menu, tiles = {}, {}
    for s in doc["screens"]:
        if s.get("area", "settings") == "settings":
            _, group, leaf = s["menu"].split(" → ")
            menu[leaf.lower()] = (group, leaf)
        elif s["id"].startswith("programmes.settings."):
            tiles[s["title"].lower()] = s["title"]
    return menu, tiles


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()
    if not os.path.exists(APP_MAP):
        sys.exit("no app map — run scripts/screenshots/app_map.py build first")
    menu, tiles = load_menu()
    problems = []
    for f in sorted(glob.glob(os.path.join(ROOT, "content", "**", "*.md"), recursive=True)):
        if "/glossary/" in f:
            continue
        lines = open(f, encoding="utf-8").read().split("\n")
        for ln, line in enumerate(lines, 1):
            for m in CUE.finditer(line):
                # a numbered step often says "Open the programme" on the line before
                before = "\n".join(lines[max(0, ln - 3): ln - 1]) + "\n" + line[: m.start()]
                first, second = m.group(1).strip(), (m.group(2) or "").strip()
                rel = os.path.relpath(f, ROOT)
                if THIRD_PARTY.search(before + line):
                    continue
                if TILE_CONTEXT.search(before[-40:]) and not CLASS_CONTEXT.search(before[-40:]):
                    # the programme's own Settings tab: the leaf must be a tile, spelled as the app spells it
                    if tiles and first.lower() in tiles and first != tiles[first.lower()]:
                        problems.append((rel, ln, f"Programme → Settings → {first}", f"tile is spelled {tiles[first.lower()]!r}"))
                    elif tiles and first.lower() not in tiles and len(first) < 30 and not re.search(r"\b(for|this|that|it|tab|tile|them)$", first) and " to " not in first:
                        problems.append((rel, ln, f"Programme → Settings → {first}", "no such tile on the programme Settings tab"))
                    continue
                if PROGRAMME_CONTEXT.search(before):
                    continue
                if re.search(r"\b(for|this|that|it)$", first) or " with " in first:   # prose, not a menu path
                    continue
                rel = os.path.relpath(f, ROOT)
                if first in ALLOWED_LEAVES:
                    # "Settings → General → Access" or "Settings → Tools"; only a wrong leaf under a group is drift
                    if first in ("General", "Billing & Payments", "Other", "Tools") and second and second.lower() not in menu and second.lower() not in ALLOWED_CARDS \
                            and len(second) < 30:   # long "leaves" are field names on the group's own page, not subpages
                        problems.append((rel, ln, f"Settings → {first} → {second}", "no such subpage"))
                    continue
                hit = menu.get(first.lower())
                if hit:
                    problems.append((rel, ln, f"Settings → {first}", f"missing group: Settings → {hit[0]} → {hit[1]}"))
                else:
                    problems.append((rel, ln, f"Settings → {first}", "not in the Settings menu"))

    for rel, ln, cue, why in problems:
        print(f"{rel}:{ln}: {cue} — {why}")
    print(f"\n{len(problems)} navigation cues to look at")
    return 1 if (args.strict and problems) else 0


if __name__ == "__main__":
    sys.exit(main())
