"""BM25 keyword search over fulltext/, papers/, concepts/ (paragraph level).

Examples:
  python scripts/search.py masked pretraining
  python scripts/search.py "cross-subject" generalization --dir fulltext -n 5
  python scripts/search.py probing superposition --dir concepts --dir papers
"""
from __future__ import annotations

import argparse
import re

from rank_bm25 import BM25Okapi

from notes import ROOT

DIRS = ("fulltext", "papers", "concepts", "topics", "bridges")
TOKEN = re.compile(r"[a-z0-9]+")
PAGE = re.compile(r"<!--\s*page (\d+)\s*-->")


def tokenize(text: str) -> list[str]:
    return TOKEN.findall(text.lower())


def paragraphs(dirs):
    """Yield (path, page or None, paragraph) for every non-trivial paragraph."""
    for d in dirs:
        for path in sorted((ROOT / d).glob("*.md")):
            page = None
            for para in re.split(r"\n\s*\n", path.read_text(encoding="utf-8")):
                if m := PAGE.search(para):
                    page = int(m.group(1))
                para = PAGE.sub("", para).strip()
                if len(tokenize(para)) >= 4:
                    yield path, page, para


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("terms", nargs="+", help="query terms (combined into one query)")
    ap.add_argument("--dir", action="append", choices=DIRS,
                    help="restrict to a folder (repeatable; default: all)")
    ap.add_argument("-n", type=int, default=10, help="number of hits (default 10)")
    ap.add_argument("--width", type=int, default=300, help="snippet length in chars")
    args = ap.parse_args()

    corpus = list(paragraphs(args.dir or DIRS))
    if not corpus:
        print("corpus is empty")
        return
    bm25 = BM25Okapi([tokenize(p) for _, _, p in corpus])
    query = tokenize(" ".join(args.terms))
    scores = bm25.get_scores(query)
    ranked = sorted(range(len(corpus)), key=lambda i: scores[i], reverse=True)

    shown = 0
    for i in ranked[: args.n]:
        if scores[i] <= 0:
            break
        path, page, para = corpus[i]
        loc = path.relative_to(ROOT).as_posix() + (f" (p. {page})" if page else "")
        snippet = " ".join(para.split())
        if len(snippet) > args.width:
            snippet = snippet[: args.width] + "…"
        print(f"{scores[i]:6.2f}  {loc}\n        {snippet}\n")
        shown += 1
    if not shown:
        print(f"no hits for: {' '.join(query)}")


if __name__ == "__main__":
    main()
