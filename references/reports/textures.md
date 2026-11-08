# Materials, textures and environment construction — seven-video study

## Scope and confidence

Observed all seven overview contact sheets and these **native 360×640, 30 fps** frames (zero-based frame / timestamp): mirror 210/7.00 s and 1200/40.00 s; knight 570/19.00 s and 930/31.00 s; spot 210/7.00 s and 1590/53.00 s; cashiers 0/0.00 s and 510/17.00 s; shape 510/17.00 s and 1470/49.00 s; railroads 210/7.00 s and 1290/43.00 s; sample-1 720/24.00 s and 1110/37.00 s. Sources live privately under `<private-study>/<id>/frames/`. Overview sheets establish variation across each video; named native frames support the detailed observations below. This is visual study, not a reconstruction of assets or shaders.

Numerical ranges below are manual **screen-space estimates**, generally ±1–2 px for thin marks, not calibrated algorithmic line-width measurements. Compression, antialiasing, blur, perspective, highlights and possible edge enhancement prevent exact material/roughness/normal recovery. At this source resolution a 1 px mark can be a painted seam, modeled edge, shadow or post outline. Do not claim a physically based material value was measured. The old DESIGN_GUIDE is a useful prior but these videos supersede claims of uniformly sparse texture or uniformly matte worlds. Current caption requirement is ALL CAPS Arial, white with black outline; source subtitle styling is not a materials instruction.

## The main result

The stable grammar is **simple graphic characters against substantially dimensional sets**, not one universal flat material preset. The set must have coherent perspective, overlap, repeated construction units and directional lighting. Surface detail can be sparse (knight stall), moderately illustrated (mirror floor, cashiers counter), or comparatively realistic/dense (railroads ballast, sample-1 vehicles and pool). Faces remain broad pale regions with sparse dark marks throughout. Gloss on a car or rail is compatible with this grammar; shiny spherical skin is not.

Material identity usually comes from a hierarchy: silhouette and construction first, broad value/color divisions second, a small number of seams/highlights third, fine variation last. Set detail is often denser around the ground/props and restrained behind a face. Blur and framing further control that hierarchy.

## Per-video evidence and differences

| Video / native evidence | Visible material construction | Practical consequence |
|---|---|---|
| mirror f210, 7.00 s | Warm timber floor has converging plank seams, uneven brown patches and isolated dark knots; blue upholstered/painted bench has broad pale streaks. Exterior is lighter and softer than foreground boards. | Use actual perspective floor geometry or UVs, several plank color variants and sparse irregular knots; a flat orange plane misses a major depth cue. |
| mirror f1200, 40.00 s | Green felt-like counter is dark, softly mottled and low-gloss; reddish wood facade has large panel divisions and a few thin streaks. Paper money is planar, pale and sharply folded/blocky. | Distinguish cloth/felt top from paneled wood even with similar overall darkness. Counter should not reflect the face like a polished mirror. |
| knight f570, 19.00 s | Stall uses large smooth wooden boards, outlined construction borders, alternating red/cream awning segments with scalloped points and tiny tassels. Armor has blue-gray gradients and bright edge patches. | Let awning structure and repeated blocks identify cloth; no woven texture needed. Armor needs selective highlights and rivets, not realistic scratched steel everywhere. |
| knight f930, 31.00 s | Large armor close-up shows smooth cool silver-blue regions, white highlight along upper helmet/shoulder, outlined layered plates, isolated pale round rivets; face remains much flatter. Forest background is heavily soft. | Plate construction and contour carry metal. Restrict wear/noise. Do not transfer helmet shading to the face. |
| spot f210, 7.00 s | Bank/store glazing is amber with broad diagonal lighter streaks, transparent-looking dark interior figures, strong dark mullions. Foreground pavement is a perspective tile grid with muted variation. | Glass reads through frame structure, tint, transmission and broad reflections. A fully opaque cyan sheet or invisible clear sheet loses this cue. |
| spot f1590, 53.00 s | Security counter is white and navy with outlined panel edges, narrow gold trims, matte box/card surfaces and mostly smooth walls. Glass booth has pale blue-gray broad tonal regions. | Modern institutional set needs clean large planes plus selected seams and hardware; avoid applying wood grain or stipple to every surface. |
| cashiers f0, 0.00 s | Gray countertop has an uneven broad light patch; wood fascia is ochre with vertical plank joins, darker lower/edge areas and sparse streaks. Green wall is gently cloudy; ceiling tiles have a fine perspective grid. | Three construction systems—counter, wall paneling, ceiling—give depth without tiny decorative clutter. |
| cashiers f510, 17.00 s | Close-up red uniform has broad red value bands with a few edges/buttons/badges; no cloth weave. Behind it, wood bands and wall are softer, lower-detail fields. | Character clothing is graphic and flat relative to the set. Avoid fabric normal maps and dense folds on card figures. |
| shape f510, 17.00 s | Night park mixes dark trees/grass with simple sky, outlined/luminous cloud edges and concentrated bright ride lighting. Ground has broad soft light pools. | Lighting can temporarily dominate material read. Do not infer a reflective floor merely from the broad luminous pool. |
| shape f1470, 49.00 s | Bright smooth tubular coaster rails with white/silver highlights and dark structural undersides; green lawn is low-frequency with scattered variation; distant trees are clustered masses. | Repeated rail ties/supports and tube highlights create engineering scale; fine grass strands are unnecessary in this wide view. |
| railroads f210, 7.00 s | Deep blue water/gorge is largely smooth with broad tonal change and subdued cliff reflection/tint. Crane timber and ropes are clearly dimensional. | Do not use turbulent ocean waves by default; the water is a large quiet depth field in this shot. |
| railroads f1290, 43.00 s | Foreground ballast consists of many irregular individually shaded tan/gray/white stones. Steel rail has bright yellow-white upper edge, dark brown web, round fasteners. Cliff is warm banded/faceted rock with broad diagonal layers. Green crate has repeated slats. | This video is substantially denser than the old sparse-texture prior. Geometric ballast and stratified cliffs are warranted near the camera, but thin linework need not trace every stone. |
| sample-1 f720, 24.00 s | Red and turquoise cars have hard panels, glass windows, dark wheels, thin seams and broad bright specular patches. Road is dark and fairly smooth; trees/houses form detailed layered scenery. | Gloss belongs to selected manufactured materials. Material contrast comes from broad reflections plus panel geometry, not all-over microdetail. |
| sample-1 f1110, 37.00 s | Pool is vivid cyan with dark reflection of stick legs, bright vertical lamp streaks and a pale rim. Duck has a bright glossy upper highlight; siding has horizontal seams. Warm bulbs bloom against dark foliage. | This water treatment differs from railroads: reflection and local light streaks are central. Keep reflections stylized and legible; do not replace with opaque flat blue. |

