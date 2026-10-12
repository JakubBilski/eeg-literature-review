---
citekey: chen2026benchmarking
title: "Benchmarking EEG Foundation Models at Scale: Lessons from 20,000 Evaluations"
authors: [Zhige Chen, Shu Peng, Chengxuan Qin, Rui Liu, Rui Yang, Kay Chen Tan, Jibin Wu]
year: 2026
venue: "arXiv preprint"
doi: ""
arxiv: "2609.32743"
pmid: ""
field: eeg
paper_type: benchmark
task: "EEG-Arena: 30 FM checkpoints vs 25 supervised baselines on 57 tasks / 23 datasets in 7 paradigms (MI, sleep, clinical, cognitive, AAD, ERP, emotion); pretraining gain, model-size and data scaling, channel robustness"
datasets: [BCIC-IV-1, BCIC-IV-2A, BCIC-IV-2B, PhysioNet-MI, Large-MI, SHU-MI, Stroke-MI, Meng2019, HGD, OpenBMI, CAP-Sleep, HMC-Sleep, UCDDB-Sleep, TUSL, TUEV, MigraineDB, EEGMat, KUL-AAD, DTU-AAD, ERP-BCI, Kaggle-INRIA, SEED, FACED]
n_subjects:
n_channels:
model_type: "30 FM checkpoints (BENDR, BIOT×3, EEGPT, LaBraM, NeuroGPT, CBraMod, CSBrain, EEGMamba, HEAR×2, LEAD, LUNA×3, mdJPT, NeuroRVQ, REVE×2, CodeBrain, ST-EEGFormer×3, SleepFM×3, SleepGPT, TFM, Uni-DMFM) vs 24 supervised DL models + YASA"
eval_protocol: "within-subject (WS) and cross-subject (CS) splits; best-validation checkpoint; full fine-tuning, linear probe, scratch training; label budgets 2–100%; pretraining-overlap results excluded"
main_metric: "average rank over balanced accuracy, macro-F1 and Cohen's kappa; top-5 count"
main_result: "FMs beat supervised baselines on most tasks, most clearly on non-bipolar data (REVE-base, ST-EEGFormer-small, LEAD, HEAR-large lead) (§3.1, Fig. 2); REVE-base 600→30,000 h pretraining: +6.69 / +4.22 points full fine-tune WS / CS (Fig. 6a, p. 13)"
code_available: "eeg.fm/benchmarks (leaderboard eeg.fm/leaderboards)"
read_depth: full
concepts: [self-supervised-pretraining, evaluation-protocols, channel-heterogeneity, sleep-staging, bci-paradigms]
---

# EEG-Arena (Chen, Peng, Qin … Wu, arXiv 2026)

## TL;DR
The largest FM benchmark so far: 30 FM checkpoints vs 25 supervised baselines on 57 tasks. FMs win most tasks, and pretraining beats the same architecture trained from scratch. Model size doesn't predict performance, but more pretraining hours for one fixed model (REVE-base, 600 → 30,000 h) do. No seeds, no significance tests and no classical (CSP/Riemannian) baseline, so it doesn't overturn [[liu2026eeg]].

*Read from arXiv v1 (26 Sep 2026; 17 pp. main + appendix to p. 91). Group: PolyU Hong Kong (Jibin Wu). None of the evaluated FMs are from this group (Uni-DMFM is a different Chen, Pattern Recognition 2026).*

## Research question
Five research questions, each with its own protocol (Fig. 1C, p. 3):
- **RQ1:** Do FMs beat strong task-specific supervised baselines?
- **RQ2:** How much does pretraining help, compared with the same architecture trained from scratch, at the first epoch, at the final epoch and across label budgets?
- **RQ3:** Does performance scale with parameter count?
- **RQ4:** Does performance scale with pretraining hours when the architecture is fixed?
- **RQ5:** How robust are channel-constrained vs channel-flexible FMs when channels are removed?

## Data & preprocessing
- **23 datasets, 57 tasks, 7 paradigms** (Table 4, pp. 24–26). MI (10 datasets incl. Large-MI with 7 tasks); sleep (CAP 10 tasks incl. 4-s epochs and CAP A-phases, HMC, UCDDB); clinical (TUSL slowing, TUEV events, MigraineDB with 9 tasks); EEGMat; AAD (KUL, DTU); ERP (P300, feedback error); emotion (SEED, FACED).
  - Table 4 also lists TUAB, TUEP, TUSZ, TUAR, CHB-MIT and Sleep-EDF, but no results for them appear anywhere (App. E.1 tables, Fig. 3). The paper doesn't say why.
