---
source_file: "2018-State of the art in artificial neural network applications A survey .txt"
original_rel_path: "Trabalhos\Artigos\Aproveitar parcialmente\txt\2018-State of the art in artificial neural network applications A survey .txt"
category: "Artigos_Aproveitar_parcialmente"
extension: ".txt"
sha256: "ac07cceace1858a9125c9f6f1f2e11fef863bfd28a646a4f4312448256115bbe"
extracted_at: "2026-09-20T00:50:21.540513"
---

﻿Received:
25 June 2018
Revised:
19 October 2018
Accepted:
13 November 2018

Cite as:
Oludare Isaac Abiodun,
Aman Jantan,
Abiodun Esther Omolara,
Kemi Victoria Dada,
Nachaat AbdElatif Mohamed,
Humaira Arshad. State-of-the-
art in artificial neural network
applications: A survey.
Heliyon 4 (2018) e00938.
doi: 10.1016/j.heliyon.2018.
e00938

https://doi.org/10.1016/j.heliyon.2018
2405-8440/ 2018 The Authors. Pub
(http://creativecommons.org/licenses/b
Review Article

State-of-the-art in artificial
neural network applications: A
survey

Oludare Isaac Abiodun a,b,∗, Aman Jantan a,∗∗, Abiodun Esther Omolara c,
Kemi Victoria Dada d, Nachaat AbdElatif Mohamed e, Humaira Arshad f

a School of Computer Sciences, Universiti Sains Malaysia, Penang, Malaysia
bDepartment of Computer Science, Bingham University, Karu, Nigeria
cDepartment of Computer Science, Ahmadu Bello University, Zaria, Nigeria
dDepartment of Mathematical Sciences, Nasarawa State University, Keffi, Nigeria
eCalifornia University, USA
fDepartment of Computer Science and Information Technology, Islamia University of Bahawalpur, Pakistan

∗Corresponding author.
∗∗Corresponding author.

E-mail addresses: aioludare@gmail.com (O.I. Abiodun), aman@usm.my (A. Jantan).
Abstract

This is a survey of neural network applications in the real-world scenario. It
provides a taxonomy of artificial neural networks (ANNs) and furnish the reader
with knowledge of current and emerging trends in ANN applications research
and area of focus for researchers. Additionally, the study presents ANN
application challenges, contributions, compare performances and critiques
methods. The study covers many applications of ANN techniques in various
disciplines which include computing, science, engineering, medicine,
environmental, agriculture, mining, technology, climate, business, arts, and
nanotechnology, etc. The study assesses ANN contributions, compare
performances and critiques methods. The study found that neural-network models
such as feedforward and feedback propagation artificial neural networks are
performing better in its application to human problems. Therefore, we proposed
feedforward and feedback propagation ANN models for research focus based on
.e00938
lished by Elsevier Ltd. This is an open access article under the CC BY license
y/4.0/).



Article Nowe00938

2 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
data analysis factors like accuracy, processing speed, latency, fault tolerance,
volume, scalability, convergence, and performance. Moreover, we recommend
that instead of applying a single method, future research can focus on combining
ANN models into one network-wide application.

Keyword: Computer science

1. Introduction

In recent times artificial neural networks (ANNs) has become popular and helpful
model for classification, clustering, pattern recognition and prediction in many dis-
ciplines. ANNs are one type of model for machine learning (ML) and has become
relatively competitive to conventional regression and statistical models regarding
usefulness [1]. Currently, artificial intelligence (machine learning, neural network,
deep learning, robotic), information security, big data, cloud computing, internet,
and forensic science are all hotspots and exciting topics of information and commu-
nication technology (ICT). ANNs full applications can be evaluated with respect to
data analysis factors such as accuracy, processing speed, latency, performance, fault
tolerance, volume, scalability and convergence [2, 3]. The great potential of ANNs is
the high-speed processing provided in a massive parallel implementation and this
has heightened the need for research in this domain [4]. ANNs can be developed
and used for image recognition, natural language processing and so on. Nowadays,
ANNs are mostly used for universal function approximation in numerical paradigms
because of their excellent properties of self-learning, adaptivity, fault tolerance,
nonlinearity, and advancement in input to an output mapping [5].

These data analysis factors give more reason why ANNs are effective, efficient and
successful in providing a high level of capability in handling complex and non-
complex problems in many spheres of life. ANNs are capable of handling problems
in agriculture, science, medical science, education, finance, management, security,
engineering, trading commodity and art. Including problems in manufacturing,
transportation, computer security, banking, insurance, properties management, mar-
keting, energy, and those challenges that cannot be solve by the computational abil-
ity of traditional procedures and conventional mathematics. Despite these extensive
applications of ANNs, there is an increasing need to address the problem of adopting
a systematic approach in ANNs development phase to improve its performance. For
instance, an approach to address major factors and topics in a choice of data sets
(size, volume, small, large and otherwise), the accuracy of data, data instrument,
data standardization, type of data inputs, data division, and data preprocessing, val-
idations, processing and output techniques.
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

3 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
Also, other key challenges or issues that are common with ANN modeling which
have received interest and require further investigation in future. Including develop-
mental techniques that can improve designing of robust models, improving pattern
transparency and allowing useful knowledge from trained ANNs. More also is the
challenges of improving extrapolation ability, new approaches to uncertainty and
improving convergences. More also, there is continuous gradient enigma and quan-
tization of variable problems and noise. Furthermore, there is a need to address the
traversal of the error surface by utilizing quantization of variable and time-
consuming convergence problems common to most artificial neural systems (ANS)
that use supervised training. Some of these problems are highlights as follows:

(i) Improve designing of robust models: model robustness means predictive capa-
bility of ANN kinds in generalizing range of data like those used for training.
An example is using of textual data or information to improve modeling pre-
diction of the financial market. Some experts believe if that ANNs become
globally accepted and reach apex potentiality, they will not only provide a
good fit to calibration and validation of data. But will enable predictions
that will be plausible regarding model’s correlation and robustness in any
range of conditions [6, 7]. ANNs validated of error can give accurate predic-
tions for conditions like those found in trained data.

(ii) Improving of model transparency and the enabling of knowledge extraction
from trained ANNs: means the possibility of interpreting ANN models in a
way that provides a deep understanding of the effect of model inputs to outputs.

(iii) Improving extrapolation ability: extrapolation of ANN models is the capability
of the model to predict accurately outward range of data used for ANN model
calibration. ANNs perform best if they do not extrapolate above the range of
data used for design or model calibration [8, 9, 10].

(iv) New approaches to uncertainty: another limitation of ANNs including uncer-
tainty in predictions which may not be taken to account. When uncertainty is
not accounted, it becomes difficult to measure ANN predictions quality, which
can critically limits or reduces their efficacy. Although ANNs has had their is-
sues, new approaches like cognitive computing and deep learning have signif-
icantly raised the support in these fields. A synthetic machine might still be out
of reach, but systems like ANNs that help improve people’s lives are here
today.
2. Main text

2.1. Artificial neural networks

Nowadays ANNs application have become popular in various area of human needs.
Many organizations are investing in the neural networks to solve problems in various
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

4 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
fields and the economic sector which traditionally fall under the responsibility of op-
erations research [11]. What makes artificial intelligence unique is that it is mostly
proposed for data analyses by academics in the fields of social science and arts apart
from its usefulness in science and engineering [12], because of its wide applications.
For example, in recent times, artificial intelligence (AI) has been extensively applied
to optimization issues in diverse areas like industrial production and petroleum
exploration [13] and business [14] setting.

A good advantage of ANNs application is that it can make models easy to use and
more accurate from complex natural systems with large inputs [15]. The ANN is
found to be a very novel and useful model applied to problem-solving and machine
learning. ANN is an information manager model that is similar to biological nervous
systems function of the man brain. Recently, research interest in brain functionality
has rapidly increased globally [16]. According to Haykin [17], an ANN can be com-
parable machine produced to function the same way the human brain performs a
given task of interest. For example, "the human brain is big and highly efficient.
The man brain is like an information-processing machine that has a variety of com-
plex signal computing operations” [18], that can be easily coordinated to perform a
task. The main element of this brain is the unique design of their information-
processing capability. It constitutes many complexes interconnected “neurons” in
the form of elements working together to solve specific problems on daily basis.
A typical example of a neural network function is the human brain that is connected
to send and receive signals for human action. An illustration of how the human brain
function is explained in Fig. 1.

Fig. 1 is a demonstration of a connection within the brain working like a neural
network that performs intelligence reasoning functions. Brainstorming to understand
a scenario (like an internet web search platform), recognizing speech (e.g. from a
known person and unknown person) like the human brain, recognizing an image
(from an object) like the brain, can process language (translate language) like the
Fig. 1. A typical human brain structure with operational capabilities.

on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

5 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
human brain does and can perform other things like eating, riding a bicycle (self-
intuition). For more specific examples; ANNs has seen massive use in specific do-
mains, such as; diagnosis of hepatitis; speech recognition; recovery of data in tele-
communications from faulty software; interpretation of multi-language messages;
three-dimensional object recognition; texture analysis; facial recognition; undersea
mine detection; and hand-written word recognition. Thus, ANNs can learn by
example like people. In some cases, ANNs can be designed for a specific application
like data classification or pattern recognition through the learning process [19].
Learning in the human brain requires adjustments to the synaptic relationship be-
tween and among neurons, likewise the learning in ANNs [19]. Generally, an
ANN function like an imitation of the man brain [1, 20]. An architecture of a typical
NN is showed in Fig. 2.

Neural network (NN) layers are independent of one another; that is, a specific layer
can have an arbitrary number of nodes. This arbitrary number of nodes is called bias
node. The bias nodes always set as equal to one. In analogy, the bias nodes are like
the offset in linear regression given as; y ¼ ax þ b, where “a” is the coefficient of
independent “x” and then “b” is called slope. A bias major function is to provide
node with a constant value that is trainable, in addition to the normal inputs received
by the network node. Importantly, a bias value enables one to move the activation
function either to the right or the left, that can be analytical for ANN training success.
When the NN used as a classifier, the input and the output nodes will match input
features and output classes. However, when the NN is used as a function
Fig. 2. A typical neural network architecture.

on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

6 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
approximation, it generally has an input and an output node. However, the number of
designed hidden nodes essential greater than those of input nodes.
2.2. Applications of neural networks

Given this description of neural networks (NNs), how its work, and their real-world
applications and uses, indeed, NNs have wide applied to real-world problem in busi-
ness, education, economics and in many aspects of life problems. NNs are also appli-
cable to optimization method [21] intrusion detection [22, 23] and data classification
[24, 25, 26]. Classification regarded as a form of difficult optimization challenge.
Most researchers applied machine learning (ML) techniques in solving classification
problem [27, 28]. NNs are excellent identifier of trends in data and patterns [29], they
are suited for forecasting and prediction needs including those items listing (with ref-
erences to Supplementary Table 1).

The list in Supplementary Table 1 based on the successful application of ANN to
real-world problems. It summarizes neural networks application in practice which
integrated into many areas like modeling, classification, pattern recognition, and pre-
diction. Prediction of financial stability is useful in economic, management and
development of any nation, which is beneficiary for analyzing the monetary value
of any economy. Moreover, ANNs have been used successfully in the prediction
of banks success or failure and stock market estimation. Likewise, it is used exten-
sively in forecasting of weather and climatic change which is helpful in human safety
and security of properties such as buildings, environment, installation, houses, and
transportation. Furthermore, ANNs applied successfully to different areas of agricul-
ture like remote sensing, particularly in the crop type classification and crop produc-
tion estimation. Therefore, Supplementary Table 1 provides a general review of the
wide scope of problems that this neuro-Intelligence system can currently address.
2.3. ANN classification

