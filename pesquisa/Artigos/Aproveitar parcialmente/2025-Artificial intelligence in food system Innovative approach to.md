---
source_file: "2025-Artificial intelligence in food system Innovative approach to.txt"
original_rel_path: "Trabalhos\Artigos\Aproveitar parcialmente\txt\2025-Artificial intelligence in food system Innovative approach to.txt"
category: "Artigos_Aproveitar_parcialmente"
extension: ".txt"
sha256: "5e43458efbef41054e90af78e8f3a895f36cf4e600c19feebf53b05df02c549e"
extracted_at: "2026-09-20T00:50:21.702962"
---

﻿See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/390573356

Artificial Intelligence in Food System: Innovative Approach to Minimizing

Food Spoilage and Food Waste

Article  in  Journal of Agriculture and Food Research · April 2025
DOI: 10.1016/j.jafr.2025.101895

CITATION READS

1 126

10 authors, including:

Helen Onyeaka Taghi Miri
University of Birmingham University of Birmingham

302 PUBLICATIONS   6,320 CITATIONS    84 PUBLICATIONS   2,294 CITATIONS   

SEE PROFILE SEE PROFILE

Nnabueze Darlington Nnaji Phemelo Tamasiga
University of Birmingham German Institute of Development and Sustainability

24 PUBLICATIONS   348 CITATIONS    40 PUBLICATIONS   612 CITATIONS   

SEE PROFILE SEE PROFILE

All content following this page was uploaded by Helen Onyeaka on 11 April 2025.

The user has requested enhancement of the downloaded file.



Journal of Agriculture and Food Research 21 (2025) 101895 

Contents lists available at ScienceDirect

Journal of Agriculture and Food Research
journal homepage: www.sciencedirect.com/journal/journal-of-agriculture-and-food-research

Artificial intelligence in food system: Innovative approach to minimizing 
food spoilage and food waste
Helen Onyeaka a,* , Adenike Akinsemolu a,b,c, Taghi Miri a, Nnabueze Darlington Nnaji a,d,  
Keru Duan e, Gu Pang e, Phemelo Tamasiga f, Samran Khalid g, Zainab T. Al-Sharify a,h,i,  
Chinenye Ugwa a

a School of Chemical Engineering, University of Birmingham, Edgbaston, B15 2TT, Birmingham, United Kingdom
b The Green Institute, Akure Road, Ondo 351101, Ondo State, Nigeria
c The Institute for Oil, Gas and Environment, Energy and Sustainable Development, Afe Babalola University, Ado Ekiti 360001, Ekiti State, Nigeria
d Department of Microbiology, University of Nigeria, Nsukka, Nigeria
e Birmingham Business School, University of Birmingham, Edgbaston, Birmingham, B15 2TT, United Kingdom
f Public Policy in Africa Initiative, Yaounde Cameroon
g National Institute of Food Science and Technology, University of Agriculture, Faisalabad, 38000, Pakistan
h Department of Oil and Gas Refining Engineering, Al Hikma University College, Baghdad, Iraq
i Department of Environmental Engineering, College of Engineering, Mustansiriyah University, Baghdad, Iraq

A R T I C L E  I N F O A B S T R A C T

Keywords: Globally, about one-third of all food produced for human consumption is lost or wasted, compounding issues of 
Artificial intelligence food security, economic inefficiency, and environmental harm. Artificial Intelligence (AI) presents trans
Food spoilage formative potential to mitigate these losses by enhancing food spoilage predictions and optimizing supply chain 
Food waste management. This paper examines the deployment of AI technologies such as machine learning models, pre
Machine learning
Predictive analytics dictive analytics, and advanced algorithm in predicting food spoilage with high accuracy, thereby reducing food 

waste substantially. Key innovations highlighted include early detection systems for spoilage indicators, dynamic 
algorithms for optimal storage conditions, and predictive models for waste forecasting based on real-time 
environmental data. A review of case studies, including AI-driven solutions from Shelf Engine and Afresh, 
shows a 14.8 % reduction in food waste per store, with an associated reduction of 26,705 tons of CO2 emissions. 
Similarly, IKEA achieved a 30 % reduction in kitchen food waste within one year using AI-powered monitoring 
systems. Despite these successes, challenges in data collection, model training, and the integration of AI into 
existing food management systems persist. These include issues related to data quality, legacy system compat
ibility, and regulatory barriers. The paper concludes with actionable recommendations for future research, 
urging interdisciplinary collaboration to develop standardized data protocols, enhance real-time monitoring 
capabilities, and address the ethical implications of AI adoption in the food sector. By advancing these strategies, 
AI’s full potential in curbing global food waste can be realized.

1. Introduction demand and supply dynamics, which in turn can drive up prices during 
periods of scarcity. Furthermore, food waste contributes to broader so

The World Food Programme (WFP) reports that one-third of food cietal issues by intensifying economic disparities. Those who are 
produced worldwide for human consumption is wasted at various stages wealthier can better afford food, thus widening the gap between social 
of the food supply chain [1]. This waste is enough to feed two billion classes. In addition, the environmental impact of food waste is signifi
people, a critical fact given that 30 % of the world’s population currently cant, as decomposing waste emits harmful pollutants. To address these 
experiences moderate to severe food insecurity, and over 900 million multifaceted problems, solutions to reduce food waste are essential. 
people face severe food shortages [2]. Food waste not only exacerbates Artificial Intelligence (AI) has emerged as a potent tool in this regard, 
these issues but also affects food availability by influencing market particularly through its ability to predict food spoilage before it 

* Corresponding author. School of Chemical Engineering, University of Birmingham, Edgbaston, B15 2TT, Birmingham, United Kingdom.
E-mail address: h.onyeaka@bham.ac.uk (H. Onyeaka). 

https://doi.org/10.1016/j.jafr.2025.101895
Received 22 January 2025; Received in revised form 29 March 2025; Accepted 5 April 2025  
Available online 6 April 2025 
2666-1543/© 2025 Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by-nc-nd/4.0/ ). 



H. Onyeaka et al.                                                                                                                                                                     J  o  u r  n  a l  o  f   A  g  r i c u  l t u  r e   a  n d    F  o  o d    R  e  s e  a r  c h 21 (2025) 101895 

happens, potentially reducing waste significantly. By leveraging AI, These questions investigate the deployment of AI tools such as ma
there is potential to improve the sustainability of the global food supply chine learning models and predictive analytics in enhancing the accu
chain, presenting a pathway to a more stable and equitable future. racy of food spoilage predictions, which could lead to significant 

Every year, approximately 1.3 billion tons of food are wasted reductions in food waste. We explore the obstacles related to data 
worldwide, resulting in financial losses estimated at US$1 trillion [3]. collection, model training, and the practical integration of AI technol
Table 1 offers a detailed summary of food waste distribution and its ogies into the food industry’s operational frameworks, emphasizing the 
primary causes throughout various stages of the supply chain. Chauhan need for standardized data and interoperable systems.
et al. [4] identify that approximately 24 % of food waste occurs at the This study provides a holistic analysis of AI applications across 
production and post-harvest stages, attributed mainly to inefficient multiple stages of the food supply chain, integrating real-time moni
agricultural practices and inadequate storage facilities, respectively. In toring, predictive modeling, and decision-support systems. Unlike pre
addition, 17 % of waste arises during transportation, often due to vious studies, this research explores how AI can dynamically adapt to 
improper handling and adverse environmental conditions. At the retail real-world complexities, including fluctuating food demand, variable 
level, 20 % of food is wasted due to overstocking and stringent cosmetic storage conditions, and multi-stakeholder interactions. The study pre
standards. However, the consumption stage accounts for the most sig sents a novel framework for AI-driven food spoilage detection and waste 
nificant loss, 35 %, predominantly influenced by consumer behaviors reduction, leveraging machine learning, IoT, and blockchain technolo
such as excessive purchasing. gies to enhance decision-making and efficiency.

The economic impact of food waste is profound, encompassing not 
only the direct loss of food value but also indirect costs including 2. Methodology
healthcare expenses, pollution, and waste management [9]. These eco
nomic repercussions vary based on household and national economic 2.1. Research approach
status, with wealthier entities generally wasting more food at the con
sumer level, whereas poorer households and developing countries A comprehensive literature review was conducted to establish a 
experience higher losses post-harvest [10]. foundational understanding of AI applications in minimizing food 

