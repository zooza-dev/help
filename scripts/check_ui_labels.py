#!/usr/bin/env python3
"""Does every field name the help quotes still exist in the app?

    python3 scripts/check_ui_labels.py            # report to build/reports/ui-labels.md
    python3 scripts/check_ui_labels.py --file content/reference/class-detail.md

`check_nav.py` checks the *paths* we tell people to click through. This checks
the *labels* at the end of them. A renamed field is worse than a stale
screenshot: a reader looks at a picture and recognises the screen anyway, but
a reader hunting for a control called something else just does not find it,
and writes to support.

Convention, from CLAUDE.md: field names go in `backticks`, buttons in **bold**.
This reads the backticked ones and looks each up in the app's and the widgets'
current English strings, read from `origin/main` — the local checkouts run
behind, and on 2026-11-06 the app's was 92 commits back. The widget half comes
from api-v1, which serves the strings the widgets render.

Reports, never blocks. A miss is a question, not a verdict: the label may be
example data, a third-party screen, or a string assembled at runtime.
"""

import argparse
import collections
import difflib
import os
import re
import subprocess
import sys
import unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CONTENT = os.path.join(ROOT, "content")
OUT = os.path.join(ROOT, "build", "reports", "ui-labels.md")
ALLOW = os.path.join(os.path.dirname(__file__), "ui-labels-allow.yml")

# Where the product's English strings actually live. The widget entries used to
# point at widgets-v1/lang/en.js and src/lang/en.js. Neither path has ever
# existed, so for every run until 2026-11-09 this checked the admin app only and
# silently reported widget labels as missing. The widgets hold no string table:
# they read document.ZOOZA.locale, which api-v1 serves from js/locale/en-EN.js.
SOURCES = [("app", "lib/str_en3.js"),
           ("api-v1", "js/locale/en-EN.js")]

LABEL = re.compile(r"`([A-Z][^`\n]{2,52})`")

# Things in backticks that are not Zooza field names. Each pattern earned its
# place by appearing as a false positive on a real run.
NOT_A_LABEL = [
    (re.compile(r"[→<>{}|/\\]"),                 "contains punctuation we use for paths or code"),
    (re.compile(r"^[A-Z0-9_]+$"),                "constant or merge tag"),
    (re.compile(r"_[A-Z]|[A-Z]_"),               "merge tag"),
    (re.compile(r"@"),                           "email address"),
    (re.compile(r"\d{4,}"),                      "an identifier or example number"),
    (re.compile(r"^[A-Z]{2}\d{2}"),              "IBAN"),
    (re.compile(r"[€£$]"),                       "example amount"),
    (re.compile(r"^(TBD|Cmd|Ctrl|Shift|Alt|Esc|Enter|Tab)\b", re.I), "keyboard key"),
    (re.compile(r"…"),                           "truncated example"),
]

# Articles about somebody else's product: their field names are theirs.
THIRD_PARTY = re.compile(r"(abra-flexi|superfaktura|szamlazz|stripe|gocardless|pohoda|xero|"
                         r"quickbooks|ecomail|mailchimp|wix|wordpress)", re.I)


VALUE = re.compile(r"^\s*[a-zA-Z_0-9]+\s*:\s*'((?:[^'\\\\]|\\\\.)*)'", re.M)


def app_labels(blob: str) -> list:
    """Every individual UI string, so we can suggest what a missing one is now called.

    Searching the whole file as one blob answers "does this exist"; it cannot
    answer "then what is it called today", which is the question that actually
    gets an article fixed.
    """
    seen = {}
    for raw in VALUE.findall(blob):
        if 2 < len(raw) < 90 and not raw.startswith("<"):
            seen.setdefault(norm(raw), raw.replace("\\'", "'").replace('\\"', '"'))
    return seen


def app_strings() -> str:
    """Every English UI string the product ships, from origin/main."""
    out = []
    for repo, path in SOURCES:
        repo_dir = os.path.abspath(os.path.join(ROOT, "..", repo))
        if not os.path.isdir(repo_dir):
            continue
        subprocess.run(["git", "fetch", "origin", "main", "-q"], cwd=repo_dir,
                       capture_output=True)
        got = subprocess.run(["git", "show", f"origin/main:{path}"], cwd=repo_dir,
                             capture_output=True)
        if got.returncode == 0:
            out.append(got.stdout.decode("utf-8", "replace"))
    return "\n".join(out)


def norm(s: str) -> str:
    """Compare on meaning, not on typography.

    The app's strings live inside single-quoted JavaScript, so apostrophes and
    quotes arrive backslash-escaped; the help is written with typographic
    quotes and en dashes. Without this, "Sender's name in the SMS message"
    reads as missing when it is on screen in front of you.
    """
    s = s.replace('\\"', '"').replace("\\'", "'")
    s = unicodedata.normalize("NFKD", s)
    for a, b in [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'),
                 ("–", "-"), ("—", "-"), ("−", "-"), ("\xa0", " ")]:
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()



