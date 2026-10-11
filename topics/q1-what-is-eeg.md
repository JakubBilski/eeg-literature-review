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

## Is EEG redundant to imaging? (asked 2026-10-11)
*Mostly textbook knowledge (🤖, unsourced). Candidate sources added to screening: [[bitar2024utility]] (ICU continuous EEG), [[bank2022structural]] (MRI in new focal epilepsy), [[riha2022multimodal]], [[nascimento2023focal]].*

- 🤖 **The ECG analogy is the right one, but it cuts the other way.** ECG isn't an inferior CT. It measures the heart's *electrical conduction*, so it is the primary test for arrhythmias, which CT can't see. EEG relates to brain imaging the same way:
  - **Structural imaging** ([[computed-tomography]], [[magnetic-resonance-imaging]]) shows *what the brain looks like*: tumours, strokes, bleeding, scars, malformations.
  - **EEG** shows *what the brain is doing electrically, millisecond by millisecond*.
  - A person with epilepsy often has a completely normal MRI, and a brain lesion on MRI doesn't tell you whether it is causing seizures.
- 🤖 **Where imaging did make EEG redundant:** localizing structural lesions. Before CT (1970s), EEG slowing over one area was used to find tumours and strokes. CT/MRI replaced that, which is one reason EEG's clinical role shrank to "functional" questions.
- 🤖 **Where EEG is still the only practical tool:**
  - **Seizures and epilepsy:** diagnosing and classifying epilepsy (interictal spikes), telling seizures from mimics such as fainting or psychogenic events, and detecting **nonconvulsive seizures** in comatose ICU patients, which have no visible signs. Continuous monitoring over days is only possible with EEG.
  - **Sleep** (PSG), **depth of anaesthesia**, and **coma / post-cardiac-arrest prognosis**. Ancillary use in brain-death testing, varying by country.
  - **Epilepsy surgery** combines both: MRI finds a candidate lesion, and scalp then intracranial EEG confirm where seizures actually start → [[seizure-detection]].
- 🤖 **The functional imaging alternatives each lose something:**

  | method | measures | time resolution | spatial | practicality |
  |---|---|---|---|---|
  | EEG | neural electrical activity (cortex, synchronized) | ms | cm, smeared | cheap, portable, bedside, days-long |
  | MEG | magnetic field of the same currents | ms | better than EEG | shielded room, very expensive, still head |
  | fMRI | blood oxygenation (BOLD), an indirect, slow proxy | seconds | mm | scanner; no long or bedside recording |
  | PET / SPECT | metabolism / blood flow via radioactive tracer | minutes | mm–cm | radiation; snapshots (ictal SPECT used in epilepsy surgery) |
  | fNIRS | blood oxygenation, outer cortex only | seconds | cm | portable; slower than EEG |
  | ultrasound | anatomy (newborns, through the open fontanelle); blood-flow velocity (transcranial Doppler) | — | — | the adult skull blocks imaging; it doesn't measure neural activity |

- 🤖 **Bottom line:** EEG is redundant for *structure* and inferior in *spatial* detail. For *fast electrical events over long periods at the bedside* (seizures, sleep, coma, anaesthesia) it has no replacement. That is also exactly where its clinical value is → [[q3-typical-tasks]] *What clinical EEG is good for*.

## Comparisons

## Open threads
- Physiological origin and the spatial resolution limits of EEG: no source yet.
- Why the bands map to brain states, and *how* coarse the spatial resolution is (in cm): not yet sourced.
- EEG vs imaging (CT/MRI/fMRI/MEG/ultrasound): answered from textbook knowledge only (🤖). Source it from [[bitar2024utility]] / [[bank2022structural]] (screening, not read).
- Why only synchronized cortical pyramidal neurons are visible (deep structures, cancellation): needs a physiology source.

## Sources
- [[roy2019deep]]: pyramidal-neuron origin, temporal vs spatial resolution, spatially correlated channels (p. 2).
- [[chaddad2023electroencephalography]]: bands, the reference problem, volume conduction, the challenge list (§2.1, §3).
- [[sabio2024scoping]]: plain-language definition (intro of a device review).
- [[jiang2024large]]: EEG as data (matrix, 10-20 system).
- [[song2022eeg]]: noise and artifacts as the core difficulty.
