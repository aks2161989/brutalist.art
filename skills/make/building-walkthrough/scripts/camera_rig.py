"""Build the camera rig for a walkthrough from a route file. Runs INSIDE Blender (background):

  blender -b MODEL.blend --python camera_rig.py -- ROUTE.json --out RIGGED.blend

It never saves over the model it opened (BLENDER.md: work on a copy). Running it twice on the
same route gives the same scene: the objects it makes for a shot id are deleted and rebuilt.

ROUTE.json (metres, world axes, Z up):
{
  "schema_version": 1,
  "fps": 24,
  "defaults": {"lens_mm": 28, "sensor_mm": 36, "clip_start_m": 0.05, "clip_end_m": 1000,
               "ease": "linear"},
  "shots": [
    {"id": "S01", "type": "walk", "frames": [1, 240],
     "waypoints": [[0, -12, 1.6], [0, -4, 1.6], [0, 4, 1.6]],
     "lens_mm": 28, "ease": "in_out", "smooth": true,
     "look": {"mode": "travel", "yaw_deg": 0, "pitch_deg": 0},
     "shift_y": 0.0,
     "dof": {"enabled": false, "focus_point": [0, 4, 1.6], "fstop": 4.0}},
    {"id": "S02", "type": "still", "frames": [241, 336], "position": [2, 1, 1.6],
     "look": {"mode": "target", "point": [6, 1, 1.4]}},
    {"id": "S03", "type": "walk", "frames": [337, 480],
     "waypoints": [...], "look": {"mode": "path", "waypoints": [...]}},
    {"id": "S04", "type": "orbit", "frames": [481, 720], "center": [0, 0, 0], "radius_m": 3.0,
     "height_m": 1.4, "degrees": 360, "start_deg": 0, "look_height_m": 0.9}
  ]
}
look.mode: "travel" (face along the path; yaw/pitch offsets allowed), "target" (look at a fixed
point), "path" (look at a point that rides its own path, in step with the camera).
Shot frame ranges must not overlap. A timeline marker with the shot's camera bound to it is
placed on each shot's first frame, so rendering the timeline uses the right camera.
"""
import argparse
import hashlib
import json
import math
import os
import sys

import bpy
from bpy_extras import anim_utils
from mathutils import Vector

RIG_COLLECTION = 'CAMERA_RIG'
PREFIXES = ('CAM_', 'RIG_', 'PATH_', 'LOOK_', 'LOOKPATH_', 'ORBITLOOK_')


def script_args():
    argv = sys.argv
    return argv[argv.index('--') + 1:] if '--' in argv else []


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()


EASES = {
    'linear': ('LINEAR', 'AUTO'),
    'in_out': ('BEZIER', 'AUTO'),         # auto-clamped handles: slow in, slow out
    'in': ('SINE', 'EASE_IN'),
    'out': ('SINE', 'EASE_OUT'),
}


def set_ease(owner, ease):
    """Set the interpolation of every key just inserted on `owner`.

    Verified on Blender 5.1.2: the user preference `keyframe_new_interpolation_type` is
    ignored by keyframe_insert(), so every new key came out BEZIER (an eased move at 1.5x the
    intended peak speed). The keys have to be set on the F-curves themselves, which in 5.x live
    in the channelbag of the assigned action slot."""
    if ease not in EASES:
        raise SystemExit(f'unknown ease {ease!r}; use one of {sorted(EASES)}')
    interp, easing = EASES[ease]
    bag = anim_utils.animdata_get_channelbag_for_assigned_slot(owner.animation_data)
    for fc in bag.fcurves:
        for kp in fc.keyframe_points:
            kp.interpolation = interp
            kp.easing = easing


def rig_collection(sc):
    coll = bpy.data.collections.get(RIG_COLLECTION)
    if coll is None:
        coll = bpy.data.collections.new(RIG_COLLECTION)
    if coll.name not in sc.collection.children:
        sc.collection.children.link(coll)
    return coll


