---
handoff_id: help-to-app-20261030-001
from: help
to: app
status: open
created: 2026-10-30
updated: 2026-10-30
related_specs: []
related_handoffs: []
---

## Request

### What we need

**"Send booking link" in the trial automation does not do what it says, and quietly does
something else.** Please correct the control. We are not asking for the email to start
being gated — see the constraint below, that route is the dangerous one.

### Why we need it

It came out of the weekly help intake. We were about to document the toggle and could not
make the source agree with its own help text, so we read the whole path. An admin who
unticks it today believes they have stopped the Trial Ended email. They have not. They
have switched off their follow-ups instead, and shortened the window before trials are
marked Lost — none of which the control says it does.

### What we verified (api-v1 and app, both read at `origin/main`, 2026-10-30)

**1. `send_booking_link` is read as a condition in exactly zero places in api-v1.** It is
written at `class/Action.php:167`, `:180`, `:182`, seeded `true` at `class/Course.php:296`,
and serialised at `class/Zooza/Resource/Action.php:19`. Nothing reads it. Also confirmed
absent from widgets-v1, from the worker path (trial actions always take the legacy cron
branch, `use_worker = 0`), and there is no `actions.send_booking_link` column, default or
trigger — it lives inside the `actions.settings` JSON blob.

**2. The email it is named for fires unconditionally.** `class/Action.php:783-786`:

```php
if( $sub_action == 'booking_link' ) {
    $notification = System_Notification::TYPE_REGISTRATION_TRIAL_ENDED;
    $statuses[]   = 'trial_ended';
```

The contrast is in the same function: the `lost` branch immediately below reads
`automatically_send_to_lost` and `notify_customer_after_lost` and sets
`$notification = false` when off, and `send_followup_link` *is* read as a hard gate at
`__zooza_cron_check_events.php:239`. So this reads as an omission, not a design.

What actually gates the Trial Ended email, all in `get_booking_links()`
(`__zooza_cron_check_events.php:105-152`): the action row exists and `active = 1`,
`registrations.status = 'trial_ended'`, `booking_link_sent IS NULL`,
`process_course_trial_automation = 1`, and the `apply_to_new_registrations_only` recency
rule.

**3. The toggle is not inert — this is the part that bites.**
`pages/courses/course_settings.js:2121-2123`:

```js
if( !form_data.settings.send_booking_link )  {
    form_data.settings.send_followup_link = false;
}
```

Unticking it silently writes `send_followup_link = false`, and *that* the cron honours.
Two consequences follow: affected registrations are stamped
`process_course_trial_automation = 2` (`Action::PROCESSING__NO_FOLLOWUPS`) by
`exclude_registration_from_automation()` at `__zooza_cron_check_events.php:245`, and in
`get_send_to_lost()` the timer collapses from
`first_followup + second_followup + send_to_lost_after` to just `send_to_lost_after`
(`:352-367`) — so **trials are marked Lost sooner**.

**4. The booking detail then reports the opposite of what happens.**
`pages/registrations/registration_detail.js:908-911` gates `will_send_booking_link` on the
same setting, so the trial timeline tells the admin the booking link will not be sent
while the cron sends it.

### Constraints from our side

- **Please do not simply start honouring it as a gate.** Both seeds default it ON
  (`Course.php:296`, `course_settings.js:2039`), so gating is a no-op for the default
  population — but any account that unticked it would silently stop receiving a Trial
  Ended email they get today, and unticking it is a very plausible thing to have done,
  since the UI presents it as the master switch for the whole chain and collapses the
  follow-up settings beneath it. If the product decision really is to gate the email,
  it needs a backfill writing an explicit `true` onto every `course_trial` action whose
  settings have the key `null` or missing, so only deliberate opt-outs change behaviour —
  and a release note.
- Whatever you choose, the **booking detail timeline** must end up agreeing with it.
- Tell us the outcome and we will write it up. We are holding the help page in the
  meantime: it currently describes the real behaviour, flagged as a fault being fixed, and
  we would rather replace that with the truth than leave it standing.

### How we imagine it — open to challenge

Make the UI tell the truth rather than changing the backend:

1. **Relabel the toggle to what it governs** — the follow-up emails — or remove it and
   leave the existing **Send follow-up** control to do its own job.
2. **Drop the hidden coercion** at `course_settings.js:2121-2123`.
3. **Fix the help text** at `lib/str_en3.js:4687`, which is the source of the belief.

Two cheap, unambiguous bugs we tripped over in the same code and would fix in the same
pass:

- **`class/Action.php:190-212`** — six dependent settings (`first_followup`,
  `second_followup`, `automatically_send_to_lost`, `send_to_lost_after`,
  `notify_customer_after_lost`, `apply_to_new_registrations_only`) are each guarded by
  `isset( $value->send_followup_link )` instead of their own key, so a PATCH that omits
  `send_followup_link` silently drops all six.
- **`components/automation_trial_1/automation_trial_1.js:96`** and the identical line in
  `automation_trial_2` — `send_followup_formatted` reads `send_booking_link`, so the
  summary reports the booking-link setting under the follow-up label.

One thing we could not determine and you can: **how many live accounts actually have it
unticked.** The value is inside a JSON blob, so it needs a query against
`actions.settings` for `action = 'course_trial'`. Worth knowing before any route that
changes behaviour. Note also that `class/Action.php:167` stores `null` when a POST omits
the key, and `lib/utils.js:2377` merges with `Object.assign({}, defaults, settings)` — a
stored `null` beats the `true` default, so such a row renders **unticked** in the UI while
still sending. Those rows are not opt-outs and must not be treated as any.
