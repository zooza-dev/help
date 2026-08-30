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
  --line:#dfe4e2; --line-soft:#ebefed;
  --ink:#414141; --ink-deep:#1a222b; --muted:#6f7d7b;
  --teal:#0e7972; --teal-soft:#e2efee;
  --brand:#fa6900; --brand-dark:#e35f00;
  --critical:#a20000; --critical-soft:#f7e6e6;
  --warn:#8a5200; --warn-soft:#fff2df;
  --ok:#3f6212; --ok-soft:#eef4e4;
  --shadow:0 1px 2px rgba(26,34,43,.06), 0 8px 24px -16px rgba(26,34,43,.28);
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --ground:#12171a; --surface:#181f22; --surface-2:#1f282c; --raise:#1b2327;
    --line:#2c383d; --line-soft:#232d31;
    --ink:#ccd5d3; --ink-deep:#f2f6f4; --muted:#8b9997;
    --teal:#4fb6ae; --teal-soft:#12302e;
    --brand:#ff8434; --brand-dark:#ff9a56;
    --critical:#ff7b72; --critical-soft:#33201f;
    --warn:#e3ac63; --warn-soft:#2e2417;
    --ok:#a3c266; --ok-soft:#1e2718;
    --shadow:0 1px 2px rgba(0,0,0,.4), 0 8px 24px -16px rgba(0,0,0,.8);
  }
}
:root[data-theme="dark"]{
  --ground:#12171a; --surface:#181f22; --surface-2:#1f282c; --raise:#1b2327;
  --line:#2c383d; --line-soft:#232d31;
  --ink:#ccd5d3; --ink-deep:#f2f6f4; --muted:#8b9997;
  --teal:#4fb6ae; --teal-soft:#12302e;
  --brand:#ff8434; --brand-dark:#ff9a56;
  --critical:#ff7b72; --critical-soft:#33201f;
  --warn:#e3ac63; --warn-soft:#2e2417;
  --ok:#a3c266; --ok-soft:#1e2718;
  --shadow:0 1px 2px rgba(0,0,0,.4), 0 8px 24px -16px rgba(0,0,0,.8);
}

*{box-sizing:border-box}
body{
  margin:0; background:var(--ground); color:var(--ink);
  font-family:ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  font-size:15px; line-height:1.55; -webkit-font-smoothing:antialiased;
}
.mono{font-family:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace;font-variant-numeric:tabular-nums}
button{font:inherit;cursor:pointer}
:focus-visible{outline:2px solid var(--brand);outline-offset:2px}

