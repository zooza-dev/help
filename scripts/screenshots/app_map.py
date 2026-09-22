#!/usr/bin/env python3
"""Map the app's screens from source, then walk them in a browser.

Three commands:

    python3 scripts/screenshots/app_map.py build     # source -> build/app-map/app-map.yml
    python3 scripts/screenshots/app_map.py explore   # walk every screen, shoot it, flag staleness
    python3 scripts/screenshots/app_map.py fields    # walk every screen, read its form -> screens/*.json + screens.jsonl

`build` reads the sibling app repo (../app): the Settings menu in moduleconfig
and the English strings in lib/str_en3.js. Nothing is typed by hand, so when the
app gains a subpage the map gains a screen.

`explore` is the review pass, not the publishing pass. It signs in with the
session capture.py saved, visits each screen, and writes three things per screen
under build/app-map/: the screenshot, the page text, and a list of findings.
The findings are what "fresh and juicy" means in practice — an expired
integration, a red ERROR row, a raw translation key, an `undefined` — the stuff
that would teach a reader the product is broken if it went into the help.

`fields` is the layer the assistant answers from. Every setting in the app is a
Knockout form component (`.zooza_forms__*`) with a label, a control and a help
text — the grey line under the field that says what the switch actually does.
Reading those straight out of the DOM gives a per-screen reference of what can
be configured and what each option means, without anyone paraphrasing it into
an article. Output: build/app-map/screens/<id>.json and
build/exports/agent/screens.jsonl (one record per card, same metadata shape
as canonical.jsonl so the consumer needs no special case).

Only Settings is mapped for now. Add a section to SCOPE to grow it.
"""

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
APP = os.path.abspath(os.path.join(ROOT, "..", "app"))
OUT = os.path.join(ROOT, "build", "app-map")
SESSION = os.path.join(ROOT, "build", "intake", "zooza-session.json")
MODULECONFIG = os.path.join(APP, "lib", "moduleconfig", "moduleconfig.js")
STRINGS = os.path.join(APP, "lib", "str_en3.js")

BASE = "https://uk.zooza.app/"
CLIENT_BASE = "https://www.playfulmotion.co.uk/parent-zone"
CLIENT_SESSION = os.path.join(ROOT, "build", "intake", "zooza-client-session.json")
BLOCK = re.compile(r"(intercom|hotjar|googletagmanager|google-analytics|facebook\.net)")

# Things that mean the screen is not fit to publish. Each is (label, regex).
# Keep these literal-ish: a pattern that fires on every page is a pattern nobody reads.
STALE = [
    ("raw i18n key", re.compile(r"\b[a-z]+__[a-z_]+__[a-z_]+\b")),
    ("undefined/NaN", re.compile(r"\b(undefined|NaN|null)\b")),
    ("error row", re.compile(r"\b(ERROR|Error:|failed|Failed)\b")),
    ("expired/reconnect", re.compile(r"\b(expired|reconnect|re-authoris|Token refresh)\b", re.I)),
    ("mojibake", re.compile(r"â‚¬|Ã[a-z¡©­³º]|Â[ ]")),
    ("empty state", re.compile(r"\bNo [a-z -]+ yet\b|\bnothing (here|found)\b", re.I)),
    ("placeholder text", re.compile(r"\b(lorem ipsum|TODO|FIXME|test test|asdf)\b", re.I)),
]


def load_strings():
    """key -> English text, from the define() blob in str_en3.js."""
    out = {}
    with open(STRINGS, encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r"^([a-z0-9_]+)\s*:\s*'((?:[^'\\]|\\.)*)'", line)
            if m:
                out[m.group(1)] = m.group(2).replace("\\'", "'")
    return out


def settings_menu(src):
    """The subpage_groups block of the settings route -> [(group_key, [(subpage, title_key)])]."""
    start = src.index("url: 'settings/:subpage:/:dialog::?query:'")
    block = src[start:]
    block = block[block.index("subpage_groups:"):]
    block = block[: block.index("\n            },")]
    groups = []
    for g in re.finditer(r"title: msg\.get\('(settings__group__[a-z_]+)'\),\s*items: \[(.*?)\]", block, re.S):
        items = re.findall(r"title: msg\.get\('([a-z_]+)'\),\s*subpage: '([a-z_]+)'", g.group(2))
        groups.append((g.group(1), [(sp, key) for key, sp in items]))
    return groups


# Representative records in the Playfulmotion demo account. Programme and class
# detail screens need a real id; these were picked on 2026-09-20 because the
# programme has several classes with bookings. Swap them if they stop being typical.
REPRESENTATIVE = {"course": 150, "schedule": 230, "event": 22131,
                  "registration": 1486, "client": 1951, "order": 26, "contact": 1}

# Programme settings tiles (courses/:id/settings?edit=X) and class detail panels
# (courses/schedules/:id?edit=X). The tile list is what the app renders on the
# Settings tab; it is not declared in moduleconfig, so it is kept here with the
# English title key where one exists and a literal where the app uses the tile's
# own card heading.
PROGRAMME_TILES = [
    ("settings", "course_settings__card_course__title", "Programme settings"),
    ("price", "course_settings__card_price__title", "Price and Payment"),
    ("online_registration", "course_settings__card_registration__title", "Online booking"),
    ("replacements", "course_settings__card_replacements__title", "Make-up sessions"),
    ("additional_sessions", "course_settings__card_additional_sessions__title", "Additional sessions"),
    ("trial", "course_settings__card_trial__title", "Trial"),
    ("retention", "course_settings__card_retention__title", "Auto-enrolment"),
    ("attendance", None, "Attendance"),
    ("extra_fields", "course_settings__card_extra_fields__title", "Additional fields"),
    ("feedback", "course_settings__card_feedback__title", "Feedback"),
    ("schedule_groups", "course_settings__card_schedule_groups__title", "Class linking"),
    ("documents", None, "Documents"),
    ("videos", None, "Videos"),
    ("urls", None, "URLs"),
]
CLASS_PANELS = [
    ("settings", "Settings"), ("trainers", "Instructors"), ("products", "Products"), ("report", "Report"),
    ("price", "Pricing"), ("payment_schedules", "Payment plans"), ("add_scheduled_payment", "Add scheduled payment"),
    ("documents", "Documents"), ("videos", "Videos"), ("urls", "URLs"), ("replacements", "Make-up sessions"),
    ("add_events", "Add sessions"),
]


