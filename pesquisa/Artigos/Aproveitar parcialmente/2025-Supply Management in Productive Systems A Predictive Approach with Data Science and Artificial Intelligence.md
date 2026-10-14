---
source_file: "2025-Supply Management in Productive Systems A Predictive Approach with Data Science and Artificial Intelligence.txt"
original_rel_path: "Trabalhos\Artigos\Aproveitar parcialmente\txt\2025-Supply Management in Productive Systems A Predictive Approach with Data Science and Artificial Intelligence.txt"
category: "Artigos_Aproveitar_parcialmente"
extension: ".txt"
sha256: "186acff86147c8fba1dfdfe81c414638ef20b01dc4d2dbd9616214e934b4a59e"
extracted_at: "2026-09-20T00:50:21.707087"
---

﻿TÍTULO: GESTÃO DE SUPRIMENTOS EM SISTEMAS PRODUTIVOS: UMA 
ABORDAGEM PREDITIVA COM CIÊNCIA DE DADOS E INTELIGÊNCIA 

ARTIFICIAL 

 
Michel Silva de Souza 

0009-0003-3951-202X 
 

Dr. Carlos Hideo Arima 
0000-0001-7922-0943 

 
Dr. Rafael Nobre Orsi 

0000-0003-4719-0131 
 
1 Introdução 
 

A eficiência dos sistemas produtivos é um fator crítico para a sustentabilidade de 
qualquer organização, seja ela pública ou privada. No contexto da educação profissional, a 
gestão de serviços de apoio, como os refeitórios institucionais, representa um complexo sistema 
produtivo caracterizado pela sequência de entrada (insumos), conversão (preparo) e saída 
(refeições servidas). A otimização deste sistema é fundamental não apenas para a estabilidade 
financeira da instituição, mas também para o cumprimento de metas de sustentabilidade, um 
pilar da Indústria 5.0 (LENG et al., 2024). 

Atualmente, um dos processos mais significativos na gestão de refeitórios de grandes 
IE é a previsão de demanda, o que gera impactos diretos na cadeia de suprimentos. A situação-
problema analisada neste estudo emerge da dinâmica operacional entre uma instituição de 
ensino superior tecnológico e a empresa terceirizada responsável pelo preparo das refeições. O 
processo atual de planejamento de suprimentos é reativo e ineficiente: o quantitativo de 
refeições necessárias para a semana subsequente é comunicado à empresa apenas às sextas-
feiras, com aproximadamente três dias de antecedência. Este prazo extremamente curto, que 
coincide com o final de semana, impõe um severo desafio logístico à empresa, que enfrenta 
dificuldades na aquisição de insumos, especialmente perecíveis. Para mitigar o risco de 
desabastecimento, a prática corrente leva a uma superprodução cautelar ou a compras 
emergenciais com custos elevados, culminando em desperdício de recursos e configurando uma 
falha crítica no sistema produtivo. Na literatura, algumas abordagens apontam o uso de IA e o 
Machine Learning (ML) como soluções promissoras para mitigar o desperdício e otimizar 
cadeias de suprimentos (ONYEAKA et al., 2025; RAJENDRAN et al., 2025; OLAWALE et 
al., 2025). Adicionalmente, a aplicação de IA em hotéis e restaurantes para ajuste de porções e 
gestão de estoque (CLARK et al., 2023) valida a relevância prática desta abordagem. 

O objetivo deste estudo é, portanto, apresentar o desenvolvimento e a validação de um 
produto técnico-tecnológico utilizando técnicas de Ciência de Dados (CD) e Inteligência 
Artificial (IA). Este trabalho visa transformar o processo reativo de planejamento em um 
modelo proativo com um sistema que fornece previsões acuradas com maior antecedência, 
baseando-se em dados históricos de demanda, calendário e fatores externos, conforme a 
literatura indica (CHAUDHARI et al., 2025). Esta intervenção busca reduzir o desperdício de 
alimentos, otimizar a gestão da cadeia de suprimentos, aumentar a eficiência operacional e 
promover a sustentabilidade e inovação em sistemas produtivos (LENG et al., 2024; 
OLAWALE et al., 2025). 

Este relato detalha a metodologia de construção do sistema, desde a fundamentação 
teórica até a implementação prática e a análise dos resultados, demonstrando o potencial das 
tecnologias digitais como ferramenta de apoio à decisão para resolver problemas complexos 
em ambientes organizacionais (XU et al., 2021; TRIPATHI et al., 2021). 
__________________________________________________________________________________________ 

 Anais do XIII SINGEP-CIK – UNINOVE – São Paulo – SP – Brasil – 22 a 24/10/2025 1 



 
 

 
2 Referencial Teórico 
 

A aplicação de tecnologias digitais para otimizar sistemas produtivos tem sido 
amplamente documentada na literatura, com a IA e o ML emergindo como ferramentas 
poderosas para a previsão de demanda e a gestão de cadeias de suprimentos. Este referencial 
teórico contextualiza a solução proposta com base em estudos que validam sua abordagem, 
alinhando-se ao tema das Tecnologias Digitais e Sustentabilidade em Sociedades Resilientes. 

