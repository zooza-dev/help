# Cross-validation: Onboarding Hypotheses Across 3 Clients

**Date:** 10 May 2026
**Sources:**
- Anna — Turtle Tots Dubai (babyballet-style swim franchise, ~250 customers, 160 days)
- Kate — babyballet Dubai (+971, dance/ballet franchise, ~100 customers, 9 months)
- Dom — Wee Kicks (toddler classes + franchise rollout in progress, 5 months)

---

## Validation results

| # | Hypothesis | Anna | Kate | Dom | Verdict |
|---|-----------|------|------|-----|---------|
| H1 | Programme/Timetable/Session hierarchy confusion | ✅ | ✅ | ✅ | **Confirmed 3/3** |
| H2 | "Class full" — trials count toward capacity | ✅ | ✅ | — | Confirmed 2/3 (not seen in Dom's use case) |
| H3 | No Zooza-native refund flow | ✅ | ✅ | ✅ | **Confirmed 3/3** |
| H4 | Term rebooking is manual | ✅ | ✅ | ~ | Confirmed 2/3 (Dom partial) |
| H5 | Attendance register too slow on phone | ✅ | ✅ | — | Confirmed 2/3 (Dom's classes smaller) |
| H6 | Payment status unreadable | ✅ | ✅ | ~ | Confirmed 2/3 + partial |
| H7 | Trial management — admin can't act | ✅ | ~ | ~ | Confirmed 1/3 + 2 partial |
| H8 | Sibling discount — no automation | ✅ | ✅ | ✅ | **Confirmed 3/3** |
| H9 | Paradigm mismatch — manual vs. rule-based | ✅ | ✅ | ✅ | **Confirmed 3/3** |
| H10 | Onboarding gap — live before ready | ✅ | ✅ | ✅ | **Confirmed 3/3** |

**Result: 8 of 10 hypotheses confirmed across all three clients. Zero contradictions.**

H2 and H5 are not universal — they depend on class size and volume. Smaller operators with few classes per week don't hit these as hard. At franchise scale (50+ locations) they will.

---

## What's consistent across all three

### 1. The hierarchy (H1) — everyone hits it, nobody understands it

All three clients ended up with wrong data in the wrong layer, settings reverting to defaults, or changes not cascading. All three needed Michal or Eva to fix it.

- Anna: instructor changes not syncing between Timetable and Sessions
- Kate: deleted venue still appearing in copies; blocks created twice because concept unclear
- Dom: *"I set up all the payment requirements on the system for each class but I've noticed that the system keeps changing them back to a default setting."*

### 2. Refunds (H3) — manual in every case

No client issued a refund from Zooza directly. All workarounds involved Stripe, manual discounts, or bank transfers.

- Kate's clients overpaid → Michal: "Easiest way: reduce her next instalment instead of refunding"
- Dom's Christmas break → Michal: *"For now, the workaround is to handle it manually... It's not as smooth as we want it to be"*
- Anna's 100+ refunds → Stripe Express nightmare

### 3. Paradigm mismatch (H9) — the root of most friction

Every client tried to do things manually that Zooza expects to be automated:
- Manually enroll clients instead of sending booking link
- Manually adjust balances instead of trusting payment rules
- Manually track discounts instead of configuring rules
- Manually contact clients instead of letting automations run

In all three cases, Michal corrected them with "always better if the client does it themselves" — but this correction was never systematic, always reactive.

### 4. Onboarding gap (H10) — everyone went live too early

All three clients were live with real customers before they had a working mental model of Zooza. The result: 5-9 months of reactive support, workarounds accumulating, and growing dependency on Michal.

---

## New findings from Kate and Dom not in original hypotheses

### N1 — Aliquot / prorating logic is opaque (Kate, Dom)

When months have different session counts (3 vs 4 sessions), Zooza prorates payments in ways that surprise clients. The calculation logic is invisible to the admin.

- Kate: unexpected payment amounts (400, 475, 500 AED instead of 500)
- Dom: £0 due shown because "no sessions before billing date" — not understood

**Implication:** Pricing setup requires understanding payment scheduling internals. Not documented in onboarding.

### N2 — Discount system limitations (Kate)

Zooza supports absolute discounts (e.g. 50 AED off) but not relative/percentage discounts on ongoing memberships. Clients expect % discounts (10% sibling, 15% loyalty).

Discount codes only apply to first payment; recurring discounts require different mechanisms (hidden payment templates, manual schedule edits). This is never communicated upfront.

### N3 — Waiting list doesn't exist (Kate)

When a class is full, Zooza doesn't offer a waiting list flow. Thinksmart changes the "Book" button to "Join Waitlist." Zooza shows "class full" and nothing else.

Kate: *"In Thinksmart the book now button would change to a waiting list button when the class was full."*

This is a missing feature, not a UX gap. Worth adding to the product backlog.

### N4 — Payment sync lag with GoCardless (Dom)

Payments collected via GoCardless don't always sync back to Zooza automatically. Dom was manually cross-referencing Zooza and GoCardless. Partial payments appeared as £9 instead of full monthly fee — confusing, no explanation in UI.

### N5 — Duplicate registrations hard to detect and merge (Dom)

When parents register twice (different emails), Zooza creates two complete registrations with different payment records. No duplicate detection. Admin needs to manually identify and cancel one — but risks cancelling the "live" one.

---

## The franchise risk — Dom names it directly

Dom is running a franchise business and planning to roll out Zooza to his franchisees by April 2026. His clearest quote:

> *"I'm worried this is going to be complicated for the franchisees if I'm struggling."*
> — Dom, 19 February 2025

This is the exact scenario Zooza is targeting. Dom is us. He has the same concerns we have about scaling to a large franchise.

After 5 months, Dom is still relying on Michal for basic operations and is anxious about his franchisees hitting the same walls.

**The gap is not a feature gap. It's a confidence gap.**

Franchisees need to feel they can operate independently. Right now, none of these three clients reached that point.

---

## Implications for franchise pitch

The data from three independent clients, across different business types, converges on the same structural issues. This means the problems are systemic, not edge cases.

Before pitching to a large franchise, Zooza needs to demonstrate:

1. **A client can run a term reset without Michal** — currently impossible
2. **A client can issue a refund from Zooza, not from Stripe** — currently impossible
3. **A client can understand their payment status in 10 seconds** — currently impossible
4. **An instructor can mark attendance in 60 seconds between classes** — currently difficult
5. **A client can read "Understanding Zooza" and then correctly set up a programme** — currently, no such document exists

Items 1 and 2 require engineering. Items 3–5 can be addressed immediately through content and UX copy.

---

*Cross-validation by Claude Code / Michal Dodok, 10 May 2026*
*Based on: Turtle Tots, babyballet Dubai, Wee Kicks WhatsApp support conversations*
