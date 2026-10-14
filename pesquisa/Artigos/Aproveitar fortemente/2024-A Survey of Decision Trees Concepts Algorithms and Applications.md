---
source_file: "2024-A Survey of Decision Trees Concepts Algorithms and Applications.txt"
original_rel_path: "Trabalhos\Artigos\Aproveitar fortemente\txt\2024-A Survey of Decision Trees Concepts Algorithms and Applications.txt"
category: "Artigos_Aproveitar_fortemente"
extension: ".txt"
sha256: "221cb95e52a0946b1569c336e64dfee38c747ad340d22cab269d0b2e91f3789c"
extracted_at: "2026-09-19T23:16:59.211672"
---

﻿Received 26 May 2024, accepted 17 June 2024, date of publication 19 June 2024, date of current version 27 June 2024.
Digital Object Identifier 10.1109/ACCESS.2024.3416838

A Survey of Decision Trees: Concepts,
Algorithms, and Applications
IBOMOIYE DOMOR MIENYE , (Member, IEEE), AND NOBERT JERE
Department of Information Technology, Walter Sisulu University, Buffalo City Campus, East London 5200, South Africa

Corresponding author: Ibomoiye Domor Mienye (imienye@wsu.ac.za)

ABSTRACT Machine learning (ML) has been instrumental in solving complex problems and significantly
advancing different areas of our lives. Decision tree-based methods have gained significant popularity
among the diverse range of ML algorithms due to their simplicity and interpretability. This paper presents a
comprehensive overview of decision trees, including the core concepts, algorithms, applications, their early
development to the recent high-performing ensemble algorithms and their mathematical and algorithmic
representations, which are lacking in the literature and will be beneficial to ML researchers and industry
experts. Some of the algorithms include classification and regression tree (CART), Iterative Dichotomiser 3
(ID3), C4.5, C5.0, Chi-squared Automatic Interaction Detection (CHAID), conditional inference trees, and
other tree-based ensemble algorithms, such as random forest, gradient-boosted decision trees, and rotation
forest. Their utilisation in recent literature is also discussed, focusing on applications in medical diagnosis
and fraud detection.

INDEX TERMS Algorithms, CART, C4.5, C5.0, decision tree, ensemble learning, ID3, machine learning.

I. INTRODUCTION Furthermore, decision trees are known for their inter-
Machine learning-based applications are revolutionising pretability [9], [10]. The resulting tree structure allows users
various industries and sectors, including healthcare, finance, to understand and interpret the decision-making process
andmarketing [1], [2], [3], [4].With the advancement of tech- easily. This is especially valuable in domains where trans-
nology and the availability of large datasets, ML algorithms parency and explainability are crucial, making it easier for
have become increasingly powerful and accurate in making stakeholders to trust and validate the results. Another sig-
predictions and informed decisions. These applications are nificance of decision tree-based algorithms is their ability to
transforming how organisations operate and paving the way handle categorical and numerical data. Traditional statistical
for a more efficient and data-driven future. methods often struggle with categorical variables, requiring

Decision tree-based algorithms have been employed in them to be converted into numerical values. Decision trees,
diverse applications, including but not limited to classifi- on the other hand, can directly handle both types of data,
cation, regression, and feature selection [5], [6], [7]. The eliminating the need for data preprocessing. This makes
basic idea behind decision tree-based algorithms is that decision tree-based algorithms more versatile and efficient in
they recursively partition the data into subsets based on the a wide range of applications.
values of different attributes until a stopping criterion is There are a few reviews of decision trees in the lit-
met. This process results in a tree-like structure, where each erature; for example, Che et al. [11] presented a review
node represents a decision or a split based on a specific of decision trees and ensemble classifiers with specific
attribute [8]. The algorithm determines the best attribute to applications to bioinformatics. The review focused on ID3,
use for each split based on certain criteria, such as information CART, and ensemble methods such as bagging, boosting,
gain, gain ratio, and Gini index. and stacked generalization. Cañete-Sifuentes et al. [12]

reviewed multivariate decision trees (MDT) and compared
the performance of several MDT induction classifiers.

The associate editor coordinating the review of this manuscript and
approving it for publication was Yilun Shang. Anuradha and Gupta [13] presented a review of decision


 2024 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License.
86716 For more information, see https://creativecommons.org/licenses/by/4.0/ VOLUME 12, 2024



I. D. Mienye, N. Jere: Survey of Decision Trees: Concepts, Algorithms, and Applications

tree classifiers, focusing on a high-level description of key
concepts, such as node splitting and tree pruning. Meanwhile,
Costa and Pedreira [14] reviewed recent decision tree-based
classifier advances. The paper covered threemain issues: how
decision trees fit the training data, their generalization, and
interpretability.

However, most of the existing surveys and reviews of
decision trees focus on their applications in specific domains
or a high-level overview of the decision tree concept. There-
fore, the current literature lacks a comprehensive overview of
decision tree algorithms, their early developments, succinct
mathematical formulations, and algorithmic representations
in a single peer-reviewed paper. Therefore, it is essential to
have a review that fills this gap in view of the continuous use
and prevalence of decision tree-based algorithms and their
application in today’s technological advancements. Hence,
in this study, we present a detailed review of decision tree-
based algorithms. Specifically, the paper aims to cover the
different decision tree algorithms, including ID3, C4.5, C5.0,
CART, conditional inference trees, and CHAID, together FIGURE 1. A decision tree example.

with other tree-based ensemble algorithms, such as random
forest, rotation forest, and gradient boosting decision trees.
The paper aims to present their mathematical formulations as shown in Figure 1. The root node, which is the starting
and algorithmic representations clearly and concisely. point of the tree, represents the entire dataset. The algorithm

The rest of the paper is structured as follows: Section II identifies the feature and the threshold that leads to the best
presents a comprehensive overview of the decision tree, split based on a specific criterion [20]. The process continues
covering key areas such as splitting criteria and tree recursively, with each subset of the data being further split at
pruning methods. Section III discusses different decision each child node. This continues until a stopping criterion is
tree algorithms, their learning process, splitting criteria, and reached, typically when the nodes are pure (i.e., all data points
mathematical formulations. Section IV reviews decision tree in a node belong to the same class) or when a predefined
applications in recent literature, including applications in depth of the tree is reached. The nodes where the tree ends,
medical diagnosis and fraud detection. Section V discusses called leaf node or terminal node, represent the outcomes
key findings and future research directions, and Section VI or class labels. The decision to split at each node is made
concludes the paper. using mathematical formulations such as information gain,

Gini impurity, or variance reduction.
II. OVERVIEW OF DECISION TREE Furthermore, the success of decision tree techniques
This section provides a comprehensive overview of decision mainly depends on several factors contributing to their
trees, focusing on the main building blocks and splitting performance, interpretability, and applicability to a wide
criteria. Decision trees, as a concept in ML, have a range of problems. These factors include data quality, tree
history that dates back to the mid-20th century. Initial depth, splitting criteria, and tree pruning method. According
decision tree studies were started by Charles J. Clopper and to Piramuthu [21], the effectiveness of decision trees is highly
Egon S. Pearson in 1934, who introduced the concept of dependent on the training data quality. Hence, it is necessary
binary decision processes [15], [16]. However, the modern to use clean or preprocessed data not containing missing
implementation of decision trees in the context of ML started values and outliers, which can significantly enhance the
decades later. Breiman [17] developed the CART algorithm in performance of the resulting models. Additionally, feature
1984, introducing concepts such as the Gini index and binary selection and feature engineering are necessary because
splitting, which are now widespread in decision tree designs. inputting relevant and well-transformed features can lead to
Quinlan [18] developed ID3, one of the first notable decision more efficient and accurate splits.
tree algorithms, in 1986. Furthermore, Quinlan [19] enhanced
the ID3, introducing the C4.5 decision tree in 1993. These A. SPLITTING RULES
developments and integration of decision trees into ensemble The term splitting criteria, or splitting rules, describes the
methods like random forests and boosting algorithms have methods used to determine where a tree should make a split
solidified their place as fundamental algorithms in machine in its nodes, effectively deciding how to divide the dataset
learning. into subsets based on different conditions [22], [23]. The

