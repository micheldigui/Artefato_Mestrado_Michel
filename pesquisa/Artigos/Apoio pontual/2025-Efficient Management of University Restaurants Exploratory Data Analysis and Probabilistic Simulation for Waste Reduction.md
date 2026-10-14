---
source_file: "2025-Efficient Management of University Restaurants Exploratory Data Analysis and Probabilistic Simulation for Waste Reduction.txt"
original_rel_path: "Trabalhos\Artigos\Apoio pontual\txt\2025-Efficient Management of University Restaurants Exploratory Data Analysis and Probabilistic Simulation for Waste Reduction.txt"
category: "Artigos_Apoio_pontual"
extension: ".txt"
sha256: "036a0e1441977ee2a387dd7ca4e379ed3b375cd922bd1ea9e6c5219d9082e85e"
extracted_at: "2026-09-20T00:05:05.679042"
---

﻿CENTRO ESTADUAL DE EDUCAÇÃO 
TECNOLÓGICA PAULA SOUZA​

UNIDADE DE PÓS-GRADUAÇÃO, EXTENSÃO E 
PESQUISA 

PROGRAMA DE MESTRADO PROFISSIONAL EM GESTÃO 
E TECNOLOGIA EM SISTEMAS PRODUTIVOS 

 

 

PROJETO DA PESQUISA EXPERIMENTAL 

Gestão Eficiente de Restaurantes Universitários: Análise 
Exploratória de Dados e Simulação Probabilística para Redução de 

Desperdícios 

 
Projeto da Pesquisa Experimental da 
disciplina de MQA. 
Michel Silva de Souza 
Julyana Nazario Alves 
Vinicius de Oliveira Querencia 

 
 

 

 

 

 

São Paulo 
11/2025 

 
 



 
 

SUMÁRIO 
1. INTRODUÇÃO​ 4 
2. OBJETIVOS​ 5 

2.1 Objetivo geral​ 5 
2.2 Objetivos específicos​ 5 

3. REFERENCIAL TEÓRICO E TRABALHOS CORRELATOS​ 6 
4. MÉTODO DE PESQUISA​ 6 

4.1 Tipo e Desenho da Pesquisa​ 7 
4.2 População e Amostra​ 7 
4.3 Material e Ambiente do Experimento​ 8 
4.4 Procedimentos de Coleta e Tratamento de Dados​ 8 
4.5 Análise de Dados​ 15 
4.6 Aspectos Éticos e Riscos Associados​ 15 

5 CRONOGRAMA​ 4 
6. ATIVIDADES REALIZADAS​ 4 

6.1 Coleta e Preparação da Base de Dados​ 4 
6.2 Análise Exploratória e Modelagem Empírica​ 4 
6.3 Estruturação e Execução do Modelo de Simulação​ 4 
6.4 Coleta e Análise dos Resultados da Simulação​ 5 

7. RESULTADOS​ 5 
8. CONCLUSÕES​ 10 

8.1. Limitações, Riscos Metodológicos e Vieses Potenciais​ 10 
8.1.1 Limitações Gerais​ 10 
8.1.2 Riscos Metodológicos e de Interpretação​ 11 

8.2. Implicações Práticas e Próximos Passos​ 11 
REFERÊNCIAS BIBLIOGRÁFICAS​ 13 

 

 
 



4 
 

 

1.​ INTRODUÇÃO 
A gestão da demanda em refeitórios institucionais, particularmente em 

restaurantes universitários, configura-se como um desafio operacional e estratégico 
de alta complexidade. Esses ambientes servem diariamente a uma população vasta 
e diversificada, composta por estudantes, docentes e servidores, frequentemente 
atuando como a principal fonte de alimentação acessível para estudantes em 
situação de vulnerabilidade socioeconômica (PAYNE-STURGES et al., 2017; 
LOOFBOURROW, 2023). A garantia de refeições regulares e nutricionalmente 
adequadas transcende o escopo assistencial, tornando-se um pilar fundamental das 
políticas de equidade e inclusão no ensino superior. 

Contudo, o planejamento da produção nesses refeitórios é um processo 
complexo e muitas vezes reativo. A volatilidade das reservas, caracterizada por 
"no-shows" (estudantes que reservam e não comparecem) e "walk-ins" (usuários 
que consomem sem reserva prévia), gera dois problemas centrais: o desperdício de 
alimentos devido à superprodução e a insatisfação dos usuários em caso de 
escassez. Do ponto de vista institucional, o desperdício representa perda econômica 
e impacto ambiental, onerando a sustentabilidade financeira das universidades 
(CBORD, 2025; REFED, 2016), enquanto a escassez pode comprometer a 
permanência estudantil. Falhas na previsão de demanda e na coordenação de 
processos logísticos são apontadas como principais fontes de ineficiência em 
sistemas de refeições coletivas (AKKERMAN, 2024). 

