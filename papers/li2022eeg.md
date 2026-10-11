---
citekey: li2022eeg
title: "EEG Based Emotion Recognition: A Tutorial and Review"
authors: [Xiang Li, Yazhou Zhang, Prayag Tiwari, Dawei Song, Bin Hu, Meihong Yang, Zhigang Zhao, Neeraj Kumar, Pekka Marttinen]
year: 2022
venue: "ACM Computing Surveys"
doi: "10.1145/3524499"
arxiv: "2203.11279"
pmid: ""
field: eeg
paper_type: review
task: "emotion recognition (valence/arousal or discrete emotions from EEG)"
datasets: [DEAP, MAHNOB-HCI, SEED, DREAMER, SEED-IV, MPED]
n_subjects: "15–32 per benchmark dataset (Table 3)"
n_channels: "14–62 across datasets (Table 3)"
model_type: ""
eval_protocol: ""
main_metric: ""
main_result: "Narrative review of ~50 emotion-recognition works 2016–2022 (Table 4). Within-subject accuracies cluster at 0.85–0.98, cross-subject at 0.65–0.90 on the same datasets. Random segment-level k-fold is called a 'wrong' split because of leakage (§5.3, p. 25)"
code_available: ""
read_depth: full
concepts: [emotion-recognition, domain-adaptation, evaluation-protocols, frequency-bands, time-frequency-analysis, riemannian-methods, consumer-grade-eeg-devices]
---

# EEG Based Emotion Recognition: A Tutorial and Review (Li, Zhang et al., 2022)

## TL;DR
A tutorial-style narrative review for newcomers to EEG emotion recognition. It covers how emotion is labelled, its neural correlates, hand-crafted features, DL architectures, domain adaptation for new subjects, benchmark datasets, and the split strategies. Its most useful parts are the dataset table (Table 3), the split taxonomy that flags segment-level leakage (§5.3), and a 50-row results table that mixes protocols (Table 4).

*arXiv preprint version (v1, Mar 2022); page markers (p. N) follow the ACM page numbers.*

## Research question
Give newcomers a holistic view of the technical routes in EEG emotion recognition (psychological basis → features → models → evaluation), focusing on DL methods that earlier surveys (mostly covering work up to 2017–2019) missed (§1, p. 2). No systematic search protocol is described.

## Data & preprocessing
- **How emotion is quantified** (§2.1, p. 3):
  - *Discrete:* Ekman's 6 or Plutchik's 8 basic emotions → classification.
  - *Continuous:* Russell's valence (unpleasant→pleasant) × arousal (calm→excited), optionally dominance. Rated per trial on the 1–9 Self-Assessment Manikin (SAM) scale (Fig. 1). Used as regression targets, or binarized/thresholded into classes.
- **How emotion is induced** (§2.3, p. 5): emotional faces, IAPS pictures, film/music clips, IADS sounds, VR scenes, or asking subjects to recall experiences. A self-report follows each trial.
- **Sampling:** usually 256/512/1024 Hz. 128 Hz is "adequate" because the bands used stop at ~45 Hz (§3, p. 5).
- **Artifacts** (§3.1, p. 5): EOG <4 Hz, ECG ~1.2 Hz, EMG >30 Hz, power line 50–60 Hz. Removed with ICA, wavelets, band-pass filters, then ASR (sliding-window PCA) and common average reference.
- **Benchmark datasets** (Table 3, p. 23; §5.1, pp. 23–24):

| dataset | year | subjects | device / channels | stimuli | labels |
|---|---|---|---|---|---|
| DEAP | 2011 | 32 | Biosemi ActiveTwo, 32 | 40 one-minute music videos | continuous valence/arousal/dominance/liking (self-report) |
| MAHNOB-HCI | 2012 | 27 | Biosemi, 32 | 20 clips | 9 discrete + continuous |
| SEED | 2017 | 15 | ESI NeuroScan, 62 | 15 Chinese film clips (~4 min), 3 sessions | positive / neutral / negative |
| DREAMER | 2018 | 25 (text says 23, p. 24) | Emotiv EPOC (consumer), 14 | 18 clips | continuous V/A/D |
| SEED-IV | 2019 | 15 | ESI NeuroScan, 62 | 72 clips, 3 sessions | happy / sad / fear / neutral |
| MPED | 2019 | 23 | ESI NeuroScan, 62 | 28 clips | 7 discrete |

