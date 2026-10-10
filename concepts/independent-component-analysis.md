---
slug: independent-component-analysis
fields: [eeg, neuro-clinical, signal-processing, ml]
familiarity: introduced     # human's level: new | introduced | understood | skip
---

# independent-component-analysis

## Field-neutral description
Several sensors each record a different weighted mixture of the same hidden sources. The method recovers the sources, and how strongly each one reaches each sensor, by assuming only that the sources are statistically independent of each other.

## Synonyms by community
- **EEG:** ICA, independent components (ICs), IC scalp maps / topographies, IC rejection, artifact subspace (cf. ASR)
- **Neuroscience / clinical:** source separation, artifact correction
- **Signal processing:** blind source separation (BSS), the "cocktail party problem", unmixing / demixing matrix, FastICA, Infomax
- **General ML:** linear latent-variable model with non-Gaussian factors, a cousin of PCA / factor analysis

## How it works (Q&A 2026-10-10)
- **Model:** X = A·S [[chaddad2023electroencephalography]] (§2.2.2, Eq. 2).
  - X is the recording (channels × time), S the sources (components × time), A the mixing matrix.
  - Unmixing means estimating W ≈ A⁻¹ so that S = W·X, by "exploiting non-Gaussianity" (Algorithm 3).
- **Each component has two parts:** a **time course** (a row of S) and a **scalp map** (a column of A: how strongly the source shows at each electrode). To remove an artifact, zero its row of S and recompute A·S.
- **Priors: none spatial, only statistical.** Sources are assumed independent and non-Gaussian, the mixing linear and fixed over the recording, and the sources no more numerous than the channels (🤖 standard assumptions). Linear, instantaneous mixing is physically plausible because scalp fields are a smeared sum of sources [[roy2019deep]] (p. 2).
- **Number of components** is a user choice (`n_components` input, Algorithm 3). 🤖 Usually it is the channel count or the data rank. Re-referencing or dropping channels lowers the rank, so PCA reduction comes first.
- **How non-Gaussianity is encouraged** (🤖 standard theory; the vault only has Algorithm 3):
  - *Why it works:* by the central limit theorem, mixtures are *more* Gaussian than their sources, so the least-Gaussian projections are likely the sources.
  - *Recipe:* center and whiten (Algorithm 3), which leaves only a rotation to find. Then pick the rotation maximizing non-Gaussianity: FastICA uses kurtosis or negentropy; Infomax (the EEGLAB default) uses maximum likelihood with a heavy-tailed source prior.
- **Not least squares** (🤖):
  - With a square, invertible A, any invertible W gives zero reconstruction error, so MSE can't choose a solution. The problem is identifiability, not fitting.
  - Whitening fixes everything except a rotation, and independence fixes the rotation. Gaussian sources would be unidentifiable.
  - An MSE / reconstruction objective gives PCA instead.
- **Labelling is manual or heuristic:** components "can be visually examined" (blink = frontal, spiky) [[chaddad2023electroencephalography]] (§2.2.2). Artifact removal "usually require[s] the intervention of a human expert" [[roy2019deep]] (p. 16).
- 🤖 **ML view:** like PCA, but the rotation is chosen for independence instead of variance. Components are unordered, and their sign and scale are arbitrary.

## Papers
- [[chaddad2023electroencephalography]]: ICA as the main blind-source-separation denoiser (§2.2.2, Algorithm 3). ERASE adds EMG reference channels so muscle noise concentrates in a few components (26% more EMG removed). ICA + wavelet hybrids appear in Table 2.
- [[roy2019deep]]: wavelet-based ICA cited as an artifact method still needing expert tuning (p. 16) *(paper not yet fully read)*.

## Variants & disagreements
- Purpose: **artifact removal** (drop components, keep the EEG) vs **source analysis** (interpret components as brain sources). Same algorithm, different goal.
- Algorithms: FastICA vs Infomax vs AMICA etc. (🤖 not compared in the vault).

## Open questions
- Do deep / foundation models benefit from ICA-cleaned input, or do they learn to ignore artifacts? → [[signal-quality-and-noise]]
- Automatic component labelling (e.g. ICLabel): no vault source yet.

## Related concepts
- [[signal-quality-and-noise]]: ICA is the workhorse artifact-removal method.
- [[riemannian-methods]]: both rest on the linear-mixing model. Riemannian distances are invariant to exactly the mixing ICA tries to undo.
- ? CSP (common spatial patterns): a supervised spatial filter, see [[classical-ml-baselines]]. Same "linear spatial filter" family, but a different objective (class-variance contrast vs independence).
