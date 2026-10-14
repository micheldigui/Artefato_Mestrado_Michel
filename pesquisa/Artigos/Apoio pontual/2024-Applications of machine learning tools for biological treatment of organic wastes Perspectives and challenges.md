---
source_file: "2024-Applications of machine learning tools for biological treatment of organic wastes Perspectives and challenges.txt"
original_rel_path: "Trabalhos\Artigos\Apoio pontual\txt\2024-Applications of machine learning tools for biological treatment of organic wastes Perspectives and challenges.txt"
category: "Artigos_Apoio_pontual"
extension: ".txt"
sha256: "5878dec54fdc566c466e6ed479f603b004c654c295372dd40dc7bfb22611a894"
extracted_at: "2026-09-20T00:05:05.637422"
---

﻿Circular Economy 3 (2024) 100088

lable at ScienceDirect
Contents lists avai
Circular Economy

journal homepage: www.journals .e lsevier .com/circular-economy
Review
Applications of machine learning tools for biological treatment
of organic wastes: Perspectives and challenges
Long Chen a, b, Pinjing He a, b, c, Hua Zhang a, b, c, Wei Peng a, b, c, Junjie Qiu a, b, c,
Fan Lü a, b, c, *

a State Key Laboratory of Pollution Control and Resource Reuse, College of Environmental Science and Engineering, Tongji University, Shanghai 200092,
China
b Institute of Waste Treatment and Reclamation, Tongji University, Shanghai 200092, China
c Shanghai Institute of Pollution Control and Ecological Security, Shanghai 200092, China
a r t i c l e i n f o

Article history:
Received 23 January 2024
Received in revised form
23 April 2024
Accepted 21 May 2024
Available online 31 May 2024

Keywords:
Anaerobic digestion
Composting
Insect farming
Machine learning
Process optimization
* Corresponding author. State Key Laboratory of Po
Reuse, College of Environmental Science and Eng
Shanghai 200092, China.

E-mail address: lvfan.rhodea@tongji.edu.cn (F. Lü)

https://doi.org/10.1016/j.cec.2024.100088
2773-1677/© 2024 The Author(s). Published by Elsev
creativecommons.org/licenses/by-nc-nd/4.0/).
a b s t r a c t

Biological treatment technologies (such as anaerobic digestion, composting, and insect farming) have
been extensively employed to handle various degradable organic wastes. However, the inherent
complexity and instability of biological treatment processes adversely affect the production of renewable
energy and nutrient-rich products. To ensure stable processes and consistent product quality, researchers
have invested heavily in control strategies for biological treatment, with machine learning (ML) recently
proving effective in optimizing treatment, predicting parameters, detecting disturbances, and enabling
real-time monitoring. This review critically assesses the application of ML in biological treatment,
providing an in-depth evaluation of key algorithms. This study reveals that artificial neural networks,
tree-based models, support vector machines, and genetic algorithms are the leading algorithms in bio-
logical treatment. A thorough investigation of the applications of ML in anaerobic digestion, composting,
and insect farming underscores its remarkable capacity to predict products, optimize processes, perform
real-time monitoring, and mitigate pollution emissions. Furthermore, this review outlines the challenges
and prospects encountered in applying ML to biological treatment, highlighting crucial directions for
future research in this area.
© 2024 The Author(s). Published by Elsevier B.V. on behalf of Tsinghua University Press. This is an open

access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/).
1. Introduction

Biological technologies, such as anaerobic digestion (AD), com-
posting, and insect farming, involve the use of organisms or mi-
croorganisms to treat organic waste and recover energy, organic
fertilizers, proteins, lipids, and other valuable products (Puyol et al.,
2017; Sharma et al., 2020). They have garnered widespread atten-
tion because they effectively render organic waste harmless, stable,
and reduced in volume, converting it into resources with lower
investment and operational costs compared with physical and
chemical methods (Hoang et al., 2022; Lohri et al., 2017). However,
biological processes are inclined to exhibit complexities and in-
stabilities because of various factors such as microbial growth rates,
substrate concentration, temperature, and pH, adversely affecting
llution Control and Resource
ineering, Tongji University,

.

ier B.V. on behalf of Tsinghua Univ
the efficiency of renewable energy and nutrient-rich product pro-
duction (Leit~ao et al., 2006; Sipma et al., 2010). Moreover, improper
management of byproducts from abnormal operations can lead to
secondary pollution, adversely affecting the environment (Guo
et al., 2022; Yuan & Zhu, 2016). Thus, it is crucial to implement
effectivemeasures for prediction, monitoring, and control to ensure
a more economical, stable, and efficient biological process.
Although some conventional mathematical models offer various
statistical evaluations of variable values, their predictive perfor-
mance is constrained by assumptions, data requirements, un-
certainties, and single-factor analysis (Rigdon, 2012; Tedeschi,
2006). Variable transformations can be employed to improve the
performance of conventional mathematical models, but suboptimal
results may still be obtained (Aydın Temel et al., 2023). Therefore,
when predicting and optimizing complex biological treatment
processes, it is necessary to adopt other more advanced methods
and tools to enhance the accuracy and reliability of prediction and
optimization.

