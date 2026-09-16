#!/usr/bin/env python3
"""Read-only gameplay evidence gate. Does not certify semantic/visual truth."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import sys


class CoverageError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise CoverageError(message)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def file_in(root, value):
    require(nonempty(value), 'Expected a nonempty relative file path')
    relative = Path(value)
    require(not relative.is_absolute(), f'Absolute evidence path: {value}')
    path = (root / relative).resolve()
    require(path.is_relative_to(root), f'Evidence escapes reel: {value}')
    require(path.is_file() and path.stat().st_size > 0, f'Missing/empty evidence: {value}')
    return path


def positive(value, label):
    require(isinstance(value, (int, float)) and not isinstance(value, bool)
            and math.isfinite(value) and value > 0, f'Invalid {label}')
    return value


def probe(path):
    result = subprocess.run([
        'ffprobe', '-v', 'error', '-show_streams', '-show_format',
        '-of', 'json', str(path)
    ], capture_output=True, text=True, timeout=30, check=True)
    data = json.loads(result.stdout)
    videos = [s for s in data.get('streams', []) if s.get('codec_type') == 'video']
    require(len(videos) == 1, f'Expected one video stream: {path.name}')
    video = videos[0]
    duration = float(video.get('duration') or data.get('format', {}).get('duration', 0))
    return {'width': int(video['width']), 'height': int(video['height']),
            'duration_s': positive(duration, f'duration in {path.name}')}


def verify(root, min_height=2160):
    root = Path(root).resolve()
    positive(min_height, 'minimum height')
    coverage = json.loads(file_in(root, 'coverage.json').read_text())
    sheet = json.loads(file_in(root, 'beat_sheet.json').read_text())
    require(isinstance(coverage, dict) and coverage.get('schema_version') == 1,
            'Expected coverage schema_version 1')
    require(isinstance(sheet, dict), 'Beat sheet must be an object')
    game = coverage.get('game')
    require(isinstance(game, dict) and nonempty(game.get('name')), 'Missing game identity')
    build_id = game.get('build_id', '')
    require(isinstance(build_id, str) and re.fullmatch(r'[a-f0-9]{64}', build_id),
            'build_id must be a source-snapshot SHA-256')
    beats = sheet.get('beats')
    require(isinstance(beats, list) and beats, 'Missing beat list')
    by_id = {}
    for beat in beats:
        require(isinstance(beat, dict) and nonempty(beat.get('beat_id')), 'Invalid beat')
        bid = beat['beat_id']
        require(bid not in by_id, f'Duplicate beat: {bid}')
        by_id[bid] = beat
    captures = coverage.get('captures')
    require(isinstance(captures, dict) and captures, 'No captures recorded')
    properties = {}
    for cid, capture in captures.items():
        require(nonempty(cid) and isinstance(capture, dict), 'Invalid capture record')
        require(capture.get('build_id') == build_id, f'{cid}: stale/different game build')
        require(capture.get('method') in ('scripted-input', 'human-input'),
                f'{cid}: capture must identify actual input method')
        file_in(root, capture.get('input_log'))
        path = file_in(root, capture.get('path'))
        require(capture.get('sha256') == sha256(path), f'{cid}: capture hash mismatch')
        props = probe(path)
        require(props['height'] >= min_height and
                props['width'] >= math.ceil(min_height * 16 / 9),
                f'{cid}: capture below required 16:9 {min_height}p dimensions')
        require(abs(props['width'] / props['height'] - 16 / 9) < 0.01,
                f'{cid}: landscape walkthrough requires 16:9 capture')
        properties[cid] = props
    features = coverage.get('features')
    require(isinstance(features, list) and features, 'No feature inventory')
    seen = set()
    implemented, planned, intervals = 0, 0, 0
    for feature in features:
        require(isinstance(feature, dict) and nonempty(feature.get('id')), 'Invalid feature')
        fid = feature['id']
        require(fid not in seen, f'Duplicate feature: {fid}')
        seen.add(fid)
        status = feature.get('status')
        require(status in ('implemented', 'planned'), f'{fid}: invalid feature status')
        evidence = feature.get('evidence')
        require(isinstance(evidence, list), f'{fid}: evidence must be a list')
        if status == 'planned':
            require(not evidence and nonempty(feature.get('reason')),
                    f'{fid}: planned features need a reason, not gameplay evidence')
            planned += 1
            continue
        implemented += 1
        require(evidence, f'{fid}: implemented feature has no gameplay evidence')
        for event in evidence:
            require(isinstance(event, dict), f'{fid}: invalid evidence interval')
            cid = event.get('capture')
            require(isinstance(cid, str) and cid in properties, f'{fid}: unknown capture')
            bid = event.get('beat_id')
            require(isinstance(bid, str) and bid in by_id, f'{fid}: unknown beat')
            require(nonempty(by_id[bid].get('narration_text')), f'{fid}: beat has no narration')
            times = [event.get(key) for key in ('start_s', 'action_s', 'end_s')]
            require(all(isinstance(t, (float, int)) and not isinstance(t, bool)
                        and math.isfinite(t) for t in times), f'{fid}: nonfinite/invalid times')
            start, action, end = times
            require(0 <= start < action < end <= properties[cid]['duration_s'] + 0.001,
                    f'{fid}: require visible before < action < after within capture')
            require(nonempty(event.get('observation')) and nonempty(event.get('riff')),
                    f'{fid}: missing observation or riff')
            intervals += 1
    require(implemented > 0, 'No implemented features demonstrated')
    return {'status': 'PASS', 'game': game['name'], 'implemented_features': implemented,
            'planned_features': planned, 'evidence_intervals': intervals,
            'captures': properties,
            'scope': 'Structural/media evidence only; visual truth, inventory completeness, '
                     'native render provenance and final-film QC still require review.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('reel', type=Path)
    parser.add_argument('--min-height', type=int, default=2160,
                        help='Pilot/test override only; final walkthroughs require 2160 (default)')
    args = parser.parse_args()
    try:
        print(json.dumps(verify(args.reel, args.min_height), indent=2))
    except (CoverageError, OSError, ValueError, KeyError, TypeError,
            subprocess.SubprocessError) as exc:
        print(f'Walkthrough evidence FAIL: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
