---
source_file: "2025-Análise Exploratória de Dados para Previsão da Demanda de Refeições e Redução do Desperdício Alimentar em Instituição de.txt"
original_rel_path: "Trabalhos\Artigos\Aproveitar fortemente\txt\2025-Análise Exploratória de Dados para Previsão da Demanda de Refeições e Redução do Desperdício Alimentar em Instituição de.txt"
category: "Artigos_Aproveitar_fortemente"
extension: ".txt"
sha256: "59c885ab3b751aec6868968488e63b71b041ffed2c5d6e443aa168e5b68ed10e"
extracted_at: "2026-09-19T23:16:59.228254"
---

﻿XX Simpósio dos Programas Profissionais de Pós-Graduação 
Coordenadoria Geral de Pós-Graduação, Extensão e  Pesquisa 

São Paulo/SP – 04, 05 e 06 de novembro de 2025 
 

Programas Profissionais de Pós-Graduação:  
perspectivas e políticas em face das necessidades locais e globais 

  
 
 
Relato Técnico 
 

Análise Exploratória de Dados para Previsão da Demanda de 
Refeições e Redução do Desperdício Alimentar em Instituição de 

Ensino 
 

Michel Silva de Souza 
0009-0003-3951-202X 

 
Dr. Carlos Hideo Arima 

0000-0001-7922-0943 

 
Dr. Rafael Nobre Orsi 

0000-0003-4719-0131 

 
Patrícia Aparecida de Souza 

0009-0004-9445-6080 

 
Resumo 
O desperdício de alimentos é um problema global que compromete a segurança alimentar e a 
sustentabilidade, sendo particularmente crítico em instituições de ensino. Este relato técnico detalha a 
Análise Exploratória de Dados (EDA) que fundamenta o desenvolvimento de um sistema de previsão de 
demanda de refeições com Machine Learning, visando otimizar recursos e reduzir o desperdício. O estudo 
focou em dados históricos de consumo, reservas, cardápios e fatores contextuais, como o clima, em uma 
instituição de ensino. Conforme a metodologia CRISP-ML(Q), a EDA foi uma etapa crucial, envolvendo pré-
processamento de dados brutos, agregação para granularidade diária e a integração de features de cardápio 
vetorizadas com Word2Vec. A análise de padrões temporais revelou tendências sazonais e semanais 
distintas, com picos de demanda nos dias úteis e uma forte correlação entre o número de reservas e as 
refeições efetivamente servidas, validando as reservas como um preditor primário. A distribuição da 
demanda mostrou-se bimodal, distinguindo claramente dias letivos de não letivos. Para aprofundar a análise, 
a série temporal foi submetida a uma decomposição sazonal, comparando-se os modelos aditivo e 
multiplicativo. O modelo multiplicativo apresentou um ajuste superior (MAPE de 12,49%), confirmando que 
a sazonalidade é proporcional à tendência da demanda. Os resultados indicaram a complexidade da série 
e a necessidade de modelos mais avançados, como Random Forest e XGBoost, que possam capturar 
relações não lineares. Este estudo reforça que uma EDA robusta é essencial para subsidiar o 
desenvolvimento de modelos preditivos eficazes, promovendo a sustentabilidade na gestão de recursos 
alimentares em ambientes educacionais.  
 
Palavras-chave: Desperdício de alimentos. Previsão de demanda. Machine learning. Análise 
Exploratória de Dados. Sustentabilidade. 
 
 

Abstract 
Food waste is a global issue that compromises food security and sustainability, being particularly critical in 
educational institutions. This technical report details the Exploratory Data Analysis (EDA) that underpins the 
development of a meal demand forecasting system using Machine Learning, aimed at optimizing resources 
and reducing food waste. The study focused on historical data of consumption, reservations, menus, and 
contextual factors, such as weather, within an educational institution. Following the CRISP-ML(Q) 
methodology, the EDA was a crucial step, involving the preprocessing of raw data, aggregation to daily 
granularity, and the integration of menu features vectorized with Word2Vec. The analysis of temporal 
patterns revealed distinct seasonal and weekly trends, with demand peaking on weekdays and a strong 

   
 



   
 

correlation between reservations and meals actually served, validating reservations as a primary predictor. 
The demand distribution was found to be bimodal, clearly distinguishing between school days and non-school 
days. To deepen the analysis, the time series was subjected to seasonal decomposition, comparing additive 
and multiplicative models. The multiplicative model showed a superior fit (MAPE of 12.49%), confirming that 
seasonality is proportional to the demand trend. The results indicated the complexity of the series and the 
need for more advanced models, such as Random Forest and XGBoost, which can capture non-linear 
relationships. This study reinforces that a robust EDA is essential to support the development of effective 
predictive models, promoting sustainability in food resource management within educational environments.  
 

Keywords: Food waste. Demand forecasting. Machine learning. Exploratory Data Analysis. Sustainability. 
 
 

1 Introdução 

 

