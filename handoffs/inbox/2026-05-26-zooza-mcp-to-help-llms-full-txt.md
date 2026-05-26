---
handoff_id: zooza-mcp-to-help-20260526-001
from: zooza-mcp
to: help
status: open
created: 2026-05-26
updated: 2026-05-26
related_specs: [ZMCP-20260526-008]
---

## Request

### What we need

A `static/llms-full.txt` file generated at deploy time and served at:
```
https://help.zooza.online/llms-full.txt
```

The file should contain a structured index of all published help articles — one entry per article with title, description, URL, and tags. **Not the full article content** — just the metadata needed to find the right article.

### Why we need it

The Zooza MCP server needs to answer operator questions like "how do I set up payment plans?" or "what is a make-up credit?" from Zooza's own sources instead of Claude's training data.

Today `help.zooza.online/llms.txt` exists but only lists categories (9 entries). When Claude fetches it, it gets category headings — not article titles. It has to then fetch the sitemap, parse XML, and still has no descriptions or tags.

With `llms-full.txt`, Claude fetches one file → gets the full article index → fetches the single most relevant article. Three HTTP calls instead of many, zero compiled data in the MCP.

`docs.zooza.online` already generates `llms-full.txt` via `scripts/build-llms-full.js`. We're asking for the same pattern on the help side, adapted for the help content structure.

### Constraints from our side

- **Not full article content** — descriptions only (~1–2 sentences per article). Full content would make the file too large for Claude to process efficiently.
- **Published articles only** — filter `status: "published"` from frontmatter.
- **Grouped by `product_area`** — makes it easier for Claude to navigate to the right section.
- **Static file, no auth** — must be publicly accessible without credentials.
- **Regenerated on every deploy** — same lifecycle as `llms.txt` today.

### How we imagine it — open to challenge

Based on the `api-docs/scripts/build-llms-full.js` pattern and the help frontmatter we've seen:

**Input:** `content/**/*.md` files where `status: "published"`

**Per article, from frontmatter:**
- `title` — article title
- `description` — 1-sentence summary (already exists in frontmatter)
- `slug` → URL: `https://help.zooza.online/{category-path}/{slug}/` (resolved from sitemap or export mapping)
- `tags[]` — existing tags array
- `product_area` — used for grouping

**Output format** (`static/llms-full.txt`):

```
# Zooza Help Centre — Article Index

> Full list of published help articles for Zooza studio management.
> Fetch an article URL to read its complete content.

---

## Payments

### Payment plans
Description: Payment templates define how clients pay for a programme — upfront, in instalments, or per session.
URL: https://help.zooza.online/payments/payment-plans/
Tags: payment, billing, subscription, programme

### GoCardless direct debit
Description: How to connect GoCardless for automatic direct debit collection from clients.
URL: https://help.zooza.online/payments/gocardless-direct-debit/
Tags: payment, gocardless, direct-debit, integration

---

## Bookings

### Creating a booking
...
```

**Script location:** `scripts/build-llms-full.js` (Node.js, same as api-docs)

**Build integration:** Add to the existing deploy/build pipeline — same step that currently generates `llms.txt`.

The URL derivation is the tricky part — you know best how the export pipeline maps slugs to final URLs. We've verified the sitemap is accurate, so fetching it once in the script and building a slug→URL map is one option. Another is using the export manifest if one exists.

---

## Discussion

<!-- Replies go here -->

---

## Decision Summary
<!-- Filled when status → agreed -->

---

## Resolution
<!-- Filled when status → resolved -->
