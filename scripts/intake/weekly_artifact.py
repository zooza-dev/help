#!/usr/bin/env python3
"""Render the week's triaged conversations as a working review board.

Reads what triage.py already produced -- it does not re-fetch or re-classify.
Two hand-written sidecars are merged in by conversation id if present:

    build/intake/notes-<end>.json   Claude's read on each conversation
    build/intake/email-<end>.json   client email threads (Gmail needs a login)

The page it writes is a board, not a report. Every conversation carries a
decision (fine as answered / into the KB / dig into it / product), a category,
and a note back to Claude. Decisions are stored in the published artifact
itself, so the board keeps its state between sessions and between people.

Re-running this script starts from a clean board. To keep decisions already
made, pass the state you exported from the board:

    python3 scripts/intake/weekly_artifact.py --start 2026-08-22 --end 2026-08-29
    python3 scripts/intake/weekly_artifact.py --start ... --end ... --state board.json
"""
import argparse
import html
import json
import os
import re
from collections import Counter

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

ap = argparse.ArgumentParser()
ap.add_argument("--start", required=True)
ap.add_argument("--end", required=True)
ap.add_argument("--intake", default=os.path.join(REPO, "build", "intake"))
ap.add_argument("--state", default=None, help="board state exported from a previous board")
ap.add_argument("--out", default=None)
args = ap.parse_args()

OUT = args.out or os.path.join(REPO, "build", "reports", f"weekly-review-{args.end}.html")

rows = json.load(open(os.path.join(args.intake, "triage.json"), encoding="utf-8"))

notes_path = os.path.join(args.intake, f"notes-{args.end}.json")
notes = json.load(open(notes_path, encoding="utf-8")) if os.path.exists(notes_path) else {}

email_path = os.path.join(args.intake, f"email-{args.end}.json")
emails = json.load(open(email_path, encoding="utf-8")) if os.path.exists(email_path) else []

prior = json.load(open(args.state, encoding="utf-8")) if args.state else {}

# triage.py only assigns buckets to bot-only rows; human rows get their own label
for r in rows:
    if r["has_human"]:
        r["bucket"] = "HUMAN"

# The category list is deliberately about what a client is asking, not about
# which screen the answer lives on -- the point is to see which parts of the
# product generate questions week after week.
CATEGORIES = [
    ("programmes", "Programmes & classes"),
    ("pricing", "Pricing & payment setup"),
    ("payments", "Payments & invoicing"),
    ("bookings", "Bookings & registrations"),
    ("trials", "Trials"),
    ("makeups", "Make-ups & attendance"),
    ("clients", "Clients & profiles"),
    ("team", "Team, roles & availability"),
    ("widgets", "Widgets & website"),
    ("comms", "Email, SMS & templates"),
    ("reports", "Reports & exports"),
    ("ai", "AI connector & API"),
    ("account", "Account & settings"),
    ("noise", "Noise"),
]

# A decision closes a conversation. "Fine" and "Product" are closed states in
# their own right -- only "KB" and "Dig" leave work behind.
DECISIONS = [
    ("ok", "Fine as answered", "Nothing to do — the answer was right and general enough."),
    ("kb", "Into the KB", "Something to write or fix in the help centre."),
    ("dig", "Dig into it", "Cannot be answered without checking the product first."),
    ("product", "Product, not KB", "A defect or a missing feature — belongs in a ticket."),
]

# Claude's read maps onto a suggested decision; the reviewer confirms or overrides.
VERDICT_TO_DECISION = {
    "gap": "kb", "verify": "dig", "check": "dig",
    "product": "product", "client": "ok", "noise": "ok",
    # the decision names themselves are natural to write in a note, so accept them
    "kb": "kb", "dig": "dig", "ok": "ok",
}

SOURCE_RE = re.compile(r"\n\s*Sources:\s*\n(.*)$", re.S)


def split_sources(text):
    """Bot answers carry their citations appended as a Sources: block."""
    m = SOURCE_RE.search(text or "")
    if not m:
        return (text or "").strip(), []
    return text[: m.start()].strip(), [s.strip() for s in m.group(1).splitlines() if s.strip()]


def first_question(r):
    skip = ("human", "dobry den", "dobrý deň", "buna", "hello", "hi")
    for role, _, text in r["turns"]:
        if role == "customer":
            t = (text or "").strip()
            if len(t) > 3 and t.lower().rstrip(".!,") not in skip:
                return t
    for role, _, text in r["turns"]:
        if role == "customer" and (text or "").strip():
            return text.strip()
    return "(no client message)"


convs = []
for r in rows:
    n = notes.get(r["id"], {})
    convs.append({
        "channel": "intercom",
        "id": r["id"],
        "date": r["date"],
        "day": r["day"],
        "human": bool(r["has_human"]),
        "bucket": r.get("bucket") or "D_assumed_with_kb",
        "reask": r.get("cust_after_bot", 0),
        "resolution": r.get("resolution_state") or "—",
        "rating": r.get("rating"),
        "carried": r.get("carried_since"),
        "sources": r.get("sources") or [],
        "q": first_question(r),
        "turns": [dict(zip(("role", "who"), t[:2]), **dict(zip(("text", "cited"), split_sources(t[2]))))
                  for t in r["turns"]],
        "verdict": n.get("verdict", ""),
        "vtitle": n.get("title", ""),
        "vnote": n.get("note", ""),
        "cat": n.get("cat", "account"),
    })

