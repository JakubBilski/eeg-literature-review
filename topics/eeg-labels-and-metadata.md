---
slug: eeg-labels-and-metadata
kind: synthesis
status: stub
updated: 2026-10-10
---

# eeg-labels-and-metadata

> What labels and metadata typically come with an EEG recording?

## Current answer
- **Labels come from the experiment design, from self-report, or from experts.** Expert annotation is costly: "annotation of EEG data usually requires a lot of effort on the part of experts" [[jiang2024large]] (§1, p. 2).
  - *Design labels (free):* the cue the subject was told to imagine (left/right hand) [[song2022eeg]] (§IV-A); the film clip shown (SEED: positive/neutral/negative) [[song2022eeg]] (§IV-A).
  - *Self-report:* emotion ratings on valence (sad→happy) and arousal (calm→excited) scales using the Self-Assessment Manikin [[li2022eeg]] (§2.1, Fig. 1, p. 3). 🤖 These are noisy, subjective and usually one rating per trial.
  - *Expert annotation:* normal vs abnormal recording (TUAB) [[jiang2024large]] (§3, p. 6); seizure segments labelled ictal (during), preictal (before) and interictal (between) [[wong2023eeg]] (§6.1); sleep stages, typically per 30 s window [[roy2019deep]] (p. 11).
- **Clinical metadata is sparse and uneven.** In seizure datasets:
  - TUSZ is the richest: medical history, *medications*, seizure type, EEG description and the clinician's "impression", and per-channel information.
  - Siena has seizure type, onset area, age and gender. CHB-MIT has only age and gender. Bonn and several Kaggle sets have none [[wong2023eeg]] (§5.7, Table 6).
  - Some sets (Bonn, Hauz Khas) don't even record which segment came from which patient, so subject-wise splits are impossible [[wong2023eeg]] (§5.6).
- **Medication context can sit in the protocol rather than a field.** CHB-MIT recorded children "following withdrawal of anti-seizure medication" [[wang2024cbramod]] (App. E, p. 23).
- **Auxiliary channels:** ECG (CHB-MIT, TUSZ, Helsinki, Siena), respiratory effort (Helsinki), photic stimulation (TUSZ), vagus nerve stimulation (one CHB-MIT patient) [[wong2023eeg]] (Table 6).
- **Recording metadata needed to use the signal:** channel names/montage, reference, sampling rate. These vary across datasets and must be harmonized → [[channel-heterogeneity]].
- 🤖 Also standard but not yet sourced in the vault: event markers ("triggers") time-stamping each stimulus, and the BIDS format for organizing EEG data and metadata.

## Comparisons
| label source | example | cost | reliability (🤖) |
|---|---|---|---|
| experiment design | motor imagery cue, film clip | free | high for "what was asked", unknown for "what the brain did" |
| self-report | valence/arousal ratings | cheap | noisy, subjective |
| expert annotation | seizures, sleep stages, abnormal EEG | expensive | inter-rater disagreement exists (no vault number yet) |
| clinical records | diagnosis, medications | varies | rarely released |

## Open threads
- Does Mumtaz2016 (depression) include medication status? Not stated in the vault. Check the dataset paper → [[eeg-depression-detection]].
- Inter-rater agreement for sleep staging and seizure annotation: expected in [[gans2024sleep]] / [[wong2023eeg]].

## Sources
- [[wong2023eeg]]: metadata audit of seizure datasets (§5.6–5.7, Tables 5–6) *(selected sections only so far)*.
- [[li2022eeg]]: emotion label models *(selected sections only)*.
- [[jiang2024large]], [[song2022eeg]], [[wang2024cbramod]]: label types per benchmark.