ANN can be classified as depicted in Fig. 3.

A feedforward neural network (FFNN) is a machine learning classification algorithm
that made up of organized in layers that are similar to human neuron processing
Fig. 3. Review framework for artificial neural networks classification.

on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

7 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
units. In FFNN each unit in a layer relates to all the other units in the layers. These
layers connections with units are not all equal because each connection can have a
different weight or strength. The weights of the network connections measure the po-
tential amount of the knowledge of the network. Also, NN units are known as nodes.
The information processing in the network involves data entry from the input units
and passes through the network, flowing from one layer to another layer until it gets
to the output units. When NN operate normally, that is when its acted as a classifier,
then there will be no feedback between layers [30]. In FFNN, information trans-
mitted only in one direction, that is from the input nodes, to the hidden nodes, if
any, and then to output nodes. With this behaviour, they are called feedforward neu-
ral networks [31]. Examples of FFNNs is single layer perception and multilayer per-
ceptron. Example of a two-layered network is 3 input units, 4 units with a hidden
layer and 5 units of output layer as circles respectively in Fig. 4.

Fig. 4, has 3 input units as shown in circles, but input units is not part of any layer in
the network system, sometimes the input units are regarded as a virtual layer having
0 layers. A hidden layer is neither an input or output layers, that is Fig. 4, has 1 hid-
den layer and 1 output layer and its shows all the connections between the units in
the layers. It is clear that a layer only connects to the previous layer. FFNN applica-
tions is classified into two such as control of dynamical systems [32, 33], and spaces
where the classic machine learning techniques are applied [34]. NNs with two or
more hidden layers are called deep networks because the network has become com-
plex with more than 1 hidden layer. Unlike FFNN, the feed-backward neural
network (FBNN) can use internal state “memory” (store information) to process
sequence of data inputs. That means FFNN can logically handle task according to
first come first serve bases of inputs.

Feed-backward NN can applied to tasks like un-segmentation, and pattern recogni-
tion (connected handwriting recognition). Feed-backward neural network
Fig. 4. Two-layered feedforward neural network.

on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

8 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
application areas include mathematical proofs, seismic data fitting, medicine, sci-
ence, engineering, classification, function estimation, and time-series prediction,
etc. An architecture of FBNN illustrated as in Fig. 5.

In feedback NNs or backpropagation, connections between nodes produced a coor-
dinated graph in sequence. The coordinated graph in sequence allows feedback NNs
to demonstrate dynamic terrestrial behaviour for a time sequence. Examples are Ko-
honen’s self organizing map and recurrent neural network (RNN). RNN referred to a
standard kind of neural network which extended over time, with edges that feed into
the next time step rather than feeding into the next layer concurrent time of step.
RNN is constructed to sequences recognition, for instance, a text or a speech signal.
It has cycles within that indicates presence of short-memory in the net. Unlike a
recurrent neural network, an RNN is like a hierarchical network where the input
need processing hierarchically in the form of a tree because there is no time to the
input sequence.
2.4. Deep learning

Artificial intelligence (AI) has existed over many decades, and the field is wide. AI
can be view as a set that contains machine learning (ML), and deep learning (DL).
The ML is a subset of AI, meanwhile, DL, in turn, a subset of ML. That is DL is an
aspect of AI; the term deep learning refers to artificial neural networks (ANN) with
complex multilayers [35]. The distinction between deep learning and neural net-
works like feedforward NNs and feed backward NNs lies in their characteristic.
Deep learning has more complex ways of connecting layers, also has more neurons
count than previous networks to express complex models, more also with more
computing power to train and further has automatic extraction of the feature.
Fig. 5. Feed-backward neural network.

on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

9 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
Therefore, DL defined as a NN with a broad variables and layers with a single basic
network architecture of unsupervised pre-trained networks, convolutional NNs,
recursive NNs, and recurrent NNs. The technological development in the field of
AI has expanded over time as showed in Fig. 6.

DL methods have been found to be fitting for big data study with remarkable success
in its applied to speech recognition, computer vision, pattern recognition, recom-
mendation systems, and natural language processing [36]. Nowadays, the innovation
of DL in image identification, object detection, image classification, and face iden-
tification tasks have great success. The research by Zhou et al. [37] presents an appli-
cation of DL in object detection task and its speedy use in the domain of computer
vision. Similarly, the recently reviewed work by Liu et al. [36] discusses popularity
of DL architectures and their industrial and practical applications. The review pro-
vided a comprehensive knowledge on four DL architectures like, deep belief
network, restricted Boltzmann machine, autoencoder, and convolutional neural
network (CNN).

One of the most common deep NNs is the convolutional NN called CNN. A CNN is
a standard NN that extends across space via shared weights. CNN is designed to
recognize images by having convolutions within, that can recognize the image of
an object. CNN has multiple layers; including fully-connected layer, pooling layer,
convolutional and non-linearity layers. The fully connected layers and convolutional
layers have parameters, however non-linearity layers and pooling do not have pa-
rameters. Study have shown that CNN has an excellent performance in ML problems
[35]. Particularly, in the applications to image data, like the most extensive image
classification dataset, natural language processing, and computer vision.
Fig. 6. Artificial intelligence development and expansion.

on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

10 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
The major concept of deep learning (DL) is learning data representations by
increasing the quality of handling the ideas rather than events (abstraction) levels.
Mostly in all levels, a significant amount of quality ideas or abstraction representa-
tion at a advance level are known through definition regarding fewer quality ideas or
non-representations at the basic levels. This type of stages of learning, growth or hi-
erarchical process of learning is superb because it can enable a system to fathom
complex or multi-complex presentations accurately from raw data [38, 39]. This su-
perb characteristic is making deep learning applicable to different fields.

To fast tract classification, recognition of patterns in biological data, many methods
of artificial intelligence particularly the machine learning has been proposed [38, 40,
41]. Artificial intelligence (AI) is a combination of reinforcement learning (RL) and
deep learning (DL), thus mathematically, AI ¼ RL þ DL. Machine learning has
become the latest model to digital evolution, that is making computing processes
more cost-effective, efficient, strong, dependable and reliable.

Conventional machine learning techniques widely classified into two sets that is, su-
pervised and unsupervised. The supervised learning has the capability of classifying
objects in a pool with possibility of given features or attributes nor annotations. A
typical example of supervised learning is when students have written an exam,
and having the exam marked by the teacher and shown which questions the students
answered incorrectly. After being shown the correct answers, the students are ex-
pected to learn then understand how to answer those questions correctly.

But the unsupervised learning methods form clusters or groups between and among
the objects in an area to identify likeness, then use similarity for classifying un-
knowns. Example of unsupervised learning is the man that is learning how to ride
a car by himself. He will start by entering the car and start the engine with the igni-
tion key, then put down the clutch and put the car in first gear and press the accel-
erator for the car to move forward and then manage to control the steering. He
continually practices the driving steps in a large open field and gradually master
the driving technique, and then over time start to enter the road to drive skillfully.

The reinforcement learning (RL) category, enables a system or an agent learn from
the previous experiences gains in the environment through interaction and observing
the results of these interactions. The interaction helps to mimic or imitates the basic
pattern in which humans and animals learn. An agent of RL can act, and each act
influences the agent’s future condition, a scalar reward signal measures RL success.
RL goal is to choose actions that maximize future gain. In nutshell, DL, is a general-
purpose framework in making decision. A framework that present learning given
require objective from raw inputs by applying minimal domain knowledge. For
instance, RL completely bypasses the problem of rules learning in a task. The
learning agent learns by participating in the given activity.
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

11 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
An example is a game of Chessboard, to determine the best action play move, the
players need to think about various possibilities and strategies. The amount of pos-
sibilities is potentially big that it is not possible to perform a brute-force search.
However, if a machine is to be built to play such a game using traditional techniques,
there will be a necessity to specify many rules to cover all these possibilities. Rein-
forcement learning completely bypasses this problem. Examples of RL include value
based deep RL, model based deep RL and policy based deep RL.

While common supervised artificial neural networks and their adaptations include
single-layer perceptron (SLP) [10, 31], multilayer perceptron (MLP) [42, 43], and
linear classifiers [44, 45]. Also, popular supervised ANNs include support vector
machines (SVMs) [46, 47], k-nearest neighbours (kNNs) [48]. More also in the cate-
gory of popular supervised ANNs are Bayesian statistics [49], decision trees [50] and
hidden Markov model (HMM) [51]. Meanwhile, some common unsupervised
methods include k-means [52], expectation maximization [53], and autoencoders
[54]. Other unsupervised approaches in literature are density-based [55], self-
organizing maps [56], clustering [57] and fuzzy [58].

Kernel-based neural networks methods are a class of algorithms for pattern analysis,
like SVM (support vector machine). Kernel functions or algorithms used in shallow
architectures, for example support vector machines (SVMs), or multilayer kernel
machines (MKMs). An investigation study by Cho and Saul [59], evaluates
MKMs and SVMs with kernel functions to demonstrate advantages of deep NN ar-
chitectures. The study highlighted the usefulness of kernel-based neural networks in
the applications to optical character recognition and DNA analysis. The research by
Camps-Valls, and Bruzzone [60], proposed kernel-based techniques for classifica-
tion of hyperspectral image, with main characteristics of various kernel-based
methods. The result demonstrates the successful performance of standard support
vector machines (SVMs) that regularized radial basis function NNs (Reg-RBFNN),
AdaBoost (Reg-AB) and kernel Fisher discriminant (KFD) analysis.

ANNs has significant advantages over statistical models when both are relatively
compared. In ANN models there are no assumptions about data properties or data
distribution. Therefore, ANNs are more useful in practical application. Also, unlike
some statistical models that require certain hypothesis for testing, ANN models do
not require any hypothesis. ANNs are very flexible, data reduction models, encom-
passing nonlinear regression models, and discriminant models. More also, unlike the
support vector machine, extreme learning machine, and random forest, ANNs are
more fault tolerant. That is, they can handle incomplete data and noise, they can
solve non-linear problems, Also, trained ANNs, can generalize at high speed and
make predictions. Furthermore, ANNs are scalable when relatively compared to
the support vector machine, extreme learning machine, and random forest.
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

12 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
Interestingly, DL techniques attracted more research attention since year 2006. DL
has the built-in ability to solve the defect of traditional paradigms dependent on
hand-built materials. Also, DL approaches have been useful in big data technique
with performance applications to pattern recognition, natural language processing,
recommendation systems, speech recognition, and computer vision.
2.5. Modeling

Generally, modeling is the process of presenting a real-world phenomenon or object
as a set of mathematical expression. However, neural network modeling is a process
representing the way the nervous system functions. That is, a NN is a simplified rep-
resentation of how the man brain processes information. Its function by simulating
many interconnected processing units that resemble idea versions of neurons. It is
the most common optimization paradigm used in optimizing a neural network.
Recently gradient descent used in updating weights in a NN model, that is updating
and changing the model’s parameters in a direction to minimize the Loss function.

