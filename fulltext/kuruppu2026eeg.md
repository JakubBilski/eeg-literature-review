<!-- source: pdf/kuruppu2026eeg.pdf | converter: pymupdf -->

<!-- page 1 -->

# EEG Foundation Models: A Critical Review of Current Progress and Future Directions

Gayal Kuruppu1,†,*, Neeraj Wagh2,†, Vaclav Kremen3, Sandipan Pati4, Gregory Worrell3, and Yogatheesan Varatharajah1,2

1Department of Computer Science & Engineering, University of Minnesota Twin Cities, MN, USA 2Department of Bioengineering, University of Illinois at Urbana-Champaign, Urbana, IL, USA 3Department of Neurology, Mayo Clinic, Rochester, MN, USA 4Department of Neurology, University of Minnesota Twin Cities, MN, USA †Equal contributions *Correspondence: kurup016@umn.edu

## ABSTRACT

Premise. Patterns of electrical brain activity recorded via electroencephalography (EEG) offer immense value for scientific and clinical investigations. The inability of supervised EEG encoders to learn robust EEG patterns and their over-reliance on expensive signal annotations have sparked a transition towards general-purpose self- supervised EEG encoders, i.e., EEG foundation models (EEG-FMs), for robust and scalable EEG feature extraction. However, the real-world readiness of early EEG-FMs and the rubrics for long-term research progress remain unclear. Objective. In this work, we conduct a review of ten early EEG-FMs to capture common trends and identify key directions for future development of EEG-FMs. Methods. We comparatively analyze each EEG-FM using three fundamental pillars of foundation modeling, namely the representation of input data, self-supervised modeling, and the evaluation strategy. Based on this analysis, we present a critical synthesis of EEG-FM methodology, empirical findings, and outstanding research gaps. Results. We find that most EEG-FMs adopt a sequence-based modeling scheme that relies on transformer-based backbones and the reconstruction of masked temporal EEG sequences for self-supervision. However, model evaluations remain heterogeneous and largely limited, making it challenging to assess their practical off-the-shelf utility. In addition to adopting standardized and realistic evaluations, future work should demonstrate more substantial scaling effects and make principled and trustworthy choices throughout the EEG representation learning pipeline. Significance. Our review indicates that the development of benchmarks, software tools, technical methodologies, and applications in collaboration with domain experts may advance the translational utility and real-world adoption of EEG-FMs.

## 1 Introduction

Electroencephalography (EEG) is a widely used neurophysiological modality for measuring the brain’s electrical activity with high temporal resolution [1]. Multi-channel EEG recordings encode complex neural dynamics across spatial, temporal, and spectral dimensions, necessitating interpretation by highly trained experts. Despite extensive efforts to develop quantitative EEG representations using handcrafted features, advanced signal processing, and contemporary machine learning approaches, expert visual review remains the gold standard for clinical EEG interpretation and decision-making. However, in the last decade, EEG research has seen significant advances in deep learning-based approaches for extracting application-specific features from raw EEG data (EEG-DL) [2, 3]. Although this line of research held significant potential to augment traditional visual EEG review, it met with limited success due to several reasons. Much of the EEG-DL research comprised end-to-end learning methods that relied on supervised learning and were trained on a very narrow group of EEG tasks, i.e., use-cases, and datasets that resulted from laborious expert-driven annotation efforts [4]. These efforts were clearly unscalable to cover the wide range of EEG tasks that might be needed in clinical or scientific EEG review. Furthermore, such supervised EEG encoders were highly susceptible to overfitting on erroneous and noisy training instances, raising concerns about robustness and transferability to other tasks and datasets. This lack of robustness was further exacerbated by the variability

1

# arXiv:2507.11783v3  [eess.SP]  24 Dec 2025

<!-- page 2 -->

of EEG recordings across recording sites, acquisition systems, subjects, and sessions, leading to a lack of trust in supervised EEG encoders [5, 6]. These limitations emphasized the need for EEG-DL solutions that rely less on expert EEG labels and yield robust, trustworthy, and explainable models with high translational value.

The emerging paradigm of foundation models (FMs) [7], based on label-free self-supervised learning (SSL) and efficient transfer learning, is a promising solution for these data-related challenges. Similar to the mainstream vision [8–10] and language [11–13] FMs, EEG foundation models (EEG-FMs) are trained to identify salient EEG features from raw unlabeled EEG recordings by using various SSL pretext tasks, such as masked reconstruction or masked prediction, via a process known as pretraining. EEG-FMs learn to represent EEG data as compressed embeddings in a latent space by leveraging the intrinsic properties found in the raw data. Pretrained EEG-FMs can then be adapted for various downstream applications using only very small amounts of labeled data, thereby alleviating the burden of expert EEG annotations – the main bottleneck in supervised EEG-DL research. As such, EEG-FMs hold promise as powerful, off-the-shelf feature extractors (or encoders) that can support scientific research, next-generation robust brain-computer interfaces, and augmented neurological decision support.

Several EEG-FMs have been proposed over the last few years [14–23], whose chronological order along with total annual Google Scholar search results for the term “EEG Foundation Model” is shown in Figure 1. Despite the growing interest, many questions remain unanswered regarding the design choices in EEG-FMs, the learned representations, performance across various real-world applications, and the guarantees of robustness and trustworthiness. For example, the choice of EEG input representations, architectural components, and SSL pretext tasks can vary significantly across models, and the effects of those choices on the learned features are unclear. The complexity, quality, and flexibility of the representations learned by EEG-FMs and their relation to brain physiology have not been sufficiently studied, raising questions about their explainability. Furthermore, the performance and generalizability of these EEG-FMs beyond the common public datasets and benchmarks have not been adequately evaluated. These questions and concerns call for a critical review of the early EEG-FMs, focusing on architectural choices, pretraining approaches, evaluations, and trustworthiness, to identify rubrics for meaningful long-term progress in EEG-FM research and to advance their translational value.

Figure 1. Electroencephalography foundation model (EEG-FM) publication trends. The total annual Google Scholar search results for the term “EEG Foundation Model” between 2021 and 2024 (September) are shown in blue. The specific EEG-FMs reviewed in this study (i.e., according to the search criteria described in section 3) are listed in red, in chronological order by their preprint publication dates.

To that end, this topical review surveys ten early EEG-FMs (between January 2021 and September 2024) and critically analyzes their building blocks, identifies key takeaways and research gaps, and suggests directions for future EEG-FM research. Recent studies have begun to survey EEG-FMs [24–26], but these reviews primarily

2/35

<!-- page 3 -->

emphasize technical components such as model architectures and self-supervised learning strategies. In contrast, critical factors related to data representation, evaluation scope, and rigor have received relatively little attention. Even more limited is the discussion of real-world translational requirements and the practical constraints under which EEG-FMs will ultimately need to operate. In this review, we offer a more holistic perspective on the development and assessment of EEG-FMs, adopting a data- and domain-centric viewpoint to evaluate their maturity for clinical translation and real-world use. We also highlight complementary research directions that can help position future EEG-FMs for meaningful practical impact. This review is organized as follows. Section 2 introduces the EEG recording procedures, the information content of EEGs, traditional quantitative EEG approaches based on feature engineering, the sources of data variability, and the different functional components of foundation models. Section 3 describes the search strategy we undertook to identify previously published EEG-FMs and provides brief summaries of those models. Section 4 provides a comprehensive analysis of each of the identified EEG-FMs along several dimensions, including training data, data preprocessing, input representations, model architectural components, and model evaluation strategies. Section 5 discusses the key takeaways and research gaps, and Section 6 lays out our view for future directions that would further advance the current state of the art.

## 2 Background

EEG is a common neurophysiological technique for recording electrical activity generated by the brain using one or more electrodes. EEG emerged in the early nineteenth century and has since expanded into many areas of science and medicine. It is widely used in clinical and research settings for diagnosing neurological disorders [27], studying brain function [28], and developing brain-computer interfaces [29]. EEG measures voltage potentials and their fluctuations resulting from ionic current flow mainly generated by firing populations of neurons [30]. Scalp EEG is typically captured using electrodes placed directly on the scalp. EEG can also be recorded invasively, with electrodes placed intracranially (within the brain) or subdurally (under the skin), commonly referred to as intracranial EEG (iEEG). While iEEG measures summated local field potentials generated by smaller neuronal populations, scalp EEG measures the electrical activity generated by large neuronal populations that pass through multiple layers of the brain and head (i.e., cerebrospinal fluid, meninges, skull, muscles, scalp). The conduction of neuronal activity through these layers causes significant attenuation and spatial mixing of the EEG signal [31], including artifacts caused by movements of electrodes and muscle activity. As a result, scalp EEG has considerably different spatio-temporal resolution, amplitude, frequency, and noise content compared to intracranial EEG [32].

2.1 Contents and Sources of Variability in EEG Data The EEG signal is a noisy, high-dimensional, spatio-temporal measurement of electrical brain activity. Several factors influence the contents of EEG recordings, including physiological, pathological, and artifactual elements. Physiological elements: Most of the physiological elements present in EEG can be described using the various oscillatory components known as the delta, theta, alpha, beta, and gamma bands, each with distinct oscillatory frequencies and physiological mechanisms [33]. The general attentional state of the subject during the recording (awake, drowsy, asleep) influences the spatio-temporal characteristics of EEG [34]. In addition, EEG also shows changes related to natural aging [35] and other benign changes in brain structure and function. Pathological elements: The primary diagnostic value of EEG is due to its ability to capture various pathological brain activity patterns. These electrographic patterns include seizures, interictal epileptiform discharges (e.g., spikes and sharp waves), triphasic waves, rhythmic discharges, lateralized periodic discharges, background slowing, and other diffuse or focal abnormal electroencephalogram patterns [27]. Artifactual and noise elements: EEG artifacts can be introduced by biological phenomena (e.g., eye blinks, head movement, muscle activity, cardiac signals), recording conditions (e.g., signal discontinuities, transient filter effects), or external sources (e.g., electromagnetic interference) [36]. Eye- and muscle-related activities are the primary sources of artifacts in EEGs, introducing slow, high-amplitude changes and fast, low-amplitude changes, respectively. In addition to these artifacts, consistent noise from the power line and its harmonics may also be present. Finally, certain medications, such as anti-depressants and anti-seizure medications, affect the EEG as well. For example, benzodiazepines and barbiturates are known to cause changes to the EEG [37].

3/35

<!-- page 4 -->

The various practices and configurations used in clinical studies introduce variabilities across EEG datasets. First, the hardware used to record EEGs can have preset configurations for sampling frequency, filtering, analog-to-digital quantization, amplification magnitude, and broadband noise levels [38]. Second, the EEG examination protocol may differ between clinical sites: the recording length could be different; recordings can have variable amounts of wake/sleep segments and eyes open/closed segments; and they may include cognitive tests and activation procedures such as sleep deprivation, photic stimulation, or hyperventilation. In addition, the EEG layout (i.e., the number of leads and their positions) and the reference leads may vary across sites. Finally, anatomical [39], genetic [40], and biochemical [41] differences introduce inter-individual variability. These factors make data ingestion and standardization non-trivial, especially in intracranial EEG datasets, where lead locations are subject-specific.

2.2 Feature Extraction from EEG Signals Characteristics of clinical EEGs are assessed visually by experts trained to detect pathological events and adverse deviations from healthy brain activity [42]. However, in non-clinical settings, the EEG is characterized by signal features derived computationally or analytically from the raw data. Quantitative EEG features serve as lower- dimensional proxies of the raw signal, quantifying pertinent brain activity and providing objective EEG assessments for various applications. Classical EEG features are derived from signal processing, statistics, and information theory domains. Examples include relative band-limited power, power ratios, independent components, sample entropy, and kurtosis, among others [43]. In select instances, these EEG features isolate and quantify meaningful characteristics of underlying brain physiology, such as neuronal oscillations and functional connectivity, and are therefore considered robust and interpretable. In supervised EEG-DL models, EEG features are learned directly from raw EEG data to increase performance for a particular task [44]. While EEG-DL models may push the boundaries of task performance, their black-box nature makes it non-trivial to relate them to brain physiology. Furthermore, EEG-DL features may overfit the noise in EEG signals, making them less likely to generalize out of the box. Hence, the robustness, reliability, and interpretability of EEG-DL feature extractors remain open research problems.

2.3 Pillars of Foundation Modeling In this section, we deconstruct the FM monolith into a set of universal, domain-agnostic building blocks or pillars. These pillars are minimally required to systematically compare diverse existing EEG-FMs and to build new ones. Representation of input data: EEG signals are acquired as a spatio-temporal data stream. Visual review of clinical EEGs is conducted primarily in this ‘native’ view. However, the computational interpretation and analysis of EEGs can benefit from alternative, perhaps more informative, representations of raw data. For example, representing EEGs as a temporal stream of short spatio-spectral data segments (10s each) could make it easier for EEG-FMs to learn latent frequency patterns and multi-scale information. Alternatively, representing EEGs using spatial covariance matrices can make it easier to extract latent connectivity patterns. Broadly, the choice of data representation at the input stage may greatly influence the quality and semantics of learned latent representations [45]. In biosignal domains where data are sampled from underlying physiological processes, constructing informative input data views may itself require significant offline transformations or even domain-specific modeling, such as inverse modeling [46]. Without these offline efforts, data-driven learning of latent representations via FMs may be infeasible. Architectural and functional design of FMs: At an architectural level, FMs are typically built from several non-linear transformer blocks that can be readily stacked to scale the model depth and size. Transformer blocks themselves contain multiple feed-forward layers followed by a multi-head attention module [47]. Vision FMs may use convolutional blocks to exploit the desirable spatial inductive bias of convolutional operations [48]. Regardless of model size or low-level architectural choices, encoder-only FMs are understood to have only two high-level functional components: a backbone network and a final single fully connected layer. The backbone network serves as a feature extractor, providing low-dimensional embeddings (or representations) of the input data. The final layer, referred to as a task head, then uses these embeddings for task-specific purposes such as classification or regression. Self-supervised learning (SSL): In the SSL paradigm, supervision for training is derived strategically from unlabeled input data (pseudo-labels) rather than from human-curated labels, as in supervised learning [49]. SSL objectives (pretext tasks) are commonly either contrastive or generative. Contrastive pretext tasks use meaningfully

4/35

<!-- page 5 -->

augmented or noisy views of the input to learn robust data representations using encoder-only backbones [50]. Generative pretext tasks mask portions of the input and reconstruct/generate the masked portions using encoder and decoder-based backbones [51]. In either case, SSL learns general intrinsic relationships within the data, thereby creating a task-agnostic backbone network that serves as a general feature extractor. The structure of representations learned by SSL tasks and general principles for effective SSL task design are under active study. Regardless, the value of SSL is particularly high in the EEG domain as it improves model generalizability [52] and partially alleviates the need for expert EEG annotations that are expensive to obtain, subjective, and error-prone [6]. Transfer learning and model adaptation: The backbone network enables the reuse, transfer, and adaptation of EEG features (i.e., data-driven EEG knowledge) across semantically overlapping tasks [53]. The proportion of the backbone adapted for a specific application is flexible. For example, the backbone may be entirely fixed/frozen (linear probing), partially updated, or entirely updated (fine-tuning) [54]. This adaptation process may use slower or layer-specific learning rates to preserve pretrained knowledge within the backbone. In either case, any pretext task-specific layers at the top are discarded and replaced with a new trainable linear head that performs classification or regression for the ‘downstream’ application. Using application-specific data splits and human-curated task-specific labels, the model is then trained further until convergence. The development of algorithms for robust and efficient adaptation is an active area of research. Broadly, transfer learning and model adaptation techniques obviate the need to train new EEG-DL models from scratch by leveraging knowledge from pre-existing models. Data and model scale: The scaling up of pretraining data volume, data diversity (i.e., the number of distinct data sources), and model size has contributed towards improved pretrained latent features, increased downstream task performance, sample efficiency, and model generalizability, among other properties [55–60]. Empirical scaling laws have established power-law relationships between FM error rates and three key modeling levers, namely the pretraining data size, model size, and compute [57, 61], which suggest that an exponential increase in data and model size can indeed improve FM performance, albeit with diminishing returns. Overall, the balance between data and model size to maximize performance under a fixed compute budget remains a critical consideration in FM research. It is noteworthy that vision and language FMs are often multi-billion-parameter models pretrained on an internet-scale collection of diverse datasets [62–64]. However, the relative scarcity of large-scale EEG corpora may limit scaling efforts in EEG-FM research.

## 3 Review Approach & Summary of EEG-FMs

This section describes our search strategy and summarizes the EEG-FMs to date, highlighting the data used to train those models, model scale, architectural details, and evaluations.

