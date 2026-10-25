---
citekey: kontras2026neuroatlas
title: "NeuroAtlas: Benchmarking Foundation Models for Clinical EEG and Brain-Computer Interfaces"
authors: [Konstantinos Kontras, Trui Osselaer, Stylianos G. Mouslech, Angeliki-Ilektra Karaiskou, Guido Gagliardi, Thomas Strypsteen, Mohammad Hossein Badiei, Anku Rani, Maarten Vanmarcke, Miguel Bhagubai, Chanakya Ekbote, Jaedong Hwang, Christos Chatzichristos, Paul Pu Liang, Maarten De Vos]
year: 2026
venue: "arXiv preprint"
doi: ""
arxiv: "2605.14698"
pmid: ""
field: eeg
paper_type: benchmark
task: "frozen-encoder linear-probe benchmark over 4 domains: seizure detection (event-level), sleep (staging, hypnogram features, events, OSA/CI diagnosis), brain age (age + brain-age gap), BCI (MI, ERP, SSVEP, cognitive; confound filtering)"
datasets: [TUSZ, Siena, SeizeIT1, SeizeIT2, CHB-MIT, Helsinki, Epilepsiae, TUAB, NMT, Bonn, CFS, DCSM, DOD, HMC, HomePAP, ISRUC, MASS, PN2026, Sleep-EDF, STAGES, UCDDB, WSC, MESA, MrOS, SHHS, BNCI2014-001, BNCI2014-004, BNCI2015-001, Weibo2014, Dreyer2023, Shin2017A, Liu2024, BI2013a, BI2014a, EPFLP300, BNCI2014-008, ErpCore2021-N170, Nakanishi2015, Kim2025BetaRange, DREAMER, EEGMat, ArithmeticTask]
n_subjects:
n_channels:
model_type: "11 EEG-FMs (BIOT, CBraMod, EEGPT, LaBraM, NeuroGPT, NeuroLM, NeuroRVQ, REVE, SleepFM, ST-EEGFormer S/B/L, MIRepNet) vs 3 time-series FMs (Chronos, Moirai, MOMENT) vs supervised-pretrained models (Seizure-TF, DeepSOZ-HEM, SleepTransformer, SleePyCo, CoRe-Sleep, Sun et al. brain age, EEGNet) + random-init CBraMod"
eval_protocol: "frozen backbone + linear probe (logistic / ridge); patient-level 5-fold CV (LOSO for BCI); leave-one-dataset-out probe for transfer; no fine-tuning, no few-shot"
main_metric: "per domain: event-level sensitivity vs log10 FA/h AUC (seizures), Cohen's kappa + hypnogram-feature MAE (sleep), MAE / Pearson r / BAG AUROC (brain age), normalized balanced accuracy vs binomial chance threshold (BCI)"
main_result: "seizure Event-Sens@FA AUC: NeuroLM 0.553, REVE 0.549 vs random-init CBraMod 0.440; 9 of 11 EEG-FMs not above chance in a top-3 win test (Tables 3-4, pp. 32-33); TS-FMs on par with EEG-FMs in every domain (§5, p. 9)"
code_available: "announced (dataset scripts, preprocessing, configs, evaluation code; §1 p. 2); no URL in the paper"
read_depth: full
concepts: [evaluation-protocols, seizure-detection, sleep-staging, bci-paradigms, self-supervised-pretraining, channel-heterogeneity]
---

# NeuroAtlas (Kontras, Osselaer, Mouslech … De Vos, arXiv 2026)

## TL;DR
Frozen-encoder benchmark: 20 models (29 variants), 42 datasets, ~260k h, with clinical metrics per domain. EEG-FMs don't consistently beat general time-series FMs, mostly sit within ~1 SD of a random-init encoder on seizures, and lose 24–45% when the probe is fit without target labels. Rankings change from dataset to dataset and from one metric to another.

*Read from arXiv v2 (30 Sep 2026; 10 pp. main + appendix to p. 50). KU Leuven (De Vos) + MIT (Liang). The group made SeizeIT1/2 and ST-EEGFormer is from KU Leuven (Van Hulle), so own-group data and models are in the benchmark.*

