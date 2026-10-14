---
source_file: "2024-Toward a responsible future- recommendations for AI-enabled clinical decision support.txt"
original_rel_path: "Trabalhos\Artigos\Aproveitar parcialmente\txt\2024-Toward a responsible future- recommendations for AI-enabled clinical decision support.txt"
category: "Artigos_Aproveitar_parcialmente"
extension: ".txt"
sha256: "2593d6da1256cff7d34086cb062709d4d45b8a8eed697e68559e0a787122ea26"
extracted_at: "2026-09-20T00:50:21.683278"
---

﻿Journal of the American Medical Informatics Association, 2024, 31(11), 2730–2739 
https://doi.org/10.1093/jamia/ocae209 
Advance access publication 26 September 2024 
Case Report 

Case Report

Toward a responsible future: recommendations for 
AI-enabled clinical decision support
Steven Labkoff , MD1,2, Bilikis Oladimeji , MBBS, MMCi3, Joseph Kannry , MD4,  
Anthony Solomonides , PhD5, Russell Leftwich , MD6, Eileen Koski , MPhil7,  
Amanda L. Joseph , MSc8, Monica Lopez-Gonzalez , PhD9, Lee A. Fleisher , MD10,  
Kimberly Nolen , BS, PharmD11, Sayon Dutta , MD, MPH12,13,14,  
Deborah R. Levy , MD, MPH, MS15,16, Amy Price , DPhil17,18, Paul J. Barr , PhD17,  
Jonathan D. Hron , MD19,20, Baihan Lin , PhD21,22, Gyana Srivastava , BA2,23,  
Nuria Pastor , MSc24, Unai Sanchez Luque , MSc24, Tien Thi Thuy Bui , PharmD25,  
Reva Singh , JD26, Tayler Williams , BA26, Mark G. Weiner , MD27, Tristan Naumann , PhD28,  
Dean F. Sittig , PhD29, Gretchen Purcell Jackson , MD, PhD30,31 and Yuri Quintana , PhD�,2,8,14,32 

1Quantori, Boston, MA 02142, United States, 2Division of Clinical Informatics, Department of Medicine, Beth Israel Deaconess Medical 
Center, Boston, MA 02215, United States, 3UnitedHealth Group, Minnetonka, MN, United States, 4Division of General Internal Medicine, 
Department of Medicine, Icahn School of Medicine at Mount Sinai, New York, NY 10029, United States, 5Research Institute, Endeavor 
Health, Evanston, IL 60035, United States, 6Department of Biomedical Informatics, Vanderbilt University, Nashville, TN, United States, 7IBM 
Research, Yorktown Heights, NY, United States, 8School of Health Information Science, University of Victoria, Victoria, BC, Canada, 
9Cognitive Insights for Artificial Intelligence, Baltimore, MD, United States, 10Anesthesiology and Critical Care, University of Pennsylvania 
Perelman School of Medicine, Philadelphia, PA, United States, 11Pfizer Inc, New York, NY, United States, 12Department of Emergency 
Medicine, Massachusetts General Hospital, Boston, MA, United States, 13Clinical Informatics, Mass General Brigham Digital, Boston, MA, 
United States, 14Harvard Medical School, Boston, MA, United States, 15Department of Medicine, Pain Research Informatics Multimorbidities 
and Epidemiology (PRIME) Center, VA-Connecticut Healthcare System, West Haven, CT, United States, 16Department of Biomedical 
Informatics and Data Sciences, Yale School of Medicine, New Haven, CT, United States, 17The Dartmouth Institute for Health Policy and 
Clinical Practice, Geisel School of Medicine at Dartmouth, Hanover, NH, United States, 18BMJ, London, United Kingdom, 19Department of 
Pediatrics, Division of General Pediatrics, Boston Children’s Hospital, Boston, MA 02115, United States, 20Department of Pediatrics, Harvard 
Medical School, Boston, MA 02115, United States, 21Departments of AI, Psychiatry, and Neuroscience, Icahn School of Medicine at Mount 
Sinai, New York, NY, United States, 22Berkman Klein Center for Internet and Society, Harvard Law School, Cambridge, MA, United States, 
23Harvard School of Public Health, Boston, MA 02115, United States, 24Vitalera, Barcelona 08028, Spain, 25Massachusetts College of 
Pharmacy and Health Sciences, Boston, MA, United States, 26American Medical Informatics Association, Washington, DC, United States, 
27Department of Population Health Sciences, Weill Cornell Medicine, New York, NY, United States, 28Microsoft Research, Redmond, WA, 
United States, 29Department of Clinical and Health Informatics, University of Texas Health Science Center, Houston, TX, United States, 
30Intuitive Surgical, Nashville, TN, United States, 31Department of Pediatrics and Biomedical Informatics, Vanderbilt University Medical 
Center, Nashville, TN, United States, 32Homewood Research Institute, Guelph, ON, Canada
�Corresponding author: Yuri Quintana, PhD, Division of Clinical Informatics, Beth Israel Deaconess Medical Center, 133 Brookline Avenue, HVMA Annex, 
Suite 2200, Boston, MA 02215, United States (yquintan@bidmc.harvard.edu)

Abstract
Background: Integrating artificial intelligence (AI) in healthcare settings has the potential to benefit clinical decision-making. Addressing chal
lenges such as ensuring trustworthiness, mitigating bias, and maintaining safety is paramount. The lack of established methodologies for pre- 
and post-deployment evaluation of AI tools regarding crucial attributes such as transparency, performance monitoring, and adverse event 
reporting makes this situation challenging.
Objectives: This paper aims to make practical suggestions for creating methods, rules, and guidelines to ensure that the development, testing, 
supervision, and use of AI in clinical decision support (CDS) systems are done well and safely for patients.
Materials and Methods: In May 2023, the Division of Clinical Informatics at Beth Israel Deaconess Medical Center and the American Medical 
Informatics Association co-sponsored a working group on AI in healthcare. In August 2023, there were 4 webinars on AI topics and a 2-day 
workshop in September 2023 for consensus-building. The event included over 200 industry stakeholders, including clinicians, software develop
ers, academics, ethicists, attorneys, government policy experts, scientists, and patients. The goal was to identify challenges associated with 
the trusted use of AI-enabled CDS in medical practice. Key issues were identified, and solutions were proposed through qualitative analysis and 
a 4-month iterative consensus process.
Results: Our work culminated in several key recommendations: (1) building safe and trustworthy systems; (2) developing validation, verification, 
and certification processes for AI-CDS systems; (3) providing a means of safety monitoring and reporting at the national level; and (4) ensuring 
that appropriate documentation and end-user training are provided.

