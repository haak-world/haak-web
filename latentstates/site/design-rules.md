# Design Rules

Non-negotiable rules for latentstates.org. These emerged from design conversation and are baked into the CSS. Violating any of them breaks the site's identity.

---

## 1. Images and text never share the same space

No text overlaid on images. No background images behind text. No captions inside image containers. Images occupy their grid columns; text occupies its grid columns. The hero section is the one exception -- it contains only media, no text overlay.

## 2. The frame is neutral. Color comes from the artwork.

Site chrome uses a neutral grey palette only. No browns, no terracotta, no color accents. Grey metadata (`#888`), grey accents (`#9a9a9a`), grey borders (`#ddd` on light, `rgba(255,255,255,0.06)` on dark). The photographs, renders, and videos provide all the color. The frame never competes.

## 3. Serif typography

Source Serif 4 Variable, loaded from Google Fonts. Weight map:
- **700** -- titles (project name, opening question)
- **500** -- labels (metadata labels, category tags, navigation)
- **400** -- body text, intro text, credits
- **300** -- opening question, closing text (light weight for large sizes)

Variable font weight transitions on hover: `font-variation-settings: 'wght' 400` to `'wght' 700`, `0.2s ease`. System sans-serif (`-apple-system, BlinkMacSystemFont, 'Segoe UI'`) used only for small uppercase labels (category tags, footer headings, pill toggle).

## 4. Dark landing, light project pages

Landing page: `#1a1a1a` background, `#e8e8e8` foreground. Project pages: `#f4f4f4` background, `#232222` foreground. The contrast marks the threshold between browsing and reading. The header bar (`#232222`) is the one dark element that persists on project pages.

## 5. Images cluster tight, text breathes

| Gap | Where |
|:----|:------|
| 5px | Between consecutive images in a cluster |
| 60px | Between adjacent text blocks |
| 90px | Between image clusters and text |
| 120px | After intro text, before metadata |
| 150px | Before prev/next navigation |

These are encoded as `.gap-5`, `.gap-60`, `.gap-90`, `.gap-120`, `.gap-150` utility classes.

## 6. Gallery catalog, not website

Maximum reverence for the artwork. Minimum interface. No decorative elements, no gradients, no shadows, no rounded corners on images. Images sit flush. The design gets out of the way.

## 7. Video over stills for heroes

When video exists for a project, use it as the hero. Attributes: `autoplay muted loop playsinline preload="auto"`. Include a `poster` frame for loading state. Keep original resolution -- don't compress to fit a standard aspect ratio.

## 8. Ken Burns drift on gallery images

Subtle animation on gallery images: scale `1.02` to `1.05`, rotation `-0.3deg` to `0.3deg`, over 30 seconds, `ease-in-out infinite alternate`. Stagger delays across images in a cluster (0s, 4s, 8s, 12s...). Parent containers must have `overflow: hidden`.

```css
.gallery-image {
  animation: subtle-drift 30s ease-in-out infinite alternate;
}
@keyframes subtle-drift {
  0%   { transform: scale(1.02) rotate(-0.3deg); }
  100% { transform: scale(1.05) rotate(0.3deg); }
}
```

## 9. People appear inside works, not in a separate roster

No "Team" page with headshots. Credits are structured by role on each project page. People are visible through their contributions, not through portraits.

## 10. No text decoration on links

All links inherit color, `text-decoration: none`. Hover state is `opacity: 0.7`. No underlines, no color shifts. Links are discoverable by context, not by visual noise.