## Method
- **Feature families** (§3.2–3.7, Table 2, p. 8):
  - time-domain statistics, Hjorth parameters, ERP amplitudes;
  - band power (PSD) over δ 1–4, θ 4–8, α 8–13, β 13–30, γ >30 Hz (§3.3);
  - wavelet energy/entropy (DWT levels map onto the bands, Table 1);
  - nonlinear measures (fractal dimension, entropies, recurrence plots);
  - **differential entropy (DE)**: for a Gaussian signal it equals ½·log(2πeσ²), so it is equivalent to log band power in a fixed band (§3.5, p. 7);
  - hemispheric asymmetry (left−right differences or ratios of symmetric electrode pairs) (§3.6);
  - connectivity / brain-network features (coherence, PLV, graph metrics) (§3.7).
- **Feature selection** (§3.8): filter methods (χ², mRMR, ANOVA), wrapper methods (RFE, L1). The authors warn, citing Haufe et al., that classifier weights should not be read as neuroscience findings (§3.8.2, p. 9).
- **"Technical routes"** (Fig. 7, p. 10, §4): thresholding a feature; classical ML on features; DL on hand-crafted feature maps (DBN, 2D-CNN on channel×band grids, CapsNet, graph CNNs with learned adjacency such as DGCNN, hemisphere-asymmetry RNNs such as BiHDM/BiDANN); end-to-end DL on raw EEG (EEGNet, 3D-CNN on electrode-grid × time, TSception, CNN-LSTM hybrids, Riemannian fusion network); domain adaptation; ensembles; fuzzy logic; data-constrained learning (augmentation, few-shot); AutoML.
- **Domain shift** (§4.5, pp. 18–21) → [[domain-adaptation]]. Four remedies: (1) per-subject calibration against a resting baseline, or Riemannian alignment of covariance matrices; (2) separate models per gender, culture or user cluster; (3) transfer learning (TCA/MIDA, fine-tuning, adversarial DANN, MMD, meta-learning, distillation); (4) selecting features that are stable across subjects.

## Evaluation
- **Metrics** (§5.2): precision, sensitivity, specificity, F-score for classification; MSE, MAE, R² for rating regression.
- **Split taxonomy** (§5.3, Fig. 32, p. 25): 7 k-fold strategies under two goals, subject-dependent (train and test on the same person) or subject-independent (test on unseen people).
  - Recommended: split by *trial* without segmenting (strategies 1, 4, 5).
  - Questionable: cutting each trial into segments that all inherit the trial label (2, 6, 7). Emotion drifts within a trial, so segment labels are noisy (Fig. 16, p. 14).
  - **Wrong:** random k-fold over segments (3, 7), because "the segments from the same trial may be assigned to the training and test sets simultaneously, introducing information leakage" (p. 25).
  - Why people segment anyway: a subject usually gives "no more than 100" trials because of fatigue, too few for DL (p. 25).

## Results (with locations)
- **Neural correlates are unsettled** (§2.2, p. 4):
  - Frontal alpha asymmetry (left more active for positive/"approach" emotions, right for negative/"withdrawal"). Other work finds no alpha effect but a beta-2 (18–22 Hz) effect instead.
  - Intracranial studies support a "distributionist" view: no single region is specific to one emotion.
  - "Localizing neural sources from scalp EEG is problematic."
  - The authors conclude the specificity is "not yet fully explored and understood" and recommend using all bands and regions.
- **Which bands work in ML:** beta and gamma give the best features (DBN, CNN on DE), but combining all bands is best (p. 4). Zheng & Lu find lateral temporal and prefrontal β/γ most discriminative (p. 4, p. 21).
- **Subject dependence:**
  - Kim & André: 95% within one user vs 70% when three users are pooled (4 classes).
  - Petrantonakis & Hadjileontiadis: 70–100% subject-dependent, reported to drop by 10–20% subject-independent (wording ambiguous).
  - AlZoubi et al. (27 students) concluded that user-independent models were "not feasible" (§4.5, p. 18).
- **Within-session drift:** EEG statistics drift even within a subject, from mental change or "drying electrode gel" (p. 18, Fig. 24).
- **Within vs cross-subject on the same model** (Table 4, pp. 26–27):
  - DGCNN on SEED: 90.4% vs 79.95%.
  - BiHDM on SEED: 93.12% vs 85.40%.
  - RGNN on SEED: 94.24% vs 85.30%.
  - BiDCNN on DEAP valence/arousal: 94.38/94.72% vs 68.14/63.94%.
