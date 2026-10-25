<!-- source: pdf/poziomska2025quantity.pdf | converter: pymupdf -->

<!-- page 1 -->

## Quantity versus Diversity: Influence of Data on Detecting EEG Pathology

## with Advanced ML Models

Martyna Poziomskad,a, Marian Dovgialoa,b, Przemysław Olbratowskia,e, Paweł Niedbalskic, Paweł Ogniewskic, Joanna Zychc,

Jacek Rogalaa, Jarosław ˙Zygierewicza,∗

aFaculty of Physics, University of Warsaw, Pasteura 5, 02-093, Warsaw, Poland bNencki Institute of Experimental Biology, Polish Academy of Sciences, Pasteura 3, 02-093, Warsaw, Poland

cElmiko Biosignals sp. z o.o., Sportowa 3, 05-822, Milanówek, Poland dAutomotive Industry Institute, Łukasiewicz Research Network, Jagiello´nska 55, 03-301, Warsaw, Poland

eWIT Academy, Newelska 6, 01-447, Warsaw, Poland

Abstract

This study investigates the impact of quantity and diversity of data on the performance of various machine-learning models for detecting general EEG pathology. We utilized an EEG dataset of 2,993 recordings from Temple University Hospital and a dataset of 55,787 recordings from Elmiko Biosignals sp. z o.o. The latter contains data from 39 hospitals and a diverse patient set with varied conditions. Thus, we introduce the Elmiko dataset – the largest publicly available EEG corpus. Our findings show that small and consistent datasets enable a wide range of models to achieve high accuracy; however, variations in pathological conditions, recording protocols, and labeling standards lead to significant performance degradation. Nonetheless, increasing the number of available recordings improves predictive accuracy and may even compensate for data diversity, particularly in neural networks based on attention mechanism or transformer architecture. A meta-model that combined these networks with a gradient-boosting approach using handcrafted features demonstrated superior performance across varied datasets.

Keywords: EEG, pathology detection, ensemble models, neural networks, data heterogeneity, scaling laws

1. Introduction

Applications of machine learning (ML) in medical diagnos- tics are developing rapidly and offer innovative solutions for exploring complex biomedical data. Electroencephalography (EEG), which non-invasively records brain activity, is crucial for diagnosing neurological conditions such as epilepsy (Yang et al., 2022). However, it presents significant challenges for automatic analysis due to its non-linear, non-stationary, and chaotic nature (Klonowski et al., 2002). The agreement among human EEG raters is moderate and fluctuates across various neurological disorders (Ahrens et al., 2021; Halford et al., 2015; Nascimento et al., 2024), complicating the task further.

Nevertheless, several ML architectures have been proposed to address challenges, such as detecting epileptic seizures or classification of EEG recordings as normal or pathological. The present paper focuses on the latter application, commonly re- ferred to as neuro-screening. Previous research on ML models for general pathology detection includes studies by Lopez de Diego (2017), Schirrmeister et al. (2017), Roy et al. (2019),

∗Corresponding author

Email addresses: martyna.poziomska@fuw.edu.pl (Martyna Poziomska), marian.dovgialo@fuw.edu.pl (Marian Dovgialo), p.olbratowsk@uw.edu.pl (Przemysław Olbratowski), pawel.niedbalski@elmiko.pl (Paweł Niedbalski), po_notice@elmiko.pl (Paweł Ogniewski), joanna.zych@elmiko.pl (Joanna Zych), jacek.rogala@fuw.edu.pl (Jacek Rogala), jaroslaw.zygierewicz@fuw.edu.pl (Jarosław ˙Zygierewicz)

Van Leeuwen et al. (2019), Gemein et al. (2020), Western et al. (2021), Khan et al. (2022), Wilson et al. (2022), Kiessner et al. (2023), and Kiessner et al. (2024). Review articles by Faust et al. (2018), Miotto et al. (2018), Craik et al. (2019), Roy et al. (2019), Merlin Praveena et al. (2022), and Tibermacine et al. (2024) provide further insights. The proposed architectures in- clude classical methods such as random forest classifiers, sup- port vector machines, Riemannian geometry, and deep neural networks.

ML models generally perform well with homogeneous data. For example, the Temple University Hospital (TUH) corpus has become the de facto benchmark in the field. It comprises approximately 3,000 labeled clinical recordings, making it the largest publicly available dataset for detecting EEG pathology to date. All recordings originate from a single institution and were labeled by a dedicated team of clinicians who exhibited a high inter-rater agreement. With over 87% of the abnormal recordings indicating epilepsy (Obeid and Picone, 2016), the classification task primarily focuses on distinguishing epilepsy from normal EEG patterns.

Despite demonstrating high accuracy with minimal electrode use (Yıldırım et al., 2020) and achieving 87.7% accuracy in recent studies utilizing wavelet feature extraction or gradient boosting (Albaqami et al., 2021), models have not achieved sig- nificantly better results on this seemingly straightforward task. Kiessner et al. (2024) note that predictive accuracy tends to plateau at around 87%, attributing this limitation to the inherent

November 28, 2024

# arXiv:2411.17709v1  [eess.SP]  13 Nov 2024

<!-- page 2 -->

Figure 1: Age, sex, and diagnosis distributions in the TUH and ELM19 databases.

noise in clinical labeling. They also indicate that although ex- panding the amount of data can enhance model capabilities, the benefits are not uniform across all model architectures. Simpler models may experience a plateau in accuracy as data volume increases, whereas more complex models, particularly neural networks with residual blocks, continue to improve.

Efforts to automatically detect EEG abnormalities have mostly focused on training ML models using signals from a sin- gle hospital, with TUH being a prominent example. Although a resulting model may achieve remarkably high accuracy for that particular hospital, its generalizability to other institutions is of- ten poor. A similar effect has been reported by Ayodele et al. (2020) in the context of automatic detection of EEG seizures. Data from one institution may be biased regarding patient con- ditions, and the corresponding model can fail even when the same institution admits less typical patients. A change in EEG hardware or the introduction of new technicians is also likely to invalidate the current model. Finally, a single hospital may not provide enough recordings for reliable training.

The need to incorporate data from multiple sources has been widely recognized in other medical domains. Examples include predicting the risk of mortality in cardiac surgery (Roques et al., 1999), the risk of intracranial aneurysm rupture (Greving et al., 2014), the risk of coronary artery disease (Aerts et al., 2017), and the risk of major bleeding in patients with noncardioem- bolic stroke (Hilkens et al., 2017). Training on data from mul- tiple institutions is often referred to as multi-cohort learning. Schinkel et al. (2023) embrace the intuitive idea that training on multiple cohorts yields models that better generalize to new cases from hospitals not included in the training set.

However, multi-cohort learning comes with its own difficul- ties. Clinical data from different hospitals can be heterogeneous or diverse in terms of patient conditions, recording protocols, and labeling standards (Tayebi Arasteh et al., 2023). Such data occupy different regions of the feature space and intro- duce greater labeling noise, which can significantly deteriorate model performance, even for hospitals included in the train- ing set. In a recent study of phenotype predictions, Gao and Sun (2023) observed a decline in accuracy across all consid-

ered statistical methods as population heterogeneity increased. There is certainly a trade-off between pros and cons. Neverthe- less, attempts to develop an approach applicable to virtually all EEG recordings are undoubtedly worth the effort for scientific purposes, for the benefit of patients, and also for commercial reasons.

Given these observations, the present study investigates the performance of simple and advanced ML models on EEG data of varying volumes and diversity. We use the relatively small, homogeneous TUH dataset and a large, heterogeneous dataset provided by Elmiko Biosignals sp. z o.o., a Polish manufac- turer of EEG hardware and software. The latter dataset includes recordings from multiple hospitals, evaluated by many indepen- dent experts, and reflects diverse patient conditions. Our mod- els include both non-neural approaches that utilize handcrafted features and neural networks that extract features directly from the raw EEG signal. Some of these networks use the atten- tion mechanism or the transformer architecture. By examining how different models respond to variations in data quantity and heterogeneity, we aim to identify the most effective approaches for developing robust EEG classifiers capable of generalizing across diverse clinical settings and patient conditions.

Our findings contribute to the broader discussion on the role of data diversity in ML, particularly within the medical field. The insights gained from this study are expected to inform the design of future ML architectures and guide the collection of medical datasets, ultimately advancing the development of more reliable and generalizable diagnostic tools.

2. Data

In the current study, we contrast two distinct sources of data. The first is the publicly available TUH Abnormal EEG Cor- pus version 2.0.0, which is part of a larger database (Lopez de Diego, 2017). It contains 2,993 recordings, of which 1,595 (53.3%) are from females. A total of 1,472 recordings (49.2%) are suggestive of pathology, with the vast majority (87%) classi- fied as epileptic. The remaining 1,521 recordings are classified as normal. Patient ages range from 0 to over 90 years. We refer

2

<!-- page 3 -->

Table 1: Descriptive statistics of the datasets. TUH SZC ELM1 ELM2 ELM4 ELM8 ELM19

