# Weekly intake queue -- 2026-08-30 to 2026-09-03

Prepared 2026-09-04. Nothing here has been written to `content/` -- this is a queue.

## Counts

- Conversations with a human reply: **39**
- Bot-only conversations: **33**
- Bot-only needing a look: **30**
- Implemented specs not yet communicated: **10**
- Still waiting for a human answer: **4**

## 0. Nobody has answered these yet

Carried until somebody replies. A conversation leaves this list the moment a human answers it -- being closed is not enough, and neither is the bot having said something.

- `215475728999106` 2026-08-31 20:35 -- waiting **3 day(s)**
  - ahoj, prečo ked som si dala termíny tak mi zmyzla cena pri registrácií? dakujem
  - state: closed / routed_to_team
- `215475774548005` 2026-09-03 14:17
  - export platieb Dobry den, robim export platieb za mesiac jul a august a v tabulke nevidim stlpec profil, kedze sa nam do zoozy tahaju platby z troch uctov potrebujem platby vyfiltrovat podla uctu na k
  - state: open / no resolution
- `215475779589808` 2026-09-03 18:06
  - NEjde podla navodu pripojit Zoozu na ChatGPT - v Juli zmenili postup https://zooza.app/#mcp Toto nefunguje. Prosim dajte tam aktualny presny postup, lebo podla Chat GPT noavodu som sa stratil. Vraj to
  - state: open / no resolution
- `215475782192470` 2026-09-03 20:19
  - Pri kopirovani dietata do skupiny nenastavi system registracny poplatok Pri kopirovani dietata do skupiny nenastavi system registracny poplatok 80eur no musím ho nastavit ja sama
  - state: open / no resolution

## 1. Human answers -- the gold standard

Read these first. A human answer that generalises belongs in the KB.

### `215475278399746` -- 2026-09-01 05:11

**Asked:** ako zruším duplicitné registrácie?

**Human answered:** Dobry den, Evka, napiste nám, co by ste potrebovali dosiahnut? Radi pomozeme. Ide o kurz Senec Štúrová, Pokročili? https://zooza.app/#courses/9507/settings?edit=price Tam som si vsimol, ze ste zmenili nastavenie platby zo splatok na jednorazovu platbu. Pri splatkach bola stale uvedena cena za hodinu, s ktorou system nadalej pracoval. Zmenil som to na 0 eur a nechal jednorazovu cenu, teraz sa to zobrazuje takto. Dajte vediet, radi pomozeme.

### `215475484934773` -- 2026-09-01 14:53

**Asked:** Login proccess Hi Martin! We would like to avoid using the “Pentru a continua, introduceți e-mailul sau numărul de telefon.” step. It complicates things for our clients and the code isn’t always sent promptly. Please let me know how we can do this. Thanks so much!

**Human answered:** Hi Mara, I understand this is bigger change but it is easily skippable - there is a button to skip the login process if users don't want to log in. We've recently introduced plenty of features that rely on users being logged into the system - loyalty program with sibling discounts, priority booking for existing customers, auto enrollment etc, so this change is not so self imposed as it may seem. I would suggest waiting little bit to gather more feedback as this is fairly new and as with any change - it usually brings complaints. When dust settles we would make adjustments - either make the Continue as Guest option more visible or we'll figure out something else. One way to speed up the proce

### `215475587179939` -- 2026-09-01 09:25

**Asked:** Dobrý den, máme na kurzy handstandů vyvinutý vlastní systém, ale chybí nám správa omluvenek a náhrad. Koukal jsem, že tohle máte vyřešené, ale na to abychom mohli tyto dva systémy propojit, bych potřeboval mít přes API možnost klientům vytvořit za ně uživatelské účty (které potvrdí) a přihlásit je na všechny lekce kurzu, ze kterých se pak odhlašují a nahrazují na jiné, v API dokumentaci jsem toto 

**Human answered:** Dobry den Michal. Dobra sprava je, ze vsetky funkcionality Zoozy su kompletne spristupnene cez Api. V ramci verejnej dokumentacie poskytujeme podklady iba k bezne konzumovanym endpointom. V teorii je teda mozne urobit to, co potrebujete. Horsia sprava je, ze ste si vybrali use case, ktory si toho vyzaduje ovela viac ako len zakladanie klienta. Nahradne hodiny su zo svojej podstaty naviazane na skupiny a terminy. Museli by ste teda viest paralelny kalendar vo svojom systeme a zaroven v Zooze. Opat. Je to mozne vdaka Api, akurat si nie som isty, ci by to pre Vas bola taka pridana hodnota, pretoze toto vsetko preintegrovat, to by ste si rovno mohli naprogramovat nahradne hodiny do Vasho systemu

### `215475648622343` -- 2026-09-01 09:40

**Asked:** Faktury Dobrý deň, Prosím vás potreboval by som klientovi vygenerovať faktúru, no generuje ju ako fakturu číslo 4, pretože 3 faktúry predtým som niečo skúšal ale tie prvé 3 som ani nazaúčtoval v účtovníctve. Peosím vedeli by ste všetky faktúry vymazať(mne to nejde) aby som číslovalo faktúry od čísla 1? .. Ďakujem krásne. S pozdravom Michal Kiss

**Human answered:** Dobry den Michal, nie je potrebne faktury mazat a popravde ani na to nemame v appke proces. Staci ak vojdete do nastavenia fakturacneho profilu a tam si viete nastavit poradove cislo alebo ciselny rad faktury. Zaroven si tam viete prednastavit aj dalsie uzitocne veci ako napriklad preddefinovat text na fakture pouzitim dynamickych znaciek ako pri emailoch.

### `215475652310711` -- 2026-08-31 07:40

**Asked:** Dobrý deň, chceli by sme Vás poprosiť o preverenie a zohľadnenie situácie, ktorá nastala pri odosielaní SMS klientom z jarného fakturačného obdobia. Lulu sa pokúšala odoslať SMS, pričom jej systém dvakrát zobrazil chybové hlásenie, že správa nebola odoslaná. Keďže sme predpokladali, že SMS naozaj neodišla, skúsila som ju odoslať aj ja, no opäť sa zobrazila chyba. Celkovo sme teda SMS skúšali odosl

