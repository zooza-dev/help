# Intercom intake — 2026-06-24 → 2026-08-06 (bot-only conversations)

**Run date:** 2026-08-07
**Scope:** 150 of 281 conversations ended without any human reply. All 150 were read.

## How these were triaged

Silence is not proof the bot was right. Instead of judging each answer by hand, conversations were bucketed on objective signals carried in Intercom's `ai_agent` field:

| Bucket | Signal | Count |
|---|---|---|
| A — hard signal | `routed_to_team`, `abandoned`, or a low CSAT rating | 5 |
| B — no KB source | Fin answered citing zero content sources | 22 |
| C — re-ask | the client asked ≥2 more times after the bot replied | 73 |
| D — assumed resolution with KB sources | the client simply went quiet | 47 |
| E — confirmed resolution | the client explicitly confirmed | 3 |

`resolution_state` across the bot-only set: `assumed_resolution` 110, `confirmed_resolution` 13, `routed_to_team` 3, `abandoned` 2, none 22. **Only 13 of 150 were actually confirmed by the client.**

Bucket B turned out to be almost entirely noise — spam email and ticket acknowledgements with no bot answer at all. The signal is concentrated in **C** (re-asks), which is where every failure below was found.

---

## 1. Repeated bot errors — same wrong answer to several different customers

These matter most: each one is a KB retrieval failure that will keep recurring until the KB is fixed.

### 1.1 "Zooza does not pair bank payments automatically" — 3 occurrences 🔴

| Conv | Date | Outcome |
|---|---|---|
| 215475256660170 | 07-28 | **abandoned** after 14 re-asks |
| 215475244142067 | 07-27 | client went to the technicians directly |
| 215475272108493 | 07-29 | client left |

The bot repeatedly stated that automatic pairing of incoming bank payments "is not described as a supported feature" and that setting the notification email in internet banking "probably has no effect". This is flatly wrong — it is a core feature, and a human resolved exactly this problem in the same week (conv 215475244228883). In every one of these three the bot cited only `Zooza PRO — Zooza` and `Ceník — Zooza`, i.e. marketing pages, never `Payment pairing`. **The KB article exists but is not being retrieved.**

Also unanswered in this thread: what file format `#payments/inbound/import` accepts.

### 1.2 "Zooza has no holiday calendar" — 2 occurrences 🔴

`215475259017286` (07-28) — the bot told the customer that skipping public and school holidays when generating sessions does not exist and must be done by hand. It does exist; it is just only in the **Advanced** session-planning tab, which is exactly what the customer could not find. Same root cause as H33 in the human review, and as `215475092076640` where a customer said the option used to be on the group and had moved.

### 1.3 Slovak answered in Czech / English — 5 occurrences ⚠️

`215475092076640`, `215475278399746`, `215475147999835`, `215474929038865`, `215475092110372`. Customers asked up to four times in a row for Slovak and kept getting Czech or English. Martin confirmed there is no way to force it. Not a KB fix, but it is the single most common source of visible frustration.

### 1.4 "You cannot force clients to re-accept updated terms" — 2 occurrences

`215475186224218` (bot-only) and `215475186259558` (human corrected it). The versioning checkbox shipped on 22 July; the KB has not caught up.

### 1.5 Delete vs cancel a registration — contradictory

`215475172672105` — "delete = permanent removal, the data is no longer visible". Wrong: it is a soft delete, recoverable from Trash for 30 days. The bot answered this correctly in `215475170287159` two weeks earlier. Source cited was the pricing page.

---

## 2. Navigation dead ends — the bot knew the answer but could not locate the screen

These are pure KB problems: the *what* is documented, the *where* is not.

| Conv | Re-asks | Topic | Where it actually is |
|---|---|---|---|
| 215475214097506 | **35** | The **extra capacity number** for trials | The bot cycled through Programme Settings → Attendance tile → Class detail → Classes list for ~15 turns. It is at **Team & Settings → Make-up sessions → "Additional slots in classes"** (global), overridable per class. The Trial tile only chooses *whether* to use it |
| 215474912699689 | 13 | "There are no Programmes in my menu" | The customer's UI says **Kurzy**; the bot kept saying Programmes. Either a terminology mismatch or an instructor role. The bot never checked the role even though it knows that rule |
| 215474868548420 | 10 | Make-up settings | Bounced between Programme → Settings → Make-up session and the global `#settings/replacements`, using English labels against a Slovak UI (NÁHRADNÉ HODINY, EXPIRÁCIA KREDITOV, POČET MIEST NAVYŠE…) |
| 215475163179973 | 6 | Programme colour will not save | The **Save button only appears after clicking Edit on the tile**. Separately, a human found that the first colour selection is always ignored — pick another colour first |
| 215475291948047 | 19 | Removing an instructor | **Remove from company** is not on the Instructors page — it is in the Users list at Settings → Team |
| 215475170981576 | 5 | Move a booking to a later class | The bot told the customer to use **Transfer to network** (a different centre) when they wanted a different time in the same centre |

