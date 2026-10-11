<!-- source: pdf/tao2026separating.pdf | converter: pymupdf -->

<!-- page 1 -->

# Separating personal from population gains when calibrating

# EEG foundation models for new users

## Xilin Tao1, Kani Chen1,2,*

## 1Department of Mathematics, The Hong Kong University of Science and Technology, Hong Kong SAR, China

2Department of Industrial Engineering and Decision Analytics, The Hong Kong University of Science and Technology, Hong Kong SAR, China

## *Correspondence: Kani Chen (makchen@ust.hk)

## Xilin Tao: xilin.tao@connect.ust.hk

## Abstract

Foundation models are increasingly adapted to individual users, but an apparent personalization gain can simply reflect a stronger population model. This distinction matters for brain–computer in- terfaces, where every new user must be calibrated. We evaluated personal adaptation of three frozen EEG foundation models (CBraMod, REVE and LaBraM) in 235 held-out subjects from three motor- imagery datasets, comparing each subject’s adapter with the population model and with adapters fitted to other subjects. Using all first-half session labels, personal adapters improved mean balanced accu- racy over the population model by 1.5–5.4 percentage points and outperformed exchanged adapters by 2.3–7.3 points in all nine model–dataset combinations. The size of this benefit depended on population training: with four times the original budget, median gains remained positive (1.0–2.0 points) but were smaller for every model, and no population model reached a confirmed plateau. Acquiring the ben- efit cheaply was unreliable: few-label calibration was consistently non-negative on only one dataset, and in CBraMod neither unlabeled context nor meta-learned initialization outperformed matched con- trols. Personalization should therefore be evaluated against both a population reference and exchanged parameters, across population-training budgets.

# 1 Introduction

Brain–computer interfaces must interpret neural signals from people whose recordings differ from those used to build the decoder. Calibration imposes a practical cost: collecting labeled trials from each new user delays use and requires sustained participation, motivating methods that reuse information across people or sessions [1]. EEG foundation models, including CBraMod, REVE and LaBraM, learn reusable representations from large recording collections [2–4]. Their value for a new user depends both on the population decoder and on the additional benefit obtained from that person’s data.

Personal adaptation can modify a small parameter set using feature-wise modulation, low-rank updates or a learned initialization [5–7]. EEG-specific approaches include shared and personal adapter branches, subject-specific encoders, and transfer from resting-state recordings [8–10]. Yet an apparent personal gain

## 1

# arXiv:2609.34801v1  [cs.LG]  28 Sep 2026

<!-- page 2 -->

can arise when the comparison model has a weaker head, less trainable capacity or less population train- ing. A shared adapter may improve predictions without information about the target; meta-training may improve the starting decoder before target labels are available. Final accuracy combines these population improvements with any contribution from personal fitting.

Two paired comparisons help distinguish these sources. Does personal fitting improve on a specified population decoder? Does the resulting adapter work better for its owner than an adapter fitted to another person? The first measures net benefit and the second measures personal specificity under the chosen donor procedure. Either alone is incomplete: an additional fit can transfer across people, and parame- ter exchange can damage predictions even when the owner’s adapter fails to improve on the population model. Benchmark comparisons with conventional decoders address another question: whether a foun- dation model is useful under a given training and evaluation protocol [11]. That question complements attribution of an adaptation gain to personal information.

The availability of a beneficial personal fit also differs from its inexpensive acquisition. Fitting all earlier labels characterizes achievable behavior within a fixed adapter family and optimization budget. Calibration with few labels, unlabeled context or meta-learning must recover that benefit with less tar- get information. We study these questions in same-session motor imagery, with subjects excluded from downstream population training and validation (Figure 1). Our results support four conclusions: personal fitting provides benefit and an owner-matching advantage across the tested model–dataset combinations; its magnitude depends on population training; few-label and tested unlabeled acquisition routes are unreli- able; and personalization should be reported jointly against a named population reference and exchanged parameters across training budgets.

EVALUATION SPLIT ATTRIBUTION CONTROLS TWO DISTINCT OUTCOMES

Source subjects

Train / validation only

Frozen EEG backbone + shared population model

Held-out subject

Earlier half: labels / context Later half: fixed query trials

Capacity control

Real / shuffled / default context

Information mismatch

Own / swapped parameters

Training-budget control

Population 1× / 2× / 4×

Meta-learning / continuation

Report both contrasts

Δ = own − population

U = own − swapped

U > 0 does not imply Δ > 0

Donor: another held-out subject in the same dataset and fold. Fit uses earlier-half labels.

Figure 1: Information boundaries and comparisons. Earlier target trials provide permitted labels or context; later query labels score predictions. Donor adapters are fitted using other held-out subjects’ earlier labels. The core contrasts measure net benefit over the population reference and the advantage of owner-matched parameters.

## 2

<!-- page 3 -->

# 2 Results

The core evaluation includes 235 held-out subjects from PhysioNet, Dreyer and Cho (Table 1). Balanced accuracy (BA) is scored on later query trials after calibration on earlier trials from the same session. Fig- ures show subject medians with bootstrap 95% confidence intervals after averaging seeds within subject; Table 2 gives the means used in the abstract, and Supplementary Section S1 provides mean versions of the figures.

Table 1: Analysis populations and CBraMod input/readout channels. EO denotes eyes-open rest. REVE and LaBraM use native-input pipelines on the core datasets; Lee and BNCI are CBraMod-only extensions. Fit/query counts are trials per subject in the temporal splits, including their ranges. Dataset sources are cited in Methods.

## Dataset N Session EEG / readout Fit / query trials Rest

PhysioNet 103 single 64 / 27 22 / 23 EO Dreyer 80 single 27 / 27 80–120 / 80–120 EO Cho 52 single 64 / 27 100–120 / 100–120 EO Lee 54 1 62 / 26 100 / 100 EO BNCI 9 2 22 / 19 72 / 72 EO

## 2.1 Personal adapters improve performance and favor their owners across models

Full-support personal fitting improves on the population decoder and favors the adapter’s owner across all nine model–dataset combinations. At the initial population-training budgets, personal LoRA improves mean BA over the population reference by 1.5–5.4 percentage points (pp) and outperforms exchanged adapters by 2.3–7.3 pp (Table 2); every corresponding median is also positive (Figure 2A–B).

The pattern also holds in the six combinations whose dataset is not listed among the model’s reported pretraining sources: CBraMod on PhysioNet, Dreyer and Cho; REVE on PhysioNet; and LaBraM on Dreyer and Cho. Population adaptation itself improves median BA over the task head in PhysioNet and Dreyer for all three models, with less consistent results in Cho (Figure 2C).

For LaBraM on Cho, mean own-minus-exchanged (4.78 pp) is smaller than mean own-minus- population (5.38 pp; Table 2); equation (3) gives a mean exchanged-minus-population estimate of 0.60 [-0.03, 1.24] pp. This positive estimate is consistent with a transferable component of personal fitting under the donor procedure, with an interval that includes zero.

The CBraMod extensions show why both contrasts matter. In Lee, personal FiLM has a mean matching advantage of 3.91 [2.17, 5.81] pp but a mean benefit over the population reference of -0.67 [-2.12, 0.84] pp. Lee LoRA’s mean benefit is 1.02 [-0.09, 2.16] pp. The BNCI exchange comparison has eight targets forming four donor pairs; its population comparison includes all nine subjects (Supplementary Sections S1 and S2).

## 3

<!-- page 4 -->

PhysioNet Dreyer Cho

0

2

4

6

Median difference (pp)

*

*

*

A  Personal benefit

PhysioNet Dreyer Cho

0

2

4

6

8

Median difference (pp)

*

*

*

B  Personal specificity

PhysioNet Dreyer Cho

−5

0

5

10

15

20

25

Median difference (pp)

*

*

*

C  Population gain

CBraMod REVE LaBraM

Figure 2: Cross-model attribution at the initial budgets. Points are medians of paired subject differences; bars are percentile subject-bootstrap 95% confidence intervals after averaging seeds. A: own minus population. B: own minus exchanged. C: population minus task head. Asterisks mark datasets listed in each model’s pretraining sources. Mean versions appear in Supplementary Section S1.

Table 2: Mean personal contrasts at the initial budgets, in pp, with subject-bootstrap 95% confidence intervals in brackets. Each subject contributes one seed-averaged paired difference. Sample sizes are 103, 80 and 52 for PhysioNet, Dreyer and Cho, respectively.

## Model Dataset Own - population Own - exchanged

CBraMod PhysioNet 1.64 [0.77, 2.51] 2.55 [1.74, 3.40] CBraMod Dreyer 3.58 [2.94, 4.24] 5.28 [4.64, 5.93] CBraMod Cho 5.13 [3.13, 7.46] 6.43 [4.34, 8.83] REVE PhysioNet 1.55 [0.91, 2.19] 2.59 [2.02, 3.19] REVE Dreyer 5.38 [4.38, 6.43] 7.25 [6.21, 8.33] REVE Cho 3.35 [2.26, 4.65] 4.38 [3.25, 5.70] LaBraM PhysioNet 1.52 [0.84, 2.24] 2.35 [1.64, 3.08] LaBraM Dreyer 3.91 [3.12, 4.76] 5.41 [4.63, 6.25] LaBraM Cho 5.38 [3.75, 7.20] 4.78 [3.21, 6.62]

## 2.2 Personal gains depend on population training and remain positive at the largest budget

Personal benefit depends on population-training budget: at four times the initial update budget, the pooled median own-minus-population gain is lower for every model (Figure 3).

REVE shows the largest observed reduction, with a paired-bootstrap change in medians of -1.42 [- 1.83, -0.68] pp from the initial to quadrupled budget; CBraMod and LaBraM change less and follow

## 4

<!-- page 5 -->

nonmonotonic paths. REVE’s smaller personal gain is not accompanied by a stronger population model: its population mean BA also falls from 81.13 [79.51, 82.70]% to 79.81 [78.32, 81.32]%. Dataset-specific trajectories can differ from the pooled direction (Supplementary Figure S13). At the largest budget, median gains remain between 1.0 and 2.0 pp, and matching advantages remain positive in all three models. No population model reaches a confirmed joint training/validation plateau (Supplementary Section S9).

1× 2× 4×

Population update budget

0

1

2

3

4

Median difference (pp)

CBraMod

1× 2× 4×

Population update budget

REVE

1× 2× 4×

Population update budget

LaBraM

Own - population Own - exchanged

Figure 3: Personal benefit and matching advantage across population-training budgets. Medians and subject- bootstrap 95% intervals use the same 235 subjects after seed averaging. Budgets are multiples of each run’s initially selected population-update count, and lines connect observed endpoints. Dataset-specific results and population scores appear in Supplementary Section S9.

## 2.3 Cheaper calibration recovers the benefit inconsistently

Reducing target-label requirements produces inconsistent gains across datasets: few-label calibration has nonnegative mean gains at every tested label budget for all three models only on PhysioNet. Calibration uses the earliest chronological label prefixes, which can contain only one class. Figure 4 shows medians, with means in Supplementary Section S1.

In CBraMod, the sole backbone tested for unlabeled context and meta-learning, true rest-conditioned FiLM and LoRA have median differences from shuffled context of 0.00 [0.00, 0.00] and 0.00 [0.00, 0.00] pp, respectively, and mean differences of -0.01 [-0.10, 0.09] and 0.01 [-0.11, 0.11] pp. True versus de- fault context also has zero median differences, but true context is slightly worse on average, with mean differences of -0.21 [-0.38, -0.04] and -0.23 [-0.48, -0.01] pp for FiLM and LoRA, respectively. Col- lapsed median intervals reflect the concentration of subject differences at zero. Selecting a single donor using rest or unlabeled task features also gives no dependable improvement over both random selection and the population reference (Figure 5); exploratory exceptions and multi-donor comparisons appear in Supplementary Section S2.

## Meta-learned initialization likewise shows no clear advantage over ordinary cross-entropy continuation

## 5

<!-- page 6 -->

5 10 20

Target labels (total)

−2

−1

0

1

2

3

Median own - population (pp)

PhysioNet

5 10 20 40

Target labels (total)

Dreyer

5 10 20 40

Target labels (total)

Cho

CBraMod REVE LaBraM

Figure 4: Few-label own-minus-population gains. Markers are subject medians; bars are subject-bootstrap 95% confidence intervals. Label counts are shown on equally spaced positions with small model offsets. Forty labels are available only for Dreyer and Cho. Lines join observed budgets. Mean versions appear in Supplementary Section S1.

FiLM LoRA

−0.4

−0.2

0.0

0.2

0.4

Median paired difference (pp)

A  Rest-conditioned adaptation

True - shuffled True - default

FiLM

rest

FiLM task

LoRA

rest

LoRA

task

−2

−1

0

1

Median paired difference (pp)

B  Single-donor selection

Nearest - random Nearest - population

Figure 5: Unlabeled context comparisons in CBraMod. A: paired true-minus-shuffled and true-minus-default con- trasts within the same-capacity contextual model. B: one-nearest-donor versus random-donor and population con- trols, using rest or unlabeled task features. Points are subject medians with subject-bootstrap 95% intervals.

## 6

<!-- page 7 -->

with the same scheduled outer-update budget and target calibration procedure. At ten labels, first-order MAML and the variant with learned inner rates have mean differences from continuation of -0.05 [-0.32, 0.21] and -0.08 [-0.34, 0.17] pp. Both median differences are zero, with intervals 0.00 [-0.20, 0.08] and 0.00 [-0.17, 0.08] pp. Figure 6 separates initial performance, final performance and calibration increments. The mean increment differences are 0.27 [-0.02, 0.56] and 0.19 [-0.10, 0.48] pp, providing no evidence of a reliable adaptation advantage under this procedure.

First-order

MAML

Learned inner rates

−0.3

−0.2

−0.1

0.0

0.1

0.2

0.3

0.4

Median difference from continuation (pp)

A  Before calibration

First-order

MAML

Learned inner rates

B  After ten labels

First-order

MAML

Learned inner rates

C  Calibration increment

Figure 6: CBraMod meta-learning versus ordinary continuation. Subject medians and subject-bootstrap 95% inter- vals compare first-order MAML and learned inner rates with ordinary continuation before calibration (A), after ten labels (B) and in calibration increments (C).

# 3 Discussion

Across the nine core model–dataset combinations, personal fitting improved on the population decoder and favored its owner, but the gain depended on population training and cheaper calibration did not recover it reliably. These findings motivate reporting both net personal benefit and owner-matching advantage against a named population reference across training budgets.

The two contrasts distinguish useful fitting from owner matching. A harmful donor exchange can create a matching advantage without improving on the population model, while a useful personal fit can transfer to other people. Jointly positive contrasts support useful owner matching under the donor proce- dure; its interpretation depends on donor support sizes, class balance and same-session recording condi- tions. This reasoning could guide evaluation in other settings combining foundation models with personal adaptation, although our evidence is limited to EEG.

Yang et al.’s ICLR 2026 benchmark compares foundation models with traditional decoders across tasks and evaluation protocols [11]. Lopes et al. report no accuracy advantage for personal encoders over a fine-tuned shared baseline when both use target labels [9, p. 20], addressing a different question from our comparison of a personal adapter with a population model fitted and selected without target information.

## 7

<!-- page 8 -->

Our contribution is to evaluate population-relative benefit and exchanged-adapter performance together across population-training budgets (Supplementary Section S3).

Training-budget curves make the population reference part of the result. Additional updates can change validation and query performance differently, so observed personal gains should be reported alongside population scores; their behavior beyond the tested budgets remains unresolved. Acquisition likewise depends on the procedure. Rest-based generative transfer, baseline correction and test-time training have reported benefits with other representations and update procedures [10, 12, 13], and ordinary transfer can compete with meta-learning in motor imagery [14, 15]. These comparisons motivate acquisition methods that distinguish the quality of an initial decoder from its adaptation increment.

The evidence is limited to binary motor imagery with within-session calibration, with a small BNCI cohort and a channel-restricted Lee readout. Differences in preprocessing, population adapters and pretraining-source overlap limit attribution of between-model differences to the backbone alone. Subject-bootstrap intervals are pointwise and conditional on selected checkpoints, omit dependence from shared population models and reused donors, and do not establish benefit for every user. The negative meta-learning result reflects one procedure with matched scheduled outer updates but additional inner- loop computation, subject to the failure handling in Supplementary Section S9.7, and does not establish equivalence.

## 8

<!-- page 9 -->

# 4 Methods

## 4.1 Evaluation unit and estimands

Let s be a target subject held out from downstream population training and validation. Within the same session, earlier task trials form a support set Ss and later trials form a query set Qs. Unlabeled context cs comprises eligible earlier rest or support-task features. A frozen backbone fθ is shared, with population parameters ϕ and target parameters as. Core population checkpoints and personal-fitting hyperparameters are selected without Qs labels. Supplementary Section S7 describes the query-informed prior controls, which use test-query information and are therefore excluded from the main comparisons. We measure balanced accuracy on Qs, averaging training seeds within subject before calculating group summaries.

## For a named population model P, define

## ∆s(P) = BA(Qs; P, as) −BA(Qs; P), (1)

## Us(P) = BA(Qs; P, as) −BA(Qs; P, ad(s)), (2)

where the swapped score averages the specified donor draws. ∆measures benefit over the population reference; U measures personal specificity against exchanged parameters. Their relationship is

## Us(P) = ∆s(P) −

## 

## BA(Qs; P, ad(s)) −BA(Qs; P)

## 

## . (3)

A harmful swap can make Us positive even when ∆s is negative. Full-support fitting characterizes attain- able performance within the tested parameterization and optimization budget.

Two CBraMod examples illustrate why both contrasts matter. Lee FiLM has positive specificity and meets the exchange criterion, yet its mean ∆is -0.67 pp. Conversely, one held-out Cho subject has mean population, own-adapter and exchanged-adapter BA of 54.00, 56.00 and 57.28%, respectively: ∆= 2.00 pp while U = −1.28 pp. Even when both means are positive, some gains may remain transferable across people.

## 4.2 Population-budget curves as part of attribution

For each prespecified population budget b, we report both medians ∆s(Pb) and medians Us(Pb) after av- eraging seeds within subject. The subjects, donor procedure and validation-selected personal-fitting grid are held constant across budgets. Population test performance and validation trajectories accompany these contrasts to show how reference quality changes with update count.

## 4.3 Three control families

Own-versus-population and own-versus-swapped LoRA diagnostics span all three backbones. Contextual capacity controls and ordinary-continuation sensitivity are restricted to CBraMod.

Capacity without personal information. The contextual models generate FiLM parameters or mixing weights over shared LoRA bases from a context representation. Real, shuffled and default-context con- ditions use the same trained model. Default context removes target-specific information while keeping

## 9

<!-- page 10 -->

shared learned capacity. The population reference continues contextual training and is scored with default context. Capacity is matched across context interventions; the task head and population model differ in capacity, and personal LoRA adds trainable parameters.

Information mismatch. Context is shuffled within dataset, while personal adapters are exchanged with other test subjects in the same dataset and fold. Donor labels fit the donor adapter; the target’s query set measures transfer. Nearest-neighbor diagnostics compare context-based selection with random donors under the same pool and transfer procedure, reporting both nearest-minus-random and nearest-minus- population. This analysis requires labeled donor support and a choice among eligible donors.

Additional population training. Ordinary continuation trains shared LoRA bases and the task head us- ing default mixture weights and cross-entropy. First-order MAML and its learned-rate variant use source- subject support/query episodes. Scheduled outer updates are matched, with additional inner-loop compu- tation and sample exposure for meta-learning. The primary population reference uses contextual training, so comparing it with ordinary continuation also changes the objective and selection procedure. Sensitivity comparisons across population references use the same subject-level paired mean statistic.

## 4.4 Decision rules and interpretation

Rules were fixed before each stage’s results in a successive-stage design, rather than a single independently preregistered study. Supplementary Section S10.1 defines the joint criteria and Holm correction families; Supplementary Data 1 reports all decisions, including unsuccessful and query-informed comparisons.

## 4.5 Data and evaluation populations

## 4.5.1 Signal processing and subject selection

The CBraMod pipeline resamples EEG to 200 Hz, applies a 0.3 Hz high-pass filter and dataset-specific mains notch, and average-references native EEG channels. Signals are expressed in microvolts divided by 100 and stored in half precision. Task windows are four seconds for PhysioNet, Dreyer and Lee, and three seconds for Cho; the BNCI configuration supplies its fixed window. Dataset-specific settings appear in the supplement. The data sources are PhysioNet EEGMMIDB [16, 17], Dreyer [18], Cho [19], Lee [20], and BCI Competition IV dataset 2a, distributed as BNCI2014-001 [21].

PhysioNet uses imagined left/right runs, excluding six subjects with sampling-rate or run-duration anomalies. Dreyer excludes seven subjects according to the original authors’ annotations, and all Cho subjects are included. Alpha-power checks are diagnostic only; the screening procedures are detailed in Supplementary Section S10.7.

Support/query allocation follows run and onset order, with trial counts and between-subject ranges in Table 1. Few-shot supports are chronological prefixes and may contain only one class. Budgets exceed- ing available support are treated as missing; query BA uses the two-class query set. Cho’s independent timeline-verification scope is described in Supplementary Section S10.7.