Machine learning (ML), as a crucial branch of artificial intelli-
gence, has garnered widespread acclaim because of its time
ersity Press. This is an open access article under the CC BY-NC-ND license (http://



2 L. Chen et al. / Circular Economy 3 (2024) 100088
savings, high prediction accuracy when facing intricate nonlinear
issues, and remarkable reductions in labor and resource con-
sumption through the elimination of redundant experiments (Guo
et al., 2021a; Khan et al., 2023). These characteristics enable ML to
overcome the limitations of conventional biological treatment
methods. Dominant MLmethodologies include supervised learning
(such as classification and regression), unsupervised learning (such
as clustering), and reinforcement learning (Bertolini et al., 2021). In
the field of biological treatment, supervised ML algorithms,
including artificial neural networks (ANNs) (Zhan & Zhu, 2024),
tree-based models (Li et al., 2022a), support vector machine (SVM)
(Ge et al., 2023), the genetic algorithm (GA) (Awhangbo et al.,
2024), and various multivariate statistical analysis (MSA)
methods (Gil et al., 2018), have been used to model nonlinear and
complex relationships.

First, ML has been employed to predict the yield and quality of
biological treatment. For instance, it has accurately forecasted AD
biogas production and composition across laboratory and industrial
scales (Li et al., 2022a; Sappl et al., 2023), anticipated compost
maturity (Kujawa et al., 2020), and predicted expected weights in
black soldier fly (BSF) farming (Muinde et al., 2023). Moreover, by
integrating optimization algorithms such as the GA and particle
swarm optimization (PSO), ANNs have been used to optimize
process parameters in various biological treatment technologies,
such as AD (Dahunsi et al., 2016), composting (Ding et al., 2022),
and BSF farming (Proietti et al., 2022). ML has also been used to
monitor and control the stability of biological treatment and
pollution emissions. For example, algorithms such as ANNs and
MSA have been used to monitor and regulate key indicators in the
AD process (Jia et al., 2022), oversee pollution and greenhouse gas
emissions in composting processes (Guo et al., 2022), and manage
the lifecycle of BSFs using computer vision-based algorithms
(Proietti et al., 2022). However, despite its vast potential in bio-
logical treatment, ML still faces challenges, including complex
parameter settings, poor model generalization, high computational
resource consumption, and lack of explainability. Addressing these
challenges will significantly propel the further application of ML in
the field of biological treatment.

Until now, several review articles have discussed the application
of ML, particularly in AD (Cruz et al., 2022; Khan et al., 2023) or
composting (Aydın Temel et al., 2023). However, a comprehensive
review focusing on the application of ML in biological treatment is
still lacking. The prevalent patterns, common challenges, and
prospects of ML applications within the biological treatment
domain necessitate further exploration and elucidation. Therefore,
this study provides a systematic and up-to-date review of the
application of ML in biological treatment. The framework of this
review is structured as follows: In Section 2, a brief introduction is
provided to various popular ML algorithms used in this field, along
with a comparison of their advantages, disadvantages, and appli-
cable scopes. Sections 3, 4, and 5 discuss studies on ML for
modeling the processes of AD, composting, and insect-based waste
treatment, respectively. Before summarizing the findings of this
study in Section 7, the current challenges in successfully deploying
ML in biological treatment and future perspectives are outlined in
Section 6.

2. Development trends and typical algorithms for ML
applications in biological treatment

The fundamental principles and workflow of ML are illustrated
in Fig. S1 which is in the Electronic Supplementary Material (ESM)
in the online version of this paper. Based on data retrieved from the
Web of Science (Fig. 1(a)), the number of studies investigating the
use of ML in the biological treatment of organic waste has steadily
increased from 2017 to 2023. However, the overall volume of
literature remains limited, indicating significant development po-
tential for the applications of ML in biological treatment. Regarding
the proportion of publications on different treatment approaches
(Fig. 1(b)), the order of percentage is AD (65.50%) > composting
(32.17%) > insect farming technology (2.33%). Figs. 1(c) and 1(d)
show the most commonly employed ML algorithms in modeling
biological treatment, which are categorized into five primary types:
ANNs, tree-based models (RF/DT/GBR), SVM, GA, and others.
Among them, ANN models are the most commonly used algo-
rithms. Specifically, research employing ANNs accounts for 32.65%
and 33.33% of the total AD and composting studies, respectively.
Following ANNs, tree-based models feature significantly, account-
ing for 22.96% and 26.26% in AD and composting studies, respec-
tively. The use rates of SVM and GAmodels are lower, at 14.80% and
18.18% for AD and 12.76% and 10.10% for composting, respectively.
Apart from these models, other models demonstrate application
rates of 16.83% and 12.13%, respectively. Table S1 in the ESM pro-
vides a detailed summary of the advantages, disadvantages, and
suitable application domains of these algorithms. Notably, there
remains a scarcity of research addressing ML applications in insect
farming technology, which can be attributed to limited engineering
practices to date. This topic will be discussed in Section 5 (ML ap-
plications for insect treatment of organic waste).
2.1. Artificial neural networks (ANNs)

ANNs emulate the functionality of neurons in the human brain
and represent a critical technology in the field of ML (Aghbashlo
et al., 2021). They exhibit robust modeling capabilities for com-
plex nonlinear systems by discerning inherent patterns and hier-
archical representations within extensive input data. In recent
years, particularlywith the advent of deep neural networks (DNNs),
the performance of ANNs has significantly improved, leading to
breakthroughs in image recognition, data processing, and other
areas. In biological treatment research, a range of ANNmodels, such
as multilayer perceptron (MLP), recurrent neural networks (RNNs),
long short-term memory (LSTM), and convolutional neural net-
works (CNNs), have recently been extensively employed.
2.2. Tree-based models

Tree-based models use tree structures to iteratively divide
datasets into distinct subsets, employing tailored decision rules for
each subset. This approach ultimately leads to accurate decision
making and prediction. Among various tree-basedmodels, decision
tree (DT), random forest (RF), and gradient boosting regression
(GBR) are the most widely used in biological treatment owing to
their remarkable flexibility and adaptability in handling intricate
biological data.
2.3. Support vector machine (SVM)

The core idea of SVM is to find an optimal hyperplane in a high-
dimensional space to maximize the distance from it to the nearest
data points, known as support vectors or maximum-margin hy-
perplane (Pisner& Schnyer, 2020). SVM employs kernel methods to
achieve optimal data separation and follows the structural risk
minimization principle (Gupta & Gupta, 2023). SVM has exhibited
remarkable predictive performance in organic waste classification,
AD, and compost quality assessment (Aydın Temel et al., 2023; Ge
et al., 2023). Furthermore, when SVM is used for regression anal-
ysis in research, it is referred to as support vector regression (SVR).



L. Chen et al. / Circular Economy 3 (2024) 100088 3

Fig. 1. Trends and proportion of publications on biological treatment applications (ANNs: artificial neural networks; DT: decision tree; RF: random forest; GBR: gradient boosting
regression; SVM: support vector machine; GA: genetic algorithm; XGBoost: extreme gradient boosting; MLR: multiple linear regression; PSO: particle swarm optimization; KNN: K-
nearest neighbor; ANFIS: adaptive network-based fuzzy inference system; LR: linear regression; GEP: gene expression programming; PLS: partial least square; PCA: principal
component analysis).
2.4. Nature-inspired optimization algorithms

The most commonly used nature-inspired optimization algo-
rithms in biological treatment are GAs and PSO. GAs mimic natural
selection and genetic processes in biological evolution, evolving
superior solutions via selective breeding, genetic crossover, and
mutation within a randomized solution pool (Renner & Ekart,
2003). Conversely, PSO emulates animal swarming behavior,
where each solution is a particle that updates its position and ve-
locity by following its personal best and the global best, converging
toward the ultimate optimal solution (Pornsing et al., 2016).
2.5. Other algorithms

2.5.1. Multivariate statistical analysis (MSA)
Principal component analysis (PCA), multiple linear regression

(MLR), and partial least squares (PLS) are the most prevalent MSA
tools for modeling biological treatment. PCA uses orthogonal
transformations to convert a set of potentially correlated variables
into linearly independent components, thereby aiding in pin-
pointing the key factors affecting the outcome variable (Jolliffe &
Cadima, 2016). MLR examines relationships between multiple
variables; however, for nonlinear associations, alternative
nonlinear regression methods are crucial for improved accuracy
(Krmar et al., 2020). PLS regression, as a highly optimized regres-
sion technique, integrates the core principles of PCA and MLR,
demonstrating superior performance in handling intricate data
(Chen et al., 2022a). Unlike PCA, PLS further delves into feature
interrelationships, thereby improving the accuracy of capturing
complex data patterns and latent connections (Kettaneh et al.,
2005).
2.5.2. Boosting algorithms
Adaptive boosting (AdaBoost) and extreme gradient boosting

(XGBoost) are among the most commonly used boosting algo-
rithms in the biological treatment of organic waste. AdaBoost as-
signs weights to each training sample, giving greater importance to
misclassified samples during iterations, making it effective for both
classification and regression tasks (Ferreira & Figueiredo, 2012).
Conversely, XGBoost employs gradient boosting trees, incorpo-
rating regularization terms and a learning rate during the con-
struction of each tree to control model complexity and improve



4 L. Chen et al. / Circular Economy 3 (2024) 100088
generalizability (Shehadeh et al., 2021). Furthermore, XGBoost
supports parallel computing and allows the customization of
optimization objective functions, exhibiting excellent performance
on large-scale datasets.

2.5.3. K-nearest neighbor (KNN)
K-nearest neighbor (KNN) is an instance-based learning algo-

rithm that classifies or predicts new data points by comparing them
to the K-nearest neighbors in the training dataset using their cat-
egories or attribute values (Uddin et al., 2022). KNN does not
require explicit model training but directly uses existing instances
for predictions, which makes it efficient in handling large-scale
datasets. However, KNN is sensitive to the local data structure,
susceptible to noise, and has high computational complexity when
dealing with high-dimensional data (Jiang et al., 2020). Further-
more, the selection of the K value plays a crucial role in determining
the performance of KNN (Zhang et al., 2018).

2.5.4. Adaptive network-based fuzzy inference system (ANFIS)
The ANFIS integrates principles from neural networks and fuzzy

logic, enabling high-precision simulation of nonlinear systems,
such as predicting and optimizing the AD process in biogas pro-
duction (Najafi & Ardabili, 2018; Zareei & Khodaei, 2017). This in-
tegrated approach combines the learning capabilities of neural
networks with the enhanced decision making abilities of fuzzy
inference systems to optimize model performance. In addition,
ANFIS offers excellent explainability and transparency (Chen et al.,
2022b). These characteristics make ANFIS highly promising and
versatile for various applications in biological treatment.

3. ML applications in AD

AD is a sustainable bioprocessing method that uses specific
microorganisms, such as methane-producing bacteria, to convert
organic matter into high-energy biogas, primarily composed of CH4
and CO2 (Wu et al., 2021; Zamri et al., 2021). To overcome the
Fig. 2. Application principle of
challenges faced in AD, including sensitivity to feedstock compo-
sition and operating parameters and difficulties in predicting and
controlling the stability and biogas production efficiency of AD
systems, an increasing number of researchers are exploring the
application of ML techniques for monitoring, controlling, and
optimizing the AD process. ML algorithms, such as ANNs, RF, SVM,
and GA, have been employed to predict biogas yield and compo-
sition, monitor and control process stability, and optimize process
parameters, thereby enhancing the efficiency and quality of AD. The
principles of AD research based on ML are presented in Fig. 2.
3.1. Biogas yield and composition prediction

3.1.1. Progress in laboratory-scale AD
ML models have found widespread application in predicting

biogas production (Khashaba et al., 2022; Long et al., 2021; Mo
et al., 2023; Neto et al., 2021; Okwu et al., 2021) and composi-
tions (CH4, CO2, H2) (Chong et al., 2023; Li et al., 2022b; Sun et al.,
2024) in laboratory-scale AD. For instance, independent ANN
models have been extensively employed to model AD processes,
predicting biogas production and composition (Cruz et al., 2023;
Ghatak & Ghatak, 2018; Jaroenpoj et al., 2014; Long et al., 2021;
Neto et al., 2021). To further improve the predictive performance of
ANN models for biogas production, combinations of ANN models
with nature-inspired optimization algorithms have been used to
select the optimal ANN structure (Beltramo et al., 2019; Gueguim
Kana et al., 2012; Oloko-Oba et al., 2018; Zaied et al., 2023). For
example, Zaied et al. (2023) and Machineni and Anupoju (2023)
integrated ANNs with PSO to optimize ANN parameters (weights
and biases), whereas other studies have employed the GA (Ghersi
et al., 2021; Jacob & Banerjee, 2016; Zhan & Zhu, 2024), ant col-
ony optimization (Fajobi et al., 2023), and the seagull optimization
algorithm (Abdel daiem et al., 2022) for selecting the most effective
ANN parameters in predicting biogas production. Furthermore,
some studies have applied ANFIS to predict biogas production in
AD, achieving R2 values exceeding 0.95 (Fajobi et al., 2023; Heydari
AD research based on ML.



L. Chen et al. / Circular Economy 3 (2024) 100088 5
et al., 2021; Okwu et al., 2021; Olatunji et al., 2022). Although ANN
models have demonstrated superior performance in modeling AD
systems, their main limitation lies in their “black-box” nature,
which results in poorer explainability. Although neural networks
often exhibit high predictive accuracy, they rely on extensive
training data and hyperparameter optimization. In addition, chal-
lenges such as overfitting, substantial computational resource
consumption, and insufficient generalization ability need to be
addressed when using ANN models to predict biogas production in
AD.

Compared with other ML methods, tree-based models are
typically easier to implement and require less data preprocessing.
Furthermore, these models allow users to easily extract the
importance of features, thereby improving model performance,
aiding in the construction of interpretable models, and enhancing
our understanding of the current context by capturing relevant
informationwithin themodel. Several studies have used tree-based
models to predict biogas production and composition during AD
processes (Chiu et al., 2022; Sun et al., 2024; Wang et al., 2021,
2023b). For instance, Zhang et al. (2023) developed RF, GBR, and
XGBoost models to predict the facilitating effects of biochar on
methane yield and the maximum methane production rate during
AD. The GBR model achieved R2 values of 0.84 and 0.69 for the
methane yield and methane production rate, respectively. The
optimal methane production and methane production rate
occurred with biochar particles of 0.3e0.5 mm, a surface area of
~290 m2/g, >31% oxygen, and >20 g/L biochar addition.

Other studies have also compared various ML algorithms for
modeling the AD process (Chong et al., 2023; Heydari et al., 2021;
Obileke et al., 2023; Okwu et al., 2023; Tufaner & Demirci, 2020).
For example, Okwu et al. (2023) compared the Mamdani fuzzy
model (MFM), ANNs, and response surface methodology (RSM) for
modeling and optimizing methane production in AD and discov-
ered that the predictive performance of the MFM and ANN models
was slightly higher than that of the RSM model. Similarly, Heydari
et al. (2021) evaluated the predictive performance of ANNs and
ANFIS for methane production in an upflow anaerobic sludge
blanket reactor, revealing that the ANN model exhibited slightly
better predictive performance than ANFIS.

In summary, ANN models have become the preferred ML algo-
rithm for predicting biogas production and composition in AD
processes. However, despite the excellent predictive accuracy of
ANN models, issues related to explainability, computational costs,
and adaptability of neural network models have prompted the
exploration of tree-based models. In particular, when handling
complex systems such as AD, where understanding the relation-
ships between variables is crucial, tree-based models have
demonstrated their unique advantages. An overview of recent
studies on the application of ML models in laboratory-scale AD is
summarized in Table 1.

3.1.2. Progress in industrial-scale AD
In recent years, ML models applied to predict biogas production

in industrial-scale ADhas alsomade some strides (as summarized in
Table 2). Specifically, Asadi et al. (2020) used ANFIS with fuzzy c-
means clustering to predict biogas production rates (CH4, CO2, and
H2S) in AD tanks at awastewater treatment plant.Wang et al. (2021)
analyzed the impact of different types of waste and operational
parameters on industrial-scale AD biogas production using various
ML methods. The results indicated that although the changes in
biogas production were mainly attributed to diverse waste types,
the predictive capability of the operational parameters was
comparatively limited. Li et al. (2022a) employed XGBoost, SVM,
ANN, RF, and linear regression (LR) to forecast biogas production
within an industrial-scale biogas facility. Their findings showed that
the RF model performed best, with an average R2 of 0.74. Feature
importance analysis revealed that feedstock amount, digestate
properties, and feedstock properties were significant factors, ac-
counting for 45.9%, 38.6%, and 15.4%, respectively. Similarly, Yildirim
and Ozkaya (2023) used RF, ANN, KNN, SVR, and XGBoost models to
forecast biogas production in a large-scale AD facility. Among these
methods, the RF model emerged as the most accurate predictor,
attaining a high R2 of 0.9242. Overall, existing studies have under-
scored the potential of ML algorithms for forecasting biogas pro-
duction on an industrial scale. However, most current applications
mainly focus on utilizing existing operational data to forecast biogas
production or composition, leaving several avenues for further
exploration and enhancement, such as developing real-time
monitoring and control systems and integrating other advanced
technologies such as the Internet of Things and cloud computing.

3.2. Monitoring and control

The accumulation of inhibitory compounds, resulting from
various factors, including high substrate concentrations, pH fluc-
tuations, unsuitable temperatures, and excessive organic load,
frequently causes reactor failure in the AD process (Wu et al., 2019;
Xie et al., 2016). Therefore, significant attention has been paid to the
development of process monitoring and control technologies to
maintain process stability and maximize methane production.
However, conventional AD process monitoring methods typically
involve extensive and time-consuming chemical and physical
analysis, which are not only costly and imprecise but also chal-
lenging to implement for real-time monitoring (Waltham &
O€rmeci, 2020; Wang et al., 2018). Consequently, automated and
intelligent control strategies, particularly those using prediction
control and optimization algorithms based on ML, have emerged as
viable solutions for real-time monitoring, optimization, and control
of the AD process by leveraging input variables and their hidden
interdependencies (Khan et al., 2023; Nguyen et al., 2015). Various
offline and online indicators have been commonly used to monitor
AD process stability, including biogas yield and composition, pH,
chemical oxygen demand (COD), oxidationereduction potential
(ORP), ammonia/ammonium (NH3/NHþ

4 ), volatile fatty acids (VFA),
alkalinity (ALK), VFA/ALK, concentrations of specific intermediate
metabolites (CO, H2, aromatic compounds, etc.), microbial com-
munity, and microbial activity (Cruz et al., 2021; Khan et al., 2023;
Nie et al., 2023). Among these indicators, VFA, ALK, COD, and pH are
the most commonly monitored. Furthermore, ANNs and MSA are
the most widely used ML models for monitoring these indicators.

VFA is the intermediate product resulting from the degradation
of organic matter in AD. The accumulation of excessive VFA con-
centrations can inhibit microbial populations within the digester,
making it a crucial indicator requiring close monitoring in the AD
process (Harirchi et al., 2022). To overcome the limitations posed by
expensive and environmentally sensitive physical sensors for VFA
measurements, Kazemi et al. (2020) proposed theuse of data-driven
soft sensors that rely on ML techniques for reliable monitoring and
prediction of VFA levels. Compared with ANNs, RF, SVM, and
extreme learning machines, genetic programming soft sensors
exhibit more precise predictive performance and better robustness.
Furthermore, to further enhance the predictive capability of soft
sensors, Xu et al. (2020) developed an integrated simulationmethod
based on random standard deviation sampling and DNNs to predict
VFAproduction inADprocesses. The optimumR2was determined to
be 0.998, with the smallest average absolute error of 3.28%.

ALK is another pivotal indicator that requires close monitoring
within the AD process. Ward et al. (2011) were pioneers in devel-
oping a software sensor based on MLR to predict the ALK of AD
tanks using pH, electrical conductivity (EC), and ORP as input



6 L. Chen et al. / Circular Economy 3 (2024) 100088Table 1
The latest applications of ML in laboratory-scale AD to predict biogas production.

Substrates Input variable Output variable ML algorithms Best performance (R2, RMSE, Reference
MSE, MAE)

Cattle dung, bamboo dust, Composition, temperature, Biogas production curve ANN R2 ¼ 0.9984, AARE ¼ 0.043% Ghatak and Ghatak (2018)
sugar-cane bagasse, saw dust time, and HRT

Anaerobic hybrid reactor (AHR), Reactor fill ratio, influent pH, Biogas production rate ANN, Nonlinear regression ANN; R2 ¼ 0.9852, Tufaner and Demirci (2020)
perlite effluent pH, influent alkalinity models RMSE ¼ 217.4

(ALK), effluent ALK, OLR,
effluent COD, effluent TSS,
effluent SS and effluent VSS

Agricultural wastes, cow Temperature, chemical dose, Cumulative methane ANN R2 ¼ 0.985, RMSE ¼ 0.0035 Almomani (2020)
manure composition, and HRT production

Crop straw, livestock manure Crude protein, crude fat, Cumulative methane yield MVLR, MCARS, GSA, PLS MCARS; R2 ¼ 0.982, Yang et al. (2021a)
cellulose, hemicellulose, lignin, RMSE ¼ 6.599
total sugar, C/N

Food, fruits and vegetables Mixing ratios, reactor/feed type, Cumulative biogas production ANN R2 ¼ 0.8486 Neto et al. (2021)
wastes VS, pH, OLR, HRT, Temperature,

reactor volume
Spearmint essential oil COD, pH, effluent MLSS, MLVSS, Biogas production ANN, ANFIS ANN; R2 ¼ 0.975, RMSE ¼ 2650, Heydari et al. (2021)

wastewater turbidity, oil and grease relative root mean ¼ 0.234%
removal, COD removal, phenol
removal, effluent volatile fatty
acids (VFA) and ALK

Poultry wastes and cow dung Mixing ratio, HRT Biogas yield ANFIS, RSM ANFIS; R2 ¼ 1, RMSE ¼ 1.0, Okwu et al. (2021)
MAE ¼ 0

Arachis hypogea shells Temperature, HRT, and particle Biogas and methane yields ANFIS, RSM, FCM ANFIS; R2 ¼ 0.9601, 0.9486, Olatunji et al. (2022)
size 0.9626, 0.9172

Manure, food waste, sewage Operating mode, HRT, Antibiotic resistance genes, ANN, RF, XGBoost XGBoost; R2 ¼ 0.9 Haffiez et al. (2022)
sludge Temperature, additives, co- mobile genetic elements

substrate
Lignocellulosic biomass VS/TS, cellulose, hemicellulose, Biochemical methane potential ANN, DT, ELM, EN, GPR, KNN, KNN; R2 ¼ 0.75, MAE ¼ 30.2 Wang et al. (2023b)

lignin, soluble saccharide, and (BMP) MLR, PR, SVM, PCA
crude protein. C, H, O, N

Palm oil mill effluent COD, BOD, TS, OLR, HRT, VFA, Biogas production and methane RSM, ANN, ANFIS ANFIS; R2 ¼ 0.9791, Chong et al. (2023)
recirculation ratio, pH and yield MAE ¼ 0.0730, RMSE ¼ 0.1438
temperature

Cow dung Global solar irradiance, absolute Biogas yield ANN, MLR ANN; R2 ¼ 0.999, Obileke et al. (2023)
relative humidity, slurry RMSE ¼ 8.33  106

temperature, biogas
temperature, absolute pH, and
ambient temperature

Poultry wastes and cow dung The ratio of cow dung to poultry Biogas yield MFM, BP-ANN, RSM MFM, ANN; R2 ¼ 1.0 Okwu et al. (2023)
wastes, and the retention time

Biochar, food waste, manure, Physicochemical properties of Methane yield GBR, RF, XGBoost GBR; R2 ¼ 0.84, RMSE ¼ 72.04 Zhang et al., (2023)
and other biomass biochar, material conditions of

AD, operating conditions for AD
Cassava wastewater, sewage pH, calcium concentration and Biogas production ANN, GA R2 ¼ 0.9999 Cruz et al. (2023)

sludge reaction time
Sweet sorghum leaves and Mixing speed, pH, reaction BMP ANN, PSO R2 ¼ 0.996, RMSE ¼ 308.42 Machineni and Anupoju (2023)

stalks, mixed microbial temperature, and SIRs
consortia

Agricultural waste Biomass type, reactor/feeding, Steady-state biogas production ANN, COA, MVO, LCA, ERWCA, ANN-ERWCA; R2 ¼ 0.9314, Sun et al. (2024)
VS, pH, OLR, HRT, temperature, SFS, TLBO RMSE ¼ 0.1969, MAE ¼ 0.1307
and reactor volume

RMSE: root mean square error, MAE: mean absolute error, NRMSE: normalized root mean square error, MAPE: mean absolute percentage error.



L. Chen et al. / Circular Economy 3 (2024) 100088 7

Table 2
The latest applications of ML in industrial-scale AD to predict biogas production.

Substrate Input variables Output variables ML algorithm Best accuracy Reference

Grass silages, maize, pig 15 variables including TS, VS, Biogas production ANN, GA, ACO Prediction error: 6.24%, Beltramo et al. (2019)
manure, and cattle HRT, NHþ

4 -N, OLR, VFA, R2 ¼ 0.90
manure detergent fiber, detergent fiber

Agricultural, municipal, 20 variables including input Biogas production SVM, XGBoost, RF, KNN; R2 ¼ 0.87 de Clercq et al. (2019)
and industrial volume of kitchen food waste, Logistic regression,
biowastes chicken litter, percolate, and KNN

municipal fecal residue
Agricultural, municipal, 18 variables including day Biomethane production RF, Elastic Net, GBR, XGBoost; R2 ¼ 0.88 de Clercq et al. (2020)

and industrial number, input volume of XGBoost
biowastes various biowastes, co-digested

wastes
18 types of biowastes, Not provided Methane production Gompertz model, 15 Gompertz-ML; Hansen et al. (2020)

mainly seaweed, commonly used ML MAPE ¼ 4.52%
manure, eulat and model, Gompertz-ML
pectin

Sludge from the 12 variables including 7 Biogas yield 4 types of ANN: linear R2 ¼ 0.741, deviation Sakiewicz et al. (2020)
wastewater operation parameters and TP, network, MLP, RBF and ratio: 0.697
treatment plant COD, BOD5, TN, TSS GRNN

Sludge, thickened Input volumes of 31 waste Biogas yield TPOT R2 ¼ 0.72, RMSE ¼ 247 Wang et al. (2021)
waste activated streams, TS, VS, VFA, ALK, VFA/
sludge, and 29 types ALK
of trucked wastes

Sedimentation sludge, 16 variables including sludge Biogas yield LSTM, DA-LSTM, DA- DA-LSTM-VSN; Jeong et al. (2021)
and food waste input/output amount, SRT, LSTM-VSN R2 ¼ 0.76,
leachate temperature, BOD, COD, VS/TS NRMSE ¼ 0.09,

ratio, TN, TP, and SS MAE ¼ 216.1
Food waste 19 variables including feed Biogas yield LR, RF, ANN, SVM, RF; R2 ¼ 0.74, Li et al. (2022a)

amount, feedstock TS, feedstock XGBoost RMSE ¼ 0.51
COD, TN, Oil, digester TS,
digester COD, VFA, ALK, and
VFA/ALK

Food waste 14 variables including pH, Biogas yield SMOTER-GA-ELM, ELM, ELM; R2 ¼ 0.972 Zhang et al. (2022)
TVFA, TS, VS, TAN, COD, pH, GA-ELM, SMOTER-ELM
ALK, TS, VS, TAN, TVFA, COD, FV

Manure, vegetable Operational parameters, TS, VS, Biogas yield RF, ANN, KNN, SVR, RF; R2 ¼ 0.9242, Yildirim and Ozkaya (2023)
waste, and temperature, pH, ALK and VFA XGBoost MAE ¼ 1119.60,
slaughterhouse RMSE ¼ 1405.84
waste

RMSE: root mean square error, MAE: mean absolute error, NRMSE: normalized root mean square error, MAPE: mean absolute percentage error.
variables, achieving an optimal calibration model with an R2 of
0.76. Subsequently, Bai et al. (2017) also employed LR methods and
software sensor technology for ALK prediction. They identified that,
among acidityealkalinity, ORP, and EC (used as input variables), EC
significantly influenced ALK prediction. However, LR or MLR
models can encounter overfitting or instability issues, especially
with high-dimensional data or in situations of multicollinearity,
leading to inaccurate predictions (Todeschini et al., 2004). To
overcome these limitations and improve predictive performance,
more complex and accurate ML algorithms have been applied to
ALK prediction. For instance, Wang et al. (2018) used an ANN to
track ALK changes during AD processes online. On the basis of
existing online measurement parameters, they established a 3-2-1
structured backpropagationefeedforward neural network model
with a high R2 value of 0.9948. Sensitivity analysis further high-
lighted ORP as the most significant factor.

However, monitoring a single indicator typically struggles to
comprehensively assess the operational state of AD digesters. To
gain a more comprehensive understanding of digester operation,
this typically necessitates the integration of complex systems
involving online sensors and ML algorithms to simultaneously
monitor the changing trends and relationships among multiple
indicators. Jia et al. (2022) investigated deep learning models for
predicting online sensor data related to state and performance
variables. They found that a combined CNN and LSTM model out-
performed individual CNN and LSTM models in predicting stability
and performance variables (such as pH, alkalinity, VFA, COD, SCOD,
TS, VS, methane production rate, and methane content in biogas)
with high accuracy (R2 ¼ 0.978; mean square error ¼ 0.031). Wang
et al. (2024) integrated a millielectrode array physical sensor
(MAPS), an AD simulation system (ADSS) based on AD Model No.1,
and explainable ML algorithms for real-time in situ monitoring of
pH, ORP, temperature, NHþ

4 -N, and EC. Comparedwith conventional
ML algorithms, the integrated MAPSeADSSeML method achieved
99% prediction accuracy. Furthermore, the adverse effects of pH,
alkalinity, and NHþ

4 -N on biogas production were confirmed by
their inverse relationship with VFA, as indicated by SHAP values
and the predicted negative correlation coefficients of Pearson
(r ¼ 0.93) and Spearman (rs ¼ 0.92).

Significant developments have been made in the application of
ML for the simultaneous monitoring of single or multiple in-
dicators. However, the environment of AD systems tends to shorten
the lifespan of physical sensors, thereby hindering the acquisition
of long-term data. Moreover, existing ML algorithms typically rely
heavily on statistical data while neglecting the underlying theories
and principles of organic waste and biological systems, resulting in
a disconnect between model predictions and physicochemical ex-
planations. Therefore, the development of high-precision, long-life
AD monitoring sensors, along with the exploration of integrated
approaches combining physicochemical models and ML, has
emerged as a critical avenue for future research to digitalize and
comprehensively interpret AD systems.



8 L. Chen et al. / Circular Economy 3 (2024) 100088
3.3. Optimization of parameters

Optimized substrate ratios, suitable temperature and pH ranges,
balanced C/N ratios, and appropriate concentrations of VFA and ALK
are crucial factors in enhancing substrate digestion and methane
production (Bong et al., 2018; Khan et al., 2016; Matheri et al.,
2018). Conventional parameter optimization methods typically
involve laboratory batch experiments to optimize various opera-
tional parameters to increase substrate digestion and methane
yield (Kunatsa & Xia, 2022; Ramachandran et al., 2019). However,
this approach has drawbacks such as complexity, time and labor
intensiveness, and high costs. To overcome these challenges, re-
searchers have adopted various ML algorithms to optimize sub-
strate ratios or process parameters, thereby achieving
comprehensive optimization of the AD process and maximizing
biogas and methane production.

Gray relational analysisePCA (GRAePCA), central composite
designeRSM (CCDeRSM), and ANNs are effective in optimizing AD
processes. For example, Senthilkumar et al. (2016) used GRAePCA
to determine the best process parameters for AD of food waste,
finding optimal conditions at 7.5% TS, pH 7, 50 C, and 30% poultry
waste co-digestion to achieve the highest biogas production.
Jimenez et al. (2015) employed CCDeRSM to conduct anaerobic co-
digestion experiments, optimizing conditions for increased
methane yield. The optimized specific methane yields under mes-
ophilic and thermophilic conditions were 1.31 and 1.38 g CH4-COD
gVSS1 d1, respectively. Kainthola et al. (2020) optimized co-
digestion parameters for agricultural and food waste using
CCDeRSM. Validation experiments under an optimized C/N ratio of
30, pH of 7.32, and F/M ratio of 1.87 exhibited methane production
of 323.78 mL/g-VSadd, which is a 166.54 mL/g-VSadd increase over
single digestion. These studies highlight that GRAePCA and
CCDeRSM can effectively reduce the number of experiments, aid-
ing in determining the best waste combination and process pa-
rameters. Dahunsi et al. (2016) further compared the optimization
effects of ANNs and RSM for the co-digestion of poultrymanure and
papaya peel. The ANN model achieved a higher R2 value (0.9828)
than the RSM model (0.9181), indicating that the ANN model was
more accurate and efficient.
Fig. 3. Principles of ML-based stud
4. ML applications in composting

Composting technology represents a sustainable approach for
biologically treating organic waste, primarily focusing on organic
components that are easily biodegradable by aerobic bacteria, such
as cellulose, proteins, and fats. The resulting compost not only
functions as an organic fertilizer to improve soil quality and
diminish dependence on chemical fertilizers but also acts as a soil
amendment, reducing heavy metal bioavailability, tackling organic
pollutants, and mitigating soil pathogens. However, conventional
composting technology still has drawbacks, including low humifi-
cation rates, greenhouse gas emissions, nitrogen loss, and high
metal dispersion (Chen et al., 2023; Guo et al., 2020; Li et al.,
2022c). Low humification during the composting process restricts
the use of the resulting compost in agricultural applications (Bernal
et al., 2009; Dias et al., 2010). Nitrogen loss, greenhouse gas emis-
sions, and the dispersion of heavy metals throughout the com-
posting process not only deteriorate the quality of the compost but
also significantly contribute to environmental contamination (Chen
et al., 2019; Yang et al., 2020). To overcome these limitations and
address these deficiencies, an increasing number of researchers are
exploring the use of ML in monitoring and controlling composting
processes to enhance product quality, optimize the composting
processes, and better protect the environment (Aydın Temel et al.,
2023; Wan et al., 2022; Wang et al., 2023a). Currently, in the
limited available literature, ML algorithms, such as ANN, RF, SVM,
ANFIS, and KNN, have been used to predict compost maturity and
other critical parameters and monitor pollution and greenhouse
gas emissions, among other aspects. The application principles of
ML-based studies for composting are presented in Fig. 3.

4.1. Prediction of composting maturity and optimization of
parameters

Partially decomposed compost contains harmful bacteria, acidic
substances, and organic or inorganic pollutants that impede plant
growth, contaminate the surrounding environment, and ultimately
pose threats to both ecosystems and human health (Wan et al.,
2022; Xue et al., 2019). Therefore, it is essential to guarantee the
ies for composting technology.



L. Chen et al. / Circular Economy 3 (2024) 100088 9
maturity of organic waste compost, as it significantly impacts both
the composting process and the final compost product quality. Key
parameters for assessing compost maturity include physical in-
dicators (temperature, color, odor, etc.), chemical indicators (pH,
EC, C/N ratio, moisture content (MC), humic acid content, total
organic carbon (TOC), etc.), and biological indicators (seed germi-
nation index (GI), enzyme activity, microbial quantity, etc.) (Aydın
Temel et al., 2023; Guo et al., 2021a). Table 3 summarizes the
recent research on the application of ML models in predicting
compost maturity.

4.1.1. Physical morphology and color changes to assess maturity
During the composting process, the decomposition and humi-

fication of organic matter change its color to a dark brown or black
hue. Consequently, by observing the physical morphology and color
changes, the maturity of the compost can be roughly assessed. To
enhance both the efficiency and accuracy of compost maturity
prediction, researchers have integrated the CNN model, which in-
volves direct and in-depth analysis of compost images for assessing
compost maturity. Xue et al. (2019) constructed a CNN model to
predict compost maturity by processing images through convolu-
tional pooling layers. This method accurately captured granularity
differences in compost images across different stages and precisely
extracted visual features, enabling the identification of compost
maturity. Kujawa et al. (2020) explored the feasibility of early
maturity classification of compost using CNNs. The study found
that the CNN model effectively classified early compost maturity,
with classification errors ranging from 0.51% to 17.77%. Sangeetha
Table 3
The latest applications of ML to predict composting maturity.

Biomass Input variables Output variables

Vegetable waste, straw, Image of composting Composting maturi
livestock waste and mixtures

Sewage sludge, rapeseed straw Image of composting Composting maturi

Grass, livestock-manure, Image of composting Composting maturi
vegetable-wastes, plastic,
glasses

Municipal solid waste and cow Cattle manure ratio, pH, EC, MC, TN, C/N
dung composting time ratio, TOC

Food waste and tea waste Tea waste ratio, composting MC, TN, TOC loss
time

Olive mill waste and natural Natural mineral material types, Temperature, pH, E
mineral amendments olive mill waste ratio, MC, TN, and C/N ra

composting time
Traditional chinese medicine C/N ratio, initial moisture Humic acid content

residues content, inoculant type,
composting days

Chicken manure, corn straw Penicillin, pH, and C/N ratio Bacterial communit
and humification
processes

Textile waste, green waste, UVevisible spectroscopy, X-ray Humification degre
paper & cardboard waste diffraction, and infrared presence of cellulos

spectroscopy mixtures, aromatic
and polymerization
degree

Rice straw, dried pig manure NIRS figures Organics, TN, C/N r
638 datasets about green waste Composting time, temperature, GI, T-value

composting pH, EC, C/N ratio, TN, OM, E4/E6,
humic acid, TOC, the presence
of additives

Food waste, garden waste Composting time, ambient GI, C/N ratio
temperature, ventilation rate,
pH. EC

452 kitchen waste composting Composting time, temperature, Composting maturi
samples MC, pH, C/N, ammonia

nitrogen, nitrate nitrogen, TN,
TOC, GI, EC, organic matter
and Govindarajan (2023) employed a rapid region-based CNN
prediction model to extract multilayer image attributes from
different compost stages for rapid maturity assessment, with an
accuracy rate of 96.4%. Overall, the introduction of CNN models for
compost maturity identification significantly improved prediction
efficiency and accuracy, surpassing the 95% accuracy threshold.
This image-based identification method aligns closely with prac-
tical applications, undoubtedly providing robust technical support
and a reference for accurately determining compost maturity in
production practices.

4.1.2. Chemical indicators to assess maturity
Temperature, pH, MC, EC, total nitrogen (TN), C/N ratio, and TOC

are significant chemical indicators for assessing compost maturity
(Aydın Temel et al., 2023; Guo et al., 2021b). Bayındır et al. (2022)
used a cascade forward neural network (CFNN) model, with the
cattle manure ratio and composting time as input variables, to
predict maturity parameters such as temperature, pH, EC, MC, TN,
C/N ratio, and TOC. Their results showed that the manure ratio
significantly affects the composting process. Using GAs for opti-
mization, the optimal manure ratio and processing time were
23.39% and 104.86 days, respectively. Yılmaz et al. (2022) used the
radial basis functional neural network (RBFNN) to investigate the
impact of tea waste ratio and composting time on parameters such
as MC, TN, and TOC loss in the cocomposting process of food waste
and tea waste. The RBFNN model achieved the lowest TN and TOC
loss in the composting process with a 25% tea waste ratio. Further
optimization of co-composting process parameters, including
ML algorithm Best accuracy Reference

ty CNN 99.7% Xue et al. (2019)

ty CNN Classification error Kujawa et al. (2020)
ranged from 0.51% to
17.77%

ty ReCNN 96.4% Sangeetha and
Govindarajan (2023)

CFNN, RSM, GA CFNN-GA; Total Bayındır et al. (2022)
desirability was 0.4455

RBFNN, GA Desirability levels are Yılmaz et al. (2022)
above 95 %

C, FF-NN, ER-NN, RSM, GA Prediction error <2% Aycan Dümenci et al.
tio (2021)

ANN, GA R2 ¼ 0.91 Shi et al. (2022)

ies RF and Linear e Kang et al. (2022)
regression

e, PLS e Biyada et al. (2020)
e
ity,

atio PLS e Shen et al. (2023)
Extra Trees, GBR, MLP, Extra Trees; R2 ¼ 0.928 Li et al. (2023)
KNN for GI, R2 ¼ 0.957 for T-

value

RF, XGBoost, LightGBM, XGBoost; R2 ¼ 0.977 for Wan et al. (2022)
MLP C/N ratio, R2 ¼ 0.986 for

GI
ty Linear regression, KNN, Stacking model; Ding et al. (2022)

DT, SVR, RF, Stacking Training R2 ¼ 0.959,
model testing R2 ¼ 0.875



10 L. Chen et al. / Circular Economy 3 (2024) 100088
temperature, pH, EC, C/N, MC loss, TN loss, and TOC loss, has been
performed using GAs. Aycan Dümenci et al. (2021) predicted
compost maturity parameters (temperature, pH, EC, MC, TN, and C/
N ratio) using a neural network model with natural mineral ma-
terials, olive waste ratio, and composting time as inputs. The model
had prediction errors below 2%. After GA optimization, blending
pumice and vermiculite achieved the desired temperature and
reduced nitrogen loss with pH, EC, and MC adjustments. In addi-
tion, ML combined with sensors was used to monitor MC in
industrial-scale composting systems (Moncks et al., 2022).

Humic acid content is also a crucial chemical indicator for
evaluating compost maturity and quality. As the composting pro-
cess proceeds, microorganisms break down organic matter to
produce metabolites, including humic acid, which accumulates to
indicate compost maturity when it reaches a stable level (Guo et al.,
2021b). Shi et al. (2022) predicted humic acid content in compost
with a backpropagation neural network model using composting
parameters (C/N ratio, initial MC, inoculant type, and composting
days), achieving an R2 value of 0.91. Through GA optimization, they
identified the best parameter combination (C/N ratio of 37.42, MC
of 69.76%, sterile conditions, and 50 days of composting). Under
these conditions, the compost products had the highest humic acid
content. Kang et al. (2022) investigated the impact of penicillin, pH,
and C/N ratio on bacterial communities and humification processes
in aerobic composting using RF and LR models. Their results indi-
cated that penicillin primarily influenced low-abundance microbial
genera, with bacterial communities regulating the synthesis of
humic substances, including fulvic acid and humic acid. Quorum
sensing modulates carbohydrate and amino acid metabolism,
controls humic acid synthesis, and influences bacterial cooperation
during composting.

Spectroscopy and other chemical characterization methods are
crucial tools for predicting compost maturity through ML.
Vergnoux et al. (2009) initially used near-infrared spectroscopy
(NIRS) to track physicochemical and biochemical changes during
composting. Using PCA, they identified distinct compost stages and
aging processes based on spectral data. The incorporation of PLS
models facilitated the prediction of diverse parameters, including
MC, temperature, pH, organic carbon (OC), organic nitrogen (ON),
OC/ON ratio, TN, NHþ

4 -N, and humic and fulvic acid ratios. Biyada
et al. (2020) examined various chemical changes, such as humifi-
cation degree, cellulose mixtures, aromaticity, and polymerization
degree, during the composting process using ultravioletevisible
spectroscopy, X-ray diffraction, and infrared spectroscopy. More-
over, through the application of PLS models, they further analyzed
the correlation between infrared spectra and compost chemical
properties. Shen et al. (2023) performed quantitative analysis of
organics, TN, and the C/N ratio under different composting condi-
tions using NIRS. They constructed three nonlinear PLS models
employing spectral preprocessing and variable selection strategies.
The results indicated that with appropriate spectral preprocessing,
NIRS demonstrated accurate predictions for each element, exhib-
iting notable predictive capabilities.

4.1.3. Biological indicators to assess maturity
The seed GI comprehensively reflects the phytotoxicity of

compost and is considered the most sensitive and reliable indicator
of compost maturity (Komilis & Tziouvaras, 2009; Yang et al.,
2021b). Simultaneously, enzyme activity, microbial quantity, and
other related indicators reflect the quantity and activity level of
microorganisms in compost, enabling an assessment of its maturity
(Goyal et al., 2005; Lv et al., 2022). Li et al. (2023) used extra trees,
GBR, MLP, and KNN to predict the GI and T-value. The extra tree
algorithm achieved the best prediction accuracy (R2 of 0.928 for GI
and 0.957 for the T-value). Pearson correlation analysis revealed
that humic acid notably impacts the GI, whereas the C/N ratio
during the composting process significantly affects the T-value. In
another study, Wan et al. (2022) employed RF, XGBoost, LightGBM,
and MLP to forecast both the GI and C/N ratio. XGBoost emerged as
the most effective in predicting the C/N ratio, with an R2 value of
0.977. However, regarding GI prediction, the ensemble model per-
formed the best, achieving an R2 value of 0.986. Feature importance
analysis highlighted the considerable influence of different seed
types on the GI, and the physicochemical properties of the raw
materials significantly affected the prediction of the C/N ratio.
Chakraborty et al. (2014) integrated visible and near-infrared
(VisNIR) diffuse reflectance spectroscopy (DRS) with various ML
models to forecast the enzymatic activity in compost. Among the
evaluatedmodels, such as PLS, PCA, RF, SVR, and PSL, theMLPeANN
model was the most accurate predictor, achieving an impressive R2

value of 0.91, validating the effectiveness of combining VisNIR DRS
with ML in forecasting compost enzyme and microbial activity.

4.1.4. Relationship between composting maturity and key
parameters

Ding et al. (2022) used existing literature data to investigate the
effects of crucial parameters (including composting time, temper-
ature, MC, pH, C/N, NHþ

4 -N, nitrate nitrogen, TN, TOC, GI, EC, and
organic matter) on compost maturity, which was evaluated
through a maturity score using ML models. Compared with LR,
KNN, DT, SVR, and RF, the stacking model exhibited superior pre-
dictive accuracy (with a training R2 value of 0.959 and a testing R2

value of 0.875). Simultaneously, SHAP and partial dependence
analysis revealed that the mesophilic phase should maintain
appropriate temperature, MC, and pH values, whereas the ther-
mophilic phase should be fine-tuned on the basis of partial
dependence analysis to provide suitable nutrients. Optimal initia-
tion conditions should maintain a mesophilic environment with a
temperature range of 30Ce45 C, an MC between 55% and 65%,
and a pH level of 6.3e8.0. In addition, during the thermophilic
stage, it is essential to ensure that the TN content exceeds 2.3% and
the TOC content exceeds 35%. Experimental validation confirmed
the improved maturity achieved by the optimized model-based
systems.

4.2. Monitoring of pollution and greenhouse gas emissions

Currently, research on the prediction and control of pollutants in
the composting process using ML remains limited. Specifically, ML
applications in composting pollutant control mainly concentrate on
heavy metal immobilization and organic pollutant degradation.
Guo et al. (2022) used various models with GAs to predict and
optimize heavy metal stabilization in composting, with GBR per-
forming best (R2: 0.76e0.94 for the bioavailability trend and
0.55e0.81 for the immobilization rate). The key factors affecting
bioavailability included initial metal bioavailability, total phos-
phorus, and composting time. After GA optimization, high immo-
bilization rates were achieved for Cu (79.53%), Zn (31.30%), Cd
(14.91%), As (46.25%), and Cr (66.27%).

The application of ML in monitoring and controlling organic
pollutants, particularly antibiotics and polycyclic aromatic hydro-
carbons (PAHs), has been a focal point. Alavi et al. (2019) used an
ANNmodel to simulate the breakdown of tetracycline antibiotics in
the composting process, achieving a remarkable R2 value of 0.99.
Furthermore, thorough sensitivity analysis revealed that time was
the most significant factor, accounting for 80.43% of the impact,
followed by the type of antibiotic (7.95%), the ratio of the bulking
agent (6.43%), and the initial concentration of the antibiotic (5.17%).
Wu et al. (2013) used six ML models to forecast bioavailability
changes of 16 PAHs in compost-contaminated soil. The



L. Chen et al. / Circular Economy 3 (2024) 100088 11
performance ranking of the ML models was as follows: radial basis
function > M5 model tree > SVR > MLP > M5 rules > LR. Key var-
iables such as incubation time, OC, soil moisture, and nutrients
significantly affect PAH bioavailability. Dragoi et al. (2021) com-
bined ANNs and differential evolution algorithms to model and
forecast the removal of petroleum hydrocarbons and OC during the
composting of oily sludge. Their findings showed that the ANN
model closely matched the experimental results, with a mean ab-
solute relative error of 5.96% for hydrocarbons and 12.7% for OC.
Other studies have successfully combined ANNs with various bio-
sensors to precisely determine the concentrations of phenols,
including phenol and catechol, generated during the composting
process (Tang et al., 2008; Zhang et al., 2009; Zhou et al., 2014).

In addition, the application of ML mainly involves monitoring
greenhouse gas emissions during the composting process. Díaz et al.
(2012) conducted preliminary research using the ANFIS model to
investigate factors affectingCO2 emissions during composting. Their
findings identified aeration time as the primary factor affecting CO2
release. Under conditions of 0.2 Lair (min$kg)1 aeration, 55% MC,
and 1e3 cm particle size, the composting process exhibited the
highest CO2 emission levels. Li et al. (2022d) employed AdaBoost,
bagging, gradient boost, RF, KNN, and DT to predict CO2 generated
during composting. TheRFmodel achieved thehighest classification
accuracy of 88% and the lowest root mean square error (RMSE). TOC
was identified as the most critical factor, contributing to 59% of CO2
generation. Najafi and Ardabili (2018) explored the influence of C/N,
reactor temperature, and retention time on methane production
during composting. Their results indicated thatmethaneproduction
peaked at 35 Cwith a C/N ratio of 20 and at 55 Cwith a C/N ratio of
30. In addition, modeling the methane production process using
logistic regression, ANFIS, and ANNmodels revealed that the ANFIS
network accurately predicted methane production under both high
andmoderate temperature conditions. The above studies showcase
the tremendous potential of ML in predicting greenhouse gas
emissions fromorganicwaste composting.However, there is limited
research on the use of ML methods for monitoring and controlling
other harmful gases (such as NH3 and N2O) during the composting
process. Subsequent research can delve deeper into investigating
and addressing this gap.

4.3. Other applications

ML not only plays a significant role in predicting compost
maturity, optimizing process parameters, controlling pollution, and
monitoring greenhouse gas emissions but also has shown vast
potential in predicting nutrient recovery efficiency, nitrogen loss,
heat loss, and pressure drop during the composting process.

Hosseinzadeh et al. (2020) evaluated the performance of ANN
and MLR models in predicting nutrient recovery efficiency in ver-
micomposting. Seven chemical and biological indicators were used
as input variables to predict the recovery rates of TN and total
phosphorus. The results demonstrated a significant increase in the
recovery rates of TN and total phosphorus through composting. The
ANN model outperformed the MLR model in predicting TN and
total phosphorus, with TN and C/N ratio being key factors in the
ANN predictions.

Kabak et al. (2022) investigated the impact of physicochemical
parameters on nitrogen loss during the composting process. The
findings revealed that nitrogen loss increased with increasing
temperature and was influenced by factors such as pH, compost
mixing, C/N ratio, and MC. Subsequently, they developed a linear
and nonlinear hybrid tool based on CFNN to predict nitrogen loss,
with the model demonstrating a mean absolute percentage error of
approximately 1%e2%. Through GA optimization, the parameter
values that minimize nitrogen loss were determined.
Boniecki et al. (2013) employed an ANN model to estimate heat
loss during the composting process. The results indicate the
effectiveness of the model in predicting heat release and loss
throughout the composting cycle. Sensitivity analysis revealed the
following six most crucial parameters in descending order: tem-
perature, mineral mass, oxygen content, flow rate, CO2 content, and
process duration. These findings facilitate a better understanding
and optimization of heat utilization in the composting process.

Sidełko et al. (2019) used an ANN model to predict the pressure
drop of organic material beds during composting operations. The
constructed MLP 5-9-1 neural network model exhibited a high
correlation between the predicted and actual values. Variables such
as time, density indicators, and hydraulic load, excluding flow di-
rection, significantly influenced the prediction of airflow resistance.
Statistical evaluationmetrics revealed the high quality of the neural
network, with an R2 value of 0.906 and a standardized residual
range of 4.082e5.453.

5. ML applications for insect treatment of organic waste

In recent years, insect farming technology has seen extensive
use in organic waste treatment because of its economic viability,
low operational costs, high social acceptance, and significant soci-
etal contributions (Ojha et al., 2020; Singh & Kumari, 2019). Insect
farming commonly involves insects such as BSFs, maggots, cock-
roaches, mealworms, and compost worms, which convert organic
waste into high-value insect protein feed and organic fertilizer
products (Addy et al., 2021). Among these, BSF is the most
commonly farmed insect, designated by the Food and Agriculture
Organization of the United Nations as an edible resource insect. BSF
larvae are rich in active proteins, insect fats, probiotics, antimi-
crobial peptides, and chitin and serve as a staple or supplementary
feed for animals (Siva Raman et al., 2022; Surendra et al., 2020). To
date, there have been limited reports on the application of ML in
insect farming. The sparse reports available mainly focus on fore-
casting the expected weight of BSFs, optimizing the farming con-
ditions of BSFs, controlling its lifecycle, and predicting the protein
content of BSF using ML. The application principle of insect farming
technology based on ML is illustrated in Fig. 4.

Arshad et al. (2023) explored the impact of time, larval quantity,
aeration frequency, waste composition, and container surface area
on the efficacy of BSF treatment of kitchenwaste. The conditions for
the BSF treatment of kitchen waste were optimized using an ANN
model and life cycle assessment, achieving an accuracy rate of
99.5%. The optimal conditions included four daily aeration runs,
600 larvae per kilogram of waste, and a stratified feeding process,
resulting in substantial larval weight gain (2.2%e6.5%) and signifi-
cant reductions in kitchenwaste (weight reduction of 70%e93% and
volume reduction of 65%e85% within 15 days).

Muinde et al. (2023) used LR, ridge regression, DT, RF, bagging,
AdaBoost, and XGBoost to determine the optimal BSF farming
conditions. The RF model achieved an RMSE of 2.91 and an R2 value
of 80.9%, effectively predicting the final weight of BSF. The key
factors included bed length, feed formulation, average larval count
per bed, feed depth, and cycle time. This tailored prediction tool not
only estimates the BSF yield but also guides production
optimization.

Proietti et al. (2022) explored the real-time monitoring and
prediction of various stages of the BSF lifecycle using RGB, infrared,
and hyperspectral imaging technologies, along with computer
vision algorithms for image and data collection (Proietti et al.,
2022). They focused on estimating the size/weight and move-
ment/vitality during the pupal stage, the movement/vitality and
temperature anomalies during the larval stage, and the correlation
between larval growth and the selected diet. Their study



12 L. Chen et al. / Circular Economy 3 (2024) 100088

Fig. 4. Principles of ML-based studies on insect farming technology.
contributes to the enhancement of the control of the BSF lifecycle
through noncontact measurements.

Cruz-Tirado et al. employed near-infrared hyperspectral imag-
ing (NIR-HSI) in conjunction with PLS and SVR to develop a pre-
dictive model for the protein content of BSF larvae (Cruz-Tirado
et al., 2023). The results indicated that both the PLS and SVR
models exhibited strong predictive capabilities (RMSEP 1.57%e
1.66%, RPD 2.0e2.5, and protein percentages 25.5%e43.5%).
Furthermore, PCA illuminated the heterogeneous distribution of
chemical compounds within larvae.

6. Challenges and potential prospects of machine learning
applied in biological treatment of organic wastes

6.1. Potential challenges

Although ML demonstrates significant advantages and enor-
mous potential in the biological treatment of organic waste, it also
faces some potential challenges that may hinder its further
development.

(1) Model Selection and Parameter Adjustment: Complex, vari-
able, and unstable data in organic waste processing compli-
cate the selection of an appropriate ML model. Different
models exhibit varying sensitivities and adaptabilities,
requiring a rigorous assessment of their strengths and
weaknesses, along with careful experimentation and vali-
dation. Moreover, optimizing model performance requires
the identification of ideal parameter combinations, which is
challenging because of the extensive and intricate parameter
space within the biological treatment of organic waste.

(2) Explainability and Reliability: ML models are typically
perceived as “black boxes” because of their opaque decision
making processes. This poses a significant challenge in the
field of organic waste biological treatment, where compre-
hending the decisionmaking process of a model is pivotal for
ensuring its reliability. However, numerous ML models lack
sufficient explainability, making it difficult for individuals to
understand their predictive outcomes and decision logic.
Therefore, enhancing the explainability and reliability of ML
models is a critical research direction.
(3) Computational Resources and Time Costs: The training and
inference processes of ML require extensive computational
resources and time. This issue becomes particularly pro-
nounced in the biological treatment of organic waste because
of the vast amounts of data and the complexity of the
models. Therefore, achieving efficient ML applications within
limited computational resources and time constraints is a
significant challenge.

(4) Lack of Practical Engineering Validation: Currently, the
application of ML in biological treatment is mainly confined
to the laboratory or pilot scale. Only through practical engi-
neering validation can the applicability and performance of
ML in biological treatment be more accurately evaluated,
thereby promoting its widespread application and optimized
development. However, practical engineering validation not
only requires adequate resources and financial support but
also necessitates close collaboration with the industry to
jointly address potential issues and challenges.
6.2. Future perspective

The following approaches are considered potential avenues for
further promoting the application of ML in the biological treatment
of organic waste:

(1) Automated Model Selection and Parameter Tuning: Methods
for automating model selection and parameter tuning can
save considerable time and human resources. Furthermore,
these methods can reveal high quality models and configu-
rations that manual tuning may overlook by systematically
exploring the model and parameter space. For instance,
employing automated model selection algorithms, such as
regularization paths, GA, or Bayesian optimization, to choose
the most suitable model for the data; developing AutoML
tools and frameworks such as TPOT or H2OAutoML to auto-
matically select appropriate models and optimize parame-
ters based on data features and prediction objectives (Cheng
et al., 2024).

(2) Research and Application of Explainable ML: To address the
“black-box” nature of ML models, several explainable



L. Chen et al. / Circular Economy 3 (2024) 100088 13
frameworks have been developed to elucidate the contri-
butions of input variables to the model, such as SHAP, LIME,
Shapash, and InterpretML. However, only a few studies have
adopted SHAP in AD (Gupta et al., 2023; Zhang et al., 2023).
Therefore, these explainable methods should find broader
applications in future research on organic waste biological
treatment. In addition, humanecomputer interaction and
feedback techniques appear to be viable paths for enhancing
the explainability of ML models.

(3) Enhancing Computational Efficiency of Computing Plat-
forms: The high computational resources and time required
to process large amounts of data and complex models can be
addressed using various strategies. For instance, leveraging
the elastic scalability of cloud computing resources allows
dynamic adjustment of computational power based on de-
mand. The adoption of distributed computing enables the
parallel processing of decomposed subtasks, thereby
reducing the overall computation time. Furthermore, data
compression and dimensionality reduction, incremental and
online learning, and open-source tools and frameworks
constitute effective avenues for achieving efficient ML
applications.

(4) Strengthen Practical Engineering Application and Validation:
To promote practical engineering applications and valida-
tion, specific measures can include i) conducting on-site
experiments or long-term monitoring in biological treat-
ment facilities to collect real-world data, applying ML
models, and assessing their applicability and robustness in
complex operational environments; ii) enabling data sharing
and collaborative research using real-world biological pro-
cessing facility data to accelerate the application and
advancement of ML techniques, and leveraging lessons
learned from successful implementations in other domains
to refine methods for biological treatment; iii) developing
customized ML solutions tailored to specific biological
treatment facilities and treatment requirements, enabling
better adaptation to actual operational environments and
needs.

