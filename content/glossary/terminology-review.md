---
title: "Zooza Terminology — Internal Review"
slug: "terminology-review"
status: "draft"
type: "reference"
product_area: "Settings"
audience: ["admin"]
last_converted: "2026-03-13"
---

# Zooza Terminology — Internal Review

> **Internal document — not for publication.**
> This is the human-readable view of `terminology.yml`.
> Edit the YAML as source of truth; this file is for review only.

---

## How to read this

- **Canonical** = the one correct term to use in all new content
- **Admin / Client / Widget** = what each audience sees
- **Deprecated** = old terms to replace when found in content
- **AI keywords** = what customers actually type (for AI disambiguation)

---

## Entity misattribution — AI critical patterns

People often name the wrong entity when describing an action. The AI must identify the **intended action** and **correct entity** from natural language.

| What the customer says | What they actually mean | Correct entity | Action |
|---|---|---|---|
| "copy a client" | copy the client's booking to another class | Booking | Copy |
| "kopírovať klienta" | kopírovať prihlásenie do inej skupiny | Booking | Copy |
| "move a child / move my child" | move the registration to another class | Booking | Transfer |
| "presunúť dieťa" | presunúť prihlásenie do inej skupiny | Booking | Transfer |
| "move a client to another group" | transfer the booking | Booking | Transfer |
| "prehodiť klienta do inej skupiny" | presunúť prihlásenie | Booking | Transfer |
| "cancel a client" | cancel or end the client's booking | Booking | Cancel booking |
| "zrušiť klienta" | zrušiť prihlásenie | Booking | Cancel booking |
| "delete a client" | usually means end/cancel the booking, rarely actual client deletion | Booking (usually) | Clarify — ask if they mean cancel the booking or remove the client record |
| "add a client to another group" | copy the booking to another class | Booking | Copy |
| "pridať klienta do inej skupiny" | kopírovať prihlásenie | Booking | Copy |
| "enrol the child in two groups" | create two bookings (or copy one) | Booking | Copy / new Booking |
| "move a session" | reschedule a session date | Session | Reschedule session |
| "free session for a client" | grant free credits on a booking OR make-up session — clarify | Booking | Free credits or Make-up |
| "give the client a free lesson" | grant free credits on booking | Booking | Free credits |

### AI rule
> When a customer says "client", "child", "attendee", or "parent" in the context of
> moving, copying, cancelling, or adding — the action almost always applies to the
> **Booking**, not the Client entity itself.
> Always confirm: *"Do you want to [action] the registration/booking to [target]?"*

---

## Product Hierarchy

### Programme
- **Canonical:** Programme
- **Admin:** Programme | **Client/Widget:** Class
- **Deprecated:** Course, Open course, One-time course
- **Definition:** Top-level container. Holds pricing, payment settings, booking form, and scheduling rules. One Programme contains multiple Classes.
- **SK:** Program | **DE:** Programm / Kurs
- **AI keywords (EN):** programme, program, course, activity
- **AI keywords (SK):** program, kurz, aktivita, hodiny
- **AI keywords (DE):** Programm, Kurs, Aktivität
- **Note:** When domain = widget → displayed as "Class". Admin always uses "Programme".

---

### Class
- **Canonical:** Class
- **Admin:** Class | **Client/Widget:** Class
- **Deprecated:** Group, Timetable, batch, track
- **Definition:** Scheduled group within a Programme. Differentiated by day/time, level, or location. Inherits all Programme settings.
- **SK:** Skupina / Lekcia | **DE:** Gruppe / Kurs
- **AI keywords (EN):** class, group, timetable, schedule, my class, which group
- **AI keywords (SK):** skupina, trieda, hodina, rozvrh
- **AI keywords (DE):** Klasse, Gruppe, Kurs, Stundenplan
- **Note:** Used at two levels — (1) subdivision within a Programme (admin), and (2) top-level name for Programme in client/widget view.

---

### Session
- **Canonical:** Session
- **Admin/Client/Widget:** Session
- **Deprecated:** slot, appointment, date, time slot
- **Synonyms:** lesson, class session
- **Definition:** Single scheduled meeting within a Class, with specific date and time. Attendance recorded at session level.
- **SK:** Termín / Hodina | **DE:** Termin / Stunde / Einheit
- **AI keywords (EN):** session, lesson, slot, time, date, class date, next session
- **AI keywords (SK):** termín, hodina, lekcia, dátum, čas
- **AI keywords (DE):** Termin, Stunde, Einheit, Datum

---

## Programme Types

