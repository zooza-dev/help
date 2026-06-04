---
title: "Attach Documents to Sessions"
description: "Upload and attach multiple prep-material documents to a session in one step, control when each file becomes available to participants, and display them inline in the client profile widget."
slug: "session-document-attachments"
type: "guides"
product_area: "Calendar"
sub_area: ""
audience: ["admin"]
tags: ["documents", "session", "files", "upload", "widget", "prep-material"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-06-04"
related_articles: ["documents", "edit-sessions-in-programmes", "calendar-bulk-actions"]
---

# Attach Documents to Sessions

You can now attach multiple documents (PDFs, images, videos, and other files) to a session directly from the session notes card — without leaving the calendar. Participants see the documents in their profile widget, with timing control over when each file becomes available.

## How to attach documents

Open any session from the calendar:

1. Go to **Calendar** and open a session (either Quick view or Full view).
2. In the **Notes** card, find the **Prep material (visible to client)** upload box.
3. **Drag and drop** files onto the box, or click it to select multiple files at once.
4. Each file uploads individually — progress is shown per file. If one file fails, the rest continue.
5. Once all uploads complete, the files are attached to the session automatically. No separate naming step is needed — the file's original filename is used.

## File availability

For each attached file you can choose when it becomes visible to participants:

| Option | When participants can see the file |
|---|---|
| **Before** (default) | Immediately on attach — useful for prep material |
| **At session** | From the session's scheduled start time |
| **After session** | From the session's end time |

Change availability at any time after attaching by using the dropdown next to each file in the attached-documents list.

## Visibility by payment status

Each file also has a visibility tier inherited from the Documents system:

- **All** — visible to any registered participant, including unpaid.
- **Paid** — visible only to participants with a completed payment.

## Managing already-attached documents

The attached-documents list (shown below the upload box) is loaded every time you open the session:

- **Open** — click a filename to open the file. Images open inline in a new tab; other file types download.
- **Change availability** — use the availability dropdown on any row.
- **Remove** — click **Remove** to detach the file from the session. The file is not deleted from your Documents library.

## What participants see

Participants view session documents in their client profile widget in two places:

1. **Inline next to the session** — a compact list of available files appears beside that session's entry in the public programme summary.
2. **Files tab** — the dedicated Súbory (Files) tab continues to work and lists all accessible documents.

**Images** are shown as a thumbnail grid. Clicking a thumbnail opens a lightbox with full-size images and previous/next navigation. Thumbnails are lazy-loaded.

A file that is not yet available shows an **"Available from [date]"** notice instead of a download link. Files that the participant is not entitled to see do not appear at all.

## Bulk download

Participants can click **Download all** on a session to receive a single zip archive of all the files they are entitled to view for that session.

## Notes

- The session document upload is available to any user role that can view and act on sessions (i.e., the same role gate as editing a session).
- Files uploaded through the session upload box remain accessible in the main Documents library.
- The maximum recommended file size follows your storage account's standard limit.
