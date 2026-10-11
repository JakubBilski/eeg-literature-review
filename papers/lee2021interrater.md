---
citekey: lee2021interrater
title: "Interrater reliability of sleep stage scoring: a meta-analysis"
authors: [Yun Ji Lee, Jae Yong Lee, Jae Hoon Cho, Ji Ho Choi]
year: 2022
venue: "Journal of Clinical Sleep Medicine 18(1):193–202 (online 2021)"
doi: "10.5664/jcsm.9538"
arxiv: ""
pmid: "34310277"
field: eeg
paper_type: review
task: "inter-scorer agreement of manual PSG sleep staging (R&K and AASM rules)"
datasets: []
n_subjects: ""
n_channels: ""
model_type: ""
eval_protocol: "meta-analysis of human scorer pairs scoring the same PSG"
main_metric: "Cohen's kappa"
main_result: "pooled κ 0.76 overall (95% CI 0.71–0.81); W 0.70, N1 0.24, N2 0.57, N3 0.57, REM 0.69 (Abstract)"
code_available: ""
read_depth: abstract
concepts: [sleep-staging, evaluation-protocols]
---

# Interrater reliability of sleep stage scoring: a meta-analysis (Lee et al., 2022)

## TL;DR
Two trained humans scoring the same sleep recording agree "substantially" overall (κ 0.76), but only fairly on N1 (κ 0.24) and moderately on N2 and N3 (κ 0.57). This is the ceiling for any wearable or model judged against human labels.

*Written from the PubMed abstract only. Open access in PMC (PMC8807917), so a full read is possible.*

## Research question
How well do human scorers agree when manually staging polysomnography, overall and per stage? (Abstract)

## Data & preprocessing
- Searched PubMed, OVID Medline, EMBASE, Cochrane, KoreaMed, KISS and MedRIC. Studies using R&K or AASM rules were included; automatic scoring and paediatric patients were excluded (Abstract).
- 101 publications retrieved, 11 included (Abstract).

## Method
- Pooled Cohen's κ, overall and per stage. Extracted scorer histories, scoring rules, number of epochs and patients' underlying diseases (Abstract).

## Results (with locations)
- Overall κ 0.76 (95% CI 0.71–0.81) (Abstract).
- Per stage: Wake 0.70, N1 0.24, N2 0.57, N3 0.57, REM 0.69 (Abstract).
- The authors call this "substantial" overall, "moderate" for N2/N3 and "only fair" for N1 (Abstract).

## Limitations (reported)
- Abstract only: limitations not read yet.

## Assessment 🤖
- 🤖 Device and model numbers fall in the same range. Wearables vs PSG reach κ 0.42–0.79 overall ([[gans2024sleep]] Table 1), and PSG models on ISRUC reach κ 0.70–0.74 ([[wang2024cbramod]] Table 7). A κ near 0.75 is roughly what two human experts achieve. Studies, populations and rules differ, so this is a range check, not a matched comparison.
- 🤖 Some device N1 κ values exceed the pooled human N1 κ (Dreem 0.43, [[gans2024sleep]] p. 4). That shows how weak N1 labels are; it doesn't mean the device is better than humans.
- 🤖 Per-stage κ is lower than overall κ, presumably because the overall figure is dominated by the large, easy classes (N2, Wake). To check in the full text.

## Concepts
- [[sleep-staging]]: human inter-scorer agreement, i.e. how well defined the stages are in practice.
- [[evaluation-protocols]]: label noise sets a ceiling on any reported score.

## Related papers
- [[gans2024sleep]]: cites this paper (ref [96]) for the claim that manual scoring varies by technician (p. 10).
- [[wang2024cbramod]]: its ISRUC sleep benchmark uses expert AASM labels (App. E.1). Which scorer's labels it used is not stated in the vault notes.

## Q&A notes
