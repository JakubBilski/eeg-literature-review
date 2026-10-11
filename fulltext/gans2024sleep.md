# Sleep assessment using EEG-based wearables – A systematic review

C.J. de Gans, P. Burger, E.S. van den Ende, J. Hermanides, P.W.B. Nanayakkara, R.J.B.J. Gemke, F. Rutters, D.J. Stenvers. Sleep Medicine Reviews 76 (2024) 101951. doi:10.1016/j.smrv.2024.101951. CC BY 4.0.

*Transcribed by hand from page renders on 2026-10-11 (the PDF has no text layer). Prose is close to verbatim; Table 1 is reformatted with one block per device; only selected references are listed. Page markers follow the PDF.*

<!-- page 1 -->

## Abstract
Polysomnography (PSG) is the reference standard of sleep measurement, but is burdensome for the participant and labor intensive. Affordable electroencephalography (EEG)-based wearables are easy to use and are gaining popularity, yet selecting the most suitable device is a challenge for clinicians and researchers. In this systematic review, we aim to provide a comprehensive overview of available EEG-based wearables to measure human sleep. For each wearable, an overview will be provided regarding validated population and reported measurement properties. A systematic search was conducted in the databases OVID MEDLINE, Embase.com and CINAHL. A machine learning algorithm (ASReview) was utilized to screen titles and abstracts for eligibility. In total, 60 papers were selected, covering 34 unique EEG-based wearables. Feasibility studies indicated good tolerance, high compliance, and success rates. The 42 included validation studies were conducted across diverse populations and showed consistently high accuracy in sleep staging detection. Therefore, the recent advancements in EEG-based wearables show great promise as alternative for PSG and for at-home sleep monitoring. Users should consider factors like user-friendliness, comfort, and costs, as these devices vary in features and pricing, impacting their suitability for individual needs.

Keywords: Sleep; Systematic review; Electro-encephalography; EEG; Wearables; Sleep assessment.

## 1. Introduction
Sleep is an essential daily requirement for the development and maintenance of physical and psychological health. During sleep, important processes such as memory processing and consolidation, cellular repair, and brain development are facilitated [1–5]. There is no uniform definition of good sleep, but some scholars define good sleep as the alternation of specific sleep stages throughout the night, initiated by a cascade of neurochemical activity with resulting systemic benefits [6]. Unfortunately, in Europe the median prevalence of insomnia with night-time symptoms is around 25 % [7]. Common consequences of poor sleep are daytime sleepiness, reduced alertness, memory loss, increased anxiety, and on the long term, metabolic syndrome, type 2 diabetes mellitus, and cardiovascular disease [8–15]. This highlights the importance of research and clinical assessment tools that can accurately and objectively measure sleep. Additionally, reliable, and valid instruments may also contribute to the comparability and replicability of study results.

Polysomnography (PSG) and wrist actigraphy are commonly used objective measures. PSG is considered the reference standard for evaluating sleep stages and sleep cycles. PSG combines biometrics of modified electro-encephalography, ocular and submental electromyography, and monitoring of several cardio-respiratory domains. However, PSG is not routinely used as it requires specialized equipment, is uncomfortable, labor intensive as well as expensive. Actigraphy records

<!-- page 2 -->

body movement, and sleep-wake periods can be inferred by analyzing activity versus inactivity segments. Wrist actigraphy, however, is limited by its lack of specificity as it does not measure sleep staging and lying still can be wrongly classified as sleep [16,17]. Recently, there has been a rapid development of affordable sleep wearables [18].

Among the new sleep wearables, electroencephalography (EEG)-based systems appear to be the most accurate in identifying sleep stages [19]. Addressing the constraints of standard PSG, innovative EEG-based wearables have been designed with novel materials, streamlined sensing architectures, and sophisticated data analytics to offer minimized and less intrusive alternatives for at-home sleep monitoring. The transition from complex and cumbersome PSG equipment to user-friendly, unobtrusive EEG-based wearables demonstrates significant progress, making sleep monitoring accessible to individuals in the comfort of their homes. However, it remains challenging to determine which wearable is the optimal one for use in specific settings or population. A systematic overview of EEG-based wearables could assist researchers and clinicians in the selection of a wearable for a particular purpose, and up till now such a systematic review is not available. Therefore, in this systematic review, we aim to provide a comprehensive overview of available (novel) EEG-based wearables to appraise human sleep. For each wearable, we will provide an overview regarding populations in which it has been validated and reported measurement properties.

Abbreviations: EEG electroencephalography; PSG polysomnography; EOG electrooculography; EMG electromyography.

## 2. Methods
This review is registered on PROSPERO (international prospective register of systematic reviews) with registration number CRD42023465973 and followed the Preferred Reporting Items for Systematic Reviews and Meta-analysis (PRISMA) guidelines [20].

### 2.1. Literature search
A systematic search was conducted (last update November 29th, 2023), independently by two researchers (CG, PB) in the databases OVID MEDLINE, Embase.com and CINAHL. The search included keywords and free text terms related to EEG sleep measurement methods combined with (synonyms of) 'sleep', 'insomnia' or 'sleep disorders' (see Supplementary content, S1). The separate search results were aggregated. No restrictions were applied regarding date or language. A grey literature and reference search was applied to capture any remaining eligible papers [21].

