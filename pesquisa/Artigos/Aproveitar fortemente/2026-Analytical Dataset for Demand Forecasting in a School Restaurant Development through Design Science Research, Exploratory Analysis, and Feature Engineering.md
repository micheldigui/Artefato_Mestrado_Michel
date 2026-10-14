---
source_file: "2026-Analytical Dataset for Demand Forecasting in a School Restaurant Development through Design Science Research, Exploratory Analysis, and Feature Engineering.txt"
original_rel_path: "Trabalhos\Artigos\Aproveitar fortemente\txt\2026-Analytical Dataset for Demand Forecasting in a School Restaurant Development through Design Science Research, Exploratory Analysis, and Feature Engineering.txt"
category: "Artigos_Aproveitar_fortemente"
extension: ".txt"
sha256: "f154891cc3ae360a89786ddac5830d9f8e4f28dab464644cc46de8eaed6aed35"
extracted_at: "2026-09-19T23:16:59.269268"
---

﻿ANALYTICAL DATASET FOR DEMAND FORECASTING IN A SCHOOL RESTAURANT: 

DEVELOPMENT THROUGH DESIGN SCIENCE RESEARCH, EXPLORATORY ANALYSIS, AND 

FEATURE ENGINEERING 

ABSTRACT 

Meal planning in school restaurants depends on demand estimates that are subject to 

operational uncertainties , such as no-shows despite reservations, consumption without prior 

reservation, recording failures, and variations associated with the academic calendar. This 

article presents the development and exploratory evaluation of an analytical dataset to support 

predictive demand models for a school restaurant, based on the Design Science Research 

approach. The data flow was organized into Bronze, Silver, and Gold layers, integrating 

reservations, consumption records, menus, academic calendar, and weather data from 2023 to 

2025. As a result, the Gold layer consolidated 548 records suitable for modeling and 140 

predictive attributes, with an explicit separation between observed consumption, estimated 

consumption, variables used for modeling, and variables eligible for prediction. The 

exploratory analysis revealed weekly patterns, seasonal regimes, menu effects, and the 

centrality of reservations as an explanatory signal of demand. An exploratory semantic 

representation of the menu was also prepared using BERT and PCA, preserving approximately 

95.16% of the variance in 44 components. The artifact contributes to reducing opacity in data 

preparation, mitigating the risk of temporal leakage, and providing a traceable dataset for future 

model comparisons aimed at production planning and food waste reduction. 

Keywords: demand forecasting; school restaurant; food waste; Design Science 

Research; exploratory data analysis. 

1. INTRODUCTION 

Food waste in collective food services is an operational, economic, and socio-

environmental problem. In school restaurants, the daily decision about how many meals to 

produce must balance two risks: preparing less than the effective demand and compromising 

service, or preparing more than demand and increasing losses. This issue becomes more critical 

when planning depends on reservations, manual records, and variations in the academic 

calendar, such as holidays, recesses, and the beginning and end of academic periods. 

Recent literature shows that machine learning models can reduce waste when they 

replace purely intuitive estimates with forecasts based on historical data, calendar information, 

and operational context. Rodrigues et al. (2024), for example, analyzed collective food services 



and demonstrated that demand forecasts can support the reduction of wasted meals when 

incorporated into planning. Similarly, Turker (2025) discusses university dining facilities as 

environments in which calendar, menu, weather, and attendance behavior data can support 

sustainable decisions. 

However, the usefulness of predictive models does not depend only on the chosen 

algorithm. Before comparing families of predictive models, such as statistical time series, tree-

based methods, linear models, neural networks, or hybrid approaches, it is necessary to build a 

traceable and coherent data artifact capable of distinguishing what was observed, what was 

estimated, and what should be used for modeling. Without this separation, the model may learn 

patterns fabricated by inadequate data treatment, producing optimistic metrics and fragile 

decisions. 

This study treats the data flow as the central research artifact, guided by Design Science 

Research (DSR). This choice is consistent with Hevner et al. (2004), Peffers et al. (2007), and 

