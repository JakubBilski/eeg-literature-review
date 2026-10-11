---
citekey: liu2026eeg
title: "EEG-FM-Compass: Progress, Benchmarking, and Future Directions for EEG Foundation Models"
authors: [Dingkun Liu, Yuheng Chen, Zhu Chen, Zhenyao Cui, Yaozhi Wen, Jiayu An, Jingwei Luo, Dongrui Wu]
year: 2026
venue: "National Science Review"
doi: ""
arxiv: "2601.17883"
pmid: ""
field: eeg
paper_type: benchmark
task: "review of 55 EEG FMs + benchmark of 12 open FMs vs 8 specialist baselines on 13 BCI/clinical datasets (MI, P300, SSVEP, seizure, abnormal EEG, sleep, emotion, workload, visual decoding, vigilance)"
datasets: [BNCI2014001, BNCI2014004, BNCI2015001, BNCI2014009, BNCI2014008, CHB-MIT, TUAB, Sleep-EDFx, SEED, Nakanishi2015, EEGMat, Things-EEG2, SEED-VIG]
n_subjects:
n_channels:
model_type: "12 FMs (BENDR, BIOT, LaBraM, Neuro-GPT, EEGPT, CBraMod, TFM, BrainOmni, EEGMamba, MIRepNet, SingLEM, LUNA) vs CSP/xDAWN/PSD+LDA/SVM, TRCA, EEGNet, ShallowConv, LMDA, TSception, CNN-T, Deformer, Conformer"
eval_protocol: "LOSO (or 10-fold subject split for TUAB/Sleep-EDFx) and within-subject few-shot; full fine-tuning vs linear probing; 3 seeds; final-epoch test"
main_metric: "balanced accuracy; average rank across 25 dataset-scenario blocks"
main_result: "CBraMod best average rank 6.56 vs EEGNet 7.40, not significantly different (Nemenyi CD 4.94) (Supp. Table 52, p. 71)"
code_available: "https://github.com/Dingkun0817/EEG-FM-Benchmark (announced)"
read_depth: full
concepts: [self-supervised-pretraining, evaluation-protocols, channel-heterogeneity, eeg-preprocessing-pipeline, common-spatial-patterns, bci-paradigms, domain-adaptation, seizure-detection]
---

# EEG-FM-Compass (Liu, Chen, Chen … Wu, Natl Sci Rev 2026)

## TL;DR
A survey of 55 EEG FMs and a benchmark of 12 open FMs against 8 specialist baselines under matched protocols. Specialists match FMs in the leave-one-subject-out setting (LOSO) and beat them in few-shot. Linear probes are mostly much worse than fine-tuning. Model size does not predict rank, and no pretraining objective wins. The first independent matched answer to Q7.

*Read from arXiv v3 (3 Aug 2026; 26 pp. main + supplement to p. 87). (p. N) = PDF pages. The main text cites supplementary Tables 49–51 and 55, which appear in the PDF as Tables 52–54 and 58; cited here by PDF numbering. Group: Dongrui Wu (HUST), who also authored MIRepNet, one of the evaluated FMs.*

## Research question
(p. 2):
- **Q1:** Do FMs give general representations, so that adaptation is easy?
- **Q2:** Do they consistently and significantly beat traditional and DL models trained from scratch on the fine-tuning data alone?
- **Q3:** Do they follow scaling laws?

## Data & preprocessing
- **Survey:** 55 FMs. 67.3% are from 2025–26, 83.6% use transformers, 71.7% use random masking. Raw-signal reconstruction is the most common target (25.5%) (Fig. 3, p. 6; §2.3 p. 10). Most resample to 200 Hz (Fig. 3f).
- **Channel unification:** six strategies (fixed montage; template or region remap; channel-wise tokens; learnable channel embeddings; coordinate-aware encoding; projection to a latent space), each with examples (pp. 8–9).
- **Benchmark data:** 13 datasets in 9 paradigms (Supp. Table 14, p. 35):
  - MI: BNCI2014001/2014004/2015001 (9–12 subjects)
  - P300: BNCI2014009/2014008
  - clinical: CHB-MIT (23 subjects), TUAB (2,383)
  - sleep: Sleep-EDFx (78, 2 channels)
  - other: SEED, Nakanishi2015 SSVEP, EEGMat workload, Things-EEG2, SEED-VIG regression
- **Task definitions:** CHB-MIT is ictal vs 10-min pre-ictal segments; TUAB uses the first 3 min of each recording; MI/P300 fine-tuning uses one session per subject (p. 15).

