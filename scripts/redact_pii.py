#!/usr/bin/env python3
"""Redact PII from KB screenshots by covering with background color + replacement text."""

from PIL import Image, ImageDraw, ImageFont
import os
import shutil

BASE = os.path.join(os.path.dirname(__file__), "..", "assets", "images")
BACKUP_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "images_backup_pii")

# Colors sampled from screenshots
BG_WHITE = (255, 255, 255)
BG_CREAM = (244, 242, 233)
TEXT_DARK = (51, 51, 51)
TEXT_ORANGE = (227, 114, 34)


def get_font(size=14):
    for path in [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSText.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
    ]:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()


def sample_bg(img, x, y, radius=15):
    """Sample average background color around a point, avoiding dark (text) pixels."""
    pixels = []
    for dx in range(-radius, radius + 1, 3):
        for dy in range(-radius, radius + 1, 3):
            px, py = x + dx, y + dy
            if 0 <= px < img.width and 0 <= py < img.height:
                r, g, b = img.getpixel((px, py))[:3]
                if r + g + b > 500:  # light pixel = background
                    pixels.append((r, g, b))
    if not pixels:
        return BG_WHITE
    return tuple(sum(c) // len(pixels) for c in zip(*pixels))


def redact(filename, regions):
    src = os.path.join(BACKUP_DIR, filename)
    dst = os.path.join(BASE, filename)
    if not os.path.exists(src):
        print(f"  SKIP (no backup): {filename}")
        return

    img = Image.open(src).convert("RGB")
    draw = ImageDraw.Draw(img)

    for r in regions:
        box = r["box"]
        # Sample actual background color from corners of the box
        bg = r.get("bg") or sample_bg(img, box[0] + 5, box[1] + 5)
        draw.rectangle(box, fill=bg)

        if r.get("text"):
            font_size = r.get("font_size", 14)
            font = get_font(font_size)
            tc = r.get("text_color", TEXT_DARK)
            draw.text((box[0] + 4, box[1] + 3), r["text"], fill=tc, font=font)

    img.save(dst, quality=95)
    print(f"  DONE: {filename} ({len(regions)} regions)")


def main():
    print("Redacting PII from images...\n")

    # ── 1. linked-registrations-02.png (1024x775) ──
    # Two registration cards with: Otec Vysoký, dominika.chlapikova@gmail.com,
    # 0948506470, Julka Vysoká (DOB 15.2.2009), Maťko Vysoký (DOB 16.1.2007),
    # Centrum Rafael Ružinov address
    redact("linked-registrations-02.png", [
        # ── TOP CARD ──
        # Name "Otec Vysoký" (bold, dark)
        {"box": (375, 50, 670, 85), "bg": BG_CREAM,
         "text": "Demo Parent", "text_color": TEXT_DARK, "font_size": 18},
        # Email + phone line (orange)
        {"box": (375, 85, 670, 118), "bg": BG_CREAM,
         "text": "parent@example.com, 0900123456", "text_color": TEXT_ORANGE, "font_size": 14},
        # Child "Julka Vysoká"
        {"box": (680, 50, 820, 120), "bg": BG_CREAM,
         "text": "Demo\nChild", "text_color": TEXT_DARK, "font_size": 16},
        # DOB block "15. februára 2009 (14 rokov, 7 mesiacov)"
        {"box": (815, 50, 985, 215), "bg": BG_CREAM,
         "text": "1. January\n2010 (\n14 years,\n7 months)", "text_color": TEXT_DARK, "font_size": 14},
        # Venue "Centrum Rafael, Ružinov, Auguste Alfred, Prvý"
        {"box": (370, 260, 660, 310), "bg": BG_WHITE,
         "text": "Demo Venue, City Center, Main St\ntermín: 4. okt 2023", "text_color": TEXT_ORANGE, "font_size": 12},

        # ── BOTTOM CARD ──
        # Name "Otec Vysoký"
        {"box": (375, 440, 670, 480), "bg": BG_CREAM,
         "text": "Demo Parent", "text_color": TEXT_DARK, "font_size": 18},
        # Email + phone
        {"box": (375, 480, 670, 515), "bg": BG_CREAM,
         "text": "parent@example.com, 0900123456", "text_color": TEXT_ORANGE, "font_size": 14},
        # Child "Maťko Vysoký"
        {"box": (680, 440, 820, 515), "bg": BG_CREAM,
         "text": "Demo\nChild 2", "text_color": TEXT_DARK, "font_size": 16},
        # DOB "16. január 2007 (16 rokov, 8 mesiacov)"
        {"box": (815, 440, 985, 605), "bg": BG_CREAM,
         "text": "15. March\n2008 (\n16 years,\n8 months)", "text_color": TEXT_DARK, "font_size": 14},
        # Venue address (same)
        {"box": (370, 610, 660, 660), "bg": BG_WHITE,
         "text": "Demo Venue, City Center, Main St\ntermín: 4. okt 2023", "text_color": TEXT_ORANGE, "font_size": 12},
    ])

    # ── 2. linked-registrations-06.png (738x218) ──
    # "Katarina Krskova / Customer" label: y=63..129, x=110..296
    redact("linked-registrations-06.png", [
        {"box": (108, 58, 300, 133), "bg": BG_WHITE,
         "text": "Jane Smith\nCustomer", "text_color": TEXT_ORANGE, "font_size": 16},
    ])

    # ── 3. types-of-registrations-02.png (542x263) ──
    # Email+phone: y=40..77, x=20..223
    # Internal note with "Czoborová Janulka": y=121..182, x=80..285
    redact("types-of-registrations-02.png", [
        {"box": (16, 36, 330, 82), "bg": BG_CREAM,
         "text": "demo@example.com, 0900123456", "text_color": TEXT_ORANGE, "font_size": 13},
        {"box": (76, 117, 490, 190), "bg": BG_WHITE,
         "text": "General address, no classroom,\nDemo Client, First lesson/event date:\n27. mar 2023", "text_color": TEXT_ORANGE, "font_size": 11},
    ])

    # ── 4-8. Payment list images with staff emails in CREATED BY column ──
    # Coordinates verified by pixel scanning originals

    # 4. edit-payment-on-registration-08.png (1982x546)
    # Row 1: y=259..288, Row 2: y=350..379, Row 3: y=440..469
    # CREATED BY emails at x=1055..1660
    redact("edit-payment-on-registration-08.png", [
        {"box": (1054, 253, 1655, 294), "bg": BG_WHITE,
         "text": "admin@example.com", "text_color": TEXT_DARK, "font_size": 22},
        {"box": (1054, 344, 1655, 385), "bg": BG_WHITE,
         "text": "admin@example.com", "text_color": TEXT_DARK, "font_size": 22},
        {"box": (1054, 434, 1655, 475), "bg": BG_WHITE,
         "text": "admin2@example.com", "text_color": TEXT_DARK, "font_size": 22},
    ])

    # 5. edit-payment-on-registration-09.png (1956x453)
    # 2 rows: y=213..242, y=253..302 (CREATED BY x=1035..1650)
    redact("edit-payment-on-registration-09.png", [
        {"box": (1030, 207, 1655, 308), "bg": BG_WHITE,
         "text": "admin@example.com\n\nadmin@example.com", "text_color": TEXT_DARK, "font_size": 22},
        {"box": (1030, 335, 1635, 375), "bg": BG_WHITE,
         "text": "admin@example.com", "text_color": TEXT_DARK, "font_size": 22},
    ])

    # 6. payment-tile-on-registration-04.png (1484x353)
    # Row 1: y=198..219, Row 2: y=265..286 (CREATED BY x=950..1450)
    redact("payment-tile-on-registration-04.png", [
        {"box": (946, 192, 1450, 225), "bg": BG_WHITE,
         "text": "admin@example.com", "text_color": TEXT_DARK, "font_size": 18},
        {"box": (946, 259, 1265, 292), "bg": BG_WHITE,
         "text": "admin@example.com", "text_color": TEXT_DARK, "font_size": 18},
    ])

    # 7. payment-tile-on-registration-05.png (1464x324)
    # Row 1: y=145..242, Row 2: y=248..269 (CREATED BY x=950..1460)
    redact("payment-tile-on-registration-05.png", [
        {"box": (945, 139, 1465, 248), "bg": BG_WHITE,
         "text": "admin@example.com\n\n\nadmin@example.com", "text_color": TEXT_DARK, "font_size": 18},
        {"box": (1000, 242, 1255, 275), "bg": BG_WHITE,
         "text": "admin@example.com", "text_color": TEXT_DARK, "font_size": 18},
    ])

    # 8. payment-tile-on-registration-06.png (1473x561)
    # CREATED BY field: y=272..292, x=528..772
    redact("payment-tile-on-registration-06.png", [
        {"box": (523, 266, 780, 298), "bg": BG_WHITE,
         "text": "admin@example.com", "text_color": TEXT_DARK, "font_size": 18},
    ])

    print("\nAll done! Originals backed up to assets/images_backup_pii/")


if __name__ == "__main__":
    main()
