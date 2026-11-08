# Outlines and edge treatment

## Observed scope

This report combines the seven full-duration overview sheets, the character/native-frame reports, and selected threshold probes. All native sources are360×640. H.264 compression, antialiasing, soft focus and the JPEG quality93 inspection export limit thin-line interpretation. A measured dark run across a row is not necessarily a vector stroke width: curve angle, a nearby dark region, hair and shadows can widen it. Contour placement is more reliable than a single universal pixel value.

## Character ink

Cashiers f00120(4.000s) is a useful large face. On source inspection rowy240, maximum-RGB<110 selects dark runs atx102–111 andx298–307, each10native pixels. These locations coincide with left/right head-boundary regions. They include blur/edge thickness and are not a recovered pen width. Mirror f00300(10.000s), rowy280, contains a right head-edge dark runx280–289 and a much narrower left-side runx113–115; background, eye, hair and overlap make other runs unsuitable as outline samples. The character report's manual boundary estimates are correspondingly approximate. Knight f00930(31.000s) has layered armor/helmet edges, which should not be collapsed into the generic head contour.

The reliable instruction is to preserve a dark plum/near-black face silhouette, generally heavier than most facial marks, that remains legible after output downsampling. Scale character strokes with the character artwork, then judge screen-space visibility at the final shot size. Do not transplant the old bridge world's3px-at1080 rule onto a close-up face. That would be about1pixel at this source size, far below some observed close-up silhouette bands.

Eyes, brows and mouths form sparse independent marks. Half-lids can be gray/softened by lighting and compression; not every pupil has the same value as the outer ink. Closed-eye expression marks can be short curves, not literal blinking eyelid meshes. Reference captions have their own black edge; never use those edges as character-line measurements.

## World ink is material- and shot-dependent

Mirror's room, counter and floor seams support depth with selective dark edges. Knight's chest, armor, stall and timber retain decorative outlined structure. Railroads' ballast and canyon contain dense shape boundaries and tonal texture that cannot all be called a uniform black contour pass. Sample-1's reflective cars and wet environments preserve highlights and surface reflections without equally heavy ink around every reflection. Shape's coaster repeatedly uses geometry silhouettes and rails against the sky. These require different edge densities.

Apply contours at meaningful silhouettes, prop seams, plate overlaps and major depth discontinuities. Avoid outlining every normal change, floor-to-wall contact and tiny texture fleck. Adjacent texture edges should not flicker as a moving camera crosses a low-resolution pixel grid. A static image-wide edge detector would also ink caption edges, car highlights, reflections and noisy leaves indiscriminately; it is not evidence of the original technique and is a poor universal replacement.

## Recommended implementation

- Draw character linework into the character artwork. Exclude it from a second world-ink pass; use a layer flag or an equivalent compositing separation.
- Use separate outline intensity/width controls for wood/stone sets, detailed rock/ballast, reflective vehicles and background scenery. These are controls to tune, not recovered source settings.
- Preserve broad graphic clothing fills and sparse seams. Allow selective hair and armor shading while keeping head/limb geometry flat.
- Process scene ink before scene blur so a defocused doorway also has defocused lines; draw subtitles afterward.
- Check alpha edges and mipmaps on cards at near, medium and far sizes. Reject dark rectangular fringes, halos around cutouts and a second contour displaced from the original.
- Scale pixel effects with output size. A360px study image stretched to1080px does not reveal new pen detail; judge relative silhouette weight, not upscaled artifacts.

## Verification samples

Review cashiers f00120 for face contrast, mirror f00300 for scaled head ink, knight f00570 andf00930 for armor layering, railroads f01290/f01650 for dense scenery versus a sparse actor, and sample-1 f01260 for pale characters against a dark world. Compare near and far outlines in the same scene. Do not require every dark edge to have identical thickness or color.
