# Catálogo de Aproveitamento dos Artigos para o Projeto

Critério usado:
- `Essencial`: entra diretamente na dissertação, no referencial, método ou justificativa do pipeline.
- `Apoio`: pode reforçar contexto, comportamento, sustentabilidade ou escolha de variáveis.
- `Não aproveitar`: não agrega de forma relevante ao problema central de predição de demanda em RU com IA.

Observação:
- Duplicatas do mesmo PDF em pastas diferentes foram consolidadas.
- Documentos institucionais, contratos, regimentos, imagens e documentação interna não entram aqui como “artigos”.

## Essenciais
- `Turker (2025) - Reducing Food Waste in Campus Dining`: usar como espelho metodológico do projeto. Trabalha campus dining, demanda, clima, cardápio e modelos como Lasso, Extra Trees e XGBoost.
- `Rodrigues et al. (2024) - Machine learning models for short-term demand forecasting in food catering services`: usar para justificar ML em catering, redução prática de desperdício e comparação com gestão manual.
- `Kim et al. (2023) - Comparative analysis of model performance for predicting the customer of cafeteria using unstructured data`: usar para sustentar embeddings de cardápio e NLP aplicado à previsão de clientes em refeitório.
- `Chaudhari et al. (2025) - Forecasting and Modelling of Food Demand Supply Chain using Machine Learning`: usar para defender boosting, lags, médias móveis e a superioridade de LightGBM/XGBoost sobre abordagens tradicionais.
- `Malefors et al. (2022) - Food waste reduction and economic savings in times of crisis`: usar para sustentar previsão de frequência/attendance como peça central para reduzir superprodução.
- `Tang et al. (2023) - Using machine learning method to predict food waste in catering industry under high resolution`: usar para justificar Random Forest e redes neurais em problemas alimentares com alta variabilidade.
- `Wicaksono et al. (2025) - Customer-centric circular economy as-a-service decision-making`: usar como apoio metodológico para feature selection com Random Forest em food service.
- `Ipkovich et al. (2024) - Network science and explainable AI-based life cycle management of sustainability models`: usar para justificar XAI, SHAP e transparência do modelo para gestores.
- `Tripathi et al. (2021) - Ensuring the Robustness and Reliability of Data-Driven Knowledge Discovery Models`: usar na fundamentação metodológica de robustez, qualidade de dados e pipeline iterativo.
- `Xu et al. (2021) - Data science: connotation, methods, technologies, and development`: usar para fundamentar epistemologicamente a Ciência de Dados como base do trabalho.
- `Peffers et al. (2007) - A Design Science Research Methodology for Information Systems Research`: usar como espinha dorsal da metodologia DSR.
- `Hevner et al. (2004) - Design Science in Information Systems Research`: usar para os princípios de avaliação do artefato.
- `Gregor and Hevner (2013) - Positioning and Presenting DSR for Maximum Impact`: usar para enquadrar a contribuição científica do artefato.
- `Simon (1996) - The Sciences of the Artificial`: usar como base filosófica da DSR e da construção do artefato.
- `BERT (Devlin, 2018)`: usar para justificar o componente semântico aplicado aos cardápios.
- `Attention Is All You Need (2017)`: usar apenas como base arquitetural remota para transformer/BERT.
- `XGBoost (Chen, 2016)`: usar para fundamentar o algoritmo.
- `CatBoost (Dorogush, 2018)`: usar para fundamentar o algoritmo.
- `Souza and Orsi (2024) - SIMPROFI`: usar como origem do problema e baseline inicial do projeto.
- `Souza et al. (2025) - SIMPROF`: usar como produção própria consolidando a EDA e a preparação do problema.
- `Souza et al. (2025) - SINGEP`: usar como principal autocitação do produto tecnológico e da arquitetura preditiva.
- `Souza et al. (2025) - Projeto MQA Etapa 4`: usar para o componente de simulação probabilística e análise de risco operacional.