- **FM preprocessing:** each FM keeps its own sampling rate, filters, normalisation and patching (Table 7a, p. 27). For example, CBraMod uses 200 Hz, 0.3–75 Hz, ÷100 µV and rejects segments above 100 µV; REVE uses session-wise z-score with a ±15σ clip.
- **Baselines:** one unified pipeline: 200 Hz, 0.1–75 Hz, 50 Hz notch, channel-wise z-score (Table 7b).
- **Data layer:** files are converted to HDF5. It supports WS, CS and leave-one-subject-out splits, plus 10-20 / 10-10 / 10-5 / dynamic channel selection (§2.1, p. 4).

## Method
- **Models** (Table 2, p. 4; Tables 5–6, pp. 26–27):
  - FMs range from 1.0M (mdJPT) to 408M (REVE-large) parameters. They split into *channel-constrained* (fixed montage) and *channel-flexible* (electrode or position encodings: HEAR, LEAD, LUNA, REVE, SleepFM, Uni-DMFM).
  - Baselines are EEGNet, Shallow/DeepConvNet, Conformer, ATCNet, FBCNet, IFNet and others for MI; EEGInceptionERP; TSception/BiDANN/HSLT for emotion; DeepSleepNet/SleepEEGNet/U-Sleep/SleepTransformer for sleep; EEGWaveNet/SlimSeiz for epilepsy. YASA (spectral features, sleep) is the only traditional model.
- **Protocol I:** every compatible model runs on identical train/val/test splits; the checkpoint with the best validation score is tested (§2.1, p. 4). Ranking is done separately for bipolar and non-bipolar tasks (Eq. 1–2, p. 5).
- **Protocol II:** Full-FT vs architecture-matched Scratch-ST (random init) for 10 FMs, at label budgets {2, 5, 10, 25, 50, 100}% with fixed val/test sets. Gain Ḡ(d) = mean Full-FT score − mean Scratch-ST score (Eq. 3–4, pp. 5–6).
- **Protocol III:** Full-FT and linear probe (frozen backbone, head only) across model variants. The authors call this observational: architecture, data and recipe differ between models (p. 6).
- **Protocol IV:** REVE-base pretrained on 600, 1,500, 3,000, 7,500, 15,000 and 30,000 h with the architecture, objective and optimiser fixed (p. 7). The adaptation is measured with relative parameter displacement ‖θpost−θpre‖/‖θpre‖ (Eq. 5) and 1 − CKA per layer (Eq. 6).
- **Protocol V:** 10 FMs on task-informed channel subsets, e.g. central electrodes for MI and centro-parietal for P300. Performance is plotted against the retained-channel ratio (Eq. 7, p. 8; Tables 51–52).
- **Proposed reporting:** 8 dimensions (Table 3, p. 15): bipolar rank, non-bipolar rank, final-epoch gain, first-epoch gain, low-label performance, channel coverage, parameter efficiency and throughput. They are combined with user-chosen weights (pp. 15–16).

## Evaluation
- **Metrics:** balanced accuracy, Cohen's κ and macro-F1 per task (App. E.1).
- **Leakage:** results are excluded from rankings when a model's pretraining data overlap the downstream dataset (red "E" in Fig. 3; §2.1, p. 4).
- **Not reported:** number of seeds, error bars, significance tests, hyperparameter search or how the WS split is made (no mention in the main text or appendix).

## Results (with locations)
- **RQ1:** "EEG FMs outperform strong supervised baselines on most evaluated tasks, with the largest advantages observed under non-bipolar channel configurations" (§3.1, p. 9).
  - Non-bipolar leaders: REVE-base, ST-EEGFormer-small, LEAD, HEAR-large.
  - Bipolar leaders: the BIOT variants (lowest average rank), then REVE-base and SleepFM. SleepEEGNet has the most top-5 placings, partly because it runs on more bipolar tasks than the FMs (Fig. 2, p. 9).
