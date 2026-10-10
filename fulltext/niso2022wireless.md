<!-- source: pdf/niso2022wireless.pdf | converter: pymupdf -->

<!-- page 1 -->

NeuroImage 269 (2023) 119774

Contents lists available at ScienceDirect

# NeuroImage

journal homepage: www.elsevier.com/locate/neuroimage

# Wireless EEG: A survey of systems and studies

## Guiomar Niso a , b , c , ∗ , Elena Romero d , Jeremy T. Moreau e , Alvaro Araujo f , Laurens R. Krol g

a Psychological & Brain Sciences, Indiana University, Bloomington, IN, USA  b Biomedical Image Technologies, ETSI Telecomunicación, Universidad Politécnica de Madrid and CIBER-BBN, Madrid, Spain  c Instituto Cajal, CSIC, Madrid, Spain  d Departamento de Tecnología Electrónica, Universidad Carlos III de Madrid, Madrid, Spain  e McConnell Brain Imaging Centre, Montreal Neurological Institute, McGill University, QC, Canada  f B105 Electronic Systems Lab, Universidad Politécnica de Madrid, Madrid, Spain  g Neuroadaptive Human-Computer Interaction, Brandenburg University of Technology, Cottbus-Senftenberg, Germany

a r t i c l e  i n f o

Keywords:  Wireless  Wearable  Portable  Mobile  EEG  Human brain

a b s t r a c t

The popular brain monitoring method of electroencephalography (EEG) has seen a surge in commercial attention  in recent years, focusing mostly on hardware miniaturization. This has led to a varied landscape of portable  EEG devices with wireless capability, allowing them to be used by relatively unconstrained users in real-life  conditions outside of the laboratory. The wide availability and relative aﬀordability of these devices provide a  low entry threshold for newcomers to the ﬁeld of EEG research. The large device variety and the at times opaque  communication from their manufacturers, however, can make it diﬃcult to obtain an overview of this hardware  landscape. Similarly, given the breadth of existing (wireless) EEG knowledge and research, it can be challenging  to get started with novel ideas. Therefore, this paper ﬁrst provides a list of 48 wireless EEG devices along with  a number of important —sometimes diﬃcult-to-obtain —features and characteristics to enable their side-by-side  comparison, along with a brief introduction to each of these aspects and how they may inﬂuence one’s decision.  Secondly, we have surveyed previous literature and focused on 110 high-impact journal publications making  use of wireless EEG, which we categorized by application and analyzed for device used, number of channels,  sample size, and participant mobility. Together, these provide a basis for informed decision making with respect  to hardware and experimental precedents when considering new, wireless EEG devices and research. At the  same time, this paper provides background material and commentary about pitfalls and caveats regarding this  increasingly accessible line of research.

1. Introduction

Electroencephalography (abbreviated EEG) is a brain monitoring  modality with an almost 100-year history of human application ( Berger,  1929 ), and experiences go even further back in time if we include ani-  mal studies (e.g., Caton 1875 ). The recorded electroencephalogram (also  abbreviated EEG) reﬂects the postsynaptic activity of large groups of  neurons in the cerebral cortex, allowing a subset of brain activity to be  recorded, analyzed, and in some cases even decoded, with applications  in medical, research, and consumer ﬁelds.

Throughout its long history, EEG has seen continuous improvements,  primarily with respect to methodology on the one hand, and hardware  on the other.

Methodologically, where early analyses involved the measurement  of the EEG signal’s peaks and troughs with ruler and pen on rolls of stan-  dardized graph paper, much has changed with the introduction of pro-  grammable computers. The ﬁrst major computer-aided paradigm shift

∗ Corresponding author at: Psychological & Brain Sciences, Indiana University, Bloomington, IN, USA.

E-mail address: guiomar.niso@ctb.upm.es (G. Niso) .

was probably the introduction of the event-related potential (ERP) tech-  nique, which allowed the brain’s responses to individual events to be  revealed and investigated. One advantage of this technique is that a  larger number of single event-related responses can be collected and  averaged, providing a detailed look at the time course of speciﬁc neural  processes. (See Luck’s (2014) excellent book for a detailed introduc-  tion to this technique). A further breakthrough was the ability to detect  such brain responses in single trials: without relying on averages, specif-  ically designed signal processing pipelines could be constructed to dis-  tinguish between two or more predeﬁned classes of responses. This was  ﬁrst demonstrated by Vidal (1977) , and especially following the success  of novel machine learning algorithms (e.g., Lotte et al. 2018 ), this led to  a variety of so-called brain-computer interface (BCI) systems and appli-  cations. Originally, these have largely been aimed at medical interven-  tions (e.g., neuroprosthetics, neurorehabilitation; Soekadar et al., 2015 ;  Cervera et al., 2018 ; Jamil et al., 2021 ), but today, EEG and BCI appli-  cations can additionally be found in industrial and commercial ﬁelds,

https://doi.org/10.1016/j.neuroimage.2022.119774 .  Received 5 May 2022; Received in revised form 18 November 2022; Accepted 27 November 2022  Available online 22 December 2022.  1053-8119/© 2022 Published by Elsevier Inc. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by-nc-nd/4.0/ )

<!-- page 2 -->

G. Niso, E. Romero, J.T. Moreau et al.  NeuroImage 269 (2023) 119774

e.g. neuroergonomics ( Parasuraman, 2003 ), neuromarketing ( Lee et al.,  2007 ), sports ( Thompson et al., 2008 ), and so-called passive BCI for  everyday and human-computer interaction applications ( Zander and  Kothe, 2011 ; Krol et al., 2018 ). As a ﬁnal example of the many method-  ological advances the modality has seen over the past decades, EEG has  been a prime candidate for mobile brain-body imaging (MoBI), where  measures of brain activity are combined with additional measures of  physiological, muscular, and/or behavioral activity in order to investi-  gate embodied cognition ( Makeig et al., 2009 ; Gramann et al., 2014 ).  This goes hand in hand with the development of new signal processing  methods that, e.g., allow environmental noise to be removed ( Klug and  Kloosterman, 2022 ) and brain activity to be separated from artifactual  signals ( Makeig et al., 1995 ).

Taken together, these and many other methodological improvements  make it possible to, today, use EEG not just for academic purposes, but  for a large variety of scientiﬁc, medical, industrial, and commercial ap-  plications. That is, these things are possible in principle : in practice, one  of the main obstacles to the everyday use of EEG remains the restric-  tive form factor of most EEG hardware. Here, too, however, signiﬁcant  progress has been made in recent decades.

In the earliest days, human EEG recordings used a trepanation or  burr hole through the skull for the electrodes to be close enough to the  cortex to record its activity. After that, for a long time, it remained com-  mon practice to remove or otherwise puncture the outer surface layer of  the skin to reduce the inﬂuence of noise, because, among other reasons,  computers were not yet available to ﬁlter this out post hoc. However,  advances in both electrode and ampliﬁer technology, as well as health  standards, have long since allowed for high-quality EEG to be recorded  completely non-invasively. Modern EEG typically requires little more  than applying conductive gel between each electrode and the scalp, and  a 64-channel setup may be prepared in as little as half an hour. So-  called active electrodes include small pre-ampliﬁers to further increase  the signal-to-noise ratio, and active shielding techniques may be used to  further protect the recorded signal from environmental artefacts. More  recently, alternative types of electrodes have also been developed that  do not even require gel, but instead use a simple saline solution (so-  called wet electrodes), or indeed nothing at all (dry electrodes). With  respect to ampliﬁers, the most noticeable recent trend is one of minia-  turization. Early EEG ampliﬁers could be the size of a large armoire, and  even modern-day stationary ampliﬁers (plus battery) can weigh a few  kilos. But, following emerging research (e.g., MoBI) and clinical needs,  and as neurotechnology ﬁnds applications in other ﬁelds as mentioned  above, both established companies and commercial newcomers are de-  veloping ever smaller, even wearable EEG ampliﬁers. Ideally, such de-  vices will allow the large body of EEG research of the past century to  be translated into real-world applications, outside of the laboratory, un-  hindered by the constraints imposed by the old, unwieldy machines.

This, then, is the topic of this paper: the wireless EEG device. We use  ’wireless’ here in the sense deﬁned below. There is some diﬃculty in pro-  viding an objective deﬁnition to characterise the large, heterogeneous  group of small, modern EEG devices that are designed for increased par-  ticipant mobility ( Bateson et al., 2017 ).

We may ﬁrst follow the terminology used by Bleichner and  Debener (2017) , who provided the following distinction between mo-  bile, portable, wearable, and transparent EEG. Here, mobile EEG refers  to EEG ’technology that does not require the user to remain still’, but  instead ’tolerate[s] at least a modest degree of motion movement dur-  ing signal acquisition’ ( Bleichner and Debener, 2017 ). A mobile EEG  setup could include, for example, a stationary EEG ampliﬁer recording  from a person walking on a treadmill ( Gramann et al., 2014 ). Portable  EEG on the other hand denotes that the whole set-up can ’easily be car-  ried around’ (as e.g. in Debener et al. 2012a , De Vos et al. 2014a ). This  is primarily a function of size: as Bleichner and Debener (2017) point  out, it does not necessarily mean that the device is also tolerant of mo-  tion. A third category of wearable EEG refers to a subset of portable EEG  with a ’self-ﬁtting characteristic’, allowing users to apply it themselves

and making it suitable to be worn alongside regular clothing. Finally  Bleichner and Debener (2017) , suggest that transparent EEG combines  all of the above: it refers to a ’portable, motion-tolerant, self-applicable’  device which, on top of that, is ’highly unobtrusive, near invisible, and  comfortable to wear’.

Since some of the above characteristics are diﬃcult to objectively  quantify, in this paper, we use the term wireless EEG to refer to EEG  devices that support wireless protocols for signal acquisition. In prac-  tice, this means that the term wireless EEG generally refers to any and  all of the above categories, since the presence of such a wireless proto-  col is a clear indication that the device is intended to be either mobile,  portable, wearable, or a combination thereof. Essentially, we interpret  the inclusion of a wireless protocol to signify the manufacturer’s inten-  tion to allow for signiﬁcant degrees of device and participant mobility.  Often, this mobility is ultimately the most important characteristic of  these devices: it allows EEG to be recorded with fewer hurdles, fewer  restrictions, and fewer distractions, to eventually enable the real-world  applications mentioned above.

The recent availability of various wireless EEG devices allows experi-  enced EEG researchers to expand their research beyond laboratory con-  ditions, and provides researchers from other disciplines a lower thresh-  old to incorporate EEG signals in their investigations and applications.  This paper is aimed primarily at the latter group, but aims to provide  an objective, general overview of the ﬁeld for all those interested, and  to serve as a stepping stone towards further relevant literature. To that  end, the primary contributions of this paper are (1) a list of 48 wireless  EEG devices along with a number of important —sometimes not eas-  ily obtained —features to enable their side-by-side comparison, and (2)  a list of 110 high-impact journal publications making use of wireless  EEG categorized by application and analyzed for device used, number  of channels, sample size, and participant mobility. Together, these pro-  vide a basis for informed decision-making with respect to hardware and  experimental precedents when considering new, wireless EEG devices  and research. At the same time, starting in the next section, this paper  provides some introductory and background material regarding EEG re-  search itself and the individual characteristics of EEG devices.

2. Before adopting EEG

As mentioned in the introduction, wireless EEG systems have signif-  icantly lowered the threshold to record or otherwise incorporate EEG  in research and development, and it can indeed be a valuable addition.  However, it is important to note that these small, seemingly simple de-  vices may appear to hide the actual complexity of EEG, just like the ease  of application can hide the great care that must in fact be taken to ob-  tain a meaningful signal. Even with all the advances in EEG hardware  and methodology of the past decades, the adoption of EEG must be ac-  companied by a thorough understanding of the signal: its physiological  origins, characteristics, limitations, and extraneous inﬂuences must al-  ways be taken into account. Luckily, even though the signal, at its core,  is the same one that was recorded a century ago, our understanding of  it has progressed as well.

For a brief introduction to EEG itself, the reader is referred  to, e.g., Cohen’s (2017) inviting introduction to the modality, or  Biasiucci et al. (2019) primer. One important aspect to remember is  the inﬂuence of various types of artefacts, or noise. The brain activ-  ity itself is only a tiny electromagnetic signal emanating from within a  body —and situated in a world —full of other, much stronger sources of  electromagnetism. The environment contains many electronic devices  which can interfere with the recording, and which may themselves be  neither stationary nor consistent in their electromagnetic spectrum. The  user’s movements can also greatly aﬀect the signal, ranging from the  large, overt movements that we can see and perhaps control for, to those  we may not be able to easily detect, such as involuntary facial expres-  sions (e.g., Tassinary and Cacioppo 1992 ). This is because the muscular  activity itself, as well as the movements generated by that activity, af-

2

<!-- page 3 -->

G. Niso, E. Romero, J.T. Moreau et al.  NeuroImage 269 (2023) 119774

fect the signal in diﬀerent ways. Other sources of possible interference  within the body are the eyes, the heart, and the skin. Dealing with arte-  facts is an essential part of both the design of any EEG experiment and  the processing of EEG signals. Since many artefacts are largely caused  by the user’s movements or their motion through the environment, an  increase in mobility often leads to an increase in artefacts of this sort.  Artefacts can be particularly troublesome when they are systematically  related to experimental conditions, for example when a comparison of  walking versus sitting induces more motion artefacts in the former con-  dition than in the latter. It is thus crucial to disentangle relevant brain  activity from the artefactual activity for any meaningful analyses to be  performed. Luck (2014 , Ch. 6) provides an overview of the most com-  mon artifactual sources and some ways to mitigate them in the context  of traditional research; Mihajlovic et al. (2015) provide a brief introduc-  tion to artefacts and a number of other considerations in the context of  wireless EEG. Also see Gwin et al. (2010) and Jacobsen et al. (2021) , for  example, speciﬁcally for gait-related artefacts. A well-considered arte-  fact handling pipeline is a must.

For further reading, this paper is part of a special issue on scientiﬁc  practice in EEG research. In particular, Niso et al. (2022) provide an in-  troduction and selected literature recommendations covering many as-  pects of EEG research, including considerations with respect to planning,  data collection, and signal analysis. Aside from the above-mentioned  sources, a further in-depth textbook dealing with EEG in general and  EEG analyses in particular is presented by Cohen (2014) , where chap-  ter 2 speciﬁcally deals with a number of fundamental considerations.  Also see Jackson and Bolger (2014) for a review focusing more on the  physical and physiological principles of EEG and its measurement.

As we mentioned, a thorough understanding of the modality is a  prerequisite for the successful use of EEG. This ultimately includes an  understanding of the various characteristics of the hardware, to which  we will turn in the next section, speciﬁcally related to our selection of  wireless EEG systems.

3. Overview of wireless EEG hardware

To obtain a list of current wireless EEG hardware, we (1) performed  the literature search described in the next section and extracted the de-  vices used (excluding discontinued devices but including their succes-  sors, if available), and (2) performed a general Internet search for ven-  dors of EEG equipment, and identiﬁed products on oﬀer which ﬁt the  main criterion: an EEG acquisition device with support for a wireless  transmission protocol.

For each of these devices, we then obtained the properties listed in  Table 1 . If these were not available from the oﬃcial documentation,

the manufacturers or oﬃcially licensed vendors were contacted directly  with the request for information, and were informed that the purpose of  this request was the inclusion of this information in the current publica-  tion. This resulted in some answers that could not be obtained, or could  not be translated into a uniform value in the table. Those ﬁelds have  been either left empty or interpreted to ﬁt the table where possible.

The remainder of this section will brieﬂy discuss general considera-  tions with respect to the diﬀerent columns listed in Table 1 , which have  also been colour-coded and organized in Fig. 1 . See also Fig. 3 for a vi-  sual summary of the devices listed along with some of their properties.

3.1. Company and device

The company and device name identify the device as it is on the mar-  ket. As mentioned in the introduction, both traditional EEG companies  and (relative) newcomers, even start-ups, compete in the wireless EEG  market. The more established companies are more likely to oﬀer a wider  variety of products which may communicate well with the wireless EEG  device, including e.g. software suites for analysis and additional hard-  ware peripherals, potentially allowing the wireless EEG device to be em-  bedded in a larger ecosystem for (neuro) physiological data acquisition.  See Fig. 2 for an impression of the devices listed in Table 1 .

3.2. Number and placement of EEG and reference channels

The number of EEG channels listed in the table refers to the eﬀective  number of EEG channels in the acquired data, i.e. excluding ground and  reference electrodes. The number of EEG channels that can be measured  can be an important consideration, depending heavily on the intended  use of the system, but the primary, related concern should perhaps be  one of coverage : how much, or what areas, of the scalp are covered by  the available electrodes? Exploratory or fundamental research, or appli-  cations where data-driven methods (e.g. for artefact rejection or source  localization) will be used, will generally beneﬁt from increased head  coverage, also meaning a certain minimum number of channels will be  required. In traditional EEG research, where the concerns speciﬁc to  portable systems can easily be ignored, a minimum of 32 channels is  often used to provide broad scalp coverage. High-density EEG currently  uses up to 256 channels. However, limited coverage can suﬃce for spe-  ciﬁc applications, where the relevant electrode sites are known. For re-  search of the visual or motor cortices, for example, it can suﬃce to place  a relatively small number of channels over the occipital or central sites,  respectively. Using more channels may be tempting, and may be use-  ful in speciﬁc cases even for local coverage, but more channels will also  take longer to prepare, may be more intrusive, will require more storage

