#!/usr/bin/env python3
"""Recapture KB screenshots from the live app.

Reads a manifest of shots, drives a real browser through them, masks the few
literal strings we must never publish, and stages the images for review. Nothing
touches `assets/images/` until you pass --apply.

    python3 scripts/screenshots/capture.py                  # shoot everything, stage it
    python3 scripts/screenshots/capture.py --only cls-classes.png
    python3 scripts/screenshots/capture.py --apply          # copy staged shots over the real ones

Before the first run
--------------------
1. Log in to the app in a browser, then export the session:

       python3 scripts/screenshots/capture.py --login <magic-link>

   The session is written to build/intake/zooza-session.json, which is
   gitignored. It is a credential — do not move it into the repo proper.

2. Put the literal strings to mask in build/intake/screenshot-mask.json:

       {"emails": ["@zooza.online"], "literals": {"+421 900 000 000": "+44 7700 900000"}}

   Literals only, deliberately. Two earlier attempts at clever pattern matching
   both did damage: "two capitalised words" renamed the menu item Custom Holidays
   to a person, and a phone-shaped regex turned the date 16. 09. 2026 into a
   phone number. A literal cannot hit anything it was not aimed at.

Why every shot carries an assertion
-----------------------------------
The app is a single-page app behind a hash route, so a wrong route renders
"Page not found" with the whole navigation still on screen — and a naive check
for the page name passes, because the name is sitting in the left-hand menu.
Each shot therefore names something only that screen has.
"""

import argparse
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
STAGE = os.path.join(ROOT, "build", "screenshots")
IMAGES = os.path.join(ROOT, "assets", "images")
SESSION = os.path.join(ROOT, "build", "intake", "zooza-session.json")
MASKFILE = os.path.join(ROOT, "build", "intake", "screenshot-mask.json")

# Third parties that either throw in a headless browser or draw over the page.
BLOCK = re.compile(r"(intercom|hotjar|googletagmanager|google-analytics|facebook\.net)")

MASK_JS = r"""
(cfg) => {
  let n = 0;
  const fix = (v) => {
    let o = v;
    for (const dom of cfg.emails) {
      const re = new RegExp('[A-Za-z0-9._%+-]+' + dom.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi');
      o = o.replace(re, () => { n++; return cfg.emailReplacement; });
    }
    for (const [from, to] of Object.entries(cfg.literals)) {
      // tolerate any spacing inside the literal (phone numbers get typed several ways)
      const re = new RegExp(from.replace(/[.*+?^${}()|[\]\\]/g, '\\$&').replace(/\s+/g, '\\s*'), 'gi');
      o = o.replace(re, () => { n++; return to; });
    }
    return o;
  };
  const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const nodes = []; while (w.nextNode()) nodes.push(w.currentNode);
  for (const t of nodes) {
    if (!t.nodeValue || !t.nodeValue.trim()) continue;
    const tag = t.parentElement && t.parentElement.tagName;
    if (tag === 'SCRIPT' || tag === 'STYLE') continue;
    const v = fix(t.nodeValue);
    if (v !== t.nodeValue) t.nodeValue = v;
  }
  document.querySelectorAll('input,textarea').forEach(i => {
    if (i.value) { const v = fix(i.value); if (v !== i.value) i.value = v; }
  });
  return n;
}
"""


def load_manifest(path):
    import yaml
    with open(path, encoding="utf-8") as fh:
        doc = yaml.safe_load(fh)
    return doc["base"], doc["shots"]


def load_mask():
    if not os.path.exists(MASKFILE):
        return {"emails": [], "literals": {}, "emailReplacement": "demo@example.com"}
    cfg = json.load(open(MASKFILE, encoding="utf-8"))
    cfg.setdefault("emails", [])
    cfg.setdefault("literals", {})
    cfg.setdefault("emailReplacement", "demo@example.com")
    return cfg


