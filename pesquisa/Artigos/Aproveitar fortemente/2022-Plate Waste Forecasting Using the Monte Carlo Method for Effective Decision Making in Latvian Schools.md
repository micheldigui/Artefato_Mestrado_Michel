---
source_file: "2022-Plate Waste Forecasting Using the Monte Carlo Method for Effective Decision Making in Latvian Schools.txt"
original_rel_path: "Trabalhos\Artigos\Aproveitar fortemente\txt\2022-Plate Waste Forecasting Using the Monte Carlo Method for Effective Decision Making in Latvian Schools.txt"
category: "Artigos_Aproveitar_fortemente"
extension: ".txt"
sha256: "f2449e99999553ca526bf4b9cf22af7f33afb6f08cd729c54f3ff43063fe2608"
extracted_at: "2026-09-19T23:16:59.188602"
---

﻿nutrients

Article

Plate Waste Forecasting Using the Monte Carlo Method for
Effective Decision Making in Latvian Schools
Sergejs Kodors 1,* , Anda Zvaigzne 2 , Lienite Litavniece 2 , Jelena Lonska 2, Inese Silicka 2 , Inta Kotane 2

and Juta Deksne 2

1 Institute of Engineering, Faculty of Engineering, Rezekne Academy of Technologies, 115 Atbrivosanas Aleja,
LV-4601 Rezekne, Latvia

2 Research Institute for Business and Social Processes, Faculty of Economics and Management, Rezekne
Academy of Technologies, 115 Atbrivosanas Aleja, LV-4601 Rezekne, Latvia; Anda.Zvaigzne@rta.lv (A.Z.);
Lienite.Litavniece@rta.lv (L.L.); Jelena.Lonska@rta.lv (J.L.); Inese.Silicka@rta.lv (I.S.); Inta.Kotane@rta.lv (I.K.);
jd07003@edu.rta.lv (J.D.)

* Correspondence: Sergejs.Kodors@rta.lv

Abstract: Food waste is a global problem, which becomes apparent at various stages of the food
supply chain. The present research study focuses on the optimization of food consumption in schools
and effective food management through data-driven decision making within the trends: zero food
waste and digital transformation. The paper presents a plate waste forecasting system based on
mathematical modeling and simulation using the Monte Carlo method, which showed an RMSE
equal to ±3% and a MAPE of 10.15%. The solution based on the simulator provides a possibility to
better understand the relationship between the parameters investigated through data visualization
and apply this knowledge to train managers to make decisions that are more effective. The developed
system has multi-disciplinary application: forecasting, education and decision making targeted to


 reduce food waste and improve public health and food management in schools.

Citation: Kodors, S.; Zvaigzne, A.;
Litavniece, L.; Lonska, J.; Silicka, I.; Keywords: applied computing; catering services; food loss; leftovers; modeling and simulation; plate
Kotane, I.; Deksne, J. Plate Waste waste; optimization; sustainability
Forecasting Using the Monte Carlo
Method for Effective Decision
Making in Latvian Schools. Nutrients
2022, 14, 587. https://doi.org/ 1. Introduction
10.3390/nu14030587 According to the Food and Agriculture Organization of the United Nations (FAO), one-
Academic Editor: Lindsay Brown third of the world’s food output—approximately 1.3 billion tons a year—is discarded [1].

Food waste and its reduction is an increasingly important problem for local, national
Received: 28 December 2021

and European policymakers, as well as for international organizations and researchers of
Accepted: 25 January 2022

various fields [2]. Some researchers such as Cattaneoa, Sánchez, Torero and Vos (2021) [3]
Published: 28 January 2022

emphasize that, despite the current public policies analyzed in a number of research
Publisher’s Note: MDPI stays neutral studies in various countries aimed at reducing food waste and wastage, there were still
with regard to jurisdictional claims in gaps in information, e.g., regarding how food waste is measured and monitored, gains
published maps and institutional affil- from reducing food waste, etc. Owing to a number of research studies by Thyberg and
iations. Tonjes [4,5], the problem of food waste and the reduction in its impact gains attention

among the public and policymakers.
Research shows that large amounts of food waste are generated during the consump-

tion phase, which includes both eating meals out and at home [6]. Households mostly
Copyright: © 2022 by the authors.
Licensee MDPI, Basel, Switzerland. consume food at home, while the catering sector represents households eating meals
This article is an open access article out. The catering services sector includes both non-commercial and commercial estab-
distributed under the terms and lishments [7], e.g., restaurants, educational institution canteens, etc. Researchers Yui and
conditions of the Creative Commons Biltekoff [8] emphasize that food waste is a significant problem at educational institutions.
Attribution (CC BY) license (https:// It should be noted; however, that school canteens are a controlled environment where
creativecommons.org/licenses/by/ educational campaigns could be conducted to reduce food waste [9]. Schools can help
4.0/).

Nutrients 2022, 14, 587. https://doi.org/10.3390/nu14030587 https://www.mdpi.com/journal/nutrients



Nutrients 2022, 14, 587 2 of 19

to improve educatees’ eating habits by educating them about nutrition and raising their
awareness of the role of food [10].

Despite the growing public, academic and government attention to the problem of
food waste, there are still little information and few research studies on the amounts of
food waste generated by school canteens, as well as the possibilities of measuring and
reducing the food waste, e.g., in Latvia.

To achieve the minimization of plate waste in schools, it is important to develop a
digital decision-making tool for effective food management in the schools, which will
be based on three pillars: (1) knowledge and education; (2) monitoring and forecasting;
(3) data updating and precise decision making.

Intervening in food-service operations to conduct field experiments and build preven-
tive strategies is costly and not always possible [11], which is reinforced due to COVID-19
nowadays. The EU Horizon 2020 project “REFRESH” emphasizes the need to model the
generation of food waste at both the consumer and producer levels [12].

The aim of the research is to develop a mathematical model and a simulator, which
can be applied to forecast plate waste and can be integrated into a decision-making system
for effective food management in schools.

The case study examined the plate waste generated in the secondary schools of
Rezekne city in Latvia. There was restricted access to the schools due to COVID-19 during
the study; therefore, it was problematic to collect enough data to apply the data-based
forecasting methods. As a result, it was decided to develop a decision-making tool for
effective food management based on the feature-based forecasting method. The Monte
Carlo method was a good choice because scientific databases contained studies about
various parameters related to a school meal, as well as some statistical data could be
collected using an anonymous survey or expert knowledge.

2. Related Work
The simulation approach is mostly applied to investigate the global strategies related

to food supply chain organization, policies and other logistic problems by using an agent-
based model. For example, Craven and Krejci [13] developed a simulator to investigate
producer disintermediation from a food hub in the regional food supply system. This
simulator was developed with consideration to be a decision support tool for food hub
managers; however, Van Voorn et al. [14] assessed efficiency and resilience in stylized food
supply chains by using the simulation approach. Scalco et al. [15] applied the agent-based
model to meat consumption by the population in Britain to investigate various marketing
campaigns and price impacts on meat consumption. Nowadays, many research studies
focus on the COVID-19 pandemic in relation to food supply chains. For example, Achmad
et al. [16] studied robust food supply chain strategies by determining the optimum food hub
location and food network to maintain food security, which is robust against disruptions
and uncertainties during the COVID-19 pandemic.

Considering the plate waste subject, Ravandi and Jovanovic [17] applied the agent-
based model to capture the dynamics between plate waste, food surplus and the facility
organization setup. They measured the impact of plate size on food waste, indicating
the need for optimizing food preparation along with designing choice environments that
encourage guests to avoid taking more food than they need. The plate waste is more
studied through other approaches, for example, the modeling approach. Dolnicar and
Juvan [18] developed a model of “Drivers of plate waste” based on an interview with hotel
staff. This model was extended and supported with statistical data later [19]. In addition,
the authors investigated a relationship of plate waste with some impact factors by using
statistical analysis, as was conducted by Anderson et al. [20], who researched a portion
plate impact on food waste.

The primary objective of our research study is related to the prediction of food waste in
schools. Traditionally, data-based methods are applied to make predictions, as was studied
by Malefors et al. [21], who experimented with different forecasting models to predict guest



Nutrients 2022, 14, 587 3 of 19

attendance in school catering. As a result, they achieved an average percentage error of
2–3%. Lately, Malefors et al. [22] completed similar research on guest prediction during the
COVID-19 pandemic; however, it was impossible to collect sufficient statistical data due to
the restrictions related to COVID-19; therefore, it was required to find some feature-based
solution, and the approach with modeling and simulation was an effective decision to
overcome a problem with restricted data because scientific databases provided quantitative
data and information on impact factors and eating models. Several comprehensive studies
are provided by Fagerberg et al. [23], Martins et al. [24] and Zandian et al. [25]. Additionally,
a simulation approach is a white-box solution, which provides the possibility to explain a
relationship between parameters, while a simulator can be applied for decision making and
education that opens multi-directional application for the presented solution, considering
the target group—the school administration.

3. Materials and Methods
3.1. Methodology and Research Ethic

The Monte Carlo model was developed using the synergy of many different methods.
Statistical data for the simulator were collected using the following methods: (1) an anony-
mous survey of parents; (2) literature review; (3) observations of schools. The business
logic of the simulator was developed using the following methods: prototyping and experi-
mental development. The first version of the prototype was presented at an international
scientific conference and contained a minimal set of properties, which was based on expert
assumptions [26]. This simulation model was extended with new parameters and based on
statistical data.

To collect statistical data for the simulator, an anonymous survey of parents was
conducted from 7 June 2021 to 7 July 2021. The questionnaire obtained ethical approval from
the Scientific Council of Rezekne Academy of Technologies on 18 May 2021 (No. 16.1/12).
All the participants were fully informed that anonymity is assured, why the research
is being conducted, how their data will be used and about any associated risks. Only
24 responses were received back, yet it was a sufficient number to develop a conceptual
model for the simulator and test it.

