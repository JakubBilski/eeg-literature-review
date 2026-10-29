---
slug: q7-foundation-models-vs-baselines
kind: hub
status: active
updated: 2026-10-25
---

# q7-foundation-models-vs-baselines

> How much do EEG foundation models actually beat strong classical (CSP/FBCSP, Riemannian, LDA) and small supervised (EEGNet) baselines under matched protocols: same split, same subjects, same amount of labelled data (incl. few-shot / frozen-embedding probes)?

*Added 2026-10-10 at the human's request, after the theme came up in 3 questions across 2 sessions. Facts live in the linked notes; this hub summarizes them.*

## Current answer
- **First independent matched benchmark (2026): FMs do not beat specialists significantly.** 12 open FMs vs 8 specialists, 13 datasets, LOSO + within-subject few-shot. Average ranks: CBraMod 6.56, EEGNet 7.40 (2K params), Conformer 7.40, ShallowConv 7.60 … LaBraM 9.36, classical 9.91. CBraMod vs the top CNNs is not significant (Nemenyi CD 4.94) [[liu2026eeg]] (Supp. Table 52, p. 72).
  - **LOSO:** FMs and specialists are comparable.
  - **Few-shot:** specialists win most tasks (p. 20). Where a standard classical pipeline exists, it wins few-shot outright: CSP+LDA 60.6 vs CBraMod 50.3 on 4-class MI with ~21 trials per class; TRCA 98.8 on SSVEP; CSP+LDA 95.6 on EEGMat (Tables 2–3).
  - **Linear probe < fine-tune** significantly for 9/12 FMs (Supp. Table 58).
  - **No size–rank correlation;** the top FMs are 0.16–5.8M params (p. 21).
  - 🤖 *Caveats:* classical baselines are weak choices outside MI/SSVEP/P300 (CSP+LDA on TUAB/SEED), there is no Riemannian tangent-space baseline, and classical is excluded from the significance test.
- **The largest benchmark (2026) reports the opposite headline, with weaker statistics.** EEG-Arena (30 FM checkpoints vs 24 DL baselines + YASA, 57 tasks) says FMs "outperform strong supervised baselines on most evaluated tasks", most clearly on non-bipolar data (REVE-base, ST-EEGFormer-small, LEAD, HEAR-large lead) [[chen2026benchmarking]] (§3.1, Fig. 2). Own tally of its Fig. 3: best FM > best baseline on 90 of 104 task × split rows, median margin +5.9 points within-subject but +2.5 cross-subject. Baselines still win BCIC-IV-2A MI and some sleep tasks.
  - 🤖 *Why the two benchmarks disagree:* EEG-Arena has no seeds, error bars or significance tests; it picks checkpoints on validation (Liu: final epoch); it compares best-of-30 FMs vs best-of-25 baselines; many baseline cells sit at chance (failed runs); its within-subject rows (largest margins, e.g. DTU-AAD +49) use an undescribed split; and it has no classical pipeline (CSP/Riemannian). The cross-subject margin of ~2.5 points fits Liu's "comparable". → [[chen2026benchmarking]] *Assessment*
  - **Pretraining vs the same architecture from scratch:** all 10 FMs tested gain by the final epoch; the mean gain is 0.4 points at 2% of labels and 8.2 at 100% (Fig. 4, p. 11). 🤖 This is the opposite of the usual "FMs help most when labels are scarce" claim, and it agrees with Liu's few-shot result.
  - Same direction with 25 seeds and tuned LRs: LaBraM-Base gains ≈ 0 on TUAB with 25 people, +3–4 points at moderate data, +1–2 at the most; on sleep +1 to +8 throughout [[bomatter2025limited]] (Figs. 5, 11). Pretrained LaBraM then matches small TCN/mAtt models; from scratch it is the worst of the three (Fig. 12).