A study by Ludermir, Yamazaki, and Zanchettin [61], proposed a new method for
NN global optimization. The method combines backpropagation algorithm, anneal-
ing, and tabu search, to produce an automation for generating networks with low
complexity and high classification. The results showed that the new method is better
than the previous studies obtained by the most used optimization approaches.
Recently, researchers synthesized artificial enzymes that functions or operates in
the metabolism of living cells. These artificial enzymes used cell’s own energy
that enable hydrogen gas production from solar energy [62]. ANNs have applied
in many ways like in system control [63], pattern recognition [64], power systems
[65], robotics control [66], forecasting [67], manufacturing [68], social sciences
[69], Art [70], optimization [71], psychological sciences [72], signal processing
[73] etc.

In an optimizer modeling approach to a solution of reusability problem. An example
of a practical approach to modeling in the optimizer for a software architecture. A
published work by Delinchant et al. [74] discusses an optimization framework in
software components paradigm for sizing. Delinchant et al. work presents a frame-
work system design based on optimization. It then highlights, a generator (analytical
expressions of the framework system), an optimization service, the component stan-
dard and the pattern of using the designed framework. The result demonstrates how
the framework system for the software components can be used in building new gen-
erations that optimized environment. That allow capitalization and reutilization by
the combined software packages and optimization algorithms. Thus, the approach
showed the possibility of building a global software architecture that optimized sys-
tems and components.
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

13 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
In measuring a good prediction model to predict the expected outcome, a loss func-
tion required. That is the group or class of functions that minimized is called “loss
functions”. A most popular used method of finding the minimal point of a function
referred to as gradient descent. DNNs are currently among the most popularly used
classifiers. In modeling on loss function, a paper by Janocha, and Czarnecki [75],
investigated the effect of loss functions choices on deep models and its learning dy-
namics, and the resulting classifiers robustness to different effects. Two experiments
(L1 and L2) performed on classical datasets. The result shows that L1 and L2 losses
are, quite interesting, that justified classification objectives for deep neural nets
because it gives probabilistic interpretation regarding expected misclassification.

In finding the optimum design that provides a lightweight and high quality at the same
time, it is significant to have effective and efficient prediction methods at the initial
design stage. In a research work on weight optimization method, the paper by Yu,
and Chi [76], proposed a weight model optimization in credit evaluation, based on
the concept that the optimal is the weight. That is, after empowerment the result of
credit evaluation should has maximum discriminating power to differentiate non-
default from default customers. The empirical results demonstrate that the discrimi-
nating power of credit evaluation was the strongest compared with the three types
of weight models, like t-value, mean square error, and variation coefficient.
2.6. ANN emerging successes and applications

In the recent times various successful used of ANNs emerged in catalysis, meteo-
rology, biology, chemistry, physics, nuclear physics, high-energy physics, and other
areas of science. Nowadays, ANN has found uses in a new area such as in catalyzing
especially in the chemical industrial sector. Catalysis is term as the significant energy
in the modernization process of chemical industries. It ensures effective, efficient and
successful use of finite natural resources, it prevent waste and air pollution, and pro-
vides safety for the industrial sector. Catalysis become the foundation of large scale
operations regarding size in chemistry and petrochemistry environment. However,
as demand changes, new environmental challenges now require new catalytic solu-
tions. For example, changed in the energy economy has driven an increasing demand
for coal and gas, hence given room for new challenges for catalytic technology in the
areas like liquefaction in material science [77, 78].

Recently, there have been reported cases of ANNs applications to catalysis research
in the literature. The reviewed paper by Li, Zhang, and Liu [79], show how ANNs
applied to catalysis helps people in addressing the complex problems and then accel-
erating the progress of the catalysis utilization. The reviewed paper further showed
how ANNs applied in many ways to catalysis prediction, new catalysts design, and
understanding of catalytic structures which produced effective result. Likewise,
research by Corma et al. [80] demonstrates how artificial NNs applied to modeling
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

14 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
catalytic data in combinatorial catalysis and to predicting a new catalyst composition
for ODHE (oxidative dehydrogenation of ethane).

In another development research on an accurate description of chemical processes
using computational methods like density functional theory (DFT). Behler and Par-
rinello [81], introduces a new breed of NN model of DFT, that gives the energy as a
function of all atomic positions in systems with arbitrary size and in various orders of
magnitude that is faster than DFT. The high level of accuracy of the NN method is
shown for bulk silicon compared with DFT. This NN approach is generic which can
be apply to all kind of periodic and nonperiodic systems.

Recently, a generalized ML input representation was applied by quantification and
concentrations of blended solutions in addressing the problem of determining
intrinsic trends in CO2 solubility under a specific condition. The research orches-
trated by Li, and Zhang [82], applied general regression NN (GRNN) algorithm
in fitting intrinsic trends or movement of CO2 solubility with a minimal amount
of experimental data. Which resulted in the average RMSE (root mean square error)
less than 0.038 mol CO2/mol of solution. The study has shown that applied gener-
alized input representation, could provide a better comprehension of the inherent
trends of CO2 solubility in a blended amount of solutions.

ANNs are useful and applicable in system modeling like in implementing system
identification and complex mappings. For instance, the application of NNs to renew-
able energy challenges have shown tremendous success. In 2001, an investigation by
Kalogirou [83], applied ANN to energy like solar regarding modeling and design of
a solar steam generating plant. The experimental result demonstrates prediction for
speed, load, and error.

Wavelet networks are been used extensively and effectively in different engineering
fields for classification, identification and control problems. Wavelet networks are
feed forward networks that uses wavelets as activation functions. ANNs application
to solar radiation data forecasting with adaptive wavelet network has been useful.
The most recent work by Li, and Liu [84], uses an adaptive wavelet network archi-
tecture in discovering an appropriate model for forecasting the daily total amount of
solar radiation. The daily total amount of solar radiation is considered the most sig-
nificant in the prediction of the performance of renewable energy like solar, impor-
tantly in sizing photovoltaic (PV) phenomenon of power systems. That is in the
conversion of light into electricity. The experimental results demonstrate that the
ANN model predicts daily total amount of solar radiation parameters with an accu-
racy of 97% with a mean absolute percentage error of 6%. Also, Li, and Liu proposed
a model on the optimization of the solar water heater and performance prediction us-
ing a knowledge-based machine learning technique. The result demonstrates that the
model generalization that can applied in different locations even for weather data,
like ambient temperature and sunshine period.
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

15 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
In recent years ANN application to chemistry and physics problems has increasingly
popular and successes [85]. Many applications of approximation techniques and
standard approaches to data fitting are performing better in NN. NN provide more
accuracy with a lower number of adjustable parameters than any other methods.
Learning in NNs is understood when it rebuilds hypersurfaces together with a sam-
ple points, generalization, and interpolation. NNs apply sigmoidal functions to re-
buildings or transformations, stated in most physics and chemistry problems.
Thus, resolving an arbitrary data fitting issue by applying a single layer net architec-
ture if there is no restriction in sigmoidal functions applied [85].

Neural networks application in physics has witnessed a remarkable success. The
research by Lynch et al. [86], describes new opportunities for applying NNs to phys-
ics and mapping kinds of physics related problems, especially in the field of science
and engineering problem. ANN has been found useful in predicting the concentra-
tions of radioactivity. An understanding the levels of radioactivity values with values
of other variables in the environment can be apply to train a network to estimate the
next levels of radioactivity. Hence, accuracy of the NN method can be better than
other approaches in certain monitoring areas.

Nuclear theory main goal is to predict nuclear structure and nuclear reactions from
the fundamental theory of high cohesion interactions, and quantum chromodynamics
(QCD). With the current superb high-performance computing (HPC) systems, many
ab initio methods, like the No-Core Shell Model (NCSM), have been designed to
calculate the chemical properties of atomic nuclei. However, to accurately calculate
the properties of atomic nuclei, there are a plethora of theoretical and computational
challenges involves. To overcome this problem, a most recent study on atomic nuclei
properties prediction by Negoita et al. [87] proposes a feed-forward ANN for pre-
dicting the properties of atomic nuclei such as ground state (gs) energy and ground
state (gs) point proton root-mean-square (rms) radius. The result demonstrates that
FFANN could predict properties of the 6Li nucleus like the gs energy and the gs
point proton rms radius. The result satisfied the ideal physics condition. An impor-
tant advantage of the ANN method is that it does not require mathematical relations
of the input data and output data. Importantly, ANN applications to Physics and
Chemistry problems should be compared with other methods like statistical tech-
niques and data fittings procedures for the performance measure.
2.7. ANN models in different application areas

Many artificial neural network techniques have been adopted in the academia and
industries to address the challenges in computer vision, speech and pattern recogni-
tions, face alignment, and detection. These include;
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

16 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
2.7.1. Speech recognition

The application of ANNs has become divergence and understood in the capability of
its successes in speech or communication recognition. In the past decades, ML algo-
rithms have applied widely in areas like acoustic modeling and ASR (automatic
speech recognition) [88].
2.7.2. Computer vision

Computer vision aims at making computers to accurately understand and process vi-
sual data efficiently like videos [88] and images [89, 90, 91]. Main goal of computer
vision is to provide computers with the kind of ability of man brain functionality.
Theoretically, computer vision alludes to the logical control which studies how to
separate data from images in artificial frameworks. Sub domains of computer vision
include object detection and object recognition, object estimation, object position,
event detection, scene reconstruction, image restoration, image editing, video
enhancement, and statistical learning. Hence, in computer vision, ANN models
are very useful.
2.7.3. Pattern recognition

The recent improvement in deep learning models has given novel ways to deal with
the issue in recognition of a pattern or pattern recognition (PR). PR is a scientific area
that focus in identification of sequence in each input [92, 93]. PR is a general concept
that surrounds various subdomains such as speech tagging, regression, sequence la-
beling and classification. There are rapidly increasing needs for information process-
ing and output, due to industrial development, that has new trend and challenges to
PR.
2.7.4. Face alignment

Face alignment plays a role that is significant in diverse visual applications. In recent
times ANNs has claimed successes in face alignment [94, 95, 96] and face recogni-
tion [97, 98, 99] and other models [100] have shown successes. Interestingly DL
techniques can be applying to explain genetic variants to identify pathogenic variants
[101, 102]. Usually, combined annotation dependent depletion algorithm is popu-
larly applied to interpret the coding and non-coding variants.
2.7.5. Detection

Detection in medical diagnosis, security, image objects, financial irregularity, a fault
in a system, are being enhanced through ANNs application. Thus, ANN plays an
essential role in the detection, particularly when applied to breast cancer [103,
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

17 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
104, 105, 106]. The performance of ANN can be relatively compared with other ap-
proaches in crime detection such as DNA and activity profiling [107] and the use of
big data for financial crime detection [108]. Despite the many publications in the uti-
lization of NN in different medical challenges, but there are few reviews study avail-
able that explain the architecture in improving the detection methods regarding
performance, accuracy, sensitivity, and specificity. Thus, detection capability is
commonly known subdomain or computing in computer vision which seeks to un-
derstand, locate, classify or differentiate the targeted image objects. An example dur-
ing detection tasks, an image can be scanned to know certain special features or
characteristics. For instance, using of image detection in medical diagnosis, espe-
cially abnormal cells or tissues in medical images.

Normally, traditional methods are base on hand-designed features and contrast infer-
ence mechanisms. The DL techniques require raw image data only [109, 110, 111,
112]. Also, DL techniques applied to Glaucoma detection with promising results
[113, 114, 115]. More also, ANN has employed in image change and computer
vision detection in both civil and military challenges. Recently, image detection
applying in remote sensing, disaster evaluation, videoing and surveillance. Further-
more, ANNs or deep learning techniques has been applying to human-robot interac-
tion systems that yielded results [116, 117, 118].
2.8. Comparison of different ANN models

