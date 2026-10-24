"""Census of a Blender scene: what is in the file, measured. Used to record each build stage, to
compare a rebuilt model with the delivered one, and to catch a build record that no longer
matches the file.

Inside Blender (background):
  blender -b FILE.blend --python census.py -- census --out census.json
  blender -b FILE.blend --python census.py -- milestone --stage 04-blockout --out-dir DIR
        [--views CMP_ISO,CMP_FRONT] [--resolution 960x540] [--blend-ref PATH]
Plain Python:
  python3 census.py compare A.json B.json [--tol 1e-4]

`census` lists every object (type, collections, parent, transform, dimensions, evaluated vertex
and triangle counts, modifiers with their settings, constraints, materials), every material
(node types and Principled values), the collection tree, armatures' bones, scenes' units and
animation, and any scripts embedded in the file, then a SIGNATURE: a hash of the parts that
define the model's shape. Two builds with the same signature have the same objects, dimensions,
placements, counts and materials to 5 decimal places.

`milestone` writes the census plus a fixed set of comparison renders (the same cameras at every
stage, so the progression from blockout to finish is visible) into DIR.

`compare` reports what differs between two censuses. It is how a replay is judged: run the build
scripts headless, census the result, compare with the delivered model's census.
It sees geometry, placement, materials and modifiers; it does not see how a surface looks in a
render, or vertex positions inside a mesh beyond the counts and dimensions."""
import argparse
import hashlib
import json
import math
import os
import sys

try:
    import bpy
except ImportError:          # `compare` runs in plain Python
    bpy = None

SCHEMA = 1
# The fixed comparison cameras (and any helper objects) are named CMP_*. They are recorded, but they are
# not part of the model: leaving them out of the signature and the totals means adding the cameras to a
# file does not change what the file says about itself.
COMPARISON_PREFIX = 'CMP_'
NOISE_PROPS = {'name', 'type', 'rna_type', 'is_override_data', 'persistent_uid', 'show_expanded',
               'show_in_editmode', 'show_on_cage', 'execution_time', 'is_active', 'is_override_data',
               'use_pin_to_last', 'show_viewport', 'show_render'}


def r5(x):
    v = round(float(x), 5) + 0.0
    return 0.0 if v == 0 else v


def vec(v):
    return [r5(c) for c in v]


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def prop_value(v):
    if isinstance(v, bool) or v is None or isinstance(v, str):
        return v
    if isinstance(v, (int, float)):
        return r5(v)
    if hasattr(v, 'name') and hasattr(v, 'bl_rna'):
        return v.name
    try:
        return [prop_value(x) for x in v]
    except TypeError:
        return str(v)


def settings_of(rna_struct, skip=()):
    out = {}
    for key, p in rna_struct.bl_rna.properties.items():
        if key in NOISE_PROPS or key in skip or p.type in ('COLLECTION',) or p.is_hidden:
            continue
        try:
            val = getattr(rna_struct, key)
        except Exception:
            continue
        if p.type == 'POINTER' and val is not None and not hasattr(val, 'name'):
            continue
        out[key] = prop_value(val)
    return out


def evaluated_counts(ob, depsgraph):
    eo = ob.evaluated_get(depsgraph)
    try:
        mesh = eo.to_mesh()
    except RuntimeError:
        return None, None
    if mesh is None:
        return None, None
    try:
        mesh.calc_loop_triangles()
        return len(mesh.vertices), len(mesh.loop_triangles)
    finally:
        eo.to_mesh_clear()


