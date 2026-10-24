"""Tests for the blender-build skill: the tape (record and harvest), the interface drafter, the
interface map's names against a real Blender, the census, the guide writer and the record gate.

The Blender tests drive the installed Blender (skipped when absent). Fixtures are synthetic."""
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import socket
import subprocess
import tempfile
import threading
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / 'skills/make/blender-build/scripts'
BLENDER = os.environ.get('BLENDER') or '/Applications/Blender.app/Contents/MacOS/Blender'
MASCOT_SESSION = ROOT.parent / 'claude-mascot-3d/mcp-run/session'


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


import sys  # noqa: E402
sys.path.insert(0, str(SCRIPTS))
tape = load('bb_tape', 'tape.py')
draft = load('bb_draft', 'draft_steps.py')
gate = load('bb_gate', 'verify_breakdown.py')
guide = load('bb_guide', 'reconstruct_md.py')
census = load('bb_census', 'census.py')
replay = load('bb_replay', 'replay.py')


def sha(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode()).hexdigest()


# ---------------------------------------------------------------- tape

class FakeAddon:
    """The wire protocol of the Blender MCP add-on: one JSON object in, one JSON object out."""

    def __init__(self):
        self.srv = socket.socket()
        self.srv.bind(('127.0.0.1', 0))
        self.srv.listen(5)
        self.port = self.srv.getsockname()[1]
        self.seen = []
        self.reply = {'status': 'success', 'result': {'executed': True, 'result': 'Code executed successfully: 3 objects'}}
        threading.Thread(target=self.loop, daemon=True).start()

    def loop(self):
        while True:
            try:
                c, _ = self.srv.accept()
            except OSError:
                return
            data = b''
            while True:
                data += c.recv(65536)
                try:
                    msg = json.loads(data.decode())
                    break
                except ValueError:
                    continue
            self.seen.append(msg)
            c.sendall(json.dumps(self.reply).encode())
            c.close()

    def close(self):
        self.srv.close()


class TapeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.addon = FakeAddon()
        self.addCleanup(self.addon.close)
        self.path = self.tmp / 'tape' / 'live.jsonl'

    def test_a_live_call_is_recorded_with_its_reason_and_reply(self):
        t = tape.Tape(self.path, stage='04-blockout', port=self.addon.port)
        seq, reply = t.code('import bpy\nprint(len(bpy.data.objects))', why='count what exists', label='census')
        self.assertEqual(seq, 1)
        rec = tape.read_tape(self.path)[0]
        self.assertEqual(rec['status'], 'ok')
        self.assertEqual(rec['stage'], '04-blockout')
        self.assertEqual(rec['why'], 'count what exists')
        self.assertIn('3 objects', rec['result'])
        self.assertEqual(rec['code_sha256'], sha('import bpy\nprint(len(bpy.data.objects))'))
        self.assertEqual(self.addon.seen[0]['type'], 'execute_code')

    def test_run_file_records_the_file_not_the_wrapper(self):
        f = self.tmp / 'build_part.py'
        f.write_text('import bpy\n# build the torso\n')
        t = tape.Tape(self.path, port=self.addon.port)
        t.run_file(f, label='torso')
        rec = tape.read_tape(self.path)[0]
        self.assertEqual(rec['code'], 'import bpy\n# build the torso\n')
        self.assertEqual(rec['script_sha256'], sha('import bpy\n# build the torso\n'))
        self.assertIn('exec(compile', self.addon.seen[0]['params']['code'])

    def test_a_failed_reply_is_an_error_line_not_a_silent_skip(self):
        self.addon.reply = {'status': 'error', 'message': 'Error executing code: boom'}
        t = tape.Tape(self.path, port=self.addon.port)
        t.code('1/0')
        self.assertEqual(tape.read_tape(self.path)[0]['status'], 'error')

    def test_an_unreachable_blender_is_recorded_too(self):
        dead = socket.socket()
        dead.bind(('127.0.0.1', 0))
        port = dead.getsockname()[1]
        dead.close()
        t = tape.Tape(self.path, port=port)
        t.code('print(1)')
        rec = tape.read_tape(self.path)[0]
        self.assertEqual(rec['status'], 'error')
        self.assertIn('cannot reach Blender', rec['result'])

    def test_a_query_is_marked_as_not_changing_the_scene(self):
        t = tape.Tape(self.path, port=self.addon.port)
        t.call('get_scene_info')
        self.assertFalse(tape.read_tape(self.path)[0]['mutates'])

    def _transcript(self, lines):
        p = self.tmp / 't.jsonl'
        p.write_text('\n'.join(json.dumps(x) for x in lines) + '\n')
        return p

    def test_harvest_pairs_calls_with_replies_and_ignores_other_tools(self):
        lines = [
            {'type': 'assistant', 'session_id': 's1', 'message': {'content': [
                {'type': 'tool_use', 'id': 'a', 'name': 'mcp__blender__execute_blender_code',
                 'input': {'code': 'import bpy\nbpy.ops.mesh.primitive_cube_add()', 'user_prompt': 'make a cube'}},
                {'type': 'tool_use', 'id': 'b', 'name': 'Read', 'input': {'file_path': '/x'}},
                {'type': 'tool_use', 'id': 'c', 'name': 'Bash',
                 'input': {'command': '/Applications/Blender.app/Contents/MacOS/Blender -b x.blend --python s.py'}},
                {'type': 'tool_use', 'id': 'd', 'name': 'Bash', 'input': {'command': 'ls -la'}}]}},
            {'type': 'user', 'message': {'content': [
                {'type': 'tool_result', 'tool_use_id': 'a',
                 'content': json.dumps({'result': 'Code executed successfully: ok'})},
                {'type': 'tool_result', 'tool_use_id': 'c', 'content': 'Traceback (most recent call last): boom',
                 'is_error': False}]}},
        ]
        recs = tape.harvest([self._transcript(lines)])
        self.assertEqual([r['tool'] for r in recs], ['mcp__blender__execute_blender_code', 'Bash'])
        self.assertEqual(recs[0]['why'], 'make a cube')
        self.assertEqual(recs[0]['status'], 'ok')
        self.assertIn('Code executed successfully', recs[0]['result'])
        self.assertEqual(recs[1]['status'], 'error')
        self.assertEqual(recs[1]['script_path'], 's.py')

    def test_harvest_can_skip_bash(self):
        lines = [{'message': {'content': [{'type': 'tool_use', 'id': 'c', 'name': 'Bash',
                                           'input': {'command': 'blender -b x.blend --python s.py'}}]}}]
        self.assertEqual(tape.harvest([self._transcript(lines)], include_bash=False), [])

    @unittest.skipUnless(MASCOT_SESSION.exists(), 'the real mascot MCP transcripts are not on this machine')
    def test_harvest_recovers_the_real_mascot_build(self):
        recs = tape.harvest(sorted(MASCOT_SESSION.glob('turn*.jsonl')))
        execs = [r for r in recs if r['tool'].endswith('execute_blender_code')]
        self.assertEqual(len(execs), 22)
        self.assertEqual(sum(r['status'] == 'error' for r in execs), 1)
        self.assertTrue(all(r['why'] for r in execs))


