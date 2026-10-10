"""Shared helpers: vault paths, frontmatter parsing, wikilink extraction."""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

sys.stdout.reconfigure(encoding="utf-8")  # Windows consoles default to cp1250/cp1252

ROOT = Path(__file__).resolve().parent.parent
NOTE_DIRS = ("papers", "concepts", "topics", "bridges")

# [[target]], [[target|alias]], [[target#heading]], [[target?]] (uncertain link)
WIKILINK = re.compile(r"\[\[([^\]|#]+?)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)


def read_note(path: Path) -> tuple[dict, str]:
    """Return (frontmatter dict, body) for a Markdown note."""
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER.match(text)
    if not m:
        return {}, text
    meta = yaml.safe_load(m.group(1)) or {}
    return meta, text[m.end():]


def wikilinks(text: str) -> list[str]:
    """Wikilink targets in text, ignoring HTML comments (template hints)."""
    text = HTML_COMMENT.sub("", text)
    targets = [t.strip().rstrip("?").strip() for t in WIKILINK.findall(text)]
    return [t for t in targets if not t.lower().endswith((".png", ".jpg", ".jpeg", ".svg", ".gif"))]


def note_paths(*dirs: str) -> list[Path]:
    out = []
    for d in dirs or NOTE_DIRS:
        out.extend(sorted((ROOT / d).glob("*.md")))
    return out
