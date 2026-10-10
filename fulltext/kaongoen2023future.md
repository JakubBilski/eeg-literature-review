<!-- source: pdf/kaongoen2023future.pdf | converter: pymupdf -->

<!-- page 1 -->

## Journal of Neural Engineering

TOPICAL REVIEW

## The future of wearable EEG: a review of ear-EEG technology and its applications

To cite this article: Netiwit Kaongoen et al 2023 J. Neural Eng. 20 051002

View the article online for updates and enhancements.

## You may also like

Identifying auditory attention with ear- EEG: cEEGrid versus high-density cap- EEG comparison Martin G Bleichner, Bojana Mirkovic and Stefan Debener

-

High-density ear-EEG for understanding ear-centered EEG Arnd Meiser, Anna Lena Knoll and Martin G Bleichner

-

Towards ASSR-based hearing assessment using natural sounds Anna Sergeeva, Christian Bech Christensen and Preben Kidmose

-

This content was downloaded from IP address 143.248.135.85 on 30/04/2024 at 07:22

<!-- page 2 -->

J. Neural Eng. 20 (2023) 051002 https://doi.org/10.1088/1741-2552/acfcda

# Journal of Neural Engineering

RECEIVED 18 April 2023

REVISED 19 September 2023

ACCEPTED FOR PUBLICATION 25 September 2023

PUBLISHED 6 October 2023

TOPICAL REVIEW

# The future of wearable EEG: a review of ear-EEG technology and its applications

Netiwit Kaongoen1,6, Jaehoon Choi2,6, Jin Woo Choi3, Haram Kwon2, Chaeeun Hwang2, Guebin Hwang4, Byung Hyung Kim5and Sungho Jo2,∗

1 Information and Electronics Research Institute, Korea Advanced Institute of Science and Technology, Daejeon, Republic of Korea 2 School of Computing, Korea Advanced Institute of Science and Technology, Daejeon, Republic of Korea 3 Department of Neurology and Neurological Sciences, Stanford University School of Medicine, Stanford, CA 94304, United States of America 4 Robotics Program, Korea Advanced Institute of Science and Technology, Daejeon, Republic of Korea 5 Department of Artificial Intelligence, Inha University, Incheon, Republic of Korea 6 Both authors contributed equally to this work. ∗Author to whom any correspondence should be addressed.

E-mail: shjo@kaist.ac.kr

Keywords: ear-EEG, in-ear EEG, around-ear EEG, brain–computer interface, wearable system

Abstract Objective. This review paper provides a comprehensive overview of ear-electroencephalogram (EEG) technology, which involves recording EEG signals from electrodes placed in or around the ear, and its applications in the field of neural engineering. Approach. We conducted a thorough literature search using multiple databases to identify relevant studies related to ear-EEG technology and its various applications. We selected 123 publications and synthesized the information to highlight the main findings and trends in this field. Main results. Our review highlights the potential of ear-EEG technology as the future of wearable EEG technology. We discuss the advantages and limitations of ear-EEG compared to traditional scalp-based EEG and methods to overcome those limitations. Through our review, we found that ear-EEG is a promising method that produces comparable results to conventional scalp-based methods. We review the development of ear-EEG sensing devices, including the design, types of sensors, and materials. We also review the current state of research on ear-EEG in different application areas such as brain–computer interfaces, and clinical monitoring. Significance. This review paper is the first to focus solely on reviewing ear-EEG research articles. As such, it serves as a valuable resource for researchers, clinicians, and engineers working in the field of neural engineering. Our review sheds light on the exciting future prospects of ear-EEG, and its potential to advance neural engineering research and become the future of wearable EEG technology.

## 1. Introduction

Electroencephalography (EEG) is a widely used, non-invasive method for measuring and recording the electrical activity of the brain. Traditional EEG involves the placement of electrodes on the scalp, which are secured in place using a combination of electrolyte gel and a tight-fitting elastic cap to ensure proper contact between the electrodes and the skin [1]. While this approach provides high-quality EEG signals, it may not be suitable for long-term monitoring or use outside of a laboratory or hos- pital setting. To overcome this challenge, research- ers have proposed various approaches. For instance,

one approach involves the utilization of different elec- trode types, such as dry electrodes, which do not require electrolyte gels. Another approach involves redesigning the EEG system to enhance wearability and accessibility, making it suitable for a broader range of applications, especially for long-term mon- itoring in daily-life usage [2]. These modifications aim to make EEG portable and wearable, allowing for greater flexibility and convenience in its use.

Ear-EEG is a novel EEG acquisition technique that aims to improve the practicality of EEG meas- urement. This technique involves the placement of electrodes in or around the ear to capture EEG signals [3, 4]. The use of ears as recording sites

© 2023 IOP Publishing Ltd

<!-- page 3 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

offers several advantages over traditional scalp-based EEG. Firstly, the absence of hair in these areas facil- itates improved skin-to-electrode contact, resulting in enhanced signal quality and increased user com- fort. Secondly, the discreet placement of the elec- trodes around the ear makes them less noticeable to others, which can help alleviate the social awkward- ness that is often associated with conventional EEG systems. Additionally, the ears can serve as an anchor- ing point for the device to attach to the user’s body and are also easily reachable by the user’s hands. This provides an added advantage for ease of wearabil- ity and self-management. It also opens up the pos- sibility for touch-based interactions with the device. This increased practicality and comfort make ear- EEG a promising tool for long-term monitoring and for use in daily-life applications. A significant draw- back of ear-EEG in comparison to the conventional scalp-based method lies in its limited coverage area. Studies such as [5, 6] have demonstrated that ear-EEG primarily captures neural signals originating from the temporal lobe. Consequently, this limitation may lead to a reduced range of detectable EEG signals or lower signal quality compared to the more compre- hensive coverage provided by scalp-based EEG. The primary focus of early ear-EEG research was to assess the range of EEG signals that could be detected using this technique and its potential applications, as well as to compare its performance with conventional EEG methods.

Ear-EEG technology can be differentiated into two categories based on its electrode placement and device design: in-ear EEG [3] and around-ear EEG [4]. In-ear EEG involves electrodes positioned inside the ear canal or on the ear, while around-ear EEG, also known as the ‘behind-ear’ method, places electrodes around the ear area, usually beneath the hairline. Both methods have their own advantages and trade-offs. While in-ear EEG offers greater discretion, with the sensing device hidden inside the ear, it may also block external sound depending on the device design. On the other hand, around-ear EEG may be less discreet than in-ear EEG, but it covers a wider area, making it more practical for detecting a broader range of brain signals. Studies have demonstrated that ear-EEG can detect meaningful neural activity and has a multitude of applications, including but not limited to monit- oring mental state and neurological conditions, and brain–computer interfaces (BCIs). It is important to emphasize that in an ear-EEG system, all electrode placements, including reference and ground, should remain within the ear region. However, this review also covers some wearable EEG systems that incor- porate electrodes placed in areas such as the scalp or forehead, in addition to those on the ear region. For the sake of simplicity, we will refer to these systems as hybrid EEG systems throughout the remainder of this

review. While a comprehensive discussion of hybrid EEG systems falls beyond the scope of this review, they will be briefly discussed alongside certain ear- EEG systems with similar device designs (refer to section 3). This approach aims to help readers under- stand that wearable EEG devices can extend their recording sites beyond a specific area. We believe this inclusion will contribute to advancing the field of wearable EEG systems.

Previous research reviews have explored the topic of ear-EEG. Ne et al conducted a review of 92 art- icles focusing on the acquisition of bio-signals using in-ear sensing devices, with only 48 studies specific- ally involving EEG [7]. Roddiger et al reviewed 271 publications relating to ear-worn sensing devices and their applications in physiological monitoring, move- ment and activity tracking, interaction, and authen- tication. However, this review still only covered 54 articles on ear-EEG [8]. Our work, on the other hand, specifically focuses on both in-ear and around- ear ear-EEG technology, highlighting its exceptional wearability and potential for real-life applications compared to traditional EEG acquisition methods. Our contribution provides a comprehensive under- standing of the history and current state of the art in ear-EEG technology and its potential as the future of wearable brain monitoring systems.

We conducted a thorough literature review of 123 research articles to enhance our understanding of ear- EEG and examine its efficacy as an EEG acquisition method and its potential applications. The primary focus of our literature review was to answer three main research questions:

(1) What are the crucial factors influencing the

development and setup of ear-EEG systems, and how do these choices impact the range of applic- ations, strengths, and limitations of ear-EEG technology? (2) What are the diverse applications and potential

uses of ear-EEG as an EEG acquisition method, and how does it contribute to various fields? (3) What are the limitations and drawbacks associ-

ated with the ear-EEG method, and what poten- tial strategies or approaches can be employed to address and mitigate these challenges?

This paper is organized into three main sections, each addressing one of the above key questions. The first section covers EEG sensing methods, includ- ing the device design (e.g. shape and material), sensors used (e.g. electrode types and placement), and signal processing modules (e.g. the EEG amp- lifier and necessary electronic parts). Many of the studies we reviewed used manual electrode placement on the ear area and traditional stationary EEG sens- ing devices, and conducted experiments only in a

2

<!-- page 4 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

laboratory setting to validate ear-EEG performance. However, many studies also propose innovative and functional wearable ear-EEG systems for both in-ear and around-ear approaches. In the second section of our review, we delve into the capabilities of ear- EEG methods. We explore the undertaken research, assessing the range of EEG signals attainable through ear-EEG, and evaluating the performance of the ear- EEG method within various experimental setups for diverse applications. In the final section, we dis- cuss the challenges associated with EEG acquisition using ear-EEG methods, mainly the limited cover- age area by the ear-EEG sensing device. We examine signal processing techniques aimed at enhancing the EEG signal’s signal-to-noise ratio (SNR) and machine learning methods to improve ear-EEG performance, enabling it to match the performance of conventional scalp-based EEG methods.

## 2. Review methodology

This review aims to provide a comprehensive over- view of ear-EEG technology, including the current state-of-the-art devices and methods used for acquir- ing ear-EEG, the different techniques used for pro- cessing and analyzing ear-EEG signals, and the diverse range of applications in which ear-EEG has been examined. We conducted a comprehensive search of electronic databases, including Google Scholar, IEEE Xplore, and PubMed, using a combination of the fol- lowing keywords as our search terms: ‘ear-EEG’, ‘in- ear EEG’, ‘around-ear EEG’, ‘behind-the-ear EEG’, and ‘ear-based EEG’. Additional studies were identified through manual searches of reference lists from rel- evant articles that met our inclusion criteria.

In this review, we included studies that used ear- EEG technology to record brain activity in humans in the ear area. It is important to mention the variabil- ity in nomenclature pertaining to the different types of ear-EEG. For instance, some literature employs the terms ‘in-ear EEG’ and ‘in-the-ear EEG’ inter- changeably, while others utilize terms like ‘around- ear EEG,’ ‘around-the-ear EEG,’ ‘behind-ear EEG,’ and ‘behind-the-ear EEG’ interchangeably as well. To ensure clarity, this review article uniformly adopts the term ‘in-ear EEG’ to denote EEG acquired from internal ear structures, encompassing the ear canal and concha. Similarly, the term ‘around-ear EEG’ is employed to refer to EEG acquired from the circular perimeter encompassing the ears. Figure 1 illustrates the skin areas covered by each type of EEG examined in this review article, including scalp EEG (gray), around-ear EEG (orange), and in-ear EEG (blue). The figure also depicts the in-ear structure, with the ear canal and concha highlighted as the common sites for in-ear EEG recording. While ear-EEG tech- nologies are typically designed for wearable purposes,

we also considered studies that recorded EEG sig- nals around the ear area using conventional, sta- tionary EEG acquisition setups. Studies that used ear-worn devices to acquire other biological sig- nals such as electrooculogram (EOG), electromyo- gram (EMG), electrocardiogram (ECG), and pho- toplethysmography (PPG) were excluded unless the device also recorded EEG signals in addition to one of the other mentioned signals. We extracted relevant data from each included study, including the study design, sample size, ear-EEG device used, electrode placement, data processing and analysis methods, and its applications.

A total of 123 relevant articles were identified in our comprehensive search for research on ear-EEG technology. Figure 2 displays the number of ear-EEG articles published each year, from 2011 to March 2023 (the time of writing this review article). Despite a steady increase in the number of studies conducted each year, the overall amount of research on ear-EEG is still relatively small, which could limit the gener- alizability of our findings. Moreover, the majority of the studies we reviewed had small sample sizes, which could impact the reliability and validity of the res- ults. Ear-EEG technology is still in its early stages, and the range of its applications is not yet fully under- stood. While this review article summarizes the devel- opment history of ear-EEG technology and highlights its potential as the future of wearable EEG technology, further research is necessary to evaluate its potential in real-world settings fully.

## 3. Development of ear-EEG sensing methods

In this section, we trace the development of ear- EEG sensing devices and examine the latest advance- ments in design. For each study, we examine the sensor components, including the material and type of electrodes, as well as the placement and number of electrodes. We evaluate the design of the device in terms of practicality and appearance and assess its wearability and potential for real-world use. Some studies present a comprehensive system, comprising sensors, a battery, and a printed circuit board (PCB) for signal processing, computing, and data trans- mission. After reviewing 123 research articles, it was found that 79 of them utilized in-ear EEG acquisi- tion techniques, while 47 of them utilized around- ear EEG acquisition techniques. Three of the articles utilized both in-ear and around-ear EEG methods. Eleven of the around-ear EEG research studies did not employ any wearable sensors specifically designed for around-ear EEG acquisition. Instead, they either manually attached the electrodes to the ear area or obtained EEG data from conventional scalp-EEG caps with channels positioned nearest to the ears. Figure 3

3

<!-- page 5 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

Figure 1. Skin coverage comparison of different EEG types: scalp EEG (grey), around-ear EEG (orange), and in-ear EEG (blue). Detailed depiction of in-ear structure highlighting common in-ear electrode placement sites: ear canal (pink) and concha (green).

Figure 2. The number of publications relevant to ear-EEG over time from 2011 to 2023 (∗March).

presents a schematic map that provides an overview of the ear-EEG articles, classified according to the design of the ear-EEG sensing device. The figure includes the number of articles (N) in each category. However, it should be noted that the size of each box is not pro- portional to the number of articles.

