# Intercom intake — 2026-06-24 → 2026-08-06 (human-agent responses)

**Run date:** 2026-08-07
**Scope:** 281 conversations. 131 had a human-agent reply (Martin Rapavý, Tech Support, Katarína Babiaková). 150 were bot-only — see `intercom-july-2026-bot-only.md`.
**Method:** every conversation with a human reply read in full. The human answer is the gold standard; the bot answer is scored against it.

Legend for **Status**: `todo` = not yet in the KB · `verify` = KB article exists, needs checking against this answer · `done` = written.

---

## A. Bot gave a wrong answer that a human had to correct

These are the highest-priority KB gaps: the bot was confident and wrong, and a human had to step in.

| # | Conv | Topic | What the bot said | What is actually true | Status |
|---|---|---|---|---|---|
| H3 | 215474840840167 | Previewing the booking widget before going live | Claimed a live preview panel exists inside **Configure**, then admitted after 32 re-asks that it does not | There is no preview panel. Use the **Playground account** (switch by clicking the account name under the logo), the test page `<account>.zooza.online`, and **Copy link** on a class to open the client-facing offer | todo |
| H4 | 215474855197157 | Printable visual timetable | "Zooza has no built-in way to export the calendar — take a screenshot" | **Calendar → toolbar → Print Version** produces a PDF covering every location for a week. Three layouts now put all venues on one page | verify |
| H13 | 215474929092668 | `Transaction type` in the received-payments export | "Credit = credit from a previous overpayment; blank = the main payment line" | **Credit** = payment recorded manually. **Credit via Transfer** = bank transfer. **Blank** = a bank transaction Zooza could not pair (once the bank is linked, every account transaction is stored). Filter *From Bank* + *Status = Paired* | todo |
| H15 | 215474990590888 | MCP connector tool list | "The tools update automatically with Zooza releases" | The connector does **not** auto-update. ChatGPT: Settings → Apps → Zooza → Disconnect / Refresh. Feedback is sent by typing "I want to send feedback to Zooza" in the chat — there is no button | todo |
| H22 | 215475010052087 | Bulk email to lead-collection clients | Said twice it is impossible and offered a manual unticking workaround | **Classes → filter Status = lead collection → Email** button at the top. Sending from Classes also exposes an extra filter (e.g. waitlist only) | todo |
| H21 | 215475001854253 | Sharing a link to a product | "Gift vouchers have no purchase link, use `*\|BOOKING_URL\|*`" | **Products → product detail → Copy** gives the product's checkout link. Classes have the same Open/Copy pair, plus a **private link** via the arrow next to Copy. There is **no dynamic tag for a product link** | todo |
| H31 | 215475109642682 | Zooza Sites theming | Invented a "Custom Colors and Fonts" theme switch and repeated it four times | Sites templates are limited and **do not support colour theming at all**. For a branded page Zooza hosts one on the client's subdomain via CNAME, free as part of account setup | todo |
| H40 | 215475186259558 | Re-accepting updated terms | "You cannot reset or force existing clients to re-accept" | A **checkbox marks a consent edit as a new version**, which re-prompts existing clients. Previously every save created a version, which is why it over-triggered | verify |
| H30 | 215475112694550 | Limiting make-up sessions per month | Contradicted itself across turns and invented a "Credit expiration policy" setting | There is a **flexible replacement limit** (e.g. 2 make-ups per 10 sessions). Admins can override a client's credit limits | todo |
| H1/H2 | 215474845646196 | Trainer holiday; changing the language | Sent the user to Settings → Custom Holidays, then to a non-existent "profile → Account settings → Language" | Trainer absence is set at `#trainer/` → **Working hours**. Custom Holidays are company-wide, a different thing. The language path the bot gave does not exist | todo |
| H48 | 215475256660852 | Changing a client's email | Pushed the formal Data correction flow | If the target email already exists it is **not** a data change — open the registration → Client card → **Change client** | todo |

---

## B. Answers only a human knew (no bot attempt, or bot escalated)

