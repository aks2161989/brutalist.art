#!/usr/bin/env python3
"""seis_speaker_series.py — the seis-speaker-series skill's engine (skills/make/seis-speaker-series).

  python3 seis_speaker_series.py plan.json --out speaker-series-1.mp4 [--dry]         # 1080p review cut (.mp4)
  python3 seis_speaker_series.py plan.json --out speaker-series-1.mov --master        # YouTube master: 3840x2160 H.264 .mov,
                                                                                      # 2-pass VBR (--bitrate, default 40M), 48 kHz
plan.json (one event recording → one film):
  {"series": 1, "speaker": "<Speaker Name>", "source": "<Teams recording>.mp4",
   "segments": [{"label": "talk", "in": "0:10.2", "out": "1:05:52"},          # the host's intro → end of talk, uncut
                {"label": "q1",   "in": "1:17:21", "out": "1:19:50"}, ...],    # the Q&A, cut down to chosen exchanges
   "bleep": [{"phrase": "~what the fuck", "word": "fuck"}, [3712.4, 3712.9]],   # optional — muted in the source clock
   "open": {...card override...} | false, "close": {...card override...} | {"image": "lockup.png", ...} | false,
   "logo_seconds": 4.5, "loudnorm": true,
   "music": {"file": "bed.mp3", "gain": 1.0, "under": 0.08}}                   # optional bed: full under the bookends, low under the talk
Timeline: SEIS logo (opacity through blur) → "Speaker Series N / <speaker>" card → segments in order (0.4 s dip at
every join, so a cut reads as a cut) → "Thank you" card → the same SEIS logo. Bookends render through Remotion
`SeisFilm` (the alumni film's logo + card, no new component); the talk is cut and conformed by ffmpeg (an 80-minute
Remotion render buys nothing). in/out: seconds, "m:ss", "h:mm:ss" (the RECORDING's clock — the Teams .docx clock is
within ~2 s of it), or "~a phrase" resolved against <source>.transcript.json (seis_extract.py transcribe). Never publishes.
NEU videography guideline (brand.northeastern.edu/design-and-experiences/design/videography): "Include no opening title
slide; simply start the video" → "open": false; end on the approved Wordmark + Motto lockup on white → "close":
{"image": "<approved PNG>", "seconds": 5, "bg": "white", "height": 0.45} (a still slate; the image is never composed here).
--master encodes the source ONCE (cut, mutes, upscale, 2-pass) — never an upscale of the review cut.
"""
import argparse, json, math, re, shutil, subprocess, sys
from difflib import SequenceMatcher
from pathlib import Path
HERE = Path(__file__).resolve().parent; TOOLKIT = HERE.parent.parent
REM = TOOLKIT / 'runtime' / 'remotion'; PUB = REM / 'public' / 'seis-speaker'; FPS = 30; DIP = 0.4
sys.path.insert(0, str(HERE))
from seis_extract import tsec, sh

# one conform for every part so the concat demuxer can join them with -c copy
VENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-video_track_timescale', '15360']
AENC = ['-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2']
def conform(w, h): return (f'scale={w}:{h}:force_original_aspect_ratio=decrease:flags=lanczos,pad={w}:{h}:(ow-iw)/2:(oh-ih)/2:color=black,'
                           f'fps={FPS},format=yuv420p,setsar=1')
HD, UHD = (1920, 1080), (3840, 2160)

def dur(p): return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)], capture_output=True, text=True).stdout.strip())
def hms(s): return f'{int(s // 3600)}:{int(s % 3600 // 60):02d}:{s % 60:04.1f}'

def card(c, seconds):
    return {'kind': 'card', 'frames': int(math.ceil(c.get('seconds', seconds) * FPS)), 'src': '', 'audio': '', 'duck': False,
            'eyebrow': c.get('eyebrow', ''), 'lines': c.get('lines', []), 'emphasis': c.get('emphasis', -1), 'dark': c.get('dark', True)}
def logo(seconds, light=False): return {'kind': 'logo', 'frames': int(math.ceil(seconds * FPS)), 'src': '', 'audio': '', 'duck': False, 'eyebrow': '', 'lines': [],
                                       'emphasis': -1, 'dark': True, 'light': light}

