# Intercom — manažérska analýza podpory
**Obdobie:** 18. február – 2. apríl 2026  
**Objem:** ~170 konverzácií (109 zklasifikovaných + ~60 surových z konca marca a začiatku apríla)  
**Zdroj:** `../help_ingest/intercom/`, `../help_ingest/intercom-clusters/`, `../help_ingest/intercom-processed/`

---

## 1. Čo klientov trápi — prehľad tém

| # | Téma | Odhad počtu | Podiel |
|---|------|------------:|--------|
| 1 | Programy a kurzy (mazanie, archivovanie, nastavenia) | ~18 | 11 % |
| 2 | Lekcie, rozvrh, dochádzka | ~17 | 10 % |
| 3 | Náhradné hodiny (make-up sessions) | ~12 | 7 % |
| 4 | Platby, faktúry, fakturácia | ~13 | 8 % |
| 5 | Registrácia a registračný formulár | ~12 | 7 % |
| 6 | Notifikácie a emaily | ~12 | 7 % |
| 7 | GoCardless / platobné prepojenie | ~8 | 5 % |
| 8 | Klienti – správa, presun | ~7 | 4 % |
| 9 | Nastavenia a roly | ~7 | 4 % |
| 10 | Export a reporty | ~7 | 4 % |
| 11 | Rezervácie a kapacita | ~6 | 4 % |
| 12 | Widget a integrácia na web | ~5 | 3 % |
| 13 | Technické problémy / bugy | ~7 | 4 % |
| 14 | Šum (spam, marketing, systémové emaily) | ~25 | 15 % |
| 15 | Ostatné (onboarding, účet, prihlásenie) | ~14 | 8 % |

> **Čisté „reálne" supportné konverzácie: ~135–140.** Zvyšok sú systémové správy, marketing a interné notifikácie.

---

## 2. Analýza podľa typu otázky

### PREČO — pochopenie systému (čo sa deje a prečo)
*~30 % reálnych konverzácií*

Klienti nechápu správanie systému. Najčastejšie:

| Otázka | Frekv. |
|--------|--------|
| Prečo GoCardless nepáruje platby? (expiry 90 dní, klienti nevedia) | ★★★★ |
| Prečo zmizli skupiny z kalendára / nevidím lekcie? | ★★★ |
| Čo znamená „awaiting payment"? | ★★ |
| Čo znamená „vycerpanie náhradnej hodiny" — rezervácia alebo účasť? | ★★ |
| Aký je rozdiel medzi náhradou a prenosom náhrady (v novej dochádzke)? | ★★ |
| Prečo klient nemôže ísť na lekciu? | ★★ |
| Prečo kurzy nie sú vidieť na webe (online booking nie je zapnuté)? | ★★ |
| Aký je rozdiel: Klienti vs. Registrácie v exporte? | ★★ |
| Prečo mi prišiel email o 1:55 ráno? | ★ |
| Aký je rozdiel: GoCardless vs. emailové párovanie z banky? | ★ |

**Koreň problému:** Zooza má komplexný systém so špeciálnou terminológiou. Dokumentácia existuje, ale klienti ju nenachádzajú — alebo systém neposiela žiadne proaktívne vysvetlenie pri kľúčových udalostiach (napr. expirácia GoCardless, chybajúce lekcie).

---

### KDE / NAVIESŤ — navigácia v aplikácii
*~35 % reálnych konverzácií*

Klienti vedia čo chcú, ale nevedia kde to je. Najčastejšie:

| Otázka | Frekv. |
|--------|--------|
| Kde nájdem faktúry? | ★★★ |
| Kde je sumár náhradných hodín? | ★★★ |
| Kde nastaviť emailové pripomienky / vypnúť notifikácie? | ★★★ |
| Kde zapnúť / obnoviť GoCardless? | ★★★ |
| Kde zmeniť popis kurzu (viditeľný na webe)? | ★★ |
| Kde nastaviť automatické pokračovanie skupiny? | ★★ |
| Kde nájsť registračný formulár (odkaz pre rodičov)? | ★★ |
| Kde nastaviť rolu pre lektorku? | ★★ |
| Kde nastaviť fakturačné obdobie? | ★★ |
| Kde nastaviť čerpanie zľavových kódov? | ★ |
| Kde nájsť informácie o novej verzii Zooza? (zákazník po refaktore) | ★ |