for e in emails:
    convs.append({
        "channel": "email",
        "id": e["id"],
        "date": e["date"],
        "day": e["day"],
        "human": True,
        "bucket": "EMAIL",
        "reask": 0,
        "resolution": "—",
        "rating": None,
        "carried": None,
        "sources": [],
        "q": e.get("subject", ""),
        "turns": [{"role": t[0], "who": t[1], "text": t[2], "cited": []} for t in e["turns"]],
        "verdict": e.get("verdict", ""),
        "vtitle": e.get("vtitle", ""),
        "vnote": e.get("vnote", ""),
        "cat": notes.get(e["id"], {}).get("cat", e.get("cat", "account")),
        "from": e.get("who", ""),
    })

convs.sort(key=lambda c: c["date"], reverse=True)

# Opening board state: every conversation undecided, carrying Claude's suggestion
# and category. A prior export wins over both.
state = {}
for c in convs:
    p = prior.get(c["id"], {})
    state[c["id"]] = {
        "d": p.get("d", ""),
        "cat": p.get("cat", c["cat"]),
        "note": p.get("note", ""),
        "sug": VERDICT_TO_DECISION.get(c["verdict"], ""),
    }

cite = Counter()
for c in convs:
    if not c["human"]:
        for s in c["sources"]:
            cite[s] += 1

meta = {
    "start": args.start,
    "end": args.end,
    "categories": CATEGORIES,
    "decisions": DECISIONS,
    "topCited": cite.most_common(8),
    "counts": {
        "total": len(convs),
        "human": sum(1 for c in convs if c["human"] and c["channel"] == "intercom"),
        "bot": sum(1 for c in convs if not c["human"]),
        "email": sum(1 for c in convs if c["channel"] == "email"),
    },
}


