---
source_file: "2025-Customer-centric circular economy as-a-service decision-making Machine learning-driven open innovation in food service.txt"
original_rel_path: "Trabalhos\Artigos\Apoio pontual\txt\2025-Customer-centric circular economy as-a-service decision-making Machine learning-driven open innovation in food service.txt"
category: "Artigos_Apoio_pontual"
extension: ".txt"
sha256: "2ed7d85863ee9faeacf6c5b5d3322d57201e48649bc5d80d0aa3b3876db119cb"
extracted_at: "2026-09-20T00:05:05.677499"
---

﻿Cleaner Environmental Systems 18 (2025) 100302 

Contents lists available at ScienceDirect

Cleaner Environmental Systems
journal homepage: www.journals.elsevier.com/cleaner-environmental-systems

Customer-centric circular economy as-a-service decision-making: Machine 
learning-driven open innovation in food service
Tutur Wicaksono a , Marhadi Marhadi b,c,* , Agustinus Fritz Wijaya d , Velly Anatasia e ,  
Krisztina Taralik f

a School of Business and Management, Universitas Ciputra, Indonesia
b Doctoral School of Economic and Regional Sciences, Hungarian University of Agriculture and Life Sciences, Hungary
c Department of Management, Faculty of Business and Economics, Universitas Riau, Indonesia
d Department of Informatics, Faculty of Technology and Design, Universitas Bunda Mulia, Jakarta, Indonesia
e Department of Management, Faculty of Social Sciences and Humanities, Universitas Bunda Mulia, Jakarta, Indonesia
f Department of Agricultural logistic, Commerce, Marketing, Hungarian University of Agriculture and Life Sciences, Hungary

A R T I C L E  I N F O A B S T R A C T

Keywords: This study addresses a key research gap by developing a machine learning-driven open innovation framework for 
Customer satisfaction prioritizing Circular Economy as a Service (CEaaS) measures in the food service sector. Conventional sustain
Sustainability practices ability strategies often fail to integrate dynamic customer preferences with scalable circular economy practices. 
Feature selection To bridge this gap, this research employs Random Forest classification and feature selection to assess the impact 
Waste reduction

of sixteen CEaaS measures on customer satisfaction across Indonesian and Hungarian food service markets. The 
framework is grounded in PRISMA-guided literature review, customer surveys, and machine learning-based 
decision analytics. Sustainable sourcing, reusable packaging systems, and circular loyalty programs emerge as 
the most critical CEaaS measures, reflecting global consumer priorities for ethical procurement, waste minimi
zation, and behavior-based engagement. Notably, surplus food redistribution and food waste upcycling services 
rank consistently high, underscoring growing expectations for visible circularity and social value. The cross- 
country model validation confirms the framework’s robustness and generalizability. By integrating circular 
economy principles, customer insights, and machine learning, the study advances open innovation theory and 
provides actionable guidance for sustainable transformation in the food service sector. The findings support 
Sustainable Development Goals related to responsible consumption, climate action, industry innovation, and 
global partnerships.

1. Introduction growing awareness, the transition to circularity remains fraught with 
challenges, as businesses struggle to align operational sustainability 

The global food service industry plays a vital role in modern econ with customer expectations, leading to a gap between their commitment 
omies, driving employment, economic growth, and cultural exchange to circularity and its actual implementation (Dorrego-Viera et al., 2025). 
(Recuero-Virto and Arróspide, 2024). However, this sector faces a crit Addressing these challenges is essential not only for the industry but also 
ical contradiction, as it is a leading contributor to environmental for global sustainability. In line with the United Nations Sustainable 
degradation, generating escalating waste, greenhouse gas emissions, Development Goals, particularly SDG 12 (Responsible Consumption and 
and resource depletion (Zhang et al., 2021). As the urgency to address Production), SDG 13 (Climate Action), SDG 9 (Industry, Innovation, and 
environmental sustainability intensifies, food service businesses face Infrastructure), and SDG 17 (Partnerships for the Goals), this research 
mounting pressure to adopt circular economy (CE) principles. These aims to develop strategies that support both environmental re
principles focus on creating closed-loop systems by reducing waste, sponsibility and long-term economic growth (Azmat et al., 2023).
reusing resources, and recycling (Kurniawan et al., 2024). Despite The concept of Circular Economy as a Service (CEaaS) has emerged 

* Corresponding author. Doctoral School of Economic and Regional Sciences, Hungarian University of Agriculture and Life Sciences, Hungary.
E-mail addresses: tutur.wicaksono@ciputra.ac.id (T. Wicaksono), marhadi.marhadi-@phd.uni-mate.hu, marhadi@lecturer.unri.ac.id (M. Marhadi), agustinus. 

wijaya@bundamulia.ac.id (A.F. Wijaya), vanatasia@bundamulia.ac.id (V. Anatasia), taralik.krisztina@uni-mate.hu (K. Taralik). 

https://doi.org/10.1016/j.cesys.2025.100302
Received 12 March 2025; Received in revised form 4 July 2025; Accepted 19 July 2025  
Available online 22 July 2025 
2666-7894/© 2025 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ ). 



T. Wicaksono et al.                                                                                                                                                                                  C  l e a  n  e r   E  n v  i r o  n  m  e  n  t a l  S  y  s t e  m  s 18 (2025) 100302 

as a promising solution, enabling businesses to adopt circular practices driven open innovation framework for constructing CEaaS in food ser
without significant upfront investments (Greer et al., 2020). The CEaaS vices. The research aims to answer the following questions: 
framework offers access to circular solutions such as waste reduction 
technologies, reusable packaging systems, and resource recovery ser RQ 1: How can machine learning models be integrated into an open 
vices, which are made available through subscription or pay-per-use innovation approach to develop a customer-centric Circular Econ
models (Da Silva et al., 2024). However, the successful implementa omy as a Service (CEaaS) framework in food services?
tion of CEaaS in food services requires a deep understanding of customer RQ 2: What are the prioritized CEaaS measures that best align with 
needs and preferences, as well as the ability to prioritize measures that customer satisfaction in food services?
deliver both environmental and economic value (Rakesh and Mahen
dran, 2023). This challenge underscores the importance of open inno To answer this question, the study pursues the following objectives: 
vation, a collaborative approach that leverages external insights, 
particularly from customers, to drive innovation and sustainability (Yun 1. Develop an integrated framework combining open innovation and 
et al., 2023, 2025). machine learning for customer-centric CEaaS solutions.

Integrating customer insights into the design and prioritization of 2. Identify potential CEaaS measures for food service providers through 
CEaaS measures is essential for ensuring market relevance and adoption a systematic literature review using the PRISMA framework.
(Ekman et al., 2020). For example, while reusable packaging systems 3. Utilize Random Forest classifier to customer survey data to assess 
may appeal to environmentally conscious consumers, they may face and validate the performance of the proposed framework.
resistance from those who prioritize convenience or cost-effectiveness 4. Utilize Random Forest-based feature selection on customer survey 
(Rabiu and Jaeger-Erben, 2023). This reflects the complexity of data to rank the priority CEaaS measures according to their signifi
decision-making in CEaaS implementation, which requires balancing cance on customer satisfaction level.
multiple criteria such as sustainability, customer satisfaction, and 
profitability (Adelodun et al., 2021). Traditional methods, such as By integrating circular economy principles, open innovation, and 
multi-criteria decision analysis (MCDA), often struggle to address the machine learning, this research provides a robust foundation for 
dynamic and multifaceted nature of customer preferences, especially advancing sustainability in the food service industry. The proposed 
when working with large and complex datasets (Beinabadi et al., 2024). framework not only addresses environmental challenges but also en

The advancement of big data and machine learning techniques offers hances customer satisfaction and business competitiveness in a 
new opportunities to overcome these challenges. Algorithms like sustainability-driven market. The remainder of this paper is organized as 
Random Forest (RF) are particularly suited for analyzing large datasets, follows. Section 2 reviews the relevant literature on circular economy as 
uncovering patterns and relationships that may be overlooked by con a service in the food service industry, open innovation in circular 
ventional methods (Mahboubi et al., 2024; Pritee et al., 2024). RF economy, and machine learning for circular economy decision-making. 
supports both feature selection and classification, allowing researchers Section 3 outlines the research methodology, detailing the use of the 
to identify and prioritize the most impactful CEaaS measures based on PRISMA Framework, Random Forest Classifier, and Random Forest 
their importance scores (Rabiee et al., 2024). By applying RF, businesses feature selection. Section 4 presents the results and discussion, while 
can streamline CEaaS development by focusing on measures aligned Section 5 discusses the conclusions and their implications for theory and 
with customer priorities while enhancing sustainability outcomes practice. Finally, Section 6 concludes by summarizing the contributions 
(Temizceri and Kara, 2024). and suggesting directions for future research.

Although there is growing interest in circular economy and machine 
learning, few studies have examined how these concepts intersect within 2. Literature review
the CEaaS context in food service. Existing research tends to focus on 
specific areas such as waste reduction, resource optimization, or supply 2.1. Circular economy as a service: concept and application in the food 
chain efficiency, rather than a service-based circular economy frame service industry
work (Damiani et al., 2021). Moreover, conventional approaches remain 
dominant and often overlook the potential of machine learning to sup The circular economy (CE) represents a transformative shift from the 
port scalable and adaptive circular economy solutions. traditional linear “take-make-dispose” paradigm to a regenerative sys

Recent developments in predictive analytics, IoT-enabled smart tem that emphasizes resource efficiency, waste minimization, and sys
systems, and AI-based decision tools provide promising means to temic resilience (Geissdoerfer et al., 2016; Hussain et al., 2023). This 
advance circularity in food services (Lakhouit, 2025). However, limited fundamental change is especially significant for the food service in
research has explored how machine learning can be integrated into dustry, which contributes substantially to greenhouse gas emissions and 
service-oriented frameworks to enable closed-loop systems, reduce food food waste (Carino et al., 2020). By embracing the principles of 
waste, and improve sustainability. Similarly, the role of open innovation reducing, reusing, recycling, and regenerating, CE provides a structured 
in co-developing CEaaS models with customers remains insufficiently framework for addressing environmental challenges through 
studied, especially in the food service context (Fang et al., 2024; Dantas closed-loop systems that optimize resource utilization (Acerbi and 
et al., 2022). Taisch, 2020). Building on these principles, Circular Economy as a 

Indonesia and Hungary were selected to represent two distinct eco Service (CEaaS) extends traditional CE approaches by incorporating 
nomic and regulatory contexts. Indonesia is an emerging economy in servitization. Unlike conventional business models that rely primarily 
Southeast Asia with a large informal food service sector, while Hungary on product sales, CEaaS focuses on performance-based services where 
is a developed economy operating within the structured regulatory revenue is directly tied to service outcomes (Patwa et al., 2020). This 
environment of the European Union. Both countries face similar chal shift embeds long-term resource optimization and waste minimization 
lenges in circular economy adoption in food services, including food into daily operations, enhancing both sustainability and economic effi
waste, resource inefficiency, and limited CE integration (Pribadi et al., ciency (Kanda et al., 2024).
2025; Sanjuan-Delmás et al., 2021). However, their contrasting levels of Numerous studies have demonstrated the effectiveness of CEaaS in 
economic development, digital readiness, and policy enforcement create reducing waste and improving operational efficiency in food-related 
a valuable setting for testing the robustness and relevance of CEaaS industries. For example, reusable container systems have significantly 
prioritization. This combination supports a comparative analysis and cut costs by optimizing inventory management, reducing the frequency 
enhances the international applicability of the findings. of supplier visits, and minimizing associated expenses (Becker et al., 

This study addresses these gaps by proposing a machine learning- 2023). Similarly, integrating microalgae cultivation with anaerobic 

