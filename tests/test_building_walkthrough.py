"""Tests for the building-walkthrough skill: the contract gate (pure Python) and the Blender
camera rig / route checker (real Blender, skipped when it is not installed).

The Blender fixtures are a synthetic two-room test building, never presented as a real model."""
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / 'skills/make/building-walkthrough/scripts'
BLENDER = os.environ.get('BLENDER') or '/Applications/Blender.app/Contents/MacOS/Blender'


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


gate = load('walkthrough_gate', 'verify_walkthrough.py')
M = 'b' * 64


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def good_route():
    return {'schema_version': 1, 'fps': 24, 'shots': [
        {'id': 'S01', 'type': 'walk', 'frames': [1, 192]},
        {'id': 'S02', 'type': 'still', 'frames': [193, 288]},
        {'id': 'S03', 'type': 'walk', 'frames': [289, 480]}]}


def good_doc():
    return {
        'schema_version': 1, 'mode': 'building', 'title': 'A walk through the test building',
        'model': {'name': 'test-building', 'path': '/nonexistent/model.blend', 'sha256': M,
                  'blender': '5.1.2', 'status': 'interpretive', 'card': 'MODEL-CARD.md'},
        'brief': {'idea': 'Two rooms joined by one doorway.', 'audience': 'students',
                  'variant': 'midday', 'viewer_height_m': 1.6},
        'disclosure': {'shot': 'S01', 'text': 'This is a test fixture, a model of nothing real, '
                                              'built only to try the gates.'},
        'departures': [{'id': 'X1', 'what': 'no furniture', 'effect': 'scale cues are missing',
                        'disclosed_in': 'S01'}],
        'looks': {'L1': {'name': 'overcast', 'time': '12:00'}, 'L2': {'name': 'dusk', 'time': '18:30'}},
        'route': {'file': 'route.json', 'report': 'route_report.json'},
        'shots': [
            {'id': 'S01', 'section': 'entrance', 'purpose': 'orientation', 'framing': 'wide',
             'look': 'L1', 'reveals': 'the doorway is the only way through',
             'narration': {'source': 'model', 'line': 'One doorway joins the two rooms.',
                           'evidence': 'survey.geometry.size'}},
            {'id': 'S02', 'section': 'main', 'purpose': 'scale', 'framing': 'medium', 'look': 'L1',
             'reveals': 'the room is eight metres wide',
             'scale_reference': {'kind': 'human', 'size_m': 1.8}},
            {'id': 'S03', 'section': 'closing', 'purpose': 'connection', 'framing': 'wide',
             'look': 'L1', 'reveals': 'the second room is a dead end',
             'narration': {'source': 'world', 'line': 'Test fixtures are built to be thrown away.',
                           'fact': 'F01'}}],
        'budget': {'engine': 'CYCLES', 'samples': 64, 'resolution': [1920, 1080], 'where': 'mac',
                   'samples_measured': [{'kind': 'interior', 'sec_per_frame': 20},
                                        {'kind': 'exterior', 'sec_per_frame': 12},
                                        {'kind': 'detail', 'sec_per_frame': 30}]},
        'checks': {'orientation_test': 'pending', 'promise_check': 'pending'},
    }


class GateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)

    def write(self, doc=None, route=None, report=None, factcheck=None, card=True):
        doc = doc or good_doc()
        route = route or good_route()
        (self.tmp / 'route.json').write_text(json.dumps(route))
        if report is None:
            report = {'route_sha256': sha(self.tmp / 'route.json'), 'model': {'sha256': M},
                      'ok': True, 'fail_count': 0, 'violations': [], 'fps': 24,
                      'shots': [{'id': s['id'], 'checked': True} for s in route['shots']]}
        (self.tmp / 'route_report.json').write_text(json.dumps(report))
        (self.tmp / 'FACTCHECK.md').write_text(factcheck if factcheck is not None else
            '| # | Beat | Claim | Verdict | Source | Fix |\n|---|---|---|---|---|---|\n'
            '| F01 | S03 | fixtures are disposable | VERIFIED | a source | |\n')
        if card:
            (self.tmp / 'MODEL-CARD.md').write_text('# card')
        p = self.tmp / 'walkthrough.json'
        p.write_text(json.dumps(doc))
        return p

    def run_gate(self, doc=None, **kw):
        final = kw.pop('final', False)
        req = kw.pop('require_human', False)
        p = self.write(doc, **kw)
        return gate.verify(p, final=final, require_human=req, hash_model=False)

    def assertFails(self, rep, needle):
        self.assertTrue(any(needle in f for f in rep.fails), f'no failure containing {needle!r}: {rep.fails}')

    def test_valid_passes_with_pending_human_tests_as_warnings(self):
        rep = self.run_gate()
        self.assertEqual(rep.fails, [], rep.fails)
        self.assertTrue(any('NOT audience-tested' in w for w in rep.warns))

    def test_pending_human_tests_fail_the_final_handoff(self):
        rep = self.run_gate(final=True)
        self.assertFails(rep, 'still pending')

    def test_finished_human_test_needs_a_name_and_date(self):
        d = good_doc()
        d['checks'] = {'orientation_test': {'status': 'done'}, 'promise_check': 'pending'}
        self.assertFails(self.run_gate(d), 'names who did it')

    def test_shot_without_a_job_fails(self):
        d = good_doc()
        d['shots'][1]['reveals'] = ''
        self.assertFails(self.run_gate(d), 'reveals')

    def test_closing_must_be_last(self):
        d = good_doc()
        d['shots'][1], d['shots'][2] = d['shots'][2], d['shots'][1]
        self.assertFails(self.run_gate(d), 'closing')

    def test_route_that_doubles_back_fails(self):
        d = good_doc()
        d['shots'][0]['section'] = 'main'
        d['shots'][1]['section'] = 'entrance'
        self.assertFails(self.run_gate(d), 'doubles back')

    def test_route_failure_blocks_the_film(self):
        rep = self.run_gate(report={'route_sha256': 'x', 'ok': False, 'fail_count': 1, 'fps': 24,
                                    'violations': [{'shot': 'S01', 'severity': 'fail', 'rule': 'clearance',
                                                    'frame': 3, 'message': 'wall'}],
                                    'shots': []})
        self.assertFails(rep, 'route failure')
        self.assertFails(rep, 'different route.json')

    def test_stale_route_report_fails(self):
        p = self.write()
        r = json.loads((self.tmp / 'route.json').read_text())
        r['shots'][0]['frames'] = [1, 200]
        (self.tmp / 'route.json').write_text(json.dumps(r))
        rep = gate.verify(p, hash_model=False)
        self.assertFails(rep, 'different route.json')

    def test_line_too_long_for_its_shot_fails(self):
        d = good_doc()
        d['shots'][1]['narration'] = {'source': 'model', 'evidence': 'survey',
                                      'line': ' '.join(['word'] * 30)}
        self.assertFails(self.run_gate(d), 'needs ~')

    def test_world_fact_must_be_verified(self):
        fc = '| # | b | c | Verdict | Source |\n|--|--|--|--|--|\n| F01 | S03 | c | UNVERIFIED | s |\n'
        self.assertFails(self.run_gate(factcheck=fc), 'not verified')
        self.assertFails(self.run_gate(factcheck='| # | b | c | Verdict | Source |\n'), 'no row')

    def test_model_claim_needs_evidence(self):
        d = good_doc()
        d['shots'][0]['narration'].pop('evidence')
        self.assertFails(self.run_gate(d), 'evidence')

    def test_undeclared_light_change_fails(self):
        d = good_doc()
        d['shots'][1]['look'] = 'L2'
        d['shots'][1]['section'] = 'entrance'
        self.assertFails(self.run_gate(d), 'look_change')

    def test_declared_light_change_passes(self):
        d = good_doc()
        d['shots'][2]['look'] = 'L2'
        d['shots'][2]['look_change'] = {'reason': 'the day ends as the viewer leaves the building'}
        rep = self.run_gate(d)
        self.assertFalse(any('look' in f for f in rep.fails), rep.fails)

    def test_disclosure_must_open_the_film(self):
        d = good_doc()
        d['disclosure']['shot'] = 'S03'
        self.assertFails(self.run_gate(d), 'first two shots')

    def test_departure_must_be_disclosed_in_a_real_shot(self):
        d = good_doc()
        d['departures'][0]['disclosed_in'] = 'S99'
        self.assertFails(self.run_gate(d), 'disclosed_in')

    def test_interpretive_model_with_no_departures_warns(self):
        d = good_doc()
        d['departures'] = []
        self.assertTrue(any('not been examined' in w for w in self.run_gate(d).warns))

    def test_numbered_title_and_narration_fail(self):
        d = good_doc()
        d['title'] = 'Walking the building, part 2'
        self.assertFails(self.run_gate(d), 'never numbered')
        d = good_doc()
        d['shots'][0]['narration']['line'] = 'This is video 3 of 9.'
        self.assertFails(self.run_gate(d), 'never numbered')

    def test_evaluative_adjective_warns(self):
        d = good_doc()
        d['shots'][0]['narration']['line'] = 'A stunning doorway joins the rooms.'
        self.assertTrue(any('evaluative' in w for w in self.run_gate(d).warns))

    def test_short_moving_shot_fails(self):
        r = good_route()
        r['shots'][0]['frames'] = [1, 48]
        self.assertFails(self.run_gate(route=r), 'cannot take the space in')

    def test_budget_needs_three_timed_frames_for_the_final(self):
        d = good_doc()
        d['budget']['samples_measured'] = d['budget']['samples_measured'][:1]
        self.assertFails(self.run_gate(d, final=True), 'at least three')

    def test_long_render_on_the_mac_warns(self):
        d = good_doc()
        d['budget']['samples_measured'] = [{'kind': 'interior', 'sec_per_frame': 400},
                                           {'kind': 'exterior', 'sec_per_frame': 400},
                                           {'kind': 'detail', 'sec_per_frame': 400}]
        rep = self.run_gate(d)
        self.assertTrue(any('Explorer' in w for w in rep.warns), rep.warns)

    def test_missing_model_card_fails(self):
        self.assertFails(self.run_gate(card=False), 'MODEL-CARD')

    def test_scale_shot_needs_a_reference(self):
        d = good_doc()
        d['shots'][1].pop('scale_reference')
        self.assertFails(self.run_gate(d), 'scale_reference')

    def test_four_framings_in_a_row_warn(self):
        d, r = good_doc(), good_route()
        for i in range(4, 7):
            d['shots'].insert(-1, {**copy.deepcopy(d['shots'][0]), 'id': f'S0{i}', 'section': 'main',
                                   'reveals': f'detail number {i}', 'narration': {'source': 'none'}})
            r['shots'].insert(-1, {'id': f'S0{i}', 'type': 'walk', 'frames': [481 + (i - 4) * 192, 672 + (i - 4) * 192]})
        r['shots'][-1]['frames'] = [1057, 1248]
        d['shots'][1]['framing'] = 'wide'
        rep = self.run_gate(d, route=r)
        self.assertTrue(any('in a row' in w for w in rep.warns), rep.warns)

    def test_asset_mode_requires_establish_scale_closing(self):
        d = good_doc()
        d['mode'] = 'asset'
        rep = self.run_gate(d)
        self.assertFails(rep, 'needs a "establish" section')

    def test_model_hash_is_rechecked_when_the_file_exists(self):
        d = good_doc()
        blend = self.tmp / 'm.blend'
        blend.write_bytes(b'not really a blend')
        d['model']['path'] = str(blend)
        p = self.write(d)
        self.assertFails(gate.verify(p, hash_model=True), 'has changed')
        d['model']['sha256'] = sha(blend)
        p = self.write(d)
        rep = gate.verify(p, hash_model=True)
        self.assertFalse(any('has changed' in f for f in rep.fails), rep.fails)


