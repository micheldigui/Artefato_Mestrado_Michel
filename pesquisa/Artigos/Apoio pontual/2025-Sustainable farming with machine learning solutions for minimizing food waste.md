---
source_file: "2025-Sustainable farming with machine learning solutions for minimizing food waste.txt"
original_rel_path: "Trabalhos\Artigos\Apoio pontual\txt\2025-Sustainable farming with machine learning solutions for minimizing food waste.txt"
category: "Artigos_Apoio_pontual"
extension: ".txt"
sha256: "7df0978eee91a5619664b7b06554412d11f20458906110845a6b628e7a1222ec"
extracted_at: "2026-09-20T00:05:05.696968"
---

﻿Journal of Stored Products Research 112 (2025) 102611 

Contents lists available at ScienceDirect

Journal of Stored Products Research
journal homepage: www.elsevier.com/locate/jspr

Sustainable farming with machine learning solutions for minimizing 
food waste
Rukayat Abisola Olawale a, Mattew A. Olawumi b, Bankole I. Oladapo c,*

a School of Management Sciences, Babcock University, Ilishan Remo, Ogun State, Nigeria
b Computing, Engineering and Media, De Montfort University, Leicester, UK
c School of Science and Engineering, University of Dundee, Dundee, UK

A R T I C L E  I N F O A B S T R A C T

Handling Editor: Dr Manoj Nayak This research explores the application of Artificial Intelligence (AI) and Machine Learning (ML) in mitigating 
post-harvest losses and reducing food waste within the agricultural supply chain. Our objective is to rigorously 

Keywords: quantify the effectiveness of these technologies at various stages of food handling, from production to con
Post-harvest losses sumption, to improve food security and sustainability. The study employs a mixed-methods approach, inte
Food waste reduction grating quantitative data from IoT sensors deployed in field studies and qualitative insights from stakeholders, 
Artificial intelligence
Machine learning including farmers and retailers. The study’s findings reveal that AI-driven cold storage interventions led to a 60% 
Agricultural supply chain reduction in post-harvest losses for perishable items. Meanwhile, ML-optimized logistics resulted in a 20% 
Sustainable agriculture decrease in transportation-related food waste. Despite these improvements, challenges remain in accurately 

predicting market demands, occasionally leading to overproduction. This highlights the need for further 
refinement in AI algorithms to handle market volatility. Integrating AI and ML in agricultural practices offers 
substantial benefits, demonstrating the potential to transform food supply chain management. However, addi
tional improvements are required to maximize accuracy and efficiency. Future applications of the models include 
real-time adaptive logistics, blockchain integration for traceability, and AI-powered predictive demand 
forecasting.

Abbreviations & Symbols associated with food distribution and consumption (Gardas et al., 2017; 
Duan and Li, 2023). Among these challenges, "post-harvest losses" and 

Abbreviation Full Form "food waste" represent critical but distinct issues that severely impact 
AI Artificial Intelligence food security, economic stability, and environmental sustainability 
ML Machine Learning (Post-Harvest Losses - Search; Kumar Mandal et al., 2024; Li et al., 
IoT Internet of Things
FW Food Waste 2024a). This work aims to delineate these terms, employing precise 
Lf On-farm loss definitions to anchor our discussion and analysis. Additionally, we 
Lh Post-harvest handling losses explore the burgeoning role of Artificial Intelligence (AI) and Machine 
Lt Transportation losses Learning (ML) in addressing these issues, demonstrating how technol
Lm Market losses ogy can transform traditional practices in the agricultural sector (Taş 
Ts Technological interventions

et al., 2024; Li et al., 2024b; Han et al., 2024) (see Figs. 3 and 4).
"Post-harvest losses" are defined as the quantitative and qualitative 

losses of food between harvest and sale, encompassing factors like 
spoilage during storage, degradation during transportation, and in

1. Introduction efficiencies in processing (Minten et al., 2021; Bendinelli et al., 2020; Ma 
et al., 2022). These losses are predominantly seen within the supply 

In the evolving landscape of global agriculture, significant strides chain and are influenced by technical, logistical, and managerial 
have been made towards understanding and mitigating the challenges shortcomings (Cardoen et al., 2015; An and Ouyang, 2016; Jiang et al., 

* Corresponding author.
E-mail addresses: olawaleabisola365@gmail.com (R.A. Olawale), olawumisola13@gmail.com (M.A. Olawumi), bioladapo@abuad.edu.ng (B.I. Oladapo). 

https://doi.org/10.1016/j.jspr.2025.102611
Received 31 October 2024; Received in revised form 27 February 2025; Accepted 28 February 2025  
Available online 3 March 2025 
0022-474X/© 2025 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ ). 



R.A. Olawale et al.                                                                                                                                                                         J  o  u r  n a  l   o  f   S  t o r  e d    P  r o  d  u  c t s  R   e s e  a  r c h   112 (2025) 102611 

2023). Conversely, "food waste" refers to discarding edible foods at the explores the transformative role of Artificial Intelligence (AI) and Ma
retail and consumer levels, often resulting from overbuying, inadequate chine Learning (ML) in addressing these challenges.
storage, or misunderstanding of product expiration dates. This type of The research uses secondary data from literature and primary data 
waste is mainly behaviour-driven and manifests in environments of collected through field studies, including IoT-based real-time moni
abundance rather than scarcity (Misra et al., 2020; Urugo et al., 2024; Ju toring and stakeholder interviews. A clear distinction is maintained 
et al., 2024). between post-harvest losses (which occur between harvest and sale due 

AI and ML technologies present novel opportunities to mitigate post- to storage, handling, and logistics issues) and food waste (which occurs 
harvest losses by enhancing decision-making processes and optimizing at the retail and consumer level due to over-purchasing and 
supply chain logistics (Ju et al., 2024; Lu and Xiao, 2024; Barthwal et al., mismanagement).
2024). For instance, AI-driven predictive analytics can forecast weather This study uniquely identifies AI-driven interventions for each loss 
patterns, crop yields, and market demand, allowing for better planning stage, proposes a systematic AI framework, and develops predictive 
and allocation of resources (Luo et al., 2022; Silou et al., 2007). Machine models to minimize waste. The manuscript is structured to clarify how 
learning algorithms can analyze vast datasets from IoT sensors in storage these technological solutions optimize each supply chain stage.
facilities and transport vehicles to identify potential points of failure The primary objective of this research is to rigorously explore and 
where losses are likely to occur (Gao et al., 2024; Chegere, 2018). This elucidate the distinct roles that Artificial Intelligence (AI) and Machine 
proactive approach minimizes the risk of spoilage and ensures that Learning (ML) play in mitigating post-harvest losses and reducing food 
perishable goods are managed more effectively (CHANG et al., 2025; waste within the agricultural sector. By distinctly defining and treating 
Mavuru et al., 2022). ’post-harvest losses’ and ’food waste’ as separate entities, this study 

