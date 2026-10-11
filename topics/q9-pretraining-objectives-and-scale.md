---
slug: q9-pretraining-objectives-and-scale
kind: hub
status: active
updated: 2026-10-11
---

# q9-pretraining-objectives-and-scale

> What should EEG foundation models learn from unlabelled data? Covers pretext targets (raw waveform, spectral features, discrete tokens, latent embeddings), data scale and diversity, and what the pretext loss does and doesn't tell us.

*Added 2026-10-11 at the human's request, after the SSL-objectives theme reached 3 questions across 2 sessions. The general SSL concept lives in [[self-supervised-pretraining]] (taxonomy, contrastive and latent-space targets explained). This hub holds the cross-paper synthesis.*

## Current answer
- **Four target families are in use:** raw waveform + MSE (CBraMod, Brant, FoME), spectral (BrainBERT/BrainWave spectrograms, SpecBraM band power), discrete tokens + cross-entropy (LaBraM, EEGFormer, NeuroLM, Sleep2.0), latent embeddings (EEGPT, Neuro-GPT, BIOT). Details in the table below.
- **The target matters more than the tokenizer, at least for frozen features.** Band power beats raw-waveform reconstruction under a strict linear probe on sleep staging (+1.6 to +2.8 points; +4.7 to +7.3 with 1% of labels) [[xie2026specbram]] (Table 2). Discrete codes beat raw MSE on TUEV but not on TUAB [[jiang2024large]] (App. G, Table 7). No target wins everywhere.
- **Raw-waveform MSE wastes capacity on unpredictable phase** (the double penalty, below). Spectral and latent targets avoid it, at the cost of morphology for transient events (🤖 + [[xie2026specbram]] §4).
- **Scale is small by LLM standards:** ~0.3–3B single-channel 1 s patches, at most ~15k–25k distinct people in public corpora, ~108k patients in HEEDB. Evidence for data or model scaling is "weak, if any" [[kuruppu2026eeg]] (§5.1).
- **Pretext loss is not a quality metric.** Lower loss can come with worse features [[wang2024eegpt]] (Table 5); [[xie2026specbram]] (App. C). Held-out pretext loss is almost never reported.
- **The same recipes appear in ECG:** HuBERT-style k-means pseudo-labels are used in both HuBERT-ECG and the sleep-EEG model Sleep2.0 (below).

## Scale, targets and pretext loss in detail (asked 2026-10-11)
**Scale.** Corpora are measured in hours or channel-hours (channels × hours) [[kuruppu2026eeg]] (Supp. Table 1).

| model | pretraining data | hours | channel-hours |
|---|---|---|---|
| BrainBERT | Brain TreeBank (iEEG) | — | 4.5k |
| LaBraM | ~20 public datasets + own | 2,535 [[jiang2024large]] (App. D) | 80k |
| Brant | private iEEG, 9 subjects | ~2,528 (sum of per-subject rows) | 282k |
| BIOT | SHHS (2 ch, sleep) + PREST | 56,643 | 312k |
| Neuro-GPT, EEGFormer | full TUEG | 27,063 | 541k |
| NeuroLM | TUEG + LaBraM's sets | ~24.7k | 546k |
| BrainWave | scalp + iEEG mix | — | 878k (3.16B 1 s patches) |
| CBraMod | TUEG, cleaned | >9,000 [[wang2024cbramod]] (§3.1) | ~171k 🤖 (19 ch × 9,000 h) |

- **TUEG** (the open clinical standard): 69,652 recordings, 14,987 subjects, 27,062 h, >40 channel configurations [[wang2024cbramod]] (§3.1).
- **Bigger than TUEG (as of 2026):**
  - **HEEDB** (Harvard EEG Database, Epilepsia 2025): ~280k clinical EEGs from ~108k patients at 4 Boston hospitals (routine, EMU, ICU, all ages), linked to reports, ICD-10 codes and medications, hosted on the Brain Data Science Platform [[sun2025harvard]] (abstract, via web search; hours and access terms not checked).
  - **REVE** (NeurIPS 2025) pooled >60,000 h from 92 datasets, ~25,000 subjects, of which TUH is 44% ([[ouahidi2025reve]], as cited by [[zare2026negative]]).
  - **Sleep PSG** archives are larger in hours: SleepFM used >100,000 h from 14,000 participants [[kuruppu2026eeg]] (Supplement); SHHS alone is 42,446 h (Supp. Table 1).
  - The NeuroAtlas *benchmark* aggregates ~260k h across 42 datasets [[kontras2026neuroatlas]] (abstract).