O desperdício de alimentos é um problema global, com impactos substanciais na 
segurança alimentar, na sustentabilidade ambiental e na economia mundial (FAO, 2021; 
Gunders, 2012). No Brasil, essa questão é ainda mais crítica, dada a persistência da 
desigualdade social e a insegurança alimentar, o que torna a gestão eficiente dos recursos 
alimentares uma prioridade inadiável. A relação entre vulnerabilidade social e a segurança 
alimentar no país tem sido amplamente documentada (BEZERRA et al., 2024), justificando 
a urgência em otimizar o uso de recursos. Em ambientes institucionais, como escolas e 
universidades, as operações de serviço de alimentação em larga escala são 
particularmente vulneráveis ao desperdício, gerando perdas financeiras e ambientais 
significativas. 

Escolas são identificadas como um setor prioritário para a redução do desperdício 
de alimentos devido à dimensão de suas operações de serviço de alimentação, 
especialmente aquelas que recebem financiamento através de programas como o 
National School Lunch Program nos Estados Unidos (ELNAKIB et al., 2021). O desafio é 
complexo, pois o desperdício ocorre em várias etapas da cadeia de suprimentos, mas 
uma parcela considerável é gerada na fase de consumo, seja em refeições fora de casa 
ou no ambiente doméstico. No contexto educacional, isso se traduz no “plate waste” 
(desperdício no prato), que pode variar amplamente, de 12% a 73,3% dos componentes 
alimentares selecionados, com destaque para vegetais, grãos e frutas (ELNAKIB et al., 
2021). 

A importância de abordar o desperdício de alimentos em instituições de ensino 
abrange aspectos econômicos, ambientais, a formação de hábitos alimentares saudáveis 
e a promoção da educação para a sustentabilidade. A precisão na previsão da demanda 
de refeições contribui para mitigar esse problema, permitindo um planejamento da 
produção e do serviço, e reduzindo o excesso de alimentos preparados e a falta de 
refeições. 

Nesse cenário, a aplicação de técnicas de Machine Learning (ML) emerge como 
uma estratégia promissora para otimizar a gestão alimentar e reduzir o desperdício, 
conforme demonstrado em diversos estudos de previsão de demanda em serviços de 
catering (RODRIGUES et al., 2024; TURKER, 2025). Tais métodos, por serem orientados 
a dados (data-driven), são úteis em extrair relações complexas, identificar padrões e 
tendências, e quantificar o impacto de intervenções no sistema. Essa capacidade analítica 
é imprescindível para a formulação de soluções mais precisas e eficientes, que apoiem o 
desenvolvimento de sistemas de gestão (HU et al., 2024). 

Este relato técnico, que se baseia e expande um trabalho anterior (SOUZA; ORSI, 
2024), tem como objetivo principal detalhar a Análise Exploratória de Dados (EDA) 
realizada sobre os dados de demanda de refeições em uma instituição de ensino. A EDA 
é uma etapa crítica no ciclo de vida de desenvolvimento de modelos de ML, conforme 

   
 



   
 

preconizado por metodologias como CRISP-ML(Q) (IPKOVICH et al., 2024), e é primordial 
para o “entendimento dos dados” e “preparação dos dados” (IPKOVICH et al., 2024). Por 
meio da EDA, o estudo visa não apenas obter a estrutura e as características do dataset, 
mas também identificar variáveis influenciadoras e padrões temporais que subsidiarão o 
desenvolvimento e o aprimoramento de modelos preditivos para a demanda de refeições, 
contribuindo, assim, de forma eficaz para a redução do desperdício alimentar e a 
promoção da sustentabilidade na instituição. 

 
2 Objetivo 

 

Este relato técnico tem como objetivo principal detalhar a Análise Exploratória de 
Dados (EDA) e as etapas de pré-processamento realizadas sobre os dados de consumo 
e reservas de refeições em uma instituição de ensino. Busca-se, através da EDA, 
identificar padrões, tendências e a influência de diversas variáveis contextuais e de 
cardápio na demanda diária de refeições servidas. Os objetivos específicos incluem: 

• Descrever o processo de coleta, validação e tratamento dos dados brutos, 
enfatizando a importância da integridade e consistência para a construção de 
modelos preditivos robustos. 

• Apresentar a metodologia de agregação de dados para a granularidade diária, 
integrando informações transacionais com features de cardápio e dados externos 
(climáticos), conforme a sua relevância para a previsão da demanda. 

• Analisar os padrões temporais da série de demandas de refeições servidas, 
investigando sazonalidades semanais e tendências, e a distribuição das variáveis 
críticas. 

• Identificar as correlações entre a demanda de refeições e variáveis explicativas 
como dia da semana, tipo de ocorrência, atributos do cardápio e condições 
meteorológicas. 

• Subsidiar o desenvolvimento futuro de modelos preditivos de Machine Learning 
mais precisos para a demanda de refeições, contribuindo para a redução do 
desperdício alimentar e a otimização da gestão de recursos na instituição de 
ensino, alinhando-se aos princípios de sustentabilidade e eficiência operacional. 
 

3 Análise do problema e solução proposta 
 

O desperdício alimentar em instituições de ensino transcende a mera perda de 
recursos, configurando-se como um problema com implicações socioeconômicas e 
ambientais significativas. Conforme apontado por pesquisas, grandes volumes de 
desperdício são gerados especificamente na fase de consumo, em serviços de 
alimentação coletiva (KODORS et al., 2022). No contexto de uma instituição de ensino 
brasileira, o problema é agravado pela desigualdade social e pela necessidade de garantir 
o direito à alimentação adequada para todos, conforme evidenciado em estudos anteriores 
(SOUZA; ORSI, 2024). 

