---
slug: time-frequency-analysis
fields: [eeg, signal-processing, ml]
familiarity: introduced     # human's level: new | introduced | understood | skip
---

# time-frequency-analysis

## Field-neutral description
Describe a signal by which rhythms it contains *and when* they occur, rather than one or the other. This is useful when the rhythms change over time, so that a single global frequency summary would blur them together.

## Synonyms by community
- **EEG:** time–frequency representation (TFR), spectrogram, event-related spectral perturbation, band power over time
- **Neuroscience / clinical:** —
- **Signal processing:** STFT, wavelet transform (CWT/DWT), empirical mode decomposition (EMD), Wigner–Ville distribution, filter bank
- **General ML:** spectrogram input, multi-scale features. The DWT is a fixed (non-learned) conv + downsampling cascade.

## How the main methods differ (Q&A 2026-10-10)
| method | basis | time localisation | adaptive? |
|---|---|---|---|
| Fourier (FFT) | global sines over the whole window | none; assumes the signal is stationary | no |
| STFT / spectrogram | sines inside a sliding window | fixed window size for every frequency | no |
| Wavelet (DWT/CWT) | shifted and scaled copies of one short "wavelet" | short at high frequencies, long at low ones | no (basis chosen by hand) |
| EMD | none fixed; oscillations are peeled off using the signal's own envelopes | yes | yes (data-driven) |
- The DWT is computed as repeated low-pass/high-pass filtering. Each level halves the frequency band, giving "approximation" and "detail" coefficients [[chaddad2023electroencephalography]] (§2.2.4, Eq. 5–6). The plain DWT is not shift-invariant; the stationary WT fixes this at a cost in redundancy and speed (§2.2.4).
- EMD decomposes the signal into "intrinsic mode functions" plus a residual by repeatedly subtracting the envelope through local maxima and minima (§2.2.5, Eq. 7). It is sensitive to spikes ("mode splitting") (§2.2.5).
- 🤖 ML view: Fourier and STFT give fixed global or windowed features. Wavelets are a hand-designed multi-scale filter bank, i.e. what the first conv layers of EEGNet/Conformer learn instead. EMD is adaptive but unlearned and has no closed-form basis, which makes it harder to compare across signals.

## Papers
- [[chaddad2023electroencephalography]]: wavelets and EMD for denoising (§2.2.4–2.2.5); time–frequency analysis as a feature family (§2.4.1).
- [[jiang2024large]]: tokenizer targets are the Fourier amplitude and phase of 1 s patches (§2.2), i.e. a per-patch short-time Fourier view.

## Variants & disagreements
- Fixed basis (Fourier, wavelets) vs data-driven (EMD) vs learned (CNN filters). There is no vault evidence yet on which works best as model input.

## Open questions
- Do foundation models benefit from spectral inputs/targets over raw waveforms? LaBraM says raw reconstruction fails to converge (§2.2). Check CBraMod/BIOT.

## Related concepts
- [[frequency-bands]]: band power is the coarsest time–frequency summary.
- [[signal-quality-and-noise]]: wavelet/EMD thresholding as denoising.
