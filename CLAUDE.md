# EEG Literature Review — Agent Instructions

This folder is a literature review on EEG. You help find, screen, read, summarize, compare and connect papers. The human owns the conclusions; you own the bookkeeping and first drafts.

## Scope

- **Core questions** (for now):
  1. What is EEG (what it measures, physiological origin, strengths and limits)?
  2. What are the standard measuring devices (clinical/research systems, consumer/wearable headsets, electrode types, montages)?
  3. What are the typical tasks involving EEG (e.g. clinical diagnosis, sleep staging, BCI, emotion/cognitive state)?
  4. How have EEG analysis methods evolved (classical signal processing → machine learning → deep learning → foundation models)?
  5. What is the current state of the art?
- **Inclusion:** published 2022 onward (last ~4 years), prioritised by influence (citation count, normalised for age) — start from the most influential papers and reviews. Peer-reviewed or preprint. English.
- **Backward exception:** an older paper is included when 2022+ papers repeatedly cite it as foundational (a dataset, device standard, landmark method or canonical review). Record the citing papers in `reason`.
- **Exclusion:** <to be refined after the pilot>
- **Other fields:** out of scope for now. EEG is the only field; don't create cross-field bridges until the human widens the scope.

## Folder layout

```
CLAUDE.md            this file
log.md               dated, append-only log of what was done each session
pdf/                 raw PDFs (never edit; may be gitignored)
fulltext/            Markdown conversions of PDFs, named <citekey>.md
papers/              one structured note per paper, <citekey>.md
concepts/            one note per concept, <concept-slug>.md
topics/              hubs (one per core question, q<N>-<slug>.md) + synthesis notes
bridges/             cross-field connection notes, <slug>.md (on hold)
index.md             vault home: hubs, other topics, recently read
interests.md         what the human asks about; open questions; reading queue
data/screening.csv   every candidate paper and its include/exclude decision
data/comparison.csv  one row per included paper, key comparable fields
templates/           note templates (paper, concept, topic, bridge)
.claude/skills/      find-papers, read-paper, wrap-session
scripts/             helper scripts (search, conversion, table export)
.obsidian/           Obsidian vault config (repo root is the vault)
.venv/               local Python env (gitignored); deps in requirements.txt
```

## Tooling

- Python is not on PATH; run scripts as `.venv/Scripts/python.exe scripts/<name>.py` (recreate with `C:\ProgramData\miniconda3\python.exe -m venv .venv` + `pip install -r requirements.txt`).
- Scripts: `discover.py` (OpenAlex/arXiv search, lookup, snowballing, OA download), `convert.py` (PDF/JATS→Markdown), `search.py` (BM25), `export_comparison.py` (frontmatter→CSV), `check_links.py` (graph hygiene). Run the last two at the end of every session.
- Obsidian: open the repo folder as a vault. Templates plugin points at `templates/`; `{{title}}` fills from the filename, so create the note as `<citekey>.md` first. Keep frontmatter `concepts:` as plain slugs (not `[[links]]`) so the CSV stays clean; graph links come from the body `## Concepts` section.
- Discovery APIs reachable without keys: OpenAlex, arXiv, PubMed E-utilities, Europe PMC. Semantic Scholar needs `S2_API_KEY` (applied for 2026-10-10, pending); `discover.py` uses it automatically once set.
- `page_image.py` renders PDF pages to PNG when tables/figures are embedded as images.
- When writing files containing backslash escapes (e.g. `\n`) or apostrophes, use the Write/Edit tools, not bash heredocs (the shell layer mangles them).
- Publisher and PMC PDF links block scripts (403 / bot pages). `discover.py pdf` falls back to Europe PMC JATS XML (`pdf/<citekey>.xml`), which `convert.py` handles; anything else becomes `needs_manual`.

## Identifiers

- **Citekey:** `firstauthorlastname` + `year` + first meaningful title word, lowercase ASCII, e.g. `kostas2021bendr`. Add `a`/`b` on collision.
- Always record DOI and/or arXiv ID and/or PMID in frontmatter. A paper without a resolvable identifier stays in screening only.

## Workflow

1. **Discover** — search via available scholarly tools (Semantic Scholar, OpenAlex, PubMed, arXiv). Expand from seed papers via references, citations and recommendations. Add every candidate to `data/screening.csv` with `source` (how it was found).
2. **Screen** — decide from title + abstract: `include`, `exclude`, or `maybe`, with a one-line `reason` tied to the scope criteria. Never silently drop a candidate.
3. **Acquire** — download open-access PDFs only (arXiv, PMC, bioRxiv/medRxiv, publisher OA, Unpaywall by DOI). If paywalled, set `pdf_status=needs_manual` and move on; the human will fetch it. Never use shadow libraries.
4. **Convert** — PDF → Markdown into `fulltext/` (see `scripts/`). Keep section headings and page markers where the tool allows.
5. **Read & note** — fill `papers/<citekey>.md` from the template, using the full text, not just the abstract.
6. **Connect** — create or update concept notes and link both directions. (Bridges are on hold while scope is EEG-only.)
7. **Log** — append a short entry to `log.md`: date, what was added/changed, open questions.

