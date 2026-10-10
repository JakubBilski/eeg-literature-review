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
- In research use (2010–2022), Emotiv dominates at 67.69% of 916 studies [[sabio2024scoping]] (§Consumer-grade EEG devices).
- Validation: Emotiv records ERPs comparable to research systems but is noisier. Muse and Mindband had no validation studies by May 2022 [[sabio2024scoping]] (§Validation).
- **Montages:** the 10-20 system is the standard placement [[jiang2024large]] (§1). Channel names encode position relative to the midline and front–back [[chaddad2023electroencephalography]] (§2.1). 🤖 (standard convention, to confirm in [[niso2022wireless]]): letters Fp/F/C/T/P/O = frontopolar, frontal, central, temporal, parietal, occipital; odd numbers left, even right, z midline; "10-20" = electrodes spaced at 10% or 20% of skull distances.
  - In practice: half of the public scalp seizure datasets follow 10-20 [[wong2023eeg]] (§5.1). CBraMod pretrains on 19 common 10-20 channels (Fp1 … O2) [[wang2024cbramod]] (§3, p. 6). TUAB/TUEV benchmarks use 16 *bipolar* channels (differences between neighbouring electrodes) (App. E).
  - The reference electrode is subtracted from all others, and devices place it differently (earlobe, mastoid, or flexible) [[niso2022wireless]] (p. 4–5). *(not yet read in full)*
  - Datasets range from 3 bipolar channels (BCI IV-2b) to 62 (SEED) [[song2022eeg]] (§IV-A). → [[channel-heterogeneity]]

## Comparisons
| class | channels | conductive medium | typical use | source |
|---|---|---|---|---|
| research/clinical cap | dozens (19–64+) | gel / saline | lab, clinic | [[sabio2024scoping]], [[jiang2024large]] |
| consumer headset | 1–16 | minimal / none | BCI, field studies | [[sabio2024scoping]] (Table 3) |

## Open threads
- Wireless/mobile research-grade systems, dry vs wet electrodes, ear-EEG: [[niso2022wireless]], [[kaongoen2023future]] (full text ready, not yet read).
- Clinical montage standards beyond 10-20 (e.g. 10-10, bipolar clinical montages).

## Sources
- [[chaddad2023electroencephalography]]: lab vs portable acquisition; Emotiv and Muse examples (§2.1).
- [[sabio2024scoping]]: consumer-grade devices: specs, use, validation.
- [[jiang2024large]]: amplifiers and caps behind common public datasets (App. D).
- [[song2022eeg]]: montages of benchmark datasets.
