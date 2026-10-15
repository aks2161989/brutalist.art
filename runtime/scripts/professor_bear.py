#!/usr/bin/env python3
"""professor_bear.py — pick a Professor Bear portrait by aspect ratio.

PROFESSOR BEAR LAW (Bear, 2026-10-07): whenever a beat needs an icon of a person, or Professor Bear
in particular, it does NOT draw a person token or pull a person icon. It uses one of the Professor
Bear portraits in `professor-bear/`, chosen at random among those with the right aspect ratio.

Ratios on disk: 1x1 (square, 3461²), 2x3 (portrait, 2822×4234), 16x9 (landscape, 4628×2604).
Cropping is fine (Bear, 2026-10-07): a circle, a rounded square, a tight head-and-shoulders, whatever the slot needs.
Downscaled JPG copies for Remotion live in runtime/remotion/public/professor-bear/ (same stems).

CLI
  ./art bear 16x9                 one random landscape portrait (absolute path)
  ./art bear 2x3 --seed B07       deterministic for a beat (same seed → same picture, so re-renders match)
  ./art bear 1x1 --n 3            three distinct squares
  ./art bear --list               every portrait by ratio
  ./art bear 16x9 --public        the Remotion public/ path (for staticFile) instead of the master PNG
  ./art bear 1x1 --crop circle    a circular cut (PNG with alpha) written to professor-bear/_crops/ — cropping is fine

Python
  from professor_bear import pick
  pick("2x3", seed="B07")  → "/…/professor-bear/professor-bear-2x3-17.png"
"""
import argparse, json, random, sys
from pathlib import Path

HOME = Path(__file__).resolve().parents[2]
DIR = HOME / "professor-bear"
PUBLIC = HOME / "runtime" / "remotion" / "public" / "professor-bear"
RATIOS = ("1x1", "2x3", "16x9")
ALIASES = {"square": "1x1", "portrait": "2x3", "3x2": "2x3", "landscape": "16x9", "wide": "16x9", "9x16": "2x3"}


def manifest(public=False):
    p = (PUBLIC if public else DIR) / "manifest.json"
    if not p.exists():
        sys.exit(f"professor_bear: no manifest at {p}")
    return json.loads(p.read_text())


def norm(ratio):
    r = ALIASES.get(ratio.lower(), ratio.lower())
    if r not in RATIOS:
        sys.exit(f"professor_bear: ratio {ratio!r} — use one of {RATIOS} (or square / portrait / landscape)")
    return r


def pick(ratio, seed=None, n=1, public=False):
    """One (or `n` distinct) portrait path(s) with the given ratio. Deterministic when `seed` is given."""
    r = norm(ratio)
    files = manifest(public)[r]
    rng = random.Random(str(seed)) if seed is not None else random.Random()
    chosen = rng.sample(files, k=min(n, len(files)))
    base = PUBLIC if public else DIR
    paths = [str(base / f) for f in chosen]
    return paths if n > 1 else paths[0]


def crop_circle(path):
    """A circular cut of a portrait (square centre crop, alpha outside the circle), cached in professor-bear/_crops/."""
    from PIL import Image, ImageDraw
    out_dir = DIR / "_crops"; out_dir.mkdir(exist_ok=True)
    out = out_dir / (Path(path).stem + "-circle.png")
    if not out.exists():
        im = Image.open(path).convert("RGBA"); w, h = im.size; s = min(w, h)
        im = im.crop(((w - s) // 2, max(0, (h - s) // 3), (w - s) // 2 + s, max(0, (h - s) // 3) + s))   # bias the crop upward: the face
        mask = Image.new("L", (s, s), 0); ImageDraw.Draw(mask).ellipse((0, 0, s - 1, s - 1), fill=255)
        im.putalpha(mask); im.save(out)
    return str(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("ratio", nargs="?", help="1x1 | 2x3 | 16x9 (or square / portrait / landscape)")
    ap.add_argument("--seed", help="deterministic choice, e.g. the beat id")
    ap.add_argument("--n", type=int, default=1, help="how many distinct portraits")
    ap.add_argument("--public", action="store_true", help="return the Remotion public/ JPG instead of the master PNG")
    ap.add_argument("--crop", choices=["circle"], help="return a circular cut (PNG with alpha) instead of the full frame")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    if a.list or not a.ratio:
        m = manifest(a.public)
        for r in RATIOS:
            print(f"{r}: {len(m[r])}")
            for f in m[r]:
                print("   ", f)
        return
    out = pick(a.ratio, a.seed, a.n, a.public)
    outs = out if isinstance(out, list) else [out]
    if a.crop == "circle":
        outs = [crop_circle(o) for o in outs]
    print("\n".join(outs))


if __name__ == "__main__":
    main()