A ineficiência no gerenciamento da demanda de refeições gera consequências que 
incluem perdas financeiras decorrentes da aquisição e preparo excessivo de alimentos, 
impactos ambientais relacionados ao descarte de resíduos orgânicos e comprometimento 
das metas institucionais de sustentabilidade (TURKER, 2025). A imprecisão na previsão 
da demanda pode ocasionar tanto o excesso de estoque, resultando em desperdício e 
elevação de custos, quanto a escassez de insumos, afetando a disponibilidade e o 
atendimento aos usuários (CHAUDHARI et al., 2025). Diante desse cenário, o uso de 
métodos de previsão de demanda constitui elemento central do planejamento estratégico. 

   
 



   
 

Este estudo, em continuidade a investigações anteriores, tem como objetivo aprimorar a 
capacidade de previsão da demanda de refeições por meio de uma abordagem de EDA, 
que servirá de base para o desenvolvimento de modelos de ML. A EDA é considerada 
uma etapa primordial em projetos de ciência de dados, permitindo a compreensão das 
características do conjunto de dados, a identificação de relações entre variáveis, a 
detecção de outliers e anomalias, e a preparação dos dados para a modelagem preditiva 
(IPKOVICH et al., 2024). 

A solução proposta se alinha à gestão do ciclo de vida de modelos de ML com 
garantia de qualidade (CRISP-ML(Q)), metodologia que prioriza as fases de 
“entendimento do negócio e dos dados” e “preparação dos dados” (IPKOVICH et al., 
2024). Dada a complexidade da demanda de refeições, que é influenciada por múltiplos 
fatores, a abordagem orientada a dados (data-driven) torna viável a identificação de 
pontos de intervenção eficazes para o planejamento da sustentabilidade (IPKOVICH et 
al., 2024). 

Para isso, é importante não apenas coletar dados de reservas e consumo, mas 
também integrar variáveis adicionais que comprovadamente influenciam a demanda, 
como o histórico de presença dos alunos, previsões climáticas, períodos de provas e o 
calendário escolar (SOUZA; ORSI, 2024). A literatura também reforça que fatores como o 
menu do dia, o número de clientes na semana anterior, as condições climáticas e o dia da 
semana são variáveis-chave na frequência de refeições (HU et al., 2024). Neste trabalho, 
as features de cardápio e os dados climáticos já foram integradas e analisadas como parte 
da construção de um dataset enriquecido. A inclusão desses elementos e uma EDA 
detalhada permite construir uma base de dados robusta, imprescindível para treinar 
modelos de ML capazes de capturar os padrões complexos e as tendências da demanda, 
gerando previsões mais precisas e promovendo, assim, uma redução efetiva do 
desperdício alimentar. 

 
4 Implementação e resultados  
 

A implementação da solução para a redução do desperdício alimentar em 
instituições de ensino requer uma abordagem sistemática que se inicia com a coleta, 
tratamento e análise de dados. Este processo, detalhado a seguir, é essencial para 
fornecer o embasamento necessário ao desenvolvimento de modelos preditivos eficazes. 

 
4.1 Coleta e Validação de Dados 
 

A fase inicial consistiu na coleta de dados detalhados sobre as refeições individuais 
servidas. Os dados brutos foram obtidos a partir de uma planilha eletrônica e incluíam 
informações detalhadas por aluno e por refeição, como data; código do aluno; tipo de 
refeição; reserva; servida; e consumo; além de variáveis contextuais como dia do ano; 
mês do ano; dia da semana; status letivo; tipo de ocorrência; e dados meteorológicos 
(temperatura média; temperatura máxima; temperatura mínima; soma de chuva; e 
velocidade máxima do vento). 

A verificação e o tratamento dos dados foram etapas de alta importância, com a 
aplicação de checagens de estrutura e regras definidas para assegurar a consistência do 
dataset. Foi confirmada a presença de todas as colunas necessárias e a correta 
formatação da coluna de data. Adicionalmente, verificou-se que as colunas de data; 
consumo; refeições servidas; e reserva estavam completas e não continham valores 
negativos. Um procedimento de alerta foi implementado para identificar casos em que o 
número de refeições servidas superava o de reservadas, indicando potenciais 

   
 



   
 

inconsistências que requerem análise (SOUZA; ORSI, 2024). A garantia da qualidade dos 
dados é condição indispensável para o treinamento eficaz de modelos de ML, pois a baixa 
qualidade dos dados é um obstáculo significativo ao processo preditivo (KANWAL et al., 
2025). 

Adicionalmente, um arquivo separado contendo variáveis de cardápio (features) foi 
carregado e validado. Este arquivo foi gerado a partir de informações de menu não 
estruturadas, que foram pré-processadas em vetores numéricos, utilizando técnicas de 
Word2Vec (HU et al., 2024). A junção dessas features de cardápio com o DataFrame 
principal foi realizada utilizando a coluna de data como chave. Foi verificada a unicidade 
das datas e eventuais valores nulos nas features foram preenchidos com zero, garantindo 
a prontidão de todas as informações para análises posteriores. 
 