### Pay-as-you-go
- **Canonical:** Pay-as-you-go
- **Deprecated:** Open course, Open registration, drop-in, flexible
- **Synonyms:** PAYG, per-session, drop-in
- **Definition:** Flexible programme. Clients book and pay for individual sessions. No full-term commitment.
- **SK:** Platba za termín / Otvorený kurz | **DE:** Pay-as-you-go / Einzelbuchung
- **AI keywords (EN):** pay as you go, drop in, single session, flexible, per session, no commitment
- **AI keywords (SK):** platba za termín, jednotlivé termíny, bez záväzkov
- **AI keywords (DE):** einzeln, flexibel, ohne Bindung, einzelne Stunde

---

### One-off Event
- **Canonical:** One-off Event
- **Deprecated:** One-time course, Registration for one session, single session event
- **Synonyms:** workshop, event, one-time event
- **Definition:** Single session on a specific date. No repeating schedule. For workshops, lectures, consultations.
- **SK:** Jednorazová udalosť | **DE:** Einzelveranstaltung / Einmaliger Kurs
- **AI keywords (EN):** one off, one-off, single event, workshop, one time, one session
- **AI keywords (SK):** jednorazovo, jednorazový, workshop, prednáška, konzultácia
- **AI keywords (DE):** einmalig, Workshop, Einzeltermin, Veranstaltung

---

### Membership
- **Canonical:** Membership
- **Synonyms:** subscription, recurring membership
- **Definition:** Ongoing programme with recurring fixed charge and no fixed end date.
- **SK:** Členstvo / Predplatné | **DE:** Mitgliedschaft / Abo
- **AI keywords (EN):** membership, subscription, monthly fee, recurring, ongoing
- **AI keywords (SK):** členstvo, predplatné, mesačný poplatok, opakujúca sa platba
- **AI keywords (DE):** Mitgliedschaft, Abo, monatlich, Dauerauftrag

---

### 1-to-1 class
- **Canonical:** 1-to-1 class
- **Admin:** 1-to-1 class | **Client/Widget:** Private class
- **Deprecated:** Individual class, individual session, private lesson
- **Synonyms:** private class, individual lesson
- **Definition:** Class with a single attendee. Admin sees "1-to-1 class"; clients see "Private class".
- **SK:** Individuálna hodina / Súkromná hodina | **DE:** Einzelstunde / Privatstunde
- **AI keywords (EN):** 1 to 1, one to one, private, individual, private class, private lesson
- **AI keywords (SK):** individuálna hodina, súkromná hodina, privát
- **AI keywords (DE):** Einzelstunde, Privatstunde, Einzelunterricht

---

## Bookings & Enrolment

### Booking / Enrolment
- **Canonical (admin):** Booking
- **Canonical (client/widget):** Enrolment
- **Deprecated:** Registration, sign-up, enrollment (American spelling)
- **Definition:** A client's formal commitment to attend a Class. Creates a payment obligation.
- **SK:** Prihlásenie / Zápis | **DE:** Buchung / Anmeldung
- **AI keywords (EN):** booking, enrolment, enrollment, registration, sign up, book a spot
- **AI keywords (SK):** prihlásenie, prihláška, zápis, registrácia, prihlásiť
- **AI keywords (DE):** Buchung, Anmeldung, einschreiben, buchen, anmelden
- **Do not confuse with:** Transfer (moves a booking), Copy (duplicates a booking)
- **AI note:** Transfer and Copy apply to the Booking entity — not to the Client. If customer says "move my child" → clarify: "Do you want to move the registration to another class?"

---

### Transfer
- **Canonical:** Transfer
- **Deprecated:** move booking, switch group, change class, relocate
- **Synonyms:** move, switch
- **Definition:** Move a booking from one Class/Group/Programme to another. Original booking ends; new booking created in target Class.
- **SK:** Presunúť / Prehodiť | **DE:** Verschieben / Wechseln
- **AI intent keywords:**
  - EN: transfer, move, switch, change group, change class, move to another, switch class
  - SK: presunúť, prehodiť, zmeniť skupinu, presun, premiestiť, iná skupina
  - DE: verschieben, wechseln, umbuchen, in andere Gruppe, Gruppenänderung
  - PL: przenieść, zmienić grupę, przeniesienie
  - RO: mută, schimbă grupa, transfer
  - HU: áthelyezni, csoport csere
  - IT: spostare, trasferire
  - FR: déplacer, transférer, changer de groupe
- **Do not confuse with:** Copy — Transfer moves the booking (original ends); Copy duplicates it (original stays)

---