Recentemente, têm surgido trabalhos que mostram que a IA é uma tecnologia 
transformadora na gestão de serviços de alimentação. Estudos como os de Onyeaka et al. (2025) 
destacam o papel da IA na minimização do desperdício de alimentos (food waste) através de 
análises preditivas que permitem um planejamento mais acurado. A capacidade de prever a 
demanda com precisão pode reduzir o desperdício em até 30% (Kanwal et al., 2025), um dado 
que reforça o potencial de impacto econômico e ambiental da solução aqui desenvolvida. 
Publicações de mercado, como a análise da Shiji Insights (2025) e o trabalho de Clark et al. 
(2023), confirmam que hotéis e restaurantes já utilizam sistemas baseados em IA para ajustar 
porções e gerenciar estoques de forma dinâmica, validando a relevância prática desta 
abordagem. 

Para que um modelo preditivo seja eficaz é importante saber selecionar as variáveis que 
causam maior impacto no processo. Trabalhos como o de Chaudhari et al. (2025) e uma análise 
sistemática da área apontam que variáveis como o histórico de demanda, dados de calendário 
(dias da semana, feriados), características do cardápio e dados climáticos são preditores-chave. 
A complexidade aumenta quando centenas de variáveis são criadas, como neste estudo, 
tornando essencial o uso de técnicas de seleção de features para construir um modelo 
parcimonioso e robusto o suficiente para evitar o ruído de variáveis irrelevantes (XU et al., 
2021). 

No que tange aos algoritmos, a escolha por um “comitê de modelos” está alinhada com 
as melhores práticas. Chaudhari et al. (2025) e Rajendran et al. (2025) mencionam algoritmos 
como Gradient Boosting e XGBoost como estado da arte para problemas de previsão em dados 
tabulares, devido à sua alta performance. Além desses, a arquitetura metodológica adotada neste 
trabalho emprega um modelo híbrido residual, que combina a robustez de modelos lineares, 
como Ridge, para capturar tendências gerais com a capacidade de modelos de árvores, como 
ExtraTrees, para aprender os resíduos. Essa abordagem de ensemble learning, que também 
inclui técnicas como Voting e Stacking, permite explorar a diversidade de algoritmos para 
otimizar a precisão, conforme discutido por Kuhl et al. (2021) e Mohaiminul et al. (2024), 
garantindo a confiabilidade do sistema (TRIPATHI et al., 2021). 

A solução proposta, ao integrar CD com a aplicabilidade da IA, alinha-se a abordagens 
promissoras na literatura que apontam para uma otimização dos sistemas produtivos para a 
sustentabilidade (OLAWALE et al., 2025). Desta forma, neste estudo é apresentado uma 
aplicação de modelagem, com intervenção gerencial fundamentada que visa aprimorar a 
governança e a eficiência do sistema produtivo em análise. 

 
3 Metodologia 
 

Este relato técnico descreve o processo de desenvolvimento e implementação de um 
produto tecnológico, concebido como uma intervenção gerencial para solucionar a ineficiência 
na cadeia de suprimentos de refeições de uma instituição de ensino superior tecnológico. Todo 
o processo metodológico, desde a análise exploratória até a validação do modelo final, foi 
documentado em um notebook computacional, cujo código-fonte está disponível para fins de 
reprodutibilidade e será fornecido mediante solicitação para garantir o anonimato durante o 
__________________________________________________________________________________________ 

 Anais do XIII SINGEP-CIK – UNINOVE – São Paulo – SP – Brasil – 22 a 24/10/2025 2 



 
 

processo de revisão. O conjunto de dados original, por conter informações sensíveis da 
instituição de ensino, não foi disponibilizado. 

 
3.1 Caracterização do Problema e Coleta de Dados 
 

O ponto de partida foi a análise do sistema produtivo de refeições, identificando o 
principal gargalo: a ausência de um mecanismo de previsão de demanda que permitisse um 
planejamento de suprimentos com antecedência. A única informação disponível para a gestão 
era a contagem de reservas, que, como será demonstrado, é um indicador insuficiente para um 
planejamento preciso. 

Um dos desafios centrais na gestão de serviços de alimentação é a discrepância entre o 
número de itens reservados e o consumo efetivo. Conforme ilustrado na Figura 1, que compara 
o total de reservas diárias com a demanda real de refeições servidas ao longo do período 
analisado, mostrando que existe uma variabilidade significativa entre as duas séries. Em certos 
dias, a demanda supera as reservas, enquanto em outros ocorre o inverso. Esta volatilidade torna 
o planejamento baseado apenas em reservas, que é uma prática arriscada, justificando a 
necessidade de um modelo preditivo mais robusto que possa aprender com esses padrões e 
incorporar outras variáveis de contexto. 

 
Figura 1 - Análise da Variabilidade entre Reservas e Demanda Real 

Para desenvolver a solução, foi realizada a coleta de dados primários e secundários. Os 
dados primários consistem nos próprios registros diários de refeições servidas e reservadas na 
instituição de ensino, abrangendo um período histórico de 78 dias letivos. Foram coletados 
também dados secundários que, conforme a literatura, influenciam o comportamento do 
consumidor e são relevantes para o contexto, como: o calendário acadêmico, para identificar 
dias letivos, feriados e eventos; e dados meteorológicos, de temperatura e precipitação 
(Chaudhari et al., 2025). O resultado foi um dataset inicial com 15.279 registros individuais, 
que serviu de base para a construção do modelo. 
 
