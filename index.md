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
- [[eeg-labels-and-metadata]] — what labels/metadata come with EEG recordings
- [[eeg-depression-detection]] — is depression detection from EEG as easy as reported? (open)

## Recently read
<!-- newest first: - YYYY-MM-DD [[citekey]] — one line -->
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

## Concepts
[[bci-paradigms]] · [[channel-heterogeneity]] · [[cnn-transformer-hybrid]] · [[common-spatial-patterns]] · [[computed-tomography]] · [[consumer-grade-eeg-devices]] · [[digital-filtering]] · [[domain-adaptation]] · [[eeg-preprocessing-pipeline]] · [[electrode-types]] · [[emotion-recognition]] · [[evaluation-protocols]] · [[frequency-bands]] · [[independent-component-analysis]] · [[linear-discriminant-analysis]] · [[magnetic-resonance-imaging]] · [[riemannian-methods]] · [[self-supervised-pretraining]] · [[seizure-detection]] · [[signal-quality-and-noise]] · [[sleep-staging]] · [[time-frequency-analysis]]

## See also
- [[interests]] — what the human asks about; reading queue
- [[log]] — session log
