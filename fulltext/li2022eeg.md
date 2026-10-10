<!-- source: pdf/li2022eeg.pdf | converter: pymupdf -->

<!-- page 1 -->

# arXiv:2203.11279v1  [eess.SP]  16 Mar 2022

## EEG based Emotion Recognition: A Tutorial and Review

XIANG LI∗, Qilu University of Technology (Shandong Academy of Sciences), Shandong Computer Science Center (National Supercom- puter Center in Jinan), China YAZHOU ZHANG∗, Software Engineering College, Zhengzhou University of Light Industry, China and State Key Lab. for Novel Soft- ware Technology, Nanjing University, China PRAYAG TIWARI†, Department of Computer Science, Aalto University, Finland DAWEI SONG†, School of Computer Science and Technology, Beijing Institute of Technology, China BIN HU†, Institute of Engineering Medicine, Beijing Institute of Technology, China MEIHONG YANG, Qilu University of Technology (Shandong Academy of Sciences), Shandong Computer Science Center (National Supercomputer Center in Jinan), China ZHIGANG ZHAO, Qilu University of Technology (Shandong Academy of Sciences), Shandong Computer Science Center (National Supercomputer Center in Jinan), China NEERAJ KUMAR†, Department of Computer Science and Engineering, Thapar Institute of Engineering and Technology (Deemed University), India PEKKA MARTTINEN†, Department of Computer Science, Aalto University, Finland

Emotion recognition technology through analyzing the EEG signal is currently an essential concept in Artiﬁcial Intelligence and holds great potential in emotional health care, human-computer interaction, multimedia content recommendation, etc. Though there have been several works devoted to reviewing EEG-based emotion recognition, the content of these reviews needs to be updated. In addition, those works are either fragmented in content or only focus on speciﬁc techniques adopted in this area but neglect the holistic perspective of the entire technical routes. Hence, in this paper, we review from the perspective of researchers who try to take the ﬁrst step on this topic. We review the recent representative works in the EEG-based emotion recognition research and provide a tutorial to guide the researchers to start from the beginning. The scientiﬁc basis of EEG-based emotion recognition in the psychological and physiological levels is introduced. Further, we categorize these reviewed works into diﬀerent technical routes and illustrate the theoretical basis and the research motivation, which will help the readers better understand why those techniques are studied and employed. At last, existing challenges and future investigations are also discussed in this paper, which guides the researchers to decide potential future research directions.

CCS Concepts: • Human-centered computing →Human computer interaction (HCI); Ubiquitous and mobile computing; • Computing methodologies →Artiﬁcial intelligence.

Additional Key Words and Phrases: EEG, emotion recognition, aﬀective computing, psychophysiological computing

ACM Reference Format: Xiang Li, Yazhou Zhang, Prayag Tiwari, Dawei Song, Bin Hu, Meihong Yang, Zhigang Zhao, Neeraj Kumar, and Pekka Marttinen. 2022. EEG based Emotion Recognition: A Tutorial and Review. ACM Comput. Surv. 1, 1, Article 1 (January 2022), 34 pages. https://doi.org/10.1145/3524499

## 1 INTRODUCTION

Emotion (or aﬀect) recognition (or detection) has increasingly drawn attention from researchers with a multidisciplinary background. It is the leading scientiﬁc problem in Aﬀective Computing, which is a comparatively new research ﬁeld proposed by Picart [1], namely how to empower computer systems to precisely process, recognize and comprehend emotional information expressed by a human for natural human-computer interactions (HCI) [2]. It is an important concept both in Artiﬁcial Intelligence and Ambient Intelligence [3]. Interdisciplinary knowledge is needed in Aﬀective Computing, and the ﬁndings can further promote the development of the various disciplines, including Computer Science, Electronic Engineering, Human Factors Engineering, Psychology, Neuroscience, Medical Science, etc.

∗Xiang Li and Yazhou Zhang contribute equally and share the co-ﬁrst authorship. †Corresponding authors.

Authors’ addresses: Xiang Li, xiangli@sdas.org, Qilu University of Technology (Shandong Academy of Sciences), Shandong Computer Science Center (National Supercom- puter Center in Jinan), Jinan, China; Yazhou Zhang, yzzhang@zzuli.edu.cn, Software Engineering College, Zhengzhou University of Light Industry, Zhengzhou, China and State Key Lab. for Novel Software Technology, Nanjing University, Nanjing, China; Prayag Tiwari, prayag.tiwari@aalto.ﬁ, Department of Computer Science, Aalto Uni- versity, Finland; Dawei Song, dwsong@bit.edu.cn, School of Computer Science and Technology, Beijing Institute of Technology, Beijing, China; Bin Hu, bh@bit.edu.cn, Institute of Engineering Medicine, Beijing Institute of Technology, Beijing, China; Meihong Yang, yangmh@sdas.org, Qilu University of Technology (Shandong Academy of Sciences), Shandong Computer Science Center (National Supercomputer Center in Jinan), Jinan, China; Zhigang Zhao, zhaozhg@sdas.org, Qilu University of Technology (Shandong Academy of Sciences), Shandong Computer Science Center (National Supercomputer Center in Jinan), Jinan, China; Neeraj Kumar, neeraj.kumar@thapar.edu, Department of Computer Science and Engineering, Thapar Institute of Engineering and Technology (Deemed University), Patiala (Punjab), India; Pekka Marttinen, pekka.marttinen@aalto.ﬁ, Department of Computer Science, Aalto University, Finland.

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for proﬁt or commercial advantage and that copies bear this notice and the full citation on the ﬁrst page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior speciﬁc permission and/or a fee. Request permissions from permissions@acm.org. © 2022 Association for Computing Machinery.

0360-0300/2022/1-ART1 $15.00 https://doi.org/10.1145/3524499

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 2 -->

1:2 • Li and Zhang, et al. As a complex psychological state, emotion is reﬂected in physical behaviors and physiological activities [4]. In the past decade, much eﬀort has been made to recognize emotions based on aﬀective information gathered from various physical behaviors and physiological activities, such as voices from the microphone, signals from neurophysiological activity measuring devices, videos from cameras, and texts from the website, etc. The essence of emotion detection research is utilizing statistical machine learning techniques (e.g., classiﬁcation, regression, or clustering) to identify users’ diﬀerent emotional states in real-time or oﬄine. The problem is challenging as we have to dig and utilize the latent components embedded in the weak and noisy emotion- related data sources, including natural language, facial expressions, speech, body gestures, bio-signals, text, eye gaze, etc., collected from multiple monitor platforms mentioned above. Currently, judging emotional states based on physiological activities (physiological clue) is a hot topic in Aﬀective Computing. Some psycho or physiological researches have manifested there exists dependencies between the physiological process and the emotion cognition process even though there still exists debates on the order of appearance of these two processes [5]. Hence, Computational Psychophysiology-based approaches are supposed to be eﬀective complements for facial or speech information (non-physiological clue) based recognition methods, whose performance could be greatly inﬂuenced when users intentionally dissemble their true feelings by wearing ‘social masks’. Considering the central nervous system (brain) regulates and controls the autonomic nervous system to participate in emotional processes, directly utilizing the brain activities information (e.g., EEG) to study the emotional cognition mechanism and recognize emotional state is especially worth studying.

The EEG based emotion recognition has wide application prospects. For example, developing emotion-aware driver assistance systems for cars is currently recognized as a potential way to enhance driving safety [6]. In the ﬁeld of neurology, identiﬁed emotions in response to speciﬁc stimuli and the corresponding neural activities can be analyzed for diagnosing some aﬀective disorders, such as PTSD (post straumatic stress disorder) [7] and depression [8, 9]. The psychological studies have found an attentional bias phenomenon in depressed individuals, in which increased attention to negative or dysphoric stimuli rather than positive contents [10]. Besides, the detected emotion can be utilized to guide various emotion disorder therapy, e.g. robot- assisted therapy [11] and music-assisted therapy [12, 13]. In the ﬁeld of Information Retrieval (IR), emotion recognition (or called sentiment analysis) has always been an active research ﬁeld. The detected emotion states can be used for emotion-associated IR needs, e.g., for implicit tagging of the multimedia contents [14–16], or for enriching user proﬁles to improve the topical relevance of the recommended multimedia contents [17]. Emotion recognition contributes to building the human-centered information retrieval (IR) system [18, 19]. In the ﬁeld of leisure and entertainment, e.g., the computer gaming, researchers sought to detect gamers’ emotional states in order to adjust to game’s level of diﬃculty, punishment, and encouragement [20]. In Virtual Reality (VR) applications, e.g., VR in education, the inﬂuence of emotional states on memory has been veriﬁed, the positive mood has beneﬁcial eﬀects on spatial learning. Hence, the emotion should be recognized during learning in VR environment [21, 22].

Essentially, EEG-based emotion recognition belongs to one kind of pattern recognition research. As we know, resolving a pattern recognition problem usually contains several main steps, namely as follows:

• Firstly, the deﬁnition and quantiﬁcation of the recognition target should be determined, by which the problem can be resolved as one computable problem. • Secondly, acquiring suﬃcient and valid research data is vitally important in preparing comprehensive space for searching model decision boundaries. • Thirdly, preprocessing the data and acquiring the representation (e.g., feature extraction or feature learning) are typically needed in building pattern recognition models. Target-related representative characteristics extracted from raw data can eliminate redundant information that may inﬂuence model construction. • Finally, the recognition models are designed, trained, and evaluated based on the processed data iteratively until a model with acceptable recognition accuracy can be determined.

Domestic and overseas research on EEG-based emotion recognition studies also covers these topics. Such being the case, in this paper, we choose to outline the review covering these topics as mentioned above. Before writing this survey, there have been several works devoted to reviewing EEG- based emotion recognition. It’s necessary to introduce those related survey papers that have been published in recent three years and expound on the motivation and the necessity to make a new survey paper for this research ﬁeld. Firstly, the contents of several survey papers need to be updated. For example, the surveys of Lotte et al. [23] and Alarcao and Fonseca [24] were published before 2019, and the surveyed works were developed between 2006 and 2017. Dadebayev et al. [25] mainly introduces the application of consumer-grade EEG acquisition devices (e.g., the Emotive, OpenBCI, and NeuroSky) in emotion recognition. It mainly reviews works between 2014 and 2019. Although the surveys conducted by Suhaimi et al. [26], Arya et al. [27], and Rahman et al. [28] were published after 2021, most of the reviewed methodologies were developed before 2019. For example, Arya et al. [27] and Suhaimi et al. [26] choose to survey works between 2009 and 2018. Secondly, these surveys emphasize traditional feature engineering and Machine Learning-based approaches. The Deep Learning-based approaches have not been systematically introduced. We think these surveys should be improved by adding more content about Deep Learning. Thirdly, several surveys are not written speciﬁcally for the aﬀective brain-computer interface (BCI) tasks. For example, although Craik et al. [29] focuses on introducing the Deep Learning-based methodologies applied to EEG modeling. The reviewed EEG classiﬁcation tasks are not restricted to emotion recognition. Other tasks related to mental workload, motor imagery, event-related potential, seizure detection, and sleep stage scoring are also included. In addition, its content needs to be updated considering its publication year is 2019. Similarly, the survey of Lotte et al. [23] mainly discusses the classiﬁcation algorithms for motor imagery-based BCI.

In our review, we focus on the EEG-based emotion recogntion tasks, and try to add more introduction about the up-to-date methodologies, especially various Deep Learning-based approaches that have not been systematically reviewed in these two papers. Further, we will discuss several up-to-date research problems, such as the ‘domain shift’ problem, the few-shot learning problem, etc. We also discuss potential routes in this research ﬁeld, such as the large-scale pre-trained EEG model applied in emotion recognition. In addition, other surveys only focus on speciﬁc techniques adopted in this area but neglect the holistic technical perspective. Hence, in this paper, we review from the perspective of researchers who try to take the ﬁrst step on this topic. In addition to reviewing the recent advances in the EEG-based emotion recognition research, we also provide a tutorial to guide the researchers to start from the very beginning. For example, we introduce the scientiﬁc basis of EEG-based emotion recognition in the psychological and physiological levels. Further, we categorize these reviewed works into diﬀerent technical routes and illustrate the theoretical basis and the research motivation, which will help the readers better understand why those techniques are studied and employed. At last, existing challenges and future investigations are also discussed in this paper, which guides the researchers to decide potential future research directions. We also carefully discuss various EEG segmentation strategies when discussing the evaluation methods, which need to be treated carefully but have been overlooked in related surveys. We believe this review provides valuable research references and research problems for researchers who are new to this ﬁeld. Overall, this review paper draws on the advantages of many survey articles, and is a high-quality complementation to these classical surveys.

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 3 -->

EEG based Emotion Recognition: A Tutorial and Review • 1:3 2 PRELIMINARIES AND BASIC KNOWLEDGE 2.1 Definition and quantification of emotional state

Acquiring users’ behavioral or physiological data with quantiﬁed emotional state labels is vital for statistical analysis-based psychological research and intelligent computing-based emotion recognition systems. Hence, the emotional state characterized by target samples should be eﬀectively recorded and quantitatively evaluated. All the quantitative methods of emotion can be divided into two main categories, as follows.

2.1.1 Discrete type of emotion quantification model. According to Darwin’s theory of evolution, human emotions are discrete, and they are preserved by natural selection [30]. Ekman [31] and Plutchik [32] approved the point of view of Darwin and then proposed that the emotion was composed of six or eight basic states, e.g., anger, anticipation, fear, sadness, disgust, trust, surprise, joy, etc., which could be further expanded to ﬁfteen or more types. On this basis, an improved model was put forward by scholars to improve the quantiﬁcation of emotions further. For example, the Palette Theory indicated that the basic emotional states could be further taken as Primary Colors, and then other emotional states would be generated by mixing the Primary Colors. For instance, the two basic emotions of surprise and sadness can be compounded into disappointment. Subsequently, Plutchik developed an emotion wheel representation method [33]. In addition, a tree type or hierarchical type of emotion quantiﬁcation method was proposed by Parrott and Gerrod [34]. In essence, these quantiﬁcation models can all be incorporated into the discrete-type emotion quantization models.

When building a recognition system on the discrete type of emotion quantiﬁcation model, we typically regard this task as a classiﬁcation modeling task, in which classiﬁcation models are applied and studied, including support vector machine (SVM) algorithm, K-nearest neighbor (KNN) algorithm, decision tree algorithm, etc.

2.1.2 Continuous dimensional type of emotion quantification model. The boundaries for distinguishing the emotional states are vague, and the changes and evolutions of states are continuous without breakpoint. Partitioning the emotional states into a dozen discrete types can only show the main aspects of emotion and fail in the accurate quantiﬁcation of emotional state. In addition, discrete emotional labels are not consistent among various cultures and nationalities. For example, we can not ﬁnd a corresponding translation in Polish for the emotion of ‘disgust’. Hence, the continuous dimensional type of emotion quantiﬁcation method is proposed. This quantiﬁcation method uses several mutually orthogonal basic axes to display diﬀerent dimensions of emotion, which solves the contradiction between the discrete quantiﬁcation method and the rich emotional connotation. The Valence-Arousal bipolar emotional quadrant system was put forward by Russell [35], which has been widely accepted in Aﬀective Computing. As shown in Figure 1(A), the classical two dimensions of Valence and Arousal are used to depict the Valence level and Arousal level of emotion.

EĞƵƚƌĂů

,ŝŐŚ

>Žǁ

EĞŐĂƚŝǀĞ

WŽƐŝƚŝǀĞ

dĞŶƐĞ

ŶŐƌǇ

&ƌƵƐƚƌĂƚĞĚ

ǆĐŝƚĞĚ

ĞůŝŐŚƚĞĚ

,ĂƉƉǇ

ĞƉƌĞƐƐĞĚ

ŽƌĞĚ

dŝƌĞĚ

ŽŶƚĞŶƚ

ZĞůĂǆĞĚ

Ăůŵ

ƌŽƵƐĂů

sĂůĞŶĐĞ

,ŝŐŚͲƌŽƵƐĂů͕ WŽƐŝƚŝǀĞͲsĂůĞŶĐĞ ,ŝŐŚͲƌŽƵƐĂů͕ EĞŐĂƚŝǀĞͲsĂůĞŶĐĞ

>ŽǁͲƌŽƵƐĂů͕ EĞŐĂƚŝǀĞͲsĂůĞŶĐĞ

>ŽǁͲƌŽƵƐĂů͕ WŽƐŝƚŝǀĞͲsĂůĞŶĐĞ





Fig. 1. Valence-Arousal Bipolar Coordinate System Porposed by Russell (A) and the corresponding Self-Assessment Manikins scale (B) [36].

The values (or ratings) of the Valence axis from positive to negative refer to the measurement for individuals’ happy and sad degrees. Likewise, a positive value in Arousal indicates an activated state (excitement), while the negative value indicates an unactivated state (calmness). In addition to the two standard base axes, adding more dimensions for a comprehensive measurement of emotions is feasible. The Dominance dimension represents the dominance control degree of the individual in the emotional process. When an external environment controls a user, the emotional state is at a lower dominance level (e.g., surprise, fear, etc.). Conversely, when a user can master the external environment, the emotional state is at a higher dominance level. It should be pointed out that the various discrete emotional states can be located to speciﬁc locations in the continuous dimensional state space with a one-to-one correspondence. For example, the sadness emotion is located in the low Arousal-low Dominance-low Valence coordinate space in the continuous emotional coordinate system, while the happiness emotion is located in a high Arousal-high Dominance-high Valence coordinate space. A broadly adopted method for evaluating continuous emotional states is the Self-Assessment Manikins (SAM) scale-based approach. SAM is designed by introducing the manikins into the questionnaire to visually evaluate the degree of Valence and arousal. The SAM questionnaire generally sets a discrete scale from 1 to 9, as shown in Figure 1(B).

When building a recognition system on the continuous type of emotion quantiﬁcation model, researchers can either tackle this task through classiﬁca- tion modeling or regression modeling. Brieﬂy speaking, constructing a model directly based on samples with continuous emotional ratings is a regression modeling task, in which the built model (e.g., ridge regression, recurrent neural networks) should be able to precisely predict the unknown samples’ emotional ratings. Whereas, when regarding this task as a classiﬁcation problem, researchers typically need to divide the emotional ratings into several levels, the samples are assigned with speciﬁc class labels according to at which level the emotional ratings are located. After that, classiﬁcation algorithms are trained on the labeled samples and applied to inferring the unknown samples’ emotional classes.

## 2.2 EEG activity’s specificity and neural correlate in the emotional process

The critical function of the central nervous system (brain) is to regulate the whole-body physical or psycho activities to participate in the emotional process. Intracranial EEG or non-implanted EEG can record the physiological activities of the central nervous system. For the non-implanted EEG, the EEG signals are acquired by deploying multiple electrodes on diﬀerent brain regions according to the standard 10-20 topology, as shown in Figure 2.

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 4 -->

1:4 • Li and Zhang, et al.

&ƌŽŶƚĂůůƉŚĂĂŶĚWŽǁĞƌ

>ĞĨƚ

ZŝŐŚƚ

,ŝŐŚ sĂůĞŶĐĞ

>Žǁ sĂůĞŶĐĞ ϭϬͲϮϬdŽƉŽůŽŐǇĨŽƌϯϮ'

ůĞĐƚƌŽĚĞƐWůĂĐĞŵĞŶƚ

Fig. 2. Diﬀerences between high and low Valence on lef and right frontal EEG alpha power in music listening (Note that EEG power is inversely related to activity, thus lower power reflects more activity [37]) .

The correlation between neural sources and emotions is one of the key scientiﬁc questions of cognitive neuroscience research. There are two diﬀerent views on neural sources and emotions. The locationist view postulates that some discrete emotions reﬂect the discrete anatomical structure in the brain (e.g., amygdala) [38, 39]. The distributionist view argues that no single anatomical structure uniquely specializes for individual emotion categories [40, 41]. Human emotion is a product of the cooperation of multiple cortex regions [42]. Localizing neural sources from scalp EEG is problematic. We should not assume that the electrical activity comes from the adjacent cortex. Hence, cognitive neuroscience adopts intracranial electrophysiology to study these questions. Intracranial electrophysiology-based studies provide evidence for the distributionist view. For example, negative emotions are processed in multiple brain regions. Stimulation of subcortical nuclei, the temporal lobe and gyrus, temporal-parietal junction, inferior frontal gyrus, etc, can aﬀect the perception of sadness, fear, and anger [43, 44]. The positive emotions (e.g., joy and mirth) are also processed in multiple brain regions [45, 46]. It is found that the forebrain takes part in the regulation process of emotion [47–49], and asynchronous activities would occur in diﬀerent locations of the brain during the emotional process. A higher left prefrontal activity is the reﬂection of an ‘approach model’ of emotion process (e.g., positive emotions), whereas a higher right prefrontal activity is the reﬂection of the ‘withdrawal model’ of emotion process (e.g., negative emotions) [50]. Researches on people with depression also found greater activation in the right forebrain than other brain regions.

The correlation between EEG components and various emotions is also one of the key scientiﬁc questions in cognitive neuroscience and is critical for building eﬀective recognition models. Joyful music has been reported to be positively correlated with the power energy in the theta band (4∼7 Hz) near the midline of the prefrontal cortex [51]. As shown in Figure 2, the valence and arousal of musical stimuli have been reported to correlate with frontal alpha (8∼13 Hz) asymmetry [37]. When playing happy music for subjects, the EEG activity in the left front area of the brain is more active than that in the right front area of the brain. However, the opposite result appears if playing sad music. Nevertheless, some works found no eﬀects in the alpha band and instead found a relationship in the beta-2 band (18∼22 Hz) [52]. The eﬀect of high-frequency EEG, including the Beta-2 band (18∼22 Hz), Beta-3 band (22∼30 Hz), and Gamma band (30∼45 Hz), in emotion also have been veriﬁed. The experience of happiness results in the decreases in beta-2 power in the front central regions and beta-3 and gamma power over the entire cortex. Whereas, when feeling anger, the Beta-2, Beta-3, and Gamma bands get increased power in the front of both hemispheres [53]. Subjects in the DEAP experiments produced higher gamma and frontal midline theta power while watching emotion provoking music videos [54]. Balconi and Lucchiari [55] reported the Gamma band activity is a marker of the subject’s evaluation of the Arousal dimension in emotional faces stimuli. Yang et al. [56] revealed that the network connections in the high Gamma band have signiﬁcant diﬀerences among the positive, neutral, and negative emotional states. In addition, the speciﬁc phenomena related to emotion in other brain areas and other frequency components have also been reported [57, 58].

Critical EEG bands and brain regions in recognizing emotions are also extensively studied in pattern recognition. Earlier traditional machine learning- based researches have reported that the features extracted from high-frequency bands (the Gamma and Beta bands) are more eﬀective for an algorithm to recognize both Valence and Arousal dimensions [59]. Currently, extensive Deep Learning-based recognition approaches also verify the Beta and Gamma band information are the most suitable bands for emotion recognition. For example, the diﬀerential entropy (DE) features extracted from these bands lead to a higher recognition performance compared with the other bands when adopting the deep belief networks [60] and the convolutional neural networks [61]. Even so, these studies also approve that combining the information from all the bands can achieve the best performance. Feature Selection based approaches are suitable for analyzing the key EEG variables in emotion recognition. Li et al. [62] studies the key frequency bands and channels by analyzing features selected out by the L1-norm logistic regression model. They ﬁnd the Hjorth parameter of mobility in the Beta band achieves the best performance. They also ﬁnd that the electrodes on the bilateral temporal and left anterior regions help get a higher performance for cross-subject emotion recognition, especially when the information in the beta band was utilized. Naser and Saha [63] adopt a Minimum Redundancy Maximum Relevance (MRMR) feature selection method on the asymmetrical features. Besides the Beta and Gamma bands, they also ﬁnd features selected from Alpha bands promote the Arousal and Valence classiﬁcation. Also adopting the mRMR method, Zhuang et al. [64] ﬁnd that the DE of the Gamma band have good classiﬁcation performance, and important electrodes are distributed in the bilateral temporal, the prefrontal, and the occipital regions. In addition to directly compare the performance between diﬀerent bands and regions in emotion recognition, analyzing the model weights associated with the variables is another common way. For example, Zheng and Lu [60] explore the critical EEG electrodes by analyzing the weights of the trained DBNs. The results show the lateral temporal and prefrontal brain areas activate more than other brain areas in beta and gamma frequency bands.

To sum up, it can be seen from these studies that the central nervous system is directly related to the emotional process. As an external manifestation of the brain’s cognitive psychological activity, EEG can be taken as an eﬀective measurement to study emotional psychology and provides the feasibility for studying emotion recognition technology. Nevertheless, the research ﬁndings mentioned above indicate that EEG activity’s speciﬁcity and neural correlate in the emotional process are not yet fully explored and understood. It’s better to build recognition models on EEG from all critical frequency bands and cortex regions.

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 5 -->

EEG based Emotion Recognition: A Tutorial and Review • 1:5

