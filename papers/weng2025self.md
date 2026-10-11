---
citekey: weng2025self
title: "Self-supervised Learning for Electroencephalogram: A Systematic Survey"
authors: [Weining Weng, Yang Gu, Shuai Guo, Yuan Ma, Zhaohua Yang, Yuchen Liu, Yiqiang Chen]
year: 2025
venue: "ACM Computing Surveys 57(12):1–38"
doi: "10.1145/3736574"
arxiv: "2401.05446"
pmid: ""
field: eeg
paper_type: review
task: "self-supervised representation learning for EEG (sleep, pathology, seizure, emotion, motor imagery, speech/image decoding)"
datasets: [Sleep-EDF, SHHS, MASS, ISRUC, PhysioNet 2018, TUAB, TUSZ, CHB-MIT, SEED, DEAP, BCI IV-2a, EEGMMI]
n_subjects:
n_channels:
model_type: ""
eval_protocol: ""
main_metric: ""
main_result: ""
code_available: false
read_depth: full
concepts: [self-supervised-pretraining, evaluation-protocols, channel-heterogeneity, sleep-staging, emotion-recognition, seizure-detection, time-frequency-analysis]
---

# Self-supervised learning for EEG: a systematic survey (Weng et al., 2025)

## TL;DR
A taxonomy of ~70 EEG self-supervised methods (≈2019–2023) by pretext task: predictive, generative, contrastive, hybrid. It is a catalogue of *how* the methods work (pretext task, loss, backbone, training mode), with **no performance numbers**, and it stops just before the foundation-model era (no BIOT, LaBraM, CBraMod).

*Read from arXiv v1 (9 Jan 2024, 35 pp.); the ACM CSUR version (2025) has 38 pp. and may add material. (p. N) = arXiv PDF pages.*

## Research question
Survey and categorize SSL frameworks for EEG, the downstream tasks and datasets they use, and future directions (§1, pp. 3–4).

## Data & preprocessing
- Review, not a systematic search: no databases, search terms, dates or PRISMA flow are given, despite the title. 🤖
- Dataset table: 31 datasets used in SSL-EEG work, with subjects, sampling rate, channels and labels (Table 5, p. 28). Largest by subjects: ASD dataset 4,899, TUAB 2,329, PhysioNet Challenge 2018 1,983 (sleep, 6 ch).
- Pattern noted: emotion and motor-imagery sets have many channels (>30), sleep sets few channels but long recordings, pathology sets more subjects (p. 28).

## Method (the taxonomy)
**Why SSL:** labels are expensive (need experts), rare states (seizures, abnormal emotions) are hard to collect, and labels are inconsistent: self-reports are subjective and experts disagree on the same segment (§1, pp. 2–3).

**Three training modes** (§2.2, Eqs. 1–3, p. 6):
- **PT** (pre-train, then fine-tune encoder + head);
- **CT/JT** (joint loss: pretext + downstream; the pretext acts as a regularizer);
- **UT** ("unsupervised-train"): the encoder is frozen and only the head is trained. This is linear probing / frozen-embedding evaluation.

**Four families** (Fig. 3, p. 7):
1. **Predictive** (§3, Table 1: 15 methods): classify a pseudo-label made from the data.
   - Spatial: channel jigsaw; channel-correlation prediction; replaced-channel detection (MBrain) (§3.1).
   - Temporal: **relative positioning** (are two windows close in time?) and **temporal shuffling** (Banville et al. 2021, ref [13]); trend and time-shift prediction (§3.2).
   - Transformation: predict which band was removed (δ/θ/α/β/γ), or which augmentation was applied (noise, scaling, sign flip X→−X, segment flip, sub-segment shuffle, time warp) (§3.3).
   - "Simple", few parameters, but "may need help to learn general representations" (§3.4, p. 12).
2. **Generative** (§4, Table 2: 20 methods): reconstruct or generate.
   - Autoencoders; **signal-level masked reconstruction** (MAEEG); **embedding-level masked prediction** with a contrastive loss (BENDR, wav2vec-style) (§4.1).
   - Multi-domain: mask/reconstruct wavelet time–frequency maps with a ViT; per-band reconstruction (Wavelet2vec); Fourier magnitude + phase targets (neuro2vec); graph-node reconstruction (§4.2).
   - GANs, mostly for data augmentation ("SA" mode) (§4.3).
   - More parameters, "can learn more efficient features" (§4.4).