To develop the simulation model, a field study was conducted in schools of Rezekne
city, Latgale region of the Republic of Latvia. Rezekne is the seventh-largest city in the
Republic of Latvia and the largest eastern border city of the European Union (Figure 1). The
field study was conducted in seven secondary schools of Rezekne. During the observations,
the emphasis was put on quantitative measurements of uneaten food (plate waste) by
examining at least 7000 school lunch plates. To measure food intake duration and path

Nutrients 2022, 14, 587 4 of 19 
 time, not influencing children and excluding them from observations, the FIFO (first in,

first out) method was applied, recording only the time when the first and last child entered
and left the canteen.

 
FigFuigreu r1e. 1M. Mapa pwwitihth tthhee oobbsseerrvvaatitoionnlo lcoactiaotnio. n. 

3.2. Important Parameters  
Various parameters were investigated to improve our Monte Carlo model. Each pa-

rameter is described in a separate subchapter: (1) a portion size (Section 3.2.1); (2) an eating 
rate (Section 3.2.2); (3) eating habits (Section 3.2.3); (4) children’s preferences (Section 
3.2.4). 

3.2.1. A portion Size 
The nutritional norms for Latvian schools are defined in regulation No. 172 “Regula-

tions Regarding Nutritional Norms for Educatees of Educational Institutions, Clients of Social 
Care and Social Rehabilitation Institutions and Patients of Medical Treatment Institutions”. Ac-
cording to the version of 28 August 2020, which was in force when the study was com-
pleted, three types of menu had to be provided at school: (1) the main dish and soup (MS); 
(2) the main dish and dessert (MD); (3) or soup and dessert (SD). The main nutritional 
norms for educatees of general primary and secondary education institutions are defined 
by the following parameters (using minimal and maximal values): energy value (kcal), 
proteins (g), fats (g) and carbohydrates (g); which are grouped by grades 1–4, 5–9 and 10–
12; however, the quality of nutrition is defined by many parameters, e.g., another food 
product must be included in the meal each day: (1) food products rich in complex carbo-
hydrates; (2) vegetables, fruit or berries (including in fresh form); (3) food products rich 
in proteins; (4) milk or dairy or cultured products. At the same time, the weekly menu 
must contain: (1) at least 200 g (net) of lean meat or fish (fillet); (2) at least 225 g (net) of 
potatoes; (3) at least 450 g of dairy, cultured products or products rich in milk proteins 
(cottage cheese, cheese); (4) at least 700 g (net) of vegetables (except for potatoes) and fruit 
or berries, of which at least 250 g in fresh form. Further, the legislation defines many other 
requirements and restrictions, which must be considered when developing a menu. The 
integration of all these requirements into the simulator is a challenging task; therefore, the 
review of online published menus was completed to simplify a portion generation model 
by developing a special classification system applicable to the simulator. The resulting 
model is depicted in Figure 2. The portion is expressed by Equation (1), but their proba-
bility distributions are de𝑝p=ict𝑚ed+ in𝑠 T+ab𝑠𝑑le+ 1.𝑙 𝑑 + 𝑏 + 𝑓𝑝 + 𝑚𝑘 (1) 
where p—a portion size (g), m—a main dish (g), s—a soup (g), sd—a solid dessert (g), ld—
a liquid dessert (g) such as a juice or a tea with sugar, b—bread (g), fp—a fresh product 
(g), mk—milk (g). 

Additionally, the review showed that each type of menu has its own probability: (a) 
the main dish and a soup—65%; (b) the main dish and a dessert—30%; (c) a soup and a 
dessert—5%. 

 



Nutrients 2022, 14, 587 4 of 19

The business logic of the Monte Carlo model was described using a flowchart and
pseudocodes (see Section 3.3) based on the experimental development of the simulator by
using Python and Jupyter Notebook.

3.2. Important Parameters
Various parameters were investigated to improve our Monte Carlo model. Each pa-

rameter is described in a separate subchapter: (1) a portion size (Section 3.2.1); (2) an eating
rate (Section 3.2.2); (3) eating habits (Section 3.2.3); (4) children’s preferences (Section 3.2.4).

3.2.1. A portion Size
The nutritional norms for Latvian schools are defined in regulation No. 172 “Regulations

Regarding Nutritional Norms for Educatees of Educational Institutions, Clients of Social Care and
Social Rehabilitation Institutions and Patients of Medical Treatment Institutions”. According
to the version of 28 August 2020, which was in force when the study was completed,
three types of menu had to be provided at school: (1) the main dish and soup (MS);
(2) the main dish and dessert (MD); (3) or soup and dessert (SD). The main nutritional
norms for educatees of general primary and secondary education institutions are defined
by the following parameters (using minimal and maximal values): energy value (kcal),
proteins (g), fats (g) and carbohydrates (g); which are grouped by grades 1–4, 5–9 and 10–12;
however, the quality of nutrition is defined by many parameters, e.g., another food product
must be included in the meal each day: (1) food products rich in complex carbohydrates;
(2) vegetables, fruit or berries (including in fresh form); (3) food products rich in proteins;
(4) milk or dairy or cultured products. At the same time, the weekly menu must contain:
(1) at least 200 g (net) of lean meat or fish (fillet); (2) at least 225 g (net) of potatoes; (3) at
least 450 g of dairy, cultured products or products rich in milk proteins (cottage cheese,
cheese); (4) at least 700 g (net) of vegetables (except for potatoes) and fruit or berries, of
which at least 250 g in fresh form. Further, the legislation defines many other requirements
and restrictions, which must be considered when developing a menu. The integration of all
these requirements into the simulator is a challenging task; therefore, the review of online
published menus was completed to simplify a portion generation model by developing a
special classification system applicable to the simulator. The resulting model is depicted in
Figure 2. The portion is expressed by Equation (1), but their probability distributions are
depicted in Table 1.

p = m + s + sd + ld + b + f p + mk (1)

where p—a portion size (g), m—a main dish (g), s—a soup (g), sd—a solid dessert (g), ld—a
liquid dessert (g) such as a juice or a tea with sugar, b—bread (g), fp—a fresh product (g),
mk—milk (g).

Nutrients 2022, 14, 587 5 of 19 
 Additionally, the review showed that each type of menu has its own probability: (a)

the main dish and a soup—65%; (b) the main dish and a dessert—30%; (c) a soup and a
dessert—5%.

 
 

(a) (b) 
FFiigguurree 2.. Generrattiion modeello offa al ulunnchchp porotriotino:n(:a ()am) manadnadtoartyorpya prta;r(tb; )(bop) toiopntiaolnpaalr pt.art. 

Fruits belong to categories “solid dessert” (Sd) or “fresh products” (Fp). This relation 
was described as a logical condition AND. The review of the menu showed that a combi-
nation of fresh products and solid desserts belongs to the range of 100–200 g. The content 
of lunch portions, which were monitored during the observation time, are depicted in 
Table 2 considering Equation (1). 

Table 1. Simulation parameters for meal portion generation. 

Meal Component Weight (g) Distribution Python 
Main dish (M) [150; 430] gumbel np.random.gumbel (225, 37.5) 

Soup (S) [150; 300] normal np.random.normal (225, 37.5) 
Solid dessert (Sd) [50; 100] normal np.random.normal (75, 12.5) 

Liquid dessert (Ld) [150; 250] normal np.random.normal (200, 25) 
Bread (B) [20; 35] exponential np.random.exponential (1.2) + 20 

Fresh product (Fp) [50; 100] normal np.random.normal (75, 12.5) 
Milk (Mk) 200 const 200 

[150; 250] + np.random.normal (200, 25) 
Main dish & soup (MS) [150; 200] normal × 2 np.random.normal (175, 12.5) 

[15; 50] + np.random.normal (32.5, 8.75) 
Solid & liquid dessert (D) [100; 200] normal × 2 np.random.normal (150, 25) 

Table 2. Menus of schools in the observation week. 

Day m (g) s (g) sd (g) ld (g) b (g) fp (g) mk (g) p (g) 
Mon 300 0 40 210 25 0 0 575 
Tue 205 0 180 200 25 25 0 635 
Wed 230 255 0 200 25 30 0 740 
Thu 230 0 180 200 25 30 0 665 
Fri 240 125 0 200 25 0 0 590 

m—a main dish, s—a soup, sd—a solid dessert, ld—a liquid dessert, b—bread, fp—a fresh product, 
mk—milk, p—a portion size. 

3.2.2. An Eating Rate 
A literature analysis identified a paper by Zandian et al. [25], which provides meas-

urements of a school lunch eating rate. They modeled cumulative food mass intake using 
Equation (2):  𝑒(𝑡) = 𝑘𝑡 + 𝑣 𝑡, (2) 
where k—is the degree of eating rate acceleration over the course of the meal, and the 𝑣 —
is the initial speed of eating. According to Zandian et al. [25] measurements, girls had the 
initial eating rate equal to 34(5) g/min and the deceleration −2.6(1.4) g/min2, while boys 
−42(7) g/min and −2.7(1.1) g/min2, respectively; however, considering the integration of 

 



Nutrients 2022, 14, 587 5 of 19

Table 1. Simulation parameters for meal portion generation.

Meal Component Weight (g) Distribution Python
Main dish (M) [150; 430] gumbel np.random.gumbel (225, 37.5)

Soup (S) [150; 300] normal np.random.normal (225, 37.5)
Solid dessert (Sd) [50; 100] normal np.random.normal (75, 12.5)

Liquid dessert (Ld) [150; 250] normal np.random.normal (200, 25)
Bread (B) [20; 35] exponential np.random.exponential (1.2) + 20

Fresh product (Fp) [50; 100] normal np.random.normal (75, 12.5)
Milk (Mk) 200 const 200

Main dish & soup (MS) [150; 250] +
[150; 200] normal × 2 np.random.normal (200, 25)

np.random.normal (175, 12.5)

Solid & liquid dessert (D) [15; 50] +
[100; 200] normal × 2 np.random.normal (32.5, 8.75)

np.random.normal (150, 25)