2 



T. Wicaksono et al.                                                                                                                                                                                  C  l e a  n  e r   E  n v  i r o  n  m  e  n  t a l  S  y  s t e  m  s 18 (2025) 100302 

digestion has transformed food waste into biogas, electricity, and bio bridges the gap between environmental imperatives and market realities 
diesel, while recycling digestate effluent for microalgae growth and in the food service industry (Leitão et al., 2020). Grounded in the theory 
fertilizer production establishes a holistic energy and waste manage that firms must leverage external knowledge and partnerships to 
ment framework (Ro et al., 2024). Furthermore, CE strategies are accelerate innovation (Chesbrough, 2019; Yun et al., 2024), open 
essential for addressing the water-food-energy nexus by enhancing innovation offers a critical framework for addressing the systemic 
water recovery and reducing waste (Samberger, 2022). Varjani et al. complexity of circular economy transitions (Srisathan et al., 2023). 
(2023) further emphasize the use of contemporary technologies, such as Unlike traditional closed innovation approaches that rely solely on in
metagenomics and AI-driven solutions, to optimize resource utilization, ternal research and development and often yield misaligned sustain
enhance food waste valorization, and mitigate environmental impacts ability solutions, open innovation fosters co-creation by integrating 
from plastic pollution and traditional waste disposal. diverse stakeholders, including customers, into the innovation process 

Digital platforms also play a crucial role in enabling CEaaS in the (Tsai et al., 2022). This approach aligns with the multi-level perspective 
food service industry. Platforms like Too Good To Go (TGTG) connect of socio-technical transitions, which considers the interplay between 
businesses with surplus food and consumers across more than 17 niche innovations (such as CEaaS), established industry norms, and 
countries, simultaneously reducing food waste and alleviating food broader sustainability pressures (Liu and Stephens, 2019). By involving 
insecurity (Magno and Cassia, 2024; Too Good To Go, 2023). The suc external stakeholders in the design of CEaaS, businesses can better 
cess of these technology-driven solutions depends on effective collabo navigate these interdependencies and align technical feasibility with 
ration among policymakers, businesses, and consumers, as well as consumer expectations (Johnson, 2022).
supportive regulatory frameworks and active stakeholder engagement. The theoretical underpinnings of open innovation in circular econ

Regulatory frameworks facilitate the adoption of CE practices. omy are further enriched by the resource-based view and stakeholder 
Global initiatives, such as the European Union’s Circular Economy Ac theory. The resource-based view argues that competitive advantage 
tion Plan, have set ambitious waste reduction targets (European Com stems from unique, valuable resources, which in circular economy as a 
mission, 2020; Moschen-Schimek et al., 2023), while Southeast Asia’s service contexts include external expertise such as waste management 
Framework for Circular Economy for the ASEAN Economic Community innovators and customer insights (Csedő et al., 2023). Stakeholder 
(AEC) reflects a regional commitment to resource efficiency (ASEAN, theory asserts that firms must address the needs of all stakeholders, 
2021; Herrador and Van, 2023). However, fragmented policies and including customers, regulators, and communities, to achieve long-term 
varying enforcement levels continue to hinder implementation. Chal sustainability (Durmaz et al., 2021). Together, these theories justify the 
lenges such as inconsistent date labeling, variable donation incentives, need for open innovation in circular economy as a service, as external 
and uneven landfill mandates discourage stakeholder collaboration and collaboration becomes a strategic resource that balances competing 
call for harmonized policies and standardized incentives (Ryen and stakeholder interests to deliver solutions that are both environmentally 
Babbitt, 2022). effective and market relevant (Eisenreich et al., 2022).

Behavioral barriers also complicate the transition to CE in the food A practical example of open innovation in food services is the 
service industry. Consumers often exhibit a “single-use bias” by priori collaboration between restaurants and local farming communities to 
tizing convenience over sustainability, even as awareness of environ establish a zero-waste supply chain. In this approach, restaurants rede
mental consequences grows (Rabiu and Jaeger-Erben, 2023). In parallel, sign procurement processes by repurposing surplus ingredients, replac
small and medium enterprises (SMEs) frequently face financial con ing single-use packaging, and co-developing sustainable menu options 
straints that limit investments in Circular Economy technologies due to based on customer feedback. Tasting events and workshops further 
high upfront costs (Worakittikul et al., 2025). These challenges suggest ensure that these offerings align with consumer preferences while 
the need for hybrid framework that combine regulatory incentives with maintaining convenience and culinary appeal (Camilleri, 2024). This 
behavioral interventions. For instance, tax breaks for zero-waste certi integration of circular economy principles into both operations and 
fications and consumer education initiatives, such as carbon footprint customer engagement demonstrates value co-creation through iterative 
labeling, can encourage sustainable purchasing decisions (Huang et al., producer-consumer collaboration (John and Supramaniam, 2023).
2024). Regulatory measures that limit disposable materials can also shift At the core of CEaaS driven by open innovation is customer- 
consumption patterns (Borg et al., 2022). For example, replacing ten centricity, which redefines end-users as co-designers of circular solu
percent of disposable materials with reusable alternatives may prevent tions (Gajdzik et al., 2024). This perspective aligns with design thinking 
most waste from causing environmental damage, particularly in marine methodologies that emphasize empathy, ideation, and prototyping in 
ecosystems (WEF, 2021). These points underscore the importance of addressing complex sustainability challenges (Imjai et al., 2024). For 
targeted policy frameworks in driving both consumer and business example, the divergence between environmentally conscious users who 
engagement in circular economy practices. favor reusable packaging and time-constrained segments that prefer 

Finally, scaling CE in the food service industry requires redefining single-use options highlights the need for open innovation to reconcile 
value chains through sustainable sourcing, transparent supply chains, conflicting priorities (Sandhu et al., 2020). By integrating customer in
and technological innovations (Al-Obadi et al., 2022). Farm-to-table sights, businesses can develop segmented CEaaS offerings tailored to 
networks that prioritize local sourcing help reduce transportation diverse needs, thereby increasing adoption rates (Bocken and Konietzko, 
emissions and minimize food spoilage, thereby reinforcing CE principles 2022).
at multiple stages of the supply chain (Camilleri, 2024). In addition, Despite its promise, implementing open innovation in CEaaS faces 
blockchain-enabled traceability systems enhance transparency and significant challenges. Transaction cost theory explains that firms may 
accountability in sustainable sourcing while reducing inefficiencies in resist external collaboration due to perceived risks such as intellectual 
circular supply chains (Mothafar et al., 2024). Despite operational property infringement and coordination costs (Audretsch and Belitski, 
challenges in an industry marked by low-profit margins and cost sensi 2022). Moreover, behavioral inertia in both organizational routines and 
tivity (Qahtan et al., 2024), the transformative potential of CE in food consumer habits often impedes the adoption of circular practices. 
services is significant if businesses, policymakers, and consumers Kanwal et al. (2024) note that ingrained consumption and disposal be
collectively embrace sustainability. haviors, reinforced by cultural norms surrounding food waste, hinder 

sustainable waste management despite the potential benefits of upcy
2.2. Open innovation in circular economy: co-creation and customer- cling and advanced reduction technologies. Similarly, Möslinger et al. 
centric solution (2023) observe that food service systems rarely adopt industrial sym

biosis and wastewater reuse, with future strategies likely to focus more 
Open innovation has emerged as a transformative paradigm that on circular business models, sustainable materials, and waste 

3 



T. Wicaksono et al.                                                                                                                                                                                  C  l e a  n  e r   E  n v  i r o  n  m  e  n  t a l  S  y  s t e  m  s 18 (2025) 100302 

prevention. CEaaS. By integrating these datasets, machine learning models can 
develop adaptive decision-making frameworks that enable real-time 

2.3. Machine learning for circular economy decision-making monitoring and adjustments. For example, IoT-enabled systems com
bined with machine learning algorithms allow for real-time tracking of 

Machine learning is revolutionizing decision-making in the circular resource consumption, optimization of energy and water usage, and 
economy, particularly in the food service sector (Kanwal et al., 2024). By waste minimization (Javaid et al., 2022). In addition, predictive ana
leveraging advanced data analytics, Machine learning transcends lytics models that forecast food waste patterns can further inform in
traditional linear fameworks and offers an adaptive framework to bal ventory management and support waste reduction efforts (Zatsu et al., 
ance environmental impact, economic feasibility, and consumer pref 2024).
erences (López-Guajardo et al., 2021). This capability is essential in 
industries facing resource constraints and rapidly changing market 3. Methodology
conditions, where both operational flexibility and long-term sustain
ability are crucial (Behera et al., 2023). This research proposes a framework to identify and prioritize Cir

The theoretical basis for applying machine learning in CE decision- cular Economy as a Service (CEaaS) measures in the food service in
making is grounded in complexity theory and systems thinking. dustry, with customer satisfaction level as the target variable. The 
Complexity theory posits that sustainability challenges, such as waste methodology begins with data collection through a systematic literature 
reduction and resource optimization, are inherently complex and review conducted under the PRISMA (Preferred Reporting Items for 
nonlinear, necessitating adaptive and iterative solutions (Tetteh et al., Systematic Reviews and Meta-Analyses) framework to ensure a rigorous 
2024). Among various machine learning algorithms, Random Forest is and transparent selection process (Ly et al., 2024). Literature was 
particularly well suited for processing large multidimensional datasets, sourced from the Scopus and Web of Science databases using the search 
identifying intricate nonlinear relationships, and performing effective query ALL (“Circular economy” “food service”). Articles addressing 
feature selection (Murthy et al., 2024; Xuan et al., 2021). These capa general sustainability practices were excluded, retaining only those 
bilities enable businesses to prioritize sustainability measures more focused specifically on CEaaS measures within the food service sector. 
accurately, as demonstrated in predictive food waste analytics (Tsui During the screening phase, conference papers, book chapters, and 
et al., 2022) and inventory optimization (Kanwal et al., 2024). non-academic publications were discarded due to quality concerns. 

Decision theory further supports the application of machine learning After reviewing abstracts, introductions, results, and conclusions, 130 
by providing a structured framework for evaluating multiple alterna articles were excluded, leaving 14 core articles that formed the foun
tives under uncertainty (Albahri et al., 2023). Ensemble methods, such dation for identifying potential CEaaS measures (see Fig. 1).
as those employed in Random Forest, aggregate multiple decision trees Following the literature review, a customer survey was conducted to 
to reduce variance and mitigate overfitting, resulting in more reliable collect data on the perceived importance of each CEaaS measure and its 
predictor importance scores (Devasahayam and Albijanic, 2023). This impact on customer satisfaction. The survey consisted of three sections. 
methodological rigor is especially valuable for integrating machine The first section collected demographic and behavioral information, 
learning into CEaaS framework, where it enhances operational strate including age, gender, experience, education level, occupation, and 
gies and aligns business practices with evolving market demands and purchasing frequency. The second section asked respondents to rate the 
regulatory requirements (Danish and Senjyu, 2023). importance of each CEaaS measure on a five-point Likert scale ranging 

Furthermore, systems theory emphasizes the interdependence of from 1 (Not Important at All) to 5 (Extremely Important) in relation to 
diverse data sources, including customer surveys, operational records, their satisfaction during the purchasing process. The third section asked 
and market trends, in the practical application of machine learning in respondents to evaluate how the implementation of each measure would 

