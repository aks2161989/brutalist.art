"""Write film/beat_sheet.md (human-readable table) from film/beat_sheet.json.

Usage: beat_sheet_md.py <model-folder>/film
"""
import json
import sys
from pathlib import Path

WPS, PAD = 3.0, 0.4


def cell(s):
    return str(s).replace('|', '\\|').replace('\n', ' ')


def main(film):
    film = Path(film)
    sheet = json.loads((film / 'beat_sheet.json').read_text())
    m, beats = sheet['metadata'], sheet['beats']
    total = sum(b['estimated_duration_s'] for b in beats)
    out = ['# %s: film beat sheet' % m['title'], '',
           '> Brutalist beat sheet (`beat_sheet.json`), written with the `blender-modelbuild` skill. '
           'Beat sheet only: Professor Bear renders the film with his own tools.', '',
           '- **Narrator:** the Liam voice only. Quotes from the notes are read as "Professor Bear said ...".',
           '- **Closing card:** "%s"' % m['closing_card'],
           '- **Captions:** none. No subtitles, no .srt.',
           '- **Model:** %s, round %s. Shot paths are relative to this `film/` folder.' % (m['model_name'], m['model_round']),
           '- **Beats:** %d. **Estimated runtime:** %d:%02d (about %.0f s, from word count; real timing comes from the audio).'
           % (len(beats), *divmod(round(total), 60), total),
           '- **Hand steps** marked "Blender UI reconstruction" are hypothetical teaching steps, not a recorded session.', '',
           '| Beat | Act | Segment | Est. s | On screen | Narration (the Liam voice) |', '|---|---|---|---|---|---|']
    for b in beats:
        sh = b['shot']
        scr = '<br>'.join('`%s`' % a for a in sh.get('assets', [])) or cell(sh.get('card_title', '') + ' / ' + sh.get('card_text', ''))
        out.append('| %s | %s | %s | %.1f | %s<br>%s | %s |' % (
            b['beat_id'], b['act'], cell(b['segment']), b['estimated_duration_s'],
            cell(sh.get('label', '')), scr, cell(b['narration_text'])))
    hand = [b for b in beats if b.get('ui_steps')]
    if hand:
        out += ['', '## Hand-build steps (Blender UI reconstruction, hypothetical)', '']
        for b in hand:
            out.append('**%s, %s.** ' % (b['beat_id'], b['segment']) + ' '.join(
                '%d. %s' % (i + 1, s) for i, s in enumerate(b['ui_steps']['steps'])))
            out.append('')
    ai = [b for b in beats if b.get('ai_did')]
    if ai:
        out += ['', '## What the AI script did (evidence)', '']
        for b in ai:
            out.append('- **%s:** %s (%s)' % (b['beat_id'], b['ai_did']['summary'],
                       ', '.join('`../%s`' % p for p in b['ai_did']['evidence'])))
    ev = json.loads((film / 'modelbuild-evidence.json').read_text())
    out += ['', '## What the evidence does not establish', ''] + ['- ' + s for s in ev['not_established']]
    (film / 'beat_sheet.md').write_text('\n'.join(out) + '\n')
    print('wrote', film / 'beat_sheet.md')


if __name__ == '__main__':
    main(sys.argv[1])
