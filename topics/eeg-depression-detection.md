---
slug: eeg-depression-detection
kind: synthesis
status: stub
updated: 2026-10-10
---

# eeg-depression-detection

> Is depression (MDD, major depressive disorder) really that easy to detect from EEG?

Hub: [[q6-reliability-of-eeg-diagnoses]]

## Current answer
- **Reported numbers are very high**, and on the one dataset seen so far they stay high under a subject-disjoint split:
  - DeprNet: 99.37% when *recordings* are split, but 91.4% when *subjects* are split [[chaddad2023electroencephalography]] (Table 6). Part of the headline number is subject leakage.
  - Mumtaz2016 (34 MDD patients vs 30 healthy controls, 19 channels, eyes-open/closed resting EEG). The split is by subject: 43 for training, 9 for validation, 10 for testing [[wang2024cbramod]] (App. E.4, p. 24).
  - On that split, every model scores 0.91–0.96 balanced accuracy. Tiny EEGNet (3k params) gets 0.923; foundation models get 0.936 (BIOT), 0.941 (LaBraM) and 0.956 (CBraMod) [[wang2024cbramod]] (Table 10).
- 🤖 **Why this is probably easier than it sounds:**
  - The test set has 10 people. Scores are computed on 5 s segments, so each test subject contributes many correlated samples, and one misjudged person moves accuracy by roughly 10 points.
  - The task contrasts diagnosed patients with healthy controls from one site. That isn't screening a general population, where cases are milder and rarer.
  - Plausible confounds (not checked in the vault): medication, recording session, and group-level differences unrelated to depression itself. Models could pick these up.
  - The model ranking spans only ~4 points, so the dataset seems close to saturated rather than a test of what models can do.
  - Supporting this: a *randomly initialised*, untrained encoder with a linear probe already reaches 0.871 balanced accuracy, and the pretext target makes no difference [[xie2026specbram]] (Table 7, §6.4).
- **Status: open.** No vault source tests cross-site / cross-dataset generalization for depression.

## Comparisons
| source | data | split | result |
|---|---|---|---|
| DeprNet (via [[chaddad2023electroencephalography]], Table 6) | not given in the review | recording vs subject | 99.37% vs 91.4% acc |
| [[wang2024cbramod]] (Table 10) | Mumtaz2016, 64 subjects | subject-disjoint (43/9/10) | 0.923 (EEGNet) – 0.956 (CBraMod) bal. acc |
| [[xie2026specbram]] (Table 7) | Mumtaz2016, CBraMod's split | frozen encoder + linear probe | 0.935 (band-power FM, = raw-recon. control), 0.893 CBraMod, 0.876 LaBraM; **random-init encoder 0.871** |

## Open threads
- Cross-dataset or multi-site evaluation of EEG depression classifiers. Need a review of EEG biomarkers for depression (to find via `find-papers`).
- **Medication as a confound:** does Mumtaz2016 record medication status? The vault doesn't say; check the dataset description (figshare, Mumtaz 2016). Clinical metadata is generally sparse; only some datasets (e.g. TUSZ) list medications → [[eeg-labels-and-metadata]].
- What actually differs in the EEG (e.g. specific bands or asymmetry)? No vault source yet.

## Sources
- [[chaddad2023electroencephalography]]: the DeprNet split comparison.
- [[xie2026specbram]]: frozen probes on Mumtaz2016, including a random-init floor.
- [[wang2024cbramod]]: Mumtaz2016 benchmark with a subject-disjoint split (eyes-open/closed sessions only; 50 Hz notch; 5 s windows; test = 5 MDD + 5 HC, App. E.4). *(full read 2026-10-25)*.
