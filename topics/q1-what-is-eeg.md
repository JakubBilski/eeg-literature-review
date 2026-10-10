---
slug: q1-what-is-eeg
kind: hub
status: stub
updated: 2026-10-10
---

# q1-what-is-eeg

> What is EEG? What it measures, physiological origin, strengths and limits.

## Current answer
- EEG measures electrical activity of the brain through metal electrodes at multiple scalp sites, recording voltage fluctuations at millisecond temporal resolution [[sabio2024scoping]] (§Introduction).
- Analyzed either as spectral activity (oscillations) or as event-related potentials (ERPs, averaged responses to stimuli) [[sabio2024scoping]] (§Introduction).
- As data: a C × T matrix (C electrodes, usually placed by the international 10-20 system; T time samples set by duration × sampling rate) [[jiang2024large]] (§1).
- Origin, as far as the vault goes: the amplified spontaneous potential of "clusters of brain cells", reflecting the macroscopic activity of the brain surface [[chaddad2023electroencephalography]] (§1, §2.1). First recorded by Hans Berger in 1924 (§2.1).
- **Frequency bands:** delta 0.5–4, theta 4–8, alpha 8–13, beta 13–30, gamma >30 Hz, each loosely tied to a state (deep sleep … active attention) [[chaddad2023electroencephalography]] (§2.1). → [[frequency-bands]]
- **It's a potential difference:** each channel is measured against a reference electrode, and the data depend on that choice [[chaddad2023electroencephalography]] (§3).
- Strengths: non-invasive, relatively cheap, easy to use [[sabio2024scoping]] (§Introduction); [[song2022eeg]] (§I). Also safe, and can be combined with MRI, fNIRS and PET [[chaddad2023electroencephalography]] (§1).
- Limits: low signal-to-noise ratio and artifacts from impedance and other physiological signals [[song2022eeg]] (§I). Also non-stationarity, **volume conduction** (each electrode sums many sources, so localization is poor) and between-subject variability (skull thickness, conductivity, anatomy) [[chaddad2023electroencephalography]] (§3). → [[signal-quality-and-noise]]
- **Physiological origin:** scalp potentials of "tens of µV" arise "when tiny excitatory post-synaptic potentials produced by pyramidal neurons in the cortical layers of the brain sum together" [[roy2019deep]] (p. 2). 🤖 So EEG mainly sees the outer brain (cortex), and only where many neurons are active in sync. Why that is (geometry, synchrony) still needs a source: Lopes da Silva 2013 (*Neuron*, ref [3] in [[chaddad2023electroencephalography]]) is the candidate.
- **Time vs space:** excellent temporal resolution (milliseconds) but low spatial resolution. The skull and other tissue smear the fields, "as a result, EEG channels are often highly correlated spatially". Reconstructing the sources is the "inverse problem" [[roy2019deep]] (p. 2).
- **Regions do differ functionally**, e.g. imagined left- vs right-hand movement shows over the opposite side's motor cortex [[song2022eeg]] (§IV-H). Neighbouring electrodes are strongly correlated, though, not weakly: an extra electrode close to others "might not provide significantly different information" [[roy2019deep]] (p. 13). 🤖 Region-specific information is present, but blurred and spread across many correlated channels, which is why spatial filters (CSP, ICA, learned spatial convs) are central to EEG methods.

## Comparisons

## Open threads
- Physiological origin and the spatial resolution limits of EEG: no source yet.
- Why the bands map to brain states, and *how* coarse the spatial resolution is (in cm): not yet sourced.
- Why only synchronized cortical pyramidal neurons are visible (deep structures, cancellation): needs a physiology source.

## Sources
- [[roy2019deep]]: pyramidal-neuron origin, temporal vs spatial resolution, spatially correlated channels (p. 2) *(intro and selected sections only so far)*.
- [[chaddad2023electroencephalography]]: bands, the reference problem, volume conduction, the challenge list (§2.1, §3).
- [[sabio2024scoping]]: plain-language definition (intro of a device review).
- [[jiang2024large]]: EEG as data (matrix, 10-20 system).
- [[song2022eeg]]: noise and artifacts as the core difficulty.
