---
source_file: "2021-Data science connotation, methods, technologies, and development.txt"
original_rel_path: "Trabalhos\Artigos\Aproveitar parcialmente\txt\2021-Data science connotation, methods, technologies, and development.txt"
category: "Artigos_Aproveitar_parcialmente"
extension: ".txt"
sha256: "fb38b3509b469aa55f2d534dd5944fb70fa029e7197045210391d1afbc604470"
extracted_at: "2026-09-20T00:50:21.575046"
---

﻿Data Science and Management 1 (2021) 32–37
Contents lists available at ScienceDirect

Data Science and Management

journal homepage: www.keaipublishing.com/en/journals/data-science-and-management
Research article
Data science: connotation, methods, technologies, and development

Zongben Xu a,*, Niansheng Tang b, Chen Xu c, Xueqi Cheng d

a School of Mathematics and Statistics, Xi’an Jiaotong University, Xi’an, 710049, PR China
b School of Mathematics and Statistics, Yunnan University, Kunming, 650091, PR China
c Department of Mathematics and Statistics, University of Ottawa, Ottawa, K1N 6N5, Canada
d Institute of Computing Technology, Chinese Academy of Sciences, Beijing, 100190, PR China
A R T I C L E I N F O

Keywords:
data science
data science methodology
big data
technical directions
Peer review under responsibility of Xi’an Jiaoto
* Corresponding author.
E-mail address: zbxu@xjtu.edu.cn (Z. Xu).

https://doi.org/10.1016/j.dsm.2021.02.002
Received 7 February 2021; Accepted 8 February 20
Available online 23 February 2021
2666-7649/© 2021 Xi'an Jiaotong University. Publi
CC BY-NC-ND license (http://creativecommons.org
A B S T R A C T

The rapid development of big data breeds data science. Understanding and mastering the internal pattern of the
value generation of big data is important for improving digitization and the covergence of data science with
management science, computer science, and other disciplines. In this study, we discuss the significance of data
science for the development of science and technology and social progress. Based on the interpretation of the
connotation of data science, we introduce the definition of data science and review its formation by summarizing
the major progress of related disciplines. We also discuss the research methodologies, development patterns and
trends, and technical directions of data science. Finally, we make suggestions for data science to promote the
development of data-based science and technology.
1. Introduction

The emergence and development of big data is the most direct,
important, and core driving force to promote the formation of data sci-
ence. The word “big” here not only means the data set contains a large
amount of data, but also reflects the substantial transformation from the
simple accumulation of quantity to the change of quality. Thus, the
amount of data is extremely large and comprehensive that to “read the
story behind the data only from these fragmented data” is possible. In
addition to the massive data set, “complexity” usually refers to complex
features, such as data heterogeneity, time variability, distribution, rele-
vance, and value sparsity.

The importance of big data is that they provide the foundation for
digital economy (including digital real economy, virtual economy, and
network economy), scientific discovery based on data, and social
governance. Big data can bring us unprecedented opportunities in at least
four aspects, including management innovation, industrial development,
scientific discovery, and discipline development. However, realizing the
great value of big data, especially to transform big data into real pro-
ductivity is still a great challenge. The challenge is mainly reflected in
scientific foundation, core technology, legal system, and talent demand.

For big data, data science indicates new principles, theories, tech-
nologies, and methods. It is a new approach and problem solving method
ng University.

21

shing services by Elsevier B.V. on
/licenses/by-nc-nd/4.0/).
to realize the value of big data. Data science lays the foundation of big
data science. It forms the core technology of big data analysis and pro-
cessing, and contains an effective approach to realize the value of big
data. Human society, physical space and information space are consid-
ered to be the ternary world of today’s society. The relationship and
interaction between the three worlds determine the technical charac-
teristics of social development (Fig. 1).