(PRWLRQ6WLPXOL ,PDJHV9LGHRV6RXQGV

((*$FTXLVLWLRQ

VLJQDOILOWHULQJGHQRVLQJ

DUWLIDFWUHPRYDOHWF

6LJQDO3UHSURFHVVLQJ

VWDWLVWLFDOIHDWXUHV WLPHIUHTXHQF\GRPDLQIHDWXUHV

QRQOLQHDUFKDRWLFV\VWHP

IHDWXUHVHWF

(PRWLRQ5HODWHG )HDWXUH([WUDFWLRQ

ILOWHUZUDSSHUHPEHGGLQJEDVHG

DSSURDFKHVJHQHWLFDQG HYROXWLRQDU\FRPSXWDWLRQEDVHG

DSSURDFKHVHWF

)HDWXUH6HOHFWLRQ

VWDWLVWLFDOPDFKLQHOHDUQLQJPHWKRGV

GHHSOHDUQLQJPHWKRGVIX]]\ORJLF

PHWKRGVHWF

(PRWLRQ5HFRJQLWLRQ 0RGHOLQJ	,QIHUHQFH

Fig. 3. The classical methods in the EEG based Emotion recognition study1

## 2.3 Classical research methodologies of EEG based emotion recognition studies

Classical research methodologies in this ﬁeld follow the procedure shown in Figure 3, namely applying pattern recognition models to the handcrafted emotion-related EEG features to distinguish diﬀerent emotional states. Firstly, if you want to build and validate the models on self-collected EEG data, you should design a user experiment to collect emotion-induced EEG data. There are two main categories of methods for emotion induction. The ﬁrst one aims to measure EEG during viewing emotionally provoking stimuli. Recommended stimuli include presentation of faces with emotional facial expressions, display of emotional pictures (e.g., IAPS pictures [65]), and emotionally provoking video or audio (e.g., ﬁlm, music, music video, IADS sounds [66]). The classical benchmark datasets introduced in Section 5.1 were collected under these types of stimuli. Building Virtual Reality scenes to induce emotions is reported eﬀective and has been extensively adopted in recent years. For example, Zhang et al. [67] proposed the Aﬀective Virtual Reality System, which combines IAPS, IADS, and China Aﬀective Video System (CAVS) to produce a virtual environment that would accommodate VR headset for emotion induction. Another method asks the test subject to imagine the target emotion (e.g., recalling the past experience). After each trial, self-reports of evoked emotional states are required. Then, classical methods need conducting data preprocessing for the acquired raw EEG data, based on which domain knowledge (signal processing, sequential pattern mining, emotional psychology, etc.) guided feature extraction is further conducted to distill as many emotion-related characteristics as possible. The reﬁned characteristics are called data features in machine learning that is further organized to construct the training samples. Furthermore, the features closely related to emotional state and helpful for improving the emotion recognition performance can be screened out from all the candidate features set by the feature selection method. Finally, we attempt to select various statistical machine learning models or Deep Learning models to build on the chosen features and iteratively evaluate their performance by computing the evaluation metrics until achieving the goal that the model outputs approximate the ground truth. Many classical studies that follow this research methodologies have veriﬁed the feasibility of building an emotion recognition system on EEGs. In addition, based on the classical methodologies, great advances have been made in this ﬁeld in recent years. This review will give a more detailed introduction of the classical and latest methodologies in the following sections.

## 3 EEG PREPROCESSING AND FEATURE ENGINEERING

Its high time resolution characterizes EEG. The high-sampled EEG data contains much emotion-related information, which has excellent potential for building precise and real-time recognition systems. Generally, EEG with a higher sampling rate may cover more details, however meanwhile may introduce lots of noise and increase the computation cost for signal processing, feature engineering, and modeling training. Regarding the device features and the problems mentioned above, the EEGs are usually sampled with a frequency of 256Hz, 512Hz, or 1024Hz. Theoretically speaking, a sampling frequency of 128 Hz would give a Nyquist frequency of 64 Hz, which is adequate for extracting suﬃcient emotion-related features. As discussed in Section 2.2, the Beta-2 band (18∼22 Hz), Beta-3 band (22∼30 Hz), and Gamma band (30∼45 Hz) are reported closely correlated with emotion recognition.

It is challenging to represent the emotional EEG signals eﬀectively due to the many noises embedded in EEG signals. Besides, it is diﬃcult to capture the implicit correlations between EEG and a speciﬁc cognitive process. Hence, preprocessing and feature engineering usually need to be included in the workﬂow.

## 3.1 EEG Preprocessing

EEG signals are mixed with various noises of the human body and environment, thus bringing challenges to the anti-interference and robustness of the recognition algorithm. Therefore, the collected EEG signals are not directly used to build the recognition models and systems. The research paradigm should not overlook preprocessing the signals and extracting representative features. The preprocessing for the acquired EEG data is mainly to remove EOG artifacts with a frequency less than 4Hz that caused by eye blink, ECG artifacts with a frequency about 1.2Hz, EMG artifacts with a frequency more than 30Hz, power frequency artifacts in the environment with a frequency between 50 to 60Hz, and so on. These above artifacts can be removed with the independent component analysis (ICA), discrete wavelet, or band-pass ﬁlters (such as the Butterworth ﬁlter) to retain the rhythmic components associated with the emotional activity. The ﬁltering process cannot remove all the artifacts from the EEG signals, and thus additional processing is needed. We can utilize the Artifact Subspace Reconstruction (ASR) method for enhanced artifact removal. The ASR method consists of a sliding window Principal Component Analysis (PCA), which statistically interpolates any high-variance signal components exceeding a threshold. Furthermore, the Common Average Reference (CAR) method is recommended to compute the average value over all electrodes and subtract it from each sample of each electrode [68].

1The bottom-left ﬁgure is obtained from the following web link: https://levita-lab.group.shef.ac.uk/eeg/

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 6 -->

1:6 • Li and Zhang, et al. Even though the emotion-provoking experiments strictly follow the experimental protocol, some problems may arise with the recordings from some subjects or trials due to technical issues or personal issues, resulting in incomplete or high-noise data. This kind of data is recommended to be entirely abandoned without further processing and analysis. By the way, we could choose only to select out a subset of the whole EEG channels for studying if we can determine the speciﬁc emotion-related brain areas, e.g., the forehead. Channel selection will decrease the computation cost and may increase the recognition performance.

## 3.2 Time Domain Features

The most direct method for extracting EEG features is to calculate statistics such as mean value, variance, skewness, kurtosis and peak-to-peak interval, etc., which can characterize the time-domain properties of EEG signal. Some studies also adopt the higher-order crossing (HOC) method, which calculates the number of zero-crossing points of EEG as a feature after being processed by diﬀerent ﬁlters [69, 70]. Event-related potentials (ERPs) reﬂect the underlying cognitive process, including emotion. Early ERP components have been veriﬁed to correlate with Valence [71], whereas the late ERP components have been veriﬁed to correlate with Arousal [72]. Hence, characteristics of ERP components, e.g, P100, N100, N200, P200, P300, were also taken into studies [73]. It should be noted, ERPs are obtained by averaging multiple EEG trials, which may not be feasible for online applications.

## 3.3 Frequency Domain Features

The frequency-domain attribute is a description of the signal from another perspective. Moreover, it has a better anti-interference to noise and can reﬂect the details of each component of the signal. Therefore, the frequency-domain features, e.g., the power spectral density (PSD), are widely extracted in physiological emotion calculation [60, 74]. PSD reﬂects the signal power of a speciﬁc frequency band. It is usually obtained through fast Fourier transform (FFT), by which the raw EEG signal can be decomposed into several distinct frequency bands, e.g., the Delta (1-4 Hz), Theta (4-8 Hz), Alpha (8-13 Hz), Beta (13-30 Hz), and Gamma (>30 Hz). Then the average power of a speciﬁc frequency band is computed and adopted as the feature. The power spectra density (PSD) can also be estimated using Welch’s method. For simplicity, we can directly take advantage of the MATLAB Signal Processing Toolbox2 to get this feature.

## 3.4 Time-Frequency Domain Composition Features

However, the single domain of time or frequency can not fully depict the characteristics of the signal. For the non-steady signal, the frequency components often change with the cranial neural, cognitive process. It needs a transition from static frequency component analysis to dynamic time-frequency joint analysis, for example, adopting the short-time Fourier transform (STFT) [75, 76] and wavelet analysis (e.g., discrete wavelet transform) [77, 78]. Wavelet analysis is usually considered as a type of ‘Sparse Representation’. It is good at manifesting subtle local characteristics in both signal domains. Hence, it is broadly applied to process non-steady neural signals, especially for the EEG [79]. STFT is only suitable for analyzing steady signals, and it is hard to get a high resolution simultaneously in frequency and time domain based on Heisenberg’s Uncertainty Principle. Hence, we recommend adopting wavelet analysis to extract ﬁne-grained EEG features.

The raw EEG signal is decomposed by the basis functions obtained through scaling and translating the mother wavelet. Speciﬁcally, the discrete wavelet transform (DWT) decomposes the signal into approximation and detail coeﬃcients. Approximation coeﬃcients describe the high-scale, low-frequency parts of the signal, while the detail coeﬃcients describe the low-scale, high-frequency parts of the signal. The decomposition process is an iteration process, i.e., the obtained approximation coeﬃcients of one scale can be further decomposed into more granular coeﬃcients corresponding to the next scale. This process is iterative, yielding a series of approximation coeﬃcients and detail coeﬃcients belonging to diﬀerent scales, as shown in Figure 4. The eﬀects of decomposition will be aﬀected by what kind of mother wavelet is predetermined, e.g., the Haar wavelet, Daubechies wavelet, Bior Wavelet, etc. [80]. For example, the Daubechies4-based DWT helps to extract the A5, D5, D4, D3, D2, and D1 signal components, the corresponding frequency range and decomposition level is listed in Table 1. The frequency ranges of these components and their correlation with various human states are provided.

Table 1. The Decomposition Levels and Corresponding Frequency Bands for EEG with 128Hz Sampling Rate.

Brain Wave Frequency Range (Hz) Decomposition Level Association

Delta Rhythm 0-4 A5 (0.5-4.3Hz) Deep sleep

Theta Rhythm 4-8 D5 (4.3-8Hz) Drowsiness; Creative inspiration; Deep meditation

Alpha Rhythm 8-13 D4 (8-16 Hz) Relaxed awareness; Eye closing

Beta Rhythm 13-30 D3 (16-32 Hz) Active thinking; Attention; Behavior; Settling problems

Gamma Rhythm 30-64 D2 (32-64 Hz) Sensory processing; High-level Information Processing, Certain cognitive; Motor function

Noise 64-128 D1 (64-128 Hz)

Then, the wavelet engery 퐸푁퐺푗feature and the wavelet entropy 퐸푁푇푗featuer can be computed in each frequency range according to the following formula 1 and 2, respectively, where 푗is the decomposition scale, 푘is the number of wavelet coeﬃcients. DWT can be easily obtained through utilizing the MATLAB Wavelet Toolbox3.

퐸푁퐺푗= 1

푁

푁 Õ

푘=1

(푑푗(푘)2) (1)

퐸푁푇푗= −

푁 Õ

푘=1

(푑푗(푘)2)푙표푔(푑푗(푘)2) (2)

2https://www.mathworks.com/help/signal/ref/dspdata.psd.html 3http://www.mathworks.com/help/wavelet/ref/dwt.html

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 7 -->

EEG based Emotion Recognition: A Tutorial and Review • 1:7

Ϭ͘ ϱΕϭϮϴ,ǌ

Ϭ͘ ϱΕϲϰ,ǌ

ϲϰΕϭϮϴ,ǌ

Ϭ͘ ϱΕϯϮ,ǌ

ϯϮΕϲϰ,ǌ

Ϭ͘ ϱΕϭϲ,ǌ

ϭϲΕϯϮ,ǌ

Ϭ͘ ϱΕϴ,ǌ

ϴΕϭϲ,ǌ

Ϭ͘ ϱΕϰ͘ ϯ,ǌ

ϰ͘ ϯΕϴ,ǌ

Ϭ͘ ϱΕϮ͘ ϰ,ǌ

Ϭ͘ ϱΕϮ͘ ϰ,ǌ

Ϭ͘ ϱΕϭ͘ ϱ,ǌ

ϭ͘ ϱΕϮ͘ ϰ,ǌ

>ĞǀĞůϭ

>ĞǀĞůϮ

>ĞǀĞůϯ

>ĞǀĞůϰ

>ĞǀĞůϱ

>ĞǀĞůϲ

>ĞǀĞůϳ

Fig. 4. Examples of 7-level decomposition and corresponding frequency bands of EEG with Sample Frequency of 128Hz.

In addition, several mode decomposition approaches, e.g., the empirical mode decomposition (EMD), the multiple empirical mode decomposition (MEMD) and the variational mode decomposition (VMD), are also quite suitable for the nonlinear unsteady EEG feature extraction, in which the multi- channel EEG is decomposed into multiple intrinsic mode functions (IMFs), based on which the more representational features can be extracted [81].

## 3.5 Nonlinear Dynamical System Features

  

Fig. 5. Phase diagram example for diﬀerent types of signals: A. Periodic Signal, B. White Noise Signal, C. EEG Signal

In addition to time-frequency-domain analysis, the researchers pay more and more attention to the chaotic characteristics in the neural system activities [82]. For instance, the brain and heart are considered non-linear dynamical systems. As shown in Figure 5, the neurophysiological signals present the properties of a non-linear dynamic system so that they can be studied and analyzed by the non-linear dynamic method. The fractal dimension is an index to describe the complexity and self-similarity of a chaotic non-linear system. EEG has multi-fractal dimensions [83].The brain states under diﬀerent cognitive tasks correspond to speciﬁc fractal dimension [84]. For example, Liu has found that the fractal dimension value corresponding to the high Arousal level was higher than that corresponding to the low Arousal level, so it could be used for emotion recognition [85]. In addition, the features describing the non-linear dynamical system, such as correlation dimension, approximate entropy, Lyapunov index, K-C complexity, etc., have all appeared in some studies on emotion recognition [86, 87]. One less studied property called Recurrence also reﬂects the characteristics of dynamical systems and can help to predict its evolution. Recurrence Plots accurately depict the distance correlation among trajectories in the non-linear system [88]. Hence, several studies also focus on Recurrence Plots-based EEG representation and feature extraction [89, 90]. However, the non-linear feature calculation cost is higher, which is disadvantageous to build a real-time recognition system. Moreover, its calculation is sensitive to parameter setting (such as embedded dimension, etc.). Simultaneously, the parameter setting is still needed to be studied and explored. In addition, diﬀerential entropy (DE) also is a kind of representative non-linear feature. It is the extension of Shannon entropy on continuous EEG variable 푥, which are assumed to obey the Gaussian distribution 푁(휇,휎2). Hence, it can be easily computed according to the following Formula 3.

퐷퐸= −

∫+∞

−∞

푝(푥)푙표푔(푝(푥))푑푥

= −

∫+∞

−∞

1

√

2휋휎2 푒 −(푥−휇)2

2휎2 푙표푔( 1

√

2휋휎2 푒 −(푥−휇)2

2휎2 )푑푥

= 1

2 (2휋푒휎2)

(3)

The eﬀectiveness and robustness of DE has been extensively veriﬁed in related works, and have advantage over PSD [60]. Some researches indicate that the computation of DE is equivalent to the logarithm power spectrum in a certain frequency range for a ﬁxed length signal [91]. More details about the non-linear dynamical features in EEG based emotion recognition can be found in the review paper of García-Martínez et al. [92].

## 3.6 Asymmetry Features

In addition, speciﬁc phenomena found in brain cognition studies can also be taken as the feature to infer emotional states. Some cognitive studies based on brain imaging technology have seen the lateralization phenomenon of the brain in diﬀerent locations in emotion processing [93]. Clinical studies have also found that there is the lateralization phenomenon of brain activity in the brains of patients with mood disorders such as anxiety and depression [94]. Asymmetry exists throughout the brain, and the hemispheres are not strictly symmetric in structure and function [95]. Therefore, some studies have adopted the diﬀerences in the EEG characteristics among electrodes in symmetrical positions of the brain to indicate the emotional states. For example,

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 8 -->

1:8 • Li and Zhang, et al. the Theta, Alpha, Beta, and Gamma spectral power asymmetry (SPA) derived from fourteen electrode pairs in the left and right lobes can be extracted as features [54]. The index asymmetry feature is generally obtained by calculating the diﬀerence [85, 96] or the ratio [97] of the indexes of two signal sources such as power spectrum, fractal dimension and so on. In addition, Petrantonakis and Hadjileontiadis [98] proposed the 퐴푠퐼measure by estimating the mutual information shared between the brain hemispheres and further expanded 퐴푠퐼to be applicable in the time-frequency domain.

## 3.7 Brain network Features

High-level cognition function depends on subtle cooperation between local and global brain activities and is inseparable from a network of brain neu- rons and brain regions [99]. There exist intrinsic correlations between EEG signals from diﬀerent brain regions. Researchers believe that the functional connectivity graph and the derived structural characteristics could signiﬁcantly enhance the distinctiveness of various emotions [100]. Several studies have found the eﬀectiveness of brain network indexes such as correlation, coherence, and synchronization in emotion recognition [101]. Therefore, the study of the brain from the perspective of the brain network has received widespread attention [102]. It provides a kind of ‘Graph Theory’ based research basis for studying the cognitive process of emotion. For example, Rotem-Kohavi et al. [103] analyzed several indicators, including connection density, clustering coeﬃcient through the EEG-derived brain network. As far as we know, it takes the ﬁrst step on utilizing graph theory to analyze infants’ brain processing of emotional facial expressions.

ŽƌƌĞůĂƚŝŽŶDĂƚƌŝǆ

ŚĂŶŶĞůϭΕE

ŚĂŶŶĞůϭΕE

ŽŶŶĞĐƚŝǀŝƚǇEĞƚǁŽƌŬ

EĞƚǁŽƌŬ&ĞĂƚƵƌĞƐ

ĞŐƌĞĞ

ůƵƐƚĞƌŝŶŐŽĞĨĨŝĐŝĞŶƚ͕

ŚĂƌĂĐƚĞƌŝƐƚŝĐWĂƚŚ

>ĞŶŐƚŚ

ĊĊ

ŵŽƚŝŽŶZĞĐŽŐŶŝƚŝŽŶ

DƵůƚŝͲĐŚĂŶŶĞů'

Fig. 6. Illustration of the brain network construction and the derived network features for classification [104].

The estimation and construction of brain networks are usually achieved by studying the time correlation or spectral coherence between multichannel brain signals, including cross-spectrum [105], Pearson correlation coeﬃcients, mutual information [106], synchronization likelihood [107], phase-lag index (PLI), phase-locking value (PLV) [100], Granger causality [108], etc. For example, the PLV reﬂects the mean diﬀerence between the instantaneous phases of two channels of EEGs over time. The value of PLV ranges from 0 to 1, where 0 indicates the inexistence of phase coupling, while 1 reﬂects a strict phase coupling. PLV has been veriﬁed eﬀective in evaluating the cooperation over diﬀerent brain areas [109]. Then, based on the constructed brain network, speciﬁc indicators related to network topology can be derived to build the recognition models [104], including the modularity, clustering coeﬃcient, degree (in-degree, out-degree, average-degree), characteristic path length, closeness centrality, local or global-eﬃciency, and small-world property, etc. [110] (see Figure 6). The constructed brain network reﬂects the coupling correlation between two EEG channels. Hence it is not sensitive to amplitude variations. This property reduces the inﬂuence of inter-person diﬀerence and helps to build robust and accurate EEG-based recognition models.

Table 2. List of representative EEG features extracted in related works.

Feature Type Extracted Features

Time+Frequency Domain Features 1. Peak-to-Peak Interval. 2. Mean Square Value. 3. Variance. 4. Mean Value. 5. Skewness. 6. Kurtosis. 7. 1st/2nd Diﬀerence. 8. Hjorth Parameter: Mobility, Complexity, Activity. 9. Higher-order Crossing. 10. Maximum Power Spectral Frequency. 11. Power Sum. 12. Maximum Power Spectral Density. 13. Wavelet Energy. 14. Wavelet Entropy. 15. Amplitude and latency of ERPs. 16. Shannon Entropy.

Nonlinear Dynamical System Fea- tures

1. Approximate Entropy. 2. C0 Complexity. 3. Correlation Dimension. 4. Kolmogorov Entropy. 5. Lyapunov Exponent. 6. Permutation En- tropy. 7. Singular Entropy. 8. Spectral Entropy. 9. Sample Entropy. 10. Diﬀerential Entropy. 11. Fractal Dimension. 12. Hurst Exponent. 13. Lyapunov Complexity. 14. Recurrence Plot: recurrence rate, determinism, entropy, averaged diagonal length, length of the longest diagonal line, laminarity, trappping time, length of longest vertical line, recurrence time of 1st type, recurrence time of 2nd type

Brain Asymmetry Features 1. Diﬀerence Between Channels. 2. Ratio Between Channels. 3. Asymmetry Index (AsI)

Brain Network Features 1. Correlation. 2. Coherence. 3. Clustering Coeﬃcient. 4. Degree. 5. Characteristic Path Length. 6. Local/Global Eﬃciency. 7. Connectivity Density. 8. Modularity. 9. Closeness Centrality

The representative EEG features utilized in related emotion recognition researches are listed in Table 2. Even though so many candidates handcrafted EEG features can be extracted, it should be pointed out that those traditional handcrafted features are obtained based on a quantity of domain knowledge, thus improving the learning cost of researchers, especially for those only majoring in computer science. In addition, most features of the current neural signals are based on the traditional time-series signal analysis theory and method. The correlation between those signal features and the emotional states is unknown and still needs to be explored, and the eﬀects are also limited. Furthermore, EEG variations triggered by physiologic or psychological factors can easily disturb those features, e.g., cardiac activity, eye movement, etc.

## 3.8 Feature Processing

3.8.1 Automatic Feature SelectionMethod. Automatic feature selection techniques can be categorized into ‘ﬁlter method’ based selection and the ‘wrapper method’ based selection [111]. Either way, the obtained EEG features need to be ranked according to speciﬁc criteria, e.g., by evaluating the relationship between the features and the target emotions or assessing the feature importance derived from the model parameters. The top vital features can be reserved for further model design, while the others will be abandoned [112, 113].

The ‘ﬁlter method’ based selection does not depend on the built recognition models, and its computation cost is usually less than the ‘wrapper method.’ Hence we recommend utilizing it in real-time and big-data scenarios. The most widely used ‘ﬁlter methods’ are the chi-squared (휒2) test-based approach, mutual information-based approach, ANOVA F-test-based approach, etc. The 휒2 test-based approach tests the independence of two variables by measuring

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 9 -->

EEG based Emotion Recognition: A Tutorial and Review • 1:9

the distribution diﬀerence between the feature variable and the emotion classes. Features with a higher 휒2 value have a close relationship with the target emotions that will be reserved. The mutual information is calculated to evaluate the interdependence between the speciﬁc feature and the emotions. The most representative mutual information-based approach is referred to as minimal-redundancy-maximal-relevance (MRMR) [114]. For example, by combining the MRMR selection method with the kernel function classiﬁer, the recognition performance can be improved [115]. ANOVA F-test measures the diﬀerence over multiple distributions by calculating the ratio of the between-class variance to within-class variance, which reﬂects the degree of discrepancy. Features with higher F-ratio values can better diﬀerentiate the diﬀerent emotions.

The ‘wrapper method’ needs to work with a speciﬁc machine learning model, among which the recursive feature elimination (RFE) method is one representative algorithm. It is originally designed by Guyon et al. [116] for gene selection. It works based on a sequential backward abandon scheme. The algorithm initially starts on the entire feature set. Then, some features with smaller feature weights are abandoned from the feature set. The process iterates several times until the desired objective is achieved. In addition, the highly eﬃcient L1-norm penalty-based method is also recommended. It adds an L1-norm regularization term at the end of the original loss function to encourage weight sparsity. Regularization is one strategy adopted in machine learning in case that the feature dimensions are larger than the size of the samples. It guarantees to produce small-value model parameters to prevent over-ﬁtting. We can abandon those features with 0 weight from the current feature set. According to some research ﬁndings, the L1-norm-based method has a big advantage over the L2-norm-based method when faced with lots of redundant features [117].

3.8.2 Manually Operated Feature Selection. The deﬁnitions of feature importance diﬀer with the change of the research objectives. For recognition tasks, the automatically selected features contribute to enhancing the recognition performance. However, the automatically selected features are not recommended for cognition studies to analyze cognition phenomenons. For example, Haufe et al. [118] pointed out that the research on the parameters of backward methods (multivariate classiﬁers) is not recommended in brain imaging data analysis. The derived ﬁndings may be inaccurate. Speciﬁcally, in machine learning, if several features are highly related to each other, only one feature may be reserved in model construction. Other features could be neglected by assigning relatively low weights without inﬂuencing the model performance. Simply considering the high-weight features may lose valuable information related to emotional cognition. Hence, in some studies, a manually operated feature selection method is recommended instead of the automation methods. For example, the ‘searchlight’ strategy can be adopted as an alternative method, by which you manually distill features from diﬀerent angles, e.g., electrode groups, brain regions, rhythms, feature types, etc. [62]. The features in critical brain regions or EEG rhythms have more impacts on the recognition performance.

3.8.3 Feature Smoothing. We know that EEG is a mixture of various neuronal activities in the brain and various noises from the body or environment. The features extracted from EEG will vary within short periods, but the human emotions may be relatively stable, which means the extracted features are still a not precise reﬂection of the emotional patterns. In addition, though increasing the kinds of features extracted may improve the recognition accuracy, it will introduce more noise and computational cost in feature extraction, model training, and the inference task. Regarding this, feature smoothing methods are also recommended in the feature processing process to decrease the inﬂuence of the emotion-irrelevant patterns and improve the emotion recognition accuracy without increasing the feature dimension. For example, we can ﬁrst divide EEG data into non-overlapping windows and extract features from each window, and further adopt the Savitzky-Golay smoothing method or the moving average method to smooth the features in time sequence [119, 120].

## 4 PATTERN RECOGNITION TECHNICAL ROUTES APPLIED IN THE FIELD

Emotion recognition follows the nature of pattern recognition research: judging target samples’ emotion categories based on existing data and some measurement criteria. We summarize existing pattern recognition approaches adopted in most related works using a ﬂow chart, shown in Figure 7, in which diﬀerent technical routes are clearly divided. With the rapid development of Deep Learning (DL) in graph and image processing and natural language processing, the DL-based technical route has begun to attract the attention of researchers in this ﬁeld, and existing works indeed have been proved eﬀective [121]. Hence, In this review, we pay more attention to Deep Learning-based studies. The following parts provide a summary of these technical routes and representative works.

## 4.1 Route: 0→1→2→4→11

The simplest method follows the route 0 →1 →2 →4 →11, namely setting a threshold for a speciﬁc feature, and if the feature value exceeds the default threshold, the sample is determined to belong to a particular emotional state [85]. However, the threshold is ﬁxed for the subject and depends on experience, leading to a lack of adaptability. Hence, this technical route is not mainstream, and we will not describe much on this route.

## 4.2 Route: 0→1→2→5→11

At present, machine learning have been extensively studied in this ﬁeld, including the traditional supervised learning models, e.g., discriminant analysis [101], support vector machine [70], K-nearest neighbor [78], Bayesian method [122], Random forest [123], perceptron [124], etc, as well as unsupervised learning methods such as manifold learning [74], clustering [125], and so on. Traditional statistical machine learning based approaches follow the route 0 →1 →2 →5 →11 are detailedly illustrated in Figure 3. Here are some representative approaches. Wang et al. [74] extracted two kinds of power spectrum features, two types of wavelet characteristics, and three types of nonlinear features from EEG. Afterward, they reduced the feature noise by the feature smoothing method and adopted linear discriminant analysis (LDA) to conduct feature dimension reduction. They ﬁnally utilized the linear SVM classiﬁer to classify the two types of emotions. Besides, they predicted the change trajectory of emotional states based on the manifold learning method. Jenke et al. [126] extracted time-frequency-domain features as well as channel combination features from multichannel EEGs. Furthermore, they utilized feature selection methods based on ReliefF, minimum redundancy maximum relevance (MRMR), and statistical test method with the quadratic discriminant analysis (QDA) modeling method for enhanced emotion classiﬁcation. In addition, Atkinson and Campos [115] combined the MRMR feature selection method and kernel function classiﬁer to promote the emotion recognition performance. Lan et al. [70] and Ackermann et al. [123] used SVM and random forest models, respectively, to construct recognition models based on statistical features, nonlinear features, spectral features, etc. Simultaneously, they compared the recognition eﬀects of the method for the same period data and diﬀerent periods data of users. Li et al. [127] proposed graph regular linear regression model (GRSLR), where the sparse regularization is introduced for channel selection. Besides, the graph regularization can preserve inherent manifold topology after data embedding, thus preventing model over-ﬁtting. Recently, Cheng et al. [128] proposed to use a deep forest model named Multi-Grained Cascade Forest, termed as gcForest,

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 10 -->

1:10 • Li and Zhang, et al.

Raw  EEG Data

Signal preprocessing

Deep Learing  Feature Engineering

Threshold Setting

and Comparison

Machine Learning Fuzzy

Logic

Ensemble

Learning

Emotion Recongnition

0

1

2

3

6 4 5

7

8

Meta Learning

Data Augmentation

Few-shot Learning

Cross-Domain

Learning

Domain Adaptation

Netwrok

MIDA

TCA

Fine-tuning  Pretrained Model

Maximum Classifier

Discrepancy

Knowledge Distillation

Multi-kernel Learning

Calibration and

Alignment

Aspect-oriented  Modeling and Grouping

Regularization

Joint Feature Selection

……

Data-Constrained

Learning

9

10

AutoML

11

Fig. 7. Flow Chart of the Patern Recognition Technical Routes Applied in The Field.

for EEG-based emotion recognition task. The gcForest algorithm has fewer hyperparameters and is robust to hyperparameter settings. In addition, its model complexity adapts with diﬀerent sizes of data, thus is worthy of our attention.

## 4.3 Route: 0→1→2→3→11

ZD

E

Fig. 8. Illustration of a deep belief network (DBN) consists of restricted Boltzmann machines (RBMs) and the corresponding training process.

In parts of DL-based works, the DL models are purely regarded as classiﬁers that play the same roles as the traditional machine learning models. The advantage of this Route compared with Route: 0 →1 →2 →5 →11 is the representation learning and the universal approximation property of the DL model that can nonlinearly transform the original features into any vector space [129]. For example, Zheng and Lu [60] and Thammasan et al. [130] utilized the deep belief network (DBN) to classify the EEG emotions based on the handcrafted features extracted from EEG, e.g., the PSD and discrete wavelet. The DBN is proposed by Hinton et al. [131], it builds on multiple restricted Boltzmann machines (RBMs) to solve the training problem of deep neural networks and promotes the rapid development of Deep Learning. RBMs are a two-layered artiﬁcial neural network with generative capabilities. Compared to Boltzmann Machines, RBMs are restricted in terms of the connections between the visible layer and the hidden layer. They are able to learn a probability distribution over the input data. Typically, the DBN training includes three main steps: 1) pre-train the DBN through Gibbs sampling method; 2) the DBN is transformed into an encoder-decoder network, thus ﬁne-tune the DBN through unsupervised back-propagation; and 3) train the DBN through supervised back-propagation, as shown in Figure 8.