3.2 Estruturação dos Dados e Seleção de Features 
 

Os dados brutos, em nível de registro individual, foram transformados por um processo 
de agregação para que cada linha representasse um único dia e suas características consolidadas. 

__________________________________________________________________________________________ 
 Anais do XIII SINGEP-CIK – UNINOVE – São Paulo – SP – Brasil – 22 a 24/10/2025 3 



 
 

Em seguida, foi aplicada a engenharia de features, para enriquecer o dataset com informações 
contextuais e temporais. Foram criadas 243 variáveis preditivas, incluindo: 

• Lags e Médias Móveis: Variáveis que representam a demanda de dias anteriores (ex: 
lag_1d, lag_7d) e a média de consumo recente (ma_7d), permitindo ao modelo capturar 
tendências e sazonalidades de curto prazo. 

• Features de Calendário: Variáveis que codificam o dia da semana, mês e dia do ano, 
incluindo representações cíclicas (seno/cosseno) para melhor interpretação pelos 
algoritmos. 

• Features de Contexto: Variáveis que integram dados de reservas, meteorologia e 
eventos acadêmicos, fornecendo ao modelo uma visão holística dos fatores que podem 
influenciar a demanda. 
Com um conjunto tão vasto de variáveis, a primeira etapa da análise foi explorar quais 

possuíam a maior relação linear com a demanda. As Figuras 2 e 3 apresentam as 10 features 
com maior correlação positiva e negativa, respectivamente. 

 
Figura 2 - Top 10 Features com Maior Correlação Positiva com a Demanda 

 
A análise exploratória inicial identificou as variáveis com maior correlação linear 

positiva com a demanda diária. A Figura 2 apresenta as dez features mais impactantes, 
destacando reservas_total e alunos_unicos_dia como os principais impulsionadores do 
consumo. Variáveis de contexto, como a ocorrência de quartas-feiras (ocorrencia_quarta) e o 
histórico de consumo (delta_serv_res_lag_3d), também se mostraram preditores relevantes 
nesta fase inicial de análise. 

 

__________________________________________________________________________________________ 
 Anais do XIII SINGEP-CIK – UNINOVE – São Paulo – SP – Brasil – 22 a 24/10/2025 4 



 
 

 
Figura 3 - Top 10 Features com Maior Correlação Negativa com a Demanda 

 
A Figura 3 complementa a análise ao apresentar as dez features com a maior correlação 

linear negativa com a demanda. Destaca-se a variável dia_semana, indicando que a demanda 
tende a diminuir com o avançar da semana. Fatores como a ocorrência de sextas-feiras 
(ocorrencia_sexta) e características do cardápio, como a presença de proteína bovina, também 
surgem como importantes detratores do consumo. 

Diante da alta dimensionalidade, tornou-se fundamental determinar o número ideal de 
features para evitar a inclusão de ruído e a complexidade desnecessária. Para isso, foi realizada 
uma análise de desempenho em função do número de features. O resultado, ilustrado na Figura 
4, demonstrou que a performance ótima (menor Erro Médio Absoluto) foi atingida com um 
conjunto enxuto de apenas 5 features, validando a escolha por um modelo mais parcimonioso 
e robusto. 

 

 
Figura 4 - Desempenho (MAE) vs. Número de Features Selecionadas 

 
A relação interna entre as 5 features finais selecionadas e a variável alvo (servidas_total) 

é detalhada no mapa de correlação da Figura 5. 
 

__________________________________________________________________________________________ 
 Anais do XIII SINGEP-CIK – UNINOVE – São Paulo – SP – Brasil – 22 a 24/10/2025 5 



 
 

 
Figura 5 - Mapa de Correlação das Features Selecionadas 

 
A análise da primeira linha do mapa de correlação (Figura 5) revela insights importantes 

para a modelagem: 
• Correlação Positiva Forte: As variáveis alunos_unicos_dia (0.60) e reservas_total 

(0.56) apresentam a maior correlação positiva com a demanda, confirmando que o 
número de pessoas presentes e o número de reservas são preditores fundamentais. A 
variável delta_serv_res_lag_3d (0.49), que representa a diferença entre refeições 
servidas e reservadas há três dias, também mostra uma forte correlação positiva, 
indicando que o “comportamento de no-show” recente é um forte preditor da demanda 
atual. 

• Correlação Negativa: A variável dia_semana (-0.52) mostra uma correlação negativa, 
indicando que a demanda tende a diminuir ao longo dos dias da semana (onde segunda-
feira = 0 e sexta-feira = 4). 

• Multicolinearidade: O mapa também expõe relações entre as próprias features, como 
a forte correlação negativa entre dia_semana e dia_semana_cos (-0.97). Essa 
compreensão é vital para a escolha de algoritmos, pois modelos baseados em árvores, 
como os utilizados neste estudo, são inerentemente robustos a problemas de 
multicolinearidade. 
Essa análise visual mostrou a relevância das features selecionadas e, também, forneceu 

um entendimento mais profundo da dinâmica dos dados, orientando a construção de um modelo 
preditivo mais preciso e interpretável. 

 
3.3 Desenvolvimento e Treinamento do Sistema Preditivo 
 

Para garantir a escolha da solução preditiva mais robusta e precisa, a metodologia 
empregou uma abordagem de modelagem competitiva, cujo fluxo de trabalho está ilustrado na 
Figura 6. O processo foi desenhado para simular o desafio operacional real, desde a preparação 
dos dados até a validação final do modelo. 