As a big data method, the massive processing capabilities of data
science (especially distributed processing capability, stream processing
capability, parallel computing capability, and edge computing capa-
bility) complete the process of big data change to qualitative change. Its
fusion analysis and processing capabilities (especially the interoperating
technology based on the combination of virtual integration and block-
chain, the heterogeneous data integration and conversion technology
based on optimal transmission, etc.) realize the association and aggre-
gation of big data; big data analysis becomes possible given the theo-
retically provable correctness (TPC), interpretable, generalizable,
parallel, and scalable analysis algorithms. These findings indicate that
data science can support the realization of big data principles, thereby
empowering big data and transforming it into actual productivity and
generating great value.
behalf of KeAi Communications Co. Ltd. This is an open access article under the



Z. Xu et al. Data Science and Management 1 (2021) 32–37

Fig. 1. Three-world theory and science technology.
2. Data science theories and methodologies

2.1. Emergence and basic concepts of data science

The emergence of data science has its inevitability, and its develop-
ment has extreme urgency and importance. Data science is based on data,
especially big data. The problems concerned, the methods used, and the
results achieved have appeared in various forms or terms in a wide range
of disciplines, such as mathematics, statistics, computer science, and
artificial intelligence (AI). Data science uses the theories and methods of
these related disciplines for integration, innovation, and development on
this basis.

Data/Datum is a digital record of the physical world and human social
activities and an information carrier in the form of encoding. Common
data forms include tables, curves, graphics, images, videos, texts, audios,
networks, maps, and biomics sequences. Information are data with se-
mantic interpretation; they are valuable for decision-making after a
certain abstraction and processing of the data. Information are different
from matter and energy. They are “used to eliminate uncertainty”.

Knowledge is obtained through the synthesis, correlation, deduction,
and reasoning of information and has been verified as accurate and
generally believed by people. Knowledge, often described by language
and words, usually has the features of systematization and structurali-
zation and is often described in language and text. In the field of
knowledge engineering, a famous data–information–knowledge–wisdom
(DIKW) hierarchy diagram depicts the hierarchical relationship from
data to information, to knowledge, and then to wisdom (Rowley, 2007).
Fig. 2. Data va

33
Data form a complete data chain from collection, aggregation,
transmission, storage, processing, and analysis to application as shown in
Fig. 2. This process is accompanied by a data value-added process from
data to information, from information to knowledge, and from knowl-
edge to decision-making. The main links of the data value chain include
data collection/convergence, data storage/governance, data processing/
computing, data analysis, and data application. Any data-driven science
and technology realizes a specific type of data value chain.

2.2. Definition of data science

A sociological explanation of data science is science about the era of
big data; it aims to reveal the new challenges, opportunities, thinking,
andmodes in the era of big data. It is a set of knowledge system composed
of new theories, methods, models, technologies, platforms, tools, appli-
cations, and best practices in the era of big data (Li and Cheng, 2012).
This explanation has sociological significance, but it is complex and lacks
a substantive description of what data science should include. This
discipline should be defined at least from the three dimensions of
research object, methodology, and scientific task/scientific goal. On this
basis, the definition of data science is introduced as follows.

Data science is the basic theory and methodology related to the
realization of the data value chain. It uses modeling, analyzing, compu-
tating, and learning to study the conversion from data to information,
from information to knowledge, and from knowledge to decision-making
and realizes the cognition and manipulation of the real world. In data
science, “realizing the value chain of data” is the research object, which is
lue chain.



Z. Xu et al. Data Science and Management 1 (2021) 32–37
more accurate and targeted than “data as the research object”. It can also
highlight the subjectivity of big data as the research object. The goal of
data science is to realize the cognition and control of the real world, and
the scientific task of data science is to complete the transformation from
data to information, from information to knowledge, and from knowl-
edge to decision-making in data space, which is summarized as “three
transformations and one realization”. It not only limits its main conno-
tation, but also strengthens its strong dependence on background-related
disciplines. The subject methodology of data science is summarized as “a
hybrid of modeling, analyzing, computating, and learning”; it is a
methodological innovation. It not only affirms the multidisciplinary
relevance of data science, but also avoids the simple definition of data
science as a general term of multiple disciplines.

