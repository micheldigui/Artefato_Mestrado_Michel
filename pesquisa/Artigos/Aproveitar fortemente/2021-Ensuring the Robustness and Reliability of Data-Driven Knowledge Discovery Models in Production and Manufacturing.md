---
source_file: "2021-Ensuring the Robustness and Reliability of Data-Driven Knowledge Discovery Models in Production and Manufacturing.txt"
original_rel_path: "Trabalhos\Artigos\Aproveitar fortemente\txt\2021-Ensuring the Robustness and Reliability of Data-Driven Knowledge Discovery Models in Production and Manufacturing.txt"
category: "Artigos_Aproveitar_fortemente"
extension: ".txt"
sha256: "7ef42781756ee8f6fe7e6012711e21d50be82566e5b5548270406e5912cca143"
extracted_at: "2026-09-19T23:16:59.141669"
---

﻿REVIEW
published: 14 June 2021

doi: 10.3389/frai.2021.576892

Ensuring the Robustness and
Reliability of Data-Driven Knowledge
Discovery Models in Production and
Manufacturing
Shailesh Tripathi 1*, David Muhr1, Manuel Brunner1, Herbert Jodlbauer1,
Matthias Dehmer2,3,4,5 and Frank Emmert-Streib6,7

1Production and Operations Management, University of Applied Sciences Upper Austria, Linz, Austria, 2Department of Computer
Science, Swiss Distance University of Applied Sciences, Brig, Switzerland, 3School of Science, Xian Technological University,
Xian, China, 4Department of Biomedical Computer Science and Mechatronics, UMIT-The Health and Life Science University, Hall
in Tyrol, Austria, 5College of Artificial Intelligence, Nankai University, Tianjin, China, 6Predictive Society and Data Analytics Lab,
Faculty of Information Technology and Communication Sciences, Tampere University, Tampere, Finland, 7Institute of Biosciences
and Medical Technology, Tampere University, Tampere, Finland

The Cross-Industry Standard Process for Data Mining (CRISP-DM) is a widely accepted
framework in production and manufacturing. This data-driven knowledge discovery
framework provides an orderly partition of the often complex data mining processes to
ensure a practical implementation of data analytics and machine learning models.

Edited by: However, the practical application of robust industry-specific data-driven knowledge
Bebeka Gjoksi-Cosandey,

Novartis (Switzerland), Switzerland discovery models faces multiple data- and model development-related issues. These

Reviewed by: issues need to be carefully addressed by allowing a flexible, customized and industry-
Saeed Tabar, specific knowledge discovery framework. For this reason, extensions of CRISP-DM are

Ball State University, United States needed. In this paper, we provide a detailed review of CRISP-DM and summarize
Nakul Parameswar,

Institute of Rural Management Anand, extensions of this model into a novel framework we call Generalized Cross-Industry
India Standard Process for Data Science (GCRISP-DS). This framework is designed to allow

*Correspondence: dynamic interactions between different phases to adequately address data- and model-
Shailesh Tripathi

shailesh.tripathi@fh-steyr.at related issues for achieving robustness. Furthermore, it emphasizes also the need for a
detailed business understanding and the interdependencies with the developed models

Specialty section: and data quality for fulfilling higher business objectives. Overall, such a customizable
This article was submitted to GCRISP-DS framework provides an enhancement for model improvements and reusability

AI in Business,
a section of the journal by minimizing robustness-issues.

Frontiers in Artificial Intelligence
Keywords: machine learning, robustness, industry 4.0, smart manufacturing, industrial production, CRISP- DM

Received: 27 June 2020
Accepted: 12 February 2021

Published: 14 June 2021 INTRODUCTION
Citation:

Tripathi S, Muhr D, Brunner M, Since the beginning of industry 4.0 initiatives, the concept of smart manufacturing has gained
Jodlbauer H, Dehmer M and considerable attention among researchers from academia and industry. Specifically, data-driven

Emmert-Streib F (2021) Ensuring the knowledge discovery models are now regarded as an essential pillar for smart manufacturing. The
Robustness and Reliability of Data-

concept of intelligent manufacturing systems was initially discussed in Refs. (Hatvany and Nemes,
Driven Knowledge Discovery Models in

Production and Manufacturing. 1978; Hatvany and Lettner, 1983), where the authors addressed the prospects of systems and their
Front. Artif. Intell. 4:576892. complexities and emphasized that systems should be built to be resilient to unforeseen situations and

doi: 10.3389/frai.2021.576892 to predict trends in real time for large amounts of data.

Frontiers in Artificial Intelligence | www.frontiersin.org 1 June 2021 | Volume 4 | Article 576892



Tripathi et al. Data-Driven Knowledge Discovery Models

In recent years, the idea of smart manufacturing developed Kusiak (2017) discusses key features of smart manufacturing
further using the framework of multi-agent systems (MASs). and considers predictive engineering as one of the essential pillars
MASs are groups of independent agents that cooperate with of smart manufacturing, and (Stanula et al., 2018) discuss various
each other and are capable of perceiving, communicating, guidelines to follow for data selection for understanding business
reproducing, and working not only toward a common goal and data in manufacturing. Wuest et al. (2014), Wuest et al.
but also toward individual objectives. An agent is composed of (2016) discuss the various challenges encountered in ML
several modules that enable it to work effectively both applications in manufacturing, such as data preprocessing,
individually and collectively. The acting module of a learning sustainability, selection of the appropriate ML algorithm,
agent collects data and information (percepts) from the external interpretation of results, evaluation, complexity, and high
world through sensors and responds through effectors, which dimensionality. The challenges raised by Wuest et al. (2014),
results in actions. The learning module and critical module of an Wuest et al. (2016) requires a systematic and robust
agent react to improve the actions and the performance standards implementation of each phase as defined via the Cross-
by interacting with each other. Furthermore, the problem Industry Standard Process for Data Mining (CRISP-DM)
generator module enforces the exploratory efforts of the agent framework in a manufacturing environment. Kusiak
to develop a more appropriate world view (Russell and Peter, (Kristoffersen et al., 2019) discusses the five key points that
1995; Khalid et al., 1997; Monostori, 2003; Lee and Kim, 2008; highlight the gaps in innovation and obstruct the advancement
Wang et al., 2016). in smart manufacturing and emphasizes that academic research

The learning agent is a software program or an algorithm must collaborate extensively to solve complex industrial
that leads to an optimal solution of a problem. The learning problems. The second point is about new and improved
processes can be classified into three categories: 1) supervised, processes of data collection, processing, regular
2) unsupervised, and 3) reinforcement learning. The learning summarization, and sharing. The third point is to develop
module is a key driver of a learning agent and puts forward a predictive models for outcome prediction. The fourth point
comprehensive automated smart manufacturing process for deals with developing general predictive models to capture
autonomous functioning, collaboration, cooperation, and trends and patterns in the data to overcome future challenges
decision making. The availability and potential of data from instead of memorizing data by feeding in large amounts. The fifth
an integrated business environment allow various business point is to connect factories and processes that work together by
objectives to be formulated, such as automated internal using open interfaces and universal standards. Kusiak
functioning, organizational goals, and social and economic (Kristoffersen et al., 2019) also emphasizes that smart
benefits. Various business analytic methods, metrics, and manufacturing systems should adopt new strategies to measure
machine learning (ML) strategies serve to analyze these useful parameters in manufacturing processes to match up with
business objectives. For instance, Gunther et al. new requirements and standards. The studies discussed above
(Mohammad, 2017) extensively reviewed big data in terms of emphasize the development of ML models and their robustness
their importance for social and economic benefits. so that ML can effectively meet the new manufacturing
Furthermore, they highlighted three main issues of big data challenges. These robustness issues may be attributed to faulty
in order to realize their potential and to match up with the sensors, corrupt data, missing data or data drifting.
ground realities of business functioning (i.e., how to transform The papers discussed above highlight the importance of big
data into information to achieve higher business goals). The data in smart manufacturing and production. These studies
three issues considered are work-practice goals, organizational emphasized various issues related to robust ML prediction
goals, and supra-organizational goals. The availability of big models and guidelines for systematic CRISP-DM model
data allows us to apply various complex ML models to various implementation and achieving business goals utilizing big data.
manufacturing problems that could not be addressed However, these studies addressed these issues largely in isolation
previously. Ross et al. (2013) discussed the big data and did not consider, e.g., systematic implementation of different
obsession of business organizations rather than asking the phases of data and modeling related issues considering CRISP-
straightforward question of whether big data are useful and DM and interactions between a data-driven Knowledge discovery
whether they increase the value of business-related goals. They model framework (CRISP-DM) and machine learning models.
concluded that many business applications might not need big Neither have model transparency issues been considered in
data to add value to business outcomes but instead need to sufficient depth.
address other organizational issues and business rules for The challenges at different phases of CRISP-DM are
evidence-based decision making founded on rather small interrelated for a data-driven model from the beginning of the
data. However, their paper does not discuss manufacturing business understanding that formulates business hypotheses and
and production but instead focuses on issues related to goals to the data understanding and preparation, modeling and
business management. Nevertheless, a similar understanding model deployment that validates the business hypotheses. It is
may be obtained in many other production- and required that the business goals and data-characteristics, models’
manufacturing-related instances that do not require big attributes and characteristics and users’ understanding must be
production data but instead require sufficient samples of quantitatively or qualitatively recorded and evaluated. Each phase
observational or experimental data to support robust data of CRISP-DM shows sensitivity towards internal parameters and
analytics and predictive models. the external parameters (that is caused by the other phases).

Frontiers in Artificial Intelligence | www.frontiersin.org 2 June 2021 | Volume 4 | Article 576892



Tripathi et al. Data-Driven Knowledge Discovery Models

Therefore a robust CRISP-DM must consider the hypothesis, is an endeavor to provide a general framework that is
which tests the influence between phases, i.e., independent of any given industry and of applications that

∣ execute data mining methods that look at different stages of a
H0 : ρ(a, b|B,Dx,Ma,Mb,Ux,Ti)  ρ(a, b∣∣∣∣B,Dy,Ma,Mb,Uy,Tj) business (Shearer, 2000). Briefly, CRISP-DM divides the data
H1 : ρ(a, b|B,Dx,Ma,Mb,Ux,Ti)≠ ρ(a, b∣∣∣B,Dy,Ma,Mb,Uy ,Tj) mining-related knowledge discovery process into six phases: 1)

(1) business understanding, 2) data understanding, 3) data
preparation, 4) modeling, 5) evaluation and 6) deployment.

Here, ρ(a,b) measures the influence between two phases of The different phases of CRISP-DM and the underlying
CRISP-DM a to b, B is a business goal, Dx and Dy are the two associated tasks are shown in Table 1. The added third
different data-sets at timepoint Ti and Tj, Ma and Mb are the column provides a brief description of the literature, which
methods applied for a and b, Ux and Uy are two sets of users, explicitly reviews the challenges of the corresponding
developers and business experts. The hypothesis provides a component related to industrial production and Big Data.
mathematical framework for a robust implementation of In Figure 1, we show a schematic overview of the standard
different phases of CRISP-DM to ensure the update of CRISP-DM framework. The edges are the interactions on
different phases if the null hypotheses is invalidated. between different phases of CRISP-DM. For example, the

Instead, in this paper considering the null hypothesis in Eq. 1, modeling phase depends on data preparation and vice versa.
we discuss the interrelation of the Knowledge Discovery and When the data preparation phase is complete, the next step is the
Data Mining (KDD) framework for developing ML models modeling phase for which different candidate models with
and the transparency issues because a KDD model (Cios et al., different assumptions about the data are proposed. To meet
2012) which does not address various levels of details of business the data requirements for model building, data experts might
and data understanding for the development of ML models step back to the data preparation phase and apply various data
will be serving as an ad-hoc model, which can not be useful in preprocessing methods. Similarly, in another example, the data
fulfilling higher business objectives and decision making in the acquisition and data preprocessing steps are done by data experts
long term. so that business goals can be achieved with the available data.

