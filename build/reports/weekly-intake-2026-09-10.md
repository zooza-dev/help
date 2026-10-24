# Weekly intake queue -- 2026-09-04 to 2026-09-10

Prepared 2026-09-11. Nothing here has been written to `content/` -- this is a queue.

## Counts

- Conversations with a human reply: **67**
- Bot-only conversations: **46**
- Bot-only needing a look: **37**
- Implemented specs not yet communicated: **27**
- Still waiting for a human answer: **3**

## 0. Nobody has answered these yet

Carried until somebody replies. A conversation leaves this list the moment a human answers it -- being closed is not enough, and neither is the bot having said something.

- `215475728999106` 2026-08-31 20:35 -- waiting **10 day(s)**
  - ahoj, prečo ked som si dala termíny tak mi zmyzla cena pri registrácií? dakujem
  - state: closed / routed_to_team
- `215475838977996` 2026-09-08 09:41 -- waiting **2 day(s)**
  - Dobrý deň Martin, ďakujeme za vysvetlenie. Rozumieme, že registrácie by sa vo všeobecnosti nemali vymazávať, keďže sú na ne naviazané platby a vymazanie spôsobuje problémy v reportingu. V tomto konkré
  - state: open / routed_to_team
- `215475877092690` 2026-09-10 07:28
  - Poprosím spojiť s ľudským agentom.
  - state: closed / routed_to_team

## 1. Human answers -- the gold standard

Read these first. A human answer that generalises belongs in the KB.

### `215474885457256` -- 2026-09-09 19:26

**Asked:** Zdravím, všimol som si vizuálny bug pri cenách za služby pri pridaní väčšieho počtu kusov. V tomto prípade som pridal do jednej registrácie 2x službu "uskladnenie bicykla" v hodnote 35 EUR/ks. Po pridaní sa suma na jednej položke znásobila a pôsobí to, akoby systém rátal (2x 35) x 2. V skutočnosti to ráta správne a teda len 2x 35 EUR. Technicky je to v poriadku, ale želaný stav to asi nebude a pre

**Human answered:** https://zooza.atlassian.net/browse/ZOOZA-4851

### `215474901539188` -- 2026-09-09 08:41

**Asked:** Dobrý deň, niekde musí byť problém pri prepájaní registrácií a následnému prevodu platieb na hlavnú registráciu. Vždy, keď sa snažím prepojiť 3 registrácie pod jednu dostávam sa do stavu, že prepojím dve a dve medzi sebou: Kvôli chybnému prepojeniu som nanovo vytvoril tri registrácie: 505170, 505171 a 505172. Pridal som im produkt a služby a snažil som ich prepojiť. Za hlavnú registráciu považujem

**Human answered:** Dobry den Jakub, nie, funguje to rovnako ako predtym ale menili sme vizualne ten proces (pridavali nahlad) plus mame rozrobeny update, ktory opravuje pridavanie poloziek k objednavke, ktora je pripojena k registracii. Skusime sa na toto pozriet, predpokladam, ze pojde len o nejasne pouzivatelske rozhranie alebo mozno su zmatocne texty a v skutocnosti tak nerobite operaciu, ktoru si myslite ze robite. Ozveme sa. Martin

### `215475168971012` -- 2026-09-09 08:38

**Asked:** Nahradne lekcie Dobrý deň, klientom a ani mne vo väčšine prípadov nejde prihlasit na nahradu i ked ju kapacita ponuka. Napr.teraz som prihladovala klienta Pekarcikova na zajtra o 10.30, system to zobral. Hned som prihlasovala i Beles a system ho uz nedal. Moznost ponukol. Toto sa mi opakuje. Prikladam info. Dakujem

**Human answered:** Dobry den Marcela. Do procesu nahrad vstupuje velmi vela parametrov a aj preto sme vyrobili nastroj, pomocou ktoreho si viete priamo v systeme sama overit, preco sa nahrada neponuka. Aj na Vasom screenshote je vidno tlacitko: Spustit diagnostiku MATKO. Kliknite na to tlacitko a z ponuky terminov najdite termin, ktory chcete otestovat a system Vam povie preco sa dany termin neponuka alebo naopak ponuka. V pripade, ze tuto diagnostiku spravite, uvidite bud priamo problem a budete vediet, co napravit, pripadne potom poslite screenshot z tejto diagnostiky a mozeme sa pozriet na to, ci je v systeme nejaka chyba. Najcastejsie byva problemom chybne nastavenie nahradok. Typicky priklad je, ze si kli

### `215475222027448` -- 2026-09-09 14:06

**Asked:** Dobrý deň, potrebujem automaticky obnovované členstvo pre skupinové fitness tréningy, ale nechcem mať priamy účet ani faktúry od Stripe alebo GoCardless. - Podporuje vaša integrácia CardPay automatické opakované platby kartou, teda tokenizáciu a následné platby bez nového zadávania karty? - Používa sa na to CardPay, ComfortPay alebo tatrapay+ od Tatra banky? - Je možné nastaviť členstvo na 8 vstup

**Human answered:** Dobry den Sergey, Zooza ponuka tuto moznost pre Stripe. Z Vasho pohladu aj z pohladu klienta v obchodnom vztahu vystupuje Zooza s.r.o. a ide o klasicku platbu kartou. Cize zakaznik plati Zooza s.r.o. a Vam fakturu vystavuje Zooza s.r.o. Faktury vystavujeme raz alebo dva krat mesacne v zavislosti od poziadaviek klienta a vzajomnej dohody. V tomto scenari nemusite mat svoj vlastny Stripe ani GoCardless ucet ale potrebujete mat entitu, kam budeme vyplacat peniaze. Peniaze nevyplacame na sukromne ucty a pred pouzitim sluzby si potrebujeme overit, ze mate zalozenu legalnu entitu v ramci EU. Z pohladu funkcnosti sa pytate na nieco co system nerobi. Zooza nema pod kontrolou vstup zakaznika priamo n

### `215475375978780` -- 2026-09-10 19:34

**Asked:** Denny prehlad nieje scrollovatelny v mobile view Dobry den, denny prehlad nieje scrollovatelny v mobilnom view. Iphone13,ios 26.4, zooza verze Neviem sa dostat dalej ako je prve zobrazenie Dakujem za pomoc Barbora

**Human answered:** Dobry den Barbora, pozrieme sa na to. Dakujeme za podnet.

### `215475377955457` -- 2026-09-07 10:30

**Asked:** ako mam nastavit aby lektorovi chodili notifikacie, kto sa prihlasil a odhlasil z jeho skupiny? chcem to nastavit na urovni skupiny, nie kurzu

**Human answered:** Dobry den Lenka, pri presuvani registracii mate moznost nastavit novy splatkovy kalendar. Najlepsie co mozete v tomto pripade urobit je nasledovne: Pri presuvani registracie vytvorite novy splatkovy kalendar, ktory nechate aplikovat od zaciatku skupiny. System potom vykalkuluje splatky rovnako akoby sa zakaznik registroval na zaciatku skupiny. Vsetky uhrady, ktore dovtedy urobil mu pri presune na registracii ostanu a tym padom bude treba doplatit len rozdiel

### `215475423522332` -- 2026-09-09 08:26

**Asked:** BBBA - prečo počíta skupinu zber záujmu do zooza statistik? ahojte, ​ narazili sme na problém, kde sme ziistili, že zooza nám počíta skupinu ktorá nemá termíny, ani cenu, ale iba miesta pre zber záujmu do statistik do kapacity a % naplnenosti ​ napriklad F.O. opatrovanie baby balance 2025/2026 - priloha č. 1 - tu je dané F.O. https://zooza.app/#courses/schedules?bp=3144&sort_by=created_desc&page=0

**Human answered:** poslane na Mata

### `215475470691665` -- 2026-09-09 08:42

**Asked:** chcela by som spravit refundaciu platby registracie https://zooza.app/#registrations/501069

**Human answered:** Dobry den Eva, je to chybovy kod priamo z tatrabanky a znamena "Ina chyba". Cize teoreticky moze ist o chybu na strane banky. Preverime to a ozveme sa.

### `215475507657595` -- 2026-09-09 08:30

**Asked:** Prosím, poraďte mi, nedarí sa mi to správne nastaviť. Dobrý deň. Prosím, poraďte mi, nedarí sa mi to správne nastaviť. ​ 1. Ako môžem nastaviť, aby sa jedna osoba nemohla na ten istý kurz zaregistrovať dvakrát? 2. Nefungujú mi platby za produkty cez profil klienta. Platba funguje iba počas registrácie. 3. Pri skúšobnej hodine odo mňa systém vôbec nevyžiadal platbu.

**Human answered:** ticket k bodu 1, biznisove rozhodnutie - volitelna moznost bod 3 - otvorene hodiny nemozu mat trial

