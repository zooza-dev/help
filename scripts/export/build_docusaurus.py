#!/usr/bin/env python3
"""Build Docusaurus 3 export from the Zooza Help KB.

Reads content/ → writes build/exports/docusaurus/

The output is a complete, ready-to-run Docusaurus 3 project.
Images are copied from assets/images/ → static/img/.
Frontmatter is converted: internal KB fields are stripped,
URLs are rewritten to match the /help/{product_area}/{slug} scheme.

Usage:
    python3 scripts/export/build_docusaurus.py
    python3 scripts/export/build_docusaurus.py --dry-run
"""

import json
import logging
import re
import shutil
import sys
from pathlib import Path

import yaml

logger = logging.getLogger(__name__)

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
CONTENT_DIR = ROOT_DIR / "content"
ASSETS_IMAGES_DIR = ROOT_DIR / "assets" / "images"
ASSETS_BRAND_DIR = ROOT_DIR / "assets" / "brand"
OUTPUT_DIR = ROOT_DIR / "build" / "exports" / "docusaurus"
DOCS_DIR = OUTPUT_DIR / "docs"
STATIC_DIR = OUTPUT_DIR / "static"

# Product areas in sidebar display order
PRODUCT_AREA_ORDER = [
    "Programmes",
    "Classes",
    "Calendar",
    "Bookings",
    "Orders",
    "Clients",
    "Payments",
    "Settings",
    "Widgets",
    "Communication",
]

# Doc types: (internal_name, sidebar_label, sidebar_position)
TYPE_ORDER = [
    ("setup", "Setup", 1),
    ("guides", "Guides", 2),
    ("reference", "Reference", 3),
    ("payments", "Payments", 4),
    ("troubleshooting", "Troubleshooting", 5),
    ("faq", "FAQ", 6),
]
TYPE_POSITION = {t[0]: t[2] for t in TYPE_ORDER}
TYPE_LABELS = {t[0]: t[1] for t in TYPE_ORDER}

