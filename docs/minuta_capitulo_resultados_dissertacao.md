# Minuta Textual do Capítulo de Resultados e Discussão

**Programa:** Mestrado Profissional em Gestão e Tecnologia em Sistemas Produtivos (PPG-GTSP)  
**Instituição Mantenedora:** Centro Estadual de Educação Tecnológica Paula Souza (CEETEPS)  
**Instituição Parceira / Objeto Empírico:** Instituto Federal de São Paulo (IFSP) — Campus Itaquaquecetuba  
**Linha de Pesquisa:** Linha 2 — Sistemas de Informação e Tecnologias Digitais  
**Produto Técnico:** Artefato de Apoio à Decisão Operacional para Previsão de Demanda de Refeições  
**Localização:** Pasta `docs/`  
**Data:** Outubro de 2026  

---

# CAPÍTULO 4 — RESULTADOS E DISCUSSÃO

Neste capítulo, apresentam-se os resultados obtidos a partir do desenvolvimento e validação do artefato técnico de apoio à decisão operacional. A exposição estrutura-se em duas seções fundamentais: primeiramente, detalha-se a modelagem sistêmica do artefato, compreendendo a integração de bases de dados, o diagnóstico histórico dos regimes de reserva e a seleção dos atributos mais relevantes; em seguida, expõem-se os resultados do torneio de algoritmos de aprendizado de máquina, o confronto direto com o planejamento institucional da nutricionista e a introdução de margens de segurança prudenciais orientadas pela perda assimétrica na alimentação escolar pública.

---

## 4.1. SEÇÃO 1: CONSTRUÇÃO DO MODELO SISTÊMICO E ENGENHARIA DO ARTEFATO

### 4.1.1. Arquitetura Sistêmica e Ingestão de Dados

A operacionalização da alimentação coletiva no IFSP Campus Itaquaquecetuba envolve múltiplos fatores exógenos e comportamentais. Para subsidiar a modelagem preditiva, estruturou-se uma arquitetura de dados em camadas (Bronze, Silver e Gold):
1. **Camada Bronze:** Repositório dos dados brutos recebidos da Coordenadoria Sociopedagógica e registros meteorológicos da estação virtual.
2. **Camada Silver:** Harmonização de 655 dias letivos (2023 a 2026), com saneamento de duplicidades, padronização fonética de cardápios e enriquecimento com o histórico de precipitação e temperatura da API Open-Meteo.
3. **Camada Gold:** *Feature Store* contendo variáveis defasadas (*lags*), atributos de calendário escolar e indicadores de adversidade climática.

---

### 4.1.2. O Diagnóstico Histórico: O Mito do Saldo Líquido e a Ruptura dos Regimes

A avaliação preliminar das planilhas históricas revelou um fenômeno clássico da literatura de gestão de operações: o **Efeito Compensatório (*offsetting errors*)**, conforme alertado por Silver, Pyke e Peterson (1998). No balanço contábil anual, desvios positivos e negativos anulam-se aritmeticamente, gerando uma falsa impressão de estabilidade que não corresponde à realidade da cozinha.

A **Tabela 1** decompõe os 655 dias letivos em registros diários de sobras e faltas efetivas.

#### Tabela 1 — Decomposição Anual de Sobras, Faltas e Efeito Compensatório (2023–2026)
| Ano | Regime Operacional | Dias | Consumo Médio | Reserva Média | Saldo Anual Aparente | Sobra Real Acumulada | Falta Real Acumulada | Dias com Falta (%) | MAE Diário (ref/dia) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **2023** | Alunos *(Manifestação)* | 181 | 107,8 | 111,9 | **$+742$ ref** | 1.916 ref | 1.174 ref | 38,1% | 17,1 |
| **2024** | Alunos *(Manifestação)* | 122 | 167,3 | 132,9 | **$-4.190$ ref** | 334 ref | 4.524 ref | **82,8%** | 39,8 |
| **2025** | Alunos *(Manifestação)* | 155 | 138,4 | 118,2 | **$-3.130$ ref** | 666 ref | 3.796 ref | **78,7%** | 28,8 |
| **2026** | Nutricionista *(Estimativa)* | 140 | 167,1 | 186,2 | **$+2.670$ ref** | 3.354 ref | 684 ref | 37,1% | 28,8 |

*Fonte: Dados da pesquisa (2026).*

A visualização desse fenômeno é apresentada na **Figura 1**.

> **[INSERIR FIGURA 1 AQUI]**  
> *Arquivo: `reports/dissertacao_selecao/figuras/figura_1_diagnostico_saldo_vs_realidade_diaria.png`*  
> **Figura 1 — Decomposição do Efeito Compensatório: O Mito do Saldo Anual vs. Sobras e Faltas Diárias Reais (2023 a 2026).**

