#!/usr/bin/env python3
"""Read-only structural evidence check; not editorial or human certification."""
import argparse
import hashlib
import json
from pathlib import Path


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check(reel, document):
    reel, document = Path(reel).resolve(), Path(document).resolve()
    ledger = json.loads((reel / 'gdd-evidence.json').read_text())
    sheet = json.loads((reel / 'beat_sheet.json').read_text())
    require(ledger['schema_version'] == 1, 'Unsupported ledger schema')
    require(digest(document) == ledger['document']['sha256'], 'GDD hash mismatch')
    lines = document.read_text().splitlines()
    headings = [line[3:].strip() for line in lines if line.startswith('## ')]
    require(headings, 'No top-level GDD sections found; adapt checker for this document structure')
    beats = {b['beat_id']: b for b in sheet['beats']}
    require(len(beats) == len(sheet['beats']), 'Duplicate beat IDs')

    def narrated(beat_id):
        require(beat_id in beats, f'Unknown beat {beat_id}')
        require(bool(beats[beat_id].get('narration_text', '').strip()), f'Unnarrated beat {beat_id}')
        return beats[beat_id]

    seen = []
    for section in ledger['sections']:
        seen.append(section['heading'])
        ids = section.get('beat_ids', [])
        exclusion = section.get('exclusion', '').strip()
        require(bool(ids) != bool(exclusion), 'Section must have coverage OR reasoned exclusion')
        for beat_id in ids:
            narrated(beat_id)
    require(len(seen) == len(set(seen)), 'Duplicate section coverage')
    require(sorted(seen) == sorted(headings), 'GDD section coverage mismatch')
    excerpt_beats = set()
    for excerpt in ledger['excerpts']:
        beat = narrated(excerpt['beat_id'])
        start, end = excerpt['start_line'], excerpt['end_line']
        require(type(start) is int and type(end) is int and 1 <= start <= end <= len(lines), 'Invalid excerpt range')
        exact = '\n'.join(lines[start - 1:end])
        require(exact == excerpt['text'], 'GDD excerpt differs from source')
        props = beat.get('shot', {}).get('remotion', {}).get('props', {})
        require(props.get('excerpt') == exact, 'Displayed excerpt differs from ledger')
        require(excerpt['beat_id'] not in excerpt_beats, 'Duplicate excerpt beat')
        excerpt_beats.add(excerpt['beat_id'])
    require(excerpt_beats, 'No exact document excerpts')
    for beat in beats.values():
        if beat.get('act') == 'BODY':
            require(beat.get('design_status') in {'proposed', 'implemented', 'observed', 'pending', 'comparison'}, 'Missing/invalid design status')
        if beat.get('shot', {}).get('remotion', {}).get('props', {}).get('excerpt'):
            require(beat['beat_id'] in excerpt_beats, 'Displayed excerpt lacks source record')
    evidence_paths = set()
    for item in ledger['evidence']:
        relative = Path(item['path'])
        require(not relative.is_absolute(), 'Evidence path must be relative')
        target = (reel / relative).resolve()
        require(target.is_relative_to(reel) and target.is_file(), 'Evidence escapes reel or is missing')
        require(target not in evidence_paths, 'Duplicate evidence file')
        evidence_paths.add(target)
        require(digest(target) == item['sha256'], 'Evidence hash mismatch')
        require(item.get('method', '').strip() and item.get('supports', '').strip(), 'Evidence needs method and claim')
    require(evidence_paths, 'No evidence records')
    return {'sections': len(seen), 'excerpts': len(excerpt_beats), 'evidence_files': len(evidence_paths)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('reel', type=Path)
    parser.add_argument('--gdd', required=True, type=Path)
    args = parser.parse_args()
    try:
        result = check(args.reel, args.gdd)
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(1, f'GDD evidence check FAILED: {error}\n')
    print('GDD evidence check PASS: ' + json.dumps(result))
    print('Structural coverage only; editorial accuracy and human judgment are separate.')


if __name__ == '__main__':
    main()
