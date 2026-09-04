# Scenic Portal editorial direction

This direction was informed by reviewing immersive product pages such as MeetPoint, but the implementation and framing metaphor must be original to each article. Do not copy another site's train window, scene names, copy, or assets.

## Core idea

Use one meaningful visual frame to make the reader feel they are looking into the article's world. The frame is narrative, not ornamental.

Possible framing devices:

- a video screen for a media or learning product;
- a telescope for discovery;
- a doorway for transition;
- a map fold for travel or planning;
- a book spread for knowledge or memory;
- a camera viewfinder for observation;
- a dashboard pane for an operational story.

Choose the device from the article. Never default to a train window simply because the reference looked good.

## Composition grammar

An immersive plate contains:

1. one full-width atmospheric scene;
2. one dominant frame or portal;
3. one narrow central text zone;
4. at most one eyebrow or chip;
5. one short title;
6. one short deck or action line;
7. generous quiet space around the focal text.

The text zone should normally remain within roughly 60–70% of the mobile article width. Avoid feature grids, multiple badges, or a collection of equal-weight cards inside the plate.

## Atmosphere as a system

For this direction, a visual variant changes more than color. Define:

- time of day;
- weather or environmental state;
- light direction and softness;
- depth and haze;
- emotional temperature;
- accent behavior;
- typography contrast.

Examples of semantic moods include anticipation, reflection, exploration, and renewal. Name them for the article rather than reusing another product's labels.

## Typography pairing

- Use a display face with personality for the short title when the article is emotional or narrative.
- Use a neutral sans-serif for decks, labels, captions, and actions.
- Strong shadow, blur, or glass effects are permitted only inside the precomposed raster plate. Do not depend on fragile CSS effects in exported WeChat HTML.

## WeChat implementation

The web pattern may rely on full-screen video, absolute positioning, backdrop blur, and layered overlays. Do not reproduce those techniques in WeChat HTML.

Instead:

1. generate or source the scene;
2. compose the frame, title, deck, and any glass treatment deterministically into one raster image;
3. export a mobile-safe full-width plate;
4. insert it as a normal `<img>` with an accurate alt description;
5. keep essential body copy outside the image for accessibility and editing.

Static image output is the compatibility layer. Video backgrounds and interactive scenery switching are out of scope for ordinary WeChat articles.

## Where to use it

Good fits:

- personal narratives;
- travel and relationship stories;
- reflective essays;
- product stories with a strong experiential metaphor;
- chapter openings where emotion or orientation matters.

Poor fits:

- installation steps;
- evidence-heavy research;
- long comparison lists;
- technical documentation that needs selectable text;
- every section of a single article.

## Restraint rules

- Use once at the opening, optionally once more at the major emotional turn.
- Do not alternate scenic plates with every paragraph.
- The scene cannot substitute for evidence.
- The portal frame must not reduce mobile text legibility.
- If removing the frame changes nothing about the story, the frame is decorative and should be removed.

## Review checklist

- Does the frame express the article's subject or emotional action?
- Does one clear focal path exist: chip → title → deck/action?
- Is the central text readable at phone width?
- Are the environmental wings expendable when cropped?
- Is the result substantially different from an ordinary Hero card?
- Has the web inspiration been transformed rather than copied?