3.1. In-ear methods The concept of recording EEG from within the ear was first introduced by Looney and their team in 2011 before the term ‘ear-EEG’ had even been published. The first in-ear EEG sensing device, referred to as the ‘in-the-ear’ (ITE) recording platform, was created by embedding three AgCl electrodes on a custom- made earpiece manufactured in the same process as a hearing-aid device [9, 10]. In these initial works, the ITE electrodes were used as an extension of the

conventional EEG setup, with the recorded EEG being referenced and grounded at the ear-lobe and chin, respectively. Following the successful confirmation of alpha activity in EEG recordings obtained from ITE electrodes, with correlations and coherence shown to be excellent when compared to on-scalp electrodes, the researchers continued to improve their ear-EEG sensing device. They added an additional electrode to each side of the earpiece, making the system truly an ITE measurement setup with all electrodes, including reference and ground electrodes, situated within the ear [3, 11]. For each in-ear EEG sensing earpiece, the reference electrode was positioned on the inferior side of the ear canal, and the ground electrode was placed at the top of the concha. This fully integrated in-ear sensing device was successfully evaluated for its abil- ity to record various types of EEG signals commonly

4

<!-- page 6 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

Figure 3. Overview map of the reviewed articles on ear-EEG, categorized according to the design of the ear-EEG sensing device. ∗Hybrid EEG systems containing electrodes beyond the ear area.

used in BCI technology. This has led to increased interest in ear-EEG from the EEG and BCI research community ever since.

3.1.1. In-ear EEG sensing device design 3.1.1.1. Personalized earpiece Following the original ear-EEG research, the major- ity of in-ear EEG devices were designed as elec- trodes embedded in personalized earpieces [12–22], with only minor adjustments from the original works such as changing the material for the earpieces and electrodes [23–26] or making the electrodes an act- ive type [27]. The process of creating these personal- ized earpieces involved taking a wax impression of the individual’s ear, 3D scanning the impressed ear shape, creating a computer-aided design (CAD) model of the earpiece, and using additive manufacturing tech- nology. To simplify the earpiece fabrication process, some researchers eliminated the 3D modeling step and instead used moldable materials that were per- sonalized to the research subject’s ear shape as the base for their in-ear EEG sensing device. They also changed the electrode material to make it easier to fabricate and more suitable for alternative earpiece materials. For example, in [28, 29], moldable plastic beads (InstaMorph) were chosen as the material for making the personalized earpieces.

3.1.1.2. Generic earpiece Although the personalized earpiece design approach offered a perfect fit for each individual’s ear shape and resulted in high-quality EEG signals, the device fabrication process was expensive, complicated, and time-consuming. To address this issue, researchers began developing in-ear EEG device designs that were

generic and could accommodate the biological struc- ture of any ear shape. In 2013, the team that pioneered in-ear EEG technology presented one of the first gen- eric designs of an in-ear EEG device [30]. Their design featured a conical-shaped earplug made of biocom- patible silicone rubber. In recent years, some innovat- ive and effective designs for generic in-ear EEG sens- ing devices have been proposed [31–34]. For instance, Kaveh et al [32] used a 3D scan of the in-ear structure to create a unique, generic design that can fit all users. Their earpieces feature four outward cantilevers, each of which acts as an individual electrode and applies pressure to the ear canal, along with two larger elec- trodes positioned on the concha for reference and ground. For their final design [33], the earpiece body was 3D printed with flexible resin for greater comfort. In 2022, Paul et al [34] introduced the weDAQ system, a complete wireless electrophysiology data acquisi- tion system that can simultaneously acquire multiple biological data streams, including in-ear EEG. Their weDAQ system features a unique generic design for in-ear EEG sensing, composed of two planar ‘cro- codile’ PCBs that fit together and form a 3D in-ear apparatus with multiple electrodes on its surface.

3.1.1.3. Viscoelastic earpiece A large number of studies use commercially available memory foam or other viscoelastic materials as the base for their in-ear EEG device designs. Like the gen- eric silicone earplug presented in [30], these designs are often conical in shape, resembling an earplug, with or without a hole in the middle for the audit- ory pathway. Viscoelastic materials such as memory foam are often used as a substitute for silicone or

5

<!-- page 7 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

plastic because the earpieces made from these mater- ials can still have some of the drawbacks of hard materials, which do not guarantee a perfect fit to the shape of the ear canal. This imperfect fit can lead to motion artifacts and may require an electrically con- ductive gel to overcome the issue. Additionally, it has been reported that conductive silicone may not be a suitable material for long-term use in EEG elec- trodes due to its degradation over several months, which can significantly increase the impedance level [35]. The idea of using viscoelastic material for in- ear EEG earpieces was first proposed by Goverdovsky et al in 2015 [35]. The first viscoelastic in-ear EEG earpiece consisted of a memory foam base mater- ial with electrodes attached to its surface. The vis- coelasticity of the material allowed the earpiece to be easily and comfortably worn and perfectly fit into the user’s ear canal. This property also ensured that energy from abrupt motion was absorbed, leading to lower motion artifacts. The viscoelastic approach to in-ear EEG has been utilized in numerous stud- ies, demonstrating its capabilities in acquiring in-ear EEG for various applications, however, the device design has undergone only minor adjustments since its origination [36–46]. Some studies directly use commercially available flexible electrode as in-ear EEG sensing device. For example, Ahn et al [47] used a Gold Tip Trode electrode (8500370, Sanibel Supply) for their in-ear EEG sensing apparatus. This dispos- able electrode is made of foam wrapped in gold foil and is typically used for recording electrocochleo- graphy. Likewise, Guermandi et al [48] presented an in-ear-EEG system that uses a conductive elastomer spike electrode covered with Ag/AgCl paint as an in- ear electrode.

While viscoelastic material is a great option for the base of the in-ear EEG electrode, providing com- fort and a perfect fit to the ear canal, simply designing the whole earpiece in an earplug shape presents some drawbacks when compared to other designs, such as personalized earpieces or generic earphones. Firstly, the viscoelastic earplug lacks an exterior hanger to fixate the earpiece to the concha, which can cause it to easily slip out of the user’s ears, especially when the earplug electrodes are wired to the external pro- cessing module. Secondly, viscoelastic earplugs com- pletely occlude the ear canal, blocking sound trans- mission, which could potentially disrupt the user’s daily activities. Additionally, the small covering area of the earplug limits the number of electrodes that can be included, particularly when the reference and ground channels are necessary to create a truly ITE measurement setup.

3.1.1.4. Earpieces in the shape of earphones or earbuds An alternative strategy for creating generic in-ear EEG sensing devices involves taking inspiration from con- ventional in-ear earphones or earbuds. Among the reviewed articles, two distinct approaches emerged.

The first approach involves directly affixing con- ductive materials and wiring to the earbud tips, utilizing them as electrodes [49–52]. The second approach revolves around creating the earbud tips themselves from a flexible conductive material, util- izing the entire earbud tip as an electrode [53, 54]. In-ear EEG sensing devices designed as earphones or earbuds offer a versatile and stylish EEG system suitable for long-term use in daily life. By incor- porating flexible or viscoelastic materials at the tip of the device, it can be easily fitted into the ear canal, providing a comfortable and secure fit. Unlike the viscoelastic earplug design discussed earlier, the earphone design includes an exterior structure that can fixate the earpiece, thus overcoming the chal- lenges associated with the earplug design. Moreover, the earphone design provides a broader coverage of the ear, enabling the positioning of the reference and ground electrodes at the concha area, thereby creating a comprehensive in-ear measurement setup.

3.1.2. In-ear EEG electrodes 3.1.2.1. Electrode types As evident from the reviewed articles, dry passive electrodes are the prevailing choice for making in-ear EEG sensing devices. This preference can be attrib- uted to the challenges associated with applying con- ductive gel or paste within the confines of the narrow ear canal. Ensuring precise application of the con- ductive paste solely onto the intended electrode, while preventing inadvertent bridging between electrodes, appears to be a formidable task. Moreover, this applic- ation process might be uncomfortable for users, as the ear canal poses difficulties for cleaning residual con- ductive substances after using the in-ear EEG device. Nonetheless, it is crucial to acknowledge that cer- tain studies do incorporate a small amount of saline solution or conductive gel to ensure optimal contact between the skin and the electrode and maintain a low impedance level. However, it is important to note that as of now, no subject survey or reported feedback has addressed the comfort levels associated with the wet in-ear electrode approach in any study.

In personalized earpieces, pure silver or Ag/AgCl is commonly favored material for making electrodes, while studies like [33] have investigated electrodes created via electroless plating using metals like palla- dium, copper, and gold. In studies employing simpli- fied fabrication methods, like those by [28, 29], elec- trodes were created by manually applying conductive silver paste (ELCOAT, CANS) directly onto the sur- face of the molded earpieces.

Conductive fabric is a practical material choice for in-ear EEG electrodes, particularly in viscoelastic earpieces [35, 51, 52]. Its remarkable flexibility and ability to adapt to the earpiece’s shape, even as the earpiece compresses during insertion into the ear canal, make it a suitable option.

6

<!-- page 8 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

As outlined in the preceding section, certain studies have crafted electrodes utilizing conductive flexible polymers as their material of choice. For example, Lee et al [53] fabricated earbud-shaped electrodes using a composite of carbon nanotubes and polydimethylsiloxane (CNTs/PDMS). The CNT material provided outstanding electrical, mechan- ical, and thermal properties, while the biocompat- ible PDMS allowed for high gas and water permeab- ility and adaptability to various fabrication methods. Similarly, Dong et al [54] utilized a conductive rub- ber material called silvered glass silicone, which con- sists of silver, glass silver, and silver conductive grains mixed with silicone rubber, for their earbud-shaped electrodes. This electrode type offers elevated comfort due to its softness and flexibility, and boasts remark- able versatility as it can be molded into diverse shapes and designs. Nonetheless, its manufacturing process is intricate, demanding specialized tools and expert- ise. Moreover, certain commercially available options may be pre-configured into shapes that may not align with a researcher’s or developer’s intended design, as seen with the conductive elastomer spike electrode utilized in [48].

Furthermore, within the scope of the reviewed in-ear EEG studies, merely two investigations intro- duce in-ear EEG devices featuring active electrodes [27, 47]. This could be attributed to the inherent chal- lenge posed by the compact size of in-ear EEG devices when compared to other EEG sensing methods. The smaller form factor complicates the inclusion of elec- tronic circuits required to render the electrodes active.

3.1.2.2. Electrode number and location In addition to the design and material of the device, the number of EEG channels is an important factor to consider when designing a wearable EEG acquisi- tion system. While a small number of EEG channels can reduce the cost and time required for fabricating the sensing device, as well as potentially lowering the computational cost during signal processing and ana- lysis, a high number of EEG channels provides a better spatial resolution of the EEG and can possibly yield better results.

The majority of in-ear EEG studies examined in this review employ a limited number of chan- nels, often comprising fewer than eight within each earpiece. This tendency might arise from the compact dimensions of the in-ear structure. Consequently, the electrodes must also be small to fit snugly within the ear, thereby rendering the fabrication process more intricate. The complexity of this situation becomes particularly noticeable when dealing with handcraf- ted electrodes.

Some studies have designed in-ear EEG sensing devices with a high number of in-ear-EEG channels. The first high-density ear-EEG device was presented by Kappel et al in 2017 [55]. Each personalized earpiece had 15 uniformly embedded electrodes

on each side, made from circular titanium pins coated with IrO2. The high-density ear-EEG record- ing enables researchers to compare neural activity with scalp-based EEG methods, which helps to invest- igate how different cortical sources are mapped to the ear. Additionally, this method provides a way to identify optimal electrode placements for the tar- get application. Another variation of a high-density in-ear EEG device was presented in the works of Paul et al in 2019 [56, 57]. This device featured 17 small Ag/AgCl electrodes fitted into each personalized earpiece, instead of the IrO2 electrodes used in earlier works.

While there is not a universally accepted inter- national standard for the nomenclature and arrange- ment of in-ear EEG electrodes, the methodology pro- posed by the original in-ear EEG research group [3] stands out for its ingenuity and meticulous electrode positioning. This particular approach designates each electrode as EXY, wherein X signifies either L or R, denoting the left or right side of the ear respectively, andY indicates the electrode’s position from the let- ters A to L (e.g. ERA, ERB,... ERL). Among these designations, A, B, and C correspond to the upper, middle, and lower regions of the concha, while D rep- resents the earlobe. The remaining eight electrodes are positioned within the ear canal, evenly spaced at distinct angles. Starting with E at the posterior point of the ear canal, the order proceeds clockwise toward the posterior direction. We strongly advocate for the adoption of this methodology in future in-ear EEG studies, as it promotes consistency and coher- ence within the research field.

Reference and ground electrodes are typically placed at the concha (EXA, EXB, EXC), a location comparatively more distant from the brain than the ear canal. Nonetheless, in numerous studies, addi- tional electrodes are employed with separate cables attached to the earlobe, around-ear area, or mast- oid, functioning as reference and ground points. This practice results in their system not aligning with a true in-ear EEG setup. In the pursuit of optimal wear- ability, we advocate for the development of a truly in-ear measurement device with integrated reference and ground electrodes, devoid of externally visible electrodes, thus maximizing discreetness. We recom- mend that future developers of in-ear EEG systems take this into account during equipment design or devise innovative solutions to maintain both discre- tion and wearability, even if external out-of-ear elec- trodes are integrated.

3.2. Around-ear methods In 2012, Wang et al [58] investigated the feasibil- ity of measuring steady-state visual evoked poten- tials (SSVEPs) from non-scalp regions, including the forehead/face, behind-the-ear, and neck areas, intro- ducing the novel concept of measuring and util- izing EEG from non-scalp regions, specifically the

7

<!-- page 9 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

area around the ear. This concept has important implications for the development of new EEG-based technologies that could lead to more accessible and wearable EEG measurements. In 2015, the advent of around-ear EEG technology gained significant recog- nition within the research community, primarily due to the introduction of cEEGrid [4]. This innovat- ive device marked a turning point in around-ear EEG research, prompting numerous studies explor- ing its efficiency, applications [59], and inspiring the development of other around-ear EEG sensing devices. In contrast to the extensive development of in-ear EEG sensing devices, the progress in around- ear EEG sensing technology, however, has been lim- ited. The majority of research in this area has relied on either cEEGrids or alternatively, manually attached conventional EEG electrodes to the around-ear area. This section explores the sensor and hardware design presented in the around-ear EEG studies.

