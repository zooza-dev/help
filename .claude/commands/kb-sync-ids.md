# kb:sync-ids — Write Intercom article IDs from deploy log into content frontmatter

## Purpose
After running the Intercom deploy pipeline (GitHub Actions), parse the log output to extract article IDs and write them back into the corresponding `content/**/*.md` files' frontmatter. This prevents duplicate article creation on subsequent deploys.

## When to use
Run this skill after every Intercom Help Center deploy. The user will paste the GitHub Actions log output.

## Inputs
- Pasted GitHub Actions log text (from the deploy step)
- All `.md` files in `content/` (excluding `_shared/` and files starting with `_`)

## What to parse
Extract article title → ID mappings from log lines matching these patterns:
- `Created article 'TITLE' -> ID` — newly created articles
- `Updated article 'TITLE' (id=ID)` — updated articles

## What to do
For each extracted title/ID pair:
1. Find the content file whose frontmatter `title` matches the extracted title (exact match)
2. Set `intercom_id: <ID>` in the file's YAML frontmatter (as integer)
3. Set `intercom_sync: false` in the file's YAML frontmatter
4. If `intercom_id` already exists and differs from the new ID, warn but update it
5. If no content file matches a title, report it as unmatched

## Frontmatter placement
Place `intercom_id` and `intercom_sync` at the end of the frontmatter block, just before the closing `---`. If they already exist, update them in place.

## Safety
- Never modify the Markdown body content, only frontmatter
- Never modify files under `_shared/` or files starting with `_`
- Verify no two files end up with the same `intercom_id` — if a duplicate would be created, warn and skip

## Output report
Print a summary:
- Total articles found in log
- Files updated with IDs
- Files already up to date (ID unchanged)
- Unmatched titles (in log but no matching content file)
- Duplicate ID warnings (if any)

## Done definition
Complete when all matched articles have `intercom_id` and `intercom_sync: false` in their frontmatter, and a summary has been printed.
