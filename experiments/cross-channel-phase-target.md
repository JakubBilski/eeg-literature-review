---
slug: cross-channel-phase-target
status: idea
questions: [q9]
concepts: [self-supervised-pretraining, time-frequency-analysis, seizure-detection]
datasets: [tueg, tuev, isruc]
scripts: []
figures: []
cost: high            # FM pretraining with a new target
origin: 2026-10-12, "does predictability reveal what matters clinically?" ([[q9-pretraining-objectives-and-scale]])
updated: 2026-10-12
---

# cross-channel-phase-target

## Hypothesis
🤖 Phase *within* a channel is mostly irrelevant for rhythms, but phase *relationships between* channels are clinical. Clinicians localize spikes by phase reversal across bipolar chains, and connectivity measures use phase. A masked target that is invariant to per-channel phase but keeps cross-channel phase should beat a pure band-power target on spike/event tasks (TUEV) without losing on sleep. Reasoning → [[q9-pretraining-objectives-and-scale]] *Does predictability reveal what matters clinically?* (caveat 5).

## Design
- **Targets per masked patch, per band:**
  - (A) log band power per channel: the SpecBraM target ([[xie2026specbram]]);
  - (B) A + cross-channel phase differences between neighbouring electrodes (cos/sin of the cross-spectrum phase, or the complex coherency);
  - (C) raw-waveform MSE as a reference.
- **Masking:** spatial masking of whole channels at a time point, so that a spike's field on neighbouring electrodes is the predictable part. Temporal-only masking can't teach spike timing (caveat 4).
- **Everything else fixed:** backbone, TUEG subset, steps.
- **Probes:** TUEV (6 event classes, transient morphology), ISRUC sleep (spectral control), linear probe + fine-tune.

## What each outcome would mean
- B > A on TUEV, B ≈ A on sleep → cross-channel phase carries event information that spectral targets drop.
- B ≈ A everywhere → spatial phase is recoverable from power patterns, or 1 s patches are too coarse for spikes.
- C > B on TUEV → waveform morphology, not phase relationships, is what matters; consistent with LaBraM's raw/codebook targets beating Fourier targets on TUEV ([[jiang2024large]] App. G Table 7).

## Prior work
- None in the vault. Related: [[covariance-pseudo-labels]] (zero-lag spatial coupling as clustered targets; B is its lagged, regression form). LaBraM regresses per-channel Fourier amplitude + phase but no cross-channel terms ([[jiang2024large]] §2.2).
- Phase reversal as a clinical localization rule is still unsourced in the vault (needs a clinical EEG reference).

## Results
—

## Log
- 2026-10-12 idea from the Q9 predictability question.
