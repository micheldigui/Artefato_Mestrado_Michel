---
source_file: "2025-Reducing-Food-Waste-in-Campus-Dining-A-DataDriven-Approach-to-Demand-Prediction-and-Sustainability_2025_Multidisciplinary-Digital-Publishing-Institute-MDPI.txt"
original_rel_path: "Trabalhos\Artigos\Aproveitar fortemente\txt\2025-Reducing-Food-Waste-in-Campus-Dining-A-DataDriven-Approach-to-Demand-Prediction-and-Sustainability_2025_Multidisciplinary-Digital-Publishing-Institute-MDPI.txt"
category: "Artigos_Aproveitar_fortemente"
extension: ".txt"
sha256: "00959531d5f2d156ea1ac81386c21581632e3d494368ab69b5932fdca630ac97"
extracted_at: "2026-09-19T23:16:59.250544"
---

﻿Article

Reducing Food Waste in Campus Dining: A Data-Driven
Approach to Demand Prediction and Sustainability
Gul Fatma Turker

Department of Computer Engineering, Suleyman Demirel University, 32260 Isparta, Turkey;
gulturker@sdu.edu.tr; Tel.: +90-246-211-0876

Abstract: Tracking density in universities is essential for planning services like food,
transportation, and social activities on campus. However, food waste remains a critical
challenge in campus dining operations, leading to significant environmental and economic
consequences. Addressing this issue is crucial not only for minimizing environmental
impact but also for achieving sustainable operational efficiency. Campus food services
significantly influence students’ university choices; thus, forecasting meal consumption and
preferences enables effective planning. This study tackles food waste by analyzing daily
campus data with machine learning, revealing strategic insights related to food variety and
sustainability. The algorithms Linear Regression, Extra Tree Regressor, Lasso, Decision Tree
Regressor, XGBoost Regressor, and Gradient Boosting Regressor were used to predict food
preferences and daily meal counts. Among these, the Lasso algorithm demonstrated the
highest accuracy with an R2 metric value of 0.999, while the XGBRegressor also performed
well with an R2 metric value of 0.882. The results underline that factors such as meal variety,
counts, revenue, campus mobility, and temperature effectively influence food preferences.
By balancing production with demand, this model significantly reduced food waste to
28%. This achievement highlights the potential for machine learning models to enhance
sustainable dining services and operational efficiency on university campuses.

Keywords: campus mobility; food prediction; food waste reduction; machine learning;
meal variety

Academic Editors: Ching-Hsin Wang
and Wei-Sho Ho

Received: 23 November 2024 1. Introduction
Revised: 30 December 2024 The mobility of student and staff numbers in universities and higher education institu-
Accepted: 5 January 2025 tions is an important indicator of campus density. This density requires strategic planning
Published: 7 January 2025

and resource allocation to effectively manage security, mobility, energy consumption, food
Citation: Turker, G.F. Reducing Food needs, and other related issues in various areas of the campus [1]. Campus food services are
Waste in Campus Dining: A

of great importance within the university and serve as a significant factor in the preferences
Data-Driven Approach to Demand
Prediction and Sustainability. of prospective students [2]. University campus food services typically consist of different
Sustainability 2025, 17, 379. https:// areas such as the central dining hall and cafeteria, which provide services to meet the food
doi.org/10.3390/su17020379 needs of students and staff with various options [3]. However, insufficient management of
Copyright: © 2025 by the author. food services often leads to significant food waste, which not only increases operational
Licensee MDPI, Basel, Switzerland. costs but also contributes to environmental degradation, making this an urgent issue for
This article is an open access article sustainable campus management. Therefore, the quality and variety of food services
distributed under the terms and directly affect the satisfaction and efficiency levels of campus life [4,5].
conditions of the Creative Commons Artificial intelligence (AI) and machine learning (ML) enable more efficient and effec-
Attribution (CC BY) license

tive delivery of various services on university campuses [6]. AI and ML optimize the use of
(https://creativecommons.org/
licenses/by/4.0/). resources and increase student and staff satisfaction to ensure efficiency and sustainability

Sustainability 2025, 17, 379 https://doi.org/10.3390/su17020379



Sustainability 2025, 17, 379 2 of 22

in the services provided [7]. Although studies such as those by Yang et al. (2022) and
Lorenzoni et al. (2021) have explored aspects like clustering consumption patterns or
analyzing transaction data, these approaches often fail to integrate environmental metrics
and broader sustainability goals [8,9]. Within the scope of food services, one of the most
important services provided at the university, it is observed that machine learning meth-
ods are effective in the management and planning of campus food services [10]. Despite
this, existing research lacks a comprehensive framework that connects campus density,
dining preferences, and sustainability outcomes, leaving critical gaps in understanding the
systemic impact of food waste in universities.

ML has also been instrumental in improving sustainability efforts in food waste
management by enabling better prediction models and inventory management [11]. In
addition, the quality of food service in campus areas is an influential factor in satisfying
students and staff [12], making it crucial that catering operations are carried out with this
quality in mind [13,14]. ML has been utilized to optimize food quality prediction, enhance
quality control processes for food products, and predict shelf life. Specifically, the Random
Forest Optimizer method was applied to forecast food freshness in storage areas, achieving
an impressive accuracy of 94.01% [15]. It is also applied in food identification processes
such as food recognition, calorie measurement, and calorie calculations [16]. Particularly,
ML optimizes the use of raw materials by increasing food production efficiency, analyzing
market dynamics, enhancing consumer preferences, and improving inventory management
by forecasting demand [7,17].

In the literature, there are studies examining various aspects of catering services on
university campuses. For example, Yang et al. (2022) analyzed canteen consumption data
using k-means clustering and large learning network architectures to identify students in
need of financial aid. Lorenzoni et al. (2021) applied a multivariate clustering method to
data from cashier transactions at a university in Pisa, demonstrating that students prefer
processed food and proteins [8,9]. Demirel and Türk (2024) analyzed the demographic struc-
ture of Iğdır University students and their knowledge about organic products, revealing a
significant relationship between organic products and physical health [18]. Furthermore,
Rahman (2024) evaluated students’ cafeteria satisfaction and its influencing factors at a pub-
lic university in Bangladesh, employing machine learning Recursive Feature Elimination
(RFE) methods [19].

Research on demand and forecasting models developed to analyze consumer pref-
erences, food preferences, and meal variety highlights the importance of these aspects in
reducing waste and enhancing sustainability [20]. Martin-Rios et al. (2020) also empha-
sized that sustainability-oriented innovations in food waste management technology are
critical for reducing waste and aligning with circular economy principles in campus food
services [9]. One of the previous studies addressing food waste reduction in campuses
examined the impact of plate shape and size on minimizing waste. Richardson et al. (2021)
used machine learning algorithms to predict meal demand and demonstrated that oval
plates significantly reduced food waste. These findings highlight the importance of physical
factors that complement machine learning-based meal demand predictions [20]. In another
study, the effects of tray and tray-less dining systems on university students’ food choices,
consumption, and waste behaviors were analyzed, revealing significant implications for
food management [21]. Aci and Yergök (2023) developed demand forecasting models for
university dining halls, incorporating the calendar effect and turnstile passage data, and
examined eighteen Machine Learning models categorized under five main techniques.
Among these, the EDT Boosted model demonstrated the most effective prediction perfor-
mance, achieving metrics such as MSE = 0.51, MAE = 0.50, and R = 0.96, highlighting its
superiority in forecasting meal demand [22].



Sustainability 2025, 17, 379 3 of 22

Finally, some studies explore the broader effects of university dining services on
student satisfaction and well-being through surveys and analytical methods [23–25].
Simulation-based approaches, such as Kambli et al. (2020), revealed that customer wait-
ing times can be reduced by 45% through optimized capacity allocation and queue
management [3]. Additional research by Oliveria et al. (2024) assessed dietary prefer-
ences among Portuguese university students, highlighting vending machine consumption
and lunchbox usage rates. Sakai et al. (2022) examined unhealthy eating habits and nutrient
deficiencies in Indonesian canteen menus [26,27].

Research demonstrates that the efficiency, student satisfaction, and sustainability of
university dining services have been extensively investigated through various studies.
These studies utilize diverse datasets, including meal types, number of meals, calorie
counts, and food preferences. While satisfaction surveys are commonly employed to
evaluate dining experiences, the development of automated systems that integrate real-
time food preferences and consumption data offers a more effective approach. Although
such surveys provide valuable insights, machine learning models frequently address
isolated issues and establish limited relationships with a narrow set of variables, thereby
diminishing their overall impact on comprehensive campus management strategies.

Sustainability in universities goes beyond reducing food waste; it aligns with the
global movement towards a circular economy and resource efficiency. Addressing food
waste within campus systems not only mitigates environmental harm but also serves as
a model for broader societal sustainability practices. This study, therefore, bridges these
gaps by combining machine learning models with campus-specific data to create actionable
insights, contributing to reduced waste and enhanced operational efficiency.

In this study, cafeteria turnover data, dining hall food types, number of meals, campus
density, and daily temperature values were comprehensively analyzed. Machine learning
algorithms were applied to predict outcomes, such as the most preferred food types and the
number of meals required for dining services. Furthermore, the daily and hourly flow of
people entering the campus and food consumption patterns were examined to assess their
influence on students’ food preferences. These analyses identified the most favored food
items, predicted meal quantities, and highlighted preferences in consumption areas using
high-performance models. The findings contribute to reduced food waste and enhanced
sustainability in campus dining services.

