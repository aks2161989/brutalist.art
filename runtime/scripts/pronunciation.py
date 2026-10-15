#!/usr/bin/env python3
"""Pronunciation dictionary for a voice persona.

apply(text, voice) rewrites words for the voice only; narration_text and captions are untouched.
  python3 runtime/scripts/pronunciation.py --check            verify every example against Kokoro's phonemizer
  python3 runtime/scripts/pronunciation.py --say "built live"  show the rewritten text and its phonemes
"""
import argparse
import json
import re
import sys
from pathlib import Path

DIR = Path(__file__).resolve().parents[1] / "pronunciation"
_CACHE = {}


def _load(voice):
    if voice in _CACHE:
        return _CACHE[voice]
    entries = []
    for f in sorted(DIR.glob("*.json")):
        d = json.loads(f.read_text())
        if d.get("voice") == voice:
            for e in d["entries"]:
                e["_re"] = [re.compile(p, re.IGNORECASE if e.get("ignorecase") else 0) for p in e["patterns"]]
                entries.append(e)
    _CACHE[voice] = entries
    return entries


def apply(text, voice):
    for e in _load(voice):
        for rx in e["_re"]:
            def sub(m, e=e):
                s, t = m.start("w") - m.start(), m.end("w") - m.start()
                return m.group(0)[:s] + e["say"] + m.group(0)[t:]
            text = rx.sub(sub, text)
    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--voice", default="am_onyx")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--say")
    a = ap.parse_args()
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import generate_audio_kokoro as g
    tok = g.load_engine().tokenizer
    if a.say:
        out = apply(a.say, a.voice)
        print(out, "->", tok.phonemize(out, "en-us"))
        return 0
    bad = 0
    for e in _load(a.voice):
        for ex in e.get("examples", []):
            out = apply(ex["text"], a.voice)
            ph = tok.phonemize(out, "en-us")
            ok = ex["expect"] in ph
            bad += not ok
            print(f"[{'ok ' if ok else 'BAD'}] {e['id']}: {ex['text']!r} -> {out!r} -> {ph}")
    print("all examples pass" if not bad else f"{bad} example(s) FAIL")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