## Research question
Do pretrained representations (EEG-FM, TS-FM or supervised) encode clinically relevant information in a form a *linear* readout can recover, across several datasets per domain? Three gaps in earlier benchmarks motivate it: one dataset per domain, generic ML metrics, and EEG-FMs compared only with each other (§1, p. 1).

## Data & preprocessing
- **Epilepsy:** 7 continuously labelled cohorts (~1,410 patients, ~58,374 h, ~9,019 seizures; neonatal Helsinki, paediatric CHB-MIT, adult Siena/SeizeIT1/2, TUSZ, Epilepsiae) (p. 4; App. B.1). Recording-level TUAB, NMT and Bonn are evaluated separately (App. D.1.3).
- **Sleep:** 15 cohorts, ~15.8k patients, ~201k h (lab, clinical and home PSG) (p. 5; App. B.2).
- **Brain age:** 10 PSG cohorts with age labels, ~15,000 patients, ~193k h. PN2026 has age-matched healthy vs cognitive-impairment (CI) subjects (App. B.3, p. 22).
- **BCI:** 17 datasets (MI 7, ERP 5, SSVEP 2, cognitive/affective 3), 509 participants, ~159 h. Fig. 1 says 170 h (App. B.4, p. 22).
- **Preprocessing:** shared steps are 0.5 Hz high-pass and notch only. Resampling, referencing, channel matching and scaling follow each model's own pretraining recipe (§3, p. 3; Table 1, pp. 20–21).

## Method
- **Protocol:** every backbone is frozen and gets a linear probe per fold: class-balanced logistic regression with C grid-searched on a validation fold, or ridge for age (§3, p. 3; App. C). Folds are patient-level, BCI uses LOSO, and CV is 5-fold (App. C.1–C.4).
- **Transfer:** leave-one-dataset-out (LODO): the probe is fit on the pooled other cohorts of a domain, and no target labels are used (§3, p. 4).
- **Random-init reference:** CBraMod with random weights. It is the only such control (§3, p. 3; p. 10).
- **Consistency test:** one-sided exact binomial test on how often a model finishes in the top 3 per dataset vs chance 3/k (App. C.5, p. 26).
- **Clinical metrics:**
  - *Seizures:* **Event-Sens@FA AUC**, the mean event sensitivity integrated over log10 FA/h in 0.1–100 FA/h (any-overlap scoring, SzCORE), bounded in [0, 1] (App. C.1, pp. 22–23).
  - *Sleep:* 29 hypnogram features such as REM latency, WASO and transitions (Table 2, p. 24).
  - *Brain age:* brain-age gap (BAG) = predicted − chronological age, with the model trained on healthy subjects (App. C.3).
  - *BCI:* chance-normalized balanced accuracy (50% = chance at any number of classes) plus a per-dataset binomial significance threshold (App. C.4.1, pp. 26–27).
- **BCI confound filter:** 4 Hz high-pass, 40 Hz low-pass and the first post-cue second removed, against eye-movement and drift confounds (p. 8).

## Results (with locations)
- **Seizure detection:**
  - The dataset-best Event-Sens@FA AUC runs from ≈0.50 (Helsinki) to ≈0.74 (SeizeIT1), and the leader alternates between NeuroLM, REVE and SleepFM (p. 5).
  - Means across 7 cohorts: NeuroLM 0.553, REVE 0.549, SleepFM 0.487, Seizure-TF 0.519, Moirai-L 0.474, **random-init CBraMod 0.440 = pretrained CBraMod 0.440**, NeuroGPT 0.277. Seven EEG-FMs sit at or below random init (Table 4, p. 33; App. D.2).
  - Top-3 win test: only NeuroLM (6/7) and REVE (5/7) are above chance. 9 of 11 EEG-FMs fail even within the EEG-FM-only pool (Table 3, p. 32).
  - **Metric changes the ranking:** Spearman ρ between AUROC and event-level ranks is 0.61–0.81 (mean 0.72). On TUSZ NeuroLM is first by AUROC but Seizure-TF is first by events (App. D.1.2, Fig. 7, pp. 27–29). By AUROC the order is REVE 0.839, Moirai-L 0.830, NeuroLM 0.821 (App. D.2).
  - **LODO:** means fall from 0.431–0.553 to 0.275–0.362 (55–76% retained). Every LODO mean lies below the within-dataset random-init 0.440, and only 3 of 42 cells improve. Neonatal Helsinki is hardest (all ≤ 0.247) (App. D.3, p. 32; Table 5, p. 35).
  - **Recording-level:** TUAB AUROC REVE 0.898, ST-EEGFormer-L 0.880, NeuroLM 0.868. Pretrained vs random CBraMod +0.023 on TUAB and +0.024 on NMT. Bonn is saturated, with 11 models at AUROC ≥ 0.99 (App. D.1.3, pp. 30–31).
