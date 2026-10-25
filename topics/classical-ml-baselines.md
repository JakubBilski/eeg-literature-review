---
slug: classical-ml-baselines
kind: synthesis
status: growing
updated: 2026-10-11
---

# classical-ml-baselines

> What are the non-deep-learning baselines for EEG classification, and how much has DL actually beaten them?

## Current answer
- **The classical recipe:** hand-crafted features (band power, entropy, wavelet coefficients) feed a shallow classifier: SVM, KNN, random forest, LDA, naive Bayes. SVM is the most common [[chaddad2023electroencephalography]] (§2.5.1, Table 4).
- **In BCI specifically, LDA is the default, not SVM:** LDA 31% vs SVM 21% of 114 BCI papers (2009–2019); CNN 4% [[varbu2022past]] (Fig. 13). LDA is described as "a simple classifier with low computation requirements and acceptable accuracy" (§5.9). The feature side is PSD, Fourier or CSP (Fig. 12).
- **Motor imagery standard:** filter-bank CSP (FBCSP). Band-pass filters → spatial filters learned per subject → linear classifier. It reaches 67.75% on BCI IV-2a vs 78.66% for Conformer [[song2022eeg]] (Table II).
- **DL gain over classical pipelines (2010–2018):** 67.9% of 156 DL papers had a traditional baseline (§3.7.1, p. 21). The median accuracy gain was +5.4% (IQR 9.4%), with only 4 negative values (p. 24) [[roy2019deep]].
- **Why that gain is overstated:** there is publication bias, and many baselines were weak (spectral features + linear classifier). Only 2 studies used Riemannian pipelines, "although these methods have set a new state-of-the-art in multiple EEG classification tasks" [[roy2019deep]] (§4, p. 28). The evaluation was loose too: 60% of studies used no cross-validation, only 22 of 108 inter-subject studies held subjects out, and 19.9% ran a statistical test (pp. 22–23). One example: an SVM at 74.2% on SEED matched a CNN that needed 30× noise augmentation to reach 74.3% (p. 14).
- **A matched 2018 comparison (same splits, 4 paradigms):** EEGNet vs xDAWN + Riemannian tangent space (ERP data) and FBCSP (motor imagery) [[lawhern2018eegnet]] (Figs. 2–5). Values are read off bar charts.
  - Within-subject: EEGNet beats xDAWN+RG on P300 (0.92 vs 0.87 AUC), MRCP (0.80 vs 0.75) and ERN (0.82 vs 0.77). It ties FBCSP on 4-class motor imagery (0.68 vs 0.68).
  - Cross-subject: CNNs win on P300 (0.90 vs 0.80) and MRCP (0.81 vs 0.70), but **xDAWN+RG wins on ERN** (0.765 vs 0.745). On motor imagery, CNNs beat FBCSP (0.40 vs 0.32), but chance is 0.25.
  - 🤖 So the classical pipelines were not dominated; the winner depends on the paradigm and the protocol.
