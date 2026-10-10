<!-- source: pdf/varbu2022past.pdf | converter: pymupdf -->

<!-- page 1 -->

Citation: Värbu, K.; Muhammad, N.;

Muhammad, Y. Past, Present, and

Future of EEG-Based BCI

Applications. Sensors 2022, 22, 3331.

https://doi.org/10.3390/s22093331

Academic Editors: Sung-Phil Kim

and Yvonne Tran

Received: 23 February 2022

Accepted: 25 April 2022

Published: 26 April 2022

Publisher’s Note: MDPI stays neutral

with regard to jurisdictional claims in

published maps and institutional afﬁl-

iations.

Copyright: © 2022 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license (https://

creativecommons.org/licenses/by/

4.0/).

# sensors

# Review Past, Present, and Future of EEG-Based BCI Applications

## Kaido Värbu 1,*, Naveed Muhammad 1 and Yar Muhammad 2

1 Institute of Computer Science, University of Tartu, 51009 Tartu, Estonia; naveed.muhammad@ut.ee 2 Department of Computing & Games, School of Computing, Engineering & Digital Technologies, Teesside University, Middlesbrough TS1 3BX, UK; yar.muhammad@tees.ac.uk * Correspondence: kaido.varbu@gmail.com

Abstract: An electroencephalography (EEG)-based brain–computer interface (BCI) is a system that provides a pathway between the brain and external devices by interpreting EEG. EEG-based BCI applications have initially been developed for medical purposes, with the aim of facilitating the return of patients to normal life. In addition to the initial aim, EEG-based BCI applications have also gained increasing signiﬁcance in the non-medical domain, improving the life of healthy people, for instance, by making it more efﬁcient, collaborative and helping develop themselves. The objective of this review is to give a systematic overview of the literature on EEG-based BCI applications from the period of 2009 until 2019. The systematic literature review has been prepared based on three databases PubMed, Web of Science and Scopus. This review was conducted following the PRISMA model. In this review, 202 publications were selected based on speciﬁc eligibility criteria. The distribution of the research between the medical and non-medical domain has been analyzed and further categorized into ﬁelds of research within the reviewed domains. In this review, the equipment used for gathering EEG data and signal processing methods have also been reviewed. Additionally, current challenges in the ﬁeld and possibilities for the future have been analyzed.

Keywords: brain–computer interface (BCI); electroencephalography (EEG); rehabilitation; systematic literature review

## 1. Introduction

The electroencephalography (EEG)-based brain–computer interface (BCI) is one of the most rapidly developing ﬁelds of BCI [1,2] and has potential to expand far beyond the domain of medical applications, in which they were initially most popular. The use of EEG has become possible due to the work and discovery by Hans Berger who discovered in 1924 that electrical signals of the human brain could be measured from the scalp [3]. The initial discovery was made using a simple galvanometer and conﬁrmed the possibility that neural activity could be measured by this method [4]. EEG measures the brain electrical activity caused by the ﬂow of electric currents during synaptic excitations of neuronal dendrites and is measured via electrodes placed on the scalp [1,4]. After the initial discovery by Hans Berger, additional brainwave types and mental states associated with the brainwave types have been determined. An EEG system can provide a pathway between the brain and external device, making it possible to read biological signals and interpret certain aspects of a person’s cognitive state [5]. BCI systems are EEG systems that allow users nearly real-time control of an external actuator. EEG-based BCI applications could be used by a person to control a computer or other device using one’s thoughts without using ordinary methods of working with a computer (e.g., using hands) [6]. EEG-based BCI applications could be used also to monitor subject’s mental states such as emotions [7], concentration [8] or drowsiness [9]. BCI adds to the monitoring processes, for example, via enabling systems to be adaptive or sending alert signals.

The BCI applications have been initially developed to help people with disabilities to be able to communicate, control computers and use aiding equipment such as wheelchairs

Sensors 2022, 22, 3331. https://doi.org/10.3390/s22093331 https://www.mdpi.com/journal/sensors

<!-- page 2 -->

Sensors 2022, 22, 3331 2 of 44

or robotic arms. One of the ﬁrst BCI applications assisted individuals with speech anoma- lies [5]. The possibility of using BCI to develop prosthetic arms was considered as early as 1917 [1]. In the overview by Tariq et al., EEG-based BCI has also been used in order to develop wearable lower-limb exoskeletons, as BCI has emerged as an alternative communi- cation system between the human brain and output devices [10]. BCI-based prosthetics are supporting patients in cases of paralysis, amputations and loss of central nervous system functionality due to other reasons [2]. BCI could also be applied in order to enhance neuroplasticity [11]. Neuroplasticity of the brain has been characterized as the capacity of the brain to change or adapt its morphology and functioning in response to experience [12]. The applications have been used in the medical domain also by people suffering from locked-in syndrome or amyotrophic lateral sclerosis (ALS) [1].

EEG-based BCI applications have been used in different areas stretching from the medical domain to non-medical domain where EEG-based BCI applications have been used for entertainment, art, as well as some other areas [5,6,13]. There have been studies concerning the non-medical domain, for example, developing devices to monitor the alertness level of employees [14]. Another aspect that has been investigated is the overall car trafﬁc safety and avoidance of driving fatigue and drowsiness during driving that could result in fatal accidents [1]. BCI applications can be used for controlling smart homes [15–18] or a car [19,20]. In the domain of non-medical applications, the BCI could also be used for sport motor skills improvement, acting skills improvement or surgical skills improvement [11]. The applications for entertainment could include games designed for improving subject attention level or concentration level [13], but also control of drones and humanoid robots [6].

During the current review, the literature on EEG-based BCI applications in the period from 2009 to 2019 was analyzed. The current review gives an overview concerning articles and conference proceedings per year, publications per region/continent, experimental publications per year, publication distribution by domain, EEG devices used, number of EEG channels used, techniques used to obtain EEG data, feature extraction and classiﬁcation methods used.

In the ﬁrst part of the review, an overview concerning the published articles as well as conference papers is also presented through the years. The regions/continents at the forefront of the scientiﬁc progress in the ﬁeld have been highlighted.

An overall review of EEG-based BCI applications has been created and the BCI ap- plications have been categorized based on domain (medical or non-medical) and by ﬁeld, describing the current trends in BCI applications development in more detail. The BCI applications have been included in the medical domain in case they have been designed to provide assistance, monitor, assess or support rehabilitation and in the non-medical domain in case the applications have been designed to entertain, control machines, authenticate, monitor or assist without a medical purpose. The distinction between the domains has been done in a way similar to the work by Al-Nafjan et al. [5].

This review introduces the current trends for the development of EEG-based BCI applications. Although the initial need for BCI applications has been in the medical domain, this review shows that there is currently a higher pace of development in the non-medical domain. The applications meant for widespread use could be used for monitoring user attention, supporting daily activities or for entertainment.

In this review, EEG signal acquisition and processing is also analyzed. The overview concerning the prevalence of different EEG devices has been given together with the details regarding the number of EEG channels used in previous studies. An overview is given concerning the techniques used to obtain the EEG data. Regarding the EEG signal processing, feature extraction and classiﬁcation methods have been reviewed.

This review was conducted in connection to the ﬁrst author’s master’s thesis [21]. This review provides a comprehensive summary of recent works conducted in the ﬁeld and an overview of current obstacles that inhibit progress, both technically and in other aspects. In addition to technical aspects there could be, for example, user-related aspects that limit the

<!-- page 3 -->

Sensors 2022, 22, 3331 3 of 44

use of BCI applications due to difﬁculty for the user to learn to use the applications and inability to generate or alter the required EEG signals.

The ethical, legal and safety considerations in BCI application development are as important as the technical aspects. The synthesis on current challenges gives a mapping of what to focus on in order to support BCI development and shows where the possible risks exist that would need to be addressed. The trends and future possibilities give a better understanding of what we could expect in years to come.

## 2. Background

BCI can be deﬁned as a system that translates the brain activity patterns of a user into messages or commands for an interactive application [22]. A BCI is a control and/or communication system in which the user’s commands and messages are not dependent on common brain-motor periphery communication channels [23]. The BCI user’s brain activity is typically measured using EEG [22]. BCI generally functions through four distinct processes consisting of recording neuronal activity, extracting features, gathering important information and combining information for useful purposes [13]. The EEG signal analysis has been further divided into four steps which are gathering of raw EEG data, signal pre-processing, feature extraction and classiﬁcation [2].

According to Padﬁeld et al. [2], the signal analysis steps could be characterized as follows. The collected raw EEG data comprises all the EEG data collected before pre- processing and further analysis. After the collection of raw EEG data, pre-processing is used to clean noise and enhance the quality of collected EEG data for further analysis. During feature extraction, discriminative and non-redundant information is extracted from the EEG data to form a set of features. Extracted features will capture distinct signal characteristics which can be used as a basis for the differentiation between task-speciﬁc brain states. According to Padﬁeld et al. during classiﬁcation step, the task carried out by a subject is determined and corresponding actions are taken by the system. The use of speciﬁc feature extraction and classiﬁcation method depends on speciﬁc type of BCI application under study.

The most common way to categorize BCI is on the basis of invasiveness. The BCI could be invasive or non-invasive, depending on whether the device is connected physi- cally to one’s brain and the electrodes are placed inside the brain or the device will read brainwaves from the top of the scalp [1]. The use of invasive method of direct contact of the electrodes with brain is more efﬁcient as there are less interfering factors that inﬂuence the signal quality [24], but the invasive method contains the risks of surgical procedures and related complications.

More popular and easy is the non-invasive method, where the brainwaves are read from the top of the scalp via electrodes located on the scalp. As this method also has some drawbacks, including disturbance from external noise, effects from the posture and mood of the subject, detecting a low strength signal resulting in a reduced signal quality [2], there is a signiﬁcant amount of on-going research to determine the best ways for signal detection and analysis.

The most popular current non-invasive method for acquiring brainwaves for BCI is detection through EEG. The popularity of EEG is supported by the inexpensiveness of the equipment, reduced complications compared to invasive procedures, portability, easy process to set-up and use and the possibility to directly measure neural activity [1,2]. EEG reading is easy to use and has high potential to be applied by majority of the population in order to use high variety of possibilities that BCI offers. Other non-invasive methods include functional magnetic resonance imaging (fMRI), magnetoencephalography (MEG) and near-infrared spectroscopy (NIRS) which can be used separately or combined [1]. The advantages of EEG are high temporal resolution, good portability, high temporal resolution, low cost, less invasive when compared to fMRI and independence from need of a complex environment when compared to MEG according to Alsharif et al. The disadvantage of EEG is low spatial resolution [25].

<!-- page 4 -->

Sensors 2022, 22, 3331 4 of 44

BCI could be divided into separate subgroups based on the way to detect and convey the signal from the brain to BCI application and principles of the functioning of the BCI. As per Al-Nafjan et al. [5], BCIs could be categorized as active or passive, based on the control of the BCI application. The categorization of BCIs based on active or passive control and corresponding techniques used to obtain EEG data is presented in Table 1.

Table 1. Categorization of BCIs and corresponding techniques used to obtain EEG data according to Al-Nafjan et al. [5] and Abiri et al. [1].

Category Technique Used to Obtain EEG Data Description

Active

Motor-imagery

Imagining the movement of a speciﬁc body part for example hands, feet or tongue. The intent will affect the brain activity and

could be detected from the EEG. The imagination activates

the brain areas that are responsible for generating the

actual movement.

Visual evoked potential

The brain activity is affected by external visual stimulation and the corresponding altered EEG activity is registered. For example,

in case of steady-state visual evoked potential (SSVEP) there are

different visual stimuli ﬂickering at different frequencies and depending on the direction of the gaze of the subject the EEG

pattern will be consistent with the speciﬁc ﬂickering rate.

Auditory evoked potential Auditory stimulation is generated and depending on the focus of

the subject corresponding EEG activity is registered.

Vibrotactile evoked potential

Physical vibrations at different frequencies are generated for example on the hands and feet of the subject. Depending on the focus of the subject, a corresponding EEG pattern to the speciﬁc physical vibration is registered and could be used to control some

external device.

Imagined speech Imagination of words or sentences that are recognized from EEG.

Error-related potential

The error-related potential is generated when there is a mismatch

between the subject’s intentions and response from the BCI application. The technique can be used to correct tasks given by

the subject. For example, when the subject is controlling the

cursor, but the cursor is moving in the wrong direction, an error-related potential is generated, and the course of the cursor

can be corrected.

Passive Analyzing EEG spectral changes

Systems wherein brain signals yield outputs without any

voluntary control. For example, monitoring drowsiness, attention, mental workload, emotions, concentration and

other states of the mind.

The BCIs using active control react on conscious efforts to alter brainwave patterns and the applications could be controlled via active efforts by the user. The BCIs applying passive control react to the involuntary status of the brainwaves, for example on emotional states such as meditation, excitement and stress. Different emotions could be elicited by, for example, visual-based elicitation using images, prepared task or audio-visual elicitation using short ﬁlm video clips [5].

During active control of the BCI application, the signal could be detected via different techniques. The range of these techniques is broad and covers motor imagery, external stimulation (such as visual, auditory and vibrotactile), error-related potential, hybrid and other techniques. During the motor imagery task, for example, the subject is imagining the movement of a speciﬁc body part, and during error-related potential task, error-related potential is generated when there is a mismatch between the subject’s intentions and response from the BCI application [1].

As per Pasqualotto et al. [23] and Machado et al. [26] BCI could also be categorized depending on whether BCI is dependent or independent of certain muscle movements.

<!-- page 5 -->

Sensors 2022, 22, 3331 5 of 44

Padﬁeld et al. [2] have also categorized BCI as evoked or spontaneous. As per Nicolas- Alonso and Gomez-Gil [27] BCI could be categorized as synchronous or asynchronous. An overview concerning additional different categorization of BCIs in the literature is presented in Table 2.

Table 2. Additional different categorization of the BCIs in the literature by Pasqualotto et al. [23], Machado et al. [26], Padﬁeld et al. [2] and Nicolas-Alonso and Gomez-Gil [27].

Author BCI Categorization Description

Pasqualotto et al. [23]

Machado et al. [26]

Dependent

Dependent on muscles and peripheral nerves. For example, in

case of visual evoked potential (VEP), gaze is directed by

muscles to focus on different visual stimuli.

Independent Muscle movement is not needed to control BCI. For example, in

case of P300 response is detected from EEG and analyzed.

Padﬁeld et al. [2]

Evoked

Also named as exogenous. Some type of external stimulation is

required such as visual, auditory, or sensory. Can be further divided to evoked potentials and event-related potentials. In case of evoked potentials, changes in EEG can be detected due

to responses to external stimuli. In case of event-related potentials, the changes in EEG are caused by sensory or

cognitive events.

Spontaneous

Also named as endogenous. External stimulation is not required. For example, motor-imagery technique, where subjects imagine movement of a limb and there is no additional

input from external stimuli.

Nicolas-Alonso and

Gomez-Gil [27]

Synchronous The BCI analyzes signals during certain time windows, and the

subject is able to give commands after ﬁxed time intervals.

Asynchronous

The brain waves of the subject are analyzed constantly, and the

subject can give commands whenever the subject wants. Asynchronous BCI gives the subject more possibilities and

ﬂexibility concerning controlling the BCI.

“Dependent BCIs” require muscle control, for example, via gaze control. “Independent BCI” on the other hand detect signals only based on changes in the brainwaves without required muscle movement [23,26]. According to Padﬁeld et al. [2], another possibility to categorize BCIs would be depending on whether external stimulation is required for the functioning of the BCI or not, thus dividing the systems into “evoked” when external stimulation is needed and to “spontaneous” in case external stimulation is not needed. According to the aforementioned categorization by Padﬁeld et al., evoked systems include for example steady-state visual evoked potential (SSVEP), where visual stimulation is received via ﬂickering at unique frequencies that causes corresponding changes in EEG when focusing on speciﬁc stimulus at a speciﬁc ﬂickering frequency. According to this categorization spontaneous systems also include for example motor-imagery technique, where external stimulation is not needed and the changes in EEG patterns are generated via imagining the movement of a limb. Padﬁeld et al. have noted that the categorization to evoked and spontaneous systems has also been named by some authors as exogenous and endogenous.

An additional way to classify BCIs is based on the time when the signals from the user are gathered by the BCI. The BCIs could therefore be divided as synchronous and asynchronous [27]. BCI is considered synchronous, when the information concerning the brainwave status is gathered during speciﬁc time intervals. It means that the user can give commands only at distinct timing, and the brainwaves are not measured at other times. In case of asynchronous analysis, the brain patterns are analyzed on an ongoing basis and the user is more ﬂexible when giving commands to the system.

<!-- page 6 -->

Sensors 2022, 22, 3331 6 of 44

## 3. Objectives

The systematic literature review was prepared based on three databases, PubMed, Web of Science and Scopus, in order to cover a wide range of reliable peer reviewed publications on EEG-based BCI applications. In previous studies, either one [5] or multiple databases [28,29] have been used to conduct the literature search, but in the current review a selection of multiple databases was used in order to cover a broader range of publications on the topic.

The time period for the publications from between 2009 and 2019 was selected in order to give an overview concerning longer period of time and to be able to compare the results with other studies. While 2019 might not seem truly up to date, we would like to highlight that it is a systematic review. Thus, once such a review has begun, altering the chosen period would mean either (i) compromising the systematic nature of the review, or (ii) conducting a new systematic review from scratch, which are undesirable and impractical, respectively. Similar lengths of the time interval have been selected in previous studies [5,28]. From the time period above, 635 publications were selected according to the search criteria speciﬁed in Appendix A, which were then further screened and assessed for eligibility. As this review includes articles until 2019, in Appendix B we list additional publications which have been published after the time period of the current review, i.e., 2009 to 2019.

After the identiﬁcation of the publications, a screening of the publications was per- formed. After the assessment of eligibility, 202 publications were included in the ﬁnal analysis. The process was conducted as per the PRISMA model [30]. Listed below are the objectives that were set at the beginning for conducting our systematic literature review.

The objectives of the systematic literature review on EEG-based BCI applications:

1. Determine the trends concerning the publication of articles, conference proceed- ings and overall number of publications on EEG-based BCI applications from 2009 until 2019. 2. Determine the techniques used for obtaining EEG data and give an overview con- cerning the trends in EEG signal processing, which includes feature extraction and classiﬁcation methods. 3. Give an overview concerning the devices used for EEG signal collection and specify the number of EEG channels used for obtaining the data. 4. Determine the proportion of scientiﬁc studies conducted on the topic in the medical and non-medical domain and further analyze the distribution of the studies per application ﬁeld. 5. Analyze the literature by regions/continents, i.e., which regions/continents are at the forefront of scientiﬁc progress in EEG-based BCI applications and highlight the most contributing authors on the topic.

## 4. Methods

As per best practice, the PRISMA model [30,31] has been used to conduct systematic literature reviews in many ﬁelds of research. In addition to the PRISMA model, guidance from Cochrane Collaboration can be followed in order to prepare a systematic literature review [32]. As the PRISMA model has been developed together with the Cochrane Collaboration and with a large number of experts in the ﬁeld, the PRISMA model was selected as the best current collection of principles in order to conduct the current systematic literature review on EEG-based BCI applications. The PRISMA method has been developed by Moher et al. [30] and has been used widely in conducting well organized systematic literature reviews such as [5,23,28,29].

4.1. Information Sources

The publications concerning EEG-based BCI applications can be found from a high number of different sources. In the current review, three well-known databases, i.e., PubMed [33], Scopus [34] and Web of Science [35] were selected to conduct the publication

<!-- page 7 -->

Sensors 2022, 22, 3331 7 of 44

search [5,28,29]. The search terms have been included in Appendix A. The process of including publications in the analysis is shown in Figure 1.

Figure 1. The ﬂow of information during selection of studies according to the PRISMA model comprising Identiﬁcation, Screening, Eligibility and Inclusion phase.

During the full review of the 202 publications included in the analysis, 25 separate data items were extracted from each publication. The extraction of the data items follows the PRISMA model for preparing systematic literature reviews, and categorization of the extracted data items has also been applied in the past by Roy et al. [28] in a similar way while following the PRISMA model.

4.2. Eligibility Criteria

Selection of the publications for the current review was based on pre-determined eligibility criteria. The eligibility criteria were determined to ﬁlter relevant publications concerning EEG-based BCI applications as per objectives of this review for further analysis. The eligibility criteria were selected according to similar principles used in previous review studies and studies that follow the PRISMA model [5,23,28–30].

The following eligibility criteria were applied during review of the publications during screening and eligibility assessment: • Publications needed to be relatively current. In the further analysis, publications were included from the period between 2009 and 2019. • We excluded meeting abstracts, book chapters, masters and doctoral dissertations and non-English publications. • We excluded non-peer-reviewed journal articles and non-peer-reviewed confer- ence proceedings.

Following the above-mentioned inclusion and exclusion steps, a manual scanning was conducted for the titles, keywords and abstracts of the publications. The screening process was conducted by one person. Publications that did not address the subject, but rather mentioned the subject in passing in general were excluded. During the review, 402 publications were excluded that did not meet the eligibility criteria. The scanning resulted in 233 publications for further full text assessment of eligibility. The overview

