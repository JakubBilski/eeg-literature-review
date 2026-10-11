---
citekey: lawhern2018eegnet
title: "EEGNet: a compact convolutional neural network for EEG-based brain–computer interfaces"
authors: [Vernon J. Lawhern, Amelia J. Solon, Nicholas R. Waytowich, Stephen M. Gordon, Chou P. Hung, Brent J. Lance]
year: 2018
venue: "Journal of Neural Engineering 15(5):056013"
doi: "10.1088/1741-2552/aace8c"
arxiv: "1611.08024"
pmid: "29932424"
field: eeg
paper_type: method
task: "BCI classification across 4 paradigms: P300 (RSVP), feedback ERN, MRCP (finger movement), SMR (motor imagery)"
datasets: [ARL RSVP P300, Kaggle BCI Challenge ERN, BioSemi finger-movement MRCP, BCI Competition IV-2a]
n_subjects: "15 / 26 / 13 / 9 (Table 1)"
n_channels: "64 / 56 / 64 / 22 (§2.1)"
model_type: "compact CNN (temporal conv → depthwise spatial conv → separable conv), 0.8–2.3k params"
eval_protocol: "within-subject 4-fold blockwise CV; cross-subject random subject folds (30 folds; 90 for SMR)"
main_metric: "AUC (P300/ERN/MRCP), accuracy (SMR)"
main_result: "Matches or beats DeepConvNet/ShallowConvNet/xDAWN+RG/FBCSP in most settings with ~100× fewer params; loses to xDAWN+RG on cross-subject ERN (Figs. 2–5, §3)"
code_available: "https://github.com/vlawhern/arl-eegmodels"
read_depth: full
concepts: [bci-paradigms, common-spatial-patterns, riemannian-methods, evaluation-protocols, digital-filtering, eeg-preprocessing-pipeline, channel-heterogeneity]
---

# EEGNet: a compact CNN for EEG-based BCIs (Lawhern et al., 2018)

## TL;DR
One small CNN (~1–2k parameters) whose layers copy the classical BCI recipe: a learned filter bank, then per-band spatial filters. It is tested on 4 BCI paradigms within and across subjects. It roughly matches paradigm-specific pipelines and much larger CNNs, and its filters can be read physiologically.

*arXiv v4 (May 2018); (p. N) = arXiv PDF pages. Results exist only as bar charts: numbers below are read off Figs. 2–5 by eye (±0.01), transcribed in `fulltext/lawhern2018eegnet.md`. Pre-2022: backward exception (4,784 citations; used as baseline or cited by [[song2022eeg]], [[wang2024cbramod]], [[jiang2024large]], [[li2022eeg]], [[varbu2022past]]).*

## Research question
Can a single, compact CNN classify EEG from different BCI paradigms (ERP and oscillatory), with little training data, and produce interpretable features? (Abstract; §1, p. 3)

## Data & preprocessing
Two families: **ERP** BCIs (time-locked waveform, robust across subjects) vs **oscillatory** BCIs (band power, lower SNR, more subject variability) (§2.1, pp. 3–4). All data downsampled to 128 Hz (§2.1).

| | P300 (RSVP) | ERN | MRCP | SMR |
|---|---|---|---|---|
| subjects | 15 (18 recorded, 3 dropped for artifacts) | 26 (16 train / 10 test, Kaggle) | 13 | 9 |
| device | BioSemi, 64 ch | 56 passive Ag/AgCl | BioSemi 256 → 64 ch | 22 Ag/AgCl |
| band-pass | 1–40 Hz | 1–40 Hz | 0.1–40 Hz | 4–40 Hz |
| epoch | 0–1 s | 0–1.25 s | −0.5–1 s | 0.5–2.5 s after cue |
| classes / imbalance | 2, ~5.6:1 | 2, ~3.4:1 | 2 (left vs right hand), none | 4, none |

(Table 1, p. 4; §2.1.1–2.1.4, pp. 4–6.) MRCP data needed the PREP pipeline because of noise (§2.1.3).