- **Range of headline numbers** (Table 4):
  - Subject-dependent DEAP: up to ~98% (MLF-CapsNet 97.97% valence).
  - Cross-subject DEAP: mostly 65–85%. Cho & Hwang 3D-CNN reports 99.11/99.74% cross-subject.
  - Cross-subject 3-class SEED: 72–93%.
- **Future directions** (§6, pp. 28–29):
  - Find a minimal critical feature set: Li et al. found that "only one or two key features" match the full set (p. 28).
  - Report computational cost; build real-time and open-environment datasets.
  - Do cross-*dataset* domain adaptation, align raw EEG first (Riemannian alignment from motor imagery).
  - Go multimodal.
  - Build an "EEG-oriented pre-trained model on large-scale open-source EEG datasets, which are not limited to emotion recognition", like BERT/GPT (p. 29).

## Limitations (reported)
- Covers single-modality EEG only; multimodal fusion is left for later (p. 29).
- Comparisons in Table 4 are "from a descriptive perspective" (p. 28), not a re-evaluation.

## Assessment 🤖
- 🤖 **Table 4 is not comparable across rows.** It mixes 2-, 3- and 4-class tasks, valence vs arousal, and subject-dependent vs independent splits. It doesn't say which papers used segment-level k-fold, the split the authors themselves call wrong in §5.3. Near-perfect numbers (DEAP ~98% within-subject, Cho & Hwang 99.7% "cross-subject") are the kind §5.3 warns about. I'd treat them as suspect without checking each paper's split.
- 🤖 **The labels are weak.** DEAP/DREAMER use one self-rating per 1-minute trial, and SEED's labels are the *intended* emotion of the film clip (a design label), not what the person felt. Every 1 s window inherits that label. So "emotion recognition" on SEED partly means "which clip was playing". With 15 clips, clip identity (visual and auditory input, eye movements) may be decodable without any emotion.
- 🤖 **The β/γ finding may be partly muscle.** The bands most predictive of emotion (β, γ up to 45 Hz; p. 4) overlap the EMG range the review itself gives (>30 Hz, p. 5). Facial expressions and jaw tension during emotional clips would show up there, mostly at temporal and frontal electrodes, where the best channels are found (p. 4). The review doesn't discuss this confound.
- 🤖 **The physiology section reads as contradictory evidence:** alpha asymmetry vs beta-2, and locationist vs distributionist accounts. The paper's answer is to give a model all bands and channels. This fits the [[q6-reliability-of-eeg-diagnoses]] pattern: the target is subtle and subjective, the reported numbers are high, and there is no agreed-upon signal underneath.
- 🤖 The paper calls for an emotion-agnostic pretrained EEG model (p. 29), and the authors' grants are on exactly that (Acknowledgments). LaBraM ([[jiang2024large]]) and CBraMod ([[wang2024cbramod]]) arrived in 2024 and use SEED-family data for both pretraining and evaluation.

## Concepts
- [[emotion-recognition]]: the task this review is about (labels, datasets, features, accuracy ranges).
- [[domain-adaptation]]: the §4.5 taxonomy of fixes for cross-subject shift.
- [[evaluation-protocols]]: 7-strategy split taxonomy; segment-level k-fold leakage (§5.3).
- [[frequency-bands]]: band definitions and which bands carry emotion information (§2.2, §3.3).
- [[time-frequency-analysis]]: DWT level ↔ band mapping (Table 1), STFT vs wavelets (§3.4).
- [[riemannian-methods]]: covariance alignment for cross-subject transfer and the RFNet fusion model (§4.4, §4.5).
- [[consumer-grade-eeg-devices]]: DREAMER uses a 14-channel Emotiv EPOC (Table 3).

## Related papers
- [[song2022eeg]]: EEG Conformer evaluated on SEED with 5-fold CV over 1 s windows, which is §5.3's "wrong" strategy.
- [[jiang2024large]]: LaBraM, the kind of large pretrained EEG model this review proposes. It evaluates on SEED-V with a pooled-subject trial split.
- [[wang2024cbramod]]: a later foundation model. On FACED (123 subjects, held-out subjects, 9 classes) the best balanced accuracy is 0.55 (Table 2), far below the 0.9+ numbers collected in Table 4 here.
- [[chaddad2023electroencephalography]]: general review that also lists DEAP/SEED as standard emotion datasets.
- [[varbu2022past]]: emotion as a passive-BCI paradigm (15 of 202 BCI papers).
- [[lawhern2018eegnet]]: EEGNet, cited as an end-to-end baseline that EmotioNet beat (p. 15).

## Q&A notes
