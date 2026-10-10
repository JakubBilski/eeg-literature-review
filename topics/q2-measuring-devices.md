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
- In research use (2010–2022), Emotiv dominates at 67.69% of 916 studies [[sabio2024scoping]] (§Consumer-grade EEG devices).
- Validation: Emotiv records ERPs comparable to research systems but is noisier. Muse and Mindband had no validation studies by May 2022 [[sabio2024scoping]] (§Validation).
- **Montages:** the 10-20 system is the standard placement [[jiang2024large]] (§1). Datasets range from 3 bipolar channels (BCI IV-2b) to 62 (SEED) [[song2022eeg]] (§IV-A). → [[channel-heterogeneity]]

## Comparisons
| class | channels | conductive medium | typical use | source |
|---|---|---|---|---|
| research/clinical cap | dozens (19–64+) | gel / saline | lab, clinic | [[sabio2024scoping]], [[jiang2024large]] |
| consumer headset | 1–16 | minimal / none | BCI, field studies | [[sabio2024scoping]] (Table 3) |

## Open threads
- Wireless/mobile research-grade systems, dry vs wet electrodes, ear-EEG: [[niso2022wireless]], [[kaongoen2023future]] (seeds, PDFs need manual download).
- Clinical montage standards beyond 10-20 (e.g. 10-10, bipolar clinical montages).

## Sources
- [[sabio2024scoping]]: consumer-grade devices: specs, use, validation.
- [[jiang2024large]]: amplifiers and caps behind common public datasets (App. D).
- [[song2022eeg]]: montages of benchmark datasets.
