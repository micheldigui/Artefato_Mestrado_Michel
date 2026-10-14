---
source_file: "2025-Large language models are less effective at clinical prediction task than locally trained machine learning.txt"
original_rel_path: "Trabalhos\Artigos\Aproveitar parcialmente\txt\2025-Large language models are less effective at clinical prediction task than locally trained machine learning.txt"
category: "Artigos_Aproveitar_parcialmente"
extension: ".txt"
sha256: "c43428be03c33586b849fd551328234070bc4451e0c730b2e08336a691528372"
extracted_at: "2026-09-20T00:50:21.705547"
---

﻿Journal of the American Medical Informatics Association, 2025, 1–12 
https://doi.org/10.1093/jamia/ocaf038 
Research and Applications 

Research and Applications

Large language models are less effective at clinical 
prediction tasks than locally trained machine learning 
models
Katherine E. Brown , PhD�,1, Chao Yan , PhD1, Zhuohang Li , MS2, Xinmeng Zhang , BS2,  
Benjamin X. Collins , MD, MS1, You Chen , PhD1,2, Ellen Wright Clayton , MD, JD3,4,5,  
Murat Kantarcioglu , PhD6, Yevgeniy Vorobeychik , PhD7, Bradley A. Malin , PhD1,2,8 

1Department of Biomedical Informatics, Vanderbilt University Medical Center (VUMC), Nashville, TN 37203, United States, 2Department of 
Computer Science, Vanderbilt University, Nashville, TN 37212, United States, 3Law School, Vanderbilt University, Nashville, TN 37203, United 
States, 4Department of Health Policy, Vanderbilt University Medical Center (VUMC), Nashville, TN 37203, United States, 5Department of 
Pediatrics, Vanderbilt University Medical Center (VUMC), Nashville, TN 37232, United States, 6Department of Computer Science, Virginia 
Tech, Blacksburg, VA 24061, United States, 7Department of Computer Science, Washington University, St. Louis, MO 63130, United States, 
8Department of Biostatistics, Vanderbilt University Medical Center (VUMC), Nashville, TN 37203, United States
�Corresponding author: Katherine E. Brown, PhD, Department of Biomedical Informatics, Vanderbilt University Medical Center (VUMC), Suite 1475, 
2525 West End Avenue, Nashville, TN 37203, United States (katherine.brown@vumc.org)

Abstract
Objectives: To determine the extent to which current large language models (LLMs) can serve as substitutes for traditional machine learning 
(ML) as clinical predictors using data from electronic health records (EHRs), we investigated various factors that can impact their adoption, 
including overall performance, calibration, fairness, and resilience to privacy protections that reduce data fidelity.
Materials and Methods: We evaluated GPT-3.5, GPT-4, and traditional ML (as gradient-boosting trees) on clinical prediction tasks in EHR data 
from Vanderbilt University Medical Center (VUMC) and MIMIC IV. We measured predictive performance with area under the receiver operating 
characteristic (AUROC) and model calibration using Brier Score. To evaluate the impact of data privacy protections, we assessed AUROC when 
demographic variables are generalized. We evaluated algorithmic fairness using equalized odds and statistical parity across race, sex, and age 
of patients. We also considered the impact of using in-context learning by incorporating labeled examples within the prompt.
Results: Traditional ML [AUROC: 0.847, 0.894 (VUMC, MIMIC)] substantially outperformed GPT-3.5 (AUROC: 0.537, 0.517) and GPT-4 
(AUROC: 0.629, 0.602) (with and without in-context learning) in predictive performance and output probability calibration [Brier Score (ML vs 
GPT-3.5 vs GPT-4): 0.134 vs 0.384 vs 0.251, 0.042 vs 0.06 vs 0.219)].
Discussion: Traditional ML is more robust than GPT-3.5 and GPT-4 in generalizing demographic information to protect privacy. GPT-4 is the fair
est model according to our selected metrics but at the cost of poor model performance.
Conclusion: These findings suggest that non-fine-tuned LLMs are less effective and robust than locally trained ML for clinical prediction tasks, 
but they are improving across releases.
Key words: large language models; clinical prediction models; fairness; privacy. 

Introduction power, and personnel that academic medical centers possess.8

Making predictions is a vital part of healthcare, with common More recently developed ML technologies, such as large lan
applications, including estimating the likelihood of a specific guage models (LLMs), have hinted at a potential to mitigate 
diagnosis,1–3 assessing the suitability of a medication,4,5 and these challenges and fundamentally change the integration of 

ML in medicine. Closed-source LLMs, such as GPT-3.5,9determining a patient’s readiness for discharge.6 Over the past 
several decades, the practice of medicine has evolved from clin GPT-4,10 and Claude,11 are pre-trained and can be interacted 
ical intuition to incorporate data-driven guidance, which is with conversationally, characteristics that reduce technical 
increasingly aided by artificial intelligence (AI) and particularly friction required to create or use ML (or more broadly, AI) 
machine learning (ML). While model development has for healthcare settings. LLMs have been used to aid in vari
advanced, it is widely recognized that implementing ML mod ous tasks, including drafting patient messages,12 optimizing 
els successfully often requires training on or fine-tuning (eg, clinical decision support,13 developing phenotyping algo
via transfer learning)7 with local, representative data.1,2 rithms,14 and summarizing patient encounters.15 There have 

However, not all institutions have sufficient resources to been recent investigations into the performance16–19 and fair
implement ML effectively. For instance, community hospitals ness20 of LLMs versus traditional ML and other diagnostic 
may lack the volume of ML-ready data, computational aids.17,21 More recently, Chen et al22 analyzed a wide range 