Como se observa na **Figura 1 (Gráfico 1)**, o ano de 2023 apresentava um saldo anual aparentemente equilibrado ($+742$ refeições em 181 dias, ou apenas $+4$ refeições/dia). Todavia, a análise registro a registro revelou que ocorreram **1.916 refeições descartadas** e **1.174 refeições em déficit**, com dias em que faltaram 43 refeições. Nos anos seguintes (2024 e 2025), o regime de manifestação individual voluntária dos alunos ruiu, atingindo índices alarmantes de **82,8% e 78,7% de dias com falta de reserva**. 

Para estancar a desordem no fornecimento, em 2026 a gestão instituiu o **Quantitativo Institucional Semanal da Nutricionista**. Ciente do custo social inaceitável de desassistir estudantes vulneráveis, a servidora adotou uma conduta de **superestimativa preventiva** (média de 186,2 estimadas contra 167,1 consumidas), derrubando as faltas, porém acumulando **3.354 refeições em potencial de sobra** (Figura 1, Gráfico 2).

---

### 4.1.3. Padrões Determinantes da Demanda Escolar (EDA)

A análise exploratória indicou que a adesão discente não é puramente aleatória, respondendo a fortes componentes de rotina acadêmica e atratividade alimentar (Eriksson et al., 2018).

Dois padrões destacaram-se como direcionadores principais:
1. **O Efeito do Dia da Semana:** Conforme ilustrado na **Figura 2**, o comparecimento atinge seu pico nas terças e quartas-feiras (médias de 168 e 172 refeições), apresentando uma queda sistemática e acentuada nas **sextas-feiras** (média de 124 refeições, redução de aproximadamente $27\%$). Esse comportamento reflete a grade horária concentrada e a evasão discente no encerramento da semana letiva.

> **[INSERIR FIGURA 2 AQUI]**  
> *Arquivo: `reports/dissertacao_selecao/figuras/figura_2_eda_consumo_dia_semana.png`*  
> **Figura 2 — Distribuição do Consumo Efetivo de Refeições por Dia da Semana.**

2. **A Influência do Cardápio:** A **Figura 3** confronta a frequência de oferta com o consumo médio conforme a proteína do dia. Cardápios contendo preparações tradicionais ou altamente atrativas (feijoada e preparações bovinas) atraem em média $20\%$ a $30\%$ mais alunos do que pratos baseados em ovos ou peixe.

> **[INSERIR FIGURA 3 AQUI]**  
> *Arquivo: `reports/dissertacao_selecao/figuras/figura_3_eda_impacto_proteina_cardapio.png`*  
> **Figura 3 — Relação entre Frequência de Oferta e Consumo Médio por Tipo de Proteína.**

---

### 4.1.4. Engenharia de Features e Importância dos Atributos

A partir do banco limpo, construíram-se mais de 60 variáveis explicativas. A aplicação de algoritmos de árvores de decisão permitiu ranquear a relevância relativa dessas características, sintetizada na **Figura 4**.

> **[INSERIR FIGURA 4 AQUI]**  
> *Arquivo: `reports/dissertacao_selecao/figuras/figura_4_importancia_top_features_rf.png`*  
> **Figura 4 — Ranquear das Variáveis Mais Importantes para a Predição de Demanda (Random Forest).**

Constata-se que a capacidade preditiva concentra-se em quatro eixos prioritários:
1. **Memória Semanal Recente:** O consumo verificado no mesmo dia da semana anterior (`consumo_mesmo_dia_sem_passada`) e duas semanas antes (`lag_10_dias_letivos`) responde por mais de $35\%$ da importância relativa;
2. **Calendário Escolar:** As variáveis binárias de dia da semana (`is_sexta`, `is_segunda`) e mês letivo;
3. **Composição Nutricional:** As variáveis indicadoras do tipo de proteína e técnica de cocção;
4. **Fatores Climáticos:** Índices de chuva acumulada (`precipitation_sum`) e rajadas de vento, que afetam diretamente o trajeto a pé da estação de trem até o campus.

---

## 4.2. SEÇÃO 2: RESULTADOS DOS ALGORITMOS E CONFRONTO DECISÓRIO

### 4.2.1. O Torneio dos Modelos e Validação Temporal Sequencial

Para assegurar validade científica e ausência total de vazamento de dados (*data leakage*), a modelagem empregou a metodologia de **Validação Temporal Sequencial (*Walk-Forward Validation*)** recomendada por Hyndman e Athanasopoulos (2021). A cada sexta-feira de corte $T$ ao longo de 28 semanas de 2026, os modelos foram treinados exclusivamente com o histórico anterior para projetar:
* **Horizonte $t+2$ (Secos — 14 dias de antecedência):** Projeção totalmente autônoma, sem interferência humana;
* **Horizonte $t+1$ (Perecíveis — 7 dias de antecedência):** Projeção da semana seguinte com a calibragem da estimativa institucional da nutricionista.