2.3. Development of the concepts of data science

Data science sprouted in the 1960s and developed from the 1990s to
the beginning of this century. However, as a discipline, it is formed in the
current big data era.

The embryonic stage (1960–1990). The term “datalogy” appeared in
1960–1990. In 1966, Naur, a Danish computer scientist and winner of
Turing Award, proposed to define “the science of data processing” with
the term “datalogy”, whose research object is digital data (Naur, 1975).
The emergence of the concept of datalogy provides data processing a
scientific status and is the origin of its concept.

Multiperspective formation stage (1990–2010). Naur first put for-
ward the concept of data science, and it has not been discussed for a long
period. However, different subjects use different terms one after another
and provide the interpretation of their respective disciplines.

New discipline establishment stage (2010–). Since the beginning of
this century, big data has promoted the rapid development of data sci-
ence, making it a widely accepted emerging discipline.

2.4. Relationship of data science and other disciplines

Mathematics and data science are evidently different. The former
only studies abstract data (in the form of vector, matrix, and graph), but
the latter focuses on entity data (such as text, image, and video). In any
case, the research of data science is based on metascience, such as
mathematics. Statistics and data science are almost identical in research
object, research goal, and application paradigm. Statistics is not only a
model of the success of data science, but also the foundation of its
development. However, statistics is not a complete data science, and the
differences between them are significant. First, statistics does not focus
on complex data types (such as images, texts, videos, and other un-
structured data), and their related applications focus on data science.
Second, the research of statistics is still based on model assumptions,
which still belongs to the third paradigm. Third, statistics pays less
attention to the deep integration of computing science and rarely pro-
duces extensive, practical, and efficient problem-solving algorithms, such
as deep learning in machine learning and AI. Fourth and most impor-
tantly, statistics are also helpless when faced with the challenges of data
science, such as complex data analysis, true-false judgment, and big data
analysis and processing.

Computer science is an important foundation and tool of data science.
It is a theoretical foundation of data science. AI is about theory, method,
and technology of simulating biological intelligence to solve problems.
Data is the basis of realizing intelligence, and the mode of realizing in-
telligence is just the mode of data science.

AI, in a narrow sense, is one of the main contents of data science. For
data science, related disciplines that portray the real world are the
foundation, which is not only the basis for understanding data, the source
of research questions, but also the destination of data science research.
Domain-related disciplines should use data science methods, and data
science should focus on discovering patterns and finding commonalities
from domain-related disciplines to realize the transformation from
34
methodology to ontology gradually.
Considering the development history of computer science, data and

computing, as the two main subjects of computer processing, have been
promoting each other and co-coupling development. In addition, the
rapid development of computer technology (especially the Internet,
cloud computing, and the Internet of Things) has greatly promoted the
realization of big data value chain. The computer gradually changes from
computing-centered to a new architecture of “computing þ data þ
network”, which promotes the formation and development of data sci-
ence. The development is from traditional statistics to computational
statistics, and exploratory data analysis, from bioinformatics to high-
dimensional statistical research, from data to distributed statistical
inference.

In computer science, “data” and “computation” are important
research objects and the theoretical bases. In particular, with the devel-
opment of big data technology, the theory, technology, and application
with “data” as the core are much more focused. Its basic pursuit is the
following: the “computing” technology is used to process and manage the
“data” to form systematic and structured data resources, and then
establish knowledge through data analysis to achieve the purpose of
assisting decision-making.

Statistics is a subject that studies how to collect, organize, and analyze
data effectively. It considers data as the research object and analyzes and
processes data in statistical description, statistical modeling, and statis-
tical inference. It is the most important theoretical basis and methodol-
ogy of data science.