7. Conclusions

This review examines the applicability, advantages, and limita-
tions of various ML models in the biological treatment of organic
wastes. According to our findings, ANNs, tree-based models, SVM,
and GAs have emerged as prominent algorithms extensively used in
modeling biological treatment. Detailed analysis of ML applications
in modeling AD, composting, and insect farming processes high-
lights the significant potential of ML in predicting products, opti-
mizing processes, enabling real-time monitoring, and mitigating
pollution emissions. However, despite significant strides, persistent
challenges include complex parameter settings and model selec-
tion, the explainability and adaptability of algorithms, computa-
tional resource demands, and the lack of practical engineering
validation. Future research should prioritize enhancing the efficacy
of ML in biological treatment by automating model selection,
employing explainable ML practices, enhancing the computing ef-
ficiency of the platform, and reinforcing practical engineering
applications.

Author contributions

Long Chen: Conceptualization, Data curation, Formal analysis.
Pinjing He: Investigation, Project administration, Resources, Su-
pervision. Hua Zhang: Resources, Software, Supervision, Valida-
tion. Wei Peng: Supervision, Validation, Visualization. Junjie Qiu:
Software, Validation, Visualization. Fan Lü: Funding acquisition,
Project administration, Resources, Software, Validation,
Visualization.
Declaration of competing interest

