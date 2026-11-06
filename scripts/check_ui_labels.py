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
behind, and on 2026-11-06 the app's was 92 commits back.

Reports, never blocks. A miss is a question, not a verdict: the label may be
example data, a third-party screen, or a string assembled at runtime.
"""

import argparse
import collections
import os
import re
import subprocess
import sys
import unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CONTENT = os.path.join(ROOT, "content")
OUT = os.path.join(ROOT, "build", "reports", "ui-labels.md")

SOURCES = [("app", "lib/str_en3.js"),
           ("widgets-v1", "lang/en.js"),
           ("widgets-v1", "src/lang/en.js")]

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

    strings = norm(app_strings())
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
             f"{skipped} backticked string(s) were skipped as not being Zooza field names.", ""]

    for rel in sorted(by_article, key=lambda r: -len(by_article[r])):
        lines.append(f"### `{rel}` — {len(by_article[rel])}")
        lines.append("")
        for n, label in sorted(by_article[rel], reverse=True):
            lines.append(f"- `{label}`" + (f"  ×{n}" if n > 1 else ""))
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
