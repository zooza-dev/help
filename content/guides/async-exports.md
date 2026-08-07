---
title: "Exporting data and reports"
description: "Export bookings, payments, invoices, and other reports from Zooza. Large exports are queued and delivered as a download when ready."
slug: "async-exports"
type: "guides"
product_area: "Settings"
sub_area: ""
audience: ["admin"]
tags: ["export", "download", "reports", "data", "XLSX"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-08-07"
related_articles: ["reports-dashboard"]
---

# Exporting data and reports

Zooza lets you export bookings, invoices, payments, credits, and session data as XLSX spreadsheets or accounting files. Exports are triggered directly from the list or report they belong to — click the **Export** or **Download** button and Zooza prepares the file.

## How exports work

Zooza decides automatically whether to deliver the file immediately or queue it in the background:

| Export size | What happens |
|---|---|
| **Small** (most exports) | File downloads immediately — the browser saves it as usual. |
| **Large** (many rows — e.g. 5,000+ registrations) | Export is queued. A "Preparing…" message appears. When the file is ready, you receive an in-app notification and the file downloads automatically. |

The threshold between small and large is checked automatically. You do not need to do anything differently — just click **Export** and wait.

> **Why some exports appear in your browser downloads and others do not.** A small export downloads straight away, the way exports always used to. A large one is prepared in the background and lands in **Settings → Tools → Exports** instead.
>
> Nothing has broken if a file does not appear in your downloads folder — it went to the exports list because it was too big to produce on the spot. If you have never opened that list, that is where your missing exports are.
>
> If an export of everything fails outright rather than queuing, narrow it with a filter (one billing period, one programme) and export in parts.

## What to do when an export is queued

1. You will see a **"Preparing…"** notification when a large export is queued.
2. Continue working in Zooza as normal — the export runs in the background.
3. When the file is ready, a toast notification appears and the download starts automatically.
4. If you closed the tab before the notification arrived, find the completed export in **Settings → Tools → Exports**.

## Tools → Exports listing

Go to **Settings → Tools → Exports** to see a full history of your company's exports.

The listing shows:

| Column | Description |
|---|---|
| **Type** | What kind of export it is (e.g. Registrations, Invoices, Pohoda) |
| **Status** | Ready / Processing / Failed / Expired |
| **Requested by** | Which admin triggered the export |
| **Created** | When the export was requested |
| **Download** | For ready exports: a download link |

Exports with a **Ready** status can be re-downloaded from this screen. Exports expire after a period and the download link becomes unavailable — re-export from the source list if you need it again.

## Which exports are covered

Large-export queuing currently applies to these export types:

- Registrations (×2 formats)
- Invoices — Omega partners, Omega EÚD
- Accounting files — Pohoda (CZ), MRP

Other export types (payments, credits, events, schedule reports, accounting integrations) use the same screen and behave identically — the large-export path will be added to them in a follow-up update.

> **Calendar and document downloads** (printable PDF calendar, individual invoice PDFs, stored documents) are separate from the export system and are not affected.
