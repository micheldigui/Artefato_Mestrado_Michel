---
source_file: "2021-preventing-food-waste-in-subsidy-based-university-dining-systems-an-artificial-neural-network-aided.txt"
original_rel_path: "Trabalhos\Artigos\Aproveitar fortemente\txt\2021-preventing-food-waste-in-subsidy-based-university-dining-systems-an-artificial-neural-network-aided.txt"
category: "Artigos_Aproveitar_fortemente"
extension: ".txt"
sha256: "eca10f38186b864735b07ab3bcf308e3290faa840267d6a6bab8e627bd1c046d"
extracted_at: "2026-09-19T23:16:59.179723"
---

﻿1017974WMR0010.1177/0734242X211017974Waste Management & ResearchFaezirad et al.
research-article2021

Original Article

Waste Management & Research

Preventing food waste in subsidy-based 2021, Vol. 39(8) 1027–1038
© The Author(s) 2021
Article reuse guidelines:  

university dining systems: An artificial sagepub.com/journals-permissions
hDtOtpIs: :1//0d.o1i.1o7rg7/1007.13147274/027X324121420X12719170417974

neural network-aided model under journals.sagepub.com/home/wmr

uncertainty

Mohammadali Faezirad1, Alireza Pooya1 ,  
Zahra Naji-Azimi1 and Maryam Amir Haeri2,3

Abstract
Food waste planning at universities is often a complex matter due to the large volume of food and variety of services. A major portion of 
university food waste arises from dining systems including meal booking and distribution. Although dining systems have a significant 
role in generating food wastes, few studies have designed prediction models that could control such wastes based on reservation 
data and behavior of students at meal delivery times. To fill this gap, analyzing meal booking systems at universities, the present 
study proposed a new model based on machine learning to reduce the food waste generated at major universities that provide food 
subsidies. Students’ reservation and their presence or absence at the dining hall (show/no-show rate) at mealtime were incorporated in 
data analysis. Given the complexity of the relationship between the attributes and the uncertainty observed in user behavior, a model 
was designed to analyze definite and random components of demand. An artificial neural network-based model designed for demand 
prediction provided a two-step prediction approach to dealing with uncertainty in actual demand. In order to estimate the lowest total 
cost based on the cost of waste and the shortage penalty cost, an uncertainty-based analysis was conducted at the final step of the 
research. This study formed a framework that could reduce the food waste volume by up to 79% and control the penalty and waste cost 
in the case study. The model was investigated with cost analysis and the results proved its efficiency in reducing total cost.

Keywords
Food waste management, meal booking, university services, artificial neural networks, error compensation

Received 9th August 2020, accepted 23rd April 2021 by Associate Editor Alberto Bezama.

Introduction cooking enough meals. On the one hand, overproduction can lead 
to wasting of food and squandering of financial resources. On the 

One of the most challenging aspects of every food supply and other hand, underproduction may cause some shortage that 
distribution system is the minimization of food waste, the success affects customer satisfaction or food service users (Dolnicar and 
of which ensures the stability of natural systems and manage- Grabler, 2004; Lasek et al., 2016). A common approach to man-
ment of the growing populations (Silvennoinen et  al., 2019). aging these issues in food services is demand planning based on 
Boosting food waste management has an impact on sustainability order reservations (Ongkunaruk and Kessuvan, 2013). Using the 
in food production and consumption (Martin-Rios et al., 2018). booking systems to pre-order and book meals is an appropriate 
According to a conventional definition, food waste is any surplus method for demand planning in food services that can efficiently 
or discarded products derived from the process of production, help reduce overproduction and food waste (Steen et al., 2018). 
processing, distribution, or consumption of food (Okazaki et al., Meal booking systems can significantly reduce food waste by 
2008). According to the material flow model in food services as 
proposed by Pirani and Arafat (2016), a considerable portion of 

1Department of Management, Ferdowsi University of Mashhad, 
waste, as well as disposing of food during the preparation and Mashhad, Iran
after serving food, is a result of unconsumed food. This type of 2Learning, Data-Analytics and Technology Department, University of 
waste is generally categorized into the post-consumption food Twente, Enschede, The Netherlands

3Department of Computer Engineering, Amirkabir University of 
waste (PCFW) group, which is hard to manage due to the prepa- Technology, Tehran, Iran
ration of final products and the presence of perishable food com-
pounds (Awasthi et  al., 2018). Undoubtedly, an accurate Corresponding author:

Alireza Pooya, Department of Management, Ferdowsi University of 
prediction of demand and possible food waste can assist food Mashhad, Azadi Square, Mashhad 91779-48974, Iran. 
service providers with the right amount of ingredients and in Email: alirezapooya@um.ac.ir



1028	 Waste Management & Research 39(8)

estimating the number of daily meals according to the reservation preparing and distributing food on campus (Abdelaal et  al., 
orders (Painter et al., 2016). In order to design booking models 2019). Besides those studies that have focused on estimating the 
that can generate these estimates, a sustainable mechanism for waste volume, other authors have also examined operational 
predicting demand is required. Here, the significance of demand methods for and approaches to reducing waste volume. A study 
prediction becomes obvious. According to Obaidat and reviewed a university that serves nearly a thousand meals a day 
Nicopolitidis (2016), future demand prediction is one of the and explored the effect of different food delivery scenarios on the 
aspects of intelligent systems that can lead to a reduction in costs amount of waste produced at the university dining hall. This 
and an increase in the quality of strategy and business perfor- study has investigated the shift from the tray-based system of 
mances. Therefore, managers are required to predict demand to food delivery to a non-tray-based system in which food waste 
make proper decisions. and customers’ perspectives are evaluated, thus leading to 

The significance of university food waste comes to the fore reduced solid food waste and high customer support at the buffet 
since it constitutes a significant part of dormitory and campus dining halls (Thiagarajah and Getty, 2013).
waste. Furthermore, due to the centrality of food distribution Determining the exact amount of food waste requires a careful 
centers at universities, the effectiveness of intervention and plan- prediction of the number of individuals receiving food services 
ning to reduce food waste will remarkably increase (Abdelaal (Pirani and Thompson, 2016). This issue becomes even more 
et al., 2019; Gallardo et al., 2016). serious when free food or subsidies are distributed, because when 

