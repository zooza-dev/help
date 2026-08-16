# Weekly intake queue -- 2026-08-07 to 2026-08-15

Prepared 2026-08-16. Nothing here has been written to `content/` -- this is a queue.

## Counts

- Conversations with a human reply: **25**
- Bot-only conversations: **35**
- Bot-only needing a look: **21**
- Implemented specs not yet communicated: **0**

## 1. Human answers -- the gold standard

Read these first. A human answer that generalises belongs in the KB.

### `215475421150442` -- 2026-08-10 05:18

**Asked:** Dobrý deň, nakoľko sa nerozumiem kódovaniu, mohol by som vás poprosiť o úpravu textov prihlas. formulári? Poprosím upraviť naseldovné: „Vyberte si *" → „Vyberte si kategóriu podľa veku" „Prispôsobte si ponuku" → „Prihlásiť na celý kurz" „Na skúšobnú hodinu" → „Najprv chcem skúšobnú hodinu zadarmo" Takto mám uložené prístupy na môj web- Link: https://foxgym.sk/wp-admin Meno: Administr@tor Heslo: Be

**Human answered:** Dobry den, Michal, ano, dajú sa tie texty na Vašom webe prispôsobiť. Pošlite želaný text, ak máme ešte prístup k webu môžeme to urobiť aj za Vás. Návod ako to dosiahnuť je aj tu: https://docs.zooza.online/widgets/registration-widget/#translations

### `215475422464434` -- 2026-08-10 08:20

**Asked:** Potřeboval bych zkontrolovat fortmátování emailů. Takhle vypadá automatický mail ze zoozy:

**Human answered:** Dobry den, Ondreji, dakujeme za napisanie. To, ako sa zobrazuje email zavisi aj od emailoveho klienta, ktoreho klient pouziva. Logo, nahravate do systemu v nejakej velkosti a Zooza zo zmensuje na prijatelnejsi rozmer. Pri forwardovani sa moze stat, ze emailovy klient (seznam, gmail, outlook), zmeni html a odstrani tieto limity. Samozrejme, to ako vyzera emailova sprava je zadefinovane a v drvivej vacsie pripadov a emailovych klientov sa to zobrazuje spravne. Napr.: ​ To ako vyzeraju spravy si mozete pozriet aj v historii sprav: https://zooza.app/#communication/sent_communication staci kliknut na email v zozname a dostanete sa do historie sprav pre daneho klienta, kde vidite +/- v akom format

### `215475423799903` -- 2026-08-10 10:46

**Asked:** Pod registráciou a ani profilom sa nič na stránke nezobrazuje, prečo ? Aj po refreshnuti stranky

**Human answered:** Dobry den, pani Birova, skusame to a vidime to v poriadku, skusali ste to ako konkretny klient? Neevidujeme vypadok na nasej strane ani u nasich dodavateloch.

### `215475423864720` -- 2026-08-10 10:56

**Asked:** Ahoj, viacerí rodičia hlásia, že keď sa chcú odhlásiť z hodiny a kliknú tlačidlo odhlásiť, či detail termínu, presmeruje ich to na domovskú stránku a neodhlási. ( odhlasujem ich teraz ja ručne) Môžete prosím skontrolovať a opraviť. Company: Zahorie_PK, fakturačné obdobie leto2026 , chybu pri odhlásení hlásili zatiaľ z kurzu Mini 1 a Mini2 ( napr reg. 495772, 495262, 496089) DakujemLenka ----------

**Human answered:** Dobry den, Lenka, ano, potvrdzujeme. Problem bol v tom, ze v ucte Zooza na nastaveniach widgetov/formularov nebola uvedena spravna adresa smerovania tych liniek z emailu. Uz sme to aktualizovali. A bude to od teraz fungovat opatovne spravne. Otazne je, ci ste tam robili nejake zmeny v ich nastaveniach?

### `215475423878813` -- 2026-08-10 10:59

**Asked:** Už to vidím aj ja, ďakujem

**Human answered:** Ok, super, dakujeme. Keby cokolvek, dajte vediet.

### `215475424461382` -- 2026-08-10 12:00

**Asked:** since the booking is confirmed even without pay we want an email to one who jus thavent paid it not the confiedm paid one

