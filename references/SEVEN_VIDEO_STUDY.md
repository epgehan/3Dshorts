# Seven-video study — native30 fps

The seven uploads were studied alongside the saved user character/background guide and the previous `cartoon-3d-short` implementation. Every native frame was computationally decoded/measured/exported; semantic visual review is targeted and documented in the topic reports. Source footage, full-frame collections and contact sheets remain local/private.

## Complete source inventory

| ID | User file | Native video duration | Frames | Cadence | Size |
|---|---|---:|---:|---|---|
| mirror | How-a-Mirror-SnapYT.App.mp4 | 64.0667s | 1,922 |30 fps|360 × 640|
| knight | This-Knight-Found-SnapYT.App.mp4 | 40.6333s | 1,219 |30 fps|360 × 640|
| spot | He-Could-Spot-SnapYT.App.mp4 | 63.2667s | 1,898 |30 fps|360 × 640|
| cashiers | Why-Cashiers-Keep-SnapYT.App.mp4 | 57.7333s | 1,732 |30 fps|360 × 640|
| shape | This-Shape.mp4 | 63.1667s | 1,895 |30 fps|360 × 640|
| railroads | Why-Perfect-Railroads-SnapYT.App.mp4 | 65.1667s | 1,955 |30 fps|360 × 640|
| sample-1 | 1.mp4 | 62.2333s | 1,867 |30 fps|360 × 640|

Total: **12,488 native frames**, **212 consecutive-frame contact sheets** (up to60 frames each). Container/audio tails are listed separately in the inventory. All full-frame collection counts, dimensions, indices and timestamps passed [coverage verification](../analysis/verification.json).

## Per-video production observations

### Mirror
A bright racetrack/bookmaker setting alternates wide streets/interiors, a small figure at a mirror, circular viewing inserts, track action, counter exchanges and crowd reaction. Pale broad heads, thin limbs, role hats/bow ties, small expressive faces and dimensionally staged rooms recur. Mirror f299–302 provides adjacent eyelid/arm changes. Frames540–599 demonstrate circular inserts;1442–1499 demonstrate blending plus movement through foreground room geometry. Preserve identity through changes of scale, with viewpoint inserts as a specific narrative tool.

### Knight
Market stall, wagon, indulgence-like chest transaction, forest travel and sunset aftermath use a more colorful storybook environment, with drawn armor plates as a material exception to simple clothing. Early stalls, layered foreground trees and the load-bearing pole support depth. Forest f802–807 has an occluder-assisted change; f890–896 blends a wide into a closer scene. The sunset has long graphic shadows with warm components. Armor contour complexity does not justify changing the basic flat face into a3Dsphere.

### Spot
Shop counters, ticket/number-grid inserts, institutional interiors and nighttime number analysis move between warm pools, bright ceiling/tiles and cobalt settings. A glowing prop colors the face in an explicitly motivated early scene. Later faces are protected near-white against darker worlds. Atf1505–1512 old/new scenes overlap in a short dissolve, followed by a reveal. Whole grids, phone/map inserts and crowd/counter views need separate composition/focus rather than one continuous camera recipe.

### Cashiers
A green shop, face/tabletop inserts, an imagined fishing/boat scene, cobalt interior, prize counter, waiting area and explanatory poster produce very different scales. Simple graphic cashier/police/office costumes remain consistent with dimensional furniture and rooms. Over-shoulder/back artwork changes are important. A smile/raised arm can hold for about37-frames while camera motion continues. The explanatory wall/board move uses strong scale/reframing; do not reinterpret every scene change as character motion.

### Shape
The tool strike, extreme scale reveal of coaster geometry, nighttime ride outline, opening-day scene, broad road/car physics view and return to the ride demonstrate unusually varied camera angles and world detail. Dark night uses white ride bulbs and a clear moon, not a general amber wash. Wide geometry stays understandable while close reactions use selective focus. Atf630 a clear scene/actor cut differs from slower blended transitions elsewhere. Cars and coaster elements may have more volume/gloss than the characters.

### Railroads
Tilted worker views, narrow rails/ballast, canyon/water, company figures, carriage interior, gap explanations and expanding track views rely on repeated perspective geometry. Dense ballast/canyon texture is a legitimate exception to sparse backgrounds. An expressive purple face is not evidence for a global purple-face light preset. Camera travel aroundf1692–1707 crops the actor away; it is not a leap/fall. Track gaps and thermal/geometry explanations need clean focus and causal framing.

### Sample1
Driver cabin, multi-car street, domestic/pool/porch, night driveway and overcast wet road use more reflective vehicles, glass, water and atmospheric backgrounds. Original character grammar remains simple inside much denser world assets. Windshield/seat/body overlaps require correct depth order. Atf1161 a hard cut differs from blended cabin changes aroundf1495–1505. Lighting shifts cyan day→pink dusk→deep-blue night→gray wet road; one sunny or violet preset is insufficient.

## What changes from the old skill

| Legacy assumption | Revised instruction | Evidence |
|---|---|---|
| Always55–70seconds | Let the approved story/brief determine duration | knight40.6333s; others~58–65s |
| No captions | ALL CAPS Arial, white only, black outline | current explicit user choice |
| Fixed3.5head heights | Use measured same-character relations; selected views span roughly2.7–3.5HH | character report |
| Always-front billboard | Supply appropriate front/three-quarter/back artwork and layer splits | cashiers over-shoulder; sample-1 cabin views |
| Violet shadows always | Use per-scene light recipes, including warm shadows | knight sunset patches |
| World always sparse/matte | Vary detail/gloss by material and setting | railroads rock/ballast; sample-1 cars/water |
| Every pose must move after4frames | Held acting poses can remain while camera/props move | cashiers1043–1079 |
| Fixed4frame blink and interval | Use explicit expression events;2-frame closed states observed | spot/cashiers/railroads opening samples |
| Fixed glides/roll/push | Shot-specific camera grammar, no recovered global ease | camera report intervals |
| Big changes always hardcut | Cuts, short dissolves, optical inserts and occluder travel coexist | motion/camera reports |
| Focus nearest/front eyes | Focus the narrative plane; near shoulder/figures may be soft | depth report |
| Fixedmusic+3/SFX−6dB | Measure the mixed program; choose original mix for intelligibility | audio metrics do not recover stems |

## Full instructions and evidence

- [Active skill](../SKILL.md)
- [Production instruction guide](PRODUCTION_GUIDE.md)
- [Characters](reports/characters.md), [lighting](reports/lighting.md), [camera](reports/camera.md), [motion](reports/motion.md), [depth](reports/depth.md), [textures](reports/textures.md), [outlines](reports/outlines.md), [grade](reports/grade.md)
- [Caption/audio rules](CAPTIONS_AND_AUDIO.md)
- [Measurement methods and limits](MEASUREMENT_METHODS.md)
- [Complete source inventory](../analysis/metrics/inventory.json), [all-frame verification](../analysis/verification.json)

## What remains to prove in production

This delivery is a researched skill and tooling package. No new matching short has been rendered from the revised recommendations. The inherited renderer is a starting code example, not a runtime-verified recreation. A new original episode still needs character/look probes, narration timing, contact/motion review, final render and independent visual acceptance. No exported360 × 640reference can identify every original vector detail,3Drig, lens or shader.
