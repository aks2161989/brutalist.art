"""Show a model going together, piece by piece: a height wipe that grows each piece up from its
base, or a staggered drop. Runs INSIDE Blender (background) on a COPY:

  blender -b MODEL.blend --python reveal.py -- wipe    ORDER.json --out revealed.blend
  blender -b MODEL.blend --python reveal.py -- stagger ORDER.json --out revealed.blend

ORDER.json
{
  "order_source": "recorded" | "explanatory",       # REQUIRED. See below.
  "edge_band": 0.04, "edge_color": [0.2, 0.8, 1.0], "edge_strength": 6.0,   # wipe
  "drop_height_m": 3.0,                                                     # stagger
  "items": [
    {"label": "Foundations", "objects": ["Slab_A", "Slab_B"], "start": 1, "duration": 24, "step": "S004"},
    {"label": "Columns", "collection": "COLUMNS", "start": 20, "duration": 30, "step": "S007"}
  ]
}

HONESTY. A film that shows a building rising piece by piece is a claim about order. `recorded`
means the items follow the order the model was really built in (each item names the build-record
step it came from, and verify_breakdown.py checks the steps exist and their order matches).
`explanatory` means the order is chosen to explain how the parts go together, NOT the order they
were modelled in, and the film must say so on screen or aloud (the gate requires
`labelled_in_film`). The choice is written into the .blend (scene property `reveal_order_source`).

`wipe` gives every object its OWN copy of each material, with a Geometry-bounding-box height
threshold (0 at the base to 1 at the top) keyed from the item's `start` over `duration` frames;
above the threshold the surface is a Transparent BSDF, and a thin emissive band rides the front.
Render it with film transparency, in Cycles (or EEVEE with a blended/dithered render method).
`stagger` keys each object to drop in from above with a BACK ease-out and hides it until its
start frame. Neither technique changes any geometry."""
import argparse
import json
import os
import sys

import bpy
from bpy_extras import anim_utils


def script_args():
    argv = sys.argv
    return argv[argv.index('--') + 1:] if '--' in argv else []


def items_objects(item):
    names = list(item.get('objects', []))
    if item.get('collection'):
        coll = bpy.data.collections.get(item['collection'])
        if coll is None:
            raise SystemExit(f'collection {item["collection"]!r} not found')
        names += [o.name for o in coll.all_objects]
    objs = []
    for n in names:
        ob = bpy.data.objects.get(n)
        if ob is None:
            raise SystemExit(f'object {n!r} not found (item {item.get("label")!r})')
        if ob.type in ('MESH', 'CURVE', 'SURFACE', 'META', 'FONT'):
            objs.append(ob)
    if not objs:
        raise SystemExit(f'item {item.get("label")!r} has no mesh objects')
    return objs


def set_interp(tree_or_ob, interp='LINEAR', easing='AUTO'):
    bag = anim_utils.animdata_get_channelbag_for_assigned_slot(tree_or_ob.animation_data)
    for fc in bag.fcurves:
        for kp in fc.keyframe_points:
            kp.interpolation = interp
            kp.easing = easing


def wipe_material(mat, start, duration, band, color, strength):
    """Wrap the surface of `mat` in a height wipe. Returns the Value node that carries the key."""
    nt = mat.node_tree
    out = next((n for n in nt.nodes if n.bl_idname == 'ShaderNodeOutputMaterial' and n.is_active_output),
               next(n for n in nt.nodes if n.bl_idname == 'ShaderNodeOutputMaterial'))
    link = out.inputs['Surface'].links[0] if out.inputs['Surface'].links else None
    if link is None:
        raise SystemExit(f'material {mat.name} has nothing plugged into its Surface')
    base_socket = link.from_socket
    N = nt.nodes.new
    coord = N('ShaderNodeTexCoord')
    sep = N('ShaderNodeSeparateXYZ')
    thr = N('ShaderNodeValue')
    thr.label = 'reveal_threshold'
    visible = N('ShaderNodeMath')            # 1 where the surface is below the front
    visible.operation = 'LESS_THAN'
    below_band = N('ShaderNodeMath')         # 1 well below the front
    below_band.operation = 'LESS_THAN'
    band_start = N('ShaderNodeMath')
    band_start.operation = 'SUBTRACT'
    band_start.inputs[1].default_value = band
    edge = N('ShaderNodeMath')               # the thin band at the front
    edge.operation = 'SUBTRACT'
    gone = N('ShaderNodeMath')               # 1 where it is not revealed yet
    gone.operation = 'SUBTRACT'
    gone.inputs[0].default_value = 1.0
    clear = N('ShaderNodeBsdfTransparent')
    mix = N('ShaderNodeMixShader')
    glow = N('ShaderNodeEmission')
    glow.inputs['Color'].default_value = (*color, 1.0)
    edge_s = N('ShaderNodeMath')
    edge_s.operation = 'MULTIPLY'
    edge_s.inputs[1].default_value = strength
    add = N('ShaderNodeAddShader')
    nt.links.new(coord.outputs['Generated'], sep.inputs['Vector'])
    nt.links.new(sep.outputs['Z'], visible.inputs[0])
    nt.links.new(thr.outputs[0], visible.inputs[1])
    nt.links.new(thr.outputs[0], band_start.inputs[0])
    nt.links.new(sep.outputs['Z'], below_band.inputs[0])
    nt.links.new(band_start.outputs[0], below_band.inputs[1])
    nt.links.new(visible.outputs[0], edge.inputs[0])
    nt.links.new(below_band.outputs[0], edge.inputs[1])
    nt.links.new(visible.outputs[0], gone.inputs[1])
    nt.links.new(gone.outputs[0], mix.inputs['Fac'])
    nt.links.new(base_socket, mix.inputs[1])
    nt.links.new(clear.outputs[0], mix.inputs[2])
    nt.links.new(edge.outputs[0], edge_s.inputs[0])
    nt.links.new(edge_s.outputs[0], glow.inputs['Strength'])
    nt.links.new(mix.outputs[0], add.inputs[0])
    nt.links.new(glow.outputs[0], add.inputs[1])
    nt.links.new(add.outputs[0], out.inputs['Surface'])
    thr.outputs[0].default_value = 0.0
    thr.outputs[0].keyframe_insert('default_value', frame=start)
    thr.outputs[0].default_value = 1.0 + band
    thr.outputs[0].keyframe_insert('default_value', frame=start + duration)
    set_interp(nt)
    return thr


