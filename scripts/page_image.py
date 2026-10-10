"""Render PDF page(s) to PNG so figures/tables embedded as images can be read.

Use when a converted full text shows a table/figure caption without its content.
After reading, transcribe the numbers into fulltext/<citekey>.md under
"## Tables transcribed from page images (p. N)" so they become searchable.

Example: python scripts/page_image.py song2022eeg 6 --top 0.62
"""
from __future__ import annotations

import argparse
import tempfile
from pathlib import Path

import pymupdf

from notes import ROOT


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("citekey")
    ap.add_argument("pages", nargs="+", type=int, help="1-based page numbers")
    ap.add_argument("--top", type=float, default=1.0, help="keep only the top fraction of the page")
    ap.add_argument("--dpi", type=int, default=170)
    ap.add_argument("--out", default=str(Path(tempfile.gettempdir()) / "eeg-pages"))
    a = ap.parse_args()

    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(ROOT / "pdf" / f"{a.citekey}.pdf")
    for n in a.pages:
        page = doc[n - 1]
        r = page.rect
        clip = pymupdf.Rect(r.x0, r.y0, r.x1, r.y0 + r.height * a.top)
        path = out / f"{a.citekey}_p{n}.png"
        page.get_pixmap(dpi=a.dpi, clip=clip).save(path)
        print(path)


if __name__ == "__main__":
    main()
