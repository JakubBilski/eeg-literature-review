---
slug: digital-filtering
fields: [eeg, signal-processing, ml]
familiarity: introduced     # human's level: new | introduced | understood | skip
---

# digital-filtering

## Field-neutral description
Remove or keep parts of a signal according to how fast they oscillate. A filter is a fixed operation that lets some frequency ranges through and attenuates others: slow drift, fast noise, or everything outside one range of interest.

## Synonyms by community
- **EEG:** high-pass / low-pass / band-pass / notch filter, "filtered 0.5–40 Hz", FIR/IIR filter, zero-phase filtering
- **Neuroscience / clinical:** time constant (old analogue term for high-pass), low-frequency filter (LFF) / high-frequency filter (HFF) on clinical EEG machines
- **Signal processing:** frequency response, passband / stopband / transition band, cutoff (−3 dB / −6 dB), filter order, FIR vs IIR, filtfilt
- **General ML:** a fixed 1-D convolution kernel (FIR filter); a learned temporal conv layer is a learned filter bank

## The filter types (🤖 textbook material, ML-oriented)
| type | keeps | typical EEG use |
|---|---|---|
| **high-pass** | everything above a cutoff | remove slow drift from sweat, electrode movement and breathing; cutoff 0.1–1 Hz |
| **low-pass** | everything below a cutoff | remove muscle noise and high-frequency junk; also needed before downsampling (anti-aliasing) |
| **band-pass** | one range | isolate a band, e.g. 8–12 Hz mu, or the whole "useful" range 1–40 Hz |
| **notch / band-stop** | everything except a narrow band | remove mains (line) noise at 50 Hz (Europe) or 60 Hz (US) and its harmonics |

- **What a filter is, mechanically:** an FIR filter *is* a 1-D convolution with a fixed kernel. The kernel's Fourier transform is the frequency response, i.e. which frequencies it passes. Designing a filter = choosing a kernel whose spectrum is ~1 in the passband and ~0 in the stopband.
- **FIR vs IIR:**
  - **FIR** (finite impulse response): a plain convolution. Always stable, can have linear phase. Needs long kernels for sharp or low cutoffs. MNE's default.
  - **IIR** (e.g. Butterworth): recursive, so each output depends on previous outputs. Gives sharp cutoffs with few coefficients, but distorts phase and can be unstable at high order.
- **Phase / zero-phase:** a causal filter delays the signal, and the delay may differ by frequency. Offline, EEG is usually filtered forwards and then backwards (`filtfilt`, or MNE's zero-phase FIR), which cancels the delay so peaks stay where they were. Online BCIs can't look ahead, so they must accept the delay.
- **Transition band and order:** real filters don't cut sharply. Between pass and stop there is a transition band. Narrower transitions need longer kernels, which smear events in time (more "ringing"). This is the same time–frequency trade-off as in [[time-frequency-analysis]].
- **Edge effects:** convolution needs data on both sides, so the first and last ~kernel-length samples of a segment are distorted. Hence the advice to filter the continuous recording first and cut epochs afterwards.
- **Pitfalls:**
  - an aggressive high-pass (> ~0.5 Hz) distorts slow ERPs such as the P300 or readiness potential;
  - filtering can't remove noise that sits *inside* the band you keep (e.g. muscle activity overlapping beta);
  - filter ringing around sharp artifacts can look like oscillations.

## Papers
- [[niso2022wireless]]: dry electrodes drift below 2 Hz with sweat, which "forces higher high-pass cut-offs" (p. 6). Activity of interest is mostly ≤50 Hz, so 250–500 Hz sampling is common (§3.8).
- [[song2022eeg]]: band-pass 4–40 Hz (motor imagery) and 4–47 Hz (SEED) before the model (§IV-A).
- [[lawhern2018eegnet]]: band-pass depends on the paradigm: 1–40 Hz for P300/ERN, 0.1–40 Hz for MRCP (to keep slow potentials), 4–40 Hz for SMR (Table 1). EEGNet's first layer is a learned temporal filter bank, conceptually like FBCSP's band-pass bank (§1).
- [[varbu2022past]]: dry headsets are reportedly more robust to line noise (Soufineyestani, p. 15).

## Variants & disagreements
- How much to filter before deep learning: many DL pipelines still band-pass (Conformer 4–40 Hz), while others feed minimally filtered data and let the first conv layer learn the filters. 🤖 There's no vault evidence on which is better.

## Open questions
- Standard filter settings in foundation-model preprocessing (LaBraM, CBraMod): check their appendices.

## Related concepts
- [[eeg-preprocessing-pipeline]]: filtering is usually the first step.
- [[time-frequency-analysis]]: band-pass + Hilbert gives band power over time; the DWT is a filter cascade.
- [[frequency-bands]]: the ranges people band-pass to.
- [[signal-quality-and-noise]]: filtering removes noise *outside* the band of interest only.
- [[common-spatial-patterns]]: spatial filtering (across channels) vs temporal filtering (across time).
