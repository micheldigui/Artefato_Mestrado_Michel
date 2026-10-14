---
source_file: "2023-Using machine learning method to predict food waste in catering industry under high resolution a case in Dongguan.txt"
original_rel_path: "Trabalhos\Artigos\Aproveitar parcialmente\txt\2023-Using machine learning method to predict food waste in catering industry under high resolution a case in Dongguan.txt"
category: "Artigos_Aproveitar_parcialmente"
extension: ".txt"
sha256: "15d28a629e261989b0dc5d1adebe34a1186180c6aeb6d9bfea9b44df4c1491cb"
extracted_at: "2026-09-20T00:50:21.628600"
---

﻿Journal of Material Cycles and Waste Management (2023) 25:2442–2456
https://doi.org/10.1007/s10163-023-01706-8

ORIGINAL ARTICLE

Using machine learning method to predict food waste in catering 
industry under high resolution: a case in Dongguan

Jiehong Tang1,2 · Yuting Tang1,2   · Yupeng Liu3,4 · Hanchen Su1,2 · Yuxuan Zhang1,2 · Ziwei Sun1,2 · Xiaoqian Ma1,2

Received: 18 December 2022 / Accepted: 10 May 2023 / Published online: 20 May 2023 
© The Author(s), under exclusive licence to Springer Nature Japan KK, part of Springer Nature 2023

Abstract
Waste classification is comprehensively carried out in China as an important national-level policy, and the large amount and 
the wide range of food waste generation (FWG) cause problems in the collection, transportation, and treatment. This study 
has conducted the prediction of FWG from the catering industry under high resolution, and provided suggestions and insights 
for food waste management and treatment. Taking Dongguan as an example, a Back Propagation Network (BPN) model 
is used to predict FWG under different operation data, and based on the acquired theoretical FWG numerical distribution, 
the intervals used to divide FWG values are determined. Then a Random Forest (RF) model is applied to predict the FWG 
intervals of the restaurants in the Point of Interest (POI) data. FWG of 96,303 restaurants is predicted, and the predicted FWG 
from the catering industry is about 3,106 t per day. Variation of FWG in different categories of restaurants, the material flow 
of FWG at the restaurant level, patterns of FWG at the restaurant level, and spatial patterns of FWG at the city level are also 
investigated. Suggestions for improvement of food waste collection standard and source reduction of FWG, and insights into 
food waste collection and distributed treatment system are raised.
Graphical abstract

Keywords  Food waste · Geographic information system · Big data · Spatial analysis · High-resolution urban grid

Extended author information available on the last page of the article

V1ol :.3(1234567890)



Journal of Material Cycles and Waste Management (2023) 25:2442–2456	 2443

Introduction Mainstream methods of solid waste generation include 
regression analysis, time series analysis, grey system 

Garbage siege has become a serious problem for further model, system dynamics and machine learning. Regression 
high-quality development of socioeconomic in China, as analysis is the most widely used traditional method, as it 
the population explosively grows and reaches 1.4 billion has simple calculation and can obtain satisfying accuracy 
in 2020 [1]. According to Urban Construction Statistical by adjusting input parameters in the model, but it needs 
Yearbook, the delivering quantity of domestic waste in a large amount of data to screen proper input [10–13]. 
China has increased at an increasing rate of about 6% since Shu et al. further predicted the spatial distribution of food 
2016, and reached over 242 million tons in 2019 [2]. The waste production in Xiamen on the street scale based on 
increasing domestic waste generation causes a significant regression analysis [14]. Autoregressive Integrated Mov-
gap between the delivery quantity and the harmless treat- ing Average (ARIMA) model is the most commonly used 
ment capacity. In order to better realize the reduction and time series analysis, as it owns good accuracy in short-
utilization of solid waste, waste classification is compre- time prediction, but lacks interpretability in inner con-
hensively carried out in China as an important national- nections [15–18]. Grey system model was found in 1982 
level policy [3], and food waste is the major part of munic- [19], and first applied in waste generation prediction in 
ipal waste, accounting for the share of 56.79% reportedly 2000 [20]. Grey system model is proven to have good per-
[4]. Because the total amount of food waste generation formance under a lack of data, but it can only be applied 
(FWG) is large, but the generation sources are scattered in the common scenes under a few limited conditions [5, 
within a broad geographic spatial scale, the pattern of 21–24]. System dynamics can capture dynamic change, 
FWG is highly complicated, resulting in chaos of food and has the advantage of simulating the inner connections 
waste collection, then a low recycle rate of food waste. of complicated system, but it’s difficult to build the model 

Improving the recycle rate of food waste can accelerate and perfect the inner connections [25–28]. Considering 
the achievement of Carbon Peak and Carbon Neutrality that Machine learning (ML) has better performance when 
at the national level. Food waste is an essential part of facing the complex non-linear problems, and it can obtain 
organic waste. It’s reported that under a recycle rate of high accuracy by automatic parameters adjustment which 
80%, the total carbon dioxide equivalent (CO −e

2 ) emis- saves time and manpower, in this study ML is applied.
sions caused by sanitary landfill of organic waste can ML is now applied in the prediction of waste genera-
reduce approximately by 16% in Australia [5–7]. How- tion, treatment and recycling processes. Guo et al. showed 
ever, the recycle rate of food waste in China needs great that the majority (54%) of relevant studies on organic 
improvement. In Shenzhen, the recycle rate of food waste waste adopted Artificial Neural Network (ANN) for mod-
from the residential areas and the catering industry were eling and prediction, followed by Support Vector Machine 
only 0.2% and 28% in 2019, respectively [4]. Thus, map- (SVM), Genetic Algorithm (GA), and Decision Tree (DT)/ 
ping the high-resolution distribution of food waste is of Random Forest (RF) [29]. ANN has successfully been 
great significance, as it can provide references for gen- applied to predict domestic, commercial, industrial, medi-
eration amount estimation, collection route and strategy cal, and construction waste [30–33]. RF has strong inter-
determination, and cascade facilities configuration of pre- pretability and the ability to model the non-linear relation-
treatment and end-of-life treatment. Then, through estab- ship in waste generation [34–36]. Other methods were also 
lishing a comprehensive food waste treatment system, the widely used in the prediction of various waste [37, 38].
food waste can be collected and treated in a more energy- To date, the distribution of waste generation at the city 
saving and eco-friendly way. Thus, a comprehensive food level has still not been comprehensively investigated. Cur-
waste treatment system can exploit the potentialities of rent researches mainly focus on directly predicting waste 
reduction of greenhouse gas emissions during food waste generation at the city level using data released by official 
recycle and disposal [8]. statistics agency, as the input data can be acquired in sta-

Xu et al. summarized a basic framework of municipal tistics and bulletin conveniently [30–38]. Few researches 
solid waste generation forecasting, and the core issues have completed the bottom-up waste generation predic-
were concluded as scale and resolution, factor and method tion, by studying the waste generation of each emission 
[9]. The prediction conducted under a larger scale and a unit, and aggregating the amount of waste generation of 
higher resolution means the growth of the predicted units, each emission unit. Also, the “black boxes” feature of 
and consequently, more data are required as input. Based ANN causes poor interpretability despite high accuracy 
on the identification of chosen scales and resolution, influ- [34]. Consequently, existing researches only can predict 
encing factors are classified into intrinsic, socio-demo- the total amount of waste generation, but it lacks analy-
graphic, individual, natural and policy factors. sis on the distribution of food waste. Either, though the 

1 3



2	 444 Journal of Material Cycles and Waste Management (2023) 25:2442–2456

prediction result can acquire good accuracy, it can’t effec- discussion” explains the results, suggestions and insights 
tively point out the denominating factor. based on the results are given. Conclusions are given in 

