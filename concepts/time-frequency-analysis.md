---
slug: time-frequency-analysis
fields: [eeg, signal-processing, ml]
familiarity: introduced     # human's level: new | introduced | understood | skip
---

# time-frequency-analysis

## Field-neutral description
Describe a signal by which rhythms it contains *and when* they occur, rather than one or the other. This is useful when the rhythms change over time, so that a single global frequency summary would blur them together.

## Synonyms by community
- **EEG:** time–frequency representation (TFR), spectrogram, event-related spectral perturbation (ERSP), band power over time, ERD/ERS
- **Neuroscience / clinical:** —
- **Signal processing:** STFT, wavelet transform (CWT/DWT), Hilbert transform / analytic signal, empirical mode decomposition (EMD), Wigner–Ville distribution, filter bank
- **General ML:** spectrogram input, multi-scale features. The DWT is a fixed (non-learned) conv + downsampling cascade.

Where this sits in the processing chain → [[eeg-preprocessing-pipeline]]. Isolating one band beforehand → [[digital-filtering]].

## The toolbox in plain language
*🤖 Textbook material, written for an ML reader; no vault source unless one is cited. Sampling rate = `fs` samples/s. The highest representable frequency is fs/2 (Nyquist), e.g. 80 Hz for EEGMMI at 160 Hz.*

### Fourier transform (FFT) and power spectrum (PSD)
- **Idea:** any window of N samples can be written exactly as a sum of sines and cosines at frequencies 0, fs/N, 2·fs/N, … up to fs/2. The FFT computes how much of each (amplitude and phase) in O(N log N). Each output bin is a dot product of the signal with a sinusoid, i.e. a **fixed linear projection onto a sinusoid basis**.
- **Power spectral density (PSD):** squared amplitude per frequency, i.e. "how much energy at each frequency". Band power = sum of PSD over e.g. 8–12 Hz.
- **Frequency resolution = 1/window length:** 1 s of data gives 1 Hz bins, 4 s gives 0.25 Hz bins.
- **Welch's method:** split the window into overlapping segments, FFT each, average the spectra. It is noisier per bin but much less variance. This is what "PSD features" usually means.
- **Limitation:** a single FFT over the whole window loses *when* things happened. A burst at the start looks the same as one at the end. Fine for stationary signals (e.g. resting EEG), wrong for event-related changes.
- **Windowing:** cutting a window out abruptly creates fake high frequencies at the edges ("spectral leakage"). Multiplying by a taper (Hann, Hamming) first reduces this.

### Short-time Fourier transform (STFT) = sliding-window FFT = spectrogram
- Slide a window (e.g. 1 s, step 0.1 s) along the signal and FFT each window. The result is a 2-D image, **time × frequency → power**: the spectrogram.
- **One fixed window for all frequencies.** That forces a trade-off: long windows give sharp frequency but blurred timing; short windows the opposite. A 0.5 s window can't resolve 1 Hz differences, and a 4 s window can't tell when within those 4 s something happened.
- ML view: a 1-D conv with fixed sinusoidal kernels of one length, stride = hop size.

### Wavelets (CWT / DWT)
- Replace "sinusoid in a fixed window" with **one short wave-shaped kernel (the wavelet), stretched or squeezed** for each frequency. Squeezed = high frequency, short in time; stretched = low frequency, long in time.
- So time resolution adapts to frequency: sharp timing at high frequencies, sharp frequency at low ones. This often suits EEG better than one window size.
- **Morlet wavelet:** a sinusoid under a Gaussian envelope. The standard choice for EEG time–frequency plots; the number of cycles (e.g. 7) sets the trade-off.
- **CWT** (continuous): many scales, redundant, used for plots. **DWT** (discrete): repeated low-pass/high-pass filtering, each level halving the band, giving "approximation" and "detail" coefficients [[chaddad2023electroencephalography]] (§2.2.4, Eq. 5–6). The plain DWT is not shift-invariant; the stationary WT fixes this at a cost in redundancy and speed (§2.2.4).
- ML view: a hand-designed multi-scale conv filter bank, which is what EEGNet/Conformer's first temporal conv layers learn instead.

### Band-pass filter + Hilbert transform (envelope and phase)
- First [[digital-filtering|band-pass]] the signal to one band (e.g. 8–12 Hz), so it looks like a single wobbly sinusoid.
- The **Hilbert transform** makes the matching 90°-shifted copy (sine for a cosine). Treating signal + i·copy as a complex number (the "analytic signal") gives, at every sample:
  - **amplitude / envelope** = its magnitude, i.e. how big the oscillation is right now (squared = instantaneous power);
  - **phase** = its angle, i.e. where in the cycle it is right now.
- Computed by FFT: transform, zero the negative frequencies, double the positive ones, inverse FFT.
- It only makes sense on a narrow band. On broadband EEG the "instantaneous phase" is meaningless.
- Time resolution is limited by the band-pass filter's length, not by an FFT window. Mathematically this is close to a Morlet wavelet at one frequency.
- Uses: band-power time courses (ERD, below), phase synchrony between channels (connectivity), phase–amplitude coupling.

### Empirical mode decomposition (EMD)
- Data-driven: no fixed basis. It repeatedly peels off the fastest oscillation by subtracting the mean of the envelopes through local maxima and minima, giving "intrinsic mode functions" plus a residual (§2.2.5, Eq. 7). It is sensitive to spikes ("mode splitting") (§2.2.5) [[chaddad2023electroencephalography]].

