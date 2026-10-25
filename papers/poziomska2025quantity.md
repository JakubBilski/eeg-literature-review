---
citekey: "poziomska2025quantity"
title: "Quantity versus Diversity: Influence of Data on Detecting EEG Pathology with Advanced ML Models"
authors: [Martyna Poziomska, Marian Dovgialo, Przemysław Olbratowski, Paweł Niedbalski, Paweł Ogniewski, Joanna Zych, Jacek Rogala, Jarosław Żygierewicz]
year: 2025
venue: "Neural Networks 193 (2026); read as arXiv v1 (Nov 2024)"
doi: "10.1016/j.neunet.2025.108073"
arxiv: "2411.17709"
pmid: "40946665"
field: eeg
paper_type: benchmark
task: "normal vs abnormal EEG (general pathology screening), recording level"
datasets: [TUAB, ELM19]
n_subjects:            # not reported; 2,993 TUAB + 55,787 ELM19 recordings
n_channels: 19
model_type: "random forest, Riemannian tangent space + SVC, CatBoost ensemble (GBE); EEGNet frame encoder + MIL pooling (attention, transformer); logistic-regression meta-model"
eval_protocol: "6-fold CV per dataset, folds by recording, stratified by pathology, sex (and hospital for ELM subsets); no held-out hospital"
main_metric: "AUC (mean ± SE over 6 folds)"
main_result: "meta-model AUC 88.7 on ELM19 (55,787 recordings, 39 hospitals) vs 91.7 on TUH; best single model GBE on TUH (92.2) but TransNetP on ELM19 (87.5) (Table B.5)"
code_available: false
read_depth: full
concepts: [evaluation-protocols, riemannian-methods, domain-adaptation]
---

# Quantity versus Diversity: Influence of Data on Detecting EEG Pathology with Advanced ML Models

*Read from arXiv v1 (13 Nov 2024); the Neural Networks version may differ. Authors from the University of Warsaw and Elmiko Biosignals, a Polish EEG manufacturer that supplied the data.*

## TL;DR
At equal size (~3k recordings), AUC drops from ~91 (TUH) to ~80 on a 39-hospital Polish set; growing that set to 55,787 recordings recovers it to ~87–89, with no saturation for attention/transformer MIL models. Classical gradient boosting on handcrafted features wins on small data and is overtaken only at the largest size.

## Research question
How do the quantity and the heterogeneity (pathology mix, hospitals, labelling) of clinical EEG affect normal/abnormal classifiers, classical and neural (§1, p. 2)?

## Data & preprocessing
- **TUH:** TUAB v2.0.0, 2,993 recordings, 49.2% abnormal; **87% of abnormal recordings are epileptic** (citing Obeid & Picone 2016); ages 0–90+ (§2, p. 2; p. 1).
- **ELM19:** >80,000 Elmiko recordings with Polish clinician reports, manually filtered: inconclusive reports, "no epileptic abnormalities" without other comment, "weak" abnormalities and heavy artifacts removed → 55,787 recordings from **39 hospitals**, 52.2% abnormal, only ~26% of abnormal recordings epileptic, ages 16–70 (§2, p. 3). Available "upon reasonable request" (Data availability, p. 14).
- **Subsets** (Table 1, p. 3): *SZC* = 2,993 recordings from **one** Elmiko hospital, matched to TUH in size, sex and class ratio; *ELM1/2/4/8* = 1×, 2×, 4×, 8× TUH size, stratified by hospital, sex and pathology.
- 19 channels (10-20), notch at 50/60 Hz, 0.1–40 Hz band-pass, resample 100 Hz, common average reference; 6 s frames; frames with flat lines or >800 µV dropped; recordings with <50 clean frames excluded (none in TUH) (§3.1, p. 3).

## Method
- **Classical** (§3.2–3.3.1): *RF* on 266 normalised band powers (14 bands, multitaper) + 2,394 band coherences, median over frames; *RG* = Riemannian mean covariance → tangent space (190 features) → RBF-SVC; *GBE* = all 2,850 features → 30 CatBoost models, averaged. RF, RG and siNet reproduce Gemein et al. 2020 (NeuroImage) (§3.3).
- **Neural** (§3.3.2): every network uses an EEGNet frame encoder of only **1,408 parameters** (Fig. 3).
  - *siNet:* trained per frame with the recording label, geometric mean of frame probabilities at test.
  - *Multiple-instance learning (MIL):* trained on whole recordings: *miNet* (same network, probability pooling inside training), *MINet* (attention pooling of frame features, 168k params), *TransNet* (3 transformer blocks + attention pooling, 4.7M params) (Table 2).
  - Suffix *P* = encoder first trained as siNet (supervised frame pretraining), *N* = from scratch.
