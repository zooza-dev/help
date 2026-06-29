---
handoff_id: api-v1-to-help-20260629-001
from: api-v1
to: help
status: open
created: 2026-06-29
updated: 2026-06-29
related_specs: [API-20260516-001]
related_handoffs: []
tags: [reviews, google-reviews, reputation, documentation, ZOOZA-4670]
---

## Request

### What we need

A user-facing help article (or short series) on help.zooza.online that lets a studio operator set up and understand the new **Reviews module** — Google review collection + read-back — entirely on their own, without contacting support.

After reading the article(s), an operator should be able to:

1. **Understand what the Reviews module is** and how it differs from the existing **NPS feedback** — Reviews = *public* reputation on Google; NPS = *private* improvement feedback. The two do not replace each other; a client who already gave NPS feedback is not asked for a public review.
2. **Connect their company to Google** (one Google account per company, via OAuth) and read what "connected as…", "needs reconnect" and "disconnected" mean.
3. **Link each physical place to its Google location** — confirm a suggested match, pick a different Google location manually, or leave a place unlinked (a place with no Google link simply never asks for reviews).
4. **Submit a brand-new place to Google** when no matching Google location exists yet, then understand that **verification happens inside Google Business Profile (postcard / phone / video), not in Zooza** — Zooza only submits the place and lets them press "Refresh status" once Google has verified it. Includes understanding the **opening-hours placeholder warning** (Zooza prefills Mon–Fri 09:00–17:00 because it does not track opening hours; the operator must fix this in Google after verification).
5. **Choose which courses ask for reviews, and when** — three independent moments per course: *after registration* (shown in the registration widget thank-you step), *after the first attended session*, and *after the class has ended* — plus a "don't ask anyone who registered before this date" backstop.
6. **Understand when a client will and won't be asked** — the 12-month per-client cooldown, and the suppression rules (already gave NPS feedback, marketing-unsubscribed, already left a matched Google review).
7. **Find the reviews that come back** — where matched reviews appear on a customer's profile, and where the company-wide Reviews list lives (matched + unmatched, filterable by stars/time), including the one-click manual confirmation for reviews that couldn't be auto-matched.

### Why we need it

The Reviews module (spec **API-20260516-001**, ZOOZA-4670) is implemented in api-v1 and the admin surfaces are being built in the app, but there is **no end-user documentation** yet. Several parts of the flow are non-obvious and will generate support load without an article:

- The Google connect + per-place linking + place-submission + verification flow has steps that happen **outside Zooza** (on Google's side). Operators need to know what Zooza does and does not do, or they will report "verification is broken" when it is simply pending on Google.
- The **opening-hours placeholder** is a deliberate workaround that *looks* like a bug unless explained.
- The **review didn't get sent / didn't get matched** cases (cooldown, NPS suppression, fuzzy name match) need a plain-language explanation so operators don't open tickets for expected behaviour.

This handoff also drives the spec's documentation lifecycle: once the article ships, api-v1 sets `docs_version` / `docs_communicated` on API-20260516-001.

### Constraints from our side

- **Reviews and NPS are separate, parallel features.** Please do not describe Reviews as a replacement for, or evolution of, the existing NPS feedback. The existing NPS articles stay valid and unchanged. In the app nav, **Feedback** splits into **NPS** (existing) and **Reviews** (new) — keep that framing.
- **Google is the only provider in Phase 1.** Do not document Trustpilot, Facebook, ProvenExpert or any "star-gating" pre-question — none of that ships. The module is Google-only for now (architecture allows more later, but that's not user-facing yet).
- **Verification is Google's, not Zooza's.** Be explicit that the postcard / phone / video verification is completed by the operator inside their Google Business Profile; Zooza only submits the location and polls status.
- **No reply-to-review, no sentiment/themes, no SMS** in Phase 1 — please don't document features that aren't there.
- Final **screen names / button labels** should match what the app ships (see related app handoff `2026-06-02-api-v1-to-app-reviews-module-admin-surfaces.md`); coordinate on exact wording once the app UI is final so the article's screenshots/labels are accurate.

### How we imagine it — open to challenge

You own the KB structure and house style; this is only a starting point.

A natural shape might be one parent article **"Collecting Google reviews"** with sections (or child articles) for:
1. *Reviews vs NPS — what's the difference* (short, sets expectations).
2. *Connect your studio to Google* (OAuth, connection status, reconnect/disconnect).
3. *Link your places to Google* (suggested matches, manual link, leaving unlinked).
4. *Don't have a Google listing yet? Submit your place* (submit → unverified → verify on Google → refresh status → opening-hours warning).
5. *Choose which courses ask for reviews, and when* (the three triggers + start-date backstop).
6. *When clients are (and aren't) asked* (12-month cooldown, NPS suppression, unsubscribe).
7. *Reading your reviews* (customer profile + company-wide Reviews list + confirming unmatched reviews).

Source of truth for behaviour is the spec **API-20260516-001** (`specs/implemented/2026-05-16-review-collection-engine.md` on branch `feature-reviews-module` in api-v1) — happy to walk through any section. We'll provide accurate field/label names once the app UI is finalised.

---

## Discussion

<!-- Each reply follows this format — append, never edit previous entries -->

### 2026-06-29 — api-v1

Opening this handoff. Reviews module is implemented in api-v1 and the admin UI is in progress in the app. We'd like a self-serve help article so the Google connect / place-linking / verification flow doesn't generate support tickets. Flagging the two most support-prone areas up front: (1) verification happening on Google's side, not in Zooza, and (2) the opening-hours placeholder. Open to your proposed article structure.

---

## Decision Summary
<!-- Filled in when status moves to "agreed" -->

**What will be built:**
**What will NOT be built (and why):**
**Constraints agreed:**
**Each party's responsibilities:**

| Project | Responsibility | Target |
|---------|---------------|--------|
| api-v1  | Provide accurate behaviour/labels from spec API-20260516-001; set docs_version/docs_communicated on publish | — |
| help    | Author + publish the user-facing article(s) | — |

---

## Resolution
<!-- Filled in when status moves to "resolved" -->
**Resolved on:**
**Outcome:**
**Related specs/PRs:**