Fruits belong to categories “solid dessert” (Sd) or “fresh products” (Fp). This relation
was described as a logical condition AND. The review of the menu showed that a combina-
tion of fresh products and solid desserts belongs to the range of 100–200 g. The content of
lunch portions, which were monitored during the observation time, are depicted in Table 2
considering Equation (1).

Table 2. Menus of schools in the observation week.

Day m (g) s (g) sd (g) ld (g) b (g) fp (g) mk (g) p (g)
Mon 300 0 40 210 25 0 0 575
Tue 205 0 180 200 25 25 0 635
Wed 230 255 0 200 25 30 0 740
Thu 230 0 180 200 25 30 0 665
Fri 240 125 0 200 25 0 0 590

m—a main dish, s—a soup, sd—a solid dessert, ld—a liquid dessert, b—bread, fp—a fresh product, mk—milk, p—a
portion size.

3.2.2. An Eating Rate
A literature analysis identified a paper by Zandian et al. [25], which provides mea-

surements of a school lunch eating rate. They modeled cumulative food mass intake using
Equation (2):

e(t) = kt2 + v0t, (2)

where k—is the degree of eating rate acceleration over the course of the meal, and the v0—is
the initial speed of eating. According to Zandian et al. [25] measurements, girls had the
initial eating rate equal to 34(5) g/min and the deceleration −2.6(1.4) g/min2, while boys
−42(7) g/min and −2.7(1.1) g/min2, respectively; however, considering the integration of
the food mass intake function (see Equation (3)), the declared deceleration must be doubled.

∫ ∫ at2
e(t) = v(t)dt = (v0 + at)dt = v0t + + C. (3)

2

As a result, the eating rate deceleration of girls was−5.2(2.8) g/min2 and−5.4(2.2) g/min2

for boys. Finding the extremum time (Equation (4)), it is possible to find the maximal food
mass intake (Equation (3)) until the eating rate achieves zero.

v0 + at = 0. (4)



Nutrients 2022, 14, 587 6 of 19 
 

the food mass intake function (see Equation (3)), the declared deceleration must be dou-
bled. 𝑒(𝑡) = 𝑣(𝑡)𝑑𝑡 = (𝑣 + 𝑎𝑡)𝑑𝑡 =  𝑣 𝑡 + + 𝐶. (3) 

As a result, the eating rate deceleration of girls was −5.2(2.8) g/min2 and −5.4(2.2) 
g/min2 for boys. Finding the extremum time (Equation (4)), it is possible to find the maxi-
mal food mass intake (Equation (3)) unti𝑣l th+e 𝑎e𝑡at=in0g rate achieves zero. 

. (4) 
Using the average initial speed and the average deceleration, the maximal intake 

must be 111.15 (g) within 6.5 (min) for girls and 163.3 (g) within 7.7 (min) for boys. That 
is strongly smaller than the declared average food intake and lunch duration: (a) girls—
258(38) g and 10.7(2.1) min; (b) boys—289(73) g and 8.8(1.8) min. 

According to the conclusions of experts, children are eating at a decelerating speed 
Nutrients 2022, 14, 587 in the first part of a lunch, then maintain a constant speed of eating 6[2of61]9; therefore, the 

food intake model with eating speed deceleration could be applied to correct the previous 
ca𝑒l(c𝑡u)l=ation𝑣 d(𝑡i)ff𝑑e𝑡re=nce(s𝑣 (se+e 𝑎E(q𝑡u)𝑡a)ti𝑑o𝑡n= (5))(: Using the average initial speed and the averag𝑣e d+ece𝑎ler𝑡a+tio𝑥n,𝑡th)e𝑑m𝑡a=xim 𝑣al𝑡in+tak𝑎e2𝑡mu+st
be 111.15 (g) within 6.5 (min) for girls and 163.3 (g) within 7.7 (min) for boys. That is strongly 𝑥
smaller than the declared average food intake and lunch duration: (a) girls—258(38) g and 3𝑡 +  𝐶 (5) 
10.7(2.1) min; (b) boys—289(73) g and 8.8(1.8) min.
wheArec c𝑎ord—inigs tothteh eincoitnicallu seiaotnisnogf esxppeeerdts ,acchciledlreernaatiroenea, tbinugt axt—a dtehcee leeraattiinngg ssppeeeded acceleration. 
Rinetchaelcfiurslat tpiaornt  opfraovluindcehd,  tthheen fmolalionwtain ga  cvoanlsutaenst: (sap)e egdirolsf —eat0in.5g5[ g26/]m; tihne3r;e (fbor)e b, othyes—0.56 g/min3. 
Tfohoids innteawke mooddeellw isit hdeeaptiincgtesdp eiend Fdiegceulreera 3ti.o n could be applied to correct the previous
calculHatioown deviffeerr,e nFcaegs e(srebeeErqgu eatti oanl.( 5[)2):∫ ∫ ∫3(] applied a m)ore simple model for food intake speed 
calculation—constant average speed (see Eq𝑣̅u=ati𝐸on (6)): a t2 xt3

e(t) = v(t)dt = (v0 + a(t)t)dt = v 2
0 + a0t + xt dt = v0t + 0 + + C (5)

2 3

where a0—is the initial eating speed acceleration, but x—𝑡  (6) 
the eating speed acceleration.

Recalculation provided the following values: (a) girls—0.55 g/min3; (b) boys—0.56 g/min3.
wThhisenreew E—mofdoeoldis mdeapsicst eidntiankFeig duurer3in. g time t. 

 
FFiigguurree3 .3C. Comobminbeidndedia gdraiamg:rsaomlid: lsioneli—d floionde—mafsosoindt amkeaasms oinuntat,kdea sahmedoluinnet—, deaatsinhgedra tlein. e—eating rate. 

However, Fagerberg et al. [23] applied a more simple model for food intake speed
calculTathioen r—esceoansrtcahn tsatuvedryag beysp Feaegde(rsebeeErgqu eatt iaoln. [(26)3)]:  has shown that there is a strong correlation 
(Pearson’s r = 0.667, p < 0.001) between the objective eating rate (g/min) and food mass 
intake (g) during school lunch. Add E

vi=tionally, the correlation between the (B6)MI z-score and 
t

eating speed: “a BMI z-score below 0 had a significantly lower eating rate (g/min) vs. stu-
dwehnertes Ew—hfoo ohdamda as sBinMtaIk ze-dsucroirneg etiqmueatl. to or above 0 (28.2 g/min vs. 35.9 g/min, respectively), 
t The research study by Fagerberg et al. [23] has shown that there is a strong correlation
(hPeea mrsoena’ns  rd=if0fe.6r6e7n, cpe< =0 −.070.17) gbe/mtwiene,n pt h=e 0o.0bj1e2ct,i 9ve5%ea tCinIg −r1a4te g(/gm/minin t)oa −n1d.8fo god/mmians”s [23]; however, 
“instlaokwe ( ge)adteurrisn”g hscahvoeo lslumnachll.eAr dfdoiotidon amllya,stsh eincotarrkeela ttiohnanbe t“wfaeesnt tehaetBerMsI”z. -Cscoorme apnadring the eating 
sepateinegds bpeetdw: e“eanB MSwI ze-sdciosrhe  baenlodw G0rheaedka sstiugndifiencatnst,l ya lsoiwgenriefiactianngtr adtieff(ge/remninc)ev ws.asstu n- ot found. The 
ddeenstcsrwiphtoivhea dstaaBtiMstIiczs-s coofr etheeq umaletnotoiroanbeodv es0tu(2d8y.2 wg/emrein pvrse.s3e5n.9teg/dm aisn ,ar esscpaetctteivrepllyo),t. The minimal 
the mean difference = −7.7 g/min, p = 0.012, 95% CI −14 g/min to −1.8 g/min” [23];
however, “slow eaters” have smaller food mass intake than “fast eaters”. Comparing
the eating speed between Swedish and Greek students, a significant difference was not

 found. The descriptive statistics of the mentioned study were presented as a scatterplot.
The minimal speed was near 10 g/min and the maximal—95 g/min (in the case of the 1st
observation). The linear function is approximately equal to Equation (7):

E(v) = 6.8v + 125 (7)



Nutrients 2022, 14, 587 7 of 19

Therefore, the average speed depending on food mass intake can be found by Equation (8):

E− 125
v(E) = (8)

6.8

It is possible to find the average speed of the model proposed by Zandian et al. [25]
using Equation (9):

a
v 0t2 xt3

0t + + = vt, (9)
2 3

the results are as follows: (a) the average eating speed of girls is 27.16 g/min; (b) boys—
32.7 g/min, which are comparable with the values mentioned by Fagerberg et al. [23].

Zandian et al. [25] and Fagerberg et al. [23] conducted their study on the main
dish. A soup is a liquid substance; therefore, the eating rate of soup must be higher.
Ferriday et al. [27] proposed a study on tomato soup (400 mL) consumed through tubing:
(a) slow rate—30 mL/min; (b) fast rate—118 mL/min; in other words, approximately
30 g/min and 118 g/min. Traditionally, a soup contains some solid mass; the normal rate
can be a doubled eating rate of the main dish.

To measure food intake duration and path time, not influencing children and exclud-
ing the{m from observations, the FIFO (first in, first out) method was applied, recording
only the time when the first and last child entered (T = {tmin; tmax}) and left the canteen
(T′

}
= t′min; t′max ). The path time was calculated as a mean of means (µT and µT′ respec-

tively); however, the food intake duration was calculated as a mean of means (µT′−T) after
subtracting the entering time from the leaving time.

The observations at the schools showed the average lunch consumption time was
equal to 8.1 min. It must be considered that children did not eat the whole portion, and
plate waste was produced; however, the average eating rate was 47 g/min.

Considering the portion mass without drinking (390–540 g) and Equation (7), the
eating rate must belong to the range [39; 61]. Additionally, Zandian et al. [25] mention
that boys and girls eat faster in restricted time, 166% and 183%, respectively; therefore, the
observed eating rate satisfies the ranges investigated by other authors.

Therefore, the eating rate of 35(5) g/min and a linear model can be a compromise for
the simulator because the ideal conditions cannot always be provided, and children can feel
some internal or external stress; however, the model with a decreasing speed (Equation (5))
can obtain the characteristics of a linear model for a restricted lunch time frame ( a0 → 0
and x → 0).