## Method
- **Survey taxonomy of objectives:** masked raw-signal reconstruction; masked embedded-token reconstruction (incl. contrastive); frequency-domain (incl. HuBERT-style spectral k-means labels in E3GT and PSGFM); codebook index; autoregressive (pp. 10–13).
- **Benchmark baselines:**
  - classical, one paradigm-specific pipeline per dataset: CSP+LDA (MI, TUAB, SEED, EEGMat), xDAWN+LDA (P300), PSD+SVM (CHB-MIT), PSD+LDA (sleep), TRCA (SSVEP), PSD+ridge (vigilance) (p. 16)
  - 7 deep models trained from scratch: EEGNet, ShallowConv, LMDA, TSception, CNN-T, Deformer, Conformer
- **FMs:** all with public weights; BIOT in 1D/2D/6D variants (p. 16).

## Evaluation
- **Two scenarios (p. 15):**
  - **LOSO:** zero calibration on the held-out subject; 10-fold subject split for TUAB and Sleep-EDFx.
  - **Within-subject few-shot:** fine-tune on a small part of the target subject (e.g. MI: 30% of one session ≈ 21 trials per class; SSVEP: 12 per class; EEGMat: 9 per class), then test on the rest (Supp. Table 15, p. 35). TUAB is excluded from few-shot (one label per subject).
- **Full fine-tuning vs linear probing** for every FM (p. 15).
- **Protocol details:** 3 seeds; test score at the *final* epoch, not a selected checkpoint; hyperparameters tuned per model; balanced accuracy (pp. 16–17).
- **Stats:** Friedman + Nemenyi over 25 dataset–scenario blocks. Traditional ML and BrainOmni are excluded from the test because their results are incomplete (p. 72). Wilcoxon full vs linear per FM (Supp. Table 58).
- **Leakage:** ‡ marks datasets in an FM's pretraining corpus, and a leakage-aware ranking drops them (Supp. Table 54, p. 71).

## Results (with locations)
- **Overall ranks** (Supp. Table 52, p. 71): CBraMod 6.56; EEGNet 7.40 (2K params); Conformer 7.40; ShallowConv 7.60; Deformer 7.72; LMDA 7.76; Neuro-GPT 7.84; … LaBraM 9.36; traditional ML 9.91; EEGPT 12.08; LUNA 14.44; TFM 16.20.
  - CBraMod vs EEGNet/ShallowConv/Conformer/Deformer/LMDA: **not significant** (Nemenyi CD 4.94; Friedman χ² = 98.19, p = 7.6×10⁻¹⁴) (pp. 21, 72).
  - The leakage-aware ranking barely changes the order (CBraMod 6.63, EEGNet 7.08) (Supp. Table 54).
- **Top-1 counts:** EEGNet most; specialists take 16 first places and 47 top-3 vs the 7 best FMs (p. 20, Fig. 5).
  - LOSO: the two groups are comparable.
  - Few-shot: specialists take most first places (p. 20).
- **Few-shot, classical pipelines win where they are standard** (Tables 2–3, pp. 18–19):
  - MI BNCI2014001: CSP+LDA **60.62** vs best FM CBraMod 50.34 and best DL TSception 58.68 (Supp. Table 16).
  - SSVEP: TRCA **98.77** vs best FM 85.91 (BENDR).
  - EEGMat: CSP+LDA **95.60** vs best FM 86.11 (BIOT-6D).
  - Classical loses on P300 (xDAWN+LDA 54.45/56.65 vs EEGNet 68.99/70.91), CHB-MIT (77.71 vs Conformer 91.58) and sleep (59.00 vs LUNA 66.02).
- **LOSO MI:** CSP+LDA 38.19 vs CBraMod 53.03 and MIRepNet (MI-specific FM) 54.21 on BNCI2014001 (Supp. Table 16).
- **TUAB (LOSO, balanced accuracy):** LUNA 81.92‡, EEGMamba 80.90‡, BrainOmni-Base 80.49, CBraMod 79.98‡ vs Deformer 81.48 and ShallowConv 79.81. The "traditional ML" baseline here is CSP+LDA at 66.03 (Table 2).
- **Linear probing:** full fine-tuning wins significantly for 9/12 FMs (BENDR and CBraMod in 23/25 pairs). EEGPT is the only FM where the probe wins (7/18). BrainOmni-Tiny and SingLEM show no difference (Supp. Table 58, p. 84).
  - Extreme case: Nakanishi2015 LOSO, CBraMod 85.39 fine-tuned vs 17.41 probed (Table 3).
  - LoRA lands between full fine-tuning and the probe (CBraMod LOSO BNCI2014001: 53.03 / 41.45 / 39.89) (Supp. Table 57).