The authors declare that they have no known competing
financial interests or personal relationships that could have
appeared to influence the work reported in this paper.
Acknowledgements

All the authors are grateful to the National Natural Science
Foundation of China (52270138) and the International Science and
Technology Cooperation Program of Shanghai Science and Tech-
nology Innovation Action Plan (22230712200) for supporting the
present work.
Electronic Supplementary Material

Supplementary data to this article can be found online at
https://doi.org/10.1016/j.cec.2024.100088.
References

Abdel daiem, M. M., Hatata, A., & Said, N. (2022). Modeling and optimization of
semi-continuous anaerobic co-digestion of activated sludge and wheat straw
using Nonlinear Autoregressive Exogenous neural network and seagull algo-
rithm. Energy, 241, Article 122939.

Addy, M., Huo, S., Liu, J., Li, K., Cheng, P., Schiappacasse, C., Chen, D., Cheng, Y., Liu, Y.,
Ma, Y., et al. (2021). Bioconversion technologies: Insect and worm farming. In
J. Wong, M. Taherzadeh, K. Lasaridi, et al. (Eds.), Current developments in
biotechnology and bioengineering. Amsterdam: Elsevier.

Aghbashlo, M., Peng, W., Tabatabaei, M., Kalogirou, S. A., Soltanian, S., Hosseinza-
deh-Bandbafha, H., Mahian, O., & Lam, S. S. (2021). Machine learning technology
in biodiesel research: A review. Progress in Energy and Combustion Science, 85,
Article 100904.