def allowed():
    """Labels a person has already judged to be fine, and why.

    Without this the same ten known-good misses head the report every run.
    Parsed by hand: the file is a flat list of label/why pairs and pulling in
    a YAML dependency for that would be the larger cost.
    """
    out = {}
    if not os.path.exists(ALLOW):
        return out
    label = None
    with open(ALLOW, encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r'\s*-\s*label:\s*"(.*)"\s*$', line)
            if m:
                label = m.group(1)
                out[norm(label)] = ""
                continue
            m = re.match(r'\s*why:\s*"(.*)"\s*$', line)
            if m and label is not None:
                out[norm(label)] = m.group(1)
                label = None
    return out


def skip_reason(label: str):
    for pat, why in NOT_A_LABEL:
        if pat.search(label):
            return why
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", help="check a single article")
    ap.add_argument("--quiet", action="store_true", help="report only, no per-label output")
    args = ap.parse_args()

    blob = app_strings()
    allow = allowed()
    strings = norm(blob)
    labels = app_labels(blob)
    keys = list(labels)
    if len(strings) < 10000:
        print("could not read the app's English strings — is ../app checked out?",
              file=sys.stderr)
        return 0  # reporting tool: never block the pipeline on its own plumbing

    paths = [args.file] if args.file else [
        os.path.join(dp, n)
        for dp, _, ns in os.walk(CONTENT) for n in sorted(ns) if n.endswith(".md")
    ]

    found = collections.Counter()
    where = collections.defaultdict(set)
    skipped = 0
    for p in paths:
        rel = os.path.relpath(p, ROOT)
        with open(p, encoding="utf-8") as fh:
            text = fh.read()
        third_party = bool(THIRD_PARTY.search(rel))
        for label in LABEL.findall(text):
            label = label.strip()
            if skip_reason(label):
                skipped += 1
                continue
            if third_party and norm(label) not in strings:
                skipped += 1          # their screen, their words
                continue
            if norm(label) in allow:
                skipped += 1          # already judged; see scripts/ui-labels-allow.yml
                continue
            if norm(label) not in strings:
                found[label] += 1
                where[label].add(rel)

    by_article = collections.defaultdict(list)
    for label, n in found.items():
        for rel in where[label]:
            by_article[rel].append((n, label))

    lines = ["# Field names the app no longer has", "",
             f"{len(found)} label(s) in `content/` are written in backticks — our convention for a",
             "field name — and do not appear in the app's or the widgets' current English strings.",
             "", "A miss is a question, not a verdict. The usual innocent explanations are example",
             "data, a label built at runtime from parts, and a screen belonging to somebody else's",
             "product. What it catches when it is right is the expensive case: a control we tell",
             "people to look for under a name it no longer has.", "",
             f"{skipped} backticked string(s) were skipped as not being Zooza field names,",
             f"{len(allow)} of them because somebody has already judged them fine - the reasons",
             "are in `scripts/ui-labels-allow.yml`, and deleting an entry re-opens the question.", ""]

    for rel in sorted(by_article, key=lambda r: -len(by_article[r])):
        lines.append(f"### `{rel}` — {len(by_article[rel])}")
        lines.append("")
        for n, label in sorted(by_article[rel], reverse=True):
            row = f"- `{label}`" + (f"  ×{n}" if n > 1 else "")
            # Only suggest when the match is strong. A loose cutoff produced
            # "Booking fee → Booking #" and "Amount owed → Amount of use", which
            # is worse than silence: a plausible wrong answer gets pasted in.
            near = difflib.get_close_matches(norm(label), keys, n=1, cutoff=0.86)
            if near and "%" in labels[near[0]]:
                # The app string has a placeholder and the article filled it in -
                # "Length of session - %1 minutes:" written up as "90 minutes".
                # Correct on both sides; not a rename, and saying so stops four
                # confident wrong suggestions.
                row += f"\n  - fine: our example of `{labels[near[0]]}`"
            elif near:
                row += f"\n  - looks renamed → `{labels[near[0]]}`"
            else:
                row += "\n  - no close match; check the screen by hand"
            lines.append(row)
        lines.append("")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")

    print(f"{len(found)} field name(s) not found in the app, across {len(by_article)} article(s)")
    print(f"  skipped as not-a-label: {skipped}")
    print(f"  report: {os.path.relpath(OUT, ROOT)}")
    if not args.quiet:
        for rel in sorted(by_article, key=lambda r: -len(by_article[r]))[:8]:
            print(f"  {len(by_article[rel]):>3}  {rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