A resolução desse desafio exige abordagens que lidem com a incerteza da 
demanda e a ineficiência operacional. Para aprimorar este cenário, será explorada a 
simulação probabilística, amplamente aplicada em contextos de planejamento 
estratégico para explorar cenários sob incerteza e quantificar riscos (SHEEL, 1995; 
CHOI, 2022). A adoção conjunta da análise exploratória de dados e da simulação 
probabilística permite projetar os impactos de diferentes políticas de produção, 
oferecendo subsídios para decisões baseadas em evidências. 

A hipótese central deste estudo é que a implementação integrada de análise 
exploratória de séries temporais para identificação de padrões de demanda e 
simulação probabilística para modelagem de cenários sob incerteza pode resultar 
 

 



 
 

em uma redução percentual significativa do desperdício de alimentos (superior a 
10%) em refeitórios institucionais, em comparação com os métodos de planejamento 
reativos atuais. 

2.​ OBJETIVOS 
2.1​Objetivo geral 

Compreender, mapear e simular os processos de reservas e consumo, 
identificando gargalos e propondo melhorias operacionais para refeitórios 
institucionais sob diferentes cenários de incerteza, integrando análise exploratória de 
dados e simulação de cenários, visando reduzir desperdícios de alimentos, otimizar 
a eficiência operacional e promover a sustentabilidade. 

 

2.2​Objetivos específicos  

●​ Analisar e modelar o padrão de demanda histórica de refeições em refeitórios 
institucionais, identificando e quantificando sazonalidades (ex: semanal) e 
tendências, utilizando técnicas de análise exploratória de dados e 
decomposição de séries temporais para compreender o impacto das variáveis 
e os dias de maior/menor consumo. 

●​ Mapear os fluxos reais do processo de reservas e consumo de refeições, bem 
como as interações com a aquisição de insumos identificando desvios (ex.: 
reservas feitas, mas não consumidas; consumo sem reserva), gargalos e 
padrões de "no-show" em relação aos fluxos prescritos. 

●​ Desenvolver um modelo de simulação para testar cenários alternativos de 
planejamento de produção e políticas de gestão de reservas (ex: redução do 
tempo entre reserva e preparo, ajuste da produção com base em atributos de 
cardápio, e implementação de políticas de incentivo/penalidade para 
"no-show"), avaliando seu impacto na redução do desperdício e na eficiência 
operacional. 

●​ Propor diretrizes e um plano de ação detalhado para a implementação das 
melhorias identificadas na gestão da cadeia de suprimentos do refeitório, com 
foco na escalabilidade e reprodutibilidade. 

 



 
 

3.​ REFERENCIAL TEÓRICO E TRABALHOS CORRELATOS 
A literatura sobre gestão de serviços de alimentação e previsão de demanda 

tem evoluído significativamente, incorporando métodos quantitativos e 
computacionais para otimização de processos. A simulação probabilística, em 
particular a Simulação de Monte Carlo, tem sido amplamente utilizada para modelar 
sistemas complexos sob incerteza, permitindo a avaliação de riscos e a projeção de 
resultados em diferentes cenários (SHEEL, 1995; CHOI, 2022). No contexto de 
restaurantes, a aplicação dessas técnicas visa aprimorar a tomada de decisão, 
especialmente no que tange à gestão de estoques e à produção, minimizando 
perdas e maximizando a satisfação do cliente. 

Estudos recentes têm explorado o uso de Machine Learning e Inteligência 
Artificial para aprimorar a previsão de demanda em diversos setores, incluindo o 
alimentício (CHAUDHARI et al., 2025; OLAWALE et al., 2025). A capacidade de 
processar grandes volumes de dados e identificar padrões complexos torna essas 
abordagens valiosas para lidar com a variabilidade inerente à demanda de refeições. 
A engenharia de features, que envolve a criação de novas variáveis a partir de 
dados existentes, é um componente crucial para o sucesso desses modelos, 
permitindo capturar sazonalidades, tendências e o impacto de eventos externos 
(RAJENDRAN et al., 2025). 

A problemática do desperdício de alimentos em instituições de ensino 
superior é um tema de crescente preocupação, com implicações econômicas, 
sociais e ambientais (CBORD, 2025; REFED, 2016). A ineficiência na gestão da 
demanda, exacerbada por fenômenos como "no-show" e "walk-in", contribui 
significativamente para esse problema (AKKERMAN, 2024). A integração de 
análises preditivas e simulações oferece um caminho promissor para mitigar esses 
desafios, permitindo que as instituições desenvolvam políticas de produção mais 
eficazes e sustentáveis. 

 
4.​ MÉTODO DE PESQUISA 

A presente pesquisa adota uma abordagem quantitativa, com desenho 
descritivo e exploratório, focando na análise exploratória de dados e na simulação 
probabilística para otimização da gestão de refeições em refeitórios universitários. 



 
 

4.1 Tipo e Desenho da Pesquisa 