In this paper, we review the general CRISP-DM framework Business experts and data experts can agree to obtain the data
and discuss extensions thereof. A special focus of attention is through a specific experimental design or by acquiring new
placed on robustness-issues of ML and AI models for data from observational data.
manufacturing and production within this framework, which is Importantly, business goals may need to be readjusted based
strongly related to model assessment. Furthermore, we on an understanding acquired during the data preparation and
emphasize the interplay between three parties, i.e., data data understanding phases. The readjustment of business goals
experts, business experts and users, after deployment of a may imply the required time, cost, data quality and the usefulness
model. This human-centered aspect requires additional of the business plan. Once the data experts and business experts
measures, e.g., for model transparency and model security agree on data issues, the data analysis process moves forward to
frequently overlooked. model development and evaluation. Similarly, also these phases

The paper is organized as follows. In the next section, we require the cooperation between different groups. Overall, the
discuss the CRISP-DM framework in detail and suggested standard CRISP-DM describes a cyclic process, which has
extensions. In order to simplify this discussion we will recently been highlighted as the emergent feature of data
introduce a summarization of such a model we call science (Emmert-Streib et al., 2016). In contrast, ML or
Generalized Cross-Industry Standard Process for Data Science statistics focus traditionally on a single method for the analysis
(GCRISP-DS). Next, we discuss the meaning of a human- of data. Thus, the CRISP-DM framework follows a general data
centered data science and its role as a safety system. Finally, science approach.
we discuss the problem of model assessment and data-related In Figure 2, we highlight two types of CRISP-DM models:
robustness issues of machine learning models which are critical general extensions (aka concept-based extensions) and
for successful project implementations. This paper finishes with a industry- (or application) specific extensions. For the circular
discussion and conclusions. economy, KDD and CRISP-DM are the concept-based

evolution of the CRISP-DM model. However, Data Mining
Methodology for Engineering (DMME) and CRISP-DM for

CROSS-INDUSTRY STANDARD PROCESS stream analytics are application-specific customizations of the
FOR DATA MINING AND EXTENSIONS basic model. Given the new industrial trends, concept-based

evolution has become a generalized extension of CRISP-DM.
The Cross-Industry Standard Process for Data Mining (CRISP- For example, the circular economy is a growing trend in the
DM) framework was introduced in 1996. Its goal is to provide a industry for lifelong services, product upgrades, and product
systematic and general approach for applying data mining recycling for sustainable and environmentally conscious
concepts to analyze industrial operations and gain in-depth manufacturing (Walter, 2016). Hence, all business sectors
insights into business processes (Shearer, 2000). It is a widely should gradually adopt the circular economy concept.
accepted framework for industrial data mining and data analytics Therefore, a knowledge discovery model must adopt concept-
for data-driven knowledge discovery. The CRISP-DM framework related extensions of the CRISP-DM framework.

Frontiers in Artificial Intelligence | www.frontiersin.org 3 June 2021 | Volume 4 | Article 576892



Tripathi et al. Data-Driven Knowledge Discovery Models

TABLE 1 | Different components of CRISP-DM model and the associated tasks.

CRISP Components Tasks Literature and Description

Business understanidng –Define business objectives In Sharma and Osei-Bryson (2009) a framework for implementing various
– Risk Assessment analysis business understanding tasks is presented and highlights dependencies between
–Cost and benefit analysis them. In Sharma and Osei-Bryson (2008); Rao et al. (2012) an organizational-
–Technical requirement analysis ontology for business understanding is presented. In Nino et al. (2015) various
– Define data analysis objectives and project planning aspects of business understanding and challenges related to big data are

discussed
Data understanding and – Data extraction In Duch et al. (2004) rule-based data extraction and understanding is discussed.
preparation – Data description Uddin et al. (2014) discuss various characteristics of big data for its efficient

– Data quality estimation applications. Karkouch et al. (2016); Qin et al. (2016) discuss data properties, life-
– Data selection for modeling cycle of data from internet of things (IoT) for maintaining data quality from IoT.
Data cleaning and feature extraction Cichy and Rass (2019) reviews various comparisons that provide data quality
– Data exploration frameworks from different areas, including industrial production. Hazen et al.

(2014); Ardagna et al. (2018) discuss methods for data quality management,
monitoring, and assessments. Steed et al. (2017); Zhou et al. (2019); Andrienko
et al. (2020)) discuss visualization methods and challenges of manufacturing and
big data. Stanula et al. (2018)) discuss guidelines for data selection for
understanding business and data in manufacturing

Modeling and evaluation – Model assumption and selection techniques for In Diez-Olivan et al. (2019), Vogl et al. (2019), Bertsimas and Kallus (2020) reviews
modeling, parameter selection of various models, models building and evaluation for descriptive, diagnostic,
– Feature engineering predictive, and prescriptive analysis in industrial production andmanufacturing are
– Model testing, result visualization and analysis presented
– Model evaluation and description
– Other data and modeling issues affecting model
performance

Deployment – Model utility assessment Issues of model deployment related to human-lefted data science and model
– Model monitoring, maintenance and updates safety are discussed in HUMAN-CENTERED Data Science and Model Safety
– Users response evaluation
– Model evaluation for data understanding and business
understanding

FIGURE 1 | The CRISP-DM framework describes a cyclic process of a data analysis project.

It is important to note that the standard CRISP-DM and other big data characteristics play key roles for determining
framework developed in 1990s did not envisage the big data the efficiency of data mining and ML models. Therefore the
evolution and futuristic applications of data-driven models for standard model suffers from a number of limitations and various
automated decision making where the data dimensions, speed required extensions of CRISP-DM and data mining algorithms,

Frontiers in Artificial Intelligence | www.frontiersin.org 4 June 2021 | Volume 4 | Article 576892



Tripathi et al. Data-Driven Knowledge Discovery Models

FIGURE 2 | Classification of the CRISP-DM framework into two categories: general extensions and industry-specific extensions.

TABLE 2 | List of extensions of the CRISP-DM process model framework based on industry-specific requirements (application-specific requirements) due to changing
business trends.

Model Description Application

DMME (Huber et al., 2019) Adds two new phases between business understanding and Engineering applications
data understanding and one phase between model
evaluation and deployment

KDDS with big data (Grady, 2016) Adding various new activities, especially to handle big data A proposed framework as a need for the current scenario in
big data and data science applications

CRISP-DM extension for stream analytics Data preparation and data modeling stage to be redefined Healthcare application
(Kalgotra and Sharda, 2016) for multidimensional and time-variant data, where the IoT

system sends multiple signals over time
CRISP-DM extension in context of circular Adds a data validation phase and new interactions between Aligning business analytics with the circular economy goals
economy (Kristoffersen et al., 2019) different phases
Context-aware standard process for data The deployment context of the model can differ from the Robust and systematic reuse of data transformation and ML
mining (CASP-DM) (Martínez-Plumed et al., training context. Therefore, for context-aware ML models models if the context changes
2017) and model evaluation, new activities and tasks are added at

different phases of CRISP-DM.
APREP-DM (Nagashima and Kato, 2019) Extended framework for handling outliers, missing data, and General extension for automated preprocessing of sensor

data preprocessing at the data-understanding phase data
QM-CRISP-DM (Schäfer et al., 2018) CRISP-DM extension for the purpose of quality management Adding quality management tools in each phase of CRISP-DM

considering DMIAC cycle framework validated in the real-world electronic production
process

ASUM-DM (Haffar, 2015) IBM-SPSS initiative for the practical implementation of General framework that allows comprehensive, scalable,
the CRISP-DM framework, which combines traditional and product-specific implementation
and agile principals. It implements existing CRSIP-DM
phases and adds additional operational, deployment, and
project-management phases

A variability-aware design approach for Extends the structural framework to capture the variability of General framework which considers model and data
CRISP-DM (Vale Tavares et al., 2018) data modeling and analysis phase as feature models for variability for the improved automation of data analysis

more flexible implementation of data process models

models, and techniques were developed over the years to achieve deployment phases). The DMME model also draws new
robustness in advanced automated decision-making processes interactions between different phases, e.g., between evaluation
(Liu et al., 2018). and technical understanding, between data understanding and