Fig. 1. Schematic overview of the main characteristics of wireless EEG devices, speciﬁed in Table 1. Characteristics are colour-coded with respect to the  physical part of the device they relate to: electrodes (red), ampliﬁer (green), analog-to-digital-converter (blue), processing and transmission (orange), battery (yellow),  or the device as a whole (grey).

3

<!-- page 4 -->

G. Niso, E. Romero, J.T. Moreau et al.  NeuroImage 269 (2023) 119774

Table 1

Speciﬁcations of wireless EEG devices. Systems are sorted alphabetically by company name. Displayed characteristics include: device, company, website as of 2022 from which the data was taken, year

of market release, number of EEG electrodes, EEG electrode placement (Fixed or Flexible), reference location (E: earlobe, M: mastoid, 2M: linked mastoids, Flex: multiple reference choices, otherwise 10–20

location), movement tracking accelerometers and gyroscopes, number of bipolar ExG and auxiliary channels (numbers in brackets indicate the ability to repurpose available EEG electrodes), availability and type

of trigger ports, electrode type (i.e. Dry, Wet, Gel; Hybrid indicates that the same electrodes can be used in multiple ways), active pre-ampliﬁcation or passive electrodes, shielded/unshielded electrodes, impedance

monitoring capabilities (Start: possible before recording, Check: possible to check while recording, Continuous: monitored continuously, No: not possible), input signal range (mVpp), input impedance (G Ω), input

noise ( 𝜇Vrms), common mode rejection ratio CMRR (dB), ampliﬁer bandwidth (Hz), sampling rate (in Hz), digital resolution (bit), least signiﬁcant bit ( 𝜇V/bit), size (mm) and weight (g), battery life (in hours),

wireless protocol (i.e. Bluetooth, BLE, Wi-Fi, or ISM Proprietary at 2.4 GHz), local storage (size of local storage, or SD for SD card support, or No for no local storage), supported output formats, real-time streaming

support (LSL: lab streaming layer compatible, SDK: software development kit available, additional information follows vendor speciﬁcations), smartphone EEG support (following vendor speciﬁcations), CoME D

score for device mobility and CoME S score for system speciﬁcations according to Bateson et al. (2017) ; when information needed to calculate the score was missing, the lowest value was used, medical certiﬁcation,

and price range (k €) valid as of December 2022. A hyphen (-) indicates that the information could not be obtained.

4

<!-- page 5 -->

G. Niso, E. Romero, J.T. Moreau et al.  NeuroImage 269 (2023) 119774

Fig. 2. Images of reported wireless EEG systems. Systems are sorted by number of EEG channels. Images were obtained with permission of manufacturers from  their respective websites (see Table 1 ).

space and bandwidth, and may drain the battery faster. A ﬁrst question  to ask is thus: does my application need wide coverage of diﬀerent sites,  or can the relevant activity be recorded from a more spatially limited  region?

A related deliberation relates to the fact that diﬀerent applications  may require diﬀerent coverages. Some devices provide a ﬁxed set of  electrode locations. Here, a ﬁxed design that provides maximum cov-  erage may be appropriate, but not optimized, for a large variety of ap-  plications, whereas a design with limited coverage may be limited to  speciﬁc use cases. An advantage of a ﬁxed form factor is that the de-  vice as a whole helps to keep electrodes in place. It should be noted,  however, that not all wireless EEG form factors can reach all regions  of the scalp. When electrodes are embedded in a headband, for exam-  ple, this necessarily excludes areas at the top of the head. Other de-  vices oﬀer (some) ﬂexibility with respect to electrode locations, allowing  you to reposition the electrodes depending on the application. Flexible  designs generally make use of separate electrode caps that cover the  head and allow electrodes to be attached, more or less freely, to that  cap.

The reference electrode is a critical electrode because all other elec-  trodes will be referenced against it (i.e., the reference activity will be  subtracted from all other electrodes), as also mentioned in the primer  cited earlier ( Biasiucci et al., 2019 ). Note that, as mentioned above,  some devices may allow (some) ﬂexibility with respect to the electrode  site, whereas others make this decision for you as part of their ﬁxed form  factor. The (default) reference location is given in Table 1 following the  manufacturer’s indications, often using the international standard 10-20  system, left/right ear (E), or mastoid (M).

From among the devices listed in Table 1 , no general advice can  be given with respect to the choice of reference, as the needs will de-  pend on the application. Again, Luck (2014 , Ch. 5) provides an excellent  introduction to the relevant issues. Other than that, for comparability  and reproducibility, it can be important to follow the standards set by  others. Here, the experiments listed in the next section as well as tra-  ditional EEG literature can help. A ﬁnal note speciﬁc to wireless EEG,

however, is that the importance of the reference electrode is such that it  may require special treatment, compared to the other electrodes. A good  connection is crucial, and must be maintained throughout the recording.  When movements can be expected to interfere with electrodes at certain  sites, this must be taken into account when choosing a reference. The  reference’s importance is also why gel is sometimes used to increase the  conductivity even when the other electrodes do not use gel (described  further below).

3.3. Additional external and internal sensors

Aside from EEG, some devices allow additional electrodes to be con-  nected to record data from diﬀerent sources. This can be used for addi-  tional electrophysiological measures such as an electrooculogram (eye  activity), electrocardiogram (heart), electromyogram (muscle), electro-  dermal skin activity, or respiration. Such measurements can be done in  a bipolar fashion or using a unipolar auxiliary channel. The number of  such available channels is listed in the table. Some devices may also  have a trigger port to allow discrete event markers to be recorded, to  synchronise the recordings with experimental events.

Finally, internal sensors are commonly recorded as if they were ad-  ditional channels. Gyroscopes or accelerometers are often included to  provide information about device movement. For head-mounted de-  vices, this would directly translate into a measure of head movement.  Table 1 contains separate counts for device gyroscopes and accelerom-  eters.

3.4. Electrode type

The outer layer of the skin is a bad conductor of electricity. For this  reason, so-called gel-based electrodes use an electrolyte gel that perme-  ates the skin. The electrode itself, typically a small disk made of sin-  tered silver/silver-chloride (Ag/AgCl), remains on the surface of the skin  while the gel creates a highly conducive bridge to lower the impedance

5

<!-- page 6 -->

G. Niso, E. Romero, J.T. Moreau et al.  NeuroImage 269 (2023) 119774

between skin and electrode. Gel also provides a buﬀer against mechan-  ical movement of the electrodes. This gel is added manually during  the preparation phase: the skin below each electrode is lightly cleaned,  rubbed, and/or scratched, and gel is inserted using a syringe. While this  provides the best signal quality from among the options listed in Table 1 ,  it requires the most work, and, because the gel dries out over time, lim-  its the maximum recording duration and leaves a residue that users will  have to wash out.

The downsides of gel-based electrodes have spurred research into  so-called dry electrodes, which do not require any additional sub-  stances, but instead use pressure to connect to the skin ( Taheri et al.,  1994 ). Dry sensors come in a wide variety of shapes and materials  with many patented designs after more than 20 years of research (see  Changkyun and Seo 2016 , Lopez-Gordo et al. 2014 , Chi et al. 2010 ,  as well as Casson 2019 for systematic reviews). Their primary beneﬁts  are the faster and easier preparation ( Di Flumeri et al., 2019 ), but this  comes with some costs. For one, users may feel discomfort after some  time, sometimes as low as 15 min, largely due to headaches caused by  the electrodes’ local pressure points ( Zander et al., 2017 ; David Hairston  et al., 2014 ). Dry electrodes also present higher noise levels, i.a. because  noise is inversely proportional to the contact area which, depending  on the design, can be quite small (e.g., Huigen et al. 2002 ). Moreover,  dry sensors usually need higher low-frequency cut-oﬀs, due to the noise  contamination of the signal spectrum below 2 Hz and DC drifts due to  sweating.

The main trade-oﬀbetween gel and dry electrodes generally comes  down to signal quality and comfort versus convenience. The large va-  riety in dry electrode designs makes generalized statements diﬃcult.  While some reports state that new dry sensor systems can be used with  comparable quality to traditional systems ( Kam et al., 2019 ), and new  shapes and materials have been proposed to minimize the noise on dry  sensors (e.g., conductive polymers, graphene and textile; Casson 2019 ),  especially in freely moving participants, dry electrodes are liable to pro-  duce a qualitatively worse signal ( Mathewson et al., 2017 ). For various  reasons, participants have reported to prefer some dry electrodes over  gel-based alternatives in speciﬁc comparisons ( Hinrichs et al., 2020 ).  However, there are still very few published results that successfully use  dry electrodes in mobile settings. Generally, primarily because of the  mentioned issues of discomfort and noise, at the time of writing, most  dry electrode systems are more suitable for short-term recordings in rel-  atively stationary settings.

The so-called wet or water-based electrodes form a perhaps interme-  diate category. Wet electrodes generally consist of the same Ag/AgCl  material used for gel-based electrodes, but are surrounded by a sponge-  like material. They are prepared before application by immersing them  in an ionic solution (e.g., saltwater), and allowing them to soak until sat-  urated. The subsequent application on the scalp is then comparable to  that of dry electrodes, while the ionic solution improves the conductivity  and, by extension, the signal quality. One downside of these electrodes  is that the maximum possible recording times will be shorter than for  gel-based electrodes and can vary depending on conditions, as the ionic  solution evaporates and the electrodes dry out.

Note that in most cases, especially for non-integrated systems, mul-  tiple electrode types are available, and a choice of system does not nec-  essarily limit the choice of electrode type.

3.5. Active, passive, and shielded electrodes

Nearby electrical equipment presents a substantial source of exter-  nal noise in EEG devices: their electromagnetic activity is picked up by  the electrode cables which essentially act as an antenna. One solution  to this problem is to amplify the signal directly at the electrodes, before  it is sent through the cables. To that end, so-called active electrodes have  an additional ultra-low-noise pre-ampliﬁer located inside the electrode.  Some comparisons between passive and active ampliﬁcation electrodes  exist in stationary conditions ( Shad et al., 2020 ; Laszlo et al., 2014 ) and

during mobile tasks ( Scanlon et al., 2021 ). In particular, the ﬁndings by  Laszlo et al. (2014) suggest that active electrodes perform better with  higher impedances, which are likely when using dry electrodes or when  preparation time is short. However, despite the perceived advantages  of active ampliﬁcation, there is no general scenario in which passive  electrodes can be said to always perform signiﬁcantly worse, and much  depends on further factors ( Scanlon et al., 2021 ). For example, under op-  timal laboratory conditions with low electrode impedances, passive elec-  trodes in fact provide cleaner data than active electrodes ( Laszlo et al.,  2014 ). With respect to signal quality, there is thus no single recommen-  dation we can give in the context of wireless EEG. An important part of  the decision will be the increased weight of the active electrodes com-  pared to passive alternatives, reducing device and participant mobility.  Where ﬁnances play a role, it should additionally be noted that active  ampliﬁcation signiﬁcantly increases the cost of the electrodes.

Where preampliﬁcation is thus a measure that can be taken immedi-  ately at the electrode site, shielding refers to the protection of the signal  as it travels through the cable, lowering the eﬀects of environmental  electromagnetic interference during transmission to the (main) ampli-  ﬁer. This is usually implemented using a layer of conductive metal sur-  rounding the signal-carrying cable. Similar considerations as above ap-  ply, with shielded electrodes and electrode cables generally being heav-  ier and more expensive ( Jackson and Bolger, 2014 ).

3.6. Impedance check

In order to evaluate the signal quality, devices provide a measure of  impedance for each electrode. During preparation, this allows the exper-  imenter or user to optimize the electrode’s connection to the scalp. In  some devices, this measurement cannot be performed during signal ac-  quisition, meaning it can only be done before acquisition starts, and ac-  quisition would have to be paused for any intermediate measures (‘Start’  in the table). Other devices provide the opportunity to check these val-  ues both at the start and on request during recording (‘Start/Check’),  while a ﬁnal category allows impedance to be monitored continuously  (‘Continuous’). In such cases, the experimenter or user can keep an eye  out for electrodes that lost contact during use. Where these quality con-  trol signals can be recorded along with the EEG, it can also be used to  identify sections of noisy data for post hoc analyses. Such continuous  quality metrics are especially useful using electrodes that are more sus-  ceptible to noise, and indeed dry-electrode devices are more likely to  oﬀer continuous impedance checks.

3.7. Ampliﬁer characteristics

An ampliﬁer can be characterized, among other things, by its input  range, gain, bandwidth, input impedance, and the common mode re-  jection ratio (CMRR). The input signal range refers to the input signal  voltage (expressed in voltage peak-to-peak, Vpp) that the ampliﬁer is  able to accept as an input with a proper functioning. Since brain ac-  tivity is typically in the range of μV or even mV, all systems shown in  Table 1 will be able to properly amplify them without saturation. Spe-  cial attention to the input range might be given in the presence of large  artefacts (e.g. movements), which can produce an increase in the voltage  of the signal resulting in ampliﬁer saturation. Gain is the ratio between  the output signal and the input signal (usually measured in dB) which  reﬂects the degree of ampliﬁcation of the system. This value is not often  provided by vendors, since it is by itself not very informative as long as  the ampliﬁer is well designed for the speciﬁc input and output necessi-  ties, and thus it is not included in the table. The ampliﬁer’s bandwidth  refers to the range of frequencies (expressed by f max and f min ) that it is  able to amplify without distortion. The gain should be constant in the  bandwidth in order to not alter the signal. As the ampliﬁer will be specif-  ically designed for the acquired brain signal and the subsequent systems  in the processing of the device, we can assume that for all the devices in  Table 1 both the gain and the bandwidth will always be suﬃcient. The

6

<!-- page 7 -->

G. Niso, E. Romero, J.T. Moreau et al.  NeuroImage 269 (2023) 119774

input impedance ( Ω) reﬂects the load seen by the signal when enter-  ing the ampliﬁer. A high input impedance prevents the ampliﬁer from  draining current, improving its performance. Finally, the CMRR (dB)  quantiﬁes the ability of the device to reject signals that appear simulta-  neously and in-phase on both inputs of the ampliﬁer. The higher CMRR  the better the ampliﬁer will perform against strong noise artefacts that  are common to all electrodes, such as environmental electromagnetic  interference.

3.8. Sampling rate

Sampling rate refers to the number of samples that are digitally ac-  quired per second, measured in Hertz (Hz). The Nyquist-Shannon theo-  rem ( Nyquist, 1928 ) states that for any periodic signal of a given fre-  quency, a sampling rate higher than two times the frequency of the  signal is needed to accurately detect its presence. In EEG, however, a  larger margin is usually taken to allow for higher signal ﬁdelity. There-  fore, with the EEG activity of interest generally being up to around 50  Hz, sampling rates of 250 or 500 are common. Some recent wireless  EEG devices have higher sampling rates, with several devices reaching  over 1000 Hz (e.g. the Mind Media NeXus-10 MKII which can record  up to 8000 Hz) enabling the study of high-frequency brain activity with  wireless EEG systems, albeit at the cost of increased battery and storage  requirements. Aside from studies that speciﬁcally require high sampling  rates, for most applications of wireless EEG, a device’s sampling rate it-  self is unlikely to be the deciding factor.

3.9. Digital resolution and least signiﬁcant bit

After sampling the analog brain activity, it is converted into a digital  value by the analog-to-digital converter (ADC). The resolution of this  converter denotes the number of ﬁnite values that the digital signal can  span. As this number of values must be coded in binary, it is expressed  as a number of bits. For example, a system with 10 bits resolution can  encode an analog input in 1024 diﬀerent levels (2 10 = 1024), and a 24  bit resolution system can encode the same analog input in 16777216  diﬀerent levels (2 24 = 16777216). The higher the resolution, the better  the digital signal can match the analog original.

The wireless EEG systems in Table 1 range from 12 to 24 bits. As  Casson (2019) mentions, even the lower end of this range is suﬃcient  for most EEG applications, although higher resolutions may still be pre-  ferred for fundamental research. Downsides of higher bit depths relate  primarily to the wireless transmission: a higher resolution implies larger  energy consumption in transmission and broader wireless transmission  bandwidth. Compressing EEG data could be a possible solution in order  to minimise data transmission, but due to the EEG signal’s nature, this  compression is extremely diﬃcult ( Zhang et al., 2013 ).

In addition to the digital resolution, Table 1 also includes the am-  plitude resolution of the least signiﬁcant bit, LSB (in μV/bit), which  represents the minimum input voltage level that produces a change in  the output. This can be computed from the input range of the ADC:  mVpp/2 Resolution (bits) . The lower this number is, the lower the quantiza-  tion error, and therefore, the more accurate the recorded signal will be.  Since this number is strongly dependent on other factors, unless there  is a speciﬁc known requirement for a certain high resolution, it requires  no further thought.

3.10. Size, weight, and battery life

