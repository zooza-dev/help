#!/usr/bin/env python3
"""Which programme settings does the help never mention?

    python3 scripts/check_settings_coverage.py
    python3 scripts/check_settings_coverage.py --branch origin/main

The programme settings redesign ships a registry: one authoritative entry per
setting, generated from the screen's own source rather than kept by hand. That
makes "have we written about all of them?" a question a script can answer,
instead of a question answered by remembering.

For each setting it resolves the i18n label key to English, then looks for that
label anywhere in `content/`. A setting nothing mentions is either a gap or a
rename — both worth knowing, and the difference needs a person.

Reports, never blocks.
"""

import argparse
import collections
import json
import os
import re
import subprocess
import sys
import unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
APP = os.path.abspath(os.path.join(ROOT, "..", "app"))
CONTENT = os.path.join(ROOT, "content")
OUT = os.path.join(ROOT, "build", "reports", "settings-coverage.md")

INVENTORY = "docs/programme-settings/inventory.md"
STRINGS = "lib/str_en3.js"

ROW = re.compile(r"^\| `([a-z_0-9.]+)` \| [^|]* \| [^|]* \| `([a-z_0-9]*)` \|", re.M)
KV = re.compile(r"^\s*([a-zA-Z_0-9]+)\s*:\s*'((?:[^'\\]|\\.)*)'", re.M)


def app_file(branch, path):
    got = subprocess.run(["git", "show", f"{branch}:{path}"], cwd=APP, capture_output=True)
    return got.stdout.decode("utf-8", "replace") if got.returncode == 0 else ""


def norm(s):
    s = s.replace('\\"', '"').replace("\\'", "'")
    s = unicodedata.normalize("NFKD", s)
    for a, b in [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'),
                 ("–", "-"), ("—", "-"), ("\xa0", " ")]:
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--branch", default="origin/feature-programme-settings-redesign",
                    help="where to read the registry from")
    args = ap.parse_args()

    subprocess.run(["git", "fetch", "origin", args.branch.split("/")[-1], "-q"],
                   cwd=APP, capture_output=True)
    inventory = app_file(args.branch, INVENTORY)
    if not inventory:
        print(f"no {INVENTORY} on {args.branch} — has the redesign branch moved?",
              file=sys.stderr)
        return 0
    strings = {k: v for k, v in KV.findall(app_file(args.branch, STRINGS))}

    settings, unlabelled = [], 0
    for sid, key in ROW.findall(inventory):
        label = strings.get(key, "").strip()
        if label:
            settings.append((sid, label))
        else:
            unlabelled += 1

    docs = {}
    for dp, _, ns in os.walk(CONTENT):
        for n in ns:
            if n.endswith(".md"):
                p = os.path.join(dp, n)
                with open(p, encoding="utf-8") as fh:
                    docs[os.path.relpath(p, CONTENT)] = norm(fh.read())

    covered, missing, skipped = {}, [], 0
    for sid, label in settings:
        nl = norm(label)
        if len(nl) < 5:        # a two-word label matches by accident
            skipped += 1
            continue
        hits = sorted(a for a, t in docs.items() if nl in t)
        if hits:
            covered[sid] = hits
        else:
            missing.append((sid, label))

    by_group = collections.Counter(s.split(".")[0] for s, _ in missing)
    lines = ["# Programme settings the help never mentions", "",
             f"Registry read from `{args.branch}`. **{len(covered)} of "
             f"{len(covered) + len(missing)} settings** appear somewhere in `content/`.", "",
             "A setting on this list is one of two things, and telling them apart needs a",
             "person: a **gap**, where we have never written about it, or a **rename**, where",
             "we have, under the name it used to have. The second kind is the more urgent -",
             "the article reads fine and sends the reader looking for a control that is not",
             "there any more.", ""]
    if skipped:
        lines += [f"{skipped} label(s) too short to match on were left out; "
                  f"{unlabelled} registry entries have no label key at all.", ""]

    lines += ["## By group", "", "| Group | Not mentioned |", "|---|---:|"]
    for g, n in by_group.most_common():
        lines.append(f"| `{g}` | {n} |")
    lines += ["", "## The settings", "", "| Setting | Label on screen |", "|---|---|"]
    for sid, label in sorted(missing):
        lines.append(f"| `{sid}` | {label} |")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")

    print(f"{len(covered)} of {len(covered) + len(missing)} settings are mentioned in the help")
    print(f"  not mentioned: {len(missing)}")
    print(f"  report: {os.path.relpath(OUT, ROOT)}")
    for g, n in by_group.most_common(8):
        print(f"  {n:>3}  {g}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