- **Own tally from Fig. 3 (p. 10; first metric column, 🤖 parsed from the PDF text):** across 104 task × split rows, the best FM beats the best baseline on 90. The median margin is +5.9 points within-subject (n = 57) and +2.5 cross-subject (n = 47).
  - Where baselines win: BCIC-IV-2A 4-class and L/R (SleepEEGNet; cross-subject L/R −9.2), CS TUEV event types (TMSA-Net, −10.1), several UCDDB sleep tasks and CAP 4-s epochs.
  - The biggest FM margins are within-subject DTU-AAD (+25 to +49, NeuroRVQ) and CS TUSL 3-class (+35, CodeBrain).
  - Most frequent winners: REVE-base 18, NeuroRVQ 13, ST-EEGFormer-small 12, Uni-DMFM 11, SleepEEGNet 8, CBraMod 8.
- **RQ2:** 8 of 10 FMs gain at the first epoch, and all 10 by the final epoch (Fig. 4a, p. 11). The mean final-epoch gain grows from 0.4% at 2% labels to 8.2% at 100%, and every model gains once d ≥ 25% (Fig. 4b, p. 11).
- **RQ3:** no consistent size trend under either Full-FT or linear probe. REVE-base beats REVE-large (bipolar), and REVE-base and ST-EEGFormer-small beat their larger variants (non-bipolar) (Fig. 5, p. 12).
- **RQ4:** going from 600 to 30,000 h improves REVE-base on average (Fig. 6a, p. 13):

  | split | Full-FT | Linear probe |
  |---|---|---|
  | within-subject | +6.69 | +5.97 |
  | cross-subject | +4.22 | +1.89 |

  - With more data, parameter displacement shrinks while output-level representation change grows (Fig. 6b).
  - Adaptation also spreads from the final layers into the intermediate layers once pretraining reaches 15–30k h; early layers stay stable (Fig. 6c, p. 13).
- **RQ5:** channel-flexible FMs have higher absolute performance than channel-constrained ones at most retained-channel ratios (Fig. 7, p. 14).
- **Profiles:** REVE-base is strong on rank and low-label performance; HEAR-large has a large final-epoch gain; CBraMod has broad coverage and high throughput; LEAD is parameter-efficient (Fig. 8, p. 16).

## Limitations (reported)
- The size analysis is observational, since checkpoints differ in architecture, data and recipe (pp. 6, 13, 17).
- Comparing bipolar-native models such as BIOT with non-bipolar ones may underestimate the former (p. 11).
- Channel reduction is structured and task-informed. Arbitrary dropout, re-referencing and device variation are untested (p. 17).
- The data-scaling series covers one model family and one objective (p. 17).

## Assessment 🤖
- 🤖 **The main disagreement with [[liu2026eeg]] has protocol explanations:**
  - Most rows are within-subject, where FM margins are largest (median +5.9 vs +2.5 cross-subject). Liu's within-subject setting was few-shot, while here WS uses the full training split.
  - Results come from single runs with no significance testing, and the best-of-30 FMs is compared against the best-of-25 baselines.
  - The checkpoint is chosen on validation data, whereas Liu reports the final epoch.
  - Baselines get one unified preprocessing pipeline, and their hyperparameters aren't described.
  - CS margins of +2.5 points without error bars fit Liu's "comparable, not significant".
- 🤖 **Failed runs, visible in the appendix** (counted in *Q&A*). Many baseline cells sit exactly at chance (B-ACC 50.00, κ 0.00; e.g. ADFCNN, ATCNet, HSLT in Tables 8–26), and so do some FM Full-FT cells at low budgets (Table 27). That points to failed training runs rather than real model limits, and failed runs inflate both the RQ1 margins and the RQ2 "pretraining gain".
- 🤖 **No classical pipeline** apart from YASA: no CSP/FBCSP, Riemannian tangent space or band power + LDA. On the Q7 question of FMs vs *classical* baselines, this paper adds nothing.
- 🤖 **The within-subject AAD and emotion margins look like leakage.** DTU-AAD WS +49 points and SEED WS at 94% for ST-EEGFormer are typical of WS splits where train and test windows come from the same trial or clip. With no description of the WS split, these rows can't be trusted → [[evaluation-protocols]].
- 🤖 **The data-scaling result is the most useful new evidence** (one architecture, six data sizes). But:
  - The pretraining corpus at each size is not described: which datasets, how subsampled, and whether it overlaps downstream.
  - The curve is reported for a 50× range only.
  - The cross-subject linear-probe gain is small (+1.89).
  - It holds for one objective only. It is still the only controlled data series in the vault → [[q9-pretraining-objectives-and-scale]].
