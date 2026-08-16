#!/usr/bin/env python3
"""
Analyze Intercom conversations from help_ingest/intercom/ and extract topic frequency.
Only processes conversations from 2026-04-02 onwards (post last intake).

Usage:
    python3 scripts/analyze_intercom_topics.py
"""

import json
import os
import re
import glob
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).parent.parent.parent / "help_ingest" / "intercom"
CUTOFF = "2026-04-02"

NOISE_TITLES = [
    "success! your video is ready",
    "new passkey added",
    "verifying it's you",
    "your atlassian account",
    "upcoming changes to how atlassian",
    "new meeting booked",
    "is a new friend suggestion",
    "march report is ready",
    "hey — your",
    "invitation to exhibit",
    "doporučovací program",
    "sibling discount",
    "geschwisterrabatt",
    "kolik rodin",
    "how many families",
    "wie viele familien",
]

TOPICS = {
    "Náhrady / make-up sessions": [
        "náhrad", "náhradn", "náhradka", "nahrad", "náhrady", "replacement",
        "make-up", "makeup", "vybírání náhrad", "ukazuje náhrad", "nevidí náhrad",
        "matko", "náhradný termín", "zmeškané", "catch up",
    ],
    "Bloky / blocks": [
        "blok", "block", "bloku", "bloky", "blokov", "blocks",
        "alikvótna", "alikvot", "neskoré prihlásenie", "neskorého prihlásenia",
        "late.*registr", "aliquot", "pro.rata",
    ],
    "Permanentky / entry passes": [
        "permanentk", "vstupový pass", "entry pass", "kredit.*pass",
        "pass.*kredit", "predplatené hodiny", "nabiť kredit",
    ],
    "Párovanie platieb / bank transactions": [
        "párovania", "párovanie", "spárovat", "spárovanie", "platba.*banka",
        "bankový.*výpis", "výpis transakcii", "výpis transakci", "pohyb.*účet",
        "inbound payment", "bank transfer", "preplaceno", "přeplaceno",
        "preplaten", "faktur", "import platb", "csv.*platb",
    ],
    "Platobné plány / payment plans": [
        "platob.*plán", "payment plan", "splátk", "platob.*šablón",
        "payment schedule", "scheduled payment", "platob.*template",
        "fakturáci", "billing", "payment template",
    ],
    "Registrácia / booking": [
        "registráci", "registrace", "registraci", "booking", "prihláseni",
        "registration", "zápis", "enrol",
    ],
    "Mobile / app problémy": [
        "telefon", "mobil", "mobile", "app.*nefung", "nefunguje.*app",
        "smartphon", "iphone", "android", "kliknem.*nic", "nič.*neurobí",
    ],
    "Email problémy": [
        "email.*odmietnut", "odmietnutý email", "email.*reject", "bounce",
        "nedostat email", "neodeslan", "neodoslan", "email.*nefung",
        "email.*spam", "spam.*email", "neprišiel email", "nedostal email",
        "email.*neodišiel",
    ],
    "Widgety / embedding": [
        "widget", "embed", "iframe", "formulár.*web", "web.*formulár",
        "booking form.*web", "stránk.*widget",
    ],
    "Lektor / instructor": [
        "lektor", "instructor", "lektor.*prida", "pridať lektora",
        "lektor.*nastav", "lektor.*nefung",
    ],
    "Klientský profil": [
        "klientsk.*profil", "client.*profile", "profil.*klient",
        "prihláseni.*klient", "client.*login", "klient.*login",
    ],
    "Kapacita / waiting list": [
        "kapacit", "capacity", "čakaci.*listina", "waiting list",
        "waitlist", "čakačk", "plná kapacit",
    ],
    "Zľavy / discounts": [
        "zľav", "slev", "discount", "súrodeneck", "sibling",
        "coupon", "promo", "code.*zľav",
    ],
    "Notifikácie / automation": [
        "notifikáci", "notification", "automatick.*email", "email.*automatick",
        "reminder", "pripomienk", "automation", "automatizáci",
    ],
    "Zrušenie / cancellation": [
        "zrušeni", "zrušenie", "zrušil", "cancel", "storno", "odhláseni",
        "odhlásil", "odhlásenie",
    ],
    "Fakturácia / invoicing": [
        "faktúr", "faktur", "invoice", "dobropis", "credit note",
        "fakturačn", "vystavila faktúr",
    ],
    "Chyba / bug report": [
        "chyb", "chybu", "bug", "nefunguje", "nefunkčn", "error",
        "urgent", "URGENT", "broken", "pokazil",
    ],
    "Ukončenie / offboarding": [
        "ukončeni", "ukonceni", "terminate", "koniec zmluvy",
        "prestať používať", "zrušit.*účet", "deactivat",
    ],
}


def strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def is_noise(title: str) -> bool:
    t = title.lower()
    return any(n in t for n in NOISE_TITLES)


def get_text(conv: dict) -> str:
    parts = [strip_html((conv.get("source") or {}).get("body") or "")]
    for p in conv.get("conversation_parts", {}).get("conversation_parts", []):
        if p.get("author", {}).get("type") in ("user", "admin", "lead"):
            parts.append(strip_html(p.get("body") or ""))
    title = conv.get("title") or ""
    parts.append(title)
    return " ".join(parts)


def match_topics(text: str) -> list[str]:
    text_lower = text.lower()
    matched = []
    for topic, patterns in TOPICS.items():
        for pat in patterns:
            if re.search(pat, text_lower):
                matched.append(topic)
                break
    return matched


def main():
    dates = sorted(
        d for d in os.listdir(BASE)
        if d >= CUTOFF and os.path.isdir(BASE / d)
    )

    topic_counts = defaultdict(int)
    topic_examples = defaultdict(list)
    total = 0
    noise_skipped = 0

    for date in dates:
        for fpath in glob.glob(str(BASE / date / "*.json")):
            try:
                with open(fpath) as f:
                    conv = json.load(f)
            except Exception:
                continue

            title = conv.get("title") or ""
            if is_noise(title):
                noise_skipped += 1
                continue

            total += 1
            text = get_text(conv)
            matched = match_topics(text)

            for topic in matched:
                topic_counts[topic] += 1
                if len(topic_examples[topic]) < 3:
                    snippet = text[:200].replace("\n", " ")
                    topic_examples[topic].append(f"[{date}] {title[:60]} — {snippet[:120]}")

    print(f"Conversations analysed: {total} (skipped noise: {noise_skipped})")
    print(f"Date range: {dates[0]} → {dates[-1]}\n")
    print("=" * 70)
    print(f"{'TOPIC':<45} {'COUNT':>6}  {'% of total':>10}")
    print("=" * 70)

    for topic, count in sorted(topic_counts.items(), key=lambda x: -x[1]):
        pct = count / total * 100
        bar = "█" * int(pct / 2)
        print(f"{topic:<45} {count:>6}  {pct:>8.1f}%  {bar}")

    print("\n" + "=" * 70)
    print("EXAMPLES PER TOPIC (up to 3)")
    print("=" * 70)
    for topic, count in sorted(topic_counts.items(), key=lambda x: -x[1]):
        print(f"\n## {topic} ({count}x)")
        for ex in topic_examples[topic]:
            print(f"  • {ex}")


if __name__ == "__main__":
    main()
