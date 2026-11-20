---
handoff_id: zooza-web-to-help-20261120-001
from: zooza-web
to: help
status: open
created: 2026-11-20
updated: 2026-11-20
related_specs: [WEB-20261120-001]
---

## Request

### What we need

Zooza is narrowing its strategy toward being the backend that clients build their own front ends on
— often by vibe-coding with Claude, Cursor or Lovable, or by handing the job to an agency. The admin
app is getting a **Developers** section with **self-serve API keys**, and it reaches production around
the weekend of 2026-11-21/22.

After this hand-off, an **owner who is not a developer** should be able to answer these from
help.zooza.online alone:

1. **Do I need an API key at all?** Widgets don't need one; your own app, dashboard or integration
   does. (The existing "You do not need a REST API key for this" section already does half of this
   well.)
2. **How do I create one?** Where it lives in the admin (Developers → API keys), what the access
   choices mean (Read only / Read and write), what the rate limit choices mean (Starter / Standard /
   Partner), and that the client secret is shown only once.
3. **How do I hand it to a developer, an agency or an AI tool safely?** The secret goes into a
   server-side environment variable or a password manager — never into an email, a chat, or code that
   runs in the browser.
4. **How do I rotate or revoke it**, and what changes when (revoking is immediate; access and limit
   changes apply to new tokens, so within an hour).
5. **Why did it stop working?** Tokens are issued in an owner's name, so if that person stops being
   an owner the tokens stop working. Plus the four token errors the app lists (`400 invalid_request`,
   `401 invalid_client`, `429 too_many_requests`, `503 temporarily_unavailable`) in plain words.

Code, endpoints and the token request itself stay in docs.zooza.online; help links there.

### Why we need it

- zooza.online is being rewritten to send operators who want to "build their own" toward self-serve
  keys (spec `WEB-20261120-001`). The website answers "can I, is it safe", the docs answer "how in
  code", and help is the place that answers "where do I click in the admin". Without the help
  articles, the operator path has a gap in the middle.
- **What we observed in help on 2026-11-20:**
  - `content/setup/deploying-zooza-on-website.md` line 32: "it is available on every plan, but it is
    not switched on by default — ask support and they will enable it and issue the key and client
    secret". This is wrong from launch day.
  - Line 30 of the same article: "A REST API key — a different thing, requested separately."
  - `content/setup/integrations-hub.md` ("REST API & Custom Integrations") links straight to the docs
    with no admin step in between.
- The most likely mistake of a vibe-coded front end is a secret pasted into browser code. A help
  article that owners read before they hand the key over is the cheapest place to prevent it.

### Constraints from our side

- **Facts come from the app's own copy:** `~/app`, branch `feature-developers-section`,
  `pages/developers/content/developers_api_keys.en.json` (and `developers.en.json`). Use the app's UI
  labels verbatim (Developers, API keys, Read only, Read and write, Starter, Standard, Partner).
- **Don't say which plan includes API keys or what levels cost.** Michal is still verifying whether a
  key requires a paid (Buyloop) subscription, and pricing of the levels is a later step. The "available
  on every plan" sentence should go rather than be restated.
- **Planned features are named only as "not available yet":** webhooks, a test mode with sample data,
  setup/import tools, an SDK. "This company only" is the only company scope today; "all companies
  where the owner has access" shows as not available yet in the key dialog.
- **Keep the existing widget-key guidance** — it is the most common wrong turn and the article handles
  it well.

### How we imagine it — open to challenge

- One new article in `setup/` ("Create and manage API keys"), plus an edit of
  `deploying-zooza-on-website.md` lines 30–32 to point to it, and a line in `integrations-hub.md`.
- A short "Handing a key to your developer or AI tool" section, possibly reusable as a `_shared`
  snippet, since the same advice belongs next to the MCP connector article.
- Screenshots of the key dialog once it is in production (the help repo knows its own screenshot
  process best).
- Heads-up only, not part of this request: the same app release moves the MCP connector and Widgets
  under Developers and rebuilds Publish, so articles that describe those paths may need the app's own
  hand-off.

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
| zooza-web | | |
| help | | |

---

## Resolution
<!-- Filled in when status moves to "resolved" -->
**Resolved on:**
**Outcome:**
**Related specs/PRs:**
