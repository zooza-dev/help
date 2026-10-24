# Zooza — Onboarding & UX Brief

**Date:** 10 May 2026  
**Source:** 3 WhatsApp support conversations — Turtle Tots Dubai (Anna, 160 days), babyballet Dubai (Kate, 9 months), Wee Kicks (Dom, 5 months). Combined ~2,500 support messages.  
**Goal:** Identify what to fix in the app so a franchisee can operate Zooza independently.

---

## The core finding

After 5–9 months of live operation, none of the three clients can run Zooza independently. They all rely on direct support from Michal for routine tasks.

> *"I should be able to do this all myself by now but it is not intuitive. The main problem is that I have to rely on you to do everything."*
> — Anna, Turtle Tots, Day 152

> *"I'm worried this is going to be complicated for the franchisees if I'm struggling."*
> — Dom, Wee Kicks — a franchise operator planning to roll out Zooza to his own franchisees

This is a systemic product problem, not a user capability problem.

---

## The paradigm shift nobody explains

Zooza works fundamentally differently from manual tools and legacy systems like Thinksmart or Netguides:

| How they used to work             | How Zooza works                                             |
| --------------------------------- | ----------------------------------------------------------- |
| Admin books clients manually      | Admin sets up rules; clients self-register                  |
| Admin sends rebooking emails      | Automations send them                                       |
| Admin adjusts payments per client | Payment rules run automatically                             |
| Edit once → applies everywhere    | Three layers: Programme → Class → Session, each independent |

**This shift is never communicated inside the app.** New operators don't trust the automation, so they try to do things manually — which breaks the automation — which confirms their distrust. Breaking this loop is as important as any individual UX fix.

---

## What's broken — validated across 3 clients

| #   | Problem                                                               | Anna | Kate | Dom |
| --- | --------------------------------------------------------------------- | ---- | ---- | --- |
| P1  | Programme/Class/Session hierarchy is invisible                        | ✅    | ✅    | ✅   |
| P2  | Editing one layer doesn't cascade to others (instructor, price, time) | ✅    | ✅    | ✅   |
| P3  | No Zooza-native refund flow                                           | ✅    | ✅    | ✅   |
| P4  | Payment status UI unreadable ("-£1,468 Outstanding")                  | ✅    | ✅    | ~   |
| P5  | Term rebooking is entirely manual                                     | ✅    | ✅    | ~   |
| P6  | "Class full" shown to enrolled clients completing payment             | ✅    | ✅    | —   |
| P7  | Attendance register too slow for in-class use on phone                | ✅    | ✅    | —   |
| P8  | Sibling discount: no automated rule                                   | ✅    | ✅    | ✅   |
| P9  | Trial management: admin cannot create or reschedule manually          | ✅    | ~    | ~   |
| P10 | No guided setup when account is new                                   | ✅    | ✅    | ✅   |

Zero contradictions across three independent clients.

---

## The franchisee journey — what they see and what to fix

This is a screen-by-screen map of a franchisee's first week. For each moment: what currently happens, what breaks, and what to change.

---

### Moment 1 — First login: no start point

**Currently:** Empty or near-empty dashboard. No prompt. No sequence.  
**What happens:** Users click randomly. Anna went to Classes before creating a Programme (Classes require a Programme — empty list, no explanation).

**Fix — Persistent setup checklist (empty state):**
```
Getting started with Zooza

□ 1. Create your first programme
□ 2. Add a class with sessions
□ 3. Set up payments (Stripe / GoCardless)
□ 4. Check your booking page
□ 5. Share your booking link

Complete each step to unlock the next.
```
Stays visible until all 5 are done. Each item links directly to the right screen.

**Effort:** Medium (new component, no logic change)

---

### Moment 2 — Navigation: three equal siblings

**Currently:** Left nav shows `Programmes`, `Classes`, `Sessions` as three flat items under Activities.  
**What happens:** Users click `Classes` first (natural instinct). It's an empty list. No context. Nothing says "create a Programme first."

This is the most disorienting moment in the first 10 minutes — confirmed by all three clients.

**Fix — Reflect the hierarchy in the nav:**

Minimal change (Option A): Visually indent Classes and Sessions under Programmes:
```
Activities
  > Programmes
      Classes
      Sessions
  > Calendar
```

Better change (Option B): Remove Classes and Sessions from the top nav. Access them by drilling into a Programme (tabs inside). The flat nav only shows entry points, not layers.