**Human answered:** Hi, just to clarify, the “Cancel from session” option is not related to cancelling the booking or payment. It only records that the parent/child will not attend that particular session. Even if make-up sessions or cancellation limits are not enabled, Zooza can still collect this attendance information so the instructor knows in advance how many children to expect. Technically, we can hide this option from the session reminder template and via CSS. However, this would be a custom change to the standard system logic and could have an impact later if you decide to use attendance, replacements or other related functionality. Before we remove it, I’d like to understand the concern behind it a lit

### `215475424552714` -- 2026-08-10 12:05

**Asked:** Vytvoril som v Zooze kurzy. v Extra poliach som nastavil nové extra polia, kde som dal na výber hodnoty. všetko som opakove uložil. keď to otvorím žiadn extra polia tam niesú a nič z toho mi neuložilo

**Human answered:** Dobry den, odpoved od AI nebola spravna. Nie je to sucastou PRO funkcionality. Su standardou sucastou formulara. Poslite link alebo screenshot, pozrieme sa na to. Možno predtým skúste refreshnut obrazovku. Dakujeme

### `215475427466894` -- 2026-08-10 14:46

**Asked:** why would a client be added to waiting list when spaces available and correct age for class

**Human answered:** Hi Sam, Yes, you can change the registration status from Waitlist to Enrolled. The reason this registration ended up on the waitlist was not the class capacity or age. The booking remained unpaid, and an automation connected to downpayments was triggered. You are not using downpayments, so I’ve now corrected that setting. For this registration, you have two options: - Go to the registration detail → Payments, add the outstanding class amount and the registration fee: https://asia.zooza.app/#registrations/1645/payments - Then go to Communication > Send Email for that registration and resend the booking confirmation, so the parent can open their profile and complete the payment. https://asia.z

### `215475428984771` -- 2026-08-10 16:02

**Asked:** ive moved someone from waiting list to booking and balance shows zero and debt zero how do I create invoice amount to send to them

**Human answered:** Hi Sam, You don’t need to create an invoice for this, as you’re not using invoices in your setup. First, go to the registration → Payments and add the outstanding amount you want the parent to pay, including the registration fee if needed: https://asia.zooza.app/#registrations/1645/payments Once the debt is set correctly, go to Communication → Send Email and resend the booking confirmation: https://asia.zooza.app/#registrations/1645/registrations_communication The confirmation email includes the payment status and a link to the parent’s profile, where they can complete the payment. In general, you can simply direct parents to their profile whenever they need to check or complete a payment: h

### `215475438764053` -- 2026-08-11 08:29

**Asked:** Hi there Noted and We have updated this code. Thanks Regards Gajan

**Human answered:** Hi Gajan, Thanks for the update, but I still see the old text live — "Cancel from session" is still showing on the profile page in the profile. Could you double-check where exactly you added it? I'm attaching a screenshot of a window.ZOOZA config block I found on the site with other translation overrides in it (registration.add_person, registration.capacity_full, etc.) — but it doesn't include course.set_attendance_cancel, so it looks like the new line either wasn't added, or it was added to a different script block that isn't loading on this particular page. Just to confirm the exact change needed: js 'course.set_attendance_cancel': "I can't attend this session", This needs to sit inside th

### `215475439705783` -- 2026-08-11 10:43

**Asked:** Vieme v ZOOZE nastavit mesacnu platbu na 30 euro mesacne ? aby to bolo na kalenadrny mesiac stale

**Human answered:** Dobrý deň, Jozef, ospravedlňujem sa, AI chat Vám na túto otázku neodpovedal úplne správne. Pri mesačných platbách záleží na tom, ako si to predstavujete — v Zooze fungujú dva režimy: 1. Kurzovné na splátky Máte finálnu sumu za školský rok a chcete umožniť, aby sa platila po mesiacoch. Nastavuje sa ako kurz v splátkach → kurzovné, pričom platobná šablóna je nastavená na mesačne, vždy k 1. dňu v mesiaci. 2. Členské Chcete zbierať peniaze mesačne, pričom suma je vždy rovnaká bez ohľadu na počet termínov v danom mesiaci. Používa sa to typicky pre kluby, kde skupina beží priebežne a nemá pevný koniec (aj keď skončiť môže). ​ Oba spôsoby vychádzajú z ceny za jeden termín. Pri členskom to však viet