4.2 Agregação e Pré-processamento dos Dados Diários 
 

Após a validação e junção, os dados por aluno e por refeição foram agregados para 
a granularidade diária. Esta etapa transformou cada registro individual em uma única 
observação diária com métricas sumarizadas. As regras de agregação incluíram a soma 
total de refeições servidas, reservas totais e consumo total, a contagem de alunos únicos 
por dia e turmas únicas por dia, e o primeiro valor de variáveis como status letivo; tipo de 
ocorrência; dia do ano; mês do ano; dia da semana; e as variáveis meteorológicas. As 
features de cardápio, representando os pratos servidos, foram mantidas com o primeiro 
valor do dia (first) e convertidas para o tipo inteiro. 

Uma regra de negócio primordial aplicada nesta fase foi a correção das reservas e 
servidas para dias de feriado. Dias identificados com tipo de ocorrência = 9 (feriado) 
tiveram seus valores de reservas totais e refeições servidas totais zerados, sob a premissa 
de que não há demanda real de refeições nesses dias. Esta correção é imprescindível 
para evitar a contaminação do histórico de demanda com valores irreais e garantir a 
precisão dos modelos preditivos. 

Em seguida, os dados agregados foram separados em df_historico e df_predicao. 
O df_historico contém os dados até a última data com refeições servidas totais > 0, 
representando a demanda observada. O df_predicao inclui as datas subsequentes, 
destinadas à previsão. Uma nova feature, flag baixa demanda, foi criada no df_historico 
para identificar dias em que refeições servidas totais foi menor ou igual a um limiar de 10, 
o que se mostra útil para análises específicas de eventos de baixa demanda. A natureza 
interativa e exploratória da gestão do ciclo de vida do modelo justifica a EDA como uma 
etapa contínua e essencial no processo de pesquisa (IPKOVICH et al., 2024). 

 
4.3 Análise Exploratória de Dados (EDA) 
 

A EDA foi realizada sobre o df_historico e o base_dados (df_historico + 
df_predicao) para compreender os padrões da demanda de refeições servidas. 

A série temporal de refeições servidas totais e reservas totais foi plotada para 
visualizar a evolução da demanda ao longo do tempo. A figura 1 permitiu identificar 
visualmente tendências, picos e vales na demanda, assim como a forte relação entre 
reservas e refeições servidas. A inclusão da feature flag baixa demanda no gráfico 
também auxiliou na identificação de dias com demanda atipicamente baixa. Esta 
visualização inicial é imprescindível para se entender a dinâmica da demanda e preparar 
o terreno para análises mais aprofundadas. 

 
 

   
 



   
 

 
Figura 1 Histórico de Demanda e Reservas Totais de Refeições Servidas ao Longo do Tempo 

  
Fonte: Elaboração própria dos autores (2025). 

 
O gráfico demonstra a sazonalidade semanal da demanda (picos e vales 

recorrentes). A Servidas Total (linha contínua azul) e as Reservas Totais (linha pontilhada 
verde) apresentam forte correlação visual, validando o uso de reservas como preditor 
primário. As “reservas” tendem a ser consistentemente maiores que as “servidas”, 
indicando o volume de não-comparecimento (no-show), que é a principal fonte de 
desperdício a ser modelada. 

 
4.3.1 Padrões Semanais e Distribuição 

 
Para identificar a sazonalidade intrínseca aos dias de operação, a demanda de 

refeições servidas foi analisada por dia da semana. 
O gráfico de barras da Figura 2 exibe a média de refeições servidas por dia da 

semana, indicando variações significativas. Os dias úteis (Segunda a Sexta-feira) 
concentram as maiores demandas, com picos notáveis na Segunda e Quarta-feira. 

 
Figura 2 Análise dos Padrões de Demanda por Dia da Semana (Média) 

  
Fonte: Elaboração própria dos autores (2025). 

   
 



   
 

O gráfico demonstra que a demanda média é mais alta no início da semana. A 
importância do dia da semana como um preditor forte da demanda é um achado 
consistente com a literatura de previsão em catering (MALEFORS et al., 2022). 

A distribuição dos dados por dia da semana (Figura 3 - Boxplot) complementa a 
análise anterior, confirmando a alta variabilidade da demanda para cada dia útil. 

 
Figura 3 Análise dos Padrões de Demanda por Dia da Semana (Distribuição) 

  
Fonte: Elaboração própria dos autores (2025). 

 
O boxplot confirma a grande dispersão dos valores de demanda (variabilidade) nos 

dias úteis e evidencia a presença de outliers (círculos) em alguns dias. Essa variabilidade 
reforça a necessidade de modelos preditivos que consigam capturar a sazonalidade 
semanal de forma precisa. 

A evolução temporal da série (Figura 4) permitiu uma visualização da tendência 
geral e das oscilações da demanda ao longo do período analisado (Fevereiro a Junho de 
2025). As quedas recorrentes e abruptas para zero ou valores próximos, especialmente 
nos fins de semana e feriados, reforçam o impacto dos fatores contextuais no consumo. 

 
Figura 4 Evolução Temporal da Demanda de Refeições Servidas 

  
Fonte: Elaboração própria dos autores (2025). 

   
 



   
 