def bleeps(spec, transcript):
    """Each bleep is [t0, t1] in the source clock, or {"phrase": "~context", "word": "fuck"}: the phrase is found in
    whisper's words and every word inside it containing `word` is muted (padded 60 ms each side)."""
    out = []
    words = [w for seg in (transcript or {}).get('segments', []) for w in seg['words']]
    norm = lambda w: re.sub(r"[^a-z0-9']", '', w.lower())
    for b in spec:
        if isinstance(b, list): out.append((float(b[0]), float(b[1]))); continue
        if not words: sys.exit("bleep by phrase needs <source>.transcript.json — run seis_extract.py transcribe first")
        target = re.findall(r"[a-z0-9']+", b['phrase'].lstrip('~').lower()); n = len(target); best, bi = 0.0, 0
        for i in range(max(1, len(words) - n + 1)):
            r = SequenceMatcher(None, target, [norm(w['w']) for w in words[i:i + n]]).ratio()
            if r > best: best, bi = r, i
        if best < 0.6: sys.exit(f"bleep phrase not found: {b['phrase']!r} (best {best:.2f})")
        hit = [w for w in words[bi:bi + n] if b['word'].lower() in norm(w['w'])]
        if not hit: sys.exit(f"bleep word {b['word']!r} not inside {b['phrase']!r} — whisper heard: {' '.join(w['w'] for w in words[bi:bi + n])}")
        out += [(w['s'] - 0.06, w['e'] + 0.06) for w in hit]
    return out

def render_bookend(items, raw, final, size, venc):
    """SeisFilm renders silent at 1080p (--scale=2 for UHD); give it a silent stereo track and the shared conform."""
    pj = raw.with_suffix('.props.json'); pj.write_text(json.dumps({'items': items, 'music': '', 'musicGain': 0, 'musicDuck': 0}, ensure_ascii=False))
    r = subprocess.run(['npx', 'remotion', 'render', 'src/index.ts', 'SeisFilm', str(raw.resolve()), f'--props={pj.resolve()}', '--codec=h264', '--crf=16',
                        f'--scale={size[0] / HD[0]:g}', '--concurrency=2', '--timeout=300000', '--log=error'], cwd=str(REM), capture_output=True, text=True)
    if r.returncode != 0: sys.exit(r.stderr[-1500:])
    sh(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(raw), '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-map', '0:v', '-map', '1:a', '-shortest',
        '-vf', conform(*size), *venc, *AENC, str(final)])

def still_slate(c, base, final, size, venc):
    """An approved lockup image, centred on a flat ground (white by default), faded up from black. Silent."""
    img = Path(c['image']); img = img if img.is_absolute() else base / img
    if not img.exists(): sys.exit(f'close image not found: {img}')
    w, h = size; s = float(c.get('seconds', 5)); lh = int(h * float(c.get('height', 0.45))) // 2 * 2
    vf = (f"[1:v]scale=-2:{lh}:flags=lanczos[l];[0:v][l]overlay=(W-w)/2:(H-h)/2:format=auto,format=yuv420p,"
          f"fade=t=in:st=0:d={DIP},fade=t=out:st={s - DIP:.3f}:d={DIP}[v]")
    sh(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'lavfi', '-i', f"color=c={c.get('bg', 'white')}:s={w}x{h}:r={FPS}:d={s}", '-loop', '1', '-t', str(s), '-i', str(img),
        '-f', 'lavfi', '-t', str(s), '-i', 'anullsrc=r=48000:cl=stereo', '-filter_complex', vf, '-map', '[v]', '-map', '2:a', *venc, *AENC, str(final)])

def bookend(c, items, work, name, base, size, venc):
    p = work / f'{name}.mp4'
    print(f'  rendering {name}')
    if 'image' in c: still_slate(c, base, p, size, venc)
    else: render_bookend(items, work / f'{name}.raw.mp4', p, size, venc)
    return p

def seg_filters(s, mutes, loudnorm, size):
    d = s['out'] - s['in']; t0, t1 = s['in'], s['out']
    vf = f'{conform(*size)},fade=t=in:st=0:d={DIP},fade=t=out:st={d - DIP:.3f}:d={DIP}'
    af = [f"volume=0:enable='between(t,{a - t0:.3f},{b - t0:.3f})'" for a, b in mutes if b > t0 and a < t1]
    if loudnorm: af.append('loudnorm=I=-16:TP=-1.5:LRA=11')
    af += ['aresample=48000', f'afade=t=in:st=0:d={DIP}', f'afade=t=out:st={d - DIP:.3f}:d={DIP}']
    return vf, ','.join(af)

def cut_segment(src, s, mutes, loudnorm, out):
    vf, af = seg_filters(s, mutes, loudnorm, HD)
    sh(['ffmpeg', '-loglevel', 'error', '-y', '-ss', f"{s['in']:.3f}", '-t', f"{s['out'] - s['in']:.3f}", '-i', str(src), '-vf', vf, '-af', af, *VENC, *AENC, str(out)])