Food waste not only highlights the disparities between affluent and waste. To ensure a broad yet rigorous examination of existing research, 
impoverished populations by affecting their respective food access and multiple databases were utilized, including PubMed (for studies related 
security [11] but also imposes substantial environmental costs. The to food systems), Google Scholar (to access a wide range of scholarly 
cultivation of food demands extensive use of critical resources such as articles, including grey literature), and Scopus (for interdisciplinary 
land and water, which are squandered when the food is not consumed research coverage).
[6]. In addition, the disposal and decomposition of wasted food 
contribute significantly to environmental degradation, emitting an 2.2. Search strategy
equivalent of 3.3 Gt of carbon dioxide annually [6]. These environ
mental and economic impacts underline the urgent need for strategic The search strategy incorporated Boolean operators (AND, OR, NOT) 
interventions to mitigate food waste at all levels of the supply chain. to refine results and improve relevance. Keywords included “AI in food 

This paper seeks to review the broader impacts of AI applications on systems”, “food spoilage prediction”, “machine learning in food waste 
reducing economic losses due to food waste and minimizing environ management”, “supply chain optimization”, and “AI-driven food 
mental damage through more effective resource management and waste sustainability”.
reduction strategies. We aim to address the following research 
questions. 2.3. Eligibility criteria

RQ 1: How can artificial intelligence (AI) technologies be applied to Articles were selected based on the following criteria. 
predict and reduce food spoilage across different stages of the food 
supply chain? • Inclusion Criteria: Relevance to AI-driven food waste reduction, 
RQ 2: What are the challenges associated with integrating AI into publication in peer-reviewed journals, and the presence of empirical 
existing food management systems, and how can these challenges be data or robust theoretical frameworks.
overcome to improve the efficiency and effectiveness of food • Exclusion Criteria: Studies lacking methodological rigor or those that 
spoilage prevention? did not directly address the application of AI in food waste reduction.
RQ 3: What potential does AI hold for improving economic and 
environmental sustainability in the food supply chain through The review primarily covered research published between 2020 and 
enhanced spoilage prediction and waste reduction? 2024 to capture recent advancements, with an emphasis on the latest 

studies up to May 2024. This approach ensured that the paper’s analysis 
was grounded in the most current and relevant findings

Table 1 
Overview of food waste by stage in the supply chain. 3. AI innovations in predicting food spoilage

Stage Percentage of Key Factors Contributing to Waste
Total Waste The integration of AI, along with other Industrial 4.0 technologies 

like big data and Internet of Things (IoT), is anticipated to significantly 
Production 24 % Inefficient farming techniques, natural 

disasters enhance the food supply chain. According to Romanello and Veglio 
Post-Harvest 24 % Poor storage facilities, lack of proper [12], these technologies are set to improve food quality and safety, boost 

infrastructure environmental sustainability, and increase operational efficiency across 
Transportation and 17 % Inadequate transportation methods, all stages of the food supply chain. AI is utilized in various phases such as 

Retail delays, exposure to unsuitable 
environments crop monitoring and early pest detection during the planting and pro
Overstocking, cosmetic standards, duction stages, storage monitoring post-harvest, routing optimization in 
improper handling transportation, inventory management in retail, and expiry tracking at 

Consumption 35 % Over-purchasing, lack of planning, poor the consumption stage. This comprehensive application of AI not only 
consumer habits addresses quality and efficiency but also plays a crucial role in reducing 

Source: Adapted from Chauhan et al. [4], WFP [3], Xue et al. [5]. food spoilage and waste, offering a potential solution to a persistent 

2 



H. Onyeaka et al.                                                                                                                                                                     J  o  u r  n  a l  o  f   A  g  r i c u  l t u  r e   a  n d    F  o  o d    R  e  s e  a r  c h 21 (2025) 101895 

global issue. Fig. 1 outlines the various stages of the food supply chain taste, texture, color, and water activity of food, making it unsafe or 
and the specific applications of AI and other technologies at each stage unpleasant for consumption [27]. AI and machine learning technologies 
to enhance efficiency and reduce waste. offer promising solutions to mitigate food waste by predicting spoilage 

In the food supply chain, AI technologies play a critical role across with high accuracy before it occurs. These machine-learning models are 
various stages to ensure efficiency and food safety. At the production trained on extensive datasets that include information about food 
stage, AI is employed for crop monitoring, pathogen detection in agri characteristics, ideal storage conditions, and signs of spoilage [28]. 
culture, and detecting microorganisms in poultry farms, aiming to These advanced models not only predict the shelf life of food items but 
enhance the quality and yield of agricultural products by preventing also use environmental data such as humidity, temperature, and venti
diseases and pests [13,14]. For instance, deep learning models have lation to recommend optimal storage conditions, thus preventing 
been successfully implemented in crop disease detection, significantly spoilage. In microbiology, AI is also repurposed for the early detection of 
improving early identification and prevention strategies [15]. More pathogens in food, contributing to food safety by predicting and 
over, AI-driven spectral imaging techniques have demonstrated high reducing the risks of foodborne illnesses [29].
accuracy in detecting pathogens in poultry farms, improving biosecurity Further, AI and big data (characterized by high volume, velocity, and 
measures [16]. During the post-harvest stage, AI aids in monitoring variety of information) play crucial roles in identifying early warning 
storage environments and sanitizing processing equipment to reduce signs of food safety risks during production, such as harmful algal 
losses from spoilage and contamination [17]. Studies show that blooms affecting seafood or fungal growth in crops, which could lead to 
AI-integrated IoT systems enable real-time monitoring of storage con mycotoxin formation. Big data technologies, including machine learning 
ditions, helping to predict and prevent spoilage [18,19]. algorithms, cloud computing, and predictive analytics, process vast 

In transportation, AI applications like routine optimization, tem amounts of real-time data from diverse sources such as IoT sensors, 
perature control, and cold-chain break analysis ensure perishable goods satellite imaging, and microbiological analysis to detect contamination 
are transported efficiently and remain unspoiled, particularly vital for patterns, optimize food distribution, and improve risk assessment in 
temperature-sensitive products [20]. Research indicates that food safety. These technologies enable the food industry to effectively 
AI-powered predictive analytics enhance cold-chain logistics, mini monitor and assess quality and safety in real-time, ensuring product 
mizing temperature fluctuations that compromise food quality [21]. At integrity and consumer health [30]. These AI-enabled systems have been 
the retail level, AI supports inventory management and food safety effectively implemented in various practical scenarios, such as the US 
training to manage stock effectively and ensure compliance with food FDA’s use of AI to detect problematic seafood imports and vegetable 
safety standards. AI-based demand forecasting techniques have growers using AI to manage crop risks based on environmental factors 
improved inventory optimization, reducing food waste in bakeries [22]. [31,32]. AI does not only enhance food safety but also reduces food 
Additionally, AI-driven training systems enhance food safety compli waste by allowing for more precise management of food quality and 
ance by providing interactive learning modules for food handlers [23, safety risks throughout the supply chain.
24]. Finally, during consumption, AI helps identify unsafe foods through 
analysis of online review comments and tracking expiration dates, thus 5. AI for optimizing food storage and distribution
assisting consumers in avoiding spoiled or unsafe products. Sentiment 
analysis of online reviews has proven effective in detecting foodborne AI technology enhances food preservation by predicting and pre
illness outbreaks, allowing for timely intervention [25]. Moreover, venting spoilage, aligning closely with sustainable agricultural prac
AI-powered smart labeling systems aid consumers in tracking product tices. Notably, a machine learning model described by Sonwani et al. 
freshness and expiration dates, reducing household food waste [26]. [33] assesses whether fruits and vegetables are stored under optimal 
Overall, Fig. 1 highlights the interconnected role of advanced technol conditions by analyzing images of produce under varying temperature 
ogies in optimizing each stage of the food supply chain, aiming to and humidity settings using convolutional neural networks (CNNs). This 
minimize waste and enhance food safety from production to consump model not only predicts the shelf life of these items but also supports the 
tion. These technological interventions not only aim to increase the ef development of intelligent inventory systems that minimize waste 
ficiency of these processes but also contribute to sustainability by through real-time adjustments of storage conditions. The model uses 
reducing the environmental impact associated with food waste and image recognition algorithms to detect subtle visual cues of spoilage 
spoilage. such as color change and texture degradation and pairs this data with 