Gregor and Hevner (2013), because the objective is not only to describe a phenomenon but to 

design, demonstrate, and evaluate an informational solution to a practical problem. The 

proposed artifact transforms heterogeneous datasets into a documented daily analytical dataset 

prepared for future modeling stages. 

The general objective of this article is to develop and conduct an exploratory evaluation 

of a Gold analytical dataset for future meal demand forecasting in a school restaurant. In this 

study, the Bronze, Silver, and Gold layers are understood, respectively, as traceable raw data, 

consolidated and qualified data, and analytical data prepared for modeling. Thus, the Gold 

dataset represents the final artifact of this research stage, while the previous layers constitute 

the processes required for its construction. 

To achieve this general objective, five sequential specific objectives were defined. The 

first consists of structuring the ingestion of reservation, consumption, menu, calendar, and 

weather sources into the Bronze layer, preserving traceability. The second consists of 

consolidating a daily Silver dataset, distinguishing observed, estimated, and non-applicable 

data. The third seeks to conduct an exploratory analysis to evaluate temporal patterns, 

seasonality, variability, and menu effects. The fourth consists of generating Gold datasets with 

temporal, operational, weather, and menu-related attributes. The fifth consists of evaluating the 

feasibility of an exploratory semantic menu block based on BERT and PCA, to be validated in 

future models. 



2. THEORETICAL BACKGROUND 

2.1 Demand forecasting and waste in food services 

Collective food services operate under daily uncertainty. In school and university 

restaurants, demand may vary by day of the week, academic period, days preceding holidays, 

exams, weather conditions, and menu attractiveness. The problem is close to what Malefors 

(2022) describes in the public collective food sector: the quantity prepared in relation to the 

actual number of users served is a central factor in waste generation. 

Rodrigues et al. (2024) reinforce that short-term demand forecasting is a concrete 

strategy to reduce both overproduction and unmet demand. Their study is especially relevant to 

this work because it uses real food service data and compares machine learning models with 

traditional estimation approaches. This supports the decision to prepare a daily, multivariate, 

and traceable database before advancing to predictive models. 

Chaudhari et al. (2025) also highlight the importance of historical data, analytical 

modules, and algorithms such as XGBoost, LightGBM, and SARIMA in forecasting systems 

for food supply chains. Although the context of the present study is a school restaurant, the 

analytical logic is similar: useful forecasting depends on reliable history, consistent explanatory 

variables, and the ability to interpret trends before operational decision-making. 

2.2 Design Science Research and analytical dataset construction 

DSR is appropriate when research seeks to build and evaluate an artifact capable of 

solving an identified problem in a real context. Hevner et al. (2004) present design research as 

a paradigm aimed at creating artifacts that expand human and organizational capabilities. 

Peffers et al. (2007) structure this process into stages such as problem identification, objective 

definition, design and development, demonstration, evaluation, and communication. 

In this article, the artifact is not yet the final predictive model, but the analytical dataset 

and preparation flow that make such a model possible. This distinction is important because, in 

data science projects, result robustness depends on decisions made before training: date 

standardization, removal of duplicate records, treatment of missing values, category encoding, 

creation of temporal lags, and preservation of quality markers. Tripathi et al. (2021) advocate 

more robust data science processes precisely because they recognize that data failures and 

modeling failures are interdependent. 

The adoption of Bronze, Silver, and Gold layers follows this concern. Bronze preserves 

ingested data with minimal transformation, maintaining traceability. Silver consolidates daily 

semantics and separates observations, estimates, and modeling criteria. Gold creates predictive 



attributes already oriented toward use by different families of models. This architecture avoids 

mixing ingestion, cleaning, imputation, and modeling into a single opaque step. 

2.3 Menu, natural language, and feature engineering 

The menu is a relevant contextual variable because users' choices are not determined 

only by calendar and reservation. Kim et al. (2023) explore the use of unstructured data and 

textual representations, such as Word2Vec, to forecast cafeteria customers. This type of 

