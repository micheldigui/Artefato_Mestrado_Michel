---
source_file: "2024-Unlocking the power of industrial artificial intelligence towards Industry 5.0 Insights, pathways, and challenges.txt"
original_rel_path: "Trabalhos\Artigos\Aproveitar parcialmente\txt\2024-Unlocking the power of industrial artificial intelligence towards Industry 5.0 Insights, pathways, and challenges.txt"
category: "Artigos_Aproveitar_parcialmente"
extension: ".txt"
sha256: "0f6cff061663c5f44f7ae0e8e145dc006dbc527f2318670bc586b5dae686e7b9"
extracted_at: "2026-09-20T00:50:21.698170"
---

﻿Journal of Manufacturing Systems 73 (2024) 349–363

Contents lists available at ScienceDirect 

Journal of Manufacturing Systems 
journal homepage: www.elsevier.com/locate/jmansys 

Review 

Unlocking the power of industrial artificial intelligence towards Industry 
5.0: Insights, pathways, and challenges 
Jiewu Leng a, Xiaofeng Zhu a, Zhiqiang Huang a, Xingyu Li b, Pai Zheng c, Xueliang Zhou d, 
Dimitris Mourtzis e, Baicun Wang f, Qinglin Qi g, Haidong Shao h, Jiafu Wan i, Xin Chen a, 
Lihui Wang j, Qiang Liu a,* 

a Guangdong Provincial Key Laboratory of Computer Integrated Manufacturing, and State Key Laboratory of Precision Electronic Manufacturing Technology and 
Equipment, Guangdong University of Technology, Guangzhou 510006, China 
b School of Engineering Technology, Purdue University, West Lafayette, IN 47907, USA 
c Department of Industrial and Systems Engineering, The Hong Kong Polytechnic University, 999077, Hong Kong, China 
d Department of Electrical and Information Engineering, HuBei University of Automotive Technology, Shiyan 442002, China 
e Laboratory for Manufacturing Systems and Automation, Department of Mechanical Engineering and Aeronautics, University of Patras, Rio Patras 26504, Greece 
f State Key Laboratory of Fluid Power and Mechatronic Systems, Zhejiang University, Hangzhou 310027, China 
g School of Automation Science and Electrical Engineering, Beihang University, Beijing 100191, China 
h College of Mechanical and Vehicle Engineering, Hunan University, Changsha 410082, China 
i School of Mechanical and Automotive Engineering, South China University of Technology, Guangzhou 510641, China 
j Department of Production Engineering, KTH Royal Institute of Technology, Stockholm, Sweden   

A R T I C L E  I N F O   A B S T R A C T   

Keywords: With the continuous development of human-centric, resilient, and sustainable manufacturing towards Industry 
Industrial artificial intelligence 5.0, Artificial Intelligence (AI) has gradually unveiled new opportunities for additional functionalities, new 
Collaborative intelligence features, and tendencies in the industrial landscape. On the other hand, the technology-driven Industry 4.0 
Self-learning intelligence paradigm is still in full swing. However, there exist many unreasonable designs, configurations, and imple
Crowd intelligence 
Industry 5.0 mentations of Industrial Artificial Intelligence (IndAI) in practice before achieving either Industry 4.0 or Industry 

5.0 vision, and a significant gap between the individualized requirement and actual implementation result still 
exists. To provide insights for designing appropriate models and algorithms in the upgrading process of the 
industry, this perspective article classifies IndAI by rating the intelligence levels and presents four principles of 
implementing IndAI. Three significant opportunities of IndAI, namely, collaborative intelligence, self-learning 
intelligence, and crowd intelligence, towards Industry 5.0 vision are identified to promote the transition from 
a technology-driven initiative in Industry 4.0 to the coexistence and interplay of Industry 4.0 and a value- 
oriented proposition in Industry 5.0. Then, pathways for implementing IndAI towards Industry 5.0 together 
with key empowering techniques are discussed. Social barriers, technology challenges, and future research di
rections of IndAI are concluded, respectively. We believe that our effort can lay a foundation for unlocking the 
power of IndAI in futuristic Industry 5.0 research and engineering practice.   

1. Introduction requires the development of circular processes, recycling of resources, 
reducing waste and environmental negative impacts, and thus forming a 

Recently, Industry 5.0 has been proposed by the European Com circular economy with higher resource efficiency. On another hand, the 
mission to achieve a human-centered, sustainable, and resilient Euro United Nations (UN) has released a series of goals to be achieved, also 
pean industry [1]. The human-centered approach places workers’ known as Sustainable Development Goals (SDGs). Therefore, the 
requirements, preferences, and interests at the center of the above-mentioned SDGs can be considered the goals for the realization of 
manufacturing process, moving from a technology-driven paradigm to a Industry 5.0, and by extension Society 5.0. Resilience necessitates the 
human-centered and society-centered one. Sustainable development cultivation of greater responsiveness within the manufacturing system 

* Corresponding author. 
E-mail address: liuqiang@gdut.edu.cn (Q. Liu).  

https://doi.org/10.1016/j.jmsy.2024.02.010 
Received 16 October 2023; Received in revised form 1 February 2024; Accepted 16 February 2024   
Available online 29 February 2024
0278-6125/© 2024 The Society of Manufacturing Engineers. Published by Elsevier Ltd. All rights reserved.



J. Leng et al.                                                                                                                                                                                     J  o  u r  n  a l  o  f  M   a  n  u f a  c  t u  r i n  g  S  y  s t e m   s 73 (2024) 349–363

to better withstand disruptions and ensure that critical infrastructure Intelligence’”, were used for retrieving publications from the Web of 
can be provided and supported in times of crisis [2]. Science database. This inclusive search outputs 17 and 316 publications, 

The significance of Industry 5.0 is to match humans with intelligent respectively, for further screening (up to 30 Sept. 2023). Secondly, high- 
machines and train collaborative robots to adapt to the intentions of quality articles advancing IndAI models/methods/technologies (e.g., 
humans when working together. Human intelligence can be used for smart design, intelligent manufacturing, and predictive maintenance) 
critical thinking about customized demands, and IndAI systems and are included. As a result, 103 publications that satisfy the selection 
collaborative robots can be used for labor-intensive tasks, thereby criteria were used. Additionally, 32 supplementary publications dis
effectively alleviating the weakening of manpower and improving pro cussing the trending of AI/IndAI (e.g., collaborative intelligence, crowd 
duction efficiency [3]. Industry 5.0 will change the global intelligence, and self-learning intelligence) and related empowering 
manufacturing system, infiltrating a new generation of IndAI systems technologies for AI/IndAI (e.g., robots and CPUs) were summarized to 
into the supply chain and production shop floor, and introducing more highlight and guide the discussion focus on unlocking the power of 
cost-effective and human-centric IndAI. IndAI towards Industry 5.0. Therefore, this article includes 135 refer

The combination of AI and industry is proceeding. IndAI focuses on ences in total. 
developing, validating, and deploying various intelligent algorithms for This perspective article classifies the IndAI by rating the intelligence 
industrial applications with sustainable performance [4–9]. From the levels, which provides a guide for proper designing and implementing 
perspectives of social science, management & operations science, and appropriate models and algorithms to unlock the power of IndAI in 
computer science, the research of AI should be a hundred schools of practice. Key characteristics and the empowering technologies of IndAI 
thought, such as embodied AI, physical AI, and artificial social intelli for human-centric, resilient, and sustainable manufacturing towards 
gence, which are indeed reasonable in the corresponding context. Industry 5.0 vision are identified. Then, typical pathways of IndAI ap
However, in industry, the simple pursuit of more advanced AI is not plications are discussed in five dimensions, namely, design, 
what we want to emphasize at the moment. In the process of digital manufacturing, marketing and logistics, operation and maintenance 
transformation and upgrading of the industry, due to either the absence service, and recycling and remanufacturing. Finally, social barriers, 
of value-oriented awareness or the lack of systematic understanding of technical challenges, and future research directions of IndAI for Industry 
IndAI technologies, there is often a contractionary that the design of 5.0 are concluded. 
IndAI models/algorithms does not match the application scenario. And This perspective article is outlined as follows. Section 2 presents the 
it includes three typical improper designs/usages of IndAI insights of IndAI towards Industry 5.0. Section 3 describes the pathways 
models/algorithms:  of IndAI towards Industry 5.0. Section 4 analyzes the challenges and 

research directions. Finally, Section 5 concludes. 
1) Abuse of IndA: Using the IndAI models to solve the problems could be 

potentially addressed by clever design of functional materials, me 2. Insights for unlocking the power of IndAI towards Industry 
chanical structures, and system behaviors. Physical hardware design 5.0 
usually is more reliable and cost-effective than software and codes. 
Abuse of IndAI models in industrial controls may lead to an increase 2.1. Connotations of IndAI 
in system complexity as well as an increase in system failure 
possibility.  Since the Dartmouth Conference in 1956, AI has been studied by a 

2) Complicating simple scenarios: Deploying advanced IndAI in simple large number of scholars. AI technologies are categorized by their ca
scenarios can meet most of the intelligent decision needs of the pacity to mimic human characteristics, the technology they use to do 
scenario. The indiscriminate pursuit of high-end intelligence not only this, their real-world applications, and the theory of mind. Since Hinton 
makes computing performance surplus but also increases the et al. put forward deep learning in 2006, AI began its prosperous 
implementation cost burden.  development, including its applications in industry. AI is evolving from 

3) Simplifying complicated scenarios: Only low-end or inadequate AI 1.0 to AI 2.0 [10]. The initial definition of AI 2.0 is a new generation 
IndAI are equipped in complex scenarios. Although the cost of IndAI of AI based on the significantly changed new informatization environ
implementations is reduced, this may result in wrong decisions, ment, a high level of autonomy and decision-making capability, and the 
quality issues, and yield loss. development of new goals. The new informatization environment is 

driven by the popularization of the mobile Internet and advanced 
The first two situations resulted from a technology-driven perspec computing terminals, the penetration of sensor and control networks, 

tive, without sufficient consideration of the value-oriented evaluation of the rise of online social communities, and the emergence of a new 
the system sustainability and societal needs. With the continuous generation of IT (e.g., blockchain, cloud computing, and big data ana
upgrading of the industry and the emerging penetration of Industry 5.0, lytics [7]). The core concepts of AI 2.0 recognized by the community 
more and more IndAI technologies will be applied in industrial pro include big-data-based Intelligence, cross-media Intelligence, 
cesses, but a relatively systematic discussion of the IndAI framework for Internet-crowd intelligence, human-machine hybrid-augmented intelli
guiding the value-oriented design and implementations is rare. gence, and autonomous intelligence. These five intelligent technologies 

The motivation of this perspective article is to address the improper represent the birth of a new generation of AI, followed by other 
design and usage of IndAI in the manufacturing paradigm evolution emerging concepts such as embodied AI, physical AI, and artificial social 
towards 5.0, and the goal is to present insights on the IndAI for providing intelligence. The implementation of a new generation of AI in industrial 
guidance rather than review all IndAI papers to make a typical statistical processes accelerates the development of products. 
survey. Although it is not necessary to address the detailed literature The combination of AI and industry is proceeding. Some scholars 
review methodology as a survey, certain guidance about the literature presented definitions of IndAI from different perspectives as shown in  
research is included here to relate the previous works to this article. Table 1. For instance, Lee et al. (2018) [4] defined IndAI as a systematic 
Although many studies on intelligent manufacturing and specific models discipline, that focuses on developing, validating, and deploying various 
of AI such as deep learning and machine learning applications may machine learning algorithms for industrial applications with sustainable 
involve research on IndAI, using these keywords will produce vast pa performance. Based on the review of the literature and the under
pers, that are similar in the application logic and could be categorized standing of actual industrial applications, this perspective article defines 
into well-known sub-fields from different perspectives. Therefore, to IndAI as follows: IndAI is an interdisciplinary research field that uses 
highlight the focus on unlocking the power of IndAI, two keywords, advanced computer technology to deeply integrate industrial infrastructures 
namely, “industrial artificial intelligence”, and “‘Industry’ and ‘Artificial with advanced AI models/methods and enables industrial systems to have 

