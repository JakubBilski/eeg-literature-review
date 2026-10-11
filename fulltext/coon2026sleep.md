<!-- source: pdf/coon2026sleep.pdf | converter: pymupdf -->

<!-- page 1 -->

# Sleep EEG foundation models reveal within-stage microstructure that improves health screening beyond traditional stages

## William Grey Coon

Johns Hopkins University Applied Physics Laboratory

## Mattson Ogg

Johns Hopkins University Applied Physics Laboratory

## Article

## Keywords:

Posted Date: June 26th, 2026

DOI: https://doi.org/10.21203/rs.3.rs-9044150/v2

License:   This work is licensed under a Creative Commons Attribution 4.0 International License.   Read Full License

Additional Declarations: No competing interests reported.

Version of Record: A version of this preprint was published at npj Digital Medicine on July 9th, 2026. See the published version at https://doi.org/10.1038/s41746-026-02970-2.

<!-- page 2 -->

1

## 1

Sleep EEG foundation models reveal within-stage microstructure  2  that improves health screening beyond traditional stages  3

4    5  William Coon1,2 & Mattson Ogg1  6    7  1Intelligent Systems Center, Research and Exploratory Development Department  8  Johns Hopkins Applied Physics Laboratory  9  2Johns Hopkins University, Whiting School of Engineering  10  will.coon@jhuapl.edu; mattson.ogg@jhuapl.edu  11    12  Corresponding author: William Coon  13    14    15    16  Abstract  17

Sleep physiology provides rich longitudinal biosignals reflecting integrated  18  brain and systemic physiology, yet polysomnography is commonly compressed  19  into coarse, human-defined stages. We asked whether self-supervised foundation  20  models learn sleep EEG structure beyond traditional staging and encode enriched  21  health information. Using 11,261 overnight recordings, we trained transformers on  22  unlabeled sleep data and probed representations across diagnostic, demographic  23  and functional outcomes. Compared with architecture-matched transformers  24  trained from random initialization on each downstream task, SSL pretraining  25  improved performance across several outcomes. Compared with five-stage- 26  supervised pretraining, EEG-only advantages were clearest for BMI and age, while  27  differences for AHI, sex, and functional outcomes were smaller, nominal, or not  28  reliable. In nested controls, EEG-derived self-supervised model scores retained  29  incremental value beyond covariates, stage summaries, spectral summaries, and  30  a matched five-stage representation. Embedding analyses show that models  31  recover the stage scaffold without labels while preserving higher-resolution, stage- 32  anchored structure that carries task-specific health information beyond the five- 33  stage interface.   34

35

<!-- page 3 -->

2

## Introduction  1

Sleep provides a densely informative window into human physiology, reflecting coordinated  2  neural, cardiovascular, respiratory, metabolic, and autonomic activity across the night.1 To make  3  this complex signal clinically tractable, sleep medicine has long compressed polysomnography  4  (PSG) into a small set of visually scored stages—Wake, N1, N2, N3, and REM—based on criteria  5  originally formalized by Rechtschaffen and Kales and later refined by the American Academy of  6  Sleep Medicine2–4. This five-stage interface remains foundational to clinical sleep medicine and  7  provides a necessary reference point for new data-driven representations.  8

Yet the same compression that makes conventional staging clinically useful also makes it  9  intentionally lossy. Visual scoring is subjective and variable across raters5,6, fixed heuristics can  10  obscure individual- and age-related physiology7, and 30-s epochs impose a coarse temporal grid  11  that limits sensitivity to shorter-lived and within-stage dynamics8–10. These limitations also  12  propagate into automated scoring systems that largely learn to reproduce human-defined labels,  13  despite major advances in sleep-stage classification11–19. A parallel literature has therefore treated  14  sleep as a continuum rather than a strictly discrete taxonomy, including early automated  15  quantification and sleep/wake continuum analyses, microstate and feature-clustering  16  approaches, whole-brain transition analyses, and recent aperiodic/fractal-cycle definitions of  17  sleep structure20,21,8,22,9,23–25. Together, this work suggests that the question is not whether stages  18  are meaningful, but what physiological information is collapsed by the five-stage scaffold.  19

This question is increasingly important for digital medicine because sleep is both routinely  20  measurable and biologically integrative. Unlike many clinic-bound assays, sleep can be captured  21  passively over long time scales with scalable sensors, making it a natural substrate for  22  decentralized monitoring and biomarker discovery26–30. Its relevance is not limited to sleep  23  disorders: sleep is linked to cardiovascular, cognitive, neurologic, and mental-health outcomes1,31– 24  33. Thus, model-derived sleep representations may be useful not only when they predict  25  immediately actionable clinical labels, but also when they summarize latent physiology. Sleep- 26  EEG brain age is a clear example: chronological age is already known, but the gap between EEG- 27  predicted age and chronological age provides a brain-age / brain-age-index biomarker associated  28  with cognition, dementia risk, mortality, and broader brain health34–37. These developments  29  motivate models that can learn health-relevant structure from sleep physiology without relying  30  exclusively on predefined scoring rules.  31

Foundation models and self-supervised learning (SSL) offer one route to such representations.  32  SSL can learn from large unlabeled physiological datasets by exploiting intrinsic signal structure  33  rather than externally supplied labels38–40. In sleep, this strategy is especially attractive because  34  physiology evolves continuously across time, space, and state, with local and regional dynamics  35  that are not fully captured by categorical stage labels41–43. Recent sleep foundation models such  36  as SleepFM and SleepGPT, and related representation-learning approaches such as SOM-CPC  37  and others, have demonstrated that learned sleep embeddings can recover the canonical stage  38  scaffold while preserving additional structure relevant to disease, age, apnea, and other  39  phenotypes25,44–47.  40

<!-- page 4 -->

3

However, these impressive results leave open a mechanistic and clinically important question: to  1  what extent do foundation model embeddings improve prediction simply by capturing the same  2  coarse information summarized by the five-stage scaffold (e.g., stage composition and stage- 3  transition dynamics), versus by uncovering additional, finer-grained organization within stages  4  that carries health-relevant signal? Resolving this distinction matters for both translation and  5  discovery, because it determines whether improvements represent a repackaging of established  6  sleep architecture or reflect previously unmeasured microstructure, and because it motivates  7  explicit benchmarks and analyses that can isolate, summarize, and interpret any structure learned  8  beyond the canonical stage interface.  9

In this study, we train Sleep2.0, a HuBERT-style transformer foundation model48, to test whether  10  foundation models trained with SSL learn representations of sleep that extend beyond traditional  11  staging, and we explicitly interrogate whether any predictive gains reflect five-stage architecture  12  versus additional learned microstructure. Using publicly available polysomnographic datasets  13  comprising 11,261 overnight recordings, we pretrain transformer-based models on unlabeled  14  sleep physiology, focusing our primary analyses on EEG-only representations to align with  15  scalable, home-relevant sensing. We then benchmark learned embeddings against two matched  16  controls—an otherwise identical model pretrained to predict five-stage labels, and a model trained  17  from scratch—to isolate whether downstream gains reflect the internalization of the canonical  18  stage scaffold or additional structure uncovered through self-supervision. To establish clinical  19  relevance, we evaluate participant-level screening behavior using discrimination, calibration,  20  decision-analytic utility, and subgroup robustness, and we test whether EEG-derived scores retain  21  incremental predictive value beyond demographic covariates, stage summaries, spectral  22  summaries, staging-derived sleep-report summaries, and a matched five-stage representation.  23  Finally, we interrogate what the models learn by quantifying and visualizing their latent  24  organization, mapping data-driven microstates and cross-subject meta-states back to both the  25  five-stage scaffold and familiar, biomarker-relevant EEG physiology. This integrative evaluation  26  connects performance to mechanism, showing how EEG foundation models can preserve the  27  familiar clinical organization of sleep while revealing higher-resolution, stage-anchored  28  structure—most clearly N2-linked for apnea- and BMI-related information, with age-related signal  29  distributed more broadly—that carries measurable information not captured by conventional stage  30  summaries.   31

## Results  32

To isolate whether self-supervised learning (SSL) captures health-relevant sleep structure  33  beyond the traditional five-stage interface, we evaluated a foundation model (Sleep2.0; Figure 1)  34  against two strictly matched control architectures: a supervised model pretrained to predict five- 35  stage sleep labels, and a baseline model trained from scratch without pretraining.  36    37  Unless otherwise noted, all analyses use strict participant-level splits and focus on EEG-only  38  models. We emphasize EEG-only representations because they derived the greatest relative  39  benefit from SSL pretraining and are the most broadly applicable to scalable, at-home monitoring  40  (though multimodal PSG variants showed comparable qualitative patterns; Figure 2).73,74,19,75,76  41

<!-- page 5 -->

4