## Screen-space construction estimates

These estimates are useful composition targets at 360 px width, not universal asset sizes. Multiply by 3 for 1080 px-wide output, or by 4 for 1440 px-wide output **only when preserving the same framing**. World-space textures must still foreshorten naturally.

| Sample | Approximate visible scale at native width | Interpretation |
|---|---|---|
| mirror f210 lower floor | Plank widths roughly 35–70 px near bottom; dark joins roughly 1–3 px; knots often 2–7 px | Large converging strips and sparse marks, not dense fine grain. |
| cashiers f0 lower counter fascia | Vertical boards roughly 25–45 px wide; joins approximately 1–2 px, with broader shaded edge zones | Board rhythm is visible; individual wood fibers are not required. |
| spot f210 foreground pavement | Front tile cells roughly 75–110 px across; seams roughly 2–4 px; cells shrink strongly upward | Perspective repetition is the dominant texture. |
| knight f930 armor | Outer/card contours often roughly 4–7 px; internal plate bands roughly 2–4 px; individual rivets roughly 7–11 px diameter | Large costume hardware and drawing scale; do not apply these widths to distant world edges. |
| railroads f1290 lower ballast | Individual stones roughly 8–35 px across; many touch/overlap with shadowed interstices | Near-camera meso geometry, not photographic pebble noise pasted on a flat plane. |
| sample-1 f720 car | Body seams often approximately 1–2 px; bright hood/window patches occupy tens of pixels | Broad reflection shapes carry gloss more strongly than tiny glints. |

World edge visibility varies with contrast, blur and material: many interior panel edges are a dark tinted seam rather than absolute black. Character contours remain conspicuously stronger. Do not infer a single fixed 3 px native world outline from these observations.

## Material recipes — implementation recommendations, not recovered settings

**Wood.** Model essential boards/panels and bevel large silhouette edges. Canvas2D base texture: 3–6 broad warm value variants, seams aligned to construction, a few elongated blotches and isolated knots. Prefer 2–4 tonal bands across a board to dozens of hairline fibers. Keep seam width stable in UV/world space unless using a deliberate screen-space ink pass. Let AO/contact darkening sit at joins without painting a uniform black border around every board. mirror is warmer and more visibly mottled than the clean knight stall. A suggested starting roughness is 0.7–0.95, reduced only for varnished focal props; this number is not measured.

**Metal.** Split bright cap/edge from dark side plane; add few rivets and plate overlaps. For knight armor, use a smooth blue-gray ramp plus painted broad white highlights; keep rivets graphical. For railroads, use bright rail top, dark oxidized web and modeled bolts. For sample-1 vehicles, use a broad environment/reflection source and restrained clearcoat. Suggested starting roughness ranges: armor 0.35–0.65, rail cap 0.2–0.45, car paint 0.15–0.35; tune by visible highlight size, never by believing those ranges were inferred from encoded frames.

