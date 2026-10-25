---
slug: embedding-data-diagnostics
status: idea
questions: [q6, q7, q9]
concepts: [evaluation-protocols, sleep-staging, self-supervised-pretraining, channel-heterogeneity, domain-adaptation]
datasets: [sleep-edf, hmc, isruc, dcsm, dod-h, dod-o, ucddb]
scripts: []
figures: []
cost: medium          # frozen-FM inference on ~7 open sleep cohorts (laptop CPU feasible but slow; downloads tens of GB); no training of FMs
origin: '2026-10-25, "explore datasets through the data lens - data-similarity measures from pretrained models to identify failure modes, but activations may be dominated by noise" (after [[kontras2026neuroatlas]])'
updated: 2026-10-25
---

# embedding-data-diagnostics

## Hypothesis
🤖 Weak downstream scores don't mean frozen-FM embeddings are *noise*. More likely they are dominated by *structured nuisance variance* (dataset, device, montage, subject, night): dataset identity is linearly decodable at AUROC 1.000 for 5 FMs [[zare2026negative]] (§4.4, Table 7), and subject identity is encoded more strongly than the task ([[kommineni2026aperiodic]], abstract via subagent). If so, embedding geometry is a usable *data lens* for failure modes, but only if it carries information beyond cheap signal statistics (band power, amplitude, line noise, metadata). NeuroAtlas found random-init CBraMod ≈ pretrained CBraMod on seizures [[kontras2026neuroatlas]] (Table 4), so that last condition is the open question.

## Design
Sleep is the testbed: NeuroAtlas's largest domain, ~7 cohorts openly downloadable, cohorts differ in site, device, montage and population, labels are per 30-s epoch, and some cohorts have multiple scorers.

**Representations (all frozen, same epochs):** CBraMod, LaBraM, BIOT, REVE (gated access) + a **random-init twin of each architecture** + **hand-crafted features** (per-channel log band power, Hjorth, spectral entropy; [[zare2026negative]] §3.4 family) + **metadata vector** (sampling rate, derivation, lab/home, age, sex, disorder). Readouts: mean-pooled and token-flattened → PCA (fixed dim), because the readout changes results [[kontras2026neuroatlas]] (App. D.8).

**Stage 0: variance decomposition (is it noise or nuisance?).** For each representation, the fraction of embedding variance explained by dataset, subject, night (Sleep-EDF SC has 2 nights per subject), sleep stage and time of night: linear mixed model / PERMANOVA on PCA components, plus batch-mixing metrics borrowed from single-cell (kBET/LISI-style neighbourhood mixing of datasets vs conservation of stages; scIB, [[luecken2021benchmarking]]). *Noise* = the residual variance that no factor explains, measured against **split-half reliability** (the same epoch re-embedded with jitter of ±1 s: an unstable embedding is noise; a stable one tied to subject or dataset is nuisance).

**Test A: does embedding distance predict transfer failure?** (main test)
- Target: a **pairwise transfer matrix**. Train a linear probe on cohort i and test on cohort j (≈7 × 6 = 42 ordered pairs), with drop_ij = κ(j→j, CV) − κ(i→j).
- Predictors: distance(i, j) computed from each representation:
  - label-conditioned OT distance (OTDD, per-stage Gaussian W2; [[alvarezmelis2020geometric]]);
  - marginal MMD;
  - a *graded* domain-classifier score (cross-entropy of a capacity-limited probe or kNN mixing, **not** accuracy, which saturates at 1.000 per [[zare2026negative]]).
- **Decisive comparison:** does FM-embedding distance predict drop_ij better than (a) the random-init twin's distance, (b) the hand-crafted-feature distance, (c) metadata distance? Partial correlations and nested models.
- Stats: pairs aren't independent (each cohort appears 12 times), so use a Mantel-type permutation test that permutes cohort labels, and leave-one-cohort-out prediction of the drop. Pre-register the main contrast (FM vs hand-crafted distance) before seeing results.

**Test B: does embedding geometry locate label ambiguity?** (label-quality test)
- Multi-scorer cohorts: DOD-H, DOD-O (several scorers, per the NeuroAtlas consensus analysis, App. D.4 Fig. 14) and ISRUC (2 scorers; to verify per dataset).
- Per epoch, compute frozen-embedding ambiguity: kNN label disagreement, margin of a probe trained on *other subjects'* consensus labels, and local density.
- Target: whether human scorers disagree on that epoch. Metric: AUROC.
- Compare with the same scores from hand-crafted features and random-init twins, and with the supervised-ensemble entropy reported by [[rossi2025sleepyland]] (ROC AUC up to 0.828 per a secondary summary; to verify in full text).
- 🤖 This tests the "noise" worry directly. If ambiguity in the embedding tracks *human* ambiguity, the geometry carries label-relevant structure even where classification is mediocre. If it doesn't, but hand-crafted features do, the FM lens is no better than spectra.

