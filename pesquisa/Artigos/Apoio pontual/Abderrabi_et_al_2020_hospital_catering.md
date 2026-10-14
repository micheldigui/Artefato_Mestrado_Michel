---
title: "Abderrabi_et_al_2020_hospital_catering"
source_pdf: "Trabalhos/Artigos/PDF_Originais/Apoio pontual/Abderrabi_et_al_2020_hospital_catering.pdf"
classification: "Apoio pontual"
conversion: "Docling 2.129.0"
---

## Mathematical model for scheduling food production in hospital catering

F. Abderrabi *, **

M. Godichaud *, A. Yalaoui *, F. Yalaoui *, L. Amodeo * A. Qerimi **, E. Thivet **

∗ University of Technology of Troyes, Logistics Industrial Systems Optimization (LOSI), ICD, Troyes, France

(e-mail: fatima.abderrabi@utt.fr, matthieu.godichaud@utt.fr,

alice.yalaoui@utt.fr, farouk.yalaoui@utt.fr, lionel.amodeo@utt.fr)

∗∗ Hospital Center of Troyes, Troyes, France

(e-mail: fatima.abderrabi@ch-troyes.fr, ardian.qerimi@ch-troyes.fr, eric.thivet@ch-troyes.fr)

Abstract: The problem addressed in this paper was motivated by a real optimization problem of supply chain of the hospital center of Troyes (HCT). The HCT is currently seeking to review and improve its logistics processes. The implementation of techniques and methods of operational research must provide solutions to improve the efficiency of logistics activities. In this work, the studied problem focuses on the catering component of the hospital logistics. A novel mathematical model for the production scheduling of multi-products and multi-stages food processes in hospital catering is proposed. This mathematical model has been implemented in commercial solver CPLEX and it has been tested on real instances of HCT and from the literature. The implementation results of the mathematical model proposed have proved its efficiency for the scheduling of the food production process.

Keywords: scheduling, flexible job shop, sequence-dependent setup time, job-splitting, hospital catering.

## 1. INTRODUCTION

Nowadays, hospitals are facing the challenges regarding quality of care and performance. In their management and organisation, there is still a lot of progress that can be made to improve the quality of care while reducing costs. To answer effectively to the patients needs and to improve the working conditions and well-being of their employees, hospitals are looking for tools and new ways of organization and management. Care facilities are discovering the importance of the logistics process as a new approach for effective management of all activities as in other organizations. In fact, the hospital logistics is part of the global performance where the activities are organized and structured with the aim of patients satisfaction in terms of quality, quantity, delay, safety and at the least cost. The main purpose of this logistics is to control and optimize physical flows from suppliers to patients at the best cost that respects technical, economic and regulatory conditions for optimal dispensing to patients. Hospital logistics is a complex process characterized by a diversity of needs, users, products and distribution channels. The flows to the hospital are much more critical and sensitive than those of the industrial sector since it is the health, and thus the life of the patients which is at stake. The coordination of these activities requires logistical expertise that few institutions will be able to develop on their own. This has led researchers to focus for some years on the management and optimization of the supply chain in hospitals. In this context and in order to improve the working conditions of the employees and their well-being, the hospital center of Troyes implements means to improve its daily efficiency. The hospital is carrying out a revision of its supply chain which must notably consider the management of food flows within the hospital.

The remainder of this paper is organized as follows : section 2 presents the state-of-the-art regarding the problem of scheduling food production. Then, the problem statement and the corresponding mathematical model are defined in section 3. Finally, in section 4 the implementation results of the mathematical model are discussed.

## 2. LITERATURE REVIEW

The production scheduling problem in food industries represents a famous class of problems referred as scheduling with sequence-dependent setups which are well known to be NP-hard (Sun et al. 1999). In recent years, there has been great interest in the development of intelligent solutions for this problem in various fields of applications. The promising results of scheduling methods (such as reduction of production costs, increased throughput and smoother operation of the production equipment, improvement of working conditions and the well-being of employees) have stimulated a considerable research effort. Most of existing works in literature on scheduling food production are from the food industry and dairy industry where the production system is a flow shop or parallel machine system in most cases (Table 1), as there is an increasing interest in investigating changeovers in scheduling approaches from this sector.

MLP: Mixed linear programming, MILP : Mixed integer linear programming, ILP : Integer linear programming Table 1. Bibliographic summary on food production scheduling problems.