**Human answered:** Ahoj Lenka, nemusim to ani preverovat, rovnaka vec sa vam stane vzdy ked posielate stovky smsiek. planujeme to prerobit na rovnaky system ako emaily ale smsky bolli urcite dorucene vsetkym.

### `215475666655561` -- 2026-09-01 15:55

**Asked:** Neodhlásilo náhradnú hodinu Ahoj, ​ Zore Mannion sme odhlásili náhradu v tejto skupinke: https://zooza.app/#calendar/1393355 ​ Nevrátil sa jej ale kredit, prosím o preverenie. Jej registrácia https://zooza.app/#clients/396445 ​ Ďakujem za preverenie. Michal

**Human answered:** Ahoj Miso, a sumarizacia v logoch hovori co? Pri kazdom odhlaseni mate v appke log, kde je napisane preco nahradna hodina nebola priznana.

### `215475707208521` -- 2026-09-01 09:39

**Asked:** Ano pomohlo, dakujem na teraz. ​ Snad to bude bez problemov, ked zacne skolsky rok. ​ ​www.luciahoxha.com ​ Ambassador of Global Institute for Extraordinary Women Join our Facebook group Journey Towards Motherhoodhttps://www.facebook.com/groups/journeytowardsmotherhood Sign up to my Newsletterhttp://eepurl.com/dvO5hf Fcb: Lucia HoxhaTwitter: @luciahoxhaInstagram: luciahoxhaLinked-In:https://www. l

**Human answered:** Dobry den, Predaj a platby -> Platby -> Parovanie platieb. Vo filtri zadate volbu Nove. Pripadne priamo na dashboarde platieb v casti Predaj a platby.

### `215475708938188` -- 2026-08-30 13:42

**Asked:** For Oradea, Ideal subscriptions have fixed modules of either 16 or 14 sessions, with fixed start and end dates. Clients can choose to pay either monthly, at the end of each month, or per module, at the end of the module month. The amount they pay also depends on their starting date. I’m not sure what payment plans we should create to accommodate both payment options.

**Human answered:** Hi Mara, there are couple options - There is a payment template with frequency - by blocks. Which means that the payment will be created at the start of each block. Or you can use after N sessions - if you have 4 sessions each month then after 8 sessions it would effectively produce bi monthly payment. If this not enough and you do need this option then we can introduce this as a new frequency option.

### `215475709524760` -- 2026-08-30 17:43

**Asked:** Zobrazovanie lektorky Dobry den, na webe sa zobrazuje lektorka Hanka ale my sme ju zmenili aj na skupine aj na terminoch za Kiku ale stale na webe zobrazuje meno Hanka.preco?Vieme to nejak zmenit?Dakujem

**Human answered:** Dobry den, v ramci registracneho formulara sa zobrazuje ten lektor, ktory je urceny na skupine. nie na terminoch. Zaroven zo screenshotu je mozne, ze mate pri tom konkretnom lektorovi zapnute iba zobrazovanie jeho prezyvky co je samostatne pole v lektorskom profile. Skuste teda prosim skontrolvoat obe veci - ci je lektor nastaveny na skupine (a nielen na terminoch), pripadne ci ten lektor nema zapnute iba zobrazovanie prezyvky a zaroven sa prezyvka nenazyva "Hanka"

### `215475718874765` -- 2026-09-01 14:59

**Asked:** Dobry den, na kurz Minicirkus, ktory je pre rodica spolu s dietatom, sa nam prihlasili dve klientky na skusobnu lekciu tak, ze vytvorili samostatne registracie pre seba a aj pre dieta. mame v systeme nastavenu automaticku zlavu pre surodenca, co sposobilo, ze na skusobnu lekciu jej tam automaticky bol pripisany preplatok. Posielam screenshot. Vymazala som dvojitu registraciu, ale kedze chceme mat 

**Human answered:** Dobry den, Lenka, - Automaticka zlava nezmizne po vymazani registracie. Ziadna taka uprava sa sama nespusti - Do počtu detí sa zarátavajú len prihlášky so stavom Registrovaný. Prihlášky na čakacej listine a skúšobné prihlášky sa nezarátavajú.

### `215475720167520` -- 2026-08-31 16:35

**Asked:** Je možnosť nastaviť v zooze to, aby sa klient mohol odhlásiť z hodiny iba 1krát za mesiac?

**Human answered:** Dobry den, Patrícia, AI systém odpísal nespravne. Neda sa nastaviť každý mesiac. Dá sa však nastaviť, že každý 4 termíny si môže nahradiť len jeden z nich. Vyzeralo by to takto. Kurz > Nastavenia > Nahradne hodiny Povolene nahradne hodiny 1 Flexibilný limit termínov 4 Dajte vedieť, či pomohlo

### `215475721574632` -- 2026-08-31 17:09

**Asked:** Presuny v sieti Dobry den, po presunuti v sieti a naswlednom prijati na druhu pobocku potrebujeme aby registracia bola vymkazana nie zrusena. Dalej neviem najst presunute deti ktore cakaju na prijatie.

**Human answered:** Dobry den, registracie skutocne nechcete vymazavat. Hlavne ak na nich su prijate platby, sposobi Vam to problemy v reportingu ale nie len to. Vymazavat by ste mali iba registracie, ktore vznikli omylom, alebo su duplicitne, ale take zasa nie je dovod nikam presuvat. Sucasny proces presunu v ramci sieti sme navrhovali po vzajomnej dohode. Prijate ziadosti je vidno na dashboarde priamo na hlavnej obrazovke v ucte spolocnosti, do ktorej bolo dieta presunute.

### `215475721963435` -- 2026-09-01 08:37

**Asked:** i want to send the specific booking link for a programma to individual parents, how do i change the bit where it says my name samuel-davis, i want it to say elizabeth samueks

