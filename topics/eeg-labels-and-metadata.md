---
slug: eeg-labels-and-metadata
kind: synthesis
status: active
updated: 2026-10-12
---

# eeg-labels-and-metadata

> What labels and metadata typically come with an EEG recording?

## Current answer
- **Labels come from the experiment design, from self-report, or from experts.** Expert annotation is costly: "annotation of EEG data usually requires a lot of effort on the part of experts" [[jiang2024large]] (§1, p. 2).
  - *Design labels (free):* the cue the subject was told to imagine (left/right hand) [[song2022eeg]] (§IV-A); the film clip shown (SEED: positive/neutral/negative) [[song2022eeg]] (§IV-A).
  - *Self-report:* emotion ratings on valence (sad→happy) and arousal (calm→excited) scales using the Self-Assessment Manikin [[li2022eeg]] (§2.1, Fig. 1, p. 3). Emotion also drifts within a trial, so the single per-trial rating is "only their overall evaluation", and every segment cut from the trial inherits it [[li2022eeg]] (p. 14, Fig. 16; p. 25). 🤖 These are noisy, subjective and usually one rating per trial.
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
| expert annotation (🤖 for sleep stages, the label is *defined* by the EEG/EOG/EMG pattern itself → [[sleep-staging]]) | seizures, sleep stages, abnormal EEG | expensive | sleep stages: human κ 0.76 overall, 0.24 on N1 [[lee2021interrater]]; seizures: no vault number yet; preictal windows are conventions (e.g. 5 min before onset, [[wong2023eeg]] Table 4) |
| clinical records | diagnosis, medications | varies | rarely released |

## Is the field missing a good downstream task? (asked 2026-10-12)
The human's view: the main problem is the lack of any downstream task with good-quality labels. 🤖 Mostly agreed, with a sharper wording. A useful FM benchmark task needs four things at once: (1) a label independent of the scorer's reading of the same EEG, (2) clinical or scientific meaning, (3) headroom (not saturated), (4) enough test subjects and sites for subject-level CIs. In the vault every common task fails at least one:

| task | (1) objective label | (2) meaning | (3) headroom | (4) test size | source |
|---|---|---|---|---|---|
| sleep staging (ISRUC/HMC) | no: scorer reads the same EEG, κ 0.76 | low diagnostic use | no: models at κ ~0.74–0.76 | 10 / 26 subjects | [[lee2021interrater]], [[sleep-staging]], [[xie2026specbram]] Table 6 |
| motor imagery (cue) | yes: the cue is exact | BCI only | yes (4-class ~0.4–0.6) | ok | [[liu2026eeg]] |
| SSVEP | yes | BCI only | no: TRCA 98.8% | ok | [[liu2026eeg]] Tables 2–3 |
| depression (Mumtaz) | diagnosis, single site | yes | no: random-init encoder 0.871 | 10 subjects | [[xie2026specbram]] Table 7, [[eeg-depression-detection]] |
| seizure (CHB-MIT) | expert-marked onsets; agreement unsourced | yes | yes | 2 test children | [[wang2024cbramod]] |
| abnormal EEG (TUAB) | expert report; what "abnormal" means is unread | yes | ceiling ~85–87%? | large | reading queue, [[kiessner2024reaching]] |
| emotion (SEED, FACED) | self-report or clip category | weak | yes (FACED 9-class ~0.24 frozen) | ok | [[li2022eeg]], [[emotion-recognition]], [[xie2026specbram]] Table 8 |

**Why each fails (the binding constraint), 🤖 unless sourced:**
- **Sleep staging fails (1) and (3), and these two failures are linked.** The label *is* a human reading of the same EEG/EOG/EMG under the AASM rules, so a model learns to imitate a scorer, and two scorers agree only at κ 0.76 (N1 0.24) [[lee2021interrater]]. Once models reach that agreement (ISRUC κ 0.74–0.76; [[wang2024cbramod]] Table 7, [[xie2026specbram]] Table 6), further gains mostly fit one scorer's habits, so there is no meaningful headroom left. (2) is weak too: stages are rarely diagnostic on their own → [[sleep-staging]].
- **Motor imagery fails (2), and its label is exact only for what was asked.** The cue is known, but whether and how well the subject imagined is not, so label noise becomes signal-to-noise variance across subjects. The task matters only for BCI. In block designs, class can be confounded with recording run: in an own test, CSP + LDA scored 0.65 on *rest* periods → [[eegmmi-imagined-vs-executed]].
- **SSVEP fails (3).** The stimulus frequency is exact and the response is strong, so a classical pipeline (TRCA) already reaches 98.8% few-shot [[liu2026eeg]] (Tables 2–3). Nothing is left for an FM to show.
- **Depression (Mumtaz) fails (3) and (4), and (1) is doubtful.** Patients vs healthy controls from one site with 10 test subjects; an untrained encoder probes at 0.871 [[xie2026specbram]] (Table 7), so the separation is likely easy and may carry group confounds such as medication or session (unchecked) → [[eeg-depression-detection]].
- **Seizure (CHB-MIT) fails (4), and (1) is unknown.** Only 2 test children in the standard split [[wang2024cbramod]] (App. E.2); with rare positives, one child moves the score. Onsets are expert-marked on the same EEG, and inter-rater agreement for seizure annotation is not sourced in the vault.
- **Abnormal EEG (TUAB) is the best candidate on (2) and (4), but (1) and (3) are unclear.** Labels come from the clinician's report on the same recording, and accuracy seems to plateau around 85–87% [[kiessner2024reaching]] (screening note, not read), which may be a label ceiling rather than a model ceiling.
- **Emotion fails (1) and (2).** Labels are the clip category or a single per-trial self-rating that every segment inherits [[li2022eeg]] (p. 14, p. 25); clip identity and muscle activity are plausible confounds → [[emotion-recognition]].
- **The pattern:** tasks with exact labels (BCI cues) have little clinical meaning or are solved; tasks with clinical meaning have labels read from the same EEG, small or single-site test sets, or a ceiling that may be label noise. Outcome-based labels (below) are the way out of this trade-off.

- 🤖 Candidates with labels that don't come from reading the same EEG: outcome after cardiac arrest ([[turella2024predictive]], 845 patients), seizure onsets confirmed by video-EEG, age (objective but meaningful only as a "brain-age gap"), later diagnosis from linked records (HEEDB scale, [[sun2025harvard]]). None is yet a shared FM benchmark in the vault.
- 🤖 Even with today's labels, part of the problem is statistics, not labels: paired subject-level tests and CIs would make 1–3 point claims interpretable ([[xie2026specbram]] Q&A).

## Open threads
- Which 2022+ benchmarks use outcome-based (non-EEG-read) labels? To find via find-papers.
- Does Mumtaz2016 (depression) include medication status? Not stated in the vault. Check the dataset paper → [[eeg-depression-detection]].
- Inter-rater agreement for seizure annotation: not covered by [[wong2023eeg]] (checked 2026-10-11); still unsourced → [[seizure-detection]] *Open questions*. (Sleep answered: [[lee2021interrater]], see [[sleep-staging]].)

## Sources
- [[wong2023eeg]]: metadata audit of seizure datasets (§5.6–5.7, Tables 5–6).
- [[li2022eeg]]: emotion label models (discrete vs valence/arousal, SAM ratings), induction protocols, label drift within trials (§2.1, §2.3, §5.3).
- [[jiang2024large]], [[song2022eeg]], [[wang2024cbramod]]: label types per benchmark.
