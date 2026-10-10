"""Rebuild data/comparison.csv from the frontmatter of papers/*.md.

List fields are joined with "; ". Run after adding or editing paper notes.
"""
from __future__ import annotations

import argparse
import csv

from notes import ROOT, note_paths, read_note

FIELDS = ["citekey", "title", "authors", "year", "venue", "doi", "arxiv", "pmid",
          "field", "paper_type", "task", "datasets", "n_subjects", "n_channels", "model_type",
          "eval_protocol", "main_metric", "main_result", "code_available",
          "read_depth", "concepts"]


def cell(value) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return "; ".join(str(v) for v in value)
    return str(value)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default=str(ROOT / "data" / "comparison.csv"))
    args = ap.parse_args()

    rows, warnings = [], []
    for path in note_paths("papers"):
        meta, _ = read_note(path)
        if meta.get("citekey") != path.stem:
            warnings.append(f"{path.name}: citekey '{meta.get('citekey')}' != filename")
        missing = [f for f in FIELDS if f not in meta]
        if missing:
            warnings.append(f"{path.name}: missing fields {missing}")
        rows.append({f: cell(meta.get(f)) for f in FIELDS})

    with open(args.out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(sorted(rows, key=lambda r: r["citekey"]))
    print(f"wrote {len(rows)} rows -> {args.out}")
    for msg in warnings:
        print("warn:", msg)


if __name__ == "__main__":
    main()
