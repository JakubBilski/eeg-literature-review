---
slug: emotion-recognition
fields: [eeg, neuro-clinical, ml]
familiarity: introduced     # human's level: new | introduced | understood | skip
---

# emotion-recognition

## Field-neutral description
Predict a person's momentary affective state, either a category (happy, sad, fear, ...) or a position on continuous scales (pleasant↔unpleasant, calm↔excited), from a physiological recording made while they are exposed to emotion-provoking material. The ground truth is usually the stimulus category or the person's own rating afterwards.

## Synonyms by community
- **EEG:** EEG emotion recognition, affective BCI (aBCI), passive BCI / monitoring
- **Neuroscience / clinical:** affective neuroscience; valence/arousal; frontal alpha asymmetry (approach/withdrawal)
- **Signal processing:** —
- **General ML:** affective computing, sentiment/affect classification, multimodal emotion recognition

## How the task is set up
- **Labels** [[li2022eeg]] (§2.1, p. 3):
  - *discrete* categories (Ekman 6, Plutchik 8);
  - *continuous* valence × arousal (× dominance), rated per trial on the 1–9 Self-Assessment Manikin scale and often thresholded into high/low classes.
  - SEED-family labels are the intended emotion of the film clip (design labels), not a per-person rating (§5.1) → [[eeg-labels-and-metadata]].
- **Stimuli:** pictures (IAPS), film or music clips, sounds, VR, or recalling past experiences. One self-report follows each trial [[li2022eeg]] (§2.3, p. 5).
- **Datasets:**
  - DEAP (32 subjects, 32 ch, 40 one-minute music videos), SEED (15 subjects, 62 ch, 15 film clips × 3 sessions), SEED-IV, DREAMER (consumer 14-ch Emotiv), MAHNOB-HCI, MPED [[li2022eeg]] (Table 3).
  - Larger and newer: FACED (123 subjects, 32 ch, 9 classes) and SEED-V (16 subjects, 5 classes) [[wang2024cbramod]] (§4, p. 6).
- **Features:** band power and differential entropy (DE ≈ log band power) per band and channel, hemispheric asymmetry, connectivity. β and γ bands carry most information, but all bands combined work best [[li2022eeg]] (§2.2, §3.5).

## What the physiology says (and doesn't)
- Frontal alpha asymmetry: relatively more left-frontal activity for positive/"approach" states, more right for negative/"withdrawal" states. Other studies find a beta-2 effect instead [[li2022eeg]] (§2.2, p. 4).
- Intracranial evidence favours a distributed view: no single region handles any one emotion. Localizing sources from scalp EEG "is problematic" (p. 4). The review concludes the neural specificity is "not yet fully explored and understood" (p. 4).
- 🤖 Plain-language reading: EEG has no agreed marker of "sadness" in the way it has one for N2 sleep (spindles) or a seizure. Models learn whatever separates the classes in a given dataset.

## How well does it work?
| setting | number | source |
|---|---|---|
| within-subject, DEAP 2-class | up to ~98% | [[li2022eeg]] Table 4 (MLF-CapsNet) |
| same model, within vs cross-subject, SEED 3-class | 90.4% → 79.95% (DGCNN); 94.24% → 85.30% (RGNN) | [[li2022eeg]] Table 4 |
| same model, within vs cross-subject, DEAP valence | 94.38% → 68.14% (BiDCNN) | [[li2022eeg]] Table 4 |
| held-out subjects, FACED 9-class (123 subjects) | bal. acc. 0.41 (EEGNet) → 0.55 (CBraMod); chance ≈ 0.11 | [[wang2024cbramod]] Table 2 |
| SEED-V 5-class, trial split, subjects pooled | bal. acc. 0.30 (EEGNet) → 0.41 (CBraMod); chance 0.20 | [[wang2024cbramod]] Table 2; [[jiang2024large]] Table 6 |
| 5-fold CV over 1 s windows, SEED, within session | 95.30% | [[song2022eeg]] Table IV (leaky split 🤖) |

- 🤖 The spread is mostly due to protocol, not model. Pooled windows and within-subject splits give 0.9+, while held-out subjects on a large dataset give about 0.5 on 9 classes. That is well above chance, but far from usable as a per-person emotion readout.

## Variants & disagreements
- **Is it emotion or the stimulus?** 🤖 With few clips (SEED: 15) and labels tied to the clip, a model can win by recognising *which clip* is playing (visual/auditory evoked activity, eye movements) rather than the felt emotion. No vault paper tests this.
- **Is it brain or muscle?** 🤖 The most informative bands (β, γ to 45 Hz) overlap the EMG range (>30 Hz) given in [[li2022eeg]] (§3.1). Facial expressions and jaw tension during emotional clips could drive temporal and frontal γ. [[li2022eeg]] doesn't discuss this.
- **User-independent models feasible?** AlZoubi et al. said no; most later work tries domain adaptation instead [[li2022eeg]] (§4.5) → [[domain-adaptation]].

## Papers
- [[li2022eeg]]: tutorial review covering labels, physiology, features, DL routes, domain adaptation, datasets, and the split taxonomy (segment k-fold = leakage).
- [[song2022eeg]]: EEG Conformer on SEED, within-session 5-fold over 1 s windows (95.30%).
- [[jiang2024large]]: LaBraM on SEED-V (5-class, subjects pooled, trial split); SEED-family data is also in pretraining.
- [[wang2024cbramod]]: CBraMod on FACED (held-out subjects) and SEED-V; the most honest numbers in the vault so far.
- [[varbu2022past]]: emotion = 15 of 202 BCI papers, 93% non-medical (Fig. 11).
- [[chaddad2023electroencephalography]]: lists DEAP and SEED as the standard emotion datasets (Table 3).
- [[roy2019deep]]: emotion is the largest monitoring domain of 2010–2018 (17 papers; DEAP 9, SEED 3; Table 6). Noise augmentation on SEED raised LeNet 49.6% → 74.3%, merely matching an SVM at 74.2% (p. 14).
- [[weng2025self]]: emotion labels from self-report or stimulus type "may introduce significant bias", a stated motivation for SSL (§7, p. 27). Emotion-specific SSL uses spatial / graph contrast (GMSS) and "meiosis": swapping channel halves between two trials of the same stimulus (§5.3).

## Open questions
- Has anyone tested whether SEED/DEAP models decode the clip rather than the emotion (e.g. train on clip identity, or test on new clips)?
- How much of the emotion signal survives EMG removal or restricting to <30 Hz?
- Is there a 2022+ cross-dataset emotion benchmark (train on SEED, test on DEAP/FACED)?

## Related concepts
- [[eeg-labels-and-metadata]]: self-report and design labels.
- [[domain-adaptation]]: cross-subject shift is the main obstacle.
- [[evaluation-protocols]]: segment-level splits inflate emotion results.
- [[frequency-bands]], [[bci-paradigms]] (emotion as passive BCI).
- [[eeg-depression-detection]]: 🤖 a similar pattern of subtle target, small single-site data and high reported accuracy; [[li2022eeg]] also lists depression diagnosis as an application (§1).
