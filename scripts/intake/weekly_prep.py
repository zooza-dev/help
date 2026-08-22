#!/usr/bin/env python3
"""Weekly intake preparation.

Runs Friday morning and prepares the queue for the review session. It does the
mechanical part only -- fetch, triage, sweep -- and never writes to content/.
Deciding what is true about the product stays with a human; the July 2026 intake
produced three false claims that only a human caught.

Window: the seven full days ending the day before the run. A Friday run covers
the previous Friday through Thursday, so consecutive runs tile without gaps or
overlap.

Specs are tracked from the first run onwards. That run records a baseline of
everything already implemented and reports nothing; later runs report only what
became implemented since.

Usage:
    python3 scripts/intake/weekly_prep.py              # window ends yesterday
    python3 scripts/intake/weekly_prep.py --date 2026-08-14   # pretend it is that day
    python3 scripts/intake/weekly_prep.py --no-fetch   # reuse what is already ingested
"""
import argparse
import json
import os
import re
import subprocess
import sys
from datetime import date, datetime, timedelta

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
STATE_PATH = os.path.join(os.path.dirname(__file__), ".weekly_state.json")
SPEC_REPOS = ["api-v1", "app", "widgets-v1"]

# Client threads worth reading. Keyword search returns mostly no-reply booking
# notifications, so the allowlist is by sender.
EMAIL_SENDERS = [
    "sarahmarsh@magikats.co.uk",
    "centralberks@weekicks.co.uk",
    "anna.blackwell@turtletots.com",
    "techsupport@zooza.online",
]


def load_state():
    if os.path.exists(STATE_PATH):
        with open(STATE_PATH) as f:
            return json.load(f)
    return {}


def save_state(state):
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=1, sort_keys=True)


def window_for(run_day, state):
    """The days not yet covered, ending yesterday.

    Normally that is the seven days Friday..Thursday. But the window continues
    from where the last run stopped rather than counting back from today, so
    running a few days late widens the window instead of skipping the gap.
    Nothing is ever missed and nothing is reviewed twice.
    """
    end = run_day - timedelta(days=1)
    last = state.get("last_window")
    if last:
        start = date.fromisoformat(last[1]) + timedelta(days=1)
        if start > end:
            return None, end  # already covered
        return start, end
    return end - timedelta(days=6), end