<!-- page 8 -->

Sensors 2022, 22, 3331 8 of 44

concerning the process of identiﬁcation, screening, assessing the eligibility and inclusion of the publications in the ﬁnal analysis as per PRISMA model is shown in Figure 1.

During the full text review of 233 publications, 31 publications which did not cor- respond to the eligibility criteria were further excluded. After all steps of publication selection per PRISMA model were completed, 202 publications were included (i.e., left at the completion of the process) for the ﬁnal analysis, which are [1–11,13–20,24,26,36–216].

## 5. Results

The results have been divided into Sections 5.1–5.9. The ﬁrst part of the results covers the distribution of articles and conference proceedings per year, publications by regions/continents, experimental publications per year and publication distribution by domain. The sections in the second part focus on the EEG devices used, number of EEG channels, signal analysis, techniques used to obtain EEG data, feature extraction and classiﬁcation. The results reﬂect the publications matching the search terms used during the Identiﬁcation phase.

5.1. Articles and Conference Proceedings per Year

During the period from 2009 to 2019, the overall number of articles and conference proceedings published per year had been gradually rising. In the beginning of the period, the total number of the publications had been 11–15 publications per year from 2009 until 2011. During the period from 2012 to 2016, there was a slight increase in the volume of the publications to 16–19 publications, and only in year 2014 was there a decrease to 10 publications per year. Signiﬁcant increases can be noted from year 2017 onwards when the number of publications per year had increased to up to 32 publications per year in 2017. Please see the overview concerning the number of articles and conference proceedings per year in Figure 2. As the search of the publications was conducted in the three databases during the period from 20 October 2019 to 30 October 2019, the ﬁnal number of publications for 2019 could be a slightly higher number.

Figure 2. The number of publications (conference proceedings and articles) per year from the period from January 2009 to October 2019.

The trend concerning increase in the overall number of publications per year has also been noted by Al-Nafjan et al. [5] when analyzing the volume of EEG-based emotion recognition publications. In the aforementioned article, there has been a rapid increase in the overall number of publications on the topic from 2010 to 2016, and it was suggested that the increase could be caused by increased knowledge of neurobiological processes, computers

<!-- page 9 -->

Sensors 2022, 22, 3331 9 of 44

with faster computational processing, greater availability of devices for recording brain signals and more powerful signal processing and machine learning algorithms. Increase in the number of publications concerning EEG-based BCIs has been also demonstrated by Hwang et al. [99], where a signiﬁcant increase has been illustrated during the period from 2007 to 2011. It can be noted from Figure 2 that during the period from 2009 to 2019, the overall number of conference proceedings published on EEG-based BCI applications has been higher than the number of articles published. Out of the 202 publications, 117 are conference proceedings (58% of the publications) and 85 are articles (42% of the publications). Although in the years from 2009 until 2016 the number of conference proceedings has been greater than the number of published articles (except for year 2014), a trend has been noted for recent years concerning the increase in the relative volume of the published articles.

The reason why the proportion of articles has increased over the recent years could be the overall development of the technology making it easier and more efﬁcient to conduct the research on EEG-based BCI applications and inclusion of the topic more in the articles. In the beginning of the period under current focus, a higher variety and number of publications were included in conference proceedings. This trend noted in the current review illustrates the observation by Roy et al. [28] noting that there would be a wide variety of research ideas within different repositories and among different type of publications. The effect highlights the need to include a higher variety of repositories and different type of publications in the literature review in order to include objective coverage of the research ideas on the topic and avoid possible publication bias.

5.2. Publications per Region/Continent

The distribution of the publications concerning EEG-based BCI applications were further analyzed by region/continent. Out of the 202 publications, the highest number of publications on the topic has been published in Asia (111 publications) where the highest number of publications per country has been published in China (39 publications).

The other regions/continents where higher number of publications have been pub- lished on the topic during the period of 2009 to 2019 are Europe (56 publications) and North America (27 publications). In Europe, most productive countries have been Germany and Italy (both countries with 9 publications), and in North America, the highest number of publications have been published in the USA (23 publications). Similar results have also been found by Hwang et al. [99] and Roy et al. [28] where USA and China have dominated as the countries with the highest number of publications on EEG-based BCI. A detailed overview concerning the publications per region/continent is presented in Figure 3.

Figure 3. Number of publications per region/continent. The highest number of publications on the topic has been published in Asia.

<!-- page 10 -->

Sensors 2022, 22, 3331 10 of 44

Altogether, 37 different countries have contributed to the publications on EEG-based BCI applications within the time period reviewed. The highest number of contributing countries came from Europe, where the publications have been contributed by 18 different countries. From Asia, the publications have been contributed by 14 different countries, but the average number of publications per country is higher. From North America, publications have been contributed by three countries: USA, Canada and Mexico. In Australia, 7 publications were published, but from South America only one publication from Brazil has been published. It is interesting to note that no publications were contributed from Africa. It is important to note that the results reﬂect the publications matching the search terms used.

5.3. Experimental Publications per Year

Among the experimental publications on EEG-based BCI applications, non-medical publications have contributed the majority of the experimental publications per year. Exceptions to this trend have been seen in 2009 and 2013 when more medical publications were published when compared to the number of non-medical publications per year. Although in general there has been higher number of non-medical publications per year during the period under review, during recent years the proportion of medical publications has risen, reaching up to 36% of the publications.

During recent years, the overall number of experimental publications has increased from 8–15 publications per year during 2014–2016 to 19–25 publications per year during the period of 2017–2019. The trend of a rapid increase in the overall number of publications on EEG-based BCI applications can also be seen in Hwang et al. [99].

Throughout the period that was analyzed, there has been 99 publications (58% of the publications) published in the non-medical domain and 53 publications (31% of the publications) in the medical domain. In 19 cases (11% of the publications) the publications cover both domains. During interpretation of the results, it should be also noted that as the database search was conducted during the period from 20 October 2019 to 30 October 2019, the ﬁnal number of publications for 2019 could have been slightly increased by the end of 2019. Please see the overview concerning the number of experimental publications per year in Figure 4.

Figure 4. Experimental publications per year covering the period from January 2009 to October 2019. The publications have been further divided into medical or non-medical domain or both in case both domains have been covered.

Although initially the EEG-based BCI applications were mainly developed for medical reasons to help patients to communicate, grasp objects, move around and support in other daily activities, the focus has been moving from the medical domain to non-medical applications. The shift in the focus does not reduce the importance of these applications in

<!-- page 11 -->

Sensors 2022, 22, 3331 11 of 44

the medical domain but rather shows the wider potential of EEG-based BCI applications and opens doors for new possibilities.

5.4. Publication Distribution by Domain

Among the publications within the period from 2009 to 2019, there were 58% of the publications (99 publications) from the non-medical domain. Among the overall number of publications that were analyzed, 31% of the publications (53 publications) are from the medical domain and in an additional 11% of the publications (19 publications) both domains have been included. Please see the distribution of the publications per domain in Figure 5. Similar prevalence of publications in medical domain has been determined by Al-Nafjan et al. [5], where 23% of the publications belonged to the medical domain.

Figure 5. Distribution of publications per domain. The ﬁgure illustrates the distribution of the publications among medical and non-medical domain and volume of the publications covering both domains.

The publications in the medical domain could be further divided based on the type of applications into ﬁelds such as assistive, monitoring, rehabilitation, assessment and others. Applications in the assistive ﬁeld help users with disorders or disabilities to perform daily tasks and provide assistance. Within the medical domain, the ﬁeld covering assistive applications is the largest contributing 74% of the publications in the domain. The assistive ﬁeld includes studies on robotic arm movement in a medical setting [78], lower-limb prosthesis control [155] and intelligent wheelchair driving system [111]. The applications in the rehabilitation ﬁeld for example help to restore the physical functions that have been lost by the patients due to accident or disease. Among studies analyzing possibilities for rehabilitation there is an important role for the studies supporting the rehabilitation of stroke patients [70,185,213]. As per Chaudhary et al., the assistive BCIs are intended to enable patients to communicate or control external devices and rehabilitative BCIs are intended to facilitate patient recovery [217]. When compared to assistive BCIs, the amount of rehabilitative BCIs is lower, covering 9% of the publications. An important ﬁeld in the medical domain is monitoring, covering 9% of the publications in the medical domain.

The publications concerning monitoring include for example monitoring emotional changes in patients [43]. Among studies analyzing possibilities for rehabilitation there is an important role for the studies supporting the rehabilitation of stroke patients [70,185,213]. The ﬁelds of “assessment” and “other” cover a total of 8% of the publications in the medical domain, both contributing 4% of the publications in the domain.

The prevalence of different ﬁelds in the medical domain differ when compared to previous work of Al-Nafjan et al. [5], as the most popular ﬁelds in this domain then were

<!-- page 12 -->

Sensors 2022, 22, 3331 12 of 44

assessment and monitoring. The difference would be explained by the difference in the scope of the studies where in previous case the focus was on emotion recognition based on EEG-based BCI, but in the current review we focus on EEG- based BCI applications in general. An overview covering the publications in the medical domain is presented in Figure 6.

Figure 6. Distribution of publications in medical domain. In the medical domain, the largest ﬁeld is assistive followed by monitoring, rehabilitation, assessment and other.

The largest ﬁeld in the non-medical domain is monitoring contributing 50% of the articles in the non-medical domain. Additionally, the two large ﬁelds are control machine and entertainment contributing 17% and 16% of the publications, respectively. Smaller cov- erage in the non-medical domain is by the publications in the ﬁeld of assistive applications covering 4% of the publications and authentication covering 2% of the publications.

Other different types of publications cover the rest of 11% of the publications in the domain. When compared to previous similar studies, Al-Nafjan et al. [5] has also noted that the majority of the publications in the non-medical domain concerning EEG-based BCI for emotion recognition has contributed to the monitoring ﬁeld. An overview of the publications in the non-medical domain is presented in Figure 7.

In the monitoring ﬁeld, a total of 49 publications have been included. The publications in the monitoring ﬁeld include studies where data are collected from the subjects in order to monitor and analyze their mental activity. The studies cover for example mental fatigue es- timation [182], emotion recognition [7] and detecting meditation [4]. In the control machine ﬁeld, the applications include those that enable people to control different machines in their daily environment, via EEG, to make their life easier. These applications can be used for example for home appliance and smart home control [15,16] or robotic systems [38]. EEG-based BCI applications are also used for entertainment such as live brain-computer cinema performance [216], driving in a virtual city [19] or recommendations for music based on a person’s mood [174]. Other applications include user authentication using visual stimuli of geometric shapes [37], age and gender prediction [109] and other various possibilities. As illustrated in Figure 7, the majority of applications in the non-medical domain are related to monitoring. As monitoring applications have many practical applica- tions such as monitoring mental fatigue at the workplace or during driving monitoring ﬁeld has high potential for further development and practical applications for daily life.

<!-- page 13 -->

Sensors 2022, 22, 3331 13 of 44

Figure 7. Distribution of publications in non-medical domain. In the non-medical domain, the largest ﬁeld is monitoring followed by control machine, entertainment and other smaller ﬁelds.

In a smaller number of the publications, both medical and non-medical domains have been covered. The domain has been further divided into the following ﬁelds: assistive, framework, control machine, monitoring and others, as per type of publications. The details concerning the distribution of publications covering both domains have been illustrated in Figure 8. Among studies covering both the medical and non-medical ﬁeld, 42% of the cases publications cover the assistive category, such as detection of imagined speech and classiﬁcation of unspoken words from EEG signals [85,86]. A total of 21% of the studies concern works such as developing a new framework for practical BCI communication development [57].

Figure 8. Distribution of publications covering both domains. The publications covering both domains have been focused mainly on assistive, but other ﬁelds such as framework and control machine also make up a signiﬁcant proportion of the publications.

Studies in the ﬁeld of control machine are covering 16% of the studies. They include research for example on controlling a car in an experimental environment outside laboratory conditions [20]. Some studies are focused on monitoring such as detection of kinesthetic

<!-- page 14 -->

Sensors 2022, 22, 3331 14 of 44

attention [147]. Other ﬁelds cover for example the development of serious games that could be used in entertainment, e-learning or medical applications [186].

5.5. EEG Devices Used

Among the studies analyzing EEG-based BCI applications, the most commonly used EEG devices are Emotiv EPOC from Emotiv (San Francisco, CA, USA), Quik-Cap from Compumedics Neuroscan (Charlotte, NC, USA) and MindWave from NeuroSky (San Jose, CA, USA). These three devices combined cover 57% of the publications on the topic. The most common EEG device, the Emotiv EPOC (Emotiv, San Francisco, CA, USA), has been used in 40% of the publications analyzed while the prevalence of other popular EEG devices Quik-Cap (Compumedics Neuroscan, Charlotte, NC, USA) and MindWave (NeuroSky, San Jose, CA, USA) was 9% and 8%, respectively. The high prevalence of Emotiv EPOC (Emotiv, San Francisco, CA, USA) and Quik-Cap (Compumedics Neuroscan, Charlotte, NC, USA) use among studies analyzing EEG-based BCI applications for emotion recognition has also been noted by Al-Nafjan et al. [5] and in general for EEG equipment by Roy et al. [28].

The most common EEG devices (Emotiv EPOC, Emotiv, San Francisco, CA, USA; Quik-Cap, Compumedics Neuroscan, Charlotte, NC, USA; MindWave, NeuroSky, San Jose, CA, USA) are all manufactured in USA. Other EEG devices used in the studies have been manufactured also in Germany (Easycap, Easycap GmbH, Wörthsee, Germany; actiCAP, Brain Products GmbH, Gliching, Germany), Netherlands (Active Two, Biosemi, Amsterdam, The Netherlands), Spain (Enobio, Neuroelectrics, Barcelona, Spain) and UK (MyndPlay BrainBandXL, MyndPlay, London, UK). The details of different EEG devices used, number of publications and percentage of publications covered is presented in Figure 9.

Figure 9. EEG devices used in the publications ordered by the number and percentage of publications where the device has been used.

Emotiv EPOC (Emotiv, San Francisco, CA, USA) and MindWave (NeuroSky, San Jose, SC, USA) are considered to be low-cost consumer EEG devices, while Quik-Cap (Compumedics Neuroscan, Charlotte, NC, USA) is more expensive to purchase [28]. While the Emotiv EPOC (Emotiv, San Francisco, CA, USA) EEG device has 14 channels and MindWave (NeuroSky, San Jose, CA, USA) has 1 channel, the Quik-Cap (Compumedics Neuroscan, Charlotte, NC, USA) EEG device uses 32 channels. The cause of the general popularity of the Emotiv EPOC (Emotiv, San Francisco, CA, USA) EEG device is due to the relative low cost of the device, sufﬁcient number of EEG channels and the device being considered easy to use. The MindWave (NeuroSky, San Jose, CA, USA) EEG device has limitations for use due to the limited number of EEG channels, but the low cost and ease of use make the device still popular. The device could be applied in speciﬁc applications that do not require a higher number of EEG channels. The Quik-Cap (Compumedics Neuroscan, Charlotte, NC, USA) device on the other hand is more expensive but has the advantage of a higher number of EEG channels.

<!-- page 15 -->

Sensors 2022, 22, 3331 15 of 44

Dadebayev et al. [218] have found that low-cost consumer-grade EEG devices can perform equally well as research-grade devices for EEG-based emotion recognition. The advantages of the Emotiv EPOC (Emotiv, San Francisco, CA, USA) device are the high quality of the signal, less artifacts, 14 sensors, ready to use assembly and modern design. The disadvantages of the Emotiv EPOC (Emotiv, San Francisco, CA, USA) device are being non-dry sensors, 10–15 min setup time and required license for raw data access. For MindWave (NeuroSky, San Jose, CA, USA), the advantages are its low price, compactness and practical wireless device. The disadvantages of MindWave (NeuroSky, San Jose, CA, USA), as highlighted by Dadebayev et al., are the inclusion of only 1 sensor and a lower quality for EEG experiments.

The low-cost EEG headsets can be more convenient for the user and the devices such as Emotiv EPOC (Emotiv, San Francisco, CA, USA) and MindWave (NeuroSky, San Jose, CA, USA) have been successfully used in the studies developing EEG-based BCI applications [219]. The ﬁnal decision concerning the use of a speciﬁc EEG device depends on the type of EEG-based BCI application determining the need for a speciﬁc number of EEG channels. The decision also depends on the cost planned for the study and devices for the end users. The EEG equipment market shows rapid development and new devices appear on the market continuously [220].

Concerning the design of the EEG devices it has been highlighted by Souﬁneyestani et al. [221] that the EEG headsets with dry electrodes such as MindWave (NeuroSky, San Jose, CA, USA) have been more robust to line noise when compared to EEG devices with wet electrodes, such as Emotiv EPOC (Emotiv, San Francisco, CA, USA) or Quick-Cap. According to Souﬁneyestani et al., the dry electrodes contain more artifacts. The dry EEG devices may lose humidity during use that may lead to decline in signal quality. In case of wet electrodes, the solution could evaporate over time, and it could be necessary to reapply the solution to the electrodes. The most convenient for the user would be dry wireless EEG devices that enable ﬂexibility in movement and lower setup time. In case of dry electrodes, it would need to be considered that dry electrodes present lower performance when compared to wet electrodes [222]. It has been also highlighted by Souﬁneyestani et al. that when using wireless connectivity, the data would need to be encrypted prior to wireless transfer in order to avoid any security risk to the data of the user.

Similarly, Hinrichs et al. [223] have compared the use of dry and wet EEG systems for clinical applications and have found that although the number of artifacts was slightly higher for the dry EEG system the results were comparable between dry and wet EEG sys- tems. The dry EEG system is more robust and less sensitive to electromagnetic interference that the subject could encounter at the clinic or at home. It has been stated by Hinrichs et al. that importantly both patients and healthy volunteers preferred the dry electrodes and reported that the dry headset was more suitable for self-application and home use.

Ratti et al. [224] have shown that although medical EEG systems offer clear advantages in data quality over consumer systems, EEG data can be collected from all systems tested in both medical and consumer contexts. Consumer EEG systems are more convenient and faster to set up. According to Ratti et al., consumer EEG systems would be more useful for a quick assessment when time is limited, while the medical grade systems would be preferred in research and clinical trial settings.

In the study by Zerafa et al. [225], a comparison was performed between a broad range of EEG devices for SSVEP BCIs. Zerafa et al. showed that low-end research grade EEG systems are comparable to the high-end research grade EEG systems in terms of signal quality. Low-cost EEG headsets suffer more from poor EEG signal quality, and it could be suggested that the best choice for developing BCI applications outside of the laboratory setting would be affordable wireless research grade systems.

When comparing the advantages and disadvantages of low-cost and more expensive EEG headsets LaRocco et al. [219] have found that traditional medical- and research-grade EEG systems have been successfully used in various applications, but are less versatile outside a laboratory environment. Low-cost EEG headsets show greater design convenience

<!-- page 16 -->

Sensors 2022, 22, 3331 16 of 44

for daily occupational use and many of the low-cost devices including Emotiv EPOC (Emotiv, San Francisco, CA, USA) and MindWave (NeuroSky, San Jose, CA, USA) have been used, for example, as drowsiness detectors. LaRocco et al. have further suggested that the use of open-source software and occupational reﬁnement may further boost the capabilities of the systems over time.

5.6. Number of EEG Channels

Among the studies analyzed, the number of EEG channels used varies across a large range. The highest number of EEG channels used was 163 by Zhou et al. for EEG-based classiﬁcation of elbow versus shoulder torque intentions [213]. Altogether there were 5 studies (3% of studies) where more than 100 EEG channels were used, indicating that the use of this high number of EEG channels is rather exceptional. The majority of the studies (64% of studies) involve 1–20 EEG channels, where 34% of the studies employ 1–10 EEG channels and 30% of the studies employ 11–20 EEG channels. There are also a signiﬁcant number of studies that use 21–40 EEG channels and 11 studies have been conducted with 61–70 EEG channels. The detailed overview regarding the number of EEG channels used in the studies is presented in Figure 10.

Figure 10. Number of EEG channels used in publications. In the majority of the publications, up to 40 EEG channels have been used.

Previously, Roy et al. [28] found that for obtaining EEG signals, 1 to 256 electrodes have been used, with half of the studies using between 8 to 62 electrodes. It was thought that a very high number of electrodes would not give added value to the studies, more important is the exact location of smaller number of electrodes. In that article, it was found that, concerning the number of electrodes, there is a signiﬁcant increase in sensitivity and speciﬁcity when increasing the number of channels up to 22, but a further increase in the number of EEG channels would not give a similar advantage.

Al-Nafjan et al. [5] have also concluded that the majority of studies use up to 64 channels for obtaining EEG data. In the study by Al-Nafjan et al., it has been emphasized that when planning the use of a speciﬁc number of EEG channels, it is important to also consider the time required for the system setup, the comfort level for the subject and the number of features to be processed. When planning studies or developing applications for users, it is important to select the electrode positions carefully and limit the number of EEG channels. A limited number of carefully selected electrode positions would make the future devices more user friendly and optimize the system performance.