**Human answered:** Hi Samuel, I understand what you mean. The zooza.site addresses are temporary, system-generated pages ,,, the key in the URL is created automatically when the account is set up, which is why your name appears there. We can rewrite it directly in the database. Just let me know and I'll tell you how quickly we can do it. That said, allow me one recommendation: if you have the option to embed the booking/registration directly on your own website, it's considerably stronger from a branding perspective than using these temporary pages. Your customers stay on your domain and the whole process feels more consistent. Let me know which way you'd like to go,,, happy to help with either option. Thank y

### `215475722059369` -- 2026-09-01 08:36

**Asked:** Booking link slug not updating after changing programme URL I am trying to change the name shown in the public booking link. The link currently contains samuel-davis, and I want it to show elizabeth-samuels. Steps I already tried: Go to Programmes → Programme Settings → Basic Information Change the URL address field to elizabeth-samuels Save the changes After saving, the Classes → Share → Public r

**Human answered:** Hi Samuel, we've changed the slug for you ,,, it's now elizabeth-samuels. For example: https://zooza.site/elizabeth-samuels/registration?course_id=9615&schedule_id=101264 If you'd like to embed it on your own website later on, just let me know ,,, happy to help with the setup. Best regards, Michal

### `215475730855728` -- 2026-09-01 05:11

**Asked:** cena Pekný deň, moja otázka znie: som na skupine cena a platba je tam uvedené 1008 € ked to rozkliknem je tam 990€ ktoré by som chcela tam mať, prečo sa mi to zmenilo? a ked mám na kurze cenu 990€ prečo pri registrácií sa zobrazuje 1008€? ďakujem

**Human answered:** Dobry den, Evka, napiste nám, co by ste potrebovali dosiahnut? Radi pomozeme. Ide o kurz Senec Štúrová, Pokročili? https://zooza.app/#courses/9507/settings?edit=price Tam som si vsimol, ze ste zmenili nastavenie platby zo splatok na jednorazovu platbu. Pri splatkach bola stale uvedena cena za hodinu, s ktorou system nadalej pracoval. Zmenil som to na 0 eur a nechal jednorazovu cenu, teraz sa to zobrazuje takto. Dajte vediet, radi pomozeme.

### `215475731671489` -- 2026-09-02 14:53

**Asked:** Dobrý den, proč nejsou mazat skupiny ani registrace?

**Human answered:** Dobry den, pani Palcutova, skupiny aj registracie sa zmazat daju. Zmazu sa okamzite avsak zostavaju 30 dni v "Kosi", odkial je mozne ich znovu aktivovat. Napada mi, ze ste zmazali skupinu a stale sa Vam zobrazovala v zozname, je to tak? Chvilu moze trvat kym z prehliadaca zmizne. Niekedy staci len urobit refresh obrazovky (stlacit F5). Niektore udaje sa ukladaju v prehliadaci a okamzite sa nezmazu. Moze to trvat par minut.

### `215475732875043` -- 2026-09-01 05:05

**Asked:** Jak funguje čekací listina a jak ji zapnout?

**Human answered:** Dobry den, pan Fisenko, texty vo formulari si mozete upravovat. Da sa to vsak len na urovni Vasej stranky. Pouzivame na to upravu cez script. Tu je k tomu dokumentacia, je potrebne najst na to kluc a k tomu zmenu textu. https://docs.zooza.online/widgets/profile-widget/#translations Takto by vyzeral script pre zmenu toho pojmu "Obsadzeno". Tých kľúčov tam môžete mať pod sebou viacero. Tlačidlo je pre všetky stavy rovnaké. <script type="text/javascript"> window.ZOOZA = { print_debug: true, translations: { 'global.region' : 'Area', 'registration.capacity_full' : '🟠 Obsazeno – čekací listina', } } </script> Dajte vediet, ci pomohlo. Radi pomozeme aj s pripadnym nastavenim. Script sa umiestnuje b

### `215475734719777` -- 2026-09-01 11:44

**Asked:** vytvorila som skupinu MS teplicka 2026/2027 zber zaujmu a tato skupina je pristupna pre rodicov na online registraciu ale v registracnom formulari sa nezobrazuje cena za kurz. ako to viem nastavit aby tam bola uvedene cena? momentalne je tam cena ze 0 ale mam nastavene na skupine ze cena kurzu je 156 eur