environmental sensors to refine predictions of produce deterioration. 
4. AI for early detection Additionally, AI’s predictive analytics are utilized to anticipate con

sumer demand patterns, allowing for better alignment of food produc
Food spoilage results from various factors including the presence of tion with consumption, thus reducing the likelihood of overproduction 

pathogens, chemical and biochemical reactions, physical damage, and [34]. Recurrent neural networks (RNNs), such as Long Short-Term 
enzymatic activities. These factors alter the pH, nutritional content, Memory (LSTM) models, are employed to recognize seasonal 

Fig 1. AI application in food supply chain.

3 



H. Onyeaka et al.                                                                                                                                                                     J  o  u r  n  a l  o  f   A  g  r i c u  l t u  r e   a  n d    F  o  o d    R  e  s e  a r  c h 21 (2025) 101895 

fluctuations and forecast future demand, allowing for better alignment protocols for data collection, which complicates efforts to standardize 
of food production with consumption, thus reducing the likelihood of data, a crucial step for developing robust AI applications [38]. These 
overproduction [35]. These capabilities extend throughout the supply challenges underscore the complexities involved in deploying AI for 
chain, ensuring proper storage conditions are maintained by adjusting food spoilage prediction and highlight the need for concerted efforts to 
factors such as temperature and humidity in real-time. AI also facilitates improve data quality and standardization in this field. Table 3 provides a 
the efficient redistribution of food to areas with high demand, such as summary of key challenges and potential solutions in implementing AI 
shelters, by integrating logistics optimization algorithms that prioritize for food spoilage prediction.
deliveries based on freshness and need. The integration of AI in food spoilage prediction faces significant 

AI also plays a crucial role in managing microbiological risks during hurdles, not least of which is data accessibility and sharing. Ethical 
storage, transportation, and consumption, by analyzing environmental concerns about data privacy, proprietary interests, and adherence to 
conditions and identifying patterns that could lead to foodborne ill regulatory standards frequently obstruct the free exchange of valuable 
nesses. [24]. Predictive models based on support vector machines data resources [53]. The reliance on expansive and diverse sets of 
(SVMs) or random forests can flag potential risk factors by correlating training data, sourced from various devices such as sensors, cell phones, 
storage conditions with microbiological data to anticipate outbreaks of and cameras, introduces additional complexities related to data security 
spoilage or contamination [24]. These models not only improve food and the potential exposure of sensitive personal information [40]. 
safety but also reduce waste due to spoilage and contamination. Moreover, collaborative projects often encounter obstacles in formu

Beyond food safety, AI applications offer significant environmental lating data-sharing agreements, adhering to legal frameworks, and 
and economic benefits. For instance, Bhatia et al. [6] report that AI reconciling stakeholder concerns over data ownership and intellectual 
implementation in food management has notably reduced CO2 emis property rights [41].
sions, with one case showing an annual reduction of 26,705 tons. To navigate these challenges, implementing strategies for data 
Economically, AI-driven forecasting tools, such as demand prediction standardization, fostering open data platforms, and cultivating part
models and dynamic pricing algorithms, have proven effective in the nerships is essential. This includes harmonizing data formats, ontol
grocery sector, reducing costs related to unsold inventory and disposal ogies, and metadata to ensure consistency and interoperability across 
while boosting profitability. The Pacific Coast Food Waste Commitment diverse sources [54]. Open data initiatives, which promote transparency 
[8] cites an average profit increase of 14.8 % per store following the and protect privacy through anonymization and encryption, are crucial 
adoption of AI technologies for inventory management (see Table 2). in this context [39]. Moreover, collaboration among industry stake
These advancements highlight the multifaceted benefits of AI, under holders, academic researchers, and regulatory authorities is vital to 
scoring its impact on both environmental sustainability and economic facilitate data sharing, establish best practices, and address the legal and 
efficiency in the food industry. ethical dimensions of data utilization [55].

A notable example of an innovative solution to these issues is the 
6. Challenges in implementing AI for food spoilage prediction decentralized privacy-preserving technology used by Gorji et al. [40]. 

This approach leverages federated learning alongside new fluorescence 
Implementing AI for predicting food spoilage presents substantial imaging technology and two deep learning models to detect invisible 

challenges, primarily stemming from the need for diverse, high-quality residues on food preparation equipment and surfaces, classifying them 
data essential for training effective predictive models. Data collection as clean or contaminated. This model operates without the need to share 
involves accumulating detailed information on variables such as tem data across clients or store data on a centralized server, thus enhancing 
perature, humidity, storage conditions, and microbial activity. Howev client data privacy and addressing one of the critical challenges in 
er, acquiring extensive and representative datasets is often difficult due deploying AI in food safety applications.
to the variability across different food types, storage conditions, and As AI and machine learning models become more prevalent in the 
spoilage processes, as highlighted by Anwar et al. [36]. Each type of food field of food spoilage, issues of bias in these technologies have also come 
has unique properties and degradation paths, requiring specifically to the forefront. Ruben, Emilio, and Javier [42] highlight that biases can 
tailored datasets for accurate modeling [37]. manifest at various stages of the AI development pipeline, from data 

Moreover, ensuring the quality and consistency of the data collected collection to model training and deployment. During the data collection 
is a significant challenge. Data sources vary widely, ranging from sensor and labeling phase, biases may arise if the dataset is incomplete, 
outputs and manual observations to historical records, each offering non-representative, or if different annotators interpret labels inconsis
differing levels of accuracy and reliability [38]. Issues such as errors, tently, leading to skewed outputs from AI algorithms. Similarly, biases 
biases, or missing entries in these datasets can severely impact the can occur in the model training phase if the data is unbalanced or if the 
performance of AI models, leading to flawed predictions and unreliable model architecture is ill-equipped to handle diverse inputs.
outcomes [39]. Moreover, it is crucial to continuously monitor and test AI models 

Another obstacle is the standardization of data collected from with a variety of inputs post-deployment to detect and mitigate biases. 
disparate sources. The food industry lacks universally accepted Thomas et al. [48] note that such biases can exacerbate existing social 

inequalities if biased data reinforce pre-existing prejudices. This issue is 
illustrated by Supriya [43], who observed that AI models can display 

Table 2 discriminatory patterns against people of color, a problem that often 
Financial and environmental impact of AI in food waste reduction. goes unrecognized when the training data itself harbors biases such as 

Impact Type Quantitative Benefit Reference Case out-group homogeneity. These biases not only distort the outputs but 
Reduction in Reduction of 26,705 tons Case Study involving AI also perpetuate and intensify social inequalities and discrimination. 

CO2 Emissions annually implementation in retail Therefore, addressing these biases is essential for ensuring fairness and 
grocery [8] equity in AI applications within food safety and beyond.

Cost Savings Decrease in costs associated Grocery retail sector through The conceptual framework illustrating sources of bias in AI deploy
with food disposal and unsold AI forecasting tools [7]
inventory ment within food systems (Fig. 2) critically underscores the multifaceted 

Increased The average increase in profits AI-enhanced inventory nature of biases that may compromise the accuracy, fairness, and 
Profitability by 14.8 % per store management in multiple applicability of AI-driven food spoilage prediction models. Data-related 

stores [8] biases, such as incomplete or skewed datasets, can arise from over- 
Sources: Bhatia et al. [6] for environmental impact figures, and Ciccullo et al. reliance on historical sales records that fail to capture emerging con
[7] and Pacific Coast Food Waste Commitment [8] for financial benefits. sumption trends, leading to inaccurate demand forecasting. Algorithmic 

4 



H. Onyeaka et al.                                                                                                                                                                     J  o  u r  n  a l  o  f   A  g  r i c u  l t u  r e   a  n d    F  o  o d    R  e  s e  a r  c h 21 (2025) 101895 

Table 3 Table 3 (continued )
Summary of key challenges and solutions in implementing AI for food spoilage Category Challenge Description References
prediction.

FoodON) to improve 
Category Challenge Description References data consistency.
Data Diverse, High- Difficult to collect Anwar et al. Active Learning & Use active learning Shorten and 