Received: February 25, 2024; Revised: July 8, 2024; Editorial Decision: July 22, 2024; Accepted: August 13, 2024 
© The Author(s) 2024. Published by Oxford University Press on behalf of the American Medical Informatics Association.  This is an Open Access article 
distributed under the terms of the Creative Commons Attribution-NonCommercial-NoDerivs licence (https://creativecommons.org/licenses/by-nc-nd/4.0/), 
which permits non-commercial reproduction and distribution of the work, in any medium, provided the original work is not altered or transformed in any way, 
and that the work is properly cited. For commercial re-use, please contact journals.permissions@oup.com 

Downloaded from https://academic.oup.com/jamia/article/31/11/2730/7776823 by guest on 28 October 2024



Journal of the American Medical Informatics Association, 2024, Vol. 31, No. 11                                                                                        2  7  3  1    

Discussion: AI-enabled Clinical Decision Support (AI-CDS) systems promise to revolutionize healthcare decision-making, necessitating a com
prehensive framework for their development, implementation, and regulation that emphasizes trustworthiness, transparency, and safety. This 
framework encompasses various aspects including model training, explainability, validation, certification, monitoring, and continuous evaluation, 
while also addressing challenges such as data privacy, fairness, and the need for regulatory oversight to ensure responsible integration of AI 
into clinical workflow.
Conclusions: Achieving responsible AI-CDS systems requires a collective effort from many healthcare stakeholders. This involves implement
ing robust safety, monitoring, and transparency measures while fostering innovation. Future steps include testing and piloting proposed trust 
mechanisms, such as safety reporting protocols, and establishing best practice guidelines.
Key words: clinical decision support; artificial intelligence; clinician AI competencies; patient safety; algorithmic transparency. 

Introduction Notably, with the introduction of large language models in 
In the early stages of clinical informatics, clinical decision November of 2022, interest in integrating AI into CDS was 
support (CDS) systems were some of the earliest applications rekindled. The 2023 HIMSS conference showcased the prolif
of computers in healthcare.1,2 The integration of computing eration of AI in healthcare systems, an exhibition unparal
technology into medical practice in the 1960s and 1970s leled in previous years.
facilitated the advent of computer-assisted decision-making However, the historical challenges of algorithm develop
in areas ranging from antibiotic selection to the management ment, validation, and deployment, including the representa
of acid-base imbalances.3 The subsequent decline in memory tiveness of the training data, have been amplified in the 
costs and the doubling every 2 years of computational current landscape. Today, despite privacy concerns, the crea
capacity led to the expansion of hospital-wide CDS systems tion and utilization of extensive datasets for training AI-CDS 
through the 1980s and 1990s. This period was characterized systems are commonplace. Similar to their predecessors, these 
by the emergence of more sophisticated expert systems, such systems may harbor latent biases that are extremely difficult 
as the Quick Medical Reference,4 DXPlain,5 and ILIAD,6

to account for. The ease of acquiring vast training datasets in 
the modern era exacerbates the challenges previously encoun

designed to augment clinical diagnosis. Efforts like Rind's tered, necessitating heightened scrutiny of AI-CDS systems' 
renal failure studies sought to institute real-time clinical training data and deployment mechanisms. Additionally, 
alerts.7 Refining algorithms and integrating detailed patient there is even less transparency in how decisions, advice, and 
data, including prior serum creatinine levels, age, and concur recommendations are made. Because there is often no way to 
rent medications, improve CDS recommendations' precision decipher the pathway to a given recommendation, the sys
and contextual relevance. tems that produce them are often called “black boxes.”

Early CDS could provide advice on making a diagnosis or While established methodologies, such as randomized con
picking a therapy. They accomplished this through algo trolled trials (RCTs), have been used to evaluate the effective
rithms, which could be comprehended using logistic regres ness and safety of traditional CDS systems,10 these 
sion, recursive partitioning, and other mathematical and approaches may not be sufficient for AI-enabled CDS (AI- 
computational methods. Yet the underlying data used to train CDS). The dynamic nature of AI algorithms, which can 
these systems was rarely exposed for review. It was difficult, evolve and adapt over time through continuous learning and 
if not impossible, to tell if a system was trained on a dataset model updates, introduces the challenge of model drift. As a 
with intrinsic bias. However, the ability to cause harm by result, new evaluation approaches are needed to assess the 
mistake in use or output due to bias was largely constrained performance, safety, and robustness of AI-CDS systems 
by the limited availability of these systems to a relatively throughout their lifecycle, accounting for potential changes 
small set of individuals who knew how to use them and the in model behavior.
patients they treated. Generative AI technologies and extensive language models 

By the early 1990s, it was recognized that further transpar (LLMs) like ChatGPT represent a significant advancement 
ency was needed. Miller and Gardner8 provided an extremely over traditional machine learning approaches. Traditional 
comprehensive review of the domain that outlined the vari machine learning models typically rely on structured datasets 
ous levels of complexity and risk associated with decision and are designed to perform specific tasks, such as classifica
support systems of the day. They provided a comprehensive tion or regression, based on predefined features. These models 
approach to document a variety of parameters of complexity, require labeled data and often involve feature engineering to 
which, in turn, reflected the degree of review and oversight optimize performance. The critical differences between LLMs 
that would be needed to ensure the safe deployment and use and traditional machine learning approaches include LLMs 
of such systems. The evolution of systems and the democra are trained on extensive, diverse datasets from various sources, 
tization of data led to the growth of CDS deployment. while traditional models use smaller, domain-specific datasets. 

By 2017, Labkoff and Sittig identified challenges to main LLMs utilize unsupervised learning to understand language 
taining the safety and quality of data used in CDS in clinical patterns and generate text, whereas traditional models rely on 
care.9 They argued that there should be ongoing oversight supervised learning with labeled data. LLMs can generate new 
and a way for patients who have suffered harm due to the use text based on input prompts, making them versatile, while tra
of CDS to report these issues to a clearinghouse at the federal ditional models are designed for specific predictive tasks. 
level. With the dramatic growth in the capabilities and diver LLMs use large, undisclosed datasets, complicating bias 
sity of AI-CDS, the need for such a reporting mechanism to assessment, whereas traditional models allow for more 
promote the safety, transparency, and trust of these systems straightforward bias evaluation and mitigation.
is now even more urgent. Regulatory and professional bodies, such as the Food and 

Today, we are witnessing an ongoing expansion in Drug Administration (FDA),11 American Medical Association 
machine learning and artificial intelligence (AI) capabilities. (AMA),12 World Health Organization (WHO),13 European 

Downloaded from https://academic.oup.com/jamia/article/31/11/2730/7776823 by guest on 28 October 2024



2732                                                                                        J o u r n al of the American Medical Informatics Association, 2024, Vol. 31, No. 11 

Commission in collaboration with the European Medicines developed rapid brainstorming methods and group discus
Agency (EMA),14 and AMIA,15 have established initial frame sions to develop the core ideas and challenges. Over the next 
works to evaluate and monitor AI systems for “fitness for 4 months, a sub-group of the team (the authors) met in 
purpose,” efficacy, safety, and fairness. The term “fitness for weekly online discussion meetings to develop consensus rec
purpose” refers to the ability of an AI system to effectively and ommendations presented in this paper. The group used a Del
efficiently fulfill the specific task or purpose for which it was phi approach to iterate on the core challenges and the 
designed. This includes the system’s accuracy and speed and its consensus approaches for how they should be prioritized and 
adherence to ethical standards such as fairness, transparency, addressed. This paper summarizes the findings and recom
and respect for privacy. Prior literature16 examined algorithm mendations of this process and the implications for the 
auditing methodologies and protocols for tailoring traditional healthcare field.
clinical evaluation approaches to AI. However, difficulties per
sist in comprehensively assessing AI-CDS tools outside limited 
research contexts.17,18 Moreover, healthcare stakeholders Results
urgently need coordinated action to implement layered AI gov Governance of these interconnected issues requires multi- 
ernance solutions to address issues across the entire AI-CDS pronged initiatives around transparency, training, and infra
lifecycle,19 including relevant ethical and social issues, not least structure from developers, regulators, and healthcare delivery 
privacy, transparency, accountability, and equity. organizations. The key findings are shown in Table 1 and can 

Recent publications have emphasized the importance of be grouped into 4 primary domains: (1) To build safe and 
addressing algorithmic bias,20,21 fairness22 issues, and the trustworthy systems by creating a systematic approach to a 
need for explainable AI and interpretability23 in healthcare “nutrition label”; (2) Validation and verification (ie, certifica
applications. Moreover, researchers have focused on develop tion of AI-CDS systems)—create a systematic approach to 
ing and applying evaluation and validation methodologies to testing and validation; (3) Safety monitoring and reporting— 
assess the performance and safety of AI-enabled CDS the creation of an AI-CDS reporting center for adverse events; 
systems. Studies have also explored the organizational, tech and (4) Documentation and end-user training—provide com
nical, and human factors24 that influence the adoption of AI- prehensive and certified training for professional and lay 
enabled CDS. There is a need to achieve consensus for the users of AI-CDS.
evaluation of AI for CDS. This paper will provide the find
ings and recommendations of a detailed consensus process 
with a broad range of stakeholders to ensure that AI-CDS is Recommendations
safer, more effective, and more equitable in a way that repre Building safe and trustworthy systems
sents the multiple viewpoints of the key stakeholder groups. Each domain in Table 1 can be reflected in the various stages 

of the AI-CDS development lifecycle. Figure 1 presents a vir
tuous cycle, leveraging design thinking concepts in software 

Materials and methods development to visualize the stated challenges.28 Several 
During the summer of 2023, in partnership with the Ameri frameworks have been proposed for AI.29,30 This illustration 
can Medical Informatics Association (AMIA), the DCI Net outlines a typical development and deployment lifecycle. By 
work,25 a consortium created by the Division of Clinical using trusted standards for system development, we can 
Informatics (DCI) at Beth Israel Deaconess Medical Center ensure that best practices are adhered to, that systems can 
(BIDMC), convened and created a working group focused on support interoperability, and facilitate workflow integration.
AI in healthcare. We prepared 4 antecedent webinars on “AI 
in Healthcare” that covered topics including (a) Bioethics and Integration into existing systems: the role of international 
Religion, (b) Patient perspectives, (c) Real-world Data and consensus standards
the Regulatory Perspective, and (d) Risk management, Trust, One way to drive trust in AI-CDS in clinical care is to provide 
and Liability.26 a framework and standards to promote transparency and 

A month later, we convened a cross-functional, interdisci interoperability. To facilitate the consistent adoption of such 
plinary team involving over 200 experts from government, tools, healthcare standards development organizations (ie, 
standards organizations, private industry, ethicists, patients HL7, IEEE, EN TC 251 - Technical Committee on Health 
and advocates, religious leaders, clinical informaticians, and Informatics Europe, and International Organization for 
regulators, gathered through 4 webinars and a 2-day live con Standardization [ISO] Technical Committee 215) should 
sortium at the Harvard Medical School in September 2023.27 strive to define specifications around required fields, formats, 
Over these 2 days, the group heard from multiple speakers and APIs for data and metadata access and use. The unique 
and, later, broke out into working groups. We focused on 3 AI Identifier (UAII) label (see below) could be adapted as a 
specific domains of how AI is being deployed in the health new class within the HL7 FHIR standard, enabling seamless 
care ecosystem: (1) a patient’s viewpoint on how they are integration with other clinical and research data. Other col
using AI in their healthcare journeys; (2) how AI is impacting laborative efforts tapping into diverse expertise have success
CDS; and (3) how AI is being used to create, enrich, and use fully propagated terminology system standards like 
real-world data/evidence. The participants were tasked with SNOMED CT through SNOMED across care settings.31,32

identifying challenges, proposing strategies, and creating key However, establishing standards alone is insufficient to 
goals to ensure that AI-CDS can be built, used, and evaluated gain the necessary trust in AI-CDS, especially as these systems 
safely, efficiently, and equitably in the context of both the may eventually undertake tasks such as prescribing medica
work that has been done in the field, as well as how to tions without human oversight. Although this scenario is not 
address current-day and future challenges presented by the yet a reality, it represents a conceivable future direction for 
democratization of AI-CDS systems. The sub-groups AI-CDS. Incorporating these unattended AI-CDS 

Downloaded from https://academic.oup.com/jamia/article/31/11/2730/7776823 by guest on 28 October 2024



Journal of the American Medical Informatics Association, 2024, Vol. 31, No. 11                                                                                        2  7  3  3    

Table 1. Key challenges identified by the consensus group (listed in alphabetical order).

Core concept Challenge

Adverse events Lack of real-time monitoring and reporting to enable aggregation, analysis, and alerts around 
potential safety issues.

Bias AI algorithms and subsequent recommendations may reflect both dataset and development biases 
due to the following:

1) Differential representation of race, gender, socioeconomics, clinical subpopulations, and 
health disparities in datasets. 