**Human answered:** Dobry den Nikol, mate v principe dve moznosti - bud Vam staci pouzit extra polia (Nastavenia kurzu -> Extra polia; alebo ak vyzadujete nejaky dlhsi dotaznik, mame v systeme integraciu na Google forms (Tim a nastavenia -> Integracie -> Google)

### `215475734954942` -- 2026-09-01 08:49

**Asked:** Dobrý den, všiml jsem si, že se změnilo menu Prodej a platby. Chtěl bych se zeptat, jestli je někde možné vyfiltrovat "nespárované platby"? Využíváme to relativně často pro kontrolu. Děkuji za info. Tomáš

**Human answered:** Dobry den Tomasi, na to aby sa platba ukazala v zooze su potrebne tri podmienky: System musi naparovat email na ucet v zooze (na to sluzi ten email, ktory sa nastavuje v internet bankingu), Zaroven musi byt Zooza schopna precitat telo emailu a napokon nesmie byt duplicitna. Ak tymito troma krokmi prejde tak sa v systeme zobrazi a to bud ako sparovana alebo ako nesparovana. Ak je nastavene ignorovanie platieb tak aj tak sa v zooze da dohladat pod filtrom Ignorovana. V pripade ak nejaku platbu neviete najst, vzdy je najlepsie poslat priamo vypis z banky aby sme vedeli pohladat, kde ta platba skoncila. Napriklad aj ked sa platba v zooze neobjavi, vsetky emaily odkladame a je mozne ich spatne do

### `215475734967717` -- 2026-09-03 19:49

**Asked:** pripomienka terminy Dobrý deň, prosím o kolkej sa posiela pripomienka pred termínom? v kurze JESS- Nestes / Praznovska sa dneska este ziadna neodoslala. kurz https://zooza.app/#courses/schedules/87539 a maju hodinu zajtra o 9:00 - v júni im pripomienky chodili a teraz uz nie.. Ďakujem za kontrolu a pomoc, Barbora

**Human answered:** Dobry den Barbora, kazda pripomienka ma svoj samostatny cas kedy sa odosiela a mozete si ho skontrolovat pre kazdu verziu rannej pripomienky samostatne: https://zooza.app/#communication/templates?type=event_notification

### `215475735084045` -- 2026-09-01 13:11

**Asked:** Dobrý deň, chceli by sme požiadať o zrušenie služby ZOOZA a ukončenie nášho mesačného predplatného, keďže túto službu už nebudeme ďalej využívať. Prosíme o zrušenie predplatného k najbližšiemu možnému termínu a zastavenie ďalších platieb. Zároveň Vás prosíme o potvrdenie prijatia tejto žiadosti a informáciu, ku ktorému dátumu bude služba definitívne ukončená. Ďakujeme. -- S pozdravom, Ing. Matej Š

**Human answered:** Dobry den, pan Štec, v prvom rade dakujeme za spolupracu a pristup. Sme radi, ze ste dali Zooza sancu, keby cokolvek v budocnosti potrebujete, dajte vediet. Budeme radi, ked nam napisete primarny dovod, aby sme sa mohli zlepsovat. Dakujeme za informaciu. Potvrdzujeme prijate. Posuvame informaciu na kolegynu, ktora to spracuje. Štandardná je mesačná výpovedná lehota. Prajeme príjemny den a uspesny start do noveho skolskeho roka

### `215475735174575` -- 2026-09-01 11:46

**Asked:** Ahoj, prosím ťa, keď napíšem cez Zoozu správu (e-mail) rodičovi a on mi odpíše, kam príde jeho odpoveď? Kde ju mám hľadať?

**Human answered:** Dobry den Peter, to ci bol odoslany prihlasovaci kod priamo v Zooze nezistite. Tychto emailov chodia tisicky denne preto ich nearchivujeme. Ak viete priblizny datum, kedy mal byt kod odoslany a zaroven cislo registracie/email vieme to preverit. V poslednej dobe mame viacero hlaseni, ze nase emaily nie su vzdy dorucovane do emailovych inboxov patriacich skupine Azet (@azet.sk) tak teoreticky aj toto moze byt problem.

### `215475735218492` -- 2026-09-01 09:35

**Asked:** co znamena tato kolonka Zahrnúť celý počiatočný dátum

**Human answered:** Dobry den, predpokladam, ze sa pytate na zaskrtavacie policko pri aplikovani novej platobnej sablony. Ak ano tak odpoved je: Znamena to ze sa pocitaju aj pripadne terminy ktore sa v tom datume nachadzaju. Cize napriklad ak zvolite 1. 1. 2027 a na tento termin pripada termin, ktory je povedzme o 17:00 ale je jasne ze zakaznik nan uz nepride, potom chcete nechat policko odskrtnute aby mu ho system do ceny nezaratal. Naopak ak to policko zaskrtnete, potom aj vsetky terminy v ten dany datum sa budu pocitat do ceny

### `215475741191785` -- 2026-09-01 17:15

**Asked:** zle ukazuje cas skoncenie kurzu v registrascnom formulari https://zooza.app/#courses/schedules/102646 ​ tento kruzok konci 18.12.26 o 12:00 ako vidno v nastaveniach. Ale v registracnom formulari mi to ukazuje ze konci o 11:00, pozrete to a fixnete pls, ak to je chyba? ​ https://btscentre.youngengineers.sk/registracia/?course_id=9589&schedule_id=102646

**Human answered:** Dobry den, v registracnom formulari sa komunikuje hodnota, ktoru ste zadavali pri vytvarani skupiny. Skupina ma samostatne definovanu dlzku hodiny, ktora sa pouziva ako prednastavena pre vsetky terminy v danej skupine. Kedze ale skupina moze mat terminy roznej dlzky (pri vytvarani terminov viete zadat vzdy rozdielnu dlzku terminov), aplikacia vzdy komunikuje dlzku, ktora je na skupine. Ak sa teda pozriete do nastaveni danej skupiny uvidite, ze tam mate nastavenu dlzku 60 minu a nie 120 ako na terminoch. Staci si tu dlzku upravit na skupine a bude to korektne aj na stranke. Tato zmena sa da urobit aj hromadne, ak by ste potrebovali upravit viacero skupin.

### `215475741202329` -- 2026-09-01 17:18

**Asked:** 491219 - Eva Baďurová (Tereza Baďurová) pani sa nevie ani na svoj ani na na manzelov mail prihlasit do systemu ani na sty krat. neviem, co jej mam dalsieho poradit.

**Human answered:** Dobry den, prihlasenie jej funguje korektne, vid screenshot: ​ Problem je na strane zakaznicky. V poslednej dobe evidujeme ze nie vsetky nase emaily su dorucitelne na domenu @azet.sk takze predpokladam, ze problem bude tam. Uplne najlepsie by bolo ak by Vam vedela poskytnut iny alternativny email.

### `215475748694375` -- 2026-09-02 15:41

**Asked:** I am setting up our Meta Pixel. I have already set up the Pixel base code inside Squarespace, and now I am setting up the scheduled event when a lead schedules. I'm guessing that is done inside Zuzar as opposed to inside Squarespace. If it's in Zuzar, tell me exactly where to paste the Meta Pixel code inside here, or do we use a certain custom event that you can give us and add a custom event in t

**Human answered:** Please look at this documentation: https://docs.zooza.online/widgets/registration-widget/#analytics for integration Meta Pixel

### `215475749567234` -- 2026-09-02 09:54

**Asked:** Nesparovaná platba v systéme (platba na účet prišla) Dobrý deň, obraciam sa na vás s prosbou o preverenie párovania konkrétnej platby v systéme. Zvyčajne mi automatické párovanie platieb funguje bez problémov, no pri tejto jednej úhrade k spárovaniu nedošlo: Platba reálne prebehla: Na bankovom účte platbu evidujem, prišla mi aj štandardná banková notifikácia o pohybe na účte emailom a klientka pos

**Human answered:** Dobry den Janka, ide o Fio banku a oni pred nejakym casom zmenili aj email odosielatela a aj sablonu emailu, preto moze byt ze v medzere kedy sa toto udialo a my sme upravili nas proces sa niektore platby nesparovali. Malo by ist o obdobie od 17 augusta do 24 augusta. Podla screenshotu ale platba prisla 31. augusta co znamena, ze by mala byt v poriadku sparovana, ale uz aj pred tym sa stavalo, ze email z Fio banky vobec neprisiel. Aj sme to testovali s niektorymi zakaznikmi a skutocne, platba prisla na ucet a oni na svoj email notifikaciu o nej nedostali. Kazdopadne pokial transakcia neprisla pocas vcerajsieho dna, tak uz nepride. Za nas vieme preverit, ci nahodou opat nezmenili nieco na svo

### `215475750245573` -- 2026-09-02 07:31

**Asked:** BBBA - platby - transakcie -otazky ahojte, vidím, že ste zmenili túto sekciu, okej ​ 1. pred updatom bola moznost filtrovat si platby aj v kategorii "nesparovane" aby som vedela venovat pozornost prave tym.. ​ kde je tato moznost teraz prosim? to je nesmierne dolezite hladsiko ​ 2. ked kliknem na detail platby, nic sa nezobrazi,preco? https://zooza.app/#payments/search/1522602 https://zooza.app/#p

**Human answered:** Cauko, je tam samozrejme aj teraz. je to hned prvy filter. Cize platby -> Parovanie platieb a vyberies hned prvy filter - nesparovane platby. To druhe je chyba, opravime to. Dakujem:)