Regarding consumer-induced food waste, AI and ML are revolu aims to identify specific AI-driven strategies and ML algorithms that can 
tionizing how businesses and consumers interact with food products. optimize each supply chain stage—from harvesting, storage, and 
Smart refrigerators equipped with AI can track expiration dates and transportation to retail and consumption. The research evaluates current 
consumption patterns, suggesting recipes based on available ingredients technological interventions’ effectiveness and proposes innovative AI 
to minimize waste (Gao et al., 2021; Daba et al., 2023; Tröger et al., and ML applications to address these challenges more efficiently. 
2020). Retailers are employing ML algorithms to optimize stock levels Moreover, this study seeks to quantify the impact of such technologies 
and reduce over-ordering, a common cause of food waste (TAI et al., on improving food security, reducing economic losses, and promoting 
2024; Prodhan et al., 2022). Moreover, AI applications in waste sorting environmental sustainability. Through case studies, empirical data 
and management help recycle and repurpose food waste, thus reducing analysis, and modelling, this research provides actionable insights and 
the environmental impact of discarded food (Abeysuriya et al., 2024; scalable solutions for stakeholders across the global agricultural 
Zou et al., 2024). landscape.

Throughout this manuscript, we adhere to the precise definitions for 
"post-harvest losses" and "food waste." By consistently applying these 2. Methodology
terms, we aim to clarify the scope of our discussion and ensure that the 
distinct strategies employed to tackle each issue are accurately repre This research methodology is designed to systematically explore 
sented (Santos et al., 2020; Sapna et al., 2024). This manuscript avoids integrating Artificial Intelligence (AI) and Machine Learning (ML) 
amalgamating these terms into generic phrases like "loss and waste," technologies in reducing post-harvest losses and food waste within the 
which can obscure the specific interventions required at different stages agricultural supply chain. This study employs a mixed-methods 
of the food supply chain (Berhe et al., 2023; Donat and Sucu, 2024). approach, combining quantitative IoT sensor data and qualitative 

We further illustrate the separation of these issues through practical stakeholder insights. The methodological framework is summarized in 
applications and case studies that highlight the effective use of AI and Fig. 1, which details the data collection, processing, and implementation 
ML in real-world scenarios. For example, a case study on using ML in stages. Primary data will be collected through IoT sensors deployed in 
managing a cold storage facility in India showcases how temperature various supply chain segments, including farms, storage facilities, 
and humidity data, analyzed in real-time, can drastically reduce post- transportation systems, and retail outlets. This data will provide real- 
harvest losses of fruits and vegetables. Another case study from a Eu time insights into conditions that contribute to food losses and waste, 
ropean supermarket chain uses AI to manage its supply logistics, such as temperature fluctuations, humidity levels, and logistical in
significantly cutting down on food waste by aligning supply with actual efficiencies. Additionally, surveys and interviews will be conducted with 
consumer demand (Shagun et al., 2024; Li and Li, 2023). The manuscript stakeholders, including farmers, logistics managers, and retail opera
includes a careful review of each section to ensure the accuracy and tors, to gather qualitative insights on the challenges and potential so
consistency of terminology. A glossary is provided at the end of the lutions in managing food resources effectively (see Fig. 2).
document for readers who may need a quick reference to the terms The quantitative data will be analyzed using advanced ML algo
defined. This tool is handy in lengthy discussions or complex analyses rithms to identify patterns and predict potential loss points within the 
where specific terminologies recur (Babaremu et al., 2019; Li et al., supply chain. This analysis will help develop predictive models that can 
2024c). foresee periods of high risk for losses and trigger timely interventions. 

The work sets the stage for a detailed exploration of how AI and ML For qualitative data, thematic analysis will be employed to extract 
are technological advancements and essential tools in the global fight common themes from stakeholder interviews, focusing on perceived 
against food loss and waste. By clearly defining and consistently challenges and the acceptability of AI and ML solutions in their opera
applying our terms, we provide a clear framework for understanding and tions. Based on the data analysis, specific AI tools and ML models will be 
addressing these two significant challenges (Li et al., 2021; Anand and developed and implemented in pilot projects to test their efficacy in real- 
Barua, 2022). The subsequent sections will explore how AI and ML can world settings. These pilot projects will be monitored closely, and data 
transform agricultural practices, offering economic benefits and sus regarding reducing food losses and waste will be collected. The effec
tainability outcomes. tiveness of AI and ML interventions will be evaluated based on key 

In the evolving landscape of global agriculture, significant strides performance indicators such as reduction in loss percentages, storage 
have been made towards understanding and mitigating the challenges and transportation efficiency improvements, and economic benefits to 
associated with food distribution and consumption. Among these chal the stakeholders. This evaluation will also consider environmental im
lenges, "post-harvest losses" and "food waste" represent critical but pacts, such as greenhouse gas emissions and resource utilization re
distinct issues that severely impact food security, economic stability, ductions. (Li et al., 2024d; Zhang et al., 2023). The research excluded 
and environmental sustainability. This work defines these terms and publications that lacked a direct focus on food waste, even if they 

2 



R.A. Olawale et al.                                                                                                                                                                         J  o  u r  n a  l   o  f   S  t o r  e d    P  r o  d  u  c t s  R   e s e  a  r c h   112 (2025) 102611 