- **Today's supervised baselines in foundation-model papers** are deep, not classical: EEGNet, Conformer, SPaRCNet, ContraWR, etc. On Mumtaz2016, EEGNet (3k params) gets 0.923 vs 0.956 for CBraMod [[wang2024cbramod]] (Table 10). 🤖 Riemannian / FBCSP baselines are missing from these comparisons, so the vault can't yet tell how much pretraining beats a strong classical pipeline.
- **FM papers rarely compare with expert features:** only 4 of 10 early EEG foundation models did, and those reported "substantial improvements" after fine-tuning [[kuruppu2026eeg]] (Fig. 4a, §5.1). The review recommends benchmarking against expert features and task-specific supervised models with statistical tests (§6.1). TUAB may already be saturated at 85–87% accuracy with traditional approaches (§5.2, ref Kiessner 2024).
- **Band power is still a strong baseline for frozen features:** on sleep staging, 5-band power with logistic regression matches or beats the frozen embeddings of LaBraM, BIOT and CBraMod [[xie2026specbram]] (Table 5). → [[q7-foundation-models-vs-baselines]]
- **The largest FM benchmark has no classical pipeline:** EEG-Arena's 25 baselines are 24 DL models plus YASA (spectral sleep features) [[chen2026benchmarking]] (Table 6). 🤖 So its "FMs beat supervised baselines" says nothing about CSP/Riemannian pipelines.
- **Hand-crafted sleep features win brain-age prediction:** in NeuroAtlas, the feature-based Sun et al. (2019) sleep-EEG model is the only one consistently top-3 on both MAE and Pearson r across 7 cohorts. It beats all 11 frozen EEG-FMs and 3 time-series FMs [[kontras2026neuroatlas]] (p. 7, Table 11). The benchmark has no CSP/Riemannian pipeline for BCI; there, end-to-end EEGNet is the strongest reference (13/18 tasks; App. D.7).
- **DL in that period:** CNN 41%, RNN ~14%, autoencoders ~13%, CNN+RNN 7% of papers [[roy2019deep]] (§3, p. 17).

## Glossary (🤖 standard definitions, no vault source yet; Lotte 2018 should cover them)
- **LDA = Linear Discriminant Analysis** (Fisher), *not* latent Dirichlet allocation: a linear classifier assuming Gaussian classes with shared covariance, used with shrinkage in BCI → [[linear-discriminant-analysis]].
- **CSP (common spatial patterns):** learns channel weightings (spatial filters) whose output variance differs most between two classes; a supervised cousin of PCA/ICA → [[common-spatial-patterns]].
- **Riemannian methods:** covariance matrices + a mixing-invariant distance; MDM or tangent-space classifiers, not just kNN → [[riemannian-methods]].

## Comparisons
| baseline | input | learned part | where seen |
|---|---|---|---|
| band power + SVM/LDA | spectral features | classifier only | [[chaddad2023electroencephalography]], [[varbu2022past]] |
| FBCSP | band-passed raw EEG | spatial filters + linear classifier | [[song2022eeg]] (Table II) |
| [[riemannian-methods]] (MDM / tangent space) | covariance matrices | class means / linear classifier | [[roy2019deep]] (§4.5: named as SOTA, used by 2 of 156 DL papers) |
| xDAWN + Riemannian tangent space + elastic net | ERP epochs | ERP spatial filters + covariance classifier | [[lawhern2018eegnet]] (§2.2.3) |
| EEGNet | raw EEG | everything (~1–3k params) | [[lawhern2018eegnet]], [[song2022eeg]], [[wang2024cbramod]] |

## Open threads
- Protocol-matched comparison: Riemannian/FBCSP vs foundation models (also in [[interests]] *Open questions*). Source to add: Lotte et al. 2018 (Roy ref [105]; also [[varbu2022past]] ref [22], which cites it for the need for user-adaptive classifiers, §5.9).

## Sources
- [[kontras2026neuroatlas]]: NeuroAtlas; the hand-crafted brain-age model wins; no classical BCI pipeline; end-to-end EEGNet vs frozen FMs.
- [[chen2026benchmarking]]: EEG-Arena; 24 DL baselines + YASA, no CSP/Riemannian.
- [[kuruppu2026eeg]]: review of 10 EEG-FMs; how rarely they test against classical baselines (Fig. 4a).
- [[lawhern2018eegnet]]: matched EEGNet vs xDAWN+RG / FBCSP comparison across 4 paradigms, within and cross-subject.
- [[roy2019deep]]: meta-analysis of DL vs traditional baselines, 2010–2018 (§3.7, §4.5).
- [[chaddad2023electroencephalography]]: catalogue of classical classifiers.
- [[varbu2022past]]: frequency of features and classifiers in 2009–2019 BCI papers.
- [[song2022eeg]]: FBCSP vs DL on motor imagery.
- [[wang2024cbramod]]: modern baseline set *(Table 10 only so far)*.
