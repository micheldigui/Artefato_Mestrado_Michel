---
source_file: "2025-Forecasting and Modelling of Food Demand Supply Chain using Machine Learning.txt"
original_rel_path: "Trabalhos\Artigos\Aproveitar parcialmente\txt\2025-Forecasting and Modelling of Food Demand Supply Chain using Machine Learning.txt"
category: "Artigos_Aproveitar_parcialmente"
extension: ".txt"
sha256: "86a95bdbfa9cf13775e86017cc65082159f4b49b84f8d7ec3c22a4f7b7fcd0de"
extracted_at: "2026-09-20T00:50:21.704514"
---

﻿Volume 13 Issue 2                                                        @ March - April 2025 IJIRMPS | ISSN: 2349-7300 
 

Forecasting and Modelling of Food Demand 
Supply Chain using Machine Learning 

 
Dr. M. A. Chaudhari1, Aditi Phapale2, Pranav Gagare3, Tejas Kardile4, 

Amruta Phatangare5 
 

Department of Information Technology Engineering 
Amrutvahini college of Engineering, Sangamner 

Abstract 
This paper presents a comprehensive software solution for addressing the challenges associated with 
predicting and managing the demand and supply of food in a dynamic environment. The system 
leverages machine learning algorithms, including XGBoost, LightGBM, and SARIMA, to provide 
accu- rate demand forecasting and optimize inventory and distribution by modelling supply chains. 
The user-friendly interface allows administrators to interpret machine learning model outputs and 
make informed decisions, while the historical data module provides essential access to past trends and 
patterns for training and validating machine learning models. The paper discusses the system’s key 
features, such as demand forecasting, inventory management, data analytics dashboard, and 
fulfillment center allocation, and outlines the nonfunctional requirements, including performance, 
safety, security, and software quality attributes. The proposed solution aims to provide valuable 
insights for stakeholders in the food industry, ultimately contributing to more efficient and informed 
decision- making in the management of food demand and supply chains. 

 
Keywords: Time Series Forecasting, Machine Learning, Demand Forecasting, Supply Chain 
Management, Food Industry, Inventory Management 

I. INTRODUCTION 

Food demand prediction has become critical issue for both businesses and continuos development. Business 
aspects are mainly related to improving the manufacturing, supply chain processes, inventory cost reduction, 
and customer satisfac- tion. Continuous development issues are mainly related to food loss and waste, and 
they have been drawing much attention in recent years. Due to the consumer’s varying and increasing needs 
and competitiveness among the companies, most of the companies in today’s market are shifting their 
focus to demand forecasting for the demand-supply chain management. Demand forecasting is beyond the 
scope of any decision planning, as they directly impact a company’s profitability. Inaccurate prediction of 
demand can either cause too large inventory, which can results in a high risk of wastage and high costs to 
pay or too little inventory, leading to out-of stocks which will make company to look after services from its 
competitors when they failed to meet customers needs. For these reasons, the use of demand 
forecasting methods is one of the most fundamental components of the strategic planning. Traditional data 
science forecasting models, such as multiple regression, gradient boosting are applied in food demand 
prediction. 
The prevention of food waste is one of the most important worldwide issues, especially in the continuous 
development. The amount of food wasted is not geographically specific lo- cation but it correlates with the 
country’s development. Wasted food is defined as food that is unconsumed or discarded by the retailer 
because of its colour or appearance. Some products delivered to the store are never sold because of the 

IJIRMPS2502232389          Website: www.ijirmps.org Email: editor@ijirmps.org 1 
 



Volume 13 Issue 2                                                        @ March - April 2025 IJIRMPS | ISSN: 2349-7300 
 

expiration date on the label or damage. Demand forecasting importance becomes noticeable as its outcome is 
used by many subdivi- sions in the company that is Purchasing department may come up with their plan of 
short investment and the operation de- partment can manage their plan of purchasing the required raw 
materials, machinery, and labor in advance. Therefore, the forecasts are beneficial and their high accuracy 
has the potential to improve demand-supply chain management, and reduce wastage. 

A. MOTIVATION 

For meal delivery companies, a big challenge is managing how much food to make without wasting 
ingredients that can spoil quickly. This makes it super important to predict how much food people will order 
accurately [1]. Predicting demand means turning a problem about time into one about figuring things out. 
Right now, there are lots of different ways to predict demand, using both simple and more complicated 
methods. In the past, people mostly used simple methods like Linear Regression or Random Forests for 
short-term predictions. But now, there are newer methods like Extreme Gradient Boost- ing Regressor[ Light 
Gradient Boosting Machine Regressor (LightGBM) [3] and Gradient Boosting Regressor (XGBoost) that 
work better, especially when we have lots of different kinds of information to consider. 

 
B. PROBLEM DEFINITION 

The client is a meal delivery service operating in multiple cities, each with several delivery centers. To 
minimize food waste, they need a reliable model to predict future order vol- umes so they can stock the right 
amount of ingredients. Since most ingredients need weekly replenishment and can spoil quickly, planning 
procurement is crucial. Accurate demand forecasts also help in staffing the centers efficiently. To forecast 
demand for the next 10 weeks, they’ll use: 

1) Past sales data for a specific meal at each center. 
2) Meal details like category, subcategory, current price, and discounts. 
3) Information about delivery centers, including region and city codes. 

 
C. NOVELTY OF THE WORK 

