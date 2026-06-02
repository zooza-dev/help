#!/usr/bin/env bash
# Deploy Help to STAGING from local Mac Mini.
# Run: bash scripts/deploy-staging.sh
#
# ⚠️  THIS SCRIPT DEPLOYS TO STAGING ONLY — NOT PRODUCTION.
#    For production use GitHub Actions: deploy-help-production workflow.
#
# Reads credentials from .env.staging in repo root (never commit that file).
# First-time setup: see STAGING-SETUP.md

set -e

# ── Safety guard — prevent accidental production use ──────────────────────────
if [[ "${FORCE_STAGING:-}" != "yes" ]]; then
  echo ""
  echo "⚠️  This script deploys to STAGING (staging-help.zooza.online)."
  echo "   For production, trigger the GitHub Actions workflow instead."
  echo ""
  read -r -p "Continue with STAGING deploy? [y/N] " confirm
  if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
    echo "Aborted."
    exit 0
  fi
fi

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ENV_FILE="$REPO_ROOT/.env.staging"
DOCUSAURUS_DIR="$REPO_ROOT/build/exports/docusaurus"

# ── Check credentials file ──────────────────────────────────────────────────
if [ ! -f "$ENV_FILE" ]; then
  echo "ERROR: $ENV_FILE not found."
  echo "Create it with:"
  echo "  SFTP_USER=..."
  echo "  SFTP_PASSWORD=..."
  echo "  SFTP_HOST=..."
  exit 1
fi

export $(grep -v '^#' "$ENV_FILE" | xargs)

if [ -z "$SFTP_USER" ] || [ -z "$SFTP_PASSWORD" ] || [ -z "$SFTP_HOST" ]; then
  echo "ERROR: .env.staging is missing SFTP_USER, SFTP_PASSWORD or SFTP_HOST."
  exit 1
fi

# ── Pull latest ──────────────────────────────────────────────────────────────
echo ""
echo "── Step 1: git pull ──"
git -C "$REPO_ROOT" pull origin test

# ── Python build (Docusaurus source files) ───────────────────────────────────
echo ""
echo "── Step 2: Generate Docusaurus export ──"
python3 "$REPO_ROOT/scripts/export/build_docusaurus.py" --clean --staging

# ── npm install (only if node_modules missing or package.json changed) ───────
echo ""
echo "── Step 3: npm install (skipped if node_modules up to date) ──"
cd "$DOCUSAURUS_DIR"
if [ ! -d node_modules ] || [ package.json -nt node_modules ]; then
  npm install --legacy-peer-deps
else
  echo "  node_modules OK, skipping."
fi

# ── Docusaurus build ─────────────────────────────────────────────────────────
echo ""
echo "── Step 4: Build site ──"
npm run build

# ── Upload via FTP ───────────────────────────────────────────────────────────
echo ""
echo "── Step 5: Upload to staging ──"
lftp -u "$SFTP_USER,$SFTP_PASSWORD" \
  -e "set ssl:verify-certificate no; \
      set net:timeout 30; \
      set net:max-retries 2; \
      set mirror:parallel-transfer-count 5; \
      mirror --reverse --delete --verbose ./dist/ /zooza.online/sub/staging-help/; \
      quit" \
  ftp://$SFTP_HOST

echo ""
echo "✓ Staging deploy complete."
echo "  https://staging-help.zooza.online/"
