---
citekey: niso2022wireless
title: "Wireless EEG: A survey of systems and studies"
authors: [Guiomar Niso, Elena Romero, Jeremy T. Moreau, Alvaro Araujo, Laurens R. Krol]
year: 2022
venue: "NeuroImage 269 (2023) 119774"
doi: "10.1016/j.neuroimage.2022.119774"
arxiv: ""
pmid: "36566924"
field: eeg
paper_type: review
task: "survey: wireless EEG hardware (48 devices) and its research use (110 studies)"
datasets: []
n_subjects: ""
n_channels: "1–264 across reviewed studies (median 14); devices 4–128"
model_type: ""
eval_protocol: ""
main_metric: ""
main_result: "48 devices compared on ~35 specs (Table 1); 110 high-impact studies: cognitive monitoring 44%, clinical 24%, methodological 22%, control/communication 10% (Fig. 7a)"
code_available: ""
read_depth: full
concepts: [consumer-grade-eeg-devices, electrode-types, signal-quality-and-noise, channel-heterogeneity, bci-paradigms, digital-filtering, eeg-preprocessing-pipeline, sleep-staging, seizure-detection]
---

# Wireless EEG: a survey of systems and studies (Niso et al., 2022)

## TL;DR
A buyer's guide plus literature survey. It explains what each spec of a wireless EEG device means and compares 48 devices on them (Table 1). It then charts how 110 high-impact studies used such devices: mostly for cognitive monitoring, and mostly with participants sitting still.

*Online Dec 2022, volume dated 2023. Table 1 has no text layer; a transcription of selected columns is at the end of `fulltext/niso2022wireless.md`.*

## Research question
What wireless EEG hardware exists, how do the devices compare, and what has it been used for? Aimed mainly at newcomers to EEG (p. 2).

## Data & preprocessing
- **Definition:** "wireless EEG" = any device supporting a wireless acquisition protocol. This covers mobile, portable, wearable and "transparent" EEG (the Bleichner & Debener 2017 categories) (p. 2).
  - mobile = tolerates movement; portable = can be carried; wearable = portable + self-applied; transparent = all of these + near-invisible (p. 2).
- **Devices:** taken from the studies below plus a web search for vendors. Missing specs were requested from manufacturers, and some answers could not be obtained or standardised (p. 3).
- **Studies:** PubMed search, March 2022, EEG terms × {wireless, mobile, portable, wearable, ambulatory}, no animal studies, up to 2021 (p. 9).
  - Kept journal papers with ≥10 citations/year. Dropped reviews, method/hardware papers without data, and papers that didn't report the system (p. 9).
  - 2137 hits → 110 papers (§4.1, Fig. 4).
  - Coded per paper: topic, device, channel count, sample size, CoME participant-mobility score (p. 9).

## Method
- Section 3 explains each column of Table 1 (pp. 3–9):
  - **Channels and coverage:** ≥32 channels is the usual minimum for broad coverage in lab research; high-density EEG goes up to 256. Few sites can suffice when the relevant region is known, e.g. occipital for vision, central for motor (§3.2).
  - **Reference:** subtracted from every other channel. Its contact must hold for the whole recording, so it sometimes gets gel when the other electrodes don't (§3.2).
  - **Electrode type:** gel / wet (saline sponge) / dry, and active / passive / shielded (§3.4–3.5). → [[electrode-types]]
  - **Impedance check:** before the recording only, on request, or continuous. Dry-electrode devices more often monitor it continuously (§3.6).
  - **Amplifier:** input range, input impedance, input noise, CMRR (§3.7).
  - **Sampling rate:** activity of interest is "generally being up to around 50 Hz", so 250 or 500 Hz is common. A few devices exceed 1000 Hz, up to 8000 Hz (§3.8).
  - **Resolution:** 12–24 bit in the table, and even 12 bit is enough for most uses. EEG is hard to compress, so more bits cost energy and wireless bandwidth (§3.9).
  - **Wireless protocol:** Bluetooth/BLE reaches 5–10 m indoors, Wi-Fi 10–20 m. All share the crowded 2.4 GHz band, and the wearer's own body can block the line of sight (§3.11).
  - **Formats and streaming:** all but two vendors export a BIDS-recommended format (EDF, BDF, BrainVision) (§3.12). Lab Streaming Layer (LSL) is "the main standard" for real-time access (§3.13).
  - **CoME scores** (Bateson 2017): device mobility 0–5, system spec 4–20, participant mobility 0 (still) to 5 (unconstrained sport) (§3.14).
  - **Certification and price:** medical certification (FDA/EMA) is required for clinical research (§3.15). Price is mostly by quote and roughly tracks channel count (§3.16).