- **Under frozen probes (the "out-of-the-box" promise) FMs mostly don't deliver (2026).** NeuroAtlas: 20 models, 42 datasets, linear probe on frozen features, clinical metrics [[kontras2026neuroatlas]].
  - **Seizures (7 cohorts, event-level sensitivity vs FA/h):** NeuroLM 0.553 and REVE 0.549 are the only models consistently top-3. Random-init CBraMod scores 0.440, the same as pretrained CBraMod, and 7 of 11 EEG-FMs are at or below it (Tables 3–4, pp. 32–33).
  - **EEG-FMs ≈ general time-series FMs** (Chronos, Moirai, MOMENT; never trained on EEG) in every domain (§5, p. 9). Moirai-L beats 9 of 11 EEG-FMs on seizures (App. D.2).
  - **Supervised models still win where they encode the task's structure:** sequence sleep models (top-3 on 15/15 cohorts, gap closed by an LSTM probe) and the feature-based Sun et al. brain-age model (Table 6, Table 11).
  - **End-to-end EEGNet (LOSO) beats the best frozen FM on 13 of 18 BCI tasks**, or 9 of 18 after confound filtering (App. D.7, pp. 48–49).
  - 🤖 The frozen-probe verdict agrees with [[liu2026eeg]]'s fine-tune verdict. Readout choice matters a lot (token flatten vs mean pool +7 points), and there are still no CSP/Riemannian baselines. → [[kontras2026neuroatlas]] *Assessment*
- **A strong classical baseline for TUAB-type screening exists and is hard to beat (no FM tested).** A CatBoost ensemble on band power + coherence + Riemannian features: AUC 92.2 on TUH, best single model up to ~24k multi-hospital recordings; supervised attention/transformer MIL networks (≤4.7M params, no SSL) pass it only at 55,787 recordings, by ~1 point (87.5 vs 86.5) [[poziomska2025quantity]] (Table B.5). 🤖 FM papers reporting TUAB should include this kind of baseline; recording-level aggregation (MIL) also mattered more than encoder choice there. → [[classical-ml-baselines]]
- **Text-supervised pretraining (EEG-CLIP) ≈ supervised on TUAB pathology, but not few-shot.** Frozen Deep4 + MLP 0.847 vs end-to-end Deep4 0.851; few-shot (fraction unstated) 0.710 vs 0.781 for training from scratch, with a win only on age (0.712 vs 0.621) [[ndir2025eeg]] (Tables 3, 5). 🤖 Single runs on 280 eval recordings, Deep4-only baselines, likely eval-set tuning; it fits the pattern that pretraining helps little when labels are scarce.
- **Historical DL gain over classical pipelines was modest and overstated:** median +5.4% accuracy (2010–2018), against often weak baselines; only 2 studies used Riemannian methods. → [[classical-ml-baselines]] ([[roy2019deep]])
- **Before foundation models, small CNN vs classical was already a split decision:** with matched splits, EEGNet beat xDAWN + Riemannian on P300 and MRCP but lost on cross-subject ERN, and tied FBCSP within-subject on motor imagery [[lawhern2018eegnet]] (Figs. 2–5). → [[classical-ml-baselines]]
- **Pretraining adds little on motor imagery:** CBraMod 0.642 vs 0.620 without pretraining (same architecture; the un-pretrained model already ties fine-tuned LaBraM-Base, 0.617; FACED +2.8, SHU-MI +0.8; Table 4), and EEGNet (3k params) 0.581 on PhysioNet-MI 4-class, cross-subject [[wang2024cbramod]] (Tables 3–4). On depression, EEGNet 0.923 vs CBraMod 0.956 (Table 10). On sleep staging (ISRUC, 5-class), κ is EEGNet 0.704, USleep 0.721 (a dedicated supervised sleep model), LaBraM 0.723 and CBraMod 0.744 (Table 7). → [[classical-ml-baselines]], [[sleep-staging]]
- **Seizure detection (CHB-MIT, subject split) is where pretraining helps most so far:** balanced accuracy EEGNet 0.566, Conformer 0.598, BIOT 0.707, LaBraM 0.708, CBraMod 0.740. AUC-PR roughly doubles (0.19 → 0.37) [[wang2024cbramod]] (Table 8). Caveats: the test set is 2 subjects, and LaBraM pretrained on TUSZ (other seizure data) [[jiang2024large]] (App. D). → [[seizure-detection]]
- **Foundation-model papers compare against deep baselines only.** FBCSP and Riemannian pipelines are missing from their own papers. *Partly filled 2026-10-11:* [[liu2026eeg]] runs CSP/xDAWN/PSD/TRCA pipelines, but no Riemannian or FBCSP. → [[classical-ml-baselines]]
- **The SSL literature before foundation models doesn't settle it either:** the main survey of ≈70 EEG SSL methods reports no performance numbers or SSL-vs-supervised comparisons [[weng2025self]] (Tables 1–4). Frozen-encoder evaluation ("UT" mode) was common in that period (§2.2).
- **Frozen embeddings can be weak:** LaBraM linear probe 0.346 vs 0.641 fine-tuned on TUEV [[jiang2024large]] (Table 10). → [[self-supervised-pretraining]]
  - **CBraMod too, even with an all-token head:** frozen backbone + classifier FACED 0.315 vs 0.551 fine-tuned, PhysioNet-MI 0.385 vs 0.642, SHU-MI 0.522 (≈ chance, 2 classes); frozen BIOT/LaBraM slightly lower. The authors: it "cannot currently serve as a fixed-parameter feature extractor" [[wang2024cbramod]] (App. J, Table 18).
  - **This holds across the field:** every early FM that reports both shows a large probe → fine-tune gap (BrainBERT AUC 0.59 → 0.83, FoME TUEV F1 ~46 → 79, Neuro-GPT on BCI IV-2a 44.3% → 64.5%), and Neuro-GPT's probe falls *below* supervised baselines [[kuruppu2026eeg]] (Supp. Table 2; §4.3, p. 13).
