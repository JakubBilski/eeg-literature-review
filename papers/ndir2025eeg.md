---
citekey: "ndir2025eeg"
title: "EEG-CLIP: learning EEG representations from natural language descriptions"
authors: [Tidiane Camaret Ndir, Robin T. Schirrmeister, Tonio Ball]
year: 2025
venue: "Frontiers in Robotics and AI"
doi: "10.3389/frobt.2025.1625731"
arxiv: "2503.16531"
pmid: "40933652"
field: eeg
paper_type: method
task: "abnormal EEG, age, gender and medication decoding from clinical EEG (TUAB) via EEG-report contrastive alignment"
datasets: [TUAB]
n_subjects:
n_channels: 21
model_type: "CLIP-style dual encoder: Deep4 CNN (EEG) + ClinicalBERT (report text), 64-d shared space, contrastive loss"
eval_protocol: "official TUAB train/eval split; frozen encoder + LogReg/MLP head; zero-shot text prompts; few-shot on a 60/20/20 re-split of TUAB train"
main_metric: "balanced accuracy"
main_result: "pathology 0.847 frozen+MLP vs 0.851 task-specific Deep4 (Table 3); zero-shot pathology 0.755 (Table 4)"
code_available: "https://github.com/tidiane-camaret/EEGClip"
read_depth: full
concepts: [language-supervised-pretraining, self-supervised-pretraining, evaluation-protocols]
---

# EEG-CLIP: learning EEG representations from natural language descriptions

*Read from arXiv v2 (29 Jul 2025); page numbers refer to that PDF, which may differ from the Frontiers version. Citekey from the script ("Ndir"); the surname is "Camaret Ndir".*

## TL;DR
CLIP for clinical EEG: a Deep4 CNN and a clinical BERT are trained contrastively to match TUAB recordings with their free-text neurologist reports. Frozen EEG features almost match a supervised Deep4 on pathology (0.847 vs 0.851) and allow zero-shot pathology at 0.755 from a text prompt, but few-shot gains over training from scratch are mixed.

## Research question
Can free-text clinical reports serve as supervision for general-purpose EEG representations that transfer across decoding tasks, including zero-shot via text prompts? (§1, p. 2)

## Data & preprocessing
- **TUAB** only: train 1,387 normal + 1,398 abnormal files, eval 150 normal + 130 abnormal (§3.1, p. 3). Each recording has age, gender and a report with 15 sections (§3.1).
- **Report sections:** Impression (2,971 non-empty, avg 16 words), Description of the record (2,964, 70 words), Clinical history (2,947, 26), Medications (2,893, 4), … heart rate (1,458, 2 words) (Table 1, p. 4).
- **Preprocessing (Schirrmeister et al. 2017 pathology recipe):** 21 common electrodes; drop the first minute and use only the next **2 minutes**; clip ±800 µV; resample to 100 Hz; divide by 30 (§3.2, p. 3).
- Windows of 1,200 samples (12 s), stride 519 (§3.3, p. 5).

## Method
- **EEG encoder:** Deep4 CNN (4 conv–max-pool blocks), flattened → FC to 128-d (§3.3, p. 3).
- **Text encoder:** pretrained BERT-type model; ClinicalBERT is best (§4.3.1, Fig. 6, p. 12). Text-encoder LR = 10⁻³ × EEG LR works best (Fig. 7, p. 13).
- **Projection:** 3-layer MLP heads → 64-d shared space; symmetric CLIP contrastive loss (§2.2, §3.3, Fig. 1, p. 4).
- Adam, LR 5×10⁻³, weight decay 5×10⁻⁴, 20 epochs, batch 64 (§3.3, p. 5).
- Text input = all report sections; random sub-string sampling was worse (§4.2, p. 9).

## Evaluation
- **4 binary tasks:** pathological; age ≤50 vs >50; gender; medication = report mentions Keppra, Dilantin or Depakote (§3.4, p. 5).
- **Classification:** frozen EEG-CLIP encoder + LogReg or 3-layer MLP vs (a) *task-specific* Deep4 trained end-to-end ("upper bound") and (b) *alternative-task* Deep4 trained on another label, frozen, new head ("lower bound") (§3.4.1, Fig. 2, p. 6).
- **Zero-shot:** nearest of two prompt embeddings, e.g. "This is a normal recording" vs "This is an abnormal recording" (Table 2, p. 6).
- **Few-shot:** TUAB train re-split 60% contrastive / 20% task-train / 20% eval; heads trained on 1/2 … 1/50 of the 20% (§3.4.3, Fig. 3, pp. 6–7).
- Metric: balanced accuracy. No seeds or error bars in Tables 3–5; Fig. 4 shows 80% CIs (p. 10).

## Results (with locations)
- **Frozen features (Table 3, p. 8)**, LogReg / MLP vs task-specific vs alternative-task:
  - pathological 0.826 / 0.847 vs 0.851 vs 0.741 (age);
  - age 0.713 / 0.747 vs 0.786 vs 0.685;
  - gender 0.687 / 0.702 vs 0.752 vs 0.667;
  - medication 0.633 / 0.615 vs 0.685 vs 0.573.
