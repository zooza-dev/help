# Blog brief — the first week is everything

**Proposed for:** November / December 2026
**Audience:** owners of children's activity businesses — swim schools, dance, music, languages, sports clubs, franchise networks. Must be useful to someone who has never heard of Zooza.
**Status:** brief, not drafted.
**Working title:** *Six in ten payments arrive in the first week. Most schools start chasing in the third.*

---

## The one claim

**Parents do not need more payment reminders. They need an earlier one — and half of what
looks like debt is not debt at all, it is a message that never arrived.**

Everything else in the piece serves that sentence.

## The structure the article needs

An unpaid fee is **two different problems**. Almost every provider sends the same reminders
to both, and separating them is the most useful thing this article can do for a reader.

| | **The instrument failed** | **Nobody paid** |
|---|---|---|
| How it happens | Card expired, insufficient funds, direct debit mandate lapsed | A bank transfer that was never made |
| What the parent intended | To pay. They believe they have | Undecided, or forgot |
| Does the parent know? | **No** | **Yes** |
| Can it retry itself | Yes | No |
| What the industry data covers | This, directly | Nothing published |
| What actually fixes it | Tell them what broke, make the fix one tap | A consequence they can predict |

The asymmetry in the "Does the parent know?" row is the insight the piece is built on.

**Column one is a notification problem wearing the costume of a collection problem.** The
parent thinks they have paid. Every day spent chasing them as a debtor is a day they spend
confused, and the repair is thirty seconds of their time if anybody tells them. This is
where reminders genuinely recover money and where speed decides the outcome.

**Column two is a decision.** The parent knows. A fourth email tells them nothing they do
not already know, which is exactly why the recovery curve flattens — and why the answer
here is not a better message.

## The evidence

### Sequence position barely matters

Churnkey's own dataset: 6 million failed payments across $3 billion of subscription revenue.

| Email | Share of payments recovered |
|---|---|
| 1st | 2.8% (opened by 55.8%) |
| 2nd | 1.9% |
| 3rd | 1.7% |
| 4th | 1.5% |
| 5th | 1.5% |

**Do not claim the third email is useless** — 1.7% against the fourth's 1.5% is barely a
decline, and every additional email still recovers something. The honest reading is not
"send fewer", it is "stop believing the next one will fix it".

### Timing matters enormously

| When | Share of all recoveries |
|---|---|
| **First 7 days** | **61.2%** |
| Week 2 | 11.7% |
| Week 3 | 8.7% |
| Week 4 | 6.4% |
| Week 5 and later | 12.1% |

Six in ten payments that will ever arrive, arrive in the first week. A provider deciding
whether to add a third email in week four is optimising the 6% and ignoring the 61%.

### Where the evidence stops

The figures above are **failed card and direct debit payments in software subscriptions**.
They transfer to column one without translation — an expired card in a swim school behaves
like an expired card in a software subscription, and a large share of Zooza providers run
on Stripe cards or GoCardless direct debit.

For **column two**, in children's activities, nothing has been published. Reason it out in
the article and say plainly that it is reasoning. Drawing that line in the right place is
what makes the piece credible; blurring it is what would sink it.

## Why Zooza is the one to write this

One week of customer conversations, 30 October to 5 November 2026, all 64 read in full:

| Theme | Conversations |
|---|---|
| **Money** — fees, instalments, reminders, pairing, refunds | **24** |
| Website and widgets | 4 |
| Team and roles | 4 |
| Classes and sessions | 4 |
| Clients, programmes, make-ups, communication | 12 |
| Everything else | 16 |

Within those 24, by payment method:

| | Conversations |
|---|---|
| **Instrument-agnostic** — when an instalment is created, when it is due, reminders, grace | **18** |
| Bank transfer — pairing, variable symbol, email parser, bank reconnection | 4 |
| Card (Stripe) | 1 |
| Direct debit (GoCardless) | 1 |

Three observations from this that no single business could make:

- **Not one of the 24 asked about timing.** Every one was about how much, how many, or
  where to click. Providers in several countries all reach for the same wrong lever.
- **Most money questions are not about the payment method at all** — they are about *when*
  money is asked for, which is the article's subject. The bank-transfer questions were
  about getting money *recognised*, not getting it *paid*: a different problem.
- **A hidden ceiling existed for a long time and nobody reported it.** Payment reminders
  set further out than roughly 35 days silently never sent. Not one provider filed it as a
  bug — they assumed they had configured it wrong. That says something real about how
  little attention this part of a business gets.

