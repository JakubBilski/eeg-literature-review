---
slug: self-supervised-pretraining
fields: [eeg, ml]
familiarity: new     # human's level: new | introduced | understood | skip
---

# self-supervised-pretraining

## Field-neutral description
Training a model on large amounts of unlabeled data with a task made from the data itself (e.g. hide part of the input and predict it), so that it can later be adapted to specific labeled tasks with little labeled data.

## Synonyms by community
- **EEG:** large EEG model (LEM), EEG/brain foundation model, masked EEG modeling, pretrain–fine-tune
- **Neuroscience / clinical:** —
- **Signal processing:** —
- **General ML:** SSL, masked modeling (BERT/BEiT/MAE), contrastive learning, foundation model

## Papers
- [[jiang2024large]]: masked prediction of discrete spectral tokens over 2,535 h from ~20 datasets. Scaling helps the largest model, but weak linear probing means fine-tuning is required (§3.6, App. K).
- [[song2022eeg]]: explicitly *does not* pretrain because of "limited data for calibration" (§IV-E). This is the small-data, per-subject paradigm that foundation models argue against.

## Variants & disagreements
- Objective: predict raw signal, spectrum, or discrete codes. LaBraM found raw reconstruction better on TUAB but discrete codes better on TUEV (App. G, Table 7). The best target may depend on the task.
- Contrastive (BENDR, BIOT) vs masked (LaBraM, CBraMod): not yet compared in the vault.

## Open questions
- How much pretraining data is enough? LaBraM extrapolates to ≥10k h (§3.6), but Base peaks at 500 h on TUAB.
- Does pretraining help cross-subject BCI tasks (motor imagery, emotion), or mostly clinical TUH-like tasks? (the 🤖 point in [[jiang2024large]])
- Fine-tuning vs linear probing: which should count as evidence of "generic" representations? → [[evaluation-protocols]]

## Related concepts
- [[channel-heterogeneity]]: pooling many datasets requires handling different montages.
- [[evaluation-protocols]]: how pretrained models are evaluated (probe vs fine-tune, data overlap).
- [[cnn-transformer-hybrid]]: the common backbone shape.