def do_login(link):
    from playwright.sync_api import sync_playwright
    os.makedirs(os.path.dirname(SESSION), exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": 1600, "height": 1000})
        pg = ctx.new_page()
        pg.goto(link, timeout=60000)
        pg.wait_for_timeout(9000)
        company = pg.inner_text("body").split("\n")[0].strip()
        ctx.storage_state(path=SESSION)
        b.close()
    print(f"signed in — company shown in the sidebar: {company!r}")
    print(f"session written to {SESSION} (gitignored)")
    print("check that company is the one you meant before capturing anything.")


def capture(manifest_path, only, apply_it):
    from playwright.sync_api import sync_playwright
    base, shots = load_manifest(manifest_path)
    mask = load_mask()
    if only:
        shots = [s for s in shots if s["image"] == only]
        if not shots:
            sys.exit(f"no shot named {only} in the manifest")
    if not os.path.exists(SESSION):
        sys.exit(f"no session at {SESSION} — run with --login <magic-link> first")
    os.makedirs(STAGE, exist_ok=True)

    results = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": 1600, "height": 1000},
                            device_scale_factor=2, color_scheme="light",
                            storage_state=SESSION)
        ctx.route(BLOCK, lambda r: r.abort())
        pg = ctx.new_page()
        for shot in shots:
            name, route = shot["image"], shot["route"]
            out = os.path.join(STAGE, name.replace("/", "__"))
            try:
                pg.goto(f"{base}#{route.lstrip('#')}", timeout=60000)
                pg.wait_for_timeout(shot.get("wait", 8000))
                text = pg.inner_text("body")

                if "Page not found" in text:
                    results.append((name, "BAD ROUTE", "the app rendered its 404"))
                    continue

                # The assertion must name something only this screen has. The left-hand
                # navigation is on every page, 404s included, so a page name alone
                # proves nothing.
                need = shot["assert"]
                if need not in text:
                    results.append((name, "NOT FOUND", f"expected {need!r} on the page"))
                    continue

                masked = pg.evaluate(MASK_JS, mask)
                pg.wait_for_timeout(300)

                after = pg.inner_text("body")
                leaked = [d for d in mask["emails"] if d.lower() in after.lower()]
                leaked += [l for l in mask["literals"] if re.search(
                    re.escape(l).replace(r"\ ", r"\s*"), after, re.I)]
                if leaked:
                    results.append((name, "PII LEFT", ", ".join(leaked)))
                    continue

                pg.screenshot(path=out)
                results.append((name, "ok", f"masked {masked}"))
            except Exception as exc:                      # noqa: BLE001
                results.append((name, "ERROR", f"{type(exc).__name__}: {exc}"[:90]))
        b.close()

    print(f"\n{'image':44} {'result':10} detail")
    print("-" * 96)
    for name, status, detail in results:
        print(f"{name:44} {status:10} {detail}")

    good = [r for r in results if r[1] == "ok"]
    print(f"\n{len(good)}/{len(results)} captured — staged in {STAGE}")
    if not apply_it:
        print("look at them, then re-run with --apply to replace the real images.")
        return 0 if len(good) == len(results) else 1

    for name, status, _ in results:
        if status != "ok":
            continue
        src = os.path.join(STAGE, name.replace("/", "__"))
        dst = os.path.join(IMAGES, name)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        print(f"  applied {name}")
    print("\nNow bump last_converted on every article whose image changed, and rewrite")
    print("the alt text if the screen no longer shows what it used to.")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--manifest", default=os.path.join(HERE, "manifest.yml"))
    ap.add_argument("--only", help="capture a single image from the manifest")
    ap.add_argument("--apply", action="store_true", help="copy staged shots over assets/images")
    ap.add_argument("--login", metavar="LINK", help="sign in with a magic link and save the session")
    args = ap.parse_args()

    if args.login:
        do_login(args.login)
        return 0
    return capture(args.manifest, args.only, args.apply)


if __name__ == "__main__":
    sys.exit(main())
