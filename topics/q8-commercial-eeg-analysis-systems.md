---
slug: q8-commercial-eeg-analysis-systems
kind: hub
status: stub
updated: 2026-10-11
---

# q8-commercial-eeg-analysis-systems

> Which automated EEG analysis systems are commercially deployed (clinical software, regulator-cleared devices, consumer products), and what do they predict? How well are those predictions validated?

*Added 2026-10-11 at the human's request. Facts live in the linked notes; this hub summarizes them.*

## Current answer
- **Automatic sleep staging ships in wearable headbands.** Dreem (5 dry electrodes) scores sleep automatically, with accuracy 0.84 and κ 0.73 against manual PSG; N1 κ is only 0.43 [[gans2024sleep]] (p. 4). Sleep Profiler under-reports N3 and over-reports N1 (p. 9). → [[sleep-staging]]
- **No agreed standard for automatic sleep scoring yet** [[gans2024sleep]] (p. 10).
- **Clinical certification (FDA/EMA) is required for clinical research use** of EEG devices [[niso2022wireless]] (§3.15). The vault doesn't yet say which *analysis software* is cleared, or for what.
- Nothing else sourced yet: the hub is a stub.

## Comparisons
| system | predicts | evidence | source |
|---|---|---|---|
| Dreem headband | sleep stages (5-class) | κ 0.73 vs PSG | [[gans2024sleep]] p. 4 |
| *(to fill)* | | | |

## Open threads
- 🤖 **Search leads (from model memory, unverified; not facts until sourced):**
  - Seizure / spike detection in clinical EEG review software (e.g. Persyst, encevis, BESA).
  - Rapid-response ICU EEG with automated seizure-burden alerts (e.g. Ceribell).
  - Automated sleep scoring for PSG (e.g. EnsoData), and the sleep headbands already in [[gans2024sleep]].
  - Other: quantitative EEG for TBI triage, depth-of-anaesthesia indices (e.g. BIS), automated normal/abnormal EEG reading.
- **Source types:** regulatory summaries (FDA 510(k) / De Novo / PMA, CE / EUDAMED) are allowed for Q8 (human, 2026-10-11; rule in CLAUDE.md Scope). Vendor white papers are still out. Keep manufacturer-reported performance separate from independent validation studies.
- Find: a 2022+ review of FDA-cleared / commercial AI EEG tools; independent validation studies of commercial seizure detectors (sensitivity, false alarms per hour) versus research models. → [[seizure-detection]]
- Link to Q6: are commercial systems validated more rigorously (multi-site, prospective) than academic models? → [[q6-reliability-of-eeg-diagnoses]]

## Sources
- [[gans2024sleep]]: validation of commercial sleep-EEG wearables against PSG.
- [[niso2022wireless]]: certification requirements for clinical use.
- [[sleep-staging]], [[seizure-detection]], [[consumer-grade-eeg-devices]].
