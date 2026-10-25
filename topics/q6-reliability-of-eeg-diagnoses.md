---
slug: q6-reliability-of-eeg-diagnoses
kind: hub
status: stub
updated: 2026-10-11
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
| seizure detection, event-level (7 continuous cohorts, frozen FMs) | mean sensitivity over 0.1–100 FA/h 0.55 (NeuroLM); ≤0.36 on an unseen cohort [[kontras2026neuroatlas]] Tables 4–5 | random-init encoder 0.44 | far from clinical use; most of the alarm range is clinically irrelevant (2026-10-25) |
| sleep-EEG brain-age gap → cognitive impairment (100 vs 100) | AUROC 0.59 (Sun et al. features) [[kontras2026neuroatlas]] p. 7 | chance 0.5 | not useful as a marker yet |

- 🤖 **It works where the signal is big and the label is tied to the signal:** sleep stages are *defined* by the EEG pattern, and seizures are large discharges. It fails or is unverified where the target is subtle, subjective or confounded (depression, emotion, cross-subject imagery).
- 🤖 **More data alone hasn't been the fix.** Pretraining on 2,500 h barely helps motor imagery (CBraMod 0.642 vs 0.620 without pretraining; [[wang2024cbramod]] Table 4). LaBraM-Base pretrained on 500 h beat the same model on 2,500 h on TUAB ([[jiang2024large]] §3.6, Fig. 5). The ceilings come from label noise (sleep κ 0.76), person-to-person variability ([[varbu2022past]] §6.1) and few labelled *subjects* rather than few hours: CHB-MIT has 326,993 windows but 23 people ([[wang2024cbramod]] App. E.2).
- 🤖 **What TUAB "abnormal" means (unverified, needs the dataset paper):** as I understand it, each *recording session* carries one normal/abnormal label taken from the neurologist's report. "Abnormal" lumps together any reportable finding (focal or diffuse slowing, epileptiform discharges, ...), and every 10 s window inherits its session's label. If so, this is triage ("does a neurologist need to look closely?"), not a diagnosis. Window-level accuracy is also partly mislabelled by construction, since an abnormal recording has many normal-looking windows. The vault so far only says "all data have been annotated as normal or abnormal" ([[jiang2024large]] §3.1, p. 6). The TUAB dataset paper is in the reading queue.
- **The labelled-data view has a source:** already in 2018, DL-EEG papers on clinical data named "the lack of labeled data, rather than the quantity of data" as the obstacle [[roy2019deep]] (p. 24). Half the datasets in 156 DL papers had <13 subjects (p. 11). In one study, accuracy on new subjects plateaued above ~15 training subjects (ref [191], p. 12).
- **For one-label-per-person diagnosis, the number of people is the data size.** On TUAB and dementia (CAUEEG), accuracy rises strongly up to several hundred people, while more data per person adds ~nothing; at a fixed 8,000 TUAB segments, 25 people give 0.74 and 800 give 0.84 [[bomatter2025limited]] (Figs. 2–3). Most EEG datasets sit far below that (half of those in [[roy2019deep]] had <13 participants). 🤖 So small single-site diagnostic studies are data-starved however long their recordings are.
- 🤖 **Is EEG ML astrology? (the human's impression, 2026-10-25)** My view: no for the measurement, partly for the ML literature.
  - *The signal is real and reproducible:* alpha blocking on eye opening, sleep spindles and slow waves, seizure discharges, and ERD at C3/C4 (seen in the own EEGMMI plots). Clinical reading of large events (seizures, ICU, coma, sleep) is established practice → [[q3-typical-tasks]].
  - *The astrology-like part is the evaluation culture:* leaky splits, curated datasets, confounds (eye movements, device, site), single runs, and metrics chosen for looks. Honest protocols such as cross-site, event-level and confound-filtered testing keep shrinking claims (NeuroAtlas, [[liu2026eeg]], [[wong2023eeg]]).
  - *The honest picture:* EEG ML works where the label is a large, EEG-defined event or state (sleep staging near human agreement, abnormal-EEG triage at AUROC ~0.9). It is unproven for subtle population differences (psychiatry, cognitive decline, brain age as a marker). Foundation models haven't changed that yet.
- 🤖 **Much of the "doesn't work" impression comes from evaluation, not models.** Leaky splits, curated datasets like Bonn, and confounds produce near-perfect numbers that collapse under honest protocols (rows below). The honest numbers are modest but real.

### Other findings
- **Clinical reading works best for large, stereotyped events** (seizures, spikes, periodic discharges) recorded on standardized gel 10-20 setups. It is weakest for subtle, population-level differences such as psychiatric conditions. → [[q3-typical-tasks]] (*What clinical EEG is good for*)
- **The DL-EEG literature of 2010–2018 was mostly unverifiable:** 60% of 156 papers used no cross-validation, and only 22 of 108 inter-subject studies held subjects out. 21% had no baseline, and only 7% could easily be reproduced (no data or code for 61 papers). The median +5.4% gain over baselines is probably biased upward [[roy2019deep]] (§3.7–3.8, pp. 21–25, p. 28). → [[evaluation-protocols]], [[classical-ml-baselines]]
- **Reported model accuracies depend heavily on the split.** Splitting by recording instead of by subject inflates scores, e.g. DeprNet 99.37% vs 91.4%, and papers mix protocols on the same dataset. → [[evaluation-protocols]]
- **Confounded recording blocks inflate scores too (own example):** when each class is recorded in its own run, shuffled CV reports 0.83 but held-out runs give 0.64, and the same pipeline separates the *rest* periods equally well. → [[eegmmi-imagined-vs-executed]], [[evaluation-protocols]]
- **Emotion recognition: the same model loses 10–26 points going from within- to cross-subject** (DGCNN on SEED 90.4 → 79.95%; BiDCNN on DEAP valence 94.4 → 68.1%), and the review itself calls random segment-level k-fold a leaky, "wrong" split (§5.3) [[li2022eeg]] (Table 4, p. 25). 🤖 Two possible confounds are untested: decoding the *clip* instead of the emotion, and facial muscle in the β/γ bands. → [[emotion-recognition]], [[domain-adaptation]]
- **Task-irrelevant behaviour can be locked to the label:** in a P300 dataset, target images also required a button press, and EEGNet learned a left-motor-cortex filter alongside the P300 one. Dropping the P300-like filter costs more than dropping the motor one (Table 4) [[lawhern2018eegnet]] (§3.3, Fig. 6, pp. 15–16). 🤖 Filter visualization and ablation are a cheap way to catch such confounds; a model deployed without button presses would lose that part of its signal.
- **Depression detection looks easy, but on tiny single-site data:** 0.91–0.96 balanced accuracy on 64 subjects with a 10-person test set; untested across sites. → [[eeg-depression-detection]]
- **Results across devices are unverified.** There is no standardized multi-device quality benchmark, only pairwise validations, and a larger N doesn't remove the confounding between device, population, task and lab. → [[q2-measuring-devices]] (*Why there's no cross-device signal-quality benchmark*)
- **Wearable sleep staging vs PSG:** overall κ is 0.42–0.79 where reported, and N1 sensitivity goes as low as 0.16–0.21. Validation is mostly in labs with small samples, and 21 of 38 studies are at high risk of bias in ≥1 QUADAS-2 domain [[gans2024sleep]] (§3, §3.3, Table 1). The "ground truth" is itself a human scorer, whose results vary with training (p. 10). → [[sleep-staging]]
- **The most-used seizure dataset is the least realistic:** Bonn (58 of 120 highly cited studies) is single-channel, curated by eye, balanced by construction (real recordings are <1% seizure) and has no patient IDs, so subject-wise splits are impossible [[wong2023eeg]] (§2, §5.4, §5.6, §6.1, Table A1). The authors suspect small datasets get cited *because* overfitting makes results look impressive (§8). Two public implanted-EEG sets share patients, a leakage trap (§7). → [[seizure-detection]], [[evaluation-protocols]]
- **Seizure benchmarks under realistic imbalance are hard:** on CHB-MIT with a subject split, the best foundation model reaches balanced accuracy 0.74 and AUC-PR 0.37 [[wang2024cbramod]] (Table 8). The test set is only 2 children. → [[seizure-detection]]
- **Human experts disagree too:** two scorers on the same PSG reach κ 0.76 overall but only 0.24 on N1 and 0.57 on N2/N3 [[lee2021interrater]] (Abstract). 🤖 So devices and models at κ ≈ 0.75 are already near the label-noise ceiling. → [[sleep-staging]] *How clearly are the stages defined?*
- **Label reliability belongs in this hub** (decided 2026-10-11; not a separate core question). Expert labels can be defined by the signal itself (sleep stages), clinically marginal (N1–N3 are rarely used diagnostically), and noisy, yet still serve as benchmarks. → [[sleep-staging]] *Why is 5-class staging a benchmark at all?*, [[eeg-labels-and-metadata]]
  - 🤖 **No common benchmark task meets all four needs at once** (label not read from the same EEG, clinical meaning, headroom, enough test subjects). BCI tasks have exact labels but little clinical meaning or are solved; clinical tasks have EEG-read labels, tiny or single-site test sets, or a ceiling that may be label noise. Outcome-based labels are the way out → [[eeg-labels-and-metadata]] *Is the field missing a good downstream task?* (2026-10-12)
