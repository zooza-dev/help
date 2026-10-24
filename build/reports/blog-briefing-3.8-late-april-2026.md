# Blog briefing — Zooza 3.8 update post, late April 2026

## Task

Update the existing **Zooza 3.8 blog post** on the WordPress website with the new features shipped in the last week of April 2026. The post already exists in all language variants (SK, EN, HU, RO, CS). Add a new section for each feature listed below. Do not rewrite existing content — append only.

Blog post location: `zooza_website/blog/` — find the 3.8 posts in all language variants.

---

## New features to add

### 1. Slack integrácia (Slack Integration)

**What it does:**
Zooza now connects directly to Slack. Once an admin links the workspace (one-time OAuth setup), the team gets Zooza notifications in Slack channels — todo assignments, system alerts, and other operational events — without switching tabs.

**Key points for the blog:**
- One install per Slack workspace, shared across an entire franchise network. Franchise units only need to pick their channels — no per-location re-authorization.
- Team members can also create Zooza to-dos directly from Slack using the `/zooza todo` command or the "Create Zooza todo" message shortcut on any message.
- First-time Slack users link their account via a quick email verification (30 seconds, one-time only).

**Help articles (EN):**
- https://help.zooza.online/communication/slack-integration/ — setup guide
- https://help.zooza.online/communication/zooza-in-slack/ — using Zooza from Slack
- https://help.zooza.online/communication/slack-faq/

---

### 2. Zoznam úloh — To-dos (To-do List)

**What it does:**
A lightweight task list is now built into the Zooza sidebar. Create a reminder in under 5 seconds — type one line, optionally assign it to a teammate and set a due date, save. Each to-do can be linked to the screen where it was created (a booking, event, or payment), so one click takes you right back to the relevant record.

**Key points for the blog:**
- Assignee gets a real-time notification in the sidebar — and in Slack if connected.
- When the assignee completes the to-do, the creator is notified.
- Private by default — you only see to-dos where you're the creator or the assignee.

**Help articles (EN):**
- https://help.zooza.online/settings/todos/
- https://help.zooza.online/settings/todos-faq/

---

### 3. Hromadné akcie na mobile — nový bočný panel (Calendar Bulk Actions on Mobile)

**What it does:**
On mobile, the calendar's bulk action buttons (Send email, Send SMS, Edit) used to wrap and overlap the calendar grid — making them unclickable. They now live in a dedicated side drawer opened via an "Actions" button. Desktop behaviour is unchanged.

**Key points for the blog:**
- Tap **Actions** → **Enable bulk selection** → select sessions → tap the action.
- A badge on the Actions button shows how many sessions are currently selected.

**Help article (EN):**
- https://help.zooza.online/calendar/calendar-bulk-actions/

---

### 4. Zrušenie registrácie — automatické skrývanie dochádzky (Scheduled Cancellation — Automatic Attendance Hiding)

**What it does:**
When you schedule a registration to cancel on a future date, Zooza now immediately hides the client's attendance from all sessions on and after that date. Trainers' attendance lists stay clean without manual cleanup. If you change the date or revoke the cancellation, the attendance is restored automatically.

**Key points for the blog:**
- Only sessions that are unset or marked "going" are touched automatically — anything the admin explicitly set (attended, no-show, etc.) stays.
- Two new email merge variables: `CANCELLATION_SCHEDULED` and `CANCELLATION_DATE` — use them in templates to conditionally tell clients when their registration ends.

**Help article (EN):**
- https://help.zooza.online/bookings/scheduled-registration-cancellation/

---

### 5. Zoskupovanie miestností vo widgete (Widget: Merge Rooms Option)

**What it does:**
A new **Merge rooms** setting in the registration widget groups all rooms at the same location into one entry. Clients pick the venue; the specific room is assigned automatically based on the selected class. Useful for venues with multiple rooms where the room distinction is an internal detail.

**Key points for the blog:**
- Enabled by default on newly created registration widgets.
- Existing widgets keep their current behaviour until the admin changes the setting.
- Set it in **Settings → Widgets → [registration widget] → Merge rooms**.

**Help article (EN):**
- https://help.zooza.online/widgets/widget-merge-rooms/

---

### 6. Výber avatara zo zoznamu (Preset Avatar Selection)

**What it does:**
Users can now set their profile avatar by choosing from a gallery of preset images — no photo upload needed. The gallery is available in **Settings → My profile**.

**Help article (EN):**
- https://help.zooza.online/settings/profile-avatar/

---

### 7. Rozdelenie faktúry pri zálohe — HU/RO (Downpayment Invoice Split — Hungary & Romania)

**What it does:**
For companies in Hungary and Romania using Számlázz.hu, SmartBill, or Oblio: a new setting issues two separate invoices for registrations with a downpayment — one for the deposit, one for the final balance. Required by local tax law (invoice must be issued within ~8 days of each payment received).

**Key points for the blog:**
- Enable in **Settings → Billing → Invoice Profile → Split downpayment invoice**.
- Applies to new registrations only (no retroactive changes to existing invoices).
- Only relevant for HU and RO markets — other markets unaffected.

**Help article (EN):**
- https://help.zooza.online/payments/downpayment-split-invoicing/

---

## Tone & style notes

- Keep consistent with existing 3.8 post tone — factual, feature-focused, no fluff.
- Slack and Todos are the headline features — lead with these.
- For the Downpayment Invoice Split, write a short paragraph; it's market-specific so don't over-emphasise it in SK/EN/CS variants. HU and RO variants should give it more prominence.
- Each language variant needs its own translated version of the new sections.
- Use the help article links as-is (EN URLs) — the help site is English-only.
- Do not blog about: manual offline charge push (too technical/admin recovery).

---

## Languages to update

- Slovak (SK) — primary, write first
- English (EN)
- Hungarian (HU) — give Downpayment Invoice Split more prominence here
- Romanian (RO) — give Downpayment Invoice Split more prominence here
- Czech (CS)
