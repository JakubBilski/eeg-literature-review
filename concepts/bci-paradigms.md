---
slug: bci-paradigms
fields: [eeg, neuro-clinical, ml]
familiarity: introduced     # human's level: new | introduced | understood | skip
---

# bci-paradigms

## Field-neutral description
A recipe for producing a brain signal that a classifier can reliably tell apart. Either the user does something mentally (imagines a movement), or the system shows a stimulus and detects the brain's response to it. The paradigm fixes the label space, the timing structure of the data and which signal features carry the information.

## Synonyms by community
- **EEG:** BCI paradigm, control signal, "technique used to obtain EEG data" [[varbu2022past]]; motor imagery (MI), SSVEP, P300 speller, ERP-based BCI, SMR-based BCI
- **Neuroscience / clinical:** experimental paradigm, evoked vs induced activity, event-related potential (ERP), event-related (de)synchronization (ERD/ERS)
- **Signal processing:** phase-locked (time-domain template) vs non-phase-locked (band-power) signal
- **General ML:** task / label definition; trial-based (epoch) classification vs continuous (streaming) detection

## The main paradigms (plain-language)
- **Motor imagery (MI) / sensorimotor rhythm (SMR):** the user imagines moving a hand, foot or tongue. This changes rhythmic activity over the motor cortex, the strip across the top of the head that controls the opposite side of the body. No stimulus is needed ("spontaneous"). Information is in **band power** over specific electrodes, which is why CSP + LDA was the standard pipeline [[varbu2022past]] (Table 1; §5.8). Benchmarks: BCI IV-2a/2b [[song2022eeg]].
  - **Imagined vs executed movement** (asked 2026-10-10):
    - **Shared, oscillatory part:** in both cases, mu (8–12 Hz) and beta (18–26 Hz) power drops (*desynchronizes*) over the sensorimotor cortex on the side opposite the limb. This happens "contralateral to an actual or imagined movement" [[lawhern2018eegnet]] (§2.1.4, p. 6). Imagery "activates the brain areas that are responsible for generating the actual movement" [[varbu2022past]] (Table 1). Conformer's maps of imagined left- vs right-hand movement show this contralateral pattern (ERD/ERS) [[song2022eeg]] (Fig. 9).
    - **Extra in execution:** the movement-related cortical potential (MRCP), a slow time-locked waveform. It has three parts: a slow 0–5 Hz *readiness potential* plus early 10–12 Hz desynchronization before onset, a *motor potential* at onset, and a 20–30 Hz rebound ~1 s after the movement [[lawhern2018eegnet]] (§2.1.3, p. 5). EEGNet treats MRCP as "ERP/Oscillatory" and SMR (imagery) as purely oscillatory (Table 1). The SMR "is very similar to the oscillatory component of the MRCP" (§2.1.4).
    - **Imagery is weaker:** SMR-based BCIs "tend to be weak and highly variable across and within subjects", and need user training and ~20 min calibration [[lawhern2018eegnet]] (§2.1.4).
    - 🤖 (general knowledge, no vault source) Execution also adds non-brain signal: muscle activity (EMG) and sensory feedback from the moving limb. A decoder of *executed* movement can partly read muscle artifacts, which is why imagery studies often check EMG to confirm the subject stayed still.
    - **Where to look:** electrodes C3 and C4, the "central" 10-20 sites roughly over the left and right hand areas of the motor cortex (naming → [[q2-measuring-devices]] *Montages*). A right-hand movement should change C3 (opposite side, *contralateral*) more than C4.
    - **Real data (own analysis, 2026-10-10):** `scripts/plot_motor_erd.py` on PhysioNet EEGMMI subjects 1–10, right-fist trials (~21 per run set per subject), common-average reference. Values are power change vs pre-cue rest, mean ± SEM over subjects, 0.5–3 s after the cue:
      ![[eegmmi-imagined-vs-executed.png]]
      | band | condition | C3 (contralateral) | C4 (ipsilateral) |
      |---|---|---|---|
      | mu 8–12 Hz | imagined | −20.5 ± 6.9% | −11.5 ± 2.9% |
      | mu 8–12 Hz | executed | −32.9 ± 6.8% | −31.0 ± 7.2% |
      | beta 16–26 Hz | imagined | −21.1 ± 5.2% | −10.9 ± 2.7% |
      | beta 16–26 Hz | executed | −29.8 ± 7.3% | −27.4 ± 6.3% |
      - Single raw trials show no visible difference. Only trial-averaged band power does.
      - **Execution gives a stronger drop** (~30% vs ~20% at C3), consistent with imagery being "weak" ([[lawhern2018eegnet]] §2.1.4).
      - **Imagery is lateralized and execution here is not:** for imagery C3 drops about twice as much as C4; for execution both sides drop about equally. 🤖 Possible reasons, not tested: real clenching adds bilateral sensory feedback and muscle activity; the common-average reference spreads strong local changes; 10 subjects, no statistical test.
      - 🤖 The power spike ~0.25 s after the cue in both conditions is most likely the visual response to the on-screen cue, not motor activity.
      - How "power vs rest" is computed (band-pass → Hilbert envelope → trial average → % of rest) → [[time-frequency-analysis]] *Band power over time and ERD%*.
    - **Single-trial decoding is possible but far from perfect.** On PhysioNet-MI, 4 *imagined* classes (left fist, right fist, both fists, feet), 64 channels, 4 s trials, with unseen test subjects (subjects 90–109): CBraMod 0.642 and EEGNet 0.581 balanced accuracy vs 0.25 chance [[wang2024cbramod]] (Table 3, p. 8; split §3). The models see all channels and learn spatial filters, which is far more than the single C3 trace in the figure.
      - **Own test, imagined vs executed (2026-10-10).** `scripts/classify_imagery_vs_execution.py`: CSP (6 components, shrinkage) + LDA on EEGMMI subjects 1–10, ~90 trials/subject (45 per class, left and right fist pooled), epochs 0.5–3.5 s after the cue. Accuracy, mean ± SEM over subjects, chance 0.50:
        ![[eegmmi-imagined-vs-executed-csp.png]]
        | band | shuffled 5-fold | by-block (leave one run pair out) | rest control (by-block) | cross-subject (LOSO) |
        |---|---|---|---|---|
        | 8–30 Hz (mu/beta) | 0.83 ± 0.03 | 0.64 ± 0.06 | 0.65 ± 0.06 | 0.56 ± 0.02 |
        | 30–75 Hz (muscle) | 0.88 ± 0.03 | 0.66 ± 0.05 | 0.57 ± 0.06 | 0.50 ± 0.02 |
        - **Shuffled CV is inflated.** Imagined and executed trials come from different runs, so shuffling lets the model learn "which recording". It drops from 0.83 to 0.64 when whole run pairs are held out. Per-subject by-block scores range from 0.39 to 0.86.
        - **The rest control scores as high as the task (0.65).** The same pipeline separates the *rest* periods of executed vs imagined runs, when nobody is doing anything. So most of the within-subject separability is recording-block differences, not the task. 🤖 Caveat: rest epochs start right after a trial, so a post-movement beta rebound after real clenching could make part of this genuine.
        - **The muscle band beats mu/beta under shuffling** (0.88): high-frequency, non-brain signal is the easiest cue.
        - **Cross-subject it is at chance** (0.56 / 0.50).
        - **The CSP patterns point at the wrong place:** subject 1's top components sit at the frontal/temporal edge (around AF7/AF8/F8), which is typical of eye and muscle artifacts, not over C3/C4.
        - 🤖 Conclusion: with CSP + LDA on this dataset there is no evidence of a usable, brain-based imagined-vs-executed decoder. The apparent 83% is a split artifact. This is a worked example for [[evaluation-protocols]] and [[q6-reliability-of-eeg-diagnoses]].
      - Imagined vs executed as a classification task in the literature: not covered in the vault.
      - Revisiting this with a pretrained encoder (contamination, better targets) → [[self-supervised-pretraining]] *EEGMMI as a frozen-embedding testbed*. 🤖 It is probably easier than telling imagined classes apart, because execution adds muscle artifacts and a stronger, bilateral ERD. But a classifier could succeed on the artifacts rather than the brain signal.
    - Data with both conditions: PhysioNet EEG Motor Movement/Imagery (109 subjects, 64 ch, both executed and imagined fists/feet) [[jiang2024large]] (App. D); [[wang2024cbramod]] uses its imagery part (§3, p. 8).
