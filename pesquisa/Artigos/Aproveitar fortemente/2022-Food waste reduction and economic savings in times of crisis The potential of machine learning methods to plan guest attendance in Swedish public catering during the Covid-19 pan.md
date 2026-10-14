---
source_file: "2022-Food waste reduction and economic savings in times of crisis The potential of machine learning methods to plan guest attendance in Swedish public catering during the Covid-19 pan.txt"
original_rel_path: "Trabalhos\Artigos\Aproveitar fortemente\txt\2022-Food waste reduction and economic savings in times of crisis The potential of machine learning methods to plan guest attendance in Swedish public catering during the Covid-19 pan.txt"
category: "Artigos_Aproveitar_fortemente"
extension: ".txt"
sha256: "65d0408e0b5c28fbb7f76c613c75052d80508e84a4c16483c7cb421b68439fe2"
extracted_at: "2026-09-19T23:16:59.184937"
---

﻿Socio-Economic Planning Sciences 82 (2022) 101041

Contents lists available at ScienceDirect 

Socio-Economic Planning Sciences 
journal homepage: http://www.elsevier.com/locate/seps 

Food waste reduction and economic savings in times of crisis: The potential 
of machine learning methods to plan guest attendance in Swedish public 
catering during the Covid-19 pandemic⋆ 

Christopher Malefors a,*, Luca Secondi b, Stefano Marchetti c, Mattias Eriksson a 

a Department of Energy and Technology, Swedish University of Agricultural Science, Box 7032, 75007, Uppsala, Sweden 
b Department for Innovation in Biological, Agro-Food and Forest Systems (DIBAF), University of Tuscia, Via S.Camillo De Lellis, Snc, Viterbo (Vt), 01100, Italy 
c Department of Economics and Management, University of Pisa, Via Ridolfi 10, Pisa, 56124, Italy   

A R T I C L E  I N F O   A B S T R A C T   

Keywords: Food waste is a significant problem within public catering establishments in any normal situation. During spring 
Food waste school kitchens forecasting 2020 the Covid-19 pandemic placed the public catering system under greater pressure, revealing weaknesses 
random-forest system optimization within the system and generation of food waste due to rapidly changing consumption patterns. In times of crisis, 

it is especially important to conserve resources and allocate existing resources to areas where they can be of most 
use, but this poses significant challenges. This study evaluated the potential of a forecasting model to predict 
guest attendance during the start and throughout the pandemic. This was done by collecting data on guest 
attendance in Swedish school and preschool catering establishments before and during the pandemic, and using a 
machine learning approach to predict future guest attendance based on historical data. Comparison of various 
learning methods revealed that random forest produced more accurate forecasts than a simple artificial neural 
network, with conditional mean absolute prediction error of <0.15 for the trained dataset. Economic savings 
were obtained by forecasting compared with a no-plan scenario, supporting selection of the random forest 
approach for effective forecasting of meal planning. Overall, the results obtained using forecasting models for 
meal planning in times of crisis confirmed their usefulness. Continuous use can improve estimates for the test 
period, due to the agile and flexible nature of these models. This is particularly important when guest attendance 
is unpredictable, so that production planning can be optimized to reduce food waste and contribute to a more 
sustainable and resilient food system.   

1. Introduction The global food system is a major driver of land use change [2,3], 
depletion of freshwater resources [4,5], climate change [6,7], and 

The Covid-19 pandemic revealed an urgent need to investigate how pollution of aquatic and terrestrial ecosystems through excessive nitro
the food supply chain reacts during a crisis, when it is necessary to save gen and phosphorus inputs [8–10]. The current steep trajectories of 
resources and allocate them to where they are most needed [1]. The food population and consumption growth further increase the importance of 
system is currently under stress on all levels, from food service provider finding solutions that can meet food demand in a sustainable fashion 
to farms. This requires the system to be quite robust and sufficiently [11]. Five major areas have been identified as possible ways of achieving 
flexible to allow swift changes due to rapidly changing consumption a sustainable food system by 2050 [12]. However, predicted climate 
patterns, in order to avoid building large imbalances into the system that change will alter the conditions for food production and future crises of 
eventually generate shortage of food in some places and food waste in different types that impact food supply and food consumption in one 
others. Only by reducing these imbalances can the food system develop way or another are likely, so it is highly important to understand effects 
in a sustainable way, ensuring food security without unnecessary arising from disruptive events, like the Covid-19 pandemic. Unlike many 
resource consumption. other countries, Sweden did not close down preschools and primary 

⋆ The article was handled by Editor in Chief, Vedat Verter 
* Corresponding author. 

E-mail address: christopher.malefors@slu.se (C. Malefors).  

https://doi.org/10.1016/j.seps.2021.101041 
Received 17 December 2020; Received in revised form 17 February 2021; Accepted 23 February 2021   
Available online 2 March 2021
0038-0121/© 2021 The Author(s). Published by Elsevier Ltd. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).



C. Malefors et al.                                                                                                                                                                                 S  o c  i o  - E  c o  n  o m   i c  P  l a  n  n  in  g   S  c i e n  c  es 82 (2022) 101041

schools in the initial phase of the Covid-19 pandemic. This created a possible on consumption patterns during the current crisis, in order to be 
somewhat unique situation where schools were open but had to apply prepared for the next crisis. 
restrictions, e.g., forcing pupils with the slightest symptoms to remain at 
home for at least two days after becoming symptom-free. This created a 2.1. Food planning, management and forecasting: the integration with a 
situation with much lower rates of guest attendance in school canteens statistical perspective 
than usual, potentially leading to large volumes of overproduction un
less the schools were agile enough to adjust their production swiftly. As The challenge of sustainable production and consumption can also 
the pandemic also led to illness among kitchen staff, the work envi act as a stimulus for enhancing the linkage between rational food 
ronment in canteens was likely to be more stressed than usual, making it planning and the use of statistical methods for obtaining accurate pre
unlikely that reducing food waste by saving and re-using leftovers was dictions of food production, therefore improving organization and 
prioritized. However, in times of crisis the food system needs to be management, and ultimately reducing food waste generation. 
resilient and not waste resources, but allocate them to where they are Food production is a complex process where uncertainty is relevant, 
most needed. Better forecasting of guest attendance has been suggested mainly due to stochastic supply and demand, and variability in raw 
as a way to reduce food waste in normal situations [13], but knowledge materials and ingredients [31]. This results in differences between 
is lacking on how feasible such forecasting is in abnormal situations. planned production and actual output, with important economic, social, 

The aim of this study was therefore to assess the accuracy with which and environmental impacts. 
a machine learning model could predict guest attendance in Swedish Several statistical methods and approaches for forecasting food 
primary school canteens during the initial phases of the Covid-19 production have been proposed in the literature, some specifically 
pandemic. The goal was to contribute to a more resilient and sustain referring to meal requirements in restaurants, catering services [32,33] 
able food system by developing knowledge on how to make production and the overall food service sector [34]. The importance of accurately 
planning more resource-efficient in times of crisis. predicting expected meal consumption in the overall hospitality sector 

has been highlighted by the Covid-19 pandemic [35]. Use of known past 
2. Consumption pattern and waste during crisis data for estimating and forecasting one or more future values in the data 

series would allow private managers and public bodies to plan the right 
Previous food waste studies of the hospitality sector report that amount of food to buy and produce, and to adjust staff levels so that food 

