---
slug: q7-foundation-models-vs-baselines
kind: hub
status: stub
updated: 2026-10-11
---

# q7-foundation-models-vs-baselines

> How much do EEG foundation models actually beat strong classical (CSP/FBCSP, Riemannian, LDA) and small supervised (EEGNet) baselines under matched protocols: same split, same subjects, same amount of labelled data (incl. few-shot / frozen-embedding probes)?

*Added 2026-10-10 at the human's request, after the theme came up in 3 questions across 2 sessions. Facts live in the linked notes; this hub summarizes them.*

## Current answer
- **Historical DL gain over classical pipelines was modest and overstated:** median +5.4% accuracy (2010–2018), against often weak baselines; only 2 studies used Riemannian methods. → [[classical-ml-baselines]] ([[roy2019deep]])
- **Before foundation models, small CNN vs classical was already a split decision:** with matched splits, EEGNet beat xDAWN + Riemannian on P300 and MRCP but lost on cross-subject ERN, and tied FBCSP within-subject on motor imagery [[lawhern2018eegnet]] (Figs. 2–5). → [[classical-ml-baselines]]
- **Pretraining adds little on motor imagery:** CBraMod 0.642 vs 0.620 without pretraining (same architecture), and EEGNet (3k params) 0.581 on PhysioNet-MI 4-class, cross-subject [[wang2024cbramod]] (Tables 3–4). On depression, EEGNet 0.923 vs CBraMod 0.956 (Table 10). On sleep staging (ISRUC, 5-class), κ is EEGNet 0.704, USleep 0.721 (a dedicated supervised sleep model), LaBraM 0.723 and CBraMod 0.744 (Table 7). → [[classical-ml-baselines]], [[sleep-staging]]
- **Seizure detection (CHB-MIT, subject split) is where pretraining helps most so far:** balanced accuracy EEGNet 0.566, Conformer 0.598, BIOT 0.707, LaBraM 0.708, CBraMod 0.740. AUC-PR roughly doubles (0.19 → 0.37) [[wang2024cbramod]] (Table 8). Caveats: the test set is 2 subjects, and LaBraM pretrained on TUSZ (other seizure data) [[jiang2024large]] (App. D). → [[seizure-detection]]
- **Foundation-model papers compare against deep baselines only.** FBCSP and Riemannian pipelines are missing, so the gap to a strong classical pipeline is unknown. → [[classical-ml-baselines]]
- **Frozen embeddings can be weak:** LaBraM linear probe 0.346 vs 0.641 fine-tuned on TUEV [[jiang2024large]] (Table 10). → [[self-supervised-pretraining]]
- **Matched protocols matter more than models:** shuffled vs held-out-block vs cross-subject splits move CSP + LDA from 0.83 to 0.64 to 0.56 on one task (own test). → [[evaluation-protocols]], [[bci-paradigms]]

## Comparisons
| model | type | PhysioNet-MI 4-class bal. acc. (cross-subject) | source |
|---|---|---|---|
| EEGNet | small CNN, supervised | 0.581 | [[wang2024cbramod]] Table 3 |
| EEG Conformer | CNN + Transformer, supervised | 0.605 | [[wang2024cbramod]] Table 3 |
| LaBraM-Base | foundation model (pretraining saw EEGMMI ⚠) | 0.617 | [[wang2024cbramod]] Table 3; [[jiang2024large]] App. D |
| CBraMod (no pretraining) | same architecture | 0.620 | [[wang2024cbramod]] Table 4 |
| CBraMod | foundation model | 0.642 | [[wang2024cbramod]] Table 3 |
| CSP + LDA / Riemannian | classical | — (not reported) | gap |

## Open threads
- Own test planned: frozen CBraMod + ridge vs CSP + LDA vs EEGNet on EEGMMI left-vs-right imagery, few-shot (k trials from a held-out subject). Plan → [[self-supervised-pretraining]] *EEGMMI as a frozen-embedding testbed*.
- Literature: a benchmark paper that runs Riemannian/FBCSP alongside foundation models on matched splits. Not searched yet. Lotte 2018 for classical baselines (reading queue).
- Does pretraining help more for clinical tasks (TUAB/TUEV) than for BCI?

## Sources
- [[roy2019deep]]: DL vs traditional baselines meta-analysis.
- [[lawhern2018eegnet]]: EEGNet itself; matched comparison with xDAWN+RG and FBCSP.
- [[wang2024cbramod]]: baseline tables and pretraining ablation *(paper note not yet written)*.
- [[jiang2024large]]: linear probe vs fine-tune; pretraining corpus.
- [[song2022eeg]]: FBCSP vs Conformer on BCI IV-2a.
- [[varbu2022past]]: LDA/SVM as the BCI default (2009–2019).
- [[classical-ml-baselines]], [[evaluation-protocols]], [[self-supervised-pretraining]], [[common-spatial-patterns]], [[riemannian-methods]].
