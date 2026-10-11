<!-- source: pdf/zare2026negative.pdf | converter: pymupdf -->

<!-- page 1 -->

# A Negative-Control Protocol for Clinical EEG Foundation-Model Benchmarks: Dataset Identity and

# External-Cohort Stress Testing

## Marzieh Zare

## Universit´e Laval, School of Psychology, Quebec City, QC, Canada

Abstract Objective. Apparent clinical EEG foundation-model gains may reflect cohort, montage, or probe design. We test whether these gains survive an external-cohort stress test and targeted negative controls. Approach. We evaluated five pretrained encoders on five benchmark tasks and one Korean CAUEEG task, using model-compatible inputs and subject-disjoint probes where identifiers exist. CAUEEG uses recording-level folds and an annotated no- overlap sensitivity. Controls test stronger comparators, fully random initialization, label permutation, and scrambled-label adaptation. Fully-random and permutation controls are model- and task-targeted; adaptation controls are REVE-only. Main results. On CAUEEG normal/mild cognitive impairment (MCI)/dementia classification (N=1,187 recordings), descriptive best-probe macro-area under the receiver operating characteristic curve (macro-AUROC) was 0.527–0.677 for five encoders versus 0.734 for simple classical features (0.736 enhanced sensitivity). On the annotated no-overlap subset (n=172), classical logistic regression remained above REVE (0.717 vs. 0.565). Fully random REVE was above pretrained REVE in a separate repeated-split control (0.667 vs. 0.570). Dataset-membership AUROC was 1.000 for every encoder in full space and after in-fold PCA-50; shuffled-label means were 0.488–0.506 and balanced subsamples remained at 1.000. This demonstrates dataset membership, not causal site, geographic, or population effects. On CHB-MIT (n=23), REVE reached 0.793 versus enhanced GBM at 0.739, fully random REVE at

0.691, and raw-signal random features at 0.505. The paired REVE–enhanced-GBM difference was +5.38 pp with 95% CI [−0.36, 11.22] pp, which crosses zero. Per-epoch normalization also precluded an amplitude-aware comparator. Significance. No task satisfies all four attribution conditions, so these results do not support a general claim of disease-information transfer across clinical populations. We distill the controls into a reporting protocol for clinical EEG foundation-model

studies. Keywords: EEG, foundation models, transfer learning, clinical EEG, seizure detection, Alzheimer’s disease, brain–computer interface, linear probing

## 1 Introduction

Electroencephalography (EEG) provides non-invasive, temporally resolved measurements of brain activity in clinical settings. A long-standing technical barrier to using EEG

1

# arXiv:2607.24519v3  [cs.LG]  13 Aug 2026

<!-- page 2 -->

across studies is the difficulty of extracting features that transfer across participants and recording conditions [1]. This paper is about how claims of such transfer are evaluated, not about any particular clinical application: every task evaluated here is retrospective diagnostic classification on public or registration-gated cohorts, which is a precondition for downstream clinical use rather than a demonstration of it.

Foundation models are large neural networks pretrained on broad corpora, commonly with self-supervised objectives, to learn representations for downstream tasks. They have transformed natural language processing [2] and computer vision [3]. In 2024–2025, several groups released pretrained EEG foundation models evaluated across brain–computer interface (BCI) and clinical downstream tasks [4–7].

Systematic multi-dataset comparisons now exist, but their protocols and adaptation settings differ [8–10]. We address a narrower gap: combining frozen probing, an external- cohort stress test, patient-overlap checks, and representation-level negative controls. Published evaluations report strong held-out-subject results on some clinical-monitoring tasks [7,11], but acquisition, population, and clinical composition can all change outside the benchmark cohort. AdaBrain-Bench standardizes comparisons but does not test this combination [8]. Here, a targeted negative control is an analysis designed to test one specific alternative explanation for an apparent model advantage, such as comparator weakness, architecture alone, label-independent structure, or nonspecific adaptation. Each control narrows one interpretation but neither excludes all confounding nor establishes causality; their joint pattern therefore supports only bounded attribution.

## 1.1 Contributions

In our review of the benchmark designs in Section 2, we did not identify one combining an external-clinical-cohort stress test with the present negative-control suite. We therefore test whether within-task frozen-probe advantages survive both. We evaluate LaBraM [4], EEGMamba [5], CBraMod [6], REVE [7], and BIOT [11] under task-specific frozen-probe protocols. Our contributions are:

1. A targeted four-part control suite. Stronger handcrafted comparators test baseline adequacy; matched fully random initialization tests pretrained-weight de- pendence; label permutation tests label dependence; and scrambled-label adaptation probes sensitivity to source-label correctness, with unmatched comparisons explicitly bounded. Coverage follows surviving task-specific claims rather than an exhaustive task-by-model grid. 2. A symmetric external-cohort stress test. All five encoders and handcrafted families start from the same clean CAUEEG montage and use identical folds. Every encoder remains below the simple comparator, and the annotated no-overlap sensitivity preserves the classical-over-REVE ordering. 3. Dataset-identity controls. Dataset membership is perfectly linearly decodable from every encoder after in-fold PCA-50, survives balanced subsampling, and collapses under label permutation. REVE-only Western–Western and harmonized- input extensions show that the effect is neither unique to the Western–Korean pair nor explained solely by line-frequency or absolute-scale cues; causal sources remain inseparable. 4. Bounded attribution of positive task margins. On CHB-MIT, REVE shows pretrained-weight and label dependence, but its paired margin over enhanced GBM has an interval crossing zero. On ds004504, completed REVE and BIOT controls

2

<!-- page 3 -->

likewise leave positive AD-versus-FTD point margins unresolved. The suite therefore supports task- and pipeline-specific conclusions, not a general transfer claim.

Figure 1 summarises the study design: which representations are compared, under which splits, and which targeted controls interrogate apparent gains. The Methods section gives the full specification.

## 2 Related Work

## 2.1 EEG Foundation Models

BIOT introduced a unified tokenizer for cross-dataset biosignal learning and was evalu- ated on EEG, ECG, and smartphone inertial-activity signals [11]. LaBraM introduced vector-quantized spectral tokenization with masked prediction and reported results on abnormal and event classification, emotion recognition, and gait prediction [4]. CBraMod proposed criss-cross attention to model spatial and temporal dependencies separately [6]; both LaBraM and CBraMod are evaluated in AdaBrain-Bench [8]. EEGMamba used a bidirectional Mamba encoder with masked EEG reconstruction and reported results across six downstream tasks [5]; its backbone builds on selective state-space models [12]. REVE introduced 4D positional encoding designed to accommodate arbitrary electrode configurations and was pretrained on more than 60,000 hours from 92 datasets and approximately 25,000 subjects [7].

## 2.2 Evaluation Protocols

Benchmark results vary across subjects, recording conditions, and datasets, and within- dataset evaluation does not by itself establish robustness to distribution shift, particularly when pretraining and evaluation share a source distribution [9,10]. Leave-one-subject-out (LOSO) cross-validation keeps each test subject unseen during training and therefore

directly evaluates cross-subject transfer. We treat within-dataset evaluation as comple- mentary to, rather than a substitute for, external-cohort evaluation. AdaBrain-Bench established a standardized benchmark that includes clinical tasks (Temple University Hospital Abnormal EEG Corpus [TUAB] normal/abnormal, Siena seizure, and sleep staging) with cross-subject results for each [8]. Its scope differs from ours in five respects: it evaluates four models (BIOT, EEGPT, LaBraM, CBraMod), not REVE or EEGMamba; it uses full fine-tuning as the primary adaptation strategy; its clinical scope covers anomaly detection, seizure detection, and sleep staging rather than neurodegenerative diagnosis; it does not include an external non-Western clinical dementia cohort comparable to CAUEEG; and it compares pretrained models with counterparts trained from scratch rather than testing matched pretrained and randomly initialized frozen encoders, label permutation, scrambled-label adaptation, or raw-signal random features [8]. On clinical- monitoring tasks, AdaBrain-Bench found foundation models comparable to or worse than traditional models; on Sleep-EDF, its best foundation model reached 69.47% versus 69.55% for its best traditional model, directionally consistent with our 2-channel sleep result [8]. AdaBrain-Bench also reported that linear probing generally underperformed full fine-tuning, with EEGPT exceptions on BCI-IV-2A and HMC, and concluded that current models were not ready for direct generalization through frozen representations [8].

3

<!-- page 4 -->

Clinical EEG tasks plus one auxiliary control dataset, which carries no task

CHB-MIT ictal vs. interictal

18 ch · 23 subj

TUH TUAB normal vs. abnormal

21 ch · 253 subj

ds004504 AD vs. HC / FTD

19 ch · 65 / 59 subj

Sleep-EDF wake vs. sleep

2 ch · 14 subj

CAUEEG normal / MCI / dementia

19 ch · 1,187 rec. external cohort ds003490 identity control only

19 ch · 50 subj

Task-specific preprocessing paths 200 Hz and 4 s non-overlapping epochs; filtering, reference, rejection, and normalisation follow each dataset pipeline

exact operations and granularity: Section 3.3

Representations

Five frozen encoders

LaBraM EEGMamba CBraMod

REVE BIOT

weights locked, task-specific embedding aggregation

Simple plus targeted enhanced features

simple band power · Hjorth · spectral entropy

enhanced + coherence · entropy · DFA · wavelet

enhanced family excludes TUAB; nonlinear sensitivi- ties reported separately

Within-task split-aware probing task-specific logistic settings; leave-one-subject-out or subject-grouped 5-fold where identifiers exist;

CAUEEG recording-level with LDA/SVM-RBF and an annotated no-overlap sensitivity

Negative controls targeted, not exhaustive

Stronger comparators

simple →enhanced

Label permutation

real y ↔shuffled y

Matched full random initialization

pretrained vs. fully random

Scrambled adaptation

real vs. scrambled LoRA

Figure 1: Study design and control structure. Four benchmark datasets and Korean CAUEEG follow documented task-specific preprocessing that is not uniform across tasks (Section 3.3). Five frozen encoders and simple features cover every primary task. The

current enhanced family covers four benchmark tasks plus CAUEEG; TUAB is excluded because no protocol-matched current-family result can be reconstructed. Independently, TUAB’s primary REVE and non-REVE rows use different samples. Probes and logistic settings are task-specific; CAUEEG additionally reports LDA and SVM-RBF and uses recording-level folds plus an annotated no-overlap sensitivity because general patient identifiers are unavailable. Encoder coverage is incomplete: BIOT is unavailable on TUAB and Sleep-EDF. ds003490 has no clinical task and enters only the Western–Western dataset-identity probe. Four targeted controls challenge apparent advantages: stronger comparators across tasks, model-specific label permutation and matched fully random initialisation (with a CHB-MIT raw-signal random-feature reference), and REVE-only scrambled-label adaptation.

4

<!-- page 5 -->

Benchmarks and critical evaluations of EEG foundation models. Critical reviews find heterogeneous and limited evidence for off-the-shelf utility, with linear probes often weaker than fine-tuned models while scratch-trained specialists remain competitive [13,14]. Recent controlled benchmarks find only marginal advantages over supervised baselines such as EEGNet under causal, artifact-aware protocols [15], while properly tuned supervised models can match or beat EEG-FMs at a fraction of the parameters [16]. Large multi- dataset comparisons report foundation models performing largely on par with simpler models, especially under clinical distribution shift [9,10]. Other systematic benchmarks broaden task coverage and diagnostic analysis [17,18], while robustness and interpretability audits show failure-mode-dependent behavior [19]. Our study differs in three respects. (i) An external non-Western stress test. We evaluate pretrained encoders on Korean

CAUEEG using a matched clean-input pipeline and add a fixed-split sensitivity on the annotated no-overlap held-out subset because general patient identifiers are unavailable for the recording-level primary analysis. (ii) A targeted negative-control suite. We combine stronger classical comparators with label permutation and task-specific scrambled-label, fully-random-initialization, and raw-signal random-feature controls. These test probe behavior, sensitivity to source-label correctness, and pretrained-weight dependence without treating either unmatched adaptation comparison as a causal estimate. (iii) A dataset- identity probe. Dataset membership remains linearly decodable at ceiling after PCA-50 for

all five encoders on the Western–Korean pair and for REVE on the Western–Western pair. This is evidence for dataset identity, not a causal geographic, site, device, or population axis because those factors are confounded. Companion representation audit. A companion preprint shares CAUEEG and some frozen-representation caches but asks a distinct spectral–temporal decoding question; it is therefore complementary rather than an independent replication [20].

