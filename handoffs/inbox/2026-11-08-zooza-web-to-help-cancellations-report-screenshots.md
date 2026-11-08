---
handoff_id: zooza-web-to-help-20261108-001
from: zooza-web
to: help
status: open
created: 2026-11-08
updated: 2026-11-08
related_specs: [WEB-20261108-001]
---

## Request

### What we need
Two pictures in the guide [Record why bookings get cancelled](https://help.zooza.online/bookings/cancellation-reasons/) (`content/guides/cancellation-reasons.md`), which the article already flags with `needs_screenshot_replacement: true`:

1. **The Cancellations report with data in it.** The current `cancellations-report.png` comes from an account with no cancellations: every rate is 0,00 %, "Where to look" says *Nothing stands out*, and *Sessions attended before cancelling* is empty. A reader cannot see what the report looks like when it actually works.
2. **The Cancellation reason picker in the cancel-booking dialog.** The guide describes it ("required", "There is no cancellation reason to choose from") but has no picture of it.

### Why we need it
zooza-web is publishing a blog post, *Why families leave your classes* (spec WEB-20261108-001, all 6 locales), whose product section links to this guide as the place to learn the feature. The guide is the right destination and its text is good. But a reader who clicks through from the blog lands on an empty report, which undersells the one picture that matters. The blog currently shows only the settings screenshot and leaves the report out because of this.

### Constraints from our side
- The blog hotlinks help images by their hashed URL (`/assets/images/cancellation-reasons-settings-<hash>.png`). If the **settings** screenshot is reshot, tell us the new URL so we can update the post. The report screenshot is not used on the blog yet.
- Demo or anonymised data only. No real client or child names.
- For the blog it is ideal if *Where to look* shows a hotspot, and *Sessions attended before cancelling* shows a visible pile at 0–2. That is the point the post makes. Only if the demo data supports it honestly.

### How we imagine it — open to challenge
Seed a demo account with a term of bookings and a spread of cancellations across categories, enough to clear the 15 bookings / 3 cancellations / 2× thresholds for one programme, then reshoot. You know the capture tooling and the demo accounts better than we do.

---

## Discussion

<!-- Each reply follows this format — append, never edit previous entries -->

---

## Decision Summary
<!-- Filled in when status moves to "agreed" -->

**What will be built:**
**What will NOT be built (and why):**
**Constraints agreed:**
**Each party's responsibilities:**

| Project | Responsibility | Target |
|---------|---------------|--------|
| zooza-web | Add the report screenshot to the blog post (all 6 locales) once it exists | after help delivers |
| help | Reshoot the report with data, add the cancel-dialog screenshot | — |

---

## Resolution
<!-- Filled in when status moves to "resolved" -->
**Resolved on:**
**Outcome:**
**Related specs/PRs:**
