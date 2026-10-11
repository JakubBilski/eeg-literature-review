---
citekey: varbu2022past
title: "Past, Present, and Future of EEG-Based BCI Applications"
authors: [Kaido Värbu, Naveed Muhammad, Yar Muhammad]
year: 2022
venue: "Sensors 22(9):3331"
doi: "10.3390/s22093331"
arxiv: ""
pmid: "35591021"
field: eeg
paper_type: review
task: "systematic review (PRISMA): EEG-based BCI applications 2009–2019, 202 publications"
datasets: []
n_subjects: ""
n_channels: "1–163 across reviewed studies; 64% use 1–20 (Fig. 10)"
model_type: ""
eval_protocol: ""
main_metric: ""
main_result: "202 papers: non-medical 58% / medical 31% / both 11% (Fig. 5); motor imagery 38, VEP 31, drowsiness/attention 29 papers (Fig. 11); LDA 31% + SVM 21% of classifiers, CNN 4% (Fig. 13); Emotiv EPOC 40% of devices (Fig. 9)"
code_available: ""
read_depth: full
concepts: [bci-paradigms, consumer-grade-eeg-devices, electrode-types, frequency-bands, evaluation-protocols, independent-component-analysis, time-frequency-analysis, common-spatial-patterns, digital-filtering, eeg-preprocessing-pipeline, linear-discriminant-analysis]
---

# Past, Present, and Future of EEG-Based BCI Applications (Värbu et al., 2022)

## TL;DR
A PRISMA systematic review of 202 EEG-BCI application papers from 2009–2019. It gives a vocabulary for BCI types (active/passive, evoked/spontaneous, sync/async) and counts which paradigms, devices, features and classifiers were used. The picture is of the **pre-deep-learning era**: PSD/FFT/CSP features with LDA/SVM, and Emotiv as the most common device.

*Published 2022 but the literature stops in Oct 2019. Appendix B (Table A1) lists ~170 later titles (Oct 2019–Jun 2021) without analysing them. Figures 9–13 are images, transcribed at the end of `fulltext/varbu2022past.md`.*

## Research question
Five objectives (§3, p. 6): publication trends; techniques for obtaining EEG data, plus features and classifiers; devices and channel counts; split between medical and non-medical domains; geography.

## Data & preprocessing
- **Search:** PubMed, Web of Science, Scopus, 20–30 Oct 2019. Query: ("EEG based" OR "electroencephalography based") AND (BCI / brain–computer / brain–machine interface) AND "application(s)" (App. A).
  - Hits: PubMed 185, WoS 451, Scopus 569 → 635 after selection → 233 after title/abstract screening → **202 included** (§4.2, Fig. 1).
- **Eligibility:** 2009–2019, peer-reviewed, English; no abstracts, chapters or theses. Screening was done **by one person** (§4.2).
- 25 data items were extracted per paper (§4.1). The review comes from the first author's master's thesis (§1).

## Method
- **BCI definition:** a system that translates brain-activity patterns into commands, independent of the normal muscle pathways (§2). Pipeline: raw EEG → preprocessing → feature extraction → classification (§2, after Padfield 2019).
- **Taxonomies** (§2, Tables 1–2) → [[bci-paradigms]]:
  - **active** (motor imagery; visual/auditory/vibrotactile evoked potentials; imagined speech; error-related potential) vs **passive** (spectral monitoring of drowsiness, attention, workload, emotion) (Table 1);
  - **dependent** (needs muscle control, e.g. gaze for VEP) vs **independent** (e.g. P300) (Table 2);
  - **evoked/exogenous** (needs an external stimulus) vs **spontaneous/endogenous** (e.g. motor imagery) (Table 2);
  - **synchronous** (fixed command windows) vs **asynchronous** (always listening) (Table 2).
- **Domains:** "medical" = assist, monitor, assess or rehabilitate patients; "non-medical" = entertainment, machine control, authentication, monitoring of healthy users (§1, after Al-Nafjan 2017).

## Evaluation
- Descriptive counts only; no quality appraisal or risk-of-bias assessment. Accuracy is not compared across studies.

## Results (with locations)
- **Volume:** 11–15 papers/yr in 2009–2011, up to 32 in 2017 (§5.1, Fig. 2). 58% conference papers, 42% journal articles (§5.1).
- **Geography:** Asia 111 (China 39), Europe 56, North America 27 (USA 23), none from Africa (§5.2).
- **Domains:** non-medical 99 (58%), medical 53 (31%), both 19 (11%) (§5.4, Fig. 5).
  - Medical: assistive 74% (robot arms, prostheses, wheelchairs), rehabilitation 9% (mainly stroke), monitoring 9% (§5.4, Fig. 6).
  - Non-medical: monitoring 50% (fatigue, emotion, meditation), machine control 17% (smart home, robots), entertainment 16%, assistive 4%, authentication 2% (§5.4, Fig. 7).
- **Paradigms** (Fig. 11, p. 17): motor imagery 38 (62% medical), visual evoked potential 31 (61% non-medical; includes P300 and SSVEP), drowsiness/attention 29 (88% non-medical), emotion 15 (93% non-medical). Also auditory EP 7, concentration 6, workload 4, vibrotactile 3, imagined speech 2, error-related potential 2, multiple 18.
- **Devices** (Fig. 9, p. 14; the figure sums to 77): Emotiv EPOC 31 (40%), Compumedics Quik-Cap 7 (9%), NeuroSky MindWave 6 (8%). Others (Easycap, actiCAP, BioSemi ActiveTwo, Enobio, MyndPlay) are 2–3 each.
- **Channels** (Fig. 10, p. 16; n = 163): 1–10 → 55 (34%), 11–20 → 50 (30%), 31–40 → 31, 21–30 → 11, 61–70 → 11; >100 → 5 (3%). Maximum 163 channels (§5.6).
- **Features** (Fig. 12, p. 18; n = 126): PSD 23 (18%), Fourier 20 (16%), CSP 18 (14%); then wavelet, fractal dimension, ICA, PCA (7–8 each).
  - Cited pros and cons (Xie): CSP works well for motor imagery but is noise-sensitive and needs many electrodes; Fourier assumes stationarity (§5.8).
