---
citekey: xie2026specbram
title: "SpecBraM: What Should an EEG Foundation Model Predict? Masked Band-Power Prediction versus Waveform Reconstruction"
authors: [Peng Xie, Yequan Bie, Jianda Mao, Kani Chen]
year: 2026
venue: "arXiv preprint (submitted for peer review July 2026)"
doi: ""
arxiv: "2610.07484"
pmid: ""
field: eeg
paper_type: method
task: "pretext-target study for EEG FMs; sleep staging (main), plus stress, depression, emotion, motor imagery, vigilance regression"
datasets: [TUEG, ISRUC, HMC, Mental Arithmetic, Mumtaz2016, FACED, PhysioNet-MI, SEED-VIG]
n_subjects: 2100
n_channels: 19
model_type: "masked-patch criss-cross transformer (51.3M) regressing log band power of masked patches"
eval_protocol: "strict linear probe (frozen, mean-pooled, logistic regression) + fine-tuning; subject-disjoint splits of CBraMod/CSBrain; 3 pretraining seeds"
main_metric: "balanced accuracy (strict linear probe)"
main_result: "frozen probe 0.7916/0.7425 BA on ISRUC/HMC vs 0.7755/0.7141 for matched raw-waveform reconstruction and 0.7636/0.7227 for hand-crafted spectral features (Tables 2, 4)"
code_available: false
read_depth: full
concepts: [self-supervised-pretraining, frequency-bands, sleep-staging, evaluation-protocols, time-frequency-analysis, signal-quality-and-noise]
---

# SpecBraM (Xie, Bie, Mao, Chen; arXiv 2026)

## TL;DR
A controlled ablation: same backbone, data and steps, only the masked-prediction target changes. Predicting log band power of masked patches beats raw-waveform reconstruction for frozen sleep-staging features (+1.6–2.8 BA points, +5–7 with 1% of labels). The gain does not carry over to motor imagery, depression or vigilance.

*Read from arXiv v1 (5 Oct 2026, 12 pp.). (p. N) = PDF page. HKUST group. Code release not mentioned.*

## Research question
- What should an EEG pretext target predict? The principle: "predict the physical quantity that the downstream readouts depend on, not a proxy of the signal" (§1, p. 1).
- Phase within a sub-second patch carries little state information and can't be inferred from neighbours, so waveform loss "spends much of its gradient on an irreducible component" (§1).

## Data & preprocessing
- **Pretraining:** TUEG v2.0.1, 256 Hz, 10 s windows, 19 channels (10–20), per-recording median/IQR normalisation; recordings <5 min dropped, 60 s trimmed per end, windows >150 µV rejected (§3, §5).
- Fixed random subset: 2,100 patients, 859,606 windows, **2,388 h**, same for every run (§5).
- Downstream patients were **not excluded** from pretraining "(as in prior work)" (§5).
- Patches: 200 samples (0.78 s) → 19 × 12 token grid; last 0.625 s of each window unused (§3).
- **Downstream:** ISRUC group I (80/10/10 subjects), HMC (100/25/26), using CBraMod/CSBrain splits; MA, Mumtaz, FACED (rebuilt from raw BIDS), PhysioNet-MI, SEED-VIG, all with CBraMod's preprocessing scripts (§5, App. B).

## Method
- **Encoder:** 12-layer criss-cross transformer (alternating channel/time attention), D = 512, 51.3M params; each patch masked with p = 0.3 (§3).
- **Target:** for each masked patch, 5 fixed (non-learnable) 65-tap band-pass filters → y = log(1 + mean power) per band (Eq. 1). Loss = MSE on masked patches + 0.05·SIGReg (isotropy regulariser) (Eq. 2). No reconstruction, no latent term.
- The filters' nominal centres are 2/6/10/21/38 Hz, but the measured peaks are 4.6/6/10/21/38 Hz. The "δ" filter peaks at 4.6 Hz (−3 dB band 2.9–6.3 Hz), and activity below 2 Hz is barely represented (Table 10, §3).
- **Controls (everything else matched):** raw-waveform MSE; band-waveform MSE (reconstruct the 5 filtered waveforms); band power via per-patch FFT with standard bands; leak-free per-patch filtering; frequency-axis masking (Table 1). A 2×2 design crosses target × tokenizer (linear patch embedding vs learnable 5-band filterbank) (Table 2).
- **Theory (§4, App. A):** for a stationary Gaussian patch whose state acts only through its spectrum, the periodogram is sufficient and phase is ancillary (Prop. 1). Band-averaged power is the MLE of band levels (Prop. 2). Log power has state-independent variance ≈ 1/m_b (Prop. 3). Any target's Bayes risk = posterior state uncertainty + an irreducible term (Prop. 5). For the waveform, the irreducible term is the patch's own innovation, which scales with power and is dominated by low frequencies under 1/f.
- Predictions: band power helps linear readout of spectral states, especially with few labels; band-waveform reconstruction won't help; the advantage shrinks for transient-shape or cross-channel-phase tasks (§4, p. 4).

