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
- [[kuruppu2026eeg]]: critical review of 10 early EEG foundation models (2021–Sep 2024). Masked reconstruction is used in 7/10, transformers in 9/10, 3.3M–1.7B parameters (§4.2). Linear probes fall far below fine-tuning (LaBraM TUEV 34.6 vs 66.2 balanced accuracy; BrainBERT AUC 0.59 vs 0.83; Supp. Table 2). Evidence for data/model scaling is "weak, if any" (§5.1). General time-series FMs (TimesNet, MOMENT) sometimes beat EEG-FMs (p. 17).

## Variants & disagreements
- Objective: predict raw signal, spectrum, or discrete codes. LaBraM found raw reconstruction better on TUAB but discrete codes better on TUEV (App. G, Table 7). The best target may depend on the task.
- Contrastive (BENDR, BIOT) vs masked (LaBraM, CBraMod): not yet compared in the vault. [[weng2025self]] calls contrastive "the most widely used" and "the most effective" (§5, §5.6) but gives no numbers. 🤖 Note that BENDR is itself a hybrid: masked embeddings with a contrastive loss (§4.1).
- **Taxonomy (pre-foundation-model, ≈2019–2023):** predictive (classify a pseudo-label: time distance, shuffled order, removed band, applied augmentation), generative (reconstruct masked signal, spectrum or embeddings; GANs), contrastive (pull augmented views together; CPC), hybrid [[weng2025self]] (Fig. 3). 🤖 Foundation models mostly use the generative / masked branch at scale.

## Data scale, prediction targets, pretext loss
Moved to the hub [[q9-pretraining-objectives-and-scale]] (2026-10-11): corpus sizes, what each FM predicts and with which loss, target ablations, the MSE double penalty, and what pretext loss does and doesn't tell you.

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

## Latent-space targets, explained (asked 2026-10-11)
- **Idea:** don't reconstruct the input (µV, pixels). Predict the *representation* of the masked part instead. A **target encoder** embeds the full input; the online encoder sees only the visible context; a small **predictor** maps context embeddings plus the masked positions to predicted embeddings. The loss is a distance (MSE or cosine) in embedding space.
- **JEPA** (Joint-Embedding Predictive Architecture; I-JEPA for images, Assran et al. 2023, cited by [[xie2026specbram]] §2). "Joint embedding" because both inputs are embedded; "predictive" because one embedding is predicted from the other. Versus *generative* SSL (reconstruct the input) and *contrastive* SSL (needs negatives). The appeal for EEG: the target encoder can drop unpredictable detail (noise, random phase), so the model doesn't spend capacity on the double penalty → [[q9-pretraining-objectives-and-scale]]. 🤖 NLP analogue: data2vec, where the student predicts the teacher's averaged layer outputs for masked tokens.
- **Collapse:** if both branches output a constant, the loss is zero. Guards are a stop-gradient on the target branch, a momentum encoder, an asymmetric predictor, or explicit variance/isotropy penalties (VICReg; SIGReg, used by SpecBraM, Eq. 2).
- **Momentum encoder:** a copy of the encoder that receives no gradients. Its weights are an exponential moving average (EMA) of the online encoder's: θ_target ← (1 − τ)·θ_target + τ·θ_online. It changes slowly, so the targets are stable while the online encoder learns. It comes from MoCo/BYOL; 🤖 it is the "teacher" in DINO-style self-distillation, essentially Polyak weight averaging. EEGPT: same architecture as the encoder, τ = 0.01, it sees all tokens (masked and visible), and the loss is MSE between the predictor output and LN(momentum features) [[wang2024eegpt]] (Eqs. 5–6). BIOT puts a BYOL-style predictor on a channel/token-dropped view [[yang2023biot]] (§2.3). NSP adds an EMA target encoder and strips channel-identity and time effects from its targets [[yu2026neural]] (abstract).
- **Layer normalization (LN):** take one vector (one token's features, or one patch's samples), subtract its mean and divide by its standard deviation. Inside networks a learnable scale and shift follow; it is the normalization in every Transformer block. Applied to *targets*, for a raw EEG patch it means z-scoring each patch on its own: the DC offset and amplitude go, only the shape is left.
  - EEGPT normalizes both targets this way (LN(menc), LN(patch); Eqs. 6, 8). Without it, pretraining loss was lower (alignment 0.15, reconstruction 0.002) but downstream fell by 1–7 points, because extreme values dominated the MSE [[wang2024eegpt]] (Table 5). MAE's normalized-pixel targets use the same trick.
  - 🤖 The EEG trade-off: amplitude is itself informative (high-amplitude delta in N3, suppression in coma, focal slowing), and a per-patch-normalized target no longer asks the model to predict it.

