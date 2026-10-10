---
slug: consumer-grade-eeg-devices
fields: [eeg, neuro-clinical]
familiarity: new     # human's level: new | introduced | understood | skip
---

# consumer-grade-eeg-devices

## Field-neutral description
Low-cost, wireless sensor headsets sold to non-specialists. They have few sensors and quick setup, trading signal quality and coverage for affordability and use outside the lab.

## Synonyms by community
- **EEG:** consumer / commercial / low-cost / wearable EEG, dry-electrode headsets (e.g. Emotiv, Muse, NeuroSky, OpenBCI)
- **Neuroscience / clinical:** mobile EEG, ambulatory EEG (overlapping, not identical?)
- **Signal processing:** —
- **General ML:** wearable sensors, edge devices

## Papers
- [[chaddad2023electroencephalography]]: Emotiv EPOC (14 ch + 2 reference) records real EEG but performs worse than larger devices. Muse has 4 electrodes (AF7, AF8, TP9, TP10) and an Fpz reference (§2.1).
- [[niso2022wireless]]: 48 wireless devices on one spec table, from <0.5 k€ 4-channel dry headsets (Muse, Emotiv INSIGHT) to 128-channel research systems at 45–60 k€ (Table 1). In 69 high-impact studies, Emotiv was used in 25% and home-made devices in 19% (Fig. 6a).
- [[varbu2022past]]: among 77 BCI papers (2009–2019) that named a device: Emotiv EPOC 40%, NeuroSky MindWave 8% vs research Quik-Cap 9% (Fig. 9). Cites comparisons: consumer devices are as good as research ones for emotion recognition (Dadebayev 2021); low-cost headsets have poorer SSVEP signal than research systems (Zerafa 2018); medical systems are better but slower to set up (Ratti 2017) (§5.5, p. 15).
- [[sabio2024scoping]]: charts 916 research studies using 5 brands. Emotiv 67.69%; 1–16 channels; BCI is the main use; validation is thin except for Emotiv (Table 3; §Research domains; §Validation).

## Variants & disagreements
- "Consumer-grade" (marketed to the public) vs "wearable/wireless research-grade" (e.g. mobile clinical systems): the boundary is fuzzy. [[niso2022wireless]] avoids it by defining "wireless EEG" as any device with a wireless protocol, a category spanning consumer headsets, research systems and 11 medically certified devices (Table 1). Ambulatory clinical EEG belongs in that wider category, not in this note.
  - Its mobility vocabulary (Bleichner & Debener 2017, p. 2): **mobile** = tolerates movement; **portable** = can be carried; **wearable** = portable and self-applied; **transparent** = all of these plus near-invisible.
  - Consumer devices differ from research ones mainly in price and software openness, not in being wireless. Several sell proprietary "engagement/stress" metrics that the vendors don't validate [[niso2022wireless]] (p. 12–13).

## Open questions
- Which devices have independent validation against research-grade systems beyond Emotiv? (Muse and Mindband had none as of May 2022; §Validation). Pre-2022 multi-device comparisons cited by [[varbu2022past]] (§5.5): Zerafa 2018 (many devices, SSVEP), Ratti 2017 (medical vs consumer), Hinrichs 2020 (dry vs wet). Not yet in screening.
- Ear-EEG and other new form factors: same concept or a separate one? → [[kaongoen2023future]]

## Related concepts
- [[signal-quality-and-noise]]: the main trade-off.
- [[channel-heterogeneity]]: sparse, non-standard montages.
- [[electrode-types]]: mostly dry or saline electrodes.
