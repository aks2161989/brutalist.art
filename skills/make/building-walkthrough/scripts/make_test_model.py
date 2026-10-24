"""Build a tiny, fully known test building so the walkthrough gates can be tried on something
whose right answers are obvious. Runs INSIDE Blender (background):

  blender -b --factory-startup --python make_test_model.py -- OUT.blend

Two 8 m x 8 m rooms (x -4..4, y -8..0 and y 0..8), floor top at z = 0, ceiling underside at
z = 3, 0.2 m walls, a 1.2 m x 2.2 m doorway in the dividing wall at y = 0 centred on x = 0,
and a 1 m pedestal in the middle of the first room. It is a TEST FIXTURE, not a model of
anything: never present it as evidence in a film.
"""
import sys

import bpy


def box(name, lo, hi, coll):
    (x0, y0, z0), (x1, y1, z1) = lo, hi
    verts = [(x, y, z) for z in (z0, z1) for y in (y0, y1) for x in (x0, x1)]
    faces = [(0, 1, 3, 2), (4, 6, 7, 5), (0, 4, 5, 1), (2, 3, 7, 6), (0, 2, 6, 4), (1, 5, 7, 3)]
    mesh = bpy.data.meshes.new(name)
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    ob = bpy.data.objects.new(name, mesh)
    coll.objects.link(ob)
    return ob


def main():
    argv = sys.argv
    out = argv[argv.index('--') + 1]
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    sc.unit_settings.system = 'METRIC'
    sc.unit_settings.scale_length = 1.0
    sc.render.fps = 24
    arch = bpy.data.collections.new('ARCHITECTURE')
    sc.collection.children.link(arch)
    box('Floor', (-4.2, -8.2, -0.2), (4.2, 8.2, 0.0), arch)
    box('Ceiling', (-4.2, -8.2, 3.0), (4.2, 8.2, 3.2), arch)
    box('Wall_W', (-4.2, -8.2, 0.0), (-4.0, 8.2, 3.0), arch)
    box('Wall_E', (4.0, -8.2, 0.0), (4.2, 8.2, 3.0), arch)
    box('Wall_S', (-4.0, -8.2, 0.0), (4.0, -8.0, 3.0), arch)
    box('Wall_N', (-4.0, 8.0, 0.0), (4.0, 8.2, 3.0), arch)
    box('Divider_L', (-4.0, -0.1, 0.0), (-0.6, 0.1, 3.0), arch)
    box('Divider_R', (0.6, -0.1, 0.0), (4.0, 0.1, 3.0), arch)
    box('Lintel', (-0.6, -0.1, 2.2), (0.6, 0.1, 3.0), arch)
    props = bpy.data.collections.new('PROPS')
    sc.collection.children.link(props)
    box('Pedestal', (-0.5, -4.5, 0.0), (0.5, -3.5, 1.0), props)
    bpy.ops.wm.save_as_mainfile(filepath=out)
    print('wrote', out)


if __name__ == '__main__':
    main()