350



J. Leng et al.                                                                                                                                                                                     J  o  u r  n  a l  o  f  M   a  n  u f a  c  t u  r i n  g  S  y  s t e m   s 73 (2024) 349–363

Table 1 intelligent systems. 
Existing definitions of IndAI.  According to these criteria, intelligence is divided into five levels 

Authors Definitions from lower level to upper level, namely, reactive IndAI, Knowledgeable 
IndAI, Learnable IndAI, Autonomous IndAI, and Sharable IndAI, as 

Lee et al. (2018)[4] Focus on developing, validating, and deploying various 
machine learning algorithms for industrial applications with shown in Table 2. They represent different levels/grades of intelligence 
sustainable performance. in the industry, and enterprises can choose different levels of intelli

Zhang et al. (2019) A deep integration of AI technology and industrial process, gence according to their actual needs. 
[11] in which industrial enterprises take IndAI technologies to Designing appropriate models and algorithms in the digital upgrad

achieve intelligent function in all stages of the industrial 
value chain. ing process of the industry is critical for unlocking the power of IndAI 

Peres et al. (2020) A systematic discipline focusing on the development, while ensuring cost-effectiveness and reliability. Usually, the lower- 
[12] validation, deployment, and maintenance of AI solutions (in level IndAI algorithms are more reliable, cost-effective, and robust 

their varied forms) for industrial applications with than the higher-level IndAI algorithms. Four principles of implementing 
sustainable performance. IndAI algorithms could be identified as follows:  

Hoffmann et al. The combination of sensors with the Industrial Internet of 
(2020)[13] Things, (big) data, algorithms, and processing power. 

Yang et al. (2021) To combine general AI technology with specific industrial 1) A designer should avoid abuse of IndAI if the needs could be resolved 
[14] scenarios in order to achieve innovative applications, such as by innovative, clever, and dedicated mechanism design in its mate

design model innovation, intelligent production decision- rial, structure, and behavior dimension since the physical mecha
making, and optimal resource allocation. 

Mathew et al. (2023) A systematic strategy for creating, validating, and deploying nism is more reliable than the software and code;  
[15] various machine learning algorithms for high-performing 2) A designer should consider all possibilities and scenarios in practice, 

industries. and design an IndAI model or algorithm possessing sufficient intel
Viola et al. (2023) Any application of AI related to the physical operations or ligence and robustness to address the challenges; 

[16] systems of an enterprise. 3) A designer should prioritize the adoption of a lower-level IndAI al
Rožanec et al. (2023) A specific case of Narrow AI applied to industry.  

[17] gorithm rather than a higher-level one to save cost and improve 
reliability if the lower-level IndAI algorithm could adequately ach
ieve the management and control goals; 

enhanced capabilities of perception, cognition, learning, organizing, execu 4) A designer should make the IndAI implementations more sustain
tion, self-decision-making, and mutual-adaptation, and makes it empower the able, resilient, and human-centric under the premise of satisfying the 
product/service lifecycle management to help enterprises realize the functional and performance needs. 
value-adding. 

2.3. Opportunities of IndAI for Industry 5.0 
2.2. Classification of IndAI and its four implementation principles 

Industry 5.0 [1] places the well-being of the workers at the center of 
IndAI is applied to different stages of product/service lifecycle ac the manufacturing process by making production respect the boundaries 

tivities and various levels of industrial systems, resulting in different of our planet and the harmonious symbiosis between humans and ma
levels of intelligence [6,18–20]. Generally, there are three grades of chines, to achieve societal goals beyond jobs and economic growth, and 
artificial intelligence, namely, Artificial Narrow Intelligence (ANI), further achieve sustainable development goals of super-smart society 
Artificial General Intelligence (AGI), and Artificial Super Intelligence and ecological values, which will become a robust and resilient provider 
(ASI). Morris et al. [20] (Google DeepMind research team) defined five of prosperity in an Industrial Community of Shared Future [21]. 
levels of AGI, including Emerging AGI, Competent AGI, Expert AGI, Three key propositions are stated in the Industry 5.0 whitepaper [1]. 
Virtuoso AGI, and Superhuman AGI. Rajani classifies AI into four cate The first proposition is human-centricity. Industry 4.0 focuses on the 
gories [19]: 1) optimal in which it is not possible to perform better, 2) feasibility and implementation of technology but pays less attention to 
strong super-human which performs better than all humans, 3) the needs of humans. As the actual operator of the process, workers fail 
super-human which performs better than most humans, and 4) to play an effective role in supervision and decision-making. Therefore, 
sub-human which performs worse than most human. These classifica in the Industry 5.0 vision, workers return to the center of the process and 
tion criteria are designed based on the comparison between computer act as the actual decision-makers of the process. The second proposition 
and human intelligence. Therefore, it is challenging to distinguish an AI is sustainability. Technology-driven Industry 4.0 aggravates some 
model/algorithm to which grade it belongs since the criteria are neither common social and environmental problems. Industry 5.0 emphasizes 
specific enough nor executable in practice. the concept of sustainable development, reusing/recycling natural re

Another perspective to classify the AI models/algorithms is to refer sources, and reducing waste and environmental impact, so that the in
to the Von Neumann architecture. For instance, Liu et al. [18] proposed dustrial ecology forms a good development pattern of symbiosis [22]. 
four criteria based on Von Neumann architecture for defining a standard The third proposition is resilience. Brittleness is a system problem that is 
intelligence system. By referring to these four criteria, to provide a guide not easy to appear. Once it occurs, it will cause serious damage to pro
for designing and implementing appropriate models and algorithms to duction. The pandemic, for example, highlights the fragility of the cur
unlock the power of IndAI in industrial practice, five criteria to classify rent rigid hierarchy of globalized collaboration mode of production. 
the IndAI applications are identified as follows: 

Criterion 1: Whether it can interact with context, that is, whether Table 2 
there is an input-output system. Intelligence level of IndAI.  

Criterion 2: Whether the industrial system has a knowledge database 
that stores and updates decision rules/patterns. Level Criterion Criterion Criterion Criterion Criterion 

1 2 3 4 5 
Criterion 3: Whether the industrial system can constantly and 

automatically learn the decision knowledge from the interaction context Sharable IndAI √ √ √ √ √ 
Autonomous √ √ √ √  

and make self-updating of knowledge. IndAI 
Criterion 4: Whether the industrial system can self-percept, self- Learnable IndAI √ √ √   

learn, self-execute, self-organize, and self-adapt to new environments. Knowledgeable √ √    
Criterion 5: Whether the industrial system can share self-updated IndAI 

knowledge and up-to-date intelligence with other heterogeneous Reactive IndAI √      

351



J. Leng et al.                                                                                                                                                                                     J  o  u r  n  a l  o  f  M   a  n  u f a  c  t u  r i n  g  S  y  s t e m   s 73 (2024) 349–363

How to make industrial production better resist disruptions is an self-learn without labeled data when transferred to a new environment. 
important research direction of Industry 5.0. The development of a Self-learning AI is artificial intelligence that can train itself using unla
sufficiently flexible strategic value chain, modulized manufacturing beled data. On a high level, it works by analyzing a dataset and looking 
system, adaptable production capacity, predictive controls, and flexible for patterns that it can draw conclusions from. The European Research 
business processes are also key issues to be faced in forming the resil Centre is supporting a self-learning AI research project, named GEN
ience of Industry 5.0. MOD (https://erc.europa.eu). 

To achieve societal goals beyond jobs and growth, and to become a As illustrated in Fig. 2, self-learning IndAI models can make the 
resilient provider of prosperity, it is urgent to make innovations in machines more intelligent and give them the potential to generate their 
models/methods as well as reorganize the advanced technologies/ own new intelligent decision patterns. These characteristics of self- 
techniques in a value-oriented manner. As shown in Fig. 1, corre learning intelligence give machines as well as the manufacturing sys
sponding to three propositions (i.e., human-centricity, sustainability, tem the ability to develop sustainability. This intelligence could change 
and resilience) mentioned above, three opportunities of IndAI towards the way AI is created and change our inertial thinking to help machines/ 
Industry 5.0, namely, collaborative intelligence, self-learning intelli systems solve many kinds of problems that they didn’t counter before. 
gence, and collective intelligence, could be identified for unlocking the Because of the low cost of trial and error, self-learning intelligence can 
power of IndAI. verify various cases to find the optimal solution for the new environment 

and complete the self-evolution. 
2.3.1. Collaborative intelligence 

Collaborative Intelligence [23,24] is defined as the joining forces of 2.3.3. Crowd intelligence 
Humans and AI. Its representative facilities are various smart devices, Crowd Intelligence [26,27] emerges from the collective intelligent 
such as collaborative robots and collaborative agents, designed to assist efforts of massive numbers of autonomous individuals, who are moti
human activities. These smart devices can notice, understand, and feel vated to carry out challenging computational tasks under a certain 
the workers, as well as the goals and expectations that are being per Internet-based organizational structure. In the context of Industry 5.0, 
formed. Its purpose is to observe and learn how humans perform tasks crowd intelligence enhances the system resilience under disruptions, 
and to help workers perform tasks. In Industry 5.0 vision, AI is required based on strong self-adaptivity among human-machine hybrid groups 
to permeate humans to collaborate, recognize, and actively enhance and lower bio-machine hybrid groups. Usually, researchers refer to the 
each other’s complementary strengths: 1) the intuition, leadership, former intelligence as collective intelligence and the latter intelligence 
teamwork, creativity, and social skills of workers, and 2) the speed, as swarm intelligence. Crowd intelligence is a synthesis of these two 
precision, and persistence of machines [21]. Through this complemen kinds of intelligence. This development of such complexes requires 
tarity, the full potential of machines and humans can be fully brought groups with different knowledge and complementary skills to be coor
into play, and human-centered collaborative intelligence can be truly dinated in a distributed manner to produce decentralized and resilient 
realized. crowd intelligence. It is necessary to connect individuals into a group 

through decentralized collaboration, competition, and good incentive 
2.3.2. Self-learning intelligence mechanisms, and at the same time, quality control of the crowd is 

Self-learning intelligence enables machines to consistently learn and necessary to ensure the quality of the whole system. 
create more knowledge and decision patterns by themselves [25]. The Fig. 3 illustrates the rationale of crowd intelligence. Individuals 
societal needs and the manufacturing system itself are dynamically make use of the obtained information, produce group interaction 
changing over time, and the operating data thereby may be of new through competition and cooperation with other individuals, and then 
unknown patterns and are difficult to label. It requires machines to make their own decisions. Crowd intelligence enables rapid reorgani

zation and adaptation in response to unexpected disruptions to form a 
new balanced manufacturing organization [28]. Finally, the individual 
decisions are aggregated and fed back to the group to produce a more 
excellent problem solution for handling disruptions. 

