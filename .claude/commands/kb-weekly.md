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

## Step 2 — Human answers first

Section 1 of the queue. **These are the gold standard** — a human agent already
worked out the correct answer, so the only question is whether it generalises.

For each one, decide:
- **Generalises** → belongs in the KB. Find where.
- **One client's specific situation** → skip it. Say which and why.

Do not skip this section in favour of the bot findings. It is where the value is.

## Step 3 — Bot-only, by risk

Section 2, already ranked. Read the buckets as evidence, not as scores:

| Bucket | What it means | Usual cause |
|---|---|---|
| `A_hard_signal` | Routed to team, abandoned, or rated poorly | The bot could not answer at all |
| `B_no_kb_source` | The bot cited nothing from the KB | No article exists |
| `C_reask` | Client asked 2+ times | An article exists but does not answer the question |

**A bot answer sourced only from marketing pages is the strongest predictor of a
wrong answer.** Watch for `Zooza PRO`, `Ceník`, and blog posts in the cited list.

Frame every finding as a **KB gap**, never as a "bot error". The bot repeats what
the KB tells it; three wrong answers in July traced back to wrong KB content.

## Step 4 — Client email

Section 4 lists the sender allowlist and a ready-made Gmail query. Run it with the
Gmail connector.

Keyword search does not work here — the mailbox is mostly `no-reply` booking
notifications. Search by sender.

These threads carry questions Intercom never sees, because they come from the
franchise owners rather than end customers.

## Step 5 — Write the changes

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

## Step 6 — Specs that shipped silently

Section 3 lists implemented specs with no `docs_communicated` date. For each one
the KB now covers, stamp the spec's frontmatter:

```yaml
docs_communicated: "YYYY-MM-DD"
```

If a spec needs something from another repo, create a handoff rather than guessing.

## Step 7 — Export and commit

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