A recent example of such an expansion is the Data Mining technical understanding, and between technical understanding
Methodology for Engineering applications (DMME) (Huber et al., and technical realization. Furthermore, this model also
2019) model, which is an extension of the CRISP-DM model for emphasizes the cooperation between specialized goals for the
engineering applications. This model adds three further phases, refinement of the framework.
namely, technical understanding, technical realization (which sits Similarly, in light of big data, technical advancements, broader
between business understanding and data understanding), and business objectives, and advanced data science models, Grady
technical implementation (which sits between the evaluation and (Leslie, 1978) discussed the need for a new and improved

Frontiers in Artificial Intelligence | www.frontiersin.org 5 June 2021 | Volume 4 | Article 576892



Tripathi et al. Data-Driven Knowledge Discovery Models

FIGURE 3 | Generalized Cross-Industry Standard Process for Data Science (GCRISP-DS). This framework is designed to allow dynamic interactions between
different phases to adequately address data- and model-related issues for achieving robustness.

framework. The author coined the term Knowledge Discovery in would be an adaptation to the companies’ business environment
Data Science (KDDS) and discussed different aspects of KDDS, and solutions. We want to emphasize three main points for active
such as KDDS phases, KDDS process models, and KDDS collaboration between all possible interactions between phases:
activities. Grady emphasized that this approach establishes a
new and improved framework, which he calls the Cross- Evaluate requirements of extensions of existing phases,
Industry Standard Process model for Data Science (CRISP- activities and attributes depending on technical and other
DS). Table 2 lists further extensions of the CRISP-DM model. business specific needs for adopting industrial application-
These models show that the basic CRISP-DM framework cannot specific requirements or general changes in the economy or
satisfy the variety of data mining requirements from different manufacturing.
sectors. Ensure the models’ utility and robustness with respect to

In general, the extensions of CRISP-DM shown in the Table 2 external changes in the business processes, data quality and
extend the standard framework to fulfill specific requirements. business understanding.
Various expansions add new phases or new attributes or activities Ensure the model transparency, explainability and reusability
on the existing phases. Subsequently, this added new interactions for newer business understanding by considering users’
between CRISP-DM phases as well as new proposed phases. response to the deployed model.
Summarizing all these extensions into one coherent framework
one obtains a fully connected CRISP network as a generalized
abstract framework of the various steps constituting a systematic HUMAN-CENTERED DATA SCIENCE AND
analysis and knowledge discovery. This extension is shown in MODEL SAFETY
Figure 3 and we call this theGeneralized Cross-Industry Standard
Process for Data Science (GCRISP-DS). The new wave of AI and ML solutions aims to replace human-

In Figure 3, the orange edges are from the traditional CRISP- related tasks and decision making processes by automated
DM whereas the green ones are newly added layers of complexity methods. This raises concerns regarding responsible and
and interactions. The fully connected GCRISP-DS raises new ethical ML and AI models that do not underestimate human
questions about how these edges are useful and what new interests and do not incorporate social and cultural bias. ML
information they contributes? In our understanding the six systems have, until now, primarily focused on applying cost-
basic phases of CRISP-DM must be interacting actively which effective automations that are useful for business organizations,
means that the business experts, data experts and data scientists but such automations are so far not part of complex decision
actively collaborate to evaluate business problems and the data- making processes. However, in the future, autonomous systems
driven solutions. Therefore, the active collaboration would ensure could take over for many crucial decision making processes. One
if a new phase or interaction is required between existing phases example of such an automation are self-driving cars. Many large
or a new attribute to be added in different phases. Also, it should car manufacturing companies have announced the launch of self-
ensure how effectively the interactions should stay between driving cars, but the acceptability and use of such vehicles is a
phases. Thus, with active collaborations one can draw a new major challenge (Urmson andWhittaker, 2008; Howard and Dai,
specific subclass of a GCRISP-DS. The new specific model 2014). (Kaur and Rampersad, 2018) quantitatively analyzed the
(subclass or extended subclass of fully connected GCRISP-DS) acceptance of technology that addresses human concerns. Their

Frontiers in Artificial Intelligence | www.frontiersin.org 6 June 2021 | Volume 4 | Article 576892



Tripathi et al. Data-Driven Knowledge Discovery Models

study analyzed the public response to this issues, which include have different characteristics and capabilities. A ML model
security, reliability, performance expectancy, trust or safety, and makes decisions based on a narrow data-related view with no
adoption scenarios. or limited contextual understanding. The AI-ML models cannot

Similarly, such cases can be discussed for industrial be held responsible for their decisions. However, they can
production and manufacturing problems when a self- produce results rationally and logically based on the data
automated system or a self-functioning machine based on AI used to train them. Interactions between humans and
or ML decides various production and manufacturing tasks. In machines are possible in two ways: The first way involves the
these cases, how a system would function in complex scenarios model developer and ML models, where the training of models
would be a question, both ethical and technical. This type of are the responsibility of data experts and business experts. They
autonomy can affect the complex production process of PPCSs should train models with a diverse range of data with no bias
estimation, which might, in adversarial cases, influence the and no breach of data ethics. The second way is between model
robustness and stability of PPCSs, predictive maintenance, and users and MLmodels. The results predicted by models empower
other production processes (Oliveira et al., 2019). Another future and assist humans to make decisions regarding simple to
question one can ask is, what should be done with an automated complex tasks. Figure 4A shows a schematic view of human-
system after it is deployed? Should it be left with no human machine interactions. In this figure, we highlight various
intervention, should it always supersede human understanding, characteristics of human and ML models and how effective
and how can humans and AI systems cooperate effectively? interactions between humans and ML models complement and

In industrial production cases, human-centered data science empower human decision making and further improves the
issues can be seen from the following perspectives: capacity of models to make fair analyses.

Further extending the human-machine interaction concept,
• What is the role of human-centered ML and data science we now discuss the industrial-production framework shown in
processes in decision making related to work goals, business Figure 4B. This highlights a CRISP-DM process in the
goals and societal goals? deployment phase of the model. The deployed model should

• Can production processes be completely automated with no have proven its utility and allow transparency so that the user
involvement of humans by AI agents with human-like can understand the models’ prediction and trust the results.
intelligence? Importantly, the deployed model interacts with data experts,

• The emergence of complexity when a series of tasks is business experts, and actual users. In an industrial production
automated and integrated: Can an AI or ML system process, the users are technical operators or machine handlers.
exhibit the higher level of intelligence required for These interactions have different meanings for different users.
independent and integrated decision making? Data experts interact with the model to improve the prediction

accuracy and model performance. They provide contextual
When industrial production processes are completed by a meaning to the results predicted by the model and train it

combination of humans and ML agents: How can humans and further for contextual learning. The data experts also explore
ML agents interact effectively for integrated analysis and decision the reusability of a model for other cases (Pan and Yang, 2010).
making? Business experts should test these results against their

The first point mentioned here is still in its infancy and awaits understanding of larger business goals and should explain
the future of integrating complex data mining and ML processes. the business context based on model results. Furthermore,
The future design of data science modeling of complex data and the results should allow the model to be reused and
business goals is beyond the scope of this paper. However, a adaptable to changes in production and manufacturing
fundamental question that remains relevant is how can large- scenarios.
scale automation led by AI andMLmodels impact humans? At its In production and manufacturing, data-driven knowledge
core, this question probes how AI can efficiently serve, empower, processes must adopt human-centered concerns in data
and facilitate human understanding and decision making tasks analytics and ML models; the human-machine interaction
and provide deeper insight into the solutions to these complex must not fizzle out after the deployment of the model
problems. This question also leads to the second and third points; (Amershi et al., 2014). The model should remain interactive
namely, should we leave the decisionmaking entirely in the hands with its users and be allowed to evolve and update itself.
of AI-ML models? In other words, can a machine decide by itself Other characteristics of the deployed models are its
what is right or wrong for humans? Complete automation would transparency and performance in adversarial cases. Model
lead to the emergence of many complex aspects of the production transparency should enable users to access various model
process, and dealing with such complexity would be the future features and evaluate the predicted results. Additionally, the
challenge of research into production andmanufacturing. In such human-machine interaction must be aware of the surrounding
complex cases, the role of humans should be to interact and environment so that the model can adapt to environmental
collaborate with the automated systems. They should use changes, as required for intelligent learning of ML models.
intelligent models for decision making and have the wisdom Continuous interactions between humans and machines
to override machine decisions if required for ensuring safety. improve the generality of the model by incremental learning

Importantly, there is a difference between a human and updating of the model so that it gives robust and stable
perspective and statistical learning perspective because both responses and can be adaptive to changes.

Frontiers in Artificial Intelligence | www.frontiersin.org 7 June 2021 | Volume 4 | Article 576892



Tripathi et al. Data-Driven Knowledge Discovery Models

FIGURE 4 | (A) Schematic view of interactions between humans and AI andML agents. (B) Schematic view of post-deployment of MLmodel not left in isolation but
continuously updating and addressing human concerns by allowing human interactions to ensure a human-centered data science.

MODEL ASSESSMENT prognostic analysis in manufacturing and highlight the
challenges faced by the prognostic health management system

For the remainder of this paper, we focus on two interrelated in the current scenario of automated maintenance.
aspects of GCRISP-DS or CRISP-DM, namely, model assessment Figure 5A shows a schematic view of the division of data
and model robustness. While all phases and interactions are analysis problems. The divisions are useful to understand the
important the effect of improper models or lack of robustness nature of the problem and the methods that are applicable to the
may lead to the most devastating problems of the analysis problem.
pipeline. For this reason, we discuss model assessment and Leek and Peng (2015) emphasizes that, even if the statistical
model robustness issues in detail to emphasize their results are correct, data analysis can be wrong because the wrong
importance. With respect to Figures 1 and 3 these correspond questions are asked. One must be aware of such a situation in an
to the internal structure of the corresponding phase nodes. industrial framework and should select the right approach for the

Model building and evaluation in CRISP-DM are two phases analysis. He further divides data analysis into six categories (see
in which data are 1) searched for patterns and 2) analyzed. These Figure 6). This chart is useful for the basic understanding of data
models are divided into four classes: descriptive, diagnostic, analysis for business experts and data experts, which helps prevent
predictive, and prescriptive (Bertsimas and Kallus, 2020). The knowledge discovery from diverging from the real objective.
primary goal of these models is pattern recognition, machine- The business understanding and the later data modeling
health management, condition-based maintenance, predictive approaches for solving the type of problem shown in
maintenance, production scheduling, life-cycle optimization, Figure 5A requires a systematic interaction between data
and supply-chain management prediction. Alberto et al. (Diez- experts and business experts. Such communication is possible
Olivan et al., 2019) provide a comprehensive review of various only when the data experts and business experts are aware of each
methods applied in manufacturing and production with other and agree with each other. Therefore, they need to address
representative studies of descriptive, predictive, and prescriptive the data- and model-related communication in the context of
models of various industrial sectors, including manufacturing. business understanding. Hicks and Peng, (2019) discuss the
Vogl et al. (2019) review current practices for diagnostic and vocabulary required to convey the accurate meaning of the

Frontiers in Artificial Intelligence | www.frontiersin.org 8 June 2021 | Volume 4 | Article 576892



Tripathi et al. Data-Driven Knowledge Discovery Models

A

B

FIGURE 5 | (A) Components of data analytics problems. (B) Model assessment.

data analysis. Additionally, They describe the six principles of learning methods. Akaike information criterion (AIC),
data analysis: Data matching, Exhaustive, Skeptical, Second Bayesian information criterion (BIC), cross-validation error,
order, Transparent, and Reproducible. These six principles are and probabilistic model selection are some of the approaches
applicable to an industrial framework to communicate the results used to select less complex models. In (Emmert-Streib and
of the data analysis. A clear understanding of these principles Dehmer, 2019b) key statistical characteristics for systematically
helps business experts and data experts develop robust models for evaluating regression models are discussed with respect to model-
data-driven knowledge discovery. Data- and model-related issues complexity for selecting the best model. Model interpretation is
are not restricted only to understanding business and data; the another crucial issue in data-driven knowledge discovery with
most crucial part is model assessment, which requires accurate ML models. In general, monotonically increasing functions
nonambiguous model selection, interpretability, and (linear and nonlinear), such as additive models, sparse linear
transparency. Model assessment depends on various issues, models, and decision trees, are regarded as interpretable models,
namely, model accuracy, model multiplicity, model whereas nonlinear and nonmonotonic functions have higher
interpretability, and model transparency (see schematic complexity and thus a lower interpretability (Ribeiro et al.,
diagram in Figure 5B), and various strategies can be applied 2016a; Hall and Gill, 2018). (Doshi-Velez and Kim, 2017)
to obtain the best model assessment. Model assessment requires provides a theoretical framework for the interpretability of
an agreement between data and business experts, so all four models by defining three classes for evaluating interpretability:
components of model assessment shown in Figure 5B should be The first class is application-grounded evaluation, where the
addressed properly. The first part is the model accuracy; Raschka, domain experts evaluate the model with real tasks. Next,
(1811) reviews model evaluation, selection, and ML model human-grounded evaluation allows a model to be tested with
selection for various ML methods, and Palacio-Niño and simplified tasks without a specific end-goal. The third class is
Berzal (Berzal, 2019) review the evaluation of unsupervised functionally grounded evaluation, which uses a predefined

Frontiers in Artificial Intelligence | www.frontiersin.org 9 June 2021 | Volume 4 | Article 576892



Tripathi et al. Data-Driven Knowledge Discovery Models

FIGURE 6 | Schematic diagram showing data analytics process. Connections are shown between the individual analysis steps that constitute the whole project
Lee et al., 2019.

definition of interpretability of a model as proxy and optimizes analysis. Local interpretable model-agnostic explanations
the candidate models. In an industrial setup, most of the model (Ribeiro et al., 2016b) explain a model locally by constructing
evaluations involve functionally grounded evaluation. a local binary classifier of a regularized linear model by using
Application- and human-grounded evaluation requires more simulated or perturbed input data to explain an instance
resources and could be expensive and time consuming. predicted by the black-box machine learning model.
Functionally grounded evaluation can be useful for learning if Another issue with model assessment is the multiplicity of
the selection of proxy models is based on factors that are relevant models; such cases are known as the “Rashomon” effect
to real-world applications. (Breiman, 2001), whereby multiple predictive models make

Model agnostic interpretability is another approach for predictions with competing accuracy of the same target
interpreting ML models. In this approach, a model is treated variable. In such cases, one should not come to a conclusion
as a black box, and the model is analyzed by entering perturbed about the validity of a prediction in terms of its explanatory
input data and analyzing the respective output (Ribeiro et al., variables from one or a few models until the hypothesis of model
2016a). The model agnostic approach allows the application of a multiplicity is invalidated. In industrial scenarios, the Rashomon
wide range of black-boxMLmodels as interpretable for predictive effect can occur when we have multiple models with competing

Frontiers in Artificial Intelligence | www.frontiersin.org 10 June 2021 | Volume 4 | Article 576892



Tripathi et al. Data-Driven Knowledge Discovery Models

accuracy; one can then choose a narrative to interpret the results resilient and self-correcting, and ultimately ensures steady and
based on the selected model. Such interpretations can differ for flexible models.
different models and would impact the business objective or
business understanding. Fisher et al. (2018) proposes the model
class reliance, which is a measure of a set of variables of a model ROBUSTNESS ISSUES OF ML AND AI
that show high predictive accuracy. Marx et al. (Charles et al., MODELS
2019) propose the ambiguity and discrepancy measures to
evaluate the multiplicity problem in classification models. In In the following, we discuss data-related issues for robust data
this approach, models are selected from a set of “good” analytics because the shortcomings of data reflect on model
models, which maximizes the discrepancy compared to a evaluation and on the deployment phase in terms of
proposed baseline model. To select a model with simplicity underperformance and biased predictions of real-world
and accuracy, Semenova and Rudin (2019) propose the problems.
Rashomon ratio measure, which is a ratio of competing
models in hypothesis space. Experimental Design and Sample Size