2. Materials and Methods
2.1. Dataset

In the research, the dataset was created by selecting the year 2024, spring semester,
when the education and training process is the busiest in Suleyman Demirel University
Campus. The data consists of daily records of various activities and parameters within the
campus. Campus entrance information, university dining hall entrance information (staff
and student), and university commercial cafeteria turnover information were obtained from
the university. In addition to these data, the database was enriched by obtaining publicly
published weather information, food types in the dining hall, and calorie information. This
database, which contains detailed information such as campus mobility (215,504 people),
number of meals (55,006 pieces), daily activities, etc., was analyzed to determine the effects
of campus density, food preferences, cafeteria performance, and weather.

The dataset is divided into several main categories: temporal, spatial, meteorological,
food, user statistics, and financial information. Temporal data includes detailed times-
tamps such as date, day, month, year, hour, and minute. Spatial information includes door
movements reflecting campus entry and exit movements. Meteorological data provides in-
formation on weather conditions that may affect campus activities by recording the average



Sustainability 2025, 17, 379 4 of 22

daily maximum and minimum temperatures. Furthermore, daily menu information forms
the food data category, while user statistics segment the population into students, academic
staff, and administrative staff. Finally, financial data is represented by the turnover figures
of the campus cafeteria. On the data obtained, missing data were edited, categorical data
were transformed, and data were scaled.

Table 1 provides an overview of all the variables used in the analysis, along with
clear descriptions of their roles and significance in the context of the study. This detailed
breakdown ensures transparency and highlights the data-driven, systematic approach of
the study. By including a comprehensive description of the dataset, this work establishes a
solid foundation for understanding and addressing food waste on campus.

Table 1. Descriptive features of the dataset.

Feature Name Description
GATE Gate entry point for data collection.
MOVEMENT Indicator of movement type (e.g., entry, exit).
ID Unique identifier for records.
DATE Date and time of the recorded data.
MONTH NAME Name of the month in the recorded data.
WEEKDAYS Day of the week in the recorded data.
AVERAGE TEMPERATURE Average temperature on the recorded day.
MAIN LUNCH 1 Primary dish served for lunch.
MAIN LUNCH 2 Secondary dish served for lunch.
MAX TEMPERATURE Maximum temperature on the recorded day.
MIN TEMPERATURE Minimum temperature on the recorded day.
ADDITIONAL PRODUCTS Additional products available during lunch.
SOUP Type of soup served for lunch.
NOON STUDENT Number of students during noon hours.
NOON ADMINISTRATIVE Number of administrative staff during noon hours.
TOTAL DAILY PERSONS Total number of people on the recorded day.
CALORIES (KCAL) Calories of the meal in kilocalories.
STAFF LUNCH Number of staff members having lunch.
STAFF ENTRY Staff members’ entry count.
CANTEEN REVENUE Revenue generated by the canteen.
TOTAL DAILY MOVEMENT PERSON Total movement of persons on the recorded day.
MENU Details of the menu served.
INVERSE CANTEEN REVENUE Inverse value of canteen revenue for some analysis.

2.2. Feature Extraction
The process of creating numerical features from raw, unprocessed data without com-

promising dataset integrity is known as feature extraction. Feature selection is an important
step in the development of machine learning models. The number of input features can
range from two to hundreds of features, many of which may be insignificant or have a
lower correlation with the target variables. Feature selection methods improve the per-
formance of models on high-dimensional datasets by reducing training time, improving
generalization, and enhancing interpretability [28]. Model parameters were optimized
with feature engineering to enhance model performance. The menus of the days of the
week were obtained by web scraping, and the minimum and maximum temperature values
for those days were added with the same method. This data was used as a feature for a
machine learning model or analysis. In addition, the need for categorization of the menus
was identified in the initial analysis, and the success of the model was increased by adding
new features in the process.

During the feature extraction phase, the missing values in the data set were identified
in the missing data editing stage, and the data were completed. In the data transformation



Sustainability 2025, 17, 379 5 of 22

phase, the data should be converted into numerical formats that can be used by regression
algorithms. In this process, categorical data were converted into numerical data with the
one-hot encoding method. The unit matrix provides many mathematical and structural
advantages in data transformations and algorithms. The superiority of the data over each
other was removed. This was achieved by associating the data with the unit matrix. When
columns are in string format, converting with one-hot encoding often results in vectors
consisting of a large number of zeros. In such cases, a “sparse matrix” was used to store the
data more efficiently. The sparse matrix reduces memory usage by storing only positions
that are “1”.

2.3. Preprocessing Using StandardScaler
Standardization is a data preprocessing step that allows data to scale within a certain

range and speeds up algorithm calculations. In particular, this process transforms the
features in the dataset to have a mean of zero and a standard deviation of one. To do
this, the mean is subtracted from each dataset and the result is divided by the standard
deviation. Commonly used scalers for transforming data sets include the robust scaler,
min-max scaler, normalizer, and standard scaler. The following formula (Equation (1)) can
be used to make adjustments: σ is the standard deviation, µ is the mean, and W is the initial
value [29].

W − µ
Y = (1)

σ

Data scaling, transformation and feature reduction create a standardized data set,
reducing prediction errors. The accuracy of models is affected by processes such as feature
selection, data cleaning, and scaling. Estimating the number of meals per day is achieved
through standardization in data preparation, which can be achieved using tools such
as StandardScaler. By normalizing the data within a certain range, consistent measure-
ments across variables are ensured. This process was applied to prevent overfitting and
under fitting.

2.4. Machine Learning Model and Regression
Regression algorithms aim to predict the value of the dependent variable using one

or more independent variables [30]. With this data set, regression algorithms can make
various predictions [31]. In this study, a total of 5 machine learning prediction algorithms
were trained considering the characteristics of the dataset, and their success metrics and
test graphs were interpreted and analyzed. The selection of these algorithms was based on
the structural characteristics of the dataset (numerical and categorical variables), the type
of relationship with the dependent variable (linear and nonlinear relationships), and the
flexibility and accuracy of the models.

The following features were included as input parameters: ‘average temperature’,
‘max temperature’, ‘min temperature’, ‘noon student’, ‘noon administrative’, ‘calories
(kcal)’, ‘staff lunch’, ‘staff entry’, ‘canteen revenue’, and ‘menu’. These variables were
selected for their predictive relevance to the target variable. The primary target parameter
was ‘total daily dining persons’, representing the total number of individuals interacting
with the system daily. This parameter is essential for understanding campus movement
and dining requirements.

The dataset was divided into training (80%) and test (20%) subsets to effectively eval-
uate the models’ learning and prediction performance on unseen data. This partitioning
ensures that the models generalize their learning and maintain accuracy on data not in-
cluded in the training process. Feature importance and transformations played a significant
role in the analysis. For instance, “average temperature” was identified as a key predictor
in models such as Lasso regression, where its coefficient highlighted a strong influence on



Sustainability 2025, 17, 379 6 of 22

the target variable. To ensure optimal contribution to prediction accuracy, the “average
temperature” feature was mathematically transformed by multiplying it by a factor of 10.
In this context, coefficients represent the extent to which a unit change in an independent
variable affects the target outcome, emphasizing why certain features are more critical in
predictive modeling.

2.4.1. Gradient Boosting Regressor
Gradient Boosting Regressor is an ensemble learning method that builds a strong

predictive model by sequentially training weak learners (usually decision trees). Each step
minimizes cumulative errors, ensuring high accuracy [32]. This algorithm was selected due
to its ability to handle both numerical (e.g., temperature, total movement) and categorical
(e.g., gate type, meal type) variables effectively. Tree-based models like Gradient Boosting
excel in modeling complex nonlinear relationships, such as predicting meal counts. Its
robust performance and low error rates make it ideal for this dataset.

2.4.2. XGBoost Regressor
XGBoost Regressor is a high-performance gradient boosting algorithm known for its

speed, scalability, and detailed hyperparameter control. It is effective on large datasets
and ensures high accuracy [33]. The algorithm was chosen for its ability to handle both
numerical (e.g., temperature) and categorical (e.g., gate type) variables. Its scalability and
capacity to model nonlinear patterns make it ideal for predicting meal counts with high
efficiency and accuracy.

2.4.3. Linear Regression
Linear Regression is a basic regression model widely used in statistics and machine

learning and is used to model the linear relationship between the dependent variable
and independent variables; basically, it allows predicting the target variable with a linear
combination of features (predictor variables) given as input, and this model is used to
understand the relationship between the variables in the data set, make predictions, and
analyze the effects of the variables; its performance varies depending on the linear relation-
ship of the features in the data set and the suitability of the model [34]. This algorithm was
selected for its simplicity and ability to analyze linear trends in numerical variables (e.g.,
temperature, total movement). It provides interpretable results and efficiently captures
primary relationships in the dataset.

2.4.4. Linear Regression Lasso
Lasso (Least Absolute Shrinkage and Selection Operator) regression is a technique for