- **Scaling:** the top six FMs are 0.16M–5.8M params with no size–rank correlation. Within the codebook family, LaBraM (5.8M) 9.36 < BrainOmni-Tiny (8.4M) 12.33 < BrainOmni-Base (33M) 12.76 (pp. 21–22).
- **Objective:** no family dominates. Ranks span 1–15 (raw), 7–18 (embedded tokens), 9–20 (codebook). No objective–paradigm match either: frequency-domain FMs are not top on SSVEP (p. 22).
- **Cost:** EEGPT ~361 GFLOPs per forward pass vs EEGNet 0.35, and ~46× lower fine-tuning throughput (p. 20).
- **Euclidean alignment** improves most models on BNCI2014001 (Fig. 7c, p. 23).
- **Data ratio 10→90%:** model rankings stay largely stable (p. 72).

## Limitations (reported)
- The specialist baselines are general-purpose, "not necessarily the state-of-the-art for every individual paradigm" (p. 16).
- Only open-weight FMs are tested. BrainOmni cannot handle bipolar montages (p. 16).

## Assessment 🤖
- 🤖 **The strongest Q7 evidence so far.** It is matched (same fine-tuning data, same test sets, per-model tuning) and independent of the FM authors (except MIRepNet). It confirms what Kuruppu inferred from reported numbers: probes are weak, scaling is absent, specialists are competitive.
- 🤖 **The classical baseline is uneven.** CSP+LDA on TUAB and SEED is not the standard pipeline; band power + logistic/GBM is the usual choice for abnormality. No Riemannian (tangent space) baseline was run, though EA was tested. So the classical side is underestimated outside MI/P300/SSVEP. It was also excluded from the significance test.
- 🤖 **Few-shot splits may flatter within-subject models.** EEGMat at 95.6% from 9 trials per class suggests that train and test windows come from the same continuous recording (temporal adjacency); the split procedure is not described. This affects FMs and specialists alike, so the comparison holds but the absolute numbers may not → [[evaluation-protocols]].
- 🤖 **Final-epoch reporting** avoids test-set checkpoint picking. It may penalise models that need early stopping, and large FMs on tiny sets more than small CNNs.
- 🤖 **CHB-MIT here is ictal vs pre-ictal segments**, not continuous detection with false alarms per hour. Results don't transfer to clinical seizure monitoring → [[seizure-detection]].
- 🤖 **Conflict of interest:** MIRepNet comes from the same group and gets the best MI results. The paradigm-specific-FM recommendation rests mostly on that one model (p. 23).

## Concepts
- [[self-supervised-pretraining]]: taxonomy of 55 FMs' objectives; no objective wins; probe vs fine-tune across 12 FMs.
- [[evaluation-protocols]]: LOSO vs within-subject few-shot; leakage-aware ranking; final-epoch reporting; Friedman/Nemenyi.
- [[channel-heterogeneity]]: six channel-unification strategies with examples (pp. 8–9).
- [[eeg-preprocessing-pipeline]]: z-score, CAR, EA, EMA normalization across FMs (p. 9).
- [[common-spatial-patterns]]: CSP+LDA wins few-shot MI and EEGMat, loses LOSO MI.
- [[bci-paradigms]]: 9 paradigms; SSVEP TRCA nearly perfect within-subject.
- [[domain-adaptation]]: Euclidean alignment helps most models cross-subject (Fig. 7c).
- [[seizure-detection]]: CHB-MIT as ictal vs pre-ictal segment classification; Conformer 91.58 few-shot vs best FM 88.54.

## Related papers
- [[kuruppu2026eeg]]: same conclusions from reported numbers; this paper tests them under matched protocols.
- [[wang2024cbramod]]: CBraMod is the #1 FM here (rank 6.56), but it is not significantly ahead of EEGNet or the other specialists.
- [[jiang2024large]]: LaBraM is ranked 9; its linear-probe weakness is confirmed.
- [[wang2024eegpt]]: the only FM whose probe beats its fine-tuning, but it ranks 15th overall.
- [[yang2023biot]]: more pretraining datasets don't help consistently. BIOT-1D/2D/6D score 32.2/33.3/34.3 LOSO but 45.6/43.6/48.6 few-shot on BNCI2014001 (Supp. Table 16).
- [[lawhern2018eegnet]]: EEGNet (2K params) ranks 2nd overall, and the 2018 matched-comparison pattern holds in 2026.
- [[xie2026specbram]]: hand-crafted band power ≈ FM frozen features; consistent.
- [[chen2026benchmarking]], [[kontras2026neuroatlas]], [[xiong2025eeg]], [[shen2026brain4fms]]: other 2025–26 benchmarks to cross-check.
- [[coppola2024hubert]]: ECG parallel with the same weak-probe pattern.

## Q&A notes
