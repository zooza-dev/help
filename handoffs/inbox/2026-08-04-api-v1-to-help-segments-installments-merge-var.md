---
handoff_id: api-v1-to-help-20260804-001
from: api-v1
to: help
status: open
created: 2026-08-04
updated: 2026-08-04
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
<!-- Filled in when status moves to "agreed" — distilled from the discussion above -->

**What will be built:**

**What will NOT be built (and why):**

**Constraints agreed:**

**Each party's responsibilities:**

| Project | Responsibility | Target |
|---------|---------------|--------|
| api-v1  |               |        |
| help    |               |        |

---

## Resolution
<!-- Filled in when status moves to "resolved" -->
**Resolved on:**
**Outcome:**
**Related specs/PRs:**