### `215475441585471` -- 2026-08-11 13:38

**Asked:** Hello, I just created a free demo account however there was errors and I wasn't able to explore the system. Thanks, Samuel (Elizabeth Samuels)

**Human answered:** Hi Sam, Thank you for letting us know. The issue seems to be related to your browser settings, and we’ll look into it. In the meantime, please use this link to open Zooza in English: https://zooza.app/?lang=en-EN Please let me know if you still experience any issues. Best, Michal

### `215475452797887` -- 2026-08-12 02:46

**Asked:** I’ve had been logged out of my desktop account, tried to log in but not receiving the code

**Human answered:** Hi Sam, I see your message about being logged out. Were you trying to log in as a parent or into the Zooza admin? For the admin account, you need to use the email address connected to your access: sam@hartbeeps.com Log in here: https://asia.zooza.app/ Please try again with that email and let me know if the code still doesn’t arrive. Thanks,

### `215475452817212` -- 2026-08-12 02:51

**Asked:** I have got a client made two bookings

**Human answered:** Hi Sam, If you’re asking how two bookings for the same client can happen, Zooza does allow another registration to be created in the same class. The reason is that we prefer to capture the booking and the client data rather than block it completely, as there can sometimes be a valid business reason for creating another registration. The parent is warned that they already have a registration in that class and is given the option to go to their profile instead, but they can still continue and create another booking. If it is genuinely a duplicate and not an intentional second booking, you can simply cancel/delete the duplicate manually. Depending on your unpaid booking automation, Zooza may al

### `215475454882066` -- 2026-08-12 09:05

**Asked:** Dakujem pekne, vyskusame a keby bol problem dopytam sa Pekny den Barbora ​

**Human answered:** Dobry den Barbora. Jednoducho vojdete do polozky Tim a Nastavenia - Vseobecne -> Suhlasy a vytvorite novy suhlas (https://help.zooza.online/settings/setting-gtc-gdpr-consents/) V registracnom formulari sa zobrazuje ta druha polozka - Nazov suhlasu v registracnom formulari. Dolezite je aby ste ponechali prelinkovanie s dynamickou znackou AGREEMENT_URL, inak sa pouzivatelia nebudu vediet prekliknut na plne znenie suhlasu.

### `215475455553056` -- 2026-08-12 10:27

**Asked:** Dobrý den Martine, jedná se o klienta 221716 Helena Císařová od Petry Císařové petra.cisarova@a23.cz.

**Human answered:** Dobry den Lado, vedeli by ste poslat nejakeho vzoroveho klienta, ktoreho ste do retencie chceli zahrnut a retencnu ponuku nevidi?

### `215475470691665` -- 2026-08-13 09:20

**Asked:** chcela by som spravit refundaciu platby registracie https://zooza.app/#registrations/501069

**Human answered:** Dobry den Eva, je to chybovy kod priamo z tatrabanky a znamena "Ina chyba". Cize teoreticky moze ist o chybu na strane banky. Preverime to a ozveme sa.

### `215475472917958` -- 2026-08-13 12:35

**Asked:** Zdravím, kde a ako nastavím v zooza podmienku pre ohraničený vek od do pre prihlásenie klienta na daný kurz

**Human answered:** Dobry den Martina. Typ ceny za kurz sa meni v nastaveniach kurzu v karte Cena a platba. Ake konkretne nastavenie neviete najst?

### `215475473494431` -- 2026-08-13 13:26

**Asked:** Pre registrácie, ktorým vznikol prenesený náhradný termín vo fakturačnom období Jar 2026

**Human answered:** Dobry den Martina, pre ktory ucet chcete zmenit expiraciu? Nitra/Topolcany alebo Prievidza/Partizanske?

### `215475474551277` -- 2026-08-13 14:35

**Asked:** dobrý deň de sa dajú vytvoriť platobné šablóny pre zákaníka, kedď mu chcem dať na výber, či má platiť mesačne, alebo ročne

**Human answered:** Tim a nastavenia -> Fakturacia -> Platby. Tam sa nachadzaju jednak vseobecne nastavenia ako splatnost a notifikacie ohladom platobnych sablon a v spodnej casti obrazovky je mozne pridavat nove alebo menit nastavenia sablon.

### `215475477246849` -- 2026-08-13 18:07

**Asked:** Dobrý den, prosím Vás keď posielame emaily aj starším klientom majú možnosť sa odhlásiť z databázy? Lebo som poslala mail na viacerých klientov a píšu odhladom GDPR a nemožnosť sa odhlásiť. Ďakujem pekne za info Odoslané z iPhonu

**Human answered:** Dobry den. Priamo klienti sami to nevedia urobit. Vo vseobecnosti informacie zo Zoozy maju vzdy relevanciu ku aktualne prebiehajucim kurzom, preto sa z nich ludia nemozu odhlasit. Mozu sa odhlasit z nepovinnych emailov ako napriklad ranne pripomienky. V pripade ak posielate reklamny email na celu databazu - je potrebne pri jeho odosielani zaskrtnut policko Reklamna sprava a vtedy system neposle email tym ludom, ktori si taketo spravy dostavat nezelaju. Na detaile klienta je karta Poznamky a preferencie, kde je mozne zakliknut ci si dany klient zela alebo nezela dostavat reklamne spravy.

### `215475484351498` -- 2026-08-14 07:55

**Asked:** Dobrý den, chtěl bych se zeptat, zdali je v Zooze možné nastavit popis u generování faktur jako dokladu o zaplacení kurzu pro pojišťovny. 1) Dáme vygenerovat fakturu u registrace. 2) Zde můžeme upravit popis položky, který bude na faktuře. 3) Chtěl bych se zeptat, zdali jde popř. by bylo možné nastavit tento text, který je na faktuře, obecně pro všechny vygenerované faktury a to ideálně dynamickým

