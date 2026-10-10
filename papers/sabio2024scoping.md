---
citekey: sabio2024scoping
title: "A scoping review on the use of consumer-grade EEG devices for research"
authors: [Joshua Sabio, Nikolas Williams, Genevieve M. McArthur, Nicholas A. Badcock]
year: 2024
venue: "PLoS ONE"
doi: "10.1371/journal.pone.0291186"
arxiv: ""
pmid: "38446762"
field: eeg
paper_type: review
task: "scoping review: research use of consumer-grade EEG devices"
datasets: []
n_subjects: ""
n_channels: "1–16 (devices reviewed)"
model_type: ""
eval_protocol: ""
main_metric: ""
main_result: "916 studies (531 journal, 385 conference); Emotiv used in 67.69% (Abstract; §Consumer-grade EEG devices)"
code_available: ""
read_depth: full
concepts: [consumer-grade-eeg-devices, signal-quality-and-noise, channel-heterogeneity, electrode-types]
---

# Consumer-grade EEG devices in research: scoping review (Sabio et al., 2024)

## TL;DR
A PRISMA-ScR scoping review of 916 studies (2010–May 2022) that used five consumer EEG brands. Emotiv dominates; BCI is the most common use. Validation evidence is thin for most devices other than Emotiv.

*Locations: the Europe PMC XML has no section numbers, so locations are section headings (§…) and tables.*

## Research question
How widely, for what research purposes, and where have consumer-grade EEG devices been used? (§Step 1)

## Data & preprocessing
- Searched PsycINFO, MEDLINE, Embase, Web of Science and IEEE Xplore for 2010 onward, human subjects, English, in April–May 2022 (§Stage 2; §Stage 3).
- Search strings for 5 brands: Emotiv, interaXon Muse, MyndPlay Mindband, NeuroSky MindWave, OpenBCI (Table 2).
- 1260 records → minus 265 duplicates → minus 79 excluded → **916 included** (531 journal + 385 conference) (§Stage 3, Fig. 1).
- Charted: device, usage category, first author's country, year (§Stage 4).

## Method
Five-stage scoping-review framework under PRISMA-ScR. Studies were categorized into 5 non-exclusive usage categories, with a joint author decision when ambiguous (§Method and results; §Research domains).

## Evaluation
Not applicable (descriptive charting; no quality appraisal by design) (§Introduction, last para).

## Results (with locations)
- **Device share:** Emotiv 67.69%, NeuroSky 24.56%, OpenBCI + Muse + MyndPlay together 7.75% (§Consumer-grade EEG devices).
- **Specs (Table 3):**
  - Emotiv EPOC+/EPOC-X: 14 ch, 128 or 256 Hz, 14-bit. Emotiv Insight: 5 ch.
  - OpenBCI Ganglion 4 ch / 200 Hz; Cyton 8 ch / 250 Hz; Cyton-Daisy 16 ch / 125 Hz; all 24-bit.
  - Muse 2: 4 ch (AF7, AF8, TP9, TP10), 256 Hz.
  - NeuroSky MindWave: 1 ch (FP1), 512 Hz. MyndPlay: 1 ch, 512 Hz.
- **Consumer vs research grade:** research systems have "dozens of electrodes" with saline or gel; consumer devices have fewer electrodes and "minimal or no conductive medium" (§Consumer-grade EEG devices).
- **Usage:** BCI 44.54% · experimental research 31.22% · signal processing 12.01% · clinical 6.22% · validation 6.18% (§Research domains).
- BCI paradigms: SSVEP, P300 (spellers) and motor imagery (wheelchairs, prostheses, drones) (§Research domains, BCI).
- **Validation:**
  - Emotiv records research-grade ERPs (N170, P100–P300, N200/P300) comparably to Neuroscan, but has a significantly higher noise floor (Grummett), more rejected trials (Barham), poor functional connectivity (Mahdid), and is sensitive to fit.
  - OpenBCI shows negligible differences from g.USBamp (one study).
  - **No validation studies** were found for Muse or Mindband (§Validation).
- Publications peaked in 2018 and dropped in 2020–21, which the authors attribute to COVID (§Discussion).
- 83 countries; top two are India 9.72% and the US 8.73% (§Research location).

## Limitations (reported)
- Only five databases, English only; devices referred to by other names would be missed (§Discussion, last para).
- A scoping review doesn't critically appraise studies (§Discussion, last para).

## Assessment 🤖
- 🤖 **Inconsistent wording:** the Discussion and Table 5 say Emotiv has a "low noise floor", but the Validation section reports a significantly *higher* noise floor. The intended meaning is almost certainly "noisy" (a high noise floor).
- 🤖 The share percentages reflect the 5-brand search design (Table 2), not the market or the full device landscape. Ear-EEG, dry-electrode research systems and newer wearables are out of scope, so see [[kaongoen2023future]] and [[niso2022wireless]].
- 🤖 Counts aren't weighted by quality. "916 studies" shows popularity, not validity.
- 🤖 Implication for ML: 1–16-channel consumer data is a very different input from 19–64-channel clinical or research caps. That gap is the practical case for montage-agnostic models ([[channel-heterogeneity]], [[jiang2024large]]).

## Concepts
- [[consumer-grade-eeg-devices]]: the review's subject.
- [[signal-quality-and-noise]]: validation evidence on noise floor and trial rejection.
- [[channel-heterogeneity]]: 1–16 channels at non-standard positions.
- [[electrode-types]]: consumer headsets use "minimal or no conductive medium" (§Consumer-grade EEG devices).

## Related papers
- [[niso2022wireless]]: broader survey: 48 wireless devices (consumer, research and medical) and 110 high-impact studies. Also finds Emotiv the most used (25%, Fig. 6a).
- [[kaongoen2023future]]: ear-EEG, a wearable form factor not covered here. *(seed; needs manual download)*
- [[gans2024sleep]]: EEG wearables for sleep. *(seed; needs manual download)*
- [[chaddad2023electroencephalography]]: briefer mention of the same consumer devices (Emotiv EPOC, Muse) (§2.1).

## Q&A notes
