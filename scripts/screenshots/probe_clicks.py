#!/usr/bin/env python3
"""What is actually clickable on a screen, so manifests stop guessing.

    python3 scripts/screenshots/probe_clicks.py settings/payment_schedule_templates
    python3 scripts/screenshots/probe_clicks.py --routes /tmp/routes.txt --out /tmp/clicks.json

`image_index.py` proposes a click target by reading the heading of the panel a
screenshot seems to show. That is a guess about the *destination*, not about
the control, and on the first real run only one target in six could be found.
This opens each screen and reads the labels off the buttons that are there.

Reads only. It clicks nothing, so it cannot change the account.
"""

import argparse
import json
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SESSION = os.path.join(ROOT, "build", "intake", "zooza-session.json")
BASE = "https://uk.zooza.app/"
BLOCK = "**/*{intercom,hotjar,googletagmanager,google-analytics,facebook.net}*"

# The page chrome is on every screen; listing it as a candidate on all 150 of
# them buries the two or three controls that are actually particular to one.
CHROME = {"help & support", "back", "save", "cancel", "menu", "home", "log out",
          "more", "reset", "close", "english", "slovenský", "česky", "deutsch",
          "magyar", "italiano", "polski", "română"}


def probe(routes, limit):
    from playwright.sync_api import sync_playwright
    if not os.path.exists(SESSION):
        sys.exit(f"no session at {SESSION} — capture.py --login <magic-link> first")
    out = {}
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": 1600, "height": 1000},
                            color_scheme="light", storage_state=SESSION)
        ctx.route(BLOCK, lambda r: r.abort())
        pg = ctx.new_page()
        for route in routes:
            try:
                pg.goto(f"{BASE}#{route.lstrip('#')}", timeout=60000)
                pg.wait_for_timeout(9000)
                if "Page not found" in pg.inner_text("body"):
                    out[route] = {"error": "404"}
                    print(f"  {route:<46} 404")
                    continue
                labels = pg.eval_on_selector_all(
                    ".app_page_layout a:visible, .app_page_layout button:visible, "
                    ".app_page_layout summary:visible",
                    "els => els.map(e => (e.innerText || '').trim()).filter(Boolean)")
                seen, clean = set(), []
                for t in labels:
                    t = " ".join(t.split())
                    if not (1 < len(t) < 46) or t.lower() in CHROME or t in seen:
                        continue
                    seen.add(t)
                    clean.append(t)
                out[route] = {"clickable": clean[:limit]}
                print(f"  {route:<46} {len(clean)} controls")
            except Exception as exc:                      # one bad screen must not end the sweep
                out[route] = {"error": str(exc)[:120]}
                print(f"  {route:<46} {type(exc).__name__}")
        b.close()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("route", nargs="*", help="one or more hash routes")
    ap.add_argument("--routes", help="a file with one route per line")
    ap.add_argument("--out", help="write the result as JSON")
    ap.add_argument("--limit", type=int, default=40, help="controls to keep per screen")
    args = ap.parse_args()

    routes = list(args.route)
    if args.routes:
        with open(args.routes, encoding="utf-8") as fh:
            routes += [l.strip() for l in fh if l.strip() and not l.startswith("#")]
    if not routes:
        ap.error("give a route, or --routes with a file of them")

    result = probe(routes, args.limit)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(result, fh, indent=1, ensure_ascii=False)
        print(f"\nwritten to {args.out}")
    else:
        for route, got in result.items():
            print(f"\n{route}")
            for t in got.get("clickable", []):
                print(f"   {t}")
            if got.get("error"):
                print(f"   ! {got['error']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
