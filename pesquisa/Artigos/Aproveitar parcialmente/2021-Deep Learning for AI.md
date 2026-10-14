---
source_file: "2021-Deep Learning for AI.txt"
original_rel_path: "Trabalhos\Artigos\Aproveitar parcialmente\txt\2021-Deep Learning for AI.txt"
category: "Artigos_Aproveitar_parcialmente"
extension: ".txt"
sha256: "b5c5abe909e714f64b2900785f02d9f098b3ac91f8d9e7415f9d3eb84e653e3b"
extracted_at: "2026-09-20T00:50:21.597909"
---

﻿turing lecture
DOI:10.1145/3448250

objects or understanding language? 
How can neural networks learn the rich Deep learning seeks to answer this 

internal representations required  question by using many layers of activ-
ity vectors as representations and 

for difficult tasks such as recognizing  learning the connection strengths that 

objects or understanding language? give rise to these vectors by following 
the stochastic gradient of an objective 
function that measures how well the 

BY YOSHUA BENGIO, YANN LECUN, AND GEOFFREY HINTON network is performing. It is very sur-
prising that such a conceptually simple 
approach has proved to be so effective 

Deep when applied to large training sets us-
ing huge amounts of computation and 
it appears that a key ingredient is 
depth: shallow networks simply do not 
work as well.

We reviewed the basic concepts 
and some of the breakthrough 

Learning achievements of deep learning several 
years ago.63 Here we briefly describe 
the origins of deep learning, describe 
a few of the more recent advances, and 
discuss some of the future challenges. 
These challenges include learning with 

for AI little or no external supervision, coping 
with test examples that come from a 
different distribution than the training 
examples, and using the deep learning 
approach for tasks that humans solve 
by using a deliberate sequence of steps 
which we attend to consciously—tasks 
that Kahneman56 calls system 2 tasks as 

TURING LECTURE opposed to system 1 tasks like object 
Yoshua Bengio, Yann LeCun, and Geoffrey Hinton are recipients  recognition or immediate natural lan-
of the 2018 ACM A.M. Turing Award for breakthroughs that have  guage understanding, which generally 
made deep neural networks a critical component of computing. feel effortless.

From Hand-Coded Symbolic 
Expressions to Learned Distributed 
Representations
There are two quite different para-
digms for AI. Put simply, the logic-in-

R E SEARCH ON ARTIFICIAL neural networks was spired paradigm views sequential rea-
motivated by the observation that human intelligence soning as the essence of intelligence 

emerges from highly parallel networks of relatively and aims to implement reasoning in 
computers using hand-designed rules 

simple, non-linear neurons that learn by adjusting of inference that operate on hand-de-

the strengths of their connections. This observation signed symbolic expressions that for-
malize knowledge. The brain-inspired 

leads to a central computational question: How is it paradigm views learning representa-
possible for networks of this general kind to learn tions from data as the essence of in-

the complicated internal representations that are telligence and aims to implement 
learning by hand-designing or evolv-

required for difficult tasks such as recognizing ing rules for modifying the connec-

58    COMMUNICATIONS OF THE ACM   |   JULY 2021  |   VOL.  64  |   NO.  7



tion strengths in simulated networks model the structure inherent in a set tors of neural activity to represent 
of artificial neurons. of symbol strings by learning appro- concepts and weight matrices to cap-

In the logic-inspired paradigm, a priate activity vectors for each symbol ture relationships between concepts 
symbol has no meaningful internal and learning non-linear transforma- is that this leads to automatic gener-
structure: Its meaning resides in its tions that allow the activity vectors alization. If Tuesday and Thursday 
relationships to other symbols which that correspond to missing elements are represented by very similar vec-
can be represented by a set of sym- of a symbol string to be filled in. This tors, they will have very similar causal 
bolic expressions or by a relational was first demonstrated in Rumelhart effects on other vectors of neural ac-
graph. By contrast, in the brain-in- et al.74 on toy data and then by Bengio tivity. This facilitates analogical rea-
spired paradigm the external sym- et al.14 on real sentences. A very im- soning and suggests that immediate, 
bols that are used for communica- pressive recent demonstration is intuitive analogical reasoning is our 
tion are converted into internal BERT,22 which also exploits self-at- primary mode of reasoning, with logi-
vectors of neural activity and these tention to dynamically connect cal sequential reasoning being a 
vectors have a rich similarity struc- groups of units, as described later. much later development,56 which we 
ture. Activity vectors can be used to The main advantage of using vec- will discuss.

JULY 2021  |   VOL.  64  |   NO.  7   |   COMMUNICATIONS OF THE ACM     59

IMAGE BY YURCHANKA SIARHEI



turing lecture

The Rise of Deep Learning the task, it makes sense to start by using deep networks involved unsupervised 
Deep learning re-energized neural net- some other source of information to cre- pre-training of layers of units that used 
work research in the early 2000s by in- ate layers of feature detectors and then the logistic sigmoid nonlinearity or the 
troducing a few elements which made to fine-tune these feature detectors us- closely related hyperbolic tangent. Rec-
it easy to train deeper networks. The ing the limited supply of labels. In trans- tified linear units had long been hy-
emergence of GPUs and the availability fer learning, the source of information is pothesized in neuroscience29 and al-
of large datasets were key enablers of another supervised learning task that ready used in some variants of RBMs70 
deep learning and they were greatly en- has plentiful labels. But it is also possi- and convolutional neural networks.54 It 
hanced by the development of open ble to create layers of feature detectors was an unexpected and pleasant sur-
source, flexible software platforms without using any labels at all by stack- prise to discover35 that rectifying non-
with automatic differentiation such as ing auto-encoders.15,50,59 linearities (now called ReLUs, with 
Theano,16 Torch,25 Caffe,55 Tensor- First, we learn a layer of feature de- many modern variants) made it easy to 
Flow,1 and PyTorch.71 This made it easy tectors whose activities allow us to re- train deep networks by backprop and 
to train complicated deep nets and to construct the input. Then we learn a stochastic gradient descent, without 
reuse the latest models and their build- second layer of feature detectors whose the need for layerwise pre-training. 
ing blocks. But the composition of activities allow us to reconstruct the ac- This was one of the technical advances 
more layers is what allowed more com- tivities of the first layer of feature detec- that enabled deep learning to outper-
plex non-linearities and achieved sur- tors. After learning several hidden lay- form previous methods for object rec-
prisingly good results in perception ers in this way, we then try to predict ognition,60 as outlined here.
tasks, as summarized here. the label from the activities in the last Breakthroughs in speech and object 

