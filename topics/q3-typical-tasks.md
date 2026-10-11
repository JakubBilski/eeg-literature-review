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
- **What clinical EEG is good for** (discussed 2026-10-10): EEG is "the most common diagnostic investigation for patients with suspected seizures or epilepsy" [[wong2023eeg]] (§1). Clinical reading looks for large, stereotyped events such as seizures, spikes and periodic discharges (the TUEV classes; [[jiang2024large]] §3.1). Recordings use certified devices, gel and 10-20 [[niso2022wireless]] (§3.15). 🤖 So the arguments against comparing devices bite less here: the events are big relative to noise and the setup is standardized. They bite hard for subtle population-level differences such as psychiatric conditions → [[eeg-depression-detection]]. Scalp EEG is "less sensitive" than intracranial EEG [[wong2023eeg]] (§2).
- **Sleep staging:** each 30 s epoch of a night is labelled Wake / N1 / N2 / N3 / REM. The clinical reference is polysomnography (PSG): EEG + eye + chin muscle + cardio-respiratory channels, scored by hand [[gans2024sleep]] (pp. 1–2); [[wang2024cbramod]] (App. E.1). → [[sleep-staging]]
  - It is the clearest at-home use of wearable EEG: 34 devices exist, 24 validated against PSG. Overall κ is 0.42–0.79 where reported, N1 is poorly detected, and 64% of validations were run in a clinic or lab, only 12% at home [[gans2024sleep]] (§3, Table 1).
  - Diagnostic use: the stage percentages are mostly descriptive. Diagnosis relies on REM (narcolepsy, REM sleep behaviour disorder as an early Parkinson's sign), on sleep/wake timing, and on breathing channels for apnea → [[sleep-staging]] *Diagnostic use of the stages* (mostly 🤖, partly sourced via [[gans2024sleep]] refs).
  - As an ML benchmark (ISRUC, 5-class): κ 0.70–0.74 across EEGNet, USleep, LaBraM and CBraMod [[wang2024cbramod]] (Table 7).
- **Depression (MDD) detection:** reported accuracies are very high (0.91–0.99), but they rest on small single-site datasets and depend on the split. See [[eeg-depression-detection]].

## Comparisons
| task family | example datasets | in vault papers |
|---|---|---|
| motor imagery (BCI) | BCI IV-2a, 2b | [[song2022eeg]], [[varbu2022past]] |
| SSVEP / P300 (BCI) | — (not yet in vault) | [[varbu2022past]], [[bci-paradigms]] |
| drowsiness / attention / workload monitoring | — | [[varbu2022past]], [[niso2022wireless]] |
| emotion recognition | SEED, SEED-V | [[song2022eeg]], [[jiang2024large]] |
| clinical: abnormal / events | TUAB, TUEV | [[jiang2024large]] |
| gait / movement regression | MoBI | [[jiang2024large]] |
| sleep staging | ISRUC, Sleep-EDF; wearable-vs-PSG validations | [[gans2024sleep]], [[wang2024cbramod]], [[sleep-staging]] |

## Open threads
- Seizure detection: seed [[wong2023eeg]] (selected sections only so far).
- Sleep: human inter-scorer agreement is now sourced (κ 0.76 overall, 0.24 on N1 [[lee2021interrater]], abstract only) → [[sleep-staging]]. Full read pending (open access in PMC).
- Emotion recognition review: [[li2022eeg]] (downloaded, not yet read).
- BCI after 2019: [[varbu2022past]] stops in Oct 2019, so a 2022+ BCI review covering DL/transfer learning is still missing.

## Sources
- [[chaddad2023electroencephalography]]: application tables and a dataset list (Tables 1, 3–6).
- [[jiang2024large]]: task list and clinical benchmarks.
- [[sabio2024scoping]]: usage categories and BCI paradigms.
- [[song2022eeg]]: motor imagery and emotion benchmarks.
- [[niso2022wireless]]: application categories in wireless EEG studies.
- [[gans2024sleep]]: sleep staging with EEG wearables, validated against PSG.
- [[varbu2022past]]: BCI applications 2009–2019; paradigm taxonomy and frequencies.