- **Hand-crafted band power ≈ published FM frozen features on sleep staging.** Strict linear probe, balanced accuracy at 100% of labels: ISRUC 5-band power 0.742 vs LaBraM-Base 0.752, BIOT 0.736, CBraMod 0.729; HMC 5-band 0.682 vs BIOT 0.658, LaBraM 0.633, CBraMod 0.620. A "rich" hand-crafted set beats all three (0.763 / 0.723), and a band-power-target FM beats everything (0.792 / 0.742) [[xie2026specbram]] (Table 5). With 1% of labels, 5-band power leads all published FMs (ISRUC 0.707 vs ≤0.680). 🤖 Caveats: sleep stages are defined by spectral content, so band power is task-aligned. Each baseline gets its own input convention (CBraMod/LaBraM at 200 Hz, µV/100; §5), but all are read out by mean-pooling tokens, which can hurt them: CBraMod's frozen backbone with its own all-token head gets 0.315 on FACED vs 0.171 mean-pooled (§6.4, Table 8). Fine-tuned FMs still beat EEGNet (ISRUC 0.763 LaBraM vs 0.715; Table 6).
  - **Beyond sleep the target's advantage fades.** Matched band-power vs raw-reconstruction: FACED +2.4, Mumtaz tie, PhysioNet-MI −0.9/+0.3, vigilance fine-tuned raw better (0.626 vs 0.587 Pearson) [[xie2026specbram]] (Tables 7–9). 🤖 A task-aligned target helps frozen features only where the label is a per-channel spectral state.
- **The same pattern in ECG (method parallel):** HuBERT-ECG compares mostly against numbers quoted from papers that used other label subsets, with no classical-feature baseline. On PTB-XL it trails supervised and other SSL models (0.911 vs 0.925–0.947), and freezing the encoder was not effective [[coppola2024hubert]] (Supp. Table 10, p. 16).
- **Field audit up to Sep 2024:** after fine-tuning, FMs give "at least some improvement, if not drastic" over supervised DL; expert-feature baselines appear in only 4 of 10 papers; scaling evidence is "weak, if any" [[kuruppu2026eeg]] (Fig. 4, §5.1). General time-series FMs not trained on EEG sometimes beat EEG-FMs (p. 17). 🤖 This is the pre-benchmark picture; [[liu2026eeg]] (top bullet) confirms it under matched protocols, [[chen2026benchmarking]] disputes it with weaker statistics, and [[kontras2026neuroatlas]] confirms it under frozen probes (EEG-FMs ≈ TS-FMs, p. 9). [[zare2026negative]] is still to read.
- **Matched protocols matter more than models:** shuffled vs held-out-block vs cross-subject splits move CSP + LDA from 0.83 to 0.64 to 0.56 on one task (own test). → [[eegmmi-imagined-vs-executed]], [[evaluation-protocols]]

## Saturated, noisy, or headroom? (asked 2026-10-25)
*The human's question: CBraMod's pretraining and architecture gains are both small (1–3 points). Is that because the tasks are noisy and saturated, or is there evidence that these tasks can be done better?*
- **Two different things.** *Noisy* means the benchmark can't resolve differences between models. *Saturated* means there is no headroom left given the labels. A task can be noisy without being saturated.
  - Noisy: CBraMod's ± are seed SDs of 1–2 points on fixed splits with 2–10 test subjects [[wang2024cbramod]] (App. E). In the matched benchmark the top-6 spread sits inside the Nemenyi CD of 4.94 rank units [[liu2026eeg]] (p. 72).