In a business scenario, when manufacturing becomes In data-driven process optimization, the data may be
increasingly complex and integrated, data-driven models are observational data or experimental data. Experimental data are
useful to make informed decisions and automate functioning, used to test the underlying hypothesis to build an understanding
which allows for efficient and cost-effective production. Even for and to optimize the response variable by controlling or modifying
a model with high accuracy, user trust is always a crucial various combinations of input parameters. In manufacturing, the
consideration for the deployment of a model. In such cases, experimental designs mostly focus on optimizing various
transparency is always a matter of concern and should be parameters for quality control. The experimental design is a
addressed with simple explanations. Trust issues arise because key criterion for determining whether a model employs all the
of data-source uncertainty, the performance of deployed models, right answers to be understood in ML-based analysis and
and user belief in the model output. This uncertainty can seep manufacturing optimization. The production process is
into the whole process of data mining, from data preprocessing to controlled by setting various process variables, which, during
model building, and thus impacts the entire business-intelligence production, are monitored for changes. In an experimental
process. Sacha et al. (2015) provide a framework to address design, we monitor certain process variables by controlling
human-machine trust issues that are caused by uncertainties other variables to understand how they affect product quality.
propagated in data processing, model building, and visual The one-factor approach is common and involves repeating
analytics. The proposed framework to deal with the experiments with the factors changed between each
uncertainty is divided into two parts: The first part is the experiment until the effect of all factors is recorded. However,
system-related uncertainty and emphasizes handling machine this one-factor approach is time consuming and expensive. For a
uncertainty by quantifying uncertainty in data processing and robust experimental design, Taguchi proposed a methodology
model building, aggregation of total uncertainty at different that uses orthogonal arrays, signal-to-noise ratios, and the
phases of data analysis, and interactive exploration of appropriate combination of factors to study the entire
uncertainty through visual and other means. The second part parameter space through a limited number of experiments
involves human factors that emphasize transparency, which (Taguchi and Konishi, 1987; Taguchi et al., 1989; Unal and
allows system functions to access experts and users for review Dean, 1991; Chang and Faison, 2001). An optimal
and to explore uncertainty, thus building an awareness of the experimental design is a useful strategy that stands between
emerging uncertainty—and additionally tracking human business and data understanding. This approach also benefits
behavior, which is also useful to estimate human bias and how model robustness in the evaluation phase in the CRISP-DM
it impacts human-machine interactions. framework. The active interaction between business

Data transparency and model transparency should ensure that understanding and data understanding serves to solve the
the entire process is explainable to business experts and users. It optimal sample-size issue and prevent an under-powered
should also be secure from external attacks, which allows models analysis.
to be deployed for making business decisions, for user control,
and for social acceptance of intelligent systems Weller, 2017; Model Complexity
Springer, 2019. Emmert-Streib et al. (2020b) featured that the AI The complexity of predictive models is sensitive to the prediction
models help analyze data but not establish a scientific-theory of of testing data. Any complex model can lead to overfitting,
the system that provides the data. Therefore, methods like deep whereas simpler models lead to prediction bias. This property
learning should not be applied as a first choice for the tasks where of predictive models is known as “bias-variance trade-off.”
requirements for explainable models are essential. However, these Complexity in the model could lead to robustness issues, such
models should be utilized for comparison with the other nearest as large testing error or the wrong interpretation of model
explainable models for evaluation. Weller (2017) discusses eight parameters. In some cases, if future data contain a lower
types of transparency rules for developers, business experts, and signal-to-noise ratio, large prediction error may occur. This
users to help them understand the existing system functioning. problem can arise because of a large number of correlated
Transparency allows a large and complex system to be robust and features or through feature engineering, where we create a

Frontiers in Artificial Intelligence | www.frontiersin.org 11 June 2021 | Volume 4 | Article 576892



Tripathi et al. Data-Driven Knowledge Discovery Models

large number of redundant features with high correlation or when recommended to evaluate models, such as the probabilistic
we try to fit a high-degree polynomial model in our data set. thresholding model (Su and Hsiao, 2007), adjusted F measure

Vapnik Chervonenk (VC) dimension (Vapnik and (Maratea et al., 2014), Matthews correlation coefficient
Chervonenkis, 1971) is a quantitative measure for measuring (Matthews, 1975), and AUC/ROC. The imbalance is critical to
the complexity of models and is used to estimate the testing error model building and evaluation problems in the CRISP-DM
in terms of model complexity. A model is selected based on the framework.
best performance with testing data and, as the complexity
increases, the optimized training error decreases and the Data Dimensionality
expected testing error first increases, then decreases, and then In ML and data mining, high-dimensional data contain a large
increases again. The training error and VC are used to calculate number of features (dimensions), so the requirement of optimal
the upper bound of the testing error. This method is called samples increases exponentially. Therefore, a high-dimensional
“structural risk minimization” and is a model that minimizes dataset is sparse (p≫n). In modern manufacturing, the
the upper bounds for the risk. Regularization (Tibshirani, 1996; complexity of the manufacturing processes is continuously
Chang and Faison, 2001; Yuan and Lin, 2006; Emmert-Streib and increasing, which also increases the dimensionality of process
Dehmer, 2019c) and feature-selection methods (both wrapper- variables that need to be monitored. Wuest et al. (2014) discuss
and filter-based) (Maldonado and Weber, 2009; Ko et al., 2017) manufacturing efficiency and product quality by considering the
are the useful strategies of variable selection to keep model complexities and high dimensionality of manufacturing
complexity in check by minimizing bias and variance. programs. High-dimensional data are a challenge for model
Hoffmann et al. (2015) propose a sparse partial robust M robustness, outlier detection (Arthur et al., 2012), time, and
regression method, which is a useful approach for regression algorithmic complexity in ML. These higher-dimensional data
models to remove variables that are important due to the outlier require changes in existing methods or the development of new
behavior in the data. The model complexity affects the modeling methods for such sparse data. One approach is to use a
and model evaluation, such as model description, robustness, and dimensionality-reduction strategy such as a principal
parameter settings in the CRISP-DM framework. component analysis (Subasi and Ismail Gursoy, 2010) and use

the principal components for ML methods. Such a strategy also
Class Imbalance requires a careful examination because of information loss when
In production and manufacturing data, class imbalance is a data are projected onto lower dimensions. Similarly, another
common phenomenon. One such example is vibration data strategy is feature selection, where the most important feature
from cold testing of engines: all manufactured engines go variables are found and we remove the redundant features from
through cold testing, and the technical expert tries to identify the model. Regularization (Tibshirani, 1996), tree-based models
different errors in the engines by using strict threshold criteria. (Hsu, 2004; Bertsimas and Dunn, 2017; Guolin et al., 2017),
They label any errors found with a particular error label based on mutual information (Jorge and Pablo, 2014; Bennasar et al.,
their technical knowledge. The proportion of engines with errors 2015), and clustering are other approaches for feature selection.
and the number of good engines are very low. To implement a
multiclass classification model using previous data, which Data Heteroscedasticity
automatically identifies the error class of an engine, developing In regression problems, the underlying assumption y ̂ for the error
such models with high accuracy is difficult. Skewed sample term in the response data is that it has constant variance
distributions are a common problem in industrial production- (homoscedasticity). Although such assumptions are useful to
related quality control, and imbalanced data lead to models where simplify models, real-world data do not follow the assumption
predictions are inclined toward the major class. In such cases, the of the constant variance error term and thus violate the
major class is “good engines.” If a model classifies a faulty engine assumption of homoscedasticity. Therefore, real data are
as a good engine (high false positives), then it would severely heteroscedastic. Predictions based on a simple linear model of
affect the reputation of quality control. In such cases, false such data would still be consistent but can lead to practical
positives could severely affect product reputation. implications that produce unreliable estimates of the standard
Undersampling of major classes and oversampling of minor error of coefficient parameters, thus leading to bias in test
classes form the basis of the solution commonly proposed for statistics and confidence intervals. Heteroscedasticity can be
the problem. References (Tajik et al., 2015; Zhang et al., 2015; caused directly or indirectly by effects such as changes in the
Duan et al., 2016) discuss fault detection models with an scale of observed data, structural shifts in the data and outliers, or
imbalanced training dataset in the industrial and the omission of explanatory variables. Heteroscedasticity can be
manufacturing sector. Resampling methods (oversampling, parametric, which means that it can be described as a function of
undersampling, and hybrid sampling) (Chawla et al., 2002; explanatory variables (White, 1980), or unspecified, meaning that
Han et al., 2005; Cateni et al., 2014; Sun et al., 2015; it cannot be described by explanatory variables. Examples in
Nekooeimehr et al., 2016), feature selection and extraction, manufacturing are related to predictive maintenance
cost-sensitive learning, and ensemble methods (Krawczyk, (i.e., predicting the remaining useful life of a machine based
2016; Guo et al., 2017) are other approaches to deal with the on vibration data), quality control, and optimization (Tamminen
class-imbalance problem. The use of evaluation measures et al., 2013; Lee et al., 2019). Heteroscedasticity in regression
considering the presence of undersampled classes is also models is identified by analyzing residual errors. Residual plots

Frontiers in Artificial Intelligence | www.frontiersin.org 12 June 2021 | Volume 4 | Article 576892



Tripathi et al. Data-Driven Knowledge Discovery Models

and several statistical tests may be used to test for model to predict product quality, the data (process parameters)
heteroscedasticity in data (Leslie, 1978; Breusch and Pagan, are recorded by sensors from several machines. In the injection
1979; White, 1980; Markowski and Markowski, 1990). Other molding process, the process parameters cannot estimate product
studies and methods to model the variance of response include quality alone because product quality is significantly affected by
weighted least squares (White, 1980), the heteroscedastic kernel temperature, humidity, machine health, and material type, and
(Cawley et al., 2004), heteroscedastic Gaussian process regression these external factors must be considered to optimize quality.
(Kersting et al., 2007; Kotanchek et al., 2010), heteroscedastic Similarly, in the sintering process (Strasser et al., 2019), where
Bayesian additive regression trees (BART) (Pratola et al., 2017), product quality is predicted in terms of its shape accuracy, the
and heteroscedastic support vector machine regression (Hu et al., data from various experiments show a considerable variation in
2016). different process parameters from unknown and unaccounted

sources. In such cases, the prediction can be biased or erroneous
Incomplete and Missing Data with high variance. A careful examination involving exploratory
Data quality is an essential part of data-driven process analysis is required to detect such effects. Gao et al. (2017) studied
optimization, process quality improvement, and smart decision a hierarchical analytic process to produce a comprehensive
making in production planning and control. In the quality evaluation system of large piston compressors that
manufacturing process, data come from various sources and is considers external and intrinsic effects.
heterogeneous in terms of variety and dimensionality. Data
quality is one of the important issues for the implementation Concept Drift
of robust ML methods in process optimization. Data quality may Changes in data over time due to various factors such as external
suffer for various reasons such as missing values, outliers, effects, environmental changes, technological advances, and
incomplete data, inconsistent data, noisy data, and various other reasons emerge from unknown real-world
unaccounted data (Köksal et al., 2011). The typical way to deal phenomena. ML models, in general, are trained with static
with missing data is to delete them or replace them with the data and thus do not consider the dynamic nature of the data,
average value or most frequent value and apply multiple such as changes over time in the underlying distribution. In such
imputations (Fritz, 2005) and expectation maximization (Allen cases, the performance of these models deteriorates over time.
and Tibshirani, 2010). Another method is to consider the Robust ML modeling requires identifying changes in data over
probability distribution of missing values in statistical time, separating noise from concept drift, adapting changes,
modeling (Rubin 1976; Little and Rubin, 2019). These and updating the model. Webb et al. (2016) provide a
considerations are of three types: 1) missing completely at hierarchical classification of concept drift that includes five
random, 2) missing at random, and 3) missing not at random. main categories: drift subject, drift frequency, drift transition,
Joint modeling and fully conditional specifications are two drift recurrence, and drift magnitude. They make the case that,
approaches to multivariate data imputation (Van Buuren rather than defining concept drift qualitatively, a quantitative
et al., 2006; van Buuren, 2007). Recent studies to impute description of concept drift is required to understand problems
missing data in production and manufacturing and optimize in order to detect and address time-dependent distributions.
production quality considered classification and regression trees These quantitative measures are cycle duration, drift rate,
to impute manufacturing data (White et al., 2018), modified fully magnitude, frequency, duration, and path length and are
conditional specifications (Guan et al., 2017), and multiple required for a detailed understanding of concept drift. Such
prediction models of a missing data set to estimate product an understanding allows modeling by new ML methods that
quality (Kang et al., 2018). Loukopoulos et al. (2018) studied are robust against various types of drifts because they can update
the application of different imputation methods to industrial themselves by active online learning and thereby detect drifts.
centrifugal compressor data and compared several methods. Lu et al. (2018) provide a detailed review of current research,
Their results suggest multiple imputations with self-organizing methods, and techniques to deal with problems related to
maps and k nearest neighbors as the best approach to follow. concept drift. One key point in that paper is that most of the
Incomplete and missing data have repercussions in business and methods identify “when” a drift happens in the data but cannot
data understanding, exploratory analysis, variable selection, answer “where” or “how” it happened. They further emphasize
model building, and evaluation. A careful strategy involving that research about concept drift should consider the following
imputation or deletion should be adopted for missing data. themes:

