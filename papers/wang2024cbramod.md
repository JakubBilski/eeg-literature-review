---
citekey: wang2024cbramod
title: "CBraMod: A Criss-Cross Brain Foundation Model for EEG Decoding"
authors: [Jiquan Wang, Sha Zhao, Zhiling Luo, Yangxuan Zhou, Haiteng Jiang, Shijian Li, Tao Li, Gang Pan]
year: 2024
venue: "ICLR 2025"
doi: ""
arxiv: "2412.07236"
pmid: ""
field: eeg
paper_type: method
task: "emotion recognition; motor imagery; sleep staging; seizure detection; imagined speech; depression diagnosis; vigilance; mental stress; event classification; abnormal EEG detection"
datasets: [TUEG, FACED, SEED-V, PhysioNet-MI, SHU-MI, ISRUC, CHB-MIT, BCIC2020-3, Mumtaz2016, SEED-VIG, MentalArithmetic, TUEV, TUAB, BCIC-IV-2a]
n_subjects: "pretraining: 14,987 (TUEG); downstream 9–123 per dataset"
n_channels: "19 (10-20) in pretraining; 6–64 downstream"
model_type: "criss-cross Transformer (parallel spatial/temporal attention heads), 4.0M params; masked raw-patch reconstruction (MSE)"
eval_protocol: "subject-disjoint train/val/test on most sets (fixed split, 5 fine-tuning seeds); trial split with pooled subjects on SEED-V; competition split on BCIC2020-3"
main_metric: "balanced accuracy / Cohen's kappa / AUROC"
main_result: "best on all 13 datasets vs 7 supervised + BIOT/LaBraM-Base, e.g. FACED kappa 0.504 vs LaBraM 0.470 (Table 2), TUAB bal. acc. 0.829 vs LaBraM-Huge 0.826 (Table 14)"
code_available: "https://github.com/wjq-learning/CBraMod"
read_depth: full
concepts: [self-supervised-pretraining, channel-heterogeneity, cnn-transformer-hybrid, time-frequency-analysis, evaluation-protocols, eeg-preprocessing-pipeline, digital-filtering, signal-quality-and-noise, emotion-recognition, bci-paradigms, sleep-staging, seizure-detection]
---

# CBraMod: criss-cross brain foundation model (Wang et al., ICLR 2025)

## TL;DR
A 4M-parameter Transformer whose attention heads are split: half attend across channels at the same time (spatial), half along time within a channel (temporal). Pretrained by reconstructing masked 1 s raw patches on ~9,000 cleaned hours of TUEG, then fully fine-tuned; reported best on 13 datasets / 10 tasks, by 1–4 points over LaBraM-Base.

## Research question
- Does modelling spatial and temporal dependencies separately ("criss-cross") beat full attention over all patches, and does a convolutional positional encoding adapt better to different montages and references than electrode-index embeddings (LaBraM)? (§1, pp. 2–3)

## Data & preprocessing
- **Pretraining corpus:** TUEG, 69,652 recordings, 14,987 subjects, 26,846 sessions, 27,062 h, >40 channel configurations, mostly 256 Hz; "significant data contamination" with unmarked artifacts and faulty channels (§3.1, p. 6).
- **Pipeline (§3.1):** drop recordings ≤5 min; cut first and last minute; keep 19 10-20 channels (Fp1 … O2); band-pass 0.3–75 Hz; notch 60 Hz; resample 200 Hz; 30 s non-overlapping samples; **drop any sample with a point >100 µV**; scale by 100 µV (as LaBraM). Leaves 1,109,545 samples, ">9000 hours" (vs LaBraM 2,534.78 h).
- 30 s samples chosen because longer context may help (BENDR) and covers all downstream lengths (App. B).
- **Downstream:** all resampled to 200 Hz, 1 s patches (§3.2). Datasets and splits in Table 1 and §3.3 / App. E:
  - FACED 123 subj, 9 emotions, subj 1–80 / 81–100 / 101–123; SEED-V 16 subj, 5 classes, **trials split 5:5:5 within each session, subjects pooled** (§3.3, p. 8). Open 16-subject SEED-V, not LaBraM's 20 (footnote 1).
  - PhysioNet-MI 109 subj, 4 classes, 1–70 / 71–89 / 90–109; SHU-MI 25 subj, 2 classes, test = 5 subj (§3.3).
  - ISRUC group 1, 100 subj, 6 ch, test = 10 subj, sequence of 20 epochs + 1-layer transformer on top for every model (App. E.1).
  - CHB-MIT 23 children, 16 bipolar ch, 10 s, test = subjects 22–23 (App. E.2). Mumtaz2016 34 MDD / 30 HC, test 5 + 5, eyes open/closed only, notch 50 Hz (App. E.4).
  - SEED-VIG 23 subj, regression of PERCLOS, test = 4 subj (App. E.5). MentalArithmetic 36 subj, test = 4 (App. E.6). BCIC2020-3 imagined speech, 15 subj, competition split (App. E.3).
  - TUEV, TUAB: BIOT preprocessing, 16 bipolar channels, official train/test, train split 80:20 into train/val (App. E.7–E.8). BCIC-IV-2a 9 subj, test = subjects 8–9 (App. E.9).