The literature on waste management at universities is mainly users enjoy a free lunch, it is likely for them to eat out somewhere 
focused on analyzing the volume and composition of waste, the else. Implementing a reservation system that compels users to 
causes and factors of waste generation, and results of implement- book meals in advance may contribute to planning and produc-
ing recycling programs and waste reduction (Gallardo et  al., tion in the cooking sector in order to prevent overproduction 
2016). In a research study conducted at a university in Nigeria, (Steen et al., 2018). In a condition where demand for food service 
the production of solid waste was studied to estimate the ratio of and uncertainty of the available information are high, efforts 
different waste components. The largest share of waste belongs made to strengthen the reservation system proved to be signifi-
to food waste, weighing nearly 140 kg per day. The cafeterias and cant (Ongkunaruk and Kessuvan, 2013).
restaurants at this university contributed the most to the produc- Since the accurate prediction of demand has a significant role 
tion of food waste (Okeniyi and Anwan, 2012). In this regard, in reducing food waste (Pirani and Thompson, 2016), the present 
another study considered a university in Iran as a case study and study consciously decided to focus on this issue. In the field of 
investigated solid waste. It was found that the largest daily pro- demand estimation with uncertainty in reservation systems, sev-
duction of compostable wastes was derived from organic waste. eral studies have been conducted, mainly focusing on the fields 
Due to the surplus volume of food distributed daily to students, of hotel management (Fiori and Foroni, 2020; Lacagnina and 
food waste, that is, the remains of the food distributed in student Provenzano, 2016) and transportation planning (Gao and Le, 
dormitories or university restaurants, constitute the largest por- 2018; Luo and Shi, 2006); however, the present research takes a 
tion of organic waste (Taghizadeh et al., 2012). The production of university reservation system as a case study and aims to accu-
waste and its compounds was also studied at a Spanish university rately estimate the exact amount of meals needed based on the 
during 1 academic year. This university uses a university waste booking data and demand-side information. Although several 
management system with two axes: waste management and studies have been conducted in the field of reservation systems 
cleaning service. In the case of university restaurants, the highest (Tsai, 2014) and their relationship with food waste management 
proportion of their waste is comprised of organic materials that (Ongkunaruk and Kessuvan, 2013), designing and implementing 
constitute approximately 61% to 72% of all wastes (Gallardo a demand estimation model under uncertainty in order to manage 
et al., 2016). In 2016, a study focused specifically on food waste and reduce food waste in university self-services has received 
at a university in South Africa. It aimed to estimate the amount of scant attention.
food waste production at the dining halls of universities. Different The case study of the present research was inspired by a pol-
factors including distance to the dining hall, mealtime, and its icy of cheap food distribution through government subsidies. The 
ingredients are known to affect the production of food waste, thus final price of food turns out to be very low by such student food 
prompting each student to produce an average of 0.555 kg of food subsidies. This is the reason why students are not fully adhering 
waste per day. This study further discussed the reasons for the to their reservations, which will lead to their no-show during ser-
slow rate of students at the dining halls and the diversity of waste vicing hours. Taking the no-show and over-show rates into con-
productions in different self-services at this university (Painter sideration has a significant role in determining the amount of 
et al., 2016). A similar study investigated the condition of food food waste (Pirani and Thompson, 2016). The present study 
waste on a university campus in Qatar. In this research, in addi- focuses on food waste reduction, separating the reserved and 
tion to revealing a general estimate of food waste in different actual demands. In order to take control of this issue, a model is 
places, the amount of waste specific to each type of food was proposed here that includes a two-step estimation using a machine 
presented. One of the key factors involved in the results of this learning model based on artificial neural networks (ANNs) to 
study was overproduction with emphasis on different places for ensure significant accuracy of demand prediction. In step 1, the 



Faezirad et al.	 1029

Table 1.  The amount of food waste due to reservations and the absence of students.

Year Number of Rate of untaken meals Estimated weight of 
untaken meals (no-shows) (%) total waste (kg)

2013 141,066 18.70 59,248
2014 93,631 17.34 39,325
2015 87,020 15.61 36,548
2016 83,435 15.09 35,043
2017 86,417 14.13 36,295
2018 94,411 14.65 39,653
2019 121,906 14.68 51,201

definite demand component is estimated and, in the next step, breakfast serving as multiple packages once a week. Therefore, 
that is, post-processing step, the uncertain demand component is the number of booking transactions for breakfast or dinner is 
estimated using error analysis. lower than that for lunch. Meanwhile, universities usually hold 

The rest of this work is organized as follows: The next section similar approaches and standards in terms of dining services. In 
discusses the case of a large university and investigates the order to develop a comprehensive and generalizable model, the 
obtained data and the proposed model. After that, section “Results present study investigated the lunch menu served at this univer-
and discussion” describes the results of implementing the pro- sity at the central dining hall (main self-service). The meal 
posed model based on the mentioned data and provides an appro- menu includes two optional foods that the student can book up 
priate response at the optimum level of confidence. In the final to 48 hours prior to the due day. Usually, a significant percent-
section, the output of the research is analyzed, hence bringing the age of students do not show up to receive the meal and their 
benefits of this study to the fore. reserved food will remain unconsumed/untaken. This amount 

of unconsumed/untaken food is defined as food waste, accord-

Materials and methods ing to the definition presented by Okazaki et al. (2008), which 
requires management.

This section describes the major steps in the current study. First, According to the data collected during this study, from 2013 
an overview of the studied case is presented to clarify the aspects to 2019, the volume of food waste due to the absence (no-show) 
of the problem. Next, the structure of data and variables is identi- of students after lunch and dinner reservation is described in 
fied. After this, the proposed machine learning approach for Table 1. An estimation based on the university analysis revealed 
demand estimation in food waste reduction is demonstrated, fol- that the average weight of each food portion is 420 g; the weight 
lowed by an uncertainty evaluation for cost minimization. of food waste related to each year is shown separately in the third 

