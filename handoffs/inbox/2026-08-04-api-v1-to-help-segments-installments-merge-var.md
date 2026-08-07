---
handoff_id: api-v1-to-help-20260804-001
from: api-v1
to: help
status: resolved
created: 2026-08-04
updated: 2026-08-07
related_specs: [API-20260804-001]
---

## Request

### What we need

An entry for a new dynamic tag, `SEGMENTS_INSTALLMENTS`, in the dynamic tags guide (`content/guides/dynamic-tags.md`), where `ORDER_SUMMARY` is already documented.

The entry has to do more than name the tag. Operators must be able to answer two questions from the guide alone:

1. **How does it differ from `SEGMENTS_SUMMARY`?** They are close cousins and easy to confuse.
   - `SEGMENTS_SUMMARY` — blocks a customer is enrolled in, each with its **total price**.
   - `SEGMENTS_INSTALLMENTS` — the same blocks on **one line**, followed by what the customer **actually pays per period**: `Math, English — 97,50 €/month`.

2. **How exact is the number?** This is the part we specifically need stated, not glossed. The tag shows a **representative** recurring payment — the amount the customer pays in a normal period. It is deliberately one figure, not a schedule. Where an operator needs the exact, complete list of payments with their dates, **`ORDER_SUMMARY` is the tag that carries it**.

There are three situations where the single figure will not match every individual payment, and an operator who hits one of them should be able to find out why from the guide rather than from support:

- **Block-based payment plans**, where each block is its own payment and blocks differ in length — so the payments genuinely differ from each other. (Plans split into a fixed number of equal payments do not have this problem.)
- **A shortened final payment**, when the last period is partial.
- **Payments an admin has edited by hand** afterwards.

**The output is sometimes two-part.** When the first payment differs from the rest — a shortened first period, or a discount that applies only to the first payment — the tag renders `45,00 €, then 97,50 €/month`. An operator who expects a single figure will read the second number as a fault, so this needs a line too.

We also need the tag's behaviour on the two "nothing to show" cases documented, because both are intentional and will otherwise be reported as bugs:

- A customer with **no payment plan** — the tag renders **nothing at all**.
- A customer on a **pay-per-attendance** plan — the block names appear, but **no amount**. The amount genuinely does not exist until sessions have happened.

### Why we need it

Jira: ZOOZA-4881. Spec: API-20260804-001.

The accuracy caveat above is not a footnote — it is the condition under which we are shipping a single-figure tag at all. We decided against solving the edge cases in code, because doing so would mean rendering a full payment list, which `ORDER_SUMMARY` already does. That decision is only safe if the guide actually tells operators what the number means. If it does not, we will get "the tag shows the wrong amount" reports for behaviour that is working exactly as designed.

There is precedent for this going wrong: `SEGMENTS_SUMMARY` shipped under API-20260724-001 and, as far as we can see, never got a help entry — `ORDER_SUMMARY` is documented in the guide but `SEGMENTS_SUMMARY` is not. If that is right, this handoff is a good moment to cover both.

### Constraints from our side

- **The token string is `SEGMENTS_INSTALLMENTS`** — exact, uppercase, underscore. Documenting a variant spelling would send operators to a tag that silently does not expand.
- It produces **formatted output for email**, like `ORDER_SUMMARY` — not suited to plain-text channels.
- Please don't describe it as "the monthly payment". The period varies: it can be monthly, quarterly, half-yearly, yearly, per N sessions, or a fixed number of payments — the tag renders whichever applies.

### How we imagine it — open to challenge

Probably a row in the existing tag table plus, given the caveat, a short subsection near the block-related guidance. You own the guide's structure and the reading level, and you are better placed than us to decide how much nuance belongs in the table versus prose — the above is what must be *communicable*, not a layout instruction.

If the block/payment vocabulary here does not match what the guide already uses with customers, follow the guide's existing terminology rather than ours.

---

## Discussion

<!-- Each reply follows this format — append, never edit previous entries -->

---

## Decision Summary

<!-- NOT negotiated. help did not reply before this was closed; recorded from the request
     so the obligation is not lost. Reopen or supersede if help disagrees with any of it. -->

**What will be built:**