@unittest.skipUnless(Path(BLENDER).exists(), 'requires Blender')
class BlenderRigTests(unittest.TestCase):
    """Real Blender runs: rig a route into a known test building and measure it."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp())
        cls.model = cls.tmp / 'model.blend'
        cls.blender(None, SCRIPTS / 'make_test_model.py', '--', str(cls.model))
        cls.route = {'schema_version': 1, 'fps': 24, 'defaults': {'lens_mm': 28}, 'shots': [
            {'id': 'S01', 'type': 'walk', 'frames': [1, 360], 'ease': 'linear',
             'waypoints': [[1.8, -7, 1.6], [1.8, -4, 1.6], [1.4, -2.5, 1.6], [0.3, -1, 1.6],
                           [0, 0.5, 1.6], [0, 3, 1.6], [0, 6.5, 1.6]], 'look': {'mode': 'travel'}},
            {'id': 'S02', 'type': 'still', 'frames': [361, 456], 'position': [0, 6, 1.6],
             'look': {'mode': 'target', 'point': [0, -6, 1.2]}},
            {'id': 'S03', 'type': 'orbit', 'frames': [457, 936], 'center': [0, -4, 0], 'radius_m': 3.0,
             'height_m': 1.4, 'degrees': 360, 'look_height_m': 0.9, 'purpose': 'feature'}]}
        cls.good = cls.rig_and_check(cls.route, 'good')

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, True)

    @classmethod
    def blender(cls, blend, script, *args):
        cmd = [BLENDER, '-b'] + ([str(blend)] if blend else ['--factory-startup']) + \
              ['--python', str(script)] + list(args)
        return subprocess.run(cmd, capture_output=True, text=True, timeout=240)

    @classmethod
    def rig_and_check(cls, route, tag, defect=None, blend=None):
        rp = cls.tmp / f'route_{tag}.json'
        rp.write_text(json.dumps(route))
        rigged = cls.tmp / f'rigged_{tag}.blend'
        p = cls.blender(blend or cls.model, SCRIPTS / 'camera_rig.py', '--', str(rp), '--out', str(rigged))
        assert p.returncode == 0 and rigged.exists(), p.stdout[-800:] + p.stderr[-800:]
        if defect:
            dscript = cls.tmp / f'defect_{tag}.py'
            dscript.write_text(defect)
            bad = cls.tmp / f'bad_{tag}.blend'
            p = cls.blender(rigged, dscript, '--', str(bad))
            assert p.returncode == 0 and bad.exists(), p.stdout[-800:]
            rigged = bad
        out = cls.tmp / f'report_{tag}.json'
        p = cls.blender(rigged, SCRIPTS / 'route_check.py', '--', 'check', str(rp), '--out', str(out))
        return {'code': p.returncode, 'report': json.loads(out.read_text()), 'rigged': rigged,
                'stdout': p.stdout}

    def rules(self, result):
        return {(v['rule'], v['severity']) for v in result['report']['violations']}

    def test_the_good_route_passes_with_measured_constant_speed(self):
        r = self.good
        self.assertEqual(r['code'], 0, r['stdout'][-600:])
        s1 = r['report']['shots'][0]
        self.assertAlmostEqual(s1['speed_mps']['min'], s1['speed_mps']['max'], delta=0.02)
        self.assertAlmostEqual(s1['eye_height_m']['mean'], 1.6, delta=0.01)
        self.assertLess(s1['roll_deg']['max_abs'], 0.01)
        self.assertGreater(s1['clearance_m']['min'], 0.45)
        self.assertEqual(r['report']['shots'][1]['speed_mps']['max'], 0.0)

    def test_orbit_has_constant_speed_and_is_not_held_to_eye_height(self):
        s3 = self.good['report']['shots'][2]
        self.assertAlmostEqual(s3['speed_mps']['min'], s3['speed_mps']['max'], delta=0.02)
        self.assertNotIn(('eye_height', 'fail'), self.rules(self.good))

    def test_a_path_through_a_wall_fails_clearance(self):
        route = copy.deepcopy(self.route)
        route['shots'] = route['shots'][:1]
        route['shots'][0]['waypoints'] = [[-2, -6, 1.6], [-2, 6, 1.6]]
        r = self.rig_and_check(route, 'wall')
        self.assertEqual(r['code'], 1)
        self.assertIn(('clearance', 'fail'), self.rules(r))

    def test_too_fast_fails_speed(self):
        route = copy.deepcopy(self.route)
        route['shots'] = route['shots'][:1]
        route['shots'][0]['frames'] = [1, 96]
        route['shots'][0]['waypoints'] = [[2, -7, 1.6], [2, 6, 1.6]]
        r = self.rig_and_check(route, 'fast')
        self.assertIn(('speed', 'fail'), self.rules(r))

    def test_wrong_eye_height_fails(self):
        route = copy.deepcopy(self.route)
        route['shots'] = route['shots'][:1]
        route['shots'][0]['waypoints'] = [[w[0], w[1], 1.2] for w in route['shots'][0]['waypoints']]
        r = self.rig_and_check(route, 'low')
        self.assertIn(('eye_height', 'fail'), self.rules(r))

    def test_a_rolled_camera_fails(self):
        r = self.rig_and_check(
            self.route, 'roll',
            defect='import bpy, sys, math\n'
                   'bpy.data.objects["CAM_S01"].rotation_euler.y += math.radians(4)\n'
                   'bpy.ops.wm.save_as_mainfile(filepath=sys.argv[sys.argv.index("--")+1], copy=True)\n')
        self.assertIn(('roll', 'fail'), self.rules(r))

    def test_a_whip_pan_fails_yaw_rate(self):
        """A camera that passes one metre from the point it is looking at swings round fast."""
        route = copy.deepcopy(self.route)
        route['shots'] = route['shots'][:1]
        route['shots'][0].update({'frames': [1, 104], 'waypoints': [[1, 1, 1.6], [1, 7, 1.6]],
                                  'look': {'mode': 'target', 'point': [0, 4, 1.6]}})
        r = self.rig_and_check(route, 'whip')
        rules = self.rules(r)
        self.assertIn(('yaw_rate', 'fail'), rules)
        self.assertNotIn(('speed', 'fail'), rules)

    def test_passing_over_an_obstacle_is_caught_as_a_height_fault(self):
        """The camera flew 0.6 m over the pedestal: measured height above the surface below it."""
        route = copy.deepcopy(self.route)
        route['shots'] = route['shots'][:1]
        route['shots'][0].update({'frames': [1, 120], 'smooth': False,
                                  'waypoints': [[2, -7, 1.6], [2, -4, 1.6], [-2, -4, 1.6]]})
        r = self.rig_and_check(route, 'over')
        self.assertIn(('eye_height', 'fail'), self.rules(r))

    def test_missing_camera_marker_fails(self):
        r = self.rig_and_check(
            self.route, 'nomarker',
            defect='import bpy, sys\nbpy.context.scene.timeline_markers.clear()\n'
                   'bpy.ops.wm.save_as_mainfile(filepath=sys.argv[sys.argv.index("--")+1], copy=True)\n')
        self.assertIn(('marker_missing', 'fail'), self.rules(r))
        self.assertIn(('camera_not_active', 'fail'), self.rules(r))

    def test_a_moving_still_fails(self):
        r = self.rig_and_check(
            self.route, 'drift',
            defect='import bpy, sys\nc = bpy.data.objects["CAM_S02"]\n'
                   'c.location.x = 0.0\nc.keyframe_insert("location", frame=361)\n'
                   'c.location.x = 0.2\nc.keyframe_insert("location", frame=456)\n'
                   'bpy.ops.wm.save_as_mainfile(filepath=sys.argv[sys.argv.index("--")+1], copy=True)\n')
        self.assertIn(('still_moves', 'fail'), self.rules(r))

    def test_rigging_twice_makes_the_same_scene(self):
        again = self.tmp / 'again.blend'
        rp = self.tmp / 'route_good.json'
        p = self.blender(self.good['rigged'], SCRIPTS / 'camera_rig.py', '--', str(rp), '--out', str(again))
        self.assertEqual(p.returncode, 0, p.stdout[-500:])
        probe = self.tmp / 'count.py'
        probe.write_text('import bpy\nprint("COUNT", len(bpy.data.objects), len(bpy.data.cameras), '
                         'len(bpy.data.curves), len(bpy.context.scene.timeline_markers))\n')
        a = self.blender(self.good['rigged'], probe).stdout
        b = self.blender(again, probe).stdout
        pick = lambda t: [l for l in t.splitlines() if l.startswith('COUNT')]  # noqa: E731
        self.assertEqual(pick(a), pick(b))

    def test_refuses_to_overwrite_the_model_it_opened(self):
        rp = self.tmp / 'route_good.json'
        p = self.blender(self.model, SCRIPTS / 'camera_rig.py', '--', str(rp), '--out', str(self.model))
        self.assertNotEqual(p.returncode, 0)

    def test_survey_reports_the_known_geometry(self):
        out = self.tmp / 'survey.json'
        self.blender(self.model, SCRIPTS / 'route_check.py', '--', 'survey', '--out', str(out))
        s = json.loads(out.read_text())
        self.assertEqual(s['geometry']['mesh_instances'], 10)
        self.assertEqual(s['geometry']['triangles_evaluated'], 120)
        self.assertEqual(s['geometry']['size'], [8.4, 16.4, 3.4])
        self.assertEqual(s['scene']['unit_system'], 'METRIC')

    def test_rig_and_gate_agree_on_a_good_film(self):
        """The measured report feeds the contract gate end to end."""
        d = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, d, True)
        d = Path(d)
        shutil.copy(self.tmp / 'route_good.json', d / 'route.json')
        shutil.copy(self.tmp / 'report_good.json', d / 'route_report.json')
        (d / 'MODEL-CARD.md').write_text('# card')
        (d / 'FACTCHECK.md').write_text('| # | b | c | Verdict | Source |\n|--|--|--|--|--|\n| F01 | S03 | c | VERIFIED | s |\n')
        doc = good_doc()
        doc['model']['sha256'] = self.good['report']['model']['sha256']
        doc['shots'][1]['framing'] = 'medium'
        doc['shots'][2]['section'] = 'closing'
        doc['shots'][2]['purpose'] = 'feature'
        (d / 'walkthrough.json').write_text(json.dumps(doc))
        rep = gate.verify(d / 'walkthrough.json', hash_model=False)
        self.assertEqual(rep.fails, [], rep.fails)


if __name__ == '__main__':
    unittest.main()