Despite humans, machines in the crowd could be empowered by 
modeling as agents [29], and its high-level potential benefits include:  

1) Collaborative and effective decision system. Democratize access to 
IndAI models and their benefits by enabling coordinated IndAI and 
multi-agent interactions [8], decentralizing data ownership, sharing 
knowledge, and access to huge datasets;  

2) Self-organizing cooperation. Enabling a new form of self-organizing 
intelligence beneficial to the race with networks that consider 
interoperability, data sovereignty, privacy, modularity, and 
scalability;  

3) Democratic governance. Incorporating democratic governance and 
other incentives in ways that support behaviors that are beneficial to 
the network as a whole moves IndAI decentralized and free markets 
in a favorable direction;  

4) Beneficial IndAI. On the decentralized network, beneficial reserves 
and network wealth form a virtuous circle through benefit ratings, so 
that IndAI can attract more users while exerting its value and culti
vating a more beneficial user economy. 

Fig. 3 shows the decentralized agent model where nodes are con
nected in a distributed manner and each node is characterized by a high 
degree of autonomy. An agent can achieve decentralized access to IndAI 

Fig. 1. Characteristics of IndAI for Industry 5.0.  based on this model. When some nodes cannot be accessed due to 

352



J. Leng et al.                                                                                                                                                                                     J  o  u r  n  a l  o  f  M   a  n  u f a  c  t u  r i n  g  S  y  s t e m   s 73 (2024) 349–363

Fig. 2. Self-learning intelligence.  

Fig. 3. Crowd intelligence for resilient manufacturing under disruptions [28].  

disruptions, the missing part is compensated by the call of other nodes as models and algorithms in the upgrading process of the industry is of 
much as possible to achieve resilient decentralized crowd intelligence. greater significance for unlocking the power of IndAI. 

Three opportunities of IndAI discussed above are promising research 
directions for advancing Industry 5.0 engineering practice, but they 
should not be directly identified as determinate directions/stages of 
Industry 5.0 development. Also, the simple pursuit of more advanced AI 
is not what we want to emphasize at the moment. Designing appropriate 

353



J. Leng et al.                                                                                                                                                                                     J  o  u r  n  a l  o  f  M   a  n  u f a  c  t u  r i n  g  S  y  s t e m   s 73 (2024) 349–363

3. Pathways for unlocking the power of IndAI towards Industry for intrusion detection [31]), decision tree (e.g., for quality disturbance 
5.0 detection [32]), K-nearest neighbor (e.g., for traffic flow prediction 

[33]), K-means (e.g., for wind power prediction [34]), random forest (e. 
3.1. Framework of IndAI applications g., for machinery fault diagnosis [35]), dimensionality reduction (e.g., 

for wind turbine state monitoring [36]), and neural network (e.g., for 
The development of IndAI cannot be separated from the advance flexible joint manipulator control [37]). These algorithms can be applied 

ment of mainstream AI, and enterprises also need a reference to guide to various industrial scenarios. 
their IndAI transformation. Therefore, this perspective article summa The most popular three academic schools of core AI algorithms are 
rizes the aspects that enterprises will be involved in the IndAI applica Symbolicism, Connectionism, and Actionism, respectively. Each pos
tions and puts forward a technical IndAI reference framework as shown sesses distinct characteristics that align with different requirements in 
in Fig. 4. It is divided into four layers, namely, the Hardware Infra industrial scenarios.  
structure Layer, Computing Engine Layer, AI Algorithms Layer, and 
Industrial Application Layer, together with related empowering tech 1) Symbolicism AI: Symbolism is also called logicism, and its core is 
nologies across layers. mathematical logic, which aims to build AI systems with axioms and 

The first layer provides the Internet of Things (IoT) facilities, logic systems. The representatives include Support Vector Machine 
computing hardware, data services, and networking capabilities. The (SVM) and Expert System. This type of AI model has achieved more 
IoT facilities are essential to quickly understanding the production status results in the early stage of AI development.  
of the industry system. Networking facilities enable rapid data trans 2) Connectionism AI: Connectionism originated from bionics, so it is 
mission and informative decisions. also called bionicsism. Based on the model of the human brain, it 

The second layer provides the runtime environment and computing proposes to use algorithms to simulate the neurons of the human 
platform. A big data platform is a set of infrastructures that deals with brain and connect the neurons as nodes to form neural networks. 
storage and real-time computing of massive uninterrupted data. At Nowadays, the neural network has been applied in various industries 
present, there are mature methods to deal with multi-source heteroge and has achieved good results. The development of neural networks 
neous data. The running environment is a container that can support the has also developed from the initial Perceptron, Long Short-Term 
development and training of InAI models/algorithms. Memory (LSTM), Hopfield Neural Network, and Backpropagation 

