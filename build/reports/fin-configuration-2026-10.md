# Fin configuration — guidance, glossary and snippets

Written 2026-10-10 from the 26 Sep – 9 Oct intake. Everything below is grounded in a
conversation where Fin actually failed; nothing is speculative best practice.

---

## What changes now that it is Fin

Fin runs its own RAG pipeline — retrieval, hybrid search, reranking are all Intercom's,
not ours. So most of the engineering from the previous plan does not apply. What we
control is narrower and, usefully, cheaper:

| Lever | What it is | What we put in it |
|---|---|---|
| **Knowledge sources** | Which content Fin may answer from | Help centre yes; marketing and blog, see below |
| **Guidance** | Natural-language rules for how Fin behaves | The rules in this document |
| **AI Translations Glossary** | Terms that must translate consistently | `terminology.yml` canonical terms |
| **Snippets** | Non-public knowledge that improves coverage | `article-intents.yml` phrasings |

Two files we already maintain finally have a home. `terminology.yml` is a translations
glossary that has never been used as one. `article-intents.yml` is a list of the ways
customers phrase things, which is precisely what snippets are for — Intercom's own advice
is to "phrase customer queries multiple ways and provide the same answer".

Our own index still matters for the MCP connector and the embeddings job, so the URL fix
and the intent records stay. This is in addition, not instead.

---

## 1. Knowledge sources — the marketing problem

In the intake, the single strongest predictor of a wrong answer was Fin citing a marketing
page instead of the help centre. The clearest case: a Romanian customer asked why a newly
created class was not appearing on their site, asked **seventeen times** over fifteen days,
and the only source Fin ever cited was a marketing checklist article. There is no
troubleshooting path in that page, so there was never going to be an answer.

**Action:** review **Knowledge → Sources** and confirm what is connected. The help centre
and the developer docs are legitimate. Blog and marketing pages should not be answering
support questions — if they cannot be removed as a source, the guidance rule below
de-prioritises them.

I could not confirm from Intercom's documentation whether a subset of a synced site can be
excluded, so this needs checking in the UI rather than taking my word for it.

---

## 2. Guidance — paste this in

Written as natural-language rules, each one traceable to a real failure.

### Content priority

```
Always prefer the Zooza Help Centre (help.zooza.online) over any blog, marketing
or pricing page when answering a product question. Blog and marketing pages
describe what Zooza can do; they do not explain how to do it. If the only
content you can find for a question is a blog or marketing page, treat the
question as unanswered and offer to pass it to the team rather than answering
from that page.

The Zooza Developer Docs are the right source only for questions about the API,
authentication, webhooks or integrations written in code. Do not cite them to an
admin asking how to do something in the app.
```

### Never invent a setting

```
Do not tell a customer that a setting exists unless you have found it in the
Help Centre. If you cannot find how to do something, say that you cannot find it
and offer to pass the question to the team. A plausible-sounding set of steps
that does not exist costs the customer more time than saying you do not know.

Equally, do not state that something is impossible unless the Help Centre says so
explicitly. Features ship weekly. "I can't find a way to do this in the help
centre" is accurate; "Zooza cannot do this" often is not.
```

*Why:* on 29 September we told a customer an attendee could not be turned into a client.
The feature had shipped on 27 September. Both halves of this rule come from that one
exchange.

### Menu paths in the customer's language

```
When you give a navigation path, give the menu names in the language the
customer is using, because that is the language their Zooza interface is in. If
you are answering in Slovak, write the path in Slovak. Do not leave English menu
names inside a Slovak or Czech sentence — the customer will not find them on
screen.
```

*Why:* a customer was given "Settings → Team → Access" in the middle of a Slovak reply,
came back asking "Čo je to Settings, Teams, Access?", and had to be handed to a human who
gave her the same answer in Slovak.

### Ask which one they mean

```
Some Zooza words cover more than one thing. Before answering, if the question
could reasonably mean more than one of these, ask one short clarifying question:

- "trial" can mean the Trial feature on a programme, a one-off taster session
  sold separately, or a regular session someone has simply named "trial"
- "skúšobná hodina" / "zkušební hodina" / "ukážková hodina" have the same
  ambiguity
- "client" and "attendee" are different things: a client has a login, an
  attendee does not. A parent is usually the client, the child the attendee.
- "class" and "programme" are different levels. A programme contains classes;
  a class contains sessions.

Ask only when the answer would genuinely differ. Do not ask a clarifying
question you do not need.
```