A pesquisa é de natureza quantitativa. O estudo adota um desenho descritivo 
e exploratório. A fase descritiva busca caracterizar os padrões históricos de 
consumo e reservas de refeições no refeitório institucional, enquanto a fase 
exploratória, por sua vez, utiliza a simulação probabilística para testar cenários 
alternativos de planejamento e políticas operacionais, oferecendo evidências 
empíricas para a tomada de decisão gerencial. A Tabela 1 resume as fases da 
análise, seus procedimentos e os objetivos específicos correspondentes. 

Tabela 1 - Fases da Análise e Relação com os Objetivos 

Fases da 
análise Procedimento Objetivo (Conforme 

item 2.2) 

Modelos Preditivos e Feature Selection: 
Desenvolver modelos preditivos (Treatment) (ex: 

Modelagem da SARIMA, Regressão Linear Múltipla) utilizando a 
Demanda Sazonalidade de 5 dias e as features de cardápio Refinamento da 
(Objetivo e clima como Variáveis Independentes (X). O modelagem do 

Específico 1 e 2) foco é maximizar a precisão (R², MAPE) da padrão de demanda. 
previsão de demanda (Y) para a próxima 

semana (df_predicao). 

Construção do Modelo de Simulação com as 
distribuições probabilísticas (extraídas da EDA) 

Simulação para modelar o refeitório. Teste de Cenários 
(Objetivo (Treatments): Comparar o cenário atual (A) com Desenvolver e validar 

Específico 3 e 4) políticas de produção alternativas (B, C...), o Modelo de Gestão 
manipulando variáveis como estoque de Otimizada. 
segurança ou tempo de lead-time para 

suprimentos. 

Validação e Cálculo de Ganhos: Quantificar o desperdício 
Conclusão esperado e custos nos cenários simulados. Quantificar os ganhos 

(Objetivo Proposição de Diretrizes: Elaborar o plano de esperados para a 

Específico 4 e 5) ação detalhado para a implementação das redução de 
políticas ótimas. desperdício. 

Fonte: Elaborado pelos autores. 

4.2 População e Amostra 

A população-alvo compreende o conjunto de usuários do refeitório 
institucional (discentes) e os registros administrativos correspondentes às operações 



 
 

de reserva e consumo de refeições. A amostra de dados é constituída por registros 
históricos extraídos do sistema de controle do refeitório, abrangendo um período de 
6 meses de operação contínua, o que permite identificar padrões sazonais semanais 
e mensais. Foram considerados apenas registros com informações completas de 
data, status de reserva, consumo efetivo e categoria de usuário. Casos com 
inconsistências, duplicidades ou ausência de timestamps foram excluídos do dataset 
final. 

4.3 Material e Ambiente do Experimento 

A coleta de dados foi baseada em dados secundários. As ferramentas 
computacionais e os dados utilizados estão detalhados na Tabela 2. 

Tabela 2 - Material e Ambiente do Experimento 

Item Descrição/Especificação Função no Experimento 

Registros históricos 
anonimizados de 6 meses Base empírica para EDA, extração 

Dados Secundários (reservas, consumo, de parâmetros probabilísticos 
cardápio, clima, (distribuições, probabilidades de 

calendário letivo). no-show). 

Linguagem de Implementação das análises 
Programação Python exploratório da dados e do Modelo 

de Simulação. 

Modelagem de Biblioteca Python para Desenvolvimento do modelo de 
Simulação simulação gestão otimizado para simular os 

fluxos operacionais. 

Modelagem da Demanda (ex: 

Modelos Estatísticos statsmodels, sklearn SARIMA/Regressão Preditiva) para 
(Biblioteca Python) gerar as previsões usadas como 

input da Simulação (o Treatment de 
Previsão). 

Fonte: Elaborado pelos autores. 

4.4 Procedimentos de Coleta e Tratamento de Dados 

Os procedimentos seguiram uma sequência estruturada para garantir a 
qualidade e a relevância dos dados para a modelagem e simulação: 



 
 

1)​ Extração de Dados: Obtenção dos registros históricos de reservas e 
consumo junto ao sistema de controle do refeitório institucional. 

2)​ Tratamento e Limpeza: Exclusão de valores inconsistentes, duplicidades e 
registros incompletos, seguida da padronização de formatos de data e 
categorias para garantir a consistência do dataset. 

3)​ Análise Exploratória de Dados (EDA) e Engenharia de Features: Esta 
etapa foi crucial para compreender o comportamento da demanda e criar 
variáveis preditivas. O processo incluiu: 
●​ Engenharia de Features de Calendário e Cíclicas: Criação de variáveis 

como dia da semana, mês, e dia do ano, incluindo suas transformações 
senoidais e cossenoidais para capturar a natureza cíclica do tempo. 

●​ Engenharia de Features de Lag: Geração de variáveis com valores 
passados da demanda (servidas_total_lag_Xd) e das reservas 
(reservas_total_lag_Xd) para capturar a dependência temporal. 

