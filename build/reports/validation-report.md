# Knowledge Base Validation Report

**Generated:** 2026-03-24
**Content directory:** `content/`
**Total docs checked:** 186

---

## Summary

| Check | Pass | Fail | Notes |
|---|---|---|---|
| 1. Required frontmatter fields | 186 | 0 | All 7 required fields present in every doc |
| 2. Unique slugs | 186 | 0 | No duplicate slugs found |
| 3. Exactly one H1 | 186 | 0 | Every doc has exactly one H1 |
| 4. No skipped heading levels | 186 | 0 | No heading level jumps found |
| 5. No broken internal .md links | 185 | 1 | One broken link found |
| 6. All referenced assets exist | 175 | 11 | 53 missing asset files across 11 docs |

**Overall result: FAIL** (1 broken link + 53 missing assets across 11 docs)

---

## Check 5 — Broken Internal Links (1 issue)

| File | Issue |
|---|---|
| `guides/payment-pairing.md` | Broken link: `../payments/gocardless-direct-debit-mandates.md` — target path does not exist (correct path is likely `../guides/gocardless-direct-debit-mandates.md`) |

---

## Check 6 — Missing Assets (53 issues across 11 files)

### `guides/automatic-session-notification.md` (1 missing)
- `assets/images/add-new-template-button.png`

### `guides/billable-sessions.md` (4 missing)
- `assets/images/how-to-create-paid-events-04.png`
- `assets/images/how-to-create-paid-events-06.png`
- `assets/images/how-to-create-paid-events-08.png`
- `assets/images/how-to-create-paid-events-10.png`

### `guides/creating-entry-passes.md` (11 missing)
- `assets/images/entry-pass-create-product.png`
- `assets/images/entry-pass-credit-value-config.png`
- `assets/images/entry-pass-items-for-sale.png`
- `assets/images/entry-pass-add-item.png`
- `assets/images/entry-pass-discount-pricing.png`
- `assets/images/entry-pass-description-template.png`
- `assets/images/entry-pass-assign-to-class.png`
- `assets/images/entry-pass-select-product.png`
- `assets/images/entry-pass-profile-availability.png`
- `assets/images/entry-pass-booking-form-availability.png`
- `assets/images/entry-pass-dual-product-setup.png`

### `guides/dynamic-tags.md` (1 missing)
- `assets/images/dynamic-tags-panel.png`

### `guides/edit-session-notification-template.md` (4 missing)
- `assets/images/communication-menu-message-templates.png`
- `assets/images/notifications-section-templates.png`
- `assets/images/general-settings-signout-rules.png`
- `assets/images/reminder-send-time-setting.png`

### `guides/message-templates.md` (4 missing)
- `assets/images/message-template-editor.png`
- `assets/images/communication-menu-templates.png`
- `assets/images/template-list-orange-labels.png`
- `assets/images/payment-reminder-example.png`

### `guides/pay-as-you-go-programme.md` (7 missing)
- `assets/images/pay-as-you-go-create-programme.png`
- `assets/images/pay-as-you-go-create-class.png`
- `assets/images/pay-as-you-go-add-sessions.png`
- `assets/images/pay-as-you-go-client-book-session.png`
- `assets/images/pay-as-you-go-client-select-session.png`
- `assets/images/pay-as-you-go-client-session-booked.png`
- `assets/images/pay-as-you-go-calendar-widget.png`

### `guides/send-email-after-session.md` (3 missing)
- `assets/images/selecting-event-date.png`
- `assets/images/automation-tile-event-detail.png`
- `assets/images/email-options-automation-tile.png`

### `guides/sending-email-sms.md` (12 missing)
- `assets/images/messages-overview-filters.png`
- `assets/images/target-group-selection.png`
- `assets/images/promotional-message-settings.png`
- `assets/images/clients-registrations-selection.png`
- `assets/images/group-selection-dropdown.png`
- `assets/images/template-custom-message-selection.png`
- `assets/images/message-editor-dynamic-tags.png`
- `assets/images/summary-screen-before-sending.png`
- `assets/images/notes-preferences-promotional.png`
- `assets/images/send-promotional-emails-checkbox.png`
- `assets/images/no-communication-warning.png`
- `assets/images/sms-sender-name-setting.png`

### `setup/company-logo-email.md` (3 missing)
- `assets/images/settings-general-menu.png`
- `assets/images/account-info-logo-url.png`
- `assets/images/email-with-company-logo.png`

### `setup/whatsapp-integration.md` (3 missing)
- `assets/images/whatsapp-connect-button.png`
- `assets/images/meta-connection-flow.png`
- `assets/images/whatsapp-pin-setup.png`

---

## Checks 1–4 — All Pass

No issues found for:
- Required frontmatter (all 7 fields: `title`, `slug`, `type`, `product_area`, `audience`, `status`, `last_converted`)
- Slug uniqueness (186 distinct slugs)
- Single H1 per doc
- Heading level progression (no skipped levels)