The implicit correlations over diﬀerent channels are a signiﬁcant indicator to recognize emotions. Convolutional neural networks (CNN) are ideally suitable for processing two-dimensional data and extracting inter-channel joint information. Applying CNN to detecting emotions based on multi-channel EEG is worthy of study. Two central problems need to solve: 1) transforming the EEG data into proper representation to ﬁt the input format of the CNN model; 2) building eﬀective representation learning models based on various CNN modules for feature transformation. As shown in Figure 9, we illustrate two possible representation approaches when applying 2D CNNs. For example, Yang et al. [90] proposed one channel-frequency convolutional neural network (CFCNN), which works with the recurrence quantiﬁcation analysis (RQA). The entropy characteristics in diﬀerent EEG frequency ranges derived through RQA are taken as the input of the CFCNN model. The input frame does not reserve the channel topology information. The rows of the feature

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 11 -->

EEG based Emotion Recognition: A Tutorial and Review • 1:11

ĂŶĚ

ϭ

ĂŶĚ

Ϯ

ĂŶĚ

ϯ

Ċ

ĂŶĚ

D

ŚĂŶŶĞů

ϭ

ŚĂŶŶĞů

Ϯ

ŚĂŶŶĞů

ϯ

ŚĂŶŶĞů

ϰ

ŚĂŶŶĞů

ϱ

ŚĂŶŶĞů

ϲ

ŚĂŶŶĞů

ϳ

ŚĂŶŶĞů

ϴ͘͘͘

ŚĂŶŶĞů

E

ϮͲEE

KŶĞ,ĂŶĚĐƌĂĨƚĞĚ&ĞĂƚƵƌĞ

&ŽƌŚĂŶŶĞůϯŝŶĂŶĚϯ

ŚĂŶŶĞůͲĂŶĚϮZĞƉƌĞƐĞŶƚĂƚŝŽŶ ŚĂŶŶĞůͲdŽƉŽůŽŐǇϮZĞƉƌĞƐĞŶƚĂƚŝŽŶ

ǆŝƐ

Ǉϭ

ǆŝƐ

ǇϮ

ǆŝƐ

Ǉϯ

Ċ

ǆŝƐ

ǆϭ

ǆŝƐ

ǆϮ

ǆŝƐ

ǆϯ

ǆŝƐ

ǆϰ

ǆŝƐ

ǆϱ

ǆŝƐ

ǆϲ

ǆŝƐ

ǆϳ

ǆŝƐ

ǆϴ͘͘͘

ǆŝƐ

ǆE

KŶĞ,ĂŶĚĐƌĂĨƚĞĚ&ĞĂƚƵƌĞ &ŽƌŚĂŶŶĞůŝŶǆŝƐǆϯĂŶĚǆŝƐǇϯ

ǆŝƐ ǇD

ϮͲEE

 

Fig. 9. Two representative 2D EEG feature representation methods in emotion recognition when adopting the 2D-CNN-based approaches.

map correspond to the channels, and the columns are the extracted feature in diﬀerent frequency bands. Similarly, Tripathi et al. [132] extracted nine types of statistical EEG characteristics of signals as the input of the CNN model, and ﬁnally, the eﬀect of this method reached and exceeded those of mainstream methods. For better data representation, the input feature map can also reserve the channel spatial topology information, for example, Li et al. [61] organized the diﬀerential entropy features from diﬀerent channels as 2D sparse graphs, which maintains information of the electrode spatial topology, and ﬁnally used for CNN training and inferring. The constructed input feature maps could be comprehended as the input images. Hence the emotion recognition task can be resolved by the approaches adopted in computer vision tasks.

reshape squash

squash [18 × 18] features

matrix

[16 × 16] ×  256 channels [7 × 7]×  256D vectors

49 vectors





squash

49 vectors

Low

High

[18 × 18]  matrix

Conv with ReLU PrimaryCaps EmotionCaps

0c

1c

0 ´W

1 ´W

iu

0ˆu

1ˆu reshape

32D  vector

32D  vector

  

Fig. 10. The architecture of the CapsNet based emotion recognition model proposed by Chao et al. [133], in which the channel signal’s PSD features are mapped into the model input, namely the multiband feature matrix.

The CNNs are not good at recognizing features of input data when they are in diﬀerent orientations. Speciﬁcally, through downsampling, pooling decreases the computation cost and can ﬁt the variations in images. Nevertheless, the advantage of pooling is at the expense of neglecting precise spatial correlations between high-level parts, which is critical for recognizing objects with abundant spatial information [134, 135]. To tackle this problem, recently, a new type of neural network called Capsule Network (CapsNet) inspired by neuroscience has been proposed. The brain is organized into modules, which can be considered capsules. An artiﬁcial neuron processes scalars, a capsule deals with vectors. The CapsNet can model the implicit correlations between local parts and whole objects. Besides, the CapsNet can be trained with a faster speed and requires a fewer amount of training samples compared with the CNN model. Hence, researchers have started to introduce CapsNet into this technical route. For example, Chao et al. [133] point out the salient correspondence between the various emotions and cortex regions can be distinguished by the CapsNet. They also proposed one input representation structure, called the multiband feature matrix (MFM), which contains the topology correlation between EEG channels and the distinction of various EEG frequency ranges. Thus, it contributes to mining emotion-related information in spatial and frequency domains. The MFM-CapsNet based approach is illustrated in Figure 10, where the length and direction of each primary capsule indicate the existence and characteristic of the low-level representations correlated to emotions, respectively.

Some researchers also believe that the traditional CNN model may be not optimal for feature learning from EEG, which is discrete in the spatial domain. Besides, a closer spatial relationship may not guarantee a closer functional relationship. Hence, adopting the 2D representation and the CNN model may neglect he complex relationship among diﬀerent channels, the relationship between the functional brain network patterns and the emotion process. The graph-based description method is advantageous in extracting signals’ discriminative features in the discrete spatial domain [136], the structural representations learned from the functional connectivity graph could capture those correlation information mentioned above. For example, the graph convolutional neural network (GCNN) allows exploring the implicit correlations among the multiple graph nodes that represent the EEG channels. Similar to the approach shown in Figure 11(A), Wang et al. [100] built one typical GCNN model on the EEG derived graph. The graph is a fusion of the within-frequency functional connectivity graph (FCG) and the cross-frequency FCG. The within-frequency FCG is obtained through computing PLV for every pair of channel signals in the same frequency band, while the cross-frequency FCG does not require the signals to come from the same frequency bands. Those two graph representations are concatenated into a big graph with 푁× 푀nodes, where 푁and 푀denote the counts of the channel and the frequency band, respectively. The experiments verify that GCNN performs better than CNN on the FCG representation. In view of the dynamic process of functional network, similar to the approach shown in Figure 11(B), Song et al. [137] proposed a dynamical graph convolutional neural networks (DGCNN)

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 12 -->

1:12 • Li and Zhang, et al.

ƚϭ ƚϮ

ĊĊ

ƚ<

ǇŶĂŵŝĐĂů'ƌĂƉŚŽŶǀŽůƵƚŝŽŶĂů

EĞƵƌĂůEĞƚǁŽƌŬ

ǇŶĂŵŝĐ&ƵŶĐƚŝŽŶĂůŽŶŶĞĐƚŝǀŝƚǇ

ĊĊ

 

'ƌĂƉŚ'ĞŶĞƌĂƚŝŽŶ

'ƌĂƉŚ ĚũĂĐĞŶĐǇ

DĂƚƌŝǆ

&ĞĂƚƵƌĞƐ

ŽŶŶĞĐƚŝǀŝƚǇƐƚŝŵĂƚŝŽŶ͗  ƐƚŝŵĂƚŝŶŐŽŶŶĞĐƚŝǀŝƚǇǇŶĂŵŝĐĂůůǇďǇ>ĞĂƌŶŝŶŐ͕ ŽƌƐƚŝŵĂƚŝŶŐŽŶŶĞĐƚŝǀŝƚǇDĂŶŶƵĂůůǇǁŝƚŚ^ůŝĚŝŶŐtŝŶĚŽǁ

ďĂƐĞĚŽŶWŚĂƐĞ>ŽĐŬŝŶŐsĂůƵĞ͕ WĞĂƌƐŽŶŽƌƌĞůĂƚŝŽŶ͕ ĞƚĐ

'ƌĂƉŚŽŶǀŽůƵƚŝŽŶĂů

EĞƵƌĂůEĞƚǁŽƌŬ

WƌĞĚĞƚĞƌŵŝŶĞĚ&ƵŶĐƚŝŽŶĂůŽŶŶĞĐƚŝǀŝƚǇ

'ƌĂƉŚ'ĞŶĞƌĂƚŝŽŶ

ŽŶŶĞĐƚŝǀŝƚǇƐƚŝŵĂƚŝŽŶ͗  ƐƚŝŵĂƚŝŶŐŽŶŶĞĐƚŝǀŝƚǇDĂŶŶƵĂůůǇ

ďĂƐĞĚŽŶWŚĂƐĞ>ŽĐŬŝŶŐsĂůƵĞ͕ 

WĞĂƌƐŽŶŽƌƌĞůĂƚŝŽŶ͕ ĞƚĐ͘

'ƌĂƉŚ ĚũĂĐĞŶĐǇ

DĂƚƌŝǆ

&ĞĂƚƵƌĞƐ

Fig. 11. Two representative approaches of applying graph convolutional neural network (GCNN). A: The traditional GCNN model, the input functional connectivity graph is pre-determined and is static in the process of model training. B: The dynamical GCNN model, the functional connectivity graph continues evolving in the process of model training.

model, by which the discriminative characteristics and the functional connectivity information can be simultaneously extracted. Unlike the traditional GCNN, the adjacency matrix is not static but is adaptively updated dynamically during the DGCNN training. It is supposed that the learned adjacency matrix can capture the intrinsic correlation of the EEG channels. The graph’s vertex representation is the handcrafted features, including the DE, PSD, DASM, and RASM, extracted from ﬁve rhythms. For DE and PSD features. The performance was evaluated based on each kind of graph. The experimental results indicated the graph of DE feature guide to the best performance and outperformed the GCNN based approach.

Fig. 12. The framework of the heuristic variational pathway reasoning (VPR) method that can adaptively determine salient pathways to facilitate EEG emotion recognition [138].

Also encouraged by the research ﬁndings that connections and pathways exist between spatially-adjacent and functional-related areas during emotion expression [139, 140]. As shown in Figure 12, Zhang et al. [138] proposed a heuristic variational pathway reasoning (VPR) method that introduced random walk to generate candidate pathways along electrodes. LSTM was used to encode their ordered connectivity into high-level features of pathways that indicate between-electrode dependency to represent each pathway. They also proposed a salient pathway reasoning method, which includes two basic modules named pathway aggregation and sparse variational scaling. It can adaptively determine salient pathways to facilitate EEG emotion recognition and provide some explanation for emotion analysis. Based on the interpretable model, they explored salient interaction pathways w.r.t. diﬀerent emotions. This research sets a new SOTA for the SEED dataset.

Another similar work is illustrated in Figure 13, considering the importance of the asymmetrical information between the hemispheres in emotion cognition, one bi-hemispheric discrepancy model (BiHDM) is developed by Li et al. [141], in which two individual horizontal and vertical traversing RNNs were employed to scan all left separately- and right-hemisphere channels’ EEG features to learn the deep features of two hemispheres. Diﬀerent from the prior work in Figure 12, the electrode pathways here were predeﬁned. After the deep representations of each channel above have been obtained, they performed pairwise subtraction, division, and inner product on the paired channels on symmetric locations of the brain region as the asymmetry information between two hemispheres is supposed to be more discriminative recognizing emotions from EEG. Another RNN models the obtained asym- metric representations, and the two-directional streams information are fused for ﬁnal classiﬁcation. In addition, they added a domain discriminator into the model to extract domain-invariant data representation. Before this work, Li et al. [142] has developed a bi-hemispheres domain adversarial neural network (BiDANN) based on the same neuroscience hypothesis. They ﬁtted the cerebral hemisphere asymmetry information into the framework and took the domain adaptation. The framework has two feature extractors. Two local discriminators reduce the distribution discrepancy between the left and right hemisphere domains, respectively. Then, the global discriminator lessens the overall distribution discrepancy between two domains. The left and right hemispheric features are extracted through LSTM modules. To the best of our knowledge, for the ﬁrst time, researchers introduced the hemisphere’ asymmetry theory into the DL model design and veriﬁed that prior neuroscience knowledge is beneﬁcial for guiding the modeling training but usually neglected by prior works.

4Reprinted from [Li Y, Wang L, Zheng W, et al. A novel bi-hemispheric discrepancy model for eeg emotion recognition. IEEE Transactions on Cognitive and Developmental Systems, 2020, 13(2): 354-367] with the permission of IEEE Publishing.

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 13 -->

EEG based Emotion Recognition: A Tutorial and Review • 1:13

Fig. 13. Handcrafed feature based bi-hemispheric discrepancy information integrated model (BiHDM)4 [141]. BiHDM utilizes four RNNs to capture the information of EEG channels on each hemisphere from horizontal and vertical streams.

## 4.4 Route: 0→1→3→11 and 0→3→11

The approaches mentioned above take handcraft feature maps as the input, somewhat underestimate DL’s ‘end-to-end’ representation learning ability, actually disagrees with the data-driven model building philosophy in Deep Learning, the handcrafed representation may lose lots of precious information implied in raw EEGs.





Fig. 14. End-to-end bi-hemispheric discrepancy information integrated model. A: BiDCNN5 [143], B: RACNN6 [144].

To tackle this issue, similar to the hypothesis of brain asymmetry in emotional processing adopted in the BiHDM and BiDANN models mentioned above, as shown in Figure 14(A), Huang et al. [143] proposed an end-to-end bi-hemisphere discrepancy convolutional neural network model (BiDCNN) that recognize the diﬀerent emotions based on the asymmetry information between the two hemispheres. They transformed the multi-channel EEGs into 2D frames with a shape of 9 × 9, which reserves the knowledge of channel topology. Three diﬀerent kinds of feature frames are proposed, namely are the original EEG value matrix (OEFM), the bi-hemisphere symmetric matrix (BiSSM) derived by subtracting the symmetrical electrode pairs’ values, and the bi-hemisphere division symmetric matrix (BiDSM) derived by dividing the symmetrical electrode pairs’ values. In BiDCNN, a 2D convolutional layer is utilized to learn from each of the three preprocessed data. Another end-to-end regional-asymmetric convolutional neural network model (RACNN) was proposed by Cui et al. [144]. As shown in 14(B), it consists of three parts of feature learners to extract temporal, regional, and asymmetric features, respectively. Three-dimensional convolution functions are utilized in temporal feature extractors to mine time-frequency characteristics. The regional feature extractor uses two-dimensional convolution functions to mine regional characteristics from neighboring electrodes. At last, the asymmetric diﬀerential layer (ADL) is designed to capture long-distance information between symmetric positions. The original multi-channel EEGs are transformed into the 3D tensor 푋, which reserves the topology information of the electrodes.

DƵůƚŝͲĐŚĂŶŶĞů

'ĂƚĂ

ϮŽŶǀŽůƵƚŝŽŶĂů

>ĂǇĞƌ

ϮĞƉƚŚǁŝƐĞ ŽŶǀŽůƵƚŝŽŶĂů>ĂǇĞƌ

Ϯ^ĞƉĂƌĂďůĞ ŽŶǀŽůƵƚŝŽŶĂů>ĂǇĞƌ

ůĂƐƐŝĨŝĐĂƚŝŽŶ

>ĂǇĞƌ

Fig. 15. The end-to-end 2D convolutional neural networks based spatial-temporal Deep Learning model (EEGNet) [145], in which the input EEGs are randomly arranged into a 2D frame.

5Reprinted from [Huang D, Chen S, Liu C, et al. Diﬀerences ﬁrst in asymmetric brain: A bi-hemisphere discrepancy convolutional neural network for EEG emotion recog- nition[J]. Neurocomputing, 2021, 448: 140-151] with the permission of Elsevier Publishing. 6Reprinted from [Cui H, Liu A, Zhang X, et al. EEG-based emotion recognition using an end-to-end regional-asymmetric convolutional neural network. Knowledge-Based Systems, 2020, 205: 106243] with the permission of Elsevier Publishing.

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 14 -->

1:14 • Li and Zhang, et al. Furthermore, as shown in Figure 15, Lawhern et al. [145] designed an EEG-speciﬁc ConvNet model (EEGNet) by integrating depthwise and separable convolutions. Even though the original EEGNet was only validated on the motor imagery classiﬁcation tasks, its idea was further veriﬁed and compared with the EmotioNet model proposed by Wang et al. [146], which adopted the 3D EEG representation method shown in 17(B). Islam et al. [147] proposed one eﬃcient recognition method with lower computational complexity, lower memory requirement, and lower time consumption. Only applying the traditional CNN model to the channel correlation matrix of Pearson’s correlation coeﬃcient can achieve ideal performance. Inspired by the works shown in Figure 10, Liu et al. [135] developed one end-to-end CapsNet based approach that builds directly on the raw EEG signals and judge the emotions. It has three modules, namely, ConvReLU, PrimaryCaps, and EmotionCaps. Compared with the prior MFM-CapsNet approach, it works without the need for any feature design and extraction stages. It incorporates multi-level learned representations into the primary capsules.

Fig. 16. The fluctuation of the ground truth emotion during one stimulus trial that leads to the problem of unreliability of the ground truth emotional label7 [146].

One drawback of the approach mentioned above is it’s only suitable for processing short input signal segments with only a few second lengths. The dependencies of a long trial signal can not be fully mined. Hence, In addition to the ‘end-to-end modeling’ problem, researchers also pay attention to the ’context modeling’ problem to mine long signal dependencies. Speciﬁcally, the works mentioned above are only suitable for modeling global static information. Nevertheless, the human’s emotional cognitive process is not static but continuously evolving. As shown in Figure 16, the subjects’ speciﬁc emotions generally evolve over the experiment with the ﬂuctuations of the EEGs. Hence, the reported so-called ground truth emotional label of one trial only reﬂects their overall evaluation of their emotional experience. The temporal and ﬂuctuant property of the EEG has been neglected in several prior related works. Contextual learning ability should be considered in the DL model study.

ŚĂŶŶĞůͲdŽƉŽůŽŐǇͲdŝŵĞϯZĞƉƌĞƐĞŶƚĂƚŝŽŶ

ǆŝƐ

Ǉϭ

ǆŝƐ

ǇϮ

ǆŝƐ

Ǉϯ

Ċ

ǆŝƐ

ǆϭ

ǆŝƐ

ǆϮ

ǆŝƐ

ǆϯ

ǆŝƐ

ǆϰ

ǆŝƐ

ǆϱ

ǆŝƐ

ǆϲ

ǆŝƐ

ǆϳ

ǆŝƐ

ǆϴ

ǆŝƐ

ǆE

dŚĞ'^ŝŐŶĂůsĂůƵĞŽĨ ŚĂŶŶĞůŝŶǆϯ͕ ǇϯŝŶdŝŵĞϭ

ǆŝƐ

ǇD

ϯͲEE

ǆŝƐ

Ǉϭ

ǆŝƐ

ǇϮ

ǆŝƐ

Ǉϯ ǆŝƐ

ǆϭ

ǆŝƐ

ǆϮ

ǆŝƐ

ǆϯ

ǆŝƐ

ǆϰ

ǆŝƐ

ǆϱ

ǆŝƐ

ǆϲ

ǆŝƐ

ǆϳ

ǆŝƐ

ǆϴ

ǆŝƐ

ǆE

ǆŝƐ

ǇD

dŝŵĞŝŵĞŶƐŝŽŶ

ŚĂŶŶĞůͲdŝŵĞͲ&ƌĂŵĞϯZĞƉƌĞƐĞŶƚĂƚŝŽŶ

dŝŵĞ

ϭ

dŝŵĞ

Ϯ

dŝŵĞ

ϯ

Ċ

ŚĂŶŶĞů

ϭ

ŚĂŶŶĞů

Ϯ

ŚĂŶŶĞů

ϯ

ŚĂŶŶĞů

ϰ

ŚĂŶŶĞů

ϱ

ŚĂŶŶĞů

ϲ

ŚĂŶŶĞů

ϳ

ŚĂŶŶĞů

ϴ͘͘͘

ŚĂŶŶĞů

E

dŚĞ'^ŝŐŶĂůsĂůƵĞŽĨ ŚĂŶŶĞůϯŝŶdŝŵĞϯŽĨ&ƌĂŵĞϭ

dŝŵĞ

D

ϯͲEE

͘͘͘

ŽŶĐĞĐƵƚŝǀĞ ^ŝŐŶĂů&ƌĂŵĞƐ

ŚĂŶŶĞůŝŵĞŶƐŝŽŶ

ŚĂŶŶĞů

ϭ

ŚĂŶŶĞů

Ϯ

ŚĂŶŶĞů

ϯ

ŚĂŶŶĞů

ϰ

ŚĂŶŶĞů

ϱ

ŚĂŶŶĞů

ϲ

ŚĂŶŶĞů

ϳ

ŚĂŶŶĞů

ϴ

ŚĂŶŶĞů

E

dŝŵĞ

ϭ

dŝŵĞ

Ϯ

dŝŵĞ

ϯ

dŝŵĞ

D

&ƌĂŵĞ<

&ƌĂŵĞϭ

ĊĊ

dŝŵĞ<

dŝŵĞϭ

 

Fig. 17. Two representative 3D EEG representation methods in emotion recognition when adopting the 3D-CNN-based approaches. A: The raw multi- channel EEGs are randomly arranged into a 2D frame and 3D cube [148]. B: The raw multi-channel EEGs are arranged into a 2D frame and 3D cube according to the 10-20 topology of electrodes [146, 149].

Various types of recurrent neural network (RNN) have been successfully applied in EEG-based emotion recognition, including the GRU, the LSTM, and the simple recurrent units (SRU). For example, Wei et al. [151] proposed to use ensemble SRU networks to learn from the features sequences of diﬀerent EEG rhythms obtained through wavelet transform. Although the recurrent neural networks (RNN) is good as sequential modeling tasks, you also can conduct end-to-end contextual learning only based on CNN without the help of the RNN. Utilizing 3D CNN for sequence modeling has been extensively explored in video analysis, e.g., action recognition [152]. Hence, inspired by those studies, 3D CNN also has been introduced into this area. For example, Salama et al. [148] proposed one 3D-CNN model that multi-channel EEGs are randomly arranged into frames. As shown in Figure 17(A), consecutive frames are further concatenated together into one 3D cube. Besides, since those current open-source EEG datasets do not collect enough trials for each subject, the data augmentation strategy is adopted by adding white Gaussian noise to the original signals. The eﬀectiveness of the 3D-CNN on long sequence modeling is veriﬁed in this work. Wang et al. [146] also proposed one 3D CNN model, called EmotioNet, which integrates batch normalization and dense prediction mechanism for resolving issues of covariance shift and the unreliability of ground truth labels. Speciﬁcally, as shown in Figure 17(B),

7Reprinted from [Wang Y, Huang Z, McCane B, et al. EmotioNet: A 3-D convolutional neural network for EEG-based emotion recognition. 2018 International Joint Conference on Neural Networks (IJCNN). IEEE, 2018: 1-7] with the permission of IEEE Publishing.

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 15 -->

EEG based Emotion Recognition: A Tutorial and Review • 1:15

Fig. 18. End-to-end 1D-CNN model TSception8 [150], which consists of two types of 1D convolution based learners: temporal learner and spatial learner. Correspondingly, the channels in the input are deliberately arranged according to the lef and right hemispheres.

they transformed the 2-D frames (channels × time) into 3-D cubes (channel topology × time ) as the input fed to the model. The ﬁrst two layers employ 3-D convolution to learn spatial and temporal characteristics, then followed by a fusion operation, which fuses these learned high-level representations. Consequently, the output of this layer only has temporal characteristics, which are fed into the following two layers to conduct high-level temporal representation learning. At the end of the model, a dense prediction is utilized to make a time-varying emotion state prediction. Experiments show that the EmotioNet performs better than the aforementioned 2D EEGNet (see Figure 15) proposed by Lawhern et al. [145]. Jia et al. [153] proposed one spatial- spectral-temporal-based attention 3D dense network, called SST-EmotionNet, which consists of the spatial-spectral stream and spatial-temporal stream. Each stream consists of several attention-based 3D dense blocks. In the end, the two parallel streams are fused for classiﬁcation. Although the EmotioNet and SST-EmotionNet seem alike in name, they are diﬀerent models. In addition, the input of SST-EmotionNet is diﬀerential entropy feature-based 3D representation instead of raw EEG signals that the EmotioNet can process. Hence, it may be the weakness of the SST-EmotionNet. Cho and Hwang [149] also introduced two types of 3D-CNN models, namely C3D and R(2 + 1)D. They adopted the 3D EEG representation method shown in Figure 17(B). The input raw EEGs are arranged into 2D frames according to electrode topology, and the interpolated 2D EEG frames are further concatenated into 3D cubes. Unfortunately, the aforementioned 3D CNN-based approaches only veriﬁed on the few second long sequences. Conducting consecutive 1D-CNN operations also could eﬀectively extract spatial-temporal information from raw multichannel EEGs. Inspired by the Inception block of GoogleNet, Ding et al. [150] proposed the TSception model. As shown in Figure 18, it consists of two types of 1D convolution-based learners for end-to-end temporal- spatial information modeling. Correspondingly, the channels in the input frame are deliberately arranged according to which hemisphere they locate. Then the spatial learner adopts a multi-scale 1D convolution operation to learn the asymmetry features from both hemispheres. The temporal learner adopts multi-scale 1D convolution operations that help to extract multiple temporal and frequency patterns.