The third layer includes typical core AI algorithms used in industry Neural Network to the Current Deep Neural Network, Recurrent 
[5], such as linear regression (e.g., for material usage optimization), Neural Network, and Convolutional Neural Network.  
logistic regression (e.g., for simplifying tomography system), support 3) Actionism AI: The core idea of actionism is cybernetics, which links 
vector machine (SVM) (e.g., for fault diagnosis [30]), Naive Bayes (e.g., the working principles of the nervous system with information 

Fig. 4. Reference framework of IndAI applications.  

354



J. Leng et al.                                                                                                                                                                                     J  o  u r  n  a l  o  f  M   a  n  u f a  c  t u  r i n  g  S  y  s t e m   s 73 (2024) 349–363

theory, control theory, logic, and computers. A representative established for selecting mechanical system components with mixed 
example of this type of AI (e.g., Reinforcement Learning, Genetic design variables and constraints [39]. IndAI could discover the risks and 
Algorithm, Evolutionary Algorithm) is the hexapod robot with a uncertainties in the design optimization process [40]. Smart design in
control system that simulates insect behavior based on sensory- volves both products and the corresponding manufacturing systems. The 
action patterns. Actionism focuses on the development of applied smart manufacturing system design is much more complex and involves 
technology, which is purposeful and can be quickly put into a multiple dimensions including function, structure, behavior, control, 
practical application. intelligence, and performance [41]. 

The smart design could reduce the amount of computation and 
The industrial application layer adapts to the individualized design, shorten the execution time. Nowadays, AI-Generated Content (AIGC) 

configuration, and operation of production/business processes/systems, technology is a promising enabler for empowering smart design. The 
as well as product lifecycle management needs. generative design enabled by the IndAI is a promising direction. How

The reference framework of IndAI presented here is not new ever, the time-consuming process of complex modeling and configuring 
knowledge but a gathering of best practices. In the implementation of the design problem is an obstacle hindering unlocking the power of 
IndAI, the practitioners are suggested to refer to the presented frame AIGC. 
work based on four principles proposed in Section 2.2, with a systematic 
understanding of goals, constraints, and characteristics of their in 3.2.2. IndAI-driven smart manufacturing 
dustries, to obtain a balance of the performance, cost, reliability, and Manufacturing is a process of processing, assembling, and inspecting 
security of the applications. And not all elements in the presented materials to create products. Smart manufacturing applications involve 
reference framework are supposed to be included and realized in a all system levels from equipment (e.g. [42]), manufacturing cell (e.g. 
specific implementation, since the simpler the design, the higher the [43]), production line (e.g. [44]), workshop (e.g. [45], [46]), factory (e. 
reliability of the system. g. [47]), to supply chain management (e.g. [48]). A smart 

manufacturing system is a reconfigurable, flexible, agile, and resilient 
3.2. Dimensions for unlocking the power of IndAI towards Industry 5.0 system with self-sensing, self-learning, and self-adaptive functions in 

multiple dimensions, such as process optimization, production sched
Typical dimensions for unlocking the power of IndAI towards In uling [9], quality control, and operations management. 

dustry 5.0 are discussed from the product lifecycle management Nowadays, production scheduling has become an indispensable part 
perspective. The product lifecycle dimension comprises a series of of smart manufacturing [49], and the application of intelligent algo
interrelated value-creating activities from product concepting to prod rithms is also a reflection of IndAI. Production scheduling organizes the 
uct recycling, such as design, manufacturing, logistics & marketing, and timing and resources of jobs or tasks in manufacturing or service to 
operation & maintenance. As shown in Fig. 5, IndAI in the product achieve predetermined system goals, such as arranging the online 
lifecycle dimension accelerates the upgrading speed, production effi sequence of various products in the assembly line to achieve the shortest 
ciency, and service quality of products. The lifecycle activities could be makespan. Scheduling intelligence is mainly reflected in various intel
iteratively optimized to achieve sustainability. ligent optimization algorithms and models in job shops [50]. Current 

intelligent scheduling studies emphasize more on energy consumption 
3.2.1. IndAI-driven smart design [51]. Dynamic events including machine failure, travel delay operation, 

Design is a process of selecting the appropriate variables and pa and poor-quality operation make intelligent scheduling more difficult 
rameters to satisfy the individualized needs of users under given con [52]. Moreover, trusted collaborative manufacturing remains chal
straints and existing conditions. Smart design is a process of optimizing lenging, and how to implement a secure and sharable IndAI model in a 
all feasible schemes from the dimensions of function, structure, distributed manufacturing context is also challenging. 
behavior, control, and performance of products/services/systems ac Enhancing the machine vision by integrating IndAI for defect 
cording to the requirements [38]. Design optimization models could be recognition and fault detection is fruitful [53]. Machine learning-based 

Fig. 5. IndAI empowering the product lifecycle management.  

355



J. Leng et al.                                                                                                                                                                                     J  o  u r  n  a l  o  f  M   a  n  u f a  c  t u  r i n  g  S  y  s t e m   s 73 (2024) 349–363

online fault identification methods could be designed for the timely [66], in which IndAI could act as a key enabler. For instance, a joint 
identification of material defects caused by process non-conformities optimization could make the pricing, quality level, and effort decisions 
[54]. The application of deep neural networks to machine vision tasks of manufacturers, retailers, and third parties more reasonable and 
enables substantial leaps in model performance [55]. Good classification coherent [67]. The IndAI models should be integrated with innovations 
can be achieved without a large number of labeled datasets. Therefore, in the process flow, flexible additive manufacturing technologies [68], 
few-shot learning-based, learnable, and physics-informed IndAI are hot and recyclable materials usage [69]. IndAI enables new process flow for 
topics in smart manufacturing for unlocking their power in the industry. the production to achieve environmental friendliness and low energy 

consumption [70]. 
3.2.3. IndAI-driven smart marketing and logistics Manufacturers are committed to developing sustainable production 

The marketing process requires analysis, prediction, and accurate and consumption strategies to reduce their negative impact on the 
recommendations to different consumers. Smart marketing combines environment and society [71]. Emerging IndAI technologies and 
advanced marketing thinking with new IndAI methods. It is supposed to advanced manufacturing capabilities are supporting the sustainable 
be a consumer-centric solution towards Industry 5.0 to achieve development and intelligent remanufacturing of manufacturers [72]. 
personalized marketing. Intelligent demand forecasting systems could Table 3 summarizes the specific IndAI applications in product life
be developed based on the analysis and interpretation of historical data cycle management for unlocking their power in the industry. In each 
by integrating time series analysis techniques. The periodic trend of user implementation dimension of IndAI, the practitioners are suggested to 
behavior could be mined to recommend the potential goods to the user refer to the presented framework based on four principles proposed in 
at the appropriate time. For instance, Li et al. [56] proposed an intelli Section 2.2, with a systematic understanding of goals, constraints, and 
gent attention allocation link prediction algorithm to predict the characteristics of their industries, to obtain a balance of the perfor
possible friendship between users in different circles for solving the mance, cost, reliability, and security of the applications. 
problem of cross-marketing network sparsity. Also, smart logistics in
volves route optimization and storage optimization in the physical flow 
process of materials/products from supplying to receiving to meet the 3.3. Related empowering technologies for implementing IndAI 
increasing complexity and volume of logistics operations due to the 
collaboration and integration of online and offline channels globally The combination of IndAI models/algorithms and related empow
[57]. How to make marketing more personalized is the problem smart ering technologies can produce outstanding results for unlocking their 
marketing and logistics have to face. power in the industry. 

3.2.4. IndAI-driven smart operation and maintenance service 3.3.1. AI CPUs and GPUs 
Operation and maintenance services encompass a series of value- AI CPUs and GPUs are of dedicated design for fasting IndAI 

adding activities resulting from the interaction between product pro computing. CPU is mainly used to manage the entire system, execute 
viders and customers. The smart operation and maintenance service software programs, process input and output, and control task sched
applications majorly include product predictive maintenance and fault uling in AI [76]. It is responsible for the operation of the AI framework, 
diagnosis. data preprocessing, and post-processing tasks. CPU is very important for 

Predictive maintenance is to predict the future development trend of controlling processes and completing complex logical calculations, 
the product status and formulate corresponding maintenance plans in especially in model optimization, parameter updating, and adjustment 
advance according to its operating trend and possible failure modes. during training. On another hand, GPU is mainly used for large-scale 
IndAI model-based predictive maintenance solution could be developed parallel computing in AI, especially good at dealing with large-scale 
to analyze the health status of products and machines [58]. For instance, data computing tasks such as matrix operations and deep neural 
Wang et al. [59] proposed a long- and short-term memory recurrent 
neural network-based maintenance predictor to improve the mainte Table 3 
nance efficiency of high-speed railway power equipment. Degradation IndAI applications for product lifecycle management.  
estimation methods could be also designed for redundant system Lifecycle Cases Ref. 
maintenance planning optimization [60]. Smart Design Constrained design optimization of [39],[73], 

Fault diagnosis is to comprehensively understand the device condi function, structure, behavior, control, [40] 
tion, discover faults in time, and identify the source of faults. Integrating intelligence, and performance of 
various machine learning strategies (e.g., transfer learning [61], deep products/services/systems 
convolutional network [62], and two-stage learning [63]) with Fuzzy multi-objective evaluation of 

design decision, 
multi-domain feature extraction methods could improve fault diagnosis Design optimization for manufacturing 
accuracy. and assembly. 

Nowadays, smart operation and maintenance services have become Smart Manufacturing Multi-objective flexible job shop [74],[75], 
more flexible, networked, autonomous, and adaptive [64]. Integrating scheduling, [51],[54], 

the new generation of behavior operation management theory into Online fault identification of [55] 
manufacturing system operating, 

hybrid IndAI models is a promising solution for unlocking their power in Product surface defect detection. 
the industry. Smart Marketing and Intelligent demand forecasting, [56],[57] 

Logistics Mining of the periodic trend of user 
3.2.5. IndAI-driven smart recycling and remanufacturing behaviors, 

Intelligent attention allocation link 
Recycling and remanufacturing have an important impact on the prediction and path optimization, 

circular economy to provide all-round sustainable benefits [65]. In a Warehousing optimization in the logistics 
circular economy, the goal is to maintain utility and value throughout process. 
the life cycle of products, components, and materials. Recycling and Smart Operation and Predictive maintenance, [59],[58], 

remanufacturing are mainly reflected in several aspects, such as reusable Maintenance Machine fault diagnosis, [62],[61] 
Proactive adjustment of operating 

resource recovery, reducing emissions, and saving energy. Combining parameters. 
consumers’ low-carbon preference and remanufacturing preference Smart Recycling and Repairing damaged parts, [68],[70]  
with market demand in the recycling and remanufacturing decision is Remanufacturing Fully recycling waste, 
important for maximizing both manufacturers’ and consumers’ interests Fast remanufacturing decision. 

356



J. Leng et al.                                                                                                                                                                                     J  o  u r  n  a l  o  f  M   a  n  u f a  c  t u  r i n  g  S  y  s t e m   s 73 (2024) 349–363

networks. Because neural networks play a key role in AI, the parallel manufacturing, social manufacturing is a new industrial paradigm. 
computing power of GPU can accelerate the training and reasoning Through CPSS, various communities can form complex dynamic 
process of neural networks. GPU’s high-performance parallel computing autonomous systems to jointly create individualized products and ser
can process multiple data points at the same time, providing faster vices. CPSS could empower IndAI to realize group-centered intelligent 
training and reasoning speed, thus accelerating the response time of AI recommendations [93]. CPSS could be also designed to empower IndAI 
applications. In general, CPU is suitable for general AI computing tasks, to provide high-quality active and personalized services for humans 
while the GPU is suitable for graphics and large-scale parallel AI [94]. 
computing tasks [77]. This collaboration enables AI applications to run Both HCPS and CPSS provide services around people, reflecting the 
and process large amounts of data more efficiently, improving overall human-oriented idea. To some extent, HCPS and CPSS are mutually 
computational performance and efficiency. explicable. HCPS takes humans as a bridge and cooperates with humans 

The development of CPU/GPU hardware is the basis of AI deep ap through IndAI to facilitate symbiotic deep human-machine collaborative 
plications [78]. Due to the influence of structure and other factors, CPU work for intelligent manufacturing. CPSS extends this focus on people to 
will produce a lot of heat during operation, which will affect the oper the social level, incorporates social organizations into the system, and 
ation efficiency of AI [79]. Therefore, the thermal management system enables resources to be deeply developed and utilized. In the integration 
of CPU is challenging [80]. To improve its operating efficiency, for of HCPS/CPPS with IndAI, there are still some potential challenges on 
example, Arafa et al. [81] proposed an extensible and accurate simula the security and privacy concerns to be solved before unlocking the 
tion framework that enables GPU code developers and architects to power of IndAI. 
accurately predict the performance of applications on different GPU 
architectures. To make full use of GPU’s powerful 2D/3D 3.3.3. Metaverse 
hardware-accelerated graphics rendering performance or parallel Industry 5.0 attaches importance to the development of the work
computing potential, Tan et al. [82] proposed a multi-channel GPU force and will create more jobs in the areas of intelligent systems, AI, 
virtualization architecture, established the corresponding credit allo human-robot collaboration, behavior operation analysis, predictive 
cation and transfer mechanism model, and redesigned the virtual maintenance, and the design/training/scheduling/reuse of cobots/ro
multi-channel GPU fair scheduling algorithm. To make full use of the bots [95]. New skills emerge, including robot assistant, machine pro
available heterogeneous hardware, Chrysogelos et al. [83] introduced gramming, robot managing, cyber-physical systems analysis, 
hetexchange, a parallel query execution framework, which encapsulates collaborative operating, and virtual operating. This means that the 
the heterogeneous parallelism of modern multi-CPU-multi-GPU servers importance of worker education and training systems will be raised to a 
and supports the parallelism of existing sequential relational operators. new level [96], in which augmented reality and metaverse technologies 

In general, the rational use, architecting, and coordinating of CPU could be used to provide risk-free training for the workforce, which 
and GPU is challenging to improve the performance and response speed accelerates the growth of workers. 
of IndAI for specific industrial applications. Augmented Reality (AR) combines and interacts with the virtual 

space with the real-world scene through actuarial calculation and image 
3.3.2. Human-cyber-physical systems analysis. AR is currently mainly used in product assembly and mainte

The blueprint of Industry 5.0 places humans as the center of the nance. For the maintenance of relatively concealed parts such as aircraft 
manufacturing system, in which the human-cyber-physical system wheels [97], it is impossible to photograph clear damaged parts for 
(HCPS) and cyber-physical-social system (CPSS) play important roles. professional engineers to identify. The AR remote maintenance can be 
From the interaction aspect, HCPS enhances workers’ abilities to quickly identified and specific maintenance work can be started. 
interact with machines via intelligent human-machine interfaces and Compared with the traditional method, it reduces maintenance time, 
techniques designed to adapt to the workers’ cognitive and physical reduces transportation costs, and improves maintenance efficiency. 
requirements. From the cognition aspect, HCPS enhances workers’ Projector-based spatial AR systems in quality assurance could improve 
physical-, sensing- and cognitive- capabilities via wearable devices [84]. the accuracy of positioning in machining [98]. Cloud computing-based 
Operators in HCPS could be integrated into flexible manufacturing AR could empower IndAI for predictive maintenance [99]. Even as AR 
processes and outlined what kind of HCPS-based infrastructure should matures, it still faces some challenges. The ergonomic design of the AR 
be designed to enhance workers’ efficiency in production systems [85]. system should enable users to achieve a high level of satisfaction and 
The next generation of HCPS for intelligent manufacturing is supposed avoid long-term visual and neck fatigue. Since AR equipment is usually 
to make the role of humans more prominent and to form the in direct contact with the human body during use, its safety must be 
human-machine symbiosis form [86]. improved during human-machine collaboration. 

As an enabler of HCPS, digital twin simulates, verifies, predicts, and The metaverse is regarded as the ultimate form of the Internet. The 
controls the lifecycle process of physical systems based on real-time data virtual world coexists with the real world. Virtual users can obtain the 
analytics, and finally realizes an optimal closed-loop for intelligent same interactive experience as in reality, and the virtual world also has 
decision-making. Digital Twin provides runtime and real-time data its economic systems. Virtual users can also conduct economic man
support to the IndAI models. In the industry, digital twin-empowered agement in the virtual world. Metaverse aligns with the vision of Web 
IndAI applications usually focus on improving system design, configu 4.0, representing a digital ecosystem where individuals and organiza
ration, and operation optimization. In the system design stage, digital tions collaborate in a human-centric approach to create personalized 
twins could empower IndAI for the individualized design of the struc value [100,101]. At present, the metaverse has great application pros
ture, behavior, control, and performance model of smart manufacturing pects in biology [102] and tourism [103]. Metaverse may be simply 
systems [87]. In the system configuration stage, digital twins could defined as Persistent Virtual Reality in a narrow sense, and the advanced 
empower IndAI for rapid semi-physical commissioning and controlling stage and long-term vision of Digital Transformation in a broad sense. 
of smart manufacturing systems [88,89]. In the system operation stage, The excellent performance of the metaverse in virtual space accelerates 
digital twins could empower IndAI for equipment health management the personalized value creation of the manufacturing industry and 
[90], as well as remaining useful life prediction [91]. By empowering makes Industry 5.0 possible [104]. Their standards, architecture pat
digital twins with intelligence, the status of the equipment can be terns, communication protocols, data processing, reliability, and inte
summarized to provide a basis for the rational arrangement of operation gration with IndAI models will be the focus of subsequent research when 
and maintenance. unlocking their power. 

CPSS emphasizes the social dimension [92]. In the case of more open 
manufacturing models and growing demand for individualized 

357



J. Leng et al.                                                                                                                                                                                     J  o  u r  n  a l  o  f  M   a  n  u f a  c  t u  r i n  g  S  y  s t e m   s 73 (2024) 349–363

3.3.4. Secure multi-party computation flexibility [118]. It is challenging to simultaneously balance the safety, 
Secure Multi-Party Computation (SMPC) uses the Internet as the reliability, flexibility, and other performance of the HRC. 

carrier to realize the on-demand acquisition of secure computing re
sources for distributed data. SMPC in the industry is usually architected 4. Challenges and research directions for unlocking the power of 
in a cloud-edge orchestration manner [105]. The cloud-side computing IndAI 
performs the costly large-scale IndAI model training, while edge-side 
computing executes the simple reasoning in IndAI algorithms to As Industry 5.0 is still in the theoretical concept stage, there will be a 
improve efficiency [106], resource utilization[107], and accuracy long time for the coexistence and interplay of Industry 4.0 and Industry 
[108]. Intelligent resource allocation schemes in SMPC are critical to 5.0. As shown in Fig. 6, there are many social barriers and technology 
adaptively allocate computing and networking resources for reducing challenges to properly selecting, designing, deploying, using, and 
the average service time [109]. SMPC not only improves decision updating various IndAI models/algorithms in practice for unlocking the 
quality via the cloud but also speeds up decisions on the edge. power of IndAI. This section ends with a gathering of future research 

The security and privacy of computing in the cloud is an urgent directions for unlocking the power of IndAI toward Industry 5.0. 
problem to be solved. Blockchain is essentially a decentralized secure 
computing paradigm that could be used to enable reliable SMPC to 4.1. Social barrier 
realize product lifecycle management. The tamper-proofing ability of 
blockchain is usually used to establish an authenticity verification Currently, many manufacturers have not yet fully implemented In
network for the distributed production, circulation, and consumption of dustry 4.0 technologies, especially in small and medium-sized enter
products to improve credibility and trustiness [110,111]. Scholars used prises (SMEs) or across the value chain. To promote the Industry 5.0 
blockchain to reshape the industrial IoT to improve the security and vision, the reorganization of IndAI technologies must be widely imple
privacy of data in the information interaction in collaborative design mented across the industry or in SMEs. Broader integration of associa
and manufacturing to achieve trusted cooperation between the manu tions and representatives from the industry is needed to further refine 
facturer, the designer, and the customers [112]. The traceability of spare the IndAI model design, selection, and implementation. 
parts and product quality in industries is much more complex than the IndAI for Industry 5.0 emphasizes the characteristics of human- 
traceability of goods in the supply chain. Industrial blockchain appli centricity, sustainability, and resilience. This means that IndAI will 
cation is still in the preliminary exploration stage in the traceability of work around workers, take humans as the center, and give full play to a 
industrial product quality. Integration self-organizing multi-agent sys human subjective initiative to improve industrial production capacity 
tem with blockchain at the edge of SMPC enables autonomous and enhance value and interests. The needs of workers of different oc
decision-making and distributed cooperation among agents with high cupations, identities, and ages are inconsistent, and the values they 
efficiency [113]. Data in blockchained SMPC applications are usually of pursue and the opinions they consider are also very different. The value 
high quality and thereby could improve the accuracy of IndAI models in brought by new technologies cannot directly radiate to each part of 
the cloud since it has been verified by multiple participants. However, society. Reaching an agreement between society and the New Deal re
there are still many potential problems, such as transmission delay quires broad support from society. The concept of human-centricity is 
caused by the consensus algorithms, which is a significant challenge for thus extended to society-centricity, and the needs of individuals are 
ensuring the security of IndAI while unlocking its full potential. supplemented by the needs of society. The individual needs of em

ployees must be coordinated with the needs of employers and the entire 
3.3.5. Collaborative robots and reconfigurable executors workforce of society. However, for many enterprises, economic perfor

The design of physical infrastructures such as robots is increasingly mance is the main goal of technology implementation. How to syn
coupled with the IndAI models. In the manufacturing paradigm evolu chronize the values of enterprises and social values is a challenge. It calls 
tion from mass production to mass individualization, reconfigurable and for the recommended practice, policy, standard, and reference archi
flexible manufacturing technologies such as reconfigurable collabora tecture to actively promote proper IndAI applications to industries, 
tive robots started to emerge in the industry. An industrial robot with which are supposed to guide on the following issues: 1) Who using 
sensors and controllers can autonomously complete various individu IndAI, 2) Why using IndAI, 3) Where to use IndAI, 4) What to establish 
alized manufacturing tasks (e.g., welding, assembly, and picking) with IndAI, 5) When to implement IndAI, and 6) How to design and operate 
high durability, high speed, and high precision while coping with the IndAI. 
uncertainty of human interaction and environments [114]. In In addition, implementing IndAI may suffer from two aspects of 
man-machine cooperative operation, the motion control of a robot needs ethics issues. The first ethical issue is that IndAI algorithms are often 
to be limited and centered on human safety when maximizing produc encapsulated as black boxes in use. Defects or incorrect values of the 
tivity [115]. Also, incorporating IndAI into the motion control of a robot algorithm may trigger biased, harmful, and misleading traps [119]. For 
should ensure the boundedness of the system’s state variables and thus example, recommendation IndAI algorithms may tend to advertise the 
enhance the stability of the system [37]. equipment of a certain manufacturer, resulting in a monopoly. The al

