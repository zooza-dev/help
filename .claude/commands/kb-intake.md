# kb:intake — Analyse customer communication and extract KB/glossary gaps

## Purpose
Process a raw customer support message, chat, or ticket and extract:
1. What the customer actually wanted (intent)
2. What terminology they used (including misattributions)
3. What is missing or outdated in the KB or glossary

## When to run
- After pasting a customer chat, support ticket, or question
- When you notice terminology in the wild that isn't captured in the glossary
- When a customer question reveals a content gap in `content/`

## Inputs
The user provides:
- `$ARGUMENTS` — the raw customer communication (paste directly after the command)
- Optional context: what the correct answer was, what the customer actually meant

## Steps

### Step 1 — Parse the communication
Read the full input. Identify:
- The customer's language (EN / SK / DE / other)
- The core question or request (one sentence)
- All product-related terms the customer used (exact words)

### Step 2 — Intent analysis
For each term or phrase the customer used, determine:
- Is it a known canonical term? (check `content/glossary/terminology.yml`)
- Is it a deprecated term? (check `deprecated` fields in terminology.yml)
- Is it an entity misattribution? (e.g. said "client" but meant "booking")
- Is it a synonym not yet in the glossary?
- Is it a term in a non-English language not yet captured in `intent_keywords`?

Output a table:

| Customer said | Language | Canonical term | Issue type |
|---|---|---|---|
| "presunúť dieťa" | SK | Transfer (Booking) | entity misattribution |
| "kurz" | SK | Programme | missing SK intent keyword |
| "payment schedule" | EN | Payment Plan | deprecated term used |

**Issue types:**
- `entity_misattribution` — customer named the wrong entity
- `missing_synonym` — valid synonym not yet in glossary
- `deprecated_term` — old term still in use
- `missing_translation` — term in a language not yet in intent_keywords
- `unknown_term` — term not recognised at all
- `content_gap` — no KB article covers what they asked

### Step 3 — Content gap analysis
Determine if the question is already answered in `content/`:
- Search for relevant guides and FAQs
- If covered: note which article answers it
- If partially covered: note what's missing
- If not covered: flag as content gap with suggested location and type

Output:

| Question | Covered? | File | Gap |
|---|---|---|---|
| How to transfer a booking | Yes | transfer-and-copy-bookings.md | — |
| How to give a client a free session | Partial | replacement-hours-complete.md | Free credits vs make-up not clearly explained |
| How to set up blocks | No | — | New guide needed: content/guides/blocks-creation.md |

### Step 4 — Generate outputs

#### A) Glossary updates
For each `entity_misattribution`, `missing_synonym`, `missing_translation`, or `unknown_term`:
- Add to `content/glossary/terminology.yml` (correct section)
- Add to the misattribution table in `content/glossary/terminology-review.md` if it's an entity misattribution

#### B) Content actions
For each content gap, output one of:
- **UPDATE** — add a section to an existing article (provide draft text)
- **NEW** — create a new article (provide frontmatter + draft outline)
- **FAQ** — add a Q&A to an existing FAQ file (provide draft Q&A)

Always include a draft for the highest-priority gap.

#### C) Summary report
Print a short summary at the end:

```
## Intake summary
- Communication language: SK
- Core intent: Transfer a booking to a different class
- Terms analysed: 4
- Glossary updates: 2 (1 missing SK keyword, 1 entity misattribution added)
- Content gaps: 1 (partial — free credits vs make-up not clear)
- Action: Added FAQ entry draft to make-up-sessions-faq.md
```

## Glossary update format
When adding to `terminology.yml`, always follow the existing schema.
When adding a misattribution to `terminology-review.md`, add a row to the
Entity misattribution table AND a new entry under `entity_misattribution:` in the YAML.

## Priority rules
- Entity misattributions → always update glossary immediately
- Content gaps with no existing article → flag, ask user before creating
- Content gaps in existing article → provide draft, ask user to approve before writing
- Deprecated terms used by customer → note only (do not auto-update content)

## Done definition
Complete when:
- Intent analysis table printed
- Content gap table printed
- All glossary updates applied (or listed if skipped)
- Summary printed
- User asked: "Want me to create/update the content for the gaps found?"
