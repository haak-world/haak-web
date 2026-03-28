# Project Page Template

Anatomy of a project page, based on the Atavic Forest implementation. Every project page follows this structure.

---

## Page Shell

```html
<title>Project Name — Latent States</title>
```

- **Font**: Source Serif 4 Variable (Google Fonts)
- **Scripts**: GSAP 3.12.5 + ScrollTrigger (CDN)
- **Background**: `#f4f4f4` (light)

## Header

Fixed dark bar, 56px tall, `#232222` background. "Latent States" link left, `x` close button right. Both link to `../` (landing page). `z-index: 100`.

## Hero

Full-bleed media, `calc(100vh - 56px)` height, `margin-top: 56px` to clear header. Video preferred (`autoplay muted loop playsinline`), image fallback. `object-fit: cover`. No overlay, no text.

## 12-Column Grid

All content below the hero lives in a single grid container:

```css
.grid-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 0 20px;
}
```

Column assignments define the layout rhythm:

| Element | Grid columns | Width ~% | Alignment |
|:--------|:-------------|:---------|:----------|
| Title | 1 / 9 | 65% | Left |
| Intro | 1 / 9 | 65% | Left |
| Metadata row | 5 / 13 | 65% | Right |
| Body text | 7 / 13 | 50% | Right |
| Image zone | 1 / 9 | 65% | Left |
| Image zone (full) | 1 / -1 | 100% | Full |
| Image caption | 1 / 4 | 25% | Left margin |
| Captioned image | 4 / 13 | 75% | Right |
| Quote block | 7 / 13 | 50% | Right |
| Video link | 7 / 13 | 50% | Right |
| Credits | 7 / 13 | 50% | Right |
| Exhibitions | 7 / 13 | 50% | Right |

The asymmetry is intentional: images anchor left, text flows right.

## Content Sections (top to bottom)

### 1. Title
72px, weight 700, `letter-spacing: -0.02em`. Class: `.project-title`.

### 2. Intro
24px, weight 400, `line-height: 1.4`. One paragraph, no more than three sentences. Class: `.project-intro`.

### 3. Metadata Row (after 120px gap)
Horizontal flex inside columns 5-13. Each `.meta-item` has a thin `border-top`, a `.meta-label` (10px uppercase), and the value (13px). Typical fields: Year, Type, Venue, Programme, Collective.

### 4. Image Clusters (after 90px gap)
Images stack vertically with 5px gaps. Apply `.gallery-image` class for Ken Burns drift. Stagger `animation-delay` by 4s per image. Wrap in `.image-zone` (cols 1-9) or `.image-zone-full` (full width). Parent has `overflow: hidden`.

### 5. Captions
`.image-caption` in cols 1-4. Label format: `[Img. 001]` in 9px uppercase (`.caption-label`), description below in 11px grey.

### 6. Body Text
`.body-text` in cols 7-13. 17px, weight 400, `line-height: 1.6`. Paragraphs spaced at `1.4em`.

### 7. Quote Block
`.quote-block` in cols 7-13. Italic, `color: #555`, `border-left: 2px solid var(--border)`, `padding-left: 24px`.

### 8. Video Link
`.video-link` in cols 7-13. Play icon SVG + text. `border-bottom: 1px solid var(--border)`. Opens in new tab.

### 9. Credits
`.credits` in cols 7-13. Role headings as `<strong>` (11px uppercase), names below in 15px grey. Roles in order: installation by, direction, artists, sound, programme, curators, coordination.

### 10. Exhibition History
`.exhibitions` in cols 7-13. Title as `.ex-title` (11px uppercase), then `<ul>` with venue, city, date range per `<li>`.

## Prev/Next Navigation (after 150px gap)

Outside the grid container. Two `.nav-item` links side by side, each with a thumbnail (200px tall, `object-fit: cover`), direction label, and project title. On hover, non-hovered item fades to `opacity: 0.4`.

## Footer

Centered, minimal: "Latent States . Zachary Mainen . Champalimaud Foundation". 13px, grey.

## GSAP ScrollTrigger

All elements with `.fade-in` start at `opacity: 0; transform: translateY(24px)` and animate to visible when they enter the viewport at 88%:

```js
gsap.utils.toArray('.fade-in').forEach(el => {
  gsap.to(el, {
    opacity: 1, y: 0, duration: 0.8, ease: 'power2.out',
    scrollTrigger: { trigger: el, start: 'top 88%', once: true }
  });
});
```

## Responsive Breakpoints

**900px** -- Grid collapses to single column. Title drops to 44px. Hero shrinks to 60vh. Metadata items wrap to 50% width. Prev/next stacks vertically.

**480px** -- Title drops to 36px. Intro to 18px. Metadata items go full width. Content padding reduced to 50px top.
