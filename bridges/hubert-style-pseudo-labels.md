---
slug: hubert-style-pseudo-labels
fields: [ecg, eeg, speech]
confidence: plausible
concepts: [self-supervised-pretraining, channel-heterogeneity, time-frequency-analysis]
---

# hubert-style-pseudo-labels

*First ECG↔EEG bridge (2026-10-11). The ECG side is a method parallel only (scope: CLAUDE.md, Other fields).*

## Claim
HuBERT-ECG's masked prediction of k-means pseudo-labels, built first on hand-crafted spectral features and then on the model's own hidden states, is the same recipe that Sleep2.0 applies to sleep EEG. Both inherit it from HuBERT in speech. The recipe should carry over to EEG wherever the hand-crafted features capture the state that matters (spectrum). It should carry over less well where shape matters (transients) or where the channel set varies.

## Common ground (field-neutral)
- **The problem:** a continuous signal has no natural vocabulary, so masked-token prediction needs discrete targets.
- **The recipe:**
  1. Compute a cheap, fixed descriptor per short frame (spectral or cepstral).
  2. Cluster all frames with k-means; the cluster ID becomes the frame's "pseudo-label".
  3. Train a transformer to predict the IDs of masked frames from the raw signal (cross-entropy).
  4. Re-cluster the trained model's intermediate hidden states with a larger k and train again.
- **Why it might work:** the targets are discrete and phase-free, so the loss does not punish unpredictable waveform detail (cf. the MSE double penalty in [[q9-pretraining-objectives-and-scale]]). Iteration 2 lets targets move from "what the descriptor sees" toward "what the model found useful".
- **Shared parameters**, almost identical:

| | speech (HuBERT) | ECG ([[coppola2024hubert]]) | sleep EEG ([[coon2026sleep]]) |
|---|---|---|---|
| frame | 20 ms | 0.64 s of one lead (p. 13) | per 30 s epoch for targets; finer native resolution in stage 2 (946 labels / 50.5 min) (p. 15) |
| iteration-1 descriptor | 39-d MFCC | 39-d MFCC (beat 16 time–frequency stats: probe 0.933 vs 0.913) (pp. 14, 34, 50) | epoch-level time–frequency power (p. 15) |
| iteration-1 k | 100 | 100 (p. 14) | 100 (p. 15) |
| iteration-2 targets | k-means on hidden layer | k = 500 on layer 8 (BASE); 500/1,000 on layer 9 (SMALL/LARGE) (p. 14) | k = 500 on stage-1 transformer embeddings (p. 15) |
| input to the model | raw waveform | raw, 12 leads concatenated, 100 Hz (pp. 11–13) | raw single central EEG channel (C3 or C4) (p. 15) |
| data | — | 9.1M ECGs (p. 10) | 11,261 PSG nights (p. 4) |

*The speech column comes from Hsu et al. 2021 (HuBERT; HuBERT-ECG ref. 24), which is not read in the vault 🤖. HuBERT-ECG states only that its MFCC descriptor follows Hsu et al. (p. 34).*

## Side A papers (EEG)
- [[coon2026sleep]] (Sleep2.0, *methods + key results read; no paper note yet*): HuBERT-style pretraining on one central EEG channel. Matched controls: the same backbone pretrained on 5-stage labels, and the same backbone trained from scratch (p. 5). SSL embeddings support finer within-night clusterings than stage-pretrained ones (BIC-selected k ≈ 10–12 vs 5) (p. 8). SSL meta-states improve screening over stage summaries (AHI AUROC 0.686→0.745) (p. 11). The authors call for a comparison with contrastive and generative objectives (p. 14).
- **More EEG cases, both from the same JHU APL group as Sleep2.0:** E3GT (Ogg et al. 2025, [[ogg2025eeg]]; 26,496 h, 96.4M params) and PSGFM (Coon & Ogg 2025, [[coon2025foundation]]; sleep PSG, likely Sleep2.0's preprint). Both use "spectrogram-derived k-means labels" as targets with cross-entropy, a 12-layer 768-d transformer [[liu2026eeg]] (pp. 4, 12; Supp. Table 5). 🤖 So HuBERT-style EEG is essentially one lab's line of work; neither model is in the open-weight benchmark.
- Contrast cases (EEG targets that avoid clustering): [[jiang2024large]] (LaBraM) *learns* a VQ codebook regressing Fourier amplitude + phase. [[xie2026specbram]] regresses band power directly. Neither clusters fixed features.

## Side B papers (ECG)
- [[coppola2024hubert]] (HuBERT-ECG, full read): 30M–188M models. Iteration 2 adds ~5 linear-probe AUROC points over iteration 1 (Supp. Fig. 4, p. 36). A 100/200/300 k-means ensemble gives +1 point at ~1.7× the steps (p. 51). Masking single frames at 33% beats HuBERT's spans (p. 37).

## Where the analogy breaks
- 🤖 **Channels.**
  - ECG has a fixed 12-lead set, so concatenating leads into one sequence and using positional encodings works (p. 13).
  - Sleep2.0 sidesteps the problem by using one channel.
  - Multi-montage clinical EEG cannot use the concatenation trick: lead order and count vary → [[channel-heterogeneity]]. Per-channel clustering plus electrode embeddings would be needed. Untested in the vault.
- 🤖 **What the descriptor captures.**
  - ECG diagnosis is largely beat morphology, and MFCCs (a smoothed log-spectrum envelope) of a 0.64 s frame mix rhythm and shape.
  - In sleep EEG, the state *is* largely spectral (delta, sigma, alpha), so time–frequency features are a near-direct proxy for the target. This is the same argument SpecBraM makes ([[xie2026specbram]] §4).
  - For transient EEG events (spikes, sharp waves) neither MFCC nor band-power clusters are obviously adequate.
- 🤖 **Scale.** ECG has ~800× more recordings (9.1M vs 11k nights; TUEG has 69,652). EEG nights are long, though, so Sleep2.0 has far more frames per recording.
- 🤖 **Validating the clusters.**
  - Speech HuBERT checked cluster quality against phone labels.
  - HuBERT-ECG had no analogue and picked layer and k by eye (p. 36).
  - Sleep EEG *has* an analogue: AASM stages, which work like phones (coarse, human-defined units). Sleep2.0 uses them for interpretation only (p. 15).
- 🤖 **Sampling.** HuBERT-ECG resamples to 100 Hz and cuts 47 Hz (p. 11), which is fine for ECG. EEG gamma and spike edges need more.

## What would test it
- A matched EEG study on the same corpus and probe: HuBERT-style clustering (band-power k-means → latent k-means) vs LaBraM VQ vs SpecBraM band-power regression vs raw MSE. No such study in the vault (Q9 open thread).
- Multi-channel HuBERT for EEG with per-channel frames, and whether iteration 2 helps as much as in ECG (+5 points).
- Cluster purity against AASM stages (sleep) or TUEV event labels as the EEG analogue of phone purity, to pick the layer and k objectively.
- Whether HuBERT-style targets lose on transient-morphology tasks (TUEV), as the spectral-target theory predicts.
