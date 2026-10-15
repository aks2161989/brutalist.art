"""Opt-in, fail-closed reuse of a verified lecture's unchanged encoded body.

Only an official BOPEN title-card replacement is supported. The caller still
runs the normal typography, preflight, audio, decode and final-frame gates.
"""
import copy
from fractions import Fraction
import json
import math
from pathlib import Path
import subprocess

from build_safety import BuildError, file_digest


def run(args):
    result = subprocess.run(list(map(str, args)), capture_output=True, text=True)
    if result.returncode:
        raise BuildError('Verified-body command failed: ' + result.stderr[-1200:])
    return result.stdout


def probe(path):
    return json.loads(run(['ffprobe', '-v', 'error', '-show_streams', '-show_format', '-of', 'json', path]))


def normalized_body(beats):
    body = copy.deepcopy(beats[1:])
    for beat in body:
        beat.get('build', {}).pop('at', None)
    return body


def validate_reuse(folder, sheet, fps, width, height, input_hashes):
    config = sheet.get('metadata', {}).get('verified_body_reuse')
    if not config:
        return None
    paths = {}
    for key in ('master', 'sheet', 'receipt'):
        path = (folder / config[key]).resolve()
        if not path.is_relative_to(folder) or not path.is_file():
            raise BuildError(f'Verified-body {key} must be a preserved file inside this reel')
        paths[key] = path
    prior = json.loads(paths['receipt'].read_text())
    old = json.loads(paths['sheet'].read_text())
    if prior.get('status') != 'ready' or file_digest(paths['master']) != prior.get('sha256'):
        raise BuildError('Verified-body master does not match its ready receipt')
    if normalized_body(old['beats']) != normalized_body(sheet['beats']):
        raise BuildError('Verified-body reuse refused: later beats changed')
    for data in (old, sheet):
        first = data['beats'][0]
        if first.get('beat_id') != 'BOPEN' or first.get('shot', {}).get('template') != 'lecture-title-slide-16x9':
            raise BuildError('Verified-body reuse supports only an official lecture BOPEN replacement')
    for key in ('title', 'channel', 'channel_title', 'fit', 'source_sha256', 'source_commit',
                'aspect_ratio', 'fps', 'width', 'height', 'palette', 'style_preset', 'skill',
                'playlist', 'series_title', 'series_video_number', 'series_video_count',
                'voice', 'voice_kokoro', 'persona', 'course', 'caption_policy', 'keep_review_labels'):
        if old['metadata'].get(key) != sheet['metadata'].get(key):
            raise BuildError(f'Verified-body metadata changed: {key}')
    first_media = str((folder / 'media/BOPEN.mp4').resolve())
    first_audio = str((folder / old['beats'][0]['audio_file']).resolve()) if old['beats'][0].get('audio_file') else None
    for path, expected in prior['input_sha256'].items():
        if path not in (first_media, first_audio) and (input_hashes.get(path) != expected or file_digest(path) != expected):
            raise BuildError(f'Verified-body source changed or disappeared: {path}')
    video = next(s for s in probe(paths['master'])['streams'] if s['codec_type'] == 'video')
    if (video['width'], video['height'], Fraction(video['r_frame_rate']), video['codec_name'], video['pix_fmt']) != (width, height, Fraction(fps), 'h264', 'yuv420p'):
        raise BuildError('Verified-body codec, dimensions or frame rate are incompatible')
    cut_frames = math.ceil(old['beats'][0]['actual_duration_s'] * fps - 1e-8)
    cut = cut_frames / fps
    frames = json.loads(run(['ffprobe', '-v', 'error', '-select_streams', 'v:0',
        '-read_intervals', f'0%{cut + 1/fps}', '-show_frames',
        '-show_entries', 'frame=best_effort_timestamp_time,key_frame', '-of', 'json', paths['master']]))['frames']
    if not any(f.get('key_frame') == 1 and abs(float(f['best_effort_timestamp_time']) - cut) < .001 for f in frames):
        raise BuildError('Verified-body cut is not an independent keyframe; use a normal full encode')
    old_frames = sum(math.ceil(b['actual_duration_s'] * fps - 1e-8) for b in old['beats'])
    if abs(prior['duration_s'] * fps - old_frames) > .01:
        raise BuildError('Verified-body prior timeline does not match its receipt')
    actual_frames = int(video.get('nb_frames') or 0)
    if actual_frames <= cut_frames or abs(actual_frames - old_frames) > 1:
        raise BuildError('Verified-body frame count is incompatible with its certified timeline')
    input_hashes[str(paths['master'])] = prior['sha256']
    return {'kind': 'verified-master-body-copy', 'previous_master': str(paths['master']),
            'previous_sha256': prior['sha256'], 'old_opening_frames': cut_frames,
            'body_frames': actual_frames - cut_frames, 'timeline_body_frames': old_frames - cut_frames,
            'fps': fps, 'width': width, 'height': height}


def make_concat(record, first_clip, first_frames, work, concat_line):
    prefix, body = work / 'verified-new-opening.mp4', work / 'verified-old-body.mp4'
    fps = record['fps']
    run(['ffmpeg', '-y', '-v', 'error', '-i', first_clip, '-frames:v', first_frames,
         '-an', '-c:v', 'libx264', '-preset', 'slow', '-crf', '16', '-pix_fmt', 'yuv420p', prefix])
    run(['ffmpeg', '-y', '-v', 'error', '-ss', record['old_opening_frames']/fps,
         '-i', record['previous_master'], '-map', '0:v:0', '-an', '-c:v', 'copy',
         '-t', record['body_frames']/fps, body])
    for path in (prefix, body):
        video = next(s for s in probe(path)['streams'] if s['codec_type'] == 'video')
        if (video['width'], video['height'], Fraction(video['r_frame_rate']), video['pix_fmt']) != (record['width'], record['height'], Fraction(fps), 'yuv420p'):
            raise BuildError('Verified-body splice stream parameters do not match')
    playlist = work / 'verified-body-concat.txt'
    playlist.write_text(concat_line(prefix) + concat_line(body))
    record['new_opening_frames'] = first_frames
    return playlist


def frame_hash(path, frame, fps):
    # Seek just before the target frame, avoiding floating-point boundary rounding.
    time = max(0, (frame - .25) / fps)
    result = run(['ffmpeg', '-v', 'error', '-ss', f'{time:.9f}', '-i', path,
                  '-map', '0:v:0', '-frames:v', '1', '-an', '-f', 'framemd5', '-'])
    rows = [line for line in result.splitlines() if line and not line.startswith('#')]
    if len(rows) != 1:
        raise BuildError(f'Verified-body frame {frame} could not be decoded from {path}')
    return rows[0].split(',')[-1].strip()


def verify_samples(record, candidate):
    results = []
    for relative in sorted({0, record['body_frames']//2, record['body_frames']-1}):
        expected = frame_hash(record['previous_master'], record['old_opening_frames'] + relative, record['fps'])
        actual = frame_hash(candidate, record['new_opening_frames'] + relative, record['fps'])
        if actual != expected:
            raise BuildError(f'Verified-body decoded frame changed at body frame {relative}')
        results.append({'body_frame': relative, 'decoded_md5': actual})
    record['decoded_frame_checks'] = results