External Effects 1) Identifying drift severity and regions to better adapt to
External effects are important factors in data-driven process concept drift;
optimization. In a big data framework, external effects might 2) Techniques for unsupervised and semisupervised drift
be unnoticed, incorrectly recorded, or not studied in detail detection and adaptation;
(i.e., unknown). External effects can involve environmental 3) A framework for selecting real-world data to evaluate ML
factors (e.g., temperature, humidity), human resources, methods that handle concept drift;
machine health, running time, material quality variation, and 4) Integrating ML methods with concept-drift
other factors that are dealt with subjectively but significantly methodologies (Gama et al., 2013) discuss the various
affect production and data quality. For example, to create a ML evaluation and assessment practices for concept-drift

Frontiers in Artificial Intelligence | www.frontiersin.org 13 June 2021 | Volume 4 | Article 576892



Tripathi et al. Data-Driven Knowledge Discovery Models

methods and strategies to rapidly and efficiently detect fault detection (Lu et al., 2017) or predicting machine health
concept drift). (Deutsch et al., 2017). Wang et al. (2018) comprehensively

reviewed deep learning methods for smart manufacturing.
Cheng et al. (Lin et al., 2019) present the ensemble learning Importantly, deep learning models may suffer from the same

algorithm for condition-based monitoring with concept drift and issues as discussed in previous sections. Data complexity, model
imbalance data for offline classifiers. Yang et al. (2019) discuss a and time complexity, model interpretation, and the requirement
novel online sequential extreme learning model to detect various of large amounts of data means that they may not be suited for
types of drifts in data. Finally, Wang and Abraham (2015) every industrial production problem. Therefore, the demand
proposed a concept-drift detection framework known as remains strong in industrial production for traditional ML
“linear four rates” that is applicable for batch and streaming algorithms using feature-selection methods.
data and also deals effectively with imbalanced datasets. In ML problems, a feature is an attribute used in supervised or

In the manufacturing environment, concept drift is an unsupervised ML models as an explanatory or input variable.
expected phenomenon. When discussing with technical Features are constructed by applying mathematical functions to
experts, data drift should be understood and explained clearly raw attributes (i.e., input data) based on domain knowledge. As a
by experts for data and business understanding to ensure that result, feature engineering and extraction lead to new
future models are flexible and adaptable to changes due to characteristics of an original data set (i.e., it constructs a new
data drift. feature space from the original data descriptors). Features can be

created by methods that are linear, nonlinear, or use independent
Data Labeling component analysis. The main objective of feature-extraction
Data annotations (i.e., labels) as output allow ML methods to techniques is to remove redundant data and create interpretable
learn functions from the data. Specifically, input data are modeled models to improve prediction accuracy or to create generalized
through class labels by using supervised ML models for features that are, e.g., classifier independent. In general, feature
classification problems. If the labeling is noisy or not learning enhances the efficiency of regression and classification
appropriately assigned, the predictive performance of the models used for predictive maintenance and product quality
classification model is severely degraded. Therefore, for classification. In the manufacturing industry, feature
supervised ML models, data labeling or annotation is a engineering and extraction is a common practice for the
nontrivial issue for data quality, model building, and classification of engine quality, machine health, or similar
evaluation. The labeling can either be done manually by crowd problems using vibration data. For instance, fast Fourier
sourcing or by using semisupervised learning, transfer learning, transform or power spectral density statistical features are
active learning, or probabilistic program induction (Zhou et al., standard feature extraction methods used for vibration data
2017). Sheng et al. (2008) discuss repeated-labeling techniques to (Caesarendra and Tjahjowidodo, 2017).
label noisy data. In a typical manufacturing environment, labeling Sondhi (2009) discusses various feature-extraction methods
is done by operators or technical experts; in some cases, the same based on decision trees, genetic programming, inductive logic
type of data is annotated by multiple operators who work in programming, and annotation-based methods. Interestingly,
different shifts or at different sites. Sometimes, the operators do genetic programming in combination with symbolic regression
not follow a strict protocol and label intuitively based on their searches for a mathematical equation that best approximates a
experience. In such cases, data quality can suffer immensely. target variable. Given its simple and understandable structure,
Inadequate learning from data may occur if a large number of this approach has been useful for many industrial applications of
samples is not available for a specific problem and the data modeling and feature extraction (Kohavi and George, 1997; Yang
labeling is noisy. et al., 2015; Strasser et al., 2019). However, training for a large

Data labeling is a part of the data understanding phase and number of variables, model overfitting, and the time complexity
should follow a clear and well-defined framework based on the of the model are problematic for this approach. Caesarendra and
technical and statistical understanding of the manufacturing and Tjahjowidodo (2017) discuss five feature categories for vibration
production processes and their outcome. Many manufacturing data:
and production tasks are managed by machine operators,
technical experts, engineers, and domain experts using 1. phase-space dissimilarity measurement;
measures and experience to optimize the quality of the output. 2. complexity measurement;
Because these experts are well aware of the existing situation, they 3. time-frequency representation;
should be allowed to label data to produce robust ML models and 4. time-domain feature extraction;
maintain data quality. 5. frequency-domain feature extraction.

Feature Engineering These feature engineering methods are useful to summarize
The deep learning framework (Wang et al., 2018; Emmert-Streib various characteristics of vibration data and reduce the size of
et al., 2020a) provides a promising approach for automated smart high-dimensional data. Mechanical vibration is a useful indicator
manufacturing. These algorithms undertake automatic feature of machine functioning. The features of vibration data are often
extraction and selection at higher levels in the networks. They are used to train ML models to predict fault detection, do predictive
used for numerous important tasks in manufacturing, such as maintenance, and for various other diagnostic analyses. He et al.

Frontiers in Artificial Intelligence | www.frontiersin.org 14 June 2021 | Volume 4 | Article 576892



Tripathi et al. Data-Driven Knowledge Discovery Models

(2019) discuss the statistical pattern analysis framework for fault phases of the CRISP-DM framework. For instance, business
detection and diagnosis for batch and process data. In this understanding and data understanding go hand in hand
approach, instead of process variables, sample-wise and because we learn business objectives (business understanding)
variable-wise statistical features that quantify process and use relevant data (data understanding), so data should be
characteristics are extracted and used for process monitoring. explored appropriately (data preparation) by various statistical
This approach is useful for real-world dynamic, nonlinear, and and analytical tools to enhance our business understanding from
non-Gaussian process data, which are transformed into a realistic viewpoint. These three phases require an active
multivariate Gaussian-distributed features related to process cooperation by data experts and business experts so that any
characteristics that are then used for multivariate statistical gap or misinformation can be quickly corrected. Similarly, each
analysis. Ko et al. (Köksal et al., 2011) discuss various feature- phase in the CRISP-DM framework can seek interactions through
extraction and -engineering techniques for anomaly detection or a feedback loop to clarify the process, and such interactions can be
binary classification in different industries. temporary or permanent extensions of the model. Thus, the

Recent results for deep learning networks and support vector active interactions between the different phases of the CRISP-
machines demonstrate that feature selection can negatively affect DM framework should be systematically and efficiently used and
the prediction performance for high-dimensional genomic data managed in order to improve the whole data analysis process.
(Smolander et al., 2019). However, whether these results translate Therefore, for an efficient adaption for implementing data mining
to data in other domains remains to be seen. Until then, feature and ML models one should consider a completely connected
selection remains a standard approach of data preprocessing. CRISP-DM, that enable an active interactions between experts to

In general, for the CRISP-DM framework, feature engineering optimize a reliable and robust subclass of completely connected
is essential for real-world problems of model building. Real-world CRISP-DM.
data features are not independent—they are correlated with each We would like to note that the cyclic-nature of CRISP-DM is
other, which hints of interactions between the underlying similar to general data science approaches (Emmert-Streib et al.,
processes in manufacturing. Many of the higher-level effects 2016). Interestingly, this differs from ML or statistics that focus
related to the maintenance and product quality are traditionally on a single method only for the analysis of data,
combinations of lower-level effects of several processes and are establishing in this way one-step processes. Thus, CRISP-DM can
reflected by the data. Therefore, approaches that use feature be seen as an industrial realization of data science by detailing all
engineering, feature extraction, and feature selection are useful relevant steps. However, a fully connected GCRISP-DS with
to build models to predict or test for higher-level effects. active interactions is a more realistic and flexible human-

centered data science model for industrial applications.
Another important issue discussed herein is related to the

DISCUSSION model assessment from the viewpoint of data experts, business
experts and users. We discussed four essential components of

In this paper, we reviewed some of the key issues affecting the model assessment: model accuracy, model interpretability, model
performance, implementation and use of AI and ML models. multiplicity, and model transparency. All are crucial for the final
Specifically, we discussed existing methods and future directions deployment of the model. A model should not deviate from its
of model building and model evaluation in the area of smart goal as it encounters new data; it should predict results with
manufacturing. In this context, GCRISP-DS is a general accuracy and provide a satisfactory interpretation. Multiple
framework that provides a structured approach for data models with competing accuracy also present a challenge
mining applications. Its goal is to provide a comprehensive when it comes to selecting a robust and interpretable model.
data analytics toolbox to address challenges in manufacturing We define cases where the interpretability of the model is crucial
and ultimately help to establish standards for data-driven process for business understanding and decision making.
models that can be implemented, e.g., for improving production The fourth issue is model transparency. This should allow
quality, predictive maintenance, error detection, and other users to obtain information on the internal structure of
problems in industrial production and manufacturing. algorithms and methods to enable them to use various

The standard CRISP-DM framework describes a cyclical flow functional parameters so that the deployment phase can be
of the entire data mining process which contains several feedback implemented and integrated with the least effort and users can
loops. However, in many realistic data mining and modeling use the model and rely on its predictions. We suggest a
cases, it is an incomplete framework that requires additional documentation that includes model-related descriptions and
information and active interactions between different sections of appropriate details on business results. Specifically, we suggest
CRISP-DM. The demand for additional or new information can the following points for maintaining transparency:
arise due to real-world production complexity, e.g., data-related
or industry-specific applications, other organizational and – Model performance evaluation results with simulated and
manufacturing issues, or new emerging business trends. surrogate data should be provided to the user. These

Our review discussed data and model-related issues for performance evaluation should be performed considering
building robust models that are successfully linked to a various model and data related parameters such as:
business understanding. One of the challenges for robust performance with imbalanced data, sample-size, correlation
model building is the active interaction between different effect, incremental changes in data over time.

Frontiers in Artificial Intelligence | www.frontiersin.org 15 June 2021 | Volume 4 | Article 576892



Tripathi et al. Data-Driven Knowledge Discovery Models

–MLModel power and false positive rate (FPR) effect on decision model accuracy, model interpretability, model multiplicity
making should be summarized by defining a performance and model transparency.
score with respect to business decisions. For example, How 7) The GCRISP-DS framework adopts a human-centric
much a prediction made by a ML model could affect the approach to allow for transparent use of the model so that
business decisions in long and short run despite the models’ users and developers can evaluate, customize, and reuse
higher accuracy and low FPR. the results that enhance their understanding of better

– Users’ input data evaluation score comparing with training production quality, maintenance, and other production,
data. This information would allow users to understand the business, and societal goals.
deviation of the input data from the training data characteristics.

– User should be provided with Feature importance and their In general, for data-driven models, data are at the center stage
stability. Various feature importance strategies discussed in and all goals are realized by the potential of the available data
Model Assessment section can be used to describe feature (Emmert-Streib and Dehmer, 2019a). The assessment of achieved
importance score. We must also provide business experts business goals at the end-phase of a CRISP realization is also
evaluation on importance of such features. given through the success of the model. Thus, all novel