# ---------------------------------------------------------------- drafter

class DraftTests(unittest.TestCase):
    def gui(self, code):
        return draft.translate(code)

    def joined(self, code):
        return '\n'.join(self.gui(code)['gui'])

    def test_a_cube_with_dimensions_becomes_menu_steps_with_the_numbers(self):
        t = self.joined('import bpy\nbpy.ops.mesh.primitive_cube_add(location=(0, 0, 0.56))\n'
                        'obj = bpy.context.active_object\nobj.name = "Torso"\nobj.dimensions = (0.96, 0.48, 0.60)\n'
                        'bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)\n')
        self.assertIn('Add ▸ Mesh ▸ Cube', t)
        self.assertIn('Location X 0, Y 0, Z 0.56', t)
        self.assertIn("Rename the object to 'Torso'", t)
        self.assertIn('Dimensions on Torso = X 0.96, Y 0.48, Z 0.6', t)
        self.assertIn('Apply ▸ Rotation & Scale', t)

    def test_rotation_radians_are_shown_as_degrees(self):
        t = self.joined('import bpy, math\nobj = bpy.context.active_object\nobj.rotation_euler = (math.radians(90), 0, 0)\n')
        self.assertIn('X 90°, Y 0°, Z 0°', t)

    def test_a_modifier_and_its_settings_use_the_interface_labels(self):
        t = self.joined('import bpy\nm = obj.modifiers.new(name="Bev", type="BEVEL")\nm.width = 0.02\nm.segments = 3\n')
        self.assertIn('Add Modifier ▸ Generate ▸ Bevel', t)
        self.assertIn('Amount = 0.02', t)
        self.assertIn('Segments = 3', t)

    def test_a_constraint_is_placed_in_its_menu(self):
        t = self.joined('c = obj.constraints.new("FOLLOW_PATH")\nc.use_fixed_location = True\nc.offset_factor = 0.5\n')
        self.assertIn('Add Object Constraint ▸ Relationship ▸ Follow Path', t)
        self.assertIn('Fixed Position = True', t)
        self.assertIn('Offset Factor = 0.5', t)

    def test_an_unknown_operator_is_unmapped_never_guessed(self):
        r = self.gui('import bpy\nbpy.ops.sculpt.dyntopo_toggle_zzz()\n')
        self.assertEqual(len(r['unmapped']), 1)
        self.assertIn('UNMAPPED', r['gui'][0])
        self.assertNotIn('Add ▸', r['gui'][0])

    def test_raw_mesh_data_has_no_interface_route(self):
        r = self.gui('import bpy\nme = bpy.data.meshes.new("m")\nme.from_pydata([(0,0,0)], [], [])\n')
        self.assertTrue(any('from_pydata' in u for u in r['unmapped']))

    def test_pure_helpers_and_restore_lines_and_prints_are_not_steps(self):
        r = self.gui('import bpy\ndef f(x):\n    return x * 2\nv = f(3)\nprint(v)\norig = scene.render.engine\n'
                     'scene.render.engine = orig\n')
        self.assertEqual(r['gui'], [])
        self.assertFalse(r['changes_scene'])

    def test_a_helper_that_changes_the_scene_is_explained_once_per_call(self):
        t = self.joined('import bpy\ndef make(name):\n    m = bpy.data.materials.new(name=name)\n    return m\n'
                        'make("A")\nmake("B")\n')
        self.assertIn("helper step 'make' (name='A')", t)
        self.assertIn("name it 'B'", t)

    def test_loops_and_conditions_around_changes_are_kept(self):
        t = self.joined('import bpy\nfor n in ["a", "b"]:\n    bpy.ops.mesh.primitive_cube_add()\n')
        self.assertIn("Repeat for each n in ['a', 'b']", t)
        self.assertIn('  Add ▸ Mesh ▸ Cube', t)

    def test_script_bookkeeping_is_not_the_scene(self):
        r = self.gui('import bpy\ncreated = {}\ncreated["x"] = 1\n')
        self.assertEqual(r['gui'], [])

    def test_a_syntax_error_is_unmapped_not_a_crash(self):
        r = self.gui('def (:\n')
        self.assertIn('does not parse', r['gui'][0])

    def test_cards_mark_failures_and_tie_the_retry_to_them(self):
        tp = [
            {'seq': 1, 'code': 'import bpy\nbpy.ops.mesh.primitive_cube_add()', 'status': 'ok', 'result': 'ok', 'mutates': True, 'why': 'a cube'},
            {'seq': 2, 'code': 'import bpy\nbpy.ops.mesh.primitive_cube_add(boom)', 'status': 'error', 'result': 'Error executing code: bad', 'mutates': True, 'why': 'a rig'},
            {'seq': 3, 'code': 'import bpy\nbpy.ops.object.armature_add()', 'status': 'ok', 'result': 'ok', 'mutates': True, 'why': 'a rig'},
            {'seq': 4, 'code': 'print(1)', 'status': 'ok', 'result': '1', 'mutates': True, 'why': 'look'},
            {'seq': 5, 'tool': 'get_scene_info', 'params': {}, 'status': 'ok', 'mutates': False},
        ]
        cards = draft.build_cards(tp, 'tape/live.jsonl', draft.parse_stage_map('1-3:04-blockout'))
        self.assertEqual([c['id'] for c in cards], ['S001', 'S002', 'S003'])   # the print-only call is skipped
        self.assertTrue(cards[1]['excluded_from_procedure'])
        self.assertEqual(cards[2]['correction']['of'], 'S002')
        self.assertIn('Error executing code: bad', cards[2]['correction']['evidence'])
        self.assertEqual(cards[0]['stage'], '04-blockout')
        self.assertEqual(cards[0]['operation']['python']['ref'], 'tape/live.jsonl#1')
        self.assertEqual(cards[0]['operation']['gui_source'], 'draft')
        self.assertIn('why', cards[0]['needs_author'])

    @unittest.skipUnless(MASCOT_SESSION.exists(), 'the real mascot MCP transcripts are not on this machine')
    def test_the_real_mascot_build_translates_with_few_unmapped_lines(self):
        recs = tape.harvest(sorted(MASCOT_SESSION.glob('turn*.jsonl')))
        for i, r in enumerate(recs, 1):
            r['seq'] = i
        cards = draft.build_cards(recs, 'tape/h.jsonl')
        self.assertEqual(len(cards), 21)
        self.assertEqual(sum(1 for c in cards if c.get('excluded_from_procedure')), 1)
        unmapped = sum(1 for c in cards for ln in c['operation']['gui'] if ln.lstrip().startswith('UNMAPPED'))
        self.assertLessEqual(unmapped, 3)
        cubes = sum(1 for c in cards if 'mesh.primitive_cube_add' in c['operation']['bl_idnames'])
        self.assertEqual(cubes, 9)


