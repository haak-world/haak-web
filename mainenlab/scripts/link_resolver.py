"""Link resolver for mainenlab site content.

Resolves entity mentions to canonical URLs. Used by description generator
and build.py to ensure all content has meaningful links.
"""

import re
from pathlib import Path

try:
    import yaml
    def _load_yaml(text):
        return yaml.safe_load(text) or {}
except ImportError:
    raise SystemExit("PyYAML required: pip install pyyaml")


class LinkResolver:
    def __init__(self, lab_root):
        self.lab_root = Path(lab_root)
        self._papers = {}   # slug -> {doi, title, year, authors}
        self._projects = {} # slug -> {name}
        self._themes = {}   # slug -> {label}
        self._people = {}   # slug -> {name}
        self._load()

    def _load(self):
        pubs_dir = self.lab_root / "publications"
        if pubs_dir.exists():
            for d in pubs_dir.iterdir():
                paper_file = d / "paper.md"
                if not paper_file.exists():
                    continue
                text = paper_file.read_text(errors='replace')
                if not text.startswith('---'):
                    continue
                parts = text.split('---', 2)
                if len(parts) < 3:
                    continue
                try:
                    meta = _load_yaml(parts[1])
                    if meta and meta.get('title'):
                        self._papers[d.name] = {
                            'doi': meta.get('doi', ''),
                            'title': meta.get('title', ''),
                            'year': meta.get('year', ''),
                            'authors': meta.get('authors', []),
                        }
                except Exception:
                    pass

        proj_dir = self.lab_root / "projects"
        if proj_dir.exists():
            for d in proj_dir.iterdir():
                pf = d / "project.yaml"
                if not pf.exists():
                    continue
                try:
                    meta = _load_yaml(pf.read_text(errors='replace'))
                    if meta and meta.get('name'):
                        proj_type = meta.get('type', 'lab')
                        if proj_type != 'internal':
                            self._projects[d.name] = {'name': meta['name']}
                except Exception:
                    pass

        tax_file = self.lab_root / "taxonomy.yaml"
        if tax_file.exists():
            try:
                tax = _load_yaml(tax_file.read_text())
                for theme in tax.get('themes', []):
                    slug = theme.get('slug', '')
                    label = theme.get('label', slug.title())
                    self._themes[slug] = {'label': label}
                    for child in theme.get('children', []):
                        cs = child.get('slug', '')
                        cl = child.get('label', cs.title())
                        self._themes[cs] = {'label': cl}
            except Exception:
                pass

        people_dir = self.lab_root / "people"
        if people_dir.exists():
            for d in people_dir.iterdir():
                pf = d / "person.yaml"
                if not pf.exists():
                    continue
                try:
                    meta = _load_yaml(pf.read_text(errors='replace'))
                    if meta and meta.get('name'):
                        self._people[d.name] = {'name': meta['name']}
                except Exception:
                    pass

    def paper_url(self, slug):
        p = self._papers.get(slug)
        if p and p['doi']:
            doi = p['doi']
            if not doi.startswith('http'):
                doi = f"https://doi.org/{doi}"
            return doi
        return None

    def paper_citation(self, slug):
        p = self._papers.get(slug)
        if not p:
            return None
        url = self.paper_url(slug)
        if not url:
            return None
        authors = p.get('authors', [])
        year = p.get('year', '')
        if authors:
            first = authors[0].split(',')[0].split()[-1]
            cite = f"{first} et al., {year}" if len(authors) > 1 else f"{first}, {year}"
        else:
            cite = f"{year}"
        return f"[{cite}]({url})"

    def project_anchor(self, slug):
        if slug in self._projects:
            return f"#project-{slug}"
        return None

    def theme_filter(self, slug):
        if slug in self._themes:
            return f"#themes={slug}"
        return None

    def person_url(self, slug):
        if slug in self._people:
            return f"https://personnel.haak.world/person/{slug}"
        return None

    def available_papers_table(self):
        lines = []
        for slug, p in sorted(self._papers.items(), key=lambda x: x[1].get('year', 0), reverse=True):
            if p.get('doi'):
                authors = p.get('authors', [])
                first_author = authors[0].split(',')[0].split()[-1] if authors else 'Unknown'
                lines.append(f"- {slug}: {first_author} et al. {p['year']} -- {p['title'][:80]} -- DOI: {p['doi']}")
        return '\n'.join(lines)

    def available_projects_table(self):
        lines = []
        for slug, p in sorted(self._projects.items()):
            lines.append(f"- {slug}: {p['name']}")
        return '\n'.join(lines)
