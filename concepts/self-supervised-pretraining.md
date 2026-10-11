---
slug: self-supervised-pretraining
fields: [eeg, ml]
familiarity: understood     # human's level: new | introduced | understood | skip
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
- [[roy2019deep]]: an early precursor. In 2010–2018, 25% of 156 DL-EEG papers used multi-step training: unsupervised feature learning with RBMs, DBNs or autoencoders, then a classifier (§3.5.2, pp. 18–19). This faded once end-to-end CNNs took over from 2015 (p. 17). The review expected large corpora like TUH to make deeper models usable (p. 27).
- [[weng2025self]]: survey of ~70 EEG SSL methods (≈2019–2023), grouped as predictive (relative positioning, temporal shuffling, band-stop prediction), generative (autoencoders, masked reconstruction, BENDR), contrastive (CPC, SimCLR-style augmentations, channel/graph views, EEG–image/speech alignment) and hybrid (Fig. 3, Tables 1–4). Sleep staging is the most common target (Table 3). It reports no performance numbers and predates LaBraM/CBraMod.

## Variants & disagreements
- Objective: predict raw signal, spectrum, or discrete codes. LaBraM found raw reconstruction better on TUAB but discrete codes better on TUEV (App. G, Table 7). The best target may depend on the task.
- Contrastive (BENDR, BIOT) vs masked (LaBraM, CBraMod): not yet compared in the vault. [[weng2025self]] calls contrastive "the most widely used" and "the most effective" (§5, §5.6) but gives no numbers. 🤖 Note that BENDR is itself a hybrid: masked embeddings with a contrastive loss (§4.1).
- **Taxonomy (pre-foundation-model, ≈2019–2023):** predictive (classify a pseudo-label: time distance, shuffled order, removed band, applied augmentation), generative (reconstruct masked signal, spectrum or embeddings; GANs), contrastive (pull augmented views together; CPC), hybrid [[weng2025self]] (Fig. 3). 🤖 Foundation models mostly use the generative / masked branch at scale.

## Contrastive learning, explained (asked 2026-10-11)
- **Idea:** train an encoder so that two "views" of the same thing get nearby embeddings and views of different things get distant ones. No labels are needed. The supervision is *which pairs belong together*, and the designer decides that.
- **Loss (InfoNCE):** for each anchor, a softmax over its similarity to 1 positive and N negatives (usually the rest of the batch), with a temperature τ. In effect it is an (N+1)-way classification: "which candidate is my partner?" [[weng2025self]] (Eq. 17, p. 20). 🤖 NLP analogues: word2vec negative sampling, SimCSE (dropout as the augmentation), CLIP (image–caption pairs).
- **Choosing the positives fixes what the model learns to ignore.** EEG versions:
  - two augmentations of the same window (noise, amplitude ×0.5–2, time shift, crop, DC shift) (§5.2, p. 20);
  - CPC: a context summary must pick out the true *future* window from other windows (§5.1);
  - channel views: region-shuffled or node-dropped electrode graphs (§5.3);
  - cross-modal: the EEG and the image or speech that evoked it (§5.5).
- **Negative-free variants** (BYOL, Barlow Twins, ContraWR) keep only positives and prevent the collapse to a constant embedding by other means (§5.2).
- **Versus masked modeling:** masked models must *reconstruct* content. Contrastive models only have to *tell samples apart*, so they may throw away detail that isn't needed for that.
- 🤖 **The EEG-specific risk:** if positives come from the same recording, the easiest way to tell samples apart is a subject or session fingerprint (electrode impedance, montage, individual alpha). Those embeddings then cluster by person rather than by brain state, the same confound as in [[evaluation-protocols]]. The survey's version is milder: "arbitrarily chosen sample pairs may yield counterproductive results" (§5.6, p. 25).

## EEGMMI as a frozen-embedding / few-shot testbed (plan, 2026-10-10)
Idea: freeze a pretrained encoder, fit ridge/logistic regression (or few-shot) on its embeddings of PhysioNet EEG Motor Movement/Imagery, and compare with CSP + LDA ([[bci-paradigms]] *Own test*).
- **Pros:** 109 subjects, 64 channels, both imagined and executed movement, open, already downloaded for 10 subjects. Many subjects allow cross-subject and "k trials from a new subject" calibration curves.
- **Contamination:** LaBraM's pretraining corpus *includes* this dataset [[jiang2024large]] (App. D, p. 17), so its embeddings have seen these recordings and any probe on it is optimistic. CBraMod pretrains on TUEG only (§3, p. 6) and uses PhysioNet-MI as a downstream task with test subjects 90–109 [[wang2024cbramod]] (Table 3, p. 8). Use a model whose pretraining excluded EEGMMI, or evaluate only on subjects it never saw.
- **How much pretraining helps here:** CBraMod 0.642 vs 0.620 balanced accuracy without pretraining (same architecture), 4-class imagery, cross-subject [[wang2024cbramod]] (Table 4, p. 10). That is +2 points, with full fine-tuning.
- **Linear probes can be weak:** LaBraM's linear probe on TUEV is 0.346 vs 0.641 fine-tuned (Table 10, p. 22) [[jiang2024large]]. 🤖 A ridge-on-embeddings result may undersell the model. Report probe *and* fine-tune.
- **Imagined vs executed is a poor target:** class = recording run, so a frozen encoder that captures session/recording fingerprints (likely, 🤖) would "solve" it by block identity. Keep the held-out-run split and the rest-period control. 🤖 Better targets inside EEGMMI: **left vs right fist within imagery** (both classes interleaved in the same run, so no block confound), or the 4-class imagery task (comparable to CBraMod Table 3).
- 🤖 Report against CSP + LDA and EEGNet trained per subject with the same few trials. The honest question is whether embeddings beat those at small k.

## Open questions
- How much pretraining data is enough? LaBraM extrapolates to ≥10k h (§3.6), but Base peaks at 500 h on TUAB.
- Does pretraining help cross-subject BCI tasks (motor imagery, emotion), or mostly clinical TUH-like tasks? (the 🤖 point in [[jiang2024large]]) *Partial (2026-10-11):* on FACED emotion (held-out subjects, 9 classes) pretrained models lead: CBraMod 0.551, LaBraM 0.527, BIOT 0.512 vs best non-pretrained 0.489 (ContraWR) and EEGNet 0.409 [[wang2024cbramod]] (Table 2). A modest gain → [[emotion-recognition]].
- Fine-tuning vs linear probing: which should count as evidence of "generic" representations? → [[evaluation-protocols]]

## Related concepts
- [[channel-heterogeneity]]: pooling many datasets requires handling different montages.
- [[evaluation-protocols]]: how pretrained models are evaluated (probe vs fine-tune, data overlap).
- [[cnn-transformer-hybrid]]: the common backbone shape.