2) Inaccurate design assumptions due to experiential or other biases by designers, developers, 
or users. 

3) Failure to consider the values and preferences of the patient. 
4) Differential coding of data due to different local conventions or interpretations of coding 

standards leads to inaccurate or inappropriate data aggregation and analysis. 
Credibility and explainability Current AI systems provide limited explanations or citations for their reasoning.
Documentation and transparency Insufficient clarity regarding the provenance of biases in training data, model development, and 

real-world testing procedures may undermine the credibility and adoption of AI tools.
Generalizability and portability The specificity of the clinical context and the data used for training may limit generalizability. 

Application to new or evolving scenarios can lead to unpredictable results in other settings.
Inaccurate inferences Inadequately constrained AI models may provide false or unsupported recommendations. Inad

equately constrained AI models refer to those AI systems that lack sufficient limitations or rules in 
their design and operation. These models may not have the necessary restrictions to guide their 
learning process effectively. This leads to overfitting, where the model learns the training data too 
well and performs poorly on new, unseen data.

Integration Interoperability challenges may hamper AI integration with data sources and clinician workflows; 
they can affect the ability to get data in and make recommendations actionable.

User competency “Users” primarily refers to clinicians interacting with the AI-enabled Clinical Decision Support 
(AI-CDS) systems. Ensuring clinicians have the necessary competencies to use these systems effec
tively is crucial for patient safety and the system's overall efficacy. Inadequate training or demon
strated competency in assessing recommendations and deploying AI-CDS risks patient harm and 
distrust.

Validation and certification Frequent model retraining on new data, which is required to prevent model “drift,” creates mov
ing targets for validation, benchmarking, and auditing. 
The existing regulatory apparatus is not equipped for the technical and governance challenges of 
near real-time review, re-evaluation, and certification. 

Veracity of results Variability in recommendations or detection of AI errors from an AI-CDS will erode confidence in 
the system. Establish clear criteria for veracity based on rigorous testing, validation, and continu
ous performance monitoring.

interventions within existing EHRs without sufficient testing (eg, sex, gender, ethnicity, disability, or sexual orientation).35

and trust will open new, complex trust challenges. Moreover, such disparities often originate in historical and 
systemic care delivery contexts, clinical research, and evi