__________________________________________________________________________________________ 
 Anais do XIII SINGEP-CIK – UNINOVE – São Paulo – SP – Brasil – 22 a 24/10/2025 6 



 
 

O ponto de partida foram os Dados Históricos Processados, um conjunto de 69 dias de 
operação já agregados e enriquecidos com features. Este conjunto foi submetido a uma Divisão 
Estratégica, separando os 14 dias mais recentes como Conjunto de Teste Final (Hold-Out), 
dados que o modelo nunca veria durante o treinamento, e os 55 dias restantes como Conjunto 
de Treino/Validação. 

Este último conjunto alimentou a Fase de Modelagem Competitiva, que consistiu em 
três etapas sequenciais: um Benchmark de Modelos base, a Otimização de Hiperparâmetros 
dos melhores candidatos com a biblioteca Optuna, e a Avaliação de Ensembles avançados. O 
resultado desta fase foi a Seleção do Modelo Campeão, a arquitetura “Campeão Híbrido”. 

Finalmente, na etapa de Validação Final, o modelo campeão foi treinado com todos os 
55 dias do conjunto de treino e avaliado uma única vez no Conjunto de Teste Final, provando 
sua eficácia em prever a demanda em um cenário futuro desconhecido. 

 
Figura 6 - Fluxograma da Metodologia de Desenvolvimento e Validação do Modelo 

 
Os modelos base foram selecionados para abranger diferentes abordagens de 

aprendizado de máquina, garantindo diversidade nas estratégias de previsão: 

__________________________________________________________________________________________ 
 Anais do XIII SINGEP-CIK – UNINOVE – São Paulo – SP – Brasil – 22 a 24/10/2025 7 



 
 

• Modelos baseados em Árvores de Decisão (Gradient Boosting, XGBoost, LightGBM, 
CatBoost, RandomForest, ExtraTrees): Escolhidos por sua alta performance em dados 
tabulares e capacidade de capturar interações complexas e não-lineares, sendo 
amplamente citados na literatura como estado da arte para problemas de previsão 
(Chaudhari et al., 2025). 

• Modelos Lineares (ElasticNet, Ridge): Incluídos para fornecer uma perspectiva linear 
e servir como um baseline robusto. 

• Modelos baseados em Distância (KNN): Utilizados por sua lógica de decisão distinta, 
que analisa a proximidade dos dados em vez de regras hierárquicas. 
Além dos modelos individuais, três técnicas avançadas de ensemble learning foram 

implementadas para potencializar a acurácia final, uma estratégia validada para otimizar a 
precisão em problemas complexos (Kuhl et al., 2021; Mohaiminul et al., 2024): 

• Modelo Híbrido Residual: Uma arquitetura customizada, desenvolvida neste estudo, 
que combina um modelo linear (Ridge) para capturar a tendência principal dos dados, e 
um modelo de árvore (ExtraTrees) que é treinado especificamente para aprender e 
corrigir os erros (resíduos) do modelo linear. 

• Voting Ensemble (Comitê Ponderado): Esta técnica agrega as previsões de múltiplos 
modelos especialistas (KNN, ExtraTrees, Ridge, CatBoost) através de uma votação 
ponderada, buscando um “conselho de especialistas” que equilibra performance e 
diversidade. 

• Custom Stacking Ensemble (Empilhamento de Modelos): Uma abordagem em que 
um meta-modelo (Ridge Regression) é treinado para aprender a melhor forma de 
combinar as previsões out-of-fold dos modelos base. Esta técnica permite ao Stacking 
aprender os padrões de erro de cada modelo e ponderar suas “opiniões” de forma 
inteligente. 
O processo de validação foi desenhado para simular o desafio operacional real: prever 

a demanda para um dia futuro desconhecido. Para isso, os 69 dias de dados históricos foram 
divididos da seguinte forma, uma prática comum para evitar otimismo nos resultados e garantir 
a robustez do modelo (Tripathi et al., 2021): 

• Conjunto de Teste Final (Hold-Out): Os 14 dias mais recentes com demanda 
representativa foram completamente separados para uma única avaliação final, 
simulando a operação em um período futuro. 
Conjunto de Treino e Validação: Os 55 dias restantes foram utilizados para treinar os 

modelos e realizar a validação cruzada temporal (TimeSeriesSplit), uma técnica essencial para 
avaliar modelos em dados sequenciais, pois garante que o treinamento seja sempre feito com 
dados passados para prever o futuro, evitando vazamento de informações. 

 
4 Análise e Discussão dos Resultados 
 

A avaliação do sistema preditivo foi conduzida com o objetivo de validar sua eficácia 
como ferramenta de apoio à decisão. Os resultados quantitativos, obtidos a partir da etapa de 
validação, e a aplicação prática do modelo no cenário de teste final (hold-out) são apresentados 
e discutidos a seguir. 
 
4.1 Desempenho dos Modelos Preditivos 
 