The originality of this study lies in the exploration of lag features and Exponentially Weighted Moving 
Average (EWMA) for enhancing prediction accuracy. Extensive ex- perimentation was conducted to identify 
the most effective parameters for each model. This paper aims to evaluate the ability of three distinct models 
: Gradient Boost, LightGBM, and XGBoost through comparative analysis. 

 
D. CONTRIBUTIONS 

This article aims to utilize machine learning regressors to forecast the number of meals for the subsequent 10 
weeks. The significant contributions of this study are as follows: 
1) Application of boosting algorithms such as XGBoost, LightGBM, and Gradient Boost, chosen for their 

ver- satility in handling both categorical and numerical fea- tures. 
2) Integration of lag and Exponentially Weighted Moving Average (EWMA) features, selected for their 

robustness in analyzing historical data and facilitating accurate forecasting. 
3) Evaluation of prediction performance metrics, including Root Mean Square Error (RMSE) and Mean 

Absolute Error (MAE), which yielded values of 172.37 and 158.48 for one model, and 91.41 and 
86.41 for another model, respectively. 

IJIRMPS2502232389          Website: www.ijirmps.org Email: editor@ijirmps.org 2 
 



Volume 13 Issue 2                                                        @ March - April 2025 IJIRMPS | ISSN: 2349-7300 
 

II. LITERATURE REVIEW 
Forecasting demand of any commodity is one of the most important aspects to prevent wastage in any 
form.Recent stud- ies demonstrated the practical application of LSTM and SVM models to analyze various 
factors. By enhancing predictive capabilities for sales and minimizing food wastage machine learning 
approaches to address supply chain issues effectively [1].The significance of accurate demand forecasting in 
the e- commerce industry and the increasing application of machine learning approaches, such as NAR and 
LSTM models.The solution which aims to solve the challenge of using statistical machine learning models 
like VAR to predict the production of crops and livestock [2].A novel algorithmic approach to address the 
challenges which is related with stochasticity and uncertainty in food delivery operations in online food 
deliv- ery, operations management [3].A hybrid approach combines ARIMA and NARNET models to 
forecast coconut prices, leveraging their strengths to capture complex patterns and im- prove forecasting 
accuracy. Performance of the hybrid model against individual models are evaluated [4]. The growing trend of 
utilizing machine learning methods that is CNN and LSTM, for predicting crop yields highlights the possible 
of these tech- niques in agricultural yield forecasting [5].The study compares ARIMA, ANNs, and SVR 
models for electricity demand and price forecasting, proposing a hybrid model to the enhance accuracy by 
improving prediction in energy sector.Predicting the prices of four key Nigerian food items using the 
ARIMA model, emphasizes the importance of accurate price forecast- ing to make less overproduction and 
underproduction losses [6].The ARIMA model combined with R-programming for food price forecasting, 
addresses the challenges of food price management in Nigeria [7].The use of hybrid CNN-GRU based 
probabilistic model for developing a highly accurate demand forecasting model for the retail industry 
[8].Machine learning based model is used to predict food sales accurately by leveraging the Random Forest 
Regression algorithm which predicts the sales for perishable goods [9].Temperature data using machine 
learning techniques emphasizes potential supe- riority of supervised machine learning models over 
traditional statistical approaches offers insights powerful alternative to traditional statistical methods 
[10].The contribution to the field of food industry by providing a robust and reliable tool for demand 
forecasting, by benefiting companies’ intelligent man- agement systems for rational control of inventories 
and food production by reducing food waste [11].A secure monitoring system using IoT, RFID, and WSN to 
enhance the security of perishable food supply chain processes during transportation for food safety [12]. 
The challenges such as overfitting and vanishing gradients, proposes solution to enhance performance 
potential of RNNs in capturing complex patterns [13].To make less losses and improve the efficiency of 
online order fulfillment by the use of penalty functions to assess model risks and potential benefits [14].The 
blockchain contributes to the field of supply chain management by providing a framework for forecasting 
demand, efficient resource allocation [15].The importance of food material management to reduce losses 
related with overproduction and underproduction [16].ARIMA model to forecast consumption for various 
food materials, demonstrating its effectiveness in enhancing decision-making and reducing financial losses. 
ARIMA, Holt-Winters, and neural networks for forecasting the prices of 11 are evaluatded efficiently 
[17].Accurate demand forecasting for fresh foods, particularly bread, in Indonesia, proving the influence the 
store of classification and seasonal factors on sales forecasting [18]. Using the ARIMA method to predict 
daily sales, to help franchise businesses in reducing waste and optimizing inventory management for 
perishable goods by [19].Utilized novel method for predicting relief food demand after natural disasters 
using SVM and factor selection techniques [20]. 

