import React from 'react';
import { AbsoluteFill } from 'remotion';
import { z } from 'zod';
import { CLAUDE, CLAUDE_FONT } from '../tokens/claude';

/**
 * ClaudeChatShot — a still of the unified Claude desktop app (Chat | Code toggle,
 * "Reply" composer, Opus·effort·Manual footer, activity rows, file cards, document
 * side panel), recreated from reference screenshots Bear supplied 2026-10-12.
 * Cowork was merged into regular Claude (announced 2026-09-16): a "Cowork" task is
 * now an ordinary desktop chat with a folder added from the + menu.
 *
 * LIBRARY RUNG 2/3 of the lecture SHOW-THE-THING LAW: a faithful skin, not a recording.
 * Everything it displays must come from a real run, the docs, or the source chapter;
 * the `label` strip is on by default and says so. Render with
 *   npx remotion still ClaudeChatShot out.png --props=props.json --scale=2
 * and play the PNG on BrowserCapture (frame:'app') or any capture pattern.
 *
 * Sidebar names are generic by design; never copy a real user's project names in.
 */

const row = z.object({
  kind: z.enum(['user', 'assistant', 'activity', 'file']),
  text: z.string().default(''),
  /** activity: seconds shown after the label; file: "Document · MD" subtitle */
  meta: z.string().default(''),
  /** activity: true = animated three-dot "working" mark, false = feather "done" mark */
  working: z.boolean().default(false),
});

export const claudeChatShotSchema = z.object({
  sidebarProjects: z.array(z.string()).default(['Workshop', 'Notes', 'Research', 'Drafts']),
  sidebarToday: z.string().default('Workshop readiness packet'),
  title: z.string().default('Workshop readiness packet'),
  /** laptop icon with a green dot = chat is connected to the desktop (folder access). */
  connected: z.boolean().default(true),
  fileCount: z.number().default(0),
  rows: z.array(row).default([]),
  composerText: z.string().default(''),
  composerBusy: z.boolean().default(false),
  model: z.string().default('Opus 5.5'),
  effort: z.string().default('Medium'),
  mode: z.string().default('Manual'),
  greeting: z.string().default(''),
  /** document side panel (replaces the chat column, as in the real app at narrow widths) */
  panelTitle: z.string().default(''),
  panelExt: z.string().default('MD'),
  panelBody: z.string().default(''),
  /** body font size in px at 1080 design; long documents use a smaller size so the whole file shows */
  panelFont: z.number().default(38),
  label: z.string().default('Recreated screen from the Claude desktop app. Not a recording.'),
});
export type ClaudeChatShotProps = z.infer<typeof claudeChatShotSchema>;
export const claudeChatShotDefaultProps = claudeChatShotSchema.parse({});

const SERIF = CLAUDE_FONT.serif;
const SANS = CLAUDE_FONT.ui;
const W = 1920, H = 1080, SIDE = 420;

const Icon: React.FC<{ d: string; size?: number; color?: string; sw?: number }> = ({ d, size = 40, color = CLAUDE.INK, sw = 2 }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth={sw} strokeLinecap="round" strokeLinejoin="round"><path d={d} /></svg>
);
const PATHS = {
  search: 'M11 4a7 7 0 1 0 0 14 7 7 0 0 0 0-14zM21 21l-4.5-4.5',
  plus: 'M12 5v14M5 12h14',
  folder: 'M3 7h6l2 2h10v10H3z',
  globe: 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18',
  doc: 'M7 3h7l5 5v13H7zM14 3v5h5',
  chat: 'M4 5h12v9H9l-3 3v-3H4zM18 9h2v9h-2l-2 2v-2h-4v-2',
  code: 'M8 7l-5 5 5 5M16 7l5 5-5 5M14 5l-4 14',
  laptop: 'M5 6h14v9H5zM3 18h18',
  mic: 'M12 3a3 3 0 0 0-3 3v5a3 3 0 0 0 6 0V6a3 3 0 0 0-3-3zM6 11a6 6 0 0 0 12 0M12 17v4',
  chev: 'M6 9l6 6 6-6',
  eye: 'M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12zM12 9a3 3 0 1 0 0 6 3 3 0 0 0 0-6z',
  x: 'M6 6l12 12M18 6L6 18',
  feather: 'M20 4c-8 0-13 5-13 12l-3 4M20 4c0 8-5 13-12 13M14 10l-6 6',
  sliders: 'M5 4v7M5 15v5M12 4v2M12 10v10M19 4v9M19 17v3M3 11h4M10 8h4M17 15h4',
};

