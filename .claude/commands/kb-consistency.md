# kb:consistency — Detect and fix content drift between guides and FAQs

## Purpose
Find articles that cover the same topic and check whether they say the same thing.
Guides and FAQs often drift after an update — the guide is corrected but the FAQ is not, or vice versa.
This skill surfaces those divergences and proposes a canonical answer.

## When to run
- After updating a guide or FAQ — to check whether related articles also need updating
- When a client reports conflicting information in the help centre
- Periodically after a large batch of intake changes (e.g. after a monthly intake session)
- When unsure whether a topic is already covered somewhere and in what form

## Inputs
The user provides one of:
- `$ARGUMENTS` — a topic keyword or phrase (e.g. "payment plan templates", "make-up waitlist")
- `$ARGUMENTS` — an article slug or file path (e.g. `content/faq/payments-and-billing-faq.md`)
- `$ARGUMENTS` — a changed file path from a recent commit (checks what the changed file links to via `related_articles`)

## Steps

### Step 1 — Identify the topic scope

If the input is a **keyword or phrase**:
- Run: `grep -rl "<keyword>" content/`
- Also run: `grep -rl "<keyword>" content/faq/ content/guides/ content/setup/ content/troubleshooting/`
- Collect all matching file paths

If the input is a **file path or slug**:
- Read the file's frontmatter to extract `related_articles` and `tags`
- Search for those slugs and tags: `grep -rl "<slug>" content/`
- Also grep for the main topic terms from the article title
- Collect all matching file paths

Deduplicate. If more than 10 files match, narrow scope by asking: "These 10 files mention the topic — do you want me to check all of them or focus on a specific subset (e.g. only FAQ files, or only guides)?"

### Step 2 — Read all candidate articles in full

For each file collected in Step 1:
- Read the entire file (not excerpts)
- Note:
  - The file path and slug
  - The article type (`type` field in frontmatter)
  - All headings that mention the topic
  - The specific claim(s) made about the topic under those headings

Output a summary table:

| File | Type | Heading | Claim |
|---|---|---|---|
| `content/faq/payments-and-billing-faq.md` | faq | "Where do I create payment plan templates?" | Created at Programme level in Settings → Price and Payment |
| `content/guides/payment-plans.md` | guide | "Setting up payment plans" | Created at class level in the class detail |

### Step 3 — Compare and classify divergences

For each topic claim, compare across files:
- **Consistent** — all files say the same thing (possibly with different wording) → no action needed
- **Stale** — one file has outdated information (e.g. old UI path, removed feature, changed behaviour)
- **Contradictory** — two or more files make conflicting factual claims
- **Incomplete** — one file covers the topic deeply, another mentions it but omits key details
- **Missing link** — articles that should reference each other but don't (not a content conflict, but a navigation gap)

Output a divergence table:

| Topic | Files affected | Type | Description |
|---|---|---|---|
| Where to create payment plan templates | payments-and-billing-faq.md, payment-plans.md | Contradictory | FAQ says Programme level; guide says class level |
| Make-up waitlist notification timing | make-up-sessions-faq.md, waiting-list-faq.md | Incomplete | FAQ mentions it; waiting-list guide doesn't |
| Login link expiry | login-and-account-faq.md | Stale | Old claim: link expires in 1 hour. Current: each new request invalidates previous link |

If no divergences found → state "No divergences found. All articles covering this topic are consistent." and stop.

### Step 4 — Establish the canonical answer

For each **Contradictory** or **Stale** divergence:
1. Identify which claim is most likely correct based on:
   - More recent `last_converted` date
   - Source: if one file has a verified claim (e.g. from intake or API spec) and the other is inferred
   - Internal logic: if one claim contradicts how the feature obviously works
2. If you cannot determine which is correct without external verification, flag it explicitly:
   > **Needs verification:** Cannot determine canonical answer from content alone. Check in the Zooza app or ask the user before updating.

Output:

| Topic | Canonical answer | Source of truth | Files to update | Action |
|---|---|---|---|---|
| Where to create payment plan templates | Programme level → Settings → Price and Payment | payments-and-billing-faq.md (2026-06-26, intake-verified) | payment-plans.md | UPDATE guide to match FAQ |
| Login link expiry | Each new request invalidates the previous link immediately | login-and-account-faq.md | — | Already consistent after intake update |

### Step 5 — Apply fixes

For each row in Step 4 where action is **UPDATE**:
- Always read the target file fully before editing
- Find the relevant heading in the file
- Update the claim to match the canonical answer
- Do not rewrite surrounding content — make the minimum change needed to correct the fact
- Update `last_converted` in frontmatter to today
- Also check `related_articles` in both files — if either is missing a link to the other, add it

For **Incomplete** divergences:
- Add a cross-reference ("See also") in the article that is missing context, pointing to the fuller article
- Do not duplicate content — link, don't copy

For **Missing link** divergences:
- Add the missing slug to `related_articles` in both files

After all edits:
- Stage each changed file: `git add content/<path>`
- Print a list of all files changed

### Step 6 — Report

Print a short summary:

```
## Consistency check — <topic>

Files checked: N
Divergences found: N
- Contradictory: N
- Stale: N
- Incomplete: N
- Missing link: N

Files updated:
- content/faq/... — <what was changed>
- content/guides/... — <what was changed>

Needs verification (cannot auto-fix):
- <topic> — <why it needs manual check>
```

## Done definition
Complete when:
- All candidate articles have been read in full (not excerpted)
- Divergence table printed
- Canonical answers established (or flagged for verification)
- All fixable divergences applied and staged
- Summary printed
- If any divergence was flagged "Needs verification" → ask user: "Can you check [X] in the app and let me know the correct answer?"
