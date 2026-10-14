---
source_file: "2022- Unsupervised machine learning in urban studies A systematic review.txt"
original_rel_path: "Trabalhos\Artigos\Apoio pontual\txt\2022- Unsupervised machine learning in urban studies A systematic review.txt"
category: "Artigos_Apoio_pontual"
extension: ".txt"
sha256: "830a0dbd1a5f0f66edb3c0eae7b06a4a1de8aa907fcd0d9f06a744bb7a4a752b"
extracted_at: "2026-09-20T00:05:05.552702"
---

﻿Cities 129 (2022) 103925

Contents lists available at ScienceDirect 

Cities 
journal homepage: www.elsevier.com/locate/cities 

Unsupervised machine learning in urban studies: A systematic review 
of applications 
Jing Wang a, Filip Biljecki a,b,* 

a Department of Architecture, National University of Singapore, Singapore 
b Department of Real Estate, National University of Singapore, Singapore   

A R T I C L E  I N F O   A B S T R A C T   

Keywords: Unsupervised learning (UL) has a long and successful history in untangling the complexity of cities. As the 
GeoAI counterpart of supervised learning, it discovers patterns from intrinsic data structures without crafted labels, 
Urban planning which is believed to be the key to real AI-generated decisions. This paper provides a systematic review of the use 
GIScience of UL in urban studies based on 140 publications. Firstly, the topic, technique, application, data type, and 
Urban data science 
k-means evaluation method of each paper are recorded, deriving statistical insights into the evolution and trends. Clus
Latent Dirichlet allocation tering is the most prominent method, followed by topic modeling. With the strong momentum of deep learning, a 

growing application field of UL methods is representing the complex real-world urban systems at multiple scales 
through multi-source data integration. Subsequently, a detailed review discusses how UL is applied in a broad 
range of urban topics, which are concluded by four dominant themes: urbanization and regional studies, built 
environment, urban sustainability, and urban dynamics. Finally, the review addresses common limitations 
regarding data quality, subjective interpretation, and validation difficulty of the results, which increasingly 
require interdisciplinary knowledge. Research opportunities are found in the rapidly evolving technological 
landscape of UL and in certain domains where supervised learning dominates.   

1. Introduction predictive models to estimate unknown values and explain relationships 
among phenomena. While supervised methods have proven to be useful 

Cities, the most sophisticated creation of people, are believed to have for a wide range of applications and datasets, they do not purport to 
hidden patterns in their physical forms and day-to-day functioning answer all research questions, and various challenges remain, e.g. 
(Batty, 2008; Bettencourt & West, 2010). The growing availability of obtaining training data as the real-world urban data is largely unlabeled 
urban data and machine learning techniques that enable automatic (Zheng et al., 2014). 
pattern recognition from massive datasets have gained momentum in Another broad category of machine learning, unsupervised learning 
serving researchers to untangle the complexity of cities, thereby (UL) infers patterns from unlabeled data, unleashing further potential of 
informing urban interventions and giving rise to data-driven planning making sense of dynamic and massive datasets in urban studies. In 
(Athey, 2017). For example, they have been used routinely to monitor contrast to supervised learning (SL), these techniques pay no attention to 
urban change (Schneider, 2012), evaluate socio-economic well-being structured semantic relationships, and therefore, are suitable to be 
(Jean et al., 2016), and assess our physical surroundings (Doersch et al., applied to heterogeneous data such as text, imagery, audio, and video 
2012; Ito & Biljecki, 2021). (Jain, 2010). Unlike supervised learning, which manually presets a goal 

Machine learning has been integral to urban studies for myriads of to predict outcomes, unsupervised learning determines what is relevant 
purposes, and the permutations of techniques and datasets that have based on data features (El Bouchefry & de Souza, 2020), providing new 
permeated the field are seemingly endless. As evident by the reviews of perspectives for urban studies beyond human's a priori knowledge. In 
Grekousis (2019) and Ullah et al. (2020), most applications of machine this regard, unsupervised machine learning is believed to be the 
learning in urban studies rely on supervised techniques. In such ap pathway to real artificial intelligence (Bengio et al., 2013), which 
proaches, workflows rely on a sample of input (training) data that is fundamentally understands the world around us and is the key to AI- 
labeled with known values or categories. These are used to develop generated design and policies. Under the prevailing trend of 

* Corresponding author at: Department of Architecture, National University of Singapore, Singapore. 
E-mail addresses: wangjing@u.nus.edu (J. Wang), filip@nus.edu.sg (F. Biljecki).  

https://doi.org/10.1016/j.cities.2022.103925 
Received 23 December 2021; Received in revised form 2 August 2022; Accepted 5 August 2022   
Available online 15 August 2022
0264-2751/© 2022 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).



J. Wang and F. Biljecki                                                                                                                                                                                                               C  i t i e  s  129 (2022) 103925

interdisciplinary GeoAI research (Janowicz et al., 2020; Liu & Biljecki, decomposition, and neural networks. To better demonstrate their ca
2022), UL is instrumental in learning spatial representations and se pabilities from a practical perspective, we use an urban dataset which 
mantic enrichment of spatial data infrastructure (Huang et al., 2022; contains multiple representative urban data types as case study. The 
Jenkins et al., 2019). selected dataset is on listings on Airbnb in Singapore with their prop

While they have been overshadowed by the popularity and uptake of erties (e.g. type of listing, number of bedrooms, and price) and reviews 
supervised learning techniques, unsupervised counterparts also have a (text and numerical scores). The data is courtesy of Inside Airbnb,1 a 
long and successful relationship with studying cities, as we will confirm project that provides open data that quantifies the impact of short-term 
in this paper. They have been instrumental in uncovering patterns from rentals on housing and residential communities, and it is frequently used 
growing urban datasets and untangling their complexities: for many in research (Gurran et al., 2018; Li & Biljecki, 2019). 
years, methods such as hierarchical clustering analysis (HCA) and 
principal component analysis (PCA) were recognized to be crucial in a 2.1. Clustering 
diverse set of investigations include evaluating built environment 
quality (Bonaiuto et al., 2003) and suburban study (Mikelbank, 2004). Clustering is the most established subcategory of UL, which identifies 
Over the past two decades, UL methods have prospered across a wider subgroups within a raw, unlabeled dataset by similarities and differ
spectrum of urban studies and related domains, and the volume of ences in features (Jain, 2010). There are multiple clustering techniques, 
publications featuring them has expanded remarkably, as we will show with k-means (Hartigan & Wong, 1979) being the most prominent one. 
in this review paper. Among others, UL techniques support studies in the In this method, clustering is done by moving centroids and assigning 
domain of assessing urbanization processes (Cottineau et al., 2017), points closest to a given centroid into the same group. In such a case, 
investigating travel patterns (Sun & Axhausen, 2016), understanding data points within a cluster share common properties whereas differ
sustainability and ecology (Richards & Tuncer, 2018), semantic mean ences among clusters are clear. The number of clusters is specified by the 
ing extraction of urban spaces (Gao et al., 2017), urban perception user. 
(Capela & Ramirez-Marquez, 2019), quality assessment of spatial data Fig. 2 demonstrates a k-means clustering on the dataset, the data 
(Jacobs & Mitchell, 2020), and analyzing energy performance (Oh & points are divided into four groups based on two dimensions of infor
Kim, 2019). Such diffusion of UL applications is associated with the mation. The input dimensions of clustering algorithm can be more than 
proliferation of diversity and volume of urban data, and the rapid ad two, in fact, one of the most common applications of UL in urban studies, 
vancements of UL techniques and their ease of use (e.g. accessible as identified by our review, is clustering by multi-dimension features for 
implementations). The trend is expected to continue, as AI scientists discovering typologies (Section 5). Fig. 3 gives an example to this 
posit that UL will become even more important in the future (LeCun application — Airbnb data points are clustered by four features, deriving 
et al., 2015). However, despite their demonstrated importance, signifi 4 typologies distributed across the city. 
cance, and growing uptake in urban studies, no comprehensive review More clustering techniques covered in this review include hierar
was conducted to summarize UL applications in the urban context and chical clustering analysis (HCA), which reveals the hierarchical struc
understand trends, a gap which we seek to bridge in this paper. This void ture of clusters, density-based spatial clustering of applications with 
is in contrast with other fields, such as biomedical research and building noise (DBSCAN) (Ester et al., 1996), which is location-aware and suit
performance analysis, in which the role of unsupervised learning has able for spatial data, spectral clustering (Ng et al., 2001), affinity 
been subject of reviews (Miller et al., 2018; Xu & Wunsch, 2010). propagation (AP) (Frey & Dueck, 2007), and Gaussian mixture model 

In this paper, we systematically review the use of unsupervised (GMM) (Zivkovic, 2004). 
learning in urban studies, with a highlight on the state of the art of the 
main techniques and their applicability in a broad range of topics. We 2.2. Decomposing signals 
hope to provide informative resources to researchers seeking to leverage 
UL for research related to cities, but also have this review to double as a This category summarizes techniques that extract feature compo
reference for researchers who are yet to become acquainted with such nents from composite signals (e.g. image, text, numeric value), the result 
techniques. We define the scope of urban studies as: urbanization and of which is high-dimensional data being mapped onto a low dimensional 
regional studies, built environment, urban sustainability, and urban space while retaining internal structure (reduction of dimensionality) 
dynamics (Fig. 1), four themes that have largely been the focus of urban (Blei et al., 2003; Lever et al., 2017). One representative technique is 
research or initiatives over the past decades. principal component analysis (PCA) (Wold et al., 1987), which com

In Section 2, we provide a high-level overview of unsupervised presses datasets through linear transforming input variables into 
learning and its capabilities. Section 3 describes the methodology of this “principal components”, i.e. new data representations composed of 
systematic review, while Section 4 offers statistical insights to the input variables. 
reviewed papers. The wide spectrum of UL applications is discussed in Through PCA, we are able to visualize the four-dimensional features 
Section 5, where the contents are adherent to the four thematic urban of Airbnb typologies in a two-dimensional space (Fig. 4). The four fea
study groups. Further, in Section 6, we reflect on the common patterns in tures are “compressed” and represented by two principal components, 
this study area, limitations of unsupervised methods, implementation, the colored axes indicate their directions. In practice, PCA is generally 
and future opportunities. Finally, Section 7 concludes the paper. performed before clustering for simplifying the interpretation of multi- 

dimensional data. It is also effective in identifying the most salient 
2. Unsupervised learning background features. 

Another popular technique is latent Dirichlet allocation (LDA) (Blei 
It is beneficial to give an introduction to unsupervised learning, et al., 2003), which generates explicit representations of collections of 

clarifying its aims and what tasks it is suited for, together with an discrete data (e.g. text corpus) by topics, i.e. lists of weighted observa
overview of methods. The major difference between the UL and SL is tions. It is often applied for topic modeling tasks, for example, discov
whether the model uses known values as supervisory signals. That is, ering latent topics discussed on social networks. It facilitates 
supervised learning uses labeled data to infer patterns and train a model understanding people's perception of the environment from volunteered 
to label unseen data, while unsupervised learning uses only unlabeled data such as neighborhood reviews (Hu et al., 2019). 
data, and does so for the purpose of discovering patterns, e.g. grouping We present the topic modeling result on the reviews of rental listings 
similar features. It is often employed in applications where labeling is 
expensive or where it is not relevant. 

Here we introduce three general categories: clustering, signal 1 http://insideairbnb.com/. 

2



J. Wang and F. Biljecki                                                                                                                                                                                                               C  i t i e  s  129 (2022) 103925

Fig. 1. Urban study topics can be categorized into the four thematic groups. This review examines the applications of unsupervised learning techniques in providing 
insights spanning the landscape of urban studies. 

Fig. 2. k-means clustering on Singapore Airbnb price and review score, results 
in 4 groups. 

Fig. 3. k-means clustering on Singapore Airbnb features (capacity, number of 
bedrooms, price, and review scores), results in 4 typologies. Basemap: (c) 

in Fig. 5 — ten major topics are discovered and each of them contains a OpenStreetMap contributors. 
series of weighted relevant terms. In the selected topic, the most char
acteristic words include “place”, “mrt” (metro system), “convenient”, the flowing and interactions of signals across layers, it has the ability to 
indicating the importance of particular topics to guests. To make the model complex non-linear relationships that are common in real-world 
LDA result sensible to the non-experts, it generally requires human problems (Schmidhuber, 2015). 
interpretation. Self-organizing map (SOM) (Kohonen, 1990) is a classical shallow 

The applications of signal decomposition techniques are versatile neural network, which associates the neurons in input layer and output 
compared to clustering, for example, it is widely adopted for anomaly neurons that summarize many observations in a two-dimensional grid 
detection, feature extraction, topic modeling, and change detection map (Fig. 6). The training process is similar to clustering, i.e. neurons 
tasks. Other related techniques include latent semantic analysis (LSA) compete with others to group around closest centroid neurons. 
(Landauer et al., 1998) and t-distributed stochastic neighbor embedding Compared to k-means clustering, SOM does not require preset cluster 
(t-SNE) (van der Maaten & Hinton, 2008). number, the neurons will gravitate toward the natural clusters learned 

from the data structure. Therefore, it is suitable for learning and visu
2.3. Unsupervised neural networks alizing patterns in datasets that have large variations. 

Deep neural network with more hidden layers has been gaining 
Unsupervised neural networks are an active research field of UL strong momentum recently. Representative models include autoencoder 

techniques, which advanced rapidly thanks to the progress in deep (AE) (Hinton & Salakhutdinov, 2006) and generative adversarial 
learning. Artificial neural networks are comprised of three types of node network (GAN) (Goodfellow et al., 2014). 
layers — input layer, multiple hidden layers, and output layer. Through AE leverages neural networks to learn representations for input data 

3



J. Wang and F. Biljecki                                                                                                                                                                                                               C  i t i e  s  129 (2022) 103925

3. Methodology 

3.1. Overview 

To identify papers employing UL in urban studies, we follow the 
PRISMA protocol of systematic review (Moher et al., 2009) following the 
practices of recent reviews in the field (Biljecki & Ito, 2021; Zhao et al., 
2021). First, we conducted a systematic search using reproducible syn
tax in a bibliographic database, fetching an initial literature pool of 668 
papers. The relevancy of the papers were further examined based on 
several criteria through manual screening, 140 papers are included for 
this review. The details of the two steps are described in the following 
subsections. 

3.2. Searching methods 

We performed a search for relevant papers in the Web of Science 
(WOS) database. The search syntax consists of two groups of keywords. 
The first set zeroes in on papers that pertain to cities and the urban 

Fig. 4. PCA applied on the short-term rental dataset. The 4-dimensional fea context, while the second one aims to delineate publications that engage 
tures are reduced to two. 

while ignoring insignificant noise (encoding), further reconstructing the 
data through the learned features (decoding) (Fig. 7). Through 
comparing the reconstructed data with the input data, the model per
formance can be evaluated. During the encode-decode process, it can 
compress the data with minimal reconstruction error, detect the most 
salient features and anomalies, and generate new data that is similar to 
the input, i.e. make predictions. 

GAN uses a discriminator to produce self-supervision signals for fine- 
tuning results from a randomized generator, therefore is able to produce 
new data output as realistic as the original input (Fig. 8). It catalyzes the 
development of applications such as image-to-image translation, video 
prediction, 3D object generation, and so forth (Wu & Biljecki, 2022). 
Restricted Boltzmann machine (RBM) (Hinton et al., 2006) is also 
included in this review. 

Fig. 6. Architecture of self-organizing map (SOM).  

Fig. 5. Discovering 10 Airbnb review topics through LDA. The red color highlights the selected topic and its corresponding terms frequencies. (For interpretation of 
the references to color in this figure legend, the reader is referred to the web version of this article.) 

4



J. Wang and F. Biljecki                                                                                                                                                                                                               C  i t i e  s  129 (2022) 103925

In the same way as the previously published reviews in the field 
(Ibrahim et al., 2020; Ma et al., 2019), we included only peer-reviewed 
papers written in English and published in academic journals, finally 
collecting 668 papers that range from 1996 to 2021 (until 19 October 
2021, when the final search was executed). The full search syntax is 
attached in Appendix A. 

3.3. Inclusion criteria 

After deriving the initial literature pool, we proceeded to manually 
select those that are relevant for our review: we screened the titles, 
abstracts, and keywords of papers to assess their relevance to our 
context. We established the following criteria that a paper should meet 
to be considered relevant for this review.  

1. The study is conducted in an urban or peri-urban area.  
Fig. 7. Architecture of Autoencoder (AE).  2. It is predominantly an urban studies paper, which represents or 