The learning procedure of decision trees involves a series choice of splitting criterion is crucial as it directly impacts
of steps where the data is split into homogenous subsets, the tree’s structure and, ultimately, its performance. Different

VOLUME 12, 2024 86717



I. D. Mienye, N. Jere: Survey of Decision Trees: Concepts, Algorithms, and Applications

decision tree algorithms use different criteria for this purpose, tree to overcome the bias of information gain towards features
including the following: that have several distinct values by considering the number

and size of branches when choosing an attribute. The IGR
1) GINI INDEX normalises the information gain by dividing it by the intrinsic
Gini Index, also called Gini Impurity, is a well-known split- information or split information (SplitInfo) of the split. This
ting criterion used in the CART algorithm. It measures the normalisation reduces the bias towards the multi-valued
probability of a randomly chosen sample being incorrectly attributes, resulting in more balanced and effective decision
classified if it was randomly labelled [24]. It is used to trees [26], [27]. The IGR criterion is calculated as:
evaluate the quality of a split in the tree and is calculated for InformationGain(S,A)
each potential split in the dataset. The Gini Index for a set can IGR(S,A) = (4)

SplitInfo(S,A)
be represented mathematically as: ∑n 4) CHI-SQUARE

Gini(S) = 1 − p2i (1) The Chi-Square (χ2) splitting criterion measures the inde-
pendence between an attribute and the class [28]. The χ2

i=1

where S, n, and pi represent a set of samples, the number test assesses whether the distribution of sample observations
of unique classes in the set, and the proportion of the across different categories deviates significantly from what
samples in the set that belong to class i, respectively. This would be expected if the categories were independent of the
formula calculates the probability of incorrectly classifying class. Given an attribute A with different categories and a
a randomly chosen element from the set S based on the target class C , the χ2 ca∑n b

r ∑e computed as:
distribution of classes in it. The value of Gini Impurity k

χ2 (Oij − E )2
ranges from 0 (perfect purity) to 1 (maximal impurity) ij

= (5)
[25]. When the algorithm evaluates where to split the data, E

i ij
=1 j=1

it calculates the Gini index for each potential split and where r is the number of categories of the attribute A, k is the
typically chooses the split that results in the lowest weighted number of classes, Oij is the observed frequency in cell (i, j)
Gini Impurity for the resulting subsets. that belong to class j), and Eij is the expected frequency in cell

(i, j) under the null hypothesis of independence, calculated
2) INFORMATION GAIN as E (row_totali×column_totalj)

ij =
Information Gain (IG), a criterion used in ID3 and C4.5, total_samples . A high χ2 value indicates

a significant association between the attribute and the class,
is based on the notion of entropy in information theory. suggesting that the attribute is a good predictor for splitting
Entropy measures the unpredictability or randomness in a the dataset [29], [30]. This criterion is useful for categorical
set of data [26]. The IG technique searches for a split that data, and it identifies the most significant splits based on the
maximizes the difference in certainty or decreases uncertainty chi-square test of independence.
before and after the split. It determines the effectiveness of an
attribute in splitting the training data into homogenous sets. B. TREE PRUNING METHODS
Meanwhile, the entropy (E) o∑f a set S is given by the formula: 1) PRE-PRUNING

n Pre-pruning or early stopping techniques are used to effec-
E(S) = − pi log2(pi) (2) tively limit the size of the tree and reduce the possibility

i=1 of overfitting [31], [32]. The main benefit of pre-pruning
where n is the number of unique classes in the set, and pi is is its simplicity and the reduction in computational cost
the proportion of the samples in the set that belong to class i. due to the construction of smaller trees. However, setting
Therefore, the IG for a split on a dataset S with an attribute A the pre-pruning parameters too aggressively may lead to
can be computed as follows: ∑ underfitting. Meanwhile, this strategy halts the tree’s growth

|Sv| according to predefined criteria, such as maximum depth,
IG = E(S) − E(Sv) (3)

|S| minimum number of instances in a node, minimum informa-
v∈ Values(A) tion gain, and maximum number of leaf nodes [33].

where Values(A) are the different values that attribute A can
take, and Sv is the subset of S for which attribute A has the 2) POST-PRUNING
value v [27]. This formula calculates the change in entropy Post-pruning, also called backward pruning, is a technique
from the original set S to the sets Sv created after the split. used to trim down a fully grown tree to improve its
A higher IG indicates a more effective attribute for splitting generalization capabilities. Unlike pre-pruning, which stops
the data, as it results in more homogeneous subsets. the tree from fully growing, post-pruning allows the tree

to first grow to its full size and then prunes it back [34].
3) INFORMATION GAIN RATIO Common post-pruning techniques include reduced error
The information gain ratio (IGR), an extension of information pruning, pessimistic error pruning, error-based pruning,
gain, is a splitting criterion mainly used in the C4.5 decision minimum error pruning, and cost complexity pruning [33].

86718 VOLUME 12, 2024



I. D. Mienye, N. Jere: Survey of Decision Trees: Concepts, Algorithms, and Applications

Post-pruning primarily removes sections of the tree that Algorithm 1 ID3 Decision Tree Algorithm
contribute little to predicting the target variable. It often Require: Training data set D = {(x1, y1), (x2, y2), . . . ,
requires a separate validation dataset to assess the impact of (xm, ym)}
pruning [35]. This dataset tests the tree’s performance as it Ensure: Decision tree T .
undergoes pruning. 1: function ID3(D)

2: if D is empty then return a terminal node with

C. INTERPRETABILITY OF DECISION TREES default class cdefault
3: end if

Decision trees are known for their inherent interpretability,
4: if all instances in D have same class label y then

making them valuable in various domains where understand- return a terminal node with class y
ing the decision-making process is crucial [14], [36]. Unlike

5: end if
many other ML algorithms that produce black-box models,

6: if the attribute set J is empty then return a terminal
decision trees offer transparency by representing the decision node with the prevalent class in D
process as a sequence of simple, intuitive rules. Specifically,

7: end if
each node in a decision tree corresponds to a feature and a

8: Select the feature f that best splits the data using
decision threshold, and the path from the root to a leaf node information gain.
represents a series of decisions based on the feature values.

9: Create a decision node for f .
This clear structure allows stakeholders to easily comprehend

10: for each value bi of f doand interpret how the model arrives at its predictions.
11: Create a branch for b

Furthermore, while complex models such as deep neural i.
12: Let Di be the subset of D where xi = b

networks and ensemble methods may achieve high accuracy, i.
13: Recursively build the subtree for Di.their black-box nature makes it challenging to understand
14: Attach the subtree to the branch for b

how they arrive at their predictions [37], [38]. In contrast, i.
15: end for

decision trees provide a visual representation of the decision-
16: return the decision node.

making process, allowing stakeholders to trace each decision
17: end function

back to specific features and thresholds. For instance, in a
medical diagnosis application, a decision tree model may
reveal which symptoms or risk factors are most influential Information Gain is chosen to make the decision at the node,
in predicting a particular disease. This transparency enables and the dataset is partitioned accordingly. This process is
domain experts to validate the model’s decisions and identify repeated recursively for each partitioned subset until one
potential biases or errors, thereby improving trust in the of the stopping criteria is met, such as when no further
model’s predictions. information can be gained, all instances in a subset belong to

Additionally, decision trees can facilitate feature selection the same class, or there are no more attributes left to consider.
and variable importance analysis, aiding in feature engineer- Lastly, the ID3’s limitations include its inability to directly
ing and model refinement [39], [40], [41]. By examining handle continuous variables and overfitting.
the splits in the tree and the associated feature importance
scores, practitioners can identify the most influential features B. 4.5 AND C5.0
in the prediction process. This information can guide data Quinlan [19] proposed the C4.5 in 1993 as an extension of the
preprocessing efforts and inform decisions about feature ID3 algorithm and is designed to handle both continuous and
inclusion or exclusion in the model, leading to more efficient discrete attributes. It introduces the concept of information
and interpretable models. gain ratio, described in Equation 4, to select the best attribute