roughly 20% of food produced ends up as waste [14–20]. This should be can be prepared and served efficiently [36]. Time series forecasting 
considered the normal level, and could be expected to rise when con through regression models [37], operation research and machine 
sumption patterns and guest attendance shift rapidly. Little is known of learning methods [31], and the Prophet algorithm [36,38] have proven 
the situation during the initial phase of the Covid-19 pandemic, as sta to be useful for this purpose. 
tistics have not yet been compiled. However, in a normal situation The machine learning statistical framework of analysis has already 
public catering is a significant actor in Sweden, with approximately 50% been used for food waste management in the context of driver assess
of all midday meals in the food service sector served in the public sector ment for household food waste [39]. In this study, we specifically 
[21], by catering establishments in hospitals, preschools, schools, and focused on the potential of the random forest approach [40] for pre
elderly care units. School kitchens are the most significant actor in the dicting guest attendance and meal planning in Swedish public catering, 
public catering segment, with almost 1.3 million meals served to using an estimation strategy that first considered the overall available 
Swedish pupils every day throughout the school year. School meals are data and then data at kitchen level, as detailed in section 3. 
provided free of charge, funded by taxes [22]. Similar approaches to 
school meals are used in Finland [23] and Estonia [24]. Other countries 3. Material and methods 
serve also school meals, although at a cost to the guest, so the concept of 
school meals is widespread. In Sweden, planning for the number of The work was carried out in three steps: i) Collecting data on guest 
meals to serve is generally based on the number of pupils registered in attendance before and during the initial phase of the Covid-19 
the school, but despite these optimal conditions, fluctuations in canteen pandemic; ii) modeling number of guests using a machine learning 
guest numbers still occur. This is one of the risk factors for food waste approach; and iii) evaluating the model in relation to actual guest 
generation identified previously [25], since kitchen staff do not get attendance. 
timely information regarding the number of guests. 

Previous studies have also shown that kitchen staff and food service 3.1. Data 
providers generally add an extra margin in meal production [25,26] in 
order to avoid running out of food, which is seen as a negative outcome The complete dataset available for the analysis covered 18 primary 
in the eyes of the guests and a source of shame for kitchen staff. The school kitchens and 16 preschool kitchens in Sweden. These were 
problem is therefore two-fold; there is little knowledge about how many selected as suitable test subjects for forecasting models because they 
guests will turn up to a specific meal, and the kitchen needs to prepare were willing to share their data upon request and because most had data 
an acceptable margin of food to avoid shortages and loss of goodwill. available for several years prior to the pandemic. Sixteen of the primary 
Reduced food waste is important to decrease the environmental impacts schools and all of the preschools belonged to one municipality, while the 
from the food system, as it reduces the overall amount of food that needs remaining two schools belonged to two other municipalities. Thus, no 
to be produced [27–29]. United Nations Sustainable Development Goal random selection of units was performed. All of the selected kitchens 
(UN-SDG) 12.3 is to halve per-capita consumer and retail food waste by serve meals to pupils ranging in age from around 1 to 15 years. The 
2030, and to reduce food losses along production and supply chains. analysis focused on lunch, as this is the most commonly served meal in 
Several studies (e.g. Refs. [12,30]) cite significantly reduced food waste the selected kitchens, although breakfast and snacks may also be served. 
levels as a prerequisite for a sustainable food system in the future. A Swedish school year consists of at least 178 days between late August 
However, such studies provide few suggestions on how exactly to ach and early June [41]. The autumn semester includes one week of holiday 
ieve the transition to a more resource-efficient society. in late October/early November. A winter holiday of around three weeks 

In times of crisis and associated changes in food consumption pat covers the Christmas and new year period. The spring semester has one 
terns, the risk of food waste increases, since the food system is not agile holiday week in February and one week around Easter, plus scattered 
enough to adapt to rapid changes. The current pandemic may not occur national holidays from early May to June. Schools do not provide 
again, but society is likely to face future crises that impose stress on the teaching during holidays but often remain open to provide childcare for 
food system. It is therefore important to gain as much knowledge as younger pupils, and therefore serve meals during these periods. The 

2



C. Malefors et al.                                                                                                                                                                                 S  o c  i o  - E  c o  n  o m   i c  P  l a  n  n  in  g   S  c i e n  c  es 82 (2022) 101041

number of meals served during holidays is therefore lower than during 3.2.1. Machine learning-based models: the random forest approach 
ordinary school time. Preschools are kept open during holidays, but The classical machine learning approach is based on training and 
guest attendance can still be influenced if families with older siblings use testing data. The training data are used to tune a prediction model that is 
the school holidays for vacation. A typical school kitchen offers pupils able to correctly predict the test data. Here, the times series of data on 
two to three lunch options. The menu follows a five-to seven week cycle portions served in school canteens over time were split into two parts. 
of menus agreed at meetings between the heads of catering and public The first part of the time series was used as training data to tune a 
catering managers. This study focused on the initial phase of the machine learning model that could effectively predict the “last” part of 
Covid-19 pandemic in Sweden, which was defined as starting on March the series as accurately as possible. If the last part of the series was well 
18, 2020, when the Swedish government introduced a strategy for social fitted, this was taken as an indication of the capability of the model to 
distancing, including restrictions on school attendance, and ending on forecast portions in future unobserved time. 
June 9, 2020, which marked the official end of the spring semester. There are many different machine learning methods for forecasting 

Data on the number of guests eating school meals from 2010 to the time series. Those pre-tested in this study were artificial neural net
beginning of June 2020 were collected by the municipalities themselves, works, Poisson auto-regressive models, and random forests. The best 
by counting plates after every lunch. The reason for counting plates is results in terms of accuracy of predictions were obtained with the 
that this number is used for internal accounting, where the public random forest approach. 
catering organization charges the school organization for the lunches. Random forest is a tree-based method involving stratification or 
There are several methods for counting the number of plates. One in segmentation of the space of inputs into a number of simple regions. 
volves drawing tally marks on the dishwasher for each full tray, and then With the aim of making a prediction for a given observation, the mean of 
multiplying the total by the capacity of each tray (usually 18 plates). the training observations in the region to which it belongs is used. The 
Another approach is to collect one plate from each full tray and all plates set of splitting rules used to segment the predictor space can be sum
from the last incomplete tray and calculate the total number of plates. In marized in a tree, so these types of approaches are known as tree-based 
this study, it was assumed that one plate was equal to one portion, which methods. Since simple tree-based methods have proven not to be 
was equivalent to one guest. However, this might not necessarily be completely effective for prediction purposes, bagging, boosting, and 
accurate, since guests are allowed to re-fill their plate or take several random forest have been introduced. Each of these approaches involves 
plates. Plate data are thus an approximation of the number of guests producing multiple trees, which are then combined to yield a single 
served, since no point-of-sale data are available to extract information consensus prediction that is very effective [43]. A tree consists of a series 
regarding guest flow as the meals are free of charge to pupils. of splitting rules, starting at the top of the tree. The necessary steps for 

building trees can be summarized as follows:  
3.2. Machine learning-based models 

