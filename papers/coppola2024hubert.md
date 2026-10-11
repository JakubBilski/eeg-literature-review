---
citekey: coppola2024hubert
title: "HuBERT-ECG as a self-supervised foundation model for broad and scalable cardiac applications"
authors: [Edoardo Coppola, Mattia Savardi, Mauro Massussi, Marianna Adamo, Marco Metra, Alberto Signoroni]
year: 2024
venue: "medRxiv (preprint, v4 posted 2026-06-01)"
doi: "10.1101/2024.11.14.24317328"
arxiv: ""
pmid: ""
field: other
paper_type: method
task: "12-lead ECG foundation model: rhythm/conduction diagnosis, echo-derived structural findings, prognosis (mortality, ICU), demographics, single-lead transfer"
datasets: [CODE/Ribeiro, PTB-XL, PTB, CPSC, CPSC-Extra, Georgia, Chapman-Shaoxing, Ningbo, Hefei, SPH, MIMIC-IV-ECG, SaMi-Trop, EchoNext, ZZU-pECG, MITHSDB, Cardio-Learning]
n_subjects:
n_channels: 12
model_type: "CNN embedder + transformer encoder, HuBERT masked prediction of k-means pseudo-labels (30M / 93M / 188M)"
eval_protocol: "full fine-tuning per dataset on predefined or 10% stratified hold-out test sets; FT vs training from scratch on 17 datasets"
main_metric: "macro AUROC"
main_result: "macro AUROC 0.9989 on Ribeiro/CODE test set (BASE, Table 2); 0.911 PTB-XL All (BASE, Supp. Table 10)"
code_available: "https://github.com/Edoar-do/HuBERT-ECG"
read_depth: full
concepts: [self-supervised-pretraining, channel-heterogeneity, evaluation-protocols]
---

# HuBERT-ECG (Coppola et al., medRxiv 2024, v4 2026)