# ---------------------------------------------------------------- replay selection

class ReplaySelectTests(unittest.TestCase):
    def test_commands_that_write_files_are_recognised(self):
        for code, why in [("bpy.ops.wm.save_as_mainfile(filepath='/x.blend')", 'saves'),
                          ("bpy.ops.export_scene.gltf(filepath='/x.glb')", 'exports'),
                          ("bpy.ops.render.render(write_still=True)", 'renders'),
                          ("open('/x.txt', 'w').write('a')", 'writing'),
                          ("import os\nos.remove('/x')", 'files'),
                          ("import subprocess\nsubprocess.run(['ls'])", 'program')]:
            self.assertIn(why, replay.classify(code) or '', code)
        self.assertIsNone(replay.classify("import bpy\nbpy.ops.mesh.primitive_cube_add()\nprint(open('/x').read())"))

    def test_select_skips_failures_queries_writes_and_other_tools_and_says_why(self):
        tp = [
            {'seq': 1, 'code': 'import bpy', 'status': 'ok', 'mutates': True, 'tool': 'execute_code'},
            {'seq': 2, 'code': 'boom', 'status': 'error', 'mutates': True, 'tool': 'execute_code'},
            {'seq': 3, 'code': 'x', 'status': 'ok', 'mutates': False, 'tool': 'execute_code'},
            {'seq': 4, 'code': "bpy.ops.wm.save_as_mainfile(filepath='/real.blend')", 'status': 'ok', 'mutates': True},
            {'seq': 5, 'code': 'blender -b x', 'status': 'ok', 'mutates': True, 'tool': 'Bash'},
            {'seq': 6, 'code': 'import bpy', 'status': 'ok', 'mutates': True, 'tool': 'mcp__blender__execute_blender_code'},
            {'seq': 7, 'code': 'import bpy', 'status': 'ok', 'mutates': True, 'tool': 'execute_code'},
        ]
        run, skipped = replay.select(tp, skip={7})
        self.assertEqual([r['seq'] for r in run], [1, 6])
        reasons = {s['seq']: s['why'] for s in skipped}
        self.assertIn('failed', reasons[2])
        self.assertIn('query', reasons[3])
        self.assertIn('writes files', reasons[4])
        self.assertIn('not Python', reasons[5])
        self.assertIn('--skip', reasons[7])
        run, _ = replay.select(tp, allow_writes=True)
        self.assertIn(4, [r['seq'] for r in run])
        run, _ = replay.select(tp, lo=6)
        self.assertEqual([r['seq'] for r in run], [6, 7])


# ---------------------------------------------------------------- Blender

def blender(blend, script, *args, timeout=240):
    cmd = [BLENDER, '-b'] + ([str(blend)] if blend else ['--factory-startup']) + ['--python', str(script)] + list(args)
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


BUILD_SCRIPT = '''
import bpy, sys
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
width = float(sys.argv[sys.argv.index("--") + 2]) if len(sys.argv) > sys.argv.index("--") + 2 else 1.0
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0.5))
o = bpy.context.active_object
o.name = "Block"
o.dimensions = (width, 1.0, 1.0)
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
m = o.modifiers.new("Bev", "BEVEL"); m.width = 0.05; m.segments = 2
mat = bpy.data.materials.new("Paint"); mat.use_nodes = True
o.data.materials.append(mat)
for name, loc in (("CMP_ISO", (4, -4, 3)), ("CMP_FRONT", (0, -6, 0.8))):
    cd = bpy.data.cameras.new(name); co = bpy.data.objects.new(name, cd); sc.collection.objects.link(co)
    co.location = loc
    c = co.constraints.new("TRACK_TO")
    t = bpy.data.objects.new(name + "_t", None); sc.collection.objects.link(t); t.location = (0, 0, 0.5)
    c.target = t; c.track_axis = "TRACK_NEGATIVE_Z"; c.up_axis = "UP_Y"
bpy.ops.wm.save_as_mainfile(filepath=sys.argv[sys.argv.index("--") + 1])
'''


