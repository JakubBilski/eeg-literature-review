---
slug: q3-typical-tasks
kind: hub
status: stub
updated: 2026-10-10
---

# q3-typical-tasks

> What are the typical tasks involving EEG (clinical diagnosis, sleep, BCI, affective/cognitive state, ...)?

## Current answer
- Commonly listed tasks: seizure/epilepsy classification, stress detection, sleep staging, motor imagery, abnormal-EEG identification, emotion analysis, auditory attention detection [[jiang2024large]] (§1).
- **BCI** paradigms: motor imagery, SSVEP, P300 spellers, used to control wheelchairs, prostheses, drones, software [[sabio2024scoping]] (§Research domains); [[song2022eeg]] (§I). What each paradigm is and how they're classified (active/passive, evoked/spontaneous, sync/async) → [[bci-paradigms]].
  - **In 202 BCI application papers (2009–2019):** non-medical 58%, medical 31%, both 11% [[varbu2022past]] (Fig. 5).
    - Medical BCI is mostly *assistive* (74%: robot arms, prostheses, wheelchairs), then rehabilitation (9%, mostly stroke) (Fig. 6).
    - Non-medical BCI is mostly *monitoring* (50%: fatigue, attention, emotion), then machine control (17%) and entertainment (16%) (Fig. 7).
  - Paradigm counts: motor imagery 38, visual evoked potentials 31, drowsiness/attention monitoring 29, emotion 15 (Fig. 11). Motor imagery is mostly medical (62%), monitoring almost entirely non-medical (88–93%).
  - Main obstacles: subject-to-subject variability, calibration time, low throughput, and noise outside the lab (§6.1).
- Among consumer-device studies: BCI 44.5%, experimental research 31.2%, signal processing 12.0%, clinical 6.2%, validation 6.2% [[sabio2024scoping]] (§Research domains).
- Among 110 high-impact **wireless** EEG studies: cognitive monitoring 44% (attention, workload, emotion; classrooms, driving, neuromarketing), clinical 24% (mostly at-home seizure detection and sleep staging), methodological 22%, communication and control 10% (SSVEP, motor imagery, P300 for games and robots) [[niso2022wireless]] (§4.2, Fig. 7a; p. 14). Cognitive monitoring is 60% of the studies where participants move (§4.2.1).
  - 🤖 This differs from Sabio's consumer-device mix, where BCI leads (44.5%). The two use different categories and samples (5 brands vs high-citation journal papers).
- **Clinical** benchmark tasks used by foundation models: abnormal vs normal EEG (TUAB), event types such as spikes, periodic discharges and artifacts (TUEV) [[jiang2024large]] (§3.1).
- Broader applications in a general review: epilepsy, motor imagery, depression, stroke, Alzheimer's, sleep disorders and staging, emotion, schizophrenia, and driver/pilot fatigue and workload [[chaddad2023electroencephalography]] (Tables 1, 4–6).
- Common datasets per task: DEAP and SEED (emotion), BCI IV-2a (motor imagery), Bonn, CHB-MIT and Siena (seizure), Sleep-EDF (sleep) [[chaddad2023electroencephalography]] (Table 3, §3).
- Standard benchmark datasets met so far: BCI IV-2a/2b (motor imagery), SEED / SEED-V (emotion), TUAB / TUEV (clinical), MoBI (gait) [[song2022eeg]]; [[jiang2024large]].

