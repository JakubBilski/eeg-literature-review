---
slug: q6-reliability-of-eeg-diagnoses
kind: hub
status: stub
updated: 2026-10-10
---

# q6-reliability-of-eeg-diagnoses

> How reliable are EEG-based diagnoses and predictions, by clinicians and by models? What inflates reported accuracies (split leakage, confounds, small single-site data), and do results hold across sites and devices?

*Added 2026-10-10 at the human's request, after the theme came up in 3 questions across 2 sessions. Facts live in the linked notes; this hub summarizes them.*

## Current answer

### Does EEG ML "work"? Scorecard by task (asked 2026-10-11)
*The human's first impression was "most EEG analysis methods don't really work, because there's not enough data to train models to recognize such noisy data". After discussion it was refined (human, 2026-10-11): **raw data isn't the bottleneck. The bottleneck is data with good labels across many subjects, plus a shortage of well-defined diagnostic problems.***

| task | best reported, honest protocol | reference point | verdict 🤖 |
|---|---|---|---|
| sleep staging (ISRUC, 5-class) | κ 0.74 (CBraMod) [[wang2024cbramod]] Table 7 | human scorers κ 0.76 [[lee2021interrater]] | imitates scorers at their own ceiling. Not a diagnostic success: κ ≈ 0.75 is weak as diagnostic accuracy, and the stage labels are rarely used diagnostically anyway → [[sleep-staging]] *Diagnostic use* |
| abnormal vs normal EEG (TUAB) | bal. acc. 0.83, AUROC 0.92 [[jiang2024large]] Table 1 | — | moderate, but it depends on what "abnormal" means (below) |
| seizure detection (CHB-MIT, subject split) | bal. acc. 0.74, AUC-PR 0.37 [[wang2024cbramod]] Table 8 | — | far from clinical use; test set is 2 children |
| motor imagery, 4-class, cross-subject | 0.64 (chance 0.25) [[wang2024cbramod]] Table 3 | — | works per user after calibration; weak across people |
| emotion, 9-class, held-out subjects (FACED, 123 subj.) | bal. acc. 0.55 (CBraMod; chance ≈ 0.11) [[wang2024cbramod]] Table 2 | 0.9+ in the literature, mostly within-subject or segment splits [[li2022eeg]] Table 4 | above chance, far from a per-person readout; labels are clip categories or self-reports → [[emotion-recognition]] |
| depression | 0.9+ reported | small single-site data, leaky splits | unknown; numbers probably inflated |

- 🤖 **It works where the signal is big and the label is tied to the signal:** sleep stages are *defined* by the EEG pattern, and seizures are large discharges. It fails or is unverified where the target is subtle, subjective or confounded (depression, emotion, cross-subject imagery).
- 🤖 **More data alone hasn't been the fix.** Pretraining on 2,500 h barely helps motor imagery (CBraMod 0.642 vs 0.620 without pretraining; [[wang2024cbramod]] Table 4). LaBraM-Base pretrained on 500 h beat the same model on 2,500 h on TUAB ([[jiang2024large]] §3.6, Fig. 5). The ceilings come from label noise (sleep κ 0.76), person-to-person variability ([[varbu2022past]] §6.1) and few labelled *subjects* rather than few hours: CHB-MIT has 326,993 windows but 23 people ([[wang2024cbramod]] App. E.2).
- 🤖 **What TUAB "abnormal" means (unverified, needs the dataset paper):** as I understand it, each *recording session* carries one normal/abnormal label taken from the neurologist's report. "Abnormal" lumps together any reportable finding (focal or diffuse slowing, epileptiform discharges, ...), and every 10 s window inherits its session's label. If so, this is triage ("does a neurologist need to look closely?"), not a diagnosis. Window-level accuracy is also partly mislabelled by construction, since an abnormal recording has many normal-looking windows. The vault so far only says "all data have been annotated as normal or abnormal" ([[jiang2024large]] §3.1, p. 6). The TUAB dataset paper is in the reading queue.
- 🤖 **Much of the "doesn't work" impression comes from evaluation, not models.** Leaky splits, curated datasets like Bonn, and confounds produce near-perfect numbers that collapse under honest protocols (rows below). The honest numbers are modest but real.