## Method
- **Patching & masking:** C × T sample → C × n patches of t = 200 samples (1 s); Bernoulli mask, ratio 0.5, full-zero mask token (§2; Table 5). One 19 × 30 s sample = 570 patches (§3.1).
- **Patch encoder:** time branch = 3 × (1D conv + GroupNorm + GELU); frequency branch = rfft magnitude → linear (101 → 200); the two embeddings are summed (§2, Eq. 3; Table 5).
- **ACPE (asymmetric conditional positional encoding):** one depthwise 2D conv over the channel × time grid of patch embeddings, kernel (19, 7): long range across channels, short across time; output added to embeddings (§2, Eq. 5; Table 5). Modified from CPE for vision (Chu et al. 2021).
- **Criss-cross transformer:** 12 layers, d = 200, FFN 800, 8 heads: 4 do attention among the C patches at one time step (S-attention), 4 among the n patches of one channel (T-attention), concatenated (§2, Eqs. 6–9). Pre-norm plus LayerNorm on queries and keys (§2, p. 5).
- **Objective:** linear head, MSE on masked patches only (§2, Eq. 12). 40 epochs, batch 128, AdamW 5e-4, 4 × RTX A5000, ~5 days (§3.1, p. 7).
- **Fine-tuning:** replace head with an MLP on the *flattened* token representations; all weights trained, 50 epochs, lr 1e-4, label smoothing 0.1 (App. D.4, Table 6).

