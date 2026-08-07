#!/usr/bin/env python3
"""Build the complete 281-conversation index payload for the artifact."""
import json, re, os

OUT = "/private/tmp/claude-501/-Users-michaldodok-help/b787eb73-e2ac-4fc3-8dcc-cf32a857708a/scratchpad"
rows = json.load(open(os.path.join(OUT, "triage.json")))

NOISE = re.compile(r"(Jira issue creation|your ticket\s+has been received|váš tiket|Zooza Assistant will try|This message was deleted|^https?://\S+$)", re.I)
SPAM = re.compile(r"promotional|spam|irrelevant to (customer )?support", re.I)

# conversations that drove a documented KB change, and what changed
KB = {
 "215475256660170":"Párovanie platieb — dedikovaná adresa, Transaction type",
 "215475244228883":"Párovanie platieb — dedikovaná adresa",
 "215474929092668":"Transaction type v exporte",
 "215475244142067":"Párovanie platieb — priame FAQ",
 "215475272108493":"Párovanie platieb — priame FAQ",
 "215475124282890":"Prázdniny — záložka Advanced",
 "215475092076640":"Prázdniny — záložka Advanced",
 "215475259017286":"Prázdniny — záložka Advanced",
 "215475362695841":"Prázdniny — región na lokalite",
 "215475298753066":"NOVÝ článok Kapacita vs extra kapacita",
 "215475214097506":"Kapacita — kde je číslo extra kapacity",
 "215475112694550":"Náhradky — flexibilný limit (pomer)",
 "215474858324500":"Presun klienta — dátum splátky",
 "215475010052087":"Hromadný e-mail z filtrovaných skupín",
 "215475001854253":"Produktové linky, Share button",
 "215475349284982":"Share button; dokumenty",
 "215475109642682":"Zooza Sites — vlastné farby neexistujú",
 "215474840840167":"Náhľad klientskeho pohľadu — Share → Copy link",
 "215475348814074":"Jazyk widgetu = jazyk webu",
 "215475375068996":"Kalendár widget — Classic view",
 "215475380624387":"Kalendár widget — Classic view",
 "215475367246018":"Dlžná suma 0 — počítadlo platených termínov",
 "215475004782223":"Dlžná suma 0 — kontrolný postup",
 "215475369447464":"Platba povinná nejde — grace period + auto-cancel",
 "215475347694069":"„Ended\" nie je „inactive\"",
 "215475363144209":"COURSE_SUMMARY namiesto COURSE_DATE_DAY",
 "215474985694009":"COURSE_ vs EVENT_ v potvrdení odhlásenia",
 "215475004206547":"COURSE_ vs EVENT_ v potvrdení odhlásenia",
 "215475286181511":"EVENT_ značky len pri automatickom odoslaní",
 "215475170361964":"Značka na blok nikdy nebude",
 "215475285561723":"1 dokument = 1 registrácia",
 "215475260475622":"GoCardless inkasuje skôr",
 "215475058978548":"GoCardless — prvý mandát nie je opakovaný",
 "215474845646196":"Dovolenka lektora; jazyk",
 "215475247901010":"Jazyk — prepínač na Dashboarde",
 "215475158428716":"Súrodenecká zľava — falošné pozitíva",
 "215474990590888":"MCP konektor — refresh nástrojov",
 "215474991743446":"MCP konektor — refresh nástrojov",
 "215475086720339":"MCP konektor — refresh nástrojov",
 "215475183244514":"Meno dieťaťa na faktúre",
 "215475222027448":"Stripe — obchodné modely",
 "215475221851086":"Stripe — obchodné modely",
 "215474974884250":"Stripe/CardPay poplatky; súhlasy",
 "215475183335193":"Obmedziť počet registrácií ≠ kapacita",
 "215475192480209":"Rodinné väzby",
 "215475256660852":"Zmena e-mailu = Zmeniť klienta",
 "215475287990029":"Dokumenty; klient ktorý je aj lektor",
 "215475290414578":"Firemné polia; DPH",
 "215475327169019":"Metadáta kurzu",
 "215475213472396":"Sledovanie konverzií #done",
 "215475255463719":"Pauza na mesiac",
 "215475171219261":"Oprava duplicitnej úhrady",
 "215474913907137":"Náhradky len v priebehových kurzoch",
 "215474884472148":"Pravidlo 4 dní",
 "215474936072510":"Pravidlo 4 dní",
 "215474885814597":"Kopírovanie registrácie — typ kurzu",
 "215474914397237":"Odhlásenie z reklamných správ",
 "215475033677159":"Jednorazovo aj na splátky",
 "215474987107415":"Jednorazovo aj na splátky",
 "215475270539659":"Termín len na triály nejde",
 "215475168971012":"MATKO diagnostika",
 "215474855197157":"Print Version kalendára",
 "215475186259558":"Opätovný súhlas — checkbox",
 "215475075194244":"Pripomienky pri zálohách",
 "215475080773045":"Triály, pay-by-blocks",
 "215475093307603":"Automatické pokračovanie",
 "215474854926690":"Automatické pokračovanie — obojstranné",
 "215474855014188":"Automatické pokračovanie — obojstranné",
 "215474855005288":"Odpovede na pokračovanie",
 "215475332472796":"Filter Meno hľadá klienta",
 "215475332769218":"Filter Meno hľadá klienta",
 "215474916995379":"Lead collection — bez ceny a platby",
 "215475270920754":"Lead collection — faktúra pri zápise",
 "215474958996339":"Lead collection — cena skrytá",
 "215475347619901":"Refund zašedený; dvojitá cena produktu",
 "215475348514389":"Veľké exporty → Tools → Exports",
 "215475075505918":"Veľké exporty",
 "215475244814791":"Cookie lišta (stiahnuté — web klienta)",
 "215475172672105":"Zmazať vs zrušiť = soft delete",
 "215474905850124":"Zmazať vs zrušiť",
 "215475292239925":"Kurzy sa kopírujú po jednom",
 "215475271350809":"Vypnutie e-mailov klientom",
 "215475291948047":"Notifikácie; podpis; odstránenie lektora",
 "215475232739392":"HTML odkaz v súhlase",
 "215475291209859":"Súhlas — názov na formulári",
 "215475207979948":"Pro-rata; šablóna viditeľná klientom",
 "215475200623649":"Cena 0 na skupine = nenastavená",
 "215474975371638":"Poradie skupín; prázdniny per programme",
 "215475002630021":"Mena účtu",
 "215475369235436":"Mena účtu",
 "215474913416433":"Fakturačný engine; príjmové doklady",
 "215475030226934":"Úprava sedení; refundácie",
 "215474825309754":"Kde sa zobrazujú refundácie",
 "215474831290084":"Refundácie s menami klientov",
 "215474922422992":"Dochádzka naprieč registráciami",
 "215474931511995":"QR kód — konštantný symbol",
 "215474886051268":"PDF do hromadného mailu; pravidlo 4 dní",
 "215474868548420":"Nastavenie náhradiek",
 "215474912699689":"Terminológia Kurzy/Programmes",
 "215475083962483":"Terminológia; neskoré registrácie",
 "215475163179973":"Farba programu — Save po Edit",
 "215475169206503":"Farba programu — prvý výber ignorovaný",
 "215475170981576":"Presun ≠ presun do siete",
 "215475061607636":"Bloky — zmena cez dochádzku",
 "215475366122500":"Bloky — skrytá dochádzka",
 "215475256685893":"Fronta hromadných e-mailov",
 "215475189098529":"Hromadné SMS — dvojité odoslanie",
 "215475093214494":"Neplatený termín v bloku",
 "215475378358407":"Variant systémovej šablóny",
 "215475347984154":"Šablóny per kurz — Online Registrácia",
}