**Human answered:** Dobry den Tomas, Je to mozne nastavit na fakturacnom profile v casti Pokrocile nastavenia tam, kde sa nastavuje cislo faktury. Viete pouzit vsetky dynamicke znacky rovnako ako keby ste nastavovali emailovu sablonu. Pokial je znacka dostupna, vyplni sa. Vyriesi toto Vasu situaciu?

### `215475484934773` -- 2026-08-14 09:18

**Asked:** I'm afraid I can't find the button for skipping the login process?

**Human answered:** Hi Mara, I understand this is bigger change but it is easily skippable - there is a button to skip the login process if users don't want to log in. We've recently introduced plenty of features that rely on users being logged into the system - loyalty program with sibling discounts, priority booking for existing customers, auto enrollment etc, so this change is not so self imposed as it may seem. I would suggest waiting little bit to gather more feedback as this is fairly new and as with any change - it usually brings complaints. When dust settles we would make adjustments - either make the Continue as Guest option more visible or we'll figure out something else. One way to speed up the proce

### `215475487814046` -- 2026-08-14 13:36

**Asked:** ahoj Martin, tak som to robila, nespravilo sa mi to. Ja som si to presne tak pamätala, ale teraz mi to nejde.

**Human answered:** Dobry den Lucia. Funguje to nasledovne: Na urovni kurzu alebo skupiny poviete kolko platenych terminov ma skupina mat - to ste urobili - zadali ste cislo 36. To co Vam teraz system hlasi je toto: Mily admin, deklarujes ze tato skupina ma mat 36 platenych terminov, ale nepovedal si mi, ktore to su. Cize to co potrebujete urobit, je oznacit si vsetky terminy, ktore maju byt platene a pomocou hromadnej zmeny - pridat priznak ze su platene (ono sa to da urobit aj pri vytvarani terminov, ale kedze uz terminy mate vyrobene, je potrebne ten priznak urobit dodatocne). Pri kazdom termine sa Vam potom urobi taky symbol penazi.

### `215475502074984` -- 2026-08-15 20:35

**Asked:** human