- **Sleep:**
  - Best per-dataset κ is 0.62–0.85 (p. 5).
  - Supervised sequence models win: CoRe-Sleep and SleepTransformer are top-3 on 15/15 cohorts (Table 6, p. 36). Setting sequence length to 1 removes most of the gap, and an LSTM probe on FM embeddings "largely closes" it (pp. 5–6; App. D.4, p. 33).
  - Without sequence context, TS-FM Moirai-B (7/15) ≈ NeuroLM (6/15) ≈ CoRe-Sleep ℓ=1 (8/15). Within EEG-FMs, NeuroLM 13/15, REVE 10/15, BIOT 8/15 (Table 6).
  - **κ does not predict hypnogram features:** strong staging on DCSM does not give accurate REM latency (p. 6, Fig. 3B).
  - Microarousals: supervised > FMs (p. 6).
  - OSA: detected vs healthy controls, but degrades when other disorders are in the cohort (p. 6).
  - CI from sleep EEG: AUROC ≈ 0.60 (App. D.4.4, p. 39).
  - LODO κ drops most for EEG-FMs (REVE −0.35, NeuroLM −0.31) (App. D.4, pp. 35–38).
  - Only REVE saw sleep data in pretraining (34 of 24,274 patients) (p. 32).
  - κ is unrelated to dataset size or embedding dimension (Fig. 10).
- **Brain age:**
  - The feature-based supervised model of Sun et al. (2019) is the only one significant on both MAE and r (p. 7; Table 11, p. 45).
  - Raw MAE: e.g. 4.86 vs 6.72 (REVE) vs 7.66 years (predict-mean) on the first Table 7 cohort (p. 40).
  - **BAG for CI (100 vs 100 age-matched):** Sun et al. ΔBAG +1.99 y, AUROC 0.592; NeuroLM-VQ similar (+1.72 y); most models near chance (p. 7; Fig. 22, p. 45).
  - LODO: only 3 of 42 fits beat predicting the held-out cohort's mean age (App. D.5, p. 44).
  - Embedding dimension is uncorrelated with performance (ρ = −0.14 for r; Fig. 19, p. 43).
- **BCI (LOSO, frozen):**
  - With the confound filter, MI falls below the significance threshold for most EEG-FMs (p. 8; Fig. 5a, p. 9). ERP, SSVEP and cognitive tasks are not significantly affected (App. D.6, Fig. 23, p. 46).
  - Frozen pretrained EEGNet and MIRepNet sit near chance (App. D.6, p. 47).
  - Flattening tokens beats mean pooling: 45.9 → 53.0% (+7.0), and SSVEP +22.5 (App. D.8, p. 49).
  - **End-to-end EEGNet (LOSO) beats the best frozen FM on 13 of 18 tasks** without the confound filter (e.g. Nakanishi2015 0.917 vs 0.313), and on 9 of 18 with it (App. D.7, pp. 48–49).
  - The best paradigm models differ: EEGPT and ST-EEGFormer-S lead MI, REVE and NeuroLM lead ERP/cognitive (p. 8).
- **Cross-domain:** NeuroLM and REVE are most often top-3 in epilepsy, sleep and BCI; brain age has no stable leader. "We do not find evidence that EEG-FMs are able to consistently outperform time-series FMs" (§5, p. 9).

