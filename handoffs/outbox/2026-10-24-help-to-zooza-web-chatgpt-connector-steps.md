---
handoff_id: help-to-zooza-web-20261024-001
from: help
to: zooza-web
status: open
created: 2026-10-24
updated: 2026-10-24
related_specs: []
related_handoffs: ["2026-09-04-zooza-web-to-app-mcp-connector-setup-instructions.md", "2026-09-04-zooza-web-to-help-mcp-articles-refresh.md"]
---

## Request

### What we need

Replace the **Developer mode** route in the ChatGPT setup steps on the public `/mcp`
page with the route we have now seen work on a live customer account.

In September you sent us — and the app — a handoff telling both of us to move *to* the
Developer-mode instructions, researched from OpenAI's own documentation. We acted on it.
We now have a customer outcome from 23 October that contradicts it, so this comes back the
other way. Your September note that "a precise path that's wrong is worse than a slightly
loose one that's right" is exactly the principle at stake; the conclusion just changed.

### Why we need it

A customer followed these steps and could not connect. He got there only when a support
agent took over with a different path. The public page is where people land before they
have an account, so it is the version that sets the first impression of the connector.

The help centre article is corrected and live:
`https://help.zooza.online/mcp/claude-plugin/`.

### What actually happened (verified 2026-10-23, one customer, browser)

| | |
|---|---|
| **Worked** | `chatgpt.com/plugins` → add a **custom MCP server** → the connector URL → **Connect** → region **Europe** → sign in with **the same email as the Zooza account** → verify with `whoami` |
| **Did not work** | The Developer-mode route, including when ChatGPT itself walked him through it |
| **Also true** | Requires a **paid** ChatGPT plan; the **desktop app did not show the setting**; a **half-finished connector from an earlier attempt had to be deleted first** |

### Constraints from our side

- Nothing in the Claude column is in question — leave it alone.
- Please keep the pasteable prompt, but take Developer mode out of the ChatGPT variant.
  As written it hands the assistant the path that failed, so asking for help reproduces
  the failure.
- Tell us if you find Developer mode does work on some plan or region and we will document
  both routes. We only know it failed for this customer.

### How we imagine it — open to challenge

Files: `src/data/mcp/{en,sk,cs,de,pl,ro}.ts`. Three touches in the English file, and the
same in each translation:

1. **`steps[0]`, the ChatGPT path.** Currently *"Switch on Developer mode in Settings,
   then open Plugins — the section that used to be called Connectors."*
   → **"Go to chatgpt.com/plugins. Needs a paid ChatGPT plan, and the browser rather than
   the desktop app."**
2. **`steps[1]`, the ChatGPT path.** Currently *"The + button in Plugins, same URL."*
   → **"Add a custom MCP server with the URL below, then Connect — choose the Europe
   region and sign in with the same email you use for Zooza. Delete any earlier Zooza
   entry first."**
3. **`setupPrompt.variants`, the ChatGPT variant.** Currently *"I first need Developer mode
   switched on in Settings, then Plugins (this section used to be called Connectors) and
   the + button with that URL."*
   → **"The route that works is chatgpt.com/plugins → add a custom MCP server with that
   URL → Connect, Europe region, signing in with the email on my Zooza account. Developer
   mode is a dead end — do not send me there. Sign-in is OAuth with my existing Zooza
   login."**

Worth considering while you are in there: `steps[3]` says *"Who am I, and what can you
do?"*. **`whoami`** is a sharper check — it is what support used, and it is the shortest
thing that tells a listed-but-unauthenticated connector apart from a working one.
