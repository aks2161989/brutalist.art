#!/usr/bin/env python3
"""The tape: a line-by-line record of every command that built a model in Blender.

Two ways to get one.

RECORD a build as it happens, through the Blender MCP add-on's socket (the same JSON wire
protocol the `mcp-for-blender` server forwards Claude's tool calls over: one JSON object
`{"type": <command>, "params": {...}}` per request, port 9876). Use this instead of a bare
socket client and every command, its reason, its reply and its duration land in a JSONL file:

  tape.py code "import bpy; print(len(bpy.data.objects))" --tape T.jsonl --stage 04-blockout --why "count what exists"
  tape.py run  build_part.py --tape T.jsonl --stage 06-modules --label "window module"
  tape.py call get_scene_info --tape T.jsonl

HARVEST a build that already happened, from Claude Code transcripts (stream-json from
`claude -p`, or the project transcripts in ~/.claude/projects). Every tool call whose name
mentions Blender, and every Bash command that runs Blender, becomes a tape line, with the
reply that came back:

  tape.py harvest session/turn1.jsonl session/turn2.jsonl --out T.jsonl [--no-bash] [--resolve-scripts]

  tape.py show T.jsonl [--seq 12]

A tape line is evidence of what was SENT and what came BACK. It is not proof the model on disk
still matches: for that, census the file (census.py). Transcripts carry no wall-clock time
unless the line has a `timestamp`; the tape says so rather than inventing one.

Tape line:
  {"seq", "source": "live"|"transcript", "tool", "t_utc", "stage", "label", "why", "code",
   "code_sha256", "params", "status": "ok"|"error"|"unknown", "result", "duration_s",
   "session", "tool_use_id", "script_path", "script_sha256", "script_read": "at-record"|"now"}
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import socket
import sys

DEFAULT_PORT = int(os.environ.get('BLENDER_MCP_PORT', '9876'))
RESULT_LIMIT = 4000
MUTATING_QUERY_TOOLS = {'get_scene_info', 'get_object_info', 'look', 'get_addon_status',
                        'get_viewport_screenshot'}


def sha256_text(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def now_utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')


def next_seq(path):
    if not Path(path).exists():
        return 1
    n = 0
    with open(path) as f:
        for line in f:
            if line.strip():
                n += 1
    return n + 1


def append(path, rec):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    rec = dict(rec)
    rec['seq'] = next_seq(path)
    with open(path, 'a') as f:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')
    return rec['seq']


def read_tape(path):
    out = []
    with open(path) as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except ValueError as e:
                    raise SystemExit(f'{path}:{i}: not JSON ({e})')
    return out


# ---------------------------------------------------------------- live recording

def send(cmd_type, params, port=DEFAULT_PORT, host='localhost', timeout=900):
    """One request to the Blender MCP add-on; returns the parsed reply (never raises on a
    refused connection: the failure is the reply, so it lands on the tape too)."""
    try:
        s = socket.create_connection((host, port), timeout=timeout)
    except OSError as e:
        return {'status': 'error', 'message': f'cannot reach Blender on {host}:{port}: {e}'}
    try:
        s.sendall(json.dumps({'type': cmd_type, 'params': params}).encode())
        buf = b''
        while True:
            chunk = s.recv(65536)
            if not chunk:
                break
            buf += chunk
            try:
                return json.loads(buf.decode())
            except ValueError:
                continue
        return {'status': 'error', 'message': 'connection closed before a full reply: '
                + buf[:200].decode('utf8', 'replace')}
    finally:
        s.close()


def reply_text(reply):
    if not isinstance(reply, dict):
        return str(reply)
    res = reply.get('result')
    if isinstance(res, dict):
        res = res.get('result', res)
    parts = [str(x) for x in (res, reply.get('message')) if x not in (None, '')]
    return '\n'.join(parts)


def reply_status(reply):
    if not isinstance(reply, dict):
        return 'unknown'
    return 'ok' if reply.get('status') in ('success', 'ok') else 'error'


class Tape:
    def __init__(self, path, stage='', port=DEFAULT_PORT, host='localhost'):
        self.path, self.stage, self.port, self.host = str(path), stage, port, host

    def call(self, cmd_type, label='', why='', stage=None, script_path=None, record_code=None, **params):
        import time
        t0 = time.time()
        reply = send(cmd_type, params, self.port, self.host)
        rec = {'source': 'live', 'tool': cmd_type, 't_utc': now_utc(),
               'stage': stage if stage is not None else self.stage, 'label': label, 'why': why,
               'status': reply_status(reply), 'result': reply_text(reply)[:RESULT_LIMIT],
               'duration_s': round(time.time() - t0, 3)}
        code = record_code if record_code is not None else params.get('code')
        if code is not None:
            rec['code'], rec['code_sha256'] = code, sha256_text(code)
        else:
            rec['params'] = params
        if script_path:
            rec['script_path'], rec['script_read'] = str(script_path), 'at-record'
            rec['script_sha256'] = sha256_text(code or '')
        rec['mutates'] = cmd_type not in MUTATING_QUERY_TOOLS
        seq = append(self.path, rec)
        return seq, reply

    def code(self, code, **kw):
        return self.call('execute_code', code=code, **kw)

    def run_file(self, path, **kw):
        """exec a file inside Blender (module state persists between calls, like mcp_client.run_file),
        recording the FILE'S CONTENT, so the tape holds what actually ran."""
        text = Path(path).read_text()
        wrapped = f'__file__ = {str(path)!r}\nexec(compile(open({str(path)!r}).read(), {str(path)!r}, "exec"), globals())\n'
        return self.call('execute_code', script_path=path, code=wrapped, record_code=text, **kw)