The size of the ampliﬁer or device is listed in mm by descending  dimensions (e.g., not the ’length’, but simply the longest value is listed  ﬁrst), and the weight is listed in grams. Battery life indicates, in hours,  the maximum duration of a recording on a single charge of the bat-  tery. The considerations here are obvious, where smaller and lighter  will be better for most wireless cases as it increases device mobility,  and a longer battery life increases participant mobility while provid-

ing more ﬂexibility in terms of study design. Some studies that require  long-term monitoring (e.g. overnight) may require battery life to be pri-  oritized over other factors. Some systems allow hot-swapable batteries  (e.g. Wearable Sensing DSI-24) or extending battery life with the use  of a power bank, (e.g. Brain Products LiveAmp) , which allowing over  24 h of continuous recording. A perhaps expected correlation between  size/weight and battery life does not emerge from this table. It should  be noted, however, that some vendors do, and others do not include  the sensors in the ﬁgures related to size and weight. Where sensors  are attached separately, these numbers typically refer to the size and  weight of the ampliﬁer. Relatively speaking, the additional weight of  the sensors are commonly negligible, especially for passive electrodes  (see above). For integrated systems, the ﬁgures refer to the combination.  With an average adult head length reaching roughly 20 cm, devices with  a longest dimension over approximately 15 cm are generally integrated  ones. The lightest device reported in Table 1 is the Mentablab Explore ,  an 8-channel ampliﬁer weighing only 27 grams and particularly low size  dimensions (40 × 40 × 20 mm).

3.11. Wireless protocol

The deﬁning factor of the devices listed in Table 1 is that they can  transmit the acquired signal wirelessly. The protocol that is used for this  transmission has some practical implications for the device’s usage and  mobility. The protocols that appear in Table 1 are Wi-Fi (IEEE 802.11),  Bluetooth (IEEE 802.15.1), Bluetooth Low Energy (BLE, the Bluetooth  4.x releases with lower energy consumption), Bluetooth 5 (with more  capabilities and compatible with both Bluetooth and BLE) and ISM Pro-  prietary at 2.4GHz (usually based on IEEE 802.15.4 or IEEE 802.15.6).  The main diﬀerences between these protocols relate to the transmission  rate, range, and the frequency band in which they operate. Bluetooth  and BLE have lower transmission rates (up to 2 Mbps) while Wi-Fi can  have higher data rates (up to 2 Gbps). Nevertheless, transmission rate  can be ignored for our purposes, as all protocols match the speciﬁca-  tions of their respective devices to transmit the recorded signals with  their respective speciﬁcations (e.g. number of channels, sampling rate,  resolution).

The protocol’s transmission range does have a major inﬂuence on  the possible use cases. In technical terms, the limitation comes from  the maximum ratio of transmitted power per unit of time allowed in  the frequency bands, which is legally regulated. Also the type of an-  tenna that the device incorporates inﬂuences the range: usually, Blue-  tooth transceivers have smaller antennas, while some Wi-Fi transceivers  allow adding external antennas to increase transmission range. The typ-  ical eﬀective transmission range for Bluetooth indoors is about 5–10 m,  while for Wi-Fi this is about 10–20 m. If the receiving device is in the  direct vicinity of the acquisition device, both protocols should provide  equivalent performance. However, over longer distances, or when there  may be no direct line of sight between transmitter and receiver, diﬀer-  ences may become evident. This latter case can easily happen when the  user’s body itself blocks the line of sight, e.g. when the EEG device is  carried at the back of the head but the receiver is located in front of  them.

As for the frequency band, most of these wireless EEG interfaces are  using the same 2.4 GHz frequency band. This is the most saturated unli-  censed spectrum band in conventional environments, as these protocols  have been adopted worldwide by handhelds (laptops, smartphones) and  Internet-of-Things devices. As a result, a high number of wireless devices  can lead to a degradation in the quality of communications. Wi-Fi proto-  col provides higher reliability (in terms of packets delivered) because it  usually uses a higher transmission power (as a result, being more resis-  tant against interferences and collisions) and also, because of the mod-  ulation used. On the other hand, energy consumption associated with  communication is higher when using Wi-Fi.

Should the wireless connection be cut oﬀfor any period of time, some  devices have the ability to store and process data locally, discussed next.

7

<!-- page 8 -->

G. Niso, E. Romero, J.T. Moreau et al.  NeuroImage 269 (2023) 119774

Fig. 3. Visual summary of reported wireless EEG systems. Wireless EEG systems are grouped by the number of channels, and each summary icon indicates the  type of device: integrated (circle) or cap + ampliﬁer (square), the type of available sensors: dry (yellow), wet (blue), dry (pink) or a multiple options (grey); the  wireless protocol used: bluetooth or BLE, Wi-Fi, or ISM Proprietary at 2.4GHz; and the medical certiﬁcation (black lined shape).

3.12. Data storage and output format

Some wireless EEG devices provide on-board signal recording capa-  bilities. This means data can be stored on local, possibly removable,  ﬂash storage before or instead of wireless transmission. Thus, if the  wireless signal is interrupted for any reason, it can be recovered and/or  re-transmitted from a local copy, alleviating the risk of signal loss in  unreliable wireless conditions.

The table also lists the ﬁle format in which the data can be stored. In  some devices this is a ﬁxed format, whereas more commonly, a choice  is given through accompanying software. All of the devices listed in  Table 1 support at least one open standard, and except from g.tec Uni-  corn and BitBrain systems that only export to .csv, all the other de-  vices are able to export data in at least one of the recommended for-  mats by the Brain Imaging Data Structure (BIDS) speciﬁcation (i.e. Euro-  pean data format [.edf], Biosemi [.bdf] and BrainVision formats [.vhdr,  .vmrk, .eeg]), facilitating the standardization of acquired brain data  ( Pernet et al., 2019 ; Niso et al., 2018 ; Holdgraf et al., 2019 ). Motion  data will soon also be incorporated into BIDS, facilitating the standard-  ization of recordings of movements coming tracking in virtual spaces  or in physical motion capture systems with IMUs (Inertial Measurement  Units). When this is done, prospective buyers for whom this is relevant  may want to verify with the vendors that motion measurements, too,  are organized according to the appropriate standard.

3.13. Real-time data access

Whereas local data storage is useful for the above-mentioned rea-  sons, the primary purpose of the wireless protocol is usually to enable  real-time remote acquisition of the data. Such access allows the device  to be used for real-time cognitive monitoring, or for interactive appli-  cations where a connected device can use the brain activity as input  and respond whenever speciﬁc mental states are detected —i.e., a brain-  computer interface.

At the very least, real-time access is generally provided through some  piece of software. Important for many cases, however, are the additional  ways in which this data may be accessed and integrated into larger,  custom processing pipelines. This is generally made possible through  a separate software development kit (SDK), or through compatibility  with open standards. In this latter category, the Lab Streaming Layer  (LSL) has recently established itself as the main standard. LSL is a soft-  ware framework that provides functionality to transmit and receive data  over a local network, automatically handling data formatting, network-  ing, synchronization, and real-time (or buﬀered) access. Devices from  Table 1 that explicitly support LSL are directly compatible with a large  ecosystem of both open-source and proprietary applications. When real-  time access is provided through an SDK or through other open standards,  this generally means that some additional programming is required be-  fore the device can be included in an existing experimental set-up (or to  make the device LSL-compatible). This option may also be dependent on  licensing agreements, potentially increasing the cost of operation. This  also applies to devices that exclusively use proprietary software to ac-  cess the data. In this latter case, embedding the device in existing set-ups  may be diﬃcult or even impossible.

3.14. Categorization of mobile EEG (CoME) score

Bateson et al. (2017) introduced the Categorization of Mobile EEG  (CoME) scheme to provide a quantitative method for the categorization  of diﬀerent EEG systems, or diﬀerent ways in which EEG systems are  used, based on selected parameters. The CoME scheme provides three  separate scores: a device mobility score, a participant mobility score,  and a system speciﬁcation score. Additionally, the full CoME score men-  tions the number of channels, which we already discussed above.

The device mobility score (CoME D ) reﬂects where and how the EEG  device is positioned, eﬀectively representing the amount to which the  participant is free from physical restrictions as a result of the device.  The minimum score of 0 indicates a traditional, tethered system, while

8

<!-- page 9 -->

G. Niso, E. Romero, J.T. Moreau et al.  NeuroImage 269 (2023) 119774

the maximum score of 5 refers to a fully head-mounted device with no  additional equipment needed —not even to wirelessly receive the data.

The system speciﬁcation score (CoME S) ranges from 4 to 20, and  sums together four separate characteristics, each scored between 1 and  5. These four characteristics are electrode type (1 being passive, un-  shielded, dry electrodes, and 5 being active, shielded, gel electrodes; see  above), bit resolution (starting at 14 bit for a score of 1, up to more than  24 bit for 5), sampling rate (from approx. 128 to more than 1000 Hz),  and battery life (from no battery up to more than 24 h).

The participant mobility score, ﬁnally, reﬂects the activity of the  wearer, ranging from lying, sitting, or standing still (0) to unconstrained  sports (5).

Note that these scores are, in most cases, not ﬁxed for a single EEG  system: the same device can be positioned diﬀerently depending on the  situational requirements, many devices allow for a selection of diﬀerent  sampling rates, electrodes, et cetera, with accordingly variable battery  life, and even the most mobile system can still be used by a seated per-  son. Still, we have attempted to score the devices in Table 1 with respect  to the device mobility and system speciﬁcation scores. For system spec-  iﬁcations, we mention the highest possible score that the device theo-  retically supports. The same applies to device mobility, with the added  note that we assume there is a need for real-time processing of the data.  That is, mere on-device, oﬄine recording capabilities do not satisfy the  requirement for a score of 5 that no additional equipment is needed.  The participant mobility score cannot meaningfully be determined for  a device in isolation. This score, therefore, is not considered here, but  used in the next section’s literature review.

3.15. Medical certiﬁcation

Use of devices in a clinical or medical context is only allowed when  those devices have received the appropriate certiﬁcations. Appropri-  ately certiﬁed devices would, for instance, have been approved by the  Food and Drug Administration (FDA) in the United States, or the Euro-  pean Medicines Agency (EMA) in the European Union. While the pres-  ence or absence of such a certiﬁcation makes no functional diﬀerence  for non-medical use cases, including academic research, this certiﬁca-  tion is a requirement for clinical research, and has thus been included  in Table 1 .

3.16. Price range

Price is a very dynamic characteristic. To the extent that the manu-  facturers or vendors agreed to supply this information, it has been men-  tioned in Table 1 valid as of December 2022. Commonly, a range is  given, reﬂecting the many customization features that can aﬀect it. It is  worth noting that in general, with few exceptions (e.g. OpenBCI, Emotiv,  which are more consumer-grade systems), it is rare to ﬁnd public prices  available online, and only direct requests for a speciﬁc quote can pro-  vide an estimate. As a general rule of thumb, the price of wireless EEG  systems seems directly related to the number of channels. Therefore, a  careful selection of the number of electrodes (and their placement) is  advisable prior to the acquisition of a new device.

4. Wireless EEG literature

This section provides a survey of published work that has made use  of wireless EEG. The search for available literature using wireless EEG  was performed in PubMed searching for ‘EEG’, ‘electroencephalogra-  phy’, or ‘electroencephalogram’ occurring together with ‘wireless’, ‘mo-  bile’, ‘portable’, ‘wearable’, or ‘ambulatory’ in the title or abstract, while  excluding results that refer to animal studies. The search was performed  in March 2022 and included search results up to and including all of  2021. For a closer look at a manageable but representative sample of  impactful research, we retained only publications that were published  in journals and were cited, on average, at least 10 times per year. Total

Fig. 4. Flow diagram for literature search, screening and inclusion process.

citations were assessed using LISC ( Donoghue, 2019 ) and averaged over  the years since the article was published. Because we are primarily in-  terested in the applications of wireless EEG, we furthermore manually  removed publications that were reviews, methodological approaches or  hardware designs without any experimental data. We further removed  studies where the EEG system details were not reported. Finally, we ex-  tracted the general topic of the study, the device used, the number of  channels, the number of participants, and determined the CoME par-  ticipant mobility score described above. For further details of the lit-  erature review approach, see the ﬂow diagram following the Preferred  Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA)  guidelines ( Page et al., 2021 ) in Fig. 4 .

4.1. Overview

A total of 2137 papers were returned by the initial search result.  The oldest result is from 1975, and describes a 4-channel 24 h cassette  recorder for long-term EEG monitoring of ambulatory patients devel-  oped at the Montreal Neurological Institute ( Ives and Woods, 1975 ).  Since then, as Fig. 5 a shows, the number of studies using wireless EEG  systems has increased rapidly —but primarily so over the past ten years,  and presently peaking in the most recent year. This ﬁgure represents the  results of the initial search without further pruning.

Our selected sample includes 110 publications, which are referenced  in Table 2 . We can see that the number of participants in the analyzed  wireless EEG studies is generally between 10 and 20, with a median  of 18 (see Fig. 5 b). However, a relatively large number of publications  used a small sample, with 25 publications having fewer than 10 partic-  ipants. In our sample, this appears to be a result of the relative novelty  of these devices, where some studies are explorative feasibility stud-  ies proposing new designs or algorithms; however, all categories of ap-  plications contained examples of both larger and smaller samples. See  Button et al. (2013) for a critique of sample sizes in neuroimaging re-  search, which, as we can see, clearly applies to the wireless EEG subﬁeld  as well. The other extreme end of the scale is held by a large-scale study  by Hashemi et al. (2016) which included 6029 participants to charac-  terise EEG measures through adulthood using a 4-channel Muse device  (excluded from the ﬁgure as an outlier for visualization purposes).

9

<!-- page 10 -->

G. Niso, E. Romero, J.T. Moreau et al.  NeuroImage 269 (2023) 119774

Fig. 5. Overview of reviewed wireless EEG literature . (A) number of studies using wireless EEG systems between 1975 and 2021 ( n = 2109 out of the 2137  selected studies); (B) number of participants in the analyzed wireless EEG studies ( n = 110); (C) number of channels reported ( n = 110).

Fig. 5 c shows the number of channels reported, and shows probably-  familiar peaks at the powers of 2: 8, 16, 32, et cetera. The median  number of channels is 14. To the left of the median, we see that here,  too, a relatively large amount of studies used signiﬁcantly fewer chan-  nels, with 37 publications using fewer than eight channels, and 11  publications reporting only one single channel. In part, this reﬂects  the availability of devices, with e.g. the single-channel Neurosky Mind-  wave having been used in some of these publications, but it also goes  hand in hand with one of the main reasons for adopting wireless EEG

more generally: the wish for miniaturization and ease of use. In the  list of 110 publications, one each reported using 157, 248, 256, and  264 channels, which have been excluded as outliers from the ﬁgures;  furthermore, they primarily used stationary EEG devices in a mobile  setting.

Fig. 6 illustrates which wireless EEG systems were used in these pa-  pers. Note that, as Bleichner and Debener (2017) also explained, ‘mo-  bile’ EEG studies may still be performed using stationary, non-wireless  devices. These were therefore removed for the illustration in Fig. 6 . Fur-

Table 2  References of the 110 selected papers, organized by ﬁeld of application.

Clinical  conditions

Chez et al., 2006 ; Malcolm et al., 2015 ; Lucey et al., 2016 ; Grønli et al., 2016 ; López-Larraz et al., 2016 ; Gu et al., 2017 ; Levendowski et al., 2017 ;  Neale et al., 2017 ; Simons et al., 2018 ; Debellemaniere et al., 2018 ; Calabrò et al., 2018 ; Dres et al., 2019 ; Shustak et al., 2019 ; Mikkelsen et al., 2019 ;  Ding et al., 2019 ; Jebelli et al., 2019 ; Ahn et al., 2019 ; Vandecasteele et al., 2020 ; Arnal et al., 2020 ; Nakamura et al., 2020 ; Martins et al., 2020 ;  Cicalese et al., 2020 ; Clarke et al., 2021  Cognitive  monitoring

Holm et al., 2009 ; Gramann et al., 2010 ; Liao et al., 2012 ; Liu et al., 2013 ; Lin et al., 2014 ; De Sanctis et al., 2014 ; Aspinall et al., 2015 ; Mirkovic et al.,  2016 ; Hashemi et al., 2016 ; Beurskens et al., 2016 ; Bradford et al., 2016 ; Zink et al., 2016 ; Leminen et al., 2017 ; Morales et al., 2017 ; Zhang et al., 2017 ;  Poulsen et al., 2017 ; So et al., 2017 ; Banaei et al., 2017 ; Al-Barrak et al., 2017 ; Dikker et al., 2017 ; Katsigiannis and Ramzan, 2018 ; Marín-Morales et al.,  2018 ; Athavipach et al., 2019 ; Gonzalez Viejo et al., 2019 ; Golnar-Nik et al., 2019 ; Ziegler et al., 2019 ; Dehais et al., 2019 ; Blanco et al., 2019 ;  Solis-Escalante et al., 2019 ; Djebbara et al., 2019 ; Reiser et al., 2019 ; Piñeyro Salvidegoitia et al., 2019 ; Ladouce et al., 2019 ; Bevilacqua et al., 2019 ;  Nordin et al., 2019 ; Scanlon et al., 2019 ; Fronso et al., 2019 ; Narayanan and Bertrand, 2020 ; Raheel et al., 2020 ; Zhang et al., 2020 ; Packheiser et al.,  2020 ; Nordin et al., 2020 ; Lin et al., 2020 ; Topalovic et al., 2020 ; Bigliassi et al., 2020 ; Haar and Faisal, 2020 ; Mustile et al., 2021 ; Hölle et al., 2021  Control and  communication

