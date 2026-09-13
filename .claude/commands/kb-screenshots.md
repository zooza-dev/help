# kb:screenshots — recapture screenshots from the live app

## Purpose
Replace stale screenshots with fresh ones taken from the running application,
without publishing anybody's personal data and without quietly shipping pictures
of the wrong screen.

As of September 2026 the library is **983 images, 806 of them dated January to
March** — the original conversion. The articles carrying the most are
`payment-templates-creation` (32), `trial-sessions` (29), `documents` (25),
`personas` (21), `user-roles` (20).

A second reason to run it: walking the app screen by screen is the fastest way
to learn how it actually behaves. Several corrections to the KB in September came
out of looking at a screenshot, not at the source.

## When to run
- After a spec ships that changes a screen — reshoot that screen while you still
  remember which one it was. This is the step whose absence created the backlog.
- In batches, working down the stale list, when there is time.

## Before you start

**One account, one region, one theme.** Playfulmotion on `uk.zooza.app`, light
mode, default orange. Mixing accounts or regions makes the help look like five
different products. Check the company name under the logo, top left, before
capturing anything — the login can land you somewhere else.

**Sign in.** The app has no passwords; ask the user for a magic link, then:

```bash
python3 scripts/screenshots/capture.py --login '<magic-link>'
```

That writes `build/intake/zooza-session.json`, which is gitignored and is a
credential. Never move it into the repo proper, never commit it, and do not
reuse the magic link afterwards.

**Set up masking.** `build/intake/screenshot-mask.json`, also gitignored:

```json
{"emails": ["@zooza.online"], "literals": {"+421 900 000 000": "+44 7700 900000"}}
```

## Step 1 — Pick the shots

Find what is stale and which article depends on it:

```bash
python3 - <<'PY'
import os,re,glob,datetime
from collections import defaultdict
use=defaultdict(list)
for f in glob.glob('content/**/*.md',recursive=True):
    t=open(f,encoding='utf-8',errors='ignore').read()
    for m in re.findall(r'\(\.\./\.\./assets/images/([^)\s]+)\)', t):
        use[f].append(m)
for f,imgs in sorted(use.items()):
    stale=[i for i in imgs if os.path.exists(f'assets/images/{i}')
           and datetime.datetime.fromtimestamp(os.path.getmtime(f'assets/images/{i}')).month<=3]
    if stale: print(f"{len(stale):3}  {f}")
PY
```

Start with `content/reference/` — those articles are "this is the screen", one
image to one route, no particular data needed. Leave for last anything that
needs a specific state to exist (an unresolved make-up credit, a half-finished
order). Those are slow, and doing them first is how a screenshot session turns
into an afternoon of hunting for a booking.

## Step 2 — Add them to the manifest

`scripts/screenshots/manifest.yml`, one entry per image. Keep the existing
filename: then nothing in `content/` has to move.

**The assertion is the important field.** It must name something that exists
only on that screen. The app is a single-page app behind hash routes, so a wrong
route renders "Page not found" with the entire navigation still on screen — and
a check for the page's own name passes, because the name is in the left-hand
menu of the error page. That happened on the first run; `#invoices` 404'd and
reported success.

## Step 3 — Capture and look

```bash
python3 scripts/screenshots/capture.py
```

Nothing is overwritten. Images land in `build/screenshots/` and the tool prints
a row per shot: `ok`, `BAD ROUTE`, `NOT FOUND`, `PII LEFT` or `ERROR`.

**Then open them.** Not to admire them — to check the screen shows what the
article claims. An automated run will happily produce a perfect photograph of an
empty list, a filtered view, or a company you did not mean.

## Step 4 — Read the article against the picture

**This is the step that pays for the whole exercise.** You now have a photograph of
what the screen really does, next to prose written months ago. Read one against the
other before touching anything else.

On 13 September a screenshot of the notification centre showed that the article's
table of notification types was wrong in **eleven rows out of fourteen** — *New
booking* had been documented as *New registration*, *Payment confirmation* as
*Online payment*, and *Class full notification*, the one people swear does not
exist, was sitting at the bottom of the list under a name nobody had written down.
The same batch moved a settings path from *Settings → General* to *Settings →
General → Access*, and replaced a checkbox that does not exist with the two toggles
that do.

None of that came from a spec, a ticket or a customer. It came from looking.

So for each recaptured screen:

- **Do the labels in the prose still match the labels on screen?** Button names,
  field names, menu paths, the names of options in a dropdown.
- **Is the navigation still right?** Menu groups get renamed and screens move.
- **Does the screen do something the article never mentions?** A new control, a
  new column, a banner. If it is worth a customer knowing, write it in — you are
  already here, and this is cheaper than finding out from a support ticket.
- **Does the article describe something that is gone?** Then the instructions are
  actively wrong, which is worse than out of date.

Fix the text in the same pass. An article whose prose contradicts its own fresh
screenshot is worse than one with an old picture, because now the reader can see
the contradiction.

## Step 5 — Apply, then finish the articles

```bash
python3 scripts/screenshots/capture.py --apply
```

For every article whose image changed:

| Field | What to do |
|---|---|
| alt text | Rewrite it to describe what is now on screen. The old alt text described the old picture. |
| `last_converted` | Today. The article did change — the picture is part of it. |
| body | Already handled in step 4 — but check it once more against the final image. |

Then `python3 scripts/seo_check.py` — it fails on generic alt text.

## Masking: literals only

The mask file holds literal strings, deliberately. Two attempts at pattern
matching both did damage on the first run:

- **Names.** "Two capitalised words" is not a person. It is also *Custom
  Holidays* and *Zooza Sitesx*, both of which were renamed to strangers in the
  middle of a screenshot of the settings menu.
- **Phone numbers.** A phone-shaped regex ate the dates. A class starting
  *16. 09. 2026* became a class starting *+44 7700 900000*.

A literal cannot hit anything it was not aimed at. If names need to disappear,
**change them in the demo account** rather than papering over them at capture
time — that fixes every future screenshot at once and cannot be got wrong.

For images that cannot be recaptured, `scripts/redact_pii.py` paints over PII in
an existing file. Prefer recapturing.

## Done definition
- Every shot in the batch is `ok`, or its manifest entry says why it is not
- Somebody has looked at each image and confirmed it shows the right screen
- Each article has been read against its new screenshot, and the labels, paths and
  options in the prose match what the picture shows
- Alt text and `last_converted` updated on every article touched
- `seo_check.py` passes
- The session file and the mask file are still outside version control

## Summary format

```
## Screenshots — 2026-09-13
- Captured: 2 of 3 (reference/cls-classes, reference/cls-sessions)
- Failed: reference/invoices-list — #invoices renders the app's 404, route unknown
- Articles updated: classes-list.md, sessions-list.md
- Corrections found by reading the prose against the picture: 0
- Still stale: 804
```