O gráfico demonstra a recorrência de picos e vales (sazonalidade) que refletem o 
padrão semanal de demanda, interrompido por períodos de recesso (Junho) e dias de 
demanda zero, o que sublinha a importância de modelar o tempo e os eventos 
acadêmicos. 

Além disso, a distribuição de frequência dos valores (Figura 5 - Histograma) 
demonstrou que a demanda se concentra em dois picos principais, o que reflete a clara 
separação entre os dias de operação normal e os dias sem demanda, sendo um dado 
importante para a escolha de modelos de previsão. 

 
Figura 5 Distribuição de Frequência da Demanda de Refeições Servidas 

  
Fonte: Elaboração própria dos autores (2025). 

 
O histograma revela a natureza bimodal da demanda, com um pico em valores 

próximos a zero (anterior à filtragem) e um segundo pico na faixa de 100 a 160 refeições. 
Essa característica bimodal indica a presença de dois regimes de demanda distintos (dias 
letivos vs. não letivos) que os modelos de Machine Learning precisarão aprender a 
diferenciar. 

 
4.3.2 Decomposição da Série Temporal 

 
Para analisar os componentes estruturais da demanda com maior profundidade, a 

série temporal de refeições servidas totais (após a filtragem de demanda zero) foi 
submetida à decomposição sazonal. A identificação de variáveis-chave, como o dia da 
semana, e a análise de suas interações constitui um aspecto central da EDA, sendo 
primordial para o desenvolvimento de modelos de ML eficazes (HU et al., 2024). A série 
temporal foi submetida à decomposição sazonal utilizando os modelos aditivo e 
multiplicativo. 

O primeiro passo foi a aplicação do Modelo Aditivo (Figura 6), que resultou em um 
R² de 60% e um MAPE (Erro Percentual Médio) de 12,44%. Embora essas métricas 
iniciais sugiram um ajuste razoável, uma análise mais aprofundada dos resíduos, 
detalhada posteriormente, indicou que o modelo não capturava adequadamente toda a 
estrutura da série temporal. 

 
 
 
 

   
 



   
 

Figura 6 Decomposição da Série Temporal de Refeições Servidas Totais (Modelo Aditivo) 

  
Fonte: Elaboração própria dos autores (2025). 

 
A Figura 6 separa a série original (gráfico superior) em seus componentes. A 

Tendência (linha amarela) mostra a evolução suave da demanda, e a Sazonalidade (linha 
verde) exibe o padrão semanal constante. Os Resíduos (linha azul) mostram a variância 
não explicada, que, no modelo aditivo, é alta, como indicado pelo desvio padrão de 17.18. 

Em seguida, explorou-se o Modelo Multiplicativo (Figura 7), que obteve um R2 de 
59% e um MAPE (Erro Percentual Médio) de 12.49%, demonstrando um ajuste superior 
em comparação ao modelo aditivo. 

 
Figura 7 Decomposição da Série Temporal de Refeições Servidas Totais (Modelo Multiplicativo) 

  
Fonte: Elaboração própria dos autores (2025). 

   
 



   
 

Na Figura 7, a Sazonalidade (fator - linha verde) oscila em torno da média 1.0, 
indicando a proporcionalidade da variação semanal em relação à tendência. A dispersão 
dos Resíduos (gráfico inferior) é significativamente mais estreita, com desvio padrão de 
15%, confirmando que a sazonalidade e a tendência capturam melhor a variância da série 
do que o modelo aditivo.. 

 
Figura 8 Comparação de Métricas de Decomposição (Modelos Aditivo e Multiplicativo) 

  
Fonte: Elaboração própria dos autores (2025). 

 
A Figura 8 apresenta a comparação visual da Sazonalidade e dos Resíduos de 

ambos os modelos, confirmando que, na série filtrada, eles performam de maneira similar, 
validando a premissa de que a abordagem de previsão deve lidar com a sazonalidade 
como um fator proporcional à demanda média. Essa conclusão reforça a necessidade de 
explorar modelos de ML mais sofisticados, como Random Forest e Gradient Boosting, 
capazes de capturar tanto a sazonalidade quanto as relações não lineares complexas 
entre as variáveis (TURKER, 2025). 

 
4.3.3 Análise de Resíduos - Modelo Aditivo 

 
A análise dos resíduos é uma etapa crítica para avaliar a qualidade e a adequação 

do modelo de decomposição escolhido. O estudo prosseguiu com a inspeção detalhada 
dos resíduos gerados pelo Modelo Aditivo, buscando validar a suposição de que o modelo 
eliminou a estrutura da série temporal, deixando apenas ruído branco. 
 

 
 
 
 
 
 
 
 
 
 

   
 



   
 

Figura 9 Série Temporal dos Resíduos (Aditivo) 

  
Fonte: Elaboração própria dos autores (2025). 

 
A Série Temporal dos Resíduos do Modelo Aditivo (Figura 9) ilustra a variância não 