Machine learning is developed from the pattern recognition and
computational learning theory in AI (Mohri et al., 2018). It mainly refers
to the research and construction of a type of algorithm that enables it to
learn from the data and predict the attributes without the data. Thus,
machine learning overcomes the traditional and strict static program
instructions, which enable the program to make decisions by using the
input samples. With the focus of AI research changing from “reasoning”
to “knowledge,” and then to “learning,” machine learning has become
the most important approach to realize AI.

There has a core problem not been solved well in traditional machine
learning, that is, the features of data/problems must be preset manually,
in other words, the features of problems cannot be automatically
extracted. Deep learning is developed to solve this problem. Deep
learning is essentially a feature learning method. With deep learning,
original data are transformed from some shallow model representations
into deeper, more complex, and more abstract neural network repre-
sentations to achieve automatic feature extraction and complete corre-
sponding machine learning tasks. The network structure design of deep
learning has always been the core of AI applications. It determines the
difficulty and success rate of deep network training and the success of the
application.

One of the main goals of AI is to create fully autonomous agent to
optimize their own behavior and improve their ability through automatic
interactive learning with the surrounding environment. Reinforcement
learning is a machine learning paradigm developed to achieve this goal.
The aim of federated learning is to build and train a machine learning
model in collaboration with multiple computing nodes in a distributed
environment. Each computing node has its own different data, and it is
not allowed to exchange sample data during the training process.

2.5. Data science methodology

In data science, the description of data needs modeling, such as the
random variables or probability distributions in probability theory. For
data science, modeling is the formalization of objective objects and
processing methods. Analyzing is a process of judging the theoretical
properties of the feasibility, accuracy, complexity, and efficiency of
completing the “three transformations” operation in the data space. For
data science, analyzing is reasoning by using meta-knowledge. Collect-
ing/gathering data, storing/managing data, searching/querying/



Z. Xu et al. Data Science and Management 1 (2021) 32–37
sorting/recommending data, mining/analyzing data, and making scien-
tific discoveries based on data are performed by computers. Computer is
the basic tool of data science.

For data science, algorithms are the core. Mathematics/statistics
solves the problems of data science foundation and modeling, computer
can achieve “accurate and fast computation”, and AI helps data science to
solve application problems to achieve the goal of “one realization”.

For data science, learning is a tool for data empowerment. The main
method of data science is not a simple synthesis or integration ofmodeling,
analyzing, computation, and learning, but a new tool and method of data
processing and analysis with theoretical accuracy and application effec-
tiveness formed by these methods after mutual reference, interaction,
infiltration, and integration. This newmethod integrates their ownways of
thinking, expression systems, value pursuits, and core methods and has the
feature of synergy. Synergy is the creation of a whole that is greater than
the simple sum of the parts. It represents the “physical action” between the
elements, and the effect after the “chemical action” between them, that is,
the overall performance improvement after the mutual enhancement of
each other. This “synergic” data science methodology has and shows great
power and opens up new disciplines.

2.6. Development pattern and trend of data science

In general, data science is “growing in multiple disciplines (devel-
opment), becoming famous in big data (prestige), and forming in a strong
foundation (soul)”. Statistics is the fastest subject to accept and strive for
data science. Computer science is the first discipline to define data sci-
ence from a broader perspective with great efforts. Although AI is based
on big data, it is unrelated to the essential connection with data science
and the possible positive reaction of data science.

Only when the following questions are understood in a scientific
approach, can they be regarded as a “soul” for data science. (1) Will the
data paradigm bemore effective than the knowledge paradigm? (2)What
is the difference between the fourth paradigm and other paradigms? (3)
Better algorithms or more data? (4) Which is more important, causal
analysis or correlation analysis? (5) Can query replace inference in big
data application? (6) Can big data be regarded as a sample population? In
summary, a rigorous data science, not a specious data subject, is required.