**Human answered:** Dobry den Anastasiia, dakujeme za napísanie. Overili sme Vás ucet, budete mat dostupnejšie aj niektoré dalšie nastavenia. Zrejme ste sa chceli pozrieť ako by vyzeral Vas formulár a profil pre rodiča. Nájdete ho tu: https://zooza.site/jumps-sk-klub-s-r-o/calendar Celé riešenie viete nasadiť priamo na Váš web tak, aby klienti pri nakupovaní či manažovaní produktu nikam neodchadzali a zostávali len s Vašou značkou. Vidím, že ste nastavili prvý kurz Kangoo Power, ako otvorená hodina. Funguje to tak, že si klient vytvorí profil a následne si vybera termíny na ktoré chodí a za tie platí. Je možné predávať aj permanentku. Viete mi povedať viac o Vašich plánoch so systémom? V čom by mal pomôcť? Radi


## 2. Bot-only, highest risk first

`A_hard_signal` = routed to team, abandoned, or rated poorly. `B_no_kb_source` = the bot cited nothing from the KB. `C_reask` = the client asked again two or more times.

- **A_hard_signal** `215475484357630` 2026-08-14 07:56 -- re-asked 2x
  - Q: Dobrý deň, v kalendari mám nastavenych 37 terminov. Potrebujem, aby ten prvý bol skusobna hodina a 36 platenych. Nastavujem to cez terminy, ale nefunguje mi to. Čo môže byť problem?
  - cited: (no KB source)
- **A_hard_signal** `215475470597017` 2026-08-13 09:11
  - Q: chcela som refundovat platbu https://zooza.app/#registrations/501069/payments?online_payment=19156, ale pise, ze sa refundacia nepodarila, kod 13. co mam robit? platba bola robena formou CardPay
  - cited: Ceník — Zooza
- **B_no_kb_source** `215475423522332` 2026-08-10 10:08
  - Q: (no client message)
  - cited: (no KB source)
- **B_no_kb_source** `215475443774921` 2026-08-11 15:29
  - Q: (no client message)
  - cited: (no KB source)
- **B_no_kb_source** `215475472874593` 2026-08-13 12:31
  - Q: (no client message)
  - cited: (no KB source)
- **B_no_kb_source** `215475473539762` 2026-08-13 13:30
  - Q: (no client message)
  - cited: (no KB source)
- **B_no_kb_source** `215475497057229` 2026-08-15 08:39
  - Q: (no client message)
  - cited: (no KB source)
- **C_reask** `215475483223253` 2026-08-14 04:36 -- re-asked 36x
  - Q: Dobrý deň, prosím Vás chcem nastaviť platobné šablóny. Máme 6 kurzov, z toho v každom kurze máme mať 3 šablóny (mesačná, 3-mesačná a ročná platba). Každý kurz má ale rozličnú výšku úhrady, tým pádom potrebujem vytvoriť 18 platobných šablón?
  - cited: Smart Discounts for Kids’ Activities: A Practical Guide — Zooza Blog, Getting Started with Zooza | Zooza Help, Blocks Configuration and Management | Zooza Help
- **C_reask** `215475429846241` 2026-08-10 16:57 -- re-asked 11x
  - Q: Ahoj, viem si niekde pozriet historiu vymazanych registracii? Mam kolegynku s pravomocou aj mazat registracie a rada by som sa pozrela kolko registracii bolo zmazanych. Dakujem, Janka
  - cited: Registration and Booking FAQ | Zooza Help, Reports | Zooza Help, Bookings | Zooza Help
- **C_reask** `215475422158215` 2026-08-10 07:40 -- re-asked 9x
  - Q: can we put two concent i agree option in bookin form
  - cited: Clients | Zooza Help, Consents and agreements (GTC, GDPR) | Zooza Help, Consents and Agreements FAQ | Zooza Help
- **C_reask** `215475496536963` 2026-08-15 06:28 -- re-asked 9x
  - Q: Dobrý deň, mesačný kurz, ktorý trvá 10 mesiacov a v každom týždni je možnosť trénovať 2x do týždňa, alebo iba jeden z vybratých dní. ako nastavím typ kurzovného pri takomto spôsobe priebehu kurzu, prosím?
  - cited: Jak automatizovat vaše podnikání v oblasti dětských aktivit (aniž byste ztratili osobní kontakt) — Zooza, 10 chytrých způsobů, jak rozvíjet svůj podnik v oblasti aktivit pro děti během léta — Zooza, Doporučení jako nejsilnější marketing: Jak zapojit rodiče ještě před začátkem kurzů — Zooza
