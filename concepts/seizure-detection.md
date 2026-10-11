---
slug: seizure-detection
fields: [eeg, neuro-clinical, ml]
familiarity: introduced     # human's level: new | introduced | understood | skip
---

# seizure-detection

## Field-neutral description
A long multichannel recording contains rare, brief episodes of abnormal activity. The task is either to flag an episode while it is happening (detection) or to raise an alarm some minutes before one starts (prediction), with as few false alarms as possible.

## Synonyms by community
- **EEG:** seizure detection, seizure onset detection, seizure prediction / forecasting; *ictal* (during a seizure), *preictal* (the period before), *interictal* (between seizures), *postictal* (after)
- **Neuroscience / clinical:** epilepsy monitoring (EMU = epilepsy monitoring unit, usually video-EEG), seizure onset zone / epileptogenic zone (the brain area where seizures start), spikes / epileptiform discharges (brief abnormal waves between seizures; not the same as seizures)
- **Signal processing:** event / change-point detection in non-stationary signals
- **General ML:** rare-event detection, highly imbalanced binary classification, anomaly detection; prediction ≈ early-warning time-series classification

## Basics (physiology) 🤖
*Textbook background, not yet sourced to a vault paper except where cited.*
- A seizure is a burst of abnormally synchronised firing in a population of neurons. On EEG it usually looks like a rhythmic discharge that evolves in frequency and amplitude, and it is large compared with background activity.
- **Epilepsy** is the tendency to have repeated unprovoked seizures. Diagnosis rests on EEG: it is "the most common diagnostic investigation for patients with suspected seizures or epilepsy" [[wong2023eeg]] (§1).
- **Focal vs generalised:** focal seizures start in one area and may show on only a few electrodes; generalised ones involve both hemispheres from the start. This is why channel coverage matters.
- **Scalp vs intracranial:** scalp EEG is cheap and non-invasive but "less sensitive" and noisier. Intracranial EEG uses electrodes implanted on the cortex: higher SNR, fewer artifacts, but invasive [[wong2023eeg]] (§2, §7) → [[electrode-types]].

## What a seizure looks like (own plot, CHB-MIT chb01_03)
![[chbmit-seizure-chb01_03.png]]
*Made with `scripts/plot_seizure.py` from PhysioNet CHB-MIT patient chb01, file chb01_03.edf. The expert-annotated seizure runs 2996–3036 s (chb01-summary.txt). The 18 traces are bipolar channels (voltage differences between neighbouring electrodes, e.g. FP1-F3), filtered 0.5–40 Hz. Below: spectrogram of FP1-F3, the channel with the most seizure power. 2026-10-11.*

What to see (own analysis; readings marked 🤖 are my interpretation):
- **Amplitude jumps on every channel.** Seizure-period SD is 110–128 µV on the top channels, against a median of 30 µV before onset: about 8–20× the power (script output). This is why seizures are among the easiest EEG events to detect.
- **It's a rhythm, not just noise.** The traces become regular, repeating waves, and power concentrates below ~6 Hz in the spectrogram. 🤖 The dominant frequency appears to drift lower as the seizure goes on, the classic "evolution" in frequency and amplitude.
- **Onset and offset are blurry.** The change at 2996 s starts small, with the big waves only from ~3000 s. Rhythmic slow activity continues after the annotated end at 3036 s. 🤖 So the exact seizure boundaries are a judgement call, a source of label noise (see *Open questions*).
- 🤖 **The background isn't clean either.** Before the seizure, the frontal channels (FP1-F3, FP2-F4) show bursts with repeating ~12 Hz energy, possibly muscle or a sleep rhythm. A constant line at ~16 Hz in the spectrogram looks like technical interference. A detector has to ignore all of this.
- 🤖 **Involves both hemispheres here.** The changes appear on left (odd numbers) and right (even numbers) channels alike. That is one patient; focal seizures can show on only a few channels.

## Detection vs prediction
- **Detection** needs ictal + interictal data. **Prediction** needs preictal + interictal data; some datasets only support one of the two [[wong2023eeg]] (§5.5, Table 4).
- The preictal window is a convention, not something the EEG defines. Kaggle prediction challenges use 5 min before onset, with interictal ≥1 week (AES) or ≥3–4 h (Melbourne) from any seizure [[wong2023eeg]] (Table 4).
- Seizure risk follows daily (circadian) and multi-day cycles. Using time of day helped forecasting on long-term implanted recordings (NeuroVista) [[wong2023eeg]] (§7).

