# Programme settings redesign — what it means for the help

Written 2026-11-08 from `feature-programme-settings-redesign` (app), the specs on it,
and the 52 screenshots in `help_ingest/screenshots/8nov`. On test; production soon.

## What actually changed

Not a reskin. The screen stopped being organised by Zooza's feature modules and became a
**hub organised by the stage a family is at**.

- **Setup card** on Settings: the handful of decisions that shape a programme, shown as a
  grid of answers — programme type, for children, payment, online booking, booking form,
  attendance, trial, next term, feedback, extra sessions — with **Review setup**.
- **Search**, with a live count ("21 matching settings") that highlights matches inside
  tiles. It searches labels, aliases, help text *and the option labels inside lists*.
- **Stages** (`Joining`, `Keeping…`, `About the…`, `Switched off`) holding **tiles**, whose
  rows are edit groups showing a headline value.
- **One drawer per edit group**, each with its own URL, an eyebrow naming the stage, and a
  **help pane** on the right carrying prose help plus **Related settings** cross-links.
- **No Save button. "Changes save automatically."**

Scale, from the registry the team generated: **43 edit groups, 201 settings.**

## The three things that break our articles

**1. "Click Save" is now wrong.** Drawers save as you go. Twelve of our core articles end a
procedure with Save.

**2. Every navigation path into a setting changed shape.** "Programme → Settings → Price and
payment → Edit" becomes "open the drawer from its tile, or search for the field". The
destination survives — the spec keeps a **legacy alias table** precisely so bookmarks and
help articles still land in the right drawer — but the *route a reader is told to walk*
does not.

**3. Groups split and one setting is gone.** Programme basics became two drawers (basics,
additional details). `fees_included_in_price` was removed outright.

## How big

| | |
|---|---|
| Articles touching programme settings at all | **116** |
| Of those, matching two or more signals — the core set | **57** |
| Core articles that tell the reader to Save | 12 |
| Articles that deep-link `?edit=` | 0 — nothing to repoint |

## Method, so no article escapes

The registry is the checklist, and it is machine-readable. Four passes, each mechanical
enough to be repeatable rather than a matter of my memory:

1. **Inventory both sides.** 201 settings and 43 groups from
   `app:docs/programme-settings/inventory.md`; 116 articles from a three-signal grep
   (edit links, navigation cues, tile names).
2. **Map every setting to the articles that mention it**, by label, using the same
   normalised comparison `check_ui_labels.py` already does. A setting with no article is a
   gap; an article naming a setting that the registry no longer has is a stale claim.
3. **Rewrite by group, not by article.** One drawer at a time, fixing every article that
   touches it together — otherwise two articles end up describing the same drawer
   differently.
4. **Re-run the checkers.** `check_ui_labels.py` for field names, `check_nav.py` for paths,
   `image_audit.py` for the pictures. The 201 labels become the new ground truth.

## The photographs

**The 49 settings screenshots are good** — English, styled, real structure. They are from
the `Kids academy` test company, which is fine: no customer data on a settings screen.

**The three profile screenshots are not usable, and anonymising will not fix them.** They
are the parent zone, in **Slovak**, with the **CSS not loaded**, showing a real name and
date of birth. Our help is English and the pictures must look like what a parent sees.
The answer is not to blur them: it is to capture the parent zone from the demo account,
which already works — seven client-zone shots captured cleanly in the 6 November run using
the saved client session.

## One thing worth a decision

The drawer's help pane is **authored content**, kept as per-locale files outside the
translation pipeline. That makes it a second help surface describing the same settings as
the help centre, maintained by a different route.

Two surfaces explaining one thing drift apart; this is exactly how the KB ended up with
articles contradicting each other on where invoices live. Worth deciding now who owns that
text, and whether the help centre should be its source.