1. Use recursive binary splitting to grow a large tree on the training 
A strategy and methodology for forecasting guest attendance (por data, stopping only when each terminal node has fewer than some 

tions) for a given kitchen in Sweden were developed using a sub-set of minimum number of observations.  
the data covering the period August 2019–June 2020. The data collected 2. Apply cost complexity pruning to the large tree in order to obtain a 
by the kitchens were transformed into a standardized format similar to sequence of best sub-trees, as a function of α.  
that proposed by Ref. [42]. Since all field trips and other extracurricular 3. Use K-fold cross-validation to choose α. That is, divide the training 
activities were canceled during the pandemic, all holidays and extreme observations into K folds. For each k in 1 to K:  
values defined as falling outside the inter-quartile range per school and (a) Repeat Steps 1 and 2 on all but the kth fold of the training data.  
school semester were removed before entering the modeling step. This is (b) Evaluate the mean squared prediction error on the data in the 
because kitchens already have a good understanding of guest seasonality left-out kth fold, as a function of α.  
and of when guests will be missing due to upcoming holidays, but (c) Average the results for each value of α, and pick to minimize the 
struggle with the variability arising on normal weekdays. The intention average error.  
was for the filter to remove known features (such as holidays and known 4. Return the sub-tree from Step 2 that corresponds to the chosen value 
study visits in the period prior to the pandemic) from the dataset, in of α. 
order to focus on the modeling aspects. 

With the filter in place, a strategy for estimation going from the The recursive binary splitting step (point 1) consists of selecting the 
pooled data set to the single kitchen data was applied. First, the models input Xj and the cut-point s such that splitting the input space into the 
were calculated by considering all kitchens and an attempt was made to regions {X||Xj < s} and {X||Xj ≥ s} leads to the greatest possible reduc
forecast number of portions using only school and kitchen features. tion in the residual sum of squares (RSS) of the output. That is, all inputs 
Second, some features relating to the pandemic crisis in Sweden were X1,…,Xp and all possible values of the cut-point s for each of the inputs 
added. Two kitchens were selected as examples, both serving food in are considered, and then the input and cut-point giving the tree with the 
primary schools, the first to children aged 6–12 years (Kitchen 1) and the lowest RSS are chosen. Without loss of generality, for any j and s, the 
second to children aged 6–9 years (Kitchen 2). The set of features can be following pair of half-planes are defined: 
denoted as inputs (predictors or independent variables), which are { } { }
measured or pre-set and have some influence on one or more outputs R1(j, s)= X||Xj < s and R2(j, s) = X||Xj ≥ s (1)  
(responses or dependent variables). The goal is generally to use the in
puts to predict the values of the outputs. This type of approach is called by searching the value of j and s that minimize the following quantity: 
supervised learning. The opposite is “unsupervised learning”, where ( )

∑ 2 ( )
∑ 2

there are only features and no measurement of outcome. The target in yi − ŷR + yi − ŷR (2)  
1 2

this step of the present work was to forecast guest attendance through i:xi⊆R1(j,s) i:xi⊆R2(j,s)

number of portions, and therefore a machine learning approach was 
used. Machine learning approaches are designed to make the most ac where ŷRi is the mean output for the training observations in Ri(j,s). The 
curate predictions possible, whereas statistical approaches are designed last split regions are called terminal nodes. Let the large tree built as 
to allow inferences about the relationships between variables to be described above (point 1) be T0. This tree can over-fit the data, obtaining 
drawn. poor performance predicting in predicting the test data. Therefore, it is 

pruned back to obtain a sub-tree in such a way that minimizes the error 
in the test data. This procedure is carried out through the complexity 

3



C. Malefors et al.                                                                                                                                                                                 S  o c  i o  - E  c o  n  o m   i c  P  l a  n  n  in  g   S  c i e n  c  es 82 (2022) 101041

pruning step (point 2) described above. For a sequence of trees indexed For series which includes yt = 0 this measure cannot be used. An 
by a non-negative tuning parameter α, each α has a sub-tree T⊂ T0 to alternative approach is to compute conditional MAPE (cMAPE) for 
minimize: yt ∕= 0, 

∑|T |
( )

∑ 2 ∑T (⃒ ⃒/ )
⃒ ⃒

yi − ŷR + α|T| (3)  cMAPE =T − 1 ⃒ ⃒
⃒yt − ŷt⃒ yt I(y

m t ∕= 0) (6)  
m=1 xi⊆Rm t=1

where |T| represents the absolute number of terminal nodes of the tree T where I(y∕= 0) is an indicator function equal to one when yt ∕= 0, and 
and Rm is the region corresponding to the mth terminal node. 0 otherwise. To compare the prediction power of the random forest 

Construction of trees following the procedure described above suf between the kitchens, the coefficient of variation (CV) was calculated as 
fers from a high level of variability. From the perspective of reducing the ratio between the square root of MSE and mean number of portions 
dispersion, and therefore the uncertainty of the estimates, the use of served in the relevant period. 
bootstrap aggregation (also called bagging) leads to a consistent With the aim of evaluating the practical implications and impact of 
reduction in the variance through the basic rule that averaging a set of our models and their usefulness in reducing economic, environmental 
observations leads to a reduction in variability. As a result, a natural way (and social) impacts related to food waste, we estimated the economic 
to reduce the variance, and therefore increase the prediction accuracy of costs (and the associated savings) for the individual kitchen in three 
a statistical learning method, is to take a large number of samples from different scenarios:  
the training set, build separate prediction models using each sample, and 
average the resulting predictions. i. A “no-plan” scenario, representing a situation in which each 

In addition to bagged trees, random forests provide an improvement kitchen prepares every day a number of meals equal to the total 
by de-correlating the trees. Similarly to bagging, a number of decision number of pupils enrolled.  
trees is built on bootstrapped training samples, by considering each time ii. An “actual” scenario, representing the actual number of meals 
a split in a tree, i.e., a random sample of l inputs chosen as split candi served, with the costs computed based on the daily information 
dates from the full set of p inputs. The split can be used only on those l available in the dataset.  
inputs. A fresh sample of l predictors is taken at each split, typically iii. A “forecast” scenario, representing the number of meals forecast 
setting l √̅

≈ p̅̅. This method, even though it sounds counter-intuitive, by our random forest model. 
leads to construction of uncorrelated trees, thus greatly reducing the 
variance by averaging them. In contrast, the bagging method may build By assigning to each meal a cost of 2 Euros (corresponding to 22 
many correlated trees, which does not lead to a reduction in variance. Swedish krona, the average cost per meal in the municipalities in 2019), 
Variance of the average of B identically distributed random variables is we computed the progressive cumulative sum of costs for preparation of 
ρσ2 + B− 1(1 − ρ)σ2, where ρ is the pairwise correlation coefficient and meals on each of the days in the test period. This value represented a first 
σ2 is the variance of a variable. measure of the total costs incurred by kitchens in the three different 

The algorithm for the random forest approach can be summarized in scenarios. We then compared the three daily series of costs both by 
the following steps:  analyzing the differences between the actual scenario and the forest 

scenario, and by comparing each of these two series with the no-plan 
1. For b scenario. The median Absolute Relative Bias (ARB) was used for this 

= 1 to B:  
(a) Draw a bootstrap sample of size N from the training data.  purpose and was calculated as the relative difference between the daily 
(b) Grow a random-forest tree T actual and predicted economic values. 

b to the bootstrapped data, by 
recursively repeating the following steps for each terminal node 
of the tree, until the minimum node size is reached. Then:  4. Results 

i. Select l inputs at random from the p inputs.  
ii. Pick the best input/split-point among the l.  4.1. Guest attendance during the pandemic 

