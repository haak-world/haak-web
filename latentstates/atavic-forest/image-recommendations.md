# Atavic Forest -- Image Recommendations

Analysis date: 2026-03-25

## Current state

The page at `/atavic-forest/` uses 14 images:

- **Hero**: `../assets/cf-metamersion-ls-atavic-forest.jpg` (1636x2385, portrait, brightness 45)
- **Gallery**: `af-01` through `af-13` (all 1600x900, landscape)
- **Mucho Flow scenes**: 20 images in `assets/` (1024x704) -- none currently used on the page

### Problems identified

1. **The hero image is portrait orientation (0.69:1) in a landscape hero slot.** It works because `object-fit: cover` crops it, but the framing is not ideal -- much of the composition is lost. The image itself is strong (vivid magenta/green/blue forest, high saturation 186) but dark overall (brightness 45).

2. **Many gallery images are catastrophically dark.** Six of the thirteen af-images have average brightness below 15/255:
   - `af-06` (brightness 1) -- essentially black with faint green text. A title card, not a photograph.
   - `af-08` (brightness 2) -- another title card ("Atavic Forest Installation" in green text on black).
   - `af-04` (brightness 9) -- presentation slide: vivid fern image embedded in black field with green captions.
   - `af-03` (brightness 11) -- presentation slide: same format, different scene.
   - `af-05` (brightness 15) -- generated mushroom scene, mostly swallowed by black borders.
   - `af-09` (brightness 15) -- silhouette of person with glasses in deep blue/amber light. Atmospheric but very dark.

3. **af-03, af-04, af-05 are presentation screenshots, not gallery-quality images.** They show generated content inside a narrow portrait window surrounded by black, with green overlay text ("180k textual descriptions...", "Fern Textural Surface"). These are documentation of a talk, not images of the installation or its output.

4. **af-06 and af-08 are title cards** -- green text on black. They break the visual flow entirely.

5. **The Mucho Flow images are the strongest generative outputs** and none of them appear on the page, despite the text describing the Mucho Flow Festival extension in detail.

## Image-by-image assessment

### Gallery images (af-01 to af-13)

| Image | Content | Brightness | Verdict |
|:------|:--------|:-----------|:--------|
| af-01 | Dreamy forest with mist, pink/blue/amber tones, tree silhouettes | 53 | KEEP -- best establishing shot of the generative forest. Ethereal. |
| af-02 | Tangled dark branches against cyan-green sky, red mossy masses | 40 | KEEP -- strong composition, alien canopy feel. |
| af-03 | Presentation screenshot: narrow portrait image + green text overlay | 11 | REMOVE -- not gallery material. |
| af-04 | Presentation screenshot: "Fern Textural Surface" + green text | 9 | REMOVE -- not gallery material. |
| af-05 | Generated mushroom on forest floor, surrounded by black | 15 | REMOVE -- too dark, framed as a slide not a photograph. |
| af-06 | Title card: green text on black | 1 | REMOVE -- not an image at all. |
| af-07 | Projection on wall: vivid green/red botanical scene, audience silhouettes visible | 47 | KEEP -- shows the installation in situ with audience. Essential documentation. |
| af-08 | Title card: "Atavic Forest Installation" in green on black | 2 | REMOVE -- title card. |
| af-09 | Silhouette of person with round glasses, deep blue light, amber glow from equipment | 15 | KEEP (barely) -- beautiful portrait of someone operating the installation, but very dark. Could work as a moody closing image. |
| af-10 | Person silhouetted at mixing desk, bathed in vivid purple/violet light, wall behind | 130 | KEEP -- strongest documentation photo. Shows the sound dimension. Striking color. |
| af-11 | Close-up of code on screen, purple light spilling from left edge | 30 | KEEP -- shows the computational layer. Good detail shot. |
| af-12 | Projector beam cutting through purple haze in warehouse ceiling | 120 | KEEP -- shows the physical space and projection apparatus. Dramatic. |
| af-13 | Person silhouetted in saturated red/orange light field | 78 | KEEP -- immersive atmosphere shot, audience-in-the-work. High saturation (250). |

### Mucho Flow scenes (best candidates)

