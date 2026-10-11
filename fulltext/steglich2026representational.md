<!-- source: pdf/steglich2026representational.pdf | converter: pymupdf -->

<!-- page 1 -->

# Representational and Functional Robustness to Electrode Montages in EEG Foundation Models

Jakob Steglich1 Justus Meyer zu Bexten1,2 Shakiba Moradi3,4 Laure Ciernik4,5

Simon M. Hofmann1,∗ Mina Jamshidi Idaji3,4,∗

1 Max Planck Institute for Human Cognitive and Brain Sciences, Leipzig, Germany 2 ScaDS.AI Dresden/Leipzig 3 BIFOLD–Berlin Institute for the Foundations of Learning and Data, Berlin, Germany 4 Machine Learning Group, Technische Universität Berlin, Berlin, Germany 5 Hector Fellow Academy, Karlsruhe, Germany ∗Equal supervision contribution Correspondence to: mina.jamshidi.idaji@tu-berlin.de

## Abstract

EEG foundation models (EEG-FMs) are intended to generalize across different datasets by learning representations that, ideally, are invariant to dataset-specific EEG configurations such as electrode montages. However, EEG-FMs that accept different montages as input do not guarantee that representations and predictions remain stable across different electrode configurations, especially outside the train- ing setting. In this work, we investigate the effects of different electrode montages through a joint functional and representational analysis of four EEG foundation models selected to span distinct montage-handling designs. We evaluate embed- dings on cross-subject resting-state eyes-open/closed and within-subject motor- imagery classification under spatially informed channel reduction. Functional robustness is tested through the generalizability of linear probes across channel counts, while representational robustness is assessed through within-subject sim- ilarity and preservation of between-subject geometry. The four models show dis- tinct robustness profiles, and the two axes dissociate: large changes in embedding similarity need not come with comparable probe degradation, and stable embed- dings can still lose downstream performance. Comparing two readouts of the same encoder further shows that aggregation, not the encoder alone, determines functional robustness: pooling into anatomically aligned regions degrades less than a learned global readout, despite being montage-invariant by construction. Montage robustness is therefore a joint property of the encoder and its aggrega- tion, and characterizing it requires both a representational and a functional axis. Input compatibility alone is evidence for neither.

## 1 Introduction

Electroencephalography (EEG) datasets vary not only in their objectives and participants, but also in their hardware setup, such as electrode layout (montage). Computational and statistical models of EEG are usually tuned to a specific dataset and rarely transfer to other studies and applications, particularly to out-of-lab deployments where electrode count and position differ from the recording setup. Recent large, pretrained EEG foundation models (EEG-FMs) leverage deep learning methods on heterogeneous datasets with the promise to overcome this lack of transferability [Aristimunha

Preprint.

# arXiv:2609.36288v1  [cs.LG]  28 Sep 2026

<!-- page 2 -->

et al., 2025, Xiong et al., 2026], ideally extracting representational spaces from diverse data that are channel- and task-invariant.

Existing EEG-FMs follow various strategies to accommodate different electrode montages. Chan- nels are modeled independently [Sukhbaatar et al., 2025], or together through explicit spatio- temporal attention [Wang et al., 2024b]. Some approaches unify them in fixed-size latent repre- sentations [Döner et al., 2025, Ouahidi et al., 2025], using Perceiver-style [Jaegle et al., 2021] cross- attention (structured overview in Appendix A). Despite efforts to accommodate various channel setups in the input domain of EEG-FMs, their ability to extract representations invariant to electrode configurations remains largely unexplored.

To address this gap, we present a joint functional and representational analysis of montage robust- ness in four EEG-FMs selected to span distinct montage-handling designs. We study a common setting in EEG-FM deployment, in which a downstream predictor encounters a different number of channels during inference than were available during pretraining. We assess functional robustness (the effect on a model’s output) by testing the generalizability of linear probes across channel counts and representational robustness (the effect on latent embeddings) [Klabunde et al., 2025] through the preservation of within-instance and between-subject representational similarity. We evaluate these properties on cross-subject eyes-open/closed and within-subject motor-imagery classifications. Across these settings, representational and decision stability do not consistently coincide, indicating that both dimensions are needed to characterize overall montage robustness.

## 2 Related Work

Recent benchmarks have shown that EEG-FMs frequently fail to match specialist baselines [Liu et al., 2026] and often encode dataset origin rather than transferable clinical features [Zare, 2026]. Their robustness to variations in electrode montages has been recently addressed through adaptation methods [Ma and Ruotsalo, 2026, Kokate et al., 2026] and evaluation protocols based on chan- nel masking, sparse subsampling, or lobe-restricted montages [Li et al., 2025, Kommineni et al., 2026]. Širca et al. [2026] perturbed six EEG-FMs with noise and random or region-based channel dropout, reporting degradation in all of them and greater tolerance to electrode omission than to zero-masking.

Whereas these studies evaluate downstream robustness or methods for adapting models to montage mismatch, our work asks whether channel-count reductions alter representations in ways that corre- spond to downstream functional stability (cf. [Klabunde et al., 2025, Ding et al., 2021]).

## 3 Methods

3.1 Foundation Model Embeddings from EEG Data

Evaluated models. We evaluated four state-of-the-art EEG-FMs, namely SingLEM [Sukhbaatar et al., 2025], CBraMod [Wang et al., 2024b], LUNA [Döner et al., 2025], and REVE [Ouahidi et al., 2025]. These represent four categories of channel fusion strategies in EEG-FMs (Appendix A), and enable us to investigate how this architectural aspect contributes to montage robustness.

Across all four models, we denote a multi-channel EEG recording by S ∈RC×T , where C is the number of EEG channels, and T the number of time points. Each model segments S into P temporal patches of Tp time points (patches may overlap, depending on the model), yielding a patched tensor Sp ∈RC×P ×Tp. SingLEM, CBraMod, and REVE project to per-channel em- beddings E ∈RC×P ×F with F being the embedding dimension, while LUNA fuses the channel dimension into Q learned query tokens, yielding E ∈R(Q·P )×F ; we set Q = 4 following the orig- inal implementation. Furthermore, REVE obtained a global query token during pretraining, which can be used to reduce its embedding to E ∈RF with attention pooling; we denote this readout of REVE as REVE-A. See Appendix B for more details.

Embedding tensors and their pooling. The main challenge in investigating the robustness of EEG-FMs to changes in the channel montage is to project their embeddings to a montage-agnostic space. For this purpose, we introduce a region-of-interest (ROI) pooling strategy ϕ : RC×P ×F → RR×P ×F , ϕ(E)r,:,: = |Rr|−1 P

c∈Rr Ec,:,: (details in Appendix B), which averages feature vectors

2

<!-- page 3 -->

