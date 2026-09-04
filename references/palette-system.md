# Palette selection system

Palette selection happens only after the editorial direction is chosen. It changes color roles, not the article's composition, information order, image plan, or component grammar.

## Required roles

Every palette proposal defines:

```json
{
  "canvas": "#FFFFFF",
  "surface": "#F8FAFC",
  "ink": "#111827",
  "body": "#374151",
  "muted": "#94A3B8",
  "border": "#E2E8F0",
  "accent": "#2563EB",
  "accent_soft": "#EFF6FF",
  "highlight": "#FDE68A",
  "dark_stage": "#0B1220",
  "dark_text": "#F8FAFC"
}
```

## Proposal rules

- Recommend exactly three palettes for the chosen direction.
- Give each an editorial name and one-sentence rationale. Avoid labels that are only hue names.
- The three proposals must differ in temperature, contrast strategy, or emotional effect—not merely swap accent hex values.
- Color must have stable semantics. Example: accent means interaction or editorial anchor; highlight means reader attention; dark-stage means video or evidence environment.
- Body text is carried by neutral ink, not brand color.
- Large backgrounds stay restrained unless the selected direction explicitly calls for immersion.

## Common direction mappings

- Product demonstration: digital contrast, clear interaction accent, restrained surfaces.
- Maker's field notes: paper-like canvas, low-saturation annotations, gentle highlight.
- Visual explainer: categorical accents with disciplined legend semantics.
- Editorial column: near-monochrome ink plus one editorial signal color.
- Evidence dossier: high-contrast neutrals with accessible chart series.
- Cultural magazine: atmospheric palette derived from the cover image.
- Scenic portal: propose atmosphere systems, not merely hex swaps. Light, weather, depth, and scene temperature should change together while preserving the editorial frame.

## Contrast gate

Check ordinary body text against its background for readable contrast. Do not use pale accent colors for paragraph text. Test highlight text, dark-stage text, muted captions, borders, and callouts. Flag combinations likely to become dirty or low-contrast in WeChat dark mode.

## Palette picker input

`build_palette_picker.py` expects a JSON object with `article_title`, `direction`, and exactly three proposals. Each proposal needs `id`, `name`, `rationale`, `roles`, and `tradeoff`.
