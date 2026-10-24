"""Measure a Blender camera route. Runs INSIDE Blender, in the background:

  blender -b MODEL.blend --python route_check.py -- survey [--out survey.json]
  blender -b MODEL.blend --python route_check.py -- check ROUTE.json --out route_report.json
        [--exclude-collection NAME ...] [--ignore-object NAME ...]

`survey` describes the model (bounds, units, triangles, cameras, lights, embedded scripts,
missing or absolute texture paths). `check` steps every frame of every shot in ROUTE.json
and measures what the camera actually does: speed, turn rate, roll, pitch, height above the
floor, distance to the nearest geometry, whether the right camera is bound to the shot.

It measures the file as it is opened (frame by frame, evaluated). It does NOT see anything
that moves independently of the camera (doors, crowds, physics), anything hidden from the
viewport evaluation, or what a person feels watching. Clearance is a ray test from the camera
point, not a volume test. Treat a pass as "no gross fault found", never as "good".
Exit status 1 when any `fail` violation exists.
"""
import argparse
import hashlib
import json
import math
import os
import sys

import bpy
import numpy as np
from mathutils import Vector
from mathutils.bvhtree import BVHTree

DEFAULT_LIMITS = {
    'eye_height_m': 1.6,        # standing adult; a game's player controller overrides this
    'eye_height_tol_m': 0.10,
    'max_speed_mps': 1.5,       # a brisk walk is ~1.4 m/s; films usually go slower
    'max_yaw_dps': 30.0,
    'roll_tol_deg': 0.5,
    'pitch_warn_deg': 8.0,
    'min_clearance_m': 0.30,
    'max_accel_mps2': 3.0,
    'still_tol_m': 0.001,
}
# Per shot type overrides on top of DEFAULT_LIMITS (an aerial or an orbit is not a walk).
TYPE_LIMITS = {
    'walk': {},
    'still': {},
    'aerial': {'max_speed_mps': 8.0, 'pitch_warn_deg': 90.0, 'check_eye_height': False,
               'min_clearance_m': 1.0},
    'crane': {'max_speed_mps': 3.0, 'pitch_warn_deg': 90.0, 'check_eye_height': False},
    'orbit': {'max_speed_mps': 6.0, 'pitch_warn_deg': 90.0, 'check_eye_height': False},
}
SHOT_TYPES = tuple(TYPE_LIMITS)


def script_args():
    argv = sys.argv
    return argv[argv.index('--') + 1:] if '--' in argv else []


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def r(x, n=4):
    return None if x is None else round(float(x), n)


def vec(v):
    return [r(v[0]), r(v[1]), r(v[2])]


def evaluated_instances(exclude_collections=(), ignore_objects=()):
    """Yield (original_object, world_vertices Nx3, triangles Mx3) for every visible,
    renderable, evaluated mesh instance (collection instances included)."""
    depsgraph = bpy.context.evaluated_depsgraph_get()
    exclude_collections, ignore_objects = set(exclude_collections), set(ignore_objects)
    for inst in depsgraph.object_instances:
        ob = inst.object
        if ob.type != 'MESH':
            continue
        orig = ob.original
        if orig.name in ignore_objects or orig.hide_render:
            continue
        if any(c.name in exclude_collections for c in orig.users_collection):
            continue
        mesh = ob.data
        if len(mesh.polygons) == 0:
            continue
        mesh.calc_loop_triangles()
        nv, nt = len(mesh.vertices), len(mesh.loop_triangles)
        co = np.empty(nv * 3, dtype=np.float64)
        mesh.vertices.foreach_get('co', co)
        tri = np.empty(nt * 3, dtype=np.int32)
        mesh.loop_triangles.foreach_get('vertices', tri)
        m = np.array(inst.matrix_world, dtype=np.float64)
        world = co.reshape(-1, 3) @ m[:3, :3].T + m[:3, 3]
        yield orig, world, tri.reshape(-1, 3)


def build_bvh(exclude_collections, ignore_objects):
    verts, tris, offset, n_obj = [], [], 0, 0
    for _orig, world, tri in evaluated_instances(exclude_collections, ignore_objects):
        verts.append(world)
        tris.append(tri + offset)
        offset += len(world)
        n_obj += 1
    if not verts:
        return None, 0, 0
    v = np.vstack(verts)
    t = np.vstack(tris)
    return BVHTree.FromPolygons(v.tolist(), t.tolist()), n_obj, len(t)