def programme_screens(strings):
    c, sch, ev = REPRESENTATIVE["course"], REPRESENTATIVE["schedule"], REPRESENTATIVE["event"]
    P, roles = "Activities → Programmes", ["owner", "assistant", "receptionist", "main_trainer"]

    def screen(sid, menu, route, title, prefixes=()):
        n = sum(1 for k in strings if any(k.startswith(p) for p in prefixes))
        return {"id": sid, "menu": menu, "title": title, "route": route,
                "url_template": "https://{region}.zooza.app/#" + route, "roles": roles,
                "string_prefixes": list(prefixes), "strings": n, "area": "programmes"}

    out = [
        screen("programmes.list", P, "courses", "Programmes", ("courses__",)),
        screen("programmes.create", f"{P} → New programme", "courses/create?product_type=course", "New programme", ("courses_create__",)),
        screen("programmes.overview", f"{P} → programme → Overview", f"courses/{c}", "Overview", ("course_detail__",)),
        screen("programmes.settings", f"{P} → programme → Settings", f"courses/{c}/settings", "Settings", ("course_settings__",)),
    ]
    for tile, key, fallback in PROGRAMME_TILES:
        title = strings.get(key, fallback) if key else fallback
        out.append(screen(f"programmes.settings.{tile}", f"{P} → programme → Settings → {title}",
                          f"courses/{c}/settings?edit={tile}", title, (f"course_settings__{tile}__", f"course_settings__card_{tile}__")))
    out += [
        screen("programmes.automations", f"{P} → programme → Automations", f"courses/{c}/automations", "Automations", ("automations__",)),
        screen("programmes.add_class", f"{P} → programme → New class", f"courses/{c}/add_schedule", "New class", ("add_schedule__",)),
        screen("programmes.copy", f"{P} → programme → Copy", f"courses/{c}/copy", "Copy programme", ("copy_course__",)),
        screen("classes.list", "Activities → Classes", "courses/schedules", "Classes", ("schedules__",)),
        screen("classes.detail", "Activities → Classes → class", f"courses/schedules/{sch}", "Class detail", ("schedules_detail__", "schedule_detail__")),
    ]
    for panel, title in CLASS_PANELS:
        out.append(screen(f"classes.detail.{panel}", f"Activities → Classes → class → {title}",
                          f"courses/schedules/{sch}?edit={panel}", title, (f"schedules_detail__{panel}__",)))
    out += [
        screen("classes.copy", "Activities → Classes → class → Copy class", f"courses/schedules/{sch}/copy", "Copy class", ("copy_schedule__",)),
        screen("sessions.list", "Activities → Sessions", "courses/events", "Sessions", ("events__",)),
        screen("sessions.detail", "Activities → Sessions → session", f"courses/events/{ev}", "Session detail", ("events_detail__", "event_detail__")),
    ]
    F = "Products & Services → Documents"
    out += [
        screen("files.list", F, "files", "Documents", ("files__",)),
        screen("files.add_new", f"{F} → Add new", "files/add_new", "New document", ("files__", "new_file_template__")),
        screen("files.document", f"{F} → document", "files/document/3", "Document detail", ("document_detail__",)),
        screen("files.dynamic_document", f"{F} → dynamic document", "files/dynamic_document/1", "Dynamic document", ("dynamic_document__",)),
        screen("files.video", f"{F} → video", "files/video/1103388481", "Video detail", ("video_detail__",)),
    ]
    for o in out[-5:]:
        o["area"] = "files"

    r, cl, od, ct = (REPRESENTATIVE[k] for k in ("registration", "client", "order", "contact"))
    B, C = "Clients → Bookings", "Clients → Clients"
    booking_tabs = [("payments", "Payments"), ("invoices", "Invoices"), ("payment_plan", "Payment plan"),
                    ("attendance", "Attendance"), ("credits", "Credits and make-up sessions")]
    booking_dialogs = [("?edit=status", "Change status"), ("?edit=cancel_registration", "Cancel booking"),
                       ("/change?action=move", "Move booking"), ("/change?action=copy", "Copy booking"),
                       ("/network_transfer", "Transfer to network"), ("/credits?action=create_credit", "Add credit")]
    more = [
        screen("bookings.list", B, "registrations", "Bookings", ("registrations__",)),
        screen("bookings.create", f"{B} → Create booking", "registrations/create", "Create booking", ("create_registration__",)),
        screen("bookings.detail", f"{B} → booking", f"registrations/{r}", "Booking detail", ("registration_detail__",)),
    ]
    more += [screen(f"bookings.detail.{tab}", f"{B} → booking → {title}", f"registrations/{r}/{tab}", title, (f"registration_{tab}__",))
             for tab, title in booking_tabs]
    more += [screen(f"bookings.detail.{re.sub(r'[^a-z]+', '_', path.strip('/?').lower()).strip('_')}", f"{B} → booking → {title}",
                    f"registrations/{r}{path}", title, ()) for path, title in booking_dialogs]
    more += [
        screen("clients.list", C, "clients", "Clients", ("clients__",)),
        screen("clients.import", f"{C} → Import", "clients/import", "Import clients", ("import__",)),
        screen("clients.detail", f"{C} → client", f"clients/{cl}", "Client detail", ("client_detail__", "clients__")),
        screen("orders.list", "Clients → Orders", "orders", "Orders", ("orders__",)),
        screen("orders.detail", "Clients → Orders → order", f"orders/{od}", "Order detail", ("order_detail__",)),
        screen("orders.detail.payments", "Clients → Orders → order → Payments", f"orders/{od}/payments", "Order payments", ()),
        screen("contacts.list", "Clients → Contacts", "contacts", "Contacts", ("contacts__",)),
        screen("contacts.detail", "Clients → Contacts → contact", f"contacts/{ct}", "Contact detail", ("contacts__",)),
    ]
    for o in more:
        o["area"] = "bookings" if o["id"].startswith("bookings.") else "clients"

    # The rest of the admin sidebar, read off the live menu on 2026-09-21. (area, id, menu, route, title, prefixes)
    rest = [
        ("payments", "payments.overview", "Sales & Payments → Payments", "payments", "Payments", ("payments__",)),
        ("payments", "payments.import", "Sales & Payments → Payments → Import", "payments/import", "Import payments", ("payments__import__", "import_payments__")),
        ("payments", "payments.refunds.requests", "Sales & Payments → Refunds → Requests", "payments/refunds/requests", "Refund requests", ("refunds__", "refund_requests__")),
        ("payments", "payments.refunds.issued", "Sales & Payments → Refunds → Issued", "payments/refunds/issued", "Issued refunds", ("refunds__",)),
        ("payments", "payments.mandates", "Sales & Payments → Direct Debit mandates", "payments/mandates", "Direct Debit mandates", ("mandates__",)),
        ("payments", "payments.transactions.cash_transfer", "Sales & Payments → Transactions → Cash & transfer", "payments/transactions/cash_transfer", "Cash & transfer", ("transactions__",)),
        ("payments", "payments.transactions.card", "Sales & Payments → Transactions → Card", "payments/transactions/card", "Card", ("transactions__",)),
        ("payments", "payments.transactions.direct_debit", "Sales & Payments → Transactions → Direct debit", "payments/transactions/direct_debit", "Direct debit", ("transactions__",)),
        ("payments", "payments.transactions.import", "Sales & Payments → Transactions → Import payments", "payments/transactions/import", "Import payments", ("transactions__",)),
        ("payments", "payments.inbound.queue", "Sales & Payments → Payment reconciliation → Queue", "payments/inbound/queue", "Queue", ("inbound__",)),
        ("payments", "payments.inbound.rules", "Sales & Payments → Payment reconciliation → AI rules & filters", "payments/inbound/rules", "AI rules & filters", ("inbound__",)),
        ("payments", "payments.inbound.analytics", "Sales & Payments → Payment reconciliation → AI analytics", "payments/inbound/analytics", "AI analytics", ("inbound__",)),
        ("payments", "payments.scheduled", "Sales & Payments → Scheduled payments overview", "payments/scheduled", "Scheduled payments overview", ("scheduled_payments__",)),
        ("payments", "payments.discounts", "Sales & Payments → Discounts", "payments/discounts", "Discounts", ("coupons__", "discounts__")),
        ("payments", "payments.loyalty", "Sales & Payments → Loyalty Programme", "payments/loyalty", "Loyalty Programme", ("loyalty__",)),
        ("payments", "payments.invoices", "Sales & Payments → Invoices", "payments/invoices", "Invoices", ("invoices__",)),
        ("payments", "payments.invoices.detail", "Sales & Payments → Invoices → invoice", "payments/invoices/26", "Invoice detail", ("invoice_detail__",)),
        ("products", "products.list", "Products & Services → ProductsPRO", "products", "Products", ("products__",)),
        ("products", "services.list", "Products & Services → Services", "services", "Services", ("services__",)),
        ("communication", "communication.compose", "Communication → Send message", "communication/compose", "Send message", ("communication__compose__", "communication__")),
        ("communication", "communication.history", "Communication → History", "communication/sent_communication", "History", ("communication__history__",)),
        ("communication", "communication.message_jobs", "Communication → Message Jobs", "communication/message_jobs", "Message Jobs", ("message_jobs__",)),
        ("communication", "communication.templates", "Communication → Templates", "communication/templates", "Templates", ("communication__templates__", "templates__")),
        ("communication", "communication.whatsapp", "Communication → WhatsApp", "communication/whatsapp", "WhatsApp", ("whatsapp__",)),
        ("calendar", "calendar.week", "Activities → Calendar", "calendar", "Calendar", ("calendar__",)),
        ("calendar", "calendar.daily", "Activities → Calendar → Daily overview", "calendar/daily", "Daily overview", ("calendar__daily__",)),
        ("calendar", "calendar.planner", "Activities → Calendar → Planning calendar", "calendar/planner", "Planning calendar", ("calendar__planner__", "planner__")),
        ("calendar", "feedback.nps", "Feedback → NPS", "feedback/nps", "NPS", ("nps__", "feedback__")),
        ("calendar", "feedback.reviews", "Feedback → Reviews", "feedback/reviews", "Reviews", ("reviews__",)),
        ("calendar", "feedback.submissions", "Feedback → Submissions", "feedback/submissions", "Submissions", ("feedback__submissions__",)),
        ("reports", "reports.dashboard", "Reports & Insights → Dashboard", "reports", "Dashboard", ("dashboard__",)),
        ("reports", "reports.registrations", "Reports & Insights → Reports → Bookings", "reports/registrations", "Bookings report", ("reports__",)),
        ("reports", "reports.trials", "Reports & Insights → Reports → Trial Sessions Report", "reports/trials", "Trial Sessions Report", ("reports__",)),
        ("reports", "reports.outstanding_payments", "Reports & Insights → Reports → Outstanding Payments", "reports/outstanding_payments", "Outstanding Payments", ("reports__",)),
        ("reports", "reports.replacements", "Reports & Insights → Reports → Make-up sessions", "reports/replacements", "Make-up sessions report", ("reports__",)),
        ("reports", "reports.additional_sessions", "Reports & Insights → Reports → Additional sessions", "reports/additional_sessions", "Additional sessions report", ("reports__",)),
        ("reports", "reports.rescheduled", "Reports & Insights → Reports → Rescheduled", "reports/rescheduled", "Rescheduled", ("reports__",)),
        ("reports", "reports.substituted", "Reports & Insights → Reports → Substituted", "reports/substituted", "Substituted", ("reports__",)),
        ("reports", "reports.cancelled", "Reports & Insights → Reports → Cancelled", "reports/cancelled", "Cancelled", ("reports__",)),
        ("reports", "reports.event_notifications", "Reports & Insights → Reports → Session notifications (not in the menu)", "reports/event_notifications", "Session notifications", ("event_notifications__",)),
        ("reports", "reports.system_messages", "Reports & Insights → System messages", "reports/system_messages", "System messages", ("system_messages__",)),
        ("team", "team.trainers", "Team & Settings → Instructors", "trainers", "Instructors", ("trainers__",)),
        ("team", "team.trainer.detail", "Team & Settings → Instructors → instructor", "trainers/60", "Instructor detail", ("trainer_detail__",)),
        ("team", "team.trainer.settings", "Team & Settings → Instructors → instructor → Settings", "trainers/60/trainer_settings", "Instructor settings", ("trainer_settings__",)),
        ("team", "team.trainer.availability", "Team & Settings → Instructors → instructor → Availability", "trainers/60/availability", "Availability", ("trainer_availability__",)),
        ("team", "team.publish", "Team & Settings → Publish", "widgets", "Publish", ("widgets__", "settings__widgets__")),
        ("team", "team.integrations", "Team & Settings → Integrations", "integrations", "Integrations", ("settings__integrations__", "integrations__")),
        ("team", "team.mcp", "Zooza AI Assistant", "mcp", "Zooza AI Assistant", ("mcp__",)),
    ]
    for area, sid, menu, route, title, prefixes in rest:
        o = screen(sid, menu, route, title, prefixes)
        o["area"] = area
        more.append(o)

    # The client zone (parent-facing widget) lives on the customer's own site, not on zooza.app.
    # Demo: Playfulmotion's parent zone, family Tanase; booking 666 is a trial, 517 a paid enrolment.
    CZ, base = "Client zone", CLIENT_BASE
    client = [
        ("client.dashboard", CZ, "dashboard", "Dashboard"),
        ("client.registrations", f"{CZ} → Registrations", "registrations", "Registrations"),
        ("client.payments", f"{CZ} → Payments", "payments", "Payments"),
        ("client.orders", f"{CZ} → Orders", "orders", "Orders"),
        ("client.referrals", f"{CZ} → Referrals", "referrals", "Referrals"),
        ("client.booking.overview", f"{CZ} → booking → Overview", "course_detail/517", "Booking overview"),
        ("client.booking.attendance", f"{CZ} → booking → Attendance", "course_detail/517/events", "Attendance"),
        ("client.booking.detail", f"{CZ} → booking → Detail", "course_detail/517/detail", "Detail"),
        ("client.booking.payments", f"{CZ} → booking → Payments", "course_detail/517/payments", "Payments"),
        ("client.booking.find_event", f"{CZ} → booking → Book session", "course_detail/517/find_event", "Book a session"),
        ("client.trial.overview", f"{CZ} → trial booking → Overview", "course_detail/666", "Trial booking overview"),
        ("client.order", f"{CZ} → Orders → order", "order/21", "Order"),
    ]
    for sid, menu, route, title in client:
        more.append({"id": sid, "menu": menu, "title": title, "route": route,
                     "url_template": base + "#" + route, "roles": ["client"],
                     "string_prefixes": [], "strings": 0, "area": "client", "base": base, "root": ".zooza-host"})
    return out + more