def master(src, segs, mutes, loudnorm, opens, closes, out, bitrate):
    """One encode from the source: bookend intermediates + every segment → concat → 2-pass VBR H.264 .mov at UHD."""
    ins, chains, labels = [], [], []
    for p in opens: ins += ['-i', str(p)]
    for s in segs: ins += ['-ss', f"{s['in']:.3f}", '-t', f"{s['out'] - s['in']:.3f}", '-i', str(src)]
    for p in closes: ins += ['-i', str(p)]
    k = 0
    for _ in opens: chains.append(f'[{k}:v]{conform(*UHD)}[v{k}];[{k}:a]aresample=48000[a{k}]'); labels.append(f'[v{k}][a{k}]'); k += 1
    for s in segs:
        vf, af = seg_filters(s, mutes, loudnorm, UHD)
        chains.append(f'[{k}:v]{vf}[v{k}];[{k}:a]{af}[a{k}]'); labels.append(f'[v{k}][a{k}]'); k += 1
    for _ in closes: chains.append(f'[{k}:v]{conform(*UHD)}[v{k}];[{k}:a]aresample=48000[a{k}]'); labels.append(f'[v{k}][a{k}]'); k += 1
    fc = ';'.join(chains) + f";{''.join(labels)}concat=n={k}:v=1:a=1[v][a]"
    rate = int(bitrate.rstrip('Mm')) if bitrate[-1] in 'Mm' else None
    venc = ['-c:v', 'libx264', '-preset', 'fast', '-profile:v', 'high', '-level:v', '5.1', '-pix_fmt', 'yuv420p', '-r', str(FPS),
            '-b:v', bitrate, *(['-maxrate', f'{int(rate * 1.5)}M', '-bufsize', f'{rate * 2}M'] if rate else []), '-g', str(FPS // 2 * 2), '-bf', '2',
            '-passlogfile', str(out.with_suffix('.2pass'))]
    common = ['ffmpeg', '-loglevel', 'error', '-stats', '-y', *ins, '-filter_complex', fc, '-map', '[v]', '-map', '[a]']
    print(f'  pass 1/2'); sh([*common, *venc, '-pass', '1', '-c:a', 'aac', '-b:a', '320k', '-f', 'mov', '/dev/null'])
    print(f'  pass 2/2'); sh([*common, *venc, '-pass', '2', '-c:a', 'aac', '-b:a', '320k', '-ar', '48000', '-ac', '2', '-movflags', '+faststart', str(out)])
    for f in out.parent.glob(out.with_suffix('.2pass').name + '*'): f.unlink()

def add_music(film, m, base, open_s, close_s, out):
    """Mix a music bed under a finished film (video stream copied): full level under the opening bookend, eased down to
    `under` ~1 s before the recording starts, held low to the end, lifted back under the closing bookend, faded out."""
    src = Path(m['file']); src = src if src.is_absolute() else base / src
    if not src.exists(): sys.exit(f'music not found: {src}')
    d = dur(film); g1, g2, r = float(m.get('gain', 1.0)), float(m.get('under', 0.08)), 1.0   # under 0 = silent under the talk
    lufs = float(re.findall(r'I:\s+(-?[\d.]+) LUFS', subprocess.run(['ffmpeg', '-hide_banner', '-i', str(src), '-af', 'ebur128=framelog=quiet',
                 '-f', 'null', '-'], capture_output=True, text=True).stderr)[-1])
    norm = 10 ** ((-16 - lufs) / 20)   # one static gain to -16 LUFS (the talk's loudnorm target); a looped 2-hour loudnorm is slow
    o = max(0.0, open_s - r); e = d - close_s
    g = (f"if(lt(t,{o}),{g1}*min(1,t/1.5),if(lt(t,{o + r}),{g1}+({g2}-{g1})*(t-{o})/{r},if(lt(t,{e}),{g2},"
         f"if(lt(t,{e + r}),{g2}+({g1}-{g2})*(t-{e})/{r},{g1}))))")
    fc = (f"[1:a]aresample=48000,volume={norm:.4f},volume='{g}':eval=frame,alimiter=limit=0.9,afade=t=out:st={d - 2:.3f}:d=2[m];"
          f"[0:a][m]amix=inputs=2:duration=first:normalize=0[a]")
    sh(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(film), '-stream_loop', '-1', '-i', str(src), '-filter_complex', fc,
        '-map', '0:v', '-map', '[a]', '-c:v', 'copy', *AENC, '-movflags', '+faststart', str(out)])

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('plan'); ap.add_argument('--out', required=True)
    ap.add_argument('--dry', action='store_true', help='resolve and print the timeline, render nothing')
    ap.add_argument('--master', action='store_true', help='YouTube master: 3840x2160 H.264 .mov, 2-pass VBR, 48 kHz')
    ap.add_argument('--bitrate', default='40M', help='--master video bitrate (YouTube 4K SDR 30 fps: 35–45M)'); a = ap.parse_args()
    plan = json.loads(Path(a.plan).read_text()); base = Path(a.plan).parent
    src = Path(plan['source']); src = src if src.is_absolute() else base / src
    if not src.exists(): sys.exit(f'source not found: {src}')
    tj = src.with_suffix('.transcript.json'); transcript = json.loads(tj.read_text()) if tj.exists() else None
    speaker, n = plan['speaker'], plan.get('series', 1); ls = float(plan.get('logo_seconds', 4.5))
    open_c = plan.get('open') or {}; close_c = plan.get('close') or {}   # an override merges over the default card text
    if open_c is not False: open_c = {'eyebrow': 'SEIS · Northeastern', 'lines': [f'Speaker Series {n}', speaker], 'emphasis': 1, **open_c}
    if close_c is not False: close_c = {'eyebrow': f'SEIS Speaker Series {n}', 'lines': ['Thank you,', f'{speaker}.'], 'emphasis': 1, **close_c}

    segs, src_d = [], dur(src)
    for s in plan['segments']:
        t0 = tsec(s['in'], transcript, 'in'); t1 = min(src_d, tsec(s['out'], transcript, 'out'))
        if t1 - t0 < 2 * DIP: sys.exit(f"segment {s.get('label')}: out ({hms(t1)}) not after in ({hms(t0)})")
        if segs and t0 < segs[-1]['out']: print(f"  ! {s.get('label')} starts before the previous segment ends — overlap repeats footage")
        segs.append({'label': s.get('label', f'seg{len(segs) + 1}'), 'in': t0, 'out': t1})
    mutes = bleeps(plan.get('bleep', []), transcript)
    def book_s(c, with_logo): return 0 if c is False else with_logo if c.get('logo_only') else float(c.get('seconds', 5 if 'image' in c else 4)) + (0 if 'image' in c else with_logo)
    body = sum(s['out'] - s['in'] for s in segs); book = book_s(open_c, ls) + book_s(close_c, ls)
    for s in segs: print(f"  {s['label']:<10} {hms(s['in'])} → {hms(s['out'])}  ({(s['out'] - s['in']) / 60:5.1f} min)")
    print(f"{len(segs)} segments · {len(mutes)} bleeps · open {'none' if open_c is False else 'card'} · close "
          f"{'none' if close_c is False else ('image' if 'image' in close_c else 'card')} · {(body + book) / 60:.1f} min total (source {src_d / 60:.1f} min)")
    out = Path(a.out).resolve(); out.parent.mkdir(parents=True, exist_ok=True)
    if a.master and out.suffix.lower() != '.mov': sys.exit('--master writes an H.264 .mov — give --out a .mov path')
    out.with_suffix('.timeline.json').write_text(json.dumps({'source': str(src), 'segments': segs, 'bleeps': mutes, 'open': open_c, 'close': close_c}, indent=1, ensure_ascii=False))
    if a.dry: return

    work = out.parent / f'.{out.stem}-parts'; work.mkdir(parents=True, exist_ok=True); PUB.mkdir(parents=True, exist_ok=True)
    size = UHD if a.master else HD; benc = VENC if not a.master else [*VENC[:5], '10', *VENC[6:]]   # UHD bookends: near-lossless intermediates
    def lg(c): return [logo(ls, c.get('light', False))]
    opens = [] if open_c is False else [bookend(open_c, lg(open_c) + ([] if open_c.get('logo_only') else [card(open_c, 4)]), work, '00-open', base, size, benc)]
    closes = [] if close_c is False else [bookend(close_c, ([] if close_c.get('logo_only') else [card(close_c, 4)]) + lg(close_c), work, '99-close', base, size, benc)]
    if a.master:
        print(f'  mastering {(body + book) / 60:.1f} min at {UHD[0]}x{UHD[1]}, {a.bitrate} 2-pass VBR')
        master(src, segs, mutes, plan.get('loudnorm', True), opens, closes, out, a.bitrate)
    else:
        parts = list(opens)
        for i, s in enumerate(segs, 1):
            p = work / f"{i:02d}-{re.sub(r'[^a-z0-9]+', '-', s['label'].lower())}.mp4"; parts.append(p)
            print(f"  cutting {s['label']} ({(s['out'] - s['in']) / 60:.1f} min)"); cut_segment(src, s, mutes, plan.get('loudnorm', True), p)
        parts += closes
        lst = work / 'concat.txt'; lst.write_text(''.join(f"file '{p.name}'\n" for p in parts))
        sh(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', str(lst), '-c', 'copy', '-movflags', '+faststart', str(out)])
    shutil.rmtree(work)
    if plan.get('music'):
        print('  mixing music bed'); tmp = out.with_name(f'.{out.stem}-nomusic{out.suffix}'); out.rename(tmp)
        add_music(tmp, plan['music'], base, book_s(open_c, ls), book_s(close_c, ls), out); tmp.unlink()
    print('wrote', out, f'({dur(out) / 60:.1f} min)')

if __name__ == '__main__': main()