To clarify clinical and translational relevance, downstream prediction targets are grouped into  1  three intended-use categories: diagnostic sleep metrics, demographic variables, and functional  2  outcomes.  3    4  This design separates architecture from training objective. The SSL and five-stage-supervised  5  models share the same transformer backbone and training corpus, but differ in pretraining targets:  6  masked pseudo-label prediction from unlabeled physiology versus supervised five-stage label  7  prediction. Downstream tasks are therefore compared after identical task-head replacement and  8  fine-tuning, allowing differences to be attributed to learned representation content rather than  9  model class alone.  10    11  Health Information is Extensively Encoded in SSL-Derived Sleep Representations  12    13  Fine-tuning the EEG-only Sleep2.0 SSL foundation model yielded above-chance prediction  14  across a diverse set of diagnostic, demographic, and functional outcomes (Figure 2, EEG-only).  15  Across the 15 EEG-only outcomes shown in Figure 2, we controlled the false discovery rate using  16  Benjamini–Hochberg correction and report nominal p-values alongside FDR-adjusted q-values.  17  After FDR correction across outcomes, SSL-derived predictions were reliably above chance for  18  key diagnostic and demographic targets, including sleep-stage classification (82.1% accuracy; p  19  = 9.77×10⁻⁴, q = 2.44×10⁻³), apnea severity (AHI, Pearson r = 0.542; p = 9.77×10⁻⁴, q =  20  2.44×10⁻³), age (r = 0.677; p = 9.77×10⁻⁴, q = 2.44×10⁻³), sex (70.6% accuracy; p = 9.77×10⁻⁴, q  21  = 2.44×10⁻³), and BMI (r = 0.383; p = 9.77×10⁻⁴, q = 2.44×10⁻³). Effects for mood and cognition  22  were smaller but still detectable for selected outcomes, including BDI (r = 0.045; p = 4.58×10⁻³, q  23  = 8.58×10⁻³), WASI-IQ (r = 0.090; p = 2.93×10⁻³, q = 6.28×10⁻³), and Pathfinder (r = 0.086; p =  24  9.77×10⁻⁴, q = 2.44×10⁻³). Other functional measures did not exceed chance after FDR correction  25  (q > 0.05), indicating that functional information is present but weaker and outcome-dependent in  26  nocturnal sleep EEG.  27    28  The relatively weak performance of from-scratch models for some participant-level outcomes is  29  expected because the same high-capacity architecture is trained only on the smaller APPLES  30  fine-tuning cohort, whereas pretrained models first learn sleep structure from the full 11,261- 31  recording corpus. Thus, SSL pretraining supplies both a better initialization and a more stable  32  inductive bias for outcomes whose EEG correlates are distributed across the night. Consistent  33  with this interpretation, smaller 2-layer and 6-layer architecture controls showed qualitatively  34  similar pretrained-model patterns and relatively stronger from-scratch behavior when model  35  capacity was better matched to available labeled data (Supplementary Figure 1).  36    37  To determine whether gains reflect SSL-derived representations rather than the transformer  38  architecture alone, we compared matched models trained from scratch versus SSL-pretrained  39  using paired Wilcoxon signed-rank tests across folds (Figure 2; nominal p-values with FDR  40  correction across outcomes). SSL pretraining significantly improved performance over from- 41  scratch training for sleep staging (V = 55, p = 1.95×10⁻³, q = 5.86×10⁻³), AHI (V = 55, p =  42  1.95×10⁻³, q = 5.86×10⁻³), BMI (V = 55, p = 1.95×10⁻³, q = 5.86×10⁻³), age (V = 55, p = 1.95×10⁻³,  43  q = 5.86×10⁻³), sex (V = 51, p = 1.37×10⁻², q = 2.56×10⁻²), BDI (V = 45, p = 9.15×10⁻³, q =  44

<!-- page 6 -->

5

1.96×10⁻²), WASI-IQ (V = 53, p = 5.86×10⁻³, q = 1.46×10⁻²), and Pathfinder (V = 55, p =  1  1.95×10⁻³, q = 5.86×10⁻³). The same pattern of results was observed for different size  2  configurations of the from-scratch model (Supplementary Figure 1A).  3    4  We next tested whether SSL’s advantage depends on learning sleep structure beyond the  5  conventional five-stage scaffold by comparing against a supervised model pretrained for five- 6  stage sleep scoring (paired Wilcoxon signed-rank tests; FDR correction across outcomes). After  7  FDR correction, SSL significantly outperformed five-stage pretraining for BMI (V = 55, p =  8  1.95×10⁻³, q = 2.93×10⁻²) and age (V = 54, p = 3.91×10⁻³, q = 2.93×10⁻²). For BDI (V = 48, p =  9  3.71×10⁻², q = 0.139) and Pathfinder (V = 47, p = 4.88×10⁻², q = 0.146), differences were nominal  10  (p < 0.05) but did not survive FDR correction. No reliable differences were observed for AHI (V =  11  44, p = 0.105, q = 0.176), sex (V = 11, p = 0.105, q = 0.176), or WASI-IQ (V = 41, p = 0.193, q =  12  0.290). As expected, five-stage pretraining yielded slightly higher staging accuracy than SSL  13  (82.4% vs 82.1%; V = 6, p = 2.73×10⁻², q = 0.137), although this difference did not survive FDR  14  correction. This pattern was consistent across pretrained models of different sizes  15  (Supplementary Figure 1B). Together, these comparisons indicate that conventional staging  16  captures meaningful coarse-grained structure (supporting competitive performance for several  17  outcomes), while SSL representations encode additional health-relevant information—most  18  consistently for age and BMI in EEG-only analyses—that is not preserved by the five-stage  19  interface. Although chronological age is directly observable and its inference from EEG may  20  appear trivial at first glance, accurate age prediction from sleep EEG serves as a probe of whether  21  the representation captures age-sensitive neurophysiology. This is particularly relevant because  22  the residual between EEG-estimated age and chronological age forms the basis of brain-age-gap  23  biomarkers, which have recently been associated with dementia risk in longitudinal cohorts.  24

Representations support participant-level screening behavior  25

To evaluate performance in a screening-like setting, we aggregated segment-level model outputs  26  to the participant level (mean across segments per participant) and assessed discrimination,  27  calibration, decision-analytic utility, and subgroup robustness (Figure 3). Across held-out  28  participants (APPLES dataset; n = 1,044), EEG-derived scores showed moderate-to-strong  29  discrimination for apnea severity (AUROC = 0.762 for AHI ≥ 15; AUROC = 0.776 for AHI ≥ 30),  30  obesity (AUROC = 0.720 for BMI ≥ 30), and demographic outcomes (AUROC = 0.877 for age ≥  31  60; AUROC = 0.803 for sex).  32

After out-of-fold probability mapping, calibration was stable across outcomes (Brier scores: 0.107  33  for AHI ≥ 15, 0.191 for AHI ≥ 30, 0.218 for BMI ≥ 30, 0.133 for age ≥ 60, 0.167 for sex). Decision  34  curve analysis for severe apnea (AHI ≥ 30) showed positive net benefit over treat-all and treat- 35  none strategies across clinically plausible threshold probabilities. Stratified AUROCs by sex and  36  by age bin (<60 vs ≥60) demonstrated broadly similar performance across subgroups (Figure  37  3e,f).  38

SSL-derived scores add information beyond demographics and stage-derived sleep  39  reports  40

<!-- page 7 -->

6

Because several targets are correlated with demographic risk factors, sleep architecture, and  1  conventional spectral physiology, we next tested whether EEG-derived SSL scores retained  2  information beyond simpler explanatory features. We compared participant-level screening  3  models using covariates, ground-truth stage summaries, conventional EEG spectral summaries,  4  the target-specific score from the matched five-stage-pretrained model, the target-specific SSL  5  score, and prespecified combinations of these blocks (Figure 4a–h). No model included both SSL  6  and five-stage scores, allowing each learned representation to be compared against the same  7  non-transformer baseline.  8

Spectral summaries were informative, especially for age (spectra-only AUROC = 0.680), and also  9  carried signal for AHI (0.677) and BMI (0.608). Adding spectra to covariates + stage summaries  10  improved AUROC for age (0.738 to 0.781), AHI (0.710 to 0.717), and BMI (0.710 to 0.728),  11  confirming that classical spectral structure explains part of the signal. However, the fully adjusted  12  SSL model still exceeded the fully adjusted five-stage representation for age (0.880 vs 0.799),  13  BMI (0.776 vs 0.730), and AHI (0.761 vs 0.733), whereas sex slightly favored the five-stage  14  representation (0.834 vs 0.846).  15

In matched residual analyses after regressing out covariates, stage summaries, and spectral  16  summaries, SSL scores remained associated with residual age (Spearman ρ = 0.47, p =  17  1.2×10⁻⁵⁸), AHI (ρ = 0.26, p = 8.9×10⁻¹⁸), and BMI (ρ = 0.24, p = 7.1×10⁻¹⁵). The corresponding  18  five-stage scores showed weaker associations for age (ρ = 0.17, p = 6.4×10⁻⁸), AHI (ρ = 0.21, p  19  = 5.1×10⁻¹²), and BMI (ρ = 0.06, p = 6.3×10⁻²). Thus, SSL retained incremental information  20  beyond covariates, stages, spectra, and the matched five-stage representational baseline, most  21  clearly for age and BMI and more modestly for AHI.  22

PSG context analysis  23

As an additional context analysis, a multimodal PSG model (EEG, EOG, EMG, ECG, respiration)  24  modestly improved discrimination for severe apnea and BMI, consistent with added respiratory  25  and peripheral physiology, while EEG-only remained competitive and retained stronger  26  performance for age and mild apnea thresholds (Supplementary Figure 3; Supplementary Table  27  2).  28

SSL learns the gross geometry of conventional stages without stage labels  29

Given that five-stage pretraining remained competitive for some outcomes, we next asked  30  whether the SSL embedding space recovers canonical stage organization despite using no stage  31  labels during pretraining. Two-dimensional t-Distributed Stochastic Neighbor Embedding (t- 32  SNE77) projections of epoch embeddings prior to any fine-tuning, colored by ground-truth stage  33  labels, showed that SSL embeddings reproduce the expected global stage geometry in all four  34  held-out test datasets (Figure 5). This cross-dataset consistency underscores the generalizability  35  of the SSL model’s latent representation and demonstrates that it autonomously captures the  36  primary physiological distinctions underlying traditional sleep stages while also supporting richer  37  internal structure.  38

<!-- page 8 -->

7

We used each held-out dataset according to the labels and outcomes it supports. APPLES was  1  the primary health-outcome cohort because it is the largest held-out dataset with rich diagnostic,  2  demographic, mood, and cognitive measures. HomePAP is smaller but shares AHI, age, BMI,  3  and sex, enabling external replication for those outcomes. Sleep-EDF and Dreem provide stage- 4  labeled EEG benchmarks but lack comparable participant-level health metadata. Accordingly, we  5  used all four datasets for stage-geometry visualization and latent-granularity analyses, HomePAP  6  for shared outcome replication, and APPLES for the full health-outcome analysis.  7

SSL supports a higher-resolution decomposition of within-night sleep structure  8  We quantified the complexity of representational microstructure using a within-night Bayesian  9  Information Criterion (BIC) cluster-sweep analysis on four held out data sets. For each recording,  10  we applied k-means clustering to the final-layer transformer embeddings (prior to any fine-tuning)  11  across a range of candidate state counts and identified the state number minimizing BIC (Figure  12  5). Across datasets, SSL supported higher selected k than the five-stage baseline: APPLES  13  median = 11 (SSL) vs 5 (5-stage), HomePAP 10 vs 5, Dreem overall 10 vs 5, and Sleep-EDF 12  14  vs 5; paired tests were significant for each dataset (APPLES, HomePAP, Sleep-EDF: p <  15  2.2×10⁻¹⁶; Dreem: p = 4.7×10⁻¹⁵; Supplementary Figure 4). These results were stable across  16  random initializations of the clustering procedure. Note that BIC is used here only as an  17  operational, penalized model-selection criterion for within-record compression. Hence the BIC  18  result is comparative rather than ontological: under the same clustering procedure, SSL  19  embeddings support finer stage-anchored partitions than five-stage-pretrained embeddings. The  20  usefulness of this extra granularity is evaluated separately through downstream analyses: Rosetta  21  summaries, meta-state prediction, spectral/event-level physiology, and robustness controls.  22

Because microstates are estimated independently within each recording, we summarized where  23  additional complexity concentrates by anchoring microstates to AASM stages (“Rosetta”  24  mapping). For each subject, each microstate was assigned to the stage in which it most frequently  25  occurred. Across recordings, Wake and N2 consistently subdivided into more microstates than  26  N3 or REM (Supplementary Figure 4), indicating that SSL-derived resolution is not uniformly  27  distributed across sleep but instead preferentially refines stages known to encompass  28  heterogeneous physiology43,78,79. Importantly, this indicates that the increased representational  29  complexity observed does not imply greater interpretive opacity. Rather, it reflects a higher- 30  resolution decomposition of sleep physiology that preserves traditional stages while subdividing  31  them into reproducible, data-driven substates.  32