Industrial robots usually need to rely on fixed external environments. gorithm of human-machine collaboration may become a way for capi
However, this kind of deployment needs a lot of material and financial talists to manipulate the value of workers. AIGC algorithms may 
resources. When the production line changes, the industrial robot also generate content that contains inaccurate operational guidelines, lead
needs to be redeployed, which is costly. Collaborative robots, which can ing to the occurrence of hazardous accidents. The second ethical issue is 
interact directly with people in collaborative areas, have the ability of the privacy risk [119]. Besides the privacy leaking caused by illegal data 
rapid deployment and low comprehensive cost than traditional indus attacks, with the further development of intelligent sensing technolo
trial robots. Human-robot collaboration (HRC) is identified as a key gies, workers’ emotions may be monitored, and deep-seated biological 
element of Industry 5.0. Adaptive control methods can enhance the data may be captured, which will infringe on workers’ privacy. In 
flexibility of robots to humans and the environment, and reduce task- addition, while blockchain brings immutability of data, it also brings 
related preprogramming [116]. In HRC, the efficiency of the interac unforgettability of data. Human past experiences and machine operation 
tion between humans and robots will affect the overall work efficiency. records can be accessed, analyzed, and monitored at any time, leading to 
Intelligent human-robot task allocation methods are supposed to allo a lack of social boundaries in the human world and the leakage of core 
cate the sequential tasks of robots and operators in different workspaces processes in manufacturing. 
to reduce the waste of resources [117]. Digital twins could be estab Possible pathways to deal with the mentioned ethical challenges 
lished for human-robot cooperative systems to enhance operation include three aspects. The first one is to identify the right fundamental 

358



J. Leng et al.                                                                                                                                                                                     J  o  u r  n  a l  o  f  M   a  n  u f a  c  t u  r i n  g  S  y  s t e m   s 73 (2024) 349–363

Fig. 6. Barriers and challenges in IndAI.  

framework, principles, and guidelines to ensure the lifecycle ethical production control, the coexistence of multi-variable factors, nonline
management (e.g., design, regulation, and use) of IndAI to benefit in arity, large delays, under-regulation, and intermittent/continuous con
dividuals, societies, and the environment [120]. Establishing new trol amplifies the complexity. Abnormal operating conditions are 
models to ascribe moral responsibility distributed among designers and extremely difficult to detect and diagnose in the early stage, and the 
users of IndAI is essential, and ethical analyses must be extended to increasingly open industrial system leads to increased system security 
account for the invisible influence exercised by IndAI on human risks. 
behavior [121]. The second one is to advance technologies such as Also, acceptance and trust in technology are crucial. Under the 
explainable IndAI, interpretable IndAI, robust IndAI, responsible IndAI, human-centered idea, IndAI should work with people. In the case of this 
differential privacy, federated learning, and homomorphic encryption to high degree of human-machine integration, IndAI technology must 
enhance transparency, fairness, non-maleficence, responsibility, and improve its interpretability and autonomous planning ability. IndAI 
accountability. The third pathway is a legal approach to regulate the must have a certain understanding of workers’ behavior to better 
research and application of IndAI through legislation, standards, and cooperate and avoid some errors that may cause harm. 
mandatory comprehensive evaluation. Also, Industry 5.0 claims to be a Sustainability is a long-term development and a key issue in Industry 
human-centric paradigm, and thereby we as humans should apply the 5.0. In the long run, society should not ignore the earth’s ecology and 
right governance before, during, and post the implementation of the must protect the earth’s ecology while keeping industrial development. 
IndAI [121]. This requires cross-field research in combination between IndAI and 

nanotechnology or smart material technology to achieve environmental 
goals such as carbon dioxide neutralization. IndAI models are supposed 

4.2. Technology challenges to be able to make full use of traceability and recycling technologies to 
obtain product footprint labels so that energy can be fully utilized to 

From the production control perspective, it is challenging to achieve meet the requirements of sustainable development. 
a wide as well as deep synergy across various professions, domains, and 
functions. The reason is that the critical operation information and 
important process parameters are difficult to obtain, resulting in 4.3. Research directions 
incomplete process information and even failure of mechanism models. 
The relationship between the process state and the overall production IndAI needs an integrated technological, organizational, policy- 
goal of the whole process is complicated, so it is difficult to describe the making, and security informatics solution. In industry, the simple pur
essential characteristics of an unsteady state and nonlinearity. Within suit of more advanced AI is not what we want to emphasize at the 

359



J. Leng et al.                                                                                                                                                                                     J  o  u r  n  a l  o  f  M   a  n  u f a  c  t u  r i n  g  S  y  s t e m   s 73 (2024) 349–363

moment. To further provide insights for designing appropriate models Blockchained privacy-preserving data-sharing mechanisms could 
and algorithms to unlock the power of IndAI in the process of digital enhance the security of federated intelligence. Security enhancement 
transformation and upgrading of the industry, future directions are that deeply integrates functional security and information security 
gathered based on value-oriented awareness as well as a systematic should be performed to form a comprehensive predictable and highly 
understanding of IndAI technologies (Fig. 7). reliable technical system of risk assessment, vulnerability analysis, 

vulnerability mining, countermeasure protection, health diagnosis, and 
4.3.1. Rapid response and reliability monitoring of industrial systems. 

Along with the operation of IndAI algorithms, the surge of data has 
brought a huge burden to servers and networks. It faces the risk of delay 4.3.3. System adaptability 
and latency [122]. To alleviate this situation, edge intelligence [123] Adaptability is a kind of ability to cross professional boundaries and 
has been gradually studied and applied. The intelligence at the edge of be competent for critical applications. It can deeply integrate complex 
industrial systems is improved to optimize resource allocation and solve mechanism characteristics and dynamic changing environment to deal 
problems characterized by diversity and time variability. Three di with strong coupling, nonlinear, large time delay, and harsh constraints, 
rections to improve the rapidity of IndAI systems could be concluded as and carry out real-time dynamic decision-making while ensuring the 
follows: 1) How to synthesize cognitive information/matter/energy system stability, controllability, optimality, and robustness. The adapt
flows and their interaction mechanisms in real time? 2) How to model ability of IndAI models is reflected in three aspects, namely, model 
the multi-scale correlation and establish the multi-spatial and temporal interaction, hardware/software adaptation, and data/task adaptation of 
panoramic features of industrial systems? and 3) How to solve the algorithms. 
cooperative regulation under complex constraints to achieve efficient In terms of interaction between models, a variety of learning 
comprehensive optimization? frameworks/paradigms were designed to implement practical IndAI 