def purge(shot_id):
    """Delete every object this script made for the shot, and its orphan data."""
    for prefix in PREFIXES:
        ob = bpy.data.objects.get(prefix + shot_id)
        if ob is not None:
            data = ob.data
            bpy.data.objects.remove(ob, do_unlink=True)
            if data is not None and data.users == 0:
                (bpy.data.cameras if isinstance(data, bpy.types.Camera) else bpy.data.curves).remove(data)
    for m in [m for m in bpy.context.scene.timeline_markers if m.name == 'M_' + shot_id]:
        bpy.context.scene.timeline_markers.remove(m)


def new_empty(name, coll, location=(0, 0, 0)):
    ob = bpy.data.objects.new(name, None)
    ob.empty_display_type = 'PLAIN_AXES'
    ob.empty_display_size = 0.3
    ob.location = location
    coll.objects.link(ob)
    return ob


def new_path(name, coll, points, smooth=True):
    cu = bpy.data.curves.new(name, 'CURVE')
    cu.dimensions = '3D'
    cu.use_path = True
    cu.use_path_clamp = True
    sp = cu.splines.new('BEZIER' if smooth else 'POLY')
    if smooth:
        sp.bezier_points.add(len(points) - 1)
        for bp, p in zip(sp.bezier_points, points):
            bp.co = p
            bp.handle_left_type = bp.handle_right_type = 'AUTO'
    else:
        sp.points.add(len(points) - 1)
        for sp_pt, p in zip(sp.points, points):
            sp_pt.co = (p[0], p[1], p[2], 1.0)
    ob = bpy.data.objects.new(name, cu)
    coll.objects.link(ob)
    return ob


def follow(owner, path_obj, f0, f1, ease):
    """Fixed Position + Offset Factor 0 -> 1: the rig sits at a fraction of the path LENGTH,
    so equal factor steps are equal distances even when the control points are unevenly
    spaced (measured on Blender 5.1.2)."""
    con = owner.constraints.new('FOLLOW_PATH')
    con.target = path_obj
    con.use_fixed_location = True
    con.use_curve_follow = True
    con.forward_axis = 'FORWARD_Y'
    con.up_axis = 'UP_Z'
    con.offset_factor = 0.0
    con.keyframe_insert('offset_factor', frame=f0)
    con.offset_factor = 1.0
    con.keyframe_insert('offset_factor', frame=f1)
    set_ease(owner, ease)
    return con


def track_to(cam, target):
    con = cam.constraints.new('TRACK_TO')
    con.target = target
    con.track_axis = 'TRACK_NEGATIVE_Z'
    con.up_axis = 'UP_Y'
    con.use_target_z = False
    return con


def make_camera(sid, coll, shot, defaults):
    cam_data = bpy.data.cameras.new('CAM_' + sid)
    g = lambda key, dflt: shot.get(key, defaults.get(key, dflt))  # noqa: E731
    cam_data.lens = g('lens_mm', 28)
    cam_data.sensor_width = g('sensor_mm', 36)
    cam_data.sensor_fit = 'AUTO'
    cam_data.clip_start = g('clip_start_m', 0.05)
    cam_data.clip_end = g('clip_end_m', 1000)
    cam_data.shift_y = shot.get('shift_y', 0.0)
    cam_data.shift_x = shot.get('shift_x', 0.0)
    dof = shot.get('dof') or {}
    cam_data.dof.use_dof = bool(dof.get('enabled', False))
    if cam_data.dof.use_dof:
        cam_data.dof.aperture_fstop = dof.get('fstop', 4.0)
    cam = bpy.data.objects.new('CAM_' + sid, cam_data)
    coll.objects.link(cam)
    return cam


def aim_dof(cam, coll, sid, dof):
    if cam.data.dof.use_dof and dof.get('focus_point'):
        focus = new_empty('LOOK_%s_focus' % sid, coll, tuple(dof['focus_point']))
        cam.data.dof.focus_object = focus