### `215475533426839` -- 2026-09-09 08:19

**Asked:** prihlásnie na certifikačné školenie Dobrý deň, nejde mi prihlásiť na školenie, posielam link a screenshot. ​ https://student.mybrainacademy.sk/sk/slovakia/?course_id=9160&schedule_id=92616

**Human answered:** Dobry den Michal, ide o chybu na nasej strane. Nateraz je riesenie taketo: Vojdite do svojho profilu na stranke student.mybrainacademy.sk a odhlaste sa. Registracia Vam potom ukaze moznost zaregistrovat sa na skolenie. Ide o docasne riesenie, kym chybu odstranime a bude Vam registracny formular fungovat aj ako prihlasenemu pouzivatelovi.

### `215475570498867` -- 2026-09-09 08:18

**Asked:** platba Nefunguje platba za službu.

**Human answered:** Dobry den, preverime kde by mohla byt chyba a ozveme sa spat. Platbu za Zoozu sprostredkuva sluzba tretej strany, preto preverovanie moze trvat dlhsie.

### `215475666655561` -- 2026-09-08 10:38

**Asked:** Neodhlásilo náhradnú hodinu Ahoj, ​ Zore Mannion sme odhlásili náhradu v tejto skupinke: https://zooza.app/#calendar/1393355 ​ Nevrátil sa jej ale kredit, prosím o preverenie. Jej registrácia https://zooza.app/#clients/396445 ​ Ďakujem za preverenie. Michal

**Human answered:** Ahoj Miso, a sumarizacia v logoch hovori co? Pri kazdom odhlaseni mate v appke log, kde je napisane preco nahradna hodina nebola priznana.

### `215475719267008` -- 2026-09-08 12:59

**Asked:** how do i add another person to my account

**Human answered:** Done, all Tuesday sessions have been updated to the new duration. They're live on the class now, so you and parents will see the corrected times straight away. Give one a quick look and shout if anything doesn't match what you expected. https://uk.zooza.app/#courses/events?day=3&filter=filter&page=0&page_size=50&sort_by=upcoming_asc

### `215475721574632` -- 2026-09-09 08:18

**Asked:** Presuny v sieti Dobry den, po presunuti v sieti a naswlednom prijati na druhu pobocku potrebujeme aby registracia bola vymkazana nie zrusena. Dalej neviem najst presunute deti ktore cakaju na prijatie.

**Human answered:** Dobry den, registracie skutocne nechcete vymazavat. Hlavne ak na nich su prijate platby, sposobi Vam to problemy v reportingu ale nie len to. Vymazavat by ste mali iba registracie, ktore vznikli omylom, alebo su duplicitne, ale take zasa nie je dovod nikam presuvat. Sucasny proces presunu v ramci sieti sme navrhovali po vzajomnej dohode. Prijate ziadosti je vidno na dashboarde priamo na hlavnej obrazovke v ucte spolocnosti, do ktorej bolo dieta presunute.

### `215475734967717` -- 2026-09-04 10:59

**Asked:** pripomienka terminy Dobrý deň, prosím o kolkej sa posiela pripomienka pred termínom? v kurze JESS- Nestes / Praznovska sa dneska este ziadna neodoslala. kurz https://zooza.app/#courses/schedules/87539 a maju hodinu zajtra o 9:00 - v júni im pripomienky chodili a teraz uz nie.. Ďakujem za kontrolu a pomoc, Barbora

**Human answered:** Dobry den Barbora, kazda pripomienka ma svoj samostatny cas kedy sa odosiela a mozete si ho skontrolovat pre kazdu verziu rannej pripomienky samostatne: https://zooza.app/#communication/templates?type=event_notification

### `215475753194796` -- 2026-09-09 14:36

**Asked:** Dobrý den, chtěl bych se zeptat, zdali by bylo možné přidat možnost hromadné úpravy termínů i pro Dodatečné lektory? Po zkušenosti z minulého roku, kdy se stávalo, že místo zkušeného trenéra brali trénink 2 méně zkušení, tak jsem letos přidal do všech našich kurzů 1) Hlavního lektora 2) Všechny ostatní lektory mezi dodatečné lektory. To mi umožňuje měnit (přidávat) pohodlně lektora na konkrétním t

**Human answered:** Dobry den Tomasi, premyslam, ako by sme toto urobili tak aby to bolo prehladne a davalo to zmysel v ramci existujuceho modelu hromadnych zmien a napadlo mi, ze by sme to pravdepodobne vedeli ovela jednoduchsie vymysliet v ramci AI konektora. Preto sa chcem opytat ci ho pouzivate a ci by toto nebola pre Vas lepsia cesta? Momentalne AI konektor tuto zmenu urobit nevie, ale vedeli by sme to tam doplnit.

### `215475753258608` -- 2026-09-08 11:27

**Asked:** Term fees are displaying as AED0 on the website booking form for Core Netball classes - can you tell me what is wrong?

**Human answered:** Hi Tommy, this is caused by billable sessions you set on class level. This is a two step setup and you only did the first step: The default behaviour of the app is this: All sessions are considered billable - which means that if the app has to calculate the price it will take ALL sessions within the class and multiplies by Unit price. However. Not every class is like that and if that is the case then you might want to tell the class: Hey, I want to have 10 billable sessions in this class (This is the step 1 that you did). This switches the app's default mode and from now on only sessions that are EXPLICITLY marked as billable will be used for the price calculation. And you did not mark those

### `215475753653969` -- 2026-09-08 07:27

**Asked:** payments Dobrý deň. Ako môžeme uskutočniť prvé vyúčtovanie a nechať si vyplatiť platby za august na náš bankový účet? s pozdravom, Sergey Polyakov

**Human answered:** Dobry den, poslali sme email, prosím, potvrdte správnosť firemných údajov. Kolegyna už účet spracúvava.

### `215475774548005` -- 2026-09-09 08:16

**Asked:** export platieb Dobry den, robim export platieb za mesiac jul a august a v tabulke nevidim stlpec profil, kedze sa nam do zoozy tahaju platby z troch uctov potrebujem platby vyfiltrovat podla uctu na ktory patria. Doteraz tato moznost v stuahnutom exporte bola, zmenilo sa nieco?

**Human answered:** Dobry den Nikol, nerobili sme v exportoch ziadnu zmenu, ale preverime to.

### `215475779589808` -- 2026-09-04 13:45

**Asked:** NEjde podla navodu pripojit Zoozu na ChatGPT - v Juli zmenili postup https://zooza.app/#mcp Toto nefunguje. Prosim dajte tam aktualny presny postup, lebo podla Chat GPT noavodu som sa stratil. Vraj to asi ani mozno nejde pripojit, ak nemam nejaky enterprise ucet po novom...Dakujem

**Human answered:** Dobry den, pan Fedor, ano, chatgpt to menil uz niekolkokrat. Najlepsie je chatgpt dat rovno prompt a mu povedat nech vas navedie ako to urobi. On to zvladne. Navod sme kazdopadne zaktualizovali. Po novom je potrebne v nastaveniach zapnut developersky mod. A v pluginoch pridat custom plugin/connector. Ale pouzite na to rovno chat, nech vas navedie

### `215475787788785` -- 2026-09-07 07:38

**Asked:** nepravdive udaje v prehlade platieb Dobrý deň, Prosím vás v sekcii Platby - Celkový pprehlad platieb - graf kolečko mi neukazuje správne uhradené a neuhradené registrácie. Keď kliknem na červenú časť kolečka neuhradené tak mi vypíše sumu 3910€. Vedľa napravo ten mráčik ukazuje neuhradené registrácie 13 . Po rozbalení už len 9(spolu s čiastočne zaplatenymi). Keď som si na kalkulačke spočítal všetky

**Human answered:** Dobry den, pan Kiss, v tom dashboarde, pocita Zooza prijmy a vydavky za registracie v stave Registrovany alebo Hosť (nezapocitava tam napriklad zrusene registracie). Zaroven do tych dlznych (ciastocne, ci neuhradene), nezapocitava stav platby, kedy sa caka na uhradu. https://zooza.app/#registrations?billing_status=awaiting_payment&order_by=created_desc&page=0&page_size=20&person_id=0&payment_id=0&segment_id=0&schedule_id=0 V takom pripade to bude sediet.

### `215475787896072` -- 2026-09-04 11:23

**Asked:** Dobrý deň, klienta: https://zooza.app/#registrations/521388/payments s dvoma registráciami, ktoré uhradil som presunul do novej skupiny. V jednom prípade uhradená platba prešla pod novú registráciu a druhú platbu som presunul z nepotrebnej registrácie. Po doplatení príspevku sa však vygenerovala faktúra, ktorá nezahŕňa 115 EUR, ktoré boli presunuté a na FA ukazuje dlh k úhrade. Neviem to nijako zm