## What each outcome would mean
- **FM distance > hand-crafted and random-init distance at predicting transfer drop:** the FM provides a usable "data lens". A cheap pre-deployment check becomes possible: embed a new site's unlabelled data and predict whether a model will transfer. Useful for [[q6-reliability-of-eeg-diagnoses]] and [[q8-commercial-eeg-analysis-systems]] (site acceptance testing).
- **FM ≈ hand-crafted ≈ random-init:** the "lens" is just spectral and amplitude statistics. The field should report cheap spectral data cards and stop attributing dataset similarity to FM understanding. This also supports [[kontras2026neuroatlas]]'s random-init result from a different angle.
- **Stage 0 shows mostly unexplained, unstable variance:** your noise worry is right; embeddings aren't a lens at all for this data.
- **Stage 0 shows mostly dataset/subject variance:** embeddings are nuisance-dominated. Test A then becomes the key question: is the nuisance *predictive* of failure, or only separating?
- **Test B positive for FMs only:** FM embeddings encode stage boundaries the way humans perceive them. That suggests label-cleaning and active-learning uses, even where FM classification adds nothing.
- **Kill criteria:** if, before running Test A, Stage 0 shows the hand-crafted features explain cohort separation as well as FM embeddings do (same mixing scores), downgrade Test A to a confirmation. If transfer drops barely vary across pairs (range < ~0.05 κ), Test A has no signal to predict.

## Prior work
- [[zare2026negative]] (full read of §3–4): dataset membership decoded at AUROC 1.000 by all 5 encoders, also after PCA-50, balanced subsampling, 0.5–40 Hz filtering and z-scoring (REVE only for the last) (§4.4, Table 7). Separability saturates, so it can't rank encoders or datasets. Causes (device, population, site) are confounded (§4.4).
- [[kontras2026neuroatlas]]: LODO transfer drops per cohort (seizures Table 5; sleep Fig. 15; brain age Fig. 20); random-init ≈ pretrained on seizures; readout matters. Its transfer numbers come from *pooled* LODO, not pairwise, so it gives no distance–drop analysis.
- [[property-probe-battery]] (own idea): decodability of nuisance properties. Its outcome list already asks "nuisance decodability predicts cross-dataset drop?". This note is the dataset-level, distance-based version, with transfer as the target. Possible merge, to decide after review.
- [[kommineni2026aperiodic]] (abstract via subagent): FM embeddings biased to aperiodic power; subject identity > task.
- [[steglich2026representational]] (screening): embedding stability vs probe performance under montage change "dissociate".
- [[rossi2025sleepyland]] (abstract + secondary summary): supervised-ensemble disagreement tracks human scorer disagreement on DOD. It is the label-ambiguity baseline for Test B.
- [[lee2021interrater]]: human κ 0.76 overall, 0.24 on N1. That is the size of label ambiguity Test B tries to locate.

### Other fields
- [[alvarezmelis2020geometric]] (ML/vision; abstract): OTDD, a label-aware OT distance between datasets; "correlates well with transfer learning hardness". Transfers to EEG? It needs a meaningful feature space; here that is exactly what is in question, which is why the hand-crafted-feature distance is the comparator.
- [[you2021logme]] (ML; abstract): LogME estimates transferability from frozen features without fine-tuning. A per-model (not per-dataset) score; usable as an extra predictor in Test A.
- [[liu2024decades]] (vision; abstract): YFCC/CC/DataComp are classified by source at 84.7% (chance 33.3%). Even huge, diverse datasets carry learnable dataset signatures, so near-perfect EEG dataset decoding is unsurprising and not by itself a failure mode.
- [[zech2018variable]] (radiology; abstract): CNNs identify the hospital system from chest X-rays, and external performance drops in 3/5 comparisons. The clinical precedent for "site is encoded, and it hurts transfer".
- [[luecken2021benchmarking]] (single-cell; abstract): scIB scores embeddings on batch removal *and* biological conservation (14 metrics). A ready-made metric set for Stage 0.
- [[kedzierska2025zero]] (single-cell FMs; abstract): zero-shot scGPT/Geneformer embeddings are often worse than simple baselines (highly variable genes, scVI) at clustering and batch correction. 🤖 The closest parallel: FM embeddings used as a "data lens" without fine-tuning lost to simple features. Prior odds for Test A's "FM ≈ hand-crafted" outcome go up.
- MRI travelling-subject designs (Oxford travelling-heads: 10 subjects, 5 sites, 6 scanners; web search, not in screening): the same people scanned on several devices is the design that *separates* device from population. 🤖 EEG has no 2022+ open equivalent found (search 2026-10-25: a 2017 four-headset oddball study released only one headset). A candidate partial substitute is simultaneous ear-EEG + scalp-EEG sleep recordings (Aarhus; to check), with the same brain and night recorded by two sensors.

