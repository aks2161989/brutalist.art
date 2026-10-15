#!/usr/bin/env python3
"""REMOTION VERSION LAW (Bear, 2026-10-10): the toolkit runs the LATEST Remotion, never a pinned-old one.

  python3 runtime/scripts/remotion_version.py            # report installed vs latest (warns, exit 0)
  python3 runtime/scripts/remotion_version.py --strict   # exit 3 when behind
  python3 runtime/scripts/remotion_version.py --upgrade  # npx remotion upgrade, then tell me what to re-render

Latest comes from `npm view remotion version` (cached 12 h in runtime/remotion/.latest-remotion; offline = skip, never block).
Called quietly by remotion_scenes.py before every render. Upgrading changes every composition, so re-render the
reels that matter and run their gates afterwards.
"""
import json, subprocess, sys, time
from pathlib import Path

REMOTION = Path(__file__).resolve().parent.parent / "remotion"
CACHE = REMOTION / ".latest-remotion"


def installed():
    try:
        return json.loads((REMOTION / "node_modules/remotion/package.json").read_text())["version"]
    except Exception:
        return None


def latest():
    try:
        if CACHE.exists() and time.time() - CACHE.stat().st_mtime < 12 * 3600:
            return CACHE.read_text().strip()
        v = subprocess.run(["npm", "view", "remotion", "version"], capture_output=True, text=True, timeout=20).stdout.strip()
        if v:
            CACHE.write_text(v)
        return v or None
    except Exception:
        return None


def key(v):
    return tuple(int(x) for x in v.split(".")[:3]) if v else ()


def main():
    have, want = installed(), latest()
    if "--upgrade" in sys.argv:
        rc = subprocess.run(["npx", "remotion", "upgrade"], cwd=REMOTION).returncode
        print("[remotion] upgraded. Now: re-render the reels you still ship (remotion_scenes.py <reel> --force), re-run their gates, "
              "and check React/transitions still bundle (a still of SkillDemo is the quick smoke test).")
        return rc
    if not have:
        print("[remotion] not installed — run `npm install` in runtime/remotion")
        return 3
    if not want:
        print(f"[remotion] {have} installed (latest unknown: offline)")
        return 0
    if key(have) < key(want):
        print(f"[remotion] BEHIND: {have} installed, {want} is latest. Bear's rule: use the latest Remotion. "
              f"Run `./art remotion-upgrade`, then re-render and re-gate.")
        return 3 if "--strict" in sys.argv else 0
    print(f"[remotion] {have} (latest)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
