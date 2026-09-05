---
title: "Zooza AI FAQ"
description: "Common questions about Zooza AI — pricing, security, multi-company access, model selection, and connection troubleshooting."
slug: "claude-plugin-faq"
type: "faq"
product_area: "MCP"
sub_area: ""
audience: ["admin"]
tags: ["claude", "mcp", "ai", "connector", "faq", "security", "troubleshooting"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-09-05"
related_articles: ["claude-plugin"]
---

# Zooza AI FAQ

## Is Zooza AI free?

Yes. Zooza AI is available at no extra cost for all active Zooza customers. You only need a Claude account — [claude.ai](https://claude.ai) has a free tier.

## Is it secure? Where does my data go?

Zooza AI does not store your login credentials. Authentication happens via OAuth — the same system as signing in to zooza.app. Claude only sees data that Zooza provides during your conversation.

## Can someone else set up Zooza AI for me — an external instructor, for example?

Yes, and it is safe to let them.

**Zooza AI inherits the permissions of the account it connects with.** It is not a separate level of access. Whatever that person's role allows them to do in the Zooza app, the assistant can do — and nothing beyond it. An external instructor who cannot see payments in the app cannot see them through the assistant either.

So the question to ask is not "should they have the assistant?" but "what should their role be?" Get the role right and the assistant follows automatically. See [User roles](../guides/user-roles.md).

> This also means the assistant is not a way to give someone temporary extra access. If they need to do more, change their role; if they should not have it permanently, do the task yourself.

## We have a franchise with multiple locations. Does Zooza AI support that?

Yes. If your account has access to multiple companies, Claude will list them and ask which one you want to work with. You can switch between companies within the same conversation.

## Which AI model should I use?

Zooza AI works with multiple Claude models. You can compare their accuracy, speed, and cost in **Settings → Zooza AI → Model performance**. The comparison is updated periodically based on real usage. Use it to choose the model that best fits your priorities.

## What is the difference between Zooza AI and the chat button in the Zooza app?

These are two different AI tools with different capabilities:

| | **Chat in the Zooza app (Intercom)** | **Zooza AI (Claude / ChatGPT connector)** |
|---|---|---|
| **What it knows** | General Zooza help articles — how features work, setup steps, FAQs | Your actual account data — your registrations, clients, classes, payments, settings |
| **What it cannot do** | Answer questions about your specific account ("which clients haven't paid?", "how many people are in my Monday class?") | None — it can look up and act on your real data |
| **How to access** | The chat bubble in the bottom-right corner of zooza.app | Via claude.ai or ChatGPT with the Zooza connector enabled |
| **Best for** | "How does retention work?" / "How do I set up a payment schedule?" | "Show me unpaid registrations for June" / "Reschedule all sessions next Tuesday" |

**The Intercom chat cannot see your account.** If you ask it "who hasn't paid?" or "what classes does client X have?", it cannot look that up — it only knows what is in the help documentation. For account-specific questions, use Zooza AI (the Claude or ChatGPT connector).

## Zooza AI says it cannot do something I know it can do

Refresh the connector's tool list. **It does not update itself.**

When Zooza adds a new capability, your connector keeps the list of tools it learned when you connected. Claude and ChatGPT both cache it, and neither refreshes automatically — so the assistant will tell you, confidently, that it has no way to do the thing that shipped last week.

**In Claude:** open your connectors list and refresh the available tools (the control is at the top right of that screen).

**In ChatGPT:** go to **Settings → Apps**, open **Zooza**, and use **Refresh**. If you only see **Disconnect**, disconnect and connect again — reconnecting rebuilds the list.

If it still misbehaves after refreshing, disconnect and reconnect under a slightly different name. That forces a clean setup rather than reusing the cached one.

> This is a limitation of the AI platforms, not of Zooza — neither currently allows a connector to push an updated tool list to clients that have already connected.

## Can I run make-ups from my own system over the API?

Technically yes — everything Zooza does is available over the API, and the public
documentation only covers the endpoints most people consume. So creating client
accounts and enrolling them is possible.

**But think about the shape of it before you start.** Make-up sessions are tied to
classes and sessions by their nature. To offer them from your own system you would
have to keep a parallel calendar in both places and hold the two in step — every
class, every date, every cancellation.

That is a much bigger integration than "create a client", and at that point building
make-ups into your own system is often less work than synchronising ours with it.
Worth being honest about before the effort goes in.

## How do I report a problem with Zooza AI?

Type it into the chat where the problem happened: **"I want to send feedback to Zooza."**

There is no button to look for, which is the part people find odd — you are asking the assistant to do something, the same way you ask it anything else. It then sends us a summary of the conversation together with the tool calls it actually made, which is diagnostic information you cannot see and could not report yourself.

Do it in the conversation that went wrong rather than a fresh one, since the context is the useful part.

> If the feedback command itself fails, the connector's tool list is probably stale — refresh it as described above, then try again.

## The connection is not working. What should I do?

1. Confirm that you have an active Zooza account with Admin access.
2. Try signing out and back in via OAuth.
3. Refresh the tool list (see above) — a stale list can look like a broken connection.
4. If the problem persists, contact [support@zooza.online](mailto:support@zooza.online).