This section highlights discusses, compares, summarizes and critiques more than
eighty research articles on artificial neural network model’s application to the diverse
area of the economy. The comparison was made based on (i) author(s)/year of pub-
lication (ii) ANN modeling (iii) ANN area of application (iii) studied contribution to
human challenges (with references to Supplementary Table 2) [11, 119, 120, 121,
122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137,
138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153,
154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169,
170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185,
186, 187, 188, 189, 190, 191, 192, 193, 194].
2.8.1. Summary and critiques

The comprehensive review has shown that interest in ANN applications exploded
over the past two decades. The results indicate that the selected research articles
are recent because they were majorly published between the year 2009e2018 and
focuses on developmental and technological issues regarding ANN. The survey
covers various areas of ANN applications such as computer security, network secu-
rity, science and engineering, medical science, biology, ecology, nuclear industry,
electricity generation, management, mineral exploration.
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

18 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
Other areas of application are; crude oil fractions quality prediction, crops, water
treatment, policy and businesses like banking, insurance, the stock market, money
laundering and other financial institutions for crime detection. The field of applica-
tion varies from science, engineering, socio science, humanity and to art-related
fields. From the survey of various articles, it became clear that the artificial neural
network application has no boundary. ANNs has attracted the most attention from
researchers in recent time, for instance, the study found that forecasting of crops
and animals yield are helpful in agricultural development.

Interestingly, this application of ANN has led to an increase in agricultural produc-
tion which has enhanced food security in many nations. In the past two decades,
ANNs have applied in different fields of agricultural, particularly to crop area esti-
mation and classification. Also, agricultural data can be predicted using a neural
network. There are diverse approaches proposed for data analysis such as neural
network models; examples are; feedforward artificial neural network, back propaga-
tion neural networks, probabilistic neural network. Others include supervised asso-
ciating networks, multi-layer perceptron neural network architectures, learning
vector quantization, and multi-layer neural network.

Although, the study by Kitchens, and Harris [195], on ANN application to detection
of fraud in insurance business and finance, demonstrates fraud detection process effi-
ciently. However, the result needs comparison with other approaches like data min-
ing, regression model and other statistical models for evidence of successes.

Though, the research by Fanning and Cogger [149], on the application of ANN for
fraud detection in management show evidence of success in fraudulent detection us-
ing ANN in financial statements. Nevertheless, the result needs to be compared with
other current techniques if it performed better or outperformed state-of-the-art detec-
tion techniques. More also, even though ANN application is quite novel, one must
not ignore that nowadays there are other novels criminal detection techniques with
graphical and programming applications like graph-theoretic anomaly detection and
inductive logic programming.

Although,ANN toolsmake it simple, easy and faster for data analysis to enable not only
the discovery of a newmethod for businesses, industrial, and educational topologies but
also cross-product, cross-channel and cross-customer performance.Nevertheless,ANN
is not necessarily a panacea; there has to be information and communication technology
(ICT) involvement in making the data sources available and, of course, ANN tools do
not exclude the need for data cleansing.But it gives newopportunities to anorganization
looking to tackle management challenges such as improvement of materials, product,
services, financial crime, and so on via new means.

With emerging technologies such as data mining, genetic algorithms, hybrid models,
mathematical models, big data application especially in crime detection and
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

19 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
prevention [185, 196]. The evolution of computer and the internet has the influence
of rapid technology and digital media growth on every aspect of human lives [197,
198]. In addition to extensive interactive software application [199]. Researchers can
follow adequate artificial intelligence application mechanisms to achieve huge suc-
cess in the diverse field of endeavours. In nowadays of global computing, there are a
plethora of benefits in NNs. Since capability to learn during and after training makes
ANN very powerful and flexible. Also, ANN do not require paradigm before per-
forming a specific task, that is, without the need in understanding the external or in-
ternal mechanisms of the task before implementation [200].
2.8.2. The result of ANN application

The result of ANNs application to different areas of lives and disciplines as found in
the literature is presents in Table 1.

Table 1 indicates that ANN models are useful in classification, pattern recognition,
claustering, optimisation and prediction. The relationships among many areas of
ANN applications further presented in Fig. 7.
Table 1. Summarized result on ANNs application regarding prediction, pattern
recognition and Classification.

Example of many fields Prediction Pattern recognition Classification Total
of applications of ANNs

Security 20 18 2 40

Science 25 25 2 52

Engineering 22 7 2 31

Medical science 10 5 2 17

Agriculture 3 3 2 7

Finance 10 15 2 27

Bank 5 15 2 22

Weather and climate 2 15 2 19

Education 30 15 2 47

Environmental 10 15 2 27

Energy 5 15 2 22

Mining 2 15 2 19

Policy 2 2 2 6

Insurance 5 4 2 11

Marketing 5 5 2 12

Management 40 2 2 44

Manufacturing 12 15 5 32

Other fields 52 11 10 71

on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

Fig. 7. Reviewed ANN applications framework.

20 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
The correlation among the distinct fields further reveals that ANN can apply to any
areas of studies, industries, and profession. The histogram reveals the areas of appli-
cation of ANN in security, science, engineering, medical science, agriculture,
finance, banking, weather and climate, education, environmental, energy, mining,
insurance, marketing etc. Therefore, interested researchers can explore the ANN
application in these areas or many other emerging areas for future research for better
solution to problems in their fields. Since there is always an algorithm, model,
scheme, and framework for any problem.
3. Conclusions

The survey was comprehensive with a discussion on how NN could applied to
address human needs. ANNs has many names as found in the literature such as; con-
nectionism/connectivist models, adaptive systems, parallel distributed processing
models, self-organizing systems, neuromorphic and neurocomputing systems
[201, 202, 203, 204].

The ANNs application areas considered in the survey include; computer security,
medical science, business, finance, bank, insurance, the stock market, electricity gen-
eration, management, nuclear industry, mineral exploration, mining, crude oil frac-
tions quality prediction, crops yield prediction, water treatment, and policy. It is
interesting to know that neural network data analysis adds accuracy, processing
speed, fault tolerance, latency, performance, volume, and scalability. Many new
and enhanced data management and data analysis approaches help in the manage-
ment of ANN. Creating analytics from the available data that aid in largely priori-
tizing information and provide its human business value. The ANN analytics in
turn help in combating challenges and mitigate any possible risks.
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

21 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
Therefore, based on data analysis factors such as accuracy, processing speed, la-
tency, performance, fault tolerance, volume, and scalability, an evaluation was
made of the ANN techniques. Then, proposes that neural-networks models such
as FFBP and hybrid model using neural networks are performing better for imple-
mentation of human problems when compared to other approaches currently in prac-
tice. Also, the study proposes hybrid neural networks models and genetic algorithms
(GA) for a better performance regarding effectiveness and efficiency.

ANN are new computational model with rapid and large uses for handling various
complex real world issues. ANNs popularity lies in information processing charac-
teristics to learning power, high parallelism, fault tolerance, nonlinearity, noise toler-
ance, and capabilities of generalization.
3.1. Suggestions

Based on the reviewed literature, some areas of improvement can be suggested to
professionals, researchers and newcomer researchers for further research and future
research development. The BPNNs and FFPNNs have the potential for modeling
variables. In optimizing BPNNs and FFPNNs performance, a systematic approach
is requiring in the model development process. Therefore, the following suggestions
are stated.

1. Transformation of data. The past and current studies indicate that it is unneces-
sary to transform or change data not normally or usually distributed that reveal
non-regular periodic development or variant. Meanwhile, the modification of
heteroscedasticity and trends in data are encourage. Also, data normalization
and scale to commensurates with function transfer in output layer.

2. Determining of appropriate inputs model. Input variables determined with the
support of a priori knowledge, using a stepwise model-building method or
analytical method like cross-correlation technique.

3. Network geometry choice. One hidden layer may be enough as adequate in most
network practical uses. However, mathematical expression could determined the
upper bound of hidden layer nodes required to approximate continuous function.
Except if nonconvergent techniques, like cross-validation, the connection be-
tween the quantity of training and the quantity of hidden layer units likewise
should be considered. The relationship can be investigated with the guide of
the rules given in some literature.

4. Researchers can focus on network characteristic at variable specification phase.
Also, it is useful to conduct trials in determining required local minimum in the
error surface, and oscillations in the R.

5. Forecasting with continuous training, with different step sizes taken in weight
space. These steps can be useful when selecting appropriate network parameters
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

22 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
like (transfer function, momentum, epoch size, learning rate, and error) and how
many training samples in the network for a case study.

6. Validation of model. The validation of model is necessary for standardization
and practical scenarios of ANNs for optimization of performance.
3.2. Future directions

This research has many areas in need of further investigation. Further research is
requiring in the following areas:

(i) A greater focus on adaptive dynamic programming (ADP) could produce
interesting findings that account more for significant contributions in the
area of brain research and computational intelligence

(ii) Emerging topic in engineering and computer science include parameter
adjustment technique in machine learning algorithms. The successful use
of algorithms optimization in adjusting network variables should be well
studied.

(iii) Further investigation into the applications of reinforcement-learning, unsu-
pervised, semi-supervised methods to the deep neural network for complex
and multi-complex systems.

(iv) Future research should concentrate on the use of intelligent analysis such as
neural network models, backpropagation neural networks, probabilistic neu-
ral network, supervised associating networks, multi-layer perceptron neural
network architectures, learning vector quantization, multi-layer neural
network, and hybrid neural network models. These are because the areas
can provide better performance in the application of neural network to diverse
challenges of life.

(v) Since the use of inferential statistics and neural networks can be more predic-
tive in data analysis. Hence, the predictive approach can also be another focus
in the study of the subject.

(vi) Research is requiring in the execution of DL algorithms for communication
materials like mobile gadgets. As recently, DL chips idea emerged that is at-
tracting research interest.

(vii) Public awareness training on artificial network neural models should continue
regularly, especially on the need for providing useful information using
empirical analysis and digital data.

(viii) More investigation is requiring in the stability analysis of deep NN because,
in recent times, the DNNs stability analysis has become a hot topic for
research focus due to its advantages in many industrial sectors.
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

23 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
(ix) With the new trend in big data technique, DL would be useful where large
amounts of un-supervised data are applied. It would be interesting to
construct DL models that can learn from fewer training data, particularly
for visual and speech recognition systems.

(x) Further research should be a focus on the use of DNNs to nonlinear net-
worked control systems. More understanding of complicated dynamics
would help us establish how to obtain better performances in control, and
filtering capability effectively and efficiently.

(xi) The governments and institutions need to provide funding into diverse areas
of application of neural networks for success, especially in this era of modern
education, technology advancement, industrial growth, economic challenges,
artificial intelligence development, and information and communication
revolution.
3.3. Other areas of further research

It would be a good idea for further research to be carried out in the following areas:

(i) Genetic algorithms (GA) for better performance regarding effectiveness and
efficiency.

(ii) Brain research focusing on RL and ADP (adaptive dynamic programming)
and RL to produce more success in performing intelligent optimization.

(iii) Hybrid neural networks models for better performance regarding effective-
ness and efficiency.

(iv) Research into possibilities in the integration of neural networks with other ex-
isting or developing technologies.

(vi) There is a need for more future research into the application of ANN technol-
ogy in businesses, industries, energy and agriculture for development and
wealth creation.

(vii) Research focus on determining if the more profitable trading system can be
implemented using hybrid intelligent systems, expert systems, genetic algo-
rithms, combining fuzzy logic and ANNs.

