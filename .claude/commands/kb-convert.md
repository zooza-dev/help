# kb:convert

Convert legacy Zooza HTML knowledge base into English Markdown in `content/`, normalize assets, extract FAQs, create redirects, and write a conversion report.

## Inputs
- `legacy/html/` (HTML)
- `legacy/assets/` (images/attachments)

## Outputs
- `legacy/manifest.json`
- `legacy/content-map.yml`
- `assets/images/` (normalized)
- `content/**` (English Markdown with required frontmatter)
- `content/_redirects.yml`
- `build/normalized/**`
- `build/reports/conversion-report.md`

## Runbook
Follow the full conversion contract in `claude.md` exactly (Steps A–J).

## Notes
- Do not block conversion due to Slovak screenshots; set `needs_screenshot_replacement: true` instead.
- Keep slugs stable; only change slugs if strictly necessary (collision).
- New/converted files must have `intercom_sync: true` and no `intercom_id` in frontmatter (they are new articles that need to be deployed).