def build():
    import yaml
    strings = load_strings()
    with open(MODULECONFIG, encoding="utf-8") as fh:
        src = fh.read()

    screens = []
    for group_key, items in settings_menu(src):
        group = strings.get(group_key, group_key)
        for subpage, title_key in items:
            title = strings.get(title_key, title_key)
            # string prefixes vary: labels_settings -> settings__labels__, trainers_settings -> settings__trainers__
            stem = subpage.replace("_settings", "")
            prefixes = sorted({p for p in (f"settings__{subpage}__", f"settings__{stem}__") if any(k.startswith(p) for k in strings)})
            n = sum(1 for k in strings if any(k.startswith(p) for p in prefixes))
            screens.append({
                "id": f"settings.{subpage}",
                "menu": f"Settings → {group} → {title}",
                "title": title,
                "route": f"settings/{subpage}",
                "url_template": f"https://{{region}}.zooza.app/#settings/{subpage}",
                "roles": ["owner", "assistant"],
                "string_prefixes": prefixes,
                "strings": n,
                "area": "settings",
            })
    screens += programme_screens(strings)

    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, "app-map.yml")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("# Generated by scripts/screenshots/app_map.py build — do not hand-edit.\n")
        fh.write(f"# Source: ../app moduleconfig.js + str_en3.js ({len(strings)} EN strings)\n")
        yaml.safe_dump({"base": BASE, "screens": screens}, fh, allow_unicode=True, sort_keys=False)
    print(f"{len(screens)} screens -> {path}")
    for s in screens:
        print(f"  {s['route']:40} {s['strings']:4} strings  {s['menu']}")
    return 0