predicts the patterns in an urban system. To clarify the fuzzy 
meaning and ameliorate the blurry boundaries of our area of focus, 

unsupervised learning. Their intersection signifies the focus of our we summarized four fundamental and trending thematic groups in 
review. urban analytics and practices. The included papers should belong to 

For the first group, we set the expression “urban* OR city”. The one of the following themes:  
asterisk expands the search to include variations of the key search terms, (a) Urbanization and regional study: the divergence and change of 
covering words such as urbanization and urbanism. Since these terms cities that are shaped by economic, social and political powers at 
appear frequently in articles from other fields that are not in the focus of the macro level (Brenner, 2013). It can either be a physical 
this review (e.g. computer science and medicine), it was an imperative process (e.g. land use change) or reflected in socio-economic 
to narrow the search scope. Deriving a more focused result was well-being.  
accomplished by limiting the search to the following subject categories (b) Built environment: the human-made physical space in which 
in WOS: Environmental Studies, Geography Physical, Green Sustainable people live, work and recreate on a daily basis (Roof & Oleru, 
Science Technology, Geography, Engineering Civil, Urban Studies, and 2008). Typical examples are building blocks, streets, and public 
Regional Urban Planning. spaces. 

The second set of keywords aims to identify articles that use unsu (c) Urban sustainability: collection of study topics such as biodi
pervised learning methods. At first, we followed the same approach as versity, ecosystem service, air pollution, and heat island effect 
UL review in other field (Li, Shepperd, & Guo, 2020), using ‘unsuper (Verma & Raghubanshi, 2018). Such insights help cities to 
vised OR unlabeled’, yet the results suggested that almost all papers develop in a sustainable and resilient manner.  
belong to the field of remote sensing, with the exception of a small (d) Urban dynamics: monitoring and predicting the patterns of 
number of articles published in the last two years. This is an interesting people's activity, traffic flow and utilities demand (Gao, 2015), 
phenomenon: the term “unsupervised” dominates the field of remote leading to smarter urban management or business decisions. 
sensing, but it is often not found explicitly in other sub-areas of urban 
research. To ensure the diversity of the literature pool, we re-ran an Our review (Section 5) gives specific examples of how UL is 
exploratory search in Google Scholar and found that the relevant articles employed in each of these themes.  
rather specified the techniques used in the abstract or keywords (e.g. 
PCA, k-means clustering), which belong to the large umbrella of unsu 3. The paper is using one or more unsupervised methods. This step was 
pervised methods. Therefore, we added the UL techniques listed in crucial, as we have encountered a number of papers that happen to 
Section 2 to the search syntax in WOS. Note that because too many contain the same acronym as an UL technique but carrying a 
papers apply PCA for dimensionality reduction without producing in different meaning.  
sights, this review will focus on its use for feature extraction. For a more 4. Unsupervised learning is the primary analysis method. This criterion 
thorough review on PCA and spatial data, the reader is referred to the is necessary to keep only papers in which UL techniques predomi
paper of Demšar et al. (2013). nate. For example, papers that use UL only for minor or peripheral 

Fig. 8. Architecture of generative adversarial network (GAN).  

5



J. Wang and F. Biljecki                                                                                                                                                                                                               C  i t i e  s  129 (2022) 103925

tasks such as data pre-processing or comparative study are not Table 1 
considered to meet this criterion and are thus excluded from Examples of information extraction.  
consideration.  Relevant Extracted information 

5. The methods proposed in the study are tested on real-world datasets publication 
Category Application Data type Technique 

instead of being purely theoretical, generating substantial insights type 
for researchers or implications for practitioners. 

(Akande Urban Factor Numeric Hierarchical 
et al., sustainability extraction clustering 

Following the screening of the papers in the initial pool, we took 2019) 
forward 140 papers that satisfy the criteria above. (Delmelle, Urbanization Clustering Numeric Multiple 

2017) and regional 
4. Results and overview study 

(Gao et al., Built Topic Multi- LDA 
2017) environment modeling source 

The papers selected for this review turned out to focus on a variety of (Samany, Built Feature Image RBM 
urban challenges and feature a diverse set of approaches, datasets and 2019) environment extraction 
tools, affirming the permeation of unsupervised learning through urban (Hu et al., Urban dynamics Clustering Image DBSCAN 

studies (Fig. 9). This section describes the general trends and insights of 2015) 
(Chen et al., Urban dynamics Prediction Spatio- Autoencoder  

the reviewed papers, based on a set of information extracted during 2021) temporal 
review (Table 1). Fig. 10 indicates the temporal evolution of unsuper
vised learning permeating through urban studies, and the change in 
share of each research category. Recently, there is a clear upsurge in the exclusive (e.g. topic modeling with clustering). However, we believe this 
number of publications, which has increased fivefold from 2016 to level of detail in categorization is necessary for outlining the funda
2021. With relevant papers proliferating rapidly, it is necessary and mental objectives of UL applications. The result suggests a steady growth 
timely to summarize previous works and follow up with recent of research relying on clustering, which is associated with the overall 
advances. growth of paper volume. Topic modeling is an observable emerging 

Regarding the share of categories, there are notable differences topic with a considerable proportion of papers published in recent three 
among them — the number of papers related to Urban Dynamics is twice years. This growth may be linked to the proliferation of readily available 
of those pertaining to Urban Sustainability. It is also worth noting that geo-tagged text data such as social media posts and Point of Interest 
although the application in Urban Dynamics started later than in other (POI) data (Huang & Li, 2019; Wang & Taylor, 2019). It is also note
areas, it has gained considerable attention in recent five years. Aside worthy that there is a new subset of papers inspecting prediction ap
from that, Built Environment has always been a field of interest, e.g. plications, virtually all of which focusing on traffic prediction (Chen 
Owen et al. (2006) use a clustering algorithm in an early investigation of et al., 2021; Ranjan et al., 2021; Zhang et al., 2021), with just one 
automatic land cover classification. exception that simulates urban growth and housing dispersal by 

In Fig. 11, we break down the annual publications by their applica Generative Adversarial Network (GAN) (Ibrahim et al., 2021). 
tion types. The categorization of the applications is determined through Deriving from the data structure, the analysis result of unsupervised 
summarizing common types from multiple related studies (Jing & Tian, learning has a close connection with the input data. The numerous 
2019; Miller et al., 2018; Usama et al., 2019), while fine-tuning ac permutations of data types and methods create a very diverse landscape 
cording to the contents in the literature pool. Note that due to the nu of research in this topic. In Fig. 12 we extract three core features that 
ances in underlying techniques, the eight types are not mutually characterize a study: category, application, and the data type been used, 

Fig. 9. Conceptual structure of the reviewed papers by correspondence analysis of keywords. Incidentally, unsupervised learning methods are useful in bibliometrics, 
e.g. clustering a large set of papers and establishing categories. The figure is created by an R package developed by Aria and Cuccurullo (2017). 

6



J. Wang and F. Biljecki                                                                                                                                                                                                               C  i t i e  s  129 (2022) 103925

Fig. 10. The upsurge of relevant publications, and the share of each category. The papers were collected in October 2021.  

Fig. 11. The annual prevalence of publications by application type.  

revealing the share and relationships among the feature segments. The uses. 
first key observation is that clustering is the most common practice for On the technical side, unsupervised methods are supported by the 
papers in all categories, especially is a substantial component in studies mainstream programming languages, including R, Python, Java, Matlab, 
about urbanization and sustainability making up more than 80 % of the and so forth, which often enable such functionalities through well- 
total. Second, for Urban Dynamics and Built Environment, the shares of documented and popular machine learning packages. They are mostly 
other applications such as topic modeling, feature extraction, and pre open-source, and there appears to be no dominant language in the field. 
diction are relatively higher. Because they are emerging applications, Among others, we feature the most frequent one — R. The base R (using 
the corresponding research categories are expected to gain a stronger it ‘out of the box’ without packages) supports PCA and k-means clus
momentum of innovation. The third observation comes from the data tering, as used in the example in Section 3. Further techniques are 
type. Unsupervised learning can be successfully applied to a wide vari implemented thanks to packages, e.g. the kohonen package supports 
ety of urban data (Table 2), and there is no data type that is predomi SOM training and visualization. However, the functions of R packages 
nantly popular. A subset of studies relies on multi-source data. Thanks to supporting unsupervised learning appear to be limited as among them 
the wide applicability, researchers use unsupervised method as a bridge over two thirds deal with clustering-related issues on numeric values, 
to connect multiple datasets, which introduces more perspectives to the while missing input data types such as image and spatio-temporal data. 
analysis process while mitigating the bias caused by reliance on a single In contrast, Python is backed by a wide range of machine learning li
data source (Cai et al., 2019; Devkota et al., 2019; Vizzari & Sigura, braries and can be applied in myriad ways. For example, there is an 
2015). integrated machine learning package for various supervised and unsu

The technical aspect is also important to cover. For each study, we pervised algorithms — scikit-learn (Pedregosa et al., 2011), and 
have noted the specific techniques and programming languages, about gensim package, which support the review topic modeling example 
one-third of the authors reveal such information. Fig. 13 illustrates the shown in Section 3. On top of that, thanks to the integration with a deep 
findings: the top 3 frequent techniques — k-means, Self-organizing learning environment, Python is able to process high-level features of a 
maps, and DBSCAN — are essentially all for clustering data, with only large amount of data. For example, Singh and Mohan (2019) train a 
a few exceptions that use SOM in extracting spatio-temporal features stacked autoencoder for generating the deep representation of road 
(Liu, Zhang, & Long, 2019; Oldoni et al., 2015; Sohn, 2013). The next traffic videos, Comber et al. (2020) extract visual features (e.g. number 
most frequent technique is latent Dirichlet allocation, which is primarily of stores) from building frontage images, with the help of autoencoder 
used for topic modeling. In fact, most of the techniques only have a capturing the most salient characteristics required to reconstruct the 
single type of application, except for autoencoder which serves versatile image. 

7



J. Wang and F. Biljecki                                                                                                                                                                                                               C  i t i e  s  129 (2022) 103925

Fig. 12. The share and relationship among publication segments. In this review, data type “spatial” represents static geographic objects such as building footprints, 
while “spatial-temporal” indicates data that record human or traffic movements such as GPS trajectory. For detailed implications of each data type, please refer 
to Table 2. 

5. Review 
Table 2 
Urban data sources identified in our review together with example studies.  5.1. Urban sustainability 

Data type Data source Example paper 

Numeric Census (Serra et al., 2014) Considering that the evaluation of urban sustainability largely relies 
Survey (social, economic, (Tu & Lin, 2008) on quantifying environmental or geographic indicators (Keirstead & 
environmental…) Leach, 2008), a common use case of unsupervised learning in this 
Numeric attributes (Li, Han, et al., 2019) 
Meteorological data (Xu et al., 2020) domain is clustering geographical units (i.e. cells and administrative 
Sensor data (Honjo et al., 2015) zones) according to features from those indicators. A recurring related 

Text Social media post (Steiger et al., 2016) area of study is ecosystem services (ESs), which means the benefits 
Online review (Olson et al., 2021) humans obtain either directly or indirectly from ecosystems (e.g. food 
News and advertisement (Capela & Ramirez- production, nutrient retention) (Lyu et al., 2019). The results of studies 

Marquez, 2019) 
Image Satellite imagery (Feng & Liu, 2013) in this domain are ES bundles — the joint spatial distribution of 

Street view imagery (SVI) (Wijnands et al., 2019) ecosystem services, based on multi-sourced datasets that consist of land 
Geotagged photos (Hu et al., 2015) use, climate, census, and geographical data, in where unsupervised 

Spatial Point of Interest (POI) (Pavlis et al., 2018) learning identifies and clusters geographic units that have common 
Building footprints (Jochem et al., 2021) 
Land use/land cover (LULC) (Owen et al., 2006) high-dimensional features (Karimi et al., 2021; Lyu et al., 2019; Yang 
Nighttime Lights (Devkota et al., 2019) et al., 2019). The ES bundles act as ideal units of visualizing their spatial 
LiDAR point cloud (Aljumaily et al., 2017) distribution, studying temporal changes (Yang et al., 2019), analyzing 

Spatio- GPS trajectory (Wang et al., 2018) spatial trade-offs and synergies (Karimi et al., 2021), and identifying 
temporal Traffic flow (Chen et al., 2021) effective environmental protection strategies (Lyu et al., 2019). Other 

Smart card (Sun & Axhausen, 2016) 
Call records (Sagl et al., 2014) than identifying similar patterns in environmental metrics, Richards and 
Cellular data (Kim, 2020b) Tuncer (2018) experiment with using unsupervised learning for assess

Sound and Sound record (Oldoni et al., 2015) ing cultural values of nature depend on social media photos. First, a step 
video Traffic video (Singh & Mohan, 2019) using computer vision (implemented in Google Cloud Vision) generates 

Multi-source – (Cai et al., 2019) 
– (Gao et al., 2017)  specific object labels from nature photographs, and second, hierarchical 

clustering summarizes the unstructured labels into 7 distinct groups. It is 
estimated that this unsupervised workflow can save 170 h of manual 

Finally, we provide a comprehensive list of the reviewed papers in work on human-assigned subject classification. 
Appendix B. The table in the appendix contains the extracted informa Moreover, the clusters with distinct environmental features may 
tion supporting the analysis, and the papers are organized by the tax serve as foundation for exploratory multivariate analysis that studies the 
onomy of data type. relationship between human activities and environmental outcomes 

(Ferrara et al., 2017; Schmiedel et al., 2015). For example, after classi
fying Italian municipalities into homogeneous partitions by forest cover 
indicators, Ferrara et al. (2017) summarize social indicators by the 

8



J. Wang and F. Biljecki                                                                                                                                                                                                               C  i t i e  s  129 (2022) 103925

Fig. 13. The breakdowns of unsupervised learning technique and used programming language.  

clusters, and through discriminant analysis, the authors point to agri change (e.g. farmland shift into built-up area). Since there are hardly 
culture, income, education, and the labor market as key predictors of any cities that have detailed land use registries over a long temporal 
forest cover. Although the limitation of this method is evident, i.e. the range, researchers in this domain mostly develop their own land use and 
degree of human impact on the environment has not been quantified, land cover classifications based on satellite imagery (Naikoo et al., 2020; 
the results can simplify indicators selection in future statistical learning Owen et al., 2006; Xu et al., 2012; Ye & Chen, 2015). Though this issue is 
tasks. widely explored by supervised classifiers, unsupervised learning pre