within R ROIs Rr ⊆{1, . . . , C}, r = 1, · · · , R, mapping embeddings to the same spatial dimen- sionality regardless of channel count. We set R = 10 and depict the ROIs in Figure S1. Because LUNA and REVE-A use a built-in channel fusion module, their embedding outputs are already montage-agnostic. Therefore, they are not directly comparable to other models. Note, [Döner et al., 2025] demonstrate how LUNA’s queries learn distinct spatial profiles, similar to ROIs. We report our results both for REVE with ROI pooling (REVE-ROI), and with attention pooling (REVE-A). For linear probing, ϕ(E) or E is flattened to RRP F (roi-concat-all) or RCP F (concat-all), of which only the former is montage-independent.

3.2 Datasets and preprocessing

Tasks. We include two complementary tasks in our experiments: (1) cross-subject classification of eyes closed vs. open resting-state (RS) data and (2) intra-subject, trial-level classification of hand movement-imagery (MI) data. For (1), closing and opening eyes has a known and pronounced neural basis, including higher alpha-band activity at the occipital region; therefore, we expect a high cross-subject classification performance. In (2), hand MI is a localized, event-related activity and has an acceptable intra-subject discriminative performance [Pfurtscheller and Neuper, 2001]1. The datasets are class-balanced, and we report AUROC as performance metrics.

Datasets. We used a 100-participant subset of the 129-channel Healthy Brain Network (HBN) EEG dataset [Shirazi et al., 2024] for cross-subject eyes open versus closed classification. We retrieved 4-s epochs from each of ten trials per participant. As channel Cz was used as reference during recording, we retained only the 128 GSN-HydroCel montage in our analyses and changed the reference to common-average. For the MI task, Lee et al. [2019] provide a dataset recorded with 62 electrodes in the standard-1005 montage from 52 participants instructed to imagine left- or right-hand movement. We used the 4-s imagery segments of the 200 labeled imagery trials per subject (see dataset details in Appendix C). The RS data was not used for pretraining of any model, while the MI dataset was present in the SingLEM pretraining corpus.

## 4 Experiments

4.1 Experiment 1: Functional cross-montage robustness

Protocol. We trained linear probes [Alain and Bengio, 2018], implemented with logistic regression, on embeddings from an N-channel training montage and evaluated them on an M-channel test montage (N2M-probes; M = N gives the within-montage N2N case). We focus on the deployment- relevant direction M < N, although Figure 1 reports the full grid (see Appendix D for details).

Within-montage baselines. To compare the raw discriminative information available in the native embeddings of each montage, we first tested N2N-probes with concat-all as the pooling, which preserves the full embedding tensor and is therefore the least constrained of the evaluated pooling methods. We observe no clear performance differences among channel montages within any FM, indicating comparable classification-relevant information content across montages (Figure 1-(a, b), Table S3). Moreover, ROI-concat-all consistently outperforms channel averaging on both datasets and trails concat-all only slightly (Table S4), so it retains enough task-relevant information while keeping a montage-independent dimensionality.

The following two experiments are done with ROI-concat-all as the pooling method with R = 10, see Figure S7 for results for R = 20 for RS data.

Experiment 1.1: Decision stability under matched samples. We first evaluated probes on the same samples used for training, changed only in montage, so that any train-test difference is at- tributable to the montage alone. Figure 1-(b,c) demonstrate an N2N-probe performance (diagonal) approximating to 1 across models and datasets. Thus, the probes are able to memorize the sam- ples. For the N2M-probes (off-diagonal), we observe minimal drops for CBraMod and REVE-ROI, and pronounced drops for LUNA and REVE-A in both tasks. SingLEM differs between the tasks, showing performance degradation in the RS task only. REVE-A shows the largest drops despite sharing an encoder with the most robust setting, REVE-ROI, which points to the readout rather than

1Note, previous reviews of EEG-FMs [Liu et al., 2026] and our own experiments indicate that cross-subject generalization does not yield sufficient classification performance for the MI dataset.

3

<!-- page 4 -->

CBraMod

LUNA

REVE

SingLEM

0.5

1.0

AUROC

a

Resting-State

32-ch 64-ch 128-ch

CBraMod

LUNA

REVE

SingLEM

0.5

1.0

AUROC

Motor Imagery

16-ch 32-ch 62-ch

32 64 128

32

64

128

train montage (ch)

b

CBraMod

32 64 128

LUNA

32 64 128 eval montage (ch)

REVE ROI

32 64 128

REVE A

32 64 128

SingLEM

0.7

1.0

AUROC

16 32 62

c

CBraMod

16 32 62

LUNA

16 32 62 eval montage (ch)

REVE ROI

16 32 62

REVE A

16 32 62

SingLEM

0.7

1.0

AUROC

32 64 128

32

64

128

train montage (ch)

d

CBraMod

32 64 128

LUNA

32 64 128 eval montage (ch)

REVE ROI

32 64 128

REVE A

32 64 128

SingLEM

0.7

1.0

AUROC

16 32 62

e

CBraMod

16 32 62

LUNA

16 32 62 eval montage (ch)

REVE ROI

16 32 62

REVE A

16 32 62

SingLEM

0.5

0.7

AUROC

Figure 1: Functional within- and cross-montage robustness. (a) Within-montage baselines (N2N- probes with concat-all as pooling) for inter-subject RS and intra-subject MI classification; bars show mean AUROC and standard deviation across seeds (n=10) for RS and subjects for MI (Table S3). (b, c) N2M-probes on RS and MI, respectively, with matched train and test samples, and (d, e) with held-out test data. Rows give the training and columns the test montage. The full montage has 128 channels for RS and 62 for MI (Appendix C).

the representation: a learned global query attending over the available channel-patch tokens is itself montage-conditioned, whereas ROI averaging is montage-invariant by construction. Furthermore, the drops of LUNA and REVE-A are smaller for RS than for MI, consistent with MI relying on a spatially focal set of sensorimotor channels [Pfurtscheller and Neuper, 2001] that is more vulnerable to channel removal than the diffusely distributed eyes-open/closed signal. LUNA and REVE-A are especially affected by these task-specifics, because their focal representation is redistributed across latent dimensions. This is in contrast to channel- and ROI-indexed readouts.

Experiment 1.2: Cross-montage generalization to held-out data. To measure cross-montage generalization to new subjects for RS or epochs for MI, we train N2M-probes with subject- and epoch-level data splitting, respectively. Here, the performance difference between the N2N- and N2M-probes reflects the model’s ability to generalize across channel counts in unseen data. AUROC is considerably lower for MI than for RS (Figure 1-(d, e)), and MI performance varies strongly across subjects (0.11–0.14 AUROC, Appendix E). For RS, no consistent pattern of cross-montage generalization emerges: CBraMod, LUNA, and REVE-ROI perform best overall, with CBraMod and REVE-ROI showing the smallest montage-related drops, and SingLEM appearing robust but at a substantially lower baseline. REVE-A again performs worst and is the only setting reproducing the degradation pattern of Experiment 1.1. The MI results follow the same ordering, with a more pronounced advantage for REVE-ROI, but here CBraMod, LUNA, and REVE-A all lose AUROC under montage change, most strongly REVE-A and least strongly CBraMod.