### `215475750270144` -- 2026-09-02 13:55

**Asked:** Ahoj, prosím ťa máme nastavené pravidlo na kurz ,,Mačkovité šelmy" vekové obmedzenie 4-6 rokov. Pokiaľ športovec nedovŕšil 4 roky a chce si vyskúšať tréning, vie sa prihlásiť spôsobom, že registráciu budeme musieť manuálne potvrdiť ?

**Human answered:** Dobry den Peter, vo vseobecnosti mozete. V ramci nastavenia vekoveho limitu (Nastavenia kurzu -> Extra polia) je mozne zakliknut aj moznost povolit registraciu ludom, ktori vekovy limit nesplnaju a pripadne im pridelit aj znacku. Takito ludia skoncia v poradovniku a je potrebne ich manualne zaradit

### `215475750933738` -- 2026-09-02 09:31

**Asked:** what have I got 16 bookings when sat the class at 15 and none showing on waiting list

**Human answered:** Hi Samantha, can you please tell me which class this is?

### `215475751285418` -- 2026-09-03 09:30

**Asked:** Notifikace o neuhrazené platbě, ačkoliv je uhrazena Dobrý den, kontaktoval nás klient, že mu přišla notifikace ze systému o neuhrazené platbě, ačkoliv je platba uhrazena. Pro názornost přikládám screenshot. Prosím, mohli byste toto prověřit a případně přenastavit? Moc děkujeme, zdravím, Aneta Honsová

**Human answered:** Dobry den Aneto, Dakujeme za podnet. Najskor co sa stalo: - Kazdy den o pol noci system vyhodnocuje neuhradene registracie - Nasledne tieto registracie zaradi do fronty a ta sa spracuje o 9 rano - V tomto pripade sa stalo, ze o polnoci bola registracia este neuhradena a platba sa doparovala 8:20 - Pri rozosielke o 9 rano sa uz nekontroluje ze ci sa medzicasom registracia uhradila alebo nie a preto zakaznik spravu dostal Upravime tu rozosielku o 9 rano aby rovnako kontrolovala stav uhrad aby sa takyto pripad neopakoval. Dakujem a prajem este pekny den.

### `215475751332166` -- 2026-09-02 10:08

**Asked:** Problem s parovanim platieb Dobrý deň, Evidujete hlásenia o nespárovanýc paltbách od iných klientov? Mne veľa patieb nespárovalo za posledný týždeň, vete sa na to pozrieť ? Aj veľa ľudom včera mrzol systém prihlasovania a registácii, je možné že bol preťažený server v prvý školský deň? Ďakujem za odpoveď

**Human answered:** Dobry den Michal. Ano Fio banka v priebehu augusta menila email z ktoreho sa posielali notifikacie o uhradach a zaroven menili aj sablonu tohto emailu cize zhruba tyzden/tyzden a pol bol vypadok v parovani platieb z tejto banky, kym sa nam podarilo dohladat dovod. Malo by to ale byt opravene takze ak Vam platby nepresli tento/minuly tyzden, poslite prosim nejaky priklad platby (idealne screenshot rovno z banky) a preverime, ci tam zasa nieco nepomenili.

### `215475751395024` -- 2026-09-02 10:25

**Asked:** Rodič nevidí registráciu Dobrý deň, mal by som dotaz k tejto registrácii https://zooza.app/#registrations/491518 robil som tam zlúčenie, keďže má prihlásené 2 deti a ja to vidím v poriadku ale mamička mi písala, že nevidí vôbec nič vo svojej registrácii, posielam screen shoty

**Human answered:** Dobry den Michal, viete prosim povedat z akej emailovej adresy sa pani prihlasuje do profilu?

### `215475753194796` -- 2026-09-02 14:37