- 🤖 **In LLM terms:** with 1 s per-channel patches as tokens, LaBraM sees ~0.3B tokens, full TUEG ~2B and BrainWave ~3.2B. That is roughly BERT-sized (~3.3B words), and 3–4 orders of magnitude below current LLMs. Each token also carries far less information than a word, because neighbouring seconds and electrodes are highly correlated (volume conduction). The number of distinct *people* (≤15k in TUEG) is probably the tighter limit → [[q6-reliability-of-eeg-diagnoses]].

**What is predicted.** Both answers occur, plus latent-space targets:

| model | input unit | target | loss |
|---|---|---|---|
| CBraMod | 1 s raw patch (200 samples) | masked raw patches, in units of 100 µV | MSE on masked patches only [[wang2024cbramod]] (Eq. 12) |
| Brant, FoME | 6 s raw patches (+ spectra) | masked raw patches (~40% zeroed) | regression; exact loss not in vault [[kuruppu2026eeg]] (§4.2) |
| BrainBERT, BrainWave | per-channel spectrograms | masked spectrogram patches / whole channels | reconstruction [[kuruppu2026eeg]] (§4.2) |
| **LaBraM** | 1 s raw patch | **discrete code from a learned tokenizer** (8,192 × 64 codebook) | stage 1: a VQ-VAE whose decoder regresses the z-scored Fourier **amplitude and phase** of each patch (MSE, Eq. 9). Stage 2: predict the code index of 50% masked patches = **cross-entropy over 8,192 classes** [[jiang2024large]] (§2.2 Eq. 9, §2.3, App. C Table 3). For the tokenizer, reconstructing raw signal directly "fails to converge" (§2.2) |
| EEGFormer | spectral patches | raw patches decoded from quantized codes | codebook reconstruction [[kuruppu2026eeg]] (§4.2) |
| NeuroLM | VQ tokens aligned to text | next token, autoregressive | LLM next-token loss (🤖 cross-entropy, standard) [[kuruppu2026eeg]] (§4.2) |
| EEGPT | raw patches | (a) the momentum encoder's features for masked parts (JEPA-like), (b) the layer-normalized raw patch | MSE + MSE [[wang2024eegpt]] (Eqs. 6, 8) |
| Neuro-GPT | raw multichannel chunks | masked *latent* embeddings, via a GPT-2 decoder | latent reconstruction [[kuruppu2026eeg]] (§3.2) |
| BIOT | per-channel FFT tokens | none: BYOL-style, the embedding of a channel/token-dropped view predicts the original's | contrastive [[yang2023biot]] (§2.3) |

- **Amplitude scaling:** LaBraM and CBraMod divide by 100 µV so values sit roughly in [−1, 1]; no per-channel z-scoring ([[jiang2024large]] §3.1; [[wang2024cbramod]] §3.1). CBraMod also drops any 30 s sample with a point above 100 µV, a crude artifact rejection. EEGPT layer-normalizes each target patch, which removes absolute amplitude; without that normalization downstream accuracy fell [[wang2024eegpt]] (Table 5).
- **Which target is better: no consensus, and it depends on the task.** LaBraM's own ablation (App. G, Table 7):

  | target | TUAB bal. acc. | TUEV bal. acc. |
  |---|---|---|
  | discrete codes (CE) | 0.814 | **0.641** |
  | raw patch (MSE) | **0.826** | 0.563 |
  | Fourier amplitude + phase (MSE) | 0.817 | 0.573 |
  | tokenizer embedding (cosine) | 0.806 | 0.616 |

  NeuroLM found different tokenizer targets help different tasks [[kuruppu2026eeg]] (§4.3).