4.2 Experiment 2: Representational similarity

Protocol. We compare the embedding of the full recording montage ECfull to that of a spatially informed subsampled montage, ECsub, assessing within-subject consistency (cosine similarity; for Wasserstein distance, see Appendix B) and across-subject structure (CKA [Kornblith et al., 2019]). Both are compared using roi-concat-all as the pooling for cosine similarity and CKA, except for LUNA, which bypasses ϕ and is compared with concat-all. For each subject we recompute the embeddings for three EEG epochs per label across all subsampled montages. Figure S2 illustrates some of the subsampled channel sets.

Experiment 2.1: Within-subject representation similarity. The cosine similarity quantifies how an EEG embedding of a subject changes in comparison to the original montage as the channels are subsampled. A high cosine similarity suggests that the overall direction of the embedding vector changes little under the channel perturbation. Similarities rise towards 1 as Csub increases (Figure 2- (a), starting around 0.75 for all FMs except CBraMod, which starts near 0.5. The MI data show the

4

<!-- page 5 -->

10 34 58 82 106 128 Csub

0.25

0.50

0.75

1.00

Cosine Similarity

a

10 34 58 82 106 128 Csub

0.25

0.50

0.75

1.00

CKA

b

CBraMod REVE A REVE ROI SingLEM LUNA

Figure 2: Representational cross-montage robustness for resting-state EEG. Each point com- pares the embedding of the full montage (Cfull) to that of a subsampled montage with Csub channels, displayed on the x-axis. For within-subject similarities, each point is an average over subjects; vari- ance is displayed over the first three EEG epochs per label (six trials per subject). (a) Within-subject cosine similarity. (b) Centered Kernel Alignment (CKA) between the subject-to-feature matrices of the two montages.

same pattern with an even larger gap for CBraMod (Figure S3). ROI-level cosine similarities and Wasserstein distances give a consistent picture (Figure S4).

Experiment 2.2: Between-subject alignment. CKA quantifies how much the pairwise structure be- tween subject embeddings changes under subsampling. Stacking the flattened ϕ(ECfull) and ϕ(ECsub) of K subjects gives Xfull, Xsub ∈RK×RP F , on which we evaluate CKA(Xfull, Xsub). Figure 2-(b) exhibits trajectories of CKA as the channels are subsampled: the cross-subject structure becomes more aligned as Csub approaches Cfull. The differences between FMs are small; only REVE-A embeddings are less aligned up to approximately Csub = 50 channels, where it matches the other models. This illustrates an overall preservation of subject-specific differences in FM embeddings during montage perturbation. Figure S3-(b) shows the resulting curves for MI data.

## 5 Discussion and Conclusion

Our results show that montage robustness is not a single property of an EEG foundation model. Stability of individual embeddings, preservation of between-subject geometry, and transfer of down- stream decisions did not produce a consistent model ranking.

For instance, representations changed in CBraMod under channel reduction without corresponding large performance losses; LUNA kept high within-instance similarity but lost downstream perfor- mance across settings; SingLEM varied by task and evaluation regime at a lower baseline, and REVE depended strongly on its readout. These differences indicate that representational similarity alone cannot predict whether a downstream model will remain functional under montage change.

The contrast between REVE’s readouts provides the clearest evidence that robustness also depends on aggregation. ROI-pooled channel-wise embeddings showed smaller functional changes than the pretrained global attention readout, despite both originating from the same encoder. ROI-pooling provides anatomically aligned feature positions across channel counts, whereas the global readout recomputes a summary from the channel-patch tokens available in each montage. This may make the global representation more sensitive to changes in channel availability. However, ROI pooling is stabilizing by construction, so the result should not be read as a property of the REVE encoder but as evidence that anatomically aligned aggregation is a useful interface between variable-channel representations and downstream predictors.

We note some limitations for our study. The cross-model patterns are consistent with architec- tural hypotheses but do not identify their causes. The high within-instance similarity observed for LUNA and REVE may reflect their stronger integration of information across channels. Yet, while CBraMod processes cross-channel interactions, as well, it exhibits substantially lower sim- ilarity. The evaluated models further differ in pretraining data, positional encoding, model size, feature dimensionality, and other design choices. Moreover, we tested each model with preprocess- ing matched to its pretraining configuration, mitigating distribution shifts. However, this limits the attribution of differences between models to their architecture alone. Model differences therefore

5

<!-- page 6 -->

characterize the complete pretrained systems rather than isolating the effect of any single channel- fusion mechanism.

Taken together, EEG-FMs that accept variable channel configurations at the input do not guarantee that representations or downstream predictions remain stable when montage/channel availability changes between training and deployment. Evaluations should therefore examine both axes and treat the aggregation method as part of the robustness pipeline: robust deployment may require not only encoders that accept variable electrode sets, but readouts that preserve stable, task-relevant feature organization across them.

## Acknowledgments and Disclosure of Funding

Justus Meyer zu Bexten is supported the Federal Ministry of Research, Technology and Space of Germany and by Sächsische Staatsministerium für Wissenschaft, Kultur und Tourismus in the pro- gramme Center of Excellence for AI-research „Center for Scalable Data Analytics and Artificial Intelligence Dresden/Leipzig“, project identification number: ScaDS.AI. Laure Ciernik is funded by the Hector Fellow Academy and is grateful for their support.

## Author Contributions

Jakob Steglich: Methodology, Software, Validation, Formal analysis, Investigation, Data Curation, Writing - Original Draft, Visualization, Project administration Justus Meyer zu Bexten: Method- ology, Writing - Original Draft, Software, Investigation Shakiba Moradi: Methodology, Writing - Original Draft, Investigation Laure Ciernik: Investigation Simon M. Hofmann: Methodology,

Validation, Investigation, Supervision, Project administration Mina Jamshidi Idaji: Conceptualiza- tion, Methodology, Validation, Visualization, Investigation, Writing - Original Draft, Supervision, Project administration All authors: Writing - Review & Editing

## References

Guillaume Alain and Yoshua Bengio. Understanding intermediate layers using linear classifier probes, November 2018. URL https://arxiv.org/abs/1610.01644.

Bruno Aristimunha, Dung Truong, Pierre Guetschel, Seyed Yahya Shirazi, Isabelle Guyon, Alexan-

dre R. Franco, Michael P. Milham, Aviv Dotan, Scott Makeig, Alexandre Gramfort, Jean-Remi King, Marie-Constance Corsi, Pedro A. Valdés-Sosa, Amit Majumdar, Alan Evans, Terrence J. Sejnowski, Oren Shriki, Sylvain Chevallier, and Arnaud Delorme. EEG Foundation Challenge: From Cross-Task to Cross-Subject EEG Decoding, June 2025. URL https://arxiv.org/abs/ 2506.19141.

Danaé Broustail, Anna Tegon, Thorir Mar Ingolfsson, Yawei Li, and Luca Benini. LuMamba: La-

tent Unified Mamba for Electrode Topology-Invariant and Efficient EEG Modeling, 2026. URL https://arxiv.org/abs/2603.19100.

Zhige Chen, Chengxuan Qin, Wenlong You, Rui Liu, Congying Chu, Rui Yang, Kay Chen Tan, and

Jibin Wu. HEAR: An EEG Foundation Model with Heterogeneous Electrode Adaptive Represen- tation, 2025. URL https://arxiv.org/abs/2510.12515.

Mingzhe Cui, Tao Chen, Yang Jiao, Yiqin Wang, Lei Xie, Yi Pan, and Luca Mainardi. BrainRVQ: A

High-Fidelity EEG Foundation Model via Dual-Domain Residual Quantization and Hierarchical Autoregression, 2026. URL https://arxiv.org/abs/2602.16951.

Wenhui Cui, Woojae Jeong, Philipp Thölke, Takfarinas Medani, Karim Jerbi, Anand A. Joshi, and

Richard M. Leahy. Neuro-GPT: Towards A Foundation Model For EEG. In 2024 IEEE In- ternational Symposium on Biomedical Imaging (ISBI), pages 1–5, Athens, Greece, May 2024. IEEE. ISBN 979-8-3503-1333-8. doi: 10.1109/ISBI56570.2024.10635453. URL https: //ieeexplore.ieee.org/document/10635453/.

Frances Ding, Jean-Stanislas Denain, and Jacob Steinhardt. Grounding representational similarity

with statistical testing. In Advances in Neural Information Processing Systems, 2021.

6

<!-- page 7 -->

Berkay Döner, Thorir Mar Ingolfsson, Luca Benini, and Yawei Li. LUNA: Efficient and Topology-

Agnostic Foundation Model for EEG Signal Analysis. In The Thirty-ninth Annual Conference on Neural Information Processing Systems, October 2025.

Zitao Fang, Chenxuan Li, Hongting Zhou, Shuyang Yu, Guodong Du, Ashwaq Qasem, Yang Lu,

Jing Li, Junsong Zhang, and Sim Kuan Goh. NeurIPT: Foundation Model for Neural Interfaces, 2025. URL https://arxiv.org/abs/2510.16548.

Jiazhen Hong, Geoffrey Mackellar, and Soheila Ghane. SAMBA: Toward a Long-Context EEG

Foundation Model via Spatial Embedding and Differential Mamba, 2025. URL https://arxiv. org/abs/2511.18571.

Andrew Jaegle, Felix Gimeno, Andy Brock, Andrew Zisserman, Oriol Vinyals, and Joao Carreira.

Perceiver: General perception with iterative attention. In International Conference on Machine Learning, 2021.

Wei-Bang Jiang, Yansen Wang, Bao-Liang Lu, and Dongsheng Li. NeuroLM: A Universal Multi-

task Foundation Model for Bridging the Gap between Language and EEG Signals, 2024a. URL https://arxiv.org/abs/2409.00101.

Wei-Bang Jiang, Li-Ming Zhao, and Bao-Liang Lu. Large Brain Model for Learning Generic Rep-

resentations with Tremendous EEG Data in BCI, 2024b. URL https://arxiv.org/abs/2405. 18765.

Max Klabunde, Tobias Schumacher, Markus Strohmaier, and Florian Lemmerich. Similarity of Neu-

ral Network Models: A Survey of Functional and Representational Measures. ACM Computing Surveys, 57(9):242:1–242:52, May 2025. ISSN 0360-0300. doi: 10.1145/3728458.

Kuntal Kokate, Bruno Aristimunha, Dung Truong, and Arnaud Delorme. Channel adaptation for EEG foundation models: A systematic benchmark across architectures, tasks, and training regimes, 2026. URL https://arxiv.org/abs/2604.23091.

Aditya Kommineni, Emily Zhou, Kleanthis Avramidis, Tiantian Feng, and Shrikanth Narayanan.

A Multi-dimensional Framework for Evaluating Generalization in EEG Foundation Models. In Proceedings of the 7th Conference on Health, Inference, and Learning, pages 221–244. PMLR, June 2026.

Simon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. Similarity of neural

network representations revisited. In International Conference on Machine Learning, 2019.

Demetres Kostas, Stéphane Aroca-Ouellette, and Frank Rudzicz. BENDR: Using Transformers

and a Contrastive Self-Supervised Learning Task to Learn From Massive Amounts of EEG Data. Frontiers in Human Neuroscience, 15:653659, June 2021. ISSN 1662-5161. doi: 10.3389/fnhum.2021.653659. URL https://www.frontiersin.org/articles/10.3389/ fnhum.2021.653659/full.

Min-Ho Lee, O-Yeon Kwon, Yong-Jeong Kim, Hong-Kyung Kim, Young-Eun Lee, John

Williamson, Siamac Fazli, and Seong-Whan Lee. EEG dataset and OpenBMI toolbox for three BCI paradigms: An investigation into BCI illiteracy. GigaScience, 8(5):giz002, 2019. doi: 10.1093/gigascience/giz002.

Yizhi Li, Yinghao Ma, Ge Zhang, Ruibin Yuan, Kang Zhu, Hangyu Guo, Yiming Liang, Jiaheng

Liu, Zekun Wang, Jian Yang, Siwei Wu, Xingwei Qu, Jinjie Shi, Xinyue Zhang, Zhenzhu Yang, Yidan Wen, Yanghai Wang, Shihao Li, Zhaoxiang Zhang, Zachary Liu, Emmanouil Benetos, Wen-

hao Huang, and Chenghua Lin. OmniBench: Towards The Future of Universal Omni-Language Models, December 2025. URL https://arxiv.org/abs/2409.15272.

Dingkun Liu, Yuheng Chen, Zhu Chen, Zhenyao Cui, Yaozhi Wen, Jiayu An, Jingwei Luo, and

Dongrui Wu. EEG-FM-Compass: Progress, Benchmarking, and Future Directions for EEG Foun- dation Models, August 2026. URL https://arxiv.org/abs/2601.17883.

Jingying Ma, Feng Wu, Qika Lin, Yucheng Xing, Chenyu Liu, Ziyu Jia, and Mengling Feng. Code-

Brain: Bridging Decoupled Tokenizer and Multi-Scale Architecture for EEG Foundation Model, May 2025. URL https://arxiv.org/abs/2506.09110.

7

<!-- page 8 -->

Jun Ma and Tuukka Ruotsalo. Adapting frozen foundation models for montage-agnostic high- resolution EEG event segmentation. Journal of Neural Engineering, 23(3):036020, May 2026. ISSN 1741-2552. doi: 10.1088/1741-2552/ae6142.

Ben Mildenhall, Pratul P. Srinivasan, Matthew Tancik, Jonathan T. Barron, Ravi Ramamoorthi, and

Ren Ng. NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis, August 2020. URL https://arxiv.org/abs/2003.08934.

Yassine El Ouahidi, Jonathan Lys, Philipp Thölke, Nicolas Farrugia, Bastien Pasdeloup, Vincent

Gripon, Karim Jerbi, and Giulia Lioi. REVE: A Foundation Model for EEG - Adapting to Any Setup with Large-Scale Pretraining on 25,000 Subjects. In The Thirty-ninth Annual Conference on Neural Information Processing Systems, October 2025.

G. Pfurtscheller and C. Neuper. Motor imagery and direct brain-computer communication. Proceed-

ings of the IEEE, 89(7):1123–1134, July 2001. ISSN 1558-2256. doi: 10.1109/5.939829.

Enze Shi, Kui Zhao, Qilong Yuan, Jiaqi Wang, Huawen Hu, Sigang Yu, and Shu Zhang. FoME: A

Foundation Model for EEG using Adaptive Temporal-Lateral Attention Scaling, September 2024. URL https://arxiv.org/abs/2409.12454.

Seyed Yahya Shirazi, Alexandre Franco, Maurício Scopel Hoffmann, Nathalia B. Esper, Dung

Truong, Arnaud Delorme, Michael P. Milham, and Scott Makeig. HBN-EEG: The FAIR im- plementation of the Healthy Brain Network electroencephalography dataset. bioRxiv, 2024.

Urban Širca, Maryam Alimardani, Stefanos Zafeiriou, and Konstantinos Barmpas. Beyond accuracy:

Robustness, interpretability and expressiveness of EEG foundation models, May 2026. URL https://arxiv.org/abs/2605.17562.

Jamiyan Sukhbaatar, Satoshi Imamura, Ibuki Inoue, Shoya Murakami, Kazi Mahmudul Hassan,

Seungwoo Han, Ingon Chanpornpakdi, and Toshihisa Tanaka. SingLEM: Single-Channel Large EEG Model, September 2025. URL https://arxiv.org/abs/2509.17920.

Guangyu Wang, Wenchao Liu, Yuhong He, Cong Xu, Lin Ma, and Haifeng Li. EEGPT: Pretrained

Transformer for Universal and Reliable Representation of EEG Signals. In Advances in Neural Information Processing Systems, 2024a.

Jiquan Wang, Sha Zhao, Zhiling Luo, Yangxuan Zhou, Haiteng Jiang, Shijian Li, Tao Li, and Gang

Pan. CBraMod: A Criss-Cross Brain Foundation Model for EEG Decoding. In The Thirteenth International Conference on Learning Representations, October 2024b.

Jiquan Wang, Sha Zhao, Zhiling Luo, Yangxuan Zhou, Shijian Li, and Gang Pan. EEGMamba:

An EEG foundation model with Mamba. Neural Networks, 192:107816, December 2025. ISSN 08936080. doi: 10.1016/j.neunet.2025.107816. URL https://linkinghub.elsevier.com/ retrieve/pii/S0893608025006963.

Wei Xiong, Jiangtong Li, Jie Li, Kun Zhu, and Changjun Jiang. EEG-FM-Bench: A Comprehensive

Benchmark for the Systematic Evaluation and Diagnostic Analyses of EEG Foundation Models, June 2026. URL https://arxiv.org/abs/2508.17742.

Chaoqi Yang, M. Brandon Westover, and Jimeng Sun. BIOT: Cross-data Biosignal Learning in the

Wild, May 2023. URL https://arxiv.org/abs/2305.10351.

Zhizhang Yuan, Fanqi Shen, Meng Li, Yuguo Yu, Chenhao Tan, and Yang Yang. BrainWave: A Brain Signal Foundation Model for Clinical Applications, September 2024. URL https: //arxiv.org/abs/2402.10251.

Marzieh Zare. A negative-control protocol for clinical EEG foundation-model benchmarks: Dataset

identity and external-cohort stress testing, August 2026. URL https://arxiv.org/abs/2607. 24519.

Yuchen Zhou, Jiamin Wu, Zichen Ren, Zhouheng Yao, Weiheng Lu, Kunyu Peng, Qihao Zheng,

Chunfeng Song, Wanli Ouyang, and Chao Gou. CSBrain: A Cross-scale Spatiotemporal Brain Foundation Model for EEG Decoding, June 2025. URL https://arxiv.org/abs/2506. 23075.

8

<!-- page 9 -->

## A Related Work: EEG-FMs

We selected four EEG foundation models—SingLEM [Sukhbaatar et al., 2025], CBraMod [Wang et al., 2024b], LUNA [Döner et al., 2025], and REVE [Ouahidi et al., 2025]—to represent different approaches to channel processing and spatial encoding. These architectural differences are directly relevant to our investigation of representation stability under changes in electrode number and con- figuration. An overview of the selected models and their architectural categories is provided in Table S1. All four models use masked autoencoding/reconstruction-based pretraining, allowing us to focus on differences in their architectural treatment of channel information. In this study, we focus on differences in their architectural treatment of channel information.

Table S1: Overview of the evaluated EEG foundation models.

SingLEM CBraMod LUNA REVE

Category Channel- independent

Spatial-temporal channel interaction

Latent channel unification

Continuous coordinate-aware

Pretraining corpus

71 datasets 1 (TUEG) 2 (TUEG + Siena) 92 datasets

Cross-channel interaction

Shared weights across channels; no interaction

Separate spatial and temporal self-attention

Learned query cross-attention

Cross-channel self-attention

Spatial encoding

None Spatio-temporal convolution

3D electrode coordinates

4D Fourier encoding of electrode and temporal coordinates

Channel/layout handling

Channel dimension retained

Channel dimension retained

Fixed-size latent representation

Coordinate-aware channel-temporal representation

Pretraining channel configurations

17–256 19 20, 22 (TUEG) 29 (Siena) 3–129

Related models

– BENDR, BIOT, Neuro-GPT, LaBraM, EEGPT, NeuroLM, BrainWave, FoME, CSBrain, EEGMamba, CodeBrain, BrainRVQ 2

LuMamba [Broustail et al., 2026], REVE (global token)

NeurIPT [Fang et al., 2025], SAMBA [Hong et al., 2025], HEAR [Chen et al., 2025]

The four models evaluated in this work provide complementary approaches along two dimensions that are central to our study: cross-channel interaction and spatial encoding (see subsection B.1).

2BENDR: Kostas et al. [2021]; BIOT: Yang et al. [2023]; Neuro-GPT: Cui et al. [2024]; LaBraM: Jiang et al. [2024b]; EEGPT: Wang et al. [2024a]; NeuroLM: Jiang et al. [2024a]; BrainWave: Yuan et al. [2024]; FoME: Shi et al. [2024]; CSBrain: Zhou et al. [2025]; EEGMamba: Wang et al. [2025]; CodeBrain: Ma et al. [2025]; BrainRVQ: Cui et al. [2026];

9

<!-- page 10 -->

## B Evaluated models and embeddings

B.1 Evaluated models

In the following, we provide details about the four FMs used in this work, summarized in Table S2.

CBraMod. The backbone of CBraMod [Wang et al., 2024b] is a criss-cross-transformer, which implements two attention mechanisms, whose aim is to model spatial and temporal relationships among the EEG data separately and in parallel. Data are segmented into P patches, resulting in a tensor ∈RC×P ×Tp. The pretraining objective is a masked signal reconstruction. Furthermore, the model introduces asymmetric conditional positional encoding (ACPE) to model the electrode position. These rely on convolutional neural networks (CNNs) to learn the positional embeddings from the spatial-temporal position of an EEG patch, which should enable the model to adapt to electrode layouts dynamically. Note that for downstream tasks, the adaptation to other montages still depends on the montages the model has seen during pretraining. Also, although the EEG patches attend to each other in the time and space domains, the model does not generate an explicitly fused representation of the input signal, the output embedding E has the shape E ∈RC×P ×F .

LUNA. LUNA [Döner et al., 2025] utilizes masked signal reconstruction. Segmented EEG-patches learn a temporal and frequency embedding. Afterwards, a positional embedding encodes the 3D electrode coordinates via NeRF sinusoidal projections [Mildenhall et al., 2020]. At the heart of LUNA lays a channel unification module, which learns fixed-sized query tokens Q that cross-attend to patch features. As a result, during channel unification, the channel count C is lost, and 2D output embeddings of shape E ∈R(Q·P )×F are retained. These latent vectors are afterwards passed through multiple Transformer encoder blocks to learn temporal dependencies across patches before retrieving the final embedding.

SingLEM. SingLEM [Sukhbaatar et al., 2025] adopts an masked autoencoder MAE framework with signal reconstruction as the pretraining objective. In contrast to CBraMod and LUNA, the model does not implement any attention or learning of inter-channel dependencies. Instead, each chan- nel is passed through the model independently. The patched EEG signal of a channel is forwarded through a 1D CNN to obtain a temporal embedding. The subsequent feature embedding module aims to represent short-range temporal relationships in contextualized embeddings. It applies multi- head self-attention on local context sequences for each token. Long-range temporal dependencies are afterwards captured by multi-head self-attention on the stacked contextualized embeddings. The final output embeddings are of shape E ∈RC×P ×F . Crucially, SingLEM uses a late-fusion strat- egy for downstream applications, meaning the single-channel representations are concatenated for classification.

REVE. REVE [Ouahidi et al., 2025] uses a masked-autoencoder paradigm designed to explicitly generalize across varying electrode montages. It creates overlapping temporal EEG patches, projects them into linear patch embeddings, and then adds spatial information. A 4D positional encoding based on the 3D electrode coordinates and temporal patch indices captures spatial information with Fourier features. These 4D encodings provide an adaptive function, which dynamically processes different electrode layouts. All positionally aware tokens are then processed jointly by a standard transformer encoder, where self-attention performs cross-channel fusion over coordinates and se- quence length. The output embedding has a shape of E ∈RC×P ×F . Simultaneously, during pre- training, an attention pooling is applied over the outputs of all Multi-Head Attention layers, which yields a global learned query token. We refer to this readout as REVE-A. This token is used in REVE’s architecture for a secondary reconstruction, which primarily exists to yield a more gener- alizable representation. This global query token can serve as a readout of the FM for collapsing the 3D-embeddings of the encoder into a fixed-size 1D representation for downstream classification tasks.

B.2 Embedding retrieval

Let k index subjects and e index the samples collected per subject. A single preprocessed EEG sam- ple is denoted as Sk,e ∈RCfull×T , where Cfull is the number of channels and T is the number of time points in the trial. Each multi-channel signal is divided into P patches of length Tp, which yields Xk,e ∈RCfull×P ×Tp. We additionally subsample the channel dimension from Cfull to Csub chan- nels, yielding Yk,e ∈RCsub×P ×Tp. Next, both {Xk,e} and {Yk,e} are passed through a pretrained

10

<!-- page 11 -->

Table S2: Overview of channel-fusion mechanisms across evaluated EEG foundation models. All four models are pretrained with a masked-reconstruction objective; C, P, F, Q follow the notation introduced in subsection B.2.

Model Channel-Fusion Mechanism Positional / Spatial Encoding Output Shape

CBraMod Criss-cross transformer: separate spatial and temporal self-attention branches

Asymmetric Conditional Positional Encoding (ACPE)

C × P × F

LUNA Cross-attention: Q ≪C learned latent queries attend to channel-wise patch features, collapsing the channel axis

3D electrode coordinates via NeRF-style sinusoidal projection

(Q · P) × F

SingLEM None during encoding. Channels processed fully independently (shared weights); cross-channel combination deferred to late-fusion concatenation downstream

(channel-independent) C × P × F

REVE Full self-attention over the flattened (C × P) token sequence + one

summary token (cf. LUNA)

4D Fourier features + learned linear projection (3D coords + temporal patch index)

C × P × F

Standard 10-05

Fp1 Fp2

AF7 AF3 AF4 AF8

F9

F7 F3 Fz F4 F8

F10

FT9

FC5 FC3 FC1 FC2 FC4 FC6

FT10

T7 C5 C3 C1 Cz C2 C4 C6 T8

TP9

TP7 CP5 CP3 CP1 CPz CP2 CP4 CP6 TP8

TP10

P7

P3 P1 Pz P2 P4

P8

PO9

PO3 POz PO4

PO10 O1 Oz O2

FTT9h FTT10h

TTP7h TTP8h

TPP9h TPP10h

GSN-HydroCel-128

E1 E2 E3 E4

E5

E6

E7

E8 E9 E10

E11

E12

E13

E14

E15 E16

E17

E18

E19

E20

E21

E22

E23

E24

E25

E26

E27

E28

E29

E30

E31

E32

E33

E34

E35

E36

E37

E38

E39

E40

E41

E42

E43

E44

E45E46E47

E48

E49

E50E51

E52

E53

E54

E55

E56 E57

E58 E59

E60

E61

E62

E63 E64 E65

E66

E67

E68

E69

E70

E71

E72

E73

E74

E75

E76

E77

E78

E79

E80

E81

E82

E83

E84

E85

E86

E87

E88

E89

E90

E91

E92

E93

E94

E95

E96

E97

E98

E99

E100 E101

E102

E103

E104 E105 E106

E107

E108

E109

E110

E111 E112

E113

E114 E115

E116

E117 E118

E119 E120

E121 E122

E123 E124 E125

E126 E127

E128

frontal_left frontal_midline frontal_right temporal_left temporal_right centroparietal_left centroparietal_right posterior_left posterior_right posterior_midline

Figure S1: Regions of Interest (ROIs) mapping for 128-channel GSN-HydroCel and 62-channel Standard-1005 montages. These ROIs were used in experiments 1 and 2. Channels were assigned to ROIs manually based on their anatomical location.

foundation model f(·) with frozen weights to obtain embeddings

E(full))

