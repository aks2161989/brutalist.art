import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/make/godot-gamedev/scripts/verify_gamedev.py'
spec = importlib.util.spec_from_file_location('gamedev', SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class GamedevEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.game = self.root / 'game'
        self.reel = self.root / 'reel'
        self.game.mkdir(); self.reel.mkdir()
        self.source = 'config_version=5\n'
        (self.game / 'project.godot').write_text(self.source)
        self.sheet = {'beats': [{'beat_id': 'B01', 'narration_text': 'This sets the file format.',
                     'shot': {'remotion': {'pattern': 'GodotDevWorkbench', 'props': {'code': 'config_version=5'}}}}]}
        self.data = {'schema_version': 1, 'files': [{'path': 'project.godot', 'role': 'config',
            'sha256': hashlib.sha256(self.source.encode()).hexdigest(), 'component_ids': ['config']}],
            'components': [{'id': 'config', 'explanation': 'Project format version',
                            'files': ['project.godot'], 'beat_ids': ['B01']}],
            'excerpts': [{'beat_id': 'B01', 'path': 'project.godot', 'start_line': 1, 'end_line': 1,
                          'text': 'config_version=5'}], 'exclusions': []}

    def run_check(self):
        (self.reel / 'beat_sheet.json').write_text(json.dumps(self.sheet))
        (self.reel / 'gamedev-evidence.json').write_text(json.dumps(self.data))
        return mod.verify(self.reel, self.game)

    def test_valid(self):
        self.assertEqual(self.run_check()['status'], 'PASS')

    def add_pair(self):
        # Hash checks only; this fixture is not a real render or visual approval.
        payload = b'test-only media bytes'
        (self.reel / 'result.png').write_bytes(payload)
        self.sheet['beats'].append({'beat_id': 'B02', 'narration_text': 'The engine reads this format.',
                                    'shot': {'evidence_media': 'result.png'}})
        self.data['teaching_contract'] = 'code-then-result-v1'
        self.data['code_result_pairs'] = [{'code_beat': 'B01', 'result_beat': 'B02',
            'observation': 'Test fixture only', 'media': {'path': 'result.png',
                'sha256': hashlib.sha256(payload).hexdigest()}}]

    def test_paired_result(self):
        self.add_pair()
        self.assertEqual(self.run_check()['code_result_pairs'], 1)

    def test_result_not_adjacent(self):
        self.add_pair()
        self.sheet['beats'].insert(1, {'beat_id': 'gap', 'narration_text': 'Other detail'})
        with self.assertRaisesRegex(ValueError, 'immediately follow'): self.run_check()

    def test_changed_result_media(self):
        self.add_pair()
        (self.reel / 'result.png').write_bytes(b'stale')
        with self.assertRaisesRegex(ValueError, 'media hash mismatch'): self.run_check()

    def test_unlinked_result_media(self):
        self.add_pair()
        self.sheet['beats'][1]['shot']['evidence_media'] = 'unrelated.png'
        with self.assertRaisesRegex(ValueError, 'does not reference'): self.run_check()

    def test_missing_pair(self):
        self.add_pair()
        self.data['code_result_pairs'] = []
        with self.assertRaisesRegex(ValueError, 'one visible result'): self.run_check()

    def test_changed_source(self):
        (self.game / 'project.godot').write_text('changed')
        with self.assertRaises(ValueError): self.run_check()

    def test_invented_excerpt(self):
        self.data['excerpts'][0]['text'] = 'invented'
        with self.assertRaises(ValueError): self.run_check()

    def test_display_mismatch(self):
        self.sheet['beats'][0]['shot']['remotion']['props']['code'] = 'changed'
        with self.assertRaises(ValueError): self.run_check()

    def test_missing_source_coverage(self):
        (self.game / 'player.gd').write_text('extends Node2D')
        with self.assertRaises(ValueError): self.run_check()

    def test_import_settings_are_source(self):
        (self.game / 'sprite.png.import').write_text('[params]\nfilter=true')
        with self.assertRaises(ValueError): self.run_check()

    def test_missing_component_beat(self):
        self.data['components'][0]['beat_ids'] = ['absent']
        with self.assertRaises(ValueError): self.run_check()

    def test_symlink_escape(self):
        external = self.root / 'outside.gd'
        external.write_text('extends Node2D')
        (self.game / 'escape.gd').symlink_to(external)
        self.data['exclusions'].append({'path': 'escape.gd', 'reason': 'Excluded'})
        with self.assertRaises(ValueError): self.run_check()

    def test_unrecorded_code(self):
        extra = copy.deepcopy(self.sheet['beats'][0]); extra['beat_id'] = 'B02'
        self.sheet['beats'].append(extra)
        with self.assertRaises(ValueError): self.run_check()

    def test_cli_from_another_directory(self):
        self.run_check()
        art = SCRIPT.parents[4] / 'art'
        result = subprocess.run([str(art), 'godot-gamedev', '--check', str(self.reel), '--game', str(self.game)],
                                cwd=self.root, capture_output=True, text=True, timeout=15)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['status'], 'PASS')

    def test_skill_help_discovery(self):
        art = SCRIPT.parents[4] / 'art'
        result = subprocess.run([str(art), 'godot-gamedev', '--help'], cwd=self.root,
                                env={**os.environ, 'PAGER': 'cat'}, capture_output=True, text=True, timeout=15)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('name: godot-gamedev', result.stdout)

if __name__ == '__main__': unittest.main()