## Evaluation
- **Strict linear probe (primary):** frozen encoder, mean-pooled tokens, standardised, class-balanced logistic regression, C ∈ {0.01, 0.1, 1} chosen on validation, test scored once. A 30 s sleep epoch = mean of three 10 s windows (§5).
- Label efficiency: 1–50% of training epochs, 5 fixed subsets shared by all models (§5).
- External baselines (BIOT, CBraMod, LaBraM-Base official weights) probed in their own input conventions; REVE numbers quoted (§5, Table 4).
- Hand-crafted baselines: 5-band log/relative power; a "rich" set (1 Hz log PSD 0.5–45 Hz, relative power in 6 bands, Hjorth, spectral entropy, spectral edge, line length, kurtosis) (§6.2).
- Fine-tuning (sleep): sequences of 20 epochs + 1-layer transformer head, early stopping on validation BA (§5).

## Results (with locations)
- **Target > tokenizer.** BP vs raw, linear tokenizer: ISRUC 0.7916 vs 0.7755 (+1.6), HMC 0.7425 vs 0.7141 (+2.8); filterbank tokenizer +1.9/+2.1; positive on 12/12 seed–dataset pairs. At 1% labels +5.2/+7.3 (linear) (Table 2). Tokenizer effect smaller (0.7916 vs 0.7863 ISRUC) (§6.1).
- **All band-power variants ≈, all waveform variants lower.** BP variants 0.7827–0.7906 (ISRUC), 0.7339–0.7398 (HMC); raw recon. 0.7677/0.7180; band-waveform 0.7682/0.7119; frequency-axis masking worst 0.7639/0.7051 (Table 1). The authors say band-waveform also changes output size and loss scale, so it is "not a clean attribution" (§6.1).
- **Early in training:** BP at epoch 4 (0.7719/0.7418) > raw at epoch 16 (0.7680/0.7190) (Table 3).
- **vs published FMs, frozen:** ISRUC/HMC BA: LaBraM-Base 0.7523/0.6323, CBraMod 0.7278/0.6190, BIOT ≤0.7430/0.6578, random-init same arch 0.6884/0.6256; REVE-Large (quoted, own protocol) 0.758/0.710 (Table 4).
- **vs hand-crafted:** rich set 0.7636/0.7227, above every external FM under this probe and above same-arch raw recon. on HMC. SpecBraM +2.8/+2.0 at 100% but only ~1 point at 1% (0.760/0.685 vs 0.747/0.674) (Tables 4–5, §6.2). Probes picked the lowest C on hand-crafted features, so a wider grid might help them (§6.2).
- **Label efficiency:** SpecBraM at 1% labels (0.760/0.685) beats every external FM at 100%. Same-arch raw recon. needs 10–25% of labels to match it (Table 5, §6.2).
- **Fine-tuned sleep:** 0.8107/0.7669 BA vs CSBrain 0.7925/0.7345, CBraMod 0.7865/0.7269, EEGNet 0.7154/0.6534; same-arch raw recon. 0.8008/0.7550, so the target gap shrinks to ~1 point after fine-tuning (Table 6, §6.3).
- **Beyond sleep (frozen, vs official CBraMod/LaBraM):** MA 0.752 vs 0.653/0.681; Mumtaz 0.935 vs 0.893/0.876; FACED 0.241 vs 0.171/0.167; PhysioNet-MI 0.388 vs 0.312/0.299 (Tables 7–8).
  - But CBraMod's frozen backbone *with its own head on all tokens* reports 0.315 (FACED) / 0.385 (MI). Mean-pooling halves the gap, so "part of the gap there reflects the probing head rather than the representation" (§6.4, Table 8).
