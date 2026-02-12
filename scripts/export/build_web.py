#!/usr/bin/env python3
"""Generate a minimal static HTML site from content/ Markdown files.

Output: build/exports/web/
  - index.html with navigation by product_area and doc type
  - /help/<product-area>/<slug>/index.html per article
  - assets/ copied from project assets/
"""

import logging
import os
import re
import shutil
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, BaseLoader

logger = logging.getLogger(__name__)

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
CONTENT_DIR = ROOT_DIR / "content"
ASSETS_DIR = ROOT_DIR / "assets"
OUTPUT_DIR = ROOT_DIR / "build" / "exports" / "web"

# --- Jinja2 Templates (inline to stay dependency-light) ---

BASE_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{ title }} — Zooza Help</title>
  <style>
    :root { --accent: #2563eb; --bg: #fff; --fg: #1e293b; --muted: #64748b; --border: #e2e8f0; }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
           color: var(--fg); background: var(--bg); line-height: 1.6; }
    .container { max-width: 860px; margin: 0 auto; padding: 2rem 1.5rem; }
    a { color: var(--accent); text-decoration: none; }
    a:hover { text-decoration: underline; }
    h1 { font-size: 1.75rem; margin-bottom: 1rem; }
    h2 { font-size: 1.35rem; margin: 1.5rem 0 0.5rem; border-bottom: 1px solid var(--border); padding-bottom: 0.25rem; }
    h3 { font-size: 1.1rem; margin: 1.25rem 0 0.4rem; }
    p, ul, ol, table, blockquote, pre { margin-bottom: 1rem; }
    ul, ol { padding-left: 1.5rem; }
    blockquote { border-left: 3px solid var(--accent); padding: 0.5rem 1rem; color: var(--muted); background: #f8fafc; }
    table { border-collapse: collapse; width: 100%; }
    th, td { border: 1px solid var(--border); padding: 0.4rem 0.75rem; text-align: left; }
    th { background: #f1f5f9; }
    img { max-width: 100%; height: auto; border: 1px solid var(--border); border-radius: 4px; margin: 0.5rem 0; }
    code { background: #f1f5f9; padding: 0.15rem 0.35rem; border-radius: 3px; font-size: 0.9em; }
    pre code { display: block; padding: 1rem; overflow-x: auto; }
    .breadcrumb { font-size: 0.85rem; color: var(--muted); margin-bottom: 1rem; }
    .breadcrumb a { color: var(--muted); }
    .tag { display: inline-block; background: #e0f2fe; color: #0369a1; padding: 0.1rem 0.5rem;
           border-radius: 3px; font-size: 0.75rem; margin-right: 0.25rem; }
    .meta { color: var(--muted); font-size: 0.85rem; margin-bottom: 1.5rem; }
    .doc-list { list-style: none; padding: 0; }
    .doc-list li { padding: 0.4rem 0; border-bottom: 1px solid var(--border); }
    .doc-list li:last-child { border-bottom: none; }
    .section-group { margin-bottom: 2rem; }
    nav.site-nav { background: #f8fafc; border-bottom: 1px solid var(--border); padding: 0.75rem 1.5rem; }
    nav.site-nav a { margin-right: 1rem; font-weight: 500; }
    footer { margin-top: 3rem; padding-top: 1rem; border-top: 1px solid var(--border);
             color: var(--muted); font-size: 0.8rem; }
  </style>
</head>
<body>
  <nav class="site-nav">
    <a href="/help/">Zooza Help</a>
  </nav>
  <div class="container">
    {% block content %}{% endblock %}
    <footer>Zooza Help Center</footer>
  </div>
</body>
</html>
"""

INDEX_TEMPLATE = """\
{% extends "base.html" %}
{% block content %}
<h1>Zooza Help Center</h1>
{% for area, types in areas.items() %}
<div class="section-group">
  <h2>{{ area }}</h2>
  {% for doc_type, docs in types.items() %}
  <h3>{{ doc_type | capitalize }}</h3>
  <ul class="doc-list">
    {% for doc in docs %}
    <li>
      <a href="/help/{{ doc.area_slug }}/{{ doc.slug }}/">{{ doc.title }}</a>
      {% for tag in doc.tags %}<span class="tag">{{ tag }}</span>{% endfor %}
    </li>
    {% endfor %}
  </ul>
  {% endfor %}
</div>
{% endfor %}
{% endblock %}
"""

ARTICLE_TEMPLATE = """\
{% extends "base.html" %}
{% block content %}
<div class="breadcrumb">
  <a href="/help/">Help</a> &rsaquo; {{ product_area }}{% if sub_area %} &rsaquo; {{ sub_area }}{% endif %}
</div>
<div class="meta">
  <span>Type: {{ doc_type }}</span>
  {% for tag in tags %}<span class="tag">{{ tag }}</span>{% endfor %}
</div>
{{ body }}
{% endblock %}
"""


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return {}, text
    fm = yaml.safe_load(m.group(1)) or {}
    return fm, text[m.end():]


def slugify_area(area: str) -> str:
    return area.lower().replace(" ", "-")


def rewrite_md_links(html: str, all_slugs: dict[str, str]) -> str:
    """Rewrite internal .md links to their HTML equivalents.

    all_slugs maps relative md paths (e.g., 'dynamic-tags.md') and
    full paths to their URL path.
    """
    def replace_link(m):
        href = m.group(1)
        # Only rewrite relative .md links
        if href.startswith("http") or not href.endswith(".md"):
            return m.group(0)
        basename = os.path.basename(href).replace(".md", "")
        if basename in all_slugs:
            return f'href="{all_slugs[basename]}/"'
        return m.group(0)

    return re.sub(r'href="([^"]*)"', replace_link, html)


def rewrite_asset_paths(html: str) -> str:
    """Rewrite ../../assets/images/X paths to /help/assets/images/X."""
    html = re.sub(
        r'src="[./]*assets/',
        'src="/help/assets/',
        html,
    )
    return html


def build_web() -> dict:
    """Main entry point. Returns stats dict."""
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    md_converter = markdown.Markdown(extensions=["tables", "fenced_code"])

    # Collect all docs
    docs: list[dict] = []
    for md_path in sorted(CONTENT_DIR.rglob("*.md")):
        if "/_shared/" in str(md_path) or md_path.name.startswith("_"):
            continue

        text = md_path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        slug = fm.get("slug")
        if not slug:
            continue

        product_area = fm.get("product_area", "")
        area_slug = slugify_area(product_area)

        md_converter.reset()
        html_body = md_converter.convert(body)

        docs.append({
            "slug": slug,
            "title": fm.get("title", slug),
            "doc_type": fm.get("type", "guides"),
            "product_area": product_area,
            "sub_area": fm.get("sub_area", ""),
            "area_slug": area_slug,
            "tags": fm.get("tags", []),
            "status": fm.get("status", "published"),
            "html_body": html_body,
            "source_path": str(md_path.relative_to(ROOT_DIR)),
        })

    # Build slug->url map for link rewriting
    slug_to_url = {d["slug"]: f'/help/{d["area_slug"]}/{d["slug"]}' for d in docs}

    # Set up Jinja2
    env = Environment(loader=BaseLoader())
    env.loader = _DictLoader({
        "base.html": BASE_TEMPLATE,
        "index.html": INDEX_TEMPLATE,
        "article.html": ARTICLE_TEMPLATE,
    })

    # Build index grouped by product_area then type
    from collections import OrderedDict
    areas: dict[str, dict[str, list]] = OrderedDict()
    for doc in docs:
        if doc["status"] == "archived":
            continue
        area = doc["product_area"] or "Other"
        dtype = doc["doc_type"]
        areas.setdefault(area, OrderedDict()).setdefault(dtype, []).append(doc)

    # Render index
    index_html = env.get_template("index.html").render(title="Help Center", areas=areas)
    index_dir = OUTPUT_DIR / "help"
    index_dir.mkdir(parents=True, exist_ok=True)
    (index_dir / "index.html").write_text(index_html, encoding="utf-8")
    # Also write root redirect
    (OUTPUT_DIR / "index.html").write_text(
        '<meta http-equiv="refresh" content="0;url=/help/">\n',
        encoding="utf-8",
    )

    # Render articles
    article_tmpl = env.get_template("article.html")
    for doc in docs:
        if doc["status"] == "archived":
            continue
        html_body = rewrite_md_links(doc["html_body"], slug_to_url)
        html_body = rewrite_asset_paths(html_body)

        page_html = article_tmpl.render(
            title=doc["title"],
            product_area=doc["product_area"],
            sub_area=doc["sub_area"],
            doc_type=doc["doc_type"],
            tags=doc["tags"],
            body=html_body,
        )
        page_dir = OUTPUT_DIR / "help" / doc["area_slug"] / doc["slug"]
        page_dir.mkdir(parents=True, exist_ok=True)
        (page_dir / "index.html").write_text(page_html, encoding="utf-8")

    # Copy assets
    if ASSETS_DIR.exists():
        dest_assets = OUTPUT_DIR / "help" / "assets"
        if dest_assets.exists():
            shutil.rmtree(dest_assets)
        shutil.copytree(ASSETS_DIR, dest_assets)
        logger.info("Copied assets/ -> %s", dest_assets)

    stats = {
        "total_docs": len(docs),
        "published": sum(1 for d in docs if d["status"] != "archived"),
        "product_areas": len(areas),
    }
    logger.info("Web export: %d docs, %d published, %d areas", stats["total_docs"], stats["published"], stats["product_areas"])
    return stats


class _DictLoader(BaseLoader):
    """Simple Jinja2 loader from a dict of template strings."""

    def __init__(self, templates: dict[str, str]):
        self._templates = templates

    def get_source(self, environment, template):
        if template in self._templates:
            src = self._templates[template]
            return src, template, lambda: True
        raise Exception(f"Template not found: {template}")


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    stats = build_web()
    print(f"Web export complete: {stats['total_docs']} docs, {stats['published']} published")
    print(f"Output: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
