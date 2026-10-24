"""Check gui_map.py against the installed Blender. Runs INSIDE Blender (background):

  blender -b --factory-startup --python check_gui_map.py -- [--out report.json]

Verifies that every operator id, modifier type, constraint type and modifier/constraint property
NAME the interface map refers to exists in this Blender. It does NOT check the menu paths or
labels (those come from the manual and need a person at the interface), and it does not run any
operator. Re-run it after every Blender upgrade; exit status 1 when a name has gone missing."""
import json
import os
import sys

import bpy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gui_map as G  # noqa: E402


def main():
    missing = {'operators': [], 'modifier_types': [], 'modifier_props': [], 'constraint_types': [],
               'constraint_props': [], 'could_not_instantiate': []}
    for op in G.OPS:
        mod, _, name = op.partition('.')
        # hasattr(bpy.ops.mesh, "anything") is always True (operators are looked up lazily), so ask
        # for the operator's RNA type: that raises for a name that does not exist.
        try:
            getattr(getattr(bpy.ops, mod), name).get_rna_type()
        except Exception:
            missing['operators'].append(op)
    mod_enum = {i.identifier for i in bpy.types.Modifier.bl_rna.properties['type'].enum_items}
    con_enum = {i.identifier for i in bpy.types.Constraint.bl_rna.properties['type'].enum_items}
    # Real instances, not class names: add each modifier / constraint to a scratch mesh and read
    # the properties off it, so no naming assumption can make a check silently pass.
    me = bpy.data.meshes.new('scratch')
    ob = bpy.data.objects.new('scratch', me)
    bpy.context.scene.collection.objects.link(ob)
    props_checked, props_expected = 0, 0
    for t, (_menu, _label, props) in G.MODIFIERS.items():
        props_expected += len(props)
        if t not in mod_enum:
            missing['modifier_types'].append(t)
            continue
        try:
            inst = ob.modifiers.new('m', t)
        except Exception as e:
            missing['could_not_instantiate'].append(f'modifier {t}: {e}')
            continue
        for prop in props:
            props_checked += 1
            if prop not in inst.bl_rna.properties:
                missing['modifier_props'].append(f'{t}.{prop}')
    for t, (_menu, _label, props) in G.CONSTRAINTS.items():
        props_expected += len(props)
        if t not in con_enum:
            missing['constraint_types'].append(t)
            continue
        try:
            inst = ob.constraints.new(t)
        except Exception as e:
            missing['could_not_instantiate'].append(f'constraint {t}: {e}')
            continue
        for prop in props:
            props_checked += 1
            if prop not in inst.bl_rna.properties:
                missing['constraint_props'].append(f'{t}.{prop}')
    report = {'blender': bpy.app.version_string, 'checked': {
        'operators': len(G.OPS), 'modifiers': len(G.MODIFIERS), 'constraints': len(G.CONSTRAINTS),
        'properties_expected': props_expected, 'properties_checked': props_checked},
        'missing': missing,
        'ok': not any(missing.values()) and props_checked == props_expected}
    argv = sys.argv
    if '--out' in argv:
        with open(argv[argv.index('--out') + 1], 'w') as fh:
            json.dump(report, fh, indent=1)
    print(json.dumps(report, indent=1))
    sys.stdout.flush()
    if not report['ok']:
        os._exit(1)


main()
