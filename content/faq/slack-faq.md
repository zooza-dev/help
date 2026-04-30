---
title: "Slack Integration FAQ"
description: "Answers to common questions about connecting Slack to Zooza, receiving notifications, using slash commands, and managing the integration."
slug: "slack-faq"
type: "faq"
product_area: "Communication"
sub_area: "Slack"
audience: ["admin"]
tags: ["slack", "integrations", "notifications", "todos", "franchise", "network"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-04-30"
---

# Slack Integration FAQ

## Who can connect Slack to Zooza?

You need the **Owner** or **Assistant** role in Zooza, plus permission to install apps in your Slack workspace (your Slack workspace admin may need to approve new apps first).

## Do all team members need to do anything in Slack?

No extra setup for most team members. Once an admin connects the workspace, Zooza can deliver notifications to your Slack channels automatically. Team members who want to **create todos from Slack** using `/zooza` do need to link their Slack account to Zooza the first time they use the command — this takes about 30 seconds. See [Use Zooza from Slack](../guides/zooza-in-slack.md).

## Our franchise has one Slack workspace for all locations. Do each location's admins need to connect separately?

No. One admin at any location installs the Zooza app into the shared Slack workspace. All other companies in the Zooza network are automatically attached. Each location's admin then only needs to go to **Settings → Integrations → Slack** to pick which Slack channels receive their notifications — no additional OAuth required.

## My Slack email is different from my Zooza email. Can I still use /zooza?

Yes. The first time you use `/zooza`, the bot detects the mismatch and asks you to verify your Zooza account with a 6-digit code sent to your Zooza email. Enter the code in Slack and your accounts are linked permanently. See [Use Zooza from Slack](../guides/zooza-in-slack.md).

## What notifications does Zooza send to Slack?

Zooza sends notifications through two streams, each mapped to a Slack channel of your choice:

- **Todos** — when a todo is assigned to a colleague (not a self-assignment), the notification appears in the configured channel.
- **System messages** — automated alerts such as worker failures, payment errors, or integration issues.

You choose which channels receive each stream in **Settings → Integrations → Slack → Channel mapping**. Unmapped streams are not delivered to Slack.

## Why am I not getting Slack notifications for todos I create myself?

Todos that you assign to yourself do not trigger a Slack notification — just like the in-app notification is also silent for self-assignments. This is by design to avoid noise. Notifications fire when you assign a todo to a colleague, or when a colleague completes a todo you created.

## Notifications stopped appearing in our Slack channel. What happened?

The most common cause is that the Zooza bot token was revoked. This can happen if:
- A Slack workspace admin removed the Zooza app from the workspace.
- Someone from a different Zooza network or company completed a fresh OAuth into the same Slack workspace, rotating the bot token.

Go to **Settings → Integrations → Slack**. If the status shows **Needs re-authorization**, click **Reconnect** and complete the OAuth flow again.

## A Slack channel is not showing up in the channel list. How do I fix this?

The Zooza bot must be a member of the channel. In Slack:
1. Open the channel.
2. Click the channel name at the top.
3. Go to **Integrations → Add apps**.
4. Search for and add **Zooza**.

The channel will appear in Zooza's channel list within a few minutes (the list is cached for 5 minutes).

## Can I stop Slack delivery for my company without disconnecting the whole network?

Yes. Go to **Settings → Integrations → Slack** and click **Disconnect this company**. This removes your channel mappings and stops Slack delivery for your company. The Slack workspace install and other companies in the network are unaffected.

## How do I remove the Zooza Slack app from our workspace entirely?

Only the company that originally completed the OAuth can uninstall. Go to **Settings → Integrations → Slack** and click **Uninstall**. This revokes the bot from Slack and deactivates the connection for all attached companies.

## Can two Zooza networks share the same Slack workspace?

No. Each Slack workspace can only be connected to one Zooza network. If a second network attempts to install into the same workspace, the install is rejected. If this is causing an issue, contact support.

## Related

- [Connect Slack to Zooza](../setup/slack-integration.md)
- [Use Zooza from Slack](../guides/zooza-in-slack.md)