As urban sustainability is a common objective for cities around the sents a complementary avenue, which is especially useful in a common 
world, many of the studies have been focusing on assessing and situation where suitable reference data (e.g. current land use map) is not 
comparing sustainable development across cities. The conventional se available (Ye & Chen, 2015). Moreover, without manually setting digital 
lection and weighting processes for sustainability evaluation can be references that generally requires prior knowledge, the economic and 
subjective to human bias (Paulvannan Kanmani et al., 2020), therefore, professional barriers of unsupervised method are lower (Johnson & Xie, 
researchers use unsupervised learning for automating the extraction of 2011). In performing such tasks, researchers engage unsupervised 
key factors that indicate sustainability (Akande et al., 2019; Martins learning to extract the most representative spectral information from 
et al., 2021). In addition, unsupervised learning is practical in satellite images (Xu et al., 2012), cluster pixels or grids by internal ho
comparing the environmental performance among cities or countries mogeneity and external heterogeneity of spectral values (Naikoo et al., 
(Amaral et al., 2021; Lu et al., 2015; Paulvannan Kanmani et al., 2020). 2020; Qi et al., 2019). Because this field of study is closely related to 
For example, Paulvannan Kanmani et al. (2020) apply SOM, a technique remote sensing, technical explorations on improving model perfor
that maps and visualizes the high-dimensional data onto two- mance are active, including utilization of luminance and saturation in
dimensional output space while preserving their relative distance, on formation (Ye & Chen, 2015), and applying LDA to enhance the 
10 environmental indicators of 180 countries, results in a map of nodes semantic correlation of the multitemporal image scenes (Du et al., 
that inform the countries' relative locations of sustainable development. 2018). 

Further, on the temporal aspect, unsupervised learning is proven The demographic and socioeconomic transitions have been subject 
valuable in capturing the environmental dynamics and natural hazards of the urbanization discourse as well, in which machine learning plays 
due to its simplicity and capability of enhancing the information on an important role. Many studies concentrate on neighborhood change, 
changes. One particular use case is monitoring urban forest and vege essentially relying on census and survey data collected in past decades 
tation conditions, which can be carried out by unsupervised classifica and using clustering methods to summarize the vectors of change (e.g. 
tion of vegetation indices derived from multi-temporal satellite data gentrification, depopulation etc.) (Delmelle, 2017; Dias & Silver, 2021; 
(Krtalic et al., 2021). Another research area is related to disasters such as Li & Xie, 2018; Liu, Deng, et al., 2019; Serra et al., 2014; Yuan et al., 
flooding. Peng et al. (2021) propose a framework of large-scale unsu 2021). For example, in a nation-wide study of 50 American metropolitan 
pervised urban flood mapping, in which auto-encoder learns the areas, Delmelle (2017) introduces SOM to summarize neighborhoods by 
multidimensional features of both pre- and post-flood patches for com their similarity onto a two-dimensional output space, simplifying the 
parison, while Xu et al. (2018) generate the urban flood map of 5 risk large and high-dimensional census datasets into the distinct groups of 
levels through clustering flood related features. Thanks to being able to the neighborhood change trajectories. Compared with the threshold- 
save time from human-annotated training data, results from such based method that is commonly used in social studies, Liu, Deng, et al. 
methods may be used in real-time to inform emergency humanitarian (2019) argue that unsupervised learning avoids arbitrariness, yet is less 
assistance and disaster relief (Peng et al., 2021). For further studies on intuitive to interpret the result as there are no preset rules that follow 
environmental change see (Tessler et al., 2016) and (Kropp, 1998). theoretical guidelines. 

Lastly, there are numbers of papers zero in on urban thermal envi Another topic in this domain is regional typology studies, which is 
ronment (Kwon et al., 2021; Xu et al., 2020; Zawadzka et al., 2021), the aimed to demonstrate the divergent states of development across cities 
application type of which also falls into clustering multi-sourced data and suburbs. Thanks to the versatile applicability of unsupervised 
such as temperature, humidity, building density, and ground surface. learning to a variety of data structures, the regional typologies have 
Among them, we feature the work of Kwon et al. (2021), which dis been investigated from multiple perspectives include social-economic 
covers the unfavourable and favourable thermal areas cities based on powers (Arribas-Bel et al., 2013; Baum et al., 2006), development con
sensible heat flux data through k-means clustering, the resulting zoning ditions (Cabrera-Barona et al., 2020; Rahman et al., 2019), urban form 
map may inform associated sustainable energy policies. (Lemoine-Rodriguez et al., 2020), and hybrid features (Mikelbank, 

2004; Fiaschetti et al., 2021). We emphasize the work of Arribas-Bel 
5.2. Urbanization and regional study et al. (2013), which visualizes the relative socio-economic locations and 

movements of 35 global cities on a hex grid coordinates plane, and 
The process of urbanization can be directly reflected by land use suggest using this unsupervised mapping technique as a supporting 

9



J. Wang and F. Biljecki                                                                                                                                                                                                               C  i t i e  s  129 (2022) 103925

toolbox of informed decisions. multilevel structural maps that may support strategic planning of eco
Considering the fuzzy spatial boundaries between urban centres, nomic clusters. 

urban, and natural or rural areas, researchers have also resorted to un Unsupervised learning is also useful in helping researchers to un
supervised learning for automating the segmentation of different ur derstand our physical surroundings, by automatically extracting or 
banized areas, eventually generating urban spatial maps that show reconstructing the most salient visual features encoded in the images (e. 
planners and policymakers the potential areas for future development. A g. street view imagery (SVI)). The purposes of studies under this topic 
common pathway is clustering urban-rural diagnostic features such as are quite diverse, including investigating visual characteristics that 
nighttime light intensity and fluctuation (Feng et al., 2020), land use affect the quality of a space (Comber et al., 2020; Wu et al., 2020), 
(Vizzari & Sigura, 2015), travel pattern (Ozus et al., 2012), and multi constructing urban appearance libraries (Nguyen et al., 2020; Tae
variate statistics (Arribas-Bel & Schmidt, 2013). For comparison among charungroj & Mathayomchan, 2020), and generating design interven
cluster methods, one can refer to the work by Fusco and Perez (2019). tion based on learnt features (Wijnands et al., 2019). Traditionally, such 
There is also a special case that is not relying on clustering: Kit et al. tasks are arduous, largely relying on field surveys and manually dis
(2012) outline urban slums only through detecting lacunarity in satellite tinguishing the variety of visual cues. Supervised learning is able to 
images by PCA and line detection algorithm. annotate properties of large image collections. There are papers using 

Finally, although the number of related studies is small, we would supervised image labeling services such as Google Cloud Vision (Tae
like to highlight that advances in urban growth prediction have been charungroj & Mathayomchan, 2020) and SegNet (Wu et al., 2020) in 
brought by unsupervised learning (Feng & Liu, 2013; Ibrahim et al., combination with unsupervised methods that reduce the dimensionality 
2021). In an experiment in Qatar, Ibrahim et al. (2021) use GAN to of the photo labels and find image groups with common characteristics 
simulate urban growth and housing dispersal, the result exhibits a high (topics). However, in studies that require information more specific than 
similarity with historical maps. According to Albert et al. (2018), GAN general labels, supervised learning is found hard to balance between 
can accurately predict future urban growth with a relatively small speed and accuracy (Comber et al., 2020). With the advancement of 
training data set composed of satellite images only. This means with the deep unsupervised models, it is possible to capture visual representa
help of unsupervised learning, realistic simulation of the urban land use tions from images directly without laborious manual labeling. Here we 
displacement is available to the developing countries without under emphasize two enabling algorithms: autoencoder that learns the most 
going the costly compilation of spatial variables in other simulation useful pixel groups traits (e.g. signage, design style, and color) of 
methods. reconstructing the input building frontage images (Comber et al., 2020), 

and GAN that captures key characteristics (e.g. ground texture, tree 
5.3. Built environment density) of SVI from one urban area and translate the style to another 

one (Wijnands et al., 2019). 
Thanks to the ability of unsupervised learning to identify and Apart from urban features, we observe a set of papers focusing on 

disentangle the discriminative information hidden in the milieu of large detecting specific urban objects. One core idea of this practice is to find 
data collection methods, study on social sensing of the real usage of iterated objects, for instance, landmarks that appear frequently in geo
urban spaces from a bottom-up perspective (as the counterpart to top- tagged photos (Samany, 2019) and landscape amenities that be 
down land use plan) (Papadakis et al., 2019) is made possible by repeatedly mentioned in housing advertisements (Su et al., 2021). The 
learning patterns from user-generated data (Gao et al., 2017). This type other approach builds upon LiDAR point cloud data, which exploits the 
of application can be summarized as urban function study. Some studies intrinsic characteristics of the raw 3D points (e.g. proximity, connec
adopt the approach of first finding spatial aggregation of activities by tivity, symmetry) and converts the points into sets of clusters by similar 
travel trajectories and call records (Rios & Munoz, 2017; Tao et al., characteristics (Aljumaily et al., 2017; Xue et al., 2020). Each cluster 
2019; Wang et al., 2021), and then inferring the urban function ac represents certain urban objects such as cars, buildings, and ground 
cording to prior knowledge on behavior patterns, e.g. high and regular surfaces, and the performances of classification are tested to be highly 
activity during weekdays refer office areas (Rios & Munoz, 2017). accurate. In short, unsupervised learning presents scalable and efficient 
However, researchers point out that this method does not capture the frameworks for mapping real-world objects that can be used in building 
true semantics of urban space (Tao et al., 2019). digital twins of cities (Aljumaily et al., 2017; Xue et al., 2020). 

A more popular method is utilizing POI data that both reflects the Another domain worth highlighting is urban morphology study. 
concentration of activities and has embedded semantic information Generally, urban morphology can be represented by a series of numeric 
(Gao et al., 2017; Hu et al., 2020; Jing et al., 2021; Miao et al., 2021; metrics generated from the shapes of buildings, plots, and streets (Bil
Papadakis et al., 2019; Pavlis et al., 2018; Yu et al., 2020; Yuan et al., jecki & Chow, 2022). Because the morphological datasets are high- 
2020; Zhang et al., 2018). In the list, we feature the work of Gao et al. dimensional in nature (e.g. the morphological metrics derived from 
(2017), which develops a statistical framework to help discover building footprint include density, size, shape and so forth (Jochem 
semantically meaningful topics and functional regions based on the co- et al., 2021)), unsupervised learning is more capable of discovering 
occurrence patterns of POI types. The functional regions are grouped underlying common geometric patterns and producing urban form ty
together by similarity in semantic meaning, resulting in a convex pologies than any other method (Abarca-Alvarez et al., 2019; Bobkova 
polygon map with distinct thematic characteristics. The featured tech et al., 2021; Jochem et al., 2021; Oh & Kim, 2019). Specifically, in a 
nique in this study is LDA, which maps the semantic information onto a study across five European cities, Bobkova et al. (2021) identify seven 
vector space, therefore the numeric distance between words can be plot types by clustering plot configurational attributes, enabling scaling- 
calculated and compared, i.e. measuring the semantic similarity of up morphological studies and substantial comparison within and across 
places. It is one of the most powerful techniques in identifying urban regions. The results of such studies are also effective in simplifying 
functions and has been replicated and adapted in other geographical downstream urban analytic tasks. For example, Oh and Kim (2019) 
spaces, for related studies see (Hu et al., 2020; Papadakis et al., 2019; develop 13 building block typologies for energy performance simula
Zhong et al., 2018). tion, providing a building geometric features reference set to urban 

Urban function is entangled with another area of research — urban energy planning and design. Note that in representing the types by 
structure (Cui et al., 2019; Kim, 2020a; Sun et al., 2016; Zhong et al., morphological metrics, researchers often choose the closest values to the 
2018), which can be viewed as a further step of spatial summarization of cluster centroids (Bobkova et al., 2021; Oh & Kim, 2019). 
urban function that reveals concentration pattern, e.g. after generating Besides the aforementioned use cases, the remaining built environ
function zones of London from aggregated tweets, Zhong et al. (2018) ment studies relying on unsupervised learning are quite diverse, 
profile the spatial structure by hierarchical clustering, results in including extracting indicators for environmental quality or livability 

10



J. Wang and F. Biljecki                                                                                                                                                                                                               C  i t i e  s  129 (2022) 103925

assessment (Bo et al., 2019; Bonaiuto et al., 2003; Tu & Lin, 2008), cluster based on density. Moreover, the authors develop a spectral 
establishing typologies of Transit-Oriented-Development stations by clustering workflow that computes image similarity so that photos 
spatio-temporal features (Li, Han, et al., 2019; Liu, Singleton, & Arribas- contain views shared by multiple people are grouped into clusters, and 
Bel, 2020; Sohn, 2013), creating acoustic summary of sound features the photo that is most similar to all others is selected representation of 
from urban environment (Oldoni et al., 2015), and analyzing the the AOI. The results help reveal the growth of cities' attractive regions 
dominant source of noise under various types of land (Chew & Wu, alongside with urban development, may inform the planning of “char
2016). ismatic” destinations. This work also demonstrates the versatility of 

unsupervised learning, as in the same work, it is applied in parallel on 
5.4. Urban dynamics different types of data and the results are combined. Many other studies 

on AOI follow the same two-step workflow, i.e. first identifying AOI 
The rise of the research domain of urban dynamics is associated with clusters, then interpreting the grounds for attractiveness. The approach 

the increasing volume and accessibility of datasets that register indi to the second step varies, besides the aforementioned identification of 
vidual activities at a dynamic pace, e.g. smart card data that traces travel preferable photos, it can also be achieved through topic modeling from 
patterns (Manley et al., 2018), call records and cellular data that imply posts (Huang & Li, 2019) and POI (Li et al., 2021). However, the tech
movements or social interactions (Sagl et al., 2014), and social media nique used in the first step is almost exclusively DBSCAN, with only a 
posts and photos that reflect personal sentiments on urban spaces (Olson single research applying k-means on phone signal data (Sun et al., 2021). 
et al., 2021). Given the complexity and large variety in such datasets, DBSCAN is particularly suitable for AOI extraction for two reasons: (1) 
retrieving key information from them has become challenging (Sun & the number of AOI clusters is hard to estimate but DBSCAN does not 
Axhausen, 2016). This problem is compounded with the lack of prior require such pre-determined number of clusters as k-means clustering 
knowledge on the complex individual behaviors in cities, making su does; and (2) it is solid at detecting clusters with arbitrary shapes (Hu 
pervised learning a less favourable option for analysis. Therefore it is not et al., 2015). However, as unsupervised methods learn patterns from the 
surprising a large number of papers employ unsupervised learning to data structure, researchers point out that the resulting locations may 
discover the interactions among space, time, and individuals from the inherit the location accuracy issue in the input datasets and are not 
high-dimensional spatio-temporal data, i.e. study the collective representative enough for all age groups (Devkota et al., 2019; Huang & 
behavior patterns within cities (Bi & Ye, 2021; Chen et al., 2019; Kim, Li, 2019; Sun et al., 2021). 
2020b; Li, Zhu, & Guo, 2019; Manley et al., 2018; Ouyang et al., 2018; Similarly, there is a set of papers that pay specific attention to human 
Pieroni et al., 2021; Sagl et al., 2014; Sun & Axhausen, 2016; Xing et al., perceptions of space (Cai et al., 2019; Capela & Ramirez-Marquez, 2019; 
2020; Yu et al., 2021; Yu & He, 2017; Yue et al., 2018). Liu, Yin, et al., 2020; Olson et al., 2021; Sparks et al., 2020; Steiger et al., 

Sun and Axhausen (2016) apply tensor decomposition method that 2016). Although all of them deal with text data, there appears to be no 
reproduces the complex dependence and interactions in 14 million predominant methodology or purpose among these studies, thus, we 
transit journeys extracted from smart card data by simple latent struc highlight a few characteristic papers: Steiger et al. (2016) combine SOM 
tures. The decomposition results depict several principle travel patterns with LDA to extract the spatio-temporal aggregation of popular topics 
and their corresponding profiles, e.g. peak hours, origin-destination, and from georeferenced tweets, Capela and Ramirez-Marquez (2019) detect 
age groups, revealing the underlying spatio-temporal structure of topics that compose the “personality” of each city in the electronic 
Singapore. The insight from the study could provide reference to prac media outlets by LDA topic modeling, Liu, Yin, et al. (2020) visualize the 
titioners for fleet management and infrastructure planning. Besides semantic structure of urban regions through embedding the POI-type 
tensor decomposition, clustering techniques are straightforward in onto 2-dimensional space using t-SNE, which preserves semantic rela
dealing with travel data as well. For example, DBSCAN captures clusters tionship among words during dimensionality reduction, and Olson et al. 
in smart card data based on the time and location similarities of indi (2021) exploit autoencoder to learn the compact representations of re
vidual travel behaviors. Compared with k-means clustering, DBSCAN views from Yelp from relatively sparse word usage, and use the repre
considers point density and is therefore capable to identify high density sentations for the ascription of tangible neighborhood change. In 
temporal events that indicative of regular behaviors (Manley et al., addition to the specific applications, the work by Abdul-Rahman et al. 
2018). For related studies on using unsupervised learning in discovering (2021) establishes a general framework to simplify the process of 
travel patterns, see the work by Ouyang et al. (2018); Chen et al. (2019); extracting public sentiment on urban issues from social media, where 
Xing et al. (2020); Pieroni et al. (2021) and Yu et al. (2021). LDA categorises sentiments into major themes such as high rental prices, 

Human activities that represented by mobile phone data is another noise, and social segregation. The code supporting the proposed method 
direction of behavior pattern study. Sagl et al. (2014) characterize is released openly. 
variations in intensity and similarity of collective human activity via Another essential component of urban dynamics is traffic flow. Un
SOM, and Liu, Zhang, and Long (2019) further aggregate human activ supervised learning has been introduced for traffic forecasting since an 
ities with similar characteristics spatially and identify several urban early point, Sun et al. (2006) predict short-term traffic flow by adopting 
vitality areas. In fact, pedestrian traffic measured by cellular activity is a Gaussian mixture model (GMM) to compute the joint probability dis
popular indicator for urban vitality, and unsupervised methods is prove tribution between input traffic and the output (traffic in the next time 
useful in unleashing its latent spatio-temporal features, for relevant interval). The fundamental concept of choosing GMM is events in the 
studies see (Kim, 2020b) and (Guo et al., 2021). The findings from such natural world obey Gaussian distributions. Similarly, Fiez and Ratliff 
studies also help to reveal how collective human activities relate to the (2020) apply GMM in parking demand modeling. However, GMM only 
underlying urban structures, e.g. connections within and between predicts by Gaussian distributions and does not take into account the 
communities (Ghahramani et al., 2019), land use (Manley & Dennett, real complex interconnections in the data. Given the advancements in 
2019), and regional functions (Dong, Wang, & Liu, 2021). deep representation learning (GAN, autoencoder), there is a surge of 

In addition to the behavior pattern portion, unsupervised learning on papers published in 2021 that opt for it for extracting implicit and 
urban dynamics information also helps to uncover the way people complicated traffic features, and compressing the large volume of raw 
perceive and interact with urban spaces. Much of the research aim to data (Chen et al., 2021; Ranjan et al., 2021; Zhang et al., 2021). For 
answer where do people like to visit in cities, that is to pinpoint the Area example, Chen et al. (2021) propose a hybrid forecasting model with 
of Interest (AOI) (Devkota et al., 2019; Hu et al., 2015; Huang & Li, autoencoder embedded, and Zhang et al. (2021) train GAN to learn the 
2019; Li et al., 2021; Liu, Singleton, et al., 2021; Sun et al., 2021). probability distribution of the real historical traffic flow, generate future 

In a study on the evolution of AOI in six cities across ten years, Hu traffic flows through the learned probability distribution. The models in 
et al. (2015) apply DBSCAN to geotagged Flickr photos to extract point both of the studies effectively improve the prediction accuracy 

11



J. Wang and F. Biljecki                                                                                                                                                                                                               C  i t i e  s  129 (2022) 103925

compared to previous statistical models and have a strong generalization by limited analytical ability, unsupervised methods relegate the issue of 
ability. arbitrariness through quantifying the latent relationship of a larger 

Aside from the regular patterns in cities, there are also outliers, i.e. number of observations (Liu, Deng, et al., 2019). 
special events. In this context, crowdsourced data is akin to sensors in Spatial aggregation profiling inspects the geographical extent of 
cities, and unsupervised learning is of assistance to process the massive clusters of specific functions (e.g. retail) or human activities (Liu, 
volume of data and identify anomalous urban events in real-time, pri Singleton, et al., 2021; Manley et al., 2018; Pavlis et al., 2018; Sun et al., 
marily by focusing on semantic information, a key information layer for 2016). Unsupervised learning demonstrates its ability in dealing with 
event detection. For example, Wang and Taylor (2019) identify geo spatial data on tasks such as this one by taking into account not only the 
locations of Twitter topics that rapidly escalate in a short time period similarity and difference, but also the relative spatial distances between 
through LDA, and combine with sentiment analysis for ranking emer points. In fact, we have also noted several other spatially aware unsu
gency events by intensity of negative sentiment. The proposed frame pervised techniques for different application types, e.g. geographically 
work is directly built upon the API of this social media channel, weighted PCA (Wu et al., 2020), meanwhile new enabling frameworks is 
therefore providing real-time tracking and assessment of disasters for keep being published (Park et al., 2021; You, 2021), implying the wide 
emergency management agencies. For related work see (Zuo et al., applicability and growing relevance of unsupervised methods to 
2018). geographical investigations. 

Another information layer is composed of traffic records such as taxi Considering the methodological aspect, some papers utilize the 
GPS trajectories (Wang et al., 2018) and traffic video (Singh & Mohan, synergy of various unsupervised techniques in analysis and deriving 
2019), identifying events in this portion can infer the occurrence of interpretations (Gao et al., 2017; Hu et al., 2015; Samany, 2019). Yet a 
adverse traffic behavior or road accidents. The approach of detecting more common approach we noticed is combining unsupervised methods 
anomalous patterns in movement trajectories is straightforward, for with other methods, for example, in some cases UL is introduced to 
example, hierarchical clustering is successful in distinguishing regular improve the performance of previous models (Honjo et al., 2015; Xue 
trajectories and anomalous trajectories (Wang et al., 2018). However, et al., 2020), or is applied in conjunction with supervised methods, e.g. 
the information extracted from traffic videos is more ambiguous and unsupervised topic modeling supplements supervised image segmenta
presents larger variations. Therefore, representation learning is intro tion (Taecharungroj & Mathayomchan, 2020; Wu et al., 2020), super
duced in such a task again, Singh and Mohan (2019) train a stacked vised model tests the validity of representations learned by from 
autoencoder for generating deep representation of video features, the unsupervised method (Olson et al., 2021). Such collaborative workflows 
proposed generalized method is able to detect abnormal incidents, such reveal that unsupervised learning can be applied not just standalone, but 
as unusual speed, trajectories, position at high accuracy. also to optimize existing methods and simplify downstream tasks. 

Lastly, there is a portion of studies in which specific improvements to Moreover, supervised learning can provide validation to the UL results 
the unsupervised algorithms are made for better inspecting spatio- which assure reliability, also makes the UL results more comparable. 
temporal data. Park et al. (2021), Liu, Huang, et al. (2021), and Choi Regarding the state of the art of unsupervised learning, which is 
and Hong (2021) optimize DBSCAN algorithm for clustering large-scale continuously evolving, we observe that it takes time for the advances in 
spatiotemporal datasets or detecting feature objects (similar to the task computer science to become adopted in urban studies. Approaches that 
elaborated on in (Hu et al., 2015)) and collective activities in an more have been developed years ago, e.g. autoencoder and GAN (Baldi, 2012; 
efficient manner, You (2021) proposes a clustering method that can be Zhao et al., 2017), are being spotlighted in urban studies only recently 
directly applied on spatial data without setting prior assumptions or (Chen et al., 2021; Comber et al., 2020; Wijnands et al., 2019; Zhang 
user-defined parameters. Notably, those papers are all published very et al., 2021). In addition, it appears that the penetration of UL tech
recently (in 2021), suggesting the rising attention on the pertinence of niques varies considerably among the domains we examined, together 
unsupervised methods and urban dynamics analysis. with the adoption of the latest instances, e.g. transportation research 

and GIS are benefiting from the most advanced techniques whereas 
6. Discussion others lag. 

A potential limitation of this review is that the methodology (Section 
6.1. General observations 3), following the common systematic review approaches, does not 

include combing through preprints and conference papers, which may 
Based on our review (Section 5), there are scores of ways unsuper describe developments and directions not captured by this review. In 

vised machine learning permeated through urban studies — the use addition, due to the breadth of research topics and few exposed tech
cases cover almost the entire landscape of urban data sources, from nical details in reviewed papers, the comparison of performances of UL 
conventional census data (Paul & Sen, 2018) and satellite imagery (Du in urban-related tasks is not provided in this review. 
et al., 2018) to prevailing spatial big data of individual activities such as 
smart card records (Manley et al., 2018), call records (Rios & Munoz, 6.2. Issues 
2017), and social media (Olson et al., 2021). We observe that the input 
datasets in the reviewed papers are generally very large, e.g. 14 million In this section, we discuss the common challenges and limitations of 
transit journeys (Sun & Axhausen, 2016) and 7 million geotagged Flickr unsupervised methods cited frequently by researchers, with a few ob
photos (Hu et al., 2015), which confirms the increasing importance of servations on our own. 
unsupervised learning in mining invisible patterns with the growing Data quality. The effectiveness of unsupervised methods relies on the 
volume and diversity of urban data. intrinsic structure and quality of the input data. Problems with the data 

Among all the application types, clustering is most frequently can accrue in bias, and data collected from different sources may 
exploited (Fig. 12). The popularity of clustering is in line with two generate different results. Researchers cite the specific issues in social 
paradigmatic tasks in urban studies: typology study and spatial aggre media data most frequently, such as the representativeness of de
gation profiling, which are found frequently in the reviewed papers. mographic groups (Hu et al., 2015), positional accuracy of geo-tagged 
Typology study is a multi-faceted task across several domains and at photos and posts (Samany, 2019), and sparse signal in fringe areas 
various scales (Bobkova et al., 2021; Guo et al., 2021; Mikelbank, 2004; (Steiger et al., 2016). In addition to data from social media, the quality 
Nguyen et al., 2020; Oh & Kim, 2019; Tessler et al., 2016). Such fashion of video and sound data is also a concern, as they are susceptible to 
can relate back to the theories by urban study precursors, which simplify environmental conditions such as darkness and noise (Oldoni et al., 
the complex urban systems into a few types for facilitating further in 2015; Singh & Mohan, 2019). 
terpretations. Compared to the traditional categorizations constrained Besides the fact that unsupervised learning can be affected by poor 

12



J. Wang and F. Biljecki                                                                                                                                                                                                               C  i t i e  s  129 (2022) 103925

data quality, it is important to note that data that has obscure patterns 6.3. Open science 
also brings challenges. For example, Zuo et al. (2018) find it difficult to 
identify emergent events that are not intensively discussed in tweets, The open science aspect is worth highlighting. There are only 10 
while Singh and Mohan (2019) report the issue in extracting patterns papers in our review pool that released their code openly, the lack of 
from vehicle movements with large variations. sharing on advances inhibits their diffusion to other cities. Given the fact 

In addition, without labels that control the expected outcomes, un that unsupervised learning can lower the economic and professional 
supervised learning generally has less accuracy in comparison with its barrier of massive scale urban analytics, it is especially valuable to the 
supervised counterpart in performing the same task. For example, in developing countries where most of the world's urbanization takes place 
land use classification and change detection tasks, supervised learning (Ibrahim et al., 2021; Rahman et al., 2019; Rios & Munoz, 2017). 
methods gained higher overall accuracy to 5–10 % than unsupervised There seem to be a need to raise the awareness of open science and 
methods (Chughtai et al., 2021; Mohammady et al., 2015). However, this is something we hope this discussion will spur — the developers 
considering its benefits of reducing cost and labor, which are vital to the should consider sharing code or model for promoting geographical eq
implementations of urban studies, there is inevitably a trade-off between uity of urban study developments, and contribute to the open de
the two. velopments in the urban data science community (Yap et al., 2022). 

Interpretation. Considering that UL learns patterns without labels as 
semantic reference, it may be difficult to interpret the results. In the case 6.4. Research opportunities 
of clustering, the most common way to generate substantive in
terpretations is through manual summarizing the cluster features by This section discusses potential research opportunities that may in
identifying the most representative variables in each grouping. For crease diversity and depth to this rapidly expanding topic. Concerning 
example, Baum et al. (2006), Tessler et al. (2016), and Ferrara et al. the issues we discussed in Section 6.2, there are scores of possible 
(2017) develop and name localities' typology based on the most signif research directions responding to them. For example, the proliferation 
icant features from social and environmental indicators. However, these of social network data (e.g. text, photos, and videos sourced from social 
researchers all posit that such a method is not considered statistically media, and POIs) presents a viable opportunity for less subjective and 
sound. The large room of interpretation also entails that the conclusions more comparable interpretations. In rare instances of related studies, 
may be easily affected by personal view, which impairs their they all target limited applications, i.e. revealing urban functions and 
comparison. travel purposes (Bi & Ye, 2021; Gao et al., 2017; Huang & Li, 2019). It 

In this regard, although UL is an objective method which preserves seems that research using crowdsourced information has gaps worth 
the intrinsic patterns within the data structure, human bias is still investigating because explaining other discovered urban patterns that 
possible to happen in the interpretation stage. On the contrary, the relate to human perceptions remains unexplored, e.g. visual features, 
human bias of SL might be produced during the crafting of labels. Before vitality, and urban morphology. 
making a selection between the two methods, it is worth considering Further, as revealed in the review, some tasks can be carried out both 
which is more convenient and the bias is more acceptable. by supervised and unsupervised methods that have dissimilar traits: SL 

Moreover, interpreting UL results is costlier as it requires pro results in higher accuracy while UL is more transferable and accessible. 
fessionals to correlate the patterns with the domain knowledge, which We believe that revisiting SL studies using unsupervised methods will be 
explains its relatively less popular in urban studies than other domains a meaningful research direction, whose reliability could be validated by 
— few experts in urban studies possess interdisciplinary knowledge as SL results as ground truth, while presenting cheaper and more efficient 
required. urban analysis frameworks for supplementing the gap in urban study in 

Similar to the absent semantic meaning, the statistical relationships numerous developing regions. 
between the results (e.g. typologies, determinants) and urban phenom Continuing the discussion on geographical aspect, as unsupervised 
enons of interest (e.g. energy consumption, forest dynamics) cannot be method can be easily employed in elsewhere, it is worthwhile to conduct 
revealed by the result of unsupervised learning alone (Ferrara et al., comparative studies across locations of different social-economic and 
2017; Li, Ying, et al., 2020), because it does not imply causation and cultural backgrounds. To our knowledge, in the built environment and 
degree of influence. urban dynamics sectors this kind of study is largely under-investigated. 

Validation. Validation is an imperative step to assess the confidence As the current deep learning models such as autoencoder and GAN 
of the findings and facilitate replication of studies in more geographical are proven to be highly capable in reconstructing data, fulfilling missing 
locations. Researchers cite two ways of validation: internal and external. pieces, even making realistic predictions, engaging them into urban 
Internal validation analyzes the internal structure (e.g. cohesion and applications is unquestionably a research frontier. Considering the small 
separation) of the results, each UL technique has well-established in proportion of related publications and the limited topics (e.g. trans
ternal validation methods, they are routinely used in many papers portation prediction) (Ranjan et al., 2021; Singh & Mohan, 2019), there 
(Arbolino et al., 2019; Feng & Liu, 2013; Schmiedel et al., 2015; Serra is a clear untapped opportunity of extending their use cases into a wide 
et al., 2014; Vizzari & Sigura, 2015). variety of scenarios such as complementing data infrastructure of digital 

However, studies engaging unsupervised applications in cities do not twins (Rasheed et al., 2020), data compression for real-time urban 
stop short at internal validation. Because urban studies have a close monitoring, simulating dynamics in urban systems, and AI-generated 
connection with real-world practice, justifying the results are aligned urban planning and design. 
with the ground truth is always an area of focus. For this purpose, re Finally, opportunities can also be found in the rapidly evolving 
searchers resort to various external sources — historical flooding maps, technological landscape of unsupervised learning, as newly developed 
official emergency event records, land use from the master plan, results methods may enable novel applications. For example, a recent self- 
of preceding studies, ground survey, and manual labeling (Akande et al., supervised image pre-trained model has outperformed the best super
2019; Aljumaily et al., 2017; Peng et al., 2021; Richards & Tuncer, 2018; vised model in a diverse set of computer vision tasks (Goyal et al., 2021). 
Xu et al., 2018; Xue et al., 2020; Ye & Chen, 2015; Zhang et al., 2018). Similar efforts are being made intensively for improving both the ac
However, these studies are rare, accounting for less than 10 % of pub curacy and efficiency of unsupervised learning, the cumulative progress 
lications. Such external information is not always readily available (e.g. appears to be promising. We believe that with the strides made in un
survey data is time-consuming and costly to gain), and results from supervised techniques, urban studies engaging them will grow expo
certain application types (e.g. clustering and topic modeling) generally nentially, but they should reduce the lag in adopting them. 
have no existing benchmark to compare with, consequently the integrity 
and reliability of UL may be questioned. 

13



J. Wang and F. Biljecki                                                                                                                                                                                                               C  i t i e  s  129 (2022) 103925

7. Conclusion We have also provided a concise introduction to unsupervised 
learning, as a gentle overview for our peers who are yet to consider using 

In this paper, we have reviewed the application of unsupervised it in their research. Thanks to the growing and easily accessible free and 
learning in urban studies. Unsupervised techniques, despite their open-source implementations, and the vibrant data science community, 
versatility and number of methods, have been somewhat overshadowed the entry barrier has never been lower. We hope that this paper will raise 
by supervised counterparts due to the different volume of papers and awareness of the potential of unsupervised learning and will catalyze 
disparate applications. However, that makes it possible to capture the further applications. 
developments in a single and self-contained review paper, in which we We expect that in the future, we will indeed witness a growing vol
have revealed trends and provided a comprehensive list of applications ume of uses in urban studies, largely thanks to the increase in the volume 
of the comprehensive list of more than a dozen unsupervised methods. of available data and the advancements in techniques. 

We find that the applications of unsupervised learning span the 
entire landscape of urban data sources. With the growing human-sensing CRediT authorship contribution statement 
data and built environment records such as street view imagery, nov
elties of UL applications have been emerging continuously, discovering Jing Wang: Conceptualization, Methodology, Validation, Formal 
new patterns and representations of cities that inform decision making analysis, Investigation, Data curation, Writing – original draft, Visuali
or catalyze novel downstream analytics. Moreover, in many instances, zation. Filip Biljecki: Conceptualization, Investigation, Writing – orig
unsupervised learning enables heterogeneous multi-source data inal draft, Supervision, Funding acquisition. 
convergence that explicitly represents the complex real-world urban 
systems at multiple scales (Zhan et al., 2020, 2021). Declaration of competing interest 

We identify clustering as the most prominent application type, fol
lowed by topic modeling that provides bottom-up understandings of the The authors declare that they have no known competing financial 
urban environment. Although unsupervised deep learning models have interests or personal relationships that could have appeared to influence 
gained popularity in other disciplines, the potentials of them in urban the work reported in this paper. 
studies are underexplored. Such domain is where we expect to see a 
growing volume of studies in the coming years. Relevant studies are Data availability 
emerging, in simulating urban growth (Albert et al., 2018), traffic 
forecasting (Chen et al., 2021), and environment beautification (Wij No data was used for the research described in the article. 
nands et al., 2019). 

The limitations of unsupervised methods are discussed in this review Acknowledgements 
as well, followed by several research opportunities addressing them. 
Through making use of the urban semantics information we believe the We gratefully acknowledge the valuable comments by the editor and 
interpretation bias of unsupervised learning results can be alleviated. It the four reviewers. We thank the members of the NUS Urban Analytics 
is also important to consider the strengths of both supervised and un Lab for the discussions. This research is part of the project Large-scale 3D 
supervised learning and optimize analysis methods through their Geospatial Data for Urban Analytics, which is supported by the National 
synergy. University of Singapore under the Start Up Grant R-295-000-171-133.  

Appendix A. Search syntax 

(((TS=(( “K-means” OR “hierarchical clustering” OR “DBSCAN” OR “Mean-shift” OR “Affinity propagation” OR “Gaussian mixture model*” OR 
“Spectral clustering” OR ( ( “principal component analysis” OR pca ) AND ( feature OR extract* ) ) OR “Latent Dirichlet Allocation” OR lda OR “Non- 
negative matrix factorization” OR nmf OR “Latent semantic analysis” OR “t-SNE” OR “Self-organizing map*” OR “Autoencoder*” OR “Auto-encoder*” 
OR “Restricted Boltzmann machine*” OR “RBMs” OR “Generative Adversarial Net*”) AND ( city OR urban* ) )) AND DT=(Article)) AND LA=(En
glish)) AND WC=(Environmental Studies or Geography Physical or Green Sustainable Science Technology or Geography or Engineering Civil or Urban 
Studies or Regional Urban Planning) 

Appendix B. Reviewed papers  
Table B.3 
Key information from reviewed papers by data type. Key: UR: urbanization and regional studies; BE: built environment; US: urban sustainability; UD: urban dynamics.  

Data type Data source Publication Category Application type Technique 

Image Image (Ranjan et al., 2021) UD Prediction Autoencoder 
Photo (Nguyen et al., 2020) BE Clustering K-means 

(Samany, 2019) BE Feature extraction RBM 
(Taecharungroj & Mathayomchan, 2020) BE Topic modeling LDA 
(Park et al., 2021) UD Clustering DBSCAN 
(Hu et al., 2015) UD Clustering DBSCAN 

Satellite imagery (Kit et al., 2012) BE Feature extraction PCA 
(Krtalic et al., 2021) US Change detection PCA 
(Peng et al., 2021) US Change detection Autoencoder 
(Ye & Chen, 2015) UR Change detection Others 
(Du et al., 2018) UR Change detection LDA 
(Xu et al., 2012) UR Feature extraction Multiple 
(Feng & Liu, 2013) UR Feature extraction PCA 
(Ibrahim et al., 2021) UR Prediction GAN 

Street view images (Wu et al., 2020) BE Factor extraction PCA 
(Wijnands et al., 2019) BE Image translation GAN 

(continued on next page) 

14



J. Wang and F. Biljecki                                                                                                                                                                                                               C  i t i e  s  129 (2022) 103925
Table B.3 (continued ) 

Data type Data source Publication Category Application type Technique 

Numeric Census (Paul & Sen, 2018) BE Clustering K-means 
(Dias & Silver, 2021) UD Clustering Others 
(Lu et al., 2015) US Clustering SOM 
(Kropp, 1998) US Clustering SOM 
(Baum et al., 2006) UR Clustering GMM 
(Christodoulou & Christidis, 2020) UR Clustering K-means 
(Delmelle, 2017) UR Clustering Multiple 
(Arribas-Bel & Schmidt, 2013) UR Clustering SOM 
(Mikelbank, 2004) UR Clustering HCA 
(Fusco & Perez, 2019) UR Clustering Multiple 
(Liu, Deng, et al., 2019) UR Clustering K-means 
(Li & Xie, 2018) UR Clustering Multiple 
(Tang et al., 2020) UR Factor extraction PCA 
(Arbolino et al., 2019) UR Factor extraction PCA 

Geography (Paulvannan Kanmani et al., 2020) US Clustering SOM 
Meteorological data (Xu et al., 2020) US Clustering K-means 
Numeric attributes (Liu, Singleton, & Arribas-Bel, 2020) BE Clustering SOM 

(Bobkova et al., 2021) BE Clustering K-means 
(Abarca-Alvarez et al., 2019) BE Clustering SOM 
(You, 2021) UD Clustering Others 
(Oh & Kim, 2019) US Clustering Multiple 
(Li, Ying, et al., 2020) US Feature extraction PCA 
(Feng et al., 2020) UR Clustering K-means 

Sensor (Honjo et al., 2015) US Clustering HCA 
Survey (Tu & Lin, 2008) BE Factor extraction PCA 

(Bonaiuto et al., 2003) BE Factor extraction PCA 
(Xi et al., 2020) UD Topic modeling LDA 
(Martins et al., 2021) US Factor extraction PCA 
(Akande et al., 2019) US Factor extraction HCA 
(Arribas-Bel et al., 2013) UR Clustering SOM 
(Yuan et al., 2021) UR Clustering K-means 

Sound & video Sound (Oldoni et al., 2015) BE Feature extraction SOM 
(Chew & Wu, 2016) BE Feature extraction PCA 

Video (Singh & Mohan, 2019) UD Anomaly detection Autoencoder 
Spatial Land use/cover (Owen et al., 2006) BE Clustering Others 

(Schmiedel et al., 2015) US Clustering K-means 
(Lyu et al., 2019) US Clustering SOM 
(Naikoo et al., 2020) UR Change detection K-means 
(Qi et al., 2019) UR Clustering SOM 
(Lemoine-Rodriguez et al., 2020) UR Clustering Multiple 
(Rahman et al., 2019) UR Clustering HCA 

LiDAR point cloud (Xue et al., 2020) BE Clustering Others 
(Aljumaily et al., 2017) BE Clustering DBSCAN 

OSM (Jochem et al., 2021) BE Clustering GMM 
(Cui et al., 2019) BE Clustering DBSCAN 
(Liu, Huang, et al., 2021) UD Clustering DBSCAN 

POI (Yu et al., 2020) BE Clustering DBSCAN 
(Pavlis et al., 2018) BE Clustering DBSCAN 
(Sparks et al., 2020) UD Clustering HCA 
(Liu, Yin, et al., 2020) UD Topic modeling t-SNE 

Spatial-temporal Call records (Rios & Munoz, 2017) BE Clustering LDA 
(Ghahramani et al., 2019) UD Clustering HCA 
(Sagl et al., 2014) UD Clustering SOM 

Cellular (Sun et al., 2021) UD Clustering K-means 
(Kim, 2020b) UD Factor extraction PCA 

GPS (Tao et al., 2019) BE Factor extraction LSA 
(Wang et al., 2018) UD Anomaly detection HCA 
(Liu, Singleton, et al., 2021) UD Clustering DBSCAN 
(Zhang et al., 2021) UD Prediction GAN 

Parking data (Fiez & Ratliff, 2020) UD Clustering GMM 
Smart card (Wang et al., 2021) BE Clustering GMM 

(Kim, 2020a) BE Clustering Multiple 
(Ouyang et al., 2018) UD Clustering DBSCAN 
(Manley et al., 2018) UD Clustering DBSCAN 
(Sun & Axhausen, 2016) UD Factor extraction LSA 
(Ozus et al., 2012) UR Clustering HCA 
(Pieroni et al., 2021) UD Clustering Multiple 

Real estate transactions (Choi & Hong, 2021) UD Clustering DBSCAN 
Traffic flow (Anwar et al., 2016) UD Clustering Spectral clustering 

(Yue et al., 2018) UD Clustering Spectral clustering 
(Sun et al., 2006) UD Prediction GMM 
(Chen et al., 2021) UD Prediction Autoencoder 

Text Electronic media outlets (Capela & Ramirez-Marquez, 2019) UD Topic modeling LDA 
Social media (Zhong et al., 2018) BE Topic modeling LDA 

(Zuo et al., 2018) UD Anomaly detection LDA 
(Steiger et al., 2016) UD Clustering SOM 

(continued on next page) 

15



J. Wang and F. Biljecki                                                                                                                                                                                                               C  i t i e  s  129 (2022) 103925
Table B.3 (continued ) 

Data type Data source Publication Category Application type Technique 

(Sun et al., 2016) UD Clustering DBSCAN 
(Olson et al., 2021) UD Topic modeling Autoencoder 
(Wang & Taylor, 2019) UD Topic modeling LDA 
(Huang & Li, 2019) UD Topic modeling LDA 
(Abdul-Rahman et al., 2021) UD Topic modeling LDA 

Labels (Richards & Tuncer, 2018) US Clustering HCA 
Geo-textual advertisements (Su et al., 2021) BE Topic modeling LDA 

Multi-source Call records, POI (Yuan et al., 2020) BE Clustering K-means 
(Dong, Wang, & Liu, 2021) UD Clustering SOM 

Cellular, POI (Chen et al., 2019) UD Clustering K-means 
(Cai et al., 2019) UD Clustering K-means 
(Liu, Zhang, & Long, 2019) UD Feature extraction SOM 

Census, search index (Xue et al., 2021) UR Clustering K-means 
DEM, Land use/cover etc. (Gao et al., 2014) US Clustering SOM 
GPS, POI (Li et al., 2021) UD Clustering DBSCAN 

(Bi & Ye, 2021) UD Topic modeling LDA 
Geography, Census (Ferrara et al., 2017) US Clustering K-means 

(Tessler et al., 2016) US Clustering Multiple 
(Amaral et al., 2021) US Clustering SOM 
(Serra et al., 2014) UR Clustering K-means 

Geography, DEM, climate (Yang et al., 2019) US Clustering K-means 
Image, POI (Comber et al., 2020) BE Feature extraction Autoencoder 
Land use/cover, Census (Fiaschetti et al., 2021) UR Clustering AP 

(Bonilla-Bedoya et al., 2020) US Clustering HCA 
(Vizzari & Sigura, 2015) UR Clustering Others 

Land use/cover, LiDAR (Karimi et al., 2021) US Clustering K-means 
Land use/cover, climate (Zawadzka et al., 2021) US Clustering K-means 
Land use/cover, geography (Cabrera-Barona et al., 2020) UR Clustering K-means 
Numeric attributes, Census (Lopes et al., 2021) BE Clustering K-means 

(Li, Han, et al., 2019) BE Clustering SOM 
(Bo et al., 2019) BE Factor extraction PCA 
(Sohn, 2013) BE Feature extraction SOM 

Numeric attributes, cellular (Manley & Dennett, 2019) UD Clustering K-means 
Numeric attributes, climate (Kwon et al., 2021) BE Clustering K-means 
OSM, social media etc. (Devkota et al., 2019) UD Clustering DBSCAN 
POI, GPS (Jing et al., 2021) BE Clustering DBSCAN 

(Li, Zhu, & Guo, 2019) UD Clustering K-means 
(Xing et al., 2020) UD Clustering K-means 

POI, OSM, census (Miao et al., 2021) BE Clustering Multiple 
POI, Smart card (Zhang et al., 2018) BE Clustering K-means 
POI, Social media (Gao et al., 2017) BE Topic modeling LDA 
POI, Social media (Papadakis et al., 2019) BE Topic modeling LDA 
POI, land use/cover (Dong, Li, et al., 2021) BE Clustering DBSCAN 
POI, street view images (Hu et al., 2020) BE Topic modeling LDA 
POI, trip records (Yu et al., 2021) UD Clustering Multiple 
POI, Call records, OSM (Guo et al., 2021) UD Clustering K-means 
Smart card, GPS (Yu & He, 2017) UD Clustering Multiple 
Climate, DEM (Xu et al., 2018) US Clustering K-means  

References Arbolino, R., Yigitcanlar, T., L’Abbate, P., & Ioppolo, G. (2019). Effective growth 
policymaking: Estimating provincial territorial development potentials. Land Use 

Abarca-Alvarez, F. J., Campos-Sánchez, F. S., & Osuna-Pérez, F. (2019). Urban shape and Policy, 86, 313–321. https://doi.org/10.1016/j.landusepol.2019.05.009 
Aria, M., & Cuccurullo, C. (2017). Bibliometrix: An R-tool for comprehensive science 

built density metrics through the analysis of European urban fabrics using artificial 
intelligence. Sustainability, 11, 6622. https://doi.org/10.3390/su11236622 mapping analysis. Journal of Informetrics, 11, 959–975. https://doi.org/10.1016/j. 

joi.2017.08.007 
Abdul-Rahman, M., Chan, E. H. W., Wong, M. S., Irekponor, V. E., & Abdul- 

Rahman, M. O. (2021). A framework to simplify pre-processing location-based social Arribas-Bel, D., Kourtit, K., & Nijkamp, P. (2013). Benchmarking of world cities through 
self-organizing maps. Cities, 31, 248–257. https://doi.org/10.1016/j. 

media big data for sustainable urban planning and management. Cities, 109, Article cities.2012.06.019 
102986. https://doi.org/10.1016/j.cities.2020.102986 

Akande, A., Cabral, P., Gomes, P., & Casteleyn, S. (2019). The Lisbon ranking for smart Arribas-Bel, D., & Schmidt, C. R. (2013). Self-organizing maps and the US urban spatial 
structure. Environment and Planning B: Planning and Design, 40, 362–371. https://doi. 

sustainable cities in Europe. Sustainable Cities and Society, 44, 475–487. https://doi. 
org/10.1016/j.scs.2018.10.009 org/10.1068/b37014 

Athey, S. (2017). Beyond prediction: Using big data for policy problems. Science, 355, 
Albert, A., Strano, E., Kaur, J., & González, M. (2018). Modeling urbanization patterns 483–485. https://doi.org/10.1126/science.aal4321 

with generative adversarial networks. In IGARSS 2018–2018 IEEE international 
geoscience and remote sensing symposium (pp. 2095–2098). https://doi.org/10.1109/ Baldi, P. (2012). Autoencoders, unsupervised learning, and deep architectures. In 

Proceedings of ICML workshop on unsupervised and transfer learning, JMLR workshop 
IGARSS.2018.8518032 

Aljumaily, H., Laefer, D. F., & Cuadra, D. (2017). Urban point cloud mining based on and conference proceedings (pp. 37–49). 
Batty, M. (2008). The size, scale, and shape of cities. Science, 319, 769–771. https://doi. 

density clustering and MapReduce. Journal of Computing in Civil Engineering, 31, 
04017021. https://doi.org/10.1061/(ASCE)CP.1943-5487.0000674 org/10.1126/science.1151419 

Baum, S., Haynes, M., van Gellecum, Y., & Han, J. H. (2006). Advantage and 
Amaral, M. H., Benites-Lazaro, L. L., Sinisgalli, P. A. D. A., Alves, H. P. D. F., & disadvantage across Australia's extended metropolitan regions: A typology of 

Giatti, L. L. (2021). Environmental injustices on green and blue infrastructure: Urban 
nexus in a macrometropolitan territory. Journal of Cleaner Production, 289, Article socioeconomic outcomes. Urban Studies, 43, 1549–1579. https://doi.org/10.1080/ 

00420980600831759 
125829. https://doi.org/10.1016/j.jclepro.2021.125829 

Anwar, T., Vu, H. L., Liu, C., & Hoogendoorn, S. P. (2016). Temporal tracking of Bengio, Y., Courville, A., & Vincent, P. (2013). Representation learning: A review and 
new perspectives. IEEE Transactions on Pattern Analysis and Machine Intelligence, 35, 

congested partitions in dynamic urban road networks. Transportation Research 1798–1828. https://doi.org/10.1109/TPAMI.2013.50 
Record, 88–97. https://doi.org/10.3141/2595-10 

16



J. Wang and F. Biljecki                                                                                                                                                                                                               C  i t i e  s  129 (2022) 103925

Bettencourt, L., & West, G. (2010). A unified theory of urban living. Nature, 467, Dong, L., Li, J., Xu, Y., Yang, Y., Li, X., & Zhang, H. (2021a). Study on the spatial 
912–913. https://doi.org/10.1038/467912a classification of construction land types in Chinese cities: A case study in Zhejiang 

Bi, H., & Ye, Z. (2021). Exploring ridesourcing trip patterns by fusing multi-source data: Province. Land, 10, 523. https://doi.org/10.3390/land10050523 
A big data approach. Sustainable Cities and Society, 64, Article 102499. https://doi. Dong, W., Wang, S., & Liu, Y. (2021b). Mapping relationships between mobile phone call 
org/10.1016/j.scs.2020.102499 activity and regional function using self-organizing map. Computers Environment and 

Biljecki, F., & Chow, Y. S. (2022). Global building morphology indicators. Computers, Urban Systems, 87, Article 101624. https://doi.org/10.1016/j. 
Environment and Urban Systems, 95, Article 101809. https://doi.org/10.1016/j. compenvurbsys.2021.101624 
compenvurbsys.2022.101809 Du, B., Wang, Y., Wu, C., & Zhang, L. (2018). Unsupervised scene change detection via 

Biljecki, F., & Ito, K. (2021). Street view imagery in urban analytics and GIS: A review. latent dirichlet allocation and multivariate alteration detection. IEEE Journal of 
Landscape and Urban Planning, 215, Article 104217. https://doi.org/10.1016/j. Selected Topics in Applied Earth Observations and Remote Sensing, 11, 4676–4689. 
landurbplan.2021.104217 https://doi.org/10.1109/JSTARS.2018.2869549 

Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent dirichlet allocation. The Journal of El Bouchefry, K., & de Souza, R. S. (2020). Chapter 12 - learning in big data: Introduction 
Machine Learning Research, 3, 993–1022. to machine learning. In P. Škoda, & F. Adam (Eds.), Knowledge discovery in big data 

Bo, F., Danlin, Y., & Yaojun, Z. (2019). The livable urban landscape: GIS and remote from astronomy and Earth observation (pp. 225–249). Elsevier. https://doi.org/ 
sensing extracted land use assessment for urban livability in Changchun Proper, 10.1016/B978-0-12-819154-5.00023-0.  
China. Land Use Policy, 87, Article 104048. https://doi.org/10.1016/j. Ester, M., Kriegel, H. P., Sander, J., & Xiaowei, X. (1996). A density-based algorithm for 
landusepol.2019.104048 discovering clusters in large spatial databases with noise. 

Bobkova, E., Pont, M. B., & Marcus, L. (2021). Towards analytical typologies of plot Feng, Y., & Liu, Y. (2013). A cellular automata model based on nonlinear kernel principal 
systems: Quantitative profile of five European cities. Environment and Planning B- component analysis for urban growth simulation. Environment and Planning. B, 
Urban Analytics and City Science, 48, 604–620. https://doi.org/10.1177/ Planning & Design, 40, 117–134. https://doi.org/10.1068/b37142 
2399808319880902 Feng, Z., Peng, J., & Wu, J. (2020). Using DMSP/OLS nighttime light data and K-means 

Bonaiuto, M., Fornara, F., & Bonnes, M. (2003). Indexes of perceived residential method to identify urban-rural fringe of megacities. Habitat International, 103, 
environment quality and neighbourhood attachment in urban environments: A Article 102227. https://doi.org/10.1016/j.habitatint.2020.102227 
confirmation study on the city of Rome. Landscape and Urban Planning, 65, 43–54. Ferrara, C., Carlucci, M., Grigoriadis, E., Corona, P., & Salvati, L. (2017). 
https://doi.org/10.1016/S0169-2046(02)00236-0 A comprehensive insight into the geography of forest cover in Italy: Exploring the 

Bonilla-Bedoya, S., Estrella, A., Vaca Yanez, A., & Angel Herrera, M. (2020). Urban socio- importance of socioeconomic local contexts. Forest Policy and Economics, 75, 12–22. 
ecological dynamics: Applying the urban-rural gradient approach in a high Andean https://doi.org/10.1016/j.forpol.2016.11.008 
city. Landscape Research, 45, 327–345. https://doi.org/10.1080/ Fiaschetti, M., Graziano, M., & Heumann, B. W. (2021). A data-based approach to 
01426397.2019.1641589 identifying regional typologies and exemplars across the urban-rural gradient in 

Brenner, N. (2013). Theses on urbanization. Public Culture, 25, 85–114. https://doi.org/ Europe using affinity propagation. Regional Studies, 55(12), 1939–1954. https://doi. 
10.1215/08992363-1890477 org/10.1080/00343404.2021.1871598 

Cabrera-Barona, P. F., Bayon, M., Duran, G., Bonilla, A., & Mejia, V. (2020). Generating Fiez, T., & Ratliff, L. J. (2020). Gaussian mixture models for parking demand data. IEEE 
and mapping Amazonian urban regions using a geospatial approach. ISPRS Transactions on Intelligent Transportation Systems, 21, 3571–3580. https://doi.org/ 
International Journal of Geo-Information, 9, 453. https://doi.org/10.3390/ 10.1109/TITS.2019.2939499 
ijgi9070453 Frey, B. J., & Dueck, D. (2007). Clustering by passing messages between data points. 

Cai, L., Xu, J., Liu, J., Ma, T., Pei, T., & Zhou, C. (2019). Sensing multiple semantics of Science, 315, 972–976. https://doi.org/10.1126/science.1136800 
urban space from crowdsourcing positioning data. Cities, 93, 31–42. https://doi.org/ Fusco, G., & Perez, J. (2019). Bayesian network clustering and self-organizing maps 
10.1016/j.cities.2019.04.011 under the test of Indian districts.A comparison. Cybergeo-European Journal of 

Capela, F. D. O., & Ramirez-Marquez, J. E. (2019). Detecting urban identity perception Geography, 31909. https://doi.org/10.4000/cybergeo.31909 
via newspaper topic modeling. Cities, 93, 72–83. https://doi.org/10.1016/j. Gao, S. (2015). Spatio-temporal analytics for exploring human mobility patterns and 
cities.2019.04.009 urban dynamics in the mobile age. Spatial Cognition & Computation, 15, 86–114. 

Chen, C., Liu, Z., Wan, S., Luan, J., & Pei, Q. (2021). Traffic flow prediction based on https://doi.org/10.1080/13875868.2014.984300 
deep learning in internet of vehicles. IEEE Transactions on Intelligent Transportation Gao, S., Janowicz, K., & Couclelis, H. (2017). Extracting urban functional regions from 
Systems, 22, 3776–3789. https://doi.org/10.1109/TITS.2020.3025856 points of interest and human activities on location-based social networks. 

Chen, Y., Zhang, Z., & Liang, T. (2019). Assessing urban travel patterns: An analysis of Transactions in GIS, 21, 446–467. https://doi.org/10.1111/tgis.12289 
traffic analysis zone-based mobility patterns. Sustainability, 11, 5452. https://doi. Gao, Y., Feng, Z., Wang, Y., Liu, J. L., Li, S. C., & Zhu, Y. K. (2014). Clustering urban 
org/10.3390/su11195452 multifunctional landscapes using the self-organizing feature map neural network 

Chew, Y. R., & Wu, B. S. (2016). A soundscape approach to analyze traffic noise in the model. Journal of Urban Planning and Development, 140. https://doi.org/10.1061/ 
city of Taipei,Taiwan. Computers Environment and Urban Systems, 59, 78–85. https:// (ASCE)UP.1943-5444.0000170 
doi.org/10.1016/j.compenvurbsys.2016.05.002 Ghahramani, M., Zhou, M., & Hon, C. T. (2019). Extracting significant mobile phone 

Choi, C., & Hong, S. Y. (2021). MDST-DBSCAN: A density-based clustering method for interaction patterns based on community structures. IEEE Transactions on Intelligent 
multidimensional spatiotemporal data. ISPRS International Journal of Geo- Transportation Systems, 20, 1031–1041. https://doi.org/10.1109/ 
Information, 10, 391. https://doi.org/10.3390/ijgi10060391 TITS.2018.2836800 

Christodoulou, A., & Christidis, P. (2020). Bridges across borders: A clustering approach Goodfellow, I. J., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., 
to support EU regional policy. Journal of Transport Geography, 83, Article 102666. Courville, A., & Bengio, Y. (2014). Generative adversarial networks. https://doi.org/ 
https://doi.org/10.1016/j.jtrangeo.2020.102666 10.48550/arXiv.1406.2661. arXiv:1406.2661. 

Chughtai, A. H., Abbasi, H., & Karas, I. R. (2021). A review on change detection method Goyal, P., Caron, M., Lefaudeux, B., Xu, M., Wang, P., Pai, V., Singh, M., Liptchinsky, V., 
and accuracy assessment for land use land cover. Remote Sensing Applications: Society Misra, I., Joulin, A., & Bojanowski, P. (2021). Self-supervised pretraining of visual 
and Environment, 22, Article 100482. https://doi.org/10.1016/j.rsase.2021.100482 features in the wild. arXiv:2103.01988 [cs] arXiv:2103.01988. 

Comber, S., Arribas-Bel, D., Singleton, A., & Dolega, L. (2020). Using convolutional Grekousis, G. (2019). Artificial neural networks and deep learning in urban geography: A 
autoencoders to extract visual features of leisure and retail environments. Landscape systematic review and meta-analysis. Computers, Environment and Urban Systems, 74, 
and Urban Planning, 202, Article 103887. https://doi.org/10.1016/j. 244–256. https://doi.org/10.1016/j.compenvurbsys.2018.10.008 
landurbplan.2020.103887 Guo, X., Chen, H., & Yang, X. (2021). An evaluation of street dynamic vitality and its 

Cottineau, C., Hatna, E., Arcaute, E., & Batty, M. (2017). Diverse cities or the systematic influential factors based on multi-source big data. ISPRS International Journal of Geo- 
paradox of urban scaling laws. Computers Environment and Urban Systems, 63, 80–94. Information, 10, 143. https://doi.org/10.3390/ijgi10030143 
https://doi.org/10.1016/j.compenvurbsys.2016.04.006 Gurran, N., Searle, G., & Phibbs, P. (2018). Urban planning in the age of Airbnb: Coase, 

Cui, X., Wang, J., Wu, F., Li, J., Gong, X., Zhao, Y., & Zhu, R. (2019). Extracting main property rights, and spatial regulation. Urban Policy and Research, 36, 399–416. 
center pattern from road networks using density-based clustering with fuzzy https://doi.org/10.1080/08111146.2018.1460268 
neighborhood. ISPRS International Journal of Geo-Information, 8, 238. https://doi. Hartigan, J. A., & Wong, M. A. (1979). Algorithm AS 136: A K-means clustering 
org/10.3390/ijgi8050238 algorithm. Journal of the Royal Statistical SocietySeries C (Applied Statistics), 28, 

Delmelle, E. C. (2017). Differentiating pathways of neighborhood change in 50 US 100–108. https://doi.org/10.2307/2346830 
metropolitan areas. Environment and Planning A, 49, 2402–2424. https://doi.org/ Hinton, G. E., Osindero, S., & Teh, Y. W. (2006). A fast learning algorithm for deep belief 
10.1177/0308518X17722564 nets. Neural Computation, 18, 1527–1554. https://doi.org/10.1162/ 

Demšar, U., Harris, P., Brunsdon, C., Fotheringham, A. S., & McLoone, S. (2013). neco.2006.18.7.1527 
Principal component analysis on spatial data: An overview. Annals of the Association Hinton, G. E., & Salakhutdinov, R. R. (2006). Reducing the dimensionality of data with 
of American Geographers, 103, 106–128. https://doi.org/10.1080/ neural networks. Science, 313, 504–507. https://doi.org/10.1126/science.1127647 
00045608.2012.689236 Honjo, T., Yamato, H., Mikami, T., & Grimmond, C. S. B. (2015). Network optimization 

Devkota, B., Miyazaki, H., Witayangkurn, A., & Kim, S. M. (2019). Using volunteered for enhanced resilience of urban heat island measurements. Sustainable Cities and 
geographic information and nighttime light remote sensing data to identify tourism Society, 19, 319–330. https://doi.org/10.1016/j.scs.2015.02.004 
areas of interest. Sustainability, 11, 4718. https://doi.org/10.3390/su11174718 Hu, F., Liu, W., Lu, J., Song, C., Meng, Y., Wang, J., & Xing, H. (2020). Urban function as 

Dias, F., & Silver, D. (2021). Neighborhood dynamics with unharmonized longitudinal a new perspective for adaptive street quality assessment. Sustainability, 12, 1296. 
data. Geographical Analysis, 53, 170–191. https://doi.org/10.1111/gean.12224 https://doi.org/10.3390/su12041296 

Doersch, C., Singh, S., Gupta, A., Sivic, J., & Efros, A. (2012). What makes Paris look like Hu, Y., Deng, C., & Zhou, Z. (2019). A semantic and sentiment analysis on online 
Paris? ACM Transactions on Graphics, 31. neighborhood reviews for understanding the perceptions of people toward their 

living environments. Annals of the American Association of Geographers, 109, 
1052–1073. https://doi.org/10.1080/24694452.2018.1535886 

17



J. Wang and F. Biljecki                                                                                                                                                                                                               C  i t i e  s  129 (2022) 103925

Hu, Y., Gao, S., Janowicz, K., Yu, B., Li, W., & Prasad, S. (2015). Extracting and Li, F., Shi, W., & Zhang, H. (2021). A two-phase clustering approach for urban hotspot 
understanding urban areas of interest using geotagged photos. Computers detection with spatiotemporal and network constraints. IEEE Journal of Selected 
Environment and Urban Systems, 54, 240–254. https://doi.org/10.1016/j. Topics in Applied Earth Observations and Remote Sensing, 14, 3695–3705. https://doi. 
compenvurbsys.2015.09.001 org/10.1109/JSTARS.2021.3068308 

Huang, W., Cui, L., Chen, M., Zhang, D., & Yao, Y. (2022). Estimating urban functional Li, J., & Biljecki, F. (2019). The implementation of big data analysis in regulating online 
distributions with semantics preserved POI embedding. International Journal of short-term rental business: A case of Airbnb in Beijing. In ISPRS Ann. Photogramm. 
Geographical Information Science, 1–26. https://doi.org/10.1080/ Remote Sens. Spatial Inf. Sci. IV-4/W9 (pp. 79–86). https://doi.org/10.5194/isprs- 
13658816.2022.2040510 annals-IV-4-W9-79-2019 

Huang, W., & Li, S. (2019). An approach for understanding human activity patterns with Li, N., Shepperd, M., & Guo, Y. (2020a). A systematic review of unsupervised learning 
the motivations behind. International Journal of Geographical Information Science, 33, techniques for software defect prediction. Information and Software Technology, 122, 
385–407. https://doi.org/10.1080/13658816.2018.1530354 Article 106287. https://doi.org/10.1016/j.infsof.2020.106287 

Ibrahim, H., Khattab, Z., Khattab, T., & Abraham, R. (2021). Expatriates'housing Li, X., Ying, Y., Xu, X., Wang, Y., Hussain, S. A., Hong, T., & Wang, W. (2020b). 
dispersal outlook in a rapidly developing Metropolis based on urban growth Identifying key determinants for building energy analysis from urban building 
predicted using a machine learning algorithm. Housing Policy Debate, 1–21. https:// datasets. Building and Environment, 181, Article 107114. https://doi.org/10.1016/j. 
doi.org/10.1080/10511482.2021.1962939 buildenv.2020.107114 

Ibrahim, M. R., Haworth, J., & Cheng, T. (2020). Understanding cities with machine Li, Y., & Xie, Y. (2018). A new urban typology model adapting data mining analytics to 
eyes: A review of deep computer vision in urban analytics. Cities, 96, Article 102481. examine dominant trajectories of neighborhood change: A case of Metro Detroit. 
https://doi.org/10.1016/j.cities.2019.102481 Annals of the American Association of Geographers, 108, 1313–1337. https://doi.org/ 

Ito, K., & Biljecki, F. (2021). Assessing bikeability with street view imagery and computer 10.1080/24694452.2018.1433016 
vision. Transportation Research Part C: Emerging Technologies, 132, Article 103371. Li, Y., Zhu, Z., & Guo, X. (2019a). Operating characteristics of dockless bike-sharing 
https://doi.org/10.1016/j.trc.2021.103371 systems near metro stations: Case study in Nanjing City,China. Sustainability, 11, 

Jacobs, K. T., & Mitchell, S. W. (2020). OpenStreetMap quality assessment using 2256. https://doi.org/10.3390/su11082256 
unsupervised machine learning methods. Transactions in GIS, 24, 1280–1298. Li, Z., Han, Z., Xin, J., Luo, X., Su, S., & Weng, M. (2019b). Transit oriented development 
https://doi.org/10.1111/tgis.12680 among metro station areas in Shanghai, China: Variations, typology, optimization 

Jain, A. (2010). Data clustering: 50 years beyond K-means. Pattern Recognition Letters, 31, and implications for land use planning. Land Use Policy, 82, 269–282. https://doi. 
651–666. https://doi.org/10.1016/j.patrec.2009.09.011 org/10.1016/j.landusepol.2018.12.003 

Janowicz, K., Gao, S., McKenzie, G., Hu, Y., & Bhaduri, B. (2020). GeoAI: Spatially Liu, C., Deng, Y., Song, W., Wu, Q., & Gong, J. (2019a). A comparison of the approaches 
explicit artificial intelligence techniques for geographic knowledge discovery and for gentrification identification. Cities, 95, Article 102482. https://doi.org/10.1016/ 
beyond. International Journal of Geographical Information Science, 34, 625–636. j.cities.2019.102482 
https://doi.org/10.1080/13658816.2019.1684500 Liu, K., Yin, L., Lu, F., & Mou, N. (2020a). Visualizing and exploring POI configurations 

Jean, N., Burke, M., Xie, M., Davis, W. M., Lobell, D. B., & Ermon, S. (2016). Combining of urban regions on POI-type semantic space. Cities, 99, Article 102610. https://doi. 
satellite imagery and machine learning to predict poverty. Science, 353, 790–794. org/10.1016/j.cities.2020.102610 
https://doi.org/10.1126/science.aaf7894 Liu, P., & Biljecki, F. (2022). A review of spatially-explicit GeoAI applications in Urban 

Jenkins, P., Farag, A., Wang, S., & Li, Z. (2019). Unsupervised representation learning of Geography. International Journal of Applied Earth Observation and Geoinformation, 
spatial data via multimodal embedding. In Proceedings of the 28th ACM international 112, Article 102936. https://doi.org/10.1016/j.jag.2022.102936 
conference on information and knowledge management (pp. 1993–2002). New York, Liu, S., Zhang, L., & Long, Y. (2019b). Urban vitality area identification and pattern 
NY, USA: Association for Computing Machinery. https://doi.org/10.1145/ analysis from the perspective of time and space fusion. Sustainability, 11, 4032. 
3357384.3358001.  https://doi.org/10.3390/su11154032 

Jing, L., & Tian, Y. (2019). Self-supervised visual feature learning with deep neural networks: Liu, X., Huang, Q., Gao, S., & Xia, J. (2021a). Activity knowledge discovery: Detecting 
A survey. https://doi.org/10.48550/arXiv.1902.06162. arXiv:1902.06162. collective and individual activities with digital footprints and open source 

Jing, Y., Shu, J., Wang, R., & Zhang, X. (2021). Tempo-spatial variability of urban leisure geographic data. Computers Environment and Urban Systems, 85, Article 101551. 
functional zones: An analysis based on geo-big data. Growth and Change, 52, https://doi.org/10.1016/j.compenvurbsys.2020.101551 
1852–1865. https://doi.org/10.1111/grow.12526 Liu, Y., Singleton, A., & Arribas-Bel, D. (2020b). Considering context and dynamics: A 

Jochem, W. C., Leasure, D. R., Pannell, O., Chamberlain, H. R., Jones, P., & Tatem, A. J. classification of transit-orientated development for New York City. Journal of 
(2021). Classifying settlement types from multi-scale spatial patterns of building Transport Geography, 85, Article 102711. https://doi.org/10.1016/j. 
footprints. Environment and Planning B: Urban Analytics and City Science, 48, jtrangeo.2020.102711 
1161–1179. https://doi.org/10.1177/2399808320921208 Liu, Y., Singleton, A., Arribas-bel, D., & Chen, M. (2021b). Identifying and understanding 

Johnson, B., & Xie, Z. (2011). Unsupervised image segmentation evaluation and road-constrained areas of interest (AOIs) through spatiotemporal taxi GPS data: A 
refinement using a multi-scale approach. ISPRS Journal of Photogrammetry and case study in New York City. Computers Environment and Urban Systems, 86, Article 
Remote Sensing, 66, 473–483. https://doi.org/10.1016/j.isprsjprs.2011.02.006 101592. https://doi.org/10.1016/j.compenvurbsys.2020.101592 

Karimi, J. D., Corstanje, R., & Harris, J. A. (2021). Bundling ecosystem services at a high Lopes, M., Mélice Dias, A., & Silva, C. (2021). The impact of urban features in cycling 
resolution in the UK: Trade-offs and synergies in urban landscapes. Landscape potential – A tale of Portuguese cities. Journal of Transport Geography, 95, Article 
Ecology, 36, 1817–1835. https://doi.org/10.1007/s10980-021-01252-4 103149. https://doi.org/10.1016/j.jtrangeo.2021.103149 

Keirstead, J., & Leach, M. (2008). Bridging the gaps between theory and practice: A Lu, D., Tian, Y., Liu, V. Y., & Zhang, Y. (2015). The performance of the smart cities in 
service niche approach to urban sustainability indicators. Sustainable Development, China-A comparative study by means of self-organizing maps and social networks 
16, 329–340. https://doi.org/10.1002/sd.349 analysis. Sustainability, 7, 7604–7621. https://doi.org/10.3390/su7067604 

Kim, K. (2020a). Identifying the structure of cities by clustering using a new similarity Lyu, R., Clarke, K. C., Zhang, J., Jia, X., Feng, J., & Li, J. (2019). The impact of 
measure based on smart card data. IEEE Transactions on Intelligent Transportation urbanization and climate change on ecosystem services: A case study of the city belt 
Systems, 21, 2002–2011. https://doi.org/10.1109/TITS.2019.2910548 along the Yellow River in Ningxia,China. Computers Environment and Urban Systems, 

Kim, Y. L. (2020b). Data-driven approach to characterize urban vitality: How 77, Article 101351. https://doi.org/10.1016/j.compenvurbsys.2019.101351 
spatiotemporal context dynamically defines Seoul's nighttime. International Journal Ma, L., Liu, Y., Zhang, X., Ye, Y., Yin, G., & Johnson, B. (2019). Deep learning in remote 
of Geographical Information Science, 34, 1235–1256. https://doi.org/10.1080/ sensing applications: A meta-analysis and review. ISPRS Journal of Photogrammetry 
13658816.2019.1694680 and Remote Sensing, 152, 166–177. https://doi.org/10.1016/j.isprsjprs.2019.04.015 

Kit, O., Luedeke, M., & Reckien, D. (2012). Texture-based identification of urban slums in Manley, E., & Dennett, A. (2019). New forms of data for understanding urban activity in 
Hyderabad, India using remote sensing data. Applied Geography, 32, 660–667. developing countries. Applied Spatial Analysis and Policy, 12, 45–70. https://doi.org/ 
https://doi.org/10.1016/j.apgeog.2011.07.016 10.1007/s12061-018-9264-8 

Kohonen, T. (1990). The self-organizing map. Proceedings of the IEEE, 78, 1464–1480. Manley, E., Zhong, C., & Batty, M. (2018). Spatiotemporal variation in travel regularity 
https://doi.org/10.1109/5.58325 through transit user profiling. Transportation, 45, 703–732. https://doi.org/ 

Kropp, J. (1998). A neural network approach to the analysis of city systems. Applied 10.1007/s11116-016-9747-x 
Geography, 18, 83–96. https://doi.org/10.1016/S0143-6228(97)00048-9 Martins, M. S., Locatelli Kalil, R. M., & Dalla Rosa, F. (2021). Sustainable 

Krtalic, A., Linardic, D., & Pernar, R. (2021). Framework for spatial and temporal neighbourhoods: Applicable indicators through principal component analysis. 
monitoring of urban forest and vegetation conditions: Case study Zagreb,Croatia. Proceedings of the Institution of Civil Engineers-Urban Design and Planning, 174, 25–36. 
Sustainability, 13, 6055. https://doi.org/10.3390/su13116055 https://doi.org/10.1680/jurdp.20.00058 

Kwon, Y. J., Lee, D. K., Kim, J. H., & Oh, K. (2021). Improving urban thermal Miao, R., Wang, Y., & Li, S. (2021). Analyzing urban spatial patterns and functional zones 
environments by analysing sensible heat flux patterns in zoning districts. Cities, 116, using Sina Weibo POI data: A case study of Beijing. Sustainability, 13, 647. https:// 
Article 103276. https://doi.org/10.1016/j.cities.2021.103276 doi.org/10.3390/su13020647 

Landauer, T. K., Foltz, P. W., & Laham, D. (1998). An introduction to latent semantic Mikelbank, B. (2004). A typology of US suburban places. HOUSING POLICY DEBATE. 15, 
analysis. Discourse Processes, 25, 259–284. https://doi.org/10.1080/ 935–964. https://doi.org/10.1080/10511482.2004.9521527, 99th Annual Meeting 
01638539809545028 of the Association-of-American-Geographers, NEW ORLEANS, LA, MAR 05-08, 2003. 

LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. Nature, 521, 436–444. https:// Miller, C., Nagy, Z., & Schlueter, A. (2018). A review of unsupervised statistical learning 
doi.org/10.1038/nature14539 and visual analytics techniques applied to performance analysis of non-residential 

Lemoine-Rodriguez, R., Inostroza, L., & Zepp, H. (2020). The global homogenization of buildings. Renewable and Sustainable Energy Reviews, 81, 1365–1377. https://doi. 
urban form. An assessment of 194 cities across time. Landscape and Urban Planning, org/10.1016/j.rser.2017.05.124 
204, Article 103949. https://doi.org/10.1016/j.landurbplan.2020.103949 Mohammady, M., Moradi, H. R., Zeinivand, H., & Temme, A. J. A. M. (2015). 

Lever, J., Krzywinski, M., & Altman, N. (2017). Principal component analysis. Nature A comparison of supervised, unsupervised and synthetic land use classification 
Methods, 14, 641–642. https://doi.org/10.1038/nmeth.4346 

18



J. Wang and F. Biljecki                                                                                                                                                                                                               C  i t i e  s  129 (2022) 103925

methods in the north of Iran. International Journal of Environmental Science and Rios, S. A., & Munoz, R. (2017). Land use detection with cell phone data using topic 
Technology, 12, 1515–1526. https://doi.org/10.1007/s13762-014-0728-3 models: Case Santiago, Chile. Computers Environment and Urban Systems, 61, 39–48. 

Moher, D., Liberati, A., Tetzlaff, J., Altman, D. G., & Group, T. P. (2009). Preferred https://doi.org/10.1016/j.compenvurbsys.2016.08.007 
reporting items for systematic reviews and meta-analyses: The PRISMA statement. Roof, K., & Oleru, N. (2008). Public health: Seattle and King County's push for the built 
PLOS Medicine, 6, Article e1000097. https://doi.org/10.1371/journal. environment. Journal of Environmental Health, 71, 24–27. 
pmed.1000097 Sagl, G., Delmelle, E., & Delmelle, E. (2014). Mapping collective human activity in an 

Naikoo, M. W., Rihan, M., Ishtiaque, M., & Shahfahad. (2020). Analyses of land use land urban environment based on mobile phone data. Cartography and Geographic 
cover (LULC) change and built-up expansion in the suburb of a metropolitan city: Information Science, 41, 272–285. https://doi.org/10.1080/15230406.2014.888958 
Spatio-temporal analysis of Delhi NCR using Landsat datasets. Journal of Urban Samany, N. N. (2019). Automatic landmark landmark extraction from geo-tagged social 
Management, 9, 347–359. https://doi.org/10.1016/j.jum.2020.05.004 media photos using deep neural network. Cities, 93, 1–12. https://doi.org/10.1016/ 

Ng, A. Y., Jordan, M. I., & Weiss, Y. (2001). On spectral clustering: Analysis and an j.cities.2019.04.012 
algorithm. In Proceedings of the 14th international conference on neural information Schmidhuber, J. (2015). Deep learning in neural networks: An overview. Neural 
processing systems: Natural and synthetic (pp. 849–856). Cambridge, MA, USA: MIT Networks, 61, 85–117. https://doi.org/10.1016/j.neunet.2014.09.003 
Press.  Schmiedel, I., Bergmeier, E., & Culmsee, H. (2015). Plant species richness patterns along 

Nguyen, L., Embrechts, J. J., & Teller, J. (2020). Colour in the city: A chromatic typology a gradient of landscape modification intensity in Lower Saxony, Germany. Landscape 
for the quantitative analysis of spatial coherence. Landscape Research, 45, 44–62. and Urban Planning, 141, 41–51. https://doi.org/10.1016/j. 
https://doi.org/10.1080/01426397.2019.1589437 landurbplan.2015.03.009 

Oh, M., & Kim, Y. (2019). Identifying urban geometric types as energy performance Schneider, A. (2012). Monitoring land cover change in urban and peri-urban areas using 
patterns. Energy for Sustainable Development, 48, 115–129. https://doi.org/10.1016/ dense time stacks of Landsat satellite data and a data mining approach. Remote 
j.esd.2018.12.002 Sensing of Environment, 124, 689–704. https://doi.org/10.1016/j.rse.2012.06.006 

Oldoni, D., De Coensel, B., Bockstael, A., Boes, M., De Baets, B., & Botteldooren, D. Serra, P., Vera, A., & Francesc Tulla, A. (2014). Spatial and socio-environmental 
(2015). The acoustic summary as a tool for representing urban sound environments. dynamics of Catalan regional planning from a multivariate statistical analysis using 
Landscape and Urban Planning, 144, 34–48. https://doi.org/10.1016/j. 1980s and 2000s data. European Planning Studies, 22, 1280–1300. https://doi.org/ 
landurbplan.2015.08.013 10.1080/09654313.2013.782388 

Olson, A. W., Calderon-Figueroa, F., Bidian, O., Silver, D., & Sanner, S. (2021). Reading Singh, D., & Mohan, C. K. (2019). Deep spatio-temporal representation for detection of 
the city through its neighbourhoods: Deep text embeddings of Yelp reviews as a basis road accidents using stacked autoencoder. IEEE Transactions on Intelligent 
for determining similarity and change. Cities, 110, Article 103045. https://doi.org/ Transportation Systems, 20, 879–887. https://doi.org/10.1109/TITS.2018.2835308 
10.1016/j.cities.2020.103045 Sohn, K. (2013). Feature mapping the Seoul Metro Station areas based on a self- 

Ouyang, Q., Lv, Y., Ren, Y., Ma, J., & Li, J. (2018). Passenger travel regularity analysis organizing map. Journal of Urban Technology, 20, 23–42. https://doi.org/10.1080/ 
based on a large scale smart card data. Journal of Advanced Transportation, 9457486. 10630732.2013.855514 
https://doi.org/10.1155/2018/9457486 Sparks, K., Thakur, G., Pasarkar, A., & Urban, M. (2020). A global analysis of 

Owen, S. M., MacKenzie, A. R., Bunce, R. G. H., Stewart, H. E., Donovan, R. G., Stark, G., cities'geosocial temporal signatures for points of interest hours of operation. 
& Hewitt, C. N. (2006). Urban land classification and its uncertainties using principal International Journal of Geographical Information Science, 34, 759–776. https://doi. 
component and cluster analyses: A case study for the UK West Midlands. Landscape org/10.1080/13658816.2019.1615069 
and Urban Planning, 78, 311–321. https://doi.org/10.1016/j. Steiger, E., Resch, B., & Zipf, A. (2016). Exploration of spatiotemporal and semantic 
landurbplan.2005.11.002 clusters of Twitter data using unsupervised neural networks. International Journal of 

Ozus, E., Akin, D., & Ciftci, M. (2012). Hierarchical cluster analysis of multicenter Geographical Information Science, 30, 1694–1716. https://doi.org/10.1080/ 
development and travel patterns in Istanbul. Journal of Urban Planning and 13658816.2015.1099658 
Development, 138, 303–318. https://doi.org/10.1061/(ASCE)UP.1943- Su, S., He, S., Sun, C., Zhang, H., Hu, L., & Kang, M. (2021). Do landscape amenities 
5444.0000121 impact private housing rental prices? A hierarchical hedonic modeling approach 

Papadakis, E., Gao, S., & Baryannis, G. (2019). Combining design patterns and topic based on semantic and sentimental analysis of online housing advertisements across 
modeling to discover regions that support particular functionality. ISPRS five Chinese megacities. Urban Forestry & Urban Greening, 58, Article 126968. 
International Journal of Geo-Information, 8, 385. https://doi.org/10.3390/ https://doi.org/10.1016/j.ufug.2020.126968 
ijgi8090385 Sun, H., Chen, Y., Lai, J., Wang, Y., & Liu, X. (2021). Identifying tourists and locals by K- 

Park, J. Y., Ryu, D. J., Nam, K. W., Jang, I., Jang, M., & Lee, Y. (2021). DeepDBSCAN: means clustering method from mobile phone signaling data. Journal of Transportation 
Deep density-based clustering for geo-tagged photos. ISPRS International Journal of Engineering, Part A: Systems, 147, 04021070. https://doi.org/10.1061/ 
Geo-Information, 10, 548. https://doi.org/10.3390/ijgi10080548 JTEPBS.0000580 

Paul, A., & Sen, J. (2018). Livability assessment within a metropolis based on the impact Sun, L., & Axhausen, K. W. (2016). Understanding urban mobility patterns with a 
of integrated urban geographic factors (IUGFs) on clustering urban centers of probabilistic tensor factorization framework. Transportation Research Part B- 
Kolkata. Cities, 74, 142–150. https://doi.org/10.1016/j.cities.2017.11.015 Methodological, 91, 511–524. https://doi.org/10.1016/j.trb.2016.06.011 

Paulvannan Kanmani, A., Obringer, R., Rachunok, B., & Nateghi, R. (2020). Assessing Sun, S., Zhang, C., & Yu, G. (2006). A Bayesian network approach to traffic flow 
global environmental sustainability via an unsupervised clustering framework. forecasting. IEEE Transactions on Intelligent Transportation Systems, 7, 124–132. 
Sustainability, 12, 563. https://doi.org/10.3390/su12020563 https://doi.org/10.1109/TITS.2006.869623 

Pavlis, M., Dolega, L., & Singleton, A. (2018). A modified DBSCAN clustering method to Sun, Y., Fan, H., Li, M., & Zipf, A. (2016). Identifying the city center using human travel 
estimate retail center extent. Geographical Analysis, 50, 141–161. https://doi.org/ flows generated from location-based social networking data. Environment and 
10.1111/gean.12138 Planning B-Planning & Design, 43, 480–498. https://doi.org/10.1177/ 

Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., 0265813515617642 
Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., & Taecharungroj, V., & Mathayomchan, B. (2020). The big picture of cities: Analysing 
Cournapeau, D. (2011). Scikit-learn: Machine learning in Python. In , 6. Machine Flickr photos of 222 cities worldwide. Cities, 102, Article 102741. https://doi.org/ 
learning in Python. 10.1016/j.cities.2020.102741 

Peng, B., Huang, Q., Vongkusolkit, J., Gao, S., Wright, D. B., Fang, Z. N., & Qiang, Y. Tang, D., Li, B., Qiu, Y., & Zhao, L. (2020). Research on urban and rural coordination 
(2021). Urban flood mapping with bitemporal multispectral imagery via a self- development and its driving force based on the space-time evolvement taking 
supervised learning framework. IEEE Journal of Selected Topics in Applied Earth Guangdong Province as an example. Land, 9, 253. https://doi.org/10.3390/ 
Observations and Remote Sensing, 14, 2001–2016. https://doi.org/10.1109/ land9080253 
JSTARS.2020.3047677 Tao, H., Wang, K., Zhuo, L., & Li, X. (2019). Re-examining urban region and inferring 

Pieroni, C., Giannotti, M., Alves, B. B., & Arbex, R. (2021). Big data for big issues: regional function based on spatial-temporal interaction. International Journal of 
Revealing travel patterns of low-income population based on smart card data mining Digital Earth, 12, 293–310. https://doi.org/10.1080/17538947.2018.1425490 
in a global south unequal city. Journal of Transport Geography, 96, Article 103203. Tessler, Z. D., Vorosmarty, C. J., Grossberg, M., Gladkova, I., & Aizenman, H. (2016). 
https://doi.org/10.1016/j.jtrangeo.2021.103203 A global empirical typology of anthropogenic drivers of environmental change in 

Qi, J., Liu, H., Liu, X., & Zhang, Y. (2019). Spatiotemporal evolution analysis of time- deltas. Sustainability Science, 11, 525–537. https://doi.org/10.1007/s11625-016- 
series land use change using self-organizing map to examine the zoning and scale 0357-5 
effects. Computers Environment and Urban Systems, 76, 11–23. https://doi.org/ Tu, K. J., & Lin, L. T. (2008). Evaluative structure of perceived residential environment 
10.1016/j.compenvurbsys.2019.03.002 quality in high-density and mixed-use urban settings: An exploratory study on Taipei 

Rahman, M. S., Mohiuddin, H., Kafy, A. A., Sheel, P. K., & Di, L. (2019). Classification of City. Landscape and Urban Planning, 87, 157–171. https://doi.org/10.1016/j. 
cities in Bangladesh based on remote sensing derived spatial characteristics. Journal landurbplan.2008.05.009 
of Urban Management, 8, 206–224. https://doi.org/10.1016/j.jum.2018.12.001 Ullah, Z., Al-Turjman, F., Mostarda, L., & Gagliardi, R. (2020). Applications of artificial 

Ranjan, N., Bhandari, S., Khan, P., Hong, Y. S., & Kim, H. (2021). Large-scale road intelligence and machine learning in smart cities. Computer Communications, 154, 
network congestion pattern analysis and prediction using deep convolutional 313–323. https://doi.org/10.1016/j.comcom.2020.02.069 
autoencoder. Sustainability, 13, 5108. https://doi.org/10.3390/su13095108 Usama, M., Qadir, J., Raza, A., Arif, H., Yau, K. L. A., Elkhatib, Y., Hussain, A., & Al- 

Rasheed, A., San, O., & Kvamsdal, T. (2020). Digital twin: Values, challenges and Fuqaha, A. (2019). Unsupervised machine learning for networking: techniques, 
enablers from a modeling perspective. IEEE Access, 8, 21980–22012. https://doi. applications and research challenges. IEEE Access, 7, 65579–65615. https://doi.org/ 
org/10.1109/ACCESS.2020.2970143 10.1109/ACCESS.2019.2916648 

Richards, D. R., & Tuncer, B. (2018). Using image recognition to automate assessment of van der Maaten, L., & Hinton, G. (2008). Viualizing data using t-SNE. Journal of Machine 
cultural ecosystem services from social media photographs. Ecosystem Services, 31, Learning Research, 9, 2579–2605. 
318–325. https://doi.org/10.1016/j.ecoser.2017.09.004 

19



J. Wang and F. Biljecki                                                                                                                                                                                                               C  i t i e  s  129 (2022) 103925

Verma, P., & Raghubanshi, A. S. (2018). Urban sustainability indicators: Challenges and Yap, W., Janssen, P., & Biljecki, F. (2022). Free and open source urbanism: Software for 
opportunities. Ecological Indicators, 93, 282–291. https://doi.org/10.1016/j. urban planning practice. Computers, Environment and Urban Planning, 96, Article 
ecolind.2018.05.007 101825. https://doi.org/10.1016/j.compenvurbsys.2022.101825 

Vizzari, M., & Sigura, M. (2015). Landscape sequences along the urban-rural-natural Ye, S., & Chen, D. (2015). An unsupervised urban change detection procedure by using 
gradient: A novel geospatial approach for identification and analysis. Landscape and luminance and saturation for multispectral remotely sensed images. Photogrammetric 
Urban Planning, 140, 42–55. https://doi.org/10.1016/j.landurbplan.2015.04.001 Engineering and Remote Sensing, 81, 637–645. https://doi.org/10.14358/ 

Wang, Y., Qin, K., Chen, Y., & Zhao, P. (2018). Detecting anomalous trajectories and PERS.81.8.637 
behavior patterns using hierarchical clustering from taxi GPS data. ISPRS You, G. (2021). Spatiotemporal data-adaptive clustering algorithm: An intelligent 
International Journal of Geo-Information, 7, 25. https://doi.org/10.3390/ijgi7010025 computational technique for city big data. Annals of the American Association of 

Wang, Y., & Taylor, J. E. (2019). DUET: Data-driven approach based on latent Dirichlet Geographers, 1–18. https://doi.org/10.1080/24694452.2021.1935207 
allocation topic modeling. Journal of Computing in Civil Engineering, 33, Article Yu, C., & He, Z. C. (2017). Analysing the spatial-temporal characteristics of bus travel 
04019023. https://doi.org/10.1061/(ASCE)CP.1943-5487.0000819 demand using the heat map. Journal of Transport Geography, 58, 247–255. https:// 

Wang, Z., Liu, H., Zhu, Y., Zhang, Y., Basiri, A., Buettner, B., Gao, X., & Cao, M. (2021). doi.org/10.1016/j.jtrangeo.2016.11.009 
Identifying urban functional areas and their dynamic changes in Beijing: Using Yu, C., Li, H., Xu, X., Liu, J., Miao, J., Wang, Y., & Sun, Q. (2021). Data-driven approach 
multiyear transit smart card data. Journal of Urban Planning and Development, 147, for passenger mobility pattern recognition using spatiotemporal embedding. Journal 
Article 04021002. https://doi.org/10.1061/(ASCE)UP.1943-5444.0000662 of Advanced Transportation, 2021, Article e5574093. https://doi.org/10.1155/2021/ 

Wijnands, J. S., Nice, K. A., Thompson, J., Zhao, H., & Stevenson, M. (2019). Streetscape 5574093 
augmentation using generative adversarial networks: Insights related to health and Yu, L., Yu, T., Wu, Y., & Wu, G. (2020). Rethinking the identification of urban centers 
wellbeing. Sustainable Cities and Society, 49, Article 101602. https://doi.org/ from the perspective of function distribution: A framework based on point-of-interest 
10.1016/j.scs.2019.101602 data. Sustainability, 12, 1543. https://doi.org/10.3390/su12041543 

Wold, S., Esbensen, K., & Geladi, P. (1987). Principal component analysis. Chemometrics Yuan, G., Chen, Y., Sun, L., Lai, J., Li, T., & Liu, Z. (2020). Recognition of functional areas 
and Intelligent Laboratory Systems, 2, 37–52. https://doi.org/10.1016/0169-7439(87) based on call detail records and point of interest data. Journal of Advanced 
80084-9 Transportation, 2020, Article 8956910. https://doi.org/10.1155/2020/8956910 

Wu, A. N., & Biljecki, F. (2022). GANmapper: Geographical data translation. International Yuan, J., Beard, K., & Johnson, T. R. (2021). A quantitative assessment of spatial patterns 
Journal of Geographical Information Science, 36, 1394–1422. https://doi.org/ of socio-demographic change in coastal Maine: One process or many? Applied 
10.1080/13658816.2022.2041643 Geography, 134, Article 102502. https://doi.org/10.1016/j.apgeog.2021.102502 

Wu, C., Peng, N., Ma, X., Li, S., & Rao, J. (2020). Assessing multiscale visual appearance Yue, M., Kang, C., Andris, C., Qin, K., Liu, Y., & Meng, Q. (2018). Understanding the 
characteristics of neighbourhoods using geographically weighted principal interplay between bus, metro, and cab ridership dynamics in Shenzhen, China. 
component analysis in Shenzhen,China. Computers Environment and Urban Systems, Transactions in GIS, 22, 855–871. https://doi.org/10.1111/tgis.12340 
84, Article 101547. https://doi.org/10.1016/j.compenvurbsys.2020.101547 Zawadzka, J. E., Harris, J. A., & Corstanje, R. (2021). A simple method for determination 

Xi, W., Calder, C. A., & Browning, C. R. (2020). Beyond activity space: Detecting of fine resolution urban form patterns with distinct thermal properties using class- 
communities in ecological networks. Annals of the American Association of level landscape metrics. Landscape Ecology, 36, 1863–1876. https://doi.org/ 
Geographers, 110, 1787–1806. https://doi.org/10.1080/24694452.2020.1715779 10.1007/s10980-020-01156-9 

Xing, Y., Wang, K., & Lu, J. J. (2020). Exploring travel patterns and trip purposes of Zhan, S., Chong, A., & Lasternas, B. (2021). Automated recognition and mapping of 
dockless bike-sharing by analyzing massive bike-sharing data in Shanghai,China. building management system (bms) data points for building energy modeling (bem). 
Journal of Transport Geography, 87, Article 102787. https://doi.org/10.1016/j. Building Simulation, 14, 43–52. https://doi.org/10.1007/s12273-020-0612-7 
jtrangeo.2020.102787 Zhan, S., Liu, Z., Chong, A., & Yan, D. (2020). Building categorization revisited: A 

Xu, C., Liu, M., Hong, C., Chi, T., An, S., & Yang, X. (2012). Temporal variation of clustering-based approach to using smart meter data for building energy 
characteristic scales in urban landscapes: An insight into the evolving internal benchmarking. Applied Energy, 269, Article 114920. https://doi.org/10.1016/j. 
structures of China's two largest cities. Landscape Ecology, 27, 1063–1074. https:// apenergy.2020.114920 
doi.org/10.1007/s10980-012-9764-x Zhang, X., Li, W., Zhang, F., Liu, R., & Du, Z. (2018). Identifying urban functional zones 

Xu, D., Zhou, D., Wang, Y., Meng, X., Chen, W., & Yang, Y. (2020). Temporal and spatial using public bicycle rental records and point-of-interest data. ISPRS International 
variations of urban climate and derivation of an urban climate map for Xi'an,China. Journal of Geo-Information, 7, 459. https://doi.org/10.3390/ijgi7120459 
Sustainable Cities and Society, 52, Article 101850. https://doi.org/10.1016/j. Zhang, Y., Wang, S., Chen, B., Cao, J., & Huang, Z. (2021). TrafficGAN: Network-scale 
scs.2019.101850 deep traffic prediction with generative adversarial nets. IEEE Transactions on 

Xu, H., Ma, C., Lian, J., Xu, K., & Chaima, E. (2018). Urban flooding risk assessment Intelligent Transportation Systems, 22, 219–230. https://doi.org/10.1109/ 
based on an integrated k-means cluster algorithm and improved entropy weight TITS.2019.2955794 
method in the region of Haikou, China. Journal of Hydrology, 563, 975–986. https:// Zhao, F., Fashola, O. I., Olarewaju, T. I., & Onwumere, I. (2021). Smart city research: A 
doi.org/10.1016/j.jhydrol.2018.06.060 holistic and state-of-the-art literature review. Cities, 119, Article 103406. https://doi. 

Xu, R., & Wunsch, D. C. (2010). Clustering algorithms in biomedical research: A review. org/10.1016/j.cities.2021.103406 
IEEE Reviews in Biomedical Engineering, 3, 120–154. https://doi.org/10.1109/ Zhao, J., Mathieu, M., & LeCun, Y. (2017). Energy-based generative adversarial network. 
RBME.2010.2083647 arXiv:1609.03126 [cs, stat] arXiv:1609.03126. comment: Submitted to ICLR 2017. 

Xue, F., Lu, W., Chen, Z., & Webster, C. J. (2020). From LiDAR point cloud towards Zheng, Y., Capra, L., Wolfson, O., & Yang, H. (2014). Urban computing: Concepts, 
digital twin city: Clustering city objects based on gestalt principles. ISPRS Journal of methodologies, and applications. ACM Transactions on Intelligent Systems and 
Photogrammetry and Remote Sensing, 167, 418–431. https://doi.org/10.1016/j. Technology, 5, 1–55. https://doi.org/10.1145/2629592 
isprsjprs.2020.07.020 Zhong, C., Zeng, S., Tu, W., & Yoshida, M. (2018). Profiling the spatial structure of 

Xue, Q., Yang, X., & Wu, F. (2021). A two-stage system analysis of real and pseudo urban London: From individual tweets to aggregated functional zones. ISPRS International 
human settlements in China. Journal of Cleaner Production, 293, Article 126272. Journal of Geo-Information, 7, 386. https://doi.org/10.3390/ijgi7100386 
https://doi.org/10.1016/j.jclepro.2021.126272 Zivkovic, Z. (2004). Improved adaptive Gaussian mixture model for background 

Yang, Y., Zheng, H., Xu, W., Zhang, L., & Ouyang, Z. (2019). Temporal changes in subtraction. In , Vol.2. Proceedings of the 17th international conference on pattern 
multiple ecosystem services and their bundles responding to urbanization and recognition, 2004. ICPR 2004 (pp. 28–31). https://doi.org/10.1109/ 
ecological restoration in the Beijing-Tianjin-Hebei metropolitan area. Sustainability, ICPR.2004.1333992 
11, 2079. https://doi.org/10.3390/su11072079 Zuo, F., Kurkcu, A., Ozbay, K., & Gao, J. (2018). Crowdsourcing incident information for 

emergency response using open data sources in smart cities. Transportation Research 
Record, 2672, 198–208. https://doi.org/10.1177/0361198118798736 

20