We next tested whether this microstate/Rosetta pattern was recoverable under different k-means  33  initializations. Holding each APPLES recording at its selected k and varying only the clustering  34  seed, fixed-k SSL microstate assignments were recoverable across 10 seeds (mean pairwise ARI  35  = 0.793; mean pairwise AMI = 0.856; n = 1,044 recordings). The selected-k distribution was  36  centered near 11 clusters per recording (median = 11; mean = 11.46), and stage-anchored  37  Rosetta counts were stable: in all 10 seeds, median microstate counts were N2 = 5, Wake = 3,  38  REM = 1, N1 = 1, and N3 = 0. The expected Rosetta ordering held in every seed (N2 > N3, N2 >  39  REM, Wake > N3, Wake > REM; one-sided Wilcoxon tests, all p < 5 × 10⁻¹³⁰). Thus, the conclusion  40  that SSL preferentially subdivides heterogeneous N2 and Wake structure is not dependent on a  41  single clustering initialization.  42

<!-- page 9 -->

8

Embedding atlases make microstructure and phenotype gradients visually interpretable  1  To visualize how microstates organize in a shared coordinate system, we constructed global  2  UMAP atlases from pooled APPLES epoch embeddings and, additionally, projected an exemplar  3  subject onto each atlas (Figure 6). Stage-colored views confirmed that both representations  4  preserve coarse stage organization, but SSL expresses clearer within-stage subdivision. When  5  viewed within an individual subject, SSL embeddings form compact, well-separated “islands,”  6  whereas stage-supervised embeddings of those same epochs showed greater dispersion and  7  overlap (Figure 6c,d). Consistent with N1’s transient, low-prevalence role in typical sleep  8  architecture, N1 epochs often do not form stable, dedicated microstates. Timeline views show  9  that microstate progression over the course of the night exhibits structure patterning consistent  10  with preserving gross 5-stage structure while exhibiting higher-resolution patterns within stages.  11  Together, these atlases provide an intuitive visualization of how SSL preserves the gross sleep- 12  stage scaffold while expressing a finer microstate geometry.    13

To assess whether health information is expressed in manifold geometry, we overlaid phenotypes  14  on the global atlases. Across diagnostic and demographic phenotypes (apnea severity, age, BMI,  15  sex), both SSL and five-stage manifolds exhibited structured gradients, with SSL atlases showing  16  additional continuous variation for several outcomes (Figure 7). When visualizations were  17  restricted to N2 epochs, gradients became more pronounced, consistent with the Rosetta analysis  18  indicating that much of the added resolution concentrates within N2.   19

To test the stability of individuals’ representations, we used Sleep-EDF, which includes 74  20  participants with two nights each, for an exploratory repeated-night analysis. A correlation-based  21  night-level embedding “fingerprinting” analysis correctly matched the alternate night from the  22  same participant in 60/148 SSL queries (40.5%; 95% CI 32.6–48.9%), above a conservative 1/74  23  chance baseline (exact binomial p < 2.2×10⁻¹⁶). SSL also exceeded the five-stage baseline in top- 24  1 matching accuracy (40.5% vs 22.9%) and same-participant night-pair similarity (Wilcoxon V =  25  1311.5, p = 8.0×10⁻⁴). These results suggest a stable trait-like component while leaving  26  substantial night-specific variation (Supplementary Figure 5).  27

A cross-subject meta-state model quantifies within-stage signal beyond the five-stage  28  scaffold  29    30  Because microstate labels are recording-specific, we next mapped subject-level microstructure  31  to a shared vocabulary by clustering microstate representatives into meta-states and summarizing  32  each subject by meta-state occupancy/diversity. The first step estimates recording-specific within- 33  night structure (including per-recording state granularity) and compresses it into compact  34  representations suitable for cross-subject mapping, whereas the second step aligns those  35  recording-specific substates into a shared cross-subject vocabulary. We chose this two-step  36  design because it preserves local within-night structure, avoids forcing a single global K on all  37  recordings, reduces domination of the clustering objective by the most prevalent epochs/stages,  38  and yields subject-level meta-state occupancy features that are directly comparable across  39  individuals. A stability-constrained M sweep supported M = 7 as a compact, interpretable solution  40  on a broader performance plateau (Supplementary Figure 6), and the resulting meta-states were  41

<!-- page 10 -->

9

stage-anchored mixtures (Figure 8a). We treat M (the objectively determined number of common  1  meta-states) as a resolution parameter rather than a fixed biological state count.  2

At M = 7, adding meta-state occupancy features to five-stage summary features improved both  3  screening and continuous-outcome prediction for key diagnostic and demographic outcomes. For  4  continuous outcomes, mean R2 increased from 0.139 to 0.211 for AHI (ΔR2 +0.072) and from  5  0.140 to 0.210 for age (ΔR2 +0.070) (Supplementary Figure 7). In contrast, meta-state summaries  6  provided limited or inconsistent benefit for mood/cognition outcomes at this level of aggregation.  7  For screening, mean AUROC increased from 0.686 to 0.745 for AHI (ΔAUROC +0.059), from  8  0.570 to 0.663 for BMI (ΔAUROC +0.093), and from 0.844 to 0.897 for age (ΔAUROC +0.053),  9  with minimal change for sex (ΔAUROC +0.006) (Figure 8b).   10

Sensitivity analyses showed that this interpretation was stable at the stage-anchored and  11  downstream levels, although not at the level of exact unsupervised labels. Across 10 M = 7 meta- 12  state seeds, exact label recoverability was moderate (mean pairwise ARI = 0.513 ± 0.086; range  13  = 0.359–0.691), but matched stage-composition structure was highly stable (dominant-stage  14  agreement = 0.879 ± 0.086; stage-composition cosine similarity = 0.964 ± 0.024) (Supplementary  15  Figure 8). Repeating downstream stage+meta models across seeds yielded positive gains over  16  stage-only summaries in 10/10 seeds for AHI, AHI ≥ 15, Age, Age ≥ 60, and BMI ≥ 30, and in 9/10  17  seeds for continuous BMI; sex remained small and inconsistent. Local sensitivity analyses over  18  M = 5–9 and PCA dimensionality = 10, 20, and 50 similarly retained positive gains in all 45  19  seed/parameter configurations for AHI, AHI ≥ 15, Age, Age ≥ 60, BMI, and BMI ≥ 30, but not for  20  sex (29/45 positive) (Supplementary Figure 9). Thus, M = 7 is best interpreted as a representative  21  solution on a stability-performance plateau rather than a unique state count.  22

Because five-stage features already capture overall stage composition and coarse transition  23  dynamics, any additional gain from meta-states could arise either from residual differences in  24  global architecture (e.g., more time awake) or from higher-resolution heterogeneity within stages  25  that the canonical taxonomy collapses. To further isolate the source of the incremental signal, we  26  compared stage-only models against augmented models that replace global meta-state  27  occupancy with stage-conditional occupancy features computed within N2 and within Wake.  28  Conceptually, these conditional features describe how a subject’s N2 (or Wake) time is distributed  29  across meta-states, independent of the total amount of N2 (or Wake) present.  30

Across key outcomes, conditioning meta-state occupancy on N2 preserved much of the full  31  stage+meta gain, whereas conditioning on Wake produced smaller and less consistent gains  32  (Supplementary Figure 10). Dominant-stage ablations provided convergent but less stable  33  localization: excluding N2-dominant meta-state features attenuated gains in the representative M  34  = 7 solution, but seed and local-hyperparameter checks showed that N2-vs-Wake ablation  35  margins were small and configuration-dependent (Supplementary Figure 10). We therefore  36  interpret these analyses as evidence that within-N2 heterogeneity contributes substantially to the  37  SSL advantage, not as proof that a fixed N2-dominant subset uniquely explains all incremental  38  information.  39

<!-- page 11 -->

10

We next tested whether apparent N2 localization simply reflected N2 occupying the largest  1  fraction of the night. Stage-conditioned controls recomputed meta-state occupancy within each  2  canonical stage and compared the resulting gain with matched-size random feature blocks  3  evaluated under the same folds and seeds. N2-conditioned features recovered substantial gain  4  for apnea- and BMI-related outcomes beyond both total N2 duration and matched random feature  5  additions: for continuous outcomes (Supplementary Figure 11), N2 was the top-performing stage- 6  conditioned block in 9/10 seeds for AHI and 8/10 seeds for BMI, whereas age was more strongly  7  distributed outside N2, with N1-linked features top-performing in 10/10 seeds. For binary  8  screening (Supplementary Figure 12), N2 was top-performing in 8/10 seeds for AHI ≥ 15 and 5/10  9  seeds for BMI ≥ 30, while age ≥ 60 and sex showed weaker or more distributed stage specificity.  10  Thus, within-N2 heterogeneity is an important contributor, especially for apnea- and BMI-related  11  information, but the SSL advantage is not exclusively N2-driven across all outcomes.  12

To further interpret what aspects of within-stage structure relate to phenotype, we examined  13  univariate associations between each meta-state’s subject-level occupancy and each continuous  14  outcome (Spearman ρ; FDR correction across meta-states within each phenotype; Figure 8c). At  15  M = 7, meta-states were stage-anchored mixtures, and the strongest phenotype associations  16  were concentrated in N2- and Wake-dominant meta-states. Importantly, the three N2-dominant  17  meta-states (m0, m3, m6) exhibited heterogeneous—and sometimes opposing—relationships  18  with both apnea severity and age, implying that collapsing heterogeneous N2 physiology into a  19  single stage can attenuate or erase phenotype signal at the five-stage level. For apnea severity,  20  an N2-dominant meta-state (m6) was positively associated with AHI (ρ = +0.325, p = 4.54×10⁻²⁷),  21  while two other N2-dominant meta-states were negatively associated (m0: ρ = −0.184, p =  22  2.25×10⁻⁹; m3: ρ = −0.184, p = 2.20×10⁻⁹; Figure 8c); a deep-sleep–dominant meta-state also  23  decreased strongly with AHI (m2: ρ = −0.350, p = 1.91×10⁻³¹). For age, Wake-dominant meta- 24  states increased (m1: ρ = +0.232, p = 3.14×10⁻¹⁴; m5: ρ = +0.148, p = 1.46×10⁻⁶) while the REM- 25  dominant meta-state decreased (m4: ρ = −0.303, p = 1.34×10⁻²³), and within N2 we again  26  observed opposing directions (m6: ρ = +0.164, p = 1.07×10⁻⁷; m3: ρ = +0.124, p = 5.84×10⁻⁵; m0:  27  ρ = −0.265, p = 3.36×10⁻¹⁸; Figure 8c). For BMI, we likewise observed both positive and negative  28  associations across N2-linked meta-states (m6; ρ = +0.074, p = 0.016 versus m2; ρ = −0.131, p  29  = 1.70×10⁻⁵; m3; ρ = −0.137, p = 6.74×10⁻⁶). These univariate associations were consistent with  30  the predictive controls. Adding SSL meta-state summaries to five-stage summaries improved  31  screening for AHI (AUROC 0.686→0.745), BMI (0.570→0.663), and age (0.844→0.897), with  32  little change for sex (ΔAUROC = +0.006; Figure 8b). A forced M = 7 analysis applied to the  33  matched five-stage-pretrained representation did not reproduce the same gains or organized  34  phenotype associations (Figure 8d–f), indicating that the result is not explained simply by adding  35  features or applying the same clustering pipeline to any transformer embedding (see also  36  Supplementary Figure 13).  37

