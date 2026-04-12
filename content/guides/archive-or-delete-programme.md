---
title: "Archive or delete a Programme"
description: "You cannot permanently delete a Programme directly in the app. Instead, you archive it — this hides it from your active list while keeping all data,..."
slug: "archive-or-delete-programme"
type: "guides"
product_area: "Programmes"
audience: ["admin"]
tags: ["programme", "archive", "delete", "remove", "class", "hide"]
status: "published"
source_language: "en"
needs_screenshot_replacement: true
last_converted: "2026-04-10"
---

# Archive or delete a Programme

You cannot permanently delete a Programme directly in the app. Instead, you **archive** it — this hides it from your active list while keeping all data, bookings, and history intact.

If you need to fully remove a Programme, you can delete it from the Programme Settings page.

---

## Archive a Programme

Archiving is the standard way to remove a Programme from your active list. Use this when a Programme has ended, is no longer needed, or contains existing bookings you want to keep.

1. Go to **Programmes**.
2. Click the name of the Programme you want to archive.
3. Go to **Programme Settings** → **Edit**.![Screenshot — archive or delete programme](../../assets/images/archive-or-delete-programme-01.png)
4. Tick **Archive**.![Screenshot — archive or delete programme](../../assets/images/archive-or-delete-programme-02.png)
5. Click **Save**.

The Programme disappears from your active list. It remains accessible via the **Archived** filter in the Programmes list.

> **To restore:** Open the archived Programme, go to Programme Settings → Edit, uncheck **Archive**, and save.

---

## Archive a Class

To hide a single Class (class) within a Programme without archiving the whole Programme:

1. Go to the Programme and open the Class you want to remove.![Screenshot — archive or delete programme](../../assets/images/archive-or-delete-programme-03.png)
2. In the Class settings, tick **Archive**. ![Screenshot — archive or delete programme](../../assets/images/archive-or-delete-programme-04.png)
3. Save.

> **Note:** You cannot delete a Class that has active bookings. Archive it instead, or transfer the bookings to another Class first.

---

## Delete a Programme

Admins with the **edit_course** permission can permanently delete a Programme directly from Programme Settings. This action cannot be undone — you will lose access to all related Classes, sessions, and bookings.

> **Note:** Deletion is a soft delete. The Programme and its data are no longer accessible in the app, but are not erased from the database. There is no restore option from the UI.

1. Go to **Programmes** and open the Programme you want to delete.
2. Go to **Programme Settings → Edit**.
3. Click **Delete programme** (next to the Save button).

   ![Screenshot — archive or delete programme](../../assets/images/archive-or-delete-programme-05.png)

4. Read the warning in the confirmation dialog and click **Delete** to confirm.

   ![Screenshot — archive or delete programme](../../assets/images/archive-or-delete-programme-06.png)

Zooza redirects you to the Programmes list after deletion.

> **When to use this:** Programmes you no longer need and want fully removed from your active view. If the Programme has historical bookings you may want to reference later, consider archiving instead.

---

## Summary

| Goal | Action |
|------|--------|
| Hide from active list, keep data | Archive the Programme |
| Remove one class, keep the Programme | Archive the Class |
| Fully remove the Programme | Delete from Programme Settings |
| Restore a hidden Programme | Unarchive from Archived filter |
| Recover an accidentally deleted Programme, Class, or Registration | **Settings → Tools → Trash** (within 30 days) |

---

## Related

- [Recover deleted sessions, classes, and registrations](../guides/trash-and-restore.md) — restore accidentally deleted items within 30 days