column of the Table 1.

Study area Student food reservation and delivery systems are not active 
due to the summer holidays except August, and students are 

This study was conducted based on relevant information about served for the rest of the year. A significant amount of food lefto-
one of the major universities in Tehran, Iran. The university has vers may be consumed through free distribution among pre-
nearly 14,000 students, 4219 of whom live in dorms. It provides determined charities or student dormitories. Further, two types of 
three meals for students: breakfasts, lunch, and dinner on week food waste respectively derived from unserved and served meals 
days (except holidays) that breakfast and dinner served only for in the form of leftovers turn into university garbage. In other 
dormitory students. Meals are distributed at different dining halls cases, such food leftovers may be sold to different students or 
of the university, some of which are located on campus and some other individuals for a different fee.
in dormitories.

Based on the usual procedure of reservation and distribution Data collection
of food at this university, each student can choose his/her 
desired food out of possible options (based on food name, food The initial step in collecting data for demand prediction is deter-
price level, and place of receiving food) in a certain period of mining the attributes or characteristics associated with the prob-
time before each mealtime and booking it online. The cost of lem. To this end, the literature on demand forecasting in university 
this reservation will be paid out of a student’s online wallet, dining systems was reviewed. However, few researchers have 
which needs charging. At the end of the reservation, students analyzed the characteristics of demand prediction and its many 
will not be able to reserve a desired meal and will eventually be aspects in the field under study. Table 2 shows a number of 
able to return to their pre-selected location at the due time to demand prediction aspects explored in the previous correspond-
receive their food. Breakfast and dinner meals are provided ing research studies for estimating the demand rate.
only for those who live in dormitory and hence, have more sta- To cover all the aspects given in Table 2, the current paper 
bility of reservation and distribution due to delivery to dorms or considers various attributes that influence students’ demand. 



1030	 Waste Management & Research 39(8)

Table 2.  Aspects of demand prediction in dining systems.

Aspect Researches

Menu or type of foods Blecher and Yeh (2008); Kılıç (2015); Yergök et al. (2018); Çetinkaya and Erdal (2019); 
Yurtsever and Tecim (2020)

Day of week or month Ryu et al. (2004); Blecher and Yeh (2008); Yergök et al. (2018); Ali et al. (2019); Çetinkaya and 
Erdal (2019); Yurtsever and Tecim (2020)

Specific times such as holidays Kılıç (2015); Xinliang and Dandan (2017); Yergök et al. (2018); Çetinkaya and Erdal (2019); 
Yurtsever and Tecim (2020)

Individual factors Kılıç (2015); Xinliang and Dandan (2017); Yurtsever and Tecim (2020)
Price or budget Yurtsever and Tecim (2020)

Table 3.  Details of the attributes used in estimating the show rate.

Attributes Type Columns

The day of week zero/one 5
The day after/before a holiday zero/one 2
Price level of Food 1/Food 2 zero/one 3+3
Name of Food 1/Food 2 zero/one 10+10
Total number of reservations for Food 1/Food 2 Real number 1+1
The rate of reservations for Food 1/Food 2 by undergraduate students Between 0 & 1 1+1
The rate of reservations for Food 1/Food 2 by Masters’ students Between 0 & 1 1+1
The rate of reservations for Food 1/Food 2 by PhD students Between 0 & 1 1+1
The rate of reservations for Food 1/Food 2 by dormitory students Between 0 & 1 1+1
Ratio of previous show rate of reservoirs of Food 1/Food 2 Between 0 & 1 1+1

Extracted attributes are weekdays, consecutive holidays, food recommended meals. Therefore, with the exception of such date 
price level, food name, number of reservations segregated by indexes as weekdays and consecutive holidays, the rest of the 
academic degree, number of reservations segregated by accom- attributes for each food have a separate, specific value. The 
modation status, and the ratios of previous attendance. Although description and characteristics of each attribute are listed sepa-
previous studies have proposed several main aspects of demand, rately in Table 3. The index of history is the converted history 
none of them performed the demand prediction under reservation of each day, which is replaced by an integer. The day of week 
data. Therefore, utilizing the mentioned novel attributes, this refers to the day number in a week that varies from 1 to 5 (in the 
study considers booking parameters to complete the proposed form of five input variables with one hot encoding format), 
model. Furthermore, individual factors are given significance by given that this service is not active on the weekends. In case of 
incorporating academic degree, accommodation status, and usual a holiday after/before a certain day, the index associated with 
participation in dining halls. These attributes were extracted from that day returns to 1. The price of foodservice is constant and 
the opinions of university experts, thanks to their former experi- categorized into three levels of high/medium/low values. 
ence and knowledge of students’ behavior. Therefore, food price level is converted into three variables of 

They are the employees and administrators of the university's zero/one. Given that 10 different types of food are served by the 
student nutrition department and have accumulated ample expe- university, 10 zero/one attributes are also considered as food 
rience and knowledge of students' behavior in terms of meal names. The total number of reservations indicates the booked 
booking and attendance at meal hours. Furthermore, it was demand for the corresponding food. Each of the attributes 
attempted to use related experts in these positions at other univer- including the rate of reservations by undergraduate/graduate/
sities. In addition, this study attempted to collect the views of postgraduate students and rate of reservations by dormitory stu-
information-technology experts who have worked extensively on dents to all students that booked meals is represented by a num-
this subject. ber in interval [0,1]. The number of dormitory students is 

The data of this study, which include a total of 886 records, considered given that those who live in dorms may treat the 
are related to lunch meals served at the university's central dining dining system differently because of their high participation 
hall from 2013 to 2019. rate on campus. Further to that, the main supply source of food 

The users’ show rate is the target variable of this research. for them is the university dining system. The last attribute for 
This variable represents the ratio of the number of users who each food is the ratio of the previous show-up of users, which is 
have booked meals through the system and come to receive the a number between zero and one. This figure suggests that the 
service. From the two food options offered in the reservation users with prior reservations showed up to receive their food in 
system, each student can make a reservation for one of the person in only a percentage of cases on average.



Faezirad et al.	 1031