@unittest.skipUnless(Path(BLENDER).exists(), 'requires Blender')
class BlenderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp())
        cls.build = cls.tmp / 'build.py'
        cls.build.write_text(BUILD_SCRIPT)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, True)

    def make(self, name, width=None):
        out = self.tmp / name
        args = [str(out)] + ([str(width)] if width is not None else [])
        p = blender(None, self.build, '--', *args)
        self.assertTrue(out.exists(), p.stdout[-600:])
        return out

    def census_of(self, blend, name):
        out = self.tmp / (name + '.json')
        p = blender(blend, SCRIPTS / 'census.py', '--', 'census', '--out', str(out))
        self.assertTrue(out.exists(), p.stdout[-600:])
        return out

    def test_every_operator_and_property_name_in_the_interface_map_exists(self):
        p = blender(None, SCRIPTS / 'check_gui_map.py')
        self.assertEqual(p.returncode, 0, p.stdout[-1500:])
        rep = json.loads(p.stdout[p.stdout.index('{'):p.stdout.rindex('}') + 1])
        self.assertTrue(rep['ok'])
        self.assertEqual(rep['checked']['properties_checked'], rep['checked']['properties_expected'])
        self.assertGreater(rep['checked']['properties_checked'], 50)    # nothing was silently skipped

    def test_the_map_check_catches_a_name_that_does_not_exist(self):
        d = self.tmp / 'scripts_copy'
        shutil.copytree(SCRIPTS, d, ignore=shutil.ignore_patterns('__pycache__'))
        with open(d / 'gui_map.py', 'a') as f:
            f.write("\nOPS['mesh.primitive_teapot_add'] = ('x', {})\n"
                    "MODIFIERS['BEVEL'][2]['not_a_real_property'] = 'x'\n"
                    "CONSTRAINTS['FOLLOW_PATH'][2]['also_not_real'] = 'x'\n")
        p = blender(None, d / 'check_gui_map.py')
        self.assertEqual(p.returncode, 1)
        self.assertIn('mesh.primitive_teapot_add', p.stdout)
        self.assertIn('BEVEL.not_a_real_property', p.stdout)
        self.assertIn('FOLLOW_PATH.also_not_real', p.stdout)

    def test_census_describes_the_scene_and_its_signature_is_stable(self):
        a = self.census_of(self.make('a.blend'), 'a')
        b = self.census_of(self.make('b.blend'), 'b')
        ca, cb = json.loads(a.read_text()), json.loads(b.read_text())
        block = next(o for o in ca['objects'] if o['name'] == 'Block')
        self.assertEqual(block['dimensions'], [1.0, 1.0, 1.0])
        self.assertEqual(block['modifiers'][0]['type'], 'BEVEL')
        self.assertEqual(block['modifiers'][0]['settings']['segments'], 2)
        self.assertEqual(block['materials'], ['Paint'])
        self.assertGreater(block['triangles'], 12)             # evaluated: the bevel adds faces
        self.assertEqual(ca['signature'], cb['signature'])      # the same script twice: the same model
        self.assertEqual(census.compare(ca, cb)['differences'], [])

    def test_comparison_cameras_are_recorded_but_are_not_part_of_the_model(self):
        blend = self.make('cmp.blend')
        base = json.loads(self.census_of(blend, 'cmp_base').read_text())
        add = self.tmp / 'add_cam.py'
        out = self.tmp / 'cmp_more.blend'
        add.write_text('import bpy, sys\n'
                       'c = bpy.data.objects.new("CMP_EXTRA", bpy.data.cameras.new("CMP_EXTRA"))\n'
                       'bpy.context.scene.collection.objects.link(c)\n'
                       'bpy.ops.wm.save_as_mainfile(filepath=%r)\n' % str(out))
        blender(blend, add)
        more = json.loads(self.census_of(out, 'cmp_more').read_text())
        self.assertEqual(base['signature'], more['signature'])
        self.assertEqual(more['totals']['comparison_objects'], base['totals']['comparison_objects'] + 1)
        self.assertEqual(more['totals']['objects'], base['totals']['objects'])
        self.assertTrue(next(o for o in more['objects'] if o['name'] == 'CMP_EXTRA')['comparison'])
        # a real model object, by contrast, changes the signature
        real = self.tmp / 'add_obj.py'
        out2 = self.tmp / 'real_more.blend'
        real.write_text('import bpy\nbpy.ops.mesh.primitive_cube_add()\n'
                        'bpy.ops.wm.save_as_mainfile(filepath=%r)\n' % str(out2))
        blender(blend, real)
        self.assertNotEqual(base['signature'], json.loads(self.census_of(out2, 'real_more').read_text())['signature'])

    def test_compare_names_what_changed(self):
        a = json.loads(self.census_of(self.make('w1.blend', 1.0), 'w1').read_text())
        b = json.loads(self.census_of(self.make('w2.blend', 2.0), 'w2').read_text())
        res = census.compare(a, b)
        self.assertFalse(res['ok'])
        self.assertNotEqual(a['signature'], b['signature'])
        self.assertTrue(any('Block: dimensions' in d for d in res['differences']), res['differences'])
        p = subprocess.run([sys.executable, str(SCRIPTS / 'census.py'), 'compare', str(self.tmp / 'w1.json'),
                            str(self.tmp / 'w2.json')], capture_output=True, text=True)
        self.assertEqual(p.returncode, 1)
        self.assertIn('DIFFERENT', p.stdout)

    def test_milestone_renders_the_fixed_views_and_reports_a_missing_one(self):
        blend = self.make('m.blend')
        out = self.tmp / 'ms'
        p = blender(blend, SCRIPTS / 'census.py', '--', 'milestone', '--stage', '04-blockout', '--out-dir', str(out),
                    '--views', 'CMP_ISO,CMP_FRONT,CMP_NOPE', '--resolution', '320x180')
        self.assertEqual(p.returncode, 0, p.stdout[-600:])
        ms = json.loads((out / 'milestone.json').read_text())
        self.assertEqual([v['name'] for v in ms['views']], ['CMP_ISO', 'CMP_FRONT'])
        self.assertEqual(ms['missing_views'], ['CMP_NOPE'])
        for v in ms['views']:
            self.assertEqual(sha((out / v['path']).read_bytes()), v['sha256'])
        self.assertEqual(ms['census_signature'], json.loads((out / 'census.json').read_text())['signature'])

    REPLAY_CMDS = [
        "import bpy\nfor o in list(bpy.data.objects):\n    bpy.data.objects.remove(o, do_unlink=True)\n"
        "bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0.5))\no = bpy.context.active_object\no.name = 'Block'\n"
        "o.dimensions = (1, 1, 1)\nbpy.ops.object.transform_apply(location=False, rotation=True, scale=True)",
        "import bpy\no = bpy.data.objects['Block']\nm = o.modifiers.new('Bev', 'BEVEL'); m.width = 0.05\n"
        "mat = bpy.data.materials.new('Paint'); mat.use_nodes = True\no.data.materials.append(mat)",
    ]

    def test_replay_from_a_tape_reproduces_the_model_and_will_not_write_a_file(self):
        guard = self.tmp / 'must_not_exist.blend'
        cmds = self.REPLAY_CMDS + [f"import bpy\nbpy.ops.wm.save_as_mainfile(filepath={str(guard)!r})"]
        tp = self.tmp / 'replay_tape.jsonl'
        tp.write_text('\n'.join(json.dumps({'seq': i, 'tool': 'execute_code', 'code': c, 'status': 'ok', 'mutates': True})
                                for i, c in enumerate(cmds, 1)) + '\n')
        direct = self.tmp / 'direct.py'
        direct.write_text('\n'.join(self.REPLAY_CMDS) + '\n')
        out = self.tmp / 'direct.blend'
        # direct build, saved and censused through the same path the replay uses
        runner = self.tmp / 'run_direct.py'
        runner.write_text(f"import bpy\nexec(open({str(direct)!r}).read())\nbpy.ops.wm.save_as_mainfile(filepath={str(out)!r})\n")
        blender(None, runner)
        a = json.loads(self.census_of(out, 'direct').read_text())
        rc, rep = self.tmp / 'replay_census.json', self.tmp / 'replay_report.json'
        p = blender(None, SCRIPTS / 'replay.py', '--', str(tp), '--out', str(self.tmp / 'replayed.blend'),
                    '--census', str(rc), '--report', str(rep))
        self.assertEqual(p.returncode, 0, p.stdout[-800:])
        report = json.loads(rep.read_text())
        self.assertTrue(report['ok'])
        self.assertEqual([r['seq'] for r in report['ran']], [1, 2])
        self.assertEqual([s['seq'] for s in report['skipped']], [3])
        self.assertFalse(guard.exists(), 'the replay wrote the file a recorded command would have written')
        b = json.loads(rc.read_text())
        self.assertEqual(census.compare(a, b)['differences'], [])
        self.assertEqual(a['signature'], b['signature'])

    def test_a_replay_that_cannot_run_a_command_fails_and_names_it(self):
        cmds = self.REPLAY_CMDS + ["import bpy\nbpy.data.objects['NoSuchObject'].name = 'x'"]
        tp = self.tmp / 'bad_tape.jsonl'
        tp.write_text('\n'.join(json.dumps({'seq': i, 'tool': 'execute_code', 'code': c, 'status': 'ok', 'mutates': True})
                                for i, c in enumerate(cmds, 1)) + '\n')
        rep = self.tmp / 'bad_report.json'
        p = blender(None, SCRIPTS / 'replay.py', '--', str(tp), '--out', str(self.tmp / 'bad.blend'), '--report', str(rep))
        self.assertEqual(p.returncode, 1)
        report = json.loads(rep.read_text())
        self.assertFalse(report['ok'])
        self.assertEqual(report['failed']['seq'], 3)
        self.assertIn('NoSuchObject', report['failed']['error'])

    def test_a_replay_can_be_told_to_leave_out_a_command_that_only_reads(self):
        cmds = self.REPLAY_CMDS + ["import bpy\nbpy.data.images.load('/no/such/render.png')"]
        tp = self.tmp / 'skip_tape.jsonl'
        tp.write_text('\n'.join(json.dumps({'seq': i, 'tool': 'execute_code', 'code': c, 'status': 'ok', 'mutates': True})
                                for i, c in enumerate(cmds, 1)) + '\n')
        args = [str(tp), '--out', str(self.tmp / 'skip.blend')]
        self.assertEqual(blender(None, SCRIPTS / 'replay.py', '--', *args).returncode, 1)
        p = blender(None, SCRIPTS / 'replay.py', '--', *args, '--skip', '3')
        self.assertEqual(p.returncode, 0, p.stdout[-600:])
        self.assertIn('skipped by --skip', p.stdout)

    def test_replay_rebuilds_the_same_signature_from_the_recorded_script(self):
        """The replay check: run the recorded build script headless again, census it, compare."""
        a = json.loads(self.census_of(self.make('orig.blend'), 'orig').read_text())
        b = json.loads(self.census_of(self.make('replay.blend'), 'replay').read_text())
        self.assertEqual(a['signature'], b['signature'])