feature selection and regularization in linear regression models. This method reduces some
regression coefficients to zero to reduce the complexity of the model and minimize the risk
of overfitting. Thus, only the most important variables are retained in the model, which
increases its simplicity and interpretability [35]. Lasso regression is a powerful technique
to avoid feature selection and overfitting, especially in high-dimensional data sets. When
the regularization parameter is chosen appropriately, the Lasso regression model yields
simpler, more interpretable, and highly generalizable results [36–38]. Lasso Regression
was selected due to the dataset’s mix of numerical and categorical variables, many of
which might be irrelevant or have weak correlations with the target variable. Its feature
selection capability makes it ideal for reducing the dataset’s dimensionality, focusing on the
most impactful variables. This not only improves model generalization but also prevents
overfitting, ensuring more robust predictions for variables like total daily movement or
meal counts.



Sustainability 2025, 17, 379 7 of 22

2.4.5. Decision Tree Regressor
The Decision Tree (DT) is an efficient algorithm for solving classification and regression

problems. Its basic principle is to break down complex problems into simpler sub-problems,
making the solution easier and more understandable. DT is based on hierarchically orga-
nized rules from root to leaf, and these rules provide the predictive power of the model [28].
DT offers the flexibility to work with both categorical and numerical data, and provides a
better understanding of the results by using if-else rules in the decision-making process.
However, there is a risk of overfitting if the model is subjected to excessive branching;
therefore, the generalizability of the model can be increased through different processes
such as pruning or cross-validation [39]. DT was selected for its ability to handle both
numerical (e.g., “Average Temperature”) and categorical (e.g., “Weekdays”) variables. It
creates interpretable rules, such as predicting “Total Daily Persons” based on meal types
and days. Its flexibility with mixed data types and ability to model complex patterns make
it suitable for this dataset. To prevent overfitting, pruning and cross-validation can enhance
its generalizability.

2.4.6. Extra Tree Regressor
Extra Tree Regressor is part of the Extremely Randomized Trees (Extra Trees) algorithm,

one of the ensemble methods, and is used in regression problems. This model prevents
overlearning and increases generalization ability by applying randomization when building
decision trees. Extra Trees is an extension of the random forest algorithm, splitting nodes
with randomized features and values, and works on the entire training dataset, while
random forest uses a bootstrap replica [40]. Extra Tree Regressor was preferred for its
effectiveness in handling numerical (e.g., “average temperature”) and categorical (e.g.,
“weekdays”) variables in the dataset. Its randomized splits reduce overfitting and enhance
generalization, making it ideal for robust predictions such as “total daily persons.

2.5. Validation Methods
Cross-validation methods were applied to evaluate the performance and generaliza-

tion ability of the models. This technique splits the dataset into training and testing subsets
and evaluates model performance on each subset individually to ensure reliable results.
Different fold counts were used to compare the models’ performance based on metrics such
as R2, Mean Absolute Error (MAE), and Root Mean Square Error (RMSE) [22]. To reduce
data imbalance and the risk of overfitting, the data was randomly selected, and different
training and testing combinations were created in each validation cycle. The validation pro-
cess contributed to a detailed analysis of each algorithm’s performance and improved the
reliability of the proposed methods. This approach aimed to enhance prediction accuracy
and establish a solid foundation for sustainable dining services.

3. Results
3.1. Analysis of Relationships in Campus Dataset Results

As the central tendency and spread of the variables in the dataset, the hourly move-
ment of people entering the campus is given in Figure 1. In this context, the hourly density
analysis on campus will contribute to the planning to be made in areas such as food services,
security needs, development of internet infrastructure, cleaning and maintenance services,
technological infrastructure, transportation and traffic management, academic services,
and social and cultural activities, and will enable optimum service provision and effective
management on campus.



Sustainability 2025, 17, x FOR PEER REVIEW 8 of 24 
 

3. Results 
3.1. Analysis of Relationships in Campus Dataset Results 

As the central tendency and spread of the variables in the dataset, the hourly 
movement of people entering the campus is given in Figure 1. In this context, the hourly 
density analysis on campus will contribute to the planning to be made in areas such as 
food services, security needs, development of internet infrastructure, cleaning and 
maintenance services, technological infrastructure, transportation and traffic 

Sustainability 2025, 17, 379 management, academic services, and social and cultural activities, and will8 oefn2a2ble 
optimum service provision and effective management on campus. 

 
FiFgiugurer e11. .DDaailiyly ccaammppuuss ddeennssiittyy bbyy hhoouurrss.. 

TThhee rreelalattioionnsshhiipp bbeettwweeeenn tthhee ttoottaall nnuummbbeerro of fp peoepolpeleo nonc acmampupsuasn adnddi ndiinnginhga lhl all 
usage according to the daily menu is shown in Figure 2. In the analysis, which was sorted

usage according to the daily menu is shown in Figure 2. In the analysis, which was sorted 
according to the most preferred menu in the dining hall, it was revealed that the use of

acthcoerddiinnign gtoh athlled midonsot tpinrecfreerarseedl imneeanruly ionn tdhaey dsiwnihnegn hthalel,t oitt awl dasa irlyevmeaolveedm tehnatt ptheres ounsse of 
Sustainability 2025, 17, x FOR PEER REVIEW 9 of 24 
 thceo udnint iwnga shhalilg hdeidr. nIot tw inacsrdeaetseer mlinineaerdlyt hoant dthaeysfo wodhemn etnhues toptraiml daariillyy maffoevcetmtheendt ipneinrsgons 

cohuanlltp wreafse rheingchee. r. It was determined that the food menus primarily affect the dining hall 
preference. 

 
FiFgiugruere2 .2M. Menenuup prerefefererenncceessa annaallyssiis based on camppuuss ddeennssitiyty. .

The relationship analysis between dining hall usage and cafeteria usage is shown in 
Figure 3. It has been observed that an increase in the total daily dining count is associated 
with a linear decrease in the average cafeteria revenue. 

 
Figure 3. Relationship between cafeteria revenue and dining hall usage. 

In the analysis, the expected linear increase in dining hall usage was not observed on 
days with high daily mobility. This suggests that the main factor determining dining hall 
preferences is the menus offered rather than the intensity of movement. Menus stood out 



Sustainability 2025, 17, x FOR PEER REVIEW 9 of 24 
 

 
Sustainability 2025, 17, 379 Figure 2. Menu preferences analysis based on campus density. 9 of 22

The relationship analysis between dining hall usage and cafeteria usage is shown in 
Figure T3.h Iet rhealast iboenesnh iopbasnearlvyesids tbheatwt aeenn indcinreinagseh ainll tuhsea gtoetaanl ddcaailfyet edriinaiunsga gcoeuisnsth ios wasnsionciated 
witFhig au rlein3e.aIrt hdaescbreeaenseo ibns etrhvee davthearat gane icnacfreetaesreiain rethveetnoutael. daily dining count is associated

with a linear decrease in the average cafeteria revenue.

 
FigFuirgeu r3e. 3R.eRlaetlaiotinosnhshipip bbeettwweeeenn ccaaffeetteerriaiar erveveneuneuaen adnddi ndiinnginhgal lhuaslla gues.age. 

In the analysis, the expected linear increase in dining hall usage was not observed on
daIyns wthieth ahniaglhysdiasi,l tyhme oebxiplietyc.teTdh ilsinsueagrg einstcsrtehaastet hine dmianiinnfga chtaolrl duestaegrme iwniansg ndoint ionbgshearvlled on 

dapyrse wferitehn cheisgihs tdhaeilmye mnuosboilfifteyre. dThraisth seurgthgaensttsh tehiantt etnhsei tmy oafinm foavcetmore ndte.tMeremnuinsisntgo oddinoiuntg hall 
preafsearefnaccteosr itsh atht sei gmneifincuasn tolyffienrfleude rnactehdesrt uthdaenn ttsh’ ech ionitceens,saitnyd otfh emreofvoerem, menetn.u Ms neeneuds tsotoboed out 

categorized and analyzed in more depth.
The meals served in the university dining hall are prepared daily in four types: two

main courses, a soup, and one additional product. In order to determine the preference
rates within the scope of the research, one menu data including meal types were first
divided into four categories: main course one, main course two, soup, and additional
product. The preference frequencies of the meals within each category were analyzed to
determine which meals were most preferred. The preference rates of 19 different types
of food in the categories of main course one and main course two, which are preferred
depending on daily consumption, are given in Figures 4 and 5.

There are 14 and 12 different options in the soup, and supplement categories offered
in the food menus. Figures 6 and 7 show the graphs of soup preference and supplement
preference rates.

The correlation heatmap, which visually represents the correlations between the vari-
ables in the dataset, is illustrated in Figure 8. Positive Correlations: if there is a red cell, this
indicates that these two variables have a strong positive relationship. Negative Correla-
tions: if there is a dark blue cell in between, this indicates that these two variables have a
strong negative relationship. When the correlation matrix between average temperature,
total daily movement person, cafeteria revenue, and total daily dining count in the cam-
pus dataset is examined, it shows that there is a very weak and negative relationship of



Sustainability 2025, 17, x FOR PEER REVIEW 10 of 24 
 

as a factor that significantly influenced students’ choices, and therefore, menus need to be 
categorized and analyzed in more depth. 