- **Visual evoked potentials:**
  - **SSVEP:** targets flicker at different frequencies, and looking at one makes visual cortex activity oscillate at that frequency. The system just finds the dominant frequency, typically with CCA [[varbu2022past]] (Table 1); [[song2022eeg]] (§I). It needs gaze, so it is a "dependent" BCI (Table 2).
  - **P300:** 🤖 a positive voltage bump ~300 ms after a rare, attended stimulus. A speller flashes rows and columns of letters, and the flash containing the wanted letter evokes it. An ERP, i.e. a **time-locked waveform**, detected by averaging or with a template classifier. EEGNet's P300 data is 2 classes with ~5.6:1 class imbalance [[lawhern2018eegnet]] (Table 1).
- **Error-related potential (ErrP/ERN):** an automatic response when the system does something the user didn't intend. Used to correct the BCI's errors [[varbu2022past]] (Table 1).
- **Auditory / vibrotactile evoked potentials:** the same idea with sounds or vibrations. Useful when vision is impaired; mostly medical [[varbu2022past]] (Fig. 11).
- **Imagined speech:** decoding imagined words. Rare (2/155 papers) [[varbu2022past]] (Fig. 11).
- **Passive BCI / monitoring:** no intentional control. Spectral changes are tracked to estimate drowsiness, attention, workload or emotion [[varbu2022past]] (Table 1). 🤖 This blurs into "cognitive state decoding". Whether it counts as BCI is a matter of definition.