def object_record(ob, depsgraph):
    rec = {
        'name': ob.name, 'type': ob.type, 'data': ob.data.name if ob.data else None,
        'collections': sorted(c.name for c in ob.users_collection),
        'parent': ob.parent.name if ob.parent else None,
        'location': vec(ob.location), 'rotation_euler': vec(ob.rotation_euler),
        'scale': vec(ob.scale), 'dimensions': vec(ob.dimensions),
        'hide_render': bool(ob.hide_render),
        'comparison': ob.name.startswith(COMPARISON_PREFIX),
        'instance_collection': ob.instance_collection.name if ob.instance_collection else None,
        'custom_props': sorted(k for k in ob.keys() if not k.startswith('_')),
        'materials': [s.material.name if s.material else None for s in ob.material_slots],
        'modifiers': [{'name': m.name, 'type': m.type, 'settings': settings_of(m)} for m in ob.modifiers],
        'constraints': [{'name': c.name, 'type': c.type,
                         'target': c.target.name if getattr(c, 'target', None) else None}
                        for c in ob.constraints],
    }
    if ob.type == 'MESH':
        rec['vertices'], rec['triangles'] = evaluated_counts(ob, depsgraph)
    if ob.type == 'ARMATURE':
        rec['bones'] = len(ob.data.bones)
    if ob.type == 'CAMERA':
        rec['lens_mm'] = r5(ob.data.lens)
    if ob.type == 'LIGHT':
        rec['light'] = {'type': ob.data.type, 'energy': r5(ob.data.energy)}
    return rec


def material_record(mat):
    rec = {'name': mat.name, 'use_nodes': bool(mat.use_nodes), 'users': mat.users,
           'diffuse_color': vec(mat.diffuse_color), 'nodes': [], 'principled': None}
    if mat.use_nodes and mat.node_tree:
        for n in mat.node_tree.nodes:
            rec['nodes'].append({'name': n.name, 'type': n.bl_idname})
            if n.bl_idname == 'ShaderNodeBsdfPrincipled' and rec['principled'] is None:
                vals = {}
                for k in ('Base Color', 'Metallic', 'Roughness', 'IOR', 'Alpha', 'Emission Color',
                          'Emission Strength', 'Coat Weight', 'Transmission Weight'):
                    s = n.inputs.get(k)
                    if s is not None and hasattr(s, 'default_value'):
                        vals[k] = prop_value(s.default_value)
                rec['principled'] = vals
    return rec


def collection_tree(coll):
    return {'name': coll.name, 'objects': sorted(o.name for o in coll.objects),
            'children': [collection_tree(c) for c in coll.children]}


def census():
    depsgraph = bpy.context.evaluated_depsgraph_get()
    objs = [object_record(o, depsgraph) for o in sorted(bpy.data.objects, key=lambda o: o.name)]
    # A material nothing uses and nothing protects is dropped when the file is saved, so it is not
    # part of the model (Blender's factory scene carries a "Dots Stroke" one).
    mats = [material_record(m) for m in sorted(bpy.data.materials, key=lambda m: m.name)
            if m.users > 0 or m.use_fake_user]
    scenes = []
    for sc in bpy.data.scenes:
        scenes.append({
            'name': sc.name, 'unit_system': sc.unit_settings.system,
            'scale_length': r5(sc.unit_settings.scale_length), 'length_unit': sc.unit_settings.length_unit,
            'fps': r5(sc.render.fps / sc.render.fps_base), 'frame_range': [sc.frame_start, sc.frame_end],
            'engine': sc.render.engine, 'camera': sc.camera.name if sc.camera else None,
            'world': sc.world.name if sc.world else None,
            'collections': collection_tree(sc.collection)})
    armatures = []
    for ob in bpy.data.objects:
        if ob.type == 'ARMATURE':
            armatures.append({'object': ob.name, 'bones': [
                {'name': b.name, 'parent': b.parent.name if b.parent else None,
                 'head': vec(b.head_local), 'tail': vec(b.tail_local), 'deform': bool(b.use_deform)}
                for b in sorted(ob.data.bones, key=lambda b: b.name)]})
    actions = [{'name': a.name, 'frame_range': [r5(a.frame_range[0]), r5(a.frame_range[1])]}
               for a in bpy.data.actions]
    texts = [{'name': t.name, 'sha256': hashlib.sha256(t.as_string().encode()).hexdigest()}
             for t in bpy.data.texts]
    model_objs = [o for o in objs if not o['comparison']]
    by_type = {}
    for o in model_objs:
        by_type[o['type']] = by_type.get(o['type'], 0) + 1
    totals = {'objects': len(model_objs), 'objects_by_type': by_type,
              'comparison_objects': len(objs) - len(model_objs),
              'vertices': sum(o.get('vertices') or 0 for o in model_objs),
              'triangles': sum(o.get('triangles') or 0 for o in model_objs),
              'materials': len(mats), 'bones': sum(len(a['bones']) for a in armatures),
              'collections': len(bpy.data.collections), 'actions': len(actions),
              'embedded_scripts': len(texts)}
    path = bpy.data.filepath
    doc = {'schema_version': SCHEMA,
           'file': {'path': path, 'sha256': sha256_file(path) if path and os.path.exists(path) else None,
                    'blender': bpy.app.version_string},
           'totals': totals, 'objects': objs, 'materials': mats, 'armatures': armatures,
           'scenes': scenes, 'actions': actions, 'embedded_scripts': texts}
    doc['signature'] = signature(doc)
    return doc