**Koreň problému:** Nastavenia sú rozptýlené cez viacero sekcií (Settings, Programme Settings, Billing profiles). Klientom chýba rozcestník alebo kontextová nápoveda priamo v UI.

---

### AKO — kroky a postupy
*~35 % reálnych konverzácií*

Klienti chcú návod. Najčastejšie:

| Otázka | Frekv. |
|--------|--------|
| Ako vymazať / archivovať kurz alebo skupinu? | ★★★★ |
| Ako obnoviť GoCardless a napárovať staré platby? | ★★★ |
| Ako nastaviť náhradné hodiny (make-up)? | ★★★ |
| Ako skopírovať / presunúť registráciu do iného kurzu? | ★★★ |
| Ako pridať pole do registračného formulára? | ★★ |
| Ako zaznamenať dochádzku? | ★★ |
| Ako nastaviť súrodenecké zľavy? | ★★ |
| Ako stiahnuť faktúry (XML hromadný export)? | ★★ |
| Ako presunúť/transferovať klienta (Transfer funkcia)? | ★★ |
| Ako nastaviť suplování (substitution)? | ★★ |
| Ako skopírovať len potvrdené registrácie (auto-pokračovanie)? | ★★ |
| Ako pridať klienta manuálne? | ★★ |
| Ako vložiť QR kód do potvrdenia emailu podmieneným spôsobom? | ★ |
| Ako stiahnuť export všetkých aktívnych registrácií? | ★ |

---

## 3. Kľúčové zistenia — produktové medzery

### 3.1 Náhradné hodiny — reportovanie je zablokované (kritické)
**Jedno z najviditeľnejších boľaví miest.** V priebehu 25. marca sa objavili 3 konverzácie v rovnaký deň od rôznych zákazníkov. Zákazníci chcú vidieť náhradné hodiny bulkovo podľa lokality — to v Zooze dnes nejde.

- Report v Kalendár → Make-up sessions: iba `naša pobočka vs iné pobočky`, bez filtra lokality.
- Bookings view: filtruje bežné registrácie, nie make-up sessions.
- Dôsledok: zákazníčka Bajerová musela požiadať tím o manuálne vytiahnutie reportu (tím ťahal custom export pre ňu priamo).

> **Chýbajúca funkcia:** Bulk export / filter make-up sessions podľa lokality.

---

### 3.2 GoCardless — „tichá" expirácia (vysoký opakujúci sa support burden)
GoCardless prepojenie expiruje po 90 dňoch. Zákazníci to nevedia. Presto to spôsobuje:
- nefunkčné párovanie platieb,
- paniku u zákazníkov,
- viacero supportných konverzácií o tom istom.