**Asked:** Dobrý den, chtěl bych se zeptat, zdali by bylo možné přidat možnost hromadné úpravy termínů i pro Dodatečné lektory? Po zkušenosti z minulého roku, kdy se stávalo, že místo zkušeného trenéra brali trénink 2 méně zkušení, tak jsem letos přidal do všech našich kurzů 1) Hlavního lektora 2) Všechny ostatní lektory mezi dodatečné lektory. To mi umožňuje měnit (přidávat) pohodlně lektora na konkrétním t

**Human answered:** Dobry den Tomasi, premyslam, ako by sme toto urobili tak aby to bolo prehladne a davalo to zmysel v ramci existujuceho modelu hromadnych zmien a napadlo mi, ze by sme to pravdepodobne vedeli ovela jednoduchsie vymysliet v ramci AI konektora. Preto sa chcem opytat ci ho pouzivate a ci by toto nebola pre Vas lepsia cesta? Momentalne AI konektor tuto zmenu urobit nevie, ale vedeli by sme to tam doplnit.

### `215475754599604` -- 2026-09-02 15:04

**Asked:** Nezobrazuje moznost skusobnej hodiny Dobrý deň, Prosím vás skupina líšky piatok 18:00 -je voľná a mám zakliknuté online registrácia aj registrácia na skušobné hodiny a neukazuje mi možnosť sa prihlásiť na skušobnú hodinu. Neviem prísť na dôvod, prečo tomu tak je. Ďakujem za odpoveď S pozdravom Michal Kiss

**Human answered:** Dobry den Michal, robili sme tam dnes update. System povoloval registrovat sa na skusobne hodiny aj ked uz bola kapacita plna, tak predpokladam, ze sme to zrovna pri vasej konfiguracii neodchytili uplne spravne. Viete prosim poslat linku na skupinu? preverime to ci to suvisi.

### `215475757699557` -- 2026-09-03 08:47

**Asked:** trial Dobrý deň. Prosím, vysvetlite nám, ako funguje platba za skúšobný tréning. Nastavili sme registráciu na skúšobný tréning, ale nie je nám jasné, kde a akým spôsobom má klient zaplatiť za vstup.

**Human answered:** Dobry den. V pripade ak pouzivate skusobne hodiny v platenom rezime, funguje to rovnako ako pri beznej registracii. Teda po vyplneni registracneho formulara sa zakaznikovi objavi: a) tlacitko na uhradu a presmerujeme ho na platobnu branu v pripade ak je platobna brana aktivna b) qr kod a instrukcie na uhradu pokial ide o platbu prevodom. V pripade ak uhradu nedokonci z akehokolvek dovodu, moze skusobnu hodinu zaplatit vo svojom profile. Proces je v tomto uplne rovnaky ako pri beznej registracii. Teda registracia je v rezime Caka sa na uhradu (doba po ktoru je v tomto stave sa nastavuje v Tim a nastavenia -> Platby a fakturacia -> Platby) a po tejto dobe sa prepne do neuhradenych.

### `215475769688053` -- 2026-09-03 18:57

**Asked:** Pokiaľ chce rodič zrušiť registráciu, aby dieťa viac nenavštevovalo krúžok, ako to vie spraviť?

**Human answered:** Dobry den, pani Izakovicova, zrusit registraciu je mozne v detaile registracie. Tlačidlo registrácie najdete hned v prvej casti s nazvom registracia.

### `215475770601796` -- 2026-09-03 09:08

**Asked:** how do I delete a user from the setting?

**Human answered:** Dobry den Natalia, Snazite sa vymazat lektora?

### `215475780933743` -- 2026-09-03 19:23

**Asked:** Turtle Tots Dubai: Login email codes not delivered Anna from Turtle Tots Dubai reported that several customers are not receiving email login codes for the parent portal today. e.g. Sylvie80@web.de https://asia.zooza.app/#registrations/1822 Please investigate urgently.

**Human answered:** Hi Anna, we've investigated the issue and it was upstream from us on the infastructure. The issue is now resolved.


## 2. Bot-only, highest risk first

`A_hard_signal` = routed to team, abandoned, or rated poorly. `B_no_kb_source` = the bot cited nothing from the KB. `C_reask` = the client asked again two or more times.

- **A_hard_signal** `215475728999106` 2026-08-31 20:35 -- re-asked 6x
  - Q: ahoj, prečo ked som si dala termíny tak mi zmyzla cena pri registrácií? dakujem
  - cited: Price and payment setup | Zooza Help, FAQ — Programmes | Zooza Help, Getting Help and Support | Zooza Help
- **B_no_kb_source** `215475707230867` 2026-08-30 10:25
  - Q: Ano, myslela som nový skolský rok. ​ OK, tak skusim pred zaciatkom skolskeho roka. ​ Dakujem ​ ​www.luciahoxha.com ​ Ambassador of Global Institute for Extraordinary Women Join our Facebook group Journey Towards Motherhoodhttps://www.facebook.com/gro
  - cited: (no KB source)
- **B_no_kb_source** `215475721709568` 2026-08-31 13:47
  - Q: Prijatie presunutych deti https://zooza.app/#registrations/transfer/change?course_id=8909&schedule_id=87182&action=transfer_accept&transfer_id=60 Ked chcem prijat diata presunute v sieti, tak mi vyskakuju tieto odkazy: pozri prilohu. V detailoch pres
  - cited: (no KB source)
- **B_no_kb_source** `215475751366512` 2026-09-02 09:11
  - Q: Ako mam pridat k tomuto klientovi dalsiu e-mailovu adresu? https://zooza.app/#registrations/501980 zuzanamegyeri@gmail.com ​ www.luciahoxha.com Ambassador of Global Institute for Extraordinary Women Join our Facebook group Journey Towards Motherhood 
  - cited: (no KB source)
- **B_no_kb_source** `215475753653969` 2026-09-02 13:03
  - Q: payments Dobrý deň. Ako môžeme uskutočniť prvé vyúčtovanie a nechať si vyplatiť platby za august na náš bankový účet? s pozdravom, Sergey Polyakov
  - cited: (no KB source)