## Evaluation
- Descriptive only. No signal-quality benchmark: the authors say quality depends too much on the study to put in a table (p. 13).

## Results (with locations)
- **Device landscape (Table 1, p. 4):** 48 entries from 18 companies, from 4 channels (Muse, Ganglion, NeXus-10) to 128 (ANT eego sports, CGX Mobile).
  - Sampling rates run from 128 Hz (Emotiv) to 2048 Hz (ANT eego, NeXus-10).
  - Prices run from <0.5 k€ (Muse, Emotiv INSIGHT) to 45–60 k€ (CGX Mobile, 128 ch).
  - Lightest device: Mentalab Explore, 27 g, 8 ch, 40×40×20 mm (§3.10).
- **Literature volume:** wireless-EEG papers grow rapidly, mostly over the last ten years, peaking in 2021 (§4.1, Fig. 5a). The earliest hit is a 1975 4-channel cassette recorder for 24 h ambulatory monitoring (§4.1).
- **Sample size:** median 18 participants, and 25/110 studies had <10 (§4.1, Fig. 5b). The outlier is 6029 people recorded with a 4-channel Muse (Hashemi 2016) (§4.1).
- **Channels:** median 14. 37 studies used <8 channels and 11 used a single channel (§4.1, Fig. 5c).
- **Devices used (n = 69):** Emotiv 25%, home-made 19%, mBrainTrain 10%; InteraXon, NeuroSky, g.tec and ANT Neuro 7% each (Fig. 6a, p. 11).
  - Home-made devices are rarely tested on moving participants. ANT Neuro shows up only in mobile studies (p. 11).
- **Applications (n = 110):** cognitive monitoring 44.1%, clinical 24.3%, methodological 21.6%, communication and control 9.9% (§4.2, Fig. 7a).
- **Mobility is rare:** 40% of studies scored 1 on participant mobility (sitting, localized movement), 21% scored 0, 19% scored 2 (constrained walking), 19% scored 3 (unconstrained walking), 3% scored 4, none scored 5 (§4.2, Fig. 7d).
  - Only 43 studies (39%) had mobility ≥2 (p. 11).
- **Mobile studies favour cognitive monitoring:** it accounts for 60% of mobile studies, 73% once methodological papers are excluded (§4.2.1).
  - Clinical studies drop from 24.3% overall to 11.6% of mobile ones (§4.2.2).
- **What the categories contain:**
  - Cognitive monitoring: attention is the most studied state (oddball/P300 while cycling or walking; classrooms; driving), plus emotion and workload (§4.2.1).
  - Clinical: mainly seizure detection and sleep staging at home; also exoskeleton rehabilitation after stroke (§4.2.2; p. 14).
  - Control: SSVEP, motor imagery and P300, mostly for games and robots (§4.2.3; p. 14).
- **Reporting:** "a high degree of variability and omissions" in reported methods, which makes meta-analysis hard. The authors recommend COBIDAS and ARTEM-IS (p. 14).