## Limitations (reported)
- Linear probing only, with no fine-tuning or few-shot, so linear-probe rankings "need not predict" adapted rankings (p. 10).
- Random-init control for CBraMod only; BrainWave left out because its code is unavailable (p. 10).
- Public data, so it can't be a verifiable scoreboard: pretraining overlap is flagged (red dots), not excluded (p. 9).
- The domain metrics are still not clinical utility; patient outcomes would be (p. 10).

## Assessment 🤖
- 🤖 **It tests the "out-of-the-box" promise, not peak performance.** [[liu2026eeg]] and [[chen2026benchmarking]] fine-tune. A frozen linear probe favours models whose features are linearly readable at a chosen pooling, and the authors show that pooling alone moves BCI scores by 7 points. So a "weak" FM can mean "needs a better readout", as [[xie2026specbram]] (§6.4) also found.
- 🤖 **Random-init ≈ pretrained is the most striking result,** but random conv/transformer features plus a tuned linear probe are a known strong baseline (random features). It only says pretraining adds little *linear-readable* seizure information beyond the architecture's inductive bias. With a single random-init model, there's no way to tell whether this holds for other architectures.
- 🤖 **The MI confound result is partly confounded too.** The filter removes eye/drift artifacts but also the first second of genuine ERD, and it shortens trials to 3 s. EEGNet trained end-to-end on the filtered SSVEP data collapses (Kim2025: 0.063), which points to a training failure rather than a confound. The authors' "models rely primarily on artifacts" (Fig. 5 caption) is stronger than the design supports. Still, it is the first FM benchmark to test eye-movement confounds at all → [[q6-reliability-of-eeg-diagnoses]].
- 🤖 **Classical baselines are again missing:** no CSP/FBCSP, Riemannian or band-power + LDA. The one hand-crafted model (Sun et al. sleep features) wins brain age. That matches [[xie2026specbram]] (band power ≈ FM frozen features on sleep) and the abstract of [[zare2026negative]].
- 🤖 **The strongest contribution is the clinical metrics.** Event-level seizure ranking ≠ AUROC ranking, κ ≠ hypnogram accuracy, and age MAE ≠ BAG utility. This is the first vault source for event-level sensitivity vs false alarms/h → [[seizure-detection]].
- 🤖 **LODO is the most deployment-like number in the vault.** With no target labels, no model beats a random-init encoder probed *with* labels. Site and cohort shift dominate model choice, consistent with [[bomatter2025limited]] and [[q6-reliability-of-eeg-diagnoses]].
- 🤖 **Small internal inconsistencies:**
  - The Fig. 2 caption says "all three pretrained families exceed random-init on every dataset", which is true for family-best only; per model, 7 EEG-FMs are ≤ 0.440 (Table 4).
  - Table 12 has ST-EEG-S at 15/18 (k = 12), but the text says 14/18 with k = 7 (p. 50).
  - BCI hours are given as 170 vs 159.
  - Table 1 (p. 21) describes "Seizure-TF" as an RNS-implant model on daily A+B pattern features, contradicting App. A.2 (a SeizureTransformer checkpoint trained on scalp TUSZ + Siena, 10 s windows). The table row looks copied from a different model.
- 🤖 **Own-group data** (SeizeIT1/2 under managed access, ST-EEGFormer) is in the benchmark. ST-EEGFormer is not the headline winner, so bias looks limited.

## Concepts
- [[evaluation-protocols]]: frozen linear probe with per-model preprocessing; LODO probe; binomial top-3 win test; per-dataset binomial chance threshold; pretraining overlap flagged, not excluded.
- [[seizure-detection]]: event-level sensitivity vs FA/h (0.1–100) AUC; AUROC and event rankings disagree; 7 continuous cohorts.
- [[sleep-staging]]: 15 cohorts; sequence context explains the supervised advantage; κ vs hypnogram features; microarousals, OSA.
- [[bci-paradigms]]: MI vs ERP/SSVEP under eye-movement/drift confound filtering; token flattening vs mean pooling.
- [[self-supervised-pretraining]]: pretrained ≈ random-init CBraMod; EEG-FMs ≈ time-series FMs; no embedding-dimension scaling.
- [[channel-heterogeneity]]: each model gets its own montage from the same recording (picked, bipolar-recomputed, interpolated or coordinate-based); handling of missing channels unstated.

