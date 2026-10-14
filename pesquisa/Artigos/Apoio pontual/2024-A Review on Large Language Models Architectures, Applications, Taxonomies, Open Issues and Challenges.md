---
source_file: "2024-A Review on Large Language Models Architectures, Applications, Taxonomies, Open Issues and Challenges.txt"
original_rel_path: "Trabalhos\Artigos\Apoio pontual\txt\2024-A Review on Large Language Models Architectures, Applications, Taxonomies, Open Issues and Challenges.txt"
category: "Artigos_Apoio_pontual"
extension: ".txt"
sha256: "4d513b61de0aa256b8cb27207b0208f40fa062f37cac19e3177d5ddc502d8a60"
extracted_at: "2026-09-20T00:05:05.592664"
---

﻿Received 14 January 2024, accepted 5 February 2024, date of publication 13 February 2024, date of current version 23 February 2024.
Digital Object Identifier 10.1109/ACCESS.2024.3365742

A Review on Large Language Models:
Architectures, Applications,
Taxonomies, Open Issues
and Challenges
MOHAIMENUL AZAM KHAN RAIAAN 1, MD. SADDAM HOSSAIN MUKTA 2,
KANIZ FATEMA 3, NUR MOHAMMAD FAHAD1, SADMAN SAKIB 1,
MOST MARUFATUL JANNAT MIM 1, JUBAER AHMAD1, MOHAMMED EUNUS ALI 4,
AND SAMI AZAM 3
1Department of Computer Science and Engineering, United International University, Dhaka 1212, Bangladesh
2LUT School of Engineering Sciences, Lappeenranta-Lahti University of Technology, 53850 Lappeenranta, Finland
3Faculty of Science and Technology, Charles Darwin University, Casuarina, NT 0909, Australia
4Department of CSE, Bangladesh University of Engineering and Technology (BUET), Dhaka 1000, Bangladesh

Corresponding author: Md. Saddam Hossain Mukta (Saddam.Mukta@lut.fi)

ABSTRACT Large Language Models (LLMs) recently demonstrated extraordinary capability in various
natural language processing (NLP) tasks including language translation, text generation, question answering,
etc. Moreover, LLMs are new and essential part of computerized language processing, having the ability to
understand complex verbal patterns and generate coherent and appropriate replies in a given context. Though
this success of LLMs has prompted a substantial increase in research contributions, rapid growth has made it
difficult to understand the overall impact of these improvements. Since a plethora of research on LLMs have
been appeared within a short time, it is quite impossible to track all of these and get an overview of the current
state of research in this area. Consequently, the research community would benefit from a short but thorough
review of the recent changes in this area. This article thoroughly overviews LLMs, including their history,
architectures, transformers, resources, training methods, applications, impacts, challenges, etc. This paper
begins by discussing the fundamental concepts of LLMs with its traditional pipeline of the LLMs training
phase. Then the paper provides an overview of the existing works, the history of LLMs, their evolution
over time, the architecture of transformers in LLMs, the different resources of LLMs, and the different
training methods that have been used to train them. The paper also demonstrates the datasets utilized in the
studies. After that, the paper discusses the wide range of applications of LLMs, including biomedical and
healthcare, education, social, business, and agriculture. The study also illustrates how LLMs create an impact
on society and shape the future of AI and how they can be used to solve real-world problems. Finally, the
paper also explores open issues and challenges to deploy LLMs in real-world scenario. Our review paper
aims to help practitioners, researchers, and experts thoroughly understand the evolution of LLMs, pre-trained
architectures, applications, challenges, and future goals.

INDEX TERMS Large language models (LLM), natural language processing (NLP), artificial intelligence,
transformer, pre-trained models, taxonomy, application.

I. INTRODUCTION make diverse use of it throughout our lifetime [1], [2].
Language is a vital tool for human expression and com- Nevertheless, machines are unable to possess the innate
munication which we begin to learn after our birth and ability to understand and speak in human language without

the help of sophisticated artificial intelligence (AI) [3].
The associate editor coordinating the review of this manuscript and Therefore, a long-standing scientific challenge and aim

approving it for publication was Bo Pu . has been to achieve human-like reading, writing, and


 2024 The Authors. This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.
VOLUME 12, 2024 For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/ 26839



M. A. K. Raiaan et al.: Review on Large Language Models

FIGURE 1. Pipeline of the LLMs training phase.

communication skills in machines [4]. Advances in deep The pipeline of the basic LLMs architecture is shown
learning approaches, the availability of immense computer in Figure 1. LLMs architecture receives text data from
resources, and the availability of vast quantities of training multiple sources and then the architecture forwards text to
data all contributed to the emergence of large language the subsequent stage for preprocessing. It then completes its
models (LLMs). LLMs are category of language models that training process by executing a series of stages, including
utilizes neural networks containing billions of parameters, random parameter initialization, numerical data input, loss
trained on enormous quantities of unlabeled text data using function calculation, parameter optimization, and iterative
a self-supervised learning approach [5]. Frequently pre- training. They offer text translation, text summarization,
training on large corpora from the web, these models sentiment analysis, and other services following the training
may learn complicated patterns, language subtleties, and phase. Prior research has shown the potential of LLMs
semantic linkages. However, LLMs have proved their ability in many NLP tasks, including specialized applications in
in various language-related tasks, including text synthesis, domains such as the medical and health sciences [11] and
translation, summarization, question-answering, and senti- politics [12]. Moreover, after inventing the most sophisticated
ment analysis, by leveraging deep learning techniques and GPT model [13], developing the state-of-the-art models
large datasets.Moreover, fine-tuning thesemodels on specific (LLaMa and Bard [14]), and exploring their capabilities, such
downstream tasks has been quite promising, with state- as Alpaca and GPTHuggingface [15], LLM has become a
of-the-art performance in several benchmarks [6]. LLMs crucial and effective domain. As a result, a trustworthy assess-
have their roots in the early development of language ment of current LLMs research is becoming increasingly
models and neural networks. Statistical approaches and important, and prior research has shown the potential and
n-gram models were used in earlier attempts to develop superiority of LLMs in NLP tasks. Despite this, only a few
language models [7]; but these models have shortcomings studies [3], [16], [17] have thoroughly reviewed latest LLMs
in expressing long-term interdependence and context in developments, possibilities, and limitations in their research.
language. After that, researchers began to explore more Besides, researchers have presented various aspects of
complex ways with the development of neural networks the LLMs domain in several studies [3], [16], [17], [18];
and the availability of larger datasets. The creation of but their work still has several limitations. These studies
the Recurrent Neural Network (RNN) [8], which allowed miss many aspects of LLM including high-level architecture
for the modeling of sequential data, including language, and configurations, taxonomies, API and domain-specific
was a crucial milestone. However, RNNs were limited in applications, and datasets of LLMs. For example, there
their efficacy due to vanishing gradients and long-term is a lack of introduction to the core architecture and
dependencies. The significant advancement in LLMs systems configurations of the LLMs model, a lack of adequate
occurred when the transformer architecture was introduced in explanation of the taxonomy of LLMs, differentiation based
the seminal work [9]. The transformer model is built around on ML, domain-specific applications, API applications, and
the self-attention mechanism, enabling parallelization and descriptions of LLMs datasets. Furthermore, the vastmajority
efficient handling of long-range dependencies. Furthermore, of LLMs review papers are not peer-reviewed works. The
LLM architectures served as the basis for models such absence of these key points in a review indicates that a
as Google’s Bidirectional Encoder Representations from thorough investigation is missing in the current literature.
Transformers (BERT) [10] and open AI’s Generative Pre- Due to the significant extent of the constraints, it is possible
trained Transformer (GPT) series, which excelled at various to mitigate these research gaps by thoroughly analyzing and
language tasks. addressing these missing points. Thus, the motivation of

26840 VOLUME 12, 2024



M. A. K. Raiaan et al.: Review on Large Language Models

FIGURE 2. Section organization of the review.

this paper is to comprehensively explore the current review • Defining insights into the potential of LLMs and their
papers, identify their limitations, and outline the current impact on society and demonstrating bio-medical appli-
state-of-the-art methods to address these vital challenges. cations in five practical domains, including bio-medical
Therefore, our primary objective is to explore, comprehend, and healthcare, education, social media, business, and
and evaluate LLMs that encompass domains, evolution, agriculture.
classification, the structure of pre-trained models, resources, • Investigating LLMs’s diverse set of open issues, chal-
and real-time applications. Additionally, our comprehensive lenges, and future opportunities. This section focuses on
review discusses open issues and challenges associated with identifying key challenges and future opportunities that
LLMs, including security, ethical, privacy, economic, and can aid in advancing knowledge in this area.
environmental considerations. In addition, we present a set The remaining sections of the paper are organized as
of guidelines to explore future research and development depicted in Figure 2. In Section II, the literature review is dis-
in the effective use of LLMs. We hope that this study will cussed. Section III illustrates the history of LLMs; Section IV
contribute to a better understanding and use of LLMs. The demonstrates the Methodology; Section V explains the clear
list of contributions to this paper is as follows: concept of large language models; Section VI describes the

• Providing a complete overview of LLMs, including their resources of LLMs; Section VII demonstrates the domain-
evolution, classification, and transformer architecture. specific applications of LLMs; and Section VIII explains
The history of LLMs provides a brief account of the the societal impact of LLMs, Indusrial significance of
evaluation from its origins (1940) to the present (2023), LLMs is highlighted in Section IX, Section X discuss the
as well as a taxonomy of LLMs based on pre-trained and open issues and challenges regarding LLMs, Section XI
API-based models and major LLMs structures. discusses about the future research directions of LLMs,

• Describing the comparison of different pre-trained Section XII acknowledges the limitation and Section XIII
model designs in LLMs, along with their own systems finally concludes the paper.
that show how the model architectures are different.

• Explaining the influence of ML models on LLMs, II. LITERATURE REVIEW
demonstrating the significance of ML in various LLMs The growing number of LLMs is an extraordinary develop-
domains. ment in the field of AI. In recent years, numerous studies [3],

• Providing a brief overview of the datasets used in the [16], [17], [18] have been conducted to investigate and
training phase to differentiate between the models in evaluate their capabilities. Researchers from various fields
existing works. have contributed on the rise of LLMs, shedding light on

• Presenting a thorough explanation of the hardware their remarkable advancements, diverse applications, and
implementation in training and testing models in terms potential to revolutionize tasks from text generation and com-
of LLMs. prehension to demonstrating reasoning skills. Collectively,

VOLUME 12, 2024 26841



M. A. K. Raiaan et al.: Review on Large Language Models

TABLE 1. Comparison between state-of-the-art research.

these studies contribute to our comprehension of LLMs’ NLP tasks, and applications in disciplines such as medicine,
significant role in shaping the landscape of AI-driven engineering, social sciences, and the humanities. In addition
language processing and problem-solving. to highlighting the dynamic and rapidly changing nature of

Huang et al., [18] presented a study on reasoning in LLMs research, the study offers insights into their current
LLMs that comprehensively summarizes the current state of status, impact, and potential in the context of scientific
LLMs’ reasoning capabilities. It examines various aspects of and technological advancements. Chang et al. [17] focuses
reasoning in LLMs, such as techniques to enhance and extract on the assessment of LMMs. Their research examines the
reasoning abilities, methodologies and criteria for assessing increasing prevalence of LLMs in academia and industry
these abilities, insights from prior research, and suggestions due to their exceptional performance in various applica-
for future directions. The primary concern is the extent to tions. The study highlights the growing significance of
which LLMs can demonstrate reasoning skills. This paper evaluating LLMs at both the task and societal levels in
aims to provide an in-depth and up-to-date examination of order to comprehend potential risks. The paper thoroughly
this topic, fostering fruitful discussions and guiding future analyzes LLMs evaluationmethods, focusing on three critical
research in LLMs-based reasoning. In another study, Zhao dimensions: what to evaluate, where to evaluate, and how
et al., [3] survey on LLMs illustrates a comprehensive to evaluate. The research also includes tasks such as natural
examination of the evolution and impact of LLMs in the field language processing, reasoning, medical applications, ethics,
of artificial intelligence and natural language processing. and education. The article examines evaluation methods and
It traces the historical journey from early language models benchmarks for assessing LLMs performance, emphasizing
to the recent emergence of pre-trained language models successful and unsuccessful cases. The paper also underlines
(PLMs) with billions of parameters. Notably, the paper future challenges in LLMs evaluation and emphasizes the
discusses LLMs’ unique capabilities as they scale in size, importance of evaluating LLMs as a fundamental discipline
including in-context learning. The authors highlight the to support the development of more competent LLMs.
significant contributions of LLMs to the AI community and Table 1 illustrates the comparison between different review
the launch of ChatGPT, a prominent AI chatbot powered papers based on some fundamental properties such as LLMs
by LLMs. The survey is structured around four key aspects models, APIs, datasets, domain specific LLMs, ml-based
of LLMs: pre-training, adaptation tuning, utilization, and comparison of LLMs, taxonomy, architectures, performance,
capacity evaluation. Additionally, the paper provides insights hardware specifications for testing and training, and config-
into available resources for LLMs development and identifies urations. Huang et al. [18] lack information on LLMs’ API,
further research and development areas. dataset, domain-specific LLMs, taxonomy, architectures, and

A recent study by Fan et al. [16] conducted a bibliometric LLMsConfigurations. In contrast, Zhao et al., [3] hasmissing
review of LLMs research from 2017 to 2023, encompass- aspects on LLMs’ API, domain-specific LLMs, taxonomy,
ing over 5,000 publications. The study aims to provide architecture, and configurations.Moreover, Fan et al. [16] and
researchers, practitioners, and policymakers with an overview Chang et al., [17] lack information on LLMs’ API, domain-
of the evolving landscape of LLMs research. The study specific LLMs, taxonomy, architecture, and configurations.
also tracks research trends during the specified time period, On the contrary, our paper offers a considerably broader
including advancements in fundamental algorithms, major aspects on the LLMs context. In addition to incorporating

26842 VOLUME 12, 2024



M. A. K. Raiaan et al.: Review on Large Language Models

every aspect specified in the table, we provide a detailed language assignments. The models were predominantly
demonstration on the account of the hardware implemen- employed for tasks involving binary classification. However,
tation and LLMs datasets. Previous research frequently their efficacy in dealing with the complex situation in NLP
focuses on limited aspects of LLMs, including historical tasks was limited [24].
development, bibliometric patterns, and assessment tech- Statistics-based models of language were created in the
niques. However, our study recovers previous shortcomings. ’80s and ’90s. These models belong to a category of
A thorough examination is conducted on each of these models utilized in the field of NLP and machine learning
aspects, resulting in a comprehensive representation of (ML) with the purpose of capturing and quantifying the
the strengths and weaknesses of LLMs. Furthermore, our statistical patterns and correlations within language data [21].
research is focused on the crucial element of reasoning Statistical language models have significance in several
capabilities in LLMs, thereby providing a significant addition applications, such as predictive text input, text generation,
to the body of knowledge in the field. By giving thorough speech recognition, spam detection, etc. These models were
information, such as descriptions of datasets and hardware superior in terms of accuracy to early neural networks and
implementations required, our paper stands out as a primary rule-basedmodels, as they were able to process large amounts
resource for LLMs practitioners and researchers. Further- of data with ease [21]. Although statistical language models
more, we briefly discuss open issues in LLMs research, have been successful in many applications of NLP, they
such as ethical and responsible AI, multimodal integration, still have limitation when these models come to predict the
energy efficiency, privacy and data protection, generalization semantic relationship between concepts and context of the
and few-shot learning, and cross-lingual and low-resource language. These techniques have difficulty dealing with long-
settings. We also highlight key challenges, including data range dependencies [25].
complexity and scaling, tokenization sensitivity, computa- During the mid-2000s, the field of NLP witnessed the
tional resource demands, fine-tuning complexity, real-time introduction of word embeddings, which were recognized as
responsiveness, contextual constraints, bias and undesirable a notable breakthrough and subsequently acquired consider-
output, knowledge temporality, and evaluation complexity. able attention [26]. Word embedding refers to the process
Our review suggests future research directions to tackle of representing words in a continuous vector space. The
open issues and important resource for LLMs researchers approach captures the semantic relationships among words
and practitioners. Our extensive systematic review presents by representing them in a vector space. The representation
a detailed discussion on LLMs which makes a substantial reduces the computational cost by mapping the words to a
contribution to the field of LLMs research. lower-dimensional space. Word2Vec and GloVe are widely

recognized word embedding models in the domain [27].
III. HISTORY OF LARGE LANGUAGE MODELS These models are mostly utilized for assessing word sim-
LLMs refer to a category of AI models developed specifically ilarity and assisting in the clustering and representation of
to comprehend and produce human language [19]. LLMs words within semantic domains. Although not classified as
have significantly contributed to the field of AI and LLMs, these embeddings have significantly contributed to
have been applied in diverse areas, including education, the progress of natural language comprehension and have set
communication, content generation, article composition, the path for the development of more complex models. Nev-
healthcare, research, entertainment, and information dissem- ertheless, these models have several limitations, such as their
ination, among others [19], [20]. The origins of LLMs can difficulty in effectively dealing with words that have multiple
be attributed to the emergence and advancement of neural meanings (i.e., homonyms) or words that sound the same
network-based methodologies in the field of NLP [20]. (i.e., homophones), as well as their inability to comprehend
In order to process language, early NLP systems utilized contextual information in an accepted manner [26].
rule-based techniques and statistical models. However, those The introduction of neural language models in the mid-
methods frequently encountered difficulties in comprehend- 2010s marked a significant advancement in LLMs [28].
ing the textual context in a specific discourse [21]. This These models employed deep learning approaches to acquire
section provides a high-level overview of LLMs, including knowledge of language patterns from extensive textual
their background, development, training, and operation. data and additionally utilized artificial neural networks to
Figure 3 depicts the history of language models. comprehend, produce, or forecast human language. Fur-
In the 1940s, Warren McCulloch and Walter Pitts intro- thermore, they have demonstrated exceptional outcomes in

duced the idea of artificial neural networks (ANNs) [22]. a wide range of language-related tasks. The initial neural
Afterwards, the 1950s and 1960s saw the development of language model to be introduced was the recurrent neural
the first language models [23]. These models included early network language model (RNNLM) in 2010 [29]. The
neural networks as well as rule-based models. The processing purpose of its development was to capture the sequential
of language was facilitated by their utilization of precisely dependencies present in textual data. The utilization of a
established linguistic rules and features [24]. These models hidden state allows for the retention and propagation of
experienced limitations in their abilities and encountered information from preceding words in a particular sequence.
difficulties in managing the complexities of complicated RNNLM has been employed in several applications such

VOLUME 12, 2024 26843



M. A. K. Raiaan et al.: Review on Large Language Models

FIGURE 3. Brief history of language models.

as text production, speech recognition, machine translation, models employ a self-attention mechanism that enables them
and language modeling. The RNNLM demonstrated the to assess the relative significance of individual words in a
capability to effectively capture the contextual information of sentence, thereby encoding complex relationships within the
words, resulting in the generation of text that exhibits a higher text [34]. The primary objective behind the development
degree of naturalness compared to earlier models. Although of the Transformer model was to overcome the inherent
the RNNLM offers certain advantages, it is not without its constraints observed in earlier models such as RNNs and
drawbacks. Some of these limitations include a limited short- Long Short-Term Memory (LSTM) networks. The Trans-
term memory capacity, extended training time requirements, former models possess notable advantages in comparison
and prone to suffer in overfitting [30]. to other models due to their ability to capture longer-term
In the year 2015, Google unveiled the initial large neural dependencies in language and facilitate concurrent training