III. DATA ANALYSIS AND PREPROCESSING 

In this section, we present our proposed methodologies, beginning with an overview of the existing and 
derived fea- tures, followed by an outline of the preprocessing techniques employed. 

IJIRMPS2502232389          Website: www.ijirmps.org Email: editor@ijirmps.org 3 
 



Volume 13 Issue 2                                                        @ March - April 2025 IJIRMPS | ISSN: 2349-7300 
 

A. Dataset Description 

The ”Food Demand Forecasting” dataset, provided by Gen- pact, an American professional services firm, 
contains weekly order data spanning 145 weeks for 50 different meals. This dataset is organized into three 
separate files, comprising a total of approximately 450,000 entries and 15 distinct features. These features 
are described below: 

1) Weekly Demand Data: This file contains historical records of sales numbers for specific meals at various 
centers. The details included are: 

a) id: A unique identifier for each order. 
b) week: The week number, ranging from 1 to 145. 
c) meal id: A unique identifier for each meal. 

d) center id: A unique identifier for each fulfillment center. 
e) checkout price: The final price of the meal after applying discounts, taxes, and delivery charges. 
f) base price: The original price of the meal as listed on the menu. 
g) emailer for promotion: Indicates whether an email was sent to promote the meal (0 for no, 1 for yes). 
h) homepage featured: Indicates whether the meal was featured on the website’s homepage (0 for no, 1 for 

yes). 
i) num orders: The number of orders received. 

2) fulfilment center info.csv: This file provides informa- tion about each fulfillment center, including: 

a) center id: The identifier for each fulfillment center. 
b) op area: The service area of each center (in square kilometers). 
c) city code: The postal code associated with each city. 
d) center type: The type of fulfillment center (type A, type B, type C). 

e) region code: A unique code for each region. 

3) meal info.csv: This file contains details about each meal, including: 

a) meal id: The identifier for each meal. 
b) category: The type of meal (e.g., beverages, snacks, soups). 
c) cuisine: The cuisine type (e.g., Indian, Italian). 

B. Dataset Analysis 

 

Fig. 1. Order per region 

 
The Fig 1 represents the total number of orders for each region code.Each bar shows corresponding to a 
specific region code and its height representing the number of orders in that particular region. The region 
code 56 shows that it has the highest number of orders, reaching approximately 60,000,000 orders.Where the 
region 34 it has the second-highest number of orders, which is reaching approximately 20,000,000 orders 

IJIRMPS2502232389          Website: www.ijirmps.org Email: editor@ijirmps.org 4 
 



Volume 13 Issue 2                                                        @ March - April 2025 IJIRMPS | ISSN: 2349-7300 
 

and region code with 77 has notable number of orders, which is slightly above 10,000,000 orders while 
remaining relatively fewer orders much less than major region. 

 
Fig. 2. number of center per center type 

 
The Fig 2 represents the number of centers for each center type. Each bar indicating to a specific center type 
and its height represents the number of centers of that type. The Center Type TYPE A has the highest 
number of centers, which is reaching above 40 centers, TYPE B Center Type has less centers compared to 
TYPE A center reaching above 10 centers, while center TYPE C has the moderate number of centers 
reaching approximately 20 centers. 

 
Fig. 3. order per center type 

 
 
The Fig 3 represents the total number of orders for each center type having center type TYPE A , TYPE B, 
TYPE C where TYPE A centers handles the most of the orders, which is followed by TYPE B and then 
TYPE C centers. 

 
 

 
 
 
 
 

IJIRMPS2502232389          Website: www.ijirmps.org Email: editor@ijirmps.org 5 
 



Volume 13 Issue 2                                                        @ March - April 2025 IJIRMPS | ISSN: 2349-7300 
 

 

 
 

Fig. 4. order per center pichart 

 
The Fig 4 representing the distribution of total orders amongs the three different center types that is center 
type TYPE A , TYPE B, TYPE C where the majority of orders are handled by TYPE A centers that 
is more than half of the total orders (57.7%) , TYPE B centers contributing moderately which is handling 
over a quarter of the total orders (25.1%) and TYPE C centers handling the smallest portion of the total 
orders 17.2%. 
 

 
Fig. 5. order per center id 

 
The Fig 5 representing the differences in number of orders across different centers highlighting the specific 
centers that handles large order of volumes, where the center ID 13 which has the highest number of orders 
which is exceeding 4,000,000 other high order centers are in range between 2,000,000 orders each to less 
than 4,000,000. There are several centers with orders which are ranging between 1,000,000 to 2,000,000, 
other Center IDs shows fewer volume of orders less than 1,000,000 order 

 