explicada pelo modelo. Visualmente, esta série apresenta flutuações amplas e 
descontroladas, com um desvio padrão de 17.18, confirmando que o modelo aditivo não 
conseguiu capturar adequadamente toda a complexidade da estrutura da demanda. 

 
Figura 10 Histograma dos Resíduos (Aditivo) 

  
Fonte: Elaboração própria dos autores (2025). 

 
O Histograma dos Resíduos (Figura 10) exibe a distribuição de frequência dos 

erros. Embora o centro da distribuição se localize próximo a zero, indicando que o modelo 
não possui viés significativo, a dispersão é ampla, refletindo a grande variabilidade dos 
erros de previsão. 

 
 
 
 
 
 

   
 



   
 

Figura 11 Q-Q Plot (Normalidade - Aditivo) 

  
Fonte: Elaboração própria dos autores (2025). 

 
O Q-Q Plot (Figura 11) é uma ferramenta para verificar se os resíduos seguem uma 

distribuição normal. A análise mostrou que, embora a hipótese de normalidade não tenha 
sido estritamente rejeitada, as extremidades (outliers) se desviam da linha reta, sugerindo 
que a adequação à suposição de normalidade não é perfeita. 

 
Figura 12 Autocorrelação dos Resíduos (Aditivo) 

  
Fonte: Elaboração própria dos autores (2025). 

 
Ainda sobre a análise de resíduos do modelo aditivo, o gráfico de Autocorrelação 

dos Resíduos (Figura 12) indica a presença de autocorrelação nos primeiros lags (valores 
fora das linhas tracejadas de intervalo de confiança). Esta autocorrelação remanescente 
é uma evidência de que a estrutura da série não foi totalmente capturada pelo modelo 
aditivo, indicando a necessidade de uma abordagem alternativa (MONTGOMERY et al., 
2021). 

 
 

   
 



   
 

4.3.4 Análise de Resíduos - Modelo Multiplicativo 
 
A análise dos resíduos do Modelo Multiplicativo demonstrou um ajuste superior 

para a série de demanda. 
 

Figura 13 Série Temporal dos Resíduos (Multiplicativo) 

  
Fonte: Elaboração própria dos autores (2025). 

 
A Série Temporal dos Resíduos do Modelo Multiplicativo (Figura 13) exibe 

flutuações visivelmente mais estreitas, com um desvio padrão de 15%. Essa redução 
significativa na dispersão da variância não explicada comprova que o modelo multiplicativo 
foi mais eficaz ao modelar a sazonalidade como um fator proporcional à tendência da 
demanda. 

 
Figura 14 Histograma dos Resíduos (Multiplicativo) 

  
Fonte: Elaboração própria dos autores (2025). 

 
O Histograma dos Resíduos (Figura 14) apresenta uma distribuição mais 

concentrada em torno do valor 1.0 (o resíduo em um modelo multiplicativo é um fator, e 
não um erro aditivo próximo a zero). Esta concentração reforça o melhor ajuste do modelo. 

   
 



   
 

Figura 15 Q-Q Plot (Normalidade - Multiplicativo) 

  
Fonte: Elaboração própria dos autores (2025). 

 
O Q-Q Plot (Figura 15) mostra que os pontos se alinham de maneira ainda mais 

coesa à linha reta, confirmando que os resíduos do modelo multiplicativo estão bem 
próximos de uma distribuição normal. 

 
Figura 16 Autocorrelação dos Resíduos (Multiplicativo) 

  
Fonte: Elaboração própria dos autores (2025). 

 
O gráfico de Autocorrelação dos Resíduos (Figura 16) do modelo multiplicativo é o 

mais importante para validar o ajuste: a maioria dos lags permanece dentro das faixas de 
confiança, indicando que o padrão de resíduos se aproxima muito mais do ruído branco 
do que no modelo aditivo. Essa validação reforça a conclusão de que a escolha do modelo 
multiplicativo foi mais apropriada para a complexidade desta série temporal de demanda, 
justificando o foco em modelos mais avançados de Machine Learning para as próximas 
etapas (TURKER, 2025). 

 
 
 

   
 



   
 

5 Lições aprendidas 

 
A execução da EDA e das etapas de pré-processamento para a previsão da 

demanda de refeições em uma instituição de ensino gerou lições valiosas para o 
aprimoramento contínuo deste projeto e para futuras iniciativas na área de 
sustentabilidade e ML. 

1. A Qualidade e Integridade dos Dados são Inegociáveis: A validação rigorosa 
dos dados brutos, incluindo a verificação de estrutura, tipos e regras de negócio, 
destacou a importância de um dataset limpo e consistente. Problemas como 
valores nulos em colunas críticas ou inconsistências entre refeições servidas e 
reservadas podem comprometer seriamente a acurácia dos modelos preditivos. A 
experiência reforça a premissa de que a eficácia da Inteligência Artificial (IA) 
depende da disponibilidade de grandes volumes de dados de alta qualidade 
(KANWAL et al., 2025). A gestão de dados é imprescindível, especialmente diante 
do crescente volume de informações (HU et al., 2024). 

