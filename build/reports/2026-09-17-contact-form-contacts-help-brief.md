# Zadanie: Contact form + Contacts (lead capture) v helpe

Dátum: 2026-09-17
Stav: návrh na schválenie, články ešte nepísané

## Čo je vonku (overené v špecifikáciách, všetko `implemented` na `main`)

Zdroje: `app/specs/implemented/2026-09-14-lead-capture-*.md` (9 specov),
`api-v1/specs/implemented/2026-09-14-contacts-core.md`, `…-public-contact-capture.md`,
`…-contact-notifications.md`, `2026-09-15-contact-widget-type-default-configuration.md`,
`2026-09-15-contact-team-work-followups.md`, `widgets-v1/specs/implemented/2026-09-14-lead-capture-contact-widget.md`,
`2026-09-16-contact-widget-analytics-tracking.md`, api-docs `docs/widgets/contact-widget.md`.
Changelog entry je na API umbrella spece (`2026.09`, headline „Turn website enquiries into contacts you can follow up in Zooza“).

### Kde to v aplikácii je

| Obrazovka | Cesta | Práva |
|---|---|---|
| Contacts (zoznam + detail) | Clients → Contacts | view `get_user`, edit `edit_user` |
| Contact forms (konfigurácie) | Team & Settings → General → Contact forms | `edit_company` |
| Custom contact fields | Team & Settings → General → Custom contact fields | `edit_company` |
| Contact form widget (URL, konfigurácia, additional domains, CSS, embed) | Team & Settings → Publish → Widget → Contact form | `edit_company` |
| Consents pre formulár (`for = Contact form`, kategórie) | Team & Settings → General → Consents & Agreements | `manage_places` |
| Notifikácia „new contact enquiry“ | Notification center | |
| Šablóna automatickej odpovede (`Default automatic reply` + varianty) | Communication → Templates | |

### Čo to dokáže

- **Formulár:** štandardné polia first name / surname / email / phone / message, každé enabled + required. Email alebo phone musí byť zapnuté a povinné (guard v UI). Vlastné polia 7 typov (short text, long text, number, date, yes/no, single choice, multiple choice). Skryté polia s hodnotou z URL parametra, cookie, embed atribútu (`data-zooza-field-<name>`) alebo pevnej hodnoty.
- **Konfigurácie:** firma má vždy jednu default konfiguráciu (nedá sa archivovať). Ďalšie konfigurácie sa dajú vytvoriť a priradiť widgetu alebo vložiť cez `data-zooza-config-id`. Poradie: embed atribút → konfigurácia vybraná na widgete → default.
- **Súhlasy:** platformové Zooza súhlasy sú vždy; firemné súhlasy s `for = Contact form` sa zapínajú per konfigurácia. Súhlas má kategóriu (general / terms / privacy / marketing / media). Aspoň jeden prijatý súhlas kategórie marketing = `Marketing consent: Yes` na kontakte.
- **Po odoslaní:** správa alebo redirect na URL.
- **Handling:** default owner, labels, extra notifikačné emaily, auto to-do (owner alebo konkrétny človek, max jedno otvorené per kontakt), automatická odpoveď (max 1× za 24 h per kontakt; obsahuje len krstné meno a názov formulára, nikdy text správy).
- **Visitor tracking:** page URL, referrer, utm_* (5), fbclid, gclid. Voliteľne „Remember where the visitor first came from“ (localStorage, first-touch wins, 1–90 dní, default 30, vyžaduje cookie consent na strane webu).
- **Analytics eventy** do GTM dataLayer / gtag / Meta Pixel (trackCustom): `zooza_event_contact_form_view`, `…_submit_start`, `…_submitted` (konverzia). Bez PII, s `zooza_contact_form_id`.
- **Spam:** neviditeľný (token, min. 3 s, proof-of-work, honeypot, obsahová heuristika, rate limity). Žiadna CAPTCHA. Spam dostane rovnakú „ďakujeme“ správu, nikdy sa nestane kontaktom. Contacts → **Spam** zoznam s „Not spam“ záchranou. Staff môže označiť enquiry ako spam z detailu. Spam sa maže po 30 dňoch.
- **Kontakty:** dedup podľa emailu (case-insensitive), ak email chýba tak podľa telefónu. Opakované enquiry = ďalší záznam v timeline toho istého kontaktu; nové hodnoty len dopĺňajú prázdne, nikdy neprepisujú. Status new / in progress / lost; converted len cez convert alebo auto-link. Owner, labels, notes, to-dos (tímové – kolega môže zavrieť cudzie to-do na kontakte), timeline (enquiry so všetkými odpoveďami, stránkou, kampaňou, súhlasmi; poznámky; systémové udalosti).
- **Kontakt ≠ klient.** Nikdy sa nezobrazí v zozname klientov. Ak email patrí existujúcemu klientovi firmy → automaticky linked („Existing client“). Convert to client vytvorí klienta (bez emailu klientovi). Ak sa kontakt sám zaregistruje cez booking widget s tým istým emailom → automaticky converted. Na profile klienta je karta s jeho kontaktnými záznamami.
- **Manuálne pridanie kontaktu** (Add contact: meno, email alebo telefón).
- **Real-time toast** „New enquiry / Another enquiry“ pre staff s `get_user`.
- **Liveness formulára:** Never seen / Loading, no enquiries yet / Receiving / Blocked domain (s tlačidlom „Allow {host}“, ktoré pridá doménu do widgetu).
- **Erase contact** = tvrdé GDPR zmazanie (submissions, notes, labels). To-dos ostanú.
- **Embed:** iba placeholder + loader (body only / head + body). Jeden formulár na stránku (druhý ukáže inline notice). WordPress shortcode `[zooza]` ho nepodporuje → Custom HTML blok. Doména: doména widgetu + doména URL + additional domains, subdomény automaticky. Štýlovanie cez `--zooza-*` CSS premenné, `zooza-contact-*` triedy, `data-status`.
- **Regióny:** loader host podľa regiónu (api / uk.api / asia.api).

