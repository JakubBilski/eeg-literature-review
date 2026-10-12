---
slug: q5-state-of-the-art
kind: hub
status: active
updated: 2026-10-12
---

# q5-state-of-the-art

> What is the current state of the art in EEG analysis?

## Current answer
- As of ICLR 2024, **LaBraM** reported the best results on clinical TUH benchmarks: TUAB balanced accuracy 0.8258 and TUEV 0.6616 (Huge), vs BIOT 0.7959 / 0.5281 [[jiang2024large]] (Tables 1–2).
- For per-subject motor imagery without pretraining, **EEG Conformer** reported 78.66% on BCI IV-2a and 84.63% on 2b [[song2022eeg]] (Tables II–III). It is now a common baseline.
- 🤖 These numbers are not one leaderboard. The protocols differ (within-subject vs cross-patient, window CV vs trial split) → [[evaluation-protocols]]. "SOTA" in EEG has to be stated per task and per protocol.
- 🤖 Newer foundation models (CBraMod, EEGPT) claim to improve on LaBraM. Not yet read.
- **As of Sep 2024, no field-wide leaderboard existed.** Only TUAB and TUEV are shared across EEG-FM papers, and only 4 of 10 models report them: fine-tuned TUAB AUC 0.86–0.92, TUEV F1 0.70–0.83, with LaBraM on top [[kuruppu2026eeg]] (Fig. 3, §5.1). Only BrainWave tested broadly (12 tasks, cross-site, few-shot). General time-series FMs (TimesNet, MOMENT) are sometimes competitive (p. 17). TUAB may be saturated (85–87% accuracy with traditional methods; §5.2).

- **As of mid-2026, no FM is the clear state of the art across paradigms.** In the largest matched benchmark (12 open FMs, 13 datasets), CBraMod has the best average rank, but EEGNet, Conformer, ShallowConv, Deformer and LMDA are statistically tied with it. Per-task winners are mostly specialists: EEGNet has the most first places (p. 20). The paradigm-specific MIRepNet leads MI (BNCI2014001 LOSO 54.2) [[liu2026eeg]] (Supp. Tables 16, 52). FMs that look strong on clinical data fail elsewhere: LUNA tops TUAB (81.9, but TUAB was in its pretraining) yet sits at chance on SSVEP (p. 17; Table 3).
- **EEG-Arena (Sep 2026; 30 FM checkpoints, 57 tasks):** REVE-base wins the most tasks (18 of 104 task × split rows in Fig. 3), then NeuroRVQ, ST-EEGFormer-small and Uni-DMFM. BIOT variants lead bipolar (sleep) tasks; channel-flexible FMs (REVE, LEAD, HEAR) lead non-bipolar ones [[chen2026benchmarking]] (§3.1, Figs. 2–3). No seeds or significance tests, and TUAB/TUSZ/CHB-MIT results are not reported. Public leaderboard at eeg.fm/leaderboards.
- 🤖 **SOTA now means "per task, per protocol, per calibration budget".** The LOSO and few-shot winners differ on most datasets [[liu2026eeg]] (Tables 2–3).

## Comparisons
| task (protocol) | best in vault | score | source |
|---|---|---|---|
| TUAB abnormal (cross-patient) | LaBraM-Huge | BA 0.8258, AUROC 0.9162 | [[jiang2024large]] Table 1 |
| TUEV events (cross-patient) | LaBraM-Huge | BA 0.6616, κ 0.6745 | [[jiang2024large]] Table 2 |
| BCI IV-2a MI (within-subject) | Conformer | 78.66%, κ 0.7155 | [[song2022eeg]] Table II |
| BCI IV-2b MI (within-subject) | Conformer | 84.63%, κ 0.6926 | [[song2022eeg]] Table III |
| BCI IV-2a MI (LOSO, 4-class) | MIRepNet | BA 54.21 | [[liu2026eeg]] Supp. Table 16 |
| BCI IV-2a MI (few-shot within-subject) | CSP + LDA | BA 60.62 | [[liu2026eeg]] Supp. Table 16 |
| TUAB (10-fold subject split, first 3 min) | LUNA-Base ‡ | BA 81.92 | [[liu2026eeg]] Table 2 |
| Sleep-EDFx (LOSO) | Deformer | BA 78.73 | [[liu2026eeg]] Table 3 |
| SSVEP Nakanishi2015 (few-shot) | TRCA | 98.77 | [[liu2026eeg]] Table 3 |

## Open threads
- Read [[wang2024cbramod]] (downloaded) and [[wang2024eegpt]] (needs manual download) for post-LaBraM results.
- Is there a common benchmark suite for foundation models? *As of Sep 2024: no* [[kuruppu2026eeg]] (§5.2). 2026: [[liu2026eeg]] read (a benchmark, but its code is only announced, so it is not yet a public leaderboard). [[chen2026benchmarking]] read 2026-10-12: code and a live leaderboard released, so this is the first public leaderboard, though without error bars. Queued: [[kontras2026neuroatlas]], [[xiong2025eeg]].

## Sources
- [[chen2026benchmarking]]: EEG-Arena benchmark and public leaderboard (30 FM checkpoints, 23 datasets, 2026).
- [[liu2026eeg]]: EEG-FM-Compass benchmark (12 FMs, 13 datasets, 2026).
- [[kuruppu2026eeg]]: review of 10 early EEG-FMs; the shared TUAB/TUEV comparison and evaluation gaps (2026).
- [[jiang2024large]]: foundation-model SOTA on TUH (2024).
- [[song2022eeg]]: non-pretrained SOTA on motor imagery (2022).