– Counter-intuitive predictions and features should be provided understanding depends on the data obtained and how we turn
to users, if any, where business experts and data models do not such data into useful information through systematic and
agree with each other. collaborative means. These objectives cannot be obtained

–Model security is one of the important concern, where the noise solely through the efforts of business experts or data experts.
in the collected data from smart sensors or IoT can be crafted Instead, a collective effort of active cooperation is required to
by a malware to give wrong decisions by a model. ML models establish a human-centered GCRISP-DS for achieving the
are vulnerable of such data despite the robustness. The data business goals. Such an interaction forms a complex system
and ML model should be tested and protected with such cases that leads to the emergence of various higher-level
and it should provide warnings to users when such data is used characteristics of KDD models in smart manufacturing. In
for prediction. such a complex system, the various AI and ML tasks must be

transparent, interactive, and flexible in order to create a robust
and stable manufacturing and production environment. Future

CONCLUSION research in this direction will explore industry-specific
requirements to develop data-driven knowledge discovery

In this paper, we provided a review of the CRISP-DM framework models and their implementation in practice.
and extensions thereof. A summarization of these extended The future challenges of GCRISP-DS are to develop methods
models we called GCRISP-DS because it provides the most and frameworks that could effectively estimate and measure the
flexible and customizable framework to deal with industry- interactions and their effect between different phases considering
specific problems. Furthermore, we provided an in-depth various influential factors in and between the phases. For
discussion of model assessment and robustness-issues which example, by quantifying these with with a quality score
are important phases of any CRISP realization. considering various data-related features such as sample-size,

Specifically, we reviewed the following important points for variance, data dimensionality, missing-values, and external
the application of data-driven knowledge discovery models: effects. One could optimize the requirements to be fulfilled by

each phase considering data quality scores and model
1) Adoption of relevant and practically implementable, performance scores for implementing a cost-effective and

scalable, cost-effective, and low-risk CRISP-DM models robust model. Similarly, different phases contribute to the cost
(subclass of the GCRISP-DS framework) with industry- and robustness depending on various other factors: domain-
specific and general industrial-trend related extensions. related challenges, technical challenges, and model

2) Each phase of the CRISP-DM framework should interact implementation challenges. Overall, such factors provide
actively so that any data and model issue can be resolved significant obstacles for a robust implementation of GCRISP-DS.
without delay.

3) When usingGCRISP-DS, define the problem category related
to industrial production and maintenance for the practical AUTHOR CONTRIBUTIONS
implementation of data analysis. This results in a problem-
specific CRISP realization (subgraph of GCRISP-DS). All authors listed have made a substantial, direct, and intellectual

4) Define the type of analysis to be performed for the model- contribution to the work and approved it for publication.
building to avoid wrong answers to the right questions.

5) Various data-issues should be appropriately handled for
data understanding and business understanding, such as FUNDING
exploration, preprocessing and model building (see
discussion in Model Assessment). ST is supported by X-pro project. X-pro is financed by research

6) Model evaluation and model deployment should ensure subsidies granted by the government of Upper Austria. MD
that the implemented model satisfies the requirements of received funding from the Austrian Science Fund (P 30031).

Frontiers in Artificial Intelligence | www.frontiersin.org 16 June 2021 | Volume 4 | Article 576892



Tripathi et al. Data-Driven Knowledge Discovery Models

REFERENCES Emmert-Streib, F., and Dehmer, M. (2019a). Defining data science by a data-driven
quantification of the community. Machine Learn. Knowl. Extr. 1 (1), 235–251.
doi:10.3390/make1010054

Allen, G. I., and Tibshirani, R. (2010). Transposable regularized covariance models Emmert-Streib, F., and Dehmer, M. (2019b). Evaluation of regression models:
with an application to missing data imputation. Ann. Appl. Stat. 4 (2), 764–790. model assessment, model selection and generalization error. Mach. Learn.
doi:10.1214/09-AOAS314 Knowl. Extr. 1 (1), 521–551. doi:10.3390/make1010032

Amershi, S., Cakmak, M., Bradley Knox, W., and Todd, K. (2014). Power to the Emmert-Streib, F., and Dehmer, M. (2019c). High-dimensional lasso-based
people: the role of humans in interactive machine learning. AI. Magazine 35, computational regression models: regularization, shrinkage, and selection.
105–120. doi:10.1609/aimag.v35i4.2513 Make 1 (1), 359–383. doi:10.3390/make1010021

Andrienko, G., Andrienko, N., Drucker, S., Fekete, J-D., Fisher, D., Idreos, S., et al. Emmert-Streib, F., Moutari, S., and Dehmer, M. (2016). The process of analyzing
(2020). “Big data visualization and analytics: future research challenges and data is the emergent feature of data science. Front. Genet. 7, 12. doi:10.3389/
emerging applications,” BigVis 2020: big data visual exploration and analytics, fgene.2016.00012
Copenhagen, DK, March 30, 2020. Emmert-Streib, F., Yang, Z., Feng, H., Tripathi, S., and Dehmer, M. (2020a). An

Ardagna, D., Cappiello, C., Samá, W., and Vitali, M. (2018). Context-aware data introductory review of deep learning for prediction models with big data. Front.
quality assessment for big data. Future Generation Comput. Syst. 89, 548–562. Artif. Intell. 3, 4. doi:10.3389/frai.2020.00004
doi:10.1016/j.future.2018.07.014 Emmert-Streib, F., Yli-Harja, O., and Dehmer, M. (2020b). Explainable artificial

Arthur, Z., Schubert, E., and Kriegel, H-P. (2012). A survey on unsupervised outlier intelligence and machine learning: a reality rooted perspective. Wiley
detection in high-dimensional numerical data. Stat. Anal. Data Mining 5 (5), Interdiscip. Rev. Data Mining Knowledge Discov. 10 (6), e1368. doi:10.1002/
363–387. doi:10.1002/sam.11161 widm.1368

Bennasar, M., Hicks, Y., and Setchi, R. (2015). Feature selection using joint mutual Fisher, A., Rudin, C., and Dominici, F. (2018). All models are wrong, but many are
information maximisation. Expert Syst. Appl. 42 (22), 8520–8532. doi:10.1016/j. useful: learning a variable’s importance by studying an entire class of prediction
eswa.2015.07.007 models simultaneously. J. Mach. Learn Res. 20, 1–81.

Bertsimas, D., and Dunn, J. (2017). Optimal classification trees. Mach Learn. 106 Fritz, S. (2005). Multiple imputation: how it began and continues. The Am.
(7), 1039–1082. doi:10.1007/s10994-017-5633-9 Statistician 59 (4), 315–319. doi:10.1198/000313005X74016

Bertsimas, D., and Kallus, N. (2020). From predictive to prescriptive analytics. Gama, J., Sebastião, R., and Rodrigues, P. P. (2013). On evaluating stream learning
Manage. Sci. 66 (3), 1005–1504. doi:10.1287/mnsc.2018.3253 algorithms. Mach Learn. 90 (3), 317–346. doi:10.1007/s10994-012-5320-9

Berzal, F. (2019). Evaluation metrics for unsupervised learning algorithms. Gao, G., Wu, H., Sun, L., and He, L. (2017). Comprehensive quality evaluation
Sebastopol, CA: O’Reilly Media, Inc. system for manufacturing enterprises of large piston compressors. Proced. Eng.

Breiman, L. (2001). Statistical modeling: the two cultures (with comments and a 174, 566–570. doi:10.1016/j.proeng.2017.01.188
rejoinder by the author). Statist. Sci. 16 (3), 199–231. doi:10.1214/ss/1009213726 Grady, N. W. (2016). “Kdd meets big data,” IEEE international conference on big

Breusch, T. S., and Pagan, A. R. (1979). A simple test for heteroscedasticity and random data (big data), Washington, DC, December 5–8, 2016.
coefficient variation. Econometrica 47 (5), 1287–1294. doi:10.2307/1911963 Guan, T., Zhang, Z., Wen, Dong., Qiao, C., and Gu, X. (2017). “Data-driven fault

Caesarendra, W., and Tjahjowidodo, T. (2017). A review of feature extraction diagnosis with missing syndromes imputation for functional test through
methods in vibration-based condition monitoring and its application for conditional specification,” in 22nd IEEE European Test Symposium (ETS),
degradation trend estimation of low-speed slew bearing. Machines 5, 4. Limassol, CY, May 22–26, 2017 (IEEE).
doi:10.3390/machines5040021 Guo, H., Li, Y., Shang, J., Gu, M., Huang, Y., and Gong, B. (2017). Learning from

Cateni, S., Colla, V., and Vannucci, M. (2014). A method for resampling class-imbalanced data: review of methods and applications. Expert Syst. Appl.
imbalanced datasets in binary classification tasks for real-world problems. 73, 220–239. doi:10.1016/j.eswa.2016.12.035
Neurocomputing 135, 32–41. doi:10.1016/j.neucom.2013.05.059 Guolin, K., Qi, M., Finley, T., Wang, T., Chen,W., Ma,W., et al. (2017). “Lightgbm:

Cawley, G. C., Talbot, N. L. C., Foxall, R. J., Dorling, S. R., andMandic, D. P. (2004). a highly efficient gradient boosting decision tree,” Advances in neural
Heteroscedastic kernel ridge regression. Neurocomputing 57, 105–124. doi:10. information processing systems. Editors I. Guyon, U. V. Luxburg, S. Bengio,
1016/j.neucom.2004.01.005 H. Wallach, R. Fergus, S. Vishwanathan, et al. (New York, NY: Curran

Chang, T. C., and Faison, E. (2001). Shrinkage behavior and optimization of Associates, Inc.) 30, 3146–3154.
injection molded parts studied by the taguchi method. Polym. Eng. Sci. 41 (5), Haffar, J. (2015). Have you seen asum-dm?. Available at: ftp://ftp.software.ibm.
703–710. doi:10.1002/pen.10766 com/software/data/sw-library/services/ASUM.pdf

Charles, T. M., Calmon, F., and Ustun, B. (2019). Predictive multiplicity in Hall, P., and Gill, N. (2018). An introduction to machine learning interpretability.
classification. arXiv, in International Conference onMachine Learning, 6765–6774. Newton, MA: O’Reilly Media,inc.

Chawla, N. V., Bowyer, K. W., Hall, L. O., and Kegelmeyer, W. P. (2002). Synthetic Han, H., Wang, W-Y., and Mao, B-H. (2005). “A new over-sampling method in
minority over-sampling technique. J. Artif. Intell. Res. (JAIR) 16, 321–357. imbalanced data sets learning,” in Advances in intelligent computing. Editors
doi:10.1613/jair.953 D-S Huang, X-P Zhang, and G-B Huang (Berlin, Heidelberg: Springer),

Cichy, C., and Rass, S. (2019). An overview of data quality frameworks. IEEE Access 878–887.
7, 24634–24648. doi:10.1109/access.2019.2899751 Hatvany, J., and Lettner, F. J. (1983). The efficient use of deficient knowledge. CIRP

Cios, K. J., Pedrycz, W., and Swiniarski, R. W. (2012). Data mining methods for Ann. 32 (1), 423–425. doi:10.1016/s0007-8506(07)63433-7
knowledge discovery: Berlin, Heidelberg: Springer Science\Business Media. Hatvany, J., and Nemes, L. (1978). Intelligent manufacturing systems–– a

Deutsch, J., He, M., and He, D. (2017). Remaining useful life prediction of hybrid tentative forecast. IFAC Proc. Volumes 11, 895–899. doi:10.1016/S1474-
ceramic bearings using an integrated deep learning and particle filter approach. 6670(17)66031-2
Appl. Sci. 7 (7), 649. doi:10.3390/app7070649 Hazen, B. T., Boone, C. A., Ezell, J. D., and Jones-Farmer, L. A. (2014). Data quality