to split the dataset at each node, aiming to overcome the
III. DECISION TREE ALGORITHMS bias towards attributes with more levels found in the original
A. ITERATIVE DICHOTOMISER 3 Information Gain criterion used by ID3.
The ID3 decision tree was first introduced in 1986 by C5.0 is an improvement over C4.5, also proposed by Quin-
Quinlan [18]. It is particularly noted for its simplicity lan [42], designed to be faster and more memory efficient.
and effectiveness in solving classification problems. The It introduces several enhancements, such as advanced pruning
algorithm follows a top-down, greedy search approach methods and the ability to handle more complex types of
through the given dataset to construct a decision tree. It begins data. C5.0 maintains the use of the information gain ratio for
with the entire dataset and divides it into subsets based on the selecting attributes but optimises the algorithm’s execution
attribute that maximizes the Information Gain (Equation 3), and the resulting decision tree’s size.
intending to efficiently classify the instances at each node of
the tree. The ID3 is described in Algorithm 1. C. CLASSIFICATION AND REGRESSION TREES
The algorithm iterates through every unused attribute and The CART decision tree was proposed in 1984 by

calculates the Information Gain for a dataset split by the Breiman [43]. Unlike C4.5, CART creates binary trees
attribute’s possible values. The attribute with the highest irrespective of the type of target variables. It uses different

VOLUME 12, 2024 86719



I. D. Mienye, N. Jere: Survey of Decision Trees: Concepts, Algorithms, and Applications

splitting criteria for classification and regression tasks. For computed as:
classification tasks, it uses the Gini index (Equation 1) as a ∑r ∑k
measure to create splits [44], [45]. Meanwhile, it employs (Oi − Eij)2

χ2 j
= (7)

variance as the splitting criterion in regression tasks [46], E
i=1 j=1 ij

[47]. The variance reduction for a set S when split on attribute
A is calculated as where r is the number of categories of the attribute A, k is

: ( the number of different classes in the target variable C , Oij
is the observed frequency in the ith category of attribute A and

|S
VR left |

= V (S) − V (Sl ft )
|S ) e the jth class ofC , andEij is the expected frequency in the same

| cell under the null hypothesis of independence, calculated as
|Sright |

+ V (S
S right ) (6) E (row_totali×column_totalj)

ij = total_samples . The attribute with the highest
| |

χ2 statistic is selected for splitting at each node. A higher χ2

value indicates a stronger association between the attribute
where V (S) is the variance of the target variable in set S, and the target variable, suggesting that the attribute is a good
and Sleft and Sright are the subsets of S after the split on predictor for splitting the dataset. Algorithm 3 details the
attribute A. In both cases, the goal is to choose the split that working process of the CHAID algorithm.
maximizes the respective measure (Gini impurity reduction
for classification and variance reduction for regression), Algorithm 3 CHAID Algorithm
leading to the most homogenous subsets possible. The CART Require: D = {(x1, y1), (x2, y2), . . . , (xm, ym)}.
algorithm is described in Algorithm 2. Ensure: Decision tree T .

1: function CHAID(D)
Algorithm 2 CART Algorithm 2: if D is empty then return a terminal node with
Require: D = {(x1, y default class c

1), (x2, y2), . . . , (xm, ym)}. default

Ensure: Decision tree T . 3: end if
1: function CART(D) 4: if all instances in D have the same class label y then
2: if D is empty then return a terminal node with return a terminal node with class y

default value or class c 5: end if
default

3: end if 6: if the feature set F is empty then return a terminal
4: if all instances in D have the same class label y then node with the most prevalent class in D

return a terminal node with class y 7: end if
5: end if 8: Calculate the chi-squared statistic for each feature
6: if the feature set F is empty then return a leaf node and its possible values.

with the average value of y in D 9: Select the feature and value with the highest chi-
7: end if squared value.
8: Select the best feature f and split point s that 10: Create a decision node for the selected feature and

minimize the cost function. value.
9: Create a decision node for f and s. 11: Partition the data set D based on the selected feature

10: Partition the data set D into two subsets D1 and and value.
D 12: for each subset Di of D do
2 based on the split.

11: Recursively build the subtree for D1 and D2. 13: Recursively build the subtree for Di.
12: Attach the subtrees to the decision node. 14: Attach the subtree to the decision node.
13: return the decision node. 15: end for
14: end function 16: return the decision node.

17: end function

D. CHI-SQUARED AUTOMATIC INTERACTION DETECTION E. CONDITIONAL INFERENCE TREES
The CHAID algorithm, developed by Kass [48], performs The conditional inference trees, developed by Hothorn et al.
multi-level splits when computing classification trees. It is [51], is a non-parametric class of decision trees that use
particularly robust in the detection of interaction between statistical tests to determine splits, reducing bias and variance
variables. CHAID can handle more than two categories and providing a more statistically sound approach. It is
for each variable, and it uses the Chi-Square (χ2) test mostly useful when solving complex, non-linear relationships
of independence as its splitting criterion [49], [50]. This that exist between the predictor variables and the response
statistical test is applied to assess the relationship between variable [52], [53]. Assuming S is a node in the tree, with m
categorical variables. For a given attribute A with differ- examples and d features. Let Xs be the subset of d features at
ent categories and a target class C , the χ2 statistic is node S, and Ys be the corresponding response values. Let Xj

86720 VOLUME 12, 2024



I. D. Mienye, N. Jere: Survey of Decision Trees: Concepts, Algorithms, and Applications

be the j-th feature in Xs. Then, the algorithm can be defined G. GRADIENT BOOSTED DECISION TREES
as: Gradient Boosted Decision Trees (GBDT) is an ensemble

1) For each feature Xj in Xs, calculate the p-value of a learning method that combines multiple decision trees to
statistical test for the null hypothesis that there is no create a powerful predictive model [57]. Unlike Random
relationship between Xj and Ys. Forest, which builds independent trees in parallel, GBDT uses

2) Choose the feature Xk and split point tk that maximize a sequential approach to build trees that correct the errors
the statistical significance, based on the p-values of the of the previous trees [58], [59]. It uses gradient descent to
tests. minimize errors. Assuming T is the number of trees, ht (x) is

3) Split the node into two child nodes S1 and S2, where the prediction of the t-th tree, Ft−1(x) is the current model’s
S1 contains examples with Xk ≤ tk and S2 contains predictions for x, and L(y,Ft−1(x)) is the loss function, the
examples with Xk > tk . GBDT algorithm works as follows:

4) Recursively repeat steps 1-3 to every child node until a 1) Initialize the model with a constant value (e.g., the
stopping criterion is reached. mean of the target variable).

2) For t = 1 to T :
F. RANDOM FOREST a) Compute the negative gradient of the loss
the random forest, described in Algorithm 4, is an ensemble function with respect to the current model’s
of decision trees [54], [55]. It improves upon the basic predictions for each instance in the training data.
decision tree algorithm by reducing overfitting. Each tree in b) Fit a decision tree to the negative gradient values,
the forest is built from a sample drawn with replacement using the input data as features and the negative
(i.e., bootstrap sample) from the input data [56]. The basic gradient values as target variables.
idea behind this algorithm is to generate a set of trees c) Update the model by adding the new tree,
using different subsets of the input samples and features and weighted by a learning rate η, to the current
then combine their outputs to obtain a final prediction. The model.
Random Forest algorithm uses twomain techniques to reduce 3) Make a prediction for a new instance by summing the
overfitting and improve accuracy: predictions from the various trees:

• Bootstrap Sampling: By sampling the data with replace- a) For a regression task, the final prediction is the
ment, the algorithm generates multiple training sets sum of the predictions of all the trees, i.e., f (x) is
that are slightly different from each other. This type given by:
of sampling ensures reduced variance and prevents ∑T
overfitting. f (x) = ηht (x) (8)

• Feature Randomization: Randomly selecting a subset of t=1
features for each tree ensures the algorithm decorrelates where η is the learning rate.
the trees and reduces the chance of selecting the same b) For a classification task, the final prediction is
‘‘best’’ feature for every tree. This improves the diversity the probability of the positive class, computed by
and accuracy of the trees. applying a sigmoid function to the sum of the