### Copy
- **Canonical:** Copy
- **Deprecated:** duplicate booking, clone
- **Synonyms:** duplicate, clone
- **Definition:** Duplicate a booking to another Class/Group/Programme. Original booking remains unchanged. Payment schedules do NOT carry over.
- **SK:** Kopírovať / Zduplikovať | **DE:** Kopieren / Duplizieren
- **AI intent keywords:**
  - EN: copy, duplicate, clone, also enrol in, add to another class, copy booking
  - SK: kopírovať, duplikovať, zduplikovať, skopírovať, zaradiť aj do
  - DE: kopieren, duplizieren, auch einschreiben, in weitere Gruppe
  - PL: skopiować, zduplikować
  - RO: duplică, copie, copiere
  - HU: másolni, duplikálni
  - IT: duplicare, copiare
  - FR: copier, dupliquer
- **Do not confuse with:** Transfer — Copy leaves original in place; Transfer removes it

---

### Trial
- **Canonical:** Trial
- **Admin:** Trial | **Client/Widget:** Trial session
- **Deprecated:** free trial session, taster session, introductory class
- **Synonyms:** trial session, taster
- **Definition:** First free or discounted session. Status: Trial Started → Trial Won / Trial Lost.
- **SK:** Skúšobná hodina | **DE:** Probestunde / Schnupperstunde
- **AI keywords (EN):** trial, trial session, free session, taster, try out, introductory
- **AI keywords (SK):** skúšobná hodina, trial, prvá hodina zadarmo, vyskúšať
- **AI keywords (DE):** Probestunde, Schnupperstunde, kostenlose Stunde, ausprobieren

---

## Clients & Attendees

### Client
- **Canonical:** Client
- **Deprecated (as generic replacements):** parent, customer, account holder
- **Synonyms:** parent (acceptable in family context)
- **Definition:** Person who holds the account, pays, and manages bookings. Unique identifier = email address.
- **SK:** Klient / Zákazník | **DE:** Kunde / Klient
- **Do not confuse with:** Attendee — Client is the payer; Attendee is the person who attends (may be a child)

---

### Attendee
- **Canonical:** Attendee
- **Deprecated (as generic replacements):** child, pupil, student, participant
- **Synonyms:** child (acceptable in family/youth context), participant, student
- **Definition:** Person who physically attends sessions. May differ from the Client (parent books for child).
- **SK:** Účastník / Dieťa | **DE:** Teilnehmer / Kind

---

## Attendance

### Make-up session
- **Canonical:** Make-up session
- **Deprecated:** Replacement session, replacement lessons, catch-up session, substitute session
- **Synonyms:** replacement session, catch-up
- **Definition:** Replacement session earned by cancelling a scheduled session in advance (before deadline). Make-up credit generated automatically.
- **SK:** Náhradná hodina | **DE:** Ersatzstunde / Ersatztermin / Nachholtermin
- **AI keywords (EN):** make-up, makeup, replacement, catch up, missed session, attend another, reschedule
- **AI keywords (SK):** náhradná hodina, náhrada, zmeškané, náhradný termín, preložiť hodinu
- **AI keywords (DE):** Ersatzstunde, Ersatztermin, Nachholtermin, verpasste Stunde, Nachholen
- **Do not confuse with:**
  - **Free credits:** Make-up = earned by cancellation (attendance). Free credits = granted allowance on booking (access).
  - **Billable session:** Billable sessions = pricing calculation only. Never mention when answering attendance questions.

---

### Free credits
- **Canonical:** Free credits
- **Deprecated:** free sessions, voľné termíny (SK colloquial), complimentary sessions
- **Definition:** Allowance granted to a booking that lets a client attend extra sessions without paying. Different from make-up credits.
- **SK:** Voľné termíny / Kredity zadarmo | **DE:** Freistunden / Gratisguthaben
- **AI keywords (EN):** free sessions, free credits, complimentary, extra sessions, sessions included
- **AI keywords (SK):** voľné termíny, zadarmo, kredity zadarmo
- **AI keywords (DE):** Freistunden, gratis, kostenlose Stunden, Gutschrift
- **Do not confuse with:** Make-up session (earned by cancellation), Billable session (pricing setting)

---

### Billable session
- **Canonical:** Billable session
- **Definition:** Session that counts toward total used for price calculation in Programme/Class settings. This is a **pricing tool only** — not an attendance feature.
- **SK:** Spoplatnený termín | **DE:** Abrechenbare Stunde
- **Do not confuse with:** Make-up session, Free credits
- **AI note:** Only discuss billable sessions when customer explicitly asks about pricing calculation settings. Never mention in response to attendance or make-up questions.

---

## Payments