Lin et al., 2010 ; De Vos et al., 2014 ; Ma et al., 2015 ; Luu et al., 2016 ; Kwak et al., 2017 ; Artoni et al., 2017 ; Chen et al., 2018 ; Zhang et al., 2019 ;  Si-Mohammed et al., 2020 ; Shao et al., 2020 ; Tortora et al., 2020  Methodological  approaches

Chi et al., 2012 ; Badcock et al., 2013 ; De Vos et al., 2014b ; David Hairston et al., 2014 ; Bleichner et al., 2015 ; Mikkelsen et al., 2015 ; Debener et al.,  2015 ; Mullen et al., 2015 ; Snyder et al., 2015 ; Rogers et al., 2016 ; Nathan and Contreras-Vidal, 2015 ; Kilicarslan et al., 2016 ; Oliveira et al., 2016 ;  Melnik et al., 2017 ; Krigolson et al., 2017 ; La et al., 2018 ; Radüntz, 2018 ; Kim et al., 2018 ; Kassab et al., 2018 ; Kam et al., 2019 ; Blum et al., 2019 ;  Titgemeyer et al., 2020 ; Hinrichs et al., 2020 ; Li et al., 2020 ; Klug and Gramann, 2021 ; Reiser et al., 2021

10

<!-- page 11 -->

G. Niso, E. Romero, J.T. Moreau et al.  NeuroImage 269 (2023) 119774

Fig. 6. Distribution of wireless EEG devices used in the analyzed stud-  ies. (A) For all studies: Emotiv 25%, Homemade 19%, mBrainTrain 10%, In-  teraxon 7%, Neurosky 7%, g.tec 7%, ANT Neuro 7%, Brain Products 4%, CGX  4%, Advanced Brain Monitoring (ABM) 3%, Neuroelectrics 3%, Compumedics  3% ( n = 69). B) For studies where the CoME participant mobility score described  in Bateson et al. (2017) is P < = 1 (left) and P < = 2 (right).

thermore, since many papers used now-discontinued devices, they are  represented by manufacturer, rather than by model name. Devices that  were not wireless, have no present-day successor, and occurred only  once in the literature search are also not included, for a total of 69 pa-  pers represented in this ﬁgure.

From the included papers, 24.6% used an Emotiv EPOC system, and  10.1% a device by mBrainTrain (often in conjunction with cEEGrid, a  type of non obtrusive, behind-the-ear electrodes; Debener et al., 2015 );  third place is shared equally among InteraXon ( Muse family), Neurosky,  g.tec, and ANT Neuro. The remainder is divided among 5 further manu-  facturers: Brain Products, ABM, Neuroelectrics, Compumedics, and CGX  (formerly Cognionics). We point out that this is exclusively a measure  of prevalence in our current selection, and that the popularity of any  one device is likely to be inﬂuenced by a number of factors, including  the time on the market and price, with Emotiv providing one of the ﬁrst  commercially available wireless EEG devices. Roughly as prevalent as  the top branded device is the category of ‘home-made’ devices: devices  that were either fully or partially constructed by the researchers them-  selves. A possible implication is that, on the one hand, oﬀ-the-shelf de-  vices may not fulﬁl the many divergent requirements placed upon wire-  less EEG devices for diﬀerent applications, while, on the other hand,  research is active and ongoing into ﬁnding new and improved wireless  EEG solutions.

Because the focus of this paper is on wireless EEG, the main pur-  pose and beneﬁt of which, as we mentioned, is the allowed participant  mobility, we speciﬁcally focus here on papers with a CoME participant  mobility score of at least 2. This is the case for 43 papers, or 39%. Fig. 6 ,  bottom, illustrates the diﬀerent distributions of these systems for essen-  tially non-mobile studies ( P of 0 or 1), and mobile studies ( P > = 2). We  see that the category of ‘homemade’ devices, which are by and large  intended to test new hardware designs, are in fact rarely tested using  mobile participants. A notable diﬀerence is also given by ANT Neuro’s

systems apparently being used primarily with mobile participants: no  paper in the current selection used such a system for stationary partici-  pants.

4.2. Fields of application

The analyzed papers broadly fall into four identiﬁed categories:  cognitive monitoring, clinical conditions, communication and control , and  methodological approaches . These emerged from more speciﬁc topics or  subﬁelds attributed to each of the papers.

As illustrated in Fig. 7 a, most studies investigated or employed cog-  nitive monitoring, with 44.1% falling in this category. Clinical appli-  cations represented the second-largest group with 24.3% of papers,  methodological approaches represented 21.6%, and communication and  control 9.9%. Fig. 7 b shows this in more detail, including the main iden-  tiﬁed subﬁeld topics.

Fig. 7 d groups the papers by the CoME participant mobility score  mentioned in the previous section ( Bateson et al., 2017 ). 40% of pa-  pers scored 1, meaning participants were ‘lying, sitting, or standing with  localized movement’ such as button pressing. 21% scored 0, meaning  there was not even any localized movement. Mobility proper starts at a  score of 2, with constrained walking/cycling (19% of papers), and 19%  achieve a score of 3, where walking/cycling is unconstrained. More in-  volved activities, represented by scores 4 were used by only 3% and  none of the papers scored 5.

Fig. 7 c. illustrates the diﬀerent distributions of the identiﬁed ﬁelds  separately for non-mobile and mobile studies. The main, clearly ob-  servable diﬀerence here is that cognitive monitoring appears much  more popular with increased mobility, whereas clinical applications  are largely performed in non-mobile settings. Indeed, in mobile set-  tings, more than half of all studies —even more than two thirds when  considering only real-life applications and removing methodological re-  search —make use of the technology to perform some form of cognitive  monitoring.

In the following subsections, the three categories that refer to real-  life applications will be discussed in more detail. This excludes the  methodological investigations, which for example used wireless EEG for  the purpose of hardware comparisons, artefact correction methods, val-  idation studies or new system design proposals. We will primarily focus  on studies with signiﬁcant participant mobility, but as we will see, in  a world where many activities are done in a seated position, the envi-  sioned use cases are generally not limited to active scenarios.

4.2.1. Cognitive monitoring  Cognitive monitoring here refers to the use of neurotechnology to,  usually in a continuous and real-time fashion, obtain a measure or index  of speciﬁc mental activity, such as preferences, emotions, or workload,  to name just a few examples. When this is done interactively, i.e., when  a device adapts or responds to the measured mental states in real time,  this may also be referred to as passive BCI ( Zander and Kothe, 2011 ;  Krol et al., 2018 ) or neuroadaptive technology ( Zander et al., 2016 ), but  for our current purposes, we include this in the broader category of  cognitive monitoring. This is the most common application of wireless  EEG in the analyzed literature, with a total of 44% of all 110 papers in  this category, 60% of all mobile papers, and even 73% when excluding  methodological papers.

As for speciﬁc mental states to be detected using wireless EEG, ‘at-  tention’ has received the most interest in the current sample. For exam-  ple, Scanlon et al. (2019) used a 15-channel Brain Products V-amp to  record an auditory oddball task in 12 cycling participants, measuring  P300 responses as an index of attention. Gramann et al. (2010) used  a visual oddball paradigm to compare attention-related indices dur-  ing standing, walking, and running on a treadmill. Applications of  attention-related cognitive monitoring have largely been sought in the  educational domain (e.g. Bevilacqua et al. 2019 , Dikker et al. 2017 ,  Poulsen et al. 2017 ). Also automotive contexts form another popu-

11

<!-- page 12 -->

G. Niso, E. Romero, J.T. Moreau et al.  NeuroImage 269 (2023) 119774

Fig. 7. Wireless EEG ﬁelds of application. (A) Fields of application of wireless EEG devices in the analyzed studies: cognitive monitoring 44% (purple), clinical  conditions 24% (orange), communication and control 10% (blue) and methodological approaches 21% (grey), ( n = 110). (B) Number of studies in each of the  subﬁelds applications with occurrence > 1: cognitive monitoring (purple), clinical conditions (orange) and communication and control (blue) and methodological  approaches (grey). (C) Fields of application of wireless EEG devices in the analyzed studies where the CoME participant mobility score described in ( Bateson et al.,  2017 ) is P < = 1 (left) and P < = 2 (right). (D) Distribution of the ﬁelds of application of the analyzed studies for each CoME participant mobility score from 0 to 5.

lar ﬁeld for attention-related cognitive monitoring ( Lee et al., 2014 ;  Lin et al., 2014 ; Zhang et al., 2017 ). In these two contexts, however,  participant mobility according to the CoME score is in eﬀect 1 as study-  ing and driving are generally seated activities.

Another popular ﬁeld of investigation, which does make clearer use  of participant mobility, focuses on people’s emotions and perceptions  of the real world around them. For example, Banaei et al. (2017) used  a 128-channel Brain Products BrainAmp , made wireless using the dis-  continued MOVE system, to investigate perceptions and experiences  in various architectural spaces experienced in virtual reality. Similar  studies have been performed in outdoor or urban areas. For exam-  ple, Neale et al. (2017) used a 14-channel Emotiv EPOC with 95 se-  nior participants. They used the device’s accompanying commercial  suite’s indices for engagement, excitement, frustration, and meditation  to look for signiﬁcant diﬀerences while the participants were explor-  ing diﬀerent outdoors areas. They acknowledge that they cannot prop-  erly scrutinise these proprietary metrics, but report some signiﬁcant  diﬀerences.

Other targeted mental states are emotions, memory, and cognitive  responses related to auditory presentation, such as attention to a spe-  ciﬁc speaker ( Mirkovic et al., 2016 ) or responses to target sounds using  auditory oddball paradigms ( De Vos et al., 2014 ; Debener et al., 2012b ;  Ladouce et al., 2019 ). Neuromarketing is another category, where a va-  riety of cognitive states may be used to detect consumer interests with  respect to diﬀerent products, including, in our sample, mobile phone  brands ( Golnar-Nik et al., 2019 ) and beer ( Neale et al., 2017 ).

Cognitive monitoring allows real-life, everyday situations to be en-  hanced by technology that can assess and respond to information con-  cerning human mental states. In the above example, a classroom teacher  may be notiﬁed by neurotechnology when the students lost the thread  of the teacher’s explanation, without any student needing to explicitly  communicate this. Similarly, a driver’s drowsiness may be automatically  detected and acted upon by an autonomous vehicle, avoiding poten-  tial catastrophe. And as most people today carry technology with them  wherever they go, a smartphone that e.g. detects how some regions of  the city evoke more positive emotions in us may in the future adapt its

navigation suggestions to follow speciﬁc, pleasing routes, or conversely,  use these methods to avoid locations with stressful traﬃc. As these ex-  amples show, most envisioned applications of such neuroadaptive tech-  nology would not practically be possible without wireless EEG.

4.2.2. Clinical conditions  EEG has always seen clinical interest, primarily for diagnostic pur-  poses, and this is no diﬀerent for wireless EEG, with 24.3% of all 110  analyzed papers in this category. This number drops signiﬁcantly to  11.6%, however, when considering only situations in which participants  are mobile (14.3% excluding methodological papers). This may indicate  that in clinical settings, other considerations than participant mobility  take precedence to opt for wireless EEG devices. The mobile conditions  in our sample involve exoskeletons, age-related research, and long-term  monitoring of pathological conditions.

For example, Chez et al. (2006) recorded EEG of 889 participants us-  ing a discontinued DigiTrace device, for a total of 24 h each, thus requir-  ing some freedom of mobility of the patients. They sought to assess the  frequency of EEG abnormalities in patients with autism spectrum disor-  ders. In less mobile situations, clinical conditions often focus on phases  of sleep. For example, Shustak et al. (2019) presented a 4-channel cus-  tom ‘temporary-tattoo EEG’ device, which contains thin, printed elec-  trodes applied directly onto the skip without gel, for unobtrusive sleep  monitoring at home, and reported ‘clear diﬀerentiation of sleep stages’  based on data recorded during either short naps (2 h) or longer night  sleeps (6 h) of nine participants. For a systematic review of the accuracy  of wearable devices for estimating sleep onset, see Scott et al. (2020) .  Dementia, stress, depression, and migraines are other conditions that  were monitored using wireless EEG in our sample.

Exoskeletons are machines that support part or all of the body,  for example in situations where a person’s natural strength or stamina  are insuﬃcient. They can furthermore be used for rehabilitation when  motor functions are impaired, e.g. after a stroke. For example, López-  Larraz et al. (2016) used an unspeciﬁed 32-channel mobile EEG system  from g.tec in order to detect a stroke patient’s movement intentions in  real time, allowing the exoskeleton to perform supportive movements.

12

<!-- page 13 -->

G. Niso, E. Romero, J.T. Moreau et al.  NeuroImage 269 (2023) 119774

While many clinical studies are performed bedside or in other sta-  tionary conditions, as is evident e.g. from Fig. 7 d, wireless EEG allows  freedom of mobility during the long-term monitoring that is often re-  quired to detect clinical symptoms in the EEG. This opens new doors  as longer monitoring becomes possible, as well monitoring under dif-  ferent, speciﬁcally real-life conditions. For rehabilitation, where partic-  ipant mobility is in fact the goal of the therapy, wireless EEG similarly  allows new avenues to be explored.

4.2.3. Communication and control  Wireless EEG, especially direct-to-consumer, commercial devices, is  often used as an input modality to replace or supplement e.g. a keyboard  or a mouse. Such uses of neurotechnology to explicitly (knowingly, vol-  untarily) communicate something or control an application are here in-  cluded in the category of communication and control. This has been one  of the main focuses of BCI research in the past ( Wolpaw et al., 2002 ),  although, as we can also see in this study, research focusing speciﬁ-  cally on passive BCI is gaining in prevalence ( Eddy et al., 2019 ). We also  include neurofeedback in this category, in the sense that engaging in  neurofeedback is an explicit act to manipulate one’s own brain activity  or mental state. 9.9% were attributed to this category from among the  110 papers, 11.6% among the P > = 2 papers, and 14.3% of the latter  minus the methodological papers.

Robots and robotic arms are a popular object of control in the se-  lected literature. For example, Si-Mohammed et al. (2020) used a 6-  channel g.tec g.USBamp to investigate the use of wireless EEG and  steady-state visually evoked potentials (SSVEP) in augmented reality in  order to control a robot. Given the robustness of SSVEP signals, this  has been a popular method to implement selection using neurotechnol-  ogy, with several other studies exploring the same ( Shao et al., 2020 ;  Chen et al., 2018 ). Virtual reality, games, and neurofeedback also con-  stitute topics of interest in the communication and control ﬁeld. For  example, an intervention program on 68 patients suﬀering from mild  cognitive impairment using a Cognionics Quick-20 wireless EEG system  based on virtual reality training, reported a signiﬁcant improvement in  cognitive and physical function in the intervention cohort ( Thapa et al.,  2020 ). Note that these applications are largely in seated contexts, but  Debener et al. (2012b) explored a popular EEG-based control paradigm  that is often used for these applications in seated and outdoor walking  conditions, using a modiﬁed Emotiv device.

Communication and control remains one of the main envisioned use  cases for BCI research and development, albeit primarily in clinical con-  ditions, e.g. for patients who have lost other means of communication  with the outside world. For healthy participants, communication and  control is popular primarily for video games and neurofeedback. These  applications do not seem to require wireless EEG as such, but as virtual  reality becomes a more popular modality, wireless EEG becomes neces-  sary to allow for the freedom of movement that is an integral part of the  experience.

5. Discussion and outlook

We have surveyed a number of currently available wireless EEG de-  vices and published works. The search for devices was limited to those  obtained from the restricted literature search and an additional Inter-  net search. As such, it is unlikely to provide a complete picture of all  devices currently available. This is illustrative of the large number of  devices currently on the market, and thus the popularity of the ﬁeld. In  Table 1 and Fig. 2 , we see a wide range of devices oﬀering a large va-  riety of conﬁgurations for many diﬀerent use cases, with new electrode  designs and novel form factors overcoming issues identiﬁed in previous  generations. Alongside these hardware improvements, we also see an  increasing number of studies making use of the available hardware in a  number of diﬀerent ﬁelds.

To provide a comparison between devices, we listed in Table 1 ob-  jective criteria primarily related to the tangible properties of the device.

We would have liked, of course, to list what is perhaps the main criteria  that the reader may be interested in aside from the oﬀered freedom of  movement: the signal quality. While some relevant aspects can be in-  ferred to some extent from the objective criteria listed in Table 1 , signal  quality is ultimately highly dependent on the speciﬁc circumstances of  any given study: a purely frequency-based analysis of EEG, for example,  may not pose the same requirements as one that targets early evoked po-  tentials, and diﬀerent assessments of ‘quality’ would apply. Nonetheless,  it may be beneﬁcial for the ﬁeld to develop standardized testing proto-  cols to evaluate wireless EEG devices in order to allow clear side-by-side  comparisons. The ERP CORE resource, for example, includes standard-  ized paradigms and analysis pipelines optimized to elicit known event-  related potentials ( Kappenman et al., 2021 ). Such resources can be used  and extended to mobile settings, e.g. by comparing sitting, standing,  and walking conditions using the same device, along with a standard-  ized measure of signal quality, such as the recently proposed standard-  ized measurement error ( Luck et al., 2021 ). Separate protocols could  test for a device’s range. The absence of such protocols currently leaves  technical details such as those listed in Table 1 as the main basis for  comparison.