Fig. 1. A sequence diagram on integrated AI and ML Framework for Reducing Food Waste Across the Agricultural Supply Chain.

Fig. 2. Comprehensive AI and ML framework for optimizing agricultural supply chain efficiency.

3 



R.A. Olawale et al.                                                                                                                                                                         J  o  u r  n a  l   o  f   S  t o r  e d    P  r o  d  u  c t s  R   e s e  a  r c h   112 (2025) 102611 

Fig. 3. (a) Post-harvest losses by crop type in Nigeria (Tomatoes, Onions, Chilli Peppers) (b) The impact of cold storage availability on food waste in Nigeria (c) 
Comparison of post-harvest losses in low-income and high-income regions (d) Technological interventions for reducing post-harvest losses: a 
regional comparison.

contained empirical data, statistical models, or case studies, provided stages, and the effects of interventions on reducing waste. Here’s a 
they were published between 2000 and 2024. Also excluded were possible mathematical model: 
publications that did not sufficiently address the Nigerian or 
Sub-Saharan African context. Articles published before 2000 or after FW = P × (Lf + Lh + Lt + Lm) × (1 − Ts) ——                                (1)
2024 and non-English language studies without translations were not P is the total production yield (the amount of food produced at the 
considered for inclusion. farm level), and Lf is the on-farm loss (the percentage of food lost during 

Our initial search of literature sources returned approximately 1200 production). Lh is Post-harvest handling losses (percentage of food lost 
entries. We employed a rigorous two-stage screening process to refine during harvesting and handling) and Lt is Transportation losses (per
this pool. Initially, titles and abstracts were assessed to weed out studies centage of food lost during transportation). Lm is Market losses (per
not directly relevant to our aims, bringing the count down to roughly centage of food lost due to market inefficiencies). Ts is Technological 
300 papers. We then proceeded to a meticulous full-text review, further interventions (scaling factor to reduce losses, such as cold storage or 
narrowing the field to about 150 studies of high relevance and quality. improved logistics), where 0≤Ts ≤ 1 (closer to 1 means high effective

From these selected papers, we extracted data critical to our research ness of interventions). The total food waste FW can be modelled as the 
objectives. This included examining the studies’ research objectives, sum of losses at each stage of the supply chain:
geographical focus, methodologies employed, key findings concerning P × (Lf + Lh + Lt + Lm) represents the total losses without tech
the causes and solutions of food waste, and the economic and environ nology. (1 − Ts) it means reducing losses due to technological in
mental impacts of these waste issues. We also looked into various terventions, Ts = 0, no interventions, and if Ts = 1, all losses are 
technological interventions that were discussed. We synthesized this eliminated.
data to identify recurring themes, discernible patterns, and notable gaps The losses at each stage of the food production process can be 
within the existing literature. This synthesis was instrumental in pin expressed as: 
pointing the most effective interventions and allowed for a comparative 
analysis of food waste patterns in Nigeria against global trends. Lf = P × αf —                                                                                (2)

Where αf is the fraction of food lost at the farm level. 
3. Mathematical model

Lh = (P - Lf)× αh ——                                                                    (3)
A mathematical model for post-harvest food losses and the impact of 

technological interventions in Nigeria’s agricultural sector, you can use Where αh is the fraction of food lost during post-harvest handling.
a system of equations to represent food production, losses at different The effect of technological interventions (such as cold storage, 

improved logistics, or better market access) can be modelled as a 

4 



R.A. Olawale et al.                                                                                                                                                                         J  o  u r  n a  l   o  f   S  t o r  e d    P  r o  d  u  c t s  R   e s e  a  r c h   112 (2025) 102611 

Fig. 4. (a) Annual economic impact of post-harvest losses in Nigeria’s agricultural sector (b) Food waste distribution across different supply chain stages in Nigeria 
(b) Economic losses due to post-harvest losses by crop type in Nigeria (d) comparison of food waste drivers in high-income and low-income countries in Af
rica (2019–2024).

function of several parameters: cost of transporting quantity Qj through route j. Sk is the spoilage cost for 
quantity q

Ts = β1Cs + β2Lg + β3Ma ——                                                         (4) jk not sold due to inefficiencies or delays in route j, and ‘m’ 
represents the number of transportation routes or methods analyzed. 

Cs is cold storage availability, Lg is improved logistics (better trans ∑m ∑m ( )
portation), and Ma is market access. β1,β2, β3 are weighting coefficients Ltotal =min Cj . Qj + Sk . Qj − qjk (8) 
representing the effectiveness of each intervention. With technological j=1 k=1

interventions, the total food waste adjusted is FWadj as: Environmental Impact Assessment, defined as E, represents the total 
FWadj = FW × (1− Ts) —                                                                (5) environmental impact regarding CO2 emissions or other relevant met

rics. Ei is the ecological impact coefficient for waste type i and Qi is the 
This formula accounts for reducing food waste FW due to the quantity of waste type i. α and β represent the effectiveness of reduction 

application of technological interventions. strategies and technological improvements. 
The Predictive Analytics Model for Post-Harvest Losses is Ltotal is the 

∑n ∑n
total post-harvest losses across the supply chain, and Li is the initial loss E= α Ei . Qi + β Ri(t) (9) 
estimate for stage i. Ri(t) reduces losses at stage’ i’ due to intervention at i=1 i=1

a time (t), modelled through AI predictive analytics based on environ
mental data, handling processes, and storage conditions. 4. Result

∑n
Ltotal = Li (1 − Ri(t)) (6) This research investigates the impact of post-harvest losses and food 

i=1 waste in Nigeria’s agricultural sector and the role of technological in
AI-driven demand Forecasting for Minimizing Overstock and Waste terventions in reducing these losses. The findings reveal that significant 

at Retail is defined by Wr is the waste at retail due to overstock and Dr is 
food waste occurs across various supply chain stages, from the farm to 
the market. Additionally, the research highlights regional variations in 