### The common thread: you can't have sharp time and sharp frequency at once
- To know a frequency precisely you must watch several cycles, which takes time. Every method above picks a point on this trade-off (time–frequency uncertainty): the FFT is all frequency, raw samples are all time, STFT is a fixed compromise, and wavelets and the Hilbert transform use a compromise that depends on frequency.

## Comparison
| method | basis | time localisation | adaptive? |
|---|---|---|---|
| Fourier (FFT) / PSD | global sines over the whole window | none; assumes the signal is stationary | no |
| STFT / spectrogram | sines inside a sliding window | fixed window size for every frequency | no |
| Wavelet (DWT/CWT) | shifted and scaled copies of one short "wavelet" | short at high frequencies, long at low ones | no (basis chosen by hand) |
| band-pass + Hilbert | one band at a time | per sample (smoothed by the filter's length) | no |
| EMD | none fixed; oscillations are peeled off using the signal's own envelopes | yes | yes (data-driven) |
- 🤖 ML view: Fourier and STFT give fixed global or windowed features. Wavelets are a hand-designed multi-scale filter bank. EMD is adaptive but unlearned and has no closed-form basis, which makes it harder to compare across signals.

## Band power over time and ERD% (Q&A 2026-10-10)
How `scripts/plot_motor_erd.py` computes "mu power" for [[bci-paradigms]]:
1. **Band-pass filter** each trial to 8–12 Hz, so only the mu rhythm remains (the blue trace in the figure).
2. **Hilbert transform → envelope:** the instantaneous amplitude of that oscillation at every sample. Squaring it gives instantaneous power.
3. **Average power over trials** (~21 per subject per condition).
4. **Normalize to rest:** ERD% = (P(t) − R) / R × 100, where R is the mean power from −1.5 to −0.25 s before the cue. Negative = desynchronization (ERD); positive = synchronization (ERS). 🤖 This is the classic Pfurtscheller definition (no vault source yet).
5. Smooth with a 250 ms moving average, then average over subjects.
- **Average power, not raw voltage.** 🤖 The mu rhythm's phase is random relative to the cue (*induced*, non-phase-locked activity). Averaging raw traces would cancel it out, so power is taken per trial *before* averaging. *Evoked* (phase-locked) responses such as ERPs survive raw averaging. The bump ~0.25 s after the cue shows up in power because evoked responses also carry power.
- **Equivalent alternatives:** STFT (sum the 8–12 Hz bins) or Morlet wavelets give the same picture, with different time/frequency smoothing. A **PSD feature**, as counted in [[varbu2022past]] (Fig. 12), is the time-collapsed version: one FFT/Welch estimate per trial window, so one number per band per channel.

## Papers
- [[chaddad2023electroencephalography]]: wavelets and EMD for denoising (§2.2.4–2.2.5); time–frequency analysis as a feature family (§2.4.1).
- [[varbu2022past]]: PSD (23/126) and Fourier (20/126) are the most common BCI features, wavelets 8/126 (Fig. 12).
- [[wang2024cbramod]]: FFT-magnitude branch added to a conv branch in the patch encoder; frequency-only input is worst (FACED 0.521 vs time-only 0.544, both 0.551; Table 17). The authors' reading: the waveform contains the spectrum implicitly, but FFT magnitude loses timing (App. I).
- [[jiang2024large]]: tokenizer targets are the Fourier amplitude and phase of 1 s patches (§2.2), i.e. a per-patch short-time Fourier view.
- [[li2022eeg]]: DWT levels mapped to EEG bands at 128 Hz (A5 ≈ δ, D5 ≈ θ, D4 ≈ α, D3 ≈ β, D2 ≈ γ; Table 1); wavelet energy and entropy per level as features. Recommends wavelets over STFT for non-stationary EEG (§3.4, pp. 6–7). Also EMD/VMD (p. 7).
- [[weng2025self]]: time–frequency views as SSL targets: masked reconstruction of continuous-wavelet maps with a ViT, per-band reconstruction, and Fourier magnitude + phase prediction (neuro2vec) (§4.2).
- [[kuruppu2026eeg]]: FM input choices: raw time series (6/10), power spectra (BIOT, EEGFormer), time series + spectra (Brant, FoME), per-channel STFT/superlet spectrograms (BrainBERT, BrainWave). No ablation settles which is better (§4.1, §5.2).
- [[xie2026specbram]]: the statistical argument for power over phase. For a stationary Gaussian segment, Fourier phases are uniform and independent of the state, the periodogram is sufficient, and log band power has state-independent variance ≈ 1/(number of bins) (App. A, Props. 1–3). 🤖 Explains why spectral features are robust targets and why raw-waveform losses chase irreducible detail.

## Variants & disagreements
- Fixed basis (Fourier, wavelets) vs data-driven (EMD) vs learned (CNN filters). There is no vault evidence yet on which works best as model input.

## Open questions
- Do foundation models benefit from spectral inputs/targets over raw waveforms? LaBraM says raw reconstruction fails to converge (§2.2). *Partial (2026-10-25):* CBraMod's raw-patch MSE converges (Fig. 6) and is competitive; as *input*, spectrum alone is worse than waveform (Table 17). As *target*, band power beats raw reconstruction on sleep in a matched study → [[xie2026specbram]], [[q9-pretraining-objectives-and-scale]]. BIOT unchecked.

## Related concepts
- [[digital-filtering]]: a band-pass filter is the first step of the Hilbert route; the DWT is a filter cascade.
- [[frequency-bands]]: band power is the coarsest time–frequency summary.
- [[eeg-preprocessing-pipeline]]: where time–frequency features sit in the chain.
- [[signal-quality-and-noise]]: wavelet/EMD thresholding as denoising.