iii. Split the node into two daughter nodes.  
2. Output the ensemble of trees Tb, b = 1,…,B. Fig. 1 displays changes over time in the number of guests in all school 

kitchens studied, and the deviation in the number of guests during the 
B pandemic in contrast to before the pandemic. Three periods are shown 

As a result, a prediction for a given point x is obtained as f̂ rf (x) = in the diagram, the time before the pandemic, the initial stage of the 
B− 1ΣB

b=1Tb(x). pandemic between 18 March (indicated by the dashed vertical line in 
Fig. 1) and the Easter holidays, and the steady state of the first wave 
from the Easter holidays to the summer holidays. The number of pupils 

3.3. Selected measures and tools for forecasting statistical and economic enrolled remained constant during the period, as this number normally 
validity does not change during the school year. However, the average attending 

school lunch was on average 181 pupils/day before the pandemic, 144 
To assess how well the test data were predicted through the trained pupils/day during the initial phase, and 185 pupils/day during the 

random forest, we calculated mean squared error (MSE), defined as: steady state. There was also a clear drop in guest attendance during the 
∑T ( )2 first day of the initial phase (i.e., 19 March), where the guest attendance 

MSE = T − 1 yt − ŷt (4)  was only 50% of that in previous weeks. However, this drop in guest 
t=1 attendance was short-lived; aggregated to weekly average, the drop in 

guest attendance in week 12 was only 25% compared with the previous 
where yt is the number of portions served the tth day and ŷt its pre week. However, this was still noticeable in comparison with the average 
diction, and T is the number of days in the test dataset. The lower the during the years prior to 2020, where a drop in guest attendance during 
MSE, the better the model. We also computed mean absolute prediction week 12 as not visible at all. 
error for the test and training dataset as: In the school canteens studied, the guest attendance during the 

∑T ⃒ ⃒
⃒ ⃒ steady state period was almost back to normal, although fewer pupils 

MAPE =T − 1 /
⃒
⃒yt − ŷ ⃒

t⃒ yt (5) than normal attended daycare in the Easter holiday (Fig. 1). This is in 
t=1 contrast to the preschools, where there was a clear drop in guest 

4



C. Malefors et al.                                                                                                                                                                                 S  o c  i o  - E  c o  n  o m   i c  P  l a  n  n  in  g   S  c i e n  c  es 82 (2022) 101041

Fig. 1. Average number of primary school meal guests over time on a weekly basis before and during the pandemic. ( ) indicates data for the school year 2019/ 
2020 and ( ) indicates data from previous school years (2010–2018). The dashed line is the day (18 March) when Sweden introduced guidelines for estab
lishments operating in the public catering sector. The shaded area ( ) indicates school breaks, with less activity. 

Fig. 2. Average number of preschool meal guests over time on a weekly basis before and during the pandemic. ( ) indicates data for the school year 2019/2020 
and ( ) indicates data from the previous school years (2010–2018). The dashed line is the day (18 March) when Sweden introduced guidelines for establishments 
operating in the public catering sector. The shaded area ( ) indicates school breaks, with less activity. 

attendance during both the initial phase and the steady state (Fig. 2). day (numerical, number of days in the year, e.g., 4 January is day 4, 28 
There were also fewer children attending preschool during the week of December is day 362), Quarter (categorical), Month (categorical), 
before Easter holiday (even though this is not an actual Easter holiday in Trend (numerical), Weekday (categorical, from Monday to Sunday), 
preschools, which is clear in the previous year). Weekend (categorical, yes, no), and Week (numerical, number of weeks 

in the year). The random forest model was fitted in the R environment 
[44], using the package randomForest [45]. Once we had estimated the 

4.2. Model specification, estimation, and validation model for the entire dataset, we concentrated on the two selected single 
kitchens with the aim of obtaining more accurate predictions. For the 

With the aim of showing the adequacy of the selected method and in two individual kitchens, we selected the inputs Holiday, Year day, 
order to achieve the objective of the present analysis, we first analyzed Month, Weekday, Weekend, and Week and assessed which were the 
the “pooled” dataset (i.e., the dataset summarizing, for each day, the most important in the final model. We drew a 500 bootstrap sample on 
total number of meals served in the 18 kitchens considered in the which we grew random forest trees, selecting at random two inputs from 
analysis) and then focused on single kitchens, carrying out separate among the six in the model. We then used the final random forest model 
analyses, estimates, and forecasting. to try to predict the test data. 

We started the estimation process by fitting a random forest with all 
the available inputs: Holiday (categorical with level Bank holiday, 
Vacation, Planning day, and None), Year (categorical, 2019, 2020), Year 

5



C. Malefors et al.                                                                                                                                                                                 S  o c  i o  - E  c o  n  o m   i c  P  l a  n  n  in  g   S  c i e n  c  es 82 (2022) 101041

Fig. 3. Time series of portions served by Kitchen 1 in the period 1 August 2019–30 June 2020.  

Fig. 4. Time series of school meal portions served by Kitchen 2 in the period 1 August 2019–30 June 2020.  

4.2.1. Definition of the training and testing datasets tuned the random forest model for each kitchen using the training data 
The results for the two individual kitchens, Kitchen 1 and Kitchen 2, and then used the model to predict the data in the test set. The test 

are displayed in Figs. 3 and 4, respectively. During the period covered by dataset for Kitchen 1 was set as 21 May-8 June 2020, since days after 8 
the analysis, the schools were closed to some extent during 73 vacation June had zero portions served. The test dataset for the Kitchen 2 covered 
days (where the school is open to provide childcare for some pupils), two the period 9–28 June 2020. The training dataset for Kitchen 1 covered 
planning days (where only teachers are present in the schools), 48 the period 1 August 2019–20 May 2020, while that for Kitchen 2 
weekends, and four bank holidays (where the school is completely covered the period 1 August 2019–8 June 2020. 
closed). The dataset had 125 missing days (mainly weekends) for 
Kitchen 1 and 119 for Kitchen 2, which were assigned a value of zero 4.2.2. Random forest estimation for the pooled data set and at kitchen level: 
school meal portions served. statistical and economic validation 

From Fig. 3, it can be seen that Kitchen 1 served zero portions during For the pooled dataset for all kitchens studied, MSE was equal to 
weekends and few portions in August, late October/early November, 59322 for the training data and 3036 for the test data. Conditional 
Christmas holidays, end of February, and middle of April. At the MAPE (cMAPE) was equal to 0.39 and 1.28 for training and test data, 
beginning of June, the number of portions served fell to zero (due to the respectively. The random forest approach was applied at kitchen level to 
kitchen closed down for summer holidays). On other days, the number of capture the characteristics and peculiarities of each series. This 
portions served varied between 154 and 209. approach made it possible to analyze in depth the statistical and eco

The series of portions served by Kitchen 2 was similar to that for nomic validity of the estimated models and to compare model perfor
Kitchen 1. The main difference was zero portions served during Christ mance for different daily series and kitchens. 
mas holidays and some portions served in June (Fig. 4) due to day care For the datasets at kitchen level, MSE for Kitchen 1 was around 609 
activities. In addition, Kitchen 2 served a lower number of daily por for the test data and 175 for the training data, and cMAPE was around 
tions, ranging between 44 and 75 during the normal period. 0.448 and 0.137 and for the training and test data, respectively. Using a 

We divided the series into two parts (training set and test set). We very simple neural network with one hidden layer, the MSE of the test 

6