3.1 Search Strategy We conducted a comprehensive search across various web platforms, including Google Scholar, arXiv, DBLP, IEEE Xplore, PubMed, bioRxiv, and medRxiv, to identify relevant research in journals, conferences, workshops, and preprints. We limited our search query, (“EEG” AND “Foundation Model”), to identify FMs that were developed primarily for scalp or intracranial EEG modalities. Our search starts from the year 2021 – the year the term Foundation Model was introduced [7] – and includes studies that were published or archived until September 30th,

2024. We then removed duplicate instances and manually reviewed the title, abstract, and introduction sections to confirm relevant EEG-FMs by identifying phrases to the effect of "We developed an EEG foundation model. . . " and "The proposed approach forms the basis for an EEG foundation model. . . ". It is important to note that we excluded studies that, a) propose individual components that are building blocks of foundation models (e.g., pretraining strategies, spatio-temporal feature encoders), but not functional off-the-shelf foundation models, and b) finetune existing EEG-FMs to derive task-specific models. Furthermore, our review does not include multi-modal foundation models and sleep foundation models developed using polysomnography (PSG) data [65, 66]. Nonetheless, we briefly discuss two sleep foundation models published during the same time frame in the supplement for interested readers. Using those search criteria, we identified nine EEG-FMs, Neuro-GPT [15], Brant [16], BIOT [17], EEGFormer [18], LaBraM [19], Mentality [20], NeuroLM [21], FoME [22], and BrainWave [23]. In addition, we also included BrainBERT because of its common presence as a baseline in other EEG-FM evaluations [16, 18, 22, 23].

5/35

<!-- page 6 -->

3.2 EEG-FM Summaries Table 1 summarizes all ten EEG-FMs. Although all the EEG-FMs share many commonalities, each FM is unique in its own right. In order to highlight the building blocks of each FM and their unique strengths, below we summarize each FM considering several factors, such as the amount of training data (in channel-hours, calculated as the total recording duration multiplied by the number of EEG channels; see Supplement Table 1 for details), model size (in terms of the number of trainable parameters), the types of EEG data (scalp EEG and/or iEEG), the way inputs are configured (raw time series, power spectra, or time-frequency representation), architectural components (convolutional and/or transformer blocks), the SSL tasks used for pretraining (masked reconstruction, auto-regressive modeling, and/or contrastive learning), and the evaluations performed.

Table 1. Brief model summaries. We provide brief summaries of the EEG foundation models (EEG-FMs) based on training data size, model size, input configurations, input data type, architectural components, and the self-supervised learning (SSL) tasks used for pretraining. Hyperlinks point to code and model weights, if available. N/A represents cases where channel-hours or model size could not be determined.

Model

Training Data (channel- hours)

Number of Param- eters

Input Configuration Data Type Architectural Components SSL Tasks

BrainBERT [link] 4.5k 43.18M Single-channel spectrogram data

Intracranial EEG

Transformer encoder and shallow decoder with two linear layers

Masked reconstruction

Neuro-GPT [link] 541k 79.53M Fixed multi-channel time series data

Scalp EEG

Encoder with both convolution and transformer layers and GPT-2 as the decoder

Masked reconstruction (causally masked latent embeddings)

Brant [link] 281k

68M, 104M, 249M and 506M

Variable multi-channel time series data

Intracranial EEG

Two transformer encoders for time and space and a linear decoder

Masked reconstruction

BIOT [link] 312k 3.3M Variable multi-channel spectral data

Scalp EEG Linear transformer, encoder-only architecture Contrastive learning

EEGFormer 541k N/A Multi-channel spectral data Scalp EEG

A transformer encoder and a shallow transformer decoder

Codebook-based reconstruction

LaBraM [link] 80k 5.8M, 46M and 369M

Fixed multi-channel time series data

Scalp EEG

Convolutional temporal encoder and transformer encoder layers and a linear decoder. A separate decoder for tokenization.

Masked reconstruction (token-level)

Mentality N/A N/A

Fixed multi-channel time series data

Scalp EEG

Convolutional layers and Mamba blocks in both encoder and decoder

Masked reconstruction

NeuroLM [link] 546k 250M, 500M and 1.7B

Variable multi-channel time series data

Scalp EEG

Vector quantization for tokenization with convolutional temporal encoder and transformer spatial encoder

Autoregressive reconstruction (token-level)

FoME N/A 476M and 745M

Variable multi-channel time series data

Scalp EEG and intracranial EEG

Temporal and Spatial transformer encoder and a linear decoder

Masked signal reconstruction

BrainWave 878k N/A

Variable multi-channel spectrogram data

Scalp EEG and intracranial EEG

Transformer encoder with channel attention and a lightweight decoder

Masked reconstruction (whole spectrogram)

BrainBERT [14]: As the first released EEG-FM, BrainBERT is relatively smaller than others, with 43.18M parame- ters, and was pretrained using a modest dataset of 4.5k channel-hours of iEEG data. The inputs were represented as channel-wise spectrograms, and a Bidirectional Encoder Representations from Transformers (BERT, [67])-type model was pretrained to predict masked patches for different types of spectrograms based on the Short-Time Fourier

6/35

<!-- page 7 -->

Transform (STFT, [68]) and Superlets [69]. The model comprised a transformer encoder and a shallow decoder with two linear layers. Evaluations focused on evoked brain responses while watching movies [70] and demonstrated generalizability to unseen subjects and electrode locations; however, the test data were drawn from the same distribution as the training data. The evaluations also showed that linear-probed BrainBERT performance matched that of randomly initialized supervised deep neural networks (DNNs) across most evaluation tasks. Additional evaluations showed that fine-tuned BrainBERT performance could match that of a randomly initialized DNN with as little as 15% of the training data for one task. A task-agnostic intrinsic dimensionality [71] (ID)-based analysis showed that the BrainBERT embeddings of different brain regions had distinct IDs, whereas the distribution across electrodes was relatively constant under randomly initialized weights. Neuro-GPT [15]: This mid-size EEG-FM with 79.53M parameters was pretrained entirely using scalp EEG data from the full Temple University Hospital (TUH) EEG Corpus [72], which included 541k channel-hours of clinical scalp EEG data. The model takes raw time series of the 22 EEG channels in the standard 10-20 layout as input and learns EEG representations using a combination of convolutional and transformer layers. Those representations are then used as input to a Generative Pretrained Transformer (GPT-2, [73]) decoder, which autoregressively predicts the masked latents. It is noteworthy that the decoder has more parameters than the encoder in this setup, which is not common in other EEG-FMs. This model was evaluated on EEG data from a 4-class Brain-Computer Interface (BCI) motor imagery task with a different channel configuration than the pretraining data. However, the downstream data were transformed to the original pretraining configuration using an inverse-forward approach [74]. The results showed that fine-tuning or linear probing the pretrained model performed better than models trained from scratch, including some fully-supervised EEG-DL approaches. Brant [16]: Brant is a relatively larger FM with 500M parameters and was pretrained using 281k channel-hours of iEEG data. However, its pretraining data were limited to a single dataset comprising 9 subjects. This model accepts raw EEG time series with different channel configurations as input. The model consisted of a temporal encoder that learns long-term temporal dependencies, a spatial encoder that learns spatial correlations, and a simple linear decoder. The spatial encoder used in this model to capture spatial relationships is a novel contribution compared to previous EEG-FMs. This model includes three scaled-down versions with 68M, 104M, and 249M parameters, respectively, all pretrained on the same data. These models were evaluated on short-term and long-term signal forecasting, frequency-phase forecasting, imputation, seizure detection, and pathology detection tasks. The results showed that Brant performs better than baselines in limited-label settings. BIOT [17]: This is the smallest of the ten reviewed EEG-FMs, with only 3.3M parameters, and was pretrained using a contrastive learning objective. The BIOT model introduced a novel approach to handling input data with variable lengths and variable numbers of channels: it tokenizes each channel into fixed-length segments representing frequency vectors, organizes them into ‘sentences’, and uses channel and position embeddings to preserve spatio- temporal information. BIOT used linear transformers to reduce training time and was evaluated across multiple clinical tasks, including seizure detection and seizure type classification. BIOT showed superior performance even without pretraining and even better performance with pretraining, compared to previous supervised EEG-DL models. EEGFormer [18]: This model was also pretrained on the full TUH corpus, which includes approximately 541k channel-hours of clinical scalp EEG data. It included a transformer-based encoder and shallow decoder, and was pretrained with a masked reconstruction objective. Latent features of input EEG patches generated by the encoder are used to train a vector quantizer to match neural codes generated by a neural codebook. The decoder then reconstructs the original EEG patches using these neural codes. Evaluations included several downstream tasks derived from the TUH corpus and an out-of-distribution (OOD) evaluation for neonatal seizure detection. Additional experiments included an interpretability analysis using the learned codebook. LaBraM [19]: This model used a relatively smaller dataset collected from multiple sources for pretraining, comprising 80k channel-hours of scalp EEG data. It was developed at three parameter scales: 5.8M, 46M, and 369M, respectively. The LaBraM pretrained model consisted of two parts, the neural tokenizer and the neural transformer. The neural tokenizer is first trained to learn a codebook that accurately predicts the amplitude and phase of the raw time series data. Then, with the codebook frozen, the neural transformer is pretrained to predict the codebook-based codes for the masked input patches. Note that this differs from typical pretraining procedures,

7/35

<!-- page 8 -->

where the goal is to reconstruct masked patches in the time-domain itself. This transformer model consists of a convolutional temporal encoder and a set of transformer blocks, with temporal and spatial positional encodings used to learn relative relationships between input patches. Although the evaluations demonstrated performance gains in various subsets of the TUH corpus, it is unclear whether these results generalize to out-of-distribution data. Mentality [20]: This model aims to capture the complex spatio-temporal dynamics of EEG signals using a Mamba [75]-based state-space model. The architecture of Mentality drew inspiration from other models such as SaShiMi [76], U-Net [77], and EEGNet [78] with the inclusion of Mamba blocks. However, the model was trained and evaluated exclusively on a subset of the TUH corpus. NeuroLM [21]: This model was inspired by a previous EEG-FM, LaBraM. However, NeuroLM was trained on 7x more data and is one of the largest EEG-FMs, with 1.7B parameters. Smaller model variants include 250M- and 500M-parameter versions. The neural tokenizer is first trained to learn a codebook that is both aligned with a text embedding space and can accurately reconstruct the input time series data in both time and frequency domains. These codes are then fed into a large language model for multi-channel autoregressive pretraining. Finally, this pretrained model is adapted via joint multi-task instruction tuning, enabling a single model to perform diverse EEG tasks without task-specific fine-tuning. However, despite the novel EEG-text alignment and joint adaptation, NeuroLM performed worse on downstream tasks than LaBraM and other state-of-the-art models. FoME [22]: This model included two versions with 476M and 745M parameters, respectively. The size of the training data was not provided in the manuscript. The model takes masked time series patches and their power spectral densities as input, which are then transformed by a temporal encoder. The outputs of the temporal encoder are then reorganized by channel and fed to a spatial encoder to reconstruct masked time patches. FoME was evaluated across multiple downstream tasks, including classification, forecasting, and imputation; however, the evaluations were conducted on in-distribution data, limiting broader conclusions. BrainWave [23]: This model was pretrained using a large dataset of size 878k channel-hours, including both scalp EEG and iEEG. It includes a transformer encoder and a channel attention module that transform EEG spectrograms into latent representations, which are then decoded by a lightweight decoder. This encoder-decoder architecture was trained using a masked-reconstruction objective. BrainWave is one of the few EEG-FMs trained and evaluated on both scalp EEG and iEEG signals, demonstrating the benefits of joint pretraining over unimodal approaches. The model has been extensively evaluated under different settings, such as cross-subject, cross-hospital, cross-subtype and few-shot classification, showcasing the generalizability and robustness across various clinical tasks.

## 4 Comparative Analysis of EEG-FMs

This section surveys the ten EEG-FMs and compares their design and construction along three major axes covering the pillars of foundation modeling described in section 2: a) preparation and representation of input data, b) model architecture and self-supervised pretraining, and c) model evaluations. The various considerations along these axes are illustrated in Figure 2.

4.1 Preparation and Representation of Input Data Datasets: Pretraining data functions as the knowledge base of an FM, making it a highly crucial component. Key factors, such as diversity, data volume, relevance, and, most importantly, data quality, can influence the generalizability of the patterns learned by an EEG-FM. Table 2 shows the datasets that were used in the pretraining and evaluation phases of the ten EEG-FMs reviewed in this article.

Most EEG-FMs (e.g., LaBraM, EEGFormer, Neuro-GPT, Mentality, BIOT, and NeuroLM) were trained only on scalp EEG data, although some (e.g., Brant and BrainBERT) were trained exclusively on iEEG data. Two EEG-FMs, FoME and BrainWave, were trained on both scalp and intracranial EEG data. A large portion of the pretraining data in the models used scalp EEGs from the Temple University Hospital (TUH) EEG corpus [4], which comprises 541k channel-hours of scalp EEG data. This corpus also included smaller derived subsets containing expert annotations for EEG abnormalities (TUAB), seizures (TUSZ), and events (TUEV). Other scalp EEG datasets used for pretraining include CHB-MIT [79] and small research datasets. Some FMs utilized EEG data available within PSG datasets such as SHHS [80], Sleep-EDF [81], and CAP Sleep [82]. Additionally, public or private iEEG data accounted for a large

8/35

<!-- page 9 -->

Figure 2. Comparative analysis of EEG foundation models (EEG-FMs). Our review analyzes EEG-FMs along three major dimensions; input data configuration, modeling, and evaluation (top figure). A summary of the various approaches undertaken by the EEG-FMs to address those components is shown in the bottom figure. EEG data is represented in one of three forms: raw time series, magnitude power spectrum, and time-frequency representation. Model architecture may include convolutional blocks to learn low-level patterns and/or transformer blocks to learn higher-level relationships. Models are pretrained primarily using self-supervised learning (SSL) approaches; the common SSL approaches used are masked reconstruction, auto-regressive modeling, and contrastive learning. The pretrained models are then evaluated on various downstream tasks, including clinical and non-clinical tasks.

portion of the training data in some models, such as Brant and BrainWave. The common publicly available iEEG datasets used for pretraining were MAYO [83], FNUSA [83], Brain TreeBank [70], and CCEP [84]. Training data volume ranged from 4.5k channel-hours in BrainBERT to 878k channel-hours in BrainWave. BrainWave utilized the most diverse pretraining dataset, including clinical scalp EEG datasets, sleep EEG datasets, various smaller-scale scalp EEG repositories, and several iEEG datasets. LaBraM and NeuroLM also used moderately diverse pretraining datasets, but were limited to the scalp EEG modality. Preprocessing and normalization: The content of EEG data is highly sensitive to the preprocessing and nor- malization steps performed before model training or evaluation. The choices made for resampling, bandpass and notch filtering, artifact removal, and temporal data segmentation into patches or epochs can directly impact the representations learned by an EEG-FM. Although some models did not comprehensively describe the preprocessing steps, most applied standard procedures such as bandpass filtering (0.5Hz to a higher cutoff frequency), powerline interference removal via notch filters (50 Hz or 60 Hz, including harmonics), and downsampling to 200 Hz or 250 Hz to standardize sampling rates across datasets. EEG signals are then segmented into smaller epochs, typically 1-10 seconds long. However, none of the EEG-FMs performed explicit artifact removal or outlier exclusion, except in cases of expertly labeled bad data or missing channels. Other, less common steps included DC offset removal and linear trend removal by FoME and Neuro-GPT. Data normalization practices after preprocessing were not described in several manuscripts. Neuro-GPT applied the commonly used z-transform along the time dimension to normalize EEG signals, whereas NeuroLM, BIOT, and LaBraM used a constant scaling factor based on the input range. Input representation: EEG is naturally a spatio-temporal data modality recorded using multiple channels. In addition to spatial and temporal information, spectral information is useful for interpreting EEG data, which is most often used as expert-derived features in statistical machine learning (ML) models. Furthermore, time-frequency

9/35

<!-- page 10 -->

representations, such as spectrograms and wavelet [85] transforms, are also used to preserve information in all three domains. All EEG-FMs used one or a combination of these representations as input.

The most widely used input representation is the multivariate time-series format, adopted by six of the ten EEG- FMs. With the adoption of a transformer architecture, the windows segmented from the original recording require further segmentation into smaller patches, also known as tokens. These patches or tokens can then be augmented with temporal and spatial information via positional encodings, allowing the models to be trained on EEG data with different channel configurations. This approach was adopted by models such as Brant, NeuroLM, and FoME to pretrain on datasets with varying channel counts. Two models, BIOT and EEGFormer, used power-spectral data as input instead of the original time-series patches, while two other models, Brant and FoME, added power-spectral data to complement the raw time-series inputs. Some EEG-FMs, such as LaBraM, Neuro-GPT, and Mentality, standardized different EEG datasets with different channel configurations to a fixed set of input channels. Two other models, BrainBERT and BrainWave, utilized channel-wise time-frequency representations of 1-5 seconds of EEG data as input. BrainBERT evaluations utilized spectrograms generated using classical methods like STFT, as well as scalograms [85] generated using modern methods such as Superlets.