- **Zero-shot (Table 4, p. 8):** pathological 0.755, age 0.642, gender 0.567, medication 0.532.
- **Few-shot (Table 5, p. 9;** the label fraction for the table is not stated): EEG-CLIP+MLP vs task-specific vs alternative: pathological 0.710 vs **0.781** vs 0.531; age **0.712** vs 0.621 vs 0.631; gender 0.550 vs **0.648** vs 0.512; medication 0.551 vs 0.575 vs 0.598.
  - Fig. 4: EEG-CLIP degrades least as the fraction shrinks; it is ahead on pathology only at ~1/20–1/50, and on age at all fractions (pp. 8–10).
- **Comparison with ELM-MIL** ([[gijsen2024eeg]]): 87.11% vs 84.7% balanced accuracy on pathology (§4.1, p. 9), numbers quoted, not rerun.
- **Report sections (Fig. 5, p. 11):** all sections best overall; impression, description and history give the strongest single-section models. The 2-word heart-rate section gives the best gender model; technical-difficulties text helps pathology (§4.2, p. 9).
- **Embedding size:** 32–128 dims beat 256–512 on all tasks (Fig. 8, p. 14).
- **Gradients (frequency domain, averaged over the eval set):** "Excessive beta activity" → 14–30 Hz; "20 Hz beta spindles in central regions" → C3/Cz/C4 at ~20 Hz; "Left temporal sharp waves … 6 Hz" → T3/T5 at ~6 Hz; "This is a normal recording" → positive peak at 8–9 Hz (alpha) (§4.4, Figs. 10–13, pp. 15–19).

## Limitations (reported)
- TUAB only; dataset-specific biases and overfitting possible; needs multi-site validation (§5, p. 20).
- Reports vary in quality and structure (§5).
- Whole recording ↔ whole report pairing; fine-grained segment–sentence alignment (MIL) could help (§5).

## Assessment 🤖
- 🤖 **"Zero-shot" is not label-free here.** TUAB's normal/abnormal label is, to my knowledge, taken from the same report's impression (not sourced in the vault; TUAB paper in reading queue), and the medication label is *defined* by words in the report. The contrastive target contains the label text, so zero-shot pathology at 0.755 is closer to weakly-supervised learning with free-text labels than to transfer to an unseen concept. A fairer zero-shot test would query a concept that is absent from or masked out of the training reports.
- 🤖 **Few-shot claims are stronger in the text than in the table.** The intro says EEG-CLIP "consistently outperforms … task-specific models when labeled data are scarce" (p. 2), yet Table 5 has task-specific ahead on pathology (−7.1 points) and gender (−9.8), and the table's label fraction isn't given. Only age clearly favours EEG-CLIP.
- 🤖 **Small data and no uncertainty.** ~2,785 training recordings × 2 min ≈ 93 h of EEG; single runs in Tables 3–5 on a 280-recording eval set (binomial SE ≈ 2.1 points at 0.85). Differences like 0.847 vs 0.851 are ties.
- 🤖 **Selection on the eval set is likely.** Text encoder, LR ratio and embedding size (Figs. 6–8) are chosen by eval-set balanced accuracy; no separate validation split is described. Patient-disjointness of the 60/20/20 few-shot re-split is not stated (TUAB's official split is patient-disjoint; repeat sessions inside train are possible).
- 🤖 **Baselines are only Deep4 variants.** No classical feature model (e.g. the CatBoost ensemble at AUC 92.2 on TUH, [[poziomska2025quantity]]) and no EEG FM. The "upper bound" is not one: TUAB supervised models reach ~0.85–0.87 ([[poziomska2025quantity]], [[wang2024cbramod]]).
- 🤖 **Section ablations invite confounds.** "Heart rate → gender" is explained as cardiac physiology, but the section's presence or length may track recording setting or report template. Same for technical-difficulties → pathology (artifacts co-occur with sick patients). Numbers are only in a heatmap.
- 🤖 **What is genuinely interesting:** frozen features from report supervision ≈ supervised Deep4 on pathology, clearly above single-task transfer (0.847 vs 0.741). The gradient maps match textbook EEG vocabulary (beta, central 20 Hz, left temporal 6 Hz, posterior alpha in normals). Excess beta is a known benzodiazepine sign, so text supervision might pick up drug effects; untested.
- 🤖 **For Q9:** report text is a cheap, rich pretext target that clinical archives already have (TUH, HEEDB). Its main risk is the same circularity as TUAB labels: the text is a reading of the same EEG.

## Concepts
- [[language-supervised-pretraining]] — the paper's method: contrastive EEG–report alignment, zero-shot prompts.
- [[self-supervised-pretraining]] — contrast: supervision here is paired text, not the signal itself.
- [[evaluation-protocols]] — frozen-head, zero-shot and few-shot protocols on TUAB; eval-set selection.

## Related papers
- [[gijsen2024eeg]] — concurrent EEG-language model on TUH reports with MIL alignment; 87.1% vs 84.7% (quoted, §4.1). Not read.
- [[jiang2024large]], [[wang2024cbramod]] — masked-pretraining FMs evaluated on the same TUAB eval split; no direct comparison.
- [[poziomska2025quantity]] — TUAB ceiling ~85–87% and a strong classical baseline that EEG-CLIP doesn't run.
- [[kontras2026neuroatlas]] — NeuroLM, the text-aligned FM, is among the most consistent frozen-probe models there.
- [[kuruppu2026eeg]] — LP / FT / few-shot / zero-shot taxonomy; zero-shot is rare in EEG FMs.

## Q&A notes