- **Headroom can be bounded without a better model,** using (a) label ceilings (inter-rater agreement), (b) learning curves in labelled subjects, and (c) a different method or protocol on the same data that scores much higher.
- **Near the ceiling (they rank models poorly):**
  - *Sleep (ISRUC):* κ 0.744 (CBraMod, Table 7) vs human–human κ 0.76 [[lee2021interrater]].
  - *TUAB:* CBraMod AUROC 0.923 / bal. acc. 0.829 (Table 14) vs fitted ceilings AUC∞ ≈ 91 and accuracy 85–87%, attributed to inter-rater agreement [[poziomska2025quantity]] (Table 4, §5); [[kuruppu2026eeg]] (§5.2).
  - *Bonn* (11 models ≥ 0.99 AUROC) [[kontras2026neuroatlas]] (App. D.1.3). *Mumtaz* (all models 0.91–0.96, 10 test subjects) can't be resolved either way.
- **Headroom shown on the same data, by something other than pretraining:**
  - *Cross-subject motor imagery:* on BCIC-IV-2a LOSO, the **same CBraMod** goes from 0.597 to 0.741 with EEG-SimpleConv's "key ingredients" (Euclidean alignment, session statistics, Mixup, subject-wise regularisation). EEG-SimpleConv goes from 0.565 to 0.722 [[wang2024cbramod]] (App. Q, Table 23). That is +14–16 points, about 5× the pretraining gain (+2.2, Table 4). Within-subject, Conformer reaches 78.7% on the same dataset [[song2022eeg]] (Table II). With ~21 calibration trials per class, CSP+LDA beats CBraMod (60.6 vs 50.3) [[liu2026eeg]] (Supp. Table 16).
  - *Seizures:* CHB-MIT AUC-PR is 0.37 at best (Table 8). On 7 continuous cohorts, event-level scores range 0.28–0.55 across models, with random init at 0.44 [[kontras2026neuroatlas]] (Table 4). A spread that wide is not a ceiling.
  - *Readout:* flattening tokens instead of mean pooling adds +7.0 points on BCI tasks and +22.5 on SSVEP [[kontras2026neuroatlas]] (App. D.8). Frozen-probe benchmarks therefore underestimate what the same encoders hold.
  - *More labelled subjects:* transformer MIL models on abnormal EEG show no saturation up to 55,787 recordings [[poziomska2025quantity]] (Fig. 11). People, not segments, drive TUAB and dementia [[bomatter2025limited]] (Fig. 3).
- **Unknown ceiling:** emotion (FACED 0.55, 9 classes) and vigilance. The labels are clip categories, self-reports or PERCLOS, with no published agreement figure, and the 0.9+ within-subject numbers are mostly leaky [[li2022eeg]] (Table 4). Some apparent signal may be confound: with an eye-movement/drift filter, frozen-FM motor imagery falls below significance for most EEG-FMs [[kontras2026neuroatlas]] (p. 8, Fig. 5a), though the filter also removes the first second of real ERD.
- 🤖 **Reading:**
  - The tasks are not uniformly saturated. Sleep and TUAB are at their label ceiling, so they shouldn't be used to rank FMs.
  - Where headroom is demonstrated (cross-subject BCI, seizures), what unlocks it is *subject alignment, calibration, readout and more labelled people*, not pretraining or model capacity.
  - So "FMs barely help" fits a better story than "the tasks are solved": current pretraining doesn't target the person-to-person shift that limits these tasks.
  - The question isn't naive. A partial answer is possible now, without a better model, by reporting each benchmark with its label ceiling and a subject-bootstrap noise floor.

## Comparisons
| model | type | PhysioNet-MI 4-class bal. acc. (cross-subject) | source |
|---|---|---|---|
| EEGNet | small CNN, supervised | 0.581 | [[wang2024cbramod]] Table 3 |
| EEG Conformer | CNN + Transformer, supervised | 0.605 | [[wang2024cbramod]] Table 3 |
| LaBraM-Base | foundation model (pretraining saw EEGMMI ⚠) | 0.617 | [[wang2024cbramod]] Table 3; [[jiang2024large]] App. D |
| CBraMod (no pretraining) | same architecture | 0.620 | [[wang2024cbramod]] Table 4 |
| CBraMod | foundation model | 0.642 | [[wang2024cbramod]] Table 3 |
| CSP + LDA / Riemannian | classical | — (not reported) | gap |

**BCI IV-2a / BNCI2014001, 4-class MI, balanced accuracy %** ([[liu2026eeg]] Supp. Table 16; 3 seeds, final epoch):