3.2.3. Children’s Eating Habits
Food preferences are the product of an interplay between genetic and environmental

factors that result in substantial individual differences to the extent to which children
are suspicious and fussy about food in general and in their likes and dislikes for specific
foods [28]. De Cosmi et al. [29] provided a comprehensive review of children’s eating
and activity behaviors influenced by both intrinsic (genetics, age, gender) and extrinsic
(family, peers, community, and society) factors. Eating habits influence children’s decision
making; therefore, the objectives of our survey were to identify children’s decisions related
to hated food and their frequency (see Figure 4), as well as to investigate how children
meet their satiation and the competitive food impact on school lunches (see Tables 3 and 4).
The competitive food probability was calculated, adding up the answers of subcategories.
Somewhere 30% of children eat competitive food; however, 67% of children decide to stop
eating if time is not sufficient to return to a classroom.



Nutrients 2022, 14, 587 8 of 19 
 

Nutrients 2022, 14, 587 8 of 19

 
Figure 4. Children’s decisions concerning rejected food.

Figure 4. Children's decisions concerning rejected food. 
Table 3. Survey answers about competitive food impacts on the package menu.

Table 3. Survey answers a
Answers Ibmopauctto cf othme Spcheotoiltive foImopdac tiomf Cpoamcptesti toivne F tohode package menu. 

Optional Menu from Outside the School
Eat 0–24% 22.2% 25.0%

Answers Impact of the School Optional Impact of Competitive Food from 
Eat 25–49% 11.1% Menu 25.0% Outside the School 
Eat 50–74% 33.3% 25.0%

EatE 0at–752–410%0% 33.3% 22.2% 25.0% 25.0% 
Eat 25–49% 11.1% 25.0% 

TablEe 4a. tS u5rv0ey–a7n4sw%ers about the sources of competiti3ve3f.o3od%.  25.0% 
EAanstw 7er5s –10H0o%me Food School Outside the Probability of

Optional Menu 33.3S%cho ol Competitive Food 25.0% 
Yes 12.5% 33.3% 16.7% 21.0%

TableN o4. Survey7 5a.0n%swers ab4o5.u8%t the sourc5e4.s2% of competit5i8v.0e% food. 
Sometimes 12.5% 20.8% 29.2% 21.0%

School Optional Outside the Probability of Com-
3.2.A4. nChsilwdreenr’ssF ood PHreofermenece sFood 

Children from different socioeconomic regions hMaveednifufer ent food preferenceSs c[3h0]o, ol petitive Food 
e.g., Ragelienė [31] discussed the differences between the food preferences of Lithuanian
and DaYnisehsc hildren. It mea1ns2t.h5a%t lo cal data must be3ap3p.l3ie%d f or the simulation. 16.7% 21.0% 

OuNr suor vey investigated7t5h.r0ee%ca tegories of food: (41)5s.o8u%p; ( 2) the main dish; (3) s5w4e.e2t % 58.0% 
drinks (see Table 5).
Sometimes 12.5% 20.8% 29.2% 21.0% 

Table 5. Children’s food preferences.

3.2A.n4s.w eCrshildDroeNnot’Esa tFSoouopd PDroeNfoetrEeatnthceeMsa in Dish Do Not Drink Sweet Drinks
Yes 50% 8% 0%
NCo hildren 5f0r%om different s9o2%cioeconomic reg1i0o0%ns have different food preferences [30], 

e.g., Ragelienė [31] discussed the differences between the food preferences of Lithuanian 
If a whole list of food products and recipes is applied for a survey to investigate chil-

adnredn’ sDpraefneriesnhce sc, hit islda trimene-c.o Ints ummiengapnrsoc teshs;acth ildorcenaall sdoacatnan omt huavsetg absetro anopmpiclied for the simulation. 
experience or cannot know their titles. Additionally, these preferences can be impacted
and mOoduelerd s; uhorwveeveyr, ianrvesetrsictteigd alisttemdin tihmrizeeset cheastcehgooolrfrieeesd oomf rfeolaotedd :t o(1m)e nsuoup; (2) the main dish; (3) sweet 

ddreivnelokpsm (enste; teh eTreafobrel,eit w5a)s. decided to leave only one parameter for input—the number
of children unsatisfied with the school meal.

Table 5. Children's food preferences. 

Answers Do Not Eat Soup Do Not Eat the Main Dish Do Not Drink Sweet Drinks 
Yes 50% 8% 0% 
No 50% 92% 100% 

If a whole list of food products and recipes is applied for a survey to investigate chil-
dren's preferences, it is a time-consuming process; children also cannot have gastronomic 
experience or cannot know their titles. Additionally, these preferences can be impacted 
and modeled; however, a restricted list minimizes the school freedom related to menu 
development; therefore, it was decided to leave only one parameter for input—the num-
ber of children unsatisfied with the school meal. 

Investigating how frequently children are not satisfied with school food (Figure 5), 
the survey showed two peaks, which can relate to two groups: “satisfied children” and 
“unsatisfied children”. Of course, the sample population must be increased; however, this 
principle can be applied to generate the frequency of hated food based on selected as-
sumptions: (a) 0(0.5) days for satisfied children; (b) 3(0.5) days—for unsatisfied children. 
Of the total children, 27% were unsatisfied with school food for more than one day. 

 



Nutrients 2022, 14, 587 9 of 19

Investigating how frequently children are not satisfied with school food (Figure 5),
the survey showed two peaks, which can relate to two groups: “satisfied children” and
“unsatisfied children”. Of course, the sample population must be increased; however,
this principle can be applied to generate the frequency of hated food based on selected
assumptions: (a) 0(0.5) days for satisfied children; (b) 3(0.5) days—for unsatisfied children.

Nutrients 2022, 14, 587 Of the total children, 27% were unsatisfied with school food for more than one day. 9 of 19 
 

The observations at the schools showed that the largest food waste, 37%, related
to liquid desserts (sweet tea, juice and lemon water); however, the total plate waste

Nutrients 2022, 14, 587 was 27.63%, and 23.28%, excluding the liquid dessert. All the categories are depicted 9 of 19 
 in Figure 6. These distributions of food waste amount can be considered for rejected

food: Mw = norm(0.30, 0.05), Sw = norm(0.15, 0.03), Sdw = 0.02, Ldw = norm(0.35, 0.07),
Fpw = norm(0.3, 0.10), Bw = 0.05 (Python).

 
Figure 5. How frequently children are unsatisfied with a lunch. 

The observations at the schools showed that the largest food waste, 37%, related to 
liquid desserts (sweet tea, juice and lemon water); however, the total plate waste was 
27.63%, and 23.28%, excluding the liquid dessert. All the categories are depicted in Figure 
6. These distributions of food waste amount can be considered for rejected food: Mw = 
norm(0.30, 0.05), Sw = norm(0.15, 0.03), Sdw = 0.02, Ldw = norm(0.35, 0. 07), Fpw = norm(0.3, 
F0i.g1u0r)e, 5Bw

. H =o w0.f0r5eq (uPeyntthlyocnh)i.l dren are unsatisfied with a lunch.
Figure 5. How frequently children are unsatisfied with a lunch. 

The observations at the schools showed that the largest food waste, 37%, related to 
liquid desserts (sweet tea, juice and lemon water); however, the total plate waste was 
27.63%, and 23.28%, excluding the liquid dessert. All the categories are depicted in Figure 
6. These distributions of food waste amount can be considered for rejected food: Mw = 
norm(0.30, 0.05), Sw = norm(0.15, 0.03), Sdw = 0.02, Ldw = norm(0.35, 0.07), Fpw = norm(0.3, 
0.10), Bw = 0.05 (Python). 

 
FFiigguurere6 .6O. Obsbesrevrevdefdo ofodowda wsteasgtreo ugproeudpbeyds ibmyu sliamtiounlactaitoeng ocrayt.egory. 

33.3.3. .T ThheeM MonotnetCe aCralorlMo oMdeoldel  
The time unit of the simulation model is a week. Each week the menu is presented by a
The time unit o→f the( →simul→ation →mode→l is a →wee)k. Each week the menu is presented 

sbeyt  oaf speatc koaf gpeamckeangues mP e=nusp m𝑃⃗on=, (p𝑝⃗tue, p, 𝑝⃗wed, , 𝑝⃗p thu, , 𝑝⃗p f ri , 𝑝⃗, wh)e,r ewehaecrhep eaacckha gpeamckeangue( wm)enu (𝑤) 
iissd deessccrirbibededb ybyE qEuqautiaotnio(n1) .(1E)a. cEhamche nmuewnuis wge inse graetneedrcaotendsi dceorninsigdtehreinsgch tehme esdchepemictee ddepicted 
in Figure 2 and the distributions described in Table 1, where each type of menu has its
oinw nFipgruobrea b2il iatyn:d( at)hteh edmisatrinibduitsihoannsd daessocuripb—ed6 5i%n ;T(ba)btlhee 1m, awinhderiseh eaancdha tydpeses eorft— m3e0n%u;  has its 
(oc)wans opurpobaanbdilaitdye: s(sae)r tt—he5 %m.aBinre dadishis aadndde ad swoiuthp—a p6r5o%ba; b(ibli)t ythoef 5m0%ai.nF dreisshh parnodd uac tdsessert—
a3n0d%m; (ilck) aar esoaudpd eadnwd iath daepssreorbta—bi5li%ty. oBfr3e3a%d fiosr aedadche;dh wowitehv ear ,ptrhoebtaybpieliotyf d oefs s5e0r%t (.s Folrieds,h prod-
luiqcutsid aonrdb motihlk)  iasrsee laedctdeeddw witihtha au npirfobrmabpilriotyb aobfi l3it3y%(3 f3o%r )e.aTche; hreolwatedveprs, etuhdeo tcyopdee oisf dessert 
d(seopliicdte, dliiqnuTiadb loer6 b. oth) is selected with a uniform probability (33%). The related pseudo-
code is depicted in Table 6. 

  
 