Clinical integration and decision partnerships dence generation.
For sustainable, safe, and effective adoption of AI-CDS in As such, in developing and adopting AI-CDS in healthcare, 
healthcare settings, it must be part of the clinical workflow it is essential to contextualize it as a facilitator as well as a 
and integrated seamlessly into HIT, such as EHRs, clinical potential barrier to equitable healthcare delivery.36–38 To 
information systems, personal health records, and patient avoid creating and perpetuating new dimensions of dispar
portals. AI-CDS should also help diminish documentation ities, individual researchers, agencies, professional bodies, 
challenges prevalent in EHR systems today.33,34

and the government have proposed various frameworks for 
Such systems should be designed to provide user-friendly ensuring health equity is considered in all innovations, 

summaries for both clinicians and patients and support docu including those driven by AI/ML.39,40

mentation encompassing: An article by the Research Triangle Institute summarizes the 
8 primary health equity frameworks and measures that inform 

� The goal and specific questions asked of the AI. how health equity performs across the Institute for Health 
� The AI-generated response. Improvement (IHI), the Robert Wood Johnson Foundation 
� Whether or not a clinician reviewed and agreed with the (RWJF), the Centers for Medicare and Medicaid Services 

recommendation. (CMS), the National Committee for Quality Assurance 
� The date and time when the system was used. (NCQA), and the Joint Commission International (JCI). Con
� Any references needed to clarify how and when the system cepts such as ‘Inclusion by design’41 and ‘algorithm vigilance’,42

was used. among others, enhance fairness in system development, deploy
ment, and evaluation. As part of the concept of Inclusion by 

Equity Design, the Global Future Council on Artificial Intelligence for 
The WHO defines equity as the absence of unfair, avoidable, Humanity designed an Inclusive AI Lifecycle.34 This provides a 
or remediable differences among groups of people, whether systems view of embedding the goal of equity in all steps of the 
those groups are defined socially, economically, demographi AI development lifecycle and mapping both the builder and 
cally, or geographically, or by other dimensions of inequality stakeholder/governance ecosystem.

Downloaded from https://academic.oup.com/jamia/article/31/11/2730/7776823 by guest on 28 October 2024



2734                                                                                        J o u r n al of the American Medical Informatics Association, 2024, Vol. 31, No. 11 

Figure 1. Human-centered AI development cycle. 

Themes across these equity frameworks include the representative diverse views on ethical principles, 
following: enhancing the accuracy of model development and 

mitigating the risks of introducing implicit bias into 
� Governance and organizational support such systems. 

There are business, moral, and health imperatives for � Audit and evaluation of health outcomes 
making equity a strategic and foundational goal of all It is crucial to monitor and assess models, recommenda
projects or programs in healthcare, which requires strong tions, and outcomes considering various forms of identity 
organizational support and governance.43 and social factors, such as race, socioeconomic status, 
� Data management health literacy, insurance coverage, etc. These factors 

AI-CDS systems depend on the datasets used to train the should improve over time as the technology is developed 
algorithms and make recommendations. Furthermore, sev and used (Figure 1). 
eral data characteristics should be assessed and docu
mented to guide model developers and users, including We recommend incorporating best practices and principles 
provenance, representation, context, and assumptions.44 from health equity frameworks45 and research through the 
� Development and Implementation Team Requirements entire AI-CDS (Figure 1) system lifecycle to reduce disparities 

� Assessment of disparities and social determinants of and promote equitable care.46

health: One must understand how sociodemographic 
determinants of health may affect outcomes and Verification, validation, and certification
implement appropriate detection and mitigation “Verification” refers to ensuring the accuracy, reliability, and 
strategies. safety of AI algorithms designed for medical applications, 

� Inclusive stakeholder/community engagement: Must including rigorous testing and assessment of the AI’s per
be multidisciplinary (ie, clinical, technical, operational, formance against predefined benchmarks. Data validation 
and end-users). All stakeholders should be involved in assesses the quality and completeness of the data used to train 
problem definition, validation, and deployment plan and test the AI model; algorithmic validation assesses the 
ning throughout the AI development cycle (Figure 1). model’s ability to produce consistent and accurate results; 

� Diverse workforce: The workforce should be diverse and clinical validation evaluates the efficacy and reliability of 
across multiple dimensions of identity, ideally repre the results in a clinical context.
senting the population on which the model is intended Certification refers to having the AI-CDS’ output (recom
to be deployed as clinicians or patient end-users. mendations) evaluated against some agreed-upon standard 
Diversification in teams could provide varied perspec from either a standards development organization or regula
tives on population samples that are considered tory body. Certification helps to ensure that the system meets 

Downloaded from https://academic.oup.com/jamia/article/31/11/2730/7776823 by guest on 28 October 2024



Journal of the American Medical Informatics Association, 2024, Vol. 31, No. 11                                                                                        2  7  3  5    

Table 2. Verification, validation, and certification issues for verification of AI-CDS.

Model training � Documentation of data origins and characteristics is critical to the credibility of advice or direction provided 
by these systems 

� Identification and documentation of known biases in the training datasets: 
� Type of data (eg, EHR data, claims data) 
� Its origin, where it was collected (facility, geography), and the nature of the population from which it 

was gathered (demographics) 
� Any known intrinsic biases in the training data (eg, limited population demographics) 

� Identification of training methods (eg, deep learning, supervised learning, unsupervised learning, etc) 
Explainability47 � How have the decisions and recommendations been reached? 
Use-case dependency � Virtually all AI-CDS systems are optimized for a particular use case and population. Results may be unpre

dictable if applied to different use cases or populations. 
Veracity of results � Variability in recommendations or detection of AI errors from an AI-CDS will erode confidence in the 

system. 
End-user training � The ability to interpret results will depend on the operator’s knowledge, experience, and training. Proper 

training should be clearly defined and repeated annually or in response to system updates and changes. 

some known standard of accuracy, which helps foster trust.  record. Adequate funding should be provided so the agency 
Table 2 identifies additional verification, validation, and cer can monitor and report the reported information.
tification issues that must be addressed to verify that AI-CDS 
provides trusted results. User competence (training)

End-users require training as with any new medical guideline, 
AI-CDS documentation device, procedure, or medical therapy. As AI-CDS becomes 
One of the first recommendations from our working group mainstream, system- and tool-specific training of end users is 
was creating a transparency label for AI-CDS systems called critical for overall safe use, regardless of whether or not it 
the Unique AI Identifier (UAII). Its purpose is to address trust resides inside otherwise familiar EHR systems.
and enhance transparency by disclosing relevant aspects of Health professions educators should define new competen
such systems. The UAII is similar to a nutrition, implantable cies for using AI-CDS in clinical practice, and these training 
device, or medical product label. It provides vital metadata requirements should be incorporated into medical education 
needed to use AI-CDS systems safely, responsibly, and with programs at all levels and evolve with the technology.54 We 
accountability. It also provides a complimentary means of propose that, as part of the UAII process, developers, manu
maintaining a certification cycle for a given system under facturers, and content authors specify appropriate training 
review. requirements for users. This should include competencies 

We recommend a set expiration of certification when a such as the context of the model, assumptions made, and the 
UAII must be reviewed, along with any data about the sys model’s limitations. The actual training should be up to 
tem’s use, performance, adverse events, or other outcomes. experts in adult education to provide such training and 

Sendak et al48 suggested one example of such a label in certification.
2020. This was modeled after the medical label. In addition Our working group recommends creating a similar set of 
to Sendak’s recommendations, our consensus working group constructs and a parallel system for training requirements, 
had additional fields to be considered for the UAII, as found which should be mandatory (depending on the application’s 

in Table 3. envisioned end users—for clinicians or laypeople) and docu
mented and monitored as part of overall risk mitigation and 