C. Malefors et al.                                                                                                                                                                                 S  o c  i o  - E  c o  n  o m   i c  P  l a  n  n  in  g   S  c i e n  c  es 82 (2022) 101041

Fig. 5. Number of school meal portions served by Kitchen 1 from April 2020 to June 2020. Black line: observed data, red line: predicted data. (For interpretation of 
the references to colour in this figure legend, the reader is referred to the Web version of this article.) 

data was around 11600 and cMAPE was around 4.104. number of daily new Covid-19 cases in the municipality where the 
Fig. 5 shows the time series from April 2020 to June 8, 2020 (black kitchen was located and a dummy identifying days before or after March 

line) with the superimposed red line of the random forest predictions for 19, 2020, which corresponded to the beginning of the restrictions in 
the test data (21 May-8 June). As can be seen, the last 19 days of the Sweden. However, neither of these inputs improved the prediction 
series were rather well predicted by the model. Using more inputs power of the random forest model. 
related to socioeconomic contextual variables (such as characteristics of In an economic assessment, we computed the cumulative sum of 
the pupils attending the school) could probably improve the prediction kitchen costs for serving meals in the three different scenarios presented 
ability of the model. in section 3.3. Fig. 6 shows the distribution of meal costs over the test 

To assess whether older data improved the prediction power of the period for Kitchen 1 (May 21-June 8) on comparing the daily progressive 
random forest model, we tried to predict the same test data using meal costs in the no-plan scenario (dashed red line in Fig. 6), the actual 
training data on the number of portions served from August 1, 2017. For scenario (blue bars), and the forecast scenario (orange bars). Two 
Kitchen 1, the inputs Weekday and Weekend were initially the most different types of comparisons were carried between the three scenarios. 
important, followed by Holiday. Based on the relative importance of the The results confirmed the effectiveness of the forecasting method from 
metrics, we decided to build a final random forest model using the inputs an economic perspective. The expected cumulative costs for serving 
Holiday, Year, Day of the year, Month, Weekday, and Weekend. Using a meals in the entire test period were found to be 4454 Euros for the actual 
longer run (three years) changed the importance of the inputs, with (real) data and 4461 Euros for the forecast data. This demonstrated good 
Holiday being the most important input, followed by Weekdays and accuracy of prediction and high levels of economic savings (and dis
Weekend, while Month, Year and Day of the year were least important. tance) compared with the total costs that the kitchen would have 
The MSE of the test set was around 555, slightly better than obtained incurred if no planning (i.e. no-plan scenario) had been implemented 
using the model trained on a shorter run (one year, MSE = 609). (costs = 5382 Euros). 

We also checked whether including information on the pandemic The alignments between actual and forecast data also showed the 
stages improved the prediction power. To do this, we added two inputs: economic value of avoiding waste. In Fig. 6, the distance for each day 

Fig. 6. Results of economic scenario analysis for Kitchen 1. ( ) Sum of meal costs based on actual data. ( ) Sum of meal costs based on forecasted data. ( ) Sum 
of meal costs based on total enrolled students. 

7



C. Malefors et al.                                                                                                                                                                                 S  o c  i o  - E  c o  n  o m   i c  P  l a  n  n  in  g   S  c i e n  c  es 82 (2022) 101041

between the dashed red line (no-plan scenario) and the forecast scenario during this period the pattern of guest attendance was close to normal 
(orange bars) represents the costs avoided by adopting a machine- for the period, as if there were no pandemic going on at all. 
learning approach to forecasting meals. The total saving for Kitchen 1 In preschools, it was more apparent that there was a pandemic going 
was approximately 921 Euros, compared with approximately 928 Euros on, with guest attendance after the restrictions were announced down to 
saved from using the series of actual (real) data (blue bars). Median ARB around 70% of what would be expected based on the regular pattern 
was equal to 0.0884%, thus confirming the potential of the machine during April–June. Thus preschools seemed to suffer more long-lasting 
learning model for food planning and management. effects of the pandemic or the restrictions, probably due to three fac

Prediction using random-forest models was also performed for tors. First, school attendance is compulsory and it is actually illegal for 
Kitchen 2 (Fig. 7). Based on availability of data, the test data period was parents to keep pupils away from school if they are not sick, while there 
9–28 June 2020,1 after which there was a sharp decrease in the actual is no such legal obligation for preschool children. Second, younger 
number of meals served (see Fig. 4). The training set covered the period children are well-known for catching other corona viruses causing reg
1 August 2019–8 June 2020. Other inputs in the initial random forest ular colds and runny noses, which are normally not considered serious 
model were the same used for Kitchen 1, as were the inputs of the refined diseases, but affected children were restricted from attending preschool 
model (selected using the importance metric). during this period. Third, many parents were asked to simply stay at 

The MSE was around 19 for the training data and 107 for the test home with their children if possible (e.g., if they were on parental leave 
data, while cMAPE was 0.095 for the training data and 0.487 for the test with younger siblings), in order to prioritize preschool staff time for the 
data. children of key workers. 

Economic validation of meal forecasting for Kitchen 2 (Fig. 8) also It is probably impossible to predict changes in guest attendance 
revealed the overall discrete adherence between the cumulative sum of during the initial phase of a pandemic, but guest attendance after just a 
kitchen costs incurred during the test period, which was approximately few weeks of restrictions appeared to be fairly steady and predictable. In 
532 Euros based on the actual data (therefore the real costs of served both the schools and preschools studied, guest attendance followed the 
meals) and approximately 774 Euros based on the estimated random- pattern in the previous year, but with a slight shift downwards, espe
forest results. In contrast, the theoretical cost of meals in the no-plan cially in preschools. However, since this downshift seemed quite con
scenario was 2072 Euros. stant over the period, it must be considered predictable given that the 

Thus the total saving from predicting meals through the machine previous days set the level of the forecast. 
learning approach during the test data period (9–28 June 2020) was Introduction of a machine learning approach to predict guest 
approximately 1298 Euros, compared with 1540 Euros based on attendance in Swedish public catering proved to be an effective tool for 
observed data. It is worth noting that although we found greater over avoiding overcatering, and could therefore be used to reduce economic, 
estimation of number of meals served on the last days of the test data environmental, and social impacts of wasting food. Machine learning 
period, the average daily deviation from the costs of the no-plan scenario techniques have been shown previously to improve demand estimation 
(i.e., cooking meals for all pupils enrolled) amounted to 64 Euros for the compared with conventional multiple linear regression methods [46]. 
forecast values and 77 Euros for the actual values. The median ARB Specifically, the random forest learning method was found to be able to 
value (0.296) confirmed the high level of variability in the estimates, predict number of portions that kitchens had to serve in schools, setting 
with the first quarter of the differences having relative bias <0.15. a “safety margin” to avoid insufficient portions. However, some meth

