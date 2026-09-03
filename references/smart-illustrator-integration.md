# Optional Smart Illustrator integration

`smart-illustrator` is an optional companion maintained at <https://github.com/axtonliu/smart-illustrator>. Keep it installed as a separate Skill. Do not copy its source, styles, or scripts into this repository.

## Use it for

- a second-pass audit of where an article genuinely benefits from illustration;
- classifying a planned visual as scene, metaphor, comparison, concept, process, architecture, sequence, or data;
- Excalidraw routing for hand-drawn comparisons, concept relationships, and simple flows;
- Mermaid-to-PNG routing only for complex flows, architectures, sequences, or decision trees;
- resumable multi-image production when its configured backend is available;
- prompt-only planning when no Gemini credential is configured.

## Do not use it for

- choosing the article's editorial direction or palette;
- mechanically assigning images to every heading;
- replacing real product screenshots or factual evidence;
- generating the final WeChat cover by default;
- embedding Mermaid code in WeChat HTML;
- overriding this skill's dual-crop cover, mobile QA, or copy packaging.

## Cover rule

For WeChat covers, keep this skill's workflow as the authority:

1. derive the concept from the selected direction and palette;
2. use the available raster image generator for the text-free background;
3. apply Chinese typography deterministically;
4. export 900×383 wide, 383×383 center crop, and safe-area proof.

Smart Illustrator cover mode may be used only to produce an additional concept candidate when the user asks for alternatives. Its result must still pass the dual-crop workflow.

## Engine mapping

| Visual need | Preferred route |
|---|---|
| Cartoon, photo, textured editorial scene, metaphor | built-in raster image generation |
| Simple deterministic comparison or process | inline SVG |
| Hand-drawn concept map or informal relationship | Smart Illustrator Excalidraw, if dependencies exist |
| Complex flow with more than about 8 nodes | Smart Illustrator Mermaid-to-PNG |
| Product behavior or evidence | real inspected screenshot |
| No clear visual job | whitespace |

## Availability and fallback

Before use, check that the separate Skill exists. Do not install Bun, browsers, global Mermaid CLI, or API credentials merely because Smart Illustrator is present. If a required engine dependency is missing, fall back to prompt-only, inline SVG, or built-in image generation as appropriate.

Do not ask the user to paste API keys into chat. Gemini generation remains optional. A complete WeChat article must remain possible without Smart Illustrator.

## Attribution and originality

Smart Illustrator is an external MIT-licensed dependency. Keep its name and repository link when describing the integration. The WeChat Editorial Director's workflow, art-direction system, palette gate, dual-crop cover logic, and packaging remain independently implemented.