- **Classifiers** (Fig. 13, p. 19; n = 114): **LDA 35 (31%), SVM 24 (21%)**, CNN 5 (4%), naive Bayes 4, random forest 4, ANN 3, DNN 3, GMM 2, kNN 2, multiple 19 (17%).
- **Device comparisons cited** (§5.5, pp. 15–16):
  - Dadebayev 2021: consumer devices perform as well as research devices for emotion recognition.
  - Zerafa 2018: low-end research systems match high-end ones for SSVEP; low-cost headsets have poorer signal.
  - Hinrichs 2020: dry wireless vs wet wired clinical EEG were "comparable", with slightly more artifacts on dry; patients preferred dry.
  - Ratti 2017: medical systems have better data quality, consumer systems are faster to set up.
- **Challenges** (§6.1, pp. 20–22): reliability in noisy everyday settings; low recognition rate and low information throughput; time-consuming per-user calibration; **inter- and intra-subject variability**, which makes subject-independent BCIs "one of the most important obstacles". Also ethics: liability, subliminal probing of private information, manipulation (p. 22).
- **Future** (§6.2): hybrid BCIs (EEG + fNIRS/fMRI/eye tracking); VR for stroke rehabilitation; attention and workload monitoring; authentication; a "brain switch" for safe asynchronous control (§6.2.3); ear-EEG and EEG from non-hairy areas (p. 23–24).

## Limitations (reported)
- The cut-off in 2019 is acknowledged (§3, §6). The query term "EEG-based" probably missed relevant papers (§6, p. 20). The 2019 count is incomplete (§5.1).

## Assessment 🤖
- 🤖 This is a map of the 2009–2019 BCI landscape, not of the current state of the art. Its 4% CNN share describes the pre-DL era. It complements [[roy2019deep]], which covers DL papers in the same years.
- 🤖 The denominators change between figures (171 in the domain counts, 163 channels, 155 techniques, 126 features, 114 classifiers, 77 devices) and are never explained. Percentages are therefore "of papers that reported X", and device reporting was sparse.
- 🤖 Single-person screening, no quality appraisal and a keyword-specific query make it weaker than a typical systematic review. Use it for the taxonomy and rough proportions.
- 🤖 The method mix (PSD/CSP + LDA/SVM) confirms stage 1 of [[q4-evolution-of-methods]] specifically for BCI, and shows why LDA is the default BCI baseline.
- 🤖 "BCI" is used broadly here, so passive monitoring (emotion, drowsiness) counts as BCI. This is why its non-medical share is high and overlaps with Niso's "cognitive monitoring".

## Concepts
- [[common-spatial-patterns]]: CSP is the third most common BCI feature (18/126); noise-sensitive (Fig. 12, §5.8).
- [[linear-discriminant-analysis]]: the most common BCI classifier, 35/114 papers (31%); "simple … low computation requirements and acceptable accuracy" (Fig. 13, §5.9).
- [[digital-filtering]]: dry headsets reportedly more robust to line noise (p. 15).
- [[eeg-preprocessing-pipeline]]: raw → preprocessing → features → classification skeleton (§2).
- [[bci-paradigms]]: the source of the active/passive, evoked/spontaneous and sync/async taxonomy (Tables 1–2), with paradigm frequencies (Fig. 11).
- [[consumer-grade-eeg-devices]]: Emotiv EPOC is 40% of device mentions. Cites consumer vs research comparisons (§5.5).
- [[electrode-types]]: dry vs wet trade-offs cited from Hinrichs 2020 and Soufineyestani (p. 15).
- [[frequency-bands]]: passive BCIs rely on spectral (PSD/FFT) changes (Table 1; §5.7–5.8).
- [[evaluation-protocols]]: subject-independent BCI is named as the key open problem (§6.1).
- [[independent-component-analysis]]: used as a feature extractor in 7/126 papers (Fig. 12).
- [[time-frequency-analysis]]: PSD and Fourier are the top BCI features (43/126 papers); wavelets 8/126 (Fig. 12).

## Related papers
- [[roy2019deep]]: a DL-for-EEG systematic review of the same period. Värbu reuses its PRISMA data-item scheme (§4.1) and channel findings (§5.6).
- [[niso2022wireless]]: also finds monitoring dominant and Emotiv first. Niso is device-centric; Värbu is application-centric.
- [[sabio2024scoping]]: BCI is the top use of consumer devices there (44.5%), and Emotiv is the top device in both.
- [[song2022eeg]]: a motor imagery decoder. Värbu shows motor imagery is the most common BCI paradigm and mostly medical.
- [[lawhern2018eegnet]]: a compact CNN tested across BCI paradigms (P300, ERN, MRCP, SMR); the DL answer to the paradigm-specific pipelines counted here. *(not yet read)*
- [[kaongoen2023future]]: ear-EEG, which Värbu lists as a future direction (p. 23). *(not yet read)*

## Q&A notes