Alavi, N., Sarmadi, K., Goudarzi, G., Babaei, A. A., Bakhshoodeh, R., & Paydary, P.
(2019). Attenuation of tetracyclines during chicken manure and bagasse co-
composting: Degradation, kinetics, and artificial neural network modeling.
Journal of Environmental Management, 231, 1203e1210.

Almomani, F. (2020). Prediction of biogas production from chemically treated co-
digested agricultural waste using artificial neural network. Fuel, 280, Article
118573.

Arshad, M. Y., Saeed, S., Raza, A., Ahmad, A. S., Urbanowska, A., Jackowski, M., &
Niedzwiecki, L. (2023). Integrating life cycle assessment and machine learning
to enhance black soldier fly larvae-based composting of kitchen waste. Sus-
tainability, 15, Article 12475.

Asadi, M., Guo, H., & McPhedran, K. (2020). Biogas production estimation using
data-driven approaches for cold region municipal wastewater anaerobic
digestion. Journal of Environmental Management, 253, Article 109708.

Awhangbo, L., Schmitt, V., Marcilhac, C., Charnier, C., Latrille, E., & Steyer, J. P. (2024).
Determination of the optimal feed recipe of anaerobic digesters using a
mathematical model and a genetic algorithm. Bioresource Technology, 393,
Article 130091.