●​ Identificação de Dias Anômalos: Foi criada uma feature binária 
(ocorrencia_consumo_zero_anomalo) para identificar dias com reservas, 
mas sem consumo registrado, indicando eventos atípicos. 

Imagem 1: Contagem de Dias com Ocorrência de Consumo Zero Anômalo 

 

Fonte: Elaborado pelos autores com uso da linguagem Python. 

 

Análise da Distribuição da Variável Alvo: A distribuição da variável 
servidas_total foi analisada para compreender sua forma, centralidade e dispersão. 

Imagem 2: distribuição Geral de Refeições Servidas 



 
 

 

Fonte: Elaborado pelos autores com uso da linguagem Python. 

Análise da Sazonalidade Semanal: A variação da demanda ao longo da 
semana foi investigada, revelando uma forte sazonalidade, com maior consumo em 
dias úteis. 

Imagem 3: Distribuição do Consumo por Dia da Semana 

 

Fonte: Elaborado pelos autores com uso da linguagem Python. 

 

Análise do Impacto de Feriados: O comportamento do consumo em feriados, 
recessos e vésperas foi analisado, mostrando quedas significativas na demanda. 

 

Imagem 4: Distribuição do Consumo em Feriados, Recessos e Vésperas 



 
 

 

Fonte: Elaborado pelos autores com uso da linguagem Python. 

 

Análise de Tendência com Médias Móveis: Foram utilizadas médias móveis 
de 7 e 30 dias para suavizar a série temporal e visualizar tendências. 

Imagem 5: Demanda de Refeições e Médias Móveis 

 

Fonte: Elaborado pelos autores com uso da linguagem Python. 

 

Decomposição da Série Temporal: A série de demanda foi decomposta nos 
componentes de Tendência, Sazonalidade e Resíduos para uma compreensão mais 
clara de sua estrutura. 

 



 
 

Imagem 6:  

 

Fonte: Elaborado pelos autores com uso da linguagem Python. 

 

Análise da Sazonalidade Semanal: A variação da demanda ao longo da 
semana foi investigada, revelando uma forte sazonalidade. O consumo é 
significativamente maior nos dias úteis, com picos de demanda ocorrendo de forma 
mais proeminente nas segundas e quartas-feiras, seguido por uma queda acentuada 
nos fins de semana. 

 

 

 

 

 

 

 

Imagem 7 - Análise de Outliers nos Resíduos da Decomposição 



 
 

 

Fonte: Elaborado pelos autores com uso da linguagem Python. 

 

Análise de Correlação e Seleção de Features: A correlação entre as features 
e a variável alvo foi calculada, e um modelo de Random Forest foi utilizado para 
identificar as variáveis mais importantes para a predição da demanda, confirmando a 
relevância dos lags e eventos especiais. 

Imagens 8 – Features com Maior Correlação Positiva 

 

Fonte: Elaborado pelos autores com uso da linguagem Python. 

 

 

 

 

 



 
 

 

 

Imagens 9 – Features com Maior Correlação Negativa 

 

Fonte: Elaborado pelos autores com uso da linguagem Python. 

 

Imagens 10 – Heatmap de correlação mais positivas 

 

Fonte: Elaborado pelos autores com uso da linguagem Python. 

 

 



 
 

 

 

Imagens 11 – Heatmap de correlação mais negativas 

 

​ Fonte: Elaborado pelos autores com uso da linguagem Python. 

 

 

4.5 Análise de Dados 

Os dados quantitativos foram analisados por meio de estatísticas descritivas 
(médias, desvios-padrão) e técnicas de análise de séries temporais (decomposição, 
autocorrelação). 

O núcleo da análise foi a Simulação Probabilística de Monte Carlo, utilizada 
para estimar distribuições de resultados (percentual de desperdício, probabilidade de 
escassez) sob diferentes políticas operacionais. Para cada política, foram realizadas 
500 iterações independentes, simulando 30 dias de operação por rodada, permitindo 
uma avaliação robusta do desempenho de cada cenário. 

 

4.6 Aspectos Éticos e Riscos Associados 

O estudo utiliza dados administrativos anonimizados, sem qualquer 
identificação pessoal dos usuários, respeitando integralmente a Lei Geral de 



 
 

Proteção de Dados (LGPD, Lei nº 13.709/2018). Como o projeto não envolve 
interação direta com indivíduos, não há riscos físicos, psicológicos ou sociais aos 
participantes. 

Ainda assim, reconhece-se um risco ético residual relacionado à possibilidade 
de reidentificação indireta, caso variáveis sensíveis sejam combinadas de maneira 
inadequada. Esse risco é mitigado por meio de agregação e anonimização dos 
dados, controle de acesso restrito aos arquivos e armazenamento em servidores 
institucionais protegidos. 



4 
 

5​ CRONOGRAMA 
A seguir, é apresentado o cronograma das atividades, estruturado para a conclusão do projeto experimental dentro dos 

prazos da disciplina MQA, com foco na iteração entre as etapas. 