We next asked whether these phenotype-associated N2 subdivisions corresponded to  38  recognizable EEG physiology. The three N2-linked meta-states differed in low-frequency and  39  sigma structure (Figure 8g–m). Within AASM-scored N2 in these meta-states, m6 showed greater  40  power in the .5–1.25Hz band (+0.40–0.44 dB) and theta power (+0.22 dB) than m0/m3, but lower  41  slow-sigma (−0.25–0.44 dB) and fast-sigma power (−0.38–0.42 dB), arguing against simple stage  42

<!-- page 12 -->

11

admixture. Event analyses confirmed this physiological separation: spindle density differed  1  strongly across N2-linked meta-states (χ² = 294.61, p = 1.06×10⁻⁶⁴, q = 9.04×10⁻⁶⁴), with m6  2  showing lower spindle density than m0/m3, while slow-oscillation density also differed (χ² = 16.20,  3  p = 3.04×10⁻⁴, q = 3.69×10⁻⁴) and m6 showed stronger slow-oscillation morphology. Thus, SSL- 4  defined N2 substates capture physiologically interpretable within-stage NREM structure, not  5  merely stage duration or stage admixture.  6

Collectively, the microstate and meta-state analyses show how SSL extends, rather than  7  replaces, the conventional stage scaffold. Canonical stages explain substantial structure and  8  remain a strong baseline, but SSL embeddings preserve additional stage-anchored variation that  9  is collapsed by five-stage summaries. We therefore interpret the recovered microstates and meta- 10  states as operational summaries of representational structure, not as an ontologically fixed set of  11  sleep states. Their value is instead supported by downstream prediction, robustness analyses,  12  and physiological anchoring: within-stage heterogeneity provides measurable information beyond  13  stage-only summaries, with N2-linked structure contributing most clearly to apnea- and BMI- 14  related analyses and age-related signal distributed more broadly across stage-linked structure.  15

## Discussion  16

This study shows that self-supervised learning (SSL) foundation models trained on unlabeled  17  sleep EEG preserve health-informative structure that is partially collapsed by conventional five- 18  stage scoring. Prior sleep foundation-model studies have demonstrated strong predictive  19  performance, but it has remained unclear whether such gains mainly repackage conventional  20  sleep architecture or reflect finer-grained physiology beyond the hypnogram. By comparing SSL  21  with architecture-matched from-scratch and five-stage-supervised models, we show that the five- 22  stage interface remains a strong clinical scaffold rather than a strawman. At the same time, SSL  23  retains additional information, most clearly for age and BMI and more modestly for AHI,  24  suggesting that learned representations preserve stage-anchored physiological structure beyond  25  the conventional stage labels.  26

These findings extend a long literature arguing that sleep physiology is more continuous and  27  heterogeneous than the five-stage hypnogram implies. Earlier automated quantification and  28  sleep/wake continuum approaches showed that sleep structure could be represented with finer  29  gradations than visual stage labels20,21. More recent clustering and embedding studies similarly  30  showed that data-driven sleep states map onto, but also subdivide, conventional stages and relate  31  to traits such as age and apnea9,25,44.  This study’s contribution is to test these ideas in a matched  32  foundation-model framework, showing that SSL embeddings recover the canonical stage scaffold  33  without labels while preserving additional stage-anchored structure beyond it.  34

Head-to-head comparisons show that SSL pretraining robustly outperforms from-scratch training,  35  whereas advantages over the matched five-stage representation were narrower and outcome- 36  specific. The clearest EEG-only advantages were for age and BMI, with smaller or nonuniform  37  evidence for AHI and other outcomes. Expanded controls further showed that SSL was not merely  38  rediscovering conventional sleep architecture or classical spectra. Spectral summaries were  39  informative, especially for age, and the five-stage representation was competitive, but SSL  40

<!-- page 13 -->

12

retained incremental value beyond covariates, stage summaries, spectral summaries, and the  1  matched five-stage representation. Thus, the interpretation is not that SSL signal is independent  2  of known EEG physiology; rather, SSL organizes partly familiar spectral and NREM  3  microphysiological information in a higher-resolution, task-relevant representational space.  4

To interpret this added information, we mapped SSL embeddings back to the canonical stage  5  scaffold using stage-anchored cross-subject meta-states. These analyses do not support a fixed  6  new sleep-state taxonomy; instead, they show that SSL preserves health-informative  7  microstructure within familiar stages. N2 provides the clearest example, though not the only  8  source of signal. Stage-conditioned meta-state analyses indicate that N2-linked structure  9  preserves substantial apnea- and BMI-related information, whereas age-related signal is  10  distributed more broadly across Wake/N1-, REM-, and N2-linked structure. The N2-linked meta- 11  states also showed distinct and sometimes opposing phenotype associations, explaining how  12  collapsing all N2 epochs into a single label can attenuate or cancel health-relevant signal. Finally,  13  these N2 subdivisions were physiologically anchored: within AASM-scored N2, they differed in  14  low-frequency/theta and sigma structure, and spindle/slow-oscillation analyses distinguished  15  more spindle-rich N2 motifs from a spindle-sparse motif with stronger slow-oscillation morphology.  16  Thus, SSL appears to preserve within-stage NREM microphysiology that conventional staging  17  compresses, rather than replacing staging or localizing all added information exclusively to N2.  18

For digital medicine, these findings position EEG-only SSL representations as compact, reusable  19  summaries of overnight physiology for screening, triage, and biomarker discovery. Their value is  20  not in replacing the five-stage hypnogram, but in preserving that familiar scaffold while adding  21  low-dimensional, stage-anchored summaries of within-stage physiology. Meta-state occupancy  22  profiles could therefore be reported alongside conventional sleep summaries, while embedding  23  manifolds may provide a coordinate system for visualizing how diagnostic or trait-related variables  24  align with specific regions of sleep physiology.  25

The age result illustrates this translational logic. Although chronological age is directly observed,  26  EEG-predicted age can be interpreted as a probe of age-sensitive neurophysiology and as the  27  basis for brain-age-gap biomarkers. Future work should test whether Sleep2.0-derived age  28  residuals predict cognitive decline, dementia risk, or other aging-related outcomes beyond  29  chronological age and conventional sleep summaries. Similarly, EEG-derived apnea scores  30  showed screening-oriented discrimination, calibration, and decision-analytic behavior, but these  31  analyses are intended for participant-level decision support / risk stratification, not as  32  replacements for event-based respiratory scoring, which remains the diagnostic standard.  33

Several limitations guide clinical translation. First, these retrospective analyses require  34  prospective validation in real-world clinical and home-monitoring settings. Second, our EEG-only  35  analyses used central PSG EEG rather than frontal consumer headband montages; thus, their  36  home-monitoring relevance is translational rather than direct validation of consumer frontal EEG.  37  Wearable EEG, wrist PPG, actigraphy, and HSAT/polygraphy are complementary sensing  38  regimes, and respiratory-event detection from airflow, effort, oximetry, or PAP flow remains the  39  clinical substrate for apnea diagnosis. Third, self-supervised models may encode biases from  40

<!-- page 14 -->

13

their training cohorts, requiring population-aware validation across age, sex, race/ethnicity,  1  disease burden, acquisition setting, and sensor configuration.  2

Methodologically, the microstate/meta-state framework presented here is just one interpretable  3  summary of embedding structure, not the only one possible. Direct pooled clustering of all epochs  4  across subjects is a reasonable alternative, but it answers a different question: it estimates a  5  single cohort-level partition, whereas our two-step approach first protects and compresses  6  recording-specific microstructure and then aligns those local substates into a shared cross- 7  subject vocabulary. The present analyses provide an initial physiological anchor for this  8  vocabulary by showing that N2-linked meta-states differ in spectral profile, spindle expression,  9  and slow-oscillation density and morphology within AASM-scored N2. Future work should extend  10  event-level validation to K-complexes, spindle–slow-oscillation coupling, arousal and respiratory- 11  event timing, richer EEG topographies, independent event detectors, and external cohorts.  12

Finally, our results should not be interpreted as requiring this specific HuBERT-style transformer.  13  Smaller 2-layer and 6-layer models showed qualitatively similar patterns, but the matched SSL  14  versus five-stage comparison indicates that the pretraining objective –stage supervision versus  15  self-supervision– matters. Future studies should compare HuBERT-style masked prediction with  16  contrastive and generative objectives, and use attribution or probing analyses to identify the signal  17  features supporting each outcome.  18

Ultimately, foundation model-based sleep analytics will require clear intended-use definitions— 19  such as screening enrichment, decision support, or biomarker discovery—rather than claims of  20  full diagnostic replacement. By reducing reliance on expert labels while remaining aligned with  21  clinically familiar concepts, self-supervised representations offer a scalable route toward  22  continuous, data-driven health assessment from passive sleep recordings.  23

## Methods  24

Data sources, partitions, and outcomes  25

We assembled a pretraining corpus of 11,261 overnight polysomnography (PSG) records from  26  7,201 participants by combining seven large, publicly available datasets hosted by the National  27  Sleep Research Resource (NSRR): MESA, MrOS, SHHS, WSC, SOF, CFS, and NCHSDB.49–56  28  All recordings from 779 randomly selected participants (~10% of the pretraining cohort) were held  29  out as an internal validation partition for model selection.  30

To evaluate generalization, we additionally held out three external benchmark datasets—Dreem  31  Open57, Sleep-EDF58,59, and HomePAP60—that were never used during pretraining. For  32  downstream fine-tuning and clinical/digital-medicine evaluation, we focused on APPLES (Visit  33  3)61,62, which couples PSG with rich baseline physiology and standardized cognitive and mood  34  assessments. Outcomes analyzed in APPLES comprised diagnostic sleep metrics (five-stage  35  sleep staging, apnea–hypopnea index [AHI], Epworth Sleepiness Scale [ESS]63), demographic  36  variables (age, sex), and functional measures spanning mood and cognition (BDI64, HAM-D65,  37  POMS66, WASI-IQ67, Pathfinder68, MMSE69, Buschke70, SWMT71, and PVT72). All experiments  38

