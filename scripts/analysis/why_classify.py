#!/usr/bin/env python3
"""Name the reason a human had to answer, for every conversation in the window.

The buckets are chosen so that each one implies a different fix. A bucket that
cannot be acted on (the customer wanted a person, the data had to be looked at)
is still worth counting - it is the part of the queue no amount of documentation
will ever remove.
"""
import json, os, re, collections

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
rows = json.load(open(os.path.join(REPO, "build", "reports", "human-why.json")))

TICKET_ACK = re.compile(r"(ticket has been received|tiket by[lt] p[řr]ij|tiket bol prijat|Ihr Ticket wurde|Zooza Assistant will try|Asistent Zooza se)", re.I)
JIRA_FAIL = re.compile(r"Jira issue creation failed", re.I)
HANDOFF = re.compile(r"(pass you to|p[řr]ed[áa]m v[áa]s|prepoj[ií]m v[áa]s|spoj[ií]m v[áa]s|transfer you|transfera|vă voi transfera|connect you with a human)", re.I)
WANTS_HUMAN = re.compile(r"(spojeni[ea] s (ľud|lud)|ľudsk[ýy]m asistent|živ[ýy] člov|real person|human (agent|support)|wait for the team|na normalneho cloveka|posli to na cloveka|vorbesc cu cineva)", re.I)
# the human is looking at this account's data
ACCOUNT = re.compile(r"(registration number|registr[áa]ci[ei]|booking number|#registrations/|cislo registracie|č[íi]slo registr|screenshot|printscreen|poslite|po[šs]lite|send me|can you send|ktor[ýa] klient|example)", re.I)
# the human says it is a defect / promises a fix
DEFECT = re.compile(r"(chyba (u n[áa]s|v zobrazen|na na[šs]ej stran)|je to chyba|opravíme|opravime|oprav[ií]me to|fix(ed)? (it|this)|bug|nevychytali|d[áa]vame opravu|hodíme na produkciu|hodime na produkciu|we('| wi)ll fix|deployed? (a )?fix|nasadili sme|zablbl|zblbl)", re.I)
# the human is designing/scoping a feature with the customer
PRODUCT_WORK = re.compile(r"(v roadmape|do changelogu|pracujeme na|we're working on|we are working on|vieme to (dorobit|fixnut)|dorobit|m[áa]me vo v[ýy]voji|upravime (to|logiku)|add(ing)? (it|this) to|pripravujeme|specifik[áa]ci)", re.I)
# the human explains how the product works -> a knowledge answer
KNOWLEDGE = re.compile(r"(funguje to tak|system sa (takto )?sprava|nastavuje sa to|staci ak|sta[čc][íi]|m[ôo][žz]ete (to )?(nastavi|urobi|zmeni)|you can (set|change|do)|to je tym|je to preto|d[ôo]vod je|standardne)", re.I)

def classify(r):
    q, h, b = r["question"], r["human_said"], r["bot_said"]
    no_ai = (not r["bot_tried"]) or (TICKET_ACK.search(b) and not re.search(r"Sources:", b) and len(b) < 420)
    out = []
    if no_ai:
        out.append("no_ai_attempt")
    if JIRA_FAIL.search(b):
        out.append("jira_error_shown")
    if HANDOFF.search(b) and len(b) < 400:
        out.append("bot_handed_off")
    if WANTS_HUMAN.search(q):
        out.append("customer_demanded_human")
    if DEFECT.search(h):
        out.append("defect_confirmed")
    if PRODUCT_WORK.search(h):
        out.append("feature_work")
    if ACCOUNT.search(h):
        out.append("account_specific")
    if KNOWLEDGE.search(h):
        out.append("explained_behaviour")
    return out

# primary cause: first match in this order of precedence
ORDER = ["defect_confirmed", "feature_work", "account_specific",
         "customer_demanded_human", "no_ai_attempt", "bot_handed_off",
         "explained_behaviour"]

cause = collections.Counter()
detail = collections.Counter()
per = []
for r in rows:
    fl = classify(r)
    prim = next((k for k in ORDER if k in fl), "other")
    cause[prim] += 1
    for f in fl:
        detail[f] += 1
    per.append({**{k: r[k] for k in ("id", "day", "question", "human_said")},
                "flags": fl, "primary": prim,
                "top_kb": (r["kb_hits"][0] if r["kb_hits"] else None)})

print(f"conversations: {len(rows)}\n")
print("PRIMARY CAUSE (precedence: defect > feature > account > demanded human > no AI > handoff > explanation)")
for k, v in cause.most_common():
    print(f"  {v:4d}  {v*100//len(rows):3d}%  {k}")
print("\nSIGNALS (not exclusive)")
for k, v in detail.most_common():
    print(f"  {v:4d}  {v*100//len(rows):3d}%  {k}")

json.dump(per, open(os.path.join(REPO, "build", "reports", "why-classified.json"), "w"), ensure_ascii=False, indent=1)
