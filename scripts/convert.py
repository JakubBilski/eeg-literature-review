"""Convert pdf/*.pdf -> fulltext/<citekey>.md.

PDFs must be named <citekey>.pdf. Backend preference: marker > docling > pymupdf
(pymupdf4llm is used inside the pymupdf fallback if installed). Already converted
files are skipped unless --force. Page markers are written as <!-- page N --> where
the backend allows it.
"""
from __future__ import annotations

import argparse
import statistics
import sys
from pathlib import Path

from notes import ROOT


def have(module: str) -> bool:
    try:
        __import__(module)
        return True
    except ImportError:
        return False


def convert_marker(pdf: Path) -> str:
    from marker.converters.pdf import PdfConverter
    from marker.models import create_model_dict
    from marker.output import text_from_rendered

    global _MARKER
    if "_MARKER" not in globals():
        _MARKER = PdfConverter(artifact_dict=create_model_dict(),
                               config={"paginate_output": True})
    text, _, _ = text_from_rendered(_MARKER(str(pdf)))
    return text


def convert_docling(pdf: Path) -> str:
    from docling.document_converter import DocumentConverter

    global _DOCLING
    if "_DOCLING" not in globals():
        _DOCLING = DocumentConverter()
    doc = _DOCLING.convert(str(pdf)).document
    return doc.export_to_markdown(page_break_placeholder="\n\n<!-- page break -->\n\n")


def convert_pymupdf(pdf: Path) -> str:
    if have("pymupdf4llm"):
        import pymupdf4llm

        pages = pymupdf4llm.to_markdown(str(pdf), page_chunks=True)
        return "\n\n".join(f"<!-- page {i} -->\n\n{p['text']}" for i, p in enumerate(pages, 1))

    import pymupdf

    doc = pymupdf.open(pdf)
    # Body font size = most common span size; larger, short lines become headings.
    sizes = [round(s["size"], 1) for page in doc for b in page.get_text("dict")["blocks"]
             for line in b.get("lines", []) for s in line["spans"] if s["text"].strip()]
    body = statistics.mode(sizes) if sizes else 10.0
    out = []
    for i, page in enumerate(doc, 1):
        out.append(f"<!-- page {i} -->")
        for b in page.get_text("dict")["blocks"]:
            lines = b.get("lines", [])
            text = " ".join("".join(s["text"] for s in ln["spans"]) for ln in lines).strip()
            if not text:
                continue
            size = max(s["size"] for ln in lines for s in ln["spans"])
            bold = all("Bold" in s["font"] or s["flags"] & 16
                       for ln in lines for s in ln["spans"] if s["text"].strip())
            if len(text) < 120 and (size > body * 1.15 or (bold and size >= body)):
                out.append(("# " if size > body * 1.6 else "## ") + text)
            else:
                out.append(text)
    return "\n\n".join(out)


def pick_backend(name: str):
    backends = {"marker": ("marker", convert_marker),
                "docling": ("docling", convert_docling),
                "pymupdf": ("pymupdf", convert_pymupdf)}
    if name != "auto":
        mod, fn = backends[name]
        if not have(mod):
            sys.exit(f"backend '{name}' requested but module '{mod}' is not installed")
        return name, fn
    for key in ("marker", "docling", "pymupdf"):
        mod, fn = backends[key]
        if have(mod):
            return key, fn
    sys.exit("no PDF backend installed (pip install pymupdf)")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("citekeys", nargs="*", help="only convert these (default: all PDFs)")
    ap.add_argument("--backend", default="auto", choices=["auto", "marker", "docling", "pymupdf"])
    ap.add_argument("--force", action="store_true", help="re-convert existing files")
    args = ap.parse_args()

    pdfs = sorted((ROOT / "pdf").glob("*.pdf"))
    if args.citekeys:
        pdfs = [p for p in pdfs if p.stem in args.citekeys]
    if not pdfs:
        print("no PDFs to convert in pdf/")
        return

    name, fn = pick_backend(args.backend)
    print(f"backend: {name}")
    done = skipped = failed = 0
    for pdf in pdfs:
        out = ROOT / "fulltext" / f"{pdf.stem}.md"
        if out.exists() and not args.force:
            skipped += 1
            continue
        try:
            md = fn(pdf)
        except Exception as e:  # keep going; report at the end
            print(f"FAIL {pdf.name}: {e}")
            failed += 1
            continue
        header = f"<!-- source: pdf/{pdf.name} | converter: {name} -->\n\n"
        out.write_text(header + md, encoding="utf-8")
        print(f"ok   {pdf.name} -> fulltext/{out.name} ({len(md):,} chars)")
        done += 1
    print(f"converted {done}, skipped {skipped} (already done), failed {failed}")


if __name__ == "__main__":
    main()
