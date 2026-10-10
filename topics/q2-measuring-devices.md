---
slug: q2-measuring-devices
kind: hub
status: stub
updated: 2026-10-10
---

# q2-measuring-devices

> What are the standard EEG measuring devices: clinical/research systems, wearables, electrode types, montages?

## Current answer
- **Research/clinical grade:** dozens of electrodes fitted with saline or gel [[sabio2024scoping]] (§Consumer-grade EEG devices). Examples in vault datasets: BrainAmp, BioSemi ActiveTwo, ESI NeuroScan, g.USBamp, Natus/EB Neuro clinical amplifiers [[jiang2024large]] (App. D).
- **Consumer grade:** few electrodes, minimal or no conductive medium, wireless, cheap. 1–16 channels: Emotiv EPOC (14), Insight (5), OpenBCI (4/8/16), Muse (4), NeuroSky / MyndPlay (1) [[sabio2024scoping]] (Table 3). → [[consumer-grade-eeg-devices]]
- Lab systems are wired, PC-attached and externally powered: reliable but heavy and power-hungry, which drives the move to portable devices [[chaddad2023electroencephalography]] (§2.1).
- **Wireless EEG landscape:** 48 devices from 18 companies, 4–128 channels, 128–2048 Hz, 12–24 bit, <0.5 to 45–60 k€; 11 are medically certified [[niso2022wireless]] (Table 1; transcription in the full text). Price roughly tracks channel count (§3.16).
  - ≥32 channels is the usual minimum for broad lab coverage; high-density goes to 256. Fewer channels suffice when the relevant region is known (§3.2).
  - Typical sampling rate is 250–500 Hz, because activity of interest is mostly ≤50 Hz (§3.8).
  - Practical specs that matter: impedance monitoring (§3.6), on-board storage as a fallback when the wireless link drops (§3.12), and LSL support for real-time streaming (§3.13).
- **Electrodes:** gel (best signal, slow setup, dries out), wet/saline (intermediate), dry (fast setup, but noisier, uncomfortable after ~15 min, needs a higher high-pass cut-off); active electrodes pre-amplify at the scalp [[niso2022wireless]] (§3.4–3.5). → [[electrode-types]]
- **Mobility vocabulary:** mobile / portable / wearable / transparent EEG [[niso2022wireless]] (p. 2). In practice, 61% of 110 high-impact wireless studies had participants who barely moved (Fig. 7d).
- In research use (2010–2022), Emotiv dominates at 67.69% of 916 studies [[sabio2024scoping]] (§Consumer-grade EEG devices). In BCI application papers (2009–2019) it is also first: 40% of 77 that named a device, vs 9% for Compumedics Quik-Cap and 8% for NeuroSky MindWave [[varbu2022past]] (Fig. 9). In those papers, 64% of 163 used ≤20 channels (Fig. 10).
- Validation: Emotiv records ERPs comparable to research systems but is noisier. Muse and Mindband had no validation studies by May 2022 [[sabio2024scoping]] (§Validation).
- **Why there's no cross-device signal-quality benchmark** (asked 2026-10-10):
  - **Pairwise validations exist.** In [[sabio2024scoping]] (§Validation), 6.18% of 916 consumer-device studies are validations: Emotiv vs Neuroscan / BioSemi / g.HIamp, NeuroSky vs Neuroscan, OpenBCI vs g.USBamp, and none for Muse or Mindband. [[niso2022wireless]] (pp. 6, 13) cites more (dry vs gel, active vs passive) and says a standardized, many-device protocol is what's missing. [[varbu2022past]] (§5.5, p. 15) cites the closest thing to a multi-device study: Zerafa 2018 compared "a broad range" of devices on SSVEP and found low-end research systems as good as high-end ones, while low-cost headsets were worse. It also cites Ratti 2017 (medical vs consumer) and Hinrichs 2020 (dry wireless vs wet wired, comparable). All three are pre-2022 and single-task.
  - **Quality depends on the task.** A frequency-based analysis "may not pose the same requirements" as early evoked potentials [[niso2022wireless]] (p. 13). For example, dry electrodes are contaminated below 2 Hz (p. 6), and Emotiv's high noise floor led Grummett to caution against it for low-frequency work, while it handled alpha and SSVEP fine [[sabio2024scoping]] (§Validation). So no single number works; you need a battery of tasks.
  - **Fit and setup matter as much as the device.** Emotiv results are sensitive to fit [[sabio2024scoping]] (§Validation). Whether active or passive electrodes win depends on impedance [[niso2022wireless]] (§3.5).
  - **More data doesn't fix it.** 🤖 Large N averages out random differences, not systematic ones. Who gets recorded on which device is systematic: TUH holds clinical patients from one hospital and makes up ≈68% of LaBraM's pretraining hours [[jiang2024large]] (App. D); the largest wireless study used a Muse on 6029 people (Hashemi 2016) [[niso2022wireless]] (§4.1); lab datasets mostly record volunteers doing set tasks. Device, population, task and lab move together at any N. The fix is in the design: the same people on several devices (within-subject), i.e. the small validation studies above.
  - **Public data can't answer it.** Datasets differ in subjects, task, lab and montage at the same time, so the device is confounded with everything else. Methods reporting is also too inconsistent for meta-analysis [[niso2022wireless]] (p. 14).
  - 🤖 **There's no ground truth.** The true brain signal is never observed, so quality is measured indirectly: recovering known effects (alpha rising with eyes closed, P300), noise floor, rejected trials, test-retest reliability. Two electrodes can't sit on the same spot either, so comparisons record at neighbouring sites at the same time, or one after another (brain state then differs).
  - 🤖 **Coverage confounds quality.** Muse has only AF7/AF8/TP9/TP10 (Table 3 in [[sabio2024scoping]]), so it can't see the motor cortex. It would fail a motor imagery test because of where its electrodes are, not because of noise.
  - 🤖 **Cost and churn.** Each comparison needs participants × devices in a lab, devices cost up to tens of k€ (Table 1 in [[niso2022wireless]]), models get discontinued (p. 11), and vendor specs are opaque (p. 13).
  - **Proposed recipe:** ERP CORE paradigms run while sitting, standing and walking, scored with the standardized measurement error (Luck 2021) [[niso2022wireless]] (p. 13); "well-powered within-subjects studies that compare signal-noise indices for each device" [[sabio2024scoping]] (§Discussion).
