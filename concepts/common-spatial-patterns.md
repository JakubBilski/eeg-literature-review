---
slug: common-spatial-patterns
fields: [eeg, signal-processing, ml]
familiarity: introduced     # human's level: new | introduced | understood | skip
---

# common-spatial-patterns

## Field-neutral description
A supervised way to combine many sensors into a few "virtual sensors" for a two-class problem. Each virtual sensor is a weighted sum of the real ones, chosen so that its signal power is as large as possible in one class and as small as possible in the other. The power of these few virtual sensors then serves as features.

## Synonyms by community
- **EEG:** CSP, spatial filter, filter-bank CSP (FBCSP), CSP patterns/filters, "log-variance features"
- **Neuroscience / clinical:** —
- **Signal processing:** generalized eigendecomposition of two covariance matrices, joint diagonalization, beamforming-like spatial filter
- **General ML:** supervised linear dimensionality reduction (cf. PCA, which is unsupervised, and LDA, which separates means rather than variances); a 1×1 conv over channels with weights from a closed-form eigenproblem

## How it works (🤖 textbook material, ML-oriented)
- **Input:** band-passed trials (e.g. 8–30 Hz), each a matrix of channels × time. Band-passing matters because CSP works on *power*, and power in which band is what changes ([[digital-filtering]]).
- **Step 1, covariance per class:** average the channel×channel covariance matrix over trials of class A (Σ_A) and of class B (Σ_B). The diagonal is power per channel; the off-diagonals are how channels co-vary.
- **Step 2, generalized eigenproblem:** solve Σ_A w = λ (Σ_A + Σ_B) w. Each eigenvector w is a spatial filter, i.e. a weight per channel. λ near 1 means the filtered signal has high power in A and low in B; λ near 0 means the opposite.
- **Step 3, keep the extremes:** take the k filters with the largest λ and the k with the smallest (k = 2–3 per side is typical).
- **Step 4, features:** for each trial, apply the filters, take the variance (= band power) of each virtual channel, then log it. Feed the 2k numbers to [[linear-discriminant-analysis|LDA]].
- **Why it helps:** one electrode picks up a blur of many sources plus noise (volume conduction, see [[independent-component-analysis]]). A learned weighted sum can cancel shared noise and emphasize the part that differs between classes. For left vs right hand motor imagery, the top filters focus on C3 vs C4 regions ([[bci-paradigms]]).
- **Filters vs patterns:** the *filter* w is what you multiply the data by. The *pattern* (columns of the inverse) shows how the underlying source projects onto the scalp. Only patterns are physiologically interpretable; filters also contain noise-cancelling weights. MNE plots patterns.
- **Weaknesses** (Xie, cited in [[varbu2022past]] §5.8): "sensitive to noise and requires multiple electrodes". 🤖 Also: it overfits with few trials, so it needs covariance regularization (shrinkage). It is two-class (multi-class needs one-vs-rest). It assumes the discriminative information is in power, not in waveform timing.
- **Filter-bank CSP (FBCSP):** run CSP separately in several frequency bands (4–8, 8–12, … Hz), pool the features, and select the best. It was the motor imagery standard before deep learning: 67.75% on BCI IV-2a vs 78.66% for Conformer [[song2022eeg]] (Table II). EEGNet was designed to mimic it with temporal convs (filter bank) followed by depthwise spatial convs (spatial filters) [[lawhern2018eegnet]] (§1).

## Papers
- [[varbu2022past]]: CSP is the third most common BCI feature (18/126 papers) (Fig. 12). It "has a good effect when applied to EEG data based on motor imagination and does not require the selection of a specific frequency band in advance" but is noise-sensitive (§5.8).
- [[song2022eeg]]: FBCSP as the classical motor imagery baseline (Table II; §I).
- [[lawhern2018eegnet]]: one-vs-rest FBCSP (9 bands 4–40 Hz, 2 filter pairs per band, elastic-net logistic regression) as the SMR baseline (§2.2.3). Within-subject on BCI IV-2a it ties EEGNet-8,2 (~0.68 vs ~0.68, 4 classes); cross-subject it trails all CNNs (~0.32 vs ~0.40, chance 0.25) (Figs. 3, 5). EEGNet's learned ~12 Hz spatial filters correlate with FBCSP's 8–12 Hz filters up to sign (ρ = 0.93, 0.83; Fig. 8, p. 17).
- Own analysis (2026-10-10): CSP + LDA on EEGMMI, imagined vs executed → [[bci-paradigms]] *Imagined vs executed movement*. A cautionary example: subject 1's top CSP patterns sit at frontal/temporal edge electrodes (eye/muscle artifact territory), not over the motor cortex. CSP maximizes *any* variance difference between classes, artifacts included. Always plot the patterns.
- [[liu2026eeg]]: CSP+LDA as the classical baseline in a 2026 FM benchmark. In within-subject few-shot (~21 trials per class) it beats every FM and DL model on BNCI2014001 4-class MI (60.62 vs CBraMod 50.34, TSception 58.68), and on EEGMat (95.60). Cross-subject (LOSO) it is weakest (38.19 vs 53.03) (Tables 2–3; Supp. Table 16).

## Variants & disagreements
- CSP vs [[riemannian-methods]]: both start from trial covariance matrices. CSP compresses them to a few log-variances, while Riemannian methods classify the whole covariance matrix using a geometry-aware distance. 🤖 The Riemannian approach is often reported stronger; no vault evidence yet.

## Open questions
- How much does CSP lose against EEGNet/Conformer under a *matched, cross-subject* protocol? (→ [[classical-ml-baselines]]) *Partial (2026-10-11):* on BCI IV-2a (9 subjects, 2018) FBCSP ties EEGNet within-subject and loses ~8 pts cross-subject, but both are near chance there [[lawhern2018eegnet]] (Figs. 3, 5). No 2022+ matched comparison yet.

## Related concepts
- [[classical-ml-baselines]]: CSP + LDA is the canonical motor imagery baseline.
- [[linear-discriminant-analysis]]: the classifier usually fed CSP log-variances (LDA separates means, CSP separates variances).
- [[riemannian-methods]]: the other covariance-based family.
- [[independent-component-analysis]]: another linear spatial unmixing, but unsupervised (statistical independence instead of class contrast).
- [[digital-filtering]]: temporal filtering before spatial filtering.
- [[bci-paradigms]]: CSP suits power-based paradigms (motor imagery), not ERP ones.
- [[eeg-preprocessing-pipeline]]: CSP is a feature-extraction step.