Diez-Olivan, A., Del Ser, J., Galar, D., and Sierra, B. (2019). Data fusion and for data science, predictive analytics, and big data in supply chain management:
machine learning for industrial prognosis: trends and perspectives towards an introduction to the problem and suggestions for research and applications.
industry 4.0. Inf. Fusion 50, 92–111. doi:10.1016/j.inffus.2018.10.005 Int. J. Prod. Econ. 154, 72–80. doi:10.1016/j.ijpe.2014.04.018

Doshi-Velez, F., and Kim, B. (2017). Towards a rigorous science of interpretable He, Q. P., Wang, J., and Shah, D. (2019). Feature space monitoring for smart
machine learning. arXiv. manufacturing via statistics pattern analysis. Comput. Chem. Eng. 126, 321–331.

Duan, L., Xie, M., Bai, T., and Wang, J. (2016). A new support vector data doi:10.1016/j.compchemeng.2019.04.010
description method for machinery fault diagnosis with unbalanced datasets. Hicks, S. C., and Peng, R. D. (2019). Elements and principles for characterizing
Expert Syst. Appl. 64, 239–246. doi:10.1016/j.eswa.2016.07.039 variation between data analyses. arXiv [Preprint arXiv:1903.07639]

Duch, W., Setiono, R., and Zurada, J. M. (2004). Computational intelligence Hoffmann, I., Serneels, S., Filzmoser, P., and Croux, C. (2015). Sparse partial robust
methods for rule-based data understanding. Proc. IEEE. 92 (5), 771–805. m regression. Chemometrics Intell. Lab. Syst. 149, 50–59. doi:10.1016/j.
doi:10.1109/jproc.2004.826605 chemolab.2015.09.019

Frontiers in Artificial Intelligence | www.frontiersin.org 17 June 2021 | Volume 4 | Article 576892



Tripathi et al. Data-Driven Knowledge Discovery Models

Howard, D. F., and Dai, D. (2014). Public perceptions of self-driving cars: the case of method of offline classifiers. IEEE Access 7, 56198–56207. doi:10.1109/
berkeley, California, in Transportation research board 93rd annual meeting, access.2019.2912631
14, 1–16. Little, R. J. A., and Rubin, D. (2019). “Statistical analysis with missing data”, in

Hsu, W. H. (2004). Genetic wrappers for feature selection in decision tree Wiley series in probability and statistics. Hoboken, NJ: Wiley.
induction and variable ordering in bayesian network structure learning. Inf. Liu, J., Kong, X., Xia, F., Bai, X., Wang, L., Qing, Q., et al. (2018). Artificial
Sci. 163, 103–122. doi:10.1016/j.ins.2003.03.019 intelligence in the 21st century. IEEE Access 6, 34403–34421. doi:10.1109/

Hu, Q., Zhang, S., Yu, M., and Xie, Z. (2016). Short-term wind speed or power access.2018.2819688
forecasting with heteroscedastic support vector regression. IEEE Trans. Sustain. Loukopoulos, P., George, Z., Bennett, I., Sampath, S., Pilidis, P., Duan, F., et al.
Energ. 7 (1), 241–249. doi:10.1109/tste.2015.2480245 (2018). “Addressing missing data for diagnostic and prognostic purposes,” in

Huber, S., Wiemer, H., Schneider, D., and Ihlenfeldt, S. (2019). Dmme: data mining Engineering asset management 2016. Editors J. Zuo, M Lin, J Mathew, and
methodology for engineering applications – a holistic extension to the crisp-dm H-Z Huang (New York, NY: Springer International Publishing), 197–(205.)
model. Proced. CIRP. 79, 403–408. doi:10.3390/app9122407 Lu, C., Wang, Z., and Zhou, B. (2017). Intelligent fault diagnosis of rolling bearing

Jorge, R. V., and Pablo, A. E. (2014). A review of feature selectionmethods based on using hierarchical convolutional network based health state classification. Adv.
mutual information. Neural Comput. Appl. 24 (1), 175–186. doi:10.1007/ Eng. Inform. 32, 139–151. doi:10.1016/j.aei.2017.02.005
s00521-013-1368-0 Lu, J., Liu, A., Dong, F., Gu, F., Gama, J., and Zhang, G. (2018). Learning under

Kalgotra, P., and Sharda, R. (2016). “Progression analysis of signals: extending concept drift: a review. IEEE Trans. Knowledge Data Eng. 12, 2346–2363. doi:10.
crisp-dm to stream analytics,” IEEE international conference on big data (big 1109/TKDE.2018.2876857
data), Washington DC, December 5–8, 2016, 2880–2885. Maldonado, S., andWeber, R. (2009). A wrapper method for feature selection using

Kang, S., Kim, E., Shim, J., Chang, W., and Cho, S. (2018). Product failure support vector machines. Inf. Sci. 179 (13), 2208–2217. doi:10.1016/j.ins.2009.
prediction with missing data. Int. J. Prod. Res. 56 (14), 4849–4859. doi:10. 02.014
1080/00207543.2017.1407883 Maratea, A., Petrosino, A., and Manzo, M. (2014). Adjusted f-measure and kernel

Karkouch, A., Mousannif, H., Al Moatassime, H., and Noel, T. (2016). Data quality scaling for imbalanced data learning. Inf. Sci. 257, 331–341. doi:10.1016/j.ins.
in internet of things: a state-of-the-art survey. J. Netw. Comput. Appl. 73, 57–81. 2013.04.016
doi:10.1016/j.jnca.2016.08.002 Markowski, C. A., and Markowski, E. P. (1990). Conditions for the effectiveness of

Kaur, K., and Rampersad, G. (2018). Trust in driverless cars: investigating key a preliminary test of variance. Am. Statistician 44 (4), 322–326. doi:10.1080/
factors influencing the adoption of driverless cars. J. Eng. Tech. Manage. 48, 00031305.1990.10475752
87–96. doi:10.1016/j.jengtecman.2018.04.006 Martínez-Plumed, F., Contreras Ochando, L., Ferri, C., and Peter, A. (2017). Casp-

Kersting, K., Plagemann, C., Pfaff, P., and Burgard, W. (2007). “Most likely dm: context aware standard process for data mining. arXiv.
heteroscedastic gaussian process regression,” in Proceedings of the 24th Matthews, B. W. (1975). Comparison of the predicted and observed secondary
international conference on machine learning. New York, NY: ICML ’07ACM. structure of t4 phage lysozyme. Biochim. Biophys. Acta (Bba) - Protein Struct.

Khalid, K., Henri, P., and Nasser, M. (1997). Using multi-agent architecture in fms 405 (2), 442–451. doi:10.1016/0005-2795(75)90109-9
for dynamic scheduling. J. Intell. Manufacturing 8 (1), 41–47. doi:10.1023/A: Mohammad, H. (2017). Debating big data: a literature review on realizing value
1018540317470 from big data. J. Strateg. Inf. Syst. 26 (3), 191–209. doi:10.1016/j.jsis.2017.

Ko, T., Lee, J. H., Cho, H., Cho, S., Lee, W., and Lee, M. (2017). Machine learning- 07.003
based anomaly detection via integration of manufacturing, inspection and after- Monostori, L. (2003). Ai and machine learning techniques for managing
sales service data. Imds. 117, 927–945. doi:10.1108/imds-06-2016-0195 complexity, changes and uncertainties in manufacturing. Eng. Appl. Artif.

Kohavi, R., and John, G. H. (1997). Wrappers for feature subset selection. Artif. Intelligence 16 (4), 277–291. doi:10.1016/s0952-1976(03)00078-2
Intelligence 97, 273–324. doi:10.1016/s0004-3702(97)00043-x Nagashima, H., and Kato, Y. (2019). “Aprep-dm: a framework for automating the

Köksal, G., Batmaz, İ., and Testik, M. C., (2011). A review of data mining pre-processing of a sensor data analysis based on crisp-dm,” IEEE international
applications for quality improvement in manufacturing industry. Expert conference on pervasive computing and communications workshops, Kyoto,
Syst. Appl. 38 (10), 13448–13467. doi:10.1016/j.eswa.2011.04.063 Japan, March 11–15, 2019 (IEEE). doi:10.1109/PERCOMW.2019.8730785

Kotanchek, M. E., Vladislavleva, E. Y., and Smits, G. F. (2010). Symbolic regression Nekooeimehr, I., Lai-Yuen, S. K., and Lai-Yuen (2016). Adaptive semi-
via genetic programming as a discovery engine: insights on outliers and unsupervised weighted oversampling (a-suwo) for imbalanced datasets.
prototypes. Boston, MA: Springer. Expert Syst. Appl. 46, 405–416. doi:10.1016/j.eswa.2015.10.031

Krawczyk, B. (2016). Learning from imbalanced data: open challenges and future Nino, M., Miguel Blanco, J., and Illarramendi, A. (2015). “Business understanding,
directions. Prog. Artif. Intell. 5 (4), 221–232. doi:10.1007/s13748-016-0094-0 challenges and issues of big data analytics for the servitization of a capital

Kristoffersen, E., Aremu, O. O., Blomsma, F., Mikalef, P., and Li, J.I (2019). equipment manufacturer,” IEEE international conference on big data (big
“Exploring the relationship between data science and circular economy: an data), Santa Clara, CA, October 29–November 1, 2015 IEEE, 1368–1377.
enhanced crisp-dm process model,” in Digital transformation for a sustainable Oliveira, M., Arica, E., Pinzone, M., Fantini, P., and Taisch, M. (2019). Human-
society in the 21st century. Editors O. Pappas, PMikalef, Y.K Dwivedi, J Jaccheri, centered manufacturing challenges affecting European industry 4.0 enabling
M Krogstie, and Mäntymäki (New york, NY: Springer International technologies. (New York, NY: Springer International Publishing), 507–517.
Publishing), 177–189. Pan, S. J., and Yang, Q. (2010). A survey on transfer learning. IEEE Trans. Knowl.

Kusiak, A. (2018). Smart manufacturing. Int. J. Prod. Res. 56 (1–2), 508–517. Data Eng. 22 (10), 1345–1359. doi:10.1109/tkde.2009.191
doi:10.1080/00207543.2017.1351644 Peng, K., Liang, D., Gao, L., and Lou, J. (2015). Probabilistic electricity price

Kusiak, A. (2017). Smart manufacturing must embrace big data.Nature 544, 23–25. forecasting with variational heteroscedastic gaussian process and active
doi:10.1038/544023a learning. Energ. Convers. Manage. 89, 298–308. doi:10.1016/j.enconman.

Lee, C-Y., Huang, T-S., Liu, M-K., and Lan, C-Y. (2019). Data science for vibration 2014.10.003
heteroscedasticity and predictive maintenance of rotary bearings. Energies 12 Pratola, M., Chipman, H., George, E., and McCulloch, R. (2017). Heteroscedastic
(5), 801. doi:10.3390/en12050801 BART using multiplicative regression trees. J. Comp. Grap. Stat. 29, 405–417.

Lee, J-H., and Kim, C-O. (2008). Multi-agent systems applications in doi:10.1080/10618600.2019.1677243
manufacturing systems and supply chain management: a review paper. Int. Qin, Y., Sheng, Q. Z., Falkner, N. J. G., Dustdar, S., Wang, H., and Vasilakos, A. V.
J. Prod. Res. 46 (1), 233–265. doi:10.1080/00207540701441921 (2016). When things matter: a survey on data-centric internet of things. J. Netw.

Leek, J. T., and Peng, R. D. (2015). What is the question?. Science 347 (6228), Comput. Appl. 64, 137–153. doi:10.1016/j.jnca.2015.12.016
1314–1315. doi:10.1126/science.aaa6146 Rao, L., Mansingh, G., and Osei-Bryson, K.-M. (2012). Building ontology based

Leslie, G. (1978). Godfrey. Testing for multiplicative heteroskedasticity. J. Econom. knowledge maps to assist business process re-engineering. Decis. Support Syst.
8 (2), 227–236. doi:10.1016/0304-4076(78)90031-3 52 (3), 577–589. doi:10.1016/j.dss.2011.10.014

Lin, C-C., Deng, D-J., Kuo, C-H., and Chen, L. (2019). Concept drift detection and Raschka, S. (1811). Model evaluation, model selection, and algorithm selection in
adaption in big imbalance industrial iot data using an ensemble learning machine learning. arXiv.