evidence does not eliminate the need for interpretable categories, but it supports the 

methodological hypothesis that dish descriptions may carry additional signals of food 

preference. 

Transformer-based models expanded the ability to represent text through contextual 

embeddings. Vaswani et al. (2017) introduced the Transformer architecture, and Devlin et al. 

(2019) proposed BERT, a bidirectional model capable of generating dense text representations. 

In this study, BERT is not assumed to be superior to manual categories; it is treated as an 

exploratory alternative to represent semantic similarities that can later be tested against models 

based only on protein, preparation, and style. 

For example, two dishes manually classified under the same protein category may carry 

distinct preference signals, such as "grilled chicken" and "chicken fricassee." Although both 

belong to the poultry group, their textual descriptions indicate different preparation methods, 

dish composition, and sensory characteristics. Embedding representations seek to preserve part 

of these semantic relationships in numerical format, allowing future testing of whether such 

information adds value to traditional categorical attributes. 

The representations generated by BERT assign an extensive numerical vector to each 

menu description. Considering the limited number of modelable records, using all these 

dimensions could increase model complexity and raise the risk of overfitting. 

For this reason, Principal Component Analysis (PCA) was applied, a dimensionality 

reduction technique that transforms correlated variables into a smaller set of components while 

preserving most of the data variation (Jolliffe & Cadima, 2016). Thus, BERT and PCA are 

treated as an exploratory strategy to compress textual menu information, not as evidence of 

causality or as prior proof of predictive gain. 

 



3. METHODOLOGY 

3.1 Research design 

The research follows an applied, exploratory approach guided by DSR. The practical 

problem consists of preparing a reliable dataset for meal demand forecasting in a school 

restaurant. The developed artifact is a data flow organized in computational notebooks, 

responsible for ingesting heterogeneous sources, consolidating daily granularity, documenting 

quality, and generating predictive attributes for future machine learning models. 

The temporal scope covers the period from January 1, 2023, to December 31, 2025, 

totaling 1,096 calendar days. The sources include individual reservations, individual 

consumption records, menus, academic calendar, and weather. Ingestion was separated by 

domain, avoiding premature coupling between variables of different natures. This separation 

also facilitates auditing, re-execution, and localized correction when a source presents 

inconsistencies. 

3.2 Ingestion and Bronze layer 

The Bronze layer was built through five ingestion computational notebooks: 

reservations, consumption records, menus, academic calendar, and weather variables. This 

division was adopted because each source has its own rules for reading, duplicate handling, 

dates, mandatory columns, and operational interpretation. 

At the end of ingestion, 84,453 reservation records, 66,869 consumption records, 1,095 

menu records, 1,096 calendar observations, and 1,096 weather observations were preserved. In 

the Bronze layer, data were persisted in two complementary formats: Parquet, due to its storage 

efficiency, preservation of data types, and ease of reading in computational notebooks; and 

CSV, because it favors manual inspection, processing transparency, and auditing of raw 

records. This decision meets the traceability requirement: any subsequent transformation can 

be compared with the ingested source. 

3.3 Silver consolidation 

The Silver layer consolidates the sources at daily granularity. This step is decisive 

because demand forecasting models will be trained by day, not by individual. Therefore, 

individual reservations and consumption records were aggregated into daily metrics, while 

calendar, weather, and menu data were aligned by date. The result was a master dataset with 

1,096 rows and 77 columns. 



A central concern was to differentiate observed days, estimated days, and days not 

applicable for modeling. Instead of silently replacing missing values with imputed values, 

Silver records modeling criteria and quality markers. This choice reduces the risk of 

transforming collection failure into real demand behavior. It also allows future models to use 

only modelable days or to test scenarios with different tolerance levels. 

Missing data treatment was conducted conservatively and traceably. For weather 

variables, a simple filling rule was planned in case any day lacked records, using nearby days 

as a reference. In the final dataset, however, this routine had no relevant impact, because 

weather records did not present significant gaps. 

