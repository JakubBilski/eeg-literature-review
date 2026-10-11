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
- **Today's supervised baselines in foundation-model papers** are deep, not classical: EEGNet, Conformer, SPaRCNet, ContraWR, etc. On Mumtaz2016, EEGNet (3k params) gets 0.923 vs 0.956 for CBraMod [[wang2024cbramod]] (Table 10). 🤖 Riemannian / FBCSP baselines are missing from these comparisons, so the vault can't yet tell how much pretraining beats a strong classical pipeline.
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
| EEGNet | raw EEG | everything (3k params) | [[song2022eeg]], [[wang2024cbramod]] |

## Open threads
- Protocol-matched comparison: Riemannian/FBCSP vs foundation models (also in [[interests]] *Open questions*). Source to add: Lotte et al. 2018 (Roy ref [105]; also [[varbu2022past]] ref [22], which cites it for the need for user-adaptive classifiers, §5.9).

## Sources
- [[roy2019deep]]: meta-analysis of DL vs traditional baselines, 2010–2018 (§3.7, §4.5).
- [[chaddad2023electroencephalography]]: catalogue of classical classifiers.
- [[varbu2022past]]: frequency of features and classifiers in 2009–2019 BCI papers.
- [[song2022eeg]]: FBCSP vs DL on motor imagery.
- [[wang2024cbramod]]: modern baseline set *(Table 10 only so far)*.
