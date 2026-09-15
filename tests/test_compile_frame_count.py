"""A source-clock film must not gain a frame from decimal -t rounding."""
import json
import unittest
from test_pipeline_safety import FixtureCase, compiler, execute


class FrameClockTests(FixtureCase):
    def test_fractional_second_beats_have_exact_frame_count(self):
        media = self.reel / 'media'
        media.mkdir()
        work = self.reel / 'work'
        work.mkdir()
        for frames in (49, 601):
            with self.subTest(frames=frames):
                source = media / 'B01.mp4'
                r = execute(['ffmpeg', '-y', '-v', 'error', '-f', 'lavfi', '-i',
                             'testsrc2=size=64x96:rate=24', '-frames:v', frames,
                             '-c:v', 'libx264', source])
                self.assertEqual(r.returncode, 0, r.stderr)
                beat = dict(beat_id='B01', actual_duration_s=frames / 24,
                            render_duration_s=frames / 24,
                            shot=dict(type='VIDEO', source='own', treatment='none'))
                output = self.reel / f'out-{frames}.mp4'
                compiler.compile_clip(self.reel, beat, output, 64, 96, 24, None, work)
                r = execute(['ffprobe', '-v', 'error', '-count_frames',
                             '-show_entries', 'stream=nb_read_frames', '-of', 'json', output])
                self.assertEqual(r.returncode, 0, r.stderr)
                self.assertEqual(int(json.loads(r.stdout)['streams'][0]['nb_read_frames']), frames)


if __name__ == '__main__':
    unittest.main()