## Evaluation
- Baselines: EEGNet, EEGConformer, SPaRCNet, ContraWR, CNN-Transformer, FFCL, ST-Transformer (re-implemented on BIOT's code unless numbers were already published); BIOT and LaBraM-Base fine-tuned from public weights (only Base weights are public); LaBraM-Large/Huge quoted on TUAB/TUEV; DeepSleepNet and USleep on ISRUC (§3.2, App. E.1).
- Same splits for all methods (§3.3). Metrics: bal. acc., AUC-PR, AUROC (binary; AUROC used for model selection), kappa, weighted F1 (multi-class; kappa for selection), Pearson / R² / RMSE (regression). Mean ± SD over 5 random seeds (§3.2, p. 7).
- No classical (CSP, Riemannian, band-power) baselines, no significance tests.

## Results (with locations)
- **Main tables, CBraMod vs best other (bal. acc. unless stated):** FACED 0.551 vs LaBraM 0.527 (EEGNet 0.409); SEED-V 0.409 vs 0.398 (Table 2). PhysioNet-MI 0.642 vs 0.617 (EEGNet 0.581); SHU-MI AUROC 0.699 vs BIOT 0.661 (Table 3). ISRUC κ 0.744 vs LaBraM 0.723, USleep 0.721, EEGNet 0.704 (Table 7). CHB-MIT 0.740 vs 0.708, AUC-PR 0.369 vs 0.329 (Table 8). BCIC2020-3 0.537 vs 0.506 (Table 9). Mumtaz 0.956 vs 0.941 (EEGNet 0.923) (Table 10). SEED-VIG Pearson 0.646 vs BIOT 0.600 (Table 11). MentalArithmetic 0.726 vs 0.691 (Table 12). TUEV 0.667 vs LaBraM-Huge 0.662 (Table 13). TUAB 0.829 vs 0.826 (Table 14). BCIC-IV-2a 0.514 vs 0.487 (Table 15).
- **Leakage control for TUH sets:** re-pretrained without TUEV / TUAB: TUEV 0.666 (vs 0.667), TUAB 0.825 (vs 0.829), still ≈ LaBraM-Huge (Tables 13–14; App. E.7–E.8).
- **Attention ablation (pretrained and fine-tuned the same way):** full attention worst, then CCNet-style, then axial (spatial in blocks 1–6, temporal in 7–12), criss-cross best on all 4 sets (Fig. 4, p. 9). Head split 4:4 beats 2:6 and 6:2 by ~1–2 points (Table 20).
- **Positional encoding:** none < absolute < CPE < ACPE (Fig. 5, pp. 9–10).
- **Pretraining ablation (Table 4):** clean pretraining / dirty (no 100 µV rejection) / none: FACED 0.551 / 0.532 / 0.523; SEED-V 0.409 / 0.391 / 0.390; PhysioNet-MI 0.642 / 0.625 / 0.620; SHU-MI 0.637 / 0.630 / 0.629. Dirty ≈ no pretraining.
- **Architecture vs data:** BIOT and LaBraM architectures re-pretrained on CBraMod's TUEG data: BIOT unchanged, LaBraM slightly better (mainly FACED), both still clearly below CBraMod → "the model architecture contributes more" than data size (App. G, Fig. 8; bars only).
- **Scaling (FACED only):** κ rises from 1 h to 9,000 h of pretraining, "the rate of improvement slows beyond 1000 hours"; also rises with model size 0.1M → 4M (App. F, Fig. 7; plot only).
- **Segment length:** 4 s / 8 s / 30 s pretraining: FACED 0.545 / 0.545 / 0.551; small effect (Table 16).
- **Patch encoder:** time + frequency 0.551, time only 0.544, frequency only 0.521 on FACED; same order on the other 3 sets (Table 17).
- **Frozen backbone + classifier (Table 18):** FACED 0.315 (vs 0.551 fine-tuned), SEED-V 0.254, PhysioNet-MI 0.385, SHU-MI 0.522 (≈ chance for 2 classes). Frozen BIOT/LaBraM slightly lower (e.g. FACED 0.278 / 0.300). Authors: CBraMod "cannot currently serve as a fixed-parameter feature extractor" (App. J).
- **30% of labels (Table 19):** FACED 0.404 (vs 0.551 full), SEED-V 0.388, PhysioNet-MI 0.561, SHU-MI 0.623; BIOT/LaBraM lower by 2–9 points.
- **Mask ratio** 0.3–0.7 works, 0.5 chosen (Fig. 9); full-zero vs learnable mask token no difference (Table 21).
- **Cost:** 4.0M params, 318.9 MFLOPs on CHB-MIT input, vs LaBraM-Base 5.8M / 483 MFLOPs, full-attention CBraMod 469 MFLOPs (Table 22). Pretraining loss falls to ~0.002 (Fig. 6).
- **LOSO on BCIC-IV-2a vs EEG-SimpleConv:** 0.597 vs 0.565 without its "key ingredients" (Euclidean alignment, session statistics, Mixup, subject-wise regularisation); 0.741 vs 0.722 with them (Table 23).
- Fine-tuning converges in <10 epochs vs ~30 for EEGConformer on FACED (App. R, Fig. 13).

## Limitations (reported)
- Crude data cleaning discards much of TUEG (App. S.2).
- More parameters and compute than non-FM models; hard to deploy on small devices (App. S.2).
- Scaling to billion-parameter size not explored (App. S.2).

## Assessment 🤖
- 🤖 **The paper's own ablations say the architecture and fine-tuning recipe matter more than pretraining.** CBraMod *without* pretraining already ties or beats fine-tuned LaBraM-Base: PhysioNet-MI 0.620 vs 0.617, SHU-MI 0.629 vs 0.617, FACED 0.523 vs 0.527 (Tables 2–4). Pretraining adds +0.8 to +2.8 points. App. G points the same way.
- 🤖 **Pretraining helps only on clean data:** without the 100 µV rejection, pretraining is worth about as much as none (Table 4). This is a data-quality result for [[q9-pretraining-objectives-and-scale]], but it rests on 4 datasets and one seed set, with gaps inside ~1 SD.
- 🤖 **Frozen features are weak** (Table 18), consistent with LaBraM's weak linear probe ([[jiang2024large]]). The UMAP figure (App. P.2) claims label structure without fine-tuning; Table 18 is the quantitative check and it is poor. Its MLP reads all flattened tokens, so the weakness is not just mean-pooling (cf. [[xie2026specbram]] §6.4, which reports these same 0.315 / 0.385).
- 🤖 **The SDs measure seed noise, not subject sampling.** Each split is fixed, and many test sets are tiny: 2 subjects (CHB-MIT, BCIC-IV-2a), 4 (SEED-VIG, MentalArithmetic), 5 (SHU-MI), 10 (Mumtaz, ISRUC). Margins of 1–3 points with no significance tests are not established wins. [[liu2026eeg]] later finds CBraMod's lead over EEGNet-class models not significant.
- 🤖 **Baselines are not equally tuned.** Hyperparameters are listed for CBraMod only (Table 6); supervised baselines come from BIOT's code base; LaBraM-Large/Huge are quoted on TUH tasks only. There is no classical pipeline. The best-tuned outside comparison (EEG-SimpleConv, Table 23) shrinks the margin to ~2 points. (Table 23's column headers say AUC-PR/AUROC for a 4-class task, while the text says kappa / weighted F1: a labelling error.)
- 🤖 **Leakage:** the exclude-TUAB/TUEV re-pretraining is a good control that most FMs lack. Patient overlap may remain, since TUH patients have several sessions and only the TUAB/TUEV *files* were removed. PhysioNet-MI was in LaBraM's pretraining but not CBraMod's ([[jiang2024large]] App. D), which slightly favours the LaBraM baseline there. SEED-V pools subjects (trial split), so it isn't cross-subject.
- 🤖 **The "19 channels" design is a fixed montage.** ACPE generalises over montage in principle, but pretraining saw only 19 referential 10-20 channels; downstream bipolar and 6–64-channel sets are handled by fine-tuning. Montage robustness is tested elsewhere ([[steglich2026representational]], [[chen2026benchmarking]] Fig. 7).
- 🤖 **The conv front end is kept:** the patch encoder is a small CNN plus FFT branch, and the frequency branch alone is worse than the time branch (Table 17). This partly answers the [[cnn-transformer-hybrid]] open question: at 4M params the conv stem is still used, though no stem-free variant is tested.
- 🤖 Raw-waveform MSE converges here (Fig. 6), unlike LaBraM's report that raw reconstruction "fails to converge" (§2.2). Amplitude rejection and 100 µV scaling may be what makes it stable; untested.