| Image | Content | Brightness | Contrast | Saturation | Verdict |
|:------|:--------|:-----------|:---------|:-----------|:--------|
| mucho-alien-fungi-066 | Purple mushrooms with orange gills, dripping, teal background | 98 | 60 | 142 | BEST Mucho image. Gorgeous, vivid, immediately legible. |
| mucho-alien-fungi-033 | Pink/purple mushrooms, warm bokeh background | 79 | 55 | 160 | Excellent. More whimsical than 066. |
| mucho-hard-particle-066 | Explosive radial burst -- purple/yellow/magenta particle eruption | 80 | 55 | 175 | Visually spectacular. Highest saturation of all Mucho images. |
| mucho-alien-vegetation-033 | Aerial view of purple-smoking crater in vivid moss/magenta landscape | 84 | 50 | 109 | Strong landscape composition. Shows geological scale. |
| mucho-tube-portal-033 | Tunnel/portal receding into blue light, organic layered walls | 47 | 36 | 147 | Compelling depth. Good "journey" metaphor. Bit dark. |
| mucho-thermal-fire-033 | Black silhouette forms against pink/blue veined luminous field | 79 | 63 | 103 | Abstract, biological. High contrast. |
| mucho-toxic-mycelium-066 | Dense mycelial network, amber/brown/teal, fibrous macro detail | 57 | 49 | 165 | Beautiful texture. Very high saturation. |
| mucho-disgusting-forest-066 | Bare tree silhouettes in grey mist -- moody, minimal | 124 | 58 | 61 | Ethereal but low saturation. Contemplative. |
| mucho-reactor-spores-033 | Spray-painted concrete wall with cyan/yellow residue, debris | 99 | 42 | 79 | NOT a generative image -- this appears to be documentation of a physical space/aftermath. Exclude. |
| mucho-night-forest-033 | Near-black dense jungle | 21 | 14 | 65 | Too dark to be useful. |

## Recommendations

### Hero image

**Keep the current hero** (`cf-metamersion-ls-atavic-forest.jpg`). Despite its portrait orientation, it is the most vivid and recognizable image of the installation's core output -- the neon-lit forest with magenta trunks and blue ground glow. The `object-fit: cover` crop works acceptably in the landscape hero slot, centering on the strongest part of the composition. No other single image better communicates "generative neural forest."

If you want a landscape-orientation alternative, **af-01** (the misty dreaming forest) would be the strongest candidate -- it reads as pure generative output without documentary framing, has good depth, and the warm-to-cool color gradient is arresting.

### Gallery layout (narrative arc)

Restructure the gallery from 13 images down to 10, organized in three clusters that follow the page's three text sections:

**Cluster 1 -- The Generative Forest** (accompanies the latent-space/IR-tracking text)
1. `af-01` -- Establishing shot. Misty forest, rainbow tones. "This is what the model dreams."
2. `af-02` -- Alien canopy. Dark tangled branches against cyan void. Depth and strangeness.
3. `mucho-alien-fungi-066` -- Purple mushrooms. The model's flora made vivid. Introduces the generative richness.

**Cluster 2 -- Sound and Space** (accompanies the Saldanha/sound text)
4. `af-07` -- Installation in situ. Projection on wall, audience silhouettes. Grounds the work in physical space.
5. `af-13` -- Red immersion. Person silhouetted in saturated red field. The body inside the generated world.

**Cluster 3 -- Mucho Flow Worlds** (accompanies the Mucho Flow Festival text, then final cluster)
6. `mucho-hard-particle-066` -- Particle explosion. Purple/yellow radial burst. Maximum visual impact.
7. `mucho-alien-vegetation-033` -- Purple-smoking crater landscape. Different generative lens on the same corpus.
8. `mucho-tube-portal-033` -- Tunnel/portal. Draws the eye inward. The journey metaphor.
9. `af-10` -- Sound operator in purple light. The human hand behind the machine.
10. `af-12` -- Projector beam in haze. The apparatus. Closing the circle from output back to mechanism.

Optional additions if more images are wanted:
- `af-11` (code on screen) after af-10 -- the computational layer
- `af-09` (glasses silhouette in blue) as a moody closer
- `mucho-thermal-fire-033` (biological abstraction) in the Mucho cluster for more variety

### Images to remove

| Image | Reason |
|:------|:-------|
| `af-03` | Presentation screenshot with text overlays. Not gallery material. |
| `af-04` | Presentation screenshot with text overlays. Not gallery material. |
| `af-05` | Generated content trapped in black presentation frame. Too dark. |
| `af-06` | Title card (green text on black). Not a photograph or render. |
| `af-08` | Title card (green text on black). Not a photograph or render. |

### Mucho Flow images to skip

| Image | Reason |
|:------|:-------|
| `mucho-reactor-spores-033` | Appears to be a photo of spray-painted concrete, not generative output. |
| `mucho-reactor-spores-066` | Same series -- physical documentation, not generative. |
| `mucho-night-forest-033/066` | Too dark (brightness 21). Nearly invisible. |
| `mucho-atavic-forest-033/066` | Low contrast, murky. The af-01/af-02 serve this role better. |
| `mucho-disgusting-forest-033` | Adequate but redundant with af-01's misty forest feel. |

### Summary of changes

- **Remove 5 images**: af-03, af-04, af-05, af-06, af-08 (presentation slides and title cards)
- **Add 4 Mucho Flow images**: mucho-alien-fungi-066, mucho-hard-particle-066, mucho-alien-vegetation-033, mucho-tube-portal-033
- **Reorder remaining af images** into a narrative arc: generative output, installation documentation, extended worlds, human operators
- **Net result**: 10 images (down from 13), all visually strong, no dead-dark frames, Mucho Flow presence matches the text