## Review (2026-10-25, independent subagent, abstracts + arXiv/web search + vault files)
**Verdict:**
- **Stage 0:** merge into [[property-probe-battery]] (nuisance arm); run it only as a descriptive appendix.
- **Test A:** pursue with major changes.
- **Test B:** pursue, small.
- Likely outcome everywhere: FM ≈ hand-crafted. Worth knowing, but a modest result. 🤖 throughout except identifiers.

**Novelty**
- *Stage 0 is mostly known:* dataset identity is at ceiling [[zare2026negative]] (Table 7, spot-checked), and subject > task [[kommineni2026aperiodic]] (abstract).
- *Test B is close to published work:* [[rossi2025sleepyland]] (ensemble disagreement vs DOD scorer disagreement); hypnodensity work reporting scorer ambiguity across many scorers (Stephansen 2018; Bakker et al. 2022, *not resolved to an identifier, not filed*); NeuroAtlas Fig. 14. The new part is *label-free frozen geometry* against hand-crafted and random-init controls.
- *Test A:* no EEG study found that correlates embedding distance with transfer drop. [[zhao2025selectivefinetuning]] uses an EMD feature distance to *select* sleep source data, not to predict drop.
- *Adjacent fields have settled the general question* (all abstract-level via the subagent): dataset distance predicts accuracy under shift ([[deng2021labels]]; [[morais2026wireless]], wireless signals, Pearson > 0.85; [[roschewitz2023distance]]), and confidence/agreement predictors are strong ([[garg2022leveraging]] ATC, [[baek2022agreement]]), with limits under medical shift ([[nguyen2023out]]). So "an FM distance predicts drop" is not a finding. Only "FM distance beats spectra *and* confidence-based predictors" would be.

**Well-posedness fix (Test A):**
- 7 cohorts give 21 unordered pairs that aren't independent (the permutation test has only 7! = 5040 permutations), so the contrast has almost no power. Move to the **subject level**.
- Pre-registrable version: per held-out target *subject*, the distance from that subject to the training pool in frozen-FM space predicts the subject's κ drop better than the same distance in hand-crafted and random-twin space. Statistic: Δ Spearman ρ with a cohort-clustered bootstrap CI. One primary FM (CBraMod), mean-pooled, fixed PCA-64.
- Test B: use *graded* scorer disagreement (fraction of scorers deviating), with Spearman ρ, or AUROC at a pre-set binarisation.

**Ranked threats**
1. **Derivation confound:** Sleep-EDF has only Fpz-Cz / Pz-Oz (spot-checked in [[zare2026negative]] §3.2), while most other cohorts have central derivations. Distance and drop would both encode "which electrode". Restrict to a shared derivation or stratify by it. FM channel contracts also degrade on 1–2 channel input.
2. **Few units;** drops are asymmetric and depend on the target's N1 share and label noise.
3. **Missing baselines:** ATC, agreement-on-the-line, LogME.
4. **The probe sees single 30-s epochs,** so drops reflect the context-free probe, not deployment (NeuroAtlas: context closes most of the gap).
5. **Readout dependence** (mean pool vs flatten).
6. **The ±1 s jitter "noise" metric is weak:** it tests time-shift invariance, which any spectral encoder passes. Drop it.

**Minimal version (~2 weeks):**
- CBraMod + its random twin + hand-crafted features.
- 4 cohorts with a shared central derivation (HMC, ISRUC, DCSM, DOD; *derivations to verify*).
- Subject-level Test A + Test B on DOD. Compute is a few GPU-hours; downloads and per-model preprocessing are the real cost.

**Order:** build the shared embedding cache → Stage 0 descriptive (about a day) → Test B → Test A (redesigned).

**Kill criteria:**
- Hand-crafted distance alone reaches ρ ≥ 0.7 with the drop and FM distance adds a Δρ whose CI includes 0.
- The random twin matches pretrained on mixing scores.
- Cohort explains most subject-level drop variance (ICC > 0.8), collapsing the test back to n = 4.

**My take (main session, 🤖):**
- Agree on the subject-level redesign, the derivation confound and adding ATC/agreement baselines. These are the most useful corrections; the original Test A would likely have produced an uninterpretable correlation on 21 pairs.
- Agree to drop the jitter metric.
- Partly disagree on merging Stage 0 away entirely: its random-twin vs hand-crafted mixing comparison is the cheapest direct answer to the human's "is it noise?" question. Keep it as the first deliverable, whichever note it lives in.

## Results
—

## Log
- 2026-10-25 independent review filed (Stage 0 merge/appendix; Test A pursue with major changes; Test B pursue, small); 7 more priors screened.
- 2026-10-25 idea from the human's question; 7 priors added to screening (1 EEG, 6 other-field).