- **BP vs raw beyond sleep is mixed:** FACED +2.4/+2.2; MA +8.6 (linear) but −3.7 (filterbank; 4 test subjects); Mumtaz tie; PhysioNet-MI −0.9/+0.3 (§6.4, Tables 7–8). Reason given: MI's µ/β changes are spatially localised and lateralised, and a per-channel band target over 0.78 s patches may not emphasise them (§6.4).
- **Vigilance (SEED-VIG, PERCLOS regression):** frozen Pearson 0.565 (BP) vs 0.548 (raw), R² 0.166 vs 0.209; fine-tuned raw better (0.626/0.357 vs 0.587/0.260). High-passing input at 4 Hz lifts BP to 0.619 but not raw (0.572) (Table 9, §6.5). Hypothesis (untested): ocular artifacts dominate the lowest target bands and mask alpha/theta drowsiness changes (§6.5).
- **Earlier experiments (App. C, different launcher, not directly comparable):**
  - Learnable target filters collapse: loss 4×10⁻⁴ from shrinking the filters, uninformative features.
  - SIGReg alone (no band-power term): chance-level fine-tuned BA 0.2124/0.2737.
  - **Data scale:** full TUEG (~17,666 h) 0.7899/0.7526 vs the 2,388 h subset 0.7928±0.0027/0.7505±0.0019 over 3 subsets: "statistically indistinguishable" (10 s fine-tuning protocol).
- **Reproducibility catch:** CBraMod's released SEED-VIG script sorts files lexicographically ('10_' before '1_'), unlike the paper's subject-ordered split. The test-label SD implied by CBraMod's reported R²/RMSE (0.318) matches the subject-ordered split, not the lexicographic one (0.175) (App. B).

## Limitations (reported)
- Target uses overlapping narrow filters and log(1+P). <2 Hz is not represented, and log(1+P) is nearly linear for small high-band energies, so the variance-stabilising argument holds only partly (§7).
- Mean-pool probe doesn't use the baselines' own heads (§7). Small cohorts (MA: 4 test subjects). Downstream recordings may overlap TUEG. TUAB evaluation "in progress". One data budget and one model size (§7).
- The theory assumes stationarity, Gaussianity, spectrum-only state; real EEG has transients, heavy tails and cross-channel phase (§7).
- External-FM comparisons differ in data, duration and architecture, so they don't establish data efficiency (§1, §6.3).

## Assessment 🤖
- 🤖 The strongest part is the matched ablation (3 seeds, 2×2 design, controls). It is the cleanest evidence in the vault that the *target* changes frozen features. Everything else (beating CBraMod/LaBraM) is protocol-dependent, as the authors admit for FACED/MI.
- 🤖 Sleep staging is the best case for a spectral target: AASM stages are defined by band content. The paper's own failures (MI, vigilance, depression tie) fit its theory, so it is the right claim at the right scope, not a general FM recipe.
- 🤖 Irony: the "δ" target barely covers <2 Hz, where sleep slow waves (N3) live. That the target still wins on sleep suggests the encoder recovers slow-wave information from context or from the 4.6 Hz-peaked band's skirt; a slow-wave-aware band might help more.
- 🤖 The gap shrinks to ~1 point after fine-tuning. So the target choice matters mostly for frozen / low-label use, which is the setting the vault cares about in Q7.
- 🤖 The full-TUEG ≈ 2,388 h result (App. C) is a small, under-controlled but direct data-scale null. It fits the "scaling evidence weak" picture of [[kuruppu2026eeg]] and [[liu2026eeg]].
- 🤖 SIGReg alone → chance level is a useful negative control: the regulariser does not carry the representation.
- 🤖 No code, and the mean-pool probe can disadvantage models with CLS-like or position-specific features ([[sirca2026beyond]] makes this point). The "beats all published FMs frozen" headline should be read with that caveat.

## Concepts
- [[self-supervised-pretraining]]: masked band-power regression as a fourth target family; matched target ablation.
- [[frequency-bands]]: band edges as conventions; narrow vs standard bands give similar results (Table 1, §3).
- [[sleep-staging]]: main evaluation task; fine-tuned SOTA on ISRUC/HMC (Table 6).
- [[evaluation-protocols]]: strict linear probe; downstream patients in pretraining; CBraMod SEED-VIG split bug (App. B).
- [[time-frequency-analysis]]: periodogram/Whittle argument for why power, not phase, carries state (App. A).
- [[signal-quality-and-noise]]: ocular artifacts likely contaminate low-band targets on vigilance (§6.5).

## Related papers
- [[jiang2024large]]: LaBraM, VQ codes of Fourier amplitude + phase; a baseline that loses to SpecBraM frozen (Table 4).
- [[wang2024cbramod]]: CBraMod, the raw-reconstruction design SpecBraM copies (criss-cross, linear patch embedding) and changes only the target.
- [[liu2026eeg]]: the matched FM benchmark; both find hand-crafted / small baselines close to FMs.
- [[kuruppu2026eeg]]: review where scale evidence is "weak"; SpecBraM's App. C adds a direct data-scale null.
- [[lawhern2018eegnet]]: EEGNet is the weakest fine-tuned baseline on sleep (Table 6).
- [[coppola2024hubert]]: ECG parallel; HuBERT's MFCC clusters are cited as the same "hand-crafted feature as target" idea (§2).
- [[yu2026neural]]: shortcut argument against masked raw prediction (screening).
- [[sirca2026beyond]]: pooling explains weak frozen probes (screening), relevant to the mean-pool caveat.

