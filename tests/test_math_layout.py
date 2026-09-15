import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'runtime' / 'scripts'))
from math_layout_check import math_layout_errors
from typeset_math import typeset


def sheet(pattern, text):
    return {'beats': [{'beat_id': 'B32', 'shot': {'remotion': {
        'pattern': pattern, 'props': {'lines': [text]}}}}]}


class MathLayoutTests(unittest.TestCase):
    def test_rejects_reported_defect(self):
        self.assertTrue(math_layout_errors(sheet('FormACard', 'exp((z − m)/T) ÷ Σ exp((z − m)/T)')))

    def test_rejects_raw_tex_and_flat_indices(self):
        for text in [r'\frac{a}{b}', 'p(i) / p(k) = exp(x)', 'z_i = 2']:
            self.assertTrue(math_layout_errors(sheet('WantQuote916', text)))

    def test_preserves_code_and_plain_arithmetic(self):
        self.assertFalse(math_layout_errors(sheet('ClaudeCodeBeat', 'p(i) / p(k) = exp(x)')))
        self.assertFalse(math_layout_errors(sheet('FormACard', '2 + 2 = 4')))
        self.assertFalse(math_layout_errors(sheet('FormACard', 'Approval ≠ correctness.')))

    def test_typesetting_produces_svg_paths(self):
        import base64
        rendered = typeset(r'\frac{p_i}{p_k}=\exp\left(\frac{z_i-z_k}{T}\right)')
        self.assertGreater(rendered['aspect'], 0)
        self.assertIn(b'<path', base64.b64decode(rendered['src'].split(',')[1]))

    def test_invalid_math_has_no_text_fallback(self):
        with self.assertRaises(ValueError):
            typeset(r'\notarealcommand{x}')


if __name__ == '__main__':
    unittest.main()