def file_facts():
    path = bpy.data.filepath
    return {'path': path, 'sha256': sha256_file(path) if path and os.path.exists(path) else None,
            'blender': bpy.app.version_string}


# ---------------------------------------------------------------- survey

def survey(exclude_collections=(), ignore_objects=()):
    sc = bpy.context.scene
    lo, hi = np.full(3, np.inf), np.full(3, -np.inf)
    per_coll, tri_total, n_inst = {}, 0, 0
    for orig, world, tri in evaluated_instances(exclude_collections, ignore_objects):
        n_inst += 1
        tri_total += len(tri)
        wmin, wmax = world.min(axis=0), world.max(axis=0)
        lo, hi = np.minimum(lo, wmin), np.maximum(hi, wmax)
        for c in orig.users_collection:
            b = per_coll.setdefault(c.name, [np.full(3, np.inf), np.full(3, -np.inf), 0])
            b[0], b[1], b[2] = np.minimum(b[0], wmin), np.maximum(b[1], wmax), b[2] + 1
    have = bool(n_inst)
    missing, absolute = [], []
    for img in bpy.data.images:
        if img.source == 'FILE' and img.filepath:
            raw = img.filepath
            if not raw.startswith('//'):
                absolute.append(raw)
            if not os.path.exists(bpy.path.abspath(raw)) and not img.packed_file:
                missing.append(raw)
    for lib in bpy.data.libraries:
        if not os.path.exists(bpy.path.abspath(lib.filepath)):
            missing.append(lib.filepath)
    world = sc.world
    return {
        'file': file_facts(),
        'scene': {'name': sc.name, 'unit_system': sc.unit_settings.system,
                  'scale_length': sc.unit_settings.scale_length,
                  'length_unit': sc.unit_settings.length_unit,
                  'fps': sc.render.fps / sc.render.fps_base,
                  'frame_range': [sc.frame_start, sc.frame_end],
                  'engine': sc.render.engine,
                  'resolution': [sc.render.resolution_x, sc.render.resolution_y,
                                 sc.render.resolution_percentage],
                  'view_transform': sc.view_settings.view_transform,
                  'look': sc.view_settings.look},
        'geometry': {'mesh_instances': n_inst, 'triangles_evaluated': tri_total,
                     'bounds_min': vec(lo) if have else None,
                     'bounds_max': vec(hi) if have else None,
                     'size': vec(hi - lo) if have else None},
        'collections': [{'name': n, 'instances': b[2], 'bounds_min': vec(b[0]),
                         'bounds_max': vec(b[1])} for n, b in sorted(per_coll.items())],
        'cameras': [{'name': o.name, 'lens_mm': r(o.data.lens), 'sensor_mm': r(o.data.sensor_width),
                     'clip_start': r(o.data.clip_start), 'clip_end': r(o.data.clip_end),
                     'dof': bool(o.data.dof.use_dof)}
                    for o in bpy.data.objects if o.type == 'CAMERA'],
        'lights': [{'name': o.name, 'type': o.data.type, 'energy': r(o.data.energy)}
                   for o in bpy.data.objects if o.type == 'LIGHT'],
        'world': {'name': world.name, 'uses_nodes': bool(world.use_nodes)} if world else None,
        'markers': [{'name': m.name, 'frame': m.frame, 'camera': m.camera.name if m.camera else None}
                    for m in sc.timeline_markers],
        'embedded_scripts': [t.name for t in bpy.data.texts],
        'missing_files': sorted(set(missing)),
        'absolute_paths': sorted(set(absolute)),
    }


# ---------------------------------------------------------------- check

def probe_dirs(fwd):
    """Fixed fan of rays for clearance: 6 axes' worth of directions (4 horizontal, up, and 8
    corners) plus the view direction. The straight-down ray is the floor and is measured
    separately. Rays toward the frame edges are NOT used: walking through a doorway puts the
    jamb close to the edge of the picture without the camera being anywhere near it."""
    dirs = [Vector(d).normalized() for d in
            [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1),
             (1, 1, 1), (1, -1, 1), (-1, 1, 1), (-1, -1, 1),
             (1, 1, -1), (1, -1, -1), (-1, 1, -1), (-1, -1, -1)]]
    dirs.append(fwd.normalized())
    return dirs