Monitoring and reporting legal/compliance constructs.
To ensure safe use of AI-CDS, there is a need for the creation 
of a National Healthcare AI-CDS Safety Reporting Clearing Discussion
house. The FDA maintains the MedWatch system as a clear AI-CDS promises to transform healthcare decision-making, 
inghouse for adverse event reporting for biologics, necessitating investments in transparency, monitoring, and 
prescription and over-the-counter drugs, combination prod oversight. This consensus analysis establishes a framework 
ucts, medical devices, special nutrition products, cosmetics, emphasizing trustworthy systems, verification, validation, 
and food.50 This system enables medical professionals and certification, monitoring, reporting, documentation, and 
others to report adverse events promptly and comprehen training. Key concepts include Unique AI Identifier labels 
sively. The system also provides real-time safety information (UAII), model training, explainable AI, result veracity, and 
alerts via a subscription email list. The FDA is also involved adverse event reporting.
with AI in post-market surveillance of Software as a Medical In recognizing that some failures of CDS systems are 
Device (SaMD).51 However, some important questions inevitable, it is essential to design them to be as fail-safe as 
remain.52 The FDA also maintains the MAUDE53 for track possible. This involves comprehensive testing and validation, 
ing issues, specifically with medical devices. Having some user-centered design, and a layered decision-making process 
thing similar for AI-CDS event reporting would be the next to ensure reliability and safety. Predictable errors such as 
logical step. data entry inaccuracies, algorithm bias, clinical context mis

An AI-CDS clearinghouse must facilitate and standardize matches, and model drift can be mitigated through strategies 
reporting of unexpected or adverse events that stem from such as automated data entry, continuous bias assessment, 
using AI-enabled CDS and must become part of the public incorporating contextual data, and regular model updates. 

Downloaded from https://academic.oup.com/jamia/article/31/11/2730/7776823 by guest on 28 October 2024



2736                                                                                        J o u r n al of the American Medical Informatics Association, 2024, Vol. 31, No. 11 

Table 3. Key fields to be included in the UAII, in descending order of importance to the clinician.

Optimal use case Descriptions of circumstances and situations where the model can be best used.

Information about training  A comprehensive review of the data used to train the system, encompassing information on how and 
data and potential biases where it was obtained, population, location, care setting (if appropriate), and date range. Any known 

imbalances or biases are to be listed. Measures taken to clean the data: how missingness was 
addressed, how representativeness was evaluated, how the data were de-biased or the effects of bias 
controlled for, and how new data types were incorporated.

Duration of certification Systems should be certified for use for a finite time to ensure they continue providing valid, accurate, 
and safe recommendations. All systems should be revalidated after system or training data updates. 
Adaptive AI systems and those that self-modify must be reviewed and calibrated regularly to correct 
any drift.

Version information Clear identification of the current version number or other means of version identification must be 
provided and refreshed during updates. Version disclosure should not be limited to the software but 
to the data and the training data.

Conflict of interest disclosures Standard processes for conflict-of-interest disclosures should apply to all system developers.
Limitations and warnings The UAII should enumerate any known limitations and warnings regarding domains of use, use 

cases, and any other information that could influence overall use or interpretations.
Algorithms employed Disclosures about the types and sources of algorithms employed by the AI-CDS.
Validation and certification The UAII should show evidence of how the system was tested and how the results of those tests were 

validated, including unexpected outcomes.
Recommended training Any prerequisites needed to certify the user should be disclosed in the UAII. 

For instance, if a licensed cardiologist should be the only person using an AI-CDS system, UAII 
should make this clear. Conversely, if it can be used by untrained end-users (ie, patients, laypersons), 
that too should be clearly described.49

By implementing these guidelines, we can enhance the inte (SaMD) and has considered regulating AI-CDS output since 
gration of CDS into clinical care, thereby improving patient 2019 and has already developed a framework for using 
safety and the overall efficacy of clinical decision-making. SaMD as CDS56 but challenges persist regarding AI decision- 

These new systems can be modified in many ways, ranging making explainability.57

from updates to training algorithms to updating their training AI systems currently do not consistently provide a plausible 
datasets. A system to test the continued validity and credibil explanation as to how or why recommendations are given 
ity of recommendations after these changes is essential. Even (ie, “black box” system). As demonstrated with Meaningful 
small changes in these systems can potentially affect how Use, Stage 2 in 2012,58 there is a need to provide the rationale 
they arrive at recommendations. The current regulatory tools to its recommendations.59 While voluntary UAII creation 
at our disposal are not sufficiently agile to meet these might lead to uneven adoption, mandating UAII publication 
challenges. could promote widespread use. However, a balance is needed 

Evaluation of AI-CDS efficacy and safety traditionally between standardization and avoiding innovation-stifling 
relies on randomized controlled trials (RCTs), cohort, and mandates.
case-control studies. However, the dynamic nature of non- The slow process of the development of national laws and 
deterministic algorithms requires new approaches. Unique to policies requires more pragmatic approaches that could be 
AI-CDS, there must also be capped autonomy levels (eg, at implemented sooner. Industry self-regulation through Stand
what point, if ever, does the software become autonomous, ards Development Organizations such as HL7, IEEE, and 
not requiring human intervention and confirmation). ISO60 could drive consistent adoption of transparency tools 

Phased-in changes to medical education curricula and com such as UAII. Standardizing specifications for data fields, for
petency testing for AI use in clinical environments will be mats, and APIs could enable seamless integration with clini
needed. Patients' understanding and reaction to these systems cal and research data. While collaborative efforts have 
also require careful consideration. Operationalizing these rec successfully propagated standards like SNOMED CT, chal
ommendations involves overcoming socio-technical barriers lenges remain, as seen with varying implementations of HL7 
to explainability and encouraging transparent developer 2.x by different vendors.61,62

behaviors while avoiding overly restrictive policies. AI-CDS tools introduce new challenges in medical infor
AI systems' modifiability necessitates continuous validity matics, particularly in ensuring trust.63 While UAII labels are 

testing. Current regulatory tools may lack the agility to helpful, trust requires rigorous validation and verification. 
address these challenges effectively. Documenting intrinsic Standard methods may not account for issues like model drift 
biases in AI models is crucial for informed utilization. Under post-launch. A multi-layered approach should combine inter
lying disparities existing today in the real world have the nal testing under varied use cases and ongoing monitoring 
potential to be promulgated in AI training models.55 Correct (eg, using the UAII above label to complement adverse event 
ing embedded, intrinsic bias in existing real-world data may reporting).52 Conversely, there is a risk of over-reliance on 
be impossible. However, documenting such issues (in the AI-CDS recommendations, as observed in some studies.64

UAII) is essential to informing appropriate utilization—or Legal and liability challenges are currently being debated, 
when not to use such models.37 especially with respect to autonomous AI CDS.65 CDS was 

Public policy support is crucial for the proposed frame faced with similar questions and addressed them best by 
work's consistent implementation. This may involve execu clearly stating that there was a human in the loop.66 What 
tive orders, federal regulations, or legislation. The FDA has happens if clinicians trust AI too much and are asked to jus
developed a framework for Software as Medical Device tify decisions based on logic they don’t understand? What 

Downloaded from https://academic.oup.com/jamia/article/31/11/2730/7776823 by guest on 28 October 2024



