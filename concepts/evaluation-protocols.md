---
slug: evaluation-protocols
fields: [eeg, ml]
familiarity: understood     # human's level: new | introduced | understood | skip
---

# evaluation-protocols

## Field-neutral description
How data is split into training and test sets, and what is measured, determines what a reported score means. Splits that let near-identical samples (same person, same session, neighbouring time windows) appear on both sides inflate scores and make results incomparable across papers.

## Synonyms by community
- **EEG:** within-subject / subject-dependent, cross-subject / subject-independent, cross-session, leave-one-subject-out (LOSO), patient-level split
- **Neuroscience / clinical:** —
- **Signal processing:** —
- **General ML:** data leakage, i.i.d. vs out-of-distribution split, group k-fold, linear probing vs fine-tuning

## Papers
- [[song2022eeg]]: within-subject only. Cross-session split on BCI IV-2a/2b, but 5-fold CV over 1 s windows from a single SEED session (likely leakage 🤖) (§IV-A).
- [[jiang2024large]]: patient-level split on TUAB/TUEV (following BIOT), but SEED-V splits trials and pools subjects (App. F). Reports fine-tuning and linear probing; the probe is much weaker on TUEV (Table 10).

- [[varbu2022past]]: in BCI, inter- and intra-subject variability is "one of the most important obstacles", and subject-independent BCIs remain a challenge. Per-user calibration is time-consuming and especially hard for people with mental disabilities (§6.1, pp. 21–22).
- [[chaddad2023electroencephalography]]: a clear example of split dependence. DeprNet (depression) gets 99.37% with a recording-level split vs 91.4% with a subject-level split (Table 6). The review's accuracy tables mix protocols.

- **Own worked example (2026-10-10):** CSP + LDA, imagined vs executed fist on EEGMMI (10 subjects). Shuffled 5-fold 0.83 → leave-one-run-pair-out 0.64 → cross-subject 0.56. A control on *rest* periods also reaches 0.65, i.e. the model mostly learns which recording block a trial came from, because the class is confounded with the run → [[bci-paradigms]] *Imagined vs executed movement*.

- [[gans2024sleep]]: **device validation** is a different protocol: the wearable and the reference (PSG) record at the same time, and their stage labels are compared epoch by epoch. Metrics vary (accuracy, κ, sensitivity, correlation), and the authors recommend κ for imbalanced classes (p. 10). Per-stage one-vs-rest accuracy misleads: N1 accuracy 0.90 with sensitivity 0.21 (Table 1, p. 5).
- [[lee2021interrater]]: **label noise sets a ceiling.** Two human sleep scorers agree at κ 0.76 overall and 0.24 on N1 (Abstract), so a model scored against one human can't meaningfully exceed that.
- [[wong2023eeg]]: **dataset construction can make proper splits impossible.** Bonn and Hauz Khas pool segments without patient IDs (§5.6). Bonn is balanced by hand-picking segments (§6.1). Kaggle Melbourne-NIH and NeuroVista Ictal share patients, which risks leakage if combined (§7). Seizures are <1% of recorded EEG (§2), and resampling to balance "does not represent the true nature" of recordings (§7).
- [[wang2024cbramod]] on CHB-MIT: a subject split, but the test set is only 2 children (subjects 22–23). With heavy imbalance, balanced accuracy is 0.57–0.74 and AUC-PR 0.12–0.37, while AUROC is 0.80–0.89 (App. E.2, Table 8). 🤖 AUROC looks good under rare positives; AUC-PR is the more honest number.
- [[li2022eeg]]: a 7-strategy split taxonomy for emotion EEG (Fig. 32, §5.3). Trial-level splits are recommended. Cutting trials into segments that inherit the trial label adds label noise, and random k-fold over segments is "wrong" because segments of one trial land in both train and test (p. 25). The reason people do it: subjects give ≤~100 trials (p. 25). Its own results table (Table 4) doesn't mark which papers used which split.
- [[roy2019deep]] (2010–2018, 156 DL papers): 60% used no cross-validation, and only 22 of 108 inter-subject studies held subjects out (§3.7.3–3.7.4, pp. 22–23). 21.1% had no baseline, 19.9% used statistical tests (pp. 21, 23). Example counts are inflated by window overlap: 4.05M examples from 18 h of EEG (p. 11). 🤖 Overlapping windows plus random splits is the segment-leakage pattern [[li2022eeg]] calls wrong.
- [[lawhern2018eegnet]]: the same 5 models on the same 4 datasets, within-subject (4-fold blockwise CV) and cross-subject (random held-out subjects, 30–90 folds) (§2.3). The gap depends on the paradigm: P300 AUC barely drops (~0.92 → ~0.90), but 4-class motor imagery falls from ~0.68 to ~0.40 (EEGNet) and ~0.32 (FBCSP), chance 0.25 (Figs. 2–5). Model rankings flip between protocols: DeepConvNet is worst within-subject on MRCP (~0.66) but best cross-subject (~0.83), which the authors attribute to 10–15× more training data (p. 21).

## Variants & disagreements
- Same dataset, different protocol: SEED appears as 5-fold window CV in Conformer and as a trial split in LaBraM (SEED-V). Accuracies are not comparable. The emotion review [[li2022eeg]] calls the first one wrong (§5.3).
- Same model, same dataset, different paper: EEGNet on BCI IV-2a within-subject is ~0.68 in [[lawhern2018eegnet]] (Fig. 3) but 74.50% in [[song2022eeg]] (Table II). 🤖 Different splits, windows and preprocessing; baseline numbers are protocol-specific.
- Within vs cross-subject on the same model and data: DGCNN on SEED 90.4% → 79.95%; BiDCNN on DEAP valence 94.4% → 68.1% [[li2022eeg]] (Table 4). → [[domain-adaptation]]
- Baselines copied vs re-run: LaBraM copies BIOT's baseline numbers (§3.2). Conformer doesn't say.

## Open questions
- Is there a standard cross-subject benchmark suite the field is converging on for foundation models? (look for benchmark papers)
- What is the protocol-matched gap between within- and cross-subject accuracy on motor imagery? *Partial (2026-10-11):* ~0.68 → ~0.40 (4-class, BCI IV-2a, EEGNet) [[lawhern2018eegnet]] (Figs. 3, 5); own EEGMMI test 0.64 → 0.56 (2-class, CSP + LDA). Still no 2022+ source.

## Related concepts
- [[domain-adaptation]]: methods that try to close the within/cross-subject gap.
- [[self-supervised-pretraining]]: probing vs fine-tuning, and pretraining/test overlap.