The coefficient of variation (CV) for Kitchen 1 was 0.1186 and odological consideration must be resolved in future research to enable 
0.2106 for the training and test data, respectively, while for Kitchen 2 it deeper analysis. We found a good level of prediction power of the 
was 0.1165 and 0.7773, respectively. Thus, the CV of the training set random forest models from a statistical perspective and considerable 
was quite similar and small for both kitchens, indicating that the random amounts of economic savings from a strict economic perspective. We 
forest models were well trained. The CV of the test set was higher, also found quite a high level of uncertainty characterizing the test 
particularly for Kitchen 2. The cMAPE values showed similar trends. As period, particularly for Kitchen 2, which was characterized by a less 
can be seen in Fig. 7, the prediction line (red) was lagged with respect to standard daily series. This suggests a need not only to assess various 
the actual data (black line), so the prediction was not so good. It was types of models, but also to collect “auxiliary” information on e.g., the 
unclear whether this was related to pandemic-specific circumstances. school, pupils, and kitchen characteristics, to improve the accuracy of 
Unfortunately, adding inputs related to the pandemic (number of daily forecasting. 
new cases and the dummy) did not improve the prediction power of the The results could be viewed as very case-dependent, given that a 
model. future crisis would most likely not follow exactly the same pattern as the 

COVID-19 pandemic and that the Swedish public catering system is rare 
5. Discussion in a global perspective. However, certain aspects are general and should 

therefore make the results more generalizable. First, even though the 
Based on data on guest attendance for meals in school and preschool next pandemic will probably take a different shape, societies will have 

canteens, it is clear that the pandemic period started exactly after the experiences from the Covid-19 pandemic, and base restrictions and 
press conference announcing restrictions in Sweden. The day after this measures on these experiences. This happened already during the sec
press conference saw the lowest attendance of children during a normal ond wave of the Covid-19 pandemic (autumn 2020), when countries all 
week day in the schools and preschools studied. However, by the second over Europe were trying to restrict the spread of the virus in society, but 
day after the start of the restrictions guest attendance started rising without closing down schools, a similar approach to that applied in 
again and in the weeks just after the start of the restrictions the atten Sweden during spring 2020. Second, even though the concept of free 
dance in schools was almost back to normal, given that the time just school meals is rather rare, meals are served in school canteens in many 
before a holiday normally has a low level of guest attendance [13]. countries, and the forecasting techniques tested in this paper should be 
During the pandemic steady state phase between Easter holiday and applicable to other settings to increase the precision of predicting future 
summer holiday guest attendance went down, but it normally does so guest attendance. An interesting finding by Ref. [47] for the household 
especially during the weeks including national holidays in May. Thus sector was an observed reduction in levels of food waste during the 

pandemic in an Italian context, due to careful food planning and man
agement. However, those authors stress the important role of contextual 

1 Kitchen 2 served portions up to the end of June, so we attempted to predict variables in reducing food waste during a lockdown scenario, and their 
the last 20 days of available data. Kitchen 1 served portions until 8 June, ac findings are not easily transferable to other sectors of the food supply 
cording to our data. chain. 

8



C. Malefors et al.                                                                                                                                                                                 S  o c  i o  - E  c o  n  o m   i c  P  l a  n  n  in  g   S  c i e n  c  es 82 (2022) 101041

Fig. 7. Number of school meal portions served by Kitchen 2 from April 2020 to June 2020. Black line: observed data, red line: predicted data. (For interpretation of 
the references to colour in this figure legend, the reader is referred to the Web version of this article.) 

Fig. 8. Results of economic scenario analysis for Kitchen 2. ( ) Sum of meal costs based on actual data. ( ) Sum of meal costs based on forecasted data. ( ) Sum 
of meal costs based on total enrolled students. 

Based on the results in this paper, policy recommendations can be For the remainder of the pandemic period, it is likely that the normal 
formulated for a future situation where there are restrictions in society forecast could be applied with good precision. There might be a new 
to contain a pandemic, but where schools and preschools are kept open. slightly lower level, e.g., if some guests are prevented from attending the 
The main recommendation is use a forecasting tool before a crisis to lunch servings, but since this would be a known factor it should be 
avoid overproduction, but also to train the forecast on a normal situa possible to adjust the forecast based on these numbers. In the random 
tion. The situation in the first days of restrictions is difficult to predict, tree approach, pandemic or non-pandemic could be used as a parameter 
since it is highly dependent on people’s reactions and precautions, to better train the machine learning algorithm. In summary, a good 
rather than the actual number of infected individuals. During this forecasting tool is likely to predict guest attendance during a pandemic 
period, the best strategy would be to accept that too much food will be with good accuracy, but not during the initial phase, where production 
purchased and therefore shift the focus to handling this overproduction adjustments are also needed. One of the key aspects in implementing 
by re-using leftovers or preparing food in smaller batches, so as to adjust forecasting in kitchens is to achieve trust in the forecasts among the staff 
production more precisely, as recommended by the Swedish Food and have an acceptable margin in place. One major advantage that 
Agency in normal situations [48]. During this period, it would also be random forest or any other tree-based method provides is that they are 
good to adjust the forecast so that recent days weigh higher in the easy to explain [50], which can be one way of establishing trust in the 
predictions, or simply shift to a simple model using moving average or forecasts that they provide. Without trust in the information provided by 
similar models, as exemplified in Refs. [13,49]. In the case of under the forecast, it is unlikely to be used by the kitchen staff and therefore 
prediction, shortages will occur and a sufficient margin needs to be in potential benefits with a forecasting system are in vain. However, using 
place. Optimization of this margin is something that is described by a method that is explainable and not of a black box type might lower the 
Ref. [13] who also proposes a system where a backup stock is used to trust threshold and increase the likelihood of implementation and usage 
handle days when the forecast delivers an underprediction to meet de among end-users. Accurate and trusted forecasting is therefore a tool 
mand. Such a system would need to be evaluated to see if it has the that can be useful to prevent overproduction and increase sustainability 
desired food waste reduction effect. both before and during a pandemic. 

9



C. Malefors et al.                                                                                                                                                                                 S o c i o - E c o n o m i c  P l a n n in g  S c i e n c es 82 (2022) 101041

6. Conclusions [8] Cordell D, White S. Lifes bottleneck: sustaining the world’s phosphorus for a food 
secure future. Annu Rev Environ Resour 2014;39(1):161–88. https://doi.org/ 
10.1146/annurev-environ-010213-113300. 

It is impossible to forecast demand early during extreme events. [9] Robertson GP, Vitousek PM. Nitrogen in agriculture: balancing the cost of an 
Instead, the focus should be on dealing with surplus food or preparing essential resource. Annu Rev Environ Resour 2009;34(1):97–125. https://doi.org/ 
smaller batches during the initial phase of a pandemic or other extreme 10.1146/annurev.environ.032108.105046. 

[10] Diaz RJ, Rosenberg R. Spreading dead zones and consequences for marine 
event. However, after a short period into the Covid-19 pandemic a ecosystems. Science 2008;321(5891):926–9. https://doi.org/10.1126/ 
forecasting tool was able to predict guest attendance at preschool and science.1156401. 
primary school meals with accuracy. A random forest approach was [11] Godfray HCJ, Beddington JR, Crute IR, Haddad L, Lawrence D, Muir JF, Pretty J, 

found to predict guest attendance during the test period with a condi Robinson S, Thomas SM, Toulmin C. Food security: the challenge of feeding 9 
billion people. Science 2010;327(5967):812–8. https://doi.org/10.1126/ 

tional absolute mean error of 0.448–0.487 on kitchen level. The most science.1185383. 
important factors for the accuracy of the forecast were found to be [12] Springmann M, Clark M, Mason-D’Croz D, Wiebe K, Bodirsky BL, Lassaletta L, de 
weekday and weekend, while number of daily new Covid-19 cases had Vries W, Vermeulen SJ, Herrero M, Carlson KM, Jonell M, Troell M, DeClerck F, 

