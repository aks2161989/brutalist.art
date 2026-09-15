"""Real media probes plus failure cases for the new read-only evidence gate."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/make/godot-waikthrough/scripts/verify_walkthrough.py'
spec = importlib.util.spec_from_file_location('walkthrough', SCRIPT)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


@unittest.skipUnless(shutil.which('ffmpeg') and shutil.which('ffprobe'), 'requires ffmpeg/ffprobe')
class EvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix='godot-walkthrough-test-')
        cls.root = Path(cls.temp.name)
        # This is a test fixture, never labeled as actual gameplay.
        subprocess.run(['ffmpeg', '-v', 'error', '-f', 'lavfi', '-i',
                        'testsrc2=size=640x360:rate=24:duration=2',
                        '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
                        str(cls.root / 'fixture.mp4')], check=True, timeout=30)
        (cls.root / 'inputs.jsonl').write_text('{"test_fixture":true,"tick":12,"action":"jump"}\n')
        (cls.root / 'beat_sheet.json').write_text(json.dumps({'beats': [
            {'beat_id': 'B02', 'narration_text': 'Test narration, not a gameplay claim.'}]}))
        cls.base = {'schema_version': 1, 'game': {'name': 'fixture', 'build_id': 'a'*64},
                    'captures': {'take': {'path': 'fixture.mp4',
                        'sha256': gate.sha256(cls.root / 'fixture.mp4'), 'build_id': 'a'*64,
                        'method': 'scripted-input', 'input_log': 'inputs.jsonl'}},
                    'features': [{'id': 'jump', 'status': 'implemented', 'evidence': [{
                        'capture': 'take', 'beat_id': 'B02', 'start_s': 0,
                        'action_s': 0.5, 'end_s': 1.5, 'observation': 'Fixture event',
                        'riff': 'Fixture interpretation'}]}]}

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def setUp(self):
        self.data = copy.deepcopy(self.base)

    def check(self, height=360):
        (self.root / 'coverage.json').write_text(json.dumps(self.data))
        return gate.verify(self.root, height)

    def rejected(self, message):
        with self.assertRaisesRegex(gate.CoverageError, message):
            self.check()

    def test_real_probe_and_valid_pilot(self):
        report = self.check()
        self.assertEqual(report['implemented_features'], 1)
        self.assertEqual(report['captures']['take']['width'], 640)
        self.assertAlmostEqual(report['captures']['take']['duration_s'], 2.0, places=2)

    def test_low_resolution_is_not_final_4k(self):
        with self.assertRaisesRegex(gate.CoverageError, 'below required'):
            self.check(2160)

    def test_no_capture_for_implemented_feature(self):
        self.data['features'][0]['evidence'] = []
        self.rejected('no gameplay evidence')

    def test_missing_feature_cannot_be_silently_passed(self):
        self.data['features'].append({'id': 'pause', 'status': 'implemented', 'evidence': []})
        self.rejected('pause: implemented')

    def test_planned_feature_explicitly_excluded(self):
        self.data['features'].append({'id': 'music', 'status': 'planned',
                                     'reason': 'Not built', 'evidence': []})
        self.assertEqual(self.check()['planned_features'], 1)

    def test_missing_clip(self):
        self.data['captures']['take']['path'] = 'missing.mp4'
        self.rejected('Missing/empty')

    def test_capture_hash_changed(self):
        self.data['captures']['take']['sha256'] = 'b'*64
        self.rejected('hash mismatch')

    def test_source_build_changed(self):
        self.data['game']['build_id'] = 'b'*64
        self.rejected('stale/different')

    def test_missing_input_log(self):
        self.data['captures']['take']['input_log'] = 'missing.jsonl'
        self.rejected('Missing/empty')

    def test_times_past_end(self):
        self.data['features'][0]['evidence'][0]['end_s'] = 3
        self.rejected('within capture')

    def test_no_visible_before_state(self):
        self.data['features'][0]['evidence'][0]['action_s'] = 0
        self.rejected('before < action')

    def test_nonfinite_time(self):
        self.data['features'][0]['evidence'][0]['end_s'] = float('nan')
        self.rejected('nonfinite')

    def test_missing_beat(self):
        self.data['features'][0]['evidence'][0]['beat_id'] = 'B99'
        self.rejected('unknown beat')

    def test_duplicate_features(self):
        self.data['features'].append(copy.deepcopy(self.data['features'][0]))
        self.rejected('Duplicate feature')

    def test_escape_paths(self):
        self.data['captures']['take']['path'] = '../fixture.mp4'
        self.rejected('escapes reel')

    def test_symlink_escape(self):
        with tempfile.TemporaryDirectory(prefix='outside-walkthrough-') as folder:
            outside = Path(folder) / 'clip.mp4'
            outside.write_bytes(b'not inspected')
            link = self.root / 'escape.mp4'
            link.symlink_to(outside)
            try:
                self.data['captures']['take']['path'] = 'escape.mp4'
                self.rejected('escapes reel')
            finally:
                link.unlink()

    def test_cli_fails_closed(self):
        self.data['features'][0]['evidence'] = []
        self.check_write_only()
        result = subprocess.run(['bash', str(ROOT / 'art'), 'godot-waikthrough',
                                 '--check', str(self.root), '--min-height', '360'],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('no gameplay evidence', result.stderr)

    def check_write_only(self):
        (self.root / 'coverage.json').write_text(json.dumps(self.data))


class DiscoveryTests(unittest.TestCase):
    def test_skills_and_alias_resolve_from_other_directory(self):
        for name in ('riff', 'godot-waikthrough', 'godot-walkthrough'):
            result = subprocess.run(['bash', str(ROOT / 'art'), name, '--help'],
                                    cwd='/tmp', capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('name: ', result.stdout)
            self.assertIn('regular', result.stdout)


if __name__ == '__main__':
    unittest.main()