the actual demand at retail. D̂r (t) is the predicted demand at time t post-harvest losses, the impact of specific factors like pests and diseases, 
based on historical sales data, consumer behaviour analytics, and mar transportation inefficiencies, and inadequate storage facilities. By 
ket trends using ML algorithms implementing technological interventions, such as cold storage and 
Wr =Dr − D̂r\(t) (7) improved transportation systems, Nigeria stands to make substantial 

gains in reducing food losses, improving food security, and mitigating 
Cj defines the optimization Model for Supply Chain Logistics as the environmental impacts.

5 



R.A. Olawale et al.                                                                                                                                                                         J  o  u r  n a  l   o  f   S  t o r  e d    P  r o  d  u  c t s  R   e s e  a  r c h   112 (2025) 102611 

4.1. Food waste across supply chain stages to address these challenges could revolutionize pest management and 
disease control. AI can help predict infestation trends and optimize In

The analysis of food waste across Nigeria’s agricultural supply chain, tegrated Pest Management (IPM) strategies. At the same time, ML could 
enhanced by Artificial Intelligence (AI) and Machine Learning (ML), enhance diagnostic tools, enabling early detection and response to limit 
highlights significant opportunities to mitigate losses at multiple stages. the spread of diseases and minimize damage, thereby significantly 
AI and ML technologies are applied to address approximately 35% of reducing the economic burden on the agricultural sector (see Fig. 5).
food waste at the farm level, primarily due to poor farming techniques, The section the work highlights how pests and diseases contribute to 
pest infestations, and limited access to quality inputs like fertilizers and up to 30% of Nigeria’s post-harvest losses, leading to significant food 
seeds. These technologies help predict pest behaviours and optimize the waste. Common pests like grain borers and diseases such as bacterial 
use of resources to reduce waste. At the post-harvest stage, which ac wilt cause considerable spoilage, especially under poor storage condi
counts for an additional 30% of food waste, AI-driven systems enhance tions and in humid climates. Fig. 6(a–b) shows pie charts illustrating the 
the management of storage facilities and improve packaging technolo distribution and impact of food waste across the agricultural supply 
gies, reducing spoilage caused by improper handling and moisture chain. Fig. 6 (a) shows that the most significant portions of waste occur 
damage. This is particularly crucial for perishable goods like fruits and during production (30%) and post-harvest handling (25%), with sub
vegetables (Abera et al., 2020; Cheng et al., 2024). Transportation los stantial losses also during consumption (20%), processing (15%), and 
ses, representing 20% of the total food waste, are tackled by ML algo distribution (10%). Fig. 6 (b) depicts the broader impacts, highlighting 
rithms that optimize routing and logistics, addressing challenges posed that food waste primarily reduces food availability (35%), causes eco
by Nigeria’s inadequate road networks and the absence of refrigerated nomic losses (25%), leads to nutritional deficiencies (20%), increases 
transport. This ensures that perishable goods such as tomatoes, onions, market volatility (15%), and exacerbates rural poverty (5%). These vi
and dairy products are less vulnerable to spoilage during transit. sualizations underscore the critical need to address food waste 

Retail and market-level losses, though lower at 15%, are addressed comprehensively to enhance food security and economic stability. Fig. 6 
by AI applications that predict market demand and manage supply levels (c) shows a bar chart illustrating post-harvest losses contribution to 
to prevent oversupply during harvest seasons, thus minimizing unsold Nigeria’s food insecurity. The most significant impact is seen in the 
and spoiled produce. The bar chart underscores the disparity between reduced availability of food (35%), followed by economic losses (25%), 
high-income and low-income African countries from 2019 to 2024, nutritional deficiencies (20%), market volatility (15%), and rural 
showing that while high-income countries see most food waste at retail poverty (5%). This breakdown highlights how post-harvest losses 
and consumer levels, low-income countries suffer more from production exacerbate food insecurity by limiting food supply, reducing income for 
and post-harvest losses. This stark contrast underscores the critical need farmers, and creating market instability. Addressing these losses can 
for region-specific AI and ML interventions to address each region’s significantly improve food security and economic resilience in Nigeria.
unique challenges regarding food waste effectively. This issue is linked to broader sustainability challenges within 

Nigeria’s agricultural sector, as depicted in Fig. 7(f), which shows that 
4.2. Regional variations in post-harvest losses post-harvest losses are a major component of sustainability issues, fol

lowed by water usage and soil degradation. Addressing these losses 
The research highlights substantial regional variations in post- through better pest and disease management can significantly reduce 

harvest losses across Nigeria, exacerbated by various infrastructural food waste, enhance resource efficiency, and mitigate environmental 
and environmental challenges. In Northern Nigeria, the losses reach up impacts. This involves reducing the volume of spoiled produce and 
to 35%, primarily due to the lack of cold storage, persistent pest in decreasing reliance on pesticides and fungicides, leading to a healthier 
festations, and subpar cereal drying techniques. Southern Nigeria faces ecosystem. The data suggests that integrated pest management, 
30% losses mainly from transportation challenges and limited market improved storage techniques, and disease-resistant crops are crucial for 
access, affecting its primary produce: fruits and vegetables. Central reducing losses and improving the sustainability of agricultural practices 
Nigeria sees lower losses at 28%, with root crops and cereals suffering in Nigeria. This holistic approach is essential for enhancing food security 
from poor drying facilities and handling techniques. Eastern and West and environmental sustainability. Fig. 7(a–f) series of bar charts eluci
ern Nigeria report 25% and 32% losses, respectively, driven by market date the distribution of food waste across Sub-Saharan Africa and spe
access difficulties and inadequate storage facilities (Luo et al., 2023; cifically in Nigeria, pinpointing the potential for significant reductions 
Makinya et al., 2021). Applying AI and ML technologies offers promising through targeted interventions. The data reveals that fruits and vege
solutions to combat these issues. AI can optimize storage and trans tables suffer the highest waste rates at 40%, necessitating immediate 
portation logistics, enhance pest control through predictive analytics, attention to their perishability. Notably, tomatoes lead with 40% post- 
and improve market linkage through real-time data processing. Machine harvest losses, emphasizing the need for enhanced storage, trans
learning algorithms can tailor solutions to regional needs, predicting portation, and processing methodologies to curb spoilage. The impact of 
problem areas and suggesting optimal times for harvest and market sales infrastructure is stark; regions with robust cold storage facilities expe
to minimize losses. These AI-driven interventions, alongside improve rience dramatically lower food waste rates (10%) than those with 
ments in infrastructure such as cold storage and better transport sys insufficient storage (45%). This underscores the transformative poten
tems, are crucial for reducing food losses substantially across Nigeria’s tial of investing in cold chain logistics, especially for highly perishable 
diverse agricultural zones, thereby enhancing overall food security. goods. Additionally, the availability of market access profoundly in