Frontiers in Artificial Intelligence | www.frontiersin.org 18 June 2021 | Volume 4 | Article 576892



Tripathi et al. Data-Driven Knowledge Discovery Models

Ribeiro, M. T., Singh, S., and Guestrin, C. (2016a). Model-agnostic interpretability Taguchi, G., Elsayed, E. A., and Hsiang, T. C. (1989). “Quality engineering in
of machine learning. arXiv. arXiv [Preprint arXiv:1606.05386] production systems,” in Series in industrial engineering and management

Ribeiro, M. T., Singh, S., and Guestrin, C. (2016b). Why should i trust you?” science (New York: McGraw-Hill).
Explaining the predictions of any classifier. 1135–1144. doi:10.1145/2939672. Taguchi, G., and Konishi, S. (1987). Orthogonal Arrays and linear graphs: tools for
2939778 quality engineering. Taguchi methods. Dearborn, MI: American Supplier

Ross, J. W., Beath, C. M., and Quaadgras, A. (2013). You may not need big data Institute.
after all. Harv. Business Rev. 91, 12. Tajik, M., Movasagh, S., Shoorehdeli, M. A., and Yousefi, I. (2015). “Gas turbine

Rubin, D. B. (1976). Inference and missing data. Biometrika 63 (3), 581–592. shaft unbalance fault detection by using vibration data and neural networks,”
doi:10.1093/biomet/63.3.581 3rd RSI international conference on robotics and mechatronics (ICROM),

Russell, S. J., and Peter, N. (1995). Artificial intelligence: a modern approach. New Tehran, IR, October 7–9, 2015 (IEEE).
Jersey: Prentice-Hall, Inc. Tamminen, S., Tiensuu, H., Juutilainen, I., and Röning, J. (2013). “Steel

Sacha, D., Senaratne, H., Kwon, B. C., Ellis, G., and Keim, D. A. (2015). The role of property and process models for quality control and optimization,”
uncertainty, awareness, and trust in visual analytics. IEEE Trans. Vis. Comput. Physical and numerical Simulation of materials processing VII, volume
Graph 22 (1), 240–269. doi:10.1109/TVCG.2015.2467591 762 of materials science forum. (Stafa-Zurich, CH: Trans Tech

Schäfer, F., Zeiselmair, C., Becker, J., and Otten, H. (2018). “Synthesizing crisp- Publications Ltd), 301–306.
dm and quality management: a data mining approach for production Tibshirani, R. (1996). Regression shrinkage and selection via the lasso. J. R. Stat.
processes,” IEEE international conference on technology management, Soc. Ser. B (Methodological) 58 (1), 267–288. doi:10.1111/j.2517-6161.1996.
operations and decisions (ICTMOD). Marrakech, MR, November 21–23, tb02080.x
2018, (IEEE). Uddin, M. F., Gupta, N., and Ali-ud-din Khan, M. (2014). “Seven v’s of big data

Semenova, L., and Rudin, C. (2019). A study in rashomon curves and volumes: a understanding big data to extract value,” Proceedings of the 2014 zone 1
new perspective on generalization and model simplicity in machine learning. conference of the American society for engineering education, Bridgeport, CT,
arXiv. United States, April 3–5, 2014 (IEEE).

Sharma, S., and Osei-Bryson, K-M. (2009). Framework for formal implementation Unal, R., and Dean, E. B. (1991). Taguchi approach to design optimization for
of the business understanding phase of data mining projects. Expert Syst. Appl. quality and cost: an overview, in Annual Conference of the International Society
36 (2), 4114–4124. doi:10.1016/j.eswa.2008.03.021 of Parametric Analysts.

Sharma, S., and Osei-Bryson, K-M. (2008). “Organization-ontology based Urmson, C., and Whittaker, W. (2008). Self-driving cars and the urban challenge.
framework for implementing the business understanding phase of data IEEE Intell. Syst. 23 (2), 66–68. doi:10.1109/mis.2008.34
mining projects,” in Proceedings of the 41st annual Hawaii international Vale Tavares, M. C., Alencar, P., and Cowan, D. (2018). “A variability-aware design
conference on system sciences. Waikoloa, HI, Janaury 7–10, 2008, (New approach to the data analysis modeling process,” IEEE international conference
York, NY: IEEE). on big data (big data), Seattle, United States, December 10–13, 2018 (IEEE),

Shearer, C. (2000). The crisp-dmmodel: the new blueprint for data mining. J. Data 2818–2827.
Warehousing 5 (4), 13–22. Van Buuren, S., Brand, J. P. L., Groothuis-Oudshoorn, C. G. M., and Rubin, D. B.

Sheng, V. S., Provost, F., and Ipeirotis, P. G. (2008). “Get another label? improving (2006). Fully conditional specification in multivariate imputation. J. Stat.
data quality and data mining using multiple, noisy labelers,” in Proceedings of Comput. Simulation 76 (12), 1049–1064. doi:10.1080/10629360600810434
the 14th ACM SIGKDD international conference on knowledge discovery and van Buuren, S. (2007). Multiple imputation of discrete and continuous data by fully
data mining. (New York, NY: KDD ’08ACM), 614–622. conditional specification. Stat. Methods Med. Res. 16 (3), 219–242. doi:10.1177/

Smolander, J., Stupnikov, A., Glazko, G., Dehmer, M., and Emmert-Streib, F. 0962280206074463
(2019). Comparing biological information contained in mrna and non-coding Vapnik, V. N., and Chervonenkis, A. Y. (1971). On the uniform convergence of
rnas for classification of lung cancer patients. BMC Cancer 19 (1), 1176. doi:10. relative frequencies of events to their probabilities. Theor. Probab. Appl. 16 (2),
1186/s12885-019-6338-1 264–280. doi:10.1137/1116025

Sondhi, P. (2009). Feature construction methods: a survey. sifaka. cs. uiuc. edu 69, Vogl, G. W., Weiss, B. A., and Helu, M. (2019). A review of diagnostic and
70–71. prognostic capabilities and best practices for manufacturing. J. Intell. Manuf. 30

Springer, A. (2019). “Enabling effective transparency: towards user-centric (1), 79–95. doi:10.1007/s10845-016-1228-8
intelligent systems,” Proceedings of the 2019 AAAI/ACM Conference on Wang, H., and Abraham, Z. (2015). “Concept drift detection for streaming data,”
AI, ethics, and society, AIES ’19. (New York, NY: ACM), 543–544. International joint conference on neural networks (IJCNN), Killarney, IE, July

Stanula, P., Ziegenbein, A., and Metternich, J. (2018). Machine learning algorithms 12–17, 2015 (IEEE).
in production: a guideline for efficient data source selection. Proced. CIRP. 78, Wang, J., Ma, Y., Zhang, L., Gao, R. X., andWu, D. (2018). Deep learning for smart
261–266. doi:10.1016/j.procir.2018.08.177 manufacturing: methods and applications. J. Manufacturing Syst. 48, 144–156.

Strasser, S., Zenisek, J., Tripathi, S., Schimpelsberger, L., and Jodlbauer, H. (2019). doi:10.1016/j.jmsy.2018.01.003
“Linear vs. symbolic regression for adaptive parameter setting in manufacturing Wang, S., Wan, J., Zhang, D., Li, D., and Zhang, C. (2016). Towards smart factory
processes,” in Christoph quix and jorge BernardinoData management technologies for industry 4.0: a self-organized multi-agent system with big data based
and applications (New York: Springer International Publishing), 50–68. feedback and coordination. Computer Networks 101, 158–168. doi:10.1016/j.

Su, C-T., and Hsiao, Y-H. (2007). An evaluation of the robustness of mts for comnet.2016.02.019
imbalanced data. IEEE Trans. Knowl. Data Eng. 19 (10), 1321–1332. doi:10. Webb, G. I., Hyde, R. H, Cao, H., Nguyen, H. L., and Petitjean, F. (2016).
1109/tkde.2007.190623 Characterizing concept drift. Data Min. Knowl. Disc. 30 (4), 964–994.

Subasi, A., and Ismail Gursoy, M. (2010). Eeg signal classification using pca, ica, lda doi:10.1007/s10618-015-0448-4
and support vector machines. Expert Syst. Appl. 37 (12), 8659–8666. doi:10. Weller, A. (2017). Transparency: motivations and challenges. New York: Springer
1016/j.eswa.2010.06.065 International Publishing.

Sun, Z., Song, Q., Zhu, X., Sun, H., Xu, B., and Zhou, Y. (2015). A novel ensemble White, H. L. (1980). A heteroskedasticity-consistent covariance matrix estimator
method for classifying imbalanced data. Pattern Recognit. 48 (5), 1623–1637. and a direct test for heteroskedasticity. Econometrica. 48 (4), 817–838. doi:10.
doi:10.1016/j.patcog.2014.11.014 2307/1912934

Stahel, W. R. (2016). The circular economy. Nature 531 (7595), 435–438. doi:10. White, T. K., Reiter, J. P., and Petrin, A. (2018). Imputation in u.s. manufacturing
1038/531435a data and its implications for productivity dispersion. Rev. Econ. Stat. 100 (3),

Steed, C. A., Halsey, W., Dehoff, R., Yoder, S. L., Paquit, V., and Powers, S. (2017). 502–509. doi:10.1162/rest_a_00678
Falcon: visual analysis of large, irregularly sampled, and multivariate time series Wuest, T., Irgens, C., and Thoben, K-D. (2014). An approach to monitoring quality
data in additive manufacturing. Comput. Graphics 63, 50–64. doi:10.1016/j.cag. in manufacturing using supervised machine learning on product state data.
2017.02.005 J. Intell. Manuf. 25 (5), 1167–1180. doi:10.1007/s10845-013-0761-y

Frontiers in Artificial Intelligence | www.frontiersin.org 19 June 2021 | Volume 4 | Article 576892



Tripathi et al. Data-Driven Knowledge Discovery Models

Wuest, T., Weimer, D., Irgens, C., and Thoben, K-D. (2016). Machine learning in Zhou, F., Lin, X., Liu, C., Zhao, Y., Xu, P., Ren, L., et al. (2019). A survey of visualization
manufacturing: advantages, challenges, and applications. Prod. Manufacturing for smart manufacturing. J. Vis. 22 (2), 419–435. doi:10.1007/s12650-018-0530-2
Res. 4 (1), 23–45. doi:10.1080/21693277.2016.1192517 Zhou, L., Pan, S., Wang, J., and Vasilakos, A. V. (2017). Machine learning on big

Yang, G., Li, X., Wang, J., Lian, L., and Ma, T. (2015). Modeling oil production data: opportunities and challenges.Neurocomputing 237, 350–361. doi:10.1016/
based on symbolic regression. Energy Policy 82, 48–61. doi:10.1016/j.enpol. j.neucom.2017.01.026
2015.02.016

Yang, Z., Al-Dahidi, S., Baraldi, P., Zio, E., and Montelatici, L. (2019). A novel Conflict of Interest: The authors declare that the research was conducted in the
concept drift detection method for incremental learning in nonstationary absence of any commercial or financial relationships that could be construed as a
environments. IEEE Trans. Neural Networks Learn. Syst. 31, 309–320. potential conflict of interest.
doi:10.1109/TNNLS.2019.2900956

Yuan, M., and Lin, Y. (2006). Model selection and estimation in regression with Copyright © 2021 Tripathi, Muhr, Brunner, Jodlbauer, Dehmer and Emmert-Streib.
grouped variables. J. R. Stat. Soc. B. 68 (1), 49–67. doi:10.1111/j.1467-9868.2005. This is an open-access article distributed under the terms of the Creative Commons
00532.x Attribution License (CC BY). The use, distribution or reproduction in other forums is

Zhang, X., Wang, B., and Chen, X. (2015). Intelligent fault diagnosis of roller permitted, provided the original author(s) and the copyright owner(s) are credited
bearings with multivariable ensemble-based incremental support vector and that the original publication in this journal is cited, in accordance with accepted
machine. Knowledge-Based Syst. 89, 56–85. doi:10.1016/j.knosys.2015. academic practice. No use, distribution or reproduction is permitted which does not
06.017 comply with these terms.

Frontiers in Artificial Intelligence | www.frontiersin.org 20 June 2021 | Volume 4 | Article 576892