Data science has made extraordinary achievements in various fields.
However, fundamentally, these achievements attribute more to break-
throughs in related disciplines, such as statistics, computer science, and
machine learning. The essential dependence and relevance of data sci-
ence is still insufficient. Data scientists hope that with its unique
perspective and method, data science can develop and form more sig-
nificant new scientific theories, new cognitive methods, and new appli-
cation technology to exert its unique value in promoting scientific and
technological progress and solving major real world problems.

Some important basic problems of science and technology in data
science need to be solved, that is, exploring the data space structure and
features. One of the primary tasks of data science is how to store and
process heterogeneous big data, such as naturally occurring images,
videos, texts, and web pages. When a set of objects is given a certain
mathematical structure (operation þ topology), it can become a space in
a mathematical sense. The internal elements of a space in a mathematical
sense can be operated according to specific rules and can also be analyzed
with some specific tools. Therefore, for a type of object (such as image),
standardized and strict analysis can be obtained only by considering it in
the corresponding mathematical space, thereby acquiring essential
recognition.

As a discipline that uses special forms of data, such as “number” and
“shape” as the research object, mathematics has deeply and extensively
studied all types of mathematical space, and established mathematical
language, mathematical principles, and mathematical methods, which
can lay the foundation of all sciences. The mature set of mathematical
theory and method will be extended to data not limited to the form of
numbers and shapes.
35
Is it possible to change “post-test” into “prediction” in the statistical
process? When the size of the sample is close to the population, is sample
analysis still necessary? If necessary, then what is the difference? If un-
necessary, then how to perform statistical analysis directly? Is causal
analysis really unnecessary? Can correlation analysis replace causal
analysis? The three basic issues have been discussed at the epistemo-
logical level in recent years, but research at scientific level is rare.

Complexity and uncertainty are the most significant characteristics of
big data. How to measure, describe, and use complexity and uncertainty
is a basic problem of data science, and new tools and methodologies are
urgently needed. It is scientific issues that must be solved to use as few
samples as possible to maintain the overall characteristics more accu-
rately, delete unimportant data safely, deal with the transformation from
structured to unstructured, and sampling in real time in a data stream
environment. Big data resampling should follow the “purpose-driven”
principle, that is, resampling adapted to different purposes can pursue
different “maintenance” goals.

3. Data science technologies

3.1. Innovation of storage computing technology and consolidation of the
foundation of AI

The characteristics and effects of big data change from quantitative
dimension to qualitative dimension. Thus, big data storage and
computing face a revolution in basic theory and technical system. In
recent years, faced with challenges, the computer science community has
made great efforts in the basic theories and technological innovations of
computational science and made some important progress. However,
some major basic scientific problems have not yet been resolved. As a
result, these basic problems restrict the development of big data storage,
processing, and computing technology. In general, under the pressure of
the rapid development and application of big data, computational theory,
hardware architecture, system software, and application models in
computer science face serious challenges.

In the big data scenario, the scale of the data itself tends to grow
exponentially, resulting in the growth of computing power being less
than that of data. Moreover, even for some static data, when their scale is
large to a certain extent, the simple data transfer in/out has far over-
whelmed the cost of computational processing. In this case, even the
traditional polynomial solvable problem (P problem) cannot easily
obtain the actual solution in the case of limited computing power and
limited storage because a solvable problem in the small data environment
may not be solvable in the big data environment. At this time, the
computational complexity theory that does not consider the pattern of
data scale growth in traditional computational theories must be seriously
considered. From the perspective of computational theory, the de-
pendency between data scale and model performance (upper and lower
bounds) and the dependency between model complexity and model
performance (upper and lower bounds) are provided. These concepts lay
an important foundation for subsequent research and applications. Under
these new computing paradigms, the computability theory and compu-
tational complexity theory of big data need to be reconsidered.