<!-- page 15 -->

14

used strict participant-level splits (all segments and all nights for a given participant assigned to  1  a single fold) to prevent information leakage across training and evaluation.  2

Signal preprocessing and model inputs  3

PSG signals were harmonized across datasets using a common preprocessing pipeline. We  4  extracted a central EEG derivation (C3 or C4) as the core modality and additional PSG channels  5  (EOG, chin EMG, ECG, and thoracic respiratory effort) for multimodal experiments. Signals were  6  resampled to 100 Hz, robustly normalized by median-centering and IQR-scaling after excluding  7  values beyond 20×IQR12, and segmented into 30 s epochs consistent with AASM conventions.  8  For transformer inputs, we concatenated 101 consecutive epochs (50.5 min) into fixed-length  9  sequences. During pretraining, sequences were sampled with overlap (hop size 25 epochs);  10  during fine-tuning and evaluation, sequences were sampled without overlap.  11

Self-supervised pretraining and matched baselines  12

We trained transformer foundation models on unlabeled sleep recordings using a HuBERT-style  13  masked pseudo-label prediction objective. In stage 1, each 101-epoch input sequence was  14  converted to epoch-level time-frequency power features, and mini-batch k-means with k = 100  15  was used to assign discrete pseudo-labels. The model was trained from raw input signals to  16  predict pseudo-labels for masked portions of the sequence, learning contextual representations  17  without stage labels. In stage 2, pseudo-labels were recomputed from first-stage transformer  18  embeddings at the model’s native temporal resolution, yielding 946 labels per 50.5-min sequence,  19  and clustered with k = 500 before retraining from the first-stage checkpoint with an updated output  20  layer.    21

All downstream comparisons used two architecture-matched baselines: (i) a supervised  22  pretraining baseline optimized to predict conventional five-stage sleep labels, and (ii) a no- 23  pretraining control initialized randomly and trained directly on each downstream task. For  24  downstream fine-tuning, the pretraining output layer was replaced with a task-specific regression  25  or classification head, and the full network was fine-tuned end-to-end using participant-level  26  cross-validation.  27

Fine-tuning experiments and statistical testing  28

To probe health information encoded in the representations, we fine-tuned each pretrained (or  29  scratch) model on APPLES for each outcome. Regression performance was evaluated by  30  Pearson correlation (r) and classification performance by accuracy. We used participant-level 10- 31  fold cross-validation: within each fold, participants were split into training (80%), validation (10%),  32  and test (10%) subsets, and the best validation checkpoint was evaluated on the held-out test  33  subset. Pairwise representation comparisons (SSL vs from-scratch; SSL vs five-stage pretraining)  34  used paired, fold-wise tests (Wilcoxon signed-rank). Nominal p-values were adjusted across the  35  15 APPLES outcomes using Benjamini–Hochberg false discovery rate (FDR) control and are  36  reported as q-values (q < 0.05).  37

Digital medicine evaluation: screening, calibration, and confound controls  38

<!-- page 16 -->

15

To evaluate participant-level screening rather than epoch-level prediction, we generated multiple  1  segment-level predictions per participant and summarized each participant by the mean model  2  output across segments. For binary screening tasks, continuous outcomes were thresholded  3  using established clinical cutoffs: AHI ≥ 15 and AHI ≥ 30, BMI ≥ 30, age ≥ 60 years, and sex;  4  additional functional thresholds used in exploratory analyses are listed in Supplementary Table  5  1. Screening discrimination was quantified using ROC curves and AUROC.  6

For severe-apnea screening (AHI ≥ 30), we additionally calibrated model scores to predicted  7  probabilities using out-of-fold Platt scaling and evaluated calibration with reliability curves and  8  Brier scores; clinical utility was assessed via decision curve analysis (DCA) against treat-all and  9  treat-none baselines.  10

To test whether SSL-derived signals provided incremental information beyond simpler  11  explanatory baselines, we conducted nested participant-level control analyses using four non- 12  overlapping feature sources: clinical/demographic covariates, conventional stage-derived sleep- 13  report summaries, conventional EEG spectral summaries, and target-specific scores from either  14  the SSL model or the matched five-stage-pretrained model. Covariates included age, sex, BMI,  15  and AHI with outcome-specific exclusions to avoid circularity. Stage summaries included standard  16  sleep-architecture features such as stage proportions, sleep efficiency, wake after sleep onset,  17  bout/transition statistics, and related hypnogram-derived measures. Spectral summaries included  18  conventional whole-night and NREM EEG features, including absolute and relative band power,  19  slowing ratios, spectral centroid, median/edge frequency, and aperiodic 1/f parameters. We  20  evaluated covariate-only, stage-only, spectra-only, model-score-only, covariate + stage, covariate  21  + stage + spectra, and fully adjusted models that added either the SSL score or the matched five- 22  stage-model score to the same covariate + stage + spectra baseline. SSL and five-stage scores  23  were not entered together, allowing a direct comparison of each learned representation against  24  identical non-transformer baselines. Models were evaluated with participant-level 5-fold cross- 25  validation; fold-wise AUROC differences were tested using exact paired sign-flip tests with FDR  26  correction within each comparison family. For continuous outcomes, we additionally assessed  27  incremental residual signal by correlating SSL and five-stage scores with out-of-fold residuals  28  after regressing out covariates, stage summaries, and spectral summaries (Spearman ρ).  29

Representation structure analyses and meta-state framework  30

To interpret what the models learn beyond traditional staging, we analyzed epoch-level  31  embeddings from the final transformer layer. Because transformer embeddings are contextual  32  over the 101-epoch input sequence, each embedding was indexed to the AASM label of the  33  corresponding focal 30-s epoch. These labels were used as anchors for interpretation, not as  34  evidence that the embedding reflected only that isolated epoch. Stage-composition summaries  35  were computed by aggregating focal-epoch AASM labels over embeddings assigned to each  36  microstate or meta-state. Embedding geometry was visualized with t-SNE/UMAP and related to  37  expert stage labels and participant phenotypes. To quantify within-night structure, we performed  38  per-recording k-means clustering on embeddings and selected the number of clusters  39  (“microstates”) using Bayesian Information Criterion (BIC) sweeps. We then introduced a meta- 40  state framework to summarize microstructure across participants: subject-specific microstates  41

<!-- page 17 -->

16

were pooled and clustered into a consistent set of M meta-states, and each participant was  1  represented by meta-state occupancy and diversity features. We used this two-step microstate- 2  to-meta-state procedure because the first step estimates recording-specific within-night structure,  3  including per-recording state granularity, whereas the second step aligns those local substates  4  into a shared cross-subject vocabulary. Direct pooled clustering would instead impose a single  5  global partition and fixed granularity on the cohort, and would be more strongly driven by the most  6  prevalent epochs/stages and longest recordings.   7

To avoid circular selection of M, we implemented nested cross-validation: an inner loop selected  8  M over a sweep (M = 3–15) using a stability-constrained performance-plateau criterion, and an  9  outer loop evaluated downstream prediction using the chosen meta-state features. We tested  10  whether meta-state features improved prediction beyond stage-only summaries by training linear  11  models on (i) stage-only features and (ii) stage summaries augmented with meta-state  12  occupancy/diversity, reporting mean out-of-fold AUROC (binary) or R² (continuous). To localize  13  incremental signal to canonical stages, we computed stage-conditional meta-state occupancies  14  (e.g., within-N2 or within-Wake occupancy independent of total time in that stage) and conducted  15  dominant-stage ablations in which meta-states dominated by N2 and/or Wake were selectively  16  excluded.  17

To assess robustness to modeling choices, we repeated the clustering-based analyses under  18  controlled perturbations. For the per-record microstate step, each recording’s selected k was held  19  fixed and k-means was rerun across 10 random initializations to quantify assignment  20  recoverability (ARI/AMI) and stage-anchored Rosetta-count stability. For the cross-subject meta- 21  state step, the APPLES M = 7 solution was rerun across 10 seeds; local sensitivity was  22  additionally assessed over M = 5–9 and PCA dimensionality of 10, 20, and 50. A fixed-k sensitivity  23  analysis near the empirical SSL median was used to verify that qualitative Rosetta/meta-state  24  conclusions were not dependent on BIC-selected k. Preprocessing was held fixed across  25  matched analyses to preserve representation-level comparability.  26

Analyses were implemented in Python (NumPy, pandas, scikit-learn, PyTorch).  27

Ethics Declaration  28    29  This study performed secondary analyses of existing, de-identified polysomnography datasets  30  accessed through established research repositories (including NSRR/SleepData.org and  31  PhysioNet) under their applicable data use terms. All datasets were originally collected under  32  approvals and consent processes managed by the respective parent studies; no new human- 33  participant recruitment or data collection was performed for this work.   34

## Data Availability  35

All datasets used in this study are publicly available. Model pretraining was performed using large- 36  scale publicly available polysomnographic datasets accessed through the National Sleep  37  Research Resource (SleepData.org), including MESA, MrOS, SHHS, WSC, SOF, CFS, and  38

<!-- page 18 -->

17

NCHSDB, comprising a total of 11,261 overnight recordings (Supplementary Table 3). Model  1  evaluation was conducted on held-out datasets not used for pretraining, including APPLES and  2  HomePAP (SleepData.org), as well as the Dreem Open dataset and Sleep-EDF, which are  3  available via PhysioNet. Access to these datasets is subject to dataset-specific data use  4  agreements and approval procedures. Because redistribution of raw polysomnographic  5  recordings is governed by these agreements, we do not host raw data; however, all preprocessing  6  and dataset construction scripts are provided to enable independent reconstruction of the analytic  7  cohorts from the original sources.  8

## Code Availability  9

All code used for data preprocessing, model training, evaluation, and figure generation, along with  10  trained model weights, is publicly available via the Open Science Framework (OSF) at  11  https://osf.io/j2mkh/. The repository includes documentation sufficient to reproduce the analyses  12  reported in this study.  13

## Acknowledgments  14

