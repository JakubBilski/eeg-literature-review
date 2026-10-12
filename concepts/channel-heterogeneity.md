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
- [[lawhern2018eegnet]]: same constraint as Conformer. The depthwise conv has a (C, 1) kernel over all channels (Table 2), so each model is trained per montage (64, 56, 64 or 22 channels; §2.1). MRCP data were reduced from 256 to the standard 64-channel BioSemi montage (§2.1.3).
- [[jiang2024large]]: designs for it. Each channel is patched separately, and learnable spatial embeddings index electrodes in the 10-20 universal set (§2.1). Without them pretraining doesn't converge and fine-tuning drops (App. L).
- [[niso2022wireless]]: device channel counts range from 4 to 128. Across 110 wireless studies the median is 14 channels, 37 studies used <8 and 11 used a single channel (Table 1; Fig. 5c). Electrode placement is either fixed by the headset or flexible via caps; headbands cannot reach the top of the head (§3.2).
- [[sabio2024scoping]]: the device side. Consumer headsets have 1–16 channels at non-standard positions (e.g. Muse AF7/AF8/TP9/TP10, MindWave FP1) (Table 3).
- [[wong2023eeg]]: public seizure datasets range from 1 to 76 channels. They mix 10-20 with extended 10-10 ("Nomenclature") placements and name channels inconsistently. Sampling rates run 173.86–5000 Hz and vary even within one dataset. So a model "cannot truly" be tested on another dataset without re-tuning (§5.1, §6.3, §7, Tables 2, 8).
- [[roy2019deep]]: the position of the reference channels matters, "making it difficult to compare across datasets coming from different neurologists and recording sites" (ref [153], p. 13). Channel counts range from 1 to 256 (p. 13).
- [[weng2025self]]: lists "SSL for heterogeneous EEG" (different channels, devices, sampling rates, tasks, subjects) as an open future direction as of early 2024 (§8, p. 29). Spatial pretext tasks (channel jigsaw, region shuffling, graph views) assume a fixed montage (§3.1, §5.3).
- [[kuruppu2026eeg]]: three strategies across 10 FMs: map every dataset to a fixed channel set (LaBraM, Neuro-GPT, Mentality), positional encodings for variable channel counts (Brant, NeuroLM, FoME), per-channel tokens with channel embeddings (BIOT) (§4.1–4.2, pp. 10–12). It counts only BIOT as truly multi-montage (🤖 debatable for LaBraM). Cross-site variability sources listed: hardware presets, protocol, montage, reference, anatomy (§2.1, p. 4).
- [[coppola2024hubert]] (ECG contrast case): the 12 leads are fixed, so they are concatenated end to end into one 1D sequence with positional encodings (pp. 12–13). Models pretrained on 12 leads still transfer to single-lead ECG (macro AUROC 0.878–0.917, p. 7). 🤖 The trick depends on a fixed lead set and does not carry over to variable EEG montages → [[hubert-style-pseudo-labels]].
- [[liu2026eeg]]: six channel-unification strategies across 55 FMs (pp. 8–9): (1) fixed montage (CBraMod, BENDR); (2) template or region remap (CSBrain, Uni-NTFM); (3) channel-wise or single-channel (BIOT, SingLEM); (4) learnable channel embeddings (LaBraM, EEGPT); (5) coordinate-aware encodings (REVE, LUNA, HEAR); (6) projection to a fixed latent space (LUNA, BrainOmni). In practice BrainOmni can't take bipolar montages (p. 16), and the topology-agnostic LUNA collapses outside clinical data (p. 17).

- [[chen2026benchmarking]]: compares channel-constrained FMs (CBraMod, CodeBrain, CSBrain, EEGPT, NeuroRVQ, ST-EEGFormer) with channel-flexible ones (REVE, HEAR, LEAD) on task-informed channel subsets. Flexible models score higher at most retained-channel ratios (Fig. 7, p. 14). Arbitrary dropout, re-referencing and device changes are untested (p. 17).

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