- 🤖 **Six datasets listed but missing** (TUAB, TUSZ, CHB-MIT, Sleep-EDF and others): probably dropped for pretraining overlap (most FMs pretrain on TUEG), but that is unstated. So the most-used clinical benchmarks are absent from the rankings.

## Concepts
- [[self-supervised-pretraining]]: architecture-matched pretrain vs scratch gain by label budget; controlled data scaling on REVE-base.
- [[evaluation-protocols]]: WS/CS rankings; exclusion of overlapping pretraining data; best-validation checkpoint; no seeds or significance.
- [[channel-heterogeneity]]: channel-flexible vs channel-constrained FMs under channel reduction (RQ5).
- [[sleep-staging]]: bipolar sleep tasks favour BIOT/SleepFM, and SleepEEGNet is the strongest baseline.
- [[bci-paradigms]]: MI is the largest task block (10 datasets); BCIC-IV-2A is where baselines still win.

## Related papers
- [[classical-ml-baselines]] (topic): only YASA as a traditional model; no CSP/Riemannian.
- [[liu2026eeg]]: the competing matched benchmark (FMs ≈ specialists, not significant). This paper reaches the opposite headline under weaker statistics.
- [[kuruppu2026eeg]]: its "scaling evidence weak" is confirmed for model size. Pretraining data scale is a new positive result.
- [[xie2026specbram]]: data-scale null (2,388 h vs all of TUEG ≈17.7k h, sleep, App. C); here +4–7 points over 600 → 30k h. Different model, objective, range and tasks, so not a direct contradiction.
- [[jiang2024large]], [[wang2024cbramod]], [[yang2023biot]], [[wang2024eegpt]]: among the evaluated FMs. BIOT leads the bipolar ranking.
- [[ouahidi2025reve]]: REVE-base is the top non-bipolar FM and the backbone of the data-scaling series.
- [[lawhern2018eegnet]]: EEGNet as a baseline; rarely in the top 3 here.
- [[kontras2026neuroatlas]], [[xiong2025eeg]], [[lu2026omnieeg]], [[banville2026neuralbench]]: other benchmarks in Table 1.

## Q&A notes
- 2026-10-12 **Q:** Is the pretrain-vs-scratch result at 2% just both models failing to converge? **A:** Mostly yes. Re-tally of Tables 27–31 (9 datasets, `scripts/eegarena_tally.py`): runs with Cohen's κ exactly 0 (constant prediction) at 2 / 25 / 100% of labels are Full-FT 40 / 11 / 9 of 98, Scratch-ST 33 / 15 / 9 of 89, linear probe 43 / 26 / 18 of 98, supervised baselines 11 / 6 / 5 of 43. Mean balanced accuracy at 2% is 46.1 (Full-FT) vs 47.0 (scratch), at 100% 64.0 vs 56.5. EEGNet sits at chance on EEGMat at every budget (Table 27), though EEGMat is easy elsewhere ([[liu2026eeg]]: CSP+LDA 95.6). 🤖 The "gain grows with labels" curve mostly shows that the shared training recipe fails at small budgets. The gain at 100% (~7–8 points) involves similar collapse rates in both arms, so it is more credible. The "FMs help most when labels are scarce" claim can't be tested from these runs. A linear probe collapsing in 18% of full-data runs points to the recipe (no per-model LR or class weighting), not to the features alone.
- 2026-10-12 **Q:** What is "bipolar data"? **A:** Channels stored as differences of electrode pairs (clinical TCP chains; sleep PSG derivations such as C4−M1, Fpz−Cz), with no per-electrode position → [[q2-measuring-devices]] *Referential vs bipolar*.
- 2026-10-12 **Q:** Does adaptation spreading into middle layers depend on the amount of pretraining data? **A:** Yes, that is exactly what Fig. 6c varies: at 600–3,000 h, fine-tuning changes mainly the last layers; at 15–30k h, intermediate layers change too; early layers stay stable at every size (p. 13). Other-domain comparison → [[q9-pretraining-objectives-and-scale]] *Where fine-tuning changes the network*.

