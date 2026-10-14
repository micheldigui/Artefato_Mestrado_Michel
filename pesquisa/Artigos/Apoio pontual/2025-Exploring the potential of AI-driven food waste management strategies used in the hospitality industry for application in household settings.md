---
source_file: "2025-Exploring the potential of AI-driven food waste management strategies used in the hospitality industry for application in household settings.txt"
original_rel_path: "Trabalhos\Artigos\Apoio pontual\txt\2025-Exploring the potential of AI-driven food waste management strategies used in the hospitality industry for application in household settings.txt"
category: "Artigos_Apoio_pontual"
extension: ".txt"
sha256: "001947cb7ade32e940cda20afd90cc04745b9d4f0f371a12ad8cbe1a729365bb"
extracted_at: "2026-09-20T00:05:05.680070"
---

﻿TYPE  Original Research
PUBLISHED  23 January 2025
DOI  10.3389/frai.2024.1429477

Exploring the potential of 
OPEN ACCESS AI-driven food waste 
EDITED BY
Tarun Belwal,  management strategies used in 
Texas A&M University, United States

REVIEWED BY the hospitality industry for 
Alessandro Bonadonna,  
University of Turin, Italy
Christian Bux,  application in household settings
University of Foggia, Italy

*CORRESPONDENCE
Quintana M. Clark 1*, Disha Basavaraja Kanavikar 2, Jason Clark 2Quintana Clark   

 quincy.clark@oregonstate.edu and Patrick J. Donnelly 2
RECEIVED 08 May 2024

1
ACCEPTED 28 December 2024  Department of Agricultural Sciences Education and the Department of Educational Practice and 

PUBLISHED 23 January 2025 Research, Oregon State University, Corvallis, OR, United States, 2 Department of Electrical Engineering 
and Computer Science, Science, Oregon State University Cascades Campus, Bend, OR, United States

CITATION
Clark QM, Kanavikar DB, Clark J and 
Donnelly PJ (2025) Exploring the potential of This study explores the potential for adapting AI-driven food waste management 
AI-driven food waste management strategies 
used in the hospitality industry for application strategies from the hospitality industry for application in household settings. 
in household settings. The hospitality industry, particularly hotels and restaurants, has implemented AI 
Front. Artif. Intell. 7:1429477. technologies through companies like Leanpath, Winnow, and Kitro, which use 
doi: 10.3389/frai.2024.1429477

real-time data and predictive analytics to monitor, categorize, and reduce food 
COPYRIGHT waste. These AI-driven systems have demonstrated significant reductions in food 
© 2025 Clark, Kanavikar, Clark and Donnelly. 
This is an open-access article distributed waste, offering economic savings and environmental benefits. This study employs 
under the terms of the Creative Commons an instrumental case study approach, utilizing semi-structured interviews with 
Attribution License (CC BY). The use, representatives from these companies to gain insights into the technologies and 
distribution or reproduction in other forums is 
permitted, provided the original author(s) and strategies that have proven effective in hospitality. The findings suggest that with 
the copyright owner(s) are credited and that modifications for scale, cost, and user engagement, AI-driven solutions could 
the original publication in this journal is cited, enhance household food management by providing insights into consumption 
in accordance with accepted academic 
practice. No use, distribution or reproduction patterns, offering expiration reminders, and supporting sustainable practices. 
is permitted which does not comply with Highlighted are key considerations for household adaptation, including policy 
these terms. support, educational strategies, economic incentives, and integration with smart 

home systems. Ultimately, this study identifies a promising avenue for reducing 
household food waste through AI, underscoring the need for continued research and 
policy initiatives to facilitate the transition of these technologies from commercial 
kitchens to everyday homes.

KEYWORDS

AI, food waste, sustainable technology, AI-driven, households

1 Introduction

Food waste is a critical global issue, with nearly one-third (about 2 billion tons) of all food 
produced annually for consumption going to waste (Xue et al., 2017; Fang et al., 2023). This 
wastage leads to approximately 3 billion tons of greenhouse gases being released from landfills 
and an annual economic loss of nearly $160 billion US dollars (Yu and Jaenicke, 2020). Food 
waste’s environmental and economic consequences are significant, representing a lost 
economic opportunity and negative ecological impacts. For example, when wasted food is 
deposited in landfills, it generates methane gas as it decomposes. Methane is more harmful to 
global warming than carbon dioxide (Xue et al., 2017; Fang et al., 2023). Additionally, food 
waste strains the agricultural industry, consuming vast amounts of valuable resources such as 
water, land, and energy for food that ultimately goes unconsumed (Kummu et al., 2012; 
Papargyropoulou et al., 2014).

Frontiers in Artificial Intelligence 01 frontiersin.org



Clark et al. 10.3389/frai.2024.1429477

The hospitality industry, which includes hotels, restaurants, and Intelligence, 2024), Winnow (The Food Waste Blog, 2024), and Kitro 
catering services, is particularly prone to food waste due to its (Kitro, 2024). Section 6, the discussion section, explores how 
operational nature (Papargyropoulou et al., 2019; Dhir et al., 2020). AI-driven food waste management strategies might be adapted for 
This sector operates on a large scale, with daily food preparation and household use. Section 7 discusses potential implications for 
consumption occurring in high volumes. The unpredictable nature of household adaptation, policy recommendations, and strategies for 
consumer demand and operational practices such as buffet-style research and education. Section 8 addresses the limitations of the 
dining and strict food safety regulations often result in a significant study. Finally, Section 9 concludes.
surplus of food that must be discarded (Papargyropoulou et al., 2019; 
Dhir et al., 2020). Furthermore, over-preparation in restaurants, where 
chefs prepare more food than necessary to avoid running out of 2 Background
popular dishes during peak hours, and plate waste from customers, 
where uneaten food is left on plates, contribute to the overall waste Food waste management refers to the practices and strategies 
(Parfitt et al., 2010). This waste includes leftover food and the resources implemented to reduce food waste in both post-production and 
used in its production, such as water, energy, and labor (Kummu et al., consumption (Sustainable Management of Food Basic, 2023). This 
2012; Dhir et al., 2020). The disposal of this waste typically involves process minimizes food waste’s negative environmental, economic, 
transporting it to landfills, where it decomposes and releases methane and social impacts. Food waste management encompasses a range of 
gas, exacerbating global warming (Fang et al., 2023; Papargyropoulou activities, from preventive measures that reduce food waste at the 
et al., 2014). source to AI-driven methods for recovering and recycling food waste, 

According to the Food Waste Index Report published by the such as returning nutrients to the soil through composting, 
United Nations Environment Program in 2021, 61% of total food greenhouse gas production from landfills, redistribution to those in 
waste occurs in households, 26% in food service establishments, and need through food banks, or creating renewable energy (Sustainable 
13% in retail businesses (Xue et al., 2017; United Nations Environment Management of Food Basic, 2023). Effective food waste management 
Programme, 2021). These statistics highlight the urgent need to reduce not only aids in environmental conservation but also can result in cost 
food waste at the hospitality and household levels. Given the savings and resource optimization.
magnitude of the issue, there has been a push for innovative solutions The global concern surrounding food waste has risen over the past 
to address food waste, particularly in industries where waste is most few decades. Research indicates that nearly a third of all food produced 
prevalent (Marvin et al., 2022; Papargyropoulou et al., 2014). Leading for human consumption gets lost or wasted, which equates to 
companies in the hospitality industry, such as Leanpath (Food Waste approximately 1.3 billion tons annually (Xue et  al., 2017; United 
Intelligence, 2024), Winnow (The Food Waste Blog, 2024), and Kitro Nations Environment Programme, 2021). Such vast amounts of 
(2024), have risen to the challenge by leveraging artificial intelligence unconstrained food waste have dire consequences, including 
(AI) to address food waste. These companies have developed exacerbating greenhouse gas emissions from landfills, significant 
AI-driven technologies integrating with existing kitchen operations to financial losses, and an increased strain on the agricultural industry 
monitor and analyze food usage in real-time. By tracking the quantity (Fang et al., 2023). The paradigm of “from farm to fork” has expanded 
and type of wasted food, AI systems provide insights that help kitchen to “from farm to fork to landfill,” illuminating the gaps in our current 
staff adjust portion sizes, optimize inventory management, and reduce food systems (Gunders and Bloom, 2012). Urban food waste 
over-preparation (Marvin et al., 2022). By identifying patterns in food management becomes vital as urban areas grow and population 
waste, these technologies enable implementing more sustainable densities increase. Efficiently managing this waste can significantly 
practices, such as menu adjustments and more accurate demand curb the negative environmental impacts and promote sustainable 
forecasting, ultimately reducing waste and its associated environmental living (Kaza et al., 2018).
impact (Fang et al., 2023; Marvin et al., 2022; Dhir et al., 2020). Household food waste remains one of the most overlooked yet 

