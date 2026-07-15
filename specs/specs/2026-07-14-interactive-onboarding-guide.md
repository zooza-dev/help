---
spec_id: HLP-20260714-001
title: "Interactive visual onboarding guide + per-client personalization"
status: spec
created: 2026-07-14
updated: 2026-07-14
author: "help"
owner: "help"
last_verified: 2026-07-14
project_type: other
depends_on: []
related_handoffs: []
tags: ["onboarding", "guide", "docusaurus", "ux", "region-switcher", "personalization"]
feature_branch: "feature/onboarding-guide"
changelog_version: ""
changelog_date: ""
docs_version: ""
docs_communicated: ""
---

## Goal

New Zooza operators get stuck at the very start: they don't know whether their business model fits Zooza, and once convinced, they don't know what to set up first or in what order. The help KB has accumulated *many* partial onboarding attempts and one real end-to-end walkthrough (`setup/getting-started-with-zooza`), but nothing that is (a) visually engaging, (b) ordered as a guided journey, and (c) reusable as a personalized starting point per client.

This spec unifies onboarding into a single **interactive, visual, motion-enabled guide** in the help KB, modeled on the proven Zooza-built `babyballet.fr/guide` layout. The generic guide becomes the canonical source of truth; individual clients (first: **YTA**) receive a short personalized email that deep-links into it, highlighting the client's specific model. This kills the duplication, gives sales a repeatable onboarding asset, and lets operators self-serve setup step by step.

## Scope

**In scope**
- A single canonical interactive guide page in the help KB, unifying and replacing the narrative of `setup/getting-started-with-zooza` (which is fixed, not deleted — see redirects).
- Babyballet-style structure: Parent Journey → Data Model → Step-by-step Setup (expandable, each step = "open in Zooza" deep-link + link to the existing deep article) → Confirm-before-build checklist → **Publish & Go-Live (how the offer reaches clients)** → Managing the Week → Daily Business → Integrations & Later → Support.
- **Publish & Go-Live layer** — a dedicated block answering the most-asked onboarding question: "setup is done, how does this actually reach my clients/parents?" Covers: fully customizable on the client's own website; Zooza generative demo site for testing (`/zooza-client-site`); Zooza-hosted booking page (`yourbrand.zooza.online`) and Zooza Sites; and the six embeddable widgets — per-product **registration** form (one form per product subpage, scoped by course/class/venue), **calendar** of activities, venue **map**, **checkout/order** form for products & services, **video** playback, and **profile/parent-zone**. Each with: what the parent experiences, how it embeds, and an editable link out to `docs.zooza.online`.
- **Visual/motion layer**: custom Docusaurus components (stepper, expandable steps, region switcher, progress, cards) + SVG illustrations (data-model diagram, parent-journey flow, step icons) + CSS motion (scroll-reveal, transitions). Mermaid where a diagram suffices.
- **Region switcher** at the top that rewrites every `zooza.app` deep-link across the page: Europe (no prefix), UK (`uk.`), Asia (`asia.`). This is a NEW convention — none exists in the KB today.
- **Terminology clarity**: guide explicitly separates *Membership* (ongoing recurring, no end) from *kurzovné / term-instalment* (fixed total split into instalments across a billing period). Aligned to master glossary.
- **Per-client personalization**: a short personalized email template + entry that deep-links into the generic guide and foregrounds the client's model. First instance: YTA (kurzovné model, product 9356).
- **Phase 1 output = an HTML Artifact visual mockup** (Zooza-branded) so the visual direction is approved before Docusaurus component engineering begins.
- Fix `setup/getting-started-with-zooza`: duplicated section 8, broken link to non-existent `business-models/business-models.md`.

**Out of scope**
- Writing new deep articles for individual setup steps — every step already has an article; the guide orchestrates and links to them. (Confirmed by content survey.)
- Changing the app UI, API, or MCP behavior. Deep-links point at existing app screens.
- A full branded per-client microsite per client (that path via `/zooza-client-site` is deferred — this spec uses the lightweight email + shared generic guide).
- Non-English guide variants (KB is English-only per project rules; SK/other keyword variants stay in terminology.yml).

## Approach

Written from the perspective of the help KB / its Docusaurus export only.

