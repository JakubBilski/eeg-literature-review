---
slug: sleep-staging
fields: [eeg, neuro-clinical, ml]
familiarity: introduced     # human's level: new | introduced | understood | skip
---

# sleep-staging

## Field-neutral description
A night of recording is cut into fixed-length windows, and each window is labelled with one of a few states that alternate over the night. The labels follow a written rulebook applied by trained human scorers, and the sequence of states summarizes how someone slept.

## Synonyms by community
- **EEG:** sleep staging, sleep scoring, hypnogram (the stage-over-time plot), AASM stages Wake / N1 / N2 / N3 / REM (older R&K rules: S1–S4, with S3+S4 = today's N3)
- **Neuroscience / clinical:** polysomnography (PSG) scoring, sleep architecture, slow-wave sleep (= N3), light sleep (N1+N2), deep sleep (N3)
- **Signal processing:** —
- **General ML:** sequence labelling / multi-class time-series classification over 30 s epochs; imbalanced classes

## What the stages look like 🤖
*Standard textbook description; not yet sourced to a vault paper.*
- **Wake:** eyes closed and relaxed, the EEG shows alpha (8–12 Hz) at the back of the head → [[frequency-bands]].
- **N1 (drowsy transition):** alpha fades into slower theta. It is short, rare, and looks like both wake and N2, which is why every scorer and device does worst on it.
- **N2:** bursts of sleep spindles (≈12–14 Hz, ~1 s) and K-complexes (single large slow waves). It takes up most of the night.
- **N3 (deep / slow-wave sleep):** large delta waves (<2 Hz) dominate.
- **REM:** the EEG looks almost awake, but the eyes make rapid movements and the body muscles go slack. EEG alone barely separates REM from wake/N1, so PSG adds eye (EOG) and chin muscle (EMG) channels.

## PSG, the reference recording
- Polysomnography (PSG) is an overnight sleep-lab recording. It combines EEG, eye (EOG) and chin-muscle (EMG) channels with "several cardio-respiratory domains" [[gans2024sleep]] (p. 1).
- It is the "reference standard" for sleep stages, but it needs specialised equipment, is uncomfortable, labour-intensive and expensive, so it isn't used routinely (pp. 1–2).
- 🤖 The cardio-respiratory channels (airflow, chest/abdomen effort, blood oxygen, ECG) serve mainly to diagnose breathing disorders such as sleep apnea. The stages themselves are scored from EEG + EOG + EMG.
- The cheap alternative, wrist actigraphy, infers sleep from lack of movement. It can't stage sleep and scores lying still as sleep (p. 2).

## How clearly are the stages defined? (asked 2026-10-11)
- **On paper, yes: there is a written rulebook.** The AASM scoring manual (Iber et al. 2007) labels each 30 s epoch as Wake, N1, N2, N3 or REM [[wang2024cbramod]] (App. E.1, p. 23). 🤖 It replaced the older Rechtschaffen & Kales (R&K) rules (both are still in use per [[lee2021interrater]], Abstract), and some devices still follow R&K: QUISI reports "N3/N4" [[gans2024sleep]] (Table 1, p. 6).
- 🤖 **The rules are visual thresholds applied by eye.** *(Paraphrased from the AASM manual, which is not in the vault.)*
  - An epoch takes the stage that fills most of it.
  - N3 = slow waves (0.5–2 Hz, >75 µV peak-to-peak) for ≥20% of the epoch.
  - N2 = spindles or K-complexes.
  - N1 = alpha replaced by low-amplitude 4–7 Hz activity.
  - Context rules carry a stage forward until a new feature appears. This is why experts look at neighbouring epochs, and why models are run on sequences ([[wang2024cbramod]] p. 23).
- 🤖 **The stages are defined by the recording itself (asked 2026-10-11).** N1–N3 are defined purely by EEG patterns, plus slow rolling eye movements (EOG) at sleep onset. REM is defined by EEG + EOG + chin EMG. There is no independent ground truth: a stage *is* "the recording looks like this".
  - Other physiology changes with the stages (harder to wake from N3, vivid dreaming in REM, heart rate and breathing), but none of it is used in the definition. Historically, the stages were *discovered* in EEG and EOG recordings.
  - **For ML:** the label is a human-applied rule over the input signal. A model is learning to imitate the scorer's reading of the rules, not to detect a hidden brain state. That fits the ceiling above: you can't beat the rule's own ambiguity.
  - **Electrode placement matters:** the rules were written for specific scalp sites. ISRUC uses F3/C3/O1 referenced to the opposite mastoid ([[wang2024cbramod]] p. 23), because alpha is strongest at the back of the head and spindles/K-complexes centrally and frontally. A forehead or ear device sees these features weakly and has to infer the stage from a different view of the same activity. Frontal electrodes do pick up eye movements well, which may be why REM works on forehead devices (see Open questions).
- 🤖 **The underlying process is continuous.** Falling asleep and deepening sleep are gradual. The rules cut a continuum into boxes at amplitude, duration and percentage thresholds, so epochs near a boundary are ambiguous by construction.
- **In practice, agreement depends on the stage.** Pooled κ between human scorers is 0.76 overall: Wake 0.70, N1 0.24, N2 0.57, N3 0.57, REM 0.69 [[lee2021interrater]] (Abstract). N1 is only "fair"; N2 and N3 are "moderate", which is mostly the N2/N3 boundary, i.e. the 20% slow-wave threshold 🤖.
- 🤖 **Consequence for ML and devices:** a κ around 0.75 against one scorer is roughly human-level. Devices (κ 0.42–0.79, [[gans2024sleep]] Table 1) and models (κ 0.70–0.74 on ISRUC, [[wang2024cbramod]] Table 7) are already in that range, so further gains on such benchmarks partly measure fitting one scorer's habits.

## Diagnostic use of the stages (asked 2026-10-11)
- **In the vault:** the diagnostic uses visible in [[gans2024sleep]] all concern **REM** (from cited titles, refs [41], [50], [71], pp. 11–12).
  - A home Sleep Profiler vs lab PSG for diagnosing REM sleep behaviour disorder (RBD).
  - Home detection of "REM sleep without atonia" with a soft electrode array.
  - A two-channel device that "can detect REM sleep behavioral disorder" in Parkinson's.
  - Otherwise, the validation populations are insomnia, sleep apnea, psychiatric and surgical patients, but the stages serve to describe their sleep, not to diagnose them (Table 1).
- 🤖 **Textbook picture (not yet sourced):** the amounts of N1/N2/N3 rarely diagnose anything on their own. The diagnostic weight sits elsewhere:
  - **REM timing and quality:**
    - Narcolepsy: REM appearing within minutes of falling asleep, measured in daytime nap tests.
    - RBD: REM without the normal muscle paralysis, so people act out dreams. It is an early warning sign of Parkinson's and related diseases.
  - **Sleep vs wake only:** sleep onset latency, sleep efficiency and wake after sleep onset, for insomnia and for timing.
  - **Non-EEG channels:** sleep apnea is diagnosed from breathing and oxygen, with staging needed mainly for total sleep time (the denominator of the apnea–hypopnea index).
  - **N3 matters indirectly:**
    - Sleepwalking and night terrors arise out of N3. They are diagnosed mostly from history and video, with N3 as context.
    - Too much N1 and frequent stage shifts signal fragmented sleep, but that is non-specific.
  - **Research biomarkers inside the stages, not in clinical use:**
    - Fewer sleep spindles (N2) in schizophrenia.
    - Less slow-wave activity (N3) with ageing and Alzheimer's.
    - Shortened time to first REM in depression.
- **Conclusion (human, 2026-10-11):** N1/N2/N3 as categories are rarely used for anything diagnostic.
- 🤖 **Summary:** the hypnogram is mostly *descriptive* ("sleep architecture"). Clinically it is a scaffold for other measurements. The diagnostic signal is in REM, in sleep/wake timing, and in features *within* stages (spindles, slow waves), more than in N1/N2/N3 percentages.

## Papers
- [[gans2024sleep]]: systematic review of 34 EEG wearables validated against PSG.
  - 70% of the validated devices give 5 stages, the rest light/deep only (§3).
  - Per-stage sensitivity is 0.11–0.98, worst for N1 (§3). Overall κ is 0.42–0.79 where reported (Table 1).
  - κ is the recommended metric because classes are unbalanced (p. 10).
  - Manual PSG scoring varies with the technician, and there is no agreed standard for automatic scoring (p. 10).
- [[wang2024cbramod]]: ISRUC benchmark: 100 adults, 6 PSG EEG channels, 200 Hz, 89,240 30-second epochs, 5 AASM classes; subjects 1–80 train / 81–90 val / 91–100 test (App. E.1, pp. 22–23).
  - Experts use the transition context between epochs, so models are run as sequence-to-sequence: 20 epochs per sequence, with a transformer on top of each encoder (p. 23).
  - κ: EEGNet 0.704, USleep 0.721, LaBraM 0.723, CBraMod 0.744 (Table 7).
- [[lee2021interrater]]: meta-analysis of human inter-scorer agreement. κ 0.76 overall, 0.24 on N1 (Abstract).
- [[roy2019deep]]: sleep staging is among the main DL-for-EEG tasks. Manual scoring "requires a lot of time" from trained technicians (p. 2). "Transitional sleep stages (e.g. S1 and S3) often lead to … unbalanced classes" (p. 14).
- [[chaddad2023electroencephalography]]: CNN+RNN reaches 79.7% on Fp1/Fp2 sleep staging (§2.5.2); Sleep-EDF is the listed sleep dataset (Table 3).
- [[niso2022wireless]]: at-home sleep staging is one of the main clinical uses of wireless EEG (§4.2.2).
- [[weng2025self]]: sleep is the most common SSL-EEG downstream task (15 of 34 contrastive methods, Table 3), favoured because sleep sets are long, few-channel recordings (p. 28). Relative positioning and CPC exploit slow stage changes (§3.2).
- [[chen2026benchmarking]]: sleep is the bipolar block of EEG-Arena (CAP, HMC, UCDDB). BIOT and SleepFM lead it, and SleepEEGNet is the strongest baseline, with the most top-5 placings overall (Fig. 2). Several UCDDB and CAP 4-s tasks are won by baselines (Fig. 3).

## Why is 5-class staging a benchmark at all? (asked 2026-10-11)
The human's objection: expert agreement is poor (N1 κ 0.24, N2/N3 0.57 [[lee2021interrater]]), the label is not grounded in brain function (it is a rule over the signal itself), and the stages are rarely used diagnostically (above). So why benchmark on it?
- **Why it is used:**
  - **Labels come for free.** Every clinical PSG is scored by a technician anyway, which yields large labelled archives: ISRUC (100 nights) [[wang2024cbramod]] (App. E.1), Sleep-EDF [[chaddad2023electroencephalography]] (Table 3). 🤖 SHHS and MASS are other large ones.
  - **There's a real workload to automate.** Manual scoring "requires a lot of time" from trained technicians [[roy2019deep]] (p. 2). Automatic scoring would save that, but there's no agreed standard for it yet [[gans2024sleep]] (p. 10).
  - **The rules are standardized.** The AASM manual makes labels comparable across labs, unlike most EEG tasks [[wang2024cbramod]] (p. 23).
  - **Overall agreement is decent.** κ 0.76 is "substantial" [[lee2021interrater]], because the big classes (Wake, N2, REM) dominate.
  - 🤖 **Inertia:** an established task with public baselines (DeepSleepNet, USleep) is easy to report on in a foundation-model paper.
- 🤖 **What it actually measures:** imitation of one scorer's rule-following, with a ceiling around κ 0.75. Models are already at κ 0.70–0.74 on ISRUC ([[wang2024cbramod]] Table 7), so differences between models are small relative to the label noise. As a test of whether a representation captures brain state, it is weak.
- 🤖 **Better-grounded alternatives** (to source):
  - REM vs non-REM, and sleep vs wake (higher agreement; clinically used).
  - Detecting RBD (REM without atonia).
  - Predicting outcomes or diagnoses from a whole night, which [[wang2024cbramod]] cites as a combined task ("Lpsgm: … sleep staging and mental disorder diagnosis").
  - Scoring with soft labels or several scorers, to measure the model against the spread between humans rather than one hypnogram.

- [[bomatter2025limited]]: PhysioNet 2018 sleep (6 EEG channels, single 30-s epochs) as the one task where data per person matters as much as the number of people (Fig. 3). PhaseRandomisation augmentation hurts small models here because it destroys waveform shapes such as K-complexes (§4.3).
- [[xie2026specbram]]: ISRUC/HMC sleep staging as the main probe task. Hand-crafted 5-band power ≈ FM frozen features (Table 5); fine-tuned SOTA 0.811 BA on ISRUC (Table 6). Comparison noise: std over 3 pretraining seeds is 0.002–0.008, but there's no CI over test subjects.

## Do people matter in sleep staging? (asked 2026-10-12)
*The human's claim: sleep staging is the task where the number of distinct people should matter least.*
- **The evidence agrees.**
  - [[bomatter2025limited]] (Fig. 3, TCN, PhysioNet 2018): 25 people × 640 epochs reach the same accuracy as 400 people × 5 epochs (0.66). On TUAB and dementia (CAUEEG), extra data per person adds ~nothing and people dominate.
  - [[oliveira2026scaling]]: ISRUC sleep is the one dataset where the per-trial term dominated for most models (p. 6), while TUAB/NMT are subject-dominated (Table 2).
  - People still help a little in sleep: at a fixed 8,000 epochs, 25 → 50 people gives +4 accuracy points, then it is flat up to 800 ([[bomatter2025limited]] Fig. 3).
- 🤖 **Why:**
  - *Every night contains every label.* One person gives all five stages, so each extra epoch is a new labelled example of some class. In one-label-per-person tasks (abnormal, dementia), extra segments repeat the same label, so the number of independent labels *is* the number of people.
  - *The label is a person-independent rule over the signal.* The stage contrasts (alpha vs theta vs spindles vs delta, see *What the stages look like*) are large compared with individual differences, and scorers apply the same thresholds to everyone.
  - *What still varies by person* (from memory, to source): slow-wave amplitude falls with age, so fewer epochs cross the 75 µV N3 threshold; individual spindle and alpha frequencies; medication; sleep disorders. That is why people still add a few points, and why an older, sicker cohort (e.g. SHHS) may show more person effect than PhysioNet 2018.
- **Consequence for experiments:** sleep is the weakest task for testing whether the number of people gates model capacity. Use it as the contrast, not the main test → [[subject-diversity-gap]] *After reading Bomatter & Gouk*.

## Variants & disagreements
- **5 vs 4 stages:** many consumer devices merge N1+N2 into "light" (Zeo, Neuroon, Umind, Zmachine, LANMAO) [[gans2024sleep]] (Table 1). Scores on 4-class and 5-class outputs are not comparable.
- **Reference labels are noisy:** the "ground truth" is one human scorer's hypnogram. Two human scorers agree at κ 0.76 overall and 0.24 on N1 [[lee2021interrater]] (Abstract). See *How clearly are the stages defined?* above.
- **Metric:** accuracy vs κ vs per-stage sensitivity vs duration correlation. Only κ (or balanced accuracy/macro-F1) is meaningful with the imbalanced stage distribution [[gans2024sleep]] (p. 10).

## Open questions
- Is per-stage human κ worse with patients (e.g. apnea, Parkinson's) than with healthy sleepers? [[lee2021interrater]] extracted underlying diseases, so the full text may say.
- Are sleep micro-features (spindle density, slow-wave activity) reliable diagnostic biomarkers across sites, e.g. for schizophrenia, Alzheimer's or depression? No source yet. Needs a 2022+ review (reading queue).
- Does a foundation model pretrained on clinical scalp EEG transfer to a single forehead or ear channel?
- 🤖 Why is REM detectable from forehead devices at all? Probably via eye-movement artifacts picked up by frontal electrodes. To check.

## Related concepts
- [[seizure-detection]]: the other clinical task with expert labels and heavy class imbalance
- [[frequency-bands]]: stages are defined largely by which bands dominate (alpha, theta, spindles, delta).
- [[consumer-grade-eeg-devices]]: sleep headbands are a large consumer category.
- [[evaluation-protocols]]: device validation against a simultaneous reference; κ for imbalanced classes.
- [[eeg-labels-and-metadata]]: sleep stages are expert labels per 30 s window.
