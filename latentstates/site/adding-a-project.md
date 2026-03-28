# Adding a Project

Step-by-step for adding a new work to latentstates.org.

---

## 1. Create the project directory

```
/project-name/
/project-name/assets/
/project-name/index.html
```

Use lowercase, hyphenated slugs: `atavic-forest`, `latent-space-i`, `mind-crystal`.

## 2. Build `index.html` from the template

Copy `atavic-forest/index.html` as your starting point. Replace:

- `<title>` -- "Project Name -- Latent States"
- `<meta name="description">` -- one-sentence summary
- Hero media -- video (preferred) or image
- Title, intro, metadata fields
- Image clusters with correct `assets/` paths
- Body text, quotes, credits, exhibition history
- Prev/next navigation links

See `project-template.md` for the full anatomy.

## 3. Add media assets

Place project-specific images and video in `/project-name/assets/`. For images shared across pages (used on landing page thumbnails), place in the root `/assets/` directory.

Image guidelines:
- High resolution source files (2000px+ wide)
- JPG for photographs, PNG for renders with transparency
- Descriptive filenames: `af-02.jpg`, `installation-overview.jpg`
- Include a poster frame for video heroes: `hero-poster.jpg`

## 4. Tag the project

Every project has a `data-tag` attribute on the landing page. Current tags:

| Tag | Meaning |
|:----|:--------|
| `origins` | Early work (Psiloscope, MindCrystal, Human Open Field) |
| `states` | Festival experiments (LSC 2023, 2024, 2025) |
| `spaces` | Immersive installations (Polylith, Atavic Forest, LS1, etc.) |
| `bridge` | Cross-format work (Altered Reflections, Submersion) |

Choose the tag that fits. The pill toggle on the landing page filters by these tags.

## 5. Add to the landing page

In `index.html` (root), add a new `.project-item` in `#project-list` at the correct chronological position:

```html
<div class="project-item" data-img="img-slug" data-tag="spaces">
  <div class="project-cat">Category Label</div>
  <a href="project-name/"><div class="project-title">Project Name</div></a>
  <div class="project-year">Year, Venue</div>
</div>
```

Add the corresponding image in `#project-images`:

```html
<div class="project-image" id="img-slug">
  <img src="assets/thumbnail.jpg" alt="Project Name">
</div>
```

## 6. Add to footer Works list

In the landing page footer, add the project to the Works column `<ul>`:

```html
<li><a href="project-name/">Project Name</a></li>
```

## 7. Update prev/next navigation

On the new project page, set prev/next links to adjacent projects. Then update the adjacent projects' pages to point to the new project. The navigation chain should be continuous.

## 8. Test locally

```bash
cd /path/to/latentstates
python3 -m http.server 8888
# Open http://localhost:8888
```

Check:
- Hero loads (video autoplays, image displays)
- Scroll animations fire (fade-ins)
- Ken Burns drift on gallery images
- Prev/next links resolve
- Landing page hover shows correct image
- Pill toggle filters correctly
- Mobile layout at 900px and 480px breakpoints

## 9. Deploy

Commit and push to `latentstates.github.io`:

```bash
git add .
git commit -m "feat: add Project Name page"
git push origin main
```

GitHub Pages serves from main branch. DNS: `latentstates.org` CNAME points to `latentstates.github.io`.