## Related papers
- [[liu2026eeg]]: the matched fine-tune + few-shot benchmark (FMs ≈ specialists). NeuroAtlas reaches the same verdict under frozen probes and adds TS-FMs and random init.
- [[chen2026benchmarking]]: EEG-Arena (fine-tune, FMs win most tasks). NeuroAtlas disagrees under frozen probing; REVE leads in both.
- [[kuruppu2026eeg]]: cited (ref 45) for incomparable FM protocols. Its remark that general time-series FMs can beat EEG-FMs is confirmed here at scale.
- [[xie2026specbram]]: hand-crafted features ≈ FM frozen features, and the pooling/readout caveat. Both point the same way.
- [[bomatter2025limited]]: cohort/people effects. Here LODO shows target-cohort labels matter more than model choice.
- [[jiang2024large]], [[wang2024cbramod]], [[yang2023biot]], [[wang2024eegpt]], [[ouahidi2025reve]]: evaluated FMs. REVE is among the most consistent; LaBraM and CBraMod are rarely top-3.
- [[lawhern2018eegnet]]: EEGNet trained end-to-end (LOSO) beats the best frozen FM on 13/18 BCI tasks.
- [[zare2026negative]]: classical features beat FMs on dementia, the same direction as brain age here.
- [[xiong2025eeg]], [[shen2026brain4fms]], [[wu2025adabrain]], [[yang2026eeg]]: earlier benchmarks in §2.1. [[yang2026eeg]] (ICLR 2026, FMs vs traditional decoders on BCI) is queued for Q7.
- [[dan2024szcore]]: the event-scoring framework used for seizures.

## Q&A notes
- 2026-10-25 **Q:** Is NeuroLM's 0.553 seizures caught divided by false alarms per hour? **A:** No. The probe gives a seizure probability per 10-s window. Each decision threshold gives one operating point: detected seizures / all seizures (sensitivity, any-overlap scoring) and false alarms per hour. Sweeping the threshold traces sensitivity against FA/h. 0.553 is the area under that curve on a log10 FA/h axis from 0.1 to 100, divided by the width, so it is the *mean sensitivity across alarm budgets* (App. C.1, pp. 22–23). 🤖 The range includes 10–100 FA/h, which is useless clinically, so sensitivity at the clinically relevant low end is lower than 55%. The paper doesn't report it.
- 2026-10-25 **Q:** What is "window-level AUROC"? **A:** Each 10-s window is scored seizure vs non-seizure on its own. AUROC is the probability that a random seizure window gets a higher score than a random background window (threshold-free). It ignores whether detections form clean events, how many alarms per hour they cause, and whether a short seizure is caught at all. With >99% background windows it can stay high while alarms are frequent (p. 4; App. D.1.2).
- 2026-10-25 **Q:** What is ρ 0.61–0.81? **A:** Spearman rank correlation (ρ, not p) between two rankings of the same ~23 models on one cohort, one by AUROC and one by event-level score. 1 = identical order; 0.61–0.81 = similar overall with many pairwise swaps, e.g. a different winner on TUSZ (Fig. 7, p. 29).
- 2026-10-25 **Q:** What are "sequences of epochs"? **A:** In sleep, an *epoch* is a 30-s scoring window, not a training pass. Supervised sleep models take a run of consecutive epochs (SleepTransformer 21 ≈ 10.5 min, SleePyCo 10) and label the centre or last one, as human scorers do under AASM rules (App. A.2, p. 20). The FM probes saw each 30-s epoch alone. The "ℓ = 1" ablation forces the supervised models to do the same, and most of their advantage disappears (p. 5).
- 2026-10-25 **Q:** Is leave-one-dataset-out the most likely clinical setting? **A:** 🤖 For a product bought off the shelf, roughly yes: it was trained elsewhere and meets a new hospital, device and population with no local labels. That is external validation. But NeuroAtlas's LODO is harsher than real practice in three ways. (1) The probe is linear and trained on only 6 pooled cohorts. (2) A held-out cohort can be a population absent from training, e.g. neonatal Helsinki, and no one would deploy an adult-only model on neonates. (3) Deployments usually allow site tuning, such as alarm thresholds or a local validation set. The within-dataset numbers correspond to a hospital training on its own past patients. For long-term monitoring, a third setting (per-patient calibration on the first seizures) is also realistic → [[evaluation-protocols]] *When is within-subject evaluation clinically realistic?*
- 2026-10-25 **Q:** Which devices: same manufacturers, same channel counts? **A:** No, and the paper doesn't tabulate devices or channels per dataset. Sourced in the paper:
  - *BCI:* 3–64 channels, 128–2048 Hz, from a consumer Emotiv EPOC (14 ch, 128 Hz) to research systems (App. C.4, pp. 25–26).
  - *Epilepsy:* SeizeIT2 is a wearable dataset (ref. 9 title, "Wearable dataset of patients with focal epilepsy"). The rest is clinical scalp EEG, from neonatal (Helsinki) to pre-surgical (Epilepsiae).
  - *Sleep:* PSG from many labs and home studies (App. B.2).
  - Channels are also chosen *per model*: each model gets its pretraining montage (e.g. BIOT 16–18 bipolar, CBraMod 19 10-20 channels, the supervised sleep models a single EEG channel; Table 1, pp. 20–21). So models don't even see the same channels of a recording. The exact per-dataset channel matching is promised for App. A.2 but not given there.
  - 🤖 From memory, unverified: SeizeIT2 uses behind-the-ear electrodes, and TUSZ mixes several referential montages.
