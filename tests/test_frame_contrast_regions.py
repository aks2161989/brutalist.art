"""Regional contrast must test readable content, never silently waive QC."""
import importlib.util
from pathlib import Path
import unittest
import numpy as np

spec = importlib.util.spec_from_file_location('frame_gate', Path(__file__).resolve().parents[1] / 'runtime/qc/final_frame_check.py')
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

class RegionalContrastTests(unittest.TestCase):
    region = [{'label': 'fixture text', 'box': [0, 0, 1, 1]}]

    def test_dark_text_on_light_card(self):
        frame = np.full((100, 200, 3), 245, dtype=np.uint8)
        frame[30:70, 40:160] = 30
        self.assertEqual(gate.contrast_regions(frame, self.region), [])

    def test_low_contrast_still_fails(self):
        frame = np.full((100, 200, 3), 245, dtype=np.uint8)
        frame[30:70, 40:160] = 200
        self.assertEqual(gate.contrast_regions(frame, self.region)[0][1], 'low-contrast')

    def test_empty_region_fails(self):
        frame = np.full((100, 200, 3), 245, dtype=np.uint8)
        self.assertEqual(gate.contrast_regions(frame, self.region)[0][1], 'empty-contrast-region')

    def test_bad_and_tiny_boxes_fail_closed(self):
        frame = np.full((100, 200, 3), 245, dtype=np.uint8)
        for regions in ([], [{'label': 'x', 'box': [-1, 0, 1, 1]}],
                        [{'label': 'x', 'box': [0, 0, .01, .01]}],
                        [{'label': 'x', 'box': [0, 0, float('nan'), 1]}]):
            with self.assertRaises(gate.BuildError):
                gate.contrast_regions(frame, regions)

if __name__ == '__main__':
    unittest.main()
