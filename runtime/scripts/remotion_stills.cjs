// Canonical serial still preflight, invoked only by remotion_scenes.py --stills.
// One browser, one bundle, one frame at a time. Does not render production clips.
const fs = require('fs');
const path = require('path');
const {createRequire} = require('module');
async function main() {
  const [project, manifestPath] = process.argv.slice(2);
  const req = createRequire(path.join(project, 'package.json'));
  const {bundle} = req('@remotion/bundler');
  const {openBrowser, selectComposition, renderStill} = req('@remotion/renderer');
  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  const serveUrl = await bundle({entryPoint: path.join(project, 'src/index.ts'),
    publicDir: path.join(project, 'public'), symlinkPublicDir: true});
  const browser = await openBrowser('chrome', process.env.ART_CHROME ?
    {browserExecutable: process.env.ART_CHROME} : {});
  const rows = [];
  try {
    for (const beat of manifest.beats) {
      const composition = await selectComposition({serveUrl, id: beat.pattern,
        inputProps: beat.props, puppeteerInstance: browser});
      for (const fraction of [.25, .5, .95]) {
        const frame = Math.min(composition.durationInFrames - 1,
          Math.floor(fraction * composition.durationInFrames));
        const output = path.join(manifest.out, `${beat.beat_id}-${Math.round(fraction*100)}.png`);
        await renderStill({serveUrl, composition, inputProps: beat.props,
          output, frame, scale: .5, imageFormat: 'png', puppeteerInstance: browser});
        rows.push({beat: beat.beat_id, pattern: beat.pattern, fraction, frame, output});
      }
      process.stdout.write(`[preflight] ${beat.beat_id}: 25/50/95% at 960x540\n`);
    }
    fs.writeFileSync(path.join(manifest.out,'receipt.json'),JSON.stringify({
      status:'Rendered for visual inspection; not a visual PASS', scale:.5,
      concurrency:1, rows},null,2)+'\n');
  } finally {
    await browser.close({silent:true});
  }
}
main().catch(error=>{process.stderr.write(String(error)+'\n'); process.exitCode=2;});
