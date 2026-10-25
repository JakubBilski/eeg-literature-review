---
slug: domain-adaptation
fields: [eeg, ml]
familiarity: introduced     # human's level: new | introduced | understood | skip (ML-standard idea; EEG specifics are new)
---

# domain-adaptation

## Field-neutral description
A model trained on data from some sources (people, sessions, devices, datasets) performs worse on a new source whose data distribution differs. Domain adaptation covers the techniques that reduce this gap: normalizing or aligning each source, training features that can't tell sources apart, or quickly re-tuning on a little data from the new source.

## Synonyms by community
- **EEG:** cross-subject / subject-independent / calibration-free decoding, inter-subject variability, cross-session transfer, calibration, Riemannian re-centering / alignment, Euclidean alignment
- **Neuroscience / clinical:** individual differences; baseline correction (subtracting a resting baseline)
- **Signal processing:** —
- **General ML:** domain shift, covariate shift, transfer learning, domain-adversarial training (DANN), MMD alignment, test-time adaptation, few-shot adaptation, meta-learning (MAML)

## Why EEG needs it
- Brain responses to the same condition differ between people (anatomy, gender, culture) and drift within a person over a session, e.g. as electrode gel dries [[li2022eeg]] (§4.5, p. 18, Fig. 24).
- Examples of the cost: 95% → 70% when going from one user to three pooled users (Kim & André), and BiDCNN on DEAP valence 94.4% within-subject vs 68.1% cross-subject [[li2022eeg]] (p. 18, Table 4).
- BCI: inter-/intra-subject variability is "one of the most important obstacles"; per-user calibration is slow [[varbu2022past]] (§6.1).
- Device and montage differences are a shift too → [[channel-heterogeneity]].

## Families of fixes ([[li2022eeg]] §4.5, pp. 18–21)
1. **Calibrate or align each source:** subtract a per-subject resting baseline; re-center each subject's covariance matrices to a common Riemannian reference ([[riemannian-methods]]); per-subject ("stratified") normalization instead of batch normalization.
2. **Aspect-specific models:** separate models per gender or culture, or cluster users and transfer from the most similar cluster.
3. **Transfer learning:**
   - classical: TCA, MIDA;
   - fine-tuning a network pretrained on other subjects;
   - adversarial (DANN: the feature extractor is trained to fool a subject/domain classifier) and MMD-based alignment;
   - meta-learning (MAML) for fast adaptation with few target labels; teacher→student distillation.
4. **Subject-invariant features:** select features whose distributions agree across people.
- Foundation models take a fifth route: pretrain on many subjects and datasets, then fine-tune → [[self-supervised-pretraining]]. [[li2022eeg]] proposed this as future work (p. 29).

## Papers
- [[li2022eeg]]: the 4-family taxonomy above for emotion recognition, and many cross-subject numbers (Table 4). It recommends cross-*dataset* adaptation and raw-signal Riemannian alignment as next steps (pp. 28–29).
- [[varbu2022past]]: inter-subject variability and calibration as the main practical BCI obstacles (§6.1).
- [[chaddad2023electroencephalography]]: proposes domain adaptation for device differences across datasets (§3).
- [[roy2019deep]]: in 2010–2018, 61% of DL papers were inter-subject, but only 22 of 108 held subjects out (pp. 22–23). One study got 75% on seen vs 38% on unseen subjects (p. 23). Pooling subjects, then fine-tuning per subject worked best (ref [127], p. 27).
- [[liu2026eeg]]: Euclidean alignment (whitening each subject's mean covariance to identity, a Riemannian re-centering) improves most models in cross-subject MI on BNCI2014001 (Fig. 7c, p. 23). EA also mixes channels, which may conflict with coordinate-aware FMs (p. 25).

- [[bomatter2025limited]]: participant distribution shift bounds scaling. With a person-level shift, overfitting is governed by the number of people, not data per person (theory, §3), and on TUAB/CAUEEG more segments per person don't help (Fig. 3). Standard augmentations don't close the gap; the authors ask for augmentations that imitate person differences (§5).
- [[poziomska2025quantity]]: the "more data" alternative to adaptation. Pooling 39 Polish hospitals costs ~10 AUC points vs single-site TUH at equal size; growing the pool to 55,787 recordings recovers most of it (META 81.8 → 88.7; Table B.5), with a fitted ceiling ≈ TUH level (Table 4). 🤖 No hospital is held out, so this is robustness to seen sites, not adaptation to new ones.

## Variants & disagreements
- 🤖 Many DA papers use the *unlabelled* target subject's test data during training (transductive). That's legitimate only if the deployment scenario allows it, so compare DA numbers to plain cross-subject numbers with care.
- 🤖 Within one dataset, "cross-subject" still shares device, lab, stimuli and protocol. Cross-*dataset* transfer is the harder and rarer test [[li2022eeg]] (p. 28).

## Open questions
- How much does simple per-subject alignment (Riemannian / Euclidean re-centering) close the cross-subject gap compared with adversarial DA or foundation-model fine-tuning, on the same benchmark? → [[q7-foundation-models-vs-baselines]]
- A dedicated EEG transfer-learning review: Wan et al. 2021 (Neurocomputing 421:1–14), recommended by [[li2022eeg]] (p. 21). Pre-2022; not in screening.

## Related concepts
- [[channel-heterogeneity]]: montage and device shift.
- [[riemannian-methods]]: covariance re-centering as alignment.
- [[evaluation-protocols]]: within- vs cross-subject splits measure different things.
- [[self-supervised-pretraining]]: pretrain broadly, then adapt.
- [[emotion-recognition]]: where most of the DA literature reviewed here comes from.