Collection Quality Data comprehensive data [36], Deng et al. Synthetic Data and synthetic data to Khoshgoftaar 
on temperature, [37] fill gaps and reduce [50]
humidity, microbial bias.
activity across food Federated Implement federated Sheller et al. 
types. Learning learning to protect [51]

Data Variability Different food types Anwar et al. data privacy while 
require tailored [36] training models.
datasets, making data Continuous Use fairness-aware Mehrabi et al. 
collection complex. Model algorithms to monitor [52]

Data Quality Inaccurate or missing Wang et al. Monitoring and correct biases in 
Issues data from sources like [38], deployed AI models.

sensors or records Voulodimos 
affect AI predictions. et al. [39]

Data Lack of universal Wang et al. [38] biases emerge when AI models disproportionately weight specific 
Standardization protocols for data spoilage factors such as temperature fluctuations while neglecting var

collection complicates iables like microbial growth, thereby reducing predictive robustness. 
consistency.

Data Privacy & Ethical and legal Qian et al. [24], Operational and human biases further exacerbate inefficiencies, as 
Accessibility Security Concerns barriers hinder data Gorji et al. [40] decision-makers may either overtrust or disregard AI recommendations 
& Sharing sharing, especially based on subjective intuition, potentially undermining the system’s ef

sensitive personal ficacy. Moreover, external constraints, including regulatory in
data. consistencies and economic disparities, hinder equitable AI adoption, 

Legal & Intellectual property Houser and 
Regulatory and legal concerns Bagby [41] particularly among small-scale retailers who may lack the financial re
Barriers block data sharing sources to implement sophisticated predictive analytics. For instance, 

agreements. while large grocery chains can leverage AI-driven demand forecasting 
Decentralized Federated learning can Gorji et al. [40] tools to optimize inventory management, smaller vendors relying on 
Data Solutions address privacy issues 

by keeping data traditional methods could face increased food waste due to less precise 
decentralized. stock adjustments. Addressing these biases necessitates a comprehensive 

Bias in AI Data-Related Skewed or incomplete Ruben et al. approach that integrates diverse datasets, refines algorithmic trans
Models Biases datasets result in [42] parency, and ensures equitable access to AI technologies across the food 

biased predictions. supply chain, ultimately fostering a more sustainable and efficient food 
Algorithmic Overemphasis on Ruben et al. 
Biases certain factors (e.g., [42] management ecosystem.

temperature) reduces To address challenges in AI-driven food spoilage prediction, targeted 
prediction accuracy. strategies must be implemented to enhance data standardization, miti

Operational & Subjective decisions Supriya [43] gate bias, and improve integration. First, establishing universal data 
Human Biases based on intuition 

affect AI model collection protocols is essential for ensuring consistency and compara
deployment. bility across different datasets. Standardized ontologies, such as the 

Integration & Legacy System Difficulty integrating Patel et al. [44] FoodON framework [49], can facilitate interoperability and improve 
Operations Compatibility AI with existing food data quality. Additionally, techniques like active learning and synthetic 

management systems. data generation can help compensate for gaps in real-world datasets, 
Organizational & Training staff and Richey et al. 
Workforce adapting workflows [45] reducing bias and improving model generalization [50]. To address 
Barriers for AI adoption can be ethical concerns surrounding data sharing, federated learning where AI 

challenging. models are trained across decentralized devices without sharing raw 
Financial High initial costs and Rejeb et al. [46] data has been successfully used in medical imaging and can be adapted 
Constraints maintenance expenses 

create financial to food safety applications [51]. Moreover, ongoing monitoring of AI 
barriers. models using adversarial testing and fairness-aware algorithms can 

Regulatory & Lack of AI technologies face Thakkar et al. detect and correct biases that emerge post-deployment [52]. Industry 
Legal Regulatory regulatory gaps in food [47] collaborations, including partnerships between regulatory agencies, 
Barriers Frameworks safety standards and food producers, and technology developers, can also foster the adoption 

assessment.
Data Need for standardized Mu et al. [31], of best practices and regulatory frameworks that balance innovation 
Harmonization data formats for Thakkar et al. with ethical considerations [56]. Implementing these solutions will not 

international [47] only enhance the accuracy and fairness of AI models but also support a 
collaboration. more sustainable and equitable food supply chain.

Ethical & Bias AI models may Thomas et al. 
Fairness Amplification perpetuate societal [48], Supriya Achieving high accuracy, integrity, and reliability in AI models is 
Issues biases if trained on [43] critical for their effective application in predicting food spoilage. This 

biased data. requires comprehensive training datasets that encompass a variety of 
Ensuring Fairness Continuous Thomas et al. food types, storage conditions, and spoilage factors. Jarray et al. [57] 

monitoring of AI [48] emphasize the importance of improving data collection methodologies, 
models is needed to 
detect and correct advancing feature selection techniques, and refining algorithmic ap
emerging biases. proaches to boost prediction accuracy. Additionally, real-world valida

Strategies for Standardizing Develop universal Dooley et al. tion of AI models is vital to ensure their robustness and applicability 
Solutions Data Protocols protocols for data [49] across different operational environments. This validation process in