k,e = f(Xk,e), E(sub)

k,e = f(Yk,e). (1)

The shape of these embeddings depends on whether the model fuses the channel and patch dimen- sion. CBraMod, SingLEM, and REVE preserve all dimensions, resulting in

E(full)

k,e ∈RCfull×P ×F , E(sub)

k,e ∈RCsub×P ×F , (2)

where F is the embedding dimension per patch.

LUNA and REVE-A fuse the channel dimension into Q query tokens per patch, giving

E(full)

k,e ∈RD×F , E(sub)

k,e ∈RD×F , (3)

where D = Q · P for LUNA and D = 1 for REVE-A.

Regions of Interest (ROI) Figure S1 shows how the Regions of Interest (ROIs) used for pooling are defined on the Standard-1005 montages used in the resting-state (RS) [Shirazi et al., 2024]

11

<!-- page 12 -->

and motor imagery (MI) [Lee et al., 2019] datasets. We decided to classify the ROIs based on neuroanatomical regions. For the Standard 10-05 montage, this could be achieved using the channel names, since these refer to such regions already. For the GSN montage, we categorized them based on our own qualitative assessment.

## C Datasets and preprocessing details

Resting-State (RS) Dataset. The Healthy Brain Network EEG Dataset contains high-resolution EEG Data from over 3000 participants aged 5–21 years [Shirazi et al., 2024]. The data are split across 11 releases. For our purposes, we utilize a random subsample with 100 participants. The signal has been downsampled to 100 Hz and bandpass-filtered between 0.5 and 50 Hz. The data have been recorded with a 129-channel GSN-HydroCel high-density layout. Each participant went through ten 30-s epochs in which they were instructed to either open or close their eyes. We selected the first 4 s of each 30-s trial for our downstream analyses. For quality control, we clipped amplitudes at 500 µV, and discarded epochs exceeding this threshold more than 5% of the time.

