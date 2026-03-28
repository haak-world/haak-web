# Landing Page Architecture

Structure and behavior of the latentstates.org homepage.

---

## Overview

Four sections in vertical sequence: Opening, Projects, Closing, Footer. Dark theme throughout (`#1a1a1a`). No navigation bar -- the opening IS the navigation. Single-page scroll into the project list.

## Section 1: Opening

Full viewport (`100vh`). Three layers:

### Flow Field Canvas
`<canvas id="flow-canvas">` fills the entire section. Simplex 2D noise drives a particle flow field:

- **320 particles** with 18-point trails
- **Neutral grey palette**: `#8a8a8a`, `#a0a0a0`, `#b0b0b0`, `#787878`, `#c0c0c0`
- **Dual-scale Perlin noise**: `SCALE1 = 0.003`, `SCALE2 = 0.006`
- **Cursor-reactive**: 280px radius, tangential + radial force, speed-boosted
- **Rendering**: `globalAlpha 0.18` for trails, `0.35` for particles. Fade via `rgba(26,26,26,0.015)` fill each frame
- **Performance**: stops rendering when opening section scrolls out of view (IntersectionObserver)

### Opening Text
Centered, `z-index: 1`, `pointer-events: none`:

- **Question**: "What is it like to experience?" -- `clamp(48px, 6vw, 80px)`, weight 300
- **Subline**: "Yourself. The world. Other people. A machine." -- `clamp(18px, 2.2vw, 28px)`, weight 300, 50% opacity

Both fade out on scroll via GSAP (`opacity: 0, y: -40`, scrubbed from `top top` to `60% top`).

### Scroll Indicator
"Scroll" label + chevron SVG at bottom. 40% opacity, pulses with 2.5s ease-in-out animation. Fades on scroll (10% to 30%).

## Section 2: Projects

Split layout inside a 1400px max-width container with `6vw` horizontal padding.

### Left Column (40%)
Vertically centered list of `.project-item` entries. Each item has:
- **Category label** (`.project-cat`) -- 11px uppercase, system sans-serif, `#888`
- **Title** (`.project-title`) -- `clamp(22px, 2.5vw, 32px)`, weight 400. On hover, variable weight transitions to 700 over 0.2s
- **Year** (`.project-year`) -- 13px, `#888`

Items separated by `1px solid rgba(255,255,255,0.06)` borders.

### Right Column (60%)
Stacked `.project-image` containers, all `position: absolute`. Only one visible at a time (`opacity: 1` via `.visible` class). Crossfade on hover (`transition: opacity 0.4s ease`). Images are `object-fit: cover`, fill the container with `inset: 2vh 0`.

### Hover Behavior
`mouseenter` on a project item shows its corresponding image (matched by `data-img` attribute). `mouseleave` returns to the last hovered image (persists).

### Data Attributes
Each `.project-item` carries:
- `data-img` -- ID of the corresponding image element
- `data-tag` -- category for filtering (`origins`, `states`, `spaces`, `bridge`)

## Pill Toggle

Fixed at bottom center (`bottom: 4vh`), `z-index: 100`. Appears/disappears based on projects section visibility (ScrollTrigger, `top 80%` to `bottom 20%`).

- **Three options**: All, States, Spaces
- **Frosted glass**: `rgba(26,26,26,0.7)` + `backdrop-filter: blur(12px)`
- **Sliding indicator**: `.pill-slider` animates `transform` and `width` to match active option
- **Filtering**: `.filtered-out` class hides non-matching project items (`display: none`)

Note: "origins" and "bridge" tags exist on project items but have no pill option. They show under "All" only.

## Section 3: Closing

Centered text: "The question continues." -- `clamp(36px, 5vw, 64px)`, weight 300. `20vh` vertical padding. Fades in via GSAP (`opacity: 0, y: 30`, scrubbed from `top 80%` to `top 40%`).

## Section 4: Footer

Three-column grid (1200px max), separated by `1px solid rgba(255,255,255,0.06)` top border:

| Column | Content |
|:-------|:--------|
| Works | Full project list with links |
| Partners | Boom Festival, Waking Life, CF, Lunar Ring |
| More | People, About |

Colophon below: "Zachary Mainen . Champalimaud Foundation . Lisbon"

## Responsive (768px)

- Projects layout stacks vertically (column direction)
- Image container goes full width, 50vh min-height
- Footer collapses to single column
- Pill toggle moves to `bottom: 2vh`
