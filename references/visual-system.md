# Visual-system gate

Choose the image source before choosing an illustration style. A visually coherent issue can include different media, but every visual must belong to one declared system.

## 1. Source strategy

Use the article's claim type and emotional job to choose:

| Strategy | Use when | Primary material |
|---|---|---|
| Evidence-led | The article makes product, event, place, or result claims | Real screenshots, user-owned photos, verified source captures |
| Photography-led | Place, person, object, atmosphere, or lived experience carries the story | Licensed or user-owned real photography |
| Illustration-led | The article is conceptual, personal, metaphorical, or future-facing | Generated or original editorial illustration |
| Diagram-led | The reader must understand a mechanism, comparison, sequence, or data relationship | Deterministic SVG, chart, or annotated schematic |
| Hybrid | Both proof and interpretation matter | Real evidence plus one coherent illustration or diagram system |

Never generate a screenshot, documentary photograph, quotation, logo, interface state, or factual evidence. Do not use a generic stock photo merely to fill space. Record the source, license, factual role, and crop for every real image.

## 2. Propose three visual systems

When illustration or stylized imagery is appropriate, propose exactly three genuinely different systems after direction and palette selection. Do not present arbitrary style labels. For each proposal include:

- article-specific concept and why the medium fits;
- medium: e.g. 3D object theatre, flat geometric vector, loose hand drawing, risograph/print, paper collage, clay miniature, pixel art, cinematic photography;
- composition grammar: subject scale, camera angle, whitespace, depth, and recurring framing device;
- surface grammar: stroke, texture, shadow, lighting, grain, and edge treatment;
- character policy: none, recurring object, recurring mascot, or real person; never introduce a mascot by habit;
- palette mapping from the selected palette roles;
- cover treatment and simplified inline-image treatment;
- one tradeoff and explicit exclusions.

The three systems must differ in medium, spatial depth, and emotional register. If changing only color or texture converts one into another, replace it.

## 3. Style anchor

Before producing the whole image set, make one text-free style anchor or visual keyframe for the chosen system. It should contain the representative subject, composition, material, palette, and lighting/line behavior without attempting to illustrate every article point.

Inspect it at mobile size. Record an `image_bible` in `design-recipe.json` with:

```json
{
  "visual_system": "article-specific-id",
  "source_strategy": "hybrid",
  "style_anchor": "assets/style-anchor.png",
  "medium": "hand-drawn editorial ink",
  "composition": "single metaphor, generous white space, off-center subject",
  "surface": "slightly irregular black line, no gradients, sparse accent fills",
  "palette_mapping": {},
  "character_policy": "no mascot",
  "cover_rule": "denser hero scene with center-square-safe focal point",
  "inline_rule": "one idea per image, quieter composition, identical line and accent behavior",
  "negative_rules": []
}
```

Use the anchor as a visual reference for subsequent generated images when the available generator supports references. If it does not, repeat the image bible verbatim in every prompt and compare the outputs side by side. A fixed seed alone is not a reliable style system.

## 4. Cover/body family rule

The cover is the most concentrated expression of the system; inline images are quieter members of the same family. They share medium, palette, material, line/lighting behavior, recurring object or character, and crop logic. They do not need identical compositions.

- Cover: one strong focal action, room for deterministic Chinese title, center-square-safe.
- Inline illustration: one cognitive anchor per image, limited or no embedded text, readable at 335px.
- Diagram: may be more restrained, but must reuse palette semantics, stroke family, corner logic, and captions.
- Real screenshot/photo: keep factual pixels intact; unify with consistent crop, border, annotation, caption, and tonal framing rather than restyling evidence into fiction.

Reject a set when the cover looks 3D but the body becomes generic flat vector, when characters drift, when every image has a different lighting model, or when illustrations merely decorate headings.

## 5. Open-source references and boundaries

Useful methodological references include `axtonliu/smart-illustrator` for illustration-position and engine routing, `caezium/nib` for article shot lists and reference-character consistency, and `tmchow/illo-skill` for named material systems and recurring visual rules. Study their workflows; do not copy their mascots, bundled artwork, prompts, or distinctive compositions into this skill.

Open illustration libraries such as unDraw, Open Doodles, Open Peeps, and Humaaans may be candidates only after checking the exact asset license and whether their established style genuinely fits the issue. Do not mix multiple libraries in one article. Preserve required attribution and record it in the image plan.

Heavy local pipelines such as ComfyUI/IP-Adapter can improve reference consistency, but they are optional. Do not install models, nodes, or large dependencies without a concrete need and user authorization.