Received: November 11, 2024; Revised: January 31, 2025; Editorial Decision: February 20, 2025; Accepted: February 21, 2025 
© The Author(s) 2025. Published by Oxford University Press on behalf of the American Medical Informatics Association.   
This is an Open Access article distributed under the terms of the Creative Commons Attribution License (https://creativecommons.org/licenses/by/4.0/), which 
permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited. 

Downloaded from https://academic.oup.com/jamia/advance-article/doi/10.1093/jamia/ocaf038/8064348 by guest on 11 March 2025



2                                                                                                J o u r n al of the American Medical Informatics Association, 2025, Vol. 00, No. 0 

of LLMs for clinical prediction tasks; however, a number of Datasets
critical aspects, including reliability and robustness (eg, This study relied on several EHR-derived datasets from 
model calibration) of these tools, remain unknown. Given the VUMC and BIDMC. Table S2 provides distributions for the 
rapid pace at which LLMs are growing in their production,23

entire datasets and the LLM evaluation set. Missing categori
it is critical to quantify their strengths and weaknesses to cal features are replaced with a “?”. Missing numeric features 
ensure responsible use. were replaced with −1. We opted for this strategy because we 

To learn more about the efficacy of LLMs for clinical pre assume that a clinician interfacing with an LLM may not use 
diction, several aspects of real-world implementation need to statistical imputation procedures. The MIMIC-IV and 
be considered. First, we need to represent the type of users MIMIC-IV ED datasets (n¼393 576) contain hospital 
and constraints that may limit how LLMs are applied in a admission records and ED records, respectively, for 
healthcare setting. In this study, we consider 2 distinct types BIDMC.26–28 From these, we derived a dataset to predict if a 
of clinical users: (1) the everyday user, whose goal is to patient will be transferred to an ICU within 24 hours of hos
retrieve an answer using a single LLM query (ie, zero-shot pital admission based on their presentation during ED triage. 
prompting) and (2) the advanced user who utilizes retrieval In this dataset, the predictors include race, age, arrival trans
augmented generation (RAG) to contextually present the port type, triage vital signs, and the number of ED, ICU, and 
LLM with similar cases or additional relevant examples in inpatient hospital stays for the past 30, 90, and 365 days.
the prompt to augment its decision-making capabilities for The VUMC dataset (n¼ 28 880) was developed to predict 
better results. In-context learning is such a strategy that helps the likelihood of patient discharge from the hospital within 
guide LLM inference.16 We assume that the end-user is a clin 24 hours.6 We ran preliminary experiments using gradient- 
ical professional who will use the output of the LLM in sup boosted trees implemented with CatBoost.29 We predicted 
port of their activities.24 Clinicians are not expected to the likelihood of discharge using the demographic and audit 
blindly accept the output of the LLM as their sole source of log data features. We then calculated feature importance 
information in decision-making; however, analyzing the based on changes in the loss function (implemented within 
downstream effects of the LLM’s prediction as a clinical deci the CatBoost library) and selected the 15 most important 
sion support tool is outside the scope of this work. audit log features. Those features and the demographic fea

Second, privacy concerns can limit the amount of patient tures—race, age, current day of week, insurance type, and 
information that can be supplied to an LLM under the con Area Deprivation Index30 of residence—were relied upon in 
trol of a third party, such as OpenAI, as these technologies this portion of our study.
risk exposing protected health information (PHI) to organiza
tions that are neither covered entities nor their business asso GPT
ciates as required by the Health Insurance Portability and Our experiments were run on a HIPAA-compliant Azure 
Accountability Act (HIPAA). Thus, it is likely that patient instantiation of OpenAI’s Generative Pre-trained Trans
data would need to be de-identified before submission to the former10 (GPT) to guard PHI. We utilized GPT-3.5 and GPT- 
LLM. Moreover, while this may address the privacy require 4, with temperature set to 0 (to reduce the likelihood of 
ments of federal regulations, such as the HIPAA Privacy extraneous text being generated) and the maximum number 
Rule, evidence suggests that as data detail is reduced, the pre of tokens set to 1024. We randomly selected 1500 data 
dictive performance of ML is weakened.25 The impact on points from each dataset to query LLMs under a random 
LLMs, however, remains unclear. Third, many commercial sampling assumption to ensure results and claims are 
LLMs do not provide detailed documentation of their archi unbiased. The features for each dataset were represented in 
tecture or training data. As a result, reproducibility and the JSON. Table S2 specifies specific prompt structures for each 
design of formal evaluation frameworks are limited for pre dataset. We considered both zero-shot prompting (not pro
diction tasks in healthcare. viding additional examples) and few-shot examples (see 

In this study, we evaluate the utility, privacy, and fairness of below). We prompted the LLM to provide a prediction and a 
LLMs compared to traditional ML, using electronic health likelihood of correctness (Table S2) and used this output in 
record (EHR) data from Vanderbilt University Medical Center our analysis.
(VUMC)6 to predict the likelihood of patient discharge from 
the hospital within 24 hours and the public-use MIMIC-IV Retrieval augmented generation
and MIMIC-IV ED datasets from Beth Israel Deaconess Medi To implement RAG, we selected likely relevant examples that 
cal Center (BIDMC)26,27 to predict the likelihood of transfer would inform LLM inference on the datapoint under consid
to the intensive care unit (ICU) within 24 hours after triage in eration. To select instances that are likely to serve as useful 
the emergency department (ED). This work is structured as fol in-context examples, we partitioned the dataset D into dis
lows: “Materials and Methods” describes the datasets, LLMs, joint subsets D1 and D2. We opted for this partitioning 
traditional ML implementation, and experimental methodolo scheme to create training and test sets from the entire 1500 
gies for evaluating the performance and calibration, robustness LLM evaluation set and to minimize the possibility of data 
to reduction in detail of a patient’s demographic information, leakage in our RAG implementation. To determine the num
and algorithmic fairness. Then, the “Results” and ber of clusters, we measured the inertia (ie, the sum of 
“Discussion” sections describe the results and our discussion squared distances of samples to their closest cluster center)31

and their broader implications, respectively. for each value of k, starting at 2 and continuing until the 
change in inertia was less than 0.001. We selected the value 
of k based on the Kneedle algorithm, which identified the 

Materials and methods point where inertia shows diminishing returns.32 This defined 
This study was approved by VUMC’s Institutional Review clusters C1; C2; . . . ; Ck for D2. We performed k-means 
Board (IRB# 191892). clustering to help ensure similar patients are selected as RAG 

Downloaded from https://academic.oup.com/jamia/advance-article/doi/10.1093/jamia/ocaf038/8064348 by guest on 11 March 2025



Journal of the American Medical Informatics Association, 2025, Vol. 00, No. 0                                                                                                3           

examples for both D1 and D2. For each x 2D1, we selected calibrated classifier should produce a calibration curve of 
cluster Ci that is closest to x by Euclidean distance. We per y ¼ x. This would indicate that, for all of the predictions 
formed a sensitivity analysis (Figure S3) to determine the assigned a predicted probability P, a fraction p of these pre
number of few-shot examples to use in our experiments. Our dictions corresponds to the positive class. The Brier Score 
sensitivity analysis indicated that there was no noticeable corresponds to the squared loss of predicted probabilities to 
advantage for selecting more than 5 in-context examples. output labels with a range of [0,1], where a lower value indi
Thus, we selected up to 5 data points in Ci and their corre cates a better-calibrated classifier—with 0 indicating perfect 
sponding labels as few-shot examples. If Ci had less than 5 calibration and 1 indicating the worst possible calibration. 
examples, then we randomly selected additional data points The calibration curves were constructed by vertically averag
in D2 to ensure that there were 5 in-context examples. Other ing33 calibration curves of the 30 bootstrap samples. The 
wise, we selected the 5 points in Ci with the closest Euclidean average Brier Score was calculated with the bootstrap sam
distance to x (eg, 5-shot examples). We repeated this proce ples, using the same technique employed with ROC curves.
dure to select few-shot examples for each x 2D2 from D1: We performed Welch’s t-test to determine if there were 
We denote the use of in-context examples as GPT-X RAG statistically significant differences in both performance and 
Closest Within Cluster (or GPT-X RAG CWC). calibration. Consider model1 and model2. The null hypothe

sis was H0 : μmodel ¼ μmodel2. For AUROC, H1 : μ
1 model1 

Traditional ML >μmodel , whereas for Brier Score, H1 : μ
2 model <μ

1 model . 
2

We used a traditional ML benchmark of a gradient-boosting Thus, these hypothesis tests determined if model1 performs 
tree (GBT) implemented with Catboost.29 Categorical data better than model2 for the appropriate metric.
were replaced with an integer corresponding to the index 
when sorting the possible values alphanumerically. We used Design of privacy-utility tradeoff experiments
default settings for the GBT and performed 10-fold cross- To evaluate the privacy-utility tradeoff associated with 
validation to collect the predictions for each data point per LLMs, we considered the following patient data obfuscation 
test set (ie, test-set predictions for each data point in dataset). procedure. Data were organized along 3 levels of detail as 

documented in Figure S3. Level 0 indicates no data obfusca
Statistical analysis tion (ie, the original data); Level 1 indicates a mild amount of 
Unless otherwise noted, we produced a total of 30 boot obfuscation, where each feature was divided into 4-8 catego
strapped samples of the predictions and report performance ries; and Level 2 indicates moderate obfuscation where each 
metrics as average and 95% confidence intervals. When feature was in a binary category (eg, for race, white/not 
applicable, we used Welch’s t-test and 1-way analysis of var white). Level 3 indicates all demographic data were sup
iance (ANOVA) test and considered P< .05 as significant for pressed (ie, removed entirely). Real-valued features were par
all statistical tests. For receiver operating characteristic titioned into ranges in Levels 1-3, while categorical features 
(ROC) curves and calibration curves, we performed vertical at Levels 1-3 were grouped into semantically similar catego
averaging to aggregate results from the bootstrap samples.33 ries. Sex was suppressed for Levels 1-3. To determine 
To perform vertical averaging of the graphs, we defined whether there was a statistically significant difference in LLM 
a comprehensive x-axis and averaged the corresponding and ML performance between these levels, we performed a 
y-values (interpolating y values if necessary). All analyses 1-way ANOVA test with a P-value threshold of .05.
were performed using Python version 3.11.5, and the 
ANOVA test was calculated using SciPy library 1.11.4. Design of algorithmic fairness experiments

To assess the fairness of ML and LLMs, we considered sub
Design of performance and calibration experiments groups (majority/minority) based on race (white/not white), 
To measure prediction performance, we used the area under age (18-49 years old/50 years or older), and sex (male/ 
the receiver operating characteristic (AUROC) curve. We per female). We measured algorithmic fairness in 2 ways: (1) 
formed vertical averaging33 across the 30 bootstrap samples average absolute odds difference (AAOD) and (2) statistical 
to construct the ROC curves. We compared the average parity difference (SPD). AAOD is a measure based on the 
AUROC using the bootstrapped samples (not the average equalized odds (EO) measure of algorithmic fairness.36 EO 
AUROC from the vertically averaged curves since vertical defines a fair classifier as one for which TPRsmaj ¼ TPRsmin 

averaging of curves interpolation of y values is required to and FPRsmaj ¼ FPRsmin for each possible pair of distinct dem
maintain a consistent x axis). ographic subgroups smaj (majority) and smin (minority). 

Currently, accessing the LLM architecture or training data Then, we can calculate AAOD as follows: AAOD¼ 1

to assess model reliability or interpretability is not possible. � � � 2 
�FPRsmaj – FPR sminj þ

1 �
2 TPRs

Therefore, evaluating the reliability and applicability of pre maj – TPRs �
min : Thus, a per

fectly fair classifier will have an AAOD of 0.
dictions is crucial to ensuring interpretability and trustwor SPD measures the difference in the rate that each sensitive 
thiness. As closed-source LLMs such as GPT-3.5 and GPT-4 
are black box classifiers, their primary point of interaction is group receives a positive prediction, denoted as SPD¼
via prompt-based querying and the generated output. In our PðYb ¼ 1 j A ¼ smajÞ   PðYb ¼ 1 j A ¼ s 3

minÞ:
7 An 

case, the generated output was the probability of a specific SPD of 0 corresponds to a perfectly fair classifier. A negative 
phenomenon (eg, likelihood of discharge, likelihood of ICU SPD indicates a preference for the minority class, whereas a 
admittance). positive SPD favors the majority class. Since SPD can range 

In light of this, we used calibration curves34 and Brier from −1 to 1, in addition to calculating the magnitude of stat
Score35 to determine how well-calibrated output probabilities istical parity, we also calculated the absolute value of SPD 
are from each model. Calibration curves plot the fraction of (jSPDj). For Welch’s t-test, we then have H0 : μmodel ¼ μ

1 model2 
positive predictions given a predicted probability. A perfectly and H1 : μmodel <μ

1 model . Since AAOD and jSPDj depict the 
2

Downloaded from https://academic.oup.com/jamia/advance-article/doi/10.1093/jamia/ocaf038/8064348 by guest on 11 March 2025



4                                                                                                J o u r n al of the American Medical Informatics Association, 2025, Vol. 00, No. 0 

magnitude of unfairness, smaller metric values indicate suppression, while GPT-3.5 and GPT-4 displayed varying 
higher fairness. We report the sum of the fairness metrics per degrees of performance but no overall directional trend. 
demographic subgroup. Next, we considered how LLMs compare to traditional ML 

as we reduced the granularity (generalize) and removed (sup
press) demographic information. By visual inspection, tradi

Results tional ML was relatively more robust to generalization and 
Performance and calibration suppression than LLMs, and LLMs varied more in perform
Table 1 summarizes the predictive performance of the LLMs ance. There was no trend that was consistent across all evalu
and traditional ML model. As shown in Figure 1, the ROC ations. Generally, when we observed differences, less 
curves for traditional ML were much larger than those for generalization appeared to lead to slightly better performance 
the LLMs, both with and without in-context learning. More than full suppression. When demographic information was 
over, the P values in Figure 2 indicated that this difference in removed, LLMs (and particularly LLMs with in-context 
performance between traditional ML and LLMs was statisti learning) dropped in performance. This raises the concern 
cally significant. Thus, in terms of measures of discrimina that LLMs may have some level of reliance on demographic 
tion, traditional ML appeared to be more capable of information when performing zero-shot predictions.
identifying different classes of patients than LLMs at the 
given clinical tasks. This was not surprising because tradi Algorithmic fairness
tional ML learns a classification function based on a subset Figures 5 and 6 plot model overall performance and fairness 
of representative data, and it has defined knowledge of on an XY-plane. It was observed that traditional ML was not 
expected feature distributions. In-context examples improved unambiguously the fairest model. For the VUMC data, GPT- 
the ROC of GPT for all dataset-model combinations except 4 with in-context examples was the fairest model across both 
for GPT-3.5 on VUMC data. Nonetheless, traditional ML fairness metrics, while in-context examples did not improve 
still outperformed GPT with in-context examples. GPT-3.5 fairness. For the MIMIC dataset, GPT-4 was the 

Figure 3 depicts the calibration curves for traditional ML, fairest model, but in-context examples improved the fairness 
GPT-3.5, and GPT-4. The classification curve for traditional of GPT-3.5.
ML nearly perfectly overlaid the y ¼ x curve. The calibra We further evaluated the statistical significance of differen
tion curves for GPT-3.5 and GPT-4, however, were heavily ces in fairness metrics between different models by subgroup. 
miscalibrated. These findings were corroborated by the Brier Figure S4 provides heatmaps of P values from the corre
Score, which can be interpreted as a calibration loss, such sponding Welch’s t-tests determining the statistical signifi
that lower Brier scores imply better calibrated classifiers. Tra cance of the results. There are 12 possible scenarios where 
ditional ML was better calibrated than GPT-3.5 or GPT-4, a one model could be statistically significantly fairer than 
result that was statistically significant, as shown in Figure 2. another (based on demographic variable, fairness metric, and 
In-context examples improved calibration for GPT-4 on both dataset). For all 12 cases, GPT-4 was statistically significantly 
datasets, but GPT-3.5 exhibited a decrease in probability cali fairer than traditional ML; however, incorporating in- 
bration for both datasets. context examples reduced this number to 10 of 12 cases. For 

GPT-3.5, zero-shot learning was statistically significantly 
Privacy-utility tradeoff fairer than traditional ML for only 6 of 12 cases. In the 
Table 2 presents the mean performance (with 95% confi VUMC dataset, GPT-3.5 struggled with maintaining fairness 
dence intervals in parentheses) of each level of generalization for race, but in the MIMIC dataset, GPT-3.5 was only fairer 
per model. There was less than a 0.01 difference among the for subgroups defined by sex. In-context learning did not 
standard deviations of performance among different levels of help the fairness of the VUMC data; however, in-context 
generalization/suppression per model. The ANOVA analysis examples improved GPT-3.5’s fairness for the race and age 
was statistically significant across all combinations of data variables in the mimic dataset. When comparing GPT-3.5 
sets and models (Table 3), indicating all models were and GPT-4, we note that there is no unambiguously fairer 
affected, to some degree, by the generalization and suppres model. Without in-context examples, GPT-4 surpassed GPT- 
sion of demographic information. 3.5’s fairness for all demographics in the MIMIC dataset but 

Figure 4 displays the privacy-utility tradeoff across 4 levels none in the VUMC dataset. With in-context examples, GPT- 
of demographic generalization and suppression. We observed 4 was fairer on the VUMC dataset, yet GPT-3.5 still sur
that traditional ML performance was generally consistent passed GPT-4’s fairness on the MIMIC dataset. We note that 
across the levels of demographic generalization and this fine-grained analysis may differ somewhat from the 

Table 1. Average AUROC and Brier Scores and 95% confidence intervals.

VUMC discharge MIMIC-IV ED

AUROC " Brier Score # AUROC " Brier Score #

GPT-3.5 0.537 (0.532, 0.543) 0.384 (0.38, 0.388) 0.517 (0.513, 0.521) 0.06 (0.057, 0.062)
GPT-4 0.629 (0.625, 0.634) 0.251 (0.249, 0.253) 0.602 (0.592, 0.612) 0.219 (0.216, 0.222)
GPT-3.5 RAG CWC 0.512 (0.509, 0.515) 0.477 (0.47, 0.484) 0.608 (0.596, 0.619) 0.078 (0.076, 0.081)
GPT-4 RAG CWC 0.638 (0.632, 0.644) 0.246 (0.244, 0.248) 0.61 (0.598, 0.621) 0.152 (0.15, 0.153)
Traditional ML 0.847 (0.845, 0.848) 0.134 (0.133, 0.134) 0.894 (0.894, 0.895) 0.042 (0.042, 0.042)

Arrow indicates a better direction. Best in bold (" ¼ higher is better; # ¼ lower is better).
Abbreviations: AUROC: area under the receiver operating characteristic; ML: machine learning; VUMC: Vanderbilt University Medical Center.

Downloaded from https://academic.oup.com/jamia/advance-article/doi/10.1093/jamia/ocaf038/8064348 by guest on 11 March 2025



Journal of the American Medical Informatics Association, 2025, Vol. 00, No. 0                                                                                                5           

Figure 1. Receiver operating characteristic curves for (A) zero-shot prompting on the Vanderbilt University Medical Center (VUMC) dataset, (B) retrieval 
augmented generation (RAG)-based few-shot prompting on the VUMC dataset, (C) zero-shot prompting on the MIMIC-IV dataset, and (D) RAG-based 
few-show prompting on the MIMIC-IV dataset. Note that the AUC given in the legends may not match those given in Table 1 due to numerical 
interpolation of the curves required for vertical curve averaging (AUC is of the final averaged curve).

overall trends presented in Figures 5 and 6 since these figures unfair model, which was validated by our findings. The use 
consider aggregate fairness across all demographic subgroups of in-context examples also impacted fairness; however, this 
considered. As a result, the small yet significant shifts may be impact was not unanimously positive or negative but 
canceled out in the aggregate. depended upon dataset and metric. Moreover, despite being 

While GPT-4 was the fairest model for both datasets, the the fairer models, GPT-3.5 and GPT-4 were also the least 
fairer model between GPT-3.5 and traditional ML depended capable predictors. Thus, it seems that overall improved fair
upon the dataset and fairness metric considered. Traditional ness comes at the cost of reduced subgroup performance, but 
ML was trained and evaluated on data from the same loca future work is necessary to confirm.
tion. Thus, whatever biases are present in the data source will 
be present in the resulting model. We evaluated GPT-3.5 and 
GPT-4 using zero-shot prompting and without knowledge of Discussion
the evaluation datasets. Thus, these models were not exposed This investigation suggests that LLMs are not yet ready to 
to the local dataset biases that may influence decisions. This serve as predictive, analytic models, although GPT-4 does 
led us to hypothesize that traditional ML would be the most surpass GPT-3.5 in most of our experiments, indicating that 

Downloaded from https://academic.oup.com/jamia/advance-article/doi/10.1093/jamia/ocaf038/8064348 by guest on 11 March 2025



6                                                                                                J o u r n al of the American Medical Informatics Association, 2025, Vol. 00, No. 0 

calibrated when compared to the traditional ML comparison. 
The weak calibration of the LLM predictions in clinical sce
narios calls into question their utility and reliability as a clini
cal classifier. This is not to say LLMs do not have advantages 
as a classifier, as there is little model tuning required out-of- 
the-box to be minimally functional (whereas traditional ML 
requires training data and computation time), and the con
versational interaction may allow for chain-of-thought rea
soning to support usability and interpretability.38 Although 
further fine-tuning would likely be beneficial, our analysis 
assumes a resource-constrained environment where fine- 
tuning may not be feasible with respect to computational, 
data, and/or financial resources. These advantages, however, 
are difficult to realize when the output probabilities do not 
indicate reliability. Unlike several traditional ML algo
rithms,39,40 LLMs have limited capability to quantify their 
uncertainty post hoc.41 Thus, if LLMs are going to be useful 
as accurate clinical predictors, further research into improv
ing the reliability and interpretability of LLMs is a must.

For LLMs to be useful as classifiers in lower resource set
tings, for example, where extensive data may not be available 
to train models, strategies such as in-context learning and 
RAG are necessary to produce good performance. We 
expected the incorporation of intelligently selected in-context 
examples16,42 would improve LLM performance to levels 
near that of traditional ML. Our results suggest RAG does 
not help; however, we used what we consider a straightfor
ward approach to RAG. There is emerging evidence that 
RAG-based examples are not always effective.16,43 It is a rea
sonable conjecture that poor examples provided to an LLM 
are likely to result in a degradation in performance. There 
might be other approaches that would result in higher gains 
in performance; however, selection of an optimal RAG strat
egy is outside the scope of this work. Table 1 reveals that for 
the VUMC data, the usage of in-context examples resulted in 
either a slight increase in performance (GPT-4) or a decrease 
in performance (GPT-3.5). Further research is needed to 
improve the selection of RAG-based in-context examples for 
biomedical classification.

In the event that LLMs are the most accessible or applica
ble model for a situation, there are still concerns with respect 
to patient privacy when using these models. As we alluded to, 
organizations may apply some form of de-identification 

Figure 2. Let model1 be the model given by the row and model2 be the 
model given by the column. Then, H0 : μmodel ¼ μmodel . For area under before sending data to the LLM. In this work, we evaluated 

1 2
the receiver operating characteristic (AUROC) H1 : μ the generalization of demographic PHI as well as suppression 

model >μmodel . For 
1 2

Brier Score, H1 : μmodel <μ
1 model Thus, these hypothesis tests determine (denoted as Level 3 generalization/suppression in the results). 

2 
if model1 performs better than model2 for the appropriate metric. (A) We did not use a randomization strategy in order to maintain 
AUROC from zero-shot prompting on Vanderbilt University Medical truthful privacy in line with the assumption that healthcare 
Center (VUMC) dataset, (B) AUROC from zero-shot prompting on MIMIC- 
IV dataset, (C) AUROC from retrieval augmented generation (RAG)-based organizations do not want to falsify information about 
few-shot prompting on VUMC dataset, (D) AUROC from RAG-based few- patients for predictive inference.44–46 Our analysis indicates 
shot prompting on MIMIC-IV dataset, (E) Brier Score from zero-shot that LLMs are much more sensitive to the level of detail in 
prompting on VUMC dataset, (F) Brier Score from zero-shot prompting on demographic information compared to traditional ML. This 
MIMIC-IV dataset, (G) Brier Score from RAG-based few-shot prompting 
on VUMC dataset, (H) Brier Score from RAG-based few-shot prompting suggests that a strategy that generalizes patient information 
on MIMIC-IV dataset. may result in a reduction in predictive performance.

The apparent sensitivity of LLMs to the completeness of 
patient demographic information raises questions about the 

GPT is improving with new releases. In our experiments, biases and unfairness present in these models based on their 
LLMs have a significantly lower AUROC compared to tradi existing training. We find that GPT-4 is the fairest model 
tional ML. This implies that LLMs simply do not match the evaluated; however, we note that LLMs are generally the 
discriminative capabilities of traditional ML for these tasks. lowest-performing models evaluated. By definition, an unfair 
These results are in line with a similar analysis recently per model is one that results in a disparate outcome for at least 
formed by Chen et al.22 Moreover, inspecting the calibration one subgroup.47 Typically, mitigating fairness concerns usu
curves and Brier Scores reveals that LLMs are poorly ally means improving the performance of the disadvantaged 

Downloaded from https://academic.oup.com/jamia/advance-article/doi/10.1093/jamia/ocaf038/8064348 by guest on 11 March 2025



Journal of the American Medical Informatics Association, 2025, Vol. 00, No. 0                                                                                                7           

Figure 3. Calibration plots (A) zero-shot prompting on the Vanderbilt University Medical Center (VUMC) dataset, (B) retrieval augmented generation 
(RAG)-based few-shot prompting on the VUMC dataset, (C) zero-shot prompting on the MIMIC-IV dataset, and (D) RAG-based few-show prompting on 
the MIMIC-IV dataset.

subgroup(s). This route ensures equity of performance with subgroups in the MIMIC dataset; however, this does not 
reduced harm.48 For the LLMs, increased fairness seems to hold for the VUMC dataset or race in the MIMIC dataset. 
come at reduced performance for all subgroups. This is evi Liu et al also found that fine-tuning using few-shot examples 
denced by the overall degradation of performance of LLMs improves the fairness gap for GPT-3.5, but there is little dis
compared to traditional ML. Thus, it may be difficult to jus cussion on the performance impact. Our analysis indicates 
tify the use of LLMs on the basis of apparent fairness in the that few-shot examples can improve fairness of GPT-3.5 and 
context of subpar performance. GPT-4, but whether or not this occurs is dependent on model 

Moreover, we find that there is not a consistently fair and dataset.
model. Fairness is conditioned on dataset and prediction Though we conducted a large number of experiments, we 
task. For example, work from Liu et al20 also compared the acknowledge several limitations of this investigation. First, 
fairness of GPT-3.5 to traditional ML. In their analysis, tradi other facets of evaluation beyond the scope of this work, 
tional ML was fairer in their analysis when compared to such as interpretability, were not evaluated and could also 
GPT-3.5 in 2 of the 3 evaluated datasets. In our evaluation, differ between model types. Second, we did not consider the 
traditional ML is fairer than GPT-3.5 for age and gender costs of implementing and maintaining these models and the 

Downloaded from https://academic.oup.com/jamia/advance-article/doi/10.1093/jamia/ocaf038/8064348 by guest on 11 March 2025



8                                                                                                J o u r n al of the American Medical Informatics Association, 2025, Vol. 00, No. 0 

Table 2. Average AUROC and 95% confidence intervals for each model and level of data obfuscation.

VUMC MIMIC-IV ED

GPT-3.5 Level 0 0.537 (0.532, 0.543) 0.517 (0.513, 0.521)
Level 1 0.573 (0.568, 0.578) 0.526 (0.522, 0.53)
Level 2 0.575 (0.57, 0.579) 0.515 (0.511, 0.518)
Level 3 0.557 (0.553, 0.561) 0.514 (0.514, 0.517)

GPT-4 Level 0 0.629 (0.625, 0.634) 0.602 (0.592, 0.612)
Level 1 0.657 (0.652, 0.662) 0.633 (0.623, 0.644)
Level 2 0.64 (0.636, 0.644) 0.609 (0.599, 0.619)
Level 3 0.649 (0.644, 0.655) 0.601 (0.59, 0.611)

GPT-3.5 RAG CWC Level 0 0.512 (0.509, 0.515) 0.608 (0.596, 0.619)
Level 1 0.557 (0.551, 0.562) 0.631 (0.621, 0.642)
Level 2 0.543 (0.54, 0.546) 0.605 (0.594, 0.615)
Level 3 0.522 (0.516, 0.527) 0.564 (0.553, 0.575)

GPT-4 RAG CWC Level 0 0.638 (0.632, 0.644) 0.61 (0.598, 0.621)
Level 1 0.61 (0.605, 0.615) 0.617 (0.602, 0.631)
Level 2 0.603 (0.598, 0.609) 0.62 (0.611, 0.629)
Level 3 0.605 (0.599, 0.611) 0.53 (0.522, 0.538)

Traditional ML Level 0 0.847 (0.845, 0.848) 0.894 (0.894, 0.895)
Level 1 0.844 (0.843, 0.845) 0.894 (0.894, 0.894)
Level 2 0.845 (0.844, 0.846) 0.892 (0.891, 0.892)
Level 3 0.846 (0.844, 0.847) 0.894 (0.894, 0.895)

Abbreviations: AUROC: area under the receiver operating characteristic; ML: machine learning; VUMC: Vanderbilt University Medical Center.

Table 3. Results of 1-way ANOVA analysis to compare the effect of data generalization/suppression on LLM AUROC.

GPT-3.5 GPT-3.5 RAG GPT-4 GPT-4 RAG Traditional ML

Dataset F P F P F P F P F P

VUMC 48.341 2.42E−20 101.859 2.31E−32 45.743 1.39E−19 40.065 7.63E−18 17.441 2.92E−10
MIMIC 10.394 4.13E−06 50.665 5.29E−21 11.696 9.43E−07 96.963 1.80E−31 92.853 1.03E−39

Abbreviations: ANOVA: analysis of variance; AUROC: area under the receiver operating characteristic; LLM: large language model; ML: machine learning; 
VUMC: Vanderbilt University Medical Center.

Figure 4. Bar charts depicting the privacy-utility tradeoff for (A) zero-shot prompting and (B) retrieval augmented generation (RAG)-based few-shot 
prompting.

associated environmental factors. Operational costs of AI are crucial for generalizability of these findings. Finally, we 
may prohibit lower-resourced medical centers from utilizing note that the privacy-utility tradeoff reported does not match 
these advances, and the energy required may have a down the tradeoff expected. Ultimately, this calls into question the 
stream negative impact both economically and environmen reliability of the datasets used for this privacy-utility tradeoff 
tally. Third, we only consider 2 clinical tasks from datasets analysis. We cannot rule out the possibility that information 
derived from 2 medical centers. Additional studies that con captured in other predictors in these datasets are serving as 
sider a wider variety of tasks across multiple medical centers appropriate proxies to demographic information.

Downloaded from https://academic.oup.com/jamia/advance-article/doi/10.1093/jamia/ocaf038/8064348 by guest on 11 March 2025



Journal of the American Medical Informatics Association, 2025, Vol. 00, No. 0                                                                                                9           

Figure 5. Two-dimensional fairness plots for the Vanderbilt University Medical Center (VUMC) dataset using (A) average absolute odds difference 
(AAOD), (B) statistical parity difference (SPD), or (C) absolute value of SPD as the fairness metric, respectively.

Downloaded from https://academic.oup.com/jamia/advance-article/doi/10.1093/jamia/ocaf038/8064348 by guest on 11 March 2025



10                                                                                              J o u r n al of the American Medical Informatics Association, 2025, Vol. 00, No. 0 

Figure 6. Two-dimensional fairness plots for the MIMIC-IV dataset using (A) average absolute odds difference (AAOD), (B) statistical parity difference 
(SPD), or (C) absolute value of SPD as the fairness metric, respectively.

Downloaded from https://academic.oup.com/jamia/advance-article/doi/10.1093/jamia/ocaf038/8064348 by guest on 11 March 2025



Journal of the American Medical Informatics Association, 2025, Vol. 00, No. 0                                                                                              1  1        

Conclusion are available from the corresponding authors upon reason
This study reported on a multifaceted comparison of LLMs able request.
to traditional ML in terms of model performance, calibra
tion, privacy, and fairness as the points of evaluation. The References
evaluation of LLMs for clinical prediction tasks is a growing 
area of research22 and as such, these benchmarks and analy 01. Manrai AK. Physicians, probabilities, and populations—estimat
ses are still developing. We focused on 2 clinical prediction ing the likelihood of disease for common clinical scenarios. JAMA 

tasks: likelihood of ICU admission within 24 hours of ED Intern Med. 2021;181:756-757.
02. Mason SL, Daws RE, Soreq E, et al. Predicting clinical diagnosis in 

arrival and likelihood of patient discharge from in-patient Huntington’s disease: an imaging polymarker. Ann Neurol. 
hospitalization within 24 hours. Even when supplemented 2018;83:532-543.
with in-context learning, we find that LLMs are not as effec 03. Blinov P, Avetisian M, Kokh V, Umerenkov D, Tuzhilin A. Predict
tive as traditional ML for clinical prediction tasks due to their ing clinical diagnosis from patients electronic health records using 
poor discriminative performance and lack of reliability, par BERT-based neural networks. In: Michalowski M, Moskovitch R, 
ticularly when demographic factors are variables in the pre eds. Artificial Intelligence in Medicine. Springer International Pub
diction model. Our analysis was limited to 2 clinical lishing; 2020:111-121.
prediction tasks, possibly limiting the generalizability of our 04. Lewin-Epstein O, Baruch S, Hadany L, Stein GY, Obolski U. Pre

claims. While LLMs are the fairest technologies, they are also dicting antibiotic resistance in hospitalized patients by applying 
machine learning to electronic medical records. Clin Infect Dis. 

those with poor model performance. This indicates that per 2021;72:e848-e855.
formance across subgroups degrades to ensure fairness, but 05. Keith A, Jenkins TC, O’Leary S, et al. Reducing length of antibiot
this needs to be confirmed. ics for children with ear infections: protocol for a cluster- 

Still, we note that LLMs have potential. Since March 2023, randomized trial in the USA. J Comp Eff Res. 2023;12:e230088.
LLMs have been used to aid with drafting patient messages,12 06. Zhang X, Yan C, Malin BA, Patel MB, Chen Y. Predicting next- 
optimizing clinical decision support,13 developing phenotyp day discharge via electronic health record access logs. J Am Med 
ing algorithms,14 and summarizing patient encounters.15 To Inform Assoc. 2021;28:2670-2680.
reach this goal, research is needed to optimize in-context 07. Weiss K, Khoshgoftaar TM, Wang D. A survey of transfer learn

learning for LLM performance, understand the effect of ing. J Big Data. 2016;3:9.
08. Davis SE, Walsh CG, Matheny ME. Open questions and research 

randomization-based privacy preservation strategies, and gaps for monitoring and updating AI-enabled tools in clinical set
understand the internal biases of LLMs to mitigate fairness tings. Front Digit Health. 2022;4:958284.
concerns. 09. Floridi L, Chiriatti M. GPT-3: its nature, scope, limits, and conse

quences. Minds Machines. 2020;30:681-694.
10. Achiam J, Adler S, Agarwal S, et al.; OpenAI. GPT-4 technical 

Author contributions report, arXiv, http://arxiv.org/abs/2303.08774, 2023, preprint: 
Katherine E. Brown (Conceptualization, Formal analysis, not peer reviewed.
Investigation), Chao Yan (Conceptualization), Zhuohang Li 11. Meet Claude. Accessed October 22, 2024. https://www.anthropic. 

(Writing), Xinmeng Zhang (Data curation), Benjamin X. com/claude
12. Liu S, McCoy AB, Wright AP, et al. Leveraging large language 

Collins (Writing), You Chen (Data curation), Ellen Wright models for generating responses to patient messages, medRxiv, 
Clayton (Writing), Murat Kantarcioglu (Conceptualization), http://medrxiv.org/lookup/doi/10.1101/2023.07.14.23292669, 
Yevgeniy Vorobeychik (Conceptualization), and Bradley A. November 27, 2023, preprint: not peer reviewed.
Malin (Conceptualization, Resources, Supervision) 13. Liu S, Wright AP, Patterson BL, et al. Using AI-generated sugges

tions from ChatGPT to optimize clinical decision support. J Am 
Med Inform Assoc. 2023;30:1237-1245.

Supplementary material 14. Yan C, Ong HH, Grabowska ME, et al. Large language models 
Supplementary material is available at Journal of the Ameri facilitate the generation of electronic health record phenotyping 
can Medical Informatics Association online. algorithms. J Am Med Inform Assoc. 2024;31:1994-2001.

15. Genes N, Simon G, Koziatek C, et al. Generative AI summaries to 
facilitate emergency department handoff. Ann Emerg Med. 

Funding 2024;84:S3.
16. Glicksberg BS, Timsina P, Patel D, et al. Evaluating the accuracy of 

This research was sponsored, in part, by National Institutes a state-of-the-art large language model for prediction of admis
of Health [grant numbers U54HG012510 and sions from the emergency room. J Am Med Inform Assoc. 
T15LM007450] and National Science Foundation [grant 2024;31:1921-1928.
number IIS-1905558]. 17. Sandmann S, Riepenhausen S, Plagwitz L, Varghese J. Systematic 

analysis of ChatGPT, Google search and Llama 2 for clinical deci
sion support tasks. Nat Commun. 2024;15:2050.

Conflicts of interest 18. Zhang J, Sun K, Jagadeesh A, et al. The potential and pitfalls of 
The authors have no conflicts of interest to disclose. using a large language model such as ChatGPT, GPT-4, or LLaMA 

as a clinical assistant. J Am Med Inform Assoc. 
2024;31:1884-1891.

Data availability 19. Acharya A, Shrestha S, Chen A, et al. Clinical risk prediction using 
language models: benefits and considerations. J Am Med Inform 

The MIMIC-IV dataset underlying this article is available in Assoc. 2024;31:1856-1864.
Physionet at https://doi.org/10.13026/5ntk-km72. The 20. Liu Y, Gautam S, Ma J, Lakkaraju H. Confronting LLMs with tra
VUMC data underlying this article cannot be shared publicly ditional ML: rethinking the fairness of large language models in 
to preserve the privacy of individuals in the study. The data tabular classifications. In: Duh K, Gomez H, Bethard S, eds. 

Downloaded from https://academic.oup.com/jamia/advance-article/doi/10.1093/jamia/ocaf038/8064348 by guest on 11 March 2025



12                                                                                              J o u r n al of the American Medical Informatics Association, 2025, Vol. 00, No. 0 

Proceedings of the 2024 Conference of the North American Chap 35. Murphy AH. A new vector partition of the probability score. J 
ter of the Association for Computational Linguistics: Human Lan Appl Meteor. 1973;12:595-600.
guage Technologies. Volume 1: Long Papers. Association for 36. Hardt M, Price E, Srebro N. Equality of opportunity in supervised 
Computational Linguistics; 2024:3603-3620. https://aclanthol learning. In: Advances in Neural Information Processing Systems. 
ogy.org/2024.naacl-long.198 Vol. 29. Curran Associates, Inc.; 2016.

21. Andreadis K, Newman DR, Twan C, Shunk A, Mann DM, Stevens 37. Besse P, del Barrio E, Gordaliza P, Loubes JM, Risser L. A survey 
ER. Mixed methods assessment of the influence of demographics of bias in machine learning through the prism of statistical parity. 
on medical advice of ChatGPT. J Am Med Inform Assoc. Am Stat. 2022;76:188-198.
2024;31:2002-2009. 38. Gramopadhye O, Nachane SS, Chanda P, et al. Few shot chain-of- 

22. Chen C, Yu J, Chen S, et al. ClinicalBench: can LLMs beat tradi thought driven reasoning to prompt LLMs for open ended medical 
tional ML models in clinical prediction? arXiv, http://arxiv.org/ question answering. arXiv, http://arxiv.org/abs/2403.04890, 
abs/2411.06469, December 12, 2024, preprint: not peer reviewed. August 20, 2024, preprint: not peer reviewed.

23. Databricks. State of Data þ AI. Accessed October 23, 2024. 39. Malinin A, Prokhorenkova L, Ustimenko A. Uncertainty in gra
https://www.databricks.com/discover/state-of-data-ai dient boosting via ensembles. 2020. Accessed November 8, 2024. 

24. Choudhury A. Factors influencing clinicians’ willingness to use an https://openreview.net/forum? id=1Jv6b0Zq3qi
AI-based clinical decision support system. Front Digit Health. 40. Gal Y, Ghahramani Z. Dropout as a Bayesian approximation: rep
2022;4:920662. resenting model uncertainty in deep learning. In: Proceedings of 

25. Brickell J, Shmatikov V. The cost of privacy: destruction of data- the 33rd International Conference on Machine Learning. PMLR; 
mining utility in anonymized data publishing. In: Proceedings of 2016:1050-1059.
the 14th ACM SIGKDD International Conference on Knowledge 41. Zhang J, Li Z, Das K, Malin B, Kumar S. SAC3: reliable hallucina
Discovery and Data Mining. ACM; 2008:70-78. https://dl.acm. tion detection in black-box language models via semantic-aware 
org/doi/10.1145/1401890.1401904 cross-check consistency. In: Bouamor H, Pino J, Bali K, eds. 

26. Johnson A, Bulgarelli L, Pollard T, Horng S, Celi LA, Mark R. Findings of the Association for Computational Linguistics: 
MIMIC-IV-ED (version 2.2). PhysioNet 2023 [cited 2024 Nov 1]. EMNLP 2023. Association for Computational Linguistics; 
https://doi.org/10.13026/5ntk-km72 2023:15445-15458. https://aclanthology.org/2023.findings-emnlp. 

27. Johnson AEW, Bulgarelli L, Shen L, et al. MIMIC-IV, a freely 1032
accessible electronic health record dataset. Sci Data. 2023;10:219. 42. Hegselmann S, Buendia A, Lang H, Agrawal M, Jiang X, Sontag 

28. Goldberger AL, Amaral LA, Glass L, et al. PhysioBank, Physio D. TabLLM: few-shot classification of tabular data with large 
Toolkit, and PhysioNet: components of a new research resource language models. In: Proceedings of the 26th International 
for complex physiologic signals. Circulation. 2000;101: Conference on Artificial Intelligence and Statistics. PMLR; 
e215-e220. 2023:5549-5581. https://proceedings.mlr.press/v206/hegsel

29. Dorogush AV, Ershov V, Gulin A. CatBoost: gradient boosting mann23a.html
with categorical features support. [cited 2024 Nov 1]. https://cat 43. Balaguer A, Benara V, Cunha Rl de F, et al. RAG vs fine-tuning: 
boost.ai/ pipelines, tradeoffs, and a case study on agriculture. arXiv, http:// 

30. Singh GK. Area deprivation and widening inequalities in US mor arxiv.org/abs/2401.08406, 2024, preprint: not peer reviewed.
tality, 1969–1998. Am J Public Health. 2003;93:1137-1143. 44. El Emam K, Dankar FK, Issa R, et al. A globally optimal k-ano

31. scikit-learn. KMeans. Accessed July 9, 2024. https://scikit-learn/ nymity method for the de-identification of health data. J Am Med 
stable/modules/generated/sklearn.cluster.KMeans.html Inform Assoc. 2009;16:670-682.

32. Satopaa V, Albrecht J, Irwin D, Raghavan B. Finding a “kneedle” 45. Dankar FK, Emam KE. Practicing differential privacy in health 
in a haystack: detecting knee points in system behavior. In: 2011 care: a review. Trans Data Priv. 2013;6:35-36.
31st International Conference on Distributed Computing Systems 46. El Emam K, Dankar FK. Protecting privacy using k-anonymity. J 
Workshops. IEEE; 2011:166-171. Am Med Inform Assoc. 2008;15:627-637.

33. Hogan J, Adams NM. On averaging ROC curves. Trans Mach 47. Ferrara E. Fairness and bias in artificial intelligence: a brief survey 
Learn Res. 2023. of sources, impacts, and mitigation strategies. Sci. 2023;6:3.

34. Wilks DS. On the combination of forecast probabilities for consec 48. Varkey B. Principles of clinical ethics and their application to prac
utive precipitation periods. Weather Forecast. 1990;5:640-650. tice. Med Princ Pract. 2021;30:17-28.

© The Author(s) 2025. Published by Oxford University Press on behalf of the American Medical Informatics Association.

This is an Open Access article distributed under the terms of the Creative Commons Attribution License (https://creativecommons.org/licenses/by/4.0/), which permits 
unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.
Journal of the American Medical Informatics Association, 2025, 00, 1–12
https://doi.org/10.1093/jamia/ocaf038
Research and Applications

Downloaded from https://academic.oup.com/jamia/advance-article/doi/10.1093/jamia/ocaf038/8064348 by guest on 11 March 2025