For the menu, imputation was restricted to school days without dish information and 

used the mode by day of the week, that is, the most frequent category observed on that same 

weekday across the historical series. When there was insufficient information in this grouping, 

the global mode of the dataset was used as an alternative. 

Missing reservations and consumption records, or very low consumption values 

classified as suspicious, were estimated using a linear regression model fitted only with days 

considered valid, using calendar, reservation, weather, and menu variables. When the amount 

of valid data was insufficient for fitting, the temporal median was used as a conservative 

alternative. In all cases, original observed values were preserved in separate columns and 

imputed records were marked for auditing. 

Thus, Silver does not erase data uncertainty. It creates three complementary views: 

observed values, estimated values, and values intended for modeling. Modeling columns are 

used to form complete series, while imputation markers and applied criteria enable later 

auditing. This decision is important because it prevents an estimated value from being confused 

with a direct empirical observation. 

3.4 Gold engineering 

The Gold layer transforms Silver into a machine learning matrix. Calendar variables, 

consumption and reservation lags, moving averages, weather attributes, categorical menu 

encodings, and relevant interactions were created. After the filters needed to avoid initial rows 

without sufficient temporal history, Gold resulted in 548 records and 140 attributes. 

The derived variables were built from information available before the meal, reducing 

the risk of temporal leakage. Consumption and reservation lags, moving averages calculated 

with temporal shifting, calendar indicators, cyclical transformations of weekday and month, 

weather attributes, and menu indicator variables were generated. This strategy makes it possible 

to represent recent demand memory, institutional seasonality, and operational context. 



Variables that would carry direct information from the outcome itself were also 

excluded from the list of predictive inputs, such as observed consumption, estimated 

consumption, modeling consumption, and audit markers. These fields remain in the dataset for 

traceability, but should not be used as direct model inputs. Thus, Gold differentiates the target 

variable, quality metadata, and attributes effectively eligible for prediction. 

This stage also separates families of attributes. Linear models tend to benefit from scaled 

variables, controlled encodings, and lower collinearity; tree-based models better handle 

nonlinearities, interactions, and sparse indicator variables; temporal models depend on lags and 

moving averages. Therefore, feature engineering was documented not as a single universal set, 

but as a catalog of attributes that can be selected according to the algorithm. 

3.5 Exploratory semantic representation with BERT and PCA 

In addition to categorical menu variables, an exploratory textual representation with 

BERT was prepared. The input text was formed by combining the main protein and preparation 

attributes, generating a short description of each day's menu. Then, BERT transformed these 

descriptions into numerical vectors, enabling computational representation of textual 

similarities between menus. 

Because these vectors have many dimensions for a dataset with 548 modelable records, 

Principal Component Analysis (PCA) was applied to compress the textual representation. The 

procedure reduced semantic information to 44 components, preserving about 95% of the 

accumulated variance. This stage was kept as an exploratory and complementary block, without 

replacing the interpretable protein, preparation, and dish style variables. 

4. RESULTS AND DISCUSSION 

4.1 Formation of the data artifact 

Before interpreting consumption patterns, it is necessary to understand how the 

analytical dataset was formed. Figure 1 presents the artifact preparation funnel, indicating the 

transition from the complete calendar to the subsets effectively useful for analysis and 

modeling. 



 
Figure 1. Data artifact preparation funnel. Source: authors’ own elaboration. 

Figure 1 summarizes the transition from the complete calendar to the analytical dataset. 

The data flow starts from 1,096 days, identifies 558 modelable days for the school restaurant, 

maintains 446 analytical observations with sufficient observed data, and reaches 548 records in 

the Gold layer after the creation of temporal variables. The apparent difference between 

analytical observations and Gold occurs because Gold incorporates temporal structure and can 

retain modelable records with explicit criteria. 

This funnel is important because it prevents a naive reading of the dataset. Not every 

calendar day represents a useful operating day for the restaurant, and not every operating day 

has observed consumption with sufficient quality. The visualization demonstrates the need to 