<!-- page 17 -->

Sensors 2022, 22, 3331 17 of 44

5.7. Technique Used to Obtain EEG Data

In the publications, a variety of techniques are used for the interaction between brain and computer in BCI applications. The most popular techniques include the motor- imagery paradigm (applied in 38 publications), visual evoked potential paradigm (applied in 31 publications) and monitoring drowsiness/attention (applied in 29 publications) or emotions/affective states (applied in 15 publications). The overview concerning the prevalence of different techniques is shown in Figure 11. These techniques have been used in 73% of the reviewed publications (where the technique used was stated).

Figure 11. Techniques used in the publications. The techniques have been represented according to the number of publications where the techniques have been used and prevalence among medical, non-medical or both domains.

Among the publications applying motor-imagery paradigm, there were 62% of the publications in the medical domain and 24% of the publications in the non-medical domain. In addition to the aforementioned, 14% of the publications covered both the domains. Among the medical domain there are innovative applications such as EConHand [163], neuro-rehabilitation using virtual reality feedback [106] and intelligent brain-controlled robotic limbs [158], applying the motor-imagery paradigm.

In the visual evoked potential paradigm, the non-medical domain is dominant as in 61% of the reviewed publications (where the technique used was stated) applied this technique. In the medical domain, the prevalence of this type of technique used was 23% and both domains were included in 16% of the cases. Visual evoked potential paradigm is widespread among BCI applications as it has been long used and tested in a high number of previous studies. The visual evoked potential paradigm also involves the visual P300 paradigm and the steady state visual evoked potential paradigm [1]. Among the most interesting applications of the aforementioned technique in the non-medical domain are the deceit identiﬁcation test [74], use of EEG-based BCI devices to subliminally probe for information [83] and authentication based on emotionally signiﬁcant images [166].

There is signiﬁcant interest in monitoring the mind for drowsiness/attention or emo- tions/affective states. Both techniques use the analysis of changes in the EEG spectrum to determine the states and changes in one’s mind. The vast majority of the publications concerning drowsiness/attention (88%) or emotions/affective states (93%) are categorized in the non-medical domain. The monitoring of drowsiness/attention based on EEG spec- tral changes has high practical value as there are a number of studies implementing the technique in order to create helmets for on-site workers for drowsiness detection [14], predicting driver fatigue [134] or implementing EEG-based attention feedback in order to improve focus in e-learning [171].

Other techniques used in the publications are applied less frequently, but there is a general trend noted in the overall use of various techniques. As in the case of motor- imagery, auditory evoked potential and vibrotactile evoked potential technique, the main

<!-- page 18 -->

Sensors 2022, 22, 3331 18 of 44

application is in the medical domain, but the majority and larger variety of techniques are applied in the non-medical domain. The trend indicates the high potential of non-medical applications for the EEG-based BCI applications. When taking into consideration that the majority of general population apply for non-medical domain, vast number of people could beneﬁt from this type of applications in the future.

5.8. Feature Extraction

The feature extraction is an important processing step in order to extract the relevant details from the wide range of signals collected during acquisition of the EEG data. In previous studies, high number of different methods have been used for feature extraction. According to Al-Nafjan et al. [5] the feature extraction step is one of the major challenges in BCI systems and the technique is not optimal across different applications. The overview concerning the prevalence of different methods for feature extraction among the studies investigating EEG-based BCI applications is presented in Figure 12.

Figure 12. Feature extraction used in the publications ordered by the number and percentage of publications where the extraction method has been used.

Among the studies reviewed the most frequent feature extraction approaches are analysis of power spectral density (used in 23 publications), Fourier transform (used in 20 publications) or the analysis of common spatial pattern (used in 18 publications). Alto- gether, the aforementioned publications contribute to 48% of the reviewed publications. These results are similar to previous work by Al-Nafjan et al. [5], who state that power spec- tral density and Fourier transform have been most frequently used for feature extraction in the studies to classify emotional features from EEG.

According to Xie et al. [226] the advantage of power spectral density is feature stability. In terms of disadvantages, the power spectral density is not suitable for unstable signals, and it would not be possible to analyze time-domain signals. The Fourier transform is, according to Xie et al., applicable for stationary signals and is appropriate for narrowband signals, but does not work for nonstationary signals, greatly sustains noise sensitivity and does not have shorter duration data record. Common spatial pattern has a good effect when applied to EEG data based on motor imagination and does not require the selection of a speciﬁc frequency band in advance, but is sensitive to noise and requires multiple electrodes [226].

<!-- page 19 -->

Sensors 2022, 22, 3331 19 of 44

Other methods for feature extraction are used less frequently, but in many cases different feature extraction methods are used within one study. Similar general prevalence concerning the use of power spectral density and use of different feature extraction methods within studies has been noted by Al-Nafjan et al. [44], for analyzing human emotions from EEG, Padﬁeld et al. [2] when analyzing EEG-based BCI interfaces using motor-imagery technique and Sourina et al. [178] for real-time brain state recognition from EEG.

Our overall results correlate with previous studies in the ﬁeld highlighting the im- portance of analyzing power spectral density, the use of Fourier transform and common spatial pattern for feature extraction and emphasizing the need to apply different types of feature extraction methods depending on the application under study.

5.9. Classiﬁcation

For the purpose of classiﬁcation, different machine learning algorithms have been used in previous studies for EEG-based BCI applications. The most common machine learning algorithms used are linear discriminant analysis and support vector machine, which have been applied in 52% of the studies. Other machine learning algorithms have the coverage of 2–5%. Among all of the methods, linear discriminant analysis has been applied in 31% of the cases and support vector machine in 21% of the studies. An overview of the classiﬁcation methods employed in the reviewed studies is presented in Figure 13.

Figure 13. Classiﬁcation method used in the publications ordered by the number and percentage of publications where the classiﬁcation method has been used.

Linear discriminant analysis has been characterized as a simple classiﬁer with low computation requirements and acceptable accuracy [122]. Linear discriminant analysis is easy to use with low computational complexity, but requires a linear model [226]. Support vector machine is a speedy classiﬁer that supports binary and multi-class method and can perform linear and nonlinear modes [122]. Support vector machine performance is better compared to other linear classiﬁers, but it has low computational complexity [226].

Other methods applied in EEG-based BCI applications are machine learning algo- rithms such as convolutional neural network, naive Bayes and random forest that account for 4–5% of the cases and artiﬁcial neural network, deep neural network, Gaussian mixed model and k-nearest neighbors that account for 2–3% of the cases.

The results of the current review are in correlation with previous studies where Al- Nafjan et al. [5] have shown that the use of support vector machine is one of the most popular methods used for classiﬁcation for EEG-based BCI systems for emotion recognition.

<!-- page 20 -->

Sensors 2022, 22, 3331 20 of 44

According to the aforementioned study, the choice for classiﬁcation algorithm depends on the type of brain signal being recorded and the type of application that is being controlled. Wide use of linear discriminant analysis and support vector machine for classiﬁcation has also been shown by Padﬁeld et al. [2] for EEG-based BCIs using motor-imagery.

Dadabayev et al. [218], which pertains to feature extraction techniques and classiﬁca- tion methods used for EEG-based emotion recognition, has stated that no feature extraction technique or classiﬁcation method could be named exclusively the best option for all cases, but the right strategy relies on the speciﬁc system paradigm and objectives. It has been suggested that it would be needed to consider many different machine learning algorithms and compare the results before choosing the best model for the given objective [218]. Simi- larly, during a comparison of machine learning methods for emotion recognition, including linear discriminant analysis, support vector machine, naive Bayes and k-nearest neighbors, Doma and Pirouz [227] did not ﬁnd that any of the methods would outperform one another.

According to Nakagome et al. [228], when comparing neural networks and machine learning algorithms for EEG gait decoding neural network-based decoders with downsam- pling or a wide range of frequency band features could improve the decoder performance and robustness for stable use of BCIs. Varszegi [229] has suggested that in order to improve artiﬁcial neural networks it would be further needed to look inside them, develop methods to analyze their internal activations, ﬁgure out the behavior of their architectural elements and create knowledge basis for conscious artiﬁcial neural network design to handle EEG signal processing tasks. According to Lotte et al. [22] the ideal classiﬁcation method would use features and classiﬁers that are invariant over time, over users and contexts. There is a need for a new generation of BCI classiﬁcation methods that consider the user in the loop and could adapt to the user [22].

## 6. Discussion

In the ﬁeld of EEG-based BCI applications, there is a number of challenges hindering the development of the applications that would need to be addressed during future studies. It is important to acknowledge these aspects to ﬁnd solutions or alternatives as needed. There are also many opportunities in the ﬁeld to be used in the future and this is also an important aspect to highlight and share ideas among researchers. The sharing of new ideas and possibilities for the future facilitates the development of a large variety of applications in the ﬁeld of EEG-based BCI applications.

During the preparation of this systematic review, a strict process has been followed including the use of planned search terms and databases before the analysis of the literature. The time period for the publications was selected from 2009 until 2019 for conducting of the analysis in order to give an overview concerning a longer period of time. The review was designed in order to be able to compare the results with other previously conducted reviews on similar topics. Similar time interval has been selected also in previous studies [5,28]. The additional publications published after the aforementioned time period and outside of the previous process have been included in the Appendix B of this review.

The selected search terms also set speciﬁc limitations for the publications identiﬁed and analyzed in the review. Using the term “EEG-based” could set speciﬁc limitations for the search results and term “EEG” could be used in order to obtain a wider variety of search results. The aforementioned use of speciﬁc search words could be the reason why some of the publications, for example [222,230–233], have not been identiﬁed for screening during the ﬁrst phase of the review. As the publications have been identiﬁed for analysis until 2019, this aspect would need to be also considered as a limitation for the review.

6.1. Challenges

The challenges for the BCI applications could be divided into technology-related and user-related, where technology-related challenges comprise technical aspects and the usability of the system and the user-related contain the aspects of a person to learn to use the BCI application and subjectiveness of the person to interpret the cues that generate

<!-- page 21 -->

Sensors 2022, 22, 3331 21 of 44

or alter the acquired EEG signals [5]. Padﬁeld et al. [2] has categorized the possible challenges also as challenges faced in the research and development, challenges impeding commercialization, ﬂawed testing process, issues with BCI use and ethical issues. The categorizations could be also combined and distinguish different technology-related and user-related challenges under the ﬁve categories proposed by Padﬁeld et al. [2].

In terms of challenges, the major aspect would be the current reliability of the BCI system in everyday noisy environments [87]. This hindrance affects both medical and non-medical applications, but higher effect is for the non-medical applications due to the wider use outside of a controlled environment. The effect on non-medical applications is also signiﬁcant as the possibilities for the use of the EEG-based BCI applications in the non-medical domain is relatively wider and number of users is higher in comparison to the applications used in the medical domain.

In the medical domain (in the assistive ﬁeld), the challenges include low recognition rate for mental commands [158], problems with the signal acquisition equipment reliability and training process [117]. The character of the brain signals and the amplitude varies between persons, which makes it more difﬁcult to develop BCI applications suitable for all patients [6]. The work on separating speciﬁc EEG signals from other signals [234] and the hindrances concerning the aspect of cross-subject classiﬁcation [235] and accuracy of interpreting the commands [236] is ongoing. The authors agree that one of the important aspects is also the low throughput of information which may be a limiting factor in some applications [117,158]. The challenge of the low accuracy of the system has also been experienced in the ﬁeld of monitoring emotional responses [161]. In the rehabilitation ﬁeld, the complexity of the system setup and high cost of the devices has been noted [163]. In neurorehabilitation, it has been highlighted that the success of the therapeutic methods is hard to measure and the repetitiveness that is needed from the subject during the therapy could be demotivating [106]. Further research needs to be conducted to overcome the repetitions needed by the patient during the use of the BCI and possibilities to overcome time-consuming calibration for the BCI users [237].

Concerning BCI applications in the non-medical domain, Wei et al. have highlighted that in order to transition laboratory-oriented BCI applications into real-world environ- ments, the convenience to use and long-term wearing comfort for the devices needs to be improved [193]. There have been alternative devices created for this reason, to increase for example the user-friendliness of the devices meant to measure drowsiness at work [14]. During detection of human emotions, the hinderance could be the ambiguity of human emotions and the complexity of EEG signals [203]. There has also been works on the closed-loop interactions of human emotions with emotional stimuli for example in the case of music interface which complicates the system setup further [77]. In the ﬁeld of entertainment, it has been emphasized that the seamless interaction between user and the device is of utmost importance and a crucial concern [110].

The challenges hindering the development of BCI applications in both medical and non-medical settings involve poor portability of the hardware, low user-friendliness of the device, low signal quality and individual differences among persons that result in difﬁculties interpreting the EEG signals across users [6,193,238,239]. The accuracy of EEG pattern decoding is one of the key aspects for developing reliable BCI applications [240]. In current development of BCI applications the variability of EEG signals received from one subject and inter-subject variability has remained one of the most important obstacles [241] and the designing of subject-independent BCI systems has remained a challenge [242].

The use of current subject-dependent applications is time consuming due to training and especially inconvenient for people with mental disabilities [243]. Therefore, in addition to the BCI application functioning for one speciﬁc person, it would be important to develop subject-independent BCI systems that can be used by various users without previous train- ing [241]. The challenge in developing subject-independent BCI applications is to overcome person-dependent scenarios where the training and sets come from the same person and would require high-performance person-independent classiﬁcation [238]. Overcoming the

<!-- page 22 -->

Sensors 2022, 22, 3331 22 of 44

challenge would enable efﬁcient use of subject-independent system in turn enabling wider implementation of the BCI applications.

Both medical and non-medical domains are affected by potential ethical issues in the EEG-based BCI applications ﬁled of research. It would need to be determined for example who would be liable in case of any accidents during the use of BCI applications or could the applications affect, for example, user’s mood and therefore affect user’s decision making in a broader sense [2]. It has been shown that under certain circumstances it would be possible to probe subliminally private information from the users using EEG-based BCI devices [83]. In case the ethical and security aspects of the BCI applications are not controlled, an especially wider spread of non-medical devices could be used to exploit user emotions to push targeted marketing and political agendas [2]. These aspects would need to be considered and the users would need to be notiﬁed about the possible risks and responsibilities. Ethical standards would need to be established in order to guide the general development of BCI technology and prevent ethical issues preemptively [2].

6.2. Future Possibilities

It has been suggested that in order to make the EEG-based BCI applications more accurate and efﬁcient hybrid BCI systems should be developed that combine BCI systems with another BCI or other kinds of interfaces [2]. In addition to the use of only EEG for obtaining the biological signals, other methods could be used to support the strength and quality of the signals such as fNIRS or fMRI [6]. Such other physiological measures could also be heart rate or eye movements [1].

Increasing attention has been paid to fNIRS due to the advantages such as non- invasiveness, user safety, affordability and portability, but fNIRS signals are highly subject- speciﬁc and have low test-retest reliability [244]. Barrios et al. [245] have also suggested that combining fMRI with EEG could overcome signiﬁcant limitations that are present in the use of EEG alone. Padﬁeld et al. [2] have suggested to combine as well different approaches using EEG, such as motor-imagery system together with steady-state visually evoked potential as a training aid. In addition, combining different methods such as fNIRS with motor-imagery EEG or motor-imagery EEG with sensory interface has been proposed by Padﬁeld et al. [2].

6.2.1. Possibilities in Medical Domain

In the medical domain, the BCI could be used to control a variety of assistive robotic devices. EEG-based BCI applications have been developed for controlling wheelchairs [111,200], and research has been conducted on the development of robotic limbs [158]. Recent studies have shown additional success for the development of EEG-based BCI applications for controlling robotic devices [246,247]. Further research could be pursued in order to develop humanoid robots and drones for the support of daily activities for the patients [6].

It has been further suggested to use virtual reality in neuro rehabilitation, where motor- imagery BCI virtual reality systems could be used for real time applications for stroke rehabilitation, to increase motivation of the patient during the rehabilitation process [106]. The monitoring of EEG could be used to enhance speech therapy sessions for people who stutter, providing real-time visualization of the brain and insights concerning the brain activity during the sessions [43]. Jeunet et al. [11] have suggested BCI neurofeedback for the reduction of hypokinetic activity in case of a stroke and reducing hyperkinetic activity in case of attention deﬁcit hyperactivity disorder (ADHD).

6.2.2. Possibilities in Non-Medical Domain

In the non-medical domain, there is a high potential for the EEG-based BCI applications monitoring cognitive load, attention, drowsiness and other aspects of the mind. Monitoring cognitive load has been studied by Friedman et al. for intelligence tests, but measuring cognitive load could also be used to better design and conduct e-learning, psychometric exams, military training and other trainings [84].

<!-- page 23 -->

Sensors 2022, 22, 3331 23 of 44

Several studies have been published on monitoring attention via EEG-based BCI applications [3,150,171]. The level of attention is essential, both in the learning process and during tasks with high responsibility. Sethi et al. [171] have developed EEG-based attention feedback to improve focus in e-learning, but the principles could also be applied for drivers to test their reﬂexes and attentiveness and for driving instructors to assess the capability of the drivers. The monitoring of attention level could also be used to correlate stress with attention level and creativity with attention level. According to Sethi et al. [171] for example, optimal stress level can boost attention, and with the help of monitoring, attention optimal stress level could be determined, i.e., when the attention level for the individual is the highest.

EEG-based BCI applications could be further developed for wider authentication of persons in addition to currently available methods [37]. It has been suggested that EEG data could also be used for deceit identiﬁcation. As polygraphy test is not fully reliable and the results could be altered in case of speciﬁc practice and training by the subject. EEG data could be an important alternative for deceit identiﬁcation in the future [74]. Punsawad et al. [161] have suggested that the monitoring of human emotions via EEG-based BCI application could be applied in neuromarketing for product branding and advertising slogan design.

Entertainment is an ever-developing ﬁeld and includes, for example, gaming. The availability and user friendliness of the games using EEG-based BCI has been increasing over time [110]. With further development of the technology and integration with currently available technologies there are numerous possibilities for the use of EEG-based BCI for games for both entertainment and serious games for training purposes [8].

The main reasons for the higher pace of development in the non-medical domain are due to the high potential of the domain for a wider range of users when compared to the medical domain. While development in medical domain is focusing on speciﬁc patient groups the EEG-based BCI applications in non-medical domain could be used by the general public, for example for smart home control, entertainment or gaming. The range of use for the devices in the non-medical domain is continuously broadening as new possibilities emerge for the use of the devices in new situations such as deceit identiﬁcation test [74] or authentication based on emotionally signiﬁcant images [166].

EEG-based BCI applications have a wide variety of applications in both medical and non-medical domains, with even higher potential recently in the non-medical domain due to a high number of potential users around the world. With the development of the technology, reduction in cost and increase in comfort of use the EEG-based BCI applications can gain increasing attention in the non-medical domain.

6.2.3. Safety and User-Friendliness

During the daily use of EEG-based BCI applications, the safety of use is one of the most important aspects to focus on. In case of synchronous BCI, the controlling of the BCI is divided into time windows when the commands by the user could be given and the transfer of commands from the user to the device is well deﬁned. For the user, asynchronous BCI applications would be preferred, as in case of asynchronous applications the commands could be given to the device at any time, independent of speciﬁc time windows. From the safety perspective, it is important to deﬁne, in case of asynchronous devices, when the user actually wanted to give command and when the user was thinking other thoughts not related to the use of the device. For this reason, the concept of “brain switch” would need to be further developed in practice, enabling the user to mentally disconnect from the device when the user is not intending to use the device [6,131].

Further possibilities for the EEG-based BCI applications include new, more convenient methods for obtaining EEG signals. Wei et al. [193] have suggested measuring EEG from non-hair-bearing scalp areas for the further ease of use during long-term usage of the EEG-based BCI devices in everyday situations. It has also been shown that in some cases it would be sufﬁcient to measure EEG only near the ear that could make the use of EEG-based

<!-- page 24 -->

Sensors 2022, 22, 3331 24 of 44

BCI applications more convenient [113]. In order to make the use of BCI applications more efﬁcient and further integrate the possibilities into our daily tasks, BCIs could be integrated with augmented reality which would create new dimensions of user experience and practicality [15].

## 7. Analysis/Synthesis

In the current review, both articles and conference proceedings have been included. The inclusion of both these types in the analysis gives better representation of the ideas in the ﬁeld and helps reduce possible publication bias.

Although initially the EEG-based BCI applications were mainly developed for medical purposes to help patients and support in daily activities, the focus has been moving from the medical domain to non-medical applications. The shift in focus does not reduce the importance of these applications in the medical domain but rather shows the wider potential of EEG-based BCI applications and opens new doors for applying the possibilities mode broadly.

