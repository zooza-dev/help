# Validation Report

**Generated:** 2026-02-13
**Scope:** All `.md` files in `content/` (excluding `_shared/` and `_`-prefixed files)
**Total files validated:** 126

## Summary

| Check                          | Status | Issues |
|-------------------------------|--------|--------|
| Required frontmatter fields   | PASS   | 0      |
| Unique slugs                  | PASS   | 0      |
| Unique intercom_id values     | PASS   | 0      |
| Exactly one H1 per doc        | PASS   | 0      |
| No skipped heading levels     | FAIL   | 1 file (2 occurrences) |
| No broken internal links      | PASS   | 0      |
| All referenced assets exist   | FAIL   | 38 missing assets across 9 files |

**Overall: FAIL** (2 check categories have issues)

---

## 1. Required Frontmatter Fields

**Status: PASS**

All 126 files contain the required frontmatter fields: `title`, `slug`, `type`, `product_area`, `audience`, `tags`, `status`, `source_legacy_path`, `source_language`, `needs_screenshot_replacement`, `last_converted`.

No issues found.

---

## 2. Unique Slugs

**Status: PASS**

All slugs are unique across the knowledge base.

No issues found.

---

## 3. Unique intercom_id Values

**Status: PASS**

No duplicate `intercom_id` values found.

No issues found.

---

## 4. Exactly One H1 Per Doc

**Status: PASS**

All 126 files contain exactly one H1 heading in the body.

No issues found.

---

## 5. No Skipped Heading Levels

**Status: FAIL -- 1 file, 2 occurrences**

| File | Issue |
|------|-------|
| `content/guides/gocardless-direct-debit-mandates.md` | H2 -> H4 (line 24: `#### Quick step-by-step`) |
| `content/guides/gocardless-direct-debit-mandates.md` | H2 -> H4 (line 60: `#### Option A: ...`, line 72: `#### Option B: ...`) |

The file jumps from `##` (H2) directly to `####` (H4), skipping H3.

---

## 6. No Broken Internal Links

**Status: PASS**

All relative `.md` links resolve to existing files.

No issues found.

---

## 7. All Referenced Assets Exist

**Status: FAIL -- 38 missing assets across 9 files**

### `content/guides/automatic-event-notification.md` (4 missing)

- `../../assets/images/sample-event-reminder-email.png`
- `../../assets/images/turning-off-event-notifications.png`
- `../../assets/images/add-new-template-button.png`
- `../../assets/images/assigning-custom-template-course.png`

### `content/guides/automatic-payment-reminders.md` (2 missing)

- `../../assets/images/payment-reminder-settings.png`
- `../../assets/images/payment-due-date-settings.png`

### `content/guides/dynamic-tags.md` (1 missing)

- `../../assets/images/dynamic-tags-panel.png`

### `content/guides/edit-event-notification-template.md` (4 missing)

- `../../assets/images/communication-menu-message-templates.png`
- `../../assets/images/notifications-section-templates.png`
- `../../assets/images/general-settings-signout-rules.png`
- `../../assets/images/reminder-send-time-setting.png`

### `content/guides/message-templates.md` (4 missing)

- `../../assets/images/message-template-editor.png`
- `../../assets/images/communication-menu-templates.png`
- `../../assets/images/template-list-orange-labels.png`
- `../../assets/images/payment-reminder-example.png`

### `content/guides/send-email-after-event.md` (3 missing)

- `../../assets/images/selecting-event-date.png`
- `../../assets/images/automation-tile-event-detail.png`
- `../../assets/images/email-options-automation-tile.png`

### `content/guides/sending-email-sms.md` (14 missing)

- `../../assets/images/messages-overview-filters.png`
- `../../assets/images/new-message-indicator.png`
- `../../assets/images/unread-messages-list.png`
- `../../assets/images/target-group-selection.png`
- `../../assets/images/promotional-message-settings.png`
- `../../assets/images/clients-registrations-selection.png`
- `../../assets/images/group-selection-dropdown.png`
- `../../assets/images/template-custom-message-selection.png`
- `../../assets/images/message-editor-dynamic-tags.png`
- `../../assets/images/summary-screen-before-sending.png`
- `../../assets/images/notes-preferences-promotional.png`
- `../../assets/images/send-promotional-emails-checkbox.png`
- `../../assets/images/no-communication-warning.png`
- `../../assets/images/sms-sender-name-setting.png`

### `content/setup/company-logo-email.md` (3 missing)

- `../../assets/images/settings-general-menu.png`
- `../../assets/images/account-info-logo-url.png`
- `../../assets/images/email-with-company-logo.png`

### `content/setup/whatsapp-integration.md` (3 missing)

- `../../assets/images/whatsapp-connect-button.png`
- `../../assets/images/meta-connection-flow.png`
- `../../assets/images/whatsapp-pin-setup.png`
