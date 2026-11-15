---
title: "Zooza through the years"
description: "Nine years of Zooza: what the app looked like at each stage, when each capability arrived, and why the product is shaped the way it is."
slug: "zooza-through-the-years"
type: "reference"
product_area: "Dashboard"
sub_area: ""
audience: ["admin"]
tags: ["reference", "changelog", "onboarding"]
status: "published"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: false
last_converted: "2026-11-15"
related_articles: ["dashboard", "getting-started-with-zooza", "reports-dashboard"]
---

# Zooza through the years

A cross-section of what the app looked like at each stage, what it could do, and how
releases were made — which changed more than the screens did.

> **Who this is for.** Anyone who wants to know why Zooza is shaped the way it is —
> a new colleague, a franchise partner, or a client who has been with us long enough
> to remember an older screen. It is a record, not a guide: nothing here tells you
> how to do anything.

---

## Why it changed

There is no grand plan behind the shape of this timeline, and it would be dishonest
to write one in afterwards.

**Zooza grew as its clients' demands grew.** A school asked for something, it got
built, and the next school asked for the thing after that. The invoicing system in
2022 and the WhatsApp work in 2025 are both in the list for the same reason: somebody
running classes needed them and said so.

**The design changed to keep up with the devices it was used on.** The screens below
are not a sequence of redesigns for their own sake. Each one is the product fitting
itself to how people actually opened it — and from about 2019 that increasingly meant
a phone in one hand, in a hall, between sessions.

**And new possibilities opened new work.** Online payments, direct debit, the shop,
and most recently running the business by talking to it. None of those were on anybody's
roadmap in 2016 because none of them were things you could reasonably do.

So read the eras below as a record of what was being asked for at the time, not as a
plan being executed.

---

## The eras

### July 2016 · before it was even called Zooza

![The course form in July 2016, branded z kurzy, annotated in fourteen numbered notes explaining what each field is for](../../assets/images/history/2016-07-course-form-annotated.png)

The product was **z kurzy**, in pink. One long form held everything a course needed:
basic properties, schedules, online registration, cancellations, waiting list and
make-ups. There were no tabs, no sections and no search — you scrolled.

What makes this particular picture worth keeping is that it is **annotated**. Somebody
opened it in Edge's Web Note and wrote fourteen numbered notes explaining what each field
was for — why the price field means one thing for a whole-course booking and another when
each session is sold separately, what the cancellation deadline is really protecting, what
"offer make-ups" should and should not reach. It is the only surviving record of the
reasoning, not just the result.

And the reasoning holds up. Note 14 asks whether a make-up may be taken in any course or
only this one. That is, word for word, a setting in the product today.

### October 2017 · the name and the Z arrive

![The courses list in October 2017: the orange Z, green course tiles with photographs, and a billing period named in the header](../../assets/images/history/2017-10-courses.png)

Fifteen months later the pink is gone and the orange **Z** is in the corner, where it
still is. Courses are tiles with photographs. The header already names a **billing
period** — *Jeseň 2017* — a concept that has never left.

Two things started here and never stopped: **a course is something you look at, not a
row in a table**, and **time is divided into named terms rather than running
continuously**.

### 2019 · the look we still have

![The 2019 dashboard: sage-green sidebar, orange Zooza wordmark, and donut charts for registrations and payments](../../assets/images/history/2019-07-dashboard.png)

The sage-green sidebar and the orange wordmark arrive, and the app stops changing its
appearance every year. From here the visual identity is stable and the work goes into
what is behind it.

The menu is four items — Kurzy, Registrácie, Kalendár, Komunikácia — against today's
dozen groups, which is a fair measure of how much the product has since taken on.

The dashboard counts capacity, registrations and occupancy, and splits payments by how
they arrived. Those are the questions the Reports section answers now, with a great deal
more arithmetic behind them.

### 2020 – 2022 · one release a quarter, each with a name

The repository begins on **21 November 2020**. From here the record stops being
photographs and starts being commits.

Versions were planned in Jira and shipped as events. Each carried a name that said
what it was for, and the commit messages still link to the release report.

| Shipped | Version | Named (Slovak) | What it was for |
|---|---|---|---|
| Dec 2020 | 2.5.3 | *Servisný release Leto 2020* | Summer 2020 service release |
| Jan 2021 | 2.5.4 | *Online platby* | **Online payments** |
| Apr 2021 | 2.5.5 | *Eshop — nehmotné veci* | **The shop**, for intangible goods |
| Jul 2021 | 2.5.6 | *Fixy, BabyBalance web a Book 1* | Fixes, the BabyBalance site, Book 1 |
| Aug 2021 | 2.5.7 | *Fixy a drobné veci* | Fixes and small things |
| Sep 2021 | 2.5.8 | *Refundácie a automatické platby* | **Refunds and automatic payments** |
| Oct 2021 | 2.5.9 | *Presúvanie registrácií* | **Moving bookings** between classes |
| Nov 2021 | 2.5.10 | *Drobné fixy* | Small fixes |
| Jan 2022 | 2.5.11 | *Fakturačný systém* | **The invoicing system** |

Read down the names and the product's priorities are obvious: **take money, then sell
other things, then give money back, then move people around, then invoice for all of
it.** Each one is a quarter of work landing at once, and the order is the order in
which schools hit the problem.

### 2023 – 2024 · release branches instead of Jira versions

Jira version names stop. Work moves onto `release-*` branches merged into main, and the
names go with them.