## Q&A notes
- 2026-10-12 **Q:** Is band power predicted per channel? Which devices? Does the result show that raw-reconstruction FM features can't even linearly encode log band power, i.e. that the objective is ill-defined and the FM fails to hold the EEG's information?
  **A:**
  - *Per channel:* yes. One 5-vector per masked (channel, 0.78 s patch) token, predicted by a linear head from that token's encoder output, using the other channels and times as context (Eq. 1–2, §3). No cross-channel target.
  - *Devices:* not stated in the paper. TUEG is clinical hospital EEG (Temple University); ISRUC and HMC are sleep-lab PSG. The vault has no source for the amplifier models. All inputs are reduced to 19 standard 10–20 leads at 256 Hz (§3, App. B).
  - *What was actually tested:* a linear probe for **sleep stage** on **mean-pooled** features, not a probe for band power. Raw-reconstruction features are only 1.6–2.8 points worse (0.776 vs 0.792 ISRUC) and beat the rich hand-crafted spectral set on ISRUC (0.776 vs 0.764) (Tables 2, 4). After fine-tuning the gap is ~1 point (Table 6). So the raw model's features are not failing at something simple; they expose spectral state a bit less linearly. Whether per-token band power is linearly decodable from them was not measured → [[property-probe-battery]]; [[kommineni2026aperiodic]] reports reconstruction FMs biased to low-frequency / aperiodic content (abstract).
  - 🤖 *Pretext error vs information:* the user's expectation is right that raw-MSE error stays high. Its Bayes-optimal error includes the masked patch's own random amplitude and phase, which no model can predict from context (Prop. 5, App. A). But that measures how unpredictable the *masked data* is, not how much information the *features* hold: even a perfect model would keep this error. High pretext loss ≠ missing information.
  - 🤖 Band-power error is not small either. With 0.78 s patches, δ/θ log power has only 3 Fourier bins, so the irreducible sd is ≈0.63 log units (a factor ~1.9) (Table 11). The paper reports no pretext loss values for either target.
  - 🤖 *Ill-defined?* No: raw MSE is well defined. It is **misaligned**: much of its gradient goes to irreducible phase detail and to power-dominated low frequencies, so the representation is shaped around what the downstream label doesn't need. → [[q9-pretraining-objectives-and-scale]] (*double penalty*, *Why pretext gains don't transfer downstream*).
  - 🤖 The closer version of the worry is about *published* FMs: frozen LaBraM/CBraMod read out sleep stage worse than hand-crafted spectral features (Table 4). Mean-pooling and readout heads explain part of this (§6.4), so it shows spectral state isn't *linearly exposed*, not that it is absent.
- 2026-10-12 **Q:** Is this squeezing publishable gains out of a downstream task too noisy for meaningful improvements?
  **A:** 🤖 Partly, depending on which claim.
  - *Squeezing:* the fine-tuned SOTA claim (ISRUC κ 0.756 vs CSBrain 0.741, BA +1.8; Table 6) compares against quoted numbers. It sits at the human inter-scorer ceiling (κ 0.76 [[lee2021interrater]]), and the error bars are over pretraining seeds only, with no CI over the 10 ISRUC / 26 HMC test subjects (§5, Table 6). Beyond sleep, MA has 4 test subjects and swings ±8 points with the tokenizer (Table 7). Mumtaz is saturated: a random-init encoder probes at 0.871 (Table 7).
  - *Not squeezing:* the matched frozen comparison is paired (same seed, same test set). It is positive on 12/12 seed–dataset pairs, its 1%-label gap (+5–7) is well above the seed sd (≤1.6), all 3 band-power variants beat both waveform variants, and band power at epoch 4 beats raw at epoch 16 (Tables 1–3). The failures are reported. Shared test-subject noise affects both arms of a paired comparison similarly, but no subject-level paired test is given.
  - *Net:* trust the direction and the low-label effect, not the size at 100% labels and not the SOTA row. Sleep staging is a poor arena for ranking near the ceiling → [[sleep-staging]] (*why benchmark on it?*). Better tests: TUAB (in progress, §7), TUEV, with subject-level bootstrap CIs.