# ---------------------------------------------------------------- harvest

def blocks(line):
    msg = line.get('message')
    content = msg.get('content') if isinstance(msg, dict) else None
    return content if isinstance(content, list) else []


def result_text(content):
    if isinstance(content, str):
        s = content
    elif isinstance(content, list):
        s = ''.join(b.get('text', '') for b in content if isinstance(b, dict) and b.get('type') == 'text')
    else:
        s = ''
    try:
        j = json.loads(s)
        if isinstance(j, dict) and 'result' in j:
            s = str(j['result'])
    except ValueError:
        pass
    return s


def looks_failed(text, is_error):
    return bool(is_error) or bool(re.search(r'Traceback|Error executing|Code execution error|^Error', text, re.M))


def blender_bash(cmd):
    return bool(re.search(r'[Bb]lender', cmd)) and bool(re.search(r'(--python\b|-b\b|--background)', cmd))


def script_in(cmd):
    m = re.search(r'--python(?:-expr)?\s+("[^"]+"|\'[^\']+\'|\S+)', cmd)
    return m.group(1).strip('"\'') if m else None


def harvest(paths, match='blender', include_bash=True, resolve_scripts=False):
    recs = []
    for p in paths:
        pending = {}
        session = None
        with open(p) as f:
            for raw in f:
                raw = raw.strip()
                if not raw.startswith('{'):
                    continue
                try:
                    line = json.loads(raw)
                except ValueError:
                    continue
                session = line.get('session_id') or session
                ts = line.get('timestamp')
                for b in blocks(line):
                    if not isinstance(b, dict):
                        continue
                    if b.get('type') == 'tool_use':
                        name, inp = b.get('name', ''), b.get('input') or {}
                        is_mcp = bool(re.search(match, name, re.I))
                        is_bash = include_bash and name == 'Bash' and blender_bash(inp.get('command', ''))
                        if not (is_mcp or is_bash):
                            continue
                        rec = {'source': 'transcript', 'tool': name, 'session': session,
                               'tool_use_id': b.get('id'), 'transcript': str(p),
                               't_utc': ts or None, 'stage': '', 'label': '',
                               'why': inp.get('user_prompt') or inp.get('description') or ''}
                        if 'code' in inp:
                            rec['code'], rec['code_sha256'] = inp['code'], sha256_text(inp['code'])
                        elif is_bash:
                            cmd = inp['command']
                            rec['code'], rec['code_sha256'] = cmd, sha256_text(cmd)
                            sp = script_in(cmd)
                            if sp:
                                rec['script_path'] = sp
                                if resolve_scripts and Path(sp).exists():
                                    text = Path(sp).read_text()
                                    rec['script_sha256'] = sha256_text(text)
                                    rec['script_read'] = 'now'
                                    rec['script_text'] = text
                        else:
                            rec['params'] = inp
                        rec['mutates'] = rec.get('code') is not None or \
                            name.rsplit('__', 1)[-1] not in MUTATING_QUERY_TOOLS
                        rec['status'], rec['result'], rec['duration_s'] = 'unknown', '', None
                        pending[b['id']] = rec
                        recs.append(rec)
                    elif b.get('type') == 'tool_result' and b.get('tool_use_id') in pending:
                        rec = pending[b['tool_use_id']]
                        text = result_text(b.get('content'))
                        rec['result'] = text[:RESULT_LIMIT]
                        rec['status'] = 'error' if looks_failed(text, b.get('is_error')) else 'ok'
    return recs