IJIRMPS2502232389          Website: www.ijirmps.org Email: editor@ijirmps.org 6 
 



Volume 13 Issue 2                                                        @ March - April 2025 IJIRMPS | ISSN: 2349-7300 
 

 

 

 
Fig. 6. order per category 

 
The Fig 6 highlights the huge popularity of beverages compared to all other categories.It indicates that Rice 
Bowl, Sandwich, and Salad are also relatively popular but it is significantly less than the Beverages.The 
beverage has the highest number of orders which is close to 40,000,000. Rice bowl ranges with orders 
between 5,000,000 to 10,000,000 where the Sandwich and Salad follows them behind. The categories like 
Pizza, Other Snacks, and Pasta have average order of volumes which is ranging between 1,000,000 to 
5,000,000 orders and the others has the lowest order of volume below 1,000,000 orders. 
The Fig 7 highlights the popularity of Italian cuisine comparing with the other cuisines indicating that 
Thai cui- sine is also popular but significantly less than Italian close to 4,000,000, Indian cuisine has 
average volume of orders 3,000,000 while the Continental has the lowest 2,000,000 orders 
 

 
 

Fig. 7. order per cuisine 
 

 

 
 

 

 

 

 

 

IJIRMPS2502232389          Website: www.ijirmps.org Email: editor@ijirmps.org 7 
 



Volume 13 Issue 2                                                        @ March - April 2025 IJIRMPS | ISSN: 2349-7300 
 

 

 

 
Fig. 8. order per cuisine pichart 

 
The Fig 8 shows the distribution of orders amongs the different types of cuisine, with each portion of the pie 
chart which is representing a different cuisine category. Italian cuisine occupies the largest volume of orders 
36.9% , Thai has 27.3% of the total orders, Indian has the 21.6% of the total orders and Continental 
representing 14.1% of the total orders. 
The Fig 9 shows the distribution of orders across different meal IDs, highlighting that which meals are 
ordered the most and the least. The meal ID 2290 is having the highest number of orders , Meal IDs such as 
1778, 2104, and 2707 moderate numbers of orders showing less than 2290 meal ID and others are having 
lower numbers. 
 

 
Fig. 10. Distribution of Orders across Cuisine and Category 

 
The Fig 10 shows the distribution of orders across different cuisines and categories, highlighting the most 
popular cate- gories within each cuisine. By displaying the total number of orders for each cuisine further 
it is broken down by category. Continental Cuisine total orders were 20 million where sandwiches and 

IJIRMPS2502232389          Website: www.ijirmps.org Email: editor@ijirmps.org 8 
 



Volume 13 Issue 2                                                        @ March - April 2025 IJIRMPS | ISSN: 2349-7300 
 

beverages are the major category .In Inidan Cuisine total orders were 30 million where the rice bowl is the 
most popular.In Italian Cuisine total orders were 40 million where salad and beverages are the major 
category and Thai Cuisine orders are above 30 million, starters is having notable presence in Thai 

The Fig 11 is the matrix scatter plot which visualizes the relationships between multiple numerical 
variables.The num orders variable is highly skewed showing that the most of the centers having low number 
of orders while with few centers having significantly higher numbers. There are notice- able clusters and 
patterns in the scatter plots, particularly in the base price vs. center id plot, where distinct vertical bands 
indicates that the certain centers are having consistent base prices and There are no clear linear relationships 
between the variables in the scatter plots. 

 
Fig. 11. Matrix Scatter Plot of Numerical Variables 

 
C. Data preprocessing techniques 

1) Numerical Features : The dataset contains numerical features with varying scales, and many of these 
features exhibit a pronounced right-skew. To reduce skewness, quantile or power transformations can be 
applied, which adjust the distribution to be more normal. However, since the data already follows a 
normal distribution, standardizing the data is more appropriate for scaling purposes than normalization. 

2) Categorical Features : There are two methods for con- verting categorical features into numerical ones: 
Label Encoding and One-Hot Encoding. Label Encoding as- signs a unique integer to each category based 
on al- phabetical order. On the other hand, One-Hot Encoding creates additional features for each unique 
value in the categorical feature, which can be memory and energy- intensive, especially with a large 
number of features. Given the already substantial number of features in the dataset, Label Encoding is 
preferred for its efficiency. 

IV. METHODOLOGY 

A. Machine Learning Models 

