---
slug: subject-diversity-gap
status: idea
questions: [q9, q7, q6]
concepts: [evaluation-protocols, domain-adaptation, sleep-staging, self-supervised-pretraining]
datasets: [shhs, physionet-2018]
scripts: []
figures: []
cost: medium          # ~200 short supervised runs + CBraMod fine-tunes (GPU hours); ~70 GB SHHS download after an NSRR data-access request
origin: 2026-10-12, "if we limit same-person recordings, does training performance drop toward test performance?" ([[q9-pretraining-objectives-and-scale]] *Does the lack of size scaling undermine EEG FMs?*)
updated: 2026-10-12
---

# subject-diversity-gap

*Design v2 (2026-10-12), rewritten after the independent review below: SHHS instead of Sleep-EDF, a nested core of seen test people, size × K as the main question, and an FM arm.*

## Hypothesis
🤖 In supervised sleep staging, the number of distinct people K gates the benefit of model capacity: at fixed labelled data E, larger models gain more from extra people than small ones. The same holds for a pretrained FM, so the field's "bigger FMs don't help" is partly a few-people effect of downstream sets. The plain "more people beats more epochs per person" effect is expected to be small, since [[oliveira2026scaling]] already found it "generally limited". It is measured, but it is not the main claim.

Pre-registered (κ = Cohen's kappa on 5 stages, primary metric; CIs = 95% bootstrap over test people, plus spread over draws × seeds):
- **H1:** κ on unseen people rises from K = 20 to K = 1000 at E = 20k by more than the CI.
- **H2:** the seen-vs-unseen gap, κ(core) − κ(unseen), falls by ≥ 50% from K = 20 to K = 1000.
- **H3 (main):** the slope of κ(unseen) vs log K is steeper for the ~1M CNN than for the ~10k CNN (size × K interaction).
- **H4 (FM):** CBraMod's fine-tuning gain over the same architecture trained from scratch changes with K. The direction is not pre-specified; either sign is informative.

## Design
- **Data:**
  - **Main:** SHHS via NSRR (data-access request + DUA): ~5,793 people at visit 1, 2,651 also at visit 2 (~5 years later).
  - **Pilot (open, while the request is pending):** PhysioNet 2018 Challenge, 994 people with stage labels, one night each. The pilot runs the unseen arm only (no H2).
  - **Channel:** one central mastoid-referenced derivation in both, C4−A1 (SHHS) ≈ C4−M1 (PhysioNet 2018). Resample to 100 Hz for the CNNs and 200 Hz for CBraMod. Never mix with Sleep-EDF's Fpz−Cz.
- **Subject pools (drawn once, fixed for every arm):**
  - *Unseen test:* 300 people, never trained on.
  - *Validation:* 50 people, for tuning and early stopping.
  - *Core:* 10 people with both visits. They are in **every** training set. Their seen-subject test is their visit-2 night (primary), plus held-out 30-min blocks of their visit-1 night with 10-min gaps on each side (secondary; no aging confound, but adjacent in time).
  - *Training pool:* the rest. Each arm draws K − 10 more people from it.
- **Axis 1, people K at fixed labelled data E:**
  - E = 20k epochs: K ∈ {20, 100, 1000}.
  - E = 100k: K ∈ {100, 1000, 5000}.
  - Constraint: E/K ≤ ~800 epochs per person (one night).
  - Each person contributes E/K epochs, **stratified by stage** in that person's own proportions.
- **Input:** one 30-s epoch per example, with no sequence context, so subsampling epochs doesn't break the model. κ will be lower than sequence-model SOTA (🤖 ~0.65–0.75 expected); that is fine for a comparison.
- **Axis 2, model:**
  - band power (5 bands + ratios) + logistic regression (classical control);
  - one CNN family widened to ~10k / ~100k / ~1M parameters;
  - **FM arm:** CBraMod (~4M; pretrained on TUEG only, so no SHHS exposure) in three modes: frozen + linear probe, full fine-tune, and the same architecture from random init.
  - Don't use BIOT-shhs or SleepFM: their pretraining includes SHHS or PSG archives that may overlap. Check REVE's corpus before adding it.
- **Tuning:** per (model, E, K) cell, a small grid (3 learning rates × 2 weight decays) on validation people, with one seed. This addresses the review's "recipe tuned at small K" threat.
- **Repeats:** 3 subject draws × 2 seeds per cell. ≈ 6 configs × 6 (E, K) cells × 6 repeats ≈ 216 final runs, plus tuning.
- **Metrics:** held-out **cross-entropy (bits per epoch)** as co-primary with κ: it is smoother than thresholded scores and is the readout under which [[oliveira2026scaling]] did see a subject effect. Also balanced accuracy, on train, core visit 2, core within-night and unseen. Compare arms **paired** on the same test people (paired bootstrap over people), not with unpaired tests over seeds. The pilot estimates the minimal detectable difference for 300 test people before SHHS is requested.
  - Gap = κ(core v2) − κ(unseen).
  - κ(core within-night) − κ(core v2) estimates the 5-year aging / equipment shift on its own.
- **Task contrast (option, 2026-10-12):** sleep staging is the task where people should matter *least* (labels vary within a person; Oliveira's ISRUC was trial-dominated, p. 6). Adding a one-label-per-person task (TUAB abnormal, ~2,300 people) would test the prediction that the K effect and the size × K interaction are stronger there. Decide after reading [[bomatter2025limited]].
- **Secondary (only if time):** identity probe = linear subject-ID decoding from penultimate features on core people. [[wang2024causes]] predicts it matters little for multi-class-per-subject tasks like sleep; a one-class-per-subject task (TUAB) would be the proper test.
- **Stop rules** (from the review, applied to SHHS):
  - if the gap at K = 20 is < 2 κ points or its CI includes 0, drop H2 and the identity probe;
  - if κ(unseen) at K = 1000 is within the CI of K = 20 for every model, report the null (replicates Oliveira) and keep only H3/H4;
  - if the 1M CNN never beats 10k even at E = 100k, K = 5000, H3 is untestable at this scale.

## What each outcome would mean
- **H3 holds** (big models gain more from people) → in EEG, capacity is gated by subject count. Downstream sets with tens of people would hide any FM size benefit → [[q7-foundation-models-vs-baselines]], [[q9-pretraining-objectives-and-scale]].
- **H3 fails** (no interaction; the big CNN is never better) → the few-people explanation of non-scaling is wrong for supervised sleep. Look at objective misalignment and label noise instead (Q9 *Why pretext gains don't transfer downstream*).
- **H4:**
  - *FM gain shrinks with K* → pretraining mainly substitutes for missing people (consistent with "FMs help most with few subjects").
  - *FM gain grows with K* → pretraining helps exploit diversity, matching EEG-Arena's "gain grows with labels" ([[chen2026benchmarking]] Fig. 4; caveat: its small-budget runs often collapsed).
- **H1/H2:**
  - *Hold* → people, not epochs, are the effective data size for downstream sets.
  - *Null* → replicates [[oliveira2026scaling]] at 10× more people.
- **Large aging shift** (core within-night ≫ core visit 2) → the same person across years behaves like a new person. "Within-subject" calibration then has a shelf life (→ [[evaluation-protocols]] *When is within-subject evaluation clinically realistic?*).

## Prior work
- [[oliveira2026scaling]] (main text read 2026-10-12): 5 models × 4 datasets (PhysioNet-MI 109, ISRUC sleep 118, TUAB ~3,000, NMT ~1,500 people), 80/20 cross-subject split, 5 seeds, power laws fitted to **test cross-entropy** over subjects and trials (§3.3–3.4).
  - **The two readouts disagree.** The loss fits say "subject diversity is the binding constraint" (p. 4): per-subject recording saturates fast once enough people are in (ISRUC: ~35 people and one night reach >85% of the gain), and the subject term dominates on TUAB/NMT (Table 2, Fig. 2). The matched-volume comparison says differences "were generally limited" (§4, Fig. 3).
  - That comparison uses **one model (CTNet), balanced accuracy, 5 seeds, unpaired Mann–Whitney** (Fig. 3 caption). Test sets are 20% of people (≈ 22 for PhysioNet, ≈ 24 for ISRUC). The ISRUC High tier has only two arms (p. 3).
  - 🤖 So the null is a low-resolution null, in line with the human's point (2026-10-12) that a coarse downstream readout may hide the effect. Our design must use the sharper readout (held-out cross-entropy) and paired comparisons.
  - No seen-vs-unseen gap, no identity probe, no within-architecture size axis ("remains to be isolated", p. 8). REVE lagged at 10–25% of subjects on PhysioNet and then caught up (p. 7).
- [[bomatter2025limited]] (screening, abstract; NeurIPS 2025): EEG scaling with total samples vs participant diversity in a multi-level data model, also testing augmentation and SSL. "Model performance scaling can be severely constrained by participant distribution shifts." **Closest prior work; read in full before running** (it may already cover axis 1 and the SSL arm).
- [[banville2025scaling]] (screening): image decoding from EEG/MEG/fMRI; per [[oliveira2026scaling]] (p. 2) it suggests data per subject may matter more there.
- [[wang2024causes]] (abstract): the cross-subject drop comes from inter-subject variability (multi-class-per-subject tasks) vs identity shortcuts (one-class-per-subject tasks).
- [[zare2026negative]] (abstract): FMs decode *dataset* identity at 1.000.
- [[eegmmi-imagined-vs-executed]] (own): recording-block identity inflated a within-session result.
- [[chen2026benchmarking]]: within-subject FM margins ~2× cross-subject (Fig. 3 re-tally); pretrain-vs-scratch gain by label budget (Fig. 4).
- [[olesen2020automatic]] (screening): mixed-cohort sleep staging on SHHS and other NSRR cohorts; source for cohort sizes and channel handling.

### Other fields
- [[yong2025effects]] (speech ASR; abstract): at fixed training hours, more speakers beats more hours per speaker, and "more speakers enables ASR performance gains from scaling number of hours". 🤖 A speakers × hours interaction, the closest analogue to H3 (people gate the benefit of another resource). Transfers if EEG people behave like speakers (a person-level shift at test).
- [[berrebbi2023more]] (speech; abstract): SSL (wav2vec 2.0) mostly needs unlabeled *hours*, self-training needs labelled *speakers*, especially at low resource. 🤖 This suggests pretraining (FM) and supervised fine-tuning may want different compositions, which is relevant to H4.
- [[ooi2025longer]] (fMRI; abstract): prediction accuracy grows with sample size × scan time per person (R² = 0.89 over 76 phenotypes). The two are interchangeable for scans ≤ 20 min, but sample size is "ultimately more important". 🤖 The closest neuroimaging analogue, and its interchangeability-then-divergence pattern is what Oliveira's loss fits suggest too.
- [[denadel2026evaluating]] (single-cell FMs; title only, plus [[oliveira2026scaling]] p. 7): performance plateaus as pretraining data grows. A non-EEG case where FM data scaling fails, as a contrast to the REVE series ([[chen2026benchmarking]]).
- Vision: wide vs deep face datasets (Bansal et al., arXiv 1705.07426; not read, not screened).
- 🤖 **Speech is a conservative prior for EEG (asked 2026-10-12):** in speech, extra hours per speaker bring new label content (new words), and people still win. EEG from one person and device adds less new content per hour. The analogy is closest for tasks whose label varies within a person (sleep, MI) and weakest for one-label-per-person diagnosis, where people should matter most. Details → [[q9-pretraining-objectives-and-scale]] *Does speech transfer?*
- 🤖 **Cross-field reading:** in speech and fMRI, people matter more than time per person once there is some data per person, and people also unlock the value of other resources. EEG's one supporting null (Oliveira's accuracy comparison) is the low-resolution readout. The prior therefore favours running H1–H3, but [[bomatter2025limited]] must be read first.

## Review (2026-10-12, independent subagent, full text of Oliveira + abstracts + dataset pages)
**Verdict: pursue with major changes.** 🤖 throughout except identifiers and facts marked from sources.
- **Feasibility bug:** one Sleep-EDF night ≈ 900–1,100 scored epochs, so E = 20,000 with K = 5 needs ~4 nights per person, and the "other night" test needs one more. On Sleep-EDF, E ≤ ~1,000 · K_min, which collapses the K axis to ~3×. The seen-test set (a) also changes with K (5 people vs 58), so the gap is measured on different populations.
- **Pre-registrable version:** nested subject sets with a fixed core of C seen-test subjects in every arm. E ∈ {20k, 100k}, K ∈ {20, 50, 200, 1000}, κ as the primary metric, one channel, stage-stratified sampling per subject.
  - H1: κ on unseen subjects rises with K, from K = 20 to 1000, by more than the 95% CI over 5 subject draws.
  - H2: the gap κ(core) − κ(unseen) falls by ≥ 50% over the same range.
  - H3: κ(unseen) rises faster with log K for the ~1M model than for the ~10k model (a size × K interaction).
- **Novelty, the main axis is largely done:**
  - [[oliveira2026scaling]] (reviewer read the arXiv full text, §3.3/§4, Fig. 3, Table 1) compares trial-heavy, balanced and subject-heavy splits at fixed volume tiers. It uses CTNet on 4 datasets, including ISRUC sleep (118 people) and TUAB/NMT (~1–3k). Composition differences were "generally limited". It has no seen-vs-unseen gap, no identity probe and no model-size axis (size is listed as future work, §5). It mentions REVE underperforming at 10–25% of subjects and catching up later (§5), an anecdotal hint of H3.
  - [[wang2024causes]] (abstract checked): the cross-subject drop comes mainly from inter-subject variability in tasks with several classes per subject (MI, emotion, ERP), and from shortcut learning in one-class-per-subject tasks (disease detection). For sleep staging, an identity probe is therefore likely uninformative; run it on TUAB if identity matters.
  - Speech has answered the same question: more speakers beats more hours per speaker at fixed hours (Yong et al. 2025, arXiv 2506.04364; Berrebbi et al., arXiv 2211.00854). Vision: wide vs deep face datasets (Bansal et al., arXiv 1705.07426; conclusion not read). These are out-of-field and not in screening.
  - **New:** the size × K interaction, and a nested-core seen/unseen gap at large K, in EEG.
- **Threats (ranked):**
  1. *Construct validity:* the vault's large-model penalty concerns *pretrained FMs* fine-tuned on small sets. A 10k → 1M scratch-CNN sweep doesn't test that; add a frozen or fine-tuned FM arm, or rename the claim.
  2. *Tiny effect:* within-dataset sleep staging has a small seen/unseen gap (a few κ points), about the noise level of 20 test subjects. Hundreds of unseen test subjects are needed.
  3. *Class mix:* contiguous E/K blocks change the stage distribution with K (N3 early, REM late), and small blocks miss stages. Stratify by stage, or subsample whole nights.
  4. *"Other night" means different things:* consecutive nights (Sleep-EDF) vs ~5 years later (SHHS2), which confounds aging and equipment with identity.
  5. *Recipe tuned once* on small K biases the comparison against large models at large K.
  6. Compute is not the issue; data access is.
- **Minimal version:** one dataset with ≥1,000 people, E = 20k, K ∈ {20, 100, 1000}, 10k vs 1M parameters, 3 draws × 2 seeds, 300 fixed unseen test subjects, a 10-subject nested core: 36 runs, days on 1–2 GPUs.
- **Kill criteria:**
  - Gap at K = 20 is < 2 κ points or its CI includes 0 → drop the gap and the identity arms.
  - κ(unseen) at K = 1000 is within the CI of K = 20 → replicates Oliveira; stop the K axis.
  - The 1M model doesn't beat 10k even at K = 1000, E = 100k → H3 can't be tested at this scale.
- **Datasets (the human's question):** a large pool widens the K axis (E ≤ ~1,000 · K_min) and allows hundreds of unseen test subjects.
  - **SHHS (NSRR):** ~5,793 people at visit 1, 2,651 at visit 2 (~5 years later). Free NSRR data-access request + DUA; the current procedure was not verified. **Recommended** for the K axis and the unseen test, with SHHS2 as the seen-subject other-night test, stating the 5-year confound.
  - **PhysioNet 2018 Challenge:** 1,985 people, 994 with stage labels, one night each, open (ODC-By). A **pilot** while the NSRR request is pending, unseen arm only.
  - **Human Sleep Project (BDSP):** ~15k+ MGH patients, credentialed (CITI training + restricted DUA). Overkill for a first pass.
  - Sleep-EDF / HMC / ISRUC: 78 / 151 / 118 people, open.
  - Don't mix Fpz−Cz (Sleep-EDF) with SHHS central derivations. SHHS sizes are cross-cited by [[olesen2020automatic]] (screening).
- **Likely outcome 🤖:** the K-at-fixed-E effect is small (replicating Oliveira); the size × K interaction is the open, publishable part.
- *Note after the review (2026-10-12, main session):* Oliveira's "generally limited" holds only for its accuracy comparison (CTNet, 5 seeds, unpaired). Its own loss-based fits call subjects "the binding constraint" (p. 4). So "largely done" overstates it; see *Prior work*.

## Results
<!-- none yet -->

## Log
- 2026-10-12 prior work extended after reading [[oliveira2026scaling]] in full and searching adjacent fields (speech, fMRI, single-cell). Its "limited" composition effect comes from the coarse accuracy readout, so cross-entropy is now co-primary with paired tests. Bomatter & Gouk 2025 is to be read first. Status stays `idea` (human, 2026-10-12).
- 2026-10-12 design v2: SHHS + PhysioNet 2018 pilot, nested core, H1–H4 pre-registered, CBraMod arm, per-cell tuning, stop rules.
- 2026-10-12 independent review filed (pursue with major changes; SHHS recommended; main axis largely done by [[oliveira2026scaling]]).
- 2026-10-12 created from the human's question; pretraining-level version = the distinct-subject axis of [[pretext-downstream-scaling-sweep]].