| # | Conv | Topic | Answer |
|---|---|---|---|
| H8 | 215474858324500 | Transferring a client between courses or accounts | Payment history transfers. Set the instalment schedule **from the transfer date**, not from the group start — otherwise Zooza back-fills duplicate instalments |
| H9/H10 | 215474854926690, 215474855014188, 215474855005288 | Auto-continuation shows "no groups available" | Two-sided setup: the source course defines where registrations may continue (`#courses/X/settings?edit=retention`) **and** each target group must be marked as allowed for continuation. Responses live at Dashboard → Registrations → Automatic continuation → All responses. No email is sent by design |
| H56 | 215475298753066 | Capacity vs extra capacity | **The registration form respects only Capacity. Make-up sessions respect Capacity + Extra capacity. For trials you choose which of the two they draw on.** So capacity 7 → set 5 + 2 extra = 5 sellable places, 2 held for trials/make-ups |
| H29 | 215475080773045 | Trials, missing extra fields, pay-by-blocks | Trials: Programme → Settings → Trial → **Shown in Form (By Number of Sessions)**. Extra fields missing → they were set to collect only from *added persons*. Pay-by-blocks: parents register for the year, place reserved, charged just before each block, first block immediately |
| H25 | 215475075194244 | Reminder before a deposit is due | Course → Settings → Price and payment → Payment reminder settings. The system does **not** distinguish deposit from full amount — it checks whether the registration is Paid. Schedule relative to the registration date **or** the group start date |
| H43 | 215475222027448 | Who invoices the 3.5% gateway fee | Own Stripe (Stripe invoices you) **or** Zooza's Stripe — money flows to Zooza, which pays out 1–2×/month with the system invoice; Zooza s.r.o. is the contracting party. Payouts only to verified legal EU entities. CardPay is one-off only |
| H44 | 215475244228883 | Payments stopped pairing | The old generic pairing address breaks when the same IBAN exists in several Zooza accounts. Fix: `#payments/inbound/setup` → click the IBAN → pick the bank → **Set** → use the dedicated address shown, in internet banking |
| H45 | 215475244814791 | Client cannot log in from the company website | A cookie-consent banner in opt-out mode blocks Zooza entirely, and the page must be refreshed after accepting |
| H50 | 215475260475622 | GoCardless charged before the scheduled date | GoCardless **collects several days before** the date shown in Zooza. Same payment, not a double charge |
| H35 | 215475170361964 | Per-block dynamic tag | Will never exist — each class has its own blocks with no technical overlap, which is also why blocks cannot be exported. Use `*\|ORDER_SUMMARY\|*` |
| H53 | 215475286181511 | `EVENT_*` tags empty in a test send | They resolve **only when the application itself sends the message** — a manual send has no session to bind to |
| H52 | 215475285561723 | Naming several children in one document | **1 document = 1 registration.** `ORDER_SUMMARY` on the main registration summarises linked sub-registrations |
| H34 | 215475168971012 | Make-up session not offered | Use the **Run diagnostics (MATKO)** button. Most common cause: make-ups restricted to a billing period that has already ended |
| H39 | 215475183335193 | Classes missing from the booking form | **Limit number of registrations** (advanced class settings) is not capacity — it caps how many people one booking may register. Set to 1 it hides the class |
| H38 | 215475183244514 | Child's name on the invoice | Use the **Item description** field with tags, e.g. `*\|COURSE_NAME\|* - *\|EF_FULL_NAME\|*`, then regenerate with "Use default description" off |
| H41 | 215475192480209 | Participant = client, family relationships | Admins must create bookings **in the app**, not from a client profile while logged in as that client — that creates cross-company family relationships |
| H55 | 215475290414578 | Business fields | Not mandatory → the client gets a checkbox that reveals them. Mandatory → no checkbox. **If the invoice profile is not a VAT payer the VAT field is hidden automatically** |
| H54 | 215475287990029 | Documents; deleting a client | Documents live under **Products & Services → Documents**. A client who is also an instructor cannot be deleted — they appear in the list only because they hold registrations |
| H57 | 215475327169019 | Custom course types / filtering | Courses carry `key=value` **metadata** usable for site-side filters and form rendering. **Classes have no metadata — use tags.** Courses sort alphabetically unless you set a **priority** |
| H42 | 215475213472396 | Booking conversion tracking | `#done` is the documented conversion trigger. The widget natively pushes DataLayer + Meta Pixel events; a separate server-side Partner Integration event also reaches Meta. Email/phone are deliberately not sent |
| H47 | 215475255463719 | Pausing a month of classes | Cancel that month's scheduled payments, delete the sessions without notifying, send one message. If the next payment is not generated yet the schedule can stop — check individually |
| H33 | 215475124282890 | Skipping holidays | Set the **Region on the place** first. The skip option exists **only in the Advanced session-planning tab**. It cannot be applied retroactively — filter the sessions and bulk delete or move |
| H36 | 215475171219261 | Removing a duplicate payment | Payment → **More** → **Correct** → zero the amount. A refund shows in reports, a correction does not. **Invitations never expire** |
| H37 | 215475158428716 | Sibling discount granted wrongly | A differently-spelled name (missing diacritics) is treated as a second child. Loyalty is beta — keep a T&C mechanism to withdraw a wrongly granted discount |
| H6/H5 | 215474913907137, 215474884472148 | Make-up rules | Make-ups only work in **continuous** courses, not one-off session types. Classes become available for make-ups only **4 days before start** |
| H11 | 215474885814597 | Copying a registration | **Cannot copy a registration into a different course type.** "Registration for a single date" courses must be created manually |
| H12 | 215474914397237 | Unsubscribing from promotional messages | The client **cannot** do it. Admin: Client card → Settings and preferences. The sender must also tick "promotional message" |
| H17 | 215475033677159, 215474987107415 | One-off vs instalments, wrong price | If the course is set to one-off payment, payment templates will not work. To offer both: set payment in instalments, set a unit price, activate both templates |
| H51 | 215475270539659 | A session reserved only for trials | Not possible — you can only offer existing group capacity |
| H28 | 215475058978548 | GoCardless instalments marked manual | The **first mandate GoCardless issues is not recurring**, so Zooza assumed it could not charge later. Fixed; the Mandates overview now shows plan, last payment, and offline payments |

---

## C. Product bugs and changes recorded during the period (context, not KB work)

- Consent versioning checkbox shipped (ZOOZA, 22 Jul).
- "Payment by block" template counted unpaid sessions — fixed (ZOOZA-4869).
- Duplicate-registration protection was wrongly active for trial sessions, blocking a second child — fixed.
- Colour picker ignores the first colour selection; pick another colour first.
- Bulk SMS can double-send on large batches (SMS is not queued like email yet).
- Retention wording changed to fit both ending and ended courses.
- Calendar print/PDF rebuilt with three layouts covering all venues.