Aycan Dümenci, N., Cagcag Yolcu, O., Aydin Temel, F., & Turan, N. G. (2021). Iden-
tifying the maturity of co-compost of olive mill waste and natural mineral
materials: Modelling via ANN and multi-objective optimization. Bioresource
Technology, 338, Article 125516.

Aydın Temel, F., Cagcag Yolcu, O., & Turan, N. G. (2023). Artificial intelligence and
machine learning approaches in composting process: A review. Bioresource
Technology, 370, Article 128539.

Bai, X., Li, Z., Wang, X., He, X., Cheng, S., Bai, X., & Gao, R. (2017). Online measure-
ment of alkalinity in anaerobic co-digestion using linear regression method.
International Journal of Agricultural and Biological Engineering, 10, 176e183.

Bayındır, Y., Cagcag Yolcu, O., Aydın Temel, F., & Turan, N. G. (2022). Evaluation of a
cascade artificial neural network for modeling and optimization of process
parameters in co-composting of cattle manure and municipal solid waste.
Journal of Environmental Management, 318, Article 115496.

Beltramo, T., Klocke, M., & Hitzmann, B. (2019). Prediction of the biogas production
using GA and ACO input features selection method for ANN model. Information
Processing in Agriculture, 6, 349e356.

Bernal, M. P., Alburquerque, J. A., & Moral, R. (2009). Composting of animal manures
and chemical criteria for compost maturity assessment. A review. Bioresource
Technology, 100, 5444e5453.



14 L. Chen et al. / Circular Economy 3 (2024) 100088
Bertolini, M., Mezzogori, D., Neroni, M., & Zammori, F. (2021). Machine learning for
industrial applications: A comprehensive literature review. Expert Systems with
Applications, 175, Article 114820.

Biyada, S., Merzouki, M., Elkarrach, K., & Benlemlih, M. (2020). Spectroscopic
characterization of organic matter transformation during composting of textile
solid waste using UVeVisible spectroscopy, Infrared spectroscopy and X-ray
diffraction (XRD). Microchemical Journal, 159, Article 105314.

Bong, C. P. C., Lim, L. Y., Lee, C. T., Klemes, J. J., Ho, C. S., & Ho, W. S. (2018). The
characterisation and treatment of food waste for improvement of biogas pro-
duction during anaerobic digestioneA review. Journal of Cleaner Production, 172,
1545e1558.

Boniecki, P., Dach, J., Mueller, W., Koszela, K., Przybyl, J., Pilarski, K., & Olszewski, T.
(2013). Neural prediction of heat loss in the pig manure composting process.
Applied Thermal Engineering, 58, 650e655.

Chakraborty, S., Das, B. S., Nasim Ali, M., Li, B., Sarathjith, M. C., Majumdar, K., &
Ray, D. P. (2014). Rapid estimation of compost enzymatic activity by spectral
analysis method combined with machine learning. Waste Management, 34,
623e631.

Chen, L., Hu, J., Han, Q., Zhang, J., Zhou, Z., Zhou, N., Zhou, H., Lu, X., Mi, B., & Wu, F.
(2022a). Resolving the enhancement effect of microwave-assisted pyrolysis on
biochar redox properties from the structure-activity relationship. Journal of
Analytical and Applied Pyrolysis, 167, Article 105706.

Chen, M., Huang, Y., Liu, H., Xie, S., & Abbas, F. (2019). Impact of different nitrogen
source on the compost quality and greenhouse gas emissions during com-
posting of garden waste. Process Safety and Environmental Protection, 124,
326e335.

Chen, J., Jin, C., Sun, S., Yang, D., He, Y., Gan, P., Nalume, W. G., Ma, Y., He, W., & Li, G.
(2023). Recognizing the challenges of composting: Critical strategies for control,
recycling, and valorization of nitrogen loss. Resources, Conservation and Recy-
cling, 198, Article 107172.

Chen, T., Su, P., Shen, Y., Chen, L., Mahmud, M., Zhao, Y., & Antoniou, G. (2022b).
A dominant set-informed interpretable fuzzy system for automated diagnosis of
dementia. Frontiers in Neuroscience, 16, Article 867664.

Cheng, X., Xu, R., Wu, Y., Tang, B., Luo, Y., Huang, W., Wang, F., Fang, S., Feng, Q.,
Cheng, Y., et al. (2024). Predicting and evaluating different pretreatment
methods on methane production from sludge anaerobic digestion via auto-
mated machine learning with ensembled semisupervised learning. ACS ES&T
Engineering, 4, 525e539.

Chiu, M. C., Wen, C. Y., Hsu, H. W., & Wang, W. C. (2022). Key wastes selection and
prediction improvement for biogas production through hybrid machine
learning methods. Sustainable Energy Technologies and Assessments, 52, Article
102223.

Chong, D. J. S., Chan, Y. J., Arumugasamy, S. K., Yazdi, S. K., & Lim, J. W. (2023).
Optimisation and performance evaluation of response surface methodology
(RSM), artificial neural network (ANN) and adaptive neuro-fuzzy inference
system (ANFIS) in the prediction of biogas production from palm oil mill
effluent (POME). Energy, 266, Article 126449.

Cruz, I. A., Andrade, L. R. S., Bharagava, R. N., Nadda, A. K., Bilal, M., Figueiredo, R. T.,
& Ferreira, L. F. R. (2021). An overview of process monitoring for anaerobic
digestion. Biosystems Engineering, 207, 106e119.

Cruz, I. A., Chuenchart, W., Long, F., Surendra, K., Andrade, L. R. S., Bilal, M., Liu, H.,
Figueiredo, R. T., Khanal, S. K., & Ferreira, L. F. R. (2022). Application of machine
learning in anaerobic digestion: Perspectives and challenges. Bioresource
Technology, 345, Article 126433.

Cruz, I. A., Nascimento, V. R. S., Felisardo, R. J. A., dos Santos, A. M. G., de Jesus, A. A.,
de Vasconcelos, B. R., Kumar, V., Cavalcanti, E. B., de Souza, R. L., & Romanholo
Ferreira, L. F. (2023). Evaluation of artificial neural network models for pre-
dictive monitoring of biogas production from cassava wastewater: A training
algorithms approach. Biomass and Bioenergy, 175, Article 106869.

Cruz-Tirado, J. P., Amigo, J. M., & Barbin, D. F. (2023). Determination of protein
content in single black fly soldier (Hermetia illucens L.) larvae by near infrared
hyperspectral imaging (NIR-HSI) and chemometrics. Food Control, 143, Article
109266.

Díaz, M. J., Eugenio, M. E., Lopez, F., García, J. C., & Yan~ez, R. (2012). Neural models
for optimizing lignocellulosic residues composting process. Waste and Biomass
Valorization, 3, 319e331.

Dahunsi, S. O., Oranusi, S., Owolabi, J. B., & Efeovbokhan, V. E. (2016). Mesophilic
anaerobic co-digestion of poultry dropping and Carica papaya peels: Modelling
and process parameter optimization study. Bioresource Technology, 216,
587e600.

de Clercq, D., Jalota, D., Shang, R., Ni, K., Zhang, Z., Khan, A., Wen, Z., Caicedo, L., &
Yuan, K. (2019). Machine learning powered software for accurate prediction of
biogas production: A case study on industrial-scale Chinese production data.
Journal of Cleaner Production, 218, 390e399.

de Clercq, D., Wen, Z., Fei, F., Caicedo, L., Yuan, K., & Shang, R. (2020). Interpretable
machine learning for predicting biomethane production in industrial-scale
anaerobic co-digestion. Science of the Total Environment, 712, Article 134574.

Dias, B. O., Silva, C. A., Higashikawa, F. S., Roig, A., & Sanchez-Monedero, M. A.
(2010). Use of biochar as bulking agent for the composting of poultry manure:
Effect on organic matter degradation and humification. Bioresource Technology,
101, 1239e1246.

Ding, S., Huang, W., Xu, W., Wu, Y., Zhao, Y., Fang, P., Hu, B., & Lou, L. (2022).
Improving kitchen waste composting maturity by optimizing the processing
parameters based on machine learning model. Bioresource Technology, 360,
Article 127606.
Dragoi, E. N., Godini, K., & Koolivand, A. (2021). Modeling of oily sludge composting
process by using artificial neural networks and differential evolution: Predic-
tion of removal of petroleum hydrocarbons and organic carbon. Environmental
Technology & Innovation, 21, Article 101338.

Fajobi, M. O., Lasode, O. A., Adeleke, A. A., Ikubanni, P. P., Balogun, A. O., &
Paramasivam, P. (2023). Prediction of biogas yield from codigestion of ligno-
cellulosic biomass using adaptive neuro-fuzzy inference system (ANFIS) model.
Journal of Engineering, 2023, Article 9335814.

Ferreira, A. J., & Figueiredo, M. A. T. (2012). Boosting algorithms: A review of
methods, theory, and applications. In C. Zhang, & Y. Ma (Eds.), Ensemble machine
learning: Methods and applications. New York, NY: Springer.

Ge, Y., Tao, J., Wang, Z., Chen, C., Mu, L., Ruan, H., Rodríguez Yon, Y., Su, H., Yan, B., &
Chen, G. (2023). Modification of anaerobic digestion model No.1 with Machine
learning models towards applicable and accurate simulation of biomass
anaerobic digestion. Chemical Engineering Journal, 454, Article 140369.

Ghatak, M. D., & Ghatak, A. (2018). Artificial neural network model to predict
behavior of biogas production curve from mixed lignocellulosic co-substrates.
Fuel, 232, 178e189.

Ghersi, D. E., Loubar, K., Amoura, M., & Tazerout, M. (2021). Multi-objective opti-
mization of micro co-generation spark-ignition engine fueled by biogas with
various CH4/CO2 content based on GA-ANN and decision-making approaches.
Journal of Cleaner Production, 329, Article 129739.

Gil, A., Toledo, M., Siles, J., & Martín, M. (2018). Multivariate analysis and biode-
gradability test to evaluate different organic wastes for biological treatments:
Anaerobic co-digestion and co-composting. Waste Management, 78, 819e828.

Goyal, S., Dhull, S. K., & Kapoor, K. K. (2005). Chemical and biological changes during
composting of different organic wastes and assessment of compost maturity.
Bioresource Technology, 96, 1584e1591.

Gueguim Kana, E. B., Oloke, J. K., Lateef, A., & Adesiyan, M. O. (2012). Modeling and
optimization of biogas production on saw dust and other co-substrates using
Artificial Neural network and Genetic Algorithm. Renewable Energy, 46,
276e281.

Guo, H. N., Liu, H. T., & Wu, S. (2022). Simulation, prediction and optimization of
typical heavy metals immobilization in swine manure composting by using
machine learning models and genetic algorithm. Journal of Environmental
Management, 323, Article 116266.

Guo, X. X., Liu, H. T., & Zhang, J. (2020). The role of biochar in organic waste
composting and soil improvement: A review. Waste Management, 102,
884e899.

Guo, H. N., Wu, S. B., Tian, Y., Zhang, J., & Liu, H. T. (2021a). Application of machine
learning methods for the prediction of organic solid waste treatment and
recycling processes: A review. Bioresource Technology, 319, Article 124114.

Guo, X. X.,Wu, S. B.,Wang, X., & Liu, H. T. (2021b). Impact of biochar addition on three-
dimensional structural changes in aggregates associated with humus during
swine manure composting. Journal of Cleaner Production, 280, Article 124380.

Gupta, U., & Gupta, D. (2023). Least squares structural twin bounded support vector
machine on class scatter. Applied Intelligence, 53, 15321e15351.

Gupta, R., Zhang, L., Hou, J., Zhang, Z., Liu, H., You, S., Ok, Y. S., & Li, W. (2023).
Review of explainable machine learning for anaerobic digestion. Bioresource
Technology, 369, Article 128468.

Haffiez, N., Chung, T. H., Zakaria, B. S., Shahidi, M., Mezbahuddin, S., Maal-Bared, R.,
& Dhar, B. R. (2022). Exploration of machine learning algorithms for predicting
the changes in abundance of antibiotic resistance genes in anaerobic digestion.
The Science of the Total Environment, 839, Article 156211.

Hansen, B. D., Tamouk, J., Tidmarsh, C. A., Johansen, R., Moeslund, T. B., &
Jensen, D. G. (2020). Prediction of the methane production in biogas plants
using a combined gompertz and machine learning model. In O. Gervasi,
B. Murgante, S. Misra, et al. (Eds.), Computational science and its applications e
iccsa 2020. Cham: Springer.

