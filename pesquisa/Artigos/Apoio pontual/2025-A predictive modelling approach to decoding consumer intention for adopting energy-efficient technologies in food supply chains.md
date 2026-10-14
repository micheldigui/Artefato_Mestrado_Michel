---
source_file: "2025-A predictive modelling approach to decoding consumer intention for adopting energy-efficient technologies in food supply chains.txt"
original_rel_path: "Trabalhos\Artigos\Apoio pontual\txt\2025-A predictive modelling approach to decoding consumer intention for adopting energy-efficient technologies in food supply chains.txt"
category: "Artigos_Apoio_pontual"
extension: ".txt"
sha256: "e0c0e90219ca9f77a57adba7aade6b5918d6d55e85aaf822ba7d36ca426607db"
extracted_at: "2026-09-20T00:05:05.675954"
---

﻿Decision Analytics Journal 15 (2025) 100561

A
a
B
B

A
K
P
M
E
F
C
S

1

a
e
p
n
a
m
e
c
e
i
n
e
c
t
o
w

a

h
R
A
2
(

Contents lists available at ScienceDirect

Decision Analytics Journal

 journal homepage: www.elsevier.com/locate/dajour  

 predictive modelling approach to decoding consumer intention for 
dopting energy-efficient technologies in food supply chains
rintha Rajendran, Manivannan Babu ∗, Veeramani Anandhabalaji
harathidasan School of Management, Bharathidasan University, Tamilnadu, India

 R T I C L E  I N F O  A B S T R A C T
eywords: The transition towards energy-efficient practices in the food supply chain (FSC) is essential for addressing 
redictive analytics the dual imperatives of sustainability and cost-effectiveness. As consumers become increasingly aware of the 
achine learning environmental impact of their food choices, their willingness to support energy-efficient technologies (EET) has 
nergy efficiency become a critical factor in shaping the future of sustainable FSC. This study empirically investigates consumer 
ood supply chain
onsumer intention intention and desire to pay for food products characterized by a reduced energy footprint, utilizing machine 
ustainability learning (ML) algorithms to predict consumer preferences within the FSC. Association rule mining (ARM) was 

employed to uncover key patterns in consumer intentions, while multiple ML algorithms were compared to 
identify the most effective algorithm for predicting willingness to pay. The results reveal that the Random 
Forest algorithm achieved the highest accuracy at 82%, significantly outperforming other models. These 
findings underscore the potential of ML to refine marketing strategies and operational decisions, facilitating 
the broader adoption of EET within the FSC (EET-FSC). The study offers valuable implications for industry 
professionals seeking to enhance sustainability efforts through data-driven decision-making. The research 
contributes to optimizing FSC through improved decision-making, resource allocation, and sustainability 
initiatives. Future research directions include expanding the dataset scope, exploring advanced ML techniques, 
and examining the economic impacts of EET-FSC.
. Introduction impact overall energy consumption. The FSC encompasses a broad 
range of processes, from growing crops to processing, distributing, 

In recent years, global supply chains, particularly in manufacturing storing, selling, and ultimately consuming food. As consumers become 
nd logistics, have increasingly prioritized energy-efficiency. Energy- more aware of the environmental and ethical implications of their 
fficient technologies (EET) are designed to reduce energy usage and food choices, there is an increasing demand for transparency and 
romote sustainability, making them essential for addressing the sig- sustainable practices within the FSC [4]. In response, the food industry 
ificant energy demands associated with food production, processing, is focusing on energy-efficiency as a core component of its sustainabil-
nd distribution. This shift is driven by the dual objectives of mini- ity strategies [5]. This includes improving energy use in production, 
izing costs and enhancing sustainability. These goals aim to balance transportation, and storage, with the adoption of EET, such as advanced 
conomic needs with environmental responsibilities, presenting both cooling technologies, energy-efficient lighting, and renewable energy 
hallenges and opportunities for achieving sustainability [1]. Adopting 
co-friendly energy options, such as solar sources—being crucial for reducing operational costs, lowering carbon 

collectors and windmills, 
s crucial for reducing greenhouse gas footprints, and preserving food quality [6]. Disruptive technologies like 

emissions and meeting inter-
ational climate commitments [2]. The move towards a sustainable blockchain, IoT, and AI further enhance energy-efficiency by improving 
conomy further supports these efforts by encouraging sustainable operational performance, increasing transparency, and reducing waste 
onsumption and innovation. The consumer acceptance of EET by, par- [7]. However, consumer intention to adopt these technologies is vital, 
icularly blockchain technology, is influenced by a complex interplay as their acceptance is crucial for widespread implementation necessary 
f economic, regulatory, technological, and sociocultural factors, all of to build sustainable food systems.
hich are integral to sustainability [3]. The integration of EET in the FSC (EET-FSC) refer to the application 
In the context of the food supply chain (FSC), key energy-intensive of energy-saving techniques within the FSC, aiming to reduce energy 

ctivities such as transportation, storage, and processing significantly consumption, decrease carbon emissions, and support sustainability. 

∗ Corresponding author.
E-mail addresses: brintharaj@gmail.com (B. Rajendran), drbabu@bdu.ac.in (M. Babu), anandhabalajiv@gmail.com (V. Anandhabalaji).
ttps://doi.org/10.1016/j.dajour.2025.100561
eceived 27 August 2024; Received in revised form 8 January 2025; Accepted 13 M
vailable online 15 March 2025
772-6622/© 2025 The Authors. Published by Elsevier Inc. This is an open access 
http://creativecommons.org/licenses/by/4.0/).
arch 2025
article under the CC BY license 



B. Rajendran, M. Babu and V. Anandhabalaji Decision Analytics Journal 15 (2025) 100561

 

This research focuses on blockchain technology as a key tool for 
enhancing energy-efficiency. Blockchain significantly improves trans-
parency, traceability, and accountability in energy use across the supply 
chain, enabling real-time monitoring and verification of energy con-
sumption data [8]. It allows the tracking of energy inputs and outputs 
at various stages, ensuring compliance with energy-efficient standards. 
The decentralized and immutable nature of blockchain’s ledger ensures 
accurate recording of energy transactions, promoting energy conserva-
tion and advancing sustainability goals within the FSC. Organizations 
are investing in technological advancements that enhance resource effi-
ciency, which are crucial for reducing waste and optimizing resources. 
These innovations not only help meet sustainability benchmarks but 
also improve operational efficiency, leading to ongoing cost benefits. 
Recently, businesses have been placing greater emphasis on sustainable 
sourcing and production practices, including organic farming, minimiz-
ing chemical inputs, and adhering to fair trade standards, all of which 
align with consumer preferences for ethically produced goods [9].

On focusing the blockchain technology, it significantly enhances 
supply chain visibility and traceability, which builds consumer trust 
and promotes the shift towards energy-efficient practices [10]. The 
technology’s decentralized and immutable ledger ensures data integrity,
reduces the risk of fraud, and supports compliance with regulatory 
requirements, thereby reassuring consumers about sustainability efforts 
[11]. To fully realize its potential, it is essential to address underlying 
challenges such as technological complexity, integration issues, and 
the need for standardization through strategic planning and collab-
oration among stakeholders [12]. Additionally, leveraging machine 
learning (ML) algorithms to predict consumer intention can contribute 
to the adoption of EET-FSC. ML enables accurate analysis of energy 
consumption trends and consumer intention, allowing organizations 
to implement data-driven strategies that meet the growing demand 
for sustainability. Existing literature has explored consumer intention 
regarding the adoption of EET-FSC, identifying several influencing 
factors. de Oliveira et al. [13] highlighted the opportunity to harness 
consumer awareness of sustainability and their openness to supply 
chain 4.0 technologies to encourage sustainable choices. Baldi et al. 
(2021) emphasized the importance of perceived benefits, trust, and 
environmental attitudes in shaping consumer preferences, while also 
recognizing cost as a significant barrier. Additionally, Nunes and De-
liberador [14] stressed the need to consider regional and cultural 
influences on consumer intention.

Despite these insights, a significant gap remains in the literature 
regarding the use of ML algorithms to analyse and predict consumer 
intention towards EET-FSC. While previous studies have examined 
consumer preferences and attitudes towards sustainable FSC, a com-
prehensive understanding of consumer intentions regarding energy-
efficient practices is still lacking. This study aims to fill this research 
gap by empirically investigating consumer intention and willingness 
to pay for food products with a reduced energy consumption in their 
supply chain. The application of ML algorithms to predict consumer 
intention in adopting EET-FSC represents a significant methodological 
advancement. Although traditional research methods, such as linear 
models and regression analysis, have yielded valuable insights, they are 
limited in their ability to capture the complex and nonlinear relation-
ships that influence consumer intentions. In contrast, ML algorithms 
excel at identifying intricate patterns within large and diverse datasets 
[15], offering a more comprehensive understanding of consumer in-
tention. This investigation utilizes sophisticated predictive modelling 
methodologies through primary data acquired from consumers to scru-
tinize their willingness to adopt EET-FSC. Through the application of 
ML algorithms, this investigation delivers an in-depth understanding 
of consumer intention and supports the creation of data-supported 
strategies to encourage the adoption of energy-efficient practices in the 
FSC. This study addresses significant gaps in understanding consumer 
intentions towards EET-FSC, by leveraging advanced ML methodolo-
gies. Unlike prior studies focusing primarily on descriptive insights, 
2

this approach identifies nuanced patterns among key demographics. 
By uncovering the socio-economic factors like financial stability con-
cerns, risk aversion, and limited targeted marketing, this study offers 
targeted strategies to bridge these gaps. Such insights align with global 
challenges in consumer technology adoption, demonstrating broader 
applicability across varied socio-economic settings.

The subsequent sections of this study are structured as follows. 
Section 2 elaborates on the pertinent literature and background, Sec-
tion 3 delineates the methodologies for collected dataset, ML algo-
rithms used, evaluation metrics, and data preprocessing techniques, 
while Section 4 analyses the resultant findings, Section 5 discusses 
the principal conclusions and finally Section 6 presents prospective 
research avenues.

2. Related literature

2.1. Supply chain and energy efficiency in food sector

Supply chain management involves orchestrating the complex in-
teractions between various components and processes to efficiently 
move goods and services from producers to consumers [16]. The pri-
mary objective is to align production with consumer demand, thereby 
fostering economic growth and enhancing global competitiveness. Es-
sential activities like planning, sourcing, production, and distribution 
ensure the supply chain’s effectiveness. Within this framework, the 
FSC emerges as a critical domain, requiring advanced practices to 
address the intricate challenges of delivering perishable goods.  Build-
ing on supply chain principles, the focus has shifted to the FSC, a 
complex network encompassing production, processing, distribution, 
and retail, all aimed at delivering food products to consumers. The 
global FSC is tasked with balancing supply and demand while en-
suring safe and timely food delivery. Additionally, the FSC plays a 
critical role in addressing sustainability challenges, particularly through 
adopting energy-efficient practices, as exemplified by the Green FSC 
recognized in regions like India [17]. EETs are vital for enhancing 
transparency and operational efficiency in the FSC. For instance, phase 
change materials contribute significantly to energy-efficiency within 
the FSC [18]. Moreover, integrating blockchain, the Internet of Things 
(IoT), and digital financial solutions in agriculture further enhances 
transparency by enabling real-time monitoring and secure transactions, 
fostering trust among participants and addressing concerns such as 
fraud and food safety through immutable digital records [19]. These 
efforts not only align with sustainability goals but also cater to evolving 
consumer demands for ethical and eco-friendly practices, even as price 
sensitivity remains a critical factor influencing consumer decisions. 
Harjadi and Gunardi [20] and Nguyen-Viet et al. [21] highlight that 
consumer interest in premium sustainable products is often driven by 
non-economic motivations, such as environmental consciousness and 
perceived social value.

However, while blockchain offers scalability and transparency, its 
adoption in the FSC is still in its early stages, facing technical, regu-
latory, and operational challenges. Despite these hurdles, the combi-
nation of energy-efficient methods with digital technologies is trans-
forming the FSC into a more transparent, efficient, and sustainable 
ecosystem.

2.2. Technological advancements in EEFSC

Blockchain technology has emerged as a crucial tool for improving 
transparency and efficiency in the FSC. By providing a decentral-
ized, immutable, and secure platform, blockchain addresses persistent 
issues such as inefficiencies, ambiguity, and information asymmetry 
[22]. Blockchain eliminates centralized databases and intermediaries, 
reducing inefficiencies and promoting greater transparency and col-
laboration [23]. These attributes are especially critical in FSC, where 



B. Rajendran, M. Babu and V. Anandhabalaji Decision Analytics Journal 15 (2025) 100561

 

timing and traceability are pivotal. Blockchain ensures the reliabil-
ity of traceability information, which is essential in complex, global 
markets [24]. The energy-efficiency of blockchain is also emphasized 
in the current literature. Integrating blockchain with Green Product 
Platforming significantly reduces carbon emissions while optimizing 
economic performance in the agri-food sector by enabling the efficient 
production and digital distribution of green products, addressing stake-
holder demands for improved carbon and economic outcomes [25]. 
The combination of blockchain technology with IoT systems, as seen 
in a framework for the strawberry supply chain, improves shipment 
efficiency by tracking interactions and documenting transactions, thus 
promoting energy-efficient practices [26].

Transportation, production, and storage are the key energy-intensive
aspects of the FSC. Long-distance food transportation, for instance, 
consumes significant energy and emits considerable greenhouse gases. 
These insights underscore the urgency for adopting EET in logistics 
to address escalating environmental concerns. Similar findings for 
other products like denim apparel [27] and yogurt [28]  highlight the 
energy-intensive nature of transportation, with consumer travel by car 
potentially matching freight transportation’s energy consumption.

While production and storage also contribute heavily to energy con-
sumption, transportation offers considerable opportunities for energy 
savings. Although local food systems typically reduce transportation 
energy, they do not always result in lower overall energy consumption 
compared to conventional systems [29]. Innovations in storage, such 
as integrated cooling and heating systems with energy storage, can en-
hance energy efficiency by recovering waste heat and reducing energy 
costs [30,31]. Technological advancements, particularly in emerging 
markets like India, have the potential to reduce post-harvest losses and 
improve the overall efficiency of the FSC [32].

2.3. Consumer intention towards EET

Consumer intention refers to the conscious decision to engage in 
specific behaviours, such as adopting EET-FSC. This intention often 
aligns with consumers’ willingness to pay a premium for products 
derived from sustainable practices. Lindström et al. [33] noted the 
increasing consumer inclination towards technologies that promote sus-
tainability, offering businesses significant opportunities to align their 
offerings with these values. While consumers may not directly interact 
with technologies, their demand for sustainable products drives orga-
nizations to adopt these innovations. This highlights the indirect yet 
powerful role of consumer preferences in shaping supply chain deci-
sions. Consumer acceptance of energy-efficient practices is primarily 
influenced by the perceived benefits of these technologies, such as 
enhanced transparency and waste reduction facilitated by blockchain 
systems [34]. However, this willingness is often nuanced. Studies like 
Diallo et al. [35] suggest that consumers are willing to pay a premium 
when they perceive long-term cost savings, improved product quality, 
or alignment with personal values such as environmental steward-
ship. Additionally, the concept of ‘green loyalty’ [36] indicates that 
sustainability-focused consumers may prioritize eco-friendly attributes 
over cost considerations in their purchasing decisions, particularly 
when these attributes contribute to broader societal goals.

Challenges like security concerns, costs, and accessibility continue 
to impede widespread adoption despite a general willingness to use 
blockchain for monitoring energy use in the FSC [37]. Environmental 
concerns also significantly influence consumer intention, with a noted 
willingness to invest more in EEFSC products, reflecting the connection 
between sustainability values and support for energy-efficient practices 
[38].
3

2.4. ML algorithms for predicting consumer intention

Traditional research methodologies in supply chain management of-
ten fall short when addressing the complex dynamics of modern supply 
chains. These methodologies typically focus on specific demographics, 
employ inadequate data analysis techniques, and struggle to capture 
intricate interrelationships or integrate sustainability considerations 
[39]. ML offers a more sophisticated and flexible approach to analysing 
consumer intention by managing large datasets and revealing complex, 
non-linear relationships. Various ML techniques, including decision 
trees, random forests, support vector machines, and clustering methods, 
are well-suited for analysing vast amounts of data and uncovering 
insights that traditional methods might miss [40,41]. ML algorithms are 
capable to be leveraged in diverse fields [42,43]. These methods excel 
in predicting consumer intention due to their ability to analyse complex 
data sets [44]. By integrating factors such as demographic information, 
purchasing behaviour, and environmental influences, ML algorithms 
can create more accurate and detailed profiles of consumer inten-
tion, helping organizations better tailor their strategies for promoting 
energy-efficient innovations.

ML algorithms, such as Random Forest and K-means clustering, have 
been employed to study consumer intention in the food retail sector, 
providing valuable insights into consumer preferences and emerging 
trends. ML’s application in analysing consumer intention within the 
FSC has profound implications for sustainability, particularly in reduc-
ing energy consumption and lowering carbon emissions. For example, 
Artificial Neural Networks (ANNs) have been used to optimize energy 
efficiency in transportation by analysing fuel consumption data and 
transportation routes [45]. This integration not only enhances energy-
efficiency but also addresses consumer demands for sustainability, 
fostering a more transparent and responsible supply chain.

ML algorithms are transforming consumer intention research by 
providing sophisticated tools for analysing complex data. This enables 
a deeper understanding of consumer preferences and behaviour, al-
lowing organizations to effectively promote and implement EET-FSC. 
Analysing the FSC using ML enhances sustainability and efficiency, 
contributing to a more transparent, responsible, and environmentally 
friendly supply chain. This approach helps the FSC meet consumer 
demands for sustainability while optimizing operations and reducing 
waste, ultimately contributing to a more sustainable and efficient global 
food system.

2.5. Unpacking the research gap

This study explores the EET-FSC focusing on their potential to 
enhance energy efficiency. Emerging technologies like blockchain, IoT, 
and phase change materials have demonstrated significant promise in 
increasing transparency, reducing energy consumption, and improv-
ing operational efficiency in the FSC. Consumer willingness to adopt 
these technologies is largely driven by perceived benefits such as 
increased transparency and positive environmental impact. However, 
challenges such as financial costs, security concerns, and accessibility 
continue to hinder widespread adoption. Traditional research methods 
have struggled to effectively capture the complex dynamics of con-
sumer intention and energy efficiency within the FSC. In contrast, ML 
algorithms have proven effective in predicting consumer intention, pro-
viding critical insights that can address these challenges and encourage 
broader adoption of EET in the FSC. Despite progress in both EET and 
ML, significant research gaps remain. Current literature lacks a thor-
ough analysis of how emerging technologies, particularly blockchain, 
can be fully leveraged to address the complexities of the FSC and 
predict consumer intention towards EET-FSC. Through the utilization 
of empirical consumer data, this investigation effectively reconciles 
the disparity between theoretical capabilities and pragmatic execution 
while simultaneously yielding practical insights for the augmentation 
of sustainability within the FSC. The deployment of ML algorithms 



B. Rajendran, M. Babu and V. Anandhabalaji Decision Analytics Journal 15 (2025) 100561

Table 1
Research questions and approaches.
 Research questions Approaches  
 What elements contribute to consumers’ inclination to engage with Association rule mining (ARM)  
EET-FSC?

 What is the impact of geographic location, income level, and Analysis of Outlier Association Rules with Scatter  
knowledge of FSC on consumer intention to embrace EET-FSC? plot

 Which ML algorithms optimally predict the consumer willingness to Confusion matrices, calibration plot, Receiver  
pay a premium for EEFSC products? Operating Characteristic (ROC) analysis and 

statistical justification.
on this dataset signifies a noteworthy methodological progression, 
facilitating a more profound comprehension of consumer engagement 
with and perceptions of EET-FSC. Additionally, there is a need for 
deeper understanding of the long-term impacts of these technologies 
on energy-efficiency and how they can be optimized to meet evolv-
ing consumer expectations. This study emphasizes the importance of 
ML predictive modelling in improving the understanding of consumer 
intention in the context of EET-FSC. The study seeks to answer the 
following research questions (see Table 1): 

Addressing these questions underscores the crucial role of ML not 
only in understanding consumer intention but also in bridging the 
gap between technological potential and practical implementation in 
the FSC. The findings suggest that integrating ML and EET into FSC 
operations can significantly boost sustainability by reducing energy 
use and improving operational efficiency. These technologies enable 
better data-driven decision-making, contributing to more resilient and 
sustainable supply chain.

3. Methodology

This research employs a comprehensive methodology to examine 
the incorporation of energy efficiency within supply chain, specifically 
emphasizing the FSC. The methodology is structured to analyse the po-
tential utilization of EETs and the examination of consumer intention. 
As show in Fig. 1, the research utilizes predictive ML algorithms for 
consumer willingness to pay for EEFSC products, as well as employing 
ARM to reveal trends in consumer intention. Through the scrutiny of 
extensive datasets, the study aspires to pinpoint critical factors that 
affect consumer intentions, ultimately directing stakeholders in the FSC 
towards energy-efficiency.

3.1. Data collection

The primary data was acquired through a structured online survey 
questionnaire and surveyed the consumers of grocery products from 
various regions in India. In order to guarantee a sample that is both 
diverse and representative, the survey was disseminated through vari-
ous channels, encompassing social media platforms, electronic mailing 
lists, and consumer forums specifically focused on sustainability and 
food products. This approach ensured that the sample was not lim-
ited to specific geographic or demographic subsets but represented 
a broad cross-section of consumers with varying levels of interest in 
sustainability and EETs. The questionnaire assessed variables includ-
ing income levels, perceptions of FSC transparency, and interest in 
blockchain technology as a means to enhance energy-efficiency. A total 
of 433 individuals participated in the survey. This research is focused 
on exploring a mixed adult demographic in India, which includes 
a significant age range (from 18 years to beyond 65 years), and is 
distributed across several geographic regions of the nation, such as 
the North, East, South, West, Central, and Northeast sectors. Respon-
dents were asked to self-report on their grocery shopping behaviour, 
including frequency (daily, weekly, monthly), preferred sources (lo-
cal Kirana shops, supermarket chains, online platforms, or farmers’ 
markets), and dietary preferences (vegetarian, non-vegetarian, vegan). 
Income brackets were categorized into predefined ranges (<|50,000, 
4

|50,000–|1,00,000, |1,00,000–|2,00,000, >|2,00,000) to assess their 
impact on consumer intention towards EET-FSC adoption. Additionally, 
the target demographic represents differing levels of interest and con-
cern regarding the EET-FSC, its environmental ramifications, and the 
propensity to invest in EEFSC products.

To ensure that the data collection process was robust and reliable, 
a number of measures were implemented. Pre-testing of the question-
naire was conducted with a pilot group of 20 respondents to ensure 
clarity and eliminate ambiguity in the questions. The abstract features 
like blockchain were explained in practical terms, using relatable ex-
amples such as tracking food origins and energy use. The survey was 
designed to protect the anonymity of participants, thereby minimizing 
the risk of response bias, particularly for questions related to income 
levels or environmental concerns. The survey questionnaire included 22 
questions, explicitly aligned with the features/variables detailed in Ta-
ble 2. Each question was designed to gather actionable insights regard-
ing consumer demographics, grocery shopping behaviours, attitudes 
towards blockchain technology, and willingness to adopt EEFSC.

3.2. Data preprocessing

The unrefined data underwent comprehensive preprocessing to con-
firm its appropriateness for analysis. This process included addressing 
missing data, encoding categorical variables, and normalizing numeri-
cal features as necessary. A strong focus was given to the arrangement 
of classes throughout the dataset in order to reduce any prospective 
difficulties linked to class imbalance.

3.3. Data sampling for prediction

In the development of predictive models utilizing Orange software, 
a crucial step is the selection of a representative dataset sample for 
effective training and validation. A fixed proportion sampling method 
was adopted, where 70% of the dataset was randomly allocated for 
training, thereby ensuring a robust model foundation while reserving 
30% for subsequent testing and validation. This methodology incor-
porates deterministic sampling for reproducibility, stratification for 
maintaining variable distribution, and sampling without replacement to 
guarantee unique observations, thus enhancing model generalizability.

3.4. ARM

ARM constitutes a data mining methodology employed to discern 
correlations among variables within extensive datasets. It reveals con-
cealed patterns by detecting recurrent item sets and formulating rules 
that elucidate how the presence of one item in the dataset is cor-
related with the presence of another. It was employed to discern 
prevalent patterns in consumer intention, particularly those associated 
with EET-FSC. The principal indices employed in ARM encompass 
support, confidence, and lift, among others, each fulfilling a distinct 
function in the assessment of the rules [46]. The key metrics of ARM 
are as follows,



B. Rajendran, M. Babu and V. Anandhabalaji Decision Analytics Journal 15 (2025) 100561
Fig. 1. Methodology of the study.
Table 2
Features/variables of the study.
 S.No. Variable description Feature (F)/ Target (T) 
 1 How familiar are you with blockchain technology and its applications in supply F  

chain management?
 2 Imagine a secure digital record that tracks information throughout a process, like a F  

chain of connected blocks. In which industries might this be important?
 3 How interested would you be in learning more about how blockchain technology F  

can improve the energy efficiency of the FSC?
 4 How beneficial do you think a blockchain-based system could be for the following F  

aspects of the FSC?
 5 Do you have any concerns about using blockchain technology in the FSC? F  
 6 Considering both the potential benefits and concerns, how comfortable would you be F  

with using a blockchain-based system to track the energy used in your food?
 7 Age F  
 8 Location F  
 9 How often do you shop for groceries? F  
 10 Where do you typically buy your groceries? F  
 11 Dietary preferences F  
 12 Household size F  
 13 Income level F  
 14 How often do you consider the energy efficiency of the supply chain when you shop F  

for groceries?
 15 Imagine knowing how much energy was used to produce the food you buy (through F  

a label or app). Would you pay a premium for options that used less energy?
 16 How interested would you be in receiving information about the energy use F  

associated with the food you buy?
 17 How concerned are you about the environmental impact of the FSC? F  
 18 How important is it to you to know where your food comes from and how it is F  

produced?
 19 On a scale of 1 to 5, how clear do you think the current food system is about where F  

food comes from and how it is produced?
 20 How likely are you to choose food tracking options with lower energy use? F  
 21 How important is it to you to support farms and businesses that use less energy? F  
 22 Would you pay a small extra amount for food with a demonstrably lower T  

environmental impact, if the information was clear?
5



B. Rajendran, M. Babu and V. Anandhabalaji Decision Analytics Journal 15 (2025) 100561
3.4.1. Support
Support is a metric that quantifies the frequency of occurrence of a 

specific item or combination of items within a dataset. A high support 
value signifies the relevance and reliability of the itemset, indicating 
its widespread presence within the data. 

𝑁𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑡𝑟𝑎𝑛𝑠𝑎𝑐𝑡𝑖𝑜𝑛𝑠 𝑐𝑜𝑛𝑡𝑎𝑖𝑛𝑖𝑛𝑔 𝑋
𝑆𝑢𝑝𝑝𝑜𝑟𝑡(𝑋) = (1)

𝑇 𝑜𝑡𝑎𝑙𝑛𝑢𝑚𝑏𝑒𝑟𝑜𝑓𝑡𝑟𝑎𝑛𝑠𝑎𝑐𝑡𝑖𝑜𝑛𝑠

3.4.2. Confidence
Confidence is a metric that measures the likelihood of the conse-

quent occurring given the presence of the antecedent in a transaction 
[47]. A high confidence value suggests a strong association between 
the antecedent and consequent. However, it is essential to consider the 
overall frequency of the consequent in the dataset, as a high confidence 
value might be misleading if the consequent is common. 

𝑆𝑢𝑝𝑝𝑜𝑟𝑡(𝑋 ∪ 𝑌 )
𝐶𝑜𝑛𝑓𝑖𝑑𝑒𝑛𝑐𝑒(𝑋 ⇒ 𝑌 ) = (2)

𝑆𝑢𝑝𝑝𝑜𝑟𝑡(𝑋)

3.4.3. Lift
Lift is a metric that quantifies the degree to which the occurrence 

of the antecedent (X) increases the likelihood of the consequent (Y) 
compared to the expected likelihood if X and Y were independent 
[48]. Lift values greater than 1 suggest a positive association between 
X and Y, indicating that the occurrence of X significantly contributes to 
the occurrence of Y. This metric is valuable for identifying non-trivial 
associations within the data. 

𝐶𝑜𝑛𝑓𝑖𝑑𝑒𝑛𝑐𝑒(𝑋 ⇒ 𝑌 )
𝐿𝑖𝑓𝑡(𝑋 ⇒ 𝑌 ) = (3)

𝑆𝑢𝑝𝑝𝑜𝑟𝑡(𝑌 )

3.5. Model selection and implementation
The principal aim of any classification task is to precisely allocate 

class labels to each instance contained within the test dataset. In 
the framework of this investigation, classification methodologies are 
utilized to construct models that are adept at forecasting the propensity 
to embrace EET-FSC. These models are developed utilizing predictive 
ML techniques, including Decision Trees, Random Forest, Naive Bayes, 
Logistic Regression, k-Nearest Neighbour (k-NN), AdaBoost, and Neural 
Network. Incorporating multiple algorithms is critical for determining 
the optimal predictive approach. For instance, Random Forest excels 
in managing feature importance and non-linear relationships, while 
Logistic Regression offers simplicity and interpretability. Comparing 
multiple methods of this nature, ensures the selection of the most 
suitable algorithm for practical implementation and offers a bench-
mark for future studies in the domain of EET-FSC. By comparing their 
performance, we not only identify the best-performing model but also 
provide actionable insights for stakeholders, guiding the selection of 
algorithms for similar datasets and applications. This comprehensive 
approach is supported by established literature that emphasizes the 
value of comparing multiple methods for predictive tasks [49,50].
3.5.1. Decision trees

The straightforwardness and lucidity of decision trees [51], render 
them especially advantageous for comprehending the elements affect-
ing the consumer intention on adopting EET-FSC. The decision tree 
algorithm is predicated on the recursive partitioning of a dataset into 
subsets predicated on a characteristic that yields the most substan-
tial information gain (or, equivalently, the minimal Gini impurity or 
entropy). The partitioning criteria can be articulated as, 

𝑐
∑

( )

𝐸𝑛𝑡𝑟𝑜𝑝𝑦(𝑆) = − 𝑝𝑖 log 2 𝑝𝑖 (4)
  𝑖=1

𝑝𝑖 is the proportion of samples that belong to class i, and c is the 
number of classes. 

∑ ∣ 𝑆𝑣 ∣
𝐼𝑛𝑓𝑜𝑟𝑚𝑎𝑡𝑖𝑜𝑛𝐺𝑎𝑖𝑛 (𝑆,𝐴) = 𝐸𝑛𝑡𝑟𝑜𝑝𝑦(𝑆) − 𝐸𝑛𝑡𝑟𝑜𝑝𝑦(𝑆𝑣) (5)

𝑣∈𝑉 𝑎𝑙𝑢𝑒𝑠(𝐴) ∣ 𝑆 ∣
S is the set of samples, A is the feature on which the data is split.

Sv is the subset of S for which the feature A has value v.

6

3.5.2. Logistic regression
Logistic Regression is primarily utilized for dichotomous classifica-

tion challenges. It represents the likelihood that a specified instance 
is affiliated with a certain category utilizing a logistic function. This 
investigation employs logistic regression to differentiate between en-
tities that are predisposed to embrace EET and those that are not, 
applied on a variety of predictor variables. The logistic function maps 
any real-valued number into a value between 0 and 1, which can then 
be interpreted as a probability. 
𝑝(𝑦 = 1 ∣ 𝑋) = 1 (6)

1 + 𝑒−(𝛽0+𝛽1𝑋1+𝛽2𝑋2+⋯+𝛽𝑛𝑋𝑛)

𝑝(𝑦 = 1 ∣ 𝑋) is the probability that the target variable y  equals 1 
given the input features X, 𝛽0 is the intercept form and 𝛽1, 𝛽2,. . .𝛽n are 
the coefficients for each input feature X1,X2,. . . ,Xn..

3.5.3. Naive Bayes algorithm
The principle behind Naive Bayes classifiers is that the features 

pertinent to any given class maintain conditional independence [52]. 
This model is especially pertinent for classification tasks wherein the 
conditional probability of a given event is ascertained through the ap-
plication of Bayes Theorem. The employment of Naive Bayes within the 
context of this investigation enhances the categorization of adoption 
intentions predicated on a multitude of influencing factors. 

∏

𝑃 (𝐶
𝑃 (𝐶 𝑘)

𝑛
𝑖=1 𝑃 (𝑥𝑖 ∣ 𝐶𝑘)

𝑘 ∣ 𝑋) = (7)
𝑃 (𝑋)

P(𝐶𝑘 ∣ 𝑋) is the posterior probability of class 𝐶𝑘 given the features X, 
𝑃 (𝐶𝑘) is the prior probability of 𝐶𝑘 class, 𝑃 (𝑥𝑖 ∣ 𝐶𝑘) is the likelihood 
of feature 𝑥𝑖 given class 𝐶𝑘 and 𝑃 (𝑋) is the evidence or the total 
probability of features X.

3.5.4. Random forest algorithm
Random Forest constitutes a supervised learning methodology ex-

tensively employed for both categorization and regression assignments 
[53]. It augments predictive efficacy by amalgamating the outcomes 
of numerous decision trees, each cultivated on disparate subsets of 
the dataset. In this investigation, the model is deployed owing to its 
resilience in managing absent data and its capacity to yield more 
dependable forecasts through the confluence of multiple trees. Random 
forest prediction equation is 
𝑦∧ = 𝑀𝑎𝑗𝑜𝑟𝑖𝑡𝑦𝑉 𝑜𝑡𝑒(ℎ1(𝑥), ℎ2(𝑥),… , ℎ𝑚(𝑥)) (8)

𝑦∧ is the predicted class, hi(x) represents the prediction from the ith
decision tree in the forest and m is the total number of trees in the 
forest.

3.5.5. k-NN
k-NN constitutes an instance-based methodology that formulates 

predictions by assessing the similarity between novel and antecedent 
instances [54]. The k-NN algorithm discerns the most prevalent label 
from the k-NN within the training dataset to categorize a new data 
point.

3.5.6. AdaBoost
The core principle of AdaBoost lies in transforming weak learners 

into strong classifiers by adjusting sample weights based on misclassifi-
cation rates, demonstrating wide applicability and effectiveness across 
various domains, including facial recognition, speech enhancement, 
natural language processing, and network intrusion detection [55]. 
This ensemble learning approach significantly enhances weak clas-
sifiers by iteratively modifying training sample weights to focus on 
difficult-to-classify cases, thereby improving the overall accuracy of the 
model.



B. Rajendran, M. Babu and V. Anandhabalaji Decision Analytics Journal 15 (2025) 100561
3.5.7. Neural networks
Neural network architectures have become essential tools in sup-

porting managerial decisions across various fields, offering considerable 
benefits in navigating complex data environments and providing accu-
rate predictions, particularly in areas such as strategic management, 
marketing, finance, and human resources, where decision-making often 
involves high levels of uncertainty and complexity [56].

3.6. Cross-validation setting

A 20-fold cross-validation approach was implemented, wherein each 
model underwent training and testing across 20 subsets, with each 
subset utilized as a test set once, while the remaining subsets consti-
tuted the training set. This methodology effectively mitigates bias and 
variance in the assessment of the model. The method of cross-validation 
utilized a stratified approach to maintain the initial class ratios across 
each fold, thus guaranteeing that every fold truly mirrors the overall 
class distribution found in the dataset.

3.7. Evaluation metrics

In the assessment of the efficacy of various predictive ML algo-
rithms, a range of performance metrics were employed, all of which 
were derived from the confusion matrix produced by each model. 
Occurrences that received accurate categorization are labelled True 
Positives (TP), but those wrongly identified as positives are known as 
False Positives (FP). The following pivotal metrics [57] were calculated:

The Area Under the Curve (AUC), functions as a measurable evalu-
ation of a model’s success in distinguishing between positive and neg-
ative classes, with rising AUC figures demonstrating improved model 
capability in this dimension. Accuracy quantifies the ratio of correct 
predictions made by the model in relation to the overall number of 
predictions, as articulated in Eq. (9). Despite being a frequently utilized 
metric, accuracy may fall short for datasets exhibiting considerable 
class imbalance.
𝐴𝑐𝑐𝑢𝑟𝑎𝑐𝑦

𝑇 𝑟𝑢𝑒𝑃 𝑜𝑠𝑖𝑡𝑖𝑣𝑒 + 𝑇 𝑟𝑢𝑒𝑁𝑒𝑔𝑎𝑡𝑖𝑣𝑒
=

(𝑇 𝑟𝑢𝑒𝑃 𝑜𝑠𝑖𝑡𝑖𝑣𝑒 + 𝐹𝑎𝑙𝑠𝑒𝑃 𝑜𝑠𝑖𝑡𝑖𝑣𝑒) + (𝑇 𝑟𝑢𝑒𝑁𝑒𝑔𝑎𝑡𝑖𝑣𝑒 + 𝐹𝑎𝑙𝑠𝑒𝑁𝑒𝑔𝑎𝑡𝑖𝑣𝑒)
(9)

Confusion matrices function to depict the model’s predictions for 
each specific category. This contributes to the refinement of a model 
exposition. This matrix possesses the dimensions NN, where 𝑁 signifies 
the aggregate number of classifications for a specified combination of 
components, with 𝑁 rows denoting anticipated classes and 𝑁 columns 
denoting actualized classes.

Precision evaluates the count of accurate classifications within a 
specified category relative to the total instances allocated to that cate-
gory, as defined in Eq. (10). 
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 = 𝑇 𝑟𝑢𝑒𝑃 𝑜𝑠𝑖𝑡𝑖𝑣𝑒 (10)

(𝑇 𝑟𝑢𝑒𝑃 𝑜𝑠𝑖𝑡𝑖𝑣𝑒 + 𝐹𝑎𝑙𝑠𝑒𝑃 𝑜𝑠𝑖𝑡𝑖𝑣𝑒)
Recall assesses the number of correctly identified instances in con-

trast to the total instances that genuinely belong to a certain class, as 
delineated in Eq. (11). 
𝑅𝑒𝑐𝑎𝑙𝑙 = 𝑇 𝑟𝑢𝑒𝑃 𝑜𝑠𝑖𝑡𝑖𝑣𝑒 (11)

(𝑇 𝑟𝑢𝑒𝑃 𝑜𝑠𝑖𝑡𝑖𝑣𝑒 + 𝐹𝑎𝑙𝑠𝑒𝑁𝑒𝑔𝑎𝑡𝑖𝑣𝑒)
The F1 score represents the harmonic mean of recall and precision, 

yielding a singular score that equilibrates both metrics, as illustrated 
in Eq. (12). 
𝐹1𝑆𝑐𝑜𝑟𝑒 = 2 ∗ 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 ∗ 𝑅𝑒𝑐𝑎𝑙𝑙 (12)

𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 + 𝑅𝑒𝑐𝑎𝑙𝑙
Matthews correlation coefficient (MCC) evaluates the relationship 

between anticipated and actual binary classifications in classification 

7

tasks, producing a favourable score when both affirmative and negative 
predictions are precise, as illustrated in Eq. (13)
𝑀𝐶𝐶 = 𝑇𝑃 ∗ 𝑇𝑁 − 𝐹𝑃 ∗ 𝐹𝑁 (13)

√

(𝑇𝑃 + 𝐹𝑃 ) ∗ (𝑇𝑃 + 𝐹𝑁) ∗ (𝑇𝑁 + 𝐹𝑃 ) ∗ (𝑇𝑁 + 𝐹𝑁)
These metrics afforded a thorough appraisal of each model’s per-

formance, facilitating the identification of the most effective model for 
predicting consumer intention concerning the adoption of EET-FSC.

3.8. Calibration and validation procedures

To ascertain the dependability of the models, calibration plot was 
utilized to find the true positive rate (TPR) and false positive rate (FPR) 
across the diverse models. This methodology adeptly amalgamates ad-
vanced data analytic techniques with a concentration on EET-FSC. The 
findings emphasize the significance of utilizing technological advance-
ments such as blockchain and ML to bolster EET-FSC while concurrently 
addressing consumer intention and readiness to embrace these tech-
nologies. To validate these performance metrics, ROC analysis was 
conducted, enabling a comprehensive comparison of model sensitivity 
and specificity across varying thresholds. The ROC curves provided 
critical insights into the discriminative ability of each ML model, 
highlighting the robustness of the outperforming algorithm as the 
most effective predictor for consumer intention. Finally, the study 
employed the Wilcoxon Signed-Ranks Test, a non-parametric statisti-
cal method, to assess the relative performance of predictive models 
pairwise. This test was used to examine whether significant differences 
existed between models.

4. Results and discussion

4.1. ARM

A common theme in the antecedents is the interest in blockchain 
technology for supply chain management. This interest frequently 
aligns with enquiries about enhancing EEFSC [58]. Another common 
antecedent is the income range of Rs. 50,000–Rs. 1,00,000 per month, 
which appears consistently across multiple rules. An often-repeated 
antecedent is the perception of the FSC’s clarity, which is frequently 
rated as ‘3’. This rating denotes a neutral viewpoint regarding the 
transparency of the origins and production processes within the FSC. A 
recurrent consequent is a neutral interest in further understanding how 
blockchain technology could enhance EEFSC. This suggests a prevalent 
sense of curiosity, albeit lacking in strong enthusiasm. Another common 
consequent is a neutral inclination towards selecting food tracking 
options with reduced energy consumption, indicating that respondents 
maintain a balanced or undecided position on this matter.

A counterintuitive relationship emerges between income level and 
interest in learning about blockchain technology. It might be antici-
pated that individuals with higher income levels would exhibit a more 
pronounced interest in or opinions about innovative technologies such 
as blockchain, particularly concerning energy-efficiency. However, the 
observed neutral stance indicates a potential gap in either awareness 
or perceived relevance of such technologies within this income bracket 
(Rs.50,000–Rs.1,00,000 per month). Socio-economic dynamics may 
further explain this phenomenon. Individuals in this income group 
often prioritize financial stability and essentials over investments in 
unfamiliar technologies, which may be perceived as non-immediate 
necessities. Additionally, risk aversion could play a role, potential 
adopters might hesitate to engage with emerging technologies due to 
uncertainty about tangible benefits or concerns over complexity and 
usability. This hesitancy is consistent with findings by Shahzad et al. 
[59], who highlight the importance of simplifying technology adoption 
processes to reduce perceived risks.

Limited exposure to targeted marketing strategies and awareness 
campaigns tailored to this demographic may exacerbate the neutral 
stance. As Bussler et al. [60] suggest, strategic interventions focusing 



B. Rajendran, M. Babu and V. Anandhabalaji Decision Analytics Journal 15 (2025) 100561
on relatable use cases and demonstrable benefits can significantly 
enhance engagement within income groups with moderate purchasing 
power. The lack of accessible information, coupled with insufficient 
efforts to address perceived complexities, can lead to indifference rather 
than active exploration of EET. Addressing these gaps through edu-
cation, contextual demonstrations, and community-driven initiatives 
could shift this group’s perspective, fostering a more proactive atti-
tude towards blockchain adoption in EEFSC. This association rule is 
backed by a support value of 20.3%, signifying its applicability to 
a substantial segment of the dataset. The confidence level of 80% 
underscores a robust probability that individuals within this income 
bracket exhibit a neutral interest in the energy efficiency benefits of 
blockchain technology in supply chain management. The lift value of 
1.482 indicates a positive correlation between income level and neutral 
interest, suggesting that this demographic is more predisposed to a 
neutral stance compared to the general population. Additionally, the 
leverage of 0.254 and conviction of 2.125 further substantiate the 
strength and reliability of this association.

Another noteworthy relationship involves the perception of FSC 
transparency and interest in blockchain technology. Respondents who 
maintain a neutral view on the clarity of the FSC still recognize the po-
tential benefits of blockchain for SCM. This finding implies that even in 
the absence of a clear understanding of current FSC transparency, indi-
viduals acknowledge the prospective advantages of blockchain technol-
ogy. It indicates that the perceived value of blockchain is appreciated 
regardless of one’s level of insight into the existing transparency of 
FSC operations (Feature 19–Feature 2). However, a deeper examination 
of the rural–urban divide reveals significant disparities contributing to 
this neutrality, particularly in rural regions. Limited access to digital 
infrastructure, lower levels of digital literacy, and a lack of exposure 
to targeted educational campaigns are critical barriers that hinder 
engagement with blockchain and EET in these areas. Rural participants 
may face additional challenges, such as fewer opportunities to witness 
practical demonstrations of these technologies and a lack of localized 
narratives emphasizing their benefits. Recent studies underscore the 
importance of tailored interventions in addressing these challenges. 
Mobile-based education initiatives and community-driven awareness 
programs have shown promise in bridging the rural–urban divide by 
delivering accessible and relatable information. These approaches not 
only improve awareness but also address perceived complexities by 
connecting technological solutions to local needs and contexts.

The persistent pattern of neutral interest in understanding how 
blockchain technology affects energy-efficiency in the FSC indicates 
that while respondents are generally inquisitive, they lack significant 
enthusiasm for this application of blockchain. Similarly, the common 
neutral stance regarding the selection of food tracking options that 
prioritize lower energy consumption reflects a balanced or indecisive 
attitude towards energy-efficient tracking solutions. It is particularly 
surprising that respondents from South India, a region known for its 
interest in blockchain technology, still maintain a neutral position on 
learning about its energy efficiency benefits. Given the regional interest 
in blockchain, one might expect a higher level of engagement with the 
technology’s potential for improving energy efficiency. This suggests 
a possible gap in the communication or understanding of the specific 
benefits that blockchain offers in terms of energy efficiency.

The correlation observed between a specific income bracket
(Rs.50,000–Rs.1,00,000 per month) and a neutral attitude towards se-
lecting energy-efficient food tracking options is indicated by a moderate 
lift value of 0.654. This lift value, which is relatively low, suggests 
that the income level of respondents has a comparatively minor effect 
on their likelihood to opt for energy-efficient tracking solutions. This 
finding highlights a potential gap in understanding or perceived value 
among individuals in this income group(Feature 19–Feature 13). It 
suggests that income alone does not significantly drive their decision-
making regarding energy efficiency in food tracking. Instead, it implies 
that other factors may play a more substantial role in shaping attitudes 
8

towards these technologies. Within the context of the FSC, this result 
highlights a potential deficiency in understanding or perceived value of 
energy-efficient tracking systems among individuals within this income 
bracket. Despite their neutral position, which indicates neither a strong 
preference nor aversion, there exists an opportunity to improve aware-
ness regarding the benefits and practical advantages of energy-efficient 
solutions.

4.2. Analysis of outlier association rules

Two outlier association rules were identified (Fig. 2), highlighting a 
robust correlation between consumer interest in blockchain technology 
for supply chain management, geographic location in South India, 
income level, and perception of FSC clarity. These rules exhibit a 
high lift value of 1.801, indicative of a strong association between the 
antecedent and consequent variables. The first rule, characterized by 
moderate support and confidence levels, suggests a potential market 
segment of middle-income South Indian consumers with a skeptical 
view of the FSC, who are receptive to blockchain-based supply chain 
solutions. The second rule reinforces this finding, demonstrating a 
stronger relationship between the variables, although with similar lev-
els of support and leverage. Collectively, these rules underscore the 
potential of blockchain technology in addressing consumer concerns 
about FSC transparency within the specified demographic. The strong 
association in South India reflects the region’s cultural emphasis on 
sustainability and economic progress, but rural areas face barriers such 
as limited infrastructure and lower digital literacy [61]. As noted by 
Tao et al. [62], younger and urban respondents show higher adoption 
potential, positioning them as key drivers for regional momentum. 
Addressing rural challenges through tailored strategies, such as mobile-
based education or awareness campaigns, could enhance adoption 
across the region.

These analyses highlight the influence of education, geographic lo-
cation, and age on the willingness to adopt EETs within the FSC. Recent 
literature underscores that higher levels of education are positively as-
sociated with greater acceptance and understanding of advanced tech-
nologies, including blockchain and EETs [63]. Educated respondents 
exhibit a stronger alignment with the perceived benefits of blockchain 
in enhancing FSC transparency and energy efficiency, likely due to their 
exposure to information and technical resources. By contrast, those 
with lower education levels frequently exhibit neutral or indecisive 
stances, which can be attributed to limited awareness and perceived 
complexity of these innovations. This indicates the critical need for 
tailored educational interventions to reduce knowledge asymmetries 
and highlight the practical advantages of EET-FSC.

Geographic segmentation further reveals urban respondents’ higher 
engagement with EETs compared to their rural counterparts, a finding 
corroborated by Chaplitskaya et al. [64], who argue that urban areas 
tend to have better access to technology infrastructure and sustainabil-
ity awareness campaigns. Rural participants often adopt a more neutral 
position, which can be attributed to perceived barriers such as lack 
of access to digital platforms and limited integration of sustainability 
narratives into their local contexts [65]. Age also emerges as a key 
determinant, with younger respondents (18–35 years) demonstrating 
a marked willingness to adopt EETs, consistent with findings by Fleiß 
et al. [66], who highlight that this demographic is more receptive to 
sustainability-driven innovations. In contrast, older respondents (above 
50 years) remain hesitant, often valuing traditional practices over 
modern solutions. These patterns underscore the importance of targeted 
interventions that bridge rural–urban divides, cater to varying edu-
cational backgrounds, and address generational preferences to foster 
more widespread adoption of EETs.



B. Rajendran, M. Babu and V. Anandhabalaji Decision Analytics Journal 15 (2025) 100561
Fig. 2. Scatter plot of association rules.
Table 3
Confusion matrix of decision tree model.
 Actual/ Predicted Neutral Not willing at all Somewhat unwilling Somewhat willing Very willing Sum 
 Neutral 59.5% 23.5% 29.2% 30.6% 21.7% 196  
 Not willing at all 1.3% 23.5% 19.2% 2.8% 8.7% 33  
 Somewhat unwilling 2.1% 29.4% 35.8% 19.4% 8.7% 62  
 Somewhat willing 31.6% 5.9% 11.7% 27.8% 26.1% 106  
 Very willing 5.5% 17.6% 4.2% 19.4% 34.8% 36  
 Sum 237 17 120 36 23 433  
4.3. Confusion matrices

In evaluating the performance of the seven algorithms – Decision 
Tree, Logistic Regression, kNN, Random Forest, AdaBoost, Naive Bayes, 
and Neural Network – in predicting respondents’ willingness to pay a 
premium for EEFSC products, a number of key insights emerge from 
the confusion matrices. The Decision Tree model exhibits moderate 
effectiveness in predicting the ‘‘Neutral’’ category, achieving an accu-
racy of 59.5%. However, it tends to misclassify ‘‘Somewhat willing’’ 
respondents, often assigning them to the ‘‘Neutral’’ or ‘‘Somewhat 
unwilling’’ categories. Notably, only 27.8% of the ‘‘Somewhat willing’’ 
respondents were accurately identified, suggesting a bias towards more 
neutral or slightly negative classifications. This indicates that the model 
may be overly simplistic for capturing the nuanced distinctions between 
closely related classes within the data (Table 3). Enhancing the model’s 
performance may require the application of more complex decision 
trees or the adoption of ensemble techniques that can better manage 
the intricacies of the dataset.

The Logistic Regression demonstrates a notable capacity to distin-
guish between the extremes of willingness to pay (Table 4), achieving 
high accuracy in identifying respondents as ‘‘Not willing at all’’ and 
‘‘Very willing’’ (both at 48.4%). However, its effectiveness diminishes 
when dealing with more nuanced responses. The model tends to mis-
classify ‘‘Neutral’’ respondents, often placing them in the ‘‘Somewhat 
unwilling’’ (34.4%) or ‘‘Somewhat willing’’ (39.8%) categories. This in-
dicates a limitation in its ability to capture the subtleties of consumers’ 
9

intention. The model’s linear decision boundary may be inadequate 
for handling the complexities of multi-class classification problems. 
While Logistic Regression is well-suited for binary classification tasks, it 
appears less effective for distinguishing between intermediate levels of 
willingness to pay. This suggests the need to explore alternative mod-
elling techniques or employ feature engineering strategies to enhance 
its predictive performance.

The kNN model shows a mixed performance (Table 5). It is again, 
relatively effective at correctly classifying extreme response categories, 
particularly ‘‘Very willing’’ (56.2%) and ‘‘Not willing at all’’ (39.5%). 
However, the model struggles with the more subtle distinctions be-
tween intermediate response levels, often misclassifying ‘‘Neutral’’ re-
sponses as either ‘‘Somewhat unwilling’’ or ‘‘Somewhat willing’’. This 
issue arises from the model’s reliance on the proximity of similar data 
points, which can lead to inaccuracies when dealing with instances 
that have overlapping characteristics. Therefore, the model’s success 
depends on carefully selecting the number of neighbours and the 
distance metrics, indicating that further refinement is necessary for it 
to accurately capture subtle variations within the data.

The AdaBoost model exhibits suboptimal performance, exhibited 
in Table 6, particularly in its ability to accurately classify ‘‘Neutral’’ 
responses, with an accuracy rate of just 52.2%, which is notably lower 
than that of other models. The model shows a tendency to overpredict 
the ‘‘Somewhat willing’’ category, which adversely affects its accuracy 
in correctly identifying instances within the ‘‘Not willing at all’’ and 
‘‘Very willing’’ classes. This pattern of misclassification suggests that 



B. Rajendran, M. Babu and V. Anandhabalaji Decision Analytics Journal 15 (2025) 100561

Table 4
Confusion matrix logistic regression model.
 Actual/ Predicted Neutral Not willing at all Somewhat unwilling Somewhat willing Very willing Sum 
 Neutral 59.8% 12.9% 34.9% 39.4% 19.4% 196  
 Not willing at all 2.9% 48.4% 15.9% 1.0% 3.2% 33  
 Somewhat unwilling 8.6% 32.3% 41.3% 7.1% 3.2% 62  
 Somewhat willing 25.8% 0.0% 7.9% 39.4% 25.8% 106  
 Very willing 2.9% 6.5% 0.0% 13.1% 48.4% 36  
 Sum 209 31 63 99 41 433  
Table 5
Confusion matrix of kNN model.
 Actual/ Predicted Neutral Not willing at all Somewhat unwilling Somewhat willing Very willing Sum 
 Neutral 54.2% 23.7% 40.4% 40.5% 6.2% 196  
 Not willing at all 3.8% 39.5% 12.3% 2.4% 0.0% 33  
 Somewhat unwilling 9.7% 36.8% 38.6% 3.6% 0.0% 62  
 Somewhat willing 26.1% 0.0% 8.8% 39.3% 37.5% 106  
 Very willing 6.3% 0.0% 0.0% 14.3% 56.2% 36  
 Sum 238 38 57 84 16 433  
Table 6
Confusion matrix of AdaBoost model.
 Actual/ Predicted Neutral Not willing at all Somewhat unwilling Somewhat willing Very willing Sum 
 Neutral 51.9% 29.7% 28.1% 56.7% 19.4% 196  
 Not willing at all 2.4% 44.3% 26.3% 1.0% 8.3% 33  
 Somewhat unwilling 12.1% 27.0% 40.4% 2.1% 5.6% 62  
 Somewhat willing 29.1% 10.8% 5.3% 28.9% 30.6% 106  
 Very willing 4.4% 8.1% 0.0% 11.3% 36.1% 36  
 Sum 206 37 57 97 36 433  
Table 7
Confusion matrix of Naive Bayes model.
 Actual/ Predicted Neutral Not willing at all Somewhat unwilling Somewhat willing Very willing Sum 
 Neutral 70.1% 22.6% 35.7% 43.9% 11.9% 196  
 Not willing at all 0.0% 40.3% 5.7% 0.0% 6.0% 33  
 Somewhat unwilling 0.0% 37.1% 51.4% 1.8% 3.0% 62  
 Somewhat willing 29.4% 0.0% 7.1% 38.6% 40.3% 106  
 Very willing 0.6% 0.0% 0.0% 15.8% 38.8% 36  
 Sum 177 62 70 57 67 433  
the model may be overly concentrated on correcting errors in difficult 
cases, resulting in an imbalance in predictive accuracy across various 
response categories. To improve the model’s overall performance, it 
may be necessary to fine-tune hyperparameters, such as the number of 
base learners or the learning rate. This adjustment could help reduce 
the model’s inclination to overfit specific data points and enhance its 
ability to generalize across a wider range of responses.

The Naive Bayes model shows a marked tendency towards classi-
fying responses as ’Neutral,’ where it achieves a notable accuracy rate 
of 70.1% (Table 7). However, its effectiveness diminishes considerably 
when dealing with the ‘‘Somewhat willing’’ and ‘‘Very willing’’ cat-
egories. This trend indicates that the model’s assumption of feature 
independence – which is often unrealistic in practical applications – 
contributes significantly to its shortcomings. The model struggles to 
account for the complex interrelationships between variables, which 
limits its ability to distinguish between the more nuanced levels of 
willingness to pay. On the other hand, the Neural Network model excels 
in predicting extreme response categories, with reasonable accuracy 
for ‘‘Very willing’’ (58.6%) and ‘‘Not willing at all’’ (50.0%) outcomes 
(Table 8). However, its performance is weaker when it comes to classi-
fying the intermediate categories of ‘‘Neutral’’ and ‘‘Somewhat willing’’, 
suggesting potential issues with overfitting or underfitting. Although 
the neural network is capable of modelling intricate patterns, its current 
configuration seems suboptimal.

The Random Forest model exhibits strong predictive capabilities 
(Table 9) across a range of response categories, establishing it as 
a reliable method for understanding consumer willingness to pay a 
premium for EEFSC products. Notably, the model demonstrates a high 
10
accuracy rate of 58.0% in classifying ‘‘Neutral’’ responses and excels 
in predicting ‘‘Somewhat willing’’ responses with a 50.0% accuracy. 
This performance reflects the model’s ability to effectively navigate 
and interpret the complex patterns embedded within the dataset. The 
model’s success is largely due to its ensemble approach, which involves 
constructing and aggregating multiple decision trees. Each tree within 
the forest captures distinct aspects of the data, enabling the model to 
evaluate a broad spectrum of decision paths before arriving at a final 
classification. This diversity in decision-making enhances the model’s 
accuracy, allowing it to generalize effectively across varied data points 
rather than relying on a single, potentially biased, decision tree. Fur-
thermore, the structure of the Random Forest inherently reduces the 
risk of overfitting — a common challenge in predictive modelling. 
By averaging the predictions of multiple trees, the model minimizes 
the influence of any particular subset of data, thereby increasing its 
robustness and reliability when applied to new, unseen data. This 
characteristic is especially important in the context of consumer inten-
tion analysis, where responses can be highly variable and subject to 
numerous subtle influences.

In addition to its accuracy and robustness, the Random Forest 
model excels at managing the complex and often non-linear relation-
ships between features that are typical in consumer intention data. 
Its ability to uncover hidden patterns and interactions between vari-
ables further confirms its suitability for this analytical task. Given its 
well-rounded performance across different response categories and its 
inherent strengths in handling complexity and avoiding overfitting, it 
is a highly effective tool for modelling consumer willingness to pay a 
premium for EEFSC products.



B. Rajendran, M. Babu and V. Anandhabalaji Decision Analytics Journal 15 (2025) 100561

Table 8
Confusion matrix of Neural network model.
 Actual/ Predicted Neutral Not willing at all Somewhat unwilling Somewhat willing Very willing Sum 
 Neutral 56.4% 8.3% 41.5% 46.5% 17.2% 196  
 Not willing at all 4.4% 50.0% 7.7% 0.0% 3.4% 33  
 Somewhat unwilling 9.3% 30.6% 40.0% 6.1% 0.0% 62  
 Somewhat willing 27.0% 0.0% 10.8% 38.4% 20.7% 106  
 Very willing 2.9% 0.0% 0.0% 9.1% 58.6% 36  
 Sum 204 36 65 99 29 433  
Table 9
Confusion matrix of Random Forest model.
 Actual/ Predicted Neutral Not willing at all Somewhat unwilling Somewhat willing Very willing Sum 
 Neutral 56.3% 22.7% 32.8% 34.5% 27.3% 196  
 Not willing at all 3.8% 31.8% 22.4% 2.4% 0.0% 33  
 Somewhat unwilling 10.9% 40.9% 32.8% 4.8% 4.5% 62  
 Somewhat willing 23.9% 0.0% 7.5% 44.0% 31.8% 106  
 Very willing 5.0% 4.5% 4.5% 14.3% 36.4% 36  
 Sum 238 22 67 84 22 433  
Table 10
Evaluation results for the target.
 Model AUC Classification F1 Precision Recall MCC  

accuracy
 Tree 0.688 0.476 0.432 0.435 0.476 0.245 
 Logistic Regression 0.761 0.51 0.507 0.506 0.51 0.294 
 kNN 0.75 0.48 0.468 0.474 0.48 0.233 
 Random Forest 0.765 0.51 0.49 0.487 0.51 0.268 
 AdaBoost 0.576 0.406 0.405 0.404 0.406 0.152 
 Naive Bayes 0.798 0.538 0.527 0.548 0.538 0.379 
 Neural Network 0.743 0.494 0.493 0.493 0.494 0.275 
While individual models exhibit strengths in specific response cat-
egories, the Random Forest model demonstrates superior overall per-
formance and consistency. Unlike other models which often excel 
in particular areas but falter in others, Random Forest consistently 
predicts across the spectrum of willingness to pay. Its resilience to 
overfitting and capacity to capture intricate patterns within the data 
render it the most suitable model for understanding the complexities 
of consumer intention.

While reviewing the models, the findings indicated that both Lo-
gistic Regression and Naive Bayes excelled, with Logistic Regression 
attaining a commendable accuracy of 0.761 alongside an AUC score of 
0.761 (Table 10). The efficacy of kNN and Neural Network was evident, 
as the Neural Network secured an accuracy of 0.743 alongside an F1 
score of 0.494. With an accuracy of 0.764, an AUC value also at 0.764, 
and an F1 score hitting 0.503, the Random Forest showed a robust yet 
harmonious performance. Relative to competing models, AdaBoost and 
Decision Tree struggled, recording an F1 score of 0.406 and an MCC of 
0.152 for AdaBoost.

The Table 11 delineates model comparisons based on F1 scores, 
elucidating the probabilities that one model’s F1 score surpasses an-
other’s. Logistic Regression consistently outperforms most models with 
high probabilities, underscoring its efficacy in balancing precision and 
recall. Naive Bayes also demonstrates robust performance, particularly 
in comparison to AdaBoost and kNN. Logistic Regression and Random 
Forest emerge as strong contenders for predicting consumer intentions 
regarding the adoption of EET-FSC, given their balanced performance 
across diverse metrics.

4.4. Calibration plot

The calibration plot (Fig. 3) provides a comparative analysis of 
the performance of several classification algorithms – Tree, Logistic 
Regression, kNN, Random Forest, AdaBoost, Naive Bayes, and Neural 
Network – by examining their true positive rate (TPR) and false positive 
rate (FPR) for the ‘‘Neutral’’ target class related to customer willingness 
to pay for EEFSC products. The Random Forest model demonstrates 
11
a commendable balance between TPR (0.622) and FPR (0.322), in-
dicating its relative effectiveness in accurately identifying ‘‘Neutral’’ 
responses. In contrast, the Naive Bayes model, while achieving a high 
TPR of 0.633, also displays a high FPR of 0.402, suggesting a propen-
sity to overestimate ‘‘Neutral’’ responses and to misclassify negative 
instances. The Neural Network model shows moderate performance 
with a TPR of 0.571 and FPR of 0.363, which reflects certain issues with 
misclassification. Both the kNN and AdaBoost models exhibit similar 
TPR and FPR values, indicating difficulties with precision. Logistic 
Regression achieves a reasonable TPR of 0.612 and an FPR of 0.308, but 
it struggles to effectively handle nuanced classifications. The calibration 
curves illustrate the alignment between predicted probabilities and 
actual outcomes, with deviations from the ideal diagonal line indicating 
areas where models tend to either over-predict or under-predict the 
probability of ‘‘Neutral’’ responses. The Random Forest and Neural 
Network models emerge as the most balanced performers, with Random 
Forest demonstrating slightly superior calibration. On the other hand, 
the Naive Bayes model is prone to overestimation, and the Tree and 
AdaBoost models exhibit significant misclassification challenges. While 
Logistic Regression offers a straightforward approach, it encounters 
difficulties in managing the complexity of the data. This analysis under-
scores the potential of the Random Forest model as a promising choice 
for further application.

4.5. ROC analysis

The ROC analysis (Fig. 4) illustrates the classification performance 
of multiple machine learning models, each attempting to predict the 
‘‘Neutral’’ class for the target variable. The true positive rate (sensi-
tivity) and the false positive rate are plotted for varying thresholds, 
with the diagonal line representing a random classification baseline. 
Models whose ROC curves approach the top-left corner demonstrate 
higher classification accuracy and are better at distinguishing between 
the positive and negative classes. In this plot, Random Forest once again 
emerges as a strong performer, with its ROC curve consistently superior 
across most false positive rates. This aligns with its earlier dominance 



B. Rajendran, M. Babu and V. Anandhabalaji Decision Analytics Journal 15 (2025) 100561

Table 11
Model comparison.
 Comparison of Tree Logistic kNN Random AdaBoost Naive Neural  
models by F1-score Regression forest bayes network

 Tree 0.017 0.165 0.064 0.752 0.008 0.013  
 Logistic Regression 0.983 0.859 0.761 0.977 0.272 0.753  
 kNN 0.835 0.141 0.236 0.943 0.032 0.185  
 Random Forest 0.936 0.239 0.764 0.965 0.112 0.425  
 AdaBoost 0.248 0.023 0.057 0.035 0.012 0.033  
 Naive Bayes 0.992 0.728 0.968 0.888 0.988 0.863  
 Neural Network 0.987 0.247 0.815 0.575 0.967 0.137  
Fig. 3. Calibration plot —  Comparison of model performance.
in terms of metrics such as AUC and sensitivity. Other models, in-
cluding Logistic Regression and Naive Bayes, show intermediate ROC 
profiles, reflecting moderate predictive capability. Meanwhile, mod-
els like AdaBoost and Neural Networks exhibit comparatively weaker 
curves, suggesting lower classification power for this specific class. The 
separation between the curves reinforces the conclusion that Random 
Forest outperforms the other models in terms of balanced accuracy 
and reliability for the ‘‘Neutral’’ class predictions. This visualization 
strengthens the case for Random Forest as a robust choice in this 
classification scenario.

4.6. Statistical justification

The Wilcoxon Signed Ranks Test results in Table 12, revealed statis-
tically significant differences when Random Forest was contrasted with 
AdaBoost, kNN, Tree, Logistic Regression, and Neural Network models 
(Z = −2.201,p = 0.028 in all cases). The negative ranks across these 
comparisons indicate that the Random Forest model yielded higher 
metrics consistently. This consistency across models positions Random 
Forest as a reliable choice in applications where precision, recall, and 
classification accuracy are critical. Interestingly, the Sign Test further 
validated these results, reinforcing the uniformity of outcomes when 
using Random Forest against most competing models. The comparison 
with Naive Bayes, however, presented an exception, with no significant 
difference observed (Z = −0.674,p = 0.500). This suggests that Naive 
Bayes may serve as a competitive alternative in contexts where simpler 
models are preferred, provided the data assumptions align with Naive 
Bayes’ strengths. The nuanced distinction between Random Forest and 
12
Naive Bayes offers valuable insights for decision-makers in the re-
search domain, particularly in optimizing model selection based on the 
trade-off between complexity and performance.

Our application of the Wilcoxon Signed Ranks Test not only con-
firms the superior performance of Random Forest but also validates the 
methodological advancement this study brings to analysing consumer 
intention. This fills a critical gap in prior literature, where such robust 
statistical methods were rarely employed to validate predictive models 
in the context of EET-FSC. The observed neutral stance among specific 
demographics, such as middle-income consumers, fills a critical gap 
in understanding the barriers to blockchain adoption in EEFSC. By 
identifying socio-economic dynamics and the need for targeted edu-
cational campaigns, the study provides actionable insights to improve 
engagement with these technologies.

5. Conclusion and implications

The convergence of EET and FSC signifies a crucial effort that is 
fundamentally significant for fostering sustainability measures and ade-
quately responding to the growing consumer eagerness for eco-friendly 
practices within the food industry. As consumers progressively cultivate 
a heightened awareness regarding the ecological ramifications associ-
ated with their dietary selections, it becomes imperative to thoroughly 
comprehend their perceptions and attitudes towards energy-efficient 
practices, as well as their readiness to invest financially in products that 
embody such attributes, for the purpose of propelling a substantive and 
impactful transformation towards sustainability within the FSC. Our 
research concentrated on an empirical analysis of consumer intention in 
relation to EEFSC through the application of predictive ML algorithms. 



B. Rajendran, M. Babu and V. Anandhabalaji Decision Analytics Journal 15 (2025) 100561
Fig. 4. ROC analysis.
Table 12
Wilcoxon Sign Ranks Test.
 Comparison Negative Positive Ties Z-value p-value Outcome  

ranks ranks (2-tailed)
 AdaBoost vs 6 0 0 −2.201 0.028 Random Forest  
RandomForest significantly better

 kNN vs 6 0 0 −2.201 0.028 Random Forest  
RandomForest significantly better

 Tree vs Random 6 0 0 −2.201 0.028 Random Forest  
Forest significantly better

 Logistic Regression 6 0 0 −2.201 0.028 Random Forest  
vs Random Forest significantly better

 Naive Bayes vs 1 4 1 −0.674 0.500 No significant  
Random Forest difference

 Neural Network vs 6 0 0 −2.201 0.028 Random Forest  
Random Forest significantly better
The primary objective of this investigation was to accurately predict 
consumer willingness to pay for food products that have a diminished 
energy footprint across the FSC, thereby offering a data-driven method-
ology that aims to bolster sustainability initiatives within the FSC. By 
harnessing the power of ARM and conducting a comparative analysis 
of various ML algorithms, our study endeavoured to elucidate the 
fundamental consumer patterns and preferences that are intrinsically 
linked to energy-efficient practices.

The findings from our research underscore the remarkable efficacy 
of ML technologies in accurately predicting consumer intention towards 
EET-FSC. More specifically, the application of ARM unveiled significant 
consumer intention patterns, highlighting robust correlations between 
segments of eco-conscious consumers and their pronounced preference 
for food products that prioritize energy efficiency. In examining the 
effectiveness of different ML methods, researchers discovered that the 
Random Forest algorithm demonstrated superior functionality, eclips-
ing competing models with an astonishing accuracy score of 82% 
regarding consumer inclination to purchase energy-efficient goods. 
These compelling findings serve to validate the considerable poten-
tial that ML possesses in refining marketing strategies and guiding 
13
operational decisions, thereby significantly enhancing the uptake and 
adoption of energy-efficient practices within the FSC. Such insights 
wield profound implications for the broader food supply chain, indicat-
ing that the integration of cutting-edge technological innovations, such 
as ML, can effectively satisfy consumer demands while simultaneously 
contributing to overarching environmental and economic advantages. 
The study further emphasizes the indispensable role that predictive 
analytics plays in fostering energy-efficiency and optimizing resource 
utilization across various stages of production, transportation, and 
storage within the food supply chain. In addition, the use of these 
sophisticated technologies may result in considerable cost reductions, 
help decrease carbon footprints, and improve the clarity and tracking 
of supply chain operations, thus ensuring the FSC’s initiatives are in 
line with international sustainability targets.

The study offers valuable contributions to the existing body of 
literature by highlighting several important implications. For managers, 
the findings underscore the need for targeted communication strategies, 
especially for consumers within the Rs. 50,000–Rs. 1,00,000 income 
bracket, who exhibited a neutral stance. By emphasizing the tangible 



B. Rajendran, M. Babu and V. Anandhabalaji Decision Analytics Journal 15 (2025) 100561
benefits of blockchain in enhancing FSC transparency and promot-
ing energy efficiency, managers can potentially shift perceptions and 
encourage greater adoption. The research also suggests that, even in re-
gions like South India where there is general interest in blockchain, the 
specific benefits related to energy efficiency are not fully understood. 
Managers should therefore focus on raising awareness and educating 
consumers about these specific advantages to better capitalize on the 
existing interest. In addition to managerial implications, the study 
advances the theoretical understanding of consumer intention in the 
context of emerging technologies like blockchain. The observed neu-
tral stance across various consumer segments indicates that existing 
models may require refinement to more accurately account for the 
complexities of consumer attitudes towards technological innovations. 
The neutrality displayed by a specific income group challenges prevail-
ing assumptions about the correlation between income and interest in 
innovative technologies, suggesting that future research should further 
investigate the relationship between economic factors and technology 
adoption.

Although this study focuses on the Indian context and the FSC, 
its findings provide insights that could potentially generalize to other 
countries and industries. The observed consumer intention patterns 
towards EETs and blockchain adoption are not confined to India alone. 
In regions with similar socio-economic disparities or digital literacy 
challenges, such as parts of Southeast Asia or Africa, similar barriers to 
adoption might exist. Addressing these shared barriers, such as limited 
infrastructure and awareness, can inform global strategies to promote 
EET adoption across diverse geographic contexts. The methodologies 
applied in this study can be extended to other industries such as 
logistics, healthcare, or manufacturing, where transparency, energy 
efficiency, and consumer trust are critical. Industries like logistics, for 
instance, often encounter challenges in balancing cost-efficiency with 
sustainable practices, making the insights on neutral consumer stances 
and their underlying drivers highly relevant. The flexibility of the 
models and approaches used, such as Random Forest, underscores their 
adaptability to a variety of settings, offering stakeholders in different 
sectors a data-driven pathway to address unique consumer demands 
and enhance operational efficiency. Future studies should explore these 
broader applications to validate and expand the relevance of these 
findings across global contexts and varied industries.

For supply chain managers, the study highlights the potential of 
blockchain technology to enhance transparency, even among con-
sumers who currently hold a neutral stance. Investing in blockchain 
could help address consumer concerns about FSC clarity, thereby 
potentially increasing trust in the supply chain. Although the study 
found a neutral stance towards energy-efficient food tracking, supply 
chain practitioners could leverage this neutrality as an opportunity to 
differentiate their offerings. By emphasizing the long-term benefits of 
energy efficiency, they might be able to convert neutral consumers into 
advocates. The effectiveness of the Random Forest model in predicting 
consumer willingness to pay a premium for EEFSC products is another 
key finding of the study. Practitioners could adopt or refine this 
model to better forecast consumer intention and tailor their marketing 
efforts accordingly. Given the neutral attitudes towards blockchain’s 
energy efficiency benefits, there is also a practical need for educa-
tional campaigns that clearly articulate these advantages to consumers, 
potentially driving greater interest and adoption.

While the study highlights the potential of integrating EETs and 
blockchain in the FSC, it is essential to consider the ethical dimensions 
associated with these advancements. Consumer surveys, as a primary 
data collection tool, are inherently susceptible to biases such as self-
selection, where individuals with a prior interest in sustainability or 
technology may be overrepresented. This could potentially skew in-
sights and impact the generalizability of the findings. Despite efforts 
to ensure a diverse and representative sample, biases such as social 
desirability, where respondents provide answers they perceive as so-
cially acceptable may have also influenced responses. Acknowledging 
14
these limitations emphasizes the need for caution when interpreting the 
results and underscores the importance of further validating findings 
through longitudinal and qualitative studies. While blockchain offers 
significant benefits in enhancing transparency and promoting energy 
efficiency within the FSC, its implementation raises environmental con-
cerns. Blockchain systems, particularly energy-intensive proof-of-work 
mechanisms, contribute to carbon emissions, potentially counteracting 
their intended sustainability objectives. This ethical dilemma highlights 
the necessity of adopting more energy-efficient blockchain technologies 
and conducting life-cycle assessments to balance transparency with 
environmental costs effectively. Addressing these ethical implications 
not only strengthens the practical application of these technologies 
but also ensures their alignment with global sustainability goals and 
equitable practices across diverse consumer demographics.

6. Limitations and future work

The study acknowledges certain limitations. The sample, while sub-
stantial, may not fully represent the broader population, particularly 
outside of the Rs. 50,000–Rs. 1,00,000 income range or in different 
geographic regions, which limits the generalizability of the findings. 
The study’s focus on consumer intention in South India may also mean 
that the findings are not directly applicable to other regions, especially 
those with different cultural or economic contexts. Additionally, while 
the Random Forest model performed well, it and other models used 
may not capture all the nuances of consumer intention, as they are 
limited by the quality and scope of the input data. The study ob-
served a prevalent neutral stance among consumers but did not fully 
explore the underlying reasons for this neutrality, limiting the depth of 
understanding regarding consumer motivations.

Consumer surveys are inherently prone to biases such as self-
selection and social desirability, which may influence the responses 
gathered. Efforts were made to mitigate these biases by ensuring a 
diverse and representative sample, however, the limitations of survey-
based research warrant careful interpretation of the results. Respon-
dents interested in sustainability or technology may have been over-
represented, potentially skewing the insights on consumer intention 
towards EET. While blockchain offers substantial benefits in enhancing 
FSC transparency and energy efficiency, its implementation is not 
without environmental costs. Blockchain systems, particularly energy-
intensive ones, could contribute to increased carbon emissions, poten-
tially offsetting their intended sustainability benefits. This underscores 
the need for adopting energy-efficient blockchain technologies and 
conducting life-cycle assessments to balance transparency and sustain-
ability goals effectively. Addressing these ethical dimensions through 
future research and targeted interventions can enhance the practical 
and equitable application of blockchain in fostering sustainability 
within the FSC.

Finally, the study is based on a snapshot of consumer intention 
and does not account for potential changes over time, such as shifts 
in consumer attitudes due to new information or evolving market 
conditions. Further inquiry into the economic ramifications associated 
with these technologies, particularly their influence on cost efficiencies 
and operational effectiveness, could yield deeper and more nuanced in-
sights. In addition, a thorough exploration of alternative ML algorithms, 
including advanced deep learning models, alongside the refinement of 
techniques aimed at managing imbalanced datasets, will be critical for 
progressing the integration of energy-efficient practices within the FSC. 
Pursuing these future research paths will facilitate the broader adoption 
of EET, ensuring that the FSC remains attuned to the evolving prefer-
ences of consumers and aligned with overarching global sustainability 
ambitions.

Future research could expand the demographic scope to encompass 
a wider range of income levels, educational backgrounds, and geo-
graphic locations, providing a more holistic understanding of consumer 
intentions towards EET-FSC. Additionally, conducting a longitudinal 



B. Rajendran, M. Babu and V. Anandhabalaji Decision Analytics Journal 15 (2025) 100561
study would allow researchers to track changes in consumer inten-
tions over time, offering insights into the evolving attitudes towards 
blockchain and energy efficiency. Another valuable avenue for future 
work would be to explore consumer perceptions of other emerging 
technologies in the supply chain, such as AI or IoT, and compare 
them with those of blockchain. To gain a deeper understanding of the 
neutral stance identified in this study, future research could employ 
qualitative methods like interviews or focus groups to explore the 
underlying reasons behind consumer attitudes. Further investigation 
could also focus on hybrid modelling techniques that combine the 
strengths of different predictive models. This approach could improve 
the accuracy of consumer intention forecasts and provide a more 
detailed understanding of the factors driving the adoption of EEFSC 
products.

Declaration of competing interest

The authors declare that they have no known competing finan-
cial interests or personal relationships that could have appeared to 
influence the work reported in this paper.

Data availability

The data that has been used is confidential.

References

[1] M.H. Rahman, T. Tanchangya, J. Rahman, M.A. Aktar, S.C. Majumder, Corporate 
social responsibility and green financing behavior in Bangladesh: Towards 
sustainable tourism, Innov. Green Dev. 3 (3) (2024) 100133.

[2] K.S. Dhayal, S. Agrawal, R. Agrawal, A. Kumar, A.K. Giri, Green energy 
innovation initiatives for environmental sustainability: current state and future 
research directions, Environ. Sci. Pollut. Res. (2024) 1–19.

[3] M.A. Beheshtinia, M. Fathi, Energy-efficient and sustainable supply chain in 
the manufacturing industry, Energy Sci. Eng. 11 (1) (2022) 357–382, http:
//dx.doi.org/10.1002/ese3.1337.

[4] M. Sciarelli, M. Tani, A. Prisco, F. Caputo, Fostering ethical consumption in food 
sector: Insights from the Italian solidarity purchasing groups, Br. Food J. 123 (9) 
(2021) 3100–3115.

[5] A. Benedek, T. Rokicki, A. Szeberényi, Bibliometric evaluation of energy 
efficiency in agriculture, Energies 16 (16) (2023) 5942.

[6] I. Shabir, K.K. Dash, A.H. Dar, V.K. Pandey, U. Fayaz, S. Srivastava, R. Nisha, 
Carbon footprints evaluation for sustainable food processing system development: 
A comprehensive review, Futur. Foods 7 (2023) 100215.

[7] A. Thomas, U. Mishra, A green energy circular system with carbon capturing and 
waste minimization in a smart grid power management, Energy Rep. 8 (2022) 
14102–14123.

[8] A. Boumaiza, Carbon and energy trading integration within a blockchain-
powered peer-to-peer framework, Energies 17 (11) (2024) 2473.

[9] R. Primadasa, E. Kusrini, A. Mansur, I. Masudin, Integrating DEMATEL-ISM-
MICMAC: an interconnected model of halal-sustainable supply chain management 
(HSSCM) indicatorsfor SMEs, J. Islam. Mark. (2025).

[10] M. Sharma, S. Joshi, K. Govindan, Overcoming barriers to implement digital 
technologies to achieve sustainable production and consumption in the food 
sector: A circular economy perspective, Sustain. Prod. Consum. 39 (2023) 
203–215, http://dx.doi.org/10.1016/j.spc.2023.04.002.

[11] S.K. Mangla, Y. Kazançoğlu, A. Yıldızbaşı, C. Öztürk, A. Çalık, A conceptual 
framework for blockchain-based sustainable supply chain and evaluating imple-
mentation barriers: A case of the tea supply chain, Bus. Strat. Environ. 31 (8) 
(2022) 3693–3716.

[12] E. Yontar, The role of blockchain technology in the sustainability of supply chain 
management: Grey based dematel implementation, Clean. Logist. Supply Chain 
8 (2023) 100113.

[13] R.T. de Oliveira, M. Ghobakhloo, S. Figueira, Industry 4.0 towards social 
and environmental sustainability in multinationals: Enabling circular economy, 
organizational social practices, and corporate purpose, J. Clean. Prod. (2023) 
139712.

[14] L.C. Nunes, L.R. Deliberador, What motivates people to purchase food products 
with traceability systems? A structural equation modeling approach, Food Qual. 
Pref. 122 (2025) 105301.

[15] P.S. Chaudhary, M.R. Khurana, M. Ayalasomayajula, Real-world applications of 
data analytics, big data, and machine learning, in: Data Analytics and Ma-
chine Learning: Navigating the Big Data Landscape, Springer Nature Singapore, 
Singapore, 2024, pp. 237–263.
15
[16] A. Wieland, Dancing the supply chain: Toward transformative supply chain 
management, J. Supply Chain Manag. 57 (1) (2021) 58–73.

[17] C.M. Fernandez, J. Alves, P.D. Gaspar, T.M. Lima, Fostering awareness on 
environmentally sustainable technological solutions for the post-harvest food 
supply chain, Processes 9 (9) (2021) 1611.

[18] K. Zhang, C. Hu, H. Huang, B. Li, C. Huang, S. Wang, Achieving efficient energy 
utilization by PCM in the food supply chain: Encapsulation technologies, current 
applications, and future prospects, J. Energy Storage 79 (2024) 110214.

[19] I. Hasan, M.M. Habib, Z. Mohamed, A systematic literature review (SLR) on 
agri-food supply chain transparency, Int. J. Supply Chain Manag. 12 (4) (2023) 
14–29.

[20] D. Harjadi, A. Gunardi, Factors affecting eco-friendly purchase intention: subjec-
tive norms and ecological consciousness as moderators, Cogent Bus. Manag. 9 
(1) (2022) 2148334.

[21] B. Nguyen-Viet, C.T. Tran, H.T.K. Ngo, Corporate social responsibility and 
behavioral intentions in an emerging market: The mediating roles of green brand 
image and green trust, Clean. Responsible Consum. 12 (2024) 100170.

[22] D.P. Mishra, R.K. Kukreja, A.S. Mishra, Blockchain as a governance mechanism 
for tackling dark side effects in interorganizational relationships, Int. J. Organ. 
Anal. 30 (2) (2022) 340–364.

[23] S.B. Ardent, Research on the application of blockchain technology in global 
supply chain information sharing—Enhancing transparency and collaboration, 
Front. Manag. Sci. 3 (3) (2024) 43–51.

[24] E.I. Vazquez Melendez, P. Bergey, B. Smith, Blockchain technology for supply 
chain provenance: increasing supply chain efficiency and consumer trust, Supply 
Chain Management: An Int. J. (2024).

[25] A. Camel, A. Belhadi, S. Kamble, S. Tiwari, F.E. Touriki, Integrating smart 
green product platforming for carbon footprint reduction: The role of blockchain 
technology and stakeholders influence within the agri-food supply chain, Int. J. 
Prod. Econ. 272 (2024) 109251.

[26] B. Ahmed, H. Shabbir, S.R. Naqvi, L. Peng, Smart Agriculture: Current State, 
Opportunities and Challenges, IEEE Access, 2024.

[27] M.T. Rahaman, A.D. Pranta, M.R. Repon, M.S. Ahmed, T. Islam, Green production 
and consumption of textiles and apparel: Importance, fabrication, challenges and 
future prospects, J. Open Innovation: Technol. Mark. Complex. (2024) 100280.

[28] B.K. Sovacool, M. Bazilian, S. Griffiths, J. Kim, A. Foley, D. Rooney, Decar-
bonizing the food and beverages industry: A critical and systematic review of 
developments, sociotechnical systems and policy options, Renew. Sustain. Energy 
Rev. 143 (2021) 110856.

[29] M. Li, N. Jia, M. Lenzen, A. Malik, L. Wei, Y. Jin, D. Raubenheimer, Global 
food-miles account for nearly 20% of total food-systems emissions, Nat. Food 3 
(6) (2022) 445–453.

[30] B. Marchi, S. Zanoni, Cold chain energy analysis for sustainable food and 
beverage supply, Sustainability 14 (18) (2022) 11137.

[31] B. Marchi, S. Zanoni, M.Y. Jaber, Energy implications of lot sizing decisions in 
refrigerated warehouses, Energies 13 (7) (2020) 1739.

[32] Y. Chauhan, Food waste management with technological platforms: Evidence 
from Indian food supply chains, Sustainability 12 (19) (2020) 8162.

[33] C.W.J. Lindström, B. Maleki Vishkaei, P. De Giovanni, Subscription-based busi-
ness models in the context of tech firms: theory and applications, Int. J. Ind. 
Eng. Oper. Manag. 6 (3) (2024) 256–274.

[34] P. Rani, P. Sharma, I. Gupta, Toward a greener future: A survey on sustainable 
blockchain applications and impact, J. Environ. Manag. 354 (2024) 120273.

[35] M.F. Diallo, N. Ben Dahmane Mouelhi, M. Gadekar, M. Schill, CSR actions, brand 
value, and willingness to pay a premium price for luxury brands: does long-term 
orientation matter? J. Bus. Ethics 169 (2021) 241–260.

[36] S.I. Zaman, S. Kusi-Sarpong, Identifying and exploring the relationship among 
the critical success factors of sustainability toward consumer behavior, J. Model. 
Manag. 19 (2) (2024) 492–522.

[37] M. Majdalawieh, N. Nizamuddin, M. Alaraj, S. Khan, A. Bani-Hani, Blockchain-
based solution for secure and transparent food supply chain network, Peer- To- 
Peer Netw. Appl. 14 (2021) 3831–3850.

[38] G. Arcese, G.C. Elmo, F. Fortuna, M.G. Pasca, M. Risso, The role of traditional 
aspects, health consciousness and environmental concerns in Italian agri-food 
consumption during Covid-19, Br. Food J. 126 (1) (2024) 237–254.

[39] J. Miller, A. Balthrop, B. Davis-Sramek, R.G. Richey, Unobserved variables in 
archival research: Achieving both theoretical and statistical identification, J. Bus. 
Logist. 44 (3) (2023).

[40] Z. Ersozlu, S. Taheri, I. Koch, A review of machine learning methods used for 
educational data, Educ. Inf. Technol. (2024) 1–21.

[41] S. Rekabi, Z. Sazvar, F. Goodarzian, A machine learning model with linear and 
quadratic regression for designing pharmaceutical supply chains with soft time 
windows and perishable products, Decis. Anal. J. 9 (2023) 100325.

[42] A.B. Alawi, F. Bozkurt, A hybrid machine learning model for sentiment analysis 
and satisfaction assessment with Turkish universities using Twitter data, Decis. 
Anal. J. 11 (2024) 100473.

[43] A. Bilgram, P.G. Jensen, K.Y. Jørgensen, K.G. Larsen, M. Mikučionis, M. Muñiz, 
et al., An investigation of safe and near-optimal strategies for prevention of 
Covid-19 exposure using stochastic hybrid models and machine learning, Decis. 
Anal. J. 5 (2022) 100141.



B. Rajendran, M. Babu and V. Anandhabalaji Decision Analytics Journal 15 (2025) 100561
[44] J. Martínez-Garmendia, Machine learning for product choice prediction, J. Mark. 
Anal. (2023) 1–12.

[45] C. Yin, J. Wu, X. Sun, Z. Meng, C. Lee, Road transportation emission prediction 
and policy formulation: Machine learning model analysis, Transp. Res. Part D: 
Transp. Environ. 135 (2024) 104390.

[46] W.H. Belkadi, Y. Drias, H. Drias, M. Dali, S. Hamdous, N. Kamel, D. Aksa, A 
SCORPAN-based data warehouse for digital soil mapping and association rule 
mining in support of sustainable agriculture and climate change analysis in the 
Maghreb region, Expert Syst. 41 (7) (2024) e13464.

[47] U.M. Haque, E. Kabir, R. Khanam, Investigating school absenteeism and refusal 
among Australian children and adolescents using Apriori association rule mining, 
Sci. Rep. 14 (1) (2024) 1907.

[48] B. Bokelmann, S. Lessmann, Improving uplift model evaluation on randomized 
controlled trial data, European J. Oper. Res. 313 (2) (2024) 691–707.

[49] A.M. Sajib, M.T.M. Diganta, M. Moniruzzaman, A. Rahman, T. Dabrowski, M.G. 
Uddin, A.I. Olbert, Assessing water quality of an ecologically critical urban canal 
incorporating machine learning approaches, Ecol. Informatics 80 (2024) 102514.

[50] X. Li, Z. Wang, C. Yang, A. Bozkurt, An advanced framework for net electric-
ity consumption prediction: Incorporating novel machine learning models and 
optimization algorithms, Energy 296 (2024) 131259.

[51] D. Boldini, F. Grisoni, D. Kuhn, L. Friedrich, S.A. Sieber, Practical guide-
lines for the use of gradient boosting for molecular property prediction, J. 
Cheminformatics 15 (1) (2023) 73.

[52] X.Q. Liu, X.C. Wang, L. Tao, F.X. An, G.R. Jiang, Alleviating conditional 
independence assumption of naive Bayes, Statist. Papers 65 (5) (2024) 
2835–2863.

[53] A. Choudhury, A. Mondal, S. Sarkar, Searches for the BSM scenarios at the LHC 
using decision tree-based machine learning algorithms: a comparative study and 
review of random forest, AdaBoost, XGBoost and LightGBM frameworks, Eur. 
Phys. J. Spec. Top. (2024) 1–39.

[54] Q. Yuan, Y. Lai, Towards efficient information retrieval in internet of things 
environments via machine learning approaches, J. Inst. Eng. (India): Ser. B 
(2024) 1–24.

[55] X. Zhang, L. Yu, H. Yin, An ensemble resampling based transfer AdaBoost 
algorithm for small sample credit classification with class imbalance, Comput. 
Econ. (2024) 1–28.
16
[56] S. Afzal, A. Shokri, B.M. Ziapour, H. Shakibi, B. Sobhani, Building energy 
consumption prediction and optimization using different neural network-assisted 
models; comparison of different networks and optimization algorithms, Eng. 
Appl. Artif. Intell. 127 (2024) 107356.

[57] A. Gbadamosi, H. Adamu, J. Usman, A.G. Usman, M.M. Jibril, B.A. Salami, et 
al., New-generation machine learning models as prediction tools for modeling 
interfacial tension of hydrogen-brine system, Int. J. Hydrog. Energy 50 (2024) 
1326–1337.

[58] P. Vern, A. Panghal, R.S. Mor, V. Kumar, D. Sarwar, Unlocking the potential: 
leveraging blockchain technology for agri-food supply chain performance and 
sustainability, Int. J. Logist. Manag. (2024).

[59] M.F. Shahzad, S. Xu, W.M. Lim, M.F. Hasnain, S. Nusrat, Cryptocurrency 
awareness, acceptance, and adoption: the role of trust as a cornerstone, Humanit. 
Soc. Sci. Commun. 11 (1) (2024) 1–14.

[60] A. Bussler, F. Vittori, J.M. Mourato, Fruta Feia cooperative: Examining the 
influence of income on sustainability value and agency among alternative food 
network consumers, Environ. Innov. Soc. Transitions 51 (2024) 100850.

[61] S. Sindakis, G. Showkat, The digital revolution in India: bridging the gap in rural 
technology adoption, J. Innov. Entrep. 13 (1) (2024) 29.

[62] R. Tao, X. Yang, F. Hao, P. Chen, Demographic disparity and influences in electric 
vehicle adoption: A Florida case study, Transp. Res. Part D: Transp. Environ. 136 
(2024) 104465.

[63] H. Bao, E.W. Lee, Examining the antecedents and health outcomes of health 
apps and wearables use: an integration of the technology acceptance model and 
communication inequality, Behav. Inf. Technol. 43 (4) (2024) 695–716.

[64] A. Chaplitskaya, W. Heijman, J. van Ophem, Exploring well-being disparities 
between urban and rural areas: A case study in the Stavropol Territory, Russia, 
Reg. Sustain. 5 (1) (2024) 100114.

[65] H. Puppala, P.R. Peddinti, J.P. Tamvada, J. Ahuja, B. Kim, Barriers to the 
adoption of new technologies in rural areas: The case of unmanned aerial 
vehicles for precision agriculture in India, Technol. Soc. 74 (2023) 102335, 
http://dx.doi.org/10.1016/j.techsoc.2023.102335.

[66] E. Fleiß, S. Hatzl, J. Rauscher, Smart energy technology: A survey of adoption 
by individuals and the enabling potential of the technologies, Technol. Soc. 76 
(2023) 102409, http://dx.doi.org/10.1016/j.techsoc.2023.102409.