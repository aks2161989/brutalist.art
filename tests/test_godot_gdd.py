import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location('verify_gdd', Path(__file__).resolve().parents[1] / 'skills/make/godot-gdd/scripts/verify_gdd.py')
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class GddGate(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.doc = self.root / 'GDD.md'
        self.doc.write_text('# Game\n## Vision\nA readable jump.\n## Tests\nCheck it.\n')
        self.reel = self.root / 'reel'
        self.reel.mkdir()
        evidence = self.reel / 'record.json'
        evidence.write_text('{}')
        self.sheet = {'beats': [{'beat_id': 'B01', 'act': 'BODY', 'design_status': 'proposed', 'narration_text': 'Explain the rule.', 'shot': {'remotion': {'props': {'excerpt': 'A readable jump.'}}}}]}
        self.ledger = {'schema_version': 1, 'document': {'sha256': MODULE.digest(self.doc)}, 'sections': [{'heading': 'Vision', 'beat_ids': ['B01']}, {'heading': 'Tests', 'beat_ids': ['B01']}], 'excerpts': [{'beat_id': 'B01', 'start_line': 3, 'end_line': 3, 'text': 'A readable jump.'}], 'evidence': [{'path': 'record.json', 'sha256': MODULE.digest(evidence), 'method': 'fixture', 'supports': 'test only'}]}

    def run_check(self):
        (self.reel / 'beat_sheet.json').write_text(json.dumps(self.sheet))
        (self.reel / 'gdd-evidence.json').write_text(json.dumps(self.ledger))
        return MODULE.check(self.reel, self.doc)

    def test_valid(self):
        self.assertEqual(self.run_check()['sections'], 2)

    def test_hash(self):
        self.doc.write_text('changed')
        with self.assertRaises(ValueError): self.run_check()

    def test_missing_section(self):
        self.ledger['sections'].pop()
        with self.assertRaises(ValueError): self.run_check()

    def test_unknown_beat(self):
        self.ledger['sections'][0]['beat_ids'] = ['unknown']
        with self.assertRaises(ValueError): self.run_check()

    def test_changed_quote(self):
        self.ledger['excerpts'][0]['text'] = 'invented'
        with self.assertRaises(ValueError): self.run_check()

    def test_display_mismatch(self):
        self.sheet['beats'][0]['shot']['remotion']['props']['excerpt'] = 'invented'
        with self.assertRaises(ValueError): self.run_check()

    def test_missing_status(self):
        del self.sheet['beats'][0]['design_status']
        with self.assertRaises(ValueError): self.run_check()

    def test_escape(self):
        self.ledger['evidence'][0]['path'] = '../GDD.md'
        with self.assertRaises(ValueError): self.run_check()

    def test_symlink_escape(self):
        (self.reel / 'outside').symlink_to(self.doc)
        self.ledger['evidence'][0]['path'] = 'outside'
        with self.assertRaises(ValueError): self.run_check()

    def test_unreasoned_exclusion(self):
        self.ledger['sections'][0] = {'heading': 'Vision', 'exclusion': ''}
        with self.assertRaises(ValueError): self.run_check()


if __name__ == '__main__':
    unittest.main()
