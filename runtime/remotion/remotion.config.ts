import {Config} from '@remotion/cli/config';

// Remotion 4.0.534 effects (grayscale, duotone, halftone, vignette, …) use WebGL2.
// The remotion-markup skill says to set this once for Studio and CLI.
Config.setChromiumOpenGlRenderer('angle');