Motor Imagery (MI) dataset. The motor imagery dataset by Lee et al. [2019] was recorded with a 62-electrode standard-1005 montage at a sampling rate of 1000 Hz from 52 subjects. Each trial followed a cued motor imagery paradigm: a 3-s preparatory fixation period, followed by a 4-s imagery task in which subjects imagined grasping with the hand indicated by a left or right visual cue. The dataset comprises balanced left- and right-hand imagery trials. Trials from a training phase and an online test phase are available, although only the training-phase trials have labels and can be used for classification. Each subject underwent 100 trials in the train and test phases in two distinct recording sessions. Thus, for each of the 52 subjects, we obtained 200 labeled imagery trials.

Preprocessing. We applied minimal preprocessing steps, matching the pretraining configurations of the foundation models: average-referencing, resampling to 200 Hz for the CBraMod and REVE, 256 Hz for the LUNA, and 128 Hz for SingLEM followed by bandpass filtering in frequency bands 0.3–75.0, 0.1–75.0, 0.5–50, 0.5–99.5 for CBraMod, LUNA, SingLEM, and REVE, respectively. All bandpass filters were applied forward-backward to prevent phase shifts.

Montage Subsampling. For the experiments including linear probing, we subsample the 128- channel montage of the HBN resting-state dataset to both 64- and 32-channel montages, while the 62-channel recording montage of the MI dataset was subsampled to 32- and 16-channel layouts. For the MI dataset, the 32- and 16-channel montages are exact subsets of the 62-channel montage. In contrast, the reduced montages in the RS dataset differ slightly in electrode layout and do not have equivalent channel names. We therefore used nearest-neighbor electrode matching to arrive at layouts that closely resemble the native 64- and 32-channel GSN-HydroCel montages.