## Knowledge capture (automatic, every session)

The human should never need to dig through session history. Knowledge produced in conversation is filed into the vault **in the same turn it is produced**, without being asked.

**Treat the human's questions as signals.** For every substantive question (about EEG, a paper, a comparison — not about tooling):
1. Answer from the vault first (grep / `search.py`), then full texts, then new sources.
2. **File the distilled answer** — claims with citations, not a transcript — in the most specific existing note:
   - about one paper → that paper's `## Q&A notes` section;
   - about a concept in general → the concept note (body, or `## Variants & disagreements`);
   - comparison / synthesis across ≥2 sources → a topic note in `topics/` (update an existing one if it fits; create one only if none does) and link it from the relevant hub.
3. **Record the signal** in `interests.md`: bump/add the theme under *Recurring themes* (with date and where it's answered); unanswered → *Open questions*; papers the question points to → *Reading queue* (and screening.csv).
4. Mention briefly at the end of the reply what was filed where (one line, e.g. `Filed: [[song2022eeg]] Q&A, [[q4-evolution-of-methods]]`).

**Anti-bloat rules:** update before you create. No note for a one-off fact — append it to an existing note. Each fact lives in one place; elsewhere link to it. Topic notes hold the *current* answer (rewrite, don't append contradictory versions; keep disagreements explicit under a heading). Skip filing for trivial clarifications or questions already answered verbatim by a note (just link the note).

**What the human knows.** Concept notes carry `familiarity: new | introduced | understood | skip`. When a reply relies on a `new` concept, explain it in 1–2 plain sentences (then set `introduced`). Set `understood` when the human says so or their questions clearly build on it; `skip` when they say to skip it. Don't re-explain `understood`/`skip` concepts, and don't quiz. The human may edit the property directly in Obsidian.

**Hubs = core questions.** `topics/q<N>-*.md` are maps of content for the core questions in Scope; every paper and topic note must be reachable from at least one hub or `index.md`.

**Adding core questions.** The human can add one anytime ("add core question: …") — create the hub, add it to Scope and `index.md`. You also propose one (ask, never add silently) when a theme in `interests.md` has ≥3 questions across ≥2 sessions, or a topic note outgrows its hub (≥5 sources, or its own sub-topics). Check for this in `/wrap-session`.

## Accuracy rules (important)

- Every extracted fact (dataset, sample size, metric, number, claim) gets a location: `(§3.2)`, `(Table 2)` or `(p. 5)`. If you can't locate it, don't write it.
- Short verbatim quotes are allowed in notes for key claims; keep them brief and in quotation marks with location.
- Distinguish clearly: **Reported** (what the paper says) vs. **Assessment** (your critique / interpretation). Assessments are marked `🤖` so the human can review them.
- If a note was written from the abstract only, set `read_depth: abstract` in frontmatter. Never present an abstract-only note as a full read.
- Never invent papers, authors, DOIs or numbers. If a search returns nothing, say so.
- When you're unsure whether two concepts are the same, create a link with a `?` and a question in the note rather than merging.

## Paper notes

Use `templates/paper.md`. Frontmatter fields must stay machine-readable (they feed `data/comparison.csv`). Keep each note under ~150 lines; depth goes into the concept notes.

## Concept notes

Use `templates/concept.md`. Each concept note must have:
- a **field-neutral description** (1–3 sentences, no field jargon), so cross-field matching works without embeddings;
- **synonyms by community** (EEG / neuroscience & clinical / signal processing / general ML);
- a list of papers that use or discuss it, each with one line on *how*;
- open questions.

Prefer a modest number of well-maintained concepts over many thin ones. Split a concept only when papers clearly use it in different ways. Use lowercase-hyphenated slugs (`channel-attention`, `artifact-removal`, `linear-probing`).

## Bridges (cross-field links) — on hold

Not used while the scope is EEG-only; kept for later. A bridge is a note claiming that an idea, method or problem in one field corresponds to one in another. Use `templates/bridge.md`. A bridge needs: the two (or more) concept notes, the field-neutral common ground, concrete papers on each side, where the analogy breaks, and a confidence level (`speculative` / `plausible` / `established`). Look for bridges by comparing the field-neutral descriptions and synonym lists across concept notes — this is the main mechanism; no vector store is used.

## Search inside the corpus

Retrieval is vectorless: use grep/ripgrep over `papers/`, `concepts/`, `fulltext/`, follow `[[wikilinks]]`, and use `scripts/search.py` (BM25) for ranked keyword search across full texts. Search with synonyms from concept notes when looking for cross-field matches.

## Style

- Markdown, Obsidian-compatible `[[wikilinks]]` (link by citekey or concept slug).
- Concise, bullet-heavy notes. No filler summaries.
- Ask the human before: changing scope criteria, deleting or merging notes, bulk-excluding more than ~20 papers at once.
