#!/usr/bin/env python3
"""Draw a wireframe of a screen we cannot photograph cleanly.

    python3 scripts/screenshots/wireframe.py client-attendance

Some screens cannot be published as screenshots. The parent zone ones we were
sent on 2026-11-08 are the case that prompted this: Slovak, with the stylesheet
not loaded, and carrying a real name and date of birth. Blurring the name fixes
none of that — the help is English and the picture has to look like what a
parent sees.

A wireframe sidesteps all three. It carries no personal data because there is
none to carry, it is written in English, and it cannot go stale in the way a
screenshot does, because it shows the shape of the screen rather than one
account's rendering of it.

Use it only where a real capture is impossible or unwise. A photograph of the
working product is better evidence when we can get one.

The client-attendance drawing has been retired: on 2026-11-13 Michal sent real
parent-zone screenshots, in English and properly styled, and they are simply
better — they carry details a drawing had to guess at, such as a booked make-up
appearing on both its old and its new date. The function is kept because the
reasoning above still holds for the next screen we cannot photograph, and
because it documents how one is made.
"""

import argparse
import os
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_DIR = os.path.join(ROOT, "assets", "images")
FONTS = "/System/Library/Fonts/Supplemental/"

INK = (32, 35, 27)
MUTED = (118, 123, 107)
LINE = (203, 205, 190)
FILL = (247, 247, 240)
ACCENT = (217, 88, 26)
BADGE = (228, 232, 218)
SCALE = 2          # drawn at 2x and downsampled, so the strokes are clean


def font(size, bold=False):
    name = "Arial Bold.ttf" if bold else "Arial.ttf"
    return ImageFont.truetype(FONTS + name, size * SCALE)


class Sheet:
    """A tiny layout helper: everything is a box with a y cursor."""

    def __init__(self, w, h):
        self.im = Image.new("RGB", (w * SCALE, h * SCALE), "white")
        self.d = ImageDraw.Draw(self.im)
        self.y = 0

    def box(self, x, y, w, h, fill=None, outline=LINE, r=8, width=1):
        self.d.rounded_rectangle([x * SCALE, y * SCALE, (x + w) * SCALE, (y + h) * SCALE],
                                 radius=r * SCALE, fill=fill, outline=outline,
                                 width=width * SCALE)

    def text(self, x, y, s, size=13, bold=False, fill=INK):
        self.d.text((x * SCALE, y * SCALE), s, font=font(size, bold), fill=fill)

    def rule(self, x, y, w, fill=LINE):
        self.d.line([x * SCALE, y * SCALE, (x + w) * SCALE, y * SCALE], fill=fill,
                    width=1 * SCALE)

    def save(self, path):
        self.im.resize((self.im.width // SCALE, self.im.height // SCALE),
                       Image.LANCZOS).save(path)


def client_attendance(path):
    """The parent's Attendance tab: a make-up offer, then the sessions."""
    s = Sheet(820, 640)

    s.text(28, 26, "Attendance", 20, bold=True)
    tabs = ["Overview", "Attendance", "Course progress", "Files", "Detail", "Payments"]
    x = 28
    for i, t in enumerate(tabs):
        w = 9 * len(t) + 22
        s.box(x, 58, w, 30, fill=BADGE if i == 1 else None, r=15)
        s.text(x + 11, 66, t, 12, bold=(i == 1), fill=INK if i == 1 else MUTED)
        x += w + 8

    # the make-up offer
    s.box(28, 108, 764, 86, fill=FILL)
    s.text(44, 122, "MAKE-UP SESSIONS TO CHOOSE FROM  (1)", 10, fill=MUTED)
    s.text(44, 144, "For the session on Mon 14 Dec", 14, bold=True)
    s.text(44, 165, "Valid until 28 Dec 2026", 11, fill=MUTED)
    s.box(596, 138, 180, 38, outline=ACCENT, r=19)
    s.text(620, 149, "Choose a make-up session", 12, fill=ACCENT)

    # which sessions to show
    x = 28
    for i, (t, n) in enumerate([("Upcoming", "8"), ("Past", "19"), ("Whole schedule", "27")]):
        s.box(x, 212, 248, 40, fill=BADGE if i == 0 else None)
        s.text(x + 18, 224, t, 13, bold=(i == 0))
        s.text(x + 18 + 9 * len(t) + 10, 225, n, 11, fill=MUTED)
        x += 256
    s.text(660, 266, "↑  Oldest first", 11, fill=MUTED)

    # the next session, expanded
    s.box(28, 292, 764, 196)
    s.text(44, 306, "NEXT SESSION", 10, fill=MUTED)
    s.text(44, 330, "Monday 09 Nov 2026", 16, bold=True)
    s.text(232, 333, "12:19  (60 minutes)", 13, fill=MUTED)
    s.box(648, 326, 128, 26, fill=BADGE, r=13)
    s.text(668, 332, "Not marked", 11, fill=MUTED)
    s.rule(44, 362, 732)
    for i, (k, v) in enumerate([("Venue", "Main hall, Riverside Centre"),
                                ("Instructor", "Chloe Evans")]):
        s.text(44, 376 + i * 24, k, 12, fill=MUTED)
        s.text(160, 376 + i * 24, v, 12)
    s.text(44, 426, "Information · Files: 2", 11, fill=MUTED)
    s.box(44, 448, 116, 32, outline=ACCENT, r=16)
    s.text(72, 457, "I can't come", 12, fill=ACCENT)
    s.text(176, 452, "Cancel by 14:00 the working day before. We tell the", 11, fill=MUTED)
    s.text(176, 468, "instructor, but the session is still charged.", 11, fill=MUTED)

    # the rest of the schedule
    y = 504
    for date, state in [("Mon 16 Nov", "Cancelled"), ("Mon 23 Nov", "Cancelled"),
                        ("Mon 30 Nov", "Not marked")]:
        s.rule(28, y, 764)
        s.text(44, y + 14, date, 13, bold=True)
        s.text(160, y + 15, "12:19  (60 minutes)", 12, fill=MUTED)
        s.box(624, y + 8, 124, 26, fill=BADGE if state == "Not marked" else None, r=13)
        s.text(642, y + 14, state, 11, fill=MUTED)
        s.text(768, y + 14, "›", 13, fill=MUTED)
        y += 44

    s.save(path)
    return path


DRAWINGS = {"client-attendance": (client_attendance, "client-zone-attendance-wireframe.png")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("name", choices=sorted(DRAWINGS), help="which wireframe to draw")
    ap.add_argument("--out", help="override the output path")
    args = ap.parse_args()
    fn, default = DRAWINGS[args.name]
    path = args.out or os.path.join(OUT_DIR, default)
    fn(path)
    print(f"drawn → {os.path.relpath(path, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
