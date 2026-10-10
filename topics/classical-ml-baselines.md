---
slug: classical-ml-baselines
kind: synthesis
status: growing
updated: 2026-10-10
---

# classical-ml-baselines

> What are the non-deep-learning baselines for EEG classification, and how much has DL actually beaten them?

## Current answer
- **The classical recipe:** hand-crafted features (band power, entropy, wavelet coefficients) feed a shallow classifier: SVM, KNN, random forest, LDA, naive Bayes. SVM is the most common [[chaddad2023electroencephalography]] (§2.5.1, Table 4).
- **Motor imagery standard:** filter-bank CSP (FBCSP). Band-pass filters → spatial filters learned per subject → linear classifier. It reaches 67.75% on BCI IV-2a vs 78.66% for Conformer [[song2022eeg]] (Table II).
- **DL gain over classical pipelines (2010–2018):** 67.9% of 156 DL papers had a traditional baseline (§3.7.1, p. 21). The median accuracy gain was +5.4% (IQR 9.4%), with only 4 negative values (p. 24) [[roy2019deep]].
- **Why that gain is overstated:** there is publication bias, and many baselines were weak (spectral features + linear classifier). Only 2 studies used Riemannian pipelines, "although these methods have set a new state-of-the-art in multiple EEG classification tasks" [[roy2019deep]] (§4, p. 28).
- **Today's supervised baselines in foundation-model papers** are deep, not classical: EEGNet, Conformer, SPaRCNet, ContraWR, etc. On Mumtaz2016, EEGNet (3k params) gets 0.923 vs 0.956 for CBraMod [[wang2024cbramod]] (Table 10). 🤖 Riemannian / FBCSP baselines are missing from these comparisons, so the vault can't yet tell how much pretraining beats a strong classical pipeline.
- **DL in that period:** CNN 41%, RNN ~14%, autoencoders ~13%, CNN+RNN 7% of papers [[roy2019deep]] (§3, p. 17).

## Glossary (🤖 standard definitions, no vault source yet; Lotte 2018 should cover them)
- **LDA = Linear Discriminant Analysis** (Fisher), *not* latent Dirichlet allocation. It assumes each class is Gaussian with a shared covariance and finds the projection that maximizes between-class over within-class variance, giving a linear decision boundary. In BCI it is usually used with covariance *shrinkage* because trials are few. It is cheap and hard to overfit.
- **CSP (common spatial patterns):** learns channel weightings (spatial filters) whose output variance differs most between two classes. It is a supervised cousin of PCA/ICA.
- **Riemannian methods:**
  - **Input:** each trial (channels × time) is summarized by its channel covariance matrix C (C × C, symmetric positive-definite, SPD). These matrices live on a curved manifold, not a flat vector space.
  - **Distance:** the usual one is the affine-invariant Riemannian distance, δ(A, B) = sqrt(Σᵢ log² λᵢ), where λᵢ are the eigenvalues of A⁻¹B. Its key property: δ(WAWᵀ, WBWᵀ) = δ(A, B) for any invertible W. Any fixed linear re-mixing of channels, such as volume conduction or a different reference, leaves distances unchanged.
  - **Classifiers:** not only kNN.
    - *MDM* (minimum distance to mean): a nearest-centroid classifier using Riemannian (Fréchet) class means.
    - *Tangent-space mapping:* flatten the matrices at a reference point (e.g. the mean), vectorize, then use any vector classifier (logistic regression, SVM, LDA).
    - kNN with δ is possible but less common.
  - **Transfer:** "re-centering" each subject's or session's covariances to a common reference is a simple cross-subject adaptation trick.

## Comparisons
| baseline | input | learned part | where seen |
|---|---|---|---|
| band power + SVM/LDA | spectral features | classifier only | [[chaddad2023electroencephalography]] |
| FBCSP | band-passed raw EEG | spatial filters + linear classifier | [[song2022eeg]] (Table II) |
| Riemannian (MDM / tangent space) | covariance matrices | class means / linear classifier | [[roy2019deep]] (§4) *(cited only)* |
| EEGNet | raw EEG | everything (3k params) | [[song2022eeg]], [[wang2024cbramod]] |

## Open threads
- Protocol-matched comparison: Riemannian/FBCSP vs foundation models (also in [[interests]] *Open questions*). Source to add: Lotte et al. 2018 (Roy ref [105]).

## Sources
- [[roy2019deep]]: meta-analysis of DL vs traditional baselines (§3.7, §4) *(selected sections)*.
- [[chaddad2023electroencephalography]]: catalogue of classical classifiers.
- [[song2022eeg]]: FBCSP vs DL on motor imagery.
- [[wang2024cbramod]]: modern baseline set *(Table 10 only so far)*.