- **Montages:** the 10-20 system is the standard placement [[jiang2024large]] (§1). Channel names encode position relative to the midline and front–back [[chaddad2023electroencephalography]] (§2.1). 🤖 (standard convention; [[niso2022wireless]] uses 10-20 names but does not explain them, so this still needs a source): letters Fp/F/C/T/P/O = frontopolar, frontal, central, temporal, parietal, occipital; odd numbers left, even right, z midline; "10-20" = electrodes spaced at 10% or 20% of skull distances.
  - In practice: half of the public scalp seizure datasets follow 10-20 [[wong2023eeg]] (§5.1). CBraMod pretrains on 19 common 10-20 channels (Fp1 … O2) [[wang2024cbramod]] (§3, p. 6). TUAB/TUEV benchmarks use 16 *bipolar* channels (differences between neighbouring electrodes) (App. E).
  - The reference electrode is subtracted from all others. Devices place it differently (earlobe, mastoid, a 10-20 site, or flexible), and its contact is critical, so it sometimes gets gel when the other electrodes don't [[niso2022wireless]] (§3.2, Table 1).
  - Datasets range from 3 bipolar channels (BCI IV-2b) to 62 (SEED) [[song2022eeg]] (§IV-A). → [[channel-heterogeneity]]

## Comparisons
| class | channels | conductive medium | typical use | source |
|---|---|---|---|---|
| research/clinical cap | dozens (19–64+) | gel / saline | lab, clinic | [[sabio2024scoping]], [[jiang2024large]] |
| consumer headset | 1–16 | minimal / none | BCI, field studies | [[sabio2024scoping]] (Table 3) |
| wireless research / medical system | 8–128 | gel, saline or dry; often active | mobile studies, home sleep/seizure monitoring | [[niso2022wireless]] (Table 1) |

## Open threads
- Ear-EEG: [[kaongoen2023future]] (full text ready, not yet read).
- Has anyone run a standardized multi-device quality benchmark since 2022 (e.g. on ERP CORE)? Not searched yet.
- Clinical montage standards beyond 10-20 (e.g. 10-10, bipolar clinical montages).

## Sources
- [[chaddad2023electroencephalography]]: lab vs portable acquisition; Emotiv and Muse examples (§2.1).
- [[sabio2024scoping]]: consumer-grade devices: specs, use, validation.
- [[jiang2024large]]: amplifiers and caps behind common public datasets (App. D).
- [[song2022eeg]]: montages of benchmark datasets.
- [[varbu2022past]]: devices and channel counts in BCI papers; cited device comparisons (§5.5).
- [[niso2022wireless]]: spec glossary and a 48-device comparison table; electrode types; how wireless EEG is used.