1. **Reconcile the canonical spine.** Take `setup/getting-started-with-zooza` as the base, fix its bugs, and restructure its narrative to the babyballet 8-block journey. Keep the slug (SEO) or redirect if renamed.
2. **Build the interactive shell.** Wire custom React/MDX components into `scripts/export/build_docusaurus.py` (they are not wired today): `RegionSwitcher`, `SetupStep` (expandable, deep-link + article-link), `JourneyFlow` (SVG), `DataModelDiagram` (SVG), `ConfirmChecklist`. Port/adapt the `AiPrompt` component from `../Documents/GitHub/api-docs/src/components/AiPrompt` for the AI-assistant step.
3. **Region switcher.** A single control that stores the chosen region and rewrites all app deep-links (`{region}.zooza.app` where europe = empty prefix). Document the convention so future articles reuse it.
4. **Deep-link + article-link matrix.** For each setup step, source the exact app URL from the user's brief and the exact click-path/help-article from the existing KB article (never re-derive UI paths — verify against the article).
5. **Terminology gate.** Resolve membership vs kurzovné against the master glossary before writing pricing copy; reflect the distinction in the pricing step and link to the relevant business-model guide.
6. **Personalization layer.** Template the YTA email (based on the user's draft) + a minimal personalized entry that deep-links into the generic guide with the client's model highlighted.
7. **Ship via the standard pre-export pipeline** (seo_check → validate → export_all), plus redirects for any moved slugs.

## Acceptance Criteria

- [ ] Generic guide page exists in `content/`, structured as the 8 babyballet-style blocks, with valid frontmatter + `related_articles`.
- [ ] Every setup step in the guide has both a working "open in Zooza" deep-link AND a link to the corresponding existing deep article; no step links to a non-existent article.
- [ ] Region switcher works: selecting Europe / UK / Asia rewrites every app deep-link on the page accordingly (europe = no prefix).
- [ ] The guide clearly distinguishes Membership from kurzovné/term-instalment, consistent with the master glossary; no conflation.
- [ ] `setup/getting-started-with-zooza` bugs fixed (no duplicated section 8; no broken `business-models/business-models.md` link) and reconciled with / redirected to the new guide.
- [ ] An approved HTML Artifact visual mockup exists and matches the shipped layout direction.
- [ ] Custom components render in the Docusaurus export build without breaking `build_docusaurus.py` or the Cloudflare/MDX build (no raw `{braces}`/`<tags>` leakage).
- [ ] The Publish & Go-Live block accurately describes all six widgets + Zooza-hosted page + demo-site path, each with parent experience + embed method + editable docs link; region-correct embed hosts (`api`/`uk.api`/`asia.api`.zooza.app); no invented capabilities (respects the documented gaps).
- [ ] A personalized YTA email + entry exists that deep-links into the guide and foregrounds the kurzovné model.
- [ ] `seo_check.py`, `validate_kb.py` pass; redirects added for any changed slugs.

## Project Context

**project_type**: static-knowledge-base (help KB → Docusaurus export). Source of truth is `content/` (English-only). Do not hand-edit `build/`. Live site builds via Docusaurus/MDX on Cloudflare — raw `{}`/`<>` break the build and are not caught by seo_check/validate ([[project_mdx_build_constraints]]).

**Reference layout**: `babyballet.fr/guide` — already a Zooza-built artifact of this exact format. Blocks: Journey, Data Model, Setup (11 expandable steps w/ open-in-Zooza + help links), Confirm checklist, Managing the Week, Daily Business, Integrations & Later, Support.

**Existing assets to unify around (from content survey — do not duplicate):**
- Canonical walkthrough: `setup/getting-started-with-zooza` (has bugs to fix).
- Hubs: `business-models/index` (model decision tree), `reference/app-navigation-map`, `guides/where-to-find`, `setup/integrations-hub`.
- Data model: `guides/programme-class-session-definition`, `glossary/`.
- Every setup step already has a deep article (places, billing-periods, custom-holidays, trainers, pricing, groups, inbound-payments/email-parser, gateways, templates, makeup, consents, trials, discounts, referral, google-reviews, notifications, dashboard, team, invoice-profiles, MCP/`setup/claude-plugin`).

**Canonical data model (MCP `explain_data_model`, authoritative):**
- Programme (API: Course) → Class (API: Schedule; SK "skupina") → Session (API: Event; SK "termín").
- Class holds Bookings (API: Registration). Booking × Session → Attendance. Booking → Credit (make-up entitlement).
- User = person holding consents, usually related to a child. Booking = order for a service; Orders = products (merch/digital/videos).
- Programme is configured mostly once; Classes/groups are added repeatedly.

**Programme types (glossary `programme-types`):** One-off Event, Pay-as-you-go (canonical for "open course"/drop-in), Membership (ongoing recurring), 1-to-1. NOTE: user's "kurzovné/členské" = fixed total split into instalments over a billing period → this is the block/term-instalment pricing model, NOT Membership. Guide must not conflate. See [[project_terminology_decisions]] and [[feedback_kb_framing]].

**Region deep-link convention (NEW):** App: Europe = `zooza.app` (no prefix), UK = `uk.zooza.app`, Asia = `asia.zooza.app`. Embed/API host (confirmed in widget docs): Europe `api.zooza.app`, UK `uk.api.zooza.app`, Asia/UAE `asia.api.zooza.app` (set via `data-zooza-api-url`). No prior convention in KB. Region switcher owns both.

**Distribution & publishing (go-live) layer — grounded in docs.zooza.online widgets + help KB embed articles:**
- **Embed model:** six widget types, embedded via WordPress plugin / Wix / manual `<script data-widget-id='zooza'>` snippet / official npm packages (`@zooza/widgets-react|vue|svelte|wc|core`). One widget per page (hard rule). Each widget must be told its own page URL in `Publish > Widget` so Zooza cross-redirects parents (map→registration, profile→checkout, calendar→registration). CSS/branding is website-side (`Use CSS` toggle + downloadable defaults).
- **Registration widget** (`type=registration`, v1) — the per-product form. Unlimited instances, each scoped to one programme/class/venue via `course_id` / `schedule_id` / `place_id` (or `filter_courses`, `labels_in/not_in`, `metadata_in/not_in`). Per-programme no-code scoping in `Programmes → Online Booking`. This is the "each product subpage has its own form" mechanism. Docs: `docs/widgets/registration-widget.md`, `guides/customizing-widgets`, `faq/booking-widget-faq`, `setup/online-registration`.
- **Calendar widget** (`type=calendar`, v2) — activities/sessions view (week or dated), filters by location/course/type/instructor, click-through to info/registration. Can import external sessions via `zooza_events`. Docs: `docs/widgets/calendar-widget.md`.
- **Map widget** (`type=map`, v2) — venue/branch map; parent searches by address/ZIP + radius, pin → location classes → registration. Admin toggles only. Docs: `docs/widgets/map-widget.md`.
- **Checkout widget** (`type=checkout`, v2) — order form for products & services (videos/eBooks, coupons, entry vouchers). Products can also sell inside the registration flow. Docs: `docs/widgets/checkout-widget.md`, `guides/selling-products-during-booking`, `guides/creating-entry-passes`.
- **Video widget** (`type=video`, v2) — secure playback for logged-in entitled users; videos hosted on Vimeo/other, Zooza gates access. Docs: `docs/widgets/video-widget.md`, `guides/embedded-videos-vimeo`.
- **Profile widget = Parent Zone** (`type=profile`, v1) — members-only portal: booking/order history, pay outstanding, cancel/book make-ups, purchased videos, session documents. Docs: `docs/widgets/profile-widget.md`, `docs/widgets/event-documents.md`.
- **Zooza-hosted routes (no embed needed):** public booking page `yourbrand.zooza.online/booking/` (deep-link via `?course_id=&schedule_id=&place_id=`; private "Copy link" for hidden classes); **Zooza Sites** full hosted website product (`setup/zooza-sites`); **generative demo site** via `/zooza-client-site` skill (landing + `/booking/` + `/parent-zone/`, for brand-testing before the client embeds — this is tooling, not a customer feature; deferred as a per-client deliverable).
- **Editable docs links:** KB→`docs.zooza.online` handoff pattern + `AiPrompt` prompt blocks (Open-in-ChatGPT/Claude, pointing at `docs.zooza.online/llms-full.txt`).
- **Documented gaps to respect (do NOT overclaim):** checkout/map/video widgets have no documented per-embed filter params; `framework-modules` npm reference page is not yet merged (only in `setup/deploying-zooza-on-website`); UAE/Asia under-covered outside raw snippet tables; `guides/widget-merge-rooms` is archived (content merged into `guides/customizing-widgets`); several `<!-- REVIEW -->` specifics in `customizing-widgets` are unconfirmed.

**App deep-links from user brief (Europe/no-prefix shown; switcher rewrites host):**
- Places `#settings/places` · Billing periods `#settings/billing_periods` · Custom holidays `#settings/custom_holidays` · Programmes/courses `#courses` · Calendar `#calendar` · Integrations `#integrations` · Email templates `#communication/templates` · Replacements `#settings/replacements` · Consents `#settings/consents` · Discounts `#payments/discounts` · Payment settings/templates `#settings/payment_settings` · Referral `#payments/loyalty` · Google Reviews `#feedback/reviews` · Notifications `#settings/notifications` · Dashboard `#` · Team `#settings/team` · Invoice profiles `#settings/invoice_profiles` · Inbound payments setup `#payments/inbound/setup?invoice_profile=0` · MCP `#mcp` · YTA product `#courses/9356`.

**Visual capability (Docusaurus help export):** preset-classic v3.9.x, MDX/JSX supported, mermaid enabled, admonitions styled — but custom React components NOT yet wired into the export scaffold. Portable `AiPrompt` component (with Open-in-ChatGPT / Open-in-Claude) lives in `../Documents/GitHub/api-docs`. Building the visual layer = adding `src/components` to the generated scaffold.

**Verified product facts (owner-confirmed 2026-07-15 during mockup review — treat as authoritative, but still cite help articles when publishing):**
- **Terminology:** public English content uses **"Term Fee"** — never the Slovak "kurzovné" ([[feedback_language_variants]]).
- **Membership** is NOT "forever/until cancel" — it bills recurring **for as long as the class/group has scheduled sessions** (no target total). Term Fee = one known total split into instalments that stop at term end. Keep these two distinct.
- **Billing period date range is OPTIONAL.** If omitted, it just frames the term. If set, Zooza uses the range to assist session generation (keeps sessions within it).
- **Getting paid is a fork, combinable:** (a) **payment gateway only (e.g. Stripe)** → NO bank pairing needed; Zooza tracks payments directly from the gateway. (b) **bank transfers** → automate via the email parser (forward bank notifications → matched by variable symbol) or **GoCardless** direct debit. (c) both together. This is why some accounts have no bank connected — by design.
- **Email template sequence (ongoing programmes):** `registration_confirmation` ("Confirm") is the FIRST email after registering — the client verifies email + contact; THEN `registration_done` ("Enrolment welcome"). Trial templates (`registration_trial_done`/`_ended`/`_followup`/`_lost`) only fire if trials are enabled. Also flag session reminders `event_notification`. The shown set is for **ongoing classes / full programmes** — **one-off events** and **pay-as-you-go** have their own template sets.
- **Publish / hosted site:** the Zooza-hosted mini-site (for clients with no website) is **`zooza.site/youraccountname`** (UK: **`zooza.site/uk/youraccountname`**), configured in the app at **`#widgets`** — NOT `yourbrand.zooza.online`. (The per-programme public booking page is a separate shareable link.) Widgets are all configured under `#widgets`.
- **Business-model overview belongs at the START** of the guide — a grid of the concrete model guides (children block/subscription, adult language school, 1-to-1, camps, drop-in, online/hybrid, franchise) each linking to its help walkthrough, plus the "Find your setup" decision hub.

**Placement:** lives in the help KB as its own standalone page (owner: "watch the design there"). Region switcher is an in-content component/control on that page. Slug TBD (`onboarding-guide` vs keeping `getting-started`).

**Mockup status:** interactive HTML Artifact built + iterated to v2 (owner: "páči sa mi to"). Reference for Phase 2 component build. Scratchpad: `onboarding-guide-mockup.html`.

**Proposed phasing:**
- **Phase 1 — IA + visual direction:** finalize the 8-block structure, deep-link/article matrix, terminology gate, and produce an approved HTML Artifact mockup (Zooza orange, motion). Fix getting-started bugs.
- **Phase 2 — Build interactive guide:** components (RegionSwitcher, SetupStep, JourneyFlow, DataModelDiagram, ConfirmChecklist), SVG graphics, wire into `build_docusaurus.py`, write the canonical content page.
- **Phase 3 — Personalization + YTA:** personalized email template + entry; ship YTA instance; redirects; pre-export pipeline; verify build.

**Personalization brief (YTA):** Jozef @ YTA, product `#courses/9356`. Model = kurzovné (split final sum into monthly instalments). Email covers: learn to set up their own classes, test registration as a parent, tailor email confirmations, connect bank via email parser (Tatra Banka → generated parse address; variable symbol auto-matches), build a few groups with sessions, view in calendar, optionally connect Claude/ChatGPT via `#mcp`. Draft exists in the user's brief.

## Notes

- RESOLVED (owner): rename canonical page `getting-started-with-zooza` → `onboarding-guide` (owner confirms old slug not meaningfully indexed). Still add a redirect from the old slug — near-zero cost, protects any inbound links.
- Open question: does the visual layer live as one big MDX page with components, or a swizzled/custom Docusaurus page? Mockup will inform this.
- Verify all click-paths against existing articles before publishing ([[feedback_no_unverified_facts]]).
- RESOLVED: babyballet guide source EXISTS at `../zooza_projects/babyballet-web/src/pages/guide.astro` (Astro, 300 lines) — the canonical reference layout. A second instance exists at `../zooza_projects/magikats/guide/index.html`. Brand/UX rules in `../zooza_projects/babyballet-web/docs/ux-guide.md`. **Reuse this real content/structure; generify from babyballet pink/blue → Zooza orange and add the two new blocks (region switcher, Publish & Go-Live) that the single-client version lacks.** Reference structure: sticky TOC · tip banner · Journey (6 numbered stages) · Data model (Programme›Class›Session cards + Client vs Booking) · Setup accordion (each step: desc + open-in-Zooza + help link) · Confirm checklist (localStorage) · Managing the week (Calendar vs class schedules) · Daily business · Integrations & later · Support (book-a-meeting + "bring the business problem"). Help links use `help.zooza.online/<area>/<slug>/` (no `/help/` prefix).
- Cross-repo: if the region-switcher convention or any deep-link needs app-side confirmation (exact hosts per region), raise a handoff before hard-coding. Embed/API hosts already confirmed from widget docs (`api`/`uk.api`/`asia.api`).
- Phase-1 generic additions over the babyballet reference: (1) a "does my business model fit?" intro + course-type explainer (One-off / Pay-as-you-go / Membership / kurzovné-instalments), (2) region switcher, (3) Publish & Go-Live block.

**Phase 2 delivery (2026-07-15) — DONE, build verified:**
- Delivery approach **A** chosen (recon-backed): the guide ships as a **standalone React page** at **`/onboarding-guide/`**, NOT a markdown content article — so its `<details>`, region switcher and localStorage never touch the MDX compiler (zero brace/tag break risk). Source lives as real files at `scripts/export/pages/onboarding-guide/{index.jsx,styles.css}`; `build_docusaurus.py` copies every subdir of `scripts/export/pages/` into the scaffold's `src/pages/` (new `PAGES_SRC_DIR` + copy loop in `_write_custom_css`). A "Get started" navbar item was added.
- All links use the **real verified slugs** (39/39 resolved, no gaps) — corrected from mockup guesses: `creating-a-class`→`/classes/`, `message-templates`→`/communication/`, `franchise-network`→`/settings/`, make-up→`replacement-hours-complete`, auto-enrolment→`/programmes/auto-enrollment/`. Region switcher rewrites app + embed API hosts; theme follows Docusaurus `[data-theme]`; SSR renders full content into static HTML (SEO/AI-crawler friendly).
- **Verified:** `npm run build` compiles clean; `dist/onboarding-guide/index.html` (39 KB) generated with expected content.
- **getting-started reconciliation — DONE (2026-07-15):** removed the misplaced duplicate §8 (order was 6→8→7→8, now 6→7→8), fixed the broken `business-models/business-models.md` link (→ `/programmes/business-models/`; note: linking `index.md` does NOT resolve in this pipeline — use the absolute area path), added a top callout pointing to the interactive `/onboarding-guide/`, added `related_articles`. Kept as the detailed written reference (not deleted/redirected — Cloudflare Pages ignores `.htaccess`, so a true redirect would need `@docusaurus/plugin-client-redirects`). Verified: `npm run build` reports **no broken links**; `seo_check` PASS (0 errors); the pre-existing `validate_kb` FAIL is unrelated (missing images + other files' broken links) and my file is not in the report.
- **Remaining follow-ups:** (a) optional real screenshots/illustrations for more "grafika". (b) Phase 3: YTA personalized email deep-linking into `/onboarding-guide/` (owner: do together). (c) before public launch, decide whether getting-started should 301 → onboarding-guide via the client-redirects plugin.