- 🤖 **"Quality" depends on the task.** Apart from amplifier noise, how good a recording is depends on the prediction target, so reliability has to be judged for each task. → [[signal-quality-and-noise]]
- **Transfer across montages and devices:** foundation models handle montage differences by design (electrode embeddings). Whether they bridge *devices*, and whether they pick up device fingerprints as shortcuts, is untested in the vault. → [[channel-heterogeneity]]
- **Foundation-model evaluations (to Sep 2024) are mostly in-distribution:** 4 of 10 FMs test only on datasets seen in pretraining, and only 2 test on unseen datasets [[kuruppu2026eeg]] (§5.1). No model did artifact removal, so artifact-driven shortcuts are unexamined (§4.1). Clinical few-shot claims (ADHD, MDD, schizophrenia AUC 0.72–0.90 in BrainWave) rest on small public sets (Supp. Table 2). → [[evaluation-protocols]]
  - *2026 update:* the first matched benchmark marks which downstream sets each FM saw in pretraining (e.g. TUAB for 7 of 12). A leakage-aware ranking that drops those sets barely changes the order [[liu2026eeg]] (Supp. Table 54). CHB-MIT there is ictal vs pre-ictal segment classification, not continuous detection, so it says nothing about false alarms per hour (p. 15). 🤖 Within-subject few-shot scores up to 95–99% (EEGMat, SSVEP) may include temporal adjacency between train and test windows; the paper does not describe the split.
