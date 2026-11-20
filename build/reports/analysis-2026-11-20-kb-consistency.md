# Consistency and duplication across the knowledge base — 20 November 2026

265 published articles, 372,000 words, 2,242 sections. Measured three ways:
near-verbatim copies (shingle overlap), same-topic-different-words (TF-IDF cosine),
and navigation cues checked against the app's generated menu map.

## 1. Verbatim duplication is rare. Topical duplication is not.

Only 7 section pairs are near-copies. But 48 pairs of articles and 210 pairs of
sections cover the same ground in different words. The pattern behind most of them
is structural: **an FAQ and a guide written separately about one feature**, then
maintained separately.

The worst cases, highest first:

| Pair | Overlap | Verdict |
|---|---|---|
| `guides/edit-payment-on-booking` ↔ `guides/payment-tile-on-booking` | 0.73 | **Retired** — the second was a strict subset, same screens, older wording |
| `faq/booking-faq` ↔ `faq/registration-and-booking-faq` | 0.42, nine identical questions | **De-duplicated** — see §2 |
| `faq/slack-faq` ↔ `setup/slack-integration` | 0.73 | Legitimate pair, but they did not link to each other |
| `faq/programmes` ↔ `faq/programmes-timetables-sessions-faq` | 0.77 on shared questions | **Still open** — two FAQs about programmes, 1,900 and 5,300 words |
| `setup/oblio` ↔ `smartbill` ↔ `szamlazz` ↔ `fakturoid` | 0.38–0.53 | Deliberately parallel, but drifting in structure |
| `guides/individual-sessions-climbing-wall` ↔ `individual-sessions-with-free-session` ↔ `multi-day-event-with-product-offer` | 0.39–0.49 | Recipe boilerplate; worth one shared "what happens at booking" block |

## 2. The duplication was hiding a contradiction

The two booking FAQs both answered *"Can I manually create a booking on behalf of a
client?"*:

- `booking-faq`: trial bookings **can** be created by an admin — **Convert to trial**
- `registration-and-booking-faq`: trial bookings **cannot** be created manually

Checked against the app (`registration_detail.js`, `lib/str_en3.js`): the first is
right. A **Convert to trial** card appears on a booking's status screen when the
class supports trials and the booking is not already one, and it warns
*"This action is irreversible. Once converted to a trial, the booking cannot be
changed back to a regular registration."*

The same pair also disagreed about moving a client between classes — one described
the **Transfer** wizard, the other a dropdown that no longer exists.

Nine duplicated questions were removed from `registration-and-booking-faq`, leaving
the current answers in `booking-faq` and a pointer between them. Both descriptions
were identical auto-extracted text; both are now written.

## 3. Navigation cues: 1,156 of them, and they did not agree

101 destinations were reached by more than one stated route. Checked against
`build/app-map/app-map.yml`, 68 cues named a real screen by a route that does not exist.

Fixed in this pass (126 occurrences across 63 articles):

- `Settings → Billing → Invoice Profiles`, `Settings → Invoice profiles`,
  `Payments → Invoice profiles` → **Settings → Billing & Payments → Invoice profiles**
- `Settings → Integrations` → **Team & Settings → Integrations** (37 occurrences)
- `Settings → Billing periods` → **Settings → Billing & Payments → Billing periods**
- `Sales & Payments → Payments → Direct Debit` → **Sales & Payments → Transactions → Direct debit**
- `Settings → Programmes` → **Activities → Programmes**
- `Communication → WhatsApp → Templates` → **Communication → Templates**
- casing against the app's own string table: *Online booking*, *Price and payment*,
  *Additional fields*, *Invoice profiles*, *Payment reminder settings*

Still open: whether the canonical prefix is `Settings → …` or `Team & Settings → Settings → …`.
The KB uses both; the app map says the former. Nine articles say the latter.

## 4. What this costs

A question that two articles answer differently gives the assistant two sources and
no way to choose. The contradiction above was live for at least seven months, in the
two most-cited booking articles in the knowledge base.

## Recommended next

1. Merge the two programme FAQs, or give them disjoint scopes.
2. Give the four invoicing-integration setup pages one shared skeleton.
3. Run `scripts/analysis/kb_topics.py` and `kb_contradictions.py` as part of the
   weekly intake, so a new duplicate is caught the week it is written.