> **Chýba:** Proaktívne upozornenie v appke (napr. 14 dní pred expirí: *„Vaše prepojenie s bankou expiruje 12. apríla — obnovte ho tu"*).

---

### 3.3 Mazanie programov / skupín — zákazníci to stále hľadajú
Päť až osem konverzácií v rôznych formách:
- *Ako vymazať kurz?*
- *Ako vymazať skupinu?*
- *Ako vymazať programy vytvorené automaticky pri onboardingu?*

Funkcia existuje (archivovanie), ale zákazníci neintuítívne hľadajú „Vymazať" nie „Archivovať". UI terminológia vs. mentálny model zákazníka niesúhlasí.

> **Návrh:** Lepsí in-app label + tooltip pri archivovaní, príp. skutočný delete pre prázdne programy.

---

### 3.4 Programme vs. Class — základná onboardingová medzera
Zákazníčka Susie (DCA Budapest) sa v marci pýtala: *„Ked sa registrujú na programe, čo sú potom classes? A čo sessions?"*. Je to fundamentálna otázka, ktorá ukazuje, že nový zákazník neprechádza štruktúrovaným onboardingom.

> **Návrh:** In-app guided tour / onboarding checklist. Prípadne silnejší welcome email s odkazom na „Zooza pre začiatočníkov".

---

### 3.5 Registračný formulár — zákazníci ho chcú viac prispôsobiť
- Pridávanie polí, odstraňovanie registračného poplatku, zmena textu súhlasov, overenie foto/video súhlasov — 5 konverzácií.
- Zákazníci hľadajú tieto nastavenia inde, nie tam kde sú.

> **Návrh:** Sekciu Registration form Settings priblížiť alebo linkovať z hlavného nastavenia programu.

---

### 3.6 Notifikácie — ťažko ovládateľné, nájditeľné, logicky nejasné
- Zákazníci nevedia nájsť nastavenia pripomienok.
- Zákazník chcel blokovať odpovede na systémové emaily.
- Zákazník chcel pridať druhú emailovú adresu na platobné notifikácie.
- Emailové hromadné operácie sa posielajú o 1:55 ráno — zákazník sťažoval.

> **Návrh:** Jednotný prehľad notifikácií (kde sú zapnuté, pre koho, kedy sa odosielajú). Čas hromadných operácií prestaviť na prijateľnejší čas (alebo dať nastaviteľné).

---

### 3.7 Export — zmätok s counts a stĺpcami
- *Exportujem klientov a vidím 178, ale mám 344 registrácií* → zákazníčka bola zmätená.
- *Čo je stĺpec AU v exporte?* → zákazník nerozumie kľúčom vs. hodnotám.
- Export XML faktúr — zákazník chcel hromadný stiahnutie.

> **Návrh:** Export UI — pridať tooltip / vysvetlivky k stĺpcom. Jasne oddeliť „Export klientov" od „Export registrácií".

---

### 3.8 AI agent odpovedá v češtine na slovenský input
Zákazníčka Barbora písala po slovensky, AI agent odpovedal po česky. Musela ho opraviť: *„po slovensky prosím"*. Agent napriek tomu pokračoval v českom jazyku.

> **Oprava:** AI agent by mal detekovať jazyk vstupnej správy a odpovedať v ňom.

---

## 4. Prioritizácia produktových akcií

| Priorita | Akcia | Dôvod |
|----------|-------|-------|
| 🔴 P1 | Bulk report make-up sessions podľa lokality | Manuálny workaround robia klienti aj tím, opakuje sa |
| 🔴 P1 | Proaktívne upozornenie na expiráciu GoCardless | Vysoký opakujúci sa support burden, frustrácia zákazníkov |
| 🟠 P2 | In-app guided onboarding (Programme → Class → Session) | Fundamentálna otázka nových zákazníkov |
| 🟠 P2 | Jednotný prehľad notifikácií | 10+ konverzácií, zákazníci nevedia kde čo je |
| 🟠 P2 | Lepší label pri archivovaní (≠ mazaní) | 5+ konverzácií o mazaní kurzu/skupiny |
| 🟡 P3 | Vysvetlivky k stĺpcom v exporte | 3+ konverzácií o zmätku v exporte |
| 🟡 P3 | Rozlíšenie Clients export vs. Registrations export | Zákazníci exportujú z nesprávneho miesta |
| 🟡 P3 | Čas hromadných emailových operácií (nie 1:55 ráno) | 1 sťažnosť, ale logický problém |
| 🟡 P3 | AI agent — detekcia jazyka (SK ≠ CZ) | Reputačný problém, zákazník frustrovaný |
| 🟢 P4 | Loyalty program na úrovni Network (ZOOZA-4682) | V Jire, zákazníci sa pýtajú |
| 🟢 P4 | Full name v exporte (ZOOZA-4666) | V Jire |

---

## 5. Kam ťahať produkt ďalej — strategický záver

### Silné stránky, ktoré zákazníci oceňujú (implicitne)
- Automatické pokračovanie skupín (auto-enrolment) — zákazníci ho aktívne používajú a chcú ho rozširovať.
- Make-up sessions — zákazníci majú komplexné scenáre, čo znamená, že feature je dobre adoptovaná.
- GoCardless integrácia — zákazníci ju chcú, len bojujú s UX.

### Tri osi, kde investícia prinesie najviac
1. **Reporting & export** — zákazníci spravujú reálny biznis a potrebujú dáta filtrovateľne a exportovateľne. Dnes je to tichá bolesť. Make-up report, active registrations report, custom export columns — to sú konkrétne medzery.

2. **Proaktívna komunikácia (in-app + email)** — zákazníci reagujú, nie sú proaktívne vedení. GoCardless expiry, blížiace sa ukončenie kurzu, klienti bez registrácie na nový term — toto by mohol systém sám komunikovať.

3. **Onboarding a discoverability** — zákazníci nevedia kde veci sú, aj keď Zooza tie veci má. Guided setup, kontextové tooltips a lepšia navigácia v Settings by redukovali support load bez akéhokoľvek nového feature vývoja.

---

*Report vygenerovaný 2026-04-13 zo surovej komunikácie z Intercomu.*