- **C_reask** `215475455132204` 2026-08-12 09:35 -- re-asked 6x
  - Q: Dobrý den, jak prosím vytvořím v systému retenci na přihlašování do vybraných skupin?
  - cited: Jak automatizovat vaše podnikání v oblasti dětských aktivit (aniž byste ztratili osobní kontakt) — Zooza, Ceník — Zooza
- **C_reask** `215475393207192` 2026-08-07 09:10 -- re-asked 5x
  - Q: Dobrý deň, vie mi s nastavením AI pomôcť externý lektor, ak mu dám prístup asistenta?
  - cited: Roles and Permissions FAQ | Zooza Help, Role Selection Guide | Zooza Help, User roles | Zooza Help
- **C_reask** `215475438184025` 2026-08-11 07:13 -- re-asked 5x
  - Q: vytvaram skupiny pod tanecny odbor 26/27 ale nezobrazuju sa mi
  - cited: Deleting/archiving courses - Zooza, Programmes, classes, and sessions explained | Zooza Help, Programmes, Timetables and Sessions FAQ | Zooza Help
- **C_reask** `215475490031349` 2026-08-14 16:44 -- re-asked 5x
  - Q: No môj zlatý, neviem nastaviť šablóny platobné v zoze. Neviem to tam vôbec nastaviť pre skupiny napríklad K4, kde chcem, aby mesačne platili 35 eur. Má vytvorenú šablónu, pozri sa na to, jak to mám vytvoriť, lebo ma už z toho drbne.
  - cited: Checklist pred spustením nových kurzov: Na čo nezabudnúť, aby sa sezóna nezačala chaosom — Zooza, Zooza PRO - Zooza, Registrační stránka pro dětské kroužky: 5sekundový návod — Zooza
- **C_reask** `215475394573038` 2026-08-07 12:17 -- re-asked 4x
  - Q: I want to change the email I use to log into my zooza account
  - cited: Login and Account FAQ | Zooza Help, Zooza 101 for Instructors | Zooza Help, User roles | Zooza Help
- **C_reask** `215475395064830` 2026-08-07 12:50 -- re-asked 2x
  - Q: Napis postup, ako zaznačiť nedostupnosť lektora na jednotlive dni počas celeho semestra
  - cited: Programmes List | Zooza Help, Instructors working hours | Zooza Help, Instructors | Zooza Help
- **C_reask** `215475442609874` 2026-08-11 14:29 -- re-asked 2x
  - Q: ako nastavit kurzovne na kurze na fix cenu
  - cited: Checklist pred spustením nových kurzov: Na čo nezabudnúť, aby sa sezóna nezačala chaosom — Zooza, Registrační stránka pro dětské kroužky: 5sekundový návod — Zooza, Nemůžete škálovat, co nemá logiku: CEO playbook pro vzdělávací a dětské značky — Zooza
- **C_reask** `215475456193532` 2026-08-12 12:02 -- re-asked 2x
  - Q: ako zyvsim pocet extra poli v kurze?
  - cited: Ceník — Zooza
- **C_reask** `215475484355876` 2026-08-14 07:56 -- re-asked 2x
  - Q: sparovanie platieb s bankou
  - cited: Zooza PRO - Zooza, Ceník — Zooza
- **C_reask** `215475484944616` 2026-08-14 09:20 -- re-asked 2x
  - Q: sparovanie uhrad s csob
  - cited: GoCardless Integration FAQ | Zooza Help, Email-notification payment matching | Zooza Help, Payment Pairing for Bank Transfers & Direct Debit | Zooza Help

## 3. Shipped but never communicated

_Nothing new._

## 4. Client email -- needs the review session

The Gmail connector needs an interactive login, so this step does not run here. In the session, search these senders over the window:

- `sarahmarsh@magikats.co.uk`
- `centralberks@weekicks.co.uk`
- `anna.blackwell@turtletots.com`
- `techsupport@zooza.online`

```
{from:sarahmarsh@magikats.co.uk from:centralberks@weekicks.co.uk from:anna.blackwell@turtletots.com from:techsupport@zooza.online} after:2026/08/07 before:2026/08/16
```
