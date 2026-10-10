---
slug: q5-state-of-the-art
kind: hub
status: stub
updated: 2026-10-10
---

# q5-state-of-the-art

> What is the current state of the art in EEG analysis?

## Current answer
- As of ICLR 2024, **LaBraM** reported the best results on clinical TUH benchmarks: TUAB balanced accuracy 0.8258 and TUEV 0.6616 (Huge), vs BIOT 0.7959 / 0.5281 [[jiang2024large]] (Tables 1–2).
- For per-subject motor imagery without pretraining, **EEG Conformer** reported 78.66% on BCI IV-2a and 84.63% on 2b [[song2022eeg]] (Tables II–III). It is now a common baseline.
- 🤖 These numbers are not one leaderboard. The protocols differ (within-subject vs cross-patient, window CV vs trial split) → [[evaluation-protocols]]. "SOTA" in EEG has to be stated per task and per protocol.
- 🤖 Newer foundation models (CBraMod, EEGPT) claim to improve on LaBraM. Not yet read.

## Comparisons
| task (protocol) | best in vault | score | source |
|---|---|---|---|
| TUAB abnormal (cross-patient) | LaBraM-Huge | BA 0.8258, AUROC 0.9162 | [[jiang2024large]] Table 1 |
| TUEV events (cross-patient) | LaBraM-Huge | BA 0.6616, κ 0.6745 | [[jiang2024large]] Table 2 |
| BCI IV-2a MI (within-subject) | Conformer | 78.66%, κ 0.7155 | [[song2022eeg]] Table II |
| BCI IV-2b MI (within-subject) | Conformer | 84.63%, κ 0.6926 | [[song2022eeg]] Table III |

## Open threads
- Read [[wang2024cbramod]] (downloaded) and [[wang2024eegpt]] (needs manual download) for post-LaBraM results.
- Is there a common benchmark suite for foundation models?

## Sources
- [[jiang2024large]]: foundation-model SOTA on TUH (2024).
- [[song2022eeg]]: non-pretrained SOTA on motor imagery (2022).