Fig. 1. Sistematic literature review through PRISMA framework.

4 



T. Wicaksono et al.                                                                                                                                                                                  C  l e a  n  e r   E  n v  i r o  n  m  e  n  t a l  S  y  s t e  m  s 18 (2025) 100302 

influence their overall satisfaction, using the same scale. diction is the mode of all individual tree predictions: 
The food service industry in Indonesia is largely dual-structured, 

with a dominant informal sector composed of street vendors and ŷ =mode(T1(x),T2(x),…,Tntree (x)) (2) 
small-scale eateries, alongside a rapidly growing formal sector driven by 
urbanization and digital platforms. Regulatory enforcement and sus Step 4: Out-of-Bag (OOB) Error Calculation
tainability integration are limited, particularly outside major urban 
centers. In contrast, Hungary’s food service sector is predominantly The OOB error is calculated to evaluate the model performance 
formal, characterized by chain restaurants and institutional providers, without using a separate validation set. Each data point is tested on the 
and governed by strict European Union regulations related to sustain decision trees for which it was not included in the bootstrap sample, and 
ability and waste management. These structural differences offer a the OOB error is computed as: 
meaningful comparative context for analyzing CEaaS adoption and 

1 ∑nOOB
prioritization across diverse regulatory and socio-economic OOBerror = I(y ŷ ) ( )

n i∕= i 3  
environments. OOB i=1

A total of 1428 responses were collected, consisting of 820 from 
Indonesia and 608 from Hungary. The survey was conducted using a where is I the indicator function that returns 1 if the observation is 
hybrid approach. Most respondents completed a self-administered on misclassified.
line questionnaire via Google Forms, accessed through a QR code or Next, Random Forest feature selection evaluates the importance of 
barcode, while a smaller portion were invited via email and social media each CEaaS measure based on its impact on model error. Importance 
groups. Target participants were individuals who had recently used food scores are determined by measuring the increase in error when a feature 
service establishments such as restaurants, food stalls, or cafés. A pur is permuted (Dunne et al., 2023). Measures causing the highest error 
posive sampling method was employed, with inclusion criteria requiring increase are ranked as the most influential and prioritized accordingly. 
participants to have made a food service purchase within the past 30 The steps are as follows: 
days. Participation was voluntary and anonymous, and informed con
sent was obtained prior to the start of the survey. Rather than enabling a Step 1: Tree construction
direct comparison, the cross-country approach enhances the generaliz
ability of findings and supports industry-wide recommendations for A set of K decision trees is constructed using the original dataset (X,
sustainable practices. Y)

Given the dataset’s size, machine learning algorithms were selected 
for their efficiency and accuracy in handling large-scale data, compared Step 2: Calculate OOB error
to traditional methods. The second stage involved data preparation, 
including cleaning and splitting. The dataset was processed to remove For each tree i in the forest, calculate the out-of-bag (OOB) error 
missing values and saved in CSV format. Independent variables (CEaaS using the unmodified OOB dataset, denoted as ErrorOOB(i). This pro
measures) were separated from the dependent variable (customer vides a baseline measure of error for each decision tree in the forest. 
satisfaction level). The methodology further employs two machine 
learning techniques: the Random Forest classifier and Random Forest- Step 3: Permutation importance
based feature selection. The Random Forest classifier aggregates pre
dictions from multiple decision trees through majority voting (Sun et al., Each feature’s importance is calculated by randomly permuting its 
2023). The process is outlined in the following steps: values in the OOB dataset and computing the error difference. The 

importance score for each feature IXj is defined as: 
Step 1: Boostraping and data sampling

1 ∑ntree ( )
IXj = ErrorOOB(i)

n j − ErrorOOB(i) (4) 
The step begins by generating ntree bootstrap samples from the tree i=1

original dataset. Let X= {x1, x2,…, xd} represent the set of independent 
{ } The performance of the Random Forest classifier model is evaluated 

variables (CEaaS measures), and Y = y1, y2,…, yd represent the cor using accuracy and F-score metrics to ensure reliability and validity. 
responding target variable (set of customer satisfaction level responses). Accuracy measures the proportion of correct predictions, while the F- 
In bootstrapping, each new sample (Xc,Yc) is created by random sam score balances precision and recall, assessing the model’s effectiveness 
pling with replacement from (X,Y), resulting in new datasets for each in capturing relevant patterns related to customer satisfaction. Perfor
bootstrap sample. This is mathematically represented as: mance evaluation is conducted before and after feature selection to 
(X assess improvements. The metrics are calculated using the following 

c,Yc)=Bootstrap (X,Y) for c= 1,2,…, n (1) 
equations: 

Each bootstrap sample (Xc,Yc) is used to train a decision tree in the 
Random Forest. The bootstrapping process ensures that each tree is Tp + T

Accuracy n
= (5) 

trained on a slightly different subset of the data, which helps to reduce Tp + Fp + Fn + Tn

overfitting and improve the model’s reliability. 
Precision × Recall

Fscore= (6) 
Step 2: Decision tree construction Precision + Recall

For each country-specific sub-sample, the Random Forest model was 
For each bootstrap sample (Xc,Yc), a decision tree is trained. Each trained using an 80/20 train-test split, accompanied by 5-fold cross- 

tree is built by selecting a random subset of features at each split, which validation to ensure reliability and reduce overfitting (Adewale et al., 
promotes diversity among the trees. 2024). For the pooled dataset, robustness was assessed through 

cross-country validation using two scenarios: in Scenario 1, the model 
Step 3: Prediction aggregation was trained on the Indonesian sub-sample and tested on the Hungarian 

sub-sample; in Scenario 2, the model was trained on the Hungarian 
For a new observation, the prediction is made by aggregating the sub-sample and tested on the Indonesian sub-sample. All modeling 

results from all ntree decision trees using majority voting. The final pre procedures were implemented in Python 3.13 via Google Colab, using 

5 



T. Wicaksono et al.                                                                                                                                                                                  C  l e a  n  e r   E  n v  i r o  n  m  e  n  t a l  S  y  s t e  m  s 18 (2025) 100302 

the Scikit-learn library. The computational setup included a 2.20 GHz 4. Results and discussion
processor, 16 GB RAM, a 4 GB graphics card, and a 64-bit operating 
system. Hyperparameter tuning determined that 700 decision trees 4.1. Profile respondents
offered an optimal balance between predictive accuracy and computa
tional efficiency (Sun et al., 2023). The Gini index was selected as the The sample of 1428 respondents comprised food service customers 
splitting criterion, following best practices in classification-based from Indonesia (820 respondents, 57.42 %) and Hungary (608 re
feature importance modeling (Majidian et al., 2024). The Random spondents, 42.58 %), providing perspectives from both an emerging and 
Forest algorithm was selected for its robustness against overfitting and a developed market. Gender distribution was well-balanced across both 
its suitability for high-dimensional, decision-oriented problems (Yang countries. In Indonesia, 373 respondents (45.5 %) were male and 447 
et al., 2024). The full research framework, including data collection, (54.5 %) were female, while in Hungary, 295 respondents (48.5 %) were 
model development, and prioritization, is presented in Fig. 2. male and 313 (51.5 %) were female.

Fig. 2. Research framework.

6 



T. Wicaksono et al.                                                                                                                                                                                  C  l e a  n  e r   E  n v  i r o  n  m  e  n  t a l  S  y  s t e  m  s 18 (2025) 100302 

Age distribution followed similar patterns in both countries, with demographic characteristics and purchasing behaviors across the two 
some variations. In Indonesia, the largest age group was 30–44 years countries.
(339 respondents, 41.3 %), followed by 18–29 years (266 respondents, 
32.4 %). Respondents aged 45–59 accounted for 17.6 % (144 re 4.2. Measures identification
spondents), while those aged 60 or older represented the smallest group 
(71 respondents, 8.7 %). Hungary showed a comparable distribution, As mentioned earlier in methodology, Sixteen potential CEaaS 
with the 30–44 age group being the largest (285 respondents, 46.9 %), measures affecting customer satisfaction in food service were identified 
followed by 18–29 years (152 respondents, 25.0 %). The 45–59 and 60+ through systematic literature review using PRISMA framework and were 
age groups constituted 18.6 % (113 respondents) and 9.5 % (58 re listed in Table 2. And were used in survey to collect the datasets in 
spondents), respectively. Indonesia and Hungary.

Educational backgrounds differed slightly between the two coun
tries. In Indonesia, the largest proportion of respondents held a Bache 4.3. Model performance metrics and CEaaS measure prioritization
lor’s degree (348 respondents, 42.4 %), followed by high school 
graduates (210 respondents, 25.6 %). Associate degrees were held by Three models were developed based on different datasets: the 
152 respondents (18.5 %), while Master’s and Doctorate degrees Indonesian sub-sample, the Hungarian sub-sample, and a pooled dataset 
accounted for 10.5 % (86 respondents) and 2.9 % (24 respondents), combining both. Model performance was assessed using the Random 
respectively. In Hungary, Bachelor’s degrees were also the most com Forest (RF) classifier, both before and after applying RF-based feature 
mon (246 respondents, 40.5 %), followed by high school diplomas (172 selection. In the initial phase, each sub-sample dataset was used to train 
respondents, 28.3 %). Associate degrees were held by 114 respondents its respective model using an 80/20 train-test split. The Indonesian 
(18.8 %), while Master’s degrees represented 11.7 % (71 respondents). model achieved an accuracy of 81.77 % (0.8177) and an F-score of 
Only 0.8 % (5 respondents) held a Doctorate. 78.63 % (0.7863), while the Hungarian model recorded an accuracy of 

Employment status revealed that the majority of respondents in both 82.44 % (0.8244) and an F-score of 79.27 % (0.7927). Further evalua
countries were employed, with 480 individuals (58.5 %) in Indonesia tion using 5-fold cross-validation yielded average performance metrics 
and 396 individuals (65.1 %) in Hungary. Students constituted 16.5 % of 80.46 % accuracy and 77.38 % F-score for the Indonesian dataset, and 
(135 respondents) in Indonesia and 17.4 % (106 respondents) in 79.66 % accuracy and 78.51 % F-score for the Hungarian dataset. For 
Hungary. Self-employed individuals represented 12.9 % (106 re the pooled dataset, a cross-country validation approach was imple
spondents) in Indonesia and 12.7 % (77 respondents) in Hungary. Un mented to assess generalizability. In Scenario 1, where the model was 
employment rates differed more noticeably, with 10.6 % (87 trained on the Indonesian dataset and tested on the Hungarian dataset, 
respondents) in Indonesia compared to only 3.8 % (23 respondents) in the model achieved an accuracy of 79.52 % (0.7952) and an F-score of 
Hungary. Retirees were the smallest group in both countries, comprising 76.27 % (0.7627). In Scenario 2, trained on the Hungarian dataset and 
1.5 % in Indonesia and 1.0 % in Hungary. tested on the Indonesian dataset, the accuracy was 76.83 % (0.7683) 

Food service purchase frequency followed similar trends in both with an F-score of 73.55 % (0.7355). These results indicate acceptable 
markets. The most common category was “Sometimes (2–3 times a levels of model robustness both within individual country contexts and 
month)," reported by 250 respondents (30.5 %) in Indonesia and 189 across cross-country scenarios.
(31.1 %) in Hungary. "Often (once a week)" was the second most Subsequently, Random Forest-based feature selection was applied 
frequent, with 239 respondents (29.1 %) in Indonesia and 178 (29.3 %) separately to the Indonesian, Hungarian, and pooled datasets to deter
in Hungary. "Very often (multiple times a week)" was indicated by 199 mine the Relative Importance Score (RIS) of each of the 16 CEaaS 
respondents (24.3 %) in Indonesia and 135 (22.2 %) in Hungary, while measures. This process enabled ranking the measures based on their 
“Rarely (once a month or less)" was reported by 132 respondents (16.1 contribution to the classifier’s predictive performance. The results are 
%) in Indonesia and 106 (17.4 %) in Hungary. These findings are visualized in Fig. 3, which compares the prioritized CEaaS measures 
summarized in Table 1, which provides a comprehensive breakdown of across the three datasets.