The meals served in the university dining hall are prepared daily in four types: two 
main courses, a soup, and one additional product. In order to determine the preference 
rates within the scope of the research, one menu data including meal types were first 

Sustainability 2025, 17, 379 divided into four categories: main course one, main course two, soup, and additio1n0aolf 22
product. The preference frequencies of the meals within each category were analyzed to 
determine which meals were most preferred. The preference rates of 19 different types of 

−f0o.o0d5  binet wthee ncaatevgeorraigees toefm mpaeirna tcuoruerasen dondea ialyn d imnianign ccoounrst.e Htwowo, ewvehri,cthe marpee prarteuferrerehda s a
stdroenpgenrdelinatgi oons dhaipilyw ciothnstuomtapl tdioanil,y amreo gvivemene innt Fpiegrusroens .4 and 5. 

Sustainability 2025, 17, x FOR PEER REVIEW 11 of 24  
 

FiFgiugruere4 .4G. Grarapphho offp prreeffeerreennccee rrattes for main lluncchh 11. .

 
FiFgiugurere5 5. .G Grraapphh ooff prrefference rates fforr maaiinn lulunncchh 22. .

There are 14 and 12 different options in the soup, and supplement categories offered 
in the food menus. Figures 6 and 7 show the graphs of soup preference and supplement 
preference rates. 

 
Figure 6. Graph of preference rates for soup. 



Sustainability 2025, 17, x FOR PEER REVIEW 11 of 24 
 

 
Figure 5. Graph of preference rates for main lunch 2. 

There are 14 and 12 different options in the soup, and supplement categories offered 
Sustainability 2025, 17, 379 in the food menus. Figures 6 and 7 show the graphs of soup preference and supplem1e1not f 22

preference rates. 

Sustainability 2025, 17, x FOR PEER REVIEW 12 of 24  
 

FiFgiugruere6 .6G. Grarapphho offp prreeffeerreennccee rates for soup.. 

 
FiFgiugurere7 7. .G Grraapphh ooff pprreeffeerreennccee rraatteess ffoorr aaddddiittioionnaal lpprorodduuctcst.s .

FTighuer eco9rrperleasteionnt shtehaetmcoarpre, lwathioicnhg vraispuhalslhyo rwepinrgestehnetsr etlhaet iocnorsrheilpastiobnetsw beeetnwteheen ptharea m-
etvearrsiaibnleths eino rthigei ndaaltadsaett,a sise ti.lluAstsreartieeds ionf Fbiagruaren d8. dPootsiptilvoets Cvoirsruealalitzioings: tihf ethienrtee rias cat iroends of
dcaeillyl, cthaims pinudsicaartreisv athl atn tdhedsep tawrtou vreardiabtale,sa hvaevraeg ae sttermonpge rpaotsuirtiev,ec arefelatetiroinasrheivpe. nNueg,atnivde the
nCumorbrelraotifopnse:o ipf lteheraet iinsg a idnatrhke bdluinei cnegllh inal bl eretwv eaelnr, othwisa indiccoaltuesm tnhactr tohsess-ien ttweroa cvtaiorinasb.leEsa ch
ofhtahvee aan aslytrsoensgp enrefogramtiveed orenlathtieondsahtiaps.e tWhahsenst rtehneg tchoernreldattihoen dmatatsreixt  abnedtwpreoevni daevderaabget ter

temperature, total daily movement person, cafeteria revenue, and total daily dining count 
in the campus dataset is examined, it shows that there is a very weak and negative 
relationship of −0.05 between average temperature and daily dining count. However, 
temperature has a strong relationship with total daily movement person. 

 
Figure 8. Campus dataset correlation heatmap. 



Sustainability 2025, 17, x FOR PEER REVIEW 12 of 24 
 

 
Figure 7. Graph of preference rates for additional products. 

The correlation heatmap, which visually represents the correlations between the 
variables in the dataset, is illustrated in Figure 8. Positive Correlations: if there is a red 
cell, this indicates that these two variables have a strong positive relationship. Negative 
Correlations: if there is a dark blue cell in between, this indicates that these two variables 

Sustainability 2025, 17, 3h79ave a strong negative relationship. When the correlation matrix between average 12 of 22
temperature, total daily movement person, cafeteria revenue, and total daily dining count 
in the campus dataset is examined, it shows that there is a very weak and negative 
relationship uofn −d0e.0r5s tbaentdwienegn oavfetrhaeged tiefmfeprernatudrey nanadm dicasilyo nditnhineg Scuoluenyt.m HaonwDeveemr, irel University campus,
temperature shuasp ap sotrrtoinngg rfeulattuiorneshpilpa nwnitihn tgo.tal daily movement person. 

Sustainability 2025, 17, x FOR PEER REVIEW 13 of 24 
 

Figure 9 presents the correlation graph showing the relationships between the 
parameters in the original dataset. A series of bar and dot plots visualizing the interactions 
of daily campus arrival and departure data, average temperature, cafeteria revenue, and 
the number of people eating in the dining hall reveal row and column cross-interactions. 
Each of the analyses performed on the dataset has strengthened the dataset and provided 
a better understanding of the different dynamics on th e Suleyman Demirel University 

Figure 8. CamFpuicgsa udmraetpa8sue.stC ,c oasrumrpeplpautoisorndt iahntegas tfmeutatcpuo. rrer eplalatinoninhega. tmap.

 
FiFgiugruere9 .9C. Camamppuussd daattaasseett ccorrrellattiion mattriix.. 

3.2. Predictive Performance via Regression Analysis: Machine Learning Results 
Changing food demand on campuses due to student and staff density necessitates 

effective meal planning. The variety of meals served in dining halls has a direct impact on 
this demand and is important for balancing and optimizing demand. Adjusting the 
number of meals according to the campus density is essential for preventing waste and 
efficient use of resources. Preventing food waste not only reduces costs but also 
contributes to environmental sustainability. Therefore, it is of strategic importance to 
accurately forecast demand and develop early solutions. 

Models were developed using various machine learning regression algorithms to 
predict the number of meals needed per day in the campus cafeteria. The dataset was 



Sustainability 2025, 17, 379 13 of 22

3.2. Predictive Performance via Regression Analysis: Machine Learning Results
Changing food demand on campuses due to student and staff density necessitates

effective meal planning. The variety of meals served in dining halls has a direct impact on
this demand and is important for balancing and optimizing demand. Adjusting the number
of meals according to the campus density is essential for preventing waste and efficient
use of resources. Preventing food waste not only reduces costs but also contributes to
environmental sustainability. Therefore, it is of strategic importance to accurately forecast
demand and develop early solutions.

Models were developed using various machine learning regression algorithms to
predict the number of meals needed per day in the campus cafeteria. The dataset was
expanded with analysis and preprocessing to predict the number of people who will eat on
a given day. The dataset includes meal types such as main course one, main course two,
soup, and additional products, as well as variables such as air temperature, the number of
staff and students eating, the number of people entering the university, other demographic
information that is important in determining the density on campus, and canteen turnover.
This rich dataset was a valuable resource for forecasting food demand. In the first stage,
missing data completion, outlier identification, and data cleaning were performed on the
collected data. Then, prediction models were created using different regression algorithms
such as Linear Regression, Extra Tree Regressor, Lasso, Decision Tree Regressor, XGB
Regressor, and Gradient Boosting Regressor. To evaluate the performance of the models,
the dataset was split into two parts, 80% training and 20% testing, to test the prediction
accuracy and generalization ability of the model. The performances of these models were
evaluated by cross-validation methods, and the model with the highest prediction accuracy
was identified. As a result, this study aimed to improve operational efficiency by more
accurately forecasting the daily food demand on campus.

Table 2 presents the R2, RMSE, and MAE values for the regression algorithms com-
pared. The Lasso algorithm achieved the highest accuracy with an R2 value of 0.999.
This success is attributed to its regularization capability, which prevents overfitting by
penalizing less significant features. Its low RMSE (1.891) and MAE (1.228) values further
emphasize its superior predictive performance. In contrast, Linear Regression demon-
strated poor performance due to its inability to handle multicollinearity and irrelevant
features. Decision Tree and Extra Tree algorithms showed moderate performance, likely
due to their sensitivity to noise and overfitting in smaller datasets. Ensemble methods
such as XGBoost performed better than Linear Regression but fell short of Lasso. Gradient
Boosting Regressor struggled to effectively capture data relationships, as reflected in its low
R2 value. In summary, Lasso’s ability to focus on the most important features underpins
its superior accuracy, while the limitations of other models in addressing multicollinearity
and feature selection contributed to their lower performance.

The primary factor enabling Lasso to outperform other models is its feature selection
and regularization mechanism. This approach reduces the complexity of the model, pre-
venting overfitting while ensuring that only the most relevant variables are included. For
instance, features such as “average temperature” exhibited strong coefficients, playing a
decisive role in predicting the target variable, “total daily persons.” Lasso’s simplicity and
compatibility with medium-sized datasets further distinguish it from the other models.



Sustainability 2025, 17, x FOR PEER REVIEW 15 of 24 
 

Sustainability 2025, 17, 379 14 of 22

