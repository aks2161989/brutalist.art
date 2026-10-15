"""Gate W must analyse every beat-scene name and never skip a Scene class silently."""
import contextlib
import importlib.util
import io
import sys
import tempfile
import unittest
import warnings
from pathlib import Path
from unittest import mock

spec = importlib.util.spec_from_file_location('gate_w', Path(__file__).resolve().parents[1] / 'runtime/qc/wcag_margin_check.py')
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


def scene(name, base='Scene'):
    # GOLD text is a W1 ERROR, so an analysed class shows up as a finding, not just "clean"
    return f'class {name}({base}):\n    def construct(self):\n        t = Text("x", color=GOLD)\n\n'


def run(source, *args):
    """gate.main() on `source` -> (exit code, stdout lines)."""
    with tempfile.TemporaryDirectory() as d:
        path = Path(d) / 'scenes.py'
        path.write_text(source, encoding='utf-8')
        out = io.StringIO()
        with mock.patch.object(sys, 'argv', ['wcag_margin_check.py', str(path), *args]), \
                contextlib.redirect_stdout(out), warnings.catch_warnings():
            warnings.simplefilter('ignore', ResourceWarning)  # main() leaves its source handle to the GC
            rc = gate.main()
    return rc, out.getvalue().splitlines()


def analysed(lines):
    """Class names with a `[gateW] <Name> ...` result line (the NOTICE line is not one)."""
    return {l.split()[1] for l in lines if l.startswith('[gateW] ') and l.split()[1] != 'NOTICE'}


def notices(lines):
    return [l for l in lines if l.startswith('[gateW] NOTICE')]


class SceneSelectionTests(unittest.TestCase):
    source = scene('B18A_X') + scene('B181_X') + scene('B05b_X') + scene('Helper_X')

    def test_letter_suffix_and_plain_digit_names_are_analysed(self):
        rc, lines = run(self.source)
        self.assertEqual(analysed(lines), {'B18A_X', 'B181_X', 'B05b_X'})
        self.assertEqual(rc, 2)
        self.assertTrue(any(l.startswith('[gateW] B18A_X ERROR W1') for l in lines))

    def test_other_names_are_not_analysed_but_are_reported(self):
        _, lines = run(self.source)
        self.assertNotIn('Helper_X', analysed(lines))
        (notice,) = notices(lines)
        self.assertTrue(notice.endswith(': Helper_X'))

    def test_notice_follows_same_file_bases_and_ignores_non_scenes(self):
        source = (scene('Base') + scene('Foo_X', 'Base') + scene('B01_X')
                  + 'class Palette:\n    pass\n\nclass Util_Y(dict):\n    pass\n')
        _, lines = run(source)
        (notice,) = notices(lines)
        self.assertTrue(notice.endswith(': Base, Foo_X'))

    def test_quiet_still_prints_the_notice(self):
        _, lines = run(self.source, '--quiet')
        self.assertEqual(len(notices(lines)), 1)

    def test_no_notice_when_nothing_is_skipped(self):
        _, lines = run(scene('B01_X') + scene('B18A_X'))
        self.assertEqual(notices(lines), [])

    def test_class_filter(self):
        _, lines = run(self.source, '--class', 'B18A_X')
        self.assertEqual(analysed(lines), {'B18A_X'})
        self.assertEqual(notices(lines), [])  # Helper_X was not asked for
        rc, lines = run(self.source, '--class', 'Helper_X')  # the run.sh case: asked for, skipped
        self.assertEqual((rc, analysed(lines)), (0, set()))
        (notice,) = notices(lines)
        self.assertTrue(notice.endswith(': Helper_X'))


if __name__ == '__main__':
    unittest.main()
