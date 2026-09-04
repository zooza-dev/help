#!/usr/bin/env python3
"""Compare the public glossary page against the master terminology dictionary.

The dictionary is the source of truth for what a term means; the glossary page is
the reader-facing rendering of it. They drift when a term is added to one and not
the other, and the drift is invisible until someone asks about a term the help
centre never defines.

This reports, it never writes. The glossary page is hand-written prose — entries
carry cross-links and "formerly called" notes the dictionary has no field for — so
new entries are added by a person, in the surrounding style.

Usage:
    python3 scripts/check_glossary_sync.py
    python3 scripts/check_glossary_sync.py --master path/to/terminology.yml
"""
import argparse
import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip3 install pyyaml")

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEFAULT_MASTER = os.path.abspath(
    os.path.join(REPO, "..", "sdd-workflow", "translations", "terminology.yml")
)
GLOSSARY = os.path.join(REPO, "content", "glossary", "index.md")

ap = argparse.ArgumentParser()
ap.add_argument("--master", default=DEFAULT_MASTER)
ap.add_argument("--glossary", default=GLOSSARY)
args = ap.parse_args()

if not os.path.exists(args.master):
    sys.exit(f"Master dictionary not found: {args.master}")

with open(args.master, encoding="utf-8") as f:
    master = yaml.safe_load(f)

with open(args.glossary, encoding="utf-8") as f:
    page = f.read()


def norm(s):
    """Compare on letters and digits only — casing, dashes and spacing all drift."""
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def variants(name):
    """A dictionary name and the heading a reader sees are rarely byte-identical.

    The dictionary disambiguates — "Pending (registration status)" — where the page
    heads the entry "Pending" and lets the surrounding section do that work. Accept
    both, so a qualifier in the dictionary does not read as a missing entry.
    """
    out = {norm(name)}
    out.add(norm(re.sub(r"\s*\(.*?\)", "", name)))          # drop the qualifier
    out.add(norm(re.sub(r"\s*\bvs\.?\b.*$", "", name)))     # "X vs. Y" heads as "X"
    return {v for v in out if v}


public = [t for t in master.get("terms", []) if t.get("public")]
headings = re.findall(r"^### (.+?)\s*$", page, re.M)
have = set()
for h in headings:
    have |= variants(h)

missing = [t for t in public if not (variants(t["canonical_en"]) & have)]

# A heading with no dictionary entry is not automatically wrong — the page carries a
# few plain-English entries — but it is worth seeing, because it is usually a term
# that was defined for readers and never made it into the dictionary the bot reads.
known = set()
for t in master.get("terms", []):
    known |= variants(t["canonical_en"])
    for syn in (t.get("synonyms") or []):
        known.add(norm(syn))
    # A see-also entry under an old name is good practice, not drift — the
    # glossary is where someone looks up the word they still have in their head.
    for old in (t.get("deprecated") or []):
        known.add(norm(old))
extra = [h for h in headings if not (variants(h) & known)]

print(f"Master dictionary : {len(master.get('terms', []))} terms, {len(public)} public")
print(f"Glossary page     : {len(headings)} entries")
print()

if missing:
    print(f"Public terms missing from the glossary page ({len(missing)}):")
    for t in missing:
        print(f"  - {t['canonical_en']}  [{t.get('category', '—')}]  id: {t['id']}")
    print()
    print("  Add each as a `### Term` entry in its A–Z section, in the page's own")
    print("  style — definition first, then any 'Also referred to as' note.")
    print()

if extra:
    print(f"Glossary entries with no dictionary term ({len(extra)}):")
    for h in extra:
        print(f"  - {h}")
    print()
    print("  Either add them to the master dictionary so the assistant knows them,")
    print("  or fold them into an existing entry.")
    print()

if not missing and not extra:
    print("In sync.")

# Reports rather than blocks — the glossary is prose and lands a beat after the
# dictionary by design.
sys.exit(0)