Para identificar o algoritmo mais eficaz, foi realizada uma avaliação comparativa do 
comitê de 10 modelos base e 3 arquiteturas de ensemble. O desempenho foi mensurado 
utilizando métricas padrão para regressão, conforme validado na literatura (Chaudhari et al., 

__________________________________________________________________________________________ 
 Anais do XIII SINGEP-CIK – UNINOVE – São Paulo – SP – Brasil – 22 a 24/10/2025 8 



 
 

2025). O benchmark inicial (Figuras 7, 8 e 9) destacam o Modelo Híbrido como a arquitetura 
mais promissora. 

 

 
Figura 7 - Benchmark dos Modelos por Coeficiente de Determinação (R²) 

 
O benchmark inicial do comitê de modelos foi realizado para identificar as arquiteturas 

mais promissoras. A Figura 7, que compara o Coeficiente de Determinação (R²) de cada 
modelo, destaca claramente a superioridade do Modelo Híbrido. Com um R² de 42,40%, ele 
demonstrou um poder explicativo consideravelmente maior que os demais modelos base, 
consolidando-se como o principal candidato para a fase de otimização. 

 

 
Figura 8 - Benchmark de Modelos por Erro Médio Absoluto (MAE) 

 
A Figura 8 complementa a análise ao comparar o Erro Médio Absoluto (MAE) das três 

arquiteturas finalistas. A imagem ilustra que o Campeão Híbrido obteve o menor erro médio 
(13.05 refeições), reforçando sua capacidade de manter um erro baixo de forma consistente e 
superando as abordagens de ensemble mais tradicionais. 

 

__________________________________________________________________________________________ 
 Anais do XIII SINGEP-CIK – UNINOVE – São Paulo – SP – Brasil – 22 a 24/10/2025 9 



 
 

 
Figura 9 - Benchmark de Modelos por Coeficiente de Determinação (R²) 

 
O Coeficiente de Determinação (R²), ilustrado na Figura 9, mede a proporção da 

variância na demanda que cada modelo consegue explicar. O Campeão Híbrido novamente 
alcançou o melhor resultado, com um R² de 49.73%, significando que o modelo explica quase 
50% da variabilidade dos dados — um indicador de forte poder preditivo para um problema 
com alta volatilidade. 

Após uma fase de otimização de hiperparâmetros com Optuna, as três arquiteturas de 
ensemble foram comparadas. A Tabela 1 consolida os resultados da validação cruzada, 
confirmando a superioridade do modelo Campeão Híbrido. 

 

Tabela 1 - Comparativo de Desempenho dos Ensembles Finais (Validação Cruzada) 

 
MAE RMSE R2 

Campeao_Hibrido 13.047825 15.617246 0.497282 

CustomStacking 14.083890 17.336900 0.397241 

VotingRegressor 14.260796 16.975271 0.423900 

 
A análise das figuras 8 e 9 e da tabela 1, que representam o erro médio esperado em 

número de refeições, revela que o Modelo Híbrido (Campeão Otimizado) obteve o melhor 
desempenho, com um MAE de 13.05 refeições. Este resultado demonstra a capacidade do 
modelo de manter um erro médio baixo de forma consistente, superando significativamente os 
demais algoritmos testados. Similarmente, para o RMSE (Raiz do Erro Quadrático Médio), o 
Modelo Híbrido também se destacou com o menor valor de 15.62, indicando a maior precisão 
geral entre os competidores. Quanto ao Coeficiente de Determinação (R²), o Modelo Híbrido 
novamente alcançou o melhor resultado, com um R² de 0.497, significando que o modelo 
explica aproximadamente 50% da variabilidade dos dados, um indicador de forte poder 
preditivo. 
 
4.2 Análise da Predição no Cenário de Teste Final (Hold-Out) 
 

A validação mais crítica do sistema consistiu em testar o modelo campeão em um 
conjunto de hold-out de 14 dias, um período que ele nunca havia visto durante o treinamento. 
Neste cenário, que simula a operação real, a solução alcançou um Erro Médio Absoluto (MAE) 
de 10.68 refeições e um Coeficiente de Determinação (R²) de 64.37%. Este resultado é uma 
forte evidência da acurácia e da confiabilidade do sistema para o planejamento operacional. A 

__________________________________________________________________________________________ 
 Anais do XIII SINGEP-CIK – UNINOVE – São Paulo – SP – Brasil – 22 a 24/10/2025 10 



 
 

Figura 10 ilustra a alta aderência das previsões do modelo à demanda real durante este período 
de teste. 

 

 
Figura 10 - Desempenho do Modelo Campeão no Teste Final (Hold-Out) 

 
Para o período em questão, o modelo demonstrou um Erro Médio Absoluto (MAE) de 

10.68 refeições, um RMSE de 14.61 e um Coeficiente de Determinação (R²) de 64.37%. Este 
resultado, com um erro baixo e uma capacidade de explicar quase dois terços da variação da 
demanda, é uma forte evidência da acurácia e da confiabilidade do sistema para o planejamento 
operacional. 

A Figura 10 ilustra essa alta aderência, comparando a demanda real (linha contínua azul) 
com as previsões do modelo (linha tracejada vermelha). É notável a capacidade do sistema em 
capturar tanto os picos quanto os vales da demanda ao longo do período de teste, demonstrando 
que a tecnologia pode, de fato, fornecer estimativas muito próximas da realidade, mesmo em 
um cenário de alta volatilidade. 

 
4.3 Análise de Impacto Prático e Financeiro (Backtesting) 
 