In our study, we applied three machine learning models Gradient Boost, LightGBM, and XGBoost—for 
predicting food demand : 
In this section, the aim is to describe the forecasting methods. The models used in the proposed system are 
Gradient Boost, Extreme Gradient Boosting Regressor(XGBoost) and Light Gradient Boosting Machine 

IJIRMPS2502232389          Website: www.ijirmps.org Email: editor@ijirmps.org 9 
 



Volume 13 Issue 2                                                        @ March - April 2025 IJIRMPS | ISSN: 2349-7300 
 

Regressor (LightGBM). These models are used for demand forecasting and inventory management. The 
XGBoost and LightGBM models are the gradient boosting frameworks that uses decision trees as base 
learners. They are known for their high accuracy and efficiently handling large datasets. These models are 
trained on historical data on food demand and inventory levels, which is accessed through the historical data 
module. The historical data is essential for training and validation of machine learning models, which allows 
them to learn from past data, trends and patterns. 
The outcome of these models are used to predict the quan- tity of food orders expected in the upcoming 
weeks and to forecast stock needs for selected food items for specific time periods before it get expired, such 
as weekly forecasts. These predictions are used to optimize inventory and distribution by modeling supply 
chains and to allocate customer orders to fulfillment centers. Overall, the models used in the project are 
designed to provide accurate insights to optimize stock levels and order fulfillment, which finally contributes 
to more efficient and informed decision-making process in the man- agement of food demand and supply 
chains. The Following key components are : 

1) Demand Forecasting: The system uses machine learning techniques that is Gradient Booost, XGBoost and 
Light- GBM to predict the quantity of food orders that is expected in the upcoming weeks based on 
historical data analysis and machine learning models. This feature is of high priority and critical for the 
effective management of stock levels. 

2) Inventory Management: Efficient management of raw material inventory is prioritized to meet forecasted 
up and down demands, reduce waste, and minimize storage costs. The system uses machine learning 
techniques to predict stock needs for selected food items for specific time periods, such as weekly 
forecasts. 

The proposed system is web application which provides restaurants with an builtin platform to effectively 
manage the inventory. It consists of three core module, each method optimizes different part of the overall 
process of inventory control.The initial page represents the login and signup page which allows users to 
access the web application.It provides secure and user-friendly interface for both new and existing users. The 
food demand forecasting module is designed to help restaurants in predicting future food orders for at least 
upcoming 10 weeks. This part of the application requires users to enter inputs to 11 distinct features 
which includes the category of food, number of weeks ,checkout price,base price,city code,region 
code,operational area etc. By using Machine learning algorithms like XGBoost, LightGBM, and Gradient 
Boosting, the forecasting tool analyzes the provided data to produce predictions. These forecasts helps 
restaurants to plan their inventory more effectively, ensuring that they can meet customer demand, 
minimize waste, and maintain optimal stock levels. By expecting future orders restaurants can make 
informed decisions that will enhance their operations and customer satisfaction. The Inventory Management 
module is used for administrator to oversee and control stock levels. This module of system provide 
comprehensive tools to monitor food orders and track inventory usage in real-time. Center owner can view 
detailed information about each order, includ- ing its status and the amount of inventory utilized. This real- 
time tracking helps to prevent stock outs and over stocking, by ensuring that inventory is managed cost-
effectively and that waste is minimized. By maintaining inventory, restaurants can ensure that they always 
have the necessary ingredients on hand to meet customer demand while optimizing their storage and 
procurement processes. 

IJIRMPS2502232389          Website: www.ijirmps.org Email: editor@ijirmps.org 10 
 



Volume 13 Issue 2                                                        @ March - April 2025 IJIRMPS | ISSN: 2349-7300 
 

 

Fig. 12. Distribution of Price 

 
The Fig 12 shows analysis of distribution of checkout price, base price, and number of orders received by 
count of number of customers. 

 
Fig. 13. Trend of orders over the week 

 
The Fig 13 represents analysis of the trend of total number of orders over the weeks. Here the number of 
orders are increasing and decreasing over weeks. 
The Fig 14 illustrates the architecture of the system. It is carefully crafted to utilize machine learning for 
predicting and modeling food demand and supply chain behavior. It starts by merging various datasets 
containing meal details, fulfillment center information, and historical demand data, laying the groundwork 
for analysis. Following this, data is prepared for analysis through thorough cleaning, transformation, and 
exploratory analysis to ensure accuracy. Then, trends and anomalies are identified to understand how 
demand fluctuates. 

IJIRMPS2502232389          Website: www.ijirmps.org Email: editor@ijirmps.org 11 
 



Volume 13 Issue 2                                                        @ March - April 2025 IJIRMPS | ISSN: 2349-7300 
 

 

 
Fig. 14. Architecture Diagram 

 
Next, machine learning models are trained and tested, refining their performance through techniques like 
feature selection, engineering, and evaluation. Finally, these models are de- ployed to forecast future demand, 
providing actionable insights for effective decision-making in the food supply chain. 