Journal of the American Medical Informatics Association, 2024, Vol. 31, No. 11                                                                                        2  7  3  7    

happens if no human is in the loop, such as with autonomous approval submission with all validation data and risk assess
AI? Much of this remains to be examined, let alone decided. ments, and post-market surveillance for monitoring real- 

The clich�e “data is the new oil” highlights data’s impor world performance and identifying adverse events through 
tance in powering AI, akin to oil’s role in traditional indus continuous monitoring and reporting mechanisms.
tries. However, it also underscores the privacy risks In summary, AI tools are poised to transform medicine by 
associated with data used in AI systems. As these systems integrating into CDS. As AI technologies proliferate, their full 
evolve, the need for robust data privacy measures intensifies. integration into clinical workflow and healthcare delivery is 
Thus, the phrase serves as a reminder of data’s dual role in inevitable. Urgent standardization of frameworks, implemen
AI: a valuable innovation driver and a potential privacy risk. tation of guiding principles, and establishment of best practi
New legislation like the European AI Act67 and the USA’s ces are needed to safeguard medical practice and patient 
Whitehouse Blueprint,68 for an AI Bill of Rights may help to outcomes. Given the prevalence of preventable adverse events 
improve privacy and safety. However, frameworks like the in hospital admissions,66 we are optimistic that AI-CDS can 
one proposed in this paper are needed to guide the develop lead to better outcomes we are optimistic that AI-CDS can 
ment and evaluation of AI-CDS systems so they comply with significantly improve healthcare outcomes.
the various emerging regulations.

Fairness in algorithmic CDS systems is complex, with vari
ous metrics often leading to conflicting results. The choice of 
fairness metric should align with the specific clinical purpose. Conclusion
For example, equalized odds may be prioritized in diagnos The speed and breadth by which AI can impact CDS have 
tics, while predictive parity might be essential for treatment become more significant due to data availability, computing 
recommendations. To navigate these complexities, we recom power, and new LLMs; however, the risks have never been 
mend context-specific evaluation, stakeholder engagement, higher for unvalidated systems. In this paper, we provided 
hybrid approaches balancing multiple metrics, and maintain specific and pragmatic approaches to improve how we evalu
ing transparency and flexibility. These principles can ensure ate AI-CDS to improve safety, efficacy, and equity. This proc
fairness in CDS systems is tailored to clinical applications, ess for reaching a consensus among many stakeholders laid 
enhancing equity and efficacy in patient care. out practical building blocks and infrastructure oversight to 

Data privacy and the balance between data dissemination help the responsible use of AI in clinical decision-making set
and model quality are crucial in AI-enabled CDS systems. tings. By embracing collaborative governance through princi
While disseminating healthcare data can enhance AI model ples including (1) building trustworthy and safe systems; (2) 
performance, it raises patient privacy and data security con verification, validation, and certification; (3) monitoring and 
cerns. Federated learning offers a potential solution by train reporting; and (4) user competence, healthcare systems can 
ing AI models on decentralized data. However, implementing benefit from improved efficiency, accuracy, and consistency 
federated learning in healthcare presents challenges, including while mitigating risks from rapidly evolving algorithms.
standardized data format requirements, potential model bias, 
and computational resource needs. Researchers, healthcare 
institutions, and policymakers must carefully balance data Acknowledgments
privacy and AI model quality, constructing robust frame
works for responsible data sharing and federated learning We thank Dr David Bray, Dr Tiffani J. Bright, and Dr Isaac 
application in healthcare. Kohane for their keynote talks at the conference. We thank 

Records scattered across multiple EHR systems and in vari Dr Bray for his initial input in early discussions on the fram
ous formats complicate AI-CDS integration. Proposed solu ing of this paper. We would also like to thank Rabbi Daniel 
tions include adopting healthcare data standards like HL7 Cohen and Reverend Greg Doll for their webinar on Bio
FHIR; developing advanced data integration strategies; inves ethics and AI, Dr Luke Sato, Dr Paul R. DeMuro, and Ken
ting in data mapping to convert unstructured data; imple neth E. White, JD, for their webinar on AI in Healthcare: 
menting pilot programs; and fostering collaboration among Risk Management, Trust, and Liability, Dr Amy Price and 
stakeholders to create a supportive ecosystem for AI-CDS Dave deBronkart (ePatient Dave) for their webinar on AI in 
integration. Healthcare: The Patient Perspective, and Dr Anne-Marie 

Re-certification and evaluation of AI systems for CDS are Meyer, Mark Shapiro, and Rob Stolper for their webinar: AI 
crucial for ongoing efficacy and safety. AI models may expe In Healthcare: Real World Data Generation and The Regula
rience “drift” over time due to changes in data distribution, tory Perspective. Lastly, we thank Dr Charles Safran for his 
training data updates, self-modifications, or patient popula input on the paper's later versions and his guidance at the 
tion shifts. Regular review, calibration, and revalidation are DCI Network.
necessary to correct drift and maintain accuracy. Certifying 
systems for finite periods ensures periodic reassessment, safe
guarding against outdated or erroneous recommendations. Author contributions
These processes are integral to AI's responsible deployment 
and maintenance in healthcare. Yuri Quintana and Steve Labkoff (Conceptualization), Yuri 

AI-enabled CDS systems require a rigorous approval proc Quintana and Steve Labkoff (Methodology), Yuri Quintana, 
ess overseen by regulatory bodies like the FDA before effec Steve Labkoff, Joseph Kannry, Eileen Koski, Bilikis Oladi
tive monitoring and adverse event reporting can be meji, Anthony Solomonides, and Gyana Srivastava (Writ
implemented. This process includes early FDA dialogue, com ing—Original draft), All authors (Writing—Review & 
prehensive clinical validation studies with RCTs, in-depth editing), Yuri Quintana and Steve Labkoff (Supervision), and 
risk assessment and mitigation strategy development, detailed Gyana Srivastava (Project administration)

Downloaded from https://academic.oup.com/jamia/article/31/11/2730/7776823 by guest on 28 October 2024



2738                                                                                        J o u r n al of the American Medical Informatics Association, 2024, Vol. 31, No. 11 

Funding gov/medical-devices/software-medical-device-samd/artificial-intel
ligence-and-machine-learning-software-medical-device

None declared. 12. Advancing health care AI through ethics, evidence and equity. (n. 
d.). Accessed January 18, 2024. https://www.ama-assn.org/prac

Conflicts of interest tice-management/digital/advancing-health-care-ai-through-ethics- 
evidence-and-equity

S.L. is an employee of Quantori, LLC. B.O. is an employee of 13. WHO outlines considerations for regulation of artificial intelli
UnitedHealth Group. R.L. is a full-time employee of InterSys gence for health. (n.d.). Accessed January 8, 2024. https://www. 
tems Corporation. E.K. owns stock in IBM. L.A.F. is a Princi who.int/news/item/19-10-2023-who-outlines-considerations-for- 
pal at Rubrum Advising, which advises companies on regulation-of-artificial-intelligence-for-health
coverage of new technologies, including AI. K.N. is an 14. Regulatory framework proposal on artificial intelligence. (n.d.). 
employee and shareholder of Pfizer Inc. T.N. is an employee Accessed January 4, 2024. https://digital-strategy.ec.europa.eu/en/ 
of Microsoft Corporation. D.F.S. is an owner of Informatics policies/regulatory-framework-ai