**Human answered:** Dobry den Jakub, pokial na detaile registracie vidite vsetky platby a faktura ich v sebe nezapocita na 99.99% to bude v datumovom rozsahu odkedy dokedy faktura cita platby. Ked date editovat fakturu tak tam mate dva datumovniky. Skuste sa s tymto pohrat a malo by to pomoct. Ak by to nepomohlo, ozvite sa a pozrieme sa na to.

### `215475791125308` -- 2026-09-09 11:38

**Asked:** kontrola nastavenia zlavy pri blokoch Ahojte, ​ chcela by som poradit pri kontrole nastavenia zlavy pri blokoch. Mam to nastavene ako v print screene. Zlava by mala byt nasledovna : jednotkova cena terminu je 13€ ale pri vybere 2 blokoch je 12€ a pri 3 blokoch je 11€. Mam 16 terminov v kurze, cize ked si vyberu 2 bloky 32. ​ Kurz: https://zooza.app/#courses/schedules/100002?edit=price ​ Posielam a

**Human answered:** Ahoj Jani, podla nastavenia, ktore mas na skupine pre blokovu cenu spravene, system vypocital zlavu spravne. Registracia v case kedy sa prihlasila mala pre sebou 30 terminov, co v nasobeni s cenou za jednotku robi 390 EUR. Kedze splnili podmienku dvoch blokov, aplikovala sa zlava 32 EUR, ktora je tam nastavena. system nevie nastavit zzlavu ako cenu za termin priamo - vie pracovat len s pevnou zlavou, ktora sa odpocitava z ceny podla poctu vybranych blokov. Cena, podla tvojho vypoctu, teda sedi iba v pripade, ze nejde o neskoru registraciu v pripad eneskorej registracie, pred jej manualnym potvrdenim, je treba vysku zlavy upravit podla toho, kolko terminov ma klient pred sebou. rozsirenie fun

### `215475791898887` -- 2026-09-06 12:11

**Asked:** where can i insert my terms and conditions?

**Human answered:** Hi Samuel, you can find it here: https://zooza.app/#settings/notifications in the menu: Team & Settings > Other > Notification centrum

### `215475803323183` -- 2026-09-08 07:05

**Asked:** Dobrý deň, všimol som si, že ste zmenili UI v rámci generovaných faktúr. Doteraz sa dala textová časť "popis služby" voľne opraviť podľa potreby, no v súčasnosti sa k tomu neviem dopracovať. Skúšal som aj pdf editor, no výsledok nedopadol najlepšie... Veľa kurzov nám dátumovo presahuje rok, no o príspevok na športovú činnosť sa dá žiadať len v rámci kalendárneho roka, takže veľa rodičov nás žiada 

**Human answered:** Dobry den Jakub, editovanie faktur by uz malo fungovat korektne.

### `215475811526581` -- 2026-09-07 04:40

**Asked:** Stripe Payments Hello! There seems to be an issue connecting to Stripe with the following error message - have tried on separate laptops and same issue when trying to take payment?

**Human answered:** Hi Tommy, Yes, I can see what’s happening. The Stripe message is actually pointing to the same issue as the browser ,,, if you look at the top of your screenshot, it says “Not Secure”. It means the page has been opened via http:// rather than https://, and Stripe won’t allow live payments on a non-secure connection. I’ve checked the Zooza widgets and everything is configured correctly there. The best fix is to ask whoever manages your hosting/domain to set up an automatic redirect from HTTP to HTTPS across the whole website. There are also WordPress plugins that can handle this, but ideally it should be configured at hosting/domain level. Once that redirect is in place, Stripe should always 

### `215475814140795` -- 2026-09-07 08:06

**Asked:** Neprehráva videá klientom Dobrý deň,nahrala som do dochádzky videá. Avšak keď som skúšala sa prihlásiť a chcem ich zobraziť automaticky ma hádže na starú stránku www.babybalancenitra.sk a tam mi ich nezobrazuje. Nová stránka je www.babybalance.sk, ale keďže kvôli niektorým produktom si chcem zachovať aj tú starú stránku. Ďakujem za odpoveď

**Human answered:** https://zooza.atlassian.net/browse/ZOOZA-4920

### `215475814816148` -- 2026-09-07 08:52

**Asked:** Potřebuji posla mail všem co chodí do konrétního místa (bazén Dobiášova)

**Human answered:** Dobry den, pan Fisenko, je viacero sposobov ako mozete poslat email na lokalitu. - Zoznam registracii, si do filtra vyfiltrujete miesto a poslete hromadnu spravu https://zooza.app/#registrations - V zozname skupin si vyberiete miesto a polsete hromadnu spravu cez poslat email https://zooza.app/#courses/schedules Na toto sa zoznam terminov nepouziva. Je tam este nejaky iny filter, ktory by ste potrebovali urobit? Ak chcete informovat napriklad o odstavke bazena v tento den, tak je mozne cez tlacidlo "hromadna uprava" poslat aj z kalendara, kde cez naseldne vyklikate terminy, ktorym chcete poslat spravu. Sprava sa odosle vsetkym uvedenym na termine. https://zooza.app/#calendar Dajte vediet, ci

### `215475818348922` -- 2026-09-09 05:44

**Asked:** Dobrý deň, Za posledné dva dni som našla v banke platby, ku ktorým rodičia uviedli správny VS ale neboli vôbec spárované. Chcem sa opýtať aká je chybovosť systému. Či mi odporúčate kontrolovať platby ručne? Myslela som, že program to spraví lepšie než ja. Je to nepríjemné upozorňovať zákazníkov, že neuhradili splátku a dostať v zapätí odpoveď, že však uhradili. V prílohe posielam printscreen plati

**Human answered:** Dobry den Anna, ak to spravne citam, ide o Fio banku. Ak je to tak, potom podla datumov na screenshotoch ide o obdobie, v ktorom evidujeme vypadky na parovacom systeme. Zhruba v polke augusta az do 2. septembra. Problem bol v tom, ze Fio banka robila viacere upravy na svojich systemoch (menili odosielatela emailov, viackrat menili emailove sablony) a teda doslo k medzere medzi ich zmenou a tym, kedy sme my upravili nas algoritmus. Moze sa preto stat ze najdete viacero platieb z tohto obdobia, ktore v Zooze nebudu. Bohuzial nevieme ovplyvnit, ci si banka emailove sablony meni alebo nie. Nedavaju o tom vediet vopred. Dakujem za pochopenie.

### `215475821347282` -- 2026-09-07 07:50

**Asked:** Ahojte, prosím vás viete prezistiť prečo AZET- maily nefungujú. Klientom od nás nič nepríde, nie je to ani v spame... posielam jeden účet ako príklad Zooza \ Registrácie \ 509538 - Lucia Steinsdorferová (Eliška Miklošková) .

**Human answered:** Ahoj, ano mame toto hlasenie od viacerych klientov. Emaily od nas smerom ku Azetu odchadzaju, cize chyba nie je u nas ale na ich strane. Snazili sme sa ich kontaktovat no zatial neuspesne, co mozete urobit je poprosit klientov aby skusili azet kontaktovat aj oni, mozno sa tam niekto zobudi a bude to riesit skor. Kazdopadne snazime sa to z nasej strany vyriesit.

### `215475822142393` -- 2026-09-07 08:18

**Asked:** Ukazovanie dieťaťa v dochádzke po presune Dobrý deň, v dochádzke ukazuje stále dieťa po presune. Presun je v rámci jednej pobočky a jednej školy. V dochádzke sa nemá čo ukazovať presunuté dieťa, nakoľko to je mätúce. Rodičom tiež ukazuje pôvodnú skupinu,napriek tomu, že dieťa mám presunuté v inej skupine. Viem, že sa to týka okrem BA1 aj Trnavy. Print screen v prílohe.

**Human answered:** Dobry den, pani Minarovic, dakujeme za napisanie. Registracia bola presunuta v case, ked klientke uz vznikol zapis na hodine v povodnej skupine, ak to chcete upravit, (napriklad skryt, alebo nahradit za iny), je to mozne priamo v detaile registracie. V tomto ma admin plnu kontrolu. https://zooza.app/#registrations/508561/attendance

### `215475822228486` -- 2026-09-07 09:57

**Asked:** Dobrý deň, v možnostiach pri "Online registrácii" je voľba "klient si vyberie", ktorá je vhodná pri možnosti registrácie na celý kurz resp. na vybrané bloky. V registračnom formulári problém nie je a funkcia funguje ako má. Problém však nastáva po prihlásení. Dieťa, ktoré sa prihlási na celý rok nie je zaradené v daných blokoch. Tzn., že ak sa mi na bicyklový blok prihlási 11 detí a na celoročný p