- **Where labels come from** (experiment design, self-report, expert annotation) and which clinical metadata ships with datasets → [[eeg-labels-and-metadata]].
- **What clinical EEG is good for** (discussed 2026-10-10): EEG is "the most common diagnostic investigation for patients with suspected seizures or epilepsy" [[wong2023eeg]] (§1). Clinical reading looks for large, stereotyped events such as seizures, spikes and periodic discharges (the TUEV classes; [[jiang2024large]] §3.1). Recordings use certified devices, gel and 10-20 [[niso2022wireless]] (§3.15). 🤖 So the arguments against comparing devices bite less here: the events are big relative to noise and the setup is standardized. They bite hard for subtle population-level differences such as psychiatric conditions → [[eeg-depression-detection]]. Scalp EEG is "less sensitive" than intracranial EEG [[wong2023eeg]] (§2). Why imaging (CT/MRI/fMRI) doesn't replace EEG for these uses → [[q1-what-is-eeg]] *Is EEG redundant to imaging?*
  - **Indications and how well EEG performs (asked 2026-10-11: "does EEG have well-documented diagnostic value?").** 🤖 Main point: clinical EEG rarely *names a disease*. It answers functional questions: is there epileptic activity, is this patient seizing now, how badly is the brain depressed. Its value is high for a few of those and low for the many vague indications it gets ordered for.
    - **Epilepsy (main use):** interictal epileptiform discharges are specific but insensitive. Web-sourced numbers, not yet read in full: the first routine EEG finds them in ~22% of adults with active epilepsy, 33.8% cumulatively by the 4th EEG (Irish cohort, [IMJ](https://imj.ie/?p=12115)); ~80% when wake and sleep recordings are combined or ~6 recordings are repeated ([Smith & Kennett 2015 chapter](https://epilepsysociety.org.uk/sites/default/files/2020-08/Chapter20SmithKennett2015.pdf)). 🤖 So a normal EEG does not rule out epilepsy. It is used to support a clinical diagnosis and to classify the syndrome (focal vs generalised), which guides drug choice.
    - **Low-yield indications:** in 1,094 EEGs ordered for syncope (fainting), 1.46% had epileptiform discharges, about the rate in healthy adults (2005 review, via web search). In a paediatric study every EEG for syncope (n = 19) and headache (n = 43) was normal ([Gazi Univ.](https://avesis.gazi.edu.tr/yayin/0c138ce8-612c-4d92-8cdb-f0b176c456ba/utility-of-electroencephalography-in-the-evaluation-of-common-neurologic-conditions-in-children)). 🤖 This is the basis for the human's impression: many hospital EEGs are ordered for "funny turns", dizziness, headache, where the yield is near zero. Over-reading benign variants as epileptiform is a known cause of epilepsy misdiagnosis (textbook; unsourced).
    - **ICU / coma:** detects nonconvulsive seizures and status epilepticus, which have no visible signs (textbook 🤖; source candidate [[bitar2024utility]]). After cardiac arrest, guideline "highly malignant" patterns (suppression or burst-suppression at ≥24 h) predict poor outcome with sensitivity 50%, specificity 93%, and 97% if also unreactive, in 845 patients (TTM2) [[turella2024predictive]] (abstract via web search). Self-fulfilling-prophecy bias is possible, since life support could be withdrawn.
    - 🤖 **Other established uses** (textbook, unsourced): PSG for sleep disorders and the MSLT (sleep-latency test) for narcolepsy; depth of anaesthesia monitoring (processed EEG indices); neonatal seizures (most are electrographic only); encephalitis and encephalopathy (nonspecific diffuse slowing, periodic discharges); Creutzfeldt-Jakob disease (periodic sharp-wave complexes, part of the diagnostic criteria); an ancillary role in brain-death testing.
    - 🤖 **Not established clinically:** psychiatric diagnosis (depression, ADHD, schizophrenia), dementia subtyping, concussion. These are where the ML literature reports its highest accuracies → [[eeg-depression-detection]], [[q6-reliability-of-eeg-diagnoses]].
- **Sleep staging:** each 30 s epoch of a night is labelled Wake / N1 / N2 / N3 / REM. The clinical reference is polysomnography (PSG): EEG + eye + chin muscle + cardio-respiratory channels, scored by hand [[gans2024sleep]] (pp. 1–2); [[wang2024cbramod]] (App. E.1). → [[sleep-staging]]
  - It is the clearest at-home use of wearable EEG: 34 devices exist, 24 validated against PSG. Overall κ is 0.42–0.79 where reported, N1 is poorly detected, and 64% of validations were run in a clinic or lab, only 12% at home [[gans2024sleep]] (§3, Table 1).
  - Diagnostic use: the stage percentages are mostly descriptive. Diagnosis relies on REM (narcolepsy, REM sleep behaviour disorder as an early Parkinson's sign), on sleep/wake timing, and on breathing channels for apnea → [[sleep-staging]] *Diagnostic use of the stages* (mostly 🤖, partly sourced via [[gans2024sleep]] refs).
  - As an ML benchmark (ISRUC, 5-class): κ 0.70–0.74 across EEGNet, USleep, LaBraM and CBraMod [[wang2024cbramod]] (Table 7).
- **Seizure detection and prediction** → [[seizure-detection]]. Detection flags an ongoing seizure (needs ictal + interictal data); prediction warns before onset (preictal + interictal) [[wong2023eeg]] (§5.5).
  - Seizures are <1% of recorded EEG (§2). There are 10 public datasets, 5 scalp and 4 intracranial (Table 2).
  - The most used is Bonn (58 of 120 studies, Table A1): single-channel, pre-cut, balanced, no patient IDs.
  - TUSZ is the largest (≈600 subjects, 3,050 seizures; Tables 5, 8). CHB-MIT (23 children) is the usual foundation-model benchmark [[wang2024cbramod]] (Table 8).
- **Emotion recognition** → [[emotion-recognition]]. Subjects watch film clips, music videos or pictures. Labels are either the clip's intended emotion (SEED) or the person's own valence/arousal rating per trial (DEAP, DREAMER) [[li2022eeg]] (§2.1, Table 3).
  - Datasets are small: 15–32 subjects (Table 3). FACED is a larger exception (123 subjects, [[wang2024cbramod]] §4).
  - Reported accuracies: 0.85–0.98 within-subject, mostly 0.65–0.90 cross-subject [[li2022eeg]] (Table 4). On held-out subjects in FACED (9 classes) the best is 0.55 [[wang2024cbramod]] (Table 2).
  - The neural basis is unsettled: frontal alpha asymmetry vs beta effects; no single region per emotion [[li2022eeg]] (§2.2).
  - Applications named: driver monitoring, affective disorders (PTSD, depression), music/media recommendation, games, VR learning (§1, p. 2).
- **Depression (MDD) detection:** reported accuracies are very high (0.91–0.99), but they rest on small single-site datasets and depend on the split. See [[eeg-depression-detection]].

## Comparisons
| task family | example datasets | in vault papers |
|---|---|---|
| motor imagery (BCI) | BCI IV-2a, 2b | [[song2022eeg]], [[varbu2022past]] |
| SSVEP / P300 (BCI) | — (not yet in vault) | [[varbu2022past]], [[bci-paradigms]] |
| drowsiness / attention / workload monitoring | — | [[varbu2022past]], [[niso2022wireless]] |
| emotion recognition | DEAP, SEED, SEED-IV/V, DREAMER, FACED | [[li2022eeg]], [[song2022eeg]], [[jiang2024large]], [[wang2024cbramod]], [[emotion-recognition]] |
| clinical: abnormal / events | TUAB, TUEV | [[jiang2024large]] |
| gait / movement regression | MoBI | [[jiang2024large]] |
| seizure detection / prediction | CHB-MIT, TUSZ, Bonn, Siena | [[wong2023eeg]], [[wang2024cbramod]], [[seizure-detection]] |
| sleep staging | ISRUC, Sleep-EDF; wearable-vs-PSG validations | [[gans2024sleep]], [[wang2024cbramod]], [[sleep-staging]] |

## Open threads
- Seizure detection: datasets covered by [[wong2023eeg]]. Still missing: a 2022+ review of methods and clinical performance (sensitivity, false alarms per hour), and inter-rater agreement on seizure labels.
- Sleep: human inter-scorer agreement is now sourced (κ 0.76 overall, 0.24 on N1 [[lee2021interrater]], abstract only) → [[sleep-staging]]. Full read pending (open access in PMC).
- Emotion: read [[li2022eeg]] (2026-10-11). Still missing: any test of whether emotion models decode the clip or muscle activity rather than emotion → [[emotion-recognition]] *Open questions*.
- BCI after 2019: [[varbu2022past]] stops in Oct 2019, so a 2022+ BCI review covering DL/transfer learning is still missing.

## Sources
- [[chaddad2023electroencephalography]]: application tables and a dataset list (Tables 1, 3–6).
- [[jiang2024large]]: task list and clinical benchmarks.
- [[sabio2024scoping]]: usage categories and BCI paradigms.
- [[song2022eeg]]: motor imagery and emotion benchmarks.
- [[niso2022wireless]]: application categories in wireless EEG studies.
- [[gans2024sleep]]: sleep staging with EEG wearables, validated against PSG.
- [[varbu2022past]]: BCI applications 2009–2019; paradigm taxonomy and frequencies.
- [[wong2023eeg]]: public seizure datasets and their characteristics.
- [[li2022eeg]]: emotion recognition: labels, datasets, features, models, splits.