**Cloth and felt.** Uniforms are 2D color blocks with limited broad shading and costume marks. Awning folds/segments are constructed with large alternating panels and scallops, not woven bump. Felt counter can use low-amplitude cloudy variation and high roughness (suggested 0.85–1). Cloth texture should disappear before facial marks do at delivery size. Do not add realistic wrinkles across a bean torso.

**Stone, earth and vegetation.** Two valid levels coexist: simplified green ground in shape and high meso-detail rock ballast in railroads. For close ballast, instance irregular low-poly stones with 5–8 restrained color variants, random rotations, local contact shade and reduced distant density. Cliff bands should be broad strata with plane-to-plane light changes, not leopard-like noise. Trees can use clustered foliage masses with a few internal variations; a universal outline around every leaf creates visual static. Match local shot scale rather than choosing one density for the entire film.

**Glass.** Build mullions first. Use mildly tinted panes with broad reflection strips, partial interior readability and modest transmission/opacity; amber spot storefront and violet-gray car windshield demand different tints. Transparent ordering and card occlusion must be checked explicitly. Avoid strong realistic refraction that distorts a flat face beyond recognition. Glass should not receive the same opaque filled toon ramp as a wall.

**Water.** Use scene-specific modes. railroads gorge: deep cobalt, broad smooth value gradient, very restrained reflection/ripple. sample-1 pool: cyan surface, recognizable simplified reflected dark figures, bright lamp streaks, pale pool rim. Three.js planar reflection/render target with blurred/refined reflection or predesigned animated reflection cards can both work; neither technique is established by these images. Broad, low-amplitude moving normals are safer than choppy high-frequency normal noise.

**Sky and clouds.** Day skies are large blue fields with horizon lift and broad cloud shapes; cloud construction ranges from simplified pale slabs (shape/sample-1) to softer cloud fields (railroads). Night shape has deep blue field, moon, tiny star points and selective pale cloud-edge illumination. Sky does not need film grain or procedural pixel noise. Keep clouds at a scale that supports the set, with fewer competing edges around the head. Fog should compress remote contrast/material detail rather than tinting all near objects identically.

## Line placement and shadow boundaries

Place ink/seams at silhouette changes, plate/panel boundaries, window frames, plank joins, roof edges, structural rail edges and key costume marks. Use geometry edges or depth/normal outlines for world structure; paint decorative grain, knots, tile joins and cliff strata. A global edge detector cannot distinguish intended seams from every tiny ballast facet, so exclude or attenuate dense detail from post ink. Do not double-outline the character card: its own contour already supplies the strongest local border.

There is no single hard/soft shadow rule. Knight armor contains smooth gradients bounded by hard plate outlines; cashiers counter/walls carry broad soft variations; railroads rock facets and rail surfaces have harder plane changes; sample-1 cars mix crisp panel transitions with broad smooth highlights. Pool lamp reflections have a softened glow. Contact shadows must be tight enough to ground feet, crates, rails and counters; large cast shadows may have readable hard direction without making every surface binary cel shading. Compare actual object boundaries independently from painted dark seams and specular patches.

## Environment construction priorities

1. Block the set with real depth and repeated units: floorboards/tiles, counter fronts, rails/ties, window mullions, road lanes, siding and support frames. Perspective and overlap are more valuable than noise maps.
2. Put material differences on adjacent objects: matte face/card versus shiny helmet, felt versus paneled wood, bright rail cap versus dark web, car paint versus asphalt, pool water versus pale coping.
3. Match detail to projected scale. Keep foreground ballast geometric, allow distant stones to collapse to a low-frequency texture, and remove high-frequency patterns behind a face when they become competitive.
4. Shade the world directionally while preserving the character card as a flat illustration. Scene tint and broad highlights can affect costumes; avoid making faces modeled spheres.
5. Inspect the exact moving camera path for rail/counter/window occlusions and repeat-pattern aliasing. Texture seams should remain attached to surfaces; screen-space noise swimming over the image is wrong.
6. Render native-size previews and final-resolution previews. Features that are one source pixel wide are uncertain evidence; do not invent hundreds of fine scratches when upscaling.

## Anti-patterns and acceptance

Reject: one perfectly smooth orange ground; photo woodgrain covering every surface; uniform black edge around every stone/leaf; fabric weave on characters; full-scene mirror gloss; opaque glass with unreadable interiors; invisible glass without framing/reflection; turbulent water for every scene; tiny repeating texture tiles; painterly noise laid over pale faces; equal detail at all depths; copying the exact reference set or assets.

Accept when a 360×640 downsample still distinguishes wood, metal, cloth, glass and water through large structural/material cues; the face remains the strongest simple graphic read; floor/counter/track perspective establishes depth; close surfaces carry appropriate meso detail; distant fields simplify; specular highlights are localized to appropriate materials; and a moving inspection reveals no texture swimming or distracting repeated pattern.