As per region, 111 publications (55%) have been contributed by Asia being ﬁrmly in the lead concerning number of studies published. From Asia most of the publications per country have been contributed by China. This is a relevant ﬁnding as China has increasing inﬂuence in general in high technology sector and EEG-based BCI could be one important ﬁeld of research resulting in a high variety of high technology applications designed for many different ﬁelds of life, both medical and non-medical. The high potential of EEG- based BCI applications and diverse possibilities for use could support the future economic strength of the countries and regions investing in the research and development in the ﬁeld.

The reasons of the general popularity of Emotiv EPOC (Emotiv, San Francisco, CA, USA) EEG device are its relatively low cost, sufﬁcient number of EEG channels and it being considered easy to use. Emotiv EPOC (Emotiv, San Francisco, CA, USA) and MindWave (NeuroSky, San Jose, CA, USA) are considered to be low-cost consumer EEG devices whereas Quik-Cap (Compumedics Neuroscan, Charlotte, NC, USA) is higher in cost. Emotiv EPOC (Emotiv, San Francisco, CA, USA) EEG device has 14 channels and MindWave (NeuroSky, San Jose, CA, USA) 1 channel, whereas the Quik-Cap (Compumedics Neuroscan, Charlotte, NC, USA) EEG device uses 32 channels. MindWave (NeuroSky, San Jose, CA, USA) EEG device has limitations in use due to the limited number of EEG channels, but the low cost and ease of use make the device popular. The device could be applied in speciﬁc applications that do not require higher number of EEG channels. The Quik-Cap (Compumedics Neuroscan, Charlotte, NC, USA) device on the other hand is more expensive but has the advantage of higher number of EEG channels. The ﬁnal decision concerning the use of a speciﬁc EEG device depends on the type of EEG-based BCI application, determining the need for speciﬁc number of EEG channels. The decision also depends on the cost planned for the study and the end users.

When planning the selection of the EEG device and number of channels, it is important to consider the end users for the EEG-based BCI application, which determines the technical requirements and possible overall cost of the device. A smaller number of carefully selected electrode positions would also make the device more user friendly and support the performance of the system.

There is a general trend noted in the overall use of various techniques. As in case of motor-imagery, auditory evoked potential and vibrotactile evoked potential technique the main application is in the medical domain, but the majority and larger variety of techniques are applied in the non-medical domain. As seen from the results of the current review, a highly diverse selection of techniques has been applied in the non-medical ﬁeld supporting further the development of diverse applications and supporting the high potential of non-medical applications among the EEG-based BCI applications.

In the current review, a trend of high prevalence of using power spectral density and Fourier transform for feature extraction has been noted. The overall results correlate with previous studies in the ﬁeld, highlighting the importance of these methods for feature

<!-- page 25 -->

Sensors 2022, 22, 3331 25 of 44

extraction and emphasizing the need to apply different types of feature extraction methods depending on the application under study. The results of the current review also show the importance of linear discriminant analysis and support vector machine for classiﬁcation in correlation with previous studies in the ﬁeld. The choice for classiﬁcation algorithm depends on the type of brain signal being recorded and the type of application that is being controlled.

With the widespread use of the devices, the safety on an individual and community level would need to be further analyzed. Nowadays, it has been unfortunately common that due to security breaches malicious software have inﬁltrated computer networks even with a high security level. This needs to be taken into consideration, especially when considering the sensitivity of the biomedical information obtained from the BCI device and also the possibility to alter the brain signals for example via neurofeedback. As the ﬁeld of EEG-based BCI is fast developing, the ethical aspects would need to be analyzed and safeguarded in parallel with the development of technology.

The BCI applications are developing rapidly and therefore it is important to have an up-to-date overview on the EEG-based BCI applications together with possible challenges and the way forward. The signiﬁcance of the current review is to provide an overview of the current work conducted in the ﬁeld of EEG-based BCI applications, along with the challenges and future possibilities.

Author Contributions: Conceptualization, Y.M., N.M. and K.V.; methodology, K.V., Y.M. and N.M.; formal analysis, K.V., N.M. and Y.M.; investigation, K.V.; writing—original draft preparation, K.V.; writing—review and editing, K.V., N.M. and Y.M.; visualization, K.V.; supervision, Y.M. and N.M.; project administration, Y.M. and N.M. All authors have read and agreed to the published version of the manuscript.

Funding: The research has been funded by the European Social Fund via the Estonian Education and Youth Board and IT Academy Programme.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Conﬂicts of Interest: The authors declare no conﬂict of interest. The funders had no role in the design of the review; in the collection, analyses, or interpretation of data; in the writing of the manuscript; or in the decision to publish the results.

## Appendix A. Search Terms Used

The search was conducted in the databases PubMed, Scopus and Web of Science using basic search settings with the below-described search terms relevant for current review. The search was conducted in PubMed database on 20 October 2019 with the search term (“electroencephalography based” OR “EEG based”) AND (“brain computer interface” OR “BCI” OR “brain machine interface” OR “BMI”) AND (“application” OR “applications”).

The search resulted in 185 publications that were then included for further screening.

The search in the Web of Science database was conducted on 28 October 2019 with the search term (“electroencephalography based” OR “EEG based”) AND (“brain computer interface” OR “BCI” OR “brain machine interface” OR “BMI”) AND (“application” OR “applications”) and the search in Web of Science database resulted in 451 publications.

The search in the Scopus database was conducted on 30 October 2019 using search term (“electroencephalography based” OR “EEG based”) AND (“brain computer interface” OR “BCI” OR “brain machine interface” OR “BMI”) AND (“application” OR “applications”) and 569 publications were identiﬁed through the search for inclusion to further screening.

<!-- page 26 -->

Sensors 2022, 22, 3331 26 of 44

## Appendix B

Table A1. Listing of Additional Publications from the Period of 31 October 2019 Until 26 June 2021.

Author Year Published Title

Choi et al. 2019 A multi-day and multi-band dataset for a steady-state visual-evoked potential-based brain–computer interface

Ganorkar and Raut 2019 Comparative analysis of mother wavelet selection for eeg signal application to motor imagery-based brain–computer interface

Hekmatmanesh et al. 2019 Combination of discrete wavelet packet transform with detrended ﬂuctuation analysis using customized mother wavelet with the aim of an imagery-motor control interface for an exoskeleton

Khan et al. 2019 Multiclass EEG motor-imagery classiﬁcation with sub-band common spatial patterns

Khoshnevis and Ghorshi 2019 Recovery of event-related potential signals using compressive sensing and kronecker technique

Liu et al. 2019 Fully Passive Flexible Wireless Neural Recorder for the Acquisition of Neuropotentials from a Rat Model

Mebarkia and Reffad 2019 Multi optimized SVM classiﬁers for motor imagery left and right hand movement identiﬁcation

Nagabushan et al. 2019 A comparative study of motor imagery-based BCI classiﬁers on EEG and iEEG data

Onay and Kose 2019 Assessment of CSP-based two-stage channel selection approach and local transformation-based feature extraction for classiﬁcation of motor imagery/movement EEG data

Oralhan 2019 2 Stages-region-based P300 Speller in Brain–Computer Interface

Saikia and Paul 2019 EEG signal processing and its classiﬁcation for rehabilitation device control

Taran and Bajaj 2019 Motor imagery tasks-based EEG signals classiﬁcation using tunable-Q wavelet transform

Wu et al. 2019 A Parallel Multiscale Filter Bank Convolutional Neural Networks for Motor Imagery EEG Classiﬁcation

Yao and Shoaran 2019 Enhanced Classiﬁcation of Individual Finger Movements with ECoG

Yu Chen and Mehmood 2019 A critical review on state-of-the-art EEG-based emotion datasets

Zhang et al. 2019 A Graph-Based Hierarchical Attention Model for Movement Intention Detection from EEG Signals

Zhang et al. 2019 Deep Learning Decoding of Mental State in Non-invasive Brain Computer Interface

Aggarwal and Chugh 2020 A decade of EEG Analysis: Prospects & Challenges in Biometric System

Alakus and Turkoglu 2020 Emotion recognition with deep learning using GAMEEMO data set

Alhakeem et al. 2020 Wheelchair Free Hands Navigation Using Robust DWT-AR Features Extraction Method with Muscle Brain Signals

Ali et al. 2020 Classiﬁcation of Motor Imagery Task by Using Novel Ensemble Pruning Approach

Al-Nafjan et al. 2020 Lightweight Building of an Electroencephalogram-Based Emotion Detection System

Andrade et al. 2020 An EEG Brain–Computer Interface to Classify Motor Imagery Signals

Angrisani et al. 2020 Instrumentation for motor imagery-based brain computer interfaces relying on dry electrodes: A functional analysis

<!-- page 27 -->

Sensors 2022, 22, 3331 27 of 44

Table A1. Cont.

Author Year Published Title

Araki et al. 2020 Wireless Monitoring Using a Stretchable and Transparent Sensor Sheet Containing Metal Nanowires

Arico et al. 2020 Brain–Computer Interfaces: Toward a Daily Life Employment

Aroudi and Doclo 2020 Cognitive-Driven Binaural Beamforming Using EEG-Based Auditory Attention Decoding

Bablani et al. 2020 A multi stage EEG data classiﬁcation using k-means and feed forward neural network

Bigirimana et al. 2020 Emotion-Inducing Imagery Versus Motor Imagery for a Brain–Computer Interface

Borra et al. 2020 Interpretable and lightweight convolutional neural network for EEG decoding: Application to movement execution and imagination

Borra et al. 2020 Convolutional Neural Network for a P300 Brain–Computer Interface to Improve Social Attention in Autistic Spectrum Disorder

Cao and Grover 2020 STIMULUS: Noninvasive Dynamic Patterns of Neurostimulation Using Spatio-Temporal Interference

Castro et al. 2020 Development of a Deep Learning-Based Brain–Computer Interface for Visual Imagery Recognition

Cha et al. 2020 Prediction of individual user’s dynamic ranges of EEG features from resting-state EEG data for evaluating their suitability for passive brain–computer interface applications

Chamola et al. 2020 Brain–computer interface-based humanoid control: A review

Chen et al. 2020 EEG-based biometric identiﬁcation with convolutional neural network

Chen et al. 2020 Emotion recognition from spatiotemporal EEG representations with hybrid convolutional recurrent neural networks via wearable multi-channel headset

Cheng et al. 2020 Motion Imagery-BCI Based on EEG and Eye Movement Data Fusion

Cho et al. 2020 A Novel Approach to Classify Natural Grasp Actions by Estimating Muscle Activity Patterns from EEG Signals

Cho et al. 2020 Decoding of Grasp Motions from EEG Signals Based on a Novel Data Augmentation Strategy

Cortez et al. 2020 Improving Speller BCI performance using a cluster-based under-sampling method

Cortez et al. 2020 Under-sampling and Classiﬁcation of P300 Single-Trials using Self-Organized Maps and Deep Neural Networks for a Speller BCI

Cozza et al. 2020 Dimension Reduction Techniques in a Brain–Computer Interface Application

Cudlenco et al. 2020 Reading into the mind’s eye: Boosting automatic visual recognition with EEG signals

de Melo et al. 2020 EEG Analysis in Coincident Timing Task Towards Motor Rehabilitation

Delvigne et al. 2020 Attention Estimation in Virtual Reality with EEG-based Image Regression

Deng et al. 2020 Self-adaptive shared control with brain state evaluation network for human-wheelchair cooperation

Deng et al. 2020 A Bayesian Shared Control Approach for Wheelchair Robot with Brain Machine Interface

Dimitrov et al. 2020 Increasing the Classiﬁcation Accuracy of EEG-based Brain–computer Interface Signals

<!-- page 28 -->

Sensors 2022, 22, 3331 28 of 44

Table A1. Cont.

Author Year Published Title

Dutta and Nandy 2020 An extensive analysis on deep neural architecture for classiﬁcation of subject-independent cognitive states

Dutta et al. 2020 Development of a BCI-based gaming application to enhance cognitive control in psychiatric disorders

Elessawy et al. 2020 A long short-term memory autoencoder approach for EEG motor imagery classiﬁcation

Elkafrawy et al. 2020 Proposed model for thought-based animation based on classifying EEG signals using estimated parameters and multi-SVM

Fathima and Kore 2020 Enhanced Differential Evolution-Based EEG Channel Selection

Feng et al. 2020 Decoding of voluntary and involuntary upper-limb motor imagery based on graph fourier transform and cross-frequency coupling coefﬁcients

Filipp et al. 2020 Application of brain–computer interfaces in assistive technologies

Fontanillo et al. 2020 Beyond Technologies of Electroencephalography-Based Brain–Computer Interfaces: A Systematic Review From Commercial and Ethical Aspects

Gembler et al. 2020 Five Shades of Grey: Exploring Quintary m-Sequences for More User-Friendly c-VEP-Based BCIs

Ghosh et al. 2020 Bi-directional Long Short-Term Memory model to analyze psychological effects on gamers

Gorriz et al. 2020 Artiﬁcial intelligence within the interplay between natural and artiﬁcial computation: Advances in data science, trends and applications

Grissmann et al. 2020 Context Sensitivity of EEG-Based Workload Classiﬁcation Under Different Affective Valence

Gu et al. 2020 The effects of varying levels of mental workload on motor imagery-based brain computer interface

Gubert et al. 2020 The performance impact of data augmentation in CSP-based motor-imagery systems for BCI applications

Gurve et al. 2020 Trends in Compressive Sensing for EEG Signal Processing Applications

Haira et al. 2020 A comparison of ECG and EEG metrics for in-ﬂight monitoring of helicopter pilot workload

Hernandez-Cuevas et al. 2020 Neurophysiological Closed-Loop Control for Competitive Multi-brain Robot Interaction

Hussain and Park 2020 HealthSOS: Real-Time Health Monitoring System for Stroke Prognostics

Idowu et al. 2020 Efﬁcient Classiﬁcation of Motor Imagery using Particle Swarm Optimization-based Neural Network for IoT Applications

Ieracitano et al. 2020 A novel multi-modal machine learning-based approach for automatic classiﬁcation of EEG recordings in dementia

Jeng et al. 2020 Low-Dimensional Subject Representation-based Transfer Learning in EEG Decoding

Jin et al. 2020 EEG classiﬁcation using sparse Bayesian extreme learning machine for brain–computer interface

Kalafatovich et al. 2020 Decoding Visual Recognition of Objects from EEG Signals based on Attention-Driven Convolutional Neural Network

Kang et al. 2020 EEG-Based Prediction of Successful Memory Formation During Vocabulary Learning

<!-- page 29 -->

Sensors 2022, 22, 3331 29 of 44

Table A1. Cont.

Author Year Published Title

Kaongoen and Jo 2020 An Ear-EEG-based Brain–Computer Interface using Concentration Level for Control

Kaur et al. 2020 A study of EEG for enterprise multimedia security

Khan et al. 2020 High performance multi-class motor imagery EEG classiﬁcation

Kouddad et al. 2020 Indexing and Image Search by the Content According to the Biological Base of the Cognitive Processing of Information using a Neural Sensor

Kurapa et al. 2020 A Hybrid Approach for Extracting EMG signals by Filtering EEG Data for IoT Applications for Immobile Persons

Kuzovkin et al. 2020 Mental state space visualization for interactive modeling of personalized BCI control strategies

Kwon et al. 2020 Decoding of Intuitive Visual Motion Imagery Using Convolutional Neural Network under 3D-BCI Training Environment

Landau et al. 2020 Mind Your Mind: EEG-Based Brain–Computer Interfaces and Their Security in Cyber Space

Lee et al. 2020 Complex Motor Imagery-based Brain–Computer Interface System: A Comparison between Different Classiﬁers

Lee et al. 2020 Classiﬁcation of Upper Limb Movements Using Convolutional Neural Network with 3D Inception Block

Leon et al. 2020 Deep learning for EEG-based Motor Imagery classiﬁcation: Accuracy-cost trade-off

Li et al. 2020 Enhancing BCI-Based Emotion Recognition Using an Improved Particle Swarm Optimization for Feature Selection

Liang et al. 2020 EEG-Based EMG Estimation of Shoulder Joint for the Power Augmentation System of Upper Limbs

Lin et al. 2020 A Multi-Scale Activity Transition Network for Data Translation in EEG Signals Decoding

Luo et al. 2020 EEG Signal Reconstruction Using a Generative Adversarial Network With Wasserstein Distance and Temporal-Spatial-Frequency Loss

Luo et al. 2020 Estimation of Motor Imagination Based on Consumer-Grade EEG Device

Ma et al. 2020 Online learning using projections onto shrinkage closed balls for adaptive brain computer interface

Mattia et al. 2020

The Promotoer, a brain–computer interface-assisted intervention to promote upper limb functional motor recovery after stroke: a study protocol for a randomized controlled trial to test early and long-term efﬁcacy and to identify determinants of response

Miao et al. 2020 Spatial-Frequency Feature Learning and Classiﬁcation of Motor Imagery EEG Based on Deep Convolution Neural Network

Min and Cai 2020 Driver Fatigue Detection Based on Multi-scale Wavelet Log Energy Entropy of Frontal EEG

Mishra et al. 2020 Effect of hand grip actions on object recognition process: a machine learning-based approach for improved motor rehabilitation

Mondini et al. 2020 Continuous low-frequency EEG decoding of arm movement for closed-loop, natural control of a robotic arm

Nakagome et al. 2020 An empirical comparison of neural networks and machine learning algorithms for EEG gait decoding

<!-- page 30 -->

Sensors 2022, 22, 3331 30 of 44

Table A1. Cont.

Author Year Published Title

Netzer et al. 2020 Real-time EEG classiﬁcation via coresets for BCI applications

Nisar et al. 2020 Reducing Sensors in Mental Imagery-Based Cognitive Task for Brain Computer Interface

Pa Aung and New 2020 Regions of Interest (ROI) Analysis for Upper Limbs EEG Neuroimaging Schemes

Padmavathy et al. 2020 A novel deep learning classiﬁer and genetic algorithm-based feature selection for hybrid EEG-FNIRS brain–computer interface

Paek et al. 2020 Towards a Portable Magnetoencephalography-Based Brain Computer Interface with Optically-Pumped Magnetometers

Pan et al. 2020 Prognosis for patients with cognitive motor dissociation identiﬁed by brain–computer interface

Pan et al. 2020 EEG-Based Emotion Recognition Using Logistic Regression with Gaussian Kernel and Laplacian Prior and Investigation of Critical Frequency Bands

Parikh and George 2020 Quadcopter Control in Three-Dimensional Space Using SSVEP and Motor Imagery-Based Brain–Computer Interface

Petukhov et al. 2020 Being present in a real or virtual world: A EEG study

Philip and George 2020 Visual P300 Mind-Speller Brain–Computer Interfaces: A Walk Through the Recent Developments With Special Focus on Classiﬁcation Algorithms

Qin et al. 2020 Smart Home Control for Disabled Using Brain Computer Interface

Rakshit et al. 2020 A Hybrid Brain–Computer Interface for Closed-Loop Position Control of a Robot Arm

Rashid et al. 2020 Current Status, Challenges, and Possible Solutions of EEG-Based Brain–Computer Interface: A Comprehensive Review

Rashid et al. 2020 Five-Class SSVEP Response Detection using Common-Spatial Pattern (CSP)-SVM Approach

Riyad et al. 2020 Incep-eegnet: A convnet for motor imagery decoding

Roy et al. 2020 A hybrid classiﬁer combination for home automation using EEG signals

Sadiq et al. 2020 Identiﬁcation of motor and mental imagery EEG in two and multiclass subject-dependent tasks using successive decomposition index

Sahu et al. 2020 EEG signal analysis and classiﬁcation on P300 speller-based BCI performance in ALS patients

Schembri et al. 2020 The Effect That Auditory Distractions Have on a Visual P300 Speller While Utilizing Low Cost Off-the-Shelf Equipment

Schneider et al. 2020 Real-time EEG Feedback on Alpha Power Lateralization Leads to Behavioral Improvements in a Covert Attention Task

Shao et al. 2020 EEG-Controlled Wall-Crawling Cleaning Robot Using SSVEP-Based Brain–Computer Interface

She et al. 2020 Multi-class motor imagery EEG classiﬁcation using collaborative representation-based semi-supervised extreme learning machine

Shi et al. 2020 Feature Extraction of Brain–Computer Interface Electroencephalogram Based on Motor Imagery

Siddharth and Trivedi 2020 On assessing driver awareness of situational criticalities: Multi-modal bio-sensing and vision-based analysis, evaluations, and insights

Singh and Singh 2020 Realising transfer learning through convolutional neural network and support vector machine for mental task classiﬁcation

Song et al. 2020 A Practical EEG-Based Human-Machine Interface to Online Control an Upper-Limb Assist Robot

<!-- page 31 -->

Sensors 2022, 22, 3331 31 of 44

Table A1. Cont.

Author Year Published Title

Suma et al. 2020 Spatial-temporal aspects of continuous EEG-based neurorobotic control

Sun et al. 2020 Multimodal affective state assessment using fNIRS+ EEG and spontaneous facial expression

Talukdar et al. 2020 Adaptive feature extraction in EEG-based motor imagery BCI: tracking mental fatigue

Tan et al. 2020 Spiking Neural Networks: Background, Recent Development and the NeuCube Architecture