**Effort:** Option A = Small. Option B = Medium.

---

### Moment 3 — Creating a Programme: confusing labels

**Currently:** Programme type options: *"One-off event"* / *"Booking for the full programme duration"* / *"Pay-as-you-go"*.  
**What happens:** Users don't know which to pick. Wrong choice = wrong payment setup = manual fixes later.

**Fix — Rename with plain language + example:**

| Current | Proposed | Sub-label |
|---------|----------|-----------|
| One-off event | Single event | A workshop, trial day, or one-time class |
| Booking for the full programme duration | Term / block booking | Clients pay once for the whole period |
| Pay-as-you-go | Drop-in | Clients book and pay per session |

Add one line at the top of the form:
> *"A programme is a container for your classes. It sets the payment model and rules. You'll add specific class schedules inside it."*

**Effort:** Small (label + copy changes)

---

### Moment 4 — Creating a Class: where am I?

**Currently:** Form title `ADD A NEW CLASS`. No indication of which Programme this belongs to.  
**What happens:** After a few classes, users lose track of which class is in which programme. They edit the wrong one.

**Fix 1 — Breadcrumb above the form:**
```
Programmes > Turtle Tots (5–7 yrs) > Add a new class
```

**Fix 2 — Price field labels:**

| Current label | Problem | Proposed label |
|--------------|---------|----------------|
| Total price | Per session? Per term? | Class fee — what clients pay to join for the full period |
| Registration fee (optional) | OK | One-time sign-up fee (charged at registration, separate from class fee) |
| Billable sessions (leave empty if all are billable) | Opaque | Number of sessions to charge for (leave empty to charge for all) |

**Effort:** Small (breadcrumb + label changes)

---

### Moment 5 — Editing instructor, time, or price: which scope?

**Currently:** Edit an instructor → save → change may or may not apply to other sessions. No indication of scope.  
**What happens:** Users change an instructor in one view; it doesn't update in another. This was the most repeated confusion across all three clients. Dom's payment settings kept "reverting to defaults" — he was editing the wrong layer.

**Fix — Scope selector on any edit that can cascade:**

```
Apply this change to:
  ○ This session only  (Monday, 3 Mar)
  ● All upcoming sessions in this class    ← default
  ○ All sessions in all classes of this programme
```

Same pattern applies to: instructor, time, price, cancellation.

This single fix resolves the most common confusion in every onboarding conversation.

**Effort:** Medium (new UI component, reused across multiple edit forms)

---

### Moment 6 — "Groups" vs "Classes"