| Shipped | Version |
|---|---|
| Mar – Jun 2023 | 2.6.6, **2.6.7**, **2.6.71** *(translations)* |
| Apr 2024 | **2.8** |
| May 2024 | **2.9** |
| Aug 2024 | **3.0** |
| Oct 2024 | **3.1** |

Four releases in 2024 against one a quarter before it. The cadence is tightening but
the shape is the same: a branch collects work for weeks, then lands in one go.

### 2025 · four releases, each with a theme

| Shipped | Version | What went in |
|---|---|---|
| 28 Jan 2025 | **3.4** | |
| 28 Mar 2025 | **3.5** | |
| 9 Jun 2025 | **3.6** | |
| 16 Aug 2025 | **3.7** | WhatsApp, the course wizard, Ecomail |

The feature branches merged into 3.7 name themselves, and they say what 2025 was
about: **reaching parents where they already are.** WhatsApp instead of email,
Ecomail for bulk sending, and a wizard so setting a course up stopped being the
long form of 2016.

**3.7.5** is the first release with a full customer-facing changelog — twenty-five
entries, written for the people using it rather than for the team. A sample of what
landed in one release:

- **AI Payment Pairing** — matching bank transfers to bookings without a human
- **Fast Attendance**, **Cancellation Log**, **Payment Adjustments**
- **Referral Program**, **Sibling Discount**, **Returning Client Discount**
- **Stripe Standard Accounts**, Czech and Hungarian bank payments
- **In-App Support Chat**, the **Integrations Page**, **Custom Holidays**

### 2026 · written down before it is built, and shipped when it is done

The year opens on the old pattern and abandons it mid-way.

| Shipped | Version | Entries |
|---|---|---|
| early 2026 | **3.8** | 12 |
| | **3.8.1** | 3 |
| 30 Apr 2026 | **3.8.2** | 11 |
| 17 May 2026 | **3.8.3** | 10 |
| 28 May 2026 | **3.8.4** | 13 |

**And then the version numbers stop.** After 3.8.4 the changelog is stamped with the
month instead: `2026.06`, `2026.07`, `2026.08`, `2026.09`, `2026.10`, `2026.11`. There
is no 3.9. Work is written as a specification first, built, and shipped when it is
done — the month is just when it reached people.

**The specification system started in February 2026**, and by November it had produced
**787 implemented specs** across the three repositories:

| Month (2026) | Specs implemented |
|---|---|
| February | 14 |
| March | 69 |
| April | 82 |
| May | 80 |
| June | 64 |
| July | 52 |
| August | 49 |
| September | 111 |
| October | 81 |
| November | 61 *(to the 15th)* |

That is the real change in 2026. Not that more ships — that **nothing ships without
being written down first**, including the reasons, the things deliberately left out,
and what would have to be true for it to be correct.

![The Zooza dashboard in November 2026: a greeting, a prompt box for Zooza AI, next sessions, and a dozen menu groups down the left](../../assets/images/history/2026-11-dashboard.png)

Set this against the 2019 dashboard above. The sidebar is the same colour and the
wordmark is the same orange — but the four menu items are now a dozen groups, and the
first thing on the page is **a box you type a question into**.

---

## The 2016 form, ten years on

The single most useful comparison in this page is the course form, because it is the
same job in both pictures.

![Programme settings in November 2026: a Setup summary, a settings search box, and grouped cards for Joining, Paying and the rest](../../assets/images/history/2026-11-programme-settings.png)

In 2016 every decision about a course sat in one scrolling form. Today the same
decisions are:

- **a Setup summary at the top** — programme type, payment, online booking, attendance,
  trial, next term, feedback, extra sessions, each showing its current answer;
- **a search box**, because there are now too many settings to scan;
- **cards grouped by what you are trying to do** — *Joining*, *Paying* and the rest —
  rather than by which database table the field belongs to.

Nothing was removed. The 2016 fields are nearly all still there. What changed is that
the product stopped expecting you to hold the whole thing in your head at once.

---

## How releases were made

The shipping method changed more than the product did, and in a direction worth naming.

| Era | Unit of work | How often | Decided |
|---|---|---|---|
| 2020 – 2022 | A named Jira version | Roughly quarterly | In Jira, before the quarter |
| 2023 – 2024 | A `release-*` branch | Three or four a year | In the branch, as it filled |
| 2025 | A themed release | Four a year | By theme, up front |
| 2026 | One written specification | Continuously | In the spec, before any code |

Each step moves the decision earlier and the batch smaller. The 2020 release shipped a
quarter of work and found out afterwards whether it was right. A 2026 spec states what
is in scope, what is explicitly out, and how you would know it worked — before the first
line is written.

---

## What the archive holds

The pictures for 2016 – 2019 come from a set Michal kept over nine years, by date:

`2016-07` · `2016-09` · `2017-02` · `2017-10` · `2019-09` · `2020-01` · `2022-06` ·
`2022-09` · `2023-03` · `2023-12` · `2024-12` · `2025-08`

Seventy-six files, including two presentations and a document of change notes. **Only
three of those dates are used here.** The years between 2020 and 2025 are told in words
and release names, because the pictures for them have not been brought across yet — and
those are exactly the years the product changed shape most.

**What the repository cannot tell you is who asked.** It records that invoicing
shipped in January 2022; it has nothing to say about the school that could not issue
a document their accountant would accept. That half of the story lives with the people
who were there, which is why *Why it changed* above is written as one honest set of
reasons rather than a motive invented for each era.

If a particular year is worth drawing out properly, the pictures for it are already
in the archive and the dates are already in git. What it needs is the one thing neither
holds: the name of the problem somebody had that month.