REVEAL_SCENE = '''
import bpy, sys, math
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
for name, x in (("Cube", 0.0), ("Cube2", 3.0)):
    bpy.ops.mesh.primitive_cube_add(size=1, location=(x, 0, 0.5))
    bpy.context.active_object.name = name
mat = bpy.data.materials.new("Red"); mat.use_nodes = True
mat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.8, 0.1, 0.1, 1)
for n in ("Cube", "Cube2"):
    bpy.data.objects[n].data.materials.append(mat)
cam = bpy.data.objects.new("Cam", bpy.data.cameras.new("Cam")); sc.collection.objects.link(cam)
cam.data.type = "ORTHO"; cam.data.ortho_scale = 5; cam.location = (1.5, -10, 0.5)
cam.rotation_euler = (math.radians(90), 0, 0); sc.camera = cam
sun = bpy.data.objects.new("L", bpy.data.lights.new("L", "SUN")); sc.collection.objects.link(sun)
sun.data.energy = 3; sun.rotation_euler = (math.radians(50), 0, math.radians(30))
sc.render.engine = "CYCLES"; sc.cycles.samples = 8; sc.cycles.device = "CPU"
sc.render.resolution_x = sc.render.resolution_y = 100; sc.render.film_transparent = True
sc.render.image_settings.color_mode = "RGBA"
bpy.ops.wm.save_as_mainfile(filepath=sys.argv[sys.argv.index("--") + 1])
'''