- **Without target-cohort labels, performance drops a lot (2026).** NeuroAtlas fits a linear probe on the other cohorts of a domain and tests on the held-out one (LODO) [[kontras2026neuroatlas]]:
  - *Seizures:* every model loses 24–45% of its event-level score, and none reaches what a random-init encoder gets *with* target labels (App. D.3, Table 5). Neonatal EEG is hardest.
  - *Sleep:* κ drops by up to 0.35 (App. D.4).
  - *Brain age:* only 3 of 42 fits beat predicting the cohort's mean age (App. D.5).
  - 🤖 Site and cohort shift matter more than which model is used.
- **Window metrics overstate clinical usability:** AUROC and event-level sensitivity at 0.1–100 false alarms/h rank seizure models differently on every cohort (ρ 0.61–0.81). Sleep κ doesn't predict REM-latency error, and age MAE doesn't predict brain-age-gap utility [[kontras2026neuroatlas]] (App. D.1.2; p. 6; p. 7). → [[seizure-detection]], [[sleep-staging]]
- **Eye-movement and drift confounds in motor imagery:** with a 4 Hz high-pass, a 40 Hz low-pass and the first post-cue second removed, frozen-FM MI decoding drops below the binomial significance threshold. ERP/SSVEP are unaffected [[kontras2026neuroatlas]] (p. 8; App. D.6). 🤖 The filter also removes early ERD, so "artifact-driven" is likely but not proven. → [[bci-paradigms]]
- **How strong the baselines are:** small models and classical methods often come within a few points of foundation models, which limits how much a given benchmark can tell apart. → [[classical-ml-baselines]], [[q7-foundation-models-vs-baselines]]

### Thought experiment: a normative model of healthy EEG (asked 2026-10-11)
*The human asked: what if a large, clean, single-device dataset with patient-level splits existed, and FMs got good at modelling what healthy EEG should look like? Mostly 🤖 speculation. The one sourced test so far is the NeuroAtlas brain-age-gap result (bullet "First evidence" below); a dedicated normative-modelling source is still missing (reading queue in [[interests]]).*
- **The idea has a name: normative modelling.** You model the healthy distribution conditioned on age, sex and state, then score each person by how far they deviate. Analogues known from memory, not yet verified: MRI "brain charts" (Bethlehem et al. 2022), ECG-predicted age vs real age as a mortality marker, and EEG "brain age" from sleep EEG.
- **What it would plausibly fix:**
  - *Fewer false positives:* a model that knows the range of benign variants could counter over-reading, a known cause of epilepsy misdiagnosis → [[q3-typical-tasks]] *Indications*.
  - *Label-free triage:* it needs only "healthy" labels, not disease labels, so it sidesteps the bottleneck identified above (well-labelled data and well-defined diagnostic problems).
  - *Per-person deviation maps:* a disease may deviate in different ways in different patients, which group classifiers average away.
  - *Personal baselines over time:* deviation from your own earlier EEG (ICU trending, wearables).
