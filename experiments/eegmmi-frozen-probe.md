---
slug: eegmmi-frozen-probe
status: planned
questions: [q7]
concepts: [self-supervised-pretraining, common-spatial-patterns, linear-discriminant-analysis, evaluation-protocols, riemannian-methods]
datasets: [eegmmi]
scripts: []
figures: []
cost: medium          # FM inference on GPU/CPU + downloading all 109 subjects (PhysioNet ~1 file/min)
origin: 2026-10-10, classical baselines vs FMs ([[q7-foundation-models-vs-baselines]])
updated: 2026-10-12
---

# eegmmi-frozen-probe

## Hypothesis
At small k (few labelled trials from a new subject), a linear probe on frozen foundation-model embeddings does *not* beat CSP + LDA or EEGNet trained on the same trials. Published few-shot results point that way: CSP+LDA 60.6 vs CBraMod 50.3 on 4-class MI with ~21 trials per class [[liu2026eeg]] (Supp. Table 16).

## Design
- **Data:** PhysioNet EEG Motor Movement/Imagery (EEGMMI): 109 subjects, 64 channels, open; 10 subjects already downloaded.
- **Task:** **left vs right fist within imagery.** Both classes are interleaved in the same run, so there is no block confound. Not imagined vs executed: there class = run, and a frozen encoder that captures recording fingerprints would "solve" it by block identity ([[eegmmi-imagined-vs-executed]]). Secondary: 4-class imagery, comparable to [[wang2024cbramod]] (Table 3).
- **Model:** frozen CBraMod + ridge / logistic regression on its embeddings. **Avoid LaBraM:** its pretraining corpus *includes* EEGMMI [[jiang2024large]] (App. D, p. 17). CBraMod pretrains on TUEG only (§3, p. 6) and tests on subjects 90–109 [[wang2024cbramod]] (Table 3, p. 8). Use subjects the model never saw.
- **Baselines, same k trials:** CSP + LDA, Riemannian tangent space + logistic regression (missing from every FM benchmark so far → [[riemannian-methods]]), EEGNet trained per subject.
- **Protocol:** calibration curves, k trials per class from a held-out subject (k = 5, 10, 20, 45), plus zero-calibration cross-subject. Report probe *and* fine-tune: linear probes can badly undersell FMs (LaBraM TUEV 0.346 probe vs 0.641 fine-tuned; [[jiang2024large]] Table 10).
- **Metric:** balanced accuracy, mean ± SEM over held-out subjects; chance 0.50.

## What each outcome would mean
- Probe ≥ CSP/Riemannian at small k → FM embeddings carry usable motor-imagery features without fine-tuning; evidence against "pretraining is only an initialization".
- Probe < classical, fine-tune ≥ classical → [[self-supervised-pretraining]]'s current reading (good initialization, weak frozen features) holds on this task too.
- Everything at chance cross-subject → the task is too weak at 10–20 trials for any method; move to 4-class or BCI IV-2a.

## Prior work
- [[liu2026eeg]]: few-shot within-subject, classical pipelines win MI/SSVEP; no Riemannian baseline.
- [[wang2024cbramod]]: pretraining adds +2 points on PhysioNet-MI (0.642 vs 0.620 without pretraining; Table 4), with full fine-tuning.
- [[tao2026separating]] (frozen-FM calibration on MI, in screening): check before running.

## Results
—

## Log
- 2026-10-10 planned in [[self-supervised-pretraining]].
- 2026-10-12 moved into this experiment note; Riemannian baseline added.