- A `SEGMENTS_INSTALLMENTS` entry in `content/guides/dynamic-tags.md`, covering how it differs from `SEGMENTS_SUMMARY` (total price vs what the client actually pays per period), that the figure is **representative** rather than an exact schedule, and that `ORDER_SUMMARY` carries the full payment list.
- Coverage of the two intentional "nothing to show" cases: **no payment plan** renders nothing at all; a **pay-per-attendance** plan renders the block names with no amount.
- Coverage of the two-part form: `45,00 €, then 97,50 €/month` when the first payment differs.
- Ideally an entry for `SEGMENTS_SUMMARY` too, which shipped under API-20260724-001 without one (`ORDER_SUMMARY` is documented in the guide; `SEGMENTS_SUMMARY` is not — verified directly).

**What will NOT be built (and why):**

- No documentation of per-block amounts — blocks have no individually attributable price under bundle pricing, which is why the tag renders one line rather than one row per block.

**Constraints agreed:**

- Token string is exactly `SEGMENTS_INSTALLMENTS`; a variant spelling sends operators to a tag that silently does not expand.
- Do not describe it as "the monthly payment" — the period can be monthly, quarterly, half-yearly, yearly, per N sessions, or a fixed number of instalments.
- Email-capable channels only, like `ORDER_SUMMARY`.
- Guide terminology wins over api-v1's wording where they differ.

**Each party's responsibilities:**

| Project | Responsibility | Target |
|---------|---------------|--------|
| api-v1  | Ship the tag and tell help exactly what it renders, including the imprecise cases | **Delivered** — API-20260804-001 |
| help    | `dynamic-tags.md` entry stating the figure is representative and pointing at `ORDER_SUMMARY` | **Delivered** — 2026-08-07 |

---

## Resolution
**Resolved on:** 2026-08-04

**Outcome:** Originally closed from the api-v1 side without a reply from help, with the documentation unwritten. The help side was completed on 2026-08-07 (see Discussion) and the request is now genuinely fulfilled.

**Delivered (api-v1):** the tag ships in API-20260804-001, verified end-to-end.

**Delivered (help), 2026-08-07:** the `dynamic-tags.md` entry. This matters more than a typical docs follow-up — spec API-20260804-001 decision 12 accepts three cases where the single figure is knowingly approximate (per-block variation on block-based plans, a shortened final payment, hand-edited payments) **on the explicit basis that the guide would tell operators the number is representative**. That basis now exists in the guide.

**Related specs/PRs:** API-20260804-001 (`specs/implemented/2026-08-04-segments-installments-merge-var.md`), JIRA ZOOZA-4881.

---

### 2026-08-07 — help

Written. `content/guides/dynamic-tags.md` now carries a **Block summary tags** section covering both tags, plus two rows in the main tag table.

What it says, against your Request:

- **Both tags documented.** `SEGMENTS_SUMMARY` had never been documented either (shipped under API-20260724-001), so it is in the same section — the two are only comprehensible side by side. `SEGMENTS_SUMMARY` = one line per block with its total price; `SEGMENTS_INSTALLMENTS` = blocks on one line plus what the client actually pays per period.
- **Representative, not a schedule.** Its own subheading, with all three imprecise cases named as intended behaviour: blocks of differing lengths, a shortened final payment, hand-edited payments. This is the basis decision 12 relies on. It points at `ORDER_SUMMARY` for the exact list.
- **Not "the monthly payment".** A subheading says the period may be monthly, quarterly, half-yearly, yearly, per N sessions, or a fixed number of instalments, and tells operators to let the tag say it rather than hard-coding "monthly" in template copy.
- **Two-part output** (`45,00 €, then 97,50 €/month`) documented.
- **Both silent cases** documented as deliberate: no payment plan renders nothing; pay-per-attendance shows block names without an amount.

Two things beyond your request:

1. Added an operator-facing warning that a client comparing the representative figure against a smaller final payment will report it as an error — the practical form the decision-12 risk takes on our side.
2. The guide previously ended its block-tag section promising *"a summary tag along the lines of `ORDER_SUMMARY` that lists only blocks"* as planned work. That promise was your tag, already shipped. Corrected to point at the new section — otherwise the guide would have described a delivered feature as forthcoming.

Terminology note, per your constraint that our wording wins: the guide calls these **blocks** (term segments) throughout, not segments. The tag tokens are of course verbatim.

**This inbox copy is updated. The outbox copy in `api-v1/handoffs/outbox/` needs the same two edits — the responsibilities row and this reply — which I have not made from here.**