## 10

<!-- page 11 -->

Lee uses session one, ordered from offline/train to online/test trials, with the earliest pre-train eyes- open rest. Its 62-channel EEG enters the backbone, and a 26-channel readout intersection excludes the unavailable shared channel. Sensitivity to this readout-channel selection remains untested.

BNCI uses session two, left/right trials and task-preceding eyes-open rest, with expert-flagged trials included. Each subject has balanced support and query halves; the 19-channel readout uses 22 native EEG channels. The test partitions leave one subject without a donor and each remaining target with a unique eligible donor. Own-versus-population is thus estimable for all subjects and own-versus-swapped for the donor-eligible subset; nearest-donor selection is not identifiable.

## 4.5.2 Subject-disjoint folds

Table 3 gives the subject partitions. Core-cohort subjects share a population model across datasets. Lee and BNCI each train population models using the corresponding core-cohort fold/seed hyperparameters, with their own validation subjects selecting checkpoints under the same rule.

Table 3: Subject-disjoint partitions. The core cohort combines PhysioNet, Dreyer and Cho. Counts are people; seeds do not add independent subjects.

## Cohort Fold Train Validation Test

Core cohort 0 169 18 48 Core cohort 1 169 18 48 Core cohort 2 170 18 47 Core cohort 3 171 18 46 Core cohort 4 171 18 46 Lee 0 39 4 11 Lee 1 39 4 11 Lee 2 39 4 11 Lee 3 39 4 11 Lee 4 40 4 10 BNCI 0 6 1 2 BNCI 1 6 1 2 BNCI 2 6 1 2 BNCI 3 6 1 2 BNCI 4 7 1 1

## 4.5.3 Pretraining overlap

Reported pretraining sources list Dreyer, Cho and Lee for REVE, and PhysioNet for LaBraM; none of the evaluated motor-imagery datasets is listed for CBraMod. No core dataset is unlisted for all three models. These are source-list comparisons without record-level deduplication, so “unseen subject” denotes exclusion from downstream population training and validation [22, 23]. Source strata are marked in the figures and tables.

## 11

<!-- page 12 -->

## 4.6 CBraMod implementation and selection

CBraMod’s contextual model generates FiLM modulation or mixing weights over shared LoRA bases. Personal FiLM adds zero-initialized offsets; personal LoRA adds a zero-increment weight update while the shared parameters, head and backbone remain fixed. Training, parameterization and selection details appear in Supplementary Section S10.2 and Table S11.

For each target and training run, full-support exchange draws ten other subjects uniformly with re- placement from the same dataset and held-out fold. Draws use the run seed and can vary across seeds; all budget endpoints use the same donor list. Donor BA is averaged within run before averaging seeds within target. A singleton donor is repeated, and absent donors yield missing exchange results. Multi-donor LoRA transfer averages weight updates. Personal-fitting settings are selected on validation subjects.

Ordinary continuation and meta-learning start from the same population LoRA model. Continua- tion uses cross-entropy and default mixture weights; first-order MAML uses source-subject support/query episodes [7], and the learned-rate variant learns layer-specific inner rates. Evaluation uses the same full- batch SGD support updates and validation-selected inner settings. Numerical failure handling and event counts are detailed in Supplementary Sections S10.2 and S9.7.

## 4.7 REVE and LaBraM implementation

REVE and LaBraM use base pretrained encoders with fixed normalization and position parameters and native EEG-channel inputs [3, 4]. Shared attention LoRA and a task head are trained with cross-entropy. Personal fitting adds a separate zero-increment adapter while keeping the backbone, shared adapter and head fixed. FiLM, LoRA and the set encoder follow their respective method families [5, 6, 24].

Preprocessing, patch extraction, channel readout, normalization and candidate ordering are specified in Supplementary Section S10.3. No target-query normalization is used. Validation-subject scores select task-head and personal-fitting settings; mean cross-entropy selects population continuation checkpoints, including the initial checkpoint as a candidate. Only the selected population candidate is continued, restor- ing optimizer and random-number state.

## 4.8 Computational resources

GPU runs used RTX 3090 hardware. Supplementary Section S6 reports stage and run-level costs, counting shared training once and identifying incomplete exploratory accounting.

## 4.9 Statistical analysis and fixed decision rules

BA is the arithmetic mean of per-class recalls on the query set. For each contrast, we average seeds within subject, calculate paired differences, and resample subjects with replacement 20,000 times. The 2.5th and 97.5th percentiles of the bootstrap mean or median give pointwise 95% confidence intervals. These intervals are conditional on the selected fits and omit dependence from shared population models and reused donors, as well as model-selection and training-seed uncertainty; positive group summaries do not establish benefit for every subject. A fixed reporting seed makes resampling reproducible. The same sampled subject indices are used at both budget endpoints to estimate the difference of medians. Pooled

## 12

<!-- page 13 -->

resampling draws from the full cohort without fixing dataset counts. Means and medians are reported separately; SDs and interquartile ranges describe between-subject heterogeneity.

Personal-specificity, contextual, neighbor and meta-learning tests use directional paired Wilcoxon pro- cedures with the normal approximation, dropping zero differences and assigning a unit p-value when all differences vanish. Holm correction applies within each specified family. Alignment comparisons use their two-sided procedures and correction families. The CBraMod alignment diagnostics whiten native EEG before the encoder; implementation and results appear in Supplementary Sections S10.5 and S2.1. Supplementary Data 1 provides test directions, raw and corrected p-values, sample sizes and decisions. These analyses test directional differences; they do not test equivalence.

Supplementary Section S10.4 specifies correction slots, eligibility criteria and descriptive consistency rules. Few-shot stability requires nonnegative means at every prescribed budget and no decreases with increasing budget. Missing budgets and absent donors remain missing. BNCI’s two contrasts use their respective eligible populations. Sensitivity comparisons across population references use paired means on the same eligible subjects; median-based decision criteria are reported separately. At the subject level, the final meta-learning contrast equals the initial contrast plus the calibration-increment contrast; means preserve this identity, whereas the medians in Figure 6 summarize each contrast separately.

## 4.10 Population-training budget extension

Each run’s initially selected population-update count defines its reference budget. Continuation uses the same objective, learning rate and sampling procedure, with endpoints at twice and four times that count and no intermediate checkpoint selection. REVE and LaBraM restore optimizer and random-number states; CBraMod restarts them because its starting checkpoint lacks those states. Nonfinite objectives stop a run; validation deterioration does not trigger checkpoint substitution.

At each new endpoint, personal LoRA settings are reselected on validation subjects using the same grid and donors; the reference endpoint uses its initial fit. Endpoint evaluation and differences from the initial core scores are detailed in Supplementary Section S9. Few-shot results use the initial population-training budget only. Complete-cohort contrasts require every subject and seed. The CBraMod curve combines 24 trajectories with one precision-adjusted rerun, whose implementation and prior failure are detailed in Supplementary Section S10.6.

The joint stopping criterion combines training/validation loss ranges and validation-score stability. Supplementary Section S10.6 gives its thresholds, attenuation and stable-positive-gain rules, and correc- tion slots.

## 4.11 Ethics statement

This study used only publicly available EEG datasets. Ethical approval and participant consent for the original data collection were the responsibility of the original investigators, as documented in the source studies. No new participant data were collected for this study.

## 13

<!-- page 14 -->

## 4.12 AI use declaration

The authors used Anthropic’s Claude to discuss study design, analysis planning, literature-search planning and critique of the manuscript. OpenAI Codex was used to implement and execute the analysis code, organize evidence, generate figures, and draft and revise the manuscript text. All experiments were run with code executed on the authors’ computing resources, and all reported numbers are generated from saved results by scripts included in the code release. X.T. reviewed the analyses and verified the reported results; all authors approved the manuscript and take responsibility for its content.

# Data availability