def build_shot(sc, coll, shot, defaults):
    sid, kind = shot['id'], shot.get('type', 'walk')
    f0, f1 = int(shot['frames'][0]), int(shot['frames'][1])
    ease = shot.get('ease', defaults.get('ease', 'linear'))
    look = shot.get('look', {'mode': 'travel'})
    purge(sid)
    cam = make_camera(sid, coll, shot, defaults)

    if kind == 'still':
        cam.location = tuple(shot['position'])
        if look['mode'] != 'target':
            raise SystemExit(f'{sid}: a still needs look.mode "target"')
        tgt = new_empty('LOOK_' + sid, coll, tuple(look['point']))
        track_to(cam, tgt)

    elif kind == 'orbit':
        centre = Vector(shot['center'])
        rig = new_empty('RIG_' + sid, coll, centre)
        cam.parent = rig
        cam.location = (shot['radius_m'], 0.0, shot['height_m'])
        tgt = new_empty('ORBITLOOK_' + sid, coll,
                        (centre.x, centre.y, centre.z + shot.get('look_height_m', 0.9)))
        track_to(cam, tgt)
        start = math.radians(shot.get('start_deg', 0.0))
        rig.rotation_euler = (0, 0, start)
        rig.keyframe_insert('rotation_euler', index=2, frame=f0)
        rig.rotation_euler = (0, 0, start + math.radians(shot.get('degrees', 360.0)))
        rig.keyframe_insert('rotation_euler', index=2, frame=f1)
        set_ease(rig, ease)

    else:  # walk, aerial, crane
        pts = [tuple(p) for p in shot['waypoints']]
        if len(pts) < 2:
            raise SystemExit(f'{sid}: a moving shot needs at least two waypoints')
        path = new_path('PATH_' + sid, coll, pts, shot.get('smooth', True))
        rig = new_empty('RIG_' + sid, coll)
        follow(rig, path, f0, f1, ease)
        cam.parent = rig
        mode = look.get('mode', 'travel')
        if mode == 'travel':
            # Camera looks down its own -Z. Rotating +90 deg about X turns -Z into the rig's +Y
            # (the direction of travel) and the camera's up into world up: a level camera.
            cam.rotation_euler = (math.radians(90.0 + look.get('pitch_deg', 0.0)), 0.0,
                                  math.radians(look.get('yaw_deg', 0.0)))
        elif mode == 'target':
            tgt = new_empty('LOOK_' + sid, coll, tuple(look['point']))
            track_to(cam, tgt)
        elif mode == 'path':
            lp = new_path('LOOKPATH_' + sid, coll, [tuple(p) for p in look['waypoints']],
                          shot.get('smooth', True))
            tgt = new_empty('LOOK_' + sid, coll)
            follow(tgt, lp, f0, f1, ease)
            track_to(cam, tgt)
        else:
            raise SystemExit(f'{sid}: unknown look.mode {mode!r}')

    aim_dof(cam, coll, sid, shot.get('dof') or {})
    cam['walkthrough_shot'] = sid
    marker = sc.timeline_markers.new('M_' + sid, frame=f0)
    marker.camera = cam
    return cam


def main():
    ap = argparse.ArgumentParser(prog='camera_rig.py')
    ap.add_argument('route')
    ap.add_argument('--out', required=True, help='where to save the rigged copy')
    a = ap.parse_args(script_args())
    src = bpy.data.filepath
    out = os.path.abspath(a.out)
    if src and os.path.abspath(src) == out:
        raise SystemExit('refusing to save over the model that was opened; choose another --out')
    with open(a.route) as fh:
        route = json.load(fh)
    sc = bpy.context.scene
    if 'fps' in route:
        sc.render.fps = int(round(route['fps']))
        sc.render.fps_base = 1.0
    shots = route['shots']
    spans = sorted((int(s['frames'][0]), int(s['frames'][1]), s['id']) for s in shots)
    for (a0, a1, an), (b0, b1, bn) in zip(spans, spans[1:]):
        if b0 <= a1:
            raise SystemExit(f'shots {an} and {bn} overlap in time ({a0}-{a1} / {b0}-{b1})')
    coll = rig_collection(sc)
    defaults = route.get('defaults', {})
    for shot in shots:
        build_shot(sc, coll, shot, defaults)
    sc.frame_start = spans[0][0]
    sc.frame_end = spans[-1][1]
    sc.camera = bpy.data.objects['CAM_' + shots[0]['id']]
    sc['walkthrough_route_sha256'] = sha256_file(a.route)
    bpy.ops.wm.save_as_mainfile(filepath=out, copy=True)
    print(f'rigged {len(shots)} shot(s) -> {out}')


if __name__ == '__main__':
    main()
