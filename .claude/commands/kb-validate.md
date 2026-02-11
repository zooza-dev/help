# kb:validate

Validate the knowledge base in `content/` and write a report.

## What to check
- required frontmatter present for every doc
- unique `slug`
- exactly one H1 per doc
- no skipped heading levels
- no broken internal links
- all referenced assets exist in `assets/`

## Outputs
- `build/reports/validation-report.md`

## Guidance
If you fix issues, prefer minimal diffs and preserve existing slugs and URLs.
