---
citekey: jiang2024large
title: "Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI"
authors: [Wei-Bang Jiang, Li-Ming Zhao, Bao-Liang Lu]
year: 2024
venue: "ICLR 2024"
doi: ""
arxiv: "2405.18765"
pmid: ""
field: eeg
paper_type: method
task: "abnormal EEG detection; EEG event classification; emotion recognition; gait regression"
datasets: [TUAB, TUEV, SEED-V, MoBI]
n_subjects: ""
n_channels: "variable (one patch per channel per 1 s; ≤256 patches)"
model_type: "Transformer foundation model; masked prediction of VQ neural-tokenizer codes"
eval_protocol: "cross-subject (patient-level split) on TUAB/TUEV; pooled-subject trial split on SEED-V"
main_metric: "balanced accuracy"
main_result: "TUEV bal. acc. 0.6409 (Base) vs BIOT 0.5281; TUAB 0.8140 vs 0.7959 (Tables 1–2)"
code_available: "https://github.com/935963004/LaBraM"
read_depth: full
concepts: [time-frequency-analysis, frequency-bands, self-supervised-pretraining, channel-heterogeneity, cnn-transformer-hybrid, evaluation-protocols, signal-quality-and-noise, bci-paradigms, seizure-detection, emotion-recognition]
---

# LaBraM: Large Brain Model (Jiang, Zhao & Lu, ICLR 2024)

## TL;DR
LaBraM cuts EEG from any montage into 1 s single-channel patches. A neural tokenizer (trained to predict the Fourier spectrum) turns them into discrete codes, and a Transformer is pretrained to predict the codes of masked patches. It was pretrained on about 2,500 h from about 20 datasets and fine-tuned on each task, beating BIOT and others on TUAB/TUEV, most clearly on the 6-class event task.

## Research question
Can LLM-style self-supervised pretraining on large, heterogeneous EEG collections produce one model that adapts to many tasks despite differing channels and lengths, low SNR, and little labeled data? How much data does it need? (§1, pp. 1–3)

## Data & preprocessing
- Pretraining: 2534.78 h from ~20 datasets: public sets (TUH subsets, SEED family, motor imagery, P300, resting state) plus 342.23 h of the authors' own recordings (App. D, pp. 17–18). The 4 downstream datasets are excluded (§3.2, p. 7).
- Preprocessing: band-pass 0.1–75 Hz, 50 Hz notch, resample to 200 Hz, scale by 0.1 mV units (§3.2, p. 7).
- Downstream: **TUAB** (normal/abnormal, 23 ch, 409,455 × 10 s samples) and **TUEV** (6 event classes, 23 ch, 112,491 × 5 s samples) (§3.1, p. 6). **SEED-V** (5 emotions, 20 subjects, 62 ch) and **MoBI** (gait joint-angle regression, 8 subjects, 60 ch) (App. F, p. 19).

## Method
- **Patching:** each channel is cut into non-overlapping 1 s windows (w = 200 samples). Sequences are capped at 256 patches, e.g. 64 ch × 4 s (§2.1, §3.2, pp. 3, 7).
- **Encoder:** a temporal conv encoder per patch, plus learnable temporal and **spatial (electrode) embeddings**, feeds a Transformer with LayerNorm on Q/K and no QKV bias (§2.1, pp. 3–4).
- **Neural tokenizer:** VQ codebook of 8192 × 64 (App. C, Table 3), trained to reconstruct the patch's Fourier **amplitude and phase**. Reconstructing raw signals directly "fails to converge" (§2.2, p. 5).
- **Pretraining:** masked EEG modeling (mask ratio 0.5) that predicts the codebook indices of masked patches, plus "symmetric masking" (the inverse mask is also used) (§2.3, p. 6; App. C).
- Sizes: Base 5.8M / Large 46M / Huge 369M parameters (§3.2, p. 6).

## Evaluation
- TUAB/TUEV follow BIOT's split: the given train/test split, with training *patients* divided 80/20 into train/val. Mean ± std over 5 seeds (§3.2, p. 7).
- Baselines' results are "from Yang et al. (2023a)" (BIOT) (§3.2, p. 7).
- SEED-V: each session's 15 trials split 5:5:5, merged across subjects (App. F, p. 19).

## Results (with locations)
- **TUAB:** Base 0.8140 balanced accuracy / AUROC 0.9022, vs BIOT 0.7959 / 0.8815. Huge reaches 0.8258 / 0.9162 (Table 1, p. 8).
- **TUEV:** Base 0.6409 balanced accuracy / κ 0.6637, vs BIOT 0.5281 / 0.5273. Huge reaches 0.6616 / 0.6745 (Table 2, p. 8).
- **SEED-V:** accuracy 0.4095 (Base) vs BIOT 0.3802. **MoBI:** Base roughly equals ST-Transformer (R² 0.2876 vs 0.2911); Large and Huge are best (Table 6, p. 19).
- Adding the downstream data to pretraining doesn't change results meaningfully (§3.5, Fig. 4, pp. 8–9).
- Scaling: on TUAB, Base pretrained on 500 h beats Base pretrained on 2,500 h. Huge is still improving at 2,500 h, and the authors extrapolate to ≥10k h (§3.6, Fig. 5, p. 9).
- Tokenizer ablation: the VQ tokenizer helps TUEV (0.6409 vs 0.5630 when raw patches are reconstructed), but raw reconstruction is better on TUAB (0.8261) (Table 7, p. 20).
- **Linear probing is weak on TUEV:** 0.3461 balanced accuracy vs 0.6409 with full fine-tuning. On TUAB the gap is small (0.7954) (Table 10, p. 22).
- Dropping spatial embeddings at fine-tuning hurts (TUEV 0.5949). Pretraining doesn't converge without them (App. L, Table 11, p. 22). Training from scratch drops performance "steeply" (App. J, Fig. 8, p. 21).