As we mentioned, however, Table 1 is in part based on self-reporting  of the manufacturers or licensed distributors, because the requested  information was not available from publicly available documentation.  Furthermore, the answers provided did not always correspond to the  questions asked. While we appreciate the desire to maintain close con-  tact with potential customers, we nonetheless urge all manufacturers to  transparently provide the details necessary to make an informed deci-  sion without obstruction, and oﬀer the columns of Table 1 as a suggested  list of characteristics.

With respect to communication from the manufacturers, we may also  brieﬂy return to the issue raised in Section 2 , as it remains important to  emphasize the mismatch between what may appear to be possible, and  what is actually possible. Historically, only researchers and clinicians  had access to devices capable of recording EEG. However, recently these  technologies have become available to the general public and are sold  directly to consumers. Easy-to-use EEG hardware, wireless or otherwise,  and accompanying marketing activities foster the imagination, but do  little to constrain the consumers’ creativity to what is physiologically  meaningful. Some vendors make multiple claims that are often not well  supported by research literature: Coates McCall et al. (2019) analyzed  the most common claims about commercial wearable neurotechnolo-  gies, and concluded that scientiﬁc evidence supporting utility, safety,  and eﬃcacy is rarely provided. As such, important ethical discourses and  regulatory frameworks are still lacking, even as the commercialization  of neurotechnology continues. We believe it is part of the manufacturers’  and distributors’ responsibility to inform the public of the possibilities  and limitations of their devices, especially to the extent that they en-  gage in direct-to-consumer practices, and provide ready-made metrics  of alleged cognitive or emotional states. Studies relying on such met-  rics should use a design that allows them to be validated before being  applied. In this work, we focused our literature search on journal pub-  lications with relatively high impact. As such, we attempted to select  studies that have undergone more rigorous peer review and achieved  peer recognition, and should thus be able to serve as examples to those  interested in wireless EEG research.

The diﬃculty we mentioned in the introduction, with respect to ﬁnd-  ing a common deﬁnition of the various wireless EEG devices, extended  to a diﬃculty in ﬁnding appropriate keywords to span the literature.  The chosen keywords ultimately reﬂected the previously chosen deﬁni-  tion of wireless EEG. This resulted in a relatively wide variety of results,  to which we intended to apply a measure of quality control: The ex-  clusion of conference contributions and focus on journal papers should  have resulted in publications subjected to a stronger peer review. The  ﬁnal selection metric, using the mean number of citations per year, is  admittedly imperfect, as, e.g., citations do not necessarily reﬂect qual-  ity and it excludes more recent papers from 2021. It was one of the

13

<!-- page 14 -->

G. Niso, E. Romero, J.T. Moreau et al.  NeuroImage 269 (2023) 119774

few metrics that could be automatically applied to the > 2000 search  results, however, and did allow us to focus on apparent high-impact  papers.

The sample of 110 selected papers illustrated that while clinical  applications, one of the traditional domains of EEG research, remain  strongly represented, they have been overtaken in prevalence by a cat-  egory of cognitive monitoring, in particular for applications that re-  quire increased mobility: the use of neurotechnology to detect speciﬁc  naturally-occuring mental states such as fatigue, engagement, or atten-  tion in real-life, unconstrained situations. These are investigated i.a.  in automotive, educational, and private contexts, as the advantages of  wireless EEG ﬁnally allow neurotechnology to leave well-controlled lab  environments. Clinical applications focus primarily on seizure detection  and sleep stage identiﬁcation, for which wireless EEG enables unobtru-  sive, long-term recordings at home. A ﬁnal category related to commu-  nication and control, where SSVEP, motor imagery, and P300 paradigms  were the main modalities of control, and were used primarily for gaming  or to manipulate robotics.

Our literature review has also revealed a high degree of variability  and omissions when reporting methodology and processing pipelines  (e.g. study design, data acquisition, preprocessing, statistics), making it  diﬃcult to perform metaanalysis and comparison of results across stud-  ies. Researchers are encouraged to follow reporting standards such as  the OHBM COBIDAS for MEG and EEG guidelines ( Pernet et al., 2020 ),  the Agreed Reporting Template for EEG Methodology - International  Standard (ARTEM-IS; Styles et al., 2021 ; Š o š ki ć et al., 2023 ), and the  good practices for reporting ERPs (e.g. N400 studies; Š o š ki ć et al., 2022 ).  Following such standards can facilitate a more comprehensive, auto-  mated review of the literature in the future. But it is not solely for the  sake of reviews that such standards are important. Neuroimaging re-  search in general has been aﬀected by what some call a ‘replication  crisis’ ( Poldrack et al., 2017 ; Shrout and Rodgers, 2018 ), referring to  diﬃculty or even inability to replicate published results. As a response,  in the ﬁeld of EEG initiatives such as #EEGManyLabs emerged, aiming to  replicate ﬁndings of inﬂuential EEG experiments ( Pavlov et al., 2021 ).  Also worth noting is that in the ﬁrst years of mobile EEG an encourag-  ing number of results were reproduced, e.g. ﬁndings related to auditory  oddball in gait ( Debener et al., 2012b ; De Vos et al., 2014 ; Scanlon et al.,  2019 ; Ladouce et al., 2019 ), or gait power modulations ( Rogers et al.,  2016 ; Troller-Renfree et al., 2021 ). Still, it should be remembered that  scientiﬁc facts, at least in the ﬁeld of neuroimaging, are rarely estab-  lished by single papers, but instead rely on the continued work by oth-  ers who validate and build upon earlier ﬁndings. Therefore, to enable  EEG research to be of lasting value, it is crucial to adhere to good sci-  entiﬁc practices, as e.g. collected in Niso, Krol et al. (2022) for EEG and  MEG, and to consider open and reproducible neuroimaging through-  out the whole research cycle ( Niso, Botvinik-Nezer et al., 2022 ). These  practices include among other things, the preregistration of experiments  ( Paul et al., 2021 ; Govaart et al., 2022 ), the accurate reporting of exper-  iment details using reporting guidelines such as COBIDAS ( Pernet et al.,  2020 ) and ARTEM-IS ( Styles et al., 2021 ), and the public sharing of stim-  ulus presentations, data, analysis pipelines and derivatives following e.g.  the FAIR guiding principles ( Wilkinson et al., 2016 ) of Findability, Ac-  cessibility, Interoperability and Reusability (using public repositories,  with persistent identiﬁers, standardized data and metadata, e.g. follow-  ing the Brain Imaging Data Structure, BIDS, and appropriate licences).  This also includes considerations of sample size, already referenced in  Section 4.1 .

Thus, keeping in mind some caveats, which any neuroimaging  modality has, the currently available wireless EEG hardware provides  a broad selection of possibilities, and the literature shows researchers  from a diverse set of backgrounds committed to providing the real-  world applications that are enabled by these new technologies. Closing  the loop, we are seeing short hardware development cycles immedi-  ately spurred on by these same research ﬁndings —to which we hope  the reader is now in a better position to add their own mark.

Ethics statement

This article did not involve any original data collection on partici-  pants and therefore no ethical approval was needed.

Declaration of Competing Interest

The authors declare that they have no known competing ﬁnancial  interests or personal relationships that could have appeared to inﬂuence  the work reported in this paper.

Credit authorship contribution statement

Guiomar Niso: Conceptualization, Data curation, Methodology, Vi-  sualization, Writing – original draft, Writing – review & editing. Elena  Romero: Conceptualization, Data curation, Writing – review & edit-  ing. Jeremy T. Moreau: Conceptualization, Writing – review & editing.  Alvaro Araujo: Conceptualization, Data curation, Writing – review &  editing. Laurens R. Krol: Conceptualization, Methodology, Writing – original draft, Writing – review & editing.

Data availability

No data was used for the research described in the article.

Funding

GN received ﬁnancial support through a postdoctoral fellowship  from the AXA Research Fund and a Ramon y Cajal grant (RYC2021-  033763-I) from the Spanish Government. ER work has been par-  tially supported by the Department of Research and Innovation of  Madrid Regional Authority , in the EMPATIA-CM research project (ref-  erence Y2018/TCS-5046 ) and ARTEMISA-CM-UC3M research project  ( 2020/00048/001 ). LRK was funded by Volkswagen Foundation. The  funders had no role in study design, data collection and analysis, deci-  sion to publish, or preparation of the manuscript. The authors thank the  manufacturers and vendors contacted for this manuscript. The authors  declare no competing ﬁnancial or non-ﬁnancial interests.

Acknowledgments

Authors would like to kindly thank the reviewers, in particular Stefan  Debener, for their insightful comments which helped to signiﬁcantly im-  prove the manuscript. Authors would also like to thank all cooperating  EEG system manufacturers and vendors for their help providing device  details.

Supplementary materials

Supplementary material associated with this article can be found, in  the online version, at doi: 10.1016/j.neuroimage.2022.119774 .

References

Ahn, J.W., Ku, Y., Kim, H.C., 2019. A novel wearable EEG and ECG recording system for

stress assessment. Sensors 19 (9). doi: 10.3390/s19091991 .  Al-Barrak, L., Kanjo, E., Younis, E.M.G., 2017. NeuroPlace: categorizing Urban places ac-

cording to mental states. PLoS One 12 (9), e0183890 .  Arnal, P.J., Thorey, V., Debellemaniere, E., Ballard, M.E., Hernandez, A.B., Guillot, A.,

Jourde, H., et al., 2020. The dreem headband compared to polysomnography  for electroencephalographic signal acquisition and sleep staging. Sleep 43 (11).  doi: 10.1093/sleep/zsaa097 .  Artoni, F., Fanciullacci, C., Bertolucci, F., Panarese, A., Makeig, S., Micera, S., Chisari, C.,

2017. Unidirectional brain to muscle connectivity reveals motor cortex control of leg  muscles during stereotyped walking. Neuroimage 159 (October), 403–416 .  Aspinall, P., Mavros, P., Coyne, R., Roe, J., 2015. The Urban brain: analysing outdoor

physical activity with mobile EEG. Br. J. Sports Med. 49 (4), 272–276 .  Athavipach, C., Pan-Ngum, S., Israsena, P., 2019. A wearable in-ear EEG device for emo-

tion monitoring. Sensors 19 (18). doi: 10.3390/s19184014 .

14

<!-- page 15 -->

G. Niso, E. Romero, J.T. Moreau et al.  NeuroImage 269 (2023) 119774

Badcock, N.A., Mousikou, P., Mahajan, Y., Lissa, P., Thie, J., McArthur, G., 2013. Val-

idation of the emotiv EPOC(®) EEG gaming system for measuring research quality  auditory ERPs. PeerJ 1 (February), e38 .  Banaei, M., Hatami, J., Yazdanfar, A., Gramann, K., 2017. Walking through architectural

spaces: the impact of interior forms on human brain dynamics. Front. Hum. Neurosci.  11 (September), 477 .  Bateson, A.D., Baseler, H.A., Paulson, K.S., Ahmed, F., Asghar, A.U.R., 2017. Categoriza-

tion of mobile EEG: a researcher’s perspective. Biomed. Res. Int. 2017 (December),  5496196 .  Berger, H., 1929. Über das Elektrenkephalogramm des Menschen. Archiv für Psychiatrie

und Nervenkrankheiten 87, 527–570 .  Beurskens, R., Steinberg, F., Antoniewicz, F., Wolﬀ, W., Granacher, U., 2016. Neural cor-

relates of dual-task walking: eﬀects of cognitive versus motor interference in young  adults. Neural Plast. 2016 (April), 8032180 .  Bevilacqua, D., Davidesco, I., Wan, L.U, Chaloner, K., Rowland, J., Ding, M., Poeppel, D.,

Dikker, S., 2019. Brain-to-brain synchrony and learning outcomes vary by studen-  t-teacher dynamics: evidence from a real-world classroom electroencephalography  study. J. Cogn. Neurosci. 31 (3), 401–411 .  Biasiucci, A., Franceschiello, B., Murray, M.M., 2019. Electroencephalography. Curr. Biol.

doi: 10.1016/j.cub.2018.11.052 .  Bigliassi, M., Galano, B.M., Lima-Silva, A.E., Bertuzzi, R., 2020. Eﬀects of mindfulness

on psychological and psychophysiological responses during self-paced walking. Psy-  chophysiology 57 (4), e13529 .  Blanco, J.A., Vanleer, A.C., Calibo, T.K., Firebaugh, S.L., 2019. Single-trial cognitive

stress classiﬁcation using portable wireless electroencephalography. Sensors 19 (3).  doi: 10.3390/s19030499 .  Bleichner, M.G., Debener, S., 2017. Concealed, unobtrusive ear-centered EEG acqui-

sition: cEEGrids for transparent EEG. Front. Hum. Neurosci. 0. doi: 10.3389/fn-  hum.2017.00163 .  Bleichner, M.G., Lundbeck, M., Selisky, M., Minow, F., Jäger, M., Emkes, R., Debener, S.,

Vos, M.D.E, 2015. Exploring miniaturized EEG electrodes for brain-computer inter-  faces. An EEG you do not see? Physiol. Rep. 3 (4). doi: 10.14814/phy2.12362 .  Blum, S., Jacobsen, N.S.J., Bleichner, M.G., Debener, S., 2019. A riemannian modiﬁcation

of artifact subspace reconstruction for EEG artifact handling. Front. Hum. Neurosci.  13 (April), 141 .  Bradford, J.C, Lukos, J.R., Ferris, D.P., 2016. Electrocortical activity distinguishes between

uphill and level walking in humans. J. Neurophysiol. 115 (2), 958–966 .  Button, K.S., Ioannidis, J.P.A., Mokrysz, C., Nosek, B.A., Flint, J., Robinson, E.S.J., Mu-

nafò, M.R., 2013. Power failure: why small sample size undermines the reliability of  neuroscience. Nat. Rev. Neurosci. 14 (5), 365–376 .  Calabrò, R.S., Naro, A., Russo, M., Bramanti, P., Carioti, L., Balletta, T., Buda, A., Man-

uli, A., Filoni, S., Bramanti, A., 2018. Shaping neuroplasticity by using powered ex-  oskeletons in patients with stroke: a randomized clinical trial. J. Neuroeng. Rehabil.  15 (1), 35 .  Casson, A.J., 2019. Wearable EEG and beyond. Biomed. Eng. Lett. 9 (1), 53–71 .  Caton, R., 1875. The electric currents of the brain. Br. Med. J. 2 (765), 278.

doi: 10.1136/bmj.2.765.257 .  Cervera, M.A., Soekadar, S.R., Ushiba, J., Millán, J.D.R., Liu, M., Birbaumer, N.,

Garipelli, G., 2018. Brain-computer interfaces for post-stroke motor rehabilitation:  a meta-analysis. Ann. Clin. Transl. Neurol. 5 (5), 651–663 .  Chen, X., Zhao, B., Wang, Y., Xu, S., Gao, X., 2018. Control of a 7-DOF robotic arm system

with an SSVEP-based BCI. Int. J. Neural Syst. 28 (8), 1850018 .  Chez, M.G., Chang, M., Krasne, V., Coughlan, C., Kominsky, M., Schwartz, A., 2006. Fre-

quency of epileptiform EEG abnormalities in a sequential screening of autistic patients  with no known clinical epilepsy from 1996 to 2005. Epilepsy Behav. 8 (1), 267–271  E&B .  Lin, C.T., Chang, C.J., Lin, B.S., Hung, S.H., Chao, C.F., Wang, I.J., 2010. A real-time wire-

less brain-computer interface system for drowsiness detection. IEEE Trans. Biomed.  Circuits Syst. 4 (4), 214–222 .  Chi, Y.U.M, Jung, T.P., Cauwenberghs, G., 2010. Dry-contact and noncontact biopotential

electrodes: methodological review. IEEE Rev. Biomed. Eng. 3, 106–119 .  Chi, Y.U.M, Wang, Y.T., Wang, Y., Maier, C., Jung, T.P., Cauwenberghs, G., 2012. Dry and

noncontact EEG sensors for mobile brain-computer interfaces. IEEE Trans. Neural Syst.  Rehabil. Eng. 20 (2), 228–235 A Publication of the IEEE Engineering in Medicine and  Biology Society .  Cicalese, P.A., Li, R., Ahmadi, M.B., Wang, C., Francis, J.T., Selvaraj, S., Schulz, P.E.,

Zhang, Y., 2020. An EEG-fNIRS hybridization technique in the four-class classiﬁcation  of Alzheimer’s disease. J. Neurosci. Methods 336 (April), 108618 .  Clarke, S., Karoly, P.J., Nurse, E., Seneviratne, U., Taylor, J., Knight-Sadler, R., Kerr, R.,

et al., 2021. Computer-assisted EEG diagnostic review for idiopathic generalized  epilepsy. Epilepsy Behav. 121 (Pt B), 106556 E&B .  Coates McCall, I., Lau, C., Minielly, N., Illes, J., 2019. Owning ethical innovation: claims