Recordings 2,993 2,993 2,993 5,986 11,972 23,944 55,787 Females 1,595 1,533 1,630 3,205 6,334 12,675 29,525 53% 51% 54% 54% 53% 53% 53% Pathological 1,472 1,497 1,561 3,119 6,238 12,479 29,074 cases 49% 50% 52% 52% 52% 52% 52%

to this database as TUH. The age, sex, and pathology distribu- tions in TUH are depicted in Fig. 1.

The second database was collected by Elmiko Biosignals sp. z o.o.1 and originally contained over 80,000 recordings, each accompanied by a description in Polish. This description in- cludes the final diagnosis based on signal examination by an EEG expert. We manually reviewed all descriptions and ex- cluded cases where the diagnosis was missing or inconclusive. Specifically, we discarded descriptions indicating the absence of epileptic abnormalities without commenting on other possi- ble disorders, as well as those emphasizing that the observed abnormalities were weak (Benbadis, 2010). Recordings with descriptions citing significant or abundant artifacts were also excluded. We retained only those recordings that unequivocally reported the presence or absence of abnormalities or explicitly stated that the signal was normal, labeling them accordingly as pathological or normal.

After additional exclusions due to the preprocessing de- scribed in Section 3.1, the database contains 55,787 record- ings, of which 29,525 (52.9%) are from females. Patient ages vary from 16 to 70. A total of 29,074 recordings (52.2%) are described by clinicians as indicative of pathology. Among these, only about 26% are recognized as epileptic or exhibiting seizures. The remaining 26,713 recordings are identified as nor- mal. Importantly for this study, the data were collected from 39 different hospitals, making it strongly heterogeneous in terms of recording procedures and labeling standards. This database will be referred to as ELM19 because it is roughly 19 times the size of TUH. The age, sex, and pathology distributions in the ELM19 database are shown in Fig. 1. Note that ELM19 and TUH have similar proportions of sex and pathology.

We also examine several subsets of the ELM19 database. The first subset, named SZC, is designed to closely match the TUH database in terms of size, the proportion of female participants, and the ratio of normal to pathological recordings. Notably, it originates from a single hospital, making it significantly more homogeneous compared to the entire ELM19 database, while still covering a broader range of pathological conditions than TUH. The next five subsets are stratified based on hospital, sex, and pathology, differing only in size. They are labeled ELM1, ELM2, ELM4, ELM8, and ELM19, with the subscript indicat- ing how many times each subset is larger than TUH. The last subset is the full ELM19 database, which is 18.64 times the size of TUH. Table 1 provides descriptive statistics for all datasets.

1https://www.elmiko.pl

While we use TUH and the complete ELM19 to examine the ef- fects of heterogeneity, the different ELM19 subsets enable us to assess the impact of varying data sizes.

EEG signals in both databases were recorded using the stan- dard 10-20 system with 19 channels denoted as follows: Fp1, Fp2, F7, F3, Fz, F4, F8, T3, C3, Cz, C4, T4, T5, P3, Pz, P4, T6, O1, and O2. They were initially sampled at various frequencies ranging from 200 to 500 Hz. The TUH and ELM19 signals were recorded in the United States and Europe, where the power-line frequency is 60 and 50 Hz, respectively.

While the homogeneous TUH data have been openly avail- able for several years, we are now sharing the heterogeneous ELM19 database for research purposes, making it the largest publicly accessible EEG corpus for pathology detection. Please refer to the data availability declaration at the end for de- tails. The recordings in both databases are originally stored as separate files in the European Data Format2 (EDF) (Kemp et al., 1992), which can be easily read using, e.g., open-access Python libraries.

3. Methods

3.1. Preprocessing We preprocessed raw signals from both databases using the MNE3 package for EEG analysis (Gramfort et al., 2013). To re- move power-line noise, a notch filter with quality factor Q = 5 and frequencies of 60 and 50 Hz was applied for the TUH and ELM19 databases, respectively. Butterworth filters were then used to eliminate frequencies often contaminated by slow drift and muscle artifacts. We applied a high-pass filter with a cutoff at 0.1 Hz and less than 1 dB passband ripple above 0.5 Hz, and a low-pass filter with a cutoff at 40 Hz, providing at least 20 dB attenuation above 50 Hz, and less than 1 dB passband ripple. All signals were then resampled to 100 Hz and re-referenced to a common average reference.

Following Gemein et al. (2020), signals were split into adja- cent 6-second frames, each containing 600 EEG samples. We checked that slicing frames of 10 or 20 seconds did not improve the results further. Frames containing flat-line channels or volt- ages exceeding 800 µV were discarded as artifacts. Recordings with fewer than 50 valid frames remaining after artifact removal were excluded from further analysis. Although the same proce- dure was applied to both databases, it did not reject any record- ings from TUH. Note that all the numbers given in Section 2

2https://www.edfplus.info 3https://mne.tools

3

<!-- page 4 -->

Figure 2: Distribution of recording lengths in the TUH and ELM19 databases after data preprocessing. The length is expressed as the number of 6-second frames.

pertain to recordings remaining after all the described exclu- sions and that were indeed involved in the training and testing of our ML models. Fig. 2 shows the resulting distributions of the recording lengths in both datasets. The histograms highlight the greater diversity of ELM19 in this respect as well.

To comply with the aggregation methods used by some of our models (see Section 3.3.2), we label normal recordings as 1 and pathological recordings as 0, contrary to the convention com- monly adopted in medicine. Consequently, our models techni- cally output the probability of normality rather than pathology. Because these two quantities are trivially related, we sometimes refer to the models as returning the probability of pathology, which may be more appealing to the reader.

3.2. Feature extraction We study a variety of neural networks alongside a group of non-neural models, referred to as classical models. The neural networks take the preprocessed signal frames directly and auto- matically extract features useful for detecting EEG pathology. In contrast, the classical models rely on handcrafted features based on time and frequency.

Time-domain covariance matrices between EEG channels form a Riemannian manifold and their projections onto the tan- gent space carry valuable information about the EEG signal (Congedo et al., 2013; Tibermacine et al., 2024). For every 6-second frame, we calculate the covariance matrix, average those matrices over frames in each recording using a Rieman- nian metric (Moakher, 2005), and then map them to the tangent space (Lotte et al., 2018). The projections yield vectors of 190 features, corresponding to the number of elements in the up- per or lower triangles of the original symmetric matrices. We computed the time-domain features end-to-end from the pre- processed signals using the pyRiemann4 library.

To construct the frequency-based features, we consider 14 frequency bands ( fb): {[0.5, 2], [1, 3], [2, 4], [3, 6], [4, 8],

4https://pyriemann.readthedocs.io

[6, 10], [8, 13], [10, 15], [13, 18], [15, 21], [18, 24], [21, 27], [24, 30], [27, 40]} Hz. These bands cover the standard EEG frequency bands of δ, θ, α, low β, and high β.

The most basic features in the frequency domain are the power spectral densities corresponding to the specified bands, denoted as S xx( fb) where x is the channel index. The densi- ties are estimated separately for each frame using the multitaper method (Thomson, 1982) and then normalized so that the sum over channels and frequency bands equals one in each frame. These estimates are aggregated over frames in each recording using the median operation, following Gemein et al. (2020). This process results in 266 power features per recording, which were extracted from the EEG signals using the MNE library.

Cross-spectral densities, S xy( fb), are also calculated for each 6-second frame and are used to estimate the band-wise coher- ences between EEG channels in that frame according to the fol- lowing formula:

Cxy( fb) = |S xy( fb)| pS xx( fb) · S yy( fb)

. (1)

These coherences are aggregated over frames in each record- ing using the median. We also considered all other connectivity estimates provided by the MNE library and found the quantities (1) to give the best results. Because the coherence matrix is symmetric with ones on the diagonal, only its sub-diagonal ele- ments are further used. This results in 2,394 coherence features per recording, forming the second group of frequency-based features.

Different classical models considered in this study use vari- ous subsets of the handcrafted features, as described in the next section.

3.3. Models

We explore a variety of ML models, ranging from classical methods to advanced neural networks. Two of these models,

4

<!-- page 5 -->

siNet5 and RG, are closely reproduced following Gemein et al. (2020), while RF is loosely inspired by that paper. RF is based on the random-forest classifier but uses a smaller and simpler set of input features. These three models serve as a state-of- the-art reference, while the other eight models proposed in this paper are their extensions.

3.3.1. Classical models The random-forest6 (RF) classifier is implemented using the scikit-learn7 package (Pedregosa et al., 2011). It uses only the handcrafted power and coherence features, totaling 2,660 features per recording.

The model based on Riemannian geometry (RG) takes the 190 time-domain features as input and passes them to a support- vector classifier8 (SVC) with a radial basis function (RBF) ker- nel, implemented using the scikit-learn library.

A model we call the gradient-boosted ensemble (GBE) is im- plemented using the CatBoost9 library (Dorogush et al., 2018). It incorporates all 2,850 handcrafted features and passes them to an ensemble of 30 gradient-boost classifiers10. The final proba- bility of EEG pathology is obtained by averaging the probabil- ities predicted by the 30 members of the ensemble. Each mem- ber is trained separately and yields a slightly different classifier because the learning algorithm involves stochastic factors.