distinguish calendar availability, operational applicability, and readiness for modeling, which 

is aligned with Tripathi et al.'s (2021) concern with the robustness of data-driven processes. 

4.2 Temporal dynamics of reservations and consumption 

After delimiting the available data volume, the next step consists of observing how 

reservations and consumption behave over time. Figure 2 compares these two series because 

the difference between consumption intention and effective consumption is one of the main 

sources of operational uncertainty in the school restaurant. 



 
Figure 2. Temporal evolution of reservations and modeled consumption in the school restaurant. Source: 

authors’ own elaboration. 

Figure 2 presents the temporal evolution of reservations and modeled consumption, 

smoothed by a 14-day moving average. This procedure calculates, for each date, the average of 

values observed in previous days, reducing point fluctuations and facilitating visualization of 

the general demand trend. 

The distance between the lines indicates that reservation is a relevant signal, but it is not 

automatically equivalent to effective consumption. This behavior is compatible with the 

literature on attendance forecasting in food services, in which planned counts need to be 

adjusted by the users' actual presence (Malefors, 2022; Rodrigues et al., 2024). 

The points highlighted as suspicious low consumption represent records that require 

methodological attention. Because consumption is manually recorded, very low values on 

operating days may reflect collection failures, and not necessarily real low demand. Therefore, 

the artifact does not erase these records; it flags them and creates modeling criteria, allowing 

future models to test the impact of including them or treating them conservatively. 

4.3 Weekly demand profile 

In addition to the aggregated temporal evolution, demand must be observed within the 

weekly operating routine. Figure 3 focuses the analysis from Monday to Friday, because these 

are the days that represent regular student meal service in the studied context. 

 



 
Figure 3. Average weekly demand profile, from Monday to Friday. Source: authors’ own elaboration. 

Figure 3 shows that average consumption is not uniformly distributed throughout the 

week. There are differences between the analyzed years and between weekdays, indicating that 

the position of the day in the weekly calendar carries relevant information for demand 

forecasting. 

This result justifies the creation of calendar variables in the Gold dataset. To represent 

cyclical patterns, such as weekday and month, sine and cosine transformations were used, 

allowing the model to recognize proximity between recurring periods. The literature on 

forecasting in collective food services also points to calendar and seasonality as relevant factors, 

especially when operations depend on school routines, holidays, and academic periods 

(Rodrigues et al., 2024; Turker, 2025). 

4.4 Monthly intensity and operational seasonality 

Because the week alone does not explain demand variation, it is also necessary to 

observe whether certain months concentrate higher or lower consumption. For this purpose, 

Figure 4 presents a heatmap that crosses month and weekday, allowing demand intensity to be 

visualized in a single representation. 



 
Figure 4. Demand intensity by month and weekday. Source: authors’ own elaboration. 

Figure 4 indicates that demand varies not only between weekdays, but also between 

months of the year. Periods of greater intensity are observed, such as months with more regular 

academic operation, as well as periods of lower demand, possibly associated with vacations, 

recesses, or academic transitions. 

This pattern reinforces that demand should not be modeled only as a mechanical 

continuation of the previous day. There are seasonal and institutional components associated 

with the academic calendar, and these components need to be explicit in the Gold dataset 

through variables such as month, year, holiday, school day, academic events, and operation 

indicators. 

4.5 Variability of observed consumption 

After evaluating average patterns, it is important to examine the dispersion of observed 

data. Figure 5 presents a boxplot to compare the distribution of consumption between 

weekdays, allowing the observation of median, amplitude, concentration of values, and extreme 

records. 



 
Figure 5. Dispersion of observed consumption by weekday. Source: authors’ own elaboration. 

Figure 5 shows that consumption variability is not the same on all weekdays. Some days 

present greater amplitude and a greater presence of extreme values, indicating that demand may 

be affected by punctual events, routine changes, or atypical operational records. 

This result reinforces that it is not enough to predict a general average consumption. 

Future models will need to deal with variability, extreme values, and regime changes. For the 