collection (e.g., volves rigorous testing in actual settings to evaluate model performance, 
pinpoint limitations, and adjust algorithms as necessary ([57]; Wang 

5 



H. Onyeaka et al.                                                                                                                                                                     J  o  u r  n  a l  o  f   A  g  r i c u  l t u  r e   a  n d    F  o  o d    R  e  s e  a r  c h 21 (2025) 101895 

Fig 2. Sources of bias in AI deployment for food systems.

et al., 2021). financial advantages of avoiding disposal of unsold inventory and 
Integrating AI technologies into existing food management and reducing shrinkage highlight the effectiveness of AI in boosting profit

supply chain systems also presents significant challenges. Technological ability while addressing food waste.
issues such as compatibility with legacy systems, interoperability con Further emphasizing the operational benefits, AI automates labor- 
cerns, and the necessity for specialized infrastructure to support AI intensive tasks such as ordering and restocking, leading to increased 
implementations are notable barriers [44]. Furthermore, operational efficiency and cost reductions. Successful pilot programs and the sub
hurdles include the need to adapt existing workflows and processes to sequent broader implementation of AI solutions across multiple stores 
integrate AI insights seamlessly, requiring organizational commitment, demonstrate the scalability and effectiveness of these technologies in the 
workforce training, and change management strategies [45]. Financial grocery retail industry.
obstacles also arise, including substantial initial investment costs, Several case studies illustrate the concrete impact of AI in reducing 
ongoing maintenance expenses, and uncertain returns on investment food waste. For example, retailers using AI solutions from Shelf Engine 
[46]. and Afresh saw an average food waste reduction of 14.8 % per store, 

Additionally, the regulatory landscape is yet to fully adapt to the achieving not only reduced shrinkage and higher profits but also labor 
integration of AI, with a current lack of appropriate scientific knowledge efficiency improvements that offset the costs of AI implementation [8]. 
and assessment practices within regulatory agencies to effectively Moreover, these initiatives prevented 26,705 tons of CO2 emissions from 
address the challenges posed by AI technologies [47]. To facilitate in reaching landfills, underscoring the significant environmental benefits. 
ternational collaboration and data exchange, researchers suggest Another case study involving Winnow Solutions and IKEA showed that 
harmonizing data formats and establishing cooperative platforms and deploying AI to monitor and analyze food waste in IKEA’s kitchens led to 
databases, which could help mitigate some of these challenges [31,47]. a 30 % reduction in food waste within just one year [59]. These exam
These efforts are crucial for harnessing AI’s potential in improving food ples demonstrate the potential of AI-driven solutions to predict food 
safety and reducing waste effectively. spoilage, optimize inventory management, and foster sustainable prac

tices, significantly mitigating food waste across various settings.
7. Case studies: success stories of AI in reducing food waste

8. AI/machine learning models for food spoilage prediction
The integration of AI technologies in the grocery retail sector rep

resents a pivotal strategy for reducing food waste, enhancing opera Building on the case studies and successful applications of AI in 
tional efficiency, and mitigating environmental impacts [7]. These AI reducing food waste, it is important to explore the underlying machine 
systems utilize sophisticated algorithms to process extensive data learning (ML) AI models that power food spoilage prediction and in
sets—including sales records, historical trends, and external influences ventory management. The deployment of these AI models varies 
like weather patterns and seasonal variations—to accurately predict depending on the nature of the data, the complexity of the environment, 
consumer demand [58]. This capability allows retailers to optimize in and the specific objectives of the food system [60]. Understanding the 
ventory levels and minimize over-ordering, thus reducing the incidence strengths, limitations, and real-world applications of these models is 
of unsold or spoiled products and, consequently, shrinkage and food critical to advancing AI’s role in mitigating food waste.
waste. According to the Pacific Coast Food Waste Commitment [8], the Supervised learning models, such as Random Forest (RF), SVM, and 

6 



H. Onyeaka et al.                                                                                                                                                                     J  o  u r  n  a l  o  f   A  g  r i c u  l t u  r e   a  n d    F  o  o d    R  e  s e  a r  c h 21 (2025) 101895 

Artificial Neural Networks (ANN), play a foundational role in food job displacement also add to the complexity of widespread AI adoption 
spoilage prediction. By learning from historical, labelled data, these in the food sector.
models help predict spoilage patterns based on variables like tempera
ture, humidity, and microbiological conditions. For instance, RF is 9. Future directions and research opportunities in AI for food 
particularly adept at managing heterogeneous datasets, making it a solid spoilage prediction
choice for diverse food products [61]. However, its reliance on large, 
labelled datasets and difficulty with high-dimensional data highlight the Future research in AI and food spoilage prediction is poised to 
challenges that can arise in real-world applications. SVM models, which advance along several integrated and strategic paths to enhance the 
excel at binary classification tasks [62], could be useful for dis effectiveness and application of these technologies:
tinguishing between fresh and spoiled food. They work by finding the Technological advancements: Research efforts should focus on 
optimal hyperplane that separates the two classes, making them suitable improving AI algorithms for better accuracy and reliability in predicting 
for such applications but can be computationally intensive for food spoilage. This involves developing advanced deep-learning models 
large-scale deployments. To address these challenges, researchers have that can process and analyze complex datasets to pinpoint subtle 
explored various strategies to enhance the efficiency of SVMs. For spoilage indicators with greater precision.
instance, a study by Pouladzadeh et al. [63] discusses the use of SVMs in Integration with emerging technologies: Investigating the synergies 
food recognition applications, which is a crucial step in calorie estima between AI and emerging technologies like the IoT and blockchain is 
tion. ANN models, especially deep learning networks, have shown great crucial. IoT sensors offer continuous monitoring of environmental con
promise in detecting subtle spoilage indicators from complex datasets, ditions and food quality parameters, feeding real-time data into AI al
such as hyperspectral imaging data, but come with higher computa gorithms for sharper spoilage predictions [75]. Similarly, blockchain 
tional costs and data requirements [64,65]. technology enhances traceability and transparency within the food 

In contrast, unsupervised learning models, including K-Means Clus supply chain, aiding in the effective tracking of food products and 
tering and Principal Component Analysis (PCA), offer potential in enabling timely interventions to prevent spoilage [68]. This trans
anomaly detection and food spoilage prediction. These models do not parency enables AI systems to process data with greater precision 
require labelled data and can identify outliers in environmental condi tracking variables such as temperature fluctuations, humidity levels, 
tions that may lead to spoilage. K-Means clustering, for example, helps and transit times which are critical to predicting spoilage [75]. By 
segment food products based on spoilage characteristics, facilitating guaranteeing the integrity and availability of data throughout the entire 
better inventory management [66]. However, challenges arise in food supply chain, blockchain facilitates the timely identification of 
handling non-spherical data distributions [67]. PCA, useful for dimen spoilage risks and vulnerabilities. As a result, AI models can generate 
sionality reduction, enhances computational efficiency but may over more reliable predictions and inform decision-making processes that 
look important spoilage indicators when critical features are discarded lead to waste reduction, particularly by minimizing the risk of over
[68]. stocking or mishandling perishable goods [33].

Deep learning models, including CNN and RNN, have revolutionized Multi-modal data fusion: The fusion of diverse data sour
the prediction of food spoilage by analyzing image and time-series data. ces—including sensory, chemical, and microbiological data—into AI 
CNNs are particularly useful for visual quality assessments, such as models can significantly enrich predictive accuracy and offer a deeper 
detecting microbial contamination in fresh produce using hyperspectral understanding of the mechanisms behind food spoilage. This compre
imaging, enabling early detection of spoilage [69]. On the other hand, hensive approach is essential for capturing the full spectrum of factors 
RNNs, particularly LSTM networks, excel in analyzing time-dependent that influence spoilage.
data, such as temperature and humidity trends in cold storage facil Real-time monitoring and adaptive control: Developing AI systems 
ities, predicting spoilage risks with high temporal accuracy [70,71]. equipped with real-time monitoring and adaptive control capabilities 
Despite their advantages, CNNs and RNNs require large, labelled data can enable proactive management of food storage conditions. By 
sets and substantial computational resources, making them more chal leveraging predictive insights, these systems can dynamically adjust 
lenging to implement for smaller-scale operations. variables such as storage environments, packaging materials, and dis

Reinforcement learning (RL) models, such as Deep Q-Networks tribution logistics to minimize waste and maximize food safety and 
(DQN), optimize inventory management by adjusting order patterns quality [33].
based on spoilage risks and demand fluctuations [72,73]. By dynami Collaborative research initiatives: Fostering interdisciplinary col
cally learning the best decision-making strategies, RL can reduce food laborations among food scientists, data scientists, engineers, and in
waste while maximizing profitability. Hybrid approaches, which inte dustry stakeholders will accelerate the pace of innovation in AI 
grate AI models with IoT sensors, provide real-time monitoring and applications for food spoilage prediction. Such collaborative efforts can 
enable adaptive control over food storage conditions. For instance, harness diverse expertise and resources to tackle complex challenges 
combining LSTM with IoT-based temperature sensors significantly en and develop viable, sustainable solutions for managing food waste [76].
hances spoilage prediction accuracy by accounting for real-time envi By focusing on these areas, researchers and industry practitioners 
ronmental changes [74]. However, RL models require significant can significantly advance the capabilities of AI in reducing food waste, 
training time and continuous real-world feedback, presenting challenges with profound implications for both the economy and the environment.
for immediate scalability.

Despite the promising results demonstrated in case studies, the use of 10. Conclusion
AI technologies to reduce food waste is not without its limitations and 
challenges. AI models heavily rely on large, high-quality datasets, which AI has emerged as a transformative force in the battle against food 
may not always be available, especially for smaller businesses with waste and spoilage, unlocking new avenues for enhancing food safety 
limited historical data. The initial costs of implementing AI systems, and sustainability across the global supply chain. By harnessing 
along with ongoing computational and maintenance requirements, can advanced algorithms and real-time data analytics, AI enables the early 
also be prohibitive. Additionally, while these technologies are scalable detection of spoilage, optimizes inventory management, and signifi
for large operations, their complexity and resource demands may make cantly reduces waste through more accurate demand forecasting. The 
them difficult to apply in smaller-scale environments. Furthermore, AI results are not just theoretical; companies like IKEA, Shelf Engine and 
solutions are often dependent on real-time data inputs, such as sensor Afresh have already demonstrated significant reduction in food waste 
readings, which can be vulnerable to inaccuracies or malfunctions. Is per store, directly translating to meaningful environmental impacts, 
sues related to model selection, computational efficiency, and potential including the prevention of thousands of tons of CO2 emissions. These 

7 



H. Onyeaka et al.                                                                                                                                                                     J  o  u r  n  a l  o  f   A  g  r i c u  l t u  r e   a  n d    F  o  o d    R  e  s e  a r  c h 21 (2025) 101895 

underscore AI’s practical applicability and the potential for large-scale References
improvements in food systems.

The unique contribution of this study lies in its demonstration of AI’s [1] F.G. Santeramo, Exploring the link among food loss, waste, and food security: what 

capacity to drive tangible, measurable change across both operational the research should focus on? Agric. Food Secur. 10 (1) (2021) 26, https://doi.org/ 
10.1186/s40066-021-00302-z.

efficiencies and environmental outcomes. The results provide clear ev [2] BMC Medicine, Food insecurity: a neglected public health issue requiring 
idence that AI can revolutionize food waste management, offering so multisectoral action, BMC Med. 21 (2023) 130, https://doi.org/10.1186/s12916- 
lutions that not only reduce waste but also contribute to a more secure 023-02845-3.

[3] World Food Programme, 5 facts about food waste and hunger, Retrieved April 15, 
and sustainable global food supply. The ability to optimize resources, 2024, from, https://www.wfp.org/stories/5-facts-about-food-waste-and-hunger, 
minimize waste, and reduce carbon footprints is essential for meeting 2020.
the world’s growing food demands while mitigating environmental [4] C. Chauhan, A. Dhir, M.U. Akram, J. Salo, Food loss and waste in food supply 

chains: a systematic literature review and framework development approach, 
harm. J. Clean. Prod. 295 (2021) 126438, https://doi.org/10.1016/j. 

To unlock AI’s full potential, however, requires overcoming key jclepro.2021.126438.
challenges, such as data quality, model training, and integration with [5] L. Xue, G. Liu, J. Parfitt, X. Liu, E. Van Herpen, Å. Stenmarck, C. O’Connor, 

K. Östergren, S. Cheng, Missing food, missing data? A critical review of global food 
existing systems. Addressing these obstacles demands a collaborative losses and food waste data, Environ. Sci. Technol. 51 (12) (2017) 6618–6633, 
effort among technologists, researchers, policymakers, and industry https://doi.org/10.1021/acs.est.7b00401.
stakeholders. The integration of AI with complementary technologies [6] L. Bhatia, H. Jha, T. Sarkar, P.K. Sarangi, Food waste utilization for reducing 

carbon footprints towards sustainable and cleaner environment: a review, Int. J. 
like IoT and big data offers additional opportunities to create a smarter, Environ. Res. Publ. Health 20 (3) (2023) 2318, https://doi.org/10.3390/ 
more efficient food system. Future research must focus on overcoming ijerph20032318.
the barriers of data privacy, model biases, and regulatory compliance, [7] F. Ciccullo, M. Fabbri, N. Abdelkafi, M. Pero, Exploring the potential of business 

ensuring that AI’s transformative potential is fully realized. By fostering models for sustainability and big data for food waste reduction, J. Clean. Prod. 340 
(2022) 130673, https://doi.org/10.1016/j.jclepro.2022.130673.

interdisciplinary collaboration and standardizing data protocols, we can [8] Pacific Coast Food Waste Commitment, Using artificial intelligence to reduce food 
build a more sustainable, efficient, and resilient food supply chain that waste in grocery retail progresses on the path to cut food waste in half by 2030, 
benefits both people and the planet for generations to come. Retrieved April 15, 2024, from, https://pacificcoastcollaborative.org/wp-content/ 

uploads/2022/12/PCFWC-Case-Study_AI_Final.pdf, 2024.
[9] C. Martin-Rios, J. Rogenhofer, M.S. Alvarado, The true cost of food waste: tackling 

CRediT authorship contribution statement the managerial challenges of the food supply chain, Trends Food Sci. Technol. 131 
(2023) 190–195, https://doi.org/10.1016/j.tifs.2022.12.005.

[10] J. Parfitt, M. Barthel, S. Macnaughton, Food waste within food supply chains: 
Helen Onyeaka: Writing – review & editing, Writing – original draft, quantification and potential for change to 2050, Phil. Trans. Biol. Sci. 365 (1554) 

Validation, Supervision, Conceptualization. Adenike Akinsemolu: (2010) 3065–3081, https://doi.org/10.1098/rstb.2010.0126.
Writing – review & editing, Writing – original draft. Taghi Miri: Writing [11] V. Lekavičius, V. Bobinaitė, D. Kliaugaitė, K. Rimkūnaitė, Socioeconomic impacts 

of food waste reduction in the European Union, Sustainability 15 (13) (2023) 
– review & editing, Writing – original draft, Supervision. Nnabueze 10151, https://doi.org/10.3390/su151310151.
Darlington Nnaji: Writing – review & editing, Writing – original draft. [12] R. Romanello, V. Veglio, Industry 4.0 in food processing: drivers, challenges and 
Keru Duan: Writing – review & editing, Writing – original draft. Gu outcomes, Br. Food J. 124 (13) (2022) 375–390, https://doi.org/10.1108/BFJ-09- 

2021-1056.
Pang: Writing – review & editing, Writing – original draft. Phemelo [13] Z. Yang, J.H. Lai, J. Zhou, H. Zhou, C. Du, Z. Lai, Agriculture-Vision challenge 
Tamasiga: Writing – review & editing, Writing – original draft. Samran 2022–the runner-up solution for agricultural pattern recognition via transformer- 
Khalid: Writing – review & editing, Writing – original draft. Zainab T. based models, arXiv preprint arXiv:2206.11920 (2022), https://doi.org/10.48550/ 

Al-Sharify: Writing – review & editing, Writing – original draft. Chi arXiv.2206.11920.
[14] A. Kamilaris, F.X. Prenafeta-Boldú, Deep learning in agriculture: a survey, Comput. 

nenye Ugwa: Writing – review & editing, Writing – original draft. Electron. Agric. 147 (2018) 70–90, https://doi.org/10.1016/j. 
compag.2018.02.016.

Ethics approval and consent to participate [15] K.P. Ferentinos, Deep learning models for plant disease detection and diagnosis, 
Comput. Electron. Agric. 145 (2018) 311–318, https://doi.org/10.1016/j. 
compag.2018.01.009.

Not applicable [16] B. Park, AOTF hyperspectral imaging for foodborne pathogen detection, 
Hyperspectral imaging technology in food and agriculture (2015) 359–390, 
https://doi.org/10.1007/978-1-4939-2836-1_15.

Consent for publication [17] P. Pathmanaban, B.K. Gnanavel, S.S. Anandan, S. Sathiyamurthy, Advancing post- 
harvest fruit handling through AI-based thermal imaging: applications, challenges, 

All authors consent to the publication of the article and future trends, Discover Food 3 (1) (2023) 27, https://doi.org/10.1007/ 
s44187-023-00068-2.

[18] H. Afreen, I.S. Bajwa, An IoT-based real-time intelligent monitoring and 
Availability of data and material notification system of cold storage, IEEE Access 9 (2021) 38236–38253, https:// 

doi.org/10.1109/ACCESS.2021.3056672.
[19] F. Siddiqua, S. Rahman, M.T. Dolon, T.F.A. Nayna, M.M. Rashid, M.A. Razzak, IoT- 

Not applicable based low-cost cold storage atmosphere monitoring and controlling system, in: 
2022 International Conference on Wireless Communications Signal Processing and 

Funding Networking (WiSPNET), IEEE, 2022, March, pp. 311–315, https://doi.org/ 
10.1109/WiSPNET54241.2022.9767151.

[20] S.D. Kale, S.C. Patil, Need for predictive data analytics in cold chain management, 
The authors have not received any funding in: Advances in VLSI and Embedded Systems: Select Proceedings of AVES 2019, 

Springer Singapore, Singapore, 2020, pp. 115–129, https://doi.org/10.1007/978- 
Declaration of competing interest 981-15-6229-7_9.

[21] S. Mercier, S. Villeneuve, M. Mondor, I. Uysal, Time–temperature management 
along the food cold chain: a review of recent developments, Compr. Rev. Food Sci. 

All authors declare no competing interests. Food Saf. 16 (4) (2017) 647–667, https://doi.org/10.1111/1541-4337.12269.
[22] N. Hübner, J. Caspers, V.C. Coroamă, M. Finkbeiner, Machine-learning-based 

demand forecasting against food waste: life cycle environmental impacts and 
Data availability benefits of a bakery case study, J. Ind. Ecol. 28 (5) (2024) 1117–1131, https://doi. 

org/10.1111/jiec.13528.
No data was used for the research described in the article. [23] S.B. Dhal, D. Kar, Leveraging artificial intelligence and advanced food processing 

techniques for enhanced food safety, quality, and security: a comprehensive 
review, Discover Applied Sciences 7 (1) (2025) 1–46, https://doi.org/10.1007/ 
s42452-025-06472-w.

[24] C. Qian, S.I. Murphy, R.H. Orsi, M. Wiedmann, How can AI help improve food 
safety? Annu. Rev. Food Sci. Technol. 14 (1) (2023) 517–538, https://doi.org/ 
10.1146/annurev-food-060721-013815.

8 



H. Onyeaka et al.                                                                                                                                                                     J  o  u r  n  a l  o  f   A  g  r i c u  l t u  r e   a  n d    F  o  o d    R  e  s e  a r  c h 21 (2025) 101895 

[25] A. Sadilek, S. Caty, L. DiPrete, R. Mansour, T. Schenk Jr, M. Bergtholdt, principles of AI and ethics in nutrition research, Nutr. Diabetes 12 (1) (2022) 48, 
E. Gabrilovich, Machine-learned epidemiology: real-time detection of foodborne https://doi.org/10.1038/s41387-022-00226-y.
illness at scale, npj Digit. Med. 1 (1) (2018) 36, https://doi.org/10.1038/s41746- [49] D.M. Dooley, E.J. Griffiths, G.S. Gosal, P.L. Buttigieg, R. Hoehndorf, M.C. Lange, W. 
018-0045-1. W. Hsiao, FoodOn: a harmonized food ontology to increase global food 

[26] Q.M. Clark, D.B. Kanavikar, J. Clark, P.J. Donnelly, Exploring the potential of AI- traceability, quality control and data integration, npj Science of Food 2 (1) (2018) 
driven food waste management strategies used in the hospitality industry for 23, https://doi.org/10.1038/s41538-018-0032-6.
application in household settings, Frontiers in Artificial Intelligence 7 (2025) [50] C. Shorten, T.M. Khoshgoftaar, A survey on image data augmentation for deep 
1429477, https://doi.org/10.3389/frai.2024.1429477. learning, Journal of big data 6 (1) (2019) 1–48, https://doi.org/10.1186/s40537- 

[27] M. Tomaszewska, B. Bilska, D. Kołożyn-Krajewska, The influence of selected food 019-0197-0.
safety practices of consumers on food waste due to its spoilage, Int. J. Environ. Res. [51] M.J. Sheller, B. Edwards, G.A. Reina, J. Martin, S. Pati, A. Kotrotsou, S. Bakas, 
Publ. Health 19 (13) (2022) 8144, https://doi.org/10.3390/ijerph19138144. Federated learning in medicine: facilitating multi-institutional collaborations 

[28] V.K. Pandey, S. Srivastava, K.K. Dash, R. Singh, S.A. Mukarram, B. Kovács, without sharing patient data, Sci. Rep. 10 (1) (2020) 12598, https://doi.org/ 
E. Harsányi, Machine learning algorithms and fundamentals as emerging safety 10.1038/s41598-020-69250-1.
tools in the preservation of fruits and vegetables: a review, Processes 11 (6) (2023) [52] N. Mehrabi, F. Morstatter, N. Saxena, K. Lerman, A. Galstyan, A survey on bias and 
1720, https://doi.org/10.3390/pr11061720. fairness in machine learning, ACM Comput. Surv. 54 (6) (2021) 1–35, https://doi. 

[29] F. Tarlak, The use of predictive microbiology for the prediction of the shelf life of org/10.1145/3457607.
food products, Foods 12 (24) (2023) 4461, https://doi.org/10.3390/ [53] C. Qian, Y. Liu, C. Barnett-Neefs, S. Salgia, O. Serbetci, A. Adalja, M. Wiedmann, 
foods12244461. A perspective on data sharing in digital food safety systems, Crit. Rev. Food Sci. 

[30] H. Ding, J. Tian, W. Yu, D.I. Wilson, B.R. Young, X. Cui, W. Li, The application of Nutr. 63 (33) (2023) 12513–12529, https://doi.org/10.1080/ 
artificial intelligence and big data in the food industry, Foods 12 (24) (2023) 4511, 10408398.2022.2103086.
https://doi.org/10.3390/foods12244511. [54] H. Liyanage, P. Krause, S. De Lusignan, Using ontologies to improve semantic 

[31] W.J. Mu, G.A. Kleter, Y. Bouzembrak, E. Dupouy, L.J. Frewer, A.N. Radwan, interoperability in health data, BMJ Health & Care Informatics 22 (2) (2015), 
N. Fadi, H.J.P. Marvin, Making food systems more resilient to food safety risks by https://doi.org/10.14236/jhi.v22i2.159.
including artificial intelligence, big data, and the internet of things in food safety [55] M. Abdallah, M. Salah, Artificial intelligence and intellectual properties: legal and 
early warning and emerging risk identification tools, Compr. Rev. Food Sci. Food ethical considerations, International Journal of Intelligent Systems and 
Saf. 23 (1) (2024) 1–18, https://doi.org/10.1111/1541-4337.13296. Applications in Engineering 12 (1) (2024) 368–376. https://ijisae.org/index.php/ 

[32] B. Miller, How artificial intelligence in food safety will affect food processors, IJISAE/article/view/3911.
SafetyChain (2023). Retrieved April 15, 2024, from, https://blog.safetychain.com/ [56] A. Hassoun, S. Jagtap, H. Trollman, G. Garcia-Garcia, L.N. Duong, P. Saxena, 
ai-in-food-safety. A. Aït-Kaddour, From Food Industry 4.0 to Food Industry 5.0: identifying 

[33] E. Sonwani, U. Bansal, R. Alroobaea, A.M. Baqasah, M. Hedabou, An artificial technological enablers and potential future applications in the food sector, Compr. 
intelligence approach toward food spoilage detection and analysis, Front. Public Rev. Food Sci. Food Saf. 23 (6) (2024) e370040, https://doi.org/10.1111/1541- 
Health 9 (2022) 816226, https://doi.org/10.3389/fpubh.2021.816226. 4337.70040.

[34] H. Onyeaka, P. Tamasiga, U.M. Nwauzoma, T. Miri, U.C. Juliet, O. Nwaiwu, A. [57] N. Jarray, A.B. Abbes, I.R. Farah, Machine learning for food security: current 
A. Akinsemolu, Using artificial intelligence to tackle food waste and enhance the status, challenges, and future perspectives, Artif. Intell. Rev. 56 (Suppl 3) (2023) 
circular economy: maximizing resource efficiency and minimizing environmental 3853–3876, https://doi.org/10.1007/s10462-023-10617-x.
impact: a review, Sustainability 15 (13) (2023) 10482, https://doi.org/10.3390/ [58] N.M. Ifham, M.I.M. Abdulla, M.R.M. Rifadh, M.H. Ajward, N.R.S. Swarnakantha, 
su151310482. K. Rajendran, Machine learning-based approach to reduce food wastage, in: 2023 

[35] M. Rodrigues, V. Migueis, S. Freitas, T. Machado, Machine learning models for 5th International Conference on Advancements in Computing (ICAC), 2023, 
short-term demand forecasting in food catering services: a solution to reduce food December, pp. 119–124, https://doi.org/10.1109/ICAC60630.2023.10417516.
waste, J. Clean. Prod. 435 (2024) 140265, https://doi.org/10.1016/j. [59] CE-Hub, Case study: Winnow solutions, Retrieved April 15, 2024, from 
jclepro.2023.140265. https://ce-hub.org/knowledge-hub/case-study-winnow-solutions/#:~:text=Winn 

[36] H. Anwar, T. Anwar, S. Murtaza, Review on food quality assessment using machine ow%20reports%20that%20employing%20their,in%20around%2095%25%20of% 
learning and electronic nose system, Biosens. Bioelectron. X 100 (2023) 365, 20cases, , 2022.
https://doi.org/10.1016/j.biosx.2023.100365. [60] F. Ciccullo, R. Cagliano, G. Bartezzaghi, A. Perego, Implementing the circular 

[37] X. Deng, S. Cao, A.L. Horn, Emerging applications of machine learning in food economy paradigm in the agri-food supply chain: the role of food waste prevention 
safety, Annu. Rev. Food Sci. Technol. 12 (2021) 513–538, https://doi.org/ technologies, Resour. Conserv. Recycl. 164 (2021) 105114, https://doi.org/ 
10.1146/annurev-food-071720-024112. 10.1016/j.resconrec.2020.105114.

[38] X. Wang, Y. Bouzembrak, A.O. Lansink, H.J. van der Fels-Klerx, Application of [61] S. Wager, S. Athey, Estimation and inference of heterogeneous treatment effects 
machine learning to the monitoring and prediction of food safety: a review, Compr. using random forests, J. Am. Stat. Assoc. 113 (523) (2018) 1228–1242, https://doi. 
Rev. Food Sci. Food Saf. 21 (1) (2022) 416–434, https://doi.org/10.1111/1541- org/10.1080/01621459.2017.1319839.
4337.12868. [62] W. Dudzik, J. Nalepa, M. Kawulok, Evolving data-adaptive support vector 

[39] A. Voulodimos, N. Doulamis, A. Doulamis, E. Protopapadakis, Deep learning for machines for binary classification, Knowl. Base Syst. 227 (2021) 107221, https:// 
computer vision: a brief review. Computational Intelligence and Neuroscience, doi.org/10.1016/j.knosys.2021.107221.
2018, https://doi.org/10.1155/2018/7068349. Advance online publication. [63] P. Pouladzadeh, S. Shirmohammadi, A. Bakirov, A. Bulut, A. Yassine, Cloud-based 

[40] H.T. Gorji, M. Saeedi, E. Mushtaq, H.K. Zadeh, K. Husarik, S.M. Shahabi, J.W. Qin, SVM for food categorization, Multimed. Tool. Appl. 74 (2015) 5243–5260, https:// 
et al., Federated learning for clients’ data privacy assurance in the food service doi.org/10.1007/s11042-014-2116-x.
industry, Appl. Sci. 13 (16) (2023) 9330, https://doi.org/10.3390/app13169330. [64] N. Gul, K. Muzaffar, S.Z.A. Shah, A. Assad, H.A. Makroo, B.N. Dar, Deep learning 

[41] K.A. Houser, J.W. Bagby, The data trust solution to data sharing problems, hyperspectral imaging: a rapid and reliable alternative to conventional techniques 
Vanderbilt Journal of Entertainment and Technology Law 25 (2023) 113. https in the testing of food quality and safety, Qual. Assur. Saf. Crop Foods 16 (1) (2024) 
://heinonline.org/HOL/Print?collection=journals&handle=hein.journals/vanep 78–97, https://doi.org/10.15586/qas.v16i1.1392.
25&id=123&email=1. [65] Z. Kang, Y. Zhao, L. Chen, Y. Guo, Q. Mu, S. Wang, Advances in machine learning 

[42] G.S. Ruben, S. Emilio, B. Javier, Mitigating bias in artificial intelligence: fair data and hyperspectral imaging in the food supply chain, Food Eng. Rev. 14 (4) (2022) 
generation via causal models for transparent and explainable decision-making, 596–616, https://doi.org/10.1007/s12393-022-09322-2.
Future Gener. Comput. Syst. 155 (2024) 384–401, https://doi.org/10.1016/j. [66] R.K. Megalingam, G.S. Sree, G.M. Reddy, I.R.S. Krishna, L.U. Suriya, Food spoilage 
future.2024.02.023. detection using convolutional neural networks and K means clustering, in: 2019 

[43] K. Supriya, Reducing racial bias in AI models for clinical use requires a top-down 3rd International Conference on Recent Developments in Control, Automation and 
intervention, Nat. Mach. Intell. 3 (6) (2021) 460, https://doi.org/10.1038/s42256- Power Engineering (RDCAPE), IEEE, 2019, October, pp. 488–493, https://doi.org/ 
021-00362-7. 10.1109/RDCAPE47089.2019.8979114.

[44] D. Patel, C.K. Sahu, R. Rai, Security in modern manufacturing systems: integrating [67] H. He, Y. He, F. Wang, W. Zhu, Improved K-means algorithm for clustering non- 
blockchain in artificial intelligence-assisted manufacturing, Int. J. Prod. Res. 62 (3) spherical data, Expert Syst. 39 (9) (2022) e13062, https://doi.org/10.1111/ 
(2024) 1041–1071, https://doi.org/10.1080/00207543.2023.2262050. exsy.13062.

[45] R.G. Richey Jr., S. Chowdhury, B. Davis-Sramek, M. Giannakis, Y.K. Dwivedi, [68] K. Duan, H. Onyeaka, G. Pang, Pioneering food safety: blockchain’s integration in 
Artificial intelligence in logistics and supply chain management: a primer and supply chain surveillance, Journal of Agricultural and Food Research 18 (2024) 
roadmap for research, J. Bus. Logist. 44 (4) (2023) 532–549, https://doi.org/ 101281, https://doi.org/10.1016/j.jafr.2024.101281.
10.1111/jbl.12364. [69] A. Soni, Y. Dixit, M.M. Reis, G. Brightwell, Hyperspectral imaging and machine 

[46] A. Rejeb, K. Rejeb, S. Zailani, J.G. Keogh, A. Appolloni, Examining the interplay learning in food microbiology: developments and challenges in detection of 
between artificial intelligence and the agri-food industry, Artificial Intelligence in bacterial, fungal, and viral contaminants, Compr. Rev. Food Sci. Food Saf. 21 (4) 
Agriculture 6 (2022) 111–128, https://doi.org/10.1016/j.aiia.2022.08.002. (2022) 3717–3745, https://doi.org/10.1111/1541-4337.12983.

[47] S. Thakkar, W. Slikker, F. Yiannas, P. Silva, B. Blais, K.R. Ching, Z. Liu, [70] J. Guo, D. Liu, S. Lin, J. Lin, W. Zhen, Temperature prediction of a temperature- 
A. Adholeya, F. Pappalardo, M. da Luz Carvalho Soares, P.E. Beeler, Artificial controlled container with cold energy storage system based on long short-term 
intelligence and real-world data for drug and food safety: a regulatory science memory neural network, Appl. Sci. 14 (2) (2024) 854, https://doi.org/10.3390/ 
perspective, Regul. Toxicol. Pharmacol. 140 (2023) 105388, https://doi.org/ app14020854.
10.1016/j.yrtph.2023.105388. [71] J. Machacuay, J. Manrique-Silupu, W. Ipanaqué, LSTM with shallow NNs for 

[48] D.M. Thomas, S. Kleinberg, A. Brown, M. Crow, N.D. Bastian, N. Reisweber, indoor temperature long-term predictions in refrigeration systems, Neural Comput. 
R. Lasater, T. Kendall, Machine learning modeling practices to support the Appl. (2024) 1–22, https://doi.org/10.1007/s00521-024-10477-8.

9 



H. Onyeaka et al.                                                                                                                                                                     J  o  u r  n  a l  o  f   A  g  r i c u  l t u  r e   a  n d    F  o  o d    R  e  s e  a r  c h 21 (2025) 101895 

[72] S. Jullien, M. Ariannezhad, P. Groth, M. de Rijke, A simulation environment and [75] K. Pachiappan, K. Anitha, R. Pitchai, S. Sangeetha, T.V.V. Satyanarayana, 
reinforcement learning method for waste reduction, arXiv preprint arXiv: S. Boopathi, Intelligent machines, IoT, and AI in revolutionizing agriculture for 
2205.15455 (2022), https://doi.org/10.48550/arXiv.2205.15455. water processing, in: Handbook of Research on AI and ML for Intelligent Machines 

[73] M. Selukar, P. Jain, T. Kumar, Inventory control of multiple perishable goods using and Systems, IGI Global, 2024, pp. 374–399, https://doi.org/10.4018/978-1-6684- 
deep reinforcement learning for sustainable environment, Sustain. Energy Technol. 9999-3.ch015.
Assessments 52 (2022) 102038, https://doi.org/10.1016/j.seta.2022.102038. [76] F. Batool, T.A. Kurniawan, A. Mohyuddin, M.H.D. Othman, F. Aziz, H. Al-Hazmi, 

[74] B.A.O. Ikram, B.A. Abdelhakim, A. Abdelali, B. Zafar, B. Mohammed, Deep H.H. Goh, A. Anouzla, Environmental impacts of food waste management 
Learning architecture for temperature forecasting in an IoT LoRa based system, in: technologies: a critical review of life cycle assessment (LCA) studies. Trends in 
Proceedings of the 2nd International Conference on Networking, Information Food Science & Technology, Advanced online publication, 2024, https://doi.org/ 
Systems and Security, 2019, March, pp. 1–6, https://doi.org/10.1145/ 10.1016/j.tifs.2023.104287.
3320326.3320375.

10 

View publication stats