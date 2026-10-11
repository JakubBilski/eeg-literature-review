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
- [[niso2022wireless]]: the hardware side. Gel/wet/dry and active/passive electrodes (§3.4–3.5, see [[electrode-types]]); continuous impedance monitoring can flag noisy segments for post-hoc analysis (§3.6); CMRR measures rejection of interference common to all electrodes (§3.7). Motion artifacts grow with mobility and become a confound when they differ between conditions, e.g. walking vs sitting (p. 3).
- [[sabio2024scoping]]: consumer devices have a higher noise floor, more rejected trials, and poor connectivity estimates. Signal depends on headset fit (§Validation).

- [[gans2024sleep]]: in sleep wearables, quality is reported as feasibility (artifact share, recording success rate, compliance), e.g. Dreem <20% artifacts, Cerebra 83% success (p. 9). It is validated by agreement with a simultaneous PSG, not by signal metrics (Table 1).
- [[wong2023eeg]]: intracranial EEG has a higher signal-to-noise ratio than scalp EEG and is less affected by artifacts and the environment (§7).

## Variants & disagreements
- **Is "noise" well-posed?** (discussed 2026-10-10) Only in part.
  - *Well-posed, task-independent:* noise the device adds, measurable without a brain: amplifier input noise (mostly ≈0.05–1 µVrms, but Enobio 10–100), CMRR, quantisation step [[niso2022wireless]] (Table 1, §3.7, §3.9). This is small next to scalp EEG's "tens of µV" [[roy2019deep]] (p. 2).
  - *Task-relative:* 🤖 the larger parts (electrode–skin contact, muscle, eyes, movement, coverage) only count as noise relative to a target. Blinks are artifacts for ERP work but signal for drowsiness detection. "Quality" is then the information a (device, setup, person) recording carries about a given target. ML analogue: mutual information with the label, not a sensor spec.
  - *Shared yardsticks:* well-known effects act as unit tests across devices, e.g. alpha rising with eyes closed (the Berger effect), SSVEP and ERP components [[sabio2024scoping]] (§Validation). → [[q2-measuring-devices]]
- Hardware side (electrodes, fit, conductive medium) vs model side (pooling, spectral targets). How much modeling can make up for hardware is unresolved in the vault.

## Open questions
- Standard artifact-handling pipelines: partly answered. [[chaddad2023electroencephalography]] lists the classical methods, but it doesn't cover ASR or the standard toolbox pipelines, and it doesn't test whether deep models still need denoising.
- Do deep / foundation models still need explicit artifact removal, or is it learned? Open. The vault has no head-to-head comparison.

## Related concepts
- [[consumer-grade-eeg-devices]]: lower signal quality is their main trade-off.
- [[cnn-transformer-hybrid]]: conv pooling as implicit denoising.
- [[independent-component-analysis]]: the main classical artifact-removal method.
- [[electrode-types]]: the main hardware-side factor.