4.2 Modeling and Pretraining Patching and context length: The temporal resolution of tokens or patches, i.e., how much EEG data each patch contains, varies between models, reflecting different design choices in model architecture and target tasks. Brant and FoME used patches corresponding to six seconds of EEG, while BrainBERT used 5-second STFT/Superlet windows. Models such as LaBraM, NeuroLM, BIOT, and BrainWave adopted a finer resolution, using 1-second segments per patch, whereas Neuro-GPT utilized a patch size of two seconds. Similarly, context length also varied among EEG-FMs. FoME was trained on 90-second segments, each represented by a sequence of 15 tokens. LaBraM could take up to 256 tokens as input, with the number of temporal tokens depending on the number of channels used. Neuro-GPT utilized a 32-token context window with overlapping segments, covering ∼57.8 seconds of EEG. BIOT utilized 19 tokens per channel and EEGFormer utilized 12 seconds of EEG context as input. Architectural components: The model architecture and training objectives play a central role in determining the effectiveness of a foundation model in extracting information from the input data [7]. EEG-FMs utilized various components at different stages of the pipeline, including tokenizers, local representation learning modules, spatial and/or temporal attention modules to learn dependencies, and task heads. Almost all the EEG-FMs we review in this article are transformer-based, except Mentality, which uses a combination of convolutional layers and a mamba-based architecture. In the transformer-based models, the input signal is divided into a fixed number of small patches/tokens to construct the input sequence. Some models that used raw time-series inputs leveraged convolutional layers to learn morphological features (e.g., Neuro-GPT, LaBraM, Mentality, NeuroLM). Neural tokenizers: Some models, such as LaBraM, NeuroLM, and EEGFormer, integrated separate tokenizers to transform the input signals into discrete tokens or codes. These EEG-FMs adapted a VQ-VAE [125]-like architecture to train a neural tokenizer, which mapped input patches into a fixed set of discrete embeddings called the codebook. During tokenizer training, latent features are mapped to nearest-neighbor embeddings from the codebook to reconstruct known features of the input, such as power and phase in LaBraM, and temporal and spectral features in NeuroLM. The models used neural codebooks to reconstruct raw time-series inputs using a transformer-like architecture. While NeuroLM and EEGFormer used codebook embeddings to map encoder outputs to discrete codes prior to decoding, LaBraM used codebook embeddings of masked input patches as targets during model pretraining. Spatial encoding: EEG-FMs implemented different spatial encoding strategies, although they differ in how explicitly they handle spatial information. Brant and FoME, for example, used transformer encoders with spatial attention but without dedicated spatial positional encodings. In contrast, LaBraM, BIOT, and NeuroLM injected spatial information through explicit spatial encodings to enhance positional encoding and capture the topographic layout of EEG channels. Among them, only BIOT supported multiple electrode configurations, while LaBraM and NeuroLM are limited to a fixed 10–20 layout for spatial encoding. Models such as Neuro-GPT and Mentality learned spatial dependencies implicitly using convolutional layers, without dedicated spatial embeddings. BrainWave incorporated spatial attention mechanisms to model inter-channel dependencies directly. In contrast, BrainBERT and EEGFormer

10/35

<!-- page 11 -->

Table 2. Datasets used for pretraining and evaluation. Here we list the diverse set of datasets and tasks that were used to pretrain and evaluate EEG foundation models (EEG-FMs). We highlight datasets that are not publicly available in bold, clinical and non-clinical datasets in pink and blue backgrounds, respectively, and use superscripts ∗and # to denote in-distribution and out-of-distribution evaluations, respectively.

Dataset/EEG-FM BrainBERT Neuro-GPT Brant BIOT EEGFormer LaBraM Mentality NeuroLM FoME BrainWave

Scalp EEG

TUEG [72] train train train train train

TUAB (Abnormal/normal classification - binary) eval# eval∗ eval∗ eval∗

TUAR (EEG artifact classification - multiclass) eval∗ train

TUEP (Epilepsy classification - binary) train

TUEV (EEG Events classification - multiclass) eval# eval∗ eval∗ eval∗

TUSL (EEG slowing classification - multiclass) eval∗ train eval∗

TUSZ (Seizure type classification - multiclass) eval∗ train train/eval∗

CHB-MIT [79] (Peadiatric seizure detection - binary) eval# train eval#

Sleep-EDFx [81] (Sleep stage classification - multiclass) train/eval∗ train

Siena Scalp EEG [86] (Seizure classification - binary) train train train

SHHS [87][80] (Sleep stage classification - multiclass) train

PREST (Abnormal event detection - binary) train

CAP Sleep [82] (Sleep stage classification - multiclass) train

HMC [88] (Sleep stage classification - multiclass) eval# train

SRM [89] (Resting state EEG data) train

Schizophrenia-81 (Schizophrenia classification - binary) train

Stroke-50 [90] (Hand movement classification - binary) train

PD-31 [91] (Parkinson disease classification - binary) train

IowaDataset [92] (Unknown task/s) train

UNMDataset [93] (Parkinson disease classification - binary) train

AD-184 [94] (Alzheimer’s disease classification - binary) train

Neonate dataset [95] (Seizure detection - binary) eval#

IIIC Seizure [96] (IIIC pattern classification) - multiclass eval#

Absence-16 (Seizure type classification - multiclass) eval#

Clonic-6 (Seizure type classification - multiclass) eval#

Atonic-5 (Seizure type classification - multiclass) eval#

DRE-Clinical (Seizure detection and localization - binary) eval#

SD-71 [97] (Sleep deprivation detection - binary) eval#

ADHD-Adult [98] (ADHD classification - binary) eval#

ADHD-Child [99] (ADHD classification - binary) eval#

Schizophrenia-28 [100] (Schizophrenia classification - binary) eval#

Depression-122 [101] (Depression classification - binary) eval#

MDD-64 [102] (Major depression detection - binary) eval#

AD-65 [103] (Alzheimer’s disease classification - binary) eval#

BCI Competition IV-1 [104] (Movement classification - binary) train train

Emobrain [105] (Emotion classification - multiclass) train train

Grasp/Lift Challenge [106] (Grasp classification/regression) train train

Inria BCI Challenge [107] (Next letter prediction - multiclass) train train

EEG Motor Imagery [108] (Classification - multiclass) train train train

Visual Categorization EEG [109] (Classification - multiclass) train train

Resting-state EEG [110] (Eye state classification - binary) train train

SEED Series [111–113] (Emotion classification - multiclass) train/eval∗ train/eval∗ train/eval∗

SPIS Resting State EEG [114] (CVS and HRT regression) train train

Brain-Invaders [115] (Target classification - binary) train train

Multiple data sources [116–120] (Unknown tasks) train train

MoBI [121] (Gait angle regression) eval#

BCI Competition IV Dataset 2a [122] eval#

Workload [123] (Workload classification - binary) eval#

Intracranial EEG

Brain TreeBank [70] (EEG classification - multiclass) train/eval∗

Private single dataset without source (Unknown) train/eval∗

Private dataset collection without source (Unknown) train

MAYO [124] (Pathology detection & events classification) eval# train/eval∗ eval#

FNUSA [124] (Pathology detection & events classification) eval# train/eval∗ eval#

CCEP [84] (Seizure onset zone localization - binary) train

11/35

<!-- page 12 -->

omit spatial modeling altogether, using only transformer layers without convolution or spatial priors. Self-supervision: SSL approaches are key components that enable the development of foundation models using massive unlabeled datasets [7]. Most EEG-FMs (seven out of ten) employed reconstruction of masked data as the primary SSL approach. EEGFormer model was pretrained by minimizing the reconstruction loss between input signals and signals decoded from codebook mappings of transformer-encoded input patches. NeuroLM employed an autoregressive approach to predict future patches from past patches, including an EEG-text alignment objective, and BIOT adopted a contrastive learning approach where the embeddings of masked inputs and the same inputs with different augmentations are minimized (i.e., the SimCLR [50] pretraining approach). Only one model — Neuro-GPT — employed masked data reconstruction in the latent space. Additionally, the LaBraM model employed a masked-signal reconstruction approach; however, the codebook embeddings of masked input patches from a previously trained neural tokenizer were used as reconstruction targets. Masking: The granularity of the learned representations in the EEG-FMs is influenced by the type and extent of masking used during self-supervised pretraining [126]. In models based on masked-signal reconstruction, masking is typically applied to random patches across temporal and spatial dimensions, as opposed to masking entire channels or full time segments. For example, Brant and FoME applied a ∼40% uniform random masking, zeroing out the masked input signal patches across time and channel dimensions. LaBraM similarly utilized a 50% patch-level masking, while BrainWave, despite operating in the spectrogram domain, performed masking entire spectrograms of several channels. On the other hand, BrainBERT applied a more fine-grained masking strategy, masking 5% from the time domain and 5% from the frequency domain, effectively masking ∼10% of the input spectrogram. Mentality applied random channel masking, targeting specific channels rather than patches. NeuroLM introduced a stair-step masking scheme, in which next token is auto-regressively predicted in a channel-conditioned manner, whereas Neuro-GPT utilized a causal masking approach in the latent space, consistent with autoregressive generation. Model scale: The number of trainable parameters (or weights) varied significantly between the ten EEG-FMs, ranging from 3.3M in BIOT to 1.7B in NeuroLM, although most models fall within the 200-500M parameter range. Some EEG-FMs, such as FoME, LaBraM, and NeuroLM, were developed at multiple scales with the same architecture, allowing users to choose a model scale according to their specific resource constraints.

4.3 Model Evaluations Downstream task evaluations: Performance on downstream tasks post-adaptation was the primary metric used for evaluation in all the EEG-FMs. However, the clinical and non-clinical downstream tasks used for evaluation and the adaptation techniques varied significantly between them. The various datasets used for evaluation are shown in Table 2. While most EEG-FM evaluations were restricted to either scalp or intracranial EEG, two models, namely FoME and BrainWave, were evaluated on both modalities. Furthermore, most FMs used common adaptation techniques, namely linear probing and fine-tuning, while some used prototype-based few-shot evaluation and instruction tuning.

Almost all EEG-FMs, except Mentality, investigated fine-tuning for downstream task evaluations, in which the pretext task decoder is discarded but the encoder is trained further using task-specific labels. On the other hand, five EEG-FMs (i.e., Brant, BrainBERT, LaBraM, EEGFormer, and Neuro-GPT) evaluated linear probing, where the encoder is typically frozen, and additional task-specific heads on top of the encoder are trained using labeled downstream data. The BrainWave model was evaluated using a prototype-based few-shot learning approach, where class prototypes were created by averaging the latent representations of a few examples per class, and downstream classification was performed by measuring similarity to those prototypes in the learned latent space. Furthermore, NeuroLM, which was pretrained with an EEG-text alignment objective, was evaluated using a text-prompting approach. The model was fine-tuned (instruction-tuned) using an auto-regressive prediction task utilizing EEG-text combined tokens, where the text tokens contained both class prompts and labels. Subsequently, the model was evaluated on various tasks by providing queries containing EEG tokens and prompts, for which the model predicted the class labels. In the following, we briefly summarize the evaluations performed by each EEG-FM and the results. BrainBERT: This model was trained and evaluated on the same intracranial EEG dataset, Brain TreeBank. The downstream task focused on predicting the features of the movies that the subjects were watching during the EEG recording. Fine-tuning the pretrained BrainBERT model on this task substantially outperformed fully-supervised

12/35

<!-- page 13 -->

linear and multi-layer neural network models. Linear probing also achieved Area Under the Receiver Operating Characteristic Curve (AUC) values similar to those of the fully supervised models. Neuro-GPT: This model was evaluated on a single scalp EEG dataset that was not used during pretraining, with the downstream task being 4-class motor-imagery classification. The fully-supervised baselines considered in this study include BENDR [127], SVM [128], EEGNet [78], CTCNN [129], CCNN [130], and NG-CRAM [131]. When used in a supervised setting without any pretraining, this model performed similarly to other supervised baselines. However, when the pretrained model was fine-tuned for the downstream task, it provided significant improvements in certain configurations. In contrast, linear probing performed worse than fully-supervised baselines. Brant: This model was evaluated on three unseen intracranial EEG datasets, including one private and two public datasets (MAYO and FNUSA). The downstream tasks evaluated include signal forecasting, imputation, seizure detection, and pathology detection. For all these tasks, the pretrained model was fine-tuned or linear-probed using task labels. The self-supervised pretrained baselines considered in this study included (RP, TS, CPC) [6], BENDR [127], MVTS [132], and BrainBERT that are designed for brain signals, and CoST [133], TF-C [134], PatchTST [135], TS-TCC [136] that are designed for general time series. Fully-supervised baselines without any pretraining included handcrafted features-based methods such as spectral power [137], rhythmicity spectrogram [138], and amplitude- integrated EEG [139] along with SEEG-Net [140]. In signal forecasting and imputation tasks, fine-tuned Brant consistently outperformed several time series baselines and its own linear probing version. In the seizure detection and pathology detection tasks, both the fine-tuned and linear probed versions of Brant outperformed other supervised and EEG-FM baselines, including BrainBERT. These observations held true in low-labeled settings as well. BIOT: This model was evaluated entirely on scalp EEG datasets on various clinical tasks. The supervised baselines considered in this study included SPaRCNet [141], ContraWR [142], CNN-Transformer [143], FFCL [144], ST- Transformer [145]. Evaluations showed that the finetuned BIOT encoder outperformed several fully-supervised baselines in CHB-MIT seizure detection and TUAB normal/abnormal classification. In two other tasks, namely IIIC seizure classification and TUEV event classification, both the vanilla untrained BIOT in the fully supervised setting and the pretrained BIOT model in the fine-tuning setting outperformed all supervised baselines. EEGFormer: The three variants of EEGFormer were evaluated against four fully-supervised models (i.e., EEG- Net [78], TCN [146], EEG-GNN [147], and GraphS4mer [148]) and BrainBERT as baselines, using five different scalp EEG datasets/tasks. Fine-tuned EEGFormer outperformed all baselines in all the tasks except one, where its performance was marginally lower than EEG-GNN. Their evaluations also showed that a smaller version of EEGFormer demonstrated less variability in some downstream evaluations. LaBraM: This model was evaluated on four scalp EEG datasets: two clinical (TUAB and TUEV) and two non- clinical (SEED-V and MoBI), with MoBI as the only external dataset. The evaluations considered several supervised models, SPaRCNet [141], ContraWR [142], CNN-Transformer [143], FFCL [144], ST-Transformer [145], and BIOT as baselines. All variations of LaBraM (base, large, and huge) with fine-tuning outperformed baselines in all tasks. Mentality: This model was evaluated on the TUSZ seizure detection dataset, which was also used for pretraining. The evaluation compared an untrained Mentality model trained in a fully supervised setting with a pretrained Mentality model linearly probed with two linear layers, showing that pretraining is beneficial for this task. NeuroLM: This model was fine-tuned jointly on six tasks and was compared against seven baselines fine-tuned individually per task. The evaluations considered supervised models SPaRCNet [141], ContraWR [142], CNN- Transformer [143], FFCL [144], ST-Transformer [145], BIOT, and LaBraM as baselines. Evaluations showed that joint fine-tuning with prompting is feasible and achieves reasonable performance across all tasks. However, NeuroLM did not perform as well as the LaBraM model on any of the tasks, where LaBraM was fine-tuned separately for each task. Evaluations showed that the TUAB and TUEV performance of NeuroLM variants was not sensitive to model size, whereas the performance on HMC and Workload tasks decreased with larger variants. FoME: This model was evaluated on 7 tasks across 4 datasets (MAYO, FNUSA, SEED, SleepEDFx), and eval- uations considered several fully-supervised models (LSTM [149], ConvNeXt [150]), general time series models (PatchTST, TimesNet), and some EEG-FMs (BrainBERT, Neuro-GPT, LaBraM) as baselines. Evaluations showed that, in emotion classification, sleep staging, events classification, and pathology detection tasks, FoME performed competitively or better than all baselines, whereas its performance was significantly better in signal forecasting tasks.

13/35

<!-- page 14 -->

