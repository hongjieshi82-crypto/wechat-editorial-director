# Semantic component contract

The builder recognizes `data-wx-role`. The semantic source should contain structure and copy, with minimal or no `style` attributes.

## Required shell

```html
<!-- ARTICLE HTML START -->
<section data-wx-role="article">
  <h1 style="display:none;">Publish title</h1>
  <!-- article components -->
</section>
<!-- ARTICLE HTML END -->
```

## Roles

| Role | Intended element | Use |
|---|---|---|
| `article` | outer `section` | article canvas |
| `hero` | `section` | optional opening composition; not necessarily a card |
| `eyebrow` | `p` or `span` | small label above a title |
| `hero-title` | `p` | primary hero promise |
| `hero-accent` | `p` | emphasized second hero line |
| `hero-subtitle` | `p` | one-sentence positioning |
| `chip-row` | `section` | tags container |
| `chip` | `span` | short category tag |
| `body` | `p` | ordinary article paragraph |
| `highlight` | `span` | one decisive phrase |
| `section-header` | `section` | section heading wrapper |
| `section-no` | `span` or `p` | section number |
| `section-copy` | `section` | title and kicker group |
| `section-title` | `p` | section title |
| `section-kicker` | `p` | short explanatory subtitle |
| `callout` | `section` | key judgment or tip |
| `callout-label` | `p` | callout label |
| `callout-text` | `p` | callout copy |
| `quote` | `blockquote` | one memorable conclusion |
| `feature-grid` | `section` | feature-card group |
| `feature-card` | `section` | one capability |
| `feature-icon` | `span` | compact icon/letter/number |
| `feature-title` | `p` | capability title |
| `feature-text` | `p` | capability explanation |
| `steps` | `section` | step-card group |
| `step-card` | `section` | one operation step |
| `step-no` | `span` | step number |
| `step-text` | `span` | step instruction |
| `terminal` | `section` | commands or installation |
| `terminal-bar` | `section` | terminal heading strip |
| `terminal-body` | `section` | terminal content |
| `link-card` | `section` | prominent external webpage, project, repository, or recommended resource |
| `link-card-chrome` | raster image | precomposed light macOS/Safari-style webpage card |
| `link-card-body` | `a` | separate, simple live call-to-action below the image |
| `figure` | `section` | image or SVG wrapper |
| `caption` | `p` | figure caption |
| `chapter-plate` | `img` or `section` | precomposed immersive scene used as an opener or major transition |
| `summary` | `section` | optional closing synthesis that visually continues the article body |
| `summary-title` | `p` | closing heading |
| `summary-text` | `p` | closing copy |
| `divider` | `hr` | quiet section separation |
| `svg-accent` | SVG shape | theme accent fill |
| `svg-soft` | SVG shape | theme soft fill |
| `svg-ink` | SVG text/shape | theme strong ink |
| `svg-muted` | SVG text/shape | theme muted ink |

## Authoring rules

- Use at most one `hero` and at most one `summary`. A hero is optional because WeChat already presents the article title and cover before the body.
- Derive the opening from the selected editorial direction and visual system. It may be a quiet typographic lead, image-led scene, light webpage panel, or direct entry into prose. Do not default to a large dark rounded card.
- Use a heavy dark hero only when its narrative purpose and palette explicitly call for a dark stage, and ensure it does not merely duplicate the platform title and cover.
- A `summary` is optional. When used, render it as ordinary editorial closure: a short heading and one or two body paragraphs, optionally preceded by a thin divider or generous whitespace.
- When the ending is only one sentence or naturally completes the preceding paragraph, merge it into the body instead of isolating it as a `summary`. Do not enlarge or bold a closing sentence merely to manufacture a climax.
- Do not turn the ending into a large dark card, poster, slogan panel, or high-contrast rounded rectangle. Let the final thought conclude in the same reading flow as the body unless the user explicitly requests a card-style ending.
- Use section headers only at real topic transitions.
- A feature list of three or more items becomes `feature-grid`; a sequential procedure becomes `steps`.
- Use `callout` for a conclusion or practical warning, not decorative repetition.
- Present a prominent webpage, GitHub repository, product site, or recommended tool as a light macOS/Safari-style `link-card` instead of a dark terminal block or a naked long URL. Precompose the browser chrome, real address, title, and description into one static image so WeChat cannot reflow the design. Attach one simple live CTA footer such as “打开项目主页 →” directly beneath the image, sharing the card's left/right edges and bottom corners so it remains one visual object. Do not use positioning, image maps, or a complex nested anchor to make only part of the bitmap clickable.
- Keep source citations and low-priority references as restrained text links or endnotes. Do not turn every citation into a large browser card.
- A link card may borrow the selected palette accent, but its canvas remains light and browser-like by default. Do not fabricate page screenshots, favicons, statistics, or repository metadata.
- Use no more than one opening `chapter-plate` plus one major transition plate in a normal article. It must be a precomposed image, not CSS-dependent background layering.
- For SVG elements, put the role on the exact shape or text node so the theme can set `fill` or `stroke`.
- Do not encode theme names in article copy.

## Compact example

```html
<section data-wx-role="hero">
  <p data-wx-role="eyebrow">PRODUCT NOTE</p>
  <p data-wx-role="hero-title">我做了一个小工具</p>
  <p data-wx-role="hero-accent">让学习少一次跳转</p>
  <p data-wx-role="hero-subtitle">一句话说清它帮谁解决什么问题。</p>
</section>

<section data-wx-role="section-header">
  <span data-wx-role="section-no">01</span>
  <section data-wx-role="section-copy">
    <p data-wx-role="section-title">为什么要做它？</p>
    <p data-wx-role="section-kicker">从一个真实痛点开始</p>
  </section>
</section>
<p data-wx-role="body">正文内容。</p>
```
