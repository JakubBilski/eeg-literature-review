---
citekey: wong2023eeg
title: "EEG datasets for seizure detection and prediction — A review"
authors: [S. Wong, A. Simmons, J. Rivera-Villicana, S. Barnett, S. Sivathamboo, P. Perucca, Z. Ge, P. Kwan, L. Kuhlmann, R. Vasa, K. Mouzakis, T.J. O'Brien]
year: 2023
venue: "Epilepsia Open 8 (2023) 252–267"
doi: "10.1002/epi4.12704"
arxiv: ""
pmid: "36740244"
field: eeg
paper_type: review
task: "seizure detection and seizure prediction (dataset characteristics)"
datasets: [Bonn, CHB-MIT, NeuroVista Ictal, Kaggle UPenn-Mayo, Kaggle AES, Hauz Khas, Kaggle Melbourne-NIH, TUSZ, Helsinki neonatal, Siena]
n_subjects: ""
n_channels: "1–76 across datasets (Table 2)"
model_type: ""
eval_protocol: ""
main_metric: ""
main_result: "10 public seizure datasets compared on 10 characteristics; the most used (Bonn, 58 of 120 studies, Table A1) is single-channel, balanced, pre-cut and has no patient IDs (§5.1, §5.6, §6.1)"
code_available: ""
read_depth: full
concepts: [seizure-detection, evaluation-protocols, channel-heterogeneity, electrode-types, signal-quality-and-noise]
---

# EEG datasets for seizure detection and prediction: a review (Wong et al., 2023)

## TL;DR
A narrative review that compares the 10 public EEG seizure datasets ML papers actually use. They differ on almost everything: channels, scalp vs implanted electrodes, continuity, class balance, patient IDs and sampling rate. The most popular ones are the least realistic.

*JATS conversion from Europe PMC; locations are the paper's section numbers (§N) and tables. The feature-count formula in §7 was lost in conversion.*

## Research question
Which public EEG datasets are used for seizure detection/prediction, how do they differ, and how should those differences guide the choice of dataset, preprocessing and ML method? (§1)

## Data & preprocessing
- **Two searches** (§3, Fig. 1):
  1. Scopus + Web of Science, "seizure prediction" OR "seizure detection", last 5 years, >20 citations → 225 unique → **120 studies** after exclusions (no ML, device design, pure replications, non-EEG or multimodal).
  2. Google Dataset Search, Kaggle, PhysioNet and earlier reviews, to find datasets directly.
- Only datasets that are publicly accessible are analysed (§4). The 21 datasets used by the 120 studies include private ones (Table A1).
- Screening: the first author labelled everything; two co-authors each labelled 50% (§3).

## Method
- **Definitions** (§5.5, §6.1):
  - *Ictal* = during a seizure; *preictal* = the period before one; *interictal* = between seizures.
  - *Detection* = recognise an ongoing seizure (needs ictal + interictal data).
  - *Prediction* = warn before onset (needs preictal + interictal data).
- **10 characteristics in two groups** (Fig. 2):
  - *Primary:* channels, signal type, temporal properties, data preparation, application, subjects, other info.
  - *Structural:* class distribution, segment information, sampling frequency.
- One table per characteristic (Tables 2–8), then a discussion of what each means for ML (§7).

## Evaluation
- Not applicable (no models trained). The authors note that selecting by citation count may favour small datasets, "as the results obtained on these datasets will appear more impressive (e.g., near 100% sensitivity as a result of overfitting to a small dataset)" (§8).

## Results (with locations)
- **Usage (Table A1):** Bonn 58 studies, CHB-MIT 31, Freiburg 19 (no longer public), NeuroVista 4, others ≤3.
- **Scalp vs intracranial:** 5 scalp datasets (CHB-MIT, Hauz Khas, TUSZ, Helsinki, Siena), 4 intracranial (NeuroVista and the three Kaggle sets). Bonn mixes scalp recordings from healthy subjects with intracranial recordings from patients (§5.2, Table 2).
- **Channels:** Bonn and Hauz Khas are single-channel, cut and pooled from multichannel recordings. Most others have 16–19 channels. Siena has 29, Kaggle UPenn 16–76 and TUSZ 23–31 (§5.1, Table 2).
- **Continuity** (§5.3, Table 3):
  - *Noncontinuous, randomly cut segments with no time relation between them:* Bonn, Hauz Khas, Kaggle.
  - *Short-term continuous (<24 h):* TUSZ, Helsinki, Siena.
  - *Some recordings over 24 h:* CHB-MIT (with 10 s gaps between files).
- **Curated segments** (§5.4, Table 4):
  - Bonn had artifacts removed by eye and kept only segments meeting "at least weak stationarity".
  - The Kaggle prediction sets define preictal as 5 min before onset. Interictal is ≥1 week from any seizure (AES) or ≥3 h before / 4 h after one (Melbourne).
- **Subjects** (§5.6, Table 5):
  - TUSZ is the largest, with 642 subjects in Table 5 but 592 in the text. Helsinki has 79 neonates, CHB-MIT 23 and Siena 14.
  - Bonn and Hauz Khas have 10 each and pool segments with no patient IDs.
  - Two Kaggle sets include dogs.
- **Class balance** (§6.1, Table 7):
  - Seizures are "<1% of the total recorded EEG data" (§2).
  - Only Bonn and Hauz Khas are balanced, because their segments were picked to be. This "does not represent true seizure dynamism".
- **Size** (Table 8):
  - Seizure events: TUSZ 3,050, Melbourne-NIH 633, Helsinki 460, CHB-MIT 198, Siena 47.
  - Bonn is 500 segments × 23.6 s (100 ictal) at 173.86 Hz.
  - Sampling rates run from 173.86 to 5000 Hz, and vary *within* the Kaggle sets and TUSZ.
- **Leakage trap:** Kaggle Melbourne-NIH and NeuroVista Ictal come from the same implanted-device trial. Kaggle used its 3 worst-performing patients, so combining the two risks data leakage (§7).
- **Discussion claims (§7):**
  - Datasets with preselected channels (e.g. inside the epileptogenic zone, the brain area where seizures start) give higher performance but are "less reflective of real-world EEG recordings".
  - Seizure EEG varies across patients and seizure types, so models pooled over a few patients generalise poorly. TUSZ's breadth helps.
  - Seizure risk follows circadian (daily) cycles, and models with a circadian term did better on long-term NeuroVista data. Only long continuous datasets allow this.
  - Neural networks and SVMs suffer from class imbalance. Resampling helps, but a balanced set misrepresents real recordings.
  - Bonn and Hauz Khas are too small for deep learning without augmentation.
  - Choose by deployment setting: scalp data for ICU/hospital use; intracranial data for long-term home warning devices, where higher SNR and fewer movement artifacts matter.
  - Extra signals help: wearable EMG detects generalised tonic–clonic seizures with >90% sensitivity, and heart rate changes during seizures.
  - Channel count, sampling rate and segment length differ so much that a model "cannot truly" be tested on another dataset without re-tuning.

## Limitations (reported)
- Total seizure duration and seizure types per dataset were not tabulated (§8).
- "Seizure segments" vs "seizure events" are counted inconsistently across datasets (§8).
- Selecting studies by citations may favour small, impressive-looking datasets (§8).

## Assessment 🤖
- 🤖 The most useful finding for Q6 is the mismatch between popularity and realism. Bonn has 58 of 120 uses, yet it is single-channel, balanced by construction, curated by eye and pooled with no patient IDs. Subject-wise splits are impossible on it, so near-100% accuracies on Bonn (e.g. the "CNN 98%" in [[chaddad2023electroencephalography]] Table 6) say little about clinical use.
- 🤖 Internal inconsistencies: TUSZ subjects 592 (text) vs 642 (Table 5); Kaggle UPenn events 48 (Table 8) vs 28 (§6.2); Bonn sampling rate 173.86 (Table 8) vs 173.6 (§6.3); Kaggle sampling "400–5000" (Table 8) vs "400 and 500 Hz" (§6.3). Treat the exact numbers with care.
- 🤖 It's a dataset catalogue, not a methods review. It doesn't compare reported accuracies, evaluation protocols (e.g. how false alarms per hour are counted) or inter-rater agreement for seizure labels.
- 🤖 Pre-foundation-model. TUSZ's breadth argument has since been taken up: TUSZ is ≈45% of LaBraM's pretraining hours ([[jiang2024large]] App. D), which makes TUH-based seizure benchmarks in-domain for it.
- 🤖 The "intracranial for home devices" advice reflects the authors' NeuroVista background. Wearable scalp, behind-the-ear and EMG devices are not discussed (cf. [[niso2022wireless]]).

## Concepts
- [[seizure-detection]]: defines detection vs prediction and ictal/preictal/interictal, and catalogues the public datasets.
- [[evaluation-protocols]]: no patient IDs in Bonn/Hauz Khas; leakage between Kaggle Melbourne and NeuroVista; imbalance and resampling.
- [[channel-heterogeneity]]: 1–76 channels, inconsistent channel naming, 10-20 vs extended 10-10 ("Nomenclature") placements; sampling rates 173.86–5000 Hz.
- [[electrode-types]]: scalp vs intracranial (implanted) EEG: SNR, artifacts, invasiveness.
- [[signal-quality-and-noise]]: intracranial EEG has higher SNR because the skull attenuates scalp signals (§7).

## Related papers
- [[chaddad2023electroencephalography]]: lists Bonn, CHB-MIT and Siena as standard seizure datasets (Table 3). This paper explains why Bonn results don't transfer.
- [[wang2024cbramod]]: CHB-MIT seizure benchmark (16 bipolar channels, test on 2 subjects; App. E.2, Table 8).
- [[jiang2024large]]: pretrains largely on TUSZ (App. D).
- [[niso2022wireless]]: at-home seizure monitoring with wireless EEG (§4.2.2).
- [[gans2024sleep]]: the parallel case for sleep, where wearables are validated against a reference recording.
- [[roy2019deep]]: in 2010–2018 DL papers, CHB-MIT (9) and Bonn (7) were already the most used seizure datasets (Table 6). 60% of DL-EEG papers used no cross-validation (p. 22).

## Q&A notes