Food waste reduction model Herein, the objective of the proposed model is to determine 
the number of requirements for food production or cooking. 

The main purpose of this study is to reduce food waste under Considering the university’s commitments to students who have 
uncertainty. There are many approaches that have been pursued made service reservations, decision-makers should make rele-
to deal with uncertainty. Given that the current study tries to esti- vant decisions under uncertainty at a sufficient level of confi-
mate the actual demand for reducing untaken meals, a perdition dence. If x  indicates the amount of the required food, relation 2 
approach should be applied to estimate the demand. Therefore, shows its relation to the random demand d  at a desired level of 
selecting an appropriate prediction tool plays a critical role in this confidence (1−α ) :
task. Artificial Neural Networks are among the most non-para-
metric methods for solving function estimation and fitness prob- 	 Pr (x ≥ d ) ≥1−α 	 (2)
lems that are learned through a set of input/output data (Zhang 
and Suganthan, 2016). An important advantage of neural net- Based on equation (1), since the parameter d  is a function of 
works is the ability to learn complex nonlinear systems (Abbasi the user’s show rate, relation 2 can be substituted as bellow:
and El Hanandeh, 2016), thus making them a good option for 
challenging issues like the one dealt with in this study. Although 	 Pr (x ≥ r.D) ≥1−α 	 (3)
neural networks in many cases outperform traditional models of 
the estimation function with respect to demand estimation The probabilistic relation 3 is actually unknown because dis-
(Muriana, 2017), the application of neural networks to predict tribution of daily show rate is not accessible. Although the esti-
outcomes under uncertainty or in case of constant systemic mated distribution obtained by the ANN can be considered 
changes is quite challenging (Khosravi et al., 2011). This study instead of the distribution r , the error resulting from neural net-
considers the aforementioned concern. Due to the uncertainty in work estimation can cause a significant deviation. Therefore, 
and instability of user behavior after reservation (Painter et al., estimation by the neural network and the error resulting from the 
2016), the usual implementation of neural networks to ensure random behavior that cannot be predicted by the neural network 
point predictions is not enough. Therefore, post-processing meth- can be used to assess the random parameter. This approach is 
ods are appropriate options to modify and reduce errors expressed in:
(Jorgensen and Linneberg, 1999; Siswantoro et al., 2016).

	 r% = r$ + e% 	 (4)
The proposed model is based on two steps: in the first stage, a 

point prediction is carried out; in the post-processing stage, the where r  (definite component) is an estimation by the neural net-
desired point is reached by simply analyzing the expected level of work and e  (random component) is error indicator. Therefore, 
confidence based on the minimum possible cost. Having applied the inequation (3) of the model can be rewritten as:
this approach in their study, Vergara-Dietrich et al. (2019) aimed to 
manage renewable power systems effectively. They combined 	 Pr (x ≥ ( r$ + e% ).D) ≥1−α 	 (5)
ANNs based on time series with chance-constrained programming. 
The considered variable is modeled as a variable with definite and 

Considering the function obtained from the cumulative distri-
random components; the definite component was estimated by the 

bution fit e , relation 5 can be substituted into inequation (6):
neural network and processed along with its random counterpart in 
the desired constraint. The proposed model in this study is similar to 

	  x 
F  $

the recent compound, except that in addition to the estimation of e% − r  ≥1−α 	 (6)
 D 

definite component, the random component is also estimated as a 
cumulative distribution function during the learning of ANNs. The Artificial neural networks-based model
steps and details of the ANN-based model are described below. Preliminaries.  By considering the nature of fitness and 

obtaining r  through ANNs, the default structure of neural network 
The framework for estimating the presence of users.  In the in this research is shallow based on feedforward framework with 
proposed model of the present research, the amount of actual a single hidden layer. Assuming that T  is the number of training 
demand is expressed in terms of the show rate. According to samples in {(pt ,rt ),t =1,…,T}  with pt = ( p n

t1, pt2,…, ptn )∈  
equation (1), the show rate r  represents the percentage of the and rt = (rt1,rt2,…,rtm )∈m  denoting respectively the input 
booked demands served at the mealtime: vectors and the targets in a supervised learning scheme, a feed-

forward neural network with N  nodes in the hidden layer and 
d	 r = 	 (1) transfer function φ  is represented as follows:
D

where d  and D  denote the number of users who succeed to N

	 YN (pt ) =∑β iφ (wi.pt + bi ), t =1,…,T 	 (7)
arrive at the designated time (which is an unknown value) and the 

i=1
number of booked demands, respectively. Due to uncertainty in 

T
the value of the random demand d , the value of r  is also subject in which equation (7), wi = (wi1,wi2,…,win )  is the vector of 
to uncertainty. input weights that binds the input nodes and the i  th hidden 



1032	 Waste Management & Research 39(8)

node. β i = (β
T

i1,βi2,…,βim )  is the output weight vector that the university or the disgrace ascribed to quality of university 
binds the i  th hidden node and the output nodes. bi  is the bias of services will significantly vary. In this regard, Sillanpää et  al. 
the i  th hidden node. Therefore, achieving the least error in esti- (2020) implemented the shortage cost function in the form of a 
mating is equivalent to finding the values of bi , β i ,wi  that mini- piecewise linear function to increase the shortage cost at higher 
mizes function 8 (Lolli et al., 2017; Siswantoro et al., 2016). levels of divergence between demand and serviceable quantity. 

Similarly, in this study, the piecewise linear function was taken 
	 YN (pt ) − rt , t =1,…,T 	 (8) into consideration, except that a fixed threshold limit was used. 

Therefore, the function of shortage cost is given as follows:
Two-step estimation based on ANNs.  After determining the 

value of r  based on the results of the mentioned network, equa- 	 Cs (x) = cs .(t.D − x) + cs .sgn (t.D − x −δ ) 	 (10)
tion (4) can be used to obtain the value of e . The second step is v f

to apply second neural network to reduce prediction errors of the where the cost parameter cs  represents the rate of service com-
probabilistic distribution function e . This assessment has been v