The main aim of this study is to predict FWG from the Sect. “Conclusion”.
catering industry of Dongguan under high-resolution based 
on big data analysis and machine learning, and to provide 
suggestions and insights for food waste management and Materials
treatment. In this study, to the best of our knowledge, high-
resolution prediction of FWG from the catering industry Study area
is first conducted. To acquire accuracy and interpretabil-
ity at the same time, this study develops a machine learn- With a permanent resident population of over 10.47 million 
ing method based on field survey data and Point of Interest people [39], Dongguan has officially entered the ranks of the 
(POI) data. Back Propagation Network (BPN) is applied to 14 megacities in China. As Dongguan connects Guangzhou 
build the subsidiary FWG simulation model, which can pro- with Shenzhen, Dongguan is considered the node city of the 
vide references for interval setting, and RF is used to con- Guangdong–Hong Kong–Macao Greater Bay Area. Dongguan 
struct the FWG prediction model, which can directly predict owns 32 sub-district administrative regions, which are divided 
the FWG of each POI. By predicting the waste generation of into six functional areas, and the designed function for Shuixi-
numerous interested points, regional waste generation can ang New Town Area (SNTA), Urban Area (UA), East Indus-
be realized through spatial analysis, and the prediction of trial Area (EIA), Coastal Area (CA), Songshanhu Area (SA) 
waste distribution is completed in the scale of each inter- and Southeast Shenzhen-adjacent Area (SSA) is the zone for 
ested object at the same time, then the resolution of the map agriculture transformation and upgrading, city code enhance-
can reach 1 km × 1 km. ment, industrial and urban coordinated development, external 

The paper unfolds as follows: Sect. “Materials” briefly communication leading, high-tech innovation, and Shenzhen 
introduces the basic situation of Dongguan and data sources. spillover resources receiving, respectively (See Fig. 1) [39]. 
The method adopted to FWG prediction and results visuali- Table S1 listed the official statistics from the Dongguan Sta-
zation are described in Sect. “Method”. Sect. “Results and tistical Yearbook used by this study, and all the figures are 

Fig. 1   Administrative map of Dongguan

1 3



Journal of Material Cycles and Waste Management (2023) 25:2442–2456	 2445

graphed based on it [39]. According to the Dongguan Statisti- consumer flow, fund flow, and material flow, and the difference 
cal Yearbook, the generation of domestic waste in Dongguan in dynamic data between workday and off day can reflect the 
reached 5 million tons, and over 120,000 catering enterprises change in restaurant operation. Dynamic data can be used to 
were registered in 2021 [39], and both the two mentioned simulate how a restaurant performs under different seasons, 
indexes are expected to grow rapidly in the further future. The and static data can be used for the approximate prediction of 
local city government has conducted a 3-year plan aimed at different restaurants.
municipal waste classification, and will constantly improve the Besides, a typical Chinese food restaurant, which owned a 
daily food waste treatment capacity [40]. seat number of 300, a C-PC of about 75 CNY and a service 

count of about 400 per day, was chosen to conduct the depth 
Big data sources data collection. As the number of Chinese food restaurants 

occupies the largest share of total restaurant counts, it is of 
The population kernel density map was collected from the great importance to trace its material flow.
Baidu map in June 2021 using python 3.7.1. The POI data was 
collected from Automap in June 2021, and we collected the 
geo-location (latitude and longitude) of over 96,000 restaurants Methods
in Dongguan. Then, the expected consumption expenditure per 
capita and seat number of these restaurants were filled based Principle of input parameters selection
on the data from Dianping.com and a manual survey.

Intrinsic factors are used the most widely, as it includes 
Survey data sources quantitative indexes in fields of economics, urbanization, 

and living, which can be measured directly and available 
From January to August 2021, the survey has been conducted from the official documents (statistics, bulletin, etc.). On the 
in Dongguan. Thirty well-trained environmental volunteers, contrary, socio-demographic, individual, natural, and policy 
which were local college students, were dispatched to carry factors are qualitative indexes at most times. Researchers 
out questionnaire investigation in different functional regions need to quantify the indexes based on given circumstances, 
in 6 areas of Dongguan. The survey questionnaire is attached and it brings unavailable personal errors. In comparison, 
as the Supplementary Material. A total of 879 restaurants intrinsic factors can most directly reflect the situation of 
were investigated, and the samples covered all 11 categories waste generation. Consequently, studies on waste generation 
of restaurants according to the acquired POI data. The waste prediction should concentrate on intrinsic factors as prereq-
generation data was acquired from the 10-consecutive-day uisites, and consider the spontaneous correction brought by 
record in the ledger of food waste collection. To obtain official socio-demographic and individual factors, and mandatory 
statistics data and acknowledge the existing problems in food correction brought by natural and policy factors.
waste treatment, the interview with local qualified enterprises The correlation analysis can reflect the impacts of other 
of food waste treatment, the Leading Group for Waste Clas- survey data, which is divided into static data and dynamic 
sification of Dongguan and local catering industry associations data on total FWG (FWG-T), and the Correlation Coefficient 
were conducted. (CC) is calculated as Eq. (1)

Except for the total FWG (FWG-T), the survey data can ∑
be divided into two categories. The first is static data, which (x − x)(y − y)

reflects the basic situation of the restaurant, such as the res- CC(X, Y) = √∑ ∑ (1)
(x − x)2 (y − y)2

taurant type reflected by food waste production per capita 
(FWG-PC), seat numbers, consumption expenditure per capita where x and y y is the average of X and Y, respectively.
(C-PC), and local consumption in the catering industry per Table 1 shows the results of the correlation analysis. In 
capita (LCPC). Usually, the static data is determined in the terms of dynamic data, the ranking of impact on FWG-T 
beginning, and seldom changes throughout the whole busi- is material flow, fund flow, and consumer flow, from the 
ness life. Another is dynamic data, it includes service count, highest to the lowest. In terms of static data, the rank-
turnover, and raw materials, which respectively correspond to ings are seat numbers, consumption expenditure per capita 

Table 1   Correlation analysis of Dynamic data Static data
dynamic data and static data to 
FWG-T Service Turnover Meat Vegetable Others Seat Number FWG-PC C-PC LC-PC

count

FWG-T 0.28 0.32 0.41 0.49 0.88 0.32 0.081 0.35  − 0.07

1 3



2	 446 Journal of Material Cycles and Waste Management (2023) 25:2442–2456

(C-PC), FWG-PC, and local consumption expenditure different scenes, and based on the distribution, static data 
per capita (LC-PC) from the highest to the lowest. Com- can be used into predicting the numerical interval of FWG.
pared with dynamic data, static data have better accuracy 
and stability in predicting FWG-T of different types of Back propagation network (BPN) and random forest 
restaurants. Static data reflects the basic situation of the (RF)
restaurant, and seldom changes throughout the whole busi-
ness life. Dynamic data, on the one hand, lacks specific BPN is a multi-layer forward neural ANN (See Fig. 2a). 
official systematic statistics, and on the other hand, it has The weights of BPN are set randomly in the beginning, and 
a wide fluctuation range. Thus, dynamic data can be used continuously modified in the back propagation, until the dif-
into acquiring the distribution of FWG of the restaurant in ferences between the training data and output data meet the 

training precision [41]. BPN computes the final value of the 

Fig. 2   Diagram of the used machine learning methods a The Schematic diagram of BPN; b The Schematic diagram of RF; c The structure of the 
used machine learning methods

1 3



Journal of Material Cycles and Waste Management (2023) 25:2442–2456	 2447