Interestingly, the evaluations also demonstrated that general time-series models, such as PatchTST and TimesNet, perform reasonably well on pathology detection after fine-tuning, despite not being pretrained on brain signals. BrainWave: This model was evaluated using multiple scalp and intracranial EEG datasets and was compared against LaBraM – a scalp-EEG-FM, BrainBERT – an intracranial EEG-FM, and MOMENT [151] – a general time series FM. Evaluations considered different criteria, including class prototype-based few-shot classification and cross-domain transfer learning across subjects, sites, and diagnostic subtypes. Results showed that BrainWave significantly outperformed all the baselines in all settings, with an average improvement of 0.21 AUC points across 12 tasks, establishing its superiority in challenging out-of-distribution evaluations. Evaluations on common tasks: We observed that two datasets, TUAB for abnormal EEG classification (two classes) and TUEV for EEG event detection (six classes), have been widely utilized for downstream evaluation. Note that both TUAB and TUEV are scalp EEG datasets derived from the larger TUH EEG corpus. In Figure 3a-3b, we compare the performances reported on these common tasks. We also analyzed the impact of the pretraining data size on the x-axis. For comparison, we use AUC and F1 scores as performance metrics, as they are the most commonly reported metrics for these two tasks. Linear probing results were available only in LaBraM and are indicated by a triangle in the figure. The remaining results are based on fine-tuning experiments conducted by LaBraM, NeuroLM, EEGFormer, and BIOT. We find that AUC values ranged 0.86−0.92 for TUAB abnormal EEG classification and F1-scores ranged 0.70−0.83 for TUEV event classification, highlighting significant performance variation across models. These comparisons also suggested that increasing the size of the pretraining dataset did not necessarily improve model performance on these two tasks.

(a) TUAB: normal vs. abnormal classification.

(b) TUEV: six-class event classification.

Figure 3. Performances on common tasks. Here we compare EEG foundation models based on their performance on the common Temple University EEG Corpus tasks – TUAB (abnormal EEG classification) and TUEV (event classification) – along with the size of the dataset used for pretraining. The performance of FoME in 3b is shown as a line because the pretraining data size was unavailable. Channel-hours are on a 103 scale. All scores represent fine-tuned model performance, except for the triangular markers, which represent linear-probed model performance.

Apart from downstream task evaluations, some models performed additional evaluations focused on model interpretability, pretraining quality, and ablations. We briefly summarize those evaluations below. Interpretability analyses: An analysis performed in BrainBERT used the intrinsic dimensionality (ID) measure to assess task-specific embeddings post-finetuning. ID is a geometric measure that quantifies the minimum number of parameters required to represent embeddings [71]. They showed that, in their model, the electrode ID distribution lies in a lower-dimensional space compared to a randomly initialized model. Furthermore, they showed that electrodes in the top 10th percentile of IDs mainly fall in brain regions associated with the task. Similarly, EEGFormer, one of the three models that utilized a vector quantizer to train a neural codebook, analyzed the learned codebook to attribute

14/35

<!-- page 15 -->

parts of the input EEG data to downstream task predictions. In their analysis, codes most likely to predict seizures were mapped back to the EEG traces to visualize where the model focused. These highlighted regions corresponded to known epileptiform patterns, indicating that the model’s decisions aligned with meaningful clinical markers. Pretraining quality: Some models evaluated pretraining quality through qualitative and quantitative assessments. Most qualitative assessments were based on visualizations of data reconstructed by the specific models, which were run in Mentality, LaBraM, and BrainBERT. Quantitative assessments focused on reconstruction error (e.g., Mentality) and performance on forecasting and imputation tasks (e.g., Brant, FoME). Ablations: Few models evaluated the contributions of various model components or datasets to task performance via ablations. An experiment in Neuro-GPT, which combined a convolutional transformer and a GPT decoder, showed that removing the GPT decoder significantly improved downstream performance. Experiments in Brant evaluated the contributions of temporal, spatial, and frequency encoders and demonstrated that, while all components were valuable for learning EEG representations, the temporal encoder made the greatest contribution. Additionally, LaBraM showed that spatial embeddings are crucial for pretraining to converge and for downstream performance. Furthermore, LaBraM studied the effect of the codebook during pretraining by replacing the neural tokenizer with traditional time- and frequency-domain masked reconstruction and showed that this degraded performance for complex downstream tasks such as TUEV. NeuroLM showed that different neural tokenizer training tasks (frequency vs. temporal vs. frequency and temporal reconstruction) can be beneficial for different downstream tasks. Additionally, NeuroLM examined the impact of model pretraining duration by fine-tuning different checkpoints, but the results were inconclusive. An experiment in BrainWave performed data ablation by training separate models with scalp and intracranial EEG and compared their performance with joint scalp-iEEG training. Their results indicated that joint training generally improved downstream performance in all tasks, except one.

## 5 Key Takeaways and Research Gaps

This section presents several key observations made across the preceding comparative analyses (Section 4) and highlights the research gaps that remain. We believe that addressing these gaps would make future EEG-FMs more principled in their methodology and trustworthy for scientific and clinical investigations.

5.1 Key Takeaways Diversity of pretraining data: Several EEG-FMs (LaBraM, NeuroLM, FoME, and BrainWave) leveraged a diverse set of EEG domains spanning clinical, sleep, and task-based BCI. Notwithstanding potential confounders such as preprocessing, data splits, and model adaptation strategies, LaBraM’s lead in the TUAB and TUEV evaluations (Figure 3) may have emerged from its higher diversity in pretraining data, i.e., the number of distinct data sources, compared to EEGFormer and BIOT. LaBraM also performed competitively in seizure detection and events classification tasks on the MAYO and FNUSA datasets as reported in FoME’s evaluations. Note that LaBraM was pretrained on significantly fewer channel-hours of scalp EEG data and while TUAB and TUEV evaluations are both in-distribution assessments, MAYO-FNUSA evaluations are both iEEG datasets. The mixed use of scalp and iEEG, as done in FoME and BrainWave, can be considered as another form of data diversity. Using data ablations (scalp EEG vs. iEEG), BrainWave demonstrated that joint pretraining (scalp EEG + iEEG) boosts downstream task performance and transfer to unseen data types (electrocardiograms). Overall, the notion of data diversity, in conjunction with data volume, may influence the performance, generalizability, and transferability of EEG-FMs. Minimal data preprocessing: Most EEG-FMs perform minimal and simple data preprocessing steps, namely filtering and resampling, to standardize EEGs from various sources. Notably, the removal of noise-related outliers, suppression of EEG artifacts, and site-related harmonization were not explicitly pursued. Moreover, data normal- ization strategies that produce training-ready samples were not sufficiently described in most studies. It remains unclear whether or how various offline data handling strategies impact EEG-FM pretraining and downstream task performance, particularly with out-of-distribution test data. Multivariate time series EEG representation: All but four EEG-FMs utilized the native multivariate time series representation of EEG, while two models utilized the spectral representations. Two other models combined time- series and spectral representations as input, while the remaining two models exclusively adopted time-frequency

15/35

<!-- page 16 -->

(a) Impact of progressive learning paradigms (A →D) on downstream EEG classifications.

(b) Model scaling and performance gains.

Figure 4. The impact of learning paradigm and model scaling on task performance. In 4a, we compare the impact of learning paradigms – feature-based statistical machine learning (ML), supervised deep learning, and self-supervised pretraining (proposed EEG-FMs and other baselines) – on task performance. For each model, a specific task is represented using a unique color, and finetuning and linear-probing evaluations are represented using ⃝and △, respectively. Note that downstream tasks and the metrics differ across models. In 4b, we analyze the impact of model scaling on task performance. Although model sizes are specific to each study, we use ‘Sm.’, ‘Md.’, ‘Lg.’, to represent the smallest, intermediate, and the largest variants, respectively. Within each model, a specific task

is represented using a unique color.

representations. Subsequently, the respective EEG inputs were positionally encoded with their spatial and temporal order. Due to a lack of shared downstream evaluations and ablation studies, it is difficult to assess the relative contributions of different EEG input representations and spatial positional encoding schemes. Furthermore, the context length of the EEG-FMs did not exceed 90 seconds (FoME), and as such, they may struggle to capture long-range EEG patterns, relationships, or dependencies. Temporal sequence modeling: Sequence-based transformer blocks were the primary workhorse of representation learning in most EEG-FMs, with the exception of Mentality, which was based on a Mamba-based architecture. A few models (NeuroLM, Neuro-GPT) utilized convolutions to capture low-level morphological features of time-domain EEG. However, the modeling of spatial EEG relationships was either ignored or limited to the positional encoding step. BrainWave, a notable exception in this trend, integrated a spatial attention mechanism. Supporting such emphasis on temporal modeling, the ablation experiments in Brant showed that their temporal encoder provided the largest contribution to downstream task performance, compared to the spatial encoder and frequency encoding. Pretraining using masked reconstruction: Reconstruction of masked temporal EEG sequences was the predomi-

16/35

<!-- page 17 -->

nant EEG-FM pretraining paradigm, albeit with varying strategies for masking of sequence tokens/patches. Despite its origins in vision and language domains, this SSL strategy seemingly holds merit in the EEG domain. However, the generalizability of representations learned during pretraining is generally unclear since most evaluations were performed after fine-tuning on downstream data. In addition, several studies (LaBraM, NeuroLM, EEGFormer) employed a learned discrete neural codebook to further facilitate the pretraining process. In auxiliary efforts, this codebook can support interpretability (EEGFormer) and interface with discrete language vocabularies (NeuroLM). Limited model evaluations: Task performance after fine-tuning was the primary paradigm of EEG-FM evaluation. However, in four of the ten reviewed studies (BrainBERT, Mentality, NeuroLM, and FoME), the downstream evaluation datasets were already used for pretraining, i.e., the evaluations were in-distribution. However, notably, BrainWave and Brant are the only studies to have performed out-of-distribution evaluations using unseen datasets (see Supplementary Table 2). Direct model rankings beyond the TUAB and TUEV tasks are difficult to determine due to heterogeneous selections of downstream tasks across most EEG-FMs (see Table 2). Even when considering the TUAB and TUEV tasks, only four out of the ten EEG-FMs can be ranked, as depicted on the y-axis in Figures 3a and 3b, respectively. In addition, linear probing and few-shot evaluations were rarely reported (see Fig. 4a and Supplementary Table 2, respectively). Overall, the number of meaningful EEG classification tasks evaluated in each study ranged from 1 (Mentality) to 12 (BrainWave), with most studies evaluating proposed EEG-FMs on at most 5 tasks. Overall, the universality and robustness of EEG-FMs have not been convincingly demonstrated in most studies, with BrainWave being a notable exception. Model scaling and task performance: In Figure 4b, we analyze the impact of model scaling on task performance using studies with at least two model variants. Each line plot indicates a specific downstream task and the x- axis shows model variants, which were typically classified as small, intermediate, and large. Some marginal improvements can be observed for certain tasks and models, although these variants were developed with a fixed amount of pretraining data and were evaluated within study-specific experimental and methodological contexts. Notably, LaBraM investigated the combined effects of pretraining data and model scale on downstream TUAB/TUEV classifications. Overall, it is unclear whether a clear and strong trend exists with model scaling, especially within the current EEG-FM parameter regime ranging from 3.3M (BIOT) to 1.7B (NeuroLM, largest variant). Performance of general-purpose time series models: Interestingly, we observed that general time series foundation models, such as TimesNet [152], performed reasonably well on several EEG tasks after fine-tuning and sometimes outperformed EEG-FMs (e.g., sleep-stage classification in FoME). Additionally, experiments in BrainWave show that a time series FM – MOMENT [151] – outperformed EEG-FMs in specific tasks, such as seizure detection and pathology detection. Experiments in Brant show that general time series architectures, such as PatchTST [153] and CoST [133], perform relatively better on some tasks, such as short- and long-term signal forecasting and imputation, respectively, than some EEG-specific architectures. However, other results reported in BrainWave and FoME suggest that EEG-specific inductive biases and modeling choices (e.g., spatial modeling, multi-scale modeling of intracranial and scalp data, time-frequency representations, diverse clinical characteristics) can indeed help EEG-FMs outperform general time-series FMs (TS-FMs) in EEG-specific tasks. Overall, these findings indicate that TS-FMs may provide moderate value in certain EEG tasks due to efficient model adaptation via fine-tuning or larger-scale general pretraining on time series containing richer and more diverse semantics than EEG. Data scaling and task performance: The trend along the x-axis of Figures 3a and 3b suggests that scaling up pretraining data may not necessarily increase downstream task performance, even with significant model scale-up (e.g., LaBraM vs. EEGFormer/NeuroLM). Notably, LaBraM demonstrated that the effects of pretraining data scaling on TUAB and TUEV classifications are sharpest under ∼1000 hours of data and begin to plateau thereafter. Overall, the evidence for data scaling is weak, if any, based on the limited shared tasks and models evaluated thus far. Advance over other feature paradigms: In Figure 4a, we compare progressive feature paradigms (i.e., expert features, supervised EEG-DL features, SSL baselines, and proposed EEG-FMs) on various tasks. In a majority of tasks, proposed EEG-FMs (‘D’) provided at least some improvement after fine-tuning, if not drastic, over previous DL (‘B’) and self-supervised baselines, including previous EEG-FMs (‘C’). Linear probing results, however, were relatively worse. Fine-tuned EEG-FMs showed substantial improvements over classical machine learning (ML) models with expert features (‘A’), although such assessments were reported in only four studies.

17/35

<!-- page 18 -->

5.2 Current Research Gaps Data and model scaling: The scaling up of data and models is a defining principle of foundation modeling. However, empirical evidence of scaling in EEG-FMs has been either weak, limited, or inconclusive. Investigations that scale up data volume (channel-hours), model size (trainable parameters), and evaluate on an expansive set of downstream tasks are lacking in current EEG-FMs, particularly at sufficiently large scales where effects are clear and discernible. Preprocessing and normalization effects: EEG datasets can require significant offline preprocessing to manage data quality and suppress artifacts. Since current studies perform minimal processing, it is unclear whether or to what extent data outliers and noise impact EEG-FM pretraining and task performance. Even clean EEG datasets require careful consideration of normalization strategies as EEG can vary across channels, subjects, and acquisition sites [5]. The choice of input representation can further complicate decisions related to preprocessing and normalization. As such, there is a need to better understand the impact of these choices on downstream EEG-FM modeling. Model ablations: EEG-FM design involves two significant choices: the input representations and the internal architectural components. However, the lack of systematic exploration of the effects of these choices in existing EEG-FM literature prevents principled choices in EEG-FM design. The relative merits of time-domain and time- frequency domain inputs remain unclear, although both appear to be effective. The contributions of positional encoding schemes, both temporal and spatial, can be better understood. Similarly, the effects of time-domain and channel-domain spatial attention mechanisms on learned patterns remain poorly understood. Long temporal context and spatial modeling: Slow variations over long timescales can be observed in multi-day intracranial and scalp EEGs [154]. Additionally, there is substantial spatial and temporal variation in EEG across behavioral states (e.g., deep sleep versus wake, eyes open versus eyes closed). However, current EEG-FMs can only process patterns within EEG sequences spanning 90 seconds or less. There is a need for solutions that expand the effective context length of EEG-FMs. Moreover, the explicit modeling of spatial or inter-channel relationships and their contributions relative to temporal modeling remains to be investigated. Quality of pretraining strategy: EEG-FM linear probing evaluations reported by some studies have performed significantly worse than fine-tuned versions and other baselines in several instances (see Figure 4a). However, some gains can be observed when FMs are fine-tuned on task data compared to fully supervised training on the same data. This contrasting observation casts doubt on the quality of the representations learned via self-supervision in EEG-FMs. Further investigations into the effects of SSL pretraining on downstream evaluations are needed to fully understand the extent of transferability achieved through SSL. Beyond the SSL strategy itself, the effects of data diversity, data volume, and model scale on the quality of EEG-FM pretraining remain unknown. Practically relevant evaluations and metrics: Current fine-tuning evaluations are limited in their ability to assess the practical utility of EEG-FMs in real-world settings. There is a need to adopt evaluation schemes and task metrics that capture the reality of EEG research and clinical use. Evaluations on out-of-distribution data and novel tasks are required to assess the off-the-shelf value of EEG-FMs. Few-shot or low-label performance, when measured in absolute terms rather than percentages, can capture how efficiently EEG-FMs leverage labels that are typically expensive and laborious to collect. Out-of-distribution performance on a known task without fine-tuning can help understand EEG-FM robustness to the idiosyncratic cross-subject and cross-site variability of EEG. Furthermore, application-specific, practically relevant metrics, such as false positives per hour for seizure detection, and comparisons with expert features can clarify the real-world utility of EEG-FMs. Finally, evaluations must account for the unbalanced nature of physiological data and its influence on metrics and model outcomes. For example, in seizure detection settings, patient data consists mostly of interictal segments, with seizure events occurring rarely. Evaluations must reflect this natural imbalance to assess the model’s real-world utility faithfully. Standardized benchmarking tasks: The comparative analysis revealed significant heterogeneity in the tasks used for EEG-FM evaluation (see Table 2). The lack of common tasks across EEG-FM evaluations makes it challenging to understand the state of the art and highlights the need to identify a common core set of evaluations for future EEG-FM development. This set must cover multiple task types and include both classification and regression tasks, with dense (one label per EEG recording) and sparse (one label per EEG segment) labels. Additionally, the tasks must be challenging enough for previous generations of EEG-DL models, with ample room for improvement, unlike TUAB, where performance may already have saturated (85-87% accuracy) with traditional approaches [155]. Finally,