def signature(doc):
    """Hash of what defines the model's shape. Independent of file path, Blender version, object
    creation order, render settings and anything cosmetic in the UI."""
    core = {
        'objects': sorted(
            [o['name'], o['type'], o['parent'], o['dimensions'], o['location'], o['rotation_euler'],
             o['scale'], o.get('vertices'), o.get('triangles'), o['materials'],
             [m['type'] for m in o['modifiers']], o.get('instance_collection')]
            for o in doc['objects'] if not o.get('comparison')),
        'materials': sorted([m['name'], m['principled']] for m in doc['materials']),
        'bones': sorted([a['object'], b['name'], b['parent']] for a in doc['armatures'] for b in a['bones']),
    }
    return hashlib.sha256(json.dumps(core, sort_keys=True, default=str).encode()).hexdigest()


# ---------------------------------------------------------------- milestone

def milestone(stage, out_dir, views, resolution, blend_ref):
    os.makedirs(os.path.join(out_dir, 'views'), exist_ok=True)
    doc = census()
    cpath = os.path.join(out_dir, 'census.json')
    with open(cpath, 'w') as fh:
        json.dump(doc, fh, indent=1)
    sc = bpy.context.scene
    w, h = (int(x) for x in resolution.split('x'))
    sc.render.engine = 'BLENDER_WORKBENCH'
    sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = w, h, 100
    sc.render.image_settings.file_format = 'PNG'
    rendered, missing = [], []
    for name in views:
        cam = bpy.data.objects.get(name)
        if cam is None or cam.type != 'CAMERA':
            missing.append(name)
            continue
        sc.camera = cam
        path = os.path.join(out_dir, 'views', name + '.png')
        sc.render.filepath = path
        bpy.ops.render.render(write_still=True)
        rendered.append({'name': name, 'path': os.path.relpath(path, out_dir), 'sha256': sha256_file(path)})
    ms = {'schema_version': SCHEMA, 'stage': stage,
          'blend': {'path': os.path.abspath(blend_ref or bpy.data.filepath or ''),
                    'sha256': doc['file']['sha256']},
          'blender': bpy.app.version_string, 'census': 'census.json',
          'census_signature': doc['signature'], 'totals': doc['totals'],
          'views': rendered, 'missing_views': missing}
    with open(os.path.join(out_dir, 'milestone.json'), 'w') as fh:
        json.dump(ms, fh, indent=1)
    print(f'milestone {stage}: {doc["totals"]["objects"]} objects, {len(rendered)} view(s) -> {out_dir}')
    if missing:
        print('MISSING comparison cameras:', ', '.join(missing))


# ---------------------------------------------------------------- compare