A principal contribuição deste sistema reside em sua capacidade de superar a incerteza 
inerente ao planejamento baseado apenas em reservas. Como demonstrado na Figura 1, a 
variabilidade entre as reservas e a demanda real é substancial. Utilizar o número de reservas 
como único preditor resultaria em erros diários significativos, em alguns dias, uma falta de mais 
de 50 refeições; em outros, um excedente de mais de 40. Essa discrepância reflete um desafio 
universal em serviços de alimentação, onde a intenção do consumidor nem sempre se traduz 
em consumo efetivo. Trata-se de um problema análogo enfrentado em indústrias como a 
hoteleira, que lida com a imprevisibilidade no número de hóspedes (Shiji Insights, 2025), e a 
aérea, que gerencia a complexidade logística da preparação antecipada de refeições (Kanwal et 
al., 2025). 

A eficácia do sistema de IA desenvolvido é comprovada ao comparar diretamente a 
precisão do modelo com a variabilidade das reservas. Enquanto o planejamento baseado em 
reservas apresenta desvios que frequentemente ultrapassam 30/40 refeições, o modelo Campeão 
(Modelo Híbrido) alcançou um erro médio (MAE) de 10.68 refeições e um erro quadrático 
médio (RMSE) de 14.61 refeições no conjunto de testes. A Figura 10 ilustra essa superioridade: 
a linha de previsão (vermelha) se ajusta de forma muito mais consistente à demanda real (azul) 
do que a linha de reservas (apresentada na Figura 1), suavizando os picos e vales extremos da 
intenção do consumidor. 

Neste produto tecnológico é feita uma otimização ao traduzir a previsão em uma 
recomendação acionável. A Figura 11 ilustra a “Sugestão de Preparo”, que incorpora a precisão 
do modelo a regras de negócio inteligentes, com margem de segurança e limite de reservas, 
oferecendo à gestão uma ferramenta de apoio para o planejamento. 
__________________________________________________________________________________________ 

 Anais do XIII SINGEP-CIK – UNINOVE – São Paulo – SP – Brasil – 22 a 24/10/2025 11 



 
 

 

 
Figura 11 - Visualização da Saída do Sistema: Previsões e Sugestão de Preparo 

A análise da Figura 11 revela a inteligência do sistema e sua contribuição direta para a 
gestão. O gráfico compara o número de Reservas Efetuadas (linha azul) com a Previsão 
Otimizada (linha vermelha) para os dias futuros, evidenciando a aplicação das regras de 
negócio: 

• Evitando a Superprodução: Para os dias 16 e 17/06, a previsão otimizada é 
consistentemente menor que o número de reservas. O sistema identifica que, apesar do 
alto número de reservas, a demanda real esperada é menor, recomendando uma 
produção mais enxuta para evitar o desperdício. 

• Mitigando o Risco: No dia 20/06, o sistema prevê uma demanda muito baixa (48 
refeições), mesmo com 86 reservas. Esta previsão conservadora, provavelmente 
baseada em padrões históricos (ex: proximidade de feriados), evita um desperdício 
massivo que ocorreria ao seguir o método reativo, provando ser uma ferramenta de 
mitigação de risco. 
Essa funcionalidade transforma a gestão de reativa para proativa. Com essas 

informações disponíveis com semanas de antecedência, a empresa parceira pode otimizar a 
compra de insumos e reduzir drasticamente as perdas, resolvendo o gargalo logístico que 
motivou este estudo. 

Para complementar esta análise e demonstrar o impacto financeiro direto da solução, 
apresentamos o resumo do desempenho simulado da estratégia “IA (Máxima)” em comparação 
com a linha de base “Reservas (Base)” no período de 55 dias de backtesting: 

 

Tabela 2 - Resumo do Desempenho das Estratégias no Backtesting 

Total de Total de Custo Total 
Estratégia 

Sobras Faltas Estimado 

IA (Máxima) 421 429 R$ 22.203,44 

Reservas (Base) 847 409 R$ 28.904,40 

 
A estratégia “IA (Máxima)” demonstrou uma redução significativa no custo total 

estimado (R$ 22.203,44 vs. R$ 28.904,40) mesmo que isso tenha implicado em um ligeiro 
aumento nas faltas em comparação com a linha de base. No entanto, a redução de sobras foi 
substancialmente maior (421 pratos vs. 847 pratos), o que, no contexto de um refeitório, é 
frequentemente mais desejável para evitar desperdício de alimentos perecíveis. 

Para uma visão mais granular do desempenho diário das estratégias, o placar de vitórias 
diárias é apresentado na Figura 12: 

__________________________________________________________________________________________ 
 Anais do XIII SINGEP-CIK – UNINOVE – São Paulo – SP – Brasil – 22 a 24/10/2025 12 



 
 

 

 
Figura 12 - Placar de Vitórias Diárias 

O placar de vitórias diárias reforça a superioridade da estratégia de IA, com 21 dias onde 
a IA venceu por ter menos sobras, e 30 dias de empate (onde ambas as estratégias tiveram o 
mesmo custo total). A linha de base venceu em apenas 4 dias por ter menos faltas. Isso indica 
que a IA, ao otimizar o balanço entre sobras e faltas, conseguiu um desempenho mais 
consistente e vantajoso na maioria dos dias. 
 
