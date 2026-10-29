---
slug: "language-supervised-pretraining"
fields: [eeg, ml]
familiarity: new
---

# language-supervised-pretraining

## Field-neutral description
Train an encoder for one kind of data by pairing each sample with a free-text description and learning a shared embedding space where matching sample–text pairs lie close together. New categories can then be recognised by comparing a sample to the embedding of a written class description, without labelled training examples ("zero-shot").

## Synonyms by community
- **EEG:** EEG–language alignment, EEG-CLIP, EEG-language model (ELM), report-supervised pretraining
- **Neuroscience / clinical:** learning from clinical reports / free-text EEG reports
- **Signal processing:** cross-modal embedding
- **General ML:** CLIP-style contrastive language–image pretraining (Radford et al. 2021), vision-language / multimodal contrastive learning, natural-language supervision, weak supervision from captions, zero-shot classification by prompt

## Papers
- [[ndir2025eeg]] — EEG-CLIP: Deep4 CNN + ClinicalBERT aligned on TUAB recordings and their reports; frozen pathology 0.847 ≈ supervised 0.851, zero-shot pathology 0.755 (Tables 3–4).
- [[gijsen2024eeg]] — EEG-language model on TUH reports with multiple-instance alignment of EEG segments to report parts; 87.1% pathology (quoted by [[ndir2025eeg]] §4.1). Not read.
- NeuroLM (evaluated in [[kontras2026neuroatlas]]) — VQ EEG tokens aligned to text and fed to an LLM (see the target table in [[q9-pretraining-objectives-and-scale]]); a different, generative route to EEG–language coupling.

## Variants & disagreements
- **Contrastive dual encoder (CLIP)** vs **EEG tokens into an LLM (NeuroLM)**: the first gives an embedding space and zero-shot by similarity; the second gives text generation and instruction following.
- **Whole recording ↔ whole report** ([[ndir2025eeg]]) vs **segment ↔ sentence via multiple-instance learning** ([[gijsen2024eeg]]). Reports describe events at unknown times, so whole-pair matching is noisy.
- 🤖 **Is it self-supervised?** Not strictly: the text is a human annotation. It sits between supervised and self-supervised: labels are free (they already exist in clinical archives) but are written by experts reading the same EEG.

## Open questions
- 🤖 How much of "zero-shot" EEG performance is real transfer? In clinical EEG the evaluation labels (abnormal, medication) are usually extracted from the same reports used as training text ([[ndir2025eeg]] *Assessment*). A concept masked out of the training reports would be a cleaner test.
- Does report supervision beat masked-signal pretraining (LaBraM/CBraMod) under a matched frozen probe? No vault paper compares them directly.
- Does it scale with archives like HEEDB (~108k patients with reports, [[sun2025harvard]])?

## Related concepts
- [[self-supervised-pretraining]] — sibling: supervision from the signal itself rather than paired text; contrastive losses shared.
- [[evaluation-protocols]] — zero-shot / few-shot / frozen-probe protocols.
