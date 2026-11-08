# Arial subtitle overlay

Copy `ArialCaptions.tsx` into a configured React/Remotion project. Supply a usable licensed Arial Bold file in the project's public font folder; the repository does not redistribute Microsoft's font file.

```tsx
<ArialCaptions
  arialBoldUrl={staticFile('fonts/arial-bold.ttf')}
  cues={[
    {startFrame: 0, endFrame: 18, text: 'AN ORIGINAL'},
    {startFrame: 18, endFrame: 38, text: 'STORY'},
  ]}
/>
```

Import `staticFile` from `remotion`. Place the overlay after the scene/post layer in a root composition. Cues are reviewed integer frame ranges, not seconds. No active-word color is applied. The component validates interval ordering and blocks capture until the font loads; it does not transcribe, auto-fit long text, author the scene or prove compatibility with an unspecified host project. Fit long words/grouping and inspect output before rendering.
