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

## Design
- **Fixed:** one backbone family, one target (e.g. raw-patch MSE *and* band-power, as two arms), preprocessing, masking.
- **Sweep:** model size (≈1M, 5M, 25M, 100M) × pretraining hours (≈500, 2k, 9k of TUEG).
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

## Results
—

## Log
- 2026-10-11 design sketched in the Q9 hub (*What would separate them*).
- 2026-10-12 moved here.
