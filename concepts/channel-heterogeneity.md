---
slug: channel-heterogeneity
fields: [eeg, ml]
familiarity: new     # human's level: new | introduced | understood | skip
---

# channel-heterogeneity

## Field-neutral description
Recordings come from sensor setups that differ in the number and placement of sensors, so the same model input "slot" can mean different things across datasets or devices. Models must either fix one setup or be designed to accept arbitrary sensor sets.

## Synonyms by community
- **EEG:** montage differences, electrode configuration mismatch, topology-agnostic / channel-agnostic modeling, 10-20 system coverage
- **Neuroscience / clinical:** montage, electrode layout
- **Signal processing:** variable sensor arrays
- **General ML:** variable-length / set-structured inputs, missing modalities, positional encoding of sensors

## Papers
- [[chaddad2023electroencephalography]]: names device differences across datasets as a key challenge and proposes domain adaptation (§3). No montage-agnostic architecture is discussed.
- [[song2022eeg]]: the counter-example. Its spatial conv kernel spans exactly `ch` channels (§III-C), so it is tied to one montage (22, 3 or 62 channels).
- [[jiang2024large]]: designs for it. Each channel is patched separately, and learnable spatial embeddings index electrodes in the 10-20 universal set (§2.1). Without them pretraining doesn't converge and fine-tuning drops (App. L).
- [[niso2022wireless]]: device channel counts range from 4 to 128. Across 110 wireless studies the median is 14 channels, 37 studies used <8 and 11 used a single channel (Table 1; Fig. 5c). Electrode placement is either fixed by the headset or flexible via caps; headbands cannot reach the top of the head (§3.2).
- [[sabio2024scoping]]: the device side. Consumer headsets have 1–16 channels at non-standard positions (e.g. Muse AF7/AF8/TP9/TP10, MindWave FP1) (Table 3).
- [[wong2023eeg]]: public seizure datasets range from 1 to 76 channels. They mix 10-20 with extended 10-10 ("Nomenclature") placements and name channels inconsistently. Sampling rates run 173.86–5000 Hz and vary even within one dataset. So a model "cannot truly" be tested on another dataset without re-tuning (§5.1, §6.3, §7, Tables 2, 8).

## Variants & disagreements
- Fixed montage + spatial conv (Conformer, EEGNet) vs channel-as-token + electrode embedding (LaBraM). Other strategies (graph/topology-aware, mapping channels to a template) are not yet in the vault.

- **Device shift vs montage shift** (discussed 2026-10-10). 🤖 Beyond *where* the electrodes are, devices differ in filtering, gain, noise and contact. Much of that shift is roughly linear (spatial mixing + filtering + additive noise), which alignment methods handle; Riemannian re-centering is the classical version ([[riemannian-methods]]). Two limits:
  - Information a device never recorded (e.g. no electrode over motor cortex on Muse; [[sabio2024scoping]] Table 3) can only be filled in from a learned prior, not measured.
  - When device correlates with label (patients on clinical amplifiers, controls on research ones), a model can learn the device "fingerprint" as a shortcut.
  - Pretraining data is mostly clinical gel recordings (≈68% TUH in LaBraM; [[jiang2024large]] App. D), so dry, low-channel consumer data is barely represented.

## Open questions
- Can foundation models map between devices (e.g. predict 19-channel gel EEG from a 4-channel dry headset)? Testing it requires paired recordings of the same person on two devices, which are scarce. No vault evidence yet.
- Do montage-agnostic foundation models actually transfer to very sparse consumer montages (1–4 channels)? No evidence in the vault yet.
- How are electrodes outside the 10-20 set (e.g. ear-EEG) embedded? → [[kaongoen2023future]]

## Related concepts
- [[domain-adaptation]]: the general family of fixes for subject, session, device and dataset shift.
- [[consumer-grade-eeg-devices]]: a major source of non-standard montages.
- [[self-supervised-pretraining]]: pooling datasets forces the issue.
- [[cnn-transformer-hybrid]]: where spatial mixing happens decides montage dependence.