**Terminology is the common thread.** Programme / Kurz / Skupina / Class / Trieda confusion appears in at least four separate conversations (`215474912699689`, `215475083962483`, `215475200623649`, `215475207979948`). Each time the customer asks some version of "programmes — is that skupiny or kurzy?".

---

## 3. Genuinely missing content the bot could not answer at all

| Conv | Question | Note |
|---|---|---|
| 215475284909115 | Bulk-enable online registration on 200 classes | Partly answerable: bulk within a programme yes (Online Booking → Class Settings → Choose all), across all programmes no |
| 215475332530770, 215475171331314 | Turn off the new-registration popup and its sound | Asked twice in the period; unanswered both times, including by a human |
| 215475183233140 | Change the invoice line description | Answered by a human elsewhere (Item description + dynamic tags) |
| 215475300344052 | Why are Saturday sessions shown in red? | Calendar colour coding is undocumented |
| 215475247901010 | Switch the interface to Polish | Bot had no steps at all — third occurrence of the language-switching gap |
| 215475214956392 | "Group is full" notification | The customer insisted the Notification Centre has this type; the bot denied it twice. Notification types are not documented |
| 215475125025634 | Every session appears twice | Never answered |
| 215475004782223 | Outstanding amount is 0 on a new registration | 14 re-asks, ended with "you're answering nonsense". Never solved |

---

## 4. Correct answers worth capturing (bot got it right, KB should say it too)

- **Trial bookings store only the date, not the time** — if several trial times run on the same day you cannot tell from the booking which one was chosen; you must open the session in the Calendar (`215475291948047`).
- **After booking a trial the parent's dashboard shows every upcoming session in the programme**, not just theirs. "Sessions shown in form" only controls the booking form. No setting hides this (`215475214097506`).
- **Trial capacity = Extra capacity** stops trials taking paid spots; with *Current available capacity* several people can book the same trial slot.
- **Pro-rata for mid-year joiners:** Term payment + Unit price, then Advanced settings → **Aliquot price calculation = Automatically calculated**. One-off payment never pro-rates (`215475207979948`).
- **A class price of 0 is treated as "not set"** and falls back to the programme price. For a free class, set the whole programme to 0 or use a separate programme (`215475200623649`).
- **Payment template must have "Visible to clients" on**, or the payment step renders blank.
- **Outstanding amount is fixed at the moment the registration is created** and never recalculates when prices change.
- **Two invoice engines:** default Faktury Online (no template settings, footer not editable) vs Zooza Invoice beta (Settings → Billing → Invoice Profile → Invoice Engine → Template). Receipts are **Dynamic documents**, generated at booking level only (`215474913416433`).
- **HTML links in consents** go in the *Name of the consent in the booking form* field; `*|AGREEMENT_URL|*` opens the internal consent page. Font size is widget CSS only (`215475232739392` — confirmed working by the customer).
- **Turning off client emails** is spread across four places: Automations (booking confirmations), Online Booking → Communication (session reminders), Price and Payment → Payment Reminder Settings, and Trial → follow-ups (`215475271350809`).
- **Cancellation limits** are global: Settings → Programmes → "Set a limit for cancelling a scheduled session", fixed or relative, plus *Instructions for the client*.
- **Session payment adjustments** are the right tool when a session did not run — Calendar → session → Bulk edit → *Adjust session payments* — not a refund.
- **Currency:** the account currency is set by country and needs a support request; extra currencies are per programme (Price and Payment → Additional currencies).
- **Booking notifications:** Settings → Notifications, one email address per entry.
- **Email signature:** Communication → Templates → Email Signatures → Preset signature (choose blank to stop the duplicate logo).
- **Class order inside a programme cannot be changed** on the booking page; only programme-level Priority (0–1000).
- **Public and school holidays are synced and not editable** — wrong dates need a support request. Editing a custom holiday does not change already-created sessions, and bulk-moving sessions does not re-apply skip rules.

---

## 5. What to fix first

1. **Payment pairing retrieval** — three abandonments in six weeks. The article exists; make it findable (title, intents, keywords).
2. **Holiday skipping** — say plainly that the option lives only in Advanced session planning, and that it cannot be applied retroactively.
3. **Capacity vs extra capacity vs trial capacity** — no article exists; 35 re-asks in a single conversation.
4. **A "where is it" article for the settings that move** — extra capacity, Remove from company, Save-appears-after-Edit, Documents under Products & Services.
5. **Terminology** — one short article mapping Programme = Kurz, Class = Skupina, Session = Termín, in the words customers actually type.