pensation for each unmet demand. δ  indicates the threshold of 
made using the ANN according to equations (7) and (8), except increase in the shortage cost; in other words, if the actual value of 
that the inputs and the output are prediction errors in the first demand exceeds the predicted value, separately calculated cs  as 
stage ( e ) and empirical cumulative distribution function of e , v

well as the constant cost parameter cs  will be considered as the 
respectively. f

penalty costs to compensate the unmet demands of student associa-
tions, loss of mutual goodwill, and legality and credibility issues 

Determining the α  level based on the lowest cost analy-
derived from the accumulated volume of unsatisfied demands.

sis.  The results of the proposed model are strongly dependent on 
Accordingly, the considered cost model according to equation 

the amount of α  in relation 6. The higher this value is, the larger 
(10) turns is substituted into equation (11):

the solution space of the inequation and the smaller the x  value 
will be. For this reason, the performance of the proposed model 
is evaluated based on not only the volume of food waste or its C(x) = (− + )+ + ( − )+cw. t.D x cs . t.D x + cs .sgn (t.D− x−δ )

+
  (11)

v f

material cost, but also the impact of lack of food needed when 
students show up to get the meal under food shortage. where cost parameter cw  indicates waste cost due to the greater 

Therefore, this research focuses on the correct estimation of amount of the predicted demand as compared to the actual 
the amount of actual demand to significantly reduce the number amount of demand per case.
of untaken meals. Based on the current state of service, any Based on the details mentioned in this section, sequential 
reduction in the amount of untaken food is equal to a considera- stages of the proposed model are shown in Figure 1. The stages 
ble reduction in cooking. In other words, if no food is distributed, of the proposed model are shown in this section.
the highest level of the desired point is achieved. In practice, 
however, there has to be a trade-off between the cost of food Results and discussion
waste (or the cost of surplus food with no demand for it at the 
mealtime) and the cost of food shortages; both of these costs are The data used in this research, which are based on the attributes in 

directly dependent on the decision-making about the amount of Table 3, were extracted from the university dataset under study. 

food production. These two costs are shown in equation (9) as These data are applicable to the analysis model of the research only 

Cw  and Cs , respectively. after being pre-processed (including the elimination of the noises, 
days without food or with incomplete data, and integration of 

	 C(x) = Cw(x) +Cs (x) 	 (9) records based on the two desired outputs). To estimate the value of 
r  in equation (4) using neural network, the acquired data were 

According to the reservation management literature which is partitioned into the three following parts based on a common ratio 
rooted in revenue management, the shortage cost is actually the (Pandey et  al., 2016) to prevent overfitting: training, validation, 
denied-service cost. According to a realistic assumption made by and testing at ratios of 70%, 15%, and 15%, respectively. To 
Talluri and Van Ryzin (2004), the penalty for shortage in the res- achieve the best ANN structure for estimating r , different struc-
ervation management models should be in the increasing and tures were examined. These structures include a combination neu-
convex form which will include the cost of an alternative service, ral network’s parameters in a permutational analysis. Two training 
compensation, and loss of goodwill (He, 2019). Given the spe- functions (Levenberg-Marquardt and Scaled Conjugate Gradient), 
cific nature of the proposed case study which is arising from gov- a range of 10–60 neurons for the hidden layer and two transfer 
ernment subsidy, the structure of the costs of unserved services in functions (Log-sigmoid and Hyperbolic Tangent Sigmoid func-
a competitive environment varies. However, one cannot ignore tion) was considered. The best architecture was evaluated based on 
the ascending pattern of shortage cost, because if the proposed the mean squared error, mean absolute error, and coefficient of 
model of this study under-predicts the outcome by a margin of determination (Abbasi and El Hanandeh, 2016; Pandey et  al., 
one person (from the actual number of actual demands) as com- 2016) on test part of data. Therefore, an ANN with 10 neurons in a 
pared to the margin of dozens of students, the costs incurred by hidden layer along with the Log-sigmoid transfer function in the 



Faezirad et al.	 1033

Figure 1.  The flow of the model’s stages.

backpropagation process with the Levenberg-Marquardt training  = 0.2378 . The proper distribution of the errors of the second 
algorithm was selected as the best structure. The performance data follows t-Location-Scale with the parameters µ = 0.0032 , 
results of trained neural networks based on the regression between σ = 0.0171 , and ν = 5.3720 . Nevertheless, compared to these 
the actual value and the estimated value with the accuracy rates of two distributions, the estimation of the cumulative distribution 
73%–75% are shown in Figure 2. function of the error values was examined using another ANN. 

According to equation (4), the probability distribution func- The output of this fitness compared with each of the two distribu-
tion of e  is used to estimate the random component. Accordingly, tions in the corresponding fitting is shown in Figure 4. For evalu-
using the difference between the values of the actual show rate ation of the neural network in comparison with the classic 
and the output of the trained neural network, the ratio of the error distribution functions, equation (12) is used (Chen et al., 2020). 
values to the target value is calculated. Figure 3 shows the histo- This performance metric is known as the mean absolute percent-
gram of the distribution of error values and the best distribution age errors (MAPEs).
fitting each of them.

By evaluating different probability distribution functions on m Fk − F	 k
the data relevant to the neural network error in both food predic- f =∑ 100%

M × 	 (12)
F

= k m
tions, the appropriate probability distribution has been fitted to k 1

each of these data. The distribution of the first data is Epsilon The MAPEs of the estimated CDF for the neural network are 
Skew Normal with the parameters θ = 0.0116 , σ = 0.0231  and equal to 1.38 and 1.34, while they are equal to 5.57 in Epsilon 



1034	 Waste Management & Research 39(8)

Figure 3.  Histogram of the output errors of neural network 
in estimating the show rate accompanied by fitting of the 
appropriate distribution function: (a) Food 1 and (b) Food 2.

therefore, the function derived from network learning can be 
written in equation (13) as follows:

  2 
	 E = SL b + T

x × 
 2 w2 	 (13)


1+ exp(−2(b1 +w x 

 1 )) 
where b1  and b2  are the biases of input and hidden layers, 
respectively, and w1  and w2  are the weight vectors of input 