The original EEG recordings are available from PhysioNet’s EEG Motor Movement/Imagery Dataset (https://physionet.org/content/eegmmidb/1.0.0/), the Dreyer motor-imagery database (https://zenodo.org/ records/8089820; analysis distribution: https://osf.io/8tdk5/), GigaDB for Cho (https://gigadb.org/dataset/ 100295) and Lee (https://gigadb.org/dataset/100542), and BNCI2014-001 (https://bnci-horizon-2020.eu/ database/data-sets). Access and reuse are subject to the source repositories’ terms. Supplementary Data 1 contains all 904 comparison records and their column and correction-family definitions. Saved subject- level results, split definitions and numerical provenance records accompany the analysis-code release. Original EEG recordings and pretrained model weights are obtained separately from their source reposi- tories. Source data are provided with this paper.

# Code availability

The original analysis code, fixed configurations, dependency specifications, reporting scripts and saved results are publicly available at https://github.com/gaivrt/eeg-personal-population-benefit, version 1.0.0 (commit 06fc75f). The reporting scripts regenerate the summaries and figures from saved results with- out training or model inference. The original analysis software is released under the MIT license; derived tables and documentation use CC BY 4.0, and third-party materials retain their original terms. The ver- sion 1.0.0 archive (assigned DOI: 10.5281/zenodo.22999685) is available at https://zenodo.org/records/ 22999685.

# References

## [1] Matthias Krauledat, Michael Tangermann, Benjamin Blankertz, and Klaus-Robert Müller. Towards

Zero Training for Brain-Computer Interfacing. PLoS ONE, 3(8):e2967, 2008. doi: 10.1371/journal. pone.0002967. URL https://doi.org/10.1371/journal.pone.0002967.

## [2] Jiquan Wang, Sha Zhao, Zhiling Luo, Yangxuan Zhou, Haiteng Jiang, Shijian Li, Tao Li, and Gang

Pan. CBraMod: A Criss-Cross Brain Foundation Model for EEG Decoding. In International Con- ference on Learning Representations, 2025. URL https://proceedings.iclr.cc/paper_files/paper/2025/ hash/bbbd6d915cb90be21c1254a82d45cedd-Abstract-Conference.html.

## 14

<!-- page 15 -->

## [3] Yassine El Ouahidi, Jonathan Lys, Philipp Thölke, Nicolas Farrugia, Bastien Pasdeloup, Vincent

Gripon, Karim Jerbi, and Giulia Lioi. REVE: A Foundation Model for EEG – Adapting to Any Setup with Large-Scale Pretraining on 25,000 Subjects, 2025. URL https://arxiv.org/abs/2510.21585v1.

[4] Wei-Bang Jiang, Li-Ming Zhao, and Bao-Liang Lu. Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI. In International Conference on Learning Representations, 2024. URL https://proceedings.iclr.cc/paper_files/paper/2024/hash/ 47393e8594c82ce8fd83adc672cf9872-Abstract-Conference.html.

## [5] Ethan Perez, Florian Strub, Harm De Vries, Vincent Dumoulin, and Aaron Courville. FiLM: Visual

Reasoning with a General Conditioning Layer. Proceedings of the AAAI Conference on Artificial Intelligence, 32(1), 2018. doi: 10.1609/aaai.v32i1.11671. URL https://doi.org/10.1609/aaai.v32i1. 11671.

## [6] Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang,

and Weizhu Chen. LoRA: Low-Rank Adaptation of Large Language Models. In International Conference on Learning Representations, 2022. URL https://arxiv.org/abs/2106.09685.

## [7] Chelsea Finn, Pieter Abbeel, and Sergey Levine. Model-Agnostic Meta-Learning for Fast Adaptation

of Deep Networks. In Proceedings of the 34th International Conference on Machine Learning, 2017. URL https://proceedings.mlr.press/v70/finn17a.html.

## [8] Aymen Sarhane, Fouad Lbakali, Mouad Souissi, Jonathan Lys, and Giulia Lioi. Stacked LoRA for

## Subject-Adaptive EEG Foundation Models in Motor Imagery Decoding, 2026. URL https://arxiv. org/abs/2607.03094v1.

## [9] Bruna J. Lopes, Gabriel Schwartz, Sylvain Chevallier, Raphael Y. de Camargo, and Bruno Aris-

timunha. Learning aligned EEG representations with subject-specific encoders. Scientific Reports, 2026. doi: 10.1038/s41598-026-69220-z. URL https://doi.org/10.1038/s41598-026-69220-z. Arti- cle in Press; accepted 26 August 2026.

## [10] Sion An, Myeongkyun Kang, Soopil Kim, Philip Chikontwe, Li Shen, and Sang Hyun Park. Subject-

Adaptive Transfer Learning Using Resting State EEG Signals for Cross-Subject EEG Motor Imagery Classification, 2024. URL https://arxiv.org/abs/2405.19346v2.

## [11] Liuyin Yang, Qiang Sun, Ang Li, and Marc M. Van Hulle. Are EEG Foundation Models Worth It?

Comparative Evaluation with Traditional Decoders in Diverse BCI Tasks. In International Confer- ence on Learning Representations, 2026. URL https://openreview.net/forum?id=5Xwm8e6vbh.

## [12] Youngchul Kwak, Kyeongbo Kong, Woo-Jin Song, and Seong-Eun Kim. Subject-Invariant Deep

Neural Networks Based on Baseline Correction for EEG Motor Imagery BCI, 2023. URL https: //doi.org/10.1109/JBHI.2023.3238421.

## [13] Suli Wang, Yangshen Deng, Zhenghua Bao, Xinyu Zhan, and Yiqun Duan. NeuroTTT: Bridging

Pretraining-Downstream Task Misalignment in EEG Foundation Models via Test-Time Training, 2025. URL https://arxiv.org/abs/2509.26301v2.

## 15

<!-- page 16 -->

## [14] Anupam Sharma and Krishna Miyapuram. Evaluating Fast Adaptability of Neural Networks for

## Brain-Computer Interface, 2024. URL https://arxiv.org/abs/2404.15350v1.

[15] Daniil A. Berdyshev, Artem M. Grachev, Sergei L. Shishkin, and Bogdan L. Kozyrskiy. EEG- Reptile: An Automatized Reptile-Based Meta-Learning Library for BCIs, 2025. URL https://arxiv. org/abs/2412.19725v2.

## [16] Gerwin Schalk. EEG Motor Movement/Imagery Dataset, 2009. URL https://physionet.org/content/

## eegmmidb/1.0.0/. PhysioNet, version 1.0.0.

## [17] G. Schalk, D.J. McFarland, T. Hinterberger, N. Birbaumer, and J.R. Wolpaw. BCI2000: A General-

Purpose Brain-Computer Interface (BCI) System. IEEE Transactions on Biomedical Engineering, 51(6):1034–1043, 2004. doi: 10.1109/tbme.2004.827072. URL https://doi.org/10.1109/tbme.2004. 827072.

[18] Pauline Dreyer, Aline Roc, Léa Pillette, Sébastien Rimbert, and Fabien Lotte. A large EEG database with users’ profile information for motor imagery brain-computer interface research. Sci- entific Data, 10(1):580, 2023. doi: 10.1038/s41597-023-02445-z. URL https://doi.org/10.1038/ s41597-023-02445-z.

## [19] Hohyun Cho, Minkyu Ahn, Sangtae Ahn, Moonyoung Kwon, and Sung Chan Jun. EEG datasets for

motor imagery brain–computer interface. GigaScience, 6(7):gix034, 2017. doi: 10.1093/gigascience/ gix034. URL https://doi.org/10.1093/gigascience/gix034.

## [20] Min-Ho Lee, O-Yeon Kwon, Yong-Jeong Kim, Hong-Kyung Kim, Young-Eun Lee, John

Williamson, Siamac Fazli, and Seong-Whan Lee. EEG dataset and OpenBMI toolbox for three BCI paradigms: an investigation into BCI illiteracy. GigaScience, 8(5):giz002, 2019. doi: 10.1093/gigascience/giz002. URL https://doi.org/10.1093/gigascience/giz002.

## [21] Michael Tangermann, Klaus-Robert Müller, Ad Aertsen, Niels Birbaumer, Christoph Braun,

Clemens Brunner, Robert Leeb, Carsten Mehring, Kai J. Miller, Gernot R. Müller-Putz, Guido Nolte, Gert Pfurtscheller, Hubert Preissl, Gerwin Schalk, Alois Schlögl, Carmen Vidaurre, Stephan Waldert, and Benjamin Blankertz. Review of the BCI Competition IV. Frontiers in Neuroscience, 6, 2012. doi: 10.3389/fnins.2012.00055. URL https://doi.org/10.3389/fnins.2012.00055.

## [22] Jun-You Lin, Ying Choon Wu, and Tzyy-Ping Jung. The Identity Trap in EEG Foundation Models:

## A Diagnostic Audit, 2026. URL https://arxiv.org/abs/2606.06647v1.

## [23] Dingkun Liu, Yuheng Chen, Zhu Chen, Zhenyao Cui, Yaozhi Wen, Jiayu An, Jingwei Luo, and Don-

grui Wu. EEG-FM-Compass: Progress, Benchmarking, and Future Directions for EEG Foundation Models, 2026. URL https://arxiv.org/abs/2601.17883v3.

## [24] Manzil Zaheer, Satwik Kottur, Siamak Ravanbakhsh, Barnabas Poczos, Ruslan Salakhutdinov, and

Alexander J. Smola. Deep Sets. In Advances in Neural Information Processing Systems, 2017. URL https://papers.nips.cc/paper/2017/hash/f22e4747da1aa27e363d86d40ff442fe-Abstract.html.

## 16

<!-- page 17 -->

# Acknowledgements

## The authors thank the original dataset investigators for making their EEG recordings publicly available.

# Funding

Computational resources and access to AI tools were provided through Kani Chen’s research group at The Hong Kong University of Science and Technology.

# Author contributions

X.T. designed the study and methodology, developed the software, curated the data, performed the ex- periments and analyses, validated the results, prepared the visualizations, and drafted and revised the manuscript. K.C. provided guidance on the overall research direction, supervision and computational resources.

# Competing interests

## The authors declare no competing interests.

## 17

<!-- page 18 -->

# Supplementary information Separating personal from population gains when calibrating EEG

# foundation models for new users

## Xilin Tao1, Kani Chen1,2,*

1Department of Mathematics, The Hong Kong University of Science and Technology, Hong Kong SAR, China

2Department of Industrial Engineering and Decision Analytics, The Hong Kong University of Science and Technology, Hong Kong SAR, China

*Correspondence: Kani Chen (makchen@ust.hk) Xilin Tao: xilin.tao@connect.ust.hk

## S0 Notation

Table S1 defines mathematical symbols, condition labels, parameter names and record identifiers used in the article, supplement and Supplementary Data 1. Codes in source-record identifiers are retained for traceability; their components use the definitions below. Comparisons are left minus right unless a row states otherwise. Column definitions, units, test directions and correction- family membership accompany Supplementary Data 1.

Table S1: Notation and identifier key. Capitalization distinguishes model families, scored conditions and experiment stages.

Code Meaning

Quantities BA; accuracy Balanced accuracy; unbalanced classification accuracy. BA is the mean class recall. Absolute scores are percentages; score contrasts use percentage points (pp). Delta; U Own-minus-population benefit; own-minus-exchanged personal specificity, respectively, de- fined in Methods 4.1. s; d(s); S_s; Q_s; c_s Target subject; assigned donor; earlier labeled support; later query set; eligible unlabeled context. P; P_b; b Named population reference; reference at population-training budget b; original, doubled or quadrupled update budget. f_theta; phi; a_s; a_d(s) Frozen backbone; population parameters; target personal parameters; donor personal parame- ters. N; n; SD; CI; CE Subject count; count or label budget as specified; between-subject standard deviation; confi- dence interval; cross-entropy loss. p; p_H; pH; p_raw; p_adjusted Raw p-value; saved Holm-adjusted p-value (p_H and pH); raw and adjusted data columns. Missing adjusted values are not zero. own; swapped; exchanged Target adapter on its owner; adapters fitted to other subjects and evaluated on that target. Swapped and exchanged are synonyms. own_gain; upper_bound Saved names for own-minus-population and own-minus-swapped contrasts. The latter name does not imply a mathematical upper bound. nearest_gain; random_gain; differ- ence

Nearest-donor minus population; random-donor minus population; nearest minus random.

ba; adapt_gain In a comparison measure field: final balanced accuracy; improvement from zero labels to the specified label budget. NA; n.a.; blank; – Unavailable or inapplicable result. None is an observed zero or a negative test. Conditions B0; B0_linear; B0_mlp Task head on frozen features; the suffix selects a linear or multilayer-perceptron head. B1; B1a B1 is the superseded initial alignment reference. B1a uses all available task/rest data for source-training covariance and eyes-open rest for validation/test covariance.

18

<!-- page 19 -->

Code Meaning

B1b Euclidean alignment using all unlabeled target task trials for test covariance; transductive because query inputs are included. B1c Euclidean alignment using only each subject’s eyes-open rest for training, validation and test covariance. B2; B2_T3A; T3A As a condition, B2 denotes the rest-supported test-time classifier adjustment (B2_T3A). As a stage identifier, B2 instead denotes the full-forward personal-adapter experiment below. B3; B3_film; B3_lora Default-context prediction by the trained contextual model; same learned capacity without target-specific context. Suffix specifies the parameter family. B4; B4_film; B4_lora Shuffled-context control of the corresponding contextual model; a same-dataset donor supplies context. B5; B5_n10; B5_n20; B5_n40; B5_ n80

Personal all-layer FiLM fitted to the earliest n labeled support trials. The n suffix is the total target-label count. B6; B6_film_all; B6_film_first2; B6_ lora4; B6_lora8

Full-earlier-half supervised personal-adapter references imported from the full-forward exper- iment; suffix gives the adapter variant. G; G_film_offset; G_lora8 Continued population reference; suffixed names identify the corresponding FiLM or LoRA population family. R0; R1; R2; R2* Initial population LoRA; random-prior control with test-query-informed validation selection; ordinary cross-entropy continuation. R2* flags use of the LoRA population reference for FiLM sensitivity. M1; M2 First-order MAML initialization; meta-learned initialization with learned layer-specific inner rates. P0; P1; P2 Population reference; random-donor parameter prior; feature-selected donor prior. These prior diagnostics can use other donors’ query labels. Parameters m_film; m_lora Lowercase model-family identifiers: context-generated FiLM and a context-weighted mixture of shared LoRA bases. They do not denote meta-learning methods. M_film; M_lora Uppercase prediction-condition identifiers: the FiLM or LoRA contextual model using the target’s real context. M alone is the meta-learning stage. M_film_lambda0; M_lora_lambda0 Corresponding real-context model trained with zero weight on the context-mismatch objec- tive. film_offset An additive personal FiLM offset on the selected default-context population model. The ordinary-continuation sensitivity can place FiLM on a LoRA population model. mix_offset Personal additive offsets to the mixture weights of shared LoRA bases. Unexecuted slots in later correction families remain unavailable. film2; film4; beta4 FiLM on the last two or last four encoder layers; shift-only adaptation on the last four layers, in the cached-feature experiment. film_first2; film_all FiLM on the first two or all encoder layers in the full-forward personal-adapter experiment. lora4; lora8 Personal attention LoRA with rank four or eight. Model-family and starting-reference fields distinguish the source experiment. head; linear; mlp; scratch_head Head-only tuning; linear classifier; multilayer perceptron; randomly reinitialized head fitted with personal support labels. selected_film FiLM variant selected on validation subjects from the candidates of that source experiment. film; FILM; lora; LORA Display aliases for FiLM and LoRA parameter families. Stages A; B; B2 Frozen-feature/alignment baselines; cached-feature personal adaptation; full-forward personal adaptation. Stage B2 is distinct from condition B2_T3A. C; C-all Contextual-generator comparisons on later query trials; compatibility summaries on all trials, respectively. C2; C3; C3-few; C4 Personal-parameter exchange and rest-neighbor diagnostics; rest/task neighbor comparison; few-label adaptation from default context; fixed donor-prior calibration. M; W; X; X1 Meta-learning comparisons; population-continuation and personal-specificity comparisons; REVE/LaBraM extension. X1 denotes its core original-budget comparisons. W-pooled; WF; WF-BNCI Pooled neighbor summaries; follow-up population-reference/BNCI analyses; BNCI popula- tion controls. WF-R2-own_minus_population; WF- R2-own_minus_swap

Ordinary-continuation reference sensitivity: own-minus-population or own-minus-swapped contrast. WF-few; WF-own BNCI few-label and full-support own-minus-population summaries. Identifiers

19

<!-- page 20 -->

Code Meaning

T0001–T0904 Stable comparison-row identifiers in Supplementary Data 1; each appears once. Rows from overlapping cohorts are not independent replications. H01–H12; none Documentation keys for the original Holm correction families in Supplementary Data 1. The Families sheet lists their members; none means no adjusted value is supplied in that row. E01–E13; N01–N14 Engineering/data checks; unexecuted, unavailable or superseded items. Each item is described in the corresponding titled table in S4. D1; D2; D3; diagnostic1; diagnostic2; diagnostic2_3

Owner-versus-exchanged specificity; rest-neighbor selection; task-neighbor selection; corre- sponding source diagnostic names. B-G; B2-*; C-*; C2-D1-*; C2-D2-*; C3-D3-*; C4-main; C4-secondary-*; M-main-*; M-secondary-*; W-*

Composite decision identifiers: stage, endpoint, parameter family and optional dataset/budget. A suffix retains the definitions in this table; each complete decision row states its rule.

R2_sensitivity_diagnostic1; BNCI_ diagnostic1_available_subset

Owner/exchanged sensitivity against ordinary continuation; BNCI specificity among subjects with an available donor. Fields variant; method; condition; control; versus

Personal parameterization; model/method identifier; scored condition; named comparator. The hypothesis defines subtraction order. start; population_family; source; k; shots; comparison; measure

Starting reference; population parameter family; rest/task donor-selection context (inside con- dition strings); number of donors; total labeled support trials; ordered contrast; score or calibration-increment measure. rest; task; P1-P0; P2-P0; P2-P1; M1- R0; M1-R1; M1-R2; M2-R0; M2-R1; M2-R2; M2-M1

Resting or unlabeled support-task context; hyphenated comparison expressions mean left mi- nus right, using the conditions defined above.

Execution fold; seed; selected; run; initial; extra Cross-validation fold; repeated initialization; selected checkpoint updates; executed updates; starting-fit updates; additional continuation updates. These counts do not increase the number of subjects. CE_patience; step_budget; plateau Early stop after the validation cross-entropy patience interval; update cap; joint train- ing/validation plateau condition. B3_continued_original_objective Saved configuration name for ordinary cross-entropy continuation with default mixture weights, not the context-mismatch objective used for population continuation. P0/P1/P2; 1x/2x/4x Slashes list separate prior conditions; x denotes the multiplier of the original population- update budget. Datasets PhysioNet; PhysionetMI; Dreyer; Dreyer2023; Cho; Cho2017; Cho2017MI

Display and saved identifiers for the three core motor-imagery datasets.

Lee; Lee2019_MI; BNCI; BNCI2014_001; BNCI2014.001

Display and saved identifiers for the two external datasets.

pooled; starter; Dreyer+Cho All available subjects in the stated core comparison; alias for the initial core cohort; pooled Dreyer and Cho subset. Row-specific N defines the denominator. Abbreviations EEG; BCI; MI; EA; LOSO Electroencephalography; brain-computer interface; motor imagery; Euclidean alignment; leave-one-subject-out evaluation. FiLM; LoRA; MAML; MLP; SGD; GPU

Feature-wise linear modulation; low-rank adaptation; model-agnostic meta-learning; multi- layer perceptron; stochastic gradient descent; graphics processing unit. CBraMod; REVE; LaBraM The three pretrained EEG backbones evaluated; original model references are provided in the main manuscript. q/k/v/o; Q/K/V/O; Hz; s; pp Query/key/value/output attention projections; hertz; seconds when used as a time unit; per- centage points.

20

<!-- page 21 -->

## S1 Subject-bootstrap uncertainty and mean figures

All comparisons in this section use existing predictions or their saved subject scores. Seeds are averaged within subject before

calculation of paired contrasts. For each contrast we draw 20,000 bootstrap samples of subjects with replacement, retaining

paired observations, and use the 2.5th and 97.5th percentiles. The original sample size is retained in each resample. Pooled

results resample the empirical subject mixture; per-dataset results resample that dataset alone. Budget changes resample the

same subjects at both endpoints and subtract their two sample medians. This differs from the median of paired changes.

These are pointwise intervals conditional on the recorded model fits and donor assignments. They do not account for shared-

model dependence, reused donors, hyperparameter selection or training-seed uncertainty. They are not a new multiplicity-

adjusted test family and do not alter original decisions. Some median intervals collapse at zero because many subjects have

identical scores between conditions. The mean intervals and original distribution tables retain information about nonzero subject

differences.

PhysioNet Dreyer Cho

0

2

4

6

8

Mean difference (pp)

*

*

*

A  Personal benefit

PhysioNet Dreyer Cho −2

0

2

4

6

8

10

Mean difference (pp)

*

*

*

B  Personal specificity

PhysioNet Dreyer Cho

−5

0

5

10

15

20

25

Mean difference (pp)

*

*

*

C  Population gain

CBraMod REVE LaBraM

Figure S1: Mean version of main Figure 2, with subject-bootstrap 95% intervals. Asterisks identify listed pretraining sources.

21

<!-- page 22 -->

1× 2× 4×

Population update budget

0

1

2

3

4

5

Mean difference (pp)

CBraMod

1× 2× 4×

Population update budget

REVE

1× 2× 4×

Population update budget

LaBraM

Own - population Own - exchanged

Figure S2: Mean version of main Figure 3, using the same paired contrasts, subjects and budget endpoints.

5 10 20

Target labels (total)

−2

0

2

4

Mean own - population (pp)

PhysioNet

5 10 20 40

Target labels (total)

Dreyer

5 10 20 40

Target labels (total)

Cho

CBraMod REVE LaBraM

Figure S3: Mean version of main Figure 4. Only PhysioNet has nonnegative means at every available budget for all models. The nonnegative- and-nondecreasing criterion uses means.

22

<!-- page 23 -->

FiLM LoRA

−0.4

−0.2

0.0

Mean paired difference (pp)

A  Rest-conditioned adaptation

True - shuffled True - default

FiLM

rest

FiLM task

LoRA

rest

LoRA

task

−3

−2

−1

0

1

Mean paired difference (pp)

B  Single-donor selection

Nearest - random Nearest - population

Figure S4: Mean version of main Figure 5. Each interval is for a within-subject difference.

First-order

MAML

Learned inner rates

−0.6

−0.4

−0.2

0.0

0.2

0.4

0.6

Mean difference from continuation (pp)

A  Before calibration

First-order

MAML

Learned inner rates

B  After ten labels

First-order

MAML

Learned inner rates

C  Calibration increment

Figure S5: Mean version of main Figure 6. Final differences equal initial differences plus differences in calibration increments. Unlike the medians, the means obey this additive identity.

23

<!-- page 24 -->

## S1.1 Complete intervals for the main comparisons

All values are percentage points; population BA rows are percentages. Mean and median bootstrap intervals use the same subject draws within each contrast. A budget-change row is the 4× statistic minus the 1× statistic. FILM/LORA denote the FiLM/LoRA families; nearest_gain, random_gain and difference denote nearest minus population, random minus population and nearest minus random, respectively.

Table S2: Subject-bootstrap intervals for all main-text comparisons. Population balanced accuracy is in percent; paired differences are in percentage points.

Model Dataset Contrast / condition N Median [95% CI] Mean [95% CI]

CBraMod PhysioNet Personal benefit 103 0.98 [0.08, 2.42] 1.64 [0.77, 2.51] CBraMod PhysioNet Personal specificity 103 1.87 [1.51, 2.61] 2.55 [1.74, 3.40] CBraMod PhysioNet Population gain 103 7.77 [6.82, 10.08] 9.14 [7.54, 10.78] CBraMod Dreyer Personal benefit 80 3.29 [2.67, 3.83] 3.58 [2.94, 4.24] CBraMod Dreyer Personal specificity 80 4.89 [4.17, 5.95] 5.28 [4.64, 5.93] CBraMod Dreyer Population gain 80 9.08 [7.33, 10.00] 9.18 [8.23, 10.15] CBraMod Cho Personal benefit 52 3.50 [1.80, 4.80] 5.13 [3.13, 7.46] CBraMod Cho Personal specificity 52 4.30 [1.90, 6.72] 6.43 [4.34, 8.83] CBraMod Cho Population gain 52 -0.08 [-1.17, 0.80] -0.06 [-1.22, 1.12] REVE PhysioNet Personal benefit 103 0.98 [0.30, 1.67] 1.55 [0.91, 2.19] REVE PhysioNet Personal specificity 103 2.39 [1.52, 2.75] 2.59 [2.02, 3.19] REVE PhysioNet Population gain 103 13.38 [10.30, 15.00] 13.92 [12.03, 15.82] REVE Dreyer Personal benefit 80 4.67 [3.17, 5.83] 5.38 [4.38, 6.43] REVE Dreyer Personal specificity 80 6.78 [5.67, 7.58] 7.25 [6.21, 8.33] REVE Dreyer Population gain 80 8.83 [6.67, 11.83] 8.98 [7.19, 10.76] REVE Cho Personal benefit 52 2.60 [1.20, 3.40] 3.35 [2.26, 4.65] REVE Cho Personal specificity 52 3.48 [2.38, 4.39] 4.38 [3.25, 5.70] REVE Cho Population gain 52 1.63 [0.60, 3.00] 2.48 [1.36, 3.61] LaBraM PhysioNet Personal benefit 103 0.91 [0.45, 1.82] 1.52 [0.84, 2.24] LaBraM PhysioNet Personal specificity 103 2.09 [1.27, 2.77] 2.35 [1.64, 3.08] LaBraM PhysioNet Population gain 103 20.38 [17.12, 22.65] 20.21 [17.90, 22.54] LaBraM Dreyer Personal benefit 80 3.00 [2.58, 4.00] 3.91 [3.12, 4.76] LaBraM Dreyer Personal specificity 80 4.32 [3.70, 5.24] 5.41 [4.63, 6.25] LaBraM Dreyer Population gain 80 9.67 [7.67, 10.50] 9.31 [8.10, 10.56] LaBraM Cho Personal benefit 52 3.38 [2.40, 4.30] 5.38 [3.75, 7.20] LaBraM Cho Personal specificity 52 2.95 [2.04, 4.26] 4.78 [3.21, 6.62] LaBraM Cho Population gain 52 0.60 [-0.20, 1.70] 1.74 [0.33, 3.33] LaBraM Cho Exchanged minus population 52 0.44 [-0.22, 0.94] 0.60 [-0.03, 1.24] CBraMod Pooled 1x Personal benefit 235 2.60 [2.00, 3.33] 3.07 [2.41, 3.78] CBraMod Pooled 1x Personal specificity 235 3.53 [2.88, 4.33] 4.34 [3.68, 5.07] CBraMod Pooled 1x Population BA 235 79.09 [76.97, 80.85] 77.06 [75.33, 78.77] CBraMod Pooled 2x Personal benefit 235 1.60 [1.31, 2.23] 2.48 [1.76, 3.24] CBraMod Pooled 2x Personal specificity 235 3.40 [2.92, 4.36] 4.03 [3.36, 4.76] CBraMod Pooled 2x Population BA 235 80.33 [78.03, 82.50] 77.98 [76.24, 79.69] CBraMod Pooled 4x Personal benefit 235 2.00 [1.33, 2.35] 2.33 [1.70, 3.00] CBraMod Pooled 4x Personal specificity 235 3.23 [2.74, 3.82] 3.74 [3.13, 4.40] CBraMod Pooled 4x Population BA 235 80.50 [78.20, 82.05] 78.25 [76.60, 79.88] CBraMod Pooled 4x minus 1x 235 -0.60 [-1.33, 0.00] -0.74 [-1.20, -0.29] REVE Pooled 1x Personal benefit 235 2.42 [1.67, 2.95] 3.25 [2.70, 3.82] REVE Pooled 1x Personal specificity 235 3.50 [3.07, 4.06] 4.58 [4.01, 5.16] REVE Pooled 1x Population BA 235 82.00 [79.80, 84.80] 81.13 [79.51, 82.70] REVE Pooled 2x Personal benefit 235 1.83 [1.50, 2.40] 2.80 [2.26, 3.35] REVE Pooled 2x Personal specificity 235 3.10 [2.42, 3.85] 4.12 [3.54, 4.72] REVE Pooled 2x Population BA 235 84.17 [81.89, 85.23] 81.80 [80.20, 83.37] REVE Pooled 4x Personal benefit 235 1.00 [0.80, 1.50] 1.68 [1.22, 2.17] REVE Pooled 4x Personal specificity 235 2.24 [1.98, 2.73] 2.89 [2.41, 3.39] REVE Pooled 4x Population BA 235 80.76 [78.67, 83.00] 79.81 [78.32, 81.32] REVE Pooled 4x minus 1x 235 -1.42 [-1.83, -0.68] -1.57 [-1.99, -1.15]

24

<!-- page 25 -->

Model Dataset Contrast / condition N Median [95% CI] Mean [95% CI]

LaBraM Pooled 1x Personal benefit 235 2.42 [1.97, 2.80] 3.19 [2.61, 3.82] LaBraM Pooled 1x Personal specificity 235 3.17 [2.77, 3.68] 3.93 [3.35, 4.54] LaBraM Pooled 1x Population BA 235 81.14 [77.73, 83.26] 77.81 [75.92, 79.69] LaBraM Pooled 2x Personal benefit 235 2.58 [2.00, 3.03] 3.02 [2.44, 3.60] LaBraM Pooled 2x Personal specificity 235 2.87 [2.37, 3.40] 3.54 [3.04, 4.06] LaBraM Pooled 2x Population BA 235 81.21 [78.83, 83.25] 78.46 [76.59, 80.26] LaBraM Pooled 4x Personal benefit 235 1.97 [1.50, 2.50] 3.01 [2.39, 3.66] LaBraM Pooled 4x Personal specificity 235 2.94 [2.63, 3.30] 3.57 [3.02, 4.16] LaBraM Pooled 4x Population BA 235 82.33 [79.09, 84.70] 78.69 [76.82, 80.52] LaBraM Pooled 4x minus 1x 235 -0.45 [-0.99, 0.10] -0.18 [-0.65, 0.28] CBraMod Cho 5 labels 52 -0.60 [-1.40, 0.40] -0.40 [-1.26, 0.49] CBraMod Cho 10 labels 52 0.40 [-0.20, 1.20] 1.05 [0.14, 2.02] CBraMod Cho 20 labels 52 0.20 [-0.60, 1.40] 1.30 [0.13, 2.60] CBraMod Cho 40 labels 52 1.20 [0.40, 2.20] 2.15 [0.83, 3.60] CBraMod Dreyer 5 labels 80 -0.33 [-1.00, 0.00] -0.46 [-1.13, 0.21] CBraMod Dreyer 10 labels 80 0.25 [-0.33, 0.83] -0.05 [-0.70, 0.58] CBraMod Dreyer 20 labels 80 0.33 [-0.08, 1.00] 0.25 [-0.31, 0.80] CBraMod Dreyer 40 labels 80 1.17 [0.83, 1.67] 1.41 [0.91, 1.92] CBraMod PhysioNet 5 labels 103 0.76 [0.00, 1.08] 0.81 [0.22, 1.40] CBraMod PhysioNet 10 labels 103 0.83 [0.00, 1.44] 0.83 [0.24, 1.44] CBraMod PhysioNet 20 labels 103 1.52 [0.76, 1.89] 1.57 [0.87, 2.28] REVE Cho 5 labels 52 -0.40 [-0.90, 0.00] -0.38 [-0.92, 0.17] REVE Cho 10 labels 52 0.00 [-0.80, 0.70] 0.24 [-0.42, 0.96] REVE Cho 20 labels 52 0.70 [0.40, 1.30] 0.93 [0.33, 1.54] REVE Cho 40 labels 52 0.73 [0.10, 1.18] 1.25 [0.53, 2.07] REVE Dreyer 5 labels 80 0.33 [-0.08, 1.00] 0.54 [-0.24, 1.29] REVE Dreyer 10 labels 80 0.92 [0.33, 1.50] 1.36 [0.61, 2.12] REVE Dreyer 20 labels 80 1.33 [0.83, 2.67] 2.19 [1.46, 2.97] REVE Dreyer 40 labels 80 2.42 [1.67, 3.17] 3.08 [2.23, 3.94] REVE PhysioNet 5 labels 103 0.08 [0.00, 0.83] 0.33 [-0.22, 0.86] REVE PhysioNet 10 labels 103 0.23 [0.00, 0.83] 0.57 [0.02, 1.14] REVE PhysioNet 20 labels 103 1.00 [0.77, 1.74] 1.41 [0.81, 2.01] LaBraM Cho 5 labels 52 0.40 [-0.20, 0.80] 0.68 [-0.32, 1.84] LaBraM Cho 10 labels 52 0.90 [0.00, 2.00] 1.86 [0.57, 3.33] LaBraM Cho 20 labels 52 1.70 [0.50, 2.45] 2.96 [1.50, 4.60] LaBraM Cho 40 labels 52 1.72 [1.20, 2.95] 3.19 [1.63, 4.91] LaBraM Dreyer 5 labels 80 0.00 [-0.50, 0.67] -0.17 [-0.83, 0.44] LaBraM Dreyer 10 labels 80 0.00 [-0.33, 0.50] -0.14 [-0.76, 0.45] LaBraM Dreyer 20 labels 80 0.50 [0.00, 1.00] 0.41 [-0.17, 0.96] LaBraM Dreyer 40 labels 80 1.00 [0.50, 2.00] 1.41 [0.75, 2.06] LaBraM PhysioNet 5 labels 103 0.54 [0.00, 1.08] 0.95 [0.35, 1.57] LaBraM PhysioNet 10 labels 103 0.91 [0.08, 1.23] 1.12 [0.51, 1.75] LaBraM PhysioNet 20 labels 103 0.98 [0.00, 1.67] 1.25 [0.63, 1.91] CBraMod Pooled FILM True - shuffled 235 0.00 [0.00, 0.00] -0.01 [-0.10, 0.09] CBraMod Pooled FILM True - default 235 0.00 [0.00, 0.00] -0.21 [-0.38, -0.04] CBraMod Pooled LORA True - shuffled 235 0.00 [0.00, 0.00] 0.01 [-0.11, 0.11] CBraMod Pooled LORA True - default 235 0.00 [0.00, 0.00] -0.23 [-0.48, -0.01] CBraMod Pooled FiLM rest Nearest - population 235 -1.67 [-2.20, -1.00] -2.01 [-2.68, -1.37] CBraMod Pooled FiLM rest Random - population 235 -2.16 [-2.67, -1.73] -2.30 [-2.67, -1.92] CBraMod Pooled FiLM rest Nearest - random 235 0.44 [-0.02, 0.88] 0.28 [-0.25, 0.81] CBraMod Pooled FiLM task Nearest - population 235 -1.50 [-2.00, -0.91] -1.84 [-2.44, -1.24] CBraMod Pooled FiLM task Random - population 235 -2.16 [-2.67, -1.73] -2.30 [-2.69, -1.91] CBraMod Pooled FiLM task Nearest - random 235 0.77 [0.32, 1.36] 0.46 [-0.05, 0.95] CBraMod Pooled LoRA rest Nearest - population 235 -0.98 [-1.67, -0.67] -1.69 [-2.26, -1.15] CBraMod Pooled LoRA rest Random - population 235 -1.38 [-1.73, -1.02] -1.27 [-1.54, -0.99] CBraMod Pooled LoRA rest Nearest - random 235 0.00 [-0.50, 0.54] -0.42 [-0.93, 0.08] CBraMod Pooled LoRA task Nearest - population 235 -0.68 [-1.21, 0.00] -1.02 [-1.50, -0.53] CBraMod Pooled LoRA task Random - population 235 -1.38 [-1.73, -1.02] -1.27 [-1.55, -1.00]

25

<!-- page 26 -->

Model Dataset Contrast / condition N Median [95% CI] Mean [95% CI]

CBraMod Pooled LoRA task Nearest - random 235 0.57 [0.04, 0.96] 0.25 [-0.16, 0.67] CBraMod Pooled First-order MAML Before 235 0.00 [-0.23, 0.00] -0.32 [-0.61, -0.05] CBraMod Pooled First-order MAML After 235 0.00 [-0.20, 0.08] -0.05 [-0.32, 0.21] CBraMod Pooled First-order MAML Calibration incre- ment

235 0.17 [0.00, 0.33] 0.27 [-0.02, 0.56]

CBraMod Pooled Learned inner rates Before 235 -0.08 [-0.23, 0.00] -0.27 [-0.54, -0.01] CBraMod Pooled Learned inner rates After 235 0.00 [-0.17, 0.08] -0.08 [-0.34, 0.17] CBraMod Pooled Learned inner rates Calibration incre- ment

235 0.00 [0.00, 0.33] 0.19 [-0.10, 0.48]

CBraMod Lee FiLM Own - population 54 -0.50 [-2.70, 1.00] -0.67 [-2.12, 0.84] CBraMod Lee FiLM Own - exchanged 54 2.50 [0.45, 4.60] 3.91 [2.17, 5.81] CBraMod Lee LoRA Own - population 54 1.00 [-0.80, 2.60] 1.02 [-0.09, 2.16] CBraMod Lee LoRA Own - exchanged 54 2.58 [1.87, 4.35] 3.78 [2.43, 5.24] CBraMod BNCI FiLM Own - population 9 5.56 [-2.22, 11.94] 5.12 [1.57, 8.67] CBraMod BNCI FiLM Own - exchanged 8 6.94 [-0.28, 16.11] 7.85 [2.50, 13.16] CBraMod BNCI LoRA Own - population 9 5.00 [-3.61, 11.39] 4.81 [0.80, 8.61] CBraMod BNCI LoRA Own - exchanged 8 12.08 [0.56, 14.72] 9.76 [5.17, 13.78]

## S2 CBraMod Supplementary Results

The descriptive tables report paired subject means, subject standard deviations, and sample sizes. Standard deviations quan- tify heterogeneity, not standard errors or confidence intervals. Zero-label gains are defined by the matched starting model; unavailable budgets remain absent.

Table S3: CBraMod few-label calibration: paired subject means and between-subject standard deviations. Gains are in percentage points.

Dataset Start Labels N Mean gain (pp) Subject SD (pp)

PhysioNet B3 5 103 0.78 2.98 PhysioNet B3 10 103 0.93 3.36 PhysioNet B3 20 103 1.50 3.91 PhysioNet G 5 103 0.81 3.07 PhysioNet G 10 103 0.83 3.11 PhysioNet G 20 103 1.57 3.65 Dreyer B3 5 80 -0.18 3.09 Dreyer B3 10 80 -0.09 2.94 Dreyer B3 20 80 0.41 2.86 Dreyer B3 40 80 1.64 2.78 Dreyer G 5 80 -0.46 3.11 Dreyer G 10 80 -0.05 2.93 Dreyer G 20 80 0.25 2.54 Dreyer G 40 80 1.41 2.31 Cho B3 5 52 0.19 3.17 Cho B3 10 52 1.27 3.86 Cho B3 20 52 1.36 4.31 Cho B3 40 52 2.36 5.72 Cho G 5 52 -0.40 3.24 Cho G 10 52 1.05 3.46 Cho G 20 52 1.30 4.63 Cho G 40 52 2.15 5.14 Lee G 5 54 -1.22 2.12 Lee G 10 54 -0.70 1.80 Lee G 20 54 -0.34 3.13 BNCI G 5 9 -0.65 2.90 BNCI G 10 9 2.69 2.67 BNCI G 20 9 0.68 4.26

26

<!-- page 27 -->

B3 G primary

R2

60

65

70

75

80

85

Mean BA (%)

A  PhysioNet · LoRA

B3 G primary

R2

60

65

70

75

80

85

B  Dreyer · LoRA

B3 G primary

R2

60

65

70

75

80

85

C  Cho · LoRA

B3 G R2* 0

1

2

3

4

Mean personal gain (pp)

3.22 3.01

1.32

3.08 3.07 2.14

D  Reference sensitivity

FiLM LoRA

−5.0

−2.5

0.0

2.5

5.0

7.5

Paired difference (pp)

E  Lee

FiLM LoRA

0

10

20

Paired difference (pp)

F  BNCI

BNCI: Δ uses all subjects; U uses the available donors.

Population start Personal fit Task head B0

Panel D

FiLM LoRA

Panels E–F

Δ: own − G U: own − swapped

Figure S6: CBraMod decomposition under B3, G, and R2. Personal gains use the same paired means; Lee and BNCI also distinguish own- minus-population from own-minus-swapped. Lee panel E shows subject interquartile ranges as vertical lines; BNCI panel F shows individual subject differences as faint points. R2-FiLM changes the population parameter family.

27

<!-- page 28 -->

0 10 20

Target labels (total)

0

2

4

Mean personal gain (pp)

PhysioNet

0 10 20 40

Target labels (total)

Dreyer

0 10 20 40

Target labels (total)

Cho

0 10 20

Target labels (total)

0

2

4

Mean personal gain (pp)

Lee

0 10 20

Target labels (total)

BNCI

B3

G

Full earlier half

Figure S7: CBraMod few-shot gains, including the external datasets and default-context reference. Full-half reference lines use the matched scoring path.

28

<!-- page 29 -->

B3 G R2*

−2.5

0.0

2.5

5.0

7.5

Own − population (pp)

PhysioNet · FiLM

B3 G R2*

Dreyer · FiLM

B3 G R2*

Cho · FiLM

B3 G R2*

−2.5

0.0

2.5

5.0

7.5

Own − population (pp)

PhysioNet · LoRA

B3 G R2*

Dreyer · LoRA

B3 G R2*

Cho · LoRA

Figure S8: Personal-gain means (points) and subject interquartile ranges (bars), separately by dataset, family, and population start. R2* is a LoRA population model also used for the FiLM sensitivity analysis.

## S2.1 Euclidean alignment and positive counterexamples

The EA experiments whiten native multichannel inputs before the frozen backbone. Their results include substantial PhysioNet

degradation and an exception: all-unlabeled-task EA with the multilayer head improves Dreyer by 1.43 pp on average, with

original Holm p = 0.0239. This variant uses unlabeled query-task inputs and is transductive. The rest-only and matched

eyes-open variants, head variants, dataset results, and negative directions all remain in the Supplementary Data 1.

EA was applied to stored microvolt-scaled signals with fixed diagonal shrinkage. Whitening changes signal amplitude and

spatial structure, and EA/non-EA intermediate precision paths are not identical. Hence this comparison does not isolate spatial

mixing alone. The original EA work [1] and positive results in ordinary deep networks [2] limit any general claim that align-

ment is harmful. Reduced-channel and Riemannian recentering approaches also have favorable frozen-model configurations

[3]. Their channel projection and covariance geometry differ from native-channel arithmetic-mean whitening here. Compass

discusses the possible interaction with pretrained spatial structure [4]; amplitude, channel rank, and covariance estimation

are further hypotheses, not established causes. Adaptive EA results involving target-test performance for projection selection

require that selection condition to be stated [5].

## S2.2 Rest-based transfer and few-shot disagreements

ResTL’s positive evidence concerns generating task examples from target rest and updating a decoder, including a noise-versus-

rest comparison [6]. Its task-adjacent baseline, optimization path, and decoder updates differ from our independent-context

generator and donor-parameter transfer. Baseline correction and test-time training provide additional positive evidence under

29

<!-- page 30 -->

FiLM

rest

FiLM task

LoRA

rest

LoRA

task

−0.2

0.0

0.2

0.4

0.6

0.8

Mean gain over population (pp)

B3 · three-donor average

FiLM

rest

FiLM task

LoRA

rest

LoRA

task

G · three-donor average

Nearest Random

Figure S9: All initial-cohort secondary three-donor averages. FiLM and LoRA nearest-minus-G means are positive; the LoRA random-donor averages also exceed G. These are secondary, uncorrected comparisons.

0 5 10 15 20

Target labels (total)

−7.5

−5.0

−2.5

0.0

2.5

5.0

Mean own − B3 (pp)

PhysioNet

0 10 20 30 40

Target labels (total)

Dreyer

0 10 20 30 40

Target labels (total)

Cho

FiLM LoRA

Figure S10: Default-context few-shot curves for both personal families. FiLM’s low-budget negative mean gains remain visible. Curves connect observed budgets only; their zero-label reference is an identity.

30

<!-- page 31 -->

other procedures [7, 8]. These differences could affect how useful personal information is extracted, but have not been separately

manipulated here.

Likewise, positive results from personal encoders and EEG-Reptile [9, 10] can coexist with our negative small-budget

outcomes. Label budget, target parameterization, source-model quality, and validation size may contribute. The available

abstract for the LaBraM calibration work supports its relevance but not a precise reconstruction of its label budget or all

controls [11]. A mismatch between outcomes is therefore a boundary on generalization, not a basis for declaring those studies

incorrect.

## S3 Literature Comparison and Search Scope

The literature comparison uses the publisher’s Scientific Reports Article in Press for Lopes et al. (accepted 26 August 2026,

published 3 September 2026, DOI 10.1038/s41598-026-69220-z), separately from their arXiv preprint. Page references below

count the cover as page 1 of that 24-page publisher PDF; the final typeset pagination may differ.

Table S4: Related evaluation questions, target settings and controls. The comparison concerns study designs and inspected controls, not an accuracy ranking.

Work Reference Question Subject / target setting Verified control scope

Identity Trap [12] Representation / identity audit

Task- and dataset- dependent

Identity diagnostics; attribution package not established here EEG-FM- Compass

[4] Benchmark and adaptation compari- son

LOSO and within- subject few-shot separately

Separate protocols; no joint own/population/swapped gain decom- position Stacked LoRA [13] Shared and personal low-rank adapters

Subjects seen in pooled trial split

Global adapter comparison; different ca- pacity; mismatch not reported in read text Lopes et al. (Scientific Reports)

[14] Personal encoders and alignment

LOSO; target calibra- tion

Low-rank, shared-adaptation, mismatch, capacity and normalization controls

Nguyen et al. [15] Frozen-model popu- lation LoRA

Held-out subjects Head versus LoRA; no target personal adapter in evaluated pipeline ResTL [6] Rest-based genera- tive transfer

LOSO; target rest Noise/rest control; updates decoder; donor- rest swap not reported in read text Sharma et al. [16] Transfer learning versus MAML

Held-out subjects; few-shot labels

Ordinary transfer baseline; optimizers dif- fer; total training budget not matched This study Gain attribution on frozen backbone

Held-out subjects; same-session split

Default/shuffled; own/swapped; outer- update continuation; separate Delta and U

## S3.1 Control-by-control comparison with Lopes et al.

Table S5: Control-by-control comparison with the published Lopes et al. study. Page numbers refer to the publisher PDF described above.

Dimension Lopes et al., published article [14] Present study

Population split LOSO; validation holds out 20% of trials within each source subject (p. 8, implemen- tation details).

Downstream train/validation/test subjects disjoint; core pools three datasets.

Target labels First 48 trials for encoder selection and fine- tuning (p. 7, Eq. 10; Fig. 2).

Full earlier half and specified few-label prefixes; later half for evaluation. Parameters Subject-specific encoder branches and resid- ual input-channel low-rank layers (pp. 6–8; Table 1, p. 13).

Frozen pretrained transformers with personal at- tention LoRA; CBraMod FiLM extension.

31

<!-- page 32 -->

Dimension Lopes et al., published article [14] Present study

Shared reference Shared encoder (p. 6); the discussion reports no encoder-bank accuracy advantage over a fine-tuned shared baseline under matched adaptation (p. 20).

Named population reference and ordinary- continuation sensitivity, with paired BA contrasts.

Mismatch Class distinctiveness and matched/mismatched latent geometry; source-subject routing (pp. 14–16, Figs. 6B and 8).

Held-out target query BA using owner versus donor adapters fitted on earlier support labels.

Capacity Widened shared model and subject-specific batch-normalization controls (p. 15, after the matched/mismatched analysis).

Same-capacity true/shuffled/default context; popu- lation and personal fits have different capacity.

Alignment With/without Euclidean Alignment; prospec- tive covariance estimation (pp. 4–5, Eqs. 6– 8; Fig. 3).

Separate native-channel alignment diagnostics, in- cluding transductive and precision limitations.

Training budget Fixed recipes and early stopping (p. 8); validation-loss trajectories in Fig. 9, but no corresponding personal-gain budget curve identified.

Exact original, doubled and quadrupled population-update endpoints; convergence unconfirmed.

The overlap includes personal low-rank parameterization and shared/mismatch controls. The additional question here is

their joint classification benefit in frozen EEG foundation models as population training varies. The comparison concerns the

published methods and results.

## S3.2 Distinguishing model benchmarking from personal attribution

Yang et al.’s ICLR 2026 article, Are EEG Foundation Models Worth It? Comparative Evaluation with Traditional Decoders in

Diverse BCI Tasks, compares foundation models with traditional decoders across six evaluation protocols and introduces ST-

EEGFormer [17]. The author repository and ICLR listing verify the conference identity; it is distinct from EEG-FM-Compass

[4] and the earlier ST-EEGFormer submission. Its model-ranking question differs from the two paired adaptation contrasts

reported here. No claim that all of its controls are absent is needed for that distinction.

The comparisons concern target settings, information access and control scope; accuracies are not pooled across different

tasks, label budgets, metrics or pretrained sources.

## S4 Complete Prespecified Checks and Comparisons

The appendix includes engineering checks, joint decisions, complete comparison rows, convergence records, and nonexecuted

or nonidentifiable items. Later extensions do not retrospectively change earlier failures. Tables reuse overlapping pooled, per-

dataset, and subgroup summaries; repeated rows and reused EA tables are not independent replication. A blank statistic denotes

unavailable or inapplicable evidence and is never imputed as zero. Raw and corrected p-values retain the correction families

specified for each analysis. The complete comparison inventory in Supplementary Data 1 includes negative and nonsignificant

results.

## S4.1 Engineering and data checks

32

<!-- page 33 -->

Table S6: Engineering and data checks with their preserved outcomes.

ID Check Preserved outcome

E01 Split, temporal, shuffle, identity and statistics contracts

Implementation checks passed; synthetic checks do not establish task performance. E02 Checkpoint source and compute compatibility

Execution checks passed; pretraining overlap remains a separate source audit. E03 Initial data-screening stop rule Triggered for PhysioNet; the initial implementation also rejected Cho. Screening was revised before the subsequent analyses; the ini- tial failures remain reported. E04 Initial task-head accuracy stop rule Saved head results exceed the threshold; the later record-only rule does not erase the previous data-screening failure. E05 Matched eyes-closed versus eyes- open alpha diagnostic

Most PhysioNet records agree; exceptions retained. Dreyer/Cho do not support the same diagnostic. E06 Rest availability, state, boundaries, duration and finite values

Included subjects and exceptional boundaries preserved; missing records are not marked as passed. E07 Cho original ordering Cohort metadata checked; limited independent signal check. A com- plete continuous-timeline reconstruction is not established. E08 Half-split labels and available sup- ports

Saved counts and imbalance diagnostics retained without subject re- moval; unavailable high-label budgets omitted. E09 Default-model score identity Batch-dependent boundary changes broke strict score equality. The observed discrepancies and the scoring rule specified before subse- quent runs are reported. E10 Population-continuation predic- tions, labels, donors and frozen settings

Saved audits verified the completed predictions; rare initial-cohort batch-path differences and exact Lee checks retained.

E11 Accuracy trend at population-model early stopping

Not recoverable: only loss trajectories and overwritten best check- points were saved. E12 BNCI raw-event/rest/task corre- spondence

Recorded audit passed. Native/readout distinction and donor-pool limitations retained. E13 Follow-up prediction and frozen- source consistency

Saved R2/BNCI audits agree with completed outputs; isolated R2 batch-path flips retained with matched baselines.

## S4.2 Original joint gates and specified secondary endpoints

R1-based M gates below use test-query-informed validation priors; their original decisions describe that query-informed access condition and are not independent confirmation under test-label isolation. This caveat applies to both primary and secondary R1 comparisons. “Pass” refers only to the named original rule. In particular, an own-versus-swapped pass does not establish a positive own-versus-population gain, and a secondary pass does not rescue a failed primary endpoint. Median differences and mean gains use pp; recovery and decline rates in the table are fractions. The contextual recovery statistic divides the mean contextual gain over B0 by the mean designated supervised-reference gain over B0; it is not a mean of individual ratios. Its observed reference means are positive, and no zero- or negative-denominator decision is inferred. W and the follow-up preserve the original three-slot own-versus-swapped Holm family: the unexecuted mixture-offset variant occupies a conservative unit-p slot internally, while its actual result remains unavailable. It is not an observed negative test.

Table S7: Original joint decision rules, observed components and decisions. A favorable component does not override a failed joint rule.

Gate ID Cohort Prespecified rule Observed Decision

B-G pooled Median vs B0 >= 2 pp median 1.000 Fail B2-film_first2 pooled Median vs B0 >= 2 pp; one-sided Holm(4) vs tuned head < .05

median 1.833; pH 0.030713 Fail

B2-film_all pooled Median vs B0 >= 2 pp; one-sided Holm(4) vs tuned head < .05

median 2.833; pH 1.155e-08 Pass

B2-lora4 pooled Median vs B0 >= 2 pp; one-sided Holm(4) vs tuned head < .05

median 2.800; pH 1.2765e-15 Pass

33

<!-- page 34 -->

Gate ID Cohort Prespecified rule Observed Decision

B2-lora8 pooled Median vs B0 >= 2 pp; one-sided Holm(4) vs tuned head < .05

median 3.409; pH 1.3182e-17 Pass

C-M_film pooled One-sided Holm(4) vs B4 and B0 < .05; re- covery >= .30; drop > 2 pp <= .10

both p pass False; recovery 0.981; drop 0.230 Fail

C-M_lora pooled One-sided Holm(4) vs B4 and B0 < .05; re- covery >= .30; drop > 2 pp <= .10

both p pass False; recovery 1.561; drop 0.128 Fail

C2-D1-film_offset pooled U median >= 2 pp; Holm(3) < .05 median 4.617; pH 4.1681e-31 Pass C2-D1-mix_offset pooled U median >= 2 pp; Holm(3) < .05 median 2.580; pH 7.1335e-23 Pass C2-D1-lora8 pooled U median >= 2 pp; Holm(3) < .05 median 3.470; pH 5.0123e-28 Pass C2-D2-film_offset pooled After D1: nearest > random; Holm(3) < .05 median 0.561; pH 0.10124 Fail C2-D2-mix_offset pooled After D1: nearest > random; Holm(3) < .05 median 0.367; pH 0.10124 Fail C2-D2-lora8 pooled After D1: nearest > random; Holm(3) < .05 median 0.017; pH 0.73119 Fail C3-D3-film_offset pooled Task nearest > random; k=1; Holm(2) < .05 median 0.917; pH 0.00051699 Pass C3-D3-lora8 pooled Task nearest > random; k=1; Holm(2) < .05 median 0.189; pH 0.17997 Fail C4-main pooled LoRA n=10; P2 > P1 and P0; both one- sided raw p < .05

P2-P1: p 0.89273; P2-P0: p 0.44768 Fail

C4-secondary-n0 pooled P2 > P1; Holm(2) across label budgets < .05

median 0.180; pH 0.078435 Fail

C4-secondary-n5 pooled P2 > P1; Holm(2) across label budgets < .05

median 0.100; pH 0.29768 Fail

M-main-M1 pooled vs R1; Holm(2) < .05; median >= 1 pp; drop > 2 pp <= .10

median 0.517; pH 6.7044e-05; drop 0.123

Fail

M-main-M2 pooled vs R1; Holm(2) < .05; median >= 1 pp; drop > 2 pp <= .10

median 0.576; pH 6.7044e-05; drop 0.132

Fail

M-secondary-n5-M1 pooled vs R1; Holm(2) < .05; median >= 1 pp; drop > 2 pp <= .10

median 0.483; pH 0.0036885; drop 0.153

Fail

M-secondary-n5-M2 pooled vs R1; Holm(2) < .05; median >= 1 pp; drop > 2 pp <= .10

median 0.500; pH 0.00033439; drop 0.128

Fail

M-secondary-n20-M1 pooled vs R1; Holm(2) < .05; median >= 1 pp; drop > 2 pp <= .10

median 0.467; pH 0.0010864; drop 0.140

Fail

M-secondary-n20-M2 pooled vs R1; Holm(2) < .05; median >= 1 pp; drop > 2 pp <= .10

median 0.333; pH 0.0010864; drop 0.094

Fail

M-adapt-M1 pooled Adaptation increment vs R1; Holm(2) < .05 mean 0.316; pH 0.041048 Pass M-adapt-M2 pooled Adaptation increment vs R1; Holm(2) < .05 mean 0.235; pH 0.06045 Fail W-diagnostic1-film_offset- pooled U median >= 2 pp; Holm(3) < .05 median 4.689; pH 9.1247e-32 Pass W-diagnostic1-lora8- pooled U median >= 2 pp; Holm(3) < .05 median 3.533; pH 3.1524e-28 Pass W-diagnostic2_3-film_offset-rest pooled Nearest > random; k=1; rest Holm(3), task Holm(2) < .05

median 0.440; pH 0.10461 Fail

W-diagnostic2_3-lora8-rest pooled Nearest > random; k=1; rest Holm(3), task Holm(2) < .05

median 0.000; pH 1 Fail

W-diagnostic2_3-film_offset-task pooled Nearest > random; k=1; rest Holm(3), task Holm(2) < .05

median 0.767; pH 0.0042664 Pass

W-diagnostic2_3-lora8-task pooled Nearest > random; k=1; rest Holm(3), task Holm(2) < .05

median 0.567; pH 0.053663 Fail

W-Lee_diagnostic1-film_offset- Lee U median >= 2 pp; Holm(3) < .05 median 2.500; pH 0.00015151 Pass W-Lee_diagnostic1-lora8- Lee U median >= 2 pp; Holm(3) < .05 median 2.580; pH 2.2285e-06 Pass W-Lee_diagnostic2-film_offset- Lee Nearest > random; k=1; rest Holm(3), task Holm(2) < .05

median 0.500; pH 0.62662 Fail

W-Lee_diagnostic2-lora8- Lee Nearest > random; k=1; rest Holm(3), task Holm(2) < .05

median 1.190; pH 0.016588 Pass

WF-R2_sensitivity_diagnostic1- film_offset-

pooled U median >= 2 pp; Holm(3) < .05 median 4.008; pH 4.4201e-29 Pass

WF-R2_sensitivity_diagnostic1- lora8-

pooled U median >= 2 pp; Holm(3) < .05 median 3.447; pH 4.3558e-26 Pass

WF-BNCI_diagnostic1_available_ subset-film_offset-

BNCI; swap subset

U median >= 2 pp; Holm(3) < .05 median 6.944; pH 0.04995 Pass

34

<!-- page 35 -->

Gate ID Cohort Prespecified rule Observed Decision

WF-BNCI_diagnostic1_available_ subset-lora8-

BNCI; swap subset

U median >= 2 pp; Holm(3) < .05 median 12.083; pH 0.037593 Pass

## S4.3 Unexecuted, unavailable, and superseded items

Table S8: Unexecuted, unavailable and superseded items with their interpretation.

ID Item Status and interpretation

N01 Initial success reference B1 Replaced by B0 before the subsequent experiment; success was not assessed retrospectively against B1. N02 Meta-learning confirmation on Lee Not executed because the M primary gate failed. The separate W Lee evaluation is not that confirmation. N03 Cross-session robustness Not executed; current performance evidence is within-session. N04 Context-duration curve Planned mechanism stage not started; no result or negative test in- ferred. N05 Eyes-open, eyes-closed and combined context

Not executed under the matched-duration design.

N06 Rest-versus-task contextual generator Not executed; task-neighbor transfer is a different operation. N07 Covariance / embedding / combined context ablation

Not executed.

N08 Training-subject scaling Not executed. N09 Context probes for identity and opti- mal personal parameters

Not executed.

N10 Mechanism-stage margin removal Mechanism stage not started; the corresponding zero-margin con- textual diagnostic is already in the contextual-model tables. N11 Label budgets above available support Unavailable for affected subjects/datasets; not filled by repeating labels. N12 Swap for BNCI’s singleton test fold Not estimable; own-versus-G still includes this target. N13 BNCI nearest-donor choice Structurally unidentifiable: absent or unique donor; no inference of information absence. N14 Validation accuracy at early stopping Unrecorded and not recoverable from the saved loss series.

## S4.4 Cross-model scope

The LoRA core on the initial three datasets is complete for REVE and LaBraM; Supplementary Section S8 records its original

decisions and descriptive comparisons. Their FiLM, rest/task neighbors, external-dataset, and meta-learning extensions remain

unexecuted. Supplementary Section S9 reports the completed three-model population-budget curves, including CBraMod’s

documented precision exception and initial failure. Those results retain the original decisions printed here.

35

<!-- page 36 -->

## S4.5 Run-level convergence records

“Both flat” requires the original train and validation plateau criteria together. Update columns report additional continuation updates; fold indices and seeds are retained for traceability. None of these records confirms joint convergence.

0.0

0.5

1.0

1.5

2.0

Subject-mean CE

Initial cohort · FiLM

0

1

2

3

Lee · FiLM

0

2

4

6

BNCI · FiLM

0 2000 4000 6000

Additional updates

0.5

1.0

1.5

Subject-mean CE

Initial cohort · LoRA

0 2000 4000 6000

Additional updates

0

1

2

3

4

5

Lee · LoRA

0 2000 4000 6000

Additional updates

0

2

4

6

8

BNCI · LoRA

Train Validation

Figure S11: Continuation-loss trajectories. Each line represents one fold/seed run through its stopping point. Training and validation subject- mean cross-entropy are shown separately without smoothing or extrapolation.

Table S9: CBraMod continuation records by dataset, parameter family, fold and seed. Update counts are additional continuation updates; no run confirms the joint plateau.

Cohort Family Fold Seed Run steps Selected Train flat Val. flat Both flat

Core cohort FiLM population 0 11 2750 750 False False False Core cohort LoRA population 0 11 2000 0 False False False Core cohort FiLM population 0 23 2250 250 False False False Core cohort LoRA population 0 23 2500 500 False False False Core cohort FiLM population 0 37 2500 500 False False False Core cohort LoRA population 0 37 2000 0 False False False Core cohort FiLM population 0 53 2000 0 False False False Core cohort LoRA population 0 53 2000 0 False False False Core cohort FiLM population 0 71 2000 0 False False False Core cohort LoRA population 0 71 2000 0 False False False Core cohort FiLM population 1 11 2250 250 False False False Core cohort LoRA population 1 11 2000 0 False False False Core cohort FiLM population 1 23 2500 500 False False False Core cohort LoRA population 1 23 2000 0 False False False Core cohort FiLM population 1 37 2000 0 False False False Core cohort LoRA population 1 37 2250 250 False False False Core cohort FiLM population 1 53 2750 750 False False False

36

<!-- page 37 -->

Cohort Family Fold Seed Run steps Selected Train flat Val. flat Both flat

Core cohort LoRA population 1 53 2000 0 False False False Core cohort FiLM population 1 71 2500 500 False False False Core cohort LoRA population 1 71 2500 500 False False False Core cohort FiLM population 2 11 4250 2250 False False False Core cohort LoRA population 2 11 4250 2250 False False False Core cohort FiLM population 2 23 6500 4500 False False False Core cohort LoRA population 2 23 2250 250 False False False Core cohort FiLM population 2 37 2000 0 False False False Core cohort LoRA population 2 37 2000 0 False False False Core cohort FiLM population 2 53 2000 0 False False False Core cohort LoRA population 2 53 3000 1000 False False False Core cohort FiLM population 2 71 2500 500 False False False Core cohort LoRA population 2 71 2500 500 False False False Core cohort FiLM population 3 11 2000 0 False False False Core cohort LoRA population 3 11 2000 0 False False False Core cohort FiLM population 3 23 2000 0 False False False Core cohort LoRA population 3 23 2000 0 False False False Core cohort FiLM population 3 37 2000 250 False False False Core cohort LoRA population 3 37 2000 0 False False False Core cohort FiLM population 3 53 2000 0 False False False Core cohort LoRA population 3 53 2750 750 False False False Core cohort FiLM population 3 71 2000 0 False False False Core cohort LoRA population 3 71 2250 250 False False False Core cohort FiLM population 4 11 2000 0 False False False Core cohort LoRA population 4 11 2000 0 False False False Core cohort FiLM population 4 23 2000 0 False False False Core cohort LoRA population 4 23 2500 500 False False False Core cohort FiLM population 4 37 2250 250 False False False Core cohort LoRA population 4 37 2000 0 False False False Core cohort FiLM population 4 53 2000 0 False False False Core cohort LoRA population 4 53 2000 0 False False False Core cohort FiLM population 4 71 2250 250 False False False Core cohort LoRA population 4 71 2250 250 False False False Lee2019_MI FiLM population 0 11 2000 0 False False False Lee2019_MI LoRA population 0 11 2250 250 False False False Lee2019_MI FiLM population 0 23 2000 0 False False False Lee2019_MI LoRA population 0 23 2000 0 False False False Lee2019_MI FiLM population 0 37 2000 0 False False False Lee2019_MI LoRA population 0 37 3250 1250 False False False Lee2019_MI FiLM population 0 53 2750 750 False False False Lee2019_MI LoRA population 0 53 2500 500 False False False Lee2019_MI FiLM population 0 71 2000 0 False False False Lee2019_MI LoRA population 0 71 2750 750 False False False Lee2019_MI FiLM population 1 11 2000 0 False False False Lee2019_MI LoRA population 1 11 2000 0 False False False Lee2019_MI FiLM population 1 23 2000 0 False False False Lee2019_MI LoRA population 1 23 3500 1500 False False False Lee2019_MI FiLM population 1 37 2750 750 False False False Lee2019_MI LoRA population 1 37 2250 250 False False False Lee2019_MI FiLM population 1 53 2750 750 False False False Lee2019_MI LoRA population 1 53 3500 1500 False False False Lee2019_MI FiLM population 1 71 2750 750 False False False Lee2019_MI LoRA population 1 71 2000 0 False False False Lee2019_MI FiLM population 2 11 2250 250 False False False Lee2019_MI LoRA population 2 11 2000 0 False False False Lee2019_MI FiLM population 2 23 3750 1750 False False False Lee2019_MI LoRA population 2 23 2000 0 False False False Lee2019_MI FiLM population 2 37 2250 250 False False False

37

<!-- page 38 -->

Cohort Family Fold Seed Run steps Selected Train flat Val. flat Both flat

Lee2019_MI LoRA population 2 37 2000 0 False False False Lee2019_MI FiLM population 2 53 2500 500 False False False Lee2019_MI LoRA population 2 53 2250 250 False False False Lee2019_MI FiLM population 2 71 2000 0 False False False Lee2019_MI LoRA population 2 71 3000 1000 False False False Lee2019_MI FiLM population 3 11 2250 250 False False False Lee2019_MI LoRA population 3 11 2750 750 False False False Lee2019_MI FiLM population 3 23 2000 0 False False False Lee2019_MI LoRA population 3 23 2750 750 False False False Lee2019_MI FiLM population 3 37 2000 0 False False False Lee2019_MI LoRA population 3 37 2250 250 False False False Lee2019_MI FiLM population 3 53 3000 1000 False False False Lee2019_MI LoRA population 3 53 2250 250 False False False Lee2019_MI FiLM population 3 71 2500 500 False False False Lee2019_MI LoRA population 3 71 2750 750 False False False Lee2019_MI FiLM population 4 11 2000 0 False False False Lee2019_MI LoRA population 4 11 2000 0 False False False Lee2019_MI FiLM population 4 23 2000 0 False False False Lee2019_MI LoRA population 4 23 2250 250 False False False Lee2019_MI FiLM population 4 37 2000 0 False False False Lee2019_MI LoRA population 4 37 2750 750 False False False Lee2019_MI FiLM population 4 53 2250 250 False False False Lee2019_MI LoRA population 4 53 2000 0 False False False Lee2019_MI FiLM population 4 71 2000 0 False False False Lee2019_MI LoRA population 4 71 2000 0 False False False BNCI FiLM population 0 11 2000 0 False False False BNCI LoRA population 0 11 2000 0 False False False BNCI FiLM population 0 23 2000 0 False False False BNCI LoRA population 0 23 2000 0 False False False BNCI FiLM population 0 37 2250 250 False False False BNCI LoRA population 0 37 2000 0 False False False BNCI FiLM population 0 53 2500 500 False False False BNCI LoRA population 0 53 2000 0 False False False BNCI FiLM population 0 71 2000 0 False False False BNCI LoRA population 0 71 2000 0 False False False BNCI FiLM population 1 11 3500 1500 False False False BNCI LoRA population 1 11 2000 0 False False False BNCI FiLM population 1 23 2000 0 False False False BNCI LoRA population 1 23 2750 750 True False False BNCI FiLM population 1 37 2250 250 False False False BNCI LoRA population 1 37 4250 2250 False False False BNCI FiLM population 1 53 2750 750 False False False BNCI LoRA population 1 53 5750 3750 False False False BNCI FiLM population 1 71 2000 0 False False False BNCI LoRA population 1 71 4000 2000 False False False BNCI FiLM population 2 11 2750 750 False False False BNCI LoRA population 2 11 3250 1250 False False False BNCI FiLM population 2 23 2000 0 False False False BNCI LoRA population 2 23 2000 0 False False False BNCI FiLM population 2 37 2250 250 False False False BNCI LoRA population 2 37 2000 0 False False False BNCI FiLM population 2 53 2000 0 False False False BNCI LoRA population 2 53 3000 1000 False False False BNCI FiLM population 2 71 2500 500 False False False BNCI LoRA population 2 71 3500 1500 False False False BNCI FiLM population 3 11 2000 0 False False False BNCI LoRA population 3 11 2500 500 False False False BNCI FiLM population 3 23 2000 0 False False False

38

<!-- page 39 -->

Cohort Family Fold Seed Run steps Selected Train flat Val. flat Both flat

BNCI LoRA population 3 23 2000 0 False False False BNCI FiLM population 3 37 2000 0 False False False BNCI LoRA population 3 37 2000 0 False False False BNCI FiLM population 3 53 2000 0 False False False BNCI LoRA population 3 53 2250 250 False False False BNCI FiLM population 3 71 2000 0 False False False BNCI LoRA population 3 71 2000 0 False False False BNCI FiLM population 4 11 2250 250 False False False BNCI LoRA population 4 11 2000 0 True False False BNCI FiLM population 4 23 2250 250 False False False BNCI LoRA population 4 23 2000 0 False False False BNCI FiLM population 4 37 2000 0 False False False BNCI LoRA population 4 37 2500 500 False False False BNCI FiLM population 4 53 2250 250 False False False BNCI LoRA population 4 53 2000 0 False False False BNCI FiLM population 4 71 2000 0 False False False BNCI LoRA population 4 71 2000 0 False False False

## S5 All statistical comparison rows

Supplementary Data 1 provides all 904 comparison rows (T0001–T0904) in CSV and XLSX formats, including negative and

nonsignificant results. The files contain the original identifiers, values, missing entries, source-row links and decisions, together

with column definitions, units, contrast directions and original correction-family descriptions. A saved Holm-adjusted value

belongs only to its identified source family; no correction across this combined inventory is applied, and a blank adjusted value

is unavailable rather than zero. Later-half and all-trial compatibility comparisons are distinguished, as are query-informed prior

comparisons. The companion README describes the CSV columns; the XLSX contains the same records plus Columns,

Families and Notation sheets. See Supplementary Data 1 (CSV) and Supplementary Data 1 (XLSX).

## S6 Recorded training resources

GPU runs used the recorded RTX 3090 environment. The population and personal-adaptation evaluation consumed 21.14

GPU card-hours, and the ordinary continuation/BNCI follow-up consumed 7.30 GPU card-hours. These are measured stage

totals, not a complete estimate for all exploratory work. Shared initial-cohort training cost is not charged separately to each

constituent dataset. Recorded meta-learning and ordinary-continuation run times appear in Supplementary Table S10. The

initial budget batch used 17.81, 51.59 and 18.70 GPU card-hours for CBraMod, REVE and LaBraM, respectively, including

the failed CBraMod run. The separately registered CBraMod retry added 0.69 GPU card-hours. The total including both

attempts was 88.79 GPU card-hours; shared-dataset training is counted once. No hardware cost is inferred for missing records.

Shared multi-dataset runs are counted once; incomplete run accounting prevents a complete total for exploratory work.

## S7 Query-informed prior controls and configuration grids

The query-informed random-prior control (R1) has test-query information leakage: its validation prior neighborhood and

shrinkage were selected using query scores from the test pool. The original R1 comparisons are retained as records of that

procedure and cannot establish independent confirmation under test-label isolation. No corrected experiment was performed.

The main meta-learning comparison with ordinary continuation is independent of that prior branch.

39

<!-- page 40 -->

Table S10: Recorded CBraMod training times. M1 and M2 include inner-loop work despite matching R2 in scheduled outer-update budget. Times are per-run means, not total study costs.

Method Inner steps Outer updates Mean seconds Runs

M1 5 2000 704.2 25 M1 10 2000 1250.1 25 M1 20 2000 2342.3 25 M2 5 2000 695.4 25 M2 10 2000 1235.3 25 M2 20 2000 2308.5 25 R2 0 2000 145.3 25

The original joint endpoint required at least one percentage point of median improvement over the validation-selected prior

control, corrected significance, and at most ten percent of subjects declining by more than two points.

At ten labels, the first-order MAML and learned-rate variants have median gains over R1 of 0.52/0.58 pp, with corrected

p = 6.7 × 10−5 for both. Both fail their original joint criterion; the secondary increment criterion passes for the first-order

method and fails for the learned-rate variant. These decisions have the leakage condition stated above.

R0 R1 R2 M1 M2

77.0

77.5

78.0

78.5

Mean BA (%)

A  Decoder performance

R0 R1 R2 M1 M2 0.0

0.2

0.4

0.6

Mean adaptation gain (pp)

B  Calibration increment

M1 M2

−0.3

−0.2

−0.1

0.0

Mean gain over R2 (pp)

C  Relative to R2

No target labels After calibration Initial Final

Figure S12: Mean meta-learning decomposition, including the query-informed prior control. R1 accesses test-query information during validation-prior selection. Its displayed comparisons are query-informed diagnostics. R2 is ordinary continuation; M1 is first-order MAML; M2 also learns inner rates.

The fixed prior diagnostic labels its population reference P0, random donor prior P1, and feature-selected prior P2. Its prior

neighborhood and shrinkage selection may use other donors’ later-half labels under the recorded leave-one-out protocol; the

target’s own query labels remain held out. This access condition is stronger than an entirely unlabeled deployment pipeline.

The failed P2 calibrated endpoint does not establish the proposed label-saving claim, even where the source file contains

interpolation summaries.

R1’s validation initialization has a distinct information boundary. The executed script selects its prior neighborhood and

shrinkage from query scores over the same-dataset test pool, then uses that prior for validation-subject calibration and control

ranking. Consequently, the query-informed R1 comparisons are not strictly isolated from test-query labels, even though their

final inner settings and reference ranking are evaluated on validation subjects. Their original numerical decisions are retained

as records under this access condition. M1, M2, R0 and R2 are selected independently of this R1 branch; the M-minus-R2

40

<!-- page 41 -->

comparison does not use its priors.

## S7.1 Configuration grids and execution identifiers

Table S11 lists the saved configuration grids. The identifier key is given in Supplementary Section S0; source-record links are included in Supplementary Data 1. Search grids and selection metadata are retained for reproducibility. Configura- tion constants specify the recorded procedures; they are separate from measured outcomes. The R2 configuration field B3_continued_original_objective denotes ordinary cross-entropy with default mixture weights, as specified by its saved configuration comment; it does not denote G’s context-mismatch objective.

Table S11: Recorded architecture and optimization settings. Semicolons in each value cell follow the setting-column order; commas enu- merate a search grid. Forty-label conditions require sufficient earlier support. New-model entries refer to REVE and LaBraM; personal optimization follows the common grid.

Component Setting (semicolon order) Value / grid

Partitions Folds; seed values 5; 11, 23, 37, 53, 71 Task head Learning rates; epochs; batch 0.001, 0.0003; 50; 128 Task head Weight decay; MLP hidden width 0.01; 128 CBraMod input Hz; high-pass Hz; rest segment s 200; 0.3; 4 Mains notch PhysioNet; Dreyer; Cho (Hz) 60; 50; 60 Personal diagnostics Earlier FiLM variants film2, film4, beta4, head Personal diagnostics Extended variants film_first2, film_all, lora4, lora8, scratch_head Personal diagnostics FiLM rate; head/LoRA rate 0.01, 0.1; 0.0001, 0.001 Personal diagnostics Steps; weight decay; batch 20, 60; 0.0, 0.01; 32 Context Minimum duration s; bands Hz 30; 8-13, 13-30 Context Band-filter order 4 Context Feature projection; hidden; latent 64; 128; 16 Context Generator hidden; FiLM bound 128; 0.1 Context LoRA Bases; rank; output-factor init SD 8; 8; 0.01 Context training Learning rates; candidate updates 0.0003, 0.001; 1000, 3000 Context training Margin weights; margins; zero ablation 0.1, 1.0; 0.1, 0.5; 0.0 Context training Batch; context dropout; decay; clip 32; 0.2; 0.01; 1.0 Personal fitting FiLM and mixture-offset rates; LoRA rates 0.01, 0.1; 0.0001, 0.001 Personal fitting Steps; weight decay; batch; rank 20, 60; 0.0, 0.01; 32; 8 Exchange Donor draws 10 Few-shot fitting Total label budgets 5, 10, 20, 40 Neighbors Primary k; secondary k; random draws 1; 3; 10 Prior Neighbors k; shrinkage alpha 3, 5; 0.25, 0.5, 1.0 Prior LoRA labels; penalty mu 0, 5, 10, 20; 0.0, 0.1, 1.0 Prior FiLM labels; penalty mu 0, 10; 0.0, 0.01, 0.1 Prior Steps; weight decay; batch 20, 60; 0.0; 32 Prior Test draws; validation draws 10; 1 G continuation Additional-step multiplier; check period 3; 250 G continuation Patience checks; minimum CE change 8; 0.0001 G plateau Window checks; relative loss range 8; 0.01 Meta inner loop SGD steps; learning rates 5, 10, 20; 0.003, 0.01, 0.03 Meta inner pilot Scanned learning rates; labels 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0; 10 Meta outer loop Episode labels; candidate updates 5, 10, 20; 1000, 2000 Meta outer loop Learning rate; decay; gradient clip 0.0001; 0.01; 1.0 Meta outer loop Subjects per batch; M2 log-rate LR 1; 0.001 REVE encoder Depth; width; patch samples; stride 22; 512; 200; 180 LaBraM encoder Depth; width; patch samples; stride 12; 200; 200; 200 LaBraM input High-pass; low-pass; notch (Hz) 0.1; 75; 50 REVE input High-pass Hz; sampling Hz 0.3; 200 New-model LoRA Rank; scale/rank; dropout 8; 1; 0 New-model population Learning rates; candidate updates 0.0003, 0.001; 1000, 3000 New-model population Batch; decay; gradient clip 32; 0.01; 1.0 New-model plateau Checks; relative CE range; floor 8; 0.01; 0.0001

41

<!-- page 42 -->

Component Setting (semicolon order) Value / grid

New-model plateau Accuracy/BA range; best-gain threshold 0.005; 0.001 Budget extension Update multipliers; check period 1, 2, 4; 250 Budget extension Directional-test alpha 0.05 BNCI input Window endpoints after trial start s 2, 6 Euclidean alignment Fixed diagonal shrinkage 0.001

42

<!-- page 43 -->

## S8 Cross-model results

## S8.1 Effect summaries and source strata

The table preserves the mean contrasts used for direction labels. Source status refers to the published pretraining-source lists. Shared parameterization and objectives differ from CBraMod, and source-unlisted is not a record-level exclusion certificate.

Table S12: Mean and median core contrasts and pretraining-source-list status. Differences are in percentage points; seeds are averaged within subject.

Dataset Model Source G-B0 mean Own-G mean Own-swap mean Own-swap median

PhysioNet CBraMod unlisted +9.14 +1.64 +2.55 +1.87 PhysioNet REVE unlisted +13.92 +1.55 +2.59 +2.39 PhysioNet LaBraM listed +20.21 +1.52 +2.35 +2.09 Dreyer CBraMod unlisted +9.18 +3.58 +5.28 +4.89 Dreyer REVE listed +8.98 +5.38 +7.25 +6.78 Dreyer LaBraM unlisted +9.31 +3.91 +5.41 +4.32 Cho CBraMod unlisted -0.06 +5.13 +6.43 +4.30 Cho REVE listed +2.48 +3.35 +4.38 +3.48 Cho LaBraM unlisted +1.74 +5.38 +4.78 +2.95

## S8.2 Original diagnostics and descriptive comparisons

The original pooled specificity test requires median own-minus-swapped at least two pp and the saved three-slot Holm criterion. Unexecuted FiLM and mixture slots remain unit-p placeholders for correction, with unavailable observed results. CBraMod’s original family includes executed FiLM and is preserved in the original decision table. No correction across the displayed model–dataset grid is introduced.

Table S13: Original pooled specificity decisions for REVE and LaBraM. The saved three-slot correction is retained.

Model N Median U (pp) Original Holm p Decision

REVE 235 3.50 1.38e-35 Pass LaBraM 235 3.17 1.19e-29 Pass

All completed cross-model core comparison rows below retain their original descriptive raw p-values. They are not nine new confirmatory tests. Means, medians and SDs are in pp; seeds are averaged within subjects.

Table S14: REVE and LaBraM core contrasts by dataset. Means, medians and standard deviations are in percentage points; p-values are the saved descriptive raw values.

Model Dataset Contrast N Mean Median SD Raw p

REVE Cho G minus B0 52 2.479 1.633 4.207 6.83e-05 REVE Cho own minus G 52 3.353 2.600 4.472 1.27e-08 REVE Cho own minus swap 52 4.383 3.480 4.556 2.57e-10 REVE Dreyer G minus B0 80 8.978 8.833 8.121 5.54e-12 REVE Dreyer own minus G 80 5.381 4.667 4.725 6.75e-14 REVE Dreyer own minus swap 80 7.251 6.775 4.911 4.39e-15 REVE PhysioNet G minus B0 103 13.915 13.385 9.854 7.16e-18 REVE PhysioNet own minus G 103 1.548 0.985 3.316 1.26e-05 REVE PhysioNet own minus swap 103 2.593 2.386 3.053 1.54e-13 LaBraM Cho G minus B0 52 1.742 0.600 5.573 0.0403 LaBraM Cho own minus G 52 5.375 3.383 6.448 1.12e-09 LaBraM Cho own minus swap 52 4.780 2.950 6.310 7.77e-09 LaBraM Dreyer G minus B0 80 9.313 9.667 5.717 7.34e-15 LaBraM Dreyer own minus G 80 3.915 3.000 3.788 1.26e-13 LaBraM Dreyer own minus swap 80 5.406 4.317 3.701 3.92e-15

43

<!-- page 44 -->

Model Dataset Contrast N Mean Median SD Raw p

LaBraM PhysioNet G minus B0 103 20.207 20.385 12.077 1.26e-18 LaBraM PhysioNet own minus G 103 1.524 0.909 3.633 5.53e-05 LaBraM PhysioNet own minus swap 103 2.347 2.091 3.786 1.72e-08

## S8.3 Few-shot reliability and original descriptive endpoints

Stability requires all prescribed mean gains to be nonnegative and nondecreasing across label budgets. It does not require every person to improve or constitute an inferential success threshold. The decline column below is the fraction of subjects losing more than two pp.

Table S15: Descriptive consistency of few-label calibration across the prescribed label budgets.

Dataset Model Descriptive stability

PhysioNet CBraMod Stable PhysioNet REVE Stable PhysioNet LaBraM Stable Dreyer CBraMod Not stable Dreyer REVE Stable Dreyer LaBraM Not stable Cho CBraMod Not stable Cho REVE Not stable Cho LaBraM Stable

## REVE.

Table S16: REVE few-label results. Gains are in percentage points; decline is the subject fraction losing more than two points.

Dataset Labels N Mean Median SD Decline fraction Raw p

Cho 5 52 -0.383 -0.400 2.036 0.154 0.963 Cho 10 52 0.241 0.000 2.574 0.115 0.409 Cho 20 52 0.928 0.700 2.212 0.077 0.00296 Cho 40 52 1.247 0.733 2.855 0.038 0.00164 Dreyer 5 80 0.544 0.333 3.523 0.138 0.0253 Dreyer 10 80 1.363 0.917 3.418 0.087 0.000253 Dreyer 20 80 2.193 1.333 3.421 0.050 2e-07 Dreyer 40 80 3.081 2.417 3.940 0.075 1.84e-09 PhysioNet 5 103 0.332 0.077 2.776 0.126 0.0483 PhysioNet 10 103 0.574 0.227 2.978 0.155 0.0256 PhysioNet 20 103 1.408 1.000 3.094 0.097 3.96e-06

## LaBraM.

Table S17: LaBraM few-label results. Gains are in percentage points; decline is the subject fraction losing more than two points.

Dataset Labels N Mean Median SD Decline fraction Raw p

Cho 5 52 0.680 0.400 4.006 0.154 0.182 Cho 10 52 1.860 0.900 5.147 0.135 0.00777 Cho 20 52 2.956 1.700 5.768 0.077 4.08e-05 Cho 40 52 3.194 1.717 6.072 0.077 1.19e-05 Dreyer 5 80 -0.175 0.000 2.922 0.175 0.518 Dreyer 10 80 -0.141 0.000 2.769 0.163 0.4 Dreyer 20 80 0.409 0.500 2.611 0.138 0.0319 Dreyer 40 80 1.407 1.000 3.014 0.075 2.16e-06

44

<!-- page 45 -->

Dataset Labels N Mean Median SD Decline fraction Raw p

PhysioNet 5 103 0.947 0.538 3.173 0.107 0.00219 PhysioNet 10 103 1.119 0.909 3.236 0.117 0.00019 PhysioNet 20 103 1.249 0.985 3.339 0.097 0.000244

## S8.4 Prespecified family inventory

Table S18: Cross-model scope of the specified evaluation families.

Family Current evidence and status

Source and structure audits Completed source and input/adapter audits; source overlap remains visible. Lee full- channel extension remains unexecuted. Engineering and formal entry Saved loading, freezing, selection, prediction, and source checks completed; engineering checks alone are not performance evidence. Resource accounting Completed saved allocation audit includes unsuccessful cache work; shared multi-dataset training costs are counted once. G trajectories All completed new-model trajectories fail to establish the specified plateau; selected and run steps are listed below. Core specificity Both new models pass the original pooled gate; own-minus-G is separately reported. Core population and personal gains

Every model/dataset core comparison is present above; dataset-level tests remain descrip- tive. Core few-shot and consistency All prescribed label budgets and direction/stability labels are retained, including negative means. FiLM specificity extension Not executed; no negative result inferred. Rest-neighbor extension Not executed; original eligibility and correction rules remain specified. Task-neighbor extension Not executed; no rest-neighbor eligibility gate is imposed. External specificity / rest ex- tensions

Lee and BNCI not executed for the new models; CBraMod results do not fill these cells.

Meta-learning primary / sec- ondary extensions

Not executed; no cross-model meta-learning conclusion is drawn.

Population-training budget curves

All three complete-cohort curves are available; CBraMod includes one documented preci- sion exception. Initial failure and final results are separated in Supplementary Section S9.

## S8.5 New-model convergence records

Initial and selected counts refer to the recorded checkpoints; extra run counts include updates after the selected point. Every plateau field is false. These records do not establish the behavior of a fully trained population model.

Table S19: REVE and LaBraM continuation records. Selected and executed updates are distinguished; the stopping rule does not establish a joint plateau.

Model Fold Seed Initial Selected updates Extra run Stop Plateau

REVE 0 11 3000 1500 3500 Loss patience No REVE 0 23 3000 1500 3500 Loss patience No REVE 0 37 3000 250 2250 Loss patience No REVE 0 53 1000 1000 3000 Loss patience No REVE 0 71 3000 0 2000 Loss patience No REVE 1 11 3000 1250 3250 Loss patience No REVE 1 23 3000 750 2750 Loss patience No REVE 1 37 3000 250 2250 Loss patience No REVE 1 53 3000 750 2750 Loss patience No REVE 1 71 3000 250 2250 Loss patience No

45

<!-- page 46 -->

Model Fold Seed Initial Selected updates Extra run Stop Plateau

REVE 2 11 1000 250 2250 Loss patience No REVE 2 23 3000 0 2000 Loss patience No REVE 2 37 3000 750 2750 Loss patience No REVE 2 53 1000 750 2750 Loss patience No REVE 2 71 3000 500 2500 Loss patience No REVE 3 11 3000 0 2000 Loss patience No REVE 3 23 3000 1000 3000 Loss patience No REVE 3 37 1000 0 2000 Loss patience No REVE 3 53 3000 500 2500 Loss patience No REVE 3 71 3000 0 2000 Loss patience No REVE 4 11 3000 1750 3750 Loss patience No REVE 4 23 3000 2000 4000 Loss patience No REVE 4 37 3000 0 2000 Loss patience No REVE 4 53 3000 1250 3250 Loss patience No REVE 4 71 1000 0 2000 Loss patience No LaBraM 0 11 3000 750 2750 Loss patience No LaBraM 0 23 3000 750 2750 Loss patience No LaBraM 0 37 3000 0 2000 Loss patience No LaBraM 0 53 3000 500 2500 Loss patience No LaBraM 0 71 3000 0 2000 Loss patience No LaBraM 1 11 3000 1500 3500 Loss patience No LaBraM 1 23 1000 500 2500 Loss patience No LaBraM 1 37 3000 500 2500 Loss patience No LaBraM 1 53 3000 3500 5500 Loss patience No LaBraM 1 71 3000 1000 3000 Loss patience No LaBraM 2 11 3000 250 2250 Loss patience No LaBraM 2 23 3000 250 2250 Loss patience No LaBraM 2 37 1000 0 2000 Loss patience No LaBraM 2 53 3000 0 2000 Loss patience No LaBraM 2 71 3000 500 2500 Loss patience No LaBraM 3 11 3000 4500 6500 Loss patience No LaBraM 3 23 3000 500 2500 Loss patience No LaBraM 3 37 3000 2000 4000 Loss patience No LaBraM 3 53 3000 0 2000 Loss patience No LaBraM 3 71 3000 500 2500 Loss patience No LaBraM 4 11 1000 2250 3000 Update cap No LaBraM 4 23 3000 0 2000 Loss patience No LaBraM 4 37 3000 0 2000 Loss patience No LaBraM 4 53 3000 0 2000 Loss patience No LaBraM 4 71 3000 250 2250 Loss patience No

46

<!-- page 47 -->

## S9 Completed population-budget extension results

All three models cover the original subjects and seeds at each prescribed endpoint. CBraMod combines 24 original successful

runs and one documented rerun using the numerical-precision exception described in Methods. The initial failure remains

documented below. G denotes population mean BA in percent; Delta and U denote own-minus-G and own-minus-swapped in

pp. Parentheses contain between-subject SDs, after within-subject seed averaging.

## S9.1 CBraMod

Table S20: Completed CBraMod population-budget results. Population balanced accuracy is in percent; personal benefit and specificity are in percentage points.

Dataset Budget N G mean (SD) Delta mean (SD) Median U mean (SD) Median

PhysioNet 1x 103 80.99 (11.70) 1.63 (4.59) 0.985 2.55 (4.35) 1.871 PhysioNet 2x 103 81.02 (11.88) 0.94 (5.15) 0.758 2.26 (4.53) 1.932 PhysioNet 4x 103 80.98 (11.57) 0.76 (4.55) 0.227 2.03 (3.91) 1.742 Dreyer 1x 80 80.37 (8.46) 3.58 (2.99) 3.292 5.28 (2.94) 4.892 Dreyer 2x 80 82.18 (8.30) 2.93 (2.93) 2.500 4.71 (3.03) 4.442 Dreyer 4x 80 82.21 (8.42) 3.09 (3.10) 2.333 4.33 (2.95) 3.975 Cho 1x 52 64.16 (15.05) 5.13 (8.10) 3.500 6.43 (8.49) 4.300 Cho 2x 52 65.51 (15.16) 4.82 (8.71) 1.500 6.48 (8.25) 5.213 Cho 4x 52 66.76 (14.48) 4.26 (7.18) 2.500 6.23 (7.54) 3.980 Pooled 1x 235 77.06 (13.44) 3.07 (5.34) 2.600 4.34 (5.44) 3.533 Pooled 2x 235 77.98 (13.40) 2.48 (5.77) 1.600 4.03 (5.45) 3.400 Pooled 4x 235 78.25 (12.88) 2.33 (5.06) 2.000 3.74 (4.98) 3.233

## S9.2 REVE

Table S21: Completed REVE population-budget results. Population balanced accuracy is in percent; personal benefit and specificity are in percentage points.

Dataset Budget N G mean (SD) Delta mean (SD) Median U mean (SD) Median

PhysioNet 1x 103 84.71 (11.20) 1.55 (3.32) 0.985 2.59 (3.05) 2.386 PhysioNet 2x 103 84.87 (10.79) 1.19 (3.59) 0.769 2.26 (3.33) 1.769 PhysioNet 4x 103 82.56 (10.97) 0.18 (2.80) 0.000 1.42 (3.08) 1.288 Dreyer 1x 80 83.91 (8.37) 5.38 (4.73) 4.667 7.25 (4.91) 6.775 Dreyer 2x 80 85.75 (7.65) 4.09 (3.93) 3.583 6.51 (4.56) 5.642 Dreyer 4x 80 82.70 (8.34) 3.16 (3.71) 1.750 4.74 (4.02) 3.792 Cho 1x 52 69.77 (13.63) 3.35 (4.47) 2.600 4.38 (4.56) 3.480 Cho 2x 52 69.68 (13.84) 3.99 (5.24) 2.200 4.15 (5.33) 2.640 Cho 4x 52 69.90 (12.59) 2.39 (4.10) 1.100 2.95 (3.68) 2.230 Pooled 1x 235 81.13 (12.48) 3.25 (4.42) 2.424 4.58 (4.57) 3.500 Pooled 2x 235 81.80 (12.43) 2.80 (4.34) 1.833 4.12 (4.64) 3.100 Pooled 4x 235 79.81 (11.77) 1.68 (3.69) 1.000 2.89 (3.83) 2.240

## S9.3 LaBraM

Table S22: Completed LaBraM population-budget results. Population balanced accuracy is in percent; personal benefit and specificity are in percentage points.

Dataset Budget N G mean (SD) Delta mean (SD) Median U mean (SD) Median

PhysioNet 1x 103 82.29 (12.04) 1.52 (3.63) 0.909 2.35 (3.79) 2.091 PhysioNet 2x 103 82.78 (11.89) 1.10 (3.85) 0.909 2.27 (3.81) 2.030 PhysioNet 4x 103 82.48 (12.18) 1.21 (4.48) 0.303 2.53 (4.41) 2.129 Dreyer 1x 80 83.17 (8.06) 3.91 (3.79) 3.000 5.41 (3.70) 4.317

47

<!-- page 48 -->

Dataset Budget N G mean (SD) Delta mean (SD) Median U mean (SD) Median

Dreyer 2x 80 83.47 (8.42) 3.94 (3.68) 3.417 4.35 (3.30) 3.467 Dreyer 4x 80 84.34 (7.91) 3.30 (3.15) 2.543 4.05 (3.00) 3.283 Cho 1x 52 60.70 (15.03) 5.38 (6.45) 3.383 4.78 (6.31) 2.950 Cho 2x 52 62.18 (14.71) 5.39 (5.57) 4.200 4.81 (4.63) 3.580 Cho 4x 52 62.49 (14.78) 6.12 (6.40) 4.300 4.90 (5.72) 3.390 Pooled 1x 235 77.81 (14.77) 3.19 (4.70) 2.424 3.93 (4.64) 3.174 Pooled 2x 235 78.46 (14.44) 3.02 (4.58) 2.576 3.54 (4.00) 2.867 Pooled 4x 235 78.69 (14.45) 3.01 (4.96) 1.970 3.57 (4.43) 2.939

## S9.4 Prespecified interpretations and complete comparison inventory

No model meets the attenuation-to-negligible-gain rule. CBraMod meets the prespecified stable-positive-gain rule after contin- ued population training. REVE retains the descriptive classification. LaBraM also retains the descriptive classification. This numerical condition does not establish convergence, uniformity across datasets or behavior beyond the tested budgets. The following corrected p-values belong to the completed six-slot positive-gain family only. Completing CBraMod changes the REVE largest-budget adjusted p-value through the shared family; its raw results and medians are unchanged.

Table S23: Completed population-budget decision records with the original six-slot positive-gain correction.

Model Budget Six-slot Holm p Curve interpretation

REVE 2x 3.02e-21 Descriptive only REVE 4x 6.57e-13 Descriptive only LaBraM 2x 5.62e-20 Descriptive only LaBraM 4x 1.62e-20 Descriptive only CBraMod 2x 5.69e-12 Operational criterion met CBraMod 4x 6.57e-13 Operational criterion met

The table label “Operational criterion met” denotes the prespecified numerical rule across the pooled doubled and quadru- pled endpoints; it is not a statistical demonstration of curve stability or model convergence. All recorded dataset-level and pooled comparisons follow. The budget-extension specificity correction and diagnostic apply to the pooled rows; dataset-level p-values remain descriptive. At each model and budget, the family contains the observed LoRA test and two unexecuted variant slots assigned unit p-values. CBraMod W instead uses its observed FiLM comparison in the three-slot family. Consequently, the original W and budget-extension adjusted p-values are distinct records even at the reference budget; neither overwrites the other. Decline columns are subject fractions losing more than two pp. These comparisons supplement, and do not replace, the comparison inventory.

Table S24: All completed population-budget comparisons. Difference columns are in percentage points; decline columns are subject fractions.

Model Dataset Budget Delta raw p U raw p U budget Holm Delta decline U decline

REVE Cho 1x 1.27e-08 2.57e-10 – 0.000 0.000 REVE Dreyer 1x 6.75e-14 4.39e-15 – 0.013 0.000 REVE PhysioNet 1x 1.26e-05 1.54e-13 – 0.107 0.029 REVE Pooled 1x 2.1e-24 4.6e-36 1.38e-35 0.051 0.013 REVE Cho 2x 2.31e-09 4.32e-09 – 0.000 0.000 REVE Dreyer 2x 2.31e-13 3.92e-15 – 0.013 0.000 REVE PhysioNet 2x 0.000385 9.1e-11 – 0.097 0.058 REVE Pooled 2x 5.03e-22 4.36e-33 1.31e-32 0.047 0.026 REVE Cho 4x 5.98e-06 1.75e-08 – 0.019 0.000 REVE Dreyer 4x 5.07e-14 3.92e-15 – 0.000 0.000 REVE PhysioNet 4x 0.192 5.62e-07 – 0.155 0.078 REVE Pooled 4x 3.2e-13 4.09e-28 1.23e-27 0.072 0.034 LaBraM Cho 1x 1.12e-09 7.77e-09 – 0.000 0.019 LaBraM Dreyer 1x 1.26e-13 3.92e-15 – 0.013 0.000 LaBraM PhysioNet 1x 5.53e-05 1.72e-08 – 0.136 0.136 LaBraM Pooled 1x 3.66e-24 3.96e-30 1.19e-29 0.064 0.064 LaBraM Cho 2x 9.2e-10 2.63e-10 – 0.019 0.000 LaBraM Dreyer 2x 4.62e-14 7.17e-15 – 0.000 0.000 LaBraM PhysioNet 2x 0.00348 2.01e-08 – 0.233 0.136 LaBraM Pooled 2x 1.4e-20 9.01e-30 2.7e-29 0.106 0.060 LaBraM Cho 4x 8.8e-10 8.98e-10 – 0.019 0.000

48

<!-- page 49 -->

Model Dataset Budget Delta raw p U raw p U budget Holm Delta decline U decline

LaBraM Dreyer 4x 1.29e-14 3.92e-15 – 0.000 0.000 LaBraM PhysioNet 4x 0.0101 1.36e-08 – 0.155 0.107 LaBraM Pooled 4x 3.24e-21 8.38e-30 2.51e-29 0.072 0.047 CBraMod Cho 1x 1.18e-06 5.23e-08 – 0.096 0.077 CBraMod Dreyer 1x 1.49e-13 3.92e-15 – 0.000 0.000 CBraMod PhysioNet 1x 0.000734 5.74e-08 – 0.204 0.136 CBraMod Pooled 1x 3.68e-18 1.58e-28 4.73e-28 0.111 0.077 CBraMod Cho 2x 1.51e-05 1.16e-08 – 0.077 0.038 CBraMod Dreyer 2x 5.52e-12 1.12e-14 – 0.037 0.013 CBraMod PhysioNet 2x 0.0713 2.09e-06 – 0.272 0.146 CBraMod Pooled 2x 5.69e-12 3.2e-26 9.59e-26 0.149 0.077 CBraMod Cho 4x 7.08e-07 4.57e-09 – 0.077 0.038 CBraMod Dreyer 4x 2.56e-12 9.14e-15 – 0.013 0.000 CBraMod PhysioNet 4x 0.0638 1.37e-06 – 0.233 0.146 CBraMod Pooled 4x 2.19e-13 1.17e-26 3.52e-26 0.123 0.072

## S9.5 Validation behavior alongside the test curves

Each endpoint summary below weights the recorded fold/seed runs equally. Within a run, validation subjects are weighted equally. The parenthesized SD is across runs and is not an uncertainty estimate based on independent validation cohorts. CE denotes cross-entropy. The completed runs end at their budget caps without satisfying the joint plateau. REVE’s deteriorating population score is therefore reported alongside its remaining personal contrast, rather than interpreted as a fully trained strong reference.

Table S25: Validation performance at each completed population-budget endpoint. Run-level means and standard deviations use equal fold/seed weights.

Model Dataset Budget CE mean (SD) Accuracy % (SD) BA % (SD)

CBraMod Cho 1x 0.714 (0.145) 64.117 (6.690) 64.117 (6.690) CBraMod Dreyer 1x 0.531 (0.162) 81.178 (2.943) 81.178 (2.943) CBraMod PhysioNet 1x 0.839 (0.213) 81.957 (3.430) 82.013 (3.449) CBraMod Pooled 1x 0.709 (0.129) 77.733 (2.681) 77.758 (2.693) CBraMod Cho 2x 0.827 (0.224) 65.407 (5.218) 65.407 (5.218) CBraMod Dreyer 2x 0.643 (0.123) 82.239 (2.116) 82.239 (2.116) CBraMod PhysioNet 2x 1.402 (0.469) 80.848 (3.561) 80.887 (3.550) CBraMod Pooled 2x 1.021 (0.209) 77.880 (2.380) 77.898 (2.400) CBraMod Cho 4x 0.918 (0.230) 67.245 (4.812) 67.245 (4.812) CBraMod Dreyer 4x 0.957 (0.221) 82.283 (2.436) 82.283 (2.436) CBraMod PhysioNet 4x 2.037 (0.763) 80.457 (3.664) 80.442 (3.729) CBraMod Pooled 4x 1.428 (0.364) 78.130 (2.557) 78.123 (2.582) LaBraM Cho 1x 0.684 (0.117) 61.610 (4.233) 61.610 (4.233) LaBraM Dreyer 1x 0.467 (0.063) 83.667 (2.239) 83.667 (2.239) LaBraM PhysioNet 1x 0.703 (0.259) 83.891 (3.669) 83.732 (3.736) LaBraM Pooled 1x 0.620 (0.122) 78.865 (2.463) 78.794 (2.484) LaBraM Cho 2x 0.914 (0.411) 61.953 (4.674) 61.953 (4.674) LaBraM Dreyer 2x 0.618 (0.245) 83.439 (3.899) 83.439 (3.899) LaBraM PhysioNet 2x 1.149 (0.366) 83.543 (3.955) 83.516 (3.998) LaBraM Pooled 2x 0.920 (0.245) 78.711 (2.549) 78.699 (2.569) LaBraM Cho 4x 1.058 (0.518) 62.050 (5.148) 62.050 (5.148) LaBraM Dreyer 4x 0.759 (0.227) 84.561 (1.816) 84.561 (1.816) LaBraM PhysioNet 4x 1.522 (0.629) 82.804 (3.594) 82.726 (3.680) LaBraM Pooled 4x 1.165 (0.378) 78.778 (2.254) 78.743 (2.286) REVE Cho 1x 1.055 (0.573) 68.463 (5.779) 68.463 (5.779) REVE Dreyer 1x 0.374 (0.111) 84.944 (8.015) 84.944 (8.015) REVE PhysioNet 1x 0.506 (0.155) 86.239 (7.605) 86.125 (8.201) REVE Pooled 1x 0.584 (0.178) 81.857 (6.691) 81.807 (6.959) REVE Cho 2x 1.448 (0.822) 68.053 (5.640) 68.053 (5.640) REVE Dreyer 2x 0.438 (0.149) 85.989 (8.125) 85.989 (8.125) REVE PhysioNet 2x 0.875 (0.428) 85.587 (7.591) 85.345 (8.174) REVE Pooled 2x 0.857 (0.353) 81.825 (6.664) 81.717 (6.932) REVE Cho 4x 1.982 (1.237) 67.942 (7.103) 67.942 (7.103) REVE Dreyer 4x 0.601 (0.273) 83.178 (12.687) 83.178 (12.687) REVE PhysioNet 4x 1.068 (0.389) 82.717 (11.940) 82.387 (12.605) REVE Pooled 4x 1.115 (0.429) 79.587 (10.388) 79.440 (10.684)

49

<!-- page 50 -->

1× 2× 4×

65

70

75

80

Mean population BA (%)

A  CBraMod

1× 2× 4×

0

1

2

3

Median own − G (pp)

B  CBraMod

1× 2× 4×

0

2

4

Median own − swapped (pp)

C  CBraMod

1× 2× 4×

70

75

80

85

Mean population BA (%)

D  REVE

1× 2× 4×

0

2

4

Median own − G (pp)

E  REVE

1× 2× 4×

0

2

4

6

Median own − swapped (pp)

F  REVE

1× 2× 4×

Population update budget

60

70

80

Mean population BA (%)

G  LaBraM

1× 2× 4×

Population update budget

0

2

4

Median own − G (pp)

H  LaBraM

1× 2× 4×

Population update budget

0

2

4

Median own − swapped (pp)

I  LaBraM

PhysioNet Dreyer Cho Pooled

Figure S13: Population performance and dataset-specific budget curves. Each model row shows mean population BA, median own-minus- G and median own-minus-swapped. Solid curves show individual datasets; the dashed curve pools the subjects after within-subject seed averaging. Lines join the tested budgets. REVE’s PhysioNet personal-gain median reaches zero at the largest budget; LaBraM’s Cho median increases, showing that the pooled net reduction is not universal across datasets.

50

<!-- page 51 -->

## S9.6 Initial CBraMod failure, missingness and run-level record

The following tables preserve the initial batch before its documented rerun; they are not the completed-cohort tables above. At each budget the original 235 subjects and 5 seeds form the intended denominator. Initially, 1127 subject–seed pairs were observed; 187 subjects had all seeds and 48 lacked a seed. No complete-case subset was substituted. The retry subsequently supplies that trajectory’s personal diagnostics under the disclosed precision exception. The original-budget cross-model result remains a separate analysis.

Table S26: Subject and seed coverage in the initial CBraMod budget batch before the documented rerun.

Budget Dataset N Seeds Planned pairs Observed pairs Complete N Incomplete N

1x PhysioNet 103 5 515 494 82 21 1x Dreyer 80 5 400 384 64 16 1x Cho 52 5 260 249 41 11 1x Pooled 235 5 1175 1127 187 48 2x PhysioNet 103 5 515 494 82 21 2x Dreyer 80 5 400 384 64 16 2x Cho 52 5 260 249 41 11 2x Pooled 235 5 1175 1127 187 48 4x PhysioNet 103 5 515 494 82 21 4x Dreyer 80 5 400 384 64 16 4x Cho 52 5 260 249 41 11 4x Pooled 235 5 1175 1127 187 48

The following rows describe each run’s test fold separately. Fold and seed are execution identifiers, not extra independent subjects. N is the saved observed-subject count; G is a mean percentage, while Delta and U are within-run subject medians in pp. These rows do not estimate the seed-averaged complete-cohort medians in the main figure. Missing personal diagnostics remain NA, including at preserved earlier population checkpoints of the failed run. Machine-readable source tables retain the dataset-level means, SDs and medians as well.

Table S27: Initial CBraMod budget results by fold and seed. Missing personal diagnostics remain unavailable.

Fold Seed Budget Status N G mean Delta median U median

0 11 1x complete 48 75.774 4.083 5.208 0 11 2x complete 48 77.521 4.083 5.483 0 11 4x complete 48 77.868 2.083 3.826 0 23 1x complete 48 76.888 3.750 5.958 0 23 2x complete 48 78.172 0.833 4.178 0 23 4x complete 48 77.488 3.894 5.140 0 37 1x complete 48 76.705 3.923 4.866 0 37 2x complete 48 77.339 0.994 1.483 0 37 4x complete 48 77.990 1.833 4.271 0 53 1x complete 48 75.920 4.167 5.542 0 53 2x complete 48 77.560 3.333 5.800 0 53 4x complete 48 77.657 4.083 4.110 0 71 1x complete 48 75.659 3.167 5.042 0 71 2x complete 48 77.690 1.250 4.746 0 71 4x complete 48 76.926 1.833 4.792 1 11 1x complete 48 78.713 2.917 3.970 1 11 2x complete 48 78.853 3.817 3.458 1 11 4x complete 48 80.059 0.917 3.125 1 23 1x complete 48 78.143 0.000 1.487 1 23 2x complete 48 78.560 0.833 3.267 1 23 4x complete 48 78.178 3.000 3.341 1 37 1x failed 0 NA NA NA 1 37 2x failed 0 NA NA NA 1 37 4x failed 0 NA NA NA 1 53 1x complete 48 78.063 0.917 2.250 1 53 2x complete 48 79.627 1.667 4.023 1 53 4x complete 48 77.768 1.667 2.542 1 71 1x complete 48 75.711 4.545 5.119 1 71 2x complete 48 78.815 2.500 2.250 1 71 4x complete 48 80.295 0.000 1.792 2 11 1x complete 47 75.754 1.667 4.700 2 11 2x complete 47 75.693 2.500 4.886

51

<!-- page 52 -->

Fold Seed Budget Status N G mean Delta median U median

2 11 4x complete 47 75.658 3.333 3.068 2 23 1x complete 47 73.422 3.788 5.152 2 23 2x complete 47 74.153 4.167 4.250 2 23 4x complete 47 74.454 3.333 3.000 2 37 1x complete 47 73.172 2.586 4.083 2 37 2x complete 47 73.082 2.500 4.250 2 37 4x complete 47 73.613 3.448 3.417 2 53 1x complete 47 74.275 5.000 5.917 2 53 2x complete 47 75.975 2.500 4.250 2 53 4x complete 47 75.612 2.500 5.583 2 71 1x complete 47 73.086 3.448 5.492 2 71 2x complete 47 74.338 0.862 2.750 2 71 4x complete 47 74.235 2.500 2.083 3 11 1x complete 46 76.578 0.000 3.250 3 11 2x complete 46 77.722 0.833 2.394 3 11 4x complete 46 77.555 1.000 1.417 3 23 1x complete 46 77.168 1.667 3.840 3 23 2x complete 46 78.387 1.000 2.128 3 23 4x complete 46 77.600 2.250 2.238 3 37 1x complete 46 78.071 1.827 3.592 3 37 2x complete 46 77.688 0.000 3.250 3 37 4x complete 46 78.948 0.917 3.667 3 53 1x complete 46 78.243 1.667 2.000 3 53 2x complete 46 78.116 1.000 3.200 3 53 4x complete 46 79.803 0.000 4.408 3 71 1x complete 46 77.732 2.917 2.148 3 71 2x complete 46 79.036 1.250 3.038 3 71 4x complete 46 79.119 0.833 2.583 4 11 1x complete 46 79.994 2.250 3.208 4 11 2x complete 46 80.267 1.333 4.178 4 11 4x complete 46 80.653 2.500 3.080 4 23 1x complete 46 82.435 1.250 2.958 4 23 2x complete 46 82.390 1.000 3.292 4 23 4x complete 46 82.538 0.189 1.614 4 37 1x complete 46 80.989 1.212 2.242 4 37 2x complete 46 81.150 0.833 3.333 4 37 4x complete 46 82.048 1.250 3.027 4 53 1x complete 46 82.204 0.833 3.558 4 53 2x complete 46 82.354 0.795 2.352 4 53 4x complete 46 81.556 0.000 3.333 4 71 1x complete 46 75.650 0.917 1.382 4 71 2x complete 46 77.061 3.705 4.803 4 71 4x complete 46 79.482 3.333 4.550

The failed run’s saved validation observations are retained below; no later endpoint is filled. Its population-training objective became nonfinite before backpropagation; personal selection and scoring were scheduled after population continuation and had not begun. The budget evaluation also records a reference-path discrepancy in CBraMod: one saved population hard prediction differs from its original-budget counterpart, while its personal and exchanged predictions are unchanged. For the affected subject–seed comparison, G increases by 4.17 pp and own-minus-G decreases by the same amount; own-minus-swapped is unchanged. The source parameters are unchanged, and the precise numerical cause is not identified. The extension uses its matched scoring path and preserves the original-budget scores separately; it does not replace missing personal diagnostics with original-budget values.

Table S28: Available validation observations from the failed initial CBraMod run. Later endpoints are not filled.

Fold Seed Budget Dataset CE Accuracy (%) BA (%)

1 37 1x Cho 0.5447 66.50 66.50 1 37 1x Dreyer 0.5782 79.44 79.44 1 37 1x PhysioNet 1.0935 79.35 79.11 1 37 1x Pooled 0.7998 76.52 76.42 1 37 2x Cho 1.1068 67.00 67.00 1 37 2x Dreyer 0.5750 82.64 82.64 1 37 2x PhysioNet 1.8851 79.89 79.78 1 37 2x Pooled 1.2754 77.94 77.89

52

<!-- page 53 -->

The initial six-slot correction is retained below to distinguish its unavailable observations from the final observed endpoints. These adjusted p-values describe the incomplete-run analysis; the completed family’s correction is reported above.

Table S29: Initial incomplete-batch budget decisions and their original six-slot correction, separate from the completed analysis.

Model Budget Initial six-slot Holm p Initial interpretation

REVE 2x 3.02e-21 Descriptive only REVE 4x 9.6e-13 Descriptive only LaBraM 2x 5.62e-20 Descriptive only LaBraM 4x 1.62e-20 Descriptive only CBraMod 2x NA Incomplete cohort CBraMod 4x NA Incomplete cohort

The retry changes three hard predictions in its original-budget comparison with the original scoring path. G and own BA

are unchanged; the maximum absolute swapped-BA difference for one subject and seed is 0.30 pp. These differences are

not averaged away or used to revise the original-budget W/X1 results. The final CBraMod curve combines the retry with the

original successful trajectories and does not isolate a causal precision effect.

## S9.7 Recorded numerical events in the meta-learning runs

The formal run manifests record 6 inner-loop divergences across 3 of 25 runs. The table lists the original counters by support- label count. A counter is an inner-loop event, not a distinct affected test subject or a confirmed chance-valued test score. The saved aggregate manifest does not identify each event’s method and execution phase. The original scores and failure-handling policy remain unchanged; a per-method attribution and an assessment of its effect remain unresolved.

Table S30: Recorded inner-loop numerical events by fold, seed and support-label count. Counts are events, not affected subjects.

Fold Seed All recorded events Five labels Ten labels Twenty labels

0 11 0 0 0 0 0 23 0 0 0 0 0 37 0 0 0 0 0 53 0 0 0 0 0 71 0 0 0 0 1 11 0 0 0 0 1 23 0 0 0 0 1 37 0 0 0 0 1 53 0 0 0 0 1 71 0 0 0 0 2 11 1 1 0 0 2 23 1 0 0 1 2 37 0 0 0 0 2 53 0 0 0 0 2 71 0 0 0 0 3 11 0 0 0 0 3 23 0 0 0 0 3 37 0 0 0 0 3 53 0 0 0 0 3 71 0 0 0 0 4 11 0 0 0 0 4 23 0 0 0 0 4 37 0 0 0 0 4 53 0 0 0 0 4 71 4 2 1 1

The query-informed R1 control uses test-pool query scores when selecting priors for validation subjects. Its original end-

point and secondary decisions in the comparison inventory therefore describe this query-informed procedure. They are not

independent confirmation under test-label isolation. The separate M-minus-R2 results do not use this R1 branch.

53

<!-- page 54 -->

## S10 Supplementary Methods

Implementation details and stage-specific decision rules complement the main Methods.

## S10.1 Decision rules and interpretation

The study proceeded through successive stages with rules fixed before their respective results. These stage-specific rules do

not constitute a single independently preregistered confirmatory design. Original decisions are preserved, including stopped

extensions and failed gates. Directional tests use the saved paired Wilcoxon procedures and their original Holm families;

descriptive comparisons retain their original status. The budget extension has its separately prespecified correction family,

described below.

The contextual-model criterion jointly required corrected superiority to shuffled context and the task head, recovery of

at least thirty percent of the mean supervised-reference gain, and no more than ten percent of subjects declining by over two

percentage points. The own-versus-swapped diagnostic required a median specificity difference of at least two percentage points

and its corrected directional test. The prior-based meta-learning endpoint and its information-access problem are described in

Supplementary Section S7; the main comparison uses ordinary continuation. The original rules and decision summaries appear

in Supplementary Section S4; Supplementary Data 1 supplies the complete comparison records.

## S10.2 CBraMod implementation and selection

## S10.2.1 Shared and personal parameterization

The following implementation details concern CBraMod. The REVE and LaBraM implementation appears in Supplementary

Section S10.3; their complete results appear in Supplementary Section S8. The task head reads compatible channel repre-

sentations from the frozen backbone. In the contextual FiLM family, a context encoder and generator output bounded affine

modulation across encoder layers. The LoRA family produces mixture weights over shared low-rank bases applied to query,

key, value, and output projections in spatial and temporal attention. Context combines backbone embeddings with covari-

ance tangent-space features; the tangent reference is estimated from training-subject segments. Dimension-normalized feature

blocks define Euclidean distance for donor selection. The frozen grids in the supplement specify ranks, dimensions, bands, and

regularization.

For contextual training, a source-subject episode has ordinary cross-entropy ℓ(cs) and, when context is retained, a mismatch

margin term:

L = ℓ(cs) + λ max{0, ℓ(cs) −ℓ(cd) + m}. (S1)

The donor context is from another source-training subject in the same dataset. Default-context dropout episodes use the or-

dinary term without an identity margin. Validation selection uses the prespecified ordering of median improvement, mean

improvement, and fixed tie-breaks. The zero-margin-weight diagnostic is kept in the full comparison tables.

Personal FiLM adds zero-initialized offsets to the default generated modulation. Personal LoRA adds a zero-initialized

weight update while shared bases, mixture weights, head, and backbone remain fixed. FiLM-on-LoRA continuation uses the

explicitly allowed FiLM-on-LoRA path, explaining the family difference in Supplementary Figure S6. The full-support and

few-shot AdamW grids are selected on validation subjects. For each target and training run, full-support exchange draws ten

other subjects uniformly with replacement from the same dataset and held-out fold. The donor generator is initialized with the

run seed; draws can vary across seeds, and the budget extension reuses the recorded donor list at every endpoint. Donor BA

scores are averaged within a run before averaging seeds within each target. A singleton eligible donor is therefore repeated.

54

<!-- page 55 -->

When no eligible donor exists, the exchange result is missing. For multi-donor LoRA transfer, weight updates are averaged,

not factor matrices independently.

## S10.2.2 Continuation and meta-learning

The population model continues the contextual training procedure with the selected hyperparameters and an optimizer restart.

Validation-subject mean cross-entropy is checked every 250 updates. Patience is eight checks with the fixed minimum im-

provement, and the minimum-loss checkpoint includes the original start. The continuation cap is proportional to each start’s

selected training budget. A separate loss-range rule describes a plateau; early stopping and a plateau are different events. The

supplementary run-level flags show that joint train/validation plateaus were not established.

The initial population LoRA model is the shared starting point. Ordinary continuation trains it with cross-entropy and fixed

default mixture weights. First-order MAML uses the recorded first-order meta-learning procedure [18]; the learned-rate variant

additionally learns layer-specific inner learning rates. Meta-training uses source subjects only. Evaluation uses the same full-

batch SGD support updates for all compared methods, with inner settings chosen on validation subjects. Each meta-learning and

ordinary-continuation training run executes the saved outer-update budget; meta-learning additionally computes the support-set

updates. The inner loop updates only personal LoRA, treating support-loss gradients as constants. Query-loss backpropagation

updates the shared LoRA bases and task head while treating the fitted personal weights as fixed, without differentiating through

support updates. In the learned-rate variant, a layer’s log-rate gradient is minus its rate multiplied by the dot product of the

query gradient on its personal parameters and its accumulated support gradients. The resulting wall time and gradient/sample

counts need not match ordinary continuation.

Following divergence in the initial inner-rate scan, the formal runs used a fixed handling rule: stop a divergent adaptation,

assign chance-level scores at unreached update counts, record the event, and skip divergent meta episodes. The 25 formal run

manifests record 6 inner-loop divergences across 3 runs. These counters combine calls across training, validation and evalua-

tion; the manifest does not retain complete event-to-method, phase or subject assignments. Skipping a meta-training episode

also skips its optimizer update. The matching therefore specifies scheduled outer-update budgets; equal counts of successful

updates cannot be independently verified from these aggregate records. Supplementary Section S9.7 lists the saved counts. The

reported results include this failure-handling policy; its effect has not been isolated. Validation accuracy trajectories for the

continued population model were not saved, so the direction of accuracy at its selected stopping point cannot be reconstructed

from loss alone.

## S10.3 REVE and LaBraM implementation

The cross-model core uses the base pretrained REVE and LaBraM encoders, with their frozen normalization and position

parameters. REVE uses the base pretrained weights rather than task-finetuned weights [19]. CBraMod and LaBraM use

their original published architectures [20, 21]. FiLM, LoRA, and the permutation-invariant set encoder follow their respective

method families [22–24].

Both models receive native EEG channels. REVE follows the fixed public motor-imagery input route: average reference,

the recorded high-pass and mains-notch filters, resampling and microvolt scaling. LaBraM is reprocessed from raw data using

its recorded band-pass and notch filters. Supplementary Table S11 gives the numerical settings. No signal z-scoring or target-

query normalization is added. REVE keeps its overlapping patch extraction without tail padding; therefore some trailing input

samples are not represented by tokens. LaBraM uses nonoverlapping patches, retains the pretrained norm and reads EEG patch

tokens instead of the class token. Final tokens are averaged over time within each channel and the common channel readout is

flattened. Feature normalization is fitted on the task head training subjects and retained for population and personal models.

55

<!-- page 56 -->

Each attention layer receives independent low-rank updates to query, key, value and output projections. The low-rank

factors are initialized with a random input factor and a zero output factor, producing a zero initial weight increment. Only the

population adapter and task head are trained for the shared model. Personal fitting adds a separate zero-increment adapter with

the backbone, the continued population model and head frozen. The parameter rank, scaling and optimizer grids are specified

in Supplementary Table S11.

Task-head selection compares linear and multilayer heads using validation-subject mean BA and the specified tie-breaks.

Initial shared-adapter candidates are ranked by validation gain median, then mean, followed by update and learning-rate tie-

breaks. Population continuation trains only the selected candidate, restoring optimizer and random-number state. Validation-

subject mean cross-entropy selects the continuation checkpoint, including the initial point and choosing the earlier point for ties.

The loss-based stopping criterion and separate plateau rules do not expand the candidate set or use target-query performance.

Full-support and few-shot personal grids likewise use validation subjects. REVE/LaBraM population models use an ordinary

shared LoRA with cross-entropy, whereas CBraMod uses shared bases learned through contextual training. This difference and

the native input pipelines constrain attribution of between-model performance differences.

## S10.4 Correction families and descriptive rules

The contextual gate corrects across both methods and both designated controls. The specificity gate retains the original three-

variant family. An unexecuted variant has an unavailable observed result but reserves a unit-p correction slot; it is not counted

as a measured failure. For the new models, only LoRA is executed in that family. Rest-neighbor testing is conditional on the

original specificity eligibility gate; task-neighbor comparisons retain their separate two-variant family. Secondary multi-donor

results remain explicitly exploratory and do not replace the primary single-donor decision.

Cross-model consistency is descriptive: a direction label reflects the mean contrast in each dataset. Few-shot stability

requires nonnegative means at every prescribed label budget and no decreases with increasing budget. Neither rule asserts that

every subject improves or creates a new significance threshold. The full-support fit is an empirical reference within the tested

family and current population-training budgets, rather than an optimized upper bound over all possible adaptations. Missing

label budgets, absent donors and unexecuted methods remain missing. BNCI own-minus-population and own-minus-swapped

have different eligible populations, and their aggregate means are not subtracted to manufacture another contrast.

The symmetry and independent-pair interpretation of signed-rank tests is limited by shared fitted models and donor reuse.

## S10.5 Euclidean alignment implementation

The CBraMod alignment diagnostics whiten native multichannel signals using the recorded covariance reference and diagonal

shrinkage, then pass the whitened signals directly to the frozen encoder. Rest-only and eyes-open-matched variants use their

named rest sources; the all-task variant can access unlabeled target queries and is transductive. Whitening is applied to the

stored microvolt-scaled signals. The alignment and unaligned activation-precision paths differ, so spatial mixing is not isolated.

The numerical settings appear in Supplementary Table S11; all saved comparisons remain in the supplementary inventory.

## S10.6 Population-budget endpoints and interpretation rules

The extension starts from each run’s originally reported population checkpoint. Its cumulative selected population-update

count defines the reference budget; subsequent endpoints are the states at twice and four times that count. The existing training

objective, learning rate and sampling procedure are retained. REVE and LaBraM restore their saved optimizer and random-

number states. CBraMod’s original checkpoint lacks those states, so its continuation restarts them using the original settings.

Endpoint states are used directly, without selecting a better checkpoint from the interval. Runs stop at the first joint plateau

56

<!-- page 57 -->

or the specified cap; nonfinite objectives stop a run and leave subsequent endpoints missing. Validation deterioration does not

trigger substitution of an earlier checkpoint.

The joint plateau uses the recorded equally spaced check window: training and validation CE ranges must satisfy their

relative and absolute tolerances, validation accuracy and BA must satisfy the range tolerance, and neither validation score may

achieve the specified running-best improvement. Supplementary Table S11 gives these thresholds. At each new endpoint,

the personal LoRA settings are selected again on validation subjects using the original grid, then evaluated using the original

donor assignments. The reference endpoint reuses its original personal fit and selection. The core table retains original-budget

scoring, whereas the budget curves use extension-reference scoring. Recorded precision-path and reference-scoring differ-

ences can therefore produce small differences between their original-budget summaries; Supplementary Section S9 documents

them. Budget changes are evaluated within the extension scoring path. Label budgets and few-shot curves are not reselected.

Complete-cohort contrasts require all original subjects and seeds; no seed deletion, original-budget score substitution or chance-

score imputation is applied to this extension.

One original CBraMod trajectory stopped on a nonfinite objective before backpropagation and before personal diagnostics,

despite retaining earlier population checkpoints. A single retry was registered after that failure: remove the eighth-layer acti-

vation’s half-precision round trip, retain float32 and disable TF32, while preserving the original population gradient clipping

and other settings. Its successful results replace that failed trajectory in the complete-cohort aggregation; the original failure,

incomplete-cohort summaries and validation observations remain in Supplementary Section S9.6 (Tables S26, S27, S28 and

S29). CBraMod therefore combines 24 original trajectories and one precision exception. Successful completion does not es-

tablish the original failure’s root cause. Original-path and retry-path prediction differences, along with their scoring effects, are

documented in Supplementary Section S9.

The interpretation rules use the pooled median own-minus-population after averaging seeds within subject. Let these

medians at the original, doubled and quadrupled budgets be ma, mb, mc. The attenuation-to-negligible-gain rule requires ma ≥

mb ≥mc, at least one strict decrease, and mc < 0.5 pp. Otherwise, the stable-positive-gain rule requires |mc −mb| < 0.5 pp,

positive mb, mc, and positive directional tests at both added endpoints. This is the prespecified criterion for a stable positive

personal gain after population continuation; its scope is the two observed added endpoints. The latter tests use the prespecified

six-slot Holm family spanning the models and added endpoints. Initially missing slots reserved unit p-values for correction;

the completed retry supplies their observed values in the same family. The initial correction record is retained separately. All

remaining complete cases are descriptive; incomplete subject/seed coverage leaves the interpretation undetermined. Specificity

uses a separate three-slot family at each model and endpoint: the observed LoRA comparison and two unexecuted variant slots

with unit p-values. This budget-extension family differs from the CBraMod specificity family, which includes the observed

FiLM test. The original specificity adjusted p-value is retained separately. These rules do not replace original decision families,

establish convergence or identify a pure causal effect of compute.

## S10.7 Screening procedures and scope of Cho timeline checks

Subject exclusions. PhysioNet excludes subjects 88, 89, 92, 100, 104 and 106 because of sampling-rate or run-duration

anomalies. Dreyer excludes subjects 4, 9, 17, 29, 41, 78 and 79 according to the original authors’ annotations. All Cho subjects

are included. These dataset-specific subject exclusions are distinct from trial screening.

Trial screening and diagnostic checks. Initial automated screening applied amplitude rejection and a post-screening class-

imbalance stopping rule, and triggered a stop. The revised procedure retained all finite-valued trials and removed these two

criteria; the initial screening outcomes remain in the released records. Alpha-power checks are diagnostic and do not retro-

spectively remove subjects. Dreyer lacks the required occipital channels for that diagnostic, and Cho lacks the corresponding

57

<!-- page 58 -->

closed-eye segment. These checks did not replace the dataset-specific exclusion criteria.

Cho ordering and verification scope. The official trial-order metadata were checked for all included Cho subjects. In-

dependent signal-level and packaged-event cross-checks covered subject s01. The within-class packaged events are not an

independent record of the original continuous timeline, so these checks do not reconstruct every subject’s continuous recording

or establish the absolute rest-to-task interval. The evaluation uses the available trial-order metadata to order the task trials.

BNCI task-preceding eyes-open rest was verified from raw-event records and aligned task data. Expert-flagged trials are

included under the study protocol.

## References

[1] He He and Dongrui Wu. Transfer Learning for Brain-Computer Interfaces: A Euclidean Space Data Alignment Approach,

2020. URL https://doi.org/10.1109/TBME.2019.2913914.

[2] Bruna Junqueira, Bruno Aristimunha, Sylvain Chevallier, and Raphael Y. de Camargo. A Systematic Evaluation of

Euclidean Alignment with Deep Learning for EEG Decoding, 2024. URL https://arxiv.org/abs/2401.10746v2.

[3] Kuntal Kokate, Bruno Aristimunha, Dung Truong, and Arnaud Delorme. Channel Adaptation for EEG Foundation Mod-

els: A Systematic Benchmark Across Architectures, Tasks, and Training Regimes, 2026. URL https://arxiv.org/abs/2604.

23091v1.

[4] Dingkun Liu, Yuheng Chen, Zhu Chen, Zhenyao Cui, Yaozhi Wen, Jiayu An, Jingwei Luo, and Dongrui Wu. EEG-FM-

Compass: Progress, Benchmarking, and Future Directions for EEG Foundation Models, 2026. URL https://arxiv.org/abs/

2601.17883v3.

[5] Huiyang Wang, Hongfang Han, John Q. Gan, and Haixian Wang. Lightweight Source-Free Domain Adaptation Based on

Adaptive Euclidean Alignment for Brain-Computer Interfaces, 2025. URL https://doi.org/10.1109/JBHI.2024.3463737.

[6] Sion An, Myeongkyun Kang, Soopil Kim, Philip Chikontwe, Li Shen, and Sang Hyun Park. Subject-Adaptive Transfer

Learning Using Resting State EEG Signals for Cross-Subject EEG Motor Imagery Classification, 2024. URL https:

//arxiv.org/abs/2405.19346v2.

[7] Youngchul Kwak, Kyeongbo Kong, Woo-Jin Song, and Seong-Eun Kim. Subject-Invariant Deep Neural Networks Based

on Baseline Correction for EEG Motor Imagery BCI, 2023. URL https://doi.org/10.1109/JBHI.2023.3238421.

[8] Suli Wang, Yangshen Deng, Zhenghua Bao, Xinyu Zhan, and Yiqun Duan. NeuroTTT: Bridging Pretraining-Downstream

Task Misalignment in EEG Foundation Models via Test-Time Training, 2025. URL https://arxiv.org/abs/2509.26301v2.

[9] Bruna J. Lopes, Gabriel Schwartz, Sylvain Chevallier, Raphael Y. de Camargo, and Bruno Aristimunha. Learning aligned

EEG representations with subject-specific encoders, 2026. URL https://arxiv.org/abs/2606.16462v1.

[10] Daniil A. Berdyshev, Artem M. Grachev, Sergei L. Shishkin, and Bogdan L. Kozyrskiy. EEG-Reptile: An Automatized

Reptile-Based Meta-Learning Library for BCIs, 2025. URL https://arxiv.org/abs/2412.19725v2.

[11] Urban Širca, Lovro Brulec, and Maryam Alimardani. Parameter-Efficient Fine-Tuning of EEG Foundation Models for

Plug-and-Play Motor Imagery BCIs, 2026. URL https://doi.org/10.1109/BCI69045.2026.11435102.

58

<!-- page 59 -->

[12] Jun-You Lin, Ying Choon Wu, and Tzyy-Ping Jung. The Identity Trap in EEG Foundation Models: A Diagnostic Audit,

2026. URL https://arxiv.org/abs/2606.06647v1.

[13] Aymen Sarhane, Fouad Lbakali, Mouad Souissi, Jonathan Lys, and Giulia Lioi. Stacked LoRA for Subject-Adaptive EEG

Foundation Models in Motor Imagery Decoding, 2026. URL https://arxiv.org/abs/2607.03094v1.

[14] Bruna J. Lopes, Gabriel Schwartz, Sylvain Chevallier, Raphael Y. de Camargo, and Bruno Aristimunha. Learning aligned

EEG representations with subject-specific encoders. Scientific Reports, 2026. doi: 10.1038/s41598-026-69220-z. URL

https://doi.org/10.1038/s41598-026-69220-z. Article in Press; accepted 26 August 2026.

[15] Anh T. Nguyen, Zihua Sun, and Michelle J. Johnson. Lightweight Adaptation of EEG Foundation Models for Stroke

Motor Imagery Decoding: Domain Shift and Subject-Level Robustness, 2026. URL https://arxiv.org/abs/2609.00282v1.

[16] Anupam Sharma and Krishna Miyapuram. Evaluating Fast Adaptability of Neural Networks for Brain-Computer Inter-

face, 2024. URL https://arxiv.org/abs/2404.15350v1.

[17] Liuyin Yang, Qiang Sun, Ang Li, and Marc M. Van Hulle. Are EEG Foundation Models Worth It? Comparative Evalu-

ation with Traditional Decoders in Diverse BCI Tasks. In International Conference on Learning Representations, 2026.

URL https://openreview.net/forum?id=5Xwm8e6vbh.

[18] Chelsea Finn, Pieter Abbeel, and Sergey Levine. Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks.

In Proceedings of the 34th International Conference on Machine Learning, 2017. URL https://proceedings.mlr.press/v70/

finn17a.html.

[19] Yassine El Ouahidi, Jonathan Lys, Philipp Thölke, Nicolas Farrugia, Bastien Pasdeloup, Vincent Gripon, Karim Jerbi,

and Giulia Lioi. REVE: A Foundation Model for EEG – Adapting to Any Setup with Large-Scale Pretraining on 25,000

Subjects, 2025. URL https://arxiv.org/abs/2510.21585v1.

[20] Jiquan Wang, Sha Zhao, Zhiling Luo, Yangxuan Zhou, Haiteng Jiang, Shijian Li, Tao Li, and Gang

Pan. CBraMod: A Criss-Cross Brain Foundation Model for EEG Decoding. In International Con-

ference on Learning Representations, 2025. URL https://proceedings.iclr.cc/paper_files/paper/2025/hash/

bbbd6d915cb90be21c1254a82d45cedd-Abstract-Conference.html.

[21] Wei-Bang Jiang, Li-Ming Zhao, and Bao-Liang Lu. Large Brain Model for Learning Generic Representations with

Tremendous EEG Data in BCI. In International Conference on Learning Representations, 2024. URL https://proceedings.

iclr.cc/paper_files/paper/2024/hash/47393e8594c82ce8fd83adc672cf9872-Abstract-Conference.html.

[22] Ethan Perez, Florian Strub, Harm De Vries, Vincent Dumoulin, and Aaron Courville. FiLM: Visual Reasoning with a

General Conditioning Layer. Proceedings of the AAAI Conference on Artificial Intelligence, 32(1), 2018. doi: 10.1609/

aaai.v32i1.11671. URL https://doi.org/10.1609/aaai.v32i1.11671.

[23] Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen.

LoRA: Low-Rank Adaptation of Large Language Models. In International Conference on Learning Representations,

2022. URL https://arxiv.org/abs/2106.09685.

[24] Manzil Zaheer, Satwik Kottur, Siamak Ravanbakhsh, Barnabas Poczos, Ruslan Salakhutdinov, and Alexander J. Smola.

Deep Sets. In Advances in Neural Information Processing Systems, 2017. URL https://papers.nips.cc/paper/2017/hash/

f22e4747da1aa27e363d86d40ff442fe-Abstract.html.

59