## EEGMMI as a frozen-embedding / few-shot testbed (plan, 2026-10-10)
Idea: freeze a pretrained encoder, fit ridge/logistic regression (or few-shot) on its embeddings of PhysioNet EEG Motor Movement/Imagery, and compare with CSP + LDA ([[bci-paradigms]] *Own test*).
- **Pros:** 109 subjects, 64 channels, both imagined and executed movement, open, already downloaded for 10 subjects. Many subjects allow cross-subject and "k trials from a new subject" calibration curves.
- **Contamination:** LaBraM's pretraining corpus *includes* this dataset [[jiang2024large]] (App. D, p. 17), so its embeddings have seen these recordings and any probe on it is optimistic. CBraMod pretrains on TUEG only (§3, p. 6) and uses PhysioNet-MI as a downstream task with test subjects 90–109 [[wang2024cbramod]] (Table 3, p. 8). Use a model whose pretraining excluded EEGMMI, or evaluate only on subjects it never saw.
- **How much pretraining helps here:** CBraMod 0.642 vs 0.620 balanced accuracy without pretraining (same architecture), 4-class imagery, cross-subject [[wang2024cbramod]] (Table 4, p. 10). That is +2 points, with full fine-tuning.
- **Linear probes can be weak:** LaBraM's linear probe on TUEV is 0.346 vs 0.641 fine-tuned (Table 10, p. 22) [[jiang2024large]]. 🤖 A ridge-on-embeddings result may undersell the model. Report probe *and* fine-tune.
- **Imagined vs executed is a poor target:** class = recording run, so a frozen encoder that captures session/recording fingerprints (likely, 🤖) would "solve" it by block identity. Keep the held-out-run split and the rest-period control. 🤖 Better targets inside EEGMMI: **left vs right fist within imagery** (both classes interleaved in the same run, so no block confound), or the 4-class imagery task (comparable to CBraMod Table 3).
- 🤖 Report against CSP + LDA and EEGNet trained per subject with the same few trials. The honest question is whether embeddings beat those at small k.

## Open questions
- Does an FM's masked-prediction error work as an unsupervised EEG anomaly score (seizure, abnormal background), beyond what an artifact or amplitude detector gives? No vault source yet (asked 2026-10-11).
- How much pretraining data is enough? LaBraM extrapolates to ≥10k h (§3.6), but Base peaks at 500 h on TUAB. *Field-level (2026-10-11):* across 10 FMs, more channel-hours did not predict better TUAB/TUEV scores, and LaBraM's gains plateau after ~1,000 h [[kuruppu2026eeg]] (Fig. 3, §5.1). Diversity of sources may matter more than volume (p. 15).
- Does pretraining help cross-subject BCI tasks (motor imagery, emotion), or mostly clinical TUH-like tasks? (the 🤖 point in [[jiang2024large]]) *Partial (2026-10-11):* on FACED emotion (held-out subjects, 9 classes) pretrained models lead: CBraMod 0.551, LaBraM 0.527, BIOT 0.512 vs best non-pretrained 0.489 (ContraWR) and EEGNet 0.409 [[wang2024cbramod]] (Table 2). A modest gain → [[emotion-recognition]].
- Fine-tuning vs linear probing: which should count as evidence of "generic" representations? → [[evaluation-protocols]]. *Partial (2026-10-11):* the probe gap is consistent across every FM that reports both. [[kuruppu2026eeg]] reads it as doubt about SSL representation quality (§5.2, p. 18); 🤖 pretraining currently looks like a good initialization rather than a frozen feature extractor.

## Related concepts
- [[channel-heterogeneity]]: pooling many datasets requires handling different montages.
- [[evaluation-protocols]]: how pretrained models are evaluated (probe vs fine-tune, data overlap).
- [[cnn-transformer-hybrid]]: the common backbone shape.