language model that employed deep learning methodologies. on many Graphical Processing Units (GPUs) with a vast
The technologywas referred to as theGoogleNeuralMachine number of parameters, enabling the construction of much
Translation (GNMT) model [31]. The model underwent larger models [35]. Parallelization capabilities and scalability
training using huge quantities of multilingual textual data. are further benefits that have resulted in notable progress
This development signifies a notable progression in the field across many NLP activities [33].
of machine translation [32]. The model demonstrated excep- The introduction of BERT in 2018 byGoogle AI represents
tional performance on machine translation tasks, departing a noteworthy advancement in the domain of NLP [16].
from traditional rule-based and statistical techniques in favor The underlying framework utilized in this study was the
of neural network-based methodologies. When compared transformer architecture. Before the introduction of BERT,
to earlier language models, it was able to tackle complex the preceding language model rooted in NLP had constraints
natural language tasks with ease. The utilization of this in understanding contextual information due to its reliance on
model resulted in enhanced translation accuracy and the unidirectional language modeling. BERT was introduced by
generation of meaningful translations, while also mitigating Google as a solution to address this particular constraint [36].
errors associated with intricate linguistic constructions [31]. The employed methodology involved the utilization of deep
The advancement of Language models persisted with the bidirectional representations, which were conditioned on

emergence of the Transformer model in the year 2017 [33]. both the left and right contexts across all layers [37]. The
The transformer model has had a significant impact on pre-trained BERT model was able to undergo fine-tuning by
the field of NLP and has played a crucial role in the incorporating an additional output layer, hence enabling its
development of language models such as Bidirectional applicability to diverse tasks such as question answering and
Encoder Representations from Transformers (BERT) and language inference. Due to the widespread adoption of BERT,
Generative Pre-trained Transformers (GPT) [34]. These several versions and subsequent models, such as RoBERTa,

26844 VOLUME 12, 2024



M. A. K. Raiaan et al.: Review on Large Language Models

T5, and DistilBERT, have been developed to effectively Megatron-LM has certain limitations, primarily due to
address diverse tasks across multiple domains [37]. its substantial dimensions, which necessitate substantial
Following the advent of transformers, subsequent years computational resources for both the training and inference

saw the development of scaling-up LLMsmodels through the processes [43].
expansion of training data and parameter counts [20]. OpenAI In the year 2020, OpenAI introduced GPT-3 as the
significantly contributed to the development of LLMs in successor to GPT-2 [40]. GPT-3 was trained on an extensive
2018. During the same year, GPT, an additional transformer- collection of textual data and demonstrated the ability to
based architecture, was developed. Multiple iterations of generate text that exhibited a high degree of coherence
the GPT models, developed by OpenAI, underwent pre- and naturalness. Similar to GPT-1 and GPT-2, this model
training using extensive datasets comprising excerpts from also utilizes the Transformer architecture [20]. The potential
the Internet, novels, and various other textual sources [38]. of LLMs for various NLP applications was exemplified
The first version of the GPT model was referred to as GPT- by GPT-3. This particular LLMs was trained on a deep
1 [39]. The introduction of GPT-1 was a notable progression neural network with an enormous 175 billion parameters,
in the field of NLP. GPT-1 effectively produces words that surpassing the size of any other LLMs available at that
are contextually appropriate, showcasing the transformative particular time [16]. The ability to produce natural language
capabilities of transformers in significantly advancing natural text of superior quality with less fine-tuning is facilitated
language processing tasks. This proficiency is attributed by sophisticated methodologies, including a more significant
to its extensive training on a vast number of parameters, number of layers and a wider range of training data. One of
specifically 117 million. The model underwent a two-step the most essential characteristics of GPT-3 is its capacity to
procedure consisting of unsupervised pre-training followed engage in few-shot and zero-shot learning, hence mitigating
by supervised fine-tuning [20]. The initial iteration of GPT the necessity for extensive data in order to generate natural
did not attain the same level of popularity as BERT due to language text of superior quality. The advent of GPT-3 has
several inherent limitations [40]. These drawbacks include a catapulted the domain of natural language processing to new
restricted context window, absence of bi-directionality, and heights [40]
occasional generation of biased content. Despite the inherent In the year 2020, OpenAI introduced GPT-4, the sub-
limits of GPT-1, this model played a crucial role in paving sequent version of their language model, following the
the way for later, more advanced models. As a result, it has achievements of GPT-3 [20]. Similar to its predecessor,
sparked a new era of AI research and intensified competition GPT-4 is a transformer-based model. The system has the
in the development of LLMs. capability to analyze both textual and visual data to produce

The subsequent version of the GPT series, known as textual outputs [16]. The performance of the system was
GPT-2, was designed with the purpose of addressing the assessed using a range of standardized professional and
limitations observed in its predecessor, GPT-1 [40]. Similar academic examinations specifically intended for human test-
to GPT-1, GPT-2 was developed utilizing the transformer takers. GPT-4 exhibited a level of performance comparable to
architecture. In the year 2019, Alec Radford introduced that of humans on themajority of examinations. Significantly,
GPT-2, a language model that was developed on a deep it achieved a ranking inside the highest decile of participants
neural network consisting of 1.5 billion parameters [41]. on a simulated iteration of the UniformBar Examination [44].
The GPT-2 model includes a transformer design, which GPT-4 has greater dimension and efficacy compared to
incorporates self-attention processes to extract information its predecessor, GPT-3, as it possesses the capacity to
from different positions within the input sequence. Despite generate text that is even more comprehensive and exhibits
the high computing cost associated with training and a heightened level of naturalness [20].
executing the model, its substantial magnitude facilitates the The development of large language models presents addi-
comprehension and generation of a wide range of linguistic tional prospects for innovation, knowledge acquisition, and
subtleties and diversified outputs [40]. The GPT-2 model has experimentation across diverse domains such as healthcare,
played a pivotal function in the advancement of LLMs and education, research, etc. The utilization of AI and NLP in
the execution of NLP activities. The influence of GPT-2 has these models has significantly transformed how we engage
had a significant impact on successor models like GPT-3 and people with machines.
GPT-4, leading to additional advancements in the field of
language processing and creation [42]. IV. METHODOLOGY
In 2019, NVIDIA produced Megatron-LM, which is an Preferred Reporting Items for Systematic Reviews and

LLMs [43]. Similar to GPT, this model is built on the Meta-Analyses (PRISMA) guide is crucial for drafting
transformer architecture. The model possesses a total of review papers as it assists systematic reviews in conducting
8.3 billion parameters, a notably bigger quantity compared to transparent meta-analyses, accurately reporting aims and
the parameter count of GPT-1 andGPT-2 [16]. Themagnitude concluding the study, and ensuring the adequate reliability
of this dimension facilitates the model’s capacity to acquire and relevance with the findings of the study [45]. Therefore,
and produce intricate linguistic structures. Nevertheless, this review work focuses on the adoption of PRISMA

VOLUME 12, 2024 26845



M. A. K. Raiaan et al.: Review on Large Language Models

TABLE 2. Electronic database search.

TABLE 3. Search queries used for the review paper.

FIGURE 4. PRISMA flow diagram of the review.

technique in analyzing the design, configurations, applica-
tions, and challenges of LLMs.

A. INITIAL SEARCHING Inclusion Criteria (IC) and Exclusion Criteria (EC). The
The research materials employed in this study have been inclusion criteria define the standards of the paper that need
acquired from recognized scientific journals and conferences to be included, while the exclusion criteria eliminate articles
from January 2020 to August 2023, conducted through the that do not meet the inclusion scope. Thus, this manual
Google Scholar platform. A comprehensive selection of screening process improves the transparency of selection
scholarly research articles has been specified, encompassing process. Table 4 presents the inclusion and exclusion criteria
various reputable academic sources such as IEEE Xplore, set for the proposed study.
ScienceDirect, ACM Digital Library, Wiley Online Library,
Springer Link, MDPI, and patents. Initially, 355 papers were D. PRISMA DIAGRAM
selected based on their relevance to the topic and keyword. Figure 4 depicts the PRISMA flow diagram utilized in
Table 2 describes the identification technique of the materials selecting papers for the study. It also provides the numbers
from various electronic sources. of included and excluded papers for better understanding.

The diagram begins by identifying articles from electronic
B. SEARCHING QUERY AND KEYWORDS databases using keywords, queries, resulting in 355 papers.
Using the combination of the appropriate search queries After applying the screening method to exclude duplicated,
and keywords enlisted in Table 3 helps to perform a proper low-quality, and irrelevant journal papers, the total number
literature search. To conduct a thorough search of the of papers for review is reduced to 294. Following a thorough
articles for our LLMs-based review work, we encompass the analysis of the titles and abstracts, a total of 207 papers were
following terms: ‘‘LLMs AND machine learning OR deep selected. The final screening method involves the application
learning OR models,’’ ‘‘LLMs AND machine learning OR of inclusion and exclusion criteria. Following this process,
deep learning OR API,’’ ‘‘LLMs AND machine learning OR a total of 135 papers were ultimately selected for the final
deep learning OR Dataset’’, ‘‘LLMs AND natural language review. The process begins with an extensive collection of
processing OR NLP’’ and ‘‘LLMs AND machine learning papers and reduces to the final selection that meets the pre-
OR deep learning OR tools.’’ These specific searching defined selection criteria for the systematic review.
techniques help to extract the eligible and quality research
papers. V. LARGE LANGUAGE MODELS

Large language models (LLMs) refer to a specific type of
C. INCLUSION AND EXCLUSION CRITERIA SET AI algorithm that holds the capability to execute a diverse
To acquire the final research papers, PRISMA protocols range of NLP tasks. The most common tasks entail text
and principles were adhered to formulate a standard set of generation, text analysis, translation, sentiment analysis,

26846 VOLUME 12, 2024



M. A. K. Raiaan et al.: Review on Large Language Models

TABLE 4. Inclusion and exclusion criteria. as WordPiece, UnigramLM, and Byte Pair Encoding (BPE).
This algorithm has distinct technique for tokenizing from the
input and then, applied for the specific tasks [47], [48], [49].

2) ATTENTION MECHANISM
The attention mechanisms used in LLMs is a crucial topic
hence it contributes in the improvement of the architecture
and performance. This mechanism helps to figure out the
representation of input sequences by forming links between
various tokens. There are several attention mechanism
available namely Self-Attention where all the queries and
values come from the same encoder-decoder block. Then,
Full Attention which is the naive understanding version of
self attention, and finally, when the output of encoder block
is used as the query of immediate decoder block, is called as
cross attention mechanism [9], [50].

question answering, and other related functions. GPT-3,
GPT-4, PaLM, and LaMDA are extensively used transformer- 3) ACTIVATION FUNCTION
based LLMs models trained on a large amount of textual The activation functions play a vital role in the curve-fitting
data. In terms of architectural properties, these models show capacities of LLMs architectures [51]. Several activation
variations in size and depth. For example, GPT-3 generates functions, such as ReLU, GeLU, and other GLU variations,
parameters of 175 billion, distributed across 96 levels, while are explored to determine their performance in current
PaLM has an even larger parameter number of 540 billion, research on LLMs [52], [53].
organized across 106 layers. All of these models have distinct
configurations. The configurations of GPT-3 and PaLM 4) NORMALIZATION LAYER
differ in terms of their techniques for generating output. Layer normalization is essential for achieving faster conver-
LLMs have evaluated several datasets withinWikipedia, code gence in LLMs model and emphasizes their effects on stabil-
repositories, books, question sets, and socialmedia data. They ity during training sessions. It presents different approaches,
have demonstrated their ability to execute diverse activities such as LayerNorm, DeepNorm, and RMSNorm. These
successfully. Consequently, LLMs have drawn significant layer normalization techniques offer distinct advantages and
attention for their effective contribution in different domains, contribute to the regularization of LLMs applications like
including education, healthcare, media marketing, and other

GPT-3, BERT, T5, etc., facilitating effective training [54].
customer services. A particular LLMs program has superior
performance in a specific domain compared to others, such 5) TRAINING METHODS AND FRAMEWORKS
as GPT-3, which has gained recognition for its proficiency in

LLMs training has different distributed methodologies,
generating text styles, whereas LaMDA demonstrates supe-

including data parallelism, pipeline parallelism, tensor par-
rior performance in providing accurate responses to factual

allelism, model parallelism, and optimizer parallelism [43],
inquiries. LLMs are an emerging technological innovation
that holds the potential to bring about transformative changes [55]. These techniques contribute to understand the practical

across various sectors. and expandable training. Additionally, different libraries and
frameworks, including Transformers, DeepSpeed, PyTorch,
TensorFlow, MXNet, and MindSpore, are used frequently for

A. BACKGROUND OF LARGE LANGUAGE MODELS their training and further implementation [55].
In this section, we present the essential aspects associated.
LLM research requires a comprehensive explanation of the 6) DATA PREPROCESSING
crucial concept. Various vital aspects, such as tokenization, The approaches used to preprocess data focus on the
encoding technique, layer normalization, etc., are encom- significance of quality filtering, data de-duplication and
passed in the following background section. privacy reduction in preparing training data for LLMs.

The filtering technique helps to reduce low quality and
1) TOKENIZATION relevant data. Besides, it reduces the compute complexity
The primary emphasis is on tokenization, a crucial prepro- by ignoring the useless pattern of the input. Duplicate
cessing stage of LLMs that involves parsing text into discrete samples are removed using de-duplication technique which
parts referred to as tokens [46]. Characters, subwords, also avoids the overfitting tendency of the model. Finally,
symbols, or words may serve as tokens, contingent upon privacy reduction ensures the security and compliance
the language model’s dimensions and nature [47], [48]. of data and upholds the preservation of the personal
Various tokenization algorithms are utilized in LLMs, such data.

VOLUME 12, 2024 26847



M. A. K. Raiaan et al.: Review on Large Language Models

FIGURE 5. Background of LLMs.

7) PARAMETER TUNING sequence. As a result, it has become the go-to architecture
The researchers explore the many stages of adaptation for in many fields, often replacing sophisticated recurrent or
LLMs, starting from pre-training and progressing to fine- convolutional neural networks with much more efficient
tuning for subsequent tasks. These approaches serve as a structure [59]. In this regard, it is particularly important for
guide for customizing models to suit specific applications. LLMs applications. Figure 6 illustrates the architecture of
Several model adaptation and parameter-efficient tuning the transformer model. Transformer architecture consists of
techniques, such as prefix tuning, prompt tuning, and adapter seven main components. A demonstration of each component
tuning, provide strategies for achieving effective fine-tuning is shown below.
while minimizing resource usage [56], [57], [58].

This background part aims to provide a thorough under- • Inputs and Input Embeddings
standing of the underlying concepts and approaches that The ML models utilize tokens, which are units of
form the basis of Language Models, which are constantly text like words or sub words, as the training data.
developing. However, these models process numbers. Tokenization

The transformer is employed in most advanced LLMs as begins this translation process by dividing down input
the basic building block because its architecture, scalability, text into meaningful components. A unique number
and pretraining approach enable the model as optimal identification is assigned to each token, connecting
framework for constructing robust LLMs. In addition, the the linguistic information to the numerical vector. This
self-attention mechanism of transformers performs effec- numerical format is known as ‘‘input embeddings.’’
tively for capturing and representing long-range relationships These input embeddings are numerical representations
in language. Consequently, Transformer-based LLMs have of words, which ML models may subsequently process.
significantly improved the state-of-the-art achievement in These embeddings function similarly to a dictionary,
NLP related tasks. In the section V-A1, a comprehensive assisting the model in understanding the meaning of
overview of transformer architectures, configurations are words by arranging them in a mathematical space where
provided for building a high-scalable, optimized and cost- comparable phrases are situated close together. The
efficient LLMs. Figure 5 depicts the visualization of the model is trained to generate these embeddings so that
LLMs background. vectors of the same size represent words with similar

meanings. Figure 6A illustrates the input and input
embeddings.

8) WHAT IS TRANSFORMER? • Positional Encoding
Transformer architecture is considered as the basic building The sequence of words in a sentence frequently
block of LLMs. It is intended for neural networks to conveys important semantic information. The same
efficiently handle sequential data [9]. This architecture does set of words in a different order conveys completely
not use iteration methods. Instead, it employs a focused (i.e., different meanings. In this regard, understanding the
attention based) approach to determine global input-output word order in a sentence is essential in NLP to identify
dependencies. The model can take input of varying lengths the correct utterance meaning. In general, in terms of
and can change its focus depending on the length of the neural networks, they do not perceive the order of inputs.

26848 VOLUME 12, 2024



M. A. K. Raiaan et al.: Review on Large Language Models

FIGURE 6. Architecture of a Transformer model.

To address the problem, positional encoding is used to • Output Embeddings
encode the position of each word in the input sequence Input embeddings, which contain text are not directly
as a collection of integers. The transformer model uses recognized by the model. Therefore, the output must
integer, input embedding and positional encoding to help be converted to a format known as ‘‘output embed-
GPT in understanding sentence word order and provide ding.’’ Similar to input embeddings, output embeddings
grammatically accurate and semantically appropriate undergo positional encoding, enabling the model to
output [60]. The positional encoding part is shown in understand the order of words in a sentence [62].
Figure 6B. In machine learning, the loss function evaluates the

• Encoder The encoder is a crucial component of the difference between a model’s prediction and the objec-
neural network which is responsible for processing the tive value. Loss functions are essential for complex
input text. Its primary function is to generate a series of GPT language models. The loss function modifies a
hidden states that represent the input text in ameaningful portion of the model to increase accuracy by reducing
way [61]. Then, it uses a series of self-attention layers the discrepancy between predictions and targets. The
that are often referred to metaphorically as ‘‘voodoo change improves the overall performance of the model.
magic,’’ emphasizing their complex and powerful ability The loss function is calculated during training, and
to capture relationships between different elements in the model parameters are modified. In the inference
the input text. In the transformer, the encoder is used process, the output text is created by mapping the
in more than one layer. This section is depicted in predicted probability of each token in the model to
Figure 6C comprehensively. the corresponding token in the vocabulary. The output

• Outputs (shifted right) During the training process, embedding part is illustrated in Figure 6E.
the decoder in the transformer model learns to predict • Decoder
the next word in a sequence by analyzing the preceding The decoder processes both positionally encoded input
words. This is achieved through a mechanism known as and output embeddings. Positional encoding is crucial
autoregressive training. The decoder’s ability to predict for the model to understand the sequential order of
the next word is critical for generating coherent and the tokens in both the input and output sequences.
contextually relevant sequences. Additionally, the GPT The positional information helps the decoder effec-
(GPT-3) is also trained on a massive amount of text tively capture the structure within the sequences. The
data, that helps it to generate sense while writing any decoder has an attention mechanism that helps to
content. Besides, several corpus including the Common improve the output’s quality by leveraging contextual
Crawl web corpus, the BooksCorpus dataset, and the information received from the encoder. The primary
English Wikipedia are also used during the common function of the decoder is to create output sequences
issue. Figure 6D highlights the transformer’s outputs based on the encoded input sequences. It generates
(shifted right) module. a sequence of tokens, often representing words or

VOLUME 12, 2024 26849



M. A. K. Raiaan et al.: Review on Large Language Models

TABLE 5. Hardware specifications for the LLMs model.