We thank the APL Research and Exploratory Development Department (REDD) for supporting  15  this work with an Independent Research and Development (IRAD) grant award. We also thank  16  the participants and investigators of the contributing sleep studies and repositories that made this  17  work possible. Data used for model pretraining and evaluation were accessed primarily through  18  the National Sleep Research Resource (NSRR/SleepData.org), including MESA, MrOS, SHHS,  19  WSC, SOF, CFS, NCHSDB, APPLES, and HomePAP, and additionally through PhysioNet  20  (including Sleep-EDF and the Dreem Open Dataset).  21    22  The Multi-Ethnic Study of Atherosclerosis (MESA) Sleep Ancillary study was funded by  23  NIH/NHLBI (R01 HL098433). MESA is supported by contracts HHSN268201500003I, N01-HC- 24  95159, N01-HC-95160, N01-HC-95161, N01-HC-95162, N01-HC-95163, N01-HC-95164, N01- 25  HC-95165, N01-HC-95166, N01-HC-95167, N01-HC-95168, and N01-HC-95169, and by  26  cooperative agreements UL1-TR-000040, UL1-TR-001079, and UL1-TR-001420 funded by  27  NCATS. The National Heart, Lung, and Blood Institute provided funding for the ancillary MrOS  28  Sleep Study (“Outcomes of Sleep Disorders in Older Men”) under the following grant numbers:  29  R01 HL071194, R01 HL070848, R01 HL070847, R01 HL070842, R01 HL070841, R01  30  HL070837, R01 HL070838, and R01 HL070839. The Study of Osteoporotic Fractures (SOF) is  31  supported by National Institutes of Health funding; the National Institute on Aging (NIA) provides  32  support under the following grant numbers: R01 AG005407, R01 AG005394, R01 AG027574,  33  R01 AG027576, R01 AG026720, and R01 AG035612. The Wisconsin Sleep Cohort (WSC) study  34  was supported by the National Institutes of Health, National Heart, Lung, and Blood Institute  35  (R01HL62252); National Institute on Aging (R01AG036838, R01AG058680); and the National  36  Center for Research Resources (1UL1RR025011). The APPLES study was supported by the  37  National Heart, Lung, and Blood Institute cooperative agreement U01HL68060. The HomePAP  38  study was supported by the American Sleep Medicine Foundation grant 38-PM-07. The Cleveland  39  Family Study (CFS) was supported by the National Heart, Lung, and Blood Institute under grant  40

<!-- page 19 -->

18

R01HL46380. The NCHSDB dataset was supported by the National Institute of Biomedical  1  Imaging and Bioengineering under grant R01EB025018. The National Sleep Research Resource  2  was supported by the National Heart, Lung, and Blood Institute (R24 HL114473, 75N92019R002).  3

## Author contributions  4

William Coon and Mattson Ogg contributed equally to this work. W.C. and M.O. jointly conceived  5  the study; designed the methodology; curated and processed the datasets; implemented the  6  software and experiments; performed the formal analyses; generated the figures and  7  visualizations; and wrote the original draft. W.C. and M.O. jointly reviewed and edited the  8  manuscript and approved the final version for submission.  9

## Competing Interests  10

The authors declare no competing financial or non-financial interests.  11    12

## References  13

14  1. Irwin, M. R. Why Sleep Is Important for Health: A Psychoneuroimmunology Perspective.  15

Annu. Rev. Psychol. 66, 143–172 (2015).   16

2. Kales, A. & Rechtschaffen, A. A Manual of Standardized Terminology, Techniques and  17

Scoring System for Sleep Stages of Human Subjects: Allan Rechtschaffen and Anthony  18

Kales, Editors. (U. S. National Institute of Neurological Diseases and Blindness,  19

Neurological Information Network, 1968).   20

3. Silber, M. H. et al. The Visual Scoring of Sleep in Adults. J. Clin. Sleep Med. 03, 121–131  21

(2007).   22

4. Himanen, S. L. & Hasan, J. Limitations of Rechtschaffen and Kales. Sleep Med. Rev. 4,  23

149–167 (2000).   24

5. Danker-Hopfe, H. et al. Interrater reliability for sleep scoring according to the Rechtschaffen  25

& Kales and the new AASM standard. J. Sleep Res. 18, 74–84 (2009).   26

6. Rosenberg, R. S. & Van Hout, S. The American Academy of Sleep Medicine Inter-scorer  27

Reliability Program: Sleep Stage Scoring. J. Clin. Sleep Med. JCSM Off. Publ. Am. Acad.  28

<!-- page 20 -->

19

Sleep Med. 9, 81–87 (2013).   1

7. Davidson, S., Sharman, R., Kyle, S. D. & Tarassenko, L. Is it time to revisit the scoring of  2

slow wave (N3) sleep? SLEEP zsaf063 (2025) doi:10.1093/sleep/zsaf063.   3

8. Brodbeck, V. et al. EEG microstates of wakefulness and NREM sleep. NeuroImage 62,  4

2129–2139 (2012).   5

9. Decat, N. et al. Beyond traditional sleep scoring: Massive feature extraction and data-driven  6

clustering of sleep time series. Sleep Med. 98, 39–52 (2022).   7

10. Stephansen, J. B. et al. Neural network analysis of sleep stages enables efficient diagnosis  8

of narcolepsy. Nat. Commun. 9, 5229 (2018).   9

11. Korkalainen, H. et al. Accurate Deep Learning-Based Sleep Staging in a Clinical Population  10

With Suspected Obstructive Sleep Apnea. IEEE J. Biomed. Health Inform. 24, 2073–2081  11

(2020).   12

12. Perslev, M. et al. U-Sleep: resilient high-frequency sleep staging. Npj Digit. Med. 4, 1–12  13

(2021).   14

13. Phan, H. et al. SleepTransformer: Automatic Sleep Staging with Interpretability and  15

Uncertainty Quantification. IEEE Trans. Biomed. Eng. 69, 2456–2467 (2022).   16

14. Yao, H., Liu, T., Zou, R., Ding, S. & Xu, Y. A Spatial-Temporal Transformer Architecture  17

Using Multi-Channel Signals for Sleep Stage Classification. IEEE Trans. Neural Syst.  18

Rehabil. Eng. 31, 3353–3362 (2023).   19

15. Hanna, J. & Flöel, A. An accessible and versatile deep learning-based sleep stage  20

classifier. Front. Neuroinformatics 17, (2023).   21

16. Kim, M., Jung, K. & Chung, W. Automatic Sleep Stage Classification Method based on  22

Transformer-in-Transformer. in 2023 11th International Winter Conference on Brain- 23

Computer Interface (BCI) 1–5 (IEEE, Gangwon, Korea, Republic of, 2023).  24

doi:10.1109/BCI57258.2023.10078607.   25

17. Huijben, I. A., Nijdam, A. A., Overeem, S., Van Gilst, M. M. & Van Sloun, R. Som-cpc:  26

<!-- page 21 -->

20

Unsupervised contrastive learning with self-organizing maps for structured representations  1

of high-rate time series. in International Conference on Machine Learning 14132–14152  2

(PMLR, 2023).   3

18. Zhang, W., Li, C., Peng, H., Qiao, H. & Chen, X. CTCNet: A CNN Transformer capsule  4

network for sleep stage classification. Measurement 226, 114157 (2024).   5

19. Coon, W. G. et al. ezscore-f: A Set of Freely Available, Validated Sleep Stage Classifiers for  6

Forehead EEG. bioRxiv 2025.06.02.657451 (2025) doi:10.1101/2025.06.02.657451.   7

20. Roberts, S. & Tarassenko, L. New method of automated sleep quantification. Med. Biol.  8

Eng. Comput. 30, 509–517 (1992).   9

21. Pardey, J., Roberts, S., Tarassenko, L. & Stradling, J. A new approach to the analysis of the  10

human sleep/wakefulness continuum. J. Sleep Res. 5, 201–210 (1996).   11

22. Stevner, A. B. A. et al. Discovery of key whole-brain transitions and dynamics during human  12

wakefulness and non-REM sleep. Nat. Commun. 10, 1035 (2019).   13

23. Hermans, L. Wa. et al. Representations of temporal sleep dynamics: Review and synthesis  14

of the literature. Sleep Med. Rev. 63, 101611 (2022).   15

24. Rosenblum, Y. et al. Fractal cycles of sleep, a new aperiodic activity-based definition of  16

sleep cycles. eLife 13, RP96784 (2025).   17

25. Huijben, I. A., Van Sloun, R. J. G., Pijpers, A., Overeem, S. & Van Gilst, M. M. Deep  18

clustering of polysomnography data to characterize sleep structure in healthy sleep and  19

non-rapid eye movement parasomnias. J. Neurosci. Methods 423, 110516 (2025).   20

26. Coravos, A., Khozin, S. & Mandl, K. D. Developing and adopting safe and effective digital  21

biomarkers to improve patient outcomes. Npj Digit. Med. 2, 14 (2019).   22

27. Vasudevan, S., Saha, A., Tarver, M. E. & Patel, B. Digital biomarkers: Convergence of  23

digital health technologies and biomarkers. Npj Digit. Med. 5, 36 (2022).   24

28. Wall, C., Hetherington, V. & Godfrey, A. Beyond the clinic: the rise of wearables and  25

smartphones in decentralising healthcare. Npj Digit. Med. 6, 219, s41746-023-00971-z  26

<!-- page 22 -->

21

(2023).   1

29. De Zambotti, M. et al. State of the science and recommendations for using wearable  2

technology in sleep and circadian research. SLEEP 47, zsad325 (2024).   3

30. Viswanath, V. K. et al. Five million nights: temporal dynamics in human sleep phenotypes.  4

Npj Digit. Med. 7, 150 (2024).   5

31. Cappuccio, F. P., Cooper, D., D’Elia, L., Strazzullo, P. & Miller, M. A. Sleep duration predicts  6

cardiovascular outcomes: a systematic review and meta-analysis of prospective studies.  7

Eur. Heart J. 32, 1484–1492 (2011).   8

32. Krause, A. J. et al. The sleep-deprived human brain. Nat. Rev. Neurosci. 18, 404–418  9

(2017).   10

33. Baglioni, C. et al. Sleep and mental disorders: A meta-analysis of polysomnographic  11

research. Psychol. Bull. 142, 969–990 (2016).   12

34. Sun, H. et al. Brain age from the electroencephalogram of sleep. Neurobiol. Aging 74, 112– 13

120 (2019).   14

35. Ye, E. et al. Association of Sleep Electroencephalography-Based Brain Age Index With  15

Dementia. JAMA Netw. Open 3, e2017357 (2020).   16

36. Sun, H. et al. Machine Learning–Based Sleep Electroencephalographic Brain Age Index  17

and Dementia Risk: An Individual Participant Data Meta-Analysis. JAMA Netw. Open 9,  18

e261521 (2026).   19

37. Ganglberger, W. et al. Brain Health from Sleep EEG: A Multicohort, Deep Learning  20

Biomarker for Cognition, Disease, and Mortality. NEJM AI 3, (2026).   21

38. Bommasani, R. et al. On the Opportunities and Risks of Foundation Models. Preprint at  22

https://doi.org/10.48550/arXiv.2108.07258 (2022).   23

39. Krishnan, R., Rajpurkar, P. & Topol, E. J. Self-supervised learning in medicine and  24