## Method
- **Block 1 (Table 2, pp. 6–8):** F1 temporal convs of length 64 (= half the sampling rate, so it can capture ≥2 Hz) → a **depthwise conv** over all C channels, giving D spatial filters *per temporal filter*. Both are linear ("no significant gains" from nonlinearities, p. 7) → BatchNorm → ELU → avg-pool /4 → dropout.
  - Explicitly "inspired in part by the Filter-Bank Common Spatial Pattern (FBCSP) algorithm" (p. 7): temporal conv = filter bank, depthwise conv = frequency-specific spatial filters.
- **Block 2:** separable conv (a 500 ms per-map temporal summary, then a 1×1 mix of maps) → avg-pool /8 (p. 8).
- **Classifier:** softmax directly on the flattened features, no dense hidden layer, to save parameters (p. 8).
- **Size:** EEGNet-4,2 has 796–1,098 params and EEGNet-8,2 1,716–2,322, vs DeepConvNet ~150–176k and ShallowConvNet ~41–105k (Table 3, p. 9).
- **Training:** Adam, cross-entropy, 500 epochs, keep the lowest-validation-loss weights; dropout 0.5 within-subject, 0.25 cross-subject; class-weighted loss for P300/ERN (§2.2.1, §2.3, pp. 6, 11–12).
- **Baselines (§2.2.2–2.2.3, pp. 9–11):** DeepConvNet and ShallowConvNet (Schirrmeister 2017, re-implemented, kernels halved for 128 Hz). Classical: **xDAWN + Riemannian tangent space + elastic net** (the Kaggle-winning ERN pipeline) for ERP data; **one-vs-rest FBCSP** (9 bands, 4–40 Hz, elastic-net logistic regression) for SMR. Single models, no ensembles or dataset-specific meta-features.

## Evaluation
- **Within-subject:** 4-fold blockwise CV (2 blocks train, 1 validation, 1 test); repeated-measures ANOVA (§2.3, p. 11).
- **Cross-subject:** P300/MRCP: 4 random validation subjects, 1 test subject, rest train, ×30. ERN: the Kaggle 10 test subjects fixed. SMR: train on 5 other subjects, validate on 3, test on the held-out subject's competition test set, ×10 per subject = 90 folds (§2.3, p. 11).

## Results (with locations)
- **Within-subject, AUC** (Fig. 2, p. 13): P300: all CNNs ≈ 0.92 > xDAWN+RG 0.87. MRCP: EEGNet 0.79–0.80 vs xDAWN+RG 0.75, DeepConvNet 0.66, ShallowConvNet 0.54. ERN: EEGNet-8,2 0.82 beats all (xDAWN+RG 0.77) (p < 0.05, §3.1).
- **Within-subject SMR, 4-class accuracy** (Fig. 3, p. 14): FBCSP 0.68, ShallowConvNet 0.70, EEGNet-8,2 0.68, EEGNet-4,2 0.63, DeepConvNet 0.51 (significantly worse). EEGNet-8,2 ≈ FBCSP (§3.1).
- **Cross-subject, AUC** (Fig. 4, p. 14): P300: CNNs ≈ 0.88–0.90 > xDAWN+RG 0.80. MRCP: DeepConvNet 0.83, EEGNet-8,2 0.81, xDAWN+RG 0.70. **ERN: xDAWN+RG 0.765 beats all CNNs** (0.71–0.745, p < 0.05) (§3.2, p. 15).
- **Cross-subject SMR** (Fig. 5, p. 15): all CNNs ≈ 0.39–0.40 vs FBCSP 0.32; chance is 0.25. No significant differences among CNNs.
- **Bigger EEGNet doesn't help:** 4,2 vs 8,2 never significantly different (§3.1–3.2).
- **DeepConvNet needs data:** close to EEGNet cross-subject, worse within-subject, where training sets are 10–15× smaller (p. 21). ShallowConvNet (log band-power by design) is weak on ERPs; DeepConvNet is weak on SMR (p. 21).
- **Interpretability (§3.3, pp. 15–19):**
  - P300 target trials also contain a **button press**, so a filter over left motor cortex with alpha desynchronization appears next to the P300 filter (Fig. 6, p. 15).
  - Filter ablation: full model AUC 0.905; keeping only the P300-like filter 4 gives 0.864, only filter 1 0.797 (Table 4, p. 16).
  - SMR spatial filters at ~12 Hz correlate with FBCSP's 8–12 Hz filters up to sign, ρ = 0.93 and 0.83 (−0.93 for a sign-flipped pair) (p. 17, Fig. 8).
  - DeepLIFT relevance: contralateral motor cortex for confident MRCP trials, diffuse for a wrong one (Fig. 9); peaks at the positive ERP peak for ERN (Fig. 10).