- 2026-10-25 **Q:** Is the brain-age model built for specific channels or a device? **A:** For a montage, not a device. Sun et al. expect a 6-channel sleep montage (F3, F4, C3, C4, O1, O2 referenced to the contralateral mastoid, e.g. F3-M2), with a 2-channel variant, at 200 Hz, and use normalized sleep-EEG features (Table 1, p. 21). These are standard PSG derivations, so most sleep cohorts can provide them. The paper doesn't say which variant was used per cohort.
- 2026-10-25 **Q:** What are drift artifacts in motor imagery? **A:** Slow baseline wander below ~1–4 Hz that isn't cortical rhythm: electrode polarisation, sweat and skin potentials, and cable or head movement. Eye movements also produce large low-frequency potentials. They become confounds when they correlate with the class. Examples: the subject looks toward a left/right arrow cue (a saccade in the first second after the cue), or class blocks fall at different times as the baseline drifts (p. 8, refs 6 and 66). The 4 Hz high-pass removes both and leaves the mu/beta (8–30 Hz) MI rhythms; dropping the first post-cue second removes the cue saccade. 🤖 It also removes early real ERD, so the drop isn't pure confound removal.
- 2026-10-25 **Q:** Isn't averaging output tokens wrong unless the model was pretrained for it? **A:** It is a real information bottleneck, though not wrong in principle. Masked-reconstruction pretraining trains *per-token* outputs and never trains a pooled vector, so averaging is an untested readout. Averaging over time throws away *when* something happened. If tokens are per channel, averaging over channels throws away *where*, e.g. C3 vs C4 laterality, which is the whole MI signal. The data agree: flattening beats mean pooling by +7.0 points on average, SSVEP +22.5, MI +6.4, ERP +6.3, cognitive +0.9 (App. D.8, p. 49). Averaging costs little for slow "state" labels such as sleep stage, abnormal background and workload. Flattening has its own cost: tokens × dimension features with few trials, so the linear probe overfits easily and needs a fixed token count. The paper doesn't say how tokens were pooled into window embeddings for seizures/sleep. Same pattern in [[xie2026specbram]]: CBraMod's own all-token head roughly doubles the mean-pooled FACED score (§6.4). → [[evaluation-protocols]] *Variants*
- 2026-10-25 **Q:** Was any performance good enough for clinical use? **A:** Not for frozen FMs, and the authors say so: current FMs "do not yet deliver on the promise of an out-of-the-box unified EEG model" (abstract), and their metrics are "still insufficient" for clinical utility (p. 10). By domain 🤖:
  - *Seizures:* the best mean sensitivity is ~55% averaged over 0.1–100 FA/h, and ~36% at best without target labels (Table 5). That is far from usable, given that 0.1 FA/h is already 2.4 false alarms per day. The clinical target (high sensitivity at well under 1 FA/day) is my unsourced assumption; [[dan2024szcore]] may give one.
  - *Sleep staging:* best per-cohort κ 0.62–0.85, mostly from supervised sequence models (p. 5). The upper end reaches human inter-scorer agreement (κ 0.76, [[lee2021interrater]]), so automated staging with human review is plausible. It drops sharply on unseen cohorts.
  - *OSA from EEG alone:* fails once other disorders are present (p. 6).
  - *Brain-age gap for cognitive impairment:* AUROC 0.59 at best (p. 7), not useful.
  - *BCI:* LOSO frozen MI is at chance after confound control.
  - The benchmark measures linear-readable information, not a tuned product, so it is a floor for what fine-tuned FMs could do. → [[q6-reliability-of-eeg-diagnoses]] scorecard