def shot_limits(base, shot):
    limits = dict(DEFAULT_LIMITS)
    limits['check_eye_height'] = True
    limits.update(base)
    limits.update(TYPE_LIMITS.get(shot.get('type', 'walk'), {}))
    limits.update(shot.get('limits', {}))
    if 'eye_height_m' in shot:
        limits['eye_height_m'] = shot['eye_height_m']
    return limits


def wrap_deg(d):
    return (d + 180.0) % 360.0 - 180.0


def check_shot(sc, shot, limits, bvh, fps, violations):
    sid = shot['id']
    f0, f1 = int(shot['frames'][0]), int(shot['frames'][1])
    cam_name = shot.get('camera') or 'CAM_' + sid

    def add(sev, rule, frame, value, limit, msg):
        violations.append({'shot': sid, 'severity': sev, 'rule': rule, 'frame': frame,
                           'value': value, 'limit': limit, 'message': msg})

    cam = sc.objects.get(cam_name)
    if cam is None or cam.type != 'CAMERA':
        add('fail', 'camera_missing', f0, None, None, f'no camera object named {cam_name}')
        return {'id': sid, 'frames': [f0, f1], 'camera': cam_name, 'checked': False}

    markers = [m for m in sc.timeline_markers if m.frame == f0 and m.camera]
    if not markers:
        add('fail', 'marker_missing', f0, None, None,
            f'no timeline marker with a bound camera at frame {f0}: the render would use '
            f'whatever camera is active, not {cam_name}')
    elif all(m.camera.name != cam_name for m in markers):
        add('fail', 'marker_wrong_camera', f0, markers[0].camera.name, cam_name,
            f'the marker at frame {f0} binds {markers[0].camera.name}, not {cam_name}')

    sc.frame_set(f0)
    if sc.camera is None or sc.camera.name != cam_name:
        add('fail', 'camera_not_active', f0, sc.camera.name if sc.camera else None, cam_name,
            f'at frame {f0} the scene camera is {sc.camera.name if sc.camera else None}, not '
            f'{cam_name}: the render would film the wrong shot')

    sensor = cam.data.sensor_width
    hfov = 2.0 * math.atan(sensor / (2.0 * cam.data.lens))
    rows = []
    prev_pos = prev_speed = prev_yaw = None
    for f in range(f0, f1 + 1):
        sc.frame_set(f)
        bpy.context.view_layer.update()
        mw = cam.matrix_world
        pos = mw.translation.copy()
        q = mw.to_quaternion()
        fwd, right = q @ Vector((0, 0, -1)), q @ Vector((1, 0, 0))
        yaw = math.degrees(math.atan2(fwd.y, fwd.x))
        pitch = math.degrees(math.asin(max(-1.0, min(1.0, fwd.z))))
        roll = math.degrees(math.asin(max(-1.0, min(1.0, right.z))))
        speed = None if prev_pos is None else (pos - prev_pos).length * fps
        yaw_rate = None if prev_yaw is None else abs(wrap_deg(yaw - prev_yaw)) * fps
        accel = None if (speed is None or prev_speed is None) else (speed - prev_speed) * fps
        height = floor_hit = None
        clearance, clr_dir = None, None
        if bvh is not None:
            hit = bvh.ray_cast(pos, Vector((0, 0, -1)), 1000.0)
            if hit[0] is not None:
                height, floor_hit = pos.z - hit[0].z, hit[0].z
            best = None
            for d in probe_dirs(fwd):
                h = bvh.ray_cast(pos, d, 100.0)
                if h[0] is not None and (best is None or h[3] < best):
                    best, clr_dir = h[3], d
            clearance = best
        rows.append({'f': f, 'pos': pos, 'speed': speed, 'yaw_rate': yaw_rate, 'accel': accel,
                     'pitch': pitch, 'roll': roll, 'height': height, 'clearance': clearance})
        prev_pos, prev_speed, prev_yaw = pos, speed, yaw

    n = len(rows)
    speeds = [x['speed'] for x in rows if x['speed'] is not None]
    yaws = [x['yaw_rate'] for x in rows if x['yaw_rate'] is not None]
    accs = [abs(x['accel']) for x in rows if x['accel'] is not None]
    heights = [x['height'] for x in rows if x['height'] is not None]
    clears = [x['clearance'] for x in rows if x['clearance'] is not None]
    length = sum((rows[i]['pos'] - rows[i - 1]['pos']).length for i in range(1, n))

    if shot.get('type') == 'still':
        spread = max(((x['pos'] - rows[0]['pos']).length for x in rows), default=0.0)
        if spread > limits['still_tol_m']:
            add('fail', 'still_moves', f0, r(spread, 5), limits['still_tol_m'],
                f'a still shot moves {spread * 1000:.1f} mm')
    else:
        worst = max(rows, key=lambda x: x['speed'] or 0)
        if speeds and worst['speed'] > limits['max_speed_mps']:
            add('fail', 'speed', worst['f'], r(worst['speed']), limits['max_speed_mps'],
                f"camera reaches {worst['speed']:.2f} m/s (limit {limits['max_speed_mps']})")
        if accs and max(accs) > limits['max_accel_mps2']:
            wa = max((x for x in rows if x['accel'] is not None), key=lambda x: abs(x['accel']))
            add('warn', 'accel', wa['f'], r(abs(wa['accel'])), limits['max_accel_mps2'],
                f"speed changes by {abs(wa['accel']):.1f} m/s^2 mid-shot: a jolt (a shot that "
                f"starts or ends at rest needs an ease)")
    if yaws and max(yaws) > limits['max_yaw_dps']:
        wy = max((x for x in rows if x['yaw_rate'] is not None), key=lambda x: x['yaw_rate'])
        add('fail', 'yaw_rate', wy['f'], r(wy['yaw_rate']), limits['max_yaw_dps'],
            f"camera turns {wy['yaw_rate']:.0f} deg/s (limit {limits['max_yaw_dps']})")
    wr = max(rows, key=lambda x: abs(x['roll']))
    if abs(wr['roll']) > limits['roll_tol_deg']:
        add('fail', 'roll', wr['f'], r(wr['roll'], 2), limits['roll_tol_deg'],
            f"camera is rolled {wr['roll']:.2f} deg: verticals will lean")
    wp = max(rows, key=lambda x: abs(x['pitch']))
    if abs(wp['pitch']) > limits['pitch_warn_deg']:
        add('warn', 'pitch', wp['f'], r(wp['pitch'], 2), limits['pitch_warn_deg'],
            f"camera pitched {wp['pitch']:.1f} deg: verticals converge (use lens shift to "
            f"frame, or declare the shot as looking up/down on purpose)")
    if limits['check_eye_height'] and shot.get('type') in ('walk', 'still', None):
        for x in rows:
            if x['height'] is None:
                add('fail', 'no_floor', x['f'], None, None, 'no geometry below the camera')
                break
        bad = [x for x in rows if x['height'] is not None
               and abs(x['height'] - limits['eye_height_m']) > limits['eye_height_tol_m']]
        if bad:
            w = max(bad, key=lambda x: abs(x['height'] - limits['eye_height_m']))
            add('fail', 'eye_height', w['f'], r(w['height'], 3), limits['eye_height_m'],
                f"camera is {w['height']:.2f} m above the surface below it (expected "
                f"{limits['eye_height_m']} +/- {limits['eye_height_tol_m']}); "
                f"{len(bad)} frame(s) outside")
    if clears:
        wc = min((x for x in rows if x['clearance'] is not None), key=lambda x: x['clearance'])
        if wc['clearance'] < limits['min_clearance_m']:
            clip = cam.data.clip_start
            sev_msg = ('inside the near clip plane: the wall will cut away'
                       if wc['clearance'] < clip else 'too close to geometry')
            add('fail', 'clearance', wc['f'], r(wc['clearance'], 3), limits['min_clearance_m'],
                f"nearest geometry {wc['clearance']:.2f} m away ({sev_msg})")
    if cam.data.dof.use_dof and shot.get('purpose') not in ('feature', 'material', 'detail'):
        add('warn', 'dof_on_route', f0, True, False,
            'depth of field is on for a shot that is not a detail or material shot')

    def stat(vals):
        return None if not vals else {'min': r(min(vals)), 'max': r(max(vals)),
                                      'mean': r(sum(vals) / len(vals))}

    return {
        'id': sid, 'type': shot.get('type', 'walk'), 'camera': cam_name, 'checked': True,
        'frames': [f0, f1], 'frame_count': n, 'duration_s': r(n / fps, 3),
        'length_m': r(length, 3),
        'lens_mm': r(cam.data.lens), 'sensor_mm': r(sensor), 'hfov_deg': r(math.degrees(hfov), 2),
        'shift_y': r(cam.data.shift_y), 'dof': bool(cam.data.dof.use_dof),
        'speed_mps': stat(speeds), 'yaw_rate_dps': stat(yaws),
        'abs_accel_mps2': {'max': r(max(accs))} if accs else None,
        'roll_deg': {'max_abs': r(max(abs(x['roll']) for x in rows), 3)},
        'pitch_deg': {'min': r(min(x['pitch'] for x in rows), 2),
                      'max': r(max(x['pitch'] for x in rows), 2)},
        'eye_height_m': stat(heights), 'clearance_m': stat(clears),
        'limits': {k: v for k, v in limits.items()},
    }


