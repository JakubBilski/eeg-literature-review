---
citekey: song2022eeg
title: "EEG Conformer: Convolutional Transformer for EEG Decoding and Visualization"
authors: [Yonghao Song, Qingqing Zheng, Bingchuan Liu, Xiaorong Gao]
year: 2022
venue: "IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 31 (2023)"
doi: "10.1109/tnsre.2022.3230250"
arxiv: ""
pmid: "37015413"
field: eeg
paper_type: method
task: "motor imagery classification; emotion recognition"
datasets: [BCI Competition IV 2a, BCI Competition IV 2b, SEED]
n_subjects: "9; 9; 15 (per dataset)"
n_channels: "22; 3; 62 (per dataset)"
model_type: "CNN-Transformer hybrid (conv tokenizer + self-attention)"
eval_protocol: "within-subject (session split on 2a/2b; 5-fold CV on SEED)"
main_metric: "accuracy, Cohen's kappa"
main_result: "78.66% mean acc., kappa 0.7155 on BCI IV-2a vs EEGNet 74.50% (Table II)"
code_available: "https://github.com/eeyhsong/EEG-Conformer"
read_depth: full
concepts: [cnn-transformer-hybrid, evaluation-protocols, signal-quality-and-noise, channel-heterogeneity, self-supervised-pretraining]
---

# EEG Conformer (Song et al., 2022)

## TL;DR
A temporal + spatial convolution front end turns raw EEG into a token sequence that a small Transformer then processes. Trained per subject without pretraining, it beat CNN and hand-crafted baselines on two motor-imagery datasets and one emotion dataset, and it is now a standard non-pretrained baseline.

## Research question
Can a compact model combine local features (CNNs) with long-range temporal dependencies (self-attention) for end-to-end decoding of raw EEG, and can what it learns be visualized? (§I, p. 2)

## Data & preprocessing
- **BCI IV-2a:** 9 subjects, 4-class motor imagery, 22 Ag/AgCl electrodes, 250 Hz. Uses the [2, 6] s window of each trial, filtered 4–40 Hz. Session 1 = train, session 2 = test (§IV-A, p. 4).
- **BCI IV-2b:** 9 subjects, 2-class motor imagery, 3 bipolar channels (C3, Cz, C4), 250 Hz. Sessions 1–3 = train, 4–5 = test (§IV-A, p. 4).
- **SEED:** 15 subjects, 3 emotions elicited by film clips, 62 channels, downsampled to 200 Hz. Cut into non-overlapping 1 s windows, 3394 per session, filtered 4–47 Hz, evaluated with 5-fold CV (§IV-A, p. 4).
- Preprocessing: band-pass (6th-order Chebyshev) + z-score using training-set statistics (§III-B, p. 3).
- Augmentation: segmentation & reconstruction (S&R), i.e. time segments of same-class trials are recombined (§IV-B, p. 4).

## Method
- Convolution module: temporal conv (40 kernels, 1×25) → spatial conv across all channels (ch×1) → BatchNorm, ELU → average pooling (1×75, stride 15). Each pooled time step becomes one token (§III-C, p. 3).
- Self-attention module: N = 6 layers, h = 10 heads (§IV-C, p. 5). Classifier: 2 fully connected layers, cross-entropy loss (§III-C, p. 4).
- Interpretability: Grad-CAM on the attention module, plus "Class Activation Topography" (CAT, the CAM-weighted EEG topography) (§IV-H, p. 8).

## Evaluation
- Subject-dependent only (§IV-D, p. 5). Metrics: accuracy and kappa; significance via Wilcoxon signed-rank test (§IV-C, p. 5).
- Baselines: FBCSP, ConvNet, EEGNet, C2CM, FBCNet, DRDA on motor imagery; SVM, GELM, DGCNN, R2G-STNN, RGNN on SEED (§IV-D, p. 5).

## Results (with locations)
- **2a:** 78.66% / κ 0.7155, vs FBCSP 67.75, EEGNet 74.50, FBCNet 76.20 (Table II). That is +10.91 pts over FBCSP (p < 0.01) (§IV-D, p. 5).
- **2b:** 84.63% / κ 0.6926, vs EEGNet 80.48, DRDA 83.98 (Table III).
- **SEED:** 95.30% / κ 0.9295, vs RGNN 94.24 (Table IV).
- Ablation on 2a: removing the Transformer costs −6.02 pts; removing S&R augmentation costs −3.75 pts (both p < 0.01) (§IV-F, Fig. 3, p. 6).
- Depth: going from 0 to 1 attention layer helps significantly; depths 1–15 are within 1.24 pts of each other (n.s.) (§IV-G, p. 6). Number of heads: range ≤1.43 pts (p. 7).
- Pooling kernel (= token length) matters most: growing it from 15 to 45 gives +13.08 pts (p < 0.01) (§IV-G, Fig. 6, p. 7).
- Cost: attention adds 17.6% parameters (§V, p. 9); training takes 0.27 s/epoch on one GPU (p. 6).
- CAT highlights the motor cortex and shows contralateral ERD/ERS for left- vs right-hand imagery (§IV-H, Figs. 8–9, p. 8).

## Limitations (reported)
- Tested only on oscillatory paradigms (motor imagery, emotion), not ERP paradigms (§V, p. 9).
- Parameter count isn't small; the fully connected classifier is heavy (§V, p. 9).
- Trained per subject; cannot use data from other subjects (§V, p. 9).

## Assessment 🤖
- 🤖 **The SEED result is probably optimistic.** Five-fold CV on 1 s windows from a single session puts neighbouring windows of the same film clip in both train and test, which is likely leakage. The baselines it is compared against used different protocols. Treat 95.3% as not comparable across papers. See [[evaluation-protocols]].
- 🤖 The paper doesn't say whether baselines were re-run or copied from the original papers. The 2a/2b comparisons look like the standard session-split protocol, so they are reasonably fair.
- 🤖 The key sensitivity is token length, not depth or heads. That fits the idea that self-attention on EEG needs coarse, denoised tokens ([[signal-quality-and-noise]]). LaBraM's 1 s patches go the same way ([[jiang2024large]]).
- 🤖 Its place in the history: the "CNN front end + Transformer" pattern that pretrained foundation models later scale up. It explicitly skips pretraining because of small data (§IV-E, p. 5).
- 🤖 The spatial conv is tied to a fixed channel count, so the model can't transfer across montages ([[channel-heterogeneity]]).

## Concepts
- [[cnn-transformer-hybrid]]: the paper's core architecture.
- [[evaluation-protocols]]: within-subject only; possible window leakage in the SEED CV.
- [[signal-quality-and-noise]]: pooling large windows before attention to suppress noise.
- [[channel-heterogeneity]]: fixed-montage spatial convolution (the counter-example).
- [[self-supervised-pretraining]]: explicitly not used, citing limited data (§IV-E).

## Related papers
- [[jiang2024large]]: LaBraM keeps a conv encoder before the Transformer but adds large-scale pretraining and montage-agnostic patches.
- [[lawhern2018eegnet]]: inspiration for the conv module and a baseline (Table II). *(not yet read)*
- [[schirrmeister2017deep]]: ConvNet, the other conv-module inspiration and a baseline. *(screening: maybe)*

## Q&A notes