## Concepts
- [[self-supervised-pretraining]]: masked raw-patch reconstruction (MSE); clean vs dirty vs no pretraining; weak frozen features.
- [[channel-heterogeneity]]: ACPE (conv positional encoding) instead of electrode-index embeddings; fixed 19-channel pretraining montage.
- [[cnn-transformer-hybrid]]: 3-layer conv + FFT patch encoder before a criss-cross transformer.
- [[time-frequency-analysis]]: FFT-magnitude branch in the patch encoder; time branch alone > frequency alone (Table 17).
- [[eeg-preprocessing-pipeline]], [[digital-filtering]]: 0.3–75 Hz band-pass, 60 Hz notch, 200 Hz, 100 µV scaling (§3.1).
- [[signal-quality-and-noise]]: 100 µV sample rejection; dirty pretraining ≈ no pretraining (Table 4).
- [[evaluation-protocols]]: fixed subject splits with tiny test sets; exclude-TUAB/TUEV re-pretraining; frozen vs fine-tuned.
- [[emotion-recognition]], [[bci-paradigms]], [[sleep-staging]], [[seizure-detection]]: downstream benchmarks (FACED/SEED-V, PhysioNet-MI/SHU-MI/BCIC-IV-2a/imagined speech, ISRUC, CHB-MIT).

## Related papers
- [[jiang2024large]]: LaBraM, the main baseline; CBraMod replaces its token target with raw MSE and its full attention with criss-cross attention.
- [[yang2023biot]]: BIOT, FM baseline and source of supervised baseline code and TUAB/TUEV/CHB-MIT preprocessing.
- [[lawhern2018eegnet]], [[song2022eeg]]: EEGNet and EEG Conformer as supervised baselines.
- [[xie2026specbram]]: copies the criss-cross design and changes only the target to band power; found a SEED-VIG split bug in CBraMod's released code (App. B).
- [[liu2026eeg]], [[chen2026benchmarking]], [[kontras2026neuroatlas]], [[zare2026negative]], [[tao2026separating]], [[steglich2026representational]]: independent benchmarks that re-evaluate CBraMod (best average rank but not significant in Liu; pretrained ≈ random init on seizures in Kontras).
- [[kuruppu2026eeg]]: critical FM review; CBraMod is after its cutoff.

## Q&A notes
- 2026-10-25 **Q:** Are the small pretraining / architecture gains a sign of noisy, saturated tasks? **A:** Noisy yes (seed SDs on 2–10 test subjects). Saturated only for sleep and TUAB. On cross-subject MI the same CBraMod gains +14 points from Euclidean alignment and related tricks (0.597 → 0.741, Table 23), about 5× its pretraining gain, so headroom exists but pretraining doesn't reach it → [[q7-foundation-models-vs-baselines]] *Saturated, noisy, or headroom?*
