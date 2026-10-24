"""Fill sha256 for every file and asset in film/modelbuild-evidence.json, and
record the runtime estimate in beat_sheet.json metadata and beat t_start values.

Usage: hash_ledger.py <model-folder>/film
Run after editing the ledger or the narration; then run verify_modelbuild.py.
"""
import hashlib
import json
import sys
from pathlib import Path

WPS, PAD = 3.0, 0.4


def main(film):
    film = Path(film).resolve()
    lp, sp = film / 'modelbuild-evidence.json', film / 'beat_sheet.json'
    data, sheet = json.loads(lp.read_text()), json.loads(sp.read_text())
    model = (film / data.get('model_folder', '..')).resolve()
    for rec in data.get('files', []) + data.get('assets', []):
        rec['sha256'] = hashlib.sha256((model / rec['path']).read_bytes()).hexdigest()
    t = 0.0
    for b in sheet['beats']:
        b['estimated_duration_s'] = round(len(b['narration_text'].split()) / WPS + PAD, 1)
        b['t_start'] = round(t, 1)
        t += b['estimated_duration_s']
    sheet['metadata']['est_runtime_s'] = round(t, 1)
    lp.write_text(json.dumps(data, indent=2) + '\n')
    sp.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + '\n')
    print('hashed %d records; est runtime %.1f s' % (len(data.get('files', []) + data.get('assets', [])), t))


if __name__ == '__main__':
    main(sys.argv[1])
