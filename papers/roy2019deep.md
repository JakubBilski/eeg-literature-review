---
citekey: roy2019deep
title: "Deep learning-based electroencephalography analysis: a systematic review"
authors: [Yannick Roy, Hubert Banville, Isabela Albuquerque, Alexandre Gramfort, Tiago H. Falk, Jocelyn Faubert]
year: 2019
venue: "Journal of Neural Engineering 16(5):051001"
doi: "10.1088/1741-2552/ab260c"
arxiv: "1901.05498"
pmid: "31151119"
field: eeg
paper_type: review
task: "deep learning for EEG across domains (epilepsy, sleep, BCI, affective/cognitive monitoring)"
datasets: [BCI Competition, EEGMMI, DEAP, SEED, CHB-MIT, Bonn, TUH, MASS, Sleep-EDF]
n_subjects: "1–16,000 per study (median 13, mean 223; p. 31)"
n_channels: "1–256 (half of studies 8–62; p. 13)"
model_type: ""
eval_protocol: ""
main_metric: "accuracy difference, best DL vs best traditional baseline"
main_result: "Median +5.4% accuracy for DL over traditional baselines (IQR 9.4%, 102 studies/tasks; Fig. 14, p. 24). Only 7% of 156 studies easily reproducible (p. 25)"
code_available: "http://dl-eeg.com"
read_depth: full
concepts: [evaluation-protocols, riemannian-methods, eeg-preprocessing-pipeline, independent-component-analysis, self-supervised-pretraining, domain-adaptation, sleep-staging, seizure-detection, emotion-recognition, consumer-grade-eeg-devices, channel-heterogeneity, signal-quality-and-noise]
---

# Deep learning-based EEG analysis: a systematic review (Roy, Banville et al., 2019)

## TL;DR
A systematic review of 156 DL-on-EEG papers (Jan 2010–Jul 2018) that coded ~70 items per paper: data, preprocessing, architecture, training, results, reproducibility. CNNs on raw EEG took over from 2015. DL beat traditional baselines by a median 5.4% accuracy, but the baselines were weak, few studies split by subject, and only 7% of studies could be reproduced.

*arXiv v2 (Jan 2019); page markers (p. N) follow the arXiv PDF. Pre-2022: included under the backward exception (>1,500 citations, cited by [[varbu2022past]], [[gans2024sleep]], [[chaddad2023electroencephalography]]).*

## Research question
Does DL beat traditional EEG pipelines, how much data does it need, which design choices are used, and how reproducible is the work? (§1.5, §3.7, p. 4, p. 21)

## Data & preprocessing (of the review)
- **Search:** PubMed, Google Scholar, arXiv, last queried 2 Jul 2018; 18 terms (EEG × DL architectures); preprints included, peer-reviewed version preferred (§2, p. 6).
- **Inclusion:** trains a DL model on non-invasive EEG. Excluded: invasive EEG/MEG only, software-only papers, reviews (Table 2, p. 6).
- **Flow:** 553 database hits + 49 from references → 156 included (§3, p. 7). 49 journal, 58 conference, 48 preprints (§3.1, p. 8).
- **Extraction:** ~70 items in 6 categories, one reviewer per paper plus a second "if needed" (§2, p. 6; Table 3, p. 7). The table is public at dl-eeg.com.

## Method
Descriptive statistics per data item, plus a meta-comparison: for 102 studies/tasks reporting accuracy against a traditional baseline, the best DL model minus the best baseline (§3.7.6, pp. 23–24). No formal meta-analysis or risk-of-bias assessment.

## Results (with locations)
- **Domains** (§3.2, Fig. 4, pp. 8–9): 86% classification. Clinical 49 papers (epilepsy 26, sleep 16), BCI 46 (motor imagery 21), monitoring 34 (emotion 17, workload 7). 9% improve tools (artifacts, interpretability), 5% generate data.
- **Growth:** the first 7 months of 2018 had more papers than 2010–2016 combined (p. 9).
- **Data quantity** (§3.3.1, p. 11): 2 to 4.8M minutes of EEG per study (median 360). 62 to 9.75M examples (median 14,000), with the count driven by window overlap: 4.05M examples from 1,080 min with 250 ms windows at 234 ms overlap.
- **Subjects** (§3.3.2, pp. 11–12): half the datasets have <13 subjects; the largest have 10,000 and 16,000. One study found diminishing returns above ~15 training subjects under leave-one-subject-out (ref [191], p. 12).
- **Hardware** (§3.3.3, p. 13): 1–256 channels, half 8–62. ~50% sampled at ≤250 Hz. Most-used devices: BioSemi ActiveTwo (research) and Emotiv EPOC (low-cost, <$1,000).
- **Channel count matters:** seizure detection 4 → 22 channels raised specificity 40% → 90% (ref [153]). In sleep staging, going from 2 to 6 channels gave most of the gain (ref [26]) (p. 13).
- **Augmentation** (§3.3.4, pp. 14–15): 3 papers studied it directly, 30 more used it. Gaussian noise on SEED lifted LeNet 49.6% → 74.3%, but an SVM already reached 74.2% (p. 14). Overlapping windows are the most common augmentation.
- **EEG processing** (§3.4, Fig. 9, pp. 15–16):
  - 72% preprocessed the data.
  - Artifacts: 46% did nothing, 24% handled them, 31% didn't say.
  - Input: 49% raw EEG, 48% hand-crafted features (36% frequency-domain).
- **Architectures** (§3.5.1, Fig. 10, pp. 17–18):
  - CNN 40.4%, RNN 13.5%, AE 12.8%, DBN 7.1%, CNN+RNN 7.1%, FC 5.8%, RBM 2.6%, GAN 1.9%.
  - DBNs and FC nets dominated until 2014; CNNs since 2015. CNNs mostly take raw EEG, DBNs frequency features.
  - Shallow: 128 of 156 use ≤10 layers.