hidden layer as shown in the Eq. (2) [42]. The decisive factor Table 2   Chosen interval values of seat number and dynamic data
(R2) and the mean absolute percentage error (MAPE) (See Seat number Service count Turnover (￥) Raw 
Eqs. (3) and (4)) are often used to evaluate the accuracy of material 
ANN [43]. (kg)

∑
y = b + xiwi (2) 50 250 2000 100

150 500 4000 200
∑ 250 750 6000 300

n
(y

i 1
R2 = i − yi)

2 350 1000 8000 400
= 1 − ∑n (3)

(y − y2 450 1250 10,000 500
i=1 i i

550 1500 12,000 600
650 1750 14,000 700

n
100% ∑ |

MAPE = |y |
i − yi | (4) 750 2000 16,000 800

n | y |
i=1 | i | 850 2250 18,000 900

950 2500 20,000 1000
where b is bias, xi is the initial variable value, w is weight, yi 1050 2750 22,000 1100
is the actual value, and yi is the predicted value. 3000 24,000 1200

RF is an ensemble learning method (See Fig. 2b). After 3250 26,000 1300
leveraging the strategy of bagging and random feature, RF 3500 28,000 1400
constructs several de-correlated decision trees and outputs 3750 30,000 1500
their average predictions [44]. Overall accuracy (OA) is the 4000 32,000 1600
proportion of correctly predicted samples to all samples 4250 34,000 1700
[45], calculated as Eq. (5). 4500 36,000 1800

True Positive + TrueNegative 4750 38,000 1900
OA =

True Positive + TrueNegative + False Positive + False Negative 5000 40,000 2000
(5)

The structure of the applied machine learning methods 
is shown in Fig. 2(c). Because the static data is collected at Graphing and mapping
the specific interval, rather than a specific value, the problem 
of the numerical prediction of FWG turns into the interval After acquiring the FWG of the restaurants in the POI, each 
estimation problem, which can be solved using a classifier restaurant is located based on its geographic information. 
in the artificial network. Thus, using proper intervals in the An urban grid under the resolution of 1 km × 1 km is con-
classification of FWG situations can both improve the pre- structed, and the FWG of one grid is the total of the FWG 
diction accuracy and the convergence rate of the artificial of the restaurants in this grid. The flow map is drawn by 
network. BPN is applied to simulate the FWG under dif- e!Sankey software (version 4.5.2). The generation of food 
ferent dynamic data. The model is trained by the dynamic waste is counted into 1 km × 1 km grids, and then aggregated 
data acquired from the field survey, using seat number, ser- into grid levels. The spatial patterns are visualized by Arc-
vice count, turnover and raw material as input, and using GIS software (version 10.7).
FWG as output. All the input and output data are used in the 
form of specific values. Then a presumed list of dynamic 
data, which is considered to fully cover the indexes of the Results and discussion
existing restaurants (See Table 2), is input to the model to 
acquire the frequency distribution of the generation of food Variation of FWG in different categories 
waste. Based on the distribution, the proper interval size of restaurants
of FWG can be determined. RF is unexcelled in accuracy 
among current algorithms, and it estimates which variables Survey data analysis
are important for the classification. The survey data after 
being processed in the determined interval size are used to Restaurants are divided into 11 categories as the same as the 
train the model, and the static data from POI are input into POI data, including Chinese food, Chinese fast food, western 
the model to predict the FWG of the restaurants in the POI. food, western fast food, bakery product, dessert, beverage, 
The output FWG of the RF model is in the form of classi- hot pot, Southeastern Cuisine, Japanese and Korean cuisine, 
fied intervals. Eventually, a numerical prediction problem is and Hong Kong style cuisine. These 11 categories can basi-
turned into an interval estimation problem. cally cover all kinds of restaurants in China. Based on the 

1 3



2	 448 Journal of Material Cycles and Waste Management (2023) 25:2442–2456

survey data, the FWG per capita (FWG-PC) of each category content can cause clogging problems in food waste treat-
of the restaurant can be calculated. The results are com- ment facilities. As business operation modes in the catering 
pared with another sampling survey conducted in Chengdu, industry are diversifying, the dynamic inventory of objects 
Sichuan Province [46] (See Table 3), as validation. The sur- to collect from and content to collect is needed to be estab-
vey in this study lacks the data on buffet, but adds the data of lished, and guidelines for each type of object to deal with its 
other 6 categories of restaurant mentioned. The FWG-PC of food waste are also needed to be published. To comprehen-
Chinese food and hot pot are lower than Yang’s survey, the sively evaluate the recycling value of food waste, a measur-
reason is the difference in dietary habits between Dongguan ing system should be innovated and standardized. Besides 
and Chengdu, as Guangdong cuisine prefers a light diet and the weight, more parameters should be included, such as oil 
Sichuan cuisine prefers food using more oil and spicy sauce, separation rate and purity. New parameters need new meas-
especially in hot pot. uring methods and tools, and using artificial measurements 

to realize the rough measure of the component proportion 
Suggestion for improvement of food waste collection in layered waste is one of the directions [51].
standard

Material flow of FWG at the restaurant level
Separate collection and recycling of food waste is not 
only the integral terminal part of restaurant food waste Material flow analysis
management [47], but also the important beginning part 
of the following municipal food waste disposal system. In order to identify key points of material flow during FWG, 
Thus, it is of great importance to regulate the collection a Chinese food restaurant is chosen to carry out material 
and recycling of food waste. Current Standard Techni- flow analysis for seven consecutive days, and Fig. 3 shows 
cal  Code  for  Food  Waste  Treatment has two versions the results. Raw materials consist of meat, vegetable, staple 
in China. One is released by the Ministry of Housing and food, sauce, seafood, and others. Staple food includes rice, 
Urban–Rural Development of the People's Republic of noodles, etc. The sauce includes oil, salt, etc. Others are the 
China (CJJ 184–2012) [48] as industry standard, and the raw materials which are not included in the listed categories 
other is released by the Market Supervision Administra- such as tofu. Food waste can be divided into avoidable and 
tion of Shenzhen Municipality (SZDBZ 252–2017) [49] unavoidable wastes [52]. Unavoidable waste is the waste 
as local standard. Both standards cover fields of definition, that can’t be eaten and thrown away during cuisine due to 
collection, transport, measurement, storage, and treatment, the need for quality, such as bone, shell, and charred food. 
but lack emphasis on collection, especially in terms of the Avoidable waste is the waste that can be eaten but thrown 
collection of different components. Current standards only away.
mentioning the wasted oil should be collected and trans- The quantification of food waste from the restaurant is 
ported separately, as waste oil is considered the most valu- based on weighting, waste composition estimation, and 
able compound of food waste in recycling [50], and high oil mass balance calculation [53]. The weight of raw material, 

leftover and food waste is measured by scales. After sepa-
Table 3   Average Food waste generation per capita of each category rating the liquid from the food waste, the waste composi-
of restaurant tion estimation is conducted. The weight of avoidable waste 

is calculated as the weight of remaining food waste minus 
Category Survey data (kg) Yang, 

et al. [46] the weight of unavoidable waste. The weight of unavoid-
(kg) able waste is calculated based on the following facts: the 

proportion of meat and bone in poultry is 8:2, the propor-
Chinese food 0.23 0.3–0.7 tion of meat and bone in livestock is 7:3, the proportion of 
Western food 0.29 0.2–0.5 meat and shell (or bone) in seafood is 9:1. The total weight 
Fast food 0.13 Chinese 0.1–0.2 of food waste is about 120 kg, and liquid takes the share of 

0.11 Western approximately 60 kg.
Hot pot 0.24 0.5–1.0 As it can be seen from Fig. 3, a main part of raw materi-
Buffet – 0.2–0.3 als (86.7%) is delivered to be served after cuisine, and the 
Beverage 0.09 – rest (13.3%) is abandoned as leftover. Then, the served part 
Dessert 0.10 – is mainly consumed (53.8%), and the rest are wasted. The 
Japanese and Korean cuisine 0.85 – proportion of avoidable and unavoidable wastes is approxi-
Southeastern cuisine 0.69 – mately 3:1. In a similar research conducted in school can-
Hong Kong style cuisine 0.21 – teens in Malaysia, it also found that unavoidable waste was 
Bakery 0.12 – the major part of food waste [54]. It can be seen that the 

1 3



Journal of Material Cycles and Waste Management (2023) 25:2442–2456	 2449

Fig. 3   Result of material flow of a Chinese food restaurant in one day

most direct way to reduce FWG in the restaurant is the real-time delivery based on actual needs. In this way, the 
reduction of avoidable waste generation, and the reduction shelf life of semi-products can fully recover the service life 
of unavoidable waste generation can also be realized through of restaurants, which makes sure all the semi-products can 
the upstream process. be consumed in 2 days. Restaurants can also play a role by 

offering a different quantity of meals to meet the needs of 
Suggestion for source reduction of FWG at the restaurant different number of consumers, and changing set-meal style 
level into individual-meal style [59]. For the government, as the 

behavior of saving food waste has relied more on personal 
FWG exists in the whole food supply chain [55]. As restau- virtue than on politics or religion in China, the Clean Your 
rants can be considered as the downstream part of the food Plate Campaign should be further continuously conducted 
supply chain, FWG is determined by the supplying capacity within long-term school education and media publicity with 
and consuming capacity of raw materials. From the perspec- appropriate incentives [60].
tives of material flow, the raw material is supplied by restau-
rants and consumed by consumers. As Fig. 3 shows, among Patterns of FWG at the restaurant level
two parts of food waste, unavoidable waste mainly relates 
to restaurants, and avoidable waste mainly relates to con- Patterns of FWG under different operation data
sumers. About 75% of food waste comes from unavoidable 
waste, and to be more specific, 20% comes from the lefto- It can be noticed during the survey that the amount of seat 
ver. To reduce leftover, restaurants can optimize the cooking number and dynamic data has a range, and to simulate all the 
process, simplify presentations or push out new dishes to situations of different restaurant operations, this study selects 
fully use the raw material [56]. To reduce the rest of the una- several interval values to make combinations as the input. 
voidable waste, purchasing pretreated raw materials that are The total number of combinations is 88000, and the chosen 
free of uneatable parts can be a good way, so that this part interval values are listed in Table 2. The R2 and MAPE of 
of waste can be left in the supplier to wait for centralized the BPN model are 0.96 and 8.12%. After rounding the pre-
treatment and eatable part of the delivered dishes becomes dicted FWG, the frequency of each value is counted (See 
more. Also, the restaurant should reasonably make operat- Fig. (a). The curve can be divided into high-, middle-, and 
ing plans and scientifically prepare raw materials based on low-frequency zones based on the trend, and several peaks 
real needs, and it can avoid raw materials being discarded can be discovered in high- and middle-frequency zones. The 
due to surplus, and proper reuse and storage of the remain- value of the discovered peaks can be considered the value 
ing materials are also important. FWG in the food prepara- with the highest probability of occurrence among the sur-
tion part is thought to be huge [57], and the central kitchen rounding values. Because the frequency of 0–15 kg is 32052, 
system  is a new way to meet the needs of material supply which is significantly higher, the first interval is set to be 
and food waste reduction in chain restaurants [58]. The food 0–15 kg. In high- and middle- frequency zones, the average 
factory and the central kitchen produce semi-products based interval of the peaks is 32.5 kg and 44.75 kg, respectively. 
on the needs of restaurants, and semi-product can remain in For convenience, the mentioned interval is set to 30 kg and 
a good status in the central kitchen for 4 to 5 days. Restau- 45 kg, respectively. In the low-frequency zone, no obvious 
rants are asked to order raw materials for needs of 2 days peak can be discovered, and we set the interval to 105 kg 
each time, and can send orders to the central kitchen for here. Above all, the intervals of 15 kg, 30 kg, 45 kg, and 

1 3



2	 450 Journal of Material Cycles and Waste Management (2023) 25:2442–2456

105 kg are used in the division of intervals of 0–15 kg, reduces the number of dimensions when using the on-hot 
15–105 kg, 105–330 kg, and 330–2115 kg, respectively. encoder method, and the fluctuation in each interval brings 

Figure 4b shows the frequency distribution when divid- similar error to the basic FWG.
ing the result into blocks of 15 kg. BPN simulation and Figure 5 shows the variation trend between the dynamic 
survey data have a similar frequency distribution, in which data and FWG. The color and the size of the data point 
the interval of 0–15 kg takes the largest share, then the reflect the quantity of FWG, and the bigger the size is, the 
second largest share is occupied by the intervals between larger the quantity is. The relation between color and quan-
15 and 105 kg in the survey, and between 15 and 285 kg in tity can refer to the scale in the figure. It shows that FWG 
BPN simulation. The total frequency of remaining results, is highly increased with the growth of raw material under 
which are between 285 and 2115 kg, is less than 4% in the the same circumstance, and on the contrary, with the same 
survey, and less than 10% in the BPN simulation, and it amount of raw material, FWG decreases as the seat number 
suggests that the interval of 0–105 kg should be divided or service count rises. This result has indicated that FWG 
into narrower intervals, then the expanded interval can be shows a positive correlation with raw material supply capac-
used to divide the interval of 105–305 kg, and the divi- ity, and a negative correlation with raw material consume 
sion of the interval of 305–2115 kg can be even looser. capacity. With other parameters remaining the same, FWG 
Figure 4c shows the frequency distribution when using increases with the rising turnover, but not significant as with 
15 kg, 30 kg, 45 kg, and 105 kg in the division of intervals the rising seat number and service count. It suggests that an 
of 0–15 kg, 15–105 kg, 105–330 kg, and 330–2115 kg, upscale restaurant tends to generate more food waste, as the 
respectively. As it shows, the result basically concentrates consumption expenditure per capita is higher, which may 
on 0–330 kg, and is sparsely distributed in the remaining relate to stricter material requirements and more complicated 
intervals. Then the number of intervals is smaller, and it cuisine craft. The highest FWG happens under the situation 

Fig. 4   Frequency distribution of the FWG based on different intervals a Based on intervals of 1 kg; b Based on equal intervals of 15 kg; c Based 
on progressive intervals

1 3



Journal of Material Cycles and Waste Management (2023) 25:2442–2456	 2451

Fig. 5   Distribution of food waste as dynamic data change a Service count, turnover, and raw materials; b Seat Number, raw materials, and turno-
ver; c Seat number, service count, and turnover; d Seat number, service count, and raw materials

of the highest raw material and consumption expenditure problem and the FWG predicting problem. The competent 
per capita, and the lowest seat number and service count. department should also have access to supervise the system. 

In a case conducted in Canada, using smart technology and 
Insights into food waste collection system geo-localization means to plan the food waste collection 

routes, based on 12.2 km between sites and a fleet of 200 
As further reliable food waste collection services can facili- trucks, a potential reduction of 940 t C O −e

2  per year can be 
tate the timely food waste separation and recycling of the realized [61].
restaurant [47], the establishment of a food waste collec-
tion and transport information system (FWCTIS) should be Spatial Patterns of FWG at the city level
put on the agenda. The survey in Dongguan showed that 
due to the information asymmetry between restaurants and Distribution of FWG under high resolution
qualified enterprises of food waste treatment, the problem 
of the food waste couldn’t be collected by qualified enter- In this study, Random Forest Network is found to be the 
prises in time, and treatment capacity can’t be fully used best prediction model, as it owns an OA of 0.85, and other 
(about 50% of the designed capacity) with surplus transport models, such as the BPN and RBFN (radial basis function 
capacity in the same time. This results in misunderstanding, network), own a significantly lower OA of about 0.5. Oper-
which causes negative effects, such as restaurants selling ating a feature importance check is a necessary step before 
food waste to unqualified enterprises illegally, and qualified running a Random Forest Network, and the result of RF 
enterprises are not willing to provide service to restaurants shows a different result compared with Fig. 4. The impor-
far from the plant due to high transport cost. FWCTIS is tance feature of seat number, C-PC, LC-PC, and FWG-PC is 
designed to eliminate information asymmetry. Restaurants 0.42, 0.24, 0.21, and 0.13, respectively, and the importance 
can upload their needs and demand on collecting frequency of seat number and LC-PC has been improved, which might 
and time, and realize the online set-up of the ledger for col- be related to the unique operation mechanism of Random 
lection. Qualified enterprises can in real time deploy collec- Forest Network.
tor vehicles based on the received information, and adjust FWG patterns of 96,303 restaurants are predicted, and 
the operation of the treatment plant. What’s more, FWCTIS the predicted FWG from the catering industry in Dongguan 
should have the ability to solve the collecting vehicle routing is about 3106.00 t per day. The results are listed in Tables 

1 3



2	 452 Journal of Material Cycles and Waste Management (2023) 25:2442–2456

S2–S5. According to the sample survey on the composition count and FWG and its fresh sugary beverage has a mas-
of domestic waste conducted in Guangzhou in 2021 [62], the sive of potential consumers, such as milky tea and fruit tea. 
share of food waste in domestic waste is 52.99%. Thus, it can However, the moisture content of food waste generated in 
be estimated that the FWG in Dongguan is about 7258.90 beverage shops is extremely higher than the others, because 
t per day, and the part from the catering industry takes the this food waste is mainly come from the remaining liquid 
share of approximately 42.79%. and sugary leftovers. Also, the generation can have a large 

Seat number has the highest figure both in correlation fluctuation, as the staff sometimes dump the liquid waste 
analysis and feature importance analysis, indicating that as directly into the drain. The FWG of the bakery is also argu-
the seat number grows, share of count and generation both able, as the bakery often overproduces to satisfy the need for 
decrease. Small-sized and medium-sized restaurants, whose display, and the waste can be re-used or donated.
seat number is between 0 and 100, take the highest share of Figure 6 shows the distribution map of food waste, the 
93.75% in count number, and contribute over 90% of the catering industry, population, and turnover of catering indus-
total food waste. As a result, the frequency of the interval of try. Figure 6(a, b) is graphed based on a metric fishnet of 
16–45 kg reaches 95.22%. Compared with the result of the 1 km × 1 km, and Fig. 6(c) is vectorized based on the popu-
prediction of BPN, the highest frequency in FWG is con- lation thermogram collected from the Gaode map. At the 
tributed by 16–45 kg rather than 0–15 kg, and the reason grid level, the distribution of population, restaurant count, 
is that to generate 0–15 kg food waste, raw material sup- and FWG has a successive trend. The FWG in area level for 
ply capacity is needed to be strictly close with raw material UA, CA, SSA, SA, EIA, and SNTA was 22.37, 23.33, 14.49, 
consume capacity, which is hard to satisfy in reality. C-PC 19.54, 15.00%, and 5.28%, respectively. High-density zones 
reflects the grades of the restaurants. The restaurants can in UA and CA were linked together. In SSA, it formed three 
be divided into the eatery, the middle-class restaurant, the high-density zones in the middle of the three main towns. 
upscale restaurant, and the luxury restaurant, whose C-PC In EIA and SA, discrete high-density zones can be found, 
is 0–50, 50–100, 100–300, and beyond 300, respectively. which may attribute to the sporadic urbanized regions in 
Eatery has the highest total and contributes the most food these two areas. SNTA only formed a middle-density zone 
waste. The category of restaurant is also an important factor. in the restricted town center.
Chinese fast food restaurants and Chinese food restaurants Figure 6d shows the correlation between the distribu-
together take 38.15% and 47.37% of restaurant count, and tion of FWG, population, GDP, local catering industry 
FWG is in accordance with local Chinese diet habits [63]. income (LCII), and LCPC at the area level. The correlation 
It’s noticeable that beverage shop ranks third in restaurant coefficients of population-FWG, Restaurant count-FWG, 

Fig. 6   Distribution map of food waste, restaurant, population and turnover of catering industry, a Food waste; b Restaurant; c Population; d Cor-
relation;

1 3



Journal of Material Cycles and Waste Management (2023) 25:2442–2456	 2453

GDP-FWG, LCII-FWG, and LCPC-FWG are 0.97, 0.99, 0.9, processing capacity of waste disposal facilities and low rates 
0.88, and 0.74, respectively. LCII reflects the local catering of sorting waste cause low efficiency of the whole food 
business status, and LCPC represents the potential of local waste treatment system. Using primary treatment facilities to 
individual consumption. A high urbanization rate means a separate oil and moisture can significantly reduce the weight 
large population and a prosperous economic level. Due to the but improve the purity of food waste in the end-of-life treat-
busier lifestyle and the stronger spending power of residents, ment, and it can solve the problem of the lack of end-of-life 
the growth of the urbanization rate brings about an increas- treatment capacity and transport capacity. Another reason of 
ing number of restaurants and a more frequent eat-out rate in-community groups constructing primary treatment facil-
[64]. It suggests that the urbanization level is a significant ity is better than end-of-life facility in-community groups 
factor in the FWG from the catering industry, as the local is that end-of-life product may not be local consumed. A 
population provides the base for the potential consumers, centralized processing can centralize the use of product and 
and local GDP determines the spending power of consum- improve efficiency. When choosing technological routes of 
ers. Food waste contains parts from the catering industry and facility, local government should comprehensively consider 
the residential area, and it can also be extrapolated that the the cost, profit, and especially the market-consuming power 
proportion of the food waste from the catering industry will of the product, to avoid the recycling product from becomes 
increase with the growth of the urbanization rate. waste again [66].

Insights into distributed food waste treatment system

Distributed food waste treatment system is considered one Conclusion
of the best ways to solve the problem that food waste has a 
larger amount of generation and a wide range of distribution. This study has first developed a machine learning method 
According to Technical Code for Food Waste Treatment (CJJ to predict the FWG from the catering industry under high-
184–2012) [48], food waste treatment plant is divided into resolution based on grabbed POI data and filed survey data. 
category I, II, III, and IV, with the daily treatment of beyond In this method, a BPN model was used to predict FWG 
300 t, 150–300 t, 50–150 t, and under 50 t, respectively. The under different operation data. Then, based on the acquired 
local government of Dongguan is conducting a plan to con- theoretical FWG numerical distribution, the intervals used 
struct category III and IV treatment plants in every town and to divide FWG values were determined. By this step, the 
street, even in community groups, to realize the real-time numerical prediction issue has been transformed into the 
and in situ treatment of food waste. With existing plants with interval classification issue, and eventually, a RF model was 
the largest capacity in Mayong (300 t/d) and Nancheng (200 used to predict the FWG intervals of the restaurants in the 
t/d), Dongguan is building a distributed food waste treatment POI data. FWG patterns of 96,303 restaurants are predicted, 
system, which uses anaerobic fermentation as centralized and the predicted FWG from the catering industry is about 
treatment, and uses high-temperature composting and bio- 3,106.00 t per day. Variations of FWG in different categories 
logical transformation as decentralized treatment. If each of restaurants, the material flow of FWG at the restaurant 
treatment plant is conducting end-of-life treatment, then level, patterns of FWG at the restaurant level, and spatial 
the capacity of the plant is limited by technological require- patterns of FWG at the city level were investigated. Based on 
ments, causing high economical costs and a huge number of the mentioned findings, suggestions for improvement of food 
plants to match the FWG. A high-resolution map can provide waste collection standard and source reduction of FWG, and 
reference to the location, service scale, and capacity of the insights into the food waste collection system and distributed 
treatment plant in the distributed food waste treatment sys- food waste treatment system were raised.
tem, and is also beneficial to the route optimizing problem.

Thus, the distributed food waste treatment system should 
consist of pre-treatment and end-of-life treatment facilities Supplementary Information  The online version contains supplemen-
to realize cascade utilization [8]. From the perspectives of tary material available at https://d​ oi.o​ rg/1​ 0.1​ 007/s​ 10163-0​ 23-0​ 1706-8.
the administrative precinct, it is estimated that the FWG of 
towns and streets in Dongguan is between 72 t/d and 1432 

Acknowledgements  Thanks for the assistance provided by the Leading 
t/d. For districts with small FWG, adjacent regions can com- Group of Waste Classification during this study.
bine to jointly construct an end-of-life plant, or districts with 
large FWG can expand their capacity to receive the waste Author contributions  JT: Conceptualization, Methodology, Software, 
which is pretreated in adjacent regions. From the perspec- Data curation, Writing–original draft, Writing–review and editing. YT: 

Supervision, Writing–review and editing. YL: Methodology, Software, 
tives of cascade utilization, the facility with primary treat- Data curation. HS: Software, Data curation. YZ: Writing – review and 
ment has a larger capacity. Wen et al. [65] found that limited editing. ZS: Writing – review and editing. XM: Supervision.

1 3



2	 454 Journal of Material Cycles and Waste Management (2023) 25:2442–2456

Funding  This study was financially supported by the National Key J Environ Manage 182:80–93. https://d​ oi.o​ rg/1​ 0.1​ 016/j.j​envma​ n.​
R&D Program of China (2020YFC1908901), Guangdong Basic and 2016.​07.​026
Applied Basic Research Foundation (2023A1515030016) and the Stra- 	13.	 Al-Salem SM, Al-Nasser A, Al-Dhafeeri AT (2018) Multi-varia-
tegic Pilot Science and Technology Projects of Chinese Academy of ble regression analysis for the solid waste generation in the State 
Sciences (XDA23030304). of Kuwait. Process Safety Environ Protect 119:172–180. https://​

doi.​org/​10.​1016/j.​psep.​2018.​07.​017
Declarations  	14.	 Shu S, Wang R, Sun Y, Liu J (2012) Spatial down-scaling analy-

sis and simulation of kitchen waste density. Environ Sci Technol 
Conflict of interest  The authors declared no potential conflicts of inter- 35(61):458–463
est with respect to the research, authorship, and/or publication of this 	15.	 Lin J-g (1998) Feasibility study on prediction of properties of 
article. municipal solid waste with time series models. J Hazardous Mate-

rials 58(1–3):47–57. https://​doi.​org/​10.​1016/​s0304-​3894(97)​
00119-2

	16.	 Navarro-Esbrı́ J, Diamadopoulos E, Ginestar D, (2002) Time 
References series analysis and forecasting techniques for municipal solid 

waste management. Resources, Conservation Recycling 
	 1.	 National Bureau of Statics (2021) Bulletin of the seventh National 35(3):201–214. https://​doi.​org/​10.​1016/​s0921-​3449(02)​00002-2

Census. http://​www.​stats.​gov.​cn/​tjsj/​tjgb/​rkpcgb/​qgrkp​cgb/ 	17.	 Wu L, Lu J, Liao L, Jiang J (2013) Prediction of domestic waste 
	 2.	 Ministry of Housing and Urban-Rural Development of the Peo- output based on ARIMA model. Environ Sanitation Eng 21(5):1–

ple’s Republic of China (2020) Urban Construction Statistical 4. https://​doi.​org/​10.​3969/j.​issn.​1005-​8206.​2013.​05.​001
Yearbook 2019. http://w​ ww.m​ ohurd.g​ ov.c​ n/x​ ytj/t​jzljs​ xytjg​ b/j​stjnj/​ 	18.	 Song Z, Li Y, Huang Z (2015) Analysis and Forecast of Construc-
w0202​01231​22485​27142​31250​00.​xls tion Waste Based on ARIMA Model. 5th International Conference 

	 3.	 Ministry of Housing and Urban-Rural Development of the Peo- on Civil Engineering and Transportation; Guangzhou.
ple’s Republic of China (2017) Domestic Waste Classification 	19.	 Ju-Long D (1982) Control problems of grey systems. Sys Con-
Regulation. http://w​ ww.m​ ohurd.g​ ov.c​ n/w​ jfb/2​ 01906/t​20190​ 606_​ trol Lett 1(5):288–294. https://​doi.​org/​10.​1016/​s0167-​6911(82)​
240787.​html 80025-x

	 4.	 Wang H, Li H, Yin M, Du X, Zhou Y, Li T, Liu J (2020) Analysis 	20.	 Chen HW, Chang NB (2000) Prediction analysis of solid waste 
on source emission rule and resource recovery path of MSW in generation based on grey fuzzy dynamic modeling. Resour Con-
Shenzhen. Environ Sanitat Eng 28(3):21–27. https://​doi.​org/​10.​ servation Recycling 29(1–2):1–18. https://d​ oi.o​ rg/1​ 0.1​ 016/S​ 0921-​
19841/j.​cnki.​hjwsgc.​2020.​03.​004 3449(99)​00052-X

	 5.	 Kiran M, Shanmugam PV, Mishra A, Mehendale A, Sherin NHR 	21.	 Liu G, Yu J (2007) Gray correlation analysis and prediction mod-
(2021) A multivariate discrete grey model for estimating the waste els of living refuse generation in Shanghai city. Waste Manag 
from mobile phones televisions and personal computers in India. 27(3):345–351. https://​doi.​org/​10.​1016/j.​wasman.​2006.​03.​010
J Cleaner Prod. https://​doi.​org/​10.​1016/j.​jclep​ro.​2021.​126185 	22.	 Zhao M, Zhao C, Yu LL, Li GM, Huang JW, Zhu HC, He WZ 

	 6.	 Australian Organics Recycling Association (2020) Australian (2016) Prediction and analysis of WEEE in China based on the 
Organics Recycling Industry Capacity Assessment: 2020–21. gray model. Selected Proceed Tenth International Conference 
Department of Agriculture, Water and the Environment of Aus- Waste Manag Technol 31:925–934. https://​doi.​org/​10.​1016/j.​
tralia, Green Industries South Australia. https://w​ ww.e​ nviro​ nment.​ proenv.​2016.​02.​113
gov.​au/​system/​files/​resou​rces/​fa3f7​0c8-​44d2-​42e6-​b57d-​0a941​ 	23.	 Duman GM, Kongar E, Gupta SM (2019) Estimation of electronic 
14832​ec/​files/​austr​alian-​organ​ics-​recyc​ling-​indus​try-​capac​ity-​ waste using optimized multivariate grey models. Waste Manag 
asses​sment-​2020-​21.​pdf 95:241–249. https://​doi.​org/​10.​1016/j.​wasman.​2019.​06.​023

	 7.	 Blue Environment (2020) National Waste Report 2020. Depart- 	24.	 Zhou W, Zeng B, Wang J, Luo X, Liu X (2021) Forecasting 
ment of Agriculture, Water and the Environment. https://​www.​ Chinese carbon emissions using a novel grey rolling prediction 
envir​onment.​gov.​au/​system/​files/​pages/​5a160​ae2-​d3a9-​480e-​ model. Chaos Solitons Fractals. https://​doi.​org/​10.​1016/j.​chaos.​
9344-​4eac4​2ef90​01/​files/​natio​nal-​waste-​report-​2020.​pdf 2021.​110968

	 8.	 Ascher S, Li W, You S (2020) Life cycle assessment and net pre- 	25.	 Tseng C-H, Hsu Y-C, Chen Y-C (2019) System dynamics mod-
sent worth analysis of a community-based food waste treatment eling of waste management, greenhouse gas emissions, and envi-
system. Bioresour Technol. https://​doi.​org/​10.​1016/j.​biort​ech.​ ronmental costs from convenience stores. J Cleaner Production. 
2020.​123076 https://​doi.​org/​10.​1016/j.​jclep​ro.​2019.​118006

	 9.	 Xu L, Cui S, Yan Z, Lin T (2013) Core issues of forecasting 	26.	 Zhu C, Fan R, Luo M, Lin J, Zhang Y (2020) Urban food waste 
municipal solid waste generation. Environ Sci Technol 32(2):184– management with multi-agent participation: a combination of evo-
190. https://​doi.​org/​10.​3969/j.​issn.​1003-​6504.​2013.​02.​038 lutionary game and system dynamics approach. J Cleaner Produc-

	10.	 Winer AM, Peters JW, Smith JP, Pitts JN (2002) Response of tion. https://​doi.​org/​10.​1016/j.​jclep​ro.​2020.​123937
commercial chemiluminescent nitric oxide-nitrogen dioxide ana- 	27.	 Galeano DAR, Rodriguez SCB (2021) An integrated method of 
lyzers to other nitrogen-containing compounds. Environ Sci Tech environmental analysis and system dynamics for management of 
8(13):1118–1121. https://​doi.​org/​10.​1021/​es600​98a004 mobile phone waste in Colombia. J Cleaner Production. https://​

	11.	 Benitez SO, Lozano-Olvera G, Morelos RA, Vega CA (2008) doi.​org/​10.​1016/j.​jclep​ro.​2020.​123768
Mathematical modeling to predict residential solid waste genera- 	28.	 Rafew SM, Rafizul IM (2021) Application of system dynamics 
tion. Waste Manag 28(Suppl 1):S7–S13. https://d​ oi.o​ rg/1​ 0.1​ 016/j.​ model for municipal solid waste management in Khulna city of 
wasman.​2008.​03.​020 Bangladesh. Waste Manag 129:1–19. https://​doi.​org/​10.​1016/j.​

	12.	 Ghinea C, Dragoi EN, Comanita ED, Gavrilescu M, Campean wasman.​2021.​04.​059
T, Curteanu S, Gavrilescu M (2016) Forecasting municipal solid 	29.	 Guo H, Wu S, Tian Y, Zhang J, Liu H (2021) Application of 
waste generation using prognostic tools and regression analysis. machine learning methods for the prediction of organic solid 

waste treatment and recycling processes: a review. Bioresour 
Technol. https://​doi.​org/​10.​1016/j.​biort​ech.​2020.​124114

1 3



Journal of Material Cycles and Waste Management (2023) 25:2442–2456	 2455

	30.	 Tiwari MK, Samir Bajpai UD (2012) Prediction of industrial solid Waste Manag 68:186–197. https://​doi.​org/​10.​1016/j.​wasman.​
Waste with ANFIS model and its comparison with ANN Model-a 2017.​03.​044
case study of Durg-Bhilai Twin City India. Internat J Eng Innova- 	45.	 Xiong N, Lu H, Yang X, Wang J, Yue D (2022) Spatial charac-
tive Technol 9001:192–201 teristics and multifactorial driving analysis of fly-tipping bulky 

	31.	 Golbaz S, Nabizadeh R, Sajadi HS (2019) Comparative study of waste in Beijing based on the random forest model. J Cleaner 
predicting hospital solid waste generation using multiple linear Production. https://​doi.​org/​10.​1016/j.​jclep​ro.​2022.​132534
regression and artificial intelligence. J Environ Health Sci Eng 	46.	 Yang S, Wang K, Wu S, Zhou Y (2018) Prediction on generation 
17(1):41–51. https://​doi.​org/​10.​1007/​s40201-​018-​00324-z quantity of food waste in planning of kitchen waste disposal facili-

	32.	 Coskuner G, Jassim MS, Zontul M, Karateke S (2021) Applica- ties. Environ Sanitation Eng 26(003):89–90
tion of artificial intelligence neural network modeling to predict 	47.	 Filimonau V, De Coteau DA (2019) Food waste management in 
the generation of domestic, commercial and construction wastes. hospitality operations: a critical review. Tour Manage 71:234–
Waste Manag Res 39(3):499–507. https://​doi.​org/​10.​1177/​07342​ 245. https://​doi.​org/​10.​1016/j.​tourm​an.​2018.​10.​009
42X20​935181 	48.	 Ministry of Housing and Urban-Rural Development of the Peo-

	33.	 Lu W, Lou J, Webster C, Xue F, Bao Z, Chi B (2021) Estimating ple’s Republic of China (2012) Technical Code for Food Waste 
construction waste generation in the greater bay area. China Using Treatment. China Architecture & Building Press, Beijing
Machine Learning Waste Manag 134:78–88. https://​doi.​org/​10.​ 	49.	 Market Supervision Administration of Shenzhen Municipality 
1016/j.​wasman.​2021.​08.​012 (2017) Technical  Code  for  Food  Waste  Treatment. Shenzhen 

	34.	 Kannangara M, Dua R, Ahmadi L, Bensebaa F (2018) Modeling city, Guangdong Province.
and prediction of regional municipal solid waste generation and 	50.	 Lang L, Wang Y, Chen X, Zhang Z, Yang N, Xue B, Han W 
diversion in Canada using machine learning approaches. Waste (2020) Awareness of food waste recycling in restaurants: evidence 
Manag 74:3–15. https://​doi.​org/​10.​1016/j.​wasman.​2017.​11.​057 from China. Resources, Conservation Recyclin. https://d​ oi.o​ rg/1​ 0.​

	35.	 Solano Meza JK, Orjuela Yepes D, Rodrigo-Ilarri J, Cassiraga E 1016/j.​resco​nrec.​2020.​104949
(2019) Predictive analysis of urban waste generation for the city of 	51.	 Cropley M, Sprajcer M, Dawson D (2022) Wastogram: Validation 
Bogota, colombia, through the implementation of decision trees- of a new tool to measure household food waste. J Environ Psy. 
based machine learning, support vector machines and artificial https://​doi.​org/​10.​1016/j.​jenvp.​2022.​101896
neural networks. Heliyon. https://d​ oi.o​ rg/1​ 0.1​ 016/j.h​ eliyo​ n.2​ 019.​ 	52.	 Papargyropoulou E, Lozano RK, Steinberger J, Wright N, Ujang 
e02810 ZB (2014) The food waste hierarchy as a framework for the 

	36.	 Rutqvist D, Kleyko D, Blomstedt F (2020) An automated machine management of food surplus and food waste. J Cleaner Product. 
learning approach for smart waste management systems. Ieee https://​doi.​org/​10.​1016/j.​jclep​ro.​2014.​04.​020
Transactions Indust Informatics 16(1):384–392. https://​doi.​org/​ 	53.	 de Oliveira PT, da Silva CA, Conejero MA, Rodrigues Delib-
10.​1109/​Tii.​2019.​29155​72 erador L, Otávio Batalha M (2022) Food waste measurement in 

	37.	 Ferreira JA, Costa M, Tereso A, Oliveira JA (2015) A multi-cri- a chain of industrial restaurants in Brazil. J Cleaner Production. 
teria decision support system for a routing problem in waste col- https://​doi.​org/​10.​1016/j.​jclep​ro.​2022.​133351
lection. International Conference on Evolutionary Multi-Criterion 	54.	 Kasavan S, Ali NIBM, Ali SSBS, Masarudin NAB, Yusoff SB 
Optimization (2021) Quantification of food waste in school canteens: a mass 

	38.	 Hu R, Chen K, Chen W, Wang Q, Luo H (2021) Estimation of flow analysis. Resour, Conservat Recycling. https://​doi.​org/​10.​
construction waste generation based on an improved on-site meas- 1016/j.​resco​nrec.​2020.​105176
urement and SVM-based prediction model: a case of commercial 	55.	 Lipinski B. HC, Lomax J., Kitinoja L., Waite R., Searchinger T. 
buildings in China. Waste Manag 126:791–799. https://​doi.​org/​ (2013) World Resources Institute Working Paper.1–40.
10.​1016/j.​wasman.​2021.​04.​012 	56.	 Spang ES, Moreno LC, Pace SA, Achmon Y, Donis-Gonzalez 

	39.	 Bureau of Statistics of Dongguan (2022) Dongguan Statiscal Year- I, Gosliner WA, Jablonski-Sheffield MP, Momin MA, Quested 
book 2021. http://​tjj.​dg.​gov.​cn/​tjnj/​index.​html TE, Winans KS, Tomich TP (2019) Food loss and waste: 

	40.	 The People's Government of Dongguan City in Guangdong Prov- measurement, drivers, and solutions. Annual Rev Environ 
ince (2020) Three-year Action Plan of Municipal Solid Waste Resour 44(1):117–156. https://​doi.​org/​10.​1146/​annur​ev-​envir​
Classification in Dongguan (2020–2022). http://​www.​dg.​gov.​cn/​ on-​101718-​033228
gkmlpt/​conte​nt/3/​3169/​post_​31699​71.​html#​684 	57.	 SRA (2010) Too Good to Waste: Restaurant Food Waste Survey 

	41.	 Wu D, Zhang D, Liu S, Jin Z, Chowwanonthapunya T, Gao J, Report. London: SRA (Sustainable Restaurant Association).
Li X (2020) Prediction of polycarbonate degradation in natural 	58.	 Gao S, Bao J, Li R, Liu X, Wu C (2021) Drivers and reduction 
atmospheric environment of China based on BP-ANN model with solutions of food waste in the Chinese food service business. 
screened environmental factors. Chem Eng J. https://​doi.​org/​10.​ Sustainable Production Consumption 26:78–88. https://​doi.​org/​
1016/j.​cej.​2020.​125878 10.​1016/j.​spc.​2020.​09.​013

	42.	 Suparmaniam U, Shaik NB, Lam MK, Lim JW, Uemura Y, Shuit 	59.	 Heikkilä L, Reinikainen A, Katajajuuri J-M, Silvennoinen K, Har-
SH, Show PL, Tan IS, Lee KT (2022) Valorization of fish bone tikainen H (2016) Elements affecting food waste in the food ser-
waste as novel bioflocculant for rapid microalgae harvesting: vice sector. Waste Manage 56:446–453. https://d​ oi.o​ rg/1​ 0.1​ 016/j.​
Experimental evaluation and modelling using back propagation wasman.​2016.​06.​019
artificial neural network. J Water Process Eng. https://d​ oi.o​ rg/1​ 0.​ 	60.	 Wang L, Yang Y, Wang G (2022) The clean your plate campaign: 
1016/j.​jwpe.​2022.​102808 resisting table food waste in an unstable world. Sustainability. 

	43.	 Jiang Y, Huang J, Luo W, Chen K, Yu W, Zhang W, Huang https://​doi.​org/​10.​3390/​su140​84699
C, Yang J, Huang Y (2023) Prediction for odor gas generation 	61.	 Montecinos J, Ouhimmou M, Chauhan S, Paquet M (2018) Fore-
from domestic waste based on machine learning. Waste Manag casting multiple waste collecting sites for the agro-food industry. 
156:264–271. https://​doi.​org/​10.​1016/j.​wasman.​2022.​12.​006 J Cleaner Production 187:932–939. https://d​ oi.o​ rg/1​ 0.1​ 016/j.j​clep​

	44.	 You H, Ma Z, Tang Y, Wang Y, Yan J, Ni M, Cen K, Huang ro.​2018.​03.​127
Q (2017) Comparison of ANN (MLP), ANFIS, SVM, and RF 	62.	 Bureau GUMaCLE (2022) Announcement of Guangzhou 
models for the online classification of heating value of burning Municipal Bureau of Urban Management and Comprehensive 
municipal solid waste in circulating fluidized bed incinerators. Law Enforcement on the results of the sampling survey on the 

1 3



2	 456 Journal of Material Cycles and Waste Management (2023) 25:2442–2456

composition and nature of domestic waste in Guangzhou in 2021. 	66.	 Fang X, Gao B, Zhong D, Wang L, Borrion A, Huang W, Xu S, 
http://​cg.​gz.​gov.​cn/​zwgk/​tzgg/​conte​nt/​post_​81865​88.​html Cui S (2023) Closing the food waste loop: Analysis of the agro-

	63.	 Song G, Semakula HM, Fullana-i-Palmer P (2018) Chinese house- nomic performance and potential of food waste disposal products. 
hold food waste and its’ climatic burden driven by urbanization: J Cleaner Product. https://d​ oi.o​ rg/1​ 0.1​ 016/j.j​clepr​o.2​ 022.1​ 35174
a bayesian belief Network modelling for reduction possibilities 
in the context of global efforts. J Cleaner Product 202:916–924. Publisher's Note  Springer Nature remains neutral with regard to 
https://​doi.​org/​10.​1016/j.​jclep​ro.​2018.​08.​233 jurisdictional claims in published maps and institutional affiliations.

	64.	 Ogunmoroti A, Liu M, Li M, Liu W (2022) Unraveling the envi-
ronmental impact of current and future food waste and its manage- Springer Nature or its licensor (e.g. a society or other partner) holds 
ment in Chinese provinces. Resources, Environment and Sustain- exclusive rights to this article under a publishing agreement with the 
ability. https://​doi.​org/​10.​1016/j.​resenv.​2022.​100064 author(s) or other rightsholder(s); author self-archiving of the accepted 

	65.	 Wen Z, Wang Y, De Clercq D (2015) Performance evaluation manuscript version of this article is solely governed by the terms of 
model of a pilot food waste collection system in Suzhou City. such publishing agreement and applicable law.
China J Environ Manage 154:201–207. https://d​ oi.o​ rg/1​ 0.1​ 016/j.​
jenvm​an.​2015.​02.​025

Authors and Affiliations

Jiehong Tang1,2 · Yuting Tang1,2   · Yupeng Liu3,4 · Hanchen Su1,2 · Yuxuan Zhang1,2 · Ziwei Sun1,2 · Xiaoqian Ma1,2

* 	 Yuting Tang 3	 Key Lab of Urban Environment and Health, Institute 
	 tangyuting_43@163.com of Urban Environment, Chinese Academy of Sciences, 

Xiamen 361021, Fujian, China
1	 School of Electric Power, South China University 4

of Technology, Guangzhou 510640, China 	 Xiamen Key Lab of Urban Metabolism, Xiamen 361021, 
Fujian, China

2	 Guangdong Province Key Laboratory of Efficient and Clean 
Energy Utilization, Guangzhou 510640, China

1 3