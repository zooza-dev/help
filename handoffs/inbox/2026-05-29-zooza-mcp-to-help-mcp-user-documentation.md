---
handoff_id: zooza-mcp-to-help-20260529-001
from: zooza-mcp
to: help
status: in_progress
created: 2026-05-29
updated: 2026-05-29
related_specs: []
related_handoffs: []
tags: [mcp, plugin, claude, documentation]
---

## Request

### What we need

A user-facing help article (or article series) on help.zooza.online that explains:
1. What the Zooza Claude plugin and MCP server is and who it's for
2. How to connect it (Claude.ai, Claude Code)
3. What users can do with it — with concrete example prompts
4. How the guided skills work
5. FAQ / troubleshooting basics

### Why we need it

The Zooza MCP server and Claude plugin have been submitted to the Anthropic marketplace and MCP connector directory. Users who find the plugin will look for documentation on help.zooza.online. Without it, they have no onboarding support.

Additionally, the submission forms (Claude connector directory) ask for a homepage URL — we're using `https://zooza.online/mcp` as a placeholder landing page (separate handoff), and `help.zooza.online` articles will be linked from there.

### Constraints from our side

- The plugin connects only to **active Zooza accounts** — document this as a prerequisite
- Auth is via **OAuth** (same login as zooza.app) — no separate password
- Currently works with **Claude.ai and Claude Code** — ChatGPT support is coming (do not document ChatGPT yet)
- Terminology: the MCP server adapts to the user's own vocabulary (hodina/session, kurz/programme) — this is a feature worth highlighting
- Screenshots available: `plugin/media/` in the zooza-mcp private repo — contact Michal for access

### How we imagine it — open to challenge

One main article: *"Zooza pre Claude — ako pripojiť a čo vieš robiť"*
With these sub-sections, or split into multiple articles if help team prefers:
- Čo je Zooza plugin pre Claude
- Ako sa pripojiť
- Čo vieš spraviť (use cases + example prompts)
- Skilly — čo sú a ako fungujú
- FAQ

---

## Full content for the documentation team

Everything below is source material — use, adapt, translate as needed.

---

### Čo je Zooza plugin pre Claude

Zooza plugin prepája Claude (AI asistenta od Anthropic) s tvojim Zooza účtom. Namiesto prepínania medzi tabmi môžeš spravovať triedy, rozvrhy a dochádzku cez jednoduchú konverzáciu.

Plugin je dostupný pre Claude Code (terminál) aj Claude.ai (Cowork). Funguje v akomkoľvek jazyku ktorý Claude podporuje.

---

### Ako sa pripojiť

**Možnosť A — Plugin pre Claude Code / Cowork**

1. Stiahni plugin zo stránky:
   `https://github.com/zooza-dev/zooza-mcp-server/releases/latest`
2. Nainštaluj: `claude plugin install zooza-plugin-vX.Y.Z.zip`
   alebo nahraj v Cowork: Customize → Browse plugins → upload
3. Plugin aktivuj v nastaveniach
4. Prihlás sa svojím Zooza účtom (OAuth — rovnaké prihlásenie ako zooza.app)

**Možnosť B — Manuálne pripojenie v Claude.ai**

1. Otvor claude.ai → Settings → Connectors
2. Pridaj nový server:
   - Name: `Zooza`
   - URL: `https://mcp.zooza.app/mcp`
3. Prihlás sa svojím Zooza účtom

**Požiadavky:**
- Aktívny Zooza účet (zooza.app)
- Admin prístup v danej spoločnosti
- Dostupné vo všetkých regiónoch kde Zooza funguje (SK, CZ, HU, RO a ďalšie)

---

### Čo vieš spraviť — príklady

**Zobraziť programy a skupiny**
> *"Ukáž mi všetky moje aktívne programy a koľko skupín každý má"*
> *"Show me all my active programmes"*

**Vytvoriť novú triedu**
> *"Chcem vytvoriť novú skupinu — pondelky o 9:00, jóga, Studio Bratislava"*
> *"Create a new Monday morning yoga class at 9am"*

Claude sa opýta na chýbajúce detaily (program, tréner, miesto, počet lekcií), ukáže náhľad rozvrhu a počká na potvrdenie pred uložením.

**Označiť dochádzku**
> *"Označ dochádzku na dnešnej 10:00 hodine tanca — Peter a Sofia chýbali"*
> *"Mark attendance for today's 10am dance class — Peter and Sofia were absent"*

**Pridať poznámku k termínu**
> *"Pridaj zhrnutie k dnešnej hodine: pracovali sme na dýchaní, prišlo 8 žiakov"*
> *"Add a summary to today's beginner yoga session: focused on breathing, 8 students attended"*