**Human answered:** Dobry den Jakub, ide o dva rozdielne rezimy registracie - ak sa prihlasujem na cely kurz, potom system predpoklada, ze sa prihlasujem do vsetkych terminov v skupine. Aj z pohladu ceny ide o dve samostatne vetvy - zatial co pri blokoch mate samostatne nastavenie ceny a zliav, pri celej skupine sa vypocet ceny riadi inymi pravidlami. Teda to co sa snazite odfiltrovat sa v jednom filtri urobit neda. Ak je zapnuty filter len na blok (na zozname registracii), potom tento filter nezahrna ludi, ktori su registrovani do celeho kurzu. Jedna cesta ako to obist je prihlasit tie deti na vsetky bloky, ale to je manualna praca. Otazka je, ako by ste si predstavovali aby to fungovalo? Preto spominam tu cen

### `215475823641439` -- 2026-09-09 17:13

**Asked:** BBBA - neaktivne miesta sa nam zacali objavovat v kalendari ahojte, prosim, mame vela miest/miestnosti/lokalit kde sme kedy boli a su aktualne neaktivne. tim-dlhodobo su neaktivne ​ a zrazu sa nam zacali vsetky tieto NEAKTIVNE miesta zobrazovat v kalendari ​ napr malina ihrisko joy zone rebella margaretka zaťko modra budova a pod ​ prosim o opravu je to velmi vyrusujuce ​ ps: nedeje sa to len mne 

**Human answered:** Cauko Sisa, toto sme nemenili, je to tak uz minimalne rok, odkedy sme redizajnovali filter na kalendari. Funguje to tak, ze lokality, ktore su na kalendari su vzdy navrchu aj s poctom terminov, ktore na kalendari su zobrazene. Ak tie lokality dalej nechcete tak ich jednoducho vymazte. Alebo ak chces tak mozeme dorobit nejaky priznak, ze lokalita je neaktivna a tym padom vam to zmizne nielen z kalendara ale aj zo skupin/registracii atd

### `215475824387919` -- 2026-09-07 12:09

**Asked:** Ahoj, posledných pár dní nám viac rodičov poslalo e-mail, že im pri registrácií neprišiel mail s prihlasovacím kódom. Čím to môže byť ?

**Human answered:** Dobry den Peter, ak su to zakaznici s emailovou adresou @azet.sk tak je to problem na strane Azetu. Snazime sa to s nimi riesit, no zatial bezuspesne :/

### `215475827252125` -- 2026-09-08 14:50

**Asked:** Dnes neodoslalo mailovú informáciu o zajtrajších hodinách klientom Dobrý deň, chcela by som sa spýtať. Dnes nechodil mail klientom o zajtrajšej hodine. Viete sa prosím na to pozrieť:? Ďakujem veľmi pekne. S pozdravom, Jarošová Simona - Baby Balance Nitra

**Human answered:** Dobry den, viete poslat priklad takej registracie, ktora nemala dostat notifikáciu? V Systeme vidime, ze pripominky odchadzali v poriadku.

### `215475831408120` -- 2026-09-09 08:12

**Asked:** Plne uhradená registrácia sa zbrazuje ako čiastočne uhradená Dobrý deň, možete sa prosím pozrieť na registráciu 17960 - Miroslav Morávek - https://zooza.app/#registrations/179680/payments ​ V platbách je nastavená dlžná suma 92.18e, k tomu je pripísaná platba 92.18e, ale na registrácii sa zobrazuje že je "čiastočne uhradená" - kde je tam nezhoda prosím ? ​ Ďakujem za pomoc, B

**Human answered:** Maťko naozaj, asi nejaké zaokruhlovanie, vyzerá to ok a predsa čiastočne uhradené.

### `215475831806487` -- 2026-09-08 07:09

**Asked:** Hello Zooza team, Your swimmer stages, badges and next-level re-enrolment look relevant. Please clarify whether you also support detailed individual skill assessments and progress history within each stage. I run a swimming school in Basel, Switzerland, and am looking for one system for bookings, payments and, most importantly, tracking each swimmer's learning progress. For an initial quotation, p

**Human answered:** Hi Stamatis, are you ready for the call? Will go through all your questions. https://meet.google.com/yhw-pqcm-eze?authuser=0

### `215475833122934` -- 2026-09-10 08:59

**Asked:** Problém s nastavením platobní šablony pro kurz Miniškôlka Platobní šablona '5x týždenne' pro paušální platbu v kurzu Miniškôlka nezobrazuje správný počet splátek, systém ukazuje pouze 3 místo 10, i přes nastavení 10 nebo 12 jednotek.

**Human answered:** Dobrý deň, Barborka, viete poslať nejakú konkrétnu registráciu, kde to chcete aplikovať. Predpokladám, že to chcete robiť ako admin, aby mal každý takúto platbu. Z toho čo popisujete by s tým nemal byť problém, len neviem najsť kurz o ktorom hovoríte. Tak pošlite jednu takú registráciu link, či meno. Pozriem a popíšem, ako to urobiť najlepšie. Našiel som len Miniškôlka (1,5-3) - tento ma typ platby členské, nie kurzovné. https://zooza.app/#courses/1799 Členské je jedna platba rovnaká každé obdobie bez ohľadu na termíny. Kurzovné je finálna suma rozdelené podľa typu platby na obdobia či počet podľa počtu termínov a cenu za termín. To je taký hlavný rozdiel :)

### `215475836852734` -- 2026-09-08 07:30

**Asked:** Payment issues Hello! There seems to be an issue with the payment page for some of our members - the below relates to the Friday Club booking from Vasilili Babich - he's tried checking out on a few occasions and gets error messages?

**Human answered:** Hi Tommy, unfortunately this is a bug on our end. We've issued a hotfix and the bug is now resolved.

### `215475838083926` -- 2026-09-09 11:39

**Asked:** Customer Provides IBAN for Invoice Payment Customer confirmed billing profile is correct and provided IBAN SK0602000000007289830751 for payment transfer as requested by support.

**Human answered:** Dobry den, prosim o doplnenie IBANu, kam peniaze zasleme. dakujem Katarina

### `215475838379717` -- 2026-09-08 11:12

**Asked:** Dobrý deň, po prázdninách sa neviem prihlásiť Zooza na mojom domácom počítači, keď som na home office.Čakám na prihlasovací kód a nechodí, skúšala som včera a dnes. Keďže pracujem aj z domu, potrebujem sa dostať do Zooza. Som prihlásená ako bilingvikaba@gmail.com.Prosím viete mi s tým pomôcť?Ďakujem,S pozdravom, -- Katarína Bachanová manažérka pre jazykové kurzy v Trnave Tel.: +421 918 827 059 Mai

**Human answered:** Dobry den, Katka, taky email neevidujeme v tom ucte. Zrejme ste pouzivali iny. Skúste ten, čo mate v mailovom podpise.

### `215475838453218` -- 2026-09-08 08:47

**Asked:** Chybová hláška Dobrý den, přestalo mi fungovat vyhledávání registrací. Chybové hlášky posílám v příloze. Mezitím to přestalo fungovat i Ladě.

**Human answered:** Dobry den, Petra, myslím, že v tomto prípade okamžite zafunguje, ked refreshnete obrazovku (znovunačítate). Dajte vedieť. Ďakujeme

### `215475838746836` -- 2026-09-08 09:18

**Asked:** Nezobrazuje sa mi detail registrácie na ziadnej pobocke https://zooza.app/#registrations/534891

**Human answered:** Dobry den, skuste pouzit ctrl+R, zrejme sa nedocitala obrazovka s datami. Dajte veideť,

### `215475839006121` -- 2026-09-08 11:36

**Asked:** Dobrý deň, z pobočiek nám hlásia, že klientom/rodičom s emailovou adresou na doméne azet.sk sa emaily zo Zoozy nedoručujú (napr. potvrdenia registrácie, notifikácie, upomienky platieb a pod.). Poprosíme o zistenie príčiny a návrh riešenia, aby v komunikácii s týmito klientmi nevznikali výpadky – momentálne netušíme, či daný email vôbec odišiel, alebo len neprešiel na strane azet.sk, a klienti tak 

**Human answered:** Dobry den Veronika, ano emaily smerom na domenu @azet bohuzial nie su dorucovane. Nejde o problem na nasej strane ale na strane Azetu. Zatial nemame od nich ziadnu spatnu vazbu v zmysle, toho, kedy by problem vedeli odstranit. Co sa tyka odpovedania na emaily tak, toto technicky nie je mozne. Vybrane sablony sa odosielaju z emailu no-reply@zooza.app ale drviva vacsina emailov sa odosiela priamo od nas a odpovede zbierame tym padom my v aplikacii. O tom, ze prisla nova odpoved viete dostat notifikaciu (zapina sa v notifikacnom centre)

