#!/usr/bin/env python3
"""Build editable lecture title cards and an audio-length visual hold.

This is a vector layout generator, not an image-generation or film pipeline.
Run: python3 build.py --out /absolute/output/directory [--data episode.json]
"""
import argparse
import base64
import html
import json
import math
from pathlib import Path
import subprocess
import sys
import textwrap
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
TOOLKIT = HERE.parents[4]
PAGE, INK, ACCENT = '#FAF9F5', '#3D3929', '#D97757'
sys.path.insert(0, str(TOOLKIT/'runtime/scripts'))
from professor_bear import pick

def from_sheet(sheet):
    """Resolve identity from film metadata, never from example defaults."""
    meta = sheet['metadata']
    description = meta.get('lecture_opening_description', '').strip()
    if not description:
        raise ValueError('Set metadata.lecture_opening_description to this film\'s short teaching payoff.')
    title_lines = meta.get('lecture_opening_title_lines') or textwrap.wrap(meta['title'], width=24, break_long_words=False, break_on_hyphens=False)
    series = meta.get('series_title') or meta.get('playlist') or ''
    # NO VIDEO NUMBERS, EVER (Bear, 2026-10-11: "we do not number our videos ... we never know what
    # X is going to be", then "remove all the numbers" -- a new film can always land first). The card
    # carries the series title only: no "Video NN", no "N of X", no "Start here" / "New here?" pointer.
    # series_video_number, series_video_count, series_entry_video and series_numbered are ignored.
    position, pointer = '', ''
    return dict(series_title=series, episode_position=position,
                title_lines=title_lines, subtitle=description,
                portrait_path=pick('1x1', seed=meta['slug'], public=True),
                presenter_name='Professor Bear',
                narrator_credit='Liam, in for Bear · Narration' if meta.get('channel', 'claude-liam') == 'claude-liam' else '',
                entry_pointer=pointer,
                channel_handle=meta.get('channel_title') or '@NikBearBrown', seed=meta['slug'])

def text(name, x, y, copy, size, family='Inter', anchor='start'):
    return (f'<text id="{name}" x="{x}" y="{y}" fill="{INK}" '
            f'font-family="{family}" font-size="{size}" text-anchor="{anchor}">'
            f'{html.escape(copy)}</text>')

def svg(data, placeholder=False):
    title = data['title_lines']
    if not 1 <= len(title) <= 3 or any(len(s) > 28 for s in title):
        raise ValueError('Title needs 1–3 manually balanced lines of at most 28 characters.')
    if len(data['series_title']) > 42 or len(data['subtitle']) > 52:
        raise ValueError('Series title or subtitle exceeds the template copy budget.')
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080">',
             '<title>Lecture opening · editable 16:9 template</title>',
             '<desc>Narrated portrait and film-title card. Named live-text fields are editable.</desc>',
             f'<rect width="1920" height="1080" fill="{PAGE}"/>',
             '<g id="series-and-position">',
             text('series-title',96,124,data['series_title'],52,'EB Garamond'),
             text('episode-position',1824,124,data['episode_position'],32,anchor='end'),
             '</g>',
             '<g id="portrait-slot">']
    if placeholder:
        parts += ['<rect x="96" y="214" width="640" height="640" fill="#EDEBE1"/>',
                  '<path d="M96 214L736 854M736 214L96 854" stroke="#A9A491" stroke-width="2"/>',
                  f'<rect x="196" y="486" width="440" height="96" fill="{PAGE}"/>',
                  text('portrait-placeholder',416,545,'[Portrait Image]',38,anchor='middle')]
    else:
        photo = Path(data['portrait_path'])
        if not photo.is_absolute():
            photo = TOOLKIT / photo
        uri = 'data:image/jpeg;base64,' + base64.b64encode(photo.read_bytes()).decode()
        parts += [f'<image id="portrait-image" x="96" y="214" width="640" height="640" '
                  f'preserveAspectRatio="xMidYMid slice" href="{uri}"/>']
    parts += ['</g>', '<g id="film-title">',
              f'<rect x="832" y="244" width="88" height="8" fill="{ACCENT}"/>']
    size = 108 if max(map(len,title)) <= 20 else 92
    top = 395 if len(title) < 3 else 352
    for i, line in enumerate(title):
        parts.append(text(f'film-title-line-{i+1}',832,top + i*116,line,size,'EB Garamond'))
    parts += [text('series-purpose',832,top + len(title)*116+42,data['subtitle'],36),
              '</g>', '<g id="presenter-credit">',
              text('presenter-name',96,918,data['presenter_name'],42,'EB Garamond'),
              text('narrator-credit',96,965,data['narrator_credit'],28),
              '</g>', '<g id="entry-and-channel">',
              text('newcomer-pointer',832,918,data['entry_pointer'],28),
              text('channel-handle',1824,1005,data['channel_handle'],28,'EB Garamond',anchor='end'),
              '</g>', '</svg>']
    return '\n'.join(parts)