def check(route_path, exclude_collections, ignore_objects):
    with open(route_path) as fh:
        route = json.load(fh)
    sc = bpy.context.scene
    fps = route.get('fps') or (sc.render.fps / sc.render.fps_base)
    if abs(fps - sc.render.fps / sc.render.fps_base) > 1e-6:
        raise SystemExit(f'route.json fps {fps} differs from the scene fps '
                         f'{sc.render.fps / sc.render.fps_base}')
    sc.frame_set(sc.frame_start)
    bvh, n_obj, n_tri = build_bvh(exclude_collections, ignore_objects)
    base = route.get('limits', {})
    violations, shots, seen = [], [], set()
    for shot in route['shots']:
        if shot['id'] in seen:
            violations.append({'shot': shot['id'], 'severity': 'fail', 'rule': 'duplicate_id',
                               'frame': None, 'value': None, 'limit': None,
                               'message': 'shot id used twice'})
            continue
        seen.add(shot['id'])
        if shot.get('type', 'walk') not in SHOT_TYPES:
            violations.append({'shot': shot['id'], 'severity': 'fail', 'rule': 'shot_type',
                               'frame': None, 'value': shot.get('type'), 'limit': list(SHOT_TYPES),
                               'message': 'unknown shot type'})
            continue
        shots.append(check_shot(sc, shot, shot_limits(base, shot), bvh, fps, violations))
    if bvh is None:
        violations.append({'shot': None, 'severity': 'fail', 'rule': 'no_geometry', 'frame': None,
                           'value': None, 'limit': None,
                           'message': 'no renderable mesh in the model: nothing to measure against'})
    fails = [v for v in violations if v['severity'] == 'fail']
    return {
        'schema_version': 1, 'model': file_facts(), 'route': os.path.abspath(route_path),
        'route_sha256': sha256_file(route_path), 'fps': fps,
        'collision_geometry': {'mesh_instances': n_obj, 'triangles': n_tri,
                               'excluded_collections': sorted(exclude_collections),
                               'ignored_objects': sorted(ignore_objects)},
        'shots': shots, 'violations': violations,
        'ok': not fails, 'fail_count': len(fails),
        'warn_count': len(violations) - len(fails),
        'scope': 'Measured from the opened file, frame by frame. Static geometry only; '
                 'ray-based clearance; no judgment of feel, framing or pacing.',
    }


