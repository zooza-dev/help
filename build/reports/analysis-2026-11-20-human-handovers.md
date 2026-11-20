# Why a human had to answer — 20 October to 19 November 2026

291 conversations. A human answered **164** of them.

The question was: what made a person necessary? The answer is not mostly the
knowledge base.

## 1. The biggest cause is the ticket channel, not the content

| Channel | Conversations | AI answered | Human had to answer |
|---|---|---|---|
| **Chat** | 215 | 156 (73%) | 101 (46%) |
| **Ticket** | 76 | **3 (4%)** | **63 (82%)** |

Every ticket gets an automatic reply that says:

> *"Your ticket has been received. Zooza Assistant will try to help you right
> away — and a member of our team will personally review it too."*

In 73 of 76 tickets the assistant never tried. `ai_agent` on those conversations
is empty — not a bad answer, no answer. The promise in the auto-reply is not kept.

Alongside it, every one of those tickets carries an internal note reading
`[Jira for Intercom Tickets] Jira issue creation failed. Check your app settings.`
Customers do not see it, but it means no ticket reached Jira either.

**This is the single highest-value fix in this report, and no amount of writing
will achieve it.** Turning the assistant on for tickets would put ~70 conversations
a month in front of it that currently go straight to a person.

## 2. Of the rest, most were never answerable from documentation

Taking the 164 and asking what the human actually did:

| What the human did | Count | Fixable by docs? |
|---|---|---|
| Looked at this account's data (asked for a registration number, a screenshot, an example) | 62 | No |
| Confirmed a defect and fixed it | 11 | No |
| Designed a feature with the customer | 7 | No |
| Customer opened with "connect me to a human" | 11 | Partly — see §4 |
| Explained how the product works | 19 | **Yes** |

Two thirds of the human workload is operational: data questions, bug reports and
product conversations with franchise owners. The queue is also concentrated —
ten people account for 90 of the 164 conversations, and 37 people appear once.

## 3. Where the knowledge base genuinely failed

55 conversations are chats where the assistant *did* answer and a human still had
to step in. That is the honest denominator for KB quality. Reading them, the
failures are of four kinds.

### a. Right answer, missing the one step that mattered

> *"Ten AI asistent odpovedá správne, ale nespomenul, že môžete kliknúť na ten
> toggle 'Zobraziť všetky plány'."* — 3 Nov

The Replace-plan list shows only the plans that class offers until you flip
**Show all plans**. Not in the KB, so not in the answer.

### b. Two things with similar names, documented as one

Four conversations in the month about instructor roles. The assistant answers with
the *user* roles (Main instructor / Instructor / External) when the question is
about the *session* roles (lektor / sekundárny / pomocný). The human's answer:
the session role is a label only — it changes nothing about what the person sees.
And financial visibility is one company-wide switch, not a per-instructor setting;
the assistant twice said otherwise and once invented a path for it.

### c. Behaviour that exists only in the code

Each of these cost a conversation, and none of it is written down anywhere:

- a payment plan created while a booking sits in **Late** is cancelled by the 01:00 job
- payment reminders have a **hard-coded 35-day limit** ("nikde ho nehovoríme")
- **reserve a seat for trial attendees** holds a place on *every* session until the
  trial resolves, and the trial form only looks at the next N sessions — together
  they produce "no trials available" on a class with free places (four
  conversations with one customer)
- a venue appears on the map only if it has sessions *and* its position was
  updated by hand after the address was typed
- changing a venue with "only on this class" leaves existing sessions on the old one
- the dashboard's *Remaining to pay* includes instalments that are not due yet
- the "bank connection needs reconnecting" notice fires at 60 days as a reminder,
  not because anything expired
- free places are shown as "last place" / words / a number depending on the count,
  unless a format is fixed per widget
- **Block weekend and holiday unsubscribes** also moves reminders to the last working day

### d. The tag family nobody has written down

Two conversations about reminder emails showing the wrong time or saying "tomorrow"
on a Friday. Both fixes are the same shape: the template used `COURSE_TIME` where it
needed `EVENT_TIME`, `EVENT_DATE_DAY`. This is the third month running that a
`COURSE_*` vs `EVENT_*` mix-up has reached support — `PAYMENT_AMOUNT` vs
`COURSE_PAYMENT` was last week's. The rule is simple and has never been stated:
**`COURSE_*` resolves against the class, `EVENT_*` against the session.**

## 4. Two bot behaviours that create work

- **It hands over on the word "human".** Eleven conversations open with a request
  for a person and the bot complies immediately. Martin's own reply to one:
  *"Odporúčame nezačínať chat s požiadavkou spojiť sa s človekom. Mali by ste
  častokrát odpoveď oveľa skôr."*
- **It answers parents as if they were administrators.** Two conversations from
  end customers looking for a language school were given admin instructions
  ("go to Activities → Programmes") before a human said "you are in the wrong place".

## 5. The dictionary layer

`sdd-workflow/translations/article-intents.yml` is what routes a question to an
article. Measured against the month's real questions:

- **123 of 242 articles** have "phrases" that are just the article's own headings.
- **1,588 of 1,892 phrases are English**; 304 carry Slovak/Czech diacritics. The
  customers in this window wrote in Slovak, Czech, Romanian, German and Polish.

The routing chunks are earning their keep — removing them changes which article wins
for 93 of 164 questions, mostly for the worse — so the fix is not to delete them but
to fill them with what people actually typed, in the language they typed it.
A month of Intercom is the obvious source.

## What to do, in order of return

1. **Make the assistant answer tickets** (or stop promising it will). ~70 conversations/month.
2. **Write the nine behaviours in §3c.** Each one has cost at least one conversation.
3. **Rewrite the instructor-roles articles** around session role ≠ user role, and state
   that financial visibility is company-wide.
4. **Add the `COURSE_*` vs `EVENT_*` rule** to the dynamic tags guide.
5. **Replace heading-derived intent phrases with mined customer phrasings**, SK/CZ first.
6. **Stop the instant handover** on the word "human"; give the bot a parent/admin check.