Fig. 19. Three representative CNN-RNN hybrid models. A: The CRNN hybrid DL model proposed by Li et al. [154] that the input data representation are 2D wavelet scalogram representation9. B: The cascade hybrid model introduced by Zhang et al. [155] that similar with the CRNN model, but the input are original EEG signal and reserves the channel spatial topology information. C: The parallel hybrid model also introduced in work of Zhang et al. [155]. The spatial-temporal features are extracted in parallel by CNN and LSTM, respectively, and fused for final recognition.

Integrating both the ability of CNN and LSTM to build hybrid Deep Learning models is a natural choice. For example, as shown in Figure 19(A), Li et al. [154] propose a wavelet transformation-based preprocessing that transforms the multi-channel EEG into scalogram based 2D frame representation. Each frame reﬂects the energy distribution of the multi-channel EEG in a time slice. Further, they designed one hybrid DL model, called C-RNN, which fuses CNN and RNN. Speciﬁcally, the CNN module can decode inter-channel relationships, and the RNN (LSTM) module helps capture contextual information from sequential data. Even though this work does not achieve very high performance, this work contributes to the further development of end-to-end and

8Reprinted from [Ding Y, Robinson N, Zeng Q, et al. Tsception: a deep learning framework for emotion detection using EEG. 2020 International Joint Conference on Neural Networks (IJCNN). IEEE, 2020: 1-7] with the permission of IEEE Publishing. 9Reprinted from [Li X, Song D, Zhang P, et al. Emotion recognition from multi-channel EEG data through convolutional recurrent neural network. 2016 IEEE international conference on bioinformatics and biomedicine (BIBM). IEEE, 2016: 352-359] with the permission of IEEE Publishing.

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 16 -->

1:16 • Li and Zhang, et al. hybrid EEG emotion recognition models. Zhang et al. [155] introduce cascade (see Figure 19(B)) and parallel (see Figure 19(C)) hybrid DL models integrate CNN and RNN, in which the input is the raw EEG signal arranged according to electrode topology, each input map corresponds to a signal timestamp. The model can eﬀectively learn the joint spatio-temporal representations from raw EEGs, the complex dependencies between adjacent signals, and the contextual information can be fully mined. For cascade model, it follows the same mechanism as the works shown in Figure 19(A). It ﬁrst learns the spatial representation from each data frame, and the sequence of the learned spatial representations is further carried to the RNN to learn temporal representations. Unlike the cascade structure-based model, the parallel structure-based model learns the spatial and temporal representations from EEG parallelly. At last, the concatenated representations are utilized for ﬁnal recognition. Both the cascade and parallel models consistently outperform the SOTA methods. Almost at the same time, a similar parallel hybrid model is proposed by Yang et al. [156]. They introduce a preprocessing method that removes the non- stimulus pre-trial baseline signal from the stimulus trial signal. Based on the preprocessed data, the parallel hybrid model’s accuracy is greatly improved by 32%. Attention is a special mechanism in the information processing of the human brain, hence, inspired by those neuroscience ﬁndings, Tao et al. [157] introduced attention mechanisms into the aforementioned CNN-LSTM hybrid DL models. They integrated channel-wise Attention and self-attention into the CNN and RNN, respectively, to learn attention characteristics among the channels and the attention characteristics within a sequence. There are several potential weaknesses in the works mentioned above: Firstly, both the cascade and parallel models mentioned above require a 2D representation of EEG channels. If we represent them according to their topology, it may cause information loss because channels are actually arranged in the 3D space, and the 2D frame has multiple positions of the null electrodes that need to be padded with zeros. Secondly, these approaches utilize RNNs to capture inter-channel and inter-time relations. However, each 2D frame corresponds to a time step rather than a time window. Hence, if the signal is extremely long with a high sampling frequency, the model computation burden will be largely increased, especially for RNN models. Thirdly, such a two-stage approach is somewhat inconvenient to implement. The whole process is time-consuming and highly dependent on domain knowledge. Hence, developing approaches modeling directly on the original multi-channel EEGs regardless of considering the topology is worth studying.

Fig. 20. The framework of LSTM based model R2G-STNN10. The region to global (R2G) process includes two streams. The spatial stream constructs the relation in and among all the brain regions hierarchically, while the temporal stream captures the EEG signal’s dynamic information as well as learning from the brain regions’ time sequences [158].

When building a spatial-temporal model, the spatial information can also be eﬀectively processed by the RNN model without the help of CNN. For example, Zhang et al. [159] designed a spatial-temporal hybrid DL model called STRNN that only integrated RNN modules. It utilized RNN to learn the temporal dependencies and to capture the spatial dependencies in the multi-channel context. Firstly, a quad-directional spatial RNN (SRNN) layer scans each slice from diﬀerent angles. Following the SRNN, a bi-directional temporal RNN layer (TRNN) learns the long-term temporal dependencies by the forward and backward processing of the sequences. Li et al. [158] proposed one LSTM based regional-to-global brain spatial-temporal neural network model (R2G-STNN) that realizes the regional to global hierarchical feature learning. A bidirectional long short-term memory (BiLSTM) network was adopted to learn spatial characteristics to model the regional correlations among EEG channels. Further, the regional attention layer is also introduced in the R2G-STNN model to diﬀerentiate the importance of diﬀerent brain regions in the emotion process. The attention layer learns and assigns weights to increase or reduce the inﬂuence of diﬀerent regions. At last, BiLSTM is adopted to learn the temporal dependencies of regional and global spatial representations. This work also adds one discriminator to solve the domain shift problem. Lew et al. [160] proposed one regionally-operated domain adversarial network (RODAN) based on the GRU-RNN model and attention mechanism that considers the spatial-temporal relationships among brain regions and across time as well as resolves the distribution shift between training and testing data by integrating the domain adversarial network.

Li et al. [161] introduced a raw EEG decoding-based recognition approaches. Speciﬁcally, they hypothesize that the EEG signals are a mixture of the multiple latent signals produced by the internal brain processes. Hence, the automatically learned representation of the source signals must contribute to building robust recognition models. They ﬁrst utilized diﬀerent AutoEncoder-like networks, including stacked AutoEncoder (non-generative model),

10Reprinted from [Li Y, Zheng W, Wang L, et al. From regional to global brain: A novel hierarchical spatial-temporal neural network model for EEG emotion recognition. IEEE Transactions on Aﬀective Computing, 2019] with the permission of IEEE Publishing.

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 17 -->

EEG based Emotion Recognition: A Tutorial and Review • 1:17

sϭ sϮ sϯ sŶͲϭ sŶ

,ϭ ,Ϯ ,ŵ

yϭ yϮ yϯ yŶͲϭ yŶ

t

Kϭ KϮ Kϯ KŶͲϭ KŶ

Ǉϭ ǇϮ Ǉϯ ǇŶͲϭ ǇŶ

DƵůƚŝĐŚĂŶŶĞů'Ɛ

ĞĐŽĚĞĚDƵůƚŝĐŚĂŶŶĞů'Ɛ

/DWHQWIDFWRUV ZĞĐƵƌƌĞŶƚEĞƵƌĂů

EĞƚǁŽƌŬ

ƵƚŽŶĐŽĚĞƌ͕ sĂƌŝĂƚŝŽŶĂůƵƚŽŶĐŽĚĞƌ͕ ZĞƐƚƌŝĐƚĞĚŽůƚǌŵĂŶŶDĂĐŚŝŶĞ͕ ĞƚĐ͘

Fig. 21. Illustration of a hybrid model that fuses unsupervised decoding of latent source factors and the recurrent neural network (RNN).

restricted Boltzmann machines (generative model), and variational AutoEncoder (generative model) to decode the source signals from the raw EEGs, then further utilized the LSTM for sequence learning and emotion recognition. One weakness of this work is the input sequences for LSTM processing are a sampled sequence of the entire decoded latent source signals that reduce the computation cost meanwhile will produce information loss. A similar AE+LSTM model was also proposed, whereas handcrafted feature extraction is needed to construct sequence before fed into the LSTM model [162] that also may lead to information loss. They are not strict end-to-end models, still need extracting intermediate latent EEG source signals. Such a two-stage approach is somewhat inconvenient for practical application.

ƚϮ

ĊĊ

ƚ<

'ƌĂƉŚŽŶǀŽůƵƚŝŽŶĂů

EĞƵƌĂůEĞƚǁŽƌŬ

ǇŶĂŵŝĐ&ƵŶĐƚŝŽŶĂůŽŶŶĞĐƚŝǀŝƚǇ

ĊĊ

'ƌĂƉŚ'ĞŶĞƌĂƚŝŽŶ

'ƌĂƉŚ ĚũĂĐĞŶĐǇ

DĂƚƌŝǆ

&ĞĂƚƵƌĞƐ

ŽŶŶĞĐƚŝǀŝƚǇƐƚŝŵĂƚŝŽŶ͗  ƐƚŝŵĂƚŝŶŐŽŶŶĞĐƚŝǀŝƚǇDĂŶŶƵĂůůǇǁŝƚŚ^ůŝĚŝŶŐtŝŶĚŽǁ ďĂƐĞĚŽŶWŚĂƐĞ>ŽĐŬŝŶŐsĂůƵĞ͕ WĞĂƌƐŽŶŽƌƌĞůĂƚŝŽŶ͕ ĞƚĐ

ZĞĐƵƌƌĞŶƚEĞƵƌĂůEĞƚǁŽƌŬ

'ƌĂƉŚŽŶǀŽůƵƚŝŽŶĂů

EĞƵƌĂůEĞƚǁŽƌŬ

'ƌĂƉŚŽŶǀŽůƵƚŝŽŶĂů

EĞƵƌĂůEĞƚǁŽƌŬ

Fig. 22. Illustration of a hybrid model that fuses graph convolutional neural network (GCNN) and RNN.

As mentioned in Route: 0 →1 →2 →3 →11, the graph neural networks (GNN) is capable of decoding the intrinsic correlations among the multi-source signal. Nevertheless, the functional connectivity between two channels is not static but continuously changing with the evolution of the emotional process. Hence, developing GNN based models that can capture the functional connectivity change between EEG channels may greatly enhance the emotion recognition eﬀect. Combining the GNN model with some sequence modeling methods is one direct way, which is similar to the ideas shown in Figure 19. For example, Yin et al. [163] proposed one hybrid DL model (named ECGGCNN) that integrates GCNN and LSTM. The GCNN module helps to learn the channel connectivity within a time slice. A parallel GCNN computing mode is designed to receive data frames in sequential order and transports the learned representations to the LSTM layer, which is used to model the evolution of the channel connectivity. At last, the dense layer predicts ﬁnal emotions according to the LSTM’s learned contextual information.

Filter Bank

DE 1 & PSD 1 Filtered Signal 1

Filtered Signal 2

Filtered Signal H

SCM 1

DE 2 & PSD 2

SCM 2

DE H & PSD H

SCM H

DE&PSD Block

Tangent Space Learning

MLP Block

Soft  Attention

Fusion Strategy

FC

FC

Dimensionality Reduction

Riemannian Manifold

LSTM Block

Vectorization

Euclidean Space

LSTM Block

LSTM Block

Multichannel EEG

Concatenation

Concatenation

Afﬁne-invariant Distance

Choice of Reference

Fig. 23. A temporal-spatial EEG information Riemannian fusion network (RFNet) for aﬀective BCI [164].

Traditional BCI solutions rely on Riemannian geometry, in which the spatial covariance matrices (SCM) derived from raw EEGs contribute to developing BCI algorithms. As the SCM is symmetric positive deﬁnite, it lies in Riemannian space rather than the Euclidean space, the models designed in Euclidean space can not be directly employed [165]. To tackle this problem, as shown in Figure 23, Zhang and Etemad [164] proposed one end-to-end Riemannian

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 18 -->

1:18 • Li and Zhang, et al. fusion network (RFNesst), which separately extract spatial representation in the Riemannian space and temporal representation in the Euclidean space. Finally, the attention strategy guides the fusion of diﬀerent learned embeddings. One key operation is mapping the spatial representations extracted from SCM in Riemannian space to the embeddings in Euclidean space through tangent space learning. Finally, an MLP is connected to process the spatial information. For the temporal representation learning in Euclidean space, they utilize the attention-LSTM network to learn from the EEG frequency sub-bands. The learned temporal representation is transported forward to a fully connected layer to get the high-level representations. At last, the latent spatial and temporal representations in Euclidean space are concatenated for ﬁnal emotion recognition tasks.

Though lots of works mentioned above adopted the RNN based approaches, they do not talk about the computation cost. Actually, the RNNs tend to be more computationally intensive than CNNs, especially when the target sequence is quite long. The reason for that is because RNNs are very memory intensive with backpropagation through time.

## 4.5 Route: 3→7→11 and 5→7→11

We hope the developed AI system can have consistent and robust performance on a wide range of data domains. Nevertheless, the diﬀerence in data distribution among users would result in degraded recognition performance. For example, Kim and André [166] ﬁrstly built a subject-dependent model with the speciﬁc user data, the 4-class emotion recognition rates can reach 95% on intra-subject data. However, when one subject-independent recognition model was established with the mixed data of three users, the data distribution deviation among three users caused the recognition accuracy to be reduced to 70%, suggesting the simple and crudely built user-independent models will inevitably have low robustness. Likewise, Petrantonakis and Hadjileontiadis [98] veriﬁed the proposed method in the speciﬁc individual data and non-speciﬁc individual data, respectively. The experimental recognition accuracy of the subject-dependent model was 70%∼100%, while for the subject-independent model, the performance decreased to 10%∼20%. AlZoubi et al. [167] analyzed the physiological signals of 27 students under eight kinds of emotions. They found that the consistency of emotional physiological response patterns of diﬀerent individuals was poorand even proposedthat user-independent modeling methods were not feasible in EEG-based emotion recognition research.

This problem is typically referred to as ‘domain shift’. The EEG data exhibit ‘domain shift’ problems due to various factors. The diﬀerences among source users (such as gender, culture, gene, etc.) would lead to diﬀerent neurophysiological activity patterns. Some studies have shown that the asyn- chronous activity of the brain presents diﬀerent patterns in diﬀerent individuals [168]. Regarding gender factors, there has been a tremendous amount of research on the diﬀerence between men and women in processing emotional stimuli. For example, researchers found that men and women showed diﬀerent scalp activity patterns and distributions in processing emotional information of music [169]. Bilalpur et al. [170] adopted the EEG to examine the gender diﬀerence in facial emotion recognition. They found that women were more sensitive and faster to recognize negative emotions than men, irrespective of age, even when only partial information was provided. Goshvarpour and Goshvarpour [171] assessed EEG powers in depressing, fun, and sad music videos for women’s and men’s groups, respectively. They found the mean power of all frequency bands in the women’s group was signiﬁcantly higher than that of the men’s group. There were signiﬁcant gender-related diﬀerences in parietal lobe activation for depressing and sad music videos and limbic lobe activation for fun stimuli. It is believed that biological and sociocultural factors cause the diﬀerences [172]. In terms of biological factors, Lee et al. [173] revealed that the right insula and left thalamus were consistently activated for men but not for women during the emotional experience. They also suggested that men evaluate current emotional experiences by recalling past emotional experiences, whereas women tended to evaluate current emotional experiences rapidly according to the immediate stimuli. In terms of the genetic factor, Raab et al. [174] revealed that serotonin transporter gene (5-HTTLPR) polymorphisms are closed correlated with brain activation during facial emotion processing. In terms of sociocultural factors, women socialize diﬀerently than men, which is not decided by genetic factors but by social norms deﬁned by politics, culture, and religion [175]. In Western culture, at least, women are more emotional than men and more reactive to unpleasant events [172]. Zhu et al. [176] studied the cross-gender EEG modeling, the recognition performance of female models is better than male models. It indicates that women share more stable EEG patterns during emo- tional experience than men. Pava et al. [177] conducted a special study on the gender diﬀerences present in the EEG-based emotion recognition system. They found the gender diﬀerences in the classiﬁcation performance, the gender diﬀerences in diﬀerential entropy features extracted from EEG, and the gender diﬀerences in evaluating the emotion experienced in the Valence dimension. Regarding cultural factors, Huang [178] studied the evaluation of emotional images by Chinese and foreign groups. The ﬁnding showed that the viewpoint diﬀerence between Western and Chinese users would lead to large diﬀerences in emotion evaluation. Kurbalija et al. [179] conducted experiments with several Serbian and Chinese subjects. They observed that cul- tural diﬀerences between the subjects did not signiﬁcantly impact the recognition tasks and models. Nevertheless, Gan et al. [180] found that French has higher mean accuracy on beta frequency band while Chinese tends to perform better on gamma frequency band on tasks of recognizing emotions. They also found similarities and diﬀerences in connectivity patterns between Chinese and French subjects. Hence, we can not say the demographic factors will not aﬀect the model building. We should pay more attention to the these factors in developing and assessing EEG-based emotion recognition systems.

The domain shift problem will appear not only in diﬀerent sources of EEG data, but they could also appear in the same source of EEG. Take the DEAP dataset for example, as shown in Figure 24(A), the instantaneous distribution of EEG continuously evolves that causing the data non-stationarity issues. The reason lies in the mental change of a participant or the technical factors, e.g., drying electrode gel changes. Therefore, the distributions of diﬀerent epochs might be diﬀerent. As shown in Figure 24(B), inter-subject variability also is a representative domain shift problem, which indicates there also exist discrepancies among the statistical characteristics of diﬀerent subjects.

Though much research has studied subject-dependent modeling, the construction of a user-independent recognition system can meet practical appli- cation requirements. This drives the relevant researchers to focus on and improve the eﬀect of user-independent approaches. At present, there are mainly four ways to solve the above problems, as follows:

(1) One way is calibrating or aligning the physiological signals among the participants. The calibration-based methods reduce the diﬀerence in physio- logical measurement among the participants by using the baseline characteristics of participants. For example, Mohammad and Nishida [181] calibrated the level of physiological signals of each participant and took the physiological characteristics at calm state as baseline characteristics. The physiological characteristics under various emotional states subtract the baseline characteristics to obtain the calibrated characteristics. Then, the relative physiolog- ical characteristics were used to establish the prediction model of emotion and obtained a good experimental eﬀect. The alignment-based methods are widely employed in brain-computer interface studies. Researchers proposed to align the multichannel EEGs of the source domain and target domain in the common Riemannian manifold space and judge the states according to the Riemannian distance between each state center and the EEG covariance matrix [182]. Fernandez et al. [183] studied diﬀerent feature normalization methods combined with the deep neural network. The results show that

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 19 -->

EEG based Emotion Recognition: A Tutorial and Review • 1:19

##  

Fig. 24. Domain shif problems in DEAP data set11. A: non-stationary EEG distribution between two epochs. B: inter-subject EEG variability under the same trial [146].

the proposed stratiﬁed normalization-based neural network signiﬁcantly outperforms batch normalization-based approaches in cross-subject emotion recognition settings.

(2) Another way is to establish aspect-oriented models according to speciﬁc factors that cause domain shift. Zhou et al. [184] established culture-speciﬁc model and gender-speciﬁc model for 46 participants, as well as compared their performance with the general models. The experiments showed that the speciﬁcities in gender and culture would aﬀect recognition performance. The emotion model built on the user of the same culture or gender speciﬁcity improves the recognition accuracy. Similarly, Bailenson et al. [185] introduced the individual-speciﬁc model, gender-speciﬁc model, and general model, respectively. The experiments suggested that the individual-speciﬁc model and gender-speciﬁc model had a higher recognition accuracy than the universal model. Chen et al. [186] proposed a user grouping-based approach, speciﬁcally the modeling workﬂow contains three stages, including user grouping, emotional state pool partition, and ﬁnal state discrimination. Liu et al. [187] also introduced subject clustering into cross-subject emotion recognition, as shown in Figure 25. Based on the clustering results, cluster selection was conducted to match the target subject with one optimal source cluster, whose source subjects have similar emotional EEG activity patterns. Subspace alignment method is further utilized for selecting the optimal sources with possibly ‘positive transfer’. Finally, the emotional state of the target data is decided by majority voting of the optimal sources.

Fig. 25. The framework of the subject clustering based cross-subject recognition method12. Cluster selection is required for selecting the optimal source cluster. Source selection is utilized for further selecting the optimal sources from the optimal cluster. The emotional state of the target is decided by those optimal sources [187].

(3) In recent years, the Transfer Learning method has been paid more and more attention by scholars. For a domain 퐷= {푋,푃(푋)} with a feature space 푋and the corresponding marginal probability distribution 푃(푋). When source domain 퐷푆{푋푆, 푃(푋푆)} and target domains 퐷푇= {푋푇, 푃(푋푇)} lie in the same feature space, namely 푋푆= 푋푇, and modeled for the same type of task, the domain shift issue can be resolved through Transfer Learning or called domain adaptation approaches. Transfer Learning maps the EEG features from source and target domains into the common feature representation space, where the inter-subject or inter-session shifts of the EEG data are adjusted, and distinctive features across subjects or sessions are obtained. For example, Lan et al. [188] veriﬁed various domain adaptation methods, including maximum independence domain adaption (MIDA) and transfer component analysis (TCA), which is believed able to decrease inter-subject variance as well as the inter-dataset discrepancies. By utilizing those domain adaptation methods, only a simple logistic regression model can have a signiﬁcant performance improvement in both cross-subject and cross-dataset experimental settings compared to the baselines that have no domain adaptation capabilities.

Transfer Learning techniques have also been extensively studied in Deep Learning. Among them, a naive approach draws lessons from experience in computer vision. They realize cross-domain application by ﬁne-tuning the source domain model on the target domain data, including ﬁne-tuning the

11Reprinted from [Wang Y, Huang Z, McCane B, et al. EmotioNet: A 3-D convolutional neural network for EEG-based emotion recognition. 2018 International Joint Confer- ence on Neural Networks (IJCNN). IEEE, 2018: 1-7] with the permission of IEEE Publishing. 12Reprinted from [Liu J, Shen X, Song S, et al. Domain Adaptation for Cross-Subject Emotion Recognition by Subject Clustering. 2021 10th International IEEE/EMBS Conference on Neural Engineering (NER). IEEE, 2021: 904-908] with the permission of IEEE Publishing. 13Reprinted from [Luo Y, Zhang S Y, Zheng W L, et al. WGAN domain adaptation for EEG-based emotion recognition. International Conference on Neural Information Processing. Springer, Cham, 2018: 275-286] with the permission of Springer Publishing. 14Reprinted from [Wang F, Zhang W, Xu Z, et al. A deep multi-source adaptation transfer network for cross-subject electroencephalogram emotion recognition. Neural Computing and Applications, 2021: 1-13] with the permission of Springer Publishing.

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 20 -->

1:20 • Li and Zhang, et al.

A B

Fig. 26. Two representative domain adaptation neural networks (DANN). A: The Wasserstein generative adversarial network based domain adaptation approach13 [189]. B: The multi-source adaptation transfer network (DMATN) based domain adaptation approach that integrates the deep adversarial network and the multi-kernel maximum mean discrepancies (MK-MMDs) measurement14 [190].

whole network model and ﬁne-tuning only part of the network structure in the target domain. For example, Cimtay and Ekmekcioglu [191] proposedto use the Inception Resnet model that pre-trained from the multi-subject raw EEG data, and they obtained promising cross-subject recognition performance on three benchmark datasets. Wang et al. [192] proposed a residual block-based CNN, which is trained on the electrode-frequency distribution maps (EFDMs) with short-time Fourier transform (STFT), the pre-trained model on SEED dataset can be successfully transferred to apply on DEAP dataset.

Integrating domain adaptation mechanisms into the Deep Learning model is increasingly gained attention. For example, as shown in Figure 26(A), Luo et al. [189] proposed the Wasserstein generative adversarial network domain adaptation (WGANDA), transferred the diﬀerential entropy characteristics of diﬀerent domains into the common space, which is helpful to improve the emotion recognition eﬀect across participants. Inspired by the same idea, Li et al. [193] also developed one domain adaptation neural network (DANN) based on a deep adversarial network. This model contains components of one feature extractor, one label predictor, and one domain discriminator. The feature extractor is trained in the direction for deceiving the domain discriminator by maximizing the domain discrimination losses. In this way, the feature extractor eliminates the domain-speciﬁc characteristics of the input for the purpose of increasing the domain identiﬁcation loss. The multi-kernel maximum mean discrepancies (MK-MMDs) were utilized for measuring the domain discrepancies. By simultaneously optimizing the loss functions of the MK-MMDs and the task, the DAN can reduce domain shift across domains, meanwhile preserving domain-invariant and task-related features. A multi-source adaptation transfer network (DMATN) for cross-subject emotion recognition is proposed by Wang et al. [190], as shown in Figure 26(B). The mechanism of this model is exactly similar to the model proposed by Li et al. [193]. The diﬀerence between these two approaches is the DMATN needs to select target domain-related source domains before modeling, and the features are automatically learned by the networks instead of handcrafted features. Cai et al. [194] also follows the DAN-based approach and proposed one model called maximum classiﬁer discrepancy (MCD) for domain adversarial neural networks (MCD_DA). MCD_DA not only adopts the GAN module to adapt the feature distribution between the source and target domains, but also it maximizes the classiﬁer diﬀerence between the source and target domains. Zhao et al. [195] proposes a plug-and-play domain adaptation method based on LSTM-Encoder-Decoder, in which the subject-invariant representations are modeled by the shared encoder and the subject-private representations are modeled by the private encoders. The target prediction is the integration of the shared classiﬁer with those of individual classiﬁers ensemble.

In the aforementioned methods, the DANN regards each domain as a whole, ignoring the class boundary in each domain. The MCD considers the speciﬁc class-boundary and trains adversarially to relocate the target feature to be inside the source features. However, since the original feature space of source and target are related but distinguishable, MCD will eliminate useful features, especially when the two domains are far more than similar. To eliminate the problems of DANN and MCD simultaneously, Ding et al. [196] proposed the task-speciﬁc domain adversarial neural network (T-DANN). Another problem that needs to be mentioned here is that although many works adopt discriminator-based domain adaptation approaches, it’s a challenge to apply on the target domain with few-labeled data. Hence, Wang et al. [197] proposed one few-label adversarial domain adaptation (FLADA) approach for cross-subject emotion recognition task. The FLADA originates from Meta-learning, which is to ﬁnd a feature representation that is broadly suitable for the target subject and source subject with limited labels. This approach can be applied to all Deep Learning models.

Recently, Zhang and Etemad [198] proposed a novel knowledge distillation-based knowledge transfer pipeline to distill EEG representations via capsule- based architectures, as shown in Figure 27, the pipeline contains a teacher network and a student network. They ﬁrst pre-train a large model (teacher network) on the large amounts of available cross-subject data. Then, using the pre-trained teacher to learn information embedded in capsules with intra-subject data. At last, the training of the lightweight student network on intra-subject data can be guided by the privileged information learned by the teacher via capsules. This knowledge distillation-based approach improves the robustness when faced with limited training samples and maxi- mally compresses the model with minimal loss in performance. This approach follows the modeling idea of ‘generalization to concretization’. Zhong et al. [199] proposed a regularized graph neural network (RGNN) to simultaneously resolve the domain shift problems of inter-subject variability and inconsistent/noisy emotion labels. Speciﬁcally, two regularizers are integrated into the model. One regularizer is the node-wise domain adversarial train- ing (NodeDAT) mechanism, which regularizes RGNN to generalize well in inter-subject recognition scenarios. NodeDAT is a ﬁne-grained regularization method to correct domain shift for each channel. Another regularizer is the emotion-aware distribution learning (EmotionDL) mechanism, which solves the problem of inconsistent emotion labels by learning the label distribution instead of the hard labels. To improve the recognition performance when facing large amounts of noisy labels.