### `215475839045054` -- 2026-09-08 09:54

**Asked:** Ako sa vytvára nulová registrácia? To znamená, že dieťa je registrované, ale neplatí za krúžok.

**Human answered:** Dobry den, pani Ruzickova, je mozne dat registracii zlavovy kupon, alebo ak uz registracia je vytvorena, tak date zlavu na registracii ale znizite dlh na 0 eur v detaile registracie > platby.

### `215475840214252` -- 2026-09-08 11:33

**Asked:** Hi, the booking system isnt prorating the cost

**Human answered:** Hi Sam, can you share more details or a specific booking? We're on it.

### `215475842733754` -- 2026-09-10 11:15

**Asked:** Dobry den, preposielam screenshot, platobny plan je 2 splatky, 20 percent zlava z kurzovneho. planovany dlh je iny ako suma na uhradu. ID klientky 533972 s pozdravom, Mgr. Lenka Pechová Kurzy, PR, marketing Tel. 0290900497 www.cirkuskus.sk FB / IG cirkuskus

**Human answered:** Dobry den Lenka ide skutocne o chybu. Na tom screenshote ktory posielate je korektna vyska splatky so zapocitanymi zlavami ale vo vnutri pri samotnej platbe sa komunikuje suma na uhradu bez zlavy. Opravime to. Dakujem za nahlasenie

### `215475843230655` -- 2026-09-08 14:26

**Asked:** Dear Michael and Martin, First of all, I would like to thank you for all your support and assistance during this period. Although I haven’t been as present lately, I know from Mara and Sorina that you have been extremely helpful and professional, as always. I’m reaching out now with a request that both Mara and Sorina have also raised, regarding the additional step for authentication or continuing

**Human answered:** Hi Nomin, thank you for reaching out. Michael probably did not have the time to write to Mara and Sorina, but just today we made the decision, on how to proceed with this and I think you'll be pleased to hear it. Essentially the problem is this - we do offer plenty of possibilities for priority registration, customer benefits such as loyalty programs or other upsell features that are only available to logged in users. However this is in conflict with a situation when the booking form is used as a lead generation tool as is in couple of your scenarios. ​ Therefore we decided to build a dedicated and greatly simplified new form specifically designed to capture leads. This new feature will also

### `215475848537071` -- 2026-09-08 20:33

**Asked:** HADZE DO PORADOVNIKA Dobrý deň, na kurze RYSY mi hádže potvrdené registrácie do poradovníkov, viete mi prosím povedať prečo? Už druhá registrácia tento týždeň. Ďakujem za odpoveď Michal Kiss

**Human answered:** Dobry vecer Michal, Mate tam pomerne vela skoncenych skusobnych lekcii - zakaznici sa nekonvertovali na plnu registraciu a tym padom Vam tam blokuju miesto. Je mozne nastavit by system automaticky cistil taketo registracie po nejakej dobe. Nastavuje sa to priamo v kurze - Nastavenia -> Skusobne hodiny -> Nastavenia automatizacie -> predposledne nastavenie - automaticky oznacit opustene registracie ako stratene po X dnoch. Alebo mozete tych ludi samozrejme obvolat pripadne im napisat spravu ako sa rozhodli.

### `215475855336922` -- 2026-09-10 08:30

**Asked:** Hi both, Apologies - I've hit another snag that neither I nor Claude can solve. We received 2 bookings for Friday Club before the programme was set up correctly. Its was for siblings Bettina and Beanie Barnett from Misty Barnett. I've tried following the ai support and Claude's instructions but the passes I've tried to add to the booking is just creating more balance as I can't check them as paid.

**Human answered:** Hi Tommy, - No there is currently only one single version of the Session reminder. That email can be customised just per company not per programme. - 13 Session reminders were sent in total so far. 6 for yesterday. You can get a quick glance on whether emails were sent on reports' dashboard at the very bottom. - Session notification is sent to everyone with the list of sessions that are available to book for them - in other words if I booked for friday session but there is no more upcomming sessions that I could book I should not get it. There might be adjustments you may want in regard of the session notifications and the mechanics how and to whom it is sent so if you have some comments reg

### `215475855889795` -- 2026-09-09 06:44

**Asked:** Dobrý de

**Human answered:** Dobry den, pre potrebu presunu ucastnika z kruzku do kruzku system poskytuje moznost presunu priamo z detailu registracie. ​ pekny den Katarina

### `215475857176613` -- 2026-09-09 09:19

**Asked:** Dobrý deň, klien sa registroval, zaplatil za krúžok, ale z určitého dôvodu si to rozmylel. Žiada o zrušenie registrácie a vrátenie platby. Komunikovala som to s účtovnou firmou. Je potrebné na existujúcu faktúru vystaviť dobropis. Ako mám postupovať? Ďakujem.

**Human answered:** Dobry den, Zooza nie je fakturacnym systemom a preto neposkytuje moznost vystavovat dobropisy. Je potrebne dobropis vytvorit mimo system a zakaznikovi ho odoslat manualne. Co sa registracie tyka, mate moznost najskor spravit refund, s tym, ze si zapisete do poznamky, ze peniaze mu posielate manualne naspat - ak klient neplatil cez online platbu platobnou branou, refund je iba administrativny ukon v systeme, peniaze neodidu automaticky. Nasledne, ked budete mat spraveny administrativny zaznam, mate moznost registraciu vymazat, aby Vam nezaberala miesto v skupine a aby neodchadzali automaticke spravy na klienta. tento krok mozte spravit cez detail registracie. pekny den Katarina

### `215475857919335` -- 2026-09-09 11:56

**Asked:** Dobry den, prosim mame maly problem. Mame kurz multicirkus, ktore rozne skupiny sa realizuju na roznych miestach. Skupina multicirkus 8-15 r utorok zac. 17:15, ma v popise uvedene, ze sa kona na mieste Nova trznica ale ked idem do rozpisu teminov, tak je tam uvedene ine miesto. tak isto aj v kalendari sa ukazuje na mieste, kde sa nekona. Spravne je meisto, ktore je uvedene v popise skupiny. Prosim

**Human answered:** Dobry den Lenka. Je bezne ze terminy v ramci jednej skupiny mozu mat ine charakteristiky. Napriklad pondelky mozu byt s lektorom Ferko a utorky s Miskom. Pondelky mozu byt 60 minutove a utorky 90 minutove. Rovnako to plati aj o lokalite. Cize jedna vec je lokalita na termine a druha vec je lokalita na skupine. Kedze skupiny su ponukane v ramci registracneho formulara, je na Vas, ktoru lokalitu, lektora alebo dlzku hodiny komunikujete zakaznikom. Skusim to este povedat inak - Na skupine mozete mat lokalitu X a na terminoch lokalitu Y. Ked vojdete do skupiny a jej nastaveni - a zmenite lokalitu - system sa Vas vzdy opyta tri veci: Mam zmenit terminy - len na skupine, na vsetkych terminoch, len

### `215475858021024` -- 2026-09-09 12:20

**Asked:** Stratena nahrada Dobrý deň, klientke prišlo potvrdenie o prihlásení nahrady na dnes 8:30 1/2r kurz, no ta náhrada tam nebola. Aj jej prišiel mail o tom. No keď som si pozrela z akého termínu trening odhlasovala, tak mi to ukazuje že sa neodhlásila, aj keď asi áno podľa mailu, inak by jej nešlo prihlásiť sa na dnešný trening. Vedeli by ste sa prosim na to pozrieť ? Ďakujem :)

**Human answered:** Dobry den, vasa klientka s reg.cislom 513647 si dna 2.9. odhlasila ucast na termine 3.9., pri com jej vznikol narok na nahradnu hodinu. Tuto nahradnu hodinu vyuzila na prihlasenie sa na termin na dnes, 9.9. o com svedci aj potvrdzovaci email, ktory ste zaslala. Rovnako tak sa vsak klienka nasledne opat prihlasila na povodnu hodinu kliknutim na tlacidlo, ktore ma na to k dispozicii vo svojom profile v dochadzke. Ak je povodny termin nenaplneny, system tento navrat povoli a nahradnu hodinu zrusi. Preto to vyzera, akoby nahradna hodina nikdy ani neexistovala. Kontrolovala som aj to, ci klientka prisla na termin 3.9. a teda ci na dnesnu hodinu prisla navyse, avsak v dochadzke z 3.9. nie je zazna

### `215475858272739` -- 2026-09-09 12:28

**Asked:** Prečo sa po nahodení skupiny nezobrazuje rodičom možnosť polročnej platby? Ako túto chybu odstránim? ​

