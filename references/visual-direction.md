# Visual direction

Plan visuals after direction selection and before generation.

For each visual record: location, narrative purpose, type, source, exact content, caption, aspect ratio, mobile crop, style relationship, and factual/copyright risk.

Before accepting a user asset, repository image, or downloaded image, open it and inspect the actual pixels. Reject debug consoles, accidental crops, stale screenshots, unreadable text, deceptive mockups, or images whose visual quality does not support the article.

Decision order:

1. Product claim → real screenshot or no claim visual.
2. Relationship/mechanism → diagram.
3. Verified values/comparison → chart.
4. Atmosphere/emotion → photography or editorial illustration.
5. No clear job → whitespace.

Use raster image generation for a requested cartoon, photo, textured editorial illustration, or other standalone bitmap. Use SVG for deterministic diagrams, process maps, comparison plates, and interface schematics. Do not quietly substitute one medium for the other.

The cover establishes tone; it must not masquerade as evidence. An explanation image reduces cognitive load and uses the aspect ratio the information needs. A screenshot proves behavior and must never be generated.

Use one image grammar per issue: shared crop logic, stroke weight, annotations, caption voice, and tonal treatment. Do not target a fixed count; one cover plus zero to four body visuals is only a common range.

For generated art, specify subject, role, composition, palette relationship, texture, ratio, safe area, and exclusions. Add Chinese typography deterministically rather than relying on image generation.

After generation, inspect the image at article scale, move the selected final into the article asset directory, compress it for the intended route, and update the consuming HTML. A generated image is not delivered merely because it appeared in chat.

For an image-led article or chapter opener, consider the Scenic Portal method in [scenic-immersion.md](scenic-immersion.md). It uses atmosphere and a story-specific framing device to replace generic Hero cards, but must be precomposed into a static image for WeChat reliability.