18/35

<!-- page 19 -->

the tasks must reflect the data heterogeneity encountered in clinical settings, including wake and sleep patient states. Trustworthy modeling: Despite the importance of explainability and uncertainty handling in the high-risk, expert- centric domain of medicine, experiments probing trust-related aspects of EEG-FMs have been limited. Notably, preliminary interpretability analyses based on intrinsic dimensionality and codebooks were conducted for BrainBERT and EEGFormer, respectively. However, studies that further demystify the EEG-FM black box are needed to gain insight into the knowledge learned by EEG-FMs (EEG patterns, dependencies, relationships) and the practical robustness of their decision-making process for downstream applications. Connections to known patterns of brain physiology or pathology may be necessary to make EEG-FMs trustworthy in the eyes of expert and clinical users.

## 6 Proposed Future Directions

From a time series perspective, EEG signals are distinct from general signals or sequences due to their non-linearity [156], non-stationarity [156], complex spatial relationships, and 1/f spectral characteristics [157]. These peculiarities would suggest that foundation modeling for EEG signals requires domain-specific inductive biases. Indeed, we have cultivated an EEG data-centric and domain-sensitive perspective throughout this review. However, counter- intuitively, EEG-FMs have enjoyed some success in drawing from vision and language domains in their adoption of patch-based sequences and transformer architecture design (transformer [47], vision transformer [64]), masked reconstruction-based SSL (masked autoencoders [126]), and discrete neural codebooks (VQ-VAE [125], BEiT v2 [158]). Moreover, time series FMs pretrained on generic, non-neural time series have performed similarly to EEG-FMs on certain EEG tasks. Therefore, it is likely that future EEG-FMs could benefit from embracing both domain-specific insights and innovations from external data domains. These domains may be semantically distant to EEG, such as vision and natural language, or loosely related, such as non-neural time series, audio, speech, or other biosignals. Below, we outline the future research directions that we believe could support meaningful and sustained progress in the EEG-FM research domain. As illustrated in Figure 5, these recommendations are organized under three broad themes of development spanning benchmarks and software tools, technical advances, and real-world applications. These suggestions build upon the research gaps identified earlier and provide additional guidance for advancing and accelerating EEG-FM research and adoption.

Figure 5. Suggested future directions. (I) Benchmarks and tools: future EEG foundation models can be compared using standardized benchmarks against prevailing feature paradigms and participate in community-specific EEG challenges to establish their real-world utility. Frictionless and user-friendly software tools are needed to quickly adopt and experiment with off-the-shelf models. (II) Technical modeling: holistic evaluation frameworks that test embedding space semantics, robustness, and transfer efficiency can meaningfully track the state of the art. Advanced representation learning techniques, such as federated or multi-modal learning, can enhance large-scale pretraining. (III) Applications: collaborations with domain experts can inspire novel applications. Strategies that help identify suitable off-the-shelf models for a particular task and address translational hurdles, such as clinical interpretability, prospective validation, and operational feasibility, can increase adoption and impact.

19/35

<!-- page 20 -->

6.1 Benchmarks and Tools Benchmarking against prevailing feature paradigms: Quantitative EEG research currently employs two ML feature paradigms: expert-crafted EEG features and task-specific supervised features. As such, data-driven self- supervised features, such as those provided by EEG-FMs, remain in their infancy. Therefore, to establish a compelling case for EEG-FM adoption, studies proposing novel EEG-FMs should evaluate against the prevailing feature paradigms. In doing so, statistical tests of superior performance must be presented when necessary. Additionally, identical subject-level splits must be used to control for inter-subject variability, and temporal past/future splits must be used to account for the temporal order of events in longer-term EEG data. Standardized community-specific benchmarks: The primary failure mode of EEG encoders remains their inability to learn robust latent features that generalize across realistic EEG distribution shifts, including those seen across subjects, age groups, acquisition setups, and experimental or clinical conditions, among other factors. However, each EEG user community (e.g., clinicians, brain computer interface users, neuroscientists) may have different practical requirements or definitions of model robustness and generalization. Therefore, future work can design community- specific EEG-FM benchmarks with clear task definitions, realistic performance criteria beyond traditional metrics, real-world datasets, and expert baselines. In doing so, EEG researchers can draw inspiration from existing FM benchmarks in other data domains. Standardized benchmarks tailored to each community’s needs can significantly boost the chances of real-world translation and adoption of EEG-FMs. Ranking EEG-FMs in global EEG competitions: Novel EEG-FM methodology can leverage international predictive modeling competitions to establish real-world performance and utility, as those competitions can highlight the most significant empirical challenges or milestones within the field. Such competitions have already been developed for time series [159], electrocardiograms [160], and speech [161] domains. Notably, within the EEG domain, previous competitions have highlighted issues with transfer learning under distribution shifts [162], abnormality detection [163], coma prognosis [164], seizure detection [165], and seizure forecasting [166]. Frictionless software: Several software modifications and code debugging are required to run the currently available EEG-FMs. The deep technical nature of EEG-FMs and the computing skills required to run these models pose a significant entry barrier for non-technical or non-computational researchers. Future studies will need to ensure that EEG-FMs can be used as off-the-shelf feature-extraction tools, with no technical modifications required. Graphical software for plug-and-play EEG-FM analytics, such as simple binary classifications, can greatly increase real-world EEG-FM adoption, testing, and experimentation. Encouragingly, a mature ecosystem for large-scale EEG analytics already exists in Python [167–169] and can support the development of frictionless EEG-FM software.

6.2 Technical Development Holistic evaluation schemes: Future studies may benefit from focusing specifically on out-of-distribution evalua- tions, as they can directly assess the effectiveness of EEG-FM pretraining and performance in realistic, off-the-shelf, and low-label scenarios. Furthermore, evaluating EEG-FMs based on their task performance on a narrow set of commonly available EEG datasets/tasks is insufficient to measure their real-world readiness. Novel evaluation and model ranking schemes can be designed to assess the computational costs, semantic EEG-FM embedding quality, transfer efficiency, and robustness to real-world EEG variability and noise sources. Privacy-preserving learning: EEG datasets required for large-scale EEG-FM pretraining can be siloed due to patient privacy and legal concerns. Research collaborations involving multiple clinical sites can utilize federated learning [170] techniques to train EEG-FMs without requiring centralized data access or sharing. Such techniques may also support the derivation of personalized, i.e., patient-specific, models from EEG-FMs. Multi-modal learning: Latent representations learned during pretraining may benefit from cross-modal supervision from text reports, video recordings, or other biosignals, such as electrocardiograms. Some of these modalities are jointly recorded with EEGs in many clinical and scientific recording settings. Notably, downstream applications can reap the performance benefits of multi-modal pretraining without requiring those modalities during evaluation. Reasoning and agentic capabilities: Future EEG-FMs could be fine-tuned to mimic expert reasoning processes, adhere to expert grading criteria [171] or instructions, and autonomously retrieve relevant evidence from verified medical literature repositories and knowledge bases. Augmented healthcare workflows could leverage insights from

20/35

<!-- page 21 -->

multiple specialized modality-specific agents to inform clinical decisions. Scaling down task-specific EEG-FMs: FMs may require model parameter scaling to obtain superior pretrained features. However, large EEG-FMs may not be suitable for applications involving streaming EEG data, real-time EEG processing, or deployment in resource-constrained settings, such as brain-computer interfaces, medical devices, and clinical environments. In such contexts, knowledge distillation [172], pruning [173], or quantization [174] techniques can deliver smaller, computationally inexpensive models that maintain high task performance. Timeseries FMs, task semantics, and inductive biases: The relative maturity of general time-series FMs (TS-FMs) can serve as a source of inspiration for EEG-FM development. For example, an understanding of how TS-FMs learn effectively from large, diverse datasets across economic, energy, traffic, climate, and industrial domains may improve EEG-FM scaling. TS-FM performance may be particularly instructive when an EEG task shares underlying semantics with more general time-series tasks, such as forecasting or anomaly detection. There may exist opportunities to ‘specialize’ TS-FMs by injecting EEG-specific biases into data representation, model design, and the self-supervised learning objective. Future EEG-FM studies can assess the utility of such biases in adapting TS-FMs for EEG tasks and the relative merits and weaknesses of TS-FMs.

6.3 Application Development Cross- and inter-disciplinary collaboration: The technical development of EEG-FMs should involve close collaboration with scientific and clinical experts. Such collaborations can productively constrain and inspire novel modeling decisions, identify novel research gaps, establish clear criteria for real-world success or progress, and facilitate EEG-FM experimentation among niche application-specific audiences. Model cards to guide EEG-FM selection: The availability of multiple EEG-FMs, each purportedly an off-the- shelf tool, poses a practical dilemma for domain experts who must make a principled selection for their research. Comprehensive comparisons of all available options may not be feasible in discovery-based research. The release of model cards [175] that summarize an EEG-FM’s functional strengths and weaknesses, inherent or dominant inductive biases, compute requirements, and evaluation scope and rankings could inform the model selection process. Clinical applications: There is a substantial opportunity for EEG-FMs to augment the clinical EEG review process in both short- and extended-duration monitoring settings. EEG-FMs could speed up review by guiding the reviewer’s attention to noteworthy temporal segments, brain regions, or channels distinct from background activity, especially in longer recordings, such as in epilepsy- or sleep-related applications. Based on these clues, an EEG-FM coupled with a text decoder could summarize the clinically relevant findings as a structured text report. Additionally, EEG-FMs could support case-based clinical reasoning by surfacing historical records with shared EEG phenotypes. Finally, EEG-FMs could improve the performance of spike and seizure detections generated by EEG reviewing software. Translational hurdles: Several hurdles and considerations prevent the translation and adoption of EEG-FMs in clinical practice. Testing and validation. Prospective pilot testing for specific use cases using site-specific patient data can provide actionable evidence on the feasibility of model deployment and its benefits to clinical stakeholders. The graceful handling of data noise, corruption, and missing values is required for operational success. Interpretability. Interfaces that relate EEG-FM outputs to clinical domain knowledge and patient-specific physiological factors could increase clinician trust and adoption. Reproducibility. Developers must transparently report and release the data sources, data splits, patient characteristics, and computational pipeline configurations that were utilized to build the EEG-FM to maintain reproducibility. Regulatory considerations. EEG-FMs and task-specific fine-tuned models will be treated as safety-critical medical artificial intelligence (AI) systems that must adhere to stringent national or international guidelines. Therefore, clinical users should focus on defining clear intended use, rigorous validation, and controlled deployment. Attention should be given to documenting data provenance, identifying known limitations and expected failure modes, and establishing human-AI teaming protocols that keep clinicians in the loop. Clinical adoption should follow medical-device regulatory pathways, including risk assessment, post-market monitoring, and predefined change-control procedures to manage model updates as data distributions evolve.

21/35

<!-- page 22 -->

## 7 Conclusion

The promise of EEG foundation models, in principle, lies in effective and robust feature learning, feature re-usability, and label efficiency. Our critical analysis of ten early EEG-FMs indicates that these efforts, inspired by their counterparts in the mainstream vision and language domains, have made moderate strides in realizing this promise for the EEG domain. However, to develop universal, robust, and general-purpose EEG feature extractors, future EEG-FMs must prioritize substantial scaling efforts, principled and trustworthy self-supervised representation learning, and practically relevant evaluations. In addition to technical modeling, we believe that future research should also pursue the collaborative development of meaningful EEG benchmarks, including standardized datasets, applications, and holistic model evaluation schemes that can measurably track the real-world readiness and impact of EEG-FMs. With sustained efforts in these directions, EEG-FMs are poised to advance scientific research, brain-computer interfaces, and clinical decision support systems.

## 8 Acknowledgments

We would like to thank Mario Serrafero and Saeid Cheshmi for fruitful discussions on foundation modeling.

## 9 Funding

This study was supported in part by the Mayo Clinic & Illinois Alliance Fellowship for Technology-based Healthcare Research, the Edward Heiken Interdisciplinary Health Sciences Institute Fund, and NSF grants IIS-2105233, IIS-2344731, and IIS-2337909.

## 10 Data Availability

This review did not generate any new data. A visual summary of the EEG-FMs included in this review and links to their original code repositories will be made available via a publicly accessible repository upon acceptance.

## 11 Conflicts of Interest

None.

22/35

<!-- page 23 -->

## References

1. Mushtaq, F., Welke, D., Gallagher, A., Pavlov, Y. G., Kouara, L., Bosch-Bayard, J., van den Bosch, J. J. F., Arvaneh, M., Bland, A. R., Chaumon, M., et al. One Hundred Years of EEG for Brain and Behaviour Research. Nature Human Behaviour 8, 1437–1443. ISSN: 2397-3374. (2025) (Aug. 2024).

2. Roy, Y., Banville, H., Albuquerque, I., Gramfort, A., Falk, T. H. & Faubert, J. Deep Learning-Based Electroen- cephalography Analysis: A Systematic Review. Journal of Neural Engineering 16, 051001. ISSN: 1741-2552. (2025) (Aug. 2019).

3. Craik, A., He, Y. & Contreras-Vidal, J. L. Deep Learning for Electroencephalogram (EEG) Classification Tasks: A Review. Journal of Neural Engineering 16, 031001. ISSN: 1741-2552. (2025) (Apr. 2019).

4. Obeid, I. & Picone, J. The temple university hospital EEG data corpus. Frontiers in neuroscience 10, 196 (2016).

5. Wagh, N., Wei, J., Rawal, S., Berry, B. M. & Varatharajah, Y. Evaluating latent space robustness and uncertainty of EEG-ML models under realistic distribution shifts. Advances in Neural Information Processing Systems 35, 21142–21156 (2022).

6. Banville, H., Chehab, O., Hyvärinen, A., Engemann, D.-A. & Gramfort, A. Uncovering the structure of clinical EEG signals with self-supervised learning. Journal of Neural Engineering 18, 046020 (2021).

7. Bommasani, R., Hudson, D. A., Adeli, E., Altman, R., Arora, S., von Arx, S., Bernstein, M. S., Bohg, J., Bosselut, A., Brunskill, E., et al. On the opportunities and risks of foundation models. arXiv preprint arXiv:2108.07258 (2021).

8. Yuan, L., Chen, D., Chen, Y.-L., Codella, N., Dai, X., Gao, J., Hu, H., Huang, X., Li, B., Li, C., et al. Florence: A new foundation model for computer vision. arXiv preprint arXiv:2111.11432 (2021).

9. Kirillov, A., Mintun, E., Ravi, N., Mao, H., Rolland, C., Gustafson, L., Xiao, T., Whitehead, S., Berg, A. C., Lo, W.-Y., et al. Segment anything in Proceedings of the IEEE/CVF international conference on computer vision (2023), 4015–4026.

10. Radford, A., Kim, J. W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., Sastry, G., Askell, A., Mishkin, P., Clark, J., et al. Learning transferable visual models from natural language supervision in International conference on machine learning (2021), 8748–8763.

11. Chowdhery, A., Narang, S., Devlin, J., Bosma, M., Mishra, G., Roberts, A., Barham, P., Chung, H. W., Sutton, C., Gehrmann, S., et al. Palm: Scaling language modeling with pathways. Journal of Machine Learning Research 24, 1–113 (2023).

12. Touvron, H., Lavril, T., Izacard, G., Martinet, X., Lachaux, M.-A., Lacroix, T., Rozière, B., Goyal, N., Hambro, E., Azhar, F., et al. Llama: Open and efficient foundation language models. arXiv preprint arXiv:2302.13971 (2023).

13. Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I., Aleman, F. L., Almeida, D., Altenschmidt, J., Altman, S., Anadkat, S., et al. Gpt-4 technical report. arXiv preprint arXiv:2303.08774 (2023).

14. Wang, C., Subramaniam, V., Yaari, A. U., Kreiman, G., Katz, B., Cases, I. & Barbu, A. BrainBERT: Self- supervised representation learning for intracranial recordings. arXiv preprint arXiv:2302.14367 (2023).