Hyperparameters of the GBE model were optimized using tree-structured Parzen estimators (TPE) (Bergstra et al., 2013) from the hyperopt11 library with respect to the area under the receiver operating characteristic curve (AUC) values from a 5- fold cross-validation on the TUH dataset. Although the hyper- parameters fitted to ELM19 are slightly different, they do not significantly alter the resulting AUC scores.

3.3.2. Neural networks We implement all our neural models within the PyTorch12

framework and train them on a single PC equipped with a gaming-class GPU with 12 GB of memory. A single training session does not significantly exceed one day, even for the most complex transformer models fitted to the largest ELM19 dataset.

5Our siNet is equivalent to the model known as BD-EEGNet in the original paper by Gemein et al. (2020).

6The RF model is implemented as an instance of the RandomForestClassifier class with hyperparameters set ac- cording to Gemein et al. (2020): criterion=’entropy’, bootstrap=False, max_features=’sqrt’, min_samples_leaf=2, min_samples_split=2, max_depth=90, and n_estimators=1600.

7https://scikit-learn.org 8The RG model is implemented as an instance of the SVC class with the fol- lowing hyperparameters: kernel=’rbf’, C=10, probability=True, and gamma=’auto’

9https://catboost.ai 10A single GBE classifier is implemented as an instance of the CatBoostClassifier class with the following hyperpa- rameters: objective=’Logloss’, boosting_type=’Plain’, bootstrap_type=’MVS’, eval_metric=’AUC’, iterations=700, learning_rate=0.085195, depth=6.0, l2_leaf_reg=1.1030, and colsample_bylevel=0.019947.

11https://hyperopt.github.io 12https://pytorch.org

Figure 3: Architecture of the EEGNet frame encoder, which processes a 6- second frame of the EEG signal and outputs an encoding as a vector of 288 fea- tures. This encoder is reimplemented from Gemein et al. (2020) and Lawhern et al. (2018) and has 1,408 parameters. Arrows represent layers and operations, while boxes indicate tensor shapes. Refer to Fig. A.14 for an explanation of the color code.

All our neural networks use a frame encoder that follows the EEGNet architecture depicted in Fig. 3. This encoder is reimplemented based on the Braindecode EEGNet described by Gemein et al. (2020), which itself is a reimplementation of the EEGNet originally introduced by Lawhern et al. (2018). The encoder is a fully convolutional network that performs separate temporal and spatial convolutions. It has 1,408 parameters and constitutes the first part of all our neural models, as described below. We tested other encoders, such as the Deep4 architec- ture discussed by Gemein et al. (2020), but found no advantages over EEGNet.

The simplest way to utilize the frame encoder is shown in Fig. 4. The encoder is attached to a single fully connected layer that serves as a frame classifier. During the training process, the network is fed individual 6-second frames, and the target label for each frame corresponds to the label of the entire recording from which the frame originates. Predictions are made using the same classifier and encoder arranged as shown in Fig. 5. Each frame of the examined recording is passed through the encoder, classifier, and sigmoid function to yield the probability

5

<!-- page 6 -->

Figure 4: Architecture used to train the siNet classifier and encoder, as well as to pretrain the encoder on single frames for later use with the miNet, MINet, and TransNet models. This network has 1,697 parameters.

of the signal in that frame being normal. These probabilities are then aggregated over all frames in the recording using the geometric mean to produce the final probability of normality for the entire recording. We refer to this basic model as siNet because it is trained on single frames.

We tested other methods of aggregating probabilities, such as the arithmetic average, minimum or maximum, but found the geometric mean to give the best results. However, it has one particular property: even if merely one frame in a recording yields zero individual probability, the aggregated probability also becomes zero. On the other hand, we want our models to have high recall and detect pathology even if a single frame ex- hibits abnormal symptoms. To reconcile these points, we make our models output the probability of the recording being nor- mal rather than pathological; therefore, we adopt the unconven- tional labeling introduced in Section 3.1.

The siNet has 1,697 parameters, both in prediction and train- ing, with the classification layer alone accounting for 289 pa- rameters. In fact, the latter layer is used by all our network mod- els as a classifier of either individual frames or entire record- ings, as specified below.

Except for the siNet, all our networks are trained in two dis- tinct ways. The first method, which we call naive, involves training the encoder from scratch along with the entire network. In the second approach, we first pretrain the encoder in a pro- cess identical to training the siNet, but the resulting classifier is discarded. The pretrained encoder is then attached to the other parts of the network and the entire network undergoes the main training. We denote the pretrained and naive versions of a model by suffixes P and N, respectively, such as miNetN or TransNetP, as described below.

The siNet is trained by assigning the label of the full record- ing to each of its frames. This is not fully justified because a pathology may not manifest itself in every single frame, and passing normal-like frames labeled as abnormal may confuse the model. To address this simplification, we resort to multiple- instance learning (MIL), a term first coined by Dietterich et al. (1997) and later discussed by several authors, including An- drews et al. (2002) and Wang et al. (2018). In the current context, the main idea is to train a model on all the frames in a recording simultaneously. Roughly speaking, this can be done using some form of aggregation before evaluating the loss. Note that the way of training our classical models can be viewed as a realization of the MIL paradigm because the handcrafted

features of individual frames are aggregated using the median operation or the Riemannian metric.

Figure 5: Architecture used by the siNet model for prediction and by the miNet model for both prediction and training. This network has 1,697 parameters. Although three frames are shown for illustration, the model can process an entire recording composed of an arbitrary number of frames.

In the realm of neural networks, successive efforts by Ra- mon and De Raedt (2000), Zhou and Zhang (2002), and Wang et al. (2018) led to a simple MIL architecture called miNet. It is formally identical to the siNet shown in Fig. 5 and the only difference is that the configuration from Fig. 5 is used for both prediction and training. In the training process, the network takes all the frames in a recording simultaneously and produces a single probability, which is then compared against the human label for the entire recording. This is possible because the archi- tecture in Fig. 5 is actually a single differentiable network that can process an arbitrary number of frames in one pass, with- out explicit loops. The encoder can be trained with the entire network from scratch or can be pretrained on single frames.

Figure 6: Architecture of the attention module. It follows the non-gated atten- tion approach of Ilse et al. (2018), while the concepts of query, key, and value are borrowed from the transformer paper by Vaswani (2017). This module has 166,176 parameters.

Although miNet is trained on entire recordings, aggregat- ing probabilities still has its limitations. A better solution is

6

<!-- page 7 -->

to aggregate features, which results in the MINet architecture proposed by Wang et al. (2018). Ilse et al. (2018) further im- proved the idea by introducing the attention mechanism, orig- inally considered in the context of machine translation and re- current networks (Bahdanau, 2014; Raffel and Ellis, 2015). Our variant of the attention module is depicted in Fig. 6. It essen- tially follows the non-gated attention of Ilse et al. (2018) but also employs the concepts of queries, keys, and values, bor- rowed from the transformer architecture (Vaswani, 2017). The attention module takes encoded features from all the frames in a recording and assigns a weight to each frame. Frames deemed more important for detecting pathology are expected to receive higher weights. These weights are then used to calculate a weighted average of the individual frame features, resulting in mean features that represent the entire recording. The attention module has 166,176 parameters.

Figure 7: Architecture of the MINet model, which has 167,873 parameters.

Our MINet model is depicted in Fig. 7. The network takes an entire recording and passes it through the frame encoder to produce encodings or features for each frame separately. These features then feed the attention module which aggregates them into a vector of mean features that encode the entire record- ing. These are finally passed to the classifier layer. The same architecture is used for both prediction and training, with the training process being identical to that of miNet. The MINet network has 167,873 parameters. Again, the encoder can be pretrained or not.

Figure 8: Architecture of our custom transformer block, which is the standard transformer encoder layer wrapped with additional layer normalization and a skip connection. This block has 1,516,640 parameters and is utilized in the TransNet model depicted in Fig. 9.

The attention module of MINet effectively selects frames that carry the most information but it cannot account for re- lations between frames, and, thus, between potentially distant regions of the recording. Such relations can be captured by self-attention, which is the main building block of the trans-

former architecture (Vaswani, 2017). We utilize only the trans- former encoder layer as introduced in the seminal paper and implemented in PyTorch as a predefined class13, with the de- fault number of 8 self-attention heads. However, we found that additional layer normalizations and skip connections slightly improve the results so we employ a custom transformer block depicted in Fig. 8. It has 1,516,640 parameters. We stack three such blocks sequentially. Although it seems sufficient to aggre- gate the transformer output features using the bare arithmetic mean, we managed to improve performance by using the atten- tion module from Fig. 6 instead, as in MINet. Our final trans- former model is depicted in Fig. 9, and we call it TransNet. It has 4,717,793 parameters.

Figure 9: Architecture of the TransNet model. The transformer block refers to the custom architecture presented in Fig. 8. The model has 4,717,793 parame- ters.