The integration of storage and computation is an effective idea to
break through the traditional memory wall problem. Storage and
computation are two completely different operators. Is there a reasonable
joint optimization model? Where are the scale options and boundaries of
the integration of storage and computation? How to connect the physical
characteristics and process of the device seamlessly? What changes do
the integration of storage and computation bring to the programming
model? A breakthrough in the basic theory and architecture of the new
computer architecture is necessary. How can an optimal collaboration of
cloud computation-edge computing-terminal be achieved given a big
data computing problem? How are complex computing tasks decom-
posed, and how are heterogeneous meters optimally scheduled? How is
the problem of inconsistent data partition and model abstraction solved?



Z. Xu et al. Data Science and Management 1 (2021) 32–37
Big data system software especially needs to be reconstructed on the
basis of basic theory and standard architecture, including theory and
architecture reconstruction of big data system software, the distribution
of big data analysis software, and the weakening of CAP constraints of
distributed data management.

Model learning relies on a large number of training samples. How is
the generalization ability of the model ensured in the case of small
samples? How can the results of the model be more robust to resist at-
tacks and deception? How are the credibility and interpretability of
model inference results answered? How is a distributed and globally
effective model built in a large-scale environment? How are local models
used to support globally trusted model inference? How are the efficiency
and accuracy of model inference balanced? These problems need to be
further explored.

AI is an outstanding technology that realizes the data value chain and
demonstrates the value of data. The following five basic scientific prob-
lems of AI need to be solved: (1) statistical basis of big data analysis, (2)
basic algorithm of big data computation, (3) mathematical principles of
deep learning, (4) optimal transport problem under unconventional
constraints, and (5) study of learningmethodology and learning theory in
function space. The learning theory of functional space is a field that has
not yet been explored. In addition to the major basic scientific problems
described in the previous section, data science faces a large number of
methods and technical problems to be solved. The exploration of these
issues has formed some important research fields.

3.2. Technical directions of data science

Internet of Things technology. Future research on the Internet of
Things needs to focus on making breakthroughs in the following areas:
(1) standard issue, (2) security issue, (3) perception technology, (4)
storage scheduling, and (5) complex network behavior.

Big data interoperating technology. Big data interoperating technol-
ogy is necessary to realize the big data value chain. Future research needs
to focus on the following aspects: (1) big data interoperating standard
protocol, (2) interoperating technology under big data of low-quality,
high-frequency, and high-noise, (3) software-defined big data exchange
and collaborative interoperability technology, (4) data interoperating
technology for ownership retention and labeling.

Big data security technology. The traditional data security protection
technology cannot be entirely applied to the big data situation. Protect-
ing big data security can start from several basic characteristics of data
security, including confidentiality, integrity, usability, and controlla-
bility. In the future, the research on the following technology should be
strengthened: (1) efficient data encryption for business adaptation, (2)
multilevel access control of fine grain, (3) high-performance privacy
protection, (4) trusted and controllable computing of distributed remote
data operation, (5) confidentiality guarantee of multisource aggregation
computing, and (6) big data security evaluation.

Big data storage technology. The future research of big data storage
technology also needs to focus on the following aspects: (1) optimization
of machine learning technology guided storage system (AI for storage),
(2) domain specific big data compression and compact computing, (3)
erasure coding storage native big data ecosystem, (4) big data storage
method with low tail delay.

Distributed collaborative computing technology. With the develop-
ment and application of technology, such as 5G communications, the
Internet of Things, and big data intelligence, a large number of future
computation is not limited to large-scale cloud computing centers, but
are deployed to an integrated distributed resources and environment
consisting of “cloud computation-edge computing-terminal”. At present,
the following aspects should be considered: (1) problem of adaptation
autonomy in heterogeneous computing resources, (2) decision delay
problem of collaboration of cloud computation-edge computing-termi-
nal, (3) consistency problem of heterogeneous data distribution.