For the representational space similarity experiments, we utilized a sampling procedure to determine the number of channels used for the construction of an embedding. This enables us to conduct those experiments for smaller steps of subsampled channels Csub, where Csub progresses from 10 to 128 in steps of 10 and from 10 to 62 in steps of size 4, for the RS and MI datasets, respectively. Specifically, we sample EEG channels while preserving spatial structure using farthest point sampling based on geodesic distance on one hemisphere, and mirror the selection to the other hemisphere. The midline channels are separately selected proportionally to the total amount of channels that were sampled. See Figure S2 for examples of subsampled channel sets in the two datasets.

## D Training details

For both datasets, we apply a 2:1:1 train-validation-test split in Experiment 1.2, and repeat the training for three data splitting seeds, while the model stochasticity stays fixed. For cross-subject experiments the split is subject-level, and for the within-subjects experiments the split is on EEG epochs. Since both tasks are binary classification tasks, we implement the probes as logistic regres- sion, and optimize only the C parameter on the validation set for regularization over a grid of [0.001, 0.01, 0.1, 1.0, 10.0, 100.0]. For evaluation, we report AUROC.

## E Supplementary figures and tables

12

<!-- page 13 -->

10 channels 26 channels

42 channels 62 channels

62 channel 10-05 montage

10 channels 42 channels