current stage, the main contribution is to diagnose this heterogeneity before modeling, avoiding 

algorithm selection without understanding the empirical distribution of the target variable. 

4.6 Effect of protein type on consumption 

The menu was initially analyzed by main protein, because this category provides a 

simple and interpretable reading of food composition. Figure 6 presents differences in median 

demand between protein groups, functioning as an initial diagnosis of the possible menu effect 

on consumption. 



 
Figure 6. Median demand by main menu protein. Source: authors’ own elaboration. 

In Figure 6, differences in median demand between protein groups are presented, but 

this reading must be interpreted with caution. The variation bars indicate that there is dispersion 

within each group, which prevents claiming direct causality between protein and consumption. 

Even so, the result reinforces that menu attributes may carry useful information for demand 

forecasting, in dialogue with Kim et al. (2023), who treat textual menu information as a 

potential source of forecasting in cafeteria environments. 

The refinement of the menu computational notebook reduced the residual protein 

category to only two cases classified as "Other," which strengthens the quality of this attribute 

block. Still, categories such as "no operation" and days without a menu must be interpreted 

carefully, because they represent operational context and not food preference. This distinction 

prevents the model from confusing absence of operation with rejection of a given dish. 

4.7 Interaction between protein and preparation 

Protein analysis alone does not capture all menu information. For this reason, Figure 7 

crosses protein and preparation, allowing verification of whether certain food combinations 

appear associated with differences in median demand. 



 
Figure 7. Median demand by combination of protein and preparation. Source: authors’ own elaboration. 

Figure 7 indicates that demand may vary according to the combination between main 

protein and preparation method. For example, similar protein categories may present different 

medians when associated with preparations such as stewed in sauce, fried, grilled, or roasted. 

This reading does not imply direct causality, but suggests that menu structure contains relevant 

contextual signals. 

This visualization justifies the creation of categorical menu attributes and possible 

interactions between food families. From the perspective of feature engineering, it shows why 

the menu was treated at three levels: main protein, main preparation, and dish style. Style 

maintains a larger residual category because not every dish has a specific culinary identity, but 

this is acceptable when the variable is complementary and does not replace protein and 

preparation. 

4.8 Exploratory attribute selection 

With the Gold dataset built, it became possible to conduct a first analysis of attribute 

relevance. Figure 8 summarizes this analysis through the importances estimated by ExtraTrees, 

a method based on extremely randomized trees (Geurts et al., 2006). The use of the method at 

this stage is exploratory and seeks to guide future comparisons between sets of variables. 



 
Figure 8. Most relevant predictors according to ExtraTrees. Source: authors’ own elaboration. 

Figure 8 highlights the centrality of reservations as a predictive signal, while also 

emphasizing moving averages, temporal lags, calendar, and contextual variables. This reading 

is coherent with the demand forecasting literature, which values recent history and operational 

variables to anticipate consumption (Chaudhari et al., 2025; Rodrigues et al., 2024). 

It is important to treat this figure as supporting analysis, not as a final conclusion of 

causality. Tree-based importances may favor variables with greater separation power within the 

sample and depend on preprocessing choices. Even so, the ranking is useful to guide the next 

modeling stage, especially when comparing linear, temporal, categorical, and semantic attribute 

sets. 

4.9 Semantic representation of the menu 

To complement the analysis, the semantic representation of the menu was evaluated in 

terms of compactness. Figure 9 shows the accumulated variance after applying PCA to the 

vectors generated by BERT. The dotted line indicates the threshold of 95% preserved variance, 

used as a reference to define how many principal components would be retained. 



 
Figure 9. Accumulated variance of BERT components reduced by PCA. Source: authors’ own elaboration. 

Figure 9 shows that 44 principal components preserve approximately 95.16% of the 

accumulated variance of the BERT vectors. This means that the textual menu representation 

could be reduced to a smaller set of variables without discarding most of the statistical 

information contained in the original vectors. This reduction is relevant because the Gold 

dataset has 548 records, and using all original BERT dimensions could increase model 

