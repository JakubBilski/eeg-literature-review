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
- [[chaddad2023electroencephalography]]: the classical denoising toolbox. Artifact types are EOG, ECG, EMG and environmental (§2.2). Methods: regression on an EOG channel (§2.2.1), ICA/PCA (§2.2.2, see [[independent-component-analysis]]), CCA (best for muscle artifacts, §2.2.3), wavelet thresholding (§2.2.4), EMD (§2.2.5), and hybrids (Table 2). Metrics: MSE/RMSE/SNR/PRD (§2.3).
- [[sabio2024scoping]]: consumer devices have a higher noise floor, more rejected trials, and poor connectivity estimates. Signal depends on headset fit (§Validation).

## Variants & disagreements
- Hardware side (electrodes, fit, conductive medium) vs model side (pooling, spectral targets). How much modeling can make up for hardware is unresolved in the vault.

## Open questions
- Standard artifact-handling pipelines: partly answered. [[chaddad2023electroencephalography]] lists the classical methods, but it doesn't cover ASR or the standard toolbox pipelines, and it doesn't test whether deep models still need denoising.
- Do deep / foundation models still need explicit artifact removal, or is it learned? Open. The vault has no head-to-head comparison.

## Related concepts
- [[consumer-grade-eeg-devices]]: lower signal quality is their main trade-off.
- [[cnn-transformer-hybrid]]: conv pooling as implicit denoising.
- [[independent-component-analysis]]: the main classical artifact-removal method.