15. Cui, W., Jeong, W., Thölke, P., Medani, T., Jerbi, K., Joshi, A. A. & Leahy, R. M. Neuro-gpt: Towards a foundation model for eeg in 2024 IEEE International Symposium on Biomedical Imaging (ISBI) (2024), 1–5.

16. Zhang, D., Yuan, Z., Yang, Y., Chen, J., Wang, J. & Li, Y. Brant: Foundation model for intracranial neural signal. Advances in Neural Information Processing Systems 36 (2024).

17. Yang, C., Westover, M. & Sun, J. Biot: Biosignal transformer for cross-data learning in the wild. Advances in Neural Information Processing Systems 36 (2024).

23/35

<!-- page 24 -->

18. Chen, Y., Ren, K., Song, K., Wang, Y., Wang, Y., Li, D. & Qiu, L. EEGFormer: Towards transferable and interpretable large-scale EEG foundation model. arXiv preprint arXiv:2401.10278 (2024).

19. Jiang, W.-B., Zhao, L.-M. & Lu, B.-L. Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI en. arXiv:2405.18765 [cs]. May 2024. http://arxiv.org/abs/2405. 18765 (2024).

20. Panchavati, S. & Speier, W. Mentality in ICLR 2024 Workshop on Learning from Time Series For Health (2024). https://openreview.net/forum?id=O6T38rRiFp.

21. Jiang, W.-B., Wang, Y., Lu, B.-L. & Li, D. NeuroLM: A Universal Multi-task Foundation Model for Bridging the Gap between Language and EEG Signals arXiv:2409.00101 [cs, eess]. Aug. 2024. http://arxiv. org/abs/2409.00101 (2024).

22. Shi, E., Zhao, K., Yuan, Q., Wang, J., Hu, H., Yu, S. & Zhang, S. FoME: A Foundation Model for EEG using Adaptive Temporal-Lateral Attention Scaling en. arXiv:2409.12454 [cs, eess]. Sept. 2024. http: //arxiv.org/abs/2409.12454 (2024).

23. Yuan, Z., Shen, F., Li, M., Yu, Y., Tan, C. & Yang, Y. BrainWave: A Brain Signal Foundation Model for Clinical Applications 2024. arXiv: 2402.10251 [q-bio.NC]. https://arxiv.org/abs/2402.10251.

24. Yuxuan, Y., Hongbo, W., Li, C., Yiheng, P. & Luo, J. Foundation models for EEG decoding: current progress and prospective research. Journal of Neural Engineering (2025).

25. Zhou, X., Liu, C., Chen, Z., Wang, K., Ding, Y., Jia, Z. & Wen, Q. Brain foundation models: A survey on advancements in neural signal processing and brain discovery. arXiv preprint arXiv:2503.00580 (2025).

26. Weng, W., Gu, Y., Guo, S., Ma, Y., Yang, Z., Liu, Y. & Chen, Y. Self-supervised learning for electroencephalo- gram: A systematic survey. ACM Computing Surveys 57, 1–38 (2025).

27. Tatum, W. O., Rubboli, G., Kaplan, P. W., Mirsatari, S., Radhakrishnan, K., Gloss, D., Caboclo, L., Drislane, F., Koutroumanidis, M., Schomer, D., et al. Clinical utility of EEG in diagnosing and monitoring epilepsy in adults. Clinical Neurophysiology 129, 1056–1082 (2018).

28. Da Silva, F. L. EEG and MEG: relevance to neuroscience. Neuron 80, 1112–1128 (2013).

29. Värbu, K., Muhammad, N. & Muhammad, Y. Past, present, and future of EEG-based BCI applications. Sensors 22, 3331 (2022).

30. Buzsáki, G., Anastassiou, C. A. & Koch, C. The origin of extracellular fields and currents—EEG, ECoG, LFP and spikes. Nature reviews neuroscience 13, 407–420 (2012).

31. Brunner, C., Billinger, M., Seeber, M., Mullen, T. R. & Makeig, S. Volume conduction influences scalp-based connectivity estimates. Frontiers in computational neuroscience 10, 121 (2016).

32. Petroff, O. A., Spencer, D. D., Goncharova, I. I. & Zaveri, H. P. A comparison of the power spectral density of scalp EEG and subjacent electrocorticograms. Clinical Neurophysiology 127, 1108–1112 (2016).

33. Klimesch, W. Memory processes, brain oscillations and EEG synchronization. International journal of psychophysiology 24, 61–100 (1996).

34. Oken, B. S., Salinsky, M. C. & Elsas, S.-M. Vigilance, alertness, or sustained attention: physiological basis and measurement. Clinical neurophysiology 117, 1885–1901 (2006).

35. Perinelli, A., Assecondi, S., Tagliabue, C. F. & Mazza, V. Power shift and connectivity changes in healthy aging during resting-state EEG. NeuroImage 256, 119247 (2022).

36. Amin, U., Nascimento, F. A., Karakis, I., Schomer, D. & Benbadis, S. R. Normal variants and artifacts: importance in EEG interpretation. Epileptic disorders 25, 591–648 (2023).

37. Blume, W. T. Drug effects on EEG. Journal of Clinical Neurophysiology 23, 306–311 (2006).

24/35

<!-- page 25 -->

38. Li, B., Cheng, T. & Guo, Z. A review of EEG acquisition, processing and application in Journal of Physics: Conference Series 1907 (2021), 012045.

39. Céspedes-Villar, Y., Martinez-Vargas, J. D. & Castellanos-Dominguez, G. Influence of Patient-Specific Head Modeling on EEG Source Imaging. Computational and Mathematical Methods in Medicine 2020, 5076865 (2020).

40. Smit, D. J., Boomsma, D. I., Schnack, H. G., Pol, H. E. H. & de Geus, E. J. Individual differences in EEG spectral power reflect genetic variance in gray and white matter volumes. Twin research and human genetics 15, 384–392 (2012).

41. Gao, R., Peterson, E. J. & Voytek, B. Inferring synaptic excitation/inhibition balance from field potentials. Neuroimage 158, 70–78 (2017).

42. Tatum IV, W. O. Handbook of EEG interpretation (Springer Publishing Company, 2021).

43. Popa, L. L., Dragos, H., Pantelemon, C., Rosu, O. V. & Strilciuc, S. The role of quantitative EEG in the diagnosis of neuropsychiatric disorders. Journal of medicine and life 13, 8 (2020).

44. Roy, Y., Banville, H., Albuquerque, I., Gramfort, A., Falk, T. H. & Faubert, J. Deep learning-based electroen- cephalography analysis: a systematic review. Journal of neural engineering 16, 051001 (2019).

45. Neumann, O., Ludwig, N., Turowski, M., Heidrich, B., Hagenmeyer, V. & Mikut, R. Smart data repre- sentations: impact on the accuracy of deep neural networks in Proceedings 31 workshop computational intelligence (2021), 113–130.

46. Michel, C. M. & Brunet, D. EEG source imaging: a practical review of the analysis steps. Frontiers in neurology 10, 325 (2019).

47. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł. & Polosukhin, I. Attention is all you need. Advances in neural information processing systems 30 (2017).

48. Wu, H., Xiao, B., Codella, N., Liu, M., Dai, X., Yuan, L. & Zhang, L. Cvt: Introducing convolutions to vision transformers in Proceedings of the IEEE/CVF international conference on computer vision (2021), 22–31.

49. Ericsson, L., Gouk, H., Loy, C. C. & Hospedales, T. M. Self-supervised representation learning: Introduction, advances, and challenges. IEEE Signal Processing Magazine 39, 42–62 (2022).

50. Chen, T., Kornblith, S., Norouzi, M. & Hinton, G. A simple framework for contrastive learning of visual representations in International conference on machine learning (2020), 1597–1607.

51. Zhang, C., Zhang, C., Song, J., Yi, J. S. K. & Kweon, I. S. A Survey on Masked Autoencoder for Visual Self-supervised Learning. in IJCAI (2023), 6805–6813.

52. Wagh, N., Wei, J., Rawal, S., Berry, B., Barnard, L., Brinkmann, B., Worrell, G., Jones, D. & Varathara- jah, Y. Domain-guided self-supervision of eeg data improves downstream classification performance and generalizability in Machine Learning for Health (2021), 130–142.

53. Thrun, S. & Pratt, L. in Learning to learn 3–17 (Springer, 1998).

54. Kumar, A., Raghunathan, A., Jones, R., Ma, T. & Liang, P. Fine-tuning can distort pretrained features and underperform out-of-distribution. arXiv preprint arXiv:2202.10054 (2022).

55. Sun, C., Shrivastava, A., Singh, S. & Gupta, A. Revisiting unreasonable effectiveness of data in deep learning era in Proceedings of the IEEE international conference on computer vision (2017), 843–852.

56. Dehghani, M., Djolonga, J., Mustafa, B., Padlewski, P., Heek, J., Gilmer, J., Steiner, A. P., Caron, M., Geirhos, R., Alabdulmohsin, I., et al. Scaling vision transformers to 22 billion parameters in International conference on machine learning (2023), 7480–7512.

57. Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., Gray, S., Radford, A., Wu, J. & Amodei, D. Scaling laws for neural language models. arXiv preprint arXiv:2001.08361 (2020).

25/35

<!-- page 26 -->

58. Yao, Q., Yang, C.-H. H., Jiang, R., Liang, Y., Jin, M. & Pan, S. Towards Neural Scaling Laws for Time Series Foundation Models. arXiv preprint arXiv:2410.12360 (2024).

59. Isik, B., Ponomareva, N., Hazimeh, H., Paparas, D., Vassilvitskii, S. & Koyejo, S. Scaling laws for downstream task performance of large language models in ICLR 2024 Workshop on Mathematical and Empirical Understanding of Foundation Models (2024).

60. Edwards, T. D., Alvey, J., Alsing, J., Nguyen, N. H. & Wandelt, B. D. Scaling-laws for large time-series models. arXiv preprint arXiv:2405.13867 (2024).

61. Rosenfeld, J. S., Rosenfeld, A., Belinkov, Y. & Shavit, N. A constructive prediction of the generalization error across scales. arXiv preprint arXiv:1909.12673 (2019).

62. Oquab, M., Darcet, T., Moutakanni, T., Vo, H., Szafraniec, M., Khalidov, V., Fernandez, P., Haziza, D., Massa, F., El-Nouby, A., et al. Dinov2: Learning robust visual features without supervision. arXiv preprint arXiv:2304.07193 (2023).

63. Wenzek, G., Lachaux, M.-A., Conneau, A., Chaudhary, V., Guzmán, F., Joulin, A. & Grave, E. CCNet: Extracting high quality monolingual datasets from web crawl data. arXiv preprint arXiv:1911.00359 (2019).

64. Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., et al. An image is worth 16x16 words: Transformers for image recognition at scale. arXiv preprint arXiv:2010.11929 (2020).

65. Thapa, R., He, B., Kjaer, M. R., Moore IV, H., Ganjoo, G., Mignot, E. & Zou, J. Y. SleepFM: Multi- modal Representation Learning for Sleep across ECG, EEG and Respiratory Signals in AAAI 2024 Spring Symposium on Clinical Foundation Models (2024).

66. Ogg, M. & Coon, W. G. Self-supervised transformer model training for a sleep-EEG foundation model in 2024 46th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC) (2024), 1–6.

67. Devlin, J., Chang, M.-W., Lee, K. & Toutanova, K. Bert: Pre-training of deep bidirectional transformers for language understanding in Proceedings of the 2019 conference of the North American chapter of the association for computational linguistics: human language technologies, volume 1 (long and short papers) (2019), 4171–4186.

68. Gabor, D. Theory of communication. Part 1: The analysis of information. Journal of the Institution of Electrical Engineers-part III: radio and communication engineering 93, 429–441 (1946).

69. Moca, V. V., Bârzan, H., Nagy-D˘abâcan, A. & Mures,an, R. C. Time-frequency super-resolution with superlets. Nature communications 12, 337 (2021).

70. Wang, C., Yaari, A., Singh, A., Subramaniam, V., Rosenfarb, D., DeWitt, J., Misra, P., Madsen, J., Stone, S., Kreiman, G., et al. Brain treebank: Large-scale intracranial recordings from naturalistic language stimuli. Advances in Neural Information Processing Systems 37, 96505–96540 (2024).

71. Ansuini, A., Laio, A., Macke, J. H. & Zoccolan, D. Intrinsic dimension of data representations in deep neural networks. Advances in Neural Information Processing Systems 32 (2019).

72. Obeid, I. & Picone, J. The temple university hospital EEG data corpus. Frontiers in neuroscience 10, 196 (2016).

73. Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., Sutskever, I., et al. Language models are unsupervised multitask learners. OpenAI blog 1, 9 (2019).

74. Mosher, J. C., Leahy, R. M. & Lewis, P. S. EEG and MEG: forward solutions for inverse methods. IEEE Transactions on biomedical engineering 46, 245–259 (2002).

75. Gu, A. & Dao, T. Mamba: Linear-time sequence modeling with selective state spaces. arXiv preprint arXiv:2312.00752 (2023).

26/35

<!-- page 27 -->

76. Goel, K., Gu, A., Donahue, C. & Ré, C. It’s raw! audio generation with state-space models in International conference on machine learning (2022), 7616–7633.

77. Ronneberger, O., Fischer, P. & Brox, T. U-net: Convolutional networks for biomedical image segmentation in Medical image computing and computer-assisted intervention–MICCAI 2015: 18th international conference, Munich, Germany, October 5-9, 2015, proceedings, part III 18 (2015), 234–241.

78. Lawhern, V. J., Solon, A. J., Waytowich, N. R., Gordon, S. M., Hung, C. P. & Lance, B. J. EEGNet: a compact convolutional neural network for EEG-based brain–computer interfaces. Journal of neural engineering 15, 056013 (2018).

79. Guttag, J. CHB-MIT scalp EEG database (version 1.0. 0). PhysioNet (2010).

80. Zhang, G.-Q., Cui, L., Mueller, R., Tao, S., Kim, M., Rueschman, M., Mariani, S., Mobley, D. & Redline, S. The National Sleep Research Resource: towards a sleep data commons. Journal of the American Medical Informatics Association 25, 1351–1358 (2018).

81. Kemp, B., Zwinderman, A. H., Tuk, B., Kamphuisen, H. A. & Oberye, J. J. Analysis of a sleep-dependent neuronal feedback loop: the slow-wave microcontinuity of the EEG. IEEE Transactions on Biomedical Engineering 47, 1185–1194 (2000).

82. Terzano, M. G., Parrino, L., Sherieri, A., Chervin, R., Chokroverty, S., Guilleminault, C., Hirshkowitz, M., Mahowald, M., Moldofsky, H., Rosa, A., et al. Atlas, rules, and recording techniques for the scoring of cyclic alternating pattern (CAP) in human sleep. Sleep medicine 2, 537–554 (2001).

83. Nejedly, P., Kremen, V., Sladky, V., Cimbalnik, J., Klimes, P., Plesinger, F., Mivalt, F., Travnicek, V., Viscor, I., Pail, M., et al. Multicenter intracranial EEG dataset for classification of graphoelements and artifactual signals. en. Scientific Data 7. Publisher: Nature Publishing Group, 179. ISSN: 2052-4463. https: //www.nature.com/articles/s41597-020-0532-5 (2024) (June 2020).

84. Van Blooijs, D., van den Boom, M., van der Aar, J., Huiskamp, G., Castegnaro, G., Demuru, M., Zweiphenning, W., van Eijsden, P., Miller, K. J., Leijten, F., et al. "CCEP ECoG dataset across age 4-51" (OpenNeuro,

2023).

85. Grossmann, A. & Morlet, J. Decomposition of Hardy functions into square integrable wavelets of constant shape. SIAM journal on mathematical analysis 15, 723–736 (1984).

86. Detti, P., Vatti, G. & Zabalo Manrique de Lara, G. EEG synchronization analysis for seizure prediction: A study on data of noninvasive recordings. Processes 8, 846 (2020).

87. Quan, S. F., Howard, B. V., Iber, C., Kiley, J. P., Nieto, F. J., O’Connor, G. T., Rapoport, D. M., Redline, S., Robbins, J., Samet, J. M., et al. The sleep heart health study: design, rationale, and methods. Sleep 20, 1077–1085 (1997).

88. Alvarez-Estevez, D. & Rijsman, R. M. Inter-database validation of a deep learning approach for automatic sleep scoring. PloS one 16, e0256111 (2021).

89. Hatlestad-Hall, C., Rygvold, T. W. & Andersson, S. BIDS-structured resting-state electroencephalography (EEG) data extracted from an experimental paradigm. Data in Brief 45, 108647 (2022).