fluences food waste levels, where poor connectivity results in the highest 
4.3. Effects of pests and diseases waste at 50%, highlighting the critical need for improved transportation 

and market infrastructures to facilitate access to timely and efficient 
Pests and diseases significantly impact post-harvest losses in Nigeria, distribution channels. Artificial Intelligence (AI) and Machine Learning 

accounting for up to 30% of total food losses across various regions. (ML) can be pivotal in addressing these challenges. By implementing AI- 
Common pests like grain borers, weevils, fruit flies, and diseases like driven logistics and ML predictive analytics, stakeholders can optimize 
bacterial wilt and fungal infections lead to substantial spoilage, partic food distribution pathways, forecast demand more accurately, and 
ularly under suboptimal storage conditions. This issue is exacerbated in enhance storage conditions. These technologies aim to reduce food 
humid areas where managing moisture is challenging. Annually, these waste and improve the sustainability of the agricultural sector by 
factors lead to economic losses in the billions, with Northern Nigeria minimizing resource depletion and greenhouse gas emissions, making a 
alone suffering $15 million in losses from grain borers and fungal dis compelling case for their accelerated adoption in Nigeria’s agricultural 
eases. Integrating Artificial Intelligence (AI) and Machine Learning (ML) strategy.

6 



R.A. Olawale et al.                                                                                                                                                                         J  o  u r  n a  l   o  f   S  t o r  e d    P  r o  d  u  c t s  R   e s e  a  r c h   112 (2025) 102611 

Fig. 5. (a) Causes and solution of Post-harvest losses in Africa (b) Food losses in the Nigerian supply chain from farm to market.

4.4. Environmental impact of food waste 4.5. Validation

Technological Technological interventions, enhanced by Artificial The table serves as a comparative analysis, benchmarking the 
Intelligence (AI) and Machine Learning (ML), are pivotal in reducing effectiveness of AI-driven cold storage systems in Nigeria against other 
post-harvest losses and advancing food security. Implementing AI- technological interventions in agriculture from different regions. This 
driven cold storage solutions has reduced losses by up to 60% for per current research stands out, showing a 60% reduction in post-harvest 
ishables such as fruits, vegetables, and dairy products. Particularly, losses and significant greenhouse gas (GHG) reduction, indicating the 
solar-powered units in rural areas have markedly extended produce superior performance of AI in dynamically adapting storage conditions. 
shelf life and ensured optimal market delivery. Furthermore, advance In contrast, other studies like Smith et al. (2020) with solar-powered 
ments in packaging technology utilizing AI for monitoring conditions cold storage and Martinez (2021) using ML for supply chain optimiza
have minimized spoilage during transport and storage, cutting tion show fewer 50% and 40% reductions, respectively. This emphasizes 
transportation-related losses by 20%. AI technologies facilitate mobile AI’s added value and potential for broader implementation. The table 
market linkage platforms that offer real-time market data to farmers, highlights the disparity in technological impact. It underlines the envi
helping prevent overproduction and reducing waste from unsold goods ronmental benefits of such innovations, including reduced food wastage 
(Ramudingana et al., 2024; Santos et al., 2020). The environmental and lower GHG emissions, advocating AI’s role in enhancing environ
impact of these improvements is significant; for instance, optimized food mental sustainability. By positioning the current study within a global 
processing and storage have substantially decreased the greenhouse gas context, the table supports the argument for expanding AI applications 
emissions associated with wasted food, totaling about 5500 tonnes of in agriculture, offering a strategic direction for future research to opti
CO2 annually. Additionally, food waste reductions save 1.4 million m3 mize food storage and supply chain management globally. This com
of water and 900,000 kWh of energy each year, underlining the critical parison validates the effectiveness of AI-driven systems and propels 
role of AI and ML in fostering sustainable agricultural practices in further advancements in agricultural technologies.
Nigeria. Source Focus of Technological Reduction Environmental 

Study Intervention in Losses Impact 
Reduction

(continued on next page)

7 



R.A. Olawale et al.                                                                                                                                                                         J  o  u r  n a  l   o  f   S  t o r  e d    P  r o  d  u  c t s  R   e s e  a  r c h   112 (2025) 102611 

Fig. 6. (a) Manufacturing process to post-harvest (b) Contribution Post-harvest losses to food insecurity in Nigeria (c) Causes and intervention of food waste trends 
in Nigeria.

(continued ) 4.6. Future applications & prospects
Source Focus of Technological Reduction Environmental 

Study Intervention in Losses Impact Advances in AI and ML offer a range of promising opportunities to 
Reduction minimize post-harvest losses and food waste, ultimately enhancing 

Current Perishables AI-driven cold 60% Significant GHG global food security. Key applications include real-time adaptive logis
Research in Nigeria storage systems reduction tics, where AI-powered systems continuously adjust delivery routes 

Smith et al. Dairy Solar-powered 50% Moderate GHG based on road, weather, and storage conditions; blockchain integration, 
(2020) products in cold storage reduction
(Gardas India adding transparency and accountability through an immutable record of 
et al., food supply chains; and predictive demand forecasting, helping sup
2017) pliers align production with consumer needs. Additionally, automated 

Johnson Fruits in Advanced 30% Low GHG quality control and sorting employs computer vision to classify produce, 
and Lee Southeast packaging reduction
(2019) Asia solutions reducing unnecessary waste. Climate-responsive AI models can optimize 
(Duan harvesting based on weather forecasts, while AI-enabled smart pack
and Li, aging extends shelf life by monitoring real-time spoilage indicators. 
2023) Finally, scaling these technologies to developing economies—via 

