# kb:spec-review — Review specs against KB and generate feedback

## Purpose
Compare business/product specifications from sibling repos against the knowledge base in `content/`.
Identify gaps on both sides and generate a feedback list for the integration/dev team.

## When to run
- When a new spec is added to `../api-v1/docs/` or `../app/docs/`
- When a spec is updated (new version, status change)
- Periodically to catch drift between specs and KB
- When user says "review spec" or "spec review"

## Inputs

### Spec sources (fixed paths, do not search)
- **API specs** → `../api-v1/docs/` (business specs, API behaviour)
- **App specs** → `../app/docs/` (product/UI specs, feature definitions)

### KB source
- `content/` — all published Markdown articles
- `build/terminology/dictionary.json` — canonical terminology

### Arguments
- If the user specifies a spec file or feature name, review only that spec
- If no argument, review all specs that have `status: draft` or `status: in-review`
- Use `--all` to review every spec regardless of status

## Process

### Step 1 — Inventory specs
For each `.md` file in the spec directories:
1. Parse the metadata table (Spec ID, Version, Status, Created, Dependencies)
2. Extract the feature/topic from the title and overview
3. Read open issues (checkbox items)
4. Note the spec type: `business-spec` (api-v1) or `product-spec` (app)

### Step 2 — Map specs to KB articles
For each spec, find related KB articles by:
1. Matching product area / feature keywords against KB `product_area`, `tags`, `title`
2. Searching KB body text for feature names mentioned in the spec
3. Checking if the spec's feature is already documented, partially documented, or missing

Classification:
- **Fully covered** — KB has comprehensive docs matching the spec's scope
- **Partially covered** — KB mentions the feature but missing key details from the spec
- **Not covered** — No KB article addresses this feature
- **New feature** — Spec describes something not yet in the product (future)

### Step 3 — Identify gaps: Spec → KB
For each spec, list what the KB is missing:
- New features/behaviours described in the spec but not in any KB article
- Changed behaviours that contradict current KB content
- New settings, fields, or UI elements the admin needs to know about
- New terminology introduced in the spec

### Step 4 — Identify gaps: KB → Spec
For each spec, list what the spec is missing that the KB team needs:
- **User-facing behaviour** not described (how does the admin/client experience this?)
- **Settings/configuration** — where in the UI? what are the options?
- **Edge cases** — what happens when X? error messages?
- **Terminology** — does the spec use canonical Zooza terms? (check against `dictionary.json`)
- **Migration/rollout** — how do existing users get the new feature? any migration steps?
- **Dependencies** — does this affect existing KB articles that need updating?

### Step 5 — Check terminology alignment
Compare terms used in specs against `build/terminology/dictionary.json`:
- Flag non-canonical terms (e.g. "course" instead of "programme", "group" instead of "class")
- List any new terms the spec introduces that should be added to the dictionary

### Step 6 — Generate report

Write `build/reports/spec-review.md` with this structure:

```markdown
# Spec Review Report

**Generated:** YYYY-MM-DD
**Specs reviewed:** N (api: X, app: Y)
**KB articles scanned:** N

## Summary

| Spec ID | Title | Status | KB Coverage | Gaps in KB | Questions for Dev |
|---|---|---|---|---|---|
| BS-001 | Payment Pairer | draft | Partial | 3 | 5 |
| SP-002 | Loyalty Referral | in-review | Not covered | — | 8 |

## Detailed Reviews

### BS-001: Payment Pairer — Managed by Resolution

**Spec:** `../api-v1/docs/business-specs/BS-payment-pairer-managed-by-resolution.md`
**KB coverage:** Partial — mentioned in `content/guides/payment-overview.md` but missing resolution flow

#### Gaps in KB (what we need to document)
1. New "managed by resolution" payment status — not in any KB article
2. Auto-pairing rules — admin needs to know when payments auto-match
3. Manual resolution workflow — step-by-step for admin

#### Questions for Dev Team (what's missing from the spec)
1. Where does the admin see the resolution queue in the UI?
2. What notification does the admin get when a payment needs manual resolution?
3. What happens to existing unmatched payments after rollout?
4. The spec uses "customer" — canonical term is "client"

#### Terminology issues
- "customer" → should be "client"
- "subscription" → should be "booking" (if applicable)

#### Affected KB articles
- `content/guides/payment-overview.md` — needs new section on resolution
- `content/faq/payments-faq.md` — needs new Q&A entries

---
(repeat for each spec)
```

## Terminology enforcement
When reviewing specs, always check against the canonical dictionary:

| Spec term (wrong) | Canonical term |
|---|---|
| course | programme |
| group | class |
| event, lesson | session |
| registration | booking |
| customer | client |
| lecturer, teacher | instructor |

Flag these in the report so the dev team can align their specs too.

## Output

### For dev team
- `build/reports/spec-review.md` — full review report with gaps and questions
- Shareable with dev team for spec validation

### For KB team (consumed by kb:spec-apply)
- `build/reports/spec-review-actions.yml` — structured action list for `kb:spec-apply`

```yaml
# Auto-generated by kb:spec-review — consumed by kb:spec-apply
generated: "2026-02-16"
specs_reviewed: 3

actions:
  - spec_id: "BS-001"
    spec_path: "../api-v1/docs/business-specs/BS-payment-pairer.md"
    spec_title: "Payment Pairer — Managed by Resolution"

    new_articles:
      - suggested_path: "content/guides/payment-resolution.md"
        suggested_title: "Resolving unmatched payments"
        product_area: "Payments"
        type: "guides"
        key_topics:
          - "What is payment resolution"
          - "Auto-pairing rules"
          - "Manual resolution workflow"
        source_sections:
          - "## Business Requirements"
          - "## Functional Requirements"

    update_articles:
      - path: "content/faq/payments-faq.md"
        action: "add_questions"
        questions:
          - "What happens when a payment doesn't match a booking?"
          - "How do I manually resolve an unmatched payment?"

      - path: "content/reference/payments-list.md"
        action: "add_section"
        section_title: "Payment resolution status"
        key_points:
          - "New status: 'Pending resolution'"
          - "Resolution queue in Payments list"

    questions_for_dev:
      - "Where does the admin see the resolution queue?"
      - "What notification does the admin get?"

    terminology_issues:
      - from: "customer"
        to: "client"
```

- Print summary to console when done

## Done definition
Complete when:
- All target specs have been reviewed
- `spec-review.md` written with gaps and questions (for dev team)
- `spec-review-actions.yml` written with structured actions (for kb:spec-apply)
- Terminology issues flagged
- Affected KB articles listed