Why depth? Although the intuition hidden layer and we backpropagate the recognition. An acoustic model con-
that deeper neural networks could be errors through all of the layers in order verts a representation of the sound wave 
more powerful pre-dated modern deep to fine-tune the feature detectors that into a probability distribution over frag-
learning techniques,82 it was a series of were initially discovered without using ments of phonemes. Heroic efforts by 
advances in both architecture and the precious information in the labels. Robinson72 using transputers and by 
training procedures,15,35,48 which ush- The pre-training may well extract all Morgan et al.69 using DSP chips had al-
ered in the remarkable advances which sorts of structure that is irrelevant to ready shown that, with sufficient pro-
are associated with the rise of deep the final classification but, in the re- cessing power, neural networks were 
learning. But why might deeper net- gime where computation is cheap and competitive with the state of the art for 
works generalize better for the kinds of labeled data is expensive, this is fine so acoustic modeling. In 2009, two gradu-
input-output relationships we are in- long as the pre-training transforms the ate students68 using Nvidia GPUs 
terested in modeling? It is important input into a representation that makes showed that pre-trained deep neural 
to realize that it is not simply a ques- classification easier. nets could slightly outperform the SOTA 
tion of having more parameters, since In addition to improving generaliza- on the TIMIT dataset. This result reig-
deep networks often generalize better tion, unsupervised pre-training initial- nited the interest of several leading 
than shallow networks with the same izes the weights in such a way that it is speech groups in neural networks. In 
number of parameters.15 The practice easy to fine-tune a deep neural network 2010, essentially the same deep network 
confirms this. The most popular class with backpropagation. The effect of was shown to beat the SOTA for large vo-
of convolutional net architecture for pre-training on optimization was his- cabulary speech recognition without re-
computer vision is the ResNet family43 torically important for overcoming the quiring speaker-dependent training28,46 
of which the most common represen- accepted wisdom that deep nets were and by 2012, Google had engineered a 
tative, ResNet-50 has 50 layers. Other hard to train, but it is much less rele- production version that significantly 
ingredients not mentioned in this arti- vant now that people use rectified lin- improved voice search on Android. This 
cle but which turned out to be very use- ear units (see next section) and residu- was an early demonstration of the dis-
ful include image deformations, drop- al connections.43 However, the effect of ruptive power of deep learning.
out,51 and batch normalization.53 pre-training on generalization has At about the same time, deep learn-

We believe that deep networks excel proved to be very important. It makes it ing scored a dramatic victory in the 
because they exploit a particular form possible to train very large models by 2012 ImageNet competition, almost 
of compositionality in which features leveraging large quantities of unla- halving the error rate for recognizing a 
in one layer are combined in many dif- beled data, for example, in natural lan- thousand different classes of object in 
ferent ways to create more abstract fea- guage processing, for which huge cor- natural images.60 The keys to this vic-
tures in the next layer. pora are available.26,32 The general tory were the major effort by Fei-Fei Li 

For tasks like perception, this kind principle of pre-training and fine-tun- and her collaborators in collecting 
of compositionality works very well and ing has turned out to be an important more than a million labeled images31 

there is strong evidence that it is used tool in the deep learning toolbox, for for the training set and the very effi-
by biological perceptual systems.83 example, when it comes to transfer cient use of multiple GPUs by Alex 

Unsupervised pre-training. When the learning or even as an ingredient of Krizhevsky. Current hardware, includ-
number of labeled training examples is modern meta-learning.33 ing GPUs, encourages the use of large 
small compared with the complexity of The mysterious success of rectified mini-batches in order to amortize the 
the neural network required to perform linear units. The early successes of cost of fetching a weight from memory 

60    COMMUNICATIONS OF THE ACM   |   JULY 2021  |   VOL.  64  |   NO.  7



turing lecture

across many uses of that weight. Pure tecture in many applications, stacks 
online stochastic gradient descent many layers of ”self-attention” modules. 
which uses each weight once converges Each module in a layer uses a scalar 
faster and future hardware may just product to compute the match be-
use weights in place rather than fetch-
ing them from memory. We believe that tween its query vector and the key vec-

tors of other modules in that layer. The 
The deep convolutional neural net deep networks matches are normalized to sum to 1, 

contained a few novelties such as the 
use of ReLUs to make learning faster excel because and the resulting scalar coefficients are 

then used to form a convex combina-
and the use of dropout to prevent over- they exploit a tion of the value vectors produced by 
fitting, but it was basically just a feed- the other modules in the previous layer. 
forward convolutional neural net of the particular form of The resulting vector forms an input for 
kind that Yann LeCun and his collabo- compositionality a module of the next stage of computa-
rators had been developing for many tion. Modules can be made multi-
years.64,65 The response of the computer in which features headed so that each module computes 
vision community to this breakthrough 
was admirable. Given this incontro- in one layer are several different query, key and value 

