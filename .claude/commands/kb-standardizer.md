# kb:standardizer — Extract Zooza terminology dictionary from content

## Purpose
Scan all Markdown files in `content/` and extract a canonical dictionary of Zooza-specific terms, keywords, and phrases. Identify inconsistencies, synonyms, and ambiguous usage so terminology can be normalised across the product, help docs, and translations.

## When to run
- After a batch conversion (kb:convert)
- Before starting translation work
- Periodically to catch terminology drift

## Inputs
- All `.md` files in `content/`
- `taxonomy.yml` (product areas, doc types, audiences)
- Existing dictionary at `build/terminology/dictionary.json` (if present — merge, don't overwrite)

## Outputs
- `build/terminology/dictionary.json` — canonical term dictionary
- `build/terminology/inconsistencies.md` — human-readable report of conflicts and ambiguities

## Dictionary schema

```json
{
  "terms": {
    "canonical_term": {
      "canonical": "class",
      "variants_found": ["group", "timetable", "class"],
      "occurrences": 142,
      "files": ["course-settings.md", "blocks-creation.md"],
      "category": "core_concept",
      "context": "admin|client|both",
      "notes": "UI uses 'class' everywhere; legacy docs often say 'group'"
    }
  },
  "extracted_at": "2026-02-11",
  "source_file_count": 85
}
```

## Term categories
- **core_concept** — fundamental Zooza objects (programme, class, session, booking, client)
- **role** — user roles (admin, instructor, client, Class King)
- **action** — verbs/CTAs (book, cancel, enrol, register)
- **payment** — payment-specific terms (payment plan, billing period, outstanding amount)
- **ui_element** — named UI surfaces (Parent Zone, dashboard, widget)
- **status** — status labels (active, cancelled, waitlist, trial, deleted)
- **integration** — third-party names (GoCardless, Stripe, Xero, Power BI)

## Extraction rules

### Step 1 — Scan content
For each `.md` file in `content/`:
1. Parse frontmatter — extract `title:` value as a scannable field (it may contain non-canonical terms).
2. Strip image references from body.
3. Extract all **bold** terms (likely UI labels / buttons).
4. Extract all `code` terms (likely field names / settings).
5. Extract nouns and noun phrases that appear 3+ times across the corpus.
6. Extract terms from the `title:` frontmatter field and H1/H2/H3 headings.

### Step 2 — Cluster synonyms
Group terms that refer to the same concept. Known synonym clusters to seed:

| Canonical | Variants to detect |
|---|---|
| programme | course |
| class | group, timetable |
| session | event, lesson |
| booking | registration |
| client | customer, parent, user (when meaning client) |
| instructor | lecturer, teacher, tutor, trainer |
| make-up lesson | replacement lesson |
| Parent Zone | parent portal |
| payment plan | payment template |
| billing period | term (when meaning billing period) |
| trial | guest (when meaning trial participant) |
| lead collection | group interested, group – interested, class interested, class – interested, interested (when meaning interest gathering without dates) |

### Step 3 — Count and locate
For each term/variant:
- Count total occurrences across all files.
- List which files use which variant.
- Flag files where multiple variants of the same concept appear.

### Step 4 — Detect new/unknown terms
Any Zooza-specific term that doesn't fit a known cluster should be added as a new entry with `category: "unknown"` for human review.

### Step 5 — Generate inconsistency report
Write `build/terminology/inconsistencies.md`:

```markdown
# Terminology Inconsistencies

## Summary
- Total terms extracted: N
- Synonym clusters: N
- Files with mixed terminology: N
- New/unknown terms for review: N

## Mixed usage by file
### course-settings.md
- Uses "group" (3x) and "class" (2x) — canonical: **class**
- Uses "event" (1x) and "session" (4x) — canonical: **session**

## Variant frequency
| Canonical | Variant | Count | Files |
|---|---|---|---|
| class | group | 47 | 12 files |
| class | timetable | 3 | 2 files |
| programme | course | 89 | 34 files |

## Unknown terms (need review)
- "turnus" (2x) — possibly means "shift" or "rotation"?
```

## Merge behaviour
If `dictionary.json` already exists:
- Keep manually added `notes` and `context` overrides.
- Update `occurrences`, `files`, and `variants_found` from fresh scan.
- Add new terms; never delete existing terms (mark as `occurrences: 0` if gone).

## Done definition
Complete when:
- `dictionary.json` written with all extracted terms
- `inconsistencies.md` written with conflict report
- Both files are valid and parseable