**Currently:** Page title says `Groups \`. Nav says `Classes`. These are the same thing.  
**What happens:** Every new user has to learn that "Groups = Classes". Unnecessary cognitive load on day 1.

**Fix:** Use `Classes` everywhere the admin sees it. `Groups` can remain an internal/technical term but never shown in the UI.

**Effort:** Small (label sweep)

---

### Moment 7 — Financial columns no one understands

**Currently:** Class list shows columns `Paid Debt | Issued Debt | Balance`.  
**What happens:** "Debt" reads as something owed. "Paid Debt" sounds like debt that was already paid (i.e. zero). Users misread their financial state.

**Fix — Rename columns:**

| Current | Proposed |
|---------|----------|
| Issued Debt | Total charged |
| Paid Debt | Collected |
| Balance | Outstanding |

**Effort:** Small (label changes)

---

### Moment 8 — Payment status: "-£1,468 Outstanding"

**Currently:** Client row in session/attendance view shows:
```
⚠ Outstanding
-£1,468.00
[Add payment]
```
**What happens:** The minus sign looks like credit or overpayment. "Outstanding" contradicts it. Anna: *"I'm not a stupid person but honestly Zooza makes me feel like I am!!"* — directly about this screen.

**Fix — Plain-language status badge:**

```
💰 £1,468 due        [Add payment]       Last payment: —
✅ Paid              [View payments]     Last payment: £230, 3 Jan
💚 £115 credit                          Last payment: £345, 15 Feb
⏳ Awaiting payment  [Send reminder]     Due: 15 Jan
```

Keep the detailed ledger accessible (expandable) — but the headline is always plain English. A franchisee should answer "has this client paid?" in under 3 seconds.

**Effort:** Medium (status component, no logic change — data already exists)

---

### Moment 9 — "Class full" shown to enrolled clients

**Currently:** All full-class scenarios show the same message: `"Class full"`.  
**What happens:** Enrolled parents who haven't yet completed payment see "class full" when they try to pay. They think they've lost their spot. They contact the franchisee, who contacts Michal. Happened with 50+ clients in Turtle Tots alone.

**Fix — Two different messages based on registration state:**

For genuinely new registrations:
> *"This class is full. Join the waitlist and we'll notify you if a spot opens."*

For clients who are already registered:
> *"You're already enrolled. Log in to your Parent Portal to complete your payment."*

**Bonus:** Show capacity breakdown to admin:
`"8/10 spots — 6 enrolled + 2 trials"`

**Effort:** Small (message copy) + Small (capacity display)

---

### Moment 11 — Dashboard: no master Create panel

**Currently:** The dashboard has no dedicated "create anything" area. Creating an entity always means: navigate left nav → find the right section → find the "New X" button. Every entity type (programme, class, booking, client, location, instructor) has its own buried entry point.  
**What happens:** Users don't know where to start. Kate searched for "how do I add a client manually." Dom asked "where do I create the block?" Anna spent Day 1 clicking around without finding where to begin.

**Fix — Master Create panel on the dashboard:**

A prominent section on the dashboard (not in the nav — on the home screen itself), always visible:

```
┌─────────────────────────────────────────────┐
│  Create                                      │
│                                             │
│  [Programme]  [Class]  [Booking]            │
│  [Location]   [Instructor]  [Email]         │
└─────────────────────────────────────────────┘
```

Large, labelled buttons. Each goes directly to the create form for that entity. This is the first thing a new franchisee sees — it answers "where do I start?" without any navigation.

For new accounts (empty state): this panel is the primary focus of the dashboard, full-width, with a short one-line description under each button explaining what it is.

For active accounts: smaller panel, secondary position below key stats.

**Source:** Intercom — "Ako pridať klienta manuálne?" (★★), "Kde nájdem registračný formulár?" (★★). All 3 WhatsApp clients had "where do I create X?" moments in their first week.

**Effort:** Medium (new dashboard component, links to existing create forms)

---

### Moment 10 — After class setup: where's the booking link?

**Currently:** After creating a class, user is returned to the class list. No next step shown.  
**What happens:** The most critical question after setup — "how do my clients register?" — has no obvious answer. Anna asked this on Day 1.

**Fix — Post-creation confirmation with booking link:**
```
✅ Class created — Monday Seahorse 9am, starting 5 Jan

Your clients can now register online.

[Copy booking link]   [Preview booking page]   [Back to programme]
```

**Effort:** Small (post-action screen or toast notification)

---

## Contextual top actions per screen

**The problem:** Users land on a detail screen knowing *what they want to do* but not *where to find it*. Intercom data shows 35% of all support conversations are navigation questions — "kde nájdem X", "ako sa dostanem k Y".

**The fix:** Each key detail screen gets a contextual **"Actions" dropdown** — one button that expands to show the 5–7 most common things people do on that screen, ordered by frequency. The dropdown is context-aware: it knows which screen you're on and what's relevant there.

**Design pattern:** Zooza already has scattered action buttons on list screens (Bookings: "Send email / Export", Classes: "Group attendance report / Send email"). The proposal is one consistent "Actions ▾" dropdown per detail screen, data-driven, replacing the current scattered or missing buttons.

```
[Actions ▾]
────────────────────
  Add payment
  Send reminder
  Transfer to class
  Apply discount
  Cancel registration
  ─────────────────
  Archive