## 2.3 Linear Probing for Foundation Models

Linear probing, training only a linear classifier on frozen pretrained features, is a stan- dard evaluation protocol for foundation models in computer vision [3, 21]. It assesses frozen features without task-specific encoder updates. For EEG, AdaBrain-Bench in- cludes linear probing alongside full fine-tuning [8]. We use frozen linear probing as the primary evaluation framework; explicitly labelled nonlinear and adaptation sensitivities are secondary.

## 3 Methods

Clinical EEG from four benchmark datasets is preprocessed through the documented task-specific pipelines, then evaluated with the applicable subset of five frozen pretrained encoders. Embeddings are evaluated by LOSO or subject-grouped five-fold probing when patient identifiers exist; CAUEEG uses recording-level folds and a separate fixed-split sensitivity on its annotated no-overlap held-out subset. Computation was performed locally on a Mac M3 laptop (16 GB unified memory), using CPU or MPS; EEGMamba’s CUDA- only Mamba2 selective scan was reimplemented in pure PyTorch for this environment. The Supplementary Material follows the order in which its contents are first used below.

5

<!-- page 6 -->

## 3.1 Foundation Models

Five pretrained EEG foundation models with distinct architectures were evaluated on their applicable datasets within task-specific frozen-probe pipelines. Covered encoders use the same cohort, primary probe, and folds within each task except TUAB: REVE used a separate 3,000-epoch global subsample, whereas the classical, LaBraM, EEGMamba, and CBraMod rows used a 4,807-epoch subject-capped sample. TUAB model differences are therefore not treated as matched comparisons. BIOT is unavailable on TUAB because the retained input lacks the names required to construct its bipolar derivations, and on two-channel Sleep-EDF because the bipolar16 contract cannot be satisfied; all other model–task cells were evaluated. Task settings are specified in Section 3.5. Fully-random- initialization and label-permutation controls target REVE on selected tasks and BIOT on both ds004504 contrasts; the raw-feature control is CHB-MIT-specific, and scrambled-label adaptation remains REVE-only.

Table 1: Foundation models evaluated. Weights were obtained from publicly listed repositories; REVE required gated Hugging Face access. Parameter counts refer to the evaluated backbones as instantiated locally.

Model Architecture Params Pretrain Pretraining objective Ref.

LaBraM-Base BEiT-inspired Transformer 5.8M 2,500 h Masked token pred. [4] EEGMamba Bidir. Mamba2 3.3M 16,724 h Masked reconst. [5] CBraMod Criss-Cross Attn. 4.9M 9,000+ h Masked reconst. [6] REVE-Base 4D Pos Enc Transf. 69.4M >60,000 h Masked autoenc. [7] BIOT Bio Transformer 3.2M 6 EEG datasets† Contrastive + multitask [11]

†The evaluated BIOT checkpoint was pretrained on MGH, SHHS, CHB-MIT, IIIC Seizure, TUAB, and TUEV. CHB-MIT and TUAB are therefore in-domain for BIOT.

LaBraM [4] uses a vector-quantized spectral tokenizer with a masked-token transformer. We loaded checkpoint braindecode/labram-pretrained through Braindecode’s LaBraM

implementation (https://braindecode.org/stable/generated/braindecode.models. LaBraM.html, accessed 6 August 2026). The 129-entry spatial position tensor (128 channel positions plus one class-token position) is linearly interpolated to Nch + 1 entries, and the 16-entry temporal position tensor is linearly interpolated to five positions for 4-s, 200-Hz inputs (align corners=False). These are study-specific approximations, not validated EEG channel- or time-mapping procedures. EEGMamba [5] uses bidirectional Mamba2 state-space blocks [22]. We use the pretrained masked-reconstruction model of Wang et al. (Neural Networks 192:107816; Hugging Face weighting666/EEGMamba), not the end-to-end multi-task classifier of Gui et al. [23]. Its CUDA-only selective scan was reimplemented in pure PyTorch for CPU/MPS execution. The port uses channel-agnostic temporal and spectral projections with a convolutional positional encoding, so it accepts the 18-channel CHB-MIT montage and the 19-channel montage; numerical parity with the upstream CUDA kernel was not independently tested. CBraMod [6] uses criss-cross attention (separate spatial and temporal attention), pre- trained by masked reconstruction on more than 9,000 cleaned hours of the TUH EEG corpus. The evaluated public backbone instantiates 4.9M parameters in our local wrapper; Table 1 reports this locally counted value. REVE [7] uses 4D positional encoding (3D electrode coordinates plus temporal position) to accept varying electrode layouts without interpolation. REVE-Base (69.4M parameters,

6

<!-- page 7 -->

512-d hidden states, 22 layers) was loaded via gated Hugging Face access. Extraction is task-specific: CHB-MIT mean-pools the final hidden states to 512 dimensions; the primary ds004504 analyses use the historical flattened 19 × 4 × 512 = 38,912-dimensional output of the final whole-vector LayerNorm; and TUAB uses token-flattened embeddings. Consequently, dimensionality checks are interpreted only within the pipeline that produced them and are not transferred across tasks. BIOT [11] (3.2M parameters) is a biosignal transformer (linear attention, 256-d). We use its six-dataset EEG checkpoint, pretrained on MGH, SHHS, and the training sets of CHB-MIT, IIIC Seizure, TUAB, and TUEV. Its published 18-token order is 16 longitudinal bipolar derivations followed by C3–A2 and C4–A1. We construct and order the first 16 by named subtraction, or reorder already-bipolar CHB-MIT inputs. A1/A2 are unavailable in the evaluated source montages, so the last two derivations are omitted without zero- padding; inputs without channel names are rejected. Because pretraining includes CHB- MIT and TUAB, those evaluations are in-domain. TUAB is not reported because the named-channel input required to construct the bipolar derivations is unavailable. We treat ds004504 and CAUEEG as out-of-domain subject to the published inventory’s completeness.

## 3.2 Datasets

Table 2 summarizes the benchmark, external-cohort, and auxiliary datasets and their roles in the study.

7

<!-- page 8 -->

Table 2: Datasets. Benchmark datasets (top), the external CAUEEG stress-test cohort (middle), and one auxiliary dataset (bottom) that carries no clinical task and enters only

the dataset-identity probe.

Benchmark Datasets

Dataset Task Subj. Ch. Epochs

Access/

origin

CHB-MIT [24,25] Ictal detection 23 18 9,712 PhysioNet TUH TUAB [26,27] Normal vs. abnormal 253 21 4,807/3,000† TUH ds004504 (OpenNeuro) [28]

AD vs. HC; AD vs. FTD 65/59 19 13,170/11,267‡ OpenNeuro

Sleep-EDF [29] Wake vs. sleep 14 2 2,996∗ PhysioNet

External-Cohort Stress Test

CAUEEG [30] Normal/MCI/Dementia n/a¶ 19∥ 1,187¶ South Korea

Auxiliary Control Dataset (no clinical task)

ds003490 (OpenNeuro) [31]

Dataset-identity control only§

50 19 — United States

† From 8,130 available epochs, the classical, LaBraM, EEGMamba, and CBraMod rows use a 4,807-epoch subject-capped sample; REVE uses a separate 3,000-epoch global sample. ∗From 28,636 by a subject- balanced random cap of at most 214 epochs per retained subject. ‡ AD/HC and AD/FTD use five-fold CV on 13,170 and 11,267 epochs, respectively. ¶ CAUEEG reports 1,155 patients in the full release but exposes no patient identifier; the analysed unit and tabulated count are recordings. ∥CAUEEG exports 21 signals; all reported comparisons use the 19-channel 10–20 montage after excluding EKG and Photic (Section 4.3). § ds003490 supplies no diagnostic label, task, or metric anywhere in this paper; it appears

only as the second member of the Western–Western pair in the dataset-identity probe (Section 4.4).

ds003490 (auxiliary control dataset) [31]: This US resting-state and auditory-oddball cohort includes participants with Parkinson’s disease and controls; we use 50 subjects at 19 channels only for the REVE dataset-identity sensitivity (Section 4.4), not for a clinical task. It was selected because it is absent from REVE’s published pretraining inventory, whereas TDBRAIN is listed [7]. Each cohort retains its own 19-channel pipeline, so this Western–Western comparison tests whether dataset separability is unique to the Western–Korean pair, not a harmonised site or geographic effect; acquisition, preprocessing,

population, and diagnostic composition remain confounded. What “external cohort” means here. Here, external cohort denotes a separately

constituted dataset not used in the five multi-dataset benchmark designs reviewed here [8– 10,17,18]; it is not external validation of a fitted clinical model. Every primary clinical probe is trained and tested within one dataset. The dataset-identity probe crosses cohorts using dataset membership, not diagnosis, as its label. The Western-to-Korean LoRA analyses of Section 4.2.4 also cross cohorts, but both correct-versus-scrambled comparisons are unmatched descriptive sensitivities: the binary training schedules differ, and the three- way arms differ in retained seed provenance and downstream probe settings. CAUEEG is therefore a within-cohort stress test in a differently constituted population, not a clinical cross-cohort transfer evaluation. CHB-MIT [24,25]: Continuous scalp EEG from the full cohort of 23 unique pediatric epilepsy patients at Boston Children’s Hospital (all 24 released case directories; case chb21 was merged with chb01 because it is a later recording from the same patient, and chb12

8

<!-- page 9 -->

was retained). The released recordings are sampled at 256 Hz; our pipeline selects an 18-channel double-banana bipolar montage, resamples it to 200 Hz, and applies a 60 Hz notch. Task: cross-subject ictal detection. Positive epochs overlap an annotated seizure by ≥50%; negatives are interictal segments drawn from the same seizure-containing recordings, at a 1:3 ictal:interictal ratio (per subject). All seizure-containing recordings per subject are included. Sharing the recording session reduces session confounding; ±30 s guard-band and all-files sensitivities further test that concern (Section 4.1). CHB-MIT is absent from REVE’s published pretraining inventory (the listed PhysioNet sources were Siena and ICARE [7]) and is treated as out-of-domain subject to the completeness of that inventory. CHB-MIT methods notes. (i) No amplitude-based rejection: no amplitude-threshold rejection was applied because ictal epochs can be legitimately high-amplitude. The retained cohort contains 2,428 ictal and 7,284 interictal epochs, preserving the specified 1:3 ratio. (ii) Amplitude normalization: per-epoch z-scoring removes absolute amplitude from both encoder inputs and relative-band-power features. An amplitude-aware handcrafted comparator cannot be reconstructed from the stored normalized epochs and was not run; the comparison therefore does not establish superiority over such a baseline. (iii) Bipolar coordinates: double-banana derivations have no single-electrode coordinate. In the executed REVE pipeline, the 18 channels were assigned the first 18 entries of its standard 10–20 coordinate bank in index order rather than derivation midpoints. The assigned coordinate matches one constituent electrode for 6 of 18 derivations (the first electrode for 4) and neither electrode for 12. This task therefore does not test REVE under anatomically valid bipolar coordinates, and no alternate-coordinate sensitivity was run.

Label note: All CHB-MIT subjects are epilepsy patients (pediatric intractable- epilepsy cases recorded during pre-surgical evaluation with anticonvulsant withdrawal); the dataset contains no non-epileptic controls [24]. Positive epochs are ictal: they overlap an annotated seizure interval by ≥50%; negative epochs are interictal segments from the same seizure-containing recordings. The task is therefore cross-subject ictal detection (ictal vs. same-session interictal epochs, in held-out epilepsy patients), not detection of

a persistent epileptic-brain trait and not sample-precise onset localization from short windows, which is a harder, separately defined task. TUH Abnormal (TUAB) [26, 27]: Clinical hospital EEG from Temple University Hospital. Our retained evaluation cohort contains 253 subjects and 21 channels from the 10–20 system. Binary normal/abnormal labels are derived from clinical EEG reports and assessments [27]. This dataset shares clinical population and recording protocol with the TUEG corpus used for CBraMod, LaBraM, and EEGMamba pretraining [4–6]. Cross-referencing against the published pretraining dataset list [7], TUH is confirmed as the largest source in REVE’s pretraining corpus (14,987 subjects, 26,847 hours, 44% of all pretraining data). The REVE authors removed downstream evaluation data from pretraining, but distributional similarity remains. BIOT was also pretrained on TUAB [11]. TUAB is therefore in-domain or distributionally adjacent for all five models; results should not be compared directly with confirmed out-of-domain evaluations. OpenNeuro ds004504 [28]: Eyes-closed resting-state EEG recorded with 19 channels in the standard 10–20 montage. The dataset comprises 36 participants with Alzheimer’s disease, 23 with frontotemporal dementia (FTD), and 29 healthy controls. The binary AD-vs-HC task uses n=65 and 13,170 epochs; the AD-vs-FTD task uses n=59 and 11,267 epochs; and the three-way AD/FTD/HC control uses all n=88 participants. Recordings were ICA-preprocessed. Both binary tasks use five-fold stratified group cross-validation