## Limitations (reported)
- The device list is unlikely to be complete. Some specs are self-reported by vendors, and some answers did not match the questions asked (p. 13).
- Selecting by citations/year is "admittedly imperfect" and disadvantages 2021 papers (pp. 13–14).
- Keyword choice follows the authors' own definition of wireless EEG (p. 13).
- There is no signal-quality comparison. The authors suggest extending ERP CORE paradigms to sitting, standing and walking with a standardized measurement error metric (p. 13).

## Assessment 🤖
- 🤖 The paper's value is as a glossary for device spec sheets (§3) plus a snapshot of who uses what. It is not evidence about signal quality: nothing is measured.
- 🤖 By my count from the Table 1 transcription, 11 of 48 entries are medically certified and 15 are dry-only. All but one of the dry-only devices use fixed headsets, which suggests that dry electrodes and fixed form factors go together.
- 🤖 Its device-usage figures broadly agree with [[sabio2024scoping]] (Emotiv first). Its 19% home-made share is a reminder that much "wearable EEG" research is hardware prototyping.
- 🤖 For ML: the usual 250–500 Hz sampling and the ≤50 Hz band of interest explain why foundation models resample to 200–256 Hz. The median of 14 channels shows how far wearable data sit from 19-channel 10-20 pretraining corpora (→ [[channel-heterogeneity]]).
- 🤖 "Wireless" here is mostly a convenience feature: 61% of studies had participants who barely moved (Fig. 7d).

## Concepts
- [[seizure-detection]]: at-home seizure monitoring is one of the two main clinical uses of wireless EEG (§4.2.2).
- [[digital-filtering]]: dry-electrode drift below 2 Hz forces higher high-pass cut-offs (p. 6); sampling 250–500 Hz (§3.8).
- [[eeg-preprocessing-pipeline]]: acquisition side: sampling, reference, impedance (§3).
- [[bci-paradigms]]: SSVEP, motor imagery and P300 are the control paradigms in the 10% of wireless studies on communication and control (§4.2.3).
- [[consumer-grade-eeg-devices]]: covers the whole spectrum from <0.5 k€ consumer headsets to 128-channel research and medical wireless systems.
- [[electrode-types]]: gel vs wet vs dry and active vs passive trade-offs (§3.4–3.5).
- [[signal-quality-and-noise]]: motion artifacts increase with mobility and can be confounded with the experimental condition (p. 3). Covers impedance monitoring and CMRR (§3.6–3.7).
- [[sleep-staging]]: at-home sleep staging is one of the main clinical uses of wireless EEG (§4.2.2).
- [[channel-heterogeneity]]: device channel counts span 4–128 and study channel counts 1–264 (median 14) (Table 1, Fig. 5c).

## Related papers
- [[sabio2024scoping]]: narrower (5 consumer brands, 916 studies) but agrees that Emotiv dominates. Niso covers research and medical wireless systems too.
- [[chaddad2023electroencephalography]]: names the lab-vs-portable trade-off (§2.1) that Niso details spec by spec.
- [[kaongoen2023future]]: ear-EEG. Niso mentions cEEGrid behind-the-ear electrodes, often used with mBrainTrain amplifiers (p. 11). *(not yet read)*
- [[varbu2022past]]: BCI applications 2009–2019. Agrees that monitoring dominates and Emotiv is the top device (40% of BCI device mentions). Application-centric where Niso is device-centric.
- [[gans2024sleep]]: sleep wearables, 24 validated against PSG. It supplies the per-device validation evidence for the home sleep staging that Niso lists as a main clinical use (§4.2.2).
- [[wong2023eeg]]: the public seizure datasets behind seizure-detection ML. All come from clinical gel or implanted systems; none are wearable.

## Q&A notes
- 2026-10-10 **Q:** Why has no one compared signal quality across devices? **A:** Pairwise validations exist; what's missing is a standardized protocol. Quality depends on the task (p. 13), there is no ground truth, setup and fit matter, and public datasets confound device with lab and task. → [[q2-measuring-devices]]
