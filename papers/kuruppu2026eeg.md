---
citekey: kuruppu2026eeg
title: "EEG Foundation Models: A Critical Review of Current Progress and Future Directions"
authors: [Gayal Kuruppu, Neeraj Wagh, Vaclav Kremen, Sandipan Pati, Gregory Worrell, Yogatheesan Varatharajah]
year: 2026
venue: "Journal of Neural Engineering"
doi: "10.1088/1741-2552/ae4455"
arxiv: "2507.11783"
pmid: ""
field: eeg
paper_type: review
task: "EEG foundation models (scalp + intracranial): clinical (abnormality, events, seizures, sleep, psychiatric) and BCI downstream tasks"
datasets: [TUEG, TUAB, TUEV, TUSZ, TUAR, TUSL, CHB-MIT, SHHS, Sleep-EDFx, HMC, SEED, BCI IV-2a, MAYO, FNUSA, Brain TreeBank]
n_subjects:
n_channels:
model_type: ""
eval_protocol: ""
main_metric: ""
main_result: ""
code_available: false
read_depth: full
concepts: [self-supervised-pretraining, evaluation-protocols, channel-heterogeneity, eeg-preprocessing-pipeline, seizure-detection, time-frequency-analysis]
---

# EEG foundation models: a critical review (Kuruppu, Wagh et al., JNE 2026)

## TL;DR
Ten early EEG foundation models (Jan 2021–Sep 2024: BrainBERT, Neuro-GPT, Brant, BIOT, EEGFormer, LaBraM, Mentality, NeuroLM, FoME, BrainWave) compared along three axes: input data, model + SSL objective, evaluation. Verdict: most are transformers trained by masked reconstruction. Evaluations are heterogeneous and mostly in-distribution, linear probes are weak, and the evidence for data or model scaling is "weak, if any". Real-world readiness is not shown.

*Read from arXiv v3 (24 Dec 2025, 35 pp. incl. supplement); (p. N) = arXiv pages. Mayo Clinic / U. Minnesota group, with clinicians as co-authors.*

## Research question
How mature are early EEG-FMs for clinical and real-world use, judged through data representation, SSL modeling and evaluation scope, and what should future work prioritise? (§1, pp. 2–3).

## Data & preprocessing (review method)
- Search on Google Scholar, arXiv, DBLP, IEEE Xplore, PubMed, bioRxiv, medRxiv: ("EEG" AND "Foundation Model"), 2021 to 30 Sep 2024. Kept papers that claim an off-the-shelf FM. Excluded components only, fine-tunes of existing FMs, multimodal and PSG sleep FMs (§3.1, p. 5). 9 found, plus BrainBERT added because it is a common baseline.
- Data scale is put on one axis as **channel-hours** (channels × hours): 4.5k (BrainBERT) to 878k (BrainWave). LaBraM 80k, TUEG-based models ~541k (Table 1, Supp. Table 1).
- Pretraining preprocessing across models: bandpass from 0.5 Hz, notch 50/60 Hz, resampling to 200/250 Hz, 1–10 s epochs. **None did explicit artifact removal or outlier exclusion**, and normalization is often undescribed (§4.1, p. 9).
- Background sections on what EEG contains (physiological, pathological, artifact, medication effects) and sources of cross-site variability (hardware, protocol, montage, reference, anatomy) (§2.1, pp. 3–4).

## Method (the comparison axes)
- **Input:** raw multichannel time series in 6/10 models. Spectra for BIOT and EEGFormer, time series + spectra for Brant and FoME, per-channel spectrograms for BrainBERT and BrainWave (§4.1, p. 10).
- **Montage handling:** LaBraM, Neuro-GPT and Mentality map datasets to a fixed channel set. Brant, NeuroLM and FoME use positional encodings to accept variable channel counts. The authors say "only BIOT supported multiple electrode configurations" among the models with explicit spatial encodings, and that LaBraM/NeuroLM are tied to a fixed 10–20 layout (§4.2, p. 10).
- **Patch / context:** patches of 1 s (LaBraM, NeuroLM, BIOT, BrainWave) up to 6 s (Brant, FoME). The maximum context is 90 s (FoME) (§4.2, p. 10).
- **SSL:** masked reconstruction in 7/10 models (LaBraM predicts codebook tokens; Neuro-GPT reconstructs in latent space). NeuroLM is autoregressive with EEG–text alignment. BIOT is contrastive (SimCLR-style) (§4.2, p. 12). Masking ratios: ~40% (Brant, FoME), 50% (LaBraM), ~10% (BrainBERT), channel masking (Mentality).
- **Scale:** 3.3M (BIOT) to 1.7B (NeuroLM) parameters, "most" in the 200–500M range (§4.2, p. 12).
- **Adaptation:** fine-tuning in 9/10, linear probing in 5/10, prototype few-shot only in BrainWave, instruction tuning in NeuroLM (§4.3, p. 12).

