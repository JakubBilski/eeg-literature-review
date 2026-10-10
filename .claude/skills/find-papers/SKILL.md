---
name: find-papers
description: Search for EEG papers on a topic (OpenAlex/arXiv, Semantic Scholar when keyed), rank by influence, screen them and add to data/screening.csv. Use when the human asks to find, search for, or expand literature on a topic, or when a question points to papers not yet in the vault.
argument-hint: <topic or seed citekey/DOI>
---

# find-papers

Goal: a short, ranked, screened candidate list for a topic, added to `data/screening.csv`, with the top pick ready for `/read-paper`.

Tool: `.venv/Scripts/python.exe scripts/discover.py` (`search`, `lookup`, `refs`, `cites`, `pdf`; see `--help`).

## Steps

1. **Check the vault first.** `grep -ri` / `scripts/search.py` over `papers/`, `topics/`, `concepts/`, and `data/screening.csv` for the topic. Report what's already there before searching outward.
2. **Search.** Run 2–4 `discover.py search` queries with synonyms (take them from concept notes' *Synonyms by community*). Defaults follow Scope: 2022+, sorted by citations.
   - Query syntax is OpenAlex `title.search` (boolean, parentheses): `"(EEG OR electroencephalography) AND (sleep OR staging)"`. Always require an EEG term — plain full-text search returns mostly off-topic papers.
3. **Snowball** from the 1–3 most relevant hits or existing seeds: `cites <id>` (forward, recent work) and `refs <id>` (backward, foundations). An older paper qualifies only via the Scope backward exception — name the citing papers in `reason`.
4. **Judge influence with care** (lessons from this project):
   - Use citations/year (`/yr` column), not raw counts.
   - OpenAlex badly **undercounts ML-conference papers** (ICLR/NeurIPS/arXiv: e.g. LaBraM 19 vs EEGNet 4,784). Don't drop a foundation-model or ML-venue paper for low counts; cross-check with Semantic Scholar if `S2_API_KEY` is set (shown as `[S2 n]`).
   - Ignore citation outliers that are off-topic (spam / gamed records exist, e.g. a 13,887-citation "Aion Framework" hit).
5. **Screen** from title + abstract against Scope: `include` / `exclude` / `maybe`, one-line `reason` naming the criterion and the core question(s) it serves (`— Q3`). Add with `--add --source "search: <query>" --decision … --reason …` (or edit the CSV for per-row reasons). Never silently drop a candidate. Ask before bulk-excluding >20.
6. **Acquire** for `include` rows: `discover.py pdf <citekeys>` then `convert.py`. Paywalled/blocked → `needs_manual`; list them for the human.
7. **Report** to the human: a table (rank, citekey, year, cites/yr, OA, one-line why), what's already in the vault, what needs manual download, and a recommended paper to read next (and why, tied to `interests.md` / core questions).
8. Note the search in `interests.md` (*Reading queue*) if it came from the human's question.