A. Models 

The proposed system uses 3 machine learning models that is Gradient Boost, Extreme Gradient Boosting 
Regres- sor(XGBoost) and Light Gradient Boosting Machine Regres- sor (LightGBM). These models are 
used for demand forecast- ing and inventory management. 

• XGBoost and LightGBM are gradient boosting frame- works that uses decision trees as base learners. 
They are known for their high accuracy and efficiency in handling large datasets.In proposed system 
these models are used for demand forecasting and inventory management. 

• Xgboost is well known for its robustness and high performance, is used to capture complex patterns and 
trends in historical sales data. It is widely used because it efficiently cuts down on running time by 
parallel and distributed computing and handles the NaN values in the dataset. 

 
Fig. 15. Xgboost Prediction 

 
The Fig 15 Represents the actual number of orders with the predictions of XGBoost model. Here the Blue 
Line indicates the actual number of orders and Orange Line indicates XGBoost model predicted number of 
orders. XGBoost prediction is following the trend of the ac- tual number of orders with some variation 
in degrees of accuracy.The model captures the changing patterns and fluctuations of the actual order data 
and tends to underestimate at particular peaks such as instances 1, 3, 9, 18 and overestimate in other areas. 
• The Light GBM algorithm performs well in proposed system , is an optimization of the original 

Gradient Boosting Algorithm. It works on the same principles as the boosting algorithm but, unlike its 
parent algorithm, it grows the decision trees using a leaf-wise policy. It is designed for fast and efficient 

IJIRMPS2502232389          Website: www.ijirmps.org Email: editor@ijirmps.org 12 
 



Volume 13 Issue 2                                                        @ March - April 2025 IJIRMPS | ISSN: 2349-7300 
 

training. It is well-suited for handling large datasets and is widely used in industry. 

Fig. 16. Lightgbm Prediction 

 
The Fig 16 shows the comparison of the actual number of orders with the LightGBM predictions 
model.Here the Blue Line indicates the actual number of orders and Orange Line indicates Lightgbm model 
predicted number of orders where Lightgbm closely follows the trend of actual orders with good alignment. 
• Gradient Boosting Machine are based on the concept of combining a group of weak learner or base 

learner regression trees with gradient boosting regression to create robust forecasting models.By using 
this approach, the error rate of weak learned models is decreased. 

The Fig 17 shows comparison between actual data values with predicted values produced by Gradient 
Boosting model.The blue line (actual values) shows increase in values from point 1 to point 5, reaching at 
point 5. It is then gradually decreasing to near 0 at point 8, increases again to another at point 12, and then 
shows another top at point 18. The orange line (predicted values) follows the similar trend but tends to 
smooth out some of the extreme fluctuations. 

The Fig 18 shows the comparison of actual data values with predicted values from three different machine 
learning models.It compares the performance of three predictive models that is XGBoost, LightGBM, and 
Gradient Boosting against the actual number of orders. The actual data is represented by the blue line 
showing fluctuations with sharp apex and troughs. LightGBM represnted by the gray line results to 
provide the closest predictions to the actual data, often matching the apex and troughs more accurately 
while comparing with other. XGBoost is represented by the orange line and Gradient Boosting by yellow line 
which also follows the general trend of the actual data but with tending to smooth out the fluctuations more 
than LightGBM. Here it is been observed that the overall LightGBM prediction model results to perform the 
best in terms of closely matching the actual data values. 

 
Fig. 17. Gradient Boosting Prediction 

 

IJIRMPS2502232389          Website: www.ijirmps.org Email: editor@ijirmps.org 13 
 



Volume 13 Issue 2                                                        @ March - April 2025 IJIRMPS | ISSN: 2349-7300 
 

 

 

Fig. 18. Models prediction 
 

B. Web Application 

Web application provides a user-friendly platform for restaurants to track inventory and forecast food 
demand ef- fectively. It is designed to streamline operations and improve decision-making. This application 
consists of five separate sections, each providing its own functionality: 

1) Web interface: This section serves as the gateway to the entire system, including buttons or options for 
logging in, registration, services and “About Us” page. The user- friendly navigation bar allows users to 
access all these sections easily. This interface provides a comprehensive overview of the system structure 
in a general way. 

2) Login/Register: The login and registration page allows users to enter a username and password or email 
address to access the system. New users can register through the registration page. This section is 
important because it provides secure access to the inventory management and forecasting modules. After 
successfully logging in or registering, the user will be redirected to the following sections of the 
application. 

3) Forecast Dashboard: This section allows users to enter various parameters such as variety, cuisine, week, 
case price, and base price to forecast food demand. After entering the required information, users can 
click the “Prediction” button to view the prediction results. The dashboard displays food demand 
forecasts for specific weeks, using multiple algorithms to ensure accuracy. 