To recapitulate, we consider 7 neural models, all of which employ the EEGNet as their frame encoder, and we denote them as TransNetP, TransNetN, MINetP, MINetN, miNetP, miNetN, and siNet. They are trained in several ways but for prediction, they all take an arbitrarily long recording split into 6-second frames and return a single probability of pathology. The pa- rameter counts are summarized in Table 2.

3.3.3. Meta-model Different models may exploit different features of the EEG signal. This suggests that an amalgamation of sufficiently dis- tinct models could utilize a richer set of signal traits and, there- fore, perform better. Presumably, the handcrafted features of Section 3.2 are significantly different from those extracted auto- matically by the neural networks. Thus, the mixture should in- clude both neural and classical models. After some testing, we decided to combine the classical GBE with the neural MINetP and TransNetP, which are our best-performing single models. Various methods exist for blending several models into one,

13The transformer encoder layer is implemented as an instance of the TransformerEncoderLayer class with the following arguments: d_model=288, nhead=8, and batch_first=True.

7

<!-- page 8 -->

Table 2: Parameter counts in our neural models. The transformer column refers to the custom transformer block shown in Fig. 8.

Encoder Transformer Attention Classifier Total

siNet 1,408 289 1,697 miNet 1,408 289 1,697 MINet 1,408 166,176 289 167,873 TransNet 1,408 3×1,516,640 166,176 289 4,717,793

such as adaptive boosting; however, we empirically chose basic logistic regression. For a given recording, the three probabil- ities of pathology returned by the component models are fed to the logistic regression as input features and the regression outputs its own final probability. We refer to this solution as a meta-model. The scikit-learn implementation of logistic regression14 was used and optimized with the TPE algorithm from the hyperopt library, as was done for the GBE.

3.4. Training, validation, and testing

Metrics based on the confusion matrix, mostly accuracy (ACC), are frequently used to assess classification quality. However, following criticism from both the medical (Beck and Shultz, 1986; Bellazzi and Zupan, 1998) and ML (Provost et al., 1998; Langley, 2000) communities, we abandon these metrics in favor of the AUC. Among its advantages, the AUC metric is independent of the arbitrary threshold on the probabilities re- turned by a classification model. We use ACC only for compar- ison with the results from other articles.

For training the neural models, we minimize the standard binary cross-entropy using the RAdam optimizer (Liu et al., 2019) with the default settings. According to its authors, the op- timizer corrects the variance of the adaptive learning rate so that it is consistent, thus eliminating the need for warm-up heuris- tics.

Each subset of our data – ELM19, ELM8, ELM4, ELM2, ELM1, SZC, and TUH – has been randomly divided into 6 equal folds, stratified by pathology, sex, and, for subsets of ELM19, also by hospitals. For each subset, we carry out a 6-fold cross- validation. In each of its 6 steps, a different fold is selected for testing and a different one for validation, while the remaining four are left as a training set. The cross-entropy is minimized on those 4 training folds, and the AUC value is monitored on the validation fold. One hundred and fifty epochs are performed for the MIL models, while 50 are performed for the siNet and for pretraining the EEGNet encoder. To prevent overfitting, the epoch yielding the highest AUC on the validation fold is cho- sen as the final one. The resulting model is then evaluated on the test fold to calculate its AUC for the current validation step. Thus, each model is tested uniquely on data that have not influ- enced its training in any way. The mean and standard deviation of the 6 AUC values obtained from this cross-validation are re- ported below as the final AUC and its uncertainty.

14The logistic regression model is implemented as an instance of the LogisticRegression class with the following hyperparameters: C=7.9059 and max_iter=4,000.

The siNet and MIL models are trained in batches of 4,096 6- second frames and in batches of 64 recordings, respectively. In the MIL approach, only 64 randomly-sampled frames of each given recording are included in the batch due to GPU memory limitations. This can be viewed as a variant of data augmenta- tion or, more specifically, as a masking technique. If a model is required to correctly classify a recording based on 64 ran- dom frames, it will perform even better when all the frames are available during the prediction phase. We calculate the training AUC using only those 64 frames, whereas the validation and test metrics are always evaluated on entire recordings.

Figure 10: Learning curves for the siNet and TransNetP models for the main training phase in a sample cross-validation step.

Sample learning curves are displayed in Fig. 10. They show the AUC scores versus epoch numbers for the main training of the siNet and TransNetP models in an exemplary cross- validation step. AUC values on the test fold, validation fold, and four training folds are plotted. The curves are fairly stan- dard, except that the validation and test values for TransNetP suffer from downward spikes at certain epochs. This undesired effect occurs for some MIL models to a greater or lesser extent. We address it by selecting the epoch that yields the highest val- idation AUC, as described above. This is one reason why we cannot simply stop the training after an a priori fixed number of epochs but must introduce the validation fold.

The classical models are trained and evaluated in cross- validation on the same 6 folds used for the neural networks. The GBE is fitted to the 4 training folds, while the validation fold is used to select the optimal number of trees that maxi- mizes the validation AUC score. The scikit-learn classes for SVC and random-forest have no similar functionality, so the validation fold is skipped for RF and RG, and their training

8

<!-- page 9 -->

terminates based on the training set, as implemented in the li- brary. However, the final AUC scores are always evaluated on the test fold to avoid data leakage and to make the results fully comparable with those obtained for the neural networks.

3.5. Statistical tests

The 6-fold cross-validation procedure yields a statistical sample of 6 AUC values for each model and dataset. To com- pare these results across different samples, we calculate the mean AUC and its standard deviation for each sample. Sta- tistical testing would certainly be desirable to better assess the differences in AUC both among various models within a single dataset and across different datasets for a given model. How- ever, a review devoted to comparing many models on many datasets (Demšar, 2006) indicates that no existing statistical test fully meets our needs due to partially violated assumptions. Keeping this in mind, we nevertheless perform a relatively ro- bust test described below, but we consider its outcomes only as auxiliary indications. Fortunately, these results support our conclusions drawn from the mean AUC values, reinforcing our belief that the presented findings are valid.

We resort to the non-parametric Kruskal-Wallis test (Kruskal and Wallis, 1952) and feed it samples of 6 AUC values from cross-validation. We pass samples either from our 11 models tested on a given dataset or from a specific model evaluated on our 7 datasets. The test checks the null hypothesis that samples do not exhibit statistically significant differences in AUC val- ues. If the hypothesis is rejected, the post-hoc Conover-Iman test (Conover and Iman, 1979) provides a further pairwise com- parison between the samples. We adjust the resulting p-values according to the false discovery rate (FDR) method (Benjamini and Hochberg, 1995). The lower the p-value, the more certain the statistical difference between the corresponding two sam- ples, and critical p-values of 0.05 or 0.01 are commonly adopted as rejection thresholds.

4. Results and discussion

4.1. Reproduction of the literature results

As a sanity check, we start by reproducing the relevant TUH results reported by Gemein et al. (2020). We carry out 6-fold cross-validations for the RF, RG, and siNet models, which are common to both papers (see Section 3.3). Because Gemein re- ports ACC, we also calculate ACC by assuming the standard probability threshold of 0.5. Table 3 compares the results, and the agreement is well within one standard error.

4.2. Comparison of cross-validation results

The cross-validation AUC scores for all our 11 models tested on all 7 considered data subsets are listed in Table B.5 of Ap- pendix B and presented graphically in Fig. 11. Results of the statistical tests described in Section 3.5 are given in Ap- pendix C. Fig. C.15 compares different models within each dataset, while Figs. C.16 and C.17 compare each model be- tween different datasets. Among other quantities, the figures

Table 3: Comparison of cross-validation ACC values for the TUH database obtained in the present study and those reported by Gemein et al. (2020) for the three common models. The equivalent of our siNet is referred to as BD- EEGNet in the original paper.

Present study Gemein et al. (2020)

RF 82.40 ± 0.56 83.10 ± 2.44 RG 81.25 ± 1.00 81.26 ± 0.19 siNet 82.54 ± 1.64 83.36 ± 1.94

provide the p-values from the Conover-Iman test, which in- dicate the pairwise statistical differences between models or datasets.

Several interesting conclusions can be drawn from Fig. 11. Most strikingly, the performance of every model degrades rapidly across the TUH, SZC, and ELM1 subsets, despite their equal sizes. The statistical significance of the differences in AUC values is supported by the low Conover-Iman p-values obtained for all our models in comparisons between TUH and SZC, as well as between SZC and ELM1 (see Figs. C.16 and C.17). The drop from TUH to SZC can be attributed to the in- crease in the diversity of pathological conditions. For example, psychogenic seizures often lack the clear electrographic mark- ers typical of epileptic seizures (Naganur et al., 2019). The de- crease in AUC from SZC to ELM1 is apparently due to the in- clusion of multiple hospitals. Data from different institutions most likely occupy overlapping but distinct regions of the fea- ture space. If the same amount of data is distributed over many different regions, then each region contains remarkably fewer samples. These points illustrate how different kinds of hetero- geneity make EEG classification more challenging and dimin- ish the model’s capabilities.