/* ---------- masthead ---------- */
.mast{border-bottom:1px solid var(--line); background:var(--surface);position:sticky;top:0;z-index:20}
.mast-in{max-width:1640px;margin:0 auto;padding:14px 24px;display:flex;align-items:center;gap:22px;flex-wrap:wrap}
.brandblock{display:flex;flex-direction:column;gap:1px;margin-right:auto}
.eyebrow{font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--teal);font-weight:600}
.mast h1{margin:0;font-size:17px;line-height:1.2;color:var(--ink-deep);font-weight:700}
.mast h1 .rng{color:var(--muted);font-weight:400;font-size:14px}
.prog{display:flex;align-items:center;gap:10px;min-width:230px}
.bar{flex:1;height:7px;border-radius:4px;background:var(--surface-2);overflow:hidden;border:1px solid var(--line)}
.bar span{display:block;height:100%;background:var(--teal);transition:width .25s}
.prog .lbl{font-size:12px;color:var(--muted);white-space:nowrap}
.prog .lbl b{color:var(--ink-deep)}
.act{display:flex;gap:8px;align-items:center}
.btn{font-size:12.5px;padding:6px 12px;border-radius:7px;border:1px solid var(--line);background:var(--raise);color:var(--ink)}
.btn:hover{border-color:var(--muted)}
.btn.primary{background:var(--brand);border-color:var(--brand);color:#fff}
.btn.primary:hover{background:var(--brand-dark);border-color:var(--brand-dark)}
.save{font-size:11.5px;color:var(--muted);min-width:96px;text-align:right}
.save.on{color:var(--teal)}
.save.err{color:var(--critical)}

/* ---------- shell ---------- */
.shell{max-width:1640px;margin:0 auto;padding:18px 24px 40px;display:grid;grid-template-columns:minmax(320px,380px) 1fr;gap:18px;align-items:start}
.pane{background:var(--raise);border:1px solid var(--line);border-radius:10px;box-shadow:var(--shadow)}

/* ---------- filters ---------- */
.filters{padding:11px 12px;border-bottom:1px solid var(--line-soft)}
.chips{display:flex;flex-wrap:wrap;gap:5px}
.chip{font-size:11.5px;padding:3px 9px;border-radius:999px;border:1px solid var(--line);background:transparent;color:var(--ink);display:inline-flex;gap:5px;align-items:center}
.chip:hover{border-color:var(--muted)}
.chip .c{color:var(--muted);font-size:10.5px}
.chip[aria-pressed="true"]{background:var(--ink-deep);border-color:var(--ink-deep);color:var(--ground)}
.chip[aria-pressed="true"] .c{color:var(--muted)}
.frow{display:flex;gap:6px;margin-top:8px}
.search,.sel{font:inherit;font-size:12.5px;padding:6px 9px;border:1px solid var(--line);border-radius:7px;background:var(--surface);color:var(--ink)}
.search{flex:1;min-width:0}
.search::placeholder{color:var(--muted)}

/* ---------- list ---------- */
.list{max-height:calc(100vh - 260px);overflow-y:auto}
.daygroup{padding:8px 13px 4px;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);background:var(--surface);border-top:1px solid var(--line-soft);border-bottom:1px solid var(--line-soft);position:sticky;top:0;z-index:1}
.row{display:block;width:100%;text-align:left;background:transparent;border:0;border-bottom:1px solid var(--line-soft);border-left:3px solid transparent;padding:9px 13px 10px;color:inherit}
.row:hover{background:var(--surface)}
.row[aria-current="true"]{background:var(--teal-soft);border-left-color:var(--teal)}
.row.d-ok{border-left-color:var(--ok)}
.row.d-kb{border-left-color:var(--teal)}
.row.d-dig{border-left-color:var(--warn)}
.row.d-product{border-left-color:var(--muted)}
.row-top{display:flex;align-items:center;gap:7px;margin-bottom:3px}
.who{font-size:10.5px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;display:inline-flex;align-items:center;gap:5px;min-width:0}
.who span.t{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:150px}
.who.h{color:var(--teal)}
.who.b{color:var(--muted)}
.dot{width:7px;height:7px;border-radius:50%;flex:none}
.who.h .dot{background:var(--teal)}
.who.b .dot{border:1.5px solid var(--muted)}
.time{margin-left:auto;font-size:10.5px;color:var(--muted);flex:none}
.row-q{font-size:13.5px;color:var(--ink-deep);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.row-tags{display:flex;flex-wrap:wrap;gap:4px;margin-top:6px;align-items:center}
.tag{font-size:10px;letter-spacing:.04em;padding:1px 6px;border-radius:4px;border:1px solid var(--line);color:var(--muted);text-transform:uppercase;font-weight:600}
.tag.crit{color:var(--critical);border-color:var(--critical);background:var(--critical-soft)}
.tag.cat{text-transform:none;letter-spacing:0;font-weight:500;color:var(--ink);background:var(--surface-2)}
.tag.dec{color:#fff;border:0;font-weight:600}
.tag.dec.ok{background:var(--ok)} .tag.dec.kb{background:var(--teal)}
.tag.dec.dig{background:var(--warn)} .tag.dec.product{background:var(--muted)}
.tag.sug{border-style:dashed}
.tag.hasnote{background:var(--brand);border-color:var(--brand);color:#fff}
.empty{padding:26px 16px;color:var(--muted);font-size:13px;text-align:center}

/* ---------- rollup ---------- */
.rollup{padding:12px 13px;border-top:1px solid var(--line-soft)}
.rollup h3{margin:0 0 8px;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:600}
table.rt{width:100%;border-collapse:collapse;font-size:12px}
table.rt th{text-align:right;font-weight:600;color:var(--muted);font-size:10px;text-transform:uppercase;letter-spacing:.06em;padding:0 0 4px}
table.rt th:first-child{text-align:left}
table.rt td{padding:2px 0;border-top:1px solid var(--line-soft);text-align:right;font-variant-numeric:tabular-nums}
table.rt td:first-child{text-align:left;color:var(--ink-deep)}
table.rt td.z{color:var(--line)}
table.rt tr.tot td{font-weight:700;color:var(--ink-deep);border-top:1px solid var(--line)}
.rt button{background:none;border:0;padding:0;color:inherit;font:inherit;text-align:left}
.rt button:hover{color:var(--brand);text-decoration:underline}

.cites{padding:12px 13px;border-top:1px solid var(--line-soft)}
.cites h3{margin:0 0 7px;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:600}
.cites ol{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:3px}
.cites li{display:flex;gap:8px;font-size:11.5px;align-items:baseline}
.cites .n{color:var(--teal);font-weight:700;min-width:14px}
.cites .m{color:var(--critical)}

/* ---------- detail ---------- */
.detail{min-height:70vh}
.dhead{padding:16px 20px 14px;border-bottom:1px solid var(--line-soft)}
.dhead h2{margin:0 0 8px;font-size:18px;line-height:1.35;color:var(--ink-deep);font-weight:600;text-wrap:balance}
.meta{display:flex;flex-wrap:wrap;gap:5px 14px;font-size:12px;color:var(--muted);align-items:center}
.meta b{color:var(--ink-deep);font-weight:600}
.idcopy{border:1px solid var(--line);background:var(--surface);border-radius:6px;padding:2px 8px;font-size:11.5px;color:var(--ink-deep)}
.idcopy:hover{border-color:var(--brand);color:var(--brand)}

.triage{padding:14px 20px;border-bottom:1px solid var(--line-soft);background:var(--surface);display:flex;flex-direction:column;gap:12px}
.tlabel{font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:600;margin-bottom:5px}
.decs{display:flex;flex-wrap:wrap;gap:7px}
.dec-btn{border:1px solid var(--line);background:var(--raise);border-radius:8px;padding:7px 12px;font-size:13px;color:var(--ink);display:flex;flex-direction:column;gap:1px;align-items:flex-start;min-width:150px}
.dec-btn small{font-size:10.5px;color:var(--muted);font-weight:400}
.dec-btn:hover{border-color:var(--muted)}
.dec-btn[aria-pressed="true"]{color:#fff;border-color:transparent}
.dec-btn[aria-pressed="true"] small{color:rgba(255,255,255,.85)}
.dec-btn[aria-pressed="true"][data-d="ok"]{background:var(--ok)}
.dec-btn[aria-pressed="true"][data-d="kb"]{background:var(--teal)}
.dec-btn[aria-pressed="true"][data-d="dig"]{background:var(--warn)}
.dec-btn[aria-pressed="true"][data-d="product"]{background:var(--muted)}
.trow{display:flex;gap:16px;flex-wrap:wrap;align-items:flex-end}
.note{width:100%;font:inherit;font-size:13.5px;padding:9px 11px;border:1px solid var(--line);border-radius:8px;background:var(--raise);color:var(--ink);resize:vertical;min-height:62px}
.note::placeholder{color:var(--muted)}
.claudread{margin:14px 20px 0;border:1px solid var(--line);border-left:3px solid var(--teal);border-radius:0 8px 8px 0;background:var(--surface);padding:11px 15px}
.claudread.v-verify,.claudread.v-check{border-left-color:var(--warn)}
.claudread.v-product,.claudread.v-client,.claudread.v-noise{border-left-color:var(--muted)}
.claudread .vk{font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:600;margin-bottom:3px}
.claudread .vt{color:var(--ink-deep);font-weight:600;margin-bottom:3px}
.claudread p{margin:0;font-size:13.5px}

.thread{padding:16px 20px 26px;display:flex;flex-direction:column;gap:13px}
.turn{display:grid;grid-template-columns:92px 1fr;gap:13px;align-items:start}
.turn .lbl{font-size:10.5px;letter-spacing:.05em;text-transform:uppercase;font-weight:600;color:var(--muted);padding-top:4px;text-align:right;overflow-wrap:anywhere}
.turn.t-customer .lbl{color:var(--ink-deep)}
.turn.t-human .lbl{color:var(--teal)}
.bubble{font-family:Georgia,"Iowan Old Style","Times New Roman",serif;font-size:14.5px;line-height:1.6;white-space:pre-wrap;overflow-wrap:anywhere;padding:10px 14px;border-radius:8px;border:1px solid var(--line-soft);background:var(--surface)}
.turn.t-customer .bubble{background:var(--surface-2);border-color:var(--line)}
.turn.t-human .bubble{background:var(--teal-soft);border-color:var(--teal)}
.turn.t-bot .bubble{background:transparent}
.cited{margin-top:8px;font-family:ui-sans-serif,system-ui,sans-serif;font-size:11.5px;color:var(--muted);border-top:1px dashed var(--line);padding-top:6px}
.cited b{display:block;letter-spacing:.08em;text-transform:uppercase;font-size:10px;margin-bottom:3px;font-weight:600}
.cited .m{color:var(--critical)}
.placeholder{padding:60px 24px;text-align:center;color:var(--muted)}
.placeholder .big{font-size:15px;color:var(--ink-deep);margin-bottom:6px}

dialog{border:1px solid var(--line);border-radius:12px;background:var(--raise);color:var(--ink);padding:0;max-width:min(780px,92vw);width:100%;box-shadow:var(--shadow)}
dialog::backdrop{background:rgba(26,34,43,.45)}
.dlg{padding:18px 20px;display:flex;flex-direction:column;gap:12px}
.dlg h2{margin:0;font-size:17px;color:var(--ink-deep)}
.dlg p{margin:0;font-size:13px;color:var(--muted)}
.dlg textarea{width:100%;height:340px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;line-height:1.5;padding:11px;border:1px solid var(--line);border-radius:8px;background:var(--surface);color:var(--ink);resize:vertical}
.dlg .row{display:flex;gap:8px;justify-content:flex-end;border:0;padding:0}

@media (max-width:1080px){
  .shell{grid-template-columns:1fr}
  .list{max-height:none}
  .turn{grid-template-columns:1fr;gap:4px}
  .turn .lbl{text-align:left}
}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""

SKELETON = """
<header class="mast"><div class="mast-in">
  <div class="brandblock">
    <p class="eyebrow">Weekly review</p>
    <h1>Help desk triage <span class="rng" id="rng"></span></h1>
  </div>
  <div class="prog">
    <div class="bar"><span id="barfill" style="width:0%"></span></div>
    <div class="lbl" id="proglbl"></div>
  </div>
  <div class="act">
    <span class="save" id="save"></span>
    <button class="btn" id="undecided">Next undecided</button>
    <button class="btn primary" id="handoff">Hand to Claude</button>
  </div>
</div></header>

<main class="shell">
  <section class="pane">
    <div class="filters">
      <div class="chips" id="chips"></div>
      <div class="frow">
        <input class="search" id="q" type="search" placeholder="Search questions and transcripts" aria-label="Search conversations">
        <select class="sel" id="catfilter" aria-label="Filter by category"></select>
      </div>
    </div>
    <div class="list" id="list"></div>
    <div class="rollup"><h3>By category — where the questions come from</h3><div id="rollup"></div></div>
    <div class="cites"><h3>What the AI cited most, with no human in the thread</h3><ol id="cites"></ol></div>
  </section>
  <section class="pane detail" id="detail"></section>
</main>

<dialog id="hdlg"><div class="dlg">
  <h2>Hand this back to Claude</h2>
  <p>Everything decided, with your notes. Copy it into the chat — Claude picks up from here.</p>
  <textarea id="hout" readonly></textarea>
  <div class="row">
    <button class="btn" id="hclose">Close</button>
    <button class="btn primary" id="hcopy">Copy</button>
  </div>
</div></dialog>
"""

APP = r"""
const el = s => document.querySelector(s);
const esc = s => (s||'').replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const MARKETING = /— Zooza$|Zooza PRO|Cen[íi]k|Cennik/;
const CATLBL = Object.fromEntries(META.categories);
const DECLBL = Object.fromEntries(META.decisions.map(d => [d[0], d[1]]));

let filter = 'todo', catf = '', q = '', current = null, readOnly = false;

const FILTERS = [
  ['todo',    'To decide',   c => !S(c).d],
  ['all',     'All',         c => true],
  ['kb',      'Into the KB', c => S(c).d === 'kb'],
  ['dig',     'Dig into it', c => S(c).d === 'dig'],
  ['ok',      'Fine',        c => S(c).d === 'ok'],
  ['product', 'Product',     c => S(c).d === 'product'],
  ['noted',   'Has my note', c => !!S(c).note],
  ['human',   'Human',       c => c.human && c.channel === 'intercom'],
  ['bot',     'AI only',     c => !c.human],
  ['email',   'Email',       c => c.channel === 'email'],
];

const S = c => (STATE[c.id] ||= {d:'', cat:c.cat, note:'', sug:''});
const byId = id => DATA.find(c => c.id === id);

/* ---------- persistence ---------- */
let saveTimer = null, artifact = null, dirty = false;

function mirror(){ try{ localStorage.setItem('zooza-board-' + META.end, JSON.stringify(STATE)); }catch(e){} }

function setSave(text, cls){ const s = el('#save'); s.textContent = text; s.className = 'save ' + (cls||''); }

function touch(){
  dirty = true; mirror(); setSave('Unsaved…');
  clearTimeout(saveTimer);
  saveTimer = setTimeout(commit, 2500);
}

function buildDoc(){
  const css  = document.getElementById('sheet').textContent;
  const skel = document.getElementById('skeleton').innerHTML;
  const app  = document.getElementById('app').textContent;
  const enc  = o => JSON.stringify(o).replace(/</g,'\\u003c').replace(/\u2028/g,'\\u2028').replace(/\u2029/g,'\\u2029');
  const S_ = '<' + 'script';
  const E_ = '<' + '/script>';
  return '<!doctype html><html lang="en"><head><meta charset="utf-8">'
    + '<meta name="viewport" content="width=device-width,initial-scale=1">'
    + '<title>' + esc(document.title) + '</title>'
    + '<style id="sheet">' + css + '</style></head><body>'
    + skel
    + '<template id="skeleton">' + skel + '</template>'
    + S_ + ' id="data">const DATA=' + enc(DATA) + ';const META=' + enc(META) + ';' + E_
    + S_ + ' id="state">const STATE=' + enc(STATE) + ';' + E_
    + S_ + ' id="app">' + app + E_
    + '</body></html>';
}

async function commit(){
  if (!dirty || readOnly) return;
  if (!artifact){ setSave('Saved on this device', ''); dirty = false; return; }
  setSave('Saving…');
  try {
    sessionStorage.setItem('zooza-board-sel', current || '');
    sessionStorage.setItem('zooza-board-filter', filter);
    await artifact.publish(buildDoc());
    dirty = false; setSave('Saved', 'on');
  } catch (e) {
    if (e && (e.code === 'not_writer' || e.code === 'not_granted' || e.code === 'not_declared'
              || e.code === 'capability_disabled' || e.code === 'capability_removed')) {
      readOnly = true; setSave('Read-only view', 'err'); return;
    }
    if (e && e.code === 'conflict') return;               // the view is reloading to the winner
    if (e && e.code === 'rate_limited'){ saveTimer = setTimeout(commit, 8000); setSave('Queued…'); return; }
    setSave('Saved on this device only', 'err');
  }
}

/* ---------- rendering ---------- */
function matches(c){
  if (!FILTERS.find(x => x[0] === filter)[2](c)) return false;
  if (catf && S(c).cat !== catf) return false;
  if (!q) return true;
  const hay = (c.q + ' ' + c.vtitle + ' ' + c.vnote + ' ' + c.id + ' ' + S(c).note + ' ' +
               c.turns.map(t => t.text).join(' ')).toLowerCase();
  return hay.includes(q);
}

function tags(c){
  const s = S(c), out = [];
  if (s.d) out.push('<span class="tag dec ' + s.d + '">' + DECLBL[s.d] + '</span>');
  else if (s.sug) out.push('<span class="tag sug">suggests ' + DECLBL[s.sug] + '</span>');
  out.push('<span class="tag cat">' + esc(CATLBL[s.cat] || s.cat) + '</span>');
  if (s.note) out.push('<span class="tag hasnote">note</span>');
  if (c.bucket === 'A_hard_signal') out.push('<span class="tag crit">hard signal</span>');
  if (c.reask >= 4) out.push('<span class="tag">re-asked ' + c.reask + '&times;</span>');
  return out.join('');
}

function renderChips(){
  el('#chips').innerHTML = FILTERS.map(([k, label, fn]) =>
    '<button class="chip" data-f="' + k + '" aria-pressed="' + (filter === k) + '">' +
    label + ' <span class="c">' + DATA.filter(fn).length + '</span></button>').join('');
}

function renderProgress(){
  const done = DATA.filter(c => S(c).d).length, total = DATA.length;
  el('#barfill').style.width = (total ? (done / total * 100) : 0) + '%';
  el('#proglbl').innerHTML = '<b>' + done + '</b> of ' + total + ' decided';
}

function renderList(){
  const rows = DATA.filter(matches);
  if (!rows.length){ el('#list').innerHTML = '<p class="empty">Nothing matches that.</p>'; return; }
  let out = '', day = '';
  for (const c of rows){
    if (c.day !== day){
      day = c.day;
      out += '<div class="daygroup">' +
        new Date(day + 'T12:00:00').toLocaleDateString('en-GB', {weekday:'long', day:'numeric', month:'long'}) +
        '</div>';
    }
    const s = S(c);
    out += '<button class="row' + (s.d ? ' d-' + s.d : '') + '" data-id="' + c.id + '"' +
             ' aria-current="' + (current === c.id) + '">' +
             '<span class="row-top">' +
               '<span class="who ' + (c.human ? 'h' : 'b') + '"><span class="dot"></span><span class="t">' +
                 (c.channel === 'email' ? esc(c.from || 'Email') : c.human ? 'Human' : 'AI only') +
               '</span></span>' +
               '<span class="time mono">' + c.date.slice(11) + '</span>' +
             '</span>' +
             '<span class="row-q">' + esc(c.vtitle || c.q) + '</span>' +
             '<span class="row-tags">' + tags(c) + '</span>' +
           '</button>';
  }
  el('#list').innerHTML = out;
}

function renderRollup(){
  const keys = META.categories.map(x => x[0]);
  const agg = {};
  for (const k of keys) agg[k] = {n:0, kb:0, dig:0, ok:0, product:0, todo:0};
  for (const c of DATA){
    const s = S(c), a = agg[s.cat] || (agg[s.cat] = {n:0, kb:0, dig:0, ok:0, product:0, todo:0});
    a.n++; if (s.d) a[s.d]++; else a.todo++;
  }
  const rows = keys.filter(k => agg[k].n).sort((a, b) => agg[b].n - agg[a].n);
  const cell = v => v ? String(v) : '<span class="z">·</span>';
  let h = '<table class="rt"><thead><tr><th>Category</th><th>All</th><th>KB</th><th>Dig</th><th>Fine</th><th>Left</th></tr></thead><tbody>';
  for (const k of rows){
    const a = agg[k];
    h += '<tr><td><button data-cat="' + k + '">' + esc(CATLBL[k] || k) + '</button></td>' +
         '<td>' + a.n + '</td><td>' + cell(a.kb) + '</td><td>' + cell(a.dig) + '</td>' +
         '<td>' + cell(a.ok) + '</td><td>' + cell(a.todo) + '</td></tr>';
  }
  const t = rows.reduce((o, k) => { const a = agg[k];
    return {n:o.n+a.n, kb:o.kb+a.kb, dig:o.dig+a.dig, ok:o.ok+a.ok, todo:o.todo+a.todo}; },
    {n:0, kb:0, dig:0, ok:0, todo:0});
  h += '<tr class="tot"><td>All</td><td>' + t.n + '</td><td>' + t.kb + '</td><td>' + t.dig +
       '</td><td>' + t.ok + '</td><td>' + t.todo + '</td></tr></tbody></table>';
  el('#rollup').innerHTML = h;
}

const VKEY = {gap:'Claude reads this as a KB gap', verify:'Claude cannot confirm this',
              check:'Claude wants to read the article first', product:'Claude reads this as a product issue',
              client:'Claude reads this as one client only', noise:'Claude reads this as noise'};

function renderDetail(){
  const c = byId(current);
  if (!c){
    el('#detail').innerHTML = '<div class="placeholder"><p class="big">Pick a conversation, or hit “Next undecided”.</p>' +
      '<p>' + DATA.length + ' this week. Decide each one, add a note where you want Claude to act, ' +
      'then hand the lot back with the button in the header.</p></div>';
    return;
  }
  const s = S(c);
  let h = '<div class="dhead"><h2>' + esc(c.vtitle || c.q.slice(0, 140)) + '</h2><div class="meta">' +
    '<button class="idcopy mono" id="idcopy" title="Copy the conversation id">' + c.id + '</button>' +
    '<span class="mono">' + c.date + '</span>' +
    (c.channel === 'email'
      ? '<span>Email from <b>' + esc(c.from) + '</b></span>'
      : '<span>Answered by <b>' + (c.human ? 'a human' : 'the AI alone') + '</b></span>' +
        '<span>Resolution <b>' + esc(c.resolution) + '</b></span>') +
    (c.reask ? '<span>Client wrote back <b>' + c.reask + '&times;</b> after the AI</span>' : '') +
    (c.rating != null ? '<span>Rated <b>' + c.rating + '</b></span>' : '') +
    '</div></div>';

  h += '<div class="triage"><div>' +
       '<div class="tlabel">Decision</div><div class="decs">' +
       META.decisions.map(([k, label, hint]) =>
         '<button class="dec-btn" data-d="' + k + '" aria-pressed="' + (s.d === k) + '">' +
         label + '<small>' + esc(hint) + '</small></button>').join('') +
       '</div></div>' +
       '<div class="trow"><div><div class="tlabel">Category</div>' +
       '<select class="sel" id="catset">' + META.categories.map(([k, label]) =>
         '<option value="' + k + '"' + (s.cat === k ? ' selected' : '') + '>' + esc(label) + '</option>').join('') +
       '</select></div></div>' +
       '<div><div class="tlabel">Note to Claude</div>' +
       '<textarea class="note" id="noteset" placeholder="What you want done with this one. Screenshots go in the chat — quote the id above.">' +
       esc(s.note) + '</textarea></div></div>';

  if (c.verdict){
    h += '<div class="claudread v-' + c.verdict + '"><div class="vk">' + (VKEY[c.verdict] || c.verdict) + '</div>' +
         (c.vtitle ? '<div class="vt">' + esc(c.vtitle) + '</div>' : '') +
         '<p>' + esc(c.vnote) + '</p></div>';
  }

  h += '<div class="thread">';
  for (const t of c.turns){
    if (!t.text && !t.cited.length) continue;
    const role = t.role === 'customer' ? 'customer' : (t.role === 'human' ? 'human' : 'bot');
    const lbl = role === 'customer' ? esc(t.who || 'Client')
              : role === 'human' ? esc(t.who || 'Zooza') : 'AI';
    h += '<div class="turn t-' + role + '"><div class="lbl">' + lbl + '</div><div class="bubble">' + esc(t.text);
    if (t.cited.length){
      h += '<div class="cited"><b>Cited</b>' + t.cited.map(x =>
             '<div class="' + (MARKETING.test(x) ? 'm' : '') + '">' + esc(x) + '</div>').join('') + '</div>';
    }
    h += '</div></div>';
  }
  el('#detail').innerHTML = h + '</div>';
}

function renderAll(){ renderChips(); renderProgress(); renderList(); renderRollup(); renderDetail(); }

/* ---------- handoff ---------- */
function handoff(){
  const order = ['kb', 'dig', 'product', 'ok'];
  const head = {kb:'Into the KB', dig:'Dig into it first', product:'Product, not KB', ok:'Fine as answered'};
  let out = '# Weekly review — ' + META.start + ' to ' + META.end + '\n';
  const left = DATA.filter(c => !S(c).d).length;
  out += '\n' + (DATA.length - left) + ' of ' + DATA.length + ' decided' +
         (left ? ', ' + left + ' still open' : '') + '.\n';
  for (const d of order){
    const rows = DATA.filter(c => S(c).d === d);
    if (!rows.length) continue;
    out += '\n## ' + head[d] + ' (' + rows.length + ')\n\n';
    for (const c of rows){
      const s = S(c);
      if (d === 'ok' && !s.note){ out += '- ' + c.id + ' — ' + (c.vtitle || c.q.slice(0, 70)) + '\n'; continue; }
      out += '- **' + c.id + '** [' + (CATLBL[s.cat] || s.cat) + '] ' + (c.vtitle || c.q.slice(0, 90)) + '\n';
      if (s.note) out += '  - Michal: ' + s.note.replace(/\n+/g, ' ') + '\n';
    }
  }
  const undec = DATA.filter(c => !S(c).d);
  if (undec.length){
    out += '\n## Not decided yet (' + undec.length + ')\n\n';
    for (const c of undec) out += '- ' + c.id + ' — ' + (c.vtitle || c.q.slice(0, 70)) + '\n';
  }
  el('#hout').value = out;
  el('#hdlg').showModal();
}

/* ---------- events ---------- */
el('#chips').addEventListener('click', e => {
  const b = e.target.closest('.chip'); if (!b) return;
  filter = b.dataset.f; renderChips(); renderList();
});
el('#catfilter').addEventListener('change', e => { catf = e.target.value; renderList(); });
el('#q').addEventListener('input', e => { q = e.target.value.trim().toLowerCase(); renderList(); });
el('#list').addEventListener('click', e => {
  const b = e.target.closest('.row'); if (!b) return;
  current = b.dataset.id; renderList(); renderDetail();
  el('#detail').scrollIntoView({block:'nearest'});
});
el('#rollup').addEventListener('click', e => {
  const b = e.target.closest('button[data-cat]'); if (!b) return;
  catf = b.dataset.cat; el('#catfilter').value = catf; filter = 'all'; renderChips(); renderList();
});
el('#detail').addEventListener('click', e => {
  const d = e.target.closest('.dec-btn');
  if (d){
    const c = byId(current), s = S(c);
    s.d = (s.d === d.dataset.d) ? '' : d.dataset.d;
    touch(); renderProgress(); renderList(); renderRollup(); renderDetail(); return;
  }
  if (e.target.closest('#idcopy')){
    navigator.clipboard?.writeText(current);
    const b = e.target.closest('#idcopy'); const t = b.textContent;
    b.textContent = 'copied'; setTimeout(() => { b.textContent = t; }, 900);
  }
});
el('#detail').addEventListener('change', e => {
  if (e.target.id === 'catset'){ S(byId(current)).cat = e.target.value; touch(); renderList(); renderRollup(); }
  if (e.target.id === 'noteset'){ renderList(); }
});
el('#detail').addEventListener('input', e => {
  if (e.target.id === 'noteset'){ S(byId(current)).note = e.target.value; touch(); }
});
el('#undecided').addEventListener('click', () => {
  const start = DATA.findIndex(c => c.id === current);
  for (let i = 1; i <= DATA.length; i++){
    const c = DATA[(start + i + DATA.length) % DATA.length];
    if (!S(c).d){ current = c.id; filter = 'todo'; renderAll(); el('#detail').scrollIntoView({block:'nearest'}); return; }
  }
  setSave('All decided', 'on');
});
el('#handoff').addEventListener('click', handoff);
el('#hclose').addEventListener('click', () => el('#hdlg').close());
el('#hcopy').addEventListener('click', async () => {
  const t = el('#hout'); t.select();
  try { await navigator.clipboard.writeText(t.value); el('#hcopy').textContent = 'Copied'; }
  catch(e) { document.execCommand('copy'); el('#hcopy').textContent = 'Copied'; }
  setTimeout(() => { el('#hcopy').textContent = 'Copy'; }, 1200);
});
window.addEventListener('beforeunload', e => { if (dirty){ commit(); e.preventDefault(); e.returnValue = ''; } });

/* ---------- boot ---------- */
el('#rng').textContent = META.start + ' – ' + META.end;
el('#catfilter').innerHTML = '<option value="">Every category</option>' +
  META.categories.map(([k, l]) => '<option value="' + k + '">' + esc(l) + '</option>').join('');
el('#cites').innerHTML = META.topCited.map(([s, n]) =>
  '<li><span class="n mono">' + n + '</span><span class="' + (MARKETING.test(s) ? 'm' : '') + '">' +
  esc(s) + '</span></li>').join('');

current = sessionStorage.getItem('zooza-board-sel') || null;
filter  = sessionStorage.getItem('zooza-board-filter') || 'todo';
sessionStorage.removeItem('zooza-board-sel'); sessionStorage.removeItem('zooza-board-filter');
setSave('');
renderAll();

if (typeof claude !== 'undefined' && claude && typeof claude.use === 'function'){
  claude.use('artifact').then(a => {
    artifact = a;
    if (!a) setSave('Saved on this device', '');
    else if (!dirty) setSave('Saving is on', 'on');
  }).catch(() => { setSave('Saved on this device', ''); });
} else {
  setSave('Saved on this device', '');
}
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
