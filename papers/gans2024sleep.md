---
citekey: gans2024sleep
title: "Sleep assessment using EEG-based wearables – A systematic review"
authors: [C.J. de Gans, P. Burger, E.S. van den Ende, J. Hermanides, P.W.B. Nanayakkara, R.J.B.J. Gemke, F. Rutters, D.J. Stenvers]
year: 2024
venue: "Sleep Medicine Reviews 76 (2024) 101951"
doi: "10.1016/j.smrv.2024.101951"
arxiv: ""
pmid: "38754209"
field: eeg
paper_type: review
task: "sleep staging with EEG wearables, validated against polysomnography"
datasets: []
n_subjects: ""
n_channels: "1–10 EEG electrodes across devices"
model_type: ""
eval_protocol: "per-device validation against simultaneous PSG (mostly manually scored)"
main_metric: "Cohen's kappa (recommended); accuracy, sensitivity/specificity, correlation also reported"
main_result: "34 devices, 24 with PSG validation (42 papers); per-stage accuracy 0.48–0.95, sensitivity 0.11–0.98, worst for N1 (§3); overall kappa 0.42–0.79 where reported (Table 1)"
code_available: ""
read_depth: full
concepts: [sleep-staging, consumer-grade-eeg-devices, electrode-types, evaluation-protocols, signal-quality-and-noise]
---

# Sleep assessment using EEG-based wearables: a systematic review (de Gans et al., 2024)

## TL;DR
Catalogues 34 EEG wearables for sleep (headbands, eye masks, ear-EEG, forehead patches, portable PSG) and what each was validated against. Most agree reasonably with lab polysomnography on the main stages but fail on stage N1. The evidence is mostly small, lab-based and at high risk of bias.

*The PDF has no text layer. The full text was transcribed by hand from page renders into `fulltext/gans2024sleep.md`, and locations below are PDF pages. The supplement (S1–S4) was not retrieved.*

## Research question
Which EEG-based wearables exist for measuring human sleep, in which populations were they validated, and how well do they agree with polysomnography (PSG), the reference standard? (p. 2)

## Data & preprocessing
- **Reference standard, PSG:** EEG plus eye (EOG) and chin muscle (EMG) channels plus cardio-respiratory monitoring. It is burdensome, labour-intensive and expensive, so it isn't used routinely (pp. 1–2).
- **Alternative, wrist actigraphy:** cheap, but it can't stage sleep, and it scores lying still as sleep (p. 2).
- **Search:** MEDLINE, Embase and CINAHL, last updated 29 Nov 2023, with no date or language limit. Grey literature and snowballing were added. Registered in PROSPERO; follows PRISMA (§2, §2.1).
- **Screening with ML:** ASReview active learning (TF-IDF + naive Bayes; stop after 150 irrelevant records in a row), then a second pass with Sentence-BERT + logistic regression (§2.3.1). Two independent reviewers.
- **Inclusion:** human devices; development or validation of an EEG wearable against the reference standard; full text available. Reviews excluded (§2.2).
- If a study compared to both automatic and manual PSG scoring, only the manual comparison was kept (§2.3.2).
- **Bias:** QUADAS-2, for full-text papers only (§2.4).

## Method
- Narrative synthesis per device in Table 1 (pp. 4–9): electrodes, number of stages, auto vs manual scoring, population and setting, reference system, and whatever metrics each study reported.
- No meta-analysis, "due to the heterogeneity of the data" (§3).

## Evaluation
- Each primary study records the wearable and PSG at the same time and compares stage labels epoch by epoch (or total stage durations).
- Metrics vary between studies: accuracy, agreement %, Cohen's κ, sensitivity/specificity, Pearson/Spearman/intraclass correlation (§2.3.2, Table 1).