(viii) Research to explore the possibility of using ANNs to forecast time series, and
the integration of expert systems and fuzzy logic in determining trading
signals.

(ix) An exploration into the possibility of using genetic algorithms to select input
variables and optimal parameters for a system.

Meanwhile, the research on ANNs applications will attain more significant progress
in the nearest future.
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

24 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
Declarations

Author contribution statement

All authors listed have significantly contributed to the development and the writing
of this article.
Funding statement

This research was partially supported by two organizations. Center for Cyber Safety
and Education, United States Internal Revenue segregated fund of (ISC)2, Inc. Code.
EIN: 45-2405127 through the (ISC)2 graduate cybersecurity scholarship award, 311
Park Place Blvd. Suite 610 Clearwater, FL 33759 USA. Also, by Fundamental
Research Grant Scheme (FRGS) for ‘‘content-based analysis framework for better
email forensic and cyber investigation” [203/PKOMP/6711426], SFRG Lab, School
of Computer Sciences, Universiti Sains Malaysia, Penang, 11800, Malaysia.
Competing interest statement

The authors declare no conflict of interest.
Additional information

Supplementary content related to this article has been published online at https://doi.
org/10.1016/j.heliyon.2018.e00938.
Acknowledgements

The authors express appreciation to the staff and students of Security & Forensic
Research Group (SFRG) Laboratory, School of Computer Sciences, Universiti Sains
Malaysia, Penang Malaysia for their material support during this study. Also, we
thank reviewers of this work for their valuable comments and suggestions that
improve the presentation of this research effort.
References

[1] V.S. Dave, K. Dutta, Neural network-based models for software effort esti-
mation: a review, Artif. Intell. Rev. 42 (2) (2014) 295e307.

[2] H. He, E.A. Garcia, Learning from imbalanced data, IEEE Trans. Knowl.
Data Eng. 21 (9) (2009) 1263e1284.

[3] A. Mozaffari, M. Emami, A. Fathi, A comprehensive investigation into the
performance, robustness, scalability and convergence of chaos-enhanced
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

25 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
evolutionary algorithms with boundary constraints, Artif. Intell. Rev. (2018)
1e62.

[4] N. Izeboudjen, C. Larbes, A. Farah, A new classification approach for neural
networks hardware: from standards chips to embedded systems on chip, Ar-
tif. Intell. Rev. 41 (4) (2014) 491e534.

[5] D. Wang, H. He, D. Liu, Intelligent optimal control with critic learning for a
nonlinear overhead crane system, IEEE Transact. Ind. Inf. 14 (7) (2018)
2932e2940.

[6] F.Z. Xing, E. Cambria, R.E. Welsch, Natural language based financial fore-
casting: a survey, Artif. Intell. Rev. (2018) 1e25.

[7] G.B. Kingston, H.R. Maier, M.F. Lambert, Calibration and validation of neu-
ral networks to ensure physically plausible hydrological modeling, J. Hydrol.
314 (1e4) (2005) 158e176.

[8] I. Flood, N. Kartam, Neural networks in civil engineering. Principles and un-
derstanding, J. Comput. Civ. Eng. 8 (2) (1994) 131e148.

[9] A.W. Minns, M.J. Hall, Artificial neural networks as rainfall-runoff models,
Hydrol. Sci. J. 41 (3) (1996) 399e417.

[10] A.S. Tokar, P.A. Johnson, Rainfall-runoff modeling using artificial neural
networks, J. Hydrol. Eng. 4 (3) (1999) 232e239.

[11] M.A. Boyacioglu, Y. Kara, O€ .K. Baykan, A predicting bank financial failures
using neural networks, support vector machines and multivariate statistical
methods: a comparative analysis in the sample of savings deposit insurance
fund (SDIF) transferred banks in Turkey, Expert Syst. Appl. 36 (2) (March
2009) 3355e3366.

[12] S. Haykin, N. Network, A comprehensive foundation, Neural Network. 2
(2004) 41.

[13] H. Rahmanifard, T. Plaksina, Application of artificial intelligence techniques
in the petroleum industry: a review, Artif. Intell. Rev. (2018) 1e24.

[14] O. Araque, I. Corcuera-Platas, J.F. Sanchez-Rada, C.A. Iglesias, Enhancing
deep learning sentiment analysis with ensemble techniques in social applica-
tions, Expert Syst. Appl. 77 (2017) 236e246.

[15] M. Jahnavi, Introduction to Neural Networks, Advantages and Applications,
towards Data Science, Jul 9, 2017. Available at: www.deeplearningtrack.com
https://towardsdatascience.com/introduction-to-neural-networks-advantages-
and-applications-96851bd1a207.
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

26 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
[16] D. Wang, H. He, D. Liu, Adaptive critic nonlinear robust control: a survey,
IEEE Trans. Cybern. 47 (10) (2017) 3429e3451.

[17] S. Haykin, Neural Networks and Learning Machines, third ed., McMaster
University Hamilton, Ontario, Canada, 2009.

[18] S. Haykin, Neural networks expand SP’s horizons, IEEE Signal Process.
Mag. 13 (2) (1996) 24e49.

[19] C. Stergiou, D. Siganos, Neural Networks 1996, 1996.

[20] T.J. Huang, Imitating the brain with neurocomputer a “new” way towards
artificial general intelligence, Int. J. Autom. Comput. 14 (5) (2017) 520e531.

[21] S.S. Haykin, Kalman Filtering and Neural Networks, Wiley, New York,
2001, pp. 221e269.

[22] W. Yu, H. He, N. Zhang, Advances in Neural Networks, ISNN 2009 6th In-
ternational Symposium, 2009.

[23] W. Fan, N. Bouguila, D. Ziou, Variational learning for finite Dirichlet
mixture models and applications, IEEE Trans. Neural Network. Learn.
Syst. 23 (5) (2012) 762e774.

[24] K. Saravanan, S. Sasithra, Review on classification based on artificial neural
networks, Int. J. Ambient Syst. Appl. (IJASA) 2 (4) (2014) 11e18.

[25] M. Martínez-Porchas, E. Villalpando-Canchola, F. Vargas-Albores, Signifi-
cant loss of sensitivity and specificity in the taxonomic classification occurs
when short 16S rRNA gene sequences are used, Heliyon 2 (9) (2016)
e00170.

[26] F. Abid, L. Hamami, A survey of neural network based automated systems
for human chromosome classification, Artif. Intell. Rev. 49 (1) (2018)
41e56.

[27] K. Das, R.N. Behera, A survey on machine learning: concept, algorithms and
applications, Int. J. Innovat. Res. Comput. Commun. Eng. 5 (2) (2017)
1301e1309.

[28] R. Boutaba, M.A. Salahuddin, N. Limam, S. Ayoubi, N. Shahriar, F. Estrada-
Solano, O.M. Caicedo, A comprehensive survey on machine learning for
networking: evolution, applications and research opportunities, J. Internet
Serv. Appl. 9 (1) (2018) 16.

[29] F.N. Ogwueleka, S. Misra, R. Colomo-Palacios, L. Fernandez, Neural
network and classification approach in identifying customer behavior in the
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

27 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
banking sector: a case study of an international bank, Hum. Factors Ergon.
Manuf. Serv. Ind. 25 (1) (2015) 28e42.

[30] M.T. Hagan, M.B. Menhaj, Training feedforward networks with the Mar-
quardt algorithm, IEEE Trans. Neural Network. 5 (6) (1994) 989e993.

[31] J.A. Hertz, Introduction to the Theory of Neural Computation, CRC Press,
2018.

[32] J.G. Kuschewski, S. Hui, S.H. Zak, Application of feedforward neural net-
works to dynamical system identification and control, IEEE Trans. Contr.
Syst. Technol. 1 (1) (1993) 37e49.

[33] K. Xiang, B.N. Li, L. Zhang, M. Pang, M. Wang, X. Li, Regularized Taylor
echo state networks for predictive control of partially observed systems,
IEEE Access 4 (2016) 3300e3309.

[34] A. De Martino, D. De Martino, An introduction to the maximum entropy
approach and its application to inference problems in biology, Heliyon 4
(4) (2018) e00596.

[35] S. Albawi, T.A. Mohammed, S. Al-Zawi, Understanding of a convolutional
neural network, in: International Conference on Engineering and Technology
(ICET), IEEE, 2017, pp. 1e6.

[36] W. Liu, Z. Wang, X. Liu, N. Zeng, Y. Liu, F.E. Alsaadi, A survey of deep
neural network architectures and their applications, Neurocomputing 234
(2017) 11e26.

[37] X. Zhou, W. Gong, W. Fu, F. Du, Application of deep learning in object
detection, in: IEEE/ACIS 16th International Conference on Computer and In-
formation Science (ICIS), IEEE, 2017, pp. 631e634.

[38] M. Mahmud, M.S. Kaiser, A. Hussain, S. Vassanelli, Applications of deep
learning and reinforcement learning to biological data, IEEE Trans. Neural
Network. Learn. Syst. 29 (6) (2018) 2063e2079.

[39] Y. Bengio, Learning deep architectures for AI, Found. Trends Mach. Learn.
2 (1) (2009) 1e127.

[40] A.L. Tarca, V.J. Carey, X.W. Chen, R. Romero, S. Draghici, Machine
learning and its applications to biology, PLoS Comput. Biol. 3 (6) (2007)
e116.

[41] A.S. Fern, C. Delgado-Mata, R. Velazquez, Training a single-layer percep-
tron for an approximate edge detection on a digital image, in: Technologies
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

28 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
and Applications of Artificial Intelligence (TAAI), 2011 International Con-
ference on (pp. 189e193), IEEE, November, 2001.

[42] A. Anarghya, D.N. Harshith, N. Rao, N.S. Nayak, B.M. Gurumurthy,
V.N. Abhishek, I.G.S. Patil, Thrust and torque force analysis in the drilling
of aramid fibre-reinforced composite laminates using RSM and MLPNN-GA,
Heliyon 4 (7) (2018) e00703.

[43] G. Singh, M. Sachan, Multi-layer perceptron (MLP) neural network tech-
nique for offline handwritten Gurmukhi character recognition, in: IEEE Inter-
national Conference on Computational Intelligence and Computing Research
(ICCIC), IEEE, 2014, pp. 1e5.

[44] A. Kolchinsky, A. Lourenço, L. Li, L.M. Rocha, Evaluation of linear classi-
fiers on articles containing pharmacokinetic evidence of drug-drug interac-
tions, in: Biocomputing, 2013, pp. 409e420.

[45] R.P. Bywater, J.N. Middleton, Melody discrimination and protein fold clas-
sification, Heliyon 2 (10) (2016), e00175.

[46] Y. Zhang, Q. Deng, W. Liang, X. Zou, An efficient feature selection strategy
based on multiple support vector machine technology with gene expression
data, BioMed Res. Int. 2018 (2018).

[47] J. Cao, Z. Fang, G. Qu, H. Sun, D. Zhang, An accurate traffic classification
model based on support vector machines, Int. J. Netw. Manag. 27 (1) (2017)
e1962.

[48] J.M. Keller, M.R. Gray, J.A. Givens, A fuzzy k-nearest neighbor algorithm,
IEEE Trans. Syst. Man Cybern. (4) (1985) 580e585.

[49] T. Cardona, Early Archean origin of heterodimeric Photosystem I, Heliyon 4
(3) (2018) e00548.