**Human answered:** Dobry den, je platobna sablona aktivovana pre konkretny kurz a skupinu o ktoru ide? Je tato sablona spravnej formy - teda v pripade zberu penazi cez kurzovne ma sablona formu predplatenych sablon, v pripade clenskeho je to forma sablony pre clenske? prosim prekontrolujte si tieto dve zakladne otazky a nasledne, v pripade, ze su obe nastavenia spravene spravne nam zaslite cislo konkretnej skupiny a takisto konretnu sablonu, ktora by sa mala pri registracii zobrazovat. Dakujem Katarina

### `215475859264439` -- 2026-09-09 13:53

**Asked:** Termíny sa nezobrazuju v dennom prehľade Dobrý deň, prosím akú podmineku musí splniť vytvorený termín aby sa zobrazil v dennom prehľade ? máme termín, kde teda nieje žiaden študent a lektor bude pridelený ale má vytvorenú miestnosť. https://zooza.app/#courses/schedules/97913 a ked si otvorim denný prehľad aby som videla blokáciu miestnosti na ten deň tak ten termín tam nieje zobrazený. máme niekto

**Human answered:** Dobry den Barbora, denny prehlad zobrazuje obsadenost miestnosti na zaklade prihlasenych ucastnikov na dany termin - nie len podla priradenej miestnosti a lektora. Kedze Vase terminy nemaju priradenych studentov, system nema co do prehladu zobrazit. Aplikacia teda v dennom prehlade nedokaze zobrazit blokaciu miestnosti tak ako by ste potrebovali. Ak mate v aplikacii testovaciu registraciu, mozte si ju do tychto blokovanych terminov vykopirovat a tak si zabezpecit, ze sa zobrazia aj v dennom prehlade. pekny den Katarina

### `215475868453448` -- 2026-09-10 08:55

**Asked:** Pekný deň, prosím Vás existuje niekde slovenský manuál? Ďakujem

**Human answered:** Dobry den Eva, bohuzial slovenska verzia manualu neexistuje. Existuje iba vo forme AI agenta, ktory Vam vie odpovedat v slovencine. Je nieco konkretne s cim Vam mozem pomoct?

### `215475868521813` -- 2026-09-10 13:24

**Asked:** Mobil - domovska stranka Dobrý deň,m v mobile sa domovská stránka profilo zobrazuje s logom zooza a AI/profil tlačítkami v dolnej časti obrazovky, je to správne ? iOS 26.4.2, iPhone 13, Ďakujem za kontrolu, pekný večer., B

**Human answered:** Dobry den Barbora, ano je to tak zamerne, hoci presny dovod preco je to tak, vam nepoviem:) Ale mate pravdu, ze to vyzera divne. Zmenime to:)

### `215475875615367` -- 2026-09-10 08:48

**Asked:** Entry Passes Issue Recent FRIDAY CLUB booking #'s 1928 and 1929. 2 bundles of 12 sessions were booked and paid - member can only see 12 passes between both children in the account?

**Human answered:** Hi Tommy, it had to be probably just a system delay. I can confirm that user sees all passes in their parent portal at this moment.

### `215475876857929` -- 2026-09-10 13:23

**Asked:** BBBA - registrácia s nesprávnym mailom = zooza check OK - a čo dalej? ahojte, ​ je skvelé, že zooza robí check ci mail existuje,je tam X ale pre nás ako admina čo dalej? ja na toto natrafím náhodou ​ prosím existuje nejaký sposob ako si zo zoozy zobrazit prehlad registracii kde zooza dala na regisistracny mail X ? tym padom je asi preklep v maily, klient si urobi znova registraciu a nam sa blokuje

**Human answered:** Cauko, zatial taka funkcia nie je. No v principe ak je tam to Xko tak to znamena, ze ten email nie je funkcny, cize ak ti na registracii klient nechal telefonicky kontakt - mozes mu zavolat a zistit aky je spravny email a nasledne ten email opravit. Ak nemas ani telefon, tak tu registraciu mozes rovno vymazat. Jedina sanca je, ze by ta ten zakaznik kontaktoval cez vseobecny email ale to si skor asi urobi novu registraciu.

### `215475876867204` -- 2026-09-10 09:28

**Asked:** Dobrý deň, ako mám zmeniť klientovi spôsob platby z ročného na polročné (2 splátky). https://zooza.app/#registrations?user=Han%C4%8D%C3%ADk&order_by=created_desc&page=0&page_size=20&person_id=0&payment_id=0&segment_id=0&schedule_id=0

**Human answered:** Dobry den Daniela, viete prosim priblizit v com spociva problem?

### `215475876901122` -- 2026-09-10 08:46

**Asked:** Missing Payment This payment is marked as outstanding in Zooza and incomplete on Stripe but the customer has received a payment confirmation message. Any ideas?

**Human answered:** Hi Tommy. The payment was completed eventually. The expiration means that user created an intent to pay but either got distracted or just stepped away from their pc/phone and never finished the payment. This parent did that twice and eventually paid on third attempt. .

### `215475877047616` -- 2026-09-10 09:23

**Asked:** Návrh na vylepšenie / funkcia hromadného e-mailu – odstránenie klienta zo zoznamu príjemcov Dobrý deň, obraciam sa na vás s podnetom na vylepšenie systému pri odosielaní hromadných e-mailov. Súčasný problém: Pri posielaní hromadného e-mailu na konkrétnu lokalitu (napr. Komárno) (nerozlisujem fakturacne obdobie, chcem zaslať všetkým klientom v danej lokalite) potrebujem zo zoznamu príjemcov manuáln

**Human answered:** Dobry den Janka, dakujeme za podnet, zapracujeme to do systemu co najskor. Martin

### `215475878514319` -- 2026-09-10 11:10

**Asked:** Vykazuje, ze email ma nesprávny formát Ahojte, chcela by som vas poprosiť. Klientke sme posielali email, ze sa kurz posuva. Neprisiel jej a v systeme mi ukazuje, ze email ma nespravny formát. Vypytala som si novu emailovu adresu ci to nebude fungovat a stale to zobrazuje. Prosim mozete sa na to pozriet? Ďakujem veľmi pekne. S pozdravom, Jarošová Simona

**Human answered:** Skus prosim poslat ten email este raz, ci to teraz prejde.

### `215475879206768` -- 2026-09-10 16:37

**Asked:** Spoj ma prosím s ľudským asistentom.

**Human answered:** Dobry den Daniela. Mozete na urovni kurzu nastavit aby prislusne extra polia boli nepovinne. Nastavuje sa to na kurze - Nastavenia -> Extra polia -> Firemne udaje. Je tam checkbox, ktorym mozete firemne udaje nastavit ako nepovinne a tym padom sa pani riaditelka bude vediet zaregistrovat aj bez vyplneneho ICO.

### `215475879590045` -- 2026-09-10 13:32

**Asked:** I have a session tonight. capacity is 20. 15 players have confirmed coming. When parents are trying to book via the website the session is not showing.

**Human answered:** Hi Louis, could you please do send me a link to that session? We will have a look why it's not showing, whether its some kind of setting or what... Thank you

### `215475880263676` -- 2026-09-10 13:56

**Asked:** Dobrý deň, začalo sa nám na niektorých počítačoch zobrazovať čierne pozadie. Nebolo by to až také tragické, pretože konečne dobre vidieť oranžové písmo, ale v kalendári vôbec nevidno mriežku ani hodiny (čas) ďakujem

**Human answered:** Dobry den dagmar. To v akom style sa zooza zobrazuje si mozete individualne prisposobit vo svojom pouzivatelskom profile. System sa automaticky prepina do tmaveho rezimu ak tak mate nastaveny pocitac ale da sa to aj prepnut tak aby bol stale v svetlych farbach. Poslite prosim screenshot ako sa Vam to zobrazuje a farby samozrejme doladime. Tato zmena je v aplikacii uz vyse roka, takze to, ze sa Vam to zacalo zobrazovat iba teraz bude pravdepodobne sposobene nejakou aktualizaciu v ramci tych pocitacov


## 2. Bot-only, highest risk first

`A_hard_signal` = routed to team, abandoned, or rated poorly. `B_no_kb_source` = the bot cited nothing from the KB. `C_reask` = the client asked again two or more times.

- **A_hard_signal** `215475728999106` 2026-08-31 20:35 -- re-asked 6x
  - Q: ahoj, prečo ked som si dala termíny tak mi zmyzla cena pri registrácií? dakujem
  - cited: Price and payment setup | Zooza Help, FAQ — Programmes | Zooza Help, Getting Help and Support | Zooza Help
- **A_hard_signal** `215475877092690` 2026-09-10 07:28 -- re-asked 4x
  - Q: Poprosím spojiť s ľudským agentom.
  - cited: (no KB source)
