---
slug: cnn-transformer-hybrid
fields: [eeg, ml]
familiarity: new     # human's level: new | introduced | understood | skip
---

# cnn-transformer-hybrid

## Field-neutral description
A model that first applies small local filters (convolutions) to compress the raw signal into a shorter sequence of feature vectors ("tokens"), then lets every token attend to every other token to capture long-range structure.

## Synonyms by community
- **EEG:** convolutional transformer, "Conformer", conv tokenizer / temporal encoder + Transformer
- **Neuroscience / clinical:** —
- **Signal processing:** filter bank followed by global (attention-based) aggregation
- **General ML:** hybrid CNN-Transformer, convolutional stem / patch embedding (as in ViT), Conformer (speech)

## Papers
- [[song2022eeg]]: the defining EEG example. Temporal conv → spatial conv → pooling → 6-layer self-attention, trained from scratch per subject. Removing attention costs −6.02 pts on BCI IV-2a (§IV-F).
- [[wang2024cbramod]]: per-patch 3-layer 1D conv (time branch) + FFT-magnitude linear layer (frequency branch), summed, then a 12-layer criss-cross transformer (§2; Table 5). Time-only > frequency-only, both together best (Table 17).
- [[jiang2024large]]: a temporal conv encoder applied *per single-channel 1 s patch* before a large pretrained Transformer (§2.1). The conv step is per patch, not across channels.

## Variants & disagreements
- Where spatial mixing happens: in the conv (Conformer: spatial conv over all channels, which fixes the montage) or in attention (LaBraM: channel-wise tokens + electrode embeddings, montage-agnostic). See [[channel-heterogeneity]].
- Token size: Conformer found pooling length the most sensitive hyper-parameter (+13 pts from 15→45 samples; §IV-G). LaBraM fixes 1 s patches.

## Open questions
- Is the conv front end still needed at foundation-model scale, or does it mainly help with small data? *Partial (2026-10-25):* CBraMod (4M) keeps a conv stem; dropping its FFT branch costs ~1 point, dropping the conv branch ~3 (Table 17). No stem-free variant is tested, and SpecBraM uses a linear patch embedding with the same backbone, so a conv stem is not required.

## Related concepts
- [[channel-heterogeneity]]: the design of the conv front end decides whether the model is tied to one montage.
- [[signal-quality-and-noise]]: conv pooling as denoising before attention.
- [[self-supervised-pretraining]]: hybrids appear both with and without pretraining.
