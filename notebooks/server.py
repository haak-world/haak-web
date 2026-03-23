#!/usr/bin/env python3
"""Notebook browser server — serves UI + JSON API + page images."""

import json, os, re, sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import unquote

PORT = int(sys.argv[sys.argv.index("--port") + 1]) if "--port" in sys.argv else 8421

# Resolve paths
HERE = Path(__file__).resolve().parent
HAAK = HERE
while HAAK.name and not (HAAK / "CLAUDE.md").exists():
    HAAK = HAAK.parent
BOOKS = HAAK / "projects" / "writing" / "notebook-ressurection" / "books"
MASTER_INDEX = BOOKS.parent / "index-master.md"
HTML_FILE = HERE / "index.html"


def get_notebook_dirs():
    return sorted(
        [d for d in BOOKS.iterdir() if d.is_dir() and (d / "manifest.json").exists()],
        key=lambda d: d.name,
    )


def load_manifests():
    result = []
    for d in get_notebook_dirs():
        with open(d / "manifest.json") as f:
            m = json.load(f)
        m["dir_name"] = d.name
        m["page_count"] = len(list((d / "pages").glob("page-*.jpg"))) if (d / "pages").exists() else 0
        result.append(m)
    return result


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = unquote(self.path).split("?")[0]

        if path == "/" or path == "/index.html":
            self._serve_file(HTML_FILE, "text/html")
        elif path == "/api/notebooks":
            self._serve_json(load_manifests())
        elif path == "/api/master-index":
            self._serve_file(MASTER_INDEX, "text/plain; charset=utf-8")
        elif m := re.match(r"/api/notebook/([^/]+)/transcription", path):
            self._serve_transcription(m.group(1))
        elif m := re.match(r"/api/notebook/([^/]+)/page/(\d+)", path):
            self._serve_page(m.group(1), m.group(2))
        else:
            self.send_error(404)

    def _serve_json(self, data):
        body = json.dumps(data, ensure_ascii=False).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)

    def _serve_file(self, filepath, content_type):
        if not filepath.exists():
            self.send_error(404)
            return
        data = filepath.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", len(data))
        self.end_headers()
        self.wfile.write(data)

    def _serve_transcription(self, dir_name):
        p = BOOKS / dir_name / "transcription.md"
        self._serve_file(p, "text/plain; charset=utf-8")

    def _serve_page(self, dir_name, num):
        p = BOOKS / dir_name / "pages" / f"page-{int(num):03d}.jpg"
        if not p.exists():
            self.send_error(404)
            return
        data = p.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "image/jpeg")
        self.send_header("Content-Length", len(data))
        self.send_header("Cache-Control", "public, max-age=86400")
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):
        pass  # quiet


if __name__ == "__main__":
    print(f"Notebook browser → http://localhost:{PORT}")
    print(f"Books directory:  {BOOKS}")
    HTTPServer(("", PORT), Handler).serve_forever()