74 channels 128 channels

128 channel GSN montage frontal_left midline frontal_right temporal_left temporal_right centroparietal_left centroparietal_right posterior_left posterior_right posterior_midline sampled

Figure S2: Sampled montages for the 128-channel and 62-channel montages.. These sampled channels were used in Experiment 2.

Table S3: AUROCs of within-montage baselines (N2N-probes with concat-all pooling) in Ex- periment 1 for RS and MI data. For the inter-subject RS task, the mean ± standard deviation of AUROC values across multiple seeds (n=10) is reported. For the intra-subject MI task, the values indicate the mean and standard deviation of AUROC values across subjects. Therefore, the high variance for MI task is associated with the high variance of subject-specific performances. This variation is in line with the CSP classification results reported in Lee et al. [2019].

Resting-State task Motor Imagery task

Model 32-ch 64-ch 128-ch 16-ch 32-ch 62-ch

CBraMod 0.91 ± 0.02 0.90 ± 0.01 0.91 ± 0.01 0.63 ± 0.12 0.67 ± 0.13 0.71 ± 0.14 LUNA 0.90 ± 0.02 0.89 ± 0.02 0.91 ± 0.02 0.60 ± 0.12 0.61 ± 0.12 0.62 ± 0.11 REVE 0.94 ± 0.01 0.92 ± 0.02 0.93 ± 0.01 0.69 ± 0.13 0.69 ± 0.13 0.69 ± 0.13 SingLEM 0.89 ± 0.03 0.88 ± 0.02 0.91 ± 0.02 0.62 ± 0.12 0.65 ± 0.12 0.67 ± 0.13