The transfer process also could be accelerated by applying Meta Learning. For example, Duan et al. [200] introduced the meta update mechanism (MUPS-EEG) for cross-subject classiﬁcation. MUPS-EEG involves interaction between a base learner and a meta learner during meta training, each formed with a representation learning network and a prediction learning network. Duan et al. [201] proposed to utilize the model-agnostic meta-learning (MAML) algorithm to perform under limited target data, as shown in Figure 28. Experiments show it keeps enough ﬂexibility to adapt to the new subject

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 21 -->

EEG based Emotion Recognition: A Tutorial and Review • 1:21

3-stacked LSTM

Feature Space

Reshape

Conv2D

Lower Level Capsules

Higher Level Capsules

Capsule Attention

Teacher Network

3-stacked LSTM

Feature Space

Reshape

Conv2D

Lower Level Capsules

Higher Level Capsules

Capsule Attention

1-LSTM

Reshape

Conv2D

Lower Level Capsules

Higher Level Capsules

Capsule Attention

Distillation Distillation

Student Network

Feature Space

1-LSTM

Reshape

Conv2D

Lower Level Capsules

Higher Level Capsules

Capsule Attention

Feature Space

Fig. 27. One novel knowledge distillation DL framework for Aﬀective BCI based on LSTM-Capsule structure that compresses the large model without performance degradation [198].

while signiﬁcantly reducing the number of parameters to transfer. Considering existing domain adaptation approaches may become sensitive where a low discriminative feature space among classes is given. Jiménez-Guarneros and Gómez-Gil [202] proposed a Standardization-Reﬁnement Domain Adaptation (SRDA) method, which trains a target neural network model using Adaptive Batch Normalization (AdaBN) and introducing a novel loss based on the Variation of Information (VOI). Using AdaBN, SRDA makes the marginal distributions similar in source and target domains.

&ĞĂƚƵƌĞǆƚƌĂĐƚŽƌ

WƌĞƚƌĂŝŶŝŶŐ

hƉĚĂƚĞDĞƚĂ>ĞĂƌŶĞƌ

ŶĚĂƐĞ>ĞĂƌŶĞƌ

ĚĂƉƚDĞƚĂ>ĞĂƌŶĞƌ

ŽŶdĂƌŐĞƚ^ƵďũĞĐƚ

ǀĂůƵĂƚĞdĞƐƚ

ĐĐƵƌĂĐǇ

dĂƌŐĞƚdĂƐŬ

dĞƐƚĂƚĂ dĂƌŐĞƚdĂƐŬ ĚĂƉƚĂƚŝŽŶĂƚĂ

DĞƚĂdĂƐŬƐ >ĂƌŐĞ^ƚĂŶĚĂƌĚ ^ŽƵƌĐĞĂƚĂƐĞƚ

;ĂͿWƌĞͲƚƌĂŝŶŝŶŐWŚĂƐĞ ;ďͿDĞƚĂdƌĂŝŶŝŶŐWŚĂƐĞ ;ĐͿDĞƚĂdĞƐƚWŚĂƐĞ

Fig. 28. The Workflow of the Meta Learning on constrained Transfer Learning (MLCL) [201].

(4) In addition to calibration, alignment, aspect-oriented modeling, and transfer learning, some researchers directly explore the subject-independent robustness features. For example, Soleymani et al. [203] studied the importance of diﬀerent EEG features in emotion recognition. The ﬁndings showed that for Arousal, the PSD extracted from the low-frequency Alpha rhythm in the occipital EEGs is the most distinguishable feature. But for Valence, the key features are mainly from the Beta and Gamma rhythm in the temporal lobe EEGs. Zheng and Lu [60] investigated the stable EEG activity patterns to promote the eﬀect of emotion recognition across participants and time periods. The results showed that the Beta and Gamma rhythms of both sides of temporal lobes under positive emotion generated stronger activation than negative ones. Moreover, the subject-independent EEG features were mainly from these scalp channels and frequency bands. Li et al. [62] extracted 18 widely used EEG features and studied the contribution of each feature in cross- subject emotion recognition according to the results derived from multiple feature selection methods. After analysis, the features of Hjorth parameters in Beta rhythm yield the best cross-subject recognition results. Yin et al. [204] proposed a locally-robust feature selection (LRFS) method for individual- independent emotion recognition. Kernel density estimation (KDE) ﬁrst modeled the extracted EEG features. The inter-individual consistency of the EEG features is described by evaluating the similarity of all density functions between every two subjects, and the locally-robust EEG features could be further determined.

In addition, there has been one review paper proposed by Wan et al. [205] that focuses on the Transfer Learning techniques in solving the ‘domain shift’ problem in EEG analysis. As a complement to our review, we recommend the readers reference this review paper for detailed guidance of building EEG-based cross-subject emotion recognition models.

## 4.6 Route: 3→8→11 and 5→8→11

The Ensemble Learning-based recognition approaches are also an eﬀective strategy for getting ideal performance in the EEG-based emotion recognition tasks. Ensemble Learning follows the idea of ‘two heads are better than one’ by taking advantage of multiple models’ decision boundaries. For example, Mehmood et al. [206] used four Ensemble Learning strategies (Bagging, Boosting, Stacking, and Voting) to integrate the abilities of multiple machine learning models and then obtained the best recognition eﬀect based on the Voting approach. Stacking is to use the training data to build several base learners and use the probability output of these learners as a new training set to learn a meta learner. The meta learner learns to organize the input and assign weights to the base learners. For example, Yin et al. [207] proposed one Deep Learning-based stacking algorithm. The constructed network combines multi-layer stacked AutoEncoders. Each corresponds to a feature subset of multiple time-frequency-domain features. Hence, multiple types of higher-level features can be extracted from those subnetworks that promote the generalization capability and the robustness against data imbalance. Chen et al. [208] proposed to apply the Adaboost algorithm to elevate the recognition performance adaptively. As shown in Figure 29, it works based on the iteration mechanism. In each iteration, a weak classiﬁer is included to be trained on the weighted samples, the importance (weight) of this weak classiﬁer is determined in each iteration, and the sample weight is adjusted according to the classiﬁcation results. Speciﬁcally, the misclassiﬁed samples will be assigned a higher weight in the next iteration to get more attention in model training, while the correctly classiﬁed samples’ weights will decrease.

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 22 -->

1:22 • Li and Zhang, et al. At last, those weak classiﬁers are combined into one strong classiﬁer by their weights to obtain an improved recognition performance while improving generalization ability and avoiding over-ﬁtting.

Data set Weak classiﬁer 1

Weak classiﬁer 2

Weak classiﬁer 3

α1

α2

α3

α2 Sign Strong  classiﬁer ∑

...

... ...

W1

W2

W3

W4

Fig. 29. The working principle diagram of AdaBoost [208].

## 4.7 Route: 0→1→2→6→11

The acquired EEG signal and the corresponding labels might be noisy, imprecise, and uncertain, leading to precise modeling problems. Fuzzy Logic provides a foundation for approximate reasoning based on fuzzy set theory. Hence, in addition to those aforementioned technical routes, some studies adopted the Fuzzy Logic-based technical route, assigning the samples to multiple categories with a certain degree of membership. The Fuzzy C-Means and Fuzzy k-Means clustering methods are two representative Fuzzy Logic methods that have been implemented very early in EEG-based emotion recognition [209]. Besides, Matiko et al. [210] designed fuzzy classiﬁcation rules based on the asymmetry theory of emotional activities in the left and right brain hemispheres. Then, the classiﬁer outputs the type of emotion and the conﬁdence levels according to various rules. Based on Dempster-Shafer’s theory, Soroush et al. [211] improved the accuracy of recognition by fusing the feature subsets and multiple MLP classiﬁers. Additionally, fuzzy cognitive maps (FCMs), which combine aspects of Fuzzy Logic, neural networks, and nonlinear dynamical systems, also has been veriﬁed its eﬀectiveness in EEG-based emotion recognition [212]. As a whole, Fuzzy Logic is rarely studied in this research ﬁeld.

## 4.8 Route: 3→9→11

From the previous related works, we can see that adopting Deep Learning is the trend in EEG-based emotion recognition. Nevertheless, deep neural network models contain more parameters and rely on suﬃcient labeled training data to optimize the parameters compared with shallow models. Conse- quently, we must face one central challenge in EEG-based emotion recognition: acquiring adequate and high-quality training data. Hence, a promising research route is studying the ‘data-constrained learning’ to address the data limitation problems. Here we introduce two potential ways.

4.8.1 Data Augmentation Techniques. Some researchers focus on studying data augmentation (DA) techniques. We can generate new samples from the existing dataset to increase the number of training samples. Exposing the model to more variable representations of training samples makes it robust to data transformations that are likely to encounter in real applications. Furthermore, increasing the size of the training set facilitates training more complex models with many parameters and reduces over-ﬁtting. Data augmentation is typically conducted in computer vision by applying geometric transformations, e.g., rotation, cropping, etc. Nevertheless, the EEG is non-stationary time series. The geometric transformation methods are not suitable for EEG. One naive way is adding random noise (e.g., Gaussian, Poisson, Salt, Pepper noise, etc.) to the raw EEG signals [154, 213]. Sliding window-based approaches are also adopted for data augmentation. However, these approaches may introduce modeling and performance evaluation risks that we discuss carefully in Section 5.3. Deep Generative Learning-based data augmentation methods are recently drawing widespread attention, including the generative adversarial network (GAN) based approaches and the variational autoencoder (VAE) based approaches [214]. For example, during the training process of the adversarial network, the generator tries to generate data that are similar to the real data until the discriminator can not distinguish the fake data. More related works about data augmentation for EEG can be found in the review paper published by Lashgari et al. [215].

4.8.2 Few-shot Learning Techniques. Few-shot learning also is potential for dealing with the data limitation problems and has been studied in recent related works [216]. Few-shot learning is a class of machine learning techniques that build eﬀective models that generalize well on classes unseen during the training process. It works well with limited samples and does not rely on re-training on the data belonging to the new classes. The few-shot learning can also be called a 푁-shot-퐾-way learning problem. Most few-shot learning techniques rely on metric learning. As shown in Figure 30, we need to construct the Support set and Query set, respectively. For the Support set, we sample 푁samples for each of the 퐾classes. Further, we again sample the 퐾 classes to construct the Query set. An embedding function is needed to project these samples to a latent space, in which the model is optimized to reduce the distance between the embeddings of query and support samples belonging to the same class while increasing the distance of the samples belonging to diﬀerent categories. The Support and Query set construction process and optimization process iterate several times. After iteration, for testing, we only need a few samples belonging to the unseen class to form a support set, whereas the samples of the query set are the target to be inferred.

## 4.9 Route: 3→10→11 and 5→10→11

The processes involved in EEG-based emotion recognition studies are somewhat tedious. The domain knowledge hidden in this task is far beyond the ma- chine learning specialists’ knowledge range. Is there a way to automatically build robust recognition models on raw EEG data? In this regard, Automated Machine Learning (AutoML) is drawing attention in this domain. For AI-based approaches, an eﬀective model is primarily decided by the model hyper- parameters and the data representations. AutoML refers to end-to-end methodologies and tools for automatic optimization of data preprocessing, feature

15Reprinted from [Bhosale S, Chakraborty R, Kopparapu S K. Calibration free meta learning based approach for subject independent EEG emotion recognition. Biomedical Signal Processing and Control, 2022, 72: 103289] with the permission of Elsevier Publishing.

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 23 -->

EEG based Emotion Recognition: A Tutorial and Review • 1:23

Fig. 30. General few-shot learning paradigm: (a) generating embeddings for the support set S, (b) generating embeddings for the query set Q, (c) Mapping query set embeddings using support sample15 [216].

engineering, model selection, model building, and hyperparameter optimization [217]. It aims to generate the models that provide the best classiﬁcation performance and minimize the generalization error for a speciﬁc problem. Currently, a few researchers have started to introduce the AutoML techniques into EEG-based emotion recognition. For example, He et al. [218] proposed one ﬁreﬂy integrated optimization algorithm (FIOA) to simultaneously realize the automatic parameter optimization, feature selection, and classiﬁer selection. For Deep Learning-based technical routes, Aquino-Brítez et al. [219] proposed a fully-conﬁgurable optimization framework based on multi-objective optimization for Deep Learning architectures. It is not only capable of optimizing the model hyperparameters, but it can also adapt the model architecture, e.g., inserting or removing layers. At present, the main problem it encounters is that the computation burden is high. For example, the neural architecture search algorithm NASNet that was proposed by Google takes 28 days of training on 800 GPUs. Such high computational costs make search algorithms impractical for most researchers. It is encouraged that researchers are devoted to reducing the cost of AutoML training. We believe introducing AutoML techniques into various EEG modeling tasks will be very promising in the future.

## 5 PERFORMANCE EVALUATION 5.1 Benchmark dataset

The proposed recognition algorithms and models should be veriﬁed on EEG data with emotional ratings or labels. However, it is impossible for some researchers, especially those in computer science, to build a professional experimental environment and design a scientiﬁc user experimental paradigm that needs specialized knowledge of psychology. Most researchers interested in studying recognition models choose to verify their ideas and compare with related works on the recognized benchmark dataset. Hence, developing open-source EEG dataset that can help evaluate recognition models’ performance is something the ﬁeld urgently needs and well worth studying.

Table 3. List of Recognized Benchmark Emotional EEG Dataset

Year Data Set Participants EEG De- vice

Stimulus Acquired Data Modalities Quantiﬁcation of Emotion

2011 DEAP [54] 32 (16 male, 16 female) Biosemi Ac- tiveTwo

40 video clips 32-channel EEG, Peripheral physiological signals (Gal- vanic Skin Response, Blood Volume Pulse, respiration, Skin temperature, Electromyography, Electro-Oculogram), Face video

continuous type (Arousal, Va- lence, Dominance, Liking)

2012 MAHNOB-HCI [14]

27 (11 male, 16 female) Biosemi Ac- tiveTwo

20 video clips 32-channel EEG, Peripheral physiological signals (Galvanic Skin Response, Respiration, Skin temperature, Electrocar- diograph), Face and body video, Eye-tracking data, Audio

discrete type (9 types), con- tinuous type (Arousal, Va- lence, Dominance) 2017 SEED [220] 15 (7 male, 8 female) ESI Neu- roScan

15 video clips 62-channel EEG, Peripheral physiological signals (Elec- tromyography, Electro-Oculogram), Face video

discrete type (Arousal- negative, Arousal-neutral, Arousal-positive) 2018 DREAMER [221] 25 (14 male, 11 female) Emotiv EPOC

18 video clips 14-channel EEG, Peripheral physiological signals (Electro- cardiogram)

continuous type (Arousal, Va- lence, Dominance) 2019 SEED-IV [222] 15 (7 male, 8 female) ESI Neu- roScan

72 video clips 62-channel EEG, Eye-tracking data discrete type (happy, sad, fear, and neutral) 2019 MPED [223] 23 (10 male, 13 female) ESI Neu- roScan