New database technology and system. Facing the 4V features of big
36
data, the traditional relational database system oriented to structured
data expression is incompetent for big data organization and manage-
ment. For specific big data application scenarios, new database tech-
nologies designed in combination with data types and data distribution
characteristics also emerge, such as in-memory databases, streaming
databases, graph databases, spatio-temporal databases, and crowd-
sourced databases. In the future, new database theory and technology
should focus on the following: (1) development of a new paradigm of
database theory, (2) promotion of the development of autonomous
database, (3) unified storage and management of multiple heterogeneous
data, and (4) learning-based database organization model.

Big data basic algorithm. On the basis of the application background
of big data, grasping the “seven giant problems” accurately is the key to
big data basic algorithm research. These questions include basic statis-
tics, generalized N-body problem, graph-theoretic computation, linear
algebraic computation, optimization, integration, and alignment prob-
lem. The study of basic big data algorithms is essentially limited by the
theory of big data computation. The researchers expect to find algorithms
to solve problems at the level of ultralow complexity (such as at least
linear complexity and below). However, when we were prepared to give
up the traditional idea that the algorithm with complex polynomials is
good, we suddenly begin to consider the future development of the basic
algorithm of big data.

Data intelligence technology. Data intelligence technology is one of
the most closely integrated fields of data science and application disci-
pline. Its technical level represents the realization level of data value
chain and is the core competence index to measure big data application.
At present, almost all fields struggle to combine with deep learning,
managing to promote intelligent progress in their fields. Some important
areas with particular potential include the following intelligent medical
care, intelligent health, intelligent education, intelligent city, and intel-
ligent manufacturing. Some hotspots of data intelligence research also
include research on machine learning theories and methods under
insufficient training data, learning theories and methods that interact
with the environment, sparse learning theories and methods in high-
dimensional feature space, explainable and credible machine learning
theories and methods, machine learning theories and methods with
privacy protection, new distributed machine learning platforms for large-
scale and multisource data and heterogeneous computing resources, and
visual analysis technology of machine learning platforms.

Blockchain technology. The core values of blockchain are as follows.
(1) It provides a trusted platform for transactions in a weak trust envi-
ronment, thereby satisfying the transaction environment that people seek
to reduce the cost of mutual trust. (2) It promotes the transformation of
the existing Internet from information interconnection to value inter-
connection to form a value Internet. Blockchain is expected to realize the
registration, circulation, and transaction of real world physical assets,
thereby establishing a virtual society with real meaning and parallel
human society. (3) It provides a credible and feasible operating platform
for cognition and manipulation of the real society in parallel virtual so-
ciety. Blockchain technology has been successfully applied to digital
currencies and asset management, such as Bitcoin and Token. A large
number of applications are found in the decentralized Internet and social
governance. Blockchain is still a developing technology, and its overall
development is in the pioneering period, showing an evident trend of
mutual driving of technology and industrial innovation. In terms of basic
theory, technology implementation, and application, blockchain still
faces a series of challenges.

Big data visualization and interaction analysis technology. Generally,
big data visualization and interaction technology can reveal data pat-
terns, display data status, and adjust data processing more intuitively and
directly. This approach is an important technical direction in the field of
big data analysis. However, visualization and interaction analysis is
similar to experimental science, which has many basic defects in formal
description, theoretical model, and objective evaluation. The following
principles determine the main research direction of data science: the first



Z. Xu et al. Data Science and Management 1 (2021) 32–37
is the principle of importance, that is, this direction can represent the
most critical technical field for data value in the data value chain; the
second is the principle of nonconflict, which indicates that the fields
classified as secondary or above disciplines in other disciplines (except
statistics and AI) or those generally recognized as the main direction
should not be specifically listed as the direction of data science; the third
is the principle of specialization, where a certain scale of practitioners is
required to carry out stable and professional research to promote the
sustainable development of the discipline; the fourth is the principle of
integrity, where all directions can cover the data value chain and support
the construction of data science knowledge system. Data collection and
management mainly include data aggregation, data management, data
processing, data governance, and other subdirections, which are the
main part of the intersection of data science, management science, and
computer science.