### 2.2. Inclusion/exclusion criteria
Inclusion criteria were: 1) devices developed for humans, 2) objective assessment of sleep/insomnia/sleep disorder with the use of EEG-based wearables, 3) papers focusing on the development of a specific EEG-wearable for sleep or evaluation of measurement properties for existing EEG-wearables against the reference standard (from now on called validation papers), 4) electronically available in full-text format.

Exclusion criteria were: 1) literature reviews, 2) written in languages other than English, Dutch, or German, and 3) animal studies.

Additionally, due to the difficulty in finding validation papers, we employed a grey literature search to identify any remaining devices, ensuring a comprehensive overview of all available options. EEG-wearables were defined as follow: electronic devices worn on the body, that measure and record the electrical activity of the brain, and the collected data is analyzed to provide insights into various neurological states.

### 2.3. Screening and data extraction

#### 2.3.1. Screening
After the initial database search and after deduplication, ASReview was used to assess the eligibility of titles and abstracts [22]. This open-source tool employs active learning and machine learning models to aid researchers in making inclusion and exclusion decisions. It presents articles one at a time for evaluation based on initial categorization. Researchers' decisions improve the algorithm's accuracy and prompt it to reorder the remaining articles, prioritizing those deemed most relevant, thereby enhancing the review process [22]. Two researchers (CG, PB) independently screened all titles and abstracts with ASReview with the following setup: TF-IDF as feature extraction technique, Naive Bayes as classifier, maximum as query strategy and dynamic resampling as balance strategy. The stop criterium was 150 irrelevant records. After the first screening, an additional model was trained in ASReview lab to search for any remaining papers, using Sentence BERT with logistic regression. Previous research has demonstrated that the latter has superior performance, but is more computationally intensive (with finding 95 % of the relevant papers by screening approximately 1.3 % of the papers). It conserves computational resources when run as a secondary model, while also increasing accuracy [23]. Subsequently, the full text versions of the potentially eligible publications were retrieved (if necessary, by contacting one of the authors) and assessed according to the inclusion and exclusion criteria by two independent reviewers (CG and PB) and reasons for exclusion were recorded. There was one discrepancy between the two reviewers and this was resolved through discussion with a third reviewer (FR).

