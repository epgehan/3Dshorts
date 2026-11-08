# Color, contrast and postprocessing

## Measurements across every decoded frame

The analyzer calculates Rec.709-weighted **display-referred gamma-encoded luma proxy**, `Y'=.2126R'+.7152G'+.0722B'`, from decoded RGB before the inspection JPEG is written. These are mixed-image statistics, not scene-linear illumination, intrinsic albedo or a direct aesthetic score. Every frame includes subjects, sets and whatever burned-in text is present. Medians below are medians over all frames of each frame's statistic. Full per-frame values and quantiles are in `analysis/metrics/`.

| Video | Frames | Median frame meanY' | Median frame medianY' | Median HSV saturation |
|---|---:|---:|---:|---:|
| mirror |1922|.470|.424|.406|
| knight |1219|.533|.525|.466|
| spot |1898|.442|.417|.472|
| cashiers |1732|.495|.503|.413|
| shape |1895|.437|.444|.485|
| railroads |1955|.457|.448|.469|
| sample-1 |1867|.400|.372|.424|

The range is evidence against one required median brightness or globally identical saturation. Knight's many bright exteriors differ from sample-1's night/cabin/overcast sequence. A whole-program median cannot tell whether a particular face is correctly exposed. The automatic `ink_fraction_proxy` means only pixels whoseY'<.12; it also counts dark car interiors, night sky, lettering and shadow, so never interpret it as actual ink coverage.

## Color relationships

The lighting report samples21 named5×5patches on native-size inspection JPEGs. Those patch values have an extra inspection encoding and should be treated as approximate rendered colors. They are not source shader colors. Cashiers f00660(22s) has a very pale pink/lavender face against a saturated blue room; sample-1 f01260(42s) has a pale lavender face against a near-black/cobalt sky; railroads f01650(55s) keeps the face near cream while the canyon is strong orange. This supports protecting face readability as the world changes.

The exceptions matter: spot f00120 has a motivated yellow-green face under a glowing object, and railroads f00570 has an expressive purple face. Those are locally motivated treatments. Do not achieve all night shots by tinting every layer blue. Do not tint every face amber because a practical light is warm.

Warm/cool separation is frequent but not mandatory. Knight f01200's sunset path and cast shadow both contain warm brown components, as documented in the lighting patch report. Cashiers has a bright mint/green store and turquoise prize office. Sample-1 includes magenta dusk, cobalt porch/pool and muted blue-gray wet highway. A single amber-versus-violet LUT cannot match all these settings.

## Bloom, contrast and atmospheric effects

Localized lamps, moonlight, luminous rails, headlights, sunset and glowing props can bloom. A global blur or glow over the whole image would soften eyes, lips, ink and captions that remain readable in the source. Bright bulbs on Shape's night ride have a different role from the broad daytime sky. Specular car reflections and wet road highlights are allowed even though character faces remain drawn.

Some foregrounds and distance layers soften; distinguish depth of field, atmospheric perspective, motion blur, glow and low source resolution. Each effect has a different cause and place in the compositing order. Do not add film grain to imitate H.264 blocks or the study export's JPEG texture. No new-sample grain amplitude or exact tone-map function has been recovered.

## Recommended post chain and controls

This is a practical implementation proposal: scene shading → selective world ink with character exclusion → depth-aware scene blur where desired → restrained source-attached glow → restrained tone/grade → captions. The inherited bridge uses a similar pipeline, but its shader coefficients and neutral tone map are an example, not evidence of the original authoring pipeline.

Provide shot-level world exposure, face-lighting protection, ambient hue, key hue, fog/haze strength, localized glow strength, and optional grade amount. Tune these against representative frames rather than forcing aggregate histograms to match. Keep caption fill solidwhite and draw it after post so scene grading cannot make subtitles yellow, blue or translucent.

## Acceptance

Pass when pale faces and dark contours remain distinguishable, scene-specific color relationships hold, night retains readable geometry, highlights stay localized, and selective blur preserves the acting plane. Reject clipped facial features, crushed black sets, orange washes, violet-face defaults, uniform saturation, large bright bloom halos and attempts to infer original physical lights from compressed pixel values.
