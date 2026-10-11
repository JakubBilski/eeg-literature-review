---
slug: q9-pretraining-objectives-and-scale
kind: hub
status: active
updated: 2026-10-12
---

# q9-pretraining-objectives-and-scale

> What should EEG foundation models learn from unlabelled data? Covers pretext targets (raw waveform, spectral features, discrete tokens, latent embeddings), data scale and diversity, and what the pretext loss does and doesn't tell us.

*Added 2026-10-11 at the human's request, after the SSL-objectives theme reached 3 questions across 2 sessions. The general SSL concept lives in [[self-supervised-pretraining]] (taxonomy, contrastive and latent-space targets explained). This hub holds the cross-paper synthesis.*

## Current answer
- **Four target families are in use:** raw waveform + MSE (CBraMod, Brant, FoME), spectral (BrainBERT/BrainWave spectrograms, SpecBraM band power), discrete tokens + cross-entropy (LaBraM, EEGFormer, NeuroLM, Sleep2.0), latent embeddings (EEGPT, Neuro-GPT, BIOT). Details in the table below.
- **The target matters more than the tokenizer, at least for frozen features.** Band power beats raw-waveform reconstruction under a strict linear probe on sleep staging (+1.6 to +2.8 points; +4.7 to +7.3 with 1% of labels) [[xie2026specbram]] (Table 2). Discrete codes beat raw MSE on TUEV but not on TUAB [[jiang2024large]] (App. G, Table 7). No target wins everywhere.
- **Raw-waveform MSE wastes capacity on unpredictable phase** (the double penalty, below). Spectral and latent targets avoid it, at the cost of morphology for transient events (🤖 + [[xie2026specbram]] §4).
- **In a matched benchmark, the objective family doesn't decide the outcome.** 12 open FMs on 13 datasets: raw-reconstruction models rank 1–15, embedded-token models 7–18, codebook models 9–20. The best of each family (CBraMod, Neuro-GPT, LaBraM) are all competitive. No objective matches a paradigm: spectral-target FMs are not best on SSVEP [[liu2026eeg]] (§4.1, Supp. Table 53). 🤖 Objective is confounded with corpus, architecture and preprocessing here, unlike SpecBraM's matched ablation.
- **Scale is small by LLM standards:** ~0.3–3B single-channel 1 s patches, at most ~15k–25k distinct people in public corpora, ~108k patients in HEEDB. Evidence for data or model scaling is "weak, if any" [[kuruppu2026eeg]] (§5.1). The 2026 benchmark agrees: the top six FMs are 0.16–5.8M params, and within the codebook family the larger models rank worse (LaBraM 5.8M 9.36 < BrainOmni 8.4M 12.33 < 33M 12.76) [[liu2026eeg]] (pp. 21–22).
- **Pretext loss is not a quality metric.** Lower loss can come with worse features [[wang2024eegpt]] (Table 5); [[xie2026specbram]] (App. C). Held-out pretext loss is almost never reported. The main reasons are that loss values depend on the target definition and that the objective is misaligned with downstream tasks; overfitting during small-data fine-tuning comes next → *Why pretext gains don't transfer downstream*.
- 🤖 **Predictability alone doesn't identify what matters clinically.** It separates structure from noise only relative to the context and loss. MSE learns the conditional mean, but rhythm state lives in the variance. Much predictable structure is nuisance (artifacts, device fingerprints), and spike or seizure timing is unpredictable yet clinical → *Does predictability reveal what matters clinically?*
- 🤖 **Covariance (Riemannian) pseudo-labels are untried as FM targets.** They would add cross-channel coupling to spectral targets, but they need a filter bank, per-recording re-centering (or they cluster by subject/device) and a fixed montage → *Covariance matrices as pseudo-label seeds?*
- **The same recipes appear in ECG:** HuBERT-style k-means pseudo-labels are used in both HuBERT-ECG and the sleep-EEG model Sleep2.0, with nearly identical settings (k = 100 on spectral features → k = 500 on hidden states) → bridge [[hubert-style-pseudo-labels]]. ECG also shows that scale is not monotonic: the 30M model beats the 188M one on small datasets ([[coppola2024hubert]] pp. 5–6).

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
- **Lower pretext loss ≠ better features.** EEGPT without target normalization reached reconstruction loss 0.002 vs 0.56 but lost 1–7 points downstream; without its alignment loss, reconstruction loss was unchanged but downstream fell 6–9 points [[wang2024eegpt]] (Table 5). SpecBraM with learnable target filters drove its loss to 4×10⁻⁴ by shrinking the targets, and the features became uninformative [[xie2026specbram]] (App. C). The same holds in ECG [[coppola2024hubert]]: at 50 Hz the pretext validation loss was lower but the linear probe worse (0.918 vs 0.933 at 100 Hz) (p. 35). The setup with the best pretext loss and accuracy (0.586 / 0.831) probed worse (0.924) than the default (0.638 / 0.821 → 0.933) (p. 51). 🤖 Easier pretext tasks give lower loss and worse features. The loss only says how easy the targets are.
- 🤖 **Pretext loss as an anomaly score (the human's idea):** plausible for unlabelled screening, but a raw-MSE score mostly measures *power*: its irreducible part scales with signal power ([[xie2026specbram]] §4), so high-amplitude artifacts (movement, electrode pops), slow waves and seizures all score high. A usable score would need per-patch normalization or a likelihood under predicted band powers, and artifacts would still dominate unless removed first. Not tested in the vault → experiment [[pretext-loss-anomaly-score]].

## Why pretext gains don't transfer downstream (asked 2026-10-11)
*The human's question: is "better at pretraining, worse downstream" due to overfitting, ill-posed downstream tasks, ill-posed pretext comparisons, or something else?*

- **The "pattern" is two different observations.** (A) *Within one model:* an ablation lowers pretext loss and downstream gets worse ([[wang2024eegpt]] Table 5; [[xie2026specbram]] App. C; [[coppola2024hubert]] pp. 35, 51). (B) *Across models:* bigger models or more pretraining data don't rank better ([[liu2026eeg]] pp. 21–22; [[jiang2024large]] §3.6 Fig. 5; [[coppola2024hubert]] pp. 5–6). In (B) nobody reports held-out pretext loss ([[kuruppu2026eeg]] p. 15), so "stronger on pretraining" is assumed there, not measured.
- **Ranked explanations (🤖 synthesis):**
  1. **Ill-posed pretext comparison: strongest support, explains every case of (A).** The loss value depends on how the target is defined, so a change to the target (scale, sampling rate, learnable filters) changes the loss without changing the features. EEGPT: removing target normalization drops the loss 0.56 → 0.002 by shrinking the target. SpecBraM: learnable filters let the model shrink its own targets (4×10⁻⁴), the human's "target is part of the model" case. HuBERT-ECG: 50 Hz removes hard high-frequency content. The loss also measures only one term: removing EEGPT's alignment loss left the reconstruction loss unchanged while downstream fell 6–9 points.
  2. **The objective is misaligned with the downstream task, so a better optimum can be worse.** Even with a fixed, honest target, a lower loss can come from fitting what the downstream task doesn't need: interpolating masked patches from neighbouring seconds and channels, unpredictable phase, power-dominated low frequencies (the double penalty above; [[xie2026specbram]] §4; [[yu2026neural]] abstract). LaBraM's target ablation shows no target wins on every task (App. G Table 7). The large probe-vs-fine-tune gaps ([[liu2026eeg]] Supp. Table 58; [[kuruppu2026eeg]] Supp. Table 2) are consistent with features specialised to the pretext.
  3. **Overfitting in the fine-tuning stage, not in pretraining.** Downstream sets have few *subjects* (CHB-MIT 23 people, test on 2: [[wang2024cbramod]] App. E.2), and few-shot uses ~21 trials per class ([[liu2026eeg]] Supp. Table 15). Big models lose most where data are smallest: HuBERT-ECG SMALL 0.894 vs BASE 0.756 on small CPSC-Extra, flat on large MIMIC-IV ([[coppola2024hubert]] p. 5, Table 3). Whether pretraining itself overfits can't be checked without held-out pretext loss.
  4. **Ill-posed / noisy downstream evaluation: compresses and scrambles ranks, but doesn't create a systematic inversion.** Label noise caps scores (sleep κ 0.76 between humans: [[lee2021interrater]]). CBraMod vs the top CNNs is within the Nemenyi critical difference ([[liu2026eeg]] p. 72). Many size–rank differences are therefore noise. Shortcuts make it worse: all encoders decode dataset identity at 1.000 ([[zare2026negative]], screening abstract).
  5. **Confounding across models.** Size goes together with corpus, preprocessing, architecture and objective in [[liu2026eeg]]. Corpus diversity seems to matter more than volume: LaBraM (80k channel-hours, many sources) beats ~541k mostly-TUEG models ([[kuruppu2026eeg]] p. 15). The "bigger is worse" ranks are not a clean size effect.
- **What would separate them:** the same model and target, a scaling sweep, held-out pretext loss on *other* datasets, and a layer-wise probe on several downstream tasks with enough subjects. No paper in the vault does this → experiment [[pretext-downstream-scaling-sweep]].

## Does predictability reveal what matters clinically? (asked 2026-10-12)
*The human's question: with enough data from the true distribution, would "what the model can predict" separate clinically important signal from noise?*

🤖 Mostly reasoning; vault evidence is cited where it exists. **Short answer:** predictability separates *structure from noise relative to a chosen context and loss*. Clinical relevance is a third axis that it doesn't determine.

- **What does hold:** with infinite data, an MSE model converges to the conditional mean E[target | context], and everything unpredictable from the context averages out. So it really won't learn random patterns.
- **Caveat 1: MSE only learns the mean, and for EEG rhythms the state is in the variance.** For a random-phase rhythm, E[waveform | context] decays to ~0 a few cycles away from the visible context, whatever the brain state, so an MSE model learns little about the state there. The state (e.g. strong vs weak alpha) lives in the conditional *variance/spectrum*. This is SpecBraM's argument: for a stationary Gaussian patch the periodogram is sufficient and phase carries no state information ([[xie2026specbram]] §4, App. A). "Predictable" must mean the full conditional distribution (likelihood, discrete tokens + CE, spectral or latent targets), not the mean.
- **Caveat 2: predictability is relative to the context.** A masked 1 s patch is mostly predictable from neighbouring seconds and electrodes (autocorrelation, volume conduction), so the cheapest predictable structure is local smoothness, not brain state ([[yu2026neural]] abstract). Context length, masking design and the target decide which structure counts as predictable.
- **Caveat 3: predictable ≠ relevant.** Much of the most predictable structure is nuisance: mains hum, cardiac artifact, blinks on frontal channels, electrode drift, device and montage fingerprints. All encoders decode dataset identity at 1.000 ([[zare2026negative]], screening abstract). Early FMs did no artifact removal ([[kuruppu2026eeg]] §4.1). In a clinical archive, medication effects and ICU-vs-routine recording conditions are predictable and correlate with disease without being the disease.
- **Caveat 4: unpredictable ≠ irrelevant.** The *timing* of spikes and seizure onsets is close to unpredictable from the past (otherwise seizure prediction would be solved), and these events are rare, so they add little to an average loss. What makes them learnable is the *spatial* context: a spike's field appears at the same moment on neighbouring electrodes. Spatial masking can therefore teach spike morphology, while purely temporal prediction can't.
- **Caveat 5: phase is not always clinically irrelevant.** The phase *within one channel* is mostly irrelevant for rhythms. Phase *relationships between channels* are clinical: clinicians localize a spike by **phase reversal**, where in a chain of bipolar channels (differences between adjacent electrodes) the deflection flips sign across the electrode nearest the source. Connectivity measures (coherence, PLV) also use phase ([[time-frequency-analysis]]). A target that is phase-invariant per channel but keeps cross-channel phase would fit this best.
- **Caveat 6: relevance needs an outside variable.** A perfect density model contains all information, the diagnosis included, but tangled with everything else. Long-context SSL pushes slowly varying, recording-level factors into the representation: diagnosis, but also age, drugs, device, impedance. Separating clinical factors from nuisance needs labels or interventions (e.g. the same person recorded on several devices). Predictability alone can't do it.
- **Summary grid:**

  | | clinically relevant | not relevant |
  |---|---|---|
  | **predictable** | background slowing, sleep/vigilance state, a spike's spatial field | mains hum, blinks, ECG artifact, device/montage, medication |
  | **unpredictable** | spike / seizure *timing*, onset | sensor noise, within-channel rhythm phase |

- 🤖 *Analogy:* text is already a compressed, human-designed code for meaning, so next-token prediction lands near "what matters". Raw audio isn't, which is why speech SSL moved to clustered targets (HuBERT). EEG is closer to raw audio, and the bridge [[hubert-style-pseudo-labels]] is the same move.

## Covariance matrices as pseudo-label seeds? (asked 2026-10-12)
*The human's question: if Riemannian methods are state of the art, why not cluster segment covariance matrices and use the clusters as the starting targets for self-supervised training (HuBERT iteration 1 with covariances instead of spectra)?*

- **Has anyone done it?** No EEG FM in the vault uses covariance targets. Two OpenAlex title searches (2026-10-12) found deep Riemannian networks trained *with labels*: [[wilson2025deep]] (EE(G)-SPDNet), [[kobler2022spd]] (TSMNet), and [[chen2026unified]] (covariances as transformer tokens). They also found one contrastive SSL method on covariance manifolds, [[tibermacine2026manifold]] (Manifold-SimCLR, title only), and unsupervised Riemannian *microstate* clustering [[pan2024task]] (abstract). Microstates are a classic EEG analysis: the scalp topography is clustered into ~4–7 recurring maps lasting ~100 ms each. Covariance k-means as masked-prediction pseudo-labels: **not found**.
- 🤖 **Why it is plausible:**
  - It fills a gap the other targets leave. The covariance of a band-passed segment holds per-channel band power (diagonal) *and* zero-lag cross-channel coupling (off-diagonal). It is invariant to within-channel phase but keeps spatial structure. That is close to the target asked for in *Does predictability reveal what matters clinically?* (caveat 5), though covariance only sees in-phase coupling. Lagged phase would need cross-spectral (complex) matrices.
  - Clustering is cheap: map every covariance to the tangent space at one global mean (log-Euclidean), then run ordinary k-means. No Fréchet means over millions of segments are needed.
- 🤖 **Why it is harder than it looks:**
  1. **"State of the art" is narrow.** Riemannian pipelines win in small, fixed-montage BCI data: within-subject motor imagery and cross-subject ERN ([[lawhern2018eegnet]] Figs. 2–4; [[riemannian-methods]]). There is no vault evidence that they lead on clinical tasks (abnormality, seizures, sleep). An SSL target inherits what the descriptor sees, not its leaderboard.
  2. **The success depends on band-pass filtering.** BCI covariances are computed per frequency band (filter banks, xDAWN-filtered ERPs). A broadband covariance is dominated by low frequencies (1/f) and high-amplitude artifacts. A usable target needs a filter bank, which makes it SpecBraM's band power plus off-diagonal terms ([[xie2026specbram]]).
  3. **Raw covariances cluster by recording, not by state.** Distances between subjects and sessions are large, which is why re-centering exists ([[riemannian-methods]] *Transfer*). k-means on un-centred covariances would mostly recover subject/device/montage identity, the nuisance already decodable at 1.000 ([[zare2026negative]], screening abstract). Re-centering per recording removes that, but it also removes recording-level traits such as diffuse slowing, which is the diagnosis in TUAB. Two variants are needed, and they target different things.
  4. **Channel sets vary.** A C × C matrix is defined only for one montage. FMs pretrain over >40 TUEG configurations ([[wang2024cbramod]] §3.1). You would need projection to a common subset (e.g. 19 channels of 10-20) or per-channel-pair targets → [[channel-heterogeneity]].
  5. **Estimation noise at FM patch sizes.** 19 channels give 190 free parameters, and a 1 s patch at 200 Hz gives 200 samples. Per-patch covariances are noisy and need shrinkage or windows of several seconds, so one label covers a whole multi-second, all-channel segment (Sleep2.0 granularity, not LaBraM's per-channel 1 s patches).
  6. **No morphology.** Like spectral targets, second-order statistics ignore spike shape and timing, so TUEV-type tasks shouldn't benefit.
  7. **Community split.** Riemannian work comes from small-data BCI, while FM work copies HuBERT/BEiT from speech and vision. Only 2 of 156 DL papers used Riemannian baselines ([[roy2019deep]] p. 28), and FM benchmarks still don't run one ([[liu2026eeg]]). The gap is cultural as much as technical.
- 🤖 **A test that would settle it:** filter-bank covariance k-means vs band-power k-means as HuBERT targets, with and without re-centering, everything else matched → experiment [[covariance-pseudo-labels]].

## Tokenization: HuBERT-style pseudo-labels in ECG and EEG (asked 2026-10-11)
*ECG is in scope as a method parallel since 2026-10-11. Full side-by-side comparison → bridge [[hubert-style-pseudo-labels]]. HuBERT-ECG was read in full on 2026-10-11 (medRxiv v4, fetched by hand); this replaces the earlier answer reconstructed from its code.*

- **HuBERT-ECG** [[coppola2024hubert]] (9.1M 12-lead ECGs from 4 countries, p. 10):
  - **Input:** 5 s × 12 leads at 100 Hz. The **12 leads are concatenated end to end into one 1D sequence**, and a CNN embedder turns it into 93 frames of 0.64 s (≈ one frame per 0.64 s of one lead) (pp. 11–13).
  - **Iteration 1 targets:** **39-d MFCCs** (13 + Δ + ΔΔ) per frame, k-means **k = 100** (p. 14). MFCCs beat 16 time–frequency statistics (linear probe 0.933 vs 0.913; pp. 34, 50). *Correction:* the 29-d stats + MFCC descriptor in the repo is a variant the paper tested and did not choose.
  - **Iteration 2:** k = 500 on **layer-8** hidden states (BASE). SMALL/LARGE use k = 500/1,000 on layer 9. Iteration 2 adds ~5 probe AUROC points (pp. 14, 36).
  - **Objective (confirmed):** 33% of single frames masked; cross-entropy over cluster IDs on masked frames, with logits = cosine similarity to learned cluster embeddings / τ (pp. 12–14).
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
- Is pretext-loss error usable as an unsupervised anomaly score? → experiment [[pretext-loss-anomaly-score]].
- No matched comparison of HuBERT-style clustering vs a learned codebook vs band-power regression on the same EEG data and probe.
- Do band-power targets lose on transient-morphology tasks (spikes, TUEV events), as SpecBraM's theory predicts? Not tested on TUEV in the vault.
- No EEG paper sweeps scale with one fixed target while reporting held-out pretext loss and layer-wise probes, so the causes of "better pretext, worse downstream" can't be separated yet → experiment [[pretext-downstream-scaling-sweep]].
- Does a cross-channel-phase-aware but per-channel-phase-invariant target help spike/TUEV tasks? → experiment [[cross-channel-phase-target]].
- Do filter-bank covariance k-means targets beat band-power k-means? → experiment [[covariance-pseudo-labels]].
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
- [[liu2026eeg]]: taxonomy of 55 FMs' objectives (Fig. 3h); benchmark ranks by objective family and size.
- [[coppola2024hubert]] (ECG parallel, full read): HuBERT pseudo-labels, iterative refinement, pretext loss vs probe, non-monotonic scaling.
- Bridge: [[hubert-style-pseudo-labels]] (ECG ↔ EEG, plausible).
