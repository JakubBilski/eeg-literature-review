---
slug: "2026-10-29-poziomska-authors"
date: 2026-10-29
status: upcoming
people: []            # which of the 8 authors attend: fill in after
papers: [poziomska2025quantity]
questions: [q6, q7, q9]
updated: 2026-10-29
---

# 2026-10-29 · meeting with authors of *Quantity versus Diversity* (2025)

## Context
- Paper: [[poziomska2025quantity]], University of Warsaw + Elmiko Biosignals (Polish EEG manufacturer that supplied the data). Normal vs abnormal EEG on TUH (2,993 recordings) vs ELM19 (55,787 recordings, 39 hospitals). The paper note has full numbers and the 🤖 critique; the 2026-10-25 Q&A there covers the leakage and hospital-hold-out analysis these questions rest on.
- The data itself (size of the next release, metadata, access terms) is a **separate discussion** and is left out here. 🤖 If it comes up: ELM19 is counted in *recordings*, not patients (§2, p. 3), so check which unit the "more than 60k" figure uses.
- Web check (2026-10-29): no public announcement of an expanded release or a follow-up paper found. The 2026 Neural Networks version (doi 10.1016/j.neunet.2025.108073) was not compared with arXiv v1.
- 🤖 Framing: the paper is one of the few in the vault that pairs a **strong classical baseline** with a **real quantity axis** on clinical EEG. Present the critique as a request, not an accusation: "we'd love to see…".

## Questions (priority order)

