# WeChat dual-crop cover system

A complete article normally needs one cover composition with two deliverables:

- **Wide cover:** default 900×383, approximately 2.35:1.
- **Square crop:** default 383×383, taken from the exact horizontal center of the wide cover.

Confirm platform requirements if the destination uses different dimensions.

## Composition zones

For a 900×383 cover, the center square spans approximately x=258–641. Everything required for recognition must remain inside that zone:

- title and essential subtitle;
- primary face or character;
- product/device or central object;
- interaction cue, logo, or symbolic action.

The left and right wings may hold lighting, texture, shelves, scenery, or other expendable atmosphere. Never place a second essential character, key text, data, or logo in the wings.

## Mandatory two-pass workflow

1. Derive the cover concept from the selected editorial direction, palette, reader promise, and image grammar.
2. Produce **concept draft v1**. Its job is to establish what the scene contains, the focal group, broad lighting, and crop-safe geometry. It is not a deliverable.
   Before refinement, apply a concept-specificity gate: could this image advertise many unrelated products after changing only the title? If yes, it is generic category imagery and must be reconceived rather than polished. The cover needs one visual metaphor, action, object relationship, or evidence cue that belongs to this article.
3. Inspect v1 and write `cover-review.json` using [cover-refinement.md](cover-refinement.md). Name the strengths to preserve and the defects to fix.
4. Use v1 as the edit/reference target for **refinement redraw v2**. The prompt must explicitly preserve the successful scene and focal composition while fixing hierarchy, title integration, lighting, depth, clutter, anatomy, and finish.
5. Inspect v2. Allow at most one additional targeted refinement by default; do not enter an open-ended regeneration loop.
6. Resolve title typography using the strategy below.
7. Export wide, square, and safe-area proof variants.
8. Inspect the square crop independently at thumbnail size. If recognition or title meaning is lost, refine the composition rather than merely shrinking elements.

## Title rules

- Prefer one short promise of 6–14 Chinese characters.
- Keep all essential title text inside the center square with 24–32px internal padding.
- Use high contrast and a restrained shadow or overlay when the background is busy.
- The cover title may be shorter than the article title but must not change its meaning.
- Small decorative labels may disappear in the square crop; the main title may not.

## Title integration strategy

Prefer this order:

1. **Composition-integrated typography:** the refined artwork intentionally reserves and shapes negative space for the title. Generated text may be accepted only when every character is exact.
2. **Deterministic compositing:** remove or avoid generated text, then typeset the exact title into the reserved space. Match perspective, lighting, rules, and visual rhythm of the artwork.
3. **Overlay shelf:** use a translucent or solid title container only when the chosen art direction calls for an interface or editorial panel.

Do not automatically place every title inside the same rounded dark rectangle. Technical correctness does not excuse a pasted-on appearance.

## Relationship to article visuals

The cover shares character design, illustration medium, stroke/texture, and palette logic with the article. It need not repeat the exact body image. A cover attracts and establishes tone; a body illustration explains.

## Required checks

- exact dimensions and aspect ratios;
- center-square coordinates;
- title and focal-point bounding boxes remain inside the safe zone;
- no generated gibberish, unintended logos, or watermarks;
- wide and square both work as independent thumbnails;
- compressed file size fits the intended publishing route.
- the final is a refinement of a diagnosed draft, not the first generated image;
- title treatment belongs to the composition instead of floating above it;
- any model-generated text is character-for-character correct;
- no unintended brand mark, book text, poster copy, or UI label remains.
- the core cover concept is specific to the article rather than a generic laptop, desk, portrait, gradient, or stock-product scene;