3. **Contrastive** (§5, Table 3: 34 methods), called "the most widely used" (§5, p. 17).
   - **CPC** (predict future window embeddings; bidirectional variant) (§5.1).
   - SimCLR-style augmentation pairs; negative-free variants (BYOL, Barlow Twins, ContraWR) (§5.2). Suggested amplitude scaling range 0.5–2 (p. 20).
   - Spatial: region shuffling, graph node dropping / sub-graphs, "meiosis" (swap channel halves between two trials of the same stimulus) (§5.3).
   - Composite: time vs frequency views (TF-C, mulEEG), multi-view CPC (TS-TCC), scalp vs dipole views (§5.4).
   - Task-oriented: **EEG–image and EEG–speech CLIP-style alignment** (NICE-EEG; Défossez 2023), and cross-subject contrast using age (§5.5).
4. **Hybrid** (§6, Table 4: 6 methods): multi-task losses; risk of gradient interference between pretext tasks (p. 25).

## Evaluation
- None of its own. Training mode per method is tabulated (PT / UT / CT / SA) (Tables 1–4).

## Results (with locations)
- **Downstream tasks:** sleep staging dominates. 15 of 34 contrastive methods include sleep (Table 3), then emotion, seizure/pathology, motor imagery, speech/image decoding (§7).
- **Backbones:** mostly CNN (also LSTM/GRU); Transformers/ViT in newer generative and composite methods; GNNs for spatial methods (Tables 1–3).
- Contrastive methods are judged "the most effective, with fewer parameters"; badly chosen sample pairs "may yield counterproductive results" (§5.6, p. 25). No numbers are given for this.
- **Future directions** (§8, pp. 28–29): EEG-specific pretext tasks rather than CV/NLP copies; knowledge-driven SSL for interpretability; graph-based SSL; **SSL over heterogeneous EEG** (different channels, devices, sampling rates, tasks); multimodal SSL with ECG/EMG/EOG.

## Limitations (reported)
- Most pretext tasks are "straightforward extension[s]" of CV/NLP ones that "ignore the intrinsic characteristics of EEG" (§8, p. 28).
- SSL representations lack "theoretical foundation and neural knowledge", so they lack generalization and interpretability (§8, p. 28).

## Assessment 🤖
- 🤖 **No quantitative comparison.** Contribution (1) promises "the performance of the SSL" (p. 3), but no table reports a score, a gain over supervised training, or a protocol. It can't answer whether SSL helps, or by how much (Q7). It is a map of method designs.
- 🤖 **Snapshot ends at the start of stage 5.** BENDR (2021) is the only large-corpus model. BIOT (2023), LaBraM, CBraMod and EEGPT are absent (v1 predates or misses them). For Q4 it covers the 2019–2023 SSL stage, not foundation models.
- 🤖 The UT (frozen-encoder) mode is common in the tables. That is relevant to Q7: a frozen probe was a standard check before LaBraM, which then found probes weak ([[jiang2024large]] Table 10).
- 🤖 Clinical precision is low: Wake is called the "weak stage" and REM listed as "RAM" (§7 p. 27; Table 5); EEGMMI is given 105 subjects (109 in the dataset). Use the table for orientation, not for facts.
- 🤖 The claim "contrastive is most effective" is unsupported here, and the vault still has no matched contrastive-vs-masked comparison. Within masked modeling alone, the best target already depends on the task ([[jiang2024large]] App. G).
- 🤖 Relative positioning works because nearby windows share a label. That is the same property that makes window-level random splits leak ([[evaluation-protocols]]).

## Concepts
- [[self-supervised-pretraining]]: the main subject; the taxonomy and the three training modes.
- [[evaluation-protocols]]: PT vs UT (frozen probe) vs joint training as evaluation modes.
- [[channel-heterogeneity]]: "SSL for heterogeneous EEG" as a future direction (§8).
- [[sleep-staging]]: the most common SSL downstream task (Table 3).
- [[emotion-recognition]]: subjective labels as a motivation; spatial / meiosis contrastive methods.
- [[seizure-detection]]: MBrain, Wavelet2vec, EEG-CGS, BrainNet (SEEG).
- [[time-frequency-analysis]]: wavelet / Fourier reconstruction targets (§4.2).

## Related papers
- [[kuruppu2026eeg]]: the follow-on review of foundation models (to Sep 2024); cites this survey (ref [26]) as architecture/objective-focused.
- [[jiang2024large]]: LaBraM, the next step (masked token prediction at scale), not covered here.
- [[wang2024cbramod]]: later foundation model; not covered.
- [[yang2023biot]]: BIOT is absent, but its author's ContraWR (ref [146], sleep, negative-free contrastive) is included.
- [[roy2019deep]]: the earlier RBM/DBN/autoencoder pretraining wave (2010–2014). This survey's autoencoder entries continue it.
- [[lawhern2018eegnet]]: SPP-EEGNet (ref [87]) builds SSL on EEGNet; the survey does not compare SSL with it.
- [[li2022eeg]]: same motivation (subjective emotion labels); it predicted large pretrained models.

## Q&A notes
