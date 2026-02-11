# Conversion Report

**Generated:** 2026-02-11

## Summary

| Metric | Count |
|---|---|
| Legacy HTML files processed | 9 |
| Markdown pages created | 11 |
| Pages translated (sk/mixed -> en) | 1 |
| Pages split | 1 (WhatsApp -> setup + troubleshooting) |
| FAQ pages extracted | 1 |
| Redirects generated | 9 |

## Output files

### content/setup/
- `whatsapp-integration.md` - WhatsApp Integration & Usage (Beta)
- `company-logo-email.md` - Company logo in email communication

### content/guides/
- `automatic-payment-reminders.md` - Automatic reminders for payment schedule
- `edit-event-notification-template.md` - Edit automatic notifications of an upcoming event
- `dynamic-tags.md` - Dynamic tags
- `automatic-event-notification.md` - Automatic notification of an upcoming event
- `message-templates.md` - Automatic communication to clients / Message templates
- `send-email-after-event.md` - Send an email after lesson/event
- `sending-email-sms.md` - Sending email/SMS to clients

### content/troubleshooting/
- `whatsapp-troubleshooting.md` - WhatsApp troubleshooting (split from WhatsApp setup)

### content/faq/
- `whatsapp-faq.md` - WhatsApp FAQ (extracted from WhatsApp setup)

## Broken links

| Source page | Broken link target | Notes |
|---|---|---|
| automatic-payment-reminders.md | `payment-templates-creation` | External link to legacy article not in this batch |
| message-templates.md | `automatic-payment-reminders` (legacy URL) | Link points to legacy URL for payment reminder settings article not in this batch |

## Missing assets

No local assets exist. All images are hosted remotely on:
- `support.zooza.online/galleryDocuments/...` (Zoho Desk CDN)
- `www.zooza.online/wp-content/uploads/...` (WordPress)

Images are referenced via remote URLs. No files were copied to `assets/images/` because no local copies exist in `legacy/assets/`.

## Pages flagged `needs_screenshot_replacement: true`

| Page | Reason |
|---|---|
| `automatic-payment-reminders.md` | Screenshots show Zooza UI (may be Slovak) |
| `edit-event-notification-template.md` | Screenshots show Zooza UI (may be Slovak) |
| `dynamic-tags.md` | Screenshot shows Zooza UI (may be Slovak) |
| `automatic-event-notification.md` | Screenshots show Zooza UI (may be Slovak) |
| `message-templates.md` | Screenshots show Zooza UI (may be Slovak) |
| `send-email-after-event.md` | Screenshots show Zooza UI (may be Slovak) |
| `sending-email-sms.md` | Screenshots show Zooza UI (may be Slovak) |

Pages **not** flagged (English UI or no UI screenshots):
- `whatsapp-integration.md`
- `company-logo-email.md`
- `whatsapp-troubleshooting.md`
- `whatsapp-faq.md`

## Translation notes

| Page | Original language | Notes |
|---|---|---|
| `sending-email-sms.md` | mixed | One Slovak callout ("Pozor!") translated to English ("Attention!") |

All other pages were already in English.

## Content map

Stable slugs and paths are recorded in `legacy/content-map.yml`.