vectors, thus making it possible for 
vertible evidence of the superiority of combined in many each module to have several distinct in-
convolutional neural nets, the commu-
nity rapidly abandoned previous hand- different ways puts, each selected from the previous 

stage modules in a different way. The 
engineered approaches and switched to create more order and number of modules does not 
to deep learning. abstract features  matter in this operation, making it pos-

sible to operate on sets of vectors rather 
Recent Advances in the next layer. than single vectors as in traditional 
Here we selectively touch on some of neural networks. For instance, a lan-
the more recent advances in deep guage translation system, when pro-
learning, clearly leaving out many im- ducing a word in the output sentence, 
portant subjects, such as deep rein- can choose to pay attention to the cor-
forcement learning, graph neural net- responding group of words in the input 
works and meta-learning. sentence, independently of their posi-

Soft attention and the transformer tion in the text. While multiplicative 
architecture. A significant development gating is an old idea for such things as 
in deep learning, especially when it coordinate transforms44 and powerful 
comes to sequential processing, is the forms of recurrent networks,52 its re-
use of multiplicative interactions, par- cent forms have made it mainstream. 
ticularly in the form of soft atten- Another way to think about attention 
tion.7,32,39,78 This is a transformative ad- mechanisms is that they make it possi-
dition to the neural net toolbox, in that ble to dynamically route information 
it changes neural nets from purely vec- through appropriately selected mod-
tor transformation machines into ar- ules and combine these modules in po-
chitectures which can dynamically tentially novel ways for improved out-
choose which inputs they operate on, of-distribution generalization.38

and can store information in differen- Transformers have produced dra-
tiable associative memories. A key matic performance improvements that 
property of such architectures is that have revolutionized natural language 
they can effectively operate on different processing,27,32 and they are now being 
kinds of data structures including sets used routinely in industry. These sys-
and graphs. tems are all pre-trained in a self-super-

Soft attention can be used by mod- vised manner to predict missing words 
ules in a layer to dynamically select in a segment of text.
which vectors from the previous layer Perhaps more surprisingly, trans-
they will combine to compute their formers have been used successfully to 
outputs. This can serve to make the solve integral and differential equa-
output independent of the order in tions symbolically.62 A very promising 
which the inputs are presented (treat- recent trend uses transformers on top 
ing them as a set) or to use relation- of convolutional nets for object detec-
ships between different inputs (treat- tion and localization in images with 
ing them as a graph). state-of-the-art performance.19 The 

The transformer architecture,85 transformer performs post-processing 
which has become the dominant archi- and object-based reasoning in a differ-

JULY 2021  |   VOL.  64  |   NO.  7   |   COMMUNICATIONS OF THE ACM     61



turing lecture

entiable manner, enabling the system ment is large and complex and repre-
to be trained end-to-end. senting the distribution of plausible 

Unsupervised and self-supervised continuations properly is essentially 
learning. Supervised learning, while an unsolved problem.
successful in a wide variety of tasks, Contrastive learning. One way to ap-
typically requires a large amount of A key question  proach this problem is through latent 
human-labeled data. Similarly, when for the future  variable models that assign an energy 
reinforcement learning is based only (that is, a badness) to examples of a 
on rewards, it requires a very large of AI is how do video and a possible continuation.a

number of interactions. These learn- humans learn Given an input video X and a pro-
ing methods tend to produce task-spe- posed continuation Y , we want a mod-
cific, specialized systems that are often so much from el to indicate whether Y is compatible 
brittle outside of the narrow domain observation  with X by using an energy function 
they have been trained on. Reducing E(X, Y) which takes low values when 
the number of human-labeled samples alone? X and Y are compatible, and higher 
or interactions with the world that are values otherwise.
required to learn a task and increasing E(X, Y) can be computed by a deep 
the out-of-domain robustness is of cru- neural net which, for a given X, is 
cial importance for applications such trained in a contrastive way to give a 
as low-resource language translation, low energy to values Y that are compat-
medical image analysis, autonomous ible with X (such as examples of (X, Y) 
driving, and content filtering. pairs from a training set), and high en-

Humans and animals seem to be ergy to other values of Y that are incom-
able to learn massive amounts of back- patible with X. For a given X, inference 
ground knowledge about the world, consists in finding one Y̌ that minimizes 
largely by observation, in a task-inde- E(X, Y) or perhaps sampling from the Y s 
pendent manner. This knowledge un- that have low values of E(X, Y). This en-
derpins common sense and allows hu- ergy-based approach to representing 
mans to learn complex tasks, such as the way Y depends on X makes it possi-
driving, with just a few hours of prac- ble to model a diverse, multi-modal set 
tice. A key question for the future of AI of plausible continuations.
is how do humans learn so much from The key difficulty with contrastive 
observation alone? learning is to pick good “negative” 

In supervised learning, a label for samples: suitable points Y whose ener-
one of N categories conveys, on aver- gy will be pushed up. When the set of 
age, at most log2(N) bits of information possible negative examples is not too 
about the world. In model-free rein- large, we can just consider them all. 
forcement learning, a reward similarly This is what a softmax does, so in this 
conveys only a few bits of information. case contrastive learning reduces to 
In contrast, audio, images and video standard supervised or self- supervised 
are high-bandwidth modalities that learning over a finite discrete set of 
implicitly convey large amounts of in- symbols. But in a real-valued high-di-
formation about the structure of the mensional space, there are far too 
world. This motivates a form of predic- many ways a vector Ŷ  could be different 
tion or reconstruction called self-su- from Y and to improve the model we 
pervised learning which is training to need to focus on those Ys that should 
“fill in the blanks” by predicting have high energy but currently have low 
masked or corrupted portions of the energy. Early methods to pick negative 
data. Self-supervised learning has been samples were based on Monte-Carlo 
very successful for training transform- methods, such as contrastive divergence 
ers to extract vectors that capture the for restricted Boltzmann machines48 and 
context-dependent meaning of a word noise-contrastive estimation.41

