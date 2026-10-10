# Interests & reading queue

Questions the human asks are treated as signals of what matters. Maintained automatically.

## Recurring themes
<!-- - theme — count, last asked YYYY-MM-DD, where it's answered: [[note]] -->
- Signal decomposition methods (ICA, wavelets, EMD vs Fourier): 2 questions, last 2026-10-10 (ICA components, non-Gaussianity, why not least squares). Answered in [[signal-quality-and-noise]], [[time-frequency-analysis]].
- Reliability of reported accuracies / split leakage / confounds (depression, medication): 2, last 2026-10-10. [[eeg-depression-detection]], [[evaluation-protocols]].
- Classical ML baselines vs DL / foundation models (LDA, Riemannian): 2, last 2026-10-10. [[classical-ml-baselines]].
- Labels & metadata available with EEG: 1, 2026-10-10. [[eeg-labels-and-metadata]].
- Spatial structure (electrode placement, regional differences, channel correlation): 1, 2026-10-10. [[q1-what-is-eeg]], [[q2-measuring-devices]]; more in [[niso2022wireless]] (next read).

## Open questions
<!-- questions not yet answered by the vault; remove when answered (link the answer) -->
- Does EEG depression detection hold up across sites/datasets, or is it driven by single-site confounds? (2026-10-10) → [[eeg-depression-detection]]
- How strong are Riemannian / classical baselines against EEG foundation models on matched protocols? (2026-10-10) → [[classical-ml-baselines]]

## Reading queue
<!-- papers pointed to by questions or by reads: - citekey/title — why, from [[note]] -->
- Lopes da Silva 2013, "EEG and MEG: Relevance to neuroscience" (Neuron, doi 10.1016/j.neuron.2013.10.017): physiological origin of EEG, the main Q1 gap. Cited by [[chaddad2023electroencephalography]] as ref [3]. Older than 2022, so it is a candidate for the backward exception if 2022+ papers keep citing it. Not yet in screening.
- Lotte et al. 2018, "A Review of Classification Algorithms for EEG-based BCIs: A 10-year Update" (J. Neural Eng. 15(3)): Riemannian and classical baselines. Cited by [[roy2019deep]] as ref [105]. Backward-exception candidate; not yet in screening.
- A 2022+ review of EEG depression detection / biomarkers: to find via find-papers, from [[eeg-depression-detection]].
- [[wang2024cbramod]] — post-LaBraM foundation model, from [[q5-state-of-the-art]] (full text ready)
- [[roy2019deep]] — DL-for-EEG systematic review; confirms Q4 stages, from [[q4-evolution-of-methods]] (full text ready)
- [[yang2023biot]] — LaBraM's main baseline and split source, from [[jiang2024large]] (screening: maybe)
- Needs manual PDF: [[niso2022wireless]], [[kaongoen2023future]], [[gans2024sleep]], [[weng2025self]], [[wang2024eegpt]]