Figure 2.  Correlation between neural network estimation layer to hidden layer and hidden layer to output layer, respec-
and actual show rate: (a) Food 1 and (b) Food 2. tively. SL  function is in fact the transfer function of output layer 

that restricts the output value between 0 and 1 in a linear manner. 
Skew Normal distribution fitness on the first food and to 6.39 in As a result, network estimates in the form of cumulative distribu-
t-Location-Scale fitness on the second food. Accordingly, the tion function work properly, as expected.
application of neural networks ensured a favorable performance By setting cost parameters cw , cs  and cs  to 120,000 IRR, 

v f

in estimating the cumulative distribution function. In addition to 360,000 IRR and 10,000,000 IRR, the proposed model was evalu-
their high performance, the convenience and simplicity of apply- ated with different values of α  from 0.01 to 0.3 according to equa-
ing the mentioned function due to neural networks in 8 is another tion (11). The performance of the model was evaluated at a time 
benefit, because no new probabilistic distribution function is interval of 1 year (2019), as shown in Figure 5, and the threshold 
replaced and the mathematical structure of constraints in the limit δ  is equal to 10 people. The values of food waste cost and 
function does not change due to user behavior variations over shortage penalty are set based on the minimum value of x .
time. In the structure of neural networks, a sigmoid symmetric The minimum total cost is obtained in α = 0.22  and α = 0.19, 
function is used as a transfer function in the hidden layer; respectively for Food 1 and Food 2. If the proposed final model 



Faezirad et al.	 1035

Figure 5.  Total costs including waste cost and shortage 
penalty based on different values of α .

an annual aspect, is lower than current cost; hence, the model 
has correctly reduced the total annual cost.

A significant reduction in the amount of food waste was 
observed in different months of 2019, except for August when 
the university system is usually inactive. This volume of waste 
reduction varies from 63.36% to 99.28% per month and, in 

Figure 4.  Comparison of CDF estimation by ANN and the general, a 79.66% reduction in food waste was recorded 
distribution function candidates on the data derived from throughout the year. This result has been obtained from the 
prediction error: (a) general view of estimated CDF for errors difference between the current untaken meals and the esti-
of Food 1 and (b) general view of estimated CDF for errors of mated untaken meals generated by the proposed demand pre-
Food 2.

diction. Therefore, the amount of reduction was obtained by 
the ratio of proposed model-based estimated untaken meals 

is run with the obtained values of α , the acquired output will be over reported untaken meals in 2019. The reduction rate of 
consistent with the value in Figure 6. The reduction rate of food waste would be determined if the new model was established 
waste in 2019 is shown in this figure. In addition, Figure 6 shows for the year 2019. However, according to the data listed in 
the estimated reduceable rate of food waste by the proposed Table 1 in 2019, 14.68% of users’ reservations generated food 
model. Meanwhile, based on analysis of the total cost for 2019, waste due to their absence (no-show). If the current model is 
this Figure shows the total cost estimated by the proposed model successfully generalized to the entire university while keeping 
with the data received in 2019. the response quality, the amount of food waste will be 

According to Figure 6, waste costs were obviously reduced 10,414 kg in 1 year. Such a reduction in food waste works in 
due to a significant reduction in the amount of food waste. conjunction with controlling the risk of improper food ser-
Moreover, this decrease is in equilibrium and consistent with the vices, because determining the costs of shortage and waste is 
shortage cost, which has finally resulted in the total cost reduc- still controversial and up for debate.
tion. Although shortage costs are added to the new model, the By keeping in mind, the negotiated, final costs of food for the 
total cost in 2019 is still lower than the total cost in the current university, the waste cost can be easily determined. However, 
situation. Although the monthly amount of waste determined by determining the cost is no longer easy in case of shortage. In 
the new model is lower than the current waste in each month, the addition to the direct cost of food replacement, compensation 
trend of the total cost in February goes against that in other costs and damaged goodwill (He, 2019) should also be consid-
months. The main reason for such higher costs lies in the nature ered in the final tally. Determining these two costs, that is, com-
of February as it is located between two semesters of the aca- pensation and damaged goodwill costs, becomes more 
demic year and it includes exam days. Therefore, the behavior of challenging at the end of each service day. The queue is always 
students in this period of time is subject to changes. The total governed by the first-in first-out rule, hence the reason if some 
reservation rate is lower than that in regular time periods, lead- students do not receive their meals, it means they would be 
ing to changes in the data pattern. It can be concluded that the among the last ones to stand in the food delivery queue. Therefore, 
proposed model has underestimated the actual demand in com- food shortage often occurs in the final minutes of mealtime.
parison to demands in usual time periods, thus imposing high According to the average number of users’ show-up from a cer-
penalty costs for unsatisfied demand. However, the total cost, as tain time to the end of the mealtime, if the reserved food runs out 



1036	 Waste Management & Research 39(8)

Figure 6.  Estimated cost and waste reduction during 2019.

within the last 15 minutes of the servicing process, an average of reasons for students’ absence in self-services to receive their 
25 users may not receive their intended services. Therefore, if the reserved meals (Painter et al., 2016), only a few studies have pro-
volume of food is not enough, there will be a very little chance to vided a model based on quantitative estimates of the students’ 
compensate for the delay in serving the students, because prepar- behavior under random situations with different uncertain costs.
ing food, even through other suppliers, requires more time and Based on investigating the behavior of students in response to 
money for which the student may not be able to wait more. their reserved meals, a set of random or uncontrolled factors 
Therefore, the parameters of this section are determined according including students’ drowsiness or satiation and crowded self-
to the university policy-making and its commitment to promoting services was given and analyzed (Painter et al., 2016). Therefore, 
the stability of servicing the students in university dining halls. a careful prediction of the effects of these factors, which vary 

from individual to individual, as well as an initial estimation, 

Conclusions requires sensitivity analysis and confidence level assessment in 
random conditions. In this regard, the first phase of the present 