about commercial wearable brain technologies. Neuron 102 (4), 728–731 .  Cohen, M.X., 2017. Where does EEG come from and what does it mean? Trends Neurosci.

doi: 10.1016/j.tins.2017.02.004 .  Cohen, M.X., 2014. Analyzing Neural Time Series Data: Theory and Practice. MIT Press .  David Hairston, W., Whitaker, K.W., Ries, A.J., Vettel, J.M., Cortney Bradford, J., Ker-

ick, S.E., McDowell, K., 2014. Usability of four commercially-oriented EEG systems.  J. Neural Eng. 11 (4), 046018 .  Debellemaniere, E., Chambon, S., Pinaud, C., Thorey, V., Dehaene, D., Léger, D., Chen-

naoui, M., Arnal, P.J., Galtier, M.N., 2018. Performance of an ambulatory dry-EEG  device for auditory closed-loop stimulation of sleep slow oscillations in the home en-  vironment. Front. Hum. Neurosci. 12 (March), 88 .  Debener, S., Emkes, R., Vos, M.D.E, Bleichner, M., 2015. Unobtrusive ambulatory EEG us-

ing a smartphone and ﬂexible printed electrodes around the ear. Sci. Rep. 5 (Novem-  ber), 16743 .

Debener, S., Minow, F., Emkes, R., Gandras, K., de Vos, M., 2012a. How about taking

a low-cost, small, and wireless EEG for a walk? Psychophysiology 49 (11), 1617– 1621 .  Debener, S., Minow, F., Emkes, R., Gandras, K., de Vos, M., 2012b. How about taking a

low-cost, small, and wireless EEG for a walk? Psychophysiology 49 (11), 1617–1621 .  Dehais, F., Duprès, A., Blum, S., Drougard, N., Scannella, S., Roy, R.N., Lotte, F.,

2019. Monitoring pilot’s mental workload using ERPs and spectral power  with a six-dry-electrode EEG system in real ﬂight conditions. Sensors 19 (6).  doi: 10.3390/s19061324 .  De Sanctis, P., Butler, J.S., Malcolm, B.R., Foxe, J.J., 2014. Recalibration of inhibitory

control systems during walking-related dual-task interference: a mobile brain-body  imaging (MOBI) study. Neuroimage 94 (July), 55–64 .  De Vos, M., Gandras, K., Debener, S., 2014. Towards a truly mobile auditory brain-com-

puter interface: exploring the P300 to take away. Int. J. Psychophysiol. 91 (1), 46–53  Oﬃcial Journal of the International Organization of Psychophysiology .  De Vos, M., Kroesen, M., Emkes, R., Debener, S., 2014a. P300 speller BCI with a mobile

EEG system: comparison to a traditional ampliﬁer. J. Neural Eng. 11 (3), 036008 .  De Vos, M., Kroesen, M., Emkes, R., Debener, S., 2014b. P300 speller BCI with a mobile

EEG system: comparison to a traditional ampliﬁer. J. Neural Eng. 11 (3), 036008 .  Di Flumeri, G., Aricò, P., Borghini, G., Sciaraﬀa, N., Florio, ADi, Babiloni, F., 2019.

The dry revolution: evaluation of three diﬀerent EEG dry electrode types in terms  of signal spectral features, mental states classiﬁcation and usability. Sensors 19 (6).  doi: 10.3390/s19061365 .  Dikker, S., Wan, L.U, Davidesco, I., Kaggen, L., Oostrik, M., McClintock, J., Rowland, J.,

et al., 2017. Brain-to-brain synchrony tracks real-world dynamic group interactions  in the classroom. Curr. Biol. 27 (9), 1375–1380 .  Ding, X., Yue, X., Zheng, R., Bi, C., Li, D., Yao, G., 2019. Classifying major depression

patients and healthy controls using EEG, eye tracking and galvanic skin response data.  J. Aﬀect. Disord. 251 (May), 156–161 .  Djebbara, Z., Fich, L.B., Petrini, L., Gramann, K., 2019. Sensorimotor brain dynam-

ics reﬂect architectural aﬀordances. Proc. Nat. Acad. Sci. U.S.A. 116 (29), 14769– 14778 .  Donoghue, T., 2019. LISC: a python package for scientiﬁc literature collection and analy-

sis. J. Open Source Softw. doi: 10.21105/joss.01674 .  Dres, M., Younes, M., Rittayamai, N., Kendzerska, T., Telias, I., Grieco, D.L., Pham, T.,

et al., 2019. Sleep and pathological wakefulness at the time of liberation from me-  chanical ventilation (SLEEWE). A prospective multicenter physiological study. Am. J.  Respir. Crit. Care Med. 199 (9), 1106–1115 .  Eddy, B.S., Garrett, S.C., Rajen, S., Peters, B., Wiedrick, J., O’Connor, A., Renda, A., Hug-

gins, J.E., Fried-Oken, M., 2019. Trends in research participant categories and de-  scriptions in abstracts from the international BCI meeting Series, 1999 to 2016. Brain  Comput. Interfaces 6 (1-2), 13–24 (Abingdon, England) .  Fronso, S., Fiedler, P., Tamburro, G., Haueisen, J., Bertollo, M., Comani, S., 2019. Dry EEG

in sports sciences: a fast and reliable tool to assess individual alpha peak frequency  changes induced by physical eﬀort. Front. Neurosci. 13 (September), 982 .  Golnar-Nik, P., Farashi, S., Safari, M.S., 2019. The application of EEG power for the predic-

tion and interpretation of consumer decision-making: a neuromarketing study. Phys-  iol. Behav. 207 (August), 90–98 .  Gonzalez Viejo, C., Fuentes, S., Howell, K., Torrico, D.D., Dunshea, F.R., 2019. Integration

of non-invasive biometrics with sensory analysis techniques to assess acceptability of  beer by consumers. Physiol. Behav. 200 (March), 139–147 .  Govaart, G.H., Schettino, A., Helbling, S., Mehler, D.M.A., Ngiam, W.X.Q., Moreau, D.,

… Paul, M., et al., 2022. EEG ERP Preregistration Template. MetaArXiv  doi: 10.31222/osf.io/4nvpt .  Gramann, K., Ferris, D.P., Gwin, J., Makeig, S., 2014. Imaging natural cognition in action.

Int. J. Psychophysiol. doi: 10.1016/j.ijpsycho.2013.09.003 .  Gramann, K., Gwin, J.T., Bigdely-Shamlo, N., Ferris, D.P., Makeig, S., 2010. Visual evoked

responses during standing and walking. Front. Hum. Neurosci. 4 (October), 202 .  Gramann, K., Jung, T.P., Ferris, D.P., Lin, C.T., Makeig, S., 2014. Towards a New Cognitive

Neuroscience: Modeling Natural Brain Dynamics. Frontiers E-books .  Grønli, J., Byrkjedal, I.K., Bjorvatn, B., Nødtvedt, Ø., Hamre, B., Pallesen, S., 2016. Read-

ing from an iPad or from a book in bed: the impact on human sleep. A randomized  controlled crossover trial. Sleep Med. 21 (May), 86–92 .  Gu, Y., Cleeren, E., Dan, J., Claes, K., Paesschen, W.V., Huﬀel, S.V., Hunyadi, B.,

2017. Comparison between scalp EEG and behind-the-ear EEG for development of  a wearable seizure detection system for patients with focal epilepsy. Sensors 18 (1).  doi: 10.3390/s18010029 .  Gwin, J.T., Gramann, K., Makeig, S., Ferris, D.P., 2010. Removal of movement artifact

from high-density EEG recorded during walking and running. J. Neurophysiol. 103  (6), 3526–3534 .  Haar, S., Faisal, A.A, 2020. Brain activity reveals multiple motor-learning mechanisms in

a real-world task. Front. Hum. Neurosci. 14 (September), 354 .  Hashemi, A., Pino, L.J., Moﬀat, G., Mathewson, K.J., Aimone, C., Bennett, P.J.,

Schmidt, L.A., Sekuler, A.B., 2016. Characterizing population EEG dynamics through-  out adulthood. eNeuro (6) 3. doi: 10.1523/ENEURO.0275-16.2016 .  Hinrichs, H., Scholz, M., Baum, A.K., Kam, J.W.Y., Knight, R.T., Heinze, H.J., 2020. Com-

parison between a wireless dry electrode EEG system with a conventional wired wet  electrode EEG system for clinical applications. Sci. Rep. 10 (1), 1–14 .  Holdgraf, C., Appelhoﬀ, S., Bickel, S., Bouchard, K., D’Ambrosio, S., David, O., Devin-

sky, O., et al., 2019. iEEG-BIDS, extending the brain imaging data structure speciﬁca-  tion to human intracranial electrophysiology. Sci. Data 6 (1), 102 .  Hölle, D., Meekes, J., Bleichner, M.G., 2021. Mobile ear-EEG to study auditory attention

in everyday life: auditory attention in everyday life. Behav. Res. Methods 53 (5),  2025–2036 .  Holm, A., Lukander, K., Korpela, J., Sallinen, M., Müller, K.M.I., 2009. Estimating brain

load from the EEG. Sci. World J. 9 (July), 639–651 .

15

<!-- page 16 -->

G. Niso, E. Romero, J.T. Moreau et al.  NeuroImage 269 (2023) 119774

Huigen, E., Peper, A., Grimbergen, C.A., 2002. Investigation into the origin of the noise

of surface electrodes. Med. Biol. Eng. Comput. 40 (3), 332–338 .  Changkyun, I.M, Seo, J.M.O, 2016. A review of electrodes for the electrical brain signal

recording. Biomed. Eng. Lett. doi: 10.1007/s13534-016-0235-1 .  Ives, J.R., Woods, J.F., 1975. 4-channel 24 hour cassette recorder for long-term eeg mon-

itoring of ambulatory patients. Electroencephalogr. Clin. Neurophysiol. 39 (1), 88– 92 .  Jackson, A.F., Bolger, D.J., 2014. The neurophysiological bases of EEG and EEG measure-

ment: a review for the rest of Us. Psychophysiology 51 (11), 1061–1071 .  Jacobsen, N.S.J., Blum, S., Witt, K., Debener, S., 2021. A walk in the park?

Characterizing gait-related artifacts in mobile EEG recordings. Eur. J. Neurosci.  doi: 10.1111/ejn.14965 .  Jamil, N., Belkacem, A.N., Ouhbi, S., Lakas, A., 2021. Noninvasive Electroencephalogra-

phy Equipment for Assistive, Adaptive, and Rehabilitative Brain–Computer Interfaces:  A Systematic Literature Review. Sensors 21 (14), 4754. doi: 10.3390/s21144754 .  Jebelli, H., Khalili, M.M., Lee, S., 2019. A continuously updated, computationally eﬃ-

cient stress recognition framework using electroencephalogram (EEG) by applying  online multitask learning algorithms (OMTL). IEEE J. Biomed. Health Inform. 23 (5),  1928–1939 .  Kam, J.W.Y., Griﬃn, S., Shen, A., Patel, S., Hinrichs, H., Heinze, H.J., Deouell, L.Y.,

Knight, R.T., 2019. Systematic comparison between a wireless EEG system  with dry electrodes and a wired EEG system with wet electrodes. Neuroimage  doi: 10.1016/j.neuroimage.2018.09.012 .  Kappenman, E.S., Farrens, J.L., Zhang, W., Stewart, A.X., Luck, S.J., 2021. ERP CORE: an

open resource for human event-related potential research. Neuroimage 225 (January),  117465 .  Kassab, A., Lan, J., Tremblay, J., Vannasing, P., Dehbozorgi, M., Pouliot, P., Gallagher, A.,

Lesage, F., Sawan, M., Nguyen, D.K., 2018. Multichannel wearable fNIRS-EEG system  for long-term clinical monitoring. Hum. Brain Mapp. 39 (1), 7–23 .  Katsigiannis, S., Ramzan, N., 2018. DREAMER: a database for emotion recognition through

EEG and ECG signals from wireless low-cost oﬀ-the-shelf devices. IEEE J. Biomed.  Health Inform. 22 (1), 98–107 .  Kilicarslan, A., Grossman, R.G., Contreras-Vidal, J.L., 2016. A robust adaptive denoising

framework for real-time artifact removal in scalp EEG measurements. J. Neural Eng.  13 (2), 026013 .  Kim, J.H., Hwang, J.Y., Hwang, H.R., Kim, H.S., Lee, J.H., Seo, J.W., Sang Shin, U.,

Lee, S.H., 2018. Simple and cost-eﬀective method of highly conductive and elastic  carbon nanotube/polydimethylsiloxane composite for wearable electronics. Sci. Rep.  8 (1), 1375 .  Klug, M., Gramann, K., 2021. Identifying key factors for improving ICA-based decompo-

sition of EEG data in mobile and stationary experiments. Eur. J. Neurosci. 54 (12),  8406–8420 .  Klug, M., Kloosterman, N.A., 2022. Zapline-plus: A Zapline extension for automatic and

adaptive removal of frequency-speciﬁc noise artifacts in M/EEG. Human Brain Map-  ping 43 (9), 2743–2758. doi: 10.1002/hbm.25832 .  Krigolson, O.E., Williams, C.C., Norton, A., Hassall, C.D., Colino, F.L., 2017. Choosing

MUSE: validation of a low-cost, portable EEG system for ERP research. Front. Neu-  rosci. 11 (March), 109 .  Krol, L.R., Andreessen, L.M., Zander, T.O., 2018. Passive brain-computer interfaces: A

perspective on increased interactivity. In: Nam, C.S., Nijholt, A., Lotte, F. (Eds.), Brain-  computer interfaces handbook: Technological and theoretical advances. CRC Press,  Boca Raton, FL, USA, pp. 69–86. doi: 10.1201/9781351231954-3 .  Kwak, N.S, Müller, K.R., Lee, S.W., 2017. A convolutional neural network for steady state

visual evoked potential classiﬁcation under ambulatory environment. PLoS One 12  (2), e0172578 .  Ladouce, S., Donaldson, D.I., Dudchenko, P.A., Ietswaart, M., 2019. Mobile EEG identiﬁes

the re-allocation of attention during real-world activity. Sci. Rep. 9 (1), 15851 .  Laszlo, S., Ruiz-Blondet, M., Khaliﬁan, N., Chu, F., Jin, Z., 2014. A direct comparison of

active and passive ampliﬁcation electrodes in the same ampliﬁer system. J. Neurosci.  Methods 235 (September), 298–307 .  La, T.G., Qiu, S., Scott, D.K., Bakhtiari, R., Kuziek, J.W.P., Mathewson, K.E., Rieger, J.,

Chung, H.J., 2018. Two-layered and stretchable e-textile patches for wearable health-  care electronics. Adv. Healthc. Mater. 7 (22), e1801033 .  Lee, B.G., Lee, B.L., Chung, W.Y., 2014. Mobile healthcare for automatic driving sleep-

-onset detection using wavelet-based EEG and respiration signals. Sensors 14 (10),  17915–17936 .  Lee, N., Broderick, A.J., Chamberlain, L., 2007. What Is ‘neuromarketing’? A discussion

and agenda for future research. Int. J. Psychophysiol. 63 (2), 199–204 Oﬃcial Journal  of the International Organization of Psychophysiology .  Leminen, M.M., Virkkala, J., Saure, E., Paajanen, T., Zee, P.C., Santostasi, G., Hublin, C.,

et al., 2017. Enhanced memory consolidation via automatic sound stimulation during  Non-REM sleep. Sleep 40 (3). doi: 10.1093/sleep/zsx003 .  Levendowski, D.J., Ferini-Strambi, L., Gamaldo, C., Cetel, M., Rosenberg, R., West-

brook, P.R., 2017. The accuracy, night-to-night variability, and stability of frontopolar  sleep electroencephalography biomarkers. J. Clin. Sleep Med. 13 (6), 791–803 JCSM:  Oﬃcial Publication of the American Academy of Sleep Medicine .  Liao, L.D., Chen, C.Y., Wang, I.J., Chen, S.F., Li, S.Y., Chen, B.W., Chang, J.Y., Lin, C.T.,

2012. Gaming control using a wearable and wireless EEG-based brain-computer in-  terface device with novel dry foam-based sensors. J. Neuroeng. Rehabil. 9 (January),  5 .  Li, G., Wu, J., Xia, Y., Wu, Y., Tian, Y., Liu, J., Chen, D., He, Q., 2020. Towards emerging

EEG applications: a novel printable ﬂexible Ag/AgCl dry electrode array for robust  recording of EEG signals at forehead sites. J. Neural Eng. 17 (2), 026001 .  Lin, C.T., Chuang, C.H., Huang, C.S., Tsai, S.F., Lu, S.W., Chen, Y.H., Ko, L.W, 2014. Wire-

less and wearable EEG system for evaluating driver vigilance. IEEE Trans. Biomed.  Circuits Syst. 8 (2), 165–176 .

Lin, W., Chen, Q., Jiang, M., Tao, J., Liu, Z., Zhang, X., Wu, L., Xu, S., Kang, Y., Zeng, Q.,

2020. Sitting or walking? Analyzing the neural emotional indicators of urban green  space behavior with mobile EEG. J. Urban Health Bull. N. Y. Acad. Med. 97 (2),  191–203 .  Liu, N.H., Chiang, C.Y., Chu, H.C., 2013. Recognizing the degree of human attention using

