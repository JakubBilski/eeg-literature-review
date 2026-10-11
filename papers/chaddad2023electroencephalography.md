---
citekey: chaddad2023electroencephalography
title: "Electroencephalography Signal Processing: A Comprehensive Review and Analysis of Methods and Techniques"
authors: [Ahmad Chaddad, Yihang Wu, Reem Kateb, Ahmed Bouridane, Chang-Hwan Im, Yvonne Tran]
year: 2023
venue: "Sensors 23(14):6434"
doi: "10.3390/s23146434"
arxiv: ""
pmid: "37514728"
field: eeg
paper_type: review
task: "general EEG signal processing (pipeline overview; applications incl. epilepsy, motor imagery, emotion, sleep, stroke, depression)"
datasets: [DEAP, SEED, BCI Competition IV 2a, Bonn, CHB-MIT, Siena, Sleep-EDF]
n_subjects:
n_channels:
model_type: ""
eval_protocol: ""
main_metric: ""
main_result: ""
code_available: false
read_depth: full
concepts: [independent-component-analysis, time-frequency-analysis, signal-quality-and-noise, frequency-bands, evaluation-protocols, consumer-grade-eeg-devices, channel-heterogeneity, eeg-preprocessing-pipeline, linear-discriminant-analysis, sleep-staging]
---

# EEG Signal Processing review (Chaddad et al., 2023)

## TL;DR
A broad, textbook-style review of the **classical EEG pipeline** (acquisition → denoising → feature engineering → classification), with pseudocode for the main denoising methods. It is a good map of the vocabulary but shallow on evidence, and its tables mix incomparable accuracies.

## Research question
Survey the whole EEG processing pipeline, compare methods at each stage, and list challenges and future trends (Abstract; §1).

## Data & preprocessing
- A narrative review. Databases are named ("major scientific and engineering databases"), but no search protocol or counts are given (Abstract; §1).
- Commonly used datasets (Table 3): DEAP (32 subjects, emotion, 128 Hz), SEED (15, emotion, 200 Hz), BCI IV-2a (9, 250 Hz), Bonn/Andrzejak (10, seizure, 173.86 Hz), CHB-MIT/Shoeb (23, seizure, 256 Hz), Siena/Detti (14, seizure, 512 Hz), among others.

## Method (the pipeline it describes, Fig. 2, Algorithm 1)
1. **Acquisition** (§2.1): invasive vs non-invasive; research systems are wired and heavy, hence the push to portable devices (Emotiv EPOC 14 ch, Muse 4 ch at AF7/AF8/TP9/TP10 with an Fpz reference).
2. **Denoising** (§2.2): artifacts come from eyes (EOG), heart (ECG), muscle (EMG) and the environment.
   - *Regression* on a simultaneously recorded EOG channel. Problem: "bidirectional contamination", because the EOG channel also picks up brain signal (§2.2.1).
   - *Blind source separation*: ICA (X = AS, i.e. unmix the channels into independent sources, drop the artifact sources, remix) and PCA (§2.2.2).
   - *CCA*: better than ICA for muscle artifacts, because muscle noise has lower autocorrelation than brain activity (§2.2.3).
   - *Wavelet transform* (DWT: threshold the detail coefficients) (§2.2.4). *EMD* (adaptive decomposition into oscillatory modes) (§2.2.5).
   - Hybrids are common, e.g. wavelet+ICA, EEMD+CCA (Table 2).
3. **Denoising metrics**: MSE, RMSE, SNR, PRD against a "true" signal (§2.3, Eq. 8).
4. **Feature engineering** (§2.4): time–frequency analysis, higher-order spectra, and nonlinear dynamics (Lyapunov exponent, fractal dimension, sample/permutation entropy, Lempel–Ziv complexity).
5. **Classification** (§2.5): traditional ML (SVM, KNN, RF, LDA, NB; "SVM … an important classifier", §2.5.1) and DL (CNNs on 2D/3D re-formatted EEG, CNN+RNN for sleep) (§2.5.2, Fig. 4).

## Results (with locations)
- **Frequency bands:** delta 0.5–4 Hz (deep sleep), theta 4–8 (relaxation, meditation), alpha 8–13 ("most noticeable when the eyes are closed"), beta 13–30 (active attention), gamma >30 Hz (higher cognition) (§2.1). → [[frequency-bands]]
- **Channel names** encode location: position relative to the midline and front-back distance (§2.1). Fig. 3 shows 14 Emotiv channels (AF3 … AF4).
- **Origin of the signal**: "the spontaneous biological potential of the brain on the scalp", reflecting "the macroscopic activity of the brain surface", from "clusters of brain cells" (§1, §2.1). This is the depth of the physiology given.
- The ERASE variant of ICA removes 26% more EMG than plain ICA (§2.2.2).
- Example accuracies from cited studies: KNN 88.57% on binary motor imagery (§2.5.1, Table 4); CNN 98% seizure detection (Table 6); AlexNet 93.33% for sleep disorders (Table 6); CNN+RNN 79.7% sleep staging from Fp1/Fp2 (§2.5.2).
- **DeprNet (depression):** 99.37% with a recording-level split vs 91.4% with a subject-level split (Table 6). → [[evaluation-protocols]]
- Federated learning reached 91.10% on Sleep-EDF (§3).