Data 
Etapa Atividade 

26/8 2/9 9/9 16/9 23/9 30/9 7/10 14/10 21/10 28/10 3/11 4/11 11/11 18/11 24/11 25/11 2/12 

Definição do Tema (Critério 
FINER, Questão de Pesquisa)  x                

Planejamento e Execução do 
Estado da Arte (Embasamento   x               

Teórico) 

1 Definição do Objetivo Geral e 
Específicos   x               

Definição da Hipótese   x               

Apresentação da Etapa 1*    x              

Entrega da apresentação e 
plano de projeto da etapa 1*    x              

Revisão e Ajuste dos Itens da 
Etapa 1 (Título, Contexto,     x             

2 Hipótese) 

Definição da Lista de Material e 
Ambiente do Experimento     x             

 
 



 
 

Data 
Etapa Atividade 

26/8 2/9 9/9 16/9 23/9 30/9 7/10 14/10 21/10 28/10 3/11 4/11 11/11 18/11 24/11 25/11 2/12 

Elaboração do Método da 
Pesquisa      x            

(Modelagem/Simulação) 

Definição da Lista de Risco e 
Viés (Threats to Validity)      x x           

Elaboração e Finalização do 
Cronograma Detalhado       x           

Apresentação do plano de 
projeto* (Etapa 2a:        x          

Planejamento do Experimento) 

Análise e modelagem da 
demanda de refeições          x x       
(Objetivo Específico 1) 

Entrega do plano de projeto** 
(Etapa 2b:Modelagem)         x         

Mapear fluxos do processo de 
reserva e consumo (Objetivo            x x     

Específico 2) 

Desenvolvimento do Modelo de 
Simulação (Artefato)            x x     

3 Teste de Cenários e 
Quantificação de Ganhos             x x    

(Objetivo Específico 4) 



 
 

Data 
Etapa Atividade 

26/8 2/9 9/9 16/9 23/9 30/9 7/10 14/10 21/10 28/10 3/11 4/11 11/11 18/11 24/11 25/11 2/12 

Entrega da apresentação e do 
relatório com o andamento do             x     

projeto *** 

Apresentação do andamento 
do projeto****              x    

Elaboração de Diretrizes e 
Redação do Relatório Final               x   

(Objetivo Específico 5) 

4 Entrega da apresentação e do 
relatório final*****                x  

Apresentação do projeto 
executado******                 x 

 



4 
 

6. ATIVIDADES REALIZADAS 
A condução da pesquisa ocorreu em etapas principais, articulando análise de 

dados, modelagem estatística e experimentação computacional, conforme detalhado 
nos procedimentos de execução e coleta de dados da seção 4. 

6.1 Coleta e Preparação da Base de Dados 

A base histórica de consumo e reservas de refeições foi extraída do sistema 
de gestão do refeitório institucional, incluindo registros de quatro meses de 
operação. Os dados passaram por processos de limpeza e padronização, com 
exclusão de duplicidades e inconsistências, para garantir a qualidade da análise. 

6.2 Análise Exploratória e Modelagem Empírica 

A partir dos registros diários de reservas e consumo, foram calculados 
indicadores de absenteísmo (no-show) e comparecimento sem reserva (walk-in). A 
análise desses dados (EDA) revelou padrões cruciais: 

●​ Sazonalidade Semanal: Confirmou-se uma forte variação no consumo ao 
longo da semana, com picos de demanda proeminentes nas segundas e 
quartas-feiras, seguidos por uma queda acentuada nos fins de semana. 

●​ Impacto de Eventos Especiais: Foi identificada uma forte correlação 
negativa entre a ocorrência de feriados e recessos e o número de refeições 
servidas. 

●​ Relevância de Features de Lag: A análise de correlação demonstrou que a 
demanda e as reservas dos dias anteriores (features de lag) estão entre os 
preditores com maior impacto positivo, confirmando a dependência temporal 
dos dados. 

Estas descobertas foram essenciais para a estruturação do modelo de 
simulação, garantindo que ele fosse alimentado por padrões empiricamente 
validados. 

6.3 Estruturação e Execução do Modelo de Simulação 

A fase de experimentação foi conduzida por meio de um modelo de simulação 
de Monte Carlo, implementado em Python com o uso das bibliotecas Numpy e 
Pandas. Diferentemente de uma abordagem com política única, o modelo foi 
 

 



 
 

desenhado para encontrar a melhor estratégia de produção para cada dia da 
semana de forma independente, reconhecendo a forte sazonalidade semanal 
identificada na análise exploratória. 

O processo de otimização consistiu nas seguintes etapas: 

1.​ Definição dos Cenários por Dia da Semana: Para cada dia (de segunda a 
sexta-feira), um conjunto de políticas de produção foi testado exaustivamente. 
Sábados e domingos foram excluídos devido não serem dias letivos para os 
alunos que têm direito a refeição. 