Figure 6. Observed food waste grouped by simulation category. 

3.3. The Monte Carlo Model  
The time unit of the simulation model is a week. Each week the menu is presented 

by a set of package menus 𝑃⃗ = (𝑝⃗ , 𝑝⃗ , 𝑝⃗ , 𝑝⃗ , 𝑝⃗ ), where each package menu (𝑤) 
is described by Equation (1). Each menu w is generated considering the scheme depicted 
in Figure 2 and the distributions described in Table 1, where each type of menu has its 
own probability: (a) the main dish and a soup—65%; (b) the main dish and a dessert—
30%; (c) a soup and a dessert—5%. Bread is added with a probability of 50%. Fresh prod-

 
ucts and milk are added with a probability of 33% for each; however, the type of dessert 
(solid, liquid or both) is selected with a uniform probability (33%). The related pseudo-
code is depicted in Table 6. 

  

 



Nutrients 2022, 14, 587 10 of 19

The plate waste is a result of two agents’ interaction: a week menu and children
→ { →}

(L = 〈P ; C 〉). Each child represents a set of three parameters c = v; e f ; N′ capturing an
eating rate, external food and the hated menu vector, which contains logical values ‘true’ or
‘false’ (n′ = {0; 1}). A child generation pseudocode is depicted in Table 7. The plate waste

→′
calculation is completed in three stages: (1) competitive food impact (we f ); (2) rejected food

→′ →′
impact (wh); (3) insufficient time impact (wt), if a child decides (d) to stop lunch or come
late to a classroom.

The core logic of the Monte Carlo model relates to plate waste calculation. It was
decided to represent a lunch portion as Equation (10):

p = e(t) + w′t(t) + w′h + w′e f , (10)

where w′t—plate waste (g) impacted by insufficient time, w′h—impacted by rejected food,
w′e f —impacted by competitive food. If e(t) and w′t(t) depend on time, w′h and w′e f Produces
constant plate waste; however, the rejected food amount depends on the competitive food
impact because children are already overfi(lled ()Equation (11)).

C = w′ w′ ′
h e f + we f . (11)