- **Training** (§3.5.2, pp. 18–20):
  - 25% used multi-step pre-training, mostly unsupervised RBM/DBN/AE feature learning, then a classifier.
  - Not reported: training procedure 26%, optimizer 47%, hyperparameter search ~80%.
  - Adam use rose from 31.9% (2017) to 52.6% (2018).
- **Inspection:** 27% inspected their models, mostly first-layer weights and activations (§3.6, Table 5, pp. 20–21).
- **Evaluation practice** (§3.7, pp. 21–23):
  - Baselines: 67.9% had a traditional baseline, 34.0% a DL baseline, 21.1% none.
  - Validation: **60% used no cross-validation.**
  - Subjects: 25% intra-subject, 61% inter-subject, 8.3% both. Only **22 of 108** inter-subject studies held out subjects.
  - One example: 38% accuracy on unseen subjects vs 75% on seen ones (ref [34], p. 23).
  - 19.9% used statistical tests.
- **DL vs baseline** (Fig. 14, p. 24): median +5.4%, IQR 9.4%, only 4 negative, best +76.7% (RSVP).
- **Reproducibility** (§3.8, Fig. 15, pp. 24–25):
  - Data: 54% public, 42% private.
  - Code: 19% shared.
  - Only 11 of 156 (7%) were easy to reproduce; 61 had neither data nor code.
  - 21% asked for more public data. In clinical work, "the lack of labeled data, rather than the quantity of data" was named as the obstacle (p. 24).
- **Most-used datasets** (Table 6, p. 26):
  - BCI Competition (13), EEGMMI (8), DEAP (9), SEED (3);
  - CHB-MIT (9), Bonn (7), TUH (5);
  - MASS (4), Sleep-EDF (4).
- **Recommendations** (Table 7, p. 30; checklist App. B, p. 45):
  - describe the architecture and the data;
  - use public datasets;
  - include state-of-the-art baselines;
  - share recordings, code and weights.

## Limitations (reported)
- Preprints are not peer reviewed (§4.8, p. 30).
- Many coded items (initialization, normalization, losses) were left out of the analysis (p. 30).
- The review dates quickly; it is meant as a living table online (p. 30).
- The accuracy gains are probably biased upward: publication bias, weak baselines, and only 2 studies used Riemannian baselines (§4.5, p. 28).

## Assessment 🤖
- 🤖 The +5.4% is a median of *self-reported* gains over *self-chosen* baselines on mostly non-subject-held-out splits. It says little about whether DL beats strong classical methods; the authors say so themselves (p. 28).
- 🤖 There is an internal inconsistency: "only four values were negative" (p. 24) vs "only six reported lower performance" (p. 26). The denominators probably differ (102 tasks vs 156 papers).
- 🤖 The conclusion that artifact removal "is in general not required" (p. 27) rests on counting which papers skipped it, not on controlled comparisons. A network can also *use* artifacts (EMG, eye movements) as features, which would inflate scores.
- 🤖 The data findings anticipate later work: the label scarcity is a clinical issue, examples are inflated by window overlap, and there are few subjects. The 2010–2014 wave of unsupervised pretraining (RBM/DBN/AE) is a precursor to today's [[self-supervised-pretraining]].
- 🤖 Refs [150] and [177] are the same paper (Schirrmeister 2017, deep ConvNets), listed twice.

## Concepts
- [[evaluation-protocols]]: 60% without CV; 22/108 inter-subject studies hold out subjects; seen vs unseen subjects 75% vs 38%.
- [[riemannian-methods]]: called state of the art, but used as a baseline by only 2 of 156 papers (p. 28).
- [[eeg-preprocessing-pipeline]]: survey of how much DL papers preprocess (72%) and handle artifacts (24%).
- [[independent-component-analysis]]: the most cited automated artifact method; artifact removal usually needs an expert (p. 16).
- [[self-supervised-pretraining]]: 2010–2014 unsupervised layer-wise pretraining (RBM/DBN/AE) as an early form.
- [[domain-adaptation]]: inter- vs intra-subject; pool subjects, then fine-tune per subject (ref [127], p. 27).
- [[sleep-staging]], [[seizure-detection]], [[emotion-recognition]]: domain counts, datasets, imbalance handling.
- [[consumer-grade-eeg-devices]]: low-cost (<$1,000) devices in the papers; Emotiv EPOC the most used (p. 13).
- [[channel-heterogeneity]]: channel count and reference placement change results; this hinders cross-site comparison (p. 13).
- [[signal-quality-and-noise]]: low SNR, non-stationarity and inter-subject variability are the three core challenges of EEG; scalp potentials are "tens of µV" (§1.2, p. 2).

## Related papers
- [[varbu2022past]]: a BCI review of the same period; reuses Roy's data-item scheme and channel findings.
- [[chaddad2023electroencephalography]]: a narrative pipeline review; Roy is the systematic DL counterpart it lacks.
- [[lawhern2018eegnet]]: compact CNN of the same era, EEG-specific temporal/spatial convolutions (Roy p. 18 describes this design pattern).
- [[li2022eeg]]: emotion follow-up; same DEAP/SEED datasets and the same leakage concern, four years later.
- [[wong2023eeg]]: CHB-MIT and Bonn are already the top seizure datasets in 2018 (Table 6).
- [[gans2024sleep]]: cites Roy for the manual sleep-scoring workload.
- [[jiang2024large]], [[wang2024cbramod]]: the pretraining-on-TUH direction that Roy anticipated (p. 27: large datasets like TUH might make deeper models usable).

## Q&A notes
