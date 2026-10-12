---
slug: pretext-downstream-scaling-sweep
status: idea
questions: [q9, q7]
concepts: [self-supervised-pretraining, evaluation-protocols]
datasets: [tueg, tuab, tuev, isruc, moabb-mi]
scripts: []
figures: []
cost: high            # several pretraining runs (sizes × data amounts)
origin: 2026-10-11, "why do FMs get better at pretext tasks but worse downstream?" ([[q9-pretraining-objectives-and-scale]])
updated: 2026-10-12
---

# pretext-downstream-scaling-sweep

## Hypothesis
🤖 "Better pretext, worse downstream" is mostly an artifact of comparing loss values across different target definitions, and of cross-model confounding. Within one fixed model family and target, held-out pretext loss should track downstream quality for a while and then decouple, with the decoupling coming from objective misalignment, not from overfitting during pretraining. Ranked candidate causes → [[q9-pretraining-objectives-and-scale]] *Why pretext gains don't transfer downstream*.
- **Competing hypothesis (human, 2026-10-12):** non-scaling of FM size is overfitting from repeated passes over too few independent samples, as with ViT on ImageNet-1k. Under it, larger models win at matched examples seen before repetition, and lose after. Track train vs held-out pretext loss per size *per pass* to separate it from misalignment. Supervised version → [[subject-diversity-gap]] *Repetitions (H5)*.

## Design
- **Fixed:** one backbone family, preprocessing, masking; raw-EEG input for every arm.
- **Target T as an axis (added 2026-10-12):** raw-patch MSE, band power ([[xie2026specbram]]), band power + cross-channel phase ([[cross-channel-phase-target]]), clustered covariance ([[covariance-pseudo-labels]]), latent (EMA encoder). Goal: per-T scaling curves of downstream vs compute, and where they cross. Reasoning → [[q9-pretraining-objectives-and-scale]] *Scaling laws per target T?*
- **Sweep:** model size (≈1M, 5M, 25M, 100M) × pretraining hours (≈500, 2k, 9k of TUEG; or REVE-scale 600–30,000 h as in [[chen2026benchmarking]] p. 13), with distinct-subject count as a separate axis where possible (cheap supervised version first: [[subject-diversity-gap]]).
- **Fit per T:** L_T(N, D) = E_T + A/N^α + B/D^β for pretext loss; downstream CE (bits, averaged over tasks) vs compute. Don't compare pretext losses across T.
- **Cost note:** 5 targets × 4 sizes × 3 data amounts = 60 pretraining runs; start with 2 targets × the smallest 3 sizes.
- **Measure at every checkpoint:**
  - held-out pretext loss on TUEG subjects not used in pretraining, *and* on other corpora (sleep PSG, a BCI set): in-distribution vs out-of-distribution pretext loss;
  - layer-wise linear probes + fine-tunes on TUAB, TUEV, ISRUC and one MI set, with enough held-out subjects to resolve the differences (beyond the Nemenyi CD in [[liu2026eeg]] p. 72).
- **Diagnostics:** in-distribution vs OOD pretext loss gap (pretraining overfitting); which layer peaks for which task (objective misalignment); fine-tune gains vs downstream subject count (fine-tuning overfitting).

## What each outcome would mean
- Pretext loss and probes improve together within an arm → the field's "inversion" came from cross-target / cross-model comparisons (explanations 1 and 5).
- Pretext loss keeps falling while probes plateau or drop, with no OOD gap → misalignment (explanation 2).
- OOD pretext loss rises while in-distribution falls → pretraining overfits the corpus.
- Large models lose only on small downstream sets → fine-tuning overfitting (explanation 3).

## Prior work
- None in the vault does this sweep. Closest: LaBraM's data-amount curve ([[jiang2024large]] §3.6 Fig. 5), field-level channel-hours vs scores ([[kuruppu2026eeg]] Fig. 3, §5.1), the size–rank analysis in [[liu2026eeg]] (pp. 21–22), and HuBERT-ECG's sizes ([[coppola2024hubert]] pp. 5–6).

## Review (2026-10-12, independent subagent, abstracts + arXiv search)
**Verdict: pursue with major changes.** 🤖 throughout except identifiers.
- **Novelty:** no study in any modality fits and compares scaling curves *per pretext target* (subagent search). Partial prior work: BrainGPT [[yue2024braingpt]] (scaling to 1.1B, one autoregressive objective), [[oliveira2026scaling]] (power laws for *supervised* EEG decoding over subjects/trials), [[panchavati2026laya]] (LeJEPA vs matched MAE, single scale), [[dou2026taming]] (objective ablations), [[xiong2025eeg]] (scaling departs from usual laws). Outside EEG: for one fixed target, MIM pretraining loss is "a good indicator" of fine-tuning (arXiv 2206.04664), which largely pre-answers the "why decoupling" arm; masked-reconstruction scaling breaks under limited data (arXiv 2602.15253).
- **Not well-posed yet:** "scales best" = steeper exponent, lower asymptote, or win at budget? 3–4 sizes × 3 data levels can't identify exponents. Pre-register: T1 beats T2 by more than the seed CI at budget C1, and the order holds/flips at ~30×C1.
- **Threats, ranked:** (1) target differences ~1–3 points vs downstream noise → ≥3 seeds per cell; (2) per-T hyperparameter tuning (VQ/EMA collapse; tokenizer training counts as compute); (3) data ceiling: ~15k TUEG subjects, ~1.5 decades of data; (4) crossovers depend on budget *and* probe-vs-fine-tune protocol.
- **Minimal version:** 3 targets (raw MSE, band power, latent) × 3 sizes (1, 5, 25M) × 3 data levels (500, 2k, 8k h, subject-split) × 2 seeds = 54 small runs; drop 100M; linear-probe CE on TUAB + sleep.
- **Kill criteria:** seed spread ≥ target gap at the smallest cells; no arm improves 500 → 8k h; band-power arm not better than hand-crafted band power.
- **Likely outcome:** a null ("no T separates within seed noise below 25M / 8k h"), which is still publishable.

## Results
—

## Log
- 2026-10-12 independent review filed (verdict: pursue with major changes).
- 2026-10-11 design sketched in the Q9 hub (*What would separate them*).
- 2026-10-12 moved here.
- 2026-10-12 target T added as a sweep axis (scaling laws per T).