sub-words, as its output. The dependency between the the hardware specifications, number of parameters, training
encoder-decoder in a transformer is significant where duration and other configurations of individual LLMs
the encoder processes the input sequence based on model.
the representation, the decoder provides the desired GPT-3: GPT-3 uses Nvidia A100 GPUs to pre-train on
output sequence. In addition, GPT is a decoder-only a large 300 billion token set, generating around 175 billion
transformer [63]. The decoder part of GPT uses a parameters [65]. GPT-3 has context learning features which
masked self-attention mechanism which can process enables itself to understand the words reasoning, sentence,
the input sequence without requiring encoder explicitly. and language properly.
Figure 6F demonstrates the decoder component of a BERT: Trained on an unspecified data scale, the BERT
transformer. model has a variable number of parameters that depends

• Linear Layer and Softmax on batch size and the corresponding model’s hidden layer
The linear layer is a fully connected neural network numbers which is around 340 million. Nvidia A100 and
layer that transforms the output embedding into a higher- V100 GPUs are used for training, and the length of the
dimensional space. This step is required to convert training depends on the scale of the model’s parameters [66].
the output embedding into the original input space. Contextual learning is incorporated in the model also.
This transformation enhances the expressiveness of the RoBERTa: RoBERTa, an enhanced version of BERT
representation, allowing the model to capture more which has a parameter count of 340 million and conducts pre-
complex patterns and relationships in the data. Besides, training on a specific amount of data. The training process
the softmax function generates a probability distribution completed on 6144 TPU v4 units, running for around a
for each output token in the developed vocabulary, duration of twoweeks [67]. Themodel also contains a context
allowing us to generate probabilistic output tokens [64]. learning feature.
Figure 6G shows the process by which the features T5: T5 uses 1024 TPU v3 units and has a number of
are propagated through a linear layer, followed by the 11 billion parameters. T5 has been pre-trained over a number
activation of the accurate output probability using the of tokens of 1 trillion [68]. There is no information available
softmax activation function. on GPU training time. It also holds the features of contextual

learning which provides a satisfactory result.
B. HARDWARE SPECIFICATIONS FOR LARGE LANGUAGE PaLM: PaLM produces a substantial number of parame-
MODELS ters, around 540 billion, and it manages the pre-training on
Understanding the computing resources and training dura- a large dataset with a tokens of 780 billion. The pre-training
tions needed for various language models is crucial. This process is carried out utilizing by 6144 TPU v4 units [69].
estimation helps us in decision-making when choosing a The training period extends for 120 days, and the model also
model for specific tasks. To choose amodel that is appropriate incorporates contextual learning.
for a given task, a clear understanding of the training times LaMDA: LaMDA uses 1024 TPU v3 units during the
and computational resources is mandatory. Table 5 shows training and the model is pre-trained over 768 billion tokens

26850 VOLUME 12, 2024



M. A. K. Raiaan et al.: Review on Large Language Models

which generates a total of 137 billion parameters [70]. employing 2048 Ascend 910 processing units [81]. It has
It requires a total of of 57.7 days during training. an impressive parameter count of 207 billion. No details

GLM-130B: GLM-130B model possesses a total of regarding the duration of GPU training.
130 billion parameters and undergoes pre-training on a huge Our comprehensive description helps to understand the
amount of dataset with 400 billion tokens. The training was hardware specifications and the computational complexity of
conducted utilizing 1024 TPU v4 units and the training each model. The researchers also find an opportunity to know
session lasts for 60 days [71]. about the implementation details of these models and can

Gopher: Gopher is a language model that has been pre- improve the performance of their studies.
trained over 300 billion tokens and required 4096 TPU
v3 for the experiment. It has a total of 280 billion C. DEEP NEURAL NETWORK ARCHITECTURES OF LLMS
parameters [72]. The GPU training period is precisely stated LLMs usually employe deep neural networks to understand
as 920 hours. Furthermore, the model integrates context and generate new content more accurately. In this section,
learning to demonstrate an effective outcome. we include a summary of various DNN architectures used in

Jurassic-1: Jurassic is a model with an impressive capacity different LLMs based on literature studies and different real
of 178 billion parameters. It has been pre-trained on amassive world applications.
dataset of 300 billion tokens, utilizing the computational
power of 800 GPUs [73]. No information regarding the 1) COMPARISON BETWEEN STATE-OF-THE-ART STUDIES
duration of GPU training is available. An LLM is a dynamic model capable of performing various

MT-NLG: MT-NLG has a huge size of 530 billion tasks, such as creating coherent text and summarizing text.
parameters. It has been trained on a massive dataset of A defining feature of a language model is its ability to
270 billion tokens, utilizing 4480 80GB A100 GPUs [74]. assume the subsequent words from the preceding text. The
No data regarding the duration of GPU training is available. deep neural network (DNN) framework is utilized in LLMs
The model integrates context learning features also. to enhance its performance which is similar to human-like

LLaMA: LLaMA is a language model with an enormous understanding [3], [82]. LLMs use different DNN models in
capacity with a total of 65 billion parameters. It has their architecture to enhance task performance.
undergone pre-training on a large dataset consisting of The transformer architecture serves as the basic building
1.4 trillion tokens. This training process was carried out block of all language models. GPT-1, the initial version of
utilizing 2048 high-performance 80GBA100GPUs [75]. The GPT employs the Transformer decoder architecture [66].
training period is explicitly set to 21 days. In GPT-1 the decoder structure operates independently from

LLaMA 2: LLaMA 2 is equipped with a total of 70 billion the encoder, therefore eliminating the multi-head attention
parameters and has performed pre-training on 2 trillion and layer norm components that are linked to the encoder.
tokens, utilizing 2000 80GB A100 GPUs [76]. The training The pre-trainedGPTmodel consists of 12 transformer blocks,
period is set to 25 days, and the model also contains context- each with a d(model) value of 768 and a total of 110 million
based learning. parameters. GPT-2, the second version of GPT, employs

Falcon: Falcon, equipped with 40 billion parameters, the transformer decoder architecture like GPT-1 [66]. GPT-
undergoes pre-training on a large dataset of 1.3 trillion 2 employs 50,257 BPE tokens and ensures that the masked
tokens [77]. No details regarding the duration of GPU training multi-head component is preceded by the Layer Norm.
and it also have the context learning features. In GPT-2, an additional layer norm is included subsequent

Chinchilla: Chinchilla is a language model that has to the last block. There are four pre-trained GPT-2 models
70 billion parameters and has been pre-trained on 1.4 trillion available, each with a unique quantity of decoder blocks.
tokens [78]. There is no details regarding the duration of GPU The largest model, which has a d(model) value of 1600 and
training. 48 blocks, comprises a total of 1.5 billion model parameters.

OPT: OPT, equipped with 175 billion parameters, con- BERT employs the transformer encoder structure, in contrast
ducts pre-training on 180 billion tokens utilizing 992 A100 to the Transformer decoder structure utilized by GPT-1 and
GPUs with a capacity of 80GB each [79]. No details GPT-2 [83]. Following the final encoder block is composed of
regarding the duration of GPU training. two fully connected output layers separated by a Layer Norm

Galactica: Galactica possesses 120 billion parameters and component. The calculation of the likelihood of each token’s
has undergone pre-training using 106 billion tokens [80]. output depends on both the previous and next tokens, making
Details regarding the duration of GPU training are not given. BERT a bidirectional language model. The smaller variant of

BLOOM: BLOOM has a remarkable capacity of 176 bil- BERT consists of 12 encoder blocks with a model dimension
lion parameters and has undergone pre-training on 366 billion of 768 and a parameter count that is approximately equal to
tokens utilizing 384 80GB A100 GPUs [55]. The training that of GPT. In contrast, the larger variant has 24 encoder
period lasts for 105 days, and the model incorporates blocks with a model dimension of 1024 and 336 million
contextual learning. parameters [66].

PanGU-a: PanGU-a is a language model that has been pre- In contrast to encoder-only models such as BERT and
trained on a massive amount of data, specifically 1.1 billion, decoder-only models like GPT-1 and GPT-2, T5 pre-train

VOLUME 12, 2024 26851



M. A. K. Raiaan et al.: Review on Large Language Models

with generative span corruption and an encoder-decoder decoder for generating captions. The findings of the study
architecture [84]. T5 models have displayed state-of-the-art demonstrate the effectiveness of the proposedmethodology in
performance on a wide variety of NLP tasks, like GLUE utilizing LLMs for audio captioning. The performance of this
and SuperGLUE, and are able to expand up to hundreds of proposed approach outperforms the traditional approaches
billions of parameters. LLaMA normalizes the input for every which are trained from the scratch.
transformer sub-layer rather than the output [75]. To increase In a recent study, Fan et al., [87] discuss the significance
performance, it employs the RMSNorm normalizing function of recommender systems in web applications and the
and the SwiGLU activation function rather than the ReLU. shortcomings of current DNN approaches in predicting user
Single models are utilized by LaMDA to execute multiple preferences. They discuss the capacity of LLMs to tackle the
duties. The model architecture is a decoder-only transformer challenges in a recommender systems.
language model. The Transformer is comprised of 64 layers, Bai et al. [88] developed an end-to-end non-autoregressive
a d(model) value of 8192, gated-GELU as the activation speech recognition model namely LASO (Listen Attentively
function, and relative attention the same as T5 LLMs [70]. and Spell Once) to improve the speed of inference by simul-
AlphaCode employs an encoder-decoder transformer archi- taneously predicting all tokens. The proposed model utilizes
tecture in which input tokens are passed to the encoder, and attention methods to combine decoded speech information
one token is extracted from the decoder until an end-of-code into hidden representations for every token. Moreover, they
token is generated [85]. When contrasting encoder-decoder suggest using cross-modal transfer learning to increase the
architectures with decoder-only architectures, the encoder- performance of the speech-modal LASO model by utilizing
decoder architecture provides the advantage of enabling a text-modal language model to align the semantic meaning
bidirectional description representation and provides addi- of tokens.
tional flexibility by separating the encoder structure from Sun et al., [89] provide a new methodology to predict the
the decoder. It employs an asymmetric architecture with effect of news releases and to minimize potential negative
1536 encoder tokens but only 768 decoder tokens. It makes consequences by automatically forecasting responses in news
use of multi-query attention to lower sampling costs. Cache media. By utilizing an LLM which utilizes a deep neural
update costs andmemory utilization are greatly reducedwhen network, their method creates a belief-centered graph on
all query heads are used but only shared for key and value an existing social network to analyze social dynamics.
heads in each attention block. It employed a SentencePiece The proposed framework shows a satisfactory efficiency in
tokenizer for tokenization, trained on a combination of predicting responses.
CodeContests and GitHub data, with a vocabulary size of Drossos et al., [90] present a technique that enables
8,000 tokens. Through the usage of DNNs, all of these LLMs an RNN to acquire LLMs for sound event detection. The
have demonstrated remarkable performance on various NLP proposed approach adjusts the input of the RNN based on the
tasks like as language understanding and generation. activity of classes in the preceding time step. This proposed

approach is evaluated on three distinct datasets: the TUT-SED
Synthetic 2016, TUT Sound Events 2016, and TUT Sound

2) APPLICATIONS OF LLMS USING VARIOUS DNN MODELS Events 2017 datasets.
Pre-training Transformer models have led to the proposal Chiu et al. [91] present an efficient method called TPBERT
of LLMs with impressive capacities in addressing a variety (based on BERT) for improving the reranking of N-best
of NLP tasks, including question-answering, document hypotheses in automatic recognition of speech. This approach
summarization, and language translation [3]. Due to their uses task-specific topic information to increase the BERT
remarkable abilities in basic tasks of language processing model’s ability to create accurate embeddings of the N-best
and creation, they have completely transformed the fields hypotheses.
of NLP and AI. Various DNN models have been employed Elhafsi et al., [92] propose a monitoring methodology that
in different industries, such as technology, healthcare, and utilizes LLMs to tackle the issue of semantic irregularities in
retail to increase performance. DNNs have made substantial robotic systems. The efficiency of LLMs-based monitoring
progress in improving the capabilities of LLMs [87]. DNN in recognizing semantic abnormalities and aligning with
models, such as convolutional neural networks (CNNs), human thinking is demonstrated through tests on autonomous
recurrent neural networks (RNNs), generative adversarial driving.
networks (GANs), capsule networks (CapsNets), transform- Shen et al., [93] present a self-regulating edge AI
ers, and BERT, have been extensively employed in diverse system that utilizes a deep neural network that can plan
applications of LLMs [94]. Numerous studies [86], [87], automatically, and adjust itself to fulfill the needs of users.
[88], [89], [90], [91], [92], [93] suggest that DNN models The proposed system uses a hierarchical design known as
are utilized in several types of LLMs-based applications to cloud-edge-client, where the primary language model is
increase task efficiency. located in the cloud. By leveraging the robust capabilities

Koizumi et al., [86] introduce an innovative method to of GPT in language comprehension, and code creation, they
address the issue of insufficient training data in audio introduce a methodology that effectively handles edge AI
captioning that utilizes a pre-trained LLMs that uses a models to meet users’ requirements while automatically

26852 VOLUME 12, 2024



M. A. K. Raiaan et al.: Review on Large Language Models

TABLE 6. Comparison of applications of LLMs using various DNN models.

generating new codes for training new models through edge and maximum training context length. GPT-4 considered as
federated learning. one of high performing LLMs with a staggering 1.8 trillion

Table 6 gives a brief overview of these DNN applications- parameters. It is comparatively faster than the prior GPT
oriented studies where they applied LLMs. These studies versions and provide many advanced features. Besides, it has
suggest that employing deep neural networks in language fast response system, generate more accurate output and it
models increases the performance of LLMs-based applica- has reduced the biases presented in the model substantially.
tions in several industries.. GPT-1, despite being lesser with 125 million parameters,

demonstrates the significant development of LLMs over
D. ARCHITECTURAL OVERVIEW OF LARGE LANGUAGE the years. An increased number of parameters in LLMs
MODELS enhances the model’s ability to comprehend intricate patterns
In this subsection, we present a detailed overview on the and produce text that is more contextually appropriate and
architecture of LLMs. Table 7 presents a description and reminiscent of human language. GPT3’s selection of a
architecture of LLMs such as GPT-1, BERT, RoBERta, and modest learning rate of 6 is notable, which highlights the
T5. The table assists researchers in selecting the optimal significance of cautious hyperparameter selection. Models
model for a NLP task. GPT-1, BERT base, and BERT are categorized as Causal decoder (CD), Autoregressive
large contain 12, 12, and 24 layers, respectively, in LLMs. (AR), Encoder-decoder (ED), and Prefix decoder (PD) to
RoBERta is an enhanced variant of BERT, while T5 is illustrate architectural diversity. Activation functions vary,
a decoder and encoder transformer. Diagram illustrating influencing the models’ expressive strength from GeLU in
BERT’s input token processing, context-aware embedding, GPT-3 to SwiGLU in LLaMA and LLaMA-2. All versions
and masked language modeling tasks, where the masked of GPT employ the GeLU as its activation function as it
words are intended to predict the model. T5 demonstrates mitigates the vanishing gradient problem and facilitates the
the sequential layers of the transformer model, including the generation of smoother gradients throughout the training
feedforward neural network, and self-attention. T5 explains process. The utilization of SwiGLU as the activation function
how information flows and structures text. GPT-1 passes data is observed in models such as PaLM and LLaMA versions
input embedding and positional encoding through multiple 1 and 2, as it has gating mechanisms that enhance its ability
transformer layers. to capture intricate correlations within the data. Models like

BERT, OPT, and T5 use ReLU as the activation function. The
Formula of these activation functions are given below [6],

