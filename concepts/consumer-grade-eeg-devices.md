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
- [[sabio2024scoping]]: charts 916 research studies using 5 brands. Emotiv 67.69%; 1–16 channels; BCI is the main use; validation is thin except for Emotiv (Table 3; §Research domains; §Validation).

## Variants & disagreements
- "Consumer-grade" (marketed to the public) vs "wearable/wireless research-grade" (e.g. mobile clinical systems): the boundary is fuzzy. Is ambulatory clinical EEG the same concept? → check [[niso2022wireless]].

## Open questions
- Which devices have independent validation against research-grade systems beyond Emotiv? (Muse and Mindband had none as of May 2022; §Validation)
- Ear-EEG and other new form factors: same concept or a separate one? → [[kaongoen2023future]]

## Related concepts
- [[signal-quality-and-noise]]: the main trade-off.
- [[channel-heterogeneity]]: sparse, non-standard montages.