healthcare. Nat. Biomed. Eng. 6, 1346–1352 (2022).   25

40. Ogg, M. & Coon, W. G. Self-Supervised Transformer Model Training for a Sleep-EEG  26

<!-- page 23 -->

22

Foundation Model. in 2024 46th Annual International Conference of the IEEE Engineering in  1

Medicine and Biology Society (EMBC) 1–6 (2024).  2

doi:10.1109/EMBC53108.2024.10782281.   3

41. Siclari, F. & Tononi, G. Local aspects of sleep and wakefulness. Curr. Opin. Neurobiol. 44,  4

222–227 (2017).   5

42. Nir, Y. et al. Regional Slow Waves and Spindles in Human Sleep. Neuron 70, 153–169  6

(2011).   7

43. Nir, Y. & De Lecea, L. Sleep and vigilance states: Embracing spatiotemporal dynamics.  8

Neuron 111, 1998–2011 (2023).   9

44. Banville, H., Chehab, O., Hyvärinen, A., Engemann, D.-A. & Gramfort, A. Uncovering the  10

structure of clinical EEG signals with self-supervised learning. J. Neural Eng. 18, 046020  11

(2021).   12

45. Thapa, R. et al. A multimodal sleep foundation model for disease prediction. Nat. Med.  13

https://doi.org/10.1038/s41591-025-04133-4 (2026) doi:10.1038/s41591-025-04133-4.   14

46. Huang, W. et al. A unified time-frequency foundation model for sleep decoding. Nat.  15

Commun. 17, 1198 (2026).   16

47. Fox, B. et al. A foundational transformer leveraging full night, multichannel sleep study data  17

accurately classifies sleep stages. Sleep zsaf061 (2025) doi:10.1093/sleep/zsaf061.   18

48. Hsu, W.-N. et al. HuBERT: Self-Supervised Speech Representation Learning by Masked  19

Prediction of Hidden Units. IEEEACM Trans. Audio Speech Lang. Process. 29, 3451–3460  20

(2021).   21

49. Zhang, G.-Q. et al. The National Sleep Research Resource: towards a sleep data  22

commons. J. Am. Med. Inform. Assoc. 25, 1351–1358 (2018).   23

50. Lee, H. et al. A large collection of real-world pediatric sleep studies. Sci. Data 9, 421 (2022).   24

51. Chen, X. et al. Racial/Ethnic Differences in Sleep Disturbances: The Multi-Ethnic Study of  25

Atherosclerosis (MESA). Sleep 38, 877–888 (2015).   26

<!-- page 24 -->

23

52. Redline, S. et al. The familial aggregation of obstructive sleep apnea. Am. J. Respir. Crit.  1

Care Med. https://doi.org/10.1164/ajrccm.151.3.7881656 (2012)  2

doi:10.1164/ajrccm.151.3.7881656.   3

53. Blackwell, T. et al. Association of Sleep Characteristics and Cognition in Older Community- 4

Dwelling Men: the MrOS Sleep Study. Sleep 34, 1347–1356 (2011).   5

54. Young, T. et al. Burden of sleep apnea: rationale, design, and major findings of the  6

Wisconsin Sleep Cohort study. WMJ Off. Publ. State Med. Soc. Wis. 108, 246–249 (2009).   7

55. Spira, A. P. et al. Sleep-Disordered Breathing and Cognition in Older Women. J. Am.  8

Geriatr. Soc. 56, 45–50 (2008).   9

56. Quan, S. F. et al. The Sleep Heart Health Study: Design, Rationale, and Methods. Sleep 20,  10

1077–1085 (1997).   11

57. Guillot, A., Sauvet, F., During, E. H. & Thorey, V. Dreem Open Datasets: Multi-Scored Sleep  12

Datasets to Compare Human and Automated Sleep Staging. IEEE Trans. Neural Syst.  13

Rehabil. Eng. 28, 1955–1965 (2020).   14

58. Kemp, B., Zwinderman, A. H., Tuk, B., Kamphuisen, H. A. C. & Oberye, J. J. L. Analysis of a  15

sleep-dependent neuronal feedback loop: the slow-wave microcontinuity of the EEG. IEEE  16

Trans. Biomed. Eng. 47, 1185–1194 (2000).   17

59. Goldberger, A. L. et al. PhysioBank, PhysioToolkit, and PhysioNet: components of a new  18

research resource for complex physiologic signals. Circulation 101, E215-220 (2000).   19

60. Rosen, C. L. et al. A Multisite Randomized Trial of Portable Sleep Studies and Positive  20

Airway Pressure Autotitration Versus Laboratory-Based Polysomnography for the Diagnosis  21

and Treatment of Obstructive Sleep Apnea: The HomePAP Study. Sleep 35, 757–767  22

(2012).   23

61. Quan, S. F. et al. The Association between Obstructive Sleep Apnea and Neurocognitive  24

Performance—The Apnea Positive Pressure Long-term Efficacy Study (APPLES). Sleep 34,  25

303–314 (2011).   26

<!-- page 25 -->

24

62. Kushida, C. A. et al. Effects of Continuous Positive Airway Pressure on Neurocognitive  1

Function in Obstructive Sleep Apnea Patients: The Apnea Positive Pressure Long-term  2

Efficacy Study (APPLES). Sleep 35, 1593–1602 (2012).   3

63. Johns, M. W. A New Method for Measuring Daytime Sleepiness: The Epworth Sleepiness  4

Scale. Sleep 14, 540–545 (1991).   5

64. Beck, A. T., Ward, C. H., Mendelson, M., Mock, J. & Erbaugh, J. An Inventory for Measuring  6

Depression. Arch. Gen. Psychiatry 4, 561–571 (1961).   7

65. Hamilton, M. A Rating Scale for Depression. J. Neurol. Neurosurg. Psychiatry 23, 56–62  8

(1960).   9

66. McNair, D. M., Lorr, M. & Droppleman, L. F. POMS Manual for the Profile of Mood States.  10

(1971).   11

67. Wechsler, D. Wechsler Abbreviated Scale of Intelligence. https://doi.org/10.1037/t15170- 12

000 (2012).   13

68. Malanchini, M. et al. Pathfinder: a gamified measure to integrate general cognitive ability  14

into the biological, medical, and behavioural sciences. Mol. Psychiatry 26, 7823–7837  15

(2021).   16

69. Folstein, M. F., Folstein, S. E. & McHugh, P. R. “Mini-mental state”. J. Psychiatr. Res. 12,  17

189–198 (1975).   18

70. Buschke, H. Selective reminding for analysis of memory and learning. J. Verbal Learn.  19

Verbal Behav. 12, 543–550 (1973).   20

71. Gevins, A. et al. A cognitive and neurophysiological test of change from an individual’s  21

baseline. Clin. Neurophysiol. 122, 114–120 (2011).   22

72. Dinges, D. F. & Powell, J. W. Microcomputer analyses of performance on a portable, simple  23

visual RT task during sustained operations. Behav. Res. Methods Instrum. Comput. 17,  24

652–655 (1985).   25

73. de Gans, C. J. et al. Sleep assessment using EEG-based wearables – A systematic review.  26

<!-- page 26 -->

25

Sleep Med. Rev. 76, 101951 (2024).   1

74. Markov, K., Elgendi, M. & Menon, C. EEG-based headset sleep wearable devices. Npj  2

Biosensing 1, 12 (2024).   3

75. Esfahani, M. J. et al. Validation of the sleep EEG headband ZMax. Preprint at  4

https://doi.org/10.1101/2023.08.18.553744 (2023).   5

76. Sikder, N. et al. Wearanize+: A Multimodal Dataset for Evaluating Wearable Technologies in  6

Sleep Research. Preprint at https://doi.org/10.31219/osf.io/dth8y_v1 (2025).   7

77. van der Maaten, L. & Hinton, G. Visualizing data using t-SNE. J. Mach. Learn. Res. 9,  8

2579–2605 (2008).   9

78. Terzano, M. G. et al. Atlas, rules, and recording techniques for the scoring of cyclic  10

alternating pattern (CAP) in human sleep.   11

79. Lüthi, A. & Nedergaard, M. Anything but small: Microarousals stand at the crossroad  12

between noradrenaline signaling and key sleep functions. Neuron 113, 509–523 (2025).   13

14

<!-- page 27 -->

26

1  Figure 1 | Study overview: self-supervised sleep EEG pretraining, downstream probing, and head-to-head  2  evaluation. Sleep EEG recordings from 11,261 overnight studies were used to train and evaluate two architecture- 3  matched transformer models. The primary Sleep2.0 model was pretrained with self-supervised learning to learn general  4  EEG representations and sleep microstructure without sleep-stage labels. A matched supervised baseline was  5  pretrained to predict conventional five-stage sleep labels. Both models were then fine-tuned and evaluated across  6  diagnostic outcomes, including alertness, sleep staging, and apnea; demographic/trait-associated outcomes, including  7  BMI, age, and sex; and functional outcomes, including mood and cognition. Downstream comparisons assessed  8  predictive performance, discrimination, calibration, representation content, and electrophysiological/information  9  content—with a particular focus on the latter two—to determine what SSL learns beyond the conventional five-stage  10  interface.  11    12

<!-- page 28 -->

27

1  Figure 2 | Self-supervised foundation models encode more health-relevant information from sleep EEG than  2  supervised or non-pretrained models.  Fine-tuning performance on the APPLES dataset comparing models trained  3  from scratch, models pretrained to predict traditional five-stage sleep labels, and self-supervised (SSL) foundation  4  models. Outcomes are grouped by intended use: diagnostic sleep metrics, demographic variables, and functional  5  measures of mood and cognition. Dots indicate model–outcome pairs whose fine-tuning performance exceeds chance  6  (chance = 20% for 5-class staging, 50% for binary classification, and 0 correlation for continuous outcomes), using  7  FDR–adjusted q-values across the 45 SSL and baseline EEG-only models evaluated against chance (q < 0.05).  8  Diamonds denote outcomes where the SSL model significantly outperforms the from-scratch baseline (paired, fold- 9  wise Wilcoxon signed-rank test; nominal p with FDR correction across the 15 outcomes, q < 0.05). Asterisks denote  10  outcomes where the SSL model significantly outperforms the five-stage–pretrained baseline (paired, fold-wise Wilcoxon  11  signed-rank test; nominal p with FDR correction across the 15 outcomes, q < 0.05). Error bars show standard error of  12  the mean across folds. For transparency, we report nominal p values in the text and use q to denote FDR–adjusted  13  significance. Across outcomes, SSL pretraining improved performance relative to from-scratch training for several  14  tasks. Relative to the matched five-stage-pretrained model, FDR-corrected EEG-only advantages were clearest for BMI  15  and age, whereas AHI, sex, and functional outcomes showed smaller, nominal, or non-reliable differences. Cross- 16  validation was performed at the participant level (all segments and all nights per participant assigned to a single fold)  17  to prevent information leakage.  18    19