- **B_no_kb_source** `215475760117282` 2026-09-02 17:52
  - Q: Enter your strongest work in The EdTech Awards 2027 and turn your impact into lasting credibility, visibility, and momentum. ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏ ‌ ͏
  - cited: (no KB source)
- **B_no_kb_source** `215475774548005` 2026-09-03 14:17
  - Q: export platieb Dobry den, robim export platieb za mesiac jul a august a v tabulke nevidim stlpec profil, kedze sa nam do zoozy tahaju platby z troch uctov potrebujem platby vyfiltrovat podla uctu na ktory patria. Doteraz tato moznost v stuahnutom exp
  - cited: (no KB source)
- **B_no_kb_source** `215475779589808` 2026-09-03 18:06
  - Q: NEjde podla navodu pripojit Zoozu na ChatGPT - v Juli zmenili postup https://zooza.app/#mcp Toto nefunguje. Prosim dajte tam aktualny presny postup, lebo podla Chat GPT noavodu som sa stratil. Vraj to asi ani mozno nejde pripojit, ak nemam nejaky ent
  - cited: (no KB source)
- **B_no_kb_source** `215475782192470` 2026-09-03 20:19
  - Q: Pri kopirovani dietata do skupiny nenastavi system registracny poplatok Pri kopirovani dietata do skupiny nenastavi system registracny poplatok 80eur no musím ho nastavit ja sama
  - cited: (no KB source)
- **C_reask** `215475713691305` 2026-09-02 19:24 -- re-asked 21x
  - Q: ako mam vytvoeit skupinu
  - cited: Jak automatizovat vaše podnikání v oblasti dětských aktivit (aniž byste ztratili osobní kontakt) — Zooza, Checklist pred spustením nových kurzov: Na čo nezabudnúť, aby sa sezóna nezačala chaosom — Zooza, Zooza PRO - Zooza
- **C_reask** `215475717855970` 2026-08-31 13:53 -- re-asked 20x
  - Q: Ahoj, rodič nechtiac zaregistroval svoje dieťa duplicitne do jednej skupiny. Dlh mu tým pádom ukazuje dvojnásobný, jednu registráciu som vymazal, no dlh ostal rovnaký. Navedieš ma ako mu upraviť správny dlh akoby za jedného športovca?
  - cited: Transfer and copy bookings | Zooza Help, Discounts and Sibling Pricing FAQ | Zooza Help, Client Management FAQ | Zooza Help
- **C_reask** `215475720567429` 2026-08-31 12:33 -- re-asked 9x
  - Q: I do not receive one-time code required for login
  - cited: Login and Account FAQ | Zooza Help, Client Profile 101 | Zooza Help, Client Profile FAQ | Zooza Help
- **C_reask** `215475720220494` 2026-08-31 12:26 -- re-asked 8x
  - Q: Dobrý deň, dnešným dňom začíname nové fakturačné obdobie, klientom od dnes začínajú tréningy v aktuálnych kurzoch. Vyskytli sa už aj situácie, kedy si rodičia na tento týždeň hodinu odhlásili, zatiaľ mi volajú a píšu, že si nevedie vybrať náhradný te
  - cited: Make-up Sessions FAQ | Zooza Help, Managing client attendance — admin | Zooza Help, Custom replacement sessions | Zooza Help
- **C_reask** `215475770990391` 2026-09-03 11:57 -- re-asked 8x
  - Q: Ahoj, chcem sa opýtať na radu ohľadom riešenia jednej situácie. Chalan sa prihlásil ku nám do skupiny, včera si zlomil ruku, do decembra nemôže trénovať. Najlepšie riešenie je vytvoriť mu nový platobný plán v registrácií?
  - cited: Getting Started with Zooza | Zooza Help, Transfer and copy bookings | Zooza Help, Common Booking Scenarios | Zooza Help
- **C_reask** `215475708981558` 2026-08-30 13:23 -- re-asked 6x
  - Q: hi, is it possible to see an overvie of terminy which are locked and attendance or not were not filled in yet ? I dont want to check teachers reports by hand but would like to see overview
  - cited: Attendance and Catch-up Classes FAQ | Zooza Help, Dashboard | Zooza Help, Class Detail | Zooza Help
- **C_reask** `215475778536860` 2026-09-03 17:17 -- re-asked 6x
  - Q: Vytvorila som omylom profi ucet. Ale chcem len dieta zahlasit na kurz
  - cited: Zooza PRO - Zooza, Ceník — Zooza, Registrační stránka pro dětské kroužky: 5sekundový návod — Zooza
- **C_reask** `215475774458554` 2026-09-03 14:19 -- re-asked 5x
  - Q: Dobry den, chcela by som sa spytat na report prijatych platieb. Doteraz sa v tabulke nachadzal aj stlpcek kde bol spomenuty profil, kedze sa nam do zoozy natahuju platby z troch uctov tak som vyuzovala filtrovanie na zaklade tychto troch profilov
  - cited: Jak automatizovat vaše podnikání v oblasti dětských aktivit (aniž byste ztratili osobní kontakt) — Zooza, Zooza PRO - Zooza, Ceník — Zooza
- **C_reask** `215475753046919` 2026-09-02 13:12 -- re-asked 4x
  - Q: ako uplatním zľavový kód pri vytvorení kreditu na konkrétnu registráciu. Závisí od toho či som prihlásený do svojho profilu cez stránku alebo Zoozu?
  - cited: Discounts and Sibling Pricing FAQ | Zooza Help, Discount code | Zooza Help, Instructors working hours | Zooza Help
- **C_reask** `215475768998327` 2026-09-03 04:56 -- re-asked 4x
  - Q: How can I set a programme payment setting to charge full term (including first session) even if it is past?
  - cited: Discounts and Sibling Pricing FAQ | Zooza Help, Programmes, Timetables and Sessions FAQ | Zooza Help, Payments and Billing FAQ | Zooza Help
