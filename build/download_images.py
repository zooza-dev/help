#!/usr/bin/env python3
"""Download remote images and update Markdown references."""

import re
import os
import glob
import hashlib
import urllib.request
import json
import sys

CONTENT_DIR = "content"
ASSETS_DIR = "assets/images"
MAPPING_FILE = "build/image_mapping.json"

# Already-converted slugs (skip these files)
SKIP_SLUGS = {
    'whatsapp-integration', 'company-logo-email', 'automatic-payment-reminders',
    'edit-event-notification-template', 'dynamic-tags', 'automatic-event-notification',
    'message-templates', 'send-email-after-event', 'sending-email-sms',
    'whatsapp-troubleshooting', 'whatsapp-faq'
}


def url_to_filename(url, slug, index):
    """Generate a descriptive kebab-case filename from URL context."""
    # Use slug + index for simplicity and uniqueness
    ext = ".png"  # Default; could detect from content-type
    if ".jpg" in url or ".jpeg" in url:
        ext = ".jpg"
    elif ".gif" in url:
        ext = ".gif"
    elif ".svg" in url:
        ext = ".svg"
    elif ".webp" in url:
        ext = ".webp"
    return f"{slug}-{index:02d}{ext}"


def download_image(url, dest_path):
    """Download an image URL to local path."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
            if len(data) < 100:
                return False
            with open(dest_path, "wb") as f:
                f.write(data)
            return True
    except Exception as e:
        print(f"  FAIL: {e}", file=sys.stderr)
        return False


def main():
    os.makedirs(ASSETS_DIR, exist_ok=True)

    # Collect all URLs from new content files
    url_mapping = {}  # url -> local_filename
    file_urls = {}    # md_path -> [(url, local_filename)]

    for md_path in sorted(glob.glob(f"{CONTENT_DIR}/**/*.md", recursive=True)):
        if "/_shared/" in md_path:
            continue

        with open(md_path) as f:
            content = f.read()

        slug_match = re.search(r'^slug:\s*"([^"]+)"', content, re.MULTILINE)
        if not slug_match:
            continue
        slug = slug_match.group(1)

        if slug in SKIP_SLUGS:
            continue

        # Find all remote image URLs
        matches = list(re.finditer(r'!\[[^\]]*\]\((https?://[^)]+)\)', content))
        if not matches:
            continue

        file_urls[md_path] = []
        for i, m in enumerate(matches, 1):
            url = m.group(1)
            if url not in url_mapping:
                fname = url_to_filename(url, slug, i)
                # Ensure uniqueness
                while os.path.exists(os.path.join(ASSETS_DIR, fname)):
                    base, ext = os.path.splitext(fname)
                    fname = f"{base}-x{ext}"
                url_mapping[url] = fname
            file_urls[md_path].append((url, url_mapping[url]))

    print(f"Found {len(url_mapping)} unique images across {len(file_urls)} files")

    # Download all images
    ok = 0
    fail = 0
    for i, (url, fname) in enumerate(url_mapping.items(), 1):
        dest = os.path.join(ASSETS_DIR, fname)
        if os.path.exists(dest):
            print(f"  [{i}/{len(url_mapping)}] SKIP (exists): {fname}")
            ok += 1
            continue
        print(f"  [{i}/{len(url_mapping)}] Downloading: {fname}")
        if download_image(url, dest):
            ok += 1
        else:
            fail += 1

    print(f"\nDownloaded: {ok} OK, {fail} failed")

    # Save mapping for reference
    with open(MAPPING_FILE, "w") as f:
        json.dump(url_mapping, f, indent=2)

    # Update Markdown files
    updated = 0
    for md_path, urls in file_urls.items():
        with open(md_path) as f:
            content = f.read()

        new_content = content
        for url, fname in urls:
            # Calculate relative path from content file to assets
            # content/guides/foo.md -> ../../assets/images/
            # content/setup/foo.md -> ../../assets/images/
            # content/faq/foo.md -> ../../assets/images/
            rel_path = f"../../assets/images/{fname}"
            new_content = new_content.replace(url, rel_path)

        if new_content != content:
            with open(md_path, "w") as f:
                f.write(new_content)
            updated += 1

    print(f"Updated {updated} Markdown files with local image paths")


if __name__ == "__main__":
    main()
