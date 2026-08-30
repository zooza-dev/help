# kb:weekly — Friday intake: work the week's queue into the KB

## Purpose
Turn one week of customer communication into KB changes. Covers Intercom
conversations, client email threads, and specs that shipped without anyone
telling users. Runs the mechanical prep, then works the queue with the user.

For a single pasted chat or ticket, use `/kb-intake` instead — this command is
the weekly batch.

## When to run
Friday morning. Running late is fine: the window continues from where the last
run stopped, so nothing is skipped.

## Inputs
None. `$ARGUMENTS` may carry a date override (`--date YYYY-MM-DD`) for a
back-dated run.

---

## Step 1 — Prepare the queue

```bash
python3 scripts/intake/weekly_prep.py
```

Report the window and the counts it prints. If it says everything is already
reviewed, stop and say so — do not invent work.

Read `build/reports/weekly-intake-<end-date>.md` in full before doing anything else.

## Step 2 — Build the review board

```bash
python3 scripts/intake/weekly_artifact.py --start <start> --end <end>
```

Then publish it with the Artifact tool, declaring `capabilities: {artifact: {}}` so
the board can save decisions into itself. Republish the **same file path** every
week only if you want one rolling board; normally each week gets its own.

Before generating, write the two sidecars the board reads. Both are keyed by
conversation id and both are optional — the board renders without them, just
blind.

`build/intake/notes-<end>.json` — your read on each conversation:

```json
{"215475348814074": {
  "verdict": "gap|verify|check|product|client|noise",
  "cat": "programmes|pricing|payments|bookings|trials|makeups|clients|team|widgets|comms|reports|ai|account|noise",
  "title": "One line naming what this is really about",
  "note": "What you found and why it matters. Name the other conversations that hit the same thing."
}}
```

`build/intake/email-<end>.json` — client email threads, since the Gmail
connector cannot run in the prep script. Same fields plus `who`, `subject`,
and `turns` as `[role, name, text]` triples (`customer` / `human`).

**Verdicts are suggestions, not decisions.** The board maps them onto a
suggested decision and the reviewer confirms or overrides. Never pre-fill the
decision itself — deciding is the reviewer's job, and a board that arrives
pre-decided gets rubber-stamped.

### What the board is for

It is a working surface, not a report. Every conversation gets:

| | |
|---|---|
| **Decision** | Fine as answered / Into the KB / Dig into it / Product, not KB |
| **Category** | What the client was asking about — the rollup makes repeat themes visible |
| **Note to Claude** | Free text: what the reviewer wants done with this one |
| **Conversation id** | One click to copy, so screenshots pasted into the chat can name it |

The header tracks how many are decided. **Hand to Claude** produces a digest
grouped by decision, with the notes attached — that digest is the input to
step 5.

To carry decisions into a regenerated board, export the state and pass
`--state <file>.json`.

## Step 3 — Human answers first

Section 1 of the queue, and the board's Human filter. **These are the gold standard** — a human agent already
worked out the correct answer, so the only question is whether it generalises.

For each one, decide:
- **Generalises** → belongs in the KB. Find where.
- **One client's specific situation** → skip it. Say which and why.

Do not skip this section in favour of the bot findings. It is where the value is.

## Step 4 — Bot-only, by risk

Section 2, already ranked; on the board these are the AI only rows. Read the buckets as evidence, not as scores:

| Bucket | What it means | Usual cause |
|---|---|---|
| `A_hard_signal` | Routed to team, abandoned, or rated poorly | The bot could not answer at all |
| `B_no_kb_source` | The bot cited nothing from the KB | No article exists |
| `C_reask` | Client asked 2+ times | An article exists but does not answer the question |

**A bot answer sourced only from marketing pages is the strongest predictor of a
wrong answer.** Watch for `Zooza PRO`, `Ceník`, and blog posts in the cited list.

Frame every finding as a **KB gap**, never as a "bot error". The bot repeats what
the KB tells it; three wrong answers in July traced back to wrong KB content.

## Step 5 — Client email

Section 4 of the queue lists the sender allowlist and a ready-made Gmail query. Run it with the
Gmail connector.

Keyword search does not work here — the mailbox is mostly `no-reply` booking
notifications. Search by sender.

These threads carry questions Intercom never sees, because they come from the
franchise owners rather than end customers.

## Step 6 — Write the changes

**Before writing anything, follow the mandatory pre-write check in CLAUDE.md:**
grep for candidates, then *read the 2–3 most relevant articles in full*. Grep
misses topics covered in different wording.