complexity and the risk of overfitting. 

From a conceptual point of view, this stage expands the reading of the menu without 

replacing manual classification. Manual categories capture explicit groups, such as protein and 

preparation; BERT vectors can capture semantic proximities between texts. Combining both 

approaches preserves interpretability and opens a test hypothesis, following Devlin et al. (2019) 

and Kim et al. (2023), that language representations can extract useful signals from food 

descriptions. 

4.10 Consolidation of Gold datasets for modeling 

After the exploratory analysis, the resulting artifact is not limited to the visualizations 

presented. The main technical delivery of this stage is the consolidation of Gold datasets, which 

organize data at daily granularity and bring together temporal, operational, weather, and menu 

attributes. These datasets materialize the processing path initiated in Bronze ingestion and 

qualified in Silver consolidation. 

 

 



 

Table 1. Gold datasets generated for the future predictive modeling stage. 
 

Gold dataset Purpose Main content Planned use 
Main tabular Gather structured Reservations, historical Train and compare predictive 
Gold attributes for consumption, lags, moving models with interpretable 

modeling. averages, calendar, weather, attributes. 
and categorized menu. 

Exploratory Represent menu text Components derived from Test whether textual menu 
semantic Gold compactly. BERT and reduced by PCA. descriptions add predictive 

information. 
Integrated Gold Combine structured Structured attributes enriched Compare models with and 

and semantic with semantic components. without semantic attributes. 
attributes. 

Source: authors’ own elaboration. 

Based on this structure, three complementary analytical datasets were generated, each 

oriented toward different predictive modeling perspectives. The main tabular Gold consolidated 

548 records and 140 attributes; the exploratory semantic Gold maintained the same 548 records 

and 44 components derived from BERT and PCA; and the integrated Gold brought together 

structured and semantic attributes in an expanded dataset with 184 columns. 

These datasets are technically prepared for subsequent predictive modeling stages. 

Within the scope of this article, the main contribution is to provide traceable, documented 

analytical datasets that are coherent with the operational problem. Complete predictive 

validation should be conducted in a specific study, with temporal separation between training 

and testing, comparison against baselines, and evaluation of error metrics. 

4.11 Implications of the Gold dataset for future modeling 

The Gold datasets indicate that predictive modeling should be conducted by families of 

attributes, rather than by a single fixed set of variables. Linear models will require attention to 

scale, collinearity, and the number of indicator variables; tree-based models may explore 

interactions and expanded categorical variables; and temporal models should treat lags and 

moving averages carefully to avoid future information leakage. 

Another direct implication of the artifact is the separation between observed 

consumption, estimated consumption, and modeling consumption. This distinction responds to 

a common limitation in operational datasets: gaps and suspicious records cannot simply be 

deleted, but they should also not be treated as absolute truth. The developed artifact makes it 

possible to test different training strategies while maintaining transparency about the criteria 

used. 

Additionally, the integration of BERT and PCA should be understood as an exploratory 

hypothesis for future evaluation. The presence of 44 semantic components with high preserved 



variance indicates dimensional feasibility, but does not, by itself, demonstrate predictive gain. 

This gain should be measured in a later stage through temporal validation and comparison 

against baselines with and without semantic attributes. 

5. CONCLUSION 

This article aimed to develop and exploratorily evaluate a Gold analytical dataset 

intended to support future studies of meal demand forecasting in a school restaurant. To this 

end, the study began with data ingestion in the Bronze layer, advanced to daily consolidation 

in the Silver layer, and subsequently structured Gold datasets oriented toward demand analysis 

and modeling. This path made it possible to transform heterogeneous operational records into 

more consistent, documented, and traceable analytical datasets. 

The results show that the layered organization favored the identification of patterns that 

would not be evident in the original records. The exploratory analysis indicated that demand is 

influenced by calendar, recent history, reservations, weekly variability, and menu composition. 

The visualizations also highlighted the importance of distinguishing observed consumption, 