| model | LOSO (zero calibration) | few-shot within-subject (~21 trials/class) |
|---|---|---|
| CSP + LDA | 38.2 | **60.6** |
| EEGNet | 45.0 | 50.2 |
| TSception | 41.6 | 58.7 |
| Conformer | 41.6 | 57.2 |
| LaBraM | 46.9 | 37.1 |
| CBraMod | 53.0 | 50.3 |
| MIRepNet (MI-only FM) | **54.2** | — |

🤖 Different protocol from [[song2022eeg]]'s 78.7% for Conformer (full session 1 → session 2, same subject). With ~30% of one session, every model loses 20+ points.

## Open threads
- Headroom table: for each benchmark in [[liu2026eeg]] / [[kontras2026neuroatlas]], list the label ceiling (inter-rater κ) and a subject-bootstrap CI of the top score, to separate saturated from merely noisy tasks (2026-10-25; from *Saturated, noisy, or headroom?*). Seizure-annotation agreement is still unsourced.
- Own test planned: frozen CBraMod + linear probe vs CSP + LDA, Riemannian and EEGNet on EEGMMI left vs right imagery, few-shot → [[eegmmi-frozen-probe]].
- Literature: a benchmark paper that runs Riemannian/FBCSP alongside foundation models on matched splits. *Searched 2026-10-11:* [[liu2026eeg]] read (CSP/xDAWN/PSD/TRCA but no Riemannian). [[chen2026benchmarking]] read 2026-10-12: no classical pipeline except YASA. [[kontras2026neuroatlas]] read 2026-10-25: none either (only the Sun et al. sleep-feature brain-age model, which wins). Its ref [95] [[yang2026eeg]] (ICLR 2026, "Are EEG foundation models worth it? … traditional decoders") is the most direct candidate; it has no DOI/arXiv yet. Still to read: [[wang2026eeg]] (tuned baselines), [[zare2026negative]] (classical features), [[xiong2025eeg]] (EEG-FM-Bench). Lotte 2018 for classical baselines (reading queue).
- Does pretraining help more for clinical tasks (TUAB/TUEV) than for BCI?
- Benchmarks may be the bottleneck: no common task has objective labels, meaning, headroom and enough test subjects at once → [[eeg-labels-and-metadata]] (*Is the field missing a good downstream task?*).

## Sources
- [[poziomska2025quantity]]: classical feature ensemble vs supervised MIL networks on TUH and up to 55,787 multi-hospital recordings (no FMs).
- [[ndir2025eeg]]: EEG-CLIP; report-text contrastive pretraining vs supervised and single-task-transfer Deep4 on TUAB; zero-shot and few-shot.
- [[kontras2026neuroatlas]]: NeuroAtlas; frozen linear probe, 11 EEG-FMs vs 3 TS-FMs vs supervised + random init, 42 datasets, clinical metrics, LODO.
- [[chen2026benchmarking]]: EEG-Arena; 30 FMs vs 25 supervised baselines, 57 tasks, pretrain-vs-scratch by label budget, size and data scaling; no seeds or significance.
- [[liu2026eeg]]: EEG-FM-Compass; matched benchmark, 12 FMs vs 8 specialists, LOSO + few-shot, probe vs fine-tune, ranks + significance.
- [[bomatter2025limited]]: LaBraM pretrained vs scratch vs TCN/mAtt over a people × segments grid (TUAB, CAUEEG, sleep).
- [[xie2026specbram]]: matched pretext-target study; hand-crafted band power vs FM frozen features on sleep (Tables 2, 4–8); mean-pool probe caveat (§6.4).
- [[kuruppu2026eeg]]: review of 10 early EEG-FMs; probe vs fine-tune across models, scaling, classical baselines rarely tested.
- [[weng2025self]]: SSL survey; training modes (fine-tune / joint / frozen); no quantitative comparison.
- [[coppola2024hubert]]: ECG parallel; quoted-number baselines, weak frozen features.
- [[roy2019deep]]: DL vs traditional baselines meta-analysis.
- [[lawhern2018eegnet]]: EEGNet itself; matched comparison with xDAWN+RG and FBCSP.
- [[wang2024cbramod]]: baseline tables (13 datasets), pretraining ablation, frozen-backbone and 30%-label results (App. J–K). *(full read 2026-10-25)*
- [[jiang2024large]]: linear probe vs fine-tune; pretraining corpus.
- [[song2022eeg]]: FBCSP vs Conformer on BCI IV-2a.
- [[varbu2022past]]: LDA/SVM as the BCI default (2009–2019).
- [[classical-ml-baselines]], [[evaluation-protocols]], [[self-supervised-pretraining]], [[common-spatial-patterns]], [[riemannian-methods]].
