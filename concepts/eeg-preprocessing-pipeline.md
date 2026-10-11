---
slug: eeg-preprocessing-pipeline
fields: [eeg, signal-processing, ml]
familiarity: introduced     # human's level: new | introduced | understood | skip
---

# eeg-preprocessing-pipeline

## Field-neutral description
The ordered chain of operations that turns a raw multichannel sensor recording into inputs for analysis or a model. It runs roughly: clean the signal, choose a reference, remove artifacts, cut it into trials, then compute features. Each step has its own concept note; this note is the map of how they fit together.

## Synonyms by community
- **EEG:** preprocessing, processing pipeline, "filtering steps", signal conditioning
- **Neuroscience / clinical:** —
- **Signal processing:** signal conditioning chain
- **General ML:** data pipeline / feature pipeline; in end-to-end DL, the part before the model

## The chain, in the usual order
The two vault reviews describe the same skeleton: raw EEG → preprocessing (denoising) → feature extraction → classification [[varbu2022past]] (§2, after Padfield 2019); [[chaddad2023electroencephalography]] (Fig. 2, §2.2–2.5). Details per step (🤖 typical practice unless cited):

| # | step | what it does | concept note | typical settings |
|---|---|---|---|---|
| 0 | **acquisition** | electrodes, amplifier, sampling | [[electrode-types]], [[signal-quality-and-noise]] | 250–500 Hz sampling ([[niso2022wireless]] §3.8) |
| 1 | **filtering (temporal)** | high-pass against drift, notch against mains noise, low-pass against high-frequency noise | [[digital-filtering]] | high-pass 0.1–1 Hz, notch 50/60 Hz, low-pass 40–100 Hz |
| 2 | **resampling** | reduce the sampling rate after low-pass (anti-aliasing) | [[digital-filtering]] | e.g. to 128–256 Hz; foundation models resample to ~200 Hz |
| 3 | **bad channels** | detect and interpolate dead or noisy electrodes | [[signal-quality-and-noise]] | impedance/variance checks |
| 4 | **re-referencing** | express each channel relative to a new reference: common average, linked mastoids, or a Laplacian (minus its neighbours) | [[channel-heterogeneity]] | common average is a frequent default; the reference choice matters ([[niso2022wireless]] §3.2) |
| 5 | **artifact removal** | remove eye, muscle and heart signals: regression, ICA, CCA, wavelet thresholding, EMD | [[independent-component-analysis]], [[signal-quality-and-noise]] | toolbox in [[chaddad2023electroencephalography]] (§2.2, Table 2) |
| 6 | **epoching** | cut fixed windows around events (cues, stimuli) or sliding windows; optional baseline correction | [[bci-paradigms]], [[evaluation-protocols]] | e.g. 0.5–3.5 s after a cue |
| 7 | **feature extraction** | temporal: band-pass to a band; spectral: PSD/FFT, STFT, wavelets, Hilbert envelope; spatial: CSP; covariance (Riemannian) | [[time-frequency-analysis]], [[frequency-bands]], [[common-spatial-patterns]], [[riemannian-methods]] | log band power per channel or per CSP component |
| 8 | **classifier** | LDA, SVM, … or a neural net | [[linear-discriminant-analysis]], [[classical-ml-baselines]] | LDA with shrinkage for BCI ([[varbu2022past]] Fig. 13) |

- **In deep learning**, steps 7–8 merge: the network takes lightly filtered, epoched EEG and learns temporal filters (conv over time) and spatial filters (conv over channels) itself [[song2022eeg]] (§III); [[lawhern2018eegnet]] (§1). Steps 1–6 mostly remain. 🤖 Choices there (filter band, reference, which epochs to drop) still change results and are a hidden source of incomparability across papers (→ [[evaluation-protocols]]).
- **Order matters** (🤖):
  - filter the continuous recording before epoching (edge effects);
  - low-pass before downsampling (aliasing);
  - high-pass before ICA (drift breaks its assumptions);
  - fit anything learned (ICA, CSP, normalization statistics) on training data only, or it leaks.

## Worked example in the vault
- EEGMMI imagined vs executed movement (2026-10-10): band-pass → Hilbert envelope → trial-average ERD for plots (`scripts/plot_motor_erd.py`). Band-pass 8–30 Hz → epochs 0.5–3.5 s → CSP → LDA for classification (`scripts/classify_imagery_vs_execution.py`). Results → [[bci-paradigms]].

## Papers
- [[varbu2022past]]: four-step skeleton; frequencies of feature and classifier choices (§2; Figs. 12–13).
- [[chaddad2023electroencephalography]]: the classical pipeline with the denoising toolbox in detail (Fig. 2, §2.2–2.5).
- [[niso2022wireless]]: acquisition side: sampling rate, reference, impedance (§3).

## Variants & disagreements
- Minimal vs heavy preprocessing before DL: whether the network should learn from near-raw data. No vault evidence on which is better.

## Open questions
- What preprocessing do foundation models (LaBraM, CBraMod) apply, and does it differ enough between pretraining corpora to matter?

## Related concepts
- every concept linked in the table above.