Recent EEG studies (Kiessner et al., 2023; Western et al., 2021) have confirmed the rather obvious expectation that using larger datasets can improve the quality of pathology detection. Indeed, the AUC values steadily increase through the ELM19 subsets due to the increase in data quantity. This also shows that a few thousand recordings present in ELM1 (like in TUH) are not enough to effectively train models on heterogeneous data. At least tens of thousands are required, as in the full ELM19. Fig. 11 strongly suggests that the AUC would continue to in- crease with larger amounts of data, indicating that even more data are actually needed. In Section 4.3, we estimate the asymp- totic behavior for infinite data.

By using the statistical test of signs, Gemein et al. (2020) conclude that the performance of all their methods on the TUH dataset is statistically equivalent. The Kruskal-Wallis test indi- cates that the same is true for our models, as seen in the high p-values in Fig. C.15 a). One may, therefore, argue that vir- tually all reasonable architectures perform relatively well on small and homogeneous data, so such data do not truly allow us to identify which approaches are best suited for EEG clas- sification. Kiessner et al. (2024) demonstrate that differences between models emerge only with increasing amounts of homo- geneous data, while we observe similar behavior for the hetero- geneous case. Throughout the ELM19 subsets, more advanced

9

<!-- page 10 -->

Figure 11: Cross-validation AUC results for our models and datasets. Data points represent mean AUC scores, and error bars indicate the standard error of the mean. Values for reference models inspired by Gemein et al. (2020) are plotted in shades of blue; the MIL models with a naive encoder are in shades of green; and the MIL models with a pretrained encoder are in shades of red.

models take over while simpler ones lag behind, which is clear from Fig. 11. The Conover-Iman p-values marked in Fig. C.15 c)–g) also illustrate the gradual onset of statistically significant differences between models as the data quantity increases.

We compare our models mostly on the data subsets from ELM1 through ELM19 because they represent the fully hetero- geneous case. As far as classical methods are concerned, they can be ordered from RF to GBE in terms of the achieved AUC values. Surprisingly, RF performs worse than RG, even though it uses 2,660 frequency-domain features compared to only 190 time-domain ones passed to RG. This may be because the fre- quency features are normalized, so they do not carry informa- tion on the total signal power or amplitude, while the time fea- tures are not normalized and do contain that information. Alter- natively, the Riemannian projections of the time-domain covari- ances may indeed be particularly well suited for EEG analysis (Wilson et al., 2022; Tibermacine et al., 2024).

Nevertheless, our GBE model significantly outperforms both RG and RF, which is confirmed by low Conover-Iman p-values

between RF and GBE as well as between RG and GBE for all our datasets apart from TUH, as displayed in Fig. C.15. The GBE is likely superior because it uses all the handcrafted fea- tures, thus gaining more information about the signal, including the total power. Also, the modern gradient-boosting algorithm is generally considered more powerful, and finally, the model makes use of an ensemble that improves its generalization ca- pabilities.

Let us now proceed to the neural networks. The simple siNet clearly loses the race against the MIL models. This is likely be- cause its single-instance training suffers from the inherent flaw of assigning the label from the entire recording to every single frame, as pointed out in Section 3.3.2. Any architecture based on single-instance learning would exhibit the same weakness, regardless of whether its frame encoder is EEGNet, Deep4, or another. A vast majority of neural EEG models considered so far fall into this category.

Even the simplest MIL model, miNet, clearly outperforms siNet, despite both having the same architecture and differing

10

<!-- page 11 -->

only in the training routine, as discussed in Section 3.3.2. This demonstrates the significance of training neural models on en- tire recordings, to which the target labels pertain. Including the attention mechanism in the MINet architecture further boosts performance. Apparently, the appropriate selection of frames that carry the most information is quite important in EEG anal- ysis. Accounting for the relations between the frames through self-attention results in even higher AUC values, and the result- ing TransNetP performs best among our single models. This observation is supported by the low Conover-Iman p-values be- tween TransNetP and almost all other single models in a pair- wise comparison on ELM19, as given in Fig. C.15 g). The superiority of TransNetP aligns with the overall success of the transformer architecture in a wide range of applications.

Networks with a pretrained encoder consistently achieve bet- ter results than those trained entirely from scratch. This im- provement is modest but still meaningful. Although training on full recordings is methodologically more accurate (refer to Sec- tion 3.3.2), it imposes fewer constraints on the encoder because only one target label must be reproduced while many frames are available. Pretraining the encoder on single frames confines its behavior more strongly because every frame has a separate label. Although assigning the overall label of a recording to every frame is not fully appropriate, this pretraining strategy is effective enough to guide the encoder in the right direction for subsequent MIL training (see Section 3.3.2).

As expected, the meta-model composed of TransNetP, MINetP, and GBE indisputably outperforms all the single mod- els. The statistical differences in the corresponding AUC scores are confirmed by the low p-values of the Conover-Iman tests shown in Fig. C.15, particularly for the largest ELM19 subsets. The meta-model takes into account both the handcrafted fea- tures and the ones extracted by the neural networks, thus getting more information about the signal at hand. It may also benefit from an implicit regularization effect. By averaging the deci- sion surfaces of its component models, it yields a smoother de- cision boundary, which is less prone to overfitting. Fig. C.17 k) reports a rather low Conover-Iman p-value for the meta-model in comparison between TUH and ELM19, which is a prelimi- nary indication that the model might perform similarly on large heterogeneous data as it does for small and homogeneous ones. More arguments in favor of such a conclusion are given in Sec- tion 4.3.

The AUC curve for our best classical model, GBE, starts to saturate for the largest ELM19 subsets. Our conjecture is that the model simply cannot extract more information from the limited number of handcrafted features. It cannot create new features either. In contrast, the neural networks extract fea- tures themselves from the raw EEG signal and thus have the full information at their disposal. The networks presumably identify more and more useful properties of the signal as they receive more data. Some of them continue to improve and even- tually outperform GBE for the full ELM19 set. Indeed, the cor- responding differences in the AUC values between GBE and the pretrained networks with (self)-attention (i.e., MINetP and TransNetP) are statistically significant, as illustrated by the low Conover-Iman p-values given in Fig. C.15 g).

Finally, note that the AUC curves for the MINet and TransNet models do not exhibit signs of saturation. Conse- quently, the same is true for the meta-model. This leads us to expect that larger datasets will allow those architectures to at- tain even higher AUC values. We elaborate on this point in the next section.

4.3. Asymptotic behavior The curves plotted in Fig. 11 strongly suggest that some models would achieve higher AUC values if more data were available. Therefore, it is interesting to estimate the upper AUC limit and the quantity of data needed to reach it. Similar consid- erations have recently gained significant attention in other ML domains, and a saturation power law is often used to approxi- mate the relationship between accuracy and data size (Kiessner et al., 2024). This law can be formulated as follows:

ACC(n) = ACC∞−αn−β (2)

In our case, n is the number of EEG recordings, while α, β, and ACC∞are parameters that can be fitted to the existing dataset. ACC∞has a clear interpretation as the asymptotic ACC value in the limit of infinite data.

For each of our models, we fitted the saturation power law (2) to the cross-validation ACC values for the ELM19 subsets using the standard least-squares procedure. The resulting curves are plotted in Fig. 12, along with the data points. The asymp- totic value of ACC and its uncertainty estimated from the fit are marked with a horizontal line and an error corridor. Al- though the fits are generally reasonable, some data points devi- ate from the fitted curves, errors on the asymptotic ACC values are sometimes large, and the fit for miNetN did not even con- verge. Additionally, fits for neural networks are systematically less robust.

Our explanation for the latter point is that the optimizers used to train neural networks somewhat chaotically vary the bias term in the last layer that generates the logit values. This is equivalent to chaotically adjusting the threshold on the re- sulting probability within a certain range. Because the ACC value depends on that threshold, it exhibits redundant oscilla- tions. In contrast, the AUC metric is independent of the proba- bility threshold and, therefore, behaves more smoothly. Given these observations, we also fitted the power law (2) to the cross- validation AUC values, substituting AUC in place of ACC. The results are presented in Fig. 13. The AUC fits indeed demon- strate better agreement with the data and smaller errors on the asymptotic values. The standard R2 score, which measures fit quality, is also closer to the expected value of one, as listed in Table 4.

Apart from R2, Table 4 provides the fitted asymptotic val- ues of ACC and AUC. Our best model, the meta-model, could theoretically achieve an AUC score of roughly 91%, which is about the mean value reached by all our models on the TUH database. Kiessner et al. (2024) estimated the asymptotic ACC for increasing quantities of homogeneous data similar to TUH (Kiessner et al., 2023) and arrived at values between 85 and 87%, depending on the model. This aligns well with the asymp- totic ACC of 86% achieved by our meta-model for ELM19.

11

<!-- page 12 -->

Figure 12: Visualization of the saturation power law (2) fitted to ACC[%] values for all models. The solid blue line represents the fit to the available data, and the dashed line indicates extrapolation. The horizontal red line shows the estimated asymptote, and the shaded region marks the error corridor. The vertical line indicates the number of recordings, NDB, for which the estimated ACC approaches the asymptotic value of ACC∞within one standard error.

