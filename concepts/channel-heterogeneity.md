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
- [[song2022eeg]]: the counter-example. Its spatial conv kernel spans exactly `ch` channels (§III-C), so it is tied to one montage (22, 3 or 62 channels).
- [[jiang2024large]]: designs for it. Each channel is patched separately, and learnable spatial embeddings index electrodes in the 10-20 universal set (§2.1). Without them pretraining doesn't converge and fine-tuning drops (App. L).
- [[sabio2024scoping]]: the device side. Consumer headsets have 1–16 channels at non-standard positions (e.g. Muse AF7/AF8/TP9/TP10, MindWave FP1) (Table 3).

## Variants & disagreements
- Fixed montage + spatial conv (Conformer, EEGNet) vs channel-as-token + electrode embedding (LaBraM). Other strategies (graph/topology-aware, mapping channels to a template) are not yet in the vault.

## Open questions
- Do montage-agnostic foundation models actually transfer to very sparse consumer montages (1–4 channels)? No evidence in the vault yet.
- How are electrodes outside the 10-20 set (e.g. ear-EEG) embedded? → [[kaongoen2023future]]

## Related concepts
- [[consumer-grade-eeg-devices]]: a major source of non-standard montages.
- [[self-supervised-pretraining]]: pooling datasets forces the issue.
- [[cnn-transformer-hybrid]]: where spatial mixing happens decides montage dependence.