A **Tabela 2** apresenta o ranking dos melhores algoritmos confrontados com o benchmark humano da nutricionista.

#### Tabela 2 — Desempenho Comparativo dos Top Modelos de Machine Learning vs. Benchmark da Nutricionista
| Ranking / Algoritmo | Cenário Experimental | Horizonte de Decisão | MAE (ref/dia) | RMSE (ref/dia) | $R^2$ | Potencial Sobra | Potencial Falta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Lasso** *(Campeão $t+1$)* | Cenário 3 (Com Nutri) | $t+1$ (Perecíveis) | **22,27** | **32,33** | **0,498** | **1.107 ref** | 741 ref |
| **2. Ridge** *(Vice-Campeão $t+1$)* | Cenário 3 (Com Nutri) | $t+1$ (Perecíveis) | **22,46** | **32,82** | **0,483** | **1.161 ref** | 703 ref |
| **3. Regressão Linear** | Cenário 3 (Com Nutri) | $t+1$ (Perecíveis) | **22,87** | **32,56** | **0,491** | **916 ref** | 981 ref |
| **4. Estimativa Nutricionista** | Benchmark Humano | $t+1$ (Perecíveis) | **24,92** | **36,94** | **0,373** | **2.705 ref** | 684 ref |
| **5. Regressão Linear** *(Campeão $t+2$)* | Cenário 2 (Com Clima) | $t+2$ (Secos / 14 dias) | **28,67** | **38,64** | **0,268** | **1.099 ref** | 1.308 ref |

*Fonte: Dados da pesquisa (2026).*

A representação gráfica do confronto do Top 5 com as reservas é demonstrada na **Figura 5**.

> **[INSERIR FIGURA 5 AQUI]**  
> *Arquivo: `reports/dissertacao_selecao/figuras/figura_5_top5_modelos_vs_benchmark.png`*  
> **Figura 5 — Confronto de Desempenho do Top 5 Modelos de Machine Learning em Relação ao Benchmark Humano.**

Os modelos lineares regularizados (**Lasso** e **Ridge**) superaram expressivamente a estimativa isolada da servidora pública, reduzindo o erro médio absoluto de 24,92 para **22,27 refeições/dia** (ganho de $10,6\%$ de acurácia) e reduzindo as sobras em **$28,3\%$** (menos 438 refeições descartadas no período de teste). No horizonte de compras antecipadas de duas semanas ($t+2$), o modelo autônomo atingiu MAE de 28,67, viabilizando o suprimento de secos com folga operacional.

---

### 4.2.2. A Solução do Dilema Social: Fronteira Eficiente de Pareto do Modelo Híbrido

Apesar da superioridade em MAE da IA pura, os modelos tradicionais operam com função de perda simétrica, tratando sobras e faltas com o mesmo peso. Em consonância com a teoria de previsão colaborativa de Blattberg e Hoch (1990) e Armstrong (2001), implementou-se o **Modelo Híbrido Colaborativo**:
$$\hat{y}_{\text{híbrido}}(\alpha) = \alpha \cdot \hat{y}_{\text{IA}} + (1 - \alpha) \cdot \text{Quantitativo}_{\text{Nutricionista}}$$

A varredura contínua de $\alpha \in [0; 1]$ gerou a **Fronteira Eficiente de Pareto**, exposta na **Figura 6**.

> **[INSERIR FIGURA 6 AQUI]**  
> *Arquivo: `reports/dissertacao_selecao/figuras/figura_6_fronteira_pareto_modelo_hibrido.png`*  
> **Figura 6 — Fronteira Eficiente de Pareto do Modelo Híbrido Colaborativo (IA + Nutricionista).**

Os resultados empíricos validam brilhantemente a literatura de tomada de decisão: o ponto de equilíbrio ótimo ocorre em **$\alpha = 0{,}50$** (combinação $50/50$). Nessa ponderação:
* O volume de faltas atinge o **menor valor de toda a pesquisa (489 refeições)**, superando tanto a nutricionista pura (518) quanto a IA pura (741);
* As sobras caem de 1.545 para **1.289 refeições** (economia de mais de R$ 2.100 em relação à nutricionista);
* O erro médio absoluto atinge a marca histórica de **21,43 refeições/dia**.

A explicação reside no fato de que o algoritmo elimina o viés de superestimativa sistemática, enquanto o olhar qualitativo da profissional absorve oscilações de contexto não capturadas pelas tabelas.