or word fragment and these vectors Generative Adversarial Networks 
work very well for downstream tasks. (GANs)36 train a generative neural net to 

For text, the transformer is trained produce contrastive samples by apply-
to predict missing words from a dis-
crete set of possibilities. But in high-

a	 As Gibbs pointed out, if energies are defined 
dimensional continuous domains so that they add for independent systems, they 
such as video, the set of plausible con- must correspond to negative log probabilities 
tinuations of a particular video seg- in any probabilistic interpretation.

62    COMMUNICATIONS OF THE ACM   |   JULY 2021  |   VOL.  64  |   NO.  7



turing lecture

ing a neural network to latent samples eschew the need for contrastive sam- ties with current AI suggests several di-
from a known distribution (for exam- ples. The first one, dubbed SwAV, quan- rections for improvement: 
ple, a Gaussian). The generator trains tizes the output of one network to train 1.	 Supervised learning requires too 
itself to produce outputs Ŷ to which the the other network,20 the second one, much labeled data and model-free rein-
model gives low energy E(Ŷ). The gen- dubbed BYOL, smoothes the weight forcement learning requires far too 
erator can do so using backpropagation trajectory of one of the two networks, many trials. Humans seem to be able to 
to get the gradient of E(Ŷ) with respect which is apparently enough to prevent a generalize well with far less experience.
to Ŷ. The generator and the model are collapse.40 2.	 Current systems are not as robust 
trained simultaneously, with the model Variational auto-encoders. A popu- to changes in distribution as humans, 
attempting to give low energy to train- lar recent self-supervised learning who can quickly adapt to such changes 
ing samples, and high energy to gener- method is the Variational Auto-Encoder with very few examples.
ated contrastive samples. (VAE).58 This consists of an encoder 3.	 Current deep learning is most 

GANs are somewhat tricky to opti- network that maps the image into a la- successful at perception tasks and gen-
mize, but adversarial training ideas tent code space and a decoder network erally what are called system 1 tasks. 
have proved extremely fertile, produc- that generates an image from a latent Using deep learning for system 2 tasks 
ing impressive results in image synthe- code. The VAE limits the information that require a deliberate sequence of 
sis, and opening up many new applica- capacity of the latent code by adding steps is an exciting area that is still in 
tions in content creation and domain Gaussian noise to the output of the its infancy.
adaptation34 as well as domain or style encoder before it is passed to the de- What needs to be improved. From 
transfer.87 coder. This is akin to packing small the early days, theoreticians of ma-

Making representations agree using noisy spheres into a larger sphere of chine learning have focused on the iid 
contrastive learning. Contrastive learn- minimum radius. The information ca- assumption, which states that the test 
ing provides a way to discover good fea- pacity is limited by how many noisy cases are expected to come from the 
ture vectors without having to recon- spheres fit inside the containing same distribution as the training ex-
struct or generate pixels. The idea is to sphere. The noisy spheres repel each amples. Unfortunately, this is not a re-
learn a feed-forward neural network that other because a good reconstruction alistic assumption in the real world: 
produces very similar output vectors error requires a small overlap between just consider the non-stationarities 
when given two different crops of the codes that correspond to different due to actions of various agents chang-
same image10 or two different views of samples. Mathematically, the system ing the world, or the gradually expand-
the same object17 but dissimilar output minimizes a free energy obtained ing mental horizon of a learning agent 
vectors for crops from different images through marginalization of the latent which always has more to learn and 
or views of different objects. The squared code over the noise distribution. How- discover. As a practical consequence, 
distance between the two output vectors ever, minimizing this free energy with the performance of today’s best AI sys-
can be treated as an energy, which is respect to the parameters is intracta- tems tends to take a hit when they go 
pushed down for compatible pairs and ble, and one has to rely on variational from the lab to the field.
pushed up for incompatible pairs.24,80 approximation methods from statisti- Our desire to achieve greater robust-

A series of recent papers that use cal physics that minimize an upper ness when confronted with changes in 
convolutional nets for extracting repre- bound of the free energy. distribution (called out-of-distribution 
sentations that agree have produced generalization) is a special case of the 
promising results in visual feature The Future of Deep Learning more general objective of reducing 
learning. The positive pairs are com- The performance of deep learning sys- sample complexity (the number of ex-
posed of different versions of the same tems can often be dramatically im- amples needed to generalize well) when 
image that are distorted through crop- proved by simply scaling them up. faced with a new task—as in transfer 
ping, scaling, rotation, color shift, blur- With a lot more data and a lot more learning and lifelong learning81—or 
ring, and so on. The negative pairs are computation, they generally work a lot simply with a change in distribution or 
similarly distorted versions of different better. The language model GPT-318 in the relationship between states of 
images which may be cleverly picked with 175 billion parameters (which is the world and rewards. Current super-
from the dataset through a process still tiny compared with the number of vised learning systems require many 
called hard negative mining or may synapses in the human brain) gener- more examples than humans (when 
simply be all of the distorted versions of ates noticeably better text than GPT-2 having to learn a new task) and the situ-
other images in a minibatch. The hid- with only 1.5 billion parameters. The ation is even worse for model-free rein-
den activity vector of one of the higher- chatbots Meena2 and BlenderBot73 also forcement learning23 since each re-
level layers of the network is subse- keep improving as they get bigger. warded trial provides less information 
quently used as input to a linear Enormous effort is now going into scal- about the task than each labeled exam-
classifier trained in a supervised man- ing up and it will improve existing sys- ple. It has already been noted61,76 that 
ner. This Siamese net approach has tems a lot, but there are fundamental humans can generalize in a way that is 
yielded excellent results on standard deficiencies of current deep learning different and more powerful than ordi-
image recognition bench- that cannot be overcome by scaling nary iid generalization: we can correctly 
marks.6,21,22,43,67 Very recently, two Sia- alone, as discussed here. interpret novel combinations of exist-
mese net approaches have managed to Comparing human learning abili- ing concepts, even if those combina-