predictions of all the trees.

Algorithm 4 Random Forest Algorithm f (x) = ∑1T (9)
1 + e− t η

1: for t = 1 to T do ▷ Generate T trees =1 ht (x)

2: Randomly sample n instances from D with replace- where η is the learning rate and e is the Euler’s
ment number.

3: Randomly select m attributes from the total p
attributes (where m ≪ p) H. ROTATION FOREST

4: Build a decision tree ht based on the sampled Rotation forest is a type of decision tree ensemble where each
instances and attributes tree is trained on the principal components of a randomly

5: end for selected subset of features [60], [61]. The core idea behind
6: end for this algorithm is to train each classifier in the ensemble on
7: To make predictions for a new instance x: a version of the training data that has been transformed to
8: if classification task then maintain the correlation between the features and introduce

1 ∑
9: f (x) = argmax T

c T t I {h (x) = } ▷ M jor ty
=1 t c a i diversity among the classifiers. This is achieved through the

vote across trees following steps:
10: else if regress 1) For each classifier to be trained, partition the set of

1 ∑ion task then
11: f (x) T

= T t h ▷ v r g o t e p e
=1 t (x) A e a e f r e r dictions features F into k subsets. The partitioning can be

12: end if random but is done in such a way that each subset
13: end if contains a different part of the features.

VOLUME 12, 2024 86721



I. D. Mienye, N. Jere: Survey of Decision Trees: Concepts, Algorithms, and Applications

TABLE 1. Summary of decision tree algorithms.

2) For each subset of features, apply PCA to obtain the majority vote (for classification tasks) of the predictions from
principal components. This step transforms the original all base classifiers.
feature space into a new space that captures the variance A summary of the different tree-based algorithms is
in the data more effectively. tabulated in Table 1, including their advantages and

3) Combine the principal components from all subsets to disadvantages.
form a new set of features for training the classifier.
This effectively rotates the axis of the feature space, IV. DECISION TREE APPLICATIONS IN RECENT
hence the name Rotation Forest. LITERATURE

4) Train each base classifier on the transformed dataset. Decision trees have gained significant attention in recent
Different classifiers can be used, but decision trees are literature. This section discusses some popular applications
commonly applied. of decision trees in fields such as healthcare and finance.

Given a dataset D with n features, the algorithm par-
titions the feature set F into k non-overlapping subsets A. MEDICAL DIAGNOSIS
F1,F2, . . . ,Fk . For each subset Fi, PCA is applied to derive a Healthcare is one of the prominent areas where decision trees
set of principal components PCi, capturing the main variance have found extensive use. Researchers have utilized decision
directions of the features in Fi. The transformation for a trees to predict disease diagnosis, treatment outcomes, and
subset Fi can be represented as: patient prognosis. Decision trees are effective in identifying

patterns and relationships in medical data, leading to more
Ti = PCA(Fi) (10) accurate diagnoses and personalized treatment plans. For

example, decision trees have been used to predict the
where Ti is the transformation matrix obtained from PCA on likelihood of a patient developing a specific disease based
subset Fi. The new feature set for training the jth classifier,Dj, on their medical history and lifestyle factors [11], [62], [63].
is obtained by applying the transformation Ti to each subset This information can then be used to implement preventive
Fi and concatenating the results: measures and interventions, ultimately improving patient

⊕k outcomes and reducing healthcare costs.
D Pathak and Arul Valan [64] proposed a heart disease
j = Ti(Fi) (11)

⊕ prediction model using a decision tree. The model was
i=1

built using a fuzzy rule-based technique combined with a
where denotes the concatenation of the transformed decision tree, achieving an accuracy of 88% when trained
feature subsets. The ensemble’s final output is typically the on the Cleveland heart disease dataset obtained from the

86722 VOLUME 12, 2024



I. D. Mienye, N. Jere: Survey of Decision Trees: Concepts, Algorithms, and Applications

University of California Irvine (UCI) machine learning 95.6%, respectively, with the XGBoost obtaining the highest
repository. Similarly, Maji and Arora [65] conducted a study accuracy.
on heart disease prediction using a different dataset from Meanwhile, Adler et al. [70] developed a Glaucoma
the UCI machine learning repository. The study employed detectionmethod using the random forest ensemble classifier.
the C4.5 decision tree and a hybrid decision tree made of The study evaluated the performance of ensemble pruning
C4.5 and artificial neural network (ANN), where the former on the imbalanced glaucoma dataset. The ensemble pruning
achieved an accuracy of 76.66% and the latter 78.14%. The techniques include pruning by prediction accuracy (using
study demonstrated the robustness of hybridising decision the Brier Score strategy), pruning by uncertainty-weighted
trees with neural networks. accuracy (UWA), and pruning by diversity (using the Double-

Ahmad et al. [66] studied the performance of several Fault measure). The experimental results indicated that the
algorithms using different heart disease datasets, including RF model reached an area under the receiver operating
Cleveland, Switzerland, and Long Beach. The algorithms characteristic curve (AUC) of 0.98 for the Brier and
studied include random forest, decision tree, support vector double-fault pruning techniques.
machine (SVM), k-nearest neighbor (KNN), linear discrim- Additionally, Mienye et al. [71] employed decision tree,
inant analysis, and gradient boosting classifier. The study SVM, and logistic regression for CKD detection. The
employed sequential feature selection (SFS) to obtain the selected algorithms were also used as the base learners
most significant features, which were then used to train the in the AdaBoost ensemble. The study reported accuracies
models. The study concluded that the random forest-SFS of 94% and 100% for the decision tree and AdaBoost
and decision tree-SFS achieved the best accuracy. For the classifier that used a decision tree as a based learner. The
Cleveland dataset, the random forest and decision tree study demonstrated the robustness of using a decision tree
obtained accuracies of 100. in the AdaBoost over the SVM and logistic regression.

In [67], the authors identified the C4.5 and random forest Furthermore, Mienye and Sun [72] studied the impact of
as potentially robust algorithms for detecting chronic kidney cost-sensitive ML in medical diagnosis using the following
disease (CKD) stages. The study employed a CKD dataset algorithms: decision tree, random forest, and XGBoost.
from the UCI machine learning repository, comprising Cost-sensitive learning involves modifying the algorithm to
25 features and 400 samples. The results indicated that the focus on the minority class samples, thereby enhancing the
C4.5 achieved an accuracy of 85.5%, outperforming the model’s performance on the minority class, which in most
random forest, which achieved an accuracy of 78.25%. applications is of higher importance than the majority class.

Decision tree-based methods have also been employed to When applied for detecting cervical cancer, the cost-sensitive
diagnose COVID-19. Ahmad et al. [66] proposed a deep random forest obtained the highest classification accuracy of
learning-based decision treemodel to detect COVID-19 using 98.8%, outperforming the other cost-sensitive and standard
chest X-ray images. The approach consists of three decision algorithms.
trees trained using deep learning architectures, including Furthermore, Khan et al. [73] proposed an ensemble
a convolutional neural network (CNN). One tree classifies approach called optimal trees ensemble (OTE) and applied
the images as normal or abnormal, another tree detects it to diverse classification problems, including hepatitis
tuberculosis indicators in the abnormal images, and the and Pakinson’s disease detection, achieving error rates of
last detects COVID-19. The approach achieved an average 0.1230 and 0.0861, respectively. The error rates, which
accuracy of 95%. Ghiasi and Zendehboudi [68] proposed a translate to 87.7% and 91.4% accuracy, imply the proposed
decision tree-based ensemble classifier for detecting breast OTE outperformed other baseline models, including KNN,
cancer. The study used the well-known Wisconsin Breast LDA, and random forest. Table 2 summarizes the discussed
Cancer dataset and aimed to build a robust breast cancer studies on medical diagnosis, indicating how decision trees
detection framework using the random forest and extra have been employed in the medical domain, achieving
trees classifier (ET). The approach resulted in an accuracy excellent classification performance.
of 100%.

