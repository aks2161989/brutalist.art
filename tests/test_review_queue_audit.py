import importlib.util
from pathlib import Path
import sys
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / 'runtime/scripts'
sys.path.insert(0, str(SCRIPTS))
from audit_review_queue import inventory
from math_layout_check import math_layout_errors


class QueueAuditTests(unittest.TestCase):
    def test_inventory_ignores_commands_and_review_prompts(self):
        text = '''26 to review
   1. 2.0MB 6b [STALE] book/youtube/reel-a
   2. 3.0MB 8b book/youtube/reel-b
[1/26] reel-a.mp4
  /absolute/path/book/youtube/reel-a
  APPROVED -> 4K + YouTube
'''
        self.assertEqual(inventory(text), [(1,'book/youtube/reel-a'),(2,'book/youtube/reel-b')])

    def test_code_math_not_confused_with_explanation(self):
        beat = {'beat_id':'B1','shot':{'remotion':{'pattern':'ClaudeCodeBeat',
                'props':{'code':'math.exp((z_i-m)/T)'}}}}
        self.assertEqual(math_layout_errors({'beats':[beat]}), [])


if __name__ == '__main__':
    unittest.main()