[50] S. Tharaha, K. Rashika, Hybrid artificial neural network and decision tree al-
gorithm for disease recognition and prediction in human blood cells, in: In-
ternational Conference on Innovations in Information, Embedded and
Communication Systems (ICIIECS), IEEE, 2017, pp. 1e5.

[51] X. Tang, Hybrid Hidden Markov Model and artificial neural network for
automatic speech recognition, in: PACCS’09. Pacific-Asia Conference on
Circuits, Communications and Systems, IEEE, 2009, pp. 682e685.

[52] K. Koonsanit, C. Jaruskulchai, A. Eiumnoh, Parameter-free K-means clus-
tering algorithm for satellite imagery application, in: International Confer-
ence on Information Science and Applications (ICISA), IEEE, 2012,
pp. 1e6.
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

29 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
[53] N.K. Verma, S. Dwivedi, R.K. Sevakula, Expectation maximization algo-
rithm made fast for large scale data, in: IEEE Workshop on Computational
Intelligence: Theories, Applications and Future Directions (WCI), IEEE,
2015, pp. 1e7.

[54] P. Baldi, Autoencoders, unsupervised learning, and deep architectures, in:
Proceedings of ICML Workshop on Unsupervised and Transfer Learning,
2012, pp. 37e49.

[55] K.S.S. Reddy, C.S. Bindu, A review on density-based clustering algorithms
for big data analysis, in: International Conference on I-SMAC (IoT in Social,
Mobile, Analytics and Cloud)(I-SMAC), IEEE, February 2017,
pp. 123e130.

[56] D. Miljkovic, Brief review of self-organizing maps, in: MIPRO, 2017.

[57] G. Ahalya, H.M. Pandey, Data clustering approaches survey and analysis, in:
International Conference on Futuristic Trends on Computational Analysis
and Knowledge Management (ABLAZE), IEEE, February 2015,
pp. 532e537.

[58] G. Wang, L. Huang, C. Zhang, Study of artificial neural network model
based on fuzzy clustering, in: WCICA 2006. The Sixth World Congress
on Intelligent Control and Automation (Vol. 1, pp. 2713e2717), IEEE, 2006.

[59] Y. Cho, L.K. Saul, Kernel methods for deep learning, in: Advances in Neural
Information Processing Systems, 2009, pp. 342e350.

[60] G. Camps-Valls, L. Bruzzone, Kernel-based methods for hyperspectral im-
age classification, IEEE Trans. Geosci. Rem. Sens. 43 (6) (2005)
1351e1362.

[61] T.B. Ludermir, A. Yamazaki, C. Zanchettin, An optimization methodology
for neural network weights and architectures, IEEE Trans. Neural Network.
17 (6) (2006) 1452e1459.

[62] Science News, Artificial Enzymes Convert Solar Energy into Hydrogen Gas,
Uppsala University, October 4, 2018. https://www.sciencedaily.com/
releases/2018/10/181004155426.htm.

[63] A. Demiroren, H.L. Zeynelgil, N.S. Sengor, The application of ANN tech-
nique to load-frequency control for three-area power system, in: IEEE Porto
Power Tech Proceedings (Vol. 2, pp. 5-pp), IEEE, 2001.

[64] H. Ma, J.C. Chan, T.K. Saha, C. Ekanayake, Pattern recognition techniques
and their applications for automatic classification of artificial partial
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

30 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
discharge sources, IEEE Trans. Dielectr. Electr. Insul. 20 (2) (2013)
468e478.

[65] V.S.S. Vankayala, N.D. Rao, Artificial neural networks and their applications
to power systemsda bibliographical survey, Elec. Power Syst. Res. 28 (1)
(1993) 67e79.

[66] R. Gopalapillai, J. Vidhya, D. Gupta, T.S.B. Sudarshan, Classification of ro-
botic data using artificial neural network, in: Intelligent Computational Sys-
tems (RAICS), 2013 IEEE Recent Advances in (pp. 333e337), IEEE,
December 2013.

[67] W. Kaminski, J. Skrzypski, E. Jach-Szakiel, Application of artificial neural
networks (ANNs) to predict air quality classes in big cities, in: 19th Interna-
tional Conference on Systems Engineering (pp. 135e140), IEEE, 2008,
August.

[68] S.C.Wang, J.X. Dong, G. Shen, ANN-based process control in manufacturing,
in: American Control Conference, IEEE, 1993, pp. 2531e2532.

[69] T. Le, P. Pardo, W. Claster, Application of artificial neural network in social
media data analysis: a case of lodging business in Philadelphia, in: Artificial
Neural Network Modelling (pp. 369e376), Springer, Cham, 2016.

[70] M. Barni, A. Pelagotti, A. Piva, Image processing for the analysis and con-
servation of paintings: opportunities and challenges, IEEE Signal Process.
Mag. 22 (5) (2005) 141e144.

[71] S. He, X. Li, Application of a group search optimization based artificial neu-
ral network to machine condition monitoring, in: Emerging Technologies and
Factory Automation, 2008. ETFA 2008. IEEE International Conference on
(pp. 1260e1266), IEEE, September 2008.

[72] A.G. Barto, R.S. Sutton, C.W. Anderson, Neuronlike adaptive elements that
can solve difficult learning control problems, IEEE Trans. Syst. Man Cybern.
(5) (1983) 834e846.

[73] M. Bogdan, M. Schroder, W. Rosenstiel, Artificial neural net based signal
processing for interaction with peripheral nervous system, in: Neural Engi-
neering, 2003. Conference Proceedings. First International IEEE EMBS Con-
ference on (pp. 134e137), IEEE, March 2003.

[74] B. Delinchant, D. Duret, L. Estrabaut, L. Gerbaud, H. Nguyen Huu, B. Du
Peloux, F. Wurtz, An optimizer using the software component paradigm
for the optimization of engineering systems, COMPEL Int. J. Comput.
Math. Electr. Electron. Eng. 26 (2) (2007) 368e379.
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

31 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
[75] K. Janocha, W.M. Czarnecki, On Loss Functions for Deep Neural Networks
in Classification, 2017 arXiv preprint arXiv:1702.05659.

[76] S. Yu, G. Chi, Weight optimization model based on the maximum discrim-
inating power of credit evaluation result, in: Proceedings of the International
Conference on Business and Information Management (pp. 6e11), ACM,
2017.

[77] M.R. Gogate, New paradigms and future critical directions in heterogeneous
catalysis and multifunctional reactors, Chem. Eng. Commun. 204 (1) (2017)
1e27.

[78] V. Bram, Future Perspectives in Catalysis, NRSC-catalysis Dutch National
Research School Combination Catalysis Controlled by Chemical Design,
1999.

[79] H. Li, Z. Zhang, Z. Liu, Application of artificial neural networks for catal-
ysis: a review, Catalysts 7 (10) (2017) 306.

[80] A. Corma, J.M. Serra, E. Argente, V. Botti, S. Valero, Application of artifi-
cial neural networks to combinatorial catalysis: modeling and predicting
ODHE catalysts, ChemPhysChem 3 (11) (2002) 939e945.

[81] J. Behler, M. Parrinello, Generalized neural-network representation of high-
dimensional potential-energy surfaces, Phys. Rev. Lett. 98 (14) (2007)
146401.

[82] H. Li, Z. Zhang, Mining the intrinsic trends of CO2 solubility in blended so-
lutions, J. CO2 Util. 26 (2018) 496e502.

[83] S.A. Kalogirou, Artificial neural networks in renewable energy systems ap-
plications: a review, Renew. Sustain. Energy Rev. 5 (4) (2001) 373e401.

[84] H. Li, Z. Liu, Performance prediction and optimization of solar water heater
via a knowledge-based machine learning method, in: Handbook of Research
on Power and Energy System Optimization (pp. 55e74), IGI Global, 2018.

[85] W. Duch, G.H. Diercksen, Neural networks as tools to solve problems in
physics and chemistry, Comput. Phys. Commun. 82 (2-3) (1994) 91e103.

[86] M. Lynch, H. Patel, A. Abrahamse, A.R. Rajendran, L. Medsker, Neural
network applications in physics, in: Proceedings. IJCNN’01. International
Joint Conference on Neural Networks (Vol. 3, pp. 2054e2058), IEEE, 2001.

[87] G.A. Negoita, G.R. Luecke, J.P. Vary, P. Maris, A.M. Shirokov, I.J. Shin,
C. Yang, Deep Learning: a Tool for Computational Nuclear Physics, 2018
arXiv preprint arXiv:1803.03215.
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

32 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
[88] L.S. Choon, A. Samsudin, R. Budiarto, Lightweight and cost-effective
MPEG video encryption, in: Information and Communication Technologies:
from Theory to Applications, 2004. Proceedings. 2004 International Confer-
ence on (pp. 525e526), IEEE, April 2004.

[89] D. Cho, Y.W. Tai, I.S. Kweon, Deep convolutional neural network for nat-
ural image matting using initial alpha mattes, in: IEEE Transactions on Image
Processing, 2018.

[90] J. Mayer, P.V. Borges, S.J. Simske, Introduction, in: Fundamentals and Ap-
plications of Hardcopy Communication (pp. 1e5), Springer, Cham, 2018.

[91] M. Almazrooie, A. Samsudin, A.A.A. Gutub, M.S. Salleh, M.A. Omar,
S.A. Hassan, Computer and Information Sciences, 2018.

[92] K.S. Narendra, K. Parthasarathy, Identification and control of dynamical sys-
tems using neural networks, IEEE Trans. Neural Network. 1 (1) (1990)
4e27.

[93] Y. LeCun, Y. Bengio, G. Hinton, Deep learning, Nature 521 (7553)
(2015) 436.

[94] B. Shi, X. Bai, W. Liu, J. Wang, Deep Regression for Face Alignment, 2014
arXiv preprint arXiv: 1409.5230.

[95] W.J. Yang, Y.C. Chen, P.C. Chung, J.F. Yang, Multi-feature shape regres-
sion for face alignment, EURASIP J. Adv. Signal Proc. (1) (2018) 51.

[96] Y. Wu, Q. Ji, Discriminative deep face shape model for facial point detection,
Int. J. Comput. Vis. 113 (1) (2015) 37e53.

[97] S. Dominic, C. Aparna, A.S. Nath, M. Mohan, M.S. Ajeesh, A. Antony, A
review of face detection system, in: Electrical, Electronics, and Optimization
Techniques (ICEEOT), International Conference on (pp. 3536e3539), IEEE,
March 2016.

[98] R. Toufiq, M.R. Islam, Face recognition system using PCA-ANN technique
with feature fusion method, in: International Conference on Electrical Engi-
neering and Information & Communication Technology (ICEEICT), IEEE,
2014, pp. 1e5.

[99] S. Joseph, R. Sowmiya, R.A. Thomas, X. Sofia, Face detection through neu-
ral network, in: 2nd International Conference on Current Trends in Engineer-
ing and Technology (ICCTET), IEEE, 2014, pp. 163e166.

[100] A.I. Oludare, A. Jantan, A.E. Omolara, M.M. Singh, A. Mohammed,
D.V. Kemi, Terrorism prevention: a mathematical model for assessing
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

33 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
individuals with profiling, Int. J. Comput. Sci. Network Secur. 10 (12) (July
2018).

[101] C. Cao, F. Liu, H. Tan, D. Song, W. Shu, W. Li, Z. Xie, Deep learning and
its applications in biomedicine, Genom. Proteom. Bioinform. 16 (1) (2018)
17e32.

[102] H. Qi, C. Chen, H. Zhang, J.J. Long, W.K. Chung, Y. Guan, Y. Shen, MVP:
Predicting Pathogenicity of Missense Variants by Deep Learning, 2018 bio-
Rxiv, 259390.

