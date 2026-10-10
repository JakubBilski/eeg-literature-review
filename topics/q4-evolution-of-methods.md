---
slug: q4-evolution-of-methods
kind: hub
status: stub
updated: 2026-10-10
---

# q4-evolution-of-methods

> How have EEG analysis methods evolved: classical signal processing → ML → deep learning → foundation models?

## Current answer
Rough stages as described by vault papers (to be confirmed by the review seeds):
1. **Hand-crafted features + classifier:** CSP and filter-bank CSP for motor imagery, CCA for SSVEP, wavelet features, then SVM or MLP. Criticized as task-specific, with features and classifier optimized separately [[song2022eeg]] (§I).
2. **End-to-end CNNs:** ConvNet, EEGNet (temporal + spatial convolutions), beating FBCSP [[song2022eeg]] (§I, Table II).
3. **RNN/LSTM, then Transformers:** for long-range dependencies. RNNs can't be parallelized and lose memory over long spans [[song2022eeg]] (§I).
4. **CNN + Transformer hybrids** trained per subject: EEG Conformer (2022), +10.9 pts over FBCSP on BCI IV-2a [[song2022eeg]] (Table II). → [[cnn-transformer-hybrid]]
5. **Self-supervised pretraining / foundation models:** BENDR (2021, contrastive) → BIOT (2023) → LaBraM (2024: 2,500 h, masked token prediction, montage-agnostic) [[jiang2024large]] (§1, App. A). → [[self-supervised-pretraining]]
- 🤖 What drives the shift: limited labeled data and montage differences push toward pretraining on pooled unlabeled data ([[jiang2024large]] §1). The per-subject small-data paradigm ([[song2022eeg]]) is what this replaces.

## Comparisons
| | Conformer (2022) | LaBraM (2024) |
|---|---|---|
| training | from scratch, per subject | pretrain on 2,535 h, fine-tune |
| montage | fixed (spatial conv) | any (channel patches + electrode embeddings) |
| eval | within-subject | cross-patient (TUAB/TUEV) |
| params | not stated (+17.6% from attention) | 5.8M–369M |

## Open threads
- Confirm the stages against the systematic reviews: [[roy2019deep]], [[chaddad2023electroencephalography]] (downloaded, not yet read), [[weng2025self]] (needs manual download).
- Where do graph neural networks and Riemannian methods fit?

## Sources
- [[song2022eeg]]: the classical → CNN → Transformer narrative (§I–II).
- [[jiang2024large]]: SSL lineage (App. A).
