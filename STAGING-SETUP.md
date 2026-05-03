# Staging deploy — Mac Mini setup

One-time setup for deploying Help to staging directly from this machine.
After setup, deploying takes ~2–3 minutes instead of 18 via GitHub Actions.

---

## Prerequisites

Install via Homebrew (install Homebrew first if missing):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then:

```bash
brew install python@3.11 node@20 lftp git
```

Verify:

```bash
python3 --version   # 3.11+
node --version      # v20+
lftp --version
git --version
```

---

## Clone the repo

```bash
cd ~
git clone git@github.com:zooza-dev/help.git
cd help
git checkout test
```

If you get a permission error, you need SSH access to the repo — ask Michal to add your SSH key to GitHub.

---

## Install Node dependencies (once)

```bash
cd ~/help/build/exports/docusaurus
npm install --legacy-peer-deps
```

This takes a few minutes the first time. After that, it is skipped automatically unless `package.json` changes.

---

## Add FTP credentials

Create the file `~/help/.env.staging` (ask Michal for the values — they are in GitHub Secrets):

```
SFTP_USER=...
SFTP_PASSWORD=...
SFTP_HOST=...
```

> This file is in `.gitignore` — never commit it.

---

## Deploy

```bash
bash ~/help/scripts/deploy-staging.sh
```

The script:
1. Pulls latest from `test` branch
2. Generates Docusaurus source files
3. Skips `npm install` if dependencies have not changed
4. Builds the site
5. Uploads changed files to staging via FTP

Result: **https://staging-help.zooza.online/**

---

## Troubleshooting

**`lftp: command not found`** — run `brew install lftp`

**`python3: command not found`** — run `brew install python@3.11`

**FTP upload fails / times out** — check that the Mac Mini has internet access and the credentials in `.env.staging` are correct.

**`npm run build` fails** — run `npm install --legacy-peer-deps` manually in `build/exports/docusaurus/` and try again.
