"""Real FFmpeg seam regression plus fail-closed provenance tests."""
import copy
import json
from pathlib import Path
import tempfile
import unittest

from build_safety import BuildError, file_digest
from verified_body import run, probe, validate_reuse, make_concat, verify_samples


class ReuseTests(unittest.TestCase):
    def test_real_splice_and_refusals(self):
        with tempfile.TemporaryDirectory(prefix='verified-body-test-') as scratch:
            root = Path(scratch).resolve()
            old_video = root / 'old.mp4'
            first_clip = root / 'new-first.mp4'
            run(['ffmpeg', '-y', '-v', 'error', '-f', 'lavfi', '-i', 'testsrc2=s=320x180:r=24:d=5.5',
                 '-force_key_frames', '2.5', '-c:v', 'libx264', '-preset', 'slow', '-crf', '16', old_video])
            run(['ffmpeg', '-y', '-v', 'error', '-f', 'lavfi', '-i', 'color=white:s=320x180:r=24',
                 '-frames:v', '153', '-c:v', 'libx264', '-crf', '12', first_clip])
            body_input = root / 'body-source.txt'
            body_input.write_text('immutable body source fixture')
            body_hash = file_digest(body_input)
            old = {'metadata': {'title': 'Fixture', 'fps': 24, 'width': 320, 'height': 180},
                   'beats': [{'beat_id': 'BOPEN', 'actual_duration_s': 2.5,
                              'shot': {'template': 'lecture-title-slide-16x9'}},
                             {'beat_id': 'BIDEA', 'actual_duration_s': 3.0}]}
            sheet = copy.deepcopy(old)
            sheet['beats'][0]['actual_duration_s'] = 6.375
            config = {'master': 'old.mp4', 'sheet': 'old.json', 'receipt': 'old.verified.json'}
            sheet['metadata']['verified_body_reuse'] = config
            (root / 'old.json').write_text(json.dumps(old))
            receipt = {'status': 'ready', 'sha256': file_digest(old_video), 'duration_s': 5.5,
                       'input_sha256': {str(body_input): body_hash}}
            (root / 'old.verified.json').write_text(json.dumps(receipt))
            inputs = {str(body_input): body_hash}
            self.assertIsNone(validate_reuse(root, old, 24, 320, 180, inputs))
            record = validate_reuse(root, sheet, 24, 320, 180, inputs)
            self.assertEqual(inputs[str(old_video)], receipt['sha256'])
            def concat_line(path):
                return f"file '{path}'\n"
            playlist = make_concat(record, first_clip, 153, root, concat_line)
            candidate = root / 'candidate.mp4'
            run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', playlist,
                 '-c:v', 'copy', candidate])
            video = next(s for s in probe(candidate)['streams'] if s['codec_type'] == 'video')
            self.assertEqual(int(video['nb_frames']), 225)
            verify_samples(record, candidate)
            self.assertEqual(len(record['decoded_frame_checks']), 3)
            # A long MP4 certified by the normal gate may have one fewer video
            # frame than its audio clock. Copy every REAL body frame and keep
            # exact fractional-frame end times when muxing the replacement.
            short_clock = copy.deepcopy(old)
            short_clock['beats'][1]['actual_duration_s'] = 73 / 24
            (root / 'old.json').write_text(json.dumps(short_clock))
            short_receipt = copy.deepcopy(receipt)
            short_receipt['duration_s'] = 133 / 24
            (root / 'old.verified.json').write_text(json.dumps(short_receipt))
            long_first = root / 'long-first.mp4'
            run(['ffmpeg', '-y', '-v', 'error', '-f', 'lavfi', '-i', 'color=white:s=320x180:r=24',
                 '-frames:v', '197', '-c:v', 'libx264', '-crf', '12', long_first])
            replacement = copy.deepcopy(sheet)
            replacement['beats'][1]['actual_duration_s'] = 73 / 24
            replacement['beats'][0]['actual_duration_s'] = 197 / 24
            new_record = validate_reuse(root, replacement, 24, 320, 180, {str(body_input): body_hash})
            self.assertEqual((new_record['body_frames'], new_record['timeline_body_frames']), (72, 73))
            new_list = make_concat(new_record, long_first, 197, root, concat_line)
            muxed = root / 'muxed.mp4'
            run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', new_list,
                 '-f', 'lavfi', '-i', 'sine=frequency=440:sample_rate=48000',
                 '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac',
                 '-frames:v', '269', '-t', f'{270/24:.9f}', muxed])
            self.assertEqual(int(probe(muxed)['streams'][0]['nb_frames']), 269)
            verify_samples(new_record, muxed)
            (root / 'old.json').write_text(json.dumps(old))
            (root / 'old.verified.json').write_text(json.dumps(receipt))
            for modification in ('body', 'title', 'source', 'receipt', 'escape', 'not-keyframe'):
                current = copy.deepcopy(sheet)
                current_inputs = {str(body_input): body_hash}
                bad_receipt = copy.deepcopy(receipt)
                if modification == 'body':
                    current['beats'][1]['actual_duration_s'] = 2.0
                elif modification == 'title':
                    current['metadata']['title'] = 'Changed'
                elif modification == 'source':
                    current_inputs[str(body_input)] = 'wrong hash'
                elif modification == 'receipt':
                    bad_receipt['sha256'] = 'wrong hash'
                elif modification == 'escape':
                    current['metadata']['verified_body_reuse']['master'] = '../outside.mp4'
                else:
                    changed_old = copy.deepcopy(old)
                    changed_old['beats'][0]['actual_duration_s'] = 2.0
                    (root / 'old.json').write_text(json.dumps(changed_old))
                (root / 'old.verified.json').write_text(json.dumps(bad_receipt))
                with self.subTest(modification=modification), self.assertRaises(BuildError):
                    validate_reuse(root, current, 24, 320, 180, current_inputs)
                (root / 'old.json').write_text(json.dumps(old))
                (root / 'old.verified.json').write_text(json.dumps(receipt))


if __name__ == '__main__':
    unittest.main()