## Results (with locations)
- **Volume:** 109,115 citations → 231 full texts → 53 + 7 snowballed = 60 papers, published 1988–2023; 52% in or after 2020 (§3).
- **Devices:** 34 in total. 24 have validation papers (37 full texts + 5 abstracts), 6 have feasibility studies only, and 4 come from grey literature (§3). Of the 24, 21 have brand names (Table 1) and 3 are unnamed device types, mostly ear-EEG (S4; p. 10).
- **Setting:** of 42 validation papers, 64% were in a clinic or sleep lab, 12% at home and 24% unspecified (§3).
- **Stage resolution:** 17 devices (70%) separate N1/N2/N3; 7 only give "light" vs "deep" (§3).
- **Ranges:** per-stage accuracy 0.48–0.95; sensitivity 0.11–0.98, "with the lowest percentages obtained for the N1 stages" (§3).
- **Examples (Table 1):**
  - Dreem (5 dry electrodes): overall accuracy 0.84, κ 0.73; N1 κ 0.43 (p. 4).
  - LANMAO forehead patch (single-channel hydrogel): overall κ 0.79 (p. 7).
  - trEEGrid (7 EEG electrodes, at home): κ 0.70 (p. 8).
  - Xtrodes (soft array; healthy + Parkinson's): κ 0.67, N1 κ 0.22, N1 sensitivity 0.16 (pp. 8–9).
  - Sleep Profiler: κ 0.67; N1 sensitivity 0.21 while N1 *accuracy* is 0.90 (p. 5). In another study, N1 κ was 0.07 with auto-scoring and 0.13 with manual scoring (p. 5).
  - SOMNOwatch: κ 0.78 with one scoring program vs 0.37 with another, on the same device (p. 7).
  - cEEGrid ear-EEG: agreement 0.59, κ 0.42 (pp. 5–6).
  - Zeo: κ 0.56; REM κ as low as 0.28 in one study (pp. 4–5).
- **Without sleep validation:** Muse (made for meditation) reached 85–86% accuracy and κ 0.77–0.79 in a deep-learning study (ref [91]). Philips SmartSleep uses auditory stimulation to boost slow waves (§3.2, p. 9).
- **Feasibility:** generally well tolerated. Dreem had <20% artifacts in most tests; Sleep Profiler had 86% compliance but under-reports N3 and over-reports N1; Cerebra had an 83% success rate (p. 9).
- **Risk of bias (38 full texts):** 21 high in ≥1 domain, 9 unclear, 8 low. No study was excluded for bias (§3.3).
- **Metric:** the authors recommend Cohen's κ, because it "accounts for chance agreement", "especially in unbalanced datasets" (p. 10).
- **Human scorers vary too:** manual scoring of PSG depends on the technician's experience and training (ref [96], an inter-rater meta-analysis), and there is "no consensus yet on a standard for automated scoring" (p. 10).

## Limitations (reported)
- Few validation studies exist for consumer devices; some devices were probably missed; 5 non-English papers were excluded (p. 10).
- Small samples are common (p. 10).
- Many ear-EEG papers name no brand, so devices were clustered by description (p. 10).
- Prices are left out because they change too fast (p. 10).
- Most studies are in labs, often with a researcher present, which "may overestimate the feasibility" at home (p. 10).
- **Research agenda:** more real-world (home) validation; comparisons of hardware, preprocessing and staging algorithms as separate components (§7, p. 11).

## Assessment 🤖
- 🤖 The headline ("consistently high accuracy … competing with … PSG", abstract, §5) is stronger than Table 1 supports. Overall κ runs from 0.42 to 0.79, N1 is close to unusable on several devices, and most studies are lab-based with high or unclear risk of bias.
- 🤖 Per-stage "accuracy" is one-vs-rest on imbalanced classes, so it flatters rare stages. Sleep Profiler's N1 accuracy is 0.90 while its N1 sensitivity is 0.21 (p. 5). The authors' preference for κ is right; ML readers should also expect macro-F1 or balanced accuracy.
- 🤖 Correlations of total stage durations (Neuroon, QUISI, Embletta) don't measure epoch-level agreement at all, and some of them are near zero.
- 🤖 Sleep is the one EEG domain where devices *are* routinely validated against a simultaneous reference (PSG). Still, each device is tested in its own study, with its own population, reference system and scoring, so devices cannot be ranked against each other. The same confounding problem appears in [[q2-measuring-devices]].
- 🤖 The scoring algorithm matters as much as the hardware: SOMNOwatch went from κ 0.78 to 0.37 depending on the staging software (p. 7). Device validation is really validation of device + algorithm.
- 🤖 The lowest sensitivity quoted (0.11, §3) isn't in Table 1, so it presumably comes from the unnamed devices in S4 (not retrieved).
- 🤖 For scale: PSG-based deep models on ISRUC reach κ 0.70–0.74 ([[wang2024cbramod]] Table 7). That is the same band as the better wearables, though the data, labels and protocols differ, so this is not a like-for-like comparison.
- 🤖 Minor: the Zmachine Insight+ feasibility sentence is duplicated on p. 9.

## Concepts
- [[sleep-staging]]: the task. 5-stage AASM vs 4-stage (light/deep) outputs; N1 is the hardest stage; PSG is the reference (§3, Table 1).
- [[consumer-grade-eeg-devices]]: sleep headbands (Dreem, Zmax, Muse, Zeo) next to medical portable PSG systems; validation evidence per device (Table 1).
- [[electrode-types]]: dry (Dreem), hydrogel patches (LANMAO, Bittium, Onera), pre-gelled grids (trEEGrid), flex-printed ear strips (cEEGrid), in-ear (IDUN) (Table 1).
- [[evaluation-protocols]]: device validation against a simultaneous reference; κ vs accuracy on imbalanced classes (p. 10).
- [[signal-quality-and-noise]]: artifact rates and success rates as feasibility outcomes (p. 9).

## Related papers
- [[niso2022wireless]]: lists home sleep staging as a main clinical use of wireless EEG (§4.2.2). Gans gives the per-device sleep validation evidence that Niso lacks.
- [[sabio2024scoping]]: reported no Muse validation as of May 2022. Gans cites a 2023 sleep-staging result for Muse (κ 0.77–0.79, ref [91]).
- [[kaongoen2023future]]: ear-EEG review. Gans covers cEEGrid, IDUN and unnamed in-ear devices for sleep (Table 1, S4). *(not yet read)*
- [[wang2024cbramod]]: sleep staging on ISRUC (6-channel PSG EEG, 30 s epochs, AASM 5 classes) as a foundation-model benchmark (App. E.1).
- [[roy2019deep]]: sleep staging is one of the main DL-for-EEG applications, and manual scoring is slow (p. 2).
- [[wong2023eeg]]: the seizure counterpart. A dataset catalogue rather than a device validation; imbalance and expert labels as in sleep.

## Q&A notes
