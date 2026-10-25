---
citekey: "bomatter2025limited"
title: "Is Limited Participant Diversity Impeding EEG-based Machine Learning?"
authors: [Philipp Bomatter, Henry Gouk]
year: 2025
venue: "NeurIPS 2025"
doi: ""
arxiv: "2503.13497"
pmid: ""
field: eeg
paper_type: benchmark
task: "normality prediction (TUAB), dementia diagnosis (CAUEEG), sleep staging (PhysioNet 2018)"
datasets: [TUAB, CAUEEG, PhysioNet-2018]
n_subjects: 4400        # approx: TUAB >2,300 + CAUEEG 1,122 + PhysioNet 2018 994 (994 from the dataset page, not stated in the paper)
n_channels: 19
model_type: "TCN, mAtt (SPD manifold attention), LaBraM-Base (scratch vs pretrained)"
eval_protocol: "cross-subject; training sets subsampled on a participants x segments-per-participant grid; fixed test set"
main_metric: "accuracy (per-participant majority vote on TUAB/CAUEEG; per-epoch on sleep)"
main_result: "TUAB TCN: 0.74 with 25 people x 320 segments vs 0.84 with 800 x 10 (same 8,000 segments); sleep: 25 x 640 = 0.66 matches 400 x 5 (Fig. 3)"
code_available: "https://github.com/bomatter/participant-diversity-paper"
read_depth: full
concepts: [evaluation-protocols, domain-adaptation, self-supervised-pretraining, sleep-staging]
---

# Is Limited Participant Diversity Impeding EEG-based Machine Learning?

## TL;DR
On three >1,000-person datasets, the number of people dominates accuracy for one-label-per-person diagnosis (TUAB, CAUEEG); more data per person adds ~nothing there. Sleep staging is the exception: data per person helps as much as people. LaBraM pretraining helps in every regime except the most data-starved one; augmentations don't.

## Research question
- Q1 Do few participants limit performance? Q2 Can more data per participant compensate? Q3/Q4 Do augmentations / SSL pretraining help, and in which data regime (p. 2)?
- Framing: two-level data model. Each person i has a distribution P_i drawn from a population Q; m segments per person, n people (§3, Fig. 1A). Cited theory: the generalisation gap scales as Θ̃(1/√n + 1/√(mn)), so with a real person-level shift, n governs overfitting "unless one is able to design a model architecture with the appropriate invariances" (§3, ref [22]).

## Data & preprocessing
- **TUAB** v3.0.1: >2,300 people, mostly 15–25 min recordings; first 30 s dropped, 15 min used (§3.2–3.3).
- **CAUEEG:** 1,122 of 1,379 people with normal / MCI / dementia labels from neurologists; 5 min used (§3.2–3.3).
- **PhysioNet 2018 Challenge:** sleep staging on 30-s AASM epochs, the **6 EEG channels only** (no EOG/EMG), public training part only, with an age- and sex-stratified participant split (§3.2, App. A.1).
- 1–50 Hz band-pass, 100 Hz, 19 channels (TUAB/CAUEEG), **average reference**, non-overlapping 2-s (TUAB/CAUEEG) or 30-s (sleep) segments (§3.3).
- LaBraM inputs follow its paper: 200 Hz, 0.1–75 Hz, 50 Hz notch (not matched to 60 Hz TUAB line noise), and **15-s** sleep epochs, because its positional encoding stops at 16 s (§3.3, p. 5).

## Method
- Grid: n ∈ {25, 50, …, 1600} people × m ∈ {5, 10, …, 640} segments per person, drawn at random from the training split (Fig. 1B, Fig. 3). A control with contiguous blocks instead of random segments gives the same pattern on TUAB (App. A.7, Fig. 7).
- Models: braindecode TCN (4 blocks, 64 filters), mAtt (covariance/SPD attention), LaBraM-Base (§3.4).
- Augmentations: AmplitudeScaling [0.5, 2], FrequencyShift (≤0.3 Hz), PhaseRandomisation (full 2π, per channel) (§3.5).
- Pretraining: public LaBraM-Base weights (16 datasets, ~500 participants per the authors), full fine-tune; learning rate tuned on validation for both the pretrained and the from-scratch arm (§3.6, Table 1).
- AdamW, fixed LR 1e-3 for TCN/mAtt, early stopping on a fixed validation set (patience 5 × 500 batches) (App. A.1).

## Evaluation
- Cross-subject, one fixed test set for every grid cell. TUAB/CAUEEG are scored per person (majority vote over segments); sleep per epoch (App. A.3).
- 25 subsampling seeds for baselines; pretraining 25 seeds (TUAB, CAUEEG) or 5 (sleep); augmentations 1 seed (App. A.3). Error bars = SEM over subsampling seeds, not over test people.
- Metric is accuracy only (no κ, no cross-entropy).

## Results (with locations)
- **People scaling (fixed m = 40):** accuracy rises strongly from 25 to several hundred people on all three tasks, then flattens. Doubling TUAB to ~3,200 people would buy "roughly 1%" (§4.1, Fig. 2).
- **People vs data per person, TCN (Fig. 3):**
  - *TUAB:* along m nothing changes (25 people: 0.75 at m = 5, 0.74 at m = 320). At a fixed 8,000 segments: 25 × 320 = 0.74, 200 × 40 = 0.82, 800 × 10 = 0.84.
  - *CAUEEG:* same pattern, e.g. 25 people 0.43 → 0.47 over m; at 2,000 segments 25 × 80 = 0.47 vs 400 × 5 = 0.53.
  - *Sleep:* m matters. 25 people: 0.51 (m = 5) → 0.66 (m = 640). "25 participants was sufficient to match the performance achieved with … 400 participants (with 5 segments per participant)" (§4.2). People still help at fixed total, but saturate early: at 8,000 segments 25 × 320 = 0.64, 50 × 160 = 0.68, then 0.67–0.69 up to 800 × 10; at 16,000, 25 × 640 = 0.66 vs 800 × 20 = 0.71 (own read of Fig. 3).
  - mAtt and LaBraM show "qualitatively similar trends" (App. A.8, Figs. 8–9).
