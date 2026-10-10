"""Convert pdf/*.pdf and pdf/*.xml (JATS, from Europe PMC) -> fulltext/<citekey>.md.

Files must be named <citekey>.pdf / <citekey>.xml. JATS XML is converted directly
(sections, tables, figure captions, references; no page numbers — cite by section).
For PDFs: Backend preference: marker > docling > pymupdf
(pymupdf4llm is used inside the pymupdf fallback if installed). Already converted
files are skipped unless --force. Page markers are written as <!-- page N --> where
the backend allows it.
"""
from __future__ import annotations

import argparse
import re
import statistics
import sys
import xml.etree.ElementTree as ET
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


def convert_jats(xml: Path) -> str:
    def text(el) -> str:
        return " ".join("".join(el.itertext()).split()) if el is not None else ""

    def local(tag: str) -> str:
        return tag.rsplit("}", 1)[-1]

    def table_md(tw) -> list[str]:
        out = [f"**{text(tw.find('label'))}** {text(tw.find('caption'))}".strip()]
        for tr_i, tr in enumerate(tw.iter("tr")):
            cells = [text(c).replace("|", "/") for c in tr if local(c.tag) in ("td", "th")]
            out.append("| " + " | ".join(cells) + " |")
            if tr_i == 0:
                out.append("|" + "---|" * len(cells))
        return ["\n".join(out)]

    def walk(el, depth: int) -> list[str]:
        out = []
        for ch in el:
            tag = local(ch.tag)
            if tag == "sec":
                label, title = text(ch.find("label")), text(ch.find("title"))
                out.append("#" * min(depth, 6) + f" {label} {title}".rstrip())
                out += walk(ch, depth + 1)
            elif tag == "p":
                out.append(text(ch))
            elif tag == "list":
                out.append("\n".join(f"- {text(li)}" for li in ch if local(li.tag) == "list-item"))
            elif tag == "table-wrap":
                out += table_md(ch)
            elif tag == "fig":
                out.append(f"*{text(ch.find('label'))}* {text(ch.find('caption'))}")
            elif tag in ("boxed-text", "disp-quote"):
                out += walk(ch, depth)
        return out

    root = ET.parse(xml).getroot()
    meta = root.find(".//article-meta")
    parts = [f"# {text(meta.find('.//article-title'))}"]
    for ab in meta.findall("abstract"):
        parts.append("## Abstract")
        parts += walk(ab, 3) or [text(ab)]
    if (body := root.find("body")) is not None:
        parts += walk(body, 2)
    if (floats := root.find("floats-group")) is not None:  # float tables/figs live outside <body>
        parts.append("## Floating tables and figures")
        parts += walk(floats, 3)
    if (refs := root.find(".//ref-list")) is not None:
        parts.append("## References")
        parts.append("\n".join(f"{i}. {text(r)}" for i, r in enumerate(refs.iter("ref"), 1)))
    return "\n\n".join(p for p in parts if p.strip())


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

    files = sorted((ROOT / "pdf").glob("*.pdf")) + sorted((ROOT / "pdf").glob("*.xml"))
    if args.citekeys:
        files = [p for p in files if p.stem in args.citekeys]
    if not files:
        print("nothing to convert in pdf/")
        return

    pdf_name, pdf_fn = (None, None)
    done = skipped = failed = 0
    for pdf in files:
        out = ROOT / "fulltext" / f"{pdf.stem}.md"
        if out.exists() and not args.force:
            skipped += 1
            continue
        if pdf.suffix == ".xml":
            name, fn = "jats", convert_jats
        else:
            if pdf_fn is None:
                pdf_name, pdf_fn = pick_backend(args.backend)
            name, fn = pdf_name, pdf_fn
        try:
            md = fn(pdf)
        except Exception as e:  # keep going; report at the end
            print(f"FAIL {pdf.name}: {e}")
            failed += 1
            continue
        header = f"<!-- source: pdf/{pdf.name} | converter: {name} -->\n\n"
        out.write_text(header + md, encoding="utf-8")
        print(f"ok   {pdf.name} -> fulltext/{out.name} [{name}] ({len(md):,} chars)")
        done += 1
    print(f"converted {done}, skipped {skipped} (already done), failed {failed}")


if __name__ == "__main__":
    main()