JULY 2021  |   VOL.  64  |   NO.  7   |   COMMUNICATIONS OF THE ACM     63



turing lecture

tions are extremely unlikely under our because their activity vector in the variables.3,13,57,66 How should we struc-
training distribution, so long as they higher-level call can be reconstructed ture and train neural nets so they can 
respect high-level syntactic and se- later using the information in the fast capture these underlying causal prop-
mantic patterns we have already weights. Multiple time scales of adap- erties of the world?
learned. Recent studies help us clarify tion also arise in learning to learn, or How are the directions suggested by 
how different neural net architectures meta-learning.12,33,75 these open questions related to the 
fare in terms of this systematic general- Higher-level cognition. When think- symbolic AI research program from the 
ization ability.8,9 How can we design fu- ing about a new challenge, such as driv- 20th century? Clearly, this symbolic AI 
ture machine learning systems with ing in a city with unusual traffic rules, program aimed at achieving system 2 
these abilities to generalize better or or even imagining driving a vehicle on abilities, such as reasoning, being able 
adapt faster out-of-distribution? the moon, we can take advantage of to factorize knowledge into pieces 

From homogeneous layers to groups pieces of knowledge and generic skills which can easily recombined in a se-
of neurons that represent entities. Evi- we have already mastered and recom- quence of computational steps, and 
dence from neuroscience suggests that bine them dynamically in new ways. being able to manipulate abstract vari-
groups of nearby neurons (forming what This form of systematic generalization ables, types, and instances. We would 
is called a hyper-column) are tightly con- allows humans to generalize fairly well like to design neural networks which 
nected and might represent a kind of in contexts that are very unlikely under can do all these things while working 
higher-level vector-valued unit able to their training distribution. We can with real-valued vectors so as to pre-
send not just a scalar quantity but rather then further improve with practice, serve the strengths of deep learning 
a set of coordinated values. This idea is fine-tuning and compiling these new which include efficient large-scale 
at the heart of the capsules architec- skills so they do not need conscious at- learning using differentiable computa-
tures,47,59 and it is also inherent in the tention anymore. How could we endow tion and gradient-based adaptation, 
use of soft-attention mechanisms, neural networks with the ability to grounding of high-level concepts in 
where each element in the set is associ- adapt quickly to new settings by mostly low-level perception and action, han-
ated with a vector, from which one can reusing already known pieces of knowl- dling uncertain data, and using distrib-
read a key vector and a value vector (and edge, thus avoiding interference with uted representations.	
sometimes also a query vector). One way known skills? Initial steps in that direc-
to think about these vector-level units is tion include Transformers32 and Recur- References
as representing the detection of an ob- rent Independent Mechanisms.38 1.	 Abadi, M. et al. Tensorflow: A system for large-

scale machine learning. In Proceedings of the 12th 
ject along with its attributes (like pose It seems that our implicit (system 1) USENIX Symp. Operating Systems Design and 

information, in capsules). Recent pa- processing abilities allow us to guess Implementation, 2016, 265–283.
2.	 Adiwardana, D., Luong, M., So, D., Hall, J., Fiedel, N., 

pers in computer vision are exploring potentially good or dangerous futures, Thoppilan, R., Yang, Z., Kulshreshtha, A., Nemade, 

extensions of convolutional neural net- when planning or reasoning. This rais- G., Lu, Y., et al. Towards a human-like open-domain 
chatbot 2020; arXiv preprint arXiv:2001.09977.

works in which the top level of the hier- es the question of how system 1 net- 3.	 Arjovsky, M., Bottou, L., Gulrajani, I., and Lopez-Paz, 

archy represents a set of candidate ob- works could guide search and plan- D. Invariant risk minimization, 2019; arXiv preprint 
arXiv:1907.02893.

jects detected in the input image, and ning at the higher (system 2) level, 4.	 Ba, J., Hinton, G., Mnih, V., Leibo, J., and Ionescu, 
C. Using fast weights to attend to the recent past. 

operations on these candidates is per- maybe in the spirit of the value func- Advances in Neural Information Processing Systems, 
formed with transformer-like architec- tions which guide Monte-Carlo tree 2016, 4331–4339.

tures.19,84,86 5.	 Baars, B. A Cognitive Theory of Consciousness. 
 Neural networks that assign search for AlphaGo.77

Cambridge University Press, Cambridge, MA, 1993.
intrinsic frames of reference to objects Machine learning research relies on 6.	 Bachman, P., Hjelm, R., and Buchwalter, W. Learning 

representations by maximizing mutual information 
and their parts and recognize objects by inductive biases or priors in order to en- across views. Advances in Neural Information 
using the geometric relationships be- courage learning in directions which Processing Systems, 2019, 15535–15545.

7.	 Bahdanau, D., Cho, K., and Bengio, Y. Neural machine 
tween parts should be far less vulnerable are compatible with some assumptions translation by jointly learning to align and translate, 
to directed adversarial attacks,79 which about the world. The nature of system 2 2014; arXiv:1409.0473.

8.	 Bahdanau, D., Murty, S., Noukhovitch, M., Nguyen, T., 
rely on the large difference between the processing and cognitive neuroscience Vries, H., and Courville, A. Systematic generalization: 

