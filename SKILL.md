---
name: wechat-design-studio
description: Direct WeChat Official Account articles from content diagnosis through art-direction selection, adaptive layout, image planning, WeChat-safe HTML, preview, and QA. Use for 公众号排版, 文章配图, or multiple genuinely different visual proposals; do not publish unless explicitly requested.
---

# 微信公众号设计工作室

Treat every article as an editorial-design commission. Never pour different articles into one template and call palette changes new styles.

## Original thesis

**Diagnose first, choose an editorial direction, choose its color system, then design.** Layout, typography, imagery, information graphics, and pacing must come from the same reading of the article. An **art direction** controls composition and visual grammar; a **palette** controls color roles inside that direction. Never confuse the two.

## Workflow

### 1. Diagnose without rewriting

Read [references/editorial-diagnosis.md](references/editorial-diagnosis.md). Identify the primary/secondary archetype, reader promise, author voice, emotional curve, information density, evidence, and visual moments. Preserve the author's facts, phrasing, and paragraph order unless rewriting is requested.

### 2. Propose exactly three directions

Read [references/art-directions.md](references/art-directions.md). Each proposal must specify its concept, opening composition, information order, component grammar, image language, typography category, palette roles, and one tradeoff. The three must differ on at least four of those axes.

Present the proposals before full layout. **Do not design the final article or generate images until the user chooses**, unless the user explicitly delegates the choice. If helpful, create a picker using `scripts/build_direction_picker.py`.

### 3. Propose three compatible color systems

After the direction is chosen, read [references/palette-system.md](references/palette-system.md). Recommend exactly three palettes that all support the chosen direction. Name palettes by mood or function, not only hue. Show a compact live specimen for the Hero, heading, body, callout, and highlight with `scripts/build_palette_picker.py`.

Each palette must assign explicit roles: canvas, surface, ink, body, muted, border, accent, accent-soft, highlight, and dark-stage. Check contrast and dark-mode sensitivity. **Do not begin final layout until the user chooses a palette**, unless they delegate the choice.

### 4. Create a design recipe

After both selections, write `design-recipe.json`: chosen direction, chosen palette with roles, content sequence, components, image plan, type scale, spacing rhythm, and density rules. Never reuse a previous article's recipe unchanged.

Read [references/semantic-components.md](references/semantic-components.md) for the content layer. Components are vocabulary, not a checklist.

### 5. Plan visuals as part of the argument

Read [references/visual-direction.md](references/visual-direction.md). Create `image-plan.md` before sourcing or generation. Every visual must do one job: **prove, explain, orient, evoke, or pace**.

If `smart-illustrator` is installed, read [references/smart-illustrator-integration.md](references/smart-illustrator-integration.md) and use it only as an optional illustration auditor and diagram router. It does not replace the selected editorial direction, palette, cover system, or this skill's quality gates.

Prefer real user-owned screenshots for product claims; static SVG for relationships; charts only with verified data; photography or generated illustration for atmosphere. **Visually inspect every candidate image before using it**; filenames and repository context are not enough. If the user asks for a cartoon, photo, or standalone illustration, use an image-generation workflow rather than substituting an SVG mockup. Never fabricate evidence, logos, quotations, or data. Whitespace is a valid visual decision.

### 6. Design the cover as a dual-crop system

For a complete WeChat article request, read [references/cover-system.md](references/cover-system.md) and [references/cover-refinement.md](references/cover-refinement.md), then deliver a cover unless the user opts out. The wide cover and the square share thumbnail are one composition, not independent afterthoughts.

Use a mandatory two-pass process: **concept draft → written visual diagnosis → refinement redraw**. Preserve what already works in the draft and target only the diagnosed weaknesses. Do not respond to a weak cover by repeatedly inventing unrelated compositions.

Keep the title, face, product, and symbolic action inside the center square-safe zone of the wide cover. Side regions contain expendable atmosphere only. Treat title integration as an art-direction problem; a generic dark title box is not the default solution. Export the wide cover, center-square crop, and a safe-area proof image. Visually inspect all three.

### 7. Compose, package, validate, and preview

Create semantic HTML with `data-wx-role`, then apply the recipe as inline styles. A preview shell may use CSS/JavaScript outside article markers; the copied article may not. Read [references/quality-gates.md](references/quality-gates.md), run checks, and inspect at 375px width.

Use a new versioned filename for every user-facing revision (`article-v2.html`, not an overwritten ambiguous preview). For a promised "direct-copy" deliverable, package local images into a self-contained HTML file with `scripts/package_single_file.py`; do not leave `file://` or relative image dependencies in the copy payload. Remove discarded or hidden visual prototypes instead of merely hiding them.

Do not call an artifact complete until the rendered page visibly contains the newly requested changes and the copy action has been tested. A first-generation cover is explicitly a draft, never the final cover.

### 8. Deliver

Deliver the diagnosis, selected direction and palette, design recipe, image plan, wide cover, square crop, safe-area proof, clean HTML, self-contained copy-preview page, and a mobile render. Publishing is separate and requires an explicit request and credential check.

## Continuity without sameness

For one author, preserve a small identity layer—byline, caption voice, logo rules, perhaps one brand accent. Vary composition, typography, image grammar, density, and component sequence. The result should resemble one publication with different issues, not one template with different text.

Optionally track recent decisions in `publication-memory.json`; avoid repeating the same opening and section grammar in consecutive pieces without a content reason.

## Originality boundary

- Do not copy third-party theme code, assets, names, or distinctive layouts.
- Market research may inform problem selection; implementation and terminology remain original.
- Keep authoring, design, and publishing separable so a publishing failure cannot damage source or design files.