<!-- page 29 -->

28

1  Figure 3 | Subject-level screening evaluation from EEG-only foundation model outputs.   2  Segment-level predictions were aggregated to the participant level (mean across 50.5-min segments per subject) and  3  evaluated on all (n=1,044) held-out APPLES participants across representative diagnostic and demographic outcomes.  4  (a) Receiver operating characteristic (ROC) curves for apnea severity (AHI ≥ 15; AHI ≥ 30), BMI ≥ 30, Age ≥ 60, and  5  Sex (male). (b) Calibration curves after out-of-fold probability mapping. (c) Decision curve analysis (DCA) for AHI ≥ 30  6  showing net benefit across threshold probabilities relative to treat-all and treat-none strategies. (d) AUROC summary  7  across outcomes. (E–F) Robustness analyses reporting AUROC stratified by sex (e) and by age bin (<60 vs ≥60) (f)  8  for the indicated outcomes, shown alongside overall cohort performance.  9    10

<!-- page 30 -->

29

1  Figure 4 | SSL-derived EEG scores retain incremental information beyond demographic covariates,  2  conventional stage summaries, spectral summaries, and a supervised five-stage representational baseline.  3  Participant-level screening models were evaluated in APPLES using out-of-fold 5-fold cross-validation. Bars show  4  mean AUROC ± s.d. across folds for eight thresholded outcomes: (a) age ≥60 years, (b) AHI ≥15, (c) BMI ≥30, (d) sex,  5  (e) Buschke Selective Reminding Test ≤ lower quartile, (f) BDI ≥14, (g) WASI-IQ ≤85, and (h) Pathfinder ≤ lower  6  quartile. The numbered bars correspond to the feature blocks shown in the inset: 1, covariates only; 2, conventional  7  sleep-stage summary features only; 3, conventional spectral summary features only; 4, covariates + stage summaries;   8  5, covariates + spectral summaries; 6, covariates + stage summaries + spectral summaries; 7, target-specific score  9  from the matched five-stage-pretrained model; 8, target-specific SSL score; 9, covariates + stage summaries + five- 10  stage score; 10, covariates + stage summaries + spectral summaries + five-stage score; and 11, covariates + stage  11  summaries + spectral summaries + SSL score. Covariates were outcome-specific and excluded the target variable to  12  avoid circularity. Stage summaries were derived from ground-truth AASM staging and included sleep-efficiency,  13

<!-- page 31 -->

30

latency, stage-composition, transition, and bout-duration features. Spectral summaries included whole-night and NREM  1  band-power, relative-power, slowing-ratio, frequency-summary, and aperiodic 1/f-slope features. Models containing  2  both SSL and five-stage scores were not fit, so bars 10 and 11 compare the two representational baselines against the  3  same non-transformer feature set. Brackets indicate planned paired fold-wise comparisons using exact sign-flip tests;  4  asterisks denote p < 0.05; selected ROC curves with bootstrap confidence intervals shown in Supplementary Figure 2.  5  The rightmost two fully adjusted learned-representation models are bar 10 (covariates + stages + spectra + five-stage  6  score) and bar 11 (covariates + stages + spectra + SSL score). (i–k) Partial-residual associations for continuous AHI,  7  BMI, and age after regressing out covariates, stage summaries, and spectral summaries using out-of-fold ridge  8  regression. Residual outcome variance remained associated with the SSL score for AHI, BMI, and age, indicating  9  information not captured by conventional covariates, stage summaries, or spectral summaries alone. (l–n) Same as i- 10  k, but for the 5-stage-pretrained representations.    11    12

<!-- page 32 -->

31

1  Figure 5 | SSL-trained models recover the canonical sleep-stage scaffold across datasets. Two-dimensional t- 2  SNE visualizations of final-layer EEG embeddings from Sleep-EDF, HomePAP, Dreem, and APPLES (displayed are  3  up to n=151 records sampled at random from each, for visual clarity). For each dataset, embeddings are shown for the  4  SSL-pretrained model and the matched five-stage-supervised baseline, faceted by ground-truth AASM stage: Wake,  5  N1, N2, N3, and REM. Although the SSL model was pretrained without sleep-stage labels, its embeddings organize  6  epochs into stage-specific regions that broadly mirror the supervised five-stage representation across all four datasets.  7  At the same time, SSL embeddings retain visible within-stage dispersion, consistent with the idea that SSL recovers  8  the canonical stage scaffold while preserving additional structure collapsed by five-stage supervision.  9

10

<!-- page 33 -->

32

1  Figure 6 | Global sleep embedding atlases and an example subject’s projections onto SSL and five-stage  2  manifolds.  (a,b) Two-dimensional UMAP projections (“global manifolds”) of 30-s EEG epoch embeddings from a  3  foundation model pretrained with self-supervised learning (SSL; a) and a matched model trained with five-class sleep  4  stage supervision (five-stage; b). Points show all epochs used to form the global atlases and are colored by five-stage  5  sleep labels (Wake, N1, N2, N3, REM). (c) A representative subject’s SSL embeddings projected onto the SSL global  6  manifold and colored by that subject’s five-stage labels, illustrating where this night’s epochs fall within the population- 7  level SSL geometry. (d) The same subject’s five-stage embeddings projected onto the five-stage global manifold and  8  colored by five-stage labels. The SSL embedding in (c) forms compact, well-separated microstate islands, whereas the  9  stage-supervised embedding in (d) shows greater dispersion and overlap among microstates, consistent with reduced  10  expression of fine-grained structure under five-stage supervision. (e) The subject’s five-stage hypnogram across the  11  night (30-s epochs), using the same stage color scheme as panels (a–d). (f) The subject’s corresponding microstate  12  timeline, using arbitrary colors; each color corresponds to one of this subject’s microstates.  13    14

<!-- page 34 -->

33

1

Figure 7 | Example phenotype overlays on the global embedding atlases. (a) Left: SSL global manifold; right: five- 2  stage global manifold. Colored overlays illustrate continuous phenotype structure for age. (b) Same as in (a), but  3  overlaid colors represent AHI in the same cohort (APPLES). (c) SSL and 5-stage manifolds for N2 only shown in light  4  gray background. Colored overlays illustrate subject-level embedding centroids from N2 sleep, colored by ground truth  5  Age. (d) same as (c), but colors show subjects’ AHI scores (ground truth). (e) SSL and 5-stage global manifolds shown  6  in light gray background. Colored overlays illustrate binarized phenotype (Age) from N2 sleep epoch embeddings. (f)   7  Same as (e), but colors show binarized AHI in the same cohort.   8

9

<!-- page 35 -->

34

1  Figure 8 | Meta-states reveal phenotype-linked, spectrally distinct N2 microstructure beyond conventional  2  stage summaries. (a), Stage composition of the fixed EEG-only M=7 APPLES meta-state solution. Stacked bars show  3  P(stage∣meta-state) for Wake, N1, N2, N3, and REM, with meta-states ordered as m5, m1, m6, m0, m3, m2, and m4.  4  (b), Cross-validated predictive baselines for binary diagnostic/demographic contrasts using five-stage sleep- 5  architecture summaries alone (“Stage-only”) or the same summaries augmented with meta-state occupancy/diversity  6  features (“Stage + Meta”). (c), Subject-level associations between meta-state occupancy and continuous AHI, age, and  7

<!-- page 36 -->

35

BMI. Points show Spearman ρ, vertical intervals show 95% confidence intervals, and the stage-composition strip below  1  the axis repeats the stage profile of each meta-state. Asterisks denote Benjamini–Hochberg FDR-corrected significance  2  across meta-states within each phenotype (*q<0.05, **q<0.01, ***q<0.001). (d–f), Forced M = 7 control analysis using  3  embeddings from the matched five-stage-pretrained model. The same meta-state pipeline was applied to the five-stage  4  representation to preserve the clustering procedure, nominal state count, and feature dimensionality. (d), Stage  5  composition of the resulting five-stage pseudo-meta-state solution. (e), Cross-validated binary prediction using five- 6  stage summaries alone versus summaries augmented with five-stage pseudo-meta-state occupancy/diversity features,  7  plotted as in panel b. (f), Subject-level associations between five-stage pseudo-meta-state occupancy and continuous  8  AHI, age, and BMI, plotted as in panel c. This control did not reproduce the SSL stage+meta gains or the same  9  organized phenotype-association structure, indicating that the SSL results are not explained simply by adding features  10  or applying the same clustering pipeline to any transformer embedding. (g), Mean spectra for the three N2-linked meta- 11  states selected from the stage-composition analysis (m0, m3, and m6); shading denotes across-subject variability. (h– 12  j), Pairwise within-subject spectral contrasts between N2-linked meta-states, plotted as Δ power in dB for m0–m3, m0– 13  m6, and m3–m6. Numbers in panel titles indicate the number of subjects contributing valid spectra for both meta-states  14  in the contrast. Orange bars indicate frequency bins surviving FDR correction across frequency bins (q<0.05). (k),  15  Event-level NREM physiology for the three N2-linked meta-states, restricted to epochs scored as AASM N2. Spindle  16  density differed strongly across meta-states (Poisson GEE omnibus χ² = 294.61, p = 1.06×10⁻⁶⁴, q = 9.04×10⁻⁶⁴), with  17  m6 showing lower spindle density than m0/m3. Slow-oscillation density also differed across meta-states (χ² = 16.20, p  18  = 3.04×10⁻⁴, q = 3.69×10⁻⁴). (l,m), Regression-adjusted canonical-band contrasts among N2-linked meta-states using  19  all contributing epochs (l) or only epochs scored as AASM N2 (m). Heatmap values show adjusted log-band-power  20  contrasts in dB; positive values indicate greater adjusted band power in the first meta-state named in the row. Models  21  included subject fixed effects and aperiodic spectral covariates. Canonical bands were slow oscillation (SO, 0.5–1 Hz),  22  delta/slow-wave activity (1–4 Hz), theta (4–8 Hz), alpha (8–11 Hz), slow sigma (11–12.5 Hz), fast sigma (13–15 Hz),  23  and beta (15–25 Hz). Stars indicate BH-FDR-corrected significance across the canonical-band contrast family.  24  Persistence of spectral differences in the within-N2-only analysis supports the interpretation that N2-linked meta-states  25  capture electrophysiologically distinct within-stage structure, rather than only mixtures of neighboring AASM stages.    26

27

<!-- page 37 -->

# Supplementary Files

This is a list of supplementary files associated with this preprint. Click to download.

SupplementaryTable1.png

SupplementaryTable2.png

SupplementaryTable3.pdf

SupplementaryFiguresandTables.pdf