However, while significant strides have been made in reducing impactful areas of waste generation (Bunditsakulchai and Liu, 2021). 
food waste at the hospitality level, food waste management using Households must purchase wisely, store efficiently, and consume 
AI-driven technology at the household level remains an area that prudently to minimize waste (Bunditsakulchai and Liu, 2021). 
needs further exploration (Dhir et  al., 2020; Parfitt et  al., 2010). Composting serves as a recycling mechanism, turning organic waste 
Through interviews with major hospitality industry companies, the into a resource for gardening. Despite these practices, a significant 
objective of this study seeks insights into how these innovative volume of food remains in landfills, with unconstrained waste 
solutions can be adapted for household use (Creswell and Poth, 2016). contributing to greenhouse gas emissions, financial loss, and undue 
As households contribute significantly to food waste, adopting these pressure on the agricultural industry.
methods could benefit policymakers and consumers alike (Janssens 
et al., 2019; Teng et al., 2021).

This paper is organized as follows: Section 2 provides a 2.1 AI-driven technology in the hospitality 
background of food waste and discusses AI’s role in food waste industry
management within the hospitality industry and its potential 
applicability in the home environment. Section 3 explores theoretical The digital age has seen AI permeate various industries, 
and managerial perspectives on the potential for adapting AI-driven revolutionizing operations and business practices (Fang et al., 2023). 
solutions in household food loss and waste management. Section 4 The hospitality industry, grappling with substantial food waste, has 
outlines the methods and procedures used in this case study. Section been no exception (Papargyropoulou et al., 2019). AI’s data-driven 
5 presents the findings from interviews with Leanpath (Food Waste approach offers predictive analytics, automates waste management, 

Frontiers in Artificial Intelligence 02 frontiersin.org



Clark et al. 10.3389/frai.2024.1429477

and provides actionable insights to reduce food waste significantly Households form the base unit of food consumption, collectively 
(Fang et al., 2023; Marvin et al., 2022). Innovations in AI-driven representing a significant proportion of food waste (Parfitt et al., 2010). 
technology have been introduced to tackle the issue of food waste, Addressing the issue at this micro-level can exponentially enhance the 
especially in industries where the volume of waste is exceptionally larger objective of curbing food waste at the macro level. Several 
high. The hospitality industry, a significant contributor to the challenges must be considered when translating the large-scale practices 
problem, has adopted various tech-driven solutions to optimize of the hospitality industry to individual households. For instance, food 
operations and reduce food waste (Engström and Carlsson- waste volume and consistency in restaurants and hotels are often more 
Kanyama, 2004). The hospitality industry, comprising hotels, predictable than in domestic settings, where variability in consumption 
restaurants, and catering services, is pivotal in global food patterns, dietary choices, and purchasing behaviors come into play 
distribution and consumption. Historically, this industry has been (Janssens et al., 2019). The economic incentives for households to invest 
identified as a significant contributor to food waste due to the in advanced AI-driven solutions may not be as immediately apparent 
industry’s operational nature, which necessitates surplus provisioning as they are for businesses. Nevertheless, there are many potential 
to meet diverse consumer demands. With high standards for food advantages. With the integration of AI into smart home systems and 
presentation and quality, substantial amounts often get discarded. IoT devices, households can benefit from predictive analytics. Such 
This waste not only implies economic losses but also an unnecessary systems could offer real-time insights into consumption patterns, 
environmental footprint. The hospitality industry has realized that recommend grocery purchasing decisions based on historical data, and 
efficient food waste management can bring tangible economic provide creative solutions for repurposing or composting leftover food. 
benefits beyond the apparent environmental and moral imperatives. All of these assist in reducing food waste and can contribute to 
As a result, there is an increasing trend in the industry to employ significant savings for households in the long run (Teng et al., 2021).
advanced AI-driven technologies to devise and implement effective Table 1 provides a side-by-side comparison of AI-driven food 
waste management strategies (Fang et al., 2023; Papargyropoulou waste management features as applied in the hospitality industry 
et al., 2014). versus potential adaptations for household use. Each feature illustrates 

In recent years, several technological solutions have been how these technologies, originally designed for large-scale, high-
developed to address the challenge of food waste in the hospitality volume settings, can be scaled down and customized to address the 
industry. Leanpath, Winnow, and Kitro have emerged as leaders in unique needs of individual households. In hospitality settings, Smart 
leveraging AI to mitigate waste. Their systems employ sophisticated bins with scale and AI camera automatically track, weigh, and 
algorithms and sensors to identify, categorize, and quantify discarded categorize food waste, helping commercial kitchens monitor waste 
food. These real-time insights provide actionable feedback to the and make data-driven adjustments (Fang et al., 2023; Marvin et al., 
hospitality industry, enabling them to adjust their practices and reduce 2022; Bux, 2024; Bux and Amicarelli, 2024). In a household context, a 
food waste. The success of such AI-driven systems in a high-waste more compact version of this bin would track waste types and 
environment like hospitality sparks interest in their potential amounts, offering simplified insights. Centralized dashboard 
applicability to the household environment. The advancements from monitoring (Bux, 2024; Bux and Amicarelli, 2024) is another key 
these organizations have led to a paradigm shift in how the hospitality feature in hospitality, where a large display provides real-time waste 
industry approaches food waste. These AI systems facilitate immediate metrics to staff. At home, a mobile app could serve as a personal 
intervention and longer-term strategic planning by offering real-time dashboard, summarizing waste data, notifying users about expiring 
analytics. The cumulative effect of these technologies is not just items, and offering waste reduction tips. Predictive inventory 
limited to economic savings for businesses. They have contributed to management (Bux, 2024; Bux and Amicarelli, 2024) helps commercial 
a more sustainable and responsible hospitality industry, setting the kitchens adjust stock levels based on historical demand, while a 
stage for scalable solutions that might be  transferred to the home household version might be integrated into a smart fridge to remind 
environment (Dhir et al., 2020). users of upcoming expiration dates. Additionally, AI-enhanced point 

of sale (POS) systems (Bux, 2024; Bux and Amicarelli, 2024) optimize 
portion sizes and menu planning in hospitality; for households, a 

2.2 AI’s potential applicability to home mobile app could suggest weekly shopping lists or meal plans based 
environment on past consumption patterns to avoid overbuying. Lastly, data-driven 

feedback loops and employee training & engagement (Bux, 2024; Bux 
There is potential for adapting AI-driven solutions from the and Amicarelli, 2024) in hospitality encourage continuous 

hospitality industry for household use. While households represent a improvements and participation, while at the household level, app 
significant contributor to food waste, their inconsistent and varied notifications can remind users to use leftovers and suggest recipes, 
food consumption patterns pose challenges to applying AI innovations fostering mindful consumption. Table  1 highlights both the 
directly. However, with the advent of smart home systems and the adaptability and potential barriers to transferring these advanced 
Internet of Things (IoT), there is an opportunity to utilize predictive technologies into everyday household environments.
analytics for improved food consumption, purchasing decisions, and 
waste reduction (Fang et al., 2023). Through user-friendly applications, 
households can optimize food utilization, providing economic and 3 Literature review of theoretical and 
environmental benefits. The success of AI-driven interventions in the managerial perspectives
hospitality industry poses a pertinent question, i.e., what is the 
potential applicability of AI-driven food waste management methods Household food loss and waste are significant contributors to 
from the hospitality industry to the household environment? global food waste, posing challenges to sustainability, food security, 

Frontiers in Artificial Intelligence 03 frontiersin.org



Clark et al. 10.3389/frai.2024.1429477

TABLE 1  Comparison of AI-driven food waste management features in framework for understanding how AI can influence household 
hospitality vs. household settings.

decision-making, behavior, and waste management 
Feature Hospitality Household reduction practices.

setting setting Theory of planned behavior (TPB): Ajzen (1991) Theory of Planned 
Smart bin with scale Large commercial smart Compact smart bin with a Behavior (TPB) suggests that behavior is driven by three primary 
and AI camera bins with integrated basic camera and scale to factors: attitudes, subjective norms, and perceived behavioral control. 

cameras and scales for track and weigh In the context of food waste, TPB can explain how AI-driven tools can 
precise food waste household food waste. positively influence consumer behavior. AI systems that provide 
tracking, identifying food Provides simplified data timely reminders, consumption data, or personalized 
types, and weighing on waste amounts and recommendations enhance individuals’ perceived control over food 
discarded items. Data is types. management, reducing waste (Stancu et al., 2016). For instance, smart 
used for real-time refrigerators and AI-powered apps track food expiration dates and 
analytics. suggest meal plans, thus reinforcing responsible food consumption 

Centralized dashboard Real-time monitoring on Mobile app dashboard behaviors. When integrated into household settings, these AI-driven 
monitoring a centralized dashboard providing a weekly or tools can shift attitudes toward reducing waste by making the process 

in the kitchen, providing daily summary of food more convenient and accessible (Roodhuyzen et al., 2017). Nudge 
detailed analytics on food waste data, notifications theory: Nudge Theory, popularized by Thaler and Sunstein (2008), 
waste sources, types, and for expiring items, and posits that small environmental changes can encourage better 
costs. tips for reducing waste. decisions without restricting freedom of choice. AI systems in food 

waste management apply nudges by sending notifications to users 
Predictive inventory AI-driven inventory Smart fridge with AI 

about food approaching expiration or suggesting recipes to use up 
management system linked to capabilities, tracking food 

leftovers. In commercial settings like hospitality, nudges have been 
suppliers, predicting stock items inside and offering 

implemented to reduce waste by adjusting portions and optimizing 
needs based on historical shopping reminders or 

inventory (Principato et al., 2021).
data to avoid over- suggestions to use soon-

When adapted to households, AI-driven nudges can be equally 
ordering and minimize to-expire items.

effective. Applications like OLIO (Olio, 2024) and Too Good To Go 
waste.

(Too Good To Go, 2024) use notifications to nudge consumers into 
AI-enhanced point of POS system integrated Shopping and meal donating excess food or redistributing surplus before it becomes 
sale (POS) system with AI to collect data on planning suggestions via waste. However, their effectiveness in households depends heavily on 

popular menu items, the mobile app, based on sustained user engagement, as occasional use may not be enough to 
adjusting portion sizes, previous household usage drive long-term behavioral change (Filimonau and Gherbin, 2017). 
and minimizing over- patterns, to help prevent Rational choice theory: Rational Choice Theory (Becker, 1976) assumes 
preparation. overbuying. that individuals make decisions by evaluating costs and benefits. AI 

Data-driven feedback Automated feedback sent Notifications on the systems align with this theory by reducing the cognitive load required 
loops to kitchen staff, helping mobile app reminding to make food management decisions. By automating tasks such as 

them adjust portion sizes, users to use leftovers or inventory tracking, meal planning, and expiration date alerts, AI tools 
menu offerings, and suggesting recipes based offer households rational solutions to minimize waste (Aschemann-
inventory levels. on available ingredients. Witzel et  al., 2015). In the hospitality industry, AI technologies 

Employee training and Staff receive training and Home users receive waste optimize supply chains and reduce waste by providing real-time data 
engagement ongoing feedback on food reduction tips and on inventory levels. Similar household tools can help consumers make 

waste practices, often with personalized suggestions more informed purchasing decisions, thus reducing the likelihood of 
features like leaderboards on the app, encouraging overbuying and food spoilage (Borrello et al., 2016). However, the 
or waste reduction goals mindful consumption success of such AI tools depends on whether households perceive the 
to encourage habits. long-term benefits as outweighing the initial costs and effort involved 
participation. in adopting the technology (Quested et al., 2013). AI and machine 

This table compares the adaptation of AI-driven food waste management features from learning frameworks: AI technologies use machine learning algorithms 
large-scale hospitality settings to individual household environments. While hospitality to predict food consumption patterns and provide personalized 
applications are optimized for high-volume operations, household adaptations focus on user- recommendations. Predictive analytics, a common AI technique, uses 
friendly, compact solutions with simplified data outputs.

historical data to forecast future food usage, helping households 
reduce overbuying and better manage their stock (van der Werf et al., 

and environmental conservation (Kitro, 2024; Bux and Amicarelli, 2021). The ability of AI systems to learn from user behavior and adjust 
2024). Recent developments in AI-driven solutions have shown the their recommendations over time is particularly valuable in household 
potential to mitigate this issue by leveraging predictive technologies settings where consumption patterns can be  irregular. In the 
and data-driven insights to manage food consumption and waste. This hospitality industry, predictive analytics has significantly reduced food 
literature review explores theoretical and managerial perspectives on waste by up to 30% in some settings (Filimonau and Gherbin, 2017). 
the potential for adapting AI-driven solutions, developed initially for However, adapting such models to households presents challenges due 
sectors such as hospitality, to manage household food loss and waste. to the variability in household consumption patterns and the often-
The behavioral and technological theories discussed provide a limited data available. Nonetheless, the potential for AI to provide 

Frontiers in Artificial Intelligence 04 frontiersin.org



Clark et al. 10.3389/frai.2024.1429477

adaptive and personalized solutions remains promising (Roodhuyzen controlled environment, concerns about data privacy are less 
et al., 2017). prevalent. To increase adoption in households, AI developers must 

From a managerial standpoint, adopting AI-driven solutions for prioritize transparency and address concerns about data privacy. 
household food waste management requires considering several Providing clear information about how data is used and the benefits 
factors: cost, technological infrastructure, consumer trust, and long- of AI systems can help build consumer trust and encourage more 
term engagement. Lessons from the hospitality industry, where widespread adoption (Quested et al., 2013).
AI-driven solutions are successfully implemented, can provide While theoretical frameworks such as the Theory of Planned 
valuable insights for household adoption. Behavior and Nudge Theory provide insights into how AI can 

Adoption of AI in food waste management: AI technologies, such influence household behavior, practical barriers such as cost, 
as smart refrigerators, food tracking apps, and AI-powered supply technological infrastructure, and consumer trust remain significant 
chain systems, have been widely adopted in hospitality to optimize obstacles. By learning from the successes of AI-driven solutions in the 
food consumption and reduce waste. For instance, restaurants use AI hospitality industry and addressing these challenges, AI systems have 
to predict customer demand and adjust inventory accordingly, the potential to transform household food management and 
reducing excess purchases and spoilage (Filimonau and Gherbin, significantly reduce food waste. Table  2 summarizes fundamental 
2017). The same principles can be applied in households, where AI studies that span theoretical and managerial perspectives, offering 
systems help families track food expiration dates, monitor inventory, insights into the behavioral theories that underpin consumer decision-
and reduce overbuying (van der Werf et al., 2021). However, adopting making and the practical challenges associated with adopting AI 
AI in households is slower due to several managerial challenges, technologies in households.
including cost, accessibility, and consumer engagement. AI tools often 
deliver immediate financial benefits in commercial settings by 
reducing waste and optimizing operations. The financial return on 4 Methods and procedures
investment is less obvious in households, which can deter adoption 
(Stancu et  al., 2016). Cost and accessibility: One of the primary This study employed an instrumental case study approach 
challenges in adopting AI-driven solutions in households is the cost (Creswell and Poth, 2016) to explore the potential applicability of 
of smart appliances and AI-driven systems. In the hospitality industry, AI-driven food waste management methods from the hospitality 
large-scale operations justify the expense of AI technologies due to industry to the household environment (Creswell and Poth, 2016). 
their ability to save costs by reducing waste (Principato et al., 2021). The central focus of this case study is to identify and analyze AI-driven 
For individual households, however, the upfront cost of smart food waste management methods that have been successfully 
refrigerators, for example, can be prohibitively high. implemented in the hospitality industry, intending to evaluate their 

Moreover, households may be unwilling to invest in technology if potential for adaptation in households. The selected case units for this 
they do not perceive a clear financial benefit or if they lack familiarity study are three leading companies in the hospitality industry, i.e., 
with AI systems (Quested et al., 2013). Low-cost alternatives, such as Leanpath (Food Waste Intelligence, 2024), Winnow (The Food Waste 
food consumption tracking mobile apps, offer a more accessible Blog, 2024), and Kitro (Kitro, 2024). Each company has established a 
option for households. Apps like OLIO (Olio, 2024) and Too Good To reputation for implementing advanced AI technologies in various 
Go (Too Good To Go, 2024) allow users to monitor their food usage hospitality settings, including hotels and restaurants. These companies 
without needing expensive appliances. However, the long-term utilize kitchen-ready trackers, integrated scales, and touchscreens as 
success of these tools depends on sustained engagement and regular part of their AI-driven systems to monitor, track, and measure 
use (Filimonau and Gherbin, 2017). Technological infrastructure: AI food waste.
technologies require reliable data inputs and a robust technological The data collection was conducted through semi-structured 
infrastructure to function effectively. In hospitality, AI technological interviews with key representatives from each selected company. 
systems are supported by integrated supply chains and real-time data Semi-structured interviews are an important source of case study 
collection, which ensures that AI-driven recommendations are evidence (Yin, 2017). The interviews were designed to gather 
accurate and timely (Filimonau and Gherbin, 2017). In households, comprehensive insights into the specific AI-driven technologies used 
the lack of such infrastructure can limit the effectiveness of AI tools. by these companies, the challenges they encountered during 
For example, smart refrigerators and food tracking apps rely on users implementation, and the overall impact of their initiatives on reducing 
to input accurate food purchases and consumption data. Without food waste. In addition to exploring the technical aspects of the AI 
consistent data, AI systems may struggle to provide useful systems, the interviews also explore methods employed by these 
recommendations, reducing their effectiveness (van der Werf et al., companies, such as machine learning algorithms, sensor technologies, 
2021). To overcome this barrier, AI systems for households must and data analytics tools, to enhance the effectiveness of their food 
be highly automated and user-friendly, requiring minimal user input waste management strategies.
to maintain accurate data on food inventories and expiration dates A thorough analysis of the recorded interview data was conducted 
(Roodhuyzen et  al., 2017). Consumer trust and data privacy: to identify the core AI-driven methods and technologies utilized in 
Consumer trust is another significant barrier to adopting AI-driven the hospitality industry and to evaluate their potential for application 
technologies in household food waste management. Many consumers in household settings. This analysis involved transcribing the interview 
are wary of sharing personal data with AI systems, particularly when data and systematically categorizing the identified technologies based 
it comes to sensitive information about their purchasing habits and on their specific applications in reducing food waste. The process 
consumption patterns (Filimonau and Gherbin, 2017). In the included (a) identifying AI-driven technologies, such as machine 
hospitality industry, where data is collected and managed within a learning algorithms, sensor technologies, and data analytics tools, and 

Frontiers in Artificial Intelligence 05 frontiersin.org



Clark et al. 10.3389/frai.2024.1429477

TABLE 2  Summary of references, study focus, key findings, and relevance to AI technology.

References Focus of study Key findings Relevance to AI technology
Ajzen (1991) Introduces the theory of planned Perceived control over behavior can Provides foundational insights into 

behavior as a framework for behavior reduce food waste through better behavior change, applicable in AI 
change relevant to understanding food management practices. algorithms for personalized waste 
waste behaviors. management recommendations.

Aschemann-Witzel et al. (2015) Examines causes of consumer food Consumer education and awareness are 
waste and proposes potential critical for reducing food waste; Highlights behavioral causes of waste, 
interventions for behavior change. identified psychological and societal which AI systems could use to customize 

causes. interventions and awareness prompts.

Becker (1976) Applies Rational Choice Theory to Perceived costs and benefits of waste Rational Choice Theory can 
consumer decision-making in areas such reduction influence decision-making be integrated into AI-driven decision-
as food waste management. processes in food management. support systems for optimizing 

household purchasing behaviors.

Borrello et al. (2016) Explores challenges in transitioning to a Identifies regulatory, economic, and Identifies systemic challenges in food 
bio-based circular economy within the technological challenges in reducing waste, which AI could help address by 
agri-food sector. waste within a bio-based economy. integrating supply chain and 

consumption data.

Bux (2024) Investigates digital and conventional Found digital solutions that are more Digital methods for waste tracking align 
methods for monitoring food waste in accurate in waste tracking, providing with AI’s role in data collection, analysis, 
healthcare settings. better data for managing food supplies. and real-time monitoring.

Bux and Amicarelli (2024) Discusses the role of blockchain in Blockchain can improve transparency in Shows blockchain potential for AI 
tracking food waste and enhancing food waste monitoring, potentially systems to enhance traceability and 
sustainability in food security. increasing consumer trust in the food transparency in food waste management.

supply.

Filimonau and Gherbin (2017) Examines food waste management Adopting sustainable waste practices can Insights into retail practices can guide 
practices in the UK grocery sector, lead to economic and environmental AI systems in optimizing inventory and 
focusing on sustainable practices. benefits for grocery retailers. reducing waste in household and 

commercial settings.

Principato et al. (2021) Provides a systematic review of Consumers’ food waste behaviors are The framework can support AI in 
consumer behavior related to household complex and shaped by social norms, identifying patterns and predicting 
food waste. habits, and situational factors. high-risk waste behaviors.

Quested et al. (2013) Analyzes complex behavioral patterns Food waste behaviors are multifaceted; Complex behavior analysis supports AI 
related to food waste using qualitative qualitative methods can capture the in designing adaptive feedback for user 
approaches. range of motivations behind waste. behavior improvement.

Roodhuyzen et al. (2017) Proposes an integral perspective on Suggests a holistic approach to waste Integral perspective aids AI in 
consumer food waste behaviors to management, integrating various developing holistic waste management 
address waste issues holistically. consumer behavior perspectives. models, incorporating multiple factors.

Stancu et al. (2016) Identifies key determinants of food Found that psychological factors and Behavioral insights support AI in 
waste behavior, focusing on daily habits significantly influence waste tailoring nudges and feedback loops to 
psychological and habitual factors. behavior in households. reduce household food waste.

Thaler and Sunstein (2008) Nudge Theory as a framework for Nudge strategies can reduce waste by Nudge Theory is highly relevant for 
behavior influence, with applications for subtly guiding consumer choices AI-based reminders and prompts 
reducing food waste. without restricting options. encouraging sustainable food practices.

van der Werf et al. (2021) Tests an intervention aimed at reducing Behavioral interventions showed Behavioral intervention data supports AI 
household food waste through significant potential in reducing waste models in designing household cost-
behavioral change techniques. and increasing savings in households. saving and waste-reducing strategies.

This table provides a selective overview of key studies relevant to AI-driven food waste management and consumer behavior.

categorizing these technologies based on their role in reducing food challenges and benefits of AI-driven food waste management in the 
waste. Additionally, we analyzed the methods the hospitality industry hospitality industry, particularly focusing on practical considerations 
uses to integrate AI into food waste management practices, focusing and obstacles when implementing similar solutions in household 
on the strategies and techniques for collecting and analyzing data settings. The transcribed data were then sent to the interviewed 
related to food waste. The analysis also involved (b) identifying the representatives from each company for peer review, with the 

Frontiers in Artificial Intelligence 06 frontiersin.org



Clark et al. 10.3389/frai.2024.1429477

understanding that certain proprietary protocols and sensitive examines machine learning algorithms, sensor technologies, and 
information could not be  disclosed or shared publicly. This step data analytics tools employed within the hospitality industry to 
ensured the accuracy of the information while maintaining the identify, categorize, and quantify food waste and generate actionable 
confidentiality of company-specific practices. insights for reduction. The study also considers the AI-driven 

The study also aimed to assess the feasibility of adapting these methods and approaches the hospitality industry employs to 
AI-driven technologies for use in household settings, which involved integrate AI into food waste management processes, including 
evaluating the practical considerations, challenges, and potential strategies and techniques for data collection and analysis related to 
benefits of implementing similar solutions in a domestic environment. food waste. Additionally, the study assesses the challenges and 
Key factors considered in this evaluation included the variability in benefits of adopting AI in the hospitality sector, identifying obstacles 
food consumption patterns in households compared to hospitality to implementing AI-driven food waste solutions and the advantages 
settings, the economic viability of such technologies for individual of their use.
consumers, and the potential obstacles that might arise during the 
adaptation process.

In summary, this comprehensive approach combines detailed data 5 Findings
collection with in-depth analysis, providing a clear pathway for 
assessing the potential for AI-driven food waste management Findings reveal Leanpath, Winnow, and Kitro’s effectiveness in 
technologies to be  adapted from the hospitality industry to the employing AI-driven food waste management systems in hospitality. 
household environment. By systematically exploring the methods, The analysis covers their technological solutions, system 
technologies, and practical implications of such an adaptation, the configurations, data analytics, and user engagement, discussing the 
study offers valuable insights into the broader application of AI in potential for home use and impacts on sustainability and efficiency. 
promoting sustainable food waste management practices across The industry term for these AI-driven bins is smart-bin. Figure 1 
different contexts. illustrates a smart-bin setup of (1a) Leanpath, (1b) Winnow, and (1c) 

Kitro’s commercially available models for AI-driven food waste 
management systems as of 2024.

4.1 The case

This research examines the application of AI-driven food waste 5.1 Leanpath
management practices by three leading companies servicing the 
hospitality industry: Leanpath, Winnow, and Kitro. These companies, Leanpath was founded in 2004, creating the first automated food 
serving as the case study’s units, operate within the food service sector, waste measurement technology system for food service and hospitality 
targeting hotels, restaurants, and institutional cafeterias, including kitchens and, in the process, creating an industry. Their system 
those in colleges, hospitals, corporate settings, sports, and leisure integrates a touchscreen terminal with scales and cameras and AI 
facilities. These companies primarily focus on the commercial market. recognition technology across a suite of models, capturing critical data 
Their platforms for preventing food waste incorporate kitchen-ready such as the type and amount of food waste per transaction, the cost, 
trackers, integrated scales, and touchscreens, allowing for efficient the reason for the waste, the source, and the disposition of the waste. 
tracking, measurement, and photographic documentation of food The data (and digital images on specific models) flow to Leanpath’s 
waste. These platforms process data through a sophisticated analytical cloud-based platform (Leanpath Online) for analysis of the 
platform, providing insights into the causes of waste generation and composition of food waste across multiple dashboards coupled with 
encouraging behavioral change. behavior change functionality, which leverages AI and culinary 

This study examines companies using AI-driven technologies in experts to guide operational changes to prevent the recurrence of 
commercial kitchens to monitor and reduce food waste. The study food waste.

FIGURE 1
(1a) Leanpath, (1b) Winnow, and (1c) Kitro’s commercially available models for AI-driven food waste management systems as of 2024.

Frontiers in Artificial Intelligence 07 frontiersin.org



Clark et al. 10.3389/frai.2024.1429477

AI-driven methods and approaches employed: categorize the food waste transaction without any screen interaction 
Leanpath utilizes a “track-discover-drive” methodology. When required from the staff. In cases where the AI’s confidence has not 

kitchen staff discard food, the type of food and the reason for reached the threshold required for automatic, no-touch 
discarding it (e.g., overproduction, spoilage, trim waste) are tracked categorization, the system will predict a shortlist of eight potential 
in seconds on a touchscreen terminal that draws on a customized items -- these eight menu items are then displayed on the screen for 
menu specific to each location. A comprehensive analytics platform the staff to choose from. Each instance in which the staff provides 
complements this process: multiple dashboards with intuitive the system with the correct selection helps inform the universal AI 
graphics, a digital photo stream, and alert functionality to flag specific model for the next time that item is thrown away to reach automatic 
waste transactions in real-time interventions, goal functionality to categorization with most of a kitchen’s food waste items. Winnow 
target and track waste reduction for specific high-value items over a also provides clients with leading analytics. This includes periodic 
defined period, donation tracking, and AI-enhanced coaching tips. automated PDF reports and access to their online dashboard, 
The system provides comprehensive reports (at individual and Winnow Hub, which allows users with plenty of functionality to 
enterprise levels) to identify types and sources of food waste, enabling view and manipulate the food waste data in real-time, download 
establishments to take actionable steps like adjusting batch sizes or additional reports, and compare performance across locations in 
modifying menus and portion sizes. Leanpath also emphasizes staff the case of a multi-site client. Winnow also provides a dedicated 
engagement and continuous monitoring to cultivate a culture of food customer success manager for each new client, who provides the 
waste prevention, including a leaderboard feature to encourage staff with coaching to discuss the reports and help identify 
participation and positive competition between locations. They offer reduction opportunities within the data.
coaching by experienced chefs to integrate food waste prevention 
techniques into daily kitchen practices. Challenges and benefits faced:

Winnow faced several challenges, including bin placement 
Challenges and benefits faced: issues, security concerns during installations, and the need for 

In Leanpath’s startup phase, Leanpath faced typical logistical staff engagement. Resistance from staff not using the system 
and cultural challenges of scaling globally and educating busy food correctly or prioritizing waste reduction also posed obstacles. 
service leaders on the importance of committing to a bold food However, the benefits have been significant. Winnow’s approach 
waste reduction goal and the strong value proposition within food has resulted in an average of 53% reduction in food waste across 
waste prevention. Despite these challenges, Leanpath has made their customer base, resulting in substantial economic savings. 
notable achievements in food waste reduction, typically cutting This achievement aligns with a shift in client focus from cost 
food waste by 50% in client sites and reducing food purchase costs savings to sustainability goals.
by up to 6% while engaging frontline food service workers in 
creating a culture of food waste prevention. Today, the company 
operates in over 4,000 locations and 29 languages across 45 5.3 Kitro
countries. It has prevented over 120 million pounds of food waste 
since its inception. In addition to cost savings, Leanpath’s platform Established in 2017, Kitro’s AI-driven technology comprises a 
provides environmental data associated with food waste savings for camera and weighing scale system designed to automatically detect 
sustainability reporting. and categorize food waste. The system utilizes weight sensors and 

cameras to capture images of discarded food, which are then processed 
using deep learning algorithms. This technology is deployed in various 

5.2 Winnow settings, including commercial kitchens, buffets, and guest plates, to 
monitor food waste effectively.

Winnow was established in 2013. They introduced their AI 
model Winnow Vision Technology in 2019, significantly impacting AI-driven methods and approaches employed:
food waste management in the hospitality industry. This system Kitro employs a centralized algorithm that works across all 
comprises a scale and a smart camera positioned above a standard properties, negating the need for individual menu data. The system 
waste bin, capturing images and data of discarded food in real- records the waste’s weight, timing, and content when food is discarded. 
time. The Vision box, equipped with a light and motion-sensitive Image recognition and categorization of items occur in the cloud, 
camera, identifies various food items as they are thrown away. A where Kitro’s algorithm recognizes approximately 300+ food items. 
touchscreen tablet facilitates staff interaction when required and This granularity enables detailed data analysis. Kitro’s dashboard 
displays immediate feedback on the most recent food waste allows clients to filter data by categories, service times, and reasons for 
transaction’s financial and environmental impact. waste, assigning a price to each ingredient to calculate total food 

waste value.
AI-driven methods and approaches employed:

Winnow’s AI capability works in real-time and is enabled on Challenges and benefits faced:
day one of usage within a client kitchen. The staff may encounter Potential clients were initially reluctant to invest due to the 
two scenarios on the touchscreen when food is scraped into the bin, perceived slowing of productivity caused by manual data entry. 
depending on the confidence level of the AI for the item that was However, these obstacles have been overcome by Kitro, which offers 
thrown away. When the AI has reached a certain threshold of 100% automation for customers where no manual input or labeling is 
confidence in identifying the item, the system will automatically required, leading to significant benefits. Kitro’s clients report an 

Frontiers in Artificial Intelligence 08 frontiersin.org



Clark et al. 10.3389/frai.2024.1429477

average reduction in food waste of 30%, with some seeing a decrease and associated greenhouse gas emissions. The data collected is integral 
of over 50%. The system has also led to substantial cost savings, with to the technical development of these systems, informing the 
average annual savings of 2 to 8% of their annual food costs, algorithmic processes and the detailed data provided to customers. 
demonstrating a solid return on investment. These systems face challenges, including scalability, cultural and 

In summary, Leanpath, Winnow, and Kitro offer innovative language barriers in global markets, and logistical complexities of 
AI-driven food waste management solutions for the hospitality managing hardware components. Customer support is pivotal for 
industry, each employing different technologies tailored to their effective implementation, with companies offering training and 
unique approaches: Leanpath uses AI-powered cameras and scales to continuous monitoring to encourage staff engagement in waste 
track food waste in real-time, capturing images and data that feed into reduction practices. The pricing models and return on investment 
a cloud-based dashboard to identify waste patterns and inform (ROI) are significant factors, with some clients reporting substantial 
reduction strategies. Winnow integrates AI with cameras and scales cost savings. Looking ahead, these companies are committed to 
to automatically identify discarded food items and quantify waste, continuous innovation, aiming to enhance their products’ accuracy 
providing actionable insights that allow kitchens to optimize inventory while exploring adaptations for potential household use to further 
and reduce waste costs. Kitro offers a fully automated solution using contribute to global waste reduction efforts.
sensors and cameras to record waste without manual input, analyzing The smart-bin products from Leanpath, Winnow, and Kitro 
the data to help businesses enhance sustainability and cut costs. each offer custom approaches to using AI-driven technology to 
Table  3 provides a detailed comparison of these companies’ reduce food waste in the hospitality industry. Leanpath’s system 
technologies, methods, and the potential benefits for focuses on continuous monitoring and detailed data analysis, 
household adaptation. identifying patterns in food waste, and developing actionable waste 

minimization strategies while continually reporting progress 
against an established baseline. Winnow utilizes a system that 

6 Discussion evolved from manual logging to AI-driven technology. Winnow’s 
Vision system features a camera and scale setup to capture real-time 

The innovative smart-bin products from companies like Leanpath, images and data of discarded food. The system predicts the type of 
Winnow, and Kitro utilize AI-driven technologies to address food waste using a universal model and automates the categorization 
waste in the hospitality industry. These systems combine AI imaging process over time. Winnow’s approach includes detailed client 
recognition and weighing mechanisms to monitor and quantify food reports and online data analysis tools, with a notable shift toward 
waste, focusing on sustainability and cost savings. Smart bins are sustainability goals among their clientele. Kitro, on the other hand, 
designed to identify the types of food wasted and measure their employs a scale and a camera to capture the weight and images of 
weight. Once quantified, the waste is translated into financial losses discarded food, which is processed by deep learning algorithms. 

TABLE 3  Comparison of AI-driven food waste management technologies in the hospitality industry.

Company Core technology AI-driven Waste measurement Potential Scope of 
methods technique household company 

benefits efforts
Leanpath, est. 2004 Integrated system with Track-Discover-Drive Tracks type, amount, reason, Detailed tracking, Prevented 120 M+ lbs. 

touchscreen, scales, methodology: real-time source, and disposal of food actionable insights, staff of food waste, operating 
cameras, and AI tracking, customizable waste per transaction engagement, continuous in 4,000+ locations 
recognition dashboards, behavior monitoring across 45 countries

change functionality, 
AI-enhanced coaching

Winnow, est. 2013 Smart camera, scale, and Winnow Vision Real-time categorization with Immediate feedback, easy Launched AI model in 
touchscreen system with Technology: AI financial and environmental categorization, staff 2019, 53% average 
AI for real-time tracking categorizes waste impact feedback training, and engagement reduction in food waste

automatically or 
suggests items for staff 
input; provides analytics 
via Winnow Hub and 
periodic PDF reports

Kitro, est. 2017 Camera and weighing Centralized AI model: Records weight, timing, and Fully automated, no Founded in 2017, 
scale system with image automatic detection and content; uses image manual input, cost achieves a 30% average 
recognition categorization, cloud- recognition for categorization savings, detailed analysis waste reduction, up to 

based processing, 50% in some cases
dashboards for analysis 
and reporting

AI-driven refers to artificial intelligence technology.

Frontiers in Artificial Intelligence 09 frontiersin.org



Clark et al. 10.3389/frai.2024.1429477

Kitro’s system offers a centralized algorithm that eliminates the behavior, suggesting optimal portion sizes, and offering reminders to 
need for individual menu data and recognizes approximately 300+ use perishable items before they spoil.
food items. This system provides extensive data analysis capabilities 
and client insights, assisting in optimizing operational processes. 7.1.3 Policy support and educational initiatives
Leanpath adopts a “track-discover-drive” methodology, combining Supportive policies and educational initiatives are crucial for 
a touchscreen terminal with a scale and supplementing it with adopting AI-driven food waste management technologies that are 
manual photo analysis and AI recognition. This approach widely adopted in households. Research has shown that public 
emphasizes the tangible (and repetitive) nature of food waste and awareness and education play significant roles in adopting sustainable 
engagement with frontline food service workers, coupled with practices (Moser, 2016). Governments and organizations could 
detailed waste reduction resources, behavior change functionality, promote AI technologies through subsidies, incentives, and public 
and expert coaching from veteran culinary professionals to foster a campaigns highlighting their benefits in reducing food waste and 
waste-conscious culture. saving money. Additionally, online platforms could offer training 

modules similar to those provided by Winnow in the hospitality 
industry but tailored to the needs of household users.

7 Potential implications
7.1.4 Scientific evaluation of household 

7.1 Adaptation for household use implementation
A rigorous scientific evaluation must be conducted to ensure the 

The transition from manual to automated food waste management successful adaptation of these technologies. Pilot programs in diverse 
processes, facilitated by AI-driven technologies, highlights the household settings could be used to test the effectiveness of these 
potential for significant environmental and economic benefits in AI-driven systems, gathering data on food waste reduction, user 
commercial and residential settings. This approach should consider engagement, and cost savings. These studies should also consider the 
households’ specific needs and behaviors and the technological, long-term sustainability of AI integration in households, exploring 
economic, and educational factors that influence the adoption and factors such as energy consumption, data privacy, and system 
effectiveness of AI-driven solutions. maintenance. For example, Kitro’s focus on continuous system 

improvement could be applied in the household context by regularly 
7.1.1 Lessons from the hospitality industry updating AI algorithms based on user feedback and waste patterns to 

The successful application of AI-driven technologies by companies maintain accuracy and relevance.
such as Leanpath, Winnow, and Kitro in the hospitality industry 
provides valuable insights for potential household adaptation. These 7.1.5 Integration with smart home systems
systems have significantly reduced food waste in commercial settings Finally, integrating AI-driven food waste management 
through continuous monitoring, real-time data analytics, and user technologies with existing smart home systems could enhance their 
engagement. For example, Leanpath’s systems have reduced food functionality and ease of use. By connecting with smart refrigerators, 
waste by up to 50% in some settings by providing detailed feedback voice-activated assistants, and mobile apps, these systems could 
on waste generation and offering actionable insights for reduction provide holistic food management solutions that help households 
(Food Waste Intelligence, 2024). Similarly, Winnow’s AI technology reduce waste while optimizing grocery shopping and meal planning. 
has achieved an average 53% reduction in food waste through real- For example, sensors in smart refrigerators could alert users when 
time categorization and feedback (The Food Waste Blog, 2024; Nu items are nearing their expiration date. At the same time, AI-driven 
et al., 2024). These successes suggest that, with proper adaptation, apps could suggest recipes that use up leftover ingredients, further 
similar outcomes could be achieved in households. reducing waste.

7.1.2 Practical considerations for household 
adaptation 7.2 Policy recommendations and 

Adapting AI-driven technologies for residential use involves implementation
addressing several key challenges. First, the scale and complexity of 
the systems used in commercial kitchens must be reduced to suit the A multifaceted strategy encompassing policy recommendations 
household environment. This includes developing compact, user- and implementation steps is essential to harness the full potential of 
friendly devices that integrate seamlessly into daily household AI-driven technologies in household food waste management. Such a 
routines. For instance, Leanpath’s technology could be miniaturized strategy should facilitate adopting and integrating these technologies 
to fit under kitchen counters, with simplified interfaces allowing users into daily life and address critical interoperability, privacy, economic 
to track and analyze their food waste. viability, and public engagement challenges. By developing 

Moreover, continuous monitoring and real-time feedback, which comprehensive policies and initiatives, stakeholders can ensure that 
are central to the effectiveness of these systems, must be tailored to the AI-driven solutions for food waste management are accessible, secure, 
more variable and less predictable nature of household food and practical, contributing to environmental sustainability and 
consumption. Studies have shown that household food waste is often household economic savings. The following strategies outline the 
driven by over-purchasing, improper storage, and lack of meal critical components of such an approach, aiming to create a robust 
planning (Parizeau et al., 2015). AI-driven systems could address these framework for the widespread adoption of AI in reducing food waste 
issues by providing personalized recommendations based on past at the household level.

Frontiers in Artificial Intelligence 10 frontiersin.org



Clark et al. 10.3389/frai.2024.1429477

7.2.1 Establishing standardized protocols and Integrating AI-driven technologies into household food waste 
frameworks management will likely require a concerted effort that spans policy 

Developing and enforcing standardized protocols and frameworks formulation, technological innovation, economic incentives, and 
is crucial for ensuring interoperability among AI systems in food public engagement. By establishing standardized protocols, ensuring 
waste management. This standardization enables seamless interaction data privacy and security, offering economic incentives, fostering 
and efficient data sharing between AI tools and platforms, facilitating collaborations with technology providers, launching public awareness 
a unified approach to tracking and analyzing food waste patterns. initiatives, and implementing monitoring and feedback mechanisms, 
Additionally, standardization can accelerate the adoption of AI-driven we can create a supportive ecosystem for AI technologies to thrive. 
technologies by providing a clear set of guidelines for developers This comprehensive approach addresses the immediate challenges of 
and users. adopting AI for food waste management and sets a foundation for 

sustainable practices that can lead to significant environmental and 
7.2.2 Ensuring robust data privacy and security economic benefits. As we  move forward, it will be  crucial to 

Implementing stringent data privacy and security measures is continuously evaluate and adapt these strategies to meet evolving 
essential in protecting sensitive household information collected by needs and maximize the positive impact of AI on reducing food waste 
AI-driven food waste management systems. This includes employing in households.
advanced encryption methods, secure data storage solutions, and 
strict access controls to prevent unauthorized data access and 
breaches. Protecting personal data upholds user confidentiality and 7.3 Research and educational strategies
builds trust in AI technologies, encouraging wider acceptance and use.

A detailed focus on research and educational strategies is 
7.2.3 Providing economic incentives paramount to optimizing the implementation of AI-driven 

Offering economic incentives, such as tax breaks, subsidies for technologies and their efficacy in household food waste management. 
purchasing smart appliances equipped with AI-driven technologies, These strategies should aim to advance the technological aspects of AI 
and rewards for verifiable reductions in food waste, can motivate solutions and address the human, ethical, and economic factors 
households to invest in and adopt AI-driven solutions. These influencing their adoption and impact (The Food Waste Blog, 2024). 
incentives can lower the financial barriers to acquiring new The following strategies outline a framework for integrating research 
technologies and highlight the economic benefits of reducing food and education into developing and disseminating AI-driven food 
waste, making adopting sustainable practices more attractive waste management solutions.
to consumers.

7.3.1 Behavioral studies on food consumption 
7.2.4 Facilitating collaboration with technology and waste
providers Conducting in-depth studies to understand the underlying 

Forming strategic partnerships with technology providers and human behaviors contributing to food consumption and waste is 
appliance manufacturers can ease the integration of AI tools into essential. These studies should examine psychological, cultural, and 
household appliances and enhance the development of innovations socioeconomic factors influencing household food waste behaviors. 
tailored to specific user needs. Collaborations can leverage the Insights gained from such research can inform the design of targeted 
strengths of both the public and private sectors, driving the creation educational interventions, promoting sustainable food consumption 
of user-friendly, efficient, and practical solutions for managing food and waste reduction practices.
waste at the household level.

7.3.2 Addressing ethical concerns in AI usage
7.2.5 Launching public awareness initiatives Future research must tackle ethical issues, especially data privacy 

Raising public awareness about the importance and benefits of and security in household AI applications. Raising awareness about 
AI-driven food waste management is key to fostering cultural and these ethical considerations through educational campaigns and 
behavioral change. This can be  achieved through comprehensive discussions can encourage the responsible use of AI-driven 
educational programs, food waste management topics integration into technologies and ensure that privacy concerns do not hinder adoption.
school curricula, and national media campaigns designed to inform 
and engage the public. Highlighting food waste’s environmental and 7.3.3 Fostering cross-sector partnerships
economic impacts can galvanize individuals and communities to Establishing collaborations among AI developers, waste 
adopt more sustainable practices. management organizations, and governmental agencies is crucial for 

developing comprehensive and practical solutions. Educational 
7.2.6 Implementing monitoring and feedback programs can serve as a bridge for these partnerships, offering forums 
mechanisms for knowledge sharing, discussion, and collaborative innovation. Such 

Establishing robust monitoring and feedback mechanisms allows collaborations can also leverage diverse expertise to tackle the 
for the continuous refinement of AI tools and a deeper understanding multifaceted challenges of food waste management.
of user behavior and preferences. Collecting and analyzing data on 
how households use AI-driven systems for food waste management 7.3.4 Economic impact studies
can inform future improvements and innovations, ensuring these Undertaking thorough studies to assess the economic impacts of 
solutions remain effective and user-friendly. AI-driven food waste management systems is vital. These studies should 

Frontiers in Artificial Intelligence 11 frontiersin.org



Clark et al. 10.3389/frai.2024.1429477

analyze cost savings, potential revenue streams, and broader economic direct applicability of the findings to the household context without 
benefits of reducing food waste. Developing educational content based further adaptation and testing. The study assumes a certain level of 
on these findings can help households understand the financial technological literacy and willingness to adopt AI-driven solutions 
advantages of adopting AI solutions, enhancing stakeholder engagement among households. However, the readiness of average consumers to 
and support. engage with these technologies may vary, affecting the feasibility of 

widespread adoption (Nunkoo et al., 2021; Van Geffen et al., 2020).
7.3.5 Sustainability and technological evolution Additionally, the economic feasibility for households to invest in 

Evaluating AI solutions’ long-term sustainability and adaptability AI-driven systems may differ significantly from commercial entities, 
within the rapidly evolving technological landscape is critical. which could limit the potential impact of these technologies at the 
Research in this area should focus on the durability of AI-driven household level (Fang et al., 2023; Onyeaka et al., 2023). Implementing 
technologies, their adaptability to new environmental challenges, and AI-driven technologies in households raises concerns about data privacy 
their compatibility with future technological advancements. and security, which this study did not explore extensively. While the 
Educational efforts can emphasize the importance of sustainable commercial sector may have more robust systems to protect sensitive 
practices and the role of AI in promoting environmental stewardship. data, households may face challenges ensuring their personal 

information is secure when using AI-driven food waste management 
7.3.6 Integrating AI into educational programs systems (Anggraeni et al., 2021). Finally, the study’s findings are based 

Investigating how AI technologies can be  incorporated into on a specific set of AI-driven technologies and operational practices 
educational curricula and programs is necessary to increase awareness within the hospitality industry. As such, the generalizability of these 
and understanding of food waste management challenges and solutions. findings to other contexts, such as smaller businesses, different cultural 
Initiatives could include developing workshops, seminars, and settings, or varying levels of technological infrastructure, may be limited. 
educational materials tailored to students and the broader community. Further research is necessary to explore how these AI-driven solutions 
We can foster a more sustainable future by educating younger generations could be tailored to meet the unique needs of different user groups.
and engaging them in AI-driven food waste management efforts.

Integrating AI-driven technologies into household food waste 
management necessitates a comprehensive approach combining 9 Conclusion
in-depth research with targeted educational initiatives. By 
understanding and addressing the complex interplay of human This paper explored the potential of AI-driven food waste 
behaviors, ethical considerations, economic impacts, and management strategies used in the hospitality industry for applications 
technological evolution, we  can enhance the adoption and to the typical household. Utilizing AI for household food waste 
effectiveness of these solutions. The strategies outlined above highlight management offers opportunities for research, innovation, and 
the importance of behavioral studies, ethical research, cross-sector societal change. While this paper lays the groundwork for potential 
partnerships, economic impact analyses, sustainability evaluations, applications, the future of this promising domain will be shaped by the 
and educational program integration. Together, these elements form evolution of technology, policy, societal attitudes, and effective 
a holistic framework for advancing AI-driven food waste management educational strategies. The urgent need to address food waste, with 
in a way that is expected to be both impactful and sustainable. Moving extensive environmental, economic, and social ramifications, 
forward, it will be essential to continue exploring these areas, fostering underscores the importance of innovative solutions, particularly in 
collaboration and innovation to reduce food waste and promote household management. This exploration into the transformative 
environmental stewardship at the household level. potential of AI technologies, initially tailored for the hospitality 

industry, reveals a promising avenue for tackling food waste. The 
convergence of AI advancements, digital connectivity, and societal 

8 Limitations focus on sustainability presents a unique opportunity. The proposed 
framework, including standardized AI solutions, robust data privacy 

While this study provides valuable insights into the potential protocols, economic incentives, public awareness initiatives, and 
application of AI-driven food waste management strategies from the collaboration with technology providers, offers a comprehensive 
hospitality industry to household settings, several limitations must approach to harnessing AI’s capabilities for sustainable food waste 
be recognized. The study focused on three leading companies, i.e., management. While challenges in implementation are acknowledged, 
Leanpath, Winnow, and Kitro - within the hospitality industry. While the pathway illuminated by these innovations, supported by informed 
these companies represent some of the most advanced AI-driven food policies and societal engagement, holds promise for significant waste 
waste management systems, the findings may not fully capture the reduction and cultivating a more sustainable global community. The 
diversity of approaches and technologies available in other sectors or study proposes avenues for adapting these technologies for household 
smaller-scale operations. This limitation suggests the need for broader use, potentially offering scalable solutions to global food waste 
research encompassing a wider range of companies and industries. challenges. The adaptability of these systems to home environments 
The study’s primary focus was on the hospitality industry, which hinges on simplifying the technology for personal use while retaining 
operates on a different scale and with various economic incentives the core functionalities that facilitate waste awareness and reduction. 
compared to household environments. The variability in household Exploring these systems’ potential adaptation to household settings 
food consumption patterns, waste generation, and technological opens exciting possibilities for reducing global food waste, enhancing 
adoption presents challenges that the study may not have fully sustainability, and driving economic savings. These companies’ 
addressed (Nunkoo et al., 2021). These differences might limit the AI-driven food waste management practices offer valuable lessons for 

Frontiers in Artificial Intelligence 12 frontiersin.org



Clark et al. 10.3389/frai.2024.1429477

the hospitality industry and signal broader applicability to households is based on work supported by the Foundation for Food & Agriculture 
and potentially other commercial settings. Research (FFAR) grant, Household Food Waste Measurement 

Challenge (grant ID #22-000420).

Data availability statement
Acknowledgments

The data supporting this study’s findings are not publicly available 
due to confidentiality agreements/legal restrictions, further inquiries The authors gratefully acknowledge the study participants Steve 
can be directed to the corresponding author. Finn of Leanpath, Gina Sears of Winnow, and Benno Rust of Kitro 

for their invaluable insights and contributions to this study. Their 
expertise and pioneering work in AI-driven food waste 

Ethics statement management greatly enriched our understanding and shaped the 
direction of this research. While we have maintained objectivity in 

The studies involving humans were approved by the Oregon State our analyses and discussions, in the interest of transparency, it is 
University, Human Research Protection Program, Institutional Review worth noting that our institution, Oregon State University, is a 
Board - HE-2023-247 Title: Smart compost bin for measuring home customer of Leanpath.
food waste. The studies were conducted in accordance with the local 
legislation and institutional requirements. The participants provided 
their written informed consent to participate in this study. Conflict of interest

The authors declare that the research was conducted in the 
Author contributions absence of any commercial or financial relationships that could 

be construed as a potential conflict of interest.
QC: Conceptualization, project administration, methodology, 

data curation, supervision, Writing – review & editing. DK: 
Conceptualization, analysis, Writing – review & editing. JC: 
Supervision, Writing – review & editing. PD: Funding acquisition, Publisher’s note
validation & investigation, Writing – review & editing.

All claims expressed in this article are solely those of the 
authors and do not necessarily represent those of their affiliated 

Funding organizations, or those of the publisher, the editors and the 
reviewers. Any product that may be evaluated in this article, or 

The author(s) declare that financial support was received for the claim that may be made by its manufacturer, is not guaranteed or 
research, authorship, and/or publication of this article. This material endorsed by the publisher.

References
Ajzen, I. (1991). The theory of planned behavior. Organ. Behav. Hum. Decis. Process. Engström, R., and Carlsson-Kanyama, A. (2004). Food losses in food service 

50, 179–211. doi: 10.1016/0749-5978(91)90020-T institutions: examples from Sweden. Food Policy 29, 203–213. doi: 10.1016/j.
Anggraeni, M. C., Silaban, C. A., Anggreainy, M. S., and Cahyadi, E. (2021). “Role of foodpol.2004.03.004

artificial intelligence in the management of food waste,” in 2021 2nd International Fang, B., Yu, J., Chen, Z., Osman, A. I., Farghali, M., Ihara, I., et al. (2023). Artificial 
Conference on Artificial Intelligence and Data Sciences (AiDAS). IEEE, 1–6. intelligence for waste management in smart cities: a review. Environ. Chem. Lett. 21, 

Aschemann-Witzel, J., de Hooge, I. E., Amani, P., Bech-Larsen, T., and Oostindjer, M. 1959–1989. doi: 10.1007/s10311-023-01604-3
(2015). Consumer-related food waste: causes and potential for action. Sustain. For. 7, Filimonau, V., and Gherbin, A. (2017). An exploratory study of food waste 
6457–6477. doi: 10.3390/su7066457 management practices in the UK grocery retail sector. J. Clean. Prod. 167, 1184–1194. 

Becker, G. S. (1976). The economic approach to human behavior. Chicago, IL: doi: 10.1016/j.jclepro.2017.07.229
University of Chicago Press. Food Waste Intelligence (2024). Food Waste Intelligence. Available at: https://blog.

Borrello, M., Lombardi, A., Pascucci, S., and Cembalo, L. (2016). The seven challenges leanpath.com/, (Accessed December 11, 2024).
for transitioning into a bio-based circular economy in the Agri-food sector. Recent Pat. Gunders, D., and Bloom, J. (2012). Wasted: how America is losing up to 40 percent of 
Food Nutr. Agric. 8, 39–47. doi: 10.2174/221279840801160304143939 its food from farm to fork to landfill. New York, NY: The National Resource Defense 

Bunditsakulchai, P., and Liu, C. (2021). Integrated strategies for household food waste Council.
reduction in Bangkok. Sustain. For. 13:7651. doi: 10.3390/su13147651 Janssens, K., Lambrechts, W., van Osch, A., and Semeijn, J. (2019). How consumer 

Bux, C. (2024). Conventional and digital technologies for measuring and monitoring behavior in daily food provisioning affects food waste at household level in the 
food waste in the healthcare foodservice. J. Foodserv. Bus. Res. 12, 1–23. doi: Netherlands. Food Secur. 8:428. doi: 10.3390/foods8100428
10.1080/15378020.2024.2394730 Kaza, S., Yao, L., Bhada-Tata, P., and Van Woerden, F. (2018). What a waste 2.0: Urban 

Bux, C., and Amicarelli, V. (2024). “Blockchain technology and material flow analysis development. New York, NY: World Bank Publications.
to track food waste and enhance food security and sustainability” in Fintech and green Kitro (2024). Available at: https://www.kitro.ch/
investment: Transforming challenges into opportunities. eds. C. Nguyen, K. Hoang and 
C. Gan (London: World Scientific Publishing Europe Ltd.), 79–105. Kummu, M., De Moel, H., Porkka, M., Siebert, S., Varis, O., and Ward, P. J. (2012). 

Lost food wasted resources: global food supply chain losses and their impacts on 
Creswell, J. W., and Poth, C. N. (2016). Qualitative inquiry and research design: freshwater, cropland, and fertiliser use. Sci. Total Environ. 438, 477–489. doi: 10.1016/j.

Choosing among five approaches. London: Sage. scitotenv.2012.08.092
Dhir, A., Talwar, S., Kaur, P., and Malibari, A. (2020). Food waste in hospitality and Marvin, H. J., Bouzembrak, Y., Van der Fels-Klerx, H. J., Kempenaar, C., Veerkamp, R., 

food services: a systematic literature review and framework development approach. J. Chauhan, A., et al. (2022). Digitalisation and artificial intelligence for sustainable food 
Clean. Prod. 270:122861. doi: 10.1016/j.jclepro.2020.122861 systems. Trends Food Sci. Technol. 120, 344–348. doi: 10.1016/j.tifs.2022.01.020

Frontiers in Artificial Intelligence 13 frontiersin.org



Clark et al. 10.3389/frai.2024.1429477

Moser, S. C. (2016). Reflections on climate change communication research and Roodhuyzen, D. M. A., Luning, P. A., Fogliano, V., and Steenbekkers, L. P. A. (2017). 
practice in the second decade of the 21st century: what more is there to say? Wiley Putting together the puzzle of consumer food waste: towards an integral perspective. 
Interdiscip. Rev. Clim. Chang. 7, 345–369. doi: 10.1002/wcc.403 Trends Food Sci. Technol. 68, 37–50. doi: 10.1016/j.tifs.2017.07.009

Nu, Y., Belavina, E., and Girotra, K. (2024). Using artificial intelligence to reduce food Stancu, V., Haugaard, P., and Lähteenmäki, L. (2016). Determinants of consumer food 
waste. SSRN 31:4826777. doi: 10.2139/ssrn.4826777 waste behaviour: two routes to food waste. Appetite 96, 7–17. doi: 10.1016/j.appet.2015.08.025

Nunkoo, R., Bhadain, M., and Baboo, S. (2021). Household food waste: attitudes, Sustainable Management of Food Basic (2023). United  States Environmental 
barriers and motivations. Br. Food J. 123, 2016–2035. doi: 10.1108/bfj-03-2020-0195 Protection Agency (EPA). Available at: https://www.epa.gov/sustainable-management-

Olio. (2024). Olio - Your local sharing app. Available at: https://olioapp.com/en/ food/sustainable-management-food-basics (Accessed May 1, 2024).

Onyeaka, H., Tamasiga, P., Nwauzoma, U. M., Miri, T., Juliet, U. C., Nwaiwu, O., et al. Teng, C. C., Chih, C., Yang, W. J., and Chien, C. H. (2021). Determinants and 
(2023). Using artificial intelligence to tackle food waste and enhance the circular prevention strategies for household food waste: an exploratory study in Taiwan. Food 
economy: maximising resource efficiency and minimising environmental impact: a Secur. 10:2331. doi: 10.3390/foods10102331
review. Sustain. For. 15:10482. doi: 10.3390/su151310482 Thaler, R., and Sunstein, C. (2008). Nudge: improving decisions about health, wealth 

Papargyropoulou, E., Lozano, R., Steinberger, J. K., Wright, N., and Ujang, Z. and happiness. Amsterdam Law Forum 293, 356–360. doi: 10.1007/s10602-008-9056-2
(2014). The food waste hierarchy as a framework for the management of food The Food Waste Blog (2024). Available at: https://blog.winnowsolutions.com/
surplus and food waste. J. Clean. Prod. 76, 106–115. doi: 10.1016/j.
jclepro.2014.04.020 Too Good To Go. (2024). Too Good To Go: End Food Waste [Mobile application 

software]. Available at: https://www.toogoodtogo.com/en-us
Papargyropoulou, E., Steinberger, J. K., Wright, N., Lozano, R., Padfield, R., and 

Ujang, Z. (2019). Patterns and causes of food waste in the hospitality and food service United Nations Environment Programme (2021). Food Waste Index Report 2021. 
sector: food waste prevention insights from Malaysia. Sustain. For. 11:6016. doi: 10.3390/ Nairobi: United Nations Environment Programme.
su11216016 van der Werf, P., Seabrook, J. A., and Gilliland, J. A. (2021). Reduce food waste, save 

Parfitt, J., Barthel, M., and Macnaughton, S. (2010). Food waste within food supply money: testing a novel intervention to reduce household food waste. Environ. Behav. 53, 
chains: quantification and potential for change to 2050. Philos. Trans. Royal Soc. B Biol. 151–183. doi: 10.1177/0013916519875180
Sci. 365, 3065–3081. doi: 10.1098/rstb.2010.0126 Van Geffen, L., van Herpen, E., and van Trijp, H. (2020). Household food waste—how 

Parizeau, K., Von Massow, M., and Martin, R. (2015). Household-level dynamics of to avoid it? An integrative review. Food Waste Manage. Solving Wicked Problem 2020, 
food waste production and related beliefs, attitudes, and behaviors in Guelph, Ontario. 27–55. doi: 10.1007/978-3-030-20561-4_2
Waste Manag. 35, 207–217. doi: 10.1016/j.wasman.2014.09.019 Xue, L., Liu, G., Parfitt, J., Liu, X., Van Herpen, E., Stenmarck, Å., et al. (2017). Missing 

Principato, L., Mattia, G., Di Leo, A., and Pratesi, C. A. (2021). The household wasteful food, missing data? A critical review of global food losses and food waste data. Environ. 
behaviour framework: a systematic review of consumer food waste. Ind. Mark. Manag. Sci. Technol. 51, 6618–6633. doi: 10.1021/acs.est.7b00401
93, 641–649. doi: 10.1016/j.indmarman.2020.07.010 Yin, R. K. (2017). Case study research and applications: Design and methods. London: 

Quested, T. E., Marsh, E., Stunell, D., and Parry, A. D. (2013). Spaghetti soup: the Sage publications.
complex world of food waste behaviours. Resour. Conserv. Recycl. 79, 43–51. doi: Yu, Y., and Jaenicke, E. C. (2020). Estimating food waste as household production 
10.1016/j.resconrec.2013.04.011 inefficiency. Am. J. Agric. Econ. 102, 525–547. doi: 10.1002/ajae.12036

Frontiers in Artificial Intelligence 14 frontiersin.org