## Public datasets (as of 2023)
| dataset | signal | subjects | notes | source |
|---|---|---|---|---|
| Bonn | 1-ch scalp (healthy) + intracranial (patients) | 10 | most used (58/120 studies); 500 × 23.6 s pre-cut, balanced, no patient IDs | [[wong2023eeg]] Tables 2, 5, 8, A1 |
| CHB-MIT | scalp, 18 ch, 256 Hz | 23 children | 198 seizures; recordings after anti-seizure medication withdrawal | [[wong2023eeg]] Table 8; [[wang2024cbramod]] App. E.2 |
| TUSZ | scalp, 23–31 ch, ≥250 Hz | 592–642 | 3,050 seizures; richest metadata | [[wong2023eeg]] Tables 5–6, 8 |
| Helsinki | scalp, 19 ch, 256 Hz | 79 neonates | 460 seizures, ~74 min each | [[wong2023eeg]] Table 8 |
| Siena | scalp, 29 ch, 512 Hz | 14 | 47 seizures; seizure type and onset area | [[wong2023eeg]] Tables 6, 8 |
| Kaggle / NeuroVista | intracranial, 16 ch | 3–12 (some dogs) | competition segments; Melbourne and NeuroVista overlap | [[wong2023eeg]] §7 |

## Papers
- [[wong2023eeg]]: catalogue of 10 public datasets and how their properties (channels, continuity, balance, patient IDs) constrain methods.
- [[wang2024cbramod]]: CHB-MIT as a foundation-model benchmark. 16 bipolar channels, 10 s windows, train on subjects 1–19, test on 22–23. Balanced accuracy EEGNet 0.566 → CBraMod 0.740; AUC-PR 0.19 → 0.37 (App. E.2, Table 8).
- [[jiang2024large]]: TUSZ is the largest single source of LaBraM's pretraining data, 1,138.5 of 2,535 h (App. D).
- [[chaddad2023electroencephalography]]: lists Bonn, CHB-MIT and Siena as standard datasets; quotes "CNN 98%" seizure detection (Tables 3, 6).
- [[niso2022wireless]]: at-home seizure monitoring is a main clinical use of wireless EEG (§4.2.2).
- [[roy2019deep]]: epilepsy is the largest clinical DL domain of 2010–2018 (26 papers, 21 detection). CHB-MIT (9) and Bonn (7) were already the top datasets (Fig. 4, Table 6). Raw-EEG CNNs beat SVMs on frequency features (p. 27). Going from 4 to 22 channels raised specificity from 40% to 90% (ref [153], p. 13).
- [[kuruppu2026eeg]]: asks FM papers to report clinically meaningful metrics such as false positives per hour and to keep the natural interictal ≫ ictal imbalance (§5.2, p. 18). In BrainWave's paper, a general time-series FM (MOMENT) beat EEG-FMs on seizure detection (p. 17).
- [[weng2025self]]: SSL seizure methods include MBrain (channel-correlation prediction + CPC), Wavelet2vec (per-band masked reconstruction, seizure subtypes), EEG-CGS (graph anomaly detection) and BrainNet (SEEG) (Tables 1–3). No performance comparison.
- [[liu2026eeg]]: CHB-MIT as ictal vs 10-min pre-ictal segment classification, not continuous detection. Few-shot (first seizure only): Conformer 91.58, CBraMod 88.54, PSD+SVM 77.71. LOSO: ShallowConv 80.18 vs best FM LUNA 78.12 (Tables 2, 15).

## Variants & disagreements
- **Segment vs event metrics.** Window-level accuracy on balanced pre-cut segments (Bonn) is not comparable to event-level sensitivity with false alarms per hour on continuous recordings. 🤖 Clinically, false alarms per hour is what decides usability; the vault has no source for it yet.
- **Patient-specific vs general models:** ML work often trains one model per patient because seizure patterns are patient-specific, unlike the clinical habit of grouping by seizure type [[wong2023eeg]] (§2).

## Open questions
- How often do human experts agree on seizure onset and offset (inter-rater κ)? [[wong2023eeg]] doesn't cover it. Needed to judge label noise, as for [[sleep-staging]].
- What do clinically deployed detectors achieve (sensitivity, false alarms/h) on continuous multi-site data? Need a 2022+ evaluation paper.
- 🤖 CBraMod's CHB-MIT test set is 2 children. How much would the ranking change with leave-one-subject-out?

## Related concepts
- [[sleep-staging]]: the other clinical task with expert labels and heavy imbalance
- [[evaluation-protocols]]: patient IDs, leakage, imbalance
- [[channel-heterogeneity]]: datasets differ in channels, montage and sampling rate
- [[electrode-types]]: scalp vs intracranial
