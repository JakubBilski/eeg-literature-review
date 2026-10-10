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

## Variants & disagreements
- Same dataset, different protocol: SEED appears as 5-fold window CV in Conformer and as a trial split in LaBraM (SEED-V). Accuracies are not comparable.
- Baselines copied vs re-run: LaBraM copies BIOT's baseline numbers (§3.2). Conformer doesn't say.

## Open questions
- Is there a standard cross-subject benchmark suite the field is converging on for foundation models? (look for benchmark papers)
- What is the protocol-matched gap between within- and cross-subject accuracy on motor imagery?

## Related concepts
- [[self-supervised-pretraining]]: probing vs fine-tuning, and pretraining/test overlap.