@unittest.skipUnless(Path(BLENDER).exists(), 'requires Blender')
class RevealTests(unittest.TestCase):
    """The reveal is measured by rendering it and counting opaque pixels, not by reading the nodes."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp())
        mk = cls.tmp / 'mk.py'
        mk.write_text(REVEAL_SCENE)
        cls.src = cls.tmp / 'src.blend'
        blender(None, mk, '--', str(cls.src))

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, True)

    def reveal(self, technique, order, name):
        o = self.tmp / (name + '.json')
        o.write_text(json.dumps(order))
        out = self.tmp / (name + '.blend')
        p = blender(self.src, SCRIPTS / 'reveal.py', '--', technique, str(o), '--out', str(out))
        return p, out

    def coverage(self, blend, frame):
        from PIL import Image
        import numpy as np
        stem = self.tmp / f'f_{blend.stem}_'
        subprocess.run([BLENDER, '-b', str(blend), '-o', str(stem), '-f', str(frame)],
                       capture_output=True, text=True, timeout=240)
        a = np.asarray(Image.open(f'{stem}{frame:04d}.png').convert('RGBA'))[:, :, 3] > 128
        return int(a[:, :50].sum()), int(a[:, 50:].sum())

    def test_the_wipe_grows_each_piece_up_from_its_base_in_the_stated_order(self):
        p, out = self.reveal('wipe', {'order_source': 'explanatory', 'edge_band': 0.04, 'items': [
            {'label': 'first', 'objects': ['Cube'], 'start': 1, 'duration': 24},
            {'label': 'second', 'objects': ['Cube2'], 'start': 25, 'duration': 24}]}, 'wipe')
        self.assertIn('order_source=explanatory', p.stdout)
        full = 400
        self.assertEqual(self.coverage(out, 1), (0, 0))
        left_mid, right_mid = self.coverage(out, 13)
        self.assertAlmostEqual(left_mid / full, 0.5, delta=0.1)      # about half the height is up
        self.assertEqual(right_mid, 0)                              # the second piece has not started
        self.assertEqual(self.coverage(out, 25), (full, 0))
        self.assertEqual(self.coverage(out, 49), (full, full))

    def test_the_stagger_hides_a_piece_until_its_start_frame_then_lands_it(self):
        p, out = self.reveal('stagger', {'order_source': 'recorded', 'drop_height_m': 3.0, 'items': [
            {'label': 'first', 'objects': ['Cube'], 'start': 10, 'duration': 12, 'step': 'S001'},
            {'label': 'second', 'objects': ['Cube2'], 'start': 30, 'duration': 12, 'step': 'S002'}]}, 'stag')
        self.assertEqual(self.coverage(out, 5), (0, 0))
        self.assertEqual(self.coverage(out, 29)[1], 0)
        self.assertEqual(self.coverage(out, 60), (400, 400))

    def test_the_order_source_is_required_and_written_into_the_file(self):
        p, _ = self.reveal('wipe', {'items': [{'objects': ['Cube'], 'start': 1, 'duration': 5}]}, 'noorder')
        self.assertNotEqual(p.returncode, 0)
        self.assertIn('order_source', p.stdout + p.stderr)
        p, out = self.reveal('wipe', {'order_source': 'recorded', 'items': [
            {'objects': ['Cube'], 'start': 1, 'duration': 5, 'step': 'S001'}]}, 'rec')
        probe = self.tmp / 'probe.py'
        probe.write_text('import bpy\nprint("SRC", bpy.context.scene["reveal_order_source"])\n')
        self.assertIn('SRC recorded', blender(out, probe).stdout)

    def test_it_refuses_to_overwrite_the_model_it_opened(self):
        o = self.tmp / 'o.json'
        o.write_text(json.dumps({'order_source': 'explanatory', 'items': [{'objects': ['Cube'], 'start': 1, 'duration': 5}]}))
        p = blender(self.src, SCRIPTS / 'reveal.py', '--', 'wipe', str(o), '--out', str(self.src))
        self.assertNotEqual(p.returncode, 0)


# ---------------------------------------------------------------- guide and gate

SIG = 'c' * 64


def make_record(tmp, replay='pass', by_hand='pending'):
    base = Path(tmp)
    (base / 'tape').mkdir()
    (base / 'script').mkdir()
    (base / 'tape/live.jsonl').write_text('\n'.join(json.dumps({'seq': i, 'code': f'print({i})'}) for i in (1, 2, 3)) + '\n')
    (base / 'script/build_part.py').write_text('import bpy\n')
    for stage in ('04-blockout', '08-materials'):
        d = base / 'milestones' / stage
        (d / 'views').mkdir(parents=True)
        (d / 'views/CMP_ISO.png').write_bytes(b'png-' + stage.encode())
        (d / 'milestone.json').write_text(json.dumps({
            'stage': stage, 'census_signature': SIG,
            'views': [{'name': 'CMP_ISO', 'path': 'views/CMP_ISO.png', 'sha256': sha(b'png-' + stage.encode())}]}))
    rec = {
        'schema_version': 1,
        'model': {'name': 'test-model', 'kind': 'asset', 'built_by': ['the Blender MCP', 'headless scripts'],
                  'path': '/abs/path/final.blend', 'sha256': 'a' * 64, 'census_signature': SIG, 'blender': '5.1.2'},
        'stages': [
            {'id': '01-define', 'title': 'Define the project', 'summary': 'What it is for.'},
            {'id': '04-blockout', 'title': 'Block out the shape', 'milestone': 'milestones/04-blockout/milestone.json'},
            {'id': '08-materials', 'title': 'Materials', 'milestone': 'milestones/08-materials/milestone.json'}],
        'sources': [{'id': 'T1', 'kind': 'tape', 'path': 'tape/live.jsonl', 'sha256': sha((base / 'tape/live.jsonl').read_bytes())},
                    {'id': 'G1', 'kind': 'script', 'path': 'script/build_part.py', 'sha256': sha((base / 'script/build_part.py').read_bytes())}],
        'credits': [{'id': 'C1', 'what': 'a wood texture', 'source': 'a library', 'licence': 'CC0'}],
        'comparison_views': ['CMP_ISO'],
        'reconstruction': {'replay': {'status': replay, 'how': 'ran script/build_part.py headless and compared censuses',
                                      'census_signature': SIG} if replay == 'pass' else {'status': replay},
                           'by_hand': {'status': by_hand}},
    }
    steps = [
        {'id': 'S001', 'stage': '01-define', 'goal': 'Start from an empty scene', 'why': 'nothing else should leak into the model',
         'operation': {'python': {'source': 'tape', 'ref': 'tape/live.jsonl#1'}, 'gui': ['File ▸ New ▸ General'],
                       'gui_source': 'human', 'bl_idnames': []},
         'settings': {}, 'result': {'reply': 'ok'}, 'tier': 'recorded', 'evidence': [{'path': 'tape/live.jsonl', 'seq': 1}]},
        {'id': 'S002', 'stage': '04-blockout', 'goal': 'Add the block with its real size', 'why': 'the later stages measure against it',
         'operation': {'python': {'source': 'script', 'ref': 'script/build_part.py'}, 'gui': ['Add ▸ Mesh ▸ Cube (Shift+A)'],
                       'gui_source': 'draft', 'bl_idnames': ['mesh.primitive_cube_add']},
         'settings': {'Dimensions': '1 x 1 x 1 m'}, 'result': {'measured': {'dimensions_m': [1, 1, 1]}},
         'tier': 'scripted', 'evidence': [{'path': 'script/build_part.py'}],
         'repeats': {'rule': 'one per bay', 'instances': 3, 'listed': ['a', 'b', 'c']}},
        {'id': 'S003', 'stage': '08-materials', 'goal': 'Paint the block with the wood', 'why': 'read as timber from across the room',
         'operation': {'python': {'source': 'tape', 'ref': 'tape/live.jsonl#3'}, 'gui': ['Properties ▸ Material tab ▸ New'],
                       'gui_source': 'draft', 'bl_idnames': []},
         'settings': {}, 'result': {'reply': 'ok'}, 'tier': 'recorded', 'evidence': [{'path': 'tape/live.jsonl', 'seq': 3}],
         'uses_external_asset': {'name': 'wood texture', 'credit_id': 'C1'}},
    ]
    (base / 'record.json').write_text(json.dumps(rec))
    (base / 'BUILD-STEPS.jsonl').write_text('\n'.join(json.dumps(s) for s in steps) + '\n')
    return base


class GuideAndGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.base = make_record(self.tmp)

    def rec(self):
        return json.loads((self.base / 'record.json').read_text())

    def steps(self):
        return [json.loads(x) for x in (self.base / 'BUILD-STEPS.jsonl').read_text().splitlines() if x.strip()]

    def save(self, rec=None, steps=None):
        if rec is not None:
            (self.base / 'record.json').write_text(json.dumps(rec))
        if steps is not None:
            (self.base / 'BUILD-STEPS.jsonl').write_text('\n'.join(json.dumps(s) for s in steps) + '\n')

    def write_guide(self):
        guide.main(['--record', str(self.base / 'record.json'), '--steps', str(self.base / 'BUILD-STEPS.jsonl'),
                    '--out', str(self.base / 'RECONSTRUCT.md')])

    def run_gate(self, **kw):
        return gate.verify(self.base / 'record.json', **kw)

    def assertFails(self, rep, needle):
        self.assertTrue(any(needle in f for f in rep.fails), f'no failure containing {needle!r}: {rep.fails}')

    def test_a_sound_record_passes_and_says_the_interface_steps_are_drafts(self):
        self.write_guide()
        rep = self.run_gate()
        self.assertEqual(rep.fails, [], rep.fails)
        self.assertTrue(any('nobody has followed' in w for w in rep.warns))

    def test_the_guide_opens_with_an_executive_summary_and_states_its_verification(self):
        self.write_guide()
        body = (self.base / 'RECONSTRUCT.md').read_text()
        self.assertEqual([ln for ln in body.splitlines() if ln.startswith('## ')][0], '## Executive summary')
        self.assertIn('## Verification status', body)
        self.assertIn('Replay', body)
        self.assertIn('no person has followed these steps yet', body)
        self.assertIn('### S002 — Add the block with its real size', body)
        self.assertIn('| Dimensions | 1 x 1 x 1 m |', body)
        self.assertIn('Credit C1', body)

    def test_the_guide_without_an_executive_summary_fails(self):
        self.write_guide()
        p = self.base / 'RECONSTRUCT.md'
        p.write_text(p.read_text().replace('## Executive summary', '## Overview', 1))
        self.assertFails(self.run_gate(), 'Executive summary')

    def test_a_failed_attempt_is_kept_but_not_in_the_procedure(self):
        st = self.steps()
        st.insert(1, {'id': 'S001b', 'stage': '01-define', 'tier': 'recorded', 'excluded_from_procedure': True,
                      'goal': 'x', 'why': 'y', 'operation': {'python': {'ref': 'tape/live.jsonl#2'}, 'gui': []},
                      'result': {'reply': 'Error'}, 'evidence': [{'path': 'tape/live.jsonl', 'seq': 2}]})
        st[2]['correction'] = {'of': 'S001b', 'evidence': 'tape/live.jsonl#2: Error executing code'}
        self.save(steps=st)
        self.write_guide()
        body = (self.base / 'RECONSTRUCT.md').read_text()
        self.assertIn('This command failed', body)
        self.assertIn('## Corrections', body)
        self.assertEqual(self.run_gate().fails, [])

    def test_a_step_without_a_reason_fails(self):
        st = self.steps()
        st[1]['why'] = ''
        self.save(steps=st)
        self.assertFails(self.run_gate(), '"why"')

    def test_a_recorded_step_must_point_at_a_real_tape_line(self):
        st = self.steps()
        st[0]['operation']['python']['ref'] = 'tape/live.jsonl#99'
        self.save(steps=st)
        self.assertFails(self.run_gate(), 'no #99')

    def test_a_tape_edited_after_recording_is_caught(self):
        (self.base / 'tape/live.jsonl').write_text('{"seq": 1}\n')
        self.assertFails(self.run_gate(), 'has changed since it was recorded')

    def test_an_inspected_step_needs_a_census_not_a_story(self):
        st = self.steps()
        st[0]['tier'] = 'inspected'
        self.save(steps=st)
        self.assertFails(self.run_gate(), 'census or milestone')

    def test_a_demonstration_names_what_it_demonstrates(self):
        st = self.steps()
        st[2]['tier'] = 'demonstrated'
        self.save(steps=st)
        self.assertFails(self.run_gate(), 'demonstration_of')

    def test_inferred_steps_warn_and_cannot_be_told_as_history(self):
        st = self.steps()
        st[1]['tier'] = 'inferred'
        rec = self.rec()
        rec['film'] = {'told_as_history': ['S001', 'S002']}
        self.save(rec, st)
        rep = self.run_gate(film=True)
        self.assertFails(rep, 'film.told_as_history S002')
        self.assertTrue(any('inferred' in w for w in rep.warns))

    def test_repeated_work_needs_a_rule_and_a_table_or_a_list(self):
        st = self.steps()
        st[1]['repeats'] = {'rule': 'one per bay', 'instances': 3}
        self.save(steps=st)
        self.assertFails(self.run_gate(), 'placement table')

    def test_a_correction_needs_evidence_and_a_target(self):
        st = self.steps()
        st[2]['correction'] = {'of': 'S404', 'evidence': ''}
        self.save(steps=st)
        rep = self.run_gate()
        self.assertFails(rep, 'correction.of')
        self.assertFails(rep, 'evidence that prompted')

    def test_an_outside_asset_must_be_credited(self):
        st = self.steps()
        st[2]['uses_external_asset'] = {'name': 'x', 'credit_id': 'C9'}
        self.save(steps=st)
        self.assertFails(self.run_gate(), 'credit')

    def test_a_scripted_step_with_no_interface_route_must_say_why(self):
        st = self.steps()
        st[1]['operation']['gui'] = []
        self.save(steps=st)
        self.assertFails(self.run_gate(), 'interface route')
        st[1]['operation']['no_gui_reason'] = 'bulk placement from a table: use the script'
        self.save(steps=st)
        self.assertEqual(self.run_gate().fails, [])

    def test_unmapped_lines_and_unwritten_judgment_fail_only_the_final(self):
        st = self.steps()
        st[1]['operation']['gui'] = ['UNMAPPED: bpy.ops.foo.bar()  [operator not in gui_map]']
        st[2]['needs_author'] = ['why']
        self.save(steps=st)
        self.write_guide()
        self.assertEqual(self.run_gate().fails, [])
        rep = self.run_gate(final=True)
        self.assertFails(rep, 'UNMAPPED')
        self.assertFails(rep, 'drafted fields')

    def test_every_milestone_must_show_the_same_comparison_views(self):
        rec = self.rec()
        rec['comparison_views'] = ['CMP_ISO', 'CMP_FRONT']
        self.save(rec)
        self.assertFails(self.run_gate(), 'missing comparison view CMP_FRONT')

    def test_a_view_changed_after_rendering_is_caught(self):
        (self.base / 'milestones/04-blockout/views/CMP_ISO.png').write_bytes(b'tampered')
        self.assertFails(self.run_gate(), 'has changed since it was rendered')

    def test_the_last_milestone_must_be_the_delivered_model(self):
        m = self.base / 'milestones/08-materials/milestone.json'
        d = json.loads(m.read_text())
        d['census_signature'] = 'd' * 64
        m.write_text(json.dumps(d))
        self.assertFails(self.run_gate(), 'not the delivered model')

    def test_a_failed_replay_blocks_and_a_pending_one_blocks_the_final(self):
        rec = self.rec()
        rec['reconstruction']['replay'] = {'status': 'fail'}
        self.save(rec)
        self.assertFails(self.run_gate(), 'did not reproduce')
        rec['reconstruction']['replay'] = {'status': 'pending'}
        self.save(rec)
        self.write_guide()
        self.assertEqual(self.run_gate().fails, [])
        self.assertFails(self.run_gate(final=True), 'nothing shows this record rebuilds')
        rec['reconstruction']['by_hand'] = {'status': 'done', 'by': 'Bear', 'date': '2026-10-18', 'module': 'the block'}
        self.save(rec)
        self.write_guide()
        self.assertEqual(self.run_gate(final=True).fails, [])

    def test_a_passing_replay_must_have_made_the_delivered_signature(self):
        rec = self.rec()
        rec['reconstruction']['replay']['census_signature'] = 'e' * 64
        self.save(rec)
        self.assertFails(self.run_gate(), 'census signature')

    def test_a_stage_that_goes_backwards_must_be_a_revisit_or_a_correction(self):
        st = self.steps()
        st.append({**copy.deepcopy(st[0]), 'id': 'S004'})
        self.save(steps=st)
        self.assertFails(self.run_gate(), 'revisit')
        st[3]['revisit'] = True
        self.save(steps=st)
        self.assertFalse(any('revisit' in f for f in self.run_gate().fails))

    def test_the_model_needs_a_hash_a_signature_and_a_builder(self):
        rec = self.rec()
        rec['model']['sha256'] = 'x'
        rec['model']['built_by'] = []
        del rec['model']['census_signature']
        self.save(rec)
        rep = self.run_gate()
        for needle in ('model.sha256', 'model.built_by', 'model.census_signature'):
            self.assertFails(rep, needle)

    def test_a_recorded_reveal_must_follow_the_recorded_steps_in_order(self):
        order = {'order_source': 'recorded', 'items': [
            {'label': 'paint', 'objects': ['A'], 'start': 1, 'duration': 5, 'step': 'S003'},
            {'label': 'block', 'objects': ['B'], 'start': 6, 'duration': 5, 'step': 'S002'}]}
        (self.base / 'order.json').write_text(json.dumps(order))
        rec = self.rec()
        rec['film'] = {'reveals': [{'order': 'order.json'}]}
        self.save(rec)
        self.assertFails(self.run_gate(), 'not the recorded order')
        order['items'][0]['step'], order['items'][1]['step'] = 'S002', 'S003'
        (self.base / 'order.json').write_text(json.dumps(order))
        self.assertEqual([f for f in self.run_gate().fails if 'reveals' in f], [])
        order['items'][1]['step'] = 'S404'
        (self.base / 'order.json').write_text(json.dumps(order))
        self.assertFails(self.run_gate(), 'not a step')

    def test_an_explanatory_reveal_must_be_labelled_in_the_film(self):
        (self.base / 'order.json').write_text(json.dumps({'order_source': 'explanatory', 'items': [
            {'label': 'walls', 'objects': ['W'], 'start': 1, 'duration': 5}]}))
        rec = self.rec()
        rec['film'] = {'reveals': [{'order': 'order.json'}]}
        self.save(rec)
        self.assertFails(self.run_gate(), 'the film must say so')
        rec['film']['reveals'][0]['labelled_in_film'] = True
        self.save(rec)
        self.assertEqual([f for f in self.run_gate().fails if 'reveals' in f], [])

    def test_a_reveal_with_no_stated_order_source_fails(self):
        (self.base / 'order.json').write_text(json.dumps({'items': []}))
        rec = self.rec()
        rec['film'] = {'reveals': [{'order': 'order.json'}]}
        self.save(rec)
        self.assertFails(self.run_gate(), 'order_source')

    @unittest.skipUnless(Path(BLENDER).exists(), 'requires Blender')
    def test_recensus_catches_a_model_that_changed_after_the_record(self):
        blend = self.tmp / 'final.blend'
        script = self.tmp / 'mk.py'
        script.write_text(BUILD_SCRIPT)
        blender(None, script, '--', str(blend))
        out = self.tmp / 'c.json'
        blender(blend, SCRIPTS / 'census.py', '--', 'census', '--out', str(out))
        c = json.loads(out.read_text())
        rec = self.rec()
        rec['model'].update({'path': str(blend), 'sha256': sha(blend.read_bytes()), 'census_signature': c['signature']})
        rec['reconstruction']['replay']['census_signature'] = c['signature']
        for stage in ('04-blockout', '08-materials'):
            m = self.base / 'milestones' / stage / 'milestone.json'
            d = json.loads(m.read_text())
            d['census_signature'] = c['signature']
            m.write_text(json.dumps(d))
        self.save(rec)
        self.write_guide()
        self.assertEqual(self.run_gate(do_recensus=True).fails, [])
        rec['model']['census_signature'] = 'f' * 64
        rec['reconstruction']['replay']['census_signature'] = 'f' * 64
        self.save(rec)
        rep = self.run_gate(do_recensus=True)
        self.assertFails(rep, 'the file now has signature')


if __name__ == '__main__':
    unittest.main()
