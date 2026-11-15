#!/usr/bin/env python3
"""What does this screen actually call its fields?

    python3 scripts/screenshots/probe_labels.py courses/schedules/40
    python3 scripts/screenshots/probe_labels.py registrations/1394 --find balance
    python3 scripts/screenshots/probe_labels.py --route-file build/intake/routes.txt

`check_ui_labels.py` can tell us that a name we published is absent from the
app's string table. It cannot tell us what replaced it, and for whole classes of
label it cannot even raise the question: a form row's label may be assembled at
runtime, and on 2026-11-15 `Timetable type` turned out to be live on screen
while matching nothing in `lib/str_en3.js` on origin/main.

So read the screen. This prints the page's visible text, which is enough to
settle a field name by eye, and `--find` narrows it to the lines around a word
when the screen is long.

Reads only. It navigates and prints; it submits nothing and changes no data.
"""

import argparse
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SESSION = os.path.join(ROOT, "build", "intake", "zooza-session.json")
BASE = "https://uk.zooza.app/"
BLOCK = "**/*{intercom,hotjar,googletagmanager,google-analytics,facebook.net}*"

# The left-hand navigation is on every screen including the 404, so its items
# are noise in every reading. Drop the chrome, keep the page.
CHROME = {"Activities", "Programmes", "Classes", "Sessions", "Calendar",
          "Feedback", "Clients", "Sales & Payments", "Products & Services",
          "Communication", "Reports & Insights", "Team & Settings", "Back"}


def xq(s):
    """XPath has no escape character, so a quoted literal must be concat()ed."""
    if '"' not in s:
        return f'"{s}"'
    return "concat(" + ", '\"', ".join(f'"{p}"' for p in s.split('"')) + ")"


def read(pg, route, wait, clicks=()):
    pg.goto(f"{BASE}#{route.lstrip('#')}", timeout=60000)
    pg.wait_for_timeout(wait)
    # Several screens keep their field names behind an Edit button, and the
    # summary card shows only the values. `card>Edit` clicks the Edit inside the
    # card whose heading is `card`, because a page has many Edit buttons.
    for spec in clicks:
        card, _, label = spec.rpartition(">")
        scope = pg.locator(f"xpath=//*[contains(., {xq(card)})]").last if card else pg
        try:
            (scope.get_by_text(label, exact=True).last if card
             else pg.get_by_role("button", name=label, exact=True).first).click(timeout=8000)
            pg.wait_for_timeout(4000)
        except Exception as exc:
            print(f"    could not click {spec!r}: {type(exc).__name__}")
    body = pg.inner_text("body")
    if "Page not found" in body:
        return None, "404 - the route is wrong"
    lines = []
    for raw in body.split("\n"):
        s = raw.strip()
        if s and s not in CHROME and s not in lines[-1:]:
            lines.append(s)
    return lines, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("route", nargs="*", help="hash route(s), without the leading #")
    ap.add_argument("--route-file", help="read routes from a file, one per line")
    ap.add_argument("--find", help="print only lines matching this (case-insensitive), with context")
    ap.add_argument("--context", type=int, default=4, help="lines either side of a --find hit")
    ap.add_argument("--wait", type=int, default=9000, help="ms to let the screen settle")
    ap.add_argument("--click", action="append", default=[], metavar="[CARD>]LABEL",
                    help="click this before reading; 'Price and payment>Edit' "
                         "picks the Edit inside that card")
    args = ap.parse_args()

    routes = list(args.route)
    if args.route_file:
        with open(args.route_file, encoding="utf-8") as fh:
            routes += [l.strip() for l in fh if l.strip() and not l.startswith("#")]
    if not routes:
        ap.error("give a route, or --route-file")
    if not os.path.exists(SESSION):
        sys.exit(f"no session at {SESSION} - capture.py --login <magic-link> first")

    pat = re.compile(re.escape(args.find), re.I) if args.find else None

    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": 1600, "height": 1200},
                            color_scheme="light", storage_state=SESSION)
        ctx.route(BLOCK, lambda r: r.abort())
        pg = ctx.new_page()
        for route in routes:
            print(f"\n=== {route}")
            try:
                lines, err = read(pg, route, args.wait, args.click)
            except Exception as exc:      # one bad screen must not end the sweep
                print(f"    {type(exc).__name__}: {str(exc)[:160]}")
                continue
            if err:
                print(f"    {err}")
                continue
            if not pat:
                for l in lines:
                    print("   ", l)
                continue
            hits = [i for i, l in enumerate(lines) if pat.search(l)]
            if not hits:
                print(f"    nothing matching {args.find!r} on this screen")
                continue
            shown = set()
            for i in hits:
                for j in range(max(0, i - args.context), min(len(lines), i + args.context + 1)):
                    if j not in shown:
                        shown.add(j)
                        print(f"   {'>' if j == i else ' '} {lines[j]}")
                print("    --")
        b.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