[103] J.Y. Lo, C.E. Floyd, Application of artificial neural networks for diagnosis of
breast cancer, in: CEC 99. Proceedings of the 1999 Congress on Evolu-
tionary Computation (Vol. 3, pp. 1755e1759), IEEE, 1999.

[104] R.R. Janghel, A. Shukla, R. Tiwari, R. Kala, Breast cancer diagnosis using
artificial neural network models, in: 3rd International Conference on Informa-
tion Sciences and Interaction Sciences (ICIS), IEEE, June 2010, pp. 89e94.

[105] M.M. Mehdy, P.Y. Ng, E.F. Shair, N.I. Saleh, C. Gomes, Artificial neural
networks in image processing for early detection of breast cancer, Comput.
Math. Method. Med. (2017).

[106] W. Yue, Z. Wang, H. Chen, A. Payne, X. Liu, Machine learning with appli-
cations in breast cancer diagnosis and prognosis, Designs 2 (2) (2018) 13.

[107] A.I. Oludare, A. Jantan, A.E. Omolara, M.M. Singh, M. Anbar, Z.F. Zaaba,
Forensic DNA profiling for identifying an individual crime, Int. J. Civil Eng.
Technol. (IJCIET) (July, 2018) 755e765.

[108] A.E. Omolara, A. Jantan, O.I. Abiodun, M.M. Singh, M. Anbar, D.V. Kemi,
State-of-the-art in big data application techniques to financial crime: a survey,
Int. J. Comput. Sci. Network Secur. 18 (7) (2018) 6e16.

[109] Y. Xin, L. Kong, Z. Liu, Y. Chen, Y. Li, H. Zhu, C. Wang, Machine learning
and deep learning methods for cybersecurity, IEEE Access 6 (2018)
35365e35381.

[110] Y. Dai, G. Wang, Analyzing tongue images using a conceptual alignment
deep autoencoder, IEEE Access 6 (2018) 5962e5972.

[111] W.G. Hatcher, W. Yu, A survey of deep learning: platforms, applications and
emerging research trends, IEEE Access 6 (2018) 24411e24432.

[112] M. Mohammadi, A. Al-Fuqaha, S. Sorour, M. Guizani, Deep learning for IoT
big data and streaming analytics: a survey, IEEE Commun. Surv. Tutorials
99 (2018) 1e39.
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

34 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
[113] I. Qureshi, Glaucoma detection in retinal images using image processing
techniques: a survey, Int. J. Adv. Netw. Appl. 7 (2) (2015) 2705.

[114] J.Y. Choi, T.K. Yoo, J.G. Seo, J. Kwak, T.T. Um, T.H. Rim, Multi-categor-
ical deep learning neural network to classify retinal images: a pilot study em-
ploying small database, PLoS One 12 (11) (2017) e0187336.

[115] G. Santos-García, E.H. Galilea, Using artificial neural networks to identify
glaucoma stages, in: The Mystery of Glaucoma, InTech, 2011.

[116] H.A. Pierson, M.S. Gashler, Deep learning in robotics: a review of recent
research, Adv. Robot. 31 (16) (2017) 821e835.

[117] I.E. Olatunji, Human Activity Recognition for Mobile Robot, 2018 arXiv
preprint arXiv:1801.07633.

[118] J. Ruiz-del-Solar, P. Loncomilla, N. Soto, A Survey on Deep Learning
Methods for Robot Vision, 2018 arXiv preprint arXiv:1803.10862.

[119] W. He, Z. Yan, Y. Sun, Y. Ou, C. Sun, Neural-learning-based control for a
constrained robotic manipulator with flexible joints, IEEE Trans. Neural
Network. Learn. Syst. (2018).

[120] X. Yang, H. He, Self-learning robust optimal control for continuous-time
nonlinear systems with mismatched disturbances, Neural Network. 99
(2018) 19e30.

[121] B.H. Chen, S.C. Huang, C.Y. Li, S.Y. Kuo, Haze removal using radial basis
function networks for visibility restoration applications, IEEE Trans. Neural
Network. Learn. Syst. (2017).

[122] J. Li, X. Mei, D. Prokhorov, D. Tao, Deep neural network for structural pre-
diction and lane detection in traffic scene, IEEE Trans. Neural Network.
Learn. Syst. 28 (3) (2017) 690e703.

[123] M. Mamuda, S. Sathasivam, Predicting the survival of diabetes using neural
network, AIP Conf. Proc. 1870 (1) (2017) 040046.

[124] B.V. Liebergen, Machine learning: a revolution in risk management and
compliance, Inst. Int. Financ. J. Financ. Transform. 45 (Apr 15, 2017)
60e67.

[125] A. Pandey, A. Mishra, Application of artificial neural networks in yield pre-
diction of potato crop, Russ. Agric. Sci. 43 (3) (2017) 266e272.

[126] X. Zhang, Y. Zhuang, H. Hu, W. Wang, 3-D Laser-based multiclass and
multiview object detection in cluttered indoor scenes, IEEE Trans. Neural
Network. Learn. Syst. 28 (1) (2017) 177e190.
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

35 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
[127] A.P. Turner, L.S. Caves, S. Stepney, A.M. Tyrrell, M.A. Lones, Artificial
epigenetic networks: automatic decomposition of dynamical control tasks us-
ing topological self-modification, IEEE Trans. Neural Network. Learn. Syst.
28 (1) (2017) 218e230.

[128] J. Nasir, Y.H. Yoo, D.H. Kim, J.H. Kim, User preference-based dual-mem-
ory neural model with memory consolidation approach, IEEE Trans. Neural
Network. Learn. Syst. (2017) 2294e2308.

[129] Y. Deng, F. Bao, Y. Kong, Z. Ren, Q. Dai, Deep direct reinforcement
learning for financial signal representation and trading, IEEE Trans. Neural
Network. Learn. Syst. 28 (3) (2017) 653e664.

[130] K. Radziszewski, Artificial neural networks as an architectural design tool-
generating new detail forms based on the Roman Corinthian order capital,
in: IOP Conference Series: Materials Science and Engineering (Vol. 245,
No. 6, p. 062030), IOP Publishing, 2017.

[131] A. Ansari, A. Riasi, Modelling and evaluating customer loyalty using neural
networks: Evidence from startup insurance companies, Future Bus. J. 2 (1)
(2016) 15e30.

[132] A. Lotko, P.A. Korneta, M.A. Lotko, R. Longwic, Using Neural Networks in
Modeling Customer Loyalty in Passenger Cars Maintenance and Repair Ser-
vices, Appl. Sci. 8 (5) (2018) 2076e3417.

[133] M. Qiu, Y. Song, F. Akagi, Application of artificial neural network for the
prediction of stock market returns. The case of the Japanese stock market,
Chaos Solit. Fractals 85 (2016) 1e7.

[134] M. G€oçken, M. O€zçalıcı, A. Boru, A.T. Dosdogru, Integrating metaheuristics
and artificial neural networks for improved stock price prediction, Expert
Syst. Appl. 44 (2016) 320e331.

[135] K.Y. Lee, N. Chung, S. Hwang, Application of an artificial neural network
(ANN) model for predicting mosquito abundances in urban areas, Ecol.
Inf. 36 (2016) 172e180.

[136] q. Pater, Application of Artificial Neural Networks and Genetic Algorithms
for Crude Fractional Distillation Process Modeling, Faculty of Mathematics
and Computer Science, Nicolaus Copernicus University Torun, Poland,
2016.

[137] G. Lai, Z. Liu, Y. Zhang, C.P. Chen, Adaptive position/attitude tracking con-
trol of aerial robot with unknown inertial matrix based on a new robust neural
identifier, IEEE Trans. Neural Network. Learn. Syst. 27 (1) (2016) 18e31.
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

36 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
[138] P. Onotu, D. Day, M.A. Rodrigues, Accurate shellcode recognition from
network traffic data using artificial neural nets, in: Electrical and Computer
Engineering (CCECE), Sheffield Hallam University Sheffield, UK, 2015
IEEE, 3 e 6, May 2015, pp. 355e360.

[139] R. Gilmore, N. Hanley, M. O’Neill, Neural network-based attack on a
masked implementation of AES, in: Hardware-oriented Security and Trust,
2015 IEEE, May 2015, pp. 106e111.

[140] I. Taro, E. Donald, Y. Liu, O. Tetsuya, B. Leonard, U. Kazunori, Application
of neural networks for intrusion detection in tor networks, in: Advanced In-
formation Networking and Applications Workshops (WAINA) 2015 IEEE,
24e27 March 2015, pp. 67e72.

[141] D.P. Gaikwad, R.C. Thool, Intrusion detection system using bagging
ensemble method of machine learning, in: Computing Communication Con-
trol and Automation (ICCUBEA), 2015 International Conference on,
February. 2015, pp. 291e295.

[142] I. Kotenko, I. Saenko, F. Skorik, S. Bushuev, Neural network approach to
forecast the state of the internet of things elements, in: Soft Computing
and Measurements, XVIII International Conference, May 2015,
pp. 133e135.

[143] A. Hajdarevic, I. Dzananovic, L. Banjanovic-Mehmedovic, F. Mehmedovic,
Anomaly detection in thermal power plant using probabilistic neural
network, in: Information and Communication Technology, Electronics and
Microelectronics (MIPRO), 2015 38th International Convention, May
2015, pp. 1118e1123.

[144] A. Zhukov, N. Tomin, D. Sidorov, D. Panasetsky, V. Spirayev, A hybrid arti-
ficial neural network for voltage security evaluation in a power system, in:
Energy (IYCE), 2015 5th International Youth Conference, May 2015,
pp. 1e8.

[145] T.V. Santosh, G. Vinod, R.K. Saraf, A.K. Ghosh, H.S. Kushwaha, Applica-
tion of artificial neural networks to nuclear power plant transient diagnosis,
Reliab. Eng. Syst. Saf. 92 (10) (2007) 1468e1472.

[146] S. Huang, F. Yu, R. Tsaih, Y. Huang, Network-traffic anomaly detection with
incremental majority learning, in: Neural Networks 2015 International Joint
Conference, July 2015, pp. 1e8.

[147] M. Turcanik, Packet filtering by artificial neural network, in: Military Tech-
nologies, 2015 International Conference, May 2015, pp. 1e4.
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

37 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
[148] H. Fatima, S.M. Al-Turki, S.K. Pradhan, G.,N. Dash, Information security:
artificial immune detectors in neural networks, in: Web Applications and
Networking (WSWAN), 2015 2nd World Symposium on 1e6, March 2015.

[149] F. Kitchens, T. Harris, Genetic adaptive neural networks for prediction of in-
surance claims, Int. J. Eng. Adv. Res. Technol. (IJEART) 1 (6) (December,
2015) 2454e9290.

[150] N. Zeinalizadeh, A.A. Shojaie, M. Shariatmadari, Modeling and analysis of
bank customer satisfaction using neural networks approach, Int. J. Bank Mar-
ket. 33 (6) (2015) 717e732.

[151] S. Abbinaya, M.S. Kumar, Software effort and risk assessment using decision
table trained by neural networks, in: Communications and Signal Processing
(ICCSP), 2015 International Conference, pp. 1389e1394, April 2015.

[152] S. Gupta, S. Kashyap, Forecasting inflation in G-7 countries: an application
of artificial neural network, Foresight 17 (1) (2015) 63e73.