9

<!-- page 10 -->

with zero subject overlap between folds. Because ds004504 is absent from the published REVE pretraining inventory (cross-referenced against all 56 OpenNeuro datasets in [7]), this evaluation does not involve direct dataset overlap; however, the present comparison does not establish that pretraining caused the observed separability. Sleep-EDF [29]: Whole-night polysomnographic recordings from 20 healthy subjects. The analysis uses a fixed 14-subject cohort from the processed input available when the primary task was constructed; every retained subject has at least six epochs of both wake and sleep. A subsequently available fifteenth eligible record was not added to this fixed comparison set. Two EEG channels (Fpz-Cz, Pz-Oz) are used. Original 30 s annotations (W, N1, N2, N3, REM) were binarized to Wake vs. Sleep, then re-epoched into 4 s windows

with majority-vote labeling. Four task-construction choices materially shape the result. (i) Only the first recording night per subject is used. (ii) Surrounding wake is cropped to 30 minutes on either side of the sleep period, so the task does not represent natural nocturnal prevalence. (iii) When wake exceeds sleep by more than 3:1, wake is subsampled to exactly 3:1 using seed 42. (iv) One advancing RandomState(42) samples at most ⌊3000/14⌋= 214 epochs from each subject, yielding 2,996 epochs; this cap is subject-balanced, not label-stratified. Normalisation is per channel across all accepted epochs of one subject. These choices define a cropped, class-capped, subject-capped two-channel task rather than deployment-prevalence sleep classification. CAUEEG (Chung-Ang University Hospital EEG) [30]: Clinical EEG database from Chung-Ang University Hospital, Seoul, South Korea, comprising 1,379 recordings from 1,155 patients. The three-way task retains 1,187 recordings: 459 Normal, 417 mild cognitive impairment (MCI), and 311 Dementia. The 192 excluded recordings carry primary categories outside that task (93 Parkinsonian syndrome, 72 transient global amnesia, 14 frontotemporal dementia, and 13 normal-pressure hydrocephalus). The public export includes 21 signals at 200 Hz; our clean comparison retains 19 standard 10–20 EEG channels and excludes EKG and Photic. CAUEEG exposes no patient identifier, so the main comparison is recording-level; a fixed-split sensitivity uses the public no-overlap annotation (Section 4.3). CAUEEG is absent from the enumerated pretraining inventories of all five encoders, subject to their completeness [4–7,11].

## 3.3 Preprocessing

Preprocessing was task-specific; no single full chain was applied to all five datasets. All primary pipelines used MNE-Python [32], 200 Hz signals, and 4.0 s non-overlapping epochs. CHB-MIT used 0.5–70 Hz filtering, a 60 Hz notch, common-average reference (CAR), no amplitude-threshold rejection, and per-epoch, per-channel z-scoring followed by clipping at ±8. TUAB was processed using the executed 0.5–70 Hz/CAR pipeline without a notch filter. It also used no amplitude-threshold rejection; z-scoring and clipping were performed per channel within each recording. The ds004504 path began from the released ICA-preprocessed derivatives, then used 0.5–70 Hz filtering, a 50 Hz notch, CAR, and 500 µV peak-to-peak rejection before per-recording z-scoring and clipping. CAUEEG used its native 200 Hz sampling, a 0.5 Hz high-pass and 60 Hz notch on the clean 19-channel montage, with no 70 Hz low-pass, CAR, amplitude rejection, z-scoring, or clipping.

Sleep-EDF used a separate pipeline: resampling to 200 Hz, 0.5–70 Hz bandpass filtering, no notch filter, no CAR, and no amplitude-threshold rejection, followed by per-channel z-scoring across all accepted epochs of one subject and clipping at ±8. Sleep-EDF retains the historical unnotched input because the primary analysis preceded the later 50 Hz-notch

10

<!-- page 11 -->

revision and subsequent comparator rows were matched to that version. No notch-filter sensitivity was performed for either task; their absolute estimates may therefore retain mains-frequency information.1

For CAUEEG, each recording was divided into all available non-overlapping 4-s epochs. Epoch-level encoder embeddings and handcrafted feature vectors were averaged within the recording before fold assignment, yielding one vector and one diagnosis label per recording. For the clinical matrix, every representation was standardized within each training fold; REVE alone was additionally reduced by in-fold PCA-50 because its recording vector is 38,912-dimensional. The other encoder and handcrafted vectors entered the probes without PCA.

## 3.4 Classical Baseline

To compare predictive performance with foundation-model representations, we use hand- crafted features: relative band power in δ (0.5–4 Hz), θ (4–8 Hz), α (8–13 Hz), β (13–30 Hz), and γ (30–45 Hz) computed by Welch’s method [33]; Hjorth parameters (activity, mobility, complexity) [34]; Shannon spectral entropy [35]; and two study-defined, channel-index- based summaries (an alpha-asymmetry proxy and mean theta power over the first four channels). The feature family has 9 × Nch + 2 features per epoch (173 features for a 19-channel montage). For Sleep-EDF, the task-specific baseline uses the 9 × Nch = 18 spectral, Hjorth, and entropy features without the two study-defined summaries. Exact formulas, channel rules, spectral settings, and enhanced-feature parameters are spec- ified in Supplementary Material, Section S1 (“Classical-feature and CAUEEG probe specifications”). We use L2-regularized logistic regression with balanced class weights.

To test whether more sophisticated handcrafted features could close the gap with foundation models, we also evaluate an enhanced classical baseline adding magnitude- squared coherence summaries over at most 20 channel pairs [33], sample entropy [36], an epoch-scale detrended fluctuation analysis (DFA) summary [37], and study-defined Haar-basis wavelet energy [38]. The full family has 15 × Nch + 6 features per epoch. The four-second DFA statistic is retained as a short-window summary and is not interpreted as evidence of long-range temporal scaling. For the matched Sleep-EDF comparison, the 16 advanced summaries are appended to its 18-feature task-specific baseline, yielding 34 features; a separate 20-versus-36-feature sensitivity evaluates the two study-defined summaries in both families. Each comparison uses the same logistic classifier as its task-specific simple baseline.

## 3.5 Evaluation Protocol

Frozen probing. Each pretrained encoder is frozen (no gradient updates). The pri- mary probe is L2-regularized logistic regression (class weight=balanced, solver=lbfgs, max iter=1000): C = 1.0 for CHB-MIT and Sleep-EDF and C = 0.1 for TUAB, the notch-filtered ds004504 tasks, and CAUEEG. These pipeline defaults were not selected by nested cross-validation, a limitation when comparing absolute estimates across tasks. The CHB-MIT result is insensitive to C over {0.1, 1.0, 10} (mean-fold AUROC 0.793). CAUEEG sensitivities use fold-local StandardScaler followed by LDA (solver=lsqr,

1These are the study’s downstream pipelines; they do not reproduce every encoder’s pretraining preprocessing. Here “raw-signal” denotes the preprocessed time-series supplied directly to the control rather than an encoder, not unprocessed ADC output.

11

<!-- page 12 -->

automatic shrinkage) or SVM-RBF (C=10, γ = scale, balanced class weights, probability estimates, seed 42); any REVE PCA is fitted within the same training fold. Best-of-family comparisons and nonlinear classical heads are descriptive rather than a unified linear-probe estimator. Balanced class weights are used by the logistic and CAUEEG SVM probes; the AD-versus-HC GradientBoosting sensitivity uses balanced sample weights, whereas the CHB-MIT GradientBoosting and MLP sensitivities are unweighted. CHB-MIT first samples same-session negatives to a fixed 1:3 ictal:interictal ratio; no additional under- or oversampling is applied during probing. Metrics. Balanced accuracy (BA) and AUROC are reported as mean ± standard deviation across folds. The analysis unit differs by task and is specified below. All five benchmark tasks are evaluated at the epoch level within subject-disjoint folds. CAUEEG diagnosis is evaluated per recording; dataset identity uses one unit per ds004504 subject and one per CAUEEG recording (88 and 1,187 units, respectively). For CHB-MIT and Sleep-EDF, every subject contributes both classes, so the reported estimand is epoch-level discrimination in held-out subjects; no single subject-level outcome was defined. Where aggregation is defined, subject- and epoch-level estimands are not interchangeable: across the two ds004504 contrasts, pooling epoch probabilities raises AUROC for both models, while the between-model ordering reverses only on AD versus HC (Sections 4.1 and 5.4).

The prediction unit follows the task construction and available metadata. The five benchmark tasks use short epochs as prediction units because the executed frozen- representation pipelines operate on short windows; folds are subject-disjoint, so no participant contributes epochs to both training and testing. For CHB-MIT and Sleep- EDF, each participant contributes both classes, so a single subject-level outcome is not defined. TUAB and ds004504 epochs inherit recording- or subject-level diagnoses; their primary estimates therefore quantify segment-level discrimination in held-out subjects rather than subject-level diagnostic performance. Subject-aggregated estimates are re- ported separately for the two ds004504 contrasts, where retained predictions support that estimand. CAUEEG is evaluated per recording because diagnoses are released at the recording level and general patient identifiers are unavailable; epoch representations are averaged within each recording before splitting.

Comparisons are interpreted within tasks, where representations share the outcome, analysis unit, and validation design, subject to the stated channel contracts and the TUAB sample mismatch. AUROCs are not compared across tasks because the outcomes, populations, analysis units, and validation schemes differ; epoch-, recording-, and subject- level values are distinct estimands and are not pooled into an overall model ranking. Cohort and epoch counts are in Table 2, and preprocessing is specified in Section 3.3. CHB-MIT. The primary analysis uses epoch-level patient LOSO. REVE tokens are mean-pooled to 512 dimensions, and every encoder representation is reduced by in-fold PCA-200 before probing. Interictal negatives come from the seizure-containing recordings at the fixed 1:3 ratio stated above. TUAB. The analysis uses epoch-level, subject-grouped five-fold validation and token- flattened REVE embeddings. REVE uses 3,000 epochs, whereas the classical, LaBraM, EEGMamba, and CBraMod rows use 4,807; model differences are therefore not estimated. ds004504. Both AD-versus-HC and AD-versus-FTD use epoch-level, subject-grouped five- fold validation and the historical 38,912-dimensional flat-LayerNorm REVE representation. The primary estimand is epoch-level discrimination; subject-aggregated estimates are reported separately where retained predictions permit it. Sleep-EDF. Wake-versus-sleep uses epoch-level subject LOSO and retains epoch vectors

12

<!-- page 13 -->

without an additional reduction. The first-night, two-channel construction and its wake, label-ratio, and per-subject caps are specified in the Sleep-EDF dataset description above. CAUEEG. The primary analysis uses recording-level stratified five-fold validation, with identical folds across representations. Epoch vectors are averaged within recording; REVE alone uses the fold-local dimensionality reduction specified in Section 3.3. The fixed-split patient-overlap sensitivity is reported separately.

Together, these protocols keep training and test subjects disjoint wherever identifiers exist, while retaining the analysis unit supported by each task’s labels and metadata. They do not create a common cross-task estimand, and the TUAB sample mismatch remains an explicit exception to within-task matching.

## 3.6 The Negative-Control Suite

A benchmark number can be high for reasons other than pretrained representation quality: a weak comparator, the architecture alone, probe capacity on high-dimensional features, or an adaptation procedure that gives similar target performance after source-label permutation. Each control below targets one of these explanations within its stated coverage; Section 4.2 reports the corresponding results.

Each control addresses a distinct alternative explanation and is interpreted only within its stated coverage. Controls are allocated sequentially to active positive model-specific claims; once a claim fails an earlier comparator, uncertainty, or provenance gate, later controls are not required to reject that claim. Comparator adequacy. Stronger handcrafted features test whether an apparent encoder advantage reflects a weak baseline. The current enhanced handcrafted family covers four of the five benchmark tasks and the CAUEEG stress test; TUAB is not included because a protocol-matched current-family result could not be reconstructed from the retained data. CAUEEG additionally includes an SVM-RBF nonlinear-probe sensitivity, whereas Gradient Boosting and MLP sensitivities were run only on CHB-MIT and AD versus HC (Section 4.2.1).