Review LLC. G.P.J. is an employee of Intuitive Surgical. G.P. 15. Solomonides AE, Koski E, Atabaki SM, et al. Defining AMIA’s 
artificial intelligence principles. J Am Med Inform Assoc. 2022;29 

J. owns stock and/or stock options for IBM, Kyndryl, and (4):585-591. https://doi.org/10.1093/jamia/ocac006
Intuitive Surgical. G.P.J. was the Past President and Past 16. Park SH, Han K, Jang HY, et al. Methods for clinical evaluation of 
Board Chair of the American Medical Informatics Associa artificial intelligence algorithms for medical diagnosis. Radiology. 
tion. The authors had no other conflicts or competing inter 2023;306(1):20-31. https://doi.org/10.1148/radiol.220182
ests to disclose. 17. Shah NH, Halamka JD, Saria S, et al. A nationwide network of 

health AI assurance laboratories. JAMA. 2024;331(3):245.
18. Stead WW, Aliferis C. Health AI assurance laboratories. JAMA. 

Data availability 2024;331(12):1061-1062. https://doi.org/10.1001/jama.2024. 
All data used in this article have been reported in this paper. 1084
There are no other data associated with this paper. 19. Sittig DF, Boxwala A, Wright A, et al. A lifecycle framework illus

trates eight stages necessary for realizing the benefits of patient- 
centered clinical decision support. J Am Med Inform Assoc. 

Disclaimer 2023;30(9):1583-1589. https://doi.org/10.1093/jamia/ocad122 
PMID: 37414544; PMCID: PMC10436138.

The contents of this manuscript represent the view of the 20. Ferryman K, Mackintosh M, Ghassemi M. Considering biased 
authors and do not necessarily reflect the position or policy data as informative artifacts in AI-assisted health care. N Engl J 
of the U.S. Department of Veterans Affairs or the United Med. 2023;389(9):833-838. https://doi.org/10.1056/NEJMra 
States Government. 2214964

21. Alvarez JM, Colmenarejo AB, Elobaid A, et al. Policy advice and 
best practices on bias and fairness in AI. Ethics Inf Technol. 

References 2024;26(2):31. https://doi.org/10.1007/s10676-024-09746-w
01. Collen MF. Computer medicine: its application today and tomor 22. Liu S, McCoy AB, Peterson JF, et al. Leveraging explainable artifi

row. Minn Med. 1966;49(11):1705-1707. cial intelligence to optimize clinical decision support. J Am Med 
02. Middleton B, Sittig DF, Wright A. Clinical decision support: a 25 Inform Assoc. 2024;31(4):968-974.

year retrospective and a 25 year vision. Yearb Med Inform. 23. Vasey B, Nagendran M, Campbell B, DECIDE-AI expert group, et 
2016;25(Suppl 1):S103-S116. https://doi.org/10.15265/IYS-2016- al. Reporting guideline for the early-stage clinical evaluation of 
s034 decision support systems driven by artificial intelligence: DECIDE- 

03. Bleich HL. Computer-based consultation: electrolyte and acid- AI. Nat Med. 2022;28(5):924-933. https://doi.org/10.1038/ 
base disorders. Am J Med. 1972;53(3):285-291. s41591-022-01772-9. Erratum in: Nat Med. 2022;28(10):2218.

04. Parker RC, Miller RA. Creation of realistic appearing simulated 24. Wang L, Zhang Z, Wang D, et al. Human-centered design and 
patient cases using the INTERNIST-1/QMR knowledge base and evaluation of AI-empowered clinical decision support systems: a 
interrelationship properties of manifestations. Methods Inf Med. systematic review. Front Comput Sci. 2023;5:1187299.
1989;28(4):346-351. 25. DCI Network. Boston, MA: Beth Israel Deaconess Medical Cen

05. Barnett GO, Cimino JJ, Hupp JA, et al. DXPlain: an evolving diag ter. Accessed September 20, 2024. https://www.dcinetwork.org
nostic decision-support system. JAMA. 1987;258(1):67-74. 26. AI in healthcare: risk management, trust, and liability. Accessed 

06. Lincoln MJ, Turner CW, Haug PJ, et al. ILIAD training enhances December 28, 2023. https://www.dcinetwork.org/events/190.
medical students’ diagnostic skills. J Med Syst. 1991;15(1):93-110. 27. Blueprints for trust: best practices and regulatory pathways for 

07. Rind DM, Safran C, Phillips RS, et al. Effect of computer-based ethical AI in healthcare. Accessed December 28, 2023. https:// 
alerts on the treatment and outcomes of hospitalized patients. www.dcinetwork.org/events/192?prev_path=/events
Arch Intern Med. 1994;154(13):1511-1517. 28. Software Engineering Models and Methods Course. (n.d.). 

08. Miller RA, Gardner RM. Recommendations for responsible moni Accessed January 16, 2024. https://www.computer.org/product/ 
toring and regulation of clinical software systems. J Am Med education/software-engineering-models-course
Inform Assoc. 1997;4(6):442-457. 29. AI guide for government: understanding and managing the AI life

09. Labkoff SE, Sittig DF. Who watches the watchers: working cycle. (n.d.). Accessed January 18, 2024. https://coe.gsa.gov/coe/ 
towards safety for EHR knowledge resources. Appl Clin ai-guide-for-government/understanding-managing-ai-lifecycle/ 
Inform. 2017;8(2):680-685. https://doi.org/10.4338/ACI-2017- #:�:text=The%20AI%20lifecycle%20is%20the,%2C%20devel
02-IE-0032 opment%2C%20and%20deployment%20phases

10. Bright TJ, Wong A, Dhurjati R, et al. Effect of clinical decision- 30. A proposed framework on integrating health equity and racial jus
support systems: a systematic review. Ann Intern Med. 2012;157 tice into the artificial intelligence development lifecycle. Accessed 
(1):29-43. https://doi.org/10.7326/0003-4819-157-1-201207030- January 4, 2024. https://muse.jhu.edu/article/789672/pdf
00450 31. Shortliffe EH, Cimino JJ, Chiang MF, eds. Biomedical Infor

11. Artificial intelligence and machine learning in software as a medi matics: Computer Applications in Health Care and Biomedicine. 
cal device. (n.d.). Accessed January 16, 2024. https://www.fda. 5th ed. Springer; 2021.

Downloaded from https://academic.oup.com/jamia/article/31/11/2730/7776823 by guest on 28 October 2024



Journal of the American Medical Informatics Association, 2024, Vol. 31, No. 11                                                                                        2  7  3  9    

32. Finnell JT, Dixon BE, eds. Clinical Informatics Study Guide: Text 50. MedWatch: the FDA safety information and adverse event report
and Review. 2nd ed. Springer; 2022. ing program. (n.d.). Accessed December 9, 2023. https://www.fda. 

33. Levy DR, Sloss EA, Chartash D, et al. Reflections on the documen gov/safety/medwatch-fda-safety-information-and-adverse-event- 
tation burden reduction AMIA Plenary Session through the lens of reporting-program#
25 × 5. Appl Clin Inform. 2023;14(1):11-15. https://doi.org/10. 51. Potnis KC, Ross JS, Aneja S, Gross CP, Richman IB. Artificial intel
1055/a-1976-2052 ligence in breast cancer screening: evaluation of FDA device regu