E. COMPARISON BETWEEN CONFIGURATIONS OF LLMS [59]:
Table 8 provides an extensive overview of various LLMs, {
highlighting their configuration details and optimization x, if x ≥ 0
settings. These LLMs have played a crucial role in advancing ReLU (x) = max(0, x) =

natural language understanding and generation tasks, making √ f (x) = (1)
0, if x < 0

them a key research topic in NLP. This analysis compares GeLU (x) = 0.5x(tanh[ 2/π (x + 0.44715x3)]) (2)
and contrasts these LLMs based on critical parameters, SwiGLU (x) = x.Sigmoid(βx).xV (3)
including model size, learning rate, category, activation
function, batch size, bias, number of layers, optimizer, BARD is recognized for its informative response. It fea-
number of attention heads, hidden state size, dropout rate, tures 24 attention heads and facilitates its contextually related

VOLUME 12, 2024 26853



M. A. K. Raiaan et al.: Review on Large Language Models

TABLE 7. Architectural overview of different LLMs.

response. BERT size is identical to BARD of 340M. The rate, batch size, and a dropout value of 0.1, leverages the
key advantage of BERT is understanding the context of convergence of the model, and contributes to the NLP-
words. It has effective training settings with a proper learning based tasks precisely. PanGU BLOOM, Galactica, and

26854 VOLUME 12, 2024



M. A. K. Raiaan et al.: Review on Large Language Models

TABLE 8. Various LLMs with configuration details and optimization settings (Here, LR = learning rate, CG = Category, AF = the activation function, bs =

batch size, NL = the number of layers, NAH = the number of attention heads, SHS = the size of the hidden states, MCLDT = the maximum context length
during training, CD = causal decoder, ED = encoder-decoder, PD = prefix decoder, and AR = autoregressive).

[]

Chinchilla are also LLMs but possess distinct configurations biased terms in models, such as Falcon, T5, LLaMA 1,2,
and challenges. Usually, PanGU is highly effective for the and Galactica’s ‘‘No,’’ highlights the complexity of the
Chinese language, whereas Galactica performs well with choices made. From 12 for GPT-1 to 118 for PaLM, the
repeated data. Chinchilla is a scaling strategy constrained by number of layers affects a model’s ability to capture intricate
data limitations and creates efficient resource allocation for patterns. Optimizers are also diverse, with Adam, AdamW,
training and generating output. Falcon and T5 are compact andAdaFactor playing crucial roles. All GPT variants employ
compared to other LLMs, and both are transformer-based Adam as the optimizer, although models such as Galactica,
models. However, they have some unique differences, such OPT, and Falcon utilize AdamW as their optimizer. Both
as Falcon is a decoder-based model whereas T5 integrated T5 and PaLM models utilize the Adafactor optimizer in
both encoder-decoders. Additionally, Falcon utilizes multi- their respective architectures. These variations highlight the
head query attention to increase the scalability of the model. significance of selecting models and configurations that are
LLaMA-2 is the updated version of LLaMA. It is an enhanced tailored to particular tasks, with performance, computational
fine-tuned version that exploits the hardware utilization resources, and task requirements playing a central role.
for efficient training sessions. MT-NLG and PaLM have The number of attention heads also exhibits variation
substantial parameter sizes of 530B and 540B, respectively. across different models. GPT-1 is equipped with a total
Both of them also use the casual decoder technique. However, of 12 attention heads, whilst GPT-4 boasts a much larger
they have some architectural differences, such as PaLM number of attention heads, ranging from 120 to 150 within
uses a SwiGLU activation function and adafactor optimizer. its model. The additional number of attention heads in the
Moreover, it uses a higher learning rate and batch size of LLMs enables the model to concurrently attend to several
1 × 102 and 1000K. On the contrary, MT-NLG uses a lower segments of the input sequence, hence expediting the model’s
learning rate and batch size of 5× 105 and 64K, respectively. training process. In order to enhance the efficacy of the
GLM-130B and LaMDA are also effective LLMs, widely LLMs, researchers employ diverse dimensions for the hidden
used for NLP-based tasks, including question answering, text states within their model. The larger dimensions of the hidden
generation, etc. Both of them use the Gated GLU (GeGLU) state enable the capturing of complex patterns within the
activation function, a GLU variant. The following equation is text. Both GPT 4 and MT-NLG employ hidden state sizes
used to express the GeGLU operation [99]. of approximately 20,000, which is significantly greater in

GEGLU(x,W ,V , b, c) comparison to the hidden state sizes of other LLMs included
= GELU(xW + b) ⊗ (xV + c) (4)

in the table. Certain LLMs models incorporate a dropout
However, there are noticeable differences between GLM- value of 0.1 to prevent overfitting issues, whereas others

130B and LaMDA in terms of their decoder mechanisms. do not employ any dropout value. The maximum context
GLM-130B employs a prefix decoder, whereas LaMDA length denotes the number of tokens that can be remembered
adopts a casual decoder technique. In addition, the GLM- by the model during training. Increasing the size of the
130B model employs a larger batch size compared to the context window boosts the model’s ability to grasp the distant
LaMDA model. In addition, the presence or absence of relationships between the texts. Consequently, the model is

VOLUME 12, 2024 26855



M. A. K. Raiaan et al.: Review on Large Language Models

TABLE 9. Dataset for large language models.

able to generate text outputs with a great coherence. Table 8 categories reflect the richness and diversity of text data used
reports that GPT-4 has the context length of 32768 which is to train LLMs, including web content, novels, news articles,
the maximum among all the LLMs. This substantial length scientific literature, and codes.
number indicates the capability of GPT-4 to remember the From the ✓, we observe that LLaMA has been trained
more extended token sequence during training. LLaMA-2 on a wide range of data sources, with significant exposure
obtained the second-highest context length of 4096. Most to webpages (87%), conversation data (5%), books and
of the models have a context length of 2048, meaning news (2%), scientific data (3%), and codes (5%). Therefore,
they can handle a maximum of 2048 tokens simultaneously LLaMA becomes a versatile model suitable for a wide array
during the text generation. A few compacted models, of NLP tasks that involve these mentioned data sources.
including BARD, BERT, and T5, possess a maximum context In contrast, GPT-3 and AlphaCode have limited data access
length of 512. This table presents a qualitative architectural of data sources to train their models. GPT-1 and GPT-2
comparison among the most popular LLMs. It also provides focus on webpages (70%) and books & news (30%) data to
comprehensive knowledge about the configurations, strength train the model. GPT-3 is proficient with web pages (84%),
of these models. These variations highlight the significance literature, and news (16%) but requires additional instruction
of selecting models for the particular tasks considering the with conversation data, scientific data, and codes. Diverse
performance, computational resources. range of datasets enables the GPT models to generate more

contextual information across various domains. Specifically,
F. COMPARISON BETWEEN DATASETS OF LLMS the Webpages, books, and news datasets help to employ
Different LLMs utilized different datasets for the training formal and structured language. Besides, GPT models
phase, distinguishing the models from one another. A concise achieve the capability of responding in an informative and
overview of the datasets is provided in this section. Moreover, accurate way.
it explicitly exhibits the diverse range of datasets used by AlphaCode, as its name suggests, is solely focused on
the model since understanding of these datasets facilitates codes (100%) and does not utilize any other data sources.
the development and training of the model and boost This feature uniquely distinguish AlphaCode from other
the performance. The datasets used to train various large models and emphasize the significance of this model for
language models (LLMs) and their compatibility with each code-based tasks. Bard, Bert, and Pangu models exhibit
model are detailed in Table 9. identical traits, with each of them concentrating on the

Table 9 demonstrates that datasets have been divided into extensive textual data obtained from webpage contents and
multiple categories: webpages, conversation data, literature, books for pretraining the models. Bloom and OPT primarily
news, scientific data, and codes. This classification enables emphasize on evaluating data from books and websites, such
us to comprehend the variety of data sources that contribute as Wikipedia or other online sources. On the other hand,
to LLMs training. C4, OpenWebText, and Wikipedia are GLM-130 not only analyzes books and web data but also
examples of datasets that belong to the ‘‘Webpages’’ category. incorporates computer code data to provide further techno-
At the same time, BookCorpus, Gutenberg, CC-Stories-R, logical benefits. LaMDA, Galactica and CodeGen models
CC-NEWES, and REALNEWS are examples of datasets use scientific data source for training which advance these
that belong to the ‘‘Books and News’’ category. These models to adapt the scientific knowledge and terminology.

26856 VOLUME 12, 2024



M. A. K. Raiaan et al.: Review on Large Language Models

Hence, these model can lead to a more accurate responses LLMs, including GPT-3.5, BingChat, and BARD. Based
in scientific domains. AlphaCode and GLM-130 are the on the accuracy presented in Table 10, it is evident that
models of choice for code-related tasks, whereas LLaMA BingChat LLM outperforms the other two models, achieving
and BERT excel in diverse text data applications. Most of an accuracy of 92.4%. LLMs such as ChatGPT and Bingwere
the LLMs such as T5, GPT models, Gopher, GLam, PaLM, evaluated using the average intraclass correlation coefficient
and BLOOM frequently utilize websource data which helps (ICC) values. The ICC value for Bing was 0.975, whereas
them to automate various practical tasks such as content ChatGPT has an ICC value of 0.858. The higher mean ICC
creation, data analysis and virtual chatbot for answering the value indicates that Bing exhibited robust performance and
question. On the contrary, some models such as Falcon and consistency in major NLP tasks. Table 10 depicts that, all
different version of GPT models utilize books and news of the LLMs mentioned in the table have been analyzed
data facilitates in educational application such as document and tested on multiple performance metrics and datasets
summarization, and article writings. The models trained on to validate the robustness and reliability of these language
scientific data have several use cases in research domain. models.
In addition, Table 9 provides contextual information of the
datasets to maintain the transparency of the comparison VI. RESOURCES OF LARGE LANGUAGE MODELS
among models and provide an effective guide to future model LLMs have a wide range of potential applications and
implementation. The ‘‘Size’’ and ‘‘Source’’ columns of the resources available for their development, deployment, and
Table listed the additional information. The size of datasets utilization. Figure 7 presents an LLM taxonomy that divided
ranges from 5GB (BookCorpus) to a huge 800GB (several into two main branches: i) pre-trained model-based and ii)
datasets), indicating the sheer magnitude of data required API-based. This taxonomy allows us to explore these two
to train these LLMs. The source information reveals when distinct aspects of LLMs.
and where the data were collected, which is essential for
understanding the temporal relevance of the training data and A. PRETRAINED MODELS
potential biases. Table 9 provides a multitude of information Pretrained language models play a pivotal role in NLP
regarding the datasets used to train LLMs and how each tasks due to their ability to encapsulate broad language
model leverages these datasets. This information is invaluable understanding and generation skills from diverse text sources.
for NLP researchers, developers, and practitioners, as it They offer a substantial advantage by minimizing the
enables them to make informed decisions about which LLMs computational resources and data required for fine-tuning
to use for specific tasks. specific tasks. There are some of the most common

pre-trained LLMs models, which have been depicted in
G. PERFORMANCE ANALYSIS OF LLMS Table 11.
LLMs are models that perform the majority of NLP tasks
and numerous models such as GPT-1 through GPT-4, 1) GENERATIVE PRETRAINED TRANSFORMER (GPT)
Bing, ChatpGPT, and BERT have developed in order to GPT [65] is an influential breakthrough in AI, particularly
contribute jointly to the industry and academia. Since in in NLP tasks. Developed by OpenAI, GPT leverages the
the literature, we find a scarcity of adequate data pertaining transformer architecture and extensive pre-training on vast
to LLMs, we present performance outcomes for diverse internet text data to achieve a deep understanding of human
tasks to publicly accessible LLMs in Table 10. All GPT language. This generative model excels at tasks like text gen-
series, including GPT-1, GPT-2, GPT-3, GPT-3.5, and GPT- eration, translation, question answering, and more, making it
4, are evaluated using a variety of metrics, including the a versatile tool across various NLP domains. GPT’s capacity
Stanford question answering dataset (SQuAD), language to capture intricate language patterns and context, coupled
model benchmark (LAMBADA), and general language with its iterative improvements, has profoundly impacted
understanding evaluation (GLUE), as shown in Table 10. in academia and industry, revolutionizing the landscape of
GPT-1 obtains a score of 68.4 on the GLUE, while GPT- language understanding and generation.
2, GPT-3, GPT-3.5, and GPT-4 attain scores of 84.6, 93.2,
93.5, and 94.4, respectively. GLUE results indicate that 2) BERT
GPT-4 outperforms prior versions of GPT. The GPT-4, i.e., BERT [10], short for ‘‘Bidirectional Encoder Representations
in SQuAD and LAMBDA have scores of 93.6 and 82.4, from Transformers,’’ is a language model with a distinctive
respectively. As shown in the table, GPT-4 outperforms its approach. Unlike previous models, BERT is designed to pre-
predecessors in both LAMBDA and SQuAD. As GPT-4 train deep bidirectional representations from unlabeled text
outperforms its predecessors in all three benchmark metrics by considering both left and right context in all layers. This
and exhibits robust performance, it can be concluded that pre-trained BERT model can be fine-tuned with minimal
GPT-4 is significantly more effective than its predecessors in adjustments to create cutting-edge models for various tasks
tasks involving language understanding and language model- like question answering and language inference, eliminating
ing. The VietNamese High School Graduation Examination the need for extensive task-specific modifications. BERT is
(VNHSGE) English dataset was utilized to analyze various both conceptually straightforward and remarkably effective,

VOLUME 12, 2024 26857



M. A. K. Raiaan et al.: Review on Large Language Models

TABLE 10. Accuracy of various LLMs on different datasets.

FIGURE 7. Taxonomy of LLMs.

achieving state-of-the-art results on different NLP tasks. and significantly improving SQuAD v1.1 question answering
Notable accomplishments include raising the GLUE score to Test F1 to 93.2 (a 1.5 point absolute improvement) and
80.5% (an impressive 7.7% absolute improvement), boosting SQuAD v2.0 Test F1 to 83.1 (a remarkable 5.1 point absolute
MultiNLI accuracy to 86.7% (a 4.6% absolute improvement), improvement).

26858 VOLUME 12, 2024



M. A. K. Raiaan et al.: Review on Large Language Models

TABLE 11. Description of LLMs.

In our analysis, we have considered variants of BERT that the significance of design decisions that were previously
are pre-trained on extensive text corpora and possess the overlooked and prompt inquiries into the origins of recently
characteristics of LLMs, enabling them to understand and reported advancements.
generate natural language comprehensively. This deliberate
choice ensures that the models we have included in our 4) XLNET
study harness the full spectrum of language understanding XLNet [107] represents a versatile autoregressive pretraining
and generation capabilities, thereby aligning with the core approach that achieves bidirectional context learning by
objective of our research in exploring the impact and optimizing expected likelihood across all possible combi-
advancements of LLMs in the field of NLP. Non-LLMs nations. XLNet addresses the constraints of BERT through
versions of BERT or those with significantly reduced its autoregressive design and incorporates insights from
model sizes were excluded from our analysis to maintain Transformer-XL, a leading autoregressive model. In practical
consistency and relevance in our investigation. experiments with consistent conditions, XLNet consistently

surpasses BERT on 20 diverse tasks, frequently by a sub-
3) ROBERTA stantial margin. These tasks encompass question answering,
RoBERTA is another LLM which replicates the BERT natural language inference, sentiment analysis, and document
pre-training approach outlined by Devlin et al. [67]. ranking, among others.
We meticulously assess the influence of various critical
hyperparameters and training data sizes. It’s worth noting 5) SPEECH-XLNET
that BERT was initially trained with room for improvement, Speech-XLNet [108] is a method for training unsupervised
yet it can now perform on par with or even surpass the acoustic models to learn speech representations using a Self-
performance of subsequent models that have been published. Attention Network (SAN) and subsequently fine-tuning it
As a result, RoBERTa achieves top-tier results in GLUE, within the hybrid SAN/HMM framework. Speech-XLNet
RACE, and SQuAD evaluations. These outcomes underscore acts as a robust regularizer, encouraging the SAN to

VOLUME 12, 2024 26859



M. A. K. Raiaan et al.: Review on Large Language Models

make inferences by prioritizing global structures through relation extraction, and named entity recognition. The pre-
its attention mechanisms. Moreover, Speech-XLNet enables trained weights of the model are accessible to the public,
the model to explore bidirectional contexts, enhancing the enabling researchers to optimize it using their biomedical
effectiveness of speech representation learning. Experimental text data. BioGPT has the capacity to substantially drive
results on TIMIT and WSJ datasets demonstrate that biomedical research forward by facilitating the analysis of
Speech-XLNet significantly enhances the performance of vast quantities of biomedical text data in a more precise and
the SAN/HMM system in terms of both convergence speed efficient manner [111], [112].
and recognition accuracy compared to systems trained from In summary, pre-trained LLMs are foundational in NLP,
randomly initialized weights. The model best achieves an providing a starting point for various applications without
impressive relative improvement of 11.9% and 8.3% on the need for extensive training from scratch. They are widely
the TIMIT and WSJ tasks, respectively. Notably, the top- used and have access to advanced language understanding
performing system achieves a phone error rate (PER) of and generation capabilities. However, responsible use and
13.3% on the TIMIT test set, which, to the best of our ethical considerations are essential when working with these
knowledge, is the lowest PER achieved by a single system. models to ensure fair and unbiased outcomes.

6) DIALOGXL
DialogXL [109] introduces enhancements to tackle longer B. API OF LLMS
historical context and multiparty structures in dialogues. In this section, we discuss the APIs of LLMs, which have
Initially, alterations are made to how XLNet manages been described in Table 12.
recurrence, transitioning from segment-level to utterance- Open AI API: The API provided by OpenAI offers access
level, thereby improving its effectiveness in modeling to GPT models that may be utilized for a wide range of
conversational data. Secondly, the integration of dialog- text-related applications [119]. The API facilitates many
aware self-attention, as opposed to the standard self- tasks such as coding, question and answer, analysis, and
attention in XLNet, enables capturing crucial dependencies other related activities. The available models encompass a
within and between speakers. While training the DialogXL, spectrum of options, spanning from gpt-4 to gpt-3.5-turbo,
a comprehensive set of experiments is conducted on four as well as many legacy variants. The Chat Completions API
ERC benchmarks, comparing DialogXL with mainstream facilitates interactive dialogues by incorporating distinct roles
models. The experimental results consistently demonstrate such as user, and assistance. The programming language
that DialogXL outperforms the baseline models across all provides support for function calling, which allows for
datasets. the retrieval of structured data. The OpenAI API provides

developers with the capability to leverage advancedmodeling
7) T5 of languages for a diverse range of applications.
T5 (Text-to-Text Transfer Transformer) [84] is a ground- Hugging Face: Hugging Face provides a complimentary
breaking LLM developed by Google Research, revolution- Inference API that facilitates the examination and assessment
izing NLP tasks. T5’s innovation lies in framing all NLP of more than 150,000 publicly available ML models [120].
tasks as text-to-text tasks, simplifying the NLP pipeline It features predictive capabilities, and integration with more
and unifying various tasks under a single framework. Built than 20 open-source libraries, and facilitates fast change
upon the Transformer architecture, T5 utilizes multi-head between models. The API facilitates a range of operations,
self-attention to capture intricate language relationships. Its including classification, image segmentation, text analysis,
extensive pre-training on vast text data, followed by fine- speech recognition, and other related functionalities.
tuning on specific tasks, empowers T5 to excel in text Google Cloud API: The Cloud-based NLP API developed
classification, translation, summarization, question answer- byGoogle provides support for a range of approaches, such as
ing, and more. With consistently state-of-the-art results sentiment analysis, text analysis, entity recognition, and other
across NLP benchmarks, T5 has reshaped the field, offering text annotations [115]. The functionalities can be accessed by
researchers and developers a versatile tool for comprehensive developers through REST API calls utilizing either the client
language understanding and generation tasks. libraries or their own custom libraries. Additionally, the API

offers moderation functionalities for the purpose of detecting
8) BIOGPT potentially sensitive content. Several API exists, and each
BioGPT [110] is a large-scale language model that was possesses distinct features and functions.
constructed by the Allen Institute for AI (AI2) with the Microsoft Azure Language APIs:TheseAPIs support many
explicit purpose of undertaking training on biomedical text. activities, including sentiment analysis, text summarization,
It was trained on an extensive corpus of biomedical literature, and other related tasks [116]. Developers use RESTful
including PubMed abstracts and full-text articles, and is endpoints to include Azure LLMs APIs. Microsoft provides
based on the GPT architecture. It has been demonstrated useful SDKs and code examples in other programming
that BioGPT outperforms alternative biomedical language languages, including Python, Java, etc. to facilitate the
models across a range of tasks, such as query answering, utilization of these APIs.

26860 VOLUME 12, 2024



M. A. K. Raiaan et al.: Review on Large Language Models

TABLE 12. Comparison of LLMs APIs.

IBM Watson Natural Language: The IBM Watson API Facebook AI’s Fairseq: The Fairseq framework developed
is a robust tool for investigating and extracting valuable by Facebook AI is a comprehensive tool for performing
information from textual data. This API offers developers a sequence-to-sequence modeling, specifically designed for
variety of functionalities, encompassing sentiment analysis, handling LLMs [121]. Fairseq is a well-suited API for
emotion analysis, and additional features [117]. Due to its many applications related to analyzing and generating natural
provision of multilingual support and a user-friendly API, language. The platform provides support for advanced
this technology enables developers to effectively include models such as BERT and RoBERTa, allowing researchers
sophisticated text analytics into their programs. to perform fine-tuning on these models according to specific
Amazon Comprehend API: The Amazon Comprehend needs.

API is a powerful NLP service provided by Amazon Web In this study, we have provided a comprehensive overview
Services [118]. This tool evaluates textual data, allowing the of seven popular APIs in Table 12 that leverage the capabili-
researchers to acquire significant knowledge, such as entity ties of LLMs for the purpose of NLP-based functionalities.
recognition, language detection, sentiment analysis, and topic However, the taxonomy revealed the presence of several
modeling. Due to its ability to accommodate many languages other APIs that are associated with text analysis but do
and simple integration, the tool displays adaptability in not utilize LLMs. These APIs are TextBlob, TextRazor,
addressing a range of use cases, including customer feedback Sapling AI, MonkeyLearn, and Aylien, etc., which utilize
analysis and others. The utilization of this API can prove to traditional machine learning, statistical methods, and rule-
be a significant resource for enterprises’ marketing to extract based natural NLP techniques instead of relying on extensive
practical insights from unstructured textual data. pre-trained LLMs. Since, the primary focus of this study has

VOLUME 12, 2024 26861



M. A. K. Raiaan et al.: Review on Large Language Models

been on describing the tools that particularly utilize LLMs and the tumor board had a high degree of decision alignment.
for the purpose of advanced text analysis, generation, and Huang et al., [123] investigate the prospective applications
comprehension, we have refrained from discussing these of LLMs with a specific emphasis on ChatGPT, in the field
APIs in depth. of dentistry, mainly focusing on automated dental diagnosis