Pretrained-weight dependence. Matched fully random initialization tests whether pretrained weights outperform the same architecture under matched inputs, folds, and probes. REVE was tested on CHB-MIT, CAUEEG, and AD versus FTD; BIOT was tested on AD versus HC and AD versus FTD (Section 4.2.2). Label dependence. Label permutation tests whether probe performance depends on the observed label structure rather than representation dimensionality or probe capacity. Labels were shuffled within subject for CHB-MIT and the complete PCA-200–scaling– logistic pipeline was refitted inside each fixed LOSO fold. For ds004504, BIOT was tested in the primary epoch-level pipelines for AD versus HC and AD versus FTD by permuting one diagnosis per participant, broadcasting it to that participant’s epochs, and reusing the fixed folds. REVE uses direct 38,912-dimensional subject-mean controls for AD versus HC, binary AD versus FTD, and three-way AD/FTD/HC. No Control 3 result is reported for TUAB, Sleep-EDF, or CAUEEG (Section 4.2.3). Adaptation-label dependence. Scrambled-label adaptation tests whether adaptation

depends on correct source labels by repeating adaptation after source-label permuta- tion. This REVE-only control was evaluated on binary and three-way CAUEEG, but neither completed comparison is a one-change label-effect experiment: the binary training schedules differ, and the three-way comparison differs in retained seed provenance and downstream SVM settings (Section 4.2.4).

13

<!-- page 14 -->

Interpretation and analysis units. These controls follow the model-specific claims that survive earlier attribution gates. Comparator and fully-random-initialization con- trasts are descriptive unless a paired interval is stated; label permutation provides a finite-randomization result under its stated probe; and the adaptation aggregates are unpaired and are not equivalence tests. The ds004504 BIOT controls and REVE random- initialization comparison follow the primary epoch-level folds; the REVE label-permutation sensitivities aggregate its primary flat-LayerNorm vectors to one vector per participant. CAUEEG controls are recording-level. The CHB-MIT Gaussian raw-feature reference does not bound other raw-signal representations. Interpretive attribution framework. We apply four conditions in sequence to each positive model-specific margin: (i) the encoder exceeds the stronger tested handcrafted family under the task’s specified probe and folds; (ii) paired uncertainty supports a positive margin where the analysis unit permits; (iii) the published pretraining inventory shows no overlap with the evaluation cohort or a closely related source distribution; and (iv) the pretrained representation exceeds matched random initialization and its observed-

label probe exceeds the corresponding permutation null, with a matched scrambled-label comparison for adaptation claims. Failure at an earlier gate ends the positive attribution claim; later controls can still characterize the pipeline but cannot rescue that claim. The framework was formulated after the analyses and is not a prospective success criterion or an AUROC threshold. Section 5.5 summarizes the model-specific outcomes.

## 4 Results

This section is organised by control, not by dataset. Section 4.1 reports the benchmark estimates once, in a single table, because those estimates are the object the rest of the section interrogates rather than the finding itself. Section 4.2 then applies the four negative controls defined in Section 3.6, and Sections 4.3–4.5 report the external-cohort stress test and the two confound probes. Additional balanced-accuracy results are consolidated in Supplementary Material, Section S2 (“Additional balanced-accuracy results”). Parameter counts are reported in Table 1, AUROC estimates in Table 3, and analysis units, validation splits, and reporting rules in Section 3.5.

## 4.1 Benchmark Estimates

Table 3 consolidates the frozen-probe estimates that the subsequent controls interrogate.

14

<!-- page 15 -->

Table 3: Frozen-probe estimates for all six primary tasks and every evaluated representation. Entries are comparable within a task except on TUAB, where REVE and the other rows use different epoch samples; no overall ranking is computed.

AUROC (%), mean ± fold SD

Task (dataset) Classical LaBraM EEGMamba CBraMod BIOT REVE

Ictal vs. interictal (CHB-MIT) 70.0 ± 17.5 79.2 ± 10.6 76.1 ± 15.5 77.7 ± 15.1 87.5 ± 9.4∗ 79.3 ± 18.3 Normal vs. abnormal (TUAB) 74.7 ± 4.1 70.2 ± 4.8∗ 71.3 ± 6.7∗ 75.0 ± 7.0∗ — 84.5 ± 3.2∗

AD vs. HC (ds004504) 80.6 ± 6.9 75.3 ± 6.5† 80.3 ± 7.8 82.3 ± 7.0 83.6 ± 4.6 82.8 ± 6.3 AD vs. FTD (ds004504)¶ 67.1 ± 4.4 66.1 ± 6.9 61.1 ± 7.3 64.6 ± 4.7 68.7 ± 3.5 76.7 ± 11.1 Wake vs. sleep (Sleep-EDF) 68.6 ± 14.1 58.1 ± 11.9 68.1 ± 13.4 68.3 ± 13.8 — 62.3 ± 12.4 N/MCI/dementia (CAUEEG)‡ 73.4 ± 1.5 52.7 ± 1.1 53.7 ± 1.9 66.9 ± 1.9 67.7 ± 2.1 56.8 ± 1.6

∗Confirmed pretraining overlap with the evaluation cohort; not out-of-domain transfer. TUAB REVE uses a separate 3,000-epoch global sample; the classical, LaBraM, EEGMamba, and CBraMod cells use a 4,807-epoch subject-capped sample, so TUAB cells are not directly differenceable. †Non-deterministic on Apple MPS; centre of a [0.752, 0.772] spread, excluded from every ranking claim. ‡External cohort, recording-level folds, best of LogReg/LDA/SVM-RBF per family; Supplementary Material, Section S3.1 (“Complete clean-input probe matrix”) reports the full matrix. — not run because BIOT’s input contract cannot be met on that task. Classical is the simple handcrafted family; the enhanced family and nonlinear heads are in Section 4.2.1. Controls (Section 4.2) were applied to task-specific REVE and BIOT claims. ¶The AD-vs-FTD row uses 11,267 epochs from 59 subjects.

Pretraining provenance. Two rows carry exposure that bars an out-of-domain reading. CHB-MIT was included in BIOT’s pretraining [11], so its top rank on that task is not evidence of transfer. On TUAB the overlap is universal: LaBraM, CBraMod, and EEGMamba were pretrained on TUEG [4–6], REVE’s corpus includes TUH (14,987 subjects, 44% of corpus) [7], and BIOT was pretrained on TUH [11]. Every TUAB entry is therefore provenance-limited, and none should be compared against a confirmed out-of-domain estimate. The LaBraM AD-vs-HC entry carries a separate reproducibility caveat: its 129-entry position tensor is interpolated to 20 entries with F.interpolate, which is non-deterministic on Apple MPS, and five load-and-extract cycles on identical input with a fixed CV seed give 0.760 ± 0.007. Reading the benchmark and subsequent controls. Four observations orient the control analyses, and none is an overall ranking. First, the largest directly comparable descriptive exceedances of the simple classical column occur on CHB-MIT and the AD- versus-FTD contrast. On AD versus HC, CBraMod, BIOT-bipolar16, and REVE are also 1.7–3.0 pp above simple classical, but the enhanced classical family reaches 83.5% (Table 4), leaving only a 0.1 pp descriptive difference for BIOT and no controlled foundation-model advantage. Second, REVE is numerically highest on TUAB, but its 3,000-epoch sample differs from the 4,807-epoch sample used by the other rows, and pretraining overlap is confirmed for every encoder; no TUAB model margin is therefore estimated. Third, on the external CAUEEG cohort the ordering inverts: the handcrafted column is highest and every encoder sits below it. Fourth, encoder coverage is not a full grid, so a column mean would be computed over different task sets per model and is not reported. The study evaluates claim robustness, not an overall model ranking. Because the tasks differ in cohorts, outcomes, preprocessing, representation construction, and validation units, the study does not seek an overall model ranking. Instead, it evaluates whether apparent advantages within each task remain credible after targeted controls. Beyond the provenance warnings above, the primary CAUEEG analysis uses recording-level folds while the others use subject-disjoint folds, and CHB-MIT uses 512-dimensional mean pooling, the ds004504 REVE analyses use the historical 38,912-dimensional flat-LayerNorm representation, and TUAB uses token flattening. We therefore restrict ourselves to three descriptive observations. Task pattern: On CHB-MIT and AD versus FTD, pretrained

15

<!-- page 16 -->

REVE is above matched fully random initialization, whereas on CAUEEG it is below; these directions are pipeline-specific. The AD-versus-HC mean is matched by stronger classical comparators (Section 4.2.1). On AD versus FTD REVE (76.7%) and BIOT-bipolar16 (68.7%) exceed the classical mean (67.1%), by 9.6 and 1.6 pp respectively, while LaBraM,

CBraMod and EEGMamba fall below it; paired control intervals for both positive margins cross zero (Section 4.2.2). Channel-count hypothesis: no evaluated encoder has a mean AUROC above the simple classical mean on 2-channel Sleep-EDF, whereas CHB-MIT uses 18 channels, but task, dataset, montage, and label construction are confounded, so a matched channel-ablation experiment would be required before attributing this to spatial coverage. Model-size hypothesis: REVE has the highest numerical mean on TUAB, but uses a separate epoch sample and overlap is confirmed for all five encoders; moreover, the benchmark varies parameter count together with architecture, objective, corpus, exposure, and preprocessing compatibility, so it cannot establish that larger models or corpora cause better clinical discrimination. The CHB-MIT row of Table 3 motivates the task-specific controls below. Task construction on CHB-MIT. Because CHB-MIT carries the paper’s clearest pretrained-versus-random separation, its task definition warrants statement in the main text. Positive epochs overlap an annotated seizure by ≥50%; negative epochs are interictal segments drawn from the same seizure-containing recordings, so the task is within-session ictal-versus-interictal discrimination generalized across held-out patients. An independent sensitivity implementation gives 0.798 both without and with a ±30 s peri-ictal guard band, 0.787 when negatives are drawn from all available files, and 0.802 after excluding chb12. The primary run is 0.793; the small offset reflects independently extracted epochs and different negative identities under the same fixed 1:3 ictal:interictal sampling ratio, not a change in sample count. These checks reduce concern about recording-session and near-onset confounding. REVE exceeds the simple classical baseline by +9.3 pp (Wilcoxon p=0.012, d=0.61, n=23). Two caveats bound that figure: LOSO training sets

overlap, so the fits are not independent, and the amplitude-normalized input omits an amplitude-aware handcrafted comparator. The result does not license sample-precise onset localization or treatment-response prediction. The probe configuration is likewise not driving the estimate: on the 512-dimensional mean-pooled representation the in-fold PCA sweep is flat, giving 0.789 at 50 dimensions, 0.781 at 100, 0.793 at 200, and 0.794 at the full 512, so the selected PCA-200 reduction does not materially change the result relative to the full representation. Exact negative-pool results and the dimensionality and probe-regularisation sensitivities are reported in Supplementary Material, Section S4 (“CHB-MIT task construction and robustness”).

Subject-level aggregation on ds004504. Aggregating epoch probabilities to one score per subject raises AUROC for Classical and REVE on both ds004504 contrasts. It preserves the REVE-over-Classical ordering on AD versus FTD but reverses the epoch-level ordering on AD versus HC, where Classical is numerically higher. These changes show that epoch- and subject-level AUROC are distinct estimands; fold dispersion remains descriptive. Supplementary Material, Section S5 (“Subject-level aggregation on ds004504”; Table S6) reports the exact AUROCs, changes from the epoch-level estimates, and retained fold SDs.

16

<!-- page 17 -->

## 4.2 The Negative-Control Suite

The estimates in Table 3 are the input to this section, not its conclusion. Four controls are applied, each targeting a different alternative explanation for an apparent gain: a weak comparator (Section 4.2.1), the architecture rather than the pretrained weights (Section 4.2.2), probe capacity rather than label structure (Section 4.2.3), and label-specific

rather than label-independent adaptation (Section 4.2.4). The controls are targeted rather than exhaustive. Control 1 compares the encoders against the handcrafted families within its five completed tasks; comparator adequacy was not adjudicated on TUAB. Controls 2 and 3 target task-specific REVE and BIOT claims, whereas Control 4 is REVE-only. The task coverage and analysis unit are stated in each control subsection.

