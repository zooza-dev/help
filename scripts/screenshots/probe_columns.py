#!/usr/bin/env python3
"""What columns does a list screen actually offer?

    python3 scripts/screenshots/probe_columns.py clients bookings orders
    python3 scripts/screenshots/probe_columns.py --all --out build/app-map/columns.json

Our `content/reference/*-list.md` articles are column tables: one row per
column, naming it and saying what it holds. `check_ui_labels.py` can tell us a
column name is absent from the app's strings, but not what replaced it, because
these names are not in the string table at all - a list's columns are assembled
from field definitions at runtime.

So read them off the screen. Two places carry them:

  - the table header, which shows the columns currently switched on;
  - the column chooser, which shows every column available, on or off.

The chooser is the one that matters. A reference article documents all the
columns a client could switch on, not the handful our demo account happens to
display, and on 2026-11-09 twelve names in those articles matched nothing in
the product.

Reads only. It opens the chooser, which is a view control, and changes no data.
"""

import argparse
import json
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SESSION = os.path.join(ROOT, "build", "intake", "zooza-session.json")
BASE = "https://uk.zooza.app/"
BLOCK = "**/*{intercom,hotjar,googletagmanager,google-analytics,facebook.net}*"

# The list screens whose columns we document.
LISTS = ["clients", "bookings", "orders", "payments", "contacts", "courses",
         "schedules", "events", "documents", "instructors", "reports"]

# Controls that open a column chooser. The product has used more than one, and a
# list that silently has none must report that rather than look like a list with
# no columns.
OPENERS = ["Columns", "Choose columns", "Table settings", "View settings",
           "Displayed columns", "Settings"]


def read_screen(pg, route):
    pg.goto(f"{BASE}#{route.lstrip('#')}", timeout=60000)
    pg.wait_for_timeout(9000)
    body = pg.inner_text("body")
    if "Page not found" in body:
        return {"error": "404"}

    out = {}
    # Switched-on columns, straight off the header row.
    out["header"] = pg.eval_on_selector_all(
        "table thead th, .table thead th, [role=columnheader]",
        "els => els.map(e => (e.innerText || '').trim()).filter(Boolean)")

    # Everything on offer, from the chooser.
    for label in OPENERS:
        try:
            btn = pg.get_by_role("button", name=label, exact=True).first
            if not btn.is_visible(timeout=1500):
                continue
            btn.click(timeout=4000)
            pg.wait_for_timeout(2500)
            opts = pg.eval_on_selector_all(
                ".modal label, .drawer label, [role=dialog] label, "
                ".popover label, .dropdown-menu label",
                "els => els.map(e => (e.innerText || '').trim()).filter(Boolean)")
            if opts:
                out["chooser"] = {"opened_with": label, "columns": opts}
                pg.keyboard.press("Escape")
                break
            pg.keyboard.press("Escape")
        except Exception:
            continue
    if "chooser" not in out:
        out["chooser"] = None            # say so; do not imply there are none
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("route", nargs="*", help="list routes to read")
    ap.add_argument("--all", action="store_true", help="every list in LISTS")
    ap.add_argument("--out", help="write the result as JSON")
    args = ap.parse_args()

    routes = LISTS if args.all else list(args.route)
    if not routes:
        ap.error("give a route, or --all")
    if not os.path.exists(SESSION):
        sys.exit(f"no session at {SESSION} - capture.py --login <magic-link> first")

    from playwright.sync_api import sync_playwright
    result = {}
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": 1600, "height": 1000},
                            color_scheme="light", storage_state=SESSION)
        ctx.route(BLOCK, lambda r: r.abort())
        pg = ctx.new_page()
        for route in routes:
            try:
                got = read_screen(pg, route)
            except Exception as exc:          # one bad screen must not end the sweep
                got = {"error": f"{type(exc).__name__}: {str(exc)[:120]}"}
            result[route] = got
            ch = got.get("chooser")
            print(f"  {route:<16} header {len(got.get('header', [])):>3}   "
                  f"chooser {len(ch['columns']) if ch else 0:>3}"
                  f"{'  ' + got['error'] if got.get('error') else ''}")
        b.close()

    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(result, fh, indent=1, ensure_ascii=False)
        print(f"\nwritten to {os.path.relpath(os.path.abspath(args.out), ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