Mienye and Sun [69] studied the performance of ML
algorithms for heart disease prediction. The study utilized B. FINANCE
the following algorithms: decision tree, XGBoost, ran- Decision trees have also been widely employed in the field
dom forest, logistic regression, and naive Bayes. Firstly, of finance. By analysing historical data and identifying
the authors employed the Synthetic Minority Oversam- relevant variables, decision trees can accurately predict the
pling Technique-Edited Nearest Neighbor (SMOTE-ENN) creditworthiness of individuals. This information is crucial
to resample the data and solve the imbalance class prob- for banks and lending institutions in determining the risk
lem. Also, the recursive feature elimination technique was associated with granting loans [74], [75]. Furthermore,
employed to identify the most significant attributes to decision trees have been used to detect fraudulent activities
further enhance the classification performance of the models. in financial transactions by examining transactional data and
The results showed that the decision tree, random forest, identifying suspicious patterns, helping to prevent financial
and XGBoost achieved an accuracy of 87.7%, 93%, and losses.

VOLUME 12, 2024 86723



I. D. Mienye, N. Jere: Survey of Decision Trees: Concepts, Algorithms, and Applications

TABLE 2. Summary of the medical diagnosis studies.

Yao et al. [76] studied credit risk within an enterprise decision tree, random forest, KNN, logistic regression, and
setting. The study proposed a decision tree-based ensemble naive Bayes classifiers. The aim of the study was to assess
classifier that uses the SMOTE and AdaBoost algorithms. which classifier would achieve the highest performance in
The proposed model was aimed at identifying enterprise terms of accuracy and other metrics. The experimental results
credit risk by incorporating supply chain information. Other indicated that the decision tree and random forest achieved
benchmarkmodels were built using KNN, logistic regression, an accuracy of 92.11% and 94.57%, with the random
SVM, and random forest. The study indicated that the forest outperforming the other classifiers, demonstrating the
proposed decision tree ensemble achieved the best and most robustness of tree-based ensemble classifiers.
stable performance, obtaining an AUC of 0.902. Seera et al. [81] employed a decision tree for credit

Liu et al. [77] developed an approach for financial card fraud detection, using credit card transaction records
institutions to effectively predict credit risk and enhance prof- in Malaysia, obtaining a classification accuracy of 99.96%.
itability. The proposed approach uses the gradient-boosting Rawat et al. [82] studied the performance of four classifiers
decision tree. While the GBDTwas efficient in predicting the on credit credit card fraud detection. The classifiers include
credit risk, it lacked sufficient interpretability. Therefore, the logistic regression, RF, KNN, and AdaBoost. The various
study introduced an enhanced method called tree-based aug- models achieved classification accuracies of 99%. Similarly,
mented GBDT, which uses a step-wise feature augmentation Adhegaonkar et al. [83] employed decision tree, random
framework. The proposed approach achieved a classification forest, logistic regression, and SVM for credit card fraud
accuracy of 93.78%, outperforming the standard GBDT and detection. The experimental results showed that the decision
displaying robust interpretability. tree obtained an accuracy of 84.9%. However, the random

Alam et al. [78] studied the imbalance class problem in forest obtained the best performance with an accuracy of
credit risk prediction. The study employed different credit 85.2%. A summary of the reviewed papers is tabulated in
risk datasets, including the German credit approval dataset, Table 3.
the Taiwan dataset, and the European credit card clients
dataset. The gradient-boosted decision tree model combined
with the k-means SMOTE technique achieved accuracies V. DISCUSSIONS AND FUTURE RESEARCH DIRECTIONS
of 84.6%, 89%, and 87.1% on the German, Taiwan, and Decision trees have proven to be effective in various domains,
European clients datasets, respectively. including healthcare and finance. However, like any other

Hancock and Khoshgoftaar [79] employed gradient- algorithm, decision trees have their limitations and areas for
boosted decision tree-based algorithms for detecting health improvement. In this section, we will explore some potential
insurance fraud. This is an important ML application as future research directions in decision trees that can enhance
healthcare fraud is capable of denying patients the needed their performance and address their limitations.
medical attention. In this study, the authors employed claims Firstly, the handling of missing data is a crucial area of
data to train the various classifiers, including categorical potential improvement for decision trees. Currently, decision
boosting (CatBoost), achieving an AUC of 0.775, outper- trees either ignore instances with missing values or use
forming other ML algorithms. The study went further to surrogate splits to make predictions [86], [87]. However,
demonstrate the model’s performance after introducing a these approaches may not always be optimal and can
new variable called Healthcare provider state, leading to the lead to biased or inaccurate results. Future research could
CatBoost obtaining an AUC of 0.882. focus on developing more sophisticated methods to handle

Wong et al. [80] conducted a comparative study of ML missing data in decision trees, such as advanced imputation
algorithms for credit risk prediction. The study focused on techniques or incorporating uncertainty estimation.

86724 VOLUME 12, 2024



I. D. Mienye, N. Jere: Survey of Decision Trees: Concepts, Algorithms, and Applications

TABLE 3. Summary of the credit risk and fraud detection studies.

Another future research direction will be enhancing the of the decision trees, including their early development to
ability of decision trees to handle high-dimensional data [88], the recent high-performing tree-based ensemble methods.
[89], [90]. Decision trees can struggle when faced with The article covers the main decision tree algorithms, such as
datasets that have a large number of features, as the tree CART, ID3, C4.5, C5.0, CHAID, and conditional inference
structure becomes complex and prone to overfitting. Future trees. Their applications in medical diagnosis, credit risk, and
research could explore techniques to improve the scalability fraud detection were reviewed. This study will be beneficial
and efficiency of decision trees in high-dimensional settings, to ML practitioners and researchers trying to understand
such as feature selectionmethods or dimensionality reduction decision trees and the widely used tree-based algorithms.
techniques.

Furthermore, while decision trees are known for their inter- REFERENCES
pretability compared to other machine learning algorithms, [1] J. G. Richens, C. M. Lee, and S. Johri, ‘‘Improving the accuracy of medical
they can still be difficult to understand and explain, especially diagnosis with causal machine learning,’’ Nature Commun., vol. 11, no. 1,
when they become large and complex. Future research could Aug. 2020, Art. no. 3923.

investigate methods to simplify decision trees and make them [2] G. Obaido, F. J. Agbo, C. Alvarado, and S. S. Oyelere, ‘‘Analysis of
attrition studies within the computer sciences,’’ IEEE Access, vol. 11,

more understandable to non-experts, such as rule extraction pp. 53736–53748, 2023.
algorithms or visualisation techniques. Additionally, decision [3] S. Ahmed, M. M. Alshater, A. E. Ammari, and H. Hammami, ‘‘Artificial
trees are sensitive to outliers and can easily be influenced by intelligence and machine learning in finance: A bibliometric review,’’ Res.

Int. Bus. Finance, vol. 61, Oct. 2022, Art. no. 101646.
noisy data, leading to inaccurate predictions [91]. It might be [4] G. Obaido, B. Ogbuokiri, C. W. Chukwu, F. J. Osaye, O. F. Egbelowo,
worth examining the robustness of decision trees to outliers M. I. Uzochukwu, I. D. Mienye, K. Aruleba, M. Primus, and O. Achilonu,
and noisy data and exploring methods to make decision trees ‘‘An improved ensemble method for predicting hyperchloremia in adults

more robust to outliers and noise, such as outlier detection with diabetic ketoacidosis,’’ IEEE Access, vol. 12, pp. 9536–9549, 2024.
[5] C. Wang, J. Xu, S. Tan, and L. Yin, ‘‘Secure decision tree classification

techniques or robust splitting criteria. with decentralized authorization and access control,’’ Comput. Standards
Lastly, the application of decision trees in emerging Interfaces, vol. 89, Apr. 2024, Art. no. 103818.

fields and domains is a potential future research direction. [6] M. M. Rahman and S. A. Nisher, ‘‘Predicting average localization error
of underwater wireless sensors via decision tree regression and gradient