## Apoio
- `Akhter et al. (2024) - food waste behaviour in university students`: útil para explicar comportamento discente e incerteza de demanda.
- `Elnakib et al. (2021) - school food waste training intervention`: útil para discutir intervenção operacional e comportamento em ambientes institucionais.
- `Eriksson et al. (2021) - guest attendance data`: útil para defender dados de presença/frequência como preditores.
- `Steen et al. (2018) - risk factors in food waste`: útil para separar desperdício por superprodução e resto-ingesta.
- `Schwartz et al. (2015) - school meal regulations and plate waste`: útil para discutir como regras mal calibradas ampliam desperdício.
- `Wu et al. (2022) - social media intervention`: útil se você quiser propor nudges digitais no sistema de reservas.
- `Chapman et al. (2017) - lunch timing`: útil para justificar features temporais e efeitos operacionais de calendário/horário.
- `Faezirad et al. (2021) - preventing food waste`: útil como pano de fundo de estratégias preventivas em food service.
- `Lonska et al. (2025) - plate waste in Latvian schools`: útil para discussão de desperdício em instituições públicas.
- `Dhir et al. (2020) - food waste and circular economy SLR`: útil para contextualização ampla de sustentabilidade e economia circular.
- `Onyeaka et al. (2025) - Artificial Intelligence in Food System`: útil para contextualização macro do uso de IA no sistema alimentar.
- `Clark (2025) - AI-driven food waste management in hospitality`: útil para motivação geral, mas não para a modelagem central do RU.
- `Olawale (2025) - sustainable farming with machine learning`: útil para argumento macro de sustentabilidade apoiada por ML.
- `Rajendran (2025) - predictive modelling approach to decoding consumer intention`: útil como apoio sobre intenção de consumo, menos aderente ao RU.
- `Leng et al. (2024) - industrial AI toward Industry 5.0`: útil para posicionamento do trabalho em Indústria 5.0.
- `Kanwal and Zhang (2024) - upcycling and digital twins`: útil para contextualização de sustentabilidade digital, não para o core preditivo.
- `Sarić et al. (2020) - environmental determinants of food choices`: útil para discussão complementar sobre fatores ambientais.
- `Scott and Ensaff (2022) - lockdown food habits`: útil apenas como contexto comportamental amplo.
- `Stacchini et al. (2024) - household waste and university students`: útil para pano de fundo comportamental, não para modelagem.
- `Balzaretti et al. (2020) - portion sizes in school meals`: útil para mostrar que o erro pode nascer na gestão e no dimensionamento da oferta.
- `Eddie et al. (2020) - school nutrition in Navajo reservation`: útil como caso institucional, mas periférico.
- `RMSE vs MAE (Chai, 2014)`: útil para explicar escolha e interpretação de métricas.

## Não aproveitar
- `06 - Unsupervised machine learning in urban studies A systematic review`: não dá para aproveitar no problema central.
- `09 - Improving the Recognition Percentage of the Identity Check System by Applying the SVM`: não dá para aproveitar.
- `10 - Identification and Detection of Cyberbullying on Facebook`: não dá para aproveitar.
- `2018 - State-of-the-art in artificial neural network applications`: não dá para aproveitar diretamente; é genérico demais.
- `2021 - Deep Learning for AI`: não dá para aproveitar diretamente; é genérico demais.
- `2024 - A Survey on Evaluation of Large Language Models`: não dá para aproveitar.
- `2024 - A Review on Large Language Models Architectures Applications Taxonomies Open Issues and Challenges`: não dá para aproveitar.
- `2024 - A Survey of Decision Trees Concepts Algorithms and Applications`: não dá para aproveitar diretamente; é genérico demais.
- `2024 - Comparative analysis of optimization strategies for k-means clustering in Big Data context`: não dá para aproveitar.
- `2024 - Toward a responsible future: recommendations for AI-enabled clinical decision support`: não dá para aproveitar.
- `2025 - Large language models are less effective at clinical prediction task than locally trained machine learning`: não dá para aproveitar.
- `Williams et al. (2025) - hyperspectral pistachios`: não dá para aproveitar no problema do RU.
- `Bathmanathan et al. (2023) - food waste management system in school`: não dá para aproveitar no core do projeto; serve só como contexto muito lateral.
- `Byker Shanks et al. (2023) - behavioural economics and vegetable waste`: não dá para aproveitar no core do projeto.
- `Morosan et al. (2024) - household food waste`: não dá para aproveitar.
- `Reardon et al. (2024) - chefs practices and food waste`: não dá para aproveitar.

## Prioridade de leitura para a dissertação
- `Prioridade 1`: Turker, Rodrigues, Kim, Chaudhari, Malefors, Wicaksono, Tang, Peffers, Hevner, Gregor and Hevner, Ipkovich, Tripathi, Xu, Souza 2024-2025.
- `Prioridade 2`: Akhter, Elnakib, Eriksson, Steen, Schwartz, Wu, Chapman, Leng, RMSE vs MAE.
- `Prioridade 3`: demais artigos de apoio contextual.