Harirchi, S., Wainaina, S., Sar, T., Ali Nojoumi, S., Parchami, M., Parchami, M.,
Varjani, S., Khanal, S. K., Wong, J., Awasthi, M. K., et al. (2022). Microbiological
insights into anaerobic digestion for biogas, hydrogen or volatile fatty acids
(VFAs): A review. Bioengineered, 13, 6521e6557.

Heydari, B., Abdollahzadeh Sharghi, E., Rafiee, S., & Mohtasebi, S. S. (2021). Use of
artificial neural network and adaptive neuro-fuzzy inference system for pre-
diction of biogas production from spearmint essential oil wastewater treatment
in up-flow anaerobic sludge blanket reactor. Fuel, 306, Article 121734.

Hoang, A. T., Varbanov, P. S., Nizetic, S., Sirohi, R., Pandey, A., Luque, R., Ng, K. H., &
Pham, V. V. (2022). Perspective review on Municipal Solid Waste-to-energy
route: Characteristics, management strategy, and role in circular economy.
Journal of Cleaner Production, 359, Article 131897.

Hosseinzadeh, A., Baziar, M., Alidadi, H., Zhou, J. L., Altaee, A., Najafpoor, A. A., &
Jafarpour, S. (2020). Application of artificial neural network and multiple linear
regression in modeling nutrient recovery in vermicompost under different
conditions. Bioresource Technology, 303, Article 122926.

Jacob, S., & Banerjee, R. (2016). Modeling and optimization of anaerobic codigestion
of potato waste and aquatic weed by response surface methodology and arti-
ficial neural network coupled genetic algorithm. Bioresource Technology, 214,
386e395.

Jaroenpoj, S., Yu, Q. J., & Ness, J. (2014). Development of artificial neural network
models for biogas production from co-digestion of leachate and pineapple peel.
The Global Environmental Engineers, 1, 42e47.

Jeong, K., Abbas, A., Shin, J., Son, M., Kim, Y. M., & Cho, K. H. (2021). Prediction of
biogas production in anaerobic co-digestion of organic wastes using deep
learning models. Water Research, 205, Article 117697.



L. Chen et al. / Circular Economy 3 (2024) 100088 15
Jia, R., Song, Y. C., Piao, D., Kim, K., Lee, C., & Park, J. (2022). Exploration of deep
learning models for real-time monitoring of state and performance of anaerobic
digestion with online sensors. Bioresource Technology, 363, Article 127908.

Jiang, J., Han, G., Liu, L., Shu, L., & Guizani, M. (2020). Outlier detection approaches
based on machine learning in the internet-of-things. IEEE Wireless Communi-
cations, 2, 53e59.

Jimenez, J., Guardia-Puebla, Y., Cisneros-Ortiz, M., Morgan-Sagastume, J., Guerra, G.,
& Noyola, A. (2015). Optimization of the specific methanogenic activity during
the anaerobic co-digestion of pig manure and rice straw, using industrial clay
residues as inorganic additive. Chemical Engineering Journal, 259, 703e714.

Jolliffe, I. T., & Cadima, J. (2016). Principal component analysis: A review and recent
developments. Philosophical Transactions of the Royal Society A: Mathematical,
Physical & Engineering Sciences, 374, Article 20150202.

Kabak, E. T., Cagcag Yolcu, O., Aydın Temel, F., & Turan, N. G. (2022). Prediction and
optimization of nitrogen losses in co-composting process by using a hybrid
cascaded prediction model and genetic algorithm. Chemical Engineering Journal,
437, Article 135499.

Kainthola, J., Kalamdhad, A. S., & Goud, V. V. (2020). Optimization of process pa-
rameters for accelerated methane yield from anaerobic co-digestion of rice
straw and food waste. Renewable Energy, 149, 1352e1359.

Kang, J., Yin, Z., Pei, F., Ye, Z., Song, G., Ling, H., Gao, D., Jiang, X., Zhang, C., & Ge, J.
(2022). Aerobic composting of chicken manure with penicillin G: Community
classification and quorum sensing mediating its contribution to humification.
Bioresource Technology, 352, Article 127097.

Kazemi, P., Steyer, J. P., Bengoa, C., Font, J., & Giralt, J. (2020). Robust data-driven soft
sensors for online monitoring of volatile fatty acids in anaerobic digestion
processes. Processes, 8, 67.

Kettaneh, N., Berglund, A., & Wold, S. (2005). PCA and PLS with very large data sets.
Computational Statistics & Data Analysis, 48, 69e85.

Khan, M., Chuenchart, W., Surendra, K. C., & Kumar Khanal, S. (2023). Applications
of artificial intelligence in anaerobic co-digestion: Recent advances and pros-
pects. Bioresource Technology, 370, Article 128501.

Khan, M. A., Ngo, H. H., Guo, W. S., Liu, Y., Nghiem, L. D., Hai, F. I., Deng, L. J., Wang, J.,
& Wu, Y. (2016). Optimization of process parameters for production of volatile
fatty acid, biohydrogen and methane from anaerobic digestion. Bioresource
Technology, 219, 738e748.

Khashaba, N. H., Ettouney, R. S., Abdelaal, M. M., Ashour, F. H., & El-Rifai, M. A. (2022).
Artificial neural networkmodeling of biochar enhanced anaerobic sewage sludge
digestion. Journal of Environmental Chemical Engineering, 10, Article 107988.

Komilis, D. P., & Tziouvaras, I. S. (2009). A statistical analysis to assess the maturity
and stability of six composts. Waste Management, 29, 1504e1513.

Krmar, J., Vukicevic, M., Kovacevic, A., Protic, A., Zecevic, M., & Otasevic, B. (2020).
Performance comparison of nonlinear and linear regression algorithms coupled
with different attribute selection methods for quantitative structure - retention
relationships modelling in micellar liquid chromatography. Journal of Chroma-
tography A, 1623, Article 461146.

Kujawa, S., Mazurkiewicz, J., & Czekała, W. (2020). Using convolutional neural
networks to classify the maturity of compost based on sewage sludge and
rapeseed straw. Journal of Cleaner Production, 258, Article 120814.

Kunatsa, T., & Xia, X. (2022). A review on anaerobic digestion with focus on the role
of biomass co-digestion, modelling and optimisation on biogas production and
enhancement. Bioresource Technology, 344, Article 126311.

Leit~ao, R. C., van Haandel, A. C., Zeeman, G., & Lettinga, G. (2006). The effects of
operational and environmental variations on anaerobic wastewater treatment
systems: A review. Bioresource Technology, 97, 1105e1118.

Li, C., He, P., Peng, W., Lü, F., Du, R., & Zhang, H. (2022a). Exploring available input
variables for machine learning models to predict biogas production in
industrial-scale biogas plants treating food waste. Journal of Cleaner Production,
380, Article 135074.

Li, Y., Li, S., Sun, X., & Hao, D. (2022d). Prediction of carbon dioxide production from
green waste composting and identification of critical factors using machine
learning algorithms. Bioresource Technology, 360, Article 127587.

Li, S., Sun, K., Latif, A., Si, Y., Gao, Y., & Huang, Q. (2022c). Insights into the appli-
cations of extracellular laccase-aided humification in livestock manure com-
posting. Environmental Science & Technology, 56, 7412e7425.

Li, Y., Xue, Z., Li, S., Sun, X., & Hao, D. (2023). Prediction of composting maturity and
identification of critical parameters for green waste compost using machine
learning. Bioresource Technology, 385, Article 129444.

Li, J., Zhang, L., Li, C., Tian, H., Ning, J., Zhang, J., Tong, Y. W., & Wang, X. (2022b).
Data-driven based In-depth interpretation and inverse design of anaerobic
digestion for CH4-rich biogas production. ACS ES&T Engineering, 2, 642e652.

Lohri, C. R., Diener, S., Zabaleta, I., Mertenat, A., & Zurbrügg, C. (2017). Treatment
technologies for urban solid biowaste to create value products: A review with
focus on low- and middle-income settings. Reviews in Environmental Science
and Biotechnology, 16, 81e130.

Long, F., Wang, L., Cai, W., Lesnik, K., & Liu, H. (2021). Predicting the performance of
anaerobic digestion using machine learning algorithms and genomic data.
Water Research, 199, Article 117182.

Lv, Y., Bao, J., Li, S., Liu, D., Dai, D., Qv, M., & Zhu, L. (2022). Biochar amendment of
aerobic composting for the effective biodegradation of heavy oil and succession
of bacterial community. Bioresource Technology, 362, Article 127820.

Machineni, L., & Anupoju, G. R. (2023). Optimization of biomethane production
from sweet sorghum bagasse using artificial neural networks combined with
particle swarm algorithm. Environmental Science and Pollution Research, 30,
114095e114110.
Matheri, A. N., Sethunya, V. L., Belaid, M., &Muzenda, E. (2018). Analysis of the biogas
productivity from dry anaerobic digestion of organic fraction of municipal solid
waste. Renewable and Sustainable Energy Reviews, 81, 2328e2334.

Mo, R., Guo, W., Batstone, D., Makinia, J., & Li, Y. (2023). Modifications to the
anaerobic digestion model no. 1 (ADM1) for enhanced understanding and
application of the anaerobic treatment processes e a comprehensive review.
Water Research, 244, Article 120504.

Moncks, P. C. S., Corrêa, E. K., Guidoni, L. L. C., Moncks, R. B., Corrêa, L. B., Lucia Jr, T.,
Araujo, R. M., Yamin, A. C., & Marques, F. S. (2022). Moisture content monitoring
in industrial-scale composting systems using low-cost sensor-based machine
learning techniques. Bioresource Technology, 359, Article 127456.

Muinde, J., Tanga, C. M., Olukuru, J., Odhiambo, C., Tonnang, H. E. Z., & Senagi, K.
(2023). Application of machine learning techniques to discern optimal rearing
conditions for improved black soldier fly farming. Insects, 14, 479.

Najafi, B., & Ardabili, S. F. (2018). Application of ANFIS, ANN, and logistic methods in
estimating biogas production from spent mushroom compost (SMC). Resources,
Conservation and Recycling, 133, 169e178.

Neto, J. G., Ozorio, L. V., Abreu, T. C. C. D., Santos, B. F., & Pradelle, F. (2021). Modeling
of biogas production from food, fruits and vegetables wastes using artificial
neural network (ANN). Fuel, 285, Article 119081.

Nguyen, D., Gadhamshetty, V., Nitayavardhana, S., & Khanal, S. K. (2015). Automatic
process control in anaerobic digestion technology: A critical review. Bioresource
Technology, 193, 513e522.

Nie, E., He, P., Peng, W., Zhang, H., & Lü, F. (2023). Microbial volatile organic com-
pounds as novel indicators of anaerobic digestion instability: Potential and
challenges. Biotechnology Advances, 67, Article 108204.

Obileke, K., Tangwe, S., Makaka, G., & Mukumba, P. (2023). Comparison of prediction
of biogas yield in a batch mode underground fixed dome digester with cow
dung. Biomass Conversion and Biorefinery. https://doi.org/10.1007/s13399-023-
04593-z

Ojha, S., Bußler, S., & Schlüter, O. K. (2020). Food waste valorisation and circular
economy concepts in insect production and processing.Waste Management, 118,
600e609.

Okwu, M. O., Samuel, O. D., Ewim, D. R. E., & Huan, Z. (2021). Estimation of biogas
yields produced from combination of waste by implementing response surface
methodology (RSM) and adaptive neuro-fuzzy inference system (ANFIS). In-
ternational Journal of Energy and Environmental Engineering, 12, 353e363.

Okwu, M. O., Samuel, O. D., Otanocha, O. B., Tartibu, L. K., Omoregbee, H. O., &
Mbachu, V. M. (2023). Development of ternary models for prediction of biogas
yield in a novel modular biodigester: A case of fuzzy Mamdani model (FMM),
artificial neural network (ANN), and response surface methodology (RSM).
Biomass Conversion and Biorefinery, 13, 917e926.

Olatunji, K. O., Ahmed, N. A., Madyira, D. M., Adebayo, A. O., Ogunkunle, O., &
Adeleke, O. (2022). Performance evaluation of ANFIS and RSM modeling in
predicting biogas and methane yields from Arachis hypogea shells pretreated
with size reduction. Renewable Energy, 189, 288e303.

Oloko-Oba, M. I., Taiwo, A. E., Ajala, S. O., Solomon, B. O., & Betiku, E. (2018). Per-
formance evaluation of three different-shaped bio-digesters for biogas pro-
duction and optimization by artificial neural network integrated with genetic
algorithm. Sustainable Energy Technologies and Assessments, 26, 116e124.

Pisner, D. A., & Schnyer, D. M. (2020). Support vector machine. In A. Mechelli, &
S. Vieira (Eds.), Machine learning. Amsterdam: Elsevier.

Pornsing, C., Sodhi, M. S., & Lamond, B. F. (2016). Novel self-adaptive particle swarm
optimization methods. Soft Computing, 20, 3579e3593.

Proietti, M., Marini, A., Garinei, A., Rossi, G., Bianchi, F., Marconi, M., Discepolo, S.,
Martarelli, M., Calcagni, M. T., Zeni, G., et al. (2022). Non-invasive measure-
ments for characterization of Hermetia Illucens (BSF) life cycle in rearing plant.
In Proceedings of the 2022 IEEE workshop on metrology for agriculture and forestry
(MetroAgriFor) (Perugia, Italy).

Puyol, D., Batstone, D. J., Hülsen, T., Astals, S., Peces, M., & Kro€mer, J. O. (2017).
Resource recovery from wastewater by biological technologies: Opportunities,
challenges, and prospects. Frontiers in Microbiology, 7, 2106.