### Payment Plan
- **Canonical:** Payment Plan
- **Deprecated:** Payment schedule, Scheduled payments, invoice profile, payment template, billing frequency
- **Definition:** Configuration that defines when and how often a client is billed (one-time, monthly, quarterly, by-block, etc.).
- **SK:** Platobný plán | **DE:** Zahlungsplan / Zahlungsrhythmus
- **AI keywords (EN):** payment plan, payment schedule, how to pay, billing, instalments, when billed
- **AI keywords (SK):** platobný plán, spôsob platby, platba, fakturácia, splátky
- **AI keywords (DE):** Zahlungsplan, Zahlungsrhythmus, Ratenzahlung, wann zahlen

---

### Term Payment
- **Canonical:** Term Payment
- **Deprecated:** Course fee
- **Definition:** Payment covering a specific term or billing period.
- **SK:** Platba za semester | **DE:** Kursbeitrag / Semesterbeitrag

---

### Reference number
- **Canonical:** Reference number
- **Deprecated:** Variable symbol, variabilný symbol, VS
- **Synonyms:** payment reference
- **Definition:** Unique identifier included with bank transfer payments for automatic matching.
- **SK:** Variabilný symbol / Referenčné číslo | **DE:** Verwendungszweck / Referenznummer
- **AI keywords (SK):** variabilný symbol, referenčné číslo, VS, prevod

---

### Entry pass
- **Canonical:** Entry pass
- **Deprecated:** credit pass, visit pass, prepaid sessions, pass
- **Synonyms:** credit pass, visit pass
- **Definition:** Prepaid bundle — either visits-based (fixed number of sessions) or money-based (credit amount). Used with Pay-as-you-go programmes.
- **SK:** Vstupový pass / Kredit | **DE:** Eintrittskarte / Guthaben / Pass
- **AI keywords (EN):** entry pass, pass, credit, prepaid, bundle, 10 sessions, top up
- **AI keywords (SK):** pass, kredit, predplatené hodiny, vstupová karta, nabiť kredit
- **AI keywords (DE):** Eintrittskarte, Guthaben, Prepaid, Paket, aufladen

---

## Settings

### Venue
- **Canonical:** Venue
- **Deprecated:** Place, Location, place, location
- **Synonyms:** location
- **Definition:** Physical location where sessions take place. Assigned at Class level.
- **SK:** Miesto / Sála / Prevádzka | **DE:** Standort / Ort / Halle
- **AI keywords (EN):** venue, location, place, address, where, room, hall
- **AI keywords (SK):** miesto, adresa, kde, sála, miestnosť
- **AI keywords (DE):** Standort, Ort, Adresse, Halle, wo

---

## Platform

### Widget
- **Canonical:** Widget
- **Synonyms:** booking widget, booking form, calendar widget
- **Definition:** Embeddable booking interface on the provider's website. Widget domain = client-facing terminology throughout.
- **SK:** Widget / Rezervačný formulár | **DE:** Widget / Buchungsformular
- **Note:** When domain = widget, all terminology flips to client-facing: Programme → Class, Booking → Enrolment, etc.

---

### Client Profile
- **Canonical:** Client Profile
- **Deprecated:** parent portal, customer portal, client portal
- **Synonyms:** client portal, parent portal (family context)
- **Definition:** Self-service dashboard for clients. Manage bookings, payments, family members. Email-link access (no password).
- **SK:** Profil klienta | **DE:** Kundenprofil / Kundenbereich

---

### Feedback
- **Canonical:** Feedback
- **Deprecated:** Course feedback
- **Synonyms:** review, rating
- **Definition:** Structured feedback collected from clients after sessions or end of programme.
- **SK:** Spätná väzba / Hodnotenie | **DE:** Feedback / Bewertung

---

## Deprecated Terms — Quick Reference

| Old term | Use instead |
|---|---|
| Course | Programme (admin) / Class (client) |
| Course fee | Term Payment |
| Course feedback | Feedback |
| Open course | Pay-as-you-go |
| One-time course | One-off Event |
| Registration for one session | One-off Event |
| Open registration | Pay-as-you-go |
| Registration | Booking (admin) / Enrolment (client) |
| Payment schedule | Payment Plan |
| Scheduled payments | Payment Plan |
| Invoice profile | Payment Plan |
| Payment template | Payment Plan |
| Place | Venue |
| Location | Venue |
| Variable symbol | Reference number |
| Individual Class | 1-to-1 class (admin) / Private class (client) |
| Group | Class |
| Timetable | Class |
| Replacement session | Make-up session |
| Free sessions | Make-up session OR Free credits (clarify context) |
| Parent portal | Client Profile |
| Customer portal | Client Profile |