| Author                |   Year | Product   | Nb Products    | Production System   | Shelf life   | Modeling   | Application Domain   |
|-----------------------|--------|-----------|----------------|---------------------|--------------|------------|----------------------|
| Our problem           |   2019 | -         | Multi products | Flexible Job Shop   | Known        | MLP        | Hospital catering    |
| Wei et al..           |   2018 | -         | Multi products | Flow Shop           | Unknown      | MILP       | Food industry        |
| Sargut and Isık       |   2017 | -         | Single product | Single machine      | Unknown      | -          | Food industry        |
| Tempelmeier et al..   |   2016 | -         | Multi products | Parallel machine    | Unknown      | -          | Food industry        |
| Stefansdottir et al.. |   2016 | Cheese    | Single product | Flow Shop           | Unknown      | MILP       | Dairy industry       |
| Acevedo-Ojeda et al.. |   2015 | -         | Single product | Single machine      | Unknown      | MIP        | Food industry        |
| Bilgen and C ¸eleb    |   2013 | -         | Multi product  | Flow Shop           | Unknown      | MILP       | Dairy industry       |
| Kopanos et al..       |   2012 | Ice cream | Single product | Flow Shop           | Unknown      | MILP       | Food industry        |
| Kilic et al..         |   2011 | Milk      | Single product | Flow Shop           | Unknown      | MILP       | Dairy industry       |
| Karray et al..        |   2011 | -         | Multi products | Single machine      | Unknown      | ILP        | Food industry        |
| Kopanos et al..       |   2010 | Yogurt    | Single product | Flow Shop           | Unknown      | MILP       | Dairy industry       |
| G¨ unther et al..     |   2006 | Sausage   | Single product | Flow Shop           | Unknown      | MILP       | Food industry        |

Akkerman and van Donk (2009) developed a methodology for the analysis of the scheduling problems in food processing. In (1988) Smith Daniels and Ritzman developed a general lot sizing model for process industries and applied their method to a situation representative of food processing facility. Kopanos et al. (2012) offered an efficient mathematical framework for detailed production scheduling in the food processing industries. Wauters et al. (2012) introduced an integrated approach to real world production scheduling for the food processing industries. In (2016) Tempelmeier and Copil considered a capacitated dynamic lot sizing problem with parallel machines for food industry, in which all the units of a given product, produced during a specified time period, is used to satisfy the related demand. Niaki et al. (2017) addressed the integrated lot sizing and scheduling problem of food production in batch manufacturing systems with multiple shared-common resources and proposed a new mixed integer linear programming formulation with multiple objective functions. In (2009) Ahumada and Villalobos reviewed models for the agri-food business where products may be perishable or not, their focus is on procurement and harvesting planning and the only goods they are interested in are crops. Sel et al. (2015) introduced the planning and scheduling decisions considering the shelf-life restrictions, product dependent machine speeds, demand due dates, regular and overtime working hours in the perishable supply chain. In (1999) Arbib et al. considered a three-dimensional matching model for perishable production scheduling, which is studied under two independent aspects : the relative perishability of products and the feasibility of launching-completion time. Basnet et al. (1999) described an exact algorithm to solve scheduling and sequencing problem in the same industry. Chen et al. (2019) provided a review of literature on the integration of scheduling and lot sizing for perishable food products and they categorized the papers by the characteristics of lotsizing and scheduling that were included in their models, and the strategies used to model perishability.

