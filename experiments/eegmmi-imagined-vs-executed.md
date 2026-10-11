---
slug: eegmmi-imagined-vs-executed
status: done
questions: [q3, q6, q7]
concepts: [bci-paradigms, common-spatial-patterns, linear-discriminant-analysis, evaluation-protocols]
datasets: [eegmmi]
scripts: [scripts/plot_motor_erd.py, scripts/classify_imagery_vs_execution.py]
figures: [figures/eegmmi-imagined-vs-executed.png, figures/eegmmi-imagined-vs-executed-csp.png]
cost: low
origin: 2026-10-10, "how does imagined movement differ from executed movement?" ([[bci-paradigms]])
updated: 2026-10-12
---

# eegmmi-imagined-vs-executed

## Hypothesis
Imagined and executed fist movements share the contralateral mu/beta drop (ERD), with execution stronger. A CSP + LDA classifier should separate the two conditions, but part of any separability may come from recording-block differences and muscle activity rather than brain signal.

## Design
- **Data:** PhysioNet EEG Motor Movement/Imagery (EEGMMI), subjects 1–10, 64 channels. Left and right fist trials pooled, ~90 trials per subject (45 per class). Epochs 0.5–3.5 s after the cue.
- **Part 1, ERD:** band power vs pre-cue rest at C3/C4, right-fist trials, common-average reference (`plot_motor_erd.py`).
- **Part 2, classification:** CSP (6 components, shrinkage) + LDA, imagined vs executed (`classify_imagery_vs_execution.py`). Four splits: shuffled 5-fold; by block (leave one run pair out); a rest-period control (same pipeline on rest epochs of imagined vs executed runs, by block); cross-subject (leave one subject out). Two bands: 8–30 Hz (mu/beta) and 30–75 Hz (muscle).
- **Metric:** accuracy, mean ± SEM over subjects; chance 0.50.

## What each outcome would mean
- By-block ≈ shuffled, and the rest control at chance → a real brain-based decoder of imagined vs executed.
- Shuffled ≫ by-block, and the rest control ≈ task → separability is mostly recording-block identity (a split artifact).

## Prior work
- Imagined vs executed as a classification task: not covered in the vault. Imagery is "weak and highly variable" [[lawhern2018eegnet]] (§2.1.4). 4-class *imagery* decoding cross-subject on this dataset: CBraMod 0.642, EEGNet 0.581 [[wang2024cbramod]] (Table 3).

## Results
- **Part 1 (ERD):** execution gives the stronger drop (~30% vs ~20% at C3). Imagery is lateralized, while execution is bilateral. Table and figure → [[bci-paradigms]] *Imagined vs executed movement*.
- **Part 2 (classification):**
  ![[eegmmi-imagined-vs-executed-csp.png]]

  | band | shuffled 5-fold | by-block (leave one run pair out) | rest control (by-block) | cross-subject (LOSO) |
  |---|---|---|---|---|
  | 8–30 Hz (mu/beta) | 0.83 ± 0.03 | 0.64 ± 0.06 | 0.65 ± 0.06 | 0.56 ± 0.02 |
  | 30–75 Hz (muscle) | 0.88 ± 0.03 | 0.66 ± 0.05 | 0.57 ± 0.06 | 0.50 ± 0.02 |

  - **Shuffled CV is inflated.** Imagined and executed trials come from different runs, so shuffling lets the model learn "which recording". Accuracy drops from 0.83 to 0.64 when whole run pairs are held out. Per-subject by-block scores range from 0.39 to 0.86.
  - **The rest control scores as high as the task (0.65).** The same pipeline separates the *rest* periods of executed vs imagined runs, when nobody is doing anything. So most of the within-subject separability is recording-block differences, not the task. 🤖 Caveat: rest epochs start right after a trial, so a post-movement beta rebound after real clenching could make part of this genuine.
  - **The muscle band beats mu/beta under shuffling** (0.88): high-frequency, non-brain signal is the easiest cue.
  - **Cross-subject it is at chance** (0.56 / 0.50).
  - **The CSP patterns point at the wrong place:** subject 1's top components sit at the frontal/temporal edge (around AF7/AF8/F8), which is typical of eye and muscle artifacts, not over C3/C4.
- 🤖 **Conclusion:** with CSP + LDA on this dataset there is no evidence of a usable, brain-based imagined-vs-executed decoder. The apparent 83% is a split artifact. Used as a worked example in [[evaluation-protocols]], [[q6-reliability-of-eeg-diagnoses]] and [[q7-foundation-models-vs-baselines]].
- **Follow-up:** the same data with a frozen pretrained encoder → [[eegmmi-frozen-probe]].

## Log
- 2026-10-10 ERD plot and CSP + LDA classification run (10 subjects).
- 2026-10-12 moved from [[bci-paradigms]] into this experiment note.
