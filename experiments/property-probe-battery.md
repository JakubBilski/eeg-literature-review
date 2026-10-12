---
slug: property-probe-battery
status: idea
questions: [q9, q7]
concepts: [self-supervised-pretraining, evaluation-protocols, time-frequency-analysis, frequency-bands]
datasets: [tueg, tuab, tuev, isruc]
scripts: []
figures: []
cost: medium          # frozen-FM inference on many recordings; no pretraining; downstream numbers reused from EEG-Arena
origin: 2026-10-12, "compare FMs on designed property tasks first, then measure transfer to downstream?" ([[q9-pretraining-objectives-and-scale]])
updated: 2026-10-12
---

# property-probe-battery

## Hypothesis
🤖 Downstream EEG scores are too noisy (few subjects, label noise) to rank pretraining choices directly. Properties computed *from the signal itself* (band power, cross-channel phase lag, spike morphology, nuisance identity) can be scored on unlimited unlabelled recordings with tight confidence intervals. A model's downstream score should then be predictable from (a) how much of each property its frozen embedding makes usable and (b) how much each property matters for the task, measured once, without any FM. Reasoning → [[q9-pretraining-objectives-and-scale]] *Probe FMs on EEG properties before downstream?*

## Design
- **Models:** open FMs with frozen embeddings (CBraMod, LaBraM, EEGPT, BIOT, REVE), each with a **random-init copy of the same architecture** as control. If available, the REVE-base checkpoints pretrained on 600 to 30,000 h with everything else fixed [[chen2026benchmarking]] (Protocol IV, p. 7): a within-family series with no architecture confound. *Checked 2026-10-12:* the paper doesn't say whether these six checkpoints are released, nor what corpus each size uses (p. 7).
- **Property battery** (targets computed from held-out TUEG recordings, subjects split):
  - *spectral:* log band power per channel and band (the SpecBraM target, [[xie2026specbram]]);
  - *spatial phase:* phase lag / imaginary coherency between neighbouring electrodes per band;
  - *spatial coupling:* zero-lag covariance in tangent space ([[covariance-pseudo-labels]]);
  - *morphology:* presence and shape of transients (spike-like sharpness, e.g. TUEV event spans);
  - *nuisance:* subject ID, dataset/device ID, age, sex, recording session.
- **Three measurement types** (all CEs in bits, continuous targets discretized into quantile bins; framing → [[q9-pretraining-objectives-and-scale]] *Information-theory framing*):
  0. *Prediction (Shannon game):* a small head on frozen embeddings of the visible context predicts T of a masked or future window. Held-out CE upper-bounds H(T(X_masked) | X_context); lower = better FM for that property.
  1. *Decodability:* V-information / MDL / online codelength of the property under a fixed small probe family (linear and 1-hidden-layer), layer-wise and on token-level embeddings, not only pooled ones ([[sirca2026beyond]], abstract: weak frozen probes are "largely explained by the pooling strategy"). Report the gain over the random-init control and over the property's own entropy.
  2. *Invariance:* embedding change (e.g. CKA or normalized distance) under transformations that should or should not matter: a shared random phase per frequency across channels (keeps power and cross-channel phase; [[wang2026eeg]] Eq. 2, App. B.1 p. 14) vs an independent random phase per channel (destroys cross-channel phase). **Every perturbation is matched by a sham with equal removed energy** ([[cao2026when]], abstract).
- **Task relevance, measured without FMs:** for TUAB, TUEV and ISRUC, how much each property computed directly from the signal predicts the label (same probe family).
- **Stage 2:** predict each model's downstream linear-probe score (reuse the EEG-Arena tables, [[chen2026benchmarking]]: linear-probe results exist only for the Protocol III variants, Tables 32–50, single runs) from Σ (task relevance × decodability gain). Few free parameters, so 5 to 30 models are enough to test it. Compare against parameter count and pretraining hours as predictors.

## What each outcome would mean
- The stage-2 model predicts downstream ranks better than size or data hours → property profiles are a cheap, low-noise way to compare pretext objectives; new targets ([[cross-channel-phase-target]], [[covariance-pseudo-labels]]) could be screened by property gain without full benchmarks.
- FMs beat random-init on spectral properties but not on spatial phase or morphology → consistent with spectral-dominated learning; TUEV-type gaps come from what objectives ignore.
- Nuisance decodability predicts cross-dataset drop → a mechanistic link to [[q6-reliability-of-eeg-diagnoses]].
- Decodability does not predict downstream (as in NLP probing tasks) → the information is present but not *used* by fine-tuning; move to intervention-style tests (steering, ablation with sham control).

## Prior work
- [[wang2026eeg]] (EEG-FM-Audit): the same phase surrogate, but applied to *fine-tuned* classifiers and scored as an accuracy drop, not as a property of frozen embeddings. Accuracy fell for all 4 FMs on TUEV, TUAB and BCI IV 2b (Table 6, p. 9). Not yet read in full.
- [[cao2026when]]: alpha removal changes SAE latents 7.3× more than a sham notch, but only 0.28× after normalizing by removed spectral energy (abstract). Perturbation-only probing is confounded by energy.
- [[sirca2026beyond]]: block-wise probing; early blocks already hold task information (abstract).
- [[lehnschiler2026mechanistic]]: SAE features of SleepFM, REVE and LaBraM grounded in abnormality, age, sex and medication; age and pathology entangled (abstract).
- [[xie2026specbram]]: band power as an explicit target; nearly matched by hand-crafted band power under a linear probe.
- 🤖 NLP precedent (out of the vault's field scope, not in screening): probing tasks (SentEval probing suite), control tasks (selectivity), MDL probing and V-information. Main lesson: probe accuracy often correlates weakly with downstream use.

## Review (2026-10-12, independent subagent, abstracts + arXiv search)
**Verdict: pursue with major changes; the better first project** (no pretraining, weeks not months, and it becomes the measurement tool for [[pretext-downstream-scaling-sweep]]). 🤖 throughout except identifiers.
- **Partly scooped:** [[kommineni2026aperiodic]] already probes reconstruction-FM embeddings with synthetic EEG: bias toward the aperiodic / low-frequency part, oscillations under-represented, subject identity encoded more strongly than the task (abstract, via subagent). [[steglich2026representational]]: embedding stability and probe performance "dissociate". **Novel part left:** cross-channel phase and morphology in bits, energy-matched shams, random-init twins, and the within-family REVE series (check whether those checkpoints are public).
- **Stage 2 weaknesses:** 5–30 confounded models; EEG-Arena preprocessing differs from the probes; decodable ≠ used; properties overlap (band power = covariance diagonal), so Σ relevance × gain double-counts. Size / data hours are a strawman baseline: compare against LogME (arXiv 2102.11005) and a direct few-label probe instead. Position stage 2 as exploratory.
- **Kill criteria:** FM gain over random-init within CI for most properties; stage 2 doesn't beat LogME / few-shot probe.

## Results
—

## Log
- 2026-10-12 independent review filed (verdict: pursue with major changes).
- 2026-10-12 idea from the human's proposal; 4 related 2026 papers screened.
