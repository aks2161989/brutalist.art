#!/usr/bin/env python3
"""Read-only film audit from a pasted isdone list; never approves or publishes.

Writes source evidence, master probes and contact sheets to --out. A flag is a
review lead, not proof of fabrication. Never executes code from a film.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess

from PIL import Image, ImageDraw
from math_layout_check import math_layout_errors


def inventory(text):
    return [(int(n), p) for n, p in re.findall(
        r'^\s+(\d+)\.\s+.*?\s((?:[^\s]+/)+[^\s]+)\s*$', text, re.M)]


def probe(path):
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_streams',
                             '-show_format', '-of', 'json', str(path)],
                            capture_output=True, text=True, timeout=30)
    return json.loads(result.stdout) if result.returncode == 0 else {'error': result.stderr}


def sample_master(record, out):
    """Twelve distributed master frames; does not infer beat alignment."""
    master = record.get('master')
    duration = float(record.get('duration') or 0)
    if not master or duration <= 0:
        return None
    contact = Image.new('RGB', (1600, 3*249), '#eee9e1')
    draw = ImageDraw.Draw(contact)
    for i in range(12):
        at = duration*(i+.5)/12
        result = subprocess.run(['ffmpeg','-v','error','-ss',str(at),'-i',master,
            '-frames:v','1','-vf','scale=400:225:force_original_aspect_ratio=decrease,pad=400:225:(ow-iw)/2:(oh-ih)/2',
            '-f','image2pipe','-vcodec','png','-threads','1','-'], capture_output=True, timeout=30)
        x,y=(i%4)*400,(i//4)*249
        draw.text((x+8,y+5),f'{record["number"]:02d} master / {at:.1f}s',fill='#181818')
        if result.returncode == 0 and result.stdout:
            contact.paste(Image.open(io.BytesIO(result.stdout)).convert('RGB'),(x,y+24))
    path=out/f'{record["number"]:02d}-master.jpg'
    contact.save(path,quality=90)
    return str(path)


def audit(n, relative, root, out):
    reel = (root / relative).resolve()
    if not reel.is_relative_to(root.resolve()):
        raise ValueError('Reel outside books root')
    sheet_path = reel / 'beat_sheet.json'
    raw = sheet_path.read_bytes()
    sheet = json.loads(raw)
    beats = sheet.get('beats', [])
    # Exact candidate rule in SCRIPTS/isdone.py: largest root/mp4 master.
    candidates = [p for p in [*reel.glob('*.mp4'), *reel.glob('mp4/*.mp4')]
                  if p.is_file() and p.stat().st_size > 200000]
    master = max(candidates, key=lambda p: p.stat().st_size) if candidates else None
    meta = probe(master) if master else {}
    video = next((s for s in meta.get('streams', []) if s.get('codec_type') == 'video'), {})
    findings, pantry, code, samples = [], [], [], []
    for error in math_layout_errors(sheet):
        findings.append({'category': 'math-layout', 'confidence': 'source-confirmed', 'detail': error})
    for beat in beats:
        bid = beat.get('beat_id', '?')
        shot = beat.get('shot') or {}
        rem = shot.get('remotion') or {}
        props = rem.get('props') or {}
        intent = shot.get('visual_intent') or shot.get('brief', '')
        pantry_path = shot.get('pantry_path') or shot.get('pantry_file') or shot.get('pantry')
        if pantry_path:
            text = ' '.join(str(shot.get(k, '')) for k in ('visual_intent', 'brief', 'subject', 'search_terms', 'hold_reason'))
            reproducible = bool(re.search(r'hand[- ](?:lettered|written|drawn)|index cards?|sticky note|terminal|REPL|pytest|notebook.*(?:ledger|rows|checks|boxes)', text, re.I))
            category = 'replace-with-code-data-or-diagram' if reproducible else 'source-artifact-or-illustration-review'
            item = {'beat': bid, 'category': category, 'intent': intent, 'path': pantry_path,
                    'exists': (reel / pantry_path).exists()}
            pantry.append(item)
            findings.append({**item, 'confidence': 'routing-review'})
        if 'Code' in rem.get('pattern', ''):
            code.append({'beat': bid, 'pattern': rem['pattern'], 'props': props, 'intent': intent})
        if re.search(r'overflows? to infinity', beat.get('narration_text', ''), re.I):
            findings.append({'beat': bid, 'category': 'overflow-claim-review',
                             'confidence': 'review', 'detail': beat['narration_text']})
        src = (beat.get('build') or {}).get('src')
        local = reel / src if src else reel / 'media' / f'{bid}.mp4'
        if not local.is_file() or local.suffix.lower() != '.mp4':
            local = reel / 'media' / f'{bid}.mp4'
        if not local.is_file():
            local = reel / 'clips' / f'{bid}.mp4'
        # Source-beat frames avoid pretending stale-master timing matches a new sheet.
        if local.is_file():
            samples.append((bid, local))
    contact = Image.new('RGB', (1600, max(1, (len(samples)+3)//4)*249), '#eee9e1')
    draw = ImageDraw.Draw(contact)
    sample_records = []
    for i, (bid, local) in enumerate(samples):
        try:
            duration = float(probe(local).get('format', {}).get('duration', 0))
            at = duration * .70
            result = subprocess.run(['ffmpeg','-v','error','-ss',str(at),'-i',str(local),
                '-frames:v','1','-vf','scale=400:225:force_original_aspect_ratio=decrease,pad=400:225:(ow-iw)/2:(oh-ih)/2',
                '-f','image2pipe','-vcodec','png','-threads','1','-'], capture_output=True, timeout=30)
            frame = Image.open(io.BytesIO(result.stdout)).convert('RGB')
            x, y = (i%4)*400, (i//4)*249
            contact.paste(frame, (x,y+24)); draw.text((x+8,y+5), f'{n:02d} / {bid} / 70%', fill='#181818')
            sample_records.append({'beat': bid, 'source': str(local), 'seconds': at, 'status': 'sampled'})
        except Exception as exc:
            sample_records.append({'beat': bid, 'status': 'error', 'error': str(exc)})
    contact_path = out / f'{n:02d}-contact.jpg'
    contact.save(contact_path, quality=88)
    evidence_files = [str(p.relative_to(reel)) for p in reel.rglob('*') if p.is_file()
                      and len(p.relative_to(reel).parts) <= 3
                      and re.search(r'(evidence|session|stdout|stderr|receipt|execution|test.*log)', str(p.relative_to(reel)), re.I)
                      and p.suffix.lower() in ('.json','.txt','.md','.log','.py')]
    return {'number': n, 'relative': relative, 'reel': str(reel), 'beats': len(beats),
            'sheet_sha256': hashlib.sha256(raw).hexdigest(), 'master': str(master) if master else None,
            'stale': master.stat().st_mtime < sheet_path.stat().st_mtime if master else None,
            'width': video.get('width'), 'height': video.get('height'),
            'duration': meta.get('format',{}).get('duration'),
            'audio_stream': any(s.get('codec_type')=='audio' for s in meta.get('streams',[])),
            'declared_slates': [b.get('beat_id') for b in beats if (b.get('build') or {}).get('status','SLATE').upper() in ('SLATE','NONE','')],
            'findings': findings, 'pantry': pantry, 'code_displays': code,
            'evidence_file_candidates': evidence_files, 'samples': sample_records,
            'contact': str(contact_path), 'visual_review': 'not yet reviewed'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--list', required=True, type=Path)
    parser.add_argument('--root', required=True, type=Path)
    parser.add_argument('--out', required=True, type=Path)
    args = parser.parse_args()
    reels = inventory(args.list.read_text())
    if not reels or len(set(p for _, p in reels)) != len(reels):
        raise ValueError('Empty or duplicate reel list')
    args.out.mkdir(parents=True, exist_ok=True)
    def job(item):
        n, relative = item
        result = audit(n, relative, args.root, args.out)
        result['master_contact'] = sample_master(result, args.out)
        (args.out / f'{n:02d}-source.json').write_text(json.dumps(result, indent=2)+'\n')
        print(f'{n:02d}: {result["beats"]} beats; {len(result["findings"])} leads; {len(result["samples"])} frame samples', flush=True)
        return result
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(job, reels))
    payload = {'created': datetime.now(timezone.utc).isoformat(), 'scope': str(args.list),
               'limitations': 'Source audit plus 70%-position source-beat frames, not continuous playback or empirical validation of every claim. Missing receipts do not prove fabrication. No human approvals changed.',
               'reels': results}
    (args.out/'audit.json').write_text(json.dumps(payload, indent=2)+'\n')


if __name__ == '__main__':
    main()
