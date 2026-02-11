# Validation Report

**Date:** 2026-02-11
**Files validated:** 11 content docs (excluding `content/_shared/doc-template.md`)

---

## Results Summary

| # | Check | Result | Issues |
|---|---|---|---|
| 1 | Required frontmatter present | **PASS** | 0 |
| 2 | Frontmatter values valid per taxonomy | **PASS** | 0 |
| 3 | Unique slugs | **PASS** | 0 |
| 4 | Exactly one H1 per doc | **PASS** | 0 |
| 5 | No skipped heading levels | **PASS** | 0 |
| 6 | No broken internal `.md` links | **PASS** | 0 broken; 1 warning |
| 7 | All referenced image assets exist | **PASS** | 0 |

**Overall: PASS (all checks passed)**

---

## 1. Required Frontmatter — PASS

All 11 files contain every required field: `title`, `slug`, `type`, `product_area`, `audience`, `tags`, `status`, `source_legacy_path`, `source_language`, `needs_screenshot_replacement`, `last_converted`.

## 2. Frontmatter Values Valid per Taxonomy — PASS

| Field | Values used | Valid? |
|---|---|---|
| `type` | setup (2), guides (6), troubleshooting (1), faq (1) | Yes |
| `product_area` | Communication (11) | Yes |
| `sub_area` | Email (8), WhatsApp (3) | Yes |
| `audience` | admin (11) | Yes |
| `status` | published (11) | Yes |

## 3. Unique Slugs — PASS

11 slugs, 0 collisions:

1. `whatsapp-integration`
2. `company-logo-email`
3. `automatic-payment-reminders`
4. `edit-event-notification-template`
5. `dynamic-tags`
6. `automatic-event-notification`
7. `message-templates`
8. `send-email-after-event`
9. `sending-email-sms`
10. `whatsapp-troubleshooting`
11. `whatsapp-faq`

## 4. Exactly One H1 per Doc — PASS

Every file has exactly one `#` heading. No file has zero or multiple H1s.

## 5. No Skipped Heading Levels — PASS

| File | Levels used | OK? |
|---|---|---|
| whatsapp-integration.md | H1 → H2 → H3 | Yes |
| company-logo-email.md | H1 only | Yes |
| automatic-payment-reminders.md | H1 → H2 | Yes |
| edit-event-notification-template.md | H1 → H2 | Yes |
| dynamic-tags.md | H1 → H2 → H3 | Yes |
| automatic-event-notification.md | H1 → H2 | Yes |
| message-templates.md | H1 → H2 → H3 | Yes |
| send-email-after-event.md | H1 only | Yes |
| sending-email-sms.md | H1 → H2 | Yes |
| whatsapp-troubleshooting.md | H1 → H2 | Yes |
| whatsapp-faq.md | H1 → H2 | Yes |

## 6. Internal Links — PASS (1 warning)

All internal `.md` links resolve to existing files:

| Source file | Link target | Resolved path | Exists? |
|---|---|---|---|
| whatsapp-integration.md | `../troubleshooting/whatsapp-troubleshooting.md` | content/troubleshooting/whatsapp-troubleshooting.md | Yes |
| whatsapp-integration.md | `../faq/whatsapp-faq.md` | content/faq/whatsapp-faq.md | Yes |
| edit-event-notification-template.md | `automatic-event-notification.md` | content/guides/automatic-event-notification.md | Yes |
| edit-event-notification-template.md | `message-templates.md` | content/guides/message-templates.md | Yes |
| automatic-event-notification.md | `edit-event-notification-template.md` | content/guides/edit-event-notification-template.md | Yes |
| message-templates.md | `dynamic-tags.md` | content/guides/dynamic-tags.md | Yes |
| message-templates.md | `automatic-event-notification.md` | content/guides/automatic-event-notification.md | Yes |
| message-templates.md | `edit-event-notification-template.md` | content/guides/edit-event-notification-template.md | Yes |
| message-templates.md | `automatic-payment-reminders.md` | content/guides/automatic-payment-reminders.md | Yes |
| sending-email-sms.md | `dynamic-tags.md` | content/guides/dynamic-tags.md | Yes |
| whatsapp-troubleshooting.md | `../setup/whatsapp-integration.md` | content/setup/whatsapp-integration.md | Yes |
| whatsapp-troubleshooting.md | `../faq/whatsapp-faq.md` | content/faq/whatsapp-faq.md | Yes |

### Warning: legacy external link

`content/guides/automatic-payment-reminders.md` contains a link to `https://support.zooza.online/portal/en/kb/articles/payment-templates-creation`. This article was not part of the current conversion batch. The link will need updating when that content is converted.

## 7. Referenced Image Assets — PASS

38 images referenced across all docs. All 38 exist in `assets/images/`.

| File | Images | All exist? |
|---|---|---|
| whatsapp-integration.md | 3 | Yes |
| company-logo-email.md | 3 | Yes |
| automatic-payment-reminders.md | 2 | Yes |
| edit-event-notification-template.md | 4 | Yes |
| dynamic-tags.md | 1 | Yes |
| automatic-event-notification.md | 4 | Yes |
| message-templates.md | 4 | Yes |
| send-email-after-event.md | 3 | Yes |
| sending-email-sms.md | 14 | Yes |
| whatsapp-troubleshooting.md | 0 | N/A |
| whatsapp-faq.md | 0 | N/A |
