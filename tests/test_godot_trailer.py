"""Real-media probes plus failure cases for the godot-trailer gate and beat grid.

Fixtures are synthetic test patterns, never presented as gameplay."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
import wave

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / 'skills/make/godot-trailer/scripts'


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


gate = load('trailer_gate', 'verify_trailer.py')
grid = load('trailer_grid', 'beat_grid.py')
asm = load('trailer_asm', 'assemble_trailer.py')
vok = load('trailer_vo', 'vo_kokoro.py')
BUILD = 'a' * 64


def ffmpeg(*args):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', *args], check=True, timeout=120)


def gameplay(sid, role, capture, a, b, **extra):
    shot = {'id': sid, 'role': role, 'kind': 'gameplay', 'capture': capture, 'in_s': a, 'out_s': b,
            'screen': 'gameplay', 'feature': 'jump', 'verb': 'jump',
            'situation': 'a gap', 'action': 'jump pressed', 'consequence': 'lands on the ledge',
            'new_information': 'mechanic', 'intensity': 1, 'camera': 'player',
            'hud': 'kept', 'debug_overlay': False}
    shot.update(extra)
    return shot


@unittest.skipUnless(shutil.which('ffmpeg') and shutil.which('ffprobe'), 'requires ffmpeg/ffprobe')
class TrailerGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix='godot-trailer-test-')
        cls.root = Path(cls.temp.name)
        (cls.root / 'capture').mkdir()
        # test pattern, 40 s; and one that fades in from black
        ffmpeg('-f', 'lavfi', '-i', 'testsrc2=size=640x360:rate=30:duration=40',
               '-f', 'lavfi', '-i', 'sine=frequency=220:duration=40', '-shortest',
               '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-c:a', 'aac', str(cls.root / 'capture/take.mp4'))
        ffmpeg('-f', 'lavfi', '-i', 'testsrc2=size=640x360:rate=30:duration=10',
               '-vf', 'fade=t=in:st=0:d=2', '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
               str(cls.root / 'capture/black.mp4'))
        for name in ('take', 'black'):
            (cls.root / f'capture/{name}-inputs.jsonl').write_text('{"test_fixture":true}\n')
        (cls.root / 'godot').mkdir()
        (cls.root / 'godot/export_presets.cfg').write_text('[preset.0]\nplatform="macOS"\n[preset.1]\nplatform="Windows Desktop"\n')

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def cap(self, name):
        path = self.root / f'capture/{name}.mp4'
        return {'path': f'capture/{name}.mp4', 'sha256': gate.sha256(path), 'build_id': BUILD,
                'method': 'scripted-input', 'input_log': f'capture/{name}-inputs.jsonl',
                'state_setup': 'Fixture; not gameplay',
                'integrity': {'teleport': False, 'invincible': False, 'collisions_disabled': False,
                              'spawned_content': False, 'time_scale': 1.0}}

    def base(self):
        end = {'kind': 'endcard', 'title': 'Test Game', 'platforms': ['macOS', 'Windows'],
               'availability': 'Playable prototype', 'directive': 'Download on GitHub'}
        return {
            'schema_version': 1,
            'game': {'name': 'fixture', 'build_id': BUILD, 'engine': 'Godot 4', 'build_status': 'prototype'},
            'type': 'store',
            'brief': {'audience': 'platformer fans', 'goal': 'play', 'genre': '2D platformer',
                      'hook': 'You jump gaps to reach the flag.', 'idea': 'bigger gaps', 'tone': 'brisk',
                      'verbs': [{'id': 'jump', 'input': 'Space', 'result': 'arcs over a gap'}],
                      'answers': {'what_is_this': 'a platformer', 'what_do_i_do': 'jump',
                                  'why_care': 'precise gaps'}},
            'features': [{'id': 'jump', 'status': 'implemented'},
                         {'id': 'checkpoints', 'status': 'planned', 'reason': 'not built'}],
            'cuts': [],
            'captures': {'take': self.cap('take'), 'black': self.cap('black')},
            'music': {'source': 'none'},
            'shots': [
                gameplay('S01', 'hook', 'take', 0.0, 2.0, shows_hook=True, establishes_genre=True),
                gameplay('S02', 'establish', 'take', 2.0, 6.0, intensity=1),
                gameplay('S03', 'escalate', 'take', 6.0, 12.0, intensity=2),
                gameplay('S04', 'escalate', 'take', 12.0, 18.0, intensity=3),
                gameplay('S05', 'escalate', 'take', 18.0, 24.0, intensity=4),
                gameplay('S06', 'peak', 'take', 24.0, 28.0, intensity=5),
                {'id': 'S07', 'role': 'cta', 'kind': 'card', 'duration_s': 4.5,
                 'card': {'pattern': 'GameTrailerCard', 'props': end}}],
            'cta': {'title': 'Test Game', 'platforms': ['macOS', 'Windows'],
                    'availability': 'Playable prototype', 'directive': 'Download on GitHub',
                    'sources': {'platforms': {'source': 'export_presets.cfg', 'ref': 'godot/export_presets.cfg'},
                                'availability': {'source': 'README', 'ref': 'README.md'},
                                'directive': {'source': 'git-remote', 'ref': 'origin'}}},
            'checks': {},
        }

    def run_gate(self, data, **kw):
        (self.root / 'trailer.json').write_text(json.dumps(data))
        return gate.verify(self.root, min_height=360, game_dir=self.root, **kw)

    def assertFails(self, data, text, **kw):
        report = self.run_gate(data, **kw)
        self.assertEqual(report['status'], 'FAIL', report)
        self.assertTrue(any(text in f for f in report['fails']), (text, report['fails']))

    def test_valid_trailer_passes_with_only_pending_warnings(self):
        report = self.run_gate(self.base())
        self.assertEqual(report['fails'], [], report['fails'])
        self.assertEqual(report['status'], 'PASS')
        self.assertAlmostEqual(report['runtime_s'], 32.5, places=2)
        self.assertTrue(any('viewer test pending' in w for w in report['warnings']))

    def test_viewer_test_pending_blocks_a_final_handoff(self):
        self.assertFails(self.base(), 'viewer test pending', require_viewer_test=True)

    def test_planned_feature_on_screen_fails(self):
        d = self.base(); d['shots'][2]['feature'] = 'checkpoints'
        self.assertFails(d, 'planned, not built')

    def test_must_open_on_the_hook_with_gameplay(self):
        d = self.base(); d['shots'][0]['role'] = 'establish'
        self.assertFails(d, 'open on the hook')

    def test_a_card_in_the_first_five_seconds_fails(self):
        d = self.base()
        d['shots'].insert(1, {'id': 'S1b', 'role': 'hook', 'kind': 'card', 'duration_s': 1.0,
                              'card': {'pattern': 'GameTrailerCard', 'props': {'kind': 'title', 'title': 'x'}}})
        self.assertFails(d, 'no card in the first 5 s')

    def test_black_first_frame_fails(self):
        d = self.base(); d['shots'][0].update(capture='black', in_s=0.0, out_s=2.0)
        self.assertFails(d, 'nearly black')

    def test_adjective_claims_fail(self):
        d = self.base(); d['shots'][1]['text'] = 'An epic adventure'
        self.assertFails(d, 'adjective claim "epic"')

    def test_text_is_budgeted(self):
        d = self.base(); d['shots'][1]['text'] = 'one two three four five six seven eight nine'
        self.assertFails(d, 'text is a tax')

    def test_capture_hash_and_build_must_match(self):
        d = self.base(); d['captures']['take']['sha256'] = 'b' * 64
        self.assertFails(d, 'hash mismatch')
        d = self.base(); d['captures']['take']['build_id'] = 'c' * 64
        self.assertFails(d, 'different game build')

    def test_footage_below_native_4k_fails_by_default(self):
        (self.root / 'trailer.json').write_text(json.dumps(self.base()))
        report = gate.verify(self.root, min_height=2160, game_dir=self.root)
        self.assertTrue(any('below native 16:9 2160p' in f for f in report['fails']))

    def test_cheats_must_be_explicitly_absent(self):
        d = self.base(); d['captures']['take']['integrity']['teleport'] = True
        self.assertFails(d, 'integrity.teleport')
        d = self.base(); d['captures']['take']['integrity']['time_scale'] = 0.5
        self.assertFails(d, 'time_scale')
        d = self.base(); del d['captures']['take']['integrity']
        self.assertFails(d, 'integrity attestation missing')

    def test_every_core_verb_must_be_shown(self):
        d = self.base(); d['brief']['verbs'].append({'id': 'shoot', 'input': 'F', 'result': 'fires'})
        self.assertFails(d, '"shoot" is a core verb but never shown')

    def test_a_shot_that_reshows_footage_fails(self):
        d = self.base(); d['shots'][3].update(in_s=6.5, out_s=11.5)
        self.assertFails(d, 'reuses source')

    def test_intensity_must_not_fall_without_contrast(self):
        d = self.base(); d['shots'][3]['intensity'] = 1
        self.assertFails(d, 'intensity falls')
        d['shots'][3]['contrast'] = True
        self.assertNotIn('intensity falls', ' '.join(self.run_gate(d)['fails']))

    def test_legibility_floor_for_establish_shots(self):
        d = self.base(); d['shots'][1].update(in_s=2.0, out_s=3.0)
        self.assertFails(d, 'legibility floor')

    def test_new_information_required(self):
        d = self.base(); d['shots'][2]['new_information'] = 'none'
        self.assertFails(d, 'shows nothing new')

    def test_non_player_camera_needs_disclosure_and_never_the_hook(self):
        d = self.base(); d['shots'][0]['camera'] = 'debug'
        self.assertFails(d, 'needs a disclosure')
        d['shots'][0]['disclosure'] = 'free camera'
        self.assertFails(d, 'hook and peak use the player camera')

    def test_hud_and_overlay_must_be_declared(self):
        d = self.base(); d['shots'][2]['hud'] = 'hidden'
        self.assertFails(d, 'hidden HUD needs a reason')
        d = self.base(); d['shots'][2]['debug_overlay'] = True
        self.assertFails(d, 'debug_overlay must be explicitly false')

    def test_end_card_must_be_last_one_action_and_sourced(self):
        d = self.base(); d['cta']['directive'] = 'Wishlist on Steam and follow us'
        self.assertFails(d, 'one directive, one action')
        d = self.base(); d['cta']['availability'] = 'Out now'
        self.assertFails(d, 'must say "prototype"')
        d = self.base(); d['cta']['platforms'] = ['PlayStation']
        d['shots'][-1]['card']['props']['platforms'] = ['PlayStation']
        self.assertFails(d, 'not in export_presets.cfg')
        d = self.base(); d['cta']['sources'].pop('directive')
        self.assertFails(d, 'directive needs source')
        d = self.base(); d['shots'][-1]['card']['props']['directive'] = 'Something else'
        self.assertFails(d, 'differs from the cta block')
        d = self.base(); d['shots'][-1]['duration_s'] = 1.5
        self.assertFails(d, 'hold the end card')
        d = self.base(); d['cta']['address'] = 'github.com/example/game'
        self.assertFails(d, 'address differs')
        d['shots'][-1]['card']['props']['address'] = 'github.com/example/game'
        self.assertFails(d, 'address needs source')
        d['cta']['sources']['address'] = {'source': 'git-remote', 'ref': 'origin'}
        self.assertEqual(self.run_gate(d)['fails'], [])
        d['cta']['directive'] = 'Download at example.com'
        d['shots'][-1]['card']['props']['directive'] = 'Download at example.com'
        self.assertFails(d, 'at most one address')

    def test_roles_must_follow_the_structure(self):
        d = self.base(); d['shots'][1]['role'] = 'peak'
        self.assertFails(d, 'roles out of order')
        d = self.base(); d['shots'] = [s for s in d['shots'] if s['role'] != 'peak']
        self.assertFails(d, 'missing a peak shot')

    def test_music_needs_provenance_and_cuts_on_the_beat(self):
        d = self.base()
        wav = self.root / 'track.wav'
        with wave.open(str(wav), 'wb') as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(8000)
            w.writeframes((np.zeros(8000 * 40, dtype=np.int16)).tobytes())
        beats = self.root / 'beats.json'
        # cuts fall at 2,6,12,18,24,28 — a 1-second grid contains all of them
        beats.write_text(json.dumps({'beats': [float(i) for i in range(40)]}))
        d['music'] = {'source': 'supplied', 'path': 'track.wav', 'sha256': gate.sha256(wav),
                      'provenance': 'test tone', 'tone_note': 'fixture', 'rhythm': 'metered',
                      'beats': 'beats.json'}
        report = self.run_gate(d)
        self.assertEqual(report['fails'], [], report['fails'])
        beats.write_text(json.dumps({'beats': [i + 0.5 for i in range(40)]}))   # grid off by half a beat
        self.assertFails(d, 'cuts land on a beat')
        d['music']['provenance'] = ''
        self.assertFails(d, 'provenance')

    def test_generated_music_must_ship_its_generator_and_say_trailer_only(self):
        d = self.base()
        wav = self.root / 'gen.wav'
        with wave.open(str(wav), 'wb') as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(8000)
            w.writeframes((np.zeros(8000 * 40, dtype=np.int16)).tobytes())
        gen = self.root / 'gen.py'
        gen.write_text('# fixture generator\n')
        d['music'] = {'source': 'generated', 'path': 'gen.wav', 'sha256': gate.sha256(wav),
                      'provenance': 'made by gen.py', 'tone_note': 'fixture', 'rhythm': 'free'}
        self.assertFails(d, 'needs its generator script')
        d['music'].update(generator='gen.py', generator_sha256='0' * 64, trailer_only=True)
        self.assertFails(d, 'generator script changed')
        d['music'].update(generator_sha256=gate.sha256(gen), trailer_only=False)
        self.assertFails(d, 'trailer_only')
        d['music']['trailer_only'] = True
        self.assertEqual(self.run_gate(d)['fails'], [])

    def test_presentation_block_is_validated(self):
        d = self.base()
        good = {'inset': 0.9, 'pad_color': '#F6F3EB',
                'contrast_regions': [{'label': 'HUD', 'box': [0.07, 0.07, 0.85, 0.2]}],
                'contrast_reason': 'fixture'}
        d['presentation'] = good
        self.assertEqual(self.run_gate(d)['fails'], [])
        d['presentation'] = dict(good, inset=1.2)
        self.assertFails(d, 'inset must be')
        d['presentation'] = dict(good, pad_color='cream')
        self.assertFails(d, 'pad_color')
        d['presentation'] = dict(good, contrast_regions=[{'label': 'HUD', 'box': [0.5, 0.1, 0.2, 0.9]}])
        self.assertFails(d, 'normalised')

    def make_vo(self, lines, seconds=1.2):
        """Synthetic voice files (a tone, never presented as speech) plus the manifest vo_kokoro would write."""
        out = self.root / 'audio/vo'
        out.mkdir(parents=True, exist_ok=True)
        manifest = {}
        for line in lines:
            wav = out / f'{line["id"]}.wav'
            with wave.open(str(wav), 'wb') as w:
                w.setnchannels(1); w.setsampwidth(2); w.setframerate(24000)
                t = np.arange(int(24000 * seconds)) / 24000
                w.writeframes((0.4 * 32767 * np.sin(2 * np.pi * 180 * t)).astype('<i2').tobytes())
            manifest[line['id']] = {'text': line['text'], 'text_sha256': __import__('hashlib').sha256(line['text'].strip().encode()).hexdigest(),
                                    'voice': 'am_onyx', 'wav': f'audio/vo/{line["id"]}.wav',
                                    'wav_sha256': gate.sha256(wav), 'duration_s': gate.probe(wav)['duration_s']}
        (out / 'manifest.json').write_text(json.dumps(manifest))

    def vo_base(self):
        d = self.base()
        d['vo'] = {'engine': 'kokoro', 'voice': 'am_onyx', 'persona': 'liam', 'lines': [
            {'id': 'V01', 'shot': 'S01', 'at_s': 0.3, 'text': 'One jump. Read the landing.',
             'on_screen_equivalent': 'single jumps and the HUD "Space: jump"'},
            {'id': 'V02', 'shot': 'S03', 'at_s': 0.4, 'text': 'Bump a block.',
             'on_screen_equivalent': '+1 TOKEN popup'}]}
        self.make_vo(d['vo']['lines'])
        return d

    def test_voiceover_passes_when_sparse_generated_and_equivalent_on_screen(self):
        self.assertEqual(self.run_gate(self.vo_base())['fails'], [])

    def test_voiceover_rules(self):
        d = self.vo_base(); d['vo']['lines'][0]['text'] = 'Hello, this is Liam, in for Bear.'
        self.make_vo(d['vo']['lines'])
        self.assertFails(d, 'opens on gameplay, not an introduction')
        d = self.vo_base(); d['vo']['lines'][1]['text'] = 'Bump an epic block.'
        self.assertFails(d, 'text changed after the audio')
        self.make_vo(d['vo']['lines'])
        self.assertFails(d, 'adjective claim "epic"')
        d = self.vo_base(); d['vo']['lines'][1]['on_screen_equivalent'] = ''
        self.assertFails(d, 'sound off')
        d = self.vo_base(); d['vo']['lines'][1].update(shot='S01', at_s=1.0)          # abs 1.0 s: overlaps V01 (0.3-1.5)
        self.assertFails(d, 'leave air between lines')
        d = self.vo_base(); d['vo']['lines'][1]['at_s'] = 99
        self.assertFails(d, 'start inside its shot')
        d = self.vo_base(); d['vo']['voice'] = 'af_bella'
        self.assertFails(d, 'Liam is Kokoro am_onyx')
        d = self.vo_base(); d['vo']['engine'] = 'elevenlabs'
        self.assertFails(d, 'engine must be kokoro')
        d = self.vo_base(); (self.root / 'audio/vo/manifest.json').unlink()
        self.assertFails(d, 'manifest.json')
        d = self.vo_base(); d['vo']['lines'] = [dict(d['vo']['lines'][0], id=f'V{k}', at_s=0.0) for k in range(7)]
        d['vo']['lines'][0]['text'] = ' '.join(['word'] * 12)
        d['vo']['lines'] = [dict(line, text=' '.join(['word'] * 11)) for line in d['vo']['lines']]
        self.make_vo(d['vo']['lines'])
        self.assertFails(d, 'the budget is')

    def test_mix_must_match_the_timeline(self):
        d = self.base()
        wav = self.root / 'mix.wav'
        with wave.open(str(wav), 'wb') as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(8000)
            w.writeframes((np.zeros(8000 * 10, dtype=np.int16)).tobytes())
        d['mix'] = 'mix.wav'
        self.assertFails(d, 'mix length differs')

    def test_done_viewer_test_must_have_passed_and_include_a_muted_viewer(self):
        d = self.base()
        row = {'id': 'v1', 'sound': 'on', 'genre_at_10s': 'platformer', 'player_does': 'jumps gaps',
               'what_is_different': 'the gaps', 'outcome': 'pass'}
        d['checks'] = {'viewer_test': {'status': 'done', 'viewers': [row]}}
        self.assertFails(d, 'viewer test needs')
        quiet = dict(row, id='v2', sound='off')
        d['checks']['viewer_test']['viewers'] = [row, quiet]
        self.assertEqual(self.run_gate(d)['fails'], [])
        d['checks']['viewer_test']['viewers'] = [row, dict(quiet, outcome='fail')]
        self.assertFails(d, 'revise the footage and sequence')


@unittest.skipUnless(shutil.which('ffmpeg') and shutil.which('ffprobe'), 'requires ffmpeg/ffprobe')
class AssemblerTests(TrailerGateTests):
    """Reuses the gate fixture: trim exactness, a sheet the compiler accepts, a mix of the right length."""

    def test_trim_sheet_and_mix(self):
        data = self.base()
        (self.root / 'trailer.json').write_text(json.dumps(data))
        asm.trim_clips(self.root, data, force=True)
        asm.write_sheet(self.root, data)
        asm.build_mix(self.root, data)
        spans, total = gate.timeline(data['shots'])
        for shot in data['shots']:
            if shot['kind'] != 'gameplay':
                continue
            frames = subprocess.run(['ffprobe', '-v', 'error', '-count_frames', '-select_streams', 'v:0',
                                     '-show_entries', 'stream=nb_read_frames', '-of', 'csv=p=0',
                                     str(self.root / 'media' / f'{shot["id"]}.mp4')],
                                    capture_output=True, text=True).stdout.strip()
            self.assertEqual(int(frames), round((shot['out_s'] - shot['in_s']) * 30), shot['id'])
        sheet = json.loads((self.root / 'beat_sheet.json').read_text())
        self.assertEqual(sum(b['render_duration_s'] for b in sheet['beats']), total)
        self.assertEqual(sheet['beats'][-1]['shot']['remotion']['props']['kind'], 'endcard')
        spec = importlib.util.spec_from_file_location('bs', ROOT / 'runtime/scripts/build_safety.py')
        safety = importlib.util.module_from_spec(spec)
        import sys
        sys.path.insert(0, str(ROOT / 'runtime/scripts'))
        spec.loader.exec_module(safety)
        safety.validate_project(sheet)        # the compiler's own structural check
        self.assertTrue(sheet['beats'][-1]['qc']['sparse_by_design'])            # cards are sparse on purpose, with a reason
        self.assertTrue(sheet['beats'][-1]['qc']['sparse_reason'])
        mix = self.root / 'audio/trailer-mix.wav'
        self.assertAlmostEqual(gate.probe(mix)['duration_s'], total, delta=0.1)
        self.assertGreater(gate.window_rms(mix, 1.0, 3.0), 0.001)    # the game audio is in the mix
        self.assertEqual(self.run_gate(dict(data, mix='audio/trailer-mix.wav'))['fails'], [])


    def test_mix_puts_the_voice_over_ducked_music(self):
        d = self.vo_base()
        wav = self.root / 'bed.wav'
        with wave.open(str(wav), 'wb') as w:                    # a steady loud bed so ducking is measurable
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(24000)
            t = np.arange(24000 * 40) / 24000
            w.writeframes((0.5 * 32767 * np.sin(2 * np.pi * 440 * t)).astype('<i2').tobytes())
        d['music'] = {'source': 'supplied', 'path': 'bed.wav', 'sha256': gate.sha256(wav),
                      'provenance': 'test tone', 'tone_note': 'fixture', 'rhythm': 'free'}
        (self.root / 'trailer.json').write_text(json.dumps(d))
        asm.build_mix(self.root, d)
        mix = self.root / 'audio/trailer-mix.wav'
        _, total = gate.timeline(d['shots'])
        self.assertAlmostEqual(gate.probe(mix)['duration_s'], total, delta=0.1)
        def tone(a, b, hz):                                      # level of one frequency in a window of the mix
            raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(a), '-t', str(b - a), '-i', str(mix), '-vn',
                                  '-ac', '1', '-ar', '24000', '-f', 'f32le', '-'], capture_output=True).stdout
            x = np.frombuffer(raw, dtype='<f4')
            return abs(np.sum(x * np.exp(-2j * np.pi * hz * np.arange(len(x)) / 24000))) / len(x)
        self.assertGreater(tone(0.5, 1.2, 180), 0.01)                 # the voice (180 Hz) is in the mix
        self.assertLess(tone(0.5, 1.2, 440), 0.6 * tone(3.0, 3.7, 440))   # and the 440 Hz bed steps down under it

    def test_presentation_insets_the_clip_and_writes_gate_regions(self):
        data = self.base()
        data['presentation'] = {'inset': 0.9, 'pad_color': '#F6F3EB',
                                'contrast_regions': [{'label': 'HUD', 'box': [0.07, 0.07, 0.85, 0.2]}],
                                'contrast_reason': 'fixture'}
        (self.root / 'trailer.json').write_text(json.dumps(data))
        asm.trim_clips(self.root, data, force=True)
        asm.write_sheet(self.root, data)
        dims = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height',
                               '-of', 'csv=p=0', str(self.root / 'media/S02.mp4')], capture_output=True, text=True).stdout.strip()
        self.assertEqual(dims, '3840,2160')
        frame = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(self.root / 'media/S02.mp4'), '-frames:v', '1',
                                '-vf', 'crop=8:8:0:0,format=rgb24', '-f', 'rawvideo', '-'], capture_output=True).stdout
        for got, want in zip(frame[:3], (0xF6, 0xF3, 0xEB)):                    # the margin is the game's own colour
            self.assertLessEqual(abs(got - want), 4)                            # (yuv420p rounds a channel or two)
        sheet = json.loads((self.root / 'beat_sheet.json').read_text())
        self.assertEqual(sheet['beats'][1]['qc']['contrast_regions'][0]['label'], 'HUD')
        data.pop('presentation')                                                # leave the shared fixture clean
        asm.trim_clips(self.root, data, force=True)


@unittest.skipUnless(shutil.which('ffmpeg') and (ROOT / 'runtime/models/kokoro/kokoro-v1.0.onnx').exists(),
                     'needs the local Kokoro model (./setup --install)')
class LiamVoiceTests(unittest.TestCase):
    def test_liam_lines_are_generated_trimmed_normalised_and_bound_to_their_text(self):
        with tempfile.TemporaryDirectory(prefix='vo-test-') as tmp:
            root = Path(tmp)
            (root / 'trailer.json').write_text(json.dumps({'vo': {'engine': 'kokoro', 'voice': 'am_onyx', 'lines': [
                {'id': 'V01', 'shot': 'S01', 'at_s': 0.2, 'text': 'One jump. Read the landing.'}]}}))
            manifest = vok.generate(root)
            entry = manifest['V01']
            self.assertEqual(entry['voice'], 'am_onyx')
            self.assertTrue(1.0 < entry['duration_s'] < 3.5, entry['duration_s'])
            wav = root / 'audio/vo/V01.wav'
            samples = np.frombuffer(wave.open(str(wav)).readframes(10 ** 7), dtype='<i2') / 32767
            self.assertAlmostEqual(float(np.abs(samples).max()), vok.TARGET_PEAK, delta=0.02)
            again = vok.generate(root)                                   # unchanged text: nothing regenerated
            self.assertEqual(again['V01']['wav_sha256'], entry['wav_sha256'])


class BeatGridTests(unittest.TestCase):
    def synth(self, path, bpm, offset, secs=24):
        sr, n = 44100, 44100 * secs
        x, rng = np.zeros(n, dtype=np.float32), np.random.default_rng(3)
        period, t, k = 60 / bpm, offset, 0
        while t < secs - 0.3:
            i, length = int(round(t * sr)), int(0.15 * sr)
            tt = np.arange(length) / sr
            amp = 1.0 if k % 4 == 0 else 0.6
            x[i:i + length] += amp * np.sin(2 * np.pi * (55 + 90 * np.exp(-tt * 40)) * tt) * np.exp(-tt * 22)
            j, h = int(round((t + period / 2) * sr)), int(0.03 * sr)
            x[j:j + h] += 0.3 * rng.standard_normal(h) * np.exp(-np.arange(h) / (0.008 * sr))   # off-beat hat
            t += period; k += 1
        x /= np.abs(x).max()
        with wave.open(str(path), 'wb') as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
            w.writeframes((x * 32000).astype(np.int16).tobytes())

    @unittest.skipUnless(shutil.which('ffmpeg'), 'requires ffmpeg')
    def test_recovers_tempo_and_follows_the_kick_not_the_hat(self):
        with tempfile.TemporaryDirectory(prefix='beat-grid-test-') as tmp:
            for bpm, offset in ((100, 0.23), (128, 0.0), (87, 0.4)):
                path = Path(tmp) / f'{bpm}.wav'
                self.synth(path, bpm, offset)
                result = grid.analyse(path)
                self.assertAlmostEqual(result['bpm'], bpm, delta=0.3)
                period = 60 / bpm
                error = ((result['beats'][0] - offset + period / 2) % period) - period / 2
                self.assertLess(abs(error), 0.04, (bpm, error))


if __name__ == '__main__':
    unittest.main()