2.​ Teste de Políticas e Parâmetros: As políticas avaliadas incluíram: 
a.​ Política exact: Produção igual ao número de reservas do dia. Serviu 

como linha de base. 
b.​ Política safety_margin: A produção é ajustada com base na demanda 

esperada (reservas - no-shows médios + walk-ins médios), acrescida 
de uma margem de segurança. O modelo testou sistematicamente 
margens de 1% a 20%. 

c.​ Política quantile: A produção é definida como um percentil da 
distribuição histórica de reservas para aquele dia da semana. O 
modelo testou percentis de 70% a 99%. 

3.​ Simulação e Cálculo de Custo: Para cada dia da semana e para cada 
combinação de política e parâmetro (e.g., safety_margin com 5%, quantile 
com 85%, etc.), foram executadas 500 simulações, cada uma representando 
30 dias de operação. Em cada dia simulado, o número de reservas, no-shows 
e walk-ins foi sorteado aleatoriamente das distribuições empíricas 
correspondentes. O custo total foi calculado considerando o custo de R$17,36 
por refeição tanto para o desperdício (refeições produzidas e não 
consumidas) quanto para a falta (demanda não atendida). 

4.​ Identificação da Política Ótima Diária: Ao final das simulações para um dia 
da semana, o modelo calculou o custo médio diário para cada cenário 
testado. A combinação de política e parâmetro que resultou no menor custo 
médio foi selecionada como a estratégia ótima para aquele dia. 

 



 
 

Essa abordagem resultou em um portfólio de políticas dinâmicas, em vez de 
uma regra única, permitindo que a produção se ajustasse de forma inteligente à 
variabilidade de demanda específica de cada dia. 

 

6.4 Coleta e Análise dos Resultados da Simulação 

A análise dos resultados foi realizada em três etapas principais para garantir 
uma validação robusta da estratégia: 

1.​ Consolidação da Otimização Diária: Para cada dia da semana, os custos 
médios diários de todas as políticas e parâmetros testados foram compilados. 
A combinação com o menor custo foi identificada, formando um portfólio de 
“políticas ótimas diárias”. 

2.​ Backtesting da Estratégia Otimizada: As políticas ótimas encontradas 
foram então aplicadas ao conjunto de dados históricos. Esse processo, 
conhecido como backtesting, calculou qual teria sido a produção, o 
desperdício e a falta para cada dia real se a estratégia otimizada estivesse 
em vigor. O resultado é uma série temporal que compara a demanda real com 
a produção que o modelo teria recomendado. 

3.​ Análise Comparativa e Financeira: Por fim, o desempenho da Simulação 
Otimizada (baseada no backtesting) foi comparado ao Cenário Atual (uma 
política exact que serve como linha de base). Um ranking diário foi criado 
para determinar qual cenário teria o menor custo a cada dia. Os custos totais 
foram consolidados para quantificar a economia financeira gerada pela 
abordagem otimizada ao longo de todo o período histórico analisado. 

 

7. RESULTADOS 
A Análise Exploratória de Dados (EDA), detalhada na seção de metodologia, 

revelou padrões cruciais na demanda de refeições, destacando a sazonalidade 
semanal como um fator de forte influência. A partir dessa constatação, a abordagem 
de simulação foi refinada para não apenas encontrar uma política ótima geral, mas 
para identificar a estratégia de produção ideal para cada dia da semana 
individualmente. 



 
 

 

O processo de otimização, executado de forma independente para cada dia, 
revelou que uma política única não é eficiente. Em vez disso, a melhor abordagem 
consiste em um portfólio de políticas dinâmicas, ajustadas à variabilidade de cada 
dia. A Tabela 3 apresenta o resumo das melhores políticas e parâmetros 
encontrados para cada dia da semana. 

Tabela 3 – Resumo comparativo das políticas operacionais simuladas 
Dia da Semana Melhor Política Parâmetro Custo Médio Diário 

Ótimo Simulado 

Segunda-feira exact N/A R$ 198.57 

Terça-feira safety_margin 1.0% R$ 186.67 

Quarta-feira safety_margin 5.0% R$ 294.05 

Quinta-feira safety_margin 4.0% R$ 433.60 

Sexta-feira safety_margin 5.0% R$ 321.61 

Fonte: Resultados da simulação Monte Carlo (n = 500 execuções por política para cada dia da 
semana). 

O resultado da otimização mostra que a política exact (produzir exatamente o 
número de reservas) permanece a mais econômica para a Segunda-feira. Para os 
demais dias, a política de safety_margin (margem de segurança) foi considerada 
superior, porém com parâmetros ótimos notavelmente baixos, variando de 1% a 5%. 
Isso sugere que, sob a nova premissa de custo onde a falta não é mais penalizada, 
o modelo de otimização favorece agressivamente a minimização da superprodução. 