Waste management at universities has received much attention in study provided an estimation obtained from the ANN, while the 
the field of waste management and led to further research. Most of second phase, that is, the combination of neural network results 
the related papers in this field focused on the procedures and fac- based on the random behavior of the error generator, made it pos-
tors involved in waste production, analysis of waste volume, and sible to consider neglected random incidents or behaviors of 
management of recycling programs and waste reduction policies model attributes in the form of a probabilistic inequation in the 
(Gallardo et  al., 2016). Although many studies have considered actual demand estimation model. To this end, the proposed model 
food waste in universities, no comprehensive studies have been carried out the corresponding estimations in accordance with 
conducted on demand prediction based on reservation data. There fluctuations of random behaviors, the results of which were dis-
is a research gap in the context of food waste management of din- cussed in the former section. The two-phase model with analysis 
ing systems that include meal booking and food distribution. of uncertainty led to a 79% decrease in the food waste of the 
Therefore, one of the main contributions of the present study is considered university. The reduction was based on decreasing the 
filling the mentioned gap in analysis of university food waste. In number of untaken meals that can reduce food waste directly. To 
addition to the aspects explored in previous studies for demand implement this approach, a simultaneous balance between mini-
prediction, the characteristics of meal booking data and reservation mizing waste cost and shortage penalty was considered. 
segments has been considered in the proposed model. The present Therefore, the reduction in food waste volume has been consid-
research represents a centralized effort to predict the proper vol- ered together with controlling the shortage and waste cost. 
ume of cooking so as to significantly reduce untaken meals. The Furthermore, emphasizing the significant reduction in food waste 
resulting wastes are generally categorized as PCFWs that the accu- by the proposed framework, novel attributes utilized in predic-
rate prediction of the amount of food consumption or actual tion part of the model can be approved and used in future estab-
demand at the universities’ dining halls will have a significant lishment of demand prediction at universities with booking data.
impact on controlling food waste. The novelty of the present study Furthermore, the proposed model managed to create a notable 
lies in analyzing the presence and absence (show and no-show potential for defining and implementing other executive rules and 
rates) of students at the dining halls and presenting a related math- service policies of the mentioned university. Since the proposed 
ematical model, likes of which have not been seen in the previous problem is not just a model limited to fitting and is defined in the 
research studies. Although previous researchers have analyzed the form of a probabilistic inequation, it will be capable of designing 



Faezirad et al.	 1037

and solving larger complexities common at any university. This conference on computer science and engineering (UBMK), Samsun, 

capability can be generalized through the chance-constrained pro- Turkey, 11–15 September 2019, pp.1–6. New York: IEEE.
Chen CH, Song F, Hwang FJ, et al. (2020) A probability density function 

gramming model. The generalization of such possible planning generator based on neural networks. Physica A: Statistical Mechanics 
could help decision-makers take into account other constraints and its Applications 541: 123344.
and limitations involved. Choosing two types of food, each as an Dolnicar S and Grabler K (2004) Forecasting in short-term planning and 

management for a casino buffet restaurant. Journal of Travel & Tourism 
alternative or a supplement to the other, is another aspect that can Marketing 16: 381–408.
promote the model efficiency. Although students have already set Fiori AM and Foroni I (2020) Prediction accuracy for reservation-based fore-
their preferences during the reservation, they may still face short- casting methods applied in Revenue Management. International Journal 

age; in this case, it may be possible to replace food 1 with food 2 of Hospitality Management 84: 102332.
Gallardo A, Edo-Alcón N, Carlos M, et al. (2016) The determination of waste 

or vice versa at a new price. This idea would realize the objective generation and composition as an essential tool to improve the waste 
of food waste reduction. management plan of a university. Waste Management 53: 3–11.

This study has been subject to certain limitations from the Gao J and Le M (2018) Mathematical programming of airline revenue manage-
ment with passenger choice behavior. In: 2018 14th international conference 

very beginning. Therefore, to extend this research and provide on natural computation, fuzzy systems and knowledge discovery (ICNC-
suggestions for future research, the data of this research should FSKD), Huangshan, 28–30 July 2018, pp.669–676. New York: IEEE.
be injected into two datasets to which the existing authors did not He W (2019) Integrating overbooking with capacity planning: Static model 

and application to airlines. Production and Operations Management 28: 
have access so that the impact and capability of the proposed 1972–1989.
model would be promoted. During the course of conducting this Jorgensen TM and Linneberg C (1999) Boosting the performance of weight-
study, the data on the daily curriculum of students were not made less neural networks by using a post-processing transformation of the out-

available to researchers. Therefore, among the attributes that put scores. Proceedings of the International Joint Conference on Neural 
Networks 2: 812–816.

could not be examined are the daily schedule of users and the Khosravi A, Nahavandi S, Creighton D, et  al. (2011) Lower upper bound 
hours before and after serving food at the university’s self-ser- estimation method for construction of neural network-based prediction 

vices. In addition, the data record associated with the behavior of intervals. IEEE Transactions on Neural Networks 22: 337–346.
Kılıç G (2015) Yapay Sinir Ağlari ile Yemekhane Günlük Talep Tahmini. 

users after reserving their intended food was not sufficiently Master’s Thesis, Pamukkale Üniversitesi Fen Bilimleri Enstitüsü.
stored in the database of the university reservation system. In Lacagnina V and Provenzano D (2016) An integrated fuzzy-stochastic model 
case these data become available, behaviors such as canceling for revenue management. Tourism Economics 22(4): 779–792.

Lasek A, Cercone N and Saunders J (2016) Smart restaurants: survey on cus-
food reservations after the authorized interval (in the form of sell- tomer demand and sales forecasting. In: Smart Cities and Homes. Boston, 
ing food to other students) can also be considered to be added to MA: Morgan Kaufmann, pp.361–386.
the model. In case the aforementioned behavioral patterns are Lolli F, Gamberini R, Regattieri A, et al. (2017) Single-hidden layer neural 

seen on a certain day, the possibility of a new emerging behavio- networks for forecasting intermittent demand. International Journal of 
Production Economics 183: 116–128.

ral pattern is reinforced. Luo L and Shi X (2006) The stochastic model of multi-leg capacity allocation 
for air cargo revenue management. In: 2006 international conference on 