and highlighting the efficacy of LLMs in dental diagnosis.
VII. DOMAIN SPECIFIC APPLICATION Furthermore, the XLNet contributes to better clinical note
Since there are several pre-trained models in LLMs, all representation by adding temporal information and a realistic
of them are utilized by training or fine-tuned to perform prediction setup [142]. Furthermore, various LLMs models
well-defined tasks maintained by their requirements in also assist the medical industry by making the procedure
different fields. Numerous research studies have consistently easier than previously.
employed LLMs from the diverse domains such as healthcare, Education: Educators have struggled for a long time
finance, education, forecasting, and natural language process- with an unequal educational resources to student demand
ing. The extensive experiments of different LLMs contribute across disciplines. One of the significant challenges is a
to revolutionizing the use of AI across these domains. This shortage of accessible educational resources for pupils to
section demonstrates the potential contribution of LLMs study outside of school. Although online instructional videos
application in different domains. Table 13 illustrates the are helping to alleviate the problem, society still hopes that
major contribution of LLMs in the specific domain, as well AI will deliver individualized teaching services to satisfy
as outline their prospective limitations and future directions. the learning demands of each student and increase teaching
Bio-Medical and Healthcare: As previously stated, GPT efficiency. In the light of above discussion, LLMs have the

has several versions, ranging from GPT1 to GPT4. GPT3 is potential to revolutionize many facets of learning, teaching,
extremely useful in the healthcare industry since it can be and educational research in the education sector [140].
trained to support customer service with no effort. GPT3 gets The GPT model aids the students in converting the math
all required information through a conversation rather than word problems into representative equations [143]. Kasenci
an intake form, and many systems might be built to assist et al., [19] highlighted substantial impact of LLMs in
numerous patients at the same time [126]. Besides, clinics education by facilitating personalized learning, automating
and hospitals are places to cure illness, but it is also true grading process, and accessibility of educational resources.
that various contagious viruses are brought into these places. Hadi et al., [137] presents a thorough analysis of LLMs, cov-
Patients and healthcare providers can be better protected from ering their historical development, wide-ranging applications
infection by replacing a human receptionist with a robot in domains such as medicine, engineering, education, and
which becomes increasingly important during the COVID- their potential impact on the trajectory of AI. Lo et al.,
19 epidemic [140]. Since clinics and hospitals often see a [138] and Dwivedi et. al. [139] investigate the prospective
high volume of patients on a daily basis, an optimum and uses of ChatGpt within the realm of education and identify
lightweight system may submit several queries for single the primary obstacles that have arisen during its initial
patients to create acceptable output. deployment. Besides, in terms of writing authentic texts in

Consequently, GPT models can also aid in cost reduction distinct formats, including essays, summaries, and articles,
in the medical industry. Furthermore, biomedical and clinical these models help to accomplish this without any error.
text mining has always been an essential and major challenge In contrast, the manual process may have human errors
due to the complex nature of domain corpora and the in the documentation. In this case, the GPT model helps
continually expanding number of documents. As a result, to address this problem. In addition, the XLNet helps to
BERT models can improve the performance of biomedical understand the texts and documents which can be utilized
and clinical text mining models [141]. Salam et al., [128] in the academic sector [38]. Furthermore, other models may
and Korngiebel et al., [126] demonstrate the substantial impact the education system by making it more engaging,
advantages of ChatGPT in the domains of healthcare, clinical accessible, and productive for both students and teachers.
research, and practice, although simultaneously underscoring Social Media: The LLMs have leveraged several aspects
the imperative necessity for proactive inspection and ethical of the social media industry regarding content production,
transparency. Several studies [125], [129], [131], [132] moderation, sentiment analysis, etc. There are some tasks
explore the utilities and constraints of LLMs such as in the social media can be generated such as writing
ChatGPT in the context of clinical practice, research, and content, classifying text, and even full blogs and articles for
public health. In their study, Kung et al., [130] conducted an social media. These models can also perform named entity
evaluation of ChatGPT’s performance on the United States recognition (NER) and text classification [144], [145]. When
Medical Licensing Examination (USMLE), and the outcomes the GPT, XLNet, BERT, etc., models aid the writer and
indicate the potentiality of LLMs to support clinical decision- content producers in generating a consistent flow of write
making and medical education. Sorin et al., [124] evaluated up. It also provides content suggestions, and to create a
ChatGPT-3.5 as a decision support for breast tumor boards safer online environment, these models are hired to assist
where they compared the tumor board’s explanations, and in discovering and filtering out different dangerous and
summaries with ChatGPT-3.5 and showed that ChatGPT-3.5 improper content. Abramski et al., [42] utilized network

26862 VOLUME 12, 2024



M. A. K. Raiaan et al.: Review on Large Language Models

TABLE 13. Domain specific machine learning-based study comparison in LLMs.

VOLUME 12, 2024 26863



M. A. K. Raiaan et al.: Review on Large Language Models

TABLE 13. (Continued.) Domain specific machine learning-based study comparison in LLMs.

science and the principles of cognitive psychology to evaluate and efficiently maintaining the entire business by saving
biases present in LLMs. Sobieszek et al., [136] presents a time and reducing laborious tasks. Frederico et al., [135]
critical examination of the stated semantic capabilities of presents an initial investigation into the potential applications
GPT-3, aiming to challenge the current view of its dismissal. and effects of ChatGPT in the domain of supply chain
Moreover, it assists in determining public opinion on certain management. Their study provides significant insights for
topics by analyzing public interest and demand. professionals engaged in this domain. Mich et. al. [133]
Business: In business, LLMs helps companies improve present an initial investigation of potential hazards associated

their decision-making processes, product manufacturing with the implementation of ChatGPT in bussiness domain.
processes, operations, and customer interactions. Communi- Yu et al., [134] presented an analysis of the capabilities
cating with customers and providing 24/7 customer service of LLMs, specifically GPT-4, in the context of financial
by answering their queries, assisting them in their work, forecasting for a time series. Besides, their findings reveal
and providing advanced advice related to areas of interest to that the performance of LLMs outperforms other traditional
customers is crucial for business progress. Moreover, it is also models also.
important to analyze customer sentiment, market trends, risk Agriculture: In agriculture, variations of GPT models,
factors, and competitive intelligence [20]. In this case, LLMs includingGPT3, BERT, andXLNetmodels, play a significant
help to fulfill all their requirements within a short period. role [146], [147], [148]. They are able to analyze large data
The LLMs models, like GPT, XLNet, BERT, etc., play a hubs of soil, crop, and weather data along with satellite
vital role in creating customer documents and product details imagery. Thesemodels provide recommendations on planting

26864 VOLUME 12, 2024



M. A. K. Raiaan et al.: Review on Large Language Models

These developments have not only expanded the
applicability of NLP but have also raised ethical consid-
erations, prompting research in biasmitigation [153] and
responsible AI. LLMs have enabled breakthroughs in
applications like conversational AI, few-shot and zero-
shot learning, and domain-specific NLP in fields like
healthcare and finance. These advancements underscore
the pivotal role of LLMs in advancing the capabilities
of NLP and continue to shape the future of language
understanding and generation.

• Automation and Efficiency:LLMs are used to automate
tasks that were previously time-consuming and labor-
intensive, leading to increased efficiency in industries

FIGURE 8. Visual representation of impact on LLMs.
such as customer support, content generation, and data
analysis. The automation and efficiency of LLMs, driven
by models like BERT and GPT, have revolutionized

times, irrigation, fertilizer application, and optimizing fields industries and applications. These models have auto-
and resources. Farmers can obtain current updates andmarket mated intricate language-related tasks, from sentiment
requirements, predict crop prices, anticipate natural disasters, analysis to language translation, making themmore effi-
and document farmers’ and crop details. Manual agricultural cient and accessible. LLMs, such as DialoGPT [154] and
management can be time-consuming and laborious, but these ChatGPT, have powered conversational AI, streamlining
LLMs can support to accomplish these tasks to a greater customer support and interactions. Moreover, they excel
extent. in few-shot and zero-shot learning, as demonstrated by

GPT-3 [155], automating tasks with minimal examples.
VIII. IMPACT OF LARGE LANGUAGE MODELS ON Multilingual LLMs like mBERT have automated lan-
SOCIETY guage tasks across various languages, enhancing global
LLMs and similar AI technologies have had a profound accessibility. Efficiency has further advanced through
impact on society across various domains. The impact models like DistilBERT and ALBERT, which maintain
of LLMs on society is multifaceted, and it is important performance while reducing computational resources.
to consider both the positive and negative consequences. These models can be fine-tuned for specific domains,
As these technologies continue to evolve, stakeholders, such as healthcare [156], making them indispensable in
including governments, businesses, researchers, and the automating domain-specific tasks efficiently.
general public, must work together to harness the benefits

• Content Generation: LLMs are capable of generating
of LLMs while addressing their challenges and ethical human-like text, which has implications for content
implications. The visual representation of Figure 8 effectively creation, including automated news articles, marketing
demonstrates the impact of LLMs, outlining their benefits on materials, and creative writing.
the left and the adversarial impacts on the right side. The

• Language Translation: LLMs have improved machine
positive impacts of LLMs are as follows: translation systems, making communication across lan-

• Advancements in Natural Language Processing guages more accessible and accurate.
(NLP): LLMs have significantly advanced the field • Virtual Assistants and Chatbots: LLMs power virtual
of NLP, making it possible to automate and scale a assistants and chatbots, enhancing customer service and
wide range of language-related tasks such as trans- providing round-the-clock support in various industries.
lation, summarization, sentiment analysis, and more. • Medical and Scientific Research: LLMs are used
In recent years, Natural Language Processing (NLP) has to analyze and summarize vast amounts of medical
witnessed significant advancements, primarily driven and scientific literature, aiding researchers in finding
by the emergence of Large Language Models (LLMs). relevant information quickly.
These advancements, exemplified by models such as • Accessibility: LLMs have the potential to improve
BERT [10], RoBERTa [67], and XLNet [107], have accessibility by providing real-time translation and
transformed the NLP landscape. Notably, LLMs have transcription services for individuals with hearing
been fine-tuned for various specific NLP tasks, enabling impairments or language barriers.
remarkable performance improvements. Multilingual • Personalization: LLMs enable personalized recommen-
models like mBERT [149] and cross-lingual models like dations and content curation on platforms such as social
XLM-R [150] have facilitated language understanding media, e-commerce, and news websites.
across diverse linguistic contexts. Additionally, there • Creative Tools: LLMs are used as creative tools in
has been a focus on creating more efficient versions of various art forms, including generating poetry, music,
LLMs such as DistilBERT [151] and ALBERT [152]. and visual art.

VOLUME 12, 2024 26865



M. A. K. Raiaan et al.: Review on Large Language Models

• Education and Skill Development: The rise of LLMs article writing, social media posts [162], product descriptions,
underscores the importance of education and skill devel- and more. This automation simplifies content creation
opment in AI and data science, as these technologies processes and allows for scalable production of top-tier
become increasingly integral to various industries. content.

In addition to numerous positive sides, LLMs also entail 5. Revolutionizing Healthcare: LLMs find applications in
some downsides. These downsides are outlined as follows: medical record analysis [129], diagnosis assistance, and drug

• Ethical Concerns: Bias and fairness issues in LLMs discovery. They empower healthcare professionals to access
have raised ethical concerns. LLMs may perpetuate or and comprehend extensivemedical literature and patient data,
amplify biases present in training data, leading to unfair thereby enhancing healthcare decision-making.
or discriminatory outcomes. 6. Revamping Education: The education sector [163]

• Misinformation and Disinformation: LLMs can gener- leverages LLMs for automated grading, ensuring prompt
ate realistic-sounding fake text, raising concerns about feedback to students. These models also contribute to the
the spread of misinformation and disinformation. development of intelligent tutoring systems and personalized

• Job Displacement: The automation capabilities of learning platforms.
LLMsmay lead to job displacement in certain industries, 7. Aiding Legal Practices: Legal practitioners [164]
particularly in routine data-entry and content-generation benefit from LLMs for contract analysis, legal research,
roles. and document review. These models assist in efficiently

• Data Privacy: The use of LLMs often involves pro- extracting pertinent information and identifying potential
cessing large amounts of user-generated text data, legal concerns.
which raises data privacy concerns, especially regarding 8. Assisting Human Resources: LLMs support HR
sensitive or personal information. professionals [165] in tasks like candidate screening, resume

• Economic Impact: The adoption of LLMs can disrupt parsing, and identifying potential job candidates. They
traditional business models and create economic shifts streamline time-consuming processes within the recruitment
as industries adapt to automation and AI technologies. phase.

• Regulation and Accountability: Policymakers and 9. Empowering Financial Services: In the realm of
regulators are grappling with the need to establish financial services [166], LLMs come into play for activities
guidelines and regulations for the responsible use of like sentiment analysis of news articles, algorithmic trading,
LLMs, including addressing issues of bias, transparency, risk assessment, and fraud detection. They are instrumental in
and accountability. making informed investment choices and managing financial

risks.
IX. INDUSTRIAL SIGNIFICANCE OF LARGE LANGUAGE 10. Boosting E-commerce: LLMs enable personalized
MODELS product recommendations [167], chatbots for customer
LLMs have gained substantial popularity in various indus- support, and efficient inventorymanagement. These enhance-
tries, bringing about radical transformations. Influence of ments result in enriched user experiences and heightened
LLMs in industries is visible which can be presented through sales.
several key facets: 11. Illuminating Customer Insights: LLMs analyze
1. Enhancing NLP Applications: LLMs have ushered in customer reviews [168], feedback, and social media data, fur-

a revolution in NLP applications [157] across sectors like nishing businesses with insights into customer preferences,
customer service, chatbots, and sentiment analysis. They opinions, and sentiments. This invaluable information aids
contribute to more precise and efficient interactions with companies in customizing their products and services.
users, leading to increased customer satisfaction and reduced As LLMs continue to advance, their industrial impor-
response times. tance is undeniable. LLMs streamline operations, enhance
2. Enabling Data Analysis and Information Extraction: decision-making, and bolster efficiency across diverse

LLMs play a pivotal role in extracting valuable insights domains, positioning them as a transformative technology in
from unstructured text data [158]. This is particularly the contemporary business landscape.
critical in fields like finance, market research [159], and
healthcare, where deciphering market trends, sentiment in X. OPEN ISSUES AND CHALLENGES
news, or medical records hold paramount significance. This section discusses critical analysis of open issues and
3. Facilitating Translation Services: Industries heavily challenges of LLMs.

reliant on multilingual communication [160], such as e-
commerce, travel, and international business which may be A. OPEN ISSUES
benefited from LLMs that streamline automated translation. In this section, we delve into the open issues related to LLMs.
Translation service saves resources and ensuring high-quality These issues appeared recently as focal point in AI research
translations across multiple languages. and development. We raise the necessity for ongoing research
4. Empowering Content Generation: LLMs are harnessed and innovation to resolve issues that have emerged alongside

for content generation [161], which encompasses automated the rapid development of LLMs. Our discussionwill cast light

26866 VOLUME 12, 2024



M. A. K. Raiaan et al.: Review on Large Language Models

on the significance of these unresolved issues, highlighting attracted significant attention and applications in numerous
their impact on various applications and the AI landscape as fields. However, this sudden rise of these technological
a whole. dependencies with higher impact has also revealed many

challenges and concerns. In this discussion, we will examine
• Issue 1: Ethical and Responsible AI The question

ten of the most significant challenges pertaining to LLMs.
regarding how to ensure the ethical use of large language
models remains unresolved. Filtering, moderation, and

• Challenge 1: Data Complexity and Scale In the era of
accountability concerns regarding AI-generated content LLMs, the size and complexity of the datasets on which
remain problematic. Misinformation, hate speech, and they are trained is one of the most significant challenges.
biased content generated by LLMs necessitate continu- These models are typically trained on enormous corpora
ous research and development [169]. of Internet-sourced text data. These datasets are so

• Issue 2: Multimodal Integration While LLMs are extensive that it is nearly impossible to understand or
predominantly concerned with text, there is a growing investigate the totality of their information. This raises
demand for multimodal models that can comprehend concerns regarding the quality and biases of the training
and generate content that includes text, images, and data and the potential for the unintentional dissemination
other media types [170]. Integrating multiple modalities of detrimental or inaccurate information [176].
into a single model poses difficulties in data acquisition,

• Challenge 2: Tokenization Sensitivity
training, and evaluation. For analysis, LLMs rely significantly on tokeniza-

• Issue 3: Energy Efficiency The environmental impact tion, dividing text into smaller units (tokens) [177].
of training and deploying large language models is still Tokenization is essential for language processing and
an urgent concern [171]. It is essential to develop more comprehension but can also present challenges. For
energy-efficient training methods, model architectures, instance, the meaning of a sentence can alter signifi-
and hardware solutions to reduce the carbon footprint of cantly based on the choice of tokens or the ordering
LLMs. of words. This sensitivity to input phrasing can lead

• Issue 4: Security and Adversarial Attacks to unintended outcomes when generating text, such
LLMs are vulnerable to adversarial context, where as adversarial assaults and output variations based on
slight input modifications can lead to an unexpected minute input changes.
and potentially harmful outputs [172]. Improving model

• Challenge 3: Computational Resource Demands
robustness and security against such situation is a crucial The training of LLMs is a computationally intensive
area of study, particularly for cybersecurity and content procedure that requires substantial hardware and energy
moderation applications. resources [178]. It is necessary to have access to

• Issue 5: Privacy and Data Protection As LLMs supercomputing clusters or specialized hardware in
become more competent, user privacy and data protec- order to train large models, and the environmental
tion concerns increase. Finding methods for users to impact of such resource-intensive training has raised
interact with these models without compromising their concerns. Significant energy consumption is associated
personal information is an ongoing challenge. There is a with training LLMs at scale, contributing to the AI
need for research on privacy-preserving techniques and industry’s overall carbon footprint.
regulatory compliance [173].

• Challenge 4: Fine-Tuning Complexity
• Issue 6: Generalization and Few-Shot Learning While pre-training gives LLMs a broad comprehension
LLMs performs well when there is abundant data of language, fine-tuning is required to adapt these
but struggles with tasks requiring few examples or models to specific tasks [179]. Fine-tuning entails
domain-specific knowledge. Improving their capacity to training the model on a smaller dataset, frequently
generalize and perform well with limited training data is requiring human annotators to label examples. As it
a crucial area of research [174]. involves the construction of task-specific datasets and

• Issue 7: Cross-Lingual and Low-Resource Settings It extensive human intervention, this process can be both
is an ongoing challenge to make LLMs more accessible time-consuming and costly.
and effective in languages and regions with limited

• Challenge 5: Real-Time Responsiveness The remark-
resources and data [175]. Global applications require able training capabilities of LLMs come at the expense
developing techniques for cross-lingual transfer learning of inference speed. Real-time response or prediction
and low-resource language support. generation with these models can be sluggish, limiting

their applicability in applications such as chatbots or
B. CHALLENGES recommendation systems where low-latency responses
LLMs have rapidly evolved from being non-existent to are crucial for user satisfaction.
becoming a ubiquitous presence in the field of machine • Challenge 6: Contextual Constraints
learning within just a few years. Its extraordinary ability LLMs can only evaluate a limited number of preceding
to generate text that resembles that of a human which has tokens when generating text due to their limited context

VOLUME 12, 2024 26867



M. A. K. Raiaan et al.: Review on Large Language Models