28 video clips 62-channel EEG, Peripheral physiological signals (Electro- cardiogram, Respiration, Galvanic Skin Response

discrete type (joy, funny, anger, fear, disgust, sad and neurality)

Among them, the Dataset for Emotion Analysis using EEG, Physiological and video signals (DEAP) is mostly used and cited, which was collected and opened by researchers from Queen Mary University of London, the University of Geneva in Switzerland, etc. [54]. Thirty-two participants were recruited for the emotional EEG induction experiment. The EEG and several kinds of peripheral physiological signals were acquired while watching forty 60s long music movie clips. Then the subjective emotional experience in induction experiments was self-evaluated and rated on assessment scales that cover multiple emotional dimensions, including Arousal, Valence, Like, Dominance and Familiarity. The ratings are taken as the emotional ratings and labels of the EEG samples for model optimization. Another well-recognized benchmark dataset is the MAHNOB-HCI multi-modal dataset. It not only records the physiological and eye- tracking activities of participants during the emotion induction experiments, but also the videos (face and body) and the audios are also synchronously recorded. This dataset is developed for emotion detection and implicit tagging studies [14]. SJTU Emotion EEG Dataset (SEED) [220] also has a great community inﬂuence that was released by the BCMI Research Center in Shanghai Jiaotong University (SJTU). In

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 24 -->

1:24 • Li and Zhang, et al. the experiment, 15 movie clips with three types of emotional states were adopted to induce the speciﬁc emotions. Each genre had ﬁve clips and each for about 4 minutes. Regarding the inﬂuence of cultural background of language on emotional stimulation eﬀect, only Chinese movies are selected in SEED for Chinese subjects. 15 Chinese participants participated in the EEG acquisition experiments for three diﬀerent periods. This experimental design allows evaluating the algorithm’s robustness when the data are acquired in diﬀerent periods. It is believed that the EEG patterns and the subjective emotional experience may be unstable across diﬀerent periods, which is a kind of ’domain shift’16 phenomenon in data science that brings great challenges in intelligent modeling [224]. Recently, DREAMER is also adopted as a benchmark dataset for evaluating performance in some researches. It contains the EEG and electrocardiogram (ECG) signals that are simultaneously collected during the audio-visual emotion induction experiments. Twenty-three participants were recruited to participate in the experiment. After each trial, self-assessment in terms of Valence, Arousal, and Dominance is required. It is worth mentioning that all the signals were captured using portable, wearable, wireless and low-cost equipment that has the potential to verify recognition methods in everyday applications [221]. SEED-IV is an extended version of the SEED data set, which is also released by SJTU [222], and also is well recognized in recent related works. It follows the experimental paradigm adopted in the SEED, and it records the 62-channel EEG from selected 15 subjects across three testing sessions. They choose 72 ﬁlm clips with four diﬀerent emotional labels (neutral, sad, fear, and happy). Each subject watched six ﬁlm clips for each emotion class in each session, resulting in 24 trials. Multi-modal Physiological Emotion Database (MPED) is one less well known and studied dataset that worth of mentioning here [219]. It is a multi-modal dataset that records the 62-channel EEG, the ECG, the respiration, and the galvanic skin response from 23 Chinese student volunteers. 28 Chinese video clips with seven types of discrete emotion (joy, funny, anger, fear, disgust, sadness, and neutrality) are selected from 1500 video clips, including ﬁlm clips, TV News, and TV shows. The experiment is divided into two sessions with an interval of at least 24-hours. Each volunteer watched 14 video clips in each session, resulting in 14 trials.

## 5.2 Evaluation Metric

All the proposed recognition methods should be evaluated on benchmark datasets by comparing the predicted emotion ratings/labels with the ground truth. For a classiﬁcation modeling task, the built classiﬁers are typically assessed based on a confusion matrix-based approach, as shown in Figure 31, based on which four classiﬁcation metrics can be derived for performance comparison, namely Precision, Sensitivity, Speciﬁcity, and F-score. Regarding the binary classiﬁcation problem for the sake of simplicity, the four metrics are calculated as the following Formula 4. The TP, FP, TN, and FN are the abbreviations for True Positive, False Positive, True Negative, and False Negative, respectively. We usually adopt these metrics to measure the performance of a classiﬁcation algorithm. True Positive is used to measure the number of actual positives (e.g., the emotion of happiness) which are correctly identiﬁed. Similarly, a True Negative is used to measure the number of actual negatives (e.g., the emotion of sadness) which are correctly identiﬁed. False Positive is the number of true negatives misclassiﬁed as positives. False Negative is the number of true positives incorrectly identiﬁed as the negatives.

Predicted Value: Positive (+)

Predicted Value: Negative (-)

Predicted Class

True Positive

TP

False Negative

FN

False Positive

FP

True Negative

TN

Actual Value: Positive (+)

Actual Value: Negative (-)

Actual Class

Confusion

Matrix

Fig. 31. Binary classification confusion matrix.





푃푟푒푐푖푠푖표푛= 푇푃

푇푃+ 퐹푃,

푆푒푛푠푖푡푖푣푖푡푦= 푇푃

푇푃+ 퐹푁,

푆푝푒푐푖푓푖푐푖푡푦= 푇푁

푇푁+ 퐹푃,

퐹푠푐표푟푒= 2 ∗푃푟푒푐푖푠푖표푛∗푆푒푛푠푖푡푖푣푖푡푦

푃푟푒푐푖푠푖표푛+ 푆푒푛푠푖푡푖푣푖푡푦

(4)

For a regression modeling task, the built model is typically evaluated by computing the deviation between the predicted emotional rating and the subjects’ reported rating. Researchers usually report the mean squared error (MSE) and the mean absolute error (MAE), as well as the coeﬃcient of determination (푅2) [16], as in the Formula 5, where 푦푖is the ground truth rating for a sample 푖, ¯푦is the mean ground truth rating of all samples and ˆ푦푖is the rating as estimated by the regressor for sample i. 푅2-score range from zero to one, a higher value indicates a higher consistency between the model prediction and the ground truth.





푀푆퐸=

r

Í푛

푖=1 (푦푖−ˆ푦푖)2

푛 ,

푀퐴퐸= 1

푛

푛 Õ

푖=1

(푦푖−ˆ푦푖)2,

푅2 = 1 −

Í푛

푖=1 (푦푖−¯푦푖)2

Í푛

푖=1 (푦푖−ˆ푦푖)2

(5)

16We discuss the domain shift problem in EEG based emotion recognition in Section 4.5

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 25 -->

## EEG based Emotion Recognition: A Tutorial and Review • 1:25 5.3 Data Split and Validation Strategy

The strategy of constructing the training and test samples has not been thoroughly studied and discussed in related works. Hence, it may be diﬃcult to reproduce some research results, which may be considered weird tricks and mislead some researchers. From our point of view, the data split and validation strategy should be designed based on the research objectives. The strategy guides to validate whether or not the research objectives can be achieved.

Hence, we will discuss this issue from the perspective of the research objectives. Generally, the research objectives in EEG-based emotion recognition can be divided into two main categories, namely subject-dependent modeling and subject-independent modeling. Subject-dependent modeling assumes that it is impossible to build one universal model to recognize each subject well. In this setting, the model training is conducted for each subject, and testing is performed on the same subject’s data, which measures how well the recognition model performs on data with intra-subject variabilities. The researchers split the dataset in each subject scope when adopting this strategy. Nevertheless, there would be a large deviation in the distributions of EEGs collected from diﬀerent subjects. Hence, subject-independent modeling and evaluation aim to build a universal and robust recognition model for various data domains. The training is performed on a group of subjects, and the evaluation is conducted on data from one or more unseen subjects. This evaluation strategy measures how well the built model handles the problem of inter-subject variabilities.

Regardless of research objectives, they all can adopt the k-fold cross-validation scheme for overall evaluation that splits the whole dataset into k independent parts without overlap. Each time, one part of the entire data is selected out as the test set for evaluating the classiﬁer, and the remaining parts of data are used as the training set for model building. This process is repeated k times. The ﬁnal overall evaluation of the recognition method can be derived by averaging the results obtained on each fold.

K-fold Data

Splitting  Strategy

Subject-Dependent

Modeling

Subject-Independent

Modeling

Leave-K-Trial-Segments-

Out Strategy

Segment the Trials of

one Subject

Training on the Trial-level Train Set and

Validating on the Trial-level Test Set

Randomly Divide all the

Segments of one  Subject into K-folds

Training on the Segment-level Train Set and

Validating on the Segment-level Test Set

Ś

ś

ş

Ŝ

ŝ

Ş

Š

Randomly Divide all

The Trials of all the  Subjects into K-folds

Segment the Trials of

All Subjects

Training on the Trial-level Train Set and

Validating on the Trial-level Test Set

Training on the Segment-level Train Set and

Validating on the Segment-level Test Set

Do not Segment the  Trials of one Subject

Leave-K-Trial-Out

Strategy

Do not Segment the  Trials of All Subjects

Leave-K-Subject-Trials-

Out Strategy

Randomly Divide all  The Segments of all the

Subjects into K-folds

Leave-K-Subject- Segments-Out Strategy

Training on the Segment-level Train Set and

Validating on the Segment-level Test Set

Training on the Trial-level Train Set and

Validating on the Trial-level Test Set

Training on the Segment-level Train Set and

Validating on the Segment-level Test Set

Ś

Fig. 32. The possible k-fold data split strategy adopted in related works

We illustrate the possible splitting strategies for the two kinds of research objectives in Figure 32. Seven possible K-fold splitting strategies may be adopted in related works. Usually, we do not segment the original trial data both for the subject-dependent and subject-independent modeling and adopt the ‘leave-K-trial-out’ and ‘leave-K-subject-trials-out’ strategies, respectively. Hence, the 1st, 4th, and 5th splitting strategies are all reasonable and recommended, and they reﬂect the recognition performance in real-world settings. However, we ﬁnd some related works proposed to segment the trials. For example, for a 60-second long trial, we can divide the entire trial into 15 segments with a 4-second long non-overlap sliding window. They build and validate the model on the segments, as shown in the 2nd, 3rd, 6th, and 7th strategies. The main reason behind it is the number of EEG trials of one subject is usually no more than 100 considering the factor of user fatigue, which is not enough for optimizing a complex recognition model, especially in the case of training deep neural networks. In these approaches, the segments that belong to the same trial are all assigned with the same trial label. From our point of view, these splitting approaches may be somewhat unsuitable, which has been illustrated in Figure 16, where the subjects’ emotional state may be continuously evolving, and the label of the trial is the overall emotional experience of the subject during a trial. Hence, assigning the segments with the same label may introduce lots of noisy labels, greatly inﬂuencing the model training. These segment-based approaches only hold when the emotional stimuli are strong enough to consistently evoke the subject’s target emotion. Nevertheless, we have to point out that the 3rd and 7th splitting strategies are wrong approaches that the researchers of this ﬁeld should not consider. To be speciﬁc, if we randomly divide the segments into K folds, the segments from the same trial may be assigned to the training and test sets simultaneously, introducing information leakage from the training set to the test set. It will lead to the high recognition performance on the test set, as the segments of the same trial are somewhat correlated in the data distribution that the trained model has remembered in the training phase.

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 26 -->

1:26 • Li and Zhang, et al.

Table 4. List of relevant representative research works in recent 5 years (from 2016 to 2021 year)

Year Author Experimental Data Set Methodology Experimental Results

2016 Atkinson and Campos [115] DEAP kernel classiﬁers combines feature selection method based on minimum-Redundancy-

Maximum-Relevance (MRMR) 2 classes, subject-independent modeling (Valence: 0.7314, Arousal: 0.7306) 2016 Thammasan et al. [130] EEGs induced by MIDI audio

materials Sliding window based signal segmentation, modeling based on DBN and handcraft features of

fractal dimension, power spectral and discrete wavelet transform 2 classes, subject-dependent modeling (Valence: 0.8824, Arousal: 0.8242) 2016 Li et al. [154] DEAP one CNN+RNN hybrid Deep Learning framework combines wavelet scalogram representation

for multi-channel EEGs 2 classes (Valence: 0.7206, Arousal: 0.7412)

2016 Lan et al. [70] EEGs induced by IADS audio

materials SVM classiﬁer combines statistical features, fractal dimension, power spectral and higher-

order crossing feature 4 classes (pleasant/happy/frightened/angry) (cross-session: 24.97%∼ 49.63%, intra-session: 46.56%∼81.41%) 2016 Ackermann et al. [123] DEAP handcraft features (statistics, STFT, HOC, hilbert-huang spectrum) combines with MRMR di-

mension reduction method and Random Forest/SVM classiﬁers 3 classes (Anger/Surprise/Other): ≃52%

2017 Tripathi et al. [132] DEAP 9 kinds of time-domain features combine with DNN and CNN models 2 classes, subject-dependent modeling (CNN-Valence: 81.41%, CNN- Arousal: 73.36%)

2017 Mohammadi et al. [78] DEAP feature extraction by discrete wavelet transform and classify by KNN/SVM 2 classes, subject-dependent modeling (Valence: 86.75%, Arousal: 84.05%) 2017 Yin et al. [207] DEAP ensemble classiﬁers based on multiple stacked auto-encoders combine with features of statis-

tics and PSD 2 classes, subject-dependent modeling (Valence: 0.7243, Arousal: 0.6901) 2017 Chen et al. [186] DEAP a three-stage decision framework based on partioning the subjects into diﬀerent groups 2 classes (Valence: 0.4357, Arousal: 0.7757) 2018 Liu et al. [76] EEGs induced by movie clips power spectral feature extraction by STFT combines with LDA based feature selection and

SVM based classiﬁer positive/negative emotion: 86.63%, intra positive emo-

tion(amusement/joy/tenderness): 86.43%, intra negative emo-

tion(anger/disgust/fear/sadness): 65.09%

2018 Li et al. [61] SEED 2D map of diﬀerential entropy feature combines with hierarchical convolutional neural net- work 2 classes (subject dependent: 0.882, subject independent: 0.802)

2018 Katsigiannis and Ramzan

[68] DREAMER artifacts removal by ASR and CAR method, PSD features extraction combines with SVM clas-

siﬁer 2 classes (Valence: 62.49%, Arousal: 62.17%)

2018 Li et al. [62] DEAP, SEED 18 kinds of handcrafted EEG features combine with multiple feature selection methods and SVM classiﬁer 2 classes, subject-independent modeling (DEAP-Valence: 0.7167, DEAP-Arousal: 0.7154, SEED: 0.8234)

2018 Mert and Akan [81] DEAP multivariate empirical mode decomposition based multiple features extraction combines with

ICA based feature dimension reduction and ANN classiﬁer 2 classes (ANN-Valence: 0.7287, ANN-Arousal: 0.7500)

2018 Wang et al. [146] DEAP an emotional EEG-speciﬁc 3D-CNN (EmotioNet) using a simultaneous temporal-spatial fea-

ture detection, the input EEGs are arranged according to the topological structure 2 classes, subject-independent modeling (Valence: 72.1%, Arousal: 73.1%) 2018 Salama et al. [148] DEAP a 3D-CNN is employed for extracting the spatiotemporal features, the input EEGs are randomly

arranged and one data augmentation scheme is adopted 2 classes, subject-dependent modeling (Valence: 87.44%, Arousal: 88.49%) 2018 Zhang et al. [155], Yang et al.

[156] DEAP cascade and parallel hybrid models integrate CNN and RNN, in which the input is the raw

EEG signal arranged according to electrode topology 2 classes, subject-dependent modeling(Valence: 90.80%, Arousal: 91.03%) 2018 Lan et al. [188] DEAP, SEED transfer learning methods (MIDA,TCA) combines with diﬀerential entropyfeature and logistic

regression classiﬁer 3 classes, subject-independent modeling (DEAP-MIDA: 0.4893, DEAP- TCA: 0.4722, SEED-MIDA: 0.7247, SEED-TCA: 0.7167)

2018 Li et al. [142] SEED a bi-hemispheres domain adversarial neural network (BiDANN) that takes into the cerebral

hemisphere asymmetry information as well as the domain adaptation 3 classes (subject-dependent modeling: 92.38%, subject-independent modeling: 83.28%)

2018 Luo et al. [189] DEAP, SEED Wasserstein generative adversarial network domain adaptation (WGANDA) framework based

transfer learning combines with diﬀerential entropy feature 2 classes, subject-independent modeling (DEAP-Valence: 0.6799, DEAP-Arousal: 0.6685, SEED: 0.8707)

2018 Li et al. [193] SEED a deep adaptation network (DAN) based on adversarial network is proposed to solve the cross-

subject recognition problem 2 classes, subject-independent modeling: 0.8381

2018 Yang et al. [90] EEGs induced by movie clips a channel-frequency convolutional neural network (CFCNN) combined with recurrence quan-

tiﬁcation analysis (RQA) 3 classes (happiness/sadness/fear), subject-dependent modeling:

92.24% 2018 Song et al. [137] SEED, DREAMER a dynamical graph convolutional neural network dynamically learns graph adjacency weight

matrix and classiﬁes emotions based on EEG features of DE, PSD, DASM, RASM and DCAU subject-dependent modeling (SEED: 90.4%, DREAMER-Valence:

86.23%, DREAMER-Arousal: 84.54%), subject-independent modeling (SEED: 79.95%)

2019 Li et al. [127] SEED time-domain and frequency-domain EEG features combine with graph regularized sparse lin-

ear regression (GRSLR) model 3 classes, subject-independent modeling: 0.8841

2019 Ma et al. [225] DEAP a multimodal residual LSTM classiﬁer based on raw EEG and physiological signal 2 classes, subject-dependent modeling (DEAP-Valence: 92.30%, DEAP- Arousal: 92.87%)

2019 Zhang et al. [159] SEED adopting multi-directional SRNN layer and bidirectional TRNN layer to learn spatiotemporal

dependencies in layers 3 classes, subject-independent modeling: 89.50%

2019 Li et al. [158] SEED a hierarchical spatio-temporal neural network model based on LSTM and attention mechanism

that acquires the intrinsic spatial relationship and time dependencies 3 classes, subject-independent modeling: 93.38%

2019 Zhang et al. [159] SEED a Riemannian fusion network to learn the most discriminative and complementary spatial and

temporal information 3 classes (subject-dependent modeling: 93.72%, subject-independent modeling: 84.16%)

2019 Guo et al. [212] DEAP fuzzy cognitive maps (FCM) combines with SVM 2 classes, subject-dependent modeling: 73.32% 2020 Li et al. [161] DEAP, SEED a raw EEG decoding approach based on stacked AE (non-generative model), RBM (generative

model), and VAE (generative model), then further utilized the LSTM for sequence learning 2 classes, subject-independent modeling (DEAP-Valence: 0.7167, DEAP-Arousal: 0.7243, SEED: 0.8429)

2020 Cho and Hwang [149] DEAP 2 types of 3D-CNN models (C3D, R(2 + 1)D) are veriﬁed, the input raw EEGs are arranged into 2D frames according to 1electrode topology, the interpolated 2D EEG frames are further

concatenated into 3D cubes

2 classes, subject-independent modeling (DEAP-Valence: 99.11%, DEAP-Arousal: 99.74%)

2020 Chao et al. [133] DEAP a framework based on multi-band feature matrix (MFM) and capsule network (CapsNet) 2 classes (Valence: 0.6673, Arousal: 0.6828, Dominance: 0.6725) 2020 Zhong et al. [199] SEED a regularized GNN model (RGNN) that adopts two kinds of regularizers: NodeDAT and Emo-

tionDL 3 classes, subject-dependent modeling: 94.24%, subject-independent modeling: 85.30%

2020 Zhang and Etemad [164] SEED an end-to-end Riemannian fusion network (RFNet) that captures spatial information from the

Riemannian manifold and temporal information from the Euclidean space 3 classes, subject-dependent modeling: 0.9372

2020 Ding et al. [150] EEGs induced by VR scenes a temporal-spacial 1D convolution based model inspired by the Inception block of GoogleNet Arousal-2 classes, subject-dependent-session-independent modeling:

86.03% 2020 Zhang et al. [138] SEED, MPED a heuristic variational pathway reasoning (VPR) method for mining salient connections infor-

mation embedded in the multi-channel EEGs that is conducive to recognition 3 classes, subject-dependent modeling (SEED: 94.30%, MPED: 75.06%)

2020 Luo et al. [226] DEAP, SEED a spiking neural network (SNN) based framework subject-independent modeling (DEAP-Valence: 78%, DEAP-Arousal:

74%, SEED: 96.67%)

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 27 -->

EEG based Emotion Recognition: A Tutorial and Review • 1:27

2020 Li et al. [141] SEED a bi-hemispheric discrepancy model(BiHDM) learns the asymmetric characteristics between

hemispheres 3 classes (subject-dependent modeling: 93.12%, subject-independent modeling: 85.40%)

2020 Cui et al. [144] DEAP, DREAMER an end-to-end regional-asymmetric CNN (RACNN) consists of temporal (1D-CNN), regional

(2D-CNN) and asymmetric feature extractors (ADL) 2 classes, subject-dependent modeling (DEAP-Valence: 96.65%, DEAP- Arousal: 97.11%, DREAMER-Valence: 95.55%, DREAMER-Arousal:

97.01%) 2020 Cimtay and Ekmekcioglu

[191] SEED, DEAP, LUMED a pretrained state-of-the-art CNN model InceptionResnetV2 subject-independent modeling (SEED-2 classes: 86.56%, SEED-3 classes: 78.34%, DEAP-2 classes: 72.81, LUMED-2 classes: 81.8%)

2020 Duan et al. [200] DEAP a transfer learning method named Meta Update Strategy (MUPS-EEG) that involves a meta

representation learning phase followed by meta adaptation to target subject Arousal-2 classes, subject-independent modelling: 66.5%

2020 Duan et al. [201] SEED, DEAP a generalized optimization-based meta learning approach under constrained transfer learning

setting that trains on large standard datasets of known subjects and then quickly adapt to a

new subject with minimal target data.

subject-independent modelling (DEAP-Arousal-2 classes: 67.5%, SEED-

3 classes: 78.6%)

2020 Wei et al. [151] SEED an emotion recognition system based on Simple Recurrent Units (SRU) network, Dual-tree

Complex Wavelet Transform (DT-CWT), diﬀerential entropy (DE), and ensemble learning subject-dependent modelling (SEED-3 classes: 83.13%)

2020 Wang et al. [192] SEED, DEAP an electrode-frequency distribution maps (EFDMs) with short-time Fourier transform (STFT)

, a Residual block-based deep convolutional neural network, and deep model transfer subject-independent modelling (SEED-3 classes: 90.59%, DEAP-

Valence-3 classes: 82.84%)

2020 Tao et al. [157] DEAP, DREAMER an attention-based convolutional recurrent neural network (ACRNN) with channel-wise at-

tention and an extended self-attention to extract discriminative spatiotemporal information 3 classes, subject-dependent modelling (DEAP-Valence: 93.72%, DEAP- Arousal:93.38%, DREAMER-Valence: 97.93%, DREAMER-Arousal:

97.98%, DREAMER-dominance: 98.23%) 2020 Jia et al. [153] SEED, SEED-IV a novel spatial-spectral-temporal based attention 3D dense network (SST-EmotionNet) works

with 3D diﬀerential entropy representations SEED-3 classes: 96.02%, SEED-IV-4 classes: 84.92%

2020 Luo et al. [214] SEED, DEAP a method based on two deep generative models, variational autoencoder(VAE) and generative

adversarial network (GAN), and two data augmentation strategies subject-dependent modelling (SEED-3 classes: 93.5%, DEAP-4 classes:

50.8%) 2020 Cheng et al. [128] DEAP, DREAMER a multi-grained cascade Forest model (gcForest) with input of 2D frame representation subject-dependent modelling (DEAP-Valence-2 classes: 97.69%, DEAP-Arousal-2 classes: 97.53%, DREAMER-Valence-3 classes: 89.03%,

DREAMER-Arousal-3 classes: 90.41%, DREAMER-Dominance-3

classes: 89.89%)

2020 Liu et al. [135] DEAP, DREAMER an eﬀective multi-level features guided capsule network (MLF-CapsNet) 2 classes, subject-dependent modelling (DEAP-Valence: 97.97%, DEAP- Arousal: 98.31%, DEAP-Dominance: 98.32%, DREAMER-Valence:

94.59%, DREAMER-Arousal: 95.26%, DREAMER-Dominance: 95.13%) 2020 He et al. [218] LabEdata, DEAP a novel ﬁreﬂy integrated optimization algorithm that automatically optimize feature selection,

parameter setting and classiﬁer selection 2 classes, subject-dependent modelling (LabEdata: 95%, DEAP: 92%)

2021 Wang et al. [190] SEED the multi-source selection is employed to obtain the source domain mostly correlated with

new subject, the deep multi-source adaptation transfer network (DMATN) model is used to

map correlated source domain and the target domain (new subject) into reproducing kernel

Hilbert space

3 classes, subject-independent modelling: 84.23%

2021 Huang et al. [143] DEAP a bi-hemisphere discrepancy convolutional neural network model (BiDCNN) built on 3 kinds

of feature matrices 2 classes, subject-dependent modeling (Valence: 94.38%, Arousal: 94.72%), subject-independent modeling (Valence: 68.14%, Arousal: 63.94%) 2021 Yin et al. [163] DEAP a GCNN-LSTM hybrid model, named ECGGCNN 2 classes, subject-dependent modeling (Valence: 90.45%, Arousal: 90.60%), subject-independent modeling (Valence: 84.81%, Arousal: 85.27%) 2021 Chen et al. [208] DEAP Adaboost based ensemble learning method 2 classes, subject-independent modeling (Valence: 85.57%, Arousal: 88.36%) 2021 Zhang and Etemad [198] SEED a LSTM-Capsule based knowledge distillation framework 3 classes, subject-independent modeling: 91.07% 2021 Zhao et al. [195] SEED a novel plug-and-play domain adaptation (PPDA) method that subject-invariant representa-

tions and private components of source subjects are separately captured by a shared encoder

and private encoders

subject-independent modelling (SEED-3 classes: 86.7%)

2021 Fernandez et al. [183] SEED a CNN-based network with diﬀerential Entropy input and three hidden layers each followed

by stratiﬁed normalization method subject-independent modelling (SEED-2 classes: 91.6%, SEED-3 classes:

79.6%) 2021 Cai et al. [194] SEED a domain adaptation method, named the maximum classiﬁer diﬀerence for domain adversarial

neural networks (MCD_DA) 3 classes, subject-independent modelling: 88.33%

2021 Islam et al. [147] DEAP a deep Convolutional Neural Network (CNN) with Pearson’s Correlation Coeﬃcient (PCC)

featured images of channel correlation of EEG sub-bands subject-dependent modelling (valence-2 classes: 78.22%, arousal-2

classes: 74.92%, valence-3 classes: 70.23%, arousal-3 classes: 70.25%)

2021 Yin et al. [204] DEAP, MAHNOB-HCI a new locally-robust feature selection (LRFS) method cooperate with SVM and ensemble learn-

ing 2 classes, subject-independent modeling (DEAP-Arousal: 65%, DEAP- Valence: 68%, MAHNOB-HCI-Arousal: 67%, MAHNOB-HCI-Valence:

70%) 2021 Ding et al. [196] SEED a Task-speciﬁc Domain Adversarial Neural Network (T-DANN)that transfers knowledge from

either one subject to predict on another subject or knowledge from one phase to predict on

another phase within the same subject

3 classes, subject-independent modelling (cross-subject: 74.19%, cross- phase: 85.13%)

2021 Wang et al. [197] SEED, DEAP a novel method called ‘few-label adversarial domain adaption’ (FLADA) that works on a small

target data subject-independent modelling (DEAP-2 classes:68.0%, SEED-3 classes:

89.32%) 2021 Liu et al. [187] DEAP an extended domain adaptation method by introducing subject clustering (DASC) 2 classes, subject-independent modelling (DEAP-Valence: 73.9%, DEAP-Arousal: 68.8%)

2022 Bhosale et al. [216] DEAP a few-shot adaptation method based on meta learning without requiring any ﬁne-tuning of

the pre-trained model 2 classes, subject-independent modelling (Valence: 76.46%, Arousal: 75.81%, Dominance: 70.63%)

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 28 -->

## 1:28 • Li and Zhang, et al. 6 CONCLUSION AND DISCUSSION

We choose to outline the review from the perspective of researchers who try to take the ﬁrst step on this topic. Hence, we review not only the overall current situation in the EEG based emotion recognition research but also provide a tutorial to guide the researchers to start from a very beginning, as well as illustrate the theoretical basis and the research motivation, which will help the readers to understand why those techniques are employed. For this prospect, we introduce the preliminaries and basic knowledge of this ﬁeld. Firstly, we present the deﬁnition and quantiﬁcation methods of emotion. It is the prerequisite for aﬀective computing, and it determines the objective of the modeling tasks (regression, clustering, classiﬁcation). Then we illustrate the speciﬁcities and neural correlates of EEG in the emotional process, and we demonstrate the feasibility of EEG in studying the emotion recognition technologies. Before reviewing the technical routes, we also exhibit the classical research methodologies for EEG-based emotion detection studies, which helps the readers understand the goal of this ﬁeld and the mainstream methodologies in the past quickly. The section of ‘Preliminaries and Basic Knowledge’ guides the readers to understand the following sections’ contents better.

Then, we devote much eﬀort to guiding the newcomers of the EEG preprocessing and the feature engineering methods, which is the basis for most classical methodologies. The remaining parts of this paper mainly focus on the pattern recognition technical routes applied in the ﬁeld, in which we summarize the mainstream and latest technical routes involved in this ﬁeld and review plenty of representative works under each route. Finally, we discuss the evaluation methods adopted in this ﬁeld. In addition to the benchmark datasets, we discuss the potential inﬂuence of diﬀerent data split strategies in modeling and validation, which is a topic that many researchers care about. Considering the rapid development of Deep Learning and its successful application in this ﬁeld, we select to review as many Deep Learning-based approaches as possible, and the selected works are within the scope of the recent three years. We tend to summarize representative works in this ﬁeld and conduct empirical comparisons for closely related approaches from a descriptive perspective. We try to list these works in a structured table (Table 4), which presents the methodologies, the validation strategies, and the achieved performance in a direct way.

Though there have been many achievements in this ﬁeld, there still exists several problems and challenges need to be further studied and resolved, as follows:

• There is still room for research to explore eﬀective EEG representation (transformation) approaches, which rely on EEG preprocessing and feature engineering. EEG preprocessing makes the emotion-related information (components) eﬀectively ﬁltered out from the multi-channel EEGs that contain redundant noisy components. Feature engineering helps to determine the critical variables related to emotions. Current widely utilized features cover various aspects, such as time-frequency characteristics, nonlinear dynamical system characteristics, etc. The feature extraction process may incur a high overhead and depends on subtle parameter settings, especially in nonlinear dynamical system feature computation. Nevertheless, the extracted features at a high cost contain many redundant and irrelevant variables that contribute slightly to the performance improvement. For example, Li et al. [62] explored a variety of EEG features in cross-subject emotion recognition, and experimental results indicate that only one or two key features lead to comparative performance to that obtained on the whole feature set. Hence, research on the critical EEG features and variables is still worth conducting. The decided scope of EEG features and variables helps reduce the computation cost in EEG representation, meanwhile, improve the recognition eﬀect. Besides, the decided critical EEG channels help mitigate the diﬃculties in user experiment, e.g., only selecting to attach fewer electrodes on the cortex help to improve the user engagement and reduce the pre-experiment preparation. The critical EEG features and variables also could provide a new perspective to analyze the mechanism of the emotion cognition process. Though several studies mentioned above have taken prior knowledge into the model design. Take the BiDHM, BiDANN, and BiDCNN shown in Figure 13 and Figure 14 for example, the asymmetry correlation information between the bi-hemispheres is utilized, there still exists gaps between the true emo- tion process manifested by the EEG and the information processing modeled by the existing models. It will be better to integrate prior knowledge about the users’ gender, age, physical condition, mental condition, and prior knowledge about the emotional stimuli, the semantic context, the environment, and the knowledge graph about emotion into the model design. Prior knowledge-guided recognition models must obtain an enhanced and robust per- formance on cross-domain learning and few-shot learning settings. Meanwhile, prior knowledge introduces interpretability to the constructed models and the obtained results. • Although abundant cutting-edge artiﬁcial intelligence models have been studied, developing computational methods for emotion recognition needs a deeper understanding of emotion processes and their neural basis. Psychophysiology-inspired, biology-inspired, and brain-inspired cognitive models based on the principle of how the human brain works in the emotion cognition process should also be taken into consideration for us. The popular Deep Learning models only are a less precise mathematical abstraction of the brain functions. They have limitations in online learning, small-sample learning, modeling the information interaction between diﬀerent brain regions. The biologically inspired methods are built on the architecture of the neocortex and try to model the process of how the human brain handles complex information about vision, audio, behavior, and emotion. These biologically inspired methods (e.g., the hierarchical temporal memory model based on neocortex theory [227] and the spiking neural network) are intuitively suitable for modeling brain imaging data and other behavioral data controlled by the neocortex. For example, Luo et al. [226] proposed one spiking neural network (SNN) based model, which makes full use of the spatiotemporal features of the EEG signal. As one kind of brain-inspired computing model, the SNN is able to encode the neural data through the synapses, neurons, and spiking activity. In addition, the Deep Learning model is perceived as one black-box that is hard to understand why they get speciﬁc decisions [228]. How to resolve the problem of the weak statistical interpretability should be taken into consideration for future works, e.g., through the ‘inceptions’ techniques adopted in Google Brain [229], and the model-agnostic explanation approach (LIME) [230]. • Several works mentioned above face the problem of lengthy signal modeling. The EEG signal acquired in one trial with a high sampling rate will be extremely long. As a result, the model computation burden will be largely increased, especially for RNN based models. Hence, researchers should not only focus on the metric of recognition accuracy but also the computational eﬃciency should also be reported. At present, the researches mainly focus on the oﬄine data processing scene. Therefore, the algorithm suitable for real-time emotion recognition and monitoring should be extensively explored. • The ‘domain shift’ problem and ‘transfer learning’ will still be the hot research topics in the next few years. Here we summarize several potential research approaches in these topics. Currently, researchers mainly focus on studying these topics within one single dataset setting, which we can call the intra-dataset-inter-subject modeling problem, in which the user diﬀerence in cultures, ages, gender, and physiology will degrade the perfor- mance. Nevertheless, developing domain adaptation techniques in inter-dataset-inter-subject settings is a more challenging task that deserves careful exploration. As we know, only a few open-source datasets about emotion recognition are available nowadays. If more EEG datasets uncorrelated with

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 29 -->

EEG based Emotion Recognition: A Tutorial and Review • 1:29

emotion recognition can be simultaneously employed, a robust model with more complex structure and more parameters could be trained. Considering the recent advances in the large-scale pre-trained model in natural language processing (e.g., GPT, BERT) [231], we believe it is possible to develop the EEG-oriented pre-trained model on large-scale open-source EEG datasets, which are not limited to emotion recognition. Nevertheless, the EEG data of multi-sources is acquired with diﬀerent devices, diﬀerent experiment designs, diﬀerent types of stimuli, etc. These factors could further increase the discrepancies caused by inter-subject/session variability. Hence, research on ’modeling on multiple source domains’ is another direction worthy of further exploration. In addition, current research on the domain shift problem mainly focuses on domain adaptation of the extracted EEG features. There are lots of room for performance enhancement on the cross-subject, cross-dataset, or cross-session emotion recognition tasks if the raw EEG signals could be calibrated and aligned to common data space in advance before adopting the traditional transfer learning approaches. Researchers who are interested in this research topic can refer to the raw EEG alignment methods based on Riemannian geometry that have been adopted in the motor imagery BCI [182]. • How eﬀective those models perform in an open environment is still unknown. As in real-world scenarios, the people are continuously in a dynamic condition that they may seldomly be calm, which is quite diﬀerent from the controlled experimental environment. Realtime EEG signals are inevitably inﬂuenced by continually evolving activities, including physical factors such as body movements and environmental noise and psychological factors such as mental workloads and attention. The robustness of the emotion recognition system will be aﬀected when people are executing psychological or physical activities. It raises a great challenge to develop recognition models that can capture robust and distinctive emotion-related features from real-time and dynamic EEGs that generalize well under various people states. Researchers should devote themselves to developing open-environment EEG datasets, the corresponding algorithms, and the evaluation criteria. • The reviewed works in this paper were designed on a single EEG modality. In recent years, increasing published articles manifest a shift of research interest from unimodal to multi-modal information-based emotion recognition tasks, in which the multi-modal approaches fuse two or more modal- ities for emotion recognition. This shift is based on some problems that unimodal systems mainly faced. Firstly, the unimodal data may be missing or inconsecutive for some reason, e.g., the monitored signal may be blocked or aﬀected by external obstacles, noise, or device instability. In such a circumstance, the data from other modalities complement the single modality properly. Secondly, the exterior behavioral information sometimes may not be consistent with the actual aﬀective state. An individual may conceal their real feelings under social masks. For example, the same facial ex- pressions may represent diﬀerent psychological activities, so that the single data modality may be insuﬃcient for an accurate recognition task. Last but not least, the recognition performance may be promoted when multi-modal information is fused and utilized, and this is also the ultimate goal of multi modalities-based approaches. For example, Ma et al. [225] developed one LSTM based multi-modal recognition framework that successfully learned the joint information from the original EEG and physiological data, and thus signiﬁcantly improving the recognition eﬀect of the DEAP dataset. Researchers should take as many data modalities as possible into emotion recognition studies, including the EEG, the facial expression, the gesture, the gait, the peripheral physiological signal, the eye movement, etc., to build a comprehensive recognition model. We will devote ourselves to reviewing relevant multi-modal fusion studies in future work.

## ACKNOWLEDGMENTS

This work was supported in part by the Major Science and Technology Innovation Projects of Key R&D Programs of Shandong Province (grant No. 2019JZZY010108 and grant No.2019JZZY010113), the Natural Science Foundation of China (grant No. U1636203 and grant No. 62006212), the Natural Science Foundation of Shandong Province (‘Research on Cross-domain Emotion Recognition Based on Large-scale Pre-trained EEG Model’), the Natural Science Foundation of China (‘Research on pre-trained EEG model for EEG-based cross-domain emotion recognition task’), the fund of State Key Lab. for Novel Software Technology in Nanjing University (grant No. KFKT2021B41), and the Industrial Science and Technology Research Project of Henan Province (grant No. 222102210031).This work was also supportedby the Academy of Finland (grants 336033, 315896), Business Finland (grant 884/31/2018), and EU H2020 (grant 101016775). REFERENCES

[1] Rosalind W Picard. Aﬀective computing. MIT press, 2000. [2] Rosalind W Picard. Building hal: Computers that sense, recognize, and respond to human emotion. In Human Vision and Electronic Imaging VI, volume 4299, pages

518–523. International Society for Optics and Photonics, 2001. [3] Rob Dunne, Tim Morris, and Simon Harper. A survey of ambient intelligence. ACM Computing Surveys (CSUR), 54(4):1–27, 2021. [4] Ralph Adolphs and David J Anderson. The neuroscience of emotion: A new synthesis. Princeton University Press, 2018. [5] Walter B Cannon. The james-lange theory of emotions: A critical examination and an alternative theory. The American journal of psychology, 39(1/4):106–124, 1927. [6] Zahid Halim and Mahma Rehan. On identiﬁcation of driving-induced stress using electroencephalogram signals: A framework based on wearable safety-critical

scheme and machine learning. Information Fusion, 53:66–79, 2020. [7] Viktor Rozgic, Amelio Vazquez-Reina, Michael Crystal, Amit Srivastava, Veasna Tan, and Chris Berka. Multi-modal prediction of ptsd and stress indicators. In 2014

IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pages 3636–3640. IEEE, 2014. [8] Michel Valstar, Björn Schuller, Kirsty Smith, Florian Eyben, Bihan Jiang, Sanjay Bilakhia, Sebastian Schnieder, Roddy Cowie, and Maja Pantic. Avec 2013: the continuous

audio/visual emotion and depression recognition challenge. In Proceedings of the 3rd ACM international workshop on Audio/visual emotion challenge, pages 3–10, 2013. [9] Hanshu Cai, Zhidiao Qu, Zhe Li, Yi Zhang, Xiping Hu, and Bin Hu. Feature-level fusion approaches based on multimodal eeg data for depression recognition.

Information Fusion, 59:127–138, 2020. [10] Aaron T Beck. Cognitive therapy and the emotional disorders. Penguin, 1979. [11] Elif Gümüslü, Duygun Erol Barkana, and Hatice Köse. Emotion recognition using eeg and physiological data for robot-assisted rehabilitation systems. In Companion

Publication of the 2020 International Conference on Multimodal Interaction, pages 379–387, 2020. [12] Hong-Yi Chang, Shih-Chang Huang, and Jia-Hao Wu. A personalized music recommendation system based on electroencephalography feedback. Multimedia Tools

and Applications, 76(19):19523–19542, 2017. [13] Rafael Ramirez, Josep Planas, Nuria Escude, Jordi Mercade, and Cristina Farriols. Eeg-based analysis of the emotional eﬀect of music therapy on palliative care cancer

patients. Frontiers in psychology, 9:254, 2018. [14] Mohammad Soleymani, Jeroen Lichtenauer, Thierry Pun, and Maja Pantic. A multimodal database for aﬀect recognition and implicit tagging. IEEE transactions on

aﬀective computing, 3(1):42–55, 2011. [15] Yashar Moshfeghi and Joemon M Jose. An eﬀective implicit relevance feedback technique using aﬀective, physiological and behavioural features. In Proceedings of

the 36th international ACM SIGIR conference on Research and development in information retrieval, pages 133–142, 2013. [16] Sander Koelstra and Ioannis Patras. Fusion of facial expressions and eeg for implicit aﬀective tagging. Image and Vision Computing, 31(2):164–174, 2013. [17] Ioannis Arapakis, Yashar Moshfeghi, Hideo Joho, Reede Ren, David Hannah, and Joemon M Jose. Enriching user proﬁling with aﬀective features for the improvement

of a multimodal recommender system. In Proceedings of the ACM international conference on image and video retrieval, pages 1–8, 2009. [18] Yashar Moshfeghi. Role of emotion in information retrieval. PhD thesis, University of Glasgow, 2012. [19] Ali Yadollahi, Ameneh Gholipour Shahraki, and Osmar R Zaiane. Current state of text sentiment analysis from opinion to emotion mining. ACM Computing Surveys

(CSUR), 50(2):1–33, 2017.

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 30 -->

1:30 • Li and Zhang, et al.

[20] Talha Burak Alakus, Murat Gonen, and Ibrahim Turkoglu. Database for an emotion recognition system based on eeg signals and various computer games–gameemo.

Biomedical Signal Processing and Control, 60:101951, 2020. [21] Kalliopi Evangelia Stavroulia, Maria Christoﬁ, Evangelia Baka, Despina Michael-Grigoriou, Nadia Magnenat-Thalmann, and Andreas Lanitis. Assessing the emotional

impact of virtual reality-based teacher training. The International Journal of Information and Learning Technology, 2019. [22] Mikko Vesisenaho, Merja Juntunen, P Johanna, Janne Fagerlund, Iryna Miakush, Tiina Parviainen, et al. Virtual reality in education: Focus on the role of emotions

and physiological reactivity. Journal For Virtual Worlds Research, 12(1), 2019. [23] Fabien Lotte, Laurent Bougrain, Andrzej Cichocki, Maureen Clerc, Marco Congedo, Alain Rakotomamonjy, and Florian Yger. A review of classiﬁcation algorithms for

eeg-based brain–computer interfaces: a 10 year update. Journal of neural engineering, 15(3):031005, 2018. [24] Soraia M Alarcao and Manuel J Fonseca. Emotions recognition using eeg signals: A survey. IEEE Transactions on Aﬀective Computing, 10(3):374–393, 2017. [25] Didar Dadebayev, Wei Wei Goh, and Ee Xion Tan. Eeg-based emotion recognition: Review of commercial eeg devices and machine learning techniques. Journal of

King Saud University-Computer and Information Sciences, 2021. [26] Nazmi Soﬁan Suhaimi, James Mountstephens, and Jason Teo. Eeg-based emotion recognition: A state-of-the-art review of current trends and opportunities. Compu-

tational intelligence and neuroscience, 2020, 2020. [27] Resham Arya, Ashok Kumar, and Megha Bhushan. Aﬀect recognition using brain signals: A survey. In Computational Methods and Data Engineering, pages 529–552.

Springer, 2021. [28] Md Mustaﬁzur Rahman, Ajay Krishno Sarkar, Md Amzad Hossain, Md Selim Hossain, Md Rabiul Islam, Md Biplob Hossain, Julian MW Quinn, and Mohammad Ali

Moni. Recognition of human emotions using eeg signals: A review. Computers in Biology and Medicine, 136:104696, 2021. [29] Alexander Craik, Yongtian He, and Jose L Contreras-Vidal. Deep learning for electroencephalogram (eeg) classiﬁcation tasks: a review. Journal of neural engineering,

16(3):031001, 2019. [30] Paul Ekman. Darwin’s contributions to our understanding of emotional expressions. Philosophical Transactions of the Royal Society B: Biological Sciences, 364(1535):

3449–3451, 2009. [31] Paul Ekman. Basic emotions. In Tim Dalgleish and Mick Power, editors, Handbook of Cognition and Emotion, pages 45–60. Hoboken, United States: John Wiley & Sons

Inc., 1999. [32] Robert Plutchik. Emotions and Life: Perspectives from Psychology, Biology, and Evolution. Washington, United States: American Psychological Association, 2003. [33] Robert Plutchik and Henry Kellerman. Theories of emotion, volume 1. Academic Press, 2013. [34] Parrott and W. Gerrod. Emotions in Social Psychology: Essential Readings. Oxfordshire, United Kingdom: Taylor & Francis Group, 2001. [35] James A Russell. Aﬀective space is bipolar. Journal of Personality and Social Psychology, 37(3):345–356, 1979. [36] Sandra JE Langeslag. Eﬀects of organization and disorganization on pleasantness, calmness, and the frontal negativity in the event-related potential. PloS one, 13(8):

e0202726, 2018. [37] Louis A Schmidt and Laurel J Trainor. Frontal brain electrical activity (eeg) distinguishes valence and intensity of musical emotions. Cognition & Emotion, 15(4):

487–500, 2001. [38] Ralph Adolphs, Daniel Tranel, Hanna Damasio, and Antonio Damasio. Impaired recognition of emotion in facial expressions following bilateral damage to the human

amygdala. Nature, 372(6507):669–672, 1994. [39] Heather C Lench, Sarah A Flores, and Shane W Bench. Discrete emotions predict changes in cognition, judgment, experience, behavior, and physiology: a meta-analysis

of experimental emotion elicitations. Psychological bulletin, 137(5):834, 2011. [40] Kristen A Lindquist, Tor D Wager, Hedy Kober, Eliza Bliss-Moreau, and Lisa Feldman Barrett. The brain basis of emotion: a meta-analytic review. The Behavioral and

brain sciences, 35(3):121, 2012. [41] Joseph LeDoux. Rethinking the emotional brain. Neuron, 73(4):653–676, 2012. [42] Jennifer C Britton, K Luan Phan, Stephan F Taylor, Robert C Welsh, Kent C Berridge, and Israel Liberzon. Neural correlates of social and nonsocial emotions: An fmri

study. Neuroimage, 31(1):397–409, 2006. [43] Barry Gordon, John Hart Jr, Ronald P Lesser, and Santiago Arroyo. Mapping cerebral sites for emotion and emotional expression with direct cortical electrical

stimulation and seizure discharges. Progress in brain research, 107:617–622, 1996. [44] J Péron, I Biseul, E Leray, S Vicente, F Le Jeune, S Drapier, D Drapier, P Sauleau, C Haegelen, and M Vérin. Subthalamic nucleus stimulation aﬀects fear and sadness

recognition in parkinson’s disease. Neuropsychology, 24(1):1–8, 2010. [45] T Satow, K Usui, M Matsuhashi, J Yamamoto, T Begum, Hiroshi Shibasaki, A Ikeda, N Mikuni, S Miyamoto, and N Hashimoto. Mirth and laughter arising from human

temporal cortex. Journal of Neurology, Neurosurgery & Psychiatry, 74(7):1004–1005, 2003. [46] Guadalupe Fernández-Baca Vaca, Hans O Lüders, Maysaa Merhi Basha, and Jonathan P Miller. Mirth and laughter elicited during brain stimulation. Epileptic Disorders,

13(4):435–440, 2011. [47] R. J. Davidson. Anterior cerebral asymmetry and the nature of emotion. Brain and Cognition, 20(1):125–151, 1992. [48] R. J. Davidson. What does the prefrontal cortex "do" in aﬀect: perspectives on frontal eeg asymmetry research. Biological Psychology, 67(1):219–234, 2004. [49] Stefan Koelsch. Brain correlates of music-evoked emotions. Nature Reviews Neuroscience, 15(3):170–180, 2014. [50] Massimiliano Palmiero and Laura Piccardi. Frontal eeg asymmetry of mood: A mini-review. Frontiers in Behavioral Neuroscience, 11:224, 2017. [51] Daniela Sammler, Maren Grigutsch, Thomas Fritz, and Stefan Koelsch. Music and emotion: electrophysiological correlates of the processing of pleasant and unpleasant

music. Psychophysiology, 44(2):293–304, 2007. [52] Ian Daly, Asad Malik, Faustina Hwang, Etienne Roesch, James Weaver, Alexis Kirke, Duncan Williams, Eduardo Miranda, and Slawomir J Nasuto. Neural correlates

of emotional responses to music: an eeg study. Neuroscience letters, 573:52–57, 2014. [53] LI Aftanas, NV Reva, LN Savotina, and VP Makhnev. Neurophysiological correlates of induced discrete emotions in humans: an individually oriented analysis.

Neuroscience and Behavioral Physiology, 36(2):119–130, 2006. [54] Sander Koelstra, Christian Muhl, Mohammad Soleymani, Jong-Seok Lee, Ashkan Yazdani, Touradj Ebrahimi, Thierry Pun, Anton Nijholt, and Ioannis Patras. Deap: A

database for emotion analysis; using physiological signals. IEEE Transactions on Aﬀective Computing, 3(1):18–31, 2012. [55] Michela Balconi and Claudio Lucchiari. Consciousness and arousal eﬀects on emotional face processing as revealed by brain oscillations. a gamma band analysis.

International Journal of Psychophysiology, 67(1):41–46, 2008. [56] Kai Yang, Li Tong, Jun Shu, Ning Zhuang, Bin Yan, and Ying Zeng. High gamma band eeg closely related to emotion: evidence from functional network. Frontiers in

human neuroscience, 14:89, 2020. [57] Dirk Hagemann, Ewald Naumann, Alexander Lürken, Gabriele Becker, Stefanie Maier, and Dieter Bartussek. Eeg asymmetry, dispositional mood and personality.

Personality and Individual Diﬀerences, 27(3):541–568, 1999. [58] James A Coan and John JB Allen. Frontal eeg asymmetry as a moderator and mediator of emotion. Biological Psychology, 67(1-2):7–50, 2004. [59] Mu Li and Bao-Liang Lu. Emotion classiﬁcation based on gamma-band eeg. In 2009 Annual International Conference of the IEEE Engineering in medicine and biology

society, pages 1223–1226. IEEE, 2009. [60] Weilong Zheng and Baoliang Lu. Investigating critical frequency bands and channels for eeg-based emotion recognition with deep neural networks. IEEE Transactions

on Autonomous Mental Development, 7(3):162–175, 2015. [61] Jinpeng Li, Zhaoxiang Zhang, and Huiguang He. Hierarchical convolutional neural networks for eeg-based emotion recognition. Cognitive Computation, pages 1–13,

2018. [62] Xiang. Li, Dawei. Song, Peng. Zhang, Yazhou. Zhang, Yuexian. Hou, and Bin. Hu. Exploring eeg features in cross-subject emotion recognition. Frontiers in Neuroscience,

12:162, 2018. [63] Daimi Syed Naser and Goutam Saha. Inﬂuence of music liking on eeg based emotion recognition. Biomedical Signal Processing and Control, 64:102251, 2021. [64] Ning Zhuang, Ying Zeng, Kai Yang, Chi Zhang, Li Tong, and Bin Yan. Investigating patterns for self-induced emotion recognition from eeg signals. Sensors, 18(3):841,

2018. [65] AlexandraC Constantinescu, Maria Wolters, Adam Moore, and Sarah E MacPherson. A cluster-based approach to selecting representative stimuli from the international

aﬀective picture system (iaps) database. Behavior research methods, 49(3):896–912, 2017. [66] Alberto Greco, Gaetano Valenza, Luca Citi, and Enzo Pasquale Scilingo. Arousal and valence recognition of aﬀective sounds based on electrodermal activity. IEEE

Sensors Journal, 17(3):716–725, 2016. [67] Wenzhuo Zhang, Lin Shu, Xiangmin Xu, and Dan Liao. Aﬀective virtual reality system (avrs): design and ratings of aﬀective vr scenes. In 2017 International Conference

on Virtual Reality and Visualization (ICVRV), pages 311–314. IEEE, 2017.

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 31 -->

EEG based Emotion Recognition: A Tutorial and Review • 1:31

[68] Stamos Katsigiannis and Naeem Ramzan. Dreamer: A database for emotion recognition through eeg and ecg signals from wireless low-cost oﬀ-the-shelf devices. IEEE

Journal of Biomedical and Health Informatics, 22(1):98–107, 2018. [69] Panagiotis C Petrantonakis and Leontios J Hadjileontiadis. Emotion recognition from brain signals using hybrid adaptive ﬁltering and higher order crossings analysis.

IEEE Transactions on Aﬀective Computing, 1(2):81–97, 2010. [70] Zirui Lan, Olga Sourina, Lipo Wang, and Yisi Liu. Real-time eeg-based emotion monitoring using stable features. The Visual Computer, 32(3):347–358, 2016. [71] Jonas K Olofsson, Steven Nordin, Henrique Sequeira, and John Polich. Aﬀective picture processing: an integrative review of erp ﬁndings. Biological psychology, 77(3):

247–265, 2008. [72] Edward Bernat, Scott Bunce, and Howard Shevrin. Event-related brain potentials diﬀerentiate positive and negative mood adjectives during both supraliminal and

subliminal visual processing. International Journal of Psychophysiology, 42(1):11–34, 2001. [73] Christos A Frantzidis, Charalampos Bratsas, Christos L Papadelis, Evdokimos Konstantinidis, Costas Pappas, and Panagiotis D Bamidis. Toward emotion aware

computing: an integrated approach using multichannel neurophysiological recordings and aﬀective visual stimuli. IEEE Transactions on Information Technology in Biomedicine, 14(3):589–597, 2010. [74] Xiaowei Wang, Dan Nie, and Baoliang Lu. Emotional state classiﬁcation from eeg data using machine learning approach. Neurocomputing, 129:94–106, 2014. [75] Yuan-Pin Lin, Chi-Hong Wang, Tien-Lin Wu, Shyh-Kang Jeng, and Jyh-Horng Chen. Eeg-based emotion recognition in music listening: A comparison of schemes for

multiclass support vector machine. In Proceedings of the 2009 IEEE international conference on acoustics, speech and signal processing, pages 489–492. IEEE, 2009. [76] Yong-Jin Liu, Minjing Yu, Guozhen Zhao, Jinjing Song, Yan Ge, and Yuanchun Shi. Real-time movie-induced discrete emotion recognition from eeg signals. IEEE

Transactions on Aﬀective Computing, 9(4):550–562, 2018. [77] Majid Memarian Sorkhabi. Emotion detection from eeg signals with continuous wavelet analyzing. American Journal of Computing Research Repository, 2(4):66–70,

2014. [78] Zeynab Mohammadi, Javad Frounchi, and Mahmood Amiri. Wavelet-based emotion recognition system using eeg signal. Neural Computing and Applications, 28(8):

1985–1990, 2017. [79] A. Subasi. Automatic recognition of alertness level from eeg by using neural network and wavelet coeﬃcients. Expert systems with applications, 28(4):701–711, 2005. [80] T. Gandhi, B. K. Panigrahi, and S. Anand. A comparative study of wavelet families for eeg signal classiﬁcation. Neurocomputing, 74(17):3051–3057, 2011. [81] Ahmet Mert and Aydin Akan. Emotion recognition from eeg signals by using multivariate empirical mode decomposition. Pattern Analysis and Applications, 21(1):

81–89, 2018. [82] C J Stam. Nonlinear dynamical analysis of eeg and meg. Clinical Neurophysiology, 116(10):2266–2301, 2005. [83] Vladimir Kulish, Alexei Sourin, and Olga Sourina. Human electroencephalograms seen as fractal time series: Mathematical analysis and visualization. Computers in

Biology and Medicine, 36(3):291–302, 2006. [84] Qiang Wang, Olga Sourina, and Minh Khoa Nguyen. Fractal dimension based neurofeedback in serious games. The Visual Computer, 27(4):299–309, 2011. [85] Yisi Liu, Olga Sourina, and Minh Khoa Nguyen. Real-time eeg-based human emotion recognition and visualization. In Proceedings of the 2010 International Conference

on Cyberworlds, pages 262–269. IEEE, 2010. [86] Behshad Hosseinifard, Mohammad Hassan Moradi, and Reza Rostami. Classifying depression patients and normal subjects using machine learning techniques and

nonlinear features from eeg signal. Computer Methods and Programs in Biomedicine, 109(3):339–345, 2013. [87] Yisi Liu and Olga Sourina. Eeg-based subject-dependent emotion recognition algorithm using fractal dimension. In Proceedings of the 2014 IEEE International Conference

on Systems, Man, and Cybernetics, pages 3166–3171. IEEE, 2014. [88] Jean-Pierre Eckmann, S Oliﬀson Kamphorst, David Ruelle, et al. Recurrence plots of dynamical systems. World Scientiﬁc Series on Nonlinear Science Series A, 16:

441–446, 1995. [89] Guangliang Yu, Xiang Li, Dawei Song, Xiaozhao Zhao, Peng Zhang, Yuexian Hou, and Bin Hu. Encoding physiological signals as images for aﬀective state recognition

using convolutional neural networks. In 2016 38th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), pages 812–815. IEEE, 2016. [90] Yu-Xuan Yang, Zhong-Ke Gao, Xin-Min Wang, Yan-Li Li, Jing-Wei Han, Norbert Marwan, and Jürgen Kurths. A recurrence quantiﬁcation analysis-based channel-

