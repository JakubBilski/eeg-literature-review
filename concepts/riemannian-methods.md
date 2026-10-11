---
slug: riemannian-methods
fields: [eeg, signal-processing, ml]
familiarity: introduced     # human's level: new | introduced | understood | skip
---

# riemannian-methods

## Field-neutral description
Summarize each multichannel recording by how its channels co-vary, then compare recordings with a distance that respects the curved geometry of such summaries. That distance ignores any fixed linear re-mixing of the sensors.

## Synonyms by community
- **EEG / BCI:** Riemannian geometry classifiers, MDM, tangent-space classification, covariance-based BCI, Riemannian re-centering (transfer)
- **Neuroscience / clinical:** functional connectivity matrices (related use of the same objects)
- **Signal processing:** SPD (symmetric positive-definite) matrix manifold, spatial covariance, information geometry
- **General ML:** manifold learning on SPD matrices, metric learning, nearest centroid

## How it works (🤖 standard method, no vault source yet; Lotte 2018 should cover it)
- **Input:** each trial (channels × time) becomes its C × C channel covariance matrix. Covariance matrices are SPD and live on a curved manifold, not a flat vector space.
- **Distance:** the affine-invariant metric, δ(A, B) = sqrt(Σᵢ log² λᵢ), where λᵢ are the eigenvalues of A⁻¹B.
  - Key property: δ(WAWᵀ, WBWᵀ) = δ(A, B) for any invertible W.
  - So fixed linear channel mixing (volume conduction, reference choice) doesn't change distances.
- **Classifiers:** not only kNN.
  - *MDM* (minimum distance to mean): nearest centroid with Riemannian (Fréchet) class means.
  - *Tangent-space mapping:* flatten around a reference point, vectorize, then any classifier (logistic regression, SVM, LDA). Usually the strongest variant.
  - kNN with δ is possible but less common.
- **Transfer:** re-centering each subject's or session's covariances to a common reference is a simple cross-subject adaptation.

## Papers
- [[roy2019deep]]: only 2 of 156 DL papers used Riemannian baselines, "although these methods have set a new state-of-the-art in multiple EEG classification tasks" (§4, p. 28).
- [[li2022eeg]]: in emotion recognition, (a) aligning source and target subjects' covariances on the Riemannian manifold as a cross-subject fix (§4.5, p. 18), and (b) RFNet, which maps covariances to the tangent space and fuses them with an LSTM over band signals (§4.4, Fig. 23). It recommends raw-signal Riemannian alignment, borrowed from motor imagery, for cross-dataset emotion work (p. 29). → [[domain-adaptation]]

- [[lawhern2018eegnet]]: **xDAWN + tangent space + elastic net** (the Kaggle BCI Challenge winner: xDAWN ERP spatial filters → covariances → tangent space with the log-Euclidean metric → elastic net) as the ERP baseline, run on the same splits as the CNNs (§2.2.3, p. 10). Cross-subject it beats every CNN on ERN (AUC ~0.765 vs ≤0.745) but loses on P300 (~0.80 vs ~0.90) and MRCP (~0.70 vs ~0.81) (Fig. 4, p. 14). Within-subject it is behind EEGNet on all three (Fig. 2).

## Variants & disagreements
- How they compare with pretrained foundation models on matched protocols: no vault evidence → [[classical-ml-baselines]].
- Against small CNNs (2018, matched splits): mixed, paradigm-dependent, see [[lawhern2018eegnet]] above.

## Open questions
- Source to add: Lotte et al. 2018 (BCI classifier review, Roy ref [105]). It would let this note move from 🤖 to sourced.

## Related concepts
- [[domain-adaptation]]: re-centering is one of its simplest forms.
- [[independent-component-analysis]]: same linear-mixing view of EEG. ICA undoes the mixing; the Riemannian distance is invariant to it.
- [[channel-heterogeneity]]: ? covariance matrices are tied to a fixed channel set, so montage changes break them. Re-centering helps across subjects, but not across montages (🤖 to verify).
- [[evaluation-protocols]]: re-centering is a cross-subject / cross-session technique.
