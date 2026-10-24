#!/usr/bin/env python3
"""Draft step cards from a tape: what a person would do in Blender's interface to repeat each
command the build ran.

  draft_steps.py TAPE.jsonl --out BUILD-STEPS.draft.jsonl [--tape-ref tape/live.jsonl]
                 [--stage-map "1-3:01-define,4-12:04-blockout"]
  draft_steps.py gui TAPE.jsonl --seq 4          # print the translation of one command

Each command that changed the scene becomes one card with: the exact Python (a pointer into the
tape), a DRAFT interface translation, the settings it used, and the reply it got. A command that
FAILED becomes a card marked `excluded_from_procedure`, and the next successful command with the
same stated purpose records it as the thing it corrected.

WHAT THIS IS AND IS NOT. The translation reads the Python's syntax tree. It handles the
operators, modifiers, constraints, materials, transforms and render settings listed in
gui_map.py, simple loops, ifs and helper functions. Everything else is printed as `UNMAPPED:`
with the source line, never guessed. Interface paths in gui_map.py come from the manual and
were NOT followed click by click; a card's `gui_source` stays `"draft"` until a person has done
the steps and changed it to `"human"`. Numbers are assumed to be metres at unit scale 1 (check
the scene's units in the census). Judgment (goal, why) is NOT drafted: the card lists
`needs_author` until someone writes it.
"""
import argparse
import ast
import json
import math
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gui_map as G  # noqa: E402

UNKNOWN = object()


def fnum(x):
    if isinstance(x, bool):
        return str(x)
    if isinstance(x, float):
        s = f'{x:.4f}'.rstrip('0').rstrip('.')
        return s if s not in ('-0', '') else '0'
    return str(x)


