#!/usr/bin/env python3
"""claude_chat_shot.py - render recreated Claude-desktop-app stills (ClaudeChatShot).

Cowork was merged into regular Claude (announced 2026-09-16), so a "Cowork" task is an
ordinary desktop chat. This renders 3840x2160 PNGs of that chat from a spec file, for
BrowserCapture / app-capture beats. Every shot carries the 'Recreated screen' label.

usage: claude_chat_shot.py SPEC.json OUT_DIR [--only NAME ...]
SPEC.json = {"base": {...shared props...}, "shots": [{"name": "x", ...props...,
             "panelFile": "path relative to the spec"}]}
panelFile's text becomes panelBody (extension sets panelExt, title from the file stem).
Rule: shot content must come from a real run, the docs or the source chapter.
"""
import json, os, subprocess, sys, tempfile, glob
from pathlib import Path

HERE = Path(__file__).resolve().parent
REMOTION = HERE.parent / "remotion"

def chrome_flags():
    chrome = os.environ.get("ART_CHROME")
    if not chrome:
        hits = sorted(glob.glob(os.path.expanduser(
            "~/Library/Caches/ms-playwright/chromium_headless_shell-*/chrome-headless-shell-*/chrome-headless-shell")))
        chrome = hits[-1] if hits else None
    return [f"--browser-executable={chrome}"] if chrome else []

def main():
    a = sys.argv[1:]
    spec_path, out = Path(a[0]).resolve(), Path(a[1]).resolve()
    only = set(a[a.index("--only") + 1:]) if "--only" in a else None
    spec = json.loads(spec_path.read_text())
    out.mkdir(parents=True, exist_ok=True)
    for shot in spec["shots"]:
        name = shot["name"]
        if only and name not in only:
            continue
        props = {**spec.get("base", {}), **{k: v for k, v in shot.items() if k not in ("name", "panelFile")}}
        if "panelFile" in shot:
            f = (spec_path.parent / shot["panelFile"]).resolve()
            props["panelBody"] = f.read_text()
            props["panelExt"] = f.suffix.lstrip(".").upper()
            props.setdefault("panelTitle", f.stem)
        pj = Path(tempfile.mkdtemp()) / f"{name}.json"
        pj.write_text(json.dumps(props))
        png = out / f"{name}.png"
        cmd = ["npx", "remotion", "still", "ClaudeChatShot", str(png), f"--props={pj}", "--scale=2"] + chrome_flags()
        print("render", name, flush=True)
        subprocess.run(cmd, cwd=REMOTION, check=True)
        print("  ->", png)

if __name__ == "__main__":
    main()