In addition, edge devices are also vulnerable to malicious nodes, and applications, and the underlying implementation technologies of each 
it is a great challenge to ensure the security of edge services. Through the framework are different, resulting in difficulties in mutual conversion 
large-scale, ubiquitous, and networked deployment of detection and between IndAI models. A direct model transformation is usually more 
control systems, a sharing and coordination mechanism that integrates complex than the development of a general framework, involving the 
across time, space, system levels, and borders could be formed. A highly inherent characteristics of the industrial field [129]. 
permeable, flexible, reconfigurable, and community-based perception The second is software/hardware adaptation. The development of 
and regulation network could be established. Integrating edge intelli CPU and software frameworks is different, which leads to the mismatch 
gence with blockchain authorization could achieve flexible and secure between the underlying hardware infrastructure and the software 
edge service management [124]. Distributed deep learning could also be framework, making IndAI algorithms often encounter some inexplicable 
established for attack detection on edge devices to improve system errors. Therefore, software framework developers and CPU manufac
stability and reliability [125]. turers need to ensure good software/hardware compatibility. A compiler 

for IndAI algorithms/models is needed to solve the adaptation and 
4.3.2. Security in a distributed computing context portability between different software frameworks and different hard

Industrial data usually exists in the form of distributed silos, and ware devices. However, there is no uniform standard for such compilers, 
direct data exchange between silos is difficult due to security and pri and the competition among hardware manufacturers in the middle 
vacy issues. The emergence of secure multi-party computing, verifiable presentation layer has also become an obstacle to the practical appli
computing, and federated learning [126] provides a secure solution to cation of IndAI technologies. 
this problem. Federated learning-based AI (here it is defined as federated The third is data/task adaptation. At present, IndAI algorithms 
intelligence) can train IndAI models based on distributed encrypted usually rely on a large number of labeled data for training. With the 
datasets without having to centralize all data to a central storage node. gradual acceleration of the penetration of AI and industrial integration, 
Federated intelligence allows knowledge sharing without compromising more and more application scenarios are facing the problem of “small 
user privacy. However, federal intelligence cannot fully guarantee the data”. In addition, due to the differentiation of industrial equipment 
security of data [127]. By sharing encrypted data, adversaries can still products, scenarios, and the diversity of tasks, the replicability of IndAI 
attack it, destroying its security and causing information leakage [128]. models in current industrial scenarios is poor, such as fault diagnosis in 

Fig. 7. Research directions of IndAI.  

360



J. Leng et al.                                                                                                                                                                                     J  o  u r  n  a l  o  f  M   a  n  u f a  c  t u  r i n  g  S  y  s t e m   s 73 (2024) 349–363

industrial scenarios. The types of defects in different production lines Acknowledgments 
and different products may be completely different. Efficient algorithms 
or solutions may be obtained in one enterprise, but they perform poorly This work was supported by the National Key Research and Devel
when being transferred to another enterprise. opment Program of China under Grant No. 2022YFF0606005; the Na

The adaptability may also originate from the active integration of tional Natural Science Foundation of China under Grant No. 52075107 
IndAI models with industrial processes, equipment, material, and and U20A6004; and the Natural Science Fund of Guangdong Province 
structural design in the design and development of the IndAI system. In under Grant No. 2022B1515020006. 
response to changes in tasks, environment, systems’ characteristics, and 
even value system changes, adaptability is enhanced by a constantly References 
continuous self-evolving and enhancement mechanism via deep pro
cessing of information, real-time dynamic feedback, system optimiza [1] J. Cotta, M. Breque, L. De Nul, A. Petridis, Industry 5.0 - Towards a sustainable, 

tion decision-making, and forward-looking global response. human-centric and resilient European industry. 〈https://op.europa.eu/en/publi 
cation-detail/-/publication/468a892a-5097–11eb-b59f-01aa75ed71a1/〉, 2021. 

[2] Xu X, Lu Y, Vogel-Heuser B, Wang L. Industry 4.0 and Industry 5.0—inception, 
4.3.4. Interpretability and robustness conception and perception. J MANUF SYST 2021;61:530–5. 

Many existing IndAI models are “black box” that lacks interpret [3] Maddikunta PKR, Pham Q, Deepa PBN, Dev K, Gadekallu TR, Ruby R, 
Liyanage M. Industry 5.0: a survey on enabling technologies and potential 

ability [130]. At present, although neural networks have shown good applications. J IND INF INTEGR 2022;26:100257. 
results on complex problems, “connectionism” represented by neural [4] Lee J, Davari H, Singh J, Pandhare V. Industrial Artificial Intelligence for industry 
networks cannot provide a clear semantic explanation [131]. Almost all 4.0-based manufacturing systems. MANUF LETT 2018;18:20–3. 

[5] Zhang M, Tao F, Zuo Y, Xiang F, Wang L, Nee AYC. Top ten intelligent algorithms 
deep learning breakthroughs are essentially curve-fitting [132]. Since towards smart manufacturing. J MANUF SYST 2023;71:158–71. 
operators are not clear about their operating mechanism and the reasons [6] Shojaeinasab A, Charter T, Jalayer M, Khadivi M, Ogunfowora O, Raiyani N, 
for making wrong decisions, there may be problems in adopting this Yaghoubi M, Najjaran H. Intelligent manufacturing execution systems: A 

systematic review. J MANUF SYST 2022;62:503–22. 
model in key and sensitive areas [133]. The solution must be reliable [7] Wang J, Xu C, Zhang J, Zhong R. Big data analytics for intelligent manufacturing 
and robust, that is, the mechanism behind it needs to be clearly systems: a review. J MANUF SYST 2022;62:738–52. 
explained [134]. It is of great significance to systematically summarize [8] Kim YG, Lee S, Son J, Bae H, Chung BD. Multi-agent system and reinforcement 

learning approach for distributed intelligence in a flexible smart manufacturing 
and visualize the features learned by IndAI models and how these fea system. J MANUF SYST 2020;57:440–50. 
tures interact to predict [135]. It may be concluded into three aspects to [9] Uhlmann IR, Frazzon EM. Production rescheduling review: Opportunities for 
achieve this goal: 1) Modeling mechanisms that can be interpreted, industrial integration and practical applications. J MANUF SYST 2018;49: 

extrapolated, and updated; 2) Large-scale dynamic, multi-objective, 186–93. 
[10] Pan Y. Heading toward Artificial Intelligence 2.0. Eng-PRC 2016;2:409–13. 

strong constraint decision-making mechanism; and 3) Man-machine [11] Zhang X, Ming X, Liu Z, Yin D, Chen Z, Chang Y. A reference framework and 
integration and progressive technological evolution mechanism. overall planning of industrial artificial intelligence (I-AI) for new application 

scenarios. Int J Adv Manuf Technol 2019;101:2367–89. 
[12] Peres RS, Jia X, Lee J, Sun K, Colombo AW, Barata J. Industrial artificial 

5. Concluding remarks intelligence in industry 4.0 - systematic review, challenges and outlook. IEEE 
ACCESS 2020;8:220121–39. 

[13] J. Beyerer, A. Maier, O. Niggemann, Proposal for requirements on industrial AI 
This perspective article presents a classification of IndAI based on the solutions, Springer Berlin / Heidelberg, Germany, 2020. 

intelligence levels (i.e., Sharable IndAI, Autonomous IndAI, Learnable [14] Yang T, Yi X, Lu S, Johansson KH, Chai T. Intelligent manufacturing for the 
IndAI, Knowledgeable IndAI, and Reactive IndAI) and gives four prin process industry driven by industrial artificial intelligence. Eng-PRC 2021;7: 

1224–30. 
ciples for implementing IndAI, which provides the guide for designing [15] Mathew D, Brintha NC, Jappes JTW. Artificial Intelligence Powered Automation 
and implementing appropriate models and algorithms in practice. Three for Industry 4.0, New Horizons for Industry 4.0 in Modern Business. Cham: 
significant opportunities of IndAI, namely, collaborative intelligence, Springer,; 2023. p. 1–28. 

self-learning intelligence, and crowd intelligence, towards Industry 5.0 [16] Viola J, Chen Y. Smart Control Engineering Enabled by Digital Twin, Digital- 
Twin-Enabled Smart Control Engineering. Cham: Springer; 2023. p. 73–102. 

vision are identified to promote the transition from a technology-driven [17] Rozanec JM, Novalija I, Zajec P, Kenda K, Ghinani HT, Suh S, Veliou E, 
initiative in Industry 4.0 to the coexistence and interplay of Industry 4.0 Papamartzivanos D, Giannetsos T, Menesidou SA, Alonso R, Cauli N, Meloni A, 
and a value-oriented proposition in Industry 5.0. Pathways of IndAI Recupero DR, Kyriazis D, Sofianidis G, Theodoropoulos S, Fortuna B, MladeniC D, 

Soldatos J. Human-centric artificial intelligence architecture for industry 5.0 
applications in Industry 4.0 are discussed in five dimensions, namely, applications. INT J PROD RES 2023;61:6847–72. 
design, manufacturing, marketing and logistics, operation and mainte [18] Liu F, Shi Y, Liu Y. Intelligence quotient and intelligence grade of artificial 
nance service, and recycling and remanufacturing. Future research di intelligence. Ann Data Sci 2017;4:179–91. 

[19] Rajani S. Artificial intelligence-man or machine. Int J Inf Technol Knowl Manag 
rections of IndAI are identified as four aspects, rapid response and 2011;4:173–6. 
reliability, security in a distributed computing context, adaptability, and [20] Morris MR, Sohl-dickstein J, Fiedel N, Warkentin T, Dafoe A, Faust A, Farabet C, 
interpretability and robustness. This perspective article is a reflection of Legg S. Levels of AGI: operationalizing progress on the path to AGI (arXiv.org). 

Ithaca: Cornell University Library,; 2023. 
significant conceptual and technical advances in unlocking the power of [21] Leng J, Sha W, Wang B, Zheng P, Zhuang C, Liu Q, Wuest T, Mourtzis D, Wang L. 
IndAI in this junction of dramatic development of Industry 4.0 and In Industry 5.0: Prospect and retrospect. J MANUF SYST 2022;65:279–95. 
dustry 5.0. We hope that our effort lays a strong foundation for making [22] Ghobakhloo M, Iranmanesh M, Mubarak MF, Mubarik M, Rejeb A, Nilashi M. 

Identifying industry 5.0 contributions to sustainable development: A strategy 
IndAI research and engineering more sustainable, resilient, and human- roadmap for delivering sustainability values. SUSTAIN PROD CONSUMP 2022; 
centric. 33:716–37. 

[23] Wilson HJ, Daugherty PR. Collaborative intelligence: humans and AI are joining 
forces. Harv BUS REV 2018;96:114–23. 

[24] Epstein SL. Wanted: collaborative intelligence. ARTIF INTELL 2015;221:36–45. 
Declaration of Competing Interest [25] Fogel DB, Hays TJ, Hahn SL, Quon J. A self-learning evolutionary chess program. 

P IEEE 2004;92:1947–54. 
The authors declare that they have no known competing financial [26] Li W, Wu W, Wang H, Cheng X, Chen H, Zhou Z, Ding R. Crowd intelligence in AI 