Ramachandran, A., Rustum, R., & Adeloye, A. J. (2019). Review of anaerobic digestion
modeling and optimization using nature-inspired techniques. Processes, 7, 953.

Renner, G., & Ekart, A. (2003). Genetic algorithms in computer aided design. Com-
puter-Aided Design, 35, 709e726.

Rigdon, E. E. (2012). Rethinking partial least squares path modeling: In praise of
simple methods. Long Range Planning, 45, 341e358.

Sakiewicz, P., Piotrowski, K., Ober, J., & Karwot, J. (2020). Innovative artificial neural
network approach for integrated biogas e wastewater treatment system
modelling: Effect of plant operating parameters on process intensification.
Renewable and Sustainable Energy Reviews, 124, Article 109784.

Sangeetha, J., & Govindarajan, P. (2023). Prediction of agricultural waste compost
maturity using fast regions with convolutional neural network(R-CNN). Mate-
rials Today: Proceedings. https://doi.org/10.1016/j.matpr.2023.01.112

Sappl, J., Harders, M., & Rauch, W. (2023). Machine learning for quantile regression
of biogas production rates in anaerobic digesters. The Science of the Total
Environment, 872, Article 161923.

Senthilkumar, N., Deepanraj, B., Vasantharaj, K., & Sivasubramanian, V. (2016).
Optimization and performance analysis of process parameters during anaerobic
digestion of food waste using hybrid GRA-PCA technique. Journal of Renewable
and Sustainable Energy, 8, Article 063107.

Sharma, P., Gaur, V. K., Kim, S. H., & Pandey, A. (2020). Microbial strategies for bio-
transforming food waste into resources. Bioresource Technology, 299, Article
122580.



16 L. Chen et al. / Circular Economy 3 (2024) 100088
Shehadeh, A., Alshboul, O., Al Mamlook, R. E., & Hamedat, O. (2021). Machine
learning models for predicting the residual value of heavy construction
equipment: An evaluation of modified decision tree, LightGBM, and XGBoost
regression. Automation in Construction, 129, Article 103827.

Shen, G., Chen, Y., Zhang, J., Wu, Y., Yi, Y., Li, S., & Yin, S. (2023). Quantitative analysis
of index factors in agricultural compost by infrared spectroscopy. Heliyon, 9,
Article e14010.

Shi, C. F., Yang, H. T., Chen, T. T., Guo, L. P., Leng, X. Y., Deng, P. B., Bi, J., Pan, J. G., &
Wang, Y. M. (2022). Artificial neural network-genetic algorithm-based optimi-
zation of aerobic composting process parameters of Ganoderma lucidum res-
idue. Bioresource Technology, 357, Article 127248.

Sidełko, R., Janowska, B., Szymanski, K., Mostowik, N., & Głowacka, A. (2019).
Advanced methods to calculation of pressure drop during aeration in com-
posting process. The Science of the Total Environment, 674, 19e25.

Singh, A., & Kumari, K. (2019). An inclusive approach for organic waste treatment
and valorisation using black soldier fly larvae: A review. Journal of Environ-
mental Management, 251, Article 109569.

Sipma, J., Osuna, M. B., Emanuelsson, M. A. E., & Castro, P. M. L. (2010). Biotreatment
of industrial wastewaters under transient-state conditions: Process stability
with fluctuations of organic load, substrates, toxicants, and environmental
parameters. Critical Reviews in Environmental Science and Technology, 40,
147e197.

Siva Raman, S., Stringer, C. L., Bruce, C. N., & Chong, S. C. (2022). Opportunities,
challenges and solutions for black soldier fly larvae-based animal feed pro-
duction. Journal of Cleaner Production, 373, Article 133802.

Sun, Y., Dai, H. L., Moayedi, H., Nguyen Le, B., & Muhammad Adnan, R. (2024).
Predicting steady-state biogas production from waste using advanced machine
learning-metaheuristic approaches. Fuel, 355, Article 129493.

Surendra, K. C., Tomberlin, J. K., van Huis, A., Cammack, J. A., Heckmann, L. H. L., &
Khanal, S. K. (2020). Rethinking organic wastes bioconversion: Evaluating the
potential of the black soldier fly (Hermetia illucens (L.)) (Diptera: Strat-
iomyidae) (BSF). Waste Management, 117, 58e80.

Tang, L., Zeng, G., Liu, J., Xu, X., Zhang, Y., Shen, G., Li, Y., & Liu, C. (2008). Catechol
determination in compost bioremediation using a laccase sensor and artificial
neural networks. Analytical and Bioanalytical Chemistry, 391, 679e685.

Tedeschi, L. O. (2006). Assessment of the adequacy of mathematical models. Agri-
cultural Systems, 89, 225e247.

Todeschini, R., Consonni, V., Mauri, A., & Pavan, M. (2004). Detecting “bad”
regression models: Multicriteria fitness functions in regression analysis. Ana-
lytica Chimica Acta, 515, 199e208.

Tufaner, F., & Demirci, Y. (2020). Prediction of biogas production rate from anaerobic
hybrid reactor by artificial neural network and nonlinear regressions models.
Clean Technologies and Environmental Policy, 22, 713e724.

Uddin, S., Haque, I., Lu, H., Ali Moni, M., & Gide, E. (2022). Comparative performance
analysis of K-nearest neighbour (KNN) algorithm and its different variants for
disease prediction. Scientific Reports, 12, 6256.

Vergnoux, A., Guiliano, M., Le Dreau, Y., Kister, J., Dupuy, N., & Doumenq, P. (2009).
Monitoring of the evolution of an industrial compost and prediction of some
compost properties by NIR spectroscopy. Science of the Total Environment, 407,
2390e2403.

Waltham, B., & O€rmeci, B. (2020). Fluorescence intensity, conductivity, and UVevis
absorbance as surrogate parameters for real-time monitoring of anaerobic
digestion of wastewater sludge. Journal of Water Process Engineering, 37, Article
101395.

Wan, X., Li, J., Xie, L., Wei, Z., Wu, J., Wah Tong, Y., Wang, X., He, Y., & Zhang, J. (2022).
Machine learning framework for intelligent prediction of compost maturity
towards automation of food waste composting system. Bioresource Technology,
365, Article 128107.

Wang, X., Bai, X., Li, Z., Zhou, X., Cheng, S., Sun, J., & Liu, T. (2018). Evaluation of
artificial neural network models for online monitoring of alkalinity in anaerobic
co-digestion system. Biochemical Engineering Journal, 140, 85e92.

Wang, Y., Huntington, T., & Scown, C. D. (2021). Tree-based automated machine
learning to predict biogas production for anaerobic co-digestion of organic
waste. ACS Sustainable Chemistry & Engineering, 9, 12990e13000.

Wang, Y., Ma, F., Zhu, T., Liu, Z., Ma, Y., Li, T., & Hao, L. (2023a). Electric heating
promotes sludge composting process: Optimization of heating method through
machine learning algorithms. Bioresource Technology, 382, Article 129177.

Wang, Z., Peng, X., Xia, A., Shah, A. A., Yan, H., Huang, Y., Zhu, X., Zhu, X., & Liao, Q.
(2023b). Comparison of machine learning methods for predicting the methane
production from anaerobic digestion of lignocellulosic biomass. Energy, 263,
Article 125883.

Wang, X., Rashid, I., Zhao, Z., Oladele, M., Xiang, W., Huang, Y., Wazer, E.,
McCutcheon, J., Bollas, G., Contreras, J., et al. (2024). Machine learning algorithm
integrated with real-time In situ sensors and physiochemical principle-driven
soft sensors toward an anaerobic digestion-data fusion framework. ACS ES&T
Water, 4, 1061e1072.
Ward, A. J., Hobbs, P. J., Holliman, P. J., & Jones, D. L. (2011). Evaluation of near
infrared spectroscopy and software sensor methods for determination of total
alkalinity in anaerobic digesters. Bioresource Technology, 102, 4083e4090.

Wu, G., Kechavarzi, C., Li, X., Wu, S., Pollard, S. J. T., Sui, H., & Coulon, F. (2013).
Machine learning models for predicting PAHs bioavailability in compost
amended soils. Chemical Engineering Journal, 223, 747e754.

Wu, D., Li, L., Zhao, X., Peng, Y., Yang, P., & Peng, X. (2019). Anaerobic digestion: A
review on process monitoring. Renewable and Sustainable Energy Reviews, 103,
1e12.

Wu, L., Wei, W., Song, L., Wozniak-Karczewska, M., Chrzanowski, Ł., & Ni, B. J.
(2021). Upgrading biogas produced in anaerobic digestion: Biological removal
and bioconversion of CO2 in biogas. Renewable and Sustainable Energy Reviews,
150, Article 111448.

Xie, S., Hai, F. I., Zhan, X., Guo, W., Ngo, H. H., Price, W. E., & Nghiem, L. D. (2016).
Anaerobic co-digestion: A critical review of mathematical modelling for per-
formance optimization. Bioresource Technology, 222, 498e512.

Xu, R. Z., Cao, J. S., Wu, Y., Wang, S. N., Luo, J. Y., Chen, X., & Fang, F. (2020). An
integrated approach based on virtual data augmentation and deep neural
networks modeling for VFA production prediction in anaerobic fermentation
process. Water Research, 184, Article 116103.

Xue, W., Hu, X., Wei, Z., Mei, X., Chen, X., & Xu, Y. (2019). A fast and easy method for
predicting agricultural waste compost maturity by image-based deep learning.
Bioresource Technology, 290, Article 121761.

Yılmaz, E. C., Aydın Temel, F., Cagcag Yolcu, O., & Turan, N. G. (2022). Modeling and
optimization of process parameters in co-composting of tea waste and food
waste: Radial basis function neural networks and genetic algorithm. Bioresource
Technology, 363, Article 127910.

Yang, Y., Kumar Awasthi, M., Du, W., Ren, X., Lei, T., & Lv, J. (2020). Compost sup-
plementation with nitrogen loss and greenhouse gas emissions during pig
manure composting. Bioresource Technology, 297, Article 122435.

Yang, G., Li, Y., Zhen, F., Xu, Y., Liu, J., Li, N., Sun, Y., Luo, L.,Wang,M., & Zhang, L. (2021a).
Biochemical methane potential prediction for mixed feedstocks of straw and
manure in anaerobic co-digestion. Bioresource Technology, 326, Article 124745.

Yang, Y., Wang, G., Li, G., Ma, R., Kong, Y., & Yuan, J. (2021b). Selection of sensitive
seeds for evaluation of compost maturity with the seed germination index.
Waste Management, 136, 238e243.

Yildirim, O., & Ozkaya, B. (2023). Prediction of biogas production of industrial scale
anaerobic digestion plant by machine learning algorithms. Chemosphere, 335,
Article 138976.

Yuan, H., & Zhu, N. (2016). Progress in inhibition mechanisms and process control of
intermediates and by-products in sewage sludge anaerobic digestion. Renew-
able and Sustainable Energy Reviews, 58, 429e438.

Zaied, B. K., Rashid, M., Nasrullah, M., Bari, B. S., Zularisam, A. W., Singh, L.,
Kumar, D., & Krishnan, S. (2023). Prediction and optimization of biogas pro-
duction from POME co-digestion in solar bioreactor using artificial neural
network coupled with particle swarm optimization (ANN-PSO). Biomass Con-
version and Biorefinery, 13, 73e88.

Zamri, M. F. M. A., Hasmady, S., Akhiar, A., Ideris, F., Shamsuddin, A. H., Mofijur, M.,
Rizwanul Fattah, I. M., & Mahlia, T. M. I. (2021). A comprehensive review on
anaerobic digestion of organic fraction of municipal solid waste. Renewable and
Sustainable Energy Reviews, 137, Article 110637.

Zareei, S., & Khodaei, J. (2017). Modeling and optimization of biogas production
from cow manure and maize straw using an adaptive neuro-fuzzy inference
system. Renewable Energy, 114, 423e427.

Zhan, Y., & Zhu, J. (2024). Response surface methodology and artificial neural
network-genetic algorithm for modeling and optimization of bioenergy pro-
duction from biochar-improved anaerobic digestion. Applied Energy, 355, Article
122336.

Zhang, Y., Feng, Y., Ren, Z., Zuo, R., Zhang, T., Li, Y., Wang, Y., Liu, Z., Sun, Z., Han, Y., &
Feng, L. (2023). Tree-based machine learning model for visualizing complex
relationships between biochar properties and anaerobic digestion. Bioresource
Technology, 374, Article 128746.

Zhang, Y., Li, L., Ren, Z., Yu, Y., Li, Y., Pan, J., Lu, Y., Feng, L., Zhang, W., & Han, Y.
(2022). Plant-scale biogas production prediction based on multiple hybrid
machine learning technique. Bioresource Technology, 363, Article 127899.

Zhang, Y., Li, W. W., Zeng, G. M., Tang, L., Feng, C. L., Huang, D. L., & Li, Y. P. (2009).
Novel neural network-based prediction model for quantifying hydroquinone in
compost with biosensor measurements. Environmental Engineering Science, 26,
1063e1070.

Zhang, S., Li, X., Zong, M., Zhu, X., & Wang, R. (2018). Efficient kNN classification
with different numbers of nearest neighbors. IEEE Transactions on Neural Net-
works and Learning Systems, 29, 1774e1785.

Zhou, Y., Tang, L., Zeng, G., Zhang, Y., Li, Z., Liu, Y., Chen, J., Yang, G., Zhou, L., &
Zhang, S. (2014). Simultaneous determination of hydroquinone and catechol in
compost bioremediation using a tyrosinase biosensor and artificial neural
networks. Analytical Methods, 6, 2371e2378.