Following feature selection, each model was retrained using only the 
Table 1 top seven CEaaS measures, which were identified as the most influential 
Survey respondent demographic. in achieving optimal model performance and relevance to the target 

variable. The hyperparameters used in the original training process were 
Demographic variables Indonesia (n Hungary (n 

= 820) = 608) retained. This refinement led to a notable improvement in performance 
metrics.

Gender Male 373 (45.5 %) 295 (48.5 %)
Female 447 (54.5 %) 313 (51.5 %) In the Indonesian model, the top seven measures included: sustain

Age 18–29 266 (32.4 %) 152 (25.0 %) able sourcing (CM6), reusable packaging systems (CM2), circular loyalty 
30–44 339 (41.3 %) 285 (46.9 %) programs (CM16), surplus food redistribution (CM3), digital inventory 
45–59 144 (17.6 %) 113 (18.6 %) management (CM7), food waste upcycling services (CM1), and carbon- 
60 or older 71 (8.7 %) 58 (9.5 %) neutral delivery services (CM8). Using the 80/20 train-test split, the F- 

Education High school 210 (25.6 %) 172 (28.3 %)
Associate degree 152 (18.5 %) 114 (18.8 %) score increased by 5.16 percentage points to 83.79 %, and accuracy 
Bachelor’s degree 348 (42.4 %) 246 (40.5 %) improved by 3.82 points to 85.59 %. Under 5-fold cross-validation, the 
Master’s degree 86 (10.5 %) 71 (11.7 %) F-score increased by 4.82 points to 82.11 %, and accuracy improved by 
Doctorate 24 (2.9 %) 5 (0.8 %) 5.47 points to 85.93 %. In the Hungarian model, the top seven measures 

Occupation Student 135 (16.5 %) 106 (17.4 %)
Employed 480 (58.5 %) 396 (65.1 %) were: circular loyalty programs (CM16), surplus food redistribution 
Self-Employed 106 (12.9 %) 77 (12.7 %) (CM3), sustainable sourcing (CM6), reusable packaging systems (CM2), 
Retired 12 (1.5 %) 6 (1 %) food waste upcycling services (CM1), carbon-neutral delivery services 
Unemployed 87 (10.6 %) 23 (3.8 %) (CM8), and digital inventory management (CM7). The 80/20 split 

Customer food service Rarely (once a month 132 (16.1 %) 106 (17.4 %) showed an F-score increase of 4.92 points to 84.19 % and an accuracy 
purchase frequency or less)

Sometimes (2–3 250 (30.5 %) 189 (31.1 %) improvement of 3.66 points to 86.10 %. With 5-fold cross-validation, the 
times a month) F-score increased by 4.73 points to 83.24 %, and accuracy rose by 5.57 
Often (once a week) 239 (29.1 %) 178 (29.3 %) points to 85.23 %. In the pooled model, the top seven measures 
Very often (multiple 199 (24.3 %) 135 (22.2 %) included: sustainable sourcing (CM6), circular loyalty programs 
times a week) (CM16), reusable packaging systems (CM2), surplus food redistribution 

7 



T. Wicaksono et al.                                                                                                                                                                                  C  l e a  n  e r   E  n v  i r o  n  m  e  n  t a l  S  y  s t e  m  s 18 (2025) 100302 

Table 2 
Potential of Circular Economy as a Service (CEaas) measures in food service.

CEaaS Measures (CM) Description References

Food waste upcycling services Transforms food waste into valuable products to provide customers with a sustainable and responsible food service Kanwal et al. (2024);
(CM1) experience.

Reusable packaging systems This service offers reusable containers through a return-and-refill system to eliminate packaging waste and enhance Camps-Posino et al. 
(CM2) customer convenience. (2021)

Surplus food redistribution (CM3) Redistributes surplus food to charities or consumers to provide customers with affordable options while reducing Rut and Davies (2023)
food waste.

Energy recovery from waste (CM4) This service converts organic waste into renewable energy to ensure customers benefit from environmentally Iqbal et al. (2023);
responsible food operations.

Closed-loop water recycling systems This service treats and reuses water within food operations to support sustainability and responsible water Biswas et al. (2019)
(CM5) management for customers.

Sustainable sourcing (CM6) prioritizes local, regenerative, or surplus ingredients to provide customers with ethically sourced and Kanwal et al. (2024);
environmentally responsible food options.

Digital inventory management This service optimizes inventory through AI-driven systems to ensure customers receive fresher products and Omar et al. (2024);
(CM7) experience minimal food waste.

Carbon-neutral delivery services This service offsets delivery emissions through sustainable practices to provide customers with environmentally Hossain et al. (2023)
(CM8) responsible food delivery.

Sustainable food literacy programs This program offers workshops and digital tools to empower customers to make informed choices that support Teng and Chih (2022)
(CM9) sustainable food consumption.

Modular equipment leasing (CM10) Leased and upgradable kitchen equipment to ensure customers benefit from efficient and sustainable food Da Silva et al. (2024)
preparation.

Local food hubs (CM11) Sources local, surplus, and imperfect produce to reduce waste, support local economies, cut emissions, and provide Son (2023)
fresher ingredients through a low-carbon supply chain.

Green cleaning (CM12) This service uses environmentally friendly cleaning materials and methods to ensure customers benefit from a Jin et al. (2021)
healthier, safer, and more sustainable food environment.

End-of-life material take-back This program collects and recycles used materials from food operations to ensure customers contribute to a fully Camps-Posino et al. 
programs (CM13) circular system. (2021)

Regenerative agriculture This service connects businesses with regenerative farms to provide customers with products that actively support Cherubin et al. (2024)
partnerships (CM14) ecosystem restoration.

Smart food waste tracking systems This service uses IoT technology to monitor food waste in real time to ensure customers benefit from sustainable Singh et al. (2025)
(CM15) resource management.

Circular loyalty programs (CM16) This program rewards customers for participating in sustainable practices to encourage responsible consumption Krampe et al. (2025)
and environmental engagement.

(CM3), food waste upcycling services (CM1), carbon-neutral delivery 2024). In contrast, while CM6 still ranks highly in the Hungarian dataset 
services (CM8), and digital inventory management (CM7). Under cross- (16.05 %), it is surpassed by circular loyalty programs (CM16) and 
country validation, Scenario 1 (trained on Indonesia, tested on Hungary) surplus food redistribution (CM3), suggesting a more nuanced prioriti
showed an F-score increase of 4.24 points to 80.51 % and accuracy zation structure potentially shaped by distinct consumer values or reg
improvement of 6.29 points to 85.81 %. Scenario 2 (trained on Hungary, ulatory pressures in the Hungarian context. The dominance of this 
tested on Indonesia) recorded an F-score increase of 6.79 points to 80.34 measure indicates that consumers are increasingly demanding not only 
% and accuracy improvement of 6.44 points to 83.27 %. These findings high-quality food products but also verifiable sustainability commit
underscore that the models achieved stronger robustness following ments from food service providers (Orden-Mejía and Moreno-Manzo, 
feature selection. By eliminating nine less significant features, the 2024; Liao et al., 2023).
models reduced noise in the datasets, thereby improving interpretability Circular loyalty programs (CM16) are particularly notable for their 
and predictive performance. The final selection of seven CEaaS measures top ranking in Hungary (17.34 %) and second-place position in the 
in each model was justified by their high contribution to performance pooled dataset (17.21 %), indicating broad appeal across both national 
improvement, as indicated by increased F-score and accuracy. Detailed and integrated datasets. This measure also ranks third in Indonesia 
comparisons of model performance before and after feature selection are (14.83 %), suggesting that gamified, incentive-based mechanisms for 
presented in Fig. 4. encouraging sustainable behavior are viewed favorably across diverse 

The importance score of each CEaaS measure was derived using the consumer groups. The appeal of CM16 likely derives from its ability to 
feature importance outputs of the Random Forest algorithm. Each bridge sustainability with consumer engagement, rewarding waste- 
measure’s significance level was calculated as a proportion of the total reducing behaviors while strengthening brand-customer relationships 
importance of the top seven measures. Table 3, Tables 4 and 5 present (Krampe et al., 2025). These programs transform sustainability from a 
the detailed rankings, importance scores, and significance levels for the passive corporate value into an interactive, loyalty-enhancing 
Indonesian, Hungarian, and pooled datasets, respectively. experience.

