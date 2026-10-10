---
citekey: "{{title}}"
title: ""
authors: []
year:
venue: ""
doi: ""
arxiv: ""
pmid: ""
field: eeg            # eeg | ecg | mi | other
task: ""              # e.g. motor imagery classification, sleep staging, seizure detection
datasets: []
n_subjects:
n_channels:
model_type: ""        # e.g. transformer, CNN, masked autoencoder
eval_protocol: ""     # e.g. cross-subject / within-subject / leave-one-dataset-out
main_metric: ""
main_result: ""       # number + dataset + location, e.g. "0.81 bal. acc. on TUAB (Table 3)"
code_available:       # true | false | URL
read_depth: abstract  # abstract | full
concepts: []          # concept slugs, e.g. [masked-pretraining, linear-probing]
---

# {{title}}

## TL;DR
<!-- 2 lines max -->

## Research question

## Data & preprocessing
<!-- datasets, subjects, channels, sampling rate, filtering, epoching, artifact handling — each with location -->

## Method

## Evaluation
<!-- splits, protocol (cross-/within-subject), baselines, metrics -->

## Results (with locations)
<!-- every number gets (Table N) / (§N) / (p. N) -->

## Limitations (reported)

## Assessment 🤖
<!-- interpretation and critique; mark each point 🤖 so the human can review it -->

## Concepts
<!-- [[concept-slug]] — how this paper uses it -->

## Related papers
<!-- [[citekey]] — one line on the relationship -->