Table S4: AUROCs of within-montage baselines (N2N-probes) in Experiment 1 by pooling method for RS and MI datasets. Here, results for the full montages (128-channel for RS, and 62-channel for MI) are reported. For the inter-subject RS task, the mean ± standard deviation of AUROC values across multiple seeds (n=10) is noted. For the intra-subject MI task, the numbers indicate the mean and standard deviation of AUROC values across subjects. Therefore, the high vari- ance for MI task is associated with the high variance of subject-specific performances. Additionally to the pooling methods introduced above, we report results for ch-mean pooling, where the embed- dings are averaged over the channel dimension, and concatenate patches and features, yielding 1D embeddings of size (C · P · F). This method serves as baseline, since it removes most information across channels, while providing montage-agnostic embeddings.

Method concat-all ROI-concat-all ch-mean attention-pool

MI task – 62-channel

CBraMod 0.71 ± 0.14 0.70 ± 0.13 0.54 ± 0.08 - LUNA 0.62 ± 0.11 - - - REVE 0.69 ± 0.13 0.68 ± 0.13 0.56 ± 0.09 0.58 ± 0.09 SingLEM 0.67 ± 0.13 0.67 ± 0.13 0.51 ± 0.05 -

RS task – 128-channel

CBraMod 0.910 ± 0.014 0.885 ± 0.016 0.790 ± 0.040 - LUNA 0.911 ± 0.019 - - - REVE 0.928 ± 0.013 0.906 ± 0.014 0.888 ± 0.023 0.790 ± 0.031 SingLEM 0.912 ± 0.018 0.878 ± 0.023 0.608 ± 0.037 -

13

<!-- page 14 -->

10 22 34 46 58 62 Csub

0.25

0.50

0.75

1.00

Cosine Similarity

a

10 22 34 46 58 62 Csub

0.25

0.50

0.75

1.00

CKA

b

CBraMod SingLEM REVE A REVE ROI LUNA

Figure S3: Representational cross-montage robustness for motor imagery EEG. Each point compares the embedding of the full montage (Cfull) to that of a subsampled montage with Csub channels, displayed on the x-axis. For within-subject similarities, each point is an average over subjects; variance is displayed over the first three EEG trials per label (six trials per subject). (a) Within-subject cosine similarity. (b) Centered Kernel Alignment (CKA) between the subject-to- feature matrices of the two montages.

10 34 58 82 106 128 Csub

0.25

0.50

0.75

1.00

Cosine Similarity

a Resting-State

10 34 58 82 106 128 Csub

0.25

0.50

0.75

1.00

Wasserstein Distance

b Resting-State

10 22 34 46 58 62 Csub

0.25

0.50

0.75

1.00

Cosine Similarity

c Motor Imagery

10 22 34 46 58 62 Csub

0.25

0.50

0.75

1.00

Wasserstein Distance

d Motor Imagery

CBraMod LUNA SingLEM REVE

Figure S4: Average cosine similarity across ROIs and Wasserstein Distances. Each point com- pares the embedding of the full montage (Cfull) to that of a subsampled montage with Csub. Each point is an average over subjects, variance is displayed over the first three EEG trials per label (six trials per subject). (a, c) ROI-level within-subject cosine similarity: the ROI-pooled embeddings were first averaged over the patch dimension to produce ∈RR×F embeddings. Then we computed D

s(f (1)

r , f (2)

r )

E

r, where f (i)

r ∈RF is the feature vector of ROI r for montage i and s(.) is the cosine similarity. (b, d) Within-subject Wasserstein distances W2 computed per subject between the two (ROI · P) × F embedding matrices, treating each of the N = ROI · P rows as a sample in RF ,

except for LUNA, which has N = Q rows in RF .

14

<!-- page 15 -->

10 34 58 82 106 128 Csub

0.25

0.50

0.75

1.00

Cosine Similarity

a Resting-State

10 34 58 82 106 128 Csub

0.25

0.50

0.75

1.00

CKA

b Resting-State

10 22 34 46 58 62 Csub

0.25

0.50

0.75

1.00

Cosine Similarity

c Motor Imagery

10 22 34 46 58 62 Csub

0.25

0.50

0.75

1.00

CKA

d Motor Imagery

CBraMod SingLEM REVE A REVE ROI LUNA

Figure S5: Representational cross-montage robustness for resting-state and motor-imagery EEG with an alternative channel sampling seed. Each point compares the embedding of the full montage (Cfull) to that of a subsampled montage with Csub channels, displayed on the x-axis. For within-subject similarities, each point is an average over subjects; variance is displayed over the first three EEG trials per label (six trials per subject). (a, c) Within-subject cosine similarity. (b, d) Centered Kernel Alignment (CKA) between the subject-to-feature matrices of the two montages.

15

<!-- page 16 -->

10 34 58 82 106 128 Csub

0.25

0.50

0.75

1.00

Cosine Similarity

a Resting-State

10 34 58 82 106 128 Csub

0.25

0.50

0.75

1.00

Wasserstein Distance

b Resting-State

10 22 34 46 58 62 Csub

0.25

0.50

0.75

1.00

Cosine Similarity

c Motor Imagery

10 22 34 46 58 62 Csub

0.25

0.50

0.75

1.00

Wasserstein Distance

d Motor Imagery

CBraMod LUNA SingLEM REVE

Figure S6: Average cosine similarity across ROIs and Wasserstein Distances with an alternative channel sampling seed. Each point compares the embedding of the full montage (Cfull) to that of a subsampled montage with Csub. Each point is an average over subjects, variance is displayed over the first three EEG trials per label (six trials per subject). (a, c) ROI-level within-subject cosine similarity: the ROI-pooled embeddings were first averaged over the patch dimension to produce ∈RR×F embeddings. Then we computed

D

s(f (1)

r , f (2)

r )

E

r, where f (i)

r ∈RF is the feature vector

of ROI r for montage i and s(.) is the cosine similarity. (b, d) Within-subject Wasserstein distances W2 computed per subject between the two (R · P) × F embedding matrices, treating each of the N = R · P rows as a sample in RF , except for LUNA, which has N = Q rows in RF .

16

<!-- page 17 -->

CBraMod

REVE

SingLEM

0.5

1.0

AUROC

a

Resting-State

32-ch 64-ch 128-ch

32 64 128

32

64

128

train montage (ch)

b

CBraMod

32 64 128 eval montage (ch)

REVE ROI

32 64 128

SingLEM

0.7

1.0

AUROC

32 64 128

32

64

128

train montage (ch)

c

CBraMod

32 64 128 eval montage (ch)

REVE ROI

32 64 128

SingLEM

0.7

1.0

AUROC

Figure S7: Functional within- and cross-montage robustness for 20 ROIs. (a) Within-montage baselines (N = M) for inter-subject RS classification; bars show mean AUROC and standard devi- ation across seeds for RS (Table S3). (b) N2M-probes on RS, with matched train and test samples, and (c) with held-out test data. Rows give the training and columns the test montage. The full mon- tage has 128 channels for RS (Appendix C).

17