Figure 13: Visualization of the saturation power law (2) fitted to AUC[%] values for all models. The solid blue line represents the fit to the available data, and the dashed line indicates extrapolation. The horizontal red line shows the estimated asymptote, and the shaded region marks the error corridor. The vertical line indicates the number of recordings, NDB, for which the estimated AUC approaches the asymptotic value of AUC∞within one standard error.

These two observations suggest that the meta-model could per- form as well for heterogeneous data as it does for homogeneous data, provided that sufficiently large datasets are available. In other words, large quantities of EEG data may potentially com-

pensate for their diversity. However, it is important to note that the power law is not fully rooted in fundamental principles, and these predictions are, to some extent, speculative.

Table 4 also lists the number of recordings, NDB, for which

12

<!-- page 13 -->

Table 4: Estimations of the asymptotic ACC and AUC values according to the saturation power law (2), along with the estimated number of recordings NDB (in thousands) needed for each model to approach the asymptotic value within one standard error. Goodness of fit is measured by R2.

ACC AUC

ACC∞[%] R2 NDB[k] AUC∞[%] R2 NDB[k]

RF 76.4 ± 1.3 0.97 336 84.2 ± 0.8 0.99 2,148 RG 76.9 ± 0.5 0.97 510 84.4 ± 0.5 0.97 237 siNet 74.8 ± 0.4 0.60 13 83.6 ± 0.1 0.96 82 miNetN fit did not converge 87.0 ± 0.4 0.98 455 MINetN 78.0 ± 1.1 0.87 20 87.6 ± 0.8 0.89 71 TransNetN 78.8 ± 0.8 0.97 67 88.2 ± 0.7 0.97 130 miNetP 76.3 ± 0.7 0.94 19 87.5 ± 0.7 0.98 383 MINetP 77.4 ± 1.5 0.88 10 90.8 ± 2.1 0.95 346 TransNetP 80.8 ± 0.9 0.99 191 89.9 ± 1.2 0.98 258 GBE 78.6 ± 0.4 0.84 36 87.1 ± 0.4 0.93 83 META 86.0 ± 5.2 0.97 66 91.3 ± 1.1 0.99 401

the fitted ACC and AUC scores approach their asymptotic lim- its within one standard error in ACC∞and AUC∞, respectively. These limits are marked in Figs. 12 and 13 by vertical lines. NDB represents the data size needed for the models to attain their asymptotic limits, given that the limits are known only up to a certain error. Although such a measure is arbitrary and comes with a significant uncertainties, we believe that NDB cor- rectly estimates the order of magnitude. From the more reliable AUC data in Table 4, we infer that at least tens, and likely hun- dreds of thousands, of recordings are needed for the best models to approach their full capabilities. One may also speculate that collecting even more data would yield only slow and negligible improvements due to the power character of the saturation law (2), given the logarithmic scale for the abscissa in Figs. 12 and 13. However, the presented figures may change if more hetero- geneity is introduced by including data from several countries etc.

5. Limitations and outlook

A major limitation of our study is that a significant portion, or even a majority, of patients with EEG pathologies are un- der pharmacological treatment. It is, therefore, possible that the models are detecting EEG patterns induced by medication rather than the pathology itself. Unfortunately, we are un- able to assess the real impact of this potential confusion, be- cause there is no precise and reliable information about med- ication use in our database. We suspect that other studies on EEG pathology detection also suffer from the same uncer- tainty. Further research should address this issue by creating longitudinal databases that contain several types of recordings, such as abnormal recordings collected before pharmacological treatment is administered, abnormal recordings collected dur- ing treatment, normal recordings collected toward the end of treatment when the pathological symptoms have already dis- appeared, normal recordings collected after treatment has been completed, and normal recordings from healthy patients who have never taken relevant medication.

Furthermore, the ELM19 data were collected only in one country. An international effort could provide significantly larger datasets, making them more representative and more het- erogeneous.

Our results indicate that as the quantity of data increases, the best models can still improve their performance and may even reach the asymptotic AUC limit of about 91%. This raises the question of where that value comes from and whether it can be surpassed. Like Kiessner et al. (2024), we believe that the limit is mostly due to moderate inter-rater agreement. Opposite la- beling of very similar recordings causes the decision boundary to become spuriously curved or ragged, leading to overfitting and deteriorated performance. In simple terms, an ML model cannot reconcile contradictory human ratings.

A possible remedy is the use of fuzzy labels. In this ap- proach, each recording is annotated by several independent ex- perts as 0 for normal or 1 for pathological. These ratings are then averaged to yield a fuzzy label, which estimates the prob- ability that a randomly chosen rater annotates the recording as pathological. An ML model is then trained to reproduce these probabilities. Averaged ratings are much less contradictory than individual ones, enabling the model to fit them more accurately. This procedure can be viewed as a data-driven regularization that makes the decision boundary smoother and more fuzzy, which in turn reduces overfitting and better elucidates the ac- tual patterns hidden in the data. The manifold mixup proposed by Verma et al. (2019) has a similar effect. The output of the resulting model naturally measures the probability or degree of pathology. Even though such a measure is not perfect, it is likely the best that can be derived from human ratings because it reflects the inter-subjective knowledge of many experts. A robustly estimated degree of pathology can be more useful for clinicians than a noisy categorical prediction. This analysis re- quires data labeled by many raters, but it would be sufficient to assign fuzzy labels only to the most doubtful recordings situ- ated close to the decision boundary.

An even more ambitious solution would be to train models on EEG recordings labeled based on a full clinical examination

13

<!-- page 14 -->

rather than the EEG signal alone. If such training succeeds, the resulting models could potentially recognize EEG patterns that are not visible to the naked eye, at least for some pathologi- cal disorders. Unfortunately, we are not aware of any clinical database large enough to attempt ML training.

6. Conclusions

In our setting, data heterogeneity makes EEG classification significantly more difficult and degrades the performance of ML models. Heterogeneity arises from collecting data across multiple hospitals and the diversity of pathological conditions, which are not limited to epileptic disorders.

The performance of ML models improves with increasing quantities of data. In the asymptotic limit of infinite data vol- ume, the best models may theoretically achieve AUC scores of approximately 91%, which is comparable to the results for ho- mogeneous datasets. This suggests that very large amounts of data can eventually compensate for data heterogeneity, justify- ing the need to collect even larger corpora of EEG recordings, comprising tens or even hundreds of thousands of samples.

Virtually all relevant ML models perform comparably well on small, homogeneous datasets, while significant differences emerge only with increasing data size. Therefore, only large, heterogeneous databases may help identify architectures best suited for EEG classification in general.

Regarding classical models, the best results are obtained by an ensemble of gradient-boosted classifiers that utilize both time-domain and frequency-domain handcrafted features, in- cluding information about signal amplitude. However, classical models cannot extract more information from the signal than is contained in the handcrafted features, which inherently limits their capabilities, particularly for large datasets.

In the case of neural networks, it seems that training on en- tire recordings within an MIL paradigm, as well as including attention and self-attention mechanisms, is essential. Conse- quently, the transformer architecture prevails among both neu- ral and classical models. Pretraining the encoder on individual frames also helps improve performance.

Because neural networks and classical models presumably exploit different properties of the EEG signal, even more infor- mation can be extracted by merging the two types into a meta- model. Indeed, our variant of the meta-model performs best among all the methods that we tested. It achieves an AUC value exceeding 88% on our largest heterogeneous dataset of 55,787 recordings and is expected to reach 91% in the asymptotic limit of infinite data.

The use of medication by most patients with EEG patholo- gies poses a challenge for automatic EEG classification and should be addressed through further research. Collecting EEG annotations from multiple raters to form fuzzy labels could po- tentially enable ML models to overcome current asymptotic limits on predictive accuracy.

Declarations

Declaration of generative AI in scientific writing. The authors used no AI assistance when writing the text of this article.

Data availability. The TUH database can be obtained from The Neural Engineering Data Consortium at https://isip.piconepress.com/projects/nedc/ html/tuh_eeg/#c_tuab. The ELM19 database is available from Elmiko Biosignals sp. z o.o. upon reasonable request to EEG.database@elmiko.pl.

Conflict of interest. The authors declare that they have no con- flicts of interest.

Ethics approval. All procedures involving human participants were performed in accordance with the ethical standards of the institutional and/or national research committee, as well as the 1964 Helsinki Declaration and its later amendments or compa- rable ethical standards.

Acknowledgments. This study was supported by The National Centre for Research and Development (NCBR) grant number POIR.01.01.01-00-1074/21 and partially supported by the Cen- ter for Machine Learning, University of Warsaw (IDUB, Action I.3.7).

CRediT authorship contribution statement. Conceptualization: M.P., M.D., Pr.O., P.N., Pa.O., J.R., Ja.Z.; Creation and anonymization of the ELM19 dataset: P.N., Pa.O., Jo.Z.; Data curation: M.P., M.D., Pa.O.; Analysis and interpretation of re- sults: M.P., M.D., Pr.O., J.R., Ja.Z.; Drafting the manuscript: M.P., M.D., Pr.O., J.R., Ja.Z.