Para validar a eficácia desta estratégia composta, foi realizado um 
backtesting, aplicando as políticas ótimas diárias sobre o conjunto de dados 
históricos real. Esta análise comparou o desempenho da “Simulação Otimizada” com 
o “Cenário Atual” (assumindo uma política “exact” para todos os dias, que serve 
como linha de base). Os resultados consolidados são apresentados na Tabela 4. 



 
 

Tabela 4 – Placar Final e Resultado Financeiro: Simulação Otimizada vs. 
Cenário Atual 

Métrica Simulação Otimizada Cenário Atual (Base) 

Dias com Melhor 
Desempenho 42 18 
(Menor Custo) 

Dias com Empate 20 20 

Custo Total no 
Período (R$) R$ 27,671.84 R$ 37,046.24 

Fonte: Resultados do backtesting sobre os dados históricos. 

A estratégia otimizada demonstrou um menor custo diário em 42 dos 80 dias 
analisados. Contudo, ao consolidar o desempenho financeiro total, a implementação 
das políticas otimizadas resultaria em um custo total de R$ 27,671.84, 
representando uma economia de R$ 9.374,40 (ou 25,30%) em comparação com o 
custo de R$ 37,046.24 da política base exact. Este resultado contra intuitivo é 
fundamental para as conclusões do estudo. A Figura 11 ilustra o comportamento da 
produção simulada. 

Figura 11: Backtesting – Comparativo entre Demanda Real e Produção 
Simulada Otimizada 

Fonte: Elaborado pelos autores com uso da linguagem Python. 

 

Este gráfico evidencia a capacidade da estratégia otimizada de se ajustar à 
demanda real, produzindo mais em dias de pico e menos em dias de vale, 



 
 

resultando em um equilíbrio mais eficiente entre evitar o desperdício e prevenir a 
falta. 

 

8. CONCLUSÕES 
Este estudo demonstrou o potencial da abordagem integrada de análise 

exploratória de dados e simulação probabilística para otimizar a gestão da produção 
de refeições em restaurantes universitários. A principal conclusão é que uma 
estratégia de produção dinâmica e específica para cada dia da semana é superior a 
uma política estática e única, resultando em economia de custos mesmo com a 
premissa de custos simétricos para desperdício e falta. 

A otimização revelou que a política exact (produzir o número de reservas) é 
ideal para Segundas-feiras, enquanto políticas de safety_margin (margem de 
segurança) com diferentes parâmetros (de 1% a 5%) são mais eficazes para os 
demais dias da semana. O backtesting da estratégia otimizada contra os dados 
históricos demonstrou uma economia de custo total de R$9.374,40 (25.30%) no 
período analisado. Este resultado não apenas confirma a eficácia do método, mas 
também quantifica seu impacto financeiro, oferecendo uma justificativa clara para a 
implementação de políticas de produção mais inteligentes. 

A hipótese da pesquisa de que a abordagem integrada poderia resultar em 
uma redução percentual significativa do desperdício de alimentos (superior a 10%) 
foi validada pelo desempenho da estratégia otimizada, que alcançou uma economia 
de 25.30% no custo total, mesmo com custos simétricos para desperdício e falta. 
Dessa forma, os achados decorrentes deste estudo podem ser aplicados pela 
gestão de um refeitório ao implementar as políticas operacionais recomendadas com 
o objetivo de promover redução de custos e aprimorar o equilíbrio entre oferta e 
demanda. O modelo de simulação desenvolvido configura-se como um instrumento 
de apoio à decisão, permitindo a avaliação controlada de novas políticas a partir de 
dados históricos. 

Apesar da robustez dos resultados, o estudo apresenta limitações que devem 
ser consideradas, incluindo a restrição da amostragem empírica a um período de 
apenas quatro meses, o que pode não refletir adequadamente as variações 
sazonais mais amplas — como início e término de semestre ou períodos de férias 



 
 

—, bem como a simplificação adotada no modelo de simulação, que considera 
unicamente o volume total diário de refeições, desconsiderando diferenças entre 
tipos de cardápio e eventuais restrições de capacidade produtiva. Adicionalmente, 
este estudo está sujeito a diferentes formas de viés que devem ser reconhecidas, 
incluindo o viés de seleção, decorrente de uma amostra que pode não representar 
plenamente todos os períodos de operação do refeitório e, portanto, omitir eventos 
atípicos de longo prazo, como greves ou reformas; o viés de observação, associado 
à possibilidade de erros de registro humano nos sistemas de reservas e consumo, 
mitigado por meio de procedimentos de limpeza e verificação de consistência interna 
dos dados; e o viés de abstração, inerente ao modelo de simulação, que 
necessariamente simplifica a realidade ao omitir mecanismos operacionais 
relevantes — como erros humanos na cozinha ou falhas de equipamentos — 
capazes de influenciar a causalidade dos resultados observados. 