EEG signals from mobile sensors. Sensors 13 (8), 10273–10286 .  Lopez-Gordo, M., Sanchez-Morillo, D., Valle, F., 2014. Dry EEG electrodes. Sensors

doi: 10.3390/s140712847 .  López-Larraz, E., Trincado-Alonso, F., Rajasekaran, V., Pérez-Nombela, S., Del-Ama, A.J.,

Aranda, J., Minguez, J., Gil-Agudo, A., Montesano, L., 2016. Control of an ambulatory  exoskeleton with a brain-machine interface for spinal cord injury gait rehabilitation.  Front. Neurosci. 10 (August), 359 .  Lotte, F., Bougrain, L., Cichocki, A., Clerc, M., Congedo, M., Rakotomamonjy, A., Yger, F.,

2018. A review of classiﬁcation algorithms for EEG-based brain-computer interfaces:  a 10 year update. J. Neural Eng. 15 (3), 031005 .  Lucey, B.P., Mcleland, J.S., Toedebusch, C.D., Boyd, J., Morris, J.C., Landsness, E.C., Ya-

mada, K., Holtzman, D.M., 2016. Comparison of a single-channel EEG sleep study to  polysomnography. J. Sleep. Res. 25 (6), 625–635 .  Luck, S.J., 2014. An Introduction to the Event-Related Potential Technique, 2nd ed. MIT

Press .  Luck, S.J., Stewart, A.X., Simmons, A.M., Rhemtulla, M., 2021. Standardized measure-

ment error: a universal metric of data quality for averaged event-related potentials.  Psychophysiology 58 (6), e13793 .  Luu, T.P., He, Y., Brown, S., Nakagame, S., Contreras-Vidal, J.L., 2016. Gait adaptation to

visual kinematic perturbations using a real-time closed-loop brain-computer interface  to a virtual reality avatar. J. Neural Eng. 13 (3), 036006 .  Ma, J., Zhang, Y.U, Cichocki, A., Matsuno, F., 2015. A novel EOG/EEG hybrid human-ma-

chine interface adopting eye movements and ERPs: application to robot control. IEEE  Trans. Biomed. Eng. 62 (3), 876–889 .  Makeig, S., Gramann, K., Jung, T.P., Sejnowski, T.J., Poizner, H., 2009. Linking brain,

mind and behavior. Int. J. Psychophysiol. doi: 10.1016/j.ijpsycho.2008.11.008 .  Makeig, S., Jung, T.-P., Bell, A.J., Sejnowski, T.J., 1996. Independent component analy-

sis of electroencephalographic data. In: Touretzky, D.S., Mozer, M.C., Hasselmo, M.E.  (Eds.), Advances in Neural Information Processing Systems, Vol. 8. MIT Press, Cam-  bridge, MA, USA, pp. 145–151 .  Malcolm, B.R., Foxe, J.J., Butler, J.S., Sanctis, P.D.E, 2015. The aging brain shows less ﬂex-

ible reallocation of cognitive resources during dual-task walking: a mobile brain/body  imaging (MoBI) study. Neuroimage 117 (August), 230–242 .  Marín-Morales, J., Higuera-Trujillo, J.L., Greco, A., Guixeres, J., Llinares, C., Scilingo, E.P.,

Alcañiz, M., Valenza, G., 2018. Aﬀective computing in virtual reality: emotion recog-  nition from brain and heartbeat dynamics using wearable sensors. Sci. Rep. 8 (1),  13657 .  Martins, I.P., Westerﬁeld, M., Lopes, M., Maruta, C., Gil-da-Costa, R., 2020. Brain state

monitoring for the future prediction of migraine attacks. Cephalalgia 40 (3), 255–265  An International Journal of Headache .  Mathewson, K.E., Harrison, T.J.L., Kizuk, S.A.D., 2017. High and dry? comparing active

dry EEG electrodes to active and passive wet electrodes. Psychophysiology 54 (1),  74–82 .  Melnik, A., Legkov, P., Izdebski, K., Kärcher, S.M., David Hairston, W., Ferris, D.P.,

König, P., 2017. Systems, subjects, sessions: to what extent do these factors inﬂuence  EEG data? Front. Hum. Neurosci. 11 (March), 150 .  Mihajlovic, V., Grundlehner, B., Vullers, R., Penders, J., 2015. Wearable, wireless EEG so-

lutions in daily life applications: what are we missing? IEEE J. Biomed. Health Inform.  19 (1), 6–21 .  Mikkelsen, K.B., Ebajemito, J.K., Bonmati-Carrion, M.A., Santhi, N., Revell, V.L., At-

zori, G., Monica, C.D., et al., 2019. Machine-learning-derived sleep-wake staging from  around-the-ear electroencephalogram outperforms manual scoring and actigraphy. J.  Sleep Res. 28 (2), e12786 .  Mikkelsen, K.B., Kappel, S.L., Mandic, D.P., Kidmose, P., 2015. EEG recorded from the

ear: characterizing the Ear-EEG method. Front. Neurosci. 9 (November), 438 .  Mirkovic, B., Bleichner, M.G., Vos, M.D.E, Debener, S., 2016. Target speaker detection

with concealed EEG around the ear. Front. Neurosci. 10 (July), 349 .  Morales, J.M., Díaz-Piedra, C., Rieiro, H., Roca-González, J., Romero, S., Catena, A.,

Fuentes, L.J., Di Stasi, L.L., 2017. Monitoring driver fatigue using a single-channel  electroencephalographic device: a validation study by gaze-based, driving perfor-  mance, and subjective data. Accid. Anal. Prev. 109 (December), 62–69 .  Mullen, T.R., Kothe, C.A.E., Chi, Y.M., Ojeda, A., Kerth, T., Makeig, S., Jung, T.P., Cauwen-

berghs, G., 2015. Real-time neuroimaging and cognitive monitoring using wearable  dry EEG. IEEE Trans. Biomed. Eng. 62 (11), 2553–2567 .  Mustile, M., Kourtis, D., Ladouce, S., Learmonth, G., Edwards, M.G., Donaldson, D.I.,

Ietswaart, M., 2021. Mobile EEG reveals functionally dissociable dynamic processes  supporting real-world ambulatory obstacle avoidance: evidence for early proactive  control. Eur. J. Neurosci. 54 (12), 8106–8119 .  Nakamura, T., Alqurashi, Y.D., Morrell, M.J., Mandic, DP., 2020. Hearables: automatic

overnight sleep monitoring with standardized in-ear EEG sensor. IEEE Trans. Biomed.  Eng. 67 (1), 203–212 .  Narayanan, A.M., Bertrand, A., 2020. Analysis of miniaturization eﬀects and channel se-

lection strategies for EEG sensor networks with application to auditory attention de-  tection. IEEE Trans. Biomed. Eng. 67 (1), 234–244 .  Nathan, K., Contreras-Vidal, J.L., 2015. Negligible motion artifacts in scalp

electroencephalography (EEG) during treadmill walking. Front. Hum. Neurosci.  9, 708 .  Neale, C., Aspinall, P., Roe, J., Tilley, S., Mavros, P., Cinderby, S., Coyne, R., Thin, N.,

Bennett, G., Thompson, C.W., 2017. The aging Urban brain: analyzing outdoor phys-  ical activity using the emotiv aﬀectiv suite in older people. J. Urban Health Bull. N.  Y. Acad. Med. 94 (6), 869–880 .

16

<!-- page 17 -->

G. Niso, E. Romero, J.T. Moreau et al.  NeuroImage 269 (2023) 119774

Niso, G., Botvinik-Nezer, R., Appelhoﬀ, S., De La Vega, A., Esteban, O., Etzel, J.A., …

Rieger, J.W., 2022. Open and reproducible neuroimaging: from study inception to  publication. NeuroImage 119623 .  Niso, G., Gorgolewski, K.J., Bock, E., Brooks, T.L., Flandin, G., Gramfort, A., Henson, R.N.,

et al., 2018. MEG-BIDS, the brain imaging data structure extended to magnetoen-  cephalography. Sci. Data 5 (June), 180110 .  Niso, G., Krol, L.R., Combrisson, E., Dubarry, A.S., Elliott, M.A., François, C., Héj-

ja-Brichard, Y., et al., 2022. Good scientiﬁc practice in MEEG research: progress and  perspectives. Neuroimage, 119056 March .  Nordin, A.D., Hairston, W.D, Ferris, D.P., 2019. Human electrocortical dynamics while

stepping over obstacles. Sci. Rep. 9 (1), 4693 .  Nordin, A.D., Hairston, W.D, Ferris, D.P., 2020. Faster gait speeds reduce alpha and beta

EEG spectral power from human sensorimotor cortex. IEEE Trans. Biomed. Eng. 67  (3), 842–853 .  Nyquist, H., 1928. Certain topics in telegraph transmission theory. Trans. Am. Inst. Electr.

Eng. doi: 10.1109/t-aiee.1928.5055024 .  Oliveira, A.S., Schlink, B.R., David Hairston, W., König, P., Ferris, D.P., 2016. Proposing

metrics for benchmarking novel EEG technologies towards real-world measurements.  Front. Hum. Neurosci. 10 (May), 188 .  Packheiser, J., Schmitz, J., Pan, Y., Basbasse, Y.E.L., Friedrich, P., Güntürkün, O., Ocklen-

burg, S., 2020. Using mobile EEG to investigate alpha and beta asymmetries during  hand and foot use. Front. Neurosci. 14 (February), 109 .  Page, M.J., McKenzie, J.E., Bossuyt, P.M., Boutron, I., Hoﬀmann, T.C., Mulrow, C.D.,

Shamseer, L., et al., 2021. The PRISMA 2020 statement: an updated guideline for  reporting systematic reviews. BMJ 372 (March) n71 .  Parasuraman, R., 2003. Neuroergonomics: research and practice. Theor. Issues Ergon. 4

(1-2), 5–20 .  Paul, M., Govaart, G.H., Schettino, A., 2021. Making ERP research more transparent:

guidelines for preregistration. Int. J. Psychophysiol. 164 (June), 52–63 Oﬃcial Jour-  nal of the International Organization of Psychophysiology .  Pavlov, Y.G., Adamian, N., Appelhoﬀ, S., Arvaneh, M., Benwell, C.S.Y., Beste, C.,

Bland, A.R., et al., 2021. #EEGManyLabs: investigating the replicability of inﬂuen-  tial EEG experiments. Cortex 144 (November), 213–229 .  Pernet, C., Garrido, M.I., Gramfort, A., Maurits, N., Michel, C.M., Pang, E., Salmelin, R.,

Schoﬀelen, J.M., Valdes-Sosa, P.A., Puce, A., 2020. Issues and recommendations from  the OHBM COBIDAS MEEG committee for reproducible EEG and MEG research. Nat.  Neurosci. doi: 10.1038/s41593-020-00709-0 , September .  Pernet, C.R., Appelhoﬀ, S., Gorgolewski, K.J., Flandin, G., Phillips, C., Delorme, A., Oost-

enveld, R., 2019. EEG-BIDS, an extension to the brain imaging data structure for elec-  troencephalography. Sci. Data 6 (1), 103 .  Piñeyro Salvidegoitia, M., Jacobsen, N., Bauer, A.K.R., Griﬃths, B., Hanslmayr, S.,

Debener, S., 2019. Out and about: subsequent memory eﬀect captured in a natural  outdoor environment with smartphone EEG. Psychophysiology 56 (5), e13331 .  Poldrack, R.A., Baker, C.I., Durnez, J., Gorgolewski, K.J., Matthews, P.M., Munafò, M.R.,

Nichols, T.E., Poline, J.B., Vul, E., Yarkoni, T., 2017. Scanning the horizon: towards  transparent and reproducible neuroimaging research. Nat. Rev. Neurosci. 18 (2),  115–126 .  Poulsen, A.T., Kamronn, S., Dmochowski, J., Parra, L.C., Hansen, L.K., 2017. EEG in

the classroom: synchronized neural recordings during video presentation. Sci. Rep.  7 (March), 43916 .  Radüntz, T., 2018. Signal quality evaluation of emerging EEG devices. Front. Physiol. 9

(February), 98 .  Raheel, A., Majid, M., Alnowami, M., Anwar, S.M., 2020. Physiological sensors based

emotion recognition while experiencing tactile enhanced multimedia. Sensors 20 (14).  doi: 10.3390/s20144037 .  Reiser, J.E., Wascher, E., Arnau, S., 2019. Recording mobile EEG in an Outdoor environ-

ment reveals cognitive-motor interference dependent on movement complexity. Sci.  Rep. 9 (1), 13086 .  Reiser, J.E., Wascher, E., Rinkenauer, G., Arnau, S., 2021. Cognitive-motor interference in

the wild: assessing the eﬀects of movement complexity on task switching using mobile  EEG. Eur. J. Neurosci. 54 (12), 8175–8195 .  Rogers, J.M., Johnstone, S.J., Aminov, A., Donnelly, J., Wilson, P.H., 2016. Test-retest re-

liability of a single-channel, wireless EEG system. Int. J. Psychophysiol. 106 (August),  87–96 Oﬃcial Journal of the International Organization of Psychophysiology .  Scanlon, J.E.M., Jacobsen, N.S.J., Maack, M.C., Debener, S., 2021. Does the electrode am-

pliﬁcation style matter? A comparison of active and passive EEG system conﬁgurations  during standing and walking. Eur. J. Neurosci. doi: 10.1111/ejn.15037 .  Scanlon, J.E.M., Townsend, K.A., Cormier, D.L., Kuziek, J.W.P., Mathewson, K.E., 2019.

Taking oﬀthe training wheels: measuring auditory P3 during outdoor cycling using  an active wet EEG system. Brain Res. 1716 (August), 50–61 .  Scott, H., Lack, L., Lovato, N., 2020. A systematic review of the accuracy of sleep wearable

devices for estimating sleep onset. Sleep Med. Rev. 49 (February), 101227 .  Shad, E.H.T., Molinas, M., Ytterdal, T., 2020. Impedance and noise of passive and active

Dry EEG electrodes: a review. IEEE Sens. J. doi: 10.1109/jsen.2020.3012394 .  Shao, L., Zhang, L., Belkacem, A.N., Zhang, Y., Chen, X., Li, J., Liu, H., 2020. EEG-con-

trolled wall-crawling cleaning robot using SSVEP-based brain-computer interface. J.  Healthc. Eng. 2020 (January), 6968713 .  Shrout, P.E., Rodgers, J.L., 2018. Psychology, science, and knowledge construction: broad-

ening perspectives from the replication crisis. Annu. Rev. Psychol. 69 (January),  487–510 .  Shustak, S., Inzelberg, L., Steinberg, S., Rand, D., Pur, M.D., Hillel, I., Katzav, S., et al.,

2019. Home monitoring of sleep with a temporary-tattoo EEG, EOG and EMG elec-  trode array: a feasibility study. J. Neural Eng. 16 (2), 026024 .  Si-Mohammed, H., Petit, J., Jeunet, C., Argelaguet, F., Spindler, F., Evain, A., Roussel, N.,

Casiez, G., Lecuyer, A., 2020. Towards BCI-based interfaces for augmented reality:  feasibility, design and evaluation. IEEE Trans. Vis. Comput. Graph. 26 (3), 1608–1621 .

Simons, S., Espino, P., Abásolo, D., 2018. Fuzzy entropy analysis of the electroencephalo-

gram in patients with Alzheimer’s disease: is the method superior to sample entropy?  Entropy 20 (1). doi: 10.3390/e20010021 .  Snyder, K.L., Kline, J.E., Huang, H.J., Ferris, D.P., 2015. Independent component analy-

sis of gait-related movement artifact recorded using EEG electrodes during treadmill  walking. Front. Hum. Neurosci. 9 (December), 639 .  Soekadar, S.R., Birbaumer, N., Slutzky, M.W., Cohen, L.G., 2015. Brain-machine interfaces

in neurorehabilitation of stroke. Neurobiol. Dis. 83 (November), 172–179 .  Solis-Escalante, T., Cruijsen, J., Kam, D., Kordelaar, J., Weerdesteyn, V., Schouten, A.C.,

2019. Cortical dynamics during preparation and execution of reactive balance re-  sponses with distinct postural demands. Neuroimage 188 (March), 557–571 .  Š o š ki ć, A., Jovanovi ć, V., Styles, S.J., et al., 2022. How to do better N400 studies: Repro-

ducibility, consistency and adherence to research standards in the existing literature.  Neuropsychol Rev 32, 577–600. doi: 10.1007/s11065-021-09513-4 .  So, W.K.Y., Wong, S.W.H., Mak, J.N., Chan, R.H.M., 2017. An evaluation of mental work-

load with frontal EEG. PLoS One 12 (4), e0174949 .  Š o š ki ć, A., Kovic, V., Algermissen, J., Fischer, N.L., Ganis, G., Gau, R., … Styles, S.J.,

2023. ARTEM-IS for ERP: Agreed Reporting Template for EEG Methodology  - International Standard for documenting studies on Event-Related Potentials  doi: 10.31234/osf.io/mq5sy .  Styles, S.J., Kovi ć, V., Ke, H., Š o š ki ć, A., 2021. Towards ARTEM-IS: design guidelines