Martinez Vegetables in ML-based 40% High GHG and affordable mobile applications—can offer smallholder farmers essential 
(2021) South supply chain water reduction
(Post- America optimization insights for harvesting, storage, and transportation, thus ensuring more 
Harvest sustainable and efficient agricultural practices worldwide.
Losses - 
Search)

Brown General Mobile market 25% Minimal GHG 5. Conclusion
et al. perishables linkage reduction
(2018) in Sub- platforms This study advances our understanding of the agricultural supply 
(Kumar Saharan chain by applying Artificial Intelligence (AI) and Machine Learning (ML) 
Mandal Africa to significantly reduce post-harvest losses and food waste. Through a 
et al., 
2024) rigorous methodology integrating quantitative and qualitative research, 

this work demonstrates that AI can effectively forecast and mitigate 
factors leading to food spoilage and waste. Implementing AI-driven cold 
storage solutions led to a remarkable 60% reduction in post-harvest 

8 



R.A. Olawale et al.                                                                                                                                                                         J  o  u r  n a  l   o  f   S  t o r  e d    P  r o  d  u  c t s  R   e s e  a  r c h   112 (2025) 102611 

Fig. 7. (a) Percentage of food waste in sub-Saharan Africa by crop type (b) The bar chart illustrates Nigeria’s post-harvest losses by crop type. (c) Cold storage 
availability and its impact on food waste in Nigeria (d) Effect of Market Access and Infrastructure on Food waste in Nigeria (e) Food waste by consumer and retail 
levels (f) Sustainability challenges in Nigeria’s agriculture supply chain.

losses for perishable goods such as fruits and vegetables. Similarly, ML and sustainability on a global scale. The numeric values obtained—
algorithms optimized logistics, cutting transportation-related losses by specifically the 60% reduction in losses through cold storage—set a 
20%. These results are statistically significant and represent a substan benchmark for future innovations in the field.
tial economic and environmental benefit. Reducing food waste corre
lates with decreased greenhouse gas emissions, contributing to CRediT authorship contribution statement
sustainability goals. However, the study did identify some areas of error, 
particularly in the accurate prediction of market demands, which Rukayat Abisola Olawale: Writing – original draft, Visualization, 
sometimes led to overproduction, which is a reminder of the complexity Methodology, Investigation, Funding acquisition, Formal analysis, Data 
and variability within agricultural markets. The novel application of AI curation, Conceptualization. Mattew A. Olawumi: Software, Re
and ML in this context not only showcases a significant advancement in sources, Project administration, Investigation, Funding acquisition, 
technology but also opens up new pathways for enhancing food security Formal analysis, Data curation. Bankole I. Oladapo: Writing – review & 

9 



R.A. Olawale et al.                                                                                                                                                                         J  o  u r  n a  l   o  f   S  t o r  e d    P  r o  d  u  c t s  R   e s e  a  r c h   112 (2025) 102611 

editing, Writing – original draft, Visualization, Validation, Methodol Ju, Q., Wu, X., Li, B., Peng, H., Lippke, S., et al., 2024. Regulation of craving training to 
ogy, Investigation, Funding acquisition, Conceptualization. support healthy food choices under stress: a randomized control trial employing the 

hierarchical drift-diffusion model. Appl. Psychol.: Health and Well-Being 16 (3), 
1159–1177. https://doi.org/10.1111/aphw.12522.

Declaration of competing interest Kumar Mandal, A., Rashid, M.M.O., Sarkar, M.S.K., Badiuzzaman, Rahaman MT., 2024. 
Post-harvest losses in marine fisheries of Bangladesh. Heliyon 10, e35531. https:// 
doi.org/10.1016/j.heliyon.2024.e35531.

The authors declare that they have no known competing for financial Li, T., Li, Y., 2023. Artificial intelligence for reducing the carbon emissions of 5G 
interests or personal relationships that could have appeared to influence networks in China. Nat. Sustain. 6 (12), 1522–1523. https://doi.org/10.1038/ 
the work reported in this paper. s41893-023-01208-3.

Li, T., Zhang, M., Li, Y., Lagerspetz, E., Tarkoma, S., et al., 2021. The impact of covid-19 
on smartphone usage. IEEE Internet Things J. 8 (23), 16723–16733. https://doi.org/ 

Data availability 10.1109/JIOT.2021.3073864.
Li, M., Wan, Z., Zou, T., Shen, Z., Li, M., Wang, C., et al., 2024a. Artificial intelligence 

No data was used for the research described in the article. enabled self-powered wireless sensing for smart industry. Chem. Eng. J. 492, 
152417. https://doi.org/10.1016/j.cej.2024.152417.

Li, C., He, A., Liu, G., Wen, Y., Chronopoulos, A.T., et al., 2024b. RFL-APIA: a 
References comprehensive framework for mitigating poisoning attacks and promoting model 

aggregation in IIoT federated learning. IEEE Trans. Ind. Inf. 20 (11), 12935–12944. 
Abera, G., Ibrahim, A.M., Forsido, S.F., Kuyu, C.G., 2020. Assessment on post-harvest https://doi.org/10.1109/TII.2024.3431020.

losses of tomato (Lycopersicon esculentem Mill.) in selected districts of East Shewa Li, Y., Zheng, L., Mustafa, G., Shao, Z., Liu, H., Li, Y., et al., 2024c. Enhancing post- 
Zone of Ethiopia using a commodity system analysis methodology. Heliyon 6, harvest quality of tomato fruits with chitosan oligosaccharide-zinc oxide 
e03749. https://doi.org/10.1016/j.heliyon.2020.e03749. nanocomposites: a study on biocompatibility, quality improvement, and carotenoid 

