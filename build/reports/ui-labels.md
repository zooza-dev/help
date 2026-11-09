# Field names the app no longer has

14 label(s) in `content/` are written in backticks — our convention for a
field name — and do not appear in the app's or the widgets' current English strings.

A miss is a question, not a verdict. The usual innocent explanations are example
data, a label built at runtime from parts, and a screen belonging to somebody else's
product. What it catches when it is right is the expensive case: a control we tell
people to look for under a name it no longer has.

152 backticked string(s) were skipped as not being Zooza field names,
10 of them because somebody has already judged them fine - the reasons
are in `scripts/ui-labels-allow.yml`, and deleting an entry re-opens the question.

### `content/reference/class-detail.md` — 4

- `Booking fee (optional)`  ×2
  - no close match; check the screen by hand
- `Timetable type`
  - no close match; check the screen by hand
- `Payment plan name`
  - no close match; check the screen by hand
- `Absence count`
  - no close match; check the screen by hand

### `content/reference/bookings-list.md` — 3

- `Current account balance`  ×6
  - no close match; check the screen by hand
- `Payment balance`
  - no close match; check the screen by hand
- `Amount owed`
  - no close match; check the screen by hand

### `content/reference/instructors-list.md` — 2

- `Length of session – 90 minutes`
  - fine: our example of `Length of session - %1 minutes:`
- `Length of session – 60 minutes`
  - fine: our example of `Length of session - %1 minutes:`

### `content/reference/reports-dashboard.md` — 2

- `Provider refund ID`
  - no close match; check the screen by hand
- `Client (Buyer)`
  - no close match; check the screen by hand

### `content/guides/payment-pairing.md` — 1

- `Credit via Transfer`
  - no close match; check the screen by hand

### `content/reference/orders-list.md` — 1

- `Current account balance`  ×6
  - no close match; check the screen by hand

### `content/guides/transfer-and-copy-bookings.md` — 1

- `Current account balance`  ×6
  - no close match; check the screen by hand

### `content/reference/clients-list.md` — 1

- `Current account balance`  ×6
  - no close match; check the screen by hand

### `content/reference/programmes-list.md` — 1

- `Booking fee (optional)`  ×2
  - no close match; check the screen by hand

### `content/reference/communication-dashboard.md` — 1

- `The customer`
  - no close match; check the screen by hand

### `content/reference/publish-widgets.md` — 1

- `View filtering by location`
  - no close match; check the screen by hand