Gordon LJ, Zurayk R, Scarborough P, Rayner M, Loken B, Fanzo J, Godfray HCJ, 
no prediction power in the model. The potential savings from use of Tilman D, Rockström J, Willett W. Options for keeping the food system within 
random tree forecasting was found to be 921–1298 Euros compared with environmental limits. Nature 2018;562(7728):519–25. https://doi.org/10.1038/ 
a situation where a meal is cooked for every pupil enrolled in schools. s41586-018-0594-0. 

[13] Malefors C, Strid I, Hansson P-A, Eriksson M. Potential for using guest attendance 
Random forest forecasting appears therefore to be a suitable tool for forecasting in Swedish public catering to reduce overcatering. Sustainable 
implementing in public catering in order to reduce food waste and Production and Consumption 2021;25:162–72. https://doi.org/10.1016/j. 
contribute to a more sustainable food system. spc.2020.08.008. 

[14] Boschini M, Falasconi L, Giordano C, Alboni F. Food waste in school canteens: a 
reference methodology for large-scale studies. J Clean Prod 2018;182:1024–32. 

CRediT authorship contribution statement https://doi.org/10.1016/j.jclepro.2018.02.040. 
[15] Byker CJ, Farris AR, Marcenelle M, Davis GC, Serrano EL. Food waste in a school 

nutrition program after implementation of new lunch program guidelines. J Nutr 
Christopher Malefors: Conceptualization, Methodology, Software. Educ Behav 2014;46(5):406–11. https://doi.org/10.1016/j.jneb.2014.03.009. 

Resources, Data Curation, Formal analysis, Writing - review & editing. [16] Engström R, Carlsson-Kanyama A. Food losses in food service institutions examples 
Luca Secondi: Conceptualization, Methodology, Software, Data Cura from Sweden. Food Pol 2004;29(3):203–13. https://doi.org/10.1016/j. 

tion, Formal analysis, Writing - review & editing. Stefano Marchetti: foodpol.2004.03.004. 
[17] Falasconi L, Vittuari M, Politano A, Segrè A. Food waste in school catering: an 

Methodology, Software, Data Curation, Formal analysis, Writing - re Italian case study. Sustainability 2015;7(11):14745–60. https://doi.org/10.3390/ 
view & editing. Mattias Eriksson: Conceptualization, Methodology, su71114745. 
Software, Resources, Data Curation, Formal analysis, Writing - review & [18] Malefors C, Callewaert P, Hansson P-A, Hartikainen H, Pietiläinen O, Strid I, 

Strotmann C, Eriksson M. Towards a baseline for food-waste quantification in the 
editing. hospitality sector—quantities and data processing criteria. Sustainability 2019;11 

(13):3541. https://doi.org/10.3390/su11133541. 
Declaration of competing interest [19] Eriksson M, Osowski CP, Malefors C, Björkman J, Eriksson E. Quantification of food 

waste in public catering services – a case study from a Swedish municipality. Waste 
Manag 2017;61:415–22. https://doi.org/10.1016/j.wasman.2017.01.035. 

The authors declare that they have no known competing financial [20] Eriksson M, Malefors C, Bergström P, Eriksson E, Osowski CP. Quantities and 
interests or personal relationships that could have appeared to influence quantification methodologies of food waste in Swedish hospitals. Sustainability 

2020;12(8):3116. https://doi.org/10.3390/su12083116. 
the work reported in this paper. [21] Swedish National Food Agency, Fakta om offentliga måltider 2019 - kartläggning 

av matsvinn i kommunalt drivna förskolor, skolor och äldreboenden., 
Acknowledgements Livsmedelsverkets rapportserie, Uppsala. 

[22] Swedish Parliament, Svensk författningssamling, Skollag (school law) 201 0:800. 
[23] Tikkanen I, Urho U-M. Free school meals, the plate model and food choices in 

This work was supported by H2020 ERA-net Cofund on Sustainable Finland. Br Food J 2009;111(2):102–19. https://doi.org/10.1108/ 
Food Production and Consumption (SUSFOOD2) by the Swedish 00070700910931940. 

Research Council for Sustainable Development (Formas), grant number [24] Ministry of Education and Research of the Republic of Estonia. Pre-school, basic 
and secondary education. Estonian Ministry of Education and Research 2019. http 

FR-2018/0001. s://www.hm.ee/en/activities/pre-school-basic-and-secondary-education. accessed 
2020-01-24. 

References [25] Steen H, Malefors C, Röös E, Eriksson M. Identification and modelling of risk 
factors for food waste generation in school and pre-school catering units. Waste 
Manag 2018;77:172–84. https://doi.org/10.1016/j.wasman.2018.05.024. 

[1] Ocampo L, Yamagishi K. Modeling the lockdown relaxation protocols of the [26] Boschini M, Falasconi L, Cicatiello C, Franco S. Why the waste? a large-scale study 
philippine government in response to the COVID-19 pandemic: an intuitionistic on the causes of food waste at school canteens. J Clean Prod 2020;246:118994. 
fuzzy DEMATEL analysis. Soc Econ Plann Sci 2020;72:100911. https://doi.org/ https://doi.org/10.1016/j.jclepro.2019.118994. 
10.1016/j.seps.2020.100911. [27] Bajželj B, Richards KS, Allwood JM, Smith P, Dennis JS, Curmi E, Gilligan CA. 

[2] Foley JA. Global consequences of land use. Science 2005;309(5734):570–4. Importance of food-demand management for climate mitigation. Nat Clim Change 
https://doi.org/10.1126/science.1111772. 2014;4(10):924–9. https://doi.org/10.1038/nclimate2353. 

[3] Newbold T, Hudson LN, Hill SLL, Contu S, Lysenko I, Senior RA, Börger L, [28] Foley JA, Ramankutty N, Brauman KA, Cassidy ES, Gerber JS, Johnston M, 
Bennett DJ, Choimes A, Collen B, Day J, Palma AD, Díaz S, Echeverria-Londoño S, Mueller ND, O’Connell C, Ray DK, West PC, Balzer C, Bennett EM, Carpenter SR, 
Edgar MJ, Feldman A, Garon M, Harrison MLK, Alhusseini T, Ingram DJ, Itescu Y, Hill J, Monfreda C, Polasky S, Rockström J, Sheehan J, Siebert S, Tilman D, 
Kattge J, Kemp V, Kirkpatrick L, Kleyer M, Correia DLP, Martin CD, Meiri S, Zaks DPM. Solutions for a cultivated planet. Nature 2011;478(7369):337–42. 
Novosolov M, Pan Y, Phillips HRP, Purves DW, Robinson A, Simpson J, Tuck SL, https://doi.org/10.1038/nature10452. 
Weiher E, White HJ, Ewers RM, Mace GM, Scharlemann JPW, Purvis A. Global [29] Garnett T. Where are the best opportunities for reducing greenhouse gas emissions 
effects of land use on local terrestrial biodiversity. Nature 2015;520(7545):45–50. in the food system (including the food chain)? Food Pol 2011;36:S23–32. https:// 
https://doi.org/10.1038/nature14324. doi.org/10.1016/j.foodpol.2010.10.010. 

[4] Shiklomanov IA. World water resources at the beginning of the twenty-first [30] J. O. Karlsson, G. Carlsson, M. Lindberg, T. Sjunnestrand, E. Röös, Designing a 
century. Cambridge, UK New York: Cambridge University Press; 2003. future food vision for the nordics through a participatory modeling approach, 