34. Brender TD. Medicine in the era of artificial intelligence: Hey lation and future recommendations. JAMA Intern Med. 2022;182 
Chatbot, write me an H&P. JAMA Intern Med. 2023;183(6):507. (12):1306-1312. https://doi.org/10.1001/jamainternmed.2022. 
https://doi.org/10.1001/jamainternmed.2023.1832 4969

35. Health equity. (n.d.). Accessed January 18, 2024. https://www. 52. Wu E, Wu K, Daneshjou R, Ouyang D, Ho DE, Zou J. How medi
who.int/health-topics/health-equity#tab=tab_1 cal AI devices are evaluated: limitations and recommendations 

36. Khan M, Bates D, Kovacheva V. (n.d.). The quest for equitable from an analysis of FDA approvals. Nat Med. 2021;27 
health care: the potential for artificial intelligence. Accessed Janu (4):582-584. https://doi.org/10.1038/s41591-021-01312-x
ary 10, 2024. https://catalyst.nejm.org/doi/full/10.1056/CAT.21. 53. MAUDE—manufacturer and user facility device experience. 
0293 Accessed January 31, 2024. https://www.accessdata.fda.gov/ 

37. Ledford H. Millions of black people affected by racial bias in scripts/cdrh/cfdocs/cfmaude/search.cfm
health-care algorithms. Nature. 2019;574(7780):608-609. https:// 54. Russell RG, Novak LL, Patel M, et al. Competencies for the use of 
doi.org/10.1038/d41586-019-03228-6 artificial intelligence-based tools by healthcare professionals. Acad 

38. Glauser W. AI in health care: improving outcomes or threatening Med. 2023;98(3):348-356. https://doi.org/10.1097/ACM. 
equity? CMAJ. 2020;192(1):E21-E22. https://doi.org/10.1503/ 0000000000004963. Selected as June 2023 Johns Hopkins Med 
cmaj.1095838 Ed Team ‘Must Read.’

39. Nordling L. A fairer way forward for AI in health care. Nature. 55. Parikh RB, Teeple S, Navathe AS. Addressing bias in artificial 
2019;573(7775):S103-S105. https://doi.org/10.1038/d41586- intelligence in health care. JAMA. 2019;322(24):2377-2378. 
019-02872-2 https://doi.org/10.1001/jama.2019.18058

40. Courtland R. Bias detectives: the researchers are striving to make 56. Artificial intelligence and machine learning in software as a medi
algorithms fair. Nature. 2018;558(7710):357-360. https://doi.org/ cal device. (n.d.). Accessed January 10, 2024. https://www.fda. 
10.1038/d41586-018-05469-3 gov/medical-devices/software-medical-device-samd/artificial-intel

41. A blueprint for equity and inclusion in artificial intelligence. (n.d.). ligence-and-machine-learning-software-medical-device
Accessed January 10, 2024. https://www.weforum.org/publica 57. Proposed regulatory framework for modifications to artificial 
tions/a-blueprint-for-equity-and-inclusion-in-artificial- intelligence/machine learning (AI/ML)-based software as a medical 
intelligence/ device (SaMD). (n.d.). Accessed December 28, 2023. https://www. 

42. Embi PJ. algorithm vigilance: advancing methods to analyze and fda.gov/media/122535/download
monitor artificial intelligence-driven health care for effectiveness 58. Medicare and Medicaid Programs: electronic health record incen
and equity. JAMA Netw Open. 2021;4(4):e214622. https://doi. tive program – stage 2. (n.d.). Accessed January 20, 2024. https:// 
org/10.1001/jamanetworkopen.2021.4622 www.federalregister.gov/documents/2012/09/04/2012-21050/ 

43. Donald M, Berwick MD. MPP: the moral determinants of health. medicare-and-medicaid-programs-electronic-health-record-incen
Accessed January 31, 2024. https://jamanetwork.com/journals/ tive-program-stage-2
jama/article-abstract/2767353 59. Greenes RA, Del Fiol G., eds. Clinical Decision Support and 

44. Datasheets for datasets. (n.d.). Accessed January 21, 2024. https:// Beyond: Progress and Opportunities in Knowledge-Enhanced 
cacm.acm.org/magazines/2021/12/256932-datasheets-for-data Health and Healthcare. 3rd ed. Academic Press; 2023.
sets/abstract 60. HL7 International. Accessed September 20, 2024. https://www. 

45. Health equity intervention and action principles. (n.d.). Accessed hl7.org
January 22, 2024. https://www.cdc.gov/healthequity/whatis/ 61. SNOMED. Accessed September 20, 2024. https://www.snomed. 
healthequityinaction/topics/he-intervention-action-principles.html org/

46. Dankwa-Mullan I, Scheufele E, Matheny ME, et al. A proposed 62. Finnell JT, Dixon BE, eds. Clinical Informatics Study Guide: Text 
framework on integrating health equity and racial justice into the and Review. Springer International Publishing; 2022. https://doi. 
artificial intelligence development lifecycle. J Health Care Poor org/10.1007/978-3-030-93765-2
Underserved. 2021;32(2S):300-317. https://doi.org/10.1353/hpu. 63. Bates DW, Auerbach A, Schulam P, Wright A, Saria S. Reporting 
2021.0065. and implementing interventions involving machine learning and 

47. What is explainable AI? (n.d.). Accessed January 19, 2024. https:// artificial intelligence. Ann Intern Med. 2020;172(11_Suppl): 
www.ibm.com/topics/explainable-ai#:�:text=Explainable%20 S137-S144. https://doi.org/10.7326/M19-0872
artificial%20intelligence%20(XAI)%20is,expected%20impact% 64. Carr NG. The Glass Cage: How Our Computers Are Changing 
20and%20potential%20biases Us. New York, London: Norton & Company, 2015.

48. Sendak MP, Gao M, Brajer N, Balu S. Presenting machine learning 65. AI in healthcare: risk management, trust, and liability. Accessed 5 
model information to clinical end users with model facts labels. January, 2024. https://www.dcinetwork.org/events/190
NPJ Digit Med. 2020;3(1):41. https://doi.org/10.1038/s41746- 66. Bates DW, Levine DM, Salmasian H, et al. The safety of inpatient 
020-0253-3 health care. N Engl J Med. 2023;388(2):142-153.

49. Liu Y, Chen P-HC, Krause J, Peng L. How to read articles that use 67. European Union. The EU Artificial Intelligence Act. Accessed 
machine learning: users’ guides to the medical literature. JAMA. December 5, 2024. https://artificialintelligenceact.eu
2019;322(18):1806-1816. https://doi.org/10.1001/jama.2019. 68. Whitehouse. Blueprint for an AI Bill of Rights. Accessed Septem
16489 ber 20, 2024. https://www.whitehouse.gov/ostp/ai-bill-of-rights/

© The Author(s) 2024. Published by Oxford University Press on behalf of the American Medical Informatics Association.
This is an Open Access article distributed under the terms of the Creative Commons Attribution-NonCommercial-NoDerivs licence (https://creativecommons.org/ 
licenses/by-nc-nd/4.0/), which permits non-commercial reproduction and distribution of the work, in any medium, provided the original work is not altered or 
transformed in any way, and that the work is properly cited. For commercial re-use, please contact journals.permissions@oup.com
Journal of the American Medical Informatics Association, 2024, 31, 2730–2739
https://doi.org/10.1093/jamia/ocae209
Case Report

Downloaded from https://academic.oup.com/jamia/article/31/11/2730/7776823 by guest on 28 October 2024