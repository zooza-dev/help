# Blog briefing — Zooza 3.8 update post, April 2026

## Task

Update the existing **Zooza 3.8 blog post** on the WordPress website with the new features shipped in the week of 7–9 April 2026. The post already exists in all language variants (SK, EN, HU, RO, CS). Add a new section for each feature listed below. Do not rewrite existing content — append only.

Blog post location: `zooza_website/blog/` — find the 3.8 posts in all language variants.

---

## New features to add

### 1. Mazanie programu (Delete a Programme)

**What it does:**  
Admins can now permanently delete a Programme directly from Programme Settings, without needing to contact support. The Delete button appears next to the Save button inside Programme Settings → Edit. Deletion shows a confirmation dialog and is a soft delete (data not erased from database, but no longer accessible in app). Use archiving if you want to keep historical data.

**Help article (EN):** https://help.zooza.online/help/guides/archive-or-delete-programme

---

### 2. Ad hoc plánovaná platba (Ad Hoc Scheduled Payment)

**What it does:**  
Admins can now add one-off scheduled payments to existing payment plans — useful for late fees, partial catch-ups, or custom arrangements. Two entry points:

- **Individual:** "Add scheduled payment" button on a registration's payment plan page
- **Bulk:** New flow from the class detail page — configure the payment, select registrations, confirm. Each registration uses its own contract values as defaults.

Amount must be entered as a negative number (e.g. `-20`) to create a charge.

**Help article (EN):** https://help.zooza.online/help/guides/ad-hoc-scheduled-payment

---

### 3. História platobného plánu (Payment Plan History)

**What it does:**  
Each registration's payment plan page now shows a full history of all previous payment plans that were applied, including which template was used and when. Useful for auditing and resolving disputes.

**Help article (EN):** https://help.zooza.online/help/guides/ad-hoc-scheduled-payment (section: Payment plan history)

---

### 4. Opravené oprávnenia asistenta (Assistant Role Permissions Fixes)

**What it does:**  
Multiple permission bugs affecting the Assistant role are now fixed:

- **Full attendance management** — assistants now see all attendance options (arrived, didn't arrive, cancelled, substitute hour, extra term). Previously only the trainer's limited view was shown.
- **Payments navigation fixed** — assistants can now access the Payments overview and payment detail pages (previously resulted in "page not found").
- **Trainer rates** — assistants can now view and edit trainer rates in the profile tab.
- **Trainer reports** — assistants can now download trainer reports.

**Help article (EN):** https://help.zooza.online/help/guides/user-roles

---

### 5. Zoraďovanie položiek služieb (Service Item Reordering)

**What it does:**  
Service items on the service detail page are now displayed as collapsible panels (composite components) and can be reordered via drag and drop. The collapsed view shows the item name and unit price. The order set in the admin is the order customers see during registration in the widget.

**Help article (EN):** https://help.zooza.online/help/reference/services-list

---

### 6. Fronta a sledovanie hromadných správ (Bulk Message Queue & Tracking)

**What it does:**  
Bulk email sending now runs through a proper background queue with full tracking:

- **Approval gate** — sends to 100+ recipients require explicit approval before the send starts (prevents accidental mass sends).
- **Progress view** — live send progress showing how many messages were sent, are in progress, or failed.
- **Send history** — each bulk send is logged as a job with status (pending approval → queued → sending → completed / cancelled / failed).
- **Cancellation** — active send jobs can be cancelled.
- **Queue** — only one active send per account at a time; additional jobs are queued automatically.

**Help articles (EN):**
- https://help.zooza.online/help/guides/sending-email-sms
- https://help.zooza.online/help/guides/bulk-email-send-tracking

---

## Tone & style notes

- Keep consistent with existing 3.8 post tone — factual, feature-focused, no fluff.
- Each language variant needs its own translated version of the new sections.
- Use the help article links as-is (EN URLs) — the help site is English-only.
- Screenshots: placeholder images exist for bulk email features; skip or use existing screenshots for other features.

---

## Languages to update

- Slovak (SK) — primary, write first
- English (EN)
- Hungarian (HU)
- Romanian (RO)
- Czech (CS)