## Limitations (reported)
- Still far smaller than vision and language foundation models (App. M, p. 22).
- Needs full fine-tuning, which is costly (App. M).
- EEG only, no other modalities (App. M).

## Assessment 🤖
- 🤖 **The pretraining data is mostly clinical TUH data.** TUSZ (1138.53 h) and TUEP (591.22 h) make up ≈68% of the 2,535 h (my arithmetic from App. D). The two headline tasks are also TUH datasets (recordings disjoint, §3.5). Domain closeness probably helps TUAB/TUEV more than it would help BCI tasks, and the weaker SEED-V and MoBI margins fit that.
- 🤖 The baseline numbers are copied from BIOT, not re-run. They follow the same split, which is acceptable, but any preprocessing differences go unchecked.
- 🤖 "Generic representations" depends on fine-tuning. Weak TUEV linear probing means the features aren't linearly ready for event types. This is relevant to how foundation models get evaluated ([[evaluation-protocols]]).
- 🤖 Only TUAB/TUEV are cross-subject. SEED-V pools subjects across splits, so the emotion result is not cross-subject.
- 🤖 The scaling evidence is suggestive but thin: one curve per size, the Base model goes non-monotonic, and the extrapolation to 10k h is not tested.
- 🤖 Its place in the history: the first widely cited "large EEG model". Its design choices (channel-wise patches, electrode embeddings, spectral targets) answer [[channel-heterogeneity]] and [[signal-quality-and-noise]] directly.

## Concepts
- [[seizure-detection]]: TUSZ is the largest pretraining source (1,138.5 of 2,535 h, App. D).
- [[bci-paradigms]]: pretraining corpus includes the PhysioNet Motor Movement/Imagery dataset (executed and imagined movements, 109 subjects) (App. D).
- [[self-supervised-pretraining]]: masked token prediction with a VQ spectral tokenizer.
- [[channel-heterogeneity]]: channel-wise patches plus learnable electrode embeddings make it montage-agnostic.
- [[cnn-transformer-hybrid]]: a temporal conv encoder per patch before the Transformer.
- [[evaluation-protocols]]: patient-level splits on TUH; trial split on SEED-V; fine-tuning vs linear probe.
- [[signal-quality-and-noise]]: predicts the spectrum, not raw signal, because of low SNR.
- [[frequency-bands]]: predicts the full Fourier amplitude/phase per patch instead of fixed bands (§2.2).
- [[time-frequency-analysis]]: Fourier amplitude/phase of 1 s patches as tokenizer targets (§2.2).
- [[emotion-recognition]]: SEED-V downstream task (5-class, subjects pooled, trial split); SEED-family data in pretraining.

## Related papers
- [[liu2026eeg]]: independent benchmark; LaBraM ranks 9th of 20 (9.36), and its probe < fine-tune gap is significant (Supp. Tables 52, 58).
- [[song2022eeg]]: the non-pretrained conv + attention predecessor pattern. Not used as a LaBraM baseline.
- [[yang2023biot]]: BIOT, the main baseline and source of the evaluation splits. *(screening: maybe)*
- [[wang2024cbramod]]: a later EEG foundation model that compares against LaBraM. *(seed, not yet read)*
- [[lawhern2018eegnet]]: cited as the canonical CNN approach (§1).
- [[chaddad2023electroencephalography]]: classical time–frequency features, which LaBraM's Fourier-amplitude/phase targets learn instead.
- [[wong2023eeg]]: describes TUSZ, LaBraM's largest pretraining source: 3,050 seizures, the richest clinical metadata (Tables 5–6, 8).
- [[li2022eeg]]: 2022 emotion review that proposed an emotion-agnostic large pretrained EEG model as future work (p. 29); LaBraM is one.
- [[roy2019deep]]: the pre-foundation-model DL-EEG landscape (2010–2018). It anticipated that large corpora like TUH would make deeper models usable (p. 27). Its 2010–2014 unsupervised pretraining (RBM/DBN/AE) is a precursor to LaBraM's.
- [[kuruppu2026eeg]]: 2026 review of 10 early FMs. LaBraM leads TUAB/TUEV, possibly through data diversity; its probe gap is the field-wide pattern; the review counts it as fixed-montage (🤖 debatable).
- [[weng2025self]]: survey of the SSL methods before LaBraM (≈2019–2023). LaBraM itself isn't covered.
- [[xie2026specbram]]: probes LaBraM-Base frozen on sleep (ISRUC 0.752, HMC 0.632), below hand-crafted spectral features on HMC (Table 4); argues a fixed band-power target avoids the learned codebook.

## Q&A notes
