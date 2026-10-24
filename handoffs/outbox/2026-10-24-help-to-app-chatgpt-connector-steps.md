---
handoff_id: help-to-app-20261024-001
from: help
to: app
status: open
created: 2026-10-24
updated: 2026-10-24
related_specs: []
related_handoffs: ["2026-09-04-zooza-web-to-app-mcp-connector-setup-instructions.md"]
---

## Request

### What we need

Replace the **Developer mode** route in the ChatGPT setup steps on the in-app MCP page
(`zooza.app/#mcp`) with the route we have now seen work on a live customer account.

This supersedes the ChatGPT half of handoff `zooza-web-to-app-20260904-001`, which is
still `open` and which asked for exactly the opposite. That handoff was written from
OpenAI's documentation in September; we now have a customer outcome from 23 October,
which beats the documentation.

### Why we need it

A customer (Mateduca s.r.o.) followed the Developer-mode instructions — ours, and the
same ones repeated back to him by an AI assistant — and **could not connect**. He got
there only after a support agent took over and gave him a different path. He went out of
his way to thank us for the handover to a human, which is a polite way of saying the
written instructions failed him.

The help centre article is already corrected and live:
`https://help.zooza.online/settings/claude-plugin/`. The in-app page is the one we tell
people to trust over the help centre, so right now the page with the most authority is
the one with the wrong steps.

### What actually happened (verified 2026-10-23, one customer, browser)

| | |
|---|---|
| **Worked** | `chatgpt.com/plugins` → add a **custom MCP server** → URL `https://mcp.zooza.app/mcp` → **Connect** → region **Europe** → sign in with **the same email as the Zooza account** → verify with `whoami` |
| **Did not work** | The Developer-mode route, including when ChatGPT itself walked him through it |
| **Also true** | Requires a **paid** ChatGPT plan |
| **Also true** | The **desktop app did not show the setting at all** — he succeeded in the browser |
| **Also true** | A **half-finished connector from an earlier attempt had to be deleted first** |

Two details worth carrying over because they are cheap and they were both failure modes:
the **Europe** region, and **the email matching the Zooza login** — a different address
authenticates happily and then finds no account.

### Constraints from our side

- **Do not hard-code a menu path beyond `chatgpt.com/plugins`.** Tech Support's note on
  this thread is that OpenAI changes this "almost every month", and the September handoff
  already made the case for not pinning a precise path. A URL is more durable than a
  breadcrumb.
- **Keep the self-service prompt, but strip Developer mode out of it.** The
  `setup_prompt` for ChatGPT currently tells the assistant to work from the Developer-mode
  steps, so it reproduces the failure on request. Asking the assistant for help is still
  the best fallback when menus have moved — it just must not be seeded with the wrong path.
- Please tell us if you find the Developer-mode route does work on some plan or region. We
  will document both rather than argue; we only know it failed for this customer.

### How we imagine it — open to challenge

Files: `pages/mcp/content/mcp.{en,sk,cs,de,hu,ro}.json`, the `clients[1]` (`chatgpt`)
block. English below; we are happy to supply the other five if that helps.

- `steps[0]` — currently *"Turn on Developer mode" / "In ChatGPT settings, switch on
  Developer mode. Custom MCP connectors need a paid plan."*
  → **"Open the plugins page"** / **"Go to chatgpt.com/plugins. Custom MCP connectors need
  a paid ChatGPT plan. If the page looks wrong in the desktop app, open it in a browser."**
- `steps[1]` — currently *"Open Plugins and add one" / "Go to Plugins and press the +
  button to add a new MCP connector."*
  → **"Add a custom MCP server"** / **"Add a custom MCP server and paste the connector URL
  below. If a Zooza entry is already there from an earlier attempt, delete it first — a
  half-finished connector does not repair itself."**
- The connect step → add **"Choose Europe as the region, and sign in with the same email
  address you use for Zooza. A different address signs in fine and then finds no account."**
- The verify step → **`whoami`** rather than "Show my programmes". It is the shortest thing
  that distinguishes "listed" from "actually authenticated", and it is what support used.
- `note` — currently titled *"Can't find Developer mode?"* → retitle to something like
  **"Nothing happens, or the page looks wrong?"** and cover: paid plan, business-workspace
  admin approval, use the browser rather than the desktop app, delete any earlier attempt.