```

Top actions visible immediately. Destructive actions (archive, cancel) separated by a divider at the bottom.

For each screen, the source is: Intercom support topics + WhatsApp conversation analysis (Anna, Kate, Dom).

---

### Programme detail

*What people go here to do:*

| Priority | Action | Source |
|----------|--------|--------|
| 1 | **Add new class** | All 3 clients, every term |
| 2 | **Copy booking link** | Anna Day 1, Intercom ★★ |
| 3 | **Edit settings** (price, payment model) | Kate, Dom — wrong layer edits |
| 4 | **Enable / disable online booking** | Intercom ★★ ("kurzy nie sú vidieť na webe") |
| 5 | **Set up make-up sessions** | Intercom ★★★, Anna, Kate |
| 6 | **Copy programme** (to new term) | Anna, Kate — term reset |
| 7 | **Archive programme** | Intercom ★★★★ ("ako vymazať kurz") |

Show as pills at top: `[+ Add class]  [Copy link]  [Edit settings]  [···]`  
Archive in `···` overflow — it's rare but always searched for.

---

### Class (Group) detail

*What people go here to do:*

| Priority | Action | Source |
|----------|--------|--------|
| 1 | **View registrations / attendee list** | All 3 clients, daily |
| 2 | **Mark attendance** | Intercom ★★, Anna, Kate |
| 3 | **Change instructor** | Anna repeatedly, Dom |
| 4 | **Send email to all clients in this class** | Intercom ★★, Kate |
| 5 | **Cancel a session** | Anna, Kate — weekly |
| 6 | **Add client to this class** | Kate, Dom |
| 7 | **Export class list** | Intercom ★★ |

Show as pills: `[Registrations]  [Mark attendance]  [Send email]  [···]`  
Note: "Mark attendance" should deep-link to today's session, not to an attendance list.

---

### Registration (Booking) detail

*What people go here to do:*

| Priority | Action | Source |
|----------|--------|--------|
| 1 | **Add payment** (manual) | Anna, Kate, Dom — most common action |
| 2 | **Send payment reminder** | Intercom ★★, Anna |
| 3 | **Transfer to different class** | Intercom ★★★ ("skopírovať/presunúť registráciu") |
| 4 | **Apply discount** | Anna, Kate — sibling, loyalty |
| 5 | **Cancel registration** | Intercom, all 3 clients |
| 6 | **Change status** (trial → enrolled, etc.) | Anna, Kate |
| 7 | **View invoice / download** | Intercom ★★★ ("kde nájdem faktúry") |

Show as pills: `[Add payment]  [Send reminder]  [Transfer]  [···]`

Intercom finding: "Čo znamená awaiting payment?" was ★★ — the status itself needs to be self-explanatory (see Moment 8, payment badge).

---

### Payment detail (within registration)

*What people go here to do:*

| Priority | Action | Source |
|----------|--------|--------|
| 1 | **Mark as received** (cash / bank transfer) | All 3 clients |
| 2 | **Adjust amount due** | Kate, Dom — prorate, discount |
| 3 | **Reconnect GoCardless** | Intercom ★★★ (expires every 90 days, silent) |
| 4 | **Download invoice** | Intercom ★★★ |
| 5 | **Issue refund** (via Stripe) | Anna — 100+ refunds, no UI |
| 6 | **Send payment reminder** | Intercom ★★ |

Critical addition: **GoCardless expiry warning** should appear here proactively, not wait for the user to notice. Intercom had 8+ conversations on this one issue alone — all reactive.

```
⚠️  GoCardless connection expires in 12 days.
    If not renewed, payments will stop collecting.
    [Renew now]
```

---

### Attendance detail (session / class view)

*What people go here to do:*

| Priority | Action | Source |
|----------|--------|--------|
| 1 | **Mark attended / did not attend** | All 3 clients, instructors daily |
| 2 | **Offer make-up session** | Intercom ★★★, Anna, Kate |
| 3 | **Contact client** (send message) | Anna, Kate |
| 4 | **Add note** (internal) | Kate |
| 5 | **Cancel this client from session** | Anna, Kate |

Mobile-specific note: This screen is used by instructors on phone between classes. Max 3 visible actions, large tap targets. "Mark attended" should be one tap per client, not a form.

---

### Session detail (individual occurrence)

*What people go here to do:*

| Priority | Action | Source |
|----------|--------|--------|
| 1 | **Cancel this session** (all clients) | Anna, Kate weekly |
| 2 | **Change instructor** for this session | Anna — instructor no-show |
| 3 | **Change time or location** for this session | Anna, Kate |
| 4 | **Mark all attendance at once** | All 3 clients |
| 5 | **Send notification to all clients** (change/cancellation) | Intercom ★★, Anna |
| 6 | **Set as make-up available** | Intercom ★★★, Kate |

Key: actions 1, 3, 5 require a **scope confirmation** (this session only). See Moment 5 — scope selector.

---

### Client detail

*What people go here to do:*

| Priority | Action | Source |
|----------|--------|--------|
| 1 | **Create new booking** for this client | All 3 clients — manual enrollment |
| 2 | **View all registrations** | All 3 clients — "where is this client enrolled?" |
| 3 | **Send email / message** | Kate, Anna |
| 4 | **View payment history** | Dom, Anna — "has this client paid?" |
| 5 | **Add internal note** | Kate |
| 6 | **Merge with duplicate** | Dom — same child, two registrations |
| 7 | **Transfer to different class** | Intercom ★★★ |

Intercom finding: "Ako pridať klienta manuálne?" (★★) — the flow exists but isn't obvious. "Create booking" from the client profile is the correct entry point.

---

### Design note

One `[Actions ▾]` button per detail screen. Orange, consistent placement (top-right of the content area, below the page header). On mobile: full-width at the bottom of the screen as a persistent bar.

This doesn't require new functionality — it's reorganising what already exists into the right place at the right time.

---

## Universal search

**Currently:** Search in Zooza is scoped per section — search clients in Clients, search bookings in Bookings. There's no cross-entity search.  
**What happens:** Users who know a client's name but don't remember where to find them have to navigate to the right section first. Users searching for a specific invoice, a transfer action, or a booking by reference number have no way to do it directly.

Dom: looked up a parent in GoCardless to verify what Zooza showed — because he couldn't find the payment by name quickly.  
Anna: asked Michal to find specific bookings for her multiple times.  
Intercom: "Kde nájdem faktúry?" (★★★), "Ako presunúť registráciu?" (★★★) — both are findability problems, not knowledge problems.

**Fix — Universal search bar (command palette pattern):**

A persistent search input, always visible in the top navigation. Searches across everything simultaneously:

```
🔍  Search...                                    [⌘K]
```

Results grouped by type:

```
🔍  "emma"

  CLIENTS
  → Emma Jackson  •  emma.jackson@example.com  •  2 active registrations

  BOOKINGS
  → Emma Jackson — Wiggle Wonders (0–12m)  •  £100 outstanding
  → Emma Hughes — Wiggle Wonders  •  Paid

  INVOICES
  → INV-0039 — Emma Jackson  •  £230  •  15 Jan 2026
