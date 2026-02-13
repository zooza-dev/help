# kb:sync-ids — Write Intercom article IDs from deploy log into content frontmatter and intercom-map.json

## Purpose
After running the Intercom deploy pipeline (GitHub Actions), parse the log output to extract article IDs and write them back into:
1. The corresponding `content/**/*.md` files' YAML frontmatter
2. The `build/exports/targets/intercom/intercom-map.json` mapping file

This prevents duplicate article creation on subsequent deploys.

## When to use
Run this skill after every Intercom Help Center deploy. The user will paste the GitHub Actions log output.

## Inputs
- Pasted GitHub Actions log text (from the deploy step)
- All `.md` files in `content/` (excluding `_shared/` and files starting with `_`)
- Existing `build/exports/targets/intercom/intercom-map.json` (if present)

## What to parse
Extract article title → ID mappings from log lines matching these patterns:
- `Created article 'TITLE' -> ID` — newly created articles
- `Updated article 'TITLE' (id=ID)` — updated articles

Also extract collection and section mappings from:
- `Found existing collection 'NAME' -> ID` or `Created collection 'NAME' -> ID`
- `Found existing section 'NAME' -> ID` or `Created section 'NAME' -> ID`

## What to do

### Step 1 — Update content frontmatter
For each extracted article title/ID pair:
1. Find the content file whose frontmatter `title` matches the extracted title (exact match)
2. Set `intercom_id: <ID>` in the file's YAML frontmatter (as integer)
3. Set `intercom_sync: false` in the file's YAML frontmatter
4. If `intercom_id` already exists and differs from the new ID, warn but update it
5. If no content file matches a title, report it as unmatched

### Step 2 — Update intercom-map.json
Read existing `build/exports/targets/intercom/intercom-map.json` (or create it if missing).
The file structure is:
```json
{
  "collections": { "CollectionName": 12345 },
  "sections": { "SectionName": 12345 },
  "articles": { "slug": 12345 }
}
```
For each matched article, add/update `articles[slug] = intercom_id` (using the file's frontmatter `slug`).
For each collection/section from the log, add/update the corresponding entry.
Write the updated JSON back (sorted keys, 2-space indent).

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
- intercom-map.json entries added/updated
- Unmatched titles (in log but no matching content file)
- Duplicate ID warnings (if any)

## Done definition
Complete when all matched articles have `intercom_id` and `intercom_sync: false` in their frontmatter, `intercom-map.json` is updated, and a summary has been printed.
