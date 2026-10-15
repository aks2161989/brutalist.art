#!/usr/bin/env python3
"""beat_grid.py — find the beat grid of a music track so a trailer can be cut to it.

Decodes any audio with ffmpeg, estimates one constant tempo from spectral flux,
fits the beat phase, and writes beats / downbeats / onsets in seconds:

    python3 beat_grid.py music/track.wav --out music/beats.json
    python3 beat_grid.py music/track.wav --bpm 128 --out music/beats.json   # you know the tempo

numpy only; no librosa. LIMITS: one constant tempo. A rubato, tempo-changing or
beatless track gets a low `confidence` — mark it `music.rhythm: "free"` in
trailer.json instead of trusting the grid, or correct the grid by ear with
--bpm / --offset. Downbeats assume 4/4 and are the weakest part of the output.
"""
import argparse
import json
import math
from pathlib import Path
import subprocess
import sys

import numpy as np

SR, N_FFT, HOP = 22050, 1024, 256
FRAME_LAG_S = N_FFT / 2 / SR   # flux frame i is centred half a window after its first sample


def decode(path):
    proc = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(path), '-vn', '-ac', '1',
                           '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, timeout=300)
    if proc.returncode != 0 or not proc.stdout:
        raise SystemExit(f'ffmpeg could not decode {path}: {proc.stderr.decode()[-300:]}')
    return np.frombuffer(proc.stdout, dtype='<f4')


def flux(samples):
    """Onset envelope (all bands) and a low-band envelope for downbeat picking."""
    if len(samples) < N_FFT * 4:
        raise SystemExit('track too short to analyse')
    window = np.hanning(N_FFT).astype(np.float32)
    count = 1 + (len(samples) - N_FFT) // HOP
    index = np.arange(N_FFT)[None, :] + HOP * np.arange(count)[:, None]
    mags = np.abs(np.fft.rfft(samples[index] * window, axis=1))
    logm = np.log1p(100.0 * mags)
    diff = np.maximum(logm[1:] - logm[:-1], 0.0)
    low_bins = int(150 * N_FFT / SR)
    env = np.concatenate([[0.0], diff.sum(axis=1)])
    low = np.concatenate([[0.0], diff[:, : max(low_bins, 2)].sum(axis=1)])

    def clean(x):
        width = int(0.5 * SR / HOP)
        local = np.convolve(x, np.ones(width) / width, mode='same')
        x = np.maximum(x - local, 0.0)
        return x / x.max() if x.max() > 0 else x
    return clean(env), clean(low)


def tempo_candidate(env, fps, lo, hi):
    n = len(env)
    spec = np.fft.rfft(env - env.mean(), 2 * n)
    acf = np.fft.irfft(spec * np.conj(spec))[:n]
    best, best_bpm = -1.0, None
    for bpm in np.arange(lo, hi, 0.25):
        lag = 60.0 / bpm * fps
        i = int(lag)
        if i + 1 >= n:
            continue
        value = acf[i] * (1 - (lag - i)) + acf[i + 1] * (lag - i)
        # gentle preference for the common 90–150 BPM zone; octave errors are the usual failure
        value *= math.exp(-0.5 * (math.log2(bpm / 120.0) / 0.9) ** 2)
        if value > best:
            best, best_bpm = value, bpm
    return best_bpm, best / acf[0] if acf[0] else 0.0


def comb_score(env, times, bpm, offset):
    period = 60.0 / bpm
    beats = np.arange(offset, times[-1], period)
    return float(np.interp(beats, times, env).mean()) if len(beats) else 0.0


def fit(env, fps, bpm0, fixed_bpm):
    times = np.arange(len(env)) / fps + FRAME_LAG_S
    bpms = [bpm0] if fixed_bpm else np.arange(bpm0 - 3, bpm0 + 3.001, 0.05)
    best = (-1.0, bpm0, 0.0)
    for bpm in bpms:
        period = 60.0 / bpm
        for offset in np.arange(0, period, (HOP / SR) / 2):
            score = comb_score(env, times, bpm, offset)
            if score > best[0]:
                best = (score, float(bpm), float(offset))
    return best


def onsets(env, fps):
    picks, last = [], -1.0
    for i in range(1, len(env) - 1):
        if env[i] >= 0.3 and env[i] >= env[i - 1] and env[i] > env[i + 1]:
            t = i / fps + FRAME_LAG_S
            if t - last >= 0.06:
                picks.append((round(t, 3), round(float(env[i]), 3)))
                last = t
    return picks


def analyse(path, bpm_hint=None, offset_hint=None, lo=70.0, hi=180.0):
    samples = decode(path)
    env, low = flux(samples)
    fps = SR / HOP
    duration = len(samples) / SR
    ratio = 0.0
    bpm0 = bpm_hint
    if bpm0 is None:
        bpm0, ratio = tempo_candidate(env, fps, lo, hi)
    # phase follows the kick/bass first: a hi-hat on the off-beat is as periodic as the kick and would win otherwise
    score, bpm, offset = fit(0.25 * env + 0.75 * low, fps, bpm0, fixed_bpm=bpm_hint is not None)
    if offset_hint is not None:
        offset = offset_hint % (60.0 / bpm)
    period = 60.0 / bpm
    beats = [round(t, 3) for t in np.arange(offset, duration, period)]
    times = np.arange(len(low)) / fps + FRAME_LAG_S
    phase_scores = []
    for p in range(4):
        pts = np.array(beats[p::4])
        phase_scores.append(float(np.interp(pts, times, low).mean()) if len(pts) else 0.0)
    phase = int(np.argmax(phase_scores))
    return {
        'source': Path(path).name,
        'duration_s': round(duration, 3),
        'bpm': round(bpm, 2),
        'offset_s': round(offset, 3),
        'confidence': round(score / max(float(env.mean()), 1e-9), 2),
        'beats': beats,
        'downbeats': beats[phase::4],
        'onsets': [t for t, _ in onsets(env, fps)],
        'method': 'spectral-flux autocorrelation + comb fit; constant tempo; 4/4 downbeats from low-band flux',
        'note': 'confidence is the mean onset strength on the beats over the track mean; '
                'below ~2.5 treat the grid as a guess and listen before cutting to it',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('audio', type=Path)
    parser.add_argument('--out', type=Path, help='write JSON here (default: print)')
    parser.add_argument('--bpm', type=float, help='known tempo: fit the phase only')
    parser.add_argument('--offset', type=float, help='force the first beat time (seconds)')
    parser.add_argument('--min-bpm', type=float, default=70.0)
    parser.add_argument('--max-bpm', type=float, default=180.0)
    args = parser.parse_args()
    result = analyse(args.audio, args.bpm, args.offset, args.min_bpm, args.max_bpm)
    text = json.dumps(result, indent=1)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text)
        print(f'{result["bpm"]} BPM, first beat {result["offset_s"]} s, '
              f'{len(result["beats"])} beats, confidence {result["confidence"]} → {args.out}')
    else:
        print(text)
    return 0


if __name__ == '__main__':
    sys.exit(main())