class Translator:
    def __init__(self):
        self.gui, self.idnames, self.settings = [], [], {}
        self.unmapped, self.approx = [], 0
        self.consts, self.kinds, self.funcs = {}, {}, {}
        self.module, self.helpers = None, []
        self._in_helper = set()

    # ---------------------------------------------------------------- values
    def ev(self, node):
        """Fold a node to a Python value when it is plainly constant; else UNKNOWN."""
        try:
            return ast.literal_eval(node)
        except Exception:
            pass
        if isinstance(node, ast.Name):
            return self.consts.get(node.id, UNKNOWN)
        if isinstance(node, (ast.Tuple, ast.List)):
            vals = [self.ev(e) for e in node.elts]
            return UNKNOWN if any(v is UNKNOWN for v in vals) else tuple(vals)
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
            v = self.ev(node.operand)
            return UNKNOWN if v is UNKNOWN else (-v if isinstance(node.op, ast.USub) else v)
        if isinstance(node, ast.BinOp):
            a, b = self.ev(node.left), self.ev(node.right)
            ops = {ast.Add: lambda x, y: x + y, ast.Sub: lambda x, y: x - y,
                   ast.Mult: lambda x, y: x * y, ast.Div: lambda x, y: x / y}
            fn = ops.get(type(node.op))
            if a is UNKNOWN or b is UNKNOWN or fn is None:
                return UNKNOWN
            try:
                return fn(a, b)
            except Exception:
                return UNKNOWN
        if isinstance(node, ast.Call):
            f = ast.unparse(node.func)
            if f in ('math.radians', 'radians') and len(node.args) == 1:
                v = self.ev(node.args[0])
                return UNKNOWN if v is UNKNOWN else math.radians(v)
            if f in ('Vector', 'mathutils.Vector') and len(node.args) == 1:
                return self.ev(node.args[0])
        return UNKNOWN

    def show(self, node, degrees=False):
        v = self.ev(node)
        if v is UNKNOWN:
            return ast.unparse(node)
        return self.fmt(v, degrees)

    def fmt(self, v, degrees=False):
        if isinstance(v, tuple):
            if degrees:
                v = tuple(math.degrees(x) if isinstance(x, (int, float)) else x for x in v)
            return '(' + ', '.join(fnum(x) for x in v) + ')' + ('°' if degrees else '')
        if isinstance(v, str):
            return repr(v)
        return fnum(v)

    def axis_text(self, v, label, degrees=False):
        if isinstance(v, tuple) and len(v) == 3:
            unit = '°' if degrees else ''
            vals = [math.degrees(x) if degrees else x for x in v]
            return f'{label} X {fnum(vals[0])}{unit}, Y {fnum(vals[1])}{unit}, Z {fnum(vals[2])}{unit}'
        return f'{label} {self.fmt(v)}'

    # ---------------------------------------------------------------- emit
    def emit(self, text, indent=0):
        self.gui.append('  ' * indent + text)

    def emit_unmapped(self, src, why, indent=0):
        self.unmapped.append(src)
        self.gui.append('  ' * indent + f'UNMAPPED: {src[:140]}  [{why}]')

    def emit_approx(self, text, indent=0):
        self.approx += 1
        self.gui.append('  ' * indent + '~ ' + text)

    # ---------------------------------------------------------------- statements
    def block(self, stmts, indent=0):
        for st in stmts:
            self.stmt(st, indent)

    def stmt(self, st, indent):
        if isinstance(st, ast.FunctionDef):
            self.funcs[st.name] = st
        elif isinstance(st, ast.Expr) and isinstance(st.value, ast.Call):
            self.call(st.value, None, indent)
        elif isinstance(st, ast.Assign):
            self.assign(st, indent)
        elif isinstance(st, ast.AugAssign):
            if isinstance(st.target, (ast.Attribute, ast.Subscript)) and self.touches_bpy(st):
                self.emit_approx(f'Change {ast.unparse(st.target)} by {ast.unparse(st.op)}'
                                 f'{ast.unparse(st.value)} (find the field by its label)', indent)
        elif isinstance(st, ast.For):
            if self.mutates(st):
                self.emit(f'Repeat for each {ast.unparse(st.target)} in {ast.unparse(st.iter)[:80]}:', indent)
                self.block(st.body, indent + 1)
        elif isinstance(st, ast.If):
            if self.mutates(st):
                self.emit(f'If {ast.unparse(st.test)[:90]}:', indent)
                self.block(st.body, indent + 1)
                if st.orelse and any(self.mutates(x) for x in st.orelse):
                    self.emit('Otherwise:', indent)
                    self.block(st.orelse, indent + 1)
        elif isinstance(st, (ast.With, ast.Try)):
            self.block(st.body, indent)

    def touches_bpy(self, node):
        src = ast.unparse(node)
        return 'bpy' in src or any(k in src for k in self.kinds) or 'obj' in src or 'scene' in src

    def mutates(self, node, _seen=None):
        _seen = _seen if _seen is not None else set()
        for n in ast.walk(node):
            if isinstance(n, ast.Call):
                f = ast.unparse(n.func)
                if f.startswith('bpy.ops.') or re.search(r'\.(new|link|unlink|remove|append|from_pydata)$', f):
                    return True
                if f in self.funcs and f not in _seen:
                    _seen.add(f)
                    if self.mutates(self.funcs[f], _seen):
                        return True
            if isinstance(n, ast.Assign) and any(isinstance(t, (ast.Attribute, ast.Subscript)) for t in n.targets):
                return True
        return False

    def assign(self, st, indent):
        tgt = st.targets[0]
        if isinstance(tgt, ast.Name):
            if isinstance(st.value, ast.Call):
                self.call(st.value, tgt.id, indent)
            else:
                if isinstance(st.value, (ast.Dict, ast.List, ast.Set)) and not st.value.__dict__.get('elts', st.value.__dict__.get('keys', [1])):
                    self.kinds[tgt.id] = ('container', None)
                v = self.ev(st.value)
                if v is not UNKNOWN:
                    self.consts[tgt.id] = v
                src = ast.unparse(st.value)
                m = re.match(r"bpy\.data\.(objects|materials|cameras|collections)\[(.+)\]$", src) or \
                    re.match(r"bpy\.data\.(objects|materials)\.get\((.+)\)$", src)
                if m:
                    self.kinds[tgt.id] = (m.group(1)[:-1], str(self.ev(ast.parse(m.group(2), mode='eval').body)))
                elif src == 'bpy.context.active_object':
                    self.kinds[tgt.id] = ('object', None)
            return
        if isinstance(tgt, (ast.Attribute, ast.Subscript)):
            self.attr_assign(tgt, st.value, indent)

    # ---------------------------------------------------------------- calls
    def call(self, node, target_var, indent):
        f = ast.unparse(node.func)
        args, kw = node.args, {k.arg: k.value for k in node.keywords if k.arg}

        if f.startswith('bpy.ops.'):
            return self.operator(f[len('bpy.ops.'):], node, indent)
        if f in self.funcs and f not in self._in_helper:
            return self.helper(f, node, indent)
        if f.endswith('.modifiers.new'):
            mtype = self.ev(kw['type']) if 'type' in kw else (self.ev(args[1]) if len(args) > 1 else UNKNOWN)
            name = self.ev(kw['name']) if 'name' in kw else (self.ev(args[0]) if args else UNKNOWN)
            spec = G.MODIFIERS.get(mtype) if mtype is not UNKNOWN else None
            if spec:
                self.emit(f'Properties ▸ Modifiers tab ▸ Add Modifier ▸ {spec[0]} ▸ {spec[1]}'
                          + (f'; rename it {name!r}' if name not in (UNKNOWN, spec[1]) else ''), indent)
                self.idnames.append(f'modifier:{mtype}')
            else:
                self.emit_unmapped(ast.unparse(node), 'modifier type not in gui_map', indent)
            if target_var:
                self.kinds[target_var] = ('modifier', mtype)
            return
        if f.endswith('.constraints.new'):
            ctype = self.ev(args[0]) if args else (self.ev(kw['type']) if 'type' in kw else UNKNOWN)
            spec = G.CONSTRAINTS.get(ctype) if ctype is not UNKNOWN else None
            if spec:
                self.emit(f'Properties ▸ Object Constraints tab ▸ Add Object Constraint ▸ {spec[0]} ▸ {spec[1]}', indent)
                self.idnames.append(f'constraint:{ctype}')
            else:
                self.emit_unmapped(ast.unparse(node), 'constraint type not in gui_map', indent)
            if target_var:
                self.kinds[target_var] = ('constraint', ctype)
            return
        if f == 'bpy.data.materials.new':
            name = self.ev(kw['name']) if 'name' in kw else (self.ev(args[0]) if args else UNKNOWN)
            self.emit(f'Properties ▸ Material tab ▸ New; name it {self.fmt(name) if name is not UNKNOWN else "(see call)"}', indent)
            if target_var:
                self.kinds[target_var] = ('material', name if name is not UNKNOWN else None)
            return
        if f.endswith('.materials.append'):
            self.emit('Properties ▸ Material tab ▸ choose the existing material in the Browse Material menu '
                      f'({ast.unparse(args[0]) if args else "?"})', indent)
            return
        if f == 'bpy.data.objects.remove':
            m = re.match(r"bpy\.data\.objects\[(['\"])(.+)\1\]$", ast.unparse(args[0])) if args else None
            who = repr(m.group(2)) if m else (ast.unparse(args[0]) if args else 'the object')
            self.emit(f'Select {who} and delete it (X)', indent)
            return
        if re.match(r'bpy\.data\.\w+\.remove$', f):
            self.emit_approx('Outliner ▸ Display Mode ▸ Blender File ▸ right-click the data-block ▸ Delete '
                             '(unused data is also cleared by File ▸ Clean Up ▸ Purge Unused Data)', indent)
            return
        if f in ('bpy.data.cameras.new', 'bpy.data.lights.new', 'bpy.data.curves.new',
                 'bpy.data.armatures.new', 'bpy.data.meshes.new'):
            self.emit_approx(f'{f} creates data with no menu of its own: add the object it is for from '
                             f'Add (Shift+A) instead', indent)
            return
        if f == 'bpy.data.objects.new':
            self.emit_approx('bpy.data.objects.new builds an object from existing data; in the interface the '
                             'object comes from the Add menu (Shift+A)', indent)
            return
        if f == 'bpy.data.collections.new':
            self.emit('Outliner ▸ right-click ▸ New Collection; rename it '
                      f'{self.show(args[0]) if args else ""}', indent)
            return
        if f.endswith('.objects.link') or f.endswith('.children.link'):
            self.emit('Outliner: drag it into the collection (or select it and press M ▸ the collection)', indent)
            return
        if f.endswith('.from_pydata') or f.startswith('bmesh.'):
            self.emit_unmapped(ast.unparse(node), 'mesh built from raw vertex data: no interface equivalent; '
                               'model the shape with primitives and Edit Mode, or use the script', indent)
            return
        if f.endswith('.edit_bones.new') or f.endswith('.edit_bones.remove'):
            self.emit_approx('Armature Edit Mode ▸ Add ▸ Single Bone (Shift+A); set Head/Tail/Roll in the '
                             'Sidebar ▸ Item tab', indent)
            return
        if f.endswith('.select_set'):
            self.emit('Click the object in the Outliner (Ctrl+click to add)', indent)
            return
        if f.endswith('.keyframe_insert'):
            self.emit_approx(f'Hover over the property named by {ast.unparse(node)[:70]} and press I', indent)
            return
        if f.endswith('.to_mesh') or f.endswith('.copy') or f.endswith('.get'):
            return
        if 'bpy' in ast.unparse(node) and not f.startswith(('print', 'len', 'round', 'os.', 'json.')):
            if re.search(r'bpy\.(data|context)\.[\w.]*(update|evaluated_depsgraph_get)', ast.unparse(node)):
                return
            self.emit_unmapped(ast.unparse(node), 'call not in gui_map', indent)

    def operator(self, op, node, indent):
        spec = G.OPS.get(op)
        kw = {k.arg: k.value for k in node.keywords if k.arg}
        if spec is None:
            self.emit_unmapped(ast.unparse(node), f'operator bpy.ops.{op} not in gui_map; look under the '
                               f'"{op.split(".")[0]}" menus', indent)
            return
        text, labels = spec
        self.idnames.append(op)
        if op == 'object.transform_apply':
            flags = {k: self.ev(kw[k]) for k in ('location', 'rotation', 'scale') if k in kw}
            on = [k for k in ('location', 'rotation', 'scale') if flags.get(k, True) is True]
            pick = {('location', 'rotation', 'scale'): 'All Transforms', ('rotation', 'scale'): 'Rotation & Scale',
                    ('location',): 'Location', ('rotation',): 'Rotation', ('scale',): 'Scale',
                    ('location', 'rotation'): 'Location & Rotation', ('location', 'scale'): 'Location & Scale'
                    }.get(tuple(on), 'All Transforms')
            self.emit(f'Object ▸ Apply ▸ {pick} (Ctrl+A)', indent)
            return
        parts = []
        for key, label in labels.items():
            if key in kw:
                v = self.ev(kw[key])
                val = ast.unparse(kw[key]) if v is UNKNOWN else v
                if key in ('rotation',):
                    parts.append(self.axis_text(val, label, degrees=True) if v is not UNKNOWN else f'{label} {val}')
                elif key in ('location', 'scale') and v is not UNKNOWN:
                    parts.append(self.axis_text(val, label))
                else:
                    parts.append(f'{label} {self.fmt(val) if v is not UNKNOWN else val}')
        extra = [f'{k}={ast.unparse(v)}' for k, v in kw.items() if k not in labels]
        line = text
        if parts:
            line += ' — then in the Adjust Last Operation panel (bottom-left of the viewport): ' + '; '.join(parts)
        if extra:
            line += f'  [other options on the call: {", ".join(extra)}]'
        self.emit(line, indent)
        if op == 'mesh.primitive_cube_add' or op.startswith('mesh.primitive_'):
            self.kinds['__last_added__'] = ('object', None)

    def helper(self, name, node, indent):
        fn = self.funcs[name]
        if not self.mutates(fn):
            return                      # a pure function (it only computes a value): no step to take
        bound = {}
        params = [a.arg for a in fn.args.args]
        for p, a in zip(params, node.args):
            bound[p] = self.ev(a)
        for k in node.keywords:
            if k.arg:
                bound[k.arg] = self.ev(k.value)
        shown = ', '.join(f'{p}={self.fmt(v) if v is not UNKNOWN else "?"}' for p, v in bound.items())
        self.emit(f"Do the helper step '{name}' ({shown}):", indent)
        self.helpers.append(name)
        saved = dict(self.consts)
        for p, v in bound.items():
            if v is not UNKNOWN:
                self.consts[p] = v
        self._in_helper.add(name)
        self.block(fn.body, indent + 1)
        self._in_helper.discard(name)
        self.consts = saved

    # ---------------------------------------------------------------- attribute assignment
    def attr_assign(self, tgt, value, indent):
        path = ast.unparse(tgt)
        root = path.split('.')[0].split('[')[0]
        kind = self.kinds.get(root)
        if isinstance(value, ast.Name) and value.id.startswith('orig'):
            return                      # putting a setting back after a temporary change: not part of the model
        if kind and kind[0] == 'container':
            return                      # script bookkeeping (a dict or list), not the scene
        attr = tgt.attr if isinstance(tgt, ast.Attribute) else None
        if kind and kind[0] == 'modifier' and isinstance(tgt, ast.Attribute) and ast.unparse(tgt.value) == root:
            spec = G.MODIFIERS.get(kind[1])
            label = spec[2].get(attr) if spec else None
            self.emit(f'On the {spec[1] if spec else kind[1]} modifier set '
                      f'{label or attr + " (Python name)"} = {self.show(value)}', indent)
            self.settings[f'{kind[1].title()}.{attr}'] = self.show(value)
            return
        if kind and kind[0] == 'constraint' and isinstance(tgt, ast.Attribute) and ast.unparse(tgt.value) == root:
            spec = G.CONSTRAINTS.get(kind[1])
            label = spec[2].get(attr) if spec else None
            self.emit(f'On the {spec[1] if spec else kind[1]} constraint set '
                      f'{label or attr + " (Python name)"} = {self.show(value)}', indent)
            self.settings[f'{kind[1].title()}.{attr}'] = self.show(value)
            return
        m = re.search(r"inputs\[['\"](.+?)['\"]\]\.default_value$", path)
        if m:
            note = ''
            if 'Color' in m.group(1):
                note = (' (a colour: the call gives linear RGBA. The colour picker\'s RGB tab takes these '
                        'linear numbers; its Hex tab is the sRGB equivalent)')
            self.emit(f'{G.PRINCIPLED_PREFIX}{m.group(1)} = {self.show(value)}{note}', indent)
            self.settings[f'Material.{m.group(1)}'] = self.show(value)
            return
        if path == 'bpy.context.view_layer.objects.active':
            self.emit('Click the object in the Outliner to make it the active object', indent)
            return
        # object name tracking
        if attr == 'name' and isinstance(tgt.value, ast.Name) and root in self.kinds:
            nm = self.ev(value)
            self.kinds[root] = (self.kinds[root][0], nm if nm is not UNKNOWN else None)
            if self.module is None and nm is not UNKNOWN:
                self.module = nm
        if path.endswith('.data.name'):
            self.emit(f'Rename its data to {self.show(value)} (Object Data properties tab ▸ the name field at the top)', indent)
            return
        if attr == 'use_nodes':
            return                      # a material made in the interface already uses nodes
        if attr == 'name':
            self.emit(f'Rename {"the object" if not (kind and kind[1]) else repr(kind[1])} to {self.show(value)} '
                      f'(F2 over the viewport, or double-click it in the Outliner)', indent)
            return
        for suffix, hint in G.PROPS:
            if path.endswith(suffix) and (suffix != 'name' or path.endswith('.name')):
                deg = suffix == 'rotation_euler'
                who = ''
                if isinstance(tgt, ast.Attribute) and isinstance(tgt.value, ast.Name):
                    k = self.kinds.get(tgt.value.id)
                    if k and k[1]:
                        who = f' on {k[1]}'
                v = self.ev(value)
                if suffix in ('dimensions', 'location', 'scale', 'rotation_euler') and v is not UNKNOWN:
                    txt = self.axis_text(v, '', degrees=deg).strip()
                else:
                    txt = self.show(value, deg)
                if suffix == 'parent':
                    self.emit(f'Parent it to {txt}: {hint}', indent)
                else:
                    self.emit(f'{hint}{who} = {txt}', indent)
                self.settings[(f'{self.kinds[root][1]}.' if root in self.kinds and self.kinds[root][1] else '') + suffix] = txt
                return
        self.emit_approx(f'Set {path} = {self.show(value)} (a Python property: find the field with the same '
                         f'label in the Properties editor or the Sidebar)', indent)


