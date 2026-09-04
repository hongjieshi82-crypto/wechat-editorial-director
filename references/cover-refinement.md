# Cover diagnosis and refinement

The purpose of the refinement pass is to preserve a promising concept while raising it from an illustration draft to a publication cover.

## Required review artifact

After viewing the actual v1 pixels, create `cover-review.json`:

```json
{
  "status": "draft",
  "preserve": [
    "core scene and story",
    "character relationship",
    "central crop-safe geometry",
    "useful palette anchors"
  ],
  "problems": {
    "hierarchy": "what competes with the headline or focal subject",
    "composition": "missing focal triangle, awkward balance, or dead space",
    "title_integration": "pasted-on, weak contrast, or no designed title zone",
    "lighting_depth": "flat illumination or weak foreground/background separation",
    "character_finish": "expression, hands, clothing, anatomy, or age mismatch",
    "clutter": "secondary props that do not form coherent groups",
    "crop": "important content at risk in the center square",
    "artifacts": "unintended words, logos, gibberish, or malformed objects"
  },
  "refinement_actions": [
    "specific change one",
    "specific change two"
  ]
}
```

Do not fill categories mechanically; omit categories with no real issue.

## Refinement prompt structure

The refinement prompt must contain:

- `Input image`: v1 is the edit target and composition reference.
- `Preserve`: scene, subjects, relationship, palette, and any successful geometry.
- `Improve`: concrete issues from the review, ordered by visual importance.
- `Composition`: desired focal triangle or reading path.
- `Lighting`: named key light, fill light, rim light, and depth intent where relevant.
- `Typography`: exact title, intended location, material/treatment, and integration with the scene.
- `Crop invariants`: title and recognition-critical subjects remain inside the center square.
- `Avoid`: the actual failure modes seen in v1, not a generic negative-prompt list.

## What refinement usually improves

- **Hierarchy:** headline → subject → product/action.
- **Focal geometry:** subjects form a stable triangle or directional path.
- **Lighting:** warm/cool separation, believable screen glow, rim light, and controlled background value.
- **Depth:** foreground framing, focused midground subjects, quieter background.
- **Prop grouping:** books, plants, lamps, or devices form intentional clusters instead of evenly distributed clutter.
- **Character performance:** eye direction, gesture, expression, clothing, and hands support the story.
- **Title integration:** type aligns with architecture, negative space, light, or editorial rules.

## Regenerate versus refine

Refine when the scene, metaphor, or subject relationship already works. Regenerate only when the core concept is wrong, misleading, unusable, or rejected by the user as a direction. Do not discard a working concept merely because finish is weak.

When the user rejects the visual direction itself—such as “too generic,” “too much like a product ad,” or “this feeling is wrong”—return to the article-specific metaphor and change the concept family. Do not keep recoloring or polishing the rejected composition.

## Completion rule

The cover is final only after:

1. v1 and its written diagnosis exist;
2. v2 visibly addresses the diagnosed issues;
3. title text is exact;
4. wide and square crops are separately inspected;
5. unintended brands, text fragments, anatomy problems, and generation artifacts are cleared or explicitly accepted.