The comparative analysis of CEaaS measure prioritizations across Interestingly, reusable packaging systems (CM2) show substantial 
Indonesian, Hungarian, and pooled datasets reveals both convergence prioritization in Indonesia (16.84 %) and the pooled dataset (16.68 %), 
and divergence in sustainability preferences across national contexts, where they rank second and third, respectively. In Hungary, this mea
offering meaningful insights into region-specific consumer expectations sure ranks fourth (14.81 %), indicating relatively consistent perceived 
as well as global trends in sustainable food service innovation. Notably, value across regions. The high priority attributed to CM2 highlights 
sustainable sourcing (CM6) emerges as the most critical measure in both increasing public concern about single-use packaging waste and its 
the Indonesian and pooled datasets, with respective importance scores environmental impacts. This preference aligns with ongoing consumer 
of 0.121333 (19.92 %) and 0.114727 (18.66 %). This consistent prior pressure for visible, product-level sustainability initiatives that mini
itization indicates a strong cross-national consensus regarding the mize waste at the point of consumption (Bonfanti et al., 2025). Its 
importance of ethically sourced, traceable, and environmentally ranking just below loyalty programs in Hungary may reflect a more 
responsible food procurement practices. This finding echoes previous behavior-centric interpretation of sustainability compared to the 
studies emphasizing consumer demand for supply chain transparency product-centric focus observed in the Indonesian context.
and ecological accountability (Hopkins et al., 2023; Wilkinson et al., Measures related to food waste mitigation, such as surplus food 

8 



T. Wicaksono et al.                                                                                                                                                                                  C  l e a  n  e r   E  n v  i r o  n  m  e  n  t a l  S  y  s t e  m  s 18 (2025) 100302 

Fig. 3. CEaaS measures importance score.

9 



T. Wicaksono et al.                                                                                                                                                                                  C  l e a  n  e r   E  n v  i r o  n  m  e  n  t a l  S  y  s t e  m  s 18 (2025) 100302 

Fig. 4. Model performance metrics.

redistribution (CM3) and food waste upcycling services (CM1), consis 2024).
tently occupy mid-ranking positions across all datasets. CM3 ranks The ranking of carbon-neutral delivery services (CM8) and digital 
fourth in both Indonesia (14.20 %) and the pooled data (13.58 %), and inventory management (CM7) offers a particularly insightful contrast. 
second in Hungary (16.53 %). CM1, meanwhile, is ranked fifth in While these measures are consistently placed at the bottom of the top- 
Hungary (13.60 %), sixth in Indonesia (11.59 %), and fifth in the pooled seven ranking across all datasets, their importance scores remain rela
data (11.64 %). This recurring prominence underscores consumer tively high, particularly in Indonesia where CM8 ranks seventh (10.26 
awareness of and support for circular economy solutions that repurpose %) and CM7 ranks fifth (12.35 %). In Hungary and the pooled datasets, 
or redirect food waste. The prominence of CM3 in Hungary may also these measures switch positions but remain in the sixth and seventh 
reflect cultural or institutional support for food-sharing systems or na spots, with similar significance levels (around 10–11 %). This pattern 
tional food rescue regulations. In both cases, these measures reflect suggests that while these measures are perceived as essential enablers of 
increasing expectations for businesses to move beyond traditional waste sustainability, they are perhaps viewed more as backend or infra
minimization and adopt proactive circular strategies (Kanwal et al., structural strategies rather than consumer-facing priorities. 

10 



T. Wicaksono et al.                                                                                                                                                                                  C  l e a  n  e r   E  n v  i r o  n  m  e  n  t a l  S  y  s t e  m  s 18 (2025) 100302 

Table 3 such as loyalty programs and food redistribution.
CEaaS measures rank based on importance level (Indonesia dataset). These insights affirm that effective CEaaS strategies must incorporate 

Priority CEaaS measures Importance Significance level Ranks both universal sustainability expectations and region-specific consumer 
score (%) preferences. A hybrid model that prioritizes traceable sourcing, visible 

Sustainable sourcing (CM6) 0.121333 0.199202 1 waste-reduction systems, incentive-based behavioral design, and oper
Reusable packaging system 0.102564 0.168387 2 ational transparency will be best positioned to meet the multidimen

(CM2) sional demands of today’s food service consumers. Moreover, the high 
Circular loyalty program 0.090326 0.148295 3 cumulative significance scores of the top seven measures in each dataset 

(CM16)
Surplus food redistribution 0.086477 0.141976 4 demonstrate the necessity for integrated, multi-pronged sustainability 

(CM3) initiatives that span sourcing, engagement, logistics, and waste man
Digital inventory management 0.075225 0.123503 5 agement. As food service businesses seek to enhance competitiveness 

(CM7) and compliance in an era of climate-conscious consumption, aligning 
Food waste upcycling services 0.070619 0.115941 6 operations with these prioritized CEaaS measures will be instrumental in 

(CM1)
Carbon-neutral delivery 0.062552 0.102696 7 achieving sustainable transformation and long-term customer trust.

services (CM8)
5. Conclusion

Table 4 This study examined the prioritization of Circular Economy as a 
CEaaS measures rank based on importance level (Hungary dataset). Service (CEaaS) measures in the food service sector using a Random 

Forest-based feature importance analysis across Indonesian, Hungarian, 
Priority CEaaS measures Importance Significance level Ranks

score (%) and pooled datasets. By comparing the top seven measures in each 
dataset, the findings reveal a clear convergence around certain sus

Circular loyalty program 0.108223 17.34 1
(CM16) tainability imperatives, particularly sustainable sourcing, reusable 

Surplus food redistribution 0.103147 16.53 2 packaging systems, circular loyalty programs, and food waste mitigation 
(CM3) strategies. Despite national differences in ranking orders, these core 

Sustainable sourcing (CM6) 0.100129 16.05 3 measures consistently reflect global consumer expectations for ethically 
Reusable packaging system 0.092433 14.81 4 responsible, resource-efficient, and socially conscious food service 

(CM2)
Food waste upcycling services 0.084877 13.60 5 practices.

(CM1) Sustainable sourcing (CM6) emerged as the most critical measure in 
Carbon-neutral delivery 0.068031 10.90 6 both the Indonesian and pooled datasets, while circular loyalty pro

services (CM8) grams (CM16) were most emphasized in Hungary, highlighting both 
Digital inventory management 0.067193 10.77 7

(CM7) cross-national alignment and cultural variability in sustainability pri
orities. The consistently high ranking of food waste-related measures, 
such as surplus food redistribution (CM3) and food waste upcycling 
services (CM1), underscores a growing demand for visible circular 

Table 5 
CEaaS measures rank based on importance level (Pooled dataset). practices that extend beyond environmental responsibility to include 

social value creation. Additionally, the inclusion of carbon-neutral de
Priority CEaaS measures Importance Significance level Ranks livery services (CM8) and digital inventory management (CM7) across 

score (%) all datasets reflects a broader recognition of the operational backbone 
Sustainable sourcing (CM6) 0.114727 18.66 1 required to support sustainable service delivery.
Circular loyalty program 0.105816 17.21 2

(CM16) The results demonstrate that consumers increasingly value a 
Reusable packaging system 0.102529 16.68 3 comprehensive approach to sustainability, one that integrates environ

(CM2) mental, social, and technological dimensions. Measures that enhance 
Surplus food redistribution 0.083468 13.58 4 traceability, reduce packaging waste, incentivize responsible behavior, 

(CM3) and minimize food loss are no longer viewed as supplementary efforts 
Food waste upcycling services 0.071583 11.64 5

(CM1) but as central to a competitive and future-ready food service strategy. 
Carbon-neutral delivery 0.070273 11.43 6 While visible front-end sustainability initiatives remain highly valued, 

services (CM8) the growing importance of back-end operational efficiency signals a 
Digital inventory management 0.066358 10.79 7 maturing consumer perspective on what constitutes meaningful 

(CM7) sustainability.
By applying the Random Forest algorithm, this study provides an 

Nevertheless, their inclusion in the top-tier measures across all datasets evidence-based understanding of feature prioritization that can inform 
signals a growing consumer sensitivity to the environmental impacts of strategic decision-making in food service innovation. The significance 
logistics and the role of intelligent systems in minimizing resource waste levels derived from model outputs offer practical guidance for stake
and ensuring service reliability (Milenković et al., 2024; Vhatkar et al., holders seeking to allocate resources and design interventions aligned 
2024). with consumer values. The integration of machine learning enhances the 

From a broader perspective, the alignment across datasets reveals objectivity and robustness of the prioritization process, reinforcing its 
several globally resonant sustainability imperatives, particularly those utility for policymaking, corporate strategy, and service design in the 
related to ethical sourcing, packaging reuse, food waste recovery, and context of circular economy transitions.
digitally enabled operational efficiency. However, the variation in top Overall, the findings reinforce the urgency for food service providers 
priorities across national datasets underscores the importance of to adopt integrated CEaaS strategies that combine ethical sourcing, 
context-sensitive strategies. Indonesian consumers appear more circular product systems, behavioral engagement tools, and digital 
responsive to upstream environmental interventions such as sustainable operational infrastructures. Such strategies will be essential for 
sourcing and packaging, while Hungarian consumers place slightly achieving long-term customer satisfaction, regulatory compliance, and 
greater emphasis on behaviorally engaging or socially focused measures alignment with broader sustainability goals.

11 



T. Wicaksono et al.                                                                                                                                                                                  C  l e a  n  e r   E  n v  i r o  n  m  e  n  t a l  S  y  s t e  m  s 18 (2025) 100302 

6. Research implications conscious marketplace.

6.1. Theoretical implication 6.3. Policy implication

This study contributes to the theoretical development of Circular The study offers several policy recommendations that support sys
Economy as a Service (CEaaS) in the food service domain by integrating temic CEaaS adoption in the food service sector. First, to promote sus
machine learning with a structured prioritization framework rooted in tainable sourcing, governments can introduce fiscal incentives such as 
customer-oriented sustainability. By applying the Random Forest algo tax credits or subsidies for businesses that prioritize local, regenerative, 
rithm for feature selection and prioritization, the research enhances or surplus-derived ingredients. This would encourage ethical procure
methodological rigor in identifying CEaaS measures aligned with con ment and support regional food ecosystems (Chenavaz and Dimitrov, 
sumer preferences across diverse national contexts. It responds to the 2024). Second, the consistent importance of reusable packaging systems 
increasing demand for data-driven sustainability research that moves across datasets points to the need for regulatory interventions that 
beyond conceptual generalizations toward empirically grounded, facilitate waste reduction. Mandating reusable packaging use in com
actionable insights (Boozary et al., 2025). mercial food service or introducing penalties for excessive single-use 

First, the study extends existing literature by systematically quanti plastic can accelerate packaging circularity and reduce landfill waste 
fying the relative importance of CEaaS measures through their contri (Suresh et al., 2024). Third, to support food waste mitigation, policies 
bution to model performance. Unlike prior works that treat should promote redistribution networks and upcycling innovation. 
sustainability practices as uniform initiatives, this study reveals regional Policymakers could create digital platforms connecting food service 
heterogeneity in their perceived value. For example, the prominence of businesses with charities and provide grants for R&D in food byproduct 
sustainable sourcing in both the Indonesian and pooled datasets, and the conversion technologies. Fourth, the importance of carbon-neutral de
top ranking of circular loyalty programs in Hungary, reflect varied livery services underscores the urgency of sustainable logistics regula
consumer expectations, emphasizing the importance of context-specific tion. Policies could mandate emission reporting for food delivery 
strategies. Second, the research refines our understanding of circular platforms and offer incentives for adopting electric vehicles or 
economy adoption by showing that consumer perceptions are influenced low-emission logistics systems. Lastly, to encourage digital trans
not only by front-facing interventions such as packaging or loyalty formation in inventory management, policymakers can support SMEs in 
programs, but also by backend operations, including digital inventory adopting smart technologies through funding, technical training, or tax 
systems and carbon-neutral logistics. This expands CEaaS’s conceptual relief. Such interventions would enhance food system efficiency while 
scope to include logistical and technological infrastructure as essential aligning national policy with consumer-driven sustainability expecta
components of sustainable service delivery. Third, the study underscores tions. By aligning theoretical advancement, strategic implementation, 
the role of technological open innovation in advancing sustainability, and regulatory frameworks with the prioritized CEaaS measures iden
highlighting how machine learning can catalyze systemic change in the tified in this study, stakeholders can foster a more resilient, efficient, and 
food service sector (Rodrigues et al., 2023). The integration of feature sustainable food service industry.
selection with cross-country model validation demonstrates machine 
learning’s potential not only for predictive performance but also for 7. Study limitation and future research direction
enabling generalizability across markets, offering a replicable frame
work for future research across sectors and regions. Despite its contributions, this study has several limitations that 

warrant attention. First, the survey sample, while sufficient for initial 
6.2. Practical implication analysis, may not fully represent the diversity of global food service 

consumers due to potential geographic and cultural bias. Future studies 
The findings provide strategic guidance for food service businesses should incorporate more geographically and demographically diverse 

aiming to implement high-impact CEaaS initiatives. The consistent pri populations to enhance generalizability. Second, the use of self-reported 
oritization of sustainable sourcing across datasets underscores the need perceptions to assess CEaaS importance levels may introduce subjective 
for ethical, traceable, and environmentally responsible procurement. bias, potentially leading to over- or underestimation of sustainability 
Businesses are advised to collaborate with regenerative agriculture priorities. Complementing survey-based data with objective perfor
networks, local producers, and surplus food suppliers to enhance supply mance metrics, such as transactional records or operational sustain
chain transparency and ecological stewardship (You et al., 2024). The ability outcomes, would enhance the robustness of future analyses. 
strong performance of circular loyalty programs and reusable packaging Third, the cross-sectional design of the study limits its ability to capture 
systems highlights a dual imperative: incentivize consumer engagement the dynamic nature of consumer attitudes toward CEaaS initiatives. 
through behavior-based rewards and reduce packaging-related waste. Longitudinal research would be valuable to track evolving priorities 
Food service firms should design loyalty schemes that promote over time, particularly as awareness of circular economy practices in
low-waste behaviors and invest in scalable reusable packaging infra creases. Addressing these limitations can support more comprehensive, 
structure that aligns with consumer convenience and sustainability accurate, and context-sensitive insights into the adoption and effec
preferences (Krampe et al., 2025; Bonfanti et al., 2025). The prominence tiveness of CEaaS measures in the global food service sector.
of surplus food redistribution and food waste upcycling points to service 
innovation opportunities embedded in circular principles. Partnering CRediT authorship contribution statement
with food banks, donation platforms, or upcycling startups allows 
businesses to cut environmental impact while generating social value Tutur Wicaksono: Writing – review & editing, Writing – original 
and alternative revenue streams (Kanwal et al., 2024). The inclusion of draft, Visualization, Validation, Resources, Project administration, 
carbon-neutral delivery and digital inventory management among the Methodology, Investigation, Formal analysis, Data curation, Conceptu
top-ranked measures indicates that operational innovations are essential alization. Marhadi Marhadi: Writing – original draft, Validation, Re
to sustainability agendas. Businesses should pursue carbon mitigation sources, Project administration, Investigation, Data curation. Agustinus 
strategies such as fleet electrification and carbon offset programs, while Fritz Wijaya: Writing – review & editing, Software, Project adminis
using AI-driven inventory tools to optimize freshness, reduce spoilage, tration, Methodology, Conceptualization. Velly Anatasia: Writing – 
and improve service reliability (Milenković et al., 2024; Vhatkar et al., review & editing, Software, Project administration, Conceptualization. 
2024). These operational upgrades not only advance sustainability goals Krisztina Taralik: Validation, Supervision, Project administration, 
but also enhance brand credibility in a competitive, environmentally Conceptualization.

12 



T. Wicaksono et al.                                                                                                                                                                                  C  l e a  n  e r   E  n v  i r o  n  m  e  n  t a l  S  y  s t e  m  s 18 (2025) 100302 

Declaration of generative AI and AI-assisted technologies in the models for accurate churn prediction. International Journal of Information 
writing process Management Data Insights 5, 100331. https://doi.org/10.1016/j. 

jjimei.2025.100331.
Borg, K., Lennox, A., Kaufman, S., Tull, F., Prime, R., Rogers, L., Dunstan, E., 2022. 

During the preparation of this work the author(s) used Grammarly in Curbing plastic consumption: a review of single-use plastic behaviour change 
order to improve language and delivery fluency. After using this tool/ interventions. J. Clean. Prod. 344, 131077. https://doi.org/10.1016/j. 

jclepro.2022.131077.
service, the author(s) reviewed and edited the content as needed and Camilleri, M.A., 2024. Sustainability accounting and disclosures of responsible 
take(s) full responsibility for the content of the publication. restaurant practices in environmental, social and governance (ESG) reports. Int. J. 

Hospit. Manag. 126, 104051. https://doi.org/10.1016/j.ijhm.2024.104051.
Camps-Posino, L., Batlle-Bayer, L., Bala, A., Song, G., Qian, H., Aldaco, R., Xifré, R., 

Declaration of competing interest Fullana-I-Palmer, P., 2021. Potential climate benefits of reusable packaging in food 
delivery services. A Chinese case study. Sci. Total Environ. 794, 148570. https://doi. 
org/10.1016/j.scitotenv.2021.148570.

The authors declare that they have no known competing financial Carino, S., Porter, J., Malekpour, S., Collins, J., 2020. Environmental sustainability of 
interests or personal relationships that could have appeared to influence hospital foodservices across the food supply chain: a systematic review. J. Acad. 
the work reported in this paper. Nutr. Diet. 120, 825–873. https://doi.org/10.1016/j.jand.2020.01.001.

Chenavaz, R.Y., Dimitrov, S., 2024. From waste to wealth: policies to promote the 
circular economy. J. Clean. Prod. 443, 141086. https://doi.org/10.1016/j. 

Acknowledgement jclepro.2024.141086.
Cherubin, M.R., Pinheiro Junior, C.R., Alves, L.A., Bayer, C., Cerri, C.E.P., Barioni, L.G., 

Peper, A., Anselmi, A.A., 2024. Carbon farming initiative: a national-scale public- 
This research did not receive any external funding or specific grants private partnership to promote regenerative agriculture in Brazil. Exp. Agric. 60. 

from public, commercial, or non-profit sectors. https://doi.org/10.1017/s0014479724000255.
Chesbrough, H., 2019. Open innovation results: going beyond the hype and getting Down 

to business. https://scholar.google.com/scholar_lookup?title=Open%20Innovation 
Data availability %20Results%3A%20Going%20Beyond%20the%20Hype%20and%20Getting%20Do 

wn%20to%20Business&author=H.%20Chesbrough&publication_year=2019.
Data will be available upon request from the corresponding author. Csedő, Z., Zavarkó, M., Magyari, J., 2023. Implications of open eco-innovation for 

sustainable development: evidence from the European renewable energy sector. 
Sustainable Futures 6, 100143. https://doi.org/10.1016/j.sftr.2023.100143.

References Da Silva, S.B.G., Barros, M.V., Radicchi, J.Â.Z., Puglieri, F.N., Piekarski, C.M., 2024. 
Opportunities and challenges to increase circularity in the product’s use phase. 

Acerbi, F., Taisch, M., 2020. A literature review on circular economy adoption in the Sustainable Futures, 100297. https://doi.org/10.1016/j.sftr.2024.100297.
manufacturing sector. J. Clean. Prod. 273, 123086. https://doi.org/10.1016/j. Damiani, M., Pastorello, T., Carlesso, A., Tesser, S., Semenzin, E., 2021. Quantifying 
jclepro.2020.123086. environmental implications of surplus food redistribution to reduce food waste. 

Adelodun, B., Kareem, K.Y., Kumar, P., Kumar, V., Choi, K.S., Yadav, K.K., Yadav, A., El- J. Clean. Prod. 289, 125813. https://doi.org/10.1016/j.jclepro.2021.125813.
Denglawey, A., Cabral-Pinto, M., Son, C.T., Krishnan, S., Khan, N.A., 2021. Danish, M.S.S., Senjyu, T., 2023. Shaping the future of sustainable energy through AI- 
Understanding the impacts of the COVID-19 pandemic on sustainable agri-food enabled circular economy policies. Circular Economy 2, 100040. https://doi.org/ 
system and agroecosystem decarbonization nexus: a review. J. Clean. Prod. 318, 10.1016/j.cec.2023.100040.
128451. https://doi.org/10.1016/j.jclepro.2021.12845. Dantas, R.M., Ilyas, A., Rita, J.X., 2022. Circular entrepreneurship in emerging markets 

Adewale, M.D., Ebem, D.U., Awodele, O., Sambo-Magaji, A., Aggrey, E.M., Okechalu, E. through the lens of sustainability. J Open Innov. Technol. Mark. Complex. 8, 211. 
A., Donatus, R.E., Olayanju, K.A., Owolabi, A.F., Oju, J.U., Ubadike, O.C., Otu, G.A., https://doi.org/10.3390/joitmc8040211.
Muhammed, U.I., Danjuma, O.R., Oluyide, O.P., 2024. Predicting gross domestic Devasahayam, S., Albijanic, B., 2023. Predicting hydrogen production from co- 
product using the ensemble machine learning method. Systems and Soft Computing gasification of biomass and plastics using tree based machine learning algorithms. 
6, 200132. https://doi.org/10.1016/j.sasc.2024.200132. Renew. Energy 222, 119883. https://doi.org/10.1016/j.renene.2023.119883.

Albahri, A.S., Hamid, R.A., Abdulnabi, A.R., Albahri, O.S., Alamoodi, A.H., Deveci, M., Dorrego-Viera, J.I., Urbinati, A., Lazzarotti, V., 2025. Transition towards circular 
Pedrycz, W., Alzubaidi, L., Santamaría, J., Gu, Y., 2023. Fuzzy decision-making economy: exploiting open innovation for circular product development. Journal of 
framework for explainable golden multi-machine learning models for real-time Innovation & Knowledge 10, 100668. https://doi.org/10.1016/j.jik.2025.100668.
adversarial attack detection in vehicular Ad-hoc networks. Inf. Fusion 105, 102208. Dunne, R., Reguant, R., Ramarao-Milne, P., Szul, P., Sng, L.M.F., Lundberg, M., Twine, N. 
https://doi.org/10.1016/j.inffus.2023.102208. A., Bauer, D.C., 2023. Thresholding gini variable importance with a single-trained 

Al-Obadi, M., Ayad, H., Pokharel, S., Ayari, M.A., 2022. Perspectives on food waste random forest: an empirical bayes approach. Comput. Struct. Biotechnol. J. 21, 
management: prevention and social innovations. Sustain. Prod. Consum. 31, 4354–4360. https://doi.org/10.1016/j.csbj.2023.08.033.
190–208. https://doi.org/10.1016/j.spc.2022.02.012. Durmaz, A., Demir, H., Sezen, B., 2021. The role of negative entropy within supply chain 

ASEAN (The Association of Southeast Asian Nations), 2021. Framework for circular sustainability. Sustain. Prod. Consum. 28, 218–230. https://doi.org/10.1016/j. 
economy for the ASEAN economic community. ASEAN. Available Online: https://a spc.2021.04.014.
sean.org/wp-content/uploads/2021/10/Framework-for-Circular-Economy-for-the- Eisenreich, A., Füller, J., Stuchtey, M., Gimenez-Jimenez, D., 2022. Toward a circular 
AEC_Final.pdf. value chain: impact of the circular economy on a company’s value chain processes. 

Audretsch, B.D., Belitski, M., 2022. The limits to open innovation and its impact on J. Clean. Prod. 378, 134375. https://doi.org/10.1016/j.jclepro.2022.134375.
innovation performance. Technovation 119, 102519. https://doi.org/10.1016/j. Ekman, P., Röndell, J., Kowalkowski, C., Raggio, R.D., Thompson, S.M., 2020. Emergent 
technovation.2022.102519. market innovation: a longitudinal study of technology-driven capability 

Azmat, F., Lim, W.M., Moyeen, A., Voola, R., Gupta, G., 2023. Convergence of business, development and institutional work. J. Bus. Res. 124, 469–482. https://doi.org/ 
innovation, and sustainability at the tipping point of the sustainable development 10.1016/j.jbusres.2020.10.061.
goals. J. Bus. Res. 167, 114170. https://doi.org/10.1016/j.jbusres.2023.114170. European Commission, 2020. A new circular economy action plan. For a cleaner and 

Becker, N.P., Arts, J., Reichardt, S., Lange, A., 2023. Managing inventories of reusable more competitive Europe. European commission, 2020. A new circular economy 
containers for food take-away at a restaurant. Int. J. Prod. Econ. 267, 109069. action plan. For a cleaner and more competitive Europe. https://eur-lex.europa.eu 
https://doi.org/10.1016/j.ijpe.2023.109069. /resource.html?uri=cellar:9903b325-6388-11ea-b735-01aa75ed71a1.0017 

Behera, R.K., Bala, P.K., Rana, N.P., 2023. Creation of sustainable growth with .02/DOC_1&format=PDF.
explainable artificial intelligence: an empirical insight from consumer packaged Fang, M., Cai, L., Park, K., Su, M., 2024. Trust (in)congruence, open innovation, and 
goods retailers. J. Clean. Prod. 399, 136605. https://doi.org/10.1016/j. circular economy performance: polynomial regression and response surface 
jclepro.2023.136605. analyses. J. Environ. Manag. 358, 120930. https://doi.org/10.1016/j. 

Beinabadi, H.Z., Baradaran, V., Komijan, A.R., 2024. Sustainable supply chain decision- jenvman.2024.120930.
making in the automotive industry: a data-driven approach. Soc. Econ. Plann. Sci. Gajdzik, B., Siwiec, D., Wolniak, R., Pacana, A., 2024. Approaching open innovation in 
95, 101908. https://doi.org/10.1016/j.seps.2024.101908. customization frameworks for product prototypes with emphasis on quality and life 

Biswas, W.K., Horr, Y.A., Joll, C., Rosano, M., 2019. Techno-economic and cycle assessment (QLCA). J Open Innov. Technol. Mark. Complex. 10, 100268. 
environmental implications of the use of a closed loop water recycling system in https://doi.org/10.1016/j.joitmc.2024.100268.
Qatar. Chemical Engineering Transactions. https://doi.org/10.3303/cet1972035. Geissdoerfer, M., Savaget, P., Bocken, N.M.P., Hultink, E.J., 2016. The circular economy 

Bocken, N., Konietzko, J., 2022. Circular business model innovation in consumer-facing – a new sustainability paradigm? J. Clean. Prod. 143, 757–768. https://doi.org/ 
corporations. Technol. Forecast. Soc. Change 185, 122076. https://doi.org/ 10.1016/j.jclepro.2016.12.048.
10.1016/j.techfore.2022.122076. Greer, R., Von Wirth, T., Loorbach, D., 2020. The diffusion of circular services: 

Bonfanti, A., Bagnato, G., Vigolo, V., 2025. The contribution of sustainable practices to transforming the Dutch catering sector. J. Clean. Prod. 267, 121906. https://doi. 
the creation of memorable customer experience: empirical evidence from michelin org/10.1016/j.jclepro.2020.121906.
green star restaurants. Int. J. Hospit. Manag. 126, 104110. https://doi.org/10.1016/ Herrador, M., Van, M.L., 2023. Circular economy strategies in the ASEAN region: a 
j.ijhm.2025.104110. comparative study. Sci. Total Environ. 908, 168280. https://doi.org/10.1016/j. 

Boozary, P., Sheykhan, S., GhorbanTanhaei, H., Magazzino, C., 2025. Enhancing scitotenv.2023.168280.
customer retention with machine learning: a comparative analysis of ensemble 

13 



T. Wicaksono et al.                                                                                                                                                                                  C  l e a  n  e r   E  n v  i r o  n  m  e  n  t a l  S  y  s t e  m  s 18 (2025) 100302 

Hopkins, C., Roberts, S.I., Caveen, A.J., Graham, C., Burns, N.M., 2023. Improved urban environment: the case of quito. Research in Transportation Business & 
traceability in seafood supply chains is achievable by minimising vulnerable nodes in Management 56, 101157. https://doi.org/10.1016/j.rtbm.2024.101157.
processing and distribution networks. Mar. Pol. 159, 105910. https://doi.org/ Moschen-Schimek, J., Kasper, T., Huber-Humer, M., 2023. Critical review of the recovery 
10.1016/j.marpol.2023.105910. rates of construction and demolition waste in the european union – an analysis of 

Hossain, M.A., Ferdous, N., Ferdous, E., 2023. Crisis-driven disruptions in global waste influencing factors in selected EU countries. Waste Manag. 167, 150–164. https:// 
management: impacts, challenges and policy responses amid COVID-19, Russia- doi.org/10.1016/j.wasman.2023.05.020.
Ukraine war, climate change, and colossal food waste. Environ. Chall. 14, 100807. Möslinger, M., Ulpiani, G., Vetters, N., 2023. Circular economy and waste management 
https://doi.org/10.1016/j.envc.2023.100807. to empower a climate-neutral urban future. J. Clean. Prod. 421, 138454. https://doi. 

Huang, L., Solangi, Y.A., Magazzino, C., Solangi, S.A., 2024. Evaluating the efficiency of org/10.1016/j.jclepro.2023.138454.
green innovation and marketing strategies for long-term sustainability in the context Mothafar, N.A., Zhang, J., Alsoffary, A., Aslam, M.A., Al-Barakani, A., Alhady, O.S., 
of environmental labeling. J. Clean. Prod. 450, 141870. https://doi.org/10.1016/j. Esangbedo, C.O., Kone, S.D., 2024. Effecting the adoption of blockchain technology 
jclepro.2024.141870. enablers in supply chain sustainability with green hydrogen acceptance role as a 

Hussain, M., Khan, M., Saber, H., 2023. Thematic analysis of circular economy practices mediator: evidence from complex decarbonization industries in the United Arab 
across closed-loop supply chains: an institutional theory perspective. Sustain. Prod. Emirates. Int. J. Hydrogen Energy 84, 1085–1100. https://doi.org/10.1016/j. 
Consum. 40, 122–134. https://doi.org/10.1016/j.spc.2023.06.017. ijhydene.2024.08.243.

Imjai, N., Nui-Suk, C., Usman, B., Somwethee, P., Aujirapongpan, S., 2024. The influence Murthy, Y.I., Meena, K.B., Patel, N., 2024. Machine learning for predicting the half cell 
of AI competency and design thinking skills on innovative entrepreneurial potential of cathodically protected reinforced cement concrete slabs subjected to 
competency: the role of strategic intelligence amongst new age entrepreneurs in chloride ingress. Eng. Appl. Artif. Intell. 137, 109090. https://doi.org/10.1016/j. 
Thailand. International Journal of Information Management Data Insights 4, engappai.2024.109090.
100301. https://doi.org/10.1016/j.jjimei.2024.100301. Omar, I.A., Hasan, H.R., Jayaraman, R., Salah, K., Omar, M., 2024. Using blockchain 

Iqbal, A., Zan, F., Liu, X., Chen, G., 2023. Net zero greenhouse emissions and energy technology to achieve sustainability in the hospitality industry by reducing food 
recovery from food waste: manifestation from modelling a city-wide food waste waste. Comput. Ind. Eng., 110586 https://doi.org/10.1016/j.cie.2024.110586.
management plan. Water Res. 244, 120481. https://doi.org/10.1016/j. Orden-Mejía, M., Moreno-Manzo, J., 2024. Examining consumer experience in a gourmet 
watres.2023.120481. food hall: impacts on satisfaction and behavioural intentions. Int. J. Gastron. Food 

Javaid, M., Haleem, A., Singh, R.P., Suman, R., Gonzalez, E.S., 2022. Understanding the Sci. 35, 100890. https://doi.org/10.1016/j.ijgfs.2024.100890.
adoption of industry 4.0 technologies in improving environmental sustainability. Patwa, N., Sivarajah, U., Seetharaman, A., Sarkar, S., Maiti, K., Hingorani, K., 2020. 
Sustainable Operations and Computers 3, 203–217. https://doi.org/10.1016/j. Towards a circular economy: an emerging economies context. J. Bus. Res. 122, 
susoc.2022.01.008. 725–735. https://doi.org/10.1016/j.jbusres.2020.05.015.

Jin, N., Zhang, F., Cui, Y., Sun, L., Gao, H., Pu, Z., Yang, W., 2021. Environment-friendly Pribadi, D.O., Indraprahasta, G.S., Aziz, S.A., Farandy, A.R., Hidayatina, A., Rosandi, V. 
surface cleaning using micro-nano bubbles. Particuology 66, 1–9. https://doi.org/ B., 2025. Developing circular cities in emerging economies: investigating circular 
10.1016/j.partic.2021.07.008. economy initiatives in the urban food system of two Indonesian cities. Cities 160, 

John, S.P., Supramaniam, S., 2023. Value co-creation research in tourism and hospitality 105816. https://doi.org/10.1016/j.cities.2025.105816.
management: a systematic literature review. J. Hospit. Tourism Manag. 58, 96–114. Pritee, Z.T., Anik, M.H., Alam, S.B., Jim, J.R., Kabir, M.M., Mridha, M.F., 2024. Machine 
https://doi.org/10.1016/j.jhtm.2023.11.008. learning and deep learning for user authentication and authorization in 

Johnson, E., 2022. Closing competency gaps for circularity: exploring partner dynamics cybersecurity: a state-of-the-art review. Comput. Secur. 140, 103747. https://doi. 
for circular-oriented innovation. Sustain. Prod. Consum. 34, 130–147. https://doi. org/10.1016/j.cose.2024.103747.
org/10.1016/j.spc.2022.08.029. Qahtan, S., Mourad, N., Ibrahim, H.A., Zaidan, A.A., Bahaa, B., Ding, W., 2024. Robust 

Kanda, W., Klofsten, M., Bienkowska, D., Henry, M., Hjelm, O., 2024. Challenges of three-way decisions based on ensembled multi-divergence measures with circular 
circular new ventures: an empirical analysis of 70 cases. J. Clean. Prod. 442, 141103. quintic fuzzy sets for developing swarm robots in mechanised agricultural 
https://doi.org/10.1016/j.jclepro.2024.141103. operations. Expert Syst. Appl., 126102 https://doi.org/10.1016/j. 

Kanwal, N., Zhang, M., Zeb, M., Batool, U., Khan, I., Rui, L., 2024. From plate to palate: eswa.2024.126102.
sustainable solutions for upcycling food waste in restaurants and catering. Trends Rabiee, M., Mirhashemi, M., Pangburn, M.S., Piri, S., Delen, D., 2024. Towards 
Food Sci. Technol. 152, 104687. https://doi.org/10.1016/j.tifs.2024.104687. explainable artificial intelligence through expert-augmented supervised feature 

Krampe, C., De Groot, A.-J., Hurst, W., 2025. Green loyalty? Unveiling consumer selection. Decis. Support Syst. 181, 114214. https://doi.org/10.1016/j. 
preferences in sustainable temporary loyalty programs. Clean. Responsib. Consum., dss.2024.114214.
100253 https://doi.org/10.1016/j.clrc.2025.100253. Rabiu, M.K., Jaeger-Erben, M., 2023. Reducing single-use plastic in everyday social 

Kurniawan, T.A., Meidiana, C., Goh, H.H., Zhang, D., Othman, M.H.D., Aziz, F., practices: insights from a living lab experiment. Resour. Conserv. Recycl. 200, 
Anouzla, A., Sarangi, P.K., Pasaribu, B., Ali, I., 2024. Unlocking synergies between 107303. https://doi.org/10.1016/j.resconrec.2023.107303.
waste management and climate change mitigation to accelerate decarbonization Rakesh, B., Mahendran, R., 2023. Upcycling of food waste and food loss – a sustainable 
through circular-economy digitalization in Indonesia. Sustain. Prod. Consum. 46, approach in the food sector. Trends Food Sci. Technol. 143, 104274. https://doi.org/ 
522–542. https://doi.org/10.1016/j.spc.2024.03.011. 10.1016/j.tifs.2023.104274.

Lakhouit, A., 2025. Revolutionizing urban solid waste management with AI and IoT: a Recuero-Virto, N., Arróspide, C.V., 2024. Culinary destination enchantment: the strategic 
review of smart solutions for waste collection, sorting, and recycling. Results Eng. interplay of local gastronomy in regional tourism development. Int. J. Gastron. Food 
25, 104018. https://doi.org/10.1016/j.rineng.2025.104018. Sci. 36, 100931. https://doi.org/10.1016/j.ijgfs.2024.100931.

Leitão, J., Pereira, D., De Brito, S., 2020. Inbound and outbound practices of open Ro, J.W., Yothers, C., Kendall, A., Franz, A., Zhang, R., 2024. Economic and 
innovation and eco-innovation: contrasting bioeconomy and non-bioeconomy firms. environmental performance of microalgal energy products – a case study exploring 
J Open Innov. Technol. Mark. Complex. 6, 145. https://doi.org/10.3390/ circular bioeconomy principles applied to recycled anaerobic digester waste flows. 
joitmc6040145. J. Environ. Manag. 358, 120802. https://doi.org/10.1016/j.jenvman.2024.120802.

Liao, J., Tang, J., Vinelli, A., Xie, R., 2023. A hybrid sustainability performance Rodrigues, M., Miguéis, V., Freitas, S., Machado, T., 2023. Machine learning models for 
measurement approach for fresh food cold supply chains. J. Clean. Prod. 398, short-term demand forecasting in food catering services: a solution to reduce food 
136466. https://doi.org/10.1016/j.jclepro.2023.136466. waste. J. Clean. Prod. 435, 140265. https://doi.org/10.1016/j.jclepro.2023.140265.

Liu, Z., Stephens, V., 2019. Exploring innovation ecosystem from the perspective of Rut, M., Davies, A.R., 2023. Food sharing in a pandemic: urban infrastructures, 
sustainability: towards a conceptual framework. J Open Innov. Technol. Mark. prefigurative practices and lessons for the future. Cities 145, 104609. https://doi. 
Complex. 5, 48. https://doi.org/10.3390/joitmc5030048. org/10.1016/j.cities.2023.104609.

López-Guajardo, E.A., Delgado-Licona, F., Álvarez, A.J., Nigam, K.D.P., Montesinos- Ryen, E.G., Babbitt, C.W., 2022. The role of U.S. policy in advancing circular economy 
Castellanos, A., Morales-Menendez, R., 2021. Process intensification 4.0: a new solutions for wasted food. J. Clean. Prod. 369, 133200. https://doi.org/10.1016/j. 
approach for attaining new, sustainable and circular processes enabled by machine jclepro.2022.133200.
learning. Chem. Eng. Process. Process Intensif. 180, 108671. https://doi.org/ Samberger, C., 2022. The role of water circularity in the food-water-energy nexus and 
10.1016/j.cep.2021.108671. climate change mitigation. Energy Nexus 6, 100061. https://doi.org/10.1016/j. 

Ly, D.H., Le, Q.H., Nguyen, T.D.H.N., Ahn, Y., Kim, K., Kwon, N., 2024. Advancing nexus.2022.100061.
modular construction through circular economy: insights from semi-automated Sandhu, S., Lodhia, S., Potts, A., Crocker, R., 2020. Environment friendly takeaway 
PRISMA analysis and topic modeling. J. Build. Eng. 98, 111232. https://doi.org/ coffee cup use: individual and institutional enablers and barriers. J. Clean. Prod. 
10.1016/j.jobe.2024.111232. 291, 125271. https://doi.org/10.1016/j.jclepro.2020.125271.

Magno, F., Cassia, F., 2024. Predicting restaurants’ surplus food platform continuance: Sanjuan-Delmás, D., Taelman, S.E., Arlati, A., Obersteg, A., Vér, C., Óvári, Á., Tonini, D., 
insights from the combined use of PLS-SEM and NCA and predictive model Dewulf, J., 2021. Sustainability assessment of organic waste management in three 
comparisons. J. Retailing Consum. Serv. 79, 103820. https://doi.org/10.1016/j. EU cities: analysing stakeholder-based solutions. Waste Manag. 132, 44–55. https:// 
jretconser.2024.103820. doi.org/10.1016/j.wasman.2021.07.013.

Mahboubi, A., Luong, K., Aboutorab, H., Bui, H.T., Jarrad, G., Bahutair, M., Camtepe, S., Singh, A., Prasad, S., Singh, R., Younis, K., Yousuf, O., 2025. Revolutionizing the supply 
Pogrebna, G., Ahmed, E., Barry, B., Gately, H., 2024. Evolving techniques in cyber chain: cutting-Edge strategies and technologies for food waste reduction. Bioresour. 
threat hunting: a systematic review. J. Netw. Comput. Appl. 232, 104004. https:// Technol. Rep., 102047 https://doi.org/10.1016/j.biteb.2025.102047.
doi.org/10.1016/j.jnca.2024.104004. Son, S., 2023. Transitions in South Korean public food procurement policy: landscape 

Majidian, S.Z., TaghipourEivazi, S., Arasteh, B., Ghaffari, A., 2024. Optimizing random context, institutionalization, and local agents. Environ. Innov. Soc. Transit. 48, 
forests to detect intrusion in the internet of things. Comput. Electr. Eng. 120, 100731. https://doi.org/10.1016/j.eist.2023.100731.
109860. https://doi.org/10.1016/j.compeleceng.2024.109860. Srisathan, W.A., Ketkaew, C., Naruetharadhol, P., 2023. Assessing the effectiveness of 

Milenković, M., De Yuso, A.M., Realpe, G.L., Munoz, M.R., Saavedra, L., 2024. A holistic open innovation implementation strategies in the promotion of ambidextrous 
approach to introducing a light electric freight vehicle (LEFV) system in a historic 

14 



T. Wicaksono et al.                                                                                                                                                                                  C  l e a  n  e r   E  n v  i r o  n  m  e  n  t a l  S  y  s t e  m  s 18 (2025) 100302 

innovation in Thai small and medium-sized enterprises. Journal of Innovation & barriers and opportunities for more localised procurement. J. Rural Stud. 108, 
Knowledge 8, 100418. https://doi.org/10.1016/j.jik.2023.100418. 103281. https://doi.org/10.1016/j.jrurstud.2024.103281.

Sun, Z., Wang, G., Li, P., Wang, H., Zhang, M., Liang, X., 2023. An improved random Worakittikul, W., Srisathan, W.A., Rattanpon, K., Kulkaew, A., Groves, J., Pontun, P., 
forest based on the classification accuracy and correlation measurement of decision Naruetharadhol, P., 2025. Cultivating sustainability: harnessing open innovation 
trees. Expert Syst. Appl. 237, 121549. https://doi.org/10.1016/j. and circular economy practices for eco-innovation in agricultural SMEs. J Open 
eswa.2023.121549. Innov. Technol. Mark. Complex., 100494 https://doi.org/10.1016/j. 

Suresh, J., Agarwal, V., Janardhanan, M., Saikouk, T., 2024. Unlocking sustainability: joitmc.2025.100494.
overcoming barriers to circular economy implementation in warehouse fulfilment Xuan, Y., Si, W., Zhu, J., Sun, Z., Zhao, J., Xu, M., Xu, S., 2021. Multi-model fusion short- 
centers. J. Clean. Prod., 144391 https://doi.org/10.1016/j.jclepro.2024.144391. term load forecasting based on random forest feature selection and hybrid neural 

Temizceri, F.T., Kara, S.S., 2024. Towards sustainable logistics in Turkey: a bi-objective network. IEEE Access 9, 69002–69009. https://doi.org/10.1109/ 
approach to green intermodal freight transportation enhanced by machine learning. access.2021.3051337.
Research in Transportation Business & Management 55, 101145. https://doi.org/ Yang, C.-T., Kristiani, E., Leong, Y.K., Chang, J.-S., 2024. Machine learning in microalgae 
10.1016/j.rtbm.2024.101145. biotechnology for sustainable biofuel production: advancements, applications, and 

Teng, C.-C., Chih, C., 2022. Sustainable food literacy: a measure to promote sustainable prospects. Bioresour. Technol., 131549 https://doi.org/10.1016/j. 
diet practices. Sustain. Prod. Consum. 30, 776–786. https://doi.org/10.1016/j. biortech.2024.131549.
spc.2022.01.008. You, F., Jiang, H., Liu, Y., Jiang, Y., 2024. Design interventions for sustainable eating: 

Tetteh, F.K., Kwateng, K.O., Mensah, J., 2024. Green logistics practices: a bibliometric case studies across UK and China. Advanced Design Research 2, 26–36. https://doi. 
and systematic methodological review and future research opportunities. J. Clean. org/10.1016/j.ijadr.2024.06.001.
Prod., 143735 https://doi.org/10.1016/j.jclepro.2024.143735. Yun, J.J., Zhao, X., Del Gaudio, G., Della Corte, V., Sadoi, Y., 2023. Leveraging business 

Too Good To Go, 2023. Too good to Go announces new global milestone: 200 million model innovation through the dynamics of open innovation: a multi-country 
meals saved. https://www.toogoodtogo.com/en-gb/press/200-million. investigation in the restaurant industry. Eur. J. Innovat. Manag. https://doi.org/ 

Tsai, F.-S., Cabrilo, S., Chou, H.-H., Hu, F., Tang, A.D., 2022. Open innovation and SME 10.1108/ejim-07-2023-0607.
performance: the roles of reverse knowledge sharing and stakeholder relationships. Yun, J.J., Zhao, X., Del Gaudio, G., Della Corte, V., Yigitcanlar, T., 2025. Tracing post- 
J. Bus. Res. 148, 433–443. https://doi.org/10.1016/j.jbusres.2022.03.051. capitalism in cities: insights from the commercial capitalism’s birthplaces—Genova, 

Tsui, T.-H., Van Loosdrecht, M.C.M., Dai, Y., Tong, Y.W., 2022. Machine learning and milan, and naples. Cities 158, 105715. https://doi.org/10.1016/j. 
circular bioeconomy: building new resource efficiency from diverse waste streams. cities.2025.105715.
Bioresour. Technol. 369, 128445. https://doi.org/10.1016/j.biortech.2022.128445. Yun, J.J., Zhao, X., Jeong, E., Ahn, H., Park, K., 2024. Micro open innovation dynamics 

Varjani, S., Yan, W., Priya, A., Xin, F., Lin, C.S.K., 2023. Management and valorisation under inter-rationality. Technol. Forecast. Soc. Change 201, 123263. https://doi. 
strategies for transforming food waste into bio-based products: roadblocks and the org/10.1016/j.techfore.2024.123263.
way forward. Curr. Opin. Green Sustainable Chem. 41, 100806. https://doi.org/ Zatsu, V., Shine, A.E., Tharakan, J.M., Peter, D., Ranganathan, T.V., Alotaibi, S.S., 
10.1016/j.cogsc.2023.100806. Mugabi, R., Muhsinah, A.B., Waseem, M., Nayik, G.A., 2024. Revolutionizing the 

Vhatkar, M.S., Raut, R.D., Gokhale, R., Kumar, M., Akarte, M., Ghoshal, S., 2024. food industry: the transformative power of artificial intelligence-a review. Food 
Leveraging digital technology in retailing business: unboxing synergy between Chem. X 24, 101867. https://doi.org/10.1016/j.fochx.2024.101867.
omnichannel retail adoption and sustainable retail performance. J. Retailing Zhang, X., Shao, X., Jeong, E., Jang, S., 2021. The effects of restaurant green demarketing 
Consum. Serv. 81, 104047. https://doi.org/10.1016/j.jretconser.2024.104047. on green skepticism and dining intentions: investigating the roles of benefit 

WEF, 2021. Future of Reusable Consumption Models. World Economic Forum. https:// associations and green reputation. Int. J. Hospit. Manag. 97, 103007. https://doi. 
www3.weforum.org/docs/WEF_IR_Future_of_Reusable_Consumption_2021.pdf. org/10.1016/j.ijhm.2021.103007.

Wilkinson, T.J., Nye, C., Lobley, M., West, H.G., Clappison, A., Hilton, J., Goodwin, A., 
2024. Transforming public food procurement: stakeholder understandings of 

15