---
slug: signal-quality-and-noise
fields: [eeg, neuro-clinical, signal-processing, ml]
familiarity: introduced     # human's level: new | introduced | understood | skip
---

# signal-quality-and-noise

## Field-neutral description
The measured signal is weak relative to unwanted contributions (other body signals, movement, poor sensor contact, electrical interference), so a lot of the effort in recording and modeling goes into getting a usable signal out of the noise.

## Synonyms by community
- **EEG:** low SNR, artifacts (eye blink, EMG, motion), impedance, noise floor, trial rejection
- **Neuroscience / clinical:** artifact, signal quality, test-retest reliability
- **Signal processing:** SNR, filtering, denoising, artifact removal
- **General ML:** label/input noise, robustness

## Papers
- [[song2022eeg]]: cites artifacts as the main decoding challenge (§I). Large pooling before attention helps, attributed to low SNR (§IV-G). Avoids noise augmentation because it lowers SNR (§IV-B).
- [[jiang2024large]]: reconstructing raw EEG "fails to converge", so it predicts the Fourier amplitude and phase instead (§2.2).
- [[chaddad2023electroencephalography]]: the classical denoising toolbox. Artifact types are EOG, ECG, EMG and environmental (§2.2). Methods: regression on an EOG channel (§2.2.1), ICA/PCA (§2.2.2), CCA (best for muscle artifacts, §2.2.3), wavelet thresholding (§2.2.4), EMD (§2.2.5), and hybrids (Table 2). Metrics: MSE/RMSE/SNR/PRD (§2.3).
- [[sabio2024scoping]]: consumer devices have a higher noise floor, more rejected trials, and poor connectivity estimates. Signal depends on headset fit (§Validation).

## How ICA "unmixes" (Q&A 2026-10-10)
- Model: X = A·S. X is the recording (channels × time), S holds independent sources (components × time), and A is the mixing matrix [[chaddad2023electroencephalography]] (§2.2.2, Eq. 2). Unmixing means estimating W ≈ A⁻¹ so that S = W·X. Training maximizes the *non-Gaussianity* of the sources (Algorithm 3).
- Each component therefore has a **time course** (a row of S) and a **scalp map** (a column of A: how strongly that source shows up at each electrode). Removing an artifact = zeroing its row of S and recomputing A·S.
- **Priors: none spatial, only statistical.** The model assumes sources are mutually independent and non-Gaussian, the mixing is linear and fixed over the recording, and there are no more sources than channels (🤖 standard ICA assumptions). The linear, instantaneous mixing is physically plausible because scalp fields are a smeared sum of sources [[roy2019deep]] (p. 2).
- The spatial and physiological knowledge comes *after* fitting. A human labels components by scalp map and time course (e.g. a blink is frontal and spiky) ([[chaddad2023electroencephalography]] §2.2.2: components "can be visually examined"). Artifact removal "usually require[s] the intervention of a human expert" [[roy2019deep]] (p. 16).
- Variants add priors: ERASE feeds extra EMG reference channels into ICA so muscle noise concentrates in a few components (26% more EMG removed) [[chaddad2023electroencephalography]] (§2.2.2).
- 🤖 ML view: like PCA, but the rotation is chosen for statistical independence instead of decorrelation and variance ranking. The components are unordered, and their sign and scale are arbitrary.
- **Number of components** is a user choice: `n_components` is an input in [[chaddad2023electroencephalography]] (Algorithm 3). 🤖 In practice it is usually the number of channels, or the data rank if PCA reduces dimensions first (e.g. after re-referencing or removing bad channels, which lowers the rank).
- **How non-Gaussianity is encouraged** (🤖 standard ICA theory; the vault only says "exploiting non-Gaussianity", Algorithm 3):
  - Why: by the central limit theorem, a sum of independent signals is *more* Gaussian than its parts. So the projections of the data that are *least* Gaussian are likely the original sources.
  - Steps: center and whiten (Algorithm 3), which leaves only a rotation to find. Then choose the rotation that maximizes a non-Gaussianity score. FastICA uses kurtosis or negentropy approximations. Infomax (the EEGLAB default) does maximum likelihood with a heavy-tailed prior on the sources.
- **Not least squares:** with a square, invertible A, *any* invertible W reconstructs X perfectly (zero MSE), so reconstruction error can't pick the solution. The problem is identifiability, not fitting. Whitening fixes everything except a rotation; independence and non-Gaussianity fix the rotation. Gaussian sources would be rotation-invariant and unidentifiable. 🤖 Reconstruction-based (MSE) objectives give PCA instead.

## Variants & disagreements
- Hardware side (electrodes, fit, conductive medium) vs model side (pooling, spectral targets). How much modeling can make up for hardware is unresolved in the vault.

## Open questions
- Standard artifact-handling pipelines: partly answered. [[chaddad2023electroencephalography]] lists the classical methods, but it doesn't cover ASR or the standard toolbox pipelines, and it doesn't test whether deep models still need denoising.
- Do deep / foundation models still need explicit artifact removal, or is it learned? Open. The vault has no head-to-head comparison.

## Related concepts
- [[consumer-grade-eeg-devices]]: lower signal quality is their main trade-off.
- [[cnn-transformer-hybrid]]: conv pooling as implicit denoising.