frequency convolutional neural network for emotion recognition from eeg. Chaos: An Interdisciplinary Journal of Nonlinear Science, 28(8):085724, 2018. [91] Li-Chen Shi, Ying-Ying Jiao, and Bao-Liang Lu. Diﬀerential entropy feature for eeg-based vigilance estimation. In 2013 35th Annual International Conference of the

IEEE Engineering in Medicine and Biology Society (EMBC), pages 6627–6630. IEEE, 2013. [92] Beatriz García-Martínez, Arturo Martinez-Rodrigo, Raul Alcaraz, and Antonio Fernández-Caballero. A review on nonlinear methods using electroencephalographic

recordings for emotion recognition. IEEE Transactions on Aﬀective Computing, 2019. [93] Nancy Aaron Jones and Nathan A Fox. Electroencephalogram asymmetry during emotionally evocative ﬁlms and its relation to positive and negative aﬀectivity. Brain

and Cognition, 20(2):280–299, 1992. [94] D Mathersul, L. M. Williams, P. J. Hopkinson, and A. H. Kemp. Investigating models of aﬀect: relationships among eeg alpha asymmetry, depression, and anxiety.

Emotion, 8(4):560–572, 2008. [95] Douglas N Greve, Lise Van der Haegen, Qing Cai, Steven Stuﬄebeam, Mert R Sabuncu, Bruce Fischl, and Marc Brysbaert. A surface-based analysis of language

lateralization and cortical asymmetry. Journal of cognitive neuroscience, 25(9):1477–1492, 2013. [96] Nattapong Thammasan, Koichi Moriyama, Ken Ichi Fukui, and Masayuki Numao. Continuous music-emotion recognition based on electroencephalogram. IEICE

Transactions on Information and Systems, 99(4):1234–1241, 2016. [97] Dong Huang, Cuntai Guan, Kai Keng Ang, Haihong Zhang, and Yaozhang Pan. Asymmetric spatial pattern for eeg-based emotion detection. In Proceedings of the

2012 International Joint Conference on Neural Networks (IJCNN), pages 1–7. IEEE, 2012. [98] Panagiotis C. Petrantonakis and Leontios J. Hadjileontiadis. Adaptive emotional information retrieval from eeg signals in the time-frequency domain. IEEE Transactions

on Signal Processing, 60(5):2604–2616, 2012. [99] Ed Bullmore and Olaf Sporns. The economy of brain network organization. Nature Reviews Neuroscience, 13(5):336–349, 2012. [100] Min Wang, Heba El-Fiqi, Jiankun Hu, and Hussein A Abbass. Convolutional neural networks using dynamic functional connectivity for eeg-based person identiﬁcation

in diverse human states. IEEE Transactions on Information Forensics and Security, 14(12):3259–3272, 2019. [101] Youyun Lee and Shulan Hsieh. Classifying diﬀerent emotional states by means of eeg-based functional connectivity patterns. PloS one, 9(4):e95415, 2014. [102] Richard F Betzel and Danielle S Bassett. Multi-scale brain networks. Neuroimage, 160:73–83, 2017. [103] N Rotem-Kohavi, TF Oberlander, and N Virji-Babul. Infants and adults have similar regional functional brain organization for the perception of emotions. Neuroscience

letters, 650:118–125, 2017. [104] Jichi Chen, Hong Wang, and Chengcheng Hua. Assessment of driver drowsiness using electroencephalogram signals based on multiple functional brain networks.

International Journal of Psychophysiology, 133:120–130, 2018. [105] Eli Kinney-Lang, Michael Yoong, Matthew Hunter, Krishnaraya Kamath Tallur, Jay Shetty, Ailsa McLellan, Richard FM Chin, and Javier Escudero. Analysis of eeg

networks and their correlation with cognitive impairment in preschool children with epilepsy. Epilepsy & Behavior, 90:45–56, 2019. [106] Francesco Carlo Morabito, Maurizio Campolo, Domenico Labate, Giuseppe Morabito, Lilla Bonanno, Alessia Bramanti, Simona De Salvo, Angela Marra, and Placido

Bramanti. A longitudinal eeg study of alzheimer’s disease progression based on a complex network approach. International journal of neural systems, 25(02):1550005, 2015. [107] Willem De Haan, Yolande AL Pijnenburg, Rob LM Strijers, Yolande van der Made, Wiesje M van der Flier, Philip Scheltens, and Cornelis J Stam. Functional neural

network analysis in frontotemporal dementia and alzheimer’s disease using eeg and graph theory. BMC neuroscience, 10(1):1–12, 2009. [108] Raﬀaella Franciotti, Nicola Walter Falasca, Dario Arnaldi, Francesco Famà, Claudio Babiloni, Marco Onofrj, Flavio Mariano Nobili, and Laura Bonanni. Cortical

network topology in prodromal and mild dementia due to alzheimer’s disease: graph theory applied to resting state eeg. Brain topography, 32(1):127–141, 2019. [109] Francisco Varela, Jean-Philippe Lachaux, Eugenio Rodriguez, and Jacques Martinerie. The brainweb: phase synchronization and large-scale integration. Nature reviews

neuroscience, 2(4):229–239, 2001. [110] He Chen, Yan Song, and Xiaoli Li. A deep learning framework for identifying children with adhd using an eeg-based brain network. Neurocomputing, 356:83–96, 2019. [111] Isabelle Guyon and André Elisseeﬀ. An introduction to variable and feature selection. Journal of Machine Learning Research, 3(Mar):1157–1182, 2003. [112] Jinjie Huang, Yunze Cai, and Xiaoming Xu. A ﬁlter approach to feature selection based on mutual information. In Proceedings of 5th IEEE International Conference on

Cognitive Informatics, volume 1, pages 84–89. New York: IEEE Press, 2006. doi: 10.1109/COGINF.2006.365681. [113] Sebastián Maldonado and Richard Weber. A wrapper method for feature selection using support vector machines. Information Sciences, 179(13):2208–2217, 2008. doi:

10.1016/j.ins.2009.02.014.

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 32 -->

1:32 • Li and Zhang, et al.

[114] Chris Ding and Hanchuan Peng. Minimum redundancy feature selection from microarray gene expression data. Journal of bioinformatics and computational biology,

3(02):185–205, 2005. [115] John Atkinson and Daniel Campos. Improving bci-based emotion recognition by combining eeg feature selection and kernel classiﬁers. Expert Systems with Applications,

47:35–41, 2016. [116] Isabelle Guyon, Jason Weston, Stephen Barnhill, and Vladimir Vapnik. Gene selection for cancer classiﬁcation using support vector machines. Machine Learning, 46

(1):389–422, 2002. doi: 10.1023/A:1012487302797. [117] Andrew Y. Ng. Feature selection, L1 vs. L2 regularization, and rotational invariance. In Proceedings of the 21st International Conference on Machine Learning, pages

78–85. New York: ACM Press, 2004. doi: 10.1145/1015330.1015435. [118] Stefan Haufe, Frank Meinecke, Kai Görgen, Sven Dähne, J. D. Haynes, Benjamin Blankertz, and Felix Bießmann. On the interpretation of weight vectors of linear

models in multivariate neuroimaging. Neuroimage, 87(2):96–110, 2014. doi: 10.1016/j.neuroimage.2013.10.067. [119] Trung Duy Pham, Dat Tran, Wanli Ma, and Nga Thuy Tran. Enhancing performance of eeg-based emotion recognition systems using feature smoothing. In Interna-

tional Conference on Neural Information Processing, pages 95–102. Springer, 2015. [120] Cheng Tang, Di Wang, Ah-Hwee Tan, and Chunyan Miao. Eeg-based emotion recognition via fast and robust feature smoothing. In International Conference on Brain

Informatics, pages 83–92. Springer, 2017. [121] Yaqing Zhang, Jinling Chen, Jen Hong Tan, Yuxuan Chen, Yunyi Chen, Dihan Li, Lei Yang, Jian Su, Xin Huang, and Wenliang Che. An investigation of deep learning

models for eeg-based emotion recognition. Frontiers in Neuroscience, 14, 2020. [122] Seong Youb Chung and Hyun Joong Yoon. Aﬀective classiﬁcation using bayesian classiﬁer and supervised learning. In Proceedings of the 2012 12th International

Conference on Control, Automation and Systems, pages 1768–1771. IEEE, 2012. [123] Pascal Ackermann, Christian Kohlschein, Jó Agila Bitsch, Klaus Wehrle, and Sabina Jeschke. Eeg-based automatic emotion recognition: Feature extraction, selection

and classiﬁcation methods. In Proceedings of the 2016 18th International Conference on e-Health Networking, Applications and Services (Healthcom), pages 1–6. IEEE, 2016. [124] Adnan Mehmood Bhatti, Muhammad Majid, Syed Muhammad Anwar, and Bilal Khan. Human emotion recognition and analysis in response to audio music using

