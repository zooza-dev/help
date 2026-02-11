# Conversion Report

**Generated:** 2026-02-11

## Summary

| Metric | Count |
|---|---|
| Legacy HTML files processed | 83 |
| Markdown pages created | 85 (83 + 1 split + 1 FAQ) |
| Pages translated (sk/mixed → en) | 1 |
| Pages split | 1 (WhatsApp → setup + troubleshooting) |
| FAQ pages extracted | 2 (whatsapp-faq, common-booking-scenarios) |
| Redirects generated | 83 |
| Images downloaded | 530 |

## Content by Product Area

| Product Area | Docs |
|---|---|
| Communication | 11 |
| Programmes | 18 |
| Classes | 5 |
| Calendar | 1 |
| Bookings | 6 |
| Clients | 5 |
| Payments | 16 |
| Settings | 16 |
| Widgets | 3 |
| Orders | 1 |

## Content by Type

| Type | Count |
|---|---|
| guides | 56 |
| setup | 23 |
| troubleshooting | 3 |
| faq | 2 |

## Batch 1 — Communication (completed previously)

Files: 0001, 0003, 0004, 0005, 0006, 0007, 0009, 0011, 0012
- 9 HTML → 11 Markdown (1 split, 1 FAQ extracted)
- 1 mixed-language file translated (0012)
- 38 images downloaded
- Manual conversion with quality review

## Batch 2 — All Other Areas (current run)

Files: 74 HTML files (0013–0114)
- 74 HTML → 74 Markdown
- All English source; no translation needed
- 492 images downloaded
- Automated conversion via `build/convert_html.py`

## Screenshot Flags

7 batch 1 files flagged `needs_screenshot_replacement: true` (Slovak UI):
- automatic-payment-reminders, edit-event-notification-template, dynamic-tags,
  automatic-event-notification, message-templates, send-email-after-event, sending-email-sms

All batch 2 files set to `needs_screenshot_replacement: false` (English UI).

## Known Issues

### Internal links to legacy URLs
Many articles contain internal links pointing to `/portal/en/kb/articles/...` (legacy URLs).
A future pass should rewrite these to local `.md` references using the content map.

### Conversion quality (batch 2)
Batch 2 used automated HTML→Markdown conversion. Complex HTML structures (nested lists,
callout boxes with icons, embedded videos) may need manual review.

## Translation Notes

| Page | Original Language | Notes |
|---|---|---|
| sending-email-sms.md | mixed | Slovak "Pozor!" translated to "Attention!" |

All other pages were already in English.

## Content Map

Stable slugs and paths recorded in `legacy/content-map.yml`.