window [180]. This limitation presents difficulties when They also need focus on integrating continuous monitoring
working with lengthy documents or having lengthy and auditing mechanisms into AI pipelines, thereby conform-
conversations. Maintaining coherence and relevance ing fairness and impartiality of the system. This commitment
over lengthy text sequences can be challenging because to mitigating bias ensures that LLMs not only advance in
the model may neglect or lose track of the relevant capability but LLMs also upholds ethical standards.
information.

• Challenge 7: Bias and Undesirable Output B. EFFICIENCY OPTIMIZATION
In the output, LLMs display biases or undesirable A core concern driving research is the quest of efficient
characteristics. This is due to the inherent biases in training techniques. Researchers are delving into innovative
the training data, which are assimilated by the model methods like federated learning, which enables the distri-
and reflected in its responses [181]. Such biases can bution of training across decentralized data sources [183].
manifest as objectionable, discriminatory, or harmful They are also exploring knowledge distillation techniques
content, making it imperative to address and mitigate for model compression and finding ways to reduce the
these concerns to ensure the responsible deployment of substantial computational and environmental costs associated
AI. with LLMs. This optimization paves the way for more

• Challenge 8: Knowledge Temporality sustainable and resource-efficient AI models.
LLMs learn using historical data from the Internet, and
their knowledge is restricted to what is available as of C. DYNAMIC CONTEXT HANDLING
a particular date. Consequently, they may lack access LLMs are being endowed with enhanced context manage-
to the most recent information or events. This can be ment capabilities. This empowers them to comprehend longer
problematic when users expect up-to-date responses or context windows and seamlessly handle extensive documents
when the conversation involves recent events. or conversations. Such enhancements significantly expand

• Challenge 9: Evaluation Complexity their utility in various applications and resolve previous
Evaluation of LLMs presents significant difficulties. limitations.
Many extant evaluation metrics are insufficient to
capture the nuances of model performance, which D. CONTINUOUS LEARNING
raises questions about their efficacy. Additionally, these To keep LLMs up-to-date, researchers are focusing on
metrics can be susceptible to manipulation or gaming, developing techniques that enable these models to adapt
which may provide an inaccurate image of a model’s on evolving language and knowledge over time. This
capabilities. To assess LLMs’ actual performance and ensures that LLMs remain valuable and accurate sources of
limitations, robust and reliable evaluation methodolo- information and consistently overcoming challenges of being
gies are required. outdated.

• Challenge 10: Dynamic Evaluation Needs
Frequently, evaluating LLMs entails comparing their E. INTERPRETABLE AI
outputs to static benchmarks or human-authored ground

The research community is committed to making LLMs’
truth. However, language is dynamic and evolves, and

outputs more transparent and interpretable. Improving inter-
preset evaluation data may not adequately reflect a

pretability fosters the confidence and comprehension in AI
model’s adaptability to language and context change.

decision-making processes which has been a major concern
This difficulty underscores the need for evaluation

for a long time after the advent of LLMs [184].
frameworks that are more dynamic and continually
updated.

F. MULTIMODAL LLMS
Researchers are pioneering the development of LLMs that

XI. FUTURE RESEARCH PROSPECTS ON LLMS incorporate text, vision, and other modalities [185]. These
Since LLMs are emerging research topic in recent times, models can understand and generate text from images, videos,
several key research focuses and directions are prominent and audio, creating new avenues for AI applications and
that may address and resolve the challenges and open issues effectively addressing the need for multi-sensory comprehen-
discussed earlier. Resolving these open issues and challenges sion.
may harness the full potential of LLMs while ensuring its
responsible and ethical use in AI landscape. G. HUMAN-AI COLLABORATION

Research on how humans and LLMs can collaborate
A. ENHANCING BIAS MITIGATION effectively, with AI assisting and augmenting human tasks,
Researchers are dedicated to refining training data to is a crucial focal point. This collaboration bridges the gap
minimize bias, devising effective debiasing techniques, and between AI capabilities and human needs, thereby resolving
establishing guidelines for responsibleAI development [182]. previous challenges and issues in deployment.

26868 VOLUME 12, 2024



M. A. K. Raiaan et al.: Review on Large Language Models

H. DYNAMIC EVALUATION METRICS AND RELEVANT XIII. CONCLUSION
BENCHMARKS The field of LLMs has witnessed a remarkable evolu-
Researchers are working on dynamic evaluation metrics that tion and expansion, resulting in extraordinary capabilities
adapt to changing language and context, ensuring that LLMs in NLP tasks and various applications in various areas.
performance is accurately assessed [186]. Finding a suitable Based on neural networks and the changing transformer
metric along with the development of relevant and up-to- architecture, these LLMs have revolutionized our approach
date benchmarks which may address earlier shortcomings in to machine language comprehension and generation. The
assessing AI capabilities. thorough review of this research has provided an insightful

overview of LLMs, encompassing their historical develop-
I. PERSONALIZATION AND CUSTOMIZATION ment, architectural foundations, training methods, and vast
Techniques to customize LLMs interactions to individual user advancement resources. The study has also examined the
preferences and needs are gaining popularity nowadays. This various applications of LLMs in disciplines such as health-
personalization boosts user satisfaction and resolves issues care, education, social sciences, business, and agriculture,
related to one-size-fits-all AI interactions. demonstrating their potential to address real-world issues.

In addition, this review has delved into the societal effects
of LLMs, discussing how they shape the future of AI and

J. ETHICAL AND LEGAL FRAMEWORKS can be utilized to address complex problems. However, the
In response to evolving AI regulation, researchers are study has not addressed the pressing challenges and ethical
diligently developing ethical and legal regulatory frame- considerations associated with deploying LLMs, including
works. These frameworks serve as guiding principles model biases, privacy concerns, and the need for enhanced
for the responsible use of LLMs and ensure com- robustness and controllability. As the field of LLMs research
pliance with data protection and privacy regulations, continues to evolve swiftly, this review could be a valuable
effectively addressing previous concerns about ethical AI resource for practitioners, researchers, and experts seeking
deployment [187]. a comprehensive understanding of LLMs’ past, present, and

These future research directions may overcome longstand- future. The study emphasizes the significance of ongoing
ing challenges and open issues raised in LLMs domain. These efforts to improve the efficacy and dependability of LLMs,
avenues may lead to the maximization of LLMs potential by as well as the need for ethical development and deployment
the future researchers while upholding the highest standards practices. LLMs represent a pivotal advancement in AI
of accountability and ethics in AI landscape. and NLP, with the potential to revolutionize a variety of

domains and solve complex problems. This article provides a
XII. LIMITATIONS comprehensive foundation for future researcher to understand
While conducting a thorough examination of LLMs, which the dynamics of ever evolving Large Language Models
includes analyzing their taxonomies, comparing configura- research.
tions, and addressing concerns and obstacles, it is essential
to recognize the existence of limitations that should be REFERENCES
considered. A primary limitation of this study is the unavail- [1] S. Pinker, The Language Instinct: How the Mind Creates Language.
ability of review papers that directly relate to the topic of London, U.K.: Penguin, 2003.

LLMs. Although we have made diligent attempts to address [2] M. D. Hauser, N. Chomsky, and W. T. Fitch, ‘‘The faculty of language:
What is it, who has it, and how did it evolve?’’ Science, vol. 298, no. 5598,

the available research thoroughly, the limited quantity of pp. 1569–1579, Nov. 2002.
papers in this field restricts our potential to perform broad [3] W. X. Zhao et al., ‘‘A survey of large language models,’’ 2023,
comparisons and evaluations. While endeavoring to offer a arXiv:2303.18223.

[4] I. Turing, ‘‘Computing machinery and intelligence,’’ Mind, vol. 59,
broad perspective on LLMs concepts, we recognize that this no. 236, p. 433, 2007.
analysis predominantly focuses on the ground-level concepts [5] Y. Shen, L. Heacock, J. Elias, K. D. Hentel, B. Reig, G. Shih, and L. Moy,
of LLMs configurations and applications. Limited resources, ‘‘ChatGPT and other large language models are double-edged swords,’’

time, and page constraints affect the extensive exploration Radiology, vol. 307, no. 2, Apr. 2023, Art. no. e230163.
[6] M. A. K. Raiaan, K. Fatema, I. U. Khan, S. Azam, M. R. U. Rashid,

of individual LLMs architectures. Although our goal is M. S. H. Mukta, M. Jonkman, and F. De Boer, ‘‘A lightweight
not to offer the understanding of single LLMs but instead robust deep learning model gained high accuracy in classifying a

provide the evolution of LLMs and its application around wide range of diabetic retinopathy images,’’ IEEE Access, vol. 11,
pp. 42361–42388, 2023.

various domains, however, readers looking for detailed [7] B. Ramabhadran, S. Khudanpur, and E. Arisoy, ‘‘Proceedings of the
analysis of specific architectures and advanced topics are NAACL-HLT 2012 workshop: Will we ever really replace the N-gram

not thoroughly covered. Furthermore, the impact of the model? On the future of language modeling for HLT,’’ in Proc. NAACL-
HLT, 2012, pp. 1–11.

LLMs across various domains, including education, health, [8] T. Mikolov, M. Karafiát, L. Burget, J. Černockỳ, and S. Khudanpur,
and economy, is highlighted, but assessing the practical ‘‘Recurrent neural network based language model,’’ in Proc. Annu. Conf.
impacts of LLMs in many domains can be complex and Int. Speech Commun. Assoc. (ISCA), 2010, pp. 1045–1048.

[9] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez,
subjective, especially when considering their impact on social Ł. Kaiser, and I. Polosukhin, ‘‘Attention is all you need,’’ in
aspects. Proc. Adv. Neural Inf. Process. Syst., vol. 30, 2017.

VOLUME 12, 2024 26869



M. A. K. Raiaan et al.: Review on Large Language Models

[10] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, ‘‘BERT: Pre-training [35] T. Wolf, L. Debut, V. Sanh, J. Chaumond, C. Delangue, A. Moi, P. Cistac,
of deep bidirectional transformers for language understanding,’’ 2018, T. Rault, R. Louf, and M. Funtowicz, ‘‘TransFormers: State-of-the-art
arXiv:1810.04805. natural language processing,’’ in Proc. Conf. Empirical Methods Natural

[11] Y. Khare, V. Bagal, M. Mathew, A. Devi, U. D. Priyakumar, and Lang. Syst. Demonstrations, 2020, pp. 38–45.
C. Jawahar, ‘‘MMBERT: Multimodal BERT pretraining for improved [36] C. Sur, ‘‘RBN: Enhancement in language attribute prediction using
medical VQA,’’ in Proc. IEEE 18th Int. Symp. Biomed. Imag. (ISBI), global representation of natural language transfer learning technology like
Apr. 2021, pp. 1033–1036. Google BERT,’’ Social Netw. Appl. Sci., vol. 2, no. 1, p. 22, Jan. 2020.

[12] R. Liu, C. Jia, J. Wei, G. Xu, L. Wang, and S. Vosoughi, ‘‘Mitigating [37] J. J. Bird, A. Ekárt, and D. R. Faria, ‘‘Chatbot interaction with artificial
political bias in language models through reinforced calibration,’’ in intelligence: Human data augmentation with t5 and language transformer
Proc. AAAI Conf. Artif. Intell., 2021, vol. 35, no. 17, pp. 14857–14866. ensemble for text classification,’’ J. Ambient Intell. Humanized Comput.,

[13] K. Sanderson, ‘‘GPT-4 is here: What scientists think,’’ Nature, vol. 615, vol. 14, no. 4, pp. 3129–3144, Apr. 2023.
no. 7954, p. 773, Mar. 2023. [38] B. D. Lund and T. Wang, ‘‘Chatting about ChatGPT: How may AI and

[14] S. Pichai. (2023). An Important Next Step on Our AI Jour- GPT impact academia and libraries?’’ Library Hi Tech News, vol. 40,
ney. [Online]. Available: https://blog.google/technology/ai/bard-google- no. 3, pp. 26–29, May 2023.
ai-search-updates [39] A. Radford, K. Narasimhan, T. Salimans, and I. Sutskever. Improving

[15] R. Taori, I. Gulrajani, T. Zhang, Y. Dubois, X. Li, C. Guestrin, Language Understanding by Generative Pre-Training. Mikecaptain.com.
P. Liang, and T. B. Hashimoto. (2023). Alpaca: A Strong, Repli- Accessed: Feb. 15, 2024. [Online]. Available: https://www.mikecaptain.
cable Instruction-following Model. [Online]. Available: https://crfm. com/resources/pdf/GPT-1.pdf
stanford.edu/2023/03/13/alpaca.html [40] B. Ghojogh and A. Ghodsi. Attention Mechanism, Transformers, BERT,

[16] L. Fan, L. Li, Z. Ma, S. Lee, H. Yu, and L. Hemphill, ‘‘A bibliometric and GPT: Tutorial and Survey. Osf.io. Accessed: Feb. 15, 2024. [Online].
review of large language models research from 2017 to 2023,’’ 2023, Available: Osf.io.
arXiv:2304.02020. [41] A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and I. Sutskever,

[17] Y. Chang, X. Wang, J. Wang, Y. Wu, L. Yang, K. Zhu, H. Chen, X. Yi, ‘‘Language models are unsupervised multitask learners,’’ OpenAI Blog,
C. Wang, Y. Wang, W. Ye, Y. Zhang, Y. Chang, P. S. Yu, Q. Yang, vol. 1, no. 8, p. 9, 2019.
and X. Xie, ‘‘A survey on evaluation of large language models,’’ 2023, [42] K. Abramski, S. Citraro, L. Lombardi, G. Rossetti, and M. Stella,
arXiv:2307.03109. ‘‘Cognitive network science reveals bias in GPT-3, GPT-3.5 turbo, and

[18] J. Huang and K. C.-C. Chang, ‘‘Towards reasoning in large language GPT-4mirroring math anxiety in high-school students,’’ Big Data Cognit.
models: A survey,’’ 2022, arXiv:2212.10403. Comput., vol. 7, no. 3, p. 124, Jun. 2023.

[19] E. Kasneci et al., ‘‘ChatGPT for good? On opportunities and challenges [43] M. Shoeybi, M. Patwary, R. Puri, P. LeGresley, J. Casper, and
of large language models for education,’’ Learn. Individual Differences, B. Catanzaro, ‘‘Megatron-LM: Training multi-billion parameter language
vol. 103, Apr. 2023, Art. no. 102274. models using model parallelism,’’ 2019, arXiv:1909.08053.

[20] M.U.Hadi, R. Qureshi, A. Shah,M. Irfan, A. Zafar,M. Shaikh, N. Akhtar, [44] D. M. Katz, M. J. Bommarito, S. Gao, and P. Arredondo,
J.Wu, and S.Mirjalili, ‘‘A survey on large languagemodels: Applications, ‘‘GPT-4 passes the bar exam,’’ Mar. 2023. [Online]. Available:
challenges, limitations, and practical usage,’’ TechRxiv, 2023. http://dx.doi.org/10.2139/ssrn.4389233

[21] B. Cronin, ‘‘Annual review of information science and technology,’’ Inf. [45] M. J. Page, J. E. McKenzie, P. M. Bossuyt, I. Boutron, T. C. Hoffmann,
Today, Medford, OR, USA, 2004, vol. 39. C. D. Mulrow, L. Shamseer, J. M. Tetzlaff, E. A. Akl, and S. E. Brennan,

[22] M. Kardum, ‘‘Rudolf Carnap—The grandfather of artificial neural ‘‘The prisma 2020 statement: An updated guideline for reporting
networks: The influence of Carnap’s philosophy onwalter pitts,’’ inGuide systematic reviews,’’ Int. J. Surg., vol. 88, Jan. 2020, Art. no. 105906.
to Deep Learning Basics. Cham, Switzerland: Springer, 2020, pp. 55–66. [46] J. J. Webster and C. Kit, ‘‘Tokenization as the initial phase in NLP,’’ in

[23] G. Leech, ‘‘Corpora and theories of linguistic performance,’’ Svartvik, Proc. 14th Conf. Comput. Linguistics (COLING), vol. 4, 1992.
J. Directions Corpus Linguistics, vol. 10, pp. 22–105, Jun. 1992. [47] T. Kudo, ‘‘Subword regularization: Improving neural network translation

[24] J. Hirschberg, B. W. Ballard, and D. Hindle, ‘‘Natural language models with multiple subword candidates,’’ 2018, arXiv:1804.10959.
processing,’’ AT&T Tech. J., vol. 67, no. 1, pp. 41–57, Jan. 1988.

[48] R. Sennrich, B. Haddow, and A. Birch, ‘‘Neural machine translation of
[25] B.-H. Juang and L. R. Rabiner, ‘‘Automatic speech rare words with subword units,’’ 2015, arXiv:1508.07909.

recognition—A brief history of the technology development,’’ Georgia
[49] M. Schuster and K. Nakajima, ‘‘Japanese and Korean voice search,’’

Inst. Technol., Santa Barbara, CA, USA, Tech. Rep., 2005, vol. 1, p. 67.
in Proc. IEEE Int. Conf. Acoust., Speech Signal Process. (ICASSP),

[26] D. S. Hain, R. Jurowetzki, T. Buchmann, and P. Wolf, ‘‘A text- Mar. 2012, pp. 5149–5152.
embedding-based approach to measuring patent-to-patent technological
similarity,’’ Technol. Forecasting Social Change, vol. 177, Apr. 2022, [50] R. Child, S. Gray, A. Radford, and I. Sutskever, ‘‘Generating long
Art. no. 121559. sequences with sparse transformers,’’ 2019, arXiv:1904.10509.

[27] G. Curto, M. F. Jojoa Acosta, F. Comim, and B. Garcia-Zapirain, [51] K. Hornik, M. Stinchcombe, and H. White, ‘‘Multilayer feedforward
‘‘Are AI systems biased against the poor? A machine learning analysis networks are universal approximators,’’ Neural Netw., vol. 2, no. 5,
using Word2Vec and GloVe embeddings,’’ AI Soc., vol. 2022, pp. 1–16, pp. 359–366, Jan. 1989.
Jun. 2022. [52] V. Nair and G. E. Hinton, ‘‘Rectified linear units improve restricted

[28] P. Azunre, Transfer Learning for Natural Language Processing. Boltzmann machines,’’ in Proc. 27th Int. Conf. Mach. Learn., 2010,
New York, NY, USA: Simon and Schuster, 2021. pp. 807–814.

[29] Y. Shi, M. Larson, and C.M. Jonker, ‘‘Recurrent neural network language [53] D. Hendrycks and K. Gimpel, ‘‘Gaussian error linear units (GELUs),’’
model adaptation with curriculum learning,’’ Comput. Speech Lang., 2016, arXiv:1606.08415.
vol. 33, no. 1, pp. 136–154, Sep. 2015. [54] B. Zhang and R. Sennrich, ‘‘Root mean square layer normalization,’’ in

[30] A. Kovačević and D. Kečo, ‘‘Bidirectional LSTM networks for Proc. Adv. Neural Inf. Process. Syst., vol. 32, 2019.
abstractive text summarization,’’ in Advanced Technologies, Systems, and [55] B. Workshop et al., ‘‘BLOOM: A 176B-parameter open-access multilin-
Applications VI. Cham, Switzerland: Springer, 2021, pp. 281–293. gual language model,’’ 2022, arXiv:2211.05100.

