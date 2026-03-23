# Links in Site Content

## Format

Use markdown link syntax in all site content (descriptions, narratives, site.md):

```
[Author et al., Year](https://doi.org/DOI)
```

## Examples

### Published paper (via DOI)
```
[Matias et al., 2017](https://doi.org/10.7554/eLife.20552)
```

### Preprint (bioRxiv)
```
[recent preprint](https://doi.org/10.1101/2025.08.01.668048)
```

### Conference poster
```
[presented at Cosyne 2026](https://cosyne.org)
```

### External site
```
[International Brain Laboratory](https://internationalbrainlab.org)
```

## Rules

1. **Every empirical claim must link to its source** — if you can't link it, you can't state it as a finding
2. **Use DOI links** (`https://doi.org/...`) for papers, not journal URLs — DOIs are permanent
3. **Preprints**: link to bioRxiv/arXiv DOI, use language like "in a preprint" or "reported in a preprint"
4. **Unpublished work**: no links possible — describe the question, not the finding
5. **Links open in new tab** — the build system adds `target="_blank"` automatically
6. **Don't link the same reference twice** in a short description — link on first mention only

## Where links work

- `public_description` in project.yaml
- Theme narratives in research/*.md
- Lab intro in site.md
- Any text field rendered by build.py

The build system converts `[text](url)` to `<a href="url" target="_blank">text</a>` at build time.
