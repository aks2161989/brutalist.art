"""Read-only source coverage and exact excerpt checks for a Godot development film."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

def require(ok, message):
    if not ok:
        raise ValueError(message)

def present(value):
    return isinstance(value, str) and bool(value.strip())

def inside(root, value):
    require(present(value) and not Path(value).is_absolute(), 'Expected relative source path')
    result = (root / value).resolve()
    require(result.is_relative_to(root) and result.is_file(), 'Missing or escaping source: ' + value)
    return result

def inventory(root):
    return {p.relative_to(root).as_posix() for p in root.rglob('*')
            if p.is_file() and not any(x in ('.godot', '.git') for x in p.relative_to(root).parts)
            and p.suffix != '.uid'}

def verify(reel, game):
    reel, game = Path(reel).resolve(), Path(game).resolve()
    require((game / 'project.godot').is_file(), '--game must contain project.godot')
    sheet = json.loads((reel / 'beat_sheet.json').read_text())
    data = json.loads((reel / 'gamedev-evidence.json').read_text())
    require(data.get('schema_version') == 1, 'Unknown evidence schema')
    beats = {b['beat_id']: b for b in sheet['beats']}
    require(len(beats) == len(sheet['beats']), 'Duplicate beat ids')
    components = {c['id']: c for c in data['components']}
    require(components and len(components) == len(data['components']), 'Empty or duplicate components')
    records = {f['path']: f for f in data['files']}
    require(len(records) == len(data['files']), 'Duplicate source records')
    excluded = {f['path']: f for f in data.get('exclusions', [])}
    require(len(excluded) == len(data.get('exclusions', [])), 'Duplicate exclusions')
    require(not set(records) & set(excluded), 'File both included and excluded')
    require(set(records) | set(excluded) == inventory(game), 'Inventory coverage mismatch')
    for p, f in excluded.items():
        inside(game, p)
        require(present(f.get('reason')), 'Exclusion requires a reason')
    for p, f in records.items():
        source = inside(game, p)
        require(hashlib.sha256(source.read_bytes()).hexdigest() == f['sha256'], 'Source hash mismatch: ' + p)
        require(present(f.get('role')) and f.get('component_ids'), 'Unassociated source: ' + p)
        require(all(c in components and p in components[c]['files'] for c in f['component_ids']), 'Broken source/component association')
    for cid, c in components.items():
        require(present(cid) and present(c.get('explanation')), 'Component lacks explanation')
        require(c.get('files') and all(p in records and cid in records[p]['component_ids'] for p in c['files']), 'Component source missing: ' + cid)
        require(c.get('beat_ids') and all(b in beats and present(beats[b].get('narration_text')) for b in c['beat_ids']), 'Component beat missing: ' + cid)
    excerpts = data.get('excerpts', [])
    require(excerpts, 'No source excerpts')
    for e in excerpts:
        require(e['path'] in records and e['beat_id'] in beats, 'Unknown excerpt source/beat')
        lines = inside(game, e['path']).read_text().splitlines()
        start, end = e['start_line'], e['end_line']
        require(type(start) is int and type(end) is int and 1 <= start <= end <= len(lines), 'Invalid source line range')
        text = '\n'.join(lines[start-1:end])
        require(text == e['text'], 'Excerpt differs from source')
        shown = beats[e['beat_id']].get('shot', {}).get('remotion', {}).get('props', {}).get('code')
        require(shown == text, 'Displayed code differs from excerpt')
    shown_beats = {bid for bid, b in beats.items()
                   if b.get('shot', {}).get('remotion', {}).get('pattern', '').startswith('GodotDevWorkbench')
                   and b['shot']['remotion'].get('props', {}).get('code')}
    require(shown_beats == {e['beat_id'] for e in excerpts}, 'Displayed code lacks an excerpt record')
    contract = data.get('teaching_contract')
    pair_count = 0
    if contract is not None:
        require(contract == 'code-then-result-v1', 'Unknown teaching contract')
        pairs = data.get('code_result_pairs', [])
        require(isinstance(pairs, list), 'Code/result pairs must be a list')
        require(len(pairs) == len(shown_beats), 'Each code beat needs one visible result')
        require({p['code_beat'] for p in pairs} == shown_beats, 'Missing or duplicate code/result pair')
        order = list(beats)
        for p in pairs:
            code, result = p['code_beat'], p['result_beat']
            index = order.index(code)
            require(index + 1 < len(order) and order[index + 1] == result,
                    'Visible result must immediately follow code: ' + code)
            require(result not in shown_beats and present(beats[result].get('narration_text')),
                    'Result must be narrated visual evidence, not more code: ' + result)
            require(present(p.get('observation')), 'Result needs an observed consequence')
            media = p['media']
            source = inside(reel, media['path'])
            require(source.suffix.lower() in ('.mp4', '.mov', '.png', '.jpg', '.jpeg'),
                    'Result evidence must be visible media')
            require(hashlib.sha256(source.read_bytes()).hexdigest() == media['sha256'],
                    'Result media hash mismatch: ' + result)
            require(beats[result].get('shot', {}).get('evidence_media') == media['path'],
                    'Result beat does not reference paired media: ' + result)
        pair_count = len(pairs)
    return {'status': 'PASS', 'source_files': len(records), 'exclusions': len(excluded),
            'components': len(components), 'exact_excerpts': len(excerpts),
            'teaching_contract': contract, 'code_result_pairs': pair_count,
            'scope': 'Hashes, inventory, source lines and associations; not semantic/visual approval.'}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('reel')
    parser.add_argument('--game', required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(verify(args.reel, args.game), indent=2))
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print('Godot gamedev evidence FAIL: ' + str(exc), file=sys.stderr)
        sys.exit(1)
