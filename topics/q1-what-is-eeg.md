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
- Strengths: non-invasive, relatively cheap, easy to use [[sabio2024scoping]] (§Introduction); [[song2022eeg]] (§I).
- Limits: low signal-to-noise ratio and artifacts from impedance and other physiological signals [[song2022eeg]] (§I). → [[signal-quality-and-noise]]
- 🤖 Gap: the physiological origin (which neural sources produce scalp potentials) isn't covered by any vault paper yet. A review or textbook-level source is needed.

## Comparisons

## Open threads
- Physiological origin and the spatial resolution limits of EEG: no source yet.
- Standard frequency bands and what they reflect: expected in [[chaddad2023electroencephalography]] (not yet read).

## Sources
- [[sabio2024scoping]]: plain-language definition (intro of a device review).
- [[jiang2024large]]: EEG as data (matrix, 10-20 system).
- [[song2022eeg]]: noise and artifacts as the core difficulty.
