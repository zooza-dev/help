#!/usr/bin/env python3
"""Old-vs-new contact sheet for staged screenshots.

    python3 scripts/screenshots/contact_sheet.py --manifest build/app-map/manifest-settings.yml

For every shot in the manifest that has a staged capture, put the current
image from assets/images/ on the left and the staged one on the right, with
the manifest note underneath, six pairs per sheet. Sheets go to
build/screenshots/review/sheet-NN.png. The point is to decide quickly: does
the new picture show what the article is talking about, or did the index
guess the wrong screen?
"""

import argparse
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
STAGE = os.path.join(ROOT, "build", "screenshots")
IMAGES = os.path.join(ROOT, "assets", "images")
REVIEW = os.path.join(STAGE, "review")
CELL_W, CELL_H, PAD, TXT = 640, 400, 16, 48
PER_SHEET = 6


def fit(img, w, h):
    from PIL import Image
    img = img.convert("RGB")
    img.thumbnail((w, h), Image.LANCZOS)
    canvas = Image.new("RGB", (w, h), (245, 245, 240))
    canvas.paste(img, (0, 0))
    return canvas


def main():
    import yaml
    from PIL import Image, ImageDraw
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    args = ap.parse_args()
    shots = yaml.safe_load(open(args.manifest, encoding="utf-8"))["shots"]
    os.makedirs(REVIEW, exist_ok=True)
    pairs = []
    for s in shots:
        staged = os.path.join(STAGE, s["image"].replace("/", "__"))
        if not os.path.exists(staged):
            continue
        old = os.path.join(IMAGES, s["image"])
        pairs.append((s, old if os.path.exists(old) else None, staged))

    sheet_w = 2 * CELL_W + 3 * PAD
    n = 0
    for start in range(0, len(pairs), PER_SHEET):
        chunk = pairs[start:start + PER_SHEET]
        sheet = Image.new("RGB", (sheet_w, len(chunk) * (CELL_H + TXT + PAD) + PAD), "white")
        d = ImageDraw.Draw(sheet)
        y = PAD
        for i, (s, old, new) in enumerate(chunk):
            if old:
                sheet.paste(fit(Image.open(old), CELL_W, CELL_H), (PAD, y))
            else:
                d.rectangle([PAD, y, PAD + CELL_W, y + CELL_H], outline="red")
                d.text((PAD + 10, y + 10), "no current image", fill="red")
            sheet.paste(fit(Image.open(new), CELL_W, CELL_H), (2 * PAD + CELL_W, y))
            label = f"#{start + i + 1}  {s['image']}  ←old | new→  route {s['route']}" + (f"  click {s['click']!r}" if s.get("click") else "") + (f"  card {s['card']!r}" if s.get("card") else "")
            d.text((PAD, y + CELL_H + 6), label[:150], fill="black")
            d.text((PAD, y + CELL_H + 24), s.get("note", "")[:150], fill=(90, 90, 90))
            y += CELL_H + TXT + PAD
        n += 1
        sheet.save(os.path.join(REVIEW, f"sheet-{n:02d}.png"))
    print(f"{len(pairs)} pairs on {n} sheets -> {REVIEW}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
