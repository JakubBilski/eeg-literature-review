---
name: read-paper
description: Read one paper end-to-end and integrate it into the Obsidian vault — fetch & convert full text, write papers/<citekey>.md, update concept/topic/hub notes in both directions, then present a summary with links to already-read papers and concepts. Use when the human asks to read, summarize or add a specific paper.
argument-hint: <citekey | DOI | arXiv ID>
---

# read-paper

## 1. Get the full text
- If the paper isn't in `data/screening.csv`, add it: `scripts/discover.py lookup <id> --add --source "<why>" --decision include --reason "…"`.
- If `fulltext/<citekey>.md` is missing: `discover.py pdf <citekey>` then `convert.py <citekey>`. If it ends `needs_manual`, tell the human and stop, or write an abstract-only note with `read_depth: abstract` only if they agree.

## 2. Read
- Read the **whole** full text (in chunks with offset/limit for long files). PDF conversions have `<!-- page N -->` markers → cite `(p. N)`; JATS conversions have numbered sections → cite `(§N)`; tables `(Table N)`.
- **Tables/figures embedded as images** (caption present, numbers missing — common in IEEE PDFs): `scripts/page_image.py <citekey> <page> [--top 0.6]`, read the PNG, and append a transcription to `fulltext/<citekey>.md` under `## Tables transcribed from page images (p. N)` so the numbers are searchable.
- JATS conversions from Europe PMC may lack section numbers → cite by heading, e.g. `(§Validation)`, and say so once in the note.
- Skim the reference list for papers already in the vault (grep citekey titles) and for important uncaptured ones → `interests.md` *Reading queue*.

## 3. Write `papers/<citekey>.md` from `templates/paper.md`
- Frontmatter complete and machine-readable; `read_depth: full`; `concepts:` = plain slugs.
- Every number/claim has a location. **Reported** in the main sections; interpretation only in *Assessment 🤖* (each bullet 🤖).
- ≤ ~150 lines. Depth goes to concept / topic notes.
- For reviews and device papers, frontmatter fields like `model_type`, `main_result` may be `""` — put the key takeaways in *Results* instead.

## 4. Connect (both directions)
- **Concepts:** for each concept the paper materially uses or discusses — existing note → add the paper under *Papers* with one line on *how*; new concept → create from `templates/concept.md` only if it is likely to recur (otherwise mention it in the paper note only). Prefer few, well-maintained concepts.
- **Related papers:** link vault papers it builds on / competes with / cites, one line each — and add the reverse link in those notes' *Related papers*.
- **Hubs/topics:** add the paper to the relevant `topics/q<N>-*.md` hub(s) (*Sources* plus a claim under *Current answer* if it contributes one). Update a synthesis topic note if the paper changes a comparison.
- `index.md` → *Recently read* (newest first).

## 5. Check
- `scripts/check_links.py` and `scripts/export_comparison.py`; fix what they report for this paper.

## 6. Present to the human
- TL;DR (2 lines) + 3–6 key findings with locations.
- **Links:** papers already in the vault it relates to (and how), concepts it touches, hubs it feeds.
- What it leaves open / what to read next.
- Then the human usually asks questions — handle them per *Knowledge capture* in CLAUDE.md (file answers as you go).