- 2026-10-25 **Q:** Were per-model channels picked from a superset the device recorded, or generated? **A:** Both, depending on the model (Table 1, pp. 20–21):
  - *Picked:* fixed-montage models take a named subset (CBraMod 19 10-20 channels, NeuroGPT 22, DeepSOZ-HEM 19, sleep models one derivation such as C4-A1 or Fpz-Cz).
  - *Computed, but trivially:* bipolar channels for BIOT (e.g. F3−C3) are differences of two recorded electrodes, and re-referencing (common average for EEGPT/NeuroGPT) is a weighted sum. Both are exact linear recombinations, not invented signal.
  - *Generated:* MIRepNet maps every layout onto a 45-channel motor template by inverse-distance interpolation, so missing electrodes are estimated from neighbours.
  - *Not needed:* REVE (3D coordinates), LaBraM/NeuroLM (channel embeddings) and the time-series FMs (channel by channel) take whatever is present.
  - The paper doesn't say what fixed-montage models got when a dataset lacked their channels, e.g. wearable SeizeIT2 or 3-channel BNCI2014-004 (zero-fill? interpolation? skipped?). 🤖 That is a real gap for exactly the cross-device question.
- 2026-10-25 **Q:** Did removing confounds push MI below chance, making frozen-FM BCI random? **A:** Below the *significance threshold*, not below chance. Read off Fig. 5a (p. 9): MI mean normalized balanced accuracy drops from ~59–68 to ~54–59 for every model (50 = chance; the aggregated p < 0.05 threshold is ~66). For a 2-class task that is ~54–59% accuracy. It applies to one setting only: MI, cross-subject with no calibration, frozen features. ERP and SSVEP were unaffected, and EEGPT reaches ~84 normalized on SSVEP (App. D.6). 🤖 Cross-subject zero-calibration MI is the hardest BCI setting for every method: CSP + LDA in the own EEGMMI test drops to 0.56 cross-subject ([[eegmmi-imagined-vs-executed]]), and practical MI BCIs calibrate per user ([[q7-foundation-models-vs-baselines]]). So the BCI paradigm isn't random. What this shows is that frozen FMs don't give a calibration-free MI decoder, and part of the apparent skill came from eye movements and drift.
- 2026-10-25 **Q:** Are tokens per second or per channel, and does that follow from what is masked? **A:** For most EEG-FMs here a token is one channel × one time patch (CBraMod 1 s per channel; LaBraM, REVE, NeuroRVQ and BIOT similar, Table 1), so it is both. Masking then hides some (channel, time) patches. A patch can be reconstructed from the same channel's neighbouring seconds *and* the neighbouring electrodes at the same moment. Time-series FMs (Chronos, MOMENT) tokenise each channel separately in time. → [[self-supervised-pretraining]] *Variants*: what the masking unit makes easy.
