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
- **Clinical reading works best for large, stereotyped events** (seizures, spikes, periodic discharges) recorded on standardized gel 10-20 setups. It is weakest for subtle, population-level differences such as psychiatric conditions. → [[q3-typical-tasks]] (*What clinical EEG is good for*)
- **Reported model accuracies depend heavily on the split.** Splitting by recording instead of by subject inflates scores, e.g. DeprNet 99.37% vs 91.4%, and papers mix protocols on the same dataset. → [[evaluation-protocols]]
- **Confounded recording blocks inflate scores too (own example):** when each class is recorded in its own run, shuffled CV reports 0.83 but held-out runs give 0.64, and the same pipeline separates the *rest* periods equally well. → [[evaluation-protocols]], [[bci-paradigms]]
- **Depression detection looks easy, but on tiny single-site data:** 0.91–0.96 balanced accuracy on 64 subjects with a 10-person test set; untested across sites. → [[eeg-depression-detection]]
- **Results across devices are unverified.** There is no standardized multi-device quality benchmark, only pairwise validations, and a larger N doesn't remove the confounding between device, population, task and lab. → [[q2-measuring-devices]] (*Why there's no cross-device signal-quality benchmark*)
- **Wearable sleep staging vs PSG:** overall κ is 0.42–0.79 where reported, and N1 sensitivity goes as low as 0.16–0.21. Validation is mostly in labs with small samples, and 21 of 38 studies are at high risk of bias in ≥1 QUADAS-2 domain [[gans2024sleep]] (§3, §3.3, Table 1). The "ground truth" is itself a human scorer, whose results vary with training (p. 10). → [[sleep-staging]]
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
- Inter-rater agreement among clinicians reading EEG: answered for sleep (below). Seizure and abnormal-EEG reading are still unsourced.

## Sources
- [[chaddad2023electroencephalography]]: split dependence (DeprNet, Table 6).
- [[wang2024cbramod]]: depression benchmark (Mumtaz2016, Table 10).
- [[jiang2024large]]: patient-level splits; pretraining dominated by TUH.
- [[niso2022wireless]]: no signal-quality comparison; inconsistent methods reporting (pp. 13–14).
- [[sabio2024scoping]]: pairwise device validations (§Validation).
- [[gans2024sleep]]: reliability of wearable sleep staging against PSG; risk of bias (§3.3).
- [[lee2021interrater]]: human inter-scorer κ for sleep staging *(abstract only)*.
- [[wong2023eeg]]: EEG as the main diagnostic test for epilepsy; scalp vs intracranial sensitivity (§1–2).
