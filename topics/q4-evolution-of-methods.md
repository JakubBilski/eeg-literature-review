---
slug: q4-evolution-of-methods
kind: hub
status: stub
updated: 2026-10-11
---

# q4-evolution-of-methods

> How have EEG analysis methods evolved: classical signal processing → ML → deep learning → foundation models?

## Current answer
*Signal-processing primer:* the ordered steps (filtering → reference → artifacts → epochs → features → classifier) are mapped in [[eeg-preprocessing-pipeline]], with per-step notes [[digital-filtering]], [[time-frequency-analysis]], [[common-spatial-patterns]].

Rough stages as described by vault papers (to be confirmed by the review seeds):
1. **Hand-crafted features + classifier:** CSP and filter-bank CSP for motor imagery, CCA for SSVEP, wavelet features, then SVM or MLP. Criticized as task-specific, with features and classifier optimized separately [[song2022eeg]] (§I).
   - The classical pipeline in full: acquisition → **denoising** (regression, ICA/PCA, CCA, wavelets, EMD) → **feature engineering** (time–frequency, higher-order spectra, nonlinear/entropy measures) → classifier (SVM most common; KNN, RF, LDA) [[chaddad2023electroencephalography]] (Fig. 2, §2.2–2.5).
   - **What was actually used in BCI, 2009–2019** (202 papers): features PSD 18%, Fourier 16%, CSP 14%; classifiers LDA 31%, SVM 21%, CNN only 4% [[varbu2022past]] (Figs. 12–13). This confirms stage 1 was the norm in BCI up to ~2019.
   - Early DL often kept this pipeline and swapped only the classifier, feeding CNNs denoised, feature-engineered EEG re-formatted as 2D/3D "images" [[chaddad2023electroencephalography]] (§2.5.2, Fig. 4).
   - How much DL beat it (median +5.4% accuracy, 2010–2018, biased upward), and the Riemannian / LDA / CSP baselines explained → [[classical-ml-baselines]].
   - **Early DL, 2010–2014: DBNs and fully connected nets**, often trained in two steps: unsupervised feature learning (RBM/DBN/autoencoder), then a classifier, typically on frequency-domain features. Their share declined after 2014 [[roy2019deep]] (§3.5.1–3.5.2, Fig. 10b–c, pp. 17–19). 🤖 This is the first, pre-SSL "pretraining" wave.
2. **End-to-end CNNs:** since 2015, the most used architecture (40% of 156 DL papers to mid-2018), mostly on raw EEG, mostly shallow (≤10 layers in 128 of 156 papers). CNN+RNN combinations were rising [[roy2019deep]] (§3.5.1, pp. 17–18). ConvNet, EEGNet (temporal + spatial convolutions), beating FBCSP [[song2022eeg]] (§I, Table II).
3. **RNN/LSTM, then Transformers:** for long-range dependencies. RNNs can't be parallelized and lose memory over long spans [[song2022eeg]] (§I).
4. **CNN + Transformer hybrids** trained per subject: EEG Conformer (2022), +10.9 pts over FBCSP on BCI IV-2a [[song2022eeg]] (Table II). → [[cnn-transformer-hybrid]]
5. **Self-supervised pretraining / foundation models:** BENDR (2021, contrastive) → BIOT (2023) → LaBraM (2024: 2,500 h, masked token prediction, montage-agnostic) [[jiang2024large]] (§1, App. A). → [[self-supervised-pretraining]]
- 🤖 What drives the shift: limited labeled data and montage differences push toward pretraining on pooled unlabeled data ([[jiang2024large]] §1). The per-subject small-data paradigm ([[song2022eeg]]) is what this replaces.
- **Today's supervised baselines** in foundation-model papers (EEGNet, Conformer, ... BIOT, LaBraM) and how small the gaps can be → [[classical-ml-baselines]], [[eeg-depression-detection]].

## Comparisons
| | Conformer (2022) | LaBraM (2024) |
|---|---|---|
| training | from scratch, per subject | pretrain on 2,535 h, fine-tune |
| montage | fixed (spatial conv) | any (channel patches + electrode embeddings) |
| eval | within-subject | cross-patient (TUAB/TUEV) |
| params | not stated (+17.6% from attention) | 5.8M–369M |

## Open threads
- Confirm the stages against the systematic reviews. *Stages 1–2 confirmed (2026-10-11)* by [[roy2019deep]]: DBN/FC until 2014, CNNs from 2015, a median +5.4% over classical baselines. It also added the unsupervised-pretraining wave of 2010–2014. Stages 3–5 still need [[weng2025self]] (needs a manual PDF). [[chaddad2023electroencephalography]] confirms stage 1 and early CNNs, but has no Transformers or SSL.
- Where do graph neural networks and Riemannian methods fit? *Partial (2026-10-11):* in emotion recognition, GNNs over electrode graphs (fixed connectivity like PLV, or learned adjacency as in DGCNN/RGNN, 2018–2020) were a main DL branch alongside CNN-on-electrode-grid, CNN-LSTM hybrids and adversarial domain adaptation. A Riemannian-tangent-space + LSTM fusion network also appears [[li2022eeg]] (§4.3–4.5, Table 4). Stage 2–3 in emotion therefore looked more like "DL on hand-crafted features (DE per band)" than raw end-to-end.

## Sources
- [[roy2019deep]]: systematic review of 156 DL-EEG papers, 2010–2018: architecture trends, DL-vs-classical meta-analysis (→ [[classical-ml-baselines]]).
- [[li2022eeg]]: emotion-recognition method routes 2016–2022 (Fig. 7): features + SVM → DBN/CNN/GNN on feature maps → end-to-end CNN/RNN → domain adaptation; proposes large pretrained EEG models (p. 29).
- [[varbu2022past]]: method frequencies in BCI 2009–2019 (stage 1 in practice).
- [[chaddad2023electroencephalography]]: the classical pipeline in detail (denoising, features, SVM-era classifiers).
- [[song2022eeg]]: the classical → CNN → Transformer narrative (§I–II).
- [[jiang2024large]]: SSL lineage (App. A).
