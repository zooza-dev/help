---
title: "Zooza through the years"
description: "How the app and the way we ship it have changed since 2016 — from quarterly Jira releases to continuous delivery, with the screens from each era."
slug: "zooza-through-the-years"
type: "reference"
product_area: "Dashboard"
sub_area: ""
audience: ["admin"]
tags: ["reference", "changelog", "onboarding"]
status: "draft"
source_legacy_path: ""
source_language: "en"
needs_screenshot_replacement: true
last_converted: "2026-11-06"
related_articles: ["reports-dashboard", "getting-started-with-zooza"]
---

# Zooza through the years

A cross-section of what the app looked like at each stage, and of how releases
were made — which changed more than the screens did.

> **Draft, not published.** This page is in the repository but not on the help
> centre. It stays that way until the picture set is complete and we have
> decided who it is for.

---

## Where the facts come from

Two sources, and they cover different periods, so the page is honest about
which is which.

- **2016 – 2020: pictures only.** The app repository begins on **21 November
  2020**; nothing before that is in version control. For those years the
  screenshots *are* the record, which is the whole reason for collecting them.
- **2020 – today: the repository.** Release names, dates and the shape of the
  work are read out of git, not remembered.

---

## The eras

### 2016 – 2020 · before the record

*Waiting on screenshots. See [what to send](#what-this-page-still-needs).*

What we want from this period is less the features than the look: the density,
the colours, the vocabulary on the buttons. This is the stretch nobody can
reconstruct later.

### Late 2020 – 2022 · named releases, a few a year

Versions were planned in Jira and shipped as events, each with a name that said
what it was for. The commit messages still carry the release report links.

| Date | Version | What it was called |
|---|---|---|
| Dec 2020 | 2.5.3 | Servisný release Leto 2020 |
| Jan 2021 | 2.5.4 | Online platby |
| Apr 2021 | 2.5.5 | Eshop — nehmotné veci |
| Jul 2021 | 2.5.6 | Fixy, BabyBalance web a Book 1 |
| Aug 2021 | 2.5.7 | Fixy a drobné veci |
| Sep 2021 | 2.5.8 | Refundácie a automatické platby |
| Oct 2021 | 2.5.9 | Presúvanie registrácií |
| Nov 2021 | 2.5.10 | Drobné fixy |
| Jan 2022 | 2.5.11 | Fakturačný systém |

Read down the names and the product's priorities are obvious: online payments
first, then the shop, then refunds and automatic payments, then invoicing. Each
one is a quarter of work landing at once.

### 2023 – 2024 · release branches

Jira version names stop; the work moves onto `release-*` branches merged into
main. **2.6.7** and **2.6.71 Preklady** in 2023, then **2.8** (April 2024),
**2.9** (May 2024) and **3.0** (August 2024). Three releases in a year instead
of one a quarter.

### 2025 · four releases, each with a theme

**3.4** (January), **3.5** (March), **3.6** (June), **3.7** (August). The
feature branches merged into 3.7 name themselves: WhatsApp, the course wizard,
Ecomail.

### 2026 · continuous, and specified before it is built

**3.8.2** lands in April and **3.8.3** in May, and then the numbered release
largely stops being the unit. Work is written as a spec first, built, and
shipped when it is done. A changelog entry is drafted per spec rather than per
release — the **Changelog** page in the app is the customer-facing end of that.

**The clearest measure of the shift is the volume of work landing in main:**

| Year | Commits on main |
|---|---|
| 2020 | 3 |
| 2021 | 10 |
| 2022 | 77 |
| 2023 | 156 |
| 2024 | 581 |
| 2025 | 573 |
| 2026 | 2 217 *(and the year is not over)* |

> **A caution about that table.** Commits measure activity, not value, and they
> are affected by how people commit as much as by how much ships. The 2020 and
> 2021 numbers are low partly because the repository was new. Read the curve,
> not the figures.

---

## What this page still needs

**Screenshots, roughly dated.** One or two per year is plenty — the home
screen or the booking list is enough to show the era. Put them in
`help_ingest/screenshots/history/` and name them so the year is in the
filename: `2016-dashboard.png`, `2018-bookings.png`. Approximate is fine; say
so and the caption will say so too.

Worth having if they exist:

- **The first version anyone used in anger**, 2016 or 2017.
- **The oldest booking form**, which is what customers' customers saw.
- **Anything from a rebrand** — the point where the colours or the logo changed.
- **A screen that no longer exists at all.** Those are the most interesting and
  the first to be lost.

**And the part only you know:** why each change happened. The repository says
*when* invoicing shipped; it does not say which customer asked for it, or what
broke before it existed. A sentence per era turns a list of versions into
something worth reading.