def compare(a, b, tol=1e-4):
    diffs = []
    ao = {o['name']: o for o in a['objects'] if not o.get('comparison')}
    bo = {o['name']: o for o in b['objects'] if not o.get('comparison')}
    for n in sorted(set(ao) - set(bo)):
        diffs.append(f'only in A: object {n}')
    for n in sorted(set(bo) - set(ao)):
        diffs.append(f'only in B: object {n}')
    for n in sorted(set(ao) & set(bo)):
        x, y = ao[n], bo[n]
        for key in ('type', 'parent', 'vertices', 'triangles', 'materials', 'instance_collection'):
            if x.get(key) != y.get(key):
                diffs.append(f'{n}: {key} {x.get(key)} != {y.get(key)}')
        for key in ('location', 'rotation_euler', 'scale', 'dimensions'):
            if any(abs(p - q) > tol for p, q in zip(x[key], y[key])):
                diffs.append(f'{n}: {key} {x[key]} != {y[key]}')
        if [m['type'] for m in x['modifiers']] != [m['type'] for m in y['modifiers']]:
            diffs.append(f'{n}: modifier stack differs')
        else:
            for m1, m2 in zip(x['modifiers'], y['modifiers']):
                for k in sorted(set(m1['settings']) | set(m2['settings'])):
                    v1, v2 = m1['settings'].get(k), m2['settings'].get(k)
                    if isinstance(v1, float) and isinstance(v2, float):
                        bad = abs(v1 - v2) > tol
                    else:
                        bad = v1 != v2
                    if bad:
                        diffs.append(f'{n}: modifier {m1["name"]}.{k} {v1} != {v2}')
    am, bm = {m['name']: m for m in a['materials']}, {m['name']: m for m in b['materials']}
    for n in sorted(set(am) ^ set(bm)):
        diffs.append(f'material {n} only in {"A" if n in am else "B"}')
    for n in sorted(set(am) & set(bm)):
        pa, pb = am[n]['principled'], bm[n]['principled']
        if pa != pb:
            diffs.append(f'material {n}: Principled values differ')
    ba = {(x['object'], bn['name']): bn for x in a['armatures'] for bn in x['bones']}
    bb = {(x['object'], bn['name']): bn for x in b['armatures'] for bn in x['bones']}
    for k in sorted(set(ba) ^ set(bb)):
        diffs.append(f'bone {k[1]} of {k[0]} only in {"A" if k in ba else "B"}')
    for k in sorted(set(ba) & set(bb)):
        if ba[k]['parent'] != bb[k]['parent']:
            diffs.append(f'bone {k[1]}: parent differs')
    for key in ('objects', 'triangles', 'materials', 'bones'):
        if a['totals'][key] != b['totals'][key]:
            diffs.append(f'total {key}: {a["totals"][key]} != {b["totals"][key]}')
    return {'same_signature': a['signature'] == b['signature'], 'differences': diffs,
            'tolerance': tol, 'ok': not diffs}


def script_args():
    argv = sys.argv
    return argv[argv.index('--') + 1:] if '--' in argv else argv[1:]


def main():
    ap = argparse.ArgumentParser(prog='census.py')
    sub = ap.add_subparsers(dest='cmd', required=True)
    c = sub.add_parser('census')
    c.add_argument('--out')
    m = sub.add_parser('milestone')
    m.add_argument('--stage', required=True)
    m.add_argument('--out-dir', required=True)
    m.add_argument('--views', default='')
    m.add_argument('--resolution', default='960x540')
    m.add_argument('--blend-ref', help='the versioned .blend this milestone stands for')
    k = sub.add_parser('compare')
    k.add_argument('a')
    k.add_argument('b')
    k.add_argument('--tol', type=float, default=1e-4)
    a = ap.parse_args(script_args())
    if a.cmd == 'compare':
        res = compare(json.load(open(a.a)), json.load(open(a.b)), a.tol)
        for d in res['differences']:
            print('DIFF', d)
        print('SAME' if res['ok'] else 'DIFFERENT',
              '(signatures match)' if res['same_signature'] else '(signatures differ)')
        sys.exit(0 if res['ok'] else 1)
    if bpy is None:
        sys.exit('census/milestone must run inside Blender: blender -b FILE.blend --python census.py -- ...')
    if a.cmd == 'census':
        doc = census()
        if a.out:
            with open(a.out, 'w') as fh:
                json.dump(doc, fh, indent=1)
            print(f'wrote {a.out}: {doc["totals"]["objects"]} objects, signature {doc["signature"][:12]}')
        else:
            print(json.dumps(doc['totals'], indent=1), doc['signature'])
    else:
        milestone(a.stage, a.out_dir, [v for v in a.views.split(',') if v], a.resolution, a.blend_ref)
    sys.stdout.flush()


if __name__ == '__main__':
    main()