Decision trees have been extensively studied and applied boosted regression,’’ in Proc. Int. Conf. Inf. Commun. Technol. Develop.
in traditional domains such as healthcare, finance, and Singapore: Springer, 2023, pp. 29–41.
marketing. However, there are numerous emerging fields [7] T. O’Halloran, G. Obaido, B. Otegbade, and I. D. Mienye, ‘‘A deep

where decision trees can potentially make a significant learning approach for maize lethal necrosis and maize streak virus disease
detection,’’Mach. Learn. Appl., vol. 16, Jun. 2024, Art. no. 100556.

impact. For example, decision trees could be applied in [8] R. Rivera-Lopez, J. Canul-Reich, E. Mezura-Montes, and
the field of autonomous vehicles to aid in decision-making M. A. Cruz-Chávez, ‘‘Induction of decision trees as classification models
processes or in the field of natural language processing through metaheuristics,’’ Swarm Evol. Comput., vol. 69, Mar. 2022,

Art. no. 101006.
to improve sentiment analysis and text classification tasks. [9] O. Sagi and L. Rokach, ‘‘Explainable decision forest: Transforming a
Future research could explore the potential applications of decision forest into an interpretable tree,’’ Inf. Fusion, vol. 61, pp. 124–138,
decision trees in these emerging fields and investigate their Sep. 2020.

effectiveness in solving complex problems. [10] L.-A. Dong, X. Ye, and G. Yang, ‘‘Two-stage rule extraction method
based on tree ensemble model for interpretable loan evaluation,’’ Inf. Sci.,
vol. 573, pp. 46–64, Sep. 2021.

[11] D. Che, Q. Liu, K. Rasheed, and X. Tao, ‘‘Decision tree and ensemble
VI. CONCLUSION learning algorithms with their applications in bioinformatics,’’ in Advances
Decision trees have shown great potential and effectiveness in Experimental Medicine and Biology. New York, NY, USA: Springer,

in various fields. Their ability to analyse complex data and 2011, pp. 191–199.
[12] L. Cañete-Sifuentes, R. Monroy, and M. A. Medina-Pérez, ‘‘A review and

identify patterns and relationships makes them valuable in the experimental comparison of multivariate decision trees,’’ IEEE Access,
field of machine learning. This paper presented an overview vol. 9, pp. 110451–110479, 2021.

VOLUME 12, 2024 86725



I. D. Mienye, N. Jere: Survey of Decision Trees: Concepts, Algorithms, and Applications

[13] A. Dhull and G. Gupta, ‘‘A self explanatory review of decision tree [37] S. J. Oh, B. Schiele, and M. Fritz, ‘‘Towards reverse-engineering black-
classifiers,’’ in Proc. Int. Conf. Recent Adv. Innov. Eng. (ICRAIE), box neural networks,’’ in Explainable AI: Interpreting, Explaining and
May 2014, pp. 1–7. Visualizing Deep Learning (Lecture Notes in Computer Science), vol.

[14] V. G. Costa and C. E. Pedreira, ‘‘Recent advances in decision trees: 11700, W. Samek, G. Montavon, A. Vedaldi, L. Hansen, and K. R. Müller,
An updated survey,’’ Artif. Intell. Rev., vol. 56, no. 5, pp. 4765–4800, Eds. Cham, Switzerland: Springer, 2019, pp. 121–144, doi: 10.1007/978-
May 2023. 3-030-28954-6_7.

[15] C. Gupta and A. Ramdas, ‘‘Distribution-free calibration guarantees [38] E. Zihni, V. I. Madai, M. Livne, I. Galinovic, A. A. Khalil, J. B. Fiebach,
for histogram binning without sample splitting,’’ in Proc. Int. Conf. and D. Frey, ‘‘Opening the black box of artificial intelligence for clinical
Mach. Learn., 2021, pp. 3942–3952. decision support: A study predicting stroke outcome,’’ PLoS ONE, vol. 15,

[16] F. Mazurek, A. Tschand, Y. Wang, M. Pajic, and D. Sorin, ‘‘Rigorous no. 4, Apr. 2020, Art. no. e0231166.
evaluation of computer processors with statistical model checking,’’ in [39] C. Strobl, A.-L. Boulesteix, T. Kneib, T. Augustin, and A. Zeileis,
Proc. 56th Annu. IEEE/ACM Int. Symp. Microarchitecture, Oct. 2023, ‘‘Conditional variable importance for random forests,’’BMCBioinf., vol. 9,
pp. 1242–1254. no. 1, pp. 1–11, Dec. 2008.

[17] L. Breiman, ‘‘Bagging predictors,’’ Mach. Learn., vol. 24, no. 2, [40] S. M. F. D. S. Mustapha, ‘‘Predictive analysis of students’ learning
pp. 123–140, Aug. 1996. performance using data mining techniques: A comparative study of feature

[18] J. R. Quinlan, ‘‘Induction of decision trees,’’ Mach. Learn., vol. 1, no. 1, selection methods,’’ Appl. Syst. Innov., vol. 6, no. 5, p. 86, Sep. 2023.
pp. 81–106, Mar. 1986. [41] S. Ben Jabeur, N. Stef, and P. Carmona, ‘‘Bankruptcy prediction using

[19] J. R. Quinlan, C4.5: Programs for Machine Learning. Amsterdam, the XGBoost algorithm and variable importance feature engineering,’’
The Netherlands: Elsevier, 2014. Comput. Econ., vol. 61, no. 2, pp. 715–741, Feb. 2023.

[20] I. D. Mienye, Y. Sun, and Z. Wang, ‘‘Prediction performance of [42] J. R. Quinlan. (2004). Data Mining Tools See5 and C5.0. [Online].
improved decision tree-based algorithms: A review,’’Proc.Manuf., vol. 35, Available: http://www.rulequest.com/see5-info.html
pp. 698–703, Jan. 2019. [43] L. Breiman, Classification and Regression Trees. Evanston, IL, USA:

[21] S. Piramuthu, ‘‘Input data for decision trees,’’ Expert Syst. Appl., vol. 34, Routledge, 2017.
no. 2, pp. 1220–1226, Feb. 2008. [44] M.-M. Chen and M.-C. Chen, ‘‘Modeling road accident severity with

[22] S. Hwang, H. G. Yeo, and J.-S. Hong, ‘‘A new splitting criterion for better comparisons of logistic regression, decision tree and random forest,’’
interpretable trees,’’ IEEE Access, vol. 8, pp. 62762–62774, 2020. Information, vol. 11, no. 5, p. 270, May 2020.

[23] J.-S. Hong, J. Lee, and M. K. Sim, ‘‘Concise rule induction algorithm [45] D.-H. Lee, S.-H. Kim, and K.-J. Kim, ‘‘Multistage MR-CART: Mul-
based on one-sided maximum decision tree approach,’’ Expert Syst. Appl., tiresponse optimization in a multistage process using a classification
vol. 237, Mar. 2024, Art. no. 121365. and regression tree method,’’ Comput. Ind. Eng., vol. 159, Sep. 2021,

[24] D. Bertsimas and J. Dunn, ‘‘Optimal classification trees,’’ Mach. Learn., Art. no. 107513.
vol. 106, no. 7, pp. 1039–1082, Jul. 2017. [46] E. Belli and S. Vantini, ‘‘Measure inducing classification and regression

[25] L. Rutkowski, M. Jaworski, L. Pietruczuk, and P. Duda, ‘‘The CART trees for functional data,’’ Stat. Anal. Data Mining, ASA Data Sci. J.,
decision tree for mining data streams,’’ Inf. Sci., vol. 266, pp. 1–15, vol. 15, no. 5, pp. 553–569, Oct. 2022.
May 2014. [47] H. Ishwaran, ‘‘The effect of splitting on random forests,’’ Mach. Learn.,

[26] C. J. Mantas, J. Abellán, and J. G. Castellano, ‘‘Analysis of credal-C4.5 for vol. 99, no. 1, pp. 75–118, Apr. 2015.
classification in noisy domains,’’ Expert Syst. Appl., vol. 61, pp. 314–326, [48] G. V. Kass, ‘‘An exploratory technique for investigating large quantities
Nov. 2016. of categorical data,’’ J. Roy. Stat. Soc. C, Appl. Statist., vol. 29, no. 2,