const Sidebar: React.FC<ClaudeChatShotProps> = (p) => (
  <div style={{ position: 'absolute', left: 0, top: 0, width: SIDE, height: H, background: '#F5F3EC', borderRight: `2px solid ${CLAUDE.BORDER}`, fontFamily: SANS, color: CLAUDE.INK }}>
    {/* window controls + Chat | Code toggle */}
    <div style={{ display: 'flex', alignItems: 'center', gap: 14, height: 84, paddingLeft: 28 }}>
      {['#FF5F57', '#FEBC2E', '#28C840'].map((c) => <span key={c} style={{ width: 20, height: 20, borderRadius: 10, background: c }} />)}
      <div style={{ marginLeft: 'auto', marginRight: 24, display: 'flex', padding: 5, borderRadius: 16, background: CLAUDE.PILL, gap: 4 }}>
        <div style={{ background: '#fff', borderRadius: 12, padding: '6px 20px', boxShadow: '0 1px 3px rgba(0,0,0,.1)' }}><Icon d={PATHS.chat} size={32} /></div>
        <div style={{ padding: '6px 20px' }}><Icon d={PATHS.code} size={32} color={CLAUDE.GHOST} /></div>
      </div>
    </div>
    <div style={{ margin: '14px 24px', height: 62, borderRadius: 14, background: '#fff', border: `2px solid ${CLAUDE.BORDER}`, display: 'flex', alignItems: 'center', gap: 14, paddingLeft: 18, fontSize: 28, color: CLAUDE.GHOST }}>
      <Icon d={PATHS.search} size={30} color={CLAUDE.INK_SOFT} />Search
    </div>
    <div style={{ margin: '8px 24px', display: 'flex', alignItems: 'center', gap: 16, fontSize: 30, height: 56 }}>
      <span style={{ width: 40, height: 40, borderRadius: 20, background: CLAUDE.PILL, display: 'grid', placeItems: 'center' }}><Icon d={PATHS.plus} size={26} /></span>New
    </div>
    {p.sidebarProjects.map((n) => (
      <div key={n} style={{ margin: '0 24px', display: 'flex', alignItems: 'center', gap: 16, fontSize: 30, height: 60, color: CLAUDE.INK }}>
        <Icon d={PATHS.folder} size={30} color={CLAUDE.INK_SOFT} />{n}
      </div>
    ))}
    <div style={{ position: 'absolute', left: 24, right: 24, top: 640, display: 'flex', justifyContent: 'space-between', fontSize: 32, color: CLAUDE.INK_SOFT }}>
      Today<Icon d={PATHS.sliders} size={28} color={CLAUDE.INK_SOFT} />
    </div>
    <div style={{ position: 'absolute', left: 14, right: 14, top: 688, height: 64, borderRadius: 14, background: '#EAE7DC', display: 'flex', alignItems: 'center', paddingLeft: 18, fontSize: 28, justifyContent: 'space-between', paddingRight: 24 }}>
      <span style={{ whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', maxWidth: 300 }}>{p.sidebarToday}</span><span style={{ flex: 'none', width: 14, height: 14, borderRadius: 7, background: p.composerBusy ? CLAUDE.SPARK : 'transparent' }} />
    </div>
    <div style={{ position: 'absolute', left: 0, right: 0, bottom: 0, height: 96, borderTop: `2px solid ${CLAUDE.BORDER}`, display: 'flex', alignItems: 'center', gap: 16, paddingLeft: 24, fontSize: 30 }}>
      <span style={{ width: 52, height: 52, borderRadius: 26, background: CLAUDE.PILL, display: 'grid', placeItems: 'center', fontSize: 28, fontWeight: 600 }}>YO</span>
      You <span style={{ color: CLAUDE.INK_SOFT }}>· Max</span>
    </div>
  </div>
);

const Header: React.FC<{ p: ClaudeChatShotProps; right: number }> = ({ p }) => (
  <div style={{ position: 'absolute', left: SIDE, right: 0, top: 0, height: 84, display: 'flex', alignItems: 'center', paddingLeft: 40, paddingRight: 36, fontFamily: SANS, color: CLAUDE.INK }}>
    <span style={{ fontSize: 32 }}>{p.title}</span>
    <span style={{ position: 'relative', marginLeft: 20 }}>
      <Icon d={PATHS.laptop} size={38} color={CLAUDE.INK_SOFT} />
      {p.connected && <span style={{ position: 'absolute', right: -4, top: -8, width: 14, height: 14, borderRadius: 7, background: '#1A9A3A' }} />}
    </span>
    <span style={{ marginLeft: 12 }}><Icon d={PATHS.chev} size={30} color={CLAUDE.INK_SOFT} /></span>
    <span style={{ marginLeft: 'auto', display: 'flex', alignItems: 'center', gap: 26 }}>
      <Icon d={PATHS.globe} size={38} />
      <span style={{ display: 'flex', alignItems: 'center', gap: 8, fontSize: 28 }}><Icon d={PATHS.doc} size={36} />{p.fileCount > 0 ? p.fileCount : ''}</span>
      <span style={{ border: `2px solid ${CLAUDE.BORDER}`, background: '#fff', borderRadius: 12, padding: '8px 22px', fontSize: 28 }}>Share</span>
    </span>
  </div>
);

const Composer: React.FC<{ p: ClaudeChatShotProps }> = ({ p }) => (
  <>
    <div style={{ position: 'absolute', left: SIDE + 100, right: 70, bottom: 130, minHeight: 100, borderRadius: 40, background: '#fff', border: `2px solid ${CLAUDE.BORDER}`, boxShadow: '0 4px 24px rgba(61,57,41,.08)', padding: '28px 36px', fontFamily: SANS, fontSize: 32, color: p.composerText ? CLAUDE.INK : CLAUDE.GHOST, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
      <span style={{ lineHeight: 1.4 }}>{p.composerText || 'Reply'}</span>
      <span style={{ width: 56, height: 56, borderRadius: 28, border: p.composerBusy ? `3px solid ${CLAUDE.INK}` : 'none', display: 'grid', placeItems: 'center', flex: 'none', marginLeft: 20 }}>
        {p.composerBusy ? <span style={{ width: 20, height: 20, background: CLAUDE.INK, borderRadius: 4 }} /> : <Icon d="M20 6v7H6M10 9l-4 4 4 4" size={34} color={CLAUDE.GHOST} />}
      </span>
    </div>
    <div style={{ position: 'absolute', left: SIDE + 120, right: 80, bottom: 64, display: 'flex', alignItems: 'center', gap: 30, fontFamily: SANS, fontSize: 30, color: CLAUDE.INK }}>
      <Icon d={PATHS.plus} size={36} /><Icon d={PATHS.mic} size={34} /><Icon d={PATHS.chev} size={26} color={CLAUDE.INK_SOFT} />
      <span style={{ marginLeft: 'auto' }}>{p.model} <span style={{ color: CLAUDE.INK_SOFT }}>{p.effort}</span></span>
      <span style={{ marginLeft: 36 }}>{p.mode}</span>
    </div>
  </>
);

const Rows: React.FC<{ p: ClaudeChatShotProps }> = ({ p }) => (
  <div style={{ position: 'absolute', left: SIDE + 100, right: 70, top: 130, bottom: 250, display: 'flex', flexDirection: 'column', gap: 34, overflow: 'hidden' }}>
    {p.rows.map((r, i) => {
      if (r.kind === 'user') return (
        <div key={i} style={{ alignSelf: 'flex-end', maxWidth: 1000, background: '#EFEDE4', borderRadius: 36, padding: '26px 34px', fontFamily: SANS, fontSize: 31, lineHeight: 1.4, color: CLAUDE.INK }}>{r.text}</div>);
      if (r.kind === 'assistant') return (
        <div key={i} style={{ fontFamily: SERIF, fontSize: 38, lineHeight: 1.45, color: CLAUDE.INK, padding: '0 20px' }}>{r.text}</div>);
      if (r.kind === 'activity') return (
        <div key={i} style={{ display: 'flex', alignItems: 'center', gap: 22, fontFamily: SANS, fontSize: 32, color: CLAUDE.INK_SOFT, padding: '0 20px' }}>
          {r.working
            ? <span style={{ color: CLAUDE.SPARK, fontSize: 40, letterSpacing: 4, lineHeight: 0.5 }}>• • •</span>
            : <Icon d={PATHS.feather} size={38} color={CLAUDE.SPARK} />}
          <span>{r.text}</span><span style={{ color: CLAUDE.GHOST }}>{r.meta}</span><Icon d="M9 6l6 6-6 6" size={26} color={CLAUDE.GHOST} />
        </div>);
      return (
        <div key={i} style={{ border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 28, background: '#fff', padding: 26, display: 'flex', alignItems: 'center', gap: 28, fontFamily: SANS, color: CLAUDE.INK }}>
          <div style={{ width: 100, height: 100, borderRadius: 18, background: '#F3F1EA', border: `2px solid ${CLAUDE.BORDER}`, display: 'grid', placeItems: 'center' }}><Icon d={PATHS.doc} size={46} color={CLAUDE.INK_SOFT} /></div>
          <div style={{ flex: 1 }}><div style={{ fontSize: 36 }}>{r.text}</div><div style={{ fontSize: 28, color: CLAUDE.INK_SOFT }}>{r.meta}</div></div>
          <div style={{ border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 16, padding: '14px 28px', fontSize: 32, display: 'flex', gap: 18, alignItems: 'center' }}>Download<Icon d={PATHS.chev} size={26} color={CLAUDE.INK_SOFT} /></div>
        </div>);
    })}
  </div>
);

/** minimal markdown / csv renderer for the document panel */
const Doc: React.FC<{ body: string; ext: string; fs: number }> = ({ body, ext, fs }) => {
  if (ext.toUpperCase() === 'CSV') {
    const lines = body.trim().split('\n').map((l) => l.split(','));
    return (
      <table style={{ borderCollapse: 'collapse', width: '100%', fontFamily: SERIF, fontSize: fs }}>
        <thead><tr>{lines[0].map((c, i) => <th key={i} style={{ textAlign: 'left', padding: '16px 20px', borderBottom: `3px solid ${CLAUDE.INK}`, fontWeight: 700 }}>{c}</th>)}</tr></thead>
        <tbody>{lines.slice(1).map((r, i) => <tr key={i}>{r.map((c, j) => <td key={j} style={{ padding: '16px 20px', borderBottom: `2px solid ${CLAUDE.BORDER}` }}>{c}</td>)}</tr>)}</tbody>
      </table>);
  }
  const out: React.ReactNode[] = [];
  body.split('\n').forEach((l, i) => {
    if (!l.trim()) return;
    if (l.startsWith('# ')) out.push(<h1 key={i} style={{ fontSize: Math.round(fs * 1.55), margin: '0 0 24px', lineHeight: 1.1 }}>{l.slice(2)}</h1>);
    else if (l.startsWith('## ')) out.push(<h2 key={i} style={{ fontSize: Math.round(fs * 1.2), margin: '28px 0 12px' }}>{l.slice(3)}</h2>);
    else if (l.startsWith('- ')) out.push(<div key={i} style={{ fontSize: fs, lineHeight: 1.45, paddingLeft: 36 }}>• {l.slice(2)}</div>);
    else out.push(<p key={i} style={{ fontSize: fs, lineHeight: 1.45, margin: '0 0 16px' }}>{l}</p>);
  });
  return <>{out}</>;
};

const Panel: React.FC<{ p: ClaudeChatShotProps }> = ({ p }) => (
  <div style={{ position: 'absolute', left: SIDE, right: 0, top: 0, bottom: 0, background: '#fff', fontFamily: SANS, color: CLAUDE.INK }}>
    <div style={{ height: 96, borderBottom: `2px solid ${CLAUDE.BORDER}`, display: 'flex', alignItems: 'center', paddingLeft: 34, paddingRight: 36, gap: 26, fontSize: 34 }}>
      <span style={{ display: 'flex', gap: 6, padding: 5, borderRadius: 16, background: CLAUDE.PILL }}>
        <span style={{ background: '#fff', borderRadius: 12, padding: '6px 18px' }}><Icon d={PATHS.eye} size={34} /></span>
        <span style={{ padding: '6px 18px' }}><Icon d={PATHS.code} size={34} color={CLAUDE.INK_SOFT} /></span>
      </span>
      <span>{p.panelTitle} <span style={{ color: CLAUDE.INK_SOFT }}>· {p.panelExt}</span></span>
      <span style={{ marginLeft: 'auto', border: `2px solid ${CLAUDE.BORDER}`, borderRadius: 16, padding: '10px 26px', fontSize: 32 }}>Copy</span>
      <Icon d={PATHS.x} size={40} />
    </div>
    <div style={{ padding: '60px 110px', fontFamily: SERIF }}><Doc body={p.panelBody} ext={p.panelExt} fs={p.panelFont} /></div>
  </div>
);

export const ClaudeChatShot: React.FC<ClaudeChatShotProps> = (p) => (
  <AbsoluteFill style={{ background: CLAUDE.PAGE, width: W, height: H }}>
    <Sidebar {...p} />
    {p.panelTitle ? <Panel p={p} /> : (
      <>
        <Header p={p} right={0} />
        {p.greeting
          ? <div style={{ position: 'absolute', left: SIDE, right: 0, top: 300, textAlign: 'center', fontFamily: SERIF, fontSize: 84, color: CLAUDE.INK }}><span style={{ color: CLAUDE.SPARK }}>✺ </span>{p.greeting}</div>
          : <Rows p={p} />}
        <Composer p={p} />
      </>
    )}
    {p.label && (
      <div style={{ position: 'absolute', left: SIDE, right: 0, bottom: 8, textAlign: 'center', fontFamily: SANS, fontSize: 32, color: CLAUDE.INK }}>{p.label}</div>
    )}
  </AbsoluteFill>
);