[153] X. Zhong, H. He, H. Zhang, Z. Wang, A neural network based online
learning and control approach for Markov jump systems, Neurocomputing
149 (2015) 116e123.

[154] S.S. Dahikar, S.V. Rode, Agricultural crop yield prediction using artificial
neural network approach, Int. J. Innovat. Res. Electr. Electron. Instrum.
Contr. Eng. 2 (1) (2014) 683e686.

[155] J. Zhu, S. Liu, SOM network-based clustering analysis of real estate enter-
prises, Am. J. Ind. Bus. Manag. 4 (3) (March 21, 2014) 167.

[156] H. Igor, J. Bohuslava, J. Martin, N. Martin, Application of neural networks in
computer security, Proc. Eng. 69 (2014) 1209e1215.

[157] F. Ecer, Comparing the bank failure prediction performance of neural net-
works and support vector machines: the Turkish case, Ekonomska Istra-
zivanja 26 (3) (2013) 81e98.

[158] I.S.H. Bahia, Using artificial neural network modeling in forecasting revenue:
case study in national insurance company/Iraq, Int. J. Intell. Sci. 3 (2013)
136e143.

[159] S.R. Khaze, M. Masdari, S. Hojjatkhah, Application of Artificial Neural Net-
works in Estimating Participation in Elections, 2013 arXiv preprint arXiv:
1309.2183.
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

38 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
[160] E.I.A. Kareem, W.A.A. Alsalihy, A. Jantan, Multi-connect architecture
(MCA) associative memory: a modified hopfield neural network, Intell. Au-
tom. Soft Comput. 18 (3) (2012) 279e296.

[161] M.S. Nasr, M.A.E. Moustafa, H.A.E. Seif, G. El Kobrosy, Application of
artificial neural network (ANN) for the prediction of EL-AGAMY waste-
water treatment plant performance-Egypt, Alexandria Eng. J. 51 (2012)
37e43.

[162] A. Adebiyi, J. Arreymbi, C. Imafidon, Assessment of software design using
neural network. School of Architecture, Computing and Engineering Univer-
sity of East London, London, UK, Int. J. Adv. Res. Artif. Intell. (IJARAI) 1
(4) (2012).

[163] F. Cheng, V. Sutariya, F. Cheng, V. Sutariya, Artificial neural networks: a
new paradigm for thermal science and engineering. College of Pharmacy,
University of South Florida, USA, Clin. Exp. Pharmacol. 2 (3) (2012) 1e2.

[164] M.A. Korany, H. Mahgoub, O.T. Fahmy, H.M. Maher, Application of artifi-
cial neural networks for response surface modelling in HPLC method devel-
opment, J. Adv. Res. 3 (1) (2012) 53e63.

[165] F. Cheng, V. Sutariya, Applications of artificial neural network modeling in
drug discovery. College of Pharmacy, University of South Florida, USA,
Clin. Exp. Pharmacol. 2 (3) (2012) 1e2. Corea F (2018) Applied artificial
intelligence: where AI can be used in business.

[166] B. Stahl, M. Carroll-Mayer, D. Elizondo, K. Wakunuma, Y. Zheng, Intelli-
gence Techniques in Computer Security and Forensics: at the Boundaries
of Ethics and Law, Computational Intelligence for Privacy and Security,
2012, pp. 237e258.

[167] W. Yan, Toward automatic time-series forecasting using neural networks,
IEEE Trans. Neural Network. Learn. Syst. 23 (7) (2012) 1028e1039.

[168] Y. Cao, H. He, H.H. Huang, LIFT: a new framework of learning from testing
data for face recognition, Neurocomputing 74 (6) (2011) 916e929.

[169] J.L. Junior, A.J.D. Neto, L.B. Neto, F.J.C.P. Soeiro, C.C. Santana,
H.F.C. Velho, Application of artificial neural networks and hybrid methods
in the solution of inverse problems. Artificial Neural Networks - Application,
In Tech. April 11 (2011).

[170] A. Quetglas, F. Ordines, B. Guijarro, The use of artificial neural networks
(ANNs) in aquatic ecology, in: Artificial Neural Networks - Application, In-
Tech, 2011.
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

39 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
[171] J. Stastny, V. Konecny, O. Trenz, Agricultural data prediction by means of
neural network, Agric. Econ. 7 (2011) 356e361. Stergiou C, Siganos D
(1996) Neural Networks 1996.

[172] A.K. Mishra, L. Ramesh, Application of neural networks in wind power
(generation) prediction, in: Sustainable Power Generation and Supply,
SUPERGEN’09, April 2009, pp. 1e5.

[173] R. Webb, P. Doble, M. Dawson, Optimisation of HPLC gradient separations
using artificial neural networks (ANNs): application to benzodiazepines in
post-mortem samples, J. Chromatog. 877 (2009) 615e620.

[174] D. Shanthi, G. Sahoo, N. Saravanan, Designing an artificial neural network
model for the prediction of thrombo-embolic stroke, J. Biometric Bioinf.
(IJBB) 3 (1) (2009) 3e10.

[175] J.L. Patel, R.K. Goyal, Applications of artificial neural networks in medical
science, Curr. Clin. Pharmacol. 2 (3) (September 2007) 217e226.

[176] Z. Liu, X. Guan, H. Wu, Bandwidth prediction and congestion control for
ABR traffic based on neural networks, Adv. Neural Network. (2006)
202e207.

[177] J. Wen, Q. Dai, Y. Jin, A neural network decision-making mechanism for
robust video transmission over 3G wireless network,” Department of Auto-
mation, Tsinghua University, Beijing 100084, China, Adv. Neural Network.
(2006) 165e170.

[178] A . Grediaga, F. Ibarra, F. García, B. Ledesma, F. Brotons, Application of
neural networks in network control and information security, Adv. Neural
Network. (2006) 208e213.

[179] S. Zhu, Y. Zhang, X. Lu, Detection for triangle traffic sign based on neural
network, in: International Symposium on Neural Networks, Springer, Berlin,
Heidelberg, 2006, pp. 40e45.

[180] P.N. Dong-Chul, L. Yunsik, Multiscale bilinear recurrent neural networks
and their application to the long-term prediction of network traffic, in: Inter-
national Symposium on Neural Networks, Springer, Berlin, Heidelberg,
May, 2006, pp. 196e201.

[181] J.P. Rigol-Sanchez, M. Chica-Olmo, F. Abarca-Hernandez, Artificial neural
networks as a tool for mineral potential mapping with GIS, Int. J. Rem.
Sens. 24 (5) (2003) 1151e1156.
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

40 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
[182] S. Agatonovic-Kustrin, R. Beresford, Basic concepts of artificial neural
network (ANN) modeling and its application in pharmaceutical research, J.
Pharmaceut. Biomed. (2000).

[183] A.S. Kate, J.N.D. Gupta, Neural networks in business: techniques and appli-
cations for the operations researcher, Comput. Oper. Res. 27 (11e12) (2000)
1023e1044.

[184] H. Pasika, S. Haykin, E. Clothiaux, R. Stewart, Neural networks for sensor
fusion in remote sensing, in: Neural Networks, International Joint Conference
on 4, IEEE, 1999, pp. 2772e2776.

[185] K.M. Fanning, K.O. Cogger, Neural network detection of management fraud
using published financial data, Int. J. Intell. Syst. Account. Finance Manag. 7
(1) (1998) 21e41.

[186] J. Cannady, Artificial neural networks for misuse detection, in: National In-
formation Systems Security Conference, 26, October 1998.

[187] C.N. Tan, An Artificial Neural Networks Primer with Financial Applications
Examples in Financial Distress Predictions and Foreign Exchange Hybrid
Trading System, Bond University, 1997, pp. 50e78.

[188] T.E. Senator, H.G. Goldberg, J. Wooton, M.A. Cottini, A.U. Khan,
C.D. Klinger, R.W. Wong, Financial crimes enforcement network AI system
(FAIS) identifying potential money laundering from reports of large cash
transactions, AI Mag. 16 (4) (1995) 21.

[189] R.D. Dony, S. Haykin, Neural network approaches to image compression,
Proc. IEEE 83 (2) (1995) 288e303.

[190] C.T. Lin, C.S.G. Lee, Neural-network-based fuzzy logic control and decision
system, IEEE Trans. Comput. 40 (12) (1991) 1320e1336.

[191] H. Jiang, H. Zhang, Iterative ADP learning algorithms for discrete-time
multi-player games, Artif. Intell. Rev. (2018) 1e17.

[192] D. Wang, D. Liu, D. Zhao, Y. Huang, D. Zhang, A neural-network-based
iterative GDHP approach for solving a class of nonlinear optimal control
problems with control constraints, Neural Comput. Appl. 22 (2) (2013)
219e227.

[193] G. Shi, Q. Wei, D. Liu, Optimization of electricity consumption in office
buildings based on adaptive dynamic programming, Soft Comput. 21 (21)
(2017) 6369e6379.
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).



Article Nowe00938

41 https://doi.org/10.1016/j.heliy
2405-8440/ 2018 The Auth
(http://creativecommons.org/li
[194] G.J. Besseris, Taguchi-generalized regression neural network micro-
screening for physical and sensory characteristics of bread, Heliyon 4 (3)
(2018) e00551.

[195] M. Nishio, C. Nagashima, S. Hirabayashi, A. Ohnishi, K. Sasaki, T. Sagawa,
T. Yamashita, Convolutional auto-encoder for image denoising of ultra-low-
dose CT, Heliyon 3 (8) (2017) e00393.

[196] A.I. Oludare, A. Jantan, E.O. Abiodun, M.M. Singh, Z.L. Abubakar,
A.M. Umar, Big data: an approach for detecting terrorist activities with peo-
ple’s profiling, in: Proceedings of the International MultiConference of Engi-
neers and Computer Scientists, Hong Kong, Vol I IMECS 2018, 14e16,
March 2018.

[197] F.N. Mahmadi, Z.F. Zaaba, A. Samsudin, Security issues in online banking:
review cases in Malaysia, Adv. Sci. Lett. 23 (5) (2017) 4327e4330.

[198] E.O. Abiodun, A. Jantan, A.I. Oludare, H.E. Poston, A novel approach for
the adaptation of honey encryption to support natural language message,
in: Proceedings of the International Multi-conference of Engineers and Com-
puter Scientists, Vol I IMECS 2018, 14e16, March 2018. Hong Kong.

[199] A.E. Omolara, A. Jantan, A.I. Oludare, H. Arshad, An enhanced practical dif-
ficulty of one-time pad algorithm resolving the key management and distri-
bution problem, in: Proceedings of the International Multi-conference of
Engineers and Computer Scientists, 2018.

[200] G. Felix, G. Napoles, R. Falcon, W. Froelich, K. Vanhoof, R. Bello, A re-
view on methods and software for fuzzy cognitive maps, Artif. Intell. Rev.
(2017) 1e31.

[201] S. Dhanalakshmi, C. Subramanian, An analysis of data mining applications
for fraud detection in securities market, J. Data Mining Techn. Appl. 3 (1)
(2014) 326e335.

[202] J. Ahire, Artificial Neural Networks: the Brain behind AI. Lulu. com.

[203] D.A. Medler, A brief history of connectionism, Neural Comput. Surv. 1
(1998) 18e72.

[204] S.I. Gallant, Connectionist expert systems, Commun. ACM 31 (2) (1998)
152e169.
on.2018.e00938
ors. Published by Elsevier Ltd. This is an open access article under the CC BY license
censes/by/4.0/).