- **C_reask** `215475707398670` 2026-08-30 08:30 -- re-asked 3x
  - Q: Ako odoberem zo zoozy neaktivneho lektora?
  - cited: Jak zautomatyzować firmę zajmującą się zajęciami dla dzieci (bez utraty osobistego podejścia) — Zooza, Zooza PRO - Zooza, Cennik — Zooza
- **C_reask** `215475733553841` 2026-09-01 06:05 -- re-asked 3x
  - Q: How to include childs date of birth, age and class on registration form?
  - cited: Additional fields on the booking form | Zooza Help, Reports | Zooza Help, Booking form settings overview | Zooza Help
- **C_reask** `215475736828706` 2026-09-01 11:49 -- re-asked 3x
  - Q: Ahojň
  - cited: Customizing widgets | Zooza Help, Booking Widget FAQ | Zooza Help, Programmes, Timetables and Sessions FAQ | Zooza Help
- **C_reask** `215475616647987` 2026-08-31 13:33 -- re-asked 2x
  - Q: how do i turn off dark mode
  - cited: Getting Started with Zooza | Zooza Help, Login and Account FAQ | Zooza Help, Onboarding and Launch FAQ | Zooza Help
- **C_reask** `215475707610459` 2026-08-30 09:18 -- re-asked 2x
  - Q: kde si prosim v zooza pozriem heslo, keď som vedená v role majiteľ- môj emailový účet je vedený ako majiteľ aj ako registrovaný rodič
  - cited: Zooza PRO - Zooza, Ceník — Zooza, Registrační stránka pro dětské kroužky: 5sekundový návod — Zooza
- **C_reask** `215475719267008` 2026-08-31 13:31 -- re-asked 2x
  - Q: how do i add another person to my account
  - cited: Getting Started with Zooza | Zooza Help, Registration and Booking FAQ | Zooza Help, Login and Account FAQ | Zooza Help
- **C_reask** `215475721894694` 2026-08-31 14:08 -- re-asked 2x
  - Q: if you have a registration fee, is this charged per child or per family?
  - cited: Registration and Booking FAQ | Zooza Help, Discounts and Sibling Pricing FAQ | Zooza Help, Programmes, Timetables and Sessions FAQ | Zooza Help
- **C_reask** `215475722822504` 2026-08-31 15:15 -- re-asked 2x
  - Q: Kde sa dá zmeniť ceny kurzu?
  - cited: Ceník — Zooza, Registrační stránka pro dětské kroužky: 5sekundový návod — Zooza
- **C_reask** `215475734950462` 2026-09-01 08:24 -- re-asked 2x
  - Q: dobry den prajem, zaevidovala som problem. Vytvaram skupiny ktore nam zacinaju buduci tyzden, v kalendari na stranke Helen Doorn vsak ich termin svieti uz tento tyzden. Prosim o pomoc
  - cited: Customizing widgets | Zooza Help, Calendar widget | Zooza Developer Docs
- **C_reask** `215475737999518` 2026-09-01 12:55 -- re-asked 2x
  - Q: prosím, ak sa mi prihlási dieťa ktoré ešte nedovršilo vek potrebny na navstevovanie krúzku, príde mi ziadost o schvalenie, alebo rovno ho zooza zamietne ako zle udaje?
  - cited: Jak automatizovat vaše podnikání v oblasti dětských aktivit (aniž byste ztratili osobní kontakt) — Zooza, Checklist pred spustením nových kurzov: Na čo nezabudnúť, aby sa sezóna nezačala chaosom — Zooza, Zooza PRO - Zooza
- **C_reask** `215475772784806` 2026-09-03 12:34 -- re-asked 2x
  - Q: Chcem vytvorit novu registraciu, ale po zadani emailu mi zooza povie, ze klient s takoutou mailovou adresou uz existuje. V registraciach vsak tuto emailovu adresu nevieme najst.
  - cited: Checklist pred spustením nových kurzov: Na čo nezabudnúť, aby sa sezóna nezačala chaosom — Zooza, Zooza PRO - Zooza, Registrační stránka pro dětské kroužky: 5sekundový návod — Zooza

## 3. Shipped but never communicated

| Repo | Spec | Title | Updated |
|---|---|---|---|
| api-v1 | API-20260831-001 | Payments module restructure — de-union the ledger list, per-family lists + exports, surface Refunds, new Inbound export | 2026-08-31 |
| api-v1 | API-20260901-001 | Show parent's make-up pickup timing in the admin cancellation email | 2026-09-01 |
| api-v1 | API-20260901-003 | Exclude trial-status registrations from loyalty eligibility | 2026-09-01 |
| api-v1 | API-20260901-002 | Profile widget: hide order total + paid-so-far (hide_total_debt) | 2026-09-01 |
| api-v1 | API-20260902-002 | Profile dashboard tells a customer their classes have ended | 2026-09-02 |
| api-v1 | API-20260902-001 | Reserve-seat trials must count against the class's seat capacity when offering trial dates | 2026-09-02 |
| api-v1 | API-20260902-003 | A reserve-seat trial holds its seat in its BLOCK, not across a segmented class | 2026-09-02 |
| app | APP-20260829-001 | App theming — user-selectable mode (light/dark/system) and colour tint | 2026-08-30 |
| app | APP-20260831-001 | Payments module restructure — Transactions families, Inbound pairing list, Refunds consolidation, config re-home | 2026-08-31 |
| widgets-v1 | W1-20260901-001 | Payments tab — positive 'To pay' figure and hide null order-total line | 2026-09-01 |

Stamp `docs_communicated` in the spec once the KB covers it.

## 4. Client email -- needs the review session

The Gmail connector needs an interactive login, so this step does not run here. In the session, search these senders over the window:

- `sarahmarsh@magikats.co.uk`
- `centralberks@weekicks.co.uk`
- `anna.blackwell@turtletots.com`
- `techsupport@zooza.online`

```
{from:sarahmarsh@magikats.co.uk from:centralberks@weekicks.co.uk from:anna.blackwell@turtletots.com from:techsupport@zooza.online} after:2026/08/30 before:2026/09/04
```