- **What it can't fix:**
  - *Sampling:* if no spike occurs during a 20-min recording, no model of normal will find one. The exception would be a subtle *background* difference in epilepsy, which is directly testable: score the "normal" first EEGs of patients later diagnosed with epilepsy (→ [[pretext-loss-anomaly-score]] *Extension*).
  - *Deviation ≠ diagnosis:* drowsiness, medication, age and artifacts deviate more than most diseases do. The model must be conditioned on them, which needs metadata → [[eeg-labels-and-metadata]].
  - *Better prediction ≠ better anomaly detection:* lower pretext loss doesn't track feature quality, and raw-MSE error mostly measures power → [[q9-pretraining-objectives-and-scale]] *Is pretext loss itself informative?* In ML generally, generative models can give *higher* likelihood to simple out-of-distribution inputs (Nalisnick et al. 2019, from memory).
  - *Who counts as "healthy"?* Hospital archives (TUH, HEEDB [[sun2025harvard]]) hold referred patients. A "normal" report is a weak proxy for healthy, and volunteer cohorts are skewed (students). A single device keeps the data clean but brings device shift back at deployment.
- **First evidence (2026-10-25):** in NeuroAtlas, a brain-age model is trained on healthy sleep EEG, and its brain-age gap (BAG) is tested on 100 cognitively impaired vs 100 age-matched healthy subjects. The gap separates them only weakly: the best is the feature-based Sun et al. model, ΔBAG +1.99 years, AUROC 0.592; NeuroLM-VQ is similar; most FMs are near chance [[kontras2026neuroatlas]] (p. 7, Fig. 22). Better age prediction did not give a better marker. A 2026 meta-analysis of the sleep-EEG brain-age index vs dementia risk is queued ([[sun2026machine]]).
- **Likely outcome:** better triage, fewer false positives, and a nonspecific "brain-health / brain-age gap" index. New disease-specific diagnoses are unlikely without labelled cohorts, which are needed at least for validation. For psychiatry an honest normative model may mostly show overlap with healthy people, which is itself useful evidence.

## Comparisons

## Open threads
- Can frozen-FM embeddings predict *where* a model will fail (new site, ambiguous labels) better than band-power statistics? → experiment [[embedding-data-diagnostics]] (2026-10-25). Independent review: Test A pursue with major changes (go subject-level, control derivation, add confidence/agreement baselines; ML already shows distances predict shift-induced drops), Test B pursue small, Stage 0 descriptive only. See *Review*.
- Cross-site / cross-dataset generalization for any diagnostic task (depression first). No source yet.
- A standardized multi-device benchmark (ERP CORE + SME) since 2022? Not searched yet.
- Do foundation models transfer to dry, low-channel devices? Do they learn device shortcuts? (reading queue in [[interests]])
- Inter-rater agreement among clinicians reading EEG: answered for sleep (below). Seizure and abnormal-EEG reading are still unsourced; [[wong2023eeg]] does not cover it.

## Sources
- [[kontras2026neuroatlas]]: LODO transfer across cohorts; clinical vs window metrics; MI eye-movement confound filtering; brain-age gap for cognitive impairment.
- [[kuruppu2026eeg]]: in-distribution vs OOD evaluation of EEG foundation models; asks for subject/temporal splits and clinical metrics.
- [[liu2026eeg]]: leakage-aware FM ranking; segment-level CHB-MIT; within-subject few-shot.
- [[chaddad2023electroencephalography]]: split dependence (DeprNet, Table 6).
- [[wang2024cbramod]]: depression benchmark (Mumtaz2016, Table 10).
- [[jiang2024large]]: patient-level splits; pretraining dominated by TUH.
- [[niso2022wireless]]: no signal-quality comparison; inconsistent methods reporting (pp. 13–14).
- [[sabio2024scoping]]: pairwise device validations (§Validation).
- [[gans2024sleep]]: reliability of wearable sleep staging against PSG; risk of bias (§3.3).
- [[lee2021interrater]]: human inter-scorer κ for sleep staging *(abstract only)*.
- [[li2022eeg]]: emotion recognition; within vs cross-subject gap; split taxonomy with segment leakage (§4.5, §5.3, Table 4).
- [[wong2023eeg]]: EEG as the main diagnostic test for epilepsy; how dataset construction (no patient IDs, balancing, channel preselection, overlap) inflates seizure results (§5–8).
- [[lawhern2018eegnet]]: within- vs cross-subject gap per paradigm (Figs. 2–5); button-press confound in P300 found through filter visualization (§3.3).
- [[bomatter2025limited]]: people vs data per person on TUAB, CAUEEG, sleep (Fig. 3).
- [[roy2019deep]]: evaluation and reproducibility practice in 156 DL-EEG papers, 2010–2018; clinical bottleneck = labelled data (pp. 21–25).