[5] Wada Y, van Beek LPH, van Kempen CM, Reckman JWTM, Vasak S, Bierkens MFP. Agron Sustain Dev 38 (6). doi:10.1007/s13593-018-0528-0. 
Global depletion of groundwater resources. Geophys Res Lett 2010;37(20). n/a–n/ [31] Garre A, Ruiz MC, Hontoria E. Application of machine learning to support 
a, 10.1029/2010gl044571. production planning of a food industry in the context of waste generation under 

[6] Edenhofer O, editor. Climate change 2014 : mitigation of climate change : working uncertainty. Operations Research Perspectives 2020;7:100147. https://doi.org/ 
group III contribution to the fifth assessment report of the intergovernmental panel 10.1016/j.orp.2020.100147. 
on climate change. New York, NY: Cambridge University Press; 2014. [32] Lasek A, Cercone N, Saunders J. Restaurant sales and customer demand 

[7] Vermeulen SJ, Campbell BM, Ingram JS. Climate change and food systems. Annu forecasting: literature survey and categorization of methods. In: Smart city 360◦. 
Rev Environ Resour 2012;37(1):195–222. https://doi.org/10.1146/annurev- Springer International Publishing; 2016. p. 479–91. https://doi.org/10.1007/978- 
environ-020411-130608. 3-319-33681-7_40. 

10



C. Malefors et al.                                                                                                                                                                                 S  o c  i o  - E  c o  n  o m   i c  P  l a  n  n  in  g   S  c i e n  c  es 82 (2022) 101041

[33] Blecher L, Yeh RJ. Forecasting meal participation in university residential dining [48] Swedish National Food Agency. Handbok för minskat matsvinn - för verksamheter 
facilities. J Foodserv Bus Res 2008;11(4):352–62. https://doi.org/10.1080/ inom vård. skola och omsorg.; 2020. 
15378020802519637. [49] Malefors C. Food waste in the food service sector - quantities, risk factors and 

[34] Miller JL, A Thompson P, Orabella M. Forecasting in foodservice: model reduction strategies, Lic thesis. Swedish University of Agricultural Sciences; 2021, 
development, testing, and evaluation. J Am Diet Assoc 1991;91(5):569–74. ISBN 978-9 1-576-9828-5. 

[35] Filimonau V. The prospects of waste management in the hospitality sector post [50] James G, Witten D, Hastie T, Tibshirani R. An introduction to statistical learning. 
COVID-19, Resources. Conserv Recycl 2020:105272doi. https://doi.org/10.1016/ Springer-Verlag GmbH; 2017. URL, https://www.ebook.de/de/product/2029 
j.resconrec.2020.105272. 2548/gareth_james_daniela_witten_trevor_hastie_robert_tibshirani_an_intro 

[36] Yurtsever M, Tecim V. Forecasting meal requirements using time series methods in duction_to_statistical_learning.html. 
organization. In: Economic and financial challenges for balkan and eastern 
European countries. Springer International Publishing; 2020. p. 243–54. https:// 
doi.org/10.1007/978-3-030-39927-6_15. Christopher Malefors is a PhD-candidate in the Department of Energy and Technology at 

[37] Ryu K, Sanchez A. The evaluation of forecasting methods at an institutional the Swedish University of Agricultural Sciences. He received his M. Sc in Sociotechnical 
foodservice dining facility. J Hospit Financ Manag 2003;11(1):27–45. https://doi. Systems Engineering from Uppsala University. His research interest include system opti
org/10.1080/10913211.2003.10653769. mization and understanding of establishments working in the food service sector with 

[38] S. J. Taylor, B. Letham, Forecasting at scaledoi:10.7287/peerj.preprints.3190v2. focus on food waste reduction measures. 
[39] Grainger MJ, Aramyan L, Piras S, Quested TE, Righi S, Setti M, Vittuari M, 

Stewart GB. Model selection and averaging in the assessment of the drivers of Luca Secondi is Associate Professor of Economic Statistics at the University of Tuscia 
household food waste to reduce the probability of false positives. PloS One 2018;13 (Viterbo– Italy). Since November 2019 he has been appointed as Rector’s Delegate for 
(2):e0192075. https://doi.org/10.1371/journal.pone.0192075. national and international ranking. He obtained the PhD in Applied Statistics at the Uni

[40] Amit Y, Geman D. Shape quantization and recognition with randomized trees. versity of Florence and was visiting researcher at the American University (Washington- 
Neural Comput 1997;9(7):1545–88. https://doi.org/10.1162/neco.1997.9.7.1545. DC), the Shanxi and Jiangxi universities (China) and the University of Castilla-La Mancha 

[41] Swedish Parliament. Svensk författningssamling. Skolförordningen 2011:185. (Spain). His main research interests cover the area of consumer behaviour especially 
[42] Eriksson M, Osowski CP, Björkman J, Hansson E, Malefors C, Eriksson E, Ghosh R. regarding food waste and circular economy issues. Starting from November 2020 he 

The tree structure — a general framework for food waste quantification in food participates as task leader and supports the coordination of the HORIZON-2020 LOW
services. Resour Conserv Recycl 2018;130:140–51. https://doi.org/10.1016/j. INFOOD project. 
resconrec.2017.11.030. 

[43] Hastie T, Tibshirani R, Friedman J. The elements of statistical learning. Springer- Stefano Marchetti is Associate Professor at the University of Pisa, he holds a PhD in 
Verlag New York Inc.; 2009. URL, https://www.ebook.de/de/product/ Applied Statistics from the University of Florence (2009). He spent a visiting period at the 
8023140/trevor_hastie_robert_tibshirani_jerome_friedman_the_elements_of_statistic Centre for Census and Survey Research, University of Manchester. He is member of the 
al_learning.html. International Association of Survey Statisticians, the Italian Statistical Society. and the 

[44] R Core Team R. A language and environment for statistical computing. Vienna, Dagum Centre on Advanced Statistics for Equitable and Sustainable Development. He is 
Austria: R Foundation for Statistical Computing; 2020. URL, https://www.R-pro Associate Editor for PLOS One and Journal of Statistics: Advances in Theory and Appli
ject.org/. cations. His research focus mainly on small area estimation. He participated to H220 and 

[45] Liaw A, Wiener M. Classification and regression by randomforest. R News 2002;2 FP7 projects. 
(3):18–22. URL, https://CRAN.R-project.org/doc/Rnews/. 

[46] Nair DJ, Rashidi TH, Dixit VV. Estimating surplus food supply for food rescue and 
delivery operations. Soc Econ Plann Sci 2017;57:73–83. https://doi.org/10.1016/j. Mattias Eriksson works as an associate professor at the Department of Energy and 
seps.2016.09.004. Technology at the Swedish University of Agricultural Science in Uppsala. He received a 

[47] Principato L, Secondi L, Cicatiello C, Mattia G. Caring more about food: the PhD in technology 2015 for his thesis titled Supermarket food waste - Prevention and man
unexpected positive effect of the covid-19 lockdown on household food agement with the focus on reduced waste for reduced carbon footprint. The focus of Erikssons 
management and waste. Soc Econ Plann Sci 2020:100953doi. https://doi.org/ research, teaching and outreach has been on sustainable food systems and especially food 
10.1016/j.seps.2020.100953. waste and life cycle assessment of agricultural products and waste management systems. 

11