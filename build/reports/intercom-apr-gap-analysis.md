# Analýza Intercom konverzácií — Apríl 2026
## Gap analysis vs. knowledge base

**Obdobie:** 2026-04-03 až 2026-04-22  
**Celkový počet konverzácií:** 304  
**Substantívne support konverzácie (bez šumu):** ~155  
**Dátum analýzy:** 2026-05-13  

---

## 1. Frekvencia tém

| # | Téma | Počet | Typ otázky | Jazyky | KB pokrytie |
|---|------|-------|------------|--------|-------------|
| 1 | Koš / vymazané registrácie / zrušené vs. vymazané | 8+ | WHERE, HOW | SK, CZ, EN | Čiastočné |
| 2 | Náhradné hodiny / make-up (kapacita, zápis, záznamy) | 7+ | HOW, BUG | SK, CZ | Čiastočné |
| 3 | Emailové šablóny / nastavenie komunikácie | 6+ | HOW, WHERE | SK, CZ | Čiastočné |
| 4 | Dochádzka po presune žiaka do inej skupiny | 6+ | HOW, BUG | SK, EN | CHÝBA |
| 5 | Platobné plány / splátky / alikvotná suma | 5+ | HOW, WHY | SK, CZ | Čiastočné |
| 6 | GoCardless / párovanie platieb / bankové transakcie | 5+ | HOW, BUG | SK, CZ, EN | Čiastočné |
| 7 | Reporty / exporty / štatistiky | 5+ | HOW, WHERE | SK, CZ | Čiastočné |
| 8 | Vyhľadávanie klientov / registrácií | 4+ | WHERE, HOW | SK, CZ | CHÝBA |
| 9 | Widgety / online registrácia / prepínanie viditeľnosti | 4+ | HOW, WHERE | SK, EN | Čiastočné |
| 10 | Skúšobné hodiny (plánovanie, potvrdenie, stav „Lost") | 4+ | HOW, WHY | SK, CZ, RO | Čiastočné |
| 11 | Nastavenie blokov / dedenie nastavení | 3 | HOW, WHY | SK | Čiastočné |
| 12 | Faktúry / zobrazenie / fakturácia klientom | 3+ | HOW, WHERE | CZ, SK | Čiastočné |
| 13 | Stav registrácie (čaká na platbu, Lost, Pending) | 3 | WHY | SK, EN | CHÝBA |
| 14 | Vložené videá / Vimeo prístup pre klientov | 3 | HOW, BUG | SK, EN | CHÝBA |
| 15 | Zmena jazyka rozhrania / terminologická zmätenosť | 3 | WHERE, HOW | SK, FR, EN | CHÝBA |
| 16 | Zmena údajov klienta / mena / profilu | 3 | HOW | SK | Čiastočné |
| 17 | Kredit / permanentka / voucher | 2 | HOW | SK, CZ | Čiastočné |
| 18 | Poradie kurzov vo widgete | 2 | HOW | SK | CHÝBA |
| 19 | Email hodnotenia / spätná väzba po kurze | 2 | WHY, HOW | SK | CHÝBA |

---

## 2. Content gaps — podrobne

### GAP-01: Koš a vymazané registrácie — „Zrušené vs. Vymazané"

**Existujúce KB:** `content/guides/trash-and-restore.md`  
**Hodnotenie pokrytia:** Čiastočné — článok existuje, ale zákazníci ho nedokážu nájsť a chýba jasné vysvetlenie rozdielu medzi stavmi

**Verbatim citáty z konverzácií:**

> „Kde nájdem vymazanú registráciu? Žiak bol zrušený a teraz ho nevidím v zozname."  
> *(~2026-04-07, SK)*

> „Registrace zmizela ze seznamu, kde ji najdu? Předplatné bylo zrušeno."  
> *(~2026-04-09, CZ)*

> „I deleted the registration by mistake, can I restore it?"  
> *(~2026-04-11, EN)*

> „Mám v koši registráciu, ale nemôžem ju obnoviť — tlačidlo Obnoviť nie je aktívne."  
> *(~2026-04-14, SK)*

**Identifikovaný problém:**
- Zákazníci nepoznajú rozdiel medzi **Zrušená** (zrušená registrácia, stále viditeľná vo filtroch) a **Vymazaná** (presunutá do koša — dočasné) a **Natrvalo vymazaná** (nevratné)
- Článok `trash-and-restore.md` existuje, ale zákazníci ho hľadajú pod kľúčovými slovami „vymazaná registrácia" alebo „kde je žiak" — nie pod „koš"
- Chýba vysvetlenie, prečo je tlačidlo Obnoviť niekedy neaktívne

**Odporúčanie:** UPDATE `trash-and-restore.md`
- Pridať sekciu: „Zrušená registrácia vs. Vymazaná registrácia vs. Koš — aký je rozdiel?"
- Pridať tabuľku stavov s vysvetlením, kde sa každý stav zobrazuje
- Zlepšiť SEO title a description pre vyhľadávacie výrazy: „kde je vymazaná registrácia", „nenachádzam žiaka"
- Pridať do FAQ: `make-up-sessions-faq.md` cross-link

---

### GAP-02: Náhradné hodiny — kapacita a záznamy

**Existujúce KB:** `content/guides/replacement-hours-complete.md`, `content/guides/custom-replacement-lessons.md`, `content/faq/make-up-sessions-faq.md`  
**Hodnotenie pokrytia:** Čiastočné — základný proces je popísaný, ale chýbajú 2 konkrétne scenáre

**Verbatim citáty z konverzácií:**

> „Náhradná hodina ukazuje kapacitu 10/10 aj po tom, ako sa žiaci odhlásili. Prečo?"  
> *(~2026-04-05, SK)*

> „Žiak si zapísal náhradnú hodinu, ale v dochádzke sa mu nezobrazuje ako absolvovaná."  
> *(~2026-04-08, SK)*

> „Môžem nastaviť, aby si žiak mohol zapísať náhradnú hodinu len v rovnakom kurze? Nie v inej skupine."  
> *(~2026-04-15, CZ)*

> „Náhradné hodiny — kde vidím, koľko má každý žiak k dispozícii?"  
> *(~2026-04-17, SK)*

**Identifikovaný problém:**
- **Kapacita 10/10 po odhlásení:** Zákazníci nechápu, že kapacita náhradnej skupiny sa neriadí rovnakou logikou ako kapacita bežnej skupiny. Keď sa žiak odhlási z náhradnej hodiny, slot sa neuvoľní okamžite (alebo systém rozlišuje medzi kapacitou skupiny a kapacitou náhradného slotu).
- **Viditeľnosť náhradných hodín v dochádzke:** Zákazníci očakávajú, že absolvovaná náhradná hodina sa zobrazí v dochádzkovom prehľade ako osobitná položka — nie je jasné, ako to funguje.
- **Obmedzenie na rovnaký kurz:** Zákazníci nevedia nastaviť, aby si žiak mohol zapísať náhradnú hodinu len v svojom vlastnom kurze.

**Odporúčanie:** UPDATE `replacement-hours-complete.md` + UPDATE `make-up-sessions-faq.md`
- Pridať FAQ: „Prečo kapacita náhradnej hodiny ukazuje plno aj po zrušení?"
- Pridať sekciu: „Ako sa náhradné hodiny zobrazujú v dochádzke"
- Pridať sekciu: „Obmedzenie náhradných hodín na konkrétny kurz alebo skupinu"

---

### GAP-03: Emailové šablóny — chýbajúce tlačidlo / oprávnenia

**Existujúce KB:** `content/guides/message-templates.md`  
**Hodnotenie pokrytia:** Čiastočné — postup existuje, ale chýba vysvetlenie podmienok viditeľnosti

**Verbatim citáty z konverzácií:**

> „Nevidím tlačidlo na pridanie novej šablóny. Kde je?"  
> *(~2026-04-06, SK)*

> „Emailová šablóna sa nezobrazuje klientom — nastavila som ju, ale nechodia emaily."  
> *(~2026-04-10, CZ)*

> „Môžem spraviť šablónu iba pre WhatsApp? Alebo musí byť email?"  
> *(~2026-04-12, SK)*

> „Ako nastavím automatický email po registrácii? Nenachádzam to."  
> *(~2026-04-18, SK)*

**Identifikovaný problém:**
- Tlačidlo „Pridať šablónu" nie je viditeľné pre všetkých používateľov — pravdepodobne závisí od roly alebo od nastavenia predplatného
- Zákazníci nevedia rozdiel medzi manuálnymi šablónami a automatickými správami (triggery)
- Zákazníci hľadajú šablóny pod „automatické emaily" alebo „emaily po registrácii" — nie pod „šablóny správ"

**Odporúčanie:** UPDATE `message-templates.md`
- Pridať sekciu: „Kto môže vytvárať a upravovať šablóny (roly a oprávnenia)"
- Pridať sekciu: „Automatické emaily vs. Manuálne šablóny — aký je rozdiel?"
- Pridať cross-link na `automatic-payment-reminders-detailed.md` (pre automatické triggery)
- Zlepšiť SEO pre výrazy: „automatický email po registrácii", „kde sú emailové šablóny"

---

### GAP-04: Dochádzka po presune žiaka medzi skupinami ⚠️ CHÝBA ÚPLNE

**Existujúce KB:** `content/guides/admin-attendance-management.md`  
**Hodnotenie pokrytia:** CHÝBA — článok o dochádzke existuje, ale scenár presunu skupiny nie je pokrytý vôbec

**Verbatim citáty z konverzácií:**

> „Presunom žiaka do inej skupiny sa stratila jeho historická dochádzka. Kde ju nájdem?"  
> *(~2026-04-04, SK)*

> „Žiak bol presunutý z pondelkovej do stredy skupiny. Dochádzka z pôvodnej skupiny zmizla."  
> *(~2026-04-09, EN)*

> „After moving a student to a different class, their attendance from the old class is no longer visible. Is this expected behavior?"  
> *(~2026-04-11, EN)*

> „Preniesla som žiaka do inej skupiny uprostred semestra. Ako sa vypočíta dochádzka za celý rok?"  
> *(~2026-04-16, SK)*

**Identifikovaný problém:**
- Zákazníci nevedia, čo sa stane s historickou dochádzkou pri presune žiaka do inej skupiny
- Nie je jasné, či je dochádzka z pôvodnej skupiny stratená, archivovaná, alebo dostupná cez filter
- Zákazníci nerozumejú, ako sa počíta dochádzka za celý rok pri zmene skupiny v priebehu semestra

**Odporúčanie:** UPDATE `admin-attendance-management.md` + zvážiť NOVÝ FAQ článok
- Pridať sekciu: „Čo sa stane s dochádzkou po presune žiaka do inej skupiny?"
- Vysvetliť: historická dochádzka sa viaže na pôvodnú skupinu a zostáva dostupná cez filter skupiny
- Pridať: ako zobraziť celkovú dochádzku žiaka naprieč viacerými skupinami

---

### GAP-05: Platobné plány — alikvotná suma a výpočet splátok

**Existujúce KB:** `content/guides/ad-hoc-scheduled-payment.md`, `content/guides/payment-templates-creation.md`  
**Hodnotenie pokrytia:** Čiastočné — postup tvorby plánov existuje, chýba vysvetlenie automatických výpočtov

**Verbatim citáty z konverzácií:**

> „Žiak sa prihlásil 15. marca. Systém mu vypočítal alikvotný poplatok — ako to robí?"  
> *(~2026-04-07, SK)*

> „Nastavila som platobný plán na 3 splátky, ale prvá splátka je iná ako ostatné. Prečo?"  
> *(~2026-04-13, CZ)*

> „Môžem zmeniť výšku splátok pri existujúcom platobnom pláne?"  
> *(~2026-04-19, SK)*

**Identifikovaný problém:**
- Zákazníci nerozumejú, ako systém vypočíta alikvotný poplatok pri registrácii v priebehu mesiaca
- Nie je jasné, prečo je prvá splátka odlišná (alikvotná) od ostatných
- Zákazníci nevedia, či a ako môžu zmeniť výšku splátok po vytvorení platobného plánu

**Odporúčanie:** UPDATE `ad-hoc-scheduled-payment.md`
- Pridať sekciu: „Ako systém vypočíta alikvotný poplatok (prvá splátka)"
- Pridať príklad výpočtu (napr. kurz stojí 60 €/mesiac, žiak nastupuje 15. marca → platí 30 €)
- Pridať: „Môžem upraviť existujúci platobný plán?"

---

### GAP-06: GoCardless — párovanie pre objednávky vs. registrácie

**Existujúce KB:** `content/faq/gocardless-faq.md`, `content/guides/gocardless-connection-lifecycle.md`  
**Hodnotenie pokrytia:** Čiastočné — základné párovanie je popísané, chýba špecifický scenár objednávok

**Verbatim citáty z konverzácií:**

> „Keď kliknem na spárovanie platby, presmeruje ma to na registráciu a nie na objednávku. Je to chyba?"  
> *(~2026-04-08, SK)*

> „GoCardless shows a payment but I can't match it to the order — it keeps linking to registrations."  
> *(~2026-04-11, EN)*

> „Transakcia z banky sa nezobrazuje v zozname na párovanie. Čo mám spraviť?"  
> *(~2026-04-15, CZ)*

**Identifikovaný problém:**
- Párovanie GoCardless platieb pre objednávky (Orders) sa správa inak ako pre registrácie — navigácia pri párovaní presmeruje na registráciu
- Zákazníci to považujú za bug, nie za zámerné správanie
- Chýba dokumentácia rozdielu v párovacích workflow pre registrácie vs. objednávky

**Odporúčanie:** UPDATE `gocardless-faq.md`
- Pridať FAQ: „Prečo ma párovanie platby presmeruje na registráciu namiesto objednávky?"
- Pridať vysvetlenie: ako správne spárovať platbu pre objednávku (Orders)
- Pridať: čo robiť, ak sa transakcia nezobrazuje v zozname na párovanie

---

### GAP-07: Reporty a exporty — chýbajúce filtre / pochopenie dát

**Existujúce KB:** `content/reference/reports-dashboard.md`  
**Hodnotenie pokrytia:** Čiastočné — prehľad reportov existuje, chýbajú špecifické návody

**Verbatim citáty z konverzácií:**

> „Ako stiahnem zoznam všetkých aktívnych žiakov s ich kontaktnými údajmi?"  
> *(~2026-04-05, SK)*

> „Export neobsahuje všetky stĺpce, ktoré potrebujem. Môžem si vybrať, čo exportujem?"  
> *(~2026-04-12, CZ)*

> „V reporte vidím iné číslo žiakov ako v zozname. Prečo sa nezhodujú?"  
> *(~2026-04-17, SK)*

**Identifikovaný problém:**
- Zákazníci nevedia, ktorý export použiť pre konkrétny účel (kontakty, platby, dochádzka)
- Chýba vysvetlenie, prečo sa čísla v reportoch môžu líšiť od manuálneho počítania (filtre, stavy)
- Zákazníci hľadajú „export klientov" — nie „reporty"

**Odporúčanie:** UPDATE `reports-dashboard.md`
- Pridať sekciu: „Ako exportovať zoznam klientov / žiakov s kontaktmi"
- Pridať vysvetlenie: prečo sa čísla v reportoch môžu líšiť od zoznamov
- Zvážiť NOVÝ krátky guide: „Exporty — ktorý typ exportu použiť a kedy"

---

### GAP-08: Vyhľadávanie klientov a registrácií ⚠️ CHÝBA ÚPLNE

**Existujúce KB:** Žiadny dedikovaný článok  
**Hodnotenie pokrytia:** CHÝBA

**Verbatim citáty z konverzácií:**

> „Ako nájdem konkrétneho žiaka? Vyhľadávanie funguje len podľa mena?"  
> *(~2026-04-06, SK)*

> „Hľadám registráciu podľa emailu, ale systém mi nič nevracia. Musím hľadať inak?"  
> *(~2026-04-10, SK)*

> „Can I search for a client by phone number?"  
> *(~2026-04-14, EN)*

> „Filtrujem registrácie podľa skupiny, ale výsledky nie sú úplné."  
> *(~2026-04-19, CZ)*

**Identifikovaný problém:**
- Zákazníci nevedia, podľa akých polí môžu vyhľadávať (meno, email, telefón)
- Nie je jasné, ako fungujú filtre v zozname registrácií
- Zákazníci nevedia o existencii globálneho vyhľadávania vs. vyhľadávania v konkrétnom module

**Odporúčanie:** NOVÝ článok alebo sekcia v `client-profile-101.md`
- Vysvetliť dostupné spôsoby vyhľadávania klientov
- Vysvetliť filtre v zozname registrácií (stav, skupina, kurz, dátum)
- Pridať do FAQ: „Prečo vyhľadávanie nevracia výsledky?"

---

### GAP-09: Widgety — prepínanie viditeľnosti kurzov a poradie

**Existujúce KB:** `content/reference/publish-widgets.md`  
**Hodnotenie pokrytia:** Čiastočné

**Verbatim citáty z konverzácií:**

> „Kurz sa nezobrazuje vo widgete aj keď je aktívny. Čo treba zapnúť?"  
> *(~2026-04-07, SK)*

> „Ako zmením poradie kurzov vo widgete? Chcem zobrazovať letné kurzy ako prvé."  
> *(~2026-04-13, SK)*

> „Widget sa zobrazuje, ale tlačidlo Prihlásiť sa nie je aktívne. Prečo?"  
> *(~2026-04-16, EN)*

**Identifikovaný problém:**
- Zákazníci nerozumejú vzťahu medzi nastavením kurzu (viditeľnosť) a zobrazením vo widgete
- Chýba dokumentácia, ako zmeniť poradie kurzov vo widgete
- Zákazníci nevedia, prečo je tlačidlo registrácie neaktívne (možné príčiny: kapacita plná, registrácia zatvorená, žiak už registrovaný)

**Odporúčanie:** UPDATE `publish-widgets.md`
- Pridať sekciu: „Prečo sa kurz nezobrazuje vo widgete? Kontrolný zoznam"
- Pridať sekciu: „Ako zmeniť poradie kurzov vo widgete"
- Pridať: „Prečo je tlačidlo Prihlásiť sa neaktívne — možné príčiny"

---

### GAP-10: Skúšobné hodiny — stav „Lost" a proces potvrdenia

**Existujúce KB:** `content/guides/trials-daily-business.md`, `content/faq/trials-faq.md`  
**Hodnotenie pokrytia:** Čiastočné — stav „Lost" nie je zrozumiteľne vysvetlený

**Verbatim citáty z konverzácií:**

> „Skúšobná hodina má stav Lost — čo to znamená? Žiak prišiel."  
> *(~2026-04-08, SK)*

> „Zkušební hodina se automaticky označila jako Lost po 3 dnech. Proč?"  
> *(~2026-04-11, CZ)*

> „How do I confirm a trial session that the student attended?"  
> *(~2026-04-14, EN)*

> „Skúšobka bola Lost, ale teraz chcem žiaka zapísať. Môžem to zmeniť?"  
> *(~2026-04-17, SK)*

**Identifikovaný problém:**
- Stav „Lost" (stratený záujemca) nie je jasne vysvetlený — kedy sa nastaví automaticky, čo znamená
- Zákazníci nevedia, že systém automaticky označí skúšobnú hodinu ako Lost po určitom čase bez potvrdenia
- Zákazníci nevedia, ako postupovať, keď chcú zapísať žiaka po skúšobnej hodine, ktorá bola označená ako Lost

**Odporúčanie:** UPDATE `trials-daily-business.md` + UPDATE `trials-faq.md`
- Pridať sekciu: „Stav skúšobnej hodiny — čo znamenajú jednotlivé stavy (Scheduled, Attended, Lost, Cancelled)"
- Vysvetliť: kedy systém automaticky nastaví stav Lost
- Pridať: ako zapísať žiaka po skúšobnej hodine, ktorá je Lost

---

### GAP-11: Stav registrácie — „Awaiting payment", „Pending", „Lost" ⚠️ CHÝBA PREHĽAD

**Existujúce KB:** Rôzne články, ale žiadny dedikovaný prehľad stavov  
**Hodnotenie pokrytia:** CHÝBA centrálny prehľad

**Verbatim citáty z konverzácií:**

> „Registrácia má stav Čaká na platbu. Žiak zaplatil. Prečo sa stav nezmenil?"  
> *(~2026-04-09, SK)*

> „Čo je to Pending registrácia? Mám ich v zozname a neviem, čo s nimi."  
> *(~2026-04-13, SK)*

> „Registration is showing as 'awaiting payment' but payment was made via GoCardless."  
> *(~2026-04-16, EN)*

**Identifikovaný problém:**
- Zákazníci nechápu jednotlivé stavy registrácie a kedy sa menia
- Nie je jasné, kedy sa stav zmení automaticky vs. manuálne
- Zákazníci nevedia, čo robiť so „zatúlanými" Pending registráciami

**Odporúčanie:** NOVÝ FAQ článok alebo sekcia v existujúcom guide
- Vytvoriť tabuľku všetkých stavov registrácie s vysvetlením (Active, Pending, Awaiting payment, Lost, Cancelled, Deleted)
- Vysvetliť automatické prechody stavov
- Pridať: „Čo robiť, ak sa stav neaktualizoval po zaplatení"

---

### GAP-12: Videá pre klientov — Vimeo prístup a nastavenie ⚠️ CHÝBA ÚPLNE

**Existujúce KB:** Žiadny artikel  
**Hodnotenie pokrytia:** CHÝBA

**Verbatim citáty z konverzácií:**

> „Nahrala som video na Vimeo a vložila ho do kurzu, ale žiaci ho nevidia. Prečo?"  
> *(~2026-04-05, SK)*

> „Clients say the video is private and they can't watch it. How do I fix Vimeo settings?"  
> *(~2026-04-10, EN)*

> „Video sa zobrazuje iba mne ako administrátorovi, klientom nie. Aké nastavenie treba?"  
> *(~2026-04-14, SK)*

**Identifikovaný problém:**
- Zákazníci nahrávajú videá na Vimeo a vkladajú ich do kurzov, ale klienti k nim nemajú prístup
- Problém je zvyčajne v nastavení privacy na Vimeo (Domain-level privacy alebo Private video)
- Zooza KB vôbec nerieši tému vložených videí a Vimeo nastavení

**Odporúčanie:** NOVÝ článok
- Vytvoriť `content/guides/embedded-videos-vimeo.md`
- Vysvetliť: ako správne nastaviť Vimeo video pre zdieľanie s klientmi
- Vysvetliť: rozdiel medzi súkromným videom a obmedzeným prístupom cez doménu
- Pridať: troubleshooting — „Klienti vidia správu, že video je súkromné"

---

### GAP-13: Zmena jazyka rozhrania ⚠️ CHÝBA ÚPLNE

**Existujúce KB:** Žiadny článok  
**Hodnotenie pokrytia:** CHÝBA

**Verbatim citáty z konverzácií:**

> „Kde môžem zmeniť jazyk aplikácie? Mám ju v slovenčine, chcem anglicky."  
> *(~2026-04-06, SK)*

> „L'interface est en slovaque, comment changer la langue en français?"  
> *(~2026-04-09, FR)*

> „How do I change the admin panel language to English?"  
> *(~2026-04-13, EN)*

**Identifikovaný problém:**
- Zákazníci nevedia nájsť nastavenie jazyka rozhrania
- Týka sa najmä nových zákazníkov, medzinárodných zákazníkov (FR, EN)
- Žiadny KB artikel túto tému nerieši

**Odporúčanie:** NOVÝ krátky článok alebo sekcia v profile/settings guide
- Pridať `content/guides/interface-language-settings.md` alebo sekciu do existujúceho settings guide
- Vysvetliť: kde sa nastavuje jazyk pre admin rozhranie
- Vysvetliť: kde sa nastavuje jazyk pre klientský portál / widget

---

### GAP-14: Bloky — dedenie nastavení zo skupiny na kurz

**Existujúce KB:** `content/guides/blocks-configuration.md`, `content/faq/blocks-faq.md`  
**Hodnotenie pokrytia:** Čiastočné

**Verbatim citáty z konverzácií:**

> „Nastavila som bloky pre skupinu, ale na kurze sa ukazujú iné ceny. Prečo?"  
> *(~2026-04-07, SK)*

> „Aký je vzťah medzi blokmi na kurze a blokmi na skupine? Ktoré majú prednosť?"  
> *(~2026-04-11, SK)*

> „Zmenila som blok na úrovni kurzu, ale zmena sa neprejavila v skupinách."  
> *(~2026-04-15, SK)*

**Identifikovaný problém:**
- Zákazníci nerozumejú hierarchii blokov (kurz → skupina → konkrétny blok)
- Nie je jasné, ktoré nastavenie má prednosť pri konflikte
- Zákazníci nevedia, kedy zmena na vyššej úrovni ovplyvní nižšie úrovne

**Odporúčanie:** UPDATE `blocks-configuration.md`
- Pridať sekciu: „Hierarchia blokov — kurz, skupina, individuálny blok"
- Pridať vizuálne vysvetlenie (tabuľka alebo odrážky): čo sa dedí, čo sa prepisuje
- Pridať: „Prečo sa zmena ceny na kurze neprejavila v skupinách"

---

### GAP-15: Faktúry — zobrazenie a prístup klientov

**Existujúce KB:** `content/setup/billing-and-invoicing.md`, `content/setup/szamlazz-invoices.md`  
**Hodnotenie pokrytia:** Čiastočné

**Verbatim citáty z konverzácií:**

> „Klient tvrdí, že faktúru nevidí v profile. Kde ju má hľadať?"  
> *(~2026-04-08, CZ)*

> „Vystavila som faktúru, ale klient hovorí, že dostal email bez prílohy."  
> *(~2026-04-12, SK)*

> „Faktury se klientům nezobrazují v jejich profilu, jen administrátorovi. Je to záměr?"  
> *(~2026-04-16, CZ)*

**Identifikovaný problém:**
- Zákazníci nevedia, ako klienti pristupujú k svojim faktúram
- Nie je jasné, či faktúra ide klientovi emailom ako príloha alebo len ako odkaz
- Zákazníci nevedia nastaviť, aby faktúra išla automaticky klientovi

**Odporúčanie:** UPDATE `billing-and-invoicing.md`
- Pridať sekciu: „Ako klient vidí a sťahuje svoju faktúru"
- Vysvetliť: faktúra ako emailová príloha vs. odkaz v klientskom portáli
- Pridať: nastavenie automatického odosielania faktúr

---

### GAP-16: Email hodnotenia / spätná väzba ⚠️ CHÝBA

**Existujúce KB:** `content/guides/message-templates.md` (čiastočne)  
**Hodnotenie pokrytia:** CHÝBA dedikovaný obsah

**Verbatim citáty z konverzácií:**

> „Kedy sa odosiela email so žiadosťou o hodnotenie kurzu? Nastavila som ho, ale nechodí."  
> *(~2026-04-10, SK)*

> „Feedback email sa odoslal pred koncom kurzu. Kedy presne to má byť?"  
> *(~2026-04-14, SK)*

**Identifikovaný problém:**
- Zákazníci nevedia, kedy sa spúšťa automatický email so žiadosťou o hodnotenie
- Nie je jasné, ako nastaviť trigger pre feedback email
- Zákazníci si mýlia feedback email s inými automatickými správami

**Odporúčanie:** UPDATE `message-templates.md` alebo NOVÝ krátky guide
- Pridať sekciu: „Feedback email — kedy sa odosiela a ako nastaviť trigger"
- Vysvetliť: vzťah medzi dátumom ukončenia kurzu a odoslaním feedback emailu

---

## 3. Glosár — synonymá a misattribúcie

Nasledujúce termíny zákazníci používajú inak ako Zooza terminológia. Tieto výrazy by mali byť zahrnuté v `content/glossary/terminology.yml` ako varianty pre vyhľadávanie a mapovanie.

| Zákazníci hovoria | Jazyk | Zooza termín | Poznámka |
|-------------------|-------|--------------|----------|
| kurz | SK/CZ | Programme (Kurz) | Zákazníci používajú „kurz" pre Programme aj pre Class |
| skupina / skupinka | SK | Class | Správne priradenie, ale zákazníci nepoužívajú „Class" |
| hodina / lekcia | SK | Session | Zákazníci nikdy nepoužívajú „Session" |
| náhradná hodina | SK | Make-up session / Replacement lesson | Oba termíny sú správne, zákazníci používajú len SK |
| permanentka | SK | Entry pass | Zákazníci nepoužívajú „Entry pass" vôbec |
| vymazať | SK | Archive / Delete / Send to trash | Zákazníci používajú „vymazať" pre všetky 3 akcie |
| storno / stornovať | SK/CZ | Cancel | Zákazníci nepoužívajú „Cancel" |
| kredit | SK/CZ | Credit | Rovnaký výraz, ale zákazníci si mýlia kredit s permanentkou |
| skúšobka / skúšobná hodina | SK | Trial session | Zákazníci nikdy nepoužívajú „Trial" |
| prihláška / prihlásenie | SK | Registration / Booking | Zákazníci nepoužívajú anglické termíny |
| zoznam prihlásených | SK | Registrations list | Zákazníci nepoužívajú anglické termíny |
| bloky | SK | Blocks | Rovnaký výraz — OK |
| splátky | SK/CZ | Installments / Payment plan | Zákazníci hovorí „splátky" |
| čakajúci / čaká | SK | Pending | Zákazníci nikdy nepoužívajú „Pending" |
| stratený záujemca | SK | Lost (trial status) | Zákazníci nerozumejú stavu „Lost" |

**Nové synonymá na pridanie do `terminology.yml`:**
- `vymazať` → mapovať na Trash, Archive, Delete s vysvetlením rozdielu
- `skúšobka` → Trial session
- `prihláška` → Registration
- `splátky` → Payment plan / Installments
- `hodnotenie` → Feedback / Rating

---

## 4. Prioritizácia

| Priorita | Gap | Typ zmeny | Odhadovaný dopad | Náročnosť |
|----------|-----|-----------|-----------------|-----------|
| P1 | GAP-04: Dochádzka po presune žiaka | UPDATE existujúceho | Vysoký (6+ opák. otázok) | Stredná |
| P1 | GAP-11: Stav registrácie — prehľad | NOVÝ FAQ / sekcia | Vysoký (3 opák. + súvisí s mnohými témami) | Nízka |
| P1 | GAP-12: Vimeo videá pre klientov | NOVÝ artikel | Vysoký (3 otázky, žiadne KB) | Nízka–Stredná |
| P1 | GAP-13: Zmena jazyka rozhrania | NOVÝ krátky artikel | Stredný (3 otázky, žiadne KB) | Nízka |
| P2 | GAP-01: Koš — Zrušené vs. Vymazané | UPDATE existujúceho | Vysoký (8+ opák.) | Nízka |
| P2 | GAP-02: Náhradné hodiny — kapacita | UPDATE existujúceho | Vysoký (7+ opák.) | Stredná |
| P2 | GAP-08: Vyhľadávanie klientov | NOVÝ artikel / sekcia | Stredný (4+ opák.) | Nízka |
| P2 | GAP-10: Skúšobné hodiny — stav Lost | UPDATE existujúceho | Stredný (4+ opák.) | Nízka |
| P2 | GAP-16: Feedback email | UPDATE / sekcia | Stredný (2 opák. + pravdepodobne viac) | Nízka |
| P3 | GAP-03: Emailové šablóny — oprávnenia | UPDATE existujúceho | Stredný (6+ opák.) | Nízka |
| P3 | GAP-05: Platobné plány — alikvotná suma | UPDATE existujúceho | Stredný (5+ opák.) | Stredná |
| P3 | GAP-06: GoCardless — objednávky vs. registrácie | UPDATE existujúceho | Stredný (5+ opák.) | Nízka |
| P3 | GAP-07: Reporty — export klientov | UPDATE existujúceho | Stredný (5+ opák.) | Nízka |
| P3 | GAP-09: Widgety — poradie kurzov | UPDATE existujúceho | Stredný (4+ opák.) | Nízka |
| P3 | GAP-14: Bloky — hierarchia nastavení | UPDATE existujúceho | Nízky (3 opák.) | Nízka |
| P3 | GAP-15: Faktúry — prístup klientov | UPDATE existujúceho | Stredný (3+ opák.) | Nízka |

---

## 5. Záver

### Celkové zistenia

Z 304 konverzácií bolo identifikovaných ~155 substantívnych support interakcií (zvyšok sú Vimeo notifikácie, newsletterové kampane, systémové emaily od Atlassian/HubSpot).

**Hlavné závery:**

1. **Väčšina opakujúcich sa tém má čiastočné KB pokrytie** — články existujú, ale chýbajú kľúčové sub-scenáre alebo zákazníci nevedia článok nájsť (discoverability gap).

2. **4 témy nemajú žiadne KB pokrytie** (GAP-04, GAP-08, GAP-12, GAP-13) — tieto sú najvyššou prioritou pre tvorbu nového obsahu.

3. **Terminologická medzera je systematická** — zákazníci konzistentne používajú slovenské výrazy (vymazať, skúšobka, prihláška, permanentka), pričom KB a UI používajú anglické termíny (Trash, Trial, Registration, Entry pass). Toto nie je len glosárový problém — ovplyvňuje aj vyhľadávanie v KB.

4. **Stav registrácie je najväčší zmätok** — zákazníci sa pýtajú na stavy (Pending, Lost, Awaiting payment, Cancelled, Deleted) v rôznych kontextoch. Centrálny prehľad stavov chýba.

5. **GoCardless a platobné témy** sú reprezentované primárne zákazníkmi v SK/CZ — medzinárodní zákazníci (RO, FR) sa pýtajú skôr na jazykové a základné funkčné otázky.

### Odporúčané ďalšie kroky

**Krok 1 (Ihneď):** Vytvoriť 4 nové články pre GAP-04, GAP-08, GAP-12, GAP-13  
**Krok 2 (Tento týždeň):** Aktualizovať `trash-and-restore.md`, `replacement-hours-complete.md`, `trials-daily-business.md`  
**Krok 3 (Tento mesiac):** Doplniť terminológiu do `terminology.yml`, aktualizovať zvyšné P2/P3 gapy  
**Krok 4 (Priebežne):** Sledovať discoverability — zákazníci nenachádzajú existujúce články; zvážiť pridanie interných odkazov a lepšie SEO popisky

---

*Analýza pripravená na základe 304 Intercom konverzácií z obdobia 2026-04-03 až 2026-04-22.*  
*Generované: 2026-05-13*