def translate(code):
    tr = Translator()
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return {'gui': [f'UNMAPPED: the code does not parse ({e.msg}, line {e.lineno})'],
                'bl_idnames': [], 'settings': {}, 'unmapped': ['syntax error'], 'approx': 0,
                'module': None, 'helpers': [], 'changes_scene': True}
    tr.block(tree.body)
    return {'gui': tr.gui, 'bl_idnames': tr.idnames, 'settings': tr.settings,
            'unmapped': tr.unmapped, 'approx': tr.approx, 'module': tr.module,
            'helpers': tr.helpers, 'changes_scene': bool(tr.gui)}


# ---------------------------------------------------------------- cards

def parse_stage_map(spec):
    out = []
    for part in filter(None, (spec or '').split(',')):
        rng, _, stage = part.partition(':')
        a, _, b = rng.partition('-')
        out.append((int(a), int(b or a), stage))
    return out


def stage_for(seq, smap, default=''):
    for a, b, s in smap:
        if a <= seq <= b:
            return s
    return default


def first_error_line(text):
    for ln in text.splitlines():
        if 'rror' in ln:
            return ln.strip()[:200]
    return text.strip()[:200]


def build_cards(tape, tape_ref, smap=()):
    cards, failed_by_why, n = [], {}, 0
    for rec in tape:
        code = rec.get('code')
        if not code or not rec.get('mutates', True):
            continue
        tr = translate(code)
        if not tr['changes_scene'] and rec.get('status') != 'error':
            continue                            # inspection only: it looked, it did not change
        n += 1
        why_hint = (rec.get('why') or '').strip()
        card = {
            'id': f'S{n:03d}', 'stage': rec.get('stage') or stage_for(rec['seq'], smap),
            'module': tr['module'], 'goal': why_hint, 'goal_from': 'tape why' if why_hint else '',
            'start_state': '', 'why': '',
            'operation': {
                'python': {'source': 'tape', 'ref': f'{tape_ref}#{rec["seq"]}'},
                'gui': tr['gui'], 'gui_source': 'draft', 'no_gui_reason': '',
                'bl_idnames': sorted(set(tr['bl_idnames'])), 'helpers': sorted(set(tr['helpers']))},
            'settings': tr['settings'],
            'result': {'status': rec.get('status'), 'reply': (rec.get('result') or '')[:400], 'measured': {}},
            'tier': 'recorded',
            'evidence': [{'path': tape_ref, 'seq': rec['seq']}],
            'needs_author': ['why'] + (['goal'] if not why_hint else ['goal (confirm)']),
        }
        if rec.get('status') == 'error':
            card['excluded_from_procedure'] = True
            card['operation']['gui'] = ['(this command failed: it is not part of the procedure; see the card '
                                        'that corrects it)']
            failed_by_why[why_hint] = (card['id'], first_error_line(rec.get('result') or ''), rec['seq'])
        elif why_hint in failed_by_why and why_hint:
            fid, err, fseq = failed_by_why.pop(why_hint)
            card['correction'] = {'of': fid, 'evidence': f'{tape_ref}#{fseq}: {err}'}
        cards.append(card)
    return cards


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == 'gui':
        gp = argparse.ArgumentParser(prog='draft_steps.py gui')
        gp.add_argument('tape')
        gp.add_argument('--seq', type=int, required=True)
        a = gp.parse_args(argv[1:])
        rec = [json.loads(x) for x in open(a.tape) if x.strip()][a.seq - 1]
        t = translate(rec.get('code') or '')
        print('\n'.join(t['gui']))
        print(f"-- {len(t['unmapped'])} unmapped, {t['approx']} approximate, ops: {sorted(set(t['bl_idnames']))}")
        return 0
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('tape')
    ap.add_argument('--out', required=True)
    ap.add_argument('--tape-ref')
    ap.add_argument('--stage-map', default='')
    a = ap.parse_args(argv)
    tape = [json.loads(x) for x in open(a.tape) if x.strip()]
    cards = build_cards(tape, a.tape_ref or a.tape, parse_stage_map(a.stage_map))
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    with open(a.out, 'w') as f:
        for c in cards:
            f.write(json.dumps(c, ensure_ascii=False) + '\n')
    unm = sum(len(c['operation']['gui']) and sum(1 for ln in c['operation']['gui'] if ln.lstrip().startswith('UNMAPPED')) for c in cards)
    app = sum(1 for c in cards for ln in c['operation']['gui'] if ln.lstrip().startswith('~'))
    failed = sum(1 for c in cards if c.get('excluded_from_procedure'))
    print(f'{len(cards)} draft card(s) from {len(tape)} tape line(s): {failed} failed attempt(s), '
          f'{unm} UNMAPPED line(s), {app} approximate line(s) -> {a.out}')
    print('Every card still needs a human-authored goal and why, and its GUI lines followed by a person.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
