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
- **BCI** paradigms: motor imagery, SSVEP, P300 spellers, used to control wheelchairs, prostheses, drones, software [[sabio2024scoping]] (§Research domains); [[song2022eeg]] (§I).
- Among consumer-device studies: BCI 44.5%, experimental research 31.2%, signal processing 12.0%, clinical 6.2%, validation 6.2% [[sabio2024scoping]] (§Research domains).
- **Clinical** benchmark tasks used by foundation models: abnormal vs normal EEG (TUAB), event types such as spikes, periodic discharges and artifacts (TUEV) [[jiang2024large]] (§3.1).
- Broader applications in a general review: epilepsy, motor imagery, depression, stroke, Alzheimer's, sleep disorders and staging, emotion, schizophrenia, and driver/pilot fatigue and workload [[chaddad2023electroencephalography]] (Tables 1, 4–6).
- Common datasets per task: DEAP and SEED (emotion), BCI IV-2a (motor imagery), Bonn, CHB-MIT and Siena (seizure), Sleep-EDF (sleep) [[chaddad2023electroencephalography]] (Table 3, §3).
- Standard benchmark datasets met so far: BCI IV-2a/2b (motor imagery), SEED / SEED-V (emotion), TUAB / TUEV (clinical), MoBI (gait) [[song2022eeg]]; [[jiang2024large]].

- **Where labels come from** (experiment design, self-report, expert annotation) and which clinical metadata ships with datasets → [[eeg-labels-and-metadata]].
- **Depression (MDD) detection:** reported accuracies are very high (0.91–0.99), but they rest on small single-site datasets and depend on the split. See [[eeg-depression-detection]].

## Comparisons
| task family | example datasets | in vault papers |
|---|---|---|
| motor imagery (BCI) | BCI IV-2a, 2b | [[song2022eeg]] |
| emotion recognition | SEED, SEED-V | [[song2022eeg]], [[jiang2024large]] |
| clinical: abnormal / events | TUAB, TUEV | [[jiang2024large]] |
| gait / movement regression | MoBI | [[jiang2024large]] |

## Open threads
- Sleep staging and seizure detection: seeds [[gans2024sleep]], [[wong2023eeg]] (not yet read).
- Emotion recognition review: [[li2022eeg]] (downloaded, not yet read). BCI overview: [[varbu2022past]] (downloaded, not yet read).

## Sources
- [[chaddad2023electroencephalography]]: application tables and a dataset list (Tables 1, 3–6).
- [[jiang2024large]]: task list and clinical benchmarks.
- [[sabio2024scoping]]: usage categories and BCI paradigms.
- [[song2022eeg]]: motor imagery and emotion benchmarks.