**Nastaviť slovník**
> *"Nauč sa moje výrazy — ja hovorím 'hodiny' nie 'sessions' a 'kurzy' nie 'programmes'"*

Claude si zapamätá tvoje výrazy na ďalšie konverzácie.

**Prehľad pobočiek / franšízy**
> *"V ktorej spoločnosti pracujem a aké mám k dispozícii?"*
> *"Who am I in Zooza and which company am I working in?"*

---

### Skilly — čo sú a ako fungujú

Skilly sú sprievodcovia pre zložitejšie operácie. Namiesto jednej otázky a odpovede Claude vedie štruktúrovaný rozhovor — pýta sa otázky po jednej, kontroluje vstupy a ukáže náhľad pred finálnym uložením.

**Dostupné skilly:**

| Skill | Ako spustiť | Čo robí |
|---|---|---|
| Vytvorenie triedy | `/class-management` alebo *"Chcem vytvoriť novú triedu"* | Prevedie celým procesom: program → miesto → tréner → rozvrh → náhľad → potvrdenie |
| Nastavenie slovníka | `/zooza-setup` alebo *"Nastav môj slovník"* | Naučí Claudea tvoje výrazy — zapamätá si ich |
| Odoslanie spätnej väzby | *"Chcem nahlásiť bug"* | Pošle správu priamo Zooza tímu |

---

### Náhľad pred uložením

Pri vytváraní triedy Claude vždy ukáže tabuľku plánovaných termínov **pred tým** než čokoľvek uloží. Môžeš skontrolovať dátumy, časy a trénerov — a ak niečo nesedí, povedz to a Claude upraví.

Uloženie prebehne až po tvojom výslovnom potvrdení.

---

### Funguje vo viacerých jazykoch

Claude odpovedá v jazyku v ktorom sa ho opýtaš — po slovensky, česky, maďarsky, rumunsky, anglicky. Dáta zo Zooza sa zobrazia v jazyku nastaveného účtu.

---

### FAQ

**Musím platiť niečo navyše?**
Nie. Plugin je dostupný zadarmo pre všetkých aktívnych Zooza zákazníkov. Potrebuješ iba Claude účet (claude.ai má bezplatnú vrstvu).

**Je to bezpečné? Kde sú moje údaje?**
Plugin neuchováva žiadne prihlasovacie údaje. Prihlasovanie prebieha cez OAuth — rovnaký systém ako keď sa prihlasovateľ do zooza.app. Claude vidí len dáta ktoré mu Zooza cez plugin poskytne.

**Funguje aj pre franšízy s viacerými pobočkami?**
Áno. Ak má tvoj účet prístup k viacerým spoločnostiam, Claude ich vypíše a opýta sa ťa s ktorou chceš pracovať. Môžeš prepínať v rámci jedného chatu.

**Nefunguje mi pripojenie — čo mám robiť?**
1. Over že máš aktívny Zooza účet s admin prístupom
2. Skús sa odhlásiť a znovu prihlásiť cez OAuth
3. Ak problém pretrváva, kontaktuj support@zooza.online

---

### Screenshoty (dostupné)

Súbory sú v privátnom repe `zooza-mcp` v priečinku `plugin/media/`. Kontaktuj Michala pre prístup.

| Súbor | Čo ukazuje |
|---|---|
| `screenshot-01-programmes.jpg` | Zoznam programov a kurzov |
| `screenshot-02-create-class.jpg` | Interview pri vytváraní triedy |
| `screenshot-03-schedule-preview.jpg` | Náhľad rozvrhu pred uložením |
| `screenshot-04-vocabulary.jpg` | Nastavenie slovníka |
| `screenshot-05-whoami.jpg` | Prehľad účtu a schopností |
| `demo-create-class.webm` | Video: vytvorenie triedy end-to-end |

---

## Discussion

### 2026-05-29 — help

Created two articles under a new **MCP** product area category, which maps to `help.zooza.online/category/mcp/` as requested:

- `help.zooza.online/mcp/claude-plugin/` — main setup guide (connection methods, use cases, skills, preview, multi-language)
- `help.zooza.online/mcp/claude-plugin-faq/` — FAQ (pricing, security, franchise, troubleshooting)

The integrations hub (`/settings/integrations-hub/`) now has an **AI** section linking to the plugin article.

**Pending:** Screenshots from `plugin/media/` in the zooza-mcp repo. Both articles have `needs_screenshot_replacement: true`. Please provide access or send the image files so they can be added before the articles go live.

**Not documented yet:** ChatGPT support (per constraint — will add a separate article when ChatGPT integration ships).

---

## Decision Summary
*(vyplní sa po dohode)*

---

## Resolution
*(vyplní sa po zverejnení dokumentácie)*
**Resolved on:**
**Published URL(s):**