### Čo NIE je vonku (nepísať ako dostupné)

- Meta Lead Ads (instant forms → Zooza), Custom Audiences, Conversions API – iba `idea` (API-20260914-010). Shipnuté je len: UTM/fbclid atribúcia + Pixel custom eventy + marketing consent kategória.
- CSV export kontaktov, bulk akcie, náhľad formulára v appke, viac formulárov na jednej stránke, zmena default konfigurácie, obnovenie archivovaného custom fieldu, zlúčenie dvoch kontaktov, filter podľa long text poľa.
- Kontakt sa nedá pridať do skupiny/kurzu priamo – najprv Convert to client, potom bežná registrácia.

## Terminológia (rozhodnúť)

V UI sa slovo „lead“ nepoužíva. UI hovorí **Contacts**, **Contact form**, **Custom contact fields**, **enquiry**. V helpe už „Lead collection“ znamená triedu bez termínov (`guides/lead-collection.md`, terminology.yml `lead-collection`). Návrh:

- Kanonicky: **contact form**, **contact**, **enquiry** (jedno odoslanie), **contact form configuration**, **custom contact field**.
- „lead“, „lead form“, „lead capture“, „lead widget“, „kontaktný formulár“, „zber leadov“, „dopyt“ → iba `intent_keywords` v terminology.yml, nie do verejného textu.
- Do `lead-collection.md` pridať odsek „Not the same as the contact form“ a naopak.

## Navrhované články (7 nových)

Poradie = poradie čítania pre nového používateľa. Každý má use-case úvod, nie len návod.

1. **guides/contact-form-overview.md** — *„Capture website enquiries as contacts“* (Clients)
   Čo to rieši, pre koho, ako to zapadá (contact → client), 4 use cases, 5-krokový quick start s odkazmi na články 2–5. Tu je najviac „business“ textu.
2. **setup/contact-form-setup.md** — *„Set up a contact form“* (Settings)
   Default konfigurácia, štandardné polia + guard, custom fields (picker), hidden fields (4 zdroje, kedy ktorý), consents per konfigurácia + kategórie, visitor tracking, after submit, handling (owner, labels, also notify, to-do, auto reply + varianty šablóny), liveness karta, viac konfigurácií (kedy áno). Archivácia.
3. **setup/custom-contact-fields.md** — *„Custom contact fields“* (Settings)
   Krátky: registry, 7 typov, key/type nemenné, options value nemenné, archivácia namiesto mazania, ako sa podľa nich filtruje. (Alternatíva: sekcia v článku 2 – viď otázka 5.)
4. **setup/contact-form-on-your-website.md** — *„Put the contact form on your website“* (Widgets)
   Publish → Widget → Contact form (URL, konfigurácia, additional domains, staging/localhost, Use CSS), embed body only vs head + body, WordPress Custom HTML, jeden formulár na stránku, viac stránok s jednou konfiguráciou cez `data-zooza-field-…`, CSS premenné (základ, odkaz na docs.zooza.online pre celý zoznam), troubleshooting z liveness (Blocked domain, Never seen, „poslal som test a nič“ = spam heuristika).
5. **guides/working-with-contacts.md** — *„Work with contacts and enquiries“* (Clients)
   Zoznam a filtre (vrátane custom field a UTM filtrov), detail, status/owner, labels, notes, to-dos ako tímová práca, timeline, Link / Convert / auto-link / auto-convert, contacts card na profile klienta, Add contact, Spam review + Mark as spam, Erase, toast a emailová notifikácia (Reply-To = odosielateľ).
6. **guides/contact-form-campaign-tracking.md** — *„Track campaigns and conversions from the contact form“* (Widgets alebo Communication)
   Use-case: Meta/Google kampaň → landing page → enquiry. Čo sa ukladá (utm, fbclid, gclid, page, referrer), first-touch a kedy ho zapnúť, hidden field ako „kampaňová značka“ pre viac stránok, filtrovanie kontaktov podľa kampane, Pixel/GTM eventy a ako z `zooza_event_contact_form_submitted` spraviť Lead konverziu, marketing consent kategória a čo znamená. Jasne: Meta Lead Ads sync zatiaľ nie je.
