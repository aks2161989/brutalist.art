#!/usr/bin/env python3
"""empty_diagram_scan.py <film-folder | clip.mp4 ...> — flag frames that contain an EMPTY CONTAINER.

The Muse-draft failure this exists for: two big boxes (raw JSON / brief card) and a check mark, with
nothing inside either box. The diagram is "about" something but shows nothing.

Method (frame-level, no render needed beyond the clips already in <film>/manim/): sample the last frame
of every clip; find large regions that are (a) a light card fill that differs from the page, or (b) page-
coloured space fully enclosed by an outline, with area >= 5% of the frame and very few holes (no text,
no marks inside). Prints one line per flagged clip with the box position. A flag is a prompt for a human
look, not a verdict (a deliberate blank 'before' panel is fine if the narration says so); a CLEAN scan
does NOT prove the diagram is informative: read the rubric in SKILL.md.
"""
import subprocess, sys, tempfile
from pathlib import Path
import numpy as np, cv2

BG = np.array([0xF2, 0xF0, 0xE9])


def last_frame(mp4, out):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-sseof", "-0.25", "-i", str(mp4), "-frames:v", "1",
                    "-vf", "scale=960:-1", str(out)], check=True)
    return cv2.imread(str(out))[:, :, ::-1].astype(int)


def scan(img):
    h, w, _ = img.shape
    area = h * w
    diff = np.abs(img - BG).max(axis=2)
    flagged = []
    # (a) light card fills that differ slightly from the page
    # (b) page-coloured pockets enclosed by an outline
    near_bg = (diff <= 3).astype(np.uint8)
    ink = (img.sum(axis=2) < 3 * 140).astype(np.uint8)
    card = ((diff > 3) & (img.sum(axis=2) > 3 * 215)).astype(np.uint8)
    for name, mask in (("card", card), ("enclosed", near_bg)):
        n, lab, st, _ = cv2.connectedComponentsWithStats(mask, connectivity=4)
        for i in range(1, n):
            x, y, bw, bh, a = st[i]
            if a < 0.05 * area or bw < 0.15 * w or bh < 0.2 * h:
                continue
            if name == "enclosed" and (x <= 1 or y <= 1 or x + bw >= w - 1 or y + bh >= h - 1):
                continue  # touches the border: this is the page itself, not a pocket
            solidity = a / float(bw * bh)
            inner = ink[y + 6:y + bh - 6, x + 6:x + bw - 6]
            ink_frac = inner.mean() if inner.size else 0
            if solidity >= 0.9 and ink_frac < 0.002:
                flagged.append((name, round(x / w, 2), round(y / h, 2), round(bw / w, 2), round(bh / h, 2)))
    return flagged


def main(args):
    clips = []
    for a in args:
        p = Path(a)
        clips += sorted(q for q in (p / "manim").glob("*.mp4") if q.exists() and not q.name.endswith(".base.mp4")) if p.is_dir() else [p]
    bad = 0
    with tempfile.TemporaryDirectory() as td:
        for c in clips:
            try:
                fl = scan(last_frame(c, Path(td) / "f.png"))
            except Exception as e:  # noqa
                print(f"?? {c.name}: {e}")
                continue
            if fl:
                bad += 1
                print(f"EMPTY? {c.parent.parent.name}/{c.name}: " + "; ".join(f"{n} box at x={x} y={y} w={bw} h={bh}" for n, x, y, bw, bh in fl))
    print(f"-- {len(clips)} clips scanned, {bad} with an empty-container flag")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
