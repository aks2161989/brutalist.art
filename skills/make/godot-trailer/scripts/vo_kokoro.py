#!/usr/bin/env python3
"""vo_kokoro.py — voiceover lines for a trailer, spoken by Liam (Kokoro am_onyx, free, local).

    python3 vo_kokoro.py REEL                  # every line in trailer.json vo.lines that is missing or stale
    python3 vo_kokoro.py REEL --only V02 V05   # just these
    python3 vo_kokoro.py REEL --force          # regenerate all

Writes audio/vo/<id>.wav (mono, trimmed of leading/trailing silence so `at_s` is when speech is
heard, peak-normalised to -3 dBFS) and audio/vo/manifest.json (text hash, spoken form, wav hash,
measured duration). The gate refuses a manifest whose text no longer matches trailer.json.
Pronunciation goes through the Liam dictionary (runtime/pronunciation/liam.json): it rewrites the
text sent to the voice only, never the text in trailer.json. Durations are ground truth.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import wave

import numpy as np

HERE = Path(__file__).resolve().parent
ART = HERE.parents[3]
sys.path.insert(0, str(ART / 'runtime/scripts'))

TARGET_PEAK = 0.7          # -3 dBFS
TRIM_FLOOR = 0.01          # about -40 dBFS
PAD_S = 0.03


def sha(data):
    return hashlib.sha256(data).hexdigest()


def trim(samples, sr):
    loud = np.where(np.abs(samples) > TRIM_FLOOR)[0]
    if not len(loud):
        return samples
    a, b = max(loud[0] - int(PAD_S * sr), 0), min(loud[-1] + int(PAD_S * sr), len(samples))
    return samples[a:b]


def generate(root, only=None, force=False, speed=1.0):
    import generate_audio_kokoro as g                       # the toolkit's own Kokoro wrapper
    data = json.loads((root / 'trailer.json').read_text())
    vo = data.get('vo') or {}
    lines = vo.get('lines') or []
    if not lines:
        print('  no vo.lines in trailer.json')
        return {}
    voice = vo.get('voice', 'am_onyx')
    if vo.get('engine', 'kokoro') != 'kokoro':
        raise SystemExit('vo.engine must be kokoro: the trailer voice is free and local')
    out_dir = root / 'audio/vo'
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = out_dir / 'manifest.json'
    manifest = json.loads(manifest_path.read_text()) if manifest_path.is_file() else {}
    engine = None
    for line in lines:
        vid, text = line['id'], line['text'].strip()
        wav_path = out_dir / f'{vid}.wav'
        prior = manifest.get(vid)
        fresh = (prior and prior['text_sha256'] == sha(text.encode()) and prior['voice'] == voice
                 and prior.get('speed') == speed and wav_path.is_file()
                 and prior['wav_sha256'] == sha(wav_path.read_bytes()))
        if (only and vid not in only) or (fresh and not force):
            continue
        engine = engine or g.load_engine()
        spoken = g.normalize_for_tts(text, voice)
        samples, sr = engine.create(spoken, voice=voice, speed=speed, lang=g.lang_for(voice))
        samples = trim(np.asarray(samples, dtype=np.float32), sr)
        peak = float(np.abs(samples).max()) or 1.0
        samples = samples / peak * TARGET_PEAK
        with wave.open(str(wav_path), 'wb') as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
            w.writeframes((np.clip(samples, -1, 1) * 32767).astype('<i2').tobytes())
        manifest[vid] = {'text': text, 'text_sha256': sha(text.encode()), 'spoken_text': spoken, 'voice': voice,
                         'engine': 'kokoro', 'speed': speed, 'wav': f'audio/vo/{vid}.wav',
                         'wav_sha256': sha(wav_path.read_bytes()), 'duration_s': round(len(samples) / sr, 3)}
        print(f'  {vid}: {manifest[vid]["duration_s"]:.2f}s  "{text}"')
    manifest_path.write_text(json.dumps(manifest, indent=1))
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('reel', type=Path)
    parser.add_argument('--only', nargs='*')
    parser.add_argument('--force', action='store_true')
    parser.add_argument('--speed', type=float, default=1.0)
    args = parser.parse_args()
    generate(args.reel.resolve(), args.only, args.force, args.speed)
    return 0


if __name__ == '__main__':
    sys.exit(main())