for evidence-based EEG methodology reporting tools. Neuroimage 245 (December),  118721 .  Taheri, B.A., Knight, R.T., Smith, R.L., 1994. A dry electrode for EEG recording. Electroen-

cephalogr. Clin. Neurophysiol. 90 (5), 376–383 .  Tassinary, L.G., Cacioppo, J.T., 1992. Unobservable facial actions and emotion. Psychol.

Sci. doi: 10.1111/j.1467-9280.1992.tb00252.x .  Thapa, N., Park, H.J., Yang, J.G., Son, H., Jang, M., Lee, J., Wan Kang, S., Won Park, K.,

Park, H., 2020. The eﬀect of a virtual reality-based intervention program on cognition  in older adults with mild cognitive impairment: a randomized control trial. J. Clin.  Med. Res. 9 (5). doi: 10.3390/jcm9051283 .  Thompson, T., Steﬀert, T., Ros, T., Leach, J., Gruzelier, J., 2008. EEG applications for sport

and performance. Methods 45 (4), 279–288 .  Titgemeyer, Y., Surges, R., Altenmüller, D.M., Fauser, S., Kunze, A., Lanz, M., Malter, MP.,

et al., 2020. Can commercially available wearable EEG devices be used for diagnostic  purposes? An explorative pilot study. Epilepsy Behav. 103 (Pt A), 106507 E&B .  Topalovic, U., Aghajan, Z.M., Villaroman, D., Hiller, S., Christov-Moore, L., Wishard, T.J.,

Stangl, M., et al., 2020. Wireless programmable recording and stimulation of deep  brain activity in freely moving humans. Neuron 108 (2), 322–334 e9 .  Tortora, S., Ghidoni, S., Chisari, C., Micera, S., Artoni, F., 2020. Deep learning-based BCI

for gait decoding from EEG with LSTM recurrent neural network. J. Neural Eng. 17  (4), 046011 .  Troller-Renfree, S.V., Morales, S., Leach, S.C., Bowers, M.E., Debnath, R., Fifer, W.P.,

Fox, N.A., Noble, K.G., 2021. Feasibility of assessing brain activity using mobile, in-  home collection of electroencephalography: methods and analysis. Dev. Psychobiol.  63 (6), e22128 .  Vandecasteele, K., Cooman, T.D.E., Dan, J., Cleeren, E., Huﬀel, S.V., Hunyadi, B., Paess-

chen, W.V., 2020. Visual seizure annotation and automated seizure detection using  behind-the-ear electroencephalographic channels. Epilepsia 61 (4), 766–775 .  Vidal, J.J., 1977. Real-time detection of brain events in EEG. Proc. IEEE

doi: 10.1109/proc.1977.10542 .  Wilkinson, M.D., Dumontier, M., Jan Aalbersberg, I.J, Appleton, G., Axton, M., Baak, A.,

Blomberg, N., et al., 2016. The FAIR guiding principles for scientiﬁc data management  and stewardship. Sci. Data 3 (March), 160018 .  Wolpaw, J.R., Birbaumer, N., McFarland, D.J., Pfurtscheller, G., Vaughan, T.M., 2002.

Brain-computer interfaces for communication and control. Clin. Neurophysiol. 113  (6), 767–791 Oﬃcial Journal of the International Federation of Clinical Neurophysi-  ology .  Zander, T.O., Andreessen, L.M., Berg, A., Bleuel, M., Pawlitzki, J., Zawallich, L., Krol, L.R.,

Gramann, K., 2017. Evaluation of a dry EEG system for application of passive  brain-computer interfaces in autonomous driving. Front. Hum. Neurosci. 11 (Febru-  ary), 78 .  Zander, T.O., Kothe, C., 2011. Towards passive brain-computer interfaces: applying brain–

computer interface technology to human-machine systems in general. J. Neural Eng.  8 (2), 025005 .  Zander, T.O., Krol, L.R., Birbaumer, N.P., Gramann, K., 2016. Neuroadaptive technology

enables implicit cursor control based on medial prefrontal cortex activity. Proc. Nat.  Acad. Sci. U.S.A. 113 (52), 14898–14903 .  Zhang, D., Yao, L., Chen, K., Wang, S., Chang, X., Liu, Y., 2020. Making sense of spa-

tio-temporal preserving representations for EEG-based human intention recognition.  IEEE Trans. Cybern. 50 (7), 3033–3044 .  Zhang, J., Wang, B., Zhang, C., Xiao, Y., Wang, M.Y.U., 2019. An EEG/EMG/EOG-based

multimodal human-machine interface to real-time control of a soft robot hand. Front.  Neurorobot. 13 (March), 7 .  Zhang, X., Li, J., Liu, Y., Zhang, Z., Wang, Z., Luo, D., Zhou, X., et al., 2017. Design of

a fatigue detection system for high-speed trains based on driver vigilance using a  wireless wearable EEG. Sensors 17 (3). doi: 10.3390/s17030486 .  Zhang, Z., Jung, T.P., Makeig, S., Rao, B.D., 2013. Compressed sensing of EEG for wireless

telemonitoring with low energy consumption and inexpensive hardware. IEEE Trans.  Biomed. Eng. 60 (1), 221–224 .  Ziegler, D.A., Simon, A.J., Gallen, C.L., Skinner, S., Janowich, J.R., Volponi, J.J.,

Rolle, C.E., et al., 2019. Closed-loop digital meditation improves sustained attention  in young adults. Nat. Hum. Behav. 3 (7), 746–757 .  Zink, R., Hunyadi, B., Huﬀel, S.V., Vos, M.D.E., 2016. Mobile EEG on the bike: disentan-

gling attentional and physical contributions to auditory attention tasks. J. Neural Eng.  13 (4), 046017 .

17

## Tables transcribed from page images (p. 4)

Table 1 (Specifications of wireless EEG devices) is drawn as vector paths with no text layer; transcribed from a 450-dpi render on 2026-10-10. Selected columns only (omitted: reference location, accelerometer/gyroscope, bipolar ExG/aux, triggers, shielding, impedance check, input range/impedance/noise, CMRR, bandwidth, LSB, size, local storage, output format, smartphone support, website). Abbreviations as in the caption: Flex = flexible electrode placement; Prop = ISM proprietary 2.4 GHz; CoME D = device mobility (0–5); CoME S = system specification (4–20); price in k EUR, Dec 2022; "-" = not obtained.

| Device | Company | Year | EEG ch | Placement | Electrode type | Preamp | Fs (Hz) | Bits | Weight (g) | Battery (h) | Protocol | Real-time | CoME D | CoME S | Med. cert. | Price (k EUR) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B-Alert X10 | Advanced Brain Monitoring | 2010 | 9 | Fixed | Gel | Passive | 256 | 16 | 71 | 8 | Bluetooth | SDK | 4 | 9 | No | 8-10 |
| B-Alert X24 | Advanced Brain Monitoring | 2012 | 20 | Fixed | Gel | Passive | 256 | 16 | 71 | 8 | Bluetooth | SDK | 4 | 9 | No | 12-15 |
| Stat X-Series X24 | Advanced Brain Monitoring | 2020 | 20 | Fixed | Gel | Passive | 256 | 16 | 71 | 8 | Bluetooth | SDK | 4 | 9 | Yes | 12-15 |
| eego mini 24 | ANT Neuro | 2022 | 24 | Flexible | Dry, Wet, Gel | Passive | 2048 | 24 | 100 | usb | WiFi | LSL/SDK | 4 | 14-12 | Yes | - |
| eego mini 8 | ANT Neuro | 2016 | 8 | Flexible | Dry, Wet, Gel | Passive | 2048 | 24 | 100 | usb | WiFi | LSL/SDK | 4 | 14-12 | Yes | - |
| eego sports | ANT Neuro | 2015 | 128/64/32 | Flexible | Dry, Wet, Gel | Passive | 2048 | 24 | 500 | 5 | WiFi | LSL/SDK | 4 | 15-13 | Yes | - |
| Air | Bitbrain | 2018 | 8 | Fixed | Dry | Passive | 256 | 24 | 212 | 8 | Bluetooth | LSL/SDK | 4 | 10 | No | 5 |
| Diadem | Bitbrain | 2016 | 12 | Fixed | Dry | Passive | 256 | 24 | 307 | 8 | Bluetooth | LSL/SDK | 4 | 10 | No | 13 |
| Hero | Bitbrain | 2022 | 9 | Fixed | Dry | Passive | 256 | 24 | 250 | 3 | Bluetooth | LSL/SDK | 4 | 10 | No | 13 |
| Neuroheadband | Bitbrain | 2023 | 5 | Fixed | Dry | Passive | 256 | 24 | 100 | 8 | BLE | LSL/SDK | 4 | 10 | On going | 2-4 |
| Versatile EEG | Bitbrain | 2017 | 64/32/16/8 | Flexible | Wet | Passive | 256 | 24 | 192/290/450 | 8 | Bluetooth | LSL/SDK | 4 | 11 | No | 26/14/9/4 |
| LiveAmp | Brain Products | 2015 | 64/32/16/8 | Flexible | Dry, Wet, Gel | Active/Passive | 1000/500/250 | 24 | 60 | 4/24 | Prop | LSL/SDK/TCP-IP | 3 | 15-10 | No | - |
| X.on | Brain Products | 2022 | 7 | Fixed | Wet | Passive | 500/250/125 | 24 (BT5)/16 (BLE) | 120 | 5 | BLE, BT5 | LSL | 4 | 11-7 | No | 2.5 |
| Mobile | CGX (Cognionics) | 2021 | 128/72 | Flexible | Gel | Active | 500 | 24 | 1000 | 10-4 | Bluetooth | LSL | 3 | 13 | No | 45-60 |
| Quick20r v2 | CGX (Cognionics) | 2021 | 21 | Fixed | Dry | Active | 500 | 24 | 596 | 8 | BLE | LSL | 4 | 12 | No | 20 |
| Quick32r | CGX (Cognionics) | 2021 | 30 | Fixed | Dry | Active | 500 | 24 | 646 | 8 | BLE | LSL | 4 | 12 | No | 28 |
| Siesta Wireless | Compumedics | 2001 | 32 | Flexible | Wet, Gel | Active | 1000/100 | 16 | 300 | 24 | WiFi | - | 2 | 14-10 | Yes | - |
| EPOC X | Emotiv | - | 14 | Fixed | Wet | Passive | 256/128 | 16/14 | 1000 | 12-6 | BLE, Bluetooth, Prop | - | 4 | 9-7 | No | <1 |
| EPOC-Flex | Emotiv | - | 32 | Fixed | Wet, Gel | Passive | 128 | 14 | 1000 | 9 | BLE, Prop | - | 3 | 8-7 | No | 1-2 |
| INSIGHT | Emotiv | - | 5 | Fixed | Dry | Passive | 128 | 16 | 1000 | 20 | BLE, Bluetooth | - | 4 | 8 | No | <0.5 |
| g.Nautilus MULTI-PURPOSE | g.tec | 2014 | 32/16/8 | Flexible | Gel, Dry/Gel (hybrid) | Active | 500/250 | 24 | 110 | 10 | Prop | LSL | 3 | 12-10 | No | 5-36 |
| g.Nautilus MULTI-PURPOSE | g.tec | 2014 | 64 | Flexible | Gel, Dry/Gel (hybrid) | Active | 250 | 24 | 140 | 6 | Prop | LSL | 3 | 14-11 | No | 5-36 |
| g.Nautilus PRO Flexible | g.tec | - | 32/16/8 | Flexible | Gel, Dry/Gel (hybrid) | Active | 500/250 | 24 | 110 | 10 | Prop | LSL | 3 | 14-11 | Yes | 6.5-25 |
| g.Nautilus RESEARCH | g.tec | 2014 | 32/16/8 | Flexible | Dry, Gel | Active | 500/250 | 24 | 110 | 10 | Prop | LSL | 3 | 12-10 | No | 5-35 |
| g.Nautilus RESEARCH | g.tec | 2014 | 64 | Flexible | Dry, Gel | Active | 250 | 24 | 140 | 6 | Prop | LSL | 3 | 14-11 | No | 5-35 |
| g.NautilusPRO | g.tec | 2014 | 32/16/8 | Flexible | Dry, Gel | Active | 500/250 | 24 | 110 | 10 | Prop | LSL | 3 | 14-11 | Yes | 6-20 |
| Unicorn Hybrid Black | g.tec | 2019 | 8 | Flexible | Dry/Gel (hybrid) | Passive | 250 | 24 | - | 4 | Bluetooth | LSL | 4 | 11-9 | No | <1 |
| Unicorn Naked BCI | g.tec | - | 8 | Flexible | Dry/Gel (hybrid) | Passive | 250 | 24 | - | 4 | Bluetooth | LSL | 4 | 11-9 | No | <1 |
| MUSE 2 | InteraXon | 2018 | 4 | Fixed | Dry | Passive | 256 | 12 | 39 | 5 | Bluetooth | LSL/SDK/OSC | 4 | 7 | No | <0.5 |
| MUSE S | InteraXon | 2021 | 4 | Fixed | Dry | Passive | 256 | 12 | 41 | 10 | Bluetooth | LSL/SDK/OSC | 4 | 8 | No | <0.5 |
| Smarting MOBI | mBrainTrain | 2014 | 24 | Flexible | Wet, Gel | Passive | 500/250 | 24 | 60 | 4 | Bluetooth | LSL | 3 | 12-10 | No | - |
| Smarting PRO | mBrainTrain | 2021 | 32 | Flexible | Wet, Gel | Passive | 1000/500/250 (2000 SD card) | 24 | 65 | 10 | BT5 | LSL | 4 | 14-11 | No | - |
| Smarting PRO X | mBrainTrain | 2022 | 64 | Fixed | Wet, Gel | Passive | 1000/500/250 (4000 SD card) | 24 | 65 | 11 | BT5 | LSL | 4 | 14-11 | No | - |
| Smarting SLEEP | mBrainTrain | 2017 | 24 | Flexible | Gel | Passive | 500/250 | 24 | 115 | 15 | Bluetooth | LSL | 3 | 13-12 | No | - |
| Explore | Mentalab | 2020 | 8/4 | Flexible | Dry, Gel | Passive | 1000/500/250 | 24 | 27 | 12 | Bluetooth | LSL/API/SDK | 4 | 14-12 | No | 4.5-6 |
| Explore+ | Mentalab | 2022 | 32/16/8 | Flexible | Dry, Gel | Passive | 1000/500/250 (2000 offline) | 24 | 36/27 | 12-10 | Bluetooth | LSL/API/SDK | 4 | 14-10 | No | 7-20 |
| NeXus-10 MKII | Mind Media | - | 4 | Flexible | Gel | Passive | 2048 | 24 | 540 | 24 | Bluetooth | SDK | 2 | 17 | Yes | - |
| SmartBCI x24/x32 | MITSAR | - | 32/24 | Flexible | Dry, Gel | Active | 500 (BT5)/250 (BT3) | 24 | 70 | 24-20 | Bluetooth, BT5 | - | 3 | 15-12 | Yes | - |
| SmartBCI x64 | MITSAR | - | 64 | Flexible | Gel | - | 250 (BT5) (2000 onboard) | 24 | 200 | 24 | BT5 | - | 3 | 13 | No | - |
| Enobio | Neuroelectrics | 2011 | 32/20/8 | Flexible | Dry, Gel | Passive | 500 | 24 | 81/83/97 | 6 | WiFi | LSL/SDK | 3 | 12-10 | Yes | 4-24 |
| Crown | Neurosity | 2021 | 8 | Fixed | Dry | Active/Passive | 256 | 24 | 228 | 3 | BLE, WiFi | LSL/SDK/OSC | 5 | 11-10 | No | <1 |
| Cyton+Daisy | OpenBCI | 2014 | 16/8 | Flexible | Dry, Wet, Gel | Active/Passive | 250/125 | 24 | 60 | 8 | BLE | LSL/Serial/UDP/OSC | 4 | 13-9 | No | 1-2 |
| Ganglion | OpenBCI | 2016 | 4 | Flexible | Dry, Wet, Gel | Passive | 200 | 24 | 30 | 8 | BLE | LSL/Serial/UDP/OSC | 4 | 12-10 | No | <1 |
| DSI-24 | Wearable Sensing | 2009 | 21 | Fixed | Dry | Active | 600/300 | 16 | 600 | 24 | Bluetooth | LSL/TCP-IP/API | 4 | 12-11 | No | - |
| DSI-7 | Wearable Sensing | 2013 | 7 | Fixed | Dry | Active | 600/300 | 16 | 350 | 12-8 | Bluetooth | LSL/TCP-IP/API | 4 | 11-10 | No | - |
| DSI-7 Flex | Wearable Sensing | 2013 | 7 | Flexible | Dry | Active | 600/300 | 16 | 200 | 12-8 | Bluetooth | LSL/TCP-IP/API | 4 | 11-10 | No | - |
| VR300 | Wearable Sensing | 2015 | 7 | Fixed | Dry | Active | 600/300 | 16 | 400 | 12-8 | Bluetooth | LSL/TCP-IP/API | 4 | 11-10 | No | - |
| Zeto WR19 | Zeto | 2020 | 21 | Fixed | Dry | Active | 500/250 | 24 | 680 | 6-5 | WiFi | LSL/SDK | 4 | 12 | Yes | - |
