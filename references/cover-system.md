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

## Workflow

1. Derive the cover concept from the selected editorial direction, palette, reader promise, and image grammar.
2. Produce a text-free visual background. In the image-generation prompt, state the exact center-square safe zone and make the side regions expendable.
3. Inspect the background before adding text.
4. Add Chinese typography deterministically with `scripts/build_cover_variants.py`; do not rely on image generation for exact Chinese titles.
5. Export wide, square, and safe-area proof variants.
6. Inspect the square crop independently at thumbnail size. If recognition or title meaning is lost, redesign rather than merely shrink.

## Title rules

- Prefer one short promise of 6–14 Chinese characters.
- Keep all essential title text inside the center square with 24–32px internal padding.
- Use high contrast and a restrained shadow or overlay when the background is busy.
- The cover title may be shorter than the article title but must not change its meaning.
- Small decorative labels may disappear in the square crop; the main title may not.

## Relationship to article visuals

The cover shares character design, illustration medium, stroke/texture, and palette logic with the article. It need not repeat the exact body image. A cover attracts and establishes tone; a body illustration explains.

## Required checks

- exact dimensions and aspect ratios;
- center-square coordinates;
- title and focal-point bounding boxes remain inside the safe zone;
- no generated gibberish, unintended logos, or watermarks;
- wide and square both work as independent thumbnails;
- compressed file size fits the intended publishing route.
