---
slug: linear-discriminant-analysis
fields: [eeg, signal-processing, ml]
familiarity: introduced     # human's level: new | introduced | understood | skip
---

# linear-discriminant-analysis

## Field-neutral description
A simple classifier that draws a straight line (a flat boundary) between groups. It assumes each group's measurements scatter like a bell-shaped cloud of the same shape, differing only in where the cloud is centred, and picks the direction along which the cloud centres are furthest apart relative to the cloud width.

## Synonyms by community
- **EEG / BCI:** LDA, shrinkage LDA (sLDA, rLDA), "the linear classifier" in CSP + LDA, Fisher classifier
- **Neuroscience / clinical:** linear decoder, discriminant function analysis
- **Signal processing:** Fisher discriminant, matched filter for Gaussian classes with equal covariance
- **General ML:** Fisher's linear discriminant, Gaussian generative classifier with tied covariance (≈ QDA with shared covariance); *not* latent Dirichlet allocation

## How it works (🤖 textbook material, no vault source yet; Lotte 2018 should cover it)
- **Model:** each class k is Gaussian N(μ_k, Σ) with one covariance Σ shared by all classes. Bayes' rule then gives a decision function that is linear in x: w = Σ⁻¹(μ_A − μ_B), predict A if wᵀx > threshold.
- **Fisher's view (same w for two classes):** find the projection that maximizes between-class variance over within-class variance. No Gaussian assumption needed to motivate it.
- **Also a dimensionality reducer:** with K classes it gives at most K − 1 discriminant directions (sklearn `transform`).
- **Shrinkage:** with few trials and many features, the estimate of Σ is noisy and Σ⁻¹ blows up. Shrinkage blends it with a scaled identity, Σ̂ = (1 − γ)S + γνI, with γ chosen analytically (Ledoit–Wolf). In sklearn: `LinearDiscriminantAnalysis(solver="lsqr", shrinkage="auto")`.
- **Why BCI likes it:** a handful of parameters, closed-form fit, no hyperparameters to tune once shrinkage is automatic, and hard to overfit. EEG trials are few (tens to hundreds per subject), which is exactly the regime where this matters.
- **Weakness:** the boundary is linear, and with tied covariance it can only use *mean* differences between classes. Differences in variance (power) must be turned into mean differences by the features first, which is what log-variance CSP features do ([[common-spatial-patterns]]).

## Papers
- [[varbu2022past]]: the most common classifier in 2009–2019 EEG-BCI papers: 35/114 (31%), vs SVM 24 (21%), CNN 5 (4%) (Fig. 13). Described as "a simple classifier with low computation requirements and acceptable accuracy" (§5.9).
- [[chaddad2023electroencephalography]]: listed among traditional classifiers (SVM, KNN, RF, LDA, NB) (§2.5.1). Here SVM, not LDA, is called the most important.
- Own analysis (2026-10-10): CSP + shrinkage LDA on EEGMMI, imagined vs executed → [[bci-paradigms]] *Imagined vs executed movement*, `scripts/classify_imagery_vs_execution.py`. Accuracy fell from 0.83 (shuffled) to 0.56 (cross-subject), so the simple classifier still overfit the *recording*, not the brain state ([[evaluation-protocols]]).

## Variants & disagreements
- **LDA vs SVM as the default:** BCI papers favour LDA [[varbu2022past]] (Fig. 13); broader EEG-classification reviews favour SVM [[chaddad2023electroencephalography]] (§2.5.1). 🤖 With a linear kernel and good regularization, both usually land close; the choice matters less than the features and the split.
- **LDA vs CSP:** both find linear projections from labelled data. LDA separates class *means* of a feature vector. CSP separates class *variances* of the channel signals. They are complementary: CSP makes the features, LDA classifies them.
- **Shrinkage LDA on a Riemannian tangent space** is one of the tangent-space classifier options ([[riemannian-methods]]).

## Open questions
- Is shrinkage LDA on good features still competitive with frozen foundation-model embeddings + linear probe at small k? A linear probe on embeddings is itself essentially LDA/logistic regression → [[q7-foundation-models-vs-baselines]].

## Related concepts
- [[common-spatial-patterns]]: the usual feature extractor in front of LDA for motor imagery.
- [[classical-ml-baselines]]: where LDA sits among classical baselines and how much DL beats them.
- [[riemannian-methods]]: tangent-space features can feed LDA.
- [[evaluation-protocols]]: a low-capacity classifier does not protect against leaky splits.
- ? linear-probing: a linear classifier on frozen embeddings; LDA is one choice for the probe ([[self-supervised-pretraining]]).
