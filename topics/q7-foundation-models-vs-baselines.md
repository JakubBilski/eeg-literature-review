---
slug: q7-foundation-models-vs-baselines
kind: hub
status: active
updated: 2026-10-12
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
- **Historical DL gain over classical pipelines was modest and overstated:** median +5.4% accuracy (2010–2018), against often weak baselines; only 2 studies used Riemannian methods. → [[classical-ml-baselines]] ([[roy2019deep]])
- **Before foundation models, small CNN vs classical was already a split decision:** with matched splits, EEGNet beat xDAWN + Riemannian on P300 and MRCP but lost on cross-subject ERN, and tied FBCSP within-subject on motor imagery [[lawhern2018eegnet]] (Figs. 2–5). → [[classical-ml-baselines]]
- **Pretraining adds little on motor imagery:** CBraMod 0.642 vs 0.620 without pretraining (same architecture), and EEGNet (3k params) 0.581 on PhysioNet-MI 4-class, cross-subject [[wang2024cbramod]] (Tables 3–4). On depression, EEGNet 0.923 vs CBraMod 0.956 (Table 10). On sleep staging (ISRUC, 5-class), κ is EEGNet 0.704, USleep 0.721 (a dedicated supervised sleep model), LaBraM 0.723 and CBraMod 0.744 (Table 7). → [[classical-ml-baselines]], [[sleep-staging]]
- **Seizure detection (CHB-MIT, subject split) is where pretraining helps most so far:** balanced accuracy EEGNet 0.566, Conformer 0.598, BIOT 0.707, LaBraM 0.708, CBraMod 0.740. AUC-PR roughly doubles (0.19 → 0.37) [[wang2024cbramod]] (Table 8). Caveats: the test set is 2 subjects, and LaBraM pretrained on TUSZ (other seizure data) [[jiang2024large]] (App. D). → [[seizure-detection]]
- **Foundation-model papers compare against deep baselines only.** FBCSP and Riemannian pipelines are missing from their own papers. *Partly filled 2026-10-11:* [[liu2026eeg]] runs CSP/xDAWN/PSD/TRCA pipelines, but no Riemannian or FBCSP. → [[classical-ml-baselines]]
- **The SSL literature before foundation models doesn't settle it either:** the main survey of ≈70 EEG SSL methods reports no performance numbers or SSL-vs-supervised comparisons [[weng2025self]] (Tables 1–4). Frozen-encoder evaluation ("UT" mode) was common in that period (§2.2).
- **Frozen embeddings can be weak:** LaBraM linear probe 0.346 vs 0.641 fine-tuned on TUEV [[jiang2024large]] (Table 10). → [[self-supervised-pretraining]]
  - **This holds across the field:** every early FM that reports both shows a large probe → fine-tune gap (BrainBERT AUC 0.59 → 0.83, FoME TUEV F1 ~46 → 79, Neuro-GPT on BCI IV-2a 44.3% → 64.5%), and Neuro-GPT's probe falls *below* supervised baselines [[kuruppu2026eeg]] (Supp. Table 2; §4.3, p. 13).
- **Hand-crafted band power ≈ published FM frozen features on sleep staging.** Strict linear probe, balanced accuracy at 100% of labels: ISRUC 5-band power 0.742 vs LaBraM-Base 0.752, BIOT 0.736, CBraMod 0.729; HMC 5-band 0.682 vs BIOT 0.658, LaBraM 0.633, CBraMod 0.620. A "rich" hand-crafted set beats all three (0.763 / 0.723), and a band-power-target FM beats everything (0.792 / 0.742) [[xie2026specbram]] (Table 5). With 1% of labels, 5-band power leads all published FMs (ISRUC 0.707 vs ≤0.680). 🤖 Caveats: sleep stages are defined by spectral content, so band power is task-aligned; and probing official weights under the authors' preprocessing (10 s windows, 256 Hz, per-recording robust normalization) may disadvantage them. Fine-tuned FMs still beat EEGNet (ISRUC 0.763 LaBraM vs 0.715; Table 6).
- **The same pattern in ECG (method parallel):** HuBERT-ECG compares mostly against numbers quoted from papers that used other label subsets, with no classical-feature baseline. On PTB-XL it trails supervised and other SSL models (0.911 vs 0.925–0.947), and freezing the encoder was not effective [[coppola2024hubert]] (Supp. Table 10, p. 16).
- **Field audit up to Sep 2024:** after fine-tuning, FMs give "at least some improvement, if not drastic" over supervised DL; expert-feature baselines appear in only 4 of 10 papers; scaling evidence is "weak, if any" [[kuruppu2026eeg]] (Fig. 4, §5.1). General time-series FMs not trained on EEG sometimes beat EEG-FMs (p. 17). 🤖 This is the pre-benchmark picture; [[liu2026eeg]] (top bullet) confirms it under matched protocols, and [[chen2026benchmarking]], [[kontras2026neuroatlas]], [[zare2026negative]] are still to read.
- **Matched protocols matter more than models:** shuffled vs held-out-block vs cross-subject splits move CSP + LDA from 0.83 to 0.64 to 0.56 on one task (own test). → [[eegmmi-imagined-vs-executed]], [[evaluation-protocols]]

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
- Own test planned: frozen CBraMod + linear probe vs CSP + LDA, Riemannian and EEGNet on EEGMMI left vs right imagery, few-shot → [[eegmmi-frozen-probe]].
- Literature: a benchmark paper that runs Riemannian/FBCSP alongside foundation models on matched splits. *Searched 2026-10-11:* [[liu2026eeg]] read (CSP/xDAWN/PSD/TRCA but no Riemannian). Still to read: [[chen2026benchmarking]] (25 supervised baselines), [[wang2026eeg]] (tuned baselines), [[zare2026negative]] (classical features), [[xiong2025eeg]] (EEG-FM-Bench). Lotte 2018 for classical baselines (reading queue).
- Does pretraining help more for clinical tasks (TUAB/TUEV) than for BCI?

## Sources
- [[liu2026eeg]]: EEG-FM-Compass; matched benchmark, 12 FMs vs 8 specialists, LOSO + few-shot, probe vs fine-tune, ranks + significance.
- [[xie2026specbram]]: matched pretext-target study; hand-crafted band power vs FM frozen features on sleep (Tables 2, 5, 6) *(key tables read; no paper note yet)*.
- [[kuruppu2026eeg]]: review of 10 early EEG-FMs; probe vs fine-tune across models, scaling, classical baselines rarely tested.
- [[weng2025self]]: SSL survey; training modes (fine-tune / joint / frozen); no quantitative comparison.
- [[coppola2024hubert]]: ECG parallel; quoted-number baselines, weak frozen features.
- [[roy2019deep]]: DL vs traditional baselines meta-analysis.
- [[lawhern2018eegnet]]: EEGNet itself; matched comparison with xDAWN+RG and FBCSP.
- [[wang2024cbramod]]: baseline tables and pretraining ablation *(paper note not yet written)*.
- [[jiang2024large]]: linear probe vs fine-tune; pretraining corpus.
- [[song2022eeg]]: FBCSP vs Conformer on BCI IV-2a.
- [[varbu2022past]]: LDA/SVM as the BCI default (2009–2019).
- [[classical-ml-baselines]], [[evaluation-protocols]], [[self-supervised-pretraining]], [[common-spatial-patterns]], [[riemannian-methods]].