- **Meta-model:** logistic regression on GBE + MINetP + TransNetP probabilities (§3.3.3).
- MIL batches use 64 random frames per recording; test uses all frames (§3.4, p. 8).

## Evaluation
- 6-fold CV per dataset: 4 train, 1 validation (early stopping / tree count), 1 test; stratified by pathology, sex, and hospital for ELM subsets (§3.4, p. 8). Folds are drawn **by recording**; patient-disjointness is not mentioned.
- AUC primary; ACC only for comparison with prior work (§3.4). Kruskal–Wallis + Conover–Iman post-hoc with FDR, called "auxiliary" (§3.5).
- Sanity check: RF, RG, siNet on TUH match Gemein et al. 2020 accuracy within one SE (82.4 / 81.3 / 82.5% vs 83.1 / 81.3 / 83.4%) (Table 3).

## Results (with locations)
- **Diversity costs ~10 AUC points at equal size.** Every model drops TUH → SZC → ELM1, e.g. GBE 92.2 → 85.4 → 81.9, META 91.7 → 86.5 → 81.8 (Table B.5); both steps significant for all models (§4.2, Figs. C.16–C.17). The authors attribute TUH → SZC to a wider pathology mix and SZC → ELM1 to multiple hospitals (p. 9).
- **Quantity recovers most of it.** ELM1 → ELM19 (2,993 → 55,787): META 81.8 → 88.7, TransNetP 79.7 → 87.5, GBE 81.9 → 86.5, RF 77.8 → 81.7 (Table B.5).
- **Models are indistinguishable on TUH** (Kruskal–Wallis, Fig. C.15a), as Gemein et al. found; differences appear only as data grows (p. 9, Fig. C.15c–g).
- **Classical vs neural:** GBE is the best single model up to ELM8 (86.2 vs TransNetP 86.0) and saturates; on ELM19 MINetP (87.0) and TransNetP (87.5) beat GBE (86.5), significantly (p. 11, Table B.5). RG (190 covariance features) beats RF (2,660 normalised spectral features), possibly because RF's features lose total power (p. 10).
- **MIL > single-frame training:** miNetN vs siNet (same network) 85.7 vs 83.5 on ELM19; attention and self-attention add more; frame-pretrained encoders help modestly (p. 11; Table B.5). On TUH all are within ~1 point.
- **Meta-model** best overall on ELM data, 88.7 on ELM19 (§4.2, Table B.5).
- **Saturation fits** (AUC = AUC∞ − αn^−β over ELM subsets): AUC∞ ≈ 91.3 ± 1.1 for META, 89.9 for TransNetP, 87.1 for GBE, 84.2 for RF; ACC∞ for META 86.0 ± 5.2%, in line with Kiessner et al.'s 85–87% on homogeneous TUH-like data (Table 4, p. 11). Reaching the asymptote within 1 SE would need ~10⁵ recordings (N_DB 71k–401k for the attention/transformer models) (Table 4, p. 13).
- Pretraining-free 4.7M-parameter TransNet trains in ≤ ~1 day on a 12 GB GPU (§3.3.2, p. 5).

## Limitations (reported)
- Medication: most patients with abnormal EEG are likely treated; models may detect drug effects, and medication data are unavailable (§5, p. 13).
- ELM19 is from one country only (§5).
- Power-law fits are "not fully rooted in fundamental principles"; predictions "to some extent, speculative" (p. 12).
- The ~91% ceiling is attributed to moderate inter-rater agreement; fuzzy multi-rater labels are proposed (§5, p. 13).