4.2.1 Control 1: Stronger handcrafted comparators

The first control asks whether an apparent encoder advantage survives a comparator stronger than band power. The current enhanced handcrafted family is evaluated on four benchmark tasks and CAUEEG; TUAB is excluded because its retained caches cannot support a protocol-matched rerun. The auxiliary ds003490 dataset carries no task and is excluded by construction. Each included task keeps its own specified probe, folds, and epoch definition, so Table 4 is a within-task simple-versus-enhanced contrast rather than a cross-task ranking. The encoder with the highest descriptive AUROC among those provenance-eligible is shown for each task. Following success condition (i) of Section 3.6, the final column subtracts the stronger of the simple and enhanced handcrafted families under the matched logistic probe; the simple family is stronger on AD versus FTD, Sleep- EDF, and CAUEEG. Using the enhanced family unconditionally would create apparent encoder gains on rows where it underperforms the simple family. Both delta columns use unrounded values and therefore need not equal differences calculated from the rounded cells shown.

Table 4: Control 1 matched-logistic AUROCs on four benchmark tasks and CAUEEG; TUAB was not evaluated. Differences are in percentage points.

Task

Simple AUROC (%)

Enhanced AUROC (%)

Enh. −simple

(pp)

Eligible encoder

AUROC (%)

Encoder −best handcrafted (pp)

Ictal detect (CHB-MIT)† 70.0% 71.5% +1.5 REVE 79.3 +7.8 AD vs Control∥ 80.6% 83.5% +2.9 BIOT-bipolar16 83.6 +0.1 AD vs FTD∗∗ 67.1% 64.3% −2.8 REVE 76.7 +9.6 Wake/Sleep (Sleep-EDF)§ 68.6% 67.5% −1.1 CBraMod 68.3 −0.3 N/MCI/dementia (CAUEEG)¶ 72.0% 70.9% −1.0 BIOT-bipolar16 67.7 −4.3 Provenance eligibility. An encoder is eligible only if published pretraining inventories show no confirmed evaluation-cohort or close distributional exposure. †BIOT-bipolar16 was pretrained on CHB-MIT; REVE is the highest provenance-clean encoder. On Sleep-EDF, sleep-domain exposure excludes LaBraM and EEGMamba; BIOT is unavailable, and CBraMod has the highest estimate among the remaining eligible encoders. ∥AD versus Control values are notch-filtered. §Sleep-EDF uses matched subjects, epochs, folds, and C = 1; a separate feature-count sensitivity is descriptive. ∗∗AD versus FTD uses 11,267 epochs from 59 subjects. ¶CAUEEG uses the prespecified LogReg comparison on identical folds; Supplementary Material, Section S3.1 reports the complete three-probe matrix. The eligible encoder is selected descriptively without model-selection-adjusted uncertainty. The matched-logistic CHB-MIT margin in this table is distinct from the post-hoc enhanced-GBM sensitivity reported below.

Table 4 shows an increase from simple to enhanced classical features on two tasks: CHB-MIT (70.0% to 71.5%) and notch-filtered AD versus Control (80.6% to 83.5%). On AD versus Control, enhanced classical exceeds REVE (83.5% vs. 82.8%), while the

17

<!-- page 18 -->

descriptively selected eligible BIOT-bipolar16 estimate is 0.1 pp higher still. On the other three tasks the enhanced mean is lower than the simple mean. Using the stronger matched- logistic handcrafted family on each row, REVE remains 7.8 pp higher on CHB-MIT and 9.6 pp higher on AD versus FTD, whereas CBraMod is 0.3 pp lower on Sleep-EDF and BIOT-bipolar16 is 4.3 pp lower on CAUEEG. The CHB-MIT, Sleep-EDF, and CAUEEG matched-logistic margins are descriptive point estimates without model-difference intervals. For AD versus FTD, the separate primary-pipeline REVE–simple comparison has a paired CI of [−3.2, 23.4] pp, which crosses zero (Section 4.2.2). Comparator choice can change a model-specific conclusion. On Sleep-EDF, provenance-eligible CBraMod (68.3%) is above the 67.5% enhanced mean while remaining below the 68.6% simple mean. On AD versus HC, the same reversal holds for the prespecified REVE comparison: REVE (82.8%) is above the 80.6% simple mean but below the 83.5% enhanced mean. It does not hold for the descriptively selected best eligible encoder, BIOT-bipolar16 (83.6%), which differs from the enhanced mean by only 0.1 pp. The Sleep-EDF and REVE AD-versus-HC comparisons remain descriptive means without model-difference intervals. For BIOT versus enhanced handcrafted features, the conditional paired pooled-OOF interval is [−6.2, 6.3] pp and crosses zero. Every point margin is smaller than the corresponding fold SD. The result is therefore sensitivity of the comparison to the chosen model and handcrafted family, not evidence of an advantage in either direction.

To further test whether nonlinear classifiers close the gap, we evaluated task-specific, post-hoc GradientBoosting and MLP configurations. AD versus HC used balanced training- sample weights for GradientBoosting and a two-hidden-layer MLP with early stopping on an epoch-random subset of each outer training fold; CHB-MIT used an unweighted GradientBoosting fit and a one-hidden-layer MLP. These single-seed configurations are exploratory rather than a common tuned estimator. On Alzheimer’s detection the observed mean gap closes, and not only through classifier capacity: the linear enhanced family already reaches 83.5%, 0.7 pp above notch-filtered REVE (82.8%), and an MLP on the full 173-feature simple handcrafted family reaches 83.3 ± 9.4% AUROC across folds, 0.5 pp above it. Its epoch-random inner validation is not participant-grouped, and seed stability is untested. Subject-level AUROC is likewise not higher for REVE (86.7% vs. 87.8% Classical; Section 4.1). An exploratory within-REVE frequency-band sensitivity is reported in Supplementary Material, Section S6 (“Exploratory REVE frequency-band ablation”); it uses C=1 and does not alter the matched encoder-versus-classical comparison above. On CHB-MIT, enhanced-GBM reaches 0.739 versus REVE 0.793. The paired equal-subject difference is +5.38 pp with a 95% held-out-subject bootstrap CI of [−0.36, 11.22] pp and conditional exact sign-flip p=0.0883. The interval crosses zero; LOSO training sets overlap, enhanced GBM was selected post hoc, and the normalized-input pipeline cannot reconstruct an amplitude-aware comparator because raw EDF waveforms and pre-normalization scales are unavailable in the retained materials.

4.2.2 Control 2: Matched fully random initialization

The second control asks whether pretrained weights, as opposed to the architecture and probe, carry the signal. REVE was fully instantiated from its pinned architecture for each random seed; every audited encoder tensor differed from the checkpoint. BIOT was likewise instantiated from its pinned architecture, with zero ordinary trainable tensors identical to the checkpoint; its deterministic non-trainable channel-index tensor was

18

<!-- page 19 -->

excluded from that count. Table 5 reports the completed model-specific comparisons.

Table 5: Control 2: matched fully-random-initialization results. Values are AUROC; ∆ is pretrained minus fully random. The raw-signal random-feature reference was run on CHB-MIT only.

Task Pretrained

Fully random

Raw random

features

∆ (pp) Retained comparison unit

CHB-MIT 0.793 0.691 0.505 +10.2 23 fold scores per seed CAUEEG 0.570 0.667 — −9.7 3 paired run means AD vs. FTD (REVE) 0.767 0.574 — +19.3 five fixed folds, three random seeds AD vs. HC (BIOT) 0.836 0.835 — +0.1 five fixed folds, one random seed AD vs. FTD (BIOT) 0.687 0.633 — +5.4 five fixed folds, one random seed

CHB-MIT and CAUEEG REVE rows use three random seeds; AD-versus-FTD REVE uses three random seeds on the primary fixed folds; each BIOT row uses one fully random seed. Paired uncertainty for ds004504 is reported in the text because its bootstrap estimand differs from the canonical mean-fold delta. All point contrasts remain conditional on the stated architecture, representation, probe, and folds.

On CHB-MIT, matched fully randomly initialized REVE encoders with seeds 42, 43, and 44 reach mean-fold AUROCs of 0.691, 0.696, and 0.687, respectively (grand mean 0.691), compared with 0.793 for pretrained REVE. A Gaussian random projection of the normalized raw epoch signal reaches 0.505 across three constructions. Thus the descriptive pretrained-minus-fully-random difference is +10.2 pp, while the raw-signal reference is near chance. Seed-specific held-out-subject fold scores are retained, but the LOSO training sets overlap and the same held-out subjects recur across initialization seeds; we therefore report no inferential interval or test. Three Gaussian constructions also do not bound what other raw-signal features could extract. Within those limits, the result supports a pretrained-weight contribution under the evaluated CHB-MIT pipeline rather than an architecture-only or probe-only reading.

On CAUEEG, every pretrained/fully-random pair uses the same clean 19-channel inputs, split, and StandardScaler–PCA-50–SVM-RBF probe on the primary 38,912- dimensional flattened-token, whole-vector-LayerNorm recording representation. A six- record raw-EDF check spanning all three classes reproduced the retained primary vectors at rtol/atol 10−4. Across paired initialization/split states 42/42, 43/142, and 44/242, pretrained run means are 0.569, 0.578, and 0.563, whereas the matched fully-random means are 0.666, 0.669, and 0.665. Fully random initialization is therefore higher by 9.62, 9.18, and 10.21 pp, yielding grand means of 0.570 and 0.667. The direction is consistent across the three runs, but the same 1,187 recordings recur and test sets overlap across split states, so the run means are not independent replications and no inferential p-value is claimed. The opposing CHB-MIT and CAUEEG directions show that the pretrained-weight contribution is task-specific; they do not support a general encoder effect in either direction.

On AD versus FTD, pretrained REVE reaches 0.767 and simple classical reaches 0.671. Three fully random REVE encoders yield a grand mean of 0.574, a +19.3 pp pretrained- minus-random separation. Every epoch representation uses the 38,912-dimensional flat- LayerNorm contract and the same fixed five folds, fold-local scaling, and balanced logistic probe. The paired within-fold subject-cluster bootstrap for the REVE-minus-simple mean-fold difference is +9.6 pp with 95% CI [−3.2, 23.4] pp. The interval crosses zero, so the positive point margin is not resolved despite the descriptive pretrained-versus-random separation.

19

<!-- page 20 -->

For BIOT, the AD-versus-HC pretrained and single-seed fully-random means are 0.836 and 0.835; the paired participant-cluster interval for pretrained minus enhanced handcrafted is [−6.2, 6.3] pp and for pretrained minus random is [−4.6, 6.0] pp. On AD versus FTD, the corresponding means are 0.687 and 0.633, with intervals [−8.2, 11.8] pp against simple handcrafted and [−2.9, 15.1] pp against random. These diagnosis-stratified participant-cluster intervals target pooled out-of-fold epoch-AUROC differences conditional on fixed predictions; they do not refit models or include comparator-selection or random- seed variance. All four cross zero, so neither the tiny AD-versus-HC margin nor the AD-versus-FTD margin supports resolved BIOT attribution.

4.2.3 Control 3: Label permutation

The third control asks whether a probe estimate reflects label structure or merely probe capacity on high-dimensional embeddings. Labels are permuted and the identical probe is refit. Table 6 reports every completed diagnostic label-permutation analysis and its task-specific permutation scheme.

Table 6: Control 3: model-specific label-permutation analyses. Observed and null AUROCs belong to the stated analysis unit and probe.

Task Observed

Null mean

± SD Shuffles Nominal p Permutation and probe scope

CHB-MIT (REVE) 0.793 0.502 ± 0.010 100 0.0099 Within-subject shuffling; exact headline in-fold pipeline AD/HC (BIOT) 0.836 0.503 ± 0.073 100 0.0099 Participant labels; primary epoch pipeline, fixed folds AD/HC (REVE) 0.860 0.507 ± 0.114 100 0.0099 Participant labels; direct subject-mean probe AD/FTD (BIOT) 0.687 0.498 ± 0.090 100 0.0198 Participant labels; primary epoch pipeline, fixed folds AD/FTD (REVE) 0.670 0.517 ± 0.106 100 0.0990 Participant labels; direct subject-mean probe AD/FTD/HC (REVE) 0.805 0.490 ± 0.068 100 0.0099 Participant labels; direct three-way subject-mean probe