high error rates. Gradient Boosting Regressor and Linear Regression, with their low R2 
Table 2. Regression algorithm results.
values, failed to effectively model the relationships within the dataset. This analysis 
highlightsA tlhgeo erffitehcmtisveness of LassRo_ wSQhiUleA sRugEgDesting thaRt MalgSoErithms like XGMBAooEst could 
achieve betteLr arsessoults with optimized h0y.9p9e9rparameters. F1u.8rt9h1ermore, it emp1h.2a2s8izes that 
simpler models may not be suitable when the dataset exhibits complexity, underscoring 

XGBoost Regressor 0.882 547.236 369.643
the importance of aligning model choice with dataset characteristics. 

DAeccicsuioranteT rfeoerReceagsrteinssgo rof food con0s.u7m65ption or actu7a7l 3d.8e5m0and in unive5r9s2it.y5 dining 
halls EsxigtrnaifiTcraenetRlye gimrespsaocrts controlling0 .f6o7o2d waste and 9o1p4.t8im30izing resourc7e8 8a.l2l5ocation. 
AGftreard tireanitnBinogo stthine gdRateagsreets, stohre develop0e.5d4 9models were1 t0e7s2t.e4d2 8with real da7t6a5,. 7a4n5d their 
performLiannecaer wReagsr eevssailounated. Figures 100. 3a6n3d 11 compar1e2 t7h5e. 2r9e3al and pred9ic1t0e.d6 4d1ata for 
each model, with Figure 10 illustrating performance based on the R2 parameter and Figure 
11 using the RMSE parameter. These graphical results align with the accuracy metrics 
presIenntceodm inp aTraibsolen 2, .X GBoost Regressor achieved a high R2 value of 0.882 but lagged
behinFdigLuarses o1d0 uheigtohlhigighhtse rtRheM pSEreadnicdtiMveA aEccvuarluaceys . oDf etshpeit emitosdaeblsil iatycrtoossm dodiffeelrceonmt pdlaetxa 
rpeolaintitosn. sThhiep Ls,aXssGo Bmooodsteld didemnoontsdtreamteosn as ntreaatre-psuerpfeecrito mriatytchin btehtwisedeant aacsteut.alD anecdi spiroendiTcrteeed 
avnadluEexs,t reavTidreeentR fergormes siotsr scodnisspisltaeynetdlyl ihmigithe dRgeneralization capabilities, as evidenced by

2 values across data points. In contrast, the 
their high error rates. Gradient Boosting Regressor and Linear Regression, with their low
Linear Regression model shows significant deviations, reflecting its poor ability to handle 
R2 values, failed to effectively model the relationships within the dataset. This analysis
data variability and multicollinearity. The Decision Tree Regressor and Extra Tree 
highlights the effectiveness of Lasso while suggesting that algorithms like XGBoost could
Regressor models exhibit moderate performance, with occasional fluctuations in 
achieve better results with optimized hyperparameters. Furthermore, it emphasizes that
accuracy, indicating sensitivity to noise and overfitting. 
simpler models may not be suitable when the dataset exhibits complexity, underscoring

Figure 11 focuses on RMSE values, measuring the average magnitude of error in the 
the importance of aligning model choice with dataset characteristics.
predictions. The Lasso model achieves the lowest RMSE values across the dataset, 

Accurate forecasting of food consumption or actual demand in university dining
confirming its ability to make precise predictions. On the other hand, models like Gradient 
halls significantly impacts controlling food waste and optimizing resource allocation. After
Boosting Regressor and Linear Regression display higher RMSE values, suggesting 
training the dataset, the developed models were tested with real data, and their performance
difficulties in capturing complex patterns. These results validate the Lasso model’s 

was evaluated. Figures 10 and 11 compare the real and predicted data for each model,
superiority in demand forecasting and highlight the limitations of other models in 

with Figure 10 illustrating performance based on the R2 parameter and Figure 11 using
handling noisy or complex data, emphasizing the need for careful algorithm selection to 
the RMSE parameter. These graphical results align with the accuracy metrics presented in
minimize food waste and improve sustainability. 

Table 2.

 
FFiigguurree1 100.. PPrreeddiicctteedda anndda accttuuaallv vaalluueesso offt thheeR R22 parrameetteerr.. 



Sustainability 2025, 17, x FOR PEER REVIEW 16 of 24 
S ustainability 2025, 17, 379 15 of 22

 
FFiigguurree1 111.. PPrreeddiicctteedda anndda accttuuaallv vaalulueesso offt thheeR RMMSSEEp paarraammeeteter.r. 

FIing uthreis1 s0tuhdigyh, ltihgeh tdsatthaeseptr ewdaicst divieviadcecdu rianctyo otrfatihneinmgo adnedls taecsrto ssestsd iwffietrhe nat rdaatitoa pofo i8n0t%s.  
TahnedL 2a0s%so, mreosdpeelcdtievmeloyn. sCtrraotsess-vaanliedaart-ipoenr feisc tumtialitzcehdb aetsw ae ekneya ctteucahlnainqduep rteod iecvteadluvaatelu tehse,  
evident from its consistently high R2
overall performance of the models. Thvisa mlueetshoacdr oiss aspdpaltiaedp tooi natsss.esIsn hcoownt wraesltl, etahcehL minoedaerl 
Rgeegnreersasliioznesm thode edl ashtao wwsitshiogunti fiecnacnotudnetveiraintigo niss,srueeflse clitkineg oivtserpfiottoirnagb iolirt yutnodhearfinttdilnegd. aBtay 
vsaprliiattbinilgit ythaen ddamtausletti cionltloin deaiffrietrye.nTt hseubDseectiss, iocrnoTssr-eveaRlidegartieosnso ernaanbdleEs xttersatiTnrge ethRee mgroedsseolsr’ 
macocduerlasceyx ahcibroitsms tohdeesrea ptearpteitrifoonrsm aanndc ep,rwovitihdoesc craesliioabnlael iflnuscigtuhatsti oinntso itnhaecirc ueffraeccyt,ivinedniecsast.i ng
sensitFivigituyreto 1n2o idseepanicdtso vtheerfi vttainriga.tion in machine learning model performance across 
diffeFreignut rcero1s1s-fvoacluidseastioonn fRolMd ScEouvnatlsu, eras,ngmineags furroimng 5 tthoe 1a0v. eTrhaeg Leamssaog mniotuddele coofnesirsrtoerntinly 
tdheemporendstircatitoends t.hTe hbeesLt apsesrofomrmodanelcea cahcireovses saltlh vealloidwaetisotnR fMolSdEs, vsatalunedsinagc roousts wthitehd itast ahsiegth,  
cgoennfierrmaliinzgatiitosna bcilaitpyactoitym aaknedp rleocwise pterneddeicntcioyn sf.oOr notvheerofittthienrgh. anInd , cmoondtrealsstl,i ktehGe raLdinieenatr 
BRoeogsrteinsgsioRne gmreosdsoelr eaxnhdibLiitneeda trhRee pgoreosrseisotn pdeirsfpolramyahnigceh,e wr RitMh lSiEmvitaeldu egse,nseurgagliezsatitniognd aifbfiicliutyl-. 
tDieesciinsiocanp Tturerein agndco Emxptrlae xTrpeaet tmerondse.lsT hsheosewreeds ufllutsctvuaaltiidnagt epethrfeoLrmasasnocme, opdaertli’csusluaprleyr iporroitnye 
itno doevmearfinttdifnogr eocans tsimngalalnerd dhaigtahsleigtsh. t XthGeBliomositta tainodn sGorfaodthieenrt mBoodoesltsinign hmaonddelilns gdneoliivsyeroerd 
cmomodpelerxatde atpae, refmorpmhaasniczein gbuthte wneeerde fosrencasriteifvuel atlog orhityhpmerspealeracmtioentetro mtuinniimngiz. eTfohoisd wgraaspteh 
ahnidghimligphrtosv tehseu ismtapinoartbainlictye. of cross-validation as a tool for evaluating the generalization 
abiliItny tohfi smsotuddelys, tahnedd eamtapsehtawsizaessd tihveid nedeeidn ttoo tcraoinnsiindgera nbdotthe sctosnestisstwenitchy aarnadti oacocfu8r0a%cy 
awnhde2n0 s%el,ercetisnpge cthtiev ebleys.t mCroodsesl-.v alidation is utilized as a key technique to evaluate the
overall performance of the models. This method is applied to assess how well each
model generalizes the data without encountering issues like overfitting or underfitting.
By splitting the dataset into different subsets, cross-validation enables testing the models’
accuracy across these partitions and provides reliable insights into their effectiveness.

Figure 12 depicts the variation in machine learning model performance across dif-
ferent cross-validation fold counts, ranging from 5 to 10. The Lasso model consistently
demonstrated the best performance across all validation folds, standing out with its high
generalization capacity and low tendency for overfitting. In contrast, the Linear Regression
model exhibited the poorest performance, with limited generalization ability. Decision Tree
and Extra Tree models showed fluctuating performance, particularly prone to overfitting on
smaller datasets. XGBoost and Gradient Boosting models delivered moderate performance
but were sensitive to hyperparameter tuning. This graph highlights the importance of
cross-validation as a tool for evaluating the generalization ability of models and emphasizes
the need to consider both consistency and accuracy when selecting the best model.



Sustainability 2025, 17, x FOR PEER REVIEW 17 of 24 
 