def main():
    ap = argparse.ArgumentParser(prog='route_check.py')
    sub = ap.add_subparsers(dest='cmd', required=True)
    s = sub.add_parser('survey')
    s.add_argument('--out')
    c = sub.add_parser('check')
    c.add_argument('route')
    c.add_argument('--out')
    for p in (s, c):
        p.add_argument('--exclude-collection', action='append', default=[])
        p.add_argument('--ignore-object', action='append', default=[])
    a = ap.parse_args(script_args())
    if a.cmd == 'survey':
        report = survey(a.exclude_collection, a.ignore_object)
    else:
        report = check(a.route, a.exclude_collection, a.ignore_object)
    text = json.dumps(report, indent=2)
    if a.out:
        with open(a.out, 'w') as fh:
            fh.write(text + '\n')
    print(text if not a.out else f'wrote {a.out}')
    if a.cmd == 'check':
        for v in report['violations']:
            print(f"[{v['severity'].upper()}] {v['shot']} f{v['frame']} {v['rule']}: {v['message']}")
        print('ROUTE OK' if report['ok'] else 'ROUTE FAILED', f"({report['fail_count']} fail, "
              f"{report['warn_count']} warn)")
        sys.stdout.flush()
        if not report['ok']:
            os._exit(1)


if __name__ == '__main__':
    main()