[31] Y. Wu et al., ‘‘Google’s neural machine translation system: Bridging the [56] B. Lester, R. Al-Rfou, and N. Constant, ‘‘The power of scale for
gap between human and machine translation,’’ 2016, arXiv:1609.08144. parameter-efficient prompt tuning,’’ 2021, arXiv:2104.08691.

[32] R. K. Yadav, S. Harwani, S. K. Maurya, and S. Kumar, [57] X. Lisa Li and P. Liang, ‘‘Prefix-tuning: Optimizing continuous prompts
‘‘Intelligent chatbot using GNMT, SEQ-2-SEQ techniques,’’ in for generation,’’ 2021, arXiv:2101.00190.
Proc. Int. Conf. Intell. Technol. (CONIT), Jun. 2021, pp. 1–5. [58] H. W. Chung et al., ‘‘Scaling instruction-finetuned language models,’’

[33] D. Luitse and W. Denkena, ‘‘The great transformer: Examining the role 2022, arXiv:2210.11416.
of large language models in the political economy of AI,’’ Big Data Soc., [59] I. U. Khan, M. A. K. Raiaan, K. Fatema, S. Azam, R. U. Rashid,
vol. 8, no. 2, Jul. 2021, Art. no. 205395172110477. S. H. Mukta, M. Jonkman, and F. De Boer, ‘‘A computer-aided

[34] M. Onat Topal, A. Bas, and I. van Heerden, ‘‘Exploring transformers diagnostic system to identify diabetic retinopathy, utilizing a modified
in natural language generation: GPT, BERT, and XLNet,’’ 2021, compact convolutional transformer and low-resolution images to reduce
arXiv:2102.08036. computation time,’’ Biomedicines, vol. 11, no. 6, p. 1566, May 2023.

26870 VOLUME 12, 2024



M. A. K. Raiaan et al.: Review on Large Language Models

[60] P. Liu, W. Yuan, J. Fu, Z. Jiang, H. Hayashi, and G. Neubig, ‘‘Pre-train, [82] H. Naveed, A. U. Khan, S. Qiu, M. Saqib, S. Anwar, M. Usman,
prompt, and predict: A systematic survey of promptingmethods in natural N. Akhtar, N. Barnes, and A. Mian, ‘‘A comprehensive overview of large
language processing,’’ ACM Comput. Surv., vol. 55, no. 9, pp. 1–35, language models,’’ 2023, arXiv:2307.06435.
2023. [83] G. Jawahar, B. Sagot, and D. Seddah, ‘‘What does BERT learn about the

[61] W. Ansar, S. Goswami, A. Chakrabarti, and B. Chakraborty, ‘‘A novel structure of language?’’ in Proc. 57th Annu. Meeting Assoc. Comput. Lin-
selective learning based transformer encoder architecture with enhanced guistics, 2019, pp. 3651–3657.
word representation,’’ Appl. Intell., vol. 53, no. 8, pp. 9424–9443, [84] J. Ni, G. Hernández Ábrego, N. Constant, J. Ma, K. B. Hall, D. Cer, and
Apr. 2023. Y. Yang, ‘‘Sentence-t5: Scalable sentence encoders from pre-trained text-

[62] G. Dar, M. Geva, A. Gupta, and J. Berant, ‘‘Analyzing transformers in to-text models,’’ 2021, arXiv:2108.08877.
embedding space,’’ 2022, arXiv:2209.02535. [85] Y. Li et al., ‘‘Competition-level code generation with AlphaCode,’’

[63] D. Hazarika, M. Namazifar, and D. Hakkani-Tür, ‘‘Attention bias- Science, vol. 378, no. 6624, pp. 1092–1097, Dec. 2022.
ing and context augmentation for zero-shot control of encoder– [86] Y. Koizumi, Y. Ohishi, D. Niizumi, D. Takeuchi, and M. Yasuda, ‘‘Audio
decoder transformers for natural language generation,’’ in Proc. AAAI captioning using pre-trained large-scale language model guided by audio-
Conf. Artif. Intell., 2022, vol. 36, no. 10, pp. 10738–10748. based similar caption retrieval,’’ 2020, arXiv:2012.07331.

[64] J. Lu, J. Yao, J. Zhang, X. Zhu, H. Xu, W. Gao, C. Xu, T. Xiang, and [87] W. Fan, Z. Zhao, J. Li, Y. Liu, X.Mei, Y.Wang, Z.Wen, F.Wang, X. Zhao,
L. Zhang, ‘‘SOFT: Softmax-free transformer with linear complexity,’’ in J. Tang, and Q. Li, ‘‘Recommender systems in the era of large language
Proc. Adv. Neural Inf. Process. Syst., vol. 34, 2021, pp. 21297–21309. models (LLMs),’’ 2023, arXiv:2307.02046.

[65] L. Floridi and M. Chiriatti, ‘‘GPT-3: Its nature, scope, limits, and [88] Y. Bai, J. Yi, J. Tao, Z. Tian, Z. Wen, and S. Zhang, ‘‘Fast end-to-
consequences,’’Minds Mach., vol. 30, no. 4, pp. 681–694, Dec. 2020. end speech recognition via non-autoregressive models and cross-modal

[66] X. Zheng, C. Zhang, and P. C. Woodland, ‘‘Adapting GPT, GPT-2 knowledge transferring from BERT,’’ IEEE/ACM Trans. Audio, Speech,
and BERT language models for speech recognition,’’ in Proc. IEEE Language Process., vol. 29, pp. 1897–1911, 2021.
Autom. Speech Recognit. Understand. Workshop (ASRU), Dec. 2021, [89] C. Sun, J. Li, Y. R. Fung, H. P. Chan, T. Abdelzaher, C. Zhai, and
pp. 162–168. H. Ji, ‘‘Decoding the silent majority: Inducing belief augmented social

[67] Y. Liu, M. Ott, N. Goyal, J. Du, M. Joshi, D. Chen, O. Levy, M. Lewis, graph with large language model for response forecasting,’’ 2023,
L. Zettlemoyer, and V. Stoyanov, ‘‘RoBERTa: A robustly optimized arXiv:2310.13297.
BERT pretraining approach,’’ 2019, arXiv:1907.11692. [90] K. Drossos, S. Gharib, P. Magron, and T. Virtanen, ‘‘Language modelling

[68] A. Roberts, C. Raffel, and N. Shazeer, ‘‘How much knowledge can you for sound event detection with teacher forcing and scheduled sampling,’’
pack into the parameters of a language model?’’ 2020, arXiv:2002.08910. 2019, arXiv:1907.08506.

[69] A. Chowdhery et al., ‘‘PaLM: Scaling language modeling with path- [91] S.-H. Chiu and B. Chen, ‘‘Innovative bert-based reranking language
ways,’’ 2022, arXiv:2204.02311. models for speech recognition,’’ in Proc. IEEE Spoken Lang. Tech-

[70] R. Thoppilan et al., ‘‘LaMDA: Language models for dialog applications,’’ nol. Workshop (SLT), Jan. 2021, pp. 266–271.
2022, arXiv:2201.08239. [92] A. Elhafsi, R. Sinha, C. Agia, E. Schmerling, I. A. D. Nesnas, and

[71] A. Zeng, X. Liu, Z. Du, Z. Wang, H. Lai, M. Ding, Z. Yang, Y. Xu, M. Pavone, ‘‘Semantic anomaly detection with large language models,’’
W. Zheng, X. Xia, W. L. Tam, Z. Ma, Y. Xue, J. Zhai, W. Chen, Auto. Robots, vol. 47, no. 8, pp. 1035–1055, Dec. 2023.
P. Zhang, Y. Dong, and J. Tang, ‘‘GLM-130B: An open bilingual pre- [93] Y. Shen, J. Shao, X. Zhang, Z. Lin, H. Pan, D. Li, J. Zhang, and
trained model,’’ 2022, arXiv:2210.02414. K. B. Letaief, ‘‘Large language models empowered autonomous edge AI

[72] J. W. Rae et al., ‘‘Scaling language models: Methods, analysis & insights for connected intelligence,’’ 2023, arXiv:2307.02779.
from training gopher,’’ 2021, arXiv:2112.11446. [94] H. Abdel-Jaber, D. Devassy, A. A. Salam, L. Hidaytallah, and

[73] O. Lieber, O. Sharir, B. Lenz, and Y. Shoham, ‘‘Jurassic-1: Technical M. El-Amir, ‘‘A review of deep learning algorithms and their applications
details and evaluation,’’White Paper. AI21 Labs, vol. 1, p. 9, 2021. in healthcare,’’ Algorithms, vol. 15, no. 2, p. 71, Feb. 2022.

[74] S. Smith, M. Patwary, B. Norick, P. LeGresley, S. Rajbhandari, J. Casper, [95] B. Peng, C. Li, P. He, M. Galley, and J. Gao, ‘‘Instruction tuning with
Z. Liu, S. Prabhumoye, G. Zerveas, V. Korthikanti, E. Zhang, R. Child, GPT-4,’’ 2023, arXiv:2304.03277.
R. Yazdani Aminabadi, J. Bernauer, X. Song, M. Shoeybi, Y. He, [96] J. Vig and Y. Belinkov, ‘‘Analyzing the structure of attention in a
M. Houston, S. Tiwary, and B. Catanzaro, ‘‘Using DeepSpeed and transformer language model,’’ 2019, arXiv:1906.04284.
megatron to train megatron-turing NLG 530B, a large-scale generative [97] A. McGowan, Y. Gui, M. Dobbs, S. Shuster, M. Cotter, A. Selloni,
language model,’’ 2022, arXiv:2201.11990. M. Goodman, A. Srivastava, G. A. Cecchi, and C. M. Corcoran,

[75] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux, ‘‘ChatGPT and bard exhibit spontaneous citation fabrication during
T. Lacroix, B. Rozière, N. Goyal, E. Hambro, F. Azhar, A. Rodriguez, psychiatry literature search,’’ Psychiatry Res., vol. 326, Aug. 2023,
A. Joulin, E. Grave, and G. Lample, ‘‘LLaMA: Open and efficient Art. no. 115334.
foundation language models,’’ 2023, arXiv:2302.13971. [98] R. Taylor, M. Kardas, G. Cucurull, T. Scialom, A. Hartshorn, E. Saravia,

[76] T. Thi Nguyen, C. Wilson, and J. Dalins, ‘‘Fine-tuning llama 2 large A. Poulton, V. Kerkez, and R. Stojnic, ‘‘Galactica: A large language
language models for detecting online sexual predatory chats and abusive model for science,’’ 2022, arXiv:2211.09085.
texts,’’ 2023, arXiv:2308.14683. [99] N. Shazeer, ‘‘GLU variants improve transformer,’’ 2020,

[77] G. Penedo, Q. Malartic, D. Hesslow, R. Cojocaru, A. Cappelli, H. Alobei- arXiv:2002.05202.
dli, B. Pannier, E. Almazrouei, and J. Launay, ‘‘The RefinedWeb dataset [100] N. Du, Y. Huang, A. M. Dai, S. Tong, D. Lepikhin, Y. Xu, M. Krikun,
for falcon LLM: Outperforming curated corpora with web data, and web Y. Zhou, A. W. Yu, and O. Firat, ‘‘GLaM: Efficient scaling of language
data only,’’ 2023, arXiv:2306.01116. models with mixture-of-experts,’’ in Proc. Int. Conf. Mach. Learn., 2022,

[78] J. Hoffmann et al., ‘‘Training compute-optimal large language models,’’ pp. 5547–5569.
2022, arXiv:2203.15556. [101] S. Black, S. Biderman, E. Hallahan, Q. Anthony, L. Gao, L. Golding,

[79] S. Zhang, S. Roller, N. Goyal, M. Artetxe, M. Chen, S. Chen, C. Dewan, H. He, C. Leahy, K. McDonell, J. Phang, M. Pieler, U. Sai Prashanth,
M. Diab, X. Li, X. Victoria Lin, T. Mihaylov, M. Ott, S. Shleifer, S. Purohit, L. Reynolds, J. Tow, B. Wang, and S. Weinbach,
K. Shuster, D. Simig, P. Singh Koura, A. Sridhar, T. Wang, and ‘‘GPT-NeoX-20B: An open-source autoregressive language model,’’
L. Zettlemoyer, ‘‘OPT: Open pre-trained transformer language models,’’ 2022, arXiv:2204.06745.
2022, arXiv:2205.01068. [102] E. Nijkamp, B. Pang, H. Hayashi, L. Tu, H. Wang, Y. Zhou, S. Savarese,

[80] J. Wei, X. Wang, D. Schuurmans, M. Bosma, F. Xia, E. Chi, Q. V. Le, and C. Xiong, ‘‘CodeGen: An open large language model for code with
and D. Zhou, ‘‘Chain-of-thought prompting elicits reasoning in large multi-turn program synthesis,’’ 2022, arXiv:2203.13474.
language models,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 35, 2022, [103] T. Hagendorff, S. Fabi, andM. Kosinski, ‘‘Thinking fast and slow in large
pp. 24824–24837. language models,’’ 2022, arXiv:2212.05206.

[81] W. Zeng et al., ‘‘PanGu-α: Large-scale autoregressive pretrained [104] P. P. Ray, ‘‘ChatGPT: A comprehensive review on background, applica-
Chinese language models with auto-parallel computation,’’ 2021, tions, key challenges, bias, ethics, limitations and future scope,’’ Internet
arXiv:2104.12369. Things Cyber-Phys. Syst., vol. 3, pp. 121–154, Jan. 2023.

VOLUME 12, 2024 26871



M. A. K. Raiaan et al.: Review on Large Language Models

[105] X.-Q. Dao, ‘‘Performance comparison of large language models on [128] M. Sallam, ‘‘ChatGPT utility in healthcare education, research, and
VNHSGE English dataset: OpenAI chatGPT, Microsoft bing chat, and practice: Systematic review on the promising perspectives and valid
Google bard,’’ 2023, arXiv:2307.02288. concerns,’’ Healthcare, vol. 11, no. 6, p. 887, Mar. 2023.

[106] D. Kelly, Y. Chen, S. E. Cornwell, N. S. Delellis, A. Mayhew, [129] M. Cascella, J. Montomoli, V. Bellini, and E. Bignami, ‘‘Evaluating the
S. Onaolapo, and V. L. Rubin, ‘‘Bing chat: The future of search engines?’’ feasibility of ChatGPT in healthcare: An analysis of multiple clinical and
Proc. Assoc. Inf. Sci. Technol., vol. 60, no. 1, pp. 1007–1009, Oct. 2023. research scenarios,’’ J. Med. Syst., vol. 47, no. 1, p. 33, Mar. 2023.

[107] Z. Yang, Z. Dai, Y. Yang, J. Carbonell, R. R. Salakhutdinov, and [130] T. H. Kung, M. Cheatham, A. Medenilla, C. Sillos, L. De Leon,
Q. V. Le, ‘‘XLNet: Generalized autoregressive pretraining for language C. Elepaño, M. Madriaga, R. Aggabao, G. Diaz-Candido, J. Maningo,
understanding,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 32, 2019. and V. Tseng, ‘‘Performance of ChatGPT on USMLE: Potential for

[108] X. Song, G. Wang, Z. Wu, Y. Huang, D. Su, D. Yu, and H. Meng, AI-assisted medical education using large language models,’’ PLOS
‘‘Speech-XLNet: Unsupervised acoustic model pretraining for self- Digit. Health, vol. 2, no. 2, Feb. 2023, Art. no. e0000198.
attention networks,’’ 2019, arXiv:1910.10387. [131] Y. Gu, R. Tinn, H. Cheng, M. Lucas, N. Usuyama, X. Liu, T. Naumann,

[109] W. Shen, J. Chen, X. Quan, and Z. Xie, ‘‘DialogXL: All-in-one J. Gao, and H. Poon, ‘‘Domain-specific language model pretraining
XLNet for multi-party conversation emotion recognition,’’ in Proc. AAAI for biomedical natural language processing,’’ ACM Trans. Comput.
Conf. Artif. Intell., vol. 35, no. 15, 2021, pp. 13789–13797. Healthcare, vol. 3, no. 1, pp. 1–23, Oct. 2021.

[110] R. Luo, L. Sun, Y. Xia, T. Qin, S. Zhang, H. Poon, and T.-Y. Liu, [132] Z. Kraljevic, D. Bean, A. Shek, R. Bendayan, H. Hemingway, and J. Au,
‘‘BioGPT: Generative pre-trained transformer for biomedical text gen- ‘‘Foresight-generative pretrained transformer (GPT) for modelling of
eration and mining,’’ Briefings Bioinf., vol. 23, no. 6, Nov. 2022, patient timelines using EHRs,’’ 2022, arXiv:2212.08072.
Art. no. bbac409. [133] L. Mich and R. Garigliano, ‘‘ChatGPT for e-tourism: A technological

[111] D. Deutsch, J. Juraska, M. Finkelstein, and M. Freitag, ‘‘Training and perspective,’’ Inf. Technol. Tourism, vol. 25, no. 1, pp. 1–12, Mar. 2023.
meta-evaluating machine translation evaluation metrics at the paragraph [134] X. Yu, Z. Chen, Y. Ling, S. Dong, Z. Liu, and Y. Lu, ‘‘Temporal
level,’’ 2023, arXiv:2308.13506. data meets LLM—Explainable financial time series forecasting,’’ 2023,

[112] A. Ushio, F. Alva-Manchego, and J. Camacho-Collados, ‘‘Genera- arXiv:2306.11025.
tive language models for paragraph-level question generation,’’ 2022, [135] G. F. Frederico, ‘‘ChatGPT in supply chains: Initial evidence of
arXiv:2210.03992. applications and potential research agenda,’’ Logistics, vol. 7, no. 2, p. 26,

[113] (2023). OpenAI. Accessed: Sep. 12, 2023. [Online]. Available: Apr. 2023.
https://openai.com/blog/openai-api [136] A. Sobieszek and T. Price, ‘‘Playing games with ais: The limits of

[114] (2023). Huggingface. Accessed: Sep. 12, 2023. [Online]. Available: GPT-3 and similar large language models,’’ Minds Mach., vol. 32, no. 2,
https://huggingface.co/docs/transformers/index pp. 341–364, Jun. 2022.

[115] (2023). Google Cloud. Accessed: Sep. 12, 2023. [Online]. Available: [137] M. U. Hadi, R. Qureshi, A. Shah, M. Irfan, A. Zafar, M. B. Shaikh,
https://cloud.google.com/natural-language N. Akhtar, J. Wu, and S. Mirjalili, ‘‘Large language models: A

[116] (2023). Azure. Accessed: Sep. 12, 2023. [Online]. Available: comprehensive survey of its applications, challenges, limitations, and

https://azure.microsoft.com/en-us/products/ai-services/ai-language future prospects,’’ Tech. Rep., 2023.
[138] C. K. Lo, ‘‘What is the impact of ChatGPT on education? A rapid review

[117] IBM. (2023). IBM Watson Natural Language Understanding. Accessed: of the literature,’’ Educ. Sci., vol. 13, no. 4, p. 410, Apr. 2023.
Sep. 12, 2023. [Online]. Available: https://www.ibm.com/

[139] Y. K. Dwivedi, N. Kshetri, L. Hughes, E. L. Slade, A. Jeyaraj,
products/natural-language-understanding

A. K. Kar, A. M. Baabdullah, A. Koohang, V. Raghavan, and M. Ahuja,
[118] G. Satyanarayana, J. Bhuvana, and M. Balamurugan, ‘‘Sentimental ‘‘‘So what if chatgpt wrote it?’ multidisciplinary perspectives on