brain signals. Computers in Human Behavior, 65:267–275, 2016. [125] M Murugappan, M Rizon, R Nagarajan, S Yaacob, I Zunaidi, and D Hazry. Lifting scheme for human emotion recognition using eeg. In Proceedings of the 2008

International symposium on information technology, volume 2, pages 1–7. IEEE, 2008. [126] Robert Jenke, Angelika Peer, and Martin Buss. Feature extraction and selection for emotion recognition from eeg. IEEE Transactions on Aﬀective Computing, 5(3):

327–339, 2014. [127] Yang Li, Wenming Zheng, Zhen Cui, Yuan Zong, and Sheng Ge. Eeg emotion recognition based on graph regularized sparse linear regression. Neural Processing Letters,

49(2):555–571, 2019. [128] Juan Cheng, Meiyao Chen, Chang Li, Yu Liu, Rencheng Song, Aiping Liu, and Xun Chen. Emotion recognition from multi-channel eeg via deep forest. IEEE Journal

of Biomedical and Health Informatics, 25(2):453–464, 2020. [129] Franco Scarselli and Ah Chung Tsoi. Universal approximation using feedforward neural networks: A survey of some existing methods, and some new results. Neural

networks, 11(1):15–37, 1998. [130] Nattapong Thammasan, Ken-ichi Fukui, and Masayuki Numao. Application of deep belief networks in eeg-based dynamic music-emotion recognition. In Proceedings

of the 2016 International Joint Conference on Neural Networks (IJCNN), pages 881–888. IEEE, 2016. [131] Geoﬀrey E Hinton, Simon Osindero, and Yee-Whye Teh. A fast learning algorithm for deep belief nets. Neural computation, 18(7):1527–1554, 2006. [132] Samarth Tripathi, Shrinivas Acharya, Ranti Dev Sharma, Sudhanshi Mittal, and Samit Bhattacharya. Using deep and convolutional neural networks for accurate

emotion classiﬁcation on deap dataset. In Proceedings of the 21st AAAI Conference on Artiﬁcial Intelligence, pages 4746–4752. AAAI Press, 2017. [133] Hao Chao, Liang Dong, Yongli Liu, and Baoyun Lu. Emotion recognition from multiband eeg signals using capsnet. Sensors, 19(9):2212, 2019. [134] Sara Sabour, Nicholas Frosst, and Geoﬀrey E Hinton. Dynamic routing between capsules. In Proceedings of the 31st International Conference on Neural Information

Processing Systems, pages 3859–3869, 2017. [135] Yu Liu, Yufeng Ding, Chang Li, Juan Cheng, Rencheng Song, Feng Wan, and Xun Chen. Multi-channel eeg-based emotion recognition via a multi-level features guided

capsule network. Computers in Biology and Medicine, 123:103927, 2020. [136] Felipe Petroski Such, Shagan Sah, Miguel Alexander Dominguez, Suhas Pillai, Chao Zhang, Andrew Michael, Nathan D Cahill, and Raymond Ptucha. Robust spatial

ﬁltering with graph convolutional neural networks. IEEE Journal of Selected Topics in Signal Processing, 11(6):884–896, 2017. [137] Tengfei Song, Wenming Zheng, Peng Song, and Zhen Cui. Eeg emotion recognition using dynamical graph convolutional neural networks. IEEE Transactions on

Aﬀective Computing, 11(3):532–541, 2018. [138] Tong Zhang, Zhen Cui, Chunyan Xu, Wenming Zheng, and Jian Yang. Variational pathway reasoning for eeg emotion recognition. In Proceedings of the AAAI

Conference on Artiﬁcial Intelligence, pages 2709–2716, 2020. [139] Ralph Adolphs. Neural systems for recognizing emotion. Current opinion in neurobiology, 12(2):169–177, 2002. [140] Ed Bullmore and Olaf Sporns. Complex brain networks: graph theoretical analysis of structural and functional systems. Nature reviews neuroscience, 10(3):186–198,

2009. [141] Yang Li, Lei Wang, Wenming Zheng, Yuan Zong, Lei Qi, Zhen Cui, Tong Zhang, and Tengfei Song. A novel bi-hemispheric discrepancy model for eeg emotion

recognition. IEEE Transactions on Cognitive and Developmental Systems, 13(2):354–367, 2020. [142] Yang Li, Wenming Zheng, Zhen Cui, Tong Zhang, and Yuan Zong. A novel neural network model based on cerebral hemispheric asymmetry for eeg emotion recognition. In IJCAI, pages 1561–1567, 2018. [143] Dongmin Huang, Sentao Chen, Cheng Liu, Lin Zheng, Zhihang Tian, and Dazhi Jiang. Diﬀerences ﬁrst in asymmetric brain: A bi-hemisphere discrepancy convolutional

neural network for eeg emotion recognition. Neurocomputing, 448:140–151, 2021. [144] Heng Cui, Aiping Liu, Xu Zhang, Xiang Chen, Kongqiao Wang, and Xun Chen. Eeg-based emotion recognition using an end-to-end regional-asymmetric convolutional

neural network. Knowledge-Based Systems, 205:106243, 2020. [145] Vernon J Lawhern, Amelia J Solon, Nicholas R Waytowich, Stephen M Gordon, Chou P Hung, and Brent J Lance. Eegnet: a compact convolutional neural network for

eeg-based brain–computer interfaces. Journal of neural engineering, 15(5):056013, 2018. [146] Yi Wang, Zhiyi Huang, Brendan McCane, and Phoebe Neo. Emotionet: A 3-d convolutional neural network for eeg-based emotion recognition. In 2018 International

Joint Conference on Neural Networks (IJCNN), pages 1–7. IEEE, 2018. [147] Md Rabiul Islam, Md Milon Islam, Md Mustaﬁzur Rahman, Chayan Mondal, Suvojit Kumar Singha, Mohiuddin Ahmad, Abdul Awal, Md Saiful Islam, and Moham-

mad Ali Moni. Eeg channel correlation based model for emotion recognition. Computers in Biology and Medicine, 136:104757, 2021. [148] Elham S Salama, Reda A El-Khoribi, Mahmoud E Shoman, and Mohamed A Wahby Shalaby. Eeg-based emotion recognition using 3d convolutional neural networks.

Int. J. Adv. Comput. Sci. Appl, 9(8):329–337, 2018. [149] Jungchan Cho and Hyoseok Hwang. Spatio-temporal representation of an electoencephalogram for emotion recognition using a three-dimensional convolutional

neural network. Sensors, 20(12):3491, 2020. [150] Yi Ding, Neethu Robinson, Qiuhao Zeng, Duo Chen, Aung Aung Phyo Wai, Tih-Shih Lee, and Cuntai Guan. Tsception: a deep learning framework for emotion

detection using eeg. In 2020 International Joint Conference on Neural Networks (IJCNN), pages 1–7. IEEE, 2020. [151] Chen Wei, Lan-lan Chen, Zhen-zhen Song, Xiao-guang Lou, and Dong-dong Li. Eeg-based emotion recognition using simple recurrent units network and ensemble

learning. Biomedical Signal Processing and Control, 58:101756, 2020. [152] Shuiwang Ji, Wei Xu, Ming Yang, and Kai Yu. 3d convolutional neural networks for human action recognition. IEEE transactions on pattern analysis and machine

intelligence, 35(1):221–231, 2012. [153] Ziyu Jia, Youfang Lin, Xiyang Cai, Haobin Chen, Haijun Gou, and Jing Wang. Sst-emotionnet: Spatial-spectral-temporal based attention 3d dense network for eeg

emotion recognition. In Proceedings of the 28th ACM International Conference on Multimedia, pages 2909–2917, 2020. [154] Xiang Li, Dawei Song, Peng Zhang, Guangliang Yu, Yuexian Hou, and Bin Hu. Emotion recognition from multi-channel eeg data through convolutional recurrent

neural network. In 2016 IEEE international conference on bioinformatics and biomedicine (BIBM), pages 352–359. IEEE, 2016. [155] Dalin Zhang, Lina Yao, Xiang Zhang, Sen Wang, Weitong Chen, Robert Boots, and Boualem Benatallah. Cascade and parallel convolutional recurrent neural networks

on eeg-based intention recognition for brain computer interface. In Proceedings of the AAAI Conference on Artiﬁcial Intelligence, 2018.

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 33 -->

EEG based Emotion Recognition: A Tutorial and Review • 1:33

[156] Yilong Yang, Qingfeng Wu, Ming Qiu, Yingdong Wang, and Xiaowei Chen. Emotion recognition from multi-channel eeg through parallel convolutional recurrent

neural network. In 2018 International Joint Conference on Neural Networks (IJCNN), pages 1–7. IEEE, 2018. [157] Wei Tao, Chang Li, Rencheng Song, Juan Cheng, Yu Liu, Feng Wan, and Xun Chen. Eeg-based emotion recognition via channel-wise attention and self attention. IEEE

Transactions on Aﬀective Computing, 2020. [158] Yang Li, Wenming Zheng, Lei Wang, Yuan Zong, and Zhen Cui. From regional to global brain: A novel hierarchical spatial-temporal neural network model for eeg

emotion recognition. IEEE Transactions on Aﬀective Computing, 2019. [159] Tong Zhang, Wenming Zheng, Zhen Cui, Yuan Zong, and Yang Li. Spatial-temporal recurrent neural network for emotion recognition. IEEE transactions on cybernetics,

49(3):839–847, 2019. [160] Wai-Cheong Lincoln Lew, Di Wang, Katsiaryna Shylouskaya, Zhuo Zhang, Joo-Hwee Lim, Kai Keng Ang, and Ah-Hwee Tan. Eeg-based emotion recognition using

spatial-temporal representation via bi-gru. In 2020 42nd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC), pages 116–119. IEEE, 2020. [161] Xiang Li, Zhigang Zhao, Dawei Song, Yazhou Zhang, Jingshan Pan, Lu Wu, Jidong Huo, Chunyang Niu, and Di Wang. Latent factor decoding of multi-channel eeg

for emotion recognition through autoencoder-like neural networks. Frontiers in neuroscience, 14:87, 2020. [162] Xiaofen Xing, Zhenqi Li, Tianyuan Xu, Lin Shu, Bin Hu, and Xiangmin Xu. Sae+ lstm: A new framework for emotion recognition from multi-channel eeg. Frontiers

in neurorobotics, 13:37, 2019. [163] Yongqiang Yin, Xiangwei Zheng, Bin Hu, Yuang Zhang, and Xinchun Cui. Eeg emotion recognition using fusion model of graph convolutional neural networks and

lstm. Applied Soft Computing, 100:106954, 2021. [164] Guangyi Zhang and Ali Etemad. Rfnet: Riemannian fusion network for eeg-based brain-computer interfaces. arXiv preprint arXiv:2008.08633, 2020. [165] Emmanuel K Kalunga, Sylvain Chevallier, Quentin Barthélemy, Karim Djouani, Yskandar Hamam, and Eric Monacelli. From euclidean to riemannian means: Informa-

tion geometry for ssvep classiﬁcation. In International Conference on Geometric Science of Information, pages 595–604. Springer, 2015. [166] Jonghwa Kim and Elisabeth André. Emotion recognition based on physiological changes in music listening. IEEE Transactions on Pattern Analysis and Machine

Intelligence, 30(12):2067–2083, 2008. [167] Omar AlZoubi, Sidney K D’Mello, and Rafael A Calvo. Detecting naturalistic expressions of nonbasic aﬀect using physiological signals. IEEE Transactions on Aﬀective

Computing, 3(3):298–310, 2012. [168] S Hamann and T Canli. Individual diﬀerences in emotion processing. Current Opinion in Neurobiology, 14(2):233–238, 2004. [169] Enrique O Flores-Gutiérrez, José-Luis Díaz, Fernando A Barrios, Miguel Ángel Guevara, Yolanda del Río-Portilla, María Corsi-Cabrera, and Enrique O del Flores-

Gutiérrez. Diﬀerential alpha coherence hemispheric patterns in men and women during pleasant and unpleasant musical emotions. International Journal of Psy- chophysiology, 71(1):43–49, 2009. [170] Maneesh Bilalpur, Seyed Mostafa Kia, Tat-Seng Chua, and Ramanathan Subramanian. Discovering gender diﬀerences in facial emotion recognition via implicit

behavioral cues. In 2017 Seventh International Conference on Aﬀective Computing and Intelligent Interaction (ACII), pages 119–124. IEEE, 2017. [171] Atefeh Goshvarpour and Ateke Goshvarpour. Eeg spectral powers and source localization in depressing, sad, and fun music videos focusing on gender diﬀerences.

Cognitive neurodynamics, 13(2):161–173, 2019. [172] Margaret M Bradley, Maurizio Codispoti, Dean Sabatinelli, and Peter J Lang. Emotion and motivation ii: sex diﬀerences in picture processing. Emotion, 1(3):300, 2001. [173] TMC Lee, HL Liu, CCH Chan, SY Fang, and JH Gao. Neural activities associated with emotion recognition observed in men and women. Molecular psychiatry, 10(5):

450–455, 2005. [174] Kyeon Raab, Peter Kirsch, and Daniela Mier. Understanding the impact of 5-httlpr, antidepressants, and acute tryptophan depletion on brain activation during facial

emotion processing: A review of the imaging literature. Neuroscience & Biobehavioral Reviews, 71:176–197, 2016. [175] Agneta H Fischer, Patricia M Rodriguez Mosquera, Annelies EM Van Vianen, and Antony SR Manstead. Gender and culture diﬀerences in emotion. Emotion, 4(1):87,

2004. [176] Jia-Yi Zhu, Wei-Long Zheng, and Bao-Liang Lu. Cross-subject and cross-gender emotion classiﬁcation from eeg. In World Congress on Medical Physics and Biomedical

Engineering, June 7-12, 2015, Toronto, Canada, pages 1188–1191. Springer, 2015. [177] I Pava, A Álvarez, Paula Herrera, Germán Castellanos-Domínguez, and A Orozco. Gender eﬀects on an eeg-based emotion level classiﬁcation system. In Iberoamerican

Congress on Pattern Recognition, pages 810–819. Springer, Cham, 2018. [178] Y. Huang. Native assessment of international aﬀective picture system. Chinese Mental Health Journal, 2004. [179] Vladimir Kurbalija, Mirjana Ivanović, Miloš Radovanović, Zoltan Geler, Weihui Dai, and Weidong Zhao. Emotion perception and recognition: an exploration of cultural

diﬀerences and similarities. Cognitive Systems Research, 52:103–116, 2018. [180] Lu Gan, Wei Liu, Yun Luo, Xun Wu, and Bao-Liang Lu. A cross-culture study on multimodal emotion recognition using deep learning. In International Conference on

Neural Information Processing, pages 670–680. Springer, 2019. [181] Yasser Mohammad and Toyoaki Nishida. Using physiological signals to detect natural interactive behavior. Applied Intelligence, 33(1):79–92, 2010. [182] Paolo Zanini, Marco Congedo, Christian Jutten, Salem Said, and Yannick Berthoumieu. Transfer learning: A riemannian geometry framework with applications to

brain–computer interfaces. IEEE Transactions on Biomedical Engineering, 65(5):1107–1116, 2017. [183] Javier Fernandez, Nicholas Guttenberg, Olaf Witkowski, and Antoine Pasquali. Cross-subject eeg-based emotion recognition through neural networks with stratiﬁed

normalization. Frontiers in neuroscience, 15:11, 2021. [184] Feng Zhou, Xingda Qu, Martin G Helander, and Jianxin Roger Jiao. Aﬀect prediction from physiological measures via visual stimuli. International Journal of Human-

Computer Studies, 69(12):801–819, 2011. [185] Jeremy N Bailenson, Emmanuel D Pontikakis, Iris B Mauss, James J Gross, Maria E Jabon, Cendri AC Hutcherson, Cliﬀord Nass, and Oliver John. Real-time classiﬁcation

of evoked emotions using facial feature tracking and physiological responses. International Journal of Human-Computer Studies, 66(5):303–317, 2008. [186] Jing Chen, Bin Hu, Yue Wang, Philip Moore, Yongqiang Dai, Lei Feng, and Zhijie Ding. Subject-independent emotion recognition based on physiological signals: a

three-stage decision method. BMC Medical Informatics and Decision Making, 17(3):167, 2017. [187] Jin Liu, Xinke Shen, Sen Song, and Dan Zhang. Domain adaptation for cross-subject emotion recognition by subject clustering. In 2021 10th International IEEE/EMBS

Conference on Neural Engineering (NER), pages 904–908. IEEE, 2021. [188] Zirui Lan, Olga Sourina, Lipo Wang, Reinhold Scherer, and Gernot R Müller-Putz. Domain adaptation techniques for eeg-based emotion recognition: a comparative

study on two public datasets. IEEE Transactions on Cognitive and Developmental Systems, 11(1):85–94, 2018. [189] Yun Luo, Si-Yang Zhang, Wei-Long Zheng, and Bao-Liang Lu. Wgan domain adaptation for eeg-based emotion recognition. In International Conference on Neural

Information Processing, pages 275–286. Springer, 2018. [190] Fei Wang, Weiwei Zhang, Zongfeng Xu, Jingyu Ping, and Hao Chu. A deep multi-source adaptation transfer network for cross-subject electroencephalogram emotion

recognition. Neural Computing and Applications, pages 1–13, 2021. [191] Yucel Cimtay and Erhan Ekmekcioglu. Investigating the use of pretrained convolutional neural network on cross-subject and cross-dataset eeg emotion recognition.

Sensors, 20(7):2034, 2020. [192] Fei Wang, Shichao Wu, Weiwei Zhang, Zongfeng Xu, Yahui Zhang, Chengdong Wu, and Sonya Coleman. Emotion recognition with convolutional neural network

and eeg-based efdms. Neuropsychologia, 146:107506, 2020. [193] He Li, Yi-Ming Jin, Wei-Long Zheng, and Bao-Liang Lu. Cross-subject emotion recognition using deep adaptation networks. In International conference on neural

information processing, pages 403–413. Springer, 2018. [194] Ziliang Cai, Miaomiao Guo, Xinsheng Yang, Xintong Chen, and Guizhi Xu. Cross-subject electroencephalogram emotion recognition based on maximum classiﬁer

discrepancy. Sheng wu yi xue gong cheng xue za zhi= Journal of biomedical engineering= Shengwu yixue gongchengxue zazhi, 38(3):455–462, 2021. [195] Li-Ming Zhao, Xu Yan, and Bao-Liang Lu. Plug-and-play domain adaptation for cross-subject eeg-based emotion recognition. In Proceedings of the 35th AAAI Conference

on Artiﬁcial Intelligence. sn, 2021. [196] Ke-Ming Ding, Tsukasa Kimura, Ken-ichi Fukui, and Masayuki Numao. Eeg emotion enhancement using task-speciﬁc domain adversarial neural network. In 2021

International Joint Conference on Neural Networks (IJCNN), pages 1–8. IEEE, 2021. [197] Yingdong Wang, Jiatong Liu, Qunsheng Ruan, Shuocheng Wang, and Chen Wang. Cross-subject eeg emotion classiﬁcation based on few-label adversarial domain

adaption. Expert Systems with Applications, 185:115581, 2021. [198] Guangyi Zhang and Ali Etemad. Distilling eeg representations via capsules for aﬀective computing. arXiv preprint arXiv:2105.00104, 2021.

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.

<!-- page 34 -->

1:34 • Li and Zhang, et al.

[199] Peixiang Zhong, Di Wang, and Chunyan Miao. Eeg-based emotion recognition using regularized graph neural networks. IEEE Transactions on Aﬀective Computing,

2020. [200] Tiehang Duan, Mihir Chauhan, Mohammad Abuzar Shaikh, Jun Chu, and Sargur Srihari. Ultra eﬃcient transfer learning with meta update for cross subject eeg

classiﬁcation. arXiv preprint arXiv:2003.06113, 2020. [201] Tiehang Duan, Mohammad Abuzar Shaikh, Mihir Chauhan, Jun Chu, Rohini K Srihari, Archita Pathak, and Sargur N Srihari. Meta learn on constrained transfer

learning for low resource cross subject eeg classiﬁcation. IEEE Access, 8:224791–224802, 2020. [202] Magdiel Jiménez-Guarneros and Pilar Gómez-Gil. Standardization-reﬁnement domain adaptation method for cross-subject eeg-based classiﬁcation in imagined speech

recognition. Pattern Recognition Letters, 141:54–60, 2021. [203] Mohammad Soleymani, Maja Pantic, and Thierry Pun. Multimodal emotion recognition in response to videos. IEEE Transactions on Aﬀective Computing, 3(2):211–223,

2012. [204] Zhong Yin, Lei Liu, Jianing Chen, Boxi Zhao, and Yongxiong Wang. Locally robust eeg feature selection for individual-independent emotion recognition. Expert

Systems with Applications, 162:113768, 2020. [205] Zitong Wan, Rui Yang, Mengjie Huang, Nianyin Zeng, and Xiaohui Liu. A review on transfer learning in eeg signal analysis. Neurocomputing, 421:1–14, 2021. [206] Raja Majid Mehmood, Ruoyu Du, and Hyo Jong Lee. Optimal feature selection and deep learning ensembles method for emotion recognition from human brain eeg

sensors. IEEE Access, 5:14797–14806, 2017. [207] Zhong Yin, Mengyuan Zhao, Yongxiong Wang, Jingdong Yang, and Jianhua Zhang. Recognition of emotions using multimodal physiological signals and an ensemble

deep learning model. Computer Methods and Programs in Biomedicine, 140:93–110, 2017. [208] Yu Chen, Rui Chang, and Jifeng Guo. Emotion recognition of eeg signals based on the ensemble learning method: Adaboost. Mathematical Problems in Engineering,

2021, 2021. [209] Murugappn Murugappan, M Rizon, R Nagarajan, S Yaacob, I Zunaidi, and D Hazry. Eeg feature extraction for classifying emotions using fcm and fkm. International

journal of Computers and Communications, 1(2):21–25, 2007. [210] Joseph W Matiko, Stephen P Beeby, and John Tudor. Fuzzy logic based emotion classiﬁcation. In Proceedings of the 2014 IEEE International Conference on Acoustics,

Speech and Signal Processing (ICASSP), pages 4389–4393. IEEE, 2014. [211] Morteza Zangeneh Soroush, Keivan Maghooli, Seyed Kamaledin Setarehdan, and Ali Motie Nasrabadi. A novel method of eeg-based emotion recognition using

nonlinear features variability and dempster–shafer theory. Biomedical Engineering: Applications, Basis and Communications, 30(04):1850026, 2018. [212] Kairui Guo, Rifai Chai, Henry Candra, Ying Guo, Rong Song, Hung Nguyen, and Steven Su. A hybrid fuzzy cognitive map/support vector machine approach for

eeg-based emotion classiﬁcation using compressed sensing. International Journal of Fuzzy Systems, 21(1):263–273, 2019. [213] Fang Wang, Sheng-hua Zhong, Jianfeng Peng, Jianmin Jiang, and Yan Liu. Data augmentation for eeg-based emotion recognition with deep convolutional neural

networks. In International Conference on Multimedia Modeling, pages 82–93. Springer, 2018. [214] Yun Luo, Li-Zhen Zhu, Zi-Yu Wan, and Bao-Liang Lu. Data augmentation for enhancing eeg-based emotion recognition with deep generative models. Journal of

Neural Engineering, 17(5):056021, 2020. [215] Elnaz Lashgari, Dehua Liang, and Uri Maoz. Data augmentation for deep-learning-based electroencephalography. Journal of Neuroscience Methods, page 108885, 2020. [216] Swapnil Bhosale, Rupayan Chakraborty, and Sunil Kumar Kopparapu. Calibration free meta learning based approach for subject independent eeg emotion recognition.

Biomedical Signal Processing and Control, 72:103289, 2022. [217] Xin He, Kaiyong Zhao, and Xiaowen Chu. Automl: A survey of the state-of-the-art. Knowledge-Based Systems, 212:106622, 2021. [218] Hong He, Yonghong Tan, Jun Ying, and Wuxiong Zhang. Strengthen eeg-based emotion recognition using ﬁreﬂy integrated optimization algorithm. Applied Soft

Computing, 94:106426, 2020. [219] Diego Aquino-Brítez, Andrés Ortiz, Julio Ortega, Javier León, Marco Formoso, John Q Gan, and Juan José Escobar. Optimization of deep architectures for eeg signal

classiﬁcation: An automl approach using evolutionary algorithms. Sensors, 21(6):2096, 2021. [220] Weilong Zheng, Jiayi Zhu, and Baoliang Lu. Identifying stable patterns over time for emotion recognition from eeg. arXiv preprint arXiv:1601.02197, 2017. [221] S. Katsigiannis and N. Ramzan. Dreamer: A database for emotion recognition through eeg and ecg signals from wireless low-cost oﬀ-the-shelf devices. IEEE Journal

of Biomedical & Health Informatics, pages 1–1, 2017. [222] Wei-Long Zheng, Wei Liu, Yifei Lu, Bao-Liang Lu, and Andrzej Cichocki. Emotionmeter: A multimodal framework for recognizing human emotions. IEEE transactions

on cybernetics, 49(3):1110–1122, 2018. [223] Tengfei Song, Wenming Zheng, Cheng Lu, Yuan Zong, Xilei Zhang, and Zhen Cui. Mped: A multi-modal physiological emotion database for discrete emotion

recognition. IEEE Access, 7:12177–12191, 2019. [224] Bo-Qun Ma, He Li, Wei-Long Zheng, and Bao-Liang Lu. Reducing the subject variability of eeg signals with adversarial domain generalization. In International

Conference on Neural Information Processing, pages 30–42. Springer, 2019. [225] Jiaxin Ma, Hao Tang, Wei-Long Zheng, and Bao-Liang Lu. Emotion recognition using multimodal residual lstm network. In Proceedings of the 27th ACM International

Conference on Multimedia, pages 176–183, 2019. [226] Yuling Luo, Qiang Fu, Juntao Xie, Yunbai Qin, Guopei Wu, Junxiu Liu, Frank Jiang, Yi Cao, and Xuemei Ding. Eeg-based emotion classiﬁcation using spiking neural

networks. IEEE Access, 8:46007–46016, 2020. [227] Yuwei Cui, Subutai Ahmad, and JeﬀHawkins. The htm spatial pooler—a neocortical algorithm for online sparse distributed coding. Frontiers in computational

neuroscience, 11:111, 2017. [228] Samira Pouyanfar, Saad Sadiq, Yilin Yan, Haiman Tian, Yudong Tao, Maria Presa Reyes, Mei-Ling Shyu, Shu-Ching Chen, and SS Iyengar. A survey on deep learning:

Algorithms, techniques, and applications. ACM Computing Surveys (CSUR), 51(5):1–36, 2018. [229] Alexander Mordvintsev, Christopher Olah, and Mike Tyka. Inceptionism: Going deeper into neural networks, 2015. URL https://research.googleblog.com/2015/06/inceptionism-going-deeper-into-neural.html. [230] Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. Model-agnostic interpretability of machine learning. arXiv preprint arXiv:1606.05386, 2016. [231] Xipeng Qiu, Tianxiang Sun, Yige Xu, Yunfan Shao, Ning Dai, and Xuanjing Huang. Pre-trained models for natural language processing: A survey. Science China

Technological Sciences, pages 1–26, 2020.

ACM Comput. Surv., Vol. 1, No. 1, Article 1. Publication date: January 2022.