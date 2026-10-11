---
slug: covariance-pseudo-labels
status: idea
questions: [q9, q7]
concepts: [riemannian-methods, self-supervised-pretraining, channel-heterogeneity]
datasets: [tueg, isruc, tuab, moabb-mi]
scripts: []
figures: []
cost: high            # FM pretraining (two iterations) on TUEG
origin: 2026-10-12, "why not use covariance clusters as starting targets for SSL?" ([[q9-pretraining-objectives-and-scale]])
updated: 2026-10-12
---

# covariance-pseudo-labels

## Hypothesis
🤖 HuBERT-style iteration-1 pseudo-labels from k-means on filter-bank covariance matrices add cross-channel (spatial) information to spectral pseudo-labels. They should help spatially localized tasks (motor imagery, focal abnormalities) more than sleep staging, and not help transient-morphology tasks (TUEV). The reasoning, obstacles and prior work are in [[q9-pretraining-objectives-and-scale]] *Covariance matrices as pseudo-label seeds?*.

## Design
- **Descriptor:** filter bank (θ 4–8, α 8–13, β 13–30 Hz), 4 s windows, 19 common 10-20 channels, shrinkage covariance per band.
- **Clustering:** map to the tangent space at the global (log-Euclidean) mean, concatenate bands, k-means with k = 100 → iteration-1 targets. Then the usual iteration 2: k = 500 on hidden states ([[hubert-style-pseudo-labels]]).
- **Two variants:** with and without per-recording re-centering. Without it, clusters likely follow subject/device; with it, recording-level traits (diffuse slowing) are removed.
- **Control:** band-power k-means on identical windows (the diagonal only). The difference isolates the value of the off-diagonal terms.
- **Everything else fixed:** backbone, corpus (TUEG subset), steps, masking.
- **Probes:** linear probe + fine-tune on sleep (ISRUC), TUAB, TUEV and a MOABB motor-imagery set, against a tangent-space Riemannian baseline on the same splits.
- **Cheap pre-check (cost low):** cluster purity of the iteration-1 labels against sleep stages and against subject ID, before any pretraining. If clusters track subject ID more than stage, the un-centred variant is dead.

## What each outcome would mean
- Covariance > band power on MI/TUAB → spatial coupling is a useful pretext target that current FMs ignore.
- Covariance ≈ band power → the diagonal (spectrum) carries what matters; the Riemannian advantage in BCI comes from the classifier/geometry, not the descriptor.
- Re-centred > un-centred on BCI, but < on TUAB → the expected nuisance-vs-trait trade-off; you would need both kinds of target.

## Prior work
- [[tibermacine2026manifold]] (Manifold-SimCLR, contrastive SSL on covariance manifolds): read first.
- [[chen2026unified]] (SPD tokens in a transformer), [[kobler2022spd]] (TSMNet), [[wilson2025deep]] (EE(G)-SPDNet): supervised deep Riemannian nets.
- [[pan2024task]]: unsupervised Riemannian microstate clustering.
- [[xie2026specbram]]: the band-power target this extends.
- Related idea: [[cross-channel-phase-target]] (lagged cross-channel phase as a regression target).

## Results
—

## Log
- 2026-10-12 idea from the Q9 question; design moved here from the hub.