3.2.1. Around-ear EEG sensor design 3.2.1.1. Adhesive c-shaped electrode array The most widely used around-ear EEG sensor in research is cEEGrid [4]. The cEEGrid is a flexible printed c-shaped electrode array specifically designed to be placed around the user’s ears. Its flexprint mater- ial consists of several layers of biocompatible polyam- ide, where the electrodes are laid on the upmost sur- face. This type of around-ear EEG sensor cannot be attached to the user’s skin directly and requires the use of double-sided adhesive tape or other adhesive material to attach them to the skin around the user’s ears.

Although the signal processing hardware has to be considered to judge the wearability of the whole system, this type of around-ear EEG sensor is very comfortable to the users, and its adhesive property to the user’s skin also ensures the fixation in elec- trode placements even in the long-term use. Its draw- backs are that the adhesive parts of the sensor have to be replaced regularly, and the user’s skin has to be cleaned and prepared every time before use to ensure the attachment between the sensors and skin. From the researcher and developer’s point of view, the pro- cess of fabricating the electrode array is complicated and cannot be easily self-made without the specific tools and experts, but the cEEGrids are commercially available (e.g. https://exgtools.expeeeriments.io/).

Some studies have utilized designs similar to cEE- Grids for fabricating around-ear EEG sensors. For instance, Guermandi et al [60] created an around- ear EEG system that incorporates their own C-shaped electrode arrays made from flexible polyimide PCB resembling cEEGrids but their reference and ground electrodes are in a rectangle shape and located parallel to each other. Souto et al [61] made direct modifica- tions to the cEEGrid array. Based on their work con- ducting a sleep analysis using ear-EEG acquired from the cEEGrid [62], they developed a novel electrode

array called trEEGrid, which is specifically designed for sleep analysis. This new sensor array is similar to cEEGrid, with the main difference being its expanded coverage area. It not only covers the around-ear area but also includes the regions around the eyes and chin to facilitate EOG and EMG measurements which are crucial for comprehensive sleep analysis.

3.2.1.2. Around-ear earpiece In both [63, 64], designs for around-ear EEG sensors were presented in the form of earpieces. Although they use different materials for their earpieces and electrodes, both designs feature a V-shaped folded structure with a hook that supports the device against the back of the pinna. Unlike the first type of around- ear sensor that uses adhesive tape to attach the sensor to the around-ear skin area, the electrodes are pressed against the skin using the spring effect created by the earpiece’s design. Additionally, the electrically conductive paste can be applied to ensure skin-to- electrode contact. The device is then connected to a processing module using wires.

3.2.1.3. Headphone In addition to C-shaped electrode arrays and earpieces, previous research has introduced sev- eral intriguing wearable EEG systems. Among these designs are headphones that utilize embedded elec- trodes within the ear cushions to record around-ear EEG signals. While headphone-based EEG systems may be less discreet and bulkier compared to other designs, they offer the advantage of using the head- band as an additional electrode site in conjunction with the around-ear area, enabling a hybrid EEG approach. Moreover, the headphone cups can serve as hosts for processing modules, rendering them com- plete wearable around-ear EEG systems in their own right. For instance, Kaongoen et al [65] presented an affordable custom-made around-ear EEG head- phone produced using 3D printing technology. In this design, all electrodes are integrated into the ear cushions, while the processing module and battery are situated within the headphone cups. In addi- tion, Smartfones (mBrainTrain, https://mbraintrain. com/smartfones) represents an integrated hybrid EEG system capable of recording both scalp-EEG and around-ear EEG signals. This system features electrodes located on its headband and ear cushion, respectively. Notably, it also facilitates simultaneous auditory input and EEG recording, expanding its range of potential applications [66].

3.2.1.4. Glasses Glasses represent another wearable design option for an around-ear EEG device. By utilizing the contact points on the skin around the user’s ears, the temples of the glasses can serve as the location for around- ear EEG sensing electrodes. Similar to the design of headphones, the coverage area of glasses extends to

8

<!-- page 10 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

the user’s eyes and nose, enabling the creation of a hybrid EEG system that incorporates around-ear EEG functionality. In 2018, Sopic et al [67] intro- duced the e-Glass, a wearable EEG system in the form of glasses. While e-Glass’s electrodes are placed on F7, F8, T3, and T4 based on the 10-20 international system which are not exactly the around-ear area, they are in close proximity to the around-ear EEG positions and therefore are relevant to this review article. In 2019, Kosmyna et al introduced another glasses-shaped wearable EEG device called AttentivU [68]. AttentivU is a hybrid EEG system that integrates EEG and EOG sensing through electrode placements extending beyond the ear area. The EEG electrodes are positioned at the temples of the glasses around the ears, while the EOG electrodes are placed at the nose pads. Ground and reference electrodes are situated at the nose bridge. To provide auditory and vibrotact- ile feedback, piezoelectric elements were integrated into the tips of the glasses temples. Both the frames of e-Glass and AttentivU are constructed from nylon plastic, which encloses the processing modules and battery.

3.2.1.5. Headband Some around-ear EEG sensing devices feature a head- band design, with the rear sections forming a c- shaped structure encircling the ears. For instance, Kaongoen et al [69] introduced a headband-based around-ear EEG device design in which the c-shaped sections around the ears are connected by a headband that wraps around the back of the user’s head. Similar to headphones and eyeglasses, the headband design also presents opportunities to expand electrode place- ment beyond the around-ear area. For instance, Ahn et al [70] proposed a headband-shaped hybrid EEG system that incorporates an electrode in the middle part of the headband, positioned on the user’s fore- head, in addition to electrodes located behind the ear area.

3.2.2. Around-ear EEG electrode 3.2.2.1. Electrode types The majority of reviewed around-ear EEG studies in this article have employed passive wet electrodes for measuring around-ear EEG signals. The prevailing choice of sensing device in around-ear EEG research, such as cEEGrid, constructs its electrodes using cir- cular gold-plated tips, pure copper traces, and a conductive Ag/AgCl-based polymer thick film ink. Electrolyte gel is applied to acquire around-ear EEG signals. The earpiece introduced in the work by Pham et al [64] also utilizes gold-based electrodes with con- ductive paste. The earpiece in Valentin et al’s study [63] employs conductive silicone along with con- ductive paste to leverage its flexible characteristics. Smartfones, on the other hand, uses saline-soaked sponge electrodes for data acquisition. This choice might be attributed to the electrodes’ coverage in the

scalp area, where the application of conductive paste or gel could be less desirable.

Certain devices, such as trEEGrid, have incorpor- ated pre-gelled electrodes to enhance user conveni- ence during self-application. In the case of around- ear EEG headphones mentioned in [65], as well as headbands described in [69, 70], single-use foam- type solid–gel snap electrodes have been adop- ted. These electrodes feature embedded snap sock- ets within the device, offering a streamlined equip- ment preparation process. However, it is import- ant to note that frequently changing electrodes for every use could potentially become cost-prohibitive for practical real-life applications. Of the around- ear EEG studies examined in this article, only two examples use dry electrodes: the c-shaped electrode array detailed in [60], which employs gold electrodes, and the AttentivU system, which utilizes silver elec- trodes. Furthermore, it is worth mentioning that only the electrode array discussed in [60] and the head- band described in [70] have introduced the allocation of active electrode electronics to enhance electrode impedance levels. It is important to note, however, that no study has directly compared the effectiveness of various electrode types for around-ear EEG acquis- ition. Nevertheless, considering the relatively hairless nature of the around-ear region, one might speculate that dry electrodes could potentially perform better compared to their usage in conventional scalp EEG setups when contrasted with wet EEG electrodes.

3.2.2.2. Electrode number and location Similar to in-ear EEG studies, there currently is not a standardized approach for measuring around-ear EEG. This lack of standardization extends to elec- trode naming, quantities, and placements. The cEE- Grid and the electrode array discussed in [60] are composed of a total of ten electrodes resulting in a total of 20 electrodes when both ears are equipped with these devices. Other around-ear EEG device has less number of electrodes. Electrode number varies between two to five per one side of the ear in the other device designs. For example, the hybrid elec- trode array, trEEGrid, consists of nine electrodes, four of which are positioned around the ear, three around the eye to serve as EOG sensors, and the last two positioned around the chin to measure EMG of the muscles around the user’s mouth. Earpiece and head- phone designs usually contain four to five electrodes while glasses and hairband design which has a nar- rower coverage area contains one to two electrodes on each side of the ear.

Reference and ground electrodes are commonly selected from the electrodes at the most inferior pos- itions, often situated near the mastoids. However, some studies utilizing the two aforementioned c- shaped electrode arrays use the electrodes at the center of the array, positioned approximately above the auricularis posterior muscles, as reference and

9

<!-- page 11 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

ground electrodes. Additionally, certain hybrid EEG systems that combine electrodes from the around- ear region with electrodes from other locations make use of electrodes positioned outside the ear, such as on the forehead and nose bridge, as reference and ground sites [68, 70]. Device designs such as head- phones, glasses, and headbands, encompass larger areas extending beyond the ear region. This broader coverage area allows for the practical and esthetic incorporation of electrodes from out-of-ear positions into the wearable design, a solution not observed in the context of in-ear EEG configurations.

Furthermore, although a universally accepted nomenclature for these electrodes is lacking, a num- ber of studies have adopted the approach pion- eered by the cEEGrid investigation. This methodo- logy employs the letters ‘L’ or ‘R’ to indicate the left or right ear side, respectively, followed by a numer- ical sequence from ‘1’ to encompass the total count of electrodes on each side (e.g. R1, R2,..., R8). This sequence originates from the most anterior or super- ior part of the design and progresses incrementally. While we find this approach commendable, there are opportunities for refinement to establish it as a standardized method. First, to enhance compre- hensiveness and accommodate future advancements, the nomenclature should extend to encompass the anterior ear region, defining the elliptical shape that surrounds the entire ear area. Second, akin to the standardized 10-20 system employed in conventional scalp EEG setups, the standardization of around- ear EEG systems could benefit from maintaining a fixed percentage-based distance between each elec- trode position relative to the vertices or co-vertices of the elliptical region surrounding the ear. This approach would ensure consistent relative electrode positions during the fabrication of the sensor array, even when adapting the sensor size for various head sizes.

3.3. Signal processing hardware used in ear-EEG studies The hardware of an EEG system can be segmented into three main parts: sensors, the signal processing module, and the computing module. In our discus- sions thus far, we have focused on ear-EEG, which primarily falls within the sensor component of the EEG system. The ear-EEG acquisition system finds its full form when complemented by the signal pro- cessing module. This integral module encompasses hardware for signal processing, amplification, and data transmission to the computing module. While this article will not delve into intricate electronic spe- cifics of the hardware itself, such as circuit schematics and detailed electrical components, we will delve into the EEG amplifier type and its design. This explora- tion is geared toward assessing the system’s wearabil- ity, a pivotal aspect that underscores the very applic- ation of ear-EEG technology.

Despite the strong wearability aspect of ear-EEG as an EEG sensing technique, the majority of ear-EEG studies conducted so far, especially those involving in-ear EEG, have employed professional-grade sta- tionary EEG amplifiers for their experiments. While this approach suits applications of ear-EEG where subjects remain stationary, such as sleep monitor- ing, it does limit the broader potential of the ear- EEG method. Introducing a fusion of the ear-EEG approach with a wearable EEG processing module could significantly enhance the system’s wearability and mobility, potentially making it viable for every- day use. Many studies leverage commercial-grade wearable EEG equipment such as SMARTING mobile amplifier (www.mbraintrain.com) that is used in most around-ear EEG studies involving cEEGrid, OpenBCI biosensing board (www.openbci.com) [20, 26, 29, 44, 52, 65, 69], WANDmini [33], or NeuroSky Mindwave headset (www.neurosky.com) [71, 72] for their signal processing. However, these studies merely attach the equipment to the subject’s attire or place it on a table during experiments, without incorpor- ating any substantial design efforts to create a seam- lessly wearable and stylish system. Some studies, nev- ertheless, has presented a good design incorporating ear-EEG sensors and wearable EEG equipment. For example, Bleichner and Emkes developed a wearable ear-EEG system named nEEGlace, which integrates cEEGrids and the SMARTING into a commercial neck speaker [73]. This innovative design approach not only allows the neck speaker to function as a mount for the EEG amplifier, bringing the entire sys- tem closer to the sensors and reducing wire length but also enables the use of auditory stimuli or feedback for interface-based applications. Additionally, the integ- rated microphone of the neck speaker offers the user voice command options and allows for the recording of environmental sounds. Furthermore, it is worth noting that while cEEGrid was initially designed with ports compatible with the SMARTING, it is pos- sible to create connecting adapters to enable com- patibility with other commercially available wearable EEG devices. This adaptability is demonstrated, for instance, in [74].

Numerous studies forego reliance on commercial EEG devices, opting instead to construct their ear- EEG system with custom-made processing modules [7, 34, 49, 63, 67, 68, 70]. Specifically for in-ear EEG, certain designs are compact enough to be integrated within the earpiece itself, rendering them remarkably wearable and practical for real-world use [47, 48]. As for around-ear EEG, some custom-made processing modules are embedded and encased within wearable devices like headphones, glasses, and headbands as discussed in the previous section.

It is crucial to emphasize that a well-designed wearable EEG system should ensure the proximity of the sensor and processing module components, min- imizing potential noise and artifacts stemming from

10

<!-- page 12 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

lengthy cable connections between the two hardware sections. It is also worth noting that although numer- ous studies have presented ear-EEG systems encom- passing fully wearable setups, there has yet to be a study that ventures into real-world, out-of-laboratory environments. Gaining a comprehensive understand- ing of the practical applicability of ear-EEG neces- sitates a departure from the controlled confines of the laboratory, undertaking experiments in authen- tic everyday settings. This endeavor stands to provide insights into the effectiveness of ear-EEG beyond the- oretical constructs, shedding light on its functionality and reliability in real-life contexts.

## 4. Applications of ear-EEG

Ear-EEG devices are an attractive alternative to more conventional scalp-EEG electrodes due to their com- pactness and wearability in various applications. Studies have been carried out using ear-EEG devices in various domains to analyze the feasibility of using ear-EEG devices, ranging from measuring neuronal response to stimulus to monitoring a subject’s state of mind. In the following section, we split the reviewed studies into different categories based on their inten- ded functions, where the first two sections examine how neurological signals commonly studied in scalp- EEG appear in ear-EEG, and the later sections on various monitoring tasks to which ear-EEGs may be applied. Figure 4 shows the distribution of different applications of ear-EEG studies.

4.1. Reactive responses Reactive responses refer to neuro-signals evoked in response to external stimuli in various forms [75]. While systems that use reactive responses require more preparation and equipment, they normally dis- play a clear, differentiable characteristic in signals that can be matched with the stimuli, making them useful not only for decoding users’ intentions but also for evaluating the quality of the measuring device.

4.1.1. Steady-state response One of the most commonly used reactive responses is the steady-state response (SSR). SSR refers to an electrophysiological response of the brain to stim- uli presented at a specific frequency or range of fre- quencies, characterized by a periodic waveform that corresponds to the frequency of the stimulus and its harmonics [76]. The fixed waveforms induced by the stimuli make it possible to validate the feasibility of an EEG acquisition method by calculating the SNR of the signals at the frequency of the stimuli or by examin- ing the power spectral density (PSD) plot. The stim- uli can be given in a diverse manner, including visual, auditory, or haptic changes.

Several studies have used auditory stimuli to measure the auditory SSR (ASSR) signals [11, 35,

51, 55] to demonstrate the feasibility of using in- ear EEG instead of scalp-EEG devices. Kidmose et al [11] were among the first to examine reactive signals measured using in-ear silver electrodes and collec- ted four different evoked responses, including ASSR, SSVEP, transient auditory evoked potential, and tran- sient visual evoked potential (VEP). They compared the SNR of the collected signals to that collected from wet EEG electrodes placed in the temporal region. Two different frequencies were used for ASSR (40, 80 Hz) and three for SSVEP (10, 15, 20 Hz). While in- ear EEG showed signals with lower amplitude com- pared to scalp EEG, the SNR was maintained at sim- ilar levels. Similarly, Goverdovsky et al [35] showed the feasibility of using a custom-made in-ear device with memory foam and conductive fabric for meas- uring ASSR and VEP signals. Here, auditory stimuli at 40 Hz were provided via an over-the-ear headphone, with visual stimuli given with a red LED. Bertelsen et al [77] measured ASSR using both a generic in- ear device and cEEGrid and examined various elec- trode configurations to determine the setups that led to a higher SNR. They found that the ear-Fpz con- figuration, as well as both within-ear and cross-ear electrode configurations, resulted in statistically sig- nificant ASSRs with the generic earpiece. However, the dry-contact cEEGrid demonstrated a significantly higher average SNR of the ASSR signal compared to the generic earpiece.

Around-ear EEG was also examined by Guermandi et al [60] for its potential use in measur- ing reactive responses. Using a wearable device similar to cEEGrid, they created a system that included the computing unit, which carried out feature extrac- tion and classification on board before transmitting the results via Bluetooth. They validated their sys- tem on various event-related potential (ERP) signals, SSVEP, and ASSR, where SSVEP stimuli were given via checkerboards flickering at 10, 12, and 15 Hz, and ASSR stimuli were given in the form of white noise modulated at 40 Hz.

Kaveh et al [32] proposed an in-ear EEG record- ing platform consisting of six electrodes, with elec- trodes made of silver spray. The device broadcasted the signals wirelessly, and the authors validated their system for use in detecting eye blinks, alpha modula- tion, and ASSR. They found that while existing sys- tems performed better, the platform displayed suffi- cient SNR for use.

Christensen et al [18] used in-ear EEG with six channels to measure ASSR to acquire hearing threshold levels, using different electrode configura- tions. They conducted experiments to validate their approach for both normal and hearing loss subjects. Chiu et al [78] also used an in-ear EEG made with conductive fabric and viscoelastic memory foam to acquire haptic and auditory SSRs, which were used to perform 20 different tasks involving the manipulation of a smartphone.

11

<!-- page 13 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

Figure 4. Distribution of different applications of ear-EEG studies.

Kappel and Kidmose [79] compared the signal qualities of in-ear EEG acquired using different types of electrodes. They created two types of in-ear dry contact electrodes using Ag/AgCl and IrO2 respect- ively and carried out measurement sessions with one type of electrode in each ear, the position of which was swapped between sessions. The experiment con- sisted of measuring the SNR of ASSR evoked by white Gaussian noise, and both types of electrodes demon- strated no significant differences in performance.

The effects of different auditory stimuli were studied by Christensen et al [80, 81]. Using both in- ear and around-ear electrodes, they measured ASSR in response to chirp stimuli with two- different repe- tition rates. While direct comparisons were not made in the study, high repetition rate chirp stimuli showed an improved performance to using click, white noise, or pure tone stimuli when used with ear-EEG for acquiring 40 Hz ASSR. For SSVEP, Mouli et al [82] used a wireless system using a circular ring LED for SSVEP stimulus, which contained an onboard com- puting unit to provide four different frequencies (7, 9, 11, and 13 Hz). A single-channel conductive rub- ber electrode was used together with an OpenBCI wireless EEG acquisition hardware to collect signals

from inside the ear, resulting in SSVEP signals with positive SNR values.

4.1.2. ERPs Apart from SSRs, ERPs are also useful types of responses. ERPs refer to changes in the EEG in response to specific stimuli or events in various forms, such as P300 or N100 signals, which refer to a pos- itive evoked potential at 300 ms after an event and a negatively evoked potential at 100 ms after an event respectively [83]. Similarly to other reactive signals, the clearly defined features make them useful for ana- lyzing the effectiveness of ear-EEG measuring systems [63, 84–86]. ERPs can also offer insights into various cognitive processes such as attention, memory, and language. In 2015, Debener et al [4] recorded around- ear EEG data from an auditory oddball experiment using two cEEGrid systems and confirmed the occur- rence of P300 signals for target stimulus, with clas- sification results up to 70.92%. In the same year, Bleichner et al [87] used a combination of the scalp, around, and in-ear EEG electrodes to create a visual P300 speller. Subjects were instructed to copy one sentence containing 19 symbols per task, achieving a

12

<!-- page 14 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

classification accuracy of 88% and an ITR of 8.33 bits per minute.

ERPs can also be used to identify auditory attention [88–94]. Recently, Ala et al [95] used an in- ear EEG device to measure alpha-related synchron- izations and desynchronizations when continuously attending to speech, with results suggesting that ear- EEG devices can be used to judge a subject’s per- ception of speech. Similarly, Holtze et al [94] meas- ured EEG from around the ear using cEEGrid during a selective auditory attention task, where two audit- ory streams were played simultaneously to the sub- ject, who was instructed to attend to a specific audio. Using speech envelope tracking, they were able to reach average decoding accuracy of 71.3%.

4.2. Active imagery Recently, there have also been investigative studies into the use of ear-EEG for measuring active imager- ies. Active imageries refer to neuronal responses to a subject’s imagery without an external stimulus. Active imageries rely solely on the user’s imagination about a fixed task [75]. Merrill et al [71] defined five men- tal tasks, where subjects were told to relax, imagine a song, listen to a fixed frequency, imagine a face, or imagine a rotating cube, as a mixture of ASSR, visual imagery, and auditory imagery. They recruited 12 students to carry out these tasks and monitored the EEG signals using a Neurosky Mindwave Mobile wireless EEG headset modified to collect signals from inside the ear, achieving a classification accuracy of 85.4% on average, with six subjects performing at accuracies over 90%. In 2019, Merrill et al built on their work further to explore the possibility of using their mental tasks for authentication, where subjects were given a custom in-ear device and nine mental tasks. A task was chosen as a ‘passthought’, with an overall accuracy of 99.82% when detecting this task using three electrodes from the left ear. The custom- made earpiece made the system more robust against an imposter since the mismatched shape lowered the classification performance.

4.2.1. Motor imagery A more commonly used active imagery paradigm is motor imagery, where users focus on imagining moving a part of their body without actually mov- ing the corresponding part. The potential of utilizing around-ear EEG was studied by Kim et al in an invest- igative study where they selected channels near the ear from a standard 10-20 international placement [96]. In this work, they found that EEG signals from Broca’s and Wernicke’s area could be used to classify four- class motor imagery with comparable performance to existing setups, suggesting that ear-EEG devices could be used for measuring motor imagery paradigms. An actual in-ear EEG device was manufactured and tested for motor imagery by Wu et al [21]. They hand- crafted custom-fit ear pieces with Ag/AgCl ink used to

print electrodes for four different positions per ear. Six subjects were recruited for two class MI classific- ation using EEGNet, with scalp EEG acquired simul- taneously to ear-EEG. The acquired ear-EEG signals were re-referenced in various methods before being compared to scalp-EEG in intra-subject and inter- subject classification. While both inter and intra- subject classification showed lower results for ear- EEG, fine-tuning the model with individual data after inter-subject classification led to classification per- formance higher than the chance level.

4.2.2. Speech imagery Another active imagery that has been gathering attention is speech imagery, in which subjects are instructed to imagine articulating a word or phon- eme, without actually moving or producing sound. Given that the auditory cortex and the language cen- ters are positioned close to the regions covered by around-ear EEG, ear-EEG may provide discreet and effective means of acquiring related signals. In 2021, Kaongoen et al [69] were the first to propose an around-ear EEG device to measure speech imagery. Using a custom-made device with gel electrodes, they acquired EEG signals regarding four different words from both around-ear and scalp EEG from ten sub- jects. Using a multi-layer extreme learning machine, their around-ear EEG device showed comparable per- formance to scalp-EEG setups for a five-class classi- fication task consisting of four words and rest. Later, Kaongoen et al [65] further expanded their work to suggest a home appliance control system using speech imagery measured with an around-ear EEG head- phone. In this work, they proposed a hybrid con- trol setup, where user inputs were combined with speech imagery classification results to control a vir- tual television for three different tasks: controlling the volume, changing the channel, and turning the power off.

4.2.3. Visual imagery Visual imagery, as its name suggests, refers to responses measured when subjects imagine a cer- tain image or action happening in front of their eyes. Subjects are shown an action or an object, and then later instructed to imagine the said object on their own. Kuatsjah et al [42] performed a visuo- motor tracking task, where users were instructed to keep track of a moving blue box and mimic its movement by controlling a different yellow box with a joystick. Two different user states, resting and tracking, were monitored using a two-channel wire- less in-ear EEG system. Ten subjects were recruited for the study and showed average accuracy above chance level, demonstrating that visuomotor tasks can be distinguished using in-ear EEG. Similarly for visual imagery, Kosmyna et al [97] used AttentivU, a hybrid EEG device in the form of glasses to test

13

<!-- page 15 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

its effectiveness in visual imagery tasks. The exper- iment consisted of four different images related to either coffee or art, repeated 20 times for 14 subjects. In this work, the authors demonstrated that their glasses-shaped hybrid EEG collection device shows comparative visual imagery classification perform- ance to when using a scalp-EEG device.

4.3. Brain state monitoring While neuronal responses can be useful for validat- ing device performance and decoding user intentions, monitoring the current state of a subject is another important domain where EEG signals can be effect- ively used. In such monitoring tasks, the brain signals of the subject are often measured over a long period of time during a specific activity, making the wearability and comfort of the EEG collection device especially important.

4.3.1. Sleep monitoring For sleep monitoring, ear-EEG has been frequently considered as an alternative to conventional scalp- EEG due to its compact and discreet form, allow- ing continuous monitoring of the user’s sleeping state without much discomfort. Zibrandtsen et al [13] compared the signals from in-ear-EEG and scalp- EEG during different sleep stages. Two experienced sleep scorers were recruited to analyze 21 h of one night’s sleep. The reported results showed 90.9% sim- ilar scores between the two methods, with similar features shown. A memory-foam in-ear EEG elec- trodes was used by Looney et al [36] to measure sig- nals from four healthy male subjects during nap and showed that their device could distinguish between N2/N3 sleep stage, as well as non-REM/wake stage using only ear-EEG signals. Several subsequent stud- ies have provided evidence supporting the utility of in-ear EEG for sleep staging [15, 19, 40, 41, 98–100].

Around-ear EEG has also been studied as an alternative to polysomnography. Sterr et al [101] used cEEGrid to measure around-ear EEG during sleep from 20 subjects simultaneously to standard poly- somnography. Different sleep parameters regarding sleep maintenance and architecture were examined from both signals for the evaluation of quality. Both systems showed similar results to each other, suggest- ing that cEEGrid can provide a viable alternative to existing methods for recording sleep signals.

Recently, Mikkelsen et al [102] performed a study on the performance of self-applied in-ear EEG for sleep monitoring. Ten subjects were recruited from a previous study performed by an expert, with 12 sleep recording sessions carried out by each participant at home. Three different metrics were used to score the quality of sleep in this study: total sleep, sleep latency, and sleep efficiency, for which participants performed similarly to expert-applied experiments even when carrying out the experiment themselves [103]. Another work by Kjaer et al [104] analyzed

the effectiveness of automatic sleep scoring with an in-ear EEG device. In this paper, they reported that repeated automatic sleep scoring with an in-ear EEG device outperforms manually labeled polysomno- graphy consisting of EEG, EMG, and EOG signals. While both methods perform similarly after the first night, ear-EEG has been shown to perform better for six out of eight sleep metrics after two nights.

Furthermore, Henao et al [46] carried out invest- igations on implementing a closed-loop stimulation system during sleep to induce slow oscillations. Using an in-ear EEG device, they proposed a system that detects sleep slow oscillation and then employs aud- itory stimulation to enhance the detected oscillation. In their system, two scalp electrodes and one bipolar in-ear electrode in both ears were used to measure the EEG activities, and a wired headband speaker was used to deliver the auditory stimuli. They evaluated their system on 24 healthy subjects and showed pos- itive results for inducing slow oscillations for eleven subjects.

4.3.2. Mental load Several works have also explored the possibility of monitoring the subjects’ state via ear-EEG. Eye state is one of the most clearly observable responses in EEG signals; when eyes are open, EEG signals show an alpha attenuation response (AAR), referring to alpha band power decreasing. Such characteristic allows eye states and the corresponding AAR to be used to check the signal quality of both in-ear [32, 34, 49, 105] and around-ear [4, 59, 106] devices.

Some studies have used ear-EEG for measuring stress, usually involving mental tasks. Ha et al [107] combined three different biosignals: EEG, hemo- encephalography (HEG), and heart rate variability (HRV) to monitor stress during an n-back task. EEG signals were measured using two channels in an in- ear device and six channels in a forehead headband, with 16 channels and two channels for HEG and HRV measurements respectively. The heart rate sensors were also placed on the in-ear device. A hybrid EEG system in the form of a headband was suggested by Ahn et al [70] for stress assessment, measuring EEG and ECG from behind the ear. Stress was induced with two different mental tasks, the Stroop color- word test and mental arithmetic (MA) tasks, and PSD extracted from EEG as a feature for classification, achieving an accuracy of 87.5% for binary classific- ation of stress/non-stress state.

4.3.3. Vigilance Vigilance is another mental state that has been researched with ear-EEG [33, 108]. Hwang et al [109] was the first work to perform alertness-drowsiness classification using in-ear EEG in a driving scen- ario. Various biosignals, scalp EEG, ECG, PPG, and galvanic skin response (GSR) were measured simul- taneously for comparison in the study, with a single

14

<!-- page 16 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

metallic EEG electrode placed in the right ear canal with gel applied for in-ear EEG acquisition. Thirteen subjects were recruited to drive a simulation of a car on a highway at a given fixed speed, with the driver’s reaction time and facial characteristics recorded to acquire alertness and drowsiness epochs. Hong et al [110] carried out a similar study, with drowsiness measured using a multi-modal device consisting of in-ear EEG, PPG, and ECG. The performance of the device was compared to results from a standard 16- channel scalp-EEG for 16 subjects in a virtual driv- ing task. The proposed system was shown to per- form at a similar level but with a shorter data acquisi- tion length. Kosmyna et al [68] used their proposed glass device to not only detect drowsiness but also provide feedback to redirect vigilance. Their device consisted of two EOG sensors at the nose pad and two EEG channels at around TP9 and TP10, with a piezo- electric element at the tip of the glasses for auditory and vibrotactile feedback. Twenty participants were recruited to perform a driving simulation task, with drowsiness level rated using the Karolinska sleepiness scale. Drowsiness was judged based on an unsuper- vised threshold-based method on the number of blink and fatigue index acquired from EEG signals, and two different biofeedbacks, auditory and vibrotactile, given to redirect vigilance.

4.3.4. Emotion recognition Emotion recognition has emerged as a notable research domain, although there exists a limited num- ber of studies that have explored the utilization of ear- EEG for this purpose. Li et al [72] was the first to propose a low-cost in-ear EEG device, made by refit- ting a Neurosky Mindset EEG headset, to distinguish three emotion states: negative, relaxed, and excited. Twelve subjects were recruited for the study, who were instructed to watch a video and listen to music to induce emotional changes. The outcomes of the study suggested that single-channel in-ear EEG can be suit- able for emotional recognition, albeit with poor per- formance in terms of arousal recognition. Another in-ear EEG device was suggested by Athavipach et al [52] for the classification of four discrete emotional states. Twelve participants were recruited, with images from the international affective picture system and the Geneva affective picture database used as visual emotional stimuli and classical music pieces selec- ted from another auditory emotional research used as auditory stimuli. Compared to electrode channels from T7 and T8, the in-ear EEG showed no significant difference in performance.

4.3.5. Epileptic seizure detection Traditional scalp EEG recordings are the gold stand- ard for detecting epileptic seizures, but they have lim- itations, such as being affected by muscle artifacts and being unable to detect deep-seated epileptic foci. In contrast, ear-EEG recordings can be less affected by

artifacts and can be worn more comfortably for a longer period of time. Recent studies have demon- strated the feasibility and effectiveness of using ear- EEG for seizure detection in patients with epilepsy. Zibrandtsen et al [13, 111] used an in-ear device with four electrodes per ear to record signals from 15 subjects suspected to suffer from seizure, showing no significant differences in performance in seizure detection when compared to conventional scalp-EEG systems.

Around-ear EEG has also been frequently used for seizure detection. You et al [112, 113] suggested a cross-head electrode layout, with two electrodes in form of a gold cup placed behind each ear. Fifty- four patients were recruited for the study, with eval- uations carried out through visual inspection by a neurologist, subject-independent classification, and subject-dependent classification. The results showed that around-ear EEG detected seizures better com- pared to patients’ self-reports. Vadecasteele et al [114] similarly employed cross-head channels around the ear to detect seizures using an unsupervised gener- ative adversarial network (GAN). Spectrograms from the acquired signals were used as the input to train a deep convolutional GAN to learn the normal state. The trained GAN was then used to detect an abnor- mality, with an accuracy of 96.6% [115].

Due to the uncertain nature of seizures and when they may occur, studies involving the long-term use of ear-EEG for monitoring are essential. Several works investigated the robustness of devices with ear-EEG when measured over a continuously long period of time [116]. Nielson et al [117] carried out continuous recording of wearable EEG, ECG, and accelerometry in 30 patients, who were given the freedom to move around. Electrodes were placed bilaterally behind the ear on the upper mastoid, with reference placed on Cz. Classification using a support vector machine showed an improved performance to using only EEG, with high sensitivity and low false alarm rate. In addi- tion, Musaeus et al [22] introduced an in-ear EEG sys- tem designed for the long-term monitoring of epilep- tiform activity in patients with Alzheimer’s disease. They investigated the comfort of the patients wearing the in-ear EEG device by recruiting ten patients suf- fering from mild to moderate cases of Alzheimer’s dis- ease. Three sessions of EEG recordings were carried out, each being up to 48 h long with several months between the sessions. All patients managed to wear the device for over 24 h, and four patients completed the study.

In summary, this section provides an overview of the capabilities of ear-EEG as a tool for acquir- ing various types of EEG signals commonly util- ized in neuro-engineering and biomedical studies, along with its applications. While the potential of ear- EEG is evident from these studies, it is important to acknowledge that the field is still in its nascent stages. Given the multitude of variables that can influence

15

<!-- page 17 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

research outcomes—including subjects, device con- figurations, and environmental factors—it becomes invaluable to observe results from diverse studies to validate consistent findings. Nonetheless, the exist- ing body of ear-EEG research, particularly within the active imagery and brain state monitoring domains such as emotion recognition, remains limited. As a result, drawing definitive conclusions from this emer- ging field should be done with careful consideration. Moreover, when adopting the ear-EEG methodology within a new paradigm, it is advisable to directly compare its performance against the conventional scalp-EEG method using the same experiment con- figurations. This comparative analysis would facilit- ate a better understanding of how effectively ear-EEG performs in relation to the well-established conven- tional scalp-EEG method, which has a more extensive research foundation.

## 5. Limitations of ear-EEG and methods to overcome them

While the previous section highlights the potential of ear-EEG in various applications, it is important to acknowledge that ear-EEG techniques have cer- tain drawbacks in comparison to conventional EEG acquisition methods. These limitations may affect their performance in specific applications, particu- larly those that require monitoring of brain activity in regions further away from the ears. To overcome these limitations, various methods and algorithms have been developed specifically to improve the quality of the ear-EEG technique. In this section, we will discuss some of these techniques that have been reported in previous literature.

5.1. Re-referencing methods EEG acquisition conventionally requires a reference electrode. The electrical potential recorded at each scalp electrode is the result of the difference in elec- trical potential between that electrode and the refer- ence electrode, so the choice of reference electrode can affect the interpretation of EEG data [1]. In ear- EEG techniques, the choice for the reference elec- trode is limited due to the small coverage of the com- pact structure of the ear-EEG devices. As discussed in section 3, in the absence of any external out-of-ear electrode, the reference and ground points of an ear- EEG system are typically situated within the concha for in-ear EEG setups, and at the lowermost posi- tions for around-ear EEG configurations. Researchers may also re-reference EEG data post hoc to another reference point to produce different interpretations of the data or improve the quality of the signal. We will review the re-referencing techniques employed in ear-EEG research, covering both traditional and innovative methods, and explore the implications of different approaches.

The common average referencing (CAR) tech- nique is a commonly used EEG re-referencing tech- nique that involves creating an average of all EEG channels and subtracting the resulting signal from each channel [15]. However, this technique assumes a uniform spatial distribution of the electrodes, which is not applicable in non-traditional electrode place- ments such as ear-EEG techniques. In these cases, the average reference may be biased towards more densely populated electrode areas, leading to suboptimal res- ults. To address this issue, researchers have proposed alternative re-referencing techniques. For instance, Kappel et al [118] conducted a study on ASSR using in-ear EEG and suggested a method called optim- ized reference configuration (ORC) that assigns dif- ferent weights to each electrode in the re-referencing process. The weights were trained by maximizing the SNR of the first harmonic of the steady-state response from the training dataset. They also pro- posed a location weighted referencing (LWR) tech- nique that assigns separate weights to the electrodes based on the location and distribution of the elec- trodes. Specifically, electrodes in the concha and canal areas of the ear are weighted differently. Results from the study indicate that the ORC method produced the highest SNR of the steady-state response compared to the CAR and LWR methods. In 2019, Choi and Hwang [106] conducted a comprehensive compar- ison of various re-referencing techniques used in pre- vious studies. They used around-ear-EEG open data- sets recorded while subjects performed an alpha mod- ulation task, and two active mental tasks: MA and mental singing. Five re-referencing techniques that were used in the previous ear-EEG research including (1) CAR [15], (2) contralateral-mean (using the mean of contralateral electrodes as the reference point) [12], (3) ipsilateral-mean (using the mean of ipsi- lateral electrodes as the reference point) [16], (4) contralateral-bipolar (using bipolar configuration on contralateral ear sides) [119], and (5) ipsilateral- bipolar (using bipolar configuration on ipsilateral ear sides) [119], were applied to the data. The results showed that the contralateral-mean method provided statistically higher SNRs and classification results in all mental tasks, suggesting that it might be an effi- cient choice of re-referencing method for the ear- EEG data and thereby increase the quality of the ear-EEG data. However, it should be noted that the contralateral-mean method does not apply to ear- EEG systems that consist only of one side of the user’s ear or systems in which electrodes from both ears are not physically connected.

Additionally, it is worth noting that active EEG electrodes do not require a common reference elec- trode. This is because active electrodes have a built- in preamplifier that amplifies the signal and sends it directly to the recording device, whereas passive electrodes require a reference electrode to provide a baseline for the recording [120]. With active

16

<!-- page 18 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

electrodes, each electrode acts as its own reference, allowing for a more flexible and scalable recording setup. An active wearable ear-EEG system presented in [70] showed an innovative way to acquire both EEG and ECG data using only two active channels each located behind each ear and one reference electrode located at the forehead. The system utilized a refer- ence configuration that involves subtracting the ref- erence signal from the signal obtained from the left and right active electrodes, respectively, to acquire two EEG signals. The ECG signal is obtained by sub- tracting the signal from the right active electrode from that of the left electrode. This reference setup ensures that the EEG signals are spatially balanced, which is essential for obtaining asymmetry features from the EEG data. Furthermore, the system enables the sim- ultaneous acquisition of HRV features from ECG data along with EEG data, without requiring additional electrodes. These features made the proposed system suitable for stress assessment in daily life.

5.2. Noise cancellation and artifact removal techniques on ear-EEG Creating a wearable EEG system presents significant obstacles, primarily due to noise and artifacts. In con- trast to a controlled laboratory environment, real- world scenarios are exposed to numerous sources of noise and artifacts, both internal and external. Noise cancellation and artifact removal techniques play vital roles in the development of a reliable wearable EEG system. These methods filter out unwanted noise and artifacts from the EEG signal, leading to more accur- ate and dependable signals and allowing the extrac- tion of meaningful insights. As a result, integrating these techniques is essential for the efficacy and suc- cess of wearable EEG systems.

While there are some variations in the noise and artifacts observed in ear-EEG compared to con- ventional scalp-EEG, such as ear-EEG being less affected by eye blinks and movements but more susceptible to artifacts associated with jaw muscle contractions, the algorithms used in scalp-EEG can generally be applied to ear-EEG with only minor modifications [121]. In fact, the study in [122] demonstrated that independent component analysis (ICA) can be used to detect artifacts in around-ear EEG obtained from cEEGrids and the artifact ICA components showed similar characteristics to those of scalp-EEG data. Despite the lack of noise cancella- tion or artifact removal techniques tailored specific- ally to ear-EEG data, we will review some innovat- ive approaches that have been successfully applied to wearable ear-EEG systems. In their 2020 paper, YE Lee and colleagues proposed a method for remov- ing artifacts from EEG signals called constrained ICA with online learning (cIOL) [123]. The cIOL method uses constrained ICA to estimate artifacts from the EEG signals using reference signals, and recursive least squares to extract an artifact-free EEG

signal. The reference signals used in their experi- ment were obtained from isolated electrodes, which were blocked with high-resistance material to pre- vent brain signals from passing through. In their study, four electrodes, two from each side of the cEEGrids, were used as the isolated electrodes. The authors evaluated the performance of the cIOL method in ERP and SSVEP experiments where sub- jects were walking on a treadmill and compared it to other state-of-the-art artifact removal methods, such as artifact subspace reconstruction (ASR) [124], Riemannian ASR [125], and fast-Fourier-transform- based methods [126]. The results showed that the cIOL method achieved the best classification accuracy across all experimental settings. Moreover, the results showed that using isolated signals as reference sig- nals for estimating the artifacts produced slightly bet- ter outcomes than using IMU data. Nonetheless, this method has only been tested with motion artifacts and may not perform as effectively with other types of noise or artifacts that could be present in real-life scenarios. The study in [45] added two microphone sensors (different positions) and an accelerometer to the viscoelastic in-ear-EEG device to capture the noises. They combined noise-assisted multivariate empirical mode decomposition (NA-MEMD) with normalized least mean square adaptive noise cancel- lation (NLMS-ANC) technique to produce an innov- ative artifact removal method for the ear-EEG data. In summary, their method involved inputting sig- nals from ear-EEG electrodes, two microphones, and an accelerometer to the NA-MEMD to generate the intrinsic mode functions (IMFs). Then, each pair of ear-EEG IMF and one of the noise-sensor IMFs is fed independently to the NLMS-ANC to clean the ear-EEG IMFs, and finally, the clean ear-EEG IMFs are then added up together again to recon- struct the denoised ear-EEG data. Results showed that the denoised EEG signals demonstrated reduced power in the frequency range where artifacts were present. Moreover, the performance of different noise sensors varied for the tested artifacts. Specifically, microphones were found to be more sensitive to arti- facts caused by internal motion within the ear canal, such as chewing, whereas accelerometers were more effective for artifacts resulting from full-body move- ments, such as walking. Both methods described in the studies above require sensors that are separate from the EEG electrodes to capture noise. It is possible that combining multiple types of noise sensors could enhance the effectiveness of these methods. However, the tradeoff between device performance, cost, and wearability must be carefully considered.

Apart from using noise cancellation and artifact removal methods, the hardware design also plays a crucial part in the quality of the EEG signal as well. In section 3, we discussed the design aspects of wearable devices, including electrode selection, and device shape and material, all of which contribute

17

<!-- page 19 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

to improving the quality of the ear-EEG signals and reducing noise and artifacts. Electrical circuit tech- niques, such as impedance boosting, DC servo loop, and active shielding can also be used to improve the signal quality as well [24, 27, 127, 128]. Corrected double sampling (CDS) is typically implemented in analog circuits by allowing a capacitor in the ampli- fier feedback loop to reset and store noise observed at the front end with the input electrode disconnec- ted. Upon reconnecting the electrode to sample the noise stored in the capacitor, the noise from the first sample is canceled from the electrode sample [105]. CDS is commonly utilized to reduce the impact of 1/f and thermal noises. In 2022, Paul et al [105] proposed utilizing a digital version of the CDS method for an in-ear EEG system. They investigated various weight- ing schemes on the CDS reference samples (distinct from the reference used in the EEG acquisition pro- cess) to subtract them from real samples and gener- ate denoised EEG samples. The study demonstrated that the digital CDS method efficiently reduced 1/f noise and kT/C thermal noise from the ear-EEG data. The Kaiser-22 window with a width of 20 exhib- ited the best performance, resulting in a 71.1% noise reduction.

5.3. Enhancing ear-EEG performance with machine learning and signal processing techniques There exist several methods for advancing the devel- opment of wearable ear-EEG systems. A notable research domain pertains to enhancing the device itself, where efforts are dedicated to developing ear-EEG sensors and circuits or refining the sys- tem’s design to make it more wearable and user- friendly. Another research area entails refining sig- nal processing techniques to eliminate noise and gain more meaningful insights from ear-EEG data. In this section, we will review machine learning approaches tailored to enhance the performance of the ear-EEG system.

One of the primary limitations of ear-EEG tech- niques is their limited coverage area. Certain brain signals dominate in specific regions, such as the visual cortex in the occipital area where SSVEP, com- monly used in BCI systems, is prominent. However, when EEG is obtained from locations farther away from its dominant region, such as the ear area, its signal quality decreases [6, 129]. This can res- ult in suboptimal performance of the ear-EEG tech- nique in specific applications compared to conven- tional methods. To address this challenge, one poten- tial solution is to establish a relationship between ear-EEG and conventional scalp-EEG and use the acquired ear-EEG data to estimate EEG data at the target brain area, thereby enhancing the perform- ance of the ear-EEG system. It is demonstrated in [5] using in-ear EEG data acquired from several experimental schemes, including alpha-attenuation, auditory onset, and mismatch-negativity responses,

that there is high mutual information between the ear-EEG and scalp-EEG data, especially in the tem- poral region. It is also shown that it is possible to use a linear model to predict scalp-EEG data from the given ear-EEG data when a shared common ref- erence electrode is used between the two methods. Furthermore, employing a forward model, the study in [6] also demonstrates the sensitivity of around- ear EEG to different cortical sources and draws the same conclusion that ear-EEG is most sensitive to the sources in the temporal cortex.

Building on this concept, Kwak et al [129] pro- posed an error correction regression (ECR) frame- work that enhances the performance of ear-EEG in detecting SSVEPs. The ECR framework utilizes estim- ated EEG signals on the occipital area by establishing linear and nonlinear relations between the ear-EEG and scalp-EEG. The framework comprises two regres- sion processes. Firstly, the first regression process is trained to predict the scalp-EEG samples from the ear-EEG samples. Secondly, using the error calculated from the first regression process, the second regres- sion process is trained to estimate the errors from the given ear-EEG samples. Finally, the error-corrected outputs are calculated by subtracting the predicted scalp-EEG samples from the estimated error values. To select the regression model in the first process, the authors evaluated three methods including multiple linear regression, ridge regression (RR), and kernel RR (KRR). They selected the regression model that gave the highest correlation value between the pre- dicted and actual scalp-EEG samples. In the second process, KRR was used as the regression model. The authors’ results demonstrated that ECR significantly improves the classification accuracy of ear-EEG in the SSVEP-based experiment and the improvements were the highest compared to using a regression model solely. Israsena and Pan-Ngum [130] developed a dif- ferent approach by estimating scalp-EEG data from ear-EEG data in a different domain to enhance SSVEP classification accuracy. Their approach involved a regression step that was incorporated into the convo- lutional neural network (CNN) model after the out- put layer to re-estimate the softmax values before gen- erating the classification result. To be precise, they fed the EEG data from T7, T8, and Oz channels into a CNN model individually to obtain their respective softmax values. Next, they trained a regression model to estimate the Oz data’s softmax values from those of the T7 and T8 data. Finally, during testing, the regres- sion model re-estimated the softmax values of the T7 and T8 data before generating the classification result using the typical approach. Their technique demon- strated superior SSVEP classification accuracy com- pared to using data from T7 and T8 channels alone without the regression step. In the future, it would be fascinating to observe the further development and application of this method with other types of brain signals to evaluate the ear-to-scalp prediction

18

<!-- page 20 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

method’s concept more comprehensively. Liang et al [131] proposed another solution to the lower SSVEP response in the ear area compared to the occipital area. They hypothesized that there is a phase differ- ence in the SSVEP response in the ear area between the left and right visual field stimulation from the SSVEP biphasic stimulation paradigm. To enhance the SSVEP response in the ear area, they adjusted the phase of the left and right visual field stimulus by estimating the phase difference between the SSVEPs from the two types of stimuli obtained from the ear area. By adding the estimated phase difference to the initial phase of the right visual field stimulus, the new phase difference would become zero, enhancing the sum response from the left and right visual stimuli in the ear area and improving the SSVEP recognition performance of the ear-EEG. Their method was valid- ated, and the results showed that the phase optimizing method in the SSVEP biphasic stimulation paradigm significantly increased the SSVEP classification accur- acy of the ear-EEG.

Additionally, several research works have focused on developing classification models to improve the performance of ear-EEG systems. While few clas- sification algorithms are specific to ear-EEG, some novel algorithms have been proposed to enhance the performance of ear-EEG systems. This review dis- cusses such algorithms, which can also apply to other types of EEG systems. One such algorithm proposed by Lee and Lee [132] is a two-stream deep neural network that combines a CNN stream for extract- ing frequency-domain features and a long-short term memory stream for extracting time-domain features. The extracted features from both streams are then combined to map the classification output. This method was successfully validated in SSVEP-based BCI experiments conducted in an ambulatory envir- onment. Zhu et al [133] re-implemented the well- known EEGNet [134], a compact CNN designed for EEG-based BCI, by experimenting with differ- ent kernel numbers and utilizing an ensemble learn- ing strategy to enhance the performance of ear- EEG, which has weak SSVEP compared to the con- ventional method. Ensemble EEGNet showed sig- nificantly higher classification results compared to canonical correlation analysis and normal EEGNet with different kernel numbers. In 2021, Lee [135] proposed an ensemble-based approach that utilizes CNNs to classify ERP responses from ear-EEG sig- nals. This method involves dividing non-target data samples into four groups and forwarding one group of non-target data and target data to each ensemble model, which is a three-layer CNN. The network then updates the weights by averaging the gradients of all four groups and combines the predictions of all four ensemble models to produce the final prediction output. This approach also addresses the imbalance problem of the ERP data, and the results were satis- factory even though the experiments were conducted

in an ambulatory environment. Recently, Borup et al [136] proposed a novel approach to enhance the per- formance of sleep-state scoring using ear-EEG data by employing ensemble learning and knowledge distilla- tion. The method consisted of two phases. In the first phase, they trained a set of individual baseline models (SeqSleepNet [137]) using classical supervised learn- ing with different random initialization. Ensemble models were then formed by taking the unweighted average of the predictions from multiple individual models. In the second phase, the ensemble model was used as a teacher model in the knowledge distilla- tion process. Pseudo labels generated from the teacher model, along with optionally labeled training data, were used to train a single student model. The res- ults demonstrated a notable improvement in accuracy from ensemble models compared to the individual baseline models. Moreover, without any alteration in the model architecture, their semi-supervised know- ledge distillation approach enabled a single student model to retain 50% to 100% of the improvements obtained by the ensemble models, while also reducing the computational cost.

## 6. Conclusion

In conclusion, the ear-EEG technology has rapidly gained attention in recent years due to its excellent wearability, making it a promising alternative to con- ventional EEG methods. Ear-EEG offers a conveni- ent and non-invasive way to capture brain activity, which is essential for applications in the real world outside research and clinical settings. Our compre- hensive review of the literature on ear-EEG highlights the significant advances made in this technology, including the development of novel ear-EEG wearable device designs, its efficient performance comparable to the conventional EEG setup in the various types of applications in BCI research fields, and signal pro- cessing and analyzing techniques that could increase the performance of ear-EEG.

However, despite these advancements, ear-EEG still faces challenges and limitations. The main dis- advantage of ear-EEG is its small and specific cover- age area, which may limit the quality of signal types it can detect and the applications it can offer. To overcome this challenge, future research should focus on signal processing or machine learning techniques such as signal estimation techniques that estimate EEG at a specific brain area using only data acquired from ear-EEG, which could enhance the quality of ear-EEG signals. Furthermore, noise reduction and artifact removal techniques are essential for wear- able EEG systems, and their integration with ear-EEG technology will be crucial to achieving the ultimate goal of making ear-EEG a viable brain-monitoring system that can be used in daily life.

It is important to note that ear-EEG research is still in its early stages, and more studies should be

19

<!-- page 21 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

conducted to generalize the results. Future studies should also focus on performing experiments in real- world settings, which is the main purpose of the ear- EEG method. Such studies will provide insight into the practical applications of ear-EEG in various real- world contexts. Despite these challenges, the potential of ear-EEG technology cannot be underestimated. We believe that it will continue to generate interest and open up new avenues of research in the coming years.

Overall, ear-EEG technology represents a prom- ising and exciting direction for the field of wearable EEG systems and neural engineering, and we look for- ward to seeing further developments and applications in the future.

## Data availability statement

No new data were created or analyzed in this study.

## Acknowledgments

This work was supported in part by Institute of Information & Communications Technology Planning & Evaluation (ITTP) funded by the Korea government (MSIT) (No. 2017-0-00432) and in part by the National Research Foundation of Korea grant funded by the Korea government (No. 2021R1C1C2012437). Jin Woo Choi participated in this study when he was with the Information and Electronics Research Institute at Korea Advanced Institute of Science and Technology.

## ORCID iDs

Netiwit Kaongoen https://orcid.org/0000-0002- 5935-9662 Jaehoon Choi https://orcid.org/0000-0002-6074- 711X Byung Hyung Kim https://orcid.org/0000-0003- 3374-0876 Sungho Jo https://orcid.org/0000-0002-7618- 362X

## References

[1] Teplan M et al 2002 Fundamentals of EEG measurement

Meas. Sci. Rev. 2 1–11 [2] Casson A J 2019 Wearable EEG and beyond Biomed. Eng.

Lett. 9 53–71 [3] Kidmose P, Looney D and Mandic D P 2012 Auditory

evoked responses from ear-EEG recordings 2012 Annual Int. Conf. of the IEEE Engineering in Medicine and Biology Society (IEEE) pp 586–9 [4] Debener S, Emkes R, De Vos M and Bleichner M 2015

Unobtrusive ambulatory EEG using a smartphone and flexible printed electrodes around the ear Sci. Rep. 5 16743 [5] Mikkelsen K B, Kidmose P and Hansen L K 2017 On the

keyhole hypothesis: high mutual information between ear and scalp EEG Front. Hum. Neurosci. 11 341 [6] Meiser A, Tadel F, Debener S and Bleichner M G 2020 The

sensitivity of ear-EEG: evaluating the source-sensor relationship using forward modeling Brain Topogr. 33 665–76

[7] Ne C K H, Muzaffar J, Amlani A and Bance M 2021

Hearables, in-ear sensing devices for bio-signal acquisition: a narrative review Expert Rev. Med. Devices 18 95–128 [8] Röddiger T, Clarke C, Breitling P, Schneegans T, Zhao H,

Gellersen H and Beigl M 2022 Sensing with earables: a systematic literature review and taxonomy of phenomena Proc. ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies vol 6 pp 1–57 [9] Looney D, Park C, Kidmose P, Rank M L, Ungstrup M,

Rosenkranz K and Mandic D P 2011 An in-the-ear platform for recording electroencephalogram 2011 Annual Int. Conf. of the IEEE Engineering in Medicine and Biology Society (IEEE) pp 6882–5 [10] Looney D, Kidmose P, Park C, Ungstrup M, Rank M L,

Rosenkranz K and Mandic D P 2012 The in-the-ear recording concept: user-centered and wearable brain monitoring IEEE Pulse 3 32–42 [11] Kidmose P, Looney D, Ungstrup M, Rank M L and

Mandic D P 2013 A study of evoked potentials from ear-EEG IEEE Trans. Biomed. Eng. 60 2824–30 [12] Mikkelsen K B, Kappel S L, Mandic D P and Kidmose P

2015 Eeg recorded from the ear: characterizing the ear-EEG method Front. Neurosci. 9 438 [13] Zibrandtsen I, Kidmose P, Otto M, Ibsen J and Kjaer T

2016 Case comparison of sleep features from ear-EEG and scalp-EEG Sleep Sci. 9 69–72 [14] Fiedler L, Obleser J, Lunner T and Graversen C 2016

Ear-EEG allows extraction of neural responses in challenging listening scenarios-a future technology for hearing aids? 2016 38th Annual Int. Conf. of the IEEE Engineering in Medicine and Biology Society (EMBC) (IEEE) pp 5697–700 [15] Mikkelsen K B, Villadsen D B, Otto M and Kidmose P 2017

Automatic sleep staging using ear-EEG Biomed. Eng. Online 16 1–15 [16] Zibrandtsen I, Kidmose P, Christensen C and Kjaer T W

2017 Ear-EEG detects ictal and interictal abnormalities in focal and generalized epilepsy–a comparison with scalp EEG monitoring Clin. Neurophysiol. 128 2454–61 [17] Bech Christensen C, Hietkamp R K, Harte J M, Lunner T

and Kidmose P 2018 Toward EEG-assisted hearing aids: objective threshold estimation based on ear-EEG in subjects with sensorineural hearing loss Trends Hear. 22 2331216518816203 [18] Christensen C B, Harte J M, Lunner T and Kidmose P 2017

Ear-EEG-based objective hearing threshold estimation evaluated on normal hearing subjects IEEE Trans. Biomed. Eng. 65 1026–34 [19] Mikkelsen K B, Tabar Y R, Kappel S L, Christensen C B,

Toft H O, Hemmsen M C, Rank M L, Otto M and Kidmose P 2019 Accurate whole-night sleep monitoring with dry-contact ear-EEG Sci. Rep. 9 16824 [20] Merrill N, Curran M T, Gandhi S and Chuang J 2019

One-step, three-factor passthought authentication with custom-fit, in-ear EEG Front. Neurosci. 13 354 [21] Wu X, Zhang W, Fu Z, Cheung R T and Chan R H 2020 An

investigation of in-ear sensing for motor task classification J. Neural Eng. 17 066010 [22] Musaeus C S, Waldemar G, Andersen B B, Høgh P,

Kidmose P, Hemmsen M C, Rank M L, Kjær T W and Frederiksen K S 2022 Long-term EEG monitoring in patients with Alzheimer’s disease using ear-EEG: a feasibility study J. Alzheimer’s Dis. 90 1–11 [23] Kappel S L, Rank M L, Toft H O, Andersen M and

Kidmose P 2018 Dry-contact electrode ear-EEG IEEE Trans. Biomed. Eng. 66 150–8 [24] Kappel S L and Kidmose P 2018 Real-life dry-contact

ear-EEG 2018 40th Annual Int. Conf. of the IEEE Engineering in Medicine and Biology Society (EMBC) (IEEE) pp 5470–4 [25] Eickenscheidt M, Schäfer P, Baslan Y, Schwarz C and

Stieglitz T 2020 Highly porous platinum electrodes for dry ear-EEG measurements Sensors 20 3176

20

<!-- page 22 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

[26] Das A et al 2022 Surface potential simulation and electrode

design for in-ear EEG measurement 2022 44th Annual Int. Conf. of the IEEE Engineering in Medicine & Biology Society (EMBC) (IEEE) pp 937–40 [27] Zhou X, Li Q, Kilsgaard S, Moradi F, Kappel S L and

Kidmose P 2016 A wearable ear-EEG recording system based on dry-contact active electrodes 2016 IEEE Symp. on VLSI Circuits (VLSI-Circuits) (IEEE) pp 1–2 [28] Jeong D-H, Jeong J, Chae Y and Choi H 2017 Identification

of attention state for menu-selection using in-ear EEG recording 2017 5th Int. Winter Conf. on Brain-Computer Interface (BCI) (IEEE) pp 112–4 [29] Jeong D-H and Jeong J 2020 In-ear EEG based attention

state classification using echo state network Brain Sci. 10 321 [30] Kidmose P, Looney D, Jochumsen L and Mandic D P 2013

Ear-EEG from generic earpieces: a feasibility study 2013 35th Annual Int. Conf. of the IEEE Engineering in Medicine and Biology Society (EMBC) (IEEE) pp 543–6 [31] Bertelsen A R, Bladt H, Christensen C B, Kappel S L,

Toft H O, Rank M L, Mikkelsen K B and Kidmose P 2019 Generic dry-contact ear-EEG 2019 41st Annual Int. Conf. of the IEEE Engineering in Medicine and Biology Society (EMBC) (IEEE) pp 5552–5 [32] Kaveh R, Doong J, Zhou A, Schwendeman C, Gopalan K,

Burghardt F L, Arias A C, Maharbiz M M and Muller R 2020 Wireless user-generic ear EEG IEEE Trans. Biomed. Circuits Syst. 14 727–37 [33] Schwendeman C, Kaveh R and Muller R 2022 Drowsiness

detection with wireless, user-generic, dry electrode ear EEG 2022 44th Annual Int. Conf. of the IEEE Engineering in Medicine & Biology Society (EMBC) (IEEE) pp 9–12 [34] Paul A, Lee M, Xu Y, Deiss S and Cauwenberghs G 2022 A

versatile in-ear biosensing system for continuous brain and health monitoring 2022 IEEE Int. Symp. on Circuits and Systems (ISCAS) (IEEE) pp 620–4 [35] Goverdovsky V, Looney D, Kidmose P and Mandic D P

2015 In-ear EEG from viscoelastic generic earpieces: robust and unobtrusive 24/7 monitoring IEEE Sens. J. 16 271–7 [36] Looney D, Goverdovsky V, Rosenzweig I, Morrell M J and

Mandic D P 2016 Wearable in-ear encephalography sensor for monitoring sleep. Preliminary observations from nap studies Ann. Am. Thoracic Soc. 13 2229–33 [37] Nakamura T, Goverdovsky V and Mandic D P 2017 In-ear

EEG biometrics for feasible and readily collectable real-world person authentication IEEE Trans. Inf. Forensics Secur. 13 648–61 [38] Nakamura T, Goverdovsky V, Morrell M J and Mandic D P

2017 Automatic sleep monitoring using ear-EEG IEEE J. Transl. Eng. Health Med. 5 1–8 [39] Nakamura T, Alqurashi Y D, Morrell M J and Mandic D P

2018 Automatic detection of drowsiness using in-ear EEG 2018 Int. Joint Conf. on Neural Networks (IJCNN) (IEEE) pp 1–6 [40] Alqurashi Y D, Nakamura T, Goverdovsky V, Moss J,

Polkey M I, Mandic D P and Morrell M J 2018 A novel in-ear sensor to determine sleep latency during the multiple sleep latency test in healthy adults with and without sleep restriction Nat. Sci. Sleep 385–96 [41] Nakamura T, Alqurashi Y D, Morrell M J and Mandic D P

2019 Hearables: automatic overnight sleep monitoring with standardized in-ear EEG sensor IEEE Trans. Biomed. Eng. 67 203–12 [42] Kuatsjah E, Zhang X, Khoshnam M and Menon C 2019

Two-channel in-ear EEG system for detection of visuomotor tracking state: a preliminary study Med. Eng. Phys. 68 25–34 [43] Hammour G M and Mandic D P 2021 Hearables: Making

sense from motion artefacts in ear-EEG for real-life human activity classification 2021 43rd Annual Int. Conf. of the IEEE Engineering in Medicine & Biology Society (EMBC) (IEEE) pp 6889–93

[44] Mandekar S, Holland A, Thielen M, Behbahani M and

Melnykowycz M 2022 Advancing towards ubiquitous EEG, correlation of in-ear EEG with forehead EEG Sensors 22 1568 [45] Occhipinti E, Davies H J, Hammour G and Mandic D P

2022 Hearables: artefact removal in ear-EEG for continuous 24/7 monitoring 2022 Int. Joint Conf. on Neural Networks (IJCNN) (IEEE) pp 1–6 [46] Henao D, Navarrete M, Juez J Y, Dinh H, Gómez R,

Valderrama M and Le Van Quyen M 2022 Auditory closed-loop stimulation on sleep slow oscillations using in-ear EEG sensors J. Sleep Res. 31 e13555 [47] Ahn J, Ku Y, Kim D, Sohn J, Kim J-H and Kim H 2018

Wearable in-the-ear EEG system for SSVEP-based brain–computer interface Electron. Lett. 54 413–4 [48] Guermandi M, Cossettini A, Benatti S and Benini L 2022 A

wireless system for EEG acquisition and processing in an earbud form factor with 600 hours battery lifetime 2022 44th Annual Int. Conf. of the IEEE Engineering in Medicine & Biology Society (EMBC) (IEEE) pp 3139–45 [49] Sintotskiy G and Hinrichs H 2020 In-ear-EEG–a portable

platform for home monitoring J. Med. Eng. Technol. 44 26–37 [50] Paul A, Hota G, Khaleghi B, Xu Y, Rosing T and

Cauwenberghs G 2021 Attention state classification with in-ear EEG 2021 IEEE Biomedical Circuits and Systems Conf. (BioCAS) (IEEE) pp 1–5 [51] Athavipach C, Pan-Ngum S and Israsena P 2018

Development of low-cost in-the-ear EEG prototype 2018 15th Int. Joint Conf. on Computer Science and Software Engineering (JCSSE) (IEEE) pp 1–6 [52] Athavipach C, Pan-Ngum S and Israsena P 2019 A wearable

in-ear EEG device for emotion monitoring Sensors 19 4014 [53] Lee J H, Lee S M, Byeon H J, Hong J S, Park K S and

Lee S-H 2014 CNT/PDMS-based canal-typed ear electrodes for inconspicuous EEG recording J. Neural Eng. 11 046014 [54] Dong H, Matthews P M and Guo Y 2016 A new soft

material based in-the-ear EEG recording technique 2016 38th Annual Int. Conf. of the IEEE Engineering in Medicine and Biology Society (EMBC) (IEEE) pp 5709–12 [55] Kappel S L and Kidmose P 2017 High-density ear-EEG

2017 39th Annual Int. Conf. of the IEEE Engineering in Medicine and Biology Society (EMBC) (IEEE) pp 2394–7 [56] Paul A, Akinin A, Lee M S, Kleffner M, Deiss S R and

Cauwenberghs G 2019 Integrated in-ear device for auditory health assessment 2019 41st Annual Int. Conf. of the IEEE Engineering in Medicine and Biology Society (EMBC) (IEEE) pp 56–59 [57] Paul A, Deiss S R, Tourtelotte D, Kleffner M, Zhang T and

Cauwenberghs G 2019 Electrode-skin impedance characterization of in-ear electrophysiology accounting for cerumen and electrodermal response 2019 9th Int. IEEE/EMBS Conf. on Neural Engineering (NER) (IEEE) pp 855–8 [58] Wang Y-T, Wang Y, Cheng C-K and Jung T-P 2012

Measuring steady-state visual evoked potentials from non-hair-bearing areas 2012 Annual Int. Conf. of the IEEE Engineering in Medicine and Biology Society (IEEE) pp 1806–9 [59] Bleichner M G and Debener S 2017 Concealed, unobtrusive

ear-centered EEG acquisition: cEEGrids for transparent EEG Front. Hum. Neurosci. 11 163 [60] Guermandi M, Benatti S, Morinigo V J K and Bertini L

2018 A wearable device for minimally-invasive behind-the-ear EEG and evoked potentials 2018 IEEE Biomedical Circuits and Systems Conf. (BioCAS) (IEEE) pp 1–4 [61] Da Silva Souto C F, Pätzold W, Paul M, Debener S and

Wolf K I 2022 Pre-gelled electrode grid for self-applied EEG sleep monitoring at home Front. Neurosci. 1004 [62] da Silva Souto C F, Pätzold W, Wolf K I, Paul M,

Matthiesen I, Bleichner M G and Debener S 2021

21

<!-- page 23 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

Flex-printed ear-EEG sensors for adequate sleep staging at home Front. Digit. Health 3 688122 [63] Valentin O, Viallet G, Delnavaz A, Cretot-Richert G,

Ducharme M, Monsarat-Chanon H and Voix J 2021 Custom-fitted in-and around-the-ear sensors for unobtrusive and on-the-go EEG acquisitions: development and validation Sensors 21 2953 [64] Pham N, Dinh T, Raghebi Z, Kim T, Bui N, Nguyen P,

Truong H, Banaei-Kashani F, Halbower A, Dinh T et al 2020 Wake: a behind-the-ear wearable system for microsleep detection Proc. 18th Int. Conf. on Mobile Systems, Applications and Services pp 404–18 [65] Kaongoen N, Choi J and Jo S 2022 A novel online BCI

system using speech imagery and ear-EEG for home appliances control Comput. Methods Programs Biomed. 224 107022 [66] An W W, Shinn-Cunningham B, Gamper H,

Emmanouilidou D, Johnston D, Jalobeanu M, Cutrell E, Wilson A, Chiang K-J and Tashev I 2021 Decoding music attention from ‘eeg headphones’: a user-friendly auditory brain-computer interface ICASSP 2021—2021 IEEE Int. Conf. on Acoustics, Speech and Signal Processing (ICASSP) pp 985–9 [67] Sopic D, Aminifar A and Atienza D 2018 eG-lass: a

wearable system for real-time detection of epileptic seizures 2018 IEEE Int. Symp. on Circuits and Systems (ISCAS) (IEEE) pp 1–5 [68] Kosmyna N, Morris C, Nguyen T, Zepf S, Hernandez J and

Maes P 2019 AttentivU: designing EEG and EOG compatible glasses for physiological sensing and feedback in the car Proc. of the 11th Int. Conf. on Automotive User Interfaces and Interactive Vehicular Applications pp 355–68 [69] Kaongoen N, Choi J and Jo S 2021 Speech-imagery-based

brain–computer interface system using ear-EEG J. Neural Eng. 18 016023 [70] Ahn J W, Ku Y and Kim H C 2019 A novel wearable EEG

and ECG recording system for stress assessment Sensors 19 1991 [71] Merrill N, Curran M T, Yang J-K and Chuang J 2016

Classifying mental gestures with in-ear EEG 2016 IEEE 13th Int. Conf. on Wearable and Implantable Body Sensor Networks (BSN) (IEEE) pp 130–5 [72] Li G, Zhang Z and Wang G 2017 Emotion recognition

based on low-cost in-ear EEG 2017 IEEE Biomedical Circuits and Systems Conf. (BioCAS) (IEEE) pp 1–4 [73] Bleichner M G and Emkes R 2020 Building an ear-EEG

system by hacking a commercial neck speaker and a commercial EEG amplifier to record brain activity beyond the lab J. Open Hardw. 4 5 [74] Knierim M T, Schemmer M and Bauer N 2022 A simplified

design of a cEEGrid ear-electrode adapter for the OpenBCI biosensing platform HardwareX 12 e00357 [75] Zander T O, Brönstrup J, Lorenz R and Krol L R 2014

Towards BCI-based implicit control in human–computer interaction Advances in Physiological Computing (Springer) pp 67–90 [76] Brenner C A, Krishnan G P, Vohs J L, Ahn W-Y,

Hetrick W P, Morzorati S L and O’Donnell B F 2009 Steady state responses: electrophysiological assessment of sensory function in schizophrenia Schizop. Bull. 35 1065–77 [77] Bertelsen A R, Bladt H, Christensen C B, Kappel S L,

Toft H O, Rank M L, Mikkelsen K B and Kidmose P 2019 Generic dry-contact ear-EEG 2019 41st Annual Int. Conf. of the IEEE Engineering in Medicine and Biology Society (EMBC) (IEEE) pp 5552–5 [78] Chiu M, Murthy H and George K 2018 Mobile switch

control using auditory and haptic steady state response in ear-EEG 2018 9th IEEE Annual Ubiquitous Computing, Electronics & Mobile Communication Conf. (UEMCON) (IEEE) pp 1032–7 [79] Kappel S L and Kidmose P 2022 Characterization of

dry-contact EEG electrodes and an empirical comparison of Ag/AgCl and IrO2 electrodes 2022 44th Annual Int. Conf.

of the IEEE Engineering in Medicine & Biology Society (EMBC) (IEEE) pp 3127–30 [80] Christensen C B, Kappel S L and Kidmose P 2018 Auditory

steady-state responses across chirp repetition rates for ear-EEG and scalp EEG 2018 40th Annual Int. Conf. of the IEEE Engineering in Medicine and Biology Society (EMBC) (IEEE) pp 1376–9 [81] Christensen C B, Lunner T, Harte J M, Rank M L and

Kidmose P 2021 Chirp-evoked auditory steady-state response: the effect of repetition rate IEEE Trans. Biomed. Eng. 69 689–99 [82] Mouli S, Palaniappan R, Molefi E and McLoughlin I 2020

In-ear electrode EEG for practical SSVEP BCI Technologies 8 63 [83] Jung T, Makeig S, Westerfield M, Townsend J,

Courchesne E and Sejnowski T 1999 Independent component analysis of single-trial event-related potentials Proc. ICA vol 99 pp 173–9 [84] Meiser A and Bleichner M G 2022 Ear-EEG compares well

to cap-EEG in recording auditory ERPs: a quantification of signal loss J. Neural Eng. 19 026042 [85] Denk F, Grzybowski M, Ernst S M, Kollmeier B, Debener S

and Bleichner M G 2018 Event-related potentials measured from in and around the ear electrodes integrated in a live hearing device for monitoring sound perception Trends Hear. 22 2331216518788219 [86] Kaongoen N and Jo S 2017 A novel hybrid auditory BCI

paradigm combining ASSR and P300 J. Neurosci. Methods 279 44–51 [87] Bleichner M G, Lundbeck M, Selisky M, Minow F, Jäger M,

Emkes R, Debener S and De Vos M 2015 Exploring miniaturized EEG electrodes for brain-computer interfaces. An EEG you do not see? Physiol. Rep. 3 e12362 [88] Hölle D, Meekes J and Bleichner M G 2021 Mobile ear-EEG

to study auditory attention in everyday life: auditory attention in everyday life Behav. Res. Methods 53 2025–36 [89] Mirkovic B, Bleichner M G, De Vos M and Debener S 2016

Target speaker detection with concealed EEG around the ear Front. Neurosci. 10 349 [90] Bleichner M G, Mirkovic B and Debener S 2016 Identifying

auditory attention with ear-EEG: cEEGrid versus high-density cap-EEG comparison J. Neural Eng. 13 066004 [91] Fiedler L, Wöstmann M, Graversen C, Brandmeyer A,

Lunner T and Obleser J 2017 Single-channel in-ear-EEG detects the focus of auditory attention to concurrent tone streams and mixed speech J. Neural Eng. 14 036020 [92] Nogueira W, Dolhopiatenko H, Schierholz I, Büchner A,

Mirkovic B, Bleichner M G and Debener S 2019 Decoding selective attention in normal hearing listeners and bilateral cochlear implant users with concealed ear EEG Front. Neurosci. 13 720 [93] Kosmyna N, Balyan A and Hauptmann E 2022 Target

speaker detection with EEG/EOG glasses: a pilot study Proc. Future Technologies Conf. (FTC) 2022 vol 2 (Springer) pp 433–46 [94] Holtze B, Rosenkranz M, Jaeger M, Debener S and

Mirkovic B 2022 Ear-EEG measures of auditory attention to continuous speech Front. Neurosci. 16 539 [95] Ala T S, Alickovic E, Cabrera A F, Whitmer W M,

Hadley L V, Rank M L, Lunner T and Graversen C 2022 Alpha oscillations during effortful continuous speech: from scalp EEG to ear-EEG IEEE Trans. Biomed. Eng. 70 1264–73 [96] Kim Y-J, Kwak N-S and Lee S-W 2018 Classification of

motor imagery for ear-EEG based brain-computer interface 2018 6th Int. Conf. on Brain-Computer Interface (BCI) (IEEE) pp 1–2 [97] Kosmyna N, Balyan A and Hauptmann E 2022 Decoding

visual imagery using EEG/EOG glasses: a pilot study Proc. Future Technologies Conf. (FTC) 2022 vol 2 (Springer) pp 415–32 [98] Mikkelsen K B, Kappel S L, Hemmsen M C, Rank M L and

Kidmose P 2019 Discrimination of sleep spindles in Ear-EEG 2019 41st Annual Int. Conf. of the IEEE

22

<!-- page 24 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

Engineering in Medicine and Biology Society (EMBC) (IEEE) pp 6697–700 [99] Jørgensen S D, Zibrandtsen I C and Kjaer T W 2020

Ear-EEG-based sleep scoring in epilepsy: a comparison with scalp-EEG J. Sleep Res. 29 e12921 [100] Mikkelsen K B, Phan H, Rank M L, Hemmsen M C, De

Vos M and Kidmose P 2021 Sleep monitoring using Ear-centered setups: investigating the influence from electrode configurations IEEE Trans. Biomed. Eng. 69 1564–72 [101] Sterr A et al 2018 Sleep EEG derived from behind-the-ear

electrodes (cEEGrid) compared to standard polysomnography: a proof of concept study Front. Hum. Neurosci. 12 452 [102] Mikkelsen K B, Tabar Y R, Toft H O, Hemmsen M C,

Rank M L and Kidmose P 2022 Self-applied Ear-EEG for sleep monitoring at home 2022 44th Annual Int. Conf. of the IEEE Engineering in Medicine & Biology Society (EMBC) (IEEE) pp 3135–8 [103] Mikkelsen K B, Ebajemito J K, Bonmati-Carrion M A,

Santhi N, Revell V L, Atzori G, Della Monica C, Debener S, Dijk D-J and Sterr A et al 2019 Machine-learning-derived sleep–wake staging from around-the-ear electroencephalogram outperforms manual scoring and actigraphy J. Sleep Res. 28 e12786 [104] Kjaer T W, Rank M L, Hemmsen M C, Kidmose P and

Mikkelsen K 2022 Repeated automatic sleep scoring based on ear-EEG is a valuable alternative to manually scored polysomnography PLOS Digit. Health 1 e0000134 [105] Paul A, Fowler P, Xu Y, Lee M, Wang J and

Cauwenberghs G 2022 Neural recording analog front-end noise reduction with digital correlated double sampling 2022 IEEE Biomedical Circuits and Systems Conf. (BioCAS) (IEEE) pp 149–52 [106] Choi S-I and Hwang H-J 2019 Effects of different

re-referencing methods on spontaneously generated ear-EEG Front. Neurosci. 13 822 [107] Ha U, Kim C, Lee Y, Kim H, Roh T and Yoo H-J 2015 A

multimodal stress monitoring system with canonical correlation analysis 2015 37th Annual Int. Conf. of the IEEE Engineering in Medicine and Biology Society (EMBC) (IEEE) pp 1263–6 [108] Wascher E, Arnau S, Reiser J E, Rudinger G, Karthaus M,

Rinkenauer G, Dreger F and Getzmann S 2019 Evaluating mental load during realistic driving simulations by means of round the ear electrodes Front. Neurosci. 13 940 [109] Hwang T, Kim M, Hong S and Park K S 2016 Driver

drowsiness detection using the in-ear EEG 2016 38th Annual Int. Conf. of the IEEE Engineering in Medicine and Biology Society (EMBC) (IEEE) pp 4646–9 [110] Hong S, Kwon H, Choi S H and Park K S 2018 Intelligent

system for drowsiness recognition based on ear canal electroencephalography with photoplethysmography and electrocardiography Inf. Sci. 453 302–22 [111] Zibrandtsen I, Kidmose P and Kjaer T 2018 Detection of

generalized tonic-clonic seizures from ear-EEG based on EMG analysis Seizure 59 54–59 [112] You S, Cho B H, Yook S, Kim J Y, Shon Y-M, Seo D-W and

Kim I Y 2020 Unsupervised automatic seizure detection for focal-onset seizures recorded with behind-the-ear EEG using an anomaly-detecting generative adversarial network Comput. Methods Programs Biomed. 193 105472 [113] You S, Cho B H, Shon Y-M, Seo D-W and Kim I Y 2022

Semi-supervised automatic seizure detection using personalized anomaly detecting variational autoencoder with behind-the-ear EEG Comput. Methods Programs Biomed. 213 106542 [114] Vandecasteele K, De Cooman T, Dan J, Cleeren E, Van

Huffel S, Hunyadi B and Van Paesschen W 2020 Visual seizure annotation and automated seizure detection using behind-the-ear electroencephalographic channels Epilepsia 61 766–75

[115] Vandecasteele K et al 2021 The power of ECG in

multimodal patient-specific seizure monitoring: added value to an EEG-based detector using limited channels Epilepsia 62 2333–43 [116] Zambrana-Vinaroz D, Vicente-Samper J M and

Sabater-Navarro J M 2022 Validation of continuous monitoring system for epileptic users in outpatient settings Sensors 22 2900 [117] Nielsen J M, Zibrandtsen I C, Masulli P, Sørensen T L,

Andersen T S and Kjær T W 2022 Towards a wearable multi-modal seizure detection system in epilepsy: a pilot study Clin. Neurophysiol. 136 40–48 [118] Kappel S L, Christensen C B, Mikkelsen K B and Kidmose P

2016 Reference configurations for ear-EEG steady-state responses 2016 38th Annual Int. Conf. of the IEEE Engineering in Medicine and Biology Society (EMBC) (IEEE) pp 5689–92 [119] Gu Y, Cleeren E, Dan J, Claes K, Van Paesschen W, Van

Huffel S and Hunyadi B 2017 Comparison between scalp EEG and behind-the-ear EEG for development of a wearable seizure detection system for patients with focal epilepsy Sensors 18 29 [120] Xu J, Mitra S, Van Hoof C, Yazicioglu R F and

Makinwa K A 2017 Active electrodes for wearable EEG acquisition: review and electronics design methodology IEEE Rev. Biomed. Eng. 10 187–98 [121] Kappel S L, Looney D, Mandic D P and Kidmose P 2017

Physiological artifacts in scalp EEG and ear-EEG Biomed. Eng. Online 16 1–16 [122] Bleichner M G and Debener S 2019 Independent

component decomposition of around ear EEG data to detect artifacts 2019 IEEE Int. Conf. on Systems, Man and Cybernetics (SMC) (IEEE) pp 3631–4 [123] Lee Y-E, Kwak N-S and Lee S-W 2020 A real-time

movement artifact removal method for ambulatory brain-computer interfaces IEEE Trans. Neural Syst. Rehabil. Eng. 28 2660–70 [124] Chang C-Y, Hsu S-H, Pion-Tonachini L and Jung T-P 2018

Evaluation of artifact subspace reconstruction for automatic EEG artifact removal 2018 40th Annual Int. Conf. of the IEEE Engineering in Medicine and Biology Society (EMBC) (IEEE) pp 1242–5 [125] Blum S, Jacobsen N S, Bleichner M G and Debener S 2019

A riemannian modification of artifact subspace reconstruction for EEG artifact handling Front. Hum. Neurosci. 13 141 [126] Nordin A D, Hairston W D and Ferris D P 2018

Dual-electrode motion artifact cancellation for mobile electroencephalography J. Neural Eng. 15 056024 [127] Kappel S L, Makeig S and Kidmose P 2019 Ear-EEG

forward models: improved head-models for ear-EEG Front. Neurosci. 13 943 [128] Lee J, Lee K-R, Ha U, Kim J-H, Lee K, Gweon S, Jang J and

Yoo H-J 2019 A 0.8-v 82.9-µw in-ear BCI controller IC with 8.8 PEF EEG instrumentation amplifier and wireless ban transceiver IEEE J. Solid-State Circuits 54 1185–95 [129] Kwak N-S and Lee S-W 2019 Error correction regression

framework for enhancing the decoding accuracies of ear-EEG brain–computer interfaces IEEE Trans. Cyber. 50 3654–67 [130] Israsena P and Pan-Ngum S 2022 A cnn-based deep

learning approach for ssvep detection targeting binaural ear-EEG Front. Comput. Neurosci. 16 868642 [131] Liang L, Bin G, Chen X, Wang Y, Gao S and Gao X 2021

Optimizing a left and right visual field biphasic stimulation paradigm for SSVEP-based BCIS with hairless region behind the ear J. Neural Eng. 18 066040 [132] Lee Y-E and Lee M 2020 Decoding visual responses based

on deep neural networks with ear-EEG signals 2020 8th Int. Winter Conf. on Brain-Computer Interface (BCI) (IEEE) pp 1–6

23

<!-- page 25 -->

J. Neural Eng. 20 (2023) 051002 N Kaongoen et al

[133] Zhu Y, Li Y, Lu J and Li P 2021 EEGNet with ensemble

learning to improve the cross-session classification of SSVEP based BCI from ear-EEG IEEE Access 9 15295–303 [134] Lawhern V J, Solon A J, Waytowich N R, Gordon S M,

Hung C P and Lance B J 2018 EEGNet: a compact convolutional neural network for EEG-based brain–computer interfaces J. Neural Eng. 15 056013 [135] Lee Y-E and Lee S-W 2021 Decoding event-related

potential from ear-EEG signals based on ensemble convolutional neural networks in ambulatory environment

2021 9th Int. Winter Conf. on Brain-Computer Interface (BCI) (IEEE) pp 1–5 [136] Borup K, Kidmose P, Phan H and Mikkelsen K 2023

Automatic sleep scoring using patient-specific ensemble models and knowledge distillation for ear-EEG data Biomed. Signal Process. Control 81 104496 [137] Phan H, Andreotti F, Cooray N, Chén O Y and De Vos M

2019 SeqSleepNet: end-to-end hierarchical recurrent neural network for sequence-to-sequence automatic sleep staging IEEE Trans. Neural Syst. Rehabil. Eng. 27 400–10

24