information used by people and that theories for them5,30 suggests several What is required and can it be learned? 2018; 
arXiv:1811.12889.

used by neural nets to recognize objects. such inductive biases and architec- 9.	 Bahdanau, D., de Vries, H., O’Donnell, T., Murty, S., 

Multiple time scales of adaption. tures,11,45 which may be exploited to de- Beaudoin, P., Bengio, Y., and Courville, A. Closure: 
Assessing systematic generalization of clever models, 

Most neural nets only have two times- sign novel deep learning systems. How 2019; arXiv:1912.05783.

cales: the weights adapt slowly over do we design deep learning architec- 10.	 Becker, S. and Hinton, G. Self-organizing neural 
network that discovers surfaces in random dot 

many examples and the activities adapt tures and training frameworks which stereograms. Nature 355, 6356 (1992), 161–163.
11.	 Bengio, Y. The consciousness prior, 2017; 

rapidly changing with each new input. incorporate such inductive biases? arXiv:1709.08568.
Adding an overlay of rapidly adapting The ability of young children to per- 12.	 Bengio, Y., Bengio, S., and Cloutier, J. Learning a 

and rapidly, decaying “fast weights”49 synaptic learning rule. In Proceedings of the IEEE 
 form causal discovery37 suggests this 1991 Seattle Intern. Joint Conf. Neural Networks 2.

introduces interesting new computa- may be a basic property of the human 13.	 Bengio, Y., Deleu, T., Rahaman, N., Ke, R., Lachapelle, 
S., Bilaniuk, O., Goyal, A., and Pal, C. A meta-

tional abilities. In particular, it creates brain, and recent work suggests that transfer objective for learning to disentangle 
a high-capacity, short-term memory,4 optimizing out-of-distribution gener- causal mechanisms. In Proceedings of ICLR’2020; 

arXiv:1901.10912.
which allows a neural net to perform alization under interventional changes 14.	 Bengio, Y., Ducharme, R., and Vincent, P. A neural 
true recursion in which the same neu- can be used to train neural networks to probabilistic language model. NIPS’2000, 2001, 932–938.

15.	 Bengio, Y., Lamblin, P., Popovici, D., and Larochelle, 
rons can be reused in a recursive call discover causal dependencies or causal H. Greedy layer-wise training of deep networks. In 

64    COMMUNICATIONS OF THE ACM   |   JULY 2021  |   VOL.  64  |   NO.  7



turing lecture

Proceedings of NIPS’2006, 2007. unnormalized statistical models. In Proceedings of the 69.	 Morgan, N., Beck, J., Allman, E., and Beer, J. Rap: 
16.	 Bergstra, J., Breuleux, O., Bastien, F., Lamblin, P., 13th Intern. Conf. Artificial Intelligence and Statistics, A ring array processor for multilayer perceptron 

Pascanu, R., Desjardins, G., Turian, J., Warde-Farley, 2010, 297–304. applications. In Proceedings of the IEEE Intern. 
D., and Bengio, Y. Theano: A CPU and GPU math 42.	 He, K., Fan, H., Wu, Y., Xie, S., and Girshick, R. Conf. Acoustics, Speech, and Signal Processing, 1990, 
expression compiler. In Proceedings of SciPy, 2010. Momentum contrast for unsupervised visual 1005–1008.

17.	 Bromley, J., Guyon, I., LeCun, Y., Säkinger, E., and representation learning. In Proceedings of CVPR’2020, 70.	 Nair, V. and Hinton, G. Rectified linear units improve 
Shah, R. Signature verification using a “Siamese” time June 2020. restricted Boltzmann machines. In Proceedings of the 
delay neural network. Advances in Neural Information 43.	 He, K., Zhang, X., Ren, S., and Sun, J. Deep residual ICML’2010.
Processing Systems, 1994, 737–744. learning for image recognition. In Proceedings of 71.	 Paszke, A., et al. Automatic differentiation in pytorch. 

18.	 Brown, T. et al. Language models are few-shot CVPR’2016, 770–778. 2017.
learners, 2020; arXiv:2005.14165. 44.	Hinton, G. A parallel computation that assigns 72.	 Robinson, A. An application of recurrent nets to phone 

19.	 Carion, N., Massa, F., Synnaeve, G., Usunier, N., Kirillov, canonical object-based frames of reference. In probability estimation. IEEE Trans. Neural Networks 5, 
A., and Zagoruyko, S. End-to-end object detection Proceedings of the 7th Intern. Joint Conf. Artificial 2 (1994), 298–305.
with transformers. In Procedings of ECCV’2020; Intelligence 2, 1981, 683–685. 73.	 Roller, S., et al. Recipes for building an open domain 
arXiv:2005.12872. 45.	 Hinton, G. Mapping part-whole hierarchies into chatbot, 2020; arXiv:2004.13637.

20.	 Caron, M., Misra, I., Mairal, J., Goyal, P., Bojanowski, connectionist networks. Artificial Intelligence 46, 1-2 74.	 Rumelhart, D., Hinton, G., and Williams, R. Learning 
P., and Joulin, A. Unsupervised learning of visual (1990), 47–75. representations by back-propagating errors. Nature 
features by contrasting cluster assignments, 2020;. 46.	 Hinton, G. et al. Deep neural networks for acoustic 323 (1986), 533–536.
arXiv:2006.09882. modeling in speech recognition: The shared views of 75.	 Schmidhuber, J. Evolutionary principles in self-

