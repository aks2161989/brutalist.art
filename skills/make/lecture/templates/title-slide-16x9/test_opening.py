"""Local regression tests for narrated timing and legacy bookend compatibility."""
import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

import build

spec = importlib.util.spec_from_file_location('bookend_check', build.TOOLKIT / 'runtime/scripts/bookend_check.py')
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


def remotion(bid, pattern, **props):
    return {'beat_id': bid, 'shot': {'remotion': {'pattern': pattern, 'props': props}}}


class OpeningTests(unittest.TestCase):
    def setUp(self):
        self.sheet = {'metadata': {'skill': 'lecture', 'title': 'Example'}, 'beats': [
            {'beat_id': 'BOPEN', 'narration_text': 'Playlist. Example. Learn the workflow.',
             'actual_duration_s': 9.2, 'audio_file': 'mp3/BOPEN.wav',
             'shot': {'template': 'lecture-title-slide-16x9',
                      'narration_contract': 'playlist-title-summary-v1'}},
            remotion('BIDEA', 'BrutalistHesitantWriter'),
            remotion('BVDT', 'ClaudeVerdictArtifact'),
            remotion('BHTF', 'ClaudeComposerAsk', topic='YOUR TURN'),
            remotion('BOUT', 'ClaudeTitleOutro', title='Example', handle='@NikBearBrown')]}

    def check(self, sheet, audio=True):
        # File-existence fixtures only; compiler's separate audio gate checks sound.
        with tempfile.TemporaryDirectory(prefix='lecture-opening-test-') as temp:
            reel = Path(temp)
            (reel / 'media').mkdir()
            (reel / 'media/BOPEN.mp4').touch()
            if audio:
                (reel / 'mp3').mkdir()
                (reel / 'mp3/BOPEN.wav').touch()
            (reel / 'beat_sheet.json').write_text(json.dumps(sheet))
            with contextlib.redirect_stdout(io.StringIO()):
                return gate.run(temp)

    def test_audio_length_hold(self):
        self.assertEqual(build.hold_duration(None, self.sheet), 9.2)
        self.assertEqual(build.hold_duration(12.0, self.sheet), 12.0)
        self.assertEqual(build.hold_duration(None), 3.0)
        for value in [None, 0, -1, True, float('nan'), float('inf'), '9']:
            with self.subTest(value=value), self.assertRaises(ValueError):
                build.hold_duration(None, {'beats': [{'beat_id': 'BOPEN', 'actual_duration_s': value}]})

    def test_narrated_opening(self):
        self.assertEqual(self.check(self.sheet), 0)
        self.assertEqual(self.check(self.sheet, audio=False), 2)
        for change in [{'narration_text': ''}, {'audio_policy': 'silence'}, {'actual_duration_s': 0}]:
            sheet = copy.deepcopy(self.sheet)
            sheet['beats'][0].update(change)
            with self.subTest(change=change):
                self.assertEqual(self.check(sheet), 2)

    def test_legacy_compatibility(self):
        sheet = copy.deepcopy(self.sheet)
        opening = sheet['beats'][0]
        opening.update(narration_text='', audio_policy='silence', actual_duration_s=2.5)
        del opening['shot']['narration_contract']
        self.assertEqual(self.check(sheet), 0)
        opening['actual_duration_s'] = 5
        self.assertEqual(self.check(sheet), 2)
        sheet['beats'].pop(0)
        self.assertEqual(self.check(sheet), 0)


if __name__ == '__main__':
    unittest.main()