## Limitations (reported) — the field's challenges (§3)
- Noise and artifacts; **non-stationarity** (statistics change over time).
- **Volume conduction**: each electrode sums many brain sources, so it's hard to locate where a signal comes from.
- **Reference electrode problem**: EEG is a potential *difference* to a reference, and the data change with the choice of reference.
- **Between-subject variability** (skull thickness, conductivity, anatomy).
- Interpretability of DL models; data heterogeneity across devices (domain adaptation is proposed); privacy/GDPR (federated learning is proposed).

## Assessment 🤖
- 🤖 **Useful as a vocabulary map, weak as evidence.** It has no systematic search protocol, and the accuracies in Tables 4–6 come from different datasets, splits and class counts, so they can't be compared. The DeprNet row (99.37% vs 91.4%) shows by itself how much the split matters.
- 🤖 **Errors in Table 3:** Ang [115] (filter-bank CSP on BCI IV-2a/2b) is labelled "Emotion recognition", but it's motor imagery. Treat the table as approximate.
- 🤖 **Physiology is thin.** It never says which cells produce the signal (the textbook answer is the synchronized postsynaptic currents of cortical pyramidal neurons), why only cortex near the surface is visible, or how volume conduction limits spatial resolution. Q1 still needs a proper source. The candidate it cites is Lopes da Silva, "EEG and MEG: Relevance to neuroscience" (Neuron 2013, ref [3]).
- 🤖 **The DL coverage is pre-2022 in spirit.** No Transformers and no self-supervised pretraining. EEGNet, Conformer and the foundation models are absent. It shows the "classical pipeline + CNN" view that [[song2022eeg]] and [[jiang2024large]] move beyond.
- 🤖 For an ML reader, the main takeaway is that classical EEG work spent most of its effort on **denoising + hand-crafted features**. Deep learning claims to make this end-to-end (§3), and foundation models go further by learning the features from unlabeled data.

## Concepts
- [[eeg-preprocessing-pipeline]]: the classical pipeline: denoising → features → classifier (Fig. 2, §2.2–2.5).
- [[signal-quality-and-noise]]: the main source in the vault on artifact types and classical denoising (regression, ICA/PCA, CCA, wavelets, EMD).
- [[frequency-bands]]: defines the five canonical bands and their typical states.
- [[sleep-staging]]: CNN+RNN reaches 79.7% on Fp1/Fp2 sleep staging (§2.5.2); Sleep-EDF is the listed sleep dataset (Table 3).
- [[linear-discriminant-analysis]]: one of the traditional classifiers (SVM, KNN, RF, LDA, NB); SVM, not LDA, is named the key one (§2.5.1).
- [[evaluation-protocols]]: the DeprNet recording vs subject split (Table 6); tables mix protocols.
- [[consumer-grade-eeg-devices]]: Emotiv EPOC and Muse as portable examples (§2.1).
- [[channel-heterogeneity]]: device heterogeneity across datasets; domain adaptation as the proposed remedy (§3).
- [[time-frequency-analysis]]: wavelets and EMD for denoising (§2.2.4–2.2.5) and as a feature family (§2.4.1).
- [[independent-component-analysis]]: main blind-source-separation denoiser (§2.2.2, Algorithm 3).

## Related papers
- [[song2022eeg]]: Conformer replaces this review's hand-crafted feature stage with end-to-end conv + attention.
- [[jiang2024large]]: LaBraM predicts Fourier amplitude/phase, the learned counterpart of the time–frequency features here.
- [[sabio2024scoping]]: covers the same consumer devices (Emotiv, Muse) in much more depth.
- [[niso2022wireless]]: works through the lab-vs-portable trade-off (§2.1 here) spec by spec for 48 wireless devices.
- [[roy2019deep]]: the systematic DL-for-EEG review that this one lacks. *(not yet read)*

## Q&A notes
- 2026-10-10 **Q:** What does ICA "unmixing" mean, and is there a spatial prior? **A:** It estimates W ≈ A⁻¹ in X = AS (Eq. 2) by maximizing non-Gaussianity (Algorithm 3). There is no spatial prior, only independence. Components are labelled afterwards by eye (§2.2.2). → [[independent-component-analysis]]
- 2026-10-10 **Q:** Are wavelets and EMD like Fourier analysis? **A:** They are relatives with time localisation. Wavelets use a fixed multi-scale filter bank (§2.2.4); EMD is a data-driven decomposition (§2.2.5). → [[time-frequency-analysis]]
- 2026-10-10 **Q:** Is depression really that easy to detect? **A:** DeprNet drops from 99.37% to 91.4% with a subject split (Table 6). One subject-split benchmark (Mumtaz2016) still gives 0.92–0.96, but on 10 test subjects. Treated as open. → [[eeg-depression-detection]]
- 2026-10-10 **Q:** What models are typical (the ML baseline)? **A:** Here: SVM, KNN, RF and LDA on hand-crafted features (§2.5.1). For the measured DL gain over these (median +5.4%) and the Riemannian caveat, see [[q4-evolution-of-methods]].