# Internal-only KB fields that should NOT appear in the Docusaurus output
INTERNAL_FIELDS = {
    "source_legacy_path",
    "source_language",
    "needs_screenshot_replacement",
    "last_converted",
    "intercom_id",
    "intercom_sync",
    "type",
    "product_area",
    "sub_area",
    "audience",
    "status",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and return (metadata, body)."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return {}, text
    fm = yaml.safe_load(m.group(1)) or {}
    return fm, text[m.end():]


def extract_description(body: str) -> str:
    """Extract the first meaningful paragraph as a description (max 160 chars)."""
    # Strip H1 line
    body = re.sub(r"^# .+\n+", "", body.strip())
    for para in body.split("\n\n"):
        para = para.strip()
        if not para:
            continue
        if para.startswith("#") or para.startswith("![") or para.startswith("|"):
            continue
        # Strip markdown formatting for plain-text description
        clean = re.sub(r"[*_`]", "", para)
        clean = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", clean)
        clean = clean.replace("\n", " ").strip()
        if len(clean) > 10:
            return clean[:157] + "..." if len(clean) > 160 else clean
    return ""


def fix_image_paths(body: str) -> str:
    """Rewrite relative assets/images/ paths to Docusaurus /img/ paths."""
    body = re.sub(r"\.\./\.\./assets/images/", "/img/", body)
    body = re.sub(r"\.\./assets/images/", "/img/", body)
    return body


def fix_mdx_html(body: str) -> str:
    """Fix HTML void elements for MDX compatibility (JSX requires self-closing tags)."""
    body = re.sub(r"<br\s*>", "<br />", body)
    body = re.sub(r"<hr\s*>", "<hr />", body)
    body = re.sub(r"<img([^>]*[^/])>", r"<img\1 />", body)
    return body


def fix_internal_links(body: str, slug_to_url: dict[str, str]) -> str:
    """Rewrite relative .md links to absolute /help/... URLs using the slug map.

    Handles patterns like:
      ../guides/some-slug.md  →  /help/area/some-slug
      some-slug.md            →  /help/area/some-slug
      some-slug.md#anchor     →  /help/area/some-slug#anchor
    """
    def replace_link(m: re.Match) -> str:
        text = m.group(1)
        target = m.group(2)
        # Split off anchor
        anchor = ""
        if "#" in target:
            target, anchor = target.split("#", 1)
            anchor = "#" + anchor
        # Extract filename stem
        stem = Path(target).stem
        if stem in slug_to_url:
            return f"[{text}]({slug_to_url[stem]}{anchor})"
        return m.group(0)  # leave unchanged if not found

    return re.sub(r"\[([^\]]+)\]\(([^)]+\.md[^)]*)\)", replace_link, body)


def to_docusaurus_frontmatter(fm: dict, body: str, position: int) -> dict:
    """Convert rich KB frontmatter to minimal Docusaurus frontmatter."""
    product_area = fm.get("product_area", "Settings")
    area_slug = product_area.lower().replace(" ", "-")
    slug = fm.get("slug", "")

    doca: dict = {}

    if fm.get("title"):
        doca["title"] = fm["title"]

    # Explicit slug — routeBasePath is '/' so slug IS the full URL path.
    if slug:
        doca["slug"] = f"/{area_slug}/{slug}"

    desc = extract_description(body)
    if desc:
        doca["description"] = desc

    if fm.get("tags"):
        doca["tags"] = fm["tags"]

    if fm.get("status") == "draft":
        doca["draft"] = True

    doca["sidebar_position"] = position

    return doca


def write_category_json(folder: Path, label: str, position: int, index: bool = False) -> None:
    """Write _category_.json. If index=True, generates a category landing page (for navbar links)."""
    folder.mkdir(parents=True, exist_ok=True)
    data: dict = {"label": label, "position": position, "collapsed": True}
    if index:
        data["link"] = {"type": "generated-index", "title": label}
    (folder / "_category_.json").write_text(
        json.dumps(data, indent=2) + "\n", encoding="utf-8"
    )


# ---------------------------------------------------------------------------
# Static file templates
# ---------------------------------------------------------------------------

_PACKAGE_JSON = {
    "name": "zooza-help",
    "version": "0.0.0",
    "private": True,
    "scripts": {
        "docusaurus": "docusaurus",
        "start": "docusaurus start",
        "build": "docusaurus build --out-dir dist",
        "serve": "docusaurus serve",
        "clear": "docusaurus clear",
    },
    "dependencies": {
        "@docusaurus/core": "^3.6.0",
        "@docusaurus/preset-classic": "^3.6.0",
        "@docusaurus/plugin-client-redirects": "^3.6.0",
        "clsx": "^2.0.0",
        "prism-react-renderer": "^2.3.0",
        "react": "^18.0.0",
        "react-dom": "^18.0.0",
    },
    "devDependencies": {
        "@docusaurus/module-type-aliases": "^3.6.0",
        "@docusaurus/types": "^3.6.0",
    },
    "engines": {"node": ">=18.0"},
    "browserslist": {
        "production": [">0.5%", "not dead", "not op_mini all"],
        "development": [
            "last 1 chrome version",
            "last 1 firefox version",
            "last 1 safari version",
        ],
    },
}

_DOCUSAURUS_CONFIG = """\
// @ts-check
// Auto-generated by scripts/export/build_docusaurus.py — do not edit directly.
const { themes: prismThemes } = require('prism-react-renderer');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Zooza Help',
  tagline: 'Help and guides for Zooza studio management software',
  favicon: 'img/favicon.ico',
  url: 'https://help.zooza.app',
  baseUrl: '/',

  organizationName: 'zooza',
  projectName: 'zooza-help',

  onBrokenLinks: 'warn',
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // routeBasePath '/' means docs are served from the root, like api-docs
          routeBasePath: '/',
          editUrl: undefined,
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
        sitemap: {
          changefreq: 'weekly',
          priority: 0.7,
          ignorePatterns: ['/tags/**'],
          filename: 'sitemap.xml',
        },
      }),
    ],
  ],

  plugins: [
    // plugin-client-redirects is available for future use (production-only).
    // Root redirect is handled by src/pages/index.js (works in dev + prod).
    // ['@docusaurus/plugin-client-redirects', { redirects: [] }],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      image: 'img/social-card.png',

      navbar: {
        title: 'Zooza Help',
        logo: {
          alt: 'Zooza',
          src: 'img/logo.svg',
          srcDark: 'img/logo-dark.svg',
        },
        items: [
          { to: '/category/programmes', label: 'Programmes', position: 'left' },
          { to: '/category/classes', label: 'Classes', position: 'left' },
          { to: '/category/bookings', label: 'Bookings', position: 'left' },
          { to: '/category/clients', label: 'Clients', position: 'left' },
          { to: '/category/payments', label: 'Payments', position: 'left' },
          { to: '/category/settings', label: 'Settings', position: 'left' },
          {
            href: 'https://zooza.app',
            label: 'Go to app',
            position: 'right',
          },
        ],
      },

      footer: {
        style: 'dark',
        links: [
          {
            title: 'Help topics',
            items: [
              { label: 'Programmes', to: '/category/programmes' },
              { label: 'Classes', to: '/category/classes' },
              { label: 'Calendar', to: '/category/calendar' },
              { label: 'Clients', to: '/category/clients' },
              { label: 'Payments', to: '/category/payments' },
              { label: 'Settings', to: '/category/settings' },
            ],
          },
          {
            title: 'More',
            items: [
              { label: 'Zooza App', href: 'https://zooza.app' },
              { label: 'Zooza Website', href: 'https://zooza.online' },
              { label: 'Support', href: 'mailto:support@zooza.online' },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Zooza. All rights reserved.`,
      },

      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },

      colorMode: {
        defaultMode: 'light',
        disableSwitch: false,
        respectPrefersColorScheme: true,
      },

      // Algolia search — configure after deploying.
      // algolia: {
      //   appId: 'YOUR_APP_ID',
      //   apiKey: 'YOUR_SEARCH_API_KEY',
      //   indexName: 'zooza_help',
      //   contextualSearch: true,
      // },
    }),
};

module.exports = config;
"""

_SIDEBARS_JS = """\
// @ts-check
// Auto-generated by scripts/export/build_docusaurus.py — do not edit directly.

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  // Docusaurus auto-builds the sidebar from _category_.json files and
  // sidebar_position frontmatter in each doc.
  helpSidebar: [{ type: 'autogenerated', dirName: '.' }],
};

module.exports = sidebars;
"""

_CUSTOM_CSS = """\
/* ─────────────────────────────────────────────
   Zooza brand tokens mapped to Docusaurus vars
   Source: zooza_css/_shared/_presets.scss
   Auto-generated by scripts/export/build_docusaurus.py
───────────────────────────────────────────── */

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap');

:root {
  /* Primary orange */
  --ifm-color-primary: #fa6900;
  --ifm-color-primary-dark: #e15e00;
  --ifm-color-primary-darker: #b36325;
  --ifm-color-primary-darkest: #7a4418;
  --ifm-color-primary-light: #fb8133;
  --ifm-color-primary-lighter: #fc9a5d;
  --ifm-color-primary-lightest: #fdb386;

  /* Typography */
  --ifm-font-family-base: 'DM Sans', system-ui, -apple-system, sans-serif;
  --ifm-font-family-monospace: 'JetBrains Mono', 'Fira Code', 'Fira Mono', 'Roboto Mono', monospace;
  --ifm-font-size-base: 16px;
  --ifm-line-height-base: 1.65;

  /* Spacing & shape */
  --ifm-global-radius: 5px;
  --ifm-button-border-radius: 5px;
  --ifm-card-border-radius: 8px;
  --ifm-code-border-radius: 5px;
  --ifm-pre-border-radius: 8px;

  /* Background */
  --ifm-background-color: #f2f5e5;
  --ifm-background-surface-color: #ffffff;
  --ifm-navbar-background-color: #ffffff;
  --ifm-footer-background-color: #4d4f46;

  /* Teal accent (secondary) */
  --zooza-teal: #3aa39d;
  --zooza-teal-light: #a7dbd8;
  --zooza-teal-lightest: #f0f5f3;

  /* Grays */
  --zooza-gray-base: #e0e4cc;
  --zooza-gray-dark: #4d4f46;
  --zooza-gray-light: #878a7a;
  --zooza-gray-lighter: #f2f5e5;

  /* Code */
  --ifm-code-background: #eef0f1;
  --ifm-code-font-size: 90%;
  --docusaurus-highlighted-code-line-bg: rgba(250, 105, 0, 0.08);

  /* Links */
  --ifm-link-color: #fa6900;
  --ifm-link-hover-color: #b36325;

  /* Borders */
  --ifm-color-emphasis-200: #e0e4cc;
  --ifm-color-emphasis-300: #c0c4b1;

  /* Navbar */
  --ifm-navbar-height: 60px;
  --ifm-navbar-shadow: 0 1px 2px rgba(0, 0, 0, 0.08);
}

/* ── Dark mode ── */
[data-theme='dark'] {
  --ifm-color-primary: #ff8c42;
  --ifm-color-primary-dark: #fa6900;
  --ifm-color-primary-darker: #c76521;
  --ifm-color-primary-darkest: #7a4418;
  --ifm-color-primary-light: #ffa06a;
  --ifm-color-primary-lighter: #ffb48e;
  --ifm-color-primary-lightest: #ffc8b2;

  --ifm-background-color: #1e1f1c;
  --ifm-background-surface-color: #2a2c28;
  --ifm-navbar-background-color: #1e1f1c;
  --ifm-footer-background-color: #1e1f1c;

  --zooza-teal: #3aa39d;
  --zooza-teal-light: #5c9794;

  --ifm-code-background: #2a2c28;
  --docusaurus-highlighted-code-line-bg: rgba(255, 140, 66, 0.12);

  --ifm-link-color: #ff8c42;
  --ifm-link-hover-color: #ffa06a;

  --ifm-color-emphasis-200: #545550;
  --ifm-color-emphasis-300: #6e726b;
}

/* ─────────────────────────────────────────────
   Global base styles
───────────────────────────────────────────── */

body {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* ── Navbar ── */
.navbar {
  border-bottom: 1px solid var(--zooza-gray-base);
}

[data-theme='dark'] .navbar {
  border-bottom: 1px solid var(--ifm-color-emphasis-200);
}

.navbar__title {
  font-weight: 700;
  letter-spacing: -0.01em;
}

/* ── Sidebar ── */
.menu__link--active {
  color: var(--ifm-color-primary);
  font-weight: 600;
}

/* ── Article / doc content ── */
.markdown h1 {
  font-size: 2rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  margin-bottom: 1rem;
}

.markdown h2 {
  font-size: 1.4rem;
  font-weight: 600;
  letter-spacing: -0.01em;
  margin-top: 2.5rem;
  padding-bottom: 0.4rem;
  border-bottom: 1px solid var(--ifm-color-emphasis-200);
}

.markdown h3 {
  font-size: 1.1rem;
  font-weight: 600;
  margin-top: 1.8rem;
}

/* ── Tables ── */
.markdown table {
  font-size: 0.9rem;
}

.markdown table th {
  background: var(--zooza-gray-lighter);
  font-weight: 600;
}

[data-theme='dark'] .markdown table th {
  background: #2a2c28;
}

/* ── Code ── */
.markdown code {
  background: var(--ifm-code-background);
  border: 1px solid var(--ifm-color-emphasis-200);
  padding: 0.1em 0.4em;
  border-radius: var(--ifm-code-border-radius);
}

/* ── Admonitions — match Zooza palette ── */
.alert--tip {
  --ifm-alert-border-color: var(--zooza-teal);
  --ifm-alert-background-color: var(--zooza-teal-lightest);
}

[data-theme='dark'] .alert--tip {
  --ifm-alert-background-color: rgba(58, 163, 157, 0.12);
}

.alert--warning {
  --ifm-alert-border-color: #fa6900;
  --ifm-alert-background-color: #fce7d5;
}

[data-theme='dark'] .alert--warning {
  --ifm-alert-background-color: rgba(250, 105, 0, 0.12);
}

/* ── Footer ── */
.footer__link-item {
  font-size: 0.875rem;
}

/* ── Breadcrumbs ── */
.breadcrumbs__link {
  font-size: 0.82rem;
}
"""

_README = """\
# Zooza Help — Docusaurus preview

> **This folder is auto-generated.** Do not edit files here directly.
> Re-run `python3 scripts/export/build_docusaurus.py` to regenerate.

## Quick start

Requires Node.js 18 or later.

```bash
npm install
npm start
```

Then open http://localhost:3000/help in your browser.

## Full guide

See [DOCUSAURUS-PREVIEW.md](../../../DOCUSAURUS-PREVIEW.md) in the repo root
for a step-by-step guide written for non-developers.
"""


# ---------------------------------------------------------------------------
# Writer helpers
# ---------------------------------------------------------------------------


def _write_package_json(out: Path) -> None:
    (out / "package.json").write_text(
        json.dumps(_PACKAGE_JSON, indent=2) + "\n", encoding="utf-8"
    )


def _write_docusaurus_config(out: Path) -> None:
    (out / "docusaurus.config.js").write_text(_DOCUSAURUS_CONFIG, encoding="utf-8")


def _write_sidebars(out: Path) -> None:
    (out / "sidebars.js").write_text(_SIDEBARS_JS, encoding="utf-8")


_HOMEPAGE_JS = """\
import React from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import styles from './index.module.css';

const CATEGORIES = [
  { label: 'Programmes',    to: '/category/programmes',   description: 'Create and manage your programmes, pricing, and settings.' },
  { label: 'Classes',       to: '/category/classes',      description: 'Set up class schedules, sessions, and instructor assignments.' },
  { label: 'Bookings',      to: '/category/bookings',     description: 'Create and manage client bookings and registrations.' },
  { label: 'Calendar',      to: '/category/calendar',     description: 'Track sessions, attendance, and instructor schedules.' },
  { label: 'Clients',       to: '/category/clients',      description: 'Manage client profiles, attendance, and communication.' },
  { label: 'Payments',      to: '/category/payments',     description: 'Set up payment templates, track invoices, and manage debt.' },
  { label: 'Settings',      to: '/category/settings',     description: 'Configure holidays, billing periods, roles, and integrations.' },
  { label: 'Widgets',       to: '/category/widgets',      description: 'Embed booking forms and calendars on your website.' },
  { label: 'Communication', to: '/category/communication',description: 'Set up email and WhatsApp templates and automated messages.' },
];

export default function Home() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout title="Help" description={siteConfig.tagline}>
      <main className={styles.main}>
        <div className={styles.hero}>
          <h1>How can we help you?</h1>
          <p>Browse guides, setup instructions, and FAQs for Zooza.</p>
        </div>
        <div className={styles.grid}>
          {CATEGORIES.map((cat) => (
            <Link key={cat.to} to={cat.to} className={styles.card}>
              <h2>{cat.label}</h2>
              <p>{cat.description}</p>
            </Link>
          ))}
        </div>
      </main>
    </Layout>
  );
}
"""

_HOMEPAGE_CSS = """\
.main {
  max-width: 1100px;
  margin: 0 auto;
  padding: 2rem 1.5rem 4rem;
}

.hero {
  text-align: center;
  padding: 3rem 1rem 2rem;
}

.hero h1 {
  font-size: 2.2rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.hero p {
  font-size: 1.1rem;
  color: var(--ifm-color-emphasis-600);
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.25rem;
  margin-top: 1rem;
}

.card {
  display: block;
  background: var(--ifm-background-surface-color);
  border: 1px solid var(--ifm-color-emphasis-200);
  border-radius: var(--ifm-card-border-radius);
  padding: 1.5rem;
  text-decoration: none !important;
  color: inherit !important;
  transition: box-shadow 0.15s ease, border-color 0.15s ease;
}

.card:hover {
  border-color: var(--ifm-color-primary);
  box-shadow: 0 2px 12px rgba(250, 105, 0, 0.12);
}

.card h2 {
  font-size: 1.1rem;
  font-weight: 600;
  margin: 0 0 0.4rem;
  color: var(--ifm-color-primary);
}

.card p {
  font-size: 0.9rem;
  color: var(--ifm-color-emphasis-700);
  margin: 0;
  line-height: 1.5;
}
"""


def _write_custom_css(out: Path) -> None:
    (out / "src" / "css").mkdir(parents=True, exist_ok=True)
    (out / "src" / "css" / "custom.css").write_text(_CUSTOM_CSS, encoding="utf-8")
    (out / "src" / "pages").mkdir(parents=True, exist_ok=True)
    (out / "src" / "pages" / "index.js").write_text(_HOMEPAGE_JS, encoding="utf-8")
    (out / "src" / "pages" / "index.module.css").write_text(_HOMEPAGE_CSS, encoding="utf-8")


def _write_gitignore(out: Path) -> None:
    (out / ".gitignore").write_text(
        "node_modules/\n.docusaurus/\nbuild/\ndist/\n", encoding="utf-8"
    )


def _write_readme(out: Path) -> None:
    (out / "README.md").write_text(_README, encoding="utf-8")


# ---------------------------------------------------------------------------
# Main export
# ---------------------------------------------------------------------------


def build_docusaurus(dry_run: bool = False, clean: bool = False) -> dict:
    """Export the KB to a Docusaurus project. Returns stats dict."""

    # --- Collect and group docs ---
    docs_by_area: dict[str, dict[str, list]] = {}
    skipped = 0

    for md_path in sorted(CONTENT_DIR.rglob("*.md")):
        if "/_shared/" in str(md_path) or md_path.name.startswith("_"):
            continue

        text = md_path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)

        if not fm.get("slug"):
            logger.warning("Skipping %s: no slug in frontmatter", md_path.name)
            skipped += 1
            continue

        if fm.get("status") == "archived":
            logger.debug("Skipping archived: %s", md_path.name)
            skipped += 1
            continue

        area = fm.get("product_area", "Settings")
        doc_type = fm.get("type", "guides")
        docs_by_area.setdefault(area, {}).setdefault(doc_type, []).append(
            (fm, body, md_path)
        )

    total_docs = sum(
        len(docs) for types in docs_by_area.values() for docs in types.values()
    )

    if dry_run:
        logger.info(
            "DRY RUN: %d docs across %d product areas (skipped: %d)",
            total_docs,
            len(docs_by_area),
            skipped,
        )
        return {"dry_run": True, "docs": total_docs, "areas": len(docs_by_area)}

    # --- Prepare output directory ---
    if clean:
        # Full wipe (used in CI — node_modules are reinstalled fresh each run anyway)
        if OUTPUT_DIR.exists():
            shutil.rmtree(OUTPUT_DIR)
    else:
        # Preserve node_modules/ and .docusaurus/ for faster local iteration
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        for subdir in ("docs", "static", "src"):
            target = OUTPUT_DIR / subdir
            if target.exists():
                shutil.rmtree(target)
    DOCS_DIR.mkdir(parents=True)
    STATIC_DIR.mkdir(parents=True)

    # --- Copy images ---
    img_out = STATIC_DIR / "img"
    if ASSETS_IMAGES_DIR.exists():
        shutil.copytree(ASSETS_IMAGES_DIR, img_out)
        logger.info("Copied images → static/img/ (%d files)", len(list(img_out.iterdir())))
    else:
        img_out.mkdir(parents=True)
        logger.warning("No assets/images/ directory found; static/img/ will be empty")

    # --- Copy brand assets (logo, favicon) ---
    if ASSETS_BRAND_DIR.exists():
        for brand_file in ASSETS_BRAND_DIR.iterdir():
            shutil.copy2(brand_file, img_out / brand_file.name)
        logger.info("Copied brand assets → static/img/ (%d files)", len(list(ASSETS_BRAND_DIR.iterdir())))
    else:
        logger.warning("No assets/brand/ directory found; logo and favicon will be missing")

    # --- Build slug → URL map for internal link rewriting ---
    slug_to_url: dict[str, str] = {}
    for area, types in docs_by_area.items():
        area_slug = area.lower().replace(" ", "-")
        for type_docs in types.values():
            for fm, _body, _src in type_docs:
                slug = fm.get("slug", "")
                if slug:
                    slug_to_url[slug] = f"/{area_slug}/{slug}"

    # --- Write docs ---
    doc_count = 0
    known_areas = set(PRODUCT_AREA_ORDER)

    def _export_area(area: str, area_idx: int) -> None:
        nonlocal doc_count
        area_slug = area.lower().replace(" ", "-")
        area_dir = DOCS_DIR / area_slug
        # index=True generates a landing page at /help/{area}/ for navbar links
        write_category_json(area_dir, area, area_idx, index=True)

        for type_name, type_label, type_pos in TYPE_ORDER:
            if type_name not in docs_by_area.get(area, {}):
                continue

            type_dir = area_dir / type_name
            write_category_json(type_dir, type_label, type_pos)

            for doc_pos, (fm, body, _src) in enumerate(
                docs_by_area[area][type_name], start=1
            ):
                doca_fm = to_docusaurus_frontmatter(fm, body, doc_pos)
                body_out = fix_image_paths(body)
                body_out = fix_mdx_html(body_out)
                body_out = fix_internal_links(body_out, slug_to_url)

                fm_yaml = yaml.dump(
                    doca_fm,
                    allow_unicode=True,
                    default_flow_style=False,
                    sort_keys=False,
                )
                out_file = type_dir / f"{fm['slug']}.md"
                out_file.write_text(
                    f"---\n{fm_yaml}---\n\n{body_out}", encoding="utf-8"
                )
                doc_count += 1

    # Export in defined order first, then any remaining unknown areas
    for idx, area in enumerate(PRODUCT_AREA_ORDER, start=1):
        if area in docs_by_area:
            _export_area(area, idx)

    for area in sorted(docs_by_area):
        if area not in known_areas:
            _export_area(area, 99)

    # --- Write config files ---
    _write_package_json(OUTPUT_DIR)
    _write_docusaurus_config(OUTPUT_DIR)
    _write_sidebars(OUTPUT_DIR)
    _write_custom_css(OUTPUT_DIR)
    _write_gitignore(OUTPUT_DIR)
    _write_readme(OUTPUT_DIR)

    logger.info("Docusaurus export complete: %d docs → %s", doc_count, OUTPUT_DIR)
    return {
        "docs_exported": doc_count,
        "skipped": skipped,
        "output": str(OUTPUT_DIR),
    }


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    dry_run = "--dry-run" in sys.argv
    clean = "--clean" in sys.argv
    stats = build_docusaurus(dry_run=dry_run, clean=clean)

    if dry_run:
        print(f"DRY RUN: {stats['docs']} docs in {stats['areas']} areas")
    else:
        print(f"Exported {stats['docs_exported']} docs → {stats['output']}")
        print(f"Skipped  {stats['skipped']} (archived or missing slug)")
        print()
        print("To preview:")
        print(f"  cd {stats['output']}")
        print("  npm install && npm start")
        print("  → open http://localhost:3000/help")


if __name__ == "__main__":
    main()