def do_wipe(order):
    band = order.get('edge_band', 0.04)
    color = tuple(order.get('edge_color', (0.2, 0.8, 1.0)))
    strength = order.get('edge_strength', 6.0)
    for item in order['items']:
        for ob in items_objects(item):
            for i, slot in enumerate(ob.material_slots):
                if slot.material is None:
                    continue
                if not slot.material.use_nodes:
                    raise SystemExit(f'{ob.name}: material {slot.material.name} does not use nodes')
                m = slot.material.copy()
                m.name = f'{slot.material.name}__reveal_{ob.name}'
                slot.material = m
                wipe_material(m, int(item['start']), int(item['duration']), band, color, strength)


def do_stagger(order):
    h = float(order.get('drop_height_m', 3.0))
    for item in order['items']:
        s, d = int(item['start']), int(item['duration'])
        for ob in items_objects(item):
            z = ob.location.z
            ob.hide_render = True
            ob.hide_viewport = True
            ob.keyframe_insert('hide_render', frame=max(s - 1, 0))
            ob.keyframe_insert('hide_viewport', frame=max(s - 1, 0))
            ob.hide_render = False
            ob.hide_viewport = False
            ob.keyframe_insert('hide_render', frame=s)
            ob.keyframe_insert('hide_viewport', frame=s)
            ob.location.z = z + h
            ob.keyframe_insert('location', index=2, frame=s)
            ob.location.z = z
            ob.keyframe_insert('location', index=2, frame=s + d)
            bag = anim_utils.animdata_get_channelbag_for_assigned_slot(ob.animation_data)
            for fc in bag.fcurves:
                for kp in fc.keyframe_points:
                    if fc.data_path == 'location':
                        kp.interpolation, kp.easing = 'BACK', 'EASE_OUT'
                    else:
                        kp.interpolation = 'CONSTANT'


def main():
    ap = argparse.ArgumentParser(prog='reveal.py')
    ap.add_argument('technique', choices=['wipe', 'stagger'])
    ap.add_argument('order')
    ap.add_argument('--out', required=True)
    a = ap.parse_args(script_args())
    src = bpy.data.filepath
    if src and os.path.abspath(src) == os.path.abspath(a.out):
        raise SystemExit('refusing to save over the model that was opened; choose another --out')
    with open(a.order) as fh:
        order = json.load(fh)
    if order.get('order_source') not in ('recorded', 'explanatory'):
        raise SystemExit('order_source must be "recorded" (the order it was built in) or "explanatory" '
                         '(an order chosen to explain; the film must say so)')
    if not order.get('items'):
        raise SystemExit('no items')
    (do_wipe if a.technique == 'wipe' else do_stagger)(order)
    sc = bpy.context.scene
    sc['reveal_order_source'] = order['order_source']
    sc['reveal_technique'] = a.technique
    sc.frame_end = max(sc.frame_end, max(int(i['start']) + int(i['duration']) for i in order['items']))
    bpy.ops.wm.save_as_mainfile(filepath=os.path.abspath(a.out), copy=True)
    print(f'{a.technique}: {len(order["items"])} item(s), order_source={order["order_source"]} -> {a.out}')


if __name__ == '__main__':
    main()