## TL;DR
HuBERT from speech applied to ECG. Pretrained on 9.1M 12-lead ECGs from 4 countries to predict k-means cluster IDs (MFCC clusters first, then clusters of the model's own layer-8 states) of masked 0.64 s frames. Fine-tuned on 21 datasets with ~1.6k targets. **ECG method parallel** (field: other) for Q9 tokenization and Q7 evaluation practice; the EEG twin is Sleep2.0 → [[hubert-style-pseudo-labels]].

*Read from medRxiv v4 (posted 1 Jun 2026, 54 pp. incl. supplement); (p. N) = PDF pages. Supplementary table captions are shifted by one against their contents in this PDF, so supplement numbers are cited by page.*

## Research question
Can one self-supervised ECG model, pretrained on large and geographically diverse data, transfer to tasks beyond rhythm reading: structural disease, prognosis, paediatric and single-lead ECGs (pp. 2–3)?

## Data & preprocessing
- **Pretraining:** 9.1M unlabelled 12-lead ECGs from 11 public or access-on-demand datasets (CODE/Ribeiro, PTB, PTB-XL, CPSC(-Extra), Georgia, Chapman, Ningbo, Hefei, SPH, MIMIC-IV-ECG) from Brazil, Germany, China and the USA (p. 10, Fig. 2a). Labels stripped. 90/10 split for pretext validation (p. 14).
- **Overlap with fine-tuning:** the same datasets are reused for fine-tuning. The paper defends this as standard practice with no label leakage (pp. 10–11) and says test sets are "hold-out partitions … not included in the pre-training phase" (p. 11). Ribeiro's public test set is excluded (p. 10). The text both includes and excludes "the unlabelled partition of Ribeiro" (p. 10).
- **Preprocessing:** FIR band-pass 0.05–47 Hz, resampled to **100 Hz**, rescaled to [−1, 1], **5 s** crops instead of 10 s (p. 11). 50 Hz gave *lower* pretext validation loss but worse linear-probe AUROC (0.918 vs 0.933) (Supp. §1.2, p. 35; table p. 50).

## Method
- **Input:** the 12 leads are **concatenated end to end into one 1D sequence** (60 s of signal). A 5-layer CNN embedder turns it into **93 frames of 0.64 s** each, i.e. one frame ≈ 0.64 s of one lead. Positional encodings are added "to account for inter-lead relationships" (pp. 12–13).
- **Pseudo-labels (iteration 1):** 39-dim **MFCCs** (13 coefficients + Δ + ΔΔ) per frame, mini-batch **k-means, k = 100** (k-means++, 20 restarts) (p. 14). Chosen over 16 time–frequency statistics and over a mixed descriptor: linear probe 0.933 (MFCC) vs 0.913 (time–frequency) (Supp. §1.1, p. 34; table p. 50). k = 100 picked by the elbow on inertia (p. 34).
- **Iteration 2 (BASE):** **k = 500** on hidden states of **layer 8** of the iteration-1 model; 770k steps vs 80k in iteration 1 (pp. 14–15). Layer and k were picked by inertia, Davies–Bouldin and Calinski–Harabasz, which all trend monotonically and so "do not provide an unequivocal indication" (Supp. §1.4, p. 36). SMALL and LARGE were trained in one iteration on layer-9 clusters of the BASE model, k = 500 and 1,000 (p. 14).
- **Objective:** masked prediction. **p = 33%** of frames are replaced by a learned [MASK] embedding (single frames, not HuBERT's spans). The loss is cross-entropy over cluster IDs on masked frames only, with logits = cosine similarity to a learned cluster-embedding table / τ (pp. 12–14). An ensemble of k = 100/200/300 targets gave 0.943 vs 0.933 but needed 135k vs 80k steps, so it was dropped (Supp. §2.2, p. 37; table p. 51).
- **Sizes:** SMALL 30M (8 layers, d = 512), BASE 93M (12, 768), LARGE 188M (16, 960) (Table 1, p. 23).
- **Dynamic regularisation:** dropout and weight decay rise when pretext validation stalls and fall when it improves (p. 15).
- **Fine-tuning:** a linear head; everything except the CNN embedder is trained. Freezing the encoder (linear probe) "did not demonstrate any efficacy". Time-aligned random crops, and at test time the most confident of several crops (p. 16).

## Evaluation
- 21 datasets + the merged **Cardio-Learning** (2.46M ECGs, 164 harmonised labels, 3 cardiologists) (pp. 4, 11; Table 7).
- Predefined test splits where they exist. Otherwise a 10% stratified hold-out plus 4-fold CV for tuning. Tiny sets (PTB, CPSC-Extra, Clinical data, SaMi-Trop): 4 stratified folds and no validation set (p. 15). **Splits are by ECG; no statement about patient-level separation.**
- Tasks are grouped by the role of the ECG: **type-1** (ECG is the gold standard), **type-2** (supportive, e.g. echo findings), **type-3** (prognosis) (pp. 2–3, 17).
- Baselines: the same model trained from scratch (17 datasets), plus **numbers quoted from other papers** (KED, ECGFounder, contrastive ECG models). ECGFounder and KED were fine-tuned by the authors only on MIMIC-IV-ECG and a few other sets (Tables 3–4). There is no classical-feature baseline.

## Results (with locations)
- Fine-tuning beats training from scratch by **3–8 AUROC points** on the small datasets (p. 5).
- Ribeiro/CODE test: macro AUROC 0.9989 (BASE) vs 0.966 for Ribeiro et al. (Table 2).
- PTB-XL All: 0.905 / 0.911 / 0.900 (S/B/L) vs Strodthoff et al. 0.925 and Hu et al. 0.947 (Supp. Table 10, p. 53). So HuBERT-ECG does **not** top PTB-XL.
- **Scaling is not monotonic:** CPSC-Extra SMALL 0.894 vs BASE 0.756 vs LARGE 0.774 (p. 5). SaMi-Trop mortality SMALL 0.871 > BASE 0.863 > LARGE 0.862 (p. 6). MIMIC-IV endpoints are flat across sizes (Table 3).
- Type-2/3 tasks: EchoNext macro 0.793 (BASE) vs 0.83 for a supervised model with echo features (p. 6). MIMIC-IV mortality 0.818–0.825 vs ECGFounder 0.824; deterioration 0.735–0.747 vs ECGFounder 0.786 (Table 3).
- Single-lead MITHSDB (12-lead pretraining only): macro 0.878–0.917 vs ECGFounder 0.965 (p. 7).
- Multitask fine-tuning on Cardio-Learning raises SaMi-Trop death prediction to 0.910 (Fig. 6a, p. 8).
- **Pretext signals vs downstream:**
  - Iteration 2 beats iteration 1 by ~5 linear-probe AUROC points (Supp. Fig. 4, p. 36).
  - Among the dynamic-regularisation setups, the one with the **best** pretext validation loss and accuracy (0.586 / 0.831) gave a **worse** linear probe (0.924) than the default setup (0.638 / 0.821 → 0.933) (table p. 51).
  - p = 33% beats HuBERT's span masking, attributed to ECG's "high information redundancy" (Supp. §2.1, p. 37).

## Limitations (reported)
- Africa and India are underrepresented. Type-2/3 datasets are scarce. Label noise across sources. Comparisons with prior work are hard because they use label subsets and do not release code (pp. 9–10).
- Human-reader comparison: not head-to-head, and no statistical test (p. 8).

## Assessment 🤖
- 🤖 **Pretraining exposure:** the fine-tuning datasets' recordings are in the pretraining pool, and only test partitions are claimed excluded. Splits are by ECG, not patient (CODE has repeat ECGs per patient). This is the same issue logged for EEG FMs in [[evaluation-protocols]].
- 🤖 **The baselines are weak.** There is no matched classical baseline. Most comparisons are quoted numbers on different label subsets, and the authors themselves acknowledge that (p. 10). On PTB-XL, the standard benchmark, supervised and other SSL models are ahead (Supp. Table 10). Same pattern as Q7 for EEG.
- 🤖 **Frozen features are weak here too:** linear probing is used only for ablations, and freezing was "not effective" for downstream use (p. 16). This mirrors the EEG probe gap ([[kuruppu2026eeg]]).
- 🤖 **Pretext metrics again misrank models** (lower sampling rate → lower loss but worse features; best pretext loss → worse probe). This is the fourth vault source after EEGPT and SpecBraM → [[q9-pretraining-objectives-and-scale]].
- 🤖 **Clustering choices were made by eye.** Layer and k were chosen without a clear signal from cluster metrics, and HuBERT's phone-purity check has no ECG analogue (p. 36). EEG has no analogue either (sleep stages could serve, as Sleep2.0 implicitly does).
- 🤖 The flatten-12-leads trick depends on a fixed lead set. It does not carry over to EEG montages ([[channel-heterogeneity]]).

## Concepts
- [[self-supervised-pretraining]]: HuBERT masked prediction of clustered MFCC/latent targets; iterative target refinement.
- [[channel-heterogeneity]]: ECG has a fixed 12-lead set, so leads are concatenated into one sequence; single-lead transfer tested.
- [[evaluation-protocols]]: pretraining on fine-tuning datasets; record-level splits; quoted-number baselines.

## Related papers
- [[liu2026eeg]]: EEG benchmark showing the same weak-probe pattern. It lists two more HuBERT-style EEG FMs (E3GT, PSGFM) (p. 12).
- [[coon2026sleep]]: Sleep2.0 uses the same HuBERT recipe on sleep EEG (k = 100 on time–frequency power → k = 500 on stage-1 embeddings) → bridge [[hubert-style-pseudo-labels]].
- [[jiang2024large]]: LaBraM learns its codebook with a VQ-VAE instead of clustering fixed features.
- [[xie2026specbram]]: regresses a hand-crafted spectral feature directly. Same intuition (features as targets), without clustering.
- [[wang2024eegpt]]: also shows pretext loss misranking downstream quality.
- [[kuruppu2026eeg]]: EEG FM review whose criticisms (weak probes, in-distribution tests, weak scaling) apply here too.

## Q&A notes
- 2026-10-11 **Q:** How does HuBERT-ECG tokenize? **A:** It doesn't use a fixed vocabulary as input. A CNN embeds 0.64 s frames of the lead-concatenated signal, and the *targets* are k-means IDs: k = 100 on 39-d MFCCs, then k = 500 on layer-8 states (pp. 12–14). The earlier repo-based answer in Q9 (29-d stats + MFCC) described a code variant; the paper's chosen descriptor is MFCC-only (p. 34). → [[q9-pretraining-objectives-and-scale]].