- **A_hard_signal** `215475838977996` 2026-09-08 09:41
  - Q: Dobrý deň Martin, ďakujeme za vysvetlenie. Rozumieme, že registrácie by sa vo všeobecnosti nemali vymazávať, keďže sú na ne naviazané platby a vymazanie spôsobuje problémy v reportingu. V tomto konkrétnom prípade však ide o inú situáciu, ktorú sme na
  - cited: (no KB source)
- **B_no_kb_source** `215475824103561` 2026-09-07 13:59
  - Q: Nefungujuci videozaznam Live Dobry den, Registracii nejde spustit videozaznam live prednasky 526588 - Sára Culinková (Sára Culinková) Vid priloha, dakujem
  - cited: (no KB source)
- **B_no_kb_source** `215475782192470` 2026-09-03 20:19
  - Q: Pri kopirovani dietata do skupiny nenastavi system registracny poplatok Pri kopirovani dietata do skupiny nenastavi system registracny poplatok 80eur no musím ho nastavit ja sama
  - cited: (no KB source)
- **B_no_kb_source** `215475839703443` 2026-09-09 08:08
  - Q: nesprávne údaje pri viacerých registráciách z jedného zariadenia Ahoj, zasa máme situáciu s prepísaním údajov: https://zooza.app/#registrations/535005 https://zooza.app/#registrations/535015 ​ Obe majú iný mail aj iného účastníka, ale opäť sa prepísa
  - cited: (no KB source)
- **B_no_kb_source** `215475846753555` 2026-09-08 16:57
  - Q: Kde v systeme prosim najdem prehľad o tom, ze Kolko deti je prihlásených na ktory kurz? Lucia Hoxha Fertility Coach Supporting Women all over the world on Their Journey Towards Motherhood ​ www.luciahoxha.com Ambassador of Global Institute for Extrao
  - cited: (no KB source)
- **B_no_kb_source** `215475855375246` 2026-09-09 08:00
  - Q: ukazovanie obsadenosti na blokoch Ahojte, zistila som, ze pri blokoch mi ukazuje obsadenost terminu, a nie bloku. Je mozne s tym nieco urobit? Posielam konkretne termin. v skupine mam 10 deti ale mam odhlaseneho niekoho https://zooza.app/#calendar/14
  - cited: (no KB source)
- **B_no_kb_source** `215475856035677` 2026-09-09 07:56
  - Q: Zle nastavenie rozlovenie strany a zalomenie na Skupinach, ale asi aj na klientoch a inde, kuknite to a otestujte to s MAX moznym poctom slov/pismen... Zle nastavenie rozlovenie strany a zalomenie na Skupinach, ale asi aj na klientoch a inde, kuknite
  - cited: (no KB source)
- **B_no_kb_source** `215475858917679` 2026-09-09 12:29
  - Q: Sibling Discount issue A member has tried booking FRIDAY CLIUB booking numbers 1920 and 1921 but sibling discount isn't being applied. Any ideas as to why?
  - cited: (no KB source)
- **B_no_kb_source** `215475868448556` 2026-09-09 20:02
  - Q: Skupiny - prekryvajuce UI Dobrý deň, pri zobrazeni rolovacieho zoznamu pri skupine, na obrazovke zozname skupin, sa zoznam prekrýva s UI štatistík v dolnej časti obrazovky - príklad v prílohe. Ďakujem za opravu, Pekný večer, B
  - cited: (no KB source)
- **B_no_kb_source** `215475876907537` 2026-09-10 07:02
  - Q: Dzień dobry, zauważyłem w Zooza rezerwacje online, grafiki, płatności i listy oczekujących. To bardzo telefoniczna branża. Pomyślałem, że Voice AI mógłby być ciekawym rozszerzeniem Państwa oferty dla szkół językowych i firm zajęciowych. Agent AI może
  - cited: (no KB source)
- **C_reask** `215475791219335` 2026-09-05 02:49 -- re-asked 9x
  - Q: How to view attendance registers?
  - cited: Concepts & glossary | Zooza Developer Docs, Billing and invoicing | Zooza Help, VAT management | Zooza Help
- **C_reask** `215475857821177` 2026-09-09 10:52 -- re-asked 9x
  - Q: Can I turn off people being able to book workshops and just have them being able to book a trial? ​
  - cited: Trial sessions | Zooza Help, Blocks Configuration and Management | Zooza Help, Manage trial bookings — reschedule, convert, and close | Zooza Help
- **C_reask** `215475855266366` 2026-09-09 04:54 -- re-asked 7x
  - Q: How can I create Entry Passes for a clients booking?
  - cited: Edit automatic notifications of an upcoming session | Zooza Help, Message Templates | Zooza Help, Creating entry passes | Zooza Help
- **C_reask** `215475868206271` 2026-09-09 20:34 -- re-asked 7x
  - Q: nemozem zmenit email lektorky
  - cited: Client Management FAQ | Zooza Help, Login and Account FAQ | Zooza Help, Clients | Zooza Help
- **C_reask** `215475774458554` 2026-09-07 08:55 -- re-asked 6x
  - Q: Dobry den, chcela by som sa spytat na report prijatych platieb. Doteraz sa v tabulke nachadzal aj stlpcek kde bol spomenuty profil, kedze sa nam do zoozy natahuju platby z troch uctov tak som vyuzovala filtrovanie na zaklade tychto troch profilov
  - cited: Jak automatizovat vaše podnikání v oblasti dětských aktivit (aniž byste ztratili osobní kontakt) — Zooza, Zooza PRO - Zooza, Payments and Billing FAQ | Zooza Help
- **C_reask** `215475857824306` 2026-09-09 12:20 -- re-asked 6x
  - Q: Sibling discount on Friday Club?
  - cited: Discounts and Sibling Pricing FAQ | Zooza Help, Automatic payment reminders | Zooza Help, Price and payment setup | Zooza Help
- **C_reask** `215475865695873` 2026-09-09 18:32 -- re-asked 6x
  - Q: viem nastavit v zpoza aby v kalnedari na nasej stranke neukazovali informacie napríklad kto uci danu hodinu?
  - cited: Deploying the Zooza app on your website - Zooza, Customizing widgets | Zooza Help, Booking Widget FAQ | Zooza Help
- **C_reask** `215475870830834` 2026-09-09 22:02 -- re-asked 6x
  - Q: dá sa hromadne vypnúť zobrazovanie skupín na úrovni online zobrazovania v kalendári na webovej stránke?
  - cited: Programmes, classes, and sessions explained | Zooza Help, Programme Settings | Zooza Help, Registration and Booking FAQ | Zooza Help
- **C_reask** `215475824318768` 2026-09-07 10:31 -- re-asked 5x
  - Q: ako spravne nastaviť párovanie
  - cited: Payment Pairing for Bank Transfers & Direct Debit | Zooza Help, Inbound payments — setup and pairing | Zooza Help
- **C_reask** `215475838174690` 2026-09-08 07:56 -- re-asked 5x
  - Q: Hallo, ich habe einen konkreten Anwendungsfall, und würde fragen ob Sie das lösen können?
  - cited: Zooza 3.7: Back-to-School-Release, das Zeit spart und Kurse füllt — Zooza, Schluss mit Pauschalrabatten: Smarte Vorteile — Zooza, Zooza PRO - Zooza
- **C_reask** `215475707398670` 2026-09-04 12:01 -- re-asked 4x
  - Q: Ako odoberem zo zoozy neaktivneho lektora?
  - cited: Jak zautomatyzować firmę zajmującą się zajęciami dla dzieci (bez utraty osobistego podejścia) — Zooza, Zooza PRO - Zooza, Cennik — Zooza
- **C_reask** `215475838139010` 2026-09-08 07:48 -- re-asked 4x
  - Q: Ahoj, chcem si overiť nastavenie pripomienok k platbe. V jednom programe už máme spustené prihlasovanie, no tréningy začnú až v októbri. Ak na úrovni kurzu nastavím možnosť ,,odoslanie pripomienky pred začatím kurzu": 1.pripomienka - 6 dní pred začia
  - cited: Automatic payment reminders | Zooza Help, Price and payment setup | Zooza Help, Payments and Billing FAQ | Zooza Help
- **C_reask** `215475856533778` 2026-09-10 04:29 -- re-asked 4x
  - Q: where do I find the dates set for automation emails to be sent after a trial has eneded
  - cited: Manage trial bookings — reschedule, convert, and close | Zooza Help, Programme Automations | Zooza Help, Programme Settings | Zooza Help
- **C_reask** `215475889682869` 2026-09-10 21:32 -- re-asked 4x
  - Q: for a payment plan like the instalment one, how is the remaining one collected
  - cited: Getting Started with Zooza | Zooza Help, Trial Classes FAQ | Zooza Help, Payment Pairing for Bank Transfers & Direct Debit | Zooza Help