Sustainability 2025, 17, 379 16 of 22

Figure 12. Change in model performance by cross-validation split count.  
Figure 12. Change in model performance by cross-validation split count. 

Figure 13 highlights the changes in the average R2 scores of the models and demon-
stratesFtihgeuirrec o1n3s ihstiegnhclyigihntsp etrhfoer mchaanncge.esT hien Ltahseso amveordaeglec oRn2s isstceonrtelys aocfh itehvee smthoedheilgs haenstd 
and most stable R2
demonstrates theirs ccoonressisatcernocsys ianl lpfeorlfdosr,mshaonwcec. aTshineg Liatssssot rmonogdegle cnoenrsailsizteantitolyn aacbhiileitvyeasn thde 

ehffiegchtievsetn aensds  inmhoastn dstlainbgleo Rve2 rsfictotirnegs .aTchroisssg raalpl hfoelmdsp, hsahsoiwzecsatshinatgL iatss ssotriosnthge gmenoesrtarleilziaatbiloen 
maobdilietlyf aonr dth eiffs edcatitvaesentesasn idn hhiagnhdlilginhgts otvheerfintteeindgf. oTrhiims gprraopvhe memenpthsaisniztehse thgeant eLraaslsizoa itsi othne 
cmapoasbt ilrietileiasbolef motohderel mfoord tehlsis.  dFaigtausreet 1a2nde mhipghhalisgizhetss tchoen sniseteedn cfyo,r wimhpilreoFviegmuerent1s 3inp rtoh-e 
vgideenseraaclilzeaatrieornd ecpapicatbioilnitoiefsd iofff eorethnecer sminomdeolds.e lFpigeurfroer m12a necme pfohrasspizeecsi ficcocnrsoissste-vnaclyid, awtihoinle 
sFpilgitucroeu 1n3t sp.rWovhideens uas ecdleatoregre tdheepr,ictthioeny ooff fedriffaemreonrceesc oinm mproedheeln psievrefoarnmaalynscies foofr osvpeercaifillc 
mcroodsesl-vpaelrifdoartmioann scpe.lit counts. When used together, they offer a more comprehensive anal-
ysis Voafr oiavbeirlaitlyl minofdoeold pdeermfoarmndandcuee. to student and staff density necessitates effective food

planning on campuses. The variety of meals served in dining halls is critical for balancing
and optimizing demand, preventing waste and ensuring efficient use of resources. Accurate
forecasting of demand ensures that student and staff needs are met, while monitoring
catering services contributes to optimizing labor costs and capacity planning. In this
study, the menus that have the greatest impact on consumption were identified, and the
impact of each dish on demand was analyzed in detail by dividing them into different
categories. Demand forecasting models created using various machine learning methods
were enriched with menu data, and as a result, the most successful model was identified.

The integration of machine learning models to balance food production and demand
has achieved a significant improvement by reducing food waste to 28%. This result indicates
that on a campus producing 1000 portions of food daily, only 280 portions are wasted, while
the remaining 720 portions are effectively consumed. This reduction not only decreases the
carbon footprint from an environmental sustainability perspective but also enhances cost
efficiency. The implementation of the model establishes a strategic foundation for resource
optimization in dining services by preventing unnecessary production. This highlights that



Sustainability 2025, 17, 379 17 of 22

Sustainability 2025, 17, x FOR PEER REVIEW 18 of 24 
 while waste cannot be entirely eliminated, it can be significantly reduced by improving

current operations.

 
FiFgiugruere1 31.3.M Mooddeellp peerrffoorrmaanncceess ffoorr ddiiffffeerreenntt ccrroossss-v-vaalildidataitoino nspslpitl ictocuonutns.t s.

CVamaripaubsilaitdym inin fiostorda tdoresmcaannde fdfeucet itvoe lsytuudtielnizte aenxdis tsitnagff rdeaenl-stiimty endeacteass(iet.agt.e,st eemffepcetriavteu re,
dfaoiloyd epnltarnyncinogu notns ,csatmudpuensetsa. nTdhes tvaaffrideteyn soift ym)etaolsi mseprlveemd einnt dthineinmg ohdaellls pirso cproitsiceadl ifnort he
arbtaiclalen.cCinogn saindder ionpgtitmhaizticnagm dpeums adnadta, aptrSevuelenytimnga nwDaesmte iraenl dU neinvseurrsiintyg iseffialcreieandty urseeg uolaf rly
corellseocutercdesa.n Adccaucrcaetses ifbolrectahsrtoinugg ohf adneminatnedrf aecnesuinresr etahla-t ismtued, eint eagnrda tsitnagff tneemedpse araretu mreeta, nd
mwenhuilei nmfoornmitaotriionng frcoatmerwinegb sseerrvvicicees scaolnotnrgibwutietsh tdoa iolypteimntirzyin-egx iltarbeocro rcdostas llaonwds cfaopratchietyu se
ofpaladnneminga.n Idn ftohriesc satsutdinyg, tmheo dmeeln. uTsh rthoautg hatvhei sthine tgergeraatteisotn i,mapdamcti noins tcroantosrusmcpantioanc cwuerraet ely
pridedenictitfideadi,l yanfdo otdhed iempaancdt oafn edacphl adnisfho odn pdreomdauncdti ownasa cacnoarldyiznegdl yin.  Addetdaiilt iboyn adlilvy,idiungri ng
sptheecimal ionctoc adsiiffoenrsensut cchateagsournieisv.e Drseimtyaenvde fnotrseocarsetxinagm mdoadyesl,s tchreeyatceadn umsinogn ivtoarrioduesm manacdhsinpeik es
inleraeranlintigm meeatnhoddosp wtiemreiz eensreicrhveidce wcaitpha mcietyn.uT dhaitsa,a panpdro aasc ha areimsusltt, otheen hmaonsct esuocpceersastfiuoln al
efmficoideenlc wy aws hidileenstiigfinedifi. cantly reducing food waste.

TThheefi inndteignrgastisohno owf mthaacthninoet loenarlynifnogo md ocdouelns ttofo braelcaansctes faoroeds upcrocedsuscftuiol,nb auntda ldseomthanatdt he
efhfiacsi eancchyieovfeddi nai nsgighnaifillcsaenrtv iimcepsrcoavnembeenint cbreya sreedduicfitnhge mfooedn uws aasrteeo tpot i2m8i%ze. dThcoisr rreecstulyl.t 

indiTcahteese xthpaetr iomn ean ctaalmrpesuusl tpsroadreuacisnfgo l1l0o0w0 sp: ortions of food daily, only 280 portions are 
wasted, while the remaining 720 portions are effectively consumed. This reduction not 

1.onlyT dheectrreaaisneisn tghsea cmarpbloeni sfosoutfpfirciinetn ftroanmd atnh eenpvrierdoincmtioenntaacl csuursataciyniasbsiliigtyn ipfiecrasnptelyctiivmep bruotv ed
alsow einthhatnhceesr ecgorsets seiffionciaelngcoyr. itThhme si;mplementation of the model establishes a strategic 

2.founIdt aistiodnif fifcour ltretsooeusrtciem oaptetimthiezatrtiuoen vianl udeinoifntgh esedrivnicinesg hbyal lpcroenvseuntminpgt iounnndeacteas,saarnyd it
prodisucftoiuonn.d Tthhiast hthigehilimghptrse sthsiavte wnehsisleo wf tahsetem caennnuost isbeh iegnhteirrelwy heelnimtihneatteodt,a litn cuamn bbeer of
signcifiocnasnutmlye rresdiuscteadk ebny iinmtporaocvcionugn ctu;rrent operations. 

3. ICt aismapnusi nnaodvmaitniivsetraidtoeras thcaant  coenffseuctmiveerlys huatvileizteh eepxiosttienngt iarletaol-toimrgea ndizaetam e(en.gu.s, in
tempaedrvaatunrce, bdyaidlye t ernmtriyn icnogutnhtse, psrteufdeerennt caenrda testsaofff fdoeondsity)p etos oinmcpalemmpeunst. the model 
propTohseedim inp athcte oafrttihclee.e Cxpoenrsiimdeernintagl trheastu clatsmispuass dfoaltlao wat sS:uleyman Demirel University is 
already regularly collected and accessible through an interface in real-time, integrating 
temperature and menu information from web services along with daily entry-exit records 



Sustainability 2025, 17, 379 18 of 22

1. Additional staff can be assigned to increase service speed and reduce customer waiting
times on peak food consumption days;

2. Additional staff can be included and additional products can be offered on days when
cafeteria usage is expected to increase;

3. By determining the preference rates and variety of food options on the menus, cam-
pus density can be monitored, and menus can be tailored according to the days of
the week.

4. Discussion
In a study, researchers developed a demand forecasting model for a university dining