90. Liu, H., Wei, P., Wang, H., Lv, X., Duan, W., Li, M., Zhao, Y., Wang, Q., Chen, X., Shi, G., et al. An EEG motor imagery dataset for brain computer interface in acute stroke patients. Scientific Data 11, 131 (2024).

91. Rockhill, A. P., Jackson, N., George, J., Aron, A. & Swann, N. C. "UC San Diego Resting State EEG Data from Patients with Parkinson’s Disease" (OpenNeuro, 2021).

92. Anjum, M. F., Dasgupta, S., Mudumbai, R., Singh, A., Cavanagh, J. F. & Narayanan, N. S. Linear predictive coding distinguishes spectral EEG features of Parkinson’s disease. Parkinsonism & related disorders 79, 79–85 (2020).

27/35

<!-- page 28 -->

93. Cavanagh, J. F., Kumar, P., Mueller, A. A., Richardson, S. P. & Mueen, A. Diminished EEG habituation to novel events effectively classifies Parkinson’s patients. Clinical Neurophysiology 129, 409–418 (2018).

94. Vicchietti, M. L., Ramos, F. M., Betting, L. E. & Campanharo, A. S. Computational methods of EEG signals analysis for Alzheimer’s disease classification. Scientific Reports 13, 8184 (2023).

95. Stevenson, N. J., Tapani, K., Lauronen, L. & Vanhatalo, S. A dataset of neonatal EEG recordings with seizure annotations. Scientific data 6, 1–8 (2019).

96. Ge, W., Jing, J., An, S., Herlopian, A., Ng, M., Struck, A. F., Appavu, B., Johnson, E. L., Osman, G., Haider, H. A., et al. Deep active learning for interictal ictal injury continuum EEG patterns. Journal of neuroscience methods 351, 108966 (2021).

97. Xiang, C., Fan, X., Bai, D., Lv, K. & Lei, X. A resting-state EEG dataset for sleep deprivation. Scientific Data 11, 427 (2024).

98. Trinh, N., Whelan, R., Ward, T. & Derosiere, G. Task-related and resting-state EEG classification of adult patients with ADHD using machine learning in 2023 IEEE 19th International Conference on Body Sensor Networks (BSN) (2023), 1–4.

99. Motie Nasrabadi, A., Allahverdy, A., Samavati, M. & Mohammadi, M. R. EEG data for ADHD/Control children. (No Title) (2020).

100. Olejarczyk, E. & Jernajczyk, W. Graph-based analysis of brain connectivity in schizophrenia. PloS one 12, e0188629 (2017).

101. jcavanagh@unm.edu, J. F. C. "EEG: Depression rest" (OpenNeuro, 2021).

102. Mumtaz, W. MDD patients and healthy controls EEG data (new). figshare, Dataset (2016).

103. Miltiadous, A., Tzimourta, K. D., Afrantou, T., Ioannidis, P., Grigoriadis, N., Tsalikakis, D. G., Angelidis, P., Tsipouras, M. G., Glavas, E., Giannakeas, N., et al. A dataset of scalp EEG recordings of Alzheimer’s disease, frontotemporal dementia and healthy subjects from routine EEG. Data 8, 95 (2023).

104. Blankertz, B., Dornhege, G., Krauledat, M., Müller, K.-R. & Curio, G. The non-invasive Berlin brain– computer interface: fast acquisition of effective performance in untrained subjects. NeuroImage 37, 539–550 (2007).

105. Savran, A., Ciftci, K., Chanel, G., Cruz Mota, J., Viet, L. H., Sankur, B., Akarun, L., Caplier, A. & Rombaut, M. Emotion detection in the loop from brain signals and facial images in Summer Workshop on Multimodal Interfaces (eINTERFACE 2006) (2006), 69–80.

106. Luciw, M. D., Jarocka, E. & Edin, B. B. Multi-channel EEG recordings during 3,936 grasp and lift trials with varying weight and friction. Scientific data 1, 1–11 (2014).

107. Margaux, P., Emmanuel, M., Sébastien, D., Olivier, B. & Jérémie, M. Objective and Subjective Evaluation of Online Error Correction during P300-Based Spelling. Advances in Human-Computer Interaction 2012, 578295 (2012).

108. Schalk, G., McFarland, D. J., Hinterberger, T., Birbaumer, N. & Wolpaw, J. R. BCI2000: a general-purpose brain-computer interface (BCI) system. IEEE Transactions on biomedical engineering 51, 1034–1043 (2004).

109. Trujillo, L. T. Mental effort and information-processing costs are inversely related to global brain free energy during visual categorization. Frontiers in neuroscience 13, 1292 (2019).

110. Trujillo, L. T., Stanfield, C. T. & Vela, R. D. The effect of electroencephalogram (EEG) reference choice on information-theoretic measures of the complexity and integration of EEG signals. Frontiers in neuroscience 11, 425 (2017).

111. Zheng, W.-L. & Lu, B.-L. Investigating critical frequency bands and channels for EEG-based emotion recognition with deep neural networks. IEEE Transactions on autonomous mental development 7, 162–175 (2015).

28/35

<!-- page 29 -->

112. Zheng, W.-L., Liu, W., Lu, Y., Lu, B.-L. & Cichocki, A. Emotionmeter: A multimodal framework for recognizing human emotions. IEEE transactions on cybernetics 49, 1110–1122 (2018).

113. Liu, W., Zheng, W.-L., Li, Z., Wu, S.-Y., Gan, L. & Lu, B.-L. Identifying similarities and differences in emotion recognition with EEG and eye movements among Chinese, German, and French People. Journal of Neural Engineering 19, 026012 (2022).

114. Torkamani-Azar, M., Kanik, S. D., Aydin, S. & Cetin, M. Prediction of reaction time and vigilance vari- ability from spatio-spectral features of resting-state EEG in a long sustained attention task. IEEE journal of biomedical and health informatics 24, 2550–2558 (2020).

115. Korczowski, L., Cederhout, M., Andreev, A., Cattan, G., Rodrigues, P. L. C., Gautheret, V. & Congedo, M. Brain Invaders calibration-less P300-based BCI with modulation of flash duration Dataset (bi2015a) PhD thesis (GIPSA-lab, 2019).

116. Jiang, W.-B., Zhao, L.-M., Guo, P. & Lu, B.-L. Discriminating surprise and anger from EEG and eye movements with a graph network in 2021 IEEE International Conference on Bioinformatics and Biomedicine (BIBM) (2021), 1353–1357.

117. Jiang, W.-B., Liu, X.-H., Zheng, W.-L. & Lu, B.-L. Multimodal adaptive emotion transformer with flexible modality inputs on a novel dataset with continuous labels in proceedings of the 31st ACM international conference on multimedia (2023), 5975–5984.

118. Luo, S., Lan, Y.-T., Peng, D., Li, Z., Zheng, W.-L. & Lu, B.-L. Multimodal emotion recognition in response to oil paintings in 2022 44th Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC) (2022), 4167–4170.

119. Li, R., Liu, L.-D. & Lu, B.-L. Discrimination of decision confidence levels from EEG signals in 2021 10th International IEEE/EMBS Conference on Neural Engineering (NER) (2021), 946–949.

120. Tao, L.-Y. & Lu, B.-L. Emotion recognition under sleep deprivation using a multimodal residual LSTM network in 2020 International Joint Conference on Neural Networks (IJCNN) (2020), 1–8.

121. He, Y., Luu, T. P., Nathan, K., Nakagome, S. & Contreras-Vidal, J. L. A mobile brain-body imaging dataset recorded during treadmill walking with a brain-computer interface. Scientific data 5, 1–10 (2018).

122. Brunner, C., Leeb, R., Müller-Putz, G., Schlögl, A. & Pfurtscheller, G. BCI Competition 2008–Graz data set A. Institute for knowledge discovery (laboratory of brain-computer interfaces), Graz University of Technology 16, 34 (2008).

123. Zyma, I., Tukaev, S., Seleznov, I., Kiyono, K., Popov, A., Chernykh, M. & Shpenkov, O. Electroencephalo- grams during mental arithmetic task performance. Data 4, 14 (2019).

124. Nejedly, P., Kremen, V., Sladky, V., Cimbalnik, J., Klimes, P., Plesinger, F., Mivalt, F., Travnicek, V., Viscor, I., Pail, M., et al. Multicenter intracranial EEG dataset for classification of graphoelements and artifactual signals. Scientific data 7, 179 (2020).

125. Van Den Oord, A., Vinyals, O., et al. Neural discrete representation learning. Advances in neural information processing systems 30 (2017).

126. He, K., Chen, X., Xie, S., Li, Y., Dollár, P. & Girshick, R. Masked autoencoders are scalable vision learners in Proceedings of the IEEE/CVF conference on computer vision and pattern recognition (2022), 16000–16009.

127. Kostas, D., Aroca-Ouellette, S. & Rudzicz, F. BENDR: Using transformers and a contrastive self-supervised learning task to learn from massive amounts of EEG data. Frontiers in Human Neuroscience 15, 653659 (2021).

128. Oikonomou, V. P., Georgiadis, K., Liaros, G., Nikolopoulos, S. & Kompatsiaris, I. A comparison study on EEG signal processing techniques using motor imagery EEG data in 2017 IEEE 30th international symposium on computer-based medical systems (CBMS) (2017), 781–786.

29/35

<!-- page 30 -->

129. Schirrmeister, R. T., Springenberg, J. T., Fiederer, L. D. J., Glasstetter, M., Eggensperger, K., Tangermann, M., Hutter, F., Burgard, W. & Ball, T. Deep learning with convolutional neural networks for EEG decoding and visualization. Human brain mapping 38, 5391–5420 (2017).

130. Amin, S. U., Alsulaiman, M., Muhammad, G., Mekhtiche, M. A. & Hossain, M. S. Deep Learning for EEG motor imagery classification based on multi-layer CNNs feature fusion. Future Generation computer systems 101, 542–554 (2019).

131. Zhang, D., Chen, K., Jian, D. & Yao, L. Motor imagery classification via temporal attention cues of graph embedded EEG signals. IEEE journal of biomedical and health informatics 24, 2570–2579 (2020).

132. Potter, I. Y., Zerveas, G., Eickhoff, C. & Duncan, D. Unsupervised multivariate time-series transformers for seizure identification on eeg in 2022 21st IEEE International Conference on Machine Learning and Applications (ICMLA) (2022), 1304–1311.

133. Woo, G., Liu, C., Sahoo, D., Kumar, A. & Hoi, S. Cost: Contrastive learning of disentangled seasonal-trend representations for time series forecasting. arXiv preprint arXiv:2202.01575 (2022).

134. Zhang, X., Zhao, Z., Tsiligkaridis, T. & Zitnik, M. Self-supervised contrastive pre-training for time series via time-frequency consistency. Advances in neural information processing systems 35, 3988–4003 (2022).

135. Nie, Y., Nguyen, N. H., Sinthong, P. & Kalagnanam, J. A Time Series Is Worth 64 Words: Long-term Forecasting with Transformers Mar. 2023. arXiv: 2211.14730 [cs]. (2025).

136. Eldele, E., Ragab, M., Chen, Z., Wu, M., Kwoh, C. K., Li, X. & Guan, C. Time-series representation learning via temporal and contextual contrasting. arXiv preprint arXiv:2106.14112 (2021).

137. Zhang, Z. & Parhi, K. K. Low-complexity seizure prediction from iEEG/sEEG using spectral power and ratios of spectral power. IEEE transactions on biomedical circuits and systems 10, 693–706 (2015).

138. Handa, P. & Goel, N. Epileptic seizure detection using rhythmicity spectrogram and cross-patient test set in 2021 8th international conference on signal processing and integrated networks (SPIN) (2021), 898–902.

139. Kadivar, M., Moghadam, E. M., Shervin Badv, R., Sangsari, R. & Saeedy, M. A comparison of conventional electroencephalography with amplitude-integrated EEG in detection of neonatal seizures. Medical Devices: Evidence and Research, 489–496 (2019).

140. Wang, Y., Yang, Y., Cao, G., Guo, J., Wei, P., Feng, T., Dai, Y., Huang, J., Kang, G. & Zhao, G. SEEG-Net: An explainable and deep learning-based cross-subject pathological activity detection method for drug-resistant epilepsy. Computers in Biology and Medicine 148, 105703 (2022).

141. Jing, J., Ge, W., Hong, S., Fernandes, M. B., Lin, Z., Yang, C., An, S., Struck, A. F., Herlopian, A., Karakis, I., et al. Development of expert-level classification of seizures and rhythmic and periodic patterns during EEG interpretation. Neurology 100, e1750–e1762 (2023).

142. Yang, C., Xiao, D., Westover, M. B. & Sun, J. Self-supervised EEG representation learning for automatic sleep staging. arXiv preprint arXiv:2110.15278 (2021).

143. Peh, W. Y., Yao, Y. & Dauwels, J. Transformer convolutional neural networks for automated artifact detection in scalp EEG in 2022 44th Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC) (2022), 3599–3602.

144. Li, H., Ding, M., Zhang, R. & Xiu, C. Motor imagery EEG classification algorithm based on CNN-LSTM feature fusion network. Biomedical signal processing and control 72, 103342 (2022).

145. Song, Y., Jia, X., Yang, L. & Xie, L. Transformer-based spatial-temporal feature learning for EEG decoding. arXiv preprint arXiv:2106.11170 (2021).

146. Bai, S., Kolter, J. Z. & Koltun, V. An empirical evaluation of generic convolutional and recurrent networks for sequence modeling. arXiv preprint arXiv:1803.01271 (2018).

30/35

<!-- page 31 -->

147. Tang, S., Dunnmon, J. A., Saab, K., Zhang, X., Huang, Q., Dubost, F., Rubin, D. L. & Lee-Messer, C. Self-supervised graph neural networks for improved electroencephalographic seizure analysis. arXiv preprint arXiv:2104.08336 (2021).

148. Tang, S., Dunnmon, J. A., Liangqiong, Q., Saab, K. K., Baykaner, T., Lee-Messer, C. & Rubin, D. L. Modeling multivariate biosignals with graph neural networks and structured state space models in Conference on health, inference, and learning (2023), 50–71.

149. Hochreiter, S. & Schmidhuber, J. Long short-term memory. Neural computation 9, 1735–1780 (1997).

150. Liu, Z., Mao, H., Wu, C.-Y., Feichtenhofer, C., Darrell, T. & Xie, S. A convnet for the 2020s in Proceedings of the IEEE/CVF conference on computer vision and pattern recognition (2022), 11976–11986.

151. Goswami, M., Szafer, K., Choudhry, A., Cai, Y., Li, S. & Dubrawski, A. Moment: A family of open time-series foundation models. arXiv preprint arXiv:2402.03885 (2024).

152. Wu, H., Hu, T., Liu, Y., Zhou, H., Wang, J. & Long, M. Timesnet: Temporal 2d-variation modeling for general time series analysis. arXiv preprint arXiv:2210.02186 (2022).

153. Nie, Y., Nguyen, N. H., Sinthong, P. & Kalagnanam, J. A time series is worth 64 words: Long-term forecasting with transformers. arXiv preprint arXiv:2211.14730 (2022).

154. Mivalt, F., Kremen, V., Sladky, V., Cui, J., Gregg, N. M., Balzekas, I., Marks, V., St Louis, E. K., Croarkin, P., Lundstrom, B. N., et al. Impedance rhythms in human limbic system. Journal of Neuroscience 43, 6653–6666 (2023).

155. Kiessner, A.-K., Schirrmeister, R. T., Boedecker, J. & Ball, T. Reaching the ceiling? Empirical scaling behaviour for deep EEG pathology classification. Computers in Biology and Medicine 178, 108681 (2024).

156. Klonowski, W. Everything you wanted to ask about EEG but were afraid to get the right answer. Nonlinear biomedical physics 3, 1–5 (2009).

157. Donoghue, T., Haller, M., Peterson, E. J., Varma, P., Sebastian, P., Gao, R., Noto, T., Lara, A. H., Wallis, J. D., Knight, R. T., et al. Parameterizing neural power spectra into periodic and aperiodic components. Nature neuroscience 23, 1655–1665 (2020).

158. Peng, Z., Dong, L., Bao, H., Ye, Q. & Wei, F. Beit v2: Masked image modeling with vector-quantized visual tokenizers. arXiv preprint arXiv:2208.06366 (2022).

159. Wang, Y., Wu, H., Dong, J., Liu, Y., Long, M. & Wang, J. Deep time series models: A comprehensive survey and benchmark. arXiv preprint arXiv:2407.13278 (2024).

160. Wan, Z., Yu, Q., Mao, J., Duan, W. & Ding, C. Openecg: Benchmarking ecg foundation models with public 1.2 million records. arXiv preprint arXiv:2503.00711 (2025).