2.0 era. FRONT INFORM TECH EL 2017;18:15–43. 
interests or personal relationships that could have appeared to influence [27] Ooi B, Tan K, Tran Q, Yip J, Chen G, Ling Z, Nguyen T, Tung A, Zhang M. 
the work reported in this paper. Contextual crowd intelligence. SIGKDD Explor 2014;16:39–46. 

[28] Leng J, Zhong Y, Lin Z, Xu K, Mourtzis D, Zhou X, Zheng P, Liu Q, Zhao JL, 

Data Availability Shen W. Towards Resilience in Industry 5.0: a decentralized autonomous 
manufacturing paradigm. J MANUF SYST 2023;71:95–114. 

[29] Montes GA, Goertzel B. Distributed, decentralized, and democratized artificial 
The data that support the findings of this study are available from the intelligence. TECHNOL FORECAST SOC 2019;141:354–8. 

corresponding author upon reasonable request. 

361



J. Leng et al.                                                                                                                                                                                     J  o  u r  n  a l  o  f  M   a  n  u f a  c  t u  r i n  g  S  y  s t e m   s 73 (2024) 349–363

[30] Yan X, Jia M. A novel optimized SVM classification algorithm with multi-domain [62] Guo L, Lei Y, Xing S, Yan T, Li N. Deep Convolutional Transfer Learning Network: 
feature and its application to fault diagnosis of rolling bearing. A New Method for Intelligent Fault Diagnosis of Machines With Unlabeled. Data, 
NEUROCOMPUTING 2018;313:47–64. IEEE T IND ELECTRON 2019;66:7316–25. 

[31] Mehmood A, Mukherjee M, Ahmed SH, Song H, Malik KM. NBC-MAIDS: Naïve [63] Lei Y, Jia F, Lin J, Xing S, Ding SX. An Intelligent Fault Diagnosis Method Using 
Bayesian classification technique in multi-agent system-enriched IDS for securing Unsupervised Feature Learning Towards Mechanical. Big Data, IEEE T IND 
IoT against DDoS attacks, The. J Supercomput 2018;74:5156–70. ELECTRON 2016;63:3137–47. 

[32] Achlerkar PD, Samantaray SR, Sabarimalai Manikandan M. Variational mode [64] Zhou L, Jiang Z, Geng N, Niu Y, Cui F, Liu K, Qi N. Production and operations 
decomposition and decision tree based detection and classification of power management for intelligent manufacturing: a systematic literature review. INT J 
quality disturbances in grid-connected distributed generation system. IEEE T PROD RES 2022;60:808–46. 
SMART GRID 2018;9:3122–32. [65] Reimann M, Xiong Y, Zhou Y. Managing a closed-loop supply chain with process 

[33] Luo X, Li D, Yang Y, Zhang S. Spatiotemporal Traffic Flow Prediction with KNN innovation for remanufacturing. EUR J OPER RES 2019;276:510–8. 
and LSTM. J ADV Transp 2019;2019:1–10. [66] Xu L, Wang C. Sustainable manufacturing in a closed-loop supply chain 

[34] Wang K, Qi X, Liu H, Song J. Deep belief network based k-means cluster approach considering emission reduction and remanufacturing. Resour, Conserv Recycl 
for short-term wind power forecasting. ENERGY 2018;165:840–52. 2018;131:297–304. 

[35] Quiroz JC, Mariun N, Mehrjou MR, Izadi M, Misron N, Mohd MA. Radzi, Fault [67] Taleizadeh AA, Moshtagh MS, Moon I. Pricing, product quality, and collection 
detection of broken rotor bar in LS-PMSM using random forests. Measurement optimization in a decentralized closed-loop supply chain with different channel 
2018;116:273–80. structures: Game theoretical approach. J CLEAN PROD 2018;189:406–31. 

[36] Wang Y, Ma X, Qian P. Wind turbine fault detection and identification through [68] Saboori A, Aversa A, Marchese G, Biamino S, Lombardi M, Fino P. Application of 
pca-based optimal variable selection. IEEE T SUSTAIN ENERG 2018;9:1627–35. Directed Energy Deposition-Based Additive Manufacturing in Repair. Appl Sci 

[37] He W, Yan Z, Sun Y, Ou Y, Sun C. Neural-learning-based control for a constrained 2019;9:3316. 
robotic manipulator with flexible. Jt, IEEE T NEUR NET LEAR 2018;29: [69] Yang Y, Okonkwo EG, Huang G, Xu S, Sun W, He Y. On the sustainability of 
5993–6003. lithium ion battery industry – A review and perspective. ENERGY STORAGE 

[38] Leng J, Lin Z, Huang Z, Ye R, Liu Q, Chen X. Rapid simplification of 3D geometry MATER 2021;36:186–212. 
model of mechanisms in the digital twins-driven manufacturing system design. [70] Ju J, Feng Y, Li H, Xu C, Xue Z, Wang B. Extraction of valuable metals from 
J INTELL MANUF 2023. minerals and industrial solid wastes via the ammonium sulfate roasting process: A 

[39] Rao RV, Pawar RB. Constrained design optimization of selected mechanical systematic review. CHEM ENG J 2023;457:141197. 
system components using Rao algorithms. Appl Soft Comput 2020;89:106141. [71] Bag S, Gupta S, Kumar S. Industry 4.0 adoption and 10R advance manufacturing 

[40] Li W, Li C, Gao L, Xiao M. Risk-based design optimization under hybrid capabilities for sustainable development. INT J PROD ECON 2021;231:107844. 
uncertainties. ENG COMPUT-Ger 2022;38:2037–49. [72] Kerin M, Pham DT. A review of emerging industry 4.0 technologies in 

[41] Leng J, Wang D, Shen W, Li X, Liu Q, Chen X. Digital twins-based smart remanufacturing. J CLEAN PROD 2019;237:117805. 
manufacturing system design in Industry 4.0: a review. J MANUF SYST 2021;60: [73] Rui H, Gao C. Fuzzy programming model and its application of the optimization 
119–37. design for smart home system. SYST SCI CONTROL ENG 2019;7:171–8. 

[42] Cao X, Zhao G, Xiao W. Digital Twin–oriented real-time cutting simulation for [74] Mokhtari H, Hasani A. An energy-efficient multi-objective optimization for 
intelligent computer numerical control machining. Proc Inst Mech Eng, Part B: J flexible job-shop scheduling problem. COMPUT CHEM ENG 2017;104:339–52. 
Eng Manuf 2022;236:5–15. [75] Lu C, Gao L, Li X, Pan Q, Wang Q. Energy-efficient permutation flow shop 

[43] Xie Z, Jin L, Luo X, Sun Z, Liu M. RNN for repetitive motion generation of scheduling problem using a hybrid multi-objective backtracking search 
redundant robot manipulators: an orthogonal projection-based scheme. IEEE T algorithm. J CLEAN PROD 2017;144:228–38. 
NEUR NET LEAR 2022;33:615–28. [76] Mittal S, Rajput P, Subramoney S. A Survey of Deep Learning on CPUs: 

[44] Leng J, Chen Z, Sha W, Lin Z, Lin J, Liu Q. Digital twins-based flexible operating Opportunities and Co-Optimizations. IEEE T NEUR NET LEAR 2022;33: 
of open architecture production line for individualized manufacturing. ADV ENG 5095–115. 
Inf 2022;53:101676. [77] J. J, D. M, J. H. Billion-Scale Similarity Search with GPUs. IEEE T BIG DATA 

[45] Gao D, Wang G, Pedrycz W. Solving fuzzy job-shop scheduling problem using de 2021;7:535–47. 
algorithm improved by a selection mechanism. IEEE T FUZZY SYST 2020;28: [78] Biggs J, Myers J, Kufel J, Ozer E, Craske S, Sou A, Ramsdale C, Williamson K, 
3265–75. Price R, White S. A natively flexible 32-bit Arm microprocessor. NATURE 2021; 

[46] Zhang H, Qi Q, Tao F. A multi-scale modeling method for digital twin shop-floor. 595:532–6. 
J MANUF SYST 2022;62:417–28. [79] Siricharoenpanich A, Wiriyasart S, Srichat A, Naphon P. Thermal management 

[47] Prakash V, Savaglio C, Garg L, Bawa S, Spezzano G. Cloud- and Edge-based ERP system of CPU cooling with a novel short heat pipe cooling system, CASE STUD. 
systems for Industrial Internet of Things and Smart. Fact, Procedia Comput Sci THERM ENG 2019;15:100545. 
2022;200:537–45. [80] Wang Y, Wang B, Zhu K, Li H, He W, Liu S. Energy saving potential of using heat 

[48] Barenji AV, Guo H, Wang Y, Li Z, Rong Y. Toward blockchain and fog computing pipes for CPU cooling. APPL THERM ENG 2018;143:630–8. 
collaborative design and manufacturing platform: Support customer view. [81] Arafa Y, Badawy AA, Chennupati G, Santhi N, Eidenbenz S. PPT-GPU: Scalable 
ROBOT CIM-INT MANUF 2021;67:102043. GPU performance modeling. IEEE COMPUT ARCHIT L 2019;18:55–8. 

[49] Wolniak R. Main functions of operation management, PROD ENG. ARCH 2020; [82] Tan H, Tan Y, He X, Li K, Li K. A virtual multi-channel GPU fair scheduling 
26:11–4. method for virtual machines. IEEE T PARALL DISTR 2019;30:257–70. 

[50] Ruiz R, Pan Q, Naderi B. Iterated Greedy methods for the distributed permutation [83] Chrysogelos P, Karpathiotakis M, Appuswamy R, Ailamaki A. HetExchange. PROC 
flowshop scheduling problem. OMEGA-INT J MANAGE S 2019;83:213–22. VLDB ENDOW 2019;12:544–56. 

[51] Li J, Sang H, Han Y, Wang C, Gao K. Efficient multi-objective optimization [84] D. Romero, P. Bernus, O. Noran, J. Stahre, A. Fast-Berglund, The Operator 4.0: 
algorithm for hybrid flow shop scheduling problems with setup energy Human Cyber-Physical Systems & Adaptive Automation Towards Human- 
consumptions. J CLEAN PROD 2018;181:584–98. Automation Symbiosis Work Systems, 2016. 

[52] Lu C, Gao L, Li X, Xiao S. A hybrid multi-objective grey wolf optimizer for [85] Ruppert T, Jaskó S, Holczinger T, Abonyi J. Enabling technologies for operator 
dynamic scheduling in a real-world welding industry. ENG APPL ARTIF INTEL 4.0: a survey. Appl Sci 2018;8:1650. 
2017;57:61–79. [86] Zhou J, Zhou Y, Wang B, Zang J. Human–cyber–physical systems (HCPSs) in the 

[53] Leng J, Lin Z, Zhou M, Liu Q, Zheng P, Liu Z, Chen X. Multi-layer parallel context of new-generation intelligent manufacturing. Eng-PRC 2019;5:624–36. 
transformer model for detecting product quality issues and locating anomalies [87] Liu Q, Leng J, Yan D, Zhang D, Wei L, Yu A, Zhao R, Zhang H, Chen X. Digital 
based on multiple time‑series process data in Industry 4.0. J MANUF SYST 2023; twin-based designing of the configuration, motion, control, and optimization 
70:501–13. model of a flow-type smart manufacturing system. J MANUF SYST 2021;58: 

