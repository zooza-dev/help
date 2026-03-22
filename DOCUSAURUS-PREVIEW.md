# Lokálny náhľad Help dokumentácie (Docusaurus)

Tento návod je pre ľudí bez programátorských znalostí.
Cieľ: spustiť si dokumentáciu lokálne v prehliadači, aby si videl, ako bude vyzerať.

---

## Čo budeš potrebovať

1. **Node.js** (runtime prostredie) — ak ho nemáš, stiahni si ho:
   - Choď na https://nodejs.org
   - Stiahni si verziu označenú **LTS** (odporúčaná)
   - Nainštaluj ho ako každý iný program (Next → Next → Install)
   - Po inštalácii reštartuj terminál

2. **Python 3** — zvyčajne už nainštalovaný na Macu. Overíš takto:
   - Otvor **Terminal** (Cmd + Space → napíš "Terminal")
   - Napíš `python3 --version` a stlač Enter
   - Ak vidíš číslo verzie (napr. `Python 3.11.x`), máš ho
   - Ak nie, stiahni ho z https://www.python.org/downloads/
https://nodejs.org---

## Krok 1 — Vygeneruj Docusaurus export

Toto musíš urobiť vždy, keď chceš vidieť aktuálny stav dokumentácie.

1. Otvor **Terminal**
2. Prejdi do priečinka s repozitárom:
   ```
   cd /Users/michaldodok/help
   ```
3. Spusti exportný skript:
   ```
   python3 scripts/export/build_docusaurus.py
   ```
4. Počkaj, kým dobehne. Na konci uvidíš niečo ako:
   ```
   Exported 168 docs → .../build/exports/docusaurus
   ```

---

## Krok 2 — Nainštaluj závislosti (iba prvýkrát)

Toto robíš **iba raz** (alebo po čerstvom vygenerovaní exportu).

1. Prejdi do vygenerovaného priečinka:
   ```
   cd /Users/michaldodok/help/build/exports/docusaurus
   ```
2. Nainštaluj závislosti:
   ```
   npm install
   ```
3. Počkaj — stiahne sa pár vecí, môže to trvať 1–2 minúty.

---

## Krok 3 — Spusti lokálny server

```
npm start
```

Terminál vypíše niečo ako:
```
[INFO] Starting the development server...
[SUCCESS] Docusaurus website is running at: http://localhost:3000/
```

---

## Krok 4 — Otvor v prehliadači

Otvor prehliadač a choď na:

```
http://localhost:3000/help
```

Dokumentácia sa zobrazí. Môžeš klikať, prehľadávať, testovať.

---

## Zastavenie servera

Keď skončíš, vráť sa do Terminálu a stlač:

```
Ctrl + C
```

---

## Skrátený postup (po prvom nastavení)

```bash
cd /Users/michaldodok/help
python3 scripts/export/build_docusaurus.py

cd build/exports/docusaurus
npm start
```

Potom otvor http://localhost:3000/help

---

## Časté problémy

### „command not found: node" alebo „command not found: npm"
Node.js nie je nainštalovaný alebo terminál ho nevidí po inštalácii.
→ Reštartuj terminál a skús znova. Ak nepomôže, reštartuj Mac.

### „command not found: python3"
Python nie je nainštalovaný.
→ Stiahni ho z https://www.python.org/downloads/

### Port 3000 is already in use
Na porte 3000 beží iný program.
→ Skús: `npm start -- --port 3001` a otvor http://localhost:3001/help

### Stránka sa nezobrazuje správne / chýbajú obrázky
Pravdepodobne si zabudol spustiť exportný skript (Krok 1) pred `npm install`.
→ Zopakuj od Kroku 1.

---

## Poznámka k deploymentu

Produkčný deploy prebieha automaticky cez GitHub Actions —
stačí spustiť workflow `Deploy Help to Production` v GitHub.
Secrets (SFTP_USER, SFTP_PASSWORD, SFTP_HOST) sú rovnaké ako pre `api-docs`.

SFTP ciele:
- **Staging**: `/zooza.online/sub/staging-help/`
- **Production**: `/zooza.online/sub/help/`

> Ak sa cesty na serveri líšia, uprav ich v:
> `.github/workflows/deploy-help-staging.yml`
> `.github/workflows/deploy-help-production.yml`