4) Inventory Management Dashboard: Accessible only to administrators, this section provides complete 
details about customer orders, including total customers, total orders, orders delivered orders, future 
orders, canceled orders and orders in progress. Admins can also view detailed information about each 
customer, including name, order history, and most recent order details. This dashboard is essential for 
updating inventory records and managing customer relationships effectively. 

5) Create Customer/Product: This module allows adminis- trators to add new dishes and customers to the 
system. To add a new dish, admins can enter the dish type, dish name, and price. To add a new customer, 
the required fields are name, phone number, email, and address. This feature ensures the system is always 
updated with the latest menu items and customer information. 
 

TABLE I COMPARISON STUDY OF MODELS 

 
Metric XGBoost LightGBM 

OriginalPredicte OriginalPredicte

IJIRMPS2502232389          Website: www.ijirmps.org Email: editor@ijirmps.org 14 
 



Volume 13 Issue 2                                                        @ March - April 2025 IJIRMPS | ISSN: 2349-7300 
 

d d 

RMSE 205.31 172.37 194.68 158.48 

MAE 106.17 91.41 104.49 86.41 
 
As shown in Table I it effectively compares the performance of XGBoost and LightGBM models using 
RMSE and MAE metrics where the LightGBM outperforms XGBoost in both RMSE and MAE metrics, it 
has a better predictive perfor- mance. 

 
CONCLUSION AND FUTURE SCOPE 
The proposed system highlights the importance of food demand forecasting in the today’s food industry. 
This system focuses on effective demand supply chain management, in- ventory cost reduction and customer 
satisfaction. Inaccurate demand prediction can lead to either excess inventory which can result in waste or 
insufficient inventory result in outoff stock. This system uses machine learning techniques such as Gradient 
Boost, XGBoost and LightGBM to provide valuable insights for stakeholders in the food industry which 
aims to optimize inventory management and predict food demand modeling supply chains. 

The dataset used in system don’t have large enough seasonality feature such as account for the date, month 
or any holidays.Without these factors, it was difficult to capture any trend or seasonality. Also, there was no 
mention of any event (like special discount or occasion) which may be able to explain sudden spikes of the 
target variable.In future by having external factors and variable will be able to predict the volume of orders 
including events and applying advanced technique. 
 
REFERENCES 
[1] S. K. Panda and S. N. Mohanty, ”Time Series Forecasting and Mod- eling of Food Demand Supply 

Chain Based on Regressors Analysis,” in IEEE Access, vol. 11, pp. 42679-42700, 2023, doi: 
10.1109/AC-CESS.2023.3266275 

[2] Peijian Wu, Ge Zhang, Yuqing Li,Xuqin Chen ”Research on E- Commerce Inventory Demand 
Forecasting Based on NAR Neural Net- work”,Open Access Library Journal, Pp 42–43, Vol.10 No.5, 
May24, 2023,doi: 10.4236/oalib.1110196 

[3] J. Zheng, L. Wang, L. Wang, S. Wang, J. -F. Chen and X. Wang, ”Solving Stochastic Online Food 
Delivery Problem via Iterated Greedy Algorithm With Decomposition-Based Strategy,” in IEEE 
Transactions on Systems, Man, and Cybernetics: Systems, vol. 53, no. 2, pp. 957-969, Feb. 2023, doi: 
10.1109/TSMC.2022.3189771 

[4] Abdullah et al., ”Intelligent Hybrid ARIMA-NARNET Time Series Model to Forecast Coconut 
Price,” in IEEE Access, vol. 11, pp. 48568- 48577, 2023, doi: 10.1109/ACCESS.2023.3275534. 

[5] Y. Zhang, L. Wang, X. Chen, Y. Liu, S. Wang, and L. Wang ”Prediction of Winter Wheat Yield at 
County Level in China Using Ensemble Learning”,Prog. Phys. Geogr.,Earth Environ., pp. 676–
696,vol.46,no.5,Oct.2022, doi.org/10.3390/rs12111744 

[6] I. Shah, H. Iftikhar, and S. Ali, “Modeling and forecasting electricity de- mand and prices: A 
comparison of alternative approaches,” J. Math.,vol. 2022, Jul. 2022, Art. no. 3581037. 

[7] J. N. Ndunagu, E. H. Aderemi, R. G. Jimoh and J. B. Awotunde, ”Time Series: Predicting 
Nigerian Food Prices using ARIMA Model and R-Programming,” 2022 5th Information Technology 
for Educa- tion and Development (ITED), Abuja, Nigeria, 2022, pp. 1-6, doi: 
10.1109/ITED56637.2022.10051516. 