- **Band-power target (SpecBraM):** [[xie2026specbram]] regresses log(1 + P) for 5 fixed narrow bands of each masked patch (MSE, Eq. 1–2), with everything else matched to a raw-waveform control (51M criss-cross transformer, 2,388 h of TUEG, 16 epochs, 3 pretraining seeds). Under a strict linear probe it gains +1.6/+2.8 balanced-accuracy points on ISRUC/HMC sleep staging, positive in all 12 seed–dataset pairs, and +4.7 to +7.3 with 1% of labels (Table 2). After full fine-tuning the gap shrinks to ~1 point (Table 6, §6.3). Beyond sleep it is mixed: better on FACED, worse on Mental Arithmetic with one tokenizer, raw slightly better on PhysioNet-MI (§6.4, Tables 7–8).
  - *Its theory (§4, App. A):* if a patch is a stationary Gaussian process whose spectrum encodes the brain state, the periodogram is sufficient and phase carries no state information. The irreducible error of a waveform target is the patch's own random amplitude and phase, which scales with power and is dominated by low frequencies (1/f). For band power the remaining error is mostly uncertainty about the state, which is what the encoder should learn.
- 🤖 **Why raw-MSE may be a weak target for EEG:** a masked 1 s patch can largely be interpolated from its temporal and spatial neighbours (autocorrelation, volume conduction). The loss can then be driven down without learning brain-state structure. Phase is also near-random for induced rhythms, so MSE on phase-sensitive waveforms penalises unpredictable detail. [[yu2026neural]] (abstract) makes the shortcut argument, and LaBraM motivates its spectral targets by low SNR (§2.2).
  - **The double penalty (the human's point, 2026-10-11):** a prediction with the right waveform shape but shifted by half a period is scored as the negation of the truth. For a sinusoid of amplitude A that gives MSE 2A², four times worse than predicting a flat line (A²/2). So under phase uncertainty the MSE-optimal output is the conditional mean, a blurred, near-zero waveform. 🤖 For rhythms this throws away nothing clinically relevant, but for transients (spikes, sharp waves) MSE rewards smoothing away exactly the morphology clinicians read. LaBraM's tokenizer reconstructs Fourier amplitude well and phase poorly (App. E, Fig. 7). SpecBraM predicts the band-power target should lose its advantage on tasks that depend on transient shape (§4).

**Is pretext loss itself informative?**
- **Held-out pretext loss is almost never reported.** Kuruppu found only Mentality reporting reconstruction error, and Brant/FoME reporting forecasting and imputation as tasks [[kuruppu2026eeg]] (§4.3, p. 15). Losses aren't comparable across models anyway (different targets, normalizations, units).
- **Lower pretext loss ≠ better features.** EEGPT without target normalization reached reconstruction loss 0.002 vs 0.56 but lost 1–7 points downstream; without its alignment loss, reconstruction loss was unchanged but downstream fell 6–9 points [[wang2024eegpt]] (Table 5). SpecBraM with learnable target filters drove its loss to 4×10⁻⁴ by shrinking the targets, and the features became uninformative [[xie2026specbram]] (App. C).
- 🤖 **Pretext loss as an anomaly score (the human's idea):** plausible for unlabelled screening, but a raw-MSE score mostly measures *power*: its irreducible part scales with signal power ([[xie2026specbram]] §4), so high-amplitude artifacts (movement, electrode pops), slow waves and seizures all score high. A usable score would need per-patch normalization or a likelihood under predicted band powers, and artifacts would still dominate unless removed first. Not tested in the vault → Open questions.

## Tokenization: HuBERT-style pseudo-labels in ECG and EEG (asked 2026-10-11)
*ECG is in scope as a method parallel since 2026-10-11 (→ bridges/). HuBERT-ECG facts come from its public code; the medRxiv full text was blocked (403), so no paper note yet.*

- **HuBERT-ECG** [[coppola2024hubert]] (Coppola et al., medRxiv 2024, doi 10.1101/2024.11.14.24317328; 9.1M 12-lead ECGs from 4 countries, per its model card). From the repo `Edoar-do/HuBERT-ECG` (`hubert_ecg/dumping.py`, `scripts/clustering.sh`, `scripts/pretraining.sh`):
  - Input: 5 s × 12 leads (2,500 samples per lead at 500 Hz), decimated (100 Hz in the 64-sample-shard configuration). The **12 leads are concatenated end to end into one 1D sequence** and cut into shards, giving 93 tokens per ECG (one per 0.64 s of one lead at 100 Hz). A CNN front end downsamples by the same factor (64) so frames align with shards.
  - **Iteration 1 targets:** per shard, 16 hand-crafted time/frequency statistics (min, max, mean, RMS, variance, std, power, peak, peak-to-peak, crest factor, skewness, kurtosis; FFT power max/sum/mean/variance) plus 13 MFCCs (29 dims; MFCC-only and stats-only variants exist). Then MiniBatch **k-means with k = 100–300**.
  - **Iteration 2+:** k-means with **k = 500–1,000** on hidden states of an intermediate transformer layer (layer 8 in the example script).
  - Masking probability 0.33 ("optimal masking ratio found empirically"). The model predicts the cluster ID of masked frames (HuBERT objective: cross-entropy over the vocabulary; 🤖 inferred from the HuBERT design and `vocab_sizes`, not read in the paper).
- **The EEG twin: Sleep2.0** [[coon2026sleep]] (Methods, p. 15): "HuBERT-style masked pseudo-label prediction". Stage 1 runs k-means with **k = 100** on epoch-level time-frequency power features. Stage 2 runs **k = 500** on first-stage transformer embeddings. The model is trained from raw signals. Its predecessor (Ogg & Coon 2024) used k = 300 on spectrogram features over a single central channel [[kuruppu2026eeg]] (Supplement).
- **Other EEG tokenizers compared:**
  - LaBraM *learns* its codebook (VQ-VAE regressing Fourier amplitude and phase, 8,192 codes) instead of clustering fixed features (BEiT-v2 style rather than HuBERT style) [[jiang2024large]] (§2.2).
  - SpecBraM regresses the hand-crafted feature (band power) directly, without clustering. It cites HuBERT's MFCC clusters and MaskFeat's HOG targets as the same idea in other modalities [[xie2026specbram]] (§2).
- 🤖 **Where ECG and EEG differ:**
  - ECG has a fixed 12-lead standard, so concatenating leads works. EEG montages vary, so EEG models tokenize per channel and add electrode embeddings → [[channel-heterogeneity]].
  - ECG is quasi-periodic, and beat *morphology* is the diagnosis, so the shape statistics (peak, crest factor, kurtosis) are informative. EEG is closer to a stochastic process whose state lives in the *spectrum*, which is why EEG targets drift toward band power.
  - ECG corpora are ~100× larger in recordings (9.1M vs TUEG's 69,652).

## Comparisons
| family | example | target | loss | phase-sensitive? |
|---|---|---|---|---|
| raw waveform | CBraMod | masked raw patch (100 µV units) | MSE | yes |
| hand-crafted spectral | SpecBraM | log band power, 5 bands | MSE | no |
| clustered features (HuBERT) | Sleep2.0, HuBERT-ECG | k-means ID of feature/latent | CE | no (features) |
| learned codebook (BEiT-v2) | LaBraM | VQ code of Fourier amp + phase | CE | partly |
| latent (JEPA / BYOL) | EEGPT, BIOT | EMA-encoder embedding | MSE / contrastive | no |

## Open threads
- Is pretext-loss error usable as an unsupervised anomaly score? → [[self-supervised-pretraining]] *Open questions*.
- No matched comparison of HuBERT-style clustering vs a learned codebook vs band-power regression on the same EEG data and probe.
- Do band-power targets lose on transient-morphology tasks (spikes, TUEV events), as SpecBraM's theory predicts? Not tested on TUEV in the vault.
- Does scale help once corpora reach HEEDB size (~108k patients)? No result yet.
- Full reads queued: [[xie2026specbram]], [[ouahidi2025reve]], [[yu2026neural]], [[coon2026sleep]].

## Sources
- [[kuruppu2026eeg]]: data scale (channel-hours) and SSL objectives of 10 early FMs; pretext-loss reporting.
- [[jiang2024large]]: VQ tokenizer and the target ablation (App. G).
- [[wang2024cbramod]]: raw-patch MSE; TUEG statistics.
- [[wang2024eegpt]]: latent + reconstruction losses; the loss-vs-downstream ablation (Table 5).
- [[xie2026specbram]]: band-power target, matched target study, theory *(key tables read)*.
- [[coon2026sleep]]: Sleep2.0, a HuBERT-style sleep-EEG FM *(methods read)*.
- [[yang2023biot]]: BYOL-style contrastive objective.
- [[sun2025harvard]], [[ouahidi2025reve]], [[kontras2026neuroatlas]]: corpus sizes.
- [[self-supervised-pretraining]]: the concept, with contrastive and latent-space targets explained.
