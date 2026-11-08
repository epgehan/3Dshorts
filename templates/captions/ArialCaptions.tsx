import React, {useEffect, useState} from 'react';
import {AbsoluteFill, cancelRender, continueRender, delayRender, useCurrentFrame, useVideoConfig} from 'remotion';

export type CaptionCue = {startFrame: number; endFrame: number; text: string};
export type ArialCaptionProps = {cues: CaptionCue[]; arialBoldUrl: string; fontSize?: number; bottomFraction?: number};

/** Original overlay: requires an actual supplied Arial Bold font asset; never silently substitutes. */
export const ArialCaptions: React.FC<ArialCaptionProps> = ({cues, arialBoldUrl, fontSize, bottomFraction}) => {
  const frame = useCurrentFrame();
  const {width, height} = useVideoConfig();
  const [handle] = useState(() => delayRender('Load supplied Arial Bold caption font'));
  useEffect(() => {
    let cancelled = false;
    const face = new FontFace('ClipScoutArial', `url(${JSON.stringify(arialBoldUrl)})`, {weight: '700', style: 'normal'});
    face.load().then((loaded) => {
      if (cancelled) return;
      document.fonts.add(loaded);
      continueRender(handle);
    }).catch((error: unknown) => {if (!cancelled) cancelRender(new Error(`Arial font failed to load: ${String(error)}`));});
    return () => {cancelled = true; document.fonts.delete(face);};
  }, [arialBoldUrl, handle]);
  let previousEnd = -1;
  for (const cue of cues) {
    if (!Number.isInteger(cue.startFrame) || !Number.isInteger(cue.endFrame) || cue.startFrame < 0 || cue.endFrame <= cue.startFrame || cue.startFrame < previousEnd) {
      throw new Error('Caption cues require ordered, nonoverlapping integer half-open frame intervals.');
    }
    previousEnd = cue.endFrame;
  }
  const cue = cues.find((item) => frame >= item.startFrame && frame < item.endFrame);
  if (!cue) return null;
  return <AbsoluteFill style={{pointerEvents: 'none', zIndex: 1000}}>
    <div style={{position: 'absolute', left: '5%', width: '90%', bottom: height * (bottomFraction ?? (height > width ? .22 : .10)), textAlign: 'center', fontFamily: 'ClipScoutArial', fontWeight: 700, fontStyle: 'normal', fontSize: fontSize ?? width * (70 / 1080), lineHeight: 1.02, color: '#FFFFFF', WebkitTextStroke: `${width * (6 / 1080)}px #000000`, paintOrder: 'stroke fill', textTransform: 'uppercase', whiteSpace: 'normal'}}>
      {cue.text.toUpperCase()}
    </div>
  </AbsoluteFill>;
};