Patterns only. No named businesses, no figures that could identify an account.

## Outline

1. **The instinct everybody has.** Fees outstanding, so add another reminder. Two real
   requests from one week, anonymised.
2. **Split the pile in two.** The table above. Ask the reader to go and count their own —
   most never have, and the ratio decides which half of the article is theirs.
3. **The half that is already solved.** Cards and direct debits. The parent does not know
   anything is wrong. The 61%-in-seven-days finding, applied without caveat.
4. **What the fourth reminder is worth.** 1.7% then 1.5%. Not an argument for sending
   fewer; an argument against waiting for the next one to work.
5. **The half nobody has data on.** The missing transfer. The parent already knows, so a
   message adds nothing. Reason it out, flagged as reasoning.
6. **The uncomfortable question.** If an instructor can see an unpaid booking, should the
   lesson be taught? Most providers have never decided. We have no number for this — say so.
7. **What to change on Monday**, per half:
   - *Failed instrument:* catch it the day it fails, say what broke, make the fix one tap.
   - *Never paid:* ask early, make the first ask a link that pays rather than a document to
     read, and decide in advance what happens if nobody does — then let it happen on its own.
8. **One paragraph on doing this in Zooza.** At the end, once, skippable. Not before.

## Hooks to test

- *Six in ten payments arrive in the first week. Most schools start chasing in the third.*
- *Half your unpaid fees are not unpaid. The parent thinks they already paid you.*
- *The third reminder is not your problem. The first one is — it went out too late.*
- *You cannot email somebody into paying. You can make it easy while they still mean to.*

## The chart this piece is missing

The strongest available claim is the founder's own observation: **providers running the
same software carry very different levels of debt, so the difference is in how they
communicate, not in the system.** If it can be shown, it is the chart the article is built
around. It is currently unverified.

It cannot be answered from the analytics store, which holds Zooza's own receivables against
its customers rather than what parents owe providers. Two routes:

1. **Product database.** The question: *for each company, the share of course fees still
   unpaid 30 days after their due date, over one term, for companies above a minimum number
   of bookings — split by payment method.* A distribution, not an average: the point is the
   spread, and whether best and worst differ by a factor of two or of twenty. Anonymous and
   aggregate.

   The split by method is what makes it worth running. If card and direct-debit providers
   carry visibly less debt, the article gains a recommendation with a number behind it. If
   they carry the same, the method is not the variable and the communication claim gets much
   stronger — the more surprising result and the better piece. **Either answer is
   publishable**, which is the mark of a question worth asking.
2. **Ask five providers.** Slower, better content: real names, real numbers, real policies.
   If one of them has near-zero debt, their policy is the article.

Neither blocks drafting. The piece stands on the timing data; the chart would make it
quotable.

## Reach beyond our customers

"How to get parents to pay on time", "chasing unpaid class fees", "payment reminder best
practice" are searches that currently return only software adverts. A piece that tells
owners to chase *earlier* rather than *more*, and shows its numbers, earns the right to
mention Zooza once at the end.

## Follow-ups if it lands

- **Discounts that pay for children who do not exist.** A sibling discount could be earned
  with an unpaid second booking, or by typing "Martinko" instead of "Martin". Both now
  closed. An invitation to audit your own discount rules, with twins and the free-newborn
  case as worked examples.
- **Trials.** Still unwritten from the make-up brief: most providers do not know their trial
  conversion rate, and the trial is where the money is won or lost.

---

## Sources

- Churnkey, *12 tactics to reduce involuntary churn* — https://churnkey.co/guides/reduce-involuntary-churn
- Churnkey, *Involuntary churn benchmarks* — https://churnkey.co/blog/involuntary-churn-benchmarks/

Both are Churnkey's own failed-payment data (6M payments, $3B revenue) from software
subscriptions. Verify the figures against the live pages before publishing; they are
updated periodically.

Figures circulating from savemrr.co were reviewed and **deliberately excluded**: that page
blends its own data with third-party benchmarks, and its recovery rates contradict
Churnkey's because they measure a different denominator. Do not mix the two sets.

*Customer evidence: Intercom conversations 2026-10-30 to 2026-11-05, all 64 read in full.
Per-conversation notes with verdicts in `build/intake/notes-2026-11-05.json`. Review board:
https://claude.ai/code/artifact/fe298463-8883-4968-b30b-c891472900db*