```

**Action search — find what to do, not just what exists:**

Users can also search for *actions*:

```
🔍  "transfer"
  → Transfer booking...       move a registration to a different class
  → Transfer make-up...       move a make-up credit to another client
```

```
🔍  "refund"
  → Issue refund via Stripe   open Stripe for selected booking
```

This turns search into a navigation shortcut — the user types what they want to do, not where to click.

**Keyboard shortcut:** `⌘K` (Mac) / `Ctrl+K` (Windows) — standard for command palettes. Power users learn it fast; casual users use the visible search bar.

**Source:** Intercom KDE category = 35% of all support conversations. The majority are findability problems that a good search would eliminate entirely. Plus: "Ako presunúť registráciu?" (★★★), "Kde nájdem faktúry?" (★★★), "Kde zapnúť GoCardless?" (★★★) — all searchable.

**Effort:** Large (cross-entity search index + UI). But reduces ~35% of support volume permanently.

---

## Priority order

**Highest impact, least effort — ship first:**
1. Payment status badge (Moment 8)
2. Capacity message split — copy only (Moment 9)
3. Scope selector on edit — instructor / time / price (Moment 5)
4. "Groups" → "Classes" terminology sweep (Moment 6)
5. Nav hierarchy — Option A indent (Moment 2)
6. GoCardless expiry warning in payment detail

**High impact, medium effort — ship second:**
7. Contextual `[Actions ▾]` dropdown — per detail screen
8. Dashboard master Create panel (Moment 11)
9. Empty state onboarding checklist (Moment 1)
10. Financial column labels: Issued Debt → Total charged etc. (Moment 7)
11. Post-creation booking link prompt (Moment 10)

**Lower urgency — ship third:**
12. Programme form label improvements (Moment 3)
13. Class breadcrumb + price field labels (Moment 4)

**Large investment, high long-term payoff:**
14. Universal search / command palette — eliminates ~35% of support volume

**Requires new product functionality:**
- Term rebooking wizard (P5)
- Zooza-native refund flow (P3)
- Sibling discount automation (P8)
- Waitlist when class is full
- Admin-initiated trial creation (P9)
- Make-up sessions report by location (Intercom P1)

---

## What success looks like

A franchisee opens Zooza, creates a programme, adds a class, and shares the booking link — without asking support. That's it. That's the bar for franchise readiness.

Currently, none of the three clients reached this independently on Day 1. Most didn't reach it in 5 months.

The fixes above don't add features. They make what's already there understandable.

---

*Based on: Turtle Tots Dubai (Anna), babyballet Dubai (Kate), Wee Kicks (Dom)*  
*Compiled: 10 May 2026*