- **C_reask** `215475788907286` 2026-09-04 10:44 -- re-asked 3x
  - Q: if i delete a session that has a trial client booked into - will they be informed?
  - cited: Manage trial bookings — reschedule, convert, and close | Zooza Help, Programmes, Timetables and Sessions FAQ | Zooza Help, Managing sessions in a class | Zooza Help
- **C_reask** `215475821156768` 2026-09-07 06:47 -- re-asked 3x
  - Q: Vreau să scriu rezumatul lecției de ieri pentru grupa de la 11:00
  - cited: Cum să automatizați afacerea dvs. de activități pentru copii (fără a pierde atingerea personală) — Zooza, Attendance and Catch-up Classes FAQ | Zooza Help, Daily Calendar — Room Swimlane View | Zooza Help
- **C_reask** `215475859668709` 2026-09-09 13:37 -- re-asked 3x
  - Q: Ako mám u registrovaného klienta/dieťaťa nastaviť nulovú platbu? Je tam použitá 100% zľava na krúžok.
  - cited: Payment Correction vs Refund Guide | Zooza Help, Zooza Glossary | Zooza Help, Bookings | Zooza Help
- **C_reask** `215475870169149` 2026-09-09 21:24 -- re-asked 3x
  - Q: informácie k úhrade , klientovi príde mail s údajmi na úhradu bez QR code ale po otvorení profilu v časti platba QR code, dá sa nastaviť aby QR code prišiel aj v maily?
  - cited: Jak automatizovat vaše podnikání v oblasti dětských aktivit (aniž byste ztratili osobní kontakt) — Zooza, Checklist pred spustením nových kurzov: Na čo nezabudnúť, aby sa sezóna nezačala chaosom — Zooza, Proč řešení „neviditelného“ rodičovského problému buduje silnější značku — Zooza
- **C_reask** `215475837745702` 2026-09-08 06:32 -- re-asked 2x
  - Q: ako vytvorím QR kod na prihlasenie do kurzu
  - cited: Getting Started with Zooza | Zooza Help, Share a course or class registration link | Zooza Help
- **C_reask** `215475840366098` 2026-09-08 11:04 -- re-asked 2x
  - Q: In my programmes i have a team membership where would i find the link to send to parents so they can sign up
  - cited: Registration and Booking FAQ | Zooza Help, Onboarding and Launch FAQ | Zooza Help, FAQ — Programmes | Zooza Help
- **C_reask** `215475843046845` 2026-09-08 13:28 -- re-asked 2x
  - Q: Ahoj, chcem sa ubezpečiť ohľadom nastavenia. Na úrovni programu nastavené, typ platby (v splátkach, kurzovné), jednotková cena 59,90€. Na úrovni skupiny, som prepísal jednotkovú cenu na 7,4875€ (nakoľko tam máme v kurze 8 tréningov). Je to tak správn
  - cited: Price and payment setup | Zooza Help, Create a programme | Zooza Help
- **C_reask** `215475855673710` 2026-09-09 05:50 -- re-asked 2x
  - Q: When a client enrolls in Friday Club (pay-as-you-go) what is the sequence of automated templates that get shared? When they use an entry pass to book a specific session, which template is sent?
  - cited: Edit automatic notifications of an upcoming session | Zooza Help, Message Templates | Zooza Help, Automated notifications overview | Zooza Help
- **C_reask** `215475857893236` 2026-09-09 11:24 -- re-asked 2x
  - Q: Ahoj, prosím ťa v poslednej dobe nám priebežne rodičia píšu že im nepríde spätný e-mail s prihlasovacím kódom. Po kontrole, udali správnu adresu, nemajú e-mailovú adresu azet.sk, každopádne registrácia prebehne, aj v systéme daných športovcov eviduje
  - cited: Login and Account FAQ | Zooza Help, Client Profile FAQ | Zooza Help, Sending email/SMS to clients | Zooza Help
- **C_reask** `215475863439833` 2026-09-09 16:09 -- re-asked 2x
  - Q: Chcem dcéru prihlásiť na ytu ako?
  - cited: Zooza PRO - Zooza, Registrační stránka pro dětské kroužky: 5sekundový návod — Zooza
- **C_reask** `215475869917705` 2026-09-09 21:15 -- re-asked 2x
  - Q: hey, can I see a document how to set up working hours and setting absence in the instructors profile ? how to approve new lesson with student?
  - cited: Programme Settings | Zooza Help, Instructors working hours | Zooza Help, User roles | Zooza Help

## 3. Shipped but never communicated

| Repo | Spec | Title | Updated |
|---|---|---|---|
| api-v1 | API-20260626-001 | Administrative refund must not crash on null gateway response (Tatra Banka) | 2026-09-09 |
| api-v1 | API-20260811-001 | full2 courses: hidden (ignore) attendance silently counts as going, blocking auto-cancel-empty-event | 2026-09-09 |
| api-v1 | API-20260817-001 | Clients list \"Active clients\" filter reads a stale denormalized role column instead of live users_companies.role | 2026-09-09 |
| api-v1 | API-20260907-004 | Cross-engine invoice due date from companies.invoice_due_days | 2026-09-07 |
| api-v1 | API-20260907-001 | Email template merge-var contract: repair the broken vars and expose the entity ↔ template linkage | 2026-09-07 |
| api-v1 | API-20260907-002 | Profile widget: choose the booking entry for pay-as-you-go classes (open_course_booking_mode) | 2026-09-07 |
| api-v1 | API-20260907-003 | Vimeo embed domains: a company-managed whitelist, suggested from the widgets we already know, applied to every video in bulk | 2026-09-07 |
| api-v1 | API-20260908-002 | App crossroad — server-issued redirect into a sibling Zooza app | 2026-09-08 |
| api-v1 | API-20260908-003 | Local seeding of the network (franchise) report read model | 2026-09-08 |
| api-v1 | API-20260908-004 | A block's advertised availability must equal what its write gate accepts | 2026-09-08 |
| api-v1 | API-20260908-001 | Trainer financial data visibility | 2026-09-08 |
| api-v1 | API-20260909-002 | Network-controlled row order in custom report documents | 2026-09-10 |
| api-v1 | API-20260909-002 | Do not write refunds to the ledger when the gateway declines | 2026-09-09 |
| app | APP-20260902-002 | Communication templates screen redesign — merge-var guidance, in-app tag reference, clearer versions, per-variant course enablement | 2026-09-07 |
| app | APP-20260902-003 | Course-settings Online-booking email picker UX — Customize email, full-width layout, close the variant/save trap | 2026-09-07 |
| app | APP-20260902-001 | Creatable label picker on the Additional fields (extra_fields) age-limit setting | 2026-09-02 |
| app | APP-20260907-002 | Restore invoice Edit action on the registration Invoices screen (listing view) | 2026-09-07 |
| app | APP-20260907-001 | Profile-widget setting: how pay-as-you-go programmes offer session booking (open_course_booking_mode) | 2026-09-07 |
| app | APP-20260907-003 | Vimeo embed domains — manage the company-wide list of hosts allowed to play the company's videos | 2026-09-07 |
| app | APP-20260908-004 | Head/body split embed method + method toggle in widget settings | 2026-09-08 |
| app | APP-20260908-001 | Hide financial information from instructor roles | 2026-09-08 |
| app | APP-20260908-003 | Payment-schedule \"na úhradu\" must be net, not gross | 2026-09-08 |
| app | APP-20260909-002 | Directional money formatting — signed figures with a balance state word | 2026-09-09 |
| app | APP-20260909-001 | Transfer form: fee-on-manual-balance, unified payment wording, scenario-driven plan choice | 2026-09-09 |
| app | APP-20260910-001 | Compose: exclude recipients by user_id when sending to Clients (selection target group) | 2026-09-10 |
| widgets-v1 | W1-20260707-001 | Registration UX: freely switch between whole-course, block and trial options, with correct pricing | 2026-09-09 |
| widgets-v1 | W1-20260908-001 | Head/body split embed method + placeholder mounting | 2026-09-08 |

Stamp `docs_communicated` in the spec once the KB covers it.

## 4. Client email -- needs the review session

The Gmail connector needs an interactive login, so this step does not run here. In the session, search these senders over the window:

- `sarahmarsh@magikats.co.uk`
- `centralberks@weekicks.co.uk`
- `anna.blackwell@turtletots.com`
- `techsupport@zooza.online`

```
{from:sarahmarsh@magikats.co.uk from:centralberks@weekicks.co.uk from:anna.blackwell@turtletots.com from:techsupport@zooza.online} after:2026/09/04 before:2026/09/11
```