[27] G. S. Reddy and S. Chittineni, ‘‘Entropy based C4.5-SHO algorithm with pp. 119–127, 1980.
information gain optimization in data mining,’’ PeerJ Comput. Sci., vol. 7, [49] S. Kushiro, S. Fukui, A. Inui, D. Kobayashi, M. Saita, and T. Naito,
p. e424, Apr. 2021. ‘‘Clinical prediction rule for bacterial arthritis: Chi-squared automatic

[28] N. Peker and C. Kubat, ‘‘Application of chi-square discretization algo- interaction detector decision tree analysis model,’’ SAGE Open Med.,
rithms to ensemble classification methods,’’ Expert Syst. Appl., vol. 185, vol. 11, Jan. 2023, Art. no. 205031212311609.
Dec. 2021, Art. no. 115540. [50] H. Prasetyono, A. Abdillah, T. Anita, A. Nurfarkhana, and A. Sefudin,

[29] L. A. Badulescu, ‘‘A chi-square based splitting criterion better for the ‘‘Identification of the decline in learning outcomes in statistics courses
decision tree algorithms,’’ in Proc. 25th Int. Conf. Syst. Theory, Control using the chi-squared automatic interaction detection method,’’ J. Phys.,
Comput. (ICSTCC), Oct. 2021, pp. 530–534. Conf. Ser., vol. 1490, no. 1, Mar. 2020, Art. no. 012072.

[30] F. Mahan, M. Mohammadzad, S. M. Rozekhani, and W. Pedrycz, [51] T. Hothorn, K. Hornik, and A. Zeileis, ‘‘Unbiased recursive partitioning:
‘‘Chi-MFlexDT: Chi-square-based multi flexible fuzzy decision tree for A conditional inference framework,’’ J. Comput. Graph. Statist., vol. 15,
data stream classification,’’ Appl. Soft Comput., vol. 105, Jul. 2021, no. 3, pp. 651–674, Sep. 2006.
Art. no. 107301. [52] N. Levshina, ‘‘Conditional inference trees and random forests,’’ in A Prac-

[31] F. M. J. M. Shamrat, S. Chakraborty, M. M. Billah, P. Das, J. N. Muna, tical Handbook of Corpus Linguistics. Cham, Switzerland: Springer, 2020,
and R. Ranjan, ‘‘A comprehensive study on pre-pruning and post-pruning pp. 611–643.
methods of decision tree classification algorithm,’’ in Proc. 5th Int. Conf. [53] B. Schivinski, ‘‘Eliciting brand-related social media engagement: A
Trends Electron. Informat. (ICOEI), Jun. 2021, pp. 1339–1345. conditional inference tree framework,’’ J. Bus. Res., vol. 130, pp. 594–602,

[32] Y. Manzali and Pr. M. E. Far, ‘‘A new decision tree pre-pruning method Jun. 2021.
based on nodes probabilities,’’ in Proc. Int. Conf. Intell. Syst. Comput. Vis. [54] N. Younas, A. Ali, H. Hina, M. Hamraz, Z. Khan, and S. Aldahmani,
(ISCV), May 2022, pp. 1–5. ‘‘Optimal causal decision trees ensemble for improved prediction and

[33] S. Trabelsi, Z. Elouedi, and K. Mellouli, ‘‘Pruning belief decision tree causal inference,’’ IEEE Access, vol. 10, pp. 13000–13011, 2022.
methods in averaging and conjunctive approaches,’’ Int. J. Approx. [55] Z. Khan, A. Gul, O.Mahmoud,M.Miftahuddin, A. Perperoglou,W. Adler,
Reasoning, vol. 46, no. 3, pp. 568–595, Dec. 2007. and B. Lausen, ‘‘An ensemble of optimal trees for class membership

[34] T. Lazebnik and S. Bunimovich-Mendrazitsky, ‘‘Decision tree post- probability estimation,’’ in Analysis of Large and Complex Data. Cham,
pruning without loss of accuracy using the SAT-PP algorithm with an Switzerland: Springer, 2016, pp. 395–409.
empirical evaluation on clinical data,’’ Data Knowl. Eng., vol. 145, [56] I. D. Mienye and Y. Sun, ‘‘A survey of ensemble learning: Con-
May 2023, Art. no. 102173. cepts, algorithms, applications, and prospects,’’ IEEE Access, vol. 10,

[35] E. Frantar and D. Alistarh, ‘‘SparseGPT: Massive language models can pp. 99129–99149, 2022.
be accurately pruned in one-shot,’’ in Proc. 40th Int. Conf. Mach. Learn., [57] Z. Zhang and C. Jung, ‘‘GBDT-MO: Gradient-boosted decision trees for
vol. 202, A. Krause, E. Brunskill, K. Cho, B. Engelhardt, S. Sabato, and multiple outputs,’’ IEEE Trans. Neural Netw. Learn. Syst., vol. 32, no. 7,
J. Scarlett, Eds., Jul. 2023, pp. 10323–10337. pp. 3156–3167, Jul. 2021.

[36] B. Mahbooba, M. Timilsina, R. Sahal, and M. Serrano, ‘‘Explainable [58] M.-J. Jun, ‘‘A comparison of a gradient boosting decision tree, random
artificial intelligence (XAI) to enhance trust management in intrusion forests, and artificial neural networks to model urban land use changes:
detection systems using decision tree model,’’ Complexity, vol. 2021, The case of the Seoul metropolitan area,’’ Int. J. Geographical Inf. Sci.,
pp. 1–11, Jan. 2021. vol. 35, no. 11, pp. 2149–2167, Nov. 2021.

86726 VOLUME 12, 2024



I. D. Mienye, N. Jere: Survey of Decision Trees: Concepts, Algorithms, and Applications

[59] V. A. Dev and M. R. Eden, ‘‘Formation lithology classification using [80] Y. Wang, Y. Zhang, Y. Lu, and X. Yu, ‘‘A comparative assessment of credit
scalable gradient boosted decision trees,’’ Comput. Chem. Eng., vol. 128, risk model based on machine learning—A case study of bank loan data,’’
pp. 392–404, Sep. 2019. Proc. Comput. Sci., vol. 174, pp. 141–149, Jan. 2020.

[60] S. Demir and E. K. Sahin, ‘‘Comparison of tree-based machine learning [81] M. Seera, C. P. Lim, A. Kumar, L. Dhamotharan, and K. H. Tan,
algorithms for predicting liquefaction potential using canonical correlation ‘‘An intelligent payment card fraud detection system,’’ Ann. Oper. Res.,
forest, rotation forest, and random forest based on CPT data,’’ Soil Dyn. vol. 334, nos. 1–3, pp. 445–467, Mar. 2024.
Earthq. Eng., vol. 154, Mar. 2022, Art. no. 107130. [82] A. Rawat, S. S. Aswal, S. Gupta, A. P. Singh, S. P. Singh, and K. C. Purohit,

[61] E. K. Sahin, I. Colkesen, and T. Kavzoglu, ‘‘A comparative assessment ‘‘Performance analysis of algorithms for credit card fraud detection,’’ in
of canonical correlation forest, random forest, rotation forest and logistic Proc. 2nd Int. Conf. Disruptive Technol. (ICDT), Mar. 2024, pp. 567–570.
regression methods for landslide susceptibility mapping,’’ Geocarto Int., [83] V. R. Adhegaonkar, A. R. Thakur, and N. Varghese, ‘‘Advancing credit card
vol. 35, no. 4, pp. 341–363, Mar. 2020. fraud detection through explainable machine learning methods,’’ in Proc.

[62] F. L. Seixas, B. Zadrozny, J. Laks, A. Conci, and D. C. Muchaluat Saade, 2nd Int. Conf. Intell. Data Commun. Technol. Internet Things (IDCIoT),
‘‘A Bayesian network decision model for supporting the diagnosis of Jan. 2024, pp. 792–796.
dementia, Alzheimer’s disease and mild cognitive impairment,’’ Comput. [84] A. H. Nadim, I. M. Sayem, A. Mutsuddy, andM. S. Chowdhury, ‘‘Analysis
Biol. Med., vol. 51, pp. 140–158, Aug. 2014. of machine learning techniques for credit card fraud detection,’’ in Proc.