def clean(s):
    return " ".join(s.split())

def gist(txt, n=190):
    t = clean(txt)
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0] + "…"

data = []
for r in rows:
    turns = r["turns"]
    cust = [t[2] for t in turns if t[0] == "customer" and len(t[2].strip()) > 25 and not NOISE.search(t[2])]
    hum  = [t[2] for t in turns if t[0] == "human"    and len(t[2].strip()) > 40 and not NOISE.search(t[2])]
    bot  = [t[2] for t in turns if t[0] == "bot"      and len(t[2].strip()) > 60 and not NOISE.search(t[2])]

    q = gist(cust[0]) if cust else ""
    if hum:
        a, who = gist(max(hum, key=len), 240), "human"
    elif bot and any(SPAM.search(b) for b in bot):
        a, who = "Vyhodnotené ako spam / obchodná ponuka.", "spam"
    elif bot:
        a, who = gist(bot[0], 240), "bot"
    else:
        a, who = "Len potvrdenie ticketu — riešené e-mailom mimo chatu.", "none"

    if not q and not hum and not bot:
        q = q or "(bez otázky v chate)"

    cid = str(r["id"])
    data.append({
        "id": cid,
        "d": r["date"][:10],
        "q": q,
        "a": a,
        "w": who,
        "r": r["cust_after_bot"],
        "s": r["resolution_state"] or "—",
        "k": KB.get(cid, ""),
    })

data.sort(key=lambda x: x["d"])
open(os.path.join(OUT, "index_data.json"), "w").write(json.dumps(data, ensure_ascii=False, separators=(",", ":")))
print("konverzácií:", len(data))
print("s ľudskou odpoveďou:", sum(1 for d in data if d["w"] == "human"))
print("s väzbou na KB zmenu:", sum(1 for d in data if d["k"]))
print("veľkosť JSON:", os.path.getsize(os.path.join(OUT, "index_data.json")) // 1024, "KB")