estimated consumption, and consumption used for modeling, preventing gaps, suspicious 

records, or non-operating days from being treated as equivalent observations. 

As a practical contribution, the constructed analytical dataset offers structured sets that 

can support future decisions on production planning, waste reduction, and resource allocation. 

As a scientific and methodological contribution, the study demonstrates how exploratory data 

analysis can function as an initial evaluation stage in Design Science Research, connecting data 

quality, feature engineering, and dataset preparation for predictive modeling. 

Some limitations must be acknowledged. The evaluation carried out is exploratory and 

does not yet compare the performance of predictive models. In addition, the results depend on 

the completeness and reliability of the available administrative records, especially regarding 

manual consumption records, reservations, and the menu. There may also be unobserved 

factors, such as internal events, routine changes, individual student preferences, or specific 

operating conditions, that influence demand and are not fully represented in the current datasets. 

As future work, predictive models should be applied to the constructed Gold datasets 

using temporal validation and comparison against baselines. It is also suggested to separately 

evaluate models with structured attributes, models with semantic menu attributes, and models 

that combine both blocks. Expansion to new periods or other units may also verify the 

robustness of the analytical dataset and support more sustainable and data-driven solutions for 

school food management. 

 



REFERENCES 

Chaudhari, M. A., Phapale, A., Gagare, P., Kardile, T., & Phatangare, A. (2025). Forecasting 

and modelling of food demand supply chain using machine learning. International 

Journal of Innovative Research in Engineering & Multidisciplinary Physical Sciences, 

13(2). 

Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of deep 

bidirectional transformers for language understanding. Proceedings of NAACL-HLT 

2019, 4171-4186. 

Geurts, P., Ernst, D., & Wehenkel, L. (2006). Extremely randomized trees. Machine Learning, 

63, 3-42. https://doi.org/10.1007/s10994-006-6226-1 

Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for 

maximum impact. MIS Quarterly, 37(2), 337-355. 

https://doi.org/10.25300/MISQ/2013/37.2.01 

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information 

systems research. MIS Quarterly, 28(1), 75-105. https://doi.org/10.2307/25148625 

Jolliffe, I. T., & Cadima, J. (2016). Principal component analysis: A review and recent 

developments. Philosophical Transactions of the Royal Society A, 374(2065), 

20150202. https://doi.org/10.1098/rsta.2015.0202 

Kim, S., Gu, N., Moon, J., Kim, K., Hwang, Y., & Lee, K. (2023). Comparative analysis of 

model performance for predicting the customer of cafeteria using unstructured data. 

Communications for Statistical Applications and Methods, 30(5), 485-499. 

https://doi.org/10.29220/CSAM.2023.30.5.485 

Malefors, C. (2022). Food waste reduction in the public catering sector [Doctoral thesis, 

Swedish University of Agricultural Sciences]. Acta Universitatis Agriculturae Sueciae, 

2022:39. 

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science 

research methodology for information systems research. Journal of Management 

Information Systems, 24(3), 45-77. https://doi.org/10.2753/MIS0742-1222240302 

Rodrigues, M., Miguéis, V., Freitas, S., & Machado, T. (2024). Machine learning models for 

short-term demand forecasting in food catering services: A solution to reduce food 

waste. Journal of Cleaner Production, 435, 140265. 

https://doi.org/10.1016/j.jclepro.2023.140265 

Tripathi, S., Muhr, D., Brunner, M., Jodlbauer, H., Dehmer, M., & Emmert-Streib, F. (2021). 

Ensuring the robustness and reliability of data-driven knowledge discovery models in 



production and manufacturing. Frontiers in Artificial Intelligence, 4, 576892. 

https://doi.org/10.3389/frai.2021.576892 

Turker, G. F. (2025). Reducing food waste in campus dining: A data-driven approach to 

demand prediction and sustainability. Sustainability, 17(2), 379. 

https://doi.org/10.3390/su17020379 

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & 

Polosukhin, I. (2017). Attention is all you need. Advances in Neural Information 

Processing Systems, 30.