def goto(pg, doc, s):
    """Open a screen: admin screens hang off doc['base'] + '#route', client-zone screens carry their own base."""
    base = s.get("base") or doc["base"]
    url = f"{base}#{s['route']}" if s.get("base") else f"{base}#{s['route']}"
    pg.goto(url, timeout=60000)
    pg.wait_for_timeout(s.get("wait", 8000))


def session_for(screens):
    """One browser context per session file; client-zone screens use the parent session."""
    if all(s.get("area") == "client" for s in screens):
        return CLIENT_SESSION
    if any(s.get("area") == "client" for s in screens):
        sys.exit("mix of admin and client screens — run --area client separately")
    return SESSION


def explore(only, area=None):
    import yaml
    from playwright.sync_api import sync_playwright
    doc = yaml.safe_load(open(os.path.join(OUT, "app-map.yml"), encoding="utf-8"))
    screens = doc["screens"]
    if only:
        screens = [s for s in screens if s["id"] == only or s["route"] == only]
    if area:
        screens = [s for s in screens if s.get("area") == area]
    sess = session_for(screens)
    if not os.path.exists(sess):
        sys.exit(f"no session at {sess} — run capture.py --login <magic-link> first")
    shots, texts = os.path.join(OUT, "shots"), os.path.join(OUT, "text")
    os.makedirs(shots, exist_ok=True)
    os.makedirs(texts, exist_ok=True)

    report = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": 1600, "height": 1000}, device_scale_factor=2,
                            color_scheme="light", storage_state=sess)
        ctx.route(BLOCK, lambda r: r.abort())
        pg = ctx.new_page()
        for s in screens:
            name = s["id"]
            row = {"id": name, "route": s["route"], "status": "ok", "findings": []}
            try:
                goto(pg, doc, s)
                text = pg.inner_text(s.get("root", "body"))
                with open(os.path.join(texts, name + ".txt"), "w", encoding="utf-8") as fh:
                    fh.write(text)
                if "Page not found" in text:
                    row["status"] = "BAD ROUTE"
                else:
                    for label, rx in STALE:
                        hits = sorted({m.group(0) for m in rx.finditer(text)})[:5]
                        if hits:
                            row["findings"].append(f"{label}: {', '.join(hits)}")
                    # a screen with nothing on it is a finding too — usually empty demo data
                    body = text.split("\n")
                    if len([l for l in body if l.strip()]) < 25:
                        row["findings"].append(f"thin page: {len(body)} lines")
                    out = os.path.join(shots, name + ".png")
                    try:
                        pg.screenshot(path=out, full_page=True, timeout=15000)
                    except Exception:  # noqa: BLE001 — full_page can hang on "waiting for fonts"; the viewport is still worth having
                        pg.screenshot(path=out, timeout=15000)
                        row["findings"].append("viewport only (full-page shot timed out)")
                    row["screenshot"] = f"shots/{name}.png"
            except Exception as exc:  # noqa: BLE001
                row["status"] = "ERROR"
                row["findings"].append(f"{type(exc).__name__}: {exc}"[:120])
            report.append(row)
            flag = "  " if row["status"] == "ok" and not row["findings"] else "!!"
            print(f"{flag} {name:36} {row['status']:9} {'; '.join(row['findings'])}")
        b.close()

    with open(os.path.join(OUT, "explore-report.json"), "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=2, ensure_ascii=False)
    flagged = [r for r in report if r["status"] != "ok" or r["findings"]]
    print(f"\n{len(report)} screens, {len(flagged)} flagged — shots in {shots}, report in {OUT}/explore-report.json")
    return 0


FIELDS_JS = r"""
() => {
  const clean = (t) => (t || '').replace(/\s+/g, ' ').trim();
  const helpOf = (el) => {
    // the field's own help is the last .form_item_help that is a direct child of its .form_item
    const item = el.querySelector(':scope > .form_item, :scope > .z2.form_item') || el.querySelector('.form_item');
    if (!item) return '';
    const hs = [...item.children].filter(c => c.classList.contains('form_item_help'));
    const h = hs.length ? hs[hs.length - 1] : item.querySelector('.form_item_help');
    return h && h.offsetParent !== null ? clean(h.textContent) : (h ? clean(h.textContent) : '');
  };
  const fieldOf = (el) => {
    const cls = [...el.classList].find(c => c.startsWith('zooza_forms__')) || '';
    const type = cls.replace('zooza_forms__', '').replace(/^input_/, '');
    const label = clean(el.querySelector('.form_label')?.textContent);
    const f = { label, type, help: helpOf(el) };
    if (type.includes('radio')) {
      f.options = [...el.querySelectorAll('li label')].map(li => {
        const t = clean(li.querySelector('span')?.textContent);
        const h = li.querySelector('.form_item_help');
        const ht = h && h.textContent !== 'false' ? clean(h.textContent) : '';
        return ht ? `${t} — ${ht}` : t;
      }).filter(Boolean);
    }
    const sel = el.querySelector('select');
    if (sel) f.options = [...sel.options].map(o => clean(o.textContent)).filter(Boolean).slice(0, 40);
    if (type.includes('checkbox') && el.querySelector('.toggle')) f.type = 'toggle';
    return f;
  };
  const isField = (el) => [...el.classList].some(c => c.startsWith('zooza_forms__'));
  const outerFields = (root) => [...root.querySelectorAll('[class*="zooza_forms__"]')]
    .filter(el => isField(el) && !(el.parentElement.closest('[class*="zooza_forms__"]')));

  const cards = [];
  const seen = new Set();
  document.querySelectorAll('.card, section[class*="card"]').forEach(card => {
    const header = card.querySelector(':scope > .card_header');
    if (!header) return;
    const title = clean(header.textContent);
    // intro: paragraphs and plain text blocks that are not inside a field
    const intro = [...card.querySelectorAll('p, .card_form > div:not([class*="zooza_forms__"]):not(.form_item)')]
      .filter(e => !e.closest('[class*="zooza_forms__"]') && !e.closest('table') && e.children.length < 3)
      .map(e => clean(e.textContent)).filter(t => t.length > 25 && t.length < 600);
    const sections = [...card.querySelectorAll('h3, h4, summary, .accordion_title, [class*="collaps"] > a')]
      .filter(e => !e.closest('.card_header') && !e.closest('[class*="zooza_forms__"]'))
      .map(e => clean(e.textContent)).filter(t => t && t.length < 80);
    const fields = outerFields(card).map(el => { seen.add(el); return fieldOf(el); }).filter(f => f.label);
    const buttons = [...card.querySelectorAll('button, a.button, [class*="btn"]')]
      .map(e => clean(e.textContent)).filter(t => t && t.length < 40);
    cards.push({ title, intro: [...new Set(intro)].slice(0, 6), sections: [...new Set(sections)].slice(0, 30),
                 fields, buttons: [...new Set(buttons)].slice(0, 12) });
  });
  const loose = outerFields(document.body).filter(el => !seen.has(el)).map(fieldOf).filter(f => f.label);
  if (loose.length) cards.push({ title: '(page)', intro: [], sections: [], fields: loose, buttons: [] });
  const notes = [...document.querySelectorAll('[class*="info_box"], [class*="alert"], [class*="notice"], [class*="message_box"]')]
    .map(e => clean(e.textContent)).filter(t => t.length > 25 && t.length < 800);
  return { cards, notes: [...new Set(notes)].slice(0, 6) };
}
"""


EMAIL_RX = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RX = re.compile(r"(?<![\d/])\+?\d[\d ]{8,}\d(?![\d/])")
IBAN_RX = re.compile(r"\b[A-Z]{2}\d{2}[A-Z0-9 ]{10,30}\b")


def scrub(text):
    """The reference is about fields, not people. Whatever the demo account put in a field stays out."""
    text = EMAIL_RX.sub("client@example.com", text)
    text = re.sub(r"\b[A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+", "client@example.com", text)   # anything the strict form missed
    text = IBAN_RX.sub("GB00 BANK 0000 0000 0000 00", text)
    return PHONE_RX.sub("+44 7700 900000", text)



AREA_PRODUCT = {"client": "Clients", "settings": "Settings", "programmes": "Programmes", "classes": "Classes", "sessions": "Classes",
                "files": "Communication", "bookings": "Bookings", "clients": "Clients", "orders": "Orders", "contacts": "Clients",
                "payments": "Payments", "products": "Orders", "communication": "Communication", "calendar": "Calendar",
                "reports": "Settings", "team": "Settings"}


def area_of(screen):
    return screen.get("area") or screen["id"].split(".")[0]
EMAIL_IN_PARENS = re.compile(r"\s*\([^()]*@[^()]*\)")


def sanitise_title(title):
    """Row labels carry the row's identity — 'Amelia Hughes (amelia@…)'. Keep the role of the click, drop the person."""
    title = EMAIL_IN_PARENS.sub("", title).strip()
    return EMAIL_RX.sub("a client", title)


def record_for(screen, card, i):
    return {
        "doc_id": f"screen:{screen['id']}", "title": screen["menu"], "url": screen["url_template"],
        "type": "screen", "product_area": AREA_PRODUCT.get(area_of(screen), "Settings"), "sub_area": "",
        "tags": ["screen-reference", area_of(screen), screen["id"].split(".")[-1]],
        "audience": screen["roles"], "status": "published",
        "heading_path": sanitise_title(card["title"]), "source_path": f"build/app-map/screens/{screen['id']}.json",
        "route": card.get("route", screen["route"]), "text": card_text(screen, card),
    }


def write_jsonl():
    """Rebuild build/exports/agent/screens.jsonl from the per-screen JSON files. No browser needed."""
    outdir = os.path.join(OUT, "screens")
    export_dir = os.path.join(ROOT, "build", "exports", "agent")
    os.makedirs(export_dir, exist_ok=True)
    path = os.path.join(export_dir, "screens.jsonl")
    n = 0
    # Screens reached from the header on every page (My profile, Subscription) turn up under
    # whichever Settings screen the crawler was on. They are their own screens: keep one copy.
    header_screens = {"me": {"id": "me", "menu": "Header → My profile", "route": "me"},
                      "subscription": {"id": "subscription", "menu": "Header → Subscription & Billing", "route": "subscription"}}
    pulled = {}
    with open(path, "w", encoding="utf-8") as fh:
        for f in sorted(os.listdir(outdir)):
            d = json.load(open(os.path.join(outdir, f), encoding="utf-8"))
            shapes = set()
            for i, card in enumerate(d["cards"]):
                card["title"] = sanitise_title(card["title"])
                # nine payment templates open nine copies of the same form — one is enough
                shape = tuple((f["label"], f["type"]) for f in card["fields"])
                if card["fields"] and shape in shapes:
                    continue
                shapes.add(shape)
                top = card.get("route", "").split("/")[0].split("?")[0]
                if top in header_screens:
                    card["title"] = card["title"].split(" › ", 1)[-1]
                    pulled.setdefault(top, {})[card["title"]] = card
                    continue
                fh.write(json.dumps(record_for(d, card, i), ensure_ascii=False) + "\n")
                n += 1
        for top, cards in pulled.items():
            sc = {**header_screens[top], "url_template": "https://{region}.zooza.app/#" + top, "roles": ["owner", "assistant"]}
            for i, card in enumerate(cards.values()):
                fh.write(json.dumps(record_for(sc, card, i), ensure_ascii=False) + "\n")
                n += 1
    print(f"{n} card records -> {path}")
    return 0


# The parent-zone widget has no form components: sections are <h3>, fields are "<strong>Label:</strong> value",
# actions are buttons/links. Read it as (section → labels, help paragraphs, buttons).
CLIENT_FIELDS_JS = r"""
() => {
  const clean = (t) => (t || '').replace(/\s+/g, ' ').trim();
  const root = document.querySelector('.zooza-host') || document.body;
  const cards = [];
  let cur = { title: '(page)', intro: [], sections: [], fields: [], buttons: [] };
  const push = () => { if (cur.fields.length || cur.intro.length || cur.buttons.length) cards.push(cur); };
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_ELEMENT);
  let e;
  while ((e = walker.nextNode())) {
    if (e.offsetParent === null && e.tagName !== 'OPTION') continue;
    const tag = e.tagName;
    if (tag === 'H2' || tag === 'H3') { push(); cur = { title: clean(e.innerText), intro: [], sections: [], fields: [], buttons: [] }; continue; }
    if (tag === 'STRONG' && /:\s*$/.test(clean(e.innerText)) && !e.closest('button,a')) {
      const label = clean(e.innerText).replace(/:$/, '');
      if (label && !cur.fields.some(f => f.label === label)) cur.fields.push({ label, type: 'value', help: '' });
      continue;
    }
    if (tag === 'LABEL') { const l = clean(e.innerText); if (l && !cur.fields.some(f => f.label === l)) cur.fields.push({ label: l, type: e.querySelector('select') ? 'select' : 'input', help: '' }); continue; }
    if (tag === 'TH') { const l = clean(e.innerText); if (l && !cur.sections.includes(l)) cur.sections.push(l); continue; }
    if ((tag === 'BUTTON' || (tag === 'A' && e.getAttribute('href'))) && clean(e.innerText).length < 40) {
      const l = clean(e.innerText); if (l && !cur.buttons.includes(l)) cur.buttons.push(l); continue;
    }
    if (tag === 'P' && e.children.length < 2) { const t = clean(e.innerText); if (t.length > 25 && t.length < 500 && !cur.intro.includes(t)) cur.intro.push(t); }
  }
  push();
  return { cards, notes: [] };
}
"""
CLIENT_SAFE = re.compile(r"^(edit|details|open|more session dates|book session|change|choose|select|view all|filter|copy link|\u22ef more|more)$", re.I)


def client_clicks(pg, doc, s, before):
    """Click the widget's own safe actions (Edit, Change, Book session…) and read what opens. Never Pay / Enrol / Cancel."""
    known = {(c["title"], tuple(f["label"] for f in c["fields"])) for c in before}
    labels = [l for c in before for l in c["buttons"] if CLIENT_SAFE.match(l)]
    out = []
    for label in dict.fromkeys(labels):
        try:
            goto(pg, doc, s)
            el = pg.locator(".zooza-host button:visible, .zooza-host a:visible").filter(has_text=re.compile(rf"^\s*{re.escape(label)}\s*$")).first
            if el.count() == 0:
                continue
            el.click(timeout=5000); pg.wait_for_timeout(2500)
            for c in pg.evaluate(CLIENT_FIELDS_JS)["cards"]:
                key = (c["title"], tuple(f["label"] for f in c["fields"]))
                if key in known or not c["fields"]:
                    continue
                known.add(key); c["title"] = f"{label} › {c['title']}"; out.append(c)
        except Exception:  # noqa: BLE001
            continue
    return out


def card_text(screen, card):
    """One card as the assistant will read it."""
    url = screen["url_template"]
    if card.get("route") and screen.get("area") != "client":   # a sub-screen reached by clicking — link straight to it
        url = "https://{region}.zooza.app/#" + card["route"]
    lines = [f"{screen['menu']} › {sanitise_title(card['title'])}", f"URL: {url}"]
    for t in card.get("intro", []):
        lines.append(t)
    if card.get("sections") and not card.get("fields"):
        lines.append("Sections: " + "; ".join(card["sections"]))
    for f in card.get("fields", []):
        head = f"- {f['label']} ({f['type']})"
        if f.get("help"):
            head += f": {f['help']}"
        lines.append(head)
        for o in f.get("options", []):
            lines.append(f"    · {o}")
    if card.get("buttons"):
        lines.append("Buttons: " + ", ".join(card["buttons"]))
    return scrub("\n".join(lines))


# Buttons that open the create form on a list screen, in the order to try them.
ADD_BUTTONS = ["Add", "Add field", "New form", "Add rate", "Add new notification", "Create new billing period"]

# --deep clicks everything in the page area that is not one of these. Opening a form is
# safe; submitting, deleting or disconnecting is not — the demo account has a live Xero
# link and a real Stripe connection, and "Run setup again" is a wizard that writes.
DENY = re.compile(r"^(save|delete|remove|disconnect|sync now|resync|restore|download|regenerate|run setup|get authori|send|log ?out|upload|reset|clear|import|export|pay|checkout|cancel|close|back|submit|confirm|apply|duplicate|archive|activate|deactivate|discard|next|finish|continue|"
                  r"help & support|more|less|\+|-|\d+|transfer|refund|approve|reject|charge|mark |unsubscribe|resend|generate|issue|void|"
                  r"spam|merge|unlink|detach|revoke|block)", re.I)
CANDIDATES_JS = r"""
() => {
  const clean = (t) => (t || '').replace(/\s+/g, ' ').trim();
  const root = document.querySelector('.app_page_layout') || document.body;
  const out = []; const count = {};
  root.querySelectorAll('a, button, summary, [role=button]').forEach(e => {
    if (e.closest('.app_menu, .app_dock, .app_drawer, .breadcrumbs, .right_pane, .app_header, .card_header, [class*=zooza_forms__]')) return;
    if (e.offsetParent === null) return;
    const t = clean(e.innerText); if (!t || t.length > 45) return;
    const n = count[t] || 0; if (n >= 4) return;   // the same button on every row: four is plenty
    count[t] = n + 1; out.push([t, n]);
  });
  return out;
}
"""
MAX_CLICKS = 30


def deep_crawl(pg, base_url, route, base_cards):
    """Click every safe button/link on the screen once, from a fresh load each time.

    Returns (new_cards, discovered_routes). A click that changes the hash is a
    sub-screen: its cards are kept too, and the route is reported so it can be
    added to the map."""
    known = {(c["title"], tuple(f["label"] for f in c["fields"])) for c in base_cards}
    labels = [(t, n) for t, n in pg.evaluate(CANDIDATES_JS) if not DENY.match(t)][:MAX_CLICKS]
    new_cards, discovered = [], []
    for label, nth in labels:
        try:
            pg.goto(f"{base_url}#{route}", timeout=60000)
            pg.wait_for_timeout(7000)
            el = pg.locator(".app_page_layout a:visible, .app_page_layout button:visible, .app_page_layout summary:visible") \
                   .filter(has_text=re.compile(rf"^\s*{re.escape(label)}\s*$")).nth(nth)
            if el.count() == 0:
                continue
            el.click(timeout=8000)
            pg.wait_for_timeout(3000)
            here = pg.evaluate("() => location.hash.replace(/^#/, '')")
            if here.split("?")[0] != route and not here.startswith("verify"):
                discovered.append({"via": label, "route": here})
                if here.startswith("login") or "zooza.app" not in pg.url:
                    continue
            cards = pg.evaluate(FIELDS_JS)["cards"]
            for c in cards:
                key = (c["title"], tuple(f["label"] for f in c["fields"]))
                if key in known or not (c["fields"] or c["sections"]):
                    continue
                known.add(key)
                tag = label if nth == 0 else f"{label} #{nth + 1}"
                c["title"] = f"{tag} › {c['title']}" if c["title"] != "(page)" else tag
                if here.split("?")[0] != route:
                    c["route"] = here
                new_cards.append(c)
        except Exception as exc:  # noqa: BLE001
            discovered.append({"via": label, "error": f"{type(exc).__name__}"[:40]})
    return new_cards, discovered


def open_dialog(pg, before):
    """Click the screen's Add button if it has one and return the cards that appeared."""
    for label in ADD_BUTTONS:
        btn = pg.locator(f"a:visible, button:visible, summary:visible").filter(has_text=re.compile(rf"^\s*{re.escape(label)}\s*$")).first
        try:
            if btn.count() == 0:
                continue
            btn.click(timeout=3000)
        except Exception:  # noqa: BLE001
            continue
        pg.wait_for_timeout(2500)
        after = pg.evaluate(FIELDS_JS)["cards"]
        known = {(c["title"], len(c["fields"])) for c in before}
        new = [c for c in after if (c["title"], len(c["fields"])) not in known and c["fields"]]
        for c in new:
            c["title"] = f"{label} dialog › {c['title']}" if c["title"] != "(page)" else f"{label} dialog"
        return new
    return []


def fields(only, deep=False, area=None):
    import yaml
    from playwright.sync_api import sync_playwright
    doc = yaml.safe_load(open(os.path.join(OUT, "app-map.yml"), encoding="utf-8"))
    screens = doc["screens"]
    if only:
        screens = [s for s in screens if s["id"] == only or s["route"] == only]
    if area:
        screens = [s for s in screens if s.get("area") == area]
    sess = session_for(screens)
    if not os.path.exists(sess):
        sys.exit(f"no session at {sess} — run capture.py --login <magic-link> first")
    outdir = os.path.join(OUT, "screens")
    os.makedirs(outdir, exist_ok=True)
    export_dir = os.path.join(ROOT, "build", "exports", "agent")
    os.makedirs(export_dir, exist_ok=True)

    records, summary = [], []
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": 1600, "height": 1000}, storage_state=sess)
        ctx.route(BLOCK, lambda r: r.abort())
        pg = ctx.new_page()
        for s in screens:
            try:
                goto(pg, doc, s)
                if "Page not found" in pg.inner_text("body"):
                    summary.append((s["id"], "BAD ROUTE", 0, 0)); continue
                if s.get("area") == "client":
                    data = pg.evaluate(CLIENT_FIELDS_JS)
                    data["cards"] += client_clicks(pg, doc, s, data["cards"]) if deep else []
                    data = {"id": s["id"], "menu": s["menu"], "route": s["route"], "url_template": s["url_template"],
                            "roles": s["roles"], "area": "client", "captured": __import__("datetime").date.today().isoformat(), **data}
                    with open(os.path.join(outdir, s["id"] + ".json"), "w", encoding="utf-8") as fh:
                        json.dump(data, fh, indent=2, ensure_ascii=False)
                    summary.append((s["id"], "ok", len(data["cards"]), sum(len(c["fields"]) for c in data["cards"])))
                    for i, card in enumerate(data["cards"]):
                        records.append(record_for(s, card, i))
                    continue
                data = pg.evaluate(FIELDS_JS)
                # List screens keep their form in an Add dialog. Open it, read again, keep what is new.
                data["cards"] += open_dialog(pg, data["cards"])
                if deep:
                    more, found = deep_crawl(pg, doc["base"], s["route"], data["cards"])
                    data["cards"] += more
                    data["discovered"] = found
                for card in data["cards"]:   # an accordion per existing row repeats the same form — keep one
                    seen_f, uniq = set(), []
                    for f in card["fields"]:
                        key = (f["label"], f["type"], f["help"])
                        if key not in seen_f:
                            seen_f.add(key); uniq.append(f)
                    card["fields"] = uniq
            except Exception as exc:  # noqa: BLE001
                summary.append((s["id"], f"ERROR {type(exc).__name__}", 0, 0)); continue
            data = {"id": s["id"], "menu": s["menu"], "route": s["route"], "url_template": s["url_template"],
                    "roles": s["roles"], "area": s.get("area", "settings"), "captured": __import__("datetime").date.today().isoformat(), **data}
            with open(os.path.join(outdir, s["id"] + ".json"), "w", encoding="utf-8") as fh:
                json.dump(data, fh, indent=2, ensure_ascii=False)
            nf = sum(len(c["fields"]) for c in data["cards"])
            summary.append((s["id"], "ok", len(data["cards"]), nf))
            for i, card in enumerate(data["cards"]):
                records.append(record_for(s, card, i))
        b.close()

    if not only:
        path = os.path.join(export_dir, "screens.jsonl")
        with open(path, "w", encoding="utf-8") as fh:
            for r in records:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"{'screen':36} {'status':10} cards fields")
    for sid, st, nc, nf in summary:
        print(f"{sid:36} {st:10} {nc:5} {nf:6}")
    if deep:
        routes = {}
        for f in sorted(os.listdir(outdir)):
            d = json.load(open(os.path.join(outdir, f), encoding="utf-8"))
            for x in d.get("discovered", []):
                if "route" in x:
                    routes.setdefault(x["route"].split("?")[0], (d["id"], x["via"]))
        if routes:
            print("\nsub-screens reached by clicking (not in the map yet):")
            for r, (sid, via) in sorted(routes.items()):
                print(f"  {r:50} from {sid} via {via!r}")
    print(f"\n{len(records)} card records" + ("" if only else f" -> {path}"))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["build", "explore", "fields", "jsonl"])
    ap.add_argument("--only", help="a single screen by id or route")
    ap.add_argument("--deep", action="store_true", help="fields: also click every safe button and read what opens")
    ap.add_argument("--area", help="explore/fields: only screens of this area (settings, programmes)")
    args = ap.parse_args()
    if args.command == "build":
        return build()
    if args.command == "fields":
        return fields(args.only, args.deep, args.area)
    if args.command == "jsonl":
        return write_jsonl()
    return explore(args.only, args.area)


if __name__ == "__main__":
    sys.exit(main())