### Escalate rather than guess

```
Pass the conversation to the team, without attempting an answer, when the
customer is asking about:

- money that has moved or failed to move on a specific booking or invoice
- anything involving their accountant, VAT, or a legal filing deadline
- a payment provider connection that has stopped working
- something they have already asked about twice in the same conversation

For these, a wrong answer is worse than a slow one.
```

*Why:* a customer with a VAT deadline waited eighteen days. Another with a disconnected
Stripe account, unable to send booking links, waited fourteen.

### Tone

```
Write plainly and briefly. Our customers run swimming schools, dance studios and
language schools; most are not technical and many are reading in their second
language. Short sentences. No marketing language. If a step has a precondition,
state the precondition first.
```

---

## 3. AI Translations Glossary

`sdd-workflow/translations/terminology.yml` holds 80 terms with confirmed translations in
SK, CZ, HU, DE, PL, RO, IT and FR, plus the deprecated variants we have agreed not to use.
That is exactly what the glossary field is for, and it is currently used by nothing.

Load the canonical term plus its translations for each term marked `public: true` (71 of
the 80). The highest-value ones, because they are where customers and we have historically
used different words:

| English | SK | Note |
|---|---|---|
| Programme | Kurz | not "program" |
| Class | Skupina | not "trieda" |
| Session | Termín | not "lekcia" or "hodina" |
| Booking | Registrácia | |
| Instructor | Lektor | never "tréner", "učiteľ" or "inštruktor" |
| Make-up session | Náhradná hodina | |
| Trial | Skúšobná hodina | |
| Client | Klient | has a login |
| Attendee | Účastník | has no login |

Getting "session" wrong is the expensive one: if Fin translates it as "hodina", every
answer about termíny reads as if it is about something else.

---

## 4. Snippets

Two kinds are worth creating.

**Phrasing snippets.** `article-intents.yml` now holds 35 articles' worth of the ways
customers actually ask, in six languages — including the exact strings behind this
fortnight's worst failures: *"unde pot schimba IBANUL"* (asked 15 times), *"prehodiť celú
skupinu do iného kurzu"* (16 times), *"this is embarrassing"*. A snippet per article
pairing those phrasings with a one-line answer and the article link is the designed use of
the feature.

**Known-issue snippets.** Short-lived, and the thing snippets are best at. Right now:

- SMS send but delivery confirmations never come back (ZOOZA-4934, under investigation)
- An unverified client email also blocks SMS to that client
- Emails to `@azet.sk` are accepted and never arrive — their end, affects all message types

These need an owner and a date, or they will outlive the bug and start causing the wrong
answer themselves.

---

## 5. How we will know it worked

We already have the test set and it costs nothing: every re-asked question in the weekly
intake is a labelled retrieval failure with a known correct answer. The current baseline,
from the 26 Sep – 9 Oct window:

| Question | Times asked | Article that already answered it |
|---|---|---|
| Move a class to another programme | 16 | programmes-timetables-sessions-faq |
| Where do I change the IBAN | 15 | invoice-profiles-and-bank-accounts |
| Download all invoices at once | 9 | the screen is archived, so nowhere |
| Can I message one client | 8 | sending-email-sms |
| What is "First class session" | 8 | nowhere |

Re-run those five questions through Fin after the glossary and guidance are in. If they
still miss, the problem is content, not configuration, and we will know which.

---

## Sources

Intercom documentation consulted 2026-10-10:
[The Fin AI Engine](https://www.intercom.com/help/en/articles/9929230-the-fin-ai-engine) ·
[Provide Fin with specific guidance](https://www.intercom.com/help/en/articles/10210126-provide-fin-ai-agent-with-specific-guidance) ·
[Fin Guidance best practices](https://www.intercom.com/help/en/articles/10560969-fin-guidance-best-practices) ·
[Multilingual support](https://www.intercom.com/help/en/articles/8322387-set-up-fin-ai-agent-s-multilingual-support) ·
[Content types and when to use them](https://www.intercom.com/help/en/articles/9357928-overview-of-content-types-and-when-to-use-them) ·
[Optimizing content for Fin](https://www.intercom.com/help/en/articles/7860255-optimizing-content-for-fin) ·
[Knowledge sources](https://www.intercom.com/help/en/articles/9440354-knowledge-sources-to-power-ai-agents-and-self-serve-support)