### Other findings
- **Clinical reading works best for large, stereotyped events** (seizures, spikes, periodic discharges) recorded on standardized gel 10-20 setups. It is weakest for subtle, population-level differences such as psychiatric conditions. → [[q3-typical-tasks]] (*What clinical EEG is good for*)
- **Reported model accuracies depend heavily on the split.** Splitting by recording instead of by subject inflates scores, e.g. DeprNet 99.37% vs 91.4%, and papers mix protocols on the same dataset. → [[evaluation-protocols]]
- **Confounded recording blocks inflate scores too (own example):** when each class is recorded in its own run, shuffled CV reports 0.83 but held-out runs give 0.64, and the same pipeline separates the *rest* periods equally well. → [[evaluation-protocols]], [[bci-paradigms]]
- **Emotion recognition: the same model loses 10–26 points going from within- to cross-subject** (DGCNN on SEED 90.4 → 79.95%; BiDCNN on DEAP valence 94.4 → 68.1%), and the review itself calls random segment-level k-fold a leaky, "wrong" split (§5.3) [[li2022eeg]] (Table 4, p. 25). 🤖 Two possible confounds are untested: decoding the *clip* instead of the emotion, and facial muscle in the β/γ bands. → [[emotion-recognition]], [[domain-adaptation]]
- **Depression detection looks easy, but on tiny single-site data:** 0.91–0.96 balanced accuracy on 64 subjects with a 10-person test set; untested across sites. → [[eeg-depression-detection]]
- **Results across devices are unverified.** There is no standardized multi-device quality benchmark, only pairwise validations, and a larger N doesn't remove the confounding between device, population, task and lab. → [[q2-measuring-devices]] (*Why there's no cross-device signal-quality benchmark*)
- **Wearable sleep staging vs PSG:** overall κ is 0.42–0.79 where reported, and N1 sensitivity goes as low as 0.16–0.21. Validation is mostly in labs with small samples, and 21 of 38 studies are at high risk of bias in ≥1 QUADAS-2 domain [[gans2024sleep]] (§3, §3.3, Table 1). The "ground truth" is itself a human scorer, whose results vary with training (p. 10). → [[sleep-staging]]
- **The most-used seizure dataset is the least realistic:** Bonn (58 of 120 highly cited studies) is single-channel, curated by eye, balanced by construction (real recordings are <1% seizure) and has no patient IDs, so subject-wise splits are impossible [[wong2023eeg]] (§2, §5.4, §5.6, §6.1, Table A1). The authors suspect small datasets get cited *because* overfitting makes results look impressive (§8). Two public implanted-EEG sets share patients, a leakage trap (§7). → [[seizure-detection]], [[evaluation-protocols]]
- **Seizure benchmarks under realistic imbalance are hard:** on CHB-MIT with a subject split, the best foundation model reaches balanced accuracy 0.74 and AUC-PR 0.37 [[wang2024cbramod]] (Table 8). The test set is only 2 children. → [[seizure-detection]]
- **Human experts disagree too:** two scorers on the same PSG reach κ 0.76 overall but only 0.24 on N1 and 0.57 on N2/N3 [[lee2021interrater]] (Abstract). 🤖 So devices and models at κ ≈ 0.75 are already near the label-noise ceiling. → [[sleep-staging]] *How clearly are the stages defined?*
- **Label reliability belongs in this hub** (decided 2026-10-11; not a separate core question). Expert labels can be defined by the signal itself (sleep stages), clinically marginal (N1–N3 are rarely used diagnostically), and noisy, yet still serve as benchmarks. → [[sleep-staging]] *Why is 5-class staging a benchmark at all?*, [[eeg-labels-and-metadata]]
- 🤖 **"Quality" depends on the task.** Apart from amplifier noise, how good a recording is depends on the prediction target, so reliability has to be judged for each task. → [[signal-quality-and-noise]]
- **Transfer across montages and devices:** foundation models handle montage differences by design (electrode embeddings). Whether they bridge *devices*, and whether they pick up device fingerprints as shortcuts, is untested in the vault. → [[channel-heterogeneity]]
- **How strong the baselines are:** small models and classical methods often come within a few points of foundation models, which limits how much a given benchmark can tell apart. → [[classical-ml-baselines]], [[q7-foundation-models-vs-baselines]]

## Comparisons

## Open threads
- Cross-site / cross-dataset generalization for any diagnostic task (depression first). No source yet.
- A standardized multi-device benchmark (ERP CORE + SME) since 2022? Not searched yet.
- Do foundation models transfer to dry, low-channel devices? Do they learn device shortcuts? (reading queue in [[interests]])
- Inter-rater agreement among clinicians reading EEG: answered for sleep (below). Seizure and abnormal-EEG reading are still unsourced; [[wong2023eeg]] does not cover it.

## Sources
- [[chaddad2023electroencephalography]]: split dependence (DeprNet, Table 6).
- [[wang2024cbramod]]: depression benchmark (Mumtaz2016, Table 10).
- [[jiang2024large]]: patient-level splits; pretraining dominated by TUH.
- [[niso2022wireless]]: no signal-quality comparison; inconsistent methods reporting (pp. 13–14).
- [[sabio2024scoping]]: pairwise device validations (§Validation).
- [[gans2024sleep]]: reliability of wearable sleep staging against PSG; risk of bias (§3.3).
- [[lee2021interrater]]: human inter-scorer κ for sleep staging *(abstract only)*.
- [[li2022eeg]]: emotion recognition; within vs cross-subject gap; split taxonomy with segment leakage (§4.5, §5.3, Table 4).
- [[wong2023eeg]]: EEG as the main diagnostic test for epilepsy; how dataset construction (no patient IDs, balancing, channel preselection, overlap) inflates seizure results (§5–8).