Every row reuses precomputed folds and applies the finite-randomization correction. CHB-MIT refits PCA-200, scaling, and logistic regression inside every LOSO training fold. BIOT rows retain the primary epoch-level pipelines; REVE ds004504 rows use one direct 38,912-dimensional subject-mean vector per participant. The analyses test label dependence for their stated probes, not between-model effects or freedom from other confounding.

On CHB-MIT, the label-permutation analysis now matches the headline pipeline exactly: within every fixed held-out-subject fold it fits PCA-200 on training embeddings, then fits the scaler and balanced C=1 logistic probe on the training coordinates. Across 100 within-subject permutations, the null mean is 0.502 ± 0.010 versus the reproduced observed mean of 0.793; zero permutations meet or exceed the observed value, giving p=0.0099. This establishes label dependence for the exact headline representation and probe, not a model-comparison or population-level causal result.

The BIOT ds004504 permutations follow each primary epoch-level pipeline: one diagnosis is permuted per participant, broadcast to all of that participant’s epochs, and evaluated on the fixed folds. AD/HC yields 0.836 versus 0.503 ± 0.073 (p=0.0099), and AD/FTD yields 0.687 versus 0.498 ± 0.090 (p=0.0198). Thus both BIOT probes depend on the observed participant diagnoses, although that does not resolve their pretrained- versus-comparator or pretrained-versus-random margins.

The REVE ds004504 sensitivities instead average the same historical flat-LayerNorm epoch vectors within participant and fit a direct fold-local scaled probe. AD/HC and three-

20

<!-- page 21 -->

way AD/FTD/HC exceed their permutation nulls (p=0.0099 each). Binary AD/FTD yields 0.670 versus 0.517 ± 0.106, with p=0.0990; this subject-mean control does not establish label dependence at the conventional 0.05 level and is not the primary epoch- level estimand. No Control 3 result is reported for TUAB, Sleep-EDF, or CAUEEG. None of these randomization tests is a between-model comparison or a test against every leakage or confounding mechanism.

4.2.4 Control 4: Scrambled-label adaptation

The fourth control asks whether a gain from task-specific adaptation depends on the labels being correct. We treat adaptation as a secondary sensitivity analysis because model, task, split, and optimization recipe vary across configurations. LoRA [39] inserts trainable low-rank matrices while leaving the pretrained backbone frozen; these experiments do not support a general sample-size, model-size, or deployment rule. CAUEEG adaptation stability comparisons. On the binary task, the three-run correct-label mean (0.8397) is within 0.06 pp of the five-run scrambled-label mean (0.8392). The correct-label runs used up to 20 training epochs with early-stopping patience 5, whereas the scrambled-label runs used up to 10 epochs with patience 3; their seed sets are also not paired. This is therefore an unmatched descriptive sensitivity, not an equivalence or label-effect test. On the three-way task, the source-cap-matched correct-label run (0.7074) is within 0.35 pp of the five-run scrambled-label mean (0.7039), but the downstream SVM settings differ and the correct-label run did not retain an explicit training seed. That comparison likewise does not isolate label correctness.

Adapted arms read CAUEEG amplitudes in microvolts, whereas the clean frozen reference receives volt-scale values, and their probes differ. Adapted-versus-frozen contrasts therefore cannot be interpreted as adaptation effects. Supplementary Material, Section S7 (“Adaptation protocol provenance and seed structure”) reports the complete results,

source-cap and full-source distinction, seed structure, and protocol differences. Within those limits, the numerical similarity does not provide evidence that correct Western source labels improved CAUEEG performance, but no mechanism is identified.

## 4.3 External-Cohort Stress Test (CAUEEG, Normal/MCI/Dementia)

Figure 2 summarizes the matched clean-input comparison and the two-task fully-random- initialization contrast. Matched clean-input comparison. CAUEEG differs from the benchmark cohorts and exposes no patient identifier [30]; the primary analysis is recording-level. Every representation starts from the same clean 19-channel montage, excluding EKG and Photic; BIOT receives the 16 upstream bipolar derivations constructible by named subtraction. All rows use identical five-fold partitions and LogReg, LDA, and SVM-RBF probes. The simple classical family reaches 0.734 AUROC, versus BIOT 0.677, CBraMod 0.669, REVE 0.568, EEGMamba 0.537, and LaBraM 0.527: a graded 5.7–20.7 pp deficit relative to the simple headline comparator. The enhanced SVM-RBF sensitivity is 0.736, only 0.18 pp above simple SVM-RBF and without a difference interval; its matched LogReg estimate is lower (0.709 vs. 0.720). We therefore retain simple classical as the headline comparator and treat

LDA/SVM-RBF and best-of-family summaries as descriptive sensitivities. Supplementary Material, Section S3.1 (“Complete clean-input probe matrix”) is the authoritative full-

21

<!-- page 22 -->

Figure 2: The external-cohort stress test and its fully-random-initialisation control. (a) Best-probe macro-AUROC for every representation from the clean 19-channel CAUEEG

source montage under identical folds; BIOT uses the 16 upstream bipolar derivations constructible from it. The simple classical family is the headline comparator; the enhanced family is shown as the comparator sensitivity and is 0.18 pp above it, which we do not promote (Section 4.2.1). All five encoders fall below both; relative to the simple headline comparator, the deficits are 5.7 to 20.7 pp. (b) The matched fully-random-initialisation control on the two tasks shown. Pretrained REVE is above fully random initialization on CHB-MIT and below it on CAUEEG, so the observed contribution of pretrained weights is task-specific rather than uniformly positive. Panel (b) is descriptive: fold positions are not paired across the repeated CAUEEG splits and no inferential p-value is claimed.

precision matrix and includes fold SDs. The separate adaptation sensitivities and their protocol mismatches are reported in Section 4.2.4 and Supplementary Material, Section S7.

## 4.4 Linear Probes Perfectly Decode Dataset Membership

Dataset-identity probe. All five encoders separate ds004504 from CAUEEG at AUROC 1.000 in full space and after in-fold PCA-50 (Table 7). BIOT uses the 16 upstream bipolar derivations available in both cohorts; the other encoders use their specified 19-channel representations. Across 20 label permutations the encoder means are 0.488–0.506, showing that the probe does not produce ceiling values for arbitrary labels; ten balanced 88-versus- 88 draws remain at 1.000, ruling out class imbalance as the explanation. The REVE-only Western–Western ds004504–ds003490 sensitivity reaches 1.0000 in full space and 1.0000

after in-fold PCA-50. After restricting ds004504–CAUEEG inputs to 0.5–40 Hz and z-scoring each epoch, REVE reaches 0.9991 in full space and 0.9998 after in-fold PCA-50. For REVE, near-ceiling decoding is therefore neither unique to the tested Western–Korean pair nor removed with line-frequency and absolute-scale cues. The result remains dataset membership: device, montage, preprocessing, population, and clinical composition vary together and cannot be separated causally. The two REVE-only extensions are reported in Supplementary Material, Section S8 (“Supplemental dataset-identity controls”).

22

<!-- page 23 -->

Table 7: Dataset-identity decoding is a property of every evaluated encoder, not of REVE alone. Values are mean five-fold AUROC for predicting which dataset produced a recording (ds004504 n=88 versus CAUEEG n=1,187), under one probe applied to each encoder’s frozen specified representation (BIOT upstream bipolar16; 19 channels for the other encoders). The two right-hand columns are controls on the ceiling itself: with the dataset label permuted every encoder falls to chance, and on a balanced 88-versus-88 subsample every encoder stays at ceiling. The label is dataset membership; site, device, montage, preprocessing, population, and clinical composition are confounded within it.

Encoder Dim. Full space PCA-50 Permuted label Balanced 88 vs. 88

REVE 38,912 1.000 1.000 0.495 ± 0.035 1.000 BIOT 256 1.000 1.000 0.495 ± 0.040 1.000 CBraMod 200 1.000 1.000 0.492 ± 0.043 1.000 EEGMamba 200 1.000 1.000 0.488 ± 0.038 1.000 LaBraM 200 1.000 1.000 0.506 ± 0.035 1.000 Probe: per-feature standardisation, then optional in-fold PCA-50, then L2-regularised logistic regression with balanced class weights, five stratified folds, seed 42. Permutation uses 20 shuffles and the balanced control 10 draws, both at PCA-50. Because all five encoders sit at 1.000, the probe supports a shared property of the panel and cannot rank encoders. The Western–Western ds003490 pair and the 0.5–40 Hz z-scored sensitivity were run for REVE only.

## 4.5 Patient-Overlap Sensitivity