def frontmatter(path):
    """Parse the leading YAML block well enough for flat scalar fields."""
    out = {}
    try:
        with open(path, encoding="utf-8") as f:
            if f.readline().strip() != "---":
                return out
            for line in f:
                if line.strip() == "---":
                    break
                m = re.match(r"^([a-z_]+):\s*(.*)$", line.rstrip("\n"))
                if m:
                    out[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    except OSError:
        pass
    return out


def frontmatter_text(text):
    """Same parse, but from a string rather than a path."""
    out = {}
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return out
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return out


def git(repo_path, *args):
    r = subprocess.run(
        ["git", "-C", repo_path, *args], capture_output=True, text=True
    )
    return r.stdout if r.returncode == 0 else None


def sweep_specs(state):
    """Implemented specs with no docs_communicated date, new since the baseline.

    Reads origin/main rather than the working tree. A sibling repo is often
    dozens of commits behind, and reading the checkout silently reports zero
    new specs while implemented ones sit on the remote.
    """
    current, undocumented = {}, []
    for repo in SPEC_REPOS:
        path = os.path.join(REPO, "..", repo)
        if not os.path.isdir(os.path.join(path, ".git")):
            continue

        git(path, "fetch", "origin", "main", "-q")
        listing = git(path, "ls-tree", "-r", "--name-only", "origin/main", "specs/implemented/")
        if listing is None:
            print(f"  {repo}: cannot read origin/main -- skipped")
            continue

        behind = (git(path, "rev-list", "--count", "HEAD..origin/main") or "0").strip()
        if behind.isdigit() and int(behind) > 0:
            print(f"  {repo}: checkout is {behind} commit(s) behind; read from origin/main")

        for rel in sorted(f for f in listing.splitlines() if f.endswith(".md")):
            name = os.path.basename(rel)
            blob = git(path, "show", f"origin/main:{rel}")
            if blob is None:
                continue
            fm = frontmatter_text(blob)
            key = f"{repo}/{name}"
            current[key] = True
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", fm.get("docs_communicated", "")):
                undocumented.append(
                    {
                        "key": key,
                        "repo": repo,
                        "file": name,
                        "spec_id": fm.get("spec_id", ""),
                        "title": fm.get("title", ""),
                        "updated": fm.get("updated", ""),
                    }
                )

    baseline = state.get("spec_baseline")
    if baseline is None:
        state["spec_baseline"] = sorted(current)
        return [], len(current), True

    known = set(baseline)
    fresh = [s for s in undocumented if s["key"] not in known]
    state["spec_baseline"] = sorted(set(baseline) | set(current))
    return fresh, len(current), False


def question(rec):
    """First thing the client actually asked. Turns are [role, name, text]."""
    for role, _, text in rec.get("turns", []):
        if role == "customer" and text.strip():
            return " ".join(text.split())
    return "(no client message)"


def human_answer(rec):
    """First human reply -- the gold standard the KB should absorb."""
    for role, _, text in rec.get("turns", []):
        if role == "human" and text.strip():
            return " ".join(text.split())
    return ""


def run(cmd, **kw):
    print("  $", " ".join(cmd))
    return subprocess.run(cmd, cwd=REPO, **kw)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="run date (YYYY-MM-DD); defaults to today")
    ap.add_argument("--no-fetch", action="store_true", help="skip the Intercom fetch")
    args = ap.parse_args()

    run_day = (
        datetime.strptime(args.date, "%Y-%m-%d").date() if args.date else date.today()
    )
    state = load_state()
    start, end = window_for(run_day, state)
    if start is None:
        print(f"Nothing to do -- everything up to {end} has already been reviewed.")
        return
    span_days = (end - start).days + 1
    print(f"Window: {start} ({start.strftime('%a')}) -> {end} ({end.strftime('%a')})  [{span_days} days]")
    if span_days > 7:
        print(f"  running {span_days - 7} day(s) late -- window widened so nothing is skipped")
    print()

    if not args.no_fetch:
        print("Fetching Intercom...")
        span = (run_day - start).days + 1
        r = run([sys.executable, "scripts/fetch_intercom.py", "--days", str(span)])
        if r.returncode != 0:
            print("  fetch failed -- continuing with whatever is already ingested")

    print("\nTriaging...")
    out_dir = os.path.join(REPO, "build", "intake")
    triage = run(
        [
            sys.executable,
            "scripts/intake/triage.py",
            "--start", start.isoformat(),
            "--end", end.isoformat(),
            "--out", out_dir,
        ],
        capture_output=True,
        text=True,
    )
    print(triage.stdout or "")
    if triage.stderr:
        print(triage.stderr, file=sys.stderr)

    bot = []
    bot_path = os.path.join(out_dir, "bot_only.json")
    if os.path.exists(bot_path):
        with open(bot_path) as f:
            bot = json.load(f)
    human = []
    human_path = os.path.join(out_dir, "human.json")
    if os.path.exists(human_path):
        with open(human_path) as f:
            human = json.load(f)

    print("Sweeping specs...")
    fresh_specs, total_specs, first_run = sweep_specs(state)

    # Highest-risk first. A bot answer sourced only from marketing pages was the
    # strongest predictor of a wrong answer in the July intake.
    priority = [r for r in bot if r.get("bucket") in ("A_hard_signal", "B_no_kb_source", "C_reask")]
    order = {"A_hard_signal": 0, "B_no_kb_source": 1, "C_reask": 2}
    priority.sort(key=lambda r: (order.get(r.get("bucket"), 9), -r.get("cust_after_bot", 0)))

    report = os.path.join(REPO, "build", "reports", f"weekly-intake-{end.isoformat()}.md")
    os.makedirs(os.path.dirname(report), exist_ok=True)
    with open(report, "w", encoding="utf-8") as f:
        w = f.write
        w(f"# Weekly intake queue -- {start} to {end}\n\n")
        w(f"Prepared {run_day}. Nothing here has been written to `content/` -- this is a queue.\n\n")
        w("## Counts\n\n")
        w(f"- Conversations with a human reply: **{len(human)}**\n")
        w(f"- Bot-only conversations: **{len(bot)}**\n")
        w(f"- Bot-only needing a look: **{len(priority)}**\n")
        w(f"- Implemented specs not yet communicated: **{len(fresh_specs)}**\n\n")

        w("## 1. Human answers -- the gold standard\n\n")
        w("Read these first. A human answer that generalises belongs in the KB.\n\n")
        if human:
            for r in human:
                w(f"### `{r.get('id')}` -- {r.get('date','')}\n\n")
                w(f"**Asked:** {question(r)[:400]}\n\n")
                ans = human_answer(r)
                if ans:
                    w(f"**Human answered:** {ans[:700]}\n\n")
        else:
            w("_None this week._\n")

        w("\n## 2. Bot-only, highest risk first\n\n")
        w("`A_hard_signal` = routed to team, abandoned, or rated poorly. ")
        w("`B_no_kb_source` = the bot cited nothing from the KB. ")
        w("`C_reask` = the client asked again two or more times.\n\n")
        if priority:
            for r in priority:
                srcs = ", ".join(r.get("sources", [])[:3]) or "(no KB source)"
                reask = r.get("cust_after_bot", 0)
                w(f"- **{r.get('bucket')}** `{r.get('id')}` {r.get('date','')}")
                w(f" -- re-asked {reask}x\n" if reask >= 2 else "\n")
                w(f"  - Q: {question(r)[:250]}\n")
                w(f"  - cited: {srcs}\n")
        else:
            w("_None this week._\n")

        w("\n## 3. Shipped but never communicated\n\n")
        if first_run:
            w(f"First run -- recorded a baseline of {total_specs} implemented specs. ")
            w("Tracking starts now, so nothing is listed. Later runs show only new ones.\n")
        elif fresh_specs:
            w("| Repo | Spec | Title | Updated |\n|---|---|---|---|\n")
            for s in fresh_specs:
                w(f"| {s['repo']} | {s['spec_id'] or s['file']} | {s['title']} | {s['updated']} |\n")
            w("\nStamp `docs_communicated` in the spec once the KB covers it.\n")
        else:
            w("_Nothing new._\n")

        w("\n## 4. Client email -- needs the review session\n\n")
        w("The Gmail connector needs an interactive login, so this step does not run here. ")
        w("In the session, search these senders over the window:\n\n")
        for s in EMAIL_SENDERS:
            w(f"- `{s}`\n")
        w(f"\n```\n{{{' '.join('from:' + s for s in EMAIL_SENDERS)}}} after:{start:%Y/%m/%d} before:{(end + timedelta(days=1)):%Y/%m/%d}\n```\n")

    # Do not close a window we could not actually look at. A run against an empty
    # ingest -- fetch skipped, failed, or nothing downloaded yet -- would otherwise
    # mark the week reviewed and the conversations would never be seen. Cost a
    # near-miss on 2026-08-22.
    if not human and not bot:
        print("\nNo conversations in this window. The window stays open —")
        print("run the fetch and try again rather than losing the week.")
    else:
        state["last_run"] = run_day.isoformat()
        state["last_window"] = [start.isoformat(), end.isoformat()]
        save_state(state)

    print(f"\nQueue written to {os.path.relpath(report, REPO)}")
    print(f"  human {len(human)} | bot-only {len(bot)} | needs a look {len(priority)} | specs {len(fresh_specs)}")


if __name__ == "__main__":
    main()