hall, taking into account the calendar effect and turnstile passage data, and examined
eighteen Machine Learning models collected under five main techniques. They tested the
diversity of methods with three Artificial Neural Network models, four Gaussian Process
Regression models, six Support Vector Regression models, three Regression Tree models,
two Ensemble Decision Tree (EDT) models, and one Linear Regression model. The EDT
Boosted model achieved the best prediction performance (MSE = 0.51, MAE = 0.50, and
R = 0.96) [22]. Another study analyzed plate shape and size as a physical factor in reducing
waste based on the number of meals predicted by machine learning algorithms and found
that the use of oval plates was effective in reducing waste significantly [20]. In addition,
predictions were made using food tracking data to ensure that food is preserved during
storage. The Random Forest Optimizer method was used to predict the freshness of the
food in the storage area, and the best result was obtained with an accuracy of 94.01% [15].
In a study on food waste planning, ANN was used to develop a prediction, taking into
account the number of reservations, but not the number of cancellations. This situation
created uncertainty between reality and prediction [41].

In the food industry, machine learning-based demand forecasting models have been
used to manage the supply chain more effectively. In studies using LSTM and SVM
algorithms, the success of LSTM forecasts was determined as a result of the comparison
of MAE and MAPE values [42–45]. In this study, regression models are preferred because
time series models require a lot of data and long training time. Regression models offer
simplicity, speed, and interpretability, enabling fast predictions with small data sets. Their
low computational cost and clear outputs benefit decision-makers.

Machine learning regression algorithms have been used in food supply chain
processes [17,30]. In this study, in addition to the features in the literature, different
features were added to the dataset created for on-campus density analysis and food de-
mand forecasting by tracking food consumption operations. While it was predicted that
the number of people entering the campus and the number of foods consumed would be
linear, with the features added to the dataset, it was determined that the biggest factor in
the number of foods actually consumed is the foods included in the menu. The effect of
the percentages of the preferred foods on the results was seen by dividing the foods into
4 categories in the menus. In addition, the effect of the data of the cafeteria selling snack
foods on the campus was also evaluated. The results of the successful model developed
with ML regression algorithms based on the campus dataset were evaluated with RMSE,
MAE, and R2 parameters in predicting the number of food demands, and the R2 coefficient
ranged from 0.99 (Lasso) to 0.36 (Linear Regression). It was seen that the Lasso algorithm
created the most successful model due to its ability to perform effective feature selection
and regularization, reducing model complexity and preventing overfitting, which ensures
the inclusion of only the most relevant variables in predictions.

Compared to the studies in the literature, they have addressed food waste in universi-
ties and used data such as reservation, plate shape, behavioral impact, and turnstile entry



Sustainability 2025, 17, 379 19 of 22

only, but there has not been a comprehensive study on demand forecasting based on the
number of meals consumed in the cafeteria, meal types, and food types by tracking on-
campus mobility. There is a research gap in the context of on-campus process management
where meal counts are influential. Therefore, one of the main contributions of the current
study is to fill this gap by creating a comprehensive dataset that includes campus density,
temperature, other canteen data, and menus that affect meal counts, and detailed analysis
for university management.

Moreover, recent studies underline the importance of sustainability and food waste
reduction. Zhang and Kwon (2022) demonstrated that implementing trayless dining
significantly reduces food waste while positively affecting diner satisfaction and food
selection behaviour [21]. Additionally, Martin-Rios et al. (2020) highlighted the role
of sustainability-oriented innovations in food waste management technology, aligning
with circular economy principles [11]. Building on these insights, the proposed model
contributes by effectively balancing production and demand, reducing food waste by up to
28%. This approach minimizes unnecessary production, optimizes resource allocation, and
supports sustainable practices in campus dining services.

In addition to the aspects examined in previous studies for demand forecasting, in the
proposed model, in addition to meal counts, other canteen consumption data on campus
and preference rates of menus that affect demand are also taken into account. The current
research used current on-campus data to estimate the volume of available meals. The
novelty of this study is that it analyzes on-campus density, daily temperature, canteen data,
days of the week, and daily dining hall attendance rates, and provides a high-performing
model with the segmentation of menus that is unprecedented in previous research. During
periods of increased demand, such as exam days or university events, the proposed model
leverages real-time input data and historical demand trends to more accurately analyze
demand dynamics. This allows managers to anticipate demand surges, include popular
meal options in the menu, and effectively optimize production planning. The unique
contribution of this study lies in the integration of menu-related variables into predictive
models, which significantly contributes to operational processes such as reducing food
waste, improving resource management, enhancing student satisfaction, and optimizing
menu planning.

The proposed model has managed to create a remarkable potential to improve the
overall service quality and efficiency within the scope of managerial operations of the men-
tioned university, such as food waste reduction, resource management, student satisfaction,
menu planning, canteen improvement. The proposed solution is not limited to a meal
count prediction model but is capable of designing and solving different objectives with
different input data in any campus area.

Limitations and Further Research
The demand forecasting model developed in this study holds significant potential to

improve operational efficiency and reduce food waste in campus dining services. How-
ever, limitations such as the lack of long-term data and cultural differences between cam-
puses constrain the model’s generalizability. Future research could address these limita-
tions by testing the model in different universities and regional contexts. Additionally,
long-term pilot implementations could provide more comprehensive evaluations of the
model’s sustainability.

Integrating real-time data can enhance prediction accuracy and enable menu optimiza-
tion based on daily demand. At Suleyman Demirel University, the existing data system
already facilitates access to temperature, menu, and entry-exit records through an interface.
This integration allows administrators to accurately predict demand and optimize service



Sustainability 2025, 17, 379 20 of 22

capacity during special occasions such as events or exam days. Consequently, operational
efficiency can be improved while significantly reducing food waste. The model is not only a
tool for predicting meal demand but also a strategic asset for resource management, menu
planning, and improving student satisfaction.

Future research could enhance the versatility and real-world applicability of the
proposed demand forecasting model by integrating factors such as cultural preferences,
multi-campus comparisons, and cost-related impacts. Investigating the role of religious
and national holidays, alongside variations in meal preferences across regions, could offer
valuable insights. By incorporating these elements, the model could better account for re-
gional and cultural dynamics in demand prediction and menu customization. Furthermore,
analyzing the model’s performance across multiple campuses could highlight its robustness
and adaptability, while addressing cost considerations would enhance its practicality in
resource distribution and operational planning.

5. Conclusions
Effective planning and management of campus food services are critical to reducing

food waste and improving service quality. This study utilized machine learning algorithms
to forecast food demand based on campus density, dining hall entries, and menu prefer-
ences. The Lasso algorithm outperformed others with an R2 value of 0.99, enabling accurate
demand predictions and better alignment of production with consumption needs. The
unique contribution of this study lies in the integration of menu-related variables into
predictive models. Results showed that food consumption is influenced more by menu
design than campus density, emphasizing the importance of optimizing menu offerings
to meet preferences. This study incorporates not only meal counts but also other canteen
consumption data and preference rates of menus, enabling a more accurate modeling of
demand. During periods of increased demand, such as exam days or university events,
the model effectively used real-time input data and historical demand trends to better
analyze demand dynamics. In addition to enhancing service quality, the forecasting models
significantly minimized food waste by preventing overproduction and reducing resource
wastage. By balancing production with demand, this model significantly reduced food
waste to 28%. The study highlights its contribution to reducing food waste by simulta-
neously lowering operational costs and supporting environmental sustainability goals.
Dynamic and responsive predictions enabled by real-time data integration made campus
food services more adaptable to changing demands. Future research should enhance the
generalizability of the proposed demand forecasting model by incorporating variables
such as cultural preferences, multi-campus analyses, and cost implications. Examining the
impact of religious and national holidays, regional meal preferences, and menu segmenta-
tion could provide valuable insights. Expanding the model to multi-campus systems and
exploring cost-related variables would further improve its adaptability and effectiveness.
This study underscores the value of data-driven approaches in achieving sustainable and
efficient food service operations, providing a solid foundation for innovative strategies in
higher education.

Funding: This research received no external funding.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: The raw data supporting the conclusions of this article will be made
available by the authors on request.



Sustainability 2025, 17, 379 21 of 22

Acknowledgments: The author thanks Suleyman Demirel University for their valuable support in
providing access to the data and resources that significantly contributed to this research.

Conflicts of Interest: The authors declare no conflicts of interest.

References
1. Villegas-Ch, W.; Palacios-Pacheco, X.; Luján-Mora, S. Application of a smart city model to a traditional university campus with a

big data architecture: A sustainable smart campus. Sustainability 2019, 11, 2857. [CrossRef]
2. Gulluce, A.C.; Yilmaz, T.; Kaygin, E. Factors affecting the university preferences of students: A case of Kafkas University. Am. J.

Ind. Bus. Manag. 2016, 6, 357–372. [CrossRef]
3. Kambli, A.; Sinha, A.A.; Srinivas, S. Improving campus dining operations using capacity and queue management: A simulation-

based case study. J. Hosp. Tour. Manag. 2020, 43, 62–70. [CrossRef]
4. Garg, A.; Kumar, J. Exploring customer satisfaction with university cafeteria food services. An empirical study of Temptation

Restaurant at Taylor’s University, Malaysia. Eur. J. Tour. Hosp. Recreat. 2017, 8, 96–106. [CrossRef]
5. Liang, X.; Zhang, S. Investigation of customer satisfaction in student food service: An example of student cafeteria in NHH. Int. J.

Qual. Serv. Sci. 2009, 1, 113–124. [CrossRef]
6. Kuleto, V.; Ilić, M.; Dumangiu, M.; Ranković, M.; Martins, O.M.; Păun, D.; Mihoreanu, L. Exploring opportunities and challenges