## Assessment 🤖
- 🤖 **"Diversity" here is in-distribution heterogeneity, not generalisation.** Folds are stratified by hospital, so every test hospital is also in training. No leave-hospital-out test and no train-ELM → test-TUH transfer are reported, though both datasets were at hand. The paper says nothing about performance at a *new* site, which is what [[kontras2026neuroatlas]] LODO measures (24–45% loss).
- 🤖 **Possible patient leakage.** Folds are by recording; TUAB has more recordings than patients (~2,300 people for 2,993 recordings per [[bomatter2025limited]]) and ELM19 patient IDs aren't discussed. Repeat recordings of one patient in train and test would inflate all absolute AUCs, perhaps unequally across datasets. TUH AUCs of 90–92 sit above the TUAB literature (e.g. LaBraM AUROC 0.92 on the patient-disjoint eval set, [[jiang2024large]]), which is consistent with, but not proof of, leakage.
  - 🤖 **Leakage, if present, would grow with subset size.** ELM1–ELM8 are random draws from one pool. The bigger the draw, the more likely a patient's other recordings fall into the same subset and so across folds. Part of the quantity curve could then be growing leakage, and identity-memorising models would gain most. The TUH-vs-SZC comparison is also exposed, since both may contain repeat patients at unknown rates.
- 🤖 **The TUH → SZC → ELM1 drop has several confounds the paper can't separate:** label source (TUH team vs Polish reports filtered by the authors), pathology mix (87% vs 26% epileptic), age range (0–90+ vs 16–70), country and power-line frequency. "Pathology diversity" for TUH → SZC is one plausible reason among these.
- 🤖 **Recordings ≠ people ≠ hospitals.** The quantity axis grows recordings while holding the hospital mix fixed; how many distinct patients each subset has is not stated, so it can't be compared directly with [[bomatter2025limited]]'s people axis. Both point the same way: for one-label-per-recording screening, more labelled cases keep helping into the thousands–tens of thousands.
- 🤖 **The "quantity compensates diversity" claim is an extrapolation** from 5 points over ~1 decade (3k–56k), landing on AUC∞ 91.3 ± 1.1, coincidentally the TUH level. The authors flag it as speculative. N_DB estimates span 71k–2.1M.
- 🤖 **Strong classical baseline lesson (Q7):** a CatBoost ensemble on band power + coherence + covariance features ties or beats all networks up to ~24k recordings and loses by ~1 AUC point at 56k. FM papers that skip such a baseline on TUAB are missing the hardest comparison.
- 🤖 **MIL matters only under heterogeneity:** label-inheritance training (siNet) is fine on TUH but costs ~2 AUC on ELM19. That fits the idea that frame-level label noise hurts more when abnormalities are rarer and less stereotyped than epileptiform discharges. It also means TUAB window-level FM benchmarks may understate what recording-level models do on diverse data.
- 🤖 Model size grows only to 4.7M and the gain keeps going at 56k recordings; supports "small supervised models are still data-limited" rather than "capacity-limited" in this regime.
- 🤖 §3.4 says "mean and standard deviation" over folds, Table B.5 says "standard errors"; the ± values are ambiguous.
- 🤖 Data-provider authors and a dataset available on request: "largest publicly available" means available on request, not open download.

## Concepts
- [[evaluation-protocols]] — recording-level random folds stratified by hospital; no site hold-out; patient-disjointness unstated.
- [[riemannian-methods]] — tangent-space covariance features + SVC (RG) as a classical baseline; beats spectral RF.
- [[classical-ml-baselines]] (topic) — GBE (CatBoost on handcrafted features) is the best single model up to ~24k recordings.
- [[domain-adaptation]] — multi-hospital heterogeneity handled only by pooling more data, no adaptation.

## Related papers
- [[bomatter2025limited]] — same task family; people vs segments per person on TUAB. Here: recordings at fixed hospital mix. Both find quantity of labelled cases dominates for screening.
- [[kiessner2024reaching]] — TUH-like homogeneous scaling, ACC ceiling 85–87%; matched here by META's ACC∞ 86% (p. 11). *(screening)*
- [[kiessner2023extended]] — 15,300 automatically labelled TUH recordings, the homogeneous scale-up. *(screening)*
- Gemein et al. 2020, "Machine-learning-based diagnostics of EEG pathology" (NeuroImage 220) — reproduced baselines (RF, RG, BD-EEGNet); pre-2022, not in vault.
- [[kontras2026neuroatlas]] — measures the site-transfer question this paper leaves out (LODO).
- [[oliveira2026scaling]] — subject vs trial scaling with loss fits; TUAB subject-dominated.
- [[lawhern2018eegnet]] — the frame encoder used by every network here.
- [[jiang2024large]] — TUAB benchmark numbers on the patient-disjoint split, for comparison.