2. A Agregação e Enriquecimento de Dados Ampliam o Poder Preditivo: A 
agregação dos dados para granularidade diária e a integração de features de 
cardápio e informações meteorológicas foram passos decisivos. A literatura 
corrobora que a inclusão de variáveis adicionais, como o histórico de presenças de 
alunos, previsões climáticas, períodos de provas e calendário escolar, é essencial 
para aprimorar a precisão das previsões de demanda (SOUZA; ORSI, 2024; 
RODRIGUES et al., 2024). A capacidade de extrair e gerar variáveis não 
diretamente relacionadas ao serviço de alimentação (como dia da semana, mês, 
feriados, temperatura e precipitação) provou ser um diferencial. 

3. Sazonalidade e Padrões Semanais são Predominantes: A análise de padrões 
semanais, com picos de demanda em dias úteis e quedas em feriados ou fins de 
semana, demonstrou a forte sazonalidade dos dados. O dia da semana emergiu 
como um dos fatores mais importantes para a acurácia da previsão (MALEFORS 
et al., 2022), reforçando a necessidade de considerar esses padrões no 
desenvolvimento de modelos. 

4. A Decomposição Sazonal Exige uma Escolha Crítica do Modelo: A EDA inicial 
forneceu insights valiosos, mas a performance modesta do modelo aditivo (R² de 
60%) ressaltou a complexidade da série. A comparação entre os modelos foi 
crucial: embora o MAPE do modelo multiplicativo (12,49%) tenha sido 
marginalmente superior ao do aditivo (12,44%), a sua escolha se validou pela 
drástica redução na variância dos resíduos. Isso demonstrou que a abordagem 
multiplicativa captura a natureza da sazonalidade proporcional de forma muito mais 
eficaz, sendo determinante para o desenvolvimento de modelos de ML mais 
sofisticados e precisos para cenários dinâmicos. 

5. A Necessidade de um Olhar Multivariado na EDA: A correlação entre variáveis, 
como reservas e taxa de consumo, é um indicativo da complexidade da demanda. 
Estudos mostram que fatores como a variedade do menu, contagens, receita, 
mobilidade no campus e temperatura influenciam efetivamente as preferências 
alimentares (TURKER, 2025). A EDA é uma ferramenta poderosa para visualizar 
essas relações e subsidiar a seleção de features mais relevantes para os modelos 
de ML, abordando os desafios de problemas de otimização multiobjetivo (HU et al., 
2024). 

6. Desafios na Coleta de Dados e Generalização: A experiência com restrições de 
dados, como as enfrentadas durante a COVID-19 em estudos semelhantes 
(KODORS et al., 2022), ou a dependência de amostras limitadas (BYKER SHANKS 

   
 



   
 

et al., 2023), destaca a importância de estratégias robustas de coleta e a cautela 
na generalização dos resultados. A necessidade de grandes conjuntos de dados 
rotulados é um desafio chave para o ML, com o risco de overfitting em amostras 
pequenas (WILLIAMS et al., 2025). 
Em suma, a EDA é uma etapa exploratória e iterativa (IPKOVICH et al., 2024) que 

não apenas revelou padrões importantes na demanda de refeições, mas também 
sublinhou a necessidade de aprimorar a coleta e o enriquecimento de dados e de explorar 
modelos de ML mais avançados para construir um sistema de previsão mais preciso e 
robusto. As lições aprendidas apontam para a importância de uma abordagem holística, 
que combine técnicas de análise de dados com o conhecimento do domínio para enfrentar 
o complexo problema do desperdício alimentar. 
 
6 Considerações finais 
 

O presente relato técnico aprofundou-se na EDA como um pilar essencial para o 
desenvolvimento de um sistema de previsão da demanda de refeições em uma instituição 
de ensino, visando a mitigação do desperdício alimentar e a promoção da 
sustentabilidade. A problemática do desperdício, reconhecida globalmente e amplificada 
em contextos educacionais, exige soluções inovadoras e baseadas em dados para 
otimizar a gestão de recursos e garantir a segurança alimentar. 

A implementação da EDA, desde a validação e o pré-processamento dos dados 
brutos até a análise de padrões temporais e correlações, revelou muitos insights. A 
integração de features de cardápio e informações meteorológicas, bem como a correção 
de dados para dias de feriado, demonstrou a importância de um dataset enriquecido e de 
alta qualidade para qualquer esforço de modelagem preditiva. A robustez da gestão de 
dados é primordial, especialmente no cenário de explosão informacional (HU et al., 2024). 

Os resultados da EDA confirmaram a forte sazonalidade semanal da demanda de 
refeições, com o dia da semana emergindo como um preditor significativo. A comparação 
entre modelos de decomposição sazonal demonstrou a complexidade da série, mas 
validou uma abordagem que lida com a sazonalidade como um fator proporcional à 
demanda média. Essa conclusão reforça a necessidade de empregar técnicas de ML mais 
avançadas, como Random Forest ou XGBoost, capazes de capturar relações não lineares 
e múltiplos fatores influenciadores, superando métodos convencionais (WICAKSONO et 
al., 2025; CHAUDHARI et al., 2025). 

