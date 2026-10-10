"""Check the vault's link graph.

Reports:
  - broken wikilinks (no note and not a screened citekey), incl. frontmatter concept slugs
  - papers with no concepts
  - concepts with fewer than 2 papers
  - non-reciprocal paper <-> concept links
  - papers / topics not reachable from index.md via wikilinks (hub rule)
Exit code 1 if any issue is found and --strict is given.
"""
from __future__ import annotations

import argparse
import sys
from collections import defaultdict

from notes import ROOT, note_paths, read_note, wikilinks


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--strict", action="store_true", help="exit 1 if issues are found")
    args = ap.parse_args()

    # Every Markdown note in the vault is a valid link target (except tooling dirs).
    skip = {".venv", "pdf", ".obsidian", ".git", "templates"}
    targets = {p.stem for p in ROOT.rglob("*.md")
               if not skip.intersection(p.relative_to(ROOT).parts)}
    papers = {p.stem: p for p in note_paths("papers")}
    # Citekeys in screening.csv without a note yet are "unread" links, not broken ones.
    import csv
    with open(ROOT / "data" / "screening.csv", newline="", encoding="utf-8") as fh:
        screened = {r["citekey"] for r in csv.DictReader(fh)}
    unread_links: set[str] = set()
    concepts = {p.stem: p for p in note_paths("concepts")}

    broken: list[str] = []
    paper_to_concepts: dict[str, set[str]] = {}
    concept_to_papers: dict[str, set[str]] = {}

    for path in note_paths():
        meta, body = read_note(path)
        links = wikilinks(body)
        rel = path.relative_to(ROOT).as_posix()
        for t in links:
            if t in targets:
                continue
            if t in screened:
                unread_links.add(t)
            else:
                broken.append(f"{rel} -> [[{t}]]")
        if path.stem in papers:
            fm = {str(c) for c in (meta.get("concepts") or [])}
            for c in fm - set(concepts):
                broken.append(f"{rel} frontmatter concept '{c}' has no concepts/{c}.md")
            paper_to_concepts[path.stem] = (fm | set(links)) & set(concepts)
        elif path.stem in concepts:
            concept_to_papers[path.stem] = set(links) & set(papers)

    inbound: dict[str, set[str]] = defaultdict(set)
    for p, cs in paper_to_concepts.items():
        for c in cs:
            inbound[c].add(p)

    no_concepts = sorted(p for p, cs in paper_to_concepts.items() if not cs)
    thin = sorted((c, len(inbound[c] | concept_to_papers.get(c, set()))) for c in concepts
                  if len(inbound[c] | concept_to_papers.get(c, set())) < 2)
    nonrecip = []
    for p, cs in paper_to_concepts.items():
        for c in cs:
            if p not in concept_to_papers.get(c, set()):
                nonrecip.append(f"[[{p}]] -> [[{c}]] but concept does not list the paper")
    for c, ps in concept_to_papers.items():
        for p in ps:
            if c not in paper_to_concepts.get(p, set()):
                nonrecip.append(f"[[{c}]] -> [[{p}]] but paper does not list the concept")

    # Reachability from index.md (follow wikilinks through notes in the vault).
    by_stem = {p.stem: p for p in note_paths()}
    by_stem["index"] = ROOT / "index.md"
    seen, stack = set(), ["index"]
    while stack:
        cur = stack.pop()
        if cur in seen or cur not in by_stem:
            continue
        seen.add(cur)
        meta, body = read_note(by_stem[cur])
        stack.extend(wikilinks(body))
    unreachable = sorted(p.relative_to(ROOT).as_posix() for p in note_paths("papers", "topics")
                         if p.stem not in seen)

    sections = [("Broken wikilinks", broken),
                ("Papers with no concepts", no_concepts),
                ("Concepts with < 2 papers", [f"{c} ({n})" for c, n in thin]),
                ("Non-reciprocal paper<->concept links", sorted(nonrecip)),
                ("Not reachable from index.md", unreachable)]
    print(f"Links to screened-but-unread papers (OK): {', '.join(sorted(unread_links)) or '-'}\n")
    print(f"{len(papers)} papers, {len(concepts)} concepts, "
          f"{len(note_paths('bridges'))} bridges\n")
    total = 0
    for title, items in sections:
        print(f"## {title}: {len(items)}")
        for it in items:
            print(f"  - {it}")
        total += len(items)
    if args.strict and total:
        sys.exit(1)


if __name__ == "__main__":
    main()