## Evaluation (of the field)
- 4/10 evaluate only on datasets also used for pretraining (BrainBERT, Mentality, NeuroLM, FoME). Only Brant and BrainWave evaluate on unseen datasets (§5.1, p. 17).
- Downstream tasks per paper: 1 (Mentality) to 12 (BrainWave), most ≤5. Only TUAB and TUEV are shared, and only 4 models can be ranked on them (§5.1, p. 17; Fig. 3).

## Results (with locations)
- **Shared benchmarks:** fine-tuned TUAB AUC 0.86–0.92, TUEV F1 0.70–0.83 across LaBraM, NeuroLM, EEGFormer, BIOT. More pretraining data did not predict better scores (Fig. 3, p. 14).
- **Linear probe ≪ fine-tune.** LaBraM TUEV balanced accuracy 34.61 vs 66.16, TUAB AUC 0.8835 vs 0.9162. BrainBERT AUC 0.59 vs 0.83. FoME TUEV F1 ~46 vs 79. Neuro-GPT on BCI IV-2a 44.3% vs 64.5% (Supp. Table 2, p. 35). Neuro-GPT's linear probe was below its supervised baselines (§4.3, p. 13). The authors say this "casts doubt on the quality of the representations learned via self-supervision" (§5.2, p. 18).
- **Paradigm comparison (Fig. 4a):** after fine-tuning, FMs give "at least some improvement, if not drastic" over supervised DL and earlier SSL. They show "substantial improvements" over classical ML with expert features, but only 4 studies ran that comparison (§5.1, p. 17).
- **Scaling:** model-size variants give marginal gains on some tasks (Fig. 4b). LaBraM's data-scaling gains are sharpest below ~1,000 h and plateau after. "The evidence for data scaling is weak, if any" (§5.1, p. 17).
- **General time-series FMs are competitive.** TimesNet beat EEG-FMs on sleep staging in FoME's paper. MOMENT beat EEG-FMs on seizure and pathology detection in BrainWave's paper. PatchTST did well on pathology detection (§4.3 p. 14; §5.1 p. 17).
- **Diversity of data sources may matter more than volume:** LaBraM (80k channel-hours, many sources) leads EEGFormer/NeuroLM (~541k, mostly TUEG) on TUAB/TUEV, confounders notwithstanding (§5.1, p. 15). BrainWave: joint scalp + iEEG pretraining beat single-modality pretraining in all tasks but one (p. 15).
- **Ablations:** removing Neuro-GPT's GPT-2 decoder *improved* downstream results. Brant's temporal encoder contributes most. LaBraM's spatial embeddings are needed for convergence (§4.3, p. 15).
- **TUAB may be saturated:** 85–87% accuracy is reached with traditional approaches (ref [155], Kiessner 2024) (§5.2, p. 18).
- **BrainWave** is the exception on evaluation breadth: 12 tasks, cross-site/subtype, few-shot, with a mean +0.21 AUC over LaBraM, BrainBERT and MOMENT (p. 14). Few-shot AUCs include ADHD-adult 0.90, MDD-64 0.90, AD-65 0.63 (Supp. Table 2, estimated from figures).

## Limitations (reported)
- The review covers early models up to Sep 2024 only. Scores are copied from papers with different protocols, and some are read off figures (Supp. Table 2).