In (1993) Claassen and Van Beek proposed an approach to solve a planning and scheduling problem for the bottleneck packaging facilities of the cheese production division of a large dairy company. Nakhla (1995) emphasizes the flexibility need for operations scheduling in the dairy industry, and proposes a rule-based approach for scheduling packaging lines. In (2005) Entrup et al. presented three different mixed integer linear programming for scheduling problems in fresh food industry in the packing stage of stirred yogurt production. They took into account shelf life issues and fermentation capacity limitations. Marinelli et al. (2007) addressed a solution approach for a capacitated lot sizing and scheduling problem with parallel machines and shared buffers, arising in a packaging company producing yoghurt. In (2007) Doganis and Sarimveis proposed a model for the optimal production scheduling in a single yoghurt production line. The model takes into account all the standard constraints encountered in production scheduling (material balances, inventory limitations', machinery capacity). It also considers special features that characterize yoghurt production which are limitations in production sequencing mainly due to different fat contents and flavors of various products and sequence dependent setup times and costs. However the model is limited to single production line. In another study, Doganis and Sarimveis (2008) presented a methodology for optimum scheduling of yoghurt packaging lines that consist of multiple parallel machines. The methodology incorporates features that allow it to tackle industry specific problems, such as multiple intermediate due dates, job mixing and splitting, product specific machine speed, minimum, maximum lot size and sequence dependent changeover times and costs. However the model does not incorporate multi-stage production decisions, and ignores some industry-specific characteristics, such as shelf life.

Finally, it is worth mentioning that, to the best of our knowledge, there is almost no study addressing the problem of scheduling food production in hospital catering. Therefore, the aim of the present work is to propose a new mathematical model for this problem.

## 3. PROBLEM DESCRIPTION

The problem of scheduling food production can be described by a set of N jobs, where each job i corresponds to the preparation of a dish characterized by a number of portions Q i (quantity), and a set of operations J i necessary for the preparation of the dish (from raw material to finished product). It is worth to highlight that the dishes to be prepared do not have the same operating ranges (set of operations necessary for the preparation of dish). In this study, we identified ten possible operating ranges for all the dishes to be prepared and it is possible that several dishes may have the same operating range. For each operation of an operating range, there is a set of material resources that can realize it. Among these material resources, we cite, as an example : ovens, packaging machines, cooling cells, etc. For each material resources there is a setup time to take into account which corresponds to the preparation time of the resource before carrying out an operation and the cleaning time of the resource between two consecutive operations.

The problem of scheduling food production treated in this study is considered as a flexible job shop scheduling with sequence-dependent setup time. The jobs do not have the same order of operations and each job has its own order of operation. Each operation does not have to be processed by a predefined machine, but rather has to be assigned to one among a set of possible machines (Figure. 1). Note that the corresponding machines may not be identical, involving different processing times according to the chosen machine. The setup times of machines are sequence dependent because it dependents on the preceding operation on the same machine. The scheduling food production involves two steps: (i) assignment of operations to machines i.e., each operation must be assigned to a machine among those that can process the considered operation, (ii) sequencing of operations on machines i.e., determining an operation sequence for each machine.

Fig. 1. Example of an operating range consisting of a set of operations from pretreatment of raw materials to stock of finished products.

<!-- image -->

As mentioned previously, in order to respect the production capacity of material resources, a job can be splitted into smaller sub-lots, in such a way that the operations of sub-lots of a job can be performed simultaneously on different machines. This strategy, which is useful when machine capacity does not allow the treatment of the whole job, also enables a more efficient processing scheme. The criterion to minimize in the present study is the flow time of jobs in the production system. The choice of this criterion is based on the fact that in a food process we must ensure the respect of the cold chain at each stage of the product life cycle which aims to constantly maintain a low temperature (positive or negative depending on the product) to ensure the maintenance of all the qualities (hygienic, nutritional and gustatory) of food.

## 3.1 Assumptions

The mathematical model for the scheduling food production inherits its main assumptions from the standard flexible job shop scheduling problem and flexible job shop scheduling problem with sequence-dependent setup times in addition to some specific features due to the job splitting.

- Jobs are independent of each other,
- A job can be split into sub-lots,
- Each sub-lot of a job consists of a set of operations that must be processed consecutively (precedence constraints between operations of sub-lots of jobs),
- Each operation of sub-lot has a given processing time,
- The preemption of operations of sub-lots of jobs is not allowed, i.e. operation processing on a machine cannot be interrupted,
- Each job has a given due date (finish date of production at latest),
- Sub-lot sizes (number of portions) are discrete,
- Sub-lots creation is consistent throughout the processing sequence, meaning that job splitting and sublot sizes remain constant for all operations,
- Machines are independent,
- A machine can process at most one operation at a time,
- The setup times of machines are dependent on the sequence of operations of sub-lots of jobs,
- Material resource has a given availability time windows that must be taken into account.

Accounting for these assumptions, the objective is to find a schedule involving sub-lots assignment to machines and sub-lot sequencing for each machine, in such a way that each job's demand is fulfilled, different constraints of problem are respected and the flow time of jobs in production system is minimized.

## 3.2 Notations

The definition of the proposed mathematical model parameters relies on the following sets and indexes :

- M : set of all material resources, where m = | M | .
- N : set of jobs (dishes to prepare), where n = | N | and { 0 , n +1 } are two dummy jobs.
- J i : set of operations of job i ∈ N , such that the operation j ∈ J i is done before the operation j +1 ∈ J i and | J 0 | = | J n +1 | = 1.
- Q i : number of portions (quantity) of job i ∈ N .
- q i : number of portions in each sub-lot of job i ∈ N .
- L i : set of sub-lot of job i ∈ N , with | L 0 | = | L n +1 | = 1 and l i = | L i | such that l i = ⌈ Q i q i ⌉ .

- d i : due date of job i ∈ N .
- M ij ⊂ M : set of material resources that can perform the operation j ∈ J i of job i ∈ N .
- R k : maximum capacity in number of portions of the material resource k ∈ M .
- M 1 ⊂ M : set of material resources that have a capacity of one portion and that can not be processed several jobs at the same time (material resources that can perform preprocessing and cold production operations).
- M 2 ⊂ M : set of material resources that have a capacity greater than one portion and which can not be processed several jobs at the same time (ovens,...).
- M 3 ⊂ M : set of material resources that have a capacity greater than one portion and that can processed several jobs at the same time (cooling cells).
- P ′ ijk : unit processing time of operation j ∈ J i of job i ∈ N on the material resource k ∈ M 1 .
- P ijk : processing time of operation j ∈ J i of job i ∈ N on the material resource k ∈ M 2 ∪ M 3 .
- s ijhgk : setup time of material resource k ∈ M ij ∩ M hg , if operation j ∈ J i of job i ∈ N precedes directly operation g ∈ J h of job h ∈ N on the material resource k ∈ M ij ∩ M hg .
- [ A k , Y k ] : time window of availability of material resource k ∈ M .
- B : big integer.

## 3.3 Decision variables

- X iljk : binary variable, equals to 1, if operation j ∈ J i of sub-lot l ∈ L i of job i ∈ N is assigned to the material resource k ∈ M ij , 0 otherwise.
- F iljhl ′ gk : binary variable, equals to 1, if operation j ∈ J i of sub-lot l ∈ L i of job i ∈ N precedes directly operation g ∈ J h of sublot l ′ ∈ L h of job h ∈ N on the material resource k ∈ M ij ∩ M hg , 0 otherwise.
- Z ill ′ jk : binary variable, equals to 1, if operation j ∈ J i of sub-lot l ∈ L i of job i ∈ N starts and finishes at the same time as the operation j ∈ J i of sub-lot l ′ ∈ L i of job i ∈ N on the material resource k ∈ M ij , 0 otherwise.
- S iljk : starting time of operation j ∈ J i of sub-lot l ∈ L i of job i ∈ N on the material resource k ∈ M ij .
- C iljk : completion time of operation j ∈ J i of sub-lot l ∈ L i of job i ∈ N on the material resource k ∈ M ij .
- C i : completion time of job i ∈ N .

## 3.4 Mathematical model

The mathematical model (P2) provided here for the problem of scheduling food production was developed based on the ( Buddala and Mahapatra, 2018) formulation (P1), that is designed for the basic flexible job shop scheduling problem. This mathematical model was adapted and improved for the problem of scheduling food production by integrating the different constraints that were not taken into consideration in the work of Buddala and Mahapatra

(2018). The following table represents the characteristics of the two mathematical models (P1) and (P2) :

Table 2. Characteristics of the mathematical models (P1) and (P2).

| Constraints and objective   | (P1)   | (P2)   |
|-----------------------------|--------|--------|
| - Processing time           | X      | X      |
| - Precedence                | X      | X      |
| - No preemption             | X      | X      |
| - Machine capacity          |        | X      |
| - Due date                  |        | X      |
| - Machine availability      |        | X      |
| - Setup time                |        | X      |
| - Splitting                 |        | X      |
| - C max - ∑ C i             | X      | X      |

The mathematical model (P2) is formulated as indicated through equations (1) to (22) :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

(15)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In the mathematical model presented previously, the first constraint (1) represents the objective function consisting in minimizing the flow time of jobs in production system, which is defined as the sum of completion time of all jobs. In turn, job completion times are computed as the completion time of the last sub-lot derived from the considered job, as indicated in (2). Note that, due to (3), for given i ∈ N , l ∈ L i and j ∈ J i , variables S iljk and C iljk are equal to zero for all k ∈ M ij values different from the index of the machine that really processes the considered sub-lot. On the other hand, when X iljk equals to 1, (4) and (5) activate the relationship constraint between starting time and completion time of an operation of a sub-lot. It is worth noting that, in this case, the processing time does not depend on the quantity of job for the material resources M 2 ∪ M 3 (4), but it depends on the quantity of job for the material resources M 1 (5). Constraints (6) considers sequence dependent setup times between completion time and starting time of two operations of sub-lots which are processed on machine one after another. Equations (7) disable the constraints (6) if two different sub-lot of the same job are performed at the same time by the same material resource. Constraints (8) and (9) require that if two operations of two different sub-lots of the same job are assigned at the same time to a material resource M 2 or M 3, they must have the same starting time and completion time respectively. Constraint (10) ensures that only one operation follows immediately j th operation of sub-lot l ∈ L i of job i ∈ N on machine k ∈ M ij ∩ M hg and constrain (11) guaranties that only one operation precedes immediately g th th operation of sub-lot l ′ ∈ L h of job h ∈ N on machine k ∈ M ij ∩ M hg . Equations (12) establishes the precedence constraint between two consecutive operations of the same sub-lot. Constraints (13) enforces that each operation of each sub-lot should be assigned to exactly one machine among the possible ones. The respect of the due date of jobs is modeled by (14). The constraints (15) ensure that the capacities of material resources in number of portions are respected. The respect of the time windows of availability of material resources is modeled by (16) and (17). Finally, (19), (20), (21) and (22) define the domain of decision variables.

## 4. IMPLEMENTATION RESULTS OF MATHEMATICAL MODEL

The mathematical model presented previously have been implemented in JAVA programming language using the CPLEX library to solve it. This model have been tested on several adapted instances of literature (Behnkel and Geiger (2012), Azzouz et al. (2017), Buddala and Mahapatra (2018), Shen et al. (2018)) and on instances of HCT. The instances of HCT were built after having timed the processing times of operations of jobs of a real example having 84 jobs, 372 operations and 29 machines. From this example, several instances were built by increasing each time the number of jobs, sub-lots and operations to see from what number of jobs, sub-lots and operations the model is not able to find solutions. Table (3) shows the implementation results of the mathematical model (P2) on some examples of HCT instances :

Table 3. Implementation results of the mathematical model (P2) on real instances of HCT.

|   Job |   Sub-lot |   Operation |   Machine | Time   | ∑ C i   |
|-------|-----------|-------------|-----------|--------|---------|
|     4 |         5 |          12 |        29 | 0.5 s  | 15.72 h |
|     5 |         6 |          17 |        29 | 2 s    | 25.43 h |
|     6 |         8 |          22 |        29 | 1 mn   | 34.16 h |
|     7 |        10 |          26 |        29 | 2 mn   | 41.12 h |
|     8 |        11 |          31 |        29 | 2h30   | 51.09 h |
|     9 |        14 |          36 |        29 | > 3 h  | -       |
|    10 |        16 |          41 |        29 | > 3 h  | -       |
|    11 |        18 |          46 |        29 | > 3 h  | -       |
|    12 |        19 |          50 |        29 | > 3 h  | -       |

Fig. 2. Computational time of instances according to the number of operations of sub-lots of jobs.

<!-- image -->

From the implementation results (Tale (3) and Figure (2)) of the mathematical model presented previously, we observe that the model gives quickly a solution for the small instances with a certain number of jobs, sub-lots, and operations. The execution times of this mathematical model for these instances vary according to the number of jobs, sub-lots, and operations. It is important to note that the execution time is given only for instances where the optimal solution is obtained. In the opposite case, the bar - means that no optimal solution was found after 3 hours of execution. The implementation results of the mathematical model proposed on real instances of HCT show the limits of an exact resolution for the problem of scheduling food production.

## 5. CONCLUSION

In this paper, a new mathematical model for scheduling food production of an industrial case was presented. The model is an improvement of standard flexible job shop scheduling problem and flexible job shop scheduling problem with sequence-dependent setup times by adding specific industrial constraints. An extensive model study confirming the effectiveness of the proposed model is presented. The practical implementation results promise to be very useful. Our future work focuses on the development of mathematical models for the problem of scheduling food production by integrating human resources availability and the development of heuristics and metaheuristics for this problem for large real instances.

## REFERENCES

- [1] R. Buddala and S. Mahapatra (2018). An integrated approach for scheduling flexible job-shop using teaching learning-based optimization method. Journal of Industrial Engineering International.
- [2] L. Shen, S. Dauzere Peres and J.S. Neufeld. (2018). Solving the flexible job shop scheduling problem with sequence-dependent setup times. Journal of Operational Research.
- [3] D. Behnke1 and M. J. Geiger (2012). Test Instances for the Flexible Job Shop Scheduling Problem. with Work Centers. Helmut-Schmidt-University, Logistics Management Department, Germany.
- [4] A. Azzouz, M. Ennigrou and L. Ben Said (2017). A hybrid algorithm for flexible job-shop scheduling problem with setup times. International Journal of Production Management and Engineering.
- [5] Tahmassebi, T. (1996). Industrial experience with a mathematical-programming based system for factory systems planning/ scheduling. Computers Chemical Engineering.
- [6] Akkerman, R., and van Donk, D. P. (2009). Analyzing scheduling in the food-processing industry: structure and tasks. Cognition, Technology Work.
- [7] Smith Daniels, V. L., and Larry P. Ritzman. (1988). 'A Model for Lot Sizing and Sequencing in Process Industries.' Journal of Production Research.
- [8] Nakhla, M. (1995). Production control in the food processing industry. International Journal of Operations Production Management.
- [9] Arbib, C., Pacciarelli, D., and Smriglio, S. (1999). A three-dimensional matching model for perishable production scheduling. Discrete Applied Mathematics.
- [10] L¨ utke entrup, M., G¨ unther, H.-O., Van Beek, P., Grunow, M., Seiler, T. (2005). Mixed-Integer Linear Programming approaches to shelf-life-integrated planning and scheduling in yoghurt production. Journal of Production Research.
- [11] Marinelli, F., Nenni, M. E., Sforza, A. (2007). Capacitated lot sizing and scheduling with parallel machines and shared buffers: A case study in a packaging company. Annals of Operations Research.
- [12] Doganis, P., Sarimveis, H. (2007). Optimal scheduling in a yogurt production line based on mixed integer
13. linear programming. Journal of Food Engineering.
- [13] Cai, X., Chen, J., Xiao, Y., and Xu, X. (2008). Product selection, machine time allocation, and scheduling decisions for manufacturing perishable products subject to a deadline. Computers Operations Research.
- [14] Ahumada, Omar, Villalobos, J.Rene, 2009. Application of planning models in the agri-food supply chain: a review. European Journal of Operational Research.
- [15] Kopanos, G. M., Puigjaner, L., Georgiadis, M. C. (2012). Efficient mathematical frameworks for detailed production scheduling in food processing industries. Computers Chemical Engineering.
- [16] Wauters, T., Verbeeck, K., Verstraete, P., Vanden Berghe, G., De Causmaecker, P. (2012). Real-world production scheduling for the food industry: An integrated approach. Engineering Applications of Artificial Intelligence.
- [17] Sel, C., Bilgen, B., Bloemhof-Ruwaard, J. M., van der Vorst, J. G. A. J. (2015). Multi-bucket optimization for integrated planning and scheduling in the perishable dairy supply chain. Computers Chemical Engineering.
- [18] Fr´ ed´ eric Dugardin, Hicham Chehade, Lionel Amodeo, Farouk Yalaoui and Christian Prins. (2007). Hybrid Job Shop and parallel machine scheduling problems: minimization of total tardiness criterion. University of Technology of Troyes, France.
- [19] Copil, K., W¨ orbelauer, M., Meyr, H., Tempelmeier, H. (2016). Simultaneous lotsizing and scheduling problems: a classification and review of models. OR Spectrum.
- [20] Niaki, M. K., Nonino, F., Komijan, A. R., Dehghani, M. (2017). Food production in batch manufacturing systems with multiple shared-common resources: a scheduling model and its application in the yoghurt industry. International Journal of Services and Operations Management.
- [21] Chen, S., Berretta, R., Clark, A., Moscato, P. (2019). Lot Sizing and Scheduling for Perishable Food Products: A Review. Reference Module in Food Science.
- [22] Wei, W., Amorim, P., Guimar˜ aes, L., Almada-Lobo, B., 2018. Tackling perishability in multi- level process industries. Int. J. Prod.
- [23] Sargut, F.Z., Isık, G., 2017. Dynamic economic lot size model with perishable inventory and capacity constraints. Appl. Math. Model.
- [24] Stefansdottir, B., Grunow, M., Akkerman, R. (2016). Classifying and modeling setups and cleanings in lot sizing and scheduling. European Journal of Operational Research.
- [25] Acevedo-Ojeda, A., Contrerasa, I., Chenb, M., 2015. Two-level lot-sizing with raw-material perishability and deterioration. Int. J. Prod. Res.
- [26] Bilgen, B., C ¸ elebi, Y., 2013. Integrated production scheduling and distribution planning in dairy supply chain by hybrid modelling. Ann. Operat. Res.