Data storage and computing mainly include data storage and the use
of new computing tools to complete data processing tasks in the field of
science and technology. Data analysis and interpretation can include
three subdirections, including big data statistics, big data machine
learning, and big data algorithms, which are the main manifestations of
statistics and machine learning extensions. Data products and applica-
tions can mainly include big data intelligence, data product development
technology and tools, and data product testing and packaging.

4. Suggestions for the development of data science

The disciplinary foundation should be consolidated to understand the
value and importance of data science. The object of data science research
should be grasped accurately to understand the changes in the research
object. We should grasp the connotation of the basic tasks and basic
scientific goals of data science. We also need to understand the essential
connection between data science and digital economy. The research on
major basic issues of data science should be promoted to make break-
throughs; the application includes the origin and destination.

The “data science and big data technology” should be developed to
build an independent data science discipline. On the basis of the orien-
tation of the university, the market demand, and the specialty of teachers,
the appropriate subject orientation should be selected. The principle of
“giving priority to charactersitics and highlighting the advantages” is the
basis to determine the subject direction. We should avoid the “assorted-
cold-dish” curriculum and balance the cultivation between “generalists”
and “professionals”. A multidisciplinary teacher team with substantial
cross discipline should be established, a “hybrid” talent training mode
should be adopted, and quality should be prioritized.

We should adhere to the “application demand driven and scientific
problem oriented” principle and enhance the connotation and achieve-
ment abundance of data science. This approach can provide practical
strategies for the implementation of national big data strategy. The focus
should be big data applications in key industries/fields to propose and
37
promote data science system solutions. Major national research tasks
should be formed to organize research and make breakthroughs; in the
scientific community, we should strengthen the discussion on the sci-
entific connotation and methodology of data science, big data and AI to
form a unified understanding. Among different disciplines, a consensus
should be established, and the relevant concepts, theories, and methods
of data science should be unified as the basis for the development of data
science in different disciplines. The public’s understanding of the core
role of data science in the digital economy should be improved.

In addition, we shall reform the evaluation system, create an envi-
ronment for interdisciplinary integration, and build a good data science
development ecology. We should create an open, cooperative, inclusive,
and innovative working environment. We should not enlarge the role of
individual value and individual subject but advocate the value that “the
inevitable factor of success is not in oneself”. The cooperation culture of
“mutual appreciation, integration, and cooperation” should be advo-
cated. The performance standards of “achievement, contribution, and
quality”, not only “academy, ranking, or quantity” should be adopted.
The distribution principle of “based on performance, considering coor-
dination, continuity, and stability” can be used.

We shall create and cultivate a large number of data science pro-
fessionals who “understand data, and can analyze and implement the
measures”. Accurate understanding of connotation, research direction,
and methodology of data science is required. Emphasis can be the data
paradigm, while adhering to the thinking mode of combining with the
knowledge paradigm. We should emphasize the active attribute of data,
but strengthen the normative management of data. We should be alert to
“specious” views and not follow and spread them blindly. For example,
we should focus on the correlation without ignoring the causality. We
should also focus on the judgment of the authenticity of data and data
analysis results. We should adhere to the value choice of the unity of
theoretical accuracy and application efficiency and strive to improve
theoretical literacy, practical ability, and scientific spirit. We should track
new trends in data science, acquire new knowledge, and master new
technologies, locate data science talent training goals accurately.

Declaration of competing interest

The authors declare that there are no conflicts of interest.

References

Li, G., Cheng, X., 2012. Research status and scientific thinking of big data. Bull. Chin.
Acad. Sci. 27 (6), 647–657.

Mohri, M., Rostamizadeh, A., Talwalkar, A., 2018. Foundations of Machine Learning,
second ed. MIT Press, Cambridge.

Naur, P., 1975. Concise Survey of Computer Methods. Petrocelli Books, New York.
Rowley, J., 2007. The wisdom hierarchy: representations of the DIKW hierarchy. J. Inf.

Sci. 33 (2), 163–180.