Declaration of conflicting interests	 service systems and service management, Troyes, France, 25–27 October 
2006, pp.917–921. New York: IEEE.

The authors declared no potential conflicts of interest with respect to Martin-Rios C, Demen-Meier C, Gössling S, et al. (2018) Food waste man-
the research, authorship, and/or publication of this article. agement innovations in the foodservice industry. Waste Management 79: 

196–206.
Funding Muriana C (2017) A focus on the state of the art of food waste/losses issue 

and suggestions for future researches. Waste Management 68: 557–570.
The authors received no financial support for the research, author- Obaidat MS and Nicopolitidis P (2016) Smart Cities and Homes: Key 
ship, and/or publication of this article. Enabling Technologies. Boston, MA: Morgan Kaufmann.

Okazaki WK, Turn SQ and Flachsbart PG (2008) Characterization of food 

ORCID iD waste generators: A Hawaii case study. Waste Management 28: 2483–2494.
Okeniyi JO and Anwan EU (2012) Solid wastes generation in Covenant 

Alireza Pooya  https://orcid.org/0000-0001-6000-3535 University, Ota, Nigeria: Characterisation and implication for sustainable 
waste management. Journal of Materials and Environmental Science 3: 

References 419–425.
Ongkunaruk P and Kessuvan A (2013) A study of large scale food services 

Abbasi M and El Hanandeh A (2016) Forecasting municipal solid waste best practices in Thailand: A case study of HORECAs. In: 2013 10th 
generation using artificial intelligence modelling approaches. Waste international conference on service systems and service management – 
Management 56: 13–22. proceedings of ICSSSM 2013, Hong Kong, 17–19 July 2013, pp.831–836. 

Abdelaal AH, McKay G and Mackey HR (2019) Food waste from a uni- New York: IEEE.
versity campus in the Middle East: Drivers, composition, and resource Painter K, Thondhlana G and Kua HW (2016) Food waste generation and 
recovery potential. Waste Management 98: 14–20. potential interventions at Rhodes University, South Africa. Waste 

Ali AY, Hassen JM and Wendem GG (2019) Forecasting as a framework for Management 56: 491–497.
reducing food waste in Ethiopian university canteens. Journal of Applied Pandey DS, Das S, Pan I, et al. (2016) Artificial neural network based model-
Research on Industrial Engineering 6: 374–380. ling approach for municipal solid waste gasification in a fluidized bed 

Awasthi MK, Selvam A, Chan MT, et al. (2018) Bio-degradation of oily food reactor. Waste Management 58: 202–213.
waste employing thermophilic bacterial strains. Bioresource Technology Pirani SI and Arafat HA (2016) Reduction of food waste generation in the 
248: 141–147. hospitality industry. Journal of Cleaner Production 132: 129–145.

Blecher L and Yeh RJ (2008) Forecasting meal participation in university Pirani SI and Thompson G (2016) FRESH: A food-service sustainability rat-
residential dining facilities. Journal of Foodservice Business Research ing for hospitality sector events. Cornell Hospitality Tool 16: 3–11.
11: 352–362. Ryu K, Jang SS and Sanchez A (2004) Forecasting methods and seasonal 

Çetinkaya Z and Erdal E (2019) Daily food demand forecast with artificial adjustment for a university foodservice operation. Journal of Foodservice 
neural networks: Kırıkkale University case. In: 2019 4th international Business Research 6(2): 17–34.



1038	 Waste Management & Research 39(8)

Sillanpää V, Liesiö J and Käki A (2020) Procurement decisions over multiple Tsai TH (2014) A self-learning advanced booking model for railway arrival 
periods under piecewise-linear shortage costs and fixed capacity commit- forecasting. Transportation Research Part C: Emerging Technologies 
ments. Omega (United Kingdom) 100: 102207. 39: 80–93.

Silvennoinen K, Nisonen S and Pietiläinen O (2019) Food waste case study Vergara-Dietrich JD, Morato MM, Mendes PR, et al. (2019) Advanced chance-
and monitoring developing in Finnish food services. Waste Management constrained predictive control for the efficient energy management of 
97: 97–104. renewable power systems. Journal of Process Control 74: 120–132.

Siswantoro J, Prabuwono AS, Abdullah A, et al. (2016) A linear model based Xinliang L and Dandan S (2017) University restaurant sales forecast based 
on Kalman filter for improving neural network classification perfor- on BP neural network – In Shanghai Jiao Tong University case. In: 
mance. Expert Systems with Applications 49: 112–122. International conference on swarm intelligence, pp.338–347. Cham: 

Steen H, Malefors C, Röös E, et al. (2018) Identification and modelling of Springer.
risk factors for food waste generation in school and pre-school catering Yergök D, Güven C and ACI M (2018) Artificial neural network model 
units. Waste Management 77: 172–184. design for daily demand prediction in mass meal production. In: 2018 

Taghizadeh S, Ghassemzadeh HR, Vahed MM, et  al. (2012) Solid waste international conference on advanced technologies, computer engineer-
characterization and management within university campuses case study: ing and science, pp.583–586. Safranbolu: Karabuk University. Available 
University of Tabriz. Elixir Pollution 43: 6650–6654. at: https://www.icatces.org/2018/home_files/proceeding_book_2018.pdf 

Talluri KT and Van Ryzin GJ (2004) The Theory and Practice of Yurtsever M and Tecim V (2020) Forecasting meal requirements 
Revenue Management, International Series in Operations Research & using time series methods in organization. In: Janowicz-Lomott M, 
Management Science, vol. 68. Boston, MA: Springer US. Łyskawa K, Polychronidou P, et  al. (eds) Economic and Financial 

Thiagarajah K and Getty VM (2013) Impact on plate waste of switching Challenges for Balkan and Eastern European Countries. Cham: 
from a tray to a trayless delivery system in a university dining hall and Springer, pp.243–254.
employee response to the switch. Journal of the Academy of Nutrition and Zhang L and Suganthan PN (2016) A survey of randomized algorithms for 
Dietetics 113: 141–145. training neural networks. Information Sciences 364–365: 146–155.