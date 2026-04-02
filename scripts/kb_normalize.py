#!/usr/bin/env python3
"""
kb:normalize — Apply canonical terminology replacements to content/**/*.md files.
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict
from datetime import date

CONTENT_DIR = Path("/Users/michaldodok/help/content")
LOG_PATH = Path("/Users/michaldodok/help/build/terminology/normalize-log.md")
DICT_PATH = Path("/Users/michaldodok/help/build/terminology/dictionary.json")
TODAY = "2026-03-14"

# ---------------------------------------------------------------------------
# Helpers to skip code blocks, HTML comments, image paths, URLs
# ---------------------------------------------------------------------------

def split_protected_regions(text):
    """
    Return a list of (start, end, protected_bool) spans for the text.
    Protected regions:
     - fenced code blocks (``` ... ```)
     - inline code (`...`)
     - HTML comments (<!-- ... -->)
     - image syntax: ![...](...) — protect the URL part only
     - link href: [...](...) — protect the URL/path in parens
     - frontmatter (first --- block) — handled separately
    """
    regions = []
    i = 0
    n = len(text)

    # We'll build a list of protected spans as (start, end)
    protected = []

    # Fenced code blocks
    for m in re.finditer(r'```[\s\S]*?```', text):
        protected.append((m.start(), m.end()))

    # Inline code (not inside fenced blocks)
    for m in re.finditer(r'`[^`\n]+`', text):
        # Check not inside a fenced block
        inside_fence = any(s <= m.start() and m.end() <= e for s, e in protected)
        if not inside_fence:
            protected.append((m.start(), m.end()))

    # HTML comments
    for m in re.finditer(r'<!--[\s\S]*?-->', text):
        protected.append((m.start(), m.end()))

    # Image alt text and path: ![alt](path) — protect entire thing
    for m in re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)', text):
        protected.append((m.start(), m.end()))

    # Link URLs in markdown: [text](url) — protect only the URL part
    for m in re.finditer(r'\[([^\]]*)\]\(([^)]+)\)', text):
        # protect the URL portion (group 2)
        url_start = m.start(2)
        url_end = m.end(2)
        protected.append((url_start, url_end))

    # HTML img src and href attributes
    for m in re.finditer(r'(?:src|href)="([^"]*)"', text):
        protected.append((m.start(1), m.end(1)))

    # Sort and merge overlapping
    protected.sort(key=lambda x: x[0])
    merged = []
    for s, e in protected:
        if merged and s <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], e))
        else:
            merged.append([s, e])

    return merged


def is_protected(pos, protected_spans):
    """Check if position is inside any protected span."""
    for s, e in protected_spans:
        if s <= pos < e:
            return True
    return False


def parse_frontmatter(text):
    """
    Return (frontmatter_text, body_text, fm_start, fm_end) or (None, text, 0, 0).
    Only the title: field in frontmatter should be normalized.
    """
    if text.startswith('---'):
        end = text.find('\n---', 3)
        if end != -1:
            fm_end = end + 4  # include closing ---
            return text[:fm_end], text[fm_end:], 0, fm_end
    return None, text, 0, 0


# ---------------------------------------------------------------------------
# Replacement rules
# ---------------------------------------------------------------------------

# Each rule: (pattern, replacement, description, exclude_patterns)
# exclude_patterns: list of regexes — if matched in context, skip this replacement

RULES = [
    # course → programme (except "of course")
    # We'll handle "of course" by protecting it first
    ("\\bcourses\\b", "programmes", "courses→programmes", []),
    ("\\bCourses\\b", "Programmes", "Courses→Programmes", []),
    ("\\bcourse\\b", "programme", "course→programme", [r'\bof\s+course\b']),
    ("\\bCourse\\b", "Programme", "Course→Programme", [r'\bof\s+Course\b', r'\bof\s+course\b']),

    # group → class (with exceptions)
    ("\\bgroups\\b", "classes", "groups→classes", [
        r'\btarget\s+groups?\b', r'\bage\s+groups?\b',
        r'\bGroup\s+classes\b', r'\bGroup\s+capacity\b', r'\bGroup\s+[Cc]apacity\b',
        r'\bGroup\s+[Ss]ession\b', r'\bgroup\s+connection\b', r'\bGroup\s+[Cc]onnection\b',
        r'\blinked\s+classes\b',
    ]),
    ("\\bGroups\\b", "Classes", "Groups→Classes", [
        r'\bTarget\s+[Gg]roups?\b', r'\bAge\s+[Gg]roups?\b',
        r'\bGroup\s+[Cc]lasses\b', r'\bGroup\s+[Cc]apacity\b',
        r'\bGroup\s+[Ss]ession\b', r'\bGroup\s+[Cc]onnection\b',
    ]),
    ("\\bgroup\\b", "class", "group→class", [
        r'\btarget\s+group\b', r'\bage\s+group\b',
        r'\bGroup\s+[Cc]lasses\b', r'\bGroup\s+[Cc]apacity\b',
        r'\bGroup\s+[Ss]ession\b', r'\bgroup\s+connection\b',
        r'\bGroup\s+[Cc]onnection\b',
    ]),
    ("\\bGroup\\b", "Class", "Group→Class", [
        r'\bTarget\s+[Gg]roup\b', r'\bAge\s+[Gg]roup\b',
        r'\bGroup\s+[Cc]lasses\b', r'\bGroup\s+[Cc]apacity\b',
        r'\bGroup\s+[Ss]ession\b', r'\bGroup\s+[Cc]onnection\b',
    ]),

    # lesson → session (except "make-up lesson")
    ("\\blessons\\b", "sessions", "lessons→sessions", [r'\bmake-up\s+lessons?\b']),
    ("\\bLessons\\b", "Sessions", "Lessons→Sessions", [r'\bMake-up\s+[Ll]essons?\b']),
    ("\\blesson\\b", "session", "lesson→session", [r'\bmake-up\s+lesson\b']),
    ("\\bLesson\\b", "Session", "Lesson→Session", [r'\bMake-up\s+[Ll]esson\b']),

    # customer → client
    ("\\bcustomers\\b", "clients", "customers→clients", []),
    ("\\bCustomers\\b", "Clients", "Customers→Clients", []),
    ("\\bcustomer\\b", "client", "customer→client", [r'\bKeep\s+customer\s+in\s+auto-enrollment\b']),
    ("\\bCustomer\\b", "Client", "Customer→Client", [r'\bKeep\s+[Cc]ustomer\s+in\s+[Aa]uto-enrollment\b']),

    # Parent Portal / Parent Zone → Client Profile
    ("Parent Portal", "Client Profile", "Parent Portal→Client Profile", []),
    ("parent portal", "Client Profile", "parent portal→Client Profile", []),
    ("Parent Zone", "Client Profile", "Parent Zone→Client Profile", []),
    ("parent zone", "Client Profile", "parent zone→Client Profile", []),

    # auto-continuation → auto-enrolment
    ("auto-continuation", "auto-enrolment", "auto-continuation→auto-enrolment", []),
    ("Auto-continuation", "Auto-enrolment", "Auto-continuation→Auto-enrolment", []),
    ("Auto-Continuation", "Auto-Enrolment", "Auto-Continuation→Auto-Enrolment", []),

    # auto-enrollment → auto-enrolment (except in slug/filename context)
    ("auto-enrollment", "auto-enrolment", "auto-enrollment→auto-enrolment", []),
    ("Auto-Enrollment", "Auto-Enrolment", "Auto-Enrollment→Auto-Enrolment", [
        r'\bKeep\s+customer\s+in\s+Auto-Enrollment\b',
        r'\bKeep\s+[Cc]lient\s+in\s+Auto-Enrollment\b',
    ]),

    # sign in → log in (preserve "Sign in button")
    ("\\bsign in\\b", "log in", "sign in→log in", [r'\bSign\s+in\s+button\b', r'\bsign\s+in\s+button\b']),
    ("\\bSign in\\b", "Log in", "Sign in→Log in", [r'\bSign\s+in\s+button\b']),
    ("\\bSign In\\b", "Log In", "Sign In→Log In", [r'\bSign\s+[Ii]n\s+[Bb]utton\b']),
    ("\\bsigned in\\b", "logged in", "signed in→logged in", []),
    ("\\bSigned in\\b", "Logged in", "Signed in→Logged in", []),

    # trainer → instructor (except "trainer availability")
    ("\\btrainers\\b", "instructors", "trainers→instructors", [r'\btrainer\s+availability\b', r'\bTrainer\s+availability\b']),
    ("\\bTrainers\\b", "Instructors", "Trainers→Instructors", [r'\b[Tt]rainer\s+[Aa]vailability\b']),
    ("\\btrainer\\b", "instructor", "trainer→instructor", [r'\btrainer\s+availability\b', r'\bTrainer\s+[Aa]vailability\b']),
    ("\\bTrainer\\b", "Instructor", "Trainer→Instructor", [r'\b[Tt]rainer\s+[Aa]vailability\b']),

    # registration form → booking form
    ("\\bregistration forms?\\b", "booking form", "registration form→booking form", [
        r'\bregistration\s+fee\b', r'\bRegistration\s+[Ff]ee\b',
        r'\bonline\s+registration\b', r'\bOnline\s+[Rr]egistration\b',
        r'\bregistration\s+widget\b', r'\bRegistration\s+[Ww]idget\b',
    ]),
    ("\\bRegistration [Ff]orms?\\b", "Booking Form", "Registration Form→Booking Form", [
        r'\b[Rr]egistration\s+[Ff]ee\b',
        r'\b[Oo]nline\s+[Rr]egistration\b',
        r'\b[Rr]egistration\s+[Ww]idget\b',
    ]),

    # catch-up lesson → make-up session
    ("\\bcatch-up lessons?\\b", "make-up session", "catch-up lesson→make-up session", []),
    ("\\bCatch-up lessons?\\b", "Make-up session", "Catch-up lesson→Make-up session", []),
    ("\\bcatch-up sessions?\\b", "make-up sessions", "catch-up sessions→make-up sessions", []),
    ("\\bCatch-up sessions?\\b", "Make-up sessions", "Catch-up sessions→Make-up sessions", []),

    # replacement lesson → make-up session
    ("\\breplacement lessons?\\b", "make-up session", "replacement lesson→make-up session", []),
    ("\\bReplacement lessons?\\b", "Make-up session", "Replacement lesson→Make-up session", []),

    # replacement hour → make-up session
    ("\\breplacement hours?\\b", "make-up session", "replacement hour→make-up session", []),
    ("\\bReplacement hours?\\b", "Make-up session", "Replacement hour→Make-up session", []),

    # replacement sessions → make-up sessions (catch-all for replacement sessions)
    ("\\breplacement sessions?\\b", "make-up session", "replacement session→make-up session", []),
    ("\\bReplacement sessions?\\b", "Make-up session", "Replacement session→Make-up session", []),

    # course fee → term payment
    ("\\bcourse fees?\\b", "term payment", "course fee→term payment", []),
    ("\\bCourse fees?\\b", "Term payment", "Course fee→Term payment", []),
    ("\\bCourse Fees?\\b", "Term Payment", "Course Fee→Term Payment", []),

    # term fee → term payment
    ("\\bterm fees?\\b", "term payment", "term fee→term payment", []),
    ("\\bTerm fees?\\b", "Term payment", "Term fee→Term payment", []),
    ("\\bTerm Fees?\\b", "Term Payment", "Term Fee→Term Payment", []),
]

# ---------------------------------------------------------------------------
# Frontmatter-specific rules (title: line only)
# ---------------------------------------------------------------------------

FM_RULES = [
    ("\\bcourses\\b", "programmes"),
    ("\\bCourses\\b", "Programmes"),
    ("\\bcourse\\b", "programme"),
    ("\\bCourse\\b", "Programme"),
    ("\\bgroups\\b", "classes"),
    ("\\bGroups\\b", "Classes"),
    ("\\bgroup\\b", "class"),
    ("\\bGroup\\b", "Class"),
    ("\\blessons\\b", "sessions"),
    ("\\bLessons\\b", "Sessions"),
    ("\\blesson\\b", "session"),
    ("\\bLesson\\b", "Session"),
    ("\\bcustomers\\b", "clients"),
    ("\\bCustomers\\b", "Clients"),
    ("\\bcustomer\\b", "client"),
    ("\\bCustomer\\b", "Client"),
    ("Parent Portal", "Client Profile"),
    ("parent portal", "Client Profile"),
    ("Parent Zone", "Client Profile"),
    ("parent zone", "Client Profile"),
    ("auto-continuation", "auto-enrolment"),
    ("Auto-continuation", "Auto-enrolment"),
    ("Auto-Continuation", "Auto-Enrolment"),
    ("auto-enrollment", "auto-enrolment"),
    ("Auto-Enrollment", "Auto-Enrolment"),
    ("\\bsign in\\b", "log in"),
    ("\\bSign in\\b", "Log in"),
    ("\\bSign In\\b", "Log In"),
    ("\\btrainers\\b", "instructors"),
    ("\\bTrainers\\b", "Instructors"),
    ("\\btrainer\\b", "instructor"),
    ("\\bTrainer\\b", "Instructor"),
    ("\\bregistration forms?\\b", "booking form"),
    ("\\bRegistration [Ff]orms?\\b", "Booking Form"),
    ("\\bcatch-up lessons?\\b", "make-up session"),
    ("\\breplacement lessons?\\b", "make-up session"),
    ("\\breplacement hours?\\b", "make-up session"),
    ("\\bcourse fees?\\b", "term payment"),
    ("\\bCourse fees?\\b", "Term payment"),
    ("\\bCourse Fees?\\b", "Term Payment"),
    ("\\bterm fees?\\b", "term payment"),
    ("\\bTerm fees?\\b", "Term payment"),
    ("\\bTerm Fees?\\b", "Term Payment"),
]

# ---------------------------------------------------------------------------
# Apply replacements to a single text segment
# ---------------------------------------------------------------------------

def apply_rules_to_text(text, rules, protected_spans):
    """Apply replacement rules to text, skipping protected spans."""
    replacements_made = []

    for pattern, replacement, desc, exclude_patterns in rules:
        # Compile pattern
        try:
            compiled = re.compile(pattern)
        except re.error:
            compiled = re.compile(re.escape(pattern))

        new_text = ""
        last_end = 0
        changed = False

        for m in compiled.finditer(text):
            start, end = m.start(), m.end()

            # Skip if in protected region
            if any(ps <= start < pe or ps < end <= pe for ps, pe in protected_spans):
                new_text += text[last_end:end]
                last_end = end
                continue

            # Check exclude patterns — look at context window around match
            context_start = max(0, start - 50)
            context_end = min(len(text), end + 50)
            context = text[context_start:context_end]

            skip = False
            for excl in exclude_patterns:
                if re.search(excl, context, re.IGNORECASE):
                    skip = True
                    break

            if skip:
                new_text += text[last_end:end]
                last_end = end
                continue

            # Apply replacement
            new_text += text[last_end:start] + replacement
            last_end = end
            changed = True
            replacements_made.append((desc, m.group(0), replacement))

        new_text += text[last_end:]
        if changed:
            text = new_text
            # Recompute protected spans after text change — approximate (lengths may shift)
            # For simplicity, recompute from scratch for subsequent rules
            protected_spans = split_protected_regions(text)

    return text, replacements_made


def normalize_frontmatter_title(fm_text):
    """Normalize only the title: line in frontmatter."""
    lines = fm_text.split('\n')
    replacements = []
    new_lines = []
    for line in lines:
        if line.startswith('title:'):
            original = line
            for pattern, replacement in FM_RULES:
                try:
                    compiled = re.compile(pattern)
                except re.error:
                    compiled = re.compile(re.escape(pattern))
                line = compiled.sub(replacement, line)
            if line != original:
                replacements.append(("title normalization", original.strip(), line.strip()))
        new_lines.append(line)
    return '\n'.join(new_lines), replacements


def normalize_file(filepath):
    """Process a single file. Returns (new_content, replacements_list) or (None, []) if no change."""
    text = filepath.read_text(encoding='utf-8')
    original = text

    # Parse frontmatter
    fm_text, body, fm_start, fm_end = parse_frontmatter(text)

    all_replacements = []

    # Normalize frontmatter title
    if fm_text:
        new_fm, fm_reps = normalize_frontmatter_title(fm_text)
        all_replacements.extend(fm_reps)
    else:
        new_fm = fm_text

    # Compute protected spans for body
    body_protected = split_protected_regions(body)

    # Apply rules to body
    new_body, body_reps = apply_rules_to_text(body, RULES, body_protected)
    all_replacements.extend(body_reps)

    # Reconstruct
    if fm_text:
        new_text = new_fm + new_body
    else:
        new_text = new_body

    if new_text != original:
        return new_text, all_replacements
    return None, []


# ---------------------------------------------------------------------------
# Flag items
# ---------------------------------------------------------------------------

FLAG_PATTERNS = [
    (r'\bregistration\b(?!\s+form|\s+fee|\s+widget)', "registration→booking candidate (context-sensitive)"),
    (r'\bevent\b', "event→session candidate (check if Zooza UI feature name)"),
]

def find_flags(filepath, text):
    """Find items that need manual review."""
    flags = []
    lines = text.split('\n')

    # Protected spans
    protected = split_protected_regions(text)

    for pattern, reason in FLAG_PATTERNS:
        compiled = re.compile(pattern, re.IGNORECASE)
        offset = 0
        for i, line in enumerate(lines, 1):
            for m in compiled.finditer(line):
                # Check if this is in a known exception
                ctx = line
                # Skip "online registration", "registration fee", "registration widget"
                if re.search(r'\bonline\s+registration\b|\bregistration\s+fee\b|\bregistration\s+widget\b',
                             ctx, re.IGNORECASE):
                    continue
                if re.search(r'\bregistration\s+form\b', ctx, re.IGNORECASE):
                    continue
                flags.append((str(filepath.name) + f":{i}", reason, line.strip()[:80]))

    # Special flag for king-of-a-group.md
    if filepath.name == 'king-of-a-group.md':
        flags.append((str(filepath.name), "King of Class vs King of a group — manual edit needed", ""))

    return flags


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    md_files = sorted(CONTENT_DIR.rglob("*.md"))

    files_scanned = 0
    files_modified = 0
    total_replacements = 0

    term_counts = defaultdict(lambda: {"count": 0, "files": set()})
    modified_files = {}
    all_flags = []

    for fp in md_files:
        files_scanned += 1
        new_content, reps = normalize_file(fp)

        # Collect flags
        read_text = fp.read_text(encoding='utf-8')
        flags = find_flags(fp, read_text)
        all_flags.extend(flags)

        if new_content is not None:
            fp.write_text(new_content, encoding='utf-8')
            files_modified += 1
            total_replacements += len(reps)

            file_reps = defaultdict(int)
            for desc, orig, repl in reps:
                term_counts[desc]["count"] += 1
                term_counts[desc]["files"].add(fp.name)
                file_reps[f'"{orig}" → "{repl}"'] += 1

            modified_files[fp.name] = dict(file_reps)

    # Write log
    log_lines = [
        "# Normalize Log",
        "",
        f"**Run:** {TODAY}",
        f"**Files scanned:** {files_scanned}",
        f"**Files modified:** {files_modified}",
        f"**Total replacements:** {total_replacements}",
        "",
        "## Replacements by term",
        "| From | To | Count | Files |",
        "|---|---|---|---|",
    ]

    for desc, data in sorted(term_counts.items(), key=lambda x: -x[1]["count"]):
        parts = desc.split("→")
        from_t = parts[0].strip() if len(parts) > 1 else desc
        to_t = parts[1].strip() if len(parts) > 1 else ""
        files_list = ", ".join(sorted(data["files"])[:5])
        if len(data["files"]) > 5:
            files_list += f" +{len(data['files'])-5} more"
        log_lines.append(f"| `{from_t}` | `{to_t}` | {data['count']} | {files_list} |")

    log_lines += [
        "",
        "## Modified files",
    ]

    for fname, reps in sorted(modified_files.items()):
        log_lines.append(f"### {fname}")
        for rep, count in sorted(reps.items()):
            log_lines.append(f"- {rep} ({count}x)")
        log_lines.append("")

    log_lines += [
        "## Items flagged for review",
    ]

    seen_flags = set()
    for flag_id, reason, context in all_flags:
        key = f"{flag_id}:{reason}"
        if key not in seen_flags:
            seen_flags.add(key)
            ctx_str = f' — `{context}`' if context else ''
            log_lines.append(f"- `{flag_id}` — {reason}{ctx_str}")

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    LOG_PATH.write_text('\n'.join(log_lines) + '\n', encoding='utf-8')

    print(f"Done. Scanned: {files_scanned}, Modified: {files_modified}, Replacements: {total_replacements}")
    print(f"Log written to: {LOG_PATH}")


if __name__ == "__main__":
    main()