Como sugestões para trabalhos futuros, recomenda-se a evolução do modelo 
proposto por meio da substituição da amostragem estocástica por uma abordagem 
baseada em Machine Learning, visando aprimorar a precisão preditiva e a robustez 
das análises. Nesse sentido, estudos subsequentes podem concentrar-se no 
desenvolvimento de modelos preditivos de demanda — tanto da demanda total 
(servidas_total) quanto de suas componentes (reservas_total, no-show, walk-in) — 
utilizando o conjunto de dados enriquecido com variáveis de defasagem, calendário 
e condições climáticas, e explorando diferentes classes de algoritmos, como 
XGBoost e LightGBM para dados tabulares, modelos de séries temporais como 
SARIMA e Prophet, e arquiteturas de Deep Learning, como redes neurais 
recorrentes (LSTM). Após a validação dos modelos mais promissores, 
recomenda-se sua integração ao arcabouço de simulação, substituindo a geração 
estocástica de valores históricos por previsões diárias produzidas pelo modelo 
preditivo. A partir dessas previsões, novas políticas operacionais — incluindo 
parâmetros como safety_margin e quantile — poderão ser otimizadas de forma 
dinâmica. Por fim, sugere-se que estudos futuros também realizem uma etapa de 
validação por backtesting sobre dados históricos, de modo a quantificar o ganho 
incremental de desempenho e a economia potencial associada ao uso de modelos 
preditivos, consolidando a viabilidade da incorporação de Machine Learning no 
processo de tomada de decisão. 



 
 

REFERÊNCIAS BIBLIOGRÁFICAS 
ABUD, J. Dívida externa, estabilização econômica, abertura comercial, ingresso de 
capitais externos e baixo crescimento econômico. 1996. 205 f. Tese (Doutorado em 
Economia de Empresas) – Escola de Administração de Empresas de São Paulo da 
Fundação Getúlio Vargas, São Paulo, 1996. 
 
AKKERMAN, A. R. Waste management in food services: a strategic perspective on 
supply chain failures. Journal of Operations Management, v. 32, n. 4, p. 115-128, 
2024. 
 
AKKERMAN, R. Food loss, food waste, and sustainability in food supply chains. In: 
Sustainable Food Supply Chains. Cham: Springer, 2024. 
 
BRASIL. Lei nº 13.709, de 15 de dezembro de 2006. Dispõe sobre a Lei Geral de 
Proteção de Dados Pessoais (LGPD). Disponível em: 
http://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/lei/l11346.htm. Acesso em: 
4 out. 2024. 
 
CBORD. Campus Dining Trends Report: Waste Reduction Strategies. New York, 
2025. 
 
CBORD. Reducing food waste in colleges 2025: a data-driven approach. Relatório 
técnico, 2025. 
 
CHAUDHARI, M. A. et al. Forecasting and modelling of food demand supply chain 
using machine learning. International Journal of Innovative Research in 
Multidisciplinary Physical Sciences (IJIRMPS), v. 13, n. 2, p. 1-14, mar./abr. 2025. 
 
CHOI, J. A review of forecasting studies for the restaurant industry. Journal of 
Foodservice Business Research, v. 25, n. 4, p. 389-407, 2022. 
 
CHOI, S. Quantitative decision making in food service supply chains: a simulation 
approach to demand forecasting and waste reduction. Journal of Food Supply Chain 
Management, v. 14, n. 2, p. 45-60, 2022. 
 
LOOFBOURROW, B. M. Food insecurity in higher education: a contemporary review. 
Journal of Student Affairs Research and Practice, v. 60, n. 2, p. 135-148, 2023. 
 
LOOFBOURROW, J. L. College student food insecurity: factors and interventions for 
health and academic success. Journal of Nutrition Education and Behavior, v. 55, n. 
4, p. 301-310, 2023. 
 
OLAWALE, R. A. et al. Sustainable farming with machine learning solutions for 
minimizing food waste. Journal of Stored Products Research, v. 112, 102611, mar. 
2025. 
 
PAYNE-STURGES, D. C. et al. Student hunger on campus: food insecurity among 
college students. American Journal of Health Promotion, v. 32, n. 2, p. 349-354, 
2017. 



 
 

 
PAYNE-STURGES, D. C. et al. The role of college and university student food 
security in academic success and persistence. Journal of Public Health Management 
and Practice, v. 23, n. 6, p. 627-635, 2017. 
 
RAJENDRAN, B. et al. A predictive modelling approach to decoding consumer 
intention for adopting energy-efficient technologies in food supply chains. Decision 
Analytics Journal, v. 15, 100561, 2025. 
 
REFED. Foodservice food waste action guide. Relatório técnico, 2016. 
REFED. The Food Waste Report: a comprehensive analysis of food waste in the US. 
New York, 2016. 
 
SHEEL, A. Monte Carlo simulations and scenario analysis. Decision Sciences, v. 26, 
n. 5, p. 537-549, 1995. 
 
SHEEL, H. G. Simulation-based planning for supply chain optimization under 
demand uncertainty. International Journal of Operations and Production 
Management, v. 15, n. 7, p. 34-45, 1995.