## Recommendations (§5.2–6, pp. 18–21)
- Benchmark against **expert features and task-specific supervised models**, with statistical tests, identical **subject-level splits**, and **past/future temporal splits** for long recordings (§6.1, p. 20).
- Use clinically meaningful metrics, e.g. **false positives per hour** for seizure detection, keep the natural class imbalance, and report few-shot results in absolute label counts (§5.2, p. 18).
- Build community-specific benchmarks (clinicians vs BCI vs neuroscience) and use competitions. Ship frictionless software and model cards (§6.1, §6.3).
- Longer context (multi-day EEG), explicit spatial modeling, study preprocessing/normalization effects, distillation for real-time and edge use, federated pretraining (§5.2, §6.2).
- Translational hurdles: prospective site-specific validation, interpretability, reproducibility of splits and data, medical-device regulation (§6.3, p. 21).

## Assessment 🤖
- 🤖 The main value is calibration. As of late 2024 the FM literature had no common test bed, no OOD testing in 8/10 papers and almost no classical baselines, so the leaderboard claims in [[jiang2024large]] and [[wang2024cbramod]] are within-protocol only.
- 🤖 The linear-probe gap is the key finding for Q7. "Foundation" in the NLP sense (frozen features that transfer) is not yet demonstrated for EEG. What is shown is a good *initialization* for fine-tuning.
- 🤖 Their claim that only BIOT handles multiple montages seems to undersell LaBraM, which patches channels separately with electrode embeddings over the 10–20 superset [[jiang2024large]] (§2.1). The disagreement is about whether a subset of a fixed superset counts as "variable".
- 🤖 Channel-hours favour high-density, short recordings. LaBraM's "80k channel-hours" is 2,535 h of recording.
- 🤖 The cutoff misses CBraMod, EEGPT and all 2025 benchmarks. Those (EEG-Arena, NeuroAtlas, EEG-FM-Compass) are the direct test of these recommendations → reading queue.
- 🤖 BrainWave's clinical few-shot numbers (ADHD, MDD, schizophrenia) sit on small single-site sets, exactly the confounded setting of [[q6-reliability-of-eeg-diagnoses]].

## Concepts
- [[self-supervised-pretraining]]: the field-level picture of EEG-FMs; the masked-reconstruction default, weak probes and weak scaling.
- [[evaluation-protocols]]: in-distribution vs OOD; LP / FT / few-shot / zero-shot taxonomy (Supp. Table 2); demands subject-level and temporal splits.
- [[channel-heterogeneity]]: three montage strategies (fixed channel set, positional encodings, per-channel tokens).
- [[eeg-preprocessing-pipeline]]: FMs pretrain on minimally preprocessed EEG with no artifact removal.
- [[seizure-detection]]: calls for false alarms/hour and natural imbalance instead of balanced metrics.
- [[time-frequency-analysis]]: spectrogram / superlet inputs (BrainBERT, BrainWave).
- [[classical-ml-baselines]]: only 4 of 10 FM papers compare with expert-feature ML.

## Related papers
- [[chen2026benchmarking]]: EEG-Arena (2026) confirms no model-size scaling across 30 FMs, but finds sustained gains from pretraining hours with the architecture fixed (REVE-base, Fig. 6).
- [[liu2026eeg]]: a 2026 matched benchmark of 12 FMs that confirms this review's inferences (weak probes, no scaling, specialists competitive).
- [[jiang2024large]]: LaBraM, one of the 10. It leads TUAB/TUEV, possibly because of data diversity. Its linear probe is weak.
- [[yang2023biot]]: BIOT, the smallest (3.3M) and the only contrastive one.
- [[weng2025self]]: cited as a prior survey (ref [26]) that focuses on architectures and SSL objectives; this review adds data and evaluation.
- [[wang2024cbramod]]: published after the cutoff, not covered.
- [[roy2019deep]], [[lawhern2018eegnet]]: cited as the supervised EEG-DL era (refs [2], [78]).
- [[banville2020uncovering]]: cited (ref [6]) for SSL reducing label dependence.
- [[xie2026specbram]]: adds a direct data-scale null (full TUEG ≈ 2,388 h subset, App. C) and the kind of matched target ablation the review calls for.

## Q&A notes
