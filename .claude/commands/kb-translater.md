# Skill: Zooza i18n Dictionary Standardiser (EN-GB source of truth)

## Purpose
Standardise all product texts and translations into a single canonical dictionary.
EN-GB is the source language. Enforce Zooza product terminology and client-facing wording rules.

This agent:
1) Normalises EN to EN-GB + Zooza vocabulary.
2) Standardises inconsistent terms (global + context-based).
3) Validates placeholders and HTML integrity across all languages.
4) Outputs one canonical dictionary plus a QA report and changelog.

## Inputs
Accept any of:
- CSV/TSV export
- JSON (any shape) as long as each record includes:
  - text_key
  - en (or original_text as EN draft)
  - optional per-language strings: sk, de, cs, pl, ro, hu, it
  - optional meta: domain, cluster, context (app/web/email), notes

## Output files
1) `dictionary.json` (canonical)
2) `dictionary.qa.json` (issues + warnings)
3) `dictionary.changelog.md` (human-readable summary)

### Canonical dictionary schema
{
  "text_key": {
    "meta": {
      "domain": "app|web|email|support|...",
      "context": "admin|client|mixed|unknown",
      "cluster": "optional",
      "notes": "optional"
    },
    "strings": {
      "en-GB": "...",
      "sk": "...",
      "de": "...",
      "cs": "...",
      "pl": "...",
      "ro": "...",
      "hu": "...",
      "it": "..."
    },
    "qa": {
      "placeholder_ok": true,
      "html_ok": true,
      "terminology_ok": true,
      "warnings": []
    }
  }
}

## Language order (fixed)
SK, EN-GB, DE, CS, PL, RO, HU, IT

## EN-GB rules
- Use UK spelling (programme, travelling, etc.).
- Keep UI labels short and consistent.
- Avoid salesy wording.
- Keep existing capitalisation patterns (buttons often ALL CAPS).

### Exception: “Enroll”
If the product already uses “Enroll” as a CTA and you want it preserved, keep it EXACTLY.
Otherwise prefer UK “Enrol”. Do not mix both.

## Zooza terminology rules

### Global hard replacements (EN-GB)
Always replace these in EN-GB output:
- timetable -> class
- group -> class
- course -> programme
- event(s) / lesson(s) -> session(s)
- replacement lesson(s) -> make-up lesson(s)
- teacher / tutor / trainer / lecturer -> instructor
- customer -> client

### Contextual replacements (EN-GB)
The agent must apply these based on meta.context/domain or inferred UI surface:

#### Client-facing (web / Parent Zone / parent portal)
- Use: booking / book / booked
- Avoid: registration / register
- Portal name: Parent Zone (title case)
- Avoid: “opt-out”; prefer “Cancel session” / “Cancel this session”

#### Admin-facing (back office)
- “registration” is allowed ONLY if it is a distinct internal concept in your system.
- If not distinct, standardise admin text to booking as well and flag any ambiguity.

#### Payments terminology
- Template naming: “Payment plan”
- Timeline/help: “payment schedule”
If a string uses “template” in a user-facing label, rewrite to the canonical term.

#### Billing period vs term
- Default: “billing period”
- If the string is explicitly parent-facing and school-like UX is intended, “term” is allowed.
- Fees: if “term” is used, “term fee” is allowed.

#### “Guest” meaning trial
- If “guest” refers to a trial participant, rewrite to “trial”.
- If “guest” means an unauthenticated visitor, keep “guest” and add warning: AMBIGUOUS_TERM.

#### “Class King” role
- Preserve the role label: “Class King”
- If explained, describe it as a client role that can manage attendance for a whole class.

## Placeholders & HTML invariants (hard rules)
- Do not modify placeholders:
  - *|LIKE_THIS|*, {like_this}, {{like_this}}, %s, etc.
- Do not break HTML tags or attributes.
- If placeholders differ across languages vs EN-GB:
  - Add issue PLACEHOLDER_MISMATCH
  - If safe, fix the translation string to match placeholders exactly.
- If HTML is invalid in source:
  - Fix EN-GB if clearly correctable, but add warning HTML_FIXED.

## Workflow per record
1) Determine canonical EN input:
   - use `en` if present; else `original_text` as EN draft.
2) Infer context:
   - If meta.context given: use it.
   - Else infer:
     - domain=web / contains “Parent Zone” / pay now / portal UI -> client
     - domain=email -> mixed (conservative)
     - domain=app admin menus/settings -> admin
3) Rewrite EN to canonical EN-GB:
   - apply global + contextual terminology
   - keep meaning identical
   - preserve placeholders & HTML exactly
4) Validate:
   - placeholders parity across languages
   - HTML validity
   - forbidden terms (per context)
5) Preserve translations unless:
   - placeholders mismatch (must fix)
   - translation clearly uses forbidden legacy terms and a safe direct replacement exists (optional fix; otherwise warning)

## Global consistency pass (after all keys)
- Find near-duplicate strings and inconsistent phrases across keys:
  - cancel wording variants
  - booking vs registration drift
  - programme/session/class drift
- Propose unification list:
  - Only auto-change when confidence is high; else add warnings.

## QA report (`dictionary.qa.json`)
{
  "summary": {"total_keys":0,"issues":0,"warnings":0},
  "by_key": {
    "some_key": {
      "issues": [{"type":"PLACEHOLDER_MISMATCH","detail":"..."}],
      "warnings": [{"type":"AMBIGUOUS_TERM","detail":"..."}]
    }
  }
}

## Changelog (`dictionary.changelog.md`)
Include:
- totals
- top terminology replacements counts
- keys changed in EN-GB (top 50)
- list of must-fix issues (placeholder/html)

## Done Definition
Complete when:
- dictionary.json exists for all keys
- EN-GB strings comply with Zooza vocabulary and context rules
- QA + changelog generated
- Placeholder and HTML issues reported (and fixed where safe)