---

### 4.2.3. Calibração de Margens de Segurança Prudenciais (Predição Conformal)

Para atender ao imperativo ético da gestão pública escolar de proteção ao estudante em vulnerabilidade nutricional, aplicou-se a teoria do modelo *Newsvendor* sob perdas assimétricas (Arrow et al., 1958; Khouja, 1999) acoplada à **Predição Conformal Não-Paramétrica** (Vovk et al., 2005; Angelopoulos & Bates, 2021). 

Calcularam-se margens empíricas a partir dos quantis de resíduos de subestimação ($P75 = +10$, $P85 = +19$ e $P90 = +29$ refeições/dia). O impacto dessa calibragem é exibido na **Figura 7**.

> **[INSERIR FIGURA 7 AQUI]**  
> *Arquivo: `reports/dissertacao_selecao/figuras/figura_7_impacto_margens_seguranca_conformal.png`*  
> **Figura 7 — Impacto das Margens de Segurança Conformal sobre o Volume de Sobras e a Taxa de Dias com Falta.**

A adoção da margem **Conformal P85 (+19 refeições)** reduz a proporção de dias com risco de falta de 43,4% para apenas **15,7% dos dias letivos**, conferindo um índice de **84,3% de proteção alimentar garantida** ao corpo discente, mantendo o custo orçamentário anual em patamares plenamente compatíveis com o contrato escolar.

---

### 4.2.4. Síntese Executiva: Matriz de Decisão Operacional

A consolidação final do artefato técnico é apresentada na **Figura 8** e sintetizada na **Tabela 3**, que confronta as trajetórias históricas com as alternativas desenvolvidas para a gestão do IFSP.

> **[INSERIR FIGURA 8 AQUI]**  
> *Arquivo: `reports/dissertacao_selecao/figuras/figura_8_matriz_decisao_custo_vs_protecao.png`*  
> **Figura 8 — Matriz Executiva de Apoio à Decisão Pública: Custo do Desperdício em Sobras (R$) vs. Índice de Proteção ao Aluno (%).**

#### Tabela 3 — Matriz Comparativa Definitiva das Políticas de Gestão de Refeições
| Estratégia de Decisão | Regime / Paradigma | Potencial Sobra (ref) | Potencial Falta (ref) | % Dias com Falta | MAE Diário | Desperdício Estimado (R$) | Diagnóstico Operacional |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **1. Reserva dos Alunos** | Histórico (2023–2025) | 2.916 ref | **9.494 ref** | **63,8%** | 27,10 | R$ 24.786,00 | **Inviável:** Déficit crônico severo. |
| **2. Nutricionista Pura** | Benchmark Humano (2026) | 1.545 ref | 518 ref | **41,0%** | 24,92 | R$ 13.132,50 | **Superestimativa:** Descarte elevado. |
| **3. IA Pura (Lasso/Ridge)** | Algoritmo Preditivo | **1.107 ref** | 741 ref | 43,4% | **22,27** | **R$ 9.409,50** | **Econômico:** Menor desperdício financeiro. |
| **4. Modelo Híbrido (50/50)** | IA + Nutricionista | **1.289 ref** | **489 ref** | 43,4% | **21,43** | **R$ 10.957,24** | **Equilíbrio Perfeito:** Menor erro absoluto. |
| **5. Híbrido + Margem P85** | **Recomendada para o IFSP** | 1.994 ref | **199 ref** | **16,9%** | 26,43 | R$ 16.952,79 | **Proteção Máxima:** 83,1% de blindagem social. |

*Fonte: Dados da pesquisa (2026). Nota: Estimativa financeira baseada no valor paramétrico contratual de R$ 8,50 por refeição.*

---

## 4.3. CONCLUSÕES DO CAPÍTULO E DIRETRIZES PARA A GESTÃO

Os resultados comprovam que a introdução de técnicas de inteligência artificial na alimentação coletiva pública não deve visar à substituição do julgamento humano, mas sim à sua capacitação técnica e instrumentalização (*Human-in-the-Loop*). 

A recomendação definitiva para o IFSP Campus Itaquaquecetuba estrutura-se no binômio:
1. **Horizonte $t+2$ (Secos — 14 dias antes):** Adoção da predição autônoma do modelo linear/ensemble para aquisição de gêneros não perecíveis;
2. **Horizonte $t+1$ (Perecíveis — 7 dias antes):** Adoção do **Modelo Híbrido Colaborativo com Margem Conformal P85**, que entrega a menor taxa de desassistência alimentar da história do campus (apenas 199 refeições em déficit potencial em 83 dias letivos) com controle orçamentário transparente.