## Q&A notes
- 2026-10-25 **Q:** They had hospital labels for 39 sites but no leave-one-hospital-out test, and the folds may leak patients. Does that invalidate all findings? **A:** 🤖 No. It invalidates the generalisation reading and weakens the quantity claim, but the findings differ in how exposed they are.
  - *Not reported, rather than shown to leak:* the paper never mentions patient IDs (§3.4). TUH v2.0.0 has a patient-disjoint official split that they pooled and re-split by recording. The ELM19 anonymisation (CRediT, p. 14) may not have kept patient IDs at all; this is unverified, so ask the authors or check the Neural Networks version.
  - *No hospital hold-out:* in-distribution claims stand ("on a pooled multi-site set, more data helps"). Claims about robustness for new hospitals, which motivate the paper (§1, p. 2), aren't tested. This mismatch between motivation and test is the main flaw.
  - *Most robust:* the TUH reproduction of Gemein (Table 3), all models tying on TUH, and the sign of the heterogeneity drop at equal size (~10 AUC; leakage would need to differ hugely between TUH and ELM1 to create it).
  - *Moderately exposed:* model rankings. All models share the folds, but a model that can memorise patient identity profits more from leakage.
  - *Most exposed:* the quantity curve, the "quantity compensates diversity" claim and the AUC∞/N_DB fits. Leakage would rise with subset size (Assessment).
  - *Follow-up (2026-10-25): can parts of one recording be in train and test? Do transformers win by memorising IDs?*
    - **Same recording: no.** The unit of the folds is the recording, frames are cut after that, and test AUC is computed on whole held-out recordings (§3.4, p. 8). Window-level leakage is ruled out by design.
    - **Hospital:** every hospital is in both train and test by design. Any model can use a hospital fingerprint (device, filters, montage habits) as a prior if abnormal rates differ by hospital (not reported). Classical features keep total power and covariance (p. 10), so they can carry fingerprints too.
    - **Patient memorisation as the reason transformers overtake:** plausible, not shown. Against it as the whole story: the 1.7k-parameter miNet nearly matches GBE on ELM19 (85.7 vs 86.5), and the 168k MINet beats it (87.0) (Table B.5). These models are too small to memorise thousands of patients. Repeat recordings of one person are similar anyway, so tree ensembles can exploit them just as well. For it: transformers gain most at the largest subset, where leakage would be highest.
    - **Decisive test:** rerun each model with patient-grouped folds and compare the drop per model. If the transformer loses more than GBE, the crossover was partly identity; also probe how well the hospital can be decoded from each model's embeddings.
  - *Openness (asked 2026-10-25):* ELM19 is "available ... upon reasonable request" by email to Elmiko (Data availability, p. 14), with no licence, DUA terms, patient IDs or per-hospital metadata described. Yet the paper calls it "the largest publicly available" (Abstract) / "publicly accessible EEG corpus for pathology detection" (p. 3). No code link anywhere in the arXiv text. Hyperparameters are given in footnotes 6, 8, 10 and 14 (pp. 5, 8). 🤖 Not open data and not open code, so the leakage and hospital questions above can't be checked independently without the company's cooperation.
  - **Questions for the authors (the human will meet them, 2026-10-25):**
    1. Were folds patient-disjoint? Does ELM19 keep patient IDs, and how many recordings per patient (TUH and ELM)?
    2. Why no leave-one-hospital-out or ELM → TUH test? How are recordings spread across the 39 hospitals, and how do abnormal rates differ by hospital?
    3. Does the shared ELM19 include patient IDs, hospital IDs, the per-recording report text, and the fold assignments? Is code available? Under what terms is it shared?
    4. Does the Neural Networks version change any of this compared with arXiv v1?
    5. Is medication recorded anywhere in the reports (§5 says no reliable data)?
  - *Fix:* group folds by patient, then leave-one-hospital-out (or leave-k-hospitals-out for small sites), plus ELM → TUH transfer. ELM19 is on request, so this is runnable if patient IDs exist.
