"""Offline regression tests. No Claude sessions, network requests, or real renders."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

REPO = Path(os.environ.get('REPOLOOP_TEST_REPO', Path(__file__).resolve().parents[1]))
SCRIPT = Path(os.environ.get('REPOLOOP_TEST_SCRIPT', REPO / 'runtime/scripts/repoloop.py'))
sys.path.insert(0, str(REPO / 'runtime/scripts'))
spec = importlib.util.spec_from_file_location('repoloop', SCRIPT)
loop = importlib.util.module_from_spec(spec)
spec.loader.exec_module(loop)


class RepoloopTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.inventory = [{'id': 'one', 'order': 1, 'slug': 'one', 'title': 'One',
                           'source_sha256': 'original', 'sources': [], 'aliases': [],
                           'kind': 'command', 'brief': 'Example'}]

    def tearDown(self):
        self.temp.cleanup()

    def test_intros_first_and_all_skills_discovered(self):
        items = loop.discover(REPO)
        self.assertEqual([i['id'] for i in items[:3]], [i[0] for i in loop.INTRO])
        actual = {i['sources'][0] for i in items if i['kind'] == 'skill'}
        expected = {str(p.relative_to(REPO)) for p in (REPO / 'skills').rglob('SKILL.md')}
        self.assertEqual(actual, expected)
        self.assertEqual(len({i['id'] for i in items}), len(items))

    def test_aliases_do_not_create_duplicate_films(self):
        items = {i['id']: i for i in loop.discover(REPO)}
        self.assertIn('scene-search', items['command-scenes']['aliases'])
        self.assertIn('--list', items['command-list']['aliases'])
        self.assertNotIn('command-scene-search', items)
        self.assertIn('command-vertical', items)
        self.assertIn('command-shorts', items)

    def test_runtime_utilities_covered(self):
        items = {i['id'] for i in loop.discover(REPO)}
        for key in ('runtime-generate-audio-kokoro', 'runtime-remotion-scenes',
                    'qc-final-frame-check', 'command-repoloop'):
            self.assertIn(key, items)

    def test_completed_survives_rescan(self):
        q = loop.merge_queue(None, self.inventory, self.root)
        q['items'][0].update(status='review_ready', outputs={'landscape': 'old.mp4'})
        new = loop.merge_queue(q, self.inventory, self.root)
        self.assertEqual(new['items'][0]['status'], 'review_ready')
        self.assertEqual(new['items'][0]['outputs'], {'landscape': 'old.mp4'})

    def test_shorts_discovery_is_independent_and_requires_verified_parent(self):
        parent = dict(self.inventory[0], status='review_ready', run_id='parent-run',
                      outputs={'landscape': 'preserved.mp4'})
        loop.atomic_json(self.root / '.repoloop/queue.json', {'items': [parent]})
        reel = self.root / 'youtube/brutalist/one'
        source = reel / 'vertical/beat_sheet.json'
        loop.atomic_json(source, {'beats': []})
        video = reel / 'exports/vertical/one-vertical.mp4'
        loop.atomic_text(video, 'synthetic master fixture')
        loop.atomic_json(video.with_suffix('.verified.json'), {'status': 'ready', 'sha256': loop.file_digest(video)})
        before = loop.file_digest(self.root / '.repoloop/queue.json')
        items = loop.discover_shorts(self.root)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['slug'], 'one-short')
        self.assertNotIn('outputs', items[0])
        self.assertNotIn('run_id', items[0])
        self.assertEqual(loop.file_digest(self.root / '.repoloop/queue.json'), before)
        q = loop.merge_queue(None, items, self.root / 'shorts')
        self.assertEqual(q['items'][0]['status'], 'pending')
        loop.atomic_text(video, 'changed outside receipt')
        self.assertEqual(loop.discover_shorts(self.root), [])

    def test_short_verifier_rejects_exact_180_before_visual_review(self):
        beats = [{'narration_text': 'Liam, in for Bear.', 'shot': {}} for _ in range(3)]
        loop.atomic_json(self.root / 'beat_sheet.json', {'metadata': {
            'kind': 'short', 'aspect_ratio': '9:16', 'playlist': 'Brutalist', 'voice': 'am_onyx'}, 'beats': beats})
        video = self.root / 'exports/short/one.mp4'
        loop.atomic_text(video, 'synthetic Short fixture')
        receipt = {'status': 'ready', 'sha256': loop.file_digest(video)}
        loop.atomic_json(video.with_suffix('.verified.json'), receipt)
        loop.atomic_json(self.root / 'build-state.json', receipt)
        probe = subprocess.CompletedProcess([], 0, json.dumps({'format': {'duration': '180'}, 'streams': [
            {'codec_type': 'video', 'width': 2160, 'height': 3840}, {'codec_type': 'audio'}]}), '')
        with patch.object(loop.subprocess, 'run', return_value=probe), \
             self.assertRaisesRegex(loop.BuildError, 'strictly under'):
            loop.verify_film(self.root, self.inventory[0], {'short': [2160, 3840]})

    def test_changed_source_requeues_without_discarding_render(self):
        q = loop.merge_queue(None, self.inventory, self.root)
        q['items'][0].update(status='review_ready', outputs={'landscape': 'old.mp4'})
        self.inventory[0]['source_sha256'] = 'changed'
        new = loop.merge_queue(q, self.inventory, self.root)
        self.assertEqual(new['items'][0]['status'], 'pending')
        self.assertEqual(new['items'][0]['outputs']['landscape'], 'old.mp4')

    def test_feedback_requeues(self):
        folder = self.root / 'one'; folder.mkdir()
        loop.atomic_text(folder / 'FEEDBACK.md', 'Initial')
        q = loop.merge_queue(None, self.inventory, self.root)
        q['items'][0]['status'] = 'review_ready'
        loop.atomic_text(folder / 'FEEDBACK.md', 'Please make the graph labels larger.')
        self.assertEqual(loop.merge_queue(q, self.inventory, self.root)['items'][0]['status'], 'pending')

    def test_removed_entry_retired_not_deleted(self):
        q = loop.merge_queue(None, self.inventory, self.root)
        self.assertEqual(loop.merge_queue(q, [], self.root)['items'][0]['status'], 'retired')

    def test_live_worker_not_reset_by_rescan(self):
        q = loop.merge_queue(None, self.inventory, self.root)
        q['items'][0]['status'] = 'building'
        self.inventory[0]['source_sha256'] = 'changed'
        self.assertEqual(loop.merge_queue(q, self.inventory, self.root)['items'][0]['status'], 'building')

    def test_lock_excludes_duplicate_worker_and_releases(self):
        path = self.root / 'worker.lock'
        with loop.exclusive_lock(path):
            self.assertTrue(loop.lock_held(path))
            with self.assertRaises(loop.BuildError):
                with loop.exclusive_lock(path):
                    pass
        self.assertFalse(loop.lock_held(path))

    def test_example_index_read_only_and_skips_derivatives(self):
        (self.root / 'fellow').mkdir()
        (self.root / 'fellow/vertical').mkdir()
        for path in (self.root / 'fellow/beat_sheet.json', self.root / 'fellow/vertical/beat_sheet.json'):
            loop.atomic_json(path, {'metadata': {'title': 'Source'}, 'beats': []})
        before = loop.file_digest(self.root / 'fellow/beat_sheet.json')
        examples = loop.example_index(self.root)
        self.assertEqual(len(examples), 1)
        self.assertEqual(before, loop.file_digest(self.root / 'fellow/beat_sheet.json'))

    def test_worker_has_no_api_fallback(self):
        with patch.dict(os.environ, {'ANTHROPIC_API_KEY': 'dummy', 'OPENAI_API_KEY': 'dummy',
                                    'CLAUDE_CODE_USE_BEDROCK': '1', 'ANTHROPIC_AUTH_TOKEN': 'dummy'}):
            env = loop.worker_environment(REPO)
        for key in ('ANTHROPIC_API_KEY', 'OPENAI_API_KEY', 'CLAUDE_CODE_USE_BEDROCK', 'ANTHROPIC_AUTH_TOKEN'):
            self.assertNotIn(key, env)

    def test_snapshot_recovers_partial_copy_and_skips_media_links(self):
        repo, workspace = self.root / 'repo', self.root / 'workspace'
        public = repo / 'runtime/remotion/public'
        public.mkdir(parents=True)
        (repo / 'runtime/remotion/node_modules').mkdir()
        (repo / 'runtime/remotion/src').mkdir()
        loop.atomic_text(public / 'font-note.txt', 'real shipped resource')
        (public / 'old-film-mp3').symlink_to(self.root / 'missing-audio')
        (workspace / 'toolkit').mkdir(parents=True)  # interrupted prior copy
        toolkit = loop.snapshot_toolkit(repo, workspace)
        self.assertTrue((workspace / 'toolkit-baseline.json').is_file())
        self.assertEqual((toolkit / 'runtime/remotion/public/font-note.txt').read_text(), 'real shipped resource')
        self.assertFalse((toolkit / 'runtime/remotion/public/old-film-mp3').is_symlink())
        self.assertTrue((toolkit / 'runtime/remotion/node_modules').is_symlink())
        loop.atomic_text(toolkit / 'runtime/remotion/src/new-scene.tsx', 'worker edit')
        loop.snapshot_toolkit(repo, workspace)
        self.assertEqual((toolkit / 'runtime/remotion/src/new-scene.tsx').read_text(), 'worker edit')

    def test_sandbox_is_fail_closed(self):
        settings = loop.worker_settings(REPO, self.root / 'work', self.root / 'film', self.root / 'fellows')
        self.assertTrue(settings['sandbox']['enabled'])
        self.assertTrue(settings['sandbox']['failIfUnavailable'])
        self.assertFalse(settings['sandbox']['allowUnsandboxedCommands'])
        self.assertEqual(settings['permissions']['defaultMode'], 'dontAsk')
        self.assertIn(str(REPO / 'runtime'), settings['sandbox']['filesystem']['denyWrite'])

    def test_rate_limit_recognized(self):
        self.assertTrue(loop.is_rate_limit("You've hit your limit · resets 3pm"))
        self.assertTrue(loop.is_rate_limit('rate limit exceeded'))
        self.assertFalse(loop.is_rate_limit('Rendering completed successfully'))

    def test_revoked_login_recognized(self):
        self.assertTrue(loop.is_auth_failure('API Error: 401 OAuth access token has been revoked.'))
        self.assertTrue(loop.is_auth_failure('"error":"authentication_failed"'))
        self.assertFalse(loop.is_auth_failure('Rendered and verified'))

    def test_error_result_even_with_zero_exit_not_success(self):
        path = self.root / 'worker.jsonl'
        loop.atomic_text(path, '{"type":"result","subtype":"success","is_error":true}\n')
        self.assertTrue(loop.worker_failed(path))
        loop.atomic_text(path, '{"type":"result","subtype":"success","is_error":false}\n')
        self.assertFalse(loop.worker_failed(path))
        loop.atomic_text(path, '{"type":"assistant"}\n')
        self.assertTrue(loop.worker_failed(path))

    def test_timeout_stops_owned_process(self):
        result = loop.run_process([sys.executable, '-c', 'import time; time.sleep(20)'], self.root,
                                  dict(os.environ), self.root / 'timeout.log', 0.1, self.root / 'STOP')
        self.assertEqual(result, 124)

    def test_stop_request_stops_owned_process(self):
        loop.atomic_text(self.root / 'STOP', 'stop')
        result = loop.run_process([sys.executable, '-c', 'import time; time.sleep(20)'], self.root,
                                  dict(os.environ), self.root / 'stop.log', 20, self.root / 'STOP')
        self.assertEqual(result, 130)

    def test_old_review_cannot_complete_new_attempt(self):
        beats = [{'engine': 'kokoro', 'voice': 'am_onyx', 'narration_text': 'Liam, in for Bear.',
                  'shot': {'remotion': {'pattern': name, 'props': {'greeting': 'Your Turn'}}}}
                 for name in ['ClaudeComposerAsk', 'BrutalistHesitantWriter', 'Demo', 'Demo',
                              'Demo', 'Demo', 'ClaudeComposerAsk', 'Outro']]
        loop.atomic_json(self.root / 'beat_sheet.json', {'metadata': {'playlist': 'Brutalist', 'voice': 'am_onyx'}, 'beats': beats})
        output = self.root / 'exports/landscape/one.mp4'; output.parent.mkdir(parents=True)
        loop.atomic_text(output, 'not a real video; subprocesses are mocked')
        sha = loop.file_digest(output)
        loop.atomic_json(output.with_suffix('.verified.json'), {'status': 'ready', 'sha256': sha})
        loop.atomic_json(self.root / 'build-state.json', {'status': 'ready', 'sha256': sha})
        loop.atomic_json(self.root / 'VISUAL-REVIEW.json', {'status': 'pass', 'reviewer_type': 'ai',
                        'video_sha256': sha, 'run_id': 'old', 'source_sha256': 'original'})
        probe = subprocess.CompletedProcess([], 0, json.dumps({'streams': [{'codec_type': 'video', 'width': 3840, 'height': 2160}, {'codec_type': 'audio'}]}), '')
        audio = subprocess.CompletedProcess([], 0, '', 'mean_volume: -20.0 dB')
        with patch.object(loop.subprocess, 'run', side_effect=[probe, audio]):
            with self.assertRaisesRegex(loop.BuildError, 'current AI frame-review'):
                loop.verify_film(self.root, dict(self.inventory[0], run_id='new'), {'landscape': [3840, 2160]})


if __name__ == '__main__':
    unittest.main()
