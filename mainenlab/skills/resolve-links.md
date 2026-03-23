# Skill: Resolve Links

## Purpose

When writing or generating content for the mainenlab site, resolve every entity mention to a clickable link.

## Usage

### In project descriptions (public_description in project.yaml)

Papers — link to DOI:
```
We showed that serotonin neurons fire at unexpected events ([Ranade & Mainen, 2009](https://doi.org/10.1152/jn.91007.2008)).
```

Other projects — link to site anchor:
```
Building on our work on [facial expression decoding](#project-face-flipping-decoding), we are investigating...
```

Themes — link to filter view:
```
This project connects our [serotonin](#themes=serotonin) research with [consciousness](#themes=consciousness) science.
```

### In theme narratives (research/*.md)

Same markdown link syntax. Build.py converts at build time.

### Rules

1. Look up DOIs from paper.md files: `publications/{slug}/paper.md` → `doi:` field
2. Project anchors use the slug: `#project-{slug}`
3. Theme filters use the slug: `#themes={slug}`
4. First mention only — don't re-link the same entity
5. If no DOI exists (unpublished), don't link — describe the question instead
6. Preprints: link to bioRxiv DOI, note "preprint" or "reported in a preprint"

### Link format quick reference

| What | Format |
|------|--------|
| Published paper | `[Author et al., Year](https://doi.org/DOI)` |
| Preprint | `[preprint](https://doi.org/10.1101/...)` |
| Project on site | `[name](#project-slug)` |
| Theme filter | `[theme](#themes=slug)` |
| Person (internal only) | `[name](https://personnel.haak.world/person/slug)` |