of artificial intelligence and machine learning in higher education institutions. Sustainability 2021, 13, 10424. [CrossRef]
7. Kumar, I.; Rawat, J.; Mohd, N.; Husain, S. Opportunities of artificial intelligence and machine learning in the food industry. J.

Food Qual. 2021, 2021, 4535567. [CrossRef]
8. Yang, C.; Wen, H.; Jiang, D.; Xu, L.; Hong, S. Analysis of college students’ canteen consumption by broad learning clustering: A

case study in Guangdong Province, China. PLoS ONE 2022, 17, e0276006. [CrossRef]
9. Lorenzoni, V.; Triulzi, I.; Martinucci, I.; Toncelli, L.; Natilli, M.; Barale, R.; Turchetti, G. Understanding eating choices among

university students: A study using data from cafeteria cashiers’ transactions. Health Policy 2021, 125, 665–673. [CrossRef]
10. Jiao, F.; Huang, T. Analysis and forecast of college student canteen consumption based on TL-LSTM. J. Data Inf. Manag. 2024, 6,

173–184. [CrossRef]
11. Martin-Rios, C.; Hofmann, A.; Mackenzie, N. Sustainability-oriented innovations in food waste management technology.

Sustainability 2020, 13, 210. [CrossRef]
12. Raman, S.; Chinniah, S. An investigation on higher learning students satisfaction on food services at university cafeteria. J. Res.

Commer. IT Manag. 2011, 1, 12–16.
13. Aigbedo, H.; Parameswaran, R. Importance-performance analysis for improving quality of campus food service. Int. J. Qual.

Reliab. Manag. 2004, 21, 876–896. [CrossRef]
14. Serhan, M.; Serhan, C. The impact of food service attributes on customer satisfaction in a rural university campus environment.

Int. J. Food Sci. 2019, 1, 2154548. [CrossRef]
15. Ahmed, M.M.; Hassanien, A.E. An Approach to Optimizing Food Quality Prediction Throughout Machine Learning. In Artificial

Intelligence: A Real Opportunity in the Food Industry; Springer International Publishing: Cham, Switzerland, 2022; pp. 141–153.
[CrossRef]

16. Vasudha, M.; Rashmi, D.; Mahalakshmi Jain, B.A. Food Recognition and Calorie Measurement Using Machine Learning. In
International Conference on Computer & Communication Technologies; Springer Nature: Singapore, 2023; pp. 9–17. [CrossRef]

17. Rodrigues, M.; Miguéis, V.; Freitas, S.; Machado, T. Machine learning models for short-term demand forecasting in food catering
services: A solution to reduce food waste. J. Clean. Prod. 2024, 435, 140265. [CrossRef]

18. Demirel, A.N.S.; Sema, T.U.R.K. Organic Product Awareness and Healthy Life Preferences of Iğdır University Students: Investiga-
tion with Machine Learning and AHP Analysis. ISPEC J. Agric. Sci. 2024, 8, 409–421. [CrossRef]

19. Rahman, A. Assessing Student Satisfaction and Improving Efficiency: A Study on University Cafeteria. Am. J. Health Educ. 2024,
55, 208–219. [CrossRef]

20. Richardson, R.; Prescott, M.P.; Ellison, B. Impact of plate shape and size on individual food waste in a university dining hall.
Resour. Conserv. Recycl. 2021, 168, 105293. [CrossRef]

21. Zhang, W.; Kwon, J. The Impact of Trayless Dining Implementation on University Diners’ Satisfaction, Food Selection, Consump-
tion, and Waste Behaviors. Sustainability 2022, 14, 16669. [CrossRef]

22. Aci, M.; Yergök, D. Demand Forecasting for Food Production Using Machine Learning Algorithms: A Case Study of University
Refectory. Teh. Vjesn. 2023, 30, 1683–1691. [CrossRef]

23. El-Said, O.A.; Fathy, E.A. Assessing university students’ satisfaction with on-campus cafeteria services. Tour. Manag. Perspect.
2015, 16, 318–324. [CrossRef]

24. Lugosi, P. Campus foodservice experiences and student wellbeing: An integrative review for design and service interventions.
Int. J. Hosp. Manag. 2019, 83, 229–235. [CrossRef]



Sustainability 2025, 17, 379 22 of 22

25. Nanu, L.; Rahman, I.; Traynor, M.; Cain, L. Something to chew on: Assessing what students want from campus dining services.
Young Consumers 2024, 25, 748–770. [CrossRef]

26. Oliveira, L.; BinMowyna, M.N.; Alasqah, I.; Zandonadi, R.P.; Teixeira-Lemos, E.; Chaves, C.; Raposo, A. A Pilot Study on Dietary
Choices at Universities: Vending Machines, Canteens, and Lunch from Home. Nutrients 2024, 16, 1722. [CrossRef]

27. Sakai, Y.; Rahayu, Y.Y.S.; Araki, T. Nutritional value of canteen menus and dietary habits and intakes of university students in
Indonesia. Nutrients 2022, 14, 1911. [CrossRef]

28. Ahmad, M.W.; Reynolds, J.; Rezgui, Y. Predictive modelling for solar thermal energy systems: A comparison of support vector
regression, random forest, extra trees and regression trees. J. Clean. Prod. 2018, 203, 810–821. [CrossRef]

29. Sudhamathi, T.; Perumal, K. Endsemble Regression Based Extra Tree Regressor for Hybrid Crop Yield Prediction System. Meas.
Sens. 2024, 35, 101277. [CrossRef]

30. Panda, S.K.; Mohanty, S.N. Time series forecasting and modeling of food demand supply chain based on regressors analysis.
IEEE Access 2023, 11, 42679–42700. [CrossRef]

31. Huang, J.C.; Ko, K.M.; Shu, M.H.; Hsu, B.M. Application and comparison of several machine learning algorithms and their
integration models in regression problems. Neural Comput. Appl. 2020, 32, 5461–5469. [CrossRef]

32. Bentéjac, C.; Csörgő, A.; Martínez-Muñoz, G. A comparative analysis of gradient boosting algorithms. Artif. Intell. Rev. 2021, 54,
1937–1967. [CrossRef]

33. Velthoen, J.; Dombry, C.; Cai, J.J.; Engelke, S. Gradient boosting for extreme quantile regression. Extremes 2023, 26, 639–667.
[CrossRef]

34. Maulud, D.; Abdulazeez, A.M. A review on linear regression comprehensive in machine learning. J. Appl. Sci. Technol. Trends
2020, 1, 140–147. [CrossRef]

35. Kukreja, S.L.; Löfberg, J.; Brenner, M.J. A least absolute shrinkage and selection operator (LASSO) for nonlinear system identifica-
tion. IFAC Proc. Vol. 2006, 39, 814–819. [CrossRef]

36. Ranstam, J.; Cook, J.A. LASSO regression. J. Br. Surg. 2018, 105, 1348. [CrossRef]
37. Diebold, F.X.; Shin, M. Machine learning for regularized survey forecast combination: Partially-egalitarian lasso and its derivatives.

Int. J. Forecast. 2019, 35, 1679–1691. [CrossRef]
38. He, H.J.; Zhang, C.; Bian, X.; An, J.; Wang, Y.; Ou, X.; Kamruzzaman, M. Improved prediction of vitamin C and reducing sugar

content in sweetpotatoes using hyperspectral imaging and LARS-enhanced LASSO variable selection. J. Food Compos. Anal. 2014,
132, 106350. [CrossRef]

39. Rodriguez-Galiano, V.; Sanchez-Castillo, M.; Chica-Olmo, M.; Chica-Rivas, M.J.O.G.R. Machine learning predictive models for
mineral prospectivity: An evaluation of neural networks, random forest, regression trees and support vector machines. Ore Geol.
Rev. 2015, 71, 804–818. [CrossRef]

40. Geurts, P.; Ernst, D.; Wehenkel, L. Extremely randomized trees. Mach. Learn. 2006, 63, 3–42. [CrossRef]
41. Faezirad, M.; Pooya, A.; Naji-Azimi, Z.; Amir Haeri, M. Preventing food waste in subsidy-based university dining systems: An

artificial neural network-aided model under uncertainty. Waste Manag. Res. 2021, 39, 1027–1038. [CrossRef]
42. Priyadarshi, R.; Panigrahi, A.; Routroy, S.; Garg, G.K. Demand forecasting at retail stage for selected vegetables: A performance

analysis. J. Model. Manag. 2019, 14, 1042–1063. [CrossRef]
43. Falatouri, T.; Darbanian, F.; Brandtner, P.; Udokwu, C. Pre- dictive Analytics for Demand Forecasting–A Comparison of SARIMA

and LSTM in Retail SCM. Procedia Comput. Sci. 2022, 200, 993–1003. [CrossRef]
44. Schmidt, A.; Kabir, M.W.U.; Hoque, M.T. Machine Learning Based Restaurant Sales Forecasting. Mach. Learn. Knowl. Extr. 2022, 4,

105–130. [CrossRef]
45. Nassibi, N.; Fasihuddin, H.; Hsairi, L. Demand forecasting models for food industry by utilizing machine learning approaches.

Int. J. Adv. Comput. Sci. Appl. 2023, 14, 892–898. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.