## Taxonomies ([[varbu2022past]] §2, Tables 1–2)
| axis | poles | example |
|---|---|---|
| control | active vs passive | MI vs drowsiness monitoring |
| stimulus | evoked/exogenous vs spontaneous/endogenous | SSVEP vs MI |
| muscle use | dependent vs independent | SSVEP (gaze) vs P300 |
| timing | synchronous vs asynchronous | cue-paced trials vs always-on ("brain switch" needed) |

## Papers
- [[varbu2022past]]: the taxonomy plus frequencies in 202 BCI papers (2009–2019). MI 38, VEP 31, drowsiness/attention 29, emotion 15 (Fig. 11). MI is mostly medical (62%), VEP and monitoring mostly non-medical.
- [[song2022eeg]]: an MI decoder (BCI IV-2a/2b). Lists CSP/FBCSP for MI and CCA for SSVEP as the classical paradigm-specific pipelines (§I).
- [[niso2022wireless]]: control/communication with wireless EEG is SSVEP, MI and P300, mostly for games and robots, and only 10% of studies (§4.2.3).
- [[sabio2024scoping]]: BCI is the top use of consumer headsets (44.5%), with MI, SSVEP and P300 paradigms (§Research domains).
- [[lawhern2018eegnet]]: one compact CNN across four paradigms (P300, ERN, MRCP, SMR), i.e. a paradigm-agnostic model replacing paradigm-specific pipelines (Abstract, Table 1). *(not yet read in full)*

## Variants & disagreements
- **"BCI" scope:** [[varbu2022past]] includes passive monitoring (emotion, fatigue) as BCI, while narrower definitions require intentional real-time control. This changes all reported domain shares.
- **ERP vs oscillatory:** [[lawhern2018eegnet]] splits paradigms into ERP-based (P300, ERN, MRCP) and oscillatory (SMR). 🤖 This is the more useful split for ML: time-domain templates vs band-power features.

## Open questions
- How large is the within- vs cross-subject gap per paradigm? Varbu names subject-independent BCI as the key obstacle (§6.1). → [[evaluation-protocols]]
- Does a decoder trained on executed movement transfer to imagery, and how much weaker is imagery ERD than execution ERD? Not quantified in the vault. Pfurtscheller & Lopes da Silva 1999 (ERD/ERS basic principles) is the canonical source.
- What fraction of users can't produce a usable MI signal ("BCI illiteracy")? Not in the vault yet.

## Related concepts
- [[frequency-bands]]: MI and passive BCIs use band power (mu/beta over motor cortex; alpha/theta for drowsiness).
- [[evaluation-protocols]]: per-subject calibration vs subject-independent models.
- [[consumer-grade-eeg-devices]]: low-channel headsets constrain which paradigms work (no motor-cortex coverage on Muse).
- [[riemannian-methods]]: covariance-based classifiers, a classical alternative to CSP + LDA.