161. Arora, S., Pasad, A., Chien, C.-M., Han, J., Sharma, R., Jung, J.-w., Dhamyal, H., Chen, W., Shon, S., Lee, H.-y., et al. On the evaluation of speech foundation models for spoken language understanding. arXiv preprint arXiv:2406.10083 (2024).

162. Wei, X., Faisal, A. A., Grosse-Wentrup, M., Gramfort, A., Chevallier, S., Jayaram, V., Jeunet, C., Bakas, S., Ludwig, S., Barmpas, K., et al. 2021 BEETL competition: Advancing transfer learning for subject independence and heterogenous EEG data sets in NeurIPS 2021 Competitions and Demonstrations Track (2022), 205–219.

163. Jing, J., Lin, Z., Yang, C., Chow, A., Dane, S., Sun, J. & Westover, M. B. HMS - Harmful Brain Activity Classification https://kaggle.com/competitions/hms-harmful-brain-activity- classification. Kaggle. 2024.

164. Reyna, M. A., Amorim, E., Sameni, R., Weigle, J., Elola, A., Rad, A. B., Seyedi, S., Kwon, H., Zheng, W.-L., Ghassemi, M. M., et al. Predicting neurological recovery from coma after cardiac arrest: The George B. Moody PhysioNet Challenge 2023 in 2023 Computing in Cardiology (CinC) 50 (2023), 1–4.

31/35

<!-- page 32 -->

165. Dan, J., Pale, U., Amirshahi, A., Cappelletti, W., Ingolfsson, T. M., Wang, X., Cossettini, A., Bernini, A., Benini, L., Beniczky, S., et al. SzCORE: Seizure Community Open-Source Research Evaluation framework for the validation of electroencephalography-based automated seizure detection algorithms. Epilepsia (2024).

166. Brinkmann, B. H., Wagenaar, J., Abbot, D., Adkins, P., Bosshard, S. C., Chen, M., Tieng, Q. M., He, J., Muñoz-Almaraz, F., Botella-Rocamora, P., et al. Crowdsourcing reproducible seizure forecasting in human and canine epilepsy. Brain 139, 1713–1722 (2016).

167. Gramfort, A., Luessi, M., Larson, E., Engemann, D. A., Strohmeier, D., Brodbeck, C., Goj, R., Jas, M., Brooks, T., Parkkonen, L., et al. MEG and EEG data analysis with MNE-Python. Frontiers in Neuroinformatics 7, 267 (2013).

168. Schirrmeister, R. T., Springenberg, J. T., Fiederer, L. D. J., Glasstetter, M., Eggensperger, K., Tangermann, M., Hutter, F., Burgard, W. & Ball, T. Deep learning with convolutional neural networks for EEG decoding and visualization. Human Brain Mapping. ISSN: 1097-0193. http://dx.doi.org/10.1002/hbm.23730 (Aug. 2017).

169. Schiratti, J.-B., Le Douget, J.-E., Le Van Quyen, M., Essid, S. & Gramfort, A. An ensemble learning approach to detect epileptic seizures from long intracranial EEG recordings in 2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (2018), 856–860.

170. McMahan, B., Moore, E., Ramage, D., Hampson, S. & y Arcas, B. A. Communication-efficient learning of deep networks from decentralized data in Artificial intelligence and statistics (2017), 1273–1282.

171. Tatum IV, W. O., Selioutski, O., Ochoa, J. G., Clary, H. M., Cheek, J., Drislane, F. W. & Tsuchida, T. N. American clinical neurophysiology society guideline 7: guidelines for EEG reporting. The Neurodiagnostic Journal 56, 285–293 (2016).

172. Hinton, G., Vinyals, O. & Dean, J. Distilling the knowledge in a neural network. arXiv preprint arXiv:1503.02531 (2015).

173. Han, S., Mao, H. & Dally, W. J. Deep compression: Compressing deep neural networks with pruning, trained quantization and huffman coding. arXiv preprint arXiv:1510.00149 (2015).

174. Gong, Y., Liu, L., Yang, M. & Bourdev, L. Compressing deep convolutional networks using vector quantiza- tion. arXiv preprint arXiv:1412.6115 (2014).

175. Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I. D. & Gebru, T. Model cards for model reporting in Proceedings of the conference on fairness, accountability, and transparency (2019), 220–229.

176. Hsu, W.-N., Bolte, B., Tsai, Y.-H. H., Lakhotia, K., Salakhutdinov, R. & Mohamed, A. Hubert: Self-supervised speech representation learning by masked prediction of hidden units. IEEE/ACM transactions on audio, speech, and language processing 29, 3451–3460 (2021).

32/35

<!-- page 33 -->

## Supplement

Sleep Foundation Models Our literature search yielded two sleep FMs that were excluded from the main review scope. Below, we summarize their salient aspects for interested readers. SleepFM [65]: Data. SleepFM is a large-scale multi-modal sleep foundation model trained on over 100,000 hours of polysomnography data from 14,000 participants. The modalities include brain activity (EEG), eye activity (EOG), muscle tone (EMG), cardiac signals (EKG), and respiratory signals. The data are minimally preprocessed and segmented into 30-second clips aligned with expert annotation boundaries. Modeling. SleepFM uses three modality-specific 1D EfficientNet-based encoders. The model is pretrained with both pairwise contrastive learning and a novel leave-one-out contrastive strategy that aligns each modality with the joint representation of the others. SleepFM supports flexible inference, allowing downstream classifiers to use any subset of the input modalities. Evaluation. The resulting embeddings are evaluated through cross-modal retrieval, demographic prediction, and sleep-related classifications, including sleep staging and sleep disordered breathing detection. Results show that SleepFM consistently outperforms supervised convolutional baselines. Ablations demonstrate that multi-modal pretraining that includes EEG is superior to single-modality pretraining. Additionally, SleepFM demonstrated strong out-of-distribution generalization to an unseen site with a different channel configuration. Self-Supervised Transformer Model Training for a Sleep-EEG Foundation Model [66]: Data. The model is pretrained on 10,897 sleep sessions from 9,013 individuals sourced from multiple public datasets. A single central EEG channel (C3/C4) is resampled to 100 Hz, normalized, clipped, and segmented into 30-second epochs. Sequences of 101 epochs with 25% overlap are constructed for subsequent modeling. Modeling. Unsupervised k-means clustering (300 clusters) on spectrogram features provides pseudo-labels for self-supervision. The approach follows a HuBERT [176]-style masked prediction framework, where the model learns to infer hidden k-means label sequences. The architecture consists of a 7-layer 1D convolutional encoder, a projection layer, positional encoding, and a 4-layer transformer encoder (28.5M parameters). Masking is applied in 10 epoch blocks, and the model is trained for 40 epochs. Evaluation. After pretraining, the model is adapted for the tasks of sleep staging, subject identification, and age prediction. The pretrained model achieves strong representation learning and rapid convergence, outperforming supervised baselines in low-label sleep staging. Experiments with frozen embeddings, i.e., linear probing, suggest that the model can generalize across montages and tasks. Additionally, the masking and k-means-based pseudo-labeling process were shown to support generalization to the external Sleep-EDF dataset.

33/35

<!-- page 34 -->

Table 1. Pretraining data volume. Channel-hours were used to represent and compare the data scale at which the EEG foundation models were pretrained. In most cases, channel-hours per dataset were calculated as the product of the number of channels and the recording durations (in hours) obtained from the original studies. Scalp EEG datasets had a fixed channel count across subjects, whereas intracranial EEG datasets used in BrainBERT and Brant had a subject-specific channel count. For Neuro-GPT and EEGFormer, channel-hours were computed from publicly available dataset statistics and were assumed to be applicable to both studies. For BrainBERT, we used the channel-hours reported by the authors. For BrainWave, the total patch count reported was used to calculate the channel-hours by converting the patch size (1 second) to hours. Channel-hours pooled across all pretraining data sources are highlighted in bold. N/A represents cases where channel-hours could not be determined.

EEG-FM Pretraining Dataset Number of Chan-

nels

Total Length of

Recordings

(Hours)

Channel-Hours (= Number of Channels × Recording Length)

Total Channel-Hours

BrainBERT Brain TreeBank [70] - - 4,551 4,551 Neuro-GPT TUEG [72] 20 27,063 541,260 541,260 Brant Private dataset (unknown source) - - (124×235.34)+ (52×82.39)+ (120×393.09)+ (133×137.45)+ (116×214.22)+ (101×386.70) +

(67×111.55) + (47×207.42)+ (134×759.80)

281,860.10

BIOT SHHS [80, 87] 2 42,446 84,892 PREST 16 14,197 227,152 312,044 EEGFormer TUEG 20 27,063 541,260 541,260 LaBraM BCI Competition IV-1 [104] 59 8.21 484.39 Emobrain [105] 64 4.94 316.16 Grasp/Lift EEG Challenge [106] 32 11.72 375.04 Inria BCI Challenge [107] 56 29.98 1,678.88 EEG Motor Imagery Dataset [108] 64 47.3 3,027.2 Visual Categorization EEG Data [109]

64 34.35 2,198.4

Resting State EEG Data [110] 64 3.04 194.56 SEED Series [111–113] 62 166.75 10,338.5 Siena Scalp EEG Database [86] 31 30.47 944.57 SPIS Resting State Dataset [114] 64 0.83 53.12 Brain-Invaders [115] 32 16 512 TUAR [72] 23 92.22 2,121.06 TUEP [72] 21 591.22 12,415.62 TUSZ [72] 21 1,138.53 23,909.13 TUSL [72] 23 20.59 473.57 Multiple data sources [116–120] 62 342.23 21,218.26 80,260.46 Mentality TUSZ N/A N/A N/A N/A NeuroLM TUEG 21 24,000 504,000 SEED Series 62 170.54 10,573.48 BCI Competition IV-1 59 8.21 484.39 Emobrain 64 4.94 316.16 Grasp/Lift EEG Challenge 32 11.72 375.04 Inria BCI Challenge 56 29.98 1,678.88 Motor Movement/Imagery Dataset 64 47.3 3,027.2 Raw EEG Data 64 34.35 2,198.4 Resting State EEG Data 64 3.04 194.56 Siena Scalp EEG Database 31 30.47 944.57 SPIS Resting State Dataset 64 0.83 53.12 Brain-Invaders 32 16 512 Multiple data sources [116–120] 62 342.23 21,218.26 545,576.06 FoME Multiple datasets N/A N/A N/A N/A BrainWave Multiple datasets - - 3,162,233,694×(1÷3,600) 878,398.25

34/35

<!-- page 35 -->

Table 2. EEG foundation model evaluation strategies. Various techniques were used to evaluate EEG foundation models: a) zero-shot transfer learning (ZSTL, in blue) with prior task knowledge but no access to data and labels from the target setting; b) few-shot learning (FSL, in green) with no prior task knowledge but access to a few labels from the target setting; c) linear probing (LP, in pink) where a classifier head is adapted using labels from the target setting; and d) fine-tuning (FT, in yellow) where the backbone and head together are adapted using labels from the target setting. Evaluation scores estimated based on the graphics in the paper are denoted using superscript ∗.

In-Distribution Out-of-Distribution

EEG-FM Task LP FT FSL ZSTL LP FT

BrainBERT Brain TreeBank AUC - 0.59 AUC - 0.83

Neuro-GPT BCI Competition IV Dataset 2a Acc. - 44.3 Acc. - 64.5

Brant

Private (Pathology Detection) Acc. - 91.17

MAYO (Pathology Detection) Acc. - 89.40

FNUSA (Pathology Detection) Acc. - 83.51

BIOT

TUAB AUC - 0.8815 AUC - 0.8739

TUEV W.F1 - 0.7504 W. F1 - 0.7322

CHB-MIT AUC - 0.8761 AUC - 0.8752

IIIC Seizure W. F1 - 0.5737 W. F1 - 0.5878

EEGFormer

TUAB AUC - 0.876

TUAR AUC - 0.827 AUC - 0.852

TUSL AUC - 0.657 AUC - 0.679

TUSZ AUC - 0.883

Neonate Dataset AUC - 0.842

LaBraM

TUAB AUC - 0.8835 AUC - 0.9162

TUEV B.Acc - 34.61 B.Acc - 66.16

SEED Series Acc. - 41.02

MoBI RMSE - 0.1196

Mentality TUSZ AUC - 0.72

NeuroLM

TUAB AUC - 0.7884

TUEV B.Acc - 0.4679

TUSL B.Acc - 0.6845

HMC B.Acc - 0.6188

SEED Series B.Acc - 0.6034

Workload B.Acc - 0.6345

FoME

TUEV F1 - 46.00∗ F1 - 79.00

Sleep-EDFx F1 - 99.10

SEED Series F1 - 57.89

MAYO (Events Classification) F1 - 78.80 F1 - 87.78

MAYO (Pathology Detection) F1 - 95.13

FNUSA (Events Classification) F1 - 77.44 F1 - 85.44

FNUSA (Pathology Detection) F1 - 91.81

BrainWave

CHB-MIT AUC - 0.90∗

Clonic-6 AUC - 0.79∗

Atonic-5 AUC - 0.77∗

Absence-16 AUC - 0.90∗ AUC - 0.96∗

DRE-Clinical AUC - 0.75∗ AUC - 0.85∗

SD-71 AUC - 0.63∗ AUC - 0.70∗

ADHD-Adult AUC - 0.90∗ AUC - 0.96∗

ADHD-Child AUC - 0.77∗ AUC - 0.80∗

Schizophrenia-28 AUC - 0.72∗ AUC - 0.88∗

Depression-122 AUC - 0.75∗ AUC - 0.78∗

MDD-64 AUC - 0.90∗ AUC - 0.92∗

AD-65 AUC - 0.63∗ AUC - 0.76∗

MAYO (Events Classification) AUC - 0.81∗ AUC - 0.93∗ AUC - 0.97∗

FNUSA (Events Classification) AUC - 0.78∗ AUC - 0.91∗ AUC - 0.91∗

35/35
## Tables transcribed from page images (p. 35)

Supplementary Table 2, column alignment checked against the page image. Columns: in-distribution LP | FT; out-of-distribution FSL | ZSTL | LP | FT. `*` = estimated from figures.
- BrainBERT, Brain TreeBank: ID LP AUC 0.59 | ID FT AUC 0.83
- Neuro-GPT, BCI IV-2a: OOD LP Acc 44.3 | OOD FT Acc 64.5
- Brant: Private pathology OOD FT Acc 91.17; MAYO pathology ZSTL Acc 89.40; FNUSA pathology ZSTL Acc 83.51
- BIOT: TUAB ID FT AUC 0.8815 / OOD FT 0.8739; TUEV ID FT W.F1 0.7504 / OOD FT 0.7322; CHB-MIT ID FT AUC 0.8761 / OOD FT 0.8752; IIIC ID FT W.F1 0.5737 / OOD FT 0.5878
- EEGFormer: TUAB ID FT AUC 0.876; TUAR ID LP 0.827 / FT 0.852; TUSL ID LP 0.657 / FT 0.679; TUSZ ID FT 0.883; Neonate OOD FT 0.842
- LaBraM: TUAB ID LP AUC 0.8835 / FT 0.9162; TUEV ID LP B.Acc 34.61 / FT 66.16; SEED ID FT Acc 41.02; MoBI OOD FT RMSE 0.1196
- Mentality: TUSZ ID FT AUC 0.72
- NeuroLM: TUAB ID FT AUC 0.7884; TUEV ID FT B.Acc 0.4679; TUSL ID FT 0.6845; HMC OOD FT 0.6188; SEED ID FT 0.6034; Workload OOD FT 0.6345
- FoME: TUEV ID LP F1 46.00* / FT 79.00; Sleep-EDFx ID FT 99.10; SEED ID FT 57.89; MAYO events ID LP 78.80 / FT 87.78; MAYO pathology ID FT 95.13; FNUSA events ID LP 77.44 / FT 85.44; FNUSA pathology ID FT 91.81
- BrainWave (all `*`): CHB-MIT OOD FT 0.90; Clonic-6 ZSTL 0.79; Atonic-5 ZSTL 0.77; Absence-16 FSL 0.90 / FT 0.96; DRE-Clinical FSL 0.75 / FT 0.85; SD-71 FSL 0.63 / FT 0.70; ADHD-Adult FSL 0.90 / FT 0.96; ADHD-Child FSL 0.77 / FT 0.80; Schizophrenia-28 FSL 0.72 / FT 0.88; Depression-122 FSL 0.75 / FT 0.78; MDD-64 FSL 0.90 / FT 0.92; AD-65 FSL 0.63 / FT 0.76; MAYO events FSL 0.81 / ZSTL 0.93 / FT 0.97; FNUSA events FSL 0.78 / ZSTL 0.91 / FT 0.91