Tao 2020 Classiﬁcation-Oriented Fuzzy-Rough Feature Selection for the EEG-Based Brain Computer Interfaces

Tiwari et al. 2020 Machine Learning approach for the classiﬁcation of EEG signals of multiple imagery tasks

Torkamani-Azar et al. 2020 Prediction of Motor Imagery Performance based on Pre-Trial Spatio-Spectral Alertness Features

Torres et al. 2020 EEG-Based BCI Emotion Recognition: A Survey

Tzdaka et al. 2020 Assessing the Relevance of Neurophysiological Patterns to Predict Motor Imagery-based BCI Users’ Performance

Vigue-Guix et al. 2020 Can the occipital alpha-phase speed up visual detection through a real-time EEG-based brain–computer interface (BCI)?

Wafeek et al. 2020 A Novel EEG Classiﬁcation Technique Based on Particle Swarm Optimization for Hand and Finger Movements

Wang et al. 2020 Enhancing gesture decoding performance using signals from posterior parietal cortex: a stereo-electroencephalograhy (SEEG) study

Wang et al. 2020 P300 Recognition Based on Ensemble of SVMs

William et al. 2020 ERP Template Matching for EEG Single Trial Classiﬁcation

Wolpaw et al. 2020 Brain–computer interfaces: Deﬁnitions and principles

Xu et al. 2020 Implementing Over 100 Command Codes for a High-Speed Hybrid Brain–Computer Interface Using Concurrent P300 and SSVEP Features

Xu et al. 2020 Motor Imagery-Based Continuous Teleoperation Robot Control with Tactile Feedback

Xu et al. 2020 Two-level multi-domain feature extraction on sparse representation for motor imagery classiﬁcation

Yan et al. 2020 An improve d common spatial pattern combine d with channel-selection strategy for electroencephalography-based emotion recognition

Yang et al. 2020 MI3DNet: A Compact CNN for Motor Imagery EEG Classiﬁcation with Visualizable Dense Layer Parameters

Yao et al. 2020 Information-preserving feature ﬁlter for short-term EEG signals

Yi 2020 Efﬁcient machine learning algorithm for electroencephalogram modeling in brain–computer interfaces

Zeng et al. 2020 InstanceEasyTL: An Improved Transfer-Learning Method for EEG-Based Cross-Subject Fatigue Detection

Zhang et al. 2020 Pain Control by Co-adaptive Learning in a Brain–Machine Interface

Zhang et al. 2020 Application of transfer learning in eeg decoding based on brain–computer interfaces: A review

Zhou et al. 2020 A Hybrid Asynchronous Brain–Computer Interface Combining SSVEP and EOG Signals

<!-- page 32 -->

Sensors 2022, 22, 3331 32 of 44

Table A1. Cont.

Author Year Published Title

Zhuang et al. 2020 State-of-the-art non-invasive brain–computer interface for neural rehabilitation: A review

Aldayel et al. 2021 Consumers’ Preference Recognition Based on Brain–Computer Interfaces: Advances, Trends, and Applications

Alhudhaif 2021 An effective classiﬁcation framework for brain–computer interface system design based on combining of fNIRS and EEG signals

Al-Saegh et al. 2021 Deep learning for motor imagery EEG-based classiﬁcation: A review

Alzahab et al. 2021 Hybrid deep learning (Hdl)-based brain–computer interface (bci) systems: A systematic review

Asogbon et al. 2021 A linearly extendible multi-artifact removal approach for improved upper extremity EEG-based motor imagery decoding.

Aydarkhanov et al. 2021 Closed-loop EEG study on visual recognition during driving

Belo et al. 2021 EEG-Based Auditory Attention Detection and Its Possible Future Applications for Passive BCI

Benaroch et al. 2021 Long-Term BCI Training of a Tetraplegic User: Adaptive Riemannian Classiﬁers and User Training

Bhattacharyya et al. 2021 Neuro-feedback system for real-time BCI decision prediction

Cattai et al. 2021 Phase/Amplitude Synchronization of Brain Signals During Motor Imagery BCI Tasks.

Chaudhary et al. 2021 Neuropsychological and neurophysiological aspects of brain–computer interface (BCI) control in paralysis

Chen et al. 2021 EEG-Based Anxious States Classiﬁcation Using Affective BCI-Based Closed Neurofeedback System

Chen et al. 2021 Implementing a calibration-free SSVEP-based BCI system with 160 targets.

Fu et al. 2021 Recognizing single-trial motor imagery EEG based on interpretable clustering method

Georgiev et al. 2021 Virtual reality for neurorehabilitation and cognitive enhancement

Gu et al. 2021 EEG-based Brain–Computer Interfaces (BCIs): A Survey of Recent Studies on Signal Sensing Technologies and Computational Intelligence Approaches and Their Applications

Guner and Erkmen 2021 A Low-Cost Real-Time BCI Integration for Automated Door Opening System

Gupta et al. 2021 Brain computer interface controlled automatic electric drive for neuro-aid system

Hong et al. 2021 Dynamic Joint Domain Adaptation Network for Motor Imagery Classiﬁcation

Islam et al. 2021 Auditory Evoked Potential (AEP)-Based Brain–Computer Interface (BCI) Technology: A Short Review

Islam et al. 2021 Probability mapping-based artifact detection and removal from single-channel EEG signals for brain–computer interface applications.

Jeng et al. 2021 Low-Dimensional Subject Representation-Based Transfer Learning in EEG Decoding

Ketu et al. 2021 Hybrid classiﬁcation model for eye state detection using electroencephalogram signals

Khan et al. 2021 Analysis of Human Gait Using Hybrid EEG-fNIRS-Based BCI System: A Review

Kharchenko et al. 2021 Inﬂuence of Signal Preprocessing When Highlighting Steady-State Visual Evoked Potentials Based on a Multivariate Synchronization Index

<!-- page 33 -->

Sensors 2022, 22, 3331 33 of 44

Table A1. Cont.

Author Year Published Title

Kharchenko et al. 2021 Implementation of robot–human control bio-interface when highlighting visual-evoked potentials based on multivariate synchronization index

Kumar et al. 2021 The classiﬁcation of EEG-based winking signals: a transfer learning and random forest pipeline

Liu et al. 2021 P300 event-related potential detection using one dimensional convolutional capsule networks

Liu et al. 2021 Multiscale space-time-frequency feature-guided multitask learning CNN for motor imagery EEG classiﬁcation

Liu et al. 2021 A Utility Human Machine Interface Using Low Cost EEG Cap and Eye Tracker

Miladinovic et al. 2021 Effect of power feature covariance shift on BCI spatial-ﬁltering techniques: A comparative study

Mishra et al. 2021 Effect of hand grip actions on object recognition process: a machine learning-based approach for improved motor rehabilitation

Qi et al. 2021 Spatiotemporal-Filtering-Based Channel Selection for Single-Trial EEG Classiﬁcation

Qi et al. 2021 Wielding and evaluating the removal composition of common artefacts in EEG signals for driving behaviour analysis.

Rammy et al. 2021 Sequence-to-sequence deep neural network with spatio-spectro and temporal features for motor imagery classiﬁcation

Ravirahul et al. 2021 Mind Wave Controlled Assistive Robot

Reyes et al. 2021 LSTM-based brain–machine interface tool for text generation through eyes blinking detection

Riyad et al. 2021 A novel multi-scale convolutional neural network for motor imagery classiﬁcation

Rybar et al. 2021 Decoding of semantic categories of imagined concepts of animals and tools in fNIRS

Saga et al. 2021 Elucidation of EEG Characteristics of Fuzzy Reasoning-Based Heuristic BCI and Its Application to Patient With Brain Infarction

Santos et al. 2021 Comparison of LORETA and CSP for Brain–Computer Interface Applications

Shaban et al. 2021 Classiﬁcation of Lactate Level Using Resting-State EEG Measurements

Shahbakhti et al. 2021 VME-DWT: An Efﬁcient Algorithm for Detection and Elimination of Eye Blink from Short Segments of Single EEG Channel

Shi et al. 2021 A binary harmony search algorithm as channel selection method for motor imagery-based BCI

Somadder et al. 2021 Frequency Domain CSP for Foot Motor Imagery Classiﬁcation Using SVM for BCI Application

Stival et al. 2021 Connectivity modeling meets machine learning: The next generation of eeg-based brain computer interfaces

Sulaiman et al. 2021 Ofﬂine eeg-based dc motor control for wheelchair application

Sun et al. 2021 WLnet: Towards an Approach for Robust Workload Estimation Based on Shallow Neural Networks

Wang et al. 2021 EEG-based auditory attention decoding using speech-level-based segmented computational models

Xu et al. 2021 Review of brain encoding and decoding mechanisms for EEG-based brain–computer interface

<!-- page 34 -->

Sensors 2022, 22, 3331 34 of 44

Table A1. Cont.

Author Year Published Title

Yoo 2021 Electroencephalogram-based neurofeedback training in persons with stroke: A scoping review in occupational therapy

Yu et al. 2021 Cross-correlation-based discriminant criterion for channel selection in motor imagery BCI systems

Zeng et al. 2021 An EEG-Based Transfer Learning Method for Cross-Subject Fatigue Mental State Prediction

Zhang et al. 2021 Improving EEG Decoding via Clustering-Based Multitask Feature Learning

Zhang et al. 2021 EEG-inception: an accurate and robust end-to-end neural network for EEG-based motor imagery classiﬁcation

Zhang et al. 2021 Tiny noise, big mistakes: adversarial perturbations induce errors in brain–computer interface spellers

Zolfaghari et al. 2021 Using convolution neural networks pattern for classiﬁcation of motor imagery in bci system

## References

1. Abiri, R.; Borhani, S.; Sellers, E.W.; Jiang, Y.; Zhao, X. A comprehensive review of EEG-based brain–computer interface paradigms. J. Neural. Eng. 2018, 16, 011001. [CrossRef] [PubMed] 2. Padﬁeld, N.; Zabalza, J.; Zhao, H.; Masero, V.; Ren, J. EEG-Based Brain-Computer Interfaces Using Motor-Imagery: Techniques and Challenges. Sensors 2019, 19, 1423. [CrossRef] [PubMed] 3. Ramakuri, S.K.; Peddi, A.; Rao, K.S.N.; Gupta, B.; Ghosh, S. Performance and Analysis of Human Attention Using Single-Channel Wireless EEG Sensor for Medical Application’. In First International Conference on Artiﬁcial Intelligence and Cognitive Computing; Springer: Singapore, 2019; pp. 355–362. [CrossRef] 4. Anwar, D.; Gupta, A.; Naik, V.; Sharma, S.K. Detecting meditation using a dry mono-electrode EEG sensor. In Proceedings of the 2017 9th International Conference on Communication Systems and Networks (COMSNETS), Bengaluru, India, 4–8 January 2017; pp. 508–513. [CrossRef] 5. Al-Nafjan, A.; Hosny, M.; Al-Ohali, Y.; Al-Wabil, A. Review and Classiﬁcation of Emotion Recognition Based on EEG Brain- Computer Interface System Research: A Systematic Review. Appl. Sci. 2017, 7, 1239. [CrossRef] 6. Mao, X.; Li, M.; Li, W.; Niu, L.; Xian, B.; Zeng, M.; Chen, G. Progress in EEG-Based Brain Robot Interaction Systems. Comput. Intell. Neurosci. 2017, 2017, 1742862. [CrossRef] 7. Yang, Y.; Wu, Q.; Fu, Y.; Chen, X. Continuous convolutional neural network with 3D input for EEG-based emotion recognition. In Proceedings of the Neural Information Processing, Siem Reap, Cambodia, 13–16 December 2018; pp. 433–443. 8. Perales, F.J.; Amengual, E. A Serious Game Application using EEG-based Brain Computer Interface. In Proceedings of the NEUROTECHNIX 2013—International Congress on Neurotechnology, Electronics and Informatics, Algarve, Portugal, 19–21 September 2013; pp. 249–255. [CrossRef] 9. Lin, C.-T.; Chang, C.-J.; Lin, B.-S.; Hung, S.-H.; Chao, C.-F.; Wang, I.-J. A Real-Time Wireless Brain–Computer Interface System for Drowsiness Detection. IEEE Trans. Biomed. Circuits Syst. 2010, 4, 214–222. [CrossRef] 10. Tariq, M.; Trivailo, P.M.; Simic, M. EEG-Based BCI Control Schemes for Lower-Limb Assistive-Robots. Front. Hum. Neurosci. 2018, 12, 312. [CrossRef] 11. Jeunet, C.; Glize, B.; McGonigal, A.; Batail, J.-M.; Micoulaud-Franchi, J.-A. Using EEG-based brain computer interface and neurofeedback targeting sensorimotor rhythms to improve motor skills: Theoretical background, applications and prospects. Neurophysiol. Clin. Neurophysiol. 2018, 49, 125–136. [CrossRef] [PubMed] 12. Molina-Rueda, F.; Navarro-Fernández, C.; Cuesta-Gómez, A.; Alguacil-Diego, I.M.; Molero-Sánchez, A.; Carratalá-Tejada, M. Neuroplasticity Modiﬁcations Following a Lower-Limb Amputation: A Systematic Review. PMR 2019, 11, 1326–1334. [CrossRef] 13. Ramakuri, S.K.; Ghosh, S.; Gupta, B. Behaviour state analysis through brain computer interface using wearable EEG devices: A review. Electron. Gov. Int. J. 2017, 13, 377. [CrossRef] 14. Dhole, S.R.; Kashyap, A.; Dangwal, A.N.; Mohan, R. A novel helmet design and implementation for drowsiness and fall detection of workers on-site using EEG and Random-Forest Classiﬁer. Procedia Comput. Sci. 2019, 151, 947–952. [CrossRef] 15. Kim, M.; Kim, M.-K.; Hwang, M.; Kim, H.-Y.; Cho, J.; Kim, S.-P. Online Home Appliance Control Using EEG-Based Brain– Computer Interfaces. Electronics 2019, 8, 1101. [CrossRef] 16. Gao, Q.; Zhao, X.; Yu, X.; Song, Y.; Wang, Z. Controlling of smart home system based on brain-computer interface. Technol. Health Care 2018, 26, 769–783. [CrossRef]

<!-- page 35 -->

Sensors 2022, 22, 3331 35 of 44

17. Holzner, C.; Guger, C.; Grönegress, C.; Edlinger, G.; Slater, M. Using a P300 Brain Computer Interface for Smart Home Control. In World Congress on Medical Physics and Biomedical Engineering, Munich, Germany, 7–12 September 2009; Springer: Berlin/Heidelberg, Germany, 2009; pp. 174–177. [CrossRef] 18. Holzner, C.; Guger, C.; Edlinger, G.; Gronegress, C.; Slater, M. Virtual Smart Home Controlled by Thoughts. In Proceedings of the 2009 18th IEEE International Workshops on Enabling Technologies: Infrastructures for Collaborative Enterprises, Groningen, The Netherlands, 29 June–1 July 2009; pp. 236–239. [CrossRef] 19. Pan, X.; Zhang, Z.; Qu, J.; Zhao, C.; Li, Y. Enjoy driving from thought in a virtual city. In Proceedings of the 2017 36th Chinese Control Conference (CCC), Dalian, China, 26–28 July 2017; pp. 11034–11040. [CrossRef] 20. Yu, Y.; Zhou, Z.; Yin, E.; Jiang, J.; Tang, J.; Liu, Y.; Hu, D. Toward brain-actuated car applications: Self-paced control with a motor imagery-based brain-computer interface. Comput. Biol. Med. 2016, 77, 148–155. [CrossRef] 21. Arvutiteaduse instituut-Lõputööderegister’. Available online: https://comserv.cs.ut.ee/ati_thesis/datasheet.php?language=en (accessed on 9 January 2021). 22. Lotte, F.; Bougrain, L.; Cichocki, A.; Clerc, M.; Congedo, M.; Rakotomamonjy, A.; Yger, F. A review of classiﬁcation algorithms for EEG-based brain–computer interfaces: A 10 year update. J. Neural Eng. 2018, 15, 031005. [CrossRef] 23. Pasqualotto, E.; Federici, S.; Belardinelli, M.O. Toward functioning and usable brain–computer interfaces (BCIs): A literature review. Disabil. Rehabil. Assist. Technol. 2011, 7, 89–103. [CrossRef] [PubMed] 24. Kosmyna, N.; Lécuyer, A. A conceptual space for EEG-based brain-computer interfaces. PLoS ONE 2019, 14, e0210145. [CrossRef] 25. Alsharif, A.; Salleh, N.; Baharun, R.; Safaei, M. Neuromarketing Approach: An Overview and Future Research Directions. J. Theor. Appl. Inf. Technol. 2020, 98, 7. 26. Machado, S.; Araújo, F.; Paes, F.; Velasques, B.; Cunha, M.; Budde, H.; Basile, L.F.; Anghinah, R.; Arias-Carrión, O.; Cagy, M.; et al. EEG-based Brain-Computer Interfaces: An Overview of Basic Concepts and Clinical Applications in Neurorehabilitation. Rev. Neurosci. 2010, 21, 451–468. [CrossRef] 27. Nicolas-Alonso, L.F.; Gomez-Gil, J. Brain Computer Interfaces, a Review. Sensors 2012, 12, 1211–1279. [CrossRef] 28. Roy, Y.; Banville, H.; Albuquerque, I.; Gramfort, A.; Falk, T.H.; Faubert, J. Deep learning-based electroencephalography analysis: A systematic review. J. Neural Eng. 2019, 16, 051001. [CrossRef] 29. Craik, A.; He, Y.; Contreras-Vidal, J.L. Deep learning for electroencephalogram (EEG) classiﬁcation tasks: A review. J. Neural Eng. 2019, 16, 031001. [CrossRef] [PubMed] 30. Moher, D.; Liberati, A.; Tetzlaff, J.; Altman, D.G.; PRISMA Group. Preferred reporting items for systematic reviews and meta-analyses: The PRISMA statement. PLoS Med. 2009, 6, e1000097. [CrossRef] [PubMed] 31. PRISMA’. Available online: http://www.prisma-statement.org/PRISMAStatement/HistoryAndDevelopment (accessed on 9 November 2020). 32. Madhok, R.; Handoll, H.; Gillespie, W.J.; Gillespie, L.D. The Cochrane Collaboration: A leading role in producing reliable evidence to inform healthcare decisions in musculoskeletal trauma and disorders. Indian J. Orthop. 2008, 42, 247–251. [CrossRef] 33. PubMed’, PubMed. Available online: https://pubmed.ncbi.nlm.nih.gov/ (accessed on 5 January 2021). 34. SCOPUS. Available online: https://www.scopus.com/home.uri (accessed on 30 October 2019). 35. Web of Science. Available online: https://login.webofknowledge.com/error/Error?Error=IPError&PathInfo=%2F&RouterURL= https%3A%2F%2Fwww.webofknowledge.com%2F&Domain=.webofknowledge.com&Src=IP&Alias=WOK5 (accessed on 5 January 2021). 36. Kumar, S.V.K.; Julian, A. Oscitancy tracking using Brain-Computer Interface. In Proceedings of the 2012 IEEE Students’ Conference on Electrical, Electronics and Computer Science, Bhopal, India, 1–2 March 2012; pp. 1–4. [CrossRef] 37. Mustafa, I.; Farooq, H.; Khatri, T.K. EEG based user authentication using visual stimuli of geometric shapes. In Proceedings of the 2019 2nd International Conference on Communication, Computing and Digital systems (C-CODE). IEEE, Islamabad, Pakistan, 6–7 March 2019; pp. 247–251. [CrossRef] 38. Abu-Alqumsan, M.; Ebert, F.; Peer, A. Goal-recognition-based adaptive brain-computer interface for navigating immersive robotic systems. J. Neural Eng. 2017, 14, 036024. [CrossRef] [PubMed] 39. Adha, M.S.; Safri, N.; Othman, M.A. Real-time target selection based on electroencephalogram (EEG) signal. ARPN J. Eng. Appl. Sci. 2015, 10, 8757–8761. 40. Ahn, J.; Ku, Y.; Kim, D.; Sohn, J.; Kim, J.; Kim, H. Wearable in-the-ear EEG system for SSVEP-based brain–computer interface. Electron. Lett. 2018, 54, 413–414. [CrossRef] 41. Sun, A.; Fan, B.; Jia, C. Motor imagery EEG-based online control system for upper artiﬁcial limb. In Proceedings of the 2011 International Conference on Transportation, Mechanical, and Electrical Engineering (TMEE), Changchun, China, 16–18 December 2011; pp. 1646–1649. [CrossRef] 42. Al-Ghamdi, N.; Al-Hudhud, G.; Alzamel, M.; Al-Wabil, A. Trials and tribulations of BCI control applications. In Proceedings of the 2013 Science and Information Conference, London, UK, 7–9 October 2013; pp. 212–217. 43. Al-Nafjan, A.; Al-Wabil, A.; AlMudhi, A.; Hosny, M. Measuring and monitoring emotional changes in children who stutter. Comput. Biol. Med. 2018, 102, 138–150. [CrossRef] 44. Alnafjan, A.; Hosny, M.; Al-Wabil, A.; Al-Ohali, Y. Classiﬁcation of Human Emotions from Electroencephalogram (EEG) Signal using Deep Neural Network. Int. J. Adv. Comput. Sci. Appl. 2017, 8, 419–425. [CrossRef]