#### 2.3.2. Properties of sleep assessment
Data extraction was performed by two reviewers (CG, PB), using a pre-approved and piloted form. In papers assessing the EEG-based wearables a variety of terms have been used to describe the validity of an assessment method. In general, validity is often described in terms of accuracy (sensitivity, specificity) or agreement (intraclass correlation coefficient, Cohen's Kappa, Bland Altman plots, or consistency checks using repeated measures). The measurement tools are often validated to the 'reference standard', e.g., polysomnography. If a study validated an EEG-based wearable against both automatic and manual scoring of polysomnography, only the manual scoring was included. Uncertainties in data extraction were resolved through discussion. Following the extraction of data, reviewers CG and PB cross-verified each other's extraction, revealing no discrepancies. To demonstrate how each EEG wearable is applied to the body, we have created drawings for each EEG device for which an example was available in the included papers or on the World Wide Web.

### 2.4. Assessing risk of bias
We assessed paper quality and risk of bias using the QUADAS-2 criteria, a widely accepted tool for evaluating articles about validity of measurements [24]. It consists of 14 items across four domains (patient selection, index test, reference standard, flow, and timing of tests) categorized into risk of bias and applicability judgment. Each item is answered as 'yes,' 'no,' or 'unclear,' with 'yes' indicating low risk of bias or applicability concerns. Two researchers (CG, PB) independently evaluated the included studies. Risk of bias was only assessed for full-text papers (e.g., not for (conference) abstracts, pilot, and feasibility studies). Disagreement was resolved through dialogue.

<!-- page 3 -->

## 3. Results
The search strategy initially yielded 109,115 unduplicated citations. Title and abstract screening resulted in the identification of 231 potentially eligible papers. After a thorough full-text screening, a total of 53 were included in the review (S2, Fig. 1). Seven additional articles were identified through reference checking or snowballing. Reasons for exclusion after full-text screening are also listed in S2, Fig. 1. A meta-analysis was not possible due to the heterogeneity of the data.

The span of the publications extended from 1988 to 2023, revealing a significant increase in research activity in recent years. This trend was particularly pronounced from 2020 onwards, with 31 of the 60 included papers (52 %) in or after 2020. This surge indicates a growing interest and advancements in the field of EEG-based wearables.

We identified 24 distinct EEG-based wearables from 37 full-text validation papers and five conference abstracts. Additionally, six devices were identified from thirteen feasibility studies, and four devices were found from grey literature without a paper validating the device against PSG. This brings the total count to 34 unique EEG-based wearables.

Of the 24 devices identified from the validation papers, 21 devices were explicitly identified with a brand name, as detailed in Table 1 [25–58]. In contrast, there were three types of devices with validation papers that did not have an associated brand name, see S4 [59–69]. The range of the EEG-based wearables was quite diverse, including headbands, eye masks, single-channel EEG, portable PSG systems, forehead multiple sensor patches and ear-EEG channels. Focusing on the 42 papers/abstracts of these 24 validated devices, 27 out of 42 (64 %) papers were conducted in a clinical setting, five papers (12 %) were based on studies conducted at home, and the remaining 10 papers (24 %) did not specify the location of the study. When analyzing the capability of these wearables to detect sleep stages, a notable variation was observed. Seventeen wearables (70 % of those studied) could differentiate between the three distinct stages of non-REM sleep. However, seven wearables had a more limited functionality, only able to distinguish between light and deep sleep within the non-REM category. Studies differed in the reported measures of validity. Reported accuracy for sleep metrics ranged between 0.48 and 0.95. Reported sensitivity ranged between 0.11 and 0.98, with the lowest percentages obtained for the N1 stages.

### 3.1. Wearability and feasibility
Fig. 1 illustrates the attachment methods for each EEG wearable listed in Table 1, including headbands/eye masks (Fig. 1, A–E), ear-EEG (Fig. 1, F–G), single-channel EEG (Fig. 1, H–I), and portable EEG devices (Fig. 1, J–L), as well as forehead multiple sensor patches (Fig. 1, M–S). However, example images for the QUISI v 1.0 and LANMAO Sleep Recorder – ×7 mini version were not available [33,37,38]. Some EEG wearables are solely equipped with one or multiple EEG channels [25,26,31–33,36–44,47,49–57,70,71], while others additionally feature capabilities such as tracking of movement, body position, breathing frequency, heart rate, light exposure, temperature, oxygen levels, and monitoring of snoring and nasal pressure [27–30,45,46,48,58,72,73].

Fourteen feasibility studies on ten EEG-based wearable devices demonstrated their general effectiveness and user tolerance. These included three headbands (Dreem [29,73], Sleep Profiler [40,41], Zmachine Insight [56]), three portable PSG systems (Nox-A1 type 2 [82,83], Cerebra sleep system [84], Philips Alice PDx [85]), and one forehead multiple sensor patch (Xtrodes sleep tracker [49]), and three

**Fig. 1.** Overview of EEG wearables (line drawings). A. Dreem, B. Neuroon, C. Zeo headband, D. Zmax, E. Sleep Profiler, F. cEEGrid, G. IDUN Guardian, H. UmindSleep, I. Z Machine Insight, J. Embletta X100, K. Onera STS, L. SOMNO Watch plus EEG, M. Prodigy sleep monitor, N. Sleep-Graph, O. Sedline Brain Function Monitor, P. trEEGrid, Q. Xtrodes sleep tracker, R. Bittium Brain-status, S. Insomnograf.

<!-- page 4 -->

## Table 1 (pp. 4–9): EEG-based wearables with validation papers against PSG

Columns in the original: name; electrode composition; sleep stages; sleep classification; validation population and setting; reference standard; accuracy; agreement % / Cohen's kappa (κ); sensitivity / specificity; correlation. Numbers are proportions unless marked %. "Light" = N1+N2, "Deep" = N3 where a device reports four stages.

### Headbands / eye masks
**Dreem headband [27–29,72,73]** (p. 4)
- Electrodes: five dry EEG electrodes, providing seven different readings. Tracks movements, body position, breathing frequency. Measures heart rate through a red-infrared pulse oximeter.
- Stages: five (Wake, REM, N1, N2, N3). Classification: auto-staging algorithm.
- [28] Participants at sleep lab; reference PSG (manually scored). Accuracy: All 0.84, Wake 0.74, N1 0.48, N2 0.83, N3 0.83, REM 0.85. κ: All 0.73, Wake 0.74, N1 0.43, N2 0.75, N3 0.74, REM 0.79.
- [27] Adults at sleep center; reference PSG (manually scored). Accuracy: REM 0.88, N1 0.54, N2 0.86, N3 0.84, Wake 0.83.

**Neuroon [34]** (p. 4)
- Electrodes: a wearable EEG eye mask, single-channel EEG signal. According to the manufacturer, it can also track heart rate, body temperature and body movements.
- Stages: four (wake, light sleep, deep sleep, REM). Classification: auto-staging algorithm.
- [34] Participants at home; reference: portable 1-channel EEG Sleep Scope (auto-staging algorithm). Pearson correlation: light sleep 0.15, deep sleep 0.50*, REM 0.05 (*p ≤ 0.05).

**Zeo headband [51–55]** (pp. 4–5)
- Electrodes: three EEG electrodes. Stages: four (wake, light, deep, REM). Classification: auto-scoring algorithm.
- [55] Healthy adults at sleep lab; reference PSG (Cadwell Easy III, manually scored). Agreement: Wake 0.64, REM 0.86, Light 0.86, Deep 0.71.
- [53] Healthy students in sleep lab; reference PSG (Siesta 802, manually scored). κ: Light 0.56, Deep 0.70, REM 0.67. Sensitivity 0.87, specificity 0.56.
- [51] Adults (primary insomnia vs good sleepers); reference PSG (semi-automatic Somnolyzer 24×7). Agreement overall 0.73, κ = 0.56. Sensitivity: Wake 0.41, REM 0.74, Light 0.80, Deep 0.62.
- [54] Healthy adults at sleep lab; reference PSG (Astro-Med Grass Heritage Model 15, Grass Gamma software, manually scored). Accuracy: Wake 0.87, Light 0.75, Deep 0.91, REM 0.81. κ: Wake 0.62, Light 0.49, Deep 0.72, REM 0.28. Sensitivity: Wake 0.59, Light 0.67, Deep 0.83, REM 0.82.
- [52] Healthy adults at sleep lab; reference PSG (Grass Comet Plus, manually scored); auto-staging. Accuracy: Wake 0.91, All sleep 0.90, Light 0.73, Deep 0.86, REM 0.86. Sensitivity: Wake 0.40, All sleep 0.97, Light 0.71, Deep 0.67, REM 0.74. Specificity: Wake 0.98, All sleep 0.45, Light 0.75, Deep 0.90, REM 0.86.

<!-- page 5 -->

**Sleep Profiler [40–44]** (p. 5)
- Electrodes: three EEG electrodes. Stages: five.
- [42] Adults scheduled for a sleep study in sleep center; manually scored; reference PSG (manually scored). Accuracy: Wake 0.89, REM 0.94, N1 0.90, N2/N3 0.88. Overall κ = 0.67. Sensitivity: Wake 0.78, REM 0.86, N1 0.21, N2/N3 0.87. Specificity: Wake 0.91, REM 0.95, N1 0.96, N2/N3 0.89. Intraclass correlation: N1 0.66, N2+3 0.96, REM 0.92.
- [43] Adults at sleep lab; auto-staging; reference PSG (Alice 5, manually scored). Agreement: Wake 0.82, N1 0.26, N2 0.85, N3 0.82, REM 0.73.
- [44] Healthy participants at clinic; auto-staging and manually scored; reference PSG (manually scored). Agreement autoscoring / manually scored: Wake 0.92/0.93 (κ = 0.42/0.44), N1 0.89/0.93 (κ = 0.07/0.13), N2 0.78/0.81 (κ = 0.55/0.61), N3 0.88/0.90 (κ = 0.62/0.71), REM 0.85/0.90 (κ = 0.58/0.73). Sensitivity (auto/manual): Wake 0.44/0.40, N1 0.27/0.27, N2 0.72/0.76, N3 0.61/0.74, REM 0.72/0.86. Specificity: Wake 0.96/0.98, N1 0.91/0.95, N2 0.83/0.85, N3 0.96/0.95, REM 0.89/0.91.

**Zmax [58]** (p. 5)
- Electrodes: Lite version: EEG electrodes, accelerometer, and a PPG sensor. Advanced version in addition: light sensor, microphone, temperature, nasal/SpO2 sensors.
- Stages: five; auto-staging. [58] Different datasets; reference PSG (manually scored). Accuracy overall 0.71; overall κ = 0.60. Sensitivity: Wake 0.73, N1 0.29, N2 0.73, N3 0.68, REM 0.77.

### Ear-EEG
**cEEGrid [26]** (pp. 5–6)
- Electrodes: a flex-printed, ultra-thin adhesive strip designed to fit behind the ear. It contains 10 embedded electrodes, utilized for capturing electrophysiological signals from the area around the ear.
- Stages: five; manually scored. Healthy adults at sleep lab; reference wireless PSG (SomnoHD, manually scored). Agreement overall 0.59, κ = 0.42. Pearson: Wake r = 0.74 (p = 0.01), N1 r = 0.64 (p = 0.01), N2 r = 0.55*, N3 r = 0.63*, REM r = 0.59 (p = 0.02) (*p = 0.05).

<!-- page 6 -->

**IDUN Guardian [31]** (p. 6)
- Electrodes: a 2-channel in-ear EEG system. Stages: five; manually scored. Healthy adults; reference PSG (SOMNOscreen plus, manually scored). Pearson average r = 0.78, no p-value.

### Single-channel EEG
**QUISI v 1.0 [37,38]** (p. 6)
- Single-channel EEG. Uses neuronal network techniques for automatic sleep stage classification. Stages: five (Wake, REM, N1, N2, N3/N4).
- [37] Men with primary snoring or obstructive sleep apnea (OSA) at sleep lab; reference PSG (SIDAS GS, manually scored). Spearman: Wake r = 0.33 (p = 0.01), N1 r = 0.25 (p = 0.05), N2 r = 0.42 (p = 0.002), N3/4 r = 0.31 (p = 0.02), REM r = 0.25 (p = 0.05).
- [38] Patients at sleep lab; reference PSG (manually scored). Pearson: Wake 0.68 (p < 0.0001), N1 0.19 (p = 0.26), N2 0.26 (p = 0.12), N3 0.30 (p = 0.07), N4 0.41 (p = 0.01), REM 0.58 (p < 0.0001).

**Umind-sleep [48]** (p. 6)
- Single-channel EEG with sticker. Measures sleep, heart rate, blood oxygen, snoring, body position and frontal temperature. Stages: four (wake, light (N1, N2), deep (N3), REM); auto-staging.
- Adults at sleep center; reference Philips Alice 6 PSG (manually scored). Accuracy: Wake 0.93, Light 0.85, Deep 0.95, REM 0.95. κ: Wake 0.72, Light 0.69, Deep 0.76, REM 0.79. Sensitivity: Wake 0.80, Light 0.88, Deep 0.79, REM 0.83. Specificity: Wake 0.95, Light 0.83, Deep 0.97, REM 0.97.

**Zmachine Insight [56,57]** (pp. 6–7)
- Single-channel EEG. Algorithm-based sleep staging. Stages: four (wake, light, deep, REM); auto-staging.
- [57] Adults with psychiatric disorders or sleep disorder; reference PSG (PSG-1100 Nihon Kohden, and Embla N7000 Natus, manually scored). Intraclass: Light 0.50, Deep 0.32, REM 0.75, Non-REM 0.65.

<!-- page 7 -->

### Portable EEG
**Embletta X100 [30]** (p. 7)
- Two EEG channels, one EOG, chin EMG, nasal cannula (pressure), thoracic and abdominal respiratory effort bands, body-position sensor, and pulse oximetry. Stages: five; auto-staging and manually scored.
- Surgical adult patients in sleep lab; reference PSG (manually scored). Pearson, autoscoring: N1 r = −0.038 (p = 0.871), N2 r = 0.298 (p = 0.189), N3 r = 0.042 (p = 0.858), REM r = 0.355 (p = 0.103). Manually scored: N1 r = 0.444 (p = 0.043), N2 r = 0.819 (p < 0.001), N3 r = 0.567 (p = 0.007), REM r = 0.730 (p < 0.001).

**Onera STS [35]** (p. 7)
- Four sensor patches with hydrogel applied to forehead, upper chest, abdomen, lower leg. Measures EEG, EOG, EMG, ECG, respiratory signals, nasal pressure, oxygen saturation, activity, body position, and snoring loudness. Stages: five; manually scored.
- Adults referred for sleep study; reference PSG (Embla S4500, manually scored). Accuracy: Wake 0.94, REM 0.95, N1 0.90, N2 0.85, N3 0.96. Sensitivity: Wake 0.62, REM 0.88, N1 0.27, N2 0.88, N3 0.77. Specificity: Wake 0.98, REM 0.96, N1 0.95, N2 0.82, N3 0.98. Pearson: Wake 0.64, REM 0.91, N1 0.67, N2 0.69, N3 0.65.

**SOMNOwatch plus EEG [45,46]** (p. 7)
- Ten EEG electrodes (Ag/AgCl), EOG, EMG, actigraph, body temperature, oximetry. Stages: five; semi-automatic Somnolyzer and auto-staging DOMINO Light.
- [45] Adults in sleep laboratory; reference EEG amplifier (Neuroscan) with semi-automatic Somnolyzer 24×7 staging. With Somnolyzer: accuracy 0.97, κ = 0.78, sensitivity 0.98, specificity 0.87. With DOMINO Light: accuracy 0.93, κ = 0.37, sensitivity 0.93, specificity 0.81.

### Forehead multiple sensor patch
**LANMAO Sleep Recorder – ×7 mini version [33]** (pp. 7–8)
- The base box: charging and processing the data. The head patch: frontal single-channel EEG electrodes with hydrogel, head movement. Stages: four (wake, light, deep, REM); auto-staging.
- Adults in sleep monitoring room; reference PSG (Natus Embla NDx, manually scored). Accuracy: overall 84.12%, Wake 0.97, Light 0.87, Deep 0.91, REM 0.94. κ: overall 0.79, Wake 0.91, Light 0.63, Deep 0.76, REM 0.83.

<!-- page 8 -->

**Prodigy sleep monitor [36]** (p. 8)
- EEG, EOG, EMG. The data collected is scored by MSS and edited using suggestions by the Editing Helper within MSS. Stages: five; auto-staging.
- Patients suspected of sleep disorder at sleep center; reference PSG (manually scored). Intraclass correlation: Wake 0.76, N1 0.60, N2 0.83, N3 0.55, REM 0.45.

**SedLine Brain Function Monitor [39]** (p. 8)
- Six channels: EEG and EMG. Stages: five; manually scored.
- Subjects scheduled for sleep study at sleep lab; reference PSG (manually scored). Agreement overall 0.75 (κ = 0.62); Wake 0.67, N1 0.29, N2 0.99, N3 0.06, REM 0.89.

**Sleep-Graph [70,71]** (p. 8)
- 2 EEG electrodes, EOG, EMG. Stages: five; manually scored.
- [70] Patients >16 years diagnosed psychiatric disorders or sleep disorder admitted to Akita University Hospital for a sleep study; reference digital PSG recorder (Somno HD, manually scored). Accuracy: sleep/wake 0.92, Light 0.80, Deep 0.93, REM 0.92. Sensitivity: Sleep 0.95, Light 0.79, Deep 0.69, REM 0.91. Specificity: Wake 0.76, Light 0.82, Deep 0.97, REM 0.93.
- [71] Participants with Parkinson's disease; reference PSG (manually scored). Spearman: N1 0.64 (p = 0.09), N2 0.60 (p = 0.12), N3 0.43 (p = 0.29), REM 0.98 (p < 0.001).

**trEEGrid [47]** (p. 8)
- Seven EEG electrodes, 1 EOG, 1 EMG. Stages: five; manually scored.
- Healthy adults at home; reference PSG system (SOMNOscreen Plus, manually scored). κ: All 0.70, Wake 0.75, N1 0.46, N2 0.66, N3 0.79, REM 0.76.

**Xtrodes sleep tracker [49,50]** (pp. 8–9)
- Four EEG electrodes, two EOG electrodes, and two EMG electrodes. Stages: five; manually scored.
- [50] Healthy adults and patients with Parkinson's disease (results/properties showed of all patients together) at sleep center; reference video PSG Natus (NDx) system (manually scored). Accuracy overall 0.77. κ: overall 0.67, Wake 0.70, N1 0.22, N2 0.58, N3 0.41, REM 0.72. Sensitivity: Wake 0.91, N1 0.16, N2 0.84, N3 0.68, REM 0.77. Specificity: Wake 0.94, N1 0.99, N2 0.80, N3 0.97, REM 0.98.

<!-- page 9 -->

**Bittium Brain-status [25]** (p. 9)
- Set of 3 hydrogel-coated silver ink electrodes positioned on the forehead, an EOG electrode under the right eye, along with two reference and two ground electrodes. Stages: five; manually scored.
- Adults with sleep bruxism or healthy controls at sleep lab; reference Embla N7000 full PSG system (manually scored). Agreement overall 0.77–0.82 (κ = 0.66–0.74). Sensitivity: Wake 0.75–0.77, N1 0.51–0.64, N2 0.86–0.88, N3 0.72–0.83, REM 0.61–0.89.

**Insomnograf [32]** (p. 9)
- Five EEG channels, EOG, EMG, heart rate, and breathing. Stages: four (Wake, N1+N2, N3, REM); manually scored.
- Healthy participants; reference PSG (manually scored). Accuracy overall 0.91.

### Body text, p. 9 (right column)
unnamed portable systems [86–88]. The studies assessed aspects like compliance, success rates, and comfort.

Key feasibility finding were the following: Dreem headband had less than 20 % artifacts in most tests, with high success rates in participant recordings [29,73]. Zmachine Insight + showed a 94 % success rate among adolescents, with varying levels of comfort reported [56]. Sleep Profiler appeared to under-report N3 sleep and over-report N1 sleep but had an 86 % compliance rate [40,41]. Zmachine Insight + showed a 94 % success rate among adolescents, with varying levels of comfort reported [56]. Nox-A1 type 2 was well-received by children, with a preference for home testing [82,83]. Cerebra system had a 83 % success rate, with improved results on second-night recordings [84]. Xtrodes Sleep Tracker provided stable recordings in different settings and was comfortable for all users [49]. Data from one of the unnamed devices was effectively scorable in a home setting [86], while another had issues in a pediatric study [87]. A study on critically ill patients indicated the potential of portable devices in assessing sleep quality for healthcare interventions [88].

### 3.2. EEG wearables without sleep measurement validation studies
Four EEG-based wearables, which lack dedicated (real-life) sleep measurement validation studies, were included in our review. As these devices are capable of measuring sleep, their functionalities are summarized in this section. The Philips Smartsleep Deep Sleep headband is designed to boost slow-wave activity with precise auditory stimulation, calibrated for high deep sleep detection (sensitivity ≥70 %, specificity ≥95 %) [89]. The URGOnight uses sensori-motor rhythm neurofeedback, which may help alleviate sleep issues, as uses have reported increased sleep duration after completing the program [90]. The MUSE headband, primarily used for meditation, demonstrated sleep staging accuracy between 85 and 86 % and a Cohen's kappa of 0.77–0.79 in a study comparing deep learning models [91]. Lastly, one study developed a multi-biosignal interface, which contained EOG, EEG, and EMG, and validated the wearable against existing datasets, with a Cohen's k of 0.67–0.7 [92].

### 3.3. Quality and risk of bias assessment
A quality and risk of bias assessment was conducted for 38 full-text papers (S3). In five validation papers, no quality and risk assessment was performed, as they were presented solely as abstracts [28,31,32,65,66]. Among the full-text papers, 21 studies were identified as having a high risk of bias in at least one of the seven assessed domains [26,27,34,35,37,39,43,44,46,47,51–53,59–64,67,70]. Eight papers were found to have no risk of bias and were consequently rated as low risk [33,36,38,45,57,58,69,71]. Nine papers were classified as having an unclear risk of bias in at least one domain [25,30,42,48,50,54,55,68,92]. The goal was to provide a comprehensive overview of the available EEG-based wearables, regardless of the identified bias levels. Hence, studies identified with a risk of bias were not excluded from this review [93].

## 4. Discussion
In this systematic review, we present a comprehensive overview of available (novel) EEG-based wearables to appraise human sleep. We provide consumers, sleep researchers and somnologists the opportunity to choose their preferred method among available technologies. Our study identified 34 unique devices, which include headbands, eye masks, single-channel EEG, portable PSG systems, multiple sensor patches and ear-EEG channels. This diversity highlights the innovative approaches being taken to measure sleep in more user-friendly and accessible ways. Notably, there has been a significant increase in relevant publications in recent years, with half of the articles published in the last three years. This trend suggests a growing interest in and recognition of the importance of sleep measurement and the potential

<!-- page 10 -->

for EEG wearables in this domain. The EEG-based wearables have shown high accuracy or sensitivity in detecting various sleep stages. The measurement properties of all EEG-based systems are similar, with most systems capable of measuring five different sleep stages, as opposed to four sleep stages. This variety allows users to select the most user-friendly system based on their needs, such as choosing a device they find most comfortable and minimally intrusive, with as few wires as possible. However, for users interested in monitoring additional variables, like, for example, nasal flow, selecting a device with these specific capabilities is recommended. Another consideration would be the costs of the devices, since they vary significantly among different devices [94].

Furthermore, there is a limited number of articles that specifically focus on the home setting. Most studies have been conducted in sleep labs or clinical settings, often with a researcher present to assist participants in operating the devices, which may overestimate the feasibility compared to the home setting. Regarding feasibility and acceptability, the EEG-based wearables appear to be well-tolerated, as indicated by high compliance and success rates. One study reports the comfort level of a wearable as ranging from comfortable to mildly uncomfortable [56].

This review primarily focuses on validating EEG-based wearables against PSG, the reference standard in sleep monitoring. Expert scoring, conducted by extensively trained professionals, remains the preferred approach to ensure the utmost accuracy in evaluating EEG-based wearables [95]. If a study validated an EEG-based wearable against both automatic and manual scoring, only the manual scoring has been included in Table 1. It is important to recognize that the accuracy of manual sleep stage scoring of both PSG and EEG-based wearables can vary, mainly due to subjective interpretation of data by technicians. The scores are influenced by the technicians' experience and training, leading to potential variations in results [96]. Therefore, the results of validation studies should be interpreted with an understanding of these limitations. We acknowledge that automatic scoring is also being extensively researched and has already shown promising results, with future studies potentially matching or even surpassing the accuracy of human experts in scoring PSG [95]. However, there is currently no consensus yet on a standard for automated scoring [95]. This lack of consensus highlights the need for additional validation methods. One promising direction is to integrate PSG with other assessment tools, such as subjective sleep quality measures, to provide a more comprehensive evaluation of new sleep monitoring systems.

The selection of appropriate statistical metrics to objectively evaluate and compare different EEG wearables is another important topic of discussion. The papers reviewed here employed a variety of metrics, complicating the task of comparing their results. Commonly used metrics include accuracy, agreement rate, sensitivity, specificity, and Pearson's correlation. However, Cohen's kappa coefficient is considered the most suitable for use in these evaluations. This is because it accounts for chance agreement in its assessment of inter-rater reliability, especially in unbalanced datasets. This ability to adjust for chance makes it a more reliable measure in the context of wearable technology assessments, where datasets can vary significantly in size and composition [97].

Actigraphy and polysomnography have been mentioned as the most well-known forms of objective sleep monitors. Alongside the emerging wearables mentioned in this systematic review, efforts have been made to develop non-wearable sleep monitoring systems to minimize interruptions to the user's natural sleep patterns. However, these systems often have limitations in their accuracy of sleep assessment. One example is a pad inflated with air and it is positioned under the mattress. It closely aligns with PSG in estimating the apnea-hypopnea index (AHI), but it tends to overestimate the total sleep time and underestimate the wake after sleep onset (WASO) [98]. Another example is a thin, flat sensor strip placed immediately under the bedsheet at chest level. In contrast to the inflated pad under the mattress, this device tends to overestimate the WASO [99].

Our review underscored the growing interest and advancements in the field of wearables, noting that over half of the included studies were published in or after 2020. This upward trend is also apparent in previous reviews on wearables. While some of these reviews are limited to commercially available devices [100,101], others cover wearables that measure EEG but do not focus specifically on sleep monitoring [102,103]. A notable limitation in two (recent) published reviews is the absence of a detailed methodology section, making it non-reproducible. Furthermore, both failed to encompass all available devices [104,105]. The unique contribution of our review lies in its systematic approach to identify available EEG-based wearables, assess the risk of bias, and distinguish between validation studies and feasibility studies. To the best of our knowledge, this systematic review is the first to offer a comprehensive overview of all EEG-based wearables, encompassing validation data and validated populations, thereby aiding in the selection of suitable devices for research or clinical applications.

However, the review faces certain limitations. The primary limitation of the literature is the scarcity of published validation studies for the available consumer devices. To address this, we sought additional studies by reference checking or through snowball sampling. Despite these efforts, it is possible that some EEG-based wearables were overlooked. Moreover, the exclusion of five papers due to language barriers may have led to similar omissions. To ensure a broad and inclusive overview, we decided to include all papers, despite acknowledging the potential risk of bias. A significant concern raised during the quality assessment was the prevalence of small sample sizes in numerous reviewed studies. It is important to recognize that small study populations are a common occurrence in the field of objective sleep measurement. Omitting these studies from our review would limit our ability to offer a comprehensive overview of the current market's wearable devices. Another challenge encountered was the ambiguity or absence of the reported device brand names. Particularly for ear-EEG wearables, many articles did not mention a brand. This led to clustering of the devices based on similarity in feature descriptions, although it remains unclear if the devices referenced were indeed the same or merely similar. Another topic not extensively addressed in this review is the aspect of costs associated with EEG-based wearables. The pricing and business models for these devices vary considerably, which is an important consideration for potential buyers. However, given the dynamic nature of the market, prices fluctuate over time. Therefore, incorporating current pricing information into this review may not be relevant for future reference, as these figures are subject to change and could quickly become outdated. This variability in costs underscores the importance of conducting up-to-date research when considering the purchase of an EEG wearable device.

## 5. Conclusion
The recent increase in EEG-based wearables demonstrate impressive accuracy in sleep staging, competing with the reference standard of PSG, while offering a more comfortable and less intrusive alternative. Thus, EEG-based wearables have good potential as alternative for PSG and for at-home sleep monitoring. The measurement properties across these EEG-based systems are notably similar, with most being able to discern five different sleep stages, rather than only four. This advancement enables users to choose the most user-friendly system according to their personal needs, prioritizing factors like comfort and minimal invasiveness, with fewer wires. Additionally, prospective users should consider the costs associated with these devices, as they vary significantly. Therefore, while EEG-based wearables offer considerable potential for home-based sleep analysis, informed choices depend on understanding their diverse capabilities, validation contexts, and cost implications.

<!-- page 11 -->

## 6. Practice points
1. EEG-based wearables demonstrate impressive accuracy in sleep staging, competing with the reference standard of PSG, while offering a more comfortable and less intrusive alternative.
2. Potential users ought to select the most user-friendly system according to their personal needs and should consider the costs associated with these devices, as they vary significantly.

## 7. Research agenda
1. To ensure generalizability of EEG based wearable performance beyond the controlled sleep lab environment, more research is required in real-world settings, such as home or other non-clinical settings.
2. Considering the diverse variety of hardware, data pre-processing, and sleep staging algorithms in the field, future research may concentrate on comparative analyses of these components. Such studies would facilitate the identification of the most effective and comparable materials, thereby enhancing the quality and reliability of outcomes within this domain.

Funding: AmsterdamUMC Innovation Grant (salary of CG). Supplementary data (S1–S4: search strategy, PRISMA flow, risk of bias, unnamed devices) at doi:10.1016/j.smrv.2024.101951 (not retrieved).

## References (selected, pp. 11–13)
- [19] Imtiaz SA. A systematic review of sensing technologies for wearable sleep staging. Sensors (Basel). 2021.
- [22] van de Schoot R, et al. An open source machine learning framework for efficient and transparent systematic reviews. Nat Mach Intell 2021;3(2):125–33.
- [24] Whiting PF, et al. QUADAS-2: a revised tool for the quality assessment of diagnostic accuracy studies. Ann Intern Med 2011;155(8):529–36.
- [26] Sterr A, et al. Sleep EEG derived from behind-the-ear electrodes (cEEGrid) compared to standard polysomnography: a proof of concept study. Front Hum Neurosci 2018;12.
- [27] Arnal P, et al. The Dreem Headband compared to polysomnography for electroencephalographic signal acquisition and sleep staging. Sleep 2020;43(11).
- [47] da Silva Souto C, et al. Pre-gelled electrode grid for self-applied EEG sleep monitoring at home. Front Neurosci 2022;16.
- [50] Oz S, et al. Monitoring sleep stages with a soft electrode array: comparison against vPSG and home-based detection of REM sleep without atonia. J Sleep Res 2023;32(5).
- [58] Esfahani M, et al. Validation of the sleep EEG headband ZMax. 2023.
- [59] Tabar Y, et al. At-home sleep monitoring using generic ear-EEG. Front Neurosci 2023;17.
- [60] Tabar Y, et al. Ear-EEG for sleep assessment: a comparison with actigraphy and PSG. Sleep & Breathing 2021;25(3).
- [61] Jørgensen S, et al. Long-term ear-EEG monitoring of sleep – a case study during shift work. J Sleep Res 2023;32(5).
- [63] Jørgensen S, et al. Ear-EEG-based sleep scoring in epilepsy: a comparison with scalp-EEG. J Sleep Res 2020;29(6).
- [64] Nakamura T, et al. Hearables: automatic overnight sleep monitoring with standardized in-ear EEG sensor. IEEE Trans Biomed Eng 2020;67(1).
- [91] Jaoude M, et al. Automated sleep staging on wearable EEG enables sleep analysis at scale. IEEE/EMBS NER 2023.
- [94] Esfahani MJ, et al. Citizen neuroscience: wearable technology and open software to study the human brain in its natural habitat. Eur J Neurosci 2023.
- [95] Gaiduk M, et al. Current status and prospects of automatic sleep stages scoring: review. Biomed Eng Lett 2023;13(3):247–72.
- [96] Lee YJ, Lee JY, Cho JH, Choi JH. Interrater reliability of sleep stage scoring: a meta-analysis. J Clin Sleep Med 18(1):193–202.
- [97] Radha M, et al. A deep transfer learning approach for wearable sleep stage classification with photoplethysmography. npj Digital Medicine 2021;4(1):135.
- [100] Ibanez V, et al. Sleep assessment devices: types, market analysis, and a critical view on accuracy and validation. Expert Rev Med Dev 2019;16(12):1041–52.
- [101] Guillodo E, et al. Clinical applications of mobile health wearable-based sleep monitoring: systematic review. JMIR mHealth uHealth 2020;8(4):e10733.
- [102] Yin J, Xu J, Ren T-L. Recent progress in long-term sleep monitoring technology. Biosensors 2023;13(3):395.
- [103] LaRocco J, Le MD, Paeng D-G. A systemic review of available low-cost EEG headsets used for drowsiness detection. Front Neuroinf 2020;14.
- [104] Mohamed M, Mohamed N, Kim JG. Advancements in wearable EEG technology for improved home-based sleep monitoring and assessment: a review. Biosensors 2023;13(12):1019.
- [105] De Fazio R, et al. Methodologies and wearable devices to monitor biophysical parameters related to sleep dysfunctions: an overview. Micromachines 2022;13(8).