def fit_title(source):
    """Fit the actual font geometry, not just a character-count estimate."""
    query = subprocess.check_output(['inkscape','--query-all',str(source)],text=True)
    factor = 1.0
    for line in query.splitlines():
        if line.startswith('film-title-line-'):
            _, x, _, width, _ = line.split(',')
            factor = min(factor, (1824-float(x))/float(width))
    if factor < 1:
        ET.register_namespace('', 'http://www.w3.org/2000/svg')
        tree=ET.parse(source)
        for element in tree.iter():
            if element.get('id','').startswith('film-title-line-'):
                size=float(element.get('font-size'))*factor*.99
                if size<76:raise ValueError('Title too wide; rebalance it into shorter lines.')
                element.set('font-size',f'{size:.2f}')
        tree.write(source,encoding='unicode')

def hold_duration(explicit, sheet=None):
    """Production follows measured BOPEN audio; design-only previews default to 3s."""
    if explicit is not None:
        duration = explicit
    elif sheet is not None:
        opening = next((b for b in sheet.get('beats', []) if b.get('beat_id') == 'BOPEN'), {})
        duration = opening.get('actual_duration_s')
    else:
        duration = 3.0
    if isinstance(duration, bool) or not isinstance(duration, (int, float)) or not math.isfinite(duration) or duration <= 0:
        raise ValueError('BOPEN needs a positive measured actual_duration_s (or --duration). Generate narration first.')
    return duration

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--data', type=Path, default=HERE/'example.json')
    parser.add_argument('--sheet', type=Path, help='Resolve fields and seeded random portrait from a film beat sheet')
    parser.add_argument('--width', type=int, default=1920, choices=[1920,3840])
    parser.add_argument('--duration', type=float, help='Measured hold duration; defaults to BOPEN.actual_duration_s with --sheet, otherwise 3s preview')
    args = parser.parse_args()
    sheet = json.loads(args.sheet.read_text()) if args.sheet else None
    args.duration = hold_duration(args.duration, sheet)
    args.out.mkdir(parents=True, exist_ok=True)
    example = from_sheet(sheet) if sheet is not None else json.loads(args.data.read_text())
    if not args.sheet and not example.get('portrait_path'):
        example['portrait_path'] = pick('1x1', seed=example.get('seed'), public=True)
    (args.out/'opening-fields.json').write_text(json.dumps(example, indent=2)+'\n')
    blank = dict(example,series_title='[Series Title]',episode_position='',
                 title_lines=['[Film Title]', '[Optional Second Line]'],
                 subtitle='[Series Purpose — Short Phrase]',presenter_name='[Presenter Name]',
                 narrator_credit='[Narrator Credit — Optional]',
                 entry_pointer='',channel_handle='[Channel Handle]')
    for name, data, placeholder in [('template',blank,True),('example',example,False)]:
        source = args.out/f'{name}-16x9.svg'
        source.write_text(svg(data,placeholder))
        fit_title(source)
        subprocess.run(['inkscape',str(source),'--export-type=png',
                        f'--export-width={args.width}',f'--export-filename={args.out/name}-16x9.png'], check=True)
    subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-n','-loop','1',
                    '-i',str(args.out/'example-16x9.png'),'-t',str(args.duration),'-r','30',
                    '-c:v','libx264','-crf','18','-pix_fmt','yuv420p',
                    '-movflags','+faststart',str(args.out/f'example-opening-{args.duration:g}s.mp4')], check=True)
    print(args.out)

if __name__ == '__main__':
    main()