def write_harvest(recs, out):
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    with open(out, 'w') as f:
        for i, r in enumerate(recs, 1):
            r = dict(r)
            r['seq'] = i
            f.write(json.dumps(r, ensure_ascii=False) + '\n')


# ---------------------------------------------------------------- show

def show(path, seq=None):
    recs = read_tape(path)
    if seq:
        r = recs[seq - 1]
        print(json.dumps(r, indent=2, ensure_ascii=False))
        return
    ok = sum(r.get('status') == 'ok' for r in recs)
    bad = sum(r.get('status') == 'error' for r in recs)
    print(f'{path}: {len(recs)} lines ({ok} ok, {bad} error, {len(recs) - ok - bad} unknown)')
    for r in recs:
        code = (r.get('code') or json.dumps(r.get('params') or {}))
        first = next((ln for ln in code.splitlines() if ln.strip() and not ln.strip().startswith('#')), '')
        print(f"  {r['seq']:>3} {r.get('status', '?'):<7} {r.get('tool', ''):<38} "
              f"{(r.get('stage') or '-'):<14} {first.strip()[:70]}")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    sub = ap.add_subparsers(dest='cmd', required=True)

    def live(p):
        p.add_argument('--tape', required=True)
        p.add_argument('--stage', default='')
        p.add_argument('--label', default='')
        p.add_argument('--why', default='')
        p.add_argument('--port', type=int, default=DEFAULT_PORT)
    c = sub.add_parser('code')
    c.add_argument('python')
    live(c)
    r = sub.add_parser('run')
    r.add_argument('file')
    live(r)
    k = sub.add_parser('call')
    k.add_argument('type')
    k.add_argument('--params', default='{}')
    live(k)
    h = sub.add_parser('harvest')
    h.add_argument('transcripts', nargs='+')
    h.add_argument('--out', required=True)
    h.add_argument('--match', default='blender', help='regex for MCP tool names')
    h.add_argument('--no-bash', action='store_true')
    h.add_argument('--resolve-scripts', action='store_true',
                   help='read the scripts a Bash call ran from disk NOW (they may have changed since)')
    s = sub.add_parser('show')
    s.add_argument('tape')
    s.add_argument('--seq', type=int)
    a = ap.parse_args(argv)

    if a.cmd in ('code', 'run', 'call'):
        t = Tape(a.tape, a.stage, a.port)
        kw = {'label': a.label, 'why': a.why}
        if a.cmd == 'code':
            seq, reply = t.code(a.python, **kw)
        elif a.cmd == 'run':
            seq, reply = t.run_file(os.path.abspath(a.file), **kw)
        else:
            seq, reply = t.call(a.type, **kw, **json.loads(a.params))
        print(f'tape #{seq} [{reply_status(reply)}]')
        print(reply_text(reply)[:2000])
        return 0 if reply_status(reply) == 'ok' else 1
    if a.cmd == 'harvest':
        recs = harvest(a.transcripts, a.match, not a.no_bash, a.resolve_scripts)
        write_harvest(recs, a.out)
        mut = sum(1 for r in recs if r.get('mutates'))
        print(f'harvested {len(recs)} Blender call(s) ({mut} that change the scene) -> {a.out}')
        return 0
    show(a.tape, a.seq)
    return 0


if __name__ == '__main__':
    sys.exit(main())