4.4 Produto Final: Plano de Ação para a Gestão 

 
Um modelo preditivo, por si só, não resolve o problema de gestão. A etapa final da 

metodologia foi traduzir a previsão estatística em uma recomendação prática e acionável. Para 
isso, foram implementadas duas regras de negócio no sistema: 

• Margem de Segurança Inteligente: Com base na análise dos erros históricos do 
modelo campeão, foi calculada uma margem de segurança de aproximadamente 11 
refeições (MAE de 10.68) para ser adicionada à previsão. Esta margem, que pode ser 
adaptativa por dia da semana, visa mitigar o risco de subestimação, que é mais crítico 
para a operação do que a superestimação. 

• Limite por Reservas: A recomendação final de preparo (Sugestão de Preparo) foi 
definida como o menor valor entre a previsão + margem e o total de reservas do dia. 
Esta regra garante que o sistema nunca sugira preparar mais refeições do que o número 
de pessoas que já se comprometeram a consumir, evitando o desperdício evidente. Esta 
metodologia resultou em um produto tecnológico que não apenas prevê um número, 
mas prescreve uma ação de gestão informada e segura. 
 

 
Figura 13 - Visualização da Saída do Sistema: Previsões e Sugestão de Preparo 

 
A Figura 13 ilustra a saída final do sistema: um plano de ação diário que fornece à gestão 

uma visão completa para a tomada de decisão. O gráfico apresenta: 
• Reservas Efetuadas (linha azul): O número de refeições já confirmadas, servindo 

como uma linha de base. 
• Previsão Central (IA) (linha pontilhada): A estimativa mais provável de demanda, 

calculada pelo modelo campeão. 

__________________________________________________________________________________________ 
 Anais do XIII SINGEP-CIK – UNINOVE – São Paulo – SP – Brasil – 22 a 24/10/2025 13 



 
 

• Faixa de Incerteza (área sombreada): O intervalo entre a Sugestão Mínima (IA) e a 
Sugestão Máxima (IA). Esta faixa representa a variabilidade esperada da previsão, 
calculada com base na margem de segurança adaptativa. 

Esta visualização transforma a gestão de reativa para proativa. Em vez de um único número, o 
sistema fornece um cenário completo de risco. Para o dia 20/06, por exemplo, o modelo prevê 
uma demanda central baixa, mas a faixa de incerteza indica um risco considerável. Essa 
ferramenta permite à gestão tomar decisões informadas, como alinhar a produção à previsão 
central para economizar, ou produzir mais perto da sugestão máxima para garantir o nível de 
serviço, mesmo diante de eventos atípicos. 
 
5 Considerações Finais e Contribuições 
 

Este estudo detalhou o desenvolvimento de um produto tecnológico destinado a 
melhorar a gestão do sistema produtivo de refeições de uma instituição de ensino superior. A 
intervenção proposta, materializada em um sistema de previsão de demanda baseado em IA, 
demonstrou ser uma ferramenta eficaz para otimizar o planejamento de suprimentos, mitigar o 
desperdício de alimentos e, consequentemente, aprimorar a eficiência operacional e a 
sustentabilidade da instituição. 

O objetivo inicial de criar um mecanismo que fornecesse previsões acuradas com maior 
antecedência foi alcançado. Os resultados da validação do modelo, que culminaram em um erro 
médio absoluto (MAE) de aproximadamente 10.68 refeições e um coeficiente de determinação 
(R²) de 64.37% no teste final, validam a robustez da metodologia empregada. Mais importante 
que a precisão estatística, o sistema incorpora uma lógica de negócio com margem de segurança 
inteligente e limite por reservas que transforma a previsão em uma recomendação de preparo 
diretamente aplicável pela gestão, configurando-se como um autêntico sistema de apoio à 
decisão. 

 
Contribuições para a Gestão e o Setor Produtivo: 
 

A principal contribuição deste trabalho é a apresentação de uma solução tecnológica 
replicável para um desafio comum em diversas organizações: a gestão de recursos em cenários 
de demanda flutuante. Para a instituição analisada e sua empresa parceira, a implementação 
deste sistema representa: 

1. Otimização da Cadeia de Suprimentos: A capacidade de prever a demanda com 
semanas de antecedência resolve o gargalo logístico, permitindo à empresa fornecedora 
um planejamento de compras mais eficiente, com potencial redução de custos e 
melhoria na qualidade dos insumos. 

2. Redução de Custos e Desperdício: Ao minimizar a superprodução, o sistema contribui 
diretamente para a redução de despesas com alimentos não consumidos e custos de 
descarte, aliviando o orçamento da instituição. 

3. Promoção da Sustentabilidade: Alinhado aos Objetivos de Desenvolvimento 
Sustentável (ODS), o projeto demonstra um caminho prático para que instituições de 
ensino incorporem a sustentabilidade em suas operações diárias, servindo de exemplo 
para a comunidade acadêmica. 

 
Limitações e Propostas para Trabalhos Futuros: 
 

A principal limitação deste estudo reside no volume de dados históricos disponíveis, 
que abrangeu um período de aproximadamente quatro meses. Embora os resultados sejam 

__________________________________________________________________________________________ 
 Anais do XIII SINGEP-CIK – UNINOVE – São Paulo – SP – Brasil – 22 a 24/10/2025 14 



 
 