Patient-overlap sensitivity. In the public CAUEEG repository (https:// github.com/ipis-mjkim/caueeg-dataset, accessed 6 August 2026), the authors’ dementia-no-overlap.json task file provides the available patient-overlap annota- tion [30]. It removes 65 of 237 held-out recordings while leaving the training split fixed. On the resulting annotated no-overlap held-out subset (n=172 recordings), classi- cal LogReg reaches 0.7165 (recording-bootstrap 95% CI [0.6560, 0.7753]) versus REVE LogReg 0.5653 ([0.5083, 0.6250]). The classical–REVE gap is about five percentage points larger in the overlap-permitting fixed-split sensitivity than on the annotated no-overlap subset, so overlap may inflate the observed gap. This is not a mathematical bound on the separate five-fold estimator: the bootstrap treats recordings as independent, general patient identifiers are unavailable, and repeat recordings wholly within training remain unquantified. The complete full-, annotated no-overlap, and overlap-only probe matrix is reported in Supplementary Material, Section S3.2 (“Patient-overlap sensitivity”).

## 4.6 Inference Status

Primary-task inference. TUAB, Sleep-EDF, and the primary CAUEEG five-fold matrix remain descriptive: they have point estimates and fold variation, but no paired model- difference interval. The CAUEEG intervals in the preceding subsection are marginal recording-bootstrap intervals from one fixed annotated no-overlap split; they are not patient-level intervals or paired between-model effects. The complete overlap matrix is reported in Supplementary Material, Section S3.2.

On CHB-MIT, the REVE-versus-simple comparison gives Wilcoxon W=57, nominal p=0.012, and paired d=0.61 across 23 held-out-subject folds. Against the stronger post- hoc enhanced GBM, the paired difference is +5.38 pp with CI [−0.36, 11.22] pp and conditional sign-flip p=0.0883. The interval crosses zero; moreover, LOSO training sets

23

<!-- page 24 -->

overlap and the stronger comparator was selected after inspection, so neither result is confirmatory.

For ds004504 AD versus HC, the marginal REVE and classical fold intervals do not estimate a paired model difference. The conditional BIOT-minus-enhanced interval [−6.2, 6.3] pp crosses zero. For AD versus FTD, the REVE-minus-simple difference is +9.6 pp with CI [−3.2, 23.4] pp, and the BIOT-minus-simple CI is [−8.2, 11.8] pp; both

cross zero. The REVE interval resamples participants within fixed folds and targets the mean-fold difference, whereas the BIOT intervals target pooled out-of-fold epoch-AUROC differences conditional on fixed predictions. Neither procedure refits models or incorporates comparator-selection or random-seed uncertainty. Targeted controls. The fully-random-initialization contrasts in Table 5 are model- specific; the ds004504 paired intervals are conditional on fixed predictions and exclude random-seed variance. The permutation analyses in Table 6 test label dependence within their stated units and probes, not patient-level population effects or between- model differences. CAUEEG random-initialization runs also reuse recordings across split states. These controls therefore answer narrower questions and do not confer confirmatory inference on the primary comparisons. CHB-MIT robustness details are in Supplementary Material, Section S4, and adaptation-protocol provenance is in Section S7.

## 5 Discussion

Across the six primary tasks, no encoder advantage satisfies all four attribution conditions. Interpretation depends on pretraining provenance, comparator strength, probe design, and analysis unit (Section 4.6).

## 5.1 Observed Advantages Depend on Task, Provenance, and Comparator

On TUAB, REVE has the highest numerical mean, but it uses a separate 3,000-epoch sample while the other reported rows use 4,807 epochs; Table 3 also documents confirmed TUH or adjacent-distribution exposure for every encoder. TUAB therefore supplies neither a matched model margin nor evidence that scale or transfer caused the numerical ordering, and comparator adequacy was not adjudicated with the current enhanced family. On AD versus HC, enhanced classical features and an exploratory MLP on the full simple handcrafted family have mean AUROCs that match or exceed REVE. BIOT is only 0.1 pp above enhanced classical in the mean-fold summary, and its paired conditional interval crosses zero. On CHB-MIT, pretrained REVE is higher than fully random initialization and the tested normalized-input baselines, but the paired strongest-comparator interval crosses zero and an amplitude-aware comparator cannot be reconstructed from the retained normalized epochs.

The CAUEEG stress test sharpens that caution. Under the shared clean-input protocol, all five encoders range from 0.527 for LaBraM to 0.677 for BIOT-bipolar16, below 0.734 for simple classical features (0.736 for the enhanced sensitivity). In the repeated-split fully-random-initialization comparison, fully random initialization is descriptively higher in all three run means, which is directionally inconsistent with a benefit from REVE’s pretrained weights under the evaluated probe; no inferential p-value is claimed because the runs reuse recordings. Linear probes decode dataset membership at AUROC 1.000

24

<!-- page 25 -->

for all five encoders in both full space and after in-fold PCA-50, but this observation does not explain the clinical-task deficit causally: site, device, montage, preprocessing, population, and diagnosis composition are bundled. These results do not establish that greater pretraining scale or a favorable numerical position on another task yields better performance on this cohort.

## 5.2 Channel Count as a Hypothesis

None of the four encoders evaluated on Sleep-EDF has a mean AUROC above the classical mean on the 2-channel binary task; no paired model-comparison test was computed. Sparse spatial coverage and the binary coarsening of the sleep-stage labels are plausible contributors, but they are confounded in this single dataset and were not experimentally separated. The result therefore motivates, rather than establishes, a channel-density hypothesis. Testing that hypothesis requires a richer-montage sleep cohort with controlled within-recording channel ablation while holding the label construction fixed.

## 5.3 Frozen Probing and Configuration-Specific Adaptation

The divergence between cross-subject ictal detection and the other evaluated configurations suggests hypotheses about compatibility with frozen probing, but the benchmark does not isolate task type from dataset and representation:

• Discrete events. CHB-MIT ictal versus interictal discrimination is captured by frozen REVE and shows a descriptive pretrained-versus-fully-random-initialization separation; untested event types such as spike-wave discharges or sleep spindles are not implied. • Diffuse states. Results are mixed: REVE leads descriptively on TUH nor- mal/abnormal, but confirmed TUH distributional overlap prevents a transfer interpre- tation; stronger classical comparators close the AD-versus-HC mean gap; and every evaluated encoder is below simple classical on CAUEEG Normal/MCI/dementia. Medication effects were not evaluated. • Differential diagnosis. On AD versus FTD, REVE (76.7%) and BIOT-bipolar16 (68.7%) are descriptively above simple Classical (67.1%), whereas LaBraM, CBraMod,

and EEGMamba are below it. REVE is 19.3 pp above the three-seed fully-random grand mean, but its paired comparator CI [−3.2, 23.4] pp crosses zero and its subject- mean label permutation gives p=0.0990. BIOT is 5.4 pp above one fully-random seed and passes its participant-label permutation, but both paired conditional intervals cross zero. The controls therefore characterize the positive point estimates without establishing either encoder’s advantage over handcrafted features.

LoRA sensitivities are reported in Section 4.2.4 and Supplementary Material, Section S7. Both the binary and three-way correct-versus-scrambled comparisons are unmatched descriptive sensitivities because their training or downstream-probe protocols differ; neither is an equivalence test or a label-effect estimate. Adaptation remains configuration-specific. The LoRA experiments vary model

family, task, sample size, and training recipe simultaneously, so they do not establish universal sample-size or model-to-data thresholds. They show only that adaptation can be unstable and that, under these settings, a claim of label-specific transfer requires a scrambled-label control.

25

<!-- page 26 -->

## 5.4 Limitations

1. Diagnostic tasks only, on public or registration-gated data. Every task here is retrospective diagnostic or state classification on third-party public or registration- gated cohorts. The protocol is not validated for, and these results say nothing about, treatment-response or pharmacodynamic biomarkers, which would require evaluation of within-subject change, test–retest reliability, and a defined context of use. Extending the control suite to longitudinal, outcome-labelled data is left to future work. 2. Subject-level metrics. Subject aggregation was retained only for the two ds004504 contrasts and cannot be reconstructed for TUAB from the retained data. Its task- specific ordering changes demonstrate that epoch- and subject-level estimates are not interchangeable; they do not establish clinical reliability or cross-cohort stability (Section 4.1; Supplementary Material, Section S5, Table S6). 3. Limited multi-class scope. Beyond binary tasks (seizure vs. interictal, nor- mal/abnormal, wake/sleep), the primary evaluation includes one three-way task (CAUEEG Normal/MCI/Dementia). A separate REVE-only Control 3 sensitivity

uses three-way ds004504 AD/FTD/HC. Regression and severity-scoring tasks are not assessed. 4. Model coverage and pretraining exposure. BIOT was evaluated with its bipolar16 input contract on CHB-MIT, both ds004504 contrasts, and CAUEEG. Sleep-EDF cannot supply the contract, and TUAB is not reported because the required named-channel input is unavailable. BIOT reaches 0.875 on CHB-MIT but was pretrained on that dataset [11], so its estimate cannot distinguish memorization from distribution familiarity. REVE and LaBraM are descriptively similar (0.793 and 0.792); additional controls cover REVE on CHB-MIT, AD versus FTD, and CAUEEG, and BIOT on both ds004504 contrasts, not the complete model–task grid. 5. REVE sleep evaluation note. REVE was evaluated on Sleep-EDF using com- pound channel names (Fpz-Cz, Pz-Oz) resolved to single electrodes (Fpz, Pz) for the REVE position bank. This coordinate substitution is a practical approximation. Evaluation on a separate sleep cohort with a full 10–20 montage and controlled channel ablation would provide a cleaner spatial-signal test. 6. REVE’s gated license. REVE’s model-card access requires registration and agreement to responsible-use terms, limiting reproducibility for groups without access (https://huggingface.co/brain-bzh/reve-base, accessed 6 August 2026). 7. Position embedding interpolation for LaBraM. The executed loader linearly interpolates LaBraM’s 129-entry spatial position tensor to Nch + 1 entries and its 16-entry temporal tensor to five positions for the 4-s inputs. These study-specific transformations may alter its representations; published LaBraM benchmarks use the native 128-channel configuration [4]. 8. EEGMamba implementation fidelity. EEGMamba’s CUDA-only Mamba2 selective scan was reimplemented in pure PyTorch for CPU/MPS execution. All evaluated EEGMamba estimates are conditional on this local port, whose numerical parity with the upstream CUDA kernel was not independently tested. 9. Consumer hardware execution and TUAB subsampling. Computation was performed on one Mac M3 (16 GB) using CPU or MPS, which does not establish computational portability or clinical deployability. From 8,130 available TUAB

26

<!-- page 27 -->

epochs, Classical, LaBraM, EEGMamba, and CBraMod use a 4,807-epoch subject- capped sample, whereas REVE uses a separate 3,000-epoch global sample. Full-set encoder estimates were not run, and the REVE and non-REVE cells do not estimate matched model differences. A current-family enhanced comparator could not be reconstructed because the retained TUAB caches do not include the required raw signals and participant-group vector. 10. Task-specific extraction. CHB-MIT uses 512-dimensional mean-pooled REVE embeddings, ds004504 uses the historical 38,912-dimensional flat-LayerNorm repre- sentation, and TUAB uses token flattening. The REVE ds004504 label-permutation sensitivities average the flat-LayerNorm epoch vectors within participant; the primary ds004504 estimates and random-initialization control remain epoch-level. Extraction choices were not compared systematically across every task. 11. Limited statistical inference. The paired REVE-versus-simple-classical CHB- MIT comparison yields nominal p = 0.012 and paired d = 0.61, but LOSO training sets overlap. Against enhanced GBM, the paired CI [−0.36, 11.22] pp crosses zero; the comparator was selected post hoc and no amplitude-aware comparator can be reconstructed. The ds004504 paired intervals also cross zero and are conditional on fixed folds or predictions; the BIOT random comparison has one seed. CAUEEG repeated splits reuse recordings. These comparisons are bounded sensitivities rather than confirmatory population tests. 12. Label-dependence analyses. Control 3 covers exact-headline CHB-MIT REVE; primary-pipeline BIOT on both ds004504 contrasts; and subject-mean REVE on AD/HC, binary AD/FTD, and three-way AD/FTD/HC. The CHB-MIT and BIOT observed-label probes exceed their permutation nulls; the binary subject-mean REVE AD/FTD control does not establish label dependence at the conventional 0.05 level. No label-permutation result is reported for TUAB, Sleep-EDF, or CAUEEG. Each result is restricted to its stated unit, probe, and permutation scheme and is not a population test or model comparison (Section 4.2.3). 13. CAUEEG metadata do not support patient-grouped cross-validation. The primary CAUEEG folds are recording-level. On the n = 172 annotated no-overlap held-out recordings, clean classical LogReg has a higher point estimate than clean REVE LogReg (0.7165 vs. 0.5653), with wide recording-bootstrap intervals. The gap was about five points larger in one overlap-permitting fixed split, so overlap may inflate it; this does not bound the separate five-fold estimator, and repeat recordings wholly within training remain unannotated. Validation on additional external cohorts with complete recordings and subject-level outcome labels remains necessary before any population-level claim is warranted.

## 5.5 Attribution Status Under the Interpretive Framework

No task supports all four conditions in Section 3.6. The sequential rule makes the conclusion direct: once a positive model-specific margin fails comparator uncertainty or provenance, later controls may explain the pipeline but cannot restore an attribution claim.

TUAB stops before the first complete gate because REVE and the non-REVE rows use unmatched samples; all encoders also have confirmed TUH or adjacent-distribution exposure. Sleep-EDF and CAUEEG stop at the comparator gate because every tested encoder mean is below the handcrafted comparator. On AD versus HC, REVE is matched

27

<!-- page 28 -->

or exceeded by stronger handcrafted configurations. BIOT has a tiny positive mean- fold margin, but its conditional paired comparator CI [−6.2, 6.3] pp crosses zero; its pretrained-versus-random interval also crosses zero even though its label-permutation test is positive.

On AD versus FTD, REVE and BIOT are above simple classical in the point estimates, but both stop at paired uncertainty. REVE’s +9.6 pp difference has CI [−3.2, 23.4] pp; pretrained REVE is well above three fully-random seeds, whereas the subject-mean label audit gives p=0.0990. BIOT’s paired comparator CI is [−8.2, 11.8] pp; it is descriptively above one random seed and its primary-pipeline label audit gives p=0.0198. Neither pattern establishes superiority over handcrafted features. The other three encoders fall below the simple classical mean.

CHB-MIT also stops at paired comparator uncertainty. REVE exceeds enhanced GBM by 5.38 pp, but the paired held-out-subject CI [−0.36, 11.22] pp crosses zero (conditional sign-flip p=0.0883). CHB-MIT is absent from REVE’s published pretraining inventory, and both the matched random-initialization and exact headline label-permutation controls are positive, but those later gates cannot repair the unresolved strongest-comparator margin. The paired sensitivity is conditional on overlapping LOSO training sets and post-hoc comparator selection; an amplitude-aware comparator is blocked because the retained data contain only per-epoch normalized signals and no raw EDF waveforms or scale parameters.

## 5.6 Implications for Clinical EEG AI

REVE’s CHB-MIT result is task-relevant separability, not onset localization or external- population transfer. Paired uncertainty against the strongest tested comparator includes zero, and an amplitude-aware baseline cannot be reconstructed from the retained normal- ized data. More broadly, a clinical EEG foundation-model advantage is a task-specific attribution claim. Evaluations should report pretraining provenance, use the strongest task- appropriate handcrafted family, matched fully random initialization, label permutation, and, for adaptation claims, a scrambled-label control. Model comparisons require paired subject-level uncertainty when the analysis unit permits it. External-cohort evaluations should use subject-grouped splits when identifiers are available, and dataset-membership decoding should not be interpreted as diagnostic transfer. These are evaluation safeguards, not deployment rules.

## 6 Conclusion

Clinical EEG foundation-model claims should be evaluated as falsifiable comparisons rather than a leaderboard. Under the controls applied here, three findings remain. First, on the matched clean-input CAUEEG stress test every encoder falls below the simple classical comparator by 5.7–20.7 pp; the enhanced-comparator sensitivity preserves that all-encoder ordering, while the patient-overlap sensitivity separately preserves only the classical-over-REVE ordering. This is one external cohort with recording-level primary folds, not geographic replication. Second, dataset identity is decodable at ceiling from all five encoders on the Western–Korean pair and from REVE on the Western–Western pair. Because acquisition and cohort factors are bundled, this warns about dataset structure but does not identify a causal site mechanism. Third, CHB-MIT cross-subject ictal detection

28

<!-- page 29 -->

shows pretrained-weight and label dependence in the evaluated pipeline: pretrained REVE exceeds matched fully random initialization and raw-signal random features, and the exact headline pipeline exceeds its within-subject permutation null. Superiority over the strongest tested handcrafted comparator is unresolved because its +5.38 pp paired margin over enhanced GBM has CI [−0.36, 11.22] pp, and an amplitude-aware comparator cannot be recovered from the retained normalized data.

We therefore recommend model-compatible channel construction; subject-grouped eval- uation or an explicit leakage sensitivity; strong linear and nonlinear classical comparators; matched fully random initialization; label permutation; a dataset-membership probe; and scrambled-label adaptation controls when transfer learning is used. None of the present tasks clears all four conditions in Section 3.6, so no general claim of disease-information transfer across clinical populations is warranted.

## Data and Code Availability

CHB-MIT is available from PhysioNet [25], and Sleep-EDF is available through Phys- ioNet [29,40]. TUH TUAB requires application to Temple University [26,27]. OpenNeuro ds004504 is publicly available from OpenNeuro [28]. CAUEEG is distributed through the repository identified by its dataset publication [30]. The auxiliary dataset used only for the dataset-identity control, ds003490 [31], is openly downloadable from OpenNeuro. The evaluated REVE checkpoint (brain-bzh/reve-base) requires gated Hugging Face access under its model-card terms (https://huggingface.co/brain-bzh/reve-base, ac- cessed 6 August 2026). The evaluated LaBraM, EEGMamba (weighting666/EEGMamba), CBraMod, and BIOT (braindecode/biot-pretrained-six-datasets-18chs) check- points are identified in their respective model sources [4–6, 11]; access terms are set by the hosting repositories. Earlier reproducibility materials are publicly available at https://github.com/MarziehzZare/eeg-fm-negative-controls. A manuscript- matched release of the analysis code, preprocessing configurations, aggregate evidence artifacts, canonical numerical registry and ledger, and evaluation protocols has been prepared and will be posted at the same URL before publication. Raw or processed EEG, participant-level embedding caches, and third-party model weights are not redistributed.

## Acknowledgments

We thank the authors of LaBraM, EEGMamba, CBraMod, REVE, and BIOT for releasing

pretrained weights, and the Temple University Hospital EEG Corpus, PhysioNet, and OpenNeuro teams for maintaining open clinical EEG datasets. OpenAI Codex (GPT-5) and Anthropic Claude (Opus 5) were used under the author’s direction for code develop- ment, manuscript drafting and restructuring, copy-editing, and adversarial consistency review. The author critically reviewed all resulting analyses and text and takes full responsibility for their accuracy, integrity, and originality. No AI-generated data were used, and no AI tool is listed as an author.

29

<!-- page 30 -->

## Funding statement

This research received no external funding, and the work was self-funded by the corre- sponding author.

## Conflict of interest statement

The author has a potential commercial interest in EEG-based biomarker technology related to this work. The study used only third-party, de-identified, publicly available or registration-gated datasets; no proprietary data or commercial products were used or evaluated. The author declares no other competing interests.

## Ethical statement

This study is a secondary analysis of previously collected and de-identified EEG datasets. No new data were collected from human participants. Ethical approval for the original data collection was obtained by the respective data providers and is described in the original publications cited in Table 2 and Section 4.3. No additional ethical approval was required for this secondary analysis.

## Author Contributions

M.Z. is the sole author and conceived the study, designed the evaluation protocol and negative-control suite, implemented the analysis pipeline, performed all experiments and statistical analyses, and wrote and revised the manuscript.

## References

[1] Jayaram, V., Alamgir, M., Altun, Y., Sch¨olkopf, B., & Grosse-Wentrup, M. (2016).

Transfer learning in brain–computer interfaces. IEEE Computational Intelligence Magazine, 11(1), 20–31. https://doi.org/10.1109/MCI.2015.2501545.

[2] Bommasani, R., et al. (2021). On the opportunities and risks of foundation models.

arXiv:2108.07258.

[3] He, K., Chen, X., Xie, S., et al. (2022). Masked autoencoders are scalable vision

learners. Proc. CVPR, pp. 16000–16009.

[4] Jiang, W. B., Zhao, L. M., & Lu, B. L. (2024). Large Brain Model for Learning

Generic Representations with Tremendous EEG Data in BCI. Proc. ICLR (Spotlight).

[5] Wang, J., et al. (2025). EEGMamba: An EEG Foundation Model with Mamba.

Neural Networks, 192, 107816.

[6] Wang, J., et al. (2025). CBraMod: A Criss-Cross Brain Foundation Model for EEG

Decoding. Proc. ICLR.

30

<!-- page 31 -->

[7] El Ouahidi, Y., Lys, J., Th¨olke, P., Farrugia, N., Pasdeloup, B., Gripon, V., Jerbi,

K., & Lioi, G. (2025). REVE: A Foundation Model for EEG, Adapting to Any Setup with Large-Scale Pretraining on 25,000 Subjects. Advances in Neural Information Processing Systems (NeurIPS). arXiv:2510.21585.

[8] Wu, J., et al. (2025). AdaBrain-Bench: Benchmarking Brain Foundation Models for

Brain-Computer Interface Applications. arXiv:2507.09882.

[9] Kastrati, A., B¨urki, J., Lauer, J., Xuan, C., Iaquinto, R., & Wattenhofer, R. (2025).

EEG-Bench: A Benchmark for EEG Foundation Models in Clinical Applications. Foundation Models for the Brain and Body Workshop (BrainBodyFM), NeurIPS 2025. arXiv:2512.08959.

[10] Kontras, K., Osselaer, T., Mouslech, S. G., Karaiskou, A.-I., Gagliardi, G., Stryp-

steen, T., Badiei, M. H., Rani, A., Vanmarcke, M., Bhagubai, M., Ekbote, C., Hwang, J., Chatzichristos, C., Liang, P. P., & De Vos, M. (2026). NeuroAtlas: Benchmarking Foundation Models for Clinical EEG and Brain-Computer Interfaces. arXiv:2605.14698.

[11] Yang, C., Westover, M. B., & Sun, J. (2023). BIOT: Biosignal Transformer for

Cross-data Learning in the Wild. Advances in Neural Information Processing Systems (NeurIPS), 36, 78240–78260.

[12] Gu, A. & Dao, T. (2024). Mamba: Linear-time sequence modeling with selective

state spaces. Proc. COLM.

[13] Kuruppu, G., Wagh, N., Kremen, V., & Varatharajah, Y. (2026). EEG Foundation

Models: A Critical Review of Current Progress and Future Directions. Journal of Neural Engineering, 23, 021001. https://doi.org/10.1088/1741-2552/ae4455.

[14] Liu, D., Chen, Y., Chen, Z., Cui, Z., Wen, Y., An, J., Luo, J., & Wu, D.

(2026). EEG Foundation Models: Progresses, Benchmarking, and Open Problems. arXiv:2601.17883.

[15] Lee, N., Bakas, S., Barmpas, K., Panagakis, Y., Adamos, D. A., Laskaris, N., &

Zafeiriou, S. (2025). Assessing the Capabilities of Large Brainwave Foundation Models. 2025 IEEE 35th International Workshop on Machine Learning for Signal Processing (MLSP).

[16] Wang, X., Yang, Y., & Coyle, D. (2026). EEG-FM-Audit: A Systematic Evaluation

and Analysis Pipeline for EEG Foundation Models. arXiv:2605.26910.

[17] Xiong, W., Li, J., Li, J., & Zhu, K. (2025). EEG-FM-Bench: A Comprehensive Bench-

mark for the Systematic Evaluation of EEG Foundation Models. arXiv:2508.17742.

[18] Lu, Z., Li, Z., Shen, X., Lou, K., Xin, Y., Chen, X., Wang, S., Chen, X., Fan,

J., Huang, C., Xu, X., Hou, Z., Wei, C., & Liu, Q. (2026). OmniEEG-Bench: A Standardized Evaluation Benchmark for EEG Foundation Models. arXiv:2606.00815.

[19] ˇSirca, U., Alimardani, M., Zafeiriou, S., & Barmpas, K. (2026). Beyond Accu-

racy: Robustness, Interpretability and Expressiveness of EEG Foundation Models. arXiv:2605.17562.

31

<!-- page 32 -->

[20] Zare, M. (2026). Cross-Cohort Spectral–Temporal Dissociation in Frozen EEG

Foundation-Model Representations. arXiv preprint arXiv:2607.24834. https://doi. org/10.48550/arXiv.2607.24834.

[21] Chen, T., Kornblith, S., Norouzi, M., & Hinton, G. (2020). A simple framework for

contrastive learning of visual representations. Proc. ICML, pp. 1597–1607.

[22] Dao, T. & Gu, A. (2024). Transformers are SSMs: Generalized models and efficient

algorithms through structured state space duality. Proc. ICML.

[23] Gui, Y., Chen, M., Su, Y., Luo, G., & Yang, Y. (2024). EEGMamba: Bidirectional

State Space Model with Mixture of Experts for EEG Multi-task Classification. arXiv:2407.20254.

[24] Shoeb, A. H. (2009). Application of machine learning to epileptic seizure onset

detection and treatment. PhD thesis, MIT.

[25] Guttag, J. (2010). CHB-MIT Scalp EEG Database (version 1.0.0). PhysioNet. https:

//doi.org/10.13026/C2K01R.

[26] Obeid, I. & Picone, J. (2016). The Temple University Hospital EEG data corpus.

Frontiers in Neuroscience, 10, 196.

[27] L´opez de Diego, S. (2017). Automated interpretation of abnormal adult electroen-

cephalograms. M.S. thesis, Temple University.

[28] Miltiadous, A., et al. (2023). A dataset of scalp EEG recordings of Alzheimer’s disease,

frontotemporal dementia and healthy subjects from routine EEG. Data, 8(6), 95.

[29] Kemp, B., et al. (2000). Analysis of a sleep-dependent neuronal feedback loop. IEEE

Trans. Biomedical Engineering, 47(9), 1185–1194.

[30] Kim, M.-J., Youn, Y. C., & Paik, J. (2023). Deep learning-based EEG analysis to

classify normal, mild cognitive impairment, and dementia: Algorithms and dataset. NeuroImage, 272, 120054.

[31] Cavanagh, J. F. (2021). EEG: 3-Stim Auditory Oddball and Rest in Parkinson’s

Disease. OpenNeuro, dataset ds003490.

[32] Gramfort, A., et al. (2013). MEG and EEG data analysis with MNE-Python. Frontiers

in Neuroscience, 7, 267.

[33] Welch, P. (1967). The use of fast Fourier transform for the estimation of power

spectra. IEEE Trans. Audio and Electroacoustics, 15(2), 70–73.

[34] Hjorth, B. (1970). EEG analysis based on time domain properties. Electroencephalog-

raphy and Clinical Neurophysiology, 29(3), 306–310.

[35] Inouye, T., Shinosaki, K., Sakamoto, H., et al. (1991). Quantification of EEG

irregularity by use of the entropy of the power spectrum. Electroencephalography and Clinical Neurophysiology, 79(3), 204–210.

32

<!-- page 33 -->

[36] Richman, J. S. & Moorman, J. R. (2000). Physiological time-series analysis using

approximate entropy and sample entropy. American Journal of Physiology–Heart and Circulatory Physiology, 278(6), H2039–H2049.

[37] Peng, C.-K., Havlin, S., Stanley, H. E., & Goldberger, A. L. (1995). Quantification of

scaling exponents and crossover phenomena in nonstationary heartbeat time series. Chaos, 5(1), 82–87.

[38] Mallat, S. G. (1989). A theory for multiresolution signal decomposition: The wavelet

representation. IEEE Transactions on Pattern Analysis and Machine Intelligence, 11(7), 674–693.

[39] Hu, E. J., Shen, Y., Wallis, P., et al. (2022). LoRA: Low-Rank Adaptation of Large

Language Models. Proc. ICLR.

[40] Goldberger, A. L., et al. (2000). PhysioBank, PhysioToolkit, and PhysioNet. Circula-

tion, 101(23), e215–e220.

33