## Limitations (reported)
- ShallowConvNet's collapse on within-subject MRCP is unexplained (p. 21).
- Baselines simplified: single xDAWN+RG model without the ensemble or meta-features; FBCSP with elastic net instead of the original classifier (pp. 10–11).

## Assessment 🤖
- 🤖 **Architecture = differentiable FBCSP.** This is why it became the default small baseline: it encodes the domain prior (band → spatial filter → power/shape) in ~2k weights, so it trains on a few hundred trials.
- 🤖 **A rare matched DL-vs-classical comparison, including a Riemannian pipeline.** Same splits for all models. The verdict is mixed: CNNs win on P300 and MRCP, tie FBCSP within-subject on SMR, and lose to xDAWN+RG on cross-subject ERN. So "DL beats classical" depends on paradigm and protocol.
- 🤖 **Within vs cross-subject is the bigger effect than model choice:** SMR 4-class falls from ~0.68 to ~0.40 for EEGNet and ~0.32 for FBCSP (chance 0.25). Cross-subject motor imagery was barely above chance in 2018.
- 🤖 **Numbers don't transfer across papers.** EEGNet on BCI IV-2a within-subject is ~0.68 here but 74.50% in [[song2022eeg]] (Table II). The protocols differ (here 4-fold blockwise CV; Conformer trains on session 1 and tests on session 2 per [[evaluation-protocols]]), as do the epoch windows and preprocessing.
- 🤖 **The P300 confound is a good Q6 lesson:** the label (target) co-occurs with a motor act, and the model uses it. The authors frame it as interpretability; it's also a confound that would not exist in a pure-perception deployment.
- 🤖 Bar charts with no tables make the results hard to reuse; numbers in the vault are approximate.

## Concepts
- [[bci-paradigms]]: ERP (P300, ERN, MRCP) vs oscillatory (SMR) split; the P300 button-press confound.
- [[common-spatial-patterns]]: FBCSP baseline; EEGNet's depthwise conv learns FBCSP-like spatial filters (ρ up to 0.93).
- [[riemannian-methods]]: xDAWN + tangent space + elastic net as the ERP baseline; wins on cross-subject ERN.
- [[evaluation-protocols]]: within- vs cross-subject on the same models and data.
- [[classical-ml-baselines]] (topic): matched classical-vs-CNN comparison across 4 paradigms.
- [[digital-filtering]]: paradigm-specific band-pass; learned temporal filters as a filter bank.
- [[eeg-preprocessing-pipeline]]: features and classifier learned end to end from lightly filtered epochs.
- [[channel-heterogeneity]]: fixed montage; the depthwise conv spans exactly C channels.

## Related papers
- [[liu2026eeg]]: 2026 benchmark where EEGNet (2K params) ranks 2nd of 20 overall and has the most top-1 placements, not significantly behind CBraMod (pp. 20–21).
- [[roy2019deep]]: the systematic review of the same era; EEGNet is the "temporal then spatial conv" pattern it describes (p. 18).
- [[song2022eeg]]: EEG Conformer reuses EEGNet-style conv modules and beats it on BCI IV-2a (74.50% → 78.66%, Table II).
- [[wang2024cbramod]]: EEGNet as the small supervised baseline across all tasks (e.g. 0.581 on PhysioNet-MI, Table 3).
- [[jiang2024large]]: cites EEGNet as the canonical CNN approach (§1).
- [[li2022eeg]]: EEGNet as an end-to-end baseline in emotion recognition (p. 15).
- [[varbu2022past]]: the paradigm-specific pipelines that EEGNet aims to replace.
- [[schirrmeister2017deep]]: source of DeepConvNet/ShallowConvNet baselines (ref [32]); not yet read.
- [[weng2025self]]: lists SPP-EEGNet (SSL built on EEGNet, ref [87]); no SSL-vs-EEGNet numbers.

## Q&A notes