As lições aprendidas neste estudo enfatizam que a precisão das previsões de 
demanda é diretamente proporcional à qualidade, integridade e diversidade das variáveis 
incluídas na análise. Fatores como a variedade do menu, condições climáticas, eventos 
no campus e o histórico de reservas e consumo são elementos críticos para aprimorar a 
acurácia dos modelos (SOUZA; ORSI, 2024; TURKER, 2025). A contínua busca por 
aprimoramentos e o investimento em tecnologias e ferramentas que promovam uma 
gestão de recursos mais responsável e sustentável são imprescindíveis para transformar 
os desafios do desperdício alimentar em oportunidades para um ambiente educacional 
mais eficiente e equitativo. 

Por fim, este trabalho reforça o papel da EDA como um processo contínuo e 
iterativo que fornece a inteligência necessária para o desenvolvimento de soluções 
baseadas em ML. A exploração de variáveis contextuais, comportamentais e 
sociodemográficas, conforme sugerido pela literatura (LONSKA et al., 2025; STACCHINI 
et al., 2024), representa o próximo passo para construir modelos preditivos de demanda 
mais robustos e explicáveis. Ao integrar a inteligência humana com a capacidade analítica 

   
 



   
 

da máquina, torna-se possível otimizar a gestão alimentar, reduzir o desperdício e 
caminhar em direção a um futuro mais sustentável nas instituições de ensino. 

 

Referências 
 

BEZERRA, M. S. et al. Insegurança alimentar e nutricional no Brasil e sua correlação 
com indicadores de vulnerabilidade. Revista Ciência & Saúde Coletiva, 2024. 
Disponível em: https://www.scielo.br/j/csc/a/vpGZNFNcKySWVrVy4KR3Gtc/. Acesso em: 
20 set. 2025. 
 
BYKER SHANKS, C. et al. School Lunch Advisory Councils' use of behavioural 
economics influences vegetable selection and waste. Health Education Journal, v. 82, 
2023. 
 
CHAUDHARI, M. A. et al. Forecasting and Modelling of Food Demand Supply Chain 
using Machine Learning. International Journal of Innovative Research in Multidisciplinary 
Portable Systems (IJIRMPS), v. 13, 2025. 
 
ELNAKIB, S. A. et al. Food Waste in Schools: A Pre-/Post-Test Study Design 
Examining the Impact of a Food Service Training Intervention to Reduce Food 
Waste. International Journal of Environmental Research and Public Health, v. 18, 2021. 
 
FAO. (2021). Food waste Index Report. Roma: FAO. Disponível em: 
https://www.unep.org/resources/report/unep-food-waste-index-report-2021. Acesso em: 
15 set. 2025. 
 
GUNDERS, D. Waste Free Kitchen Handbook: A Guide to Reducing Food Waste, 
Saving Money, and Eating Better. New York: Ten Speed Press, 2012. 
 
HU, J. et al. Design of information management model based on multiobjective 
optimization algorithm in intelligent electric financial system. PeerJ Computer 
Science, v. 10, 2024. 
 
IPKOVICH, Á. et al. Network science and explainable AI-based life cycle management 
of sustainability models. PLoS ONE, v. 19, 2024. 
 
KANWAL, N. et al. Revolutionizing food safety in the airline industry: AI-powered 
smart solutions. Trends in Food Science & Technology, v. 159, 2025. 
 
KODORS, S. et al. Plate Waste Forecasting Using the Monte Carlo Method for 
Effective Decision Making in Latvian Schools. Nutrients, v. 14, 2022. 
 
LONSKA, J. et al. Reducing Plate Waste in Latvian Schools: Evaluating Interventions 
to Promote Sustainable Food Consumption Practices. Foods, v. 14, 2025. 
 
MALEFORS, C. et al. Food waste reduction and economic savings in times of crisis: 
The potential of machine learning methods to plan guest attendance in Swedish 
public catering during the Covid-19 pandemic. Socio-Economic Planning Sciences, v. 
82, 2022. 
 

   
 



   
 

MONTGOMERY, D. C.; PECK, E. A.; VINING, G. Introduction to Linear Regression 
Analysis. New York: Wiley, 2021. 
 
RODRIGUES, M. et al. Machine learning models for short-term demand forecasting 
in food catering services: A solution to reduce food waste. Journal of Cleaner 
Production, v. 435, 2024. 
 
SOUZA, M. S.; ORSI, R. N. Sustentabilidade na Mesa: redução do desperdício 
alimentar em uma instituição de ensino com previsão de demanda por aprendizado 
de máquina. Revista H-Tec Humanidades e Tecnologia, v. 11, 2024, Ed. Especial XIX 
SIMPROFI. 
 
STACCHINI, L. et al. Association Between Socio-Demographic Characteristics and 
Household Food Waste Behaviors Among University Students in Italy: The 
UniFoodWaste Study. Sustainability, v. 16, 2024. 
 
TURKER, G. F. Reducing Food Waste in Campus Dining: A Data-Driven Approach to 
Demand Prediction and Sustainability. Sustainability, v. 17, 2025. 
 
WICAKSONO, T. et al. Customer-centric circular economy as-a-service decision-
making: Machine learning-driven open innovation in food service. Cleaner 
Environmental Systems, v. 18, 2025. 
 
WILLIAMS, L. et al. Measuring the Level of Aflatoxin Infection in Pistachio Nuts by 
Applying Machine Learning Techniques to Hyperspectral Images. Sensors, v. 25, 
2025.