### 1. Why no leave-one-hospital-out test?
- **Ask:** "Folds were stratified by hospital, so every test hospital was also in training. Did you try leave-one-hospital-out, or train on ELM and test on TUH? If so, how big was the drop?"
- **Follow-ups:** How are recordings spread across the 39 hospitals (largest hospital's share; how many tiny ones)? Do abnormal rates differ by hospital? Can the hospital be decoded from the features or embeddings?
- **Why:** the paper is motivated by robustness at new sites (§1, p. 2) but tests only pooled, in-distribution heterogeneity. The only cross-cohort number in the vault is NeuroAtlas LODO, a 24–45% loss [[kontras2026neuroatlas]]. A site fingerprint plus differing abnormal rates per hospital would be a shortcut that both GBE and the networks can use ([[poziomska2025quantity]] Q&A).
- **Answer → change:** a small LOHO drop would make ELM19 the strongest evidence in [[q6-reliability-of-eeg-diagnoses]] that multi-site clinical EEG generalises; a large drop would make "quantity compensates diversity" an in-distribution claim only.

### 2. EEG benchmarks are saturated: which tasks are worth pursuing with your data?
- **Ask:** "Two of the most used clinical-style benchmarks seem capped by expert agreement rather than by models: sleep staging, where models reach human–human κ, and normal/abnormal, where your own fit and Kiessner's land on the same ceiling, ~86% accuracy / AUC ~91. Beyond those, the open benchmarks that are 'solved' look easy rather than capped (SSVEP, Bonn seizures, single-site depression). Given that, which tasks would you pursue with the data you have, where a better model could still show up as a better score?"
- **Prompts if the conversation needs them:**
  - Do you think the ~91 ceiling is really agreement? Do you have any recordings read by two doctors to measure it?
  - Finer labels from the reports: abnormality type (focal vs generalised slowing, epileptiform discharges), location, severity; the ~25k reports filtered out as inconclusive or weak.
  - Labels not read from the same EEG: later diagnosis, outcome, repeat visits of one patient over years. Age as an objective target (brain-age gap)?
- **Why:** [[q7-foundation-models-vs-baselines]] *Saturated, noisy, or headroom?*: sleep and TUAB are at their label ceiling, so they rank foundation models poorly. Headroom shows up only where the person-to-person shift dominates (cross-subject BCI, seizures). [[eeg-labels-and-metadata]] *Is the field missing a good downstream task?*: no common task has an objective label, clinical meaning, headroom and enough test subjects at once. Outcome-type labels exist elsewhere: cardiac arrest ([[turella2024predictive]]) and HEEDB's ICD-10 codes ([[sun2025harvard]]).
- 🤖 Accuracy of the premise: only sleep has a measured agreement cap in the vault (κ 0.76, [[lee2021interrater]]). For normal/abnormal the cap is a fitted plateau that the authors *attribute* to agreement (§5, p. 13); agreement itself is not measured. The other saturated tasks are easy or tiny, not agreement-capped. Saying it this way invites them to confirm or correct the TUAB part.
- **Answer → change:** a measured agreement number fills the "?" in the TUAB row of the [[eeg-labels-and-metadata]] table; a task they name with headroom becomes a candidate benchmark for Q7.

### 3. What could your data test that TUH can't?
*One merged question; pick the thread that fits the conversation.*
- **Ask:** "With patients, hospitals and reports in one corpus, several things become testable that TUH can't answer. Which of these do you plan, or would you consider?"
  - **Patient-grouped evaluation:** were folds split by patient, and do patient IDs exist? Leakage, if present, grows with subset size, so it would inflate the quantity curve and the AUC∞ / N_DB fits most ([[poziomska2025quantity]] Assessment). TUH AUCs of 90–92 sit at or above patient-disjoint TUAB results (LaBraM 0.92 [[jiang2024large]], CBraMod 0.923 [[wang2024cbramod]]). The decisive rerun: patient-grouped folds, then LOHO, comparing the drop per model (does the transformer lose more than GBE?).
  - **Separate scaling axes:** the quantity curve with the axis in *patients*, and in *number of hospitals at fixed N* tested on held-out hospitals. People, not data per person, drive one-label-per-person diagnosis on TUAB ([[bomatter2025limited]]; [[oliveira2026scaling]]); varying hospitals at fixed N is the clean version of the paper's own diversity question. Our [[subject-diversity-gap]] asks the same at a much smaller scale, without hospital labels.
  - **Foundation models vs your baselines:** self-supervised pretraining on the full corpus, or existing EEG FMs (LaBraM, CBraMod, REVE) with MIL heads, against GBE at matched labelled N, under LOHO. The FM TUAB numbers in the vault use the official TUAB split, with no recording-level MIL head and no feature-ensemble baseline ([[q7-foundation-models-vs-baselines]]). One manufacturer's devices across 39 hospitals would also separate *site* from *device* effects, which TUEG-pretrained FMs can't.
  - **A public benchmark:** a hidden, hospital-held-out test split as a successor to TUAB.
- 🤖 Order of importance if time is short: patient grouping (it qualifies every number) > hospitals-at-fixed-N (their own question, done properly) > FMs.

## Backup questions
- **Version:** does the Neural Networks version change the protocol (folds, patient grouping, extra tests) compared with arXiv v1?
- **Ambiguity:** are the ± values in Table B.5 SDs or SEs? §3.4 and the table disagree.
- **Medication:** is it mentioned in reports often enough to stratify, even roughly (§5)?
- **Confounds TUH → SZC:** can they separate label source, pathology mix (87% vs ~26% epileptic), age range and line frequency? For example, SZC restricted to epileptic abnormals vs TUH.
- **Interpretability:** do the attention weights of MINet/TransNet land on the segments the report describes?
  - **Report text as training signal:** EEG-CLIP-style pretraining aligns recordings with their report text; on TUAB (~2.8k reports) frozen features ≈ supervised on pathology ([[ndir2025eeg]] Table 3). With ~56k reports in Polish, would they try it, and is the report text kept per recording? 🤖 Added 2026-10-29 after reading EEG-CLIP.
- **Ceiling extrapolation:** with more data, will they test the N_DB ≈ 10⁵ prediction (Table 4) out of sample? A pre-registered check of their own power law would be strong evidence either way.

## Notes from the meeting
<!-- fill after the meeting; then file each answer: evaluation answers → [[poziomska2025quantity]] Q&A; ceilings and tasks → [[eeg-labels-and-metadata]] / [[q7-foundation-models-vs-baselines]]; scaling → [[q9-pretraining-objectives-and-scale]] -->