def js(obj):
    """Embed as JS source: JSON with the characters that can break out escaped."""
    return (json.dumps(obj, ensure_ascii=False)
            .replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029"))

CSS = """
:root{
  --ground:#ffffff; --surface:#f7f8f2; --surface-2:#eef2f5; --raise:#ffffff;
  --line:#dde3e1; --line-soft:#ebefed;
  --ink:#414141; --ink-deep:#1a222b; --muted:#6f7d7b; --faint:#9aa7a4;
  --teal:#0e7972; --teal-soft:#e2efee;
  --brand:#fa6900; --brand-dark:#e35f00;
  --ok:#3f6212; --ok-soft:#eef4e4;
  --kb:#0e7972; --kb-soft:#e2efee;
  --dig:#8a5200; --dig-soft:#fff2df;
  --prod:#6f7d7b; --prod-soft:#eef2f5;
  --critical:#a20000; --critical-soft:#f7e6e6;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --ground:#12171a; --surface:#181f22; --surface-2:#1f282c; --raise:#171e21;
    --line:#2c383d; --line-soft:#222b2f;
    --ink:#ccd5d3; --ink-deep:#f2f6f4; --muted:#8b9997; --faint:#6b7876;
    --teal:#4fb6ae; --teal-soft:#12302e;
    --brand:#ff8434; --brand-dark:#ff9a56;
    --ok:#a3c266; --ok-soft:#1e2718;
    --kb:#4fb6ae; --kb-soft:#12302e;
    --dig:#e3ac63; --dig-soft:#2e2417;
    --prod:#8b9997; --prod-soft:#1f282c;
    --critical:#ff7b72; --critical-soft:#33201f;
  }
}
:root[data-theme="dark"]{
  --ground:#12171a; --surface:#181f22; --surface-2:#1f282c; --raise:#171e21;
  --line:#2c383d; --line-soft:#222b2f;
  --ink:#ccd5d3; --ink-deep:#f2f6f4; --muted:#8b9997; --faint:#6b7876;
  --teal:#4fb6ae; --teal-soft:#12302e;
  --brand:#ff8434; --brand-dark:#ff9a56;
  --ok:#a3c266; --ok-soft:#1e2718;
  --kb:#4fb6ae; --kb-soft:#12302e;
  --dig:#e3ac63; --dig-soft:#2e2417;
  --prod:#8b9997; --prod-soft:#1f282c;
  --critical:#ff7b72; --critical-soft:#33201f;
}

*{box-sizing:border-box}
body{
  margin:0; background:var(--ground); color:var(--ink);
  font-family:ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  font-size:13.5px; line-height:1.45; -webkit-font-smoothing:antialiased;
}
.mono{font-family:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace;font-variant-numeric:tabular-nums}
button{font:inherit;cursor:pointer;color:inherit}
:focus-visible{outline:2px solid var(--brand);outline-offset:1px;border-radius:3px}

/* ══ command bar ══ */
.bar{position:sticky;top:0;z-index:30;background:var(--surface);border-bottom:1px solid var(--line)}
.bar-in{max-width:1240px;margin:0 auto;padding:9px 20px;display:flex;flex-direction:column;gap:8px}
.bar-top{display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.wk{display:flex;flex-direction:column;line-height:1.15;margin-right:auto}
.wk b{font-size:13px;color:var(--ink-deep);font-weight:700}
.wk span{font-size:11px;color:var(--muted)}
.done{font-size:12px;color:var(--muted);white-space:nowrap}
.done b{color:var(--ink-deep);font-size:14px}
.seg{display:flex;height:5px;border-radius:3px;overflow:hidden;background:var(--surface-2);
     border:1px solid var(--line);flex:1;min-width:120px;max-width:300px}
.seg i{display:block;height:100%}
.seg i.ok{background:var(--ok)} .seg i.kb{background:var(--kb)}
.seg i.dig{background:var(--dig)} .seg i.product{background:var(--prod)}
.btn{font-size:12px;padding:5px 11px;border-radius:6px;border:1px solid var(--line);background:var(--raise)}
.btn:hover{border-color:var(--muted)}
.btn.primary{background:var(--brand);border-color:var(--brand);color:#fff}
.btn.primary:hover{background:var(--brand-dark);border-color:var(--brand-dark)}
.save{font-size:11px;color:var(--muted);white-space:nowrap}
.save.on{color:var(--teal)} .save.err{color:var(--critical)}

.bar-bot{display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.chip{font-size:11.5px;padding:3px 9px;border-radius:999px;border:1px solid var(--line);
      background:transparent;display:inline-flex;gap:5px;align-items:center;white-space:nowrap}
.chip:hover{border-color:var(--muted)}
.chip b{font-weight:600;color:var(--muted);font-variant-numeric:tabular-nums}
.chip[aria-pressed="true"]{background:var(--ink-deep);border-color:var(--ink-deep);color:var(--ground)}
.chip[aria-pressed="true"] b{color:var(--ground);opacity:.75}
.chip.k-ok[aria-pressed="true"]{background:var(--ok);border-color:var(--ok);color:#fff}
.chip.k-kb[aria-pressed="true"]{background:var(--kb);border-color:var(--kb);color:#fff}
.chip.k-dig[aria-pressed="true"]{background:var(--dig);border-color:var(--dig);color:#fff}
.chip.k-wait[aria-pressed="true"]{background:var(--critical);border-color:var(--critical);color:#fff}
.srch{margin-left:auto;font:inherit;font-size:12px;padding:4px 9px;border:1px solid var(--line);
      border-radius:6px;background:var(--raise);color:var(--ink);width:190px}
.srch::placeholder{color:var(--faint)}
.sel{font:inherit;font-size:12px;padding:4px 7px;border:1px solid var(--line);border-radius:6px;
     background:var(--raise);color:var(--ink)}

/* ══ list ══ */
.wrap{max-width:1240px;margin:0 auto;padding:0 20px 60px}
.day{display:flex;align-items:center;gap:9px;padding:14px 2px 5px;font-size:10.5px;
     letter-spacing:.1em;text-transform:uppercase;color:var(--faint);font-weight:600}
.day::after{content:"";flex:1;height:1px;background:var(--line-soft)}

.row{display:block;width:100%;text-align:left;background:var(--raise);border:0;
     border-bottom:1px solid var(--line-soft);border-left:3px solid transparent;padding:0}
.row:hover{background:var(--surface)}
.row.cursor{background:var(--surface-2)}
.row.d-ok{border-left-color:var(--ok)} .row.d-kb{border-left-color:var(--kb)}
.row.d-dig{border-left-color:var(--dig)} .row.d-product{border-left-color:var(--prod)}
.row.decided .ttl{color:var(--muted)}
.line{display:grid;grid-template-columns:auto 46px 1fr auto auto;align-items:center;
      gap:10px;padding:7px 10px;min-height:38px}
.dot{width:7px;height:7px;border-radius:50%;flex:none}
.dot.h{background:var(--teal)} .dot.b{border:1.5px solid var(--faint)}
.tm{font-size:11px;color:var(--faint);text-align:right}
.ttl{color:var(--ink-deep);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;min-width:0}
.meta{display:flex;gap:5px;align-items:center;flex-wrap:nowrap}
.pill{font-size:10px;padding:1px 6px;border-radius:4px;border:1px solid var(--line);
      color:var(--muted);white-space:nowrap}
.pill.cat{background:var(--surface-2)}
.pill.wait{color:var(--critical);border-color:var(--critical);background:var(--critical-soft);font-weight:600}
.pill.re{color:var(--dig);border-color:var(--dig);background:var(--dig-soft)}
.pill.note{color:#fff;background:var(--brand);border-color:var(--brand)}
.pill.sug{border-style:dashed;color:var(--faint)}

.acts{display:flex;gap:3px}
.act{font-size:10.5px;font-weight:600;letter-spacing:.02em;padding:3px 8px;border-radius:5px;
     border:1px solid var(--line);background:var(--raise);color:var(--muted);line-height:1.5}
.act:hover{border-color:var(--muted);color:var(--ink-deep)}
.act[aria-pressed="true"]{color:#fff;border-color:transparent}
.act.a-ok[aria-pressed="true"]{background:var(--ok)}
.act.a-kb[aria-pressed="true"]{background:var(--kb)}
.act.a-dig[aria-pressed="true"]{background:var(--dig)}
.act.a-product[aria-pressed="true"]{background:var(--prod)}

/* ══ expanded ══ */
.open{border-left-width:3px;background:var(--surface)}
.panel{padding:2px 10px 16px 30px;display:flex;flex-direction:column;gap:12px}
.read{border-left:2px solid var(--kb);background:var(--raise);padding:9px 13px;border-radius:0 6px 6px 0}
.read .k{font-size:10px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);font-weight:600}
.read p{margin:3px 0 0}
.frm{display:flex;gap:10px;align-items:flex-start;flex-wrap:wrap}
.note{flex:1;min-width:240px;font:inherit;font-size:12.5px;padding:7px 9px;border:1px solid var(--line);
      border-radius:6px;background:var(--raise);color:var(--ink);resize:vertical;min-height:52px}
.note::placeholder{color:var(--faint)}
.idc{font-size:11px;border:1px solid var(--line);background:var(--raise);border-radius:5px;padding:2px 7px}
.idc:hover{border-color:var(--brand);color:var(--brand)}
.thread{display:flex;flex-direction:column;gap:8px;max-height:min(60vh,620px);overflow-y:auto;
        padding-right:4px}
.turn{display:grid;grid-template-columns:64px 1fr;gap:10px;align-items:start}
.turn .who{font-size:10px;letter-spacing:.04em;text-transform:uppercase;font-weight:600;
           color:var(--faint);padding-top:5px;text-align:right;overflow-wrap:anywhere}
.turn.t-customer .who{color:var(--ink-deep)} .turn.t-human .who{color:var(--teal)}
.bub{font-family:Georgia,"Iowan Old Style",serif;font-size:13.5px;line-height:1.55;white-space:pre-wrap;
     overflow-wrap:anywhere;padding:7px 11px;border-radius:6px;background:var(--raise);
     border:1px solid var(--line-soft)}
.turn.t-customer .bub{background:var(--surface-2);border-color:var(--line)}
.turn.t-human .bub{background:var(--teal-soft);border-color:var(--teal)}
.cited{margin-top:6px;font-family:ui-sans-serif,system-ui,sans-serif;font-size:10.5px;color:var(--muted);
       border-top:1px dashed var(--line);padding-top:5px}
.cited b{display:block;font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:2px}
.cited .m{color:var(--critical)}

.empty{padding:40px 10px;text-align:center;color:var(--muted)}
.foot{max-width:1240px;margin:0 auto;padding:4px 20px 40px;display:flex;gap:26px;flex-wrap:wrap;
      font-size:11.5px;color:var(--faint)}
.foot kbd{font-family:ui-monospace,Menlo,monospace;font-size:10.5px;border:1px solid var(--line);
          border-bottom-width:2px;border-radius:4px;padding:0 4px;color:var(--muted);background:var(--raise)}

details.roll{border-top:1px solid var(--line-soft)}
details.roll summary{cursor:pointer;font-size:11px;letter-spacing:.08em;text-transform:uppercase;
                     color:var(--muted);font-weight:600;padding:11px 2px;list-style:none}
details.roll summary::-webkit-details-marker{display:none}
details.roll summary::before{content:"▸ ";color:var(--faint)}
details.roll[open] summary::before{content:"▾ "}
table.rt{width:100%;border-collapse:collapse;font-size:12px;margin-bottom:14px}
table.rt th{text-align:right;font-weight:600;color:var(--faint);font-size:10px;text-transform:uppercase;
            letter-spacing:.06em;padding:0 6px 4px 0}
table.rt th:first-child{text-align:left}
table.rt td{padding:3px 6px 3px 0;border-top:1px solid var(--line-soft);text-align:right;
            font-variant-numeric:tabular-nums}
table.rt td:first-child{text-align:left;color:var(--ink-deep)}
table.rt td.z{color:var(--line)}
.rt button{background:none;border:0;padding:0;font:inherit;text-align:left}
.rt button:hover{color:var(--brand);text-decoration:underline}

dialog{border:1px solid var(--line);border-radius:10px;background:var(--raise);color:var(--ink);
       padding:0;max-width:min(760px,92vw);width:100%}
dialog::backdrop{background:rgba(26,34,43,.5)}
.dlg{padding:16px 18px;display:flex;flex-direction:column;gap:10px}
.dlg h2{margin:0;font-size:15px;color:var(--ink-deep)}
.dlg p{margin:0;font-size:12px;color:var(--muted)}
.dlg textarea{width:100%;height:320px;font-family:ui-monospace,Menlo,monospace;font-size:11.5px;
              line-height:1.5;padding:10px;border:1px solid var(--line);border-radius:6px;
              background:var(--surface);color:var(--ink);resize:vertical}
.dlg .rw{display:flex;gap:8px;justify-content:flex-end}

@media (max-width:820px){
  .line{grid-template-columns:auto 1fr;grid-template-areas:"d t" "m m" "a a";gap:5px 9px}
  .tm{display:none}
  .meta{grid-area:m;flex-wrap:wrap} .acts{grid-area:a}
  .ttl{white-space:normal}
  .srch{width:100%;margin-left:0;order:99}
  .panel{padding-left:12px}
  .turn{grid-template-columns:1fr;gap:2px}
  .turn .who{text-align:left}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
"""

SKELETON = """
<header class="bar"><div class="bar-in">
  <div class="bar-top">
    <div class="wk"><b id="wkname">Help desk triage</b><span id="wkrange"></span></div>
    <div class="seg" id="seg" title="How the week has been decided"></div>
    <div class="done" id="done"></div>
    <span class="save" id="save"></span>
    <button class="btn" id="next">Next undecided</button>
    <button class="btn primary" id="hand">Hand to Claude</button>
  </div>
  <div class="bar-bot">
    <div class="chips" id="chips" style="display:flex;gap:6px;flex-wrap:wrap"></div>
    <select class="sel" id="catf" aria-label="Filter by category"></select>
    <input class="srch" id="q" type="search" placeholder="Search transcripts" aria-label="Search">
  </div>
</div></header>

<main class="wrap"><div id="list"></div></main>

<div class="wrap"><details class="roll"><summary>Where the questions came from</summary>
  <div id="roll"></div>
</details></div>

<div class="foot">
  <span><kbd>j</kbd> <kbd>k</kbd> move</span>
  <span><kbd>1</kbd>–<kbd>4</kbd> decide</span>
  <span><kbd>Enter</kbd> open</span>
  <span><kbd>n</kbd> next undecided</span>
  <span><kbd>/</kbd> search</span>
</div>

<dialog id="hdlg"><div class="dlg">
  <h2>Hand this back to Claude</h2>
  <p>Everything decided, with your notes. Copy it into the chat.</p>
  <textarea id="hout" readonly></textarea>
  <div class="rw"><button class="btn" id="hclose">Close</button>
  <button class="btn primary" id="hcopy">Copy</button></div>
</div></dialog>
"""

APP = r"""
const el = s => document.querySelector(s);
const esc = s => (s||'').replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const MARKETING = /— Zooza$|Zooza PRO|Cen[íi]k|Cennik/;
const CATLBL = Object.fromEntries(META.categories);
const DECS = META.decisions.map(d => d[0]);
const SHORT = {ok:'Fine', kb:'KB', dig:'Dig', product:'Product'};

let filter='todo', catf='', q='', open=null, cursor=0, readOnly=false;

const S = c => (c && c.id ? (STATE[c.id] ||= {d:'', cat:c.cat, note:'', sug:''})
                          : {d:'', cat:'', note:'', sug:''});
const byId = id => DATA.find(c => c.id === id);

const FILTERS = [
  ['todo',   'To decide', '',        c => !S(c).d],
  ['all',    'All',       '',        c => true],
  ['kb',     'KB',        'k-kb',    c => S(c).d === 'kb'],
  ['dig',    'Dig',       'k-dig',   c => S(c).d === 'dig'],
  ['ok',     'Fine',      'k-ok',    c => S(c).d === 'ok'],
  ['waiting','Still waiting','k-wait',c => !!c.carried],
  ['noted',  'My notes',  '',        c => !!S(c).note],
  ['human',  'Human',     '',        c => c.human && c.channel === 'intercom'],
  ['bot',    'AI only',   '',        c => !c.human],
];

/* ── saving ───────────────────────────────────────────── */
let timer=null, artifact=null, dirty=false;
const mirror = () => { try{ localStorage.setItem('zb-'+META.end, JSON.stringify(STATE)); }catch(e){} };
const setSave = (t,c) => { const s=el('#save'); s.textContent=t; s.className='save '+(c||''); };
function touch(){ dirty=true; mirror(); setSave('Unsaved…'); clearTimeout(timer); timer=setTimeout(commit,2500); }

function buildDoc(){
  const css=document.getElementById('sheet').textContent;
  const skel=document.getElementById('skeleton').innerHTML;
  const app=document.getElementById('app').textContent;
  const enc=o=>JSON.stringify(o).replace(/</g,'\\u003c')
    .replace(/\u2028/g,'\\u2028').replace(/\u2029/g,'\\u2029');
  const S_='<'+'script', E_='<'+'/script>';
  return '<!doctype html><html lang="en"><head><meta charset="utf-8">'
    +'<meta name="viewport" content="width=device-width,initial-scale=1">'
    +'<title>'+esc(document.title)+'</title><style id="sheet">'+css+'</style></head><body>'
    +skel+'<template id="skeleton">'+skel+'</template>'
    +S_+' id="data">const DATA='+enc(DATA)+';const META='+enc(META)+';'+E_
    +S_+' id="state">const STATE='+enc(STATE)+';'+E_
    +S_+' id="app">'+app+E_+'</body></html>';
}
async function commit(){
  if(!dirty||readOnly) return;
  if(!artifact){ setSave('Saved on this device'); dirty=false; return; }
  setSave('Saving…');
  try{
    sessionStorage.setItem('zb-open', open||''); sessionStorage.setItem('zb-filter', filter);
    await artifact.publish(buildDoc()); dirty=false; setSave('Saved','on');
  }catch(e){
    const c=e&&e.code;
    if(c==='conflict') return;
    if(c==='rate_limited'){ timer=setTimeout(commit,8000); setSave('Queued…'); return; }
    if(['not_writer','not_granted','not_declared','capability_disabled','capability_removed'].includes(c)){
      readOnly=true; setSave('Read-only view','err'); return; }
    setSave('Saved on this device only','err');
  }
}

/* ── rendering ────────────────────────────────────────── */
function matches(c){
  if(!FILTERS.find(f=>f[0]===filter)[3](c)) return false;
  if(catf && S(c).cat!==catf) return false;
  if(!q) return true;
  return (c.q+' '+c.vtitle+' '+c.vnote+' '+c.id+' '+S(c).note+' '+
          c.turns.map(t=>t.text).join(' ')).toLowerCase().includes(q);
}
const visible = () => DATA.filter(matches);

function renderBar(){
  const n=DATA.length, by={ok:0,kb:0,dig:0,product:0};
  DATA.forEach(c=>{ const d=S(c).d; if(d) by[d]=(by[d]||0)+1; });
  const done=by.ok+by.kb+by.dig+by.product;
  el('#seg').innerHTML=DECS.map(k=>by[k]?'<i class="'+k+'" style="width:'+(by[k]/n*100)+'%" title="'+SHORT[k]+' '+by[k]+'"></i>':'').join('');
  el('#done').innerHTML='<b>'+done+'</b> / '+n+' decided';
  el('#chips').innerHTML=FILTERS.map(([k,label,cls,fn])=>
    '<button class="chip '+cls+'" data-f="'+k+'" aria-pressed="'+(filter===k)+'">'+
    label+' <b>'+DATA.filter(fn).length+'</b></button>').join('');
}

function rowHTML(c){
  const s=S(c), out=[];
  out.push('<span class="pill cat">'+esc(CATLBL[s.cat]||s.cat)+'</span>');
  if(c.carried) out.push('<span class="pill wait">waiting since '+c.carried+'</span>');
  if(c.reask>=4) out.push('<span class="pill re">'+c.reask+'× re-asked</span>');
  if(s.note) out.push('<span class="pill note">note</span>');
  if(!s.d&&s.sug) out.push('<span class="pill sug">'+SHORT[s.sug]+'?</span>');
  return '<div class="line">'
    +'<span class="dot '+(c.human?'h':'b')+'" title="'+(c.human?'A human replied':'AI only')+'"></span>'
    +'<span class="tm mono">'+c.date.slice(11)+'</span>'
    +'<span class="ttl">'+esc(c.vtitle||c.q)+'</span>'
    +'<span class="meta">'+out.join('')+'</span>'
    +'<span class="acts">'+DECS.map(k=>
        '<button class="act a-'+k+'" data-d="'+k+'" data-id="'+c.id+'" aria-pressed="'+(s.d===k)+'"'
        +' title="'+SHORT[k]+'">'+SHORT[k]+'</button>').join('')+'</span>'
    +'</div>';
}

function panelHTML(c){
  const s=S(c);
  let h='<div class="panel">';
  if(c.verdict) h+='<div class="read"><div class="k">Claude reads this as: '+esc(c.verdict)+'</div><p>'+esc(c.vnote)+'</p></div>';
  h+='<div class="frm">'
    +'<button class="idc mono" data-copy="'+c.id+'">'+c.id+'</button>'
    +'<select class="sel" data-cat="'+c.id+'">'+META.categories.map(([k,l])=>
        '<option value="'+k+'"'+(s.cat===k?' selected':'')+'>'+esc(l)+'</option>').join('')+'</select>'
    +'<textarea class="note" data-note="'+c.id+'" placeholder="What you want done with this one. Screenshots go in the chat — quote the id.">'+esc(s.note)+'</textarea>'
    +'</div><div class="thread">';
  for(const t of c.turns){
    if(!t.text&&!t.cited.length) continue;
    const r=t.role==='customer'?'customer':(t.role==='human'?'human':'bot');
    const w=r==='customer'?esc(t.who||'Client'):r==='human'?esc(t.who||'Zooza'):'AI';
    h+='<div class="turn t-'+r+'"><div class="who">'+w+'</div><div class="bub">'+esc(t.text);
    if(t.cited.length) h+='<div class="cited"><b>Cited</b>'+t.cited.map(x=>
      '<div class="'+(MARKETING.test(x)?'m':'')+'">'+esc(x)+'</div>').join('')+'</div>';
    h+='</div></div>';
  }
  return h+'</div></div>';
}

function renderList(){
  const rows=visible();
  if(cursor>=rows.length) cursor=Math.max(0,rows.length-1);
  if(!rows.length){ el('#list').innerHTML='<p class="empty">Nothing matches that.</p>'; return; }
  let h='', day='';
  rows.forEach((c,i)=>{
    if(c.day!==day){ day=c.day;
      h+='<div class="day">'+new Date(day+'T12:00:00').toLocaleDateString('en-GB',
         {weekday:'long',day:'numeric',month:'long'})+'</div>'; }
    const s=S(c), isOpen=open===c.id;
    h+='<div class="row'+(s.d?' decided d-'+s.d:'')+(isOpen?' open':'')+(i===cursor?' cursor':'')
      +'" data-id="'+c.id+'" data-i="'+i+'">'+rowHTML(c)+(isOpen?panelHTML(c):'')+'</div>';
  });
  el('#list').innerHTML=h;
}

function renderRoll(){
  const keys=META.categories.map(x=>x[0]), agg={};
  keys.forEach(k=>agg[k]={n:0,kb:0,dig:0,ok:0,product:0,todo:0});
  DATA.forEach(c=>{ const s=S(c), a=agg[s.cat]||(agg[s.cat]={n:0,kb:0,dig:0,ok:0,product:0,todo:0});
    a.n++; if(s.d) a[s.d]++; else a.todo++; });
  const rows=keys.filter(k=>agg[k].n).sort((a,b)=>agg[b].n-agg[a].n);
  const cell=v=>v?String(v):'<span class="z">·</span>';
  let h='<table class="rt"><thead><tr><th>Category</th><th>All</th><th>KB</th><th>Dig</th><th>Fine</th><th>Left</th></tr></thead><tbody>';
  rows.forEach(k=>{const a=agg[k];
    h+='<tr><td><button data-cat-filter="'+k+'">'+esc(CATLBL[k]||k)+'</button></td><td>'+a.n+'</td><td>'
      +cell(a.kb)+'</td><td>'+cell(a.dig)+'</td><td>'+cell(a.ok)+'</td><td>'+cell(a.todo)+'</td></tr>';});
  el('#roll').innerHTML=h+'</tbody></table>';
}

const render=()=>{ renderBar(); renderList(); renderRoll(); };

function scrollCursor(){
  const r=el('.row.cursor'); if(!r) return;
  const top=r.getBoundingClientRect().top, h=el('.bar').offsetHeight;
  if(top<h+8||top>window.innerHeight-60) r.scrollIntoView({block:'center'});
}

/* ── acting ───────────────────────────────────────────── */
function decide(id,d){
  const s=S(byId(id)); s.d = s.d===d ? '' : d; touch(); render();
}
function toggle(id){ open = open===id ? null : id; renderList();
  if(open){ const r=el('.row.open'); if(r) r.scrollIntoView({block:'nearest'}); } }

el('#chips').addEventListener('click',e=>{const b=e.target.closest('.chip'); if(!b) return;
  filter=b.dataset.f; cursor=0; render(); window.scrollTo({top:0});});
el('#catf').addEventListener('change',e=>{catf=e.target.value; cursor=0; render();});
el('#q').addEventListener('input',e=>{q=e.target.value.trim().toLowerCase(); cursor=0; render();});
el('#roll').addEventListener('click',e=>{const b=e.target.closest('[data-cat-filter]'); if(!b) return;
  catf=b.dataset.catFilter; el('#catf').value=catf; filter='all'; render(); window.scrollTo({top:0});});

el('#list').addEventListener('click',e=>{
  const a=e.target.closest('.act'); if(a){ e.stopPropagation(); decide(a.dataset.id,a.dataset.d); return; }
  const cp=e.target.closest('[data-copy]'); if(cp){ e.stopPropagation();
    navigator.clipboard?.writeText(cp.dataset.copy);
    const t=cp.textContent; cp.textContent='copied'; setTimeout(()=>{cp.textContent=t;},900); return; }
  if(e.target.closest('.note')||e.target.closest('.sel')) return;
  const r=e.target.closest('.row'); if(!r) return;
  cursor=+r.dataset.i; toggle(r.dataset.id);
});
el('#list').addEventListener('input',e=>{
  const n=e.target.closest('[data-note]'); if(n){ S(byId(n.dataset.note)).note=n.value; touch(); }});
el('#list').addEventListener('change',e=>{
  const c=e.target.closest('[data-cat]'); if(c){ S(byId(c.dataset.cat)).cat=c.value; touch(); renderBar(); renderRoll(); }
  const n=e.target.closest('[data-note]'); if(n) renderList();});

function nextUndecided(){
  const rows=visible();
  for(let i=1;i<=rows.length;i++){ const j=(cursor+i)%rows.length;
    if(!S(rows[j]).d){ cursor=j; open=rows[j].id; renderList(); scrollCursor(); return; } }
  setSave('All decided','on');
}
el('#next').addEventListener('click',nextUndecided);

document.addEventListener('keydown',e=>{
  if(e.metaKey||e.ctrlKey||e.altKey) return;
  const t=e.target.tagName;
  if(t==='INPUT'||t==='TEXTAREA'||t==='SELECT'){ if(e.key==='Escape') e.target.blur(); return; }
  const rows=visible(); if(!rows.length) return;
  if(e.key==='j'||e.key==='ArrowDown'){ e.preventDefault(); cursor=Math.min(cursor+1,rows.length-1); renderList(); scrollCursor(); }
  else if(e.key==='k'||e.key==='ArrowUp'){ e.preventDefault(); cursor=Math.max(cursor-1,0); renderList(); scrollCursor(); }
  else if(e.key==='Enter'){ e.preventDefault(); toggle(rows[cursor].id); }
  else if(e.key==='Escape'&&open){ open=null; renderList(); }
  else if(e.key==='n'){ e.preventDefault(); nextUndecided(); }
  else if(e.key==='/'){ e.preventDefault(); el('#q').focus(); }
  else if('1234'.includes(e.key)){ e.preventDefault(); decide(rows[cursor].id,DECS[+e.key-1]); scrollCursor(); }
});

/* ── handoff ──────────────────────────────────────────── */
el('#hand').addEventListener('click',()=>{
  const head={kb:'Into the KB',dig:'Dig into it first',product:'Product, not KB',ok:'Fine as answered'};
  let out='# Weekly review — '+META.start+' to '+META.end+'\n';
  const left=DATA.filter(c=>!S(c).d).length;
  out+='\n'+(DATA.length-left)+' of '+DATA.length+' decided'+(left?', '+left+' still open':'')+'.\n';
  ['kb','dig','product','ok'].forEach(d=>{
    const rows=DATA.filter(c=>S(c).d===d); if(!rows.length) return;
    out+='\n## '+head[d]+' ('+rows.length+')\n\n';
    rows.forEach(c=>{ const s=S(c);
      if(d==='ok'&&!s.note){ out+='- '+c.id+' — '+(c.vtitle||c.q.slice(0,70))+'\n'; return; }
      out+='- **'+c.id+'** ['+(CATLBL[s.cat]||s.cat)+'] '+(c.vtitle||c.q.slice(0,90))+'\n';
      if(c.carried) out+='  - unanswered since '+c.carried+'\n';
      if(s.note) out+='  - Michal: '+s.note.replace(/\n+/g,' ')+'\n'; });
  });
  const un=DATA.filter(c=>!S(c).d);
  if(un.length){ out+='\n## Not decided yet ('+un.length+')\n\n';
    un.forEach(c=>{ out+='- '+c.id+' — '+(c.vtitle||c.q.slice(0,70))+'\n'; }); }
  el('#hout').value=out; el('#hdlg').showModal();
});
el('#hclose').addEventListener('click',()=>el('#hdlg').close());
el('#hcopy').addEventListener('click',async()=>{
  const t=el('#hout'); t.select();
  try{ await navigator.clipboard.writeText(t.value); }catch(e){ document.execCommand('copy'); }
  el('#hcopy').textContent='Copied'; setTimeout(()=>{el('#hcopy').textContent='Copy';},1200);
});
window.addEventListener('beforeunload',e=>{ if(dirty){ commit(); e.preventDefault(); e.returnValue=''; }});

/* ── boot ─────────────────────────────────────────────── */
el('#wkrange').textContent=META.start+' – '+META.end+' · '+META.counts.total+' conversations';
el('#catf').innerHTML='<option value="">Every category</option>'+
  META.categories.map(([k,l])=>'<option value="'+k+'">'+esc(l)+'</option>').join('');
open=sessionStorage.getItem('zb-open')||null;
filter=sessionStorage.getItem('zb-filter')||'todo';
sessionStorage.removeItem('zb-open'); sessionStorage.removeItem('zb-filter');
setSave('');
render();
if(typeof claude!=='undefined'&&claude&&typeof claude.use==='function'){
  claude.use('artifact').then(a=>{ artifact=a;
    setSave(a?'Saving is on':'Saved on this device', a?'on':''); })
    .catch(()=>setSave('Saved on this device'));
} else setSave('Saved on this device');
"""
TITLE = f"Help desk triage — {args.start} to {args.end}"

doc = (
    f'<title>{html.escape(TITLE)}</title>\n'
    f'<style id="sheet">{CSS}</style>\n'
    f'{SKELETON}\n'
    f'<template id="skeleton">{SKELETON}</template>\n'
    f'<script id="data">const DATA={js(convs)};const META={js(meta)};</script>\n'
    f'<script id="state">const STATE={js(state)};</script>\n'
    f'<script id="app">{APP}</script>\n'
)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(doc)

sug = Counter(v["sug"] for v in state.values() if v["sug"])
print(f"Wrote {OUT} ({os.path.getsize(OUT)/1024:.0f} KB)")
print("  " + " | ".join(f"{k} {v}" for k, v in meta["counts"].items()))
print("  suggested: " + " | ".join(f"{k} {n}" for k, n in sug.most_common()))