[8] K. Honjo, X. Zhou and S. Shimizu, ”CNN-GRU Based Deep Learning Model for Demand Forecast in 
Retail Industry,” 2022 International Joint Conference on Neural Networks (IJCNN), Padua, Italy, 

IJIRMPS2502232389          Website: www.ijirmps.org Email: editor@ijirmps.org 15 
 



Volume 13 Issue 2                                                        @ March - April 2025 IJIRMPS | ISSN: 2349-7300 
 

2022, pp. 1-8, doi: 10.1109/IJCNN55064.2022.9892599. 
[9] H. Naik, K. Yashwanth, S. P and N. Jayapandian, ”Machine Learn- ing based Food Sales Prediction 

using Random Forest Regression,” 2022 6th International Conference on Electronics, Communication 
and Aerospace Technology, Coimbatore, India, 2022, pp. 998-1004, doi: 
10.1109/ICECA55336.2022.10009277 

[10] J. Pant, R. K. Sharma, A. Juyal, D. Singh, H. Pant and P. Pant, ”A Machine-Learning Approach to 
Time Series Forecasting of Tempera- ture,” 2022 6th International Conference on Electronics, 
Communication and Aerospace Technology, Coimbatore, India, 2022, pp. 1125-1129, doi: 
10.1109/ICECA55336.2022.10009165 

[11] K. Lutoslawski, M. Hernes, J. Radomska, M. Hajdas, E. Walaszczyk and Kozina, ”Food Demand 
Prediction Using the Nonlinear Autoregres- sive Exogenous Neural Network,” in IEEE Access, vol. 9, 
pp. 146123- 146136, 2021, doi: 10.1109/ACCESS.2021.3123255 

[12] M. N. M. Bhutta and M. Ahmad, ”Secure Identification, Traceability and Real-Time Tracking of 
Agricultural Food Supply During Transportation Using Internet of Things,” in IEEE Access, vol. 9, 
pp. 65660-65675, 2021, doi: 10.1109/ACCESS.2021.3076373. 

[13] H. Hewamalage, C. Bergmeir, and K.Bandara ”Recurrent neural net- works for time series 
forecasting: Current status and future direc- tions”,Int. J.Forecasting, vol. 37,no. 1, pp. 388–427,March 
2021,doi: doi.org/10.1016/j.ijforecast.2020.06.008 

[14] O. Suprun, N. Klimenkova, M. Melnyk and S. Lavriy, ”Forecasting and Analysis of Online Orders 
Rejections Using Data Mining Algorithms and Penalty Function,” 2021 IEEE 3rd International 
Conference on Advanced Trends in Information Theory (ATIT), Kyiv, Ukraine, 2021. 

[15] Amitesh and D. Kumar, ”Blockchain-based solution for Demand Forecasting in Supply chain,” 2021 
First International Confer- ence on Advances in Computing and Future Communication Tech- 
nologies kkk(ICACFCT), Meerut, India, 2021, pp. 217-224, doi: 
10.1109/ICACFCT53978.2021.9837339 

[16] N. Wang and Z. Liu, ”Food Material Consumption Prediction Of Catering Enterprises Based On Time 
Series Model,” 2021 IEEE 5th Advanced Information Technology, Electronic and Automation Con- 
trol Conference (IAEAC), Chongqing, China, 2021, pp. 965-968, doi: 
10.1109/IAEAC50856.2021.9390884 

[17] M. Astiningrum, V. N. Wijayaningrum and I. K. Putri, ”Analysis of Staple Food Price Forecasting 
Results Using Various Approaches,” 2021 7th International Conference on Electrical, Electronics and 
Information Engineering (ICEEIE), Malang, Indonesia, 2021, pp. 625-630, doi: 
10.1109/ICEEIE52663.2021.9616763 

[18] M. A. Zha`o and B. Setyawan, ”Sales Forecasting for Fresh Foods: A study in Indonesian FMCG,” 
2020 International Conference on Infor- mation Science and Communications Technologies 
(ICISCT), Tashkent, Uzbekistan, 2020, pp. 1-9, doi: 10.1109/ICISCT50599.2020.9351484. 

[19] C. -L. Yang and H. Sutrisno, ”Short-Term Sales Forecast of Perishable Goods for Franchise 
Business,” 2018 10th International Conference on Knowledge and Smart Technology (KST), Chiang 
Mai, Thailand, 2018, pp. 101-105, doi: 10.1109/KST.2018.8426091 

[20] X. -L. Wang, X. -L. Wu and B. -Y. Sun, ”Factor selection and regression for forecasting relief food 
demand,” 2012 8th International Conference on Natural Computation, Chongqing, China, 2012, pp. 
226-228, doi: 10.1109/ICNC.2012.623460. 

IJIRMPS2502232389          Website: www.ijirmps.org Email: editor@ijirmps.org 16