21.	 Chen, T., Kornblith, S., Norouzi, M., and Hinton, G. A four research groups. IEEE Signal Processing 29, 6 referential learning. Diploma thesis, Institut f. 
simple framework for contrastive learning of visual (2012), 82–97. Informatik, Tech.Univ. Munich, 1987.
representations, 2020; arXiv:2002.05709. 47.	 Hinton, G., Krizhevsky, A., and Wang, S. Transforming 76.	 Shepard, R. Toward a universal law of generalization 

22.	 Chen, X., Fan, H., Girshick, R., and He, K. Improved auto-encoders. In Proceedings of Intern. Conf. for psychological science. Science 237, 4820 (1987), 
baselines with momentum contrastive learning, 2020; Artificial Neural Networks. Springer, 2011, 44–51. 1317–1323.
arXiv:2003.04297. 48.	 Hinton, G., Osindero, S., and Teh, Y-W. A fast-learning 77.	 Silver, D., et al. Mastering the game of go with deep 

23.	 Chevalier-Boisvert, M., Bahdanau, D., Lahlou, S., algorithm for deep belief nets. Neural Computation 18 neural networks and tree search. Nature 529, 7587 
Willems, L., Saharia, C., Nguyen, T., and Bengio, Y. (2006), 1527–1554. (2016), 484.
Babyai: First steps towards grounded language 49.	Hinton, G. and Plaut, D. Using fast weights to deblur 78.	 Sukhbaatar, S., Szlam, A., Weston, J., and Fergus, R. 
learning with a human in the loop. In Proceedings in old memories. In Proceedings of the 9th Annual Conf. End-to-end memory networks. Advances in Neural 
ICLR’2019; arXiv:1810.08272. Cognitive Science Society, 1987, 177–186. Information Processing Systems 28, 2015, 2440–2448. 

24.	 Chopra, S., Hadsell, R., and LeCun, Y. Learning a 50.	 Hinton, G. and Salakhutdinov, R. Reducing the C. Cortes et al., eds. Curran Associates, Inc.; http://
similarity metric discriminatively, with application to dimensionality of data with neural networks. Science papers.nips.cc/paper/5846-end-to-end-memory-
face verification. In Proceedings of the 2005 IEEE 313 (July 2006), 504–507. networks.pdf.
Computer Society Conf. Computer Vision and Pattern 51.	 Hinton, G., Srivastava, N., Krizhevsky, A., Sutskever, 79.	 Szegedy, C., Zaremba, W., Sutskever, I., Bruna, J., 
Recognition 1, 539–546. I., and Salakhutdinov, R. Improving neural networks Erhan, D., Goodfellow, I., and Fergus, R. Intriguing 

25.	 Collobert, R., Kavukcuoglu, K., and Farabet, C. Torch7: by preventing co-adaptation of feature detectors. In properties of neural networks. In Proceedings of 
A matlab-like environment for machine learning. In Proceedings of NeurIPS’2012; arXiv:1207.0580. ICLR’2014; arXiv:1312.6199.
Proceedings of NIPS Worskshop BigLearn, 2011. 52.	 Hochreiter, S. and Schmidhuber, J. Long short-term 80.	 Taigman, Y., Yang, M., Ranzato, M., and Wolf, L. Web-

26.	 Collobert, R. and Weston, J. A unified architecture for memory. Neural Computation 9, 8 (1997), 1735–1780. scale training for face identification. In Proceedings of 
natural language processing: Deep neural networks 53.	 Ioffe, S. and Szegedy, C. Batch normalization: CVPR’2015, 2746–2754.
with multitask learning. In Proceedings of ICML’2008. Accelerating deep network training by reducing 81.	 Thrun, S. Is learning the n-th thing any easier than 

27.	 Conneau, A. and Lample, G. Cross-lingual language internal covariate shift. 2015. learning the first? In Proceedings of NIPS’1995. MIT 
model pretraining. Advances in Neural Information 54.	Jarrett, K., Kavukcuoglu, K., Ranzato, M., and LeCun, Press, Cambridge, MA, 640–646.
Processing Systems 32, 2019. H. Wallach et al., eds. Y. What is the best multi-stage architecture for object 82.	 Utgoff, P. and Stracuzzi, D. Many-layered learning. 
7059–7069. Curran Associates, Inc.; http://papers. recognition? In Proceedings of ICCV’09, 2009. Neural Computation 14 (2002), 2497–2539, 2002.
nips.cc/paper/8928-cross-lingual-language-model- 55.	 Jia, Y., Shelhamer, E., Donahue, J., Karayev, S., Long, 83.	 Van Essen, D. and Maunsell, J. Hierarchical 
pretraining.pdf. J., Girshick, R., Guadarrama, S., and Darrell, T. Caffe: organization and functional streams in the visual 

28.	 Dahl, G., Yu, D., Deng, L., and Acero, A. Context- Convolutional architecture for fast feature embedding. cortex. Trends in Neurosciences 6 (1983), 370–375.
dependent pre-trained deep neural networks for large- In Proceedings of the 22nd ACM Intern. Conf. 84.	 van Steenkiste, S., Chang, M., Greff, K., and 
vocabulary speech recognition. IEEE Trans. Audio, Multimedia, 2014, 675–678. Schmidhuber, J. Relational neural expectation 
Speech, and Language Processing 20, 1 (2011), 30–42. 56.	 Kahneman, D. Thinking, Fast and Slow. Macmillan, 2011. maximization: Unsupervised discovery of objects and 

29.	 Dayan, P. and Abbott, L. Theoretical Neuroscience. The 57.	 Ke, N., Bilaniuk, O., Goyal, A., Bauer, S., Larochelle, H., their interactions, 2018; arXiv:1802.10353.
MIT Press, 2001. Pal, C., and Bengio, Y. Learning neural causal models 85.	 Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., 