<!-- page 36 -->

Sensors 2022, 22, 3331 36 of 44

45. Aloise, F.; Schettini, F.; Aricò, P.; Bianchi, L.; Riccio, A.; Mecella, M.; Babiloni, F.; Mattia, D.; Cincotti, F. Advanced brain computer interface for communication and control. In Proceedings of the International Conference on Advanced Visual Interfaces, Roma, Italy, 26–28 May 2010; pp. 399–400. [CrossRef] 46. AlQattan, D.; Sepulveda, F. Towards sign language recognition using EEG-based motor imagery brain computer interface. In Proceedings of the 2017 5th International Winter Conference on Brain-Computer Interface (BCI), Gangwon, Korea, 9–11 January 2017; pp. 5–8. [CrossRef] 47. Amarasinghe, K.; Sivils, P.; Manic, M. EEG feature selection for thought driven robots using evolutionary Algorithms. In Proceed- ings of the 2016 9th International Conference on Human System Interactions (HSI), Portsmouth, UK, 6–8 July 2016; pp. 355–361. [CrossRef] 48. An, X.; Wei, J.; Liu, S.; Ming, N. A sLORETA study for gaze-independent BCI speller. In Proceedings of the 2017 39th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), Jeju Island, Korea, 11–15 July 2017; pp. 994–997. [CrossRef] 49. Anil, D.G.; Pelayo, P.; Mistry, K.S.; George, K. A tactile P300 based brain computer interface system for communication in iOS devices. In Proceedings of the 2018 IEEE International Instrumentation and Measurement Technology Conference (I2MTC), Houston, TX, USA, 14–17 May 2018; pp. 1–6. [CrossRef] 50. Arfaras, G.; Athanasiou, A.; Pandria, N.; Kavazidi, K.; Kartsidis, P.; Astaras, A.; Bamidis, P.D.; Niki, P.; Kyriaki, R.K.; Panagiotis, D.B. Visual Versus Kinesthetic Motor Imagery for BCI Control of Robotic Arms (Mercury 2.0). In Proceedings of the 2017 IEEE 30th International Symposium on Computer-Based Medical Systems (CBMS), Thessaloniki, Greece, 22–24 June 2017; pp. 440–445. [CrossRef] 51. Aricò, P.; Borghini, G.; Di Flumeri, G.; Colosimo, A.; Bonelli, S.; Golfetti, A.; Pozzi, S.; Imbert, J.-P.; Granger, G.; Benhacene, R.; et al. Adaptive Automation Triggered by EEG-Based Mental Workload Index: A Passive Brain-Computer Interface Application in Realistic Air Trafﬁc Control Environment. Front. Hum. Neurosci. 2016, 10, 539. [CrossRef] 52. Aricò, P.; Borghini, G.; Di Flumeri, G.; Sciaraffa, N.; Colosimo, A.; Babiloni, F. Passive BCI in Operational Environments: Insights, Recent Advances, and Future Trends. IEEE Trans. Biomed. Eng. 2017, 64, 1431–1436. [CrossRef] 53. Bai, O.; Lin, P.; Huang, D.; Fei, D.-Y.; Floeter, M.K. Towards a user-friendly brain–computer interface: Initial tests in ALS and PLS patients. Clin. Neurophysiol. 2010, 121, 1293–1303. [CrossRef] [PubMed] 54. Bhattacharyya, S.; Konar, A.; Tibarewala, D.N. Motor imagery, P300 and error-related EEG-based robot arm movement control for rehabilitation purpose. Med. Biol. Eng. Comput. 2014, 52, 1007–1017. [CrossRef] [PubMed] 55. Bhattacharyya, S.; Sengupta, A.; Chakraborti, T.; Banerjee, D.; Khasnobish, A.; Konar, A.; Tibarewala, D.N.; Janarthanan, R.; Bhattacharyya, S.; Sengupta, A.; et al. EEG controlled remote robotic system from motor imagery classiﬁcation. In Proceedings of the 2012 Third International Conference on Computing, Communication and Networking Technologies (ICCCNT’12), Karur, India, 26–28 July 2012; pp. 1–8. [CrossRef] 56. Boubakeur, M.R.; Wang, G.; Zhang, C.; Liu, K. EEG-Based Person Recognition Analysis and Criticism. In Proceedings of the 2017 IEEE International Conference on Big Knowledge (ICBK), Hefei, China, 9–10 August 2017; pp. 155–160. [CrossRef] 57. Brumberg, J.S.; Lorenz, S.D.; Galbraith, B.V.; Guenther, F.H. The unlock project: A Python-based framework for practical brain- computer interface communication “app” development. In Proceedings of the 2012 Annual International Conference of the IEEE Engineering in Medicine and Biology Society, San Diego, CA, USA, 28 August–1 September 2012; pp. 2505–2508. [CrossRef] 58. Brummer, N.B.; Rawson, J.A.; Grimm, M.W.; Tupper, P.; Miller, A.J.L.; Billings, C.J.; Jacobs, P.G. Electrode selection and other design considerations for a modular, portable single-channel EEG-augmented hearing aid. In Proceedings of the 2013 6th International IEEE/EMBS Conference on Neural Engineering (NER), San Diego, CA, USA, 6–8 November 2013; pp. 431–434. [CrossRef] 59. Bryan, M.; Green, J.; Chung, M.; Chang, L.; Scherer, R.; Smith, J.; Rao, R.P.N. An adaptive brain-computer interface for humanoid robot control. In Proceedings of the 2011 11th IEEE-RAS International Conference on Humanoid Robots, Bled, Slovenia, 26–28 October 2011; pp. 199–204. [CrossRef] 60. Chacko, S.G.; Tayade, P.; Kaur, S.; Sharma, R. Creation of a high resolution EEG based Brain Computer Interface for classifying motor imagery of daily life activities. In Proceedings of the 2019 7th International Winter Conference on Brain-Computer Interface (BCI), Gangwon, Korea, 18–20 February 2019; pp. 1–5. [CrossRef] 61. Chai, R.; Naik, G.R.; Nguyen, T.N.; Ling, S.H.; Tran, Y.; Craig, A.; Nguyen, H.T. Driver Fatigue Classiﬁcation With Independent Component by Entropy Rate Bound Minimization Analysis in an EEG-Based System. IEEE J. Biomed. Health Inform. 2017, 21, 715–724. [CrossRef] 62. Chakraborti, T.; Sengupta, A.; Banerjee, D.; Konar, A.; Bhattacharyya, S.; Khasnobish, A.; Janarthanan, R. Implementation of EEG based control of remote robotic systems. In Proceedings of the 2011 International Conference on Recent Trends in Information Systems, Kolkata, India, 21–23 December 2011; pp. 203–208. [CrossRef] 63. Chen, J.X.; Mao, Z.J.; Yao, W.X.; Huang, Y.F. EEG-based biometric identiﬁcation with convolutional neural network. Multimed. Tools Appl. 2019, 79, 10655–10675. [CrossRef] 64. Chen, S.-A.; Chen, C.-H.; Lin, J.-W.; Ko, L.-W.; Lin, C.-T. Gaming controlling via brain-computer interface using multiple physiological signals. In Proceedings of the 2014 IEEE International Conference on Systems, Man, and Cybernetics (SMC), San Diego, CA, USA, 5–8 October 2014; pp. 3156–3159. [CrossRef]

<!-- page 37 -->

Sensors 2022, 22, 3331 37 of 44

65. Chennu, S.; Alsufyani, A.; Filetti, M.; Owen, A.M.; Bowman, H. The cost of space independence in P300-BCI spellers. J. Neuroeng. Rehabil. 2013, 10, 82. [CrossRef] 66. Chiesi, M.; Guermandi, M.; Placati, S.; Scarselli, E.F.; Guerrieri, R. Creamino: A Cost-Effective, Open-Source EEG-Based BCI System. IEEE Trans. Biomed. Eng. 2018, 66, 900–909. [CrossRef] [PubMed] 67. Chowdhury, A.; Raza, H.; Dutta, A.; Prasad, G. EEG-EMG based Hybrid Brain Computer Interface for Triggering Hand Exoskeleton for Neuro-Rehabilitation. In Proceedings of the Advances in Robotics, New Delhi, India, 28 June–2 July 2017; pp. 1–6. [CrossRef] 68. Chumerin, N.; Manyakov, N.; Combaz, A.; Suykens, J.; Yazicioglu, R.F.; Torfs, T.; Merken, P.; Neves, H.; Van Hoof, C.; Van Hulle, M. P300 Detection Based on Feature Extraction in On-line Brain-Computer Interface. In Proceedings of the KI 2009: Advances in Artiﬁcial Intelligence, Berlin/Heidelberg, Germany, 15–18 September 2009; pp. 339–346. [CrossRef] 69. Chumerin, N.; Manyakov, N.V.; Combaz, A.; Suykens, J.; Van Hulle, M.M. An application of feature selection to on-line P300 detection in brain-computer interface. In Proceedings of the 2009 IEEE International Workshop on Machine Learning for Signal Processing, Southampton, UK, 22–25 September 2013; pp. 1–6. [CrossRef] 70. Cincotti, F.; Pichiorri, F.; Arico, P.; Aloise, F.; Leotta, F.; Fallani, F.D.V.; Millan, J.D.R.; Molinari, M.; Mattia, D. EEG-based Brain-Computer Interface to support post-stroke motor rehabilitation of the upper limb. In Proceedings of the 2012 Annual International Conference of the IEEE Engineering in Medicine and Biology Society, San Diego, CA, USA, 28 August–1 September 2012; pp. 4112–4115. [CrossRef] 71. Cincotti, F.; Quitadamo, L.R.; Aloise, F.; Bianchi, L.; Babiloni, F.; Mattia, D. Interacting with the Environment through Non-invasive Brain-Computer Interfaces. In Universal Access in Human-Computer Interaction. Intelligent and Ubiquitous Interaction Environments; Springer: Berlin/Heidelberg, Germany, 2009; pp. 483–492. [CrossRef] 72. Cui, Y.; Wu, D. EEG-Based Driver Drowsiness Estimation Using Convolutional Neural Networks. In Neural Information Processing; Springer: Cham, Switzerland, 2017; pp. 822–832. [CrossRef] 73. Djamal, E.C.; Lodaya, P. EEG based emotion monitoring using wavelet and learning vector quantization. In Proceedings of the 2017 4th International Conference on Electrical Engineering, Computer Science and Informatics (EECSI), IEEE, Yogyakarta, Indonesia, 19–21 September 2017; pp. 1–6. [CrossRef] 74. Dodia, S.; Edla, D.R.; Bablani, A.; Ramesh, D.; Kuppili, V. An efﬁcient EEG based deceit identiﬁcation test using wavelet packet transform and linear discriminant analysis. J. Neurosci. Methods 2019, 314, 31–40. [CrossRef] 75. Dongwei, C.; Fang, W.; Zhen, W.; Haifang, L.; Junjie, C. Eeg-based emotion recognition with brain network using indepen- dent components analysis and granger causality. In Proceedings of the 2013 International Conference on Computer Medical Applications (ICCMA), IEEE, Sousse, Tunisia, 20–22 January 2013; pp. 1–6. [CrossRef] 76. Duvinage, M.; Castermans, T.; Dutoit, T.; Petieau, M.; Hoellinger, T.; De Saedeleer, C.; Seetharaman, K.; Cheron, G. A P300-based Quantitative Comparison between the Emotiv Epoc Headset and a Medical EEG Device. Biomed. Eng. 2012, 765, 2012–2764. [CrossRef] 77. Ehrlich, S.; Guan, C.; Cheng, G. A closed-loop brain-computer music interface for continuous affective interaction. In Proceedings of the 2017 International Conference on Orange Technologies (ICOT), IEEE, Singapore, 8–10 December 2017; pp. 176–179. [CrossRef] 78. Fatima, M.; Amjad, N.; Shaﬁque, M. Analysis of Electroencephalographic Signal Acquisition and Processing for Use in Robotic Arm Movement. In Proceedings of the 2018 IEEE-EMBS Conference on Biomedical Engineering and Sciences (IECBES), IEEE, Sarawak, Malaysia, 3–6 December 2018; pp. 117–121. [CrossRef] 79. Fatima, M.; Shaﬁque, M.; Khan, Z.H. Towards a low cost Brain-computer Interface for real time control of a 2 DOF robotic arm. In Proceedings of the 2015 International Conference on Emerging Technologies (ICET), IEEE, Peshawa, Pakistan, 19–20 December 2015; pp. 1–6. [CrossRef] 80. Fazli, S.; Dahne, S.; Samek, W.; Bieszmann, F.; Mueller, K.-R. Learning From More Than One Data Source: Data Fusion Techniques for Sensorimotor Rhythm-Based Brain–Computer Interfaces. Proc. IEEE 2015, 103, 891–906. [CrossRef] 81. Finke, A.; Hachmeister, N.; Riechmann, H.; Ritter, H. Thought-controlled robots-Systems, studies and future challenges. In Proceedings of the 2013 IEEE International Conference on Robotics and Automation, IEEE, Karlsruhe, Germany, 6–10 May 2013; pp. 3403–3408. [CrossRef] 82. Folgieri, R.; Zampolini, R. BCI Promises in Emotional Involvement in Music and Games. Comput. Entertain. 2014, 12, 1–10. [CrossRef] 83. Frank, M.; Hwu, T.; Jain, S.; Knight, R.T.; Martinovic, I.; Mittal, P.; Perito, D.; Sluganovic, I.; Song, D. Using EEG-Based BCI Devices to Subliminally Probe for Private Information. In Proceedings of the 2017 on Workshop on Privacy in the Electronic Society, Dallas, TX, USA, 30 October 2017; pp. 133–136. [CrossRef] 84. Friedman, N.; Fekete, T.; Gal, K.; Shriki, O. EEG-Based Prediction of Cognitive Load in Intelligence Tests. Front. Hum. Neurosci. 2019, 13, 191. [CrossRef] [PubMed] 85. García-Salinas, J.S.; Villaseñor-Pineda, L.; Reyes-García, C.A.; Torres-Garcia, A.A. Transfer learning in imagined speech EEG-based BCIs. Biomed. Signal Process. Control 2019, 50, 151–157. [CrossRef] 86. González-Castañeda, E.F.; Torres-García, A.A.; Reyes-García, C.A.; Villasenor-Pineda, L. Soniﬁcation and textiﬁcation: Proposing methods for classifying unspoken words from EEG signals. Biomed. Signal Process. Control 2017, 37, 82–91. [CrossRef]

<!-- page 38 -->

Sensors 2022, 22, 3331 38 of 44

87. Gorjup, G.; Vrabiˇc, R.; Stoyanov, S.P.; Andersen, M.; Manoonpong, P. Development of a Real-Time Motor-Imagery-Based EEG Brain-Machine Interface. In Proceedings of the International Conference on Neural Information Processing, Siem Reap, Cambodia, 13–16 December 2018; Springer: Cham, Switzerland, 2018; pp. 610–622. [CrossRef] 88. Gu, J.-N.; Lu, H.-T.; Lu, B.-L. An integrated Gaussian mixture model to estimate vigilance level based on EEG recordings. Neurocomputing 2013, 129, 107–113. [CrossRef] 89. Guger, C.; Daban, S.; Sellers, E.; Holzner, C.; Krausz, G.; Carabalona, R.; Gramatica, F.; Edlinger, G. How many people are able to control a P300-based brain–computer interface (BCI)? Neurosci. Lett. 2009, 462, 94–98. [CrossRef] 90. Guger, C.; Holzner, C.; Groenegress, C.; Edlinger, G.; Slater, M. Brain Computer Interface for Virtual Reality Control. Cyberpsychol- ogy Behav. 2009, 12, 84. 91. Haghighi, M.; Akcakaya, M.; Orhan, U.; Erdogmus, D.; Oken, B.; Fried-Oken, M.; Haghighi, M.; Akçakaya, M. Initial assessment of artifact ﬁltering for RSVP Keyboard. In Proceedings of the 2013 IEEE Signal Processing in Medicine and Biology Symposium (SPMB), Brooklyn, NY, USA, 7 December 2013; pp. 1–5. [CrossRef] 92. Han, C.-H.; Im, C.-H. EEG-based brain-computer interface for real-time communication of patients in completely locked-in state. In Proceedings of the 2018 6th International Conference on Brain-Computer Interface (BCI), Gangwon, Korea, 15–17 January 2018; pp. 1–2. [CrossRef] 93. Heger, D.; Putze, F.; Schultz, T. Online Recognition of Facial Actions for Natural EEG-Based BCI Applications. In International Conference on Affective Computing and Intelligent Interaction, Memphis, TN, USA, 9–12 October 2011; Springer: Berlin, Germany, 2011; pp. 436–446. [CrossRef] 94. Hsieh, Z.-H.; Fang, W.-C.; Jung, T.-P. A brain-computer interface with real-time independent component analysis for biomedical applications. In Proceedings of the 2012 IEEE International Conference on Consumer Electronics (ICCE), IEEE, Las Vegas, NV, USA, 12–15 January 2012; pp. 339–340. [CrossRef] 95. Huang, D.; Zhang, S.; Zhang, Y. EEG-based emotion recognition using empirical wavelet transform. In Proceedings of the 2017 4th International Conference on Systems and Informatics (ICSAI), IEEE, Hangzhou, China, 11–13 November 2017; pp. 1444–1449. [CrossRef] 96. Huang, D.; Zhang, H.; Ang, K.; Guan, C.; Pan, Y.; Wang, C.; Yu, J. Fast emotion detection from EEG using asymmetric spatial ﬁltering. In Proceedings of the 2012 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Kyoto, Japan, 25–30 March 2012; pp. 589–592. [CrossRef] 97. Huster, R.J.; Mokom, Z.N.; Enriquez-Geppert, S.; Herrmann, C.S. Brain–computer interfaces for EEG neurofeedback: Peculiarities and solutions. Int. J. Psychophysiol. 2014, 91, 36–45. [CrossRef] 98. Hwang, H.-J.; Kim, K.-H.; Jung, Y.-J.; Kim, D.-W.; Lee, Y.-H.; Im, C.-H. An EEG-based real-time cortical functional connectivity imaging system. Med Biol. Eng. Comput. 2011, 49, 985–995. [CrossRef] 99. Hwang, H.-J.; Kim, S.; Choi, S.; Im, C.-H. EEG-Based Brain-Computer Interfaces: A Thorough Literature Survey. Int. J. Hum.-Comput. Interact. 2013, 29, 814–826. [CrossRef] 100. Ibáñez, J.; Serrano, J.; del Castillo, M.; Gallego, J.; Rocon, E. Online detector of movement intention based on EEG—Application in tremor patients. Biomed. Signal Process. Control 2013, 8, 822–829. [CrossRef] 101. Irimia, D.; Ortner, R.; Krausz, G.; Guger, C.; Poboroniuc, M. BCI Application in Robotics Control. IFAC Proc. Vol. 2012, 45, 1869–1874. [CrossRef] 102. Iturrate, I.; Montesano, L.; Minguez, J. Shared-control brain-computer interface for a two dimensional reaching task using EEG error-related potentials. In Proceedings of the 2013 35th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), IEEE, Osaka, Japan, 3–7 July 2013; pp. 5258–5262. [CrossRef] 103. Jayabhavani, G.N.; Raajan, N.R.; Abirami, J. A speller based mechanized messenger for smart phones using brain mobile interface (BMI). In Proceedings of the 2013 International Conference on Emerging Trends in VLSI, Embedded System, Nano Electronics and Telecommunication System (ICEVENT), Tiruvannamalai, India, 7–9 January 2013; pp. 1–5. [CrossRef] 104. Ji, H.; Li, J.; Cao, L.; Wang, D. A EEG-Based Brain Computer Interface System towards Applicable Vigilance Monitoring. In Foundations of Intelligent Systems; Springer: Berlin/Heidelberg, Germany, 2012; pp. 743–749. [CrossRef] 105. Kapeller, C.; Hintermüller, C.; Guger, C. Augmented control of an avatar using an SSVEP based BCI. In Proceedings of the 3rd augmented human international conference, Megève, France, 8–9 March 2012; pp. 1–2. [CrossRef] 106. Karácsony, T.; Hansen, J.P.; Iversen, H.K.; Puthusserypady, S. Brain Computer Interface for Neuro-rehabilitation With Deep Learning Classiﬁcation and Virtual Reality Feedback. In Proceedings of the 10th Augmented Human International Conference 2019, Reims, France, 11–12 March 2019; ACM: New York, NY, USA, 2019. [CrossRef] 107. Kartsch, V.; Benatti, S.; Rossi, D.; Benini, L. A wearable EEG-based drowsiness detection system with blink duration and alpha waves analysis. In Proceedings of the 2017 8th International IEEE/EMBS Conference on Neural Engineering (NER), IEEE, Shanghai, China, 25–28 May 2017; pp. 251–254. [CrossRef] 108. Katona, J.; K˝ovári, A. The Evaluation of BCI and PEBL-based Attention Tests. Acta Polytech. Hung. 2018, 15, 225–249. [CrossRef] 109. Kaushik, P.; Gupta, A.; Roy, P.P.; Dogra, D.P. EEG-Based Age and Gender Prediction Using Deep BLSTM-LSTM Network Model. IEEE Sens. J. 2018, 19, 2634–2641. [CrossRef] 110. Kerous, B.; Skola, F.; Liarokapis, F. EEG-based BCI and video games: A progress report. Virtual Real. 2017, 22, 119–135. [CrossRef]