- **Architectures:** accuracies are "relatively similar"; "the sample size was the primary driver" (App. A.5). LaBraM from scratch is worst, most on sleep (part preprocessing: TCN on LaBraM inputs also drops, but still beats it; App. A.6, Fig. 6).
- **Augmentations:** small and inconsistent; PhaseRandomisation hurts TCN/mAtt on sleep (destroys waveforms such as K-complexes), helps LaBraM there. No correlation of benefit with sample size (§4.3, Fig. 4, Table 2).
- **Pretraining (LaBraM fine-tuned − scratch, paired by seed):**
  - TUAB: ≈ 0 at 25 people (−0.01 to +0.02), +0.03–0.04 at 100–1,600 people with few segments, +0.01–0.02 at the most data (Fig. 5). It "looks like a boost in the amount of data per participant" (§4.4).
  - Sleep: +0.01 to +0.08 everywhere, no trend with people (Fig. 11). CAUEEG: −0.02 to +0.04 (Fig. 10).
  - Pretrained LaBraM matches or beats TCN/mAtt on TUAB (Fig. 12).

## Limitations (reported)
- Only cross-participant settings; BCI often trains per-person models (§6).
- Existing augmentations only; the nature of the participant shift (anatomy vs disease phenotype diversity) is not identified (§6).
- PhysioNet heatmaps have missing top-right cells (not every person has 640 epochs) (App. A.3).

## Assessment 🤖
- 🤖 The cleanest EEG answer so far to "people vs data per person", and it splits by task exactly along the one-label-per-person line: TUAB/CAUEEG are people-bound, sleep is not. Agrees with [[oliveira2026scaling]]'s loss fits (TUAB subject-dominated, ISRUC sleep trial-dominated).
- 🤖 The authors explain the TUAB/CAUEEG pattern as a person-level distribution shift. A simpler reading also fits: with one label per person, n *is* the number of independent labels, and m adds only correlated repeats of the same label (pseudo-replication). The theory term 1/√n covers both, but the two explanations predict different things for tasks with within-person labels.
- 🤖 The sleep setup is weak by sleep standards: 6 average-referenced EEG channels, no EOG/EMG, single epochs without context, accuracy rather than κ. Peak 0.73 accuracy is far below sequence models. Random epoch sampling across a night also inflates the value of m relative to taking whole short recordings (tested only on TUAB).
- 🤖 SEM over subsampling seeds with one fixed test set ignores test-person sampling error; with the sleep test set size unstated, small differences (≤2 points) are not interpretable.
- 🤖 The model axis is three different architectures, not one family at several sizes, so no size × people interaction can be read off. A hint: LaBraM-scratch gains along m on TUAB (0.69 → 0.73 at 25 people) where TCN gains nothing, i.e. the larger model wants more data of *any* kind, not specifically more people.
- 🤖 Pretraining gain on TUAB is ≈ 0 at 25 people and largest at moderate data, which contradicts "FMs help most when labels are scarce" and agrees in direction with [[chen2026benchmarking]] Fig. 4.

## Concepts
- [[evaluation-protocols]] — participant × segment grid with a fixed cross-subject test set; per-person vs per-epoch scoring.
- [[domain-adaptation]] — names participant distribution shift as the bound on scaling; asks for augmentations that imitate person differences (§5).
- [[self-supervised-pretraining]] — LaBraM pretrained vs scratch over the whole data grid.
- [[sleep-staging]] — the task where people matter least.

## Related papers
- [[poziomska2025quantity]] — same task family at larger scale: recordings (3k → 56k) at a fixed 39-hospital mix rather than people × segments; quantity keeps helping, attention/transformer MIL nets overtake a feature ensemble only at 56k.
- [[kontras2026neuroatlas]]: leave-one-dataset-out probes lose 24–45% (seizures), and only 3/42 brain-age fits beat the cohort mean. Cohort shift outweighs model choice.
- [[oliveira2026scaling]] — concurrent supervised scaling study over subjects vs trials; same task split (subjects bind TUAB, trials bind sleep).
- [[jiang2024large]] — LaBraM-Base, the pretrained model evaluated here.
- [[chen2026benchmarking]] — pretrain-vs-scratch gain by label budget, same direction (small at the lowest budget).
- [[roy2019deep]] — cited for dataset sizes: half of 154 studies had <13 participants, six had >250 (§4.1).
- [[wang2024causes]] — identity shortcuts in one-class-per-subject tasks vs inter-subject variability in multi-class tasks.
- [[kiessner2024reaching]] — TUAB scaling by number of recordings (cited as ref [8]/[9], §2).
- [[banville2025scaling]] — within-subject image decoding: few gains from more participants (§2, §6).

## Q&A notes
- 2026-10-12 **Q:** Sleep staging is the task where people should matter least. What does that mean for [[subject-diversity-gap]]? **A:** Confirmed here (Fig. 3) and in [[oliveira2026scaling]] (p. 6). The experiment's H1 is now largely answered on the very pilot dataset, and sleep is the weakest place to test the size × people interaction (H3). Details and a proposed redesign → [[subject-diversity-gap]] *After reading Bomatter & Gouk*; why sleep is people-light → [[sleep-staging]] *Do people matter in sleep staging?*