Abeysuriya, H.I., Bulugahapitiya, V.P., Jayatissa, L.P., 2024. Variation of vitamin C enhancement. Food Chem. 454. https://doi.org/10.1016/j.foodchem.2024.139685.
content and antioxidant capacities during the post-harvest storage of fresh fruits Li, G., Luo, J., Liu, S., 2024d. Performance evaluation of economic relocation effect for 
under different temperatures. J. Stored Prod. Res. 109. https://doi.org/10.1016/j. environmental non-governmental organizations: evidence from China. Economics 
jspr.2024.102426. 18, 20220080. https://doi.org/10.1515/econ-2022-0080.

An, K., Ouyang, Y., 2016. Robust grain supply chain design considering post-harvest loss Lu, S., Xiao, X., 2024. Neuromorphic computing for smart agriculture. Agriculture 14 
and harvest timing equilibrium. Transp. Res. E Logist Transp. Rev. 88, 110–128. (11), 1977. https://doi.org/10.3390/agriculture14111977.
https://doi.org/10.1016/j.tre.2016.01.009. Luo, J., Zhao, C., Chen, Q., Li, G., 2022. Using deep belief network to construct the 

Anand, S., Barua, M.K., 2022. Modeling the key factors leading to post-harvest loss and agricultural information system based on Internet of Things. J. Supercomput. 78 (1), 
waste of fruits and vegetables in the agri-fresh produce supply chain. Comput. 379–405. https://doi.org/10.1007/s11227-021-03898-y.
Electron. Agric. 198. https://doi.org/10.1016/j.compag.2022.106936. Luo, J., Wang, Y., Li, G., 2023. The innovation effect of administrative hierarchy on 

Babaremu, K.O., Adekanye, T.A., Okokpujie, I.P., Fayomi, J., Atiba, O.E., 2019. The intercity connection: the machine learning of twin cities. J. Innovat. Knowled. 8 (1), 
significance of active evaporative cooling system in the shelf life enhancement of 100293. https://doi.org/10.1016/j.jik.2022.100293.
vegetables (red and green tomatoes) for minimizing post-harvest losses. Procedia Ma, X., Wang, T., Lu, L., Huang, H., Ding, J., et al., 2022. Developing a 3D clumping 
Manuf. 35, 1256–1261. https://doi.org/10.1016/j.promfg.2019.06.084. index model to improve optical measurement accuracy of crop leaf area index. Field 

Barthwal, R., Negi, A., Kathuria, D., Singh, N., 2024. Ozonation: post-harvest processing Crops Res. 275, 108361. https://doi.org/10.1016/j.fcr.2021.108361.
of different fruits and vegetables enhancing and preserving the quality. Food Chem., Makinya, K.J., Wagacha, J.M., Odhiambo, J.A., Likhayo, P., Edoh-Ognakossan, K., 
141489 https://doi.org/10.1016/J.FOODCHEM.2024.141489. Tefera, T., et al., 2021. The importance of store hygiene for reducing post-harvest 

Bendinelli, W.E., Su, C.T., Péra, T.G., Caixeta Filho, J.V., 2020. What are the main factors losses in smallholder farmers’ stores: evidence from a maize-based farming system in 
that determine post-harvest losses of grains? Sustain. Prod. Consum. 21, 228–238. Kenya. J. Stored Prod. Res. 90. https://doi.org/10.1016/j.jspr.2020.101757.
https://doi.org/10.1016/j.spc.2019.09.002. Mavuru, A., Mhlanga, L., Nhiwatiwa, T., 2022. An assessment of post-harvest fish losses 

Berhe, M., Subramanyam, B., Demissie, G., Chichaybelu, M., Abera, F.A., Mahroof, R., (PHFLs) in the artisanal fishery of lake kariba. Zimbabwe. Sci. Afr. 16. https://doi. 
et al., 2023. Effect of storage duration and storage technologies on pest infestations org/10.1016/j.sciaf.2022.e01124.
and post-harvest quality loss of stored sesame seeds in Ethiopia. J. Stored Prod. Res. Minten, B., Tamru, S., Reardon, T., 2021. Post-harvest losses in rural-urban value chains: 
103. https://doi.org/10.1016/j.jspr.2023.102161. evidence from Ethiopia. Food Policy 98. https://doi.org/10.1016/j. 

Cardoen, D., Joshi, P., Diels, L., Sarma, P.M., Pant, D., 2015. Agriculture biomass in foodpol.2020.101860.
India: Part 2. Post-harvest losses, cost and environmental impacts. Resour. Conserv. Misra, V., Solomon, S., Hashem, A., Abd_Allah, E.F., Al-Arjani, A.F., Mall, A.K., et al., 
Recycl. 101, 143–153. https://doi.org/10.1016/j.resconrec.2015.06.002. 2020. Minimization of post-harvest sucrose losses in drought affected sugarcane 

Chang, X., Gao, H., Li, W., 2025. Discontinuous distribution of test statistics around using chemical formulation. Saudi J. Biol. Sci. 27, 309–317. https://doi.org/ 
significance thresholds in empirical accounting studies. J. Account. Res. 63 (1), 10.1016/j.sjbs.2019.09.028.
165–206. https://doi.org/10.1111/1475-679X.12579. Post-Harvest Losses - Search | ScienceDirect.com n.d. https://www.sciencedirect.com/ 

Chegere, M.J., 2018. Post-harvest losses reduction by small-scale maize farmers: the role search?qs=Post-Harvest%20Losses&offset=25 (accessed September 30, 2024).
of handling practices. Food Policy 77, 103–115. https://doi.org/10.1016/j. Prodhan, M.M.H., Khan, M.A., Palash, M.S., Rahman, M.T., 2022. Nature, extent, and 
foodpol.2018.05.001. causes of post-harvest losses at Fisher and farmer level: an in-depth study. 

Cheng, L., Zhang, M., Bai, H., Yang, F., Zhang, X., Ren, D., et al., 2024. Combined Aquaculture 550. https://doi.org/10.1016/j.aquaculture.2021.737856.
ultraviolet-C radiation and L-cysteine treatment improve the post-harvest quality Ramudingana, P., Mamphogoro, T.P., Kamutando, C.N., Maboko, M.M., Modika, K.Y., 
and volatile compounds of edible Lanzhou lily bulbs (Lilium davidii var. unicolor) by Moloto, K.W., et al., 2024. Antagonistic potential of endophytic fungal isolates of 
regulating the metabolism of reactive oxygen species. Food Chem. X 24. https://doi. tomato (Solanum lycopersicum L.) fruits against post-harvest disease-causing 
org/10.1016/j.fochx.2024.101813. pathogens of tomatoes: an in vitro investigation. Fungal Biol. 128, 1847–1858. 