analysis on voice using AWS comprehend,’’ in Proc. Int. Conf. Com- opportunities, challenges and implications of generative conversational ai
put. Commun. Informat. (ICCCI), Jan. 2020, pp. 1–4. for research, practice and policy,’’ Int. J. Inf. Manage., vol. 71, Jul. 2023,

[119] A. Kolides, A. Nawaz, A. Rathor, D. Beeman, M. Hashmi, S. Fatima, Art. no. 102642.
D. Berdik, M. Al-Ayyoub, and Y. Jararweh, ‘‘Artificial intelligence foun- [140] M. Zong and B. Krishnamachari, ‘‘A survey on GPT-3,’’ 2022,
dation and pre-trainedmodels: Fundamentals, applications, opportunities, arXiv:2212.00857.
and social impacts,’’ Simul. Model. Pract. Theory, vol. 126, Jul. 2023, [141] R. Zhu, X. Tu, and J. X. Huang, ‘‘Utilizing BERT for biomedical and
Art. no. 102754. clinical text mining,’’ in Data Analytics in Biomedical Engineering and

[120] S. M. Jain, ‘‘Hugging face,’’ in Introduction to Transformers for Healthcare. Amsterdam, The Netherlands: Elsevier, 2021, pp. 73–103.
NLP: With Hugging Face Library Models to Solve Problems. Cham, [142] K. Huang, A. Singh, S. Chen, E. T. Moseley, C.-Y. Deng, N. George,
Switzerland: Springer, 2022, pp. 51–67. and C. Lindvall, ‘‘Clinical XLNet: Modeling sequential clinical notes and

[121] J.Wang, X. Hu,W. Hou, H. Chen, R. Zheng, Y.Wang, L. Yang, H. Huang, predicting prolonged mechanical ventilation,’’ 2019, arXiv:1912.11975.
W. Ye, X. Geng, B. Jiao, Y. Zhang, and X. Xie, ‘‘On the robustness [143] J. Zhang, L. Wang, R. K. W. Lee, Y. Bin, Y. Wang, J. Shao, and E. P. Lim,
of ChatGPT: An adversarial and out-of-distribution perspective,’’ 2023, ‘‘Graph-to-tree learning for solving math word problems,’’ in Proc. 58th
arXiv:2302.12095. Annu. Meeting Assoc. Comput. Linguistics, 2020, pp. 3928–3937.

[122] S. Chen, Y. Li, S. Lu, H. Van, H. J. Aerts, G. K. Savova, and [144] X. Dai, S. Karimi, B. Hachey, and C. Paris, ‘‘Cost-effective selection of
D. S. Bitterman, ‘‘Evaluation of ChatGPT family of models for pretraining data: A case study of pretraining BERT on social media,’’
biomedical reasoning and classification,’’ 2023, arXiv:2304.02496. 2020, arXiv:2010.01150.

[123] H. Huang, O. Zheng, D. Wang, J. Yin, Z. Wang, S. Ding, H. Yin, [145] S. Biswas, ‘‘The function of chat GPT in social media: Accord-
C. Xu, R. Yang, Q. Zheng, and B. Shi, ‘‘ChatGPT for shaping the ing to chat GPT,’’ Mar. 2023. [Online]. Available: http://dx.doi.org/
future of dentistry: The potential of multi-modal large language model,’’ 10.2139/ssrn.4405389
Int. J. Oral Sci., vol. 15, no. 1, p. 29, Jul. 2023. [146] R. Peng, K. Liu, P. Yang, Z. Yuan, and S. Li, ‘‘Embedding-based

[124] V. Sorin, E. Klang, M. Sklair-Levy, I. Cohen, D. B. Zippel, N. Balint retrieval with LLM for effective agriculture information extracting from
Lahat, E. Konen, and Y. Barash, ‘‘Large language model (ChatGPT) as a unstructured data,’’ 2023, arXiv:2308.03107.
support tool for breast tumor board,’’ NPJ Breast Cancer, vol. 9, no. 1, [147] S. Biswas, ‘‘Importance of chat GPT in agriculture: According
p. 44, May 2023. to chat GPT,’’ Mar. 2023. [Online]. Available: http://dx.doi.org/

[125] A. J. Thirunavukarasu, D. S. J. Ting, K. Elangovan, L. Gutierrez, T. F. Tan, 10.2139/ssrn.4405391
and D. S. W. Ting, ‘‘Large language models in medicine,’’ Nature Med., [148] M. A. K. Raiaan, N. M. Fahad, S. Chowdhury, D. Sutradhar, S. S. Mihad,
vol. 29, no. 8, pp. 1930–1940, 2023. and M. M. Islam, ‘‘IoT-based object-detection system to safeguard

[126] D. M. Korngiebel and S. D. Mooney, ‘‘Considering the possibil- endangered animals and bolster agricultural farm security,’’ Future
ities and pitfalls of generative pre-trained transformer 3 (GPT-3) Internet, vol. 15, no. 12, p. 372, Nov. 2023.
in healthcare delivery,’’ npj Digit. Med., vol. 4, no. 1, p. 93, [149] T. Pires, E. Schlinger, and D. Garrette, ‘‘How multilingual is multilingual
Jun. 2021. BERT?’’ 2019, arXiv:1906.01502.

[127] L. De Angelis, F. Baglivo, G. Arzilli, G. P. Privitera, P. Ferragina, [150] A. Conneau, K. Khandelwal, N. Goyal, V. Chaudhary, G. Wenzek,
A. E. Tozzi, and C. Rizzo, ‘‘ChatGPT and the rise of large language F. Guzmán, E. Grave, M. Ott, L. Zettlemoyer, and V. Stoyanov,
models: The new AI-driven infodemic threat in public health,’’ Frontiers ‘‘Unsupervised cross-lingual representation learning at scale,’’ 2019,
Public Health, vol. 11, Apr. 2023, Art. no. 1166120. arXiv:1911.02116.

26872 VOLUME 12, 2024



M. A. K. Raiaan et al.: Review on Large Language Models

[151] V. Sanh, L. Debut, J. Chaumond, and T. Wolf, ‘‘DistilBERT, a [173] Z. Sun, ‘‘A short survey of viewing large language models in legal
distilled version of BERT: Smaller, faster, cheaper and lighter,’’ 2019, aspect,’’ 2023, arXiv:2303.09136.
arXiv:1910.01108. [174] Y. Meng, M. Michalski, J. Huang, Y. Zhang, T. Abdelzaher, and J. Han,

[152] Z. Lan, M. Chen, S. Goodman, K. Gimpel, P. Sharma, and R. Soricut, ‘‘Tuning language models as training data generators for augmentation-
‘‘ALBERT: A lite BERT for self-supervised learning of language enhanced few-shot learning,’’ in Proc. Int. Conf. Mach. Learn., 2023,
representations,’’ 2019, arXiv:1909.11942. pp. 24457–24477.

[153] T. Bolukbasi, K.-W. Chang, J. Y. Zou, V. Saligrama, and A. T. Kalai, [175] S. Fincke, S. Agarwal, S. Miller, and E. Boschee, ‘‘Language
‘‘Man is to computer programmer as woman is to homemaker? Debiasing model priming for cross-lingual event extraction,’’ in Proc. AAAI
word embeddings,’’ in Proc. Adv. Neural Inf. Process. Syst., vol. 29, Conf. Artif. Intell., 2022, vol. 36, no. 10, pp. 10627–10635.
2016. [176] N. M. Fahad, S. Sakib, M. A. Khan Raiaan, and Md. S. Hossain

[154] Y. Zhang, S. Sun, M. Galley, Y.-C. Chen, C. Brockett, X. Gao, J. Gao, Mukta, ‘‘SkinNet-8: An efficient CNN architecture for classifying
J. Liu, and B. Dolan, ‘‘DialoGPT: Large-scale generative pre-training for skin cancer on an imbalanced dataset,’’ in Proc. Int. Conf. Electr.,
conversational response generation,’’ 2019, arXiv:1911.00536. Comput. Commun. Eng. (ECCE), Feb. 2023, pp. 1–6.

[155] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, [177] N. Jain, K. Saifullah, Y. Wen, J. Kirchenbauer, M. Shu, A. Saha,
A. Neelakantan, P. Shyam, G. Sastry, and A. Askell, ‘‘Language models M. Goldblum, J. Geiping, and T. Goldstein, ‘‘Bring your own
are few-shot learners,’’ in Proc. NIPS, 2020, pp. 1877–1901. data! Self-supervised evaluation for large language models,’’ 2023,

[156] J. Lee, W. Yoon, S. Kim, D. Kim, S. Kim, C. H. So, and J. Kang, arXiv:2306.13651.
‘‘BioBERT: A pre-trained biomedical language representation model for [178] X. Zhu, J. Li, Y. Liu, C. Ma, and W. Wang, ‘‘A survey on model
biomedical text mining,’’ Bioinformatics, vol. 36, no. 4, pp. 1234–1240, compression for large language models,’’ 2023, arXiv:2308.07633.
Feb. 2020. [179] L. Xue, N. Constant, A. Roberts, M. Kale, R. Al-Rfou, A. Siddhant,

[157] Y. Gat, N. Calderon, A. Feder, A. Chapanin, A. Sharma, and R. Reichart, A. Barua, and C. Raffel, ‘‘MT5: A massively multilingual pre-trained
‘‘Faithful explanations of black-box NLP models using LLM-generated text-to-text transformer,’’ 2020, arXiv:2010.11934.
counterfactuals,’’ 2023, arXiv:2310.00603. [180] N. Ratner, Y. Levine, Y. Belinkov, O. Ram, I. Magar, O. Abend,

[158] M. Josifoski, M. Sakota, M. Peyrard, and R. West, ‘‘Exploiting E. Karpas, A. Shashua, K. Leyton-Brown, and Y. Shoham, ‘‘Parallel
asymmetry for synthetic training data generation: SynthIE and the case context windows for large language models,’’ 2022, arXiv:2212.10947.
of information extraction,’’ 2023, arXiv:2303.04132. [181] F. Motoki, V. Pinho Neto, and V. Rodrigues, ‘‘More human than human:

[159] M. S. H. Mukta, J. Ahmad, M. A. K. Raiaan, S. Islam, S. Azam, Measuring ChatGPT political bias,’’ Public Choice, vol. 2023, pp. 1–21,
M. E. Ali, and M. Jonkman, ‘‘An investigation of the effectiveness of Aug. 2023.
deepfake models and tools,’’ J. Sensor Actuator Netw., vol. 12, no. 4, [182] K. Werder, B. Ramesh, and R. Zhang, ‘‘Establishing data provenance
p. 61, Aug. 2023. for responsible artificial intelligence systems,’’ ACM Trans. Man-

[160] A. Awasthi, N. Gupta, B. Samanta, S. Dave, S. Sarawagi, and P. Talukdar, age. Inf. Syst., vol. 13, no. 2, pp. 1–23, Jun. 2022.
‘‘Bootstrapping multilingual semantic parsers using large language [183] J. Jiang, X. Liu, and C. Fan, ‘‘Low-parameter federated learning with
models,’’ 2022, arXiv:2210.07313. large language models,’’ 2023, arXiv:2307.13896.

[161] P. Sridhar, A. Doyle, A. Agarwal, C. Bogart, J. Savelka, and M. Sakr, [184] W. S. Saba, ‘‘Towards explainable and language-agnostic LLMs: Sym-
‘‘Harnessing LLMs in curricular design: Using GPT-4 to support bolic reverse engineering of language at scale,’’ 2023, arXiv:2306.00017.
authoring of learning objectives,’’ 2023, arXiv:2306.17459. [185] Z. Zhang, A. Zhang, M. Li, H. Zhao, G. Karypis, and A. Smola,

[162] M. A. K. Raiaan, A. Al Mamun, Md. A. Islam, M. E. Ali, and ‘‘Multimodal chain-of-thought reasoning in language models,’’ 2023,
Md. S. H. Mukta, ‘‘Envy prediction from Users’ photos using arXiv:2302.00923.
convolutional neural networks,’’ in Proc. Int. Conf. Comput., Electr. Com- [186] Z. Liu, Y. Zhang, P. Li, Y. Liu, and D. Yang, ‘‘Dynamic LLM-agent
mun. Eng. (ICCECE), Jan. 2023, pp. 1–7. network: An LLM-agent collaboration framework with agent team

[163] E.Waisberg, J. Ong,M.Masalkhi, and A. G. Lee, ‘‘Large language model optimization,’’ 2023, arXiv:2310.02170.
(LLM)-driven chatbots for neuro-ophthalmic medical education,’’ Eye, [187] U. Iqbal, T. Kohno, and F. Roesner, ‘‘LLM platform security: Applying a
vol. 2023, pp. 1–3, Sep. 2023. systematic evaluation framework to OpenAI’s ChatGPT plugins,’’ 2023,

[164] W. Channell, ‘‘Making a difference: The role of the LLM in policy arXiv:2309.10254.
formulation and reform,’’ in The Export of Legal Education. Evanston,
IL, USA: Routledge, 2016, pp. 13–21. MOHAIMENUL AZAM KHAN RAIAAN

[165] P. Budhwar et al., ‘‘Human resource management in the age of generative received the Bachelor of Science degree in
artificial intelligence: Perspectives and research directions on ChatGPT,’’ computer science and engineering from United
Hum. Resource Manage. J., vol. 33, no. 3, pp. 606–659, Jul. 2023. International University (UIU), in 2023. Currently,

[166] G. Fatouros, J. Soldatos, K. Kouroumali, G. Makridis, and D. Kyriazis, he is a Research Assistant with the Computer
‘‘Transforming sentiment analysis in the financial domain with Chat- Science and Engineering Department, UIU.
GPT,’’Mach. Learn. Appl., vol. 14, Dec. 2023, Art. no. 100508. His professional pursuits are marked by active

[167] Y. Li, S. Ma, X. Wang, S. Huang, C. Jiang, H.-T. Zheng, P. Xie, F. Huang, involvement in diverse research areas, such as
and Y. Jiang, ‘‘EcomGPT: Instruction-tuning large language models with computer vision, health informatics, explainable
chain-of-task tasks for e-commerce,’’ 2023, arXiv:2308.06966. artificial intelligence, and graph optimization.

[168] P. Weingart, T. Wambsganss, and M. Soellner, ‘‘A taxonomy for deriving Notably, he has made significant contributions to the field, as evidenced by
business insights from user-generated content,’’ ECIS, Res. Papers 401, his multiple research articles published in prestigious journals indexed by
2023. [Online]. Available: https://aisel.aisnet.org/ecis2023_rp/401 Scopus and categorized under the Q1 ranking.

[169] L. Zhu, X. Xu, Q. Lu, G. Governatori, and J. Whittle, ‘‘AI and
ethics—Operationalizing responsible AI,’’ in Humanity Driven AI: Pro- MD. SADDAM HOSSAIN MUKTA received
ductivity, Well-being, Sustainability and Partnership. Cham, Switzerland: the Ph.D. degree from the Data Science and
Springer, 2022, pp. 15–33.

Engineering Research Laboratory (Data Labo-
[170] I. Molenaar, S. D. Mooij, R. Azevedo, M. Bannert, S. Järvelä,

and D. Gašević, ‘‘Measuring self-regulated learning and the role of ratory), BUET, in 2018. He is a Postdoctoral
AI: Five years of research using multimodal multichannel data,’’ Researcher with the LUT School of Engineering
Comput. Hum. Behav., vol. 139, Feb. 2023, Art. no. 107540. Sciences, Lappeenranta, Finland. He was an

[171] M. C. Rillig, M. Ågerstrand, M. Bi, K. A. Gould, and U. Sauerland, Associate Professor and a Undergraduate Program
‘‘Risks and benefits of large language models for the environment,’’ Coordinator with the Department of Computer
Environ. Sci. Technol., vol. 57, no. 9, pp. 3464–3466, Mar. 2023. Science and Engineering, United International

[172] B. Liu, B. Xiao, X. Jiang, S. Cen, X. He, and W. Dou, ‘‘Adversarial University, Bangladesh. He has a number of
attacks on large language model-based system and mitigating strategies: quality publications in both national and international conferences and
A case study on ChatGPT,’’ Secur. Commun. Netw., vol. 2023, pp. 1–10, journals. His research interests include deep learning, machine learning, data
Jun. 2023. mining, and social computing.

VOLUME 12, 2024 26873



M. A. K. Raiaan et al.: Review on Large Language Models

KANIZ FATEMA received the bachelor’s degree JUBAER AHMAD received the B.Sc. degree
in computer science and engineering from Daf- in computer science and engineering from
fodil International University, Dhaka, Bangladesh. United International University (UIU), Dhaka,
She is currently a Research Assistant (RA) Bangladesh, in 2022. He is currently a Research
with Charles Darwin University. She is actively Assistant with the IAR Project, UIU. His research
involved in research activities, especially in health interests include computer vision, NLP, big data,
informatics, computer vision, machine learning, and distributed learning.
deep learning, and artificial intelligence-based
systems. She has published several research papers
in journals (Scopus) and international conferences.

NUR MOHAMMAD FAHAD received the bach-
elor’s degree from the Department of Computer
Science and Engineering, United International
University (UIU), Bangladesh. During the bach-
elor’s study, he has contributed to the academic
community as an Undergraduate Teaching Assis- MOHAMMED EUNUS ALI is a Professor with
tant with the Department of Computer Science

the Department of CSE, Bangladesh University
and Engineering, UIU. In addition to his teaching

of Engineering and Technology (BUET), where
role, he has deeply engaged in cutting-edge

he is also the Group Leader of the Data Science
research across several domains, including com-

and Engineering Research Laboratory (DataLab).
puter vision, machine learning, deep learning, health informatics, graph

His research papers have published in top ranking
theory, and mental health modeling.

journals and conferences, such as the VLDB
Journal, IEEE TRANSACTIONS ON KNOWLEDGE AND

SADMAN SAKIB received the bachelor’s degree DATA ENGINEERING, DMKD, Information Systems
in computer science and engineering from the Journal, WWWJ, DKE, ICDE, CIKM, EDBT,
Department of Computer Science and Engineer- PVLDB, and UbiComp. His research interests include database systems
ing, United International University, Bangladesh, and information management, including spatial databases, practical machine
in 2023. He was a Teaching Assistant of learning, and social media analytics. He served as a Program Committee
undergraduate students with the Department of Member for many prestigious conferences, including SIGMOD, VLDB,
Computer Science and Engineering, United Inter- AAAI, and SIGSPATIAL.
national University. Besides this, he is actively
involved in machine learning, deep learning,
artificial intelligence, computer vision, and health
informatics research.

MOST MARUFATUL JANNAT MIM is currently
pursuing the degree with the Computer Science
and Engineering Department, United International SAMI AZAM is a leading Researcher and a
University (UIU). She is actively involved in Professor with the Faculty of Science and Technol-
research activities related to computer vision, ogy, Charles Darwin University, Australia. He is
deep learning, graph theory, and human–computer actively involved in the research fields relating
interaction. Her passion lies in pioneering inno- to computer vision, signal processing, artificial
vative research in computer science. Apart from intelligence, and biomedical engineering. He has a
studies, she is involved in co-curricular activities number of publications in peer-reviewed journals
with the UIU APP Forum, where she is also the and international conference proceedings.

President and demonstrates strong leadership by organizing various seminars
and workshops for computer science students.

26874 VOLUME 12, 2024