[54] Caggiano A, Zhang J, Alfieri V, Caiazzo F, Gao R, Teti R. Machine learning-based 52–64. 
image processing for on-line defect recognition in additive manufacturing. CIRP [88] Leng J, Zhu X, Huang Z, Xu K, Liu Z, Liu Q, Chen X. ManuChain II: blockchained 
Ann 2019;68:451–4. smart contract system as the digital twin of decentralized autonomous 

[55] Tabernik D, Šela S, Skvarč J, Skočaj D. Segmentation-based deep-learning manufacturing towards resilience in Industry 5.0, IEEE Transactions on Systems. 
approach for surface-defect detection. J INTELL MANUF 2019;31:759–76. Man, Cyber: Syst 2023;53:4715–28. 

[56] Li S, Song X, Lu H, Zeng L, Shi M, Liu F. Friend recommendation for cross [89] Leng J, Zhou M, Xiao Y, Zhang H, Liu Q, Shen W, Su Q, Li L. Digital twins-based 
marketing in online brand community based on intelligent attention allocation remote semi-physical commissioning of flow-type smart manufacturing systems. 
link prediction algorithm. EXPERT SYST APPL 2020;139:112839. J CLEAN PROD 2021;306:127278. 

[57] Feng B, Ye Q. Operations management of smart logistics: a literature review and [90] Tao F, Zhang M, Liu Y, Nee AYC. Digital twin driven prognostics and health 
future research. FRONT ENG MANAG 2021;8:344–55. management for complex equipment. CIRP Ann 2018;67:169–72. 

[58] Jimenez VJ, Bouhmala N, Gausdal AH. Developing a predictive maintenance [91] Luo W, Hu T, Ye Y, Zhang C, Wei Y. A hybrid predictive maintenance approach 
model for vessel machinery. J OCEAN ENG SCI 2020;5:358–86. for CNC machine tool driven by Digital Twin. ROBOT CIM-INT MANUF 2020;65: 

[59] Wang Q, Bu S, He Z. Achieving predictive and proactive maintenance for high- 101974. 
speed railway power equipment With LSTM-RNN. IEEE T IND Inf 2020;16: [92] Yilma BA, Panetto H, Naudet Y. Systemic formalisation of Cyber-Physical-Social 
6509–17. System (CPSS): a systematic literature review. COMPUT IND 2021;129:103458. 

[60] Vianna WOL, Yoneyama T. Predictive Maintenance Optimization for Aircraft [93] Zhang Y. GroRec: a group-centric intelligent recommender system integrating 
Redundant Systems Subjected to Multiple Wear Profiles. IEEE SYST J 2018;12: social, mobile and big data technologies. IEEE T SERV COMPUT 2016;9:786–95. 
1170–81. [94] Wang X, Yang LT, Xie X, Jin J, Deen MJ, Cloud-Edge A. Computing framework for 

[61] Shao S, McAleer S, Yan R, Baldi P. Highly Accurate Machine Fault Diagnosis cyber-physical-social services. IEEE COMMUN MAG 2017;55:80–5. 
Using Deep Transfer Learning. IEEE T IND Inf 2019;15:2446–55. 

362



J. Leng et al.                                                                                                                                                                                     J  o  u r  n  a l  o  f  M   a  n  u f a  c  t u  r i n  g  S  y  s t e m   s 73 (2024) 349–363

[95] Huang S, Wang B, Li X, Zheng P, Mourtzis D, Wang L. Industry 5.0 and Society [114] Pedersen MR, Nalpantidis L, Andersen RS, Schou C, Bøgh S, Krüger V, Madsen O. 
5.0—Comparison, complementation and co-evolution. J MANUF SYST 2022;64: Robot skills for manufacturing: from concept to industrial deployment. ROBOT 
424–8. CIM-INT MANUF 2016;37:282–91. 

[96] Grabowska S, Saniuk S, Gajdzik B. Industry 5.0: improving humanization and [115] Zanchettin AM, Ceriani NM, Rocco P, Ding H, Matthias B. Safety in human-robot 
sustainability of Industry 4.0. SCIENTOMETRICS 2022;127:3117–44. collaborative manufacturing environments: Metrics and control. IEEE T AUTOM 

[97] Ceruti A, Marzocca P, Liverani A, Bil C. Maintenance in aeronautics in an industry SCI ENG 2016;13:882–93. 
4.0 context: the role of augmented reality and additive manufacturing. [116] Ajoudani A, Zanchettin AM, Ivaldi S, Albu-Schäffer A, Kosuge K, Khatib O. 
J COMPUT DES ENG 2019;6:516–26. Progress and prospects of the human–robot collaboration, AUTON. ROBOT 2017; 

[98] Doshi A, Smith RT, Thomas BH, Bouras C. Use of projector based augmented 42:957–75. 
reality to improve manual spot-welding precision and accuracy for automotive [117] Tsarouchi P, Matthaiakis A, Makris S, Chryssolouris G. On a human-robot 
manufacturing. Int J Adv Manuf Technol 2017;89:1279–93. collaboration in an assembly cell. INT J COMPUT INTEG M 2017;30:580–9. 

[99] Mourtzis D, Vlachou A, Zogopoulos V. Cloud-based augmented reality remote [118] Bilberg A, Malik AA. Digital twin driven human–robot collaborative assembly. 
maintenance through shop-floor monitoring: a product-service system approach. CIRP Ann 2019;68:499–502. 
J MANUF SCI E-T ASME 2017;(139 (). [119] Huang C, Zhang Z, Mao B, Yao X. An Overview of Artificial Intelligence Ethics. 

[100] Mourtzis D. The metaverse in industry 5.0: a human-centric approach towards IEEE Trans Artif Intell 2023;4:799–819. 
personalized value creation. Encyclopedia 2023;3:1105–20. [120] Taddeo M, Floridi L. How AI can be a force for good. SCIENCE 2018;361:751–2. 

[101] Mourtzis D. Digital twin inception in the Era of industrial metaverse. Front Manuf [121] A.C. Ciobanu, G. Meșniță, A.I. Ethics for Industry 5.0 – From Principles to 
Technol 2023;3:1155735. Practice, Proceedings of the Workshop of I-ESA’22, March 23–24, 2022, Valencia, 

[102] Rillig MC, Gould KA, Maeder M, Kim SW, Dueñas JF, Pinek L, Lehmann A, Spain., (2023). 
Bielcik M. Opportunities and Risks of the “Metaverse” For Biodiversity and the [122] Su W, Li L, Liu F, He M, Liang X. AI on the edge: a comprehensive review. ARTIF 
Environment. ENVIRON SCI TECHNOL 2022;56:4721–3. INTELL REV 2022. 

[103] Gursoy D, Malodia S, Dhir A. The metaverse in the hospitality and tourism [123] Deng S, Zhao H, Fang W, Yin J, Dustdar S, Zomaya AY. Edge intelligence: the 
industry: an overview of current trends and future research directions. J HOSP confluence of edge computing and artificial intelligence. IEEE INTERNET THINGS 
Mark MANAG 2022;31:527–34. 2020;7:7457–69. 

[104] Mourtzis D, Panopoulos N, Angelopoulos J, Wang B, Wang L. Human centric [124] Zhang K, Zhu Y, Maharjan S, Zhang Y. Edge Intelligence and blockchain 
platforms for personalized value creation in metaverse. J MANUF SYST 2022;65: empowered 5g beyond for the industrial internet of things. IEEE Netw 2019;33: 
653–9. 12–9. 

[105] Fu J, Liu Y, Chao H, Bhargava BK, Zhang Z. Secure data storage and searching for [125] Tian Z, Luo C, Qiu J, Du X, Guizani M, Distributed A. Deep learning system for 
industrial iot by integrating fog computing and cloud computing. IEEE T IND Inf web attack detection on edge devices. IEEE T IND Inf 2020;16:1963–71. 
2018;14:4519–28. [126] Yang Q, Liu Y, Chen T, Tong Y. Federated Machine Learning. ACM T INTEL SYST 

[106] Mourtzis D, Vlachou E. A cloud-based cyber-physical system for adaptive shop- TEC 2019;10:1–19. 
floor scheduling and condition-based maintenance. J MANUF SYST 2018;47: [127] Hao M, Li H, Luo X, Xu G, Yang H, Liu S. Efficient and privacy-enhanced federated 
179–98. learning for industrial. Artif Intell, IEEE T IND Inf 2020;16:6532–42. 

[107] Dai Y, Xu D, Maharjan S, Qiao G, Zhang Y. Artificial intelligence empowered edge [128] Li T, Sahu AK, Talwalkar A, Smith V. Federated learning: challenges, methods, 
computing and caching for internet of vehicles. IEEE WIREL COMMUN 2019;26: and future directions. IEEE SIGNAL PROC MAG 2020;37:50–60. 
12–8. [129] Magalhaes APF, Andrade AMS, Maciel RSP. Model driven transformation 

[108] Wang J, Zhang L, Duan L, Gao RX. A new paradigm of cloud-based predictive development (MDTD): an approach for developing model to model 
maintenance for intelligent manufacturing. J INTELL MANUF 2017;28:1125–37. transformation. Inform Software Tech 2019;114:55–76. 

[109] Wang J, Zhao L, Liu J, Kato N. Smart resource allocation for mobile edge [130] Arinez JF, Chang Q, Gao RX, Xu C, Zhang J. Artificial intelligence in advanced 
computing: a deep reinforcement learning approach. IEEE T EMERG TOP COM manufacturing: current status and future outlook. J Manuf Sci Eng 2020;142. 
2021;9:1529–41. [131] Barredo Arrieta A, Díaz-Rodríguez N, Del Ser J, Bennetot A, Tabik S, Barbado A, 

[110] Leng J, Sha W, Lin Z, Jing J, Liu Q, Chen X. Blockchained smart contract pyramid- Garcia S, Gil-Lopez S, Molina D, Benjamins R, Chatila R, Herrera F. Explainable 
driven multi-agent autonomous process control for resilient individualised Artificial Intelligence (XAI): Concepts, taxonomies, opportunities and challenges 
manufacturing towards Industry 5.0. INT J PROD RES 2023;61:4302–21. toward responsible AI, INFORM. FUSION 2020;58:82–115. 

[111] Leng J, Jiang P, Xu K, Liu Q, Zhao JL, Bian Y, Shi R. Makerchain: a blockchain [132] Lundberg SM, Lee S. A unified approach to interpreting model predictions. Adv 
with chemical signature for self-organizing process in social manufacturing. Neural Inf Process Syst 2017;30. 
J CLEAN PROD 2019;234:767–78. [133] Linardatos P, Papastefanopoulos V, Kotsiantis S. Explainable AI: a review of 

[112] Wan J, Li J, Imran M, Li D, Fazal-e-Amin A. Blockchain-based solution for machine learning interpretability. Methods, Entropy-Switz 2021;23:18. 
enhancing security and privacy in smart. Fact, IEEE T IND Inf 2019;15:3652–60. [134] Zafar MR, Khan N. Deterministic local interpretable model-agnostic explanations 

[113] Wang S, Wan J, Zhang D, Li D, Zhang C. Towards smart factory for industry 4.0: a for stable explainability. Mach Learn Know Extr 2021;3:525–41. 
self-organized multi-agent system with big data based feedback and coordination. [135] Hohman F, Park H, Robinson C, Polo CD. Summit: Scaling Deep Learning 
COMPUT NETW 2016;101:158–68. Interpretability by Visualizing Activation and Attribution Summarizations. IEEE T 

VIS COMPUT GR, 26; 2020. p. 1096–106. 

363