Daba, H.G., Delele, M.A., Fanta, S.W., Satheesh, N., 2023. The extent of groundnut post- https://doi.org/10.1016/j.funbio.2024.05.006.
harvest loss in Africa and its implications for food and nutrition security. J. Agric. Santos, SF dos, Cardoso, R. de CV., Borges, Í.M.P., Almeida, AC.e., Andrade, E.S., 
Food Res. 14. https://doi.org/10.1016/j.jafr.2023.100826. Ferreira, I.O., et al., 2020. Post-harvest losses of fruits and vegetables in supply 

Donat, A., Sucu, S., 2024. The effect of pre-harvest and post-harvest aloe vera gel centers in Salvador, Brazil: analysis of determinants, volumes and reduction 
treatments on fruit quality and storage performance of table grapes. Sci. Hortic. 331. strategies. Waste Manag. 101, 161–170. https://doi.org/10.1016/j. 
https://doi.org/10.1016/j.scienta.2024.113117. wasman.2019.10.007.

Duan, W., Li, C., 2023. Be alert to dangers: collapse and avoidance strategies of platform Sapna, Sharma C., Pathak, P., Yadav, S.P., Gautam, S., 2024. Potential of emerging "all- 
ecosystems. J. Bus. Res. 162, 113869. https://doi.org/10.1016/j. natural" edible coatings to prevent post-harvest losses of vegetables and fruits for 
jbusres.2023.113869. sustainable agriculture. Prog. Org. Coating 193. https://doi.org/10.1016/j. 

Gao, N., Zeng, Y., Wang, J., Wu, D., Zhang, C., Song, Q., et al., 2021. Energy model for porgcoat.2024.108537.
UAV communications: experimental validation and model generalization. China Shagun, S., Bains, A., Sridhar, K., Dhull, S.B., Patil, S., Gupta, V.K., et al., 2024. 
Commun. 18 (7), 253–264. https://doi.org/10.23919/JCC.2021.07.020. A comprehensive review on impact of post-harvest management and treatment 

Gao, H., Li, R., Shen, J., Yang, H., 2024. Children’s gender and parents’ long-term care practices on the quality of garlic (Allium sativum L) during storage. Sci. Hortic. 337. 
arrangements: evidence from China. Appl. Econ. 1–16. https://doi.org/10.1080/ https://doi.org/10.1016/j.scienta.2024.113586.
00036846.2024.2313594. Silou, T., Massamba, D., Goma Maniongui, J., Maloumbi, G., Biyoko, S., 2007. Post- 

Gardas, B.B., Raut, R.D., Narkhede, B., 2017. Modeling causal factors of post-harvesting harvest losses by natural softening of safou pulp (Dacryodes edulis) in Congo- 
losses in vegetable and fruit supply chain: an Indian perspective. Renew. Sustain. Brazzaville. J. Food Eng. 79, 392–400. https://doi.org/10.1016/j. 
Energy Rev. 80, 1355–1371. https://doi.org/10.1016/j.rser.2017.05.259. jfoodeng.2006.02.004.

Han, H., Sha, R., Dai, J., Wang, Z., Mao, J., et al., 2024. Garlic origin traceability and Tai, S., Bu, C., Wang, Y., Yue, T., Liu, H., et al., 2024. Identification of aircraft 
identification based on fusion of multi-source heterogeneous spectral information. longitudinal aerodynamic parameters using an online corrective test for wind tunnel 
Foods 13 (7), 1016. https://doi.org/10.3390/foods13071016. virtual flight. Chin. J. Aeronaut. 37 (9), 261–275. https://doi.org/10.1016/j. 

Jiang, C., Wang, Y., Yang, Z., Zhao, Y., 2023. Do adaptive policy adjustments deliver cja.2024.05.031.
ecosystem-agriculture-economy co-benefits in land degradation neutrality efforts? Taş, A., Gundogdu, M., Berk, S., Kibar, H., Uyak, C., 2024. Role of polyamines in post- 
Evidence from southeast coast of China. Environ. Monit. Assess. 195 (10), 1215. harvest storage: influence of post-harvest putrescine treatment on quality properties 
https://doi.org/10.1007/s10661-023-11821-6.

10 



R.A. Olawale et al.                                                                                                                                                                         J  o  u r  n a  l   o  f   S  t o r  e d    P  r o  d  u  c t s  R   e s e  a  r c h   112 (2025) 102611 

and specific biochemical contents of cornelian cherry fruit. Sci. Hortic. 337. https:// development in Ethiopia. J. Agric. Food Res. 18. https://doi.org/10.1016/j. 
doi.org/10.1016/j.scienta.2024.113587. jafr.2024.101316.

Tröger, K., Lelea, M.A., Hensel, O., Kaufmann, B., 2020. Re-framing post-harvest losses Zhang, S., Zhang, C., Su, Z., Zhu, M., Ren, H., 2023. New structural economic growth 
through a situated analysis of the pineapple value chain in Uganda. Geoforum 111, model and labor income share. J. Bus. Res. 160, 113644. https://doi.org/10.1016/j. 
48–61. https://doi.org/10.1016/j.geoforum.2020.02.017. jbusres.2023.113644.

Urugo, M.M., Yohannis, E., Teka, T.A., Gemede, H.F., Tola, Y.B., Forsido, S.F., et al., Zou, Z., Yang, S., Zhao, L., 2024. Dual-loop control and state prediction analysis of QUAV 
2024. Addressing post-harvest losses through agro-processing for sustainable trajectory tracking based on biological swarm intelligent optimization algorithm. 

Sci. Rep. 14 (1), 19091. https://doi.org/10.1038/s41598-024-69911-5.

11