# EEG literature review — home

## Core questions (hubs)
- [[q1-what-is-eeg]]
- [[q2-measuring-devices]]
- [[q3-typical-tasks]]
- [[q4-evolution-of-methods]]
- [[q5-state-of-the-art]]
- [[q6-reliability-of-eeg-diagnoses]]
- [[q7-foundation-models-vs-baselines]]
- [[q8-commercial-eeg-analysis-systems]]
- [[q9-pretraining-objectives-and-scale]]

## Other topics
<!-- synthesis notes not owned by a single hub -->
- [[classical-ml-baselines]] — classical EEG classifiers (LDA, CSP, Riemannian) and how much DL beats them
- [[eeg-labels-and-metadata]] — what labels/metadata come with EEG recordings; why no common task makes a good FM benchmark
- [[eeg-depression-detection]] — is depression detection from EEG as easy as reported? (open)

## Recently read
<!-- newest first: - YYYY-MM-DD [[citekey]] — one line -->
- 2026-10-25 [[kontras2026neuroatlas]] — NeuroAtlas: frozen linear probes, 20 models, 42 datasets with clinical metrics; EEG-FMs ≈ time-series FMs, seizures often ≈ random init (only NeuroLM/REVE consistent), supervised sequence/feature models win sleep and brain age, LODO costs 24–45%, MI drops to chance after eye-movement confound filtering
- 2026-10-12 [[bomatter2025limited]] — people vs data per person on TUAB, CAUEEG, sleep: people dominate one-label-per-person diagnosis, sleep is the exception; LaBraM pretraining helps except at the smallest data; augmentations don't
- 2026-10-12 [[chen2026benchmarking]] — EEG-Arena: 30 FMs vs 25 supervised baselines, 57 tasks; FMs win most tasks (margins ~2× larger within-subject), pretraining beats scratch more with more labels, no size scaling, REVE-base +4–7 points from 600 → 30k h; single runs, no classical pipeline
- 2026-10-12 [[xie2026specbram]] — SpecBraM: matched ablation; band-power target beats raw-waveform reconstruction for frozen sleep features (+2–3, +5–7 points at 1% labels), not for MI/vigilance; full TUEG ≈ 2,388 h
- 2026-10-11 [[liu2026eeg]] — EEG-FM-Compass: survey of 55 FMs + matched benchmark of 12; specialists tie FMs cross-subject and win few-shot, probes weak, no scaling
- 2026-10-11 [[coppola2024hubert]] — HuBERT-ECG (ECG method parallel): k-means pseudo-labels on MFCC then latent features, 9.1M ECGs; same recipe as Sleep2.0 → bridge [[hubert-style-pseudo-labels]]
- 2026-10-11 [[kuruppu2026eeg]] — critical review of the first 10 EEG foundation models: transformers + masked reconstruction, weak linear probes, weak scaling evidence, mostly in-distribution tests
- 2026-10-11 [[weng2025self]] — survey of ~70 EEG self-supervised methods (2019–2023): predictive / generative / contrastive / hybrid taxonomy; no performance numbers, no foundation models
- 2026-10-11 [[lawhern2018eegnet]] — EEGNet: ~2k-parameter CNN that mimics FBCSP; matches paradigm-specific pipelines on 4 BCI paradigms, loses to Riemannian on cross-subject ERN
- 2026-10-11 [[roy2019deep]] — systematic review of 156 DL-EEG papers (2010–2018): CNNs on raw EEG take over, median +5.4% vs weak baselines, 7% reproducible
- 2026-10-11 [[li2022eeg]] — tutorial review of EEG emotion recognition: labels, features, DL routes, cross-subject transfer, leaky segment splits
- 2026-10-11 [[wong2023eeg]] — review of 10 public seizure EEG datasets; the most used (Bonn) is the least realistic
- 2026-10-11 [[gans2024sleep]] — systematic review of 34 EEG sleep wearables; 24 validated against PSG, κ 0.42–0.79, N1 poorly detected
- 2026-10-10 [[varbu2022past]] — systematic review of 202 EEG-BCI application papers (2009–2019): paradigms, devices, LDA/SVM era
- 2026-10-10 [[niso2022wireless]] — survey of 48 wireless EEG devices (spec glossary) and 110 studies using them
- 2026-10-10 [[chaddad2023electroencephalography]] — review of the classical EEG pipeline: denoising, features, SVM-era classifiers
- 2026-10-10 [[jiang2024large]] — LaBraM: first large EEG foundation model (2,535 h, masked token prediction)
- 2026-10-10 [[song2022eeg]] — EEG Conformer: CNN + Transformer, per-subject, common baseline
- 2026-10-10 [[sabio2024scoping]] — scoping review of consumer-grade EEG devices (916 studies)

## Experiments
<!-- own tests; status · cost · core questions -->
- [[eegmmi-imagined-vs-executed]] — done · low · Q3/Q6/Q7: CSP + LDA "decodes" imagined vs executed only via recording-block identity
- [[eegmmi-frozen-probe]] — planned · medium · Q7: frozen FM probe vs CSP / Riemannian / EEGNet, few-shot MI
- [[pretext-loss-anomaly-score]] — idea · medium · Q9/Q6: is masked-prediction error more than a power detector?
- [[covariance-pseudo-labels]] — idea · high · Q9: filter-bank covariance k-means as HuBERT targets
- [[cross-channel-phase-target]] — idea · high · Q9: per-channel phase-invariant, cross-channel phase-aware target for TUEV
- [[pretext-downstream-scaling-sweep]] — idea · high · Q9/Q7: size × data × target sweep: per-target scaling curves, held-out pretext loss
- [[subject-diversity-gap]] — idea · medium · Q9/Q7/Q6: does subject count gate the benefit of model size (CNN 10k→1M, CBraMod)? v3 (2026-10-12): TUAB main, sleep as contrast, CNN + transformer, H5 = does limiting repetitions make bigger models win?
- [[property-probe-battery]] — idea · medium · Q9/Q7: probe frozen FMs for signal properties (spectral, spatial phase, morphology, nuisance), then predict downstream ranks
- [[embedding-data-diagnostics]] — idea · medium · Q6/Q7/Q9: frozen-FM embeddings as a data lens: noise vs nuisance variance, does embedding distance predict cross-cohort transfer drop beyond band power / random init, does geometry locate scorer disagreement (sleep)

## Bridges (ECG ↔ EEG)
- [[hubert-style-pseudo-labels]] — HuBERT-ECG and Sleep2.0 share the k-means pseudo-label recipe (plausible)

## Concepts
[[bci-paradigms]] · [[channel-heterogeneity]] · [[cnn-transformer-hybrid]] · [[common-spatial-patterns]] · [[computed-tomography]] · [[consumer-grade-eeg-devices]] · [[digital-filtering]] · [[domain-adaptation]] · [[eeg-preprocessing-pipeline]] · [[electrode-types]] · [[emotion-recognition]] · [[evaluation-protocols]] · [[frequency-bands]] · [[independent-component-analysis]] · [[linear-discriminant-analysis]] · [[magnetic-resonance-imaging]] · [[riemannian-methods]] · [[self-supervised-pretraining]] · [[seizure-detection]] · [[signal-quality-and-noise]] · [[sleep-staging]] · [[time-frequency-analysis]]

## See also
- [[interests]] — what the human asks about; reading queue
- [[log]] — session log