<!-- page 39 -->

Sensors 2022, 22, 3331 39 of 44

111. Kim, K.-T.; Lee, S.-W. Towards an EEG-based intelligent wheelchair driving system with vibro-tactile stimuli. In Proceedings of the 2016 IEEE International Conference on Systems, Man, and Cybernetics (SMC), IEEE, Budapest, Hungary, 9–12 October 2016; pp. 002382–002385. [CrossRef] 112. Kim, M.; Kim, B.H.; Jo, S. Quantitative Evaluation of a Low-Cost Noninvasive Hybrid Interface Based on EEG and Eye Movement. IEEE Trans. Neural Syst. Rehabil. Eng. 2014, 23, 159–168. [CrossRef] 113. Kim, Y.-J.; Kwak, N.-S.; Lee, S.-W. Classiﬁcation of motor imagery for Ear-EEG based brain-computer interface. In Proceedings of the 2018 6th International Conference on Brain-Computer Interface (BCI), IEEE, Gangwon, Korea, 15–17 January 2018; pp. 1–2. [CrossRef] 114. Kinney-Lang, E.; Auyeung, B.; Escudero, J. Expanding the (kaleido)scope: Exploring current literature trends for translating electroencephalography (EEG) based brain–computer interfaces for motor rehabilitation in children. J. Neural Eng. 2016, 13, 061002. [CrossRef] 115. Kovacevic, N.; Ritter, P.; Tays, W.; Moreno, S.; McIntosh, A. ‘My Virtual Dream’: Collective Neurofeedback in an Immersive Art Environment. PLoS ONE 2015, 10, e0130129. [CrossRef] 116. Lan, Z.; Liu, Y.; Sourina, O.; Wang, L. Real-time EEG-based user’s valence monitoring. In Proceedings of the 2015 10th International Conference on Information, Communications and Signal Processing (ICICS), IEEE, Singapore, 2–4 December 2015; pp. 1–5. [CrossRef] 117. Landavazo, B.; Nandikolla, V.K. Brain-Computer Interface Application in Robotic Gripper Control. In Proceedings of thepresented at the ASME 2018 International Mechanical Engineering Congress and Exposition, Pittsburgh, PA, USA, 9–15 November 2018. [CrossRef] 118. Lee, Y.-C.; Lin, W.-C.; Cherng, F.-Y.; Ko, L.-W. A Visual Attention Monitor Based on Steady-State Visual Evoked Potential. IEEE Trans. Neural Syst. Rehabil. Eng. 2015, 24, 399–408. [CrossRef] 119. Li, J.; Ji, H.; Cao, L.; Gu, R.; Xia, B.; Huang, Y. Wheelchair Control Based on Multimodal Brain-Computer Interfaces. In Neural Information Processing; Springer: Berlin/Heidelberg, Germany, 2013; pp. 434–441. [CrossRef] 120. Li, J.; Liang, J.; Zhao, Q.; Li, J.; Hong, K.; Zhang, L. Design of Assistive Wheelchair System Directly Steered by Human Thoughts. Int. J. Neural Syst. 2013, 23, 1350013. [CrossRef] 121. Li, M.; Zhang, Y.; Zhang, H.; Hu, H.S. An EEG Based Control System for Intelligent Wheelchair. Appl. Mech. Mater. 2013, 300–301, 1540–1545. [CrossRef] 122. Li, S.; Leider, A.; Qiu, M.; Gai, K.; Liu, M. Brain-Based Computer Interfaces in Virtual Reality. In Proceedings of the 2017 IEEE 4th International Conference on Cyber Security and Cloud Computing (CSCloud), IEEE, New York, NY, USA, 26–28 June 2017; pp. 300–305. [CrossRef] 123. Li, Y.; Yu, T. EEG-based hybrid BCIs and their applications. In Proceedings of the 3rd International Winter Conference on Brain-Computer Interface, Gangwon-Do, Korea, 12–14 January 2015; pp. 1–4. [CrossRef] 124. Liao, L.-D.; Chen, C.-Y.; Wang, I.-J.; Chen, S.-F.; Li, S.-Y.; Chen, B.-W.; Chang, J.-Y.; Lin, C.-T. Gaming control using a wearable and wireless EEG-based brain-computer interface device with novel dry foam-based sensors. J. Neuroeng. Rehabil. 2012, 9, 5. [CrossRef] [PubMed] 125. Liao, L.-D.; Wang, I.-J.; Chang, C.-J.; Lin, B.-S.; Lin, C.-T.; Tseng, K.C. Human cognitive application by using Wearable Mobile Brain Computer Interface. In Proceedings of the TENCON 2010-2010 IEEE Region 10 Conference, IEEE, Fukuoka, Japan, 21–24 November 2010; pp. 346–351. [CrossRef] 126. Lin, C.-T.; Lin, F.-C.; Chen, S.-A.; Lu, S.-W.; Chen, T.-C.; Ko, L.-W. EEG-based Brain-computer Interface for Smart Living Environment Auto-adjustment. J. Med. Biol. Eng. 2010, 30, 237–245. [CrossRef] 127. Lin, J.S.; Huang, S.M. An FPGA-Based Brain-Computer Interface for Wireless Electric Wheelchairs. Appl. Mech. Mater. 2013, 284–287, 1616–1621. [CrossRef] 128. Lin, J.-S.; Yang, W.-C. Wireless brain-computer interface for electric wheelchairs with EEG and eye-blinking signals. Int. J. Innov. Comput. Inf. Control 2012, 8, 6011–6024. 129. Lin, Y.-P.; Wang, Y.; Wei, C.-S.; Jung, T.-P. A Mobile Brain-Computer Interface for Freely Moving Humans. In Human-Computer Interaction. Towards Intelligent and Implicit Interaction; Springer: Berlin/Heidelberg, Germany, 2013; pp. 448–453. [CrossRef] 130. Liu, D.; Chen, W.; Lee, K.; Chavarriaga, R.; Bouri, M.; Pei, Z.; Millán, J.D.R. Brain-actuated gait trainer with visual and proprioceptive feedback. J. Neural Eng. 2017, 14, 056017. [CrossRef] 131. Liu, D.; Chen, W.; Lee, K.; Chavarriaga, R.; Iwane, F.; Bouri, M.; Pei, Z.; Millan, J.D.R. EEG-Based Lower-Limb Movement Onset Decoding: Continuous Classiﬁcation and Asynchronous Detection. IEEE Trans. Neural Syst. Rehabil. Eng. 2018, 26, 1626–1635. [CrossRef] 132. Liu, Y.; Ayaz, H.; Shewokis, P.A. Multisubject “Learning” for Mental Workload Classiﬁcation Using Concurrent EEG, fNIRS, and Physiological Measures. Front. Hum. Neurosci. 2017, 11, 389. [CrossRef] 133. Liu, Y.; Sourina, O.; Nguyen, M.K. Real-Time EEG-Based Human Emotion Recognition and Visualization. In Proceedings of the 2010 International Conference on Cyberworlds, Singapore, 20–22 October 2010; pp. 262–269. [CrossRef] 134. Liu, Y.-T.; Lin, Y.-Y.; Wu, S.-L.; Chuang, C.-H.; Lin, C.-T. Brain Dynamics in Predicting Driving Fatigue Using a Recurrent Self-Evolving Fuzzy Neural Network. IEEE Trans. Neural Networks Learn. Syst. 2015, 27, 347–360. [CrossRef] 135. Lopez-Gordo, M.A.; Ron-Angevin, R.; Pelayo, F. Authentication of Brain-Computer Interface Users in Network Applications. In Proceedings of the Advances in Computational Intelligence, Palma de Mallorca, Spain, 10–12 June 2015; pp. 124–132. [CrossRef]

<!-- page 40 -->

Sensors 2022, 22, 3331 40 of 44

136. Lotte, F.; Fujisawa, J.; Touyama, H.; Ito, R.; Hirose, M.; Lecuyer, A. Towards ambulatory brain-computer Interfaces: A Pilot Study with P300 Signals’, Book Ambul. Brain-Comput. Interfaces Pilot Study P300 Signals. In Proceedings of the International Conference on Advances in Computer Enterntainment Technology, Athens, Greece, 29–31 October 2009. [CrossRef] 137. Lu, Y.; Hu, Y.; Liu, R.; Wang, H.; Asama, H.; Duan, F. The design of simulation vehicle system controlled by multichannel EEG based on imaginary movements. In Proceedings of the 2016 35th Chinese Control Conference (CCC), IEEE, Chengdu, China, 27 July 2016; pp. 4976–4981. [CrossRef] 138. Ma, T.; Li, H.; Deng, L.; Yang, H.; Lv, X.; Li, P.; Li, F.; Zhang, R.; Liu, T.; Yao, D.; et al. The hybrid BCI system for movement control by combining motor imagery and moving onset visual evoked potential. J. Neural Eng. 2017, 14, 026015. [CrossRef] 139. Mahajan, R.; Bansal, D. Real Time EEG Based Cognitive Brain Computer Interface for Control Applications via Arduino Interfacing. Procedia Comput. Sci. 2017, 115, 812–820. [CrossRef] 140. Maiorana, E.; La Rocca, D.; Campisi, P. EEG-based biometric recognition using EigenBrains. In Proceedings of the 2015 IEEE International Conference on Multimedia Expo Workshops (ICMEW), IEEE, Turin, Italy, 29 June–3 July 2015; pp. 1–6. [CrossRef] 141. Mandel, C.; Luth, T.; Laue, T.; Rofer, T.; Graser, A.; Krieg-Bruckner, B. Navigating a smart wheelchair with a brain-computer interface interpreting steady-state visual evoked potentials. In Proceedings of the 2009 IEEE/RSJ International Conference on Intelligent Robots and Systems, IEEE, Louis, MO, USA, 10–15 October 2009; pp. 1118–1125. [CrossRef] 142. Manolova, A.; Tsenov, G.; Lazarova, V.; Neshov, N. Combined EEG and EMG fatigue measurement framework with application to hybrid brain-computer interface. In Proceedings of the 2016 IEEE International Black Sea Conference on Communications and Networking (BlackSeaCom), IEEE, Bucharest, Romania, 6–9 June 2016; pp. 1–5. [CrossRef] 143. Mao, Z.; Yao, W.X.; Huang, Y. EEG-based biometric identiﬁcation with deep learning. In Proceedings of the 2017 8th International IEEE/EMBS Conference on Neural Engineering (NER), IEEE, Shanghai, China, 25–28 May 2017; pp. 609–612. [CrossRef] 144. Marchesotti, S.; Martuzzi, R.; Schurger, A.; Blefari, M.L.; Millan, J.D.R.; Bleuler, H.; Blanke, O. Cortical and subcortical mechanisms of brain-machine interfaces. Hum. Brain Mapp. 2017, 38, 2971–2989. [CrossRef] 145. McFarland, D.; Wolpaw, J. EEG-based brain–computer interfaces. Curr. Opin. Biomed. Eng. 2017, 4, 194–200. [CrossRef] 146. Melinšˇcak, F.; Jerbi´c, A.B.; Cifrek, M. A P300-based brain-computer interface: Towards a simpler approach. In Proceedings of the 2013 36th International Convention on Information and Communication Technology, Electronics and Microelectronics (MIPRO), IEEE, Opatija, Croatia, 20–24 May 2013; pp. 1049–1052. 147. Melinscak, F.; Montesano, L.; Minguez, J. Asynchronous detection of kinesthetic attention during mobilization of lower limbs using EEG measurements. J. Neural Eng. 2016, 13, 016018. [CrossRef] 148. Mikołajewska, E.; Mikołajewski, D. Non-invasive EEG-based brain-computer interfaces in patients with disorders of consciousness. Mil. Med Res. 2014, 1, 14. [CrossRef] 149. Millán, J.D.R.; Rupp, R.; Mueller-Putz, G.; Murray-Smith, R.; Giugliemma, C.; Tangermann, M.; Vidaurre, C.; Cincotti, F.; Kubler, A.; Leeb, R.; et al. Combining brain-computer interfaces and assistive technologies: State-of-the-art and challenges. Front. Neurosci. 2010, 4, 161. [CrossRef] 150. Mohammadpour, M.; Mozaffari, S. Classiﬁcation of EEG-based attention for brain computer interface. In Proceedings of the 2017 3rd Iranian Conference on Intelligent Systems and Signal Processing (ICSPIS), Shahrood, Iran, 20–21 December 2017; pp. 34–37. [CrossRef] 151. Mohanchandra, K. Criminal forensic: An application to EEG. In Proceedings of the 2015 Recent and Emerging trends in Computer and Computational Sciences (RETCOMP), IEEE, Bangalore, India, 8–10 January 2015; pp. 18–21. [CrossRef] 152. Molina, G.G.; Tsoneva, T.; Nijholt, A. Emotional brain-computer interfaces. In Proceedings of the 2009 3rd International Conference on Affective Computing and Intelligent Interaction and Workshops, IEEE, Amsterdam, The Netherlands, 10–12 September 2009; pp. 1–9. [CrossRef] 153. Application of a brain-computer interface for person authentication using EEG responses to photo stimuli. J. Integr. Neurosci. 2018, 17, 53–60. [CrossRef] 154. Müller-Putz, G.R.; Rupp, R. Achievements and challenges of translational research in non-invasive SMR-BCI-controlled upper extremity neuroprosthesis in spinal cord injury. In Proceedings of the 2015 7th International IEEE/EMBS Conference on Neural Engineering (NER), Montpellier, France, 22–24 April 2015; pp. 158–161. [CrossRef] 155. Murphy, D.P.; Bai, O.; Gorgey, A.S.; Fox, J.; Lovegreen, W.T.; Burkhardt, B.W.; Atri, R.; Marquez, J.S.; Li, Q.; Fei, D.-Y. Electroencephalogram-Based Brain–Computer Interface and Lower-Limb Prosthesis Control: A Case Study. Front. Neurol. 2017, 8, 696. [CrossRef] 156. Pan, J.; Xie, Q.; Huang, H.; He, Y.; Sun, Y.; Yu, R.; Li, Y. Emotion-Related Consciousness Detection in Patients With Disorders of Consciousness Through an EEG-Based BCI System. Front. Hum. Neurosci. 2018, 12, 198. [CrossRef] 157. Park, J.; Woo, I.; Park, S. Application of EEG for multimodal human-machine interface. In Proceedings of the 2012 12th International Conference on Control, Automation and Systems, Jeju Island, Korea, 17–21 October 2012; pp. 1869–1873. 158. Penaloza, C.; Hernandez-Carmona, D.; Nishio, S. Towards Intelligent Brain-Controlled Body Augmentation Robotic Limbs. In Proceedings of the 2018 IEEE International Conference on Systems, Man, and Cybernetics (SMC), Miyazaki, Japan, 7–10 October 2018; pp. 1011–1015. [CrossRef] 159. Penaloza, C.I.; Alimardani, M.; Nishio, S. Android Feedback-Based Training Modulates Sensorimotor Rhythms During Motor Imagery. IEEE Trans. Neural Syst. Rehabil. Eng. 2018, 26, 666–674. [CrossRef]

<!-- page 41 -->

Sensors 2022, 22, 3331 41 of 44

160. Prashant, P.; Joshi, A.; Gandhi, V. Brain computer interface: A review. In Proceedings of the 2015 5th Nirma University International Conference on Engineering (NUiCONE), Ahmedabad, India, 26–28 November 2015; pp. 1–6. [CrossRef] 161. Punsawad, Y.; Wongsawat, Y. Self-paced Emotional Imagery-Based Brain Computer Interface System. In Proceedings of the 6th International Conference on the Development of Biomedical Engineering in Vietnam (BME6), Singapore, 24 September 2017; pp. 567–571. [CrossRef] 162. Qidwai, U.A.; Shakir, M. Fuzzy Classiﬁcation-Based Control of Wheelchair Using EEG Data to Assist People with Disabilities. In Neural Information Processing; Springer: Berlin/Heidelberg, Germany, 2012; pp. 458–467. [CrossRef] 163. Qin, Z.; Xu, Y.; Shu, X.; Hua, L.; Sheng, X.; Zhu, X. eConHand: A Wearable Brain-Computer Interface System for Stroke Rehabilitation. In Proceedings of the 2019 9th International IEEE/EMBS Conference on Neural Engineering (NER), IEEE, San Francisco, CA, USA, 20–23 March 2019; pp. 734–737. [CrossRef] 164. Ramakuri, S.K.; Chakraborty, C.; Ghosh, S.; Gupta, B. Performance analysis of eye-state charecterization through single electrode EEG device for medical application. In Proceedings of the 2017 Global Wireless Summit (GWS), IEEE, Cape Town, South Africa, 15–18 October 2017; pp. 1–6. [CrossRef] 165. Risangtuni, A.G.; Suprijanto; Widyotriatmo, A. Towards online application of wireless EEG-based open platform Brain Com- puter Interface. In Proceedings of the 2012 IEEE Conference on Control, Systems Industrial Informatics, Bandung, Indonesia, 23–26 September 2012; pp. 141–144. [CrossRef] 166. Rodriguez, R.J. Electroencephalogram (EEG) based authentication leveraging visual evoked potentials (VEP) resulting from exposure to emotionally signiﬁcant images. In Proceedings of the 2016 IEEE Symposium on Technologies for Homeland Security (HST), Waltham, MA, USA, 10–12 May 2016; pp. 1–6. [CrossRef] 167. Rutkowski, T.; Tanaka, T.; Zhao, Q.; Cichocki, A. Spatial Auditory BCI/BMI Paradigm-Multichannel EMD Approach to Brain Responses Estimation. In Proceedings of the APSIPA annual summit and conference, Auckland, New Zealand, 7–10 December 2010; pp. 197–202. 168. Sanchez, A.M.; Gaume, A.; Dreyfus, G.; Vialatte, F.-B. A cognitive brain-computer interface prototype for the continuous monitoring of visual working memory load. In Proceedings of the 2015 IEEE 25th International Workshop on Machine Learning for Signal Processing (MLSP), Boston, MA, USA, 17–20 September 2015; pp. 1–5. [CrossRef] 169. Scherer, R.; Müller-Putz, G.R.; Pfurtscheller, G. Chapter 9 Flexibility and Practicality. Int. Rev. Neurobiol. 2009, 86, 119–131. [CrossRef] 170. Seoane, L.F.; Gabler, S.; Blankertz, B. Images from the mind: BCI image evolution based on rapid serial visual presentation of polygon primitives. Brain-Comput. Interfac. 2015, 2, 40–56. [CrossRef] 171. Sethi, C.; Dabas, H.; Dua, C.; Dalawat, M.; Sethia, D. EEG-Based Attention Feedback to Improve Focus in E-Learning. In Proceedings of the 2018 2nd International Conference on Computer Science and Artiﬁcial Intelligence, Shenzhen, China, 8–10 December 2018; pp. 321–326. [CrossRef] 172. Shakir, M.; Malik, A.S.; Kamel, N.; Qidwai, U. Detection of partial seizure: An application of fuzzy rule system for wearable ambulatory systems. In Proceedings of the 2014 5th International Conference on Intelligent and Advanced Systems (ICIAS), Kuala Lumpur, Malaysia, 3–5 June 2014; pp. 1–5. [CrossRef] 173. Shi, M.-H.; Zhou, C.-L.; Xie, J.; Li, S.-Z.; Hong, Q.-Y.; Jiang, M.; Chao, F.; Ren, W.-F.; Liu, X.-Q.; Zhou, D.-J.; et al. Electroencephalogram-based brain-computer interface for the Chinese spelling system: A survey. Front. Inf. Technol. Electron. Eng. 2018, 19, 423–436. [CrossRef] 174. Shin, S.; Jang, D.; Lee, J.J.; Jang, S.-J.; Kim, J.-H. MyMusicShufﬂer: Mood-based music recommendation with the practical usage of brainwave signals. In Proceedings of the 2014 IEEE International Conference on Consumer Electronics (ICCE), Las Vegas, NV, USA, 10–13 January 2014; pp. 355–356. [CrossRef] 175. Simonyi, D.; Kovács, T. Brain-Computer Interface-Based Feasibility of Entering Customer Code on Ticket Vending Machines. Interdiscip. Descr. Complex Syst. 2018, 16, 350–359. [CrossRef] 176. Sourina, O.; Liu, Y.; Hou, X.; Lim, W.L.; Mueller-Wittig, W.; Wang, L.; Konovessis, D.; Chen, C.-H.; Ang, W.T. Neuroscience Based Design: Fundamentals and Applications. In Proceedings of the 2016 International Conference on Cyberworlds (CW), Chongqing, China, 28–30 September 2016; pp. 250–257. [CrossRef] 177. Sourina, O.; Liu, Y.; Wang, Q.; Nguyen, M.K. EEG-Based Personalized Digital Experience. In Universal Access in Human-Computer Interaction. Users Diversity; Springer: Berlin/Heidelberg, Germany, 2011; pp. 591–599. [CrossRef] 178. Sourina, O.; Wang, Q.; Liu, Y.; Nguyen, M.K. A Real-time Fractal-based Brain State Recognition from EEG and its Applications. In Proceedings of the BIOSIGNALS 2011—International Conference on Bio-Inspired Systems and Signal Processing, Rome, Italy, 26–29 January 2011. 179. Spuler, M. A Brain-Computer Interface (BCI) system to use arbitrary Windows applications by directly controlling mouse and keyboard. In Proceedings of the 2015 37th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), Milan, Italy, 25–29 August 2015; pp. 1087–1090. [CrossRef] 180. Tan, H.G.; Kong, K.H.; Shee, C.Y.; Wang, C.C.; Guan, C.T.; Ang, W.T. Post-acute stroke patients use brain-computer interface to activate electrical stimulation. In Proceedings of the 2010 Annual International Conference of the IEEE Engineering in Medicine and Biology, Buenos Aires, Argentina, 31 August–4 September 2010; pp. 4234–4237. [CrossRef] 181. Thomas, K.P.; Vinod, A.P.; Guan, C. Design of an online EEG based neurofeedback game for enhancing attention and memory. Conf. Proc. Annu. Int. Conf. IEEE Eng. Med. Biol. Soc. IEEE Eng. Med. Biol. Soc. Annu. Conf. 2013, 2013, 433–436. [CrossRef]