[63] G. Obaido, B. Ogbuokiri, I. D. Mienye, and S. M. Kasongo, ‘‘A voting Int. Conf. Mach. Learn. Data Eng. (iCMLDE), Dec. 2019, pp. 42–47.
classifier for mortality prediction post-thoracic surgery,’’ inProc. Int. Conf. [85] S.Makki, Z. Assaghir, Y. Taher, R. Haque,M.-S. Hacid, andH. Zeineddine,
Intell. Syst. Design Appl.Cham, Switzerland: Springer, 2022, pp. 263–272. ‘‘An experimental study with imbalanced classification approaches for

[64] A. K. Pathak and J. A. Valan, ‘‘A predictive model for heart disease credit card fraud detection,’’ IEEE Access, vol. 7, pp. 93010–93022, 2019.
diagnosis using fuzzy logic and decision tree,’’ in Smart Computing [86] S. Nijman, A. Leeuwenberg, I. Beekers, I. Verkouter, J. Jacobs, M. Bots,
Paradigms: New Progresses and Challenges (Advances in Intelligent F. Asselbergs, K. Moons, and T. Debray, ‘‘Missing data is poorly handled
Systems and Computing). Singapore: Springer, 2019, pp. 131–140. and reported in prediction model studies using machine learning: A

[65] S. Maji and S. Arora, ‘‘Decision tree algorithms for prediction of heart literature review,’’ J. Clin. Epidemiol., vol. 142, pp. 218–229, Feb. 2022.
disease,’’ in Information and Communication Technology for Competitive [87] R. V.McCarthy,M.M.McCarthy,W. Ceccucci, and L. Halawi, ‘‘Predictive
Strategies. Singapore: Springer, Aug. 2018, pp. 447–454. models using decision trees,’’ in Applying Predictive Analytics. Cham,

[66] G. N. Ahmad, S. Ullah, A. Algethami, H. Fatima, and S. Md. H. Akhter, Switzerland: Springer, 2019, pp. 123–144.
‘‘Comparative study of optimummedical diagnosis of human heart disease [88] A. Mhasawade, G. Rawal, P. Roje, R. Raut, and A. Devkar, ‘‘Comparative
using machine learning technique with and without sequential feature study of SVM, KNN and decision tree for diabetic retinopathy detection,’’
selection,’’ IEEE Access, vol. 10, pp. 23808–23828, 2022. in Proc. Int. Conf. Comput. Intell. Sustain. Eng. Solutions (CISES),

[67] H. Ilyas, S. Ali, M. Ponum, O. Hasan, M. T. Mahmood, M. Iftikhar, Apr. 2023, pp. 166–170.
and M. H. Malik, ‘‘Chronic kidney disease diagnosis using decision tree [89] T. Wang, R. Gault, and D. Greer, ‘‘Cutting down high dimensional data
algorithms,’’ BMC Nephrology, vol. 22, no. 1, Dec. 2021, Art. no. 273. with fuzzy weighted forests (FWF),’’ in Proc. IEEE Int. Conf. Fuzzy Syst.

[68] M. M. Ghiasi and S. Zendehboudi, ‘‘Application of decision tree-based (FUZZ-IEEE), Jul. 2022, pp. 1–8.
ensemble learning in the classification of breast cancer,’’ Comput. Biol. [90] Z. Azam, M. M. Islam, and M. N. Huda, ‘‘Comparative analysis of
Med., vol. 128, Jan. 2021, Art. no. 104089. intrusion detection systems and machine learning-based model analysis

[69] I. D. Mienye and Y. Sun, ‘‘Effective feature selection for improved through decision tree,’’ IEEE Access, vol. 11, pp. 80348–80391, 2023.
prediction of heart disease,’’ in Pan-African Artificial Intelligence and [91] Y. Xia, ‘‘A novel reject inference model using outlier detection and
Smart Systems, T. M. N. Ngatched and I. Woungang, Eds. Cham, gradient boosting technique in peer-to-peer lending,’’ IEEE Access, vol. 7,
Switzerland: Springer, 2022, pp. 94–107. pp. 92893–92907, 2019.

[70] O. Gefeller, A. Gul, F. Horn, Z. Khan, B. Lausen, andW. Adler, ‘‘Ensemble
pruning for glaucoma detection in an unbalanced data set,’’ Methods Inf.
Med., vol. 55, no. 6, pp. 557–563, 2016.

[71] I. D. Mienye, G. Obaido, K. Aruleba, and O. A. Dada, ‘‘Enhanced
prediction of chronic kidney disease using feature selection and boosted
classifiers,’’ in Proc. Int. Conf. Intell. Syst. Design Appl. Cham, IBOMOIYE DOMOR MIENYE (Member, IEEE)
Switzerland: Springer, 2021, pp. 527–537. received the B.Eng. degree in electrical and

[72] I. D. Mienye and Y. Sun, ‘‘Performance analysis of cost-sensitive learning electronic engineering and the M.Sc. degree (cum
methods with application to imbalanced medical data,’’ Informat. Med.
Unlocked, vol. 25, Jan. 2021, Art. no. 100690. laude) in computer systems engineering from the

[73] Z. Khan, A. Gul, A. Perperoglou, M.Miftahuddin, O.Mahmoud,W. Adler, University of East London, in 2012 and 2014,
and B. Lausen, ‘‘Ensemble of optimal trees, random forest and random respectively, and the Ph.D. degree in electrical
projection ensemble classification,’’ Adv. Data Anal. Classification, and electronic engineering from the University of
vol. 14, no. 1, pp. 97–116, Mar. 2020. Johannesburg, South Africa. His research interests

[74] V. García, A. I. Marqués, and J. S. Sánchez, ‘‘Exploring the synergetic include machine learning and deep learning for
effects of sample types on the performance of ensembles for credit risk finance and healthcare applications.
and corporate bankruptcy prediction,’’ Inf. Fusion, vol. 47, pp. 88–101,
May 2019.

[75] N. Arora and P. D. Kaur, ‘‘A bolasso based consistent feature selection
enabled random forest classification algorithm: An application to credit
risk assessment,’’ Appl. Soft Comput., vol. 86, Jan. 2020, Art. no. 105936.

[76] G. Yao, X. Hu, T. Zhou, and Y. Zhang, ‘‘Enterprise credit risk prediction NOBERT JERE received the M.Sc. and Ph.D.
using supply chain information: A decision tree ensemble model based on
the differential sampling rate, synthetic minority oversampling technique degrees in computer science from the University of
and AdaBoost,’’ Expert Syst., vol. 39, no. 6, Jul. 2022, Art. no. e12953. Fort Hare, South Africa, in 2009 and 2013, respec-

[77] W. Liu, H. Fan, and M. Xia, ‘‘Credit scoring based on tree-enhanced tively. He is currently an Associate Professor
gradient boosting decision trees,’’ Expert Syst. Appl., vol. 189, Mar. 2022, with the Department of Information Technology,
Art. no. 116034. Walter Sisulu University, South Africa. He has

[78] T. M. Alam, K. Shaukat, I. A. Hameed, S. Luo, M. U. Sarwar, S. Shabbir, authored or coauthored numerous peer-reviewed
J. Li, and M. Khushi, ‘‘An investigation of credit card default prediction in journal articles and conference proceedings. His
the imbalanced datasets,’’ IEEE Access, vol. 8, pp. 201173–201198, 2020. main research interest include ICT for sustainable

[79] J. T. Hancock and T. M. Khoshgoftaar, ‘‘Gradient boosted decision tree development. He serves as a reviewer for numer-
algorithms formedicare fraud detection,’’ Social Netw. Comput. Sci., vol. 2, ous reputable journals. He has chaired/co-chaired international conferences.
no. 4, Jul. 2021, Art. no. 268.

VOLUME 12, 2024 86727