7. **faq/contact-form-and-contacts-faq.md** (Clients)
   ~20 otázok: rozdiel contact vs client vs lead collection; prečo sa mi nezobrazil testovací dopyt; formulár sa nenačíta (doména); dva formuláre na stránke; WordPress; kto dostane email; prečo neprišla automatická odpoveď (24 h); môžem kontakt zapísať do kurzu; čo sa stane pri opakovanom odoslaní; export; GDPR zmazanie; kto vidí kontakty (inštruktor?); ako zmeniť „Send“ text; funguje na zooza.site; ako viem, z ktorej kampane prišiel; atď.

### Use cases do článku 1 (návrh textu, 1 odsek každý)

- **Platená kampaň bez zápisu do skupiny.** Meta/Google reklama vedie na stránku s formulárom „Mám záujem“. Rodič nechá meno + email/telefón + čo ho zaujíma (custom field). Tím vidí kontakt s kampaňou, zavolá, a až potom zapíše (Convert → registrácia).
- **Náhrada generického kontaktného formulára.** Dopyty z webu neskončia v schránke, ale v Zooze s owner-om, to-do a históriou. Odpovedať sa dá priamo z emailu (Reply-To).
- **Záujem o nový kurz / mesto / termín pred spustením.** Rýchlejšie a jednoduchšie než lead collection trieda: nie je nutný kurz ani programme. Keď je rozvrh hotový, Convert to client + booking. (Porovnanie kedy lead collection a kedy contact form.)
- **Jedna konfigurácia, viac lokalít alebo stránok.** Hidden field `location` cez embed atribút → filter kontaktov podľa lokality, alebo per-page owner cez samostatné konfigurácie.
- **Rýchlosť.** Minimum polí (email alebo telefón + meno), bez CAPTCHA, formulár je súčasťou stránky, načíta sa asynchrónne.

## Existujúce články na update

| Článok | Zmena |
|---|---|
| `reference/settings-hub.md` | riadky Custom contact fields, Contact forms |
| `setup/deploying-zooza-on-website.md` | odkaz na Contact form widget, poznámka WordPress |
| `guides/customizing-widgets.md` | sekcia Tracking conversions – doplniť contact eventy; Changing wording – `contact.*` kľúče |
| `setup/setting-gtc-gdpr-consents.md` | „For: Contact form“, kategórie súhlasov, prečo marketing kategória |
| `guides/notifications-center.md` | nový typ notifikácie |
| `guides/message-templates.md` | Contact form automatic reply + varianty, merge vars |
| `faq/todos-faq.md` | to-do na kontakte, tímové zatváranie |
| `guides/labels.md` | labels na kontaktoch |
| `guides/client-profile-101.md` | karta Contacts na profile |
| `guides/lead-collection.md` + `individual-sessions-lead-collection.md` | disambiguácia |
| `content/glossary/terminology.yml` + `glossary/index.md` | nové termíny + synonymá |
| `static/llms.txt` | nové články |
| spec `api-v1/…/2026-09-14-lead-capture-umbrella.md` | po publikovaní stamp `docs_communicated` |

## Screenshoty

Máme (ingest, Playfulmotion UK): formulár na webe, Contacts empty state + zoznam + Add contact, detail kontaktu (Lou Falle) + Convert dialóg, Contact forms zoznam, editor konfigurácie (celý + výrezy), Custom contact fields empty + New field modal + typ dropdown, Publish → Widget → Contact form.

Chýba (viem dokapturovať cez `kb:screenshots`, alebo dodáš): custom field so single choice options, konfigurácia s pridaným custom + hidden poľom, Spam zoznam, Consents & Agreements s „For: Contact form“ a kategóriou, Templates s automatickou odpoveďou, Notification center s novým typom, timeline s poznámkou + to-do + linked client, karta Contacts na profile klienta, email notifikácia staffu.

## Otvorené otázky (pred písaním)

1. **Názov v helpe:** „contact form“ + „contacts“ (ako v UI), „lead capture“ len ako synonymum? Alebo chceš „Lead capture“ ako marketingový názov modulu v nadpisoch?
2. **Dostupnosť:** všetky regióny a všetky plány? Nejaké obmedzenie počtu kontaktov/formulárov? Dátum releasu do changelogu (spec hovorí 2026.09).
3. **Meta:** potvrď, že píšeme len atribúciu + Pixel eventy. Meta Lead Ads sync nespomíname vôbec, alebo ako „pripravujeme“?
4. **Zooza Sites:** default URL widgetu je `zooza.site/{slug}/contact/`. Zobrazuje sa contact form na Zooza Sites automaticky? Neviem overiť zo specov.
5. **Custom contact fields:** samostatný krátky článok (má vlastnú obrazovku v Settings hube) alebo sekcia v „Set up a contact form“?
6. **Use cases:** sedia tie štyri vyššie? Máš konkrétneho klienta/segment (plavecká škola, tanečná, kids activities), ktorého príbeh môžem použiť anonymne?
7. **Screenshoty:** dokapturovať cez kb:screenshots na tvojom účte, alebo dodáš?
8. **Newsletter / changelog:** chceš z toho zároveň brief pre changelog a weekly newsletter, keď budú články hotové?