<!-- page 42 -->

Sensors 2022, 22, 3331 42 of 44

182. Tian, S.; Wang, Y.; Dong, G.; Pei, W.; Chen, H. Mental Fatigue Estimation Using EEG in a Vigilance Task and Resting States. In Proceedings of the 2018 40th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC), Honolulu, HI, USA, 17–21 July 2018; pp. 1980–1983. [CrossRef] 183. Tseng, K.C.; Lin, B.-S.; Han, C.-M.; Wang, P.-S. Emotion recognition of EEG underlying favourite music by support vector machine. In Proceedings of the 2013 1st International Conference on Orange Technologies (ICOT), Tainan, Taiwan, 12–16 March 2013; pp. 155–158. [CrossRef] 184. Ullah, K.; Ali, M.; Rizwan, M.; Imran, M. Low-cost single-channel EEG based communication system for people with lock-in syndrome. In Proceedings of the 2011 IEEE 14th International Multitopic Conference, Karachi, Pakistan, 22–24 December 2011; pp. 120–125. [CrossRef] 185. Wang, C.; Phua, K.S.; Ang, K.K.; Guan, C.; Zhang, H.; Lin, R.; Chua, K.S.G.; Ang, B.T.; Kuah, C.W.K. A feasibility study of non-invasive motor-imagery BCI-based robotic rehabilitation for Stroke patients. In Proceedings of the 2009 4th International IEEE/EMBS Conference on Neural Engineering, Antalya, Turkey, 29 April–2 May 2009; pp. 271–274. [CrossRef] 186. Wang, Q.; Sourina, O.; Nguyen, M.K. EEG-Based “Serious” Games Design for Medical Applications. In Proceedings of the 2010 International Conference on Cyberworlds, Singapore, 20–22 October 2010; pp. 270–276. [CrossRef] 187. Wang, Q.; Sourina, O.; Nguyen, M.K. Fractal dimension based neurofeedback in serious games. Vis. Comput. 2011, 27, 299–309. [CrossRef] 188. Wang, Y.-K.; Chen, S.-A.; Lin, C.-T. An EEG-based brain–computer interface for dual task driving detection. Neurocomputing 2013, 129, 85–93. [CrossRef] 189. Wang, Y.; Hidaka, T.; Kawai, Y.; Okuda, J. Why Cannot Control Your Smartphones by Thinking? Hands-Free Information Control System Based on EEG. In Proceedings of the Innovation in Medicine and Healthcare 2015, Kyoto, Japan, 11–12 September 2015; pp. 553–564. [CrossRef] 190. Watanabe, H.; Tanaka, H.; Sakti, S.; Nakamura, S. Neural Oscillation-Based Classiﬁcation of Japanese Spoken Sentences During Speech Perception. IEICE Trans. Inf. Syst. 2019, 102, 383–391. [CrossRef] 191. Waytowich, N.; Henderson, A.; Krusienski, D.; Cox, D. Robot application of a brain computer interface to staubli TX40 robots-early stages. In Proceedings of the 2010 World Automation Congress, Kobe, Japan, 19–23 September 2010; pp. 1–6. 192. Wei, C.-S.; Lin, Y.-P.; Wang, Y.-T.; Jung, T.-P.; Bigdely-Shamlo, N.; Lin, C.-T. Selective Transfer Learning for EEG-Based Drowsiness Detection. In Proceedings of the 2015 IEEE International Conference on Systems, Man, and Cybernetics, Kowloon, China, 9–12 October 2015; pp. 3229–3232. 193. Wei, C.-S.; Wang, Y.-T.; Lin, C.-T.; Jung, T.-P. Toward Drowsiness Detection Using Non-hair-Bearing EEG-Based Brain-Computer Interfaces. IEEE Trans. Neural Syst. Rehabil. Eng. 2018, 26, 400–406. [CrossRef] 194. Wei, P. An virtual vehicle control game for online brain computer interface feedback training. In Proceedings of the 2010 IEEE International Conference on Mechatronics and Automation, Xi’an, China, 4–7 August 2010; pp. 1942–1944. [CrossRef] 195. Wolpaw, J.R. Brain–Computer Interface Research Comes of Age: Traditional Assumptions Meet Emerging Realities. J. Mot. Behav. 2010, 42, 351–353. [CrossRef] 196. Wriessnegger, S.C.; Hackhofer, D.; Muller-Putz, G.R. Classiﬁcation of unconscious like/dislike decisions: First results towards a novel application for BCI technology. Conf. Proc. Annu. Int. Conf. IEEE Eng. Med. Biol. Soc. IEEE Eng. Med. Biol. Soc. Annu. Conf. 2015, 2015, 2331–2334. [CrossRef] 197. Wu, S.-L.; Liu, Y.-T.; Chou, K.-P.; Lin, Y.-Y.; Lu, J.; Zhang, G.; Chuang, C.-H.; Lin, W.-C.; Lin, C.-T. A motor imagery based brain-computer interface system via swarm-optimized fuzzy integral and its application. In Proceedings of the 2016 IEEE International Conference on Fuzzy Systems (FUZZ-IEEE), Vancouver, BC, Canada, 24–29 July 2016; pp. 2495–2500. [CrossRef] 198. Xiao, J.; Lin, Q.; Yu, T.; Xie, Q.; Yu, R.; Li, Y. A BCI system for assisting visual ﬁxation assessment in behavioral evaluation of patients with disorders of consciousness. In Proceedings of the 2017 8th International IEEE/EMBS Conference on Neural Engineering (NER), Shanghai, China, 25–28 May 2017; pp. 399–402. [CrossRef] 199. Xiao, J.; Xie, Q.; He, Y.; Yu, T.; Lu, S.; Huang, N.; Yu, R.; Li, Y. An Auditory BCI System for Assisting CRS-R Behavioral Assessment in Patients with Disorders of Consciousness. Sci. Rep. 2016, 6, 32917. [CrossRef] [PubMed] 200. Xie, Y.; Li, X. A brain controlled wheelchair based on common spatial pattern. In Proceedings of the 2015 International Symposium on Bioelectronics and Bioinformatics (ISBB), Beijing, China, 14–17 October 2015; pp. 19–22. [CrossRef] 201. Xu, H.; Plataniotis, K.N. EEG-based affect states classiﬁcation using Deep Belief Networks. In Proceedings of the 2016 Digital Media Industry Academic Forum (DMIAF), Santorini, Greece, 4–6 July 2016; pp. 148–153. [CrossRef] 202. Xu, R.; Heilinger, A.; Murovec, N.; Spataro, R.; Cho, W.; Cao, F.; Allison, B.Z.; Guger, C. Effects of Repeating a Tactile Brain- Computer Interface on Patients with Disorder of Consciousness: A Hint of Recovery? In Proceedings of the 2019 9th International IEEE/EMBS Conference on Neural Engineering (NER), San Francisco, CA, USA, 20–23 March 2019; pp. 29–32. [CrossRef] 203. Yan, J.; Chen, S.; Deng, S. A EEG-based emotion recognition model with rhythm and time characteristics. Brain Inform. 2019, 6, 7. [CrossRef] [PubMed] 204. Yin, J.; Hu, J. Design and Implement of Pocket PC Game Based on Brain-Computer Interface. In Computing and Intelligent Systems; Springer: Berlin/Heidelberg, Germany, 2011; pp. 456–463. [CrossRef] 205. Yin, J.; Hu, J.; Mu, Z. Design and Implement of BCI System Based on Android Platform. In Information Engineering and Applications; Springer: London, UK, 2012; pp. 522–529. [CrossRef]

<!-- page 43 -->

Sensors 2022, 22, 3331 43 of 44

206. Yu, Y.; Liu, Y.; Yin, E.; Jiang, J.; Zhou, Z.; Hu, D. An Asynchronous Hybrid Spelling Approach Based on EEG–EOG Signals for Chinese Character Input. IEEE Trans. Neural Syst. Rehabil. Eng. 2019, 27, 1292–1302. [CrossRef] 207. Yue, J.; Zhou, Z.; Jiang, J.; Liu, Y.; Hu, D. Balancing a simulated inverted pendulum through motor imagery: An EEG-based real-time control paradigm. Neurosci. Lett. 2012, 524, 95–100. [CrossRef] 208. Zao, J.K.; Gan, T.-T.; You, C.-K.; Chung, C.-E.; Wang, Y.-T.; Méndez, S.J.R.; Mullen, T.; Yu, C.; Kothe, C.; Hsiao, C.-T.; et al. Pervasive brain monitoring and data sharing based on multi-tier distributed computing and linked data technology. Front. Hum. Neurosci. 2014, 8, 370. [CrossRef] [PubMed] 209. Zarjam, P.; Epps, J.; Lovell, N. Beyond Subjective Self-Rating: EEG Signal Classiﬁcation of Cognitive Workload. IEEE Trans. Auton. Ment. Dev. 2015, 7, 301–310. [CrossRef] 210. Zeng, H.; Yang, C.; Zhang, H.; Wu, Z.; Zhang, J.; Dai, G.; Babiloni, F.; Kong, W. A LightGBM-Based EEG Analysis Method for Driver Mental States Classiﬁcation. Comput. Intell. Neurosci. 2019, 2019, 3761203. [CrossRef] 211. Zhang, H.; Chavarriaga, R.; Khaliliardali, Z.; Gheorghe, L.A.; Iturrate, I.; Millan, J.D.R. EEG-based decoding of error-related brain activity in a real-world driving task. J. Neural Eng. 2015, 12, 066028. [CrossRef] 212. Zhang, X.; Yao, L.; Sheng, Q.Z.; Kanhere, S.S.; Gu, T.; Zhang, D. Converting Your Thoughts to Texts: Enabling Brain Typing via Deep Feature Learning of EEG Signals. In Proceedings of the 2018 IEEE International Conference on Pervasive Computing and Communications (PerCom) Converting, Athens, Greece, 19–23 March 2018; pp. 1–10. 213. Zhou, J.; Yao, J.; Deng, J.; Dewald, J.P. EEG-based classiﬁcation for elbow versus shoulder torque intentions involving stroke subjects. Comput. Biol. Med. 2009, 39, 443–452. [CrossRef] 214. Zhou, Z.; Li, P.; Liu, J.; Dong, W. A Novel Real-Time EEG Based Eye State Recognition System. In Communications and Networking; Springer: Cham, Switzerland, 2019; pp. 175–183. [CrossRef] 215. Zioga, P.; Chapman, P.; Ma, M.; Pollick, F. A Hypothesis of Brain-to-Brain Coupling in Interactive New Media Art and Games Using Brain-Computer Interfaces. In Serious Games; Springer: Cham, Switzerland, 2015; pp. 103–113. [CrossRef] 216. Zioga, P.; Pollick, F.; Ma, M.; Chapman, P.; Stefanov, K. “Enheduanna—A Manifesto of Falling” Live Brain-Computer Cinema Performance: Performer and Audience Participation, Cognition and Emotional Engagement Using Multi-Brain BCI Interaction. Front. Neurosci. 2018, 12, 191. [CrossRef] 217. Chaudhary, U.; Birbaumer, N.; Ramos-Murguialday, A. Brain–computer interfaces for communication and rehabilitation. Nat. Rev. Neurol. 2016, 12, 513–525. [CrossRef] 218. Dadebayev, D.; Goh, W.W.; Tan, E.X. EEG-based emotion recognition: Review of commercial EEG devices and machine learning techniques. J. King Saud Univ.-Comput. Inf. Sci. 2021. [CrossRef] 219. Larocco, J.; Le, M.D.; Paeng, D.-G. A Systemic Review of Available Low-Cost EEG Headsets Used for Drowsiness Detection. Front. Neuroinformatics 2020, 14, 553352. [CrossRef] 220. Radüntz, T.; Meffert, B. User Experience of 7 Mobile Electroencephalography Devices: Comparative Study. JMIR mHealth uHealth 2019, 7, e14474. [CrossRef] 221. Souﬁneyestani, M.; Dowling, D.; Khan, A. Electroencephalography (EEG) Technology Applications and Available Devices. Appl. Sci. 2020, 10, 7453. [CrossRef] 222. Amaral, C.; Simões, M.; Mouga, S.; Andrade, J.; Castelo-Branco, M. A novel Brain Computer Interface for classiﬁcation of social joint attention in autism and comparison of 3 experimental setups: A feasibility study. J. Neurosci. Methods 2017, 290, 105–115. [CrossRef] 223. Hinrichs, H.; Scholz, M.; Baum, A.K.; Kam, J.W.Y.; Knight, R.T.; Heinze, H.-J. Comparison between a wireless dry electrode EEG system with a conventional wired wet electrode EEG system for clinical applications. Sci. Rep. 2020, 10, 5218. [CrossRef] 224. Ratti, E.; Waninger, S.; Berka, C.; Rufﬁni, G.; Verma, A. Comparison of Medical and Consumer Wireless EEG Systems for Use in Clinical Trials. Front. Hum. Neurosci. 2017, 11, 398. [CrossRef] 225. Zerafa, R.; Camilleri, T.; Falzon, O.; Camilleri, K.P. A comparison of a broad range of EEG acquisition devices–is there any difference for SSVEP BCIs? Brain-Comput. Interfaces 2018, 5, 121–131. [CrossRef] 226. Xie, Y.; Oniga, S. A Review of Processing Methods and Classiﬁcation Algorithm for EEG Signal. Carpath. J. Electron. Comput. Eng. 2020, 13, 23–29. [CrossRef] 227. Doma, V.; Pirouz, M. A comparative analysis of machine learning methods for emotion recognition using EEG and peripheral physiological signals. J. Big Data 2020, 7, 1–21. [CrossRef] 228. Nakagome, S.; Luu, T.P.; He, Y.; Ravindran, A.S.; Contreras-Vidal, J.L. An empirical comparison of neural networks and machine learning algorithms for EEG gait decoding. Sci. Rep. 2020, 10, 4372. [CrossRef] [PubMed] 229. Varszegi, K. Comparison of algorithms for detecting hand movement from EEG signals. In Proceedings of the 2016 IEEE International Conference on Systems, Man, and Cybernetics (SMC), Budapest, Hungary, 9–12 October 2016; pp. 002208–002213. [CrossRef] 230. Pires, G.; Torres, M.; Casaleiro, N.; Nunes, U.; Castelo-Branco, M. Playing Tetris with non-invasive BCI. In Proceedings of the 2011 IEEE 1st International Conference on Serious Games and Applications for Health (SeGAH), Braga, Portugal, 16–18 November 2011; pp. 1–6. [CrossRef] 231. Pires, G.; Nunes, U.; Castelo-Branco, M. Evaluation of Brain-computer Interfaces in Accessing Computer and other Devices by People with Severe Motor Impairments. Procedia Comput. Sci. 2012, 14, 283–292. [CrossRef]

<!-- page 44 -->

Sensors 2022, 22, 3331 44 of 44

232. Cruz, A.; Pires, G.; Nunes, U.J. Double ErrP Detection for Automatic Error Correction in an ERP-Based BCI Speller. IEEE Trans. Neural Syst. Rehabil. Eng. 2017, 26, 26–36. [CrossRef] 233. Cruz, A.; Pires, G.; Lopes, A.; Carona, C.; Nunes, U.J. A Self-Paced BCI With a Collaborative Controller for Highly Reliable Wheelchair Driving: Experimental Tests With Physically Disabled Individuals. IEEE Trans. Hum.-Mach. Syst. 2021, 51, 109–119. [CrossRef] 234. Muhammad, Y.; Vaino, D. Controlling Electronic Devices with Brain Rhythms/Electrical Activity Using Artiﬁcial Neural Network (ANN). Bioengineering 2019, 6, 46. [CrossRef] 235. Roots, K.; Muhammad, Y.; Muhammad, N. Fusion Convolutional Neural Network for Cross-Subject EEG Motor Imagery Classiﬁcation. Computers 2020, 9, 72. [CrossRef] 236. Tamm, M.-O.; Muhammad, Y.; Muhammad, N. Classiﬁcation of Vowels from Imagined Speech with Convolutional Neural Networks. Computers 2020, 9, 46. [CrossRef] 237. Krauledat, M.; Tangermann, M.; Blankertz, B.; Müller, K.-R. Towards Zero Training for Brain-Computer Interfacing. PLoS ONE 2008, 3, e2967. [CrossRef] 238. Zhang, X.; Yao, L.; Wang, X.; Monaghan, J.; McAlpine, D.; Zhang, Y. A survey on deep learning-based non-invasive brain signals: Recent advances and new frontiers. J. Neural Eng. 2021, 18, 031002. [CrossRef] 239. Jiao, Y.; Zhou, T.; Yao, L.; Zhou, G.; Wang, X.; Zhang, Y. Multi-View Multi-Scale Optimization of Feature Representation for EEG Classiﬁcation Improvement. IEEE Trans. Neural Syst. Rehabil. Eng. 2020, 28, 2589–2597. [CrossRef] 240. Zhang, Y.; Zhou, T.; Wu, W.; Xie, H.; Zhu, H.; Zhou, G.; Cichocki, A. Improving EEG Decoding via Clustering-Based Multitask Feature Learning. IEEE Trans. Neural Netw. Learn. Syst. 2021, 1–11. [CrossRef] 241. Kwon, O.-Y.; Lee, M.-H.; Guan, C.; Lee, S.-W. Subject-Independent Brain–Computer Interfaces Based on Deep Convolutional Neural Networks. IEEE Trans. Neural Netw. Learn. Syst. 2019, 31, 3839–3852. [CrossRef] 242. Mussabayeva, A.; Jamwal, P.K.; Akhtar, M.T. Comparison of Generic and Subject-Speciﬁc Training for Features Classiﬁcation in P300 Speller. In Proceedings of the 2020 Asia-Paciﬁc Signal and Information Processing Association Annual Summit and Conference (APSIPA ASC), Tokyo, Japan, 14–17 December 2020; pp. 222–227. 243. Joadder, A.; Siuly, S.; Kabir, E.; Wang, H.; Zhang, Y. A New Design of Mental State Classiﬁcation for Subject Independent BCI Systems. IRBM 2019, 40, 297–305. [CrossRef] 244. Kwon, J.; Im, C.-H. Subject-Independent Functional Near-Infrared Spectroscopy-Based Brain–Computer Interfaces Based on Convolutional Neural Networks. Front. Hum. Neurosci. 2021, 15, 121. [CrossRef] 245. Barrios, L.J.; del Castillo, M.D.; Serrano, J.I.; Pons, J.L. A review of fMRI as a tool for enhancing EEG-based brain-machine interfaces. Appl. Bionics Biomech. 2012, 9, 125–133. [CrossRef] 246. Edelman, B.J.; Meng, J.; Suma, D.; Zurn, C.; Nagarajan, E.; Baxter, B.S.; Cline, C.C.; He, B. Noninvasive neuroimaging enhances continuous neural tracking for robotic device control. Sci. Robot. 2019, 4, eaaw6844. [CrossRef] 247. Meng, J.; Zhang, S.; Bekyo, A.; Olsoe, J.; Baxter, B.; He, B. Noninvasive Electroencephalogram Based Control of a Robotic Arm for Reach and Grasp Tasks. Sci. Rep. 2016, 6, 38565. [CrossRef]