References

L. Yang, J. He, D. Liu, W. Zheng, Z. Song, EEG microstate features as an

automatic recognition model of high-density epileptic EEG using support vector machine, Brain Sciences 12 (2022) 1731. W. Klonowski, E. Olejarczyk, R. Stepien, Complexity of EEG-signal in time

domain-possible biomedical application, in: AIP Conference Proceedings, volume 622, American Institute of Physics, 2002, pp. 155–162. S. Ahrens, J. D. Twanow, J. Vidaurre, S. Gedela, M. Moore-Clingenpeel, A. P.

Ostendorf, Electroencephalography technologist inter-rater agreement and interpretation of pediatric critical care electroencephalography, Pediatric neurology 115 (2021) 66–71. J. J. Halford, D. Shiau, J. Desrochers, B. Kolls, B. Dean, C. Waters, N. Azar,

K. Haas, E. Kutluay, G. Martz, et al., Inter-rater agreement on identification of electrographic seizures and periodic discharges in ICU EEG recordings, Clinical Neurophysiology 126 (2015) 1661–1669. F. A. Nascimento, R. Katyal, M. Olandoski, H. Gao, S. Yap, R. Matthews,

S. Rampp, W. Tatum, R. Strowd, S. Beniczky, Expert accuracy and inter- rater agreement of “must-know” EEG findings for adult and child neurology residents, Epileptic Disorders 26 (2024) 109–120. S. Lopez de Diego, Automated interpretation of abnormal adult elec-

troencephalography., 2017. URL: https://isip.piconepress.com/ publications/ms_theses/2017/abnormal/thesis/, master Thesis, Temple University. R. T. Schirrmeister, J. T. Springenberg, L. D. J. Fiederer, M. Glasstetter,

K. Eggensperger, M. Tangermann, F. Hutter, W. Burgard, T. Ball, Deep learning with convolutional neural networks for EEG decoding and visual- ization, Human brain mapping 38 (2017) 5391–5420.

14

<!-- page 15 -->

S. Roy, I. Kiral-Kornek, S. Harrer, Chrononet: A deep recurrent neural network

for abnormal EEG identification, in: Artificial Intelligence in Medicine: 17th Conference on Artificial Intelligence in Medicine, AIME 2019, Poz- nan, Poland, June 26–29, 2019, Proceedings 17, Springer, 2019, pp. 47–56. K. Van Leeuwen, H. Sun, M. Tabaeizadeh, A. Struck, M. Van Putten, M. West-

over, Detecting abnormal electroencephalograms using deep convolutional networks, Clinical neurophysiology 130 (2019) 77–84. L. A. Gemein, R. T. Schirrmeister, P. Chrab˛aszcz, D. Wilson, J. Boedecker,

A. Schulze-Bonhage, F. Hutter, T. Ball, Machine-learning-based diagnostics of EEG pathology, NeuroImage 220 (2020) 117021. D. Western, T. Weber, R. Kandasamy, F. May, S. Taylor, Y. Zhu, L. Can-

ham, Automatic report-based labelling of clinical EEGs for classifier train- ing, in: 2021 IEEE Signal Processing in Medicine and Biology Symposium (SPMB), IEEE, 2021, pp. 1–6. H. A. Khan, R. Ul Ain, A. M. Kamboh, H. T. Butt, S. Shafait, W. Alamgir,

D. Stricker, F. Shafait, The NMT scalp EEG dataset: an open-source an- notated dataset of healthy and pathological EEG recordings for predictive modeling, Frontiers in neuroscience 15 (2022) 755817. D. Wilson, R. T. Schirrmeister, L. A. W. Gemein, T. Ball, Deep riemannian

networks for EEG decoding, arXiv preprint arXiv:2212.10426 (2022). A.-K. Kiessner, R. T. Schirrmeister, L. A. Gemein, J. Boedecker, T. Ball, An

extended clinical EEG dataset with 15,300 automatically labelled recordings for pathology decoding, NeuroImage: Clinical 39 (2023) 103482. A.-K. Kiessner, R. T. Schirrmeister, J. Boedecker, T. Ball, Reaching the ceil-

ing? empirical scaling behaviour for deep EEG pathology classification, Computers in Biology and Medicine (2024) 108681. O. Faust, Y. Hagiwara, T. J. Hong, O. S. Lih, U. R. Acharya, Deep learning for

healthcare applications based on physiological signals: A review, Computer methods and programs in biomedicine 161 (2018) 1–13. R. Miotto, F. Wang, S. Wang, X. Jiang, J. T. Dudley, Deep learning for health-

care: review, opportunities and challenges, Briefings in bioinformatics 19 (2018) 1236–1246. A. Craik, Y. He, J. L. Contreras-Vidal, Deep learning for electroencephalogram

(EEG) classification tasks: a review, Journal of neural engineering 16 (2019) 031001. Y. Roy, H. Banville, I. Albuquerque, A. Gramfort, T. H. Falk, J. Faubert, Deep

learning-based electroencephalography analysis: a systematic review, Jour- nal of neural engineering 16 (2019) 051001. D. Merlin Praveena, D. Angelin Sarah, S. Thomas George, Deep learning tech-

niques for EEG signal applications–a review, IETE journal of Research 68 (2022) 3030–3037. I. E. Tibermacine, S. Russo, A. Tibermacine, A. Rabehi, B. Nail, K. Kadri,

C. Napoli, Riemannian geometry-based EEG approaches: A literature re- view, arXiv preprint arXiv:2407.20250 (2024). I. Obeid, J. Picone, The Temple University Hospital EEG data corpus, Frontiers

in neuroscience 10 (2016) 196. Ö. Yıldırım, U. B. Baloglu, U. R. Acharya, A deep convolutional neural net-

work model for automated identification of abnormal EEG signals, Neural Computing and Applications 32 (2020) 15857–15868. H. Albaqami, G. M. Hassan, A. Subasi, A. Datta, Automatic detection of ab-

normal EEG signals using wavelet feature extraction and gradient boosting decision tree, Biomedical Signal Processing and Control 70 (2021) 102957. K. P. Ayodele, W. O. Ikezogwo, M. A. Komolafe, P. Ogunbona, Supervised

domain generalization for integration of disparate scalp EEG datasets for automatic epileptic seizure detection, Computers in biology and medicine 120 (2020) 103757. F. Roques, S. Nashef, P. Michel, E. Gauducheau, C. De Vincentiis, E. Baudet,

J. Cortina, M. David, A. Faichney, F. Gavrielle, et al., Risk factors and out- come in european cardiac surgery: analysis of the euroscore multinational database of 19030 patients, European journal of cardio-thoracic surgery 15 (1999) 816–823. J. P. Greving, M. J. Wermer, R. D. Brown, A. Morita, S. Juvela, M. Yonekura,

T. Ishibashi, J. C. Torner, T. Nakayama, G. J. Rinkel, et al., Development of the phases score for prediction of risk of rupture of intracranial aneurysms: a pooled analysis of six prospective cohort studies, The Lancet Neurology 13 (2014) 59–66. M. Aerts, G. Minalu, S. Bösner, F. Buntinx, B. Burnand, J. Haasenritter,

L. Herzig, J. A. Knottnerus, S. Nilsson, W. Renier, et al., Pooled individual patient data from five countries were used to derive a clinical prediction rule for coronary artery disease in primary care, Journal of clinical epidemiology 81 (2017) 120–128.

N. A. Hilkens, A. Algra, H.-C. Diener, J. B. Reitsma, P. M. Bath, L. Csiba,

W. Hacke, L. J. Kappelle, P. J. Koudstaal, D. Leys, et al., Predicting major bleeding in patients with noncardioembolic stroke on antiplatelets: S2top- bleed, Neurology 89 (2017) 936–943. M. Schinkel, F. C. Bennis, A. W. Boerman, W. J. Wiersinga, P. W. Nanayakkara,

Embracing cohort heterogeneity in clinical machine learning development: a step toward generalizable models, Scientific reports 13 (2023) 8363. S. Tayebi Arasteh, C. Kuhl, M.-J. Saehn, P. Isfort, D. Truhn, S. Nebelung, En-

hancing domain generalization in the AI-based analysis of chest radiographs with federated learning, Scientific Reports 13 (2023) 22576. Y. Gao, F. Sun, Batch normalization followed by merging is powerful for phe-

notype prediction integrating multiple heterogeneous studies, PLOS Com- putational Biology 19 (2023) e1010608. S. R. Benbadis, The tragedy of over-read EEGs and wrong diagnoses of epilepsy, Expert review of neurotherapeutics 10 (2010) 343–346. B. Kemp, A. Värri, A. C. Rosa, K. D. Nielsen, J. Gade, A simple format for

exchange of digitized polygraphic recordings, Electroencephalography and clinical neurophysiology 82 (1992) 391–393. A. Gramfort, M. Luessi, E. Larson, D. A. Engemann, D. Strohmeier, C. Brod-