30.	 Dehaene, S., Lau, H., and Kouider, S. What is from unknown interventions, 2019; arXiv:1910.01075. Jones, L., Gomez, A., Kaiser, T., and Polosukhin, 
consciousness, and could machines have it? Science 58.	 Kingma, D. and Welling, M. Auto-encoding variational I. Attention is all you need. Advances in Neural 
358, 6362 (2017, 486–492. bayes. In Proceedings of the Intern. Conf. Learning Information Processing Systems, 2017, 5998–6008.

31.	 Deng, J., Dong, W., Socher, R., Li, L., Li, K., and Representations, 2014. 86.	 Zambaldi, V., et al. Relational deep reinforcement 
Fei-Fei, L. ImageNet: A large-scale hierarchical 59.	 Kosiorek, A., Sabour, S., Teh, Y., and Hinton, G. Stacked learning, 2018; arXiv:1806.01830.
image database. In Proceedings of 2009 IEEE Conf. capsule autoencoders. Advances in Neural Information 87.	 Zhu, J-Y., Park, T., Isola, P., and Efros, A. Unpaired 
Computer Vision and Pattern Recognition, 248–255. Processing Systems, 2019, 15512–15522. image-to-image translation using cycle-consistent 

32.	 Devlin, J., Chang, M., Lee, K., and Toutanova, K. Bert: 60.	Krizhevsky, A., Sutskever, I., and Hinton, G. ImageNet adversarial networks. In Proceedings of the 2017 IEEE 
Pre-training of deep bidirectional transformers for classification with deep convolutional neural Intern. Conf. on Computer Vision, 2223–2232.
language understanding. In Proceedings of ACL’2019; networks. In Proceedings of NIPS’2012.
arXiv:1810.04805. 61.	 Lake, B., Ullman, T., Tenenbaum, J., and Gershman, Yoshua Bengio is a professor in the Department 

33.	 Finn, C., Abbeel, P., and Levine, S. Model-agnostic S. Building machines that learn and think like people. of Computer Science and Operational Research at 
meta-learning for fast adaptation of deep networks, Behavioral and Brain Sciences 40 (2017). the Université de Montréal. He is also the founder 
2017; arXiv:1703.03400. 62.	 Lample, G. and Charton, F. Deep learning for and scientific director of Mila, the Quebec Artificial 

34.	 Ganin, Y and Lempitsky, V. Unsupervised domain symbolic mathematics. In Proceedings of ICLR’2020; Intelligence Institute, and the co-director of CIFAR’s 
adaptation by backpropagation. In Proceedings of arXiv:1912.01412. Learning in Machines & Brains program.
Intern. Conf. Machine Learning, 2015, 1180–1189. 63.	 LeCun, Y., Bengio, Y., and Hinton, G. Deep learning. 

35.	 Glorot, X., Bordes, A., and Bengio, Y. Deep sparse Nature 521, 7553 (2015), 436–444. Yann LeCun is VP and Chief AI Scientist at Facebook 
rectifier neural networks. In Proceedings of 64.	 LeCun, Y., Boser, B., Denker, J., Henderson, D., Howard, and Silver Professor at New York University affiliated with 
AISTATS’2011. R., Hubbard, W., and Jackel, L. Backpropagation the Courant Institute of Mathematical Sciences and the 

36.	 Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., applied to handwritten zip code recognition. Neural Center for Data Science, New York, NY, USA.
Warde-Farley, D., Ozair, S., Courville, A., and Bengio, Computation 1, 4 (1989), 541–551.
Y. Generative adversarial nets. In Advances in Neural 65.	 LeCun, Y., Bottou, L., Bengio, Y., and Haffner, P. Geoffrey Hinton is the Chief Scientific Advisor of the 
Information Processing Systems, 2014, 2672–26804. Gradient-based learning applied to document Vector Institute, Toronto, Vice President and Engineering 

37.	 Gopnik, A., Glymour, C., Sobel, D., Schulz, L., Kushnir, recognition. In Proceedings of the IEEE 86, 11 (1998), Fellow at Google, and Emeritus Distinguished Professor of 
T., and Danks, D. A theory of causal learning in 2278–2324. Computer Science at the University of Toronto, Canada.
children: causal maps and bayes nets. Psychological 66.	 Lopez-Paz, D., Nishihara, R., Chintala, S., Scholkopf, B., 
Review 111, 1 (2004). and Bottou, L. Discovering causal signals in images. This work is licensed under a http://

38.	 Goyal, A., Lamb, A., Hoffmann, J., Sodhani, S., Levine, In Proceedings of the IEEE Conf. Computer Vision and creativecommons.org/licenses/by/4.0/
S., Bengio, Y., and Schölkopf, B. Recurrent independent Pattern Recognition, 2017, 6979–6987.
mechanisms, 2019; arXiv:1909.10893. 67.	 Misra, I. and Maaten, L. Self-supervised learning of 

39.	 Graves, A. Generating sequences with recurrent neural pretext-invariant representations. In Proceedings of 
networks, 2013; arXiv:1308.0850. CVPR’2020, June 2020; arXiv:1912.01991.

40.	Grill, J-B. et al. Bootstrap your own latent: A 68.	 Mohamed, A., Dahl, G., and Hinton, G. Deep belief Watch the authors discuss  
new approach to self-supervised learning, 2020; networks for phone recognition. In Proceedings this work in the exclusive 
aeXiv:2006.07733. of NIPS Workshop on Deep Learning for Speech Communications video.  

41.	 Gutmann, M. and Hyvärinen, A. Noise-contrastive Recognition and Related Applications. (Vancouver, https://cacm.acm.org/videos/ 
estimation: A new estimation principle for Canada, 2009). deep-learning-for-ai

JULY 2021  |   VOL.  64  |   NO.  7   |   COMMUNICATIONS OF THE ACM     65