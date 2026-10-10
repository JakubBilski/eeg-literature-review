---
slug: frequency-bands
fields: [eeg, neuro-clinical, signal-processing]
familiarity: introduced     # human's level: new | introduced | understood | skip
---

# frequency-bands

## Field-neutral description
A recorded oscillating signal is split into a handful of conventional frequency ranges, and the strength of each range is used as a compact summary of the system's state. The ranges are conventions that grew out of observation, not physical constants.

## Synonyms by community
- **EEG:** delta / theta / alpha / beta / gamma bands, brain rhythms, band power, power spectral density (PSD), differential entropy (DE) features
- **Neuroscience / clinical:** neural oscillations, rhythms (e.g. "alpha rhythm", "sleep spindles"), slowing
- **Signal processing:** sub-band decomposition, filter bank, spectral power, band-pass filtering
- **General ML:** spectral features, frequency-domain tokens

## Definitions (as given by [[chaddad2023electroencephalography]], §2.1)
| band | range | typical association |
|---|---|---|
| delta | 0.5–4 Hz | slow-wave activity, deep sleep |
| theta | 4–8 Hz | relaxation, meditation |
| alpha | 8–13 Hz | most visible with eyes closed |
| beta | 13–30 Hz | active, attentive cognition |
| gamma | >30 Hz | higher cognitive processing, sensory integration |

## Papers
- [[chaddad2023electroencephalography]]: canonical definitions and associations (§2.1). Bands are the basis of time–frequency features (§2.4.1).
- [[song2022eeg]]: band-passes the input to 4–40 Hz (motor imagery) and 4–47 Hz (SEED) (§IV-A). Its topographies show changes in band power over motor cortex during imagined movement (ERD/ERS) (§IV-H).
- [[varbu2022past]]: in 2009–2019 BCI papers, band-type features dominate: PSD in 23/126 and Fourier in 20/126 papers (Fig. 12). Passive BCIs (drowsiness, attention, emotion) work by "analysis of the changes in the EEG spectrum" (§5.7). → [[bci-paradigms]]
- [[jiang2024large]]: instead of fixed bands, the tokenizer predicts the full Fourier amplitude and phase of each 1 s patch (§2.2), i.e. a learned and finer-grained version of band features.

## Variants & disagreements
- Boundaries differ between papers (e.g. alpha 8–12 vs 8–13 Hz; the gamma upper limit is often left open). Check each paper's definition before comparing.

## Open questions
- Why do these ranges correspond to distinct brain states (the physiological mechanism)? No vault source yet. See [[q1-what-is-eeg]].

## Related concepts
- [[signal-quality-and-noise]]: 🤖 (general knowledge, no vault source yet) muscle artifacts mostly contaminate high frequencies (beta/gamma), and eye artifacts the low ones (delta).