promissores, um histórico mais longo permitiria capturar sazonalidades anuais e aumentar ainda 
mais a confiabilidade do modelo. 

Como propostas para a evolução deste trabalho técnico-profissional, destacam-se: 
1. Implantação em Produção e Monitoramento Contínuo: O próximo passo natural é a 

implementação do sistema na rotina da gestão do refeitório, com o re-treinamento 
periódico do modelo à medida que novos dados são coletados. 

2. Desenvolvimento de uma Interface de Usuário (Dashboard): A criação de um painel 
de controle interativo para que os gestores possam visualizar as previsões e ajustar 
parâmetros, tornando a ferramenta ainda mais acessível. 

3. Integração via API: Conforme apontado pela literatura (Shiji Insights, 2025), a 
integração do sistema de previsão com outros sistemas da instituição (como sistemas de 
compra ou controle de estoque) via API (Application Programming Interface) 
representaria um avanço significativo na automação dos processos de gestão. 

4. Escalabilidade: O modelo e a metodologia aqui descritos são escaláveis e poderiam ser 
adaptados para outros campi ou outras instituições de ensino que enfrentam desafios 
similares. 
Em suma, este trabalho evidencia como a aplicação de tecnologias digitais, 

fundamentada em uma metodologia científica, pode gerar soluções para problemas da gestão 
em sistemas produtivos, fortalecendo a sinergia entre academia e setor produtivo e contribuindo 
para a formação de profissionais capazes de liderar a inovação em suas organizações. 

 
6 Referências 

 
Chaudhari, M. A., Phapale, A., Gagare, P., Kardile, T., & Phatangare, A. (2025). Forecasting 
and Modelling of Food Demand Supply Chain using Machine Learning. International Journal 
of Innovative Research in Multidisciplinary Physical Sciences (IJIRMPS), 13(2), 1-16. 
https://www.ijirmps.org/papers/2025/2/232389.pdf 

Clark, M., Basavaraja, D., Kanavikar, J., & Donnelly, P. (2025). Exploring the potential of AI-
driven food waste management strategies used in the hospitality industry for application in 
household settings. Frontiers in Artificial Intelligence, 6, 1429477. 
https://doi.org/10.3389/frai.2024.1429477 

Kanwal, N., Zhang, M., Zeb, M., Hussain, M., & Wang, D. (2025). Revolutionizing food safety 
in the airline industry: AI-powered smart solutions. Trends in Food Science & Technology, 
159, 104970. https://doi.org/10.1016/j.tifs.2025.104970 

Kuhl, N., Hirt, R., Baier, L., Schmitz, B., & Satzger, G. (2021). How to Conduct Rigorous 
Supervised Machine Learning in Information Systems Research: The Supervised Machine 
Learning Report Card. Communications of the Association for Information Systems, 48. 

Leng, J., Wang, D., Shen, B., Li, Z., Liu, Q., Chen, X., & Liu, C. (2024). Unlocking the power 
of industrial artificial intelligence towards Industry 5.0: Insights, pathways, and challenges. 
Journal of Manufacturing Systems, 72, 103-116. https://doi.org/10.1016/j.jmsy.2024.01.001 

Mohaiminul, M., Khan, M. A. R., & Rahman, M. M. (2024). A Review on Large Language 
Models: Architectures, Applications, Taxonomies, Open Issues and Challenges. IEEE Access. 

__________________________________________________________________________________________ 
 Anais do XIII SINGEP-CIK – UNINOVE – São Paulo – SP – Brasil – 22 a 24/10/2025 15 



 
 

Olawale, R. A., Olawumi, M. A., & Oladapo, B. I. (2025). Sustainable farming with machine 
learning solutions for minimizing food waste. Journal of Stored Products Research, 112, 
102611. https://doi.org/10.1016/j.jspr.2025.102611 

Onyeaka, H., Akinsemolu, A., Miri, T., Nnaji, N. D., Duan, K., Pang, G., Tamasiga, P., Khalid, 
S., Al-Sharify, Z. T., & Ugwa, C. (2025). Artificial Intelligence in Food System: Innovative 
Approach to Minimizing Food Spoilage and Food Waste. Journal of Agriculture and Food 
Research, 21, 101895. https://doi.org/10.1016/j.jafr.2025.101895 

Rajendran, B., Babu, M., & Anandhabalaji, V. (2025). A predictive modelling approach to 
decoding consumer intention for adopting energy-efficient technologies in food supply chains. 
Decision Analytics Journal, 15, 100561. https://doi.org/10.1016/j.dajour.2025.100561 

Shiji Insights. (2025). Technology's role in reducing hotel food waste. Shiji Group. 
https://insights.shijigroup.com/technologys-role-in-reducing-hotel-food-waste/ 

Tripathi, S., et al. (2021). Ensuring the Robustness and Reliability of Data-Driven Knowledge 
Discovery Models in Production and Manufacturing. Frontiers in Artificial Intelligence, 4, 73. 
https://doi.org/10.3389/frai.2021.721471 

Xu, Z., et al. (2021). Data science: connotation, methods, technologies, and development. Data 
Science and Management, 4(2), 79-88. https://doi.org/10.1016/j.dsm.2021.08.001 

 

__________________________________________________________________________________________ 
 Anais do XIII SINGEP-CIK – UNINOVE – São Paulo – SP – Brasil – 22 a 24/10/2025 16