Mathematically, the rejected f{ood can be calculated using Equation (12):

w′h = rand− w′e f (12)
w′h ≥ 0

Table 6. Pseudocode for week menu generation.

Attributes Pseudocode
k—type of menu; Generate the main part:
MS—distribution “main dish & soup”; m = s = 0
MD—distribution “main dish & dessert”; k← rand({MS, MD, SD}, {0.65, 0.30, 0.05})
SD—distribution “soup & dessert”; i f k = MD : m ∈ MD
m—main dish (g); eli f k = SD : s ∈ SD
s—soup (g). else : {m, s} ∈ MS
dtype of dessert; Generate a dessert:
Sddistribution “solid dessert”; sd = ld = 0
Lddistribution “liquid dessert”; d← rand( {Sd, Ld, D} )
Ddistribution “solid & liquid desserts”; i f d = Sd : sd ∈ Sd
sdsolid dessert (g); eli f d = Ld : ld ∈ Sd
ld—liquid dessert (g). else : {sd, ld} ∈ D
otype of optional part; Generate an optional part:
Bdistribution “bread”; b = f p = 0
Fpdistribution “fresh products”; i f rand({0; 1}) : b ∈ B
Mkdistribution “milk”; o ← rand( {Fp, Mk, ∅} )
f pfresh products (g); i f o = Fp : f p ∈ Fp
mk—milk (g). eli f o = Mk : mk ∈ Mk
→ →
p —meal portion. return : p = { m, s, sd, ld, b, f p }

Distributions of categories are provided in Table 1.



Nutrients 2022, 14, 587 11 of 19

Table 7. Pseudocode for child generation.

Attributes Pseudocode
prprobability that a child is unsatisfied Generate a child (pr) :
with school food; vs = norm( 35, 5 )
vseating rate of solid food (g/min); vl = 2·vs
vleating rate of liquid food (g/min); e f = rand( {0; 1}, {0.7; 0.3} )
e f user of competitive food; u = rand( {0; 1}, {1− pr; pr} )
u—child unsatisfied with school food.

Generate days of rejected food(u) :
→′ i f u = 1 :h = norm( 3, 0.5 ), 0 ≤ h ≤ 5
N —days of rejected food. else : h = norm( 0, 0.5 ), 0 ≤ h ≤ 5

→′
N = { n′| N{′(1) = h & N}′(0) = 5− h }

→ →′
c—child. return : c = v , e f , N

The related pseudocodes are depicted in Tables 8 and 9.

Table 8. Pseudocode for competitive food impact calculation.

Attributes Pseudocode
→
p (

meal portion; →)
Calculate competitive food impact p :

k—average impact of competitive food;
→′ k = rand( {0.12, 0.37, 0.62, 0.87} )
we f —plate waste due to →′ →
competitive food. we f = p · norm({k, 0.06 )

→′ }
return : we f = wm

e f , ws , wsd d p
e f e f , wl

e f , w f
e f , wb

e f

Table 9. Pseudocode for rejected food impact calculation.

Attributes Pseu(docode
→′ )

Calculate rejected food we f :
→′
w →′ →

h—plate waste due to rejected food; wh = p ·(Mw, Sw, Sdw, Ldw, Fpw, Bw)
{Mw, Sw, Sdw, Ldw, Fpw, Bw} waste hs = rand( {0; 1} )
distributions by food categories; i f hs = 1 : ws

h = ps
hs child does not eat soup; hm = rand( {0; 1} , {0.08, 0.92} )
hm—child does not eat the main dish. i f h m m

m = 1 : wh = p
→′ →′
wh = p− we f ,{where wi

h ≥ 0
→′ }

return : w d f p
h = wm

h , ws
h, wsd

h , wl
h , wh , wb

h

The results in the form of a flowchart for plate waste simulation are depicted in Figure 7.
The simulation was repeated 10,000 times to investigate the impacts of parameters.



NutNruietnritesn 2ts022022, 21,41,4 5, 85787 12 of 1 12 of 19 
 9

 
Fiigguurree7 7. .F Flolwowchcahrat rotf opfl aptelawtea swteasitme usilmatiuolna.tion. 
3.4. Quality Control
3.4. Quality Control 

The root mean square error (RMSE) was applied to measure the forecasting error of the
develoTpheed rsoimotu mlaetoarn.  Ssoqmuearsec heororlosrh (aRdMdSifEfe)r ewntaslu anpchpllieendg tthos mfoeradsiuffreere tnhtec lfaosrseecsa; tshtienreg- error of 
ftohree ,dtheevefolorepceadst isnigmreuslualttowr.a Ssocommep sacrhedoowlsit hhoabds edrivfefedrpenlatt eluwnacshte lpeenrgwthese kf,ocro ndsiifdfeerrienngt classes; 
theerluenfochred, uthraet ifoonre(sceaestEinquga rteiosnul(t1 3w))a. s compared with observed plate waste per week, con-
sidering the lunch duration (see Equ√ation (13)). 

RMSE =𝑅√√√𝑀 ( )2
∑𝑆𝐸w=t − w∑(′s, t

, , ) , (13) (13) 
N

where 𝑁—number of observations, 𝑡—lunch length corrected considering the walking 
time (min), 𝑠—school, 𝑤 —forecasted plate waste per week (g/week), 𝑤 , —observed 
plate waste per week for school 𝑠, for a child group restricted by lunch duration 𝑡. 

Additionally, a mean average percentage error was applied (see Equation (14)): 

 



Nutrients 2022, 14, 587 13 of 19

Nutrients 2022, 14, 587 13 of 19 
 

where N—number of observations, t—lunch length corrected considering the walking time
(min), s—school, wt—forecasted plate waste per week (g/week), w′s, t—observed plate
waste per week for school s, for a child𝑀g𝐴ro𝑃u𝐸p r=estric%te∑d b, y( lunc, h, d) uration t.

Additionally, a mean average percentage erro(r was app

100% wt − w′
)lied (s.e e Equation (14)): (14) 

Next, assumptions were applied for the simulation based on the previous analysis: 
MAPE =

N ∑N s, t
s,t w′

. (14)
external food probability—0.3, the probability s,otf children unsatisfied with the school 
meal—0.27 and the compromise eating rate—35(5) g/min. 

Next, assumptions were applied for the simulation based on the previous analysis:
external food probability—0.3, the probability of children unsatisfied with the school
m4e. aElx—p0e.2ri7manedntt hReecsoumltpsr omise eating rate—35(5) g/min.

The simulation model has two input parameters (see Figure 7): lunch duration and a 
4p. eErxcpeenritmageen toRf ecshuilltdsren unsatisfied with school food. The results of simulations are de-
pictTehde insi mFiugluatrioe n8m; hoodwelehvaesrt,w Foiginupreu t9p dareapmicettse rssu(rsfeaecFei gtoumreo7g):rlaumncsh tod ueraastiioenr uannddaerstand the 

piemrcpenatcatg oefo ef achchild irnepnuutn psaatirsafimedetweirt honsc hpoloaltefo woda.sTteh.e Freigsuulrtse o1f0s idmeuplaictitosn tshaer eindteepriscetecdtion of real 
in Figure 8; however, Figure 9 depicts surface tomograms to easier understand the impact
odf aeatac hwinitphu tthpea rsaimmeutelartoendp dlaatteaw toas vtea.lFidigautree t1h0ed mepoicdteslt.h e intersection of real data with
the simTuhlea tsecdhdoaotalst ohavdal ilduantechth de umroadtieol.ns of 15, 20, 25 and 30 min. The observed plate waste 
at thTeh escshchooolsls whads liunntechrsdeuctreadti ownsitohf t1h5e,  2s0i,m2u5 laantdio3n0 rmesinu.ltTsh aedojbussetrevde dfoprl awteawlkaisntge time. The 

acththiledsrcehno coolsmwea isnintote trhsec cteadntweeitnh wthiethsi ma udlealtaioyn orfe sauplptsraodxjiumstaetdelfyor uwpa tlok i3n gmtimn—e. tThhee same time 
cwhialdsr ecnoncosimdeerinetdo ftohre aca rnetteuenrnw pitahtha;d tehlaeyreoffoarpe,p trhoxei mtoattaell ydeulpayto w3 amsi ne—quthael tsoa m6 emtiimn.e 
was coTnhsied ecroemd pfoarraisroentu ronf pthateh f;othreerceafsotrien,gth reetsoutaltlsd welaityhw thase eoqbusaelrtvoe6dm pinla. te waste showed an 
RMTShEe ecqoumapl atroi s0o.n03o.f the forecasting results with the observed plate waste showed an

RMSE equal to 0.03.
TThihsisse sceticotniomna my baey dbiev iddievdidinetdo  siunbtose scutibonses.ctItiosnhos.u Ildt sphroovuildde parcoovnicdisee aa ncodnpcriesceis aend precise 

ddeescsrcirpitpiotinonof othf etheex peexrpimereinmtaelnretasul lrtes,suthletsir, itnhteeirrp rienttaetriopnr,eatastwioenll, aass twheeellx paesr itmhee netxapl erimental 
ccoonnclculsuisoinosntsh atht caatn cabne  dbrea wdrna. wn. 

 
FFigiguurere8 .8S.i mSiumlautiloantiorens urlets.ults. 

 



NNuuttrriiNeennuttsrs i e22n00t22s222,,0  112424,,,  155488,775  87 14 of 1 1144  ooff  1199  
  

9

  
((aa))  ((bb))  

FFFiiigguurree  99...  TTooommmoooggrgarrmaamms ossf  oothff  etthhsieem  ssuiimmlatuuiollanattriioeosnnu  lrrteess:suu(all)ttssd::e  ((paai))c  tddteehppeiiiccmtt  ptthhaecet  iiommf prpeaajecccttt  eoodff  rrfoeeojjeedcctoteenddp  fflooatooeddw  ooannst  epp;llaattee  wwaassttee;;  
(((bb)))  ddeeppiiiccctttt  ththheeei m iimmpappcaatccottf  ooluff n llucuhnndcchuh r ddatuuiorrnaattoiioonnnp  looannte  ppwllaasttetee  .wwaassttee..  

  
FFFiiiggguurree  11000...S  SSimiimmuluualltaaiottniioornne s rrueeltsssuuilnltttsse  riisnnettceetrersdseewccttieethddt  hwweiiotthhb s ttehhrveee  oodbbpssleaetrrevvweedda s pptellaaptteeer  wweaaessktteep  eppreecrrl a wwssee, ewekkh  eppreerrt  hccellaassss,,  wwhheerree  
ttbhhoeex  bbpooloxxtpsplaloorettsst  haaerreeo  btthhseeer  vooebbdsseperrlavvteeddw  ppalslaatett.ee  wwaassttee..  

555...  DDDiiissscccuuussssssiiiooonnn  
I
II
n
nn  

s
ss
p
pp
it
ii
e
ttee

o
  
f
oo
t
ff
h
  
e
tthh

fa
ee

c
  ff
t
aa
th
cctt

a
  
t
tt
m
hhaa

a
tt
n
  
y
mm

p
aa
a
nn
r
yy
am
  pp

e
aa
te
rr
r
aa
s
mm

of
eett

th
ee

e
rrss

M
  oo

o
ff
n
  tt

t
hh
e
ee
C
  
a
MM
rl

oo
o
nn
m
ttee
o
  
d
CC
el
aa

w
rrll

e
oo
r
  
e
mm

b
oo
as
dd
e
ee
d
ll  

o
ww
n

ee
th
rree

e
  bbaasseedd  oonn  

tt
statistical data of the survey with only 24 responses, the quality control of the developed
mhheeo  dsstetaal ttsiihssttoiiwccaaelld  ddsaauttafafi  oociffe  ntthhtleey  ssguuorrovvdeeyyre  wwsuiilttthhs—  ooannnllyyR  22M44 S rrEeesswppaoosnnseseqesus,,a  ttlhhteeo  qq±uu3aa%llii.ttyyT  cchooennmttrrioonlli  mooffa  ltthhee  ddeevveell--

ooappneedddm  mmaxooidmdeealll  ssahhboosowwlueetdde  essruurfofffriiscciiweennerttellyy0  .gg5o5o%oodda  nrreedss5uu.l8ltt4ss%—(aathnne  RRsMqMuSSaErEe  wweraarossr  ees—qquu2aa.9ll  7ttoo×  ±±1330%%−5..  aTTnhhdee  mmiinniimmaall  
aa3nn.4dd1  mm×aa1x0x−iimm3,aarell  saapbbesscootillvuuettleey  )ee;rrhrrooowrrsse  vwweree,rrieet   m00..u55s55t%%be  aacnnoddn  s55id..88e44re%%d  ((tththhaeet   tsshqqeuuRaaMrreeS  eEerrwrrooarrsssc—al22cu..99la77te××d1100   aanndd  
33c..o44n11si××de11ri00ng ,t,  hrreessappveecrcattiigvveeevllyya)l)u;;  ehhsoofwworeevavleelrrt,,h  iiett  ommbusuessrttv  bbedee  csccoohnnossoiidldsee; rrtehedder  etthhfoaartte  ,tthhtheee  RReMMrroSSrEEr  ewwlaaatessd  ccaallccuullaatteedd  
cctooonntshsiieddpeerrreiindngigc  tttihhoene  afaovvreearraacggiteey  vvoarallauureeessg  fifooonrr  aaalnllld  tthhneeo  toofbbossreeerravvceehdds  csshccohhooolooillnssd;;  ittvhhiederrueeaffloolyrr.eeI,, n tthhaeed  deeirrtrriooonrr  ,rreellaatteedd  ttoo  
tt
t
hh
h
ee
e
  pp
st

rr
a
ee
ti
dd
st
ii
i
cc
c
tt
a
ii
l
oo

d
nn

a
  ff
ta
oorr

a
  
p
aa

p
  cc

li
ii
e
ttyy
d
  
f
oo
o
rr
r
  aa

th
  rr

e
ee

s
gg
im
iioo

u
nn

l
  
a
aa
t
nn
o
dd
r r

  nn
ep
oo

r
tt
e
  ff
s
oo
en
rr  

t
ee
e
aa
d
cc
a
hh

s
  ss
u
cc
m
hh

m
oooo

a
ll
r
  
y
iinn

fo
dd

r
iivv
a
ii
c
dd
it
uu
y.
aa

A
llllyy

s
..
r
  
e
IInn
ga
  aa
rd
dd

s
ddiittiioonn,,  tthhee  

ss
the precision, Malefors et al. [21] mention: “The past year was used for testing the models
attgaaattiiissnttsiitccaarell a ddlaaottbaas  eaarppvppaltliiioeendds  ff.ooTrr h ttehheec u ssriirmmenuutllaabttuoosrrin  rreeesppsrraeessseeunnsutteeaddl   saac  essnuuammriommraaerrsyyu  lfftoosrri  naa  accniittyyav..  AeArsas g rreeeggaarrddss  tthhee  

pprreecciissiioonn,,  MMaalleeffoorrss  eett  aall..  [[2211]]  mmeennttiioonn::  ““TThhee  ppaasstt  yyeeaarr  wwaass  uusseedd  ffoorr  tteessttiinngg  tthhee  mmooddeellss  
aaggaaiinnsstt  rreeaall  oobbsseerrvvaattiioonnss..  TThhee  ccuurrrreenntt  bbuussiinneessss  aass  uussuuaall  sscceennaarriioo  rreessuullttss  iinn  aann  aavveerraaggee  ppeerr--
cceennttaaggee  eerrrroorr  ooff  2200––4400%%,,  wwhheerreeaass  tthhee  bbeesstt  ffoorreeccaassttiinngg  ccaassee  hhaass  aann  eerrrroorr  ooff  aarroouunndd  22––33%%””..  
TThhee  ddeevveellooppeedd  ssiimmuullaattoorr  oobbttaaiinneedd  aa  MMAAPPEE  ooff  1100..1155%%..  

IIff  ccoonnssiiddeerriinngg  eeaacchh  ccllaassss  iinnddiivviidduuaallllyy,,  iitt  iiss  ppoossssiibbllee  ttoo  sseeee  llaarrggee  ddiissppeerrssiioonn  ooff  tthhee  ppllaattee  
wwaassttee  iinn  FFiigguurree  1100..  AAtt  tthhiiss  mmoommeenntt,,  sscchhoooollss  ddoo  nnoott  ppeerrffoorrmm  tthhee  mmoonniittoorriinngg  ooff  cchhiillddrreenn''ss  
ssaattiissffaaccttiioonn  wwiitthh  sscchhooooll  lluunncchh..  IIff  sscchhoooollss  ssuurrvveeyy  cchhiillddrreenn  aanndd  ccoolllleecctt  ddaattaa  oonn  uunnssaattiissffiieedd  

  



Nutrients 2022, 14, 587 15 of 19

percentage error of 20–40%, whereas the best forecasting case has an error of around 2–3%”.
The developed simulator obtained a MAPE of 10.15%.

If considering each class individually, it is possible to see large dispersion of the plate
waste in Figure 10. At this moment, schools do not perform the monitoring of children’s
satisfaction with school lunch. If schools survey children and collect data on unsatisfied
children and the probability of competitive food for each class, it is possible to obtain
precise forecasting results for each school. Additionally, the project group did not have a
possibility to collect a comprehensive statistic related to path time; therefore, the samples of
bounding boxes have left and right movement allowances, which increases the dispersion.

Speaking about the plate waste, Martins et al. [24] summarized the information about
the plate waste, mentioning the following statistical values: 2–49% for primary school
lunches in the United States of America, 23%—in Swedish school canteens and 20–29% of
prepared meal in Italian schools. Figure 10 depicts comparable simulated and observed
values; however, other regions must tune the developed model using local statistical data
on school meals.

The developed Monte Carlo model applies two parameters for the simulation: lunch
duration and the number of unsatisfied children with school meals. That does not require
some complex data monitoring for plate waste forecasting. In addition, considering the rela-
tionship depicted in Figure 9, the input list of the developed model must be extended with
the parameter “Competitive food probability”. It must be mentioned that the parameters—
competitive food and a number of unsatisfied children—can have a strong correlation that
must be studied in the future to simplify the developed model considering its practical
usability for schools. Additionally, it can be time consuming for schools to complete a
continuous survey of children’s preferences; therefore, it is important to consider autom-
atization using digital tools, which can be connected to a system for menu generation to
increase children’s satisfaction with school meals.

The real parameters of schools can be applied for plate waste forecasting. The mathe-
matical models constructed in Figures 9 and 10 can be used to train managers of canteens.
Our simulation results precisely show that schools must primarily schedule lunch duration
correctly because insufficient time provides the exponential increase in the plate waste
amount (see Figures 8–10). Additionally, schools must teach children about healthy food
importance and monitor food preferences to minimize the rejected food amount and com-
petitive food impact because the competitive and rejected food provides a linear increase
in food waste proportional to the number of unsatisfied children (see Figure 9). In addi-
tion, it is possible to calculate the optimal lunch duration for the ideal conditions when
all children are satisfied with school food and do not buy competitive food. Figure 11
depicts the plate waste amount depending on lunch duration, considering the linear model
and the recalculated eating rate of 27(2) g/min mentioned by Zandian et al. [25] for girls
because the eating rate of girls was lower than the eating rate of boys. Considering the
obtained results, the minimal meal duration must be 20 min, excluding walking time and
other external factors, which can cause food intake delay. This duration is longer than our
previously proposed lunch duration (15 min) based on smaller data amount [26], which is
more consistent with the durations found by Cohen et al. [32] and Hamdi et al. [33], 20 min
and 17/18 min, respectively.

It is possible to construct a model for effective decision making to minimize the plate
waste of schools based on the simulation results and the developed simulator itself. The
capability model for effective decision making on food management in schools is depicted
in Figure 12, where the developed simulator is one of the services, which can be applied to
correctly schedule lessons and lunchtime and to train school managers; however, a menu
optimization tool must be developed to personalize a menu for children to reduce the num-
ber of kids who are not satisfied with school meals and eat competitive food. In addition,
measurable properties of children’s satisfaction with school meals can be monitored by
some IoT solution or data can be collected through mobile application/surveys.



Nutrients 2022, 14, 587 16 of 19 
 Nutrients 2022, 14, 587 16 of 19

Nutrients 2022, 14, 587 16 of 19 
 

  
FFiiigguurer e11 1.. 1L.u Lncuhn dcuhr adttiuiorna iitnio tthne  iiind etahll ec oinddeiiattiilo cnos..n ditions. 

 
FFiigguurree 1122.. CCaappaabbiilliittyy mmooddeell ffoorr eeffffeeccttiivvee ddeecciissiioonn mmaakkiinngg oonn ffoooodd mmaannaaggeemmeenntt iinn sscchhoooollss.. 

6. Conclusions 
The simulator developed by using the Monte Carlo method showed an RMSE equal  

to ±33%% aanndd aa MMAAPPEE ofo f101.01.51%5%, w, whihchic hreprerpesresnetns ttsheth beebste sfot rfeocraesctainstgin cgascea mseemnteionntieodn ebdy 
bMFyiagMluefraoelre s1f o2er.t s Caela.t p[a2al1b.];i[ l2hi1toy]w; mhevoowedree, vlm efaor,nr mye fpafnaerycatimpvaeert ademresce oitsefi rtoshneo  mfMtahokneitnMeg Co oannrtle ofo Cmoadorld omelma anopadpgeleilemadp eipnnl tit ehidne  schools. 
ienxpthereimexepnet rwimereen tbawseedre obna s2e4d reosnpo2n4seres.s pTohnes pesra. cTtihcael pursacgteic oafl tuhsea gdeevoeflothpeedd seivmeulolpateodr 
sr6iem.q Cuiloraentsoc ralr uleasqriugoiernre ss aamlaprlgee, rasnadm tphlee ,taanrgdetth peotparugleattipoonp muluastito bnem thues tebdeutchaeteeeds uocfa ttheees socfhtohoel 
swchhoeroel wthhe efroerethcaesftoinregc taosotiln (gsitmooulla(stoimr) uwlaitlol rb)ew aipllpblieeda.p Aplnie Rd.MASnE RwMasS Ecawlcuaslactaeldc ufolart eadll 
fsocrhoaolllTss;hc hheoo wsoilemsv; euhrol, awthtoeevr ae dbr,seotvhlueetleao bepsreorodlur  tbfeoyre  ruerasocirhn fgsoc rhtheoaoecl h Mobsoctahnionteoe ldCo aab mrtaloianx emimdeaatlh mvoaadlxu iesm hoaofl 5wv.8ae4ldu%e ,a n RMSE equal 
owtfoh5 i±.c83h4% ca ,naw nbhedi c raehd McuacnAedbP euEsr ieondgfu  1tche0ed. 1du5as%tian ,go wnt hthheiecd htaa trargeeoptn rsecthhsoeontalt.r sAg ettht thsece hb soeaosmlt. ef Aotitrmetehc,ea tshstaeim npgese tucimadsoee-,  mentioned by 
tcMhoedaepl efsoeforu crdhso icledot d gaeeln.f oe[rr2a1ctih]o;i nlhd (oTgwaebneleevr 7ae)tr ii,os  nmba(asTneadby lo epn7a t)hraies mdbiaeststreidbruso toinofnt ht dheeedp iiMcstteroidbn uitnet iF oCingaudrreleop 5 i,cm wteodhdicienhl  applied in the 
Fsehixgopuwreeerd5im ,twwehoni tcp hewaskhesro,ew b ebudat stiwte cdoa npo enha ak2vs4e,   baruents eiptxocpanonnshenasvt. ieaTlah dneies ptxrpriboaunctetiinocntai;a llh udosiwsatergvibeu ro,t ifiot  ntihs;  heno odwte evvveeerylr,o ped simulator 
iirtmeisqpounroitrtaenvste  braye cliaamurpgseoe rerta ascnhat msbcehpcoaleoul,s  ceaanenad hc ahtvhsece hi ttosa oorlwgcnean ts ppheaocvpifeiuci tldsaitositworinnb usmtpioeuncsi.fi tI tcb idse im stthorirebe u eitmdiopunoc.raIttateniset m s of the school 
two

o mreenimhereti o
p
thn
o ret

tha fe
n
o 
tlri

tmoeci
mtaast

einto
t

inn
io go

n
 ft 

tthoh
e
oe lld

im
 (esv

i
ie
ta
mlo

ti
up
o
le
n
ad

o
t os

firm
th
) u

e
wla

d
it
e
lo
v
lr

e
 —

lo
bed

p
 a

e
at

d
pa pu

si
lp
m
id

u
eadtl.i

a
 n
to
Ag

r——n tRh
deaMr

teaSfo
u
Er
ped ,w 

athtiaens 
g
 d

—
cea-veloped simulator must be supported by the periodical surveys completed by schools; lculated for all 

asdcdhiotioolnsa;l lhyo, twheesve esur,r vtehyes  acabns toulnuet eth ee rsrimoru lfaotor re faocr han socthheoro tal rogbett raeignieodn  oar  smchaoxoilm. Faulr -value of 5.84%, 
twhehr,i cthe  cdaenve bloep erde dsiumcueldat ourscianngb tehaep pdliaetda a os na  dtehceis tioanr-gmeat ksicnhg ot ooll.  aAndt  tahtrea isnaimnget otoiml.  e, the pseudo-
code for child generation (Table 7) is based on the distribution depicted in Figure 5, which 
showed two peaks, but it can have an exponential distribution; however, it is not very 

 important because each school can have its own specific distribution. It is more important 
to mention the limitation of the developed simulator—data updating—therefore, the de-
veloped simulator must be supported by the periodical surveys completed by schools; 
additionally, these surveys can tune the simulator for another target region or school. Fur-
ther, the developed simulator can be applied as a decision-making tool and a training tool.  

 



Nutrients 2022, 14, 587 17 of 19

therefore, the developed simulator must be supported by the periodical surveys completed
by schools; additionally, these surveys can tune the simulator for another target region or
school. Further, the developed simulator can be applied as a decision-making tool and a
training tool.

The Monte Carlo method identified that schools must primarily correctly schedule
lunch duration because insufficient time leads to an exponential increase in plate waste
amount. In the ideal conditions, the simulator showed that the minimal meal duration
must be 20 min, excluding walking time. After that, schools must teach children about
healthy food importance and negative food waste impacts and monitor food preferences
to minimize the rejected food amount and decrease the competitive food probability. The
continuous monitoring of children’s preferences and their surveys are time-consuming
processes that could be automated by digital tools connected to a menu generation system.

The developed capability model for effective decision making on food management
in schools (Figure 12) considers the plate waste only. It does not consider the quality
of the meal intake; however, the system could be extended in the future if a computer
vision system is developed to measure plate waste components, as well as an ontology,
which matches a product with macro and micronutrients. As a result, it will be possible to
recalculate the plate waste into insufficient meal intake expressed in macro and micronutri-
ents. However, if a school meal is developed considering nutrition recommendations for a
healthy lifestyle, it is a challenge to join these data with data on a competitive food; it can
be achieved if children have a personalized health monitoring system, which can import
school data and information from their private monitoring systems.

Author Contributions: Conceptualization, S.K. and A.Z.; methodology, S.K.; software, S.K.; valida-
tion, S.K.; formal analysis, S.K.; investigation, A.Z., L.L., J.L., I.S., I.K. and J.D.; resources, L.L., J.L.
and I.S.; data curation, L.L. and I.S.; writing—original draft preparation, S.K., A.Z. and L.L.; writing—
review and editing, J.L. and I.K.; visualization, S.K.; supervision, S.K.; project administration, A.Z.;
funding acquisition, J.L. All authors have read and agreed to the published version of the manuscript.

Funding: This research is funded by the Latvian Council of Science project “E-mentor as a Transfor-
mation Tool for Ensuring Zero-Waste Food Consumption in Educational Institutions”, project No.
lzp-2020/2-0115.

Institutional Review Board Statement: The study was exempt by the Scientific Council of Rezekne
Academy of Technologies (protocol code 16.1/12 on 18 May 2021) due to not collecting information
about the students’ parents.

Informed Consent Statement: Not applicable.

Data Availability Statement: All datasets generated during the current study are available from the
corresponding author upon reasonable request.

Acknowledgments: We would like to thank Arnolds Dreilings, the head of the Education Department
of the Rezekne State City, Rita Deksne, the chief catering specialist, the principals of the participated
schools and the heads of the school canteens, as well as volunteer students and colleagues from
Rezekne Academy of Technologies for assistance in sorting plate waste at the schools’ canteens.

Conflicts of Interest: The authors declare no conflict of interest. The funders had no role in the design
of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript, or
in the decision to publish the results.

References
1. Food and Agriculture Organization of the United Nations. The State of Food Agriculture. Moving Forward on Food Loss and

Waste Reduction. 2019. Available online: https://www.fao.org/3/ca6030en/ca6030en.pdf (accessed on 3 December 2021).
2. Schanes, K.; Dobernig, K.; Goezet, B. Food waste matters—A systematic review of household food waste practices and their

policy implications. J. Clean. Prod. 2018, 182, 978–991. [CrossRef]
3. Cattaneo, A.; Sánchez, M.V.; Torero, M.; Vos, R. Reducing food loss and waste: Five challenges for policy and research. Food Policy

2021, 98, 101974. [CrossRef] [PubMed]
4. Thyberg, K.L.; Tonjes, D.J. A Management Framework for Municipal Solid Waste Systems and Its Application to Food Waste

Prevention. Systems 2015, 3, 133–151. [CrossRef]



Nutrients 2022, 14, 587 18 of 19

5. Thyberg, K.L.; Tonjes, D.J. Drivers of food waste and their implications for sustainable policy development. Resour. Conserv.
Recycl. 2016, 106, 110–123. [CrossRef]

6. Martin-Rios, C.; Demen-Meier, C.; Gössling, S.; Cornuz, C. Food waste management innovations in the foodservice industry.
Waste Manag. 2018, 79, 196–206. [CrossRef]

7. Betz, A.; Buchli, J.; Göbel, C.; Müller, C. Food waste in the Swiss food service industry—Magnitude and potential for reduction.
Waste Manag. 2015, 35, 218–226. [CrossRef]

8. Yui, S.; Biltekoff, C. How Food Becomes Waste: Students as “Carriers of Practice” in the UC Davis Dining Commons. J. Hunger
Environ. Nutr. 2020, 16, 684–705. [CrossRef]

9. Wilkie, A.C.; Graunke, R.E.; Cornejo, C. Food Waste Auditing at Three Florida Schools. Sustainability 2015, 7, 1370–1387.
[CrossRef]

10. Benvenuti, L.; De Santis, A.; Santesarti, F.; Tocca, L. An optimal plan for food consumption with minimal environmental impact:
The case of school lunch menus. J. Clean. Prod. 2016, 129, 704–713. [CrossRef]

11. Martin, C.K.; Newton, R.L., Jr.; Anton, S.D.; Allen, H.R.; Alfonso, A.; Han, H.; Stewart, T.; Sothern, M.; Williamson, D.A.
Measurement of children’s food intake with digital photography and the effects of second servings upon food intake. Eat. Behav.
2007, 8, 148–156. [CrossRef]

12. Grainger, M.; Stewart, G.; Piras, S.; Righi, S.; Setti, M.; Vittuari, M. D4.2-Model Development and Data Proto-Col. Technical
Report. Available online: http://edepot.wur.nl/399920 (accessed on 3 December 2021).

13. Craven, T.J.; Krejci, C.C. An agent-based model of regional food supply chain disintermediation. In Proceedings of the Agent-
Directed Simulation Symposium (ADS ’17). Society for Computer Simulation International, San Diego, CA, USA, 23–26 April
2017; Article 8. pp. 1–10.

14. Van Voorn, G.; Hengeveld, G.; Verhagen, J. An agent based model representation to assess resilience and efficiency of food supply
chains. PLoS ONE 2020, 15, e0242323. [CrossRef] [PubMed]

15. Scalco, A.; MacDiarmid, J.I.; Craig, T.; Whybrow, S.; Horgan, G.W. An Agent-Based Model to Simulate Meat Consumption
Behaviour of Consumers in Britain. J. Artif. Soc. Soc. Simul. 2019, 22, 8. [CrossRef]

16. Achmad, A.L.H.; Chaerani, D.; Perdana, T. Designing a food supply chain strategy during COVID-19 pandemic using an
integrated Agent-Based Modelling and Robust Optimization. Heliyon 2021, 7, e08448. [CrossRef] [PubMed]

17. Ravandi, B.; Jovanovic, N. Impact of plate size on food waste: Agent-based simulation of food consumption. Resour. Conserv.
Recycl. 2019, 149, 550–565. [CrossRef]

18. Dolnicar, S.; Juvan, E. Drivers of plate waste: A mini theory of action based on staff observations. Ann. Tour. Res. 2019, 78, 102731.
[CrossRef]

19. Juvan, E.; Grün, B.; Baruca, P.Z.; Dolnicar, S. Drivers of plate waste at buffets: A comprehensive conceptual model based on
observational data and staff insights. Ann. Tour. Res. Empir. Insights 2021, 2, 100010. [CrossRef]

20. Anderson, S.M.; Olds, D.A.; Wolfe, K.L. The Impact of a Portion Plate on Plate Waste in a University Dining Hall. J. Foodserv. Manag.
Educ. 2021, 15, 1–7. Available online: https://fsmec.org/wp-content/uploads/2021/11/15-2.pdf (accessed on 3 December 2021).

21. Malefors, C.; Strid, I.; Hansson, P.-A.; Eriksson, M. Potential for using guest attendance forecasting in Swedish public catering to
reduce overcatering. Sustain. Prod. Consum. 2021, 25, 162–172. [CrossRef]

22. Malefors, C.; Secondi, L.; Marchetti, S.; Eriksson, M. Food waste reduction and economic savings in times of crisis: The potential
of machine learning methods to plan guest attendance in Swedish public catering during the COVID-19 pandemic. Socio-Econ.
Plan. Sci. 2021, 101041. [CrossRef]

23. Fagerberg, P.; Charmandari, E.; Diou, C.; Heimeier, R.; Karavidopoulou, Y.; Kassari, P.; Koukoula, E.; Lekka, I.; Maglaveras, N.;
Maramis, C.; et al. Fast Eating Is Associated with Increased BMI among High-School Students. Nutrients 2021, 13, 880. [CrossRef]

24. Liz Martins, M.; Rodrigues, S.S.; Cunha, L.M.; Rocha, A. Factors influencing food waste during lunch of fourth-grade school
children. Waste Manag. 2020, 113, 439–446. [CrossRef] [PubMed]

25. Zandian, M.; Ioakimidis, I.; Bergström, J.; Brodin, U.; Bergh, C.; Leon, M.; Shield, J.; Södersten, P. Children eat their school lunch
too quickly: An exploratory study of the effect on food intake. BMC Public Health 2012, 12, 351. [CrossRef] [PubMed]

26. Kodors, S.; Zhukov, V.; Zarembo, I.; Litavniece, L.; Lonska, J.; Zvaigzne, A. Simulation of a school canteen to understand
meal duration impact on food waste. In Proceedings of the 13th International Scientific and Practical Conference Environment,
Technology, Resources, Rezekne, Latvia, 17–18 June 2021; Volume 2, pp. 84–87. [CrossRef]

27. Ferriday, D.; Bosworth, M.; Lai, S.; Godinot, N.; Martin, N.; Martin, A.A.; Rogers, P.J.; Brunstrom, J. Effects of eating rate on
satiety: A role for episodic memory? Physiol. Behav. 2015, 152 Pt B, 389–396. [CrossRef]

28. Scaglioni, S.; Arrizza, C.; Vecchi, F.; Tedeschi, S. Determinants of children’s eating behavior. Am. J. Clin. Nutr. 2011,
94, 2006S–2011S. [CrossRef] [PubMed]

29. De Cosmi, V.; Scaglioni, S.; Agostoni, C. Early Taste Experiences and Later Food Choices. Nutrients 2017, 9, 107. [CrossRef]
[PubMed]

30. Scaglioni, S.; De Cosmi, V.; Ciappolino, V.; Parazzini, F.; Brambilla, P.; Agostoni, C. Factors Influencing Children’s Eating
Behaviours. Nutrients 2018, 10, 706. [CrossRef] [PubMed]

31. Ragelienė, T. Do children favor snacks and dislike vegetables? Exploring children’s food preferences using drawing as a projective
technique. A cross-cultural study. Appetite 2021, 165, 105276. [CrossRef] [PubMed]



Nutrients 2022, 14, 587 19 of 19

32. Cohen, J.F.; Jahn, J.L.; Richardson, S.; Cluggish, S.A.; Parker, E.; Rimm, E.B. Amount of Time to Eat Lunch Is Associated with
Children’s Selection and Consumption of School Meal Entrée, Fruits, Vegetables, and Milk. J. Acad. Nutr. Diet. 2016, 116, 123–128.
[CrossRef] [PubMed]

33. Hamdi, N.; Ellison, B.; McCaffrey, J.; Metcalfe, J.J.; Hoffman, A.; Haywood, P.; Prescott, M.P. Implementation of a Multi-
Component School Lunch Environmental Change Intervention to Improve Child Fruit and Vegetable Intake: A Mixed-Methods
Study. Int. J. Environ. Res. Public Health 2020, 17, 3971. [CrossRef] [PubMed]



Reproduced with permission of copyright owner. Further reproduction
prohibited without permission.