beck, R. Goj, M. Jas, T. Brooks, L. Parkkonen, M. S. Hämäläinen, MEG and EEG data analysis with MNE-Python, Frontiers in Neuroscience 7 (2013) 1–13. doi:10.3389/fnins.2013.00267. M. Congedo, A. Barachant, A. Andreev, A new generation of brain-computer

interface based on riemannian geometry, arXiv preprint arXiv:1310.8115 (2013). M. Moakher, A differential geometric approach to the geometric mean of sym-

metric positive-definite matrices, SIAM Journal on Matrix Analysis and Applications 26 (2005) 735–747. F. Lotte, L. Bougrain, A. Cichocki, M. Clerc, M. Congedo, A. Rakotoma-

monjy, F. Yger, A review of classification algorithms for EEG-based brain– computer interfaces: a 10 year update, Journal of neural engineering 15 (2018) 031005. D. J. Thomson, Spectrum estimation and harmonic analysis, Proceedings of

the IEEE 70 (1982) 1055–1096. F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel,

M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, E. Duchesnay, Scikit-learn: Ma- chine learning in Python, Journal of Machine Learning Research 12 (2011) 2825–2830. A. V. Dorogush, V. Ershov, A. Gulin, Catboost: Gradient boosting with categor-

ical features support. arxiv 2018, arXiv preprint arXiv:1810.11363 (2018). J. Bergstra, D. Yamins, D. Cox, Making a science of model search: Hyperpa-

rameter optimization in hundreds of dimensions for vision architectures, in: International conference on machine learning, PMLR, 2013, pp. 115–123. V. J. Lawhern, A. J. Solon, N. R. Waytowich, S. M. Gordon, C. P. Hung, B. J.

Lance, EEGNet: a compact convolutional neural network for EEG-based brain–computer interfaces, Journal of neural engineering 15 (2018) 056013. T. G. Dietterich, R. H. Lathrop, T. Lozano-Pérez, Solving the multiple instance

problem with axis-parallel rectangles, Artificial intelligence 89 (1997) 31– 71. S. Andrews, I. Tsochantaridis, T. Hofmann, Support vector machines for multiple-instance learning, Advances in neural information processing sys- tems 15 (2002). X. Wang, Y. Yan, P. Tang, X. Bai, W. Liu, Revisiting multiple instance neural

networks, Pattern Recognition 74 (2018) 15–24. J. Ramon, L. De Raedt, Multi instance neural networks, in: ICML-2000 Work-

shop on Attribute-Value and Relational Learning, 2000, pp. 53–60. Z.-H. Zhou, M.-L. Zhang, Neural networks for multi-instance learning, in: Pro-

ceedings of the International Conference on Intelligent Information Technol- ogy, Beijing, China, Citeseer, 2002, pp. 455–459. M. Ilse, J. Tomczak, M. Welling, Attention-based deep multiple instance learn-

ing, in: International conference on machine learning, PMLR, 2018, pp. 2127–2136. A. Vaswani, Attention is all you need, Advances in Neural Information Pro-

cessing Systems (2017). D. Bahdanau, Neural machine translation by jointly learning to align and trans-

late, arXiv preprint arXiv:1409.0473 (2014). C. Raffel, D. P. Ellis, Feed-forward networks with attention can solve some

long-term memory problems, arXiv preprint arXiv:1512.08756 (2015). J. R. Beck, E. K. Shultz, The use of relative operating characteristic (roc) curves in test performance evaluation., Archives of pathology & laboratory

15

<!-- page 16 -->

medicine 110 (1986) 13–20. R. Bellazzi, B. Zupan, Intelligent data analysis in medicine and pharmacology:

a position statement, in: IDAMAP Workshop Notes at the 13th European Conference on Artificial Intelligence, ECAI, volume 98, 1998. F. J. Provost, T. Fawcett, R. Kohavi, et al., The case against accuracy estimation

for comparing induction algorithms., in: ICML, volume 98, 1998, pp. 445– 453. P. Langley, Crafting papers on machine learning, in: ICML, 2000, pp. 1207–

1216. L. Liu, H. Jiang, P. He, W. Chen, X. Liu, J. Gao, J. Han, On the variance of the

adaptive learning rate and beyond, arXiv preprint arXiv:1908.03265 (2019). J. Demšar, Statistical comparisons of classifiers over multiple data sets, The

Journal of Machine Learning Research 7 (2006) 1–30. W. H. Kruskal, W. A. Wallis, Use of ranks in one-criterion variance analysis,

Journal of the American statistical Association 47 (1952) 583–621. W. J. Conover, R. L. Iman, On Multiple-Comparisons Procedures, Technical

Report LA-7677-MS, Los Alamos Scientific Laboratory, 1979. Y. Benjamini, Y. Hochberg, Controlling the false discovery rate: a practi- cal and powerful approach to multiple testing, J. Roy. Statist. Soc. Ser. B 57 (1995) 289–300. URL: http://links.jstor.org/sici?sici= 0035-9246(1995)57:1<289:CTFDRA>2.0.CO;2-E&origin=MSN. V. D. Naganur, S. Kusmakar, Z. Chen, M. S. Palaniswami, P. Kwan, T. J.

O’Brien, The utility of an automated and ambulatory device for detecting and differentiating epileptic and psychogenic non-epileptic seizures, Epilep- sia open 4 (2019) 309–317. V. Verma, A. Lamb, C. Beckham, A. Najafi, I. Mitliagkas, D. Lopez-Paz,

Y. Bengio, Manifold mixup: Better representations by interpolating hid- den states, in: International conference on machine learning, PMLR, 2019, pp. 6438–6447.

16

<!-- page 17 -->

Appendix A. Color code for neural-network architectures

Figure A.14: Color code used throughout the paper to visualize neural-network architectures.

Appendix B. AUC values for the cross-validation results

Table B.5: Mean cross-validation AUC values and their standard errors obtained for each model and dataset. These results are visualized in Fig. 11

TUH SZC ELM1 ELM2 ELM4 ELM8 ELM19

RF 90.4 ± 0.5 82.8 ± 0.5 77.8 ± 0.9 79.1 ± 0.7 80.3 ± 0.6 80.9 ± 0.2 81.7 ± 0.1 RG 89.2 ± 0.7 81.3 ± 0.4 79.1 ± 0.6 80.4 ± 0.6 81.7 ± 0.5 82.7 ± 0.3 83.2 ± 0.2 siNet 91.0 ± 0.4 85.8 ± 0.3 79.8 ± 0.3 81.9 ± 0.4 82.6 ± 0.4 83.3 ± 0.2 83.5 ± 0.1 miNetN 90.4 ± 0.6 85.6 ± 0.5 79.4 ± 1.0 82.0 ± 0.5 83.3 ± 0.5 84.8 ± 0.2 85.7 ± 0.1 MINetN 90.8 ± 0.5 85.2 ± 0.7 79.9 ± 0.7 83.3 ± 0.3 84.5 ± 0.5 85.2 ± 0.6 86.7 ± 0.2 TransNetN 90.1 ± 0.7 84.0 ± 0.9 78.3 ± 0.9 81.4 ± 0.8 84.6 ± 0.3 85.6 ± 0.4 86.9 ± 0.2 miNetP 90.5 ± 1.7 85.4 ± 0.7 80.8 ± 0.5 82.4 ± 0.6 83.9 ± 0.6 85.1 ± 0.2 85.8 ± 0.2 MINetP 91.5 ± 0.9 85.7 ± 0.5 81.1 ± 0.3 83.3 ± 0.6 85.0 ± 0.6 85.7 ± 0.2 87.0 ± 0.2 TransNetP 91.3 ± 0.9 85.1 ± 0.8 79.7 ± 1.3 82.4 ± 0.7 85.0 ± 0.5 86.0 ± 0.4 87.5 ± 0.1 GBE 92.2 ± 0.6 85.4 ± 0.5 81.9 ± 0.7 83.7 ± 0.5 85.3 ± 0.4 86.2 ± 0.2 86.5 ± 0.2 META 91.7 ± 1.1 86.5 ± 0.8 81.8 ± 0.7 84.7 ± 0.9 86.0 ± 0.5 87.5 ± 0.4 88.7 ± 0.5

17

<!-- page 18 -->

Appendix C. Statistical tests

Figure C.15: Statistical comparison of AUC scores yielded by the models within each dataset. Left – boxplots and Kruskal-Wallis test statistic H and p-value; right – post-hoc Conover-Iman p-values adjusted using the FDR method.

18

<!-- page 19 -->

Figure C.16: Statistical comparison of AUC scores yielded by each model across different datasets. Left – boxplots and Kruskal-Wallis test statistic H and p-value; right – post-hoc Conover-Iman p-values adjusted using the FDR method.

19

<!-- page 20 -->

Figure C.17: Statistical comparison of AUC scores yielded by each model across different datasets. Left – boxplots and Kruskal-Wallis test statistic H and p-value; right – post-hoc Conover-Iman p-values adjusted using the FDR method.

20