Then, for each change:
- Prefer a new section in an existing article over a new standalone article.
- Add `related_articles` to frontmatter, and check whether those articles need
  the same update.
- Brand-new FAQ? Run `python3 scripts/generate_faq_schema.py` before exporting —
  the SEO check blocks on a missing schema file.

**Never document product behaviour you have not verified.** If a customer report
implies a behaviour but nothing confirms it, ask the user. Do not write a
plausible guess. The July 2026 intake produced three false claims that only the
user caught.

### Finish the frontmatter on every article you touch

Editing the body is half the job. Before moving on, on **each** file changed:

| Field | What to do |
|---|---|
| `last_converted` | Set to today. Otherwise nothing downstream can tell the article moved, and a February date on an article rewritten in August is simply wrong. |
| `related_articles` | Must be present. Add it if the article never had one — several older articles do not. |
| `description` | Re-read it. If the edit changed what the article is now mostly about, the description is stale. |
| `tags` | Add one only if the edit introduced a genuinely new topic. |

Check the whole batch at the end rather than trusting memory:

```bash
for f in $(git diff --cached --name-only -- content/); do
  printf "%-52s %-12s %s\n" "$(basename $f)" \
    "$(grep -m1 '^last_converted:' $f | sed 's/.*: *//;s/"//g')" \
    "$(grep -c '^related_articles:' $f)"
done
```

Every row should show today's date and a `1`.

## Step 7 — Dictionary and glossary

The KB explains; the dictionary is what the assistant reasons with. A week that
produced KB changes has almost always produced dictionary work too, and skipping
it is why the bot keeps missing questions the KB can already answer.

**Propose dictionary changes as part of the weekly write-up — do not wait to be
asked.** For each thing written this week:

1. **New wording customers used** → add to `intent_keywords` on the existing term,
   in their language. This is where "ukážková hodina", "poradovník" and "členské"
   belong. Per-language variants live **only** here, never in public content.
2. **A distinction that caused a wrong answer** → add a `do_not_confuse_with`
   entry with the reason. Členské vs kurzovné is the model: two words, one mix-up,
   one line that prevents it.
3. **Behaviour confirmed this week** → add to `ai_notes`, dated. Say plainly when
   it supersedes older content, so a stale article does not quietly win.
4. **A term with no entry at all** → add the term.

Edit **only** the master:

```
{root}/sdd-workflow/translations/terminology.yml
```

`help/content/glossary/terminology.yml` is a derived copy. Never edit it in place.

Then check the reader-facing page, which drifts behind the dictionary:

```bash
python3 scripts/check_glossary_sync.py
```

It reports and never writes. Add any missing **public** term to
`content/glossary/index.md` by hand, in the page's own style — an entry there is
prose with cross-links, not a dump of the YAML. Terms on the page with no
dictionary entry are the same problem in reverse: the assistant cannot use a
definition that only exists as prose.

## Step 8 — Specs that shipped silently

Section 3 of the queue lists implemented specs with no `docs_communicated` date. For each one
the KB now covers, stamp the spec's frontmatter:

```yaml
docs_communicated: "YYYY-MM-DD"
```

If a spec needs something from another repo, create a handoff rather than guessing.

## Step 9 — Export and commit

```bash
python3 scripts/export/export_all.py
```

Commit in batches with a plain message describing what changed for the user, not
which conversation prompted it. Stage by explicit path — never `git add .`.

Push only when the user asks.

---

## Done definition
Complete when:
- Every human answer in section 1 is either written up or explicitly skipped with a reason
- Every `A_hard_signal` and `B_no_kb_source` item has a decision
- Email threads for the window have been read
- Every touched article has today's `last_converted` and a `related_articles` list
- Dictionary additions are proposed, and `check_glossary_sync.py` reports no missing public term
- `export_all.py` passes with 0 errors
- Specs now covered are stamped with `docs_communicated`
- A short summary is printed: counts in, changes made, questions left for the user

## Summary format

```
## Weekly intake — 2026-08-07 to 2026-08-13
- Human answers: 24 (9 written up, 15 client-specific)
- Bot-only needing a look: 18 (6 KB gaps closed, 12 already covered)
- Email threads: 4 read, 2 gaps found
- Specs stamped: 3
- Needs you: how EF_EXTRA_FIELD_1..6 map to configured fields
```

Always end with what you could not verify. That list is the point of the exercise.
