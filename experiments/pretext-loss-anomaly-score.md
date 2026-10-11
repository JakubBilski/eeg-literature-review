---
slug: pretext-loss-anomaly-score
status: idea
questions: [q9, q6]
concepts: [self-supervised-pretraining, seizure-detection, signal-quality-and-noise]
datasets: [chbmit, tuab]
scripts: []
figures: []
cost: medium          # FM inference only, but needs a released checkpoint with its reconstruction head
origin: 2026-10-11, "is pretext loss informative / usable as an anomaly score?" ([[q9-pretraining-objectives-and-scale]])
updated: 2026-10-12
---

# pretext-loss-anomaly-score

## Hypothesis
🤖 A pretrained FM's masked-prediction error is high on abnormal EEG (seizures, abnormal background), so it could screen unlabelled recordings. But raw-MSE error mostly measures *power*: its irreducible part scales with signal power ([[xie2026specbram]] §4). So the raw score should do no better than a simple amplitude or line-length detector, and artifacts should dominate it. A power-normalized score might add something.

## Design
- **Model:** a released FM checkpoint that ships its pretraining head. CBraMod (raw-patch MSE, [[wang2024cbramod]] Eq. 12) is the natural choice; check that the reconstruction head is in the release. Its pretraining excluded CHB-MIT.
- **Score per window:** mean masked-patch reconstruction error over random masks. Three variants: raw MSE; MSE divided by patch power; error in band-power space.
- **Baselines:** per-window total power, line length, and a high-amplitude artifact flag. These are the null models the FM score must beat.
- **Data:**
  - CHB-MIT seizure vs non-seizure windows, per patient. One annotated record is already local ([[seizure-detection]]; `plot_seizure.py`).
  - TUAB abnormal vs normal at the recording level (mean score per recording).
- **Metric:** AUROC and AUPRC; also the score's correlation with power. Inspect the top-scoring non-seizure windows: are they artifacts?

## What each outcome would mean
- Raw score ≈ power baseline → the pretext loss is a power detector, as the theory predicts; not useful beyond simple features.
- Normalized score > power and line length → FM error carries information beyond amplitude; a candidate for label-free triage ([[q6-reliability-of-eeg-diagnoses]] *Thought experiment*).
- Top-scoring windows are mostly artifacts → needs artifact removal before any clinical use.
- **Extension (Q6, needs data not in the vault):** score the "normal" first EEGs of patients later diagnosed with epilepsy against controls.

## Prior work
- None in the vault. Held-out pretext loss is almost never reported [[kuruppu2026eeg]] (§4.3, p. 15). Lower pretext loss ≠ better features ([[wang2024eegpt]] Table 5). 🤖 In ML generally, generative models can give *higher* likelihood to simple out-of-distribution inputs (Nalisnick et al. 2019, from memory, not in the vault).
- To find: 2022+ EEG normative-modelling / brain-age papers and reconstruction-based EEG anomaly detection (reading queue in [[interests]]).

## Results
—

## Log
- 2026-10-11 idea raised by the human (Q9 *Is pretext loss itself informative?*; Q6 thought experiment).
- 2026-10-12 turned into this experiment note.
