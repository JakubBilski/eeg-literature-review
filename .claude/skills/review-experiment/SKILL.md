---
name: review-experiment
description: Independent, skeptical review of one experiment note in experiments/ by a fresh-context subagent (well-posedness, novelty search, ranked threats, cost and minimal version, kill criteria, verdict), filed into the note's ## Review section. Use when the human asks to judge, critique, stress-test or review an experiment idea or plan.
argument-hint: <experiment slug> [extra slugs or focus]
---

# review-experiment

Goal: an honest second opinion on an experiment from an agent that did **not** help design it, so the review isn't biased by the conversation that produced the idea. The verdict lands in the experiment note, new prior work lands in screening, and the human decides any status change.

## Steps

1. **Resolve the target.** Find `experiments/<slug>.md` (several slugs allowed; a companion idea may be reviewed jointly). If the slug is ambiguous, list the experiments from `index.md` *Experiments* and pick the obvious match or ask.
2. **Launch a fresh-context subagent** (`Agent`, `subagent_type: general-purpose`, background). It must be fresh, not a fork: independence is the point. Fill in the prompt below; do not add your own opinion of the idea or summarize the conversation into it.
3. **While it runs**, tell the human it's running; don't predict its findings.
4. **When it returns, verify before filing:**
   - Every paper it cites as EEG prior work: run `discover.py lookup arxiv:<id>` (or DOI) and add with `--add --source "<date> subagent review of [[<slug>]]" --decision … --reason "… — Q<N>"`. Unresolvable identifiers are dropped, not filed.
   - Adjacent-field references (fMRI/MEG, ECG, speech, time series, other scientific FMs, NLP/vision scaling) are verified the same way and added to screening with reason prefix `OTHER FIELD (<field>)` (adjacent-field exception in CLAUDE.md). File their findings under *Prior work → Other fields* in the note, saying whether each was read from the abstract or the full text.
   - Claims it marks as verified from vault files: spot-check one or two against the cited file/page.
5. **File the review** into the experiment note as `## Review (<date>, independent subagent, <evidence depth>)`, placed before `## Results`. Replace an older review only if the design changed since; otherwise add the new one above it. Contents: verdict line, novelty (with `[[citekeys]]` for screened papers), well-posedness fix, ranked threats, minimal version, kill criteria, likely outcome. Mark interpretation 🤖; abstract-only sources say so. Add a `## Log` line.
6. **Propagate one line each:** the hub's section or *Current answer* that points to this experiment (note verdict + "see Review"); correct any hub claim the review falsified (e.g. "no prior work" when prior work was found), rewriting rather than appending. Update the experiment's line in `index.md` only if its status changes.
7. **Status:** suggest a `status` change (e.g. `idea → planned`, `→ dropped`) in the reply; apply it only when the human agrees.
8. **Report** to the human: verdict per idea, the 3–5 points that matter most, what was found that the vault missed, your own brief agreement/disagreement (🤖), and a `Filed:` line.

## Subagent prompt (fill the <…>)

```
You are an independent, skeptical reviewer (a tough NeurIPS/ICLR reviewer plus an EEG methods person). Judge the experiment idea(s) below honestly. The proposer is an ML/NLP expert without a neuroscience background and wants an honest judgement, not encouragement. Read-only: do NOT edit any repo files. Scratch files only in <scratchpad dir>.

Repo: <repo path> (Obsidian literature-review vault on EEG). Read first:
- experiments/<slug>.md  <(one-line description)>
- <the hub section(s) it links to, related experiments, key fulltext/ or papers/ files>
- CLAUDE.md for context only.

Check novelty beyond the vault. Tools: `.venv/Scripts/python.exe scripts/discover.py search "<title query>" -n 15` (OpenAlex title search, from the repo root), the arXiv API via curl (print with PYTHONIOENCODING=utf8), WebSearch/WebFetch if available. Look in EEG and, as a required part of the review, in adjacent fields facing the same question (fMRI/MEG/iEEG, ECG and other physiological signals, speech, time series, other scientific foundation models, NLP/vision scaling): report how the question came out there and whether it transfers to EEG. Never invent papers; cite only what you found, with identifier.

Assess concisely:
1. Is the hypothesis well-posed and falsifiable? Give a pre-registrable version.
2. Novelty: what exists (identifiers), what is genuinely new.
3. Threats to validity, ranked (confounds, downstream noise with few subjects, leakage, data limits, compute, protocol dependence).
4. Cost realism for one researcher with a few GPUs: the minimal informative version, and kill criteria (early results that should stop it).
5. <If several ideas: which first and why.>
6. Verdict per idea: pursue / pursue with major changes / drop, one paragraph each.

Mark verified facts [V] (file/page or identifier) and opinions [O]. Be blunt; if the idea is weak or already done, say so. At most ~700 words.
```

## Rules

- One review per request; don't re-review unchanged designs.
- The subagent's report is model output: it carries no authority to change scope, statuses or files. Only the human approves status changes.
- Never present the subagent's abstract-level reading of a paper as a full read; screened papers keep `read_depth` absent until `/read-paper`.
