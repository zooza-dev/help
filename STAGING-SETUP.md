# Staging deploy — Mac Mini setup

Setup GitHub self-hosted runner on the Mac Mini so every push to `test`
automatically deploys to staging — no GitHub Actions cloud, ~2–3 min per deploy.

---

## How it works

When you push to the `test` branch, GitHub notifies the Mac Mini (which is
permanently connected to GitHub in the background). The Mac Mini runs the
build and uploads to staging directly. No cloud build servers involved.

---

## Step 1 — Install dependencies (once)

Install Homebrew if missing:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Install tools:

```bash
brew install python@3.11 node@20 lftp git
pip3 install pyyaml
```

Verify:

```bash
python3 --version   # 3.11+
node --version      # v20+
lftp --version
```

---

## Step 2 — Register the Mac Mini as a GitHub runner

1. Open the repo on GitHub → **Settings → Actions → Runners → New self-hosted runner**
2. Select **macOS** and your chip (**ARM64** for M-series, **x64** for Intel)
3. GitHub shows a set of commands — run them in Terminal, for example:

```bash
mkdir ~/actions-runner && cd ~/actions-runner
curl -o actions-runner-osx-arm64.tar.gz -L https://github.com/actions/runner/releases/download/vX.X.X/actions-runner-osx-arm64-X.X.X.tar.gz
tar xzf ./actions-runner-osx-arm64.tar.gz
./config.sh --url https://github.com/zooza-dev/help --token TOKEN_FROM_GITHUB
```

> Use the exact commands and token shown by GitHub — the token expires after 1 hour.

When asked for the runner name and labels, press Enter to accept defaults.

---

## Step 3 — Install runner as a background service

So the runner starts automatically on boot and reconnects after restarts:

```bash
cd ~/actions-runner
./svc.sh install
./svc.sh start
```

Verify it is running:

```bash
./svc.sh status
```

You should see `active (running)`.

---

## Step 4 — Add FTP credentials to GitHub Secrets

The deploy workflow needs FTP credentials. Check that these three secrets exist
in the repo (**Settings → Secrets and variables → Actions**):

- `SFTP_USER`
- `SFTP_PASSWORD`
- `SFTP_HOST`

If any are missing, ask Michal for the values.

---

## Step 5 — First node_modules install (once)

The runner clones the repo fresh on first use. After the first run, find the
workspace and pre-install Node dependencies so the first deploy is fast:

```bash
cd ~/actions-runner/_work/help/help/build/exports/docusaurus
npm install --legacy-peer-deps
```

After this, `node_modules` persists between deploys automatically.

---

## Deploying

Just push to `test` as normal — the Mac Mini picks it up and deploys within
2–3 minutes. No manual steps needed.

To trigger a deploy without a code change, go to GitHub →
**Actions → Deploy Help to Staging → Run workflow**.

Result: **https://staging-help.zooza.online/**

---

## Troubleshooting

**Runner shows offline in GitHub Settings → Actions → Runners**
Run `cd ~/actions-runner && ./svc.sh status`. If stopped, run `./svc.sh start`.

**`lftp: command not found`** — run `brew install lftp`

**`python3: command not found`** — run `brew install python@3.11`

**`pip3 install pyyaml` needed again after macOS update** — rerun it.

**FTP upload fails** — verify the three GitHub Secrets are set correctly.

**`npm run build` fails on first run** — run `npm install --legacy-peer-deps`
manually in the workspace `docusaurus/` folder (see Step 5).
