# 5 ANÁLISE E DISCUSSÃO DOS RESULTADOS PARCIAIS

Neste capítulo, apresentam-se os resultados empíricos, as análises diagnósticas e a validação experimental do artefato técnico desenvolvido para apoiar a tomada de decisão no planejamento da produção de refeições escolares. Em consonância com o método *Design Science Research Methodology* (DSRM) (Peffers et al., 2007), este capítulo corresponde às etapas de **Demonstração e Avaliação** da solução proposta. Para conferir clareza à interpretação gerencial dos achados, a trajetória dos resultados é estruturada segundo a abordagem de comunicação analítica e *storytelling com dados* (Knaflic, 2015), conduzindo o leitor por uma narrativa encadeada que parte dos dados brutos e alcança a formulação de políticas decisórias operacionais sob perda assimétrica.

A exposição organiza-se nas seguintes seções integradas:
1. **Resultados do processamento de dados nas camadas arquiteturais** (volumes consolidados na Camada Bronze, taxas de saneamento e padronização na Camada Silver, e a matriz de 106 preditores na Camada Gold);
2. **Resultados do diagnóstico retrospectivo e do efeito compensatório** (análise dos 655 dias letivos de 2023 a 2026, com segregação detalhada entre o período de reservas dos estudantes e o período de planejamento institucional da nutricionista);
3. **Resultados da análise exploratória dos padrões de demanda** (distribuição semanal com queda nas sextas-feiras, preferências por proteína e preparo, influência de intempéries meteorológicas e autocorrelação temporal da série);
4. **Resultados da seleção de atributos e relevância dos preditores na Camada Gold**;
5. **Resultados do torneio preditivo nas janelas de decisão operacional** (avaliação sequencial *walk-forward* em 28 semanas de 2026, confrontando o horizonte de compras antecipadas $t+2$ e o de preparo diário $t+1$ em três cenários de informação);
6. **Resultados das políticas operacionais, modelo híbrido e margens de segurança** (Fronteira Eficiente de Pareto e calibração não-paramétrica de margens prudenciais com Predição Conformal);
7. **Síntese dos resultados econômico-sociais, limitações da etapa de qualificação e passos para a defesa final**.

---

## 5.1 RESULTADOS DO PROCESSAMENTO DE DADOS NAS CAMADAS ARQUITETURAIS

A construção de um artefato preditivo robusto exige demonstrar a integridade e a qualidade dos dados gerados ao longo de seu pipeline de engenharia. Em conformidade com o padrão em medalhão (*Medallion Architecture*), a base empírica foi processada em três camadas sucessivas, cujos resultados quantitativos de ingestão, higienização e enriquecimento são apresentados a seguir.

### 5.1.1 Resultados da Ingestão na Camada Bronze

A Camada Bronze consolidou o repositório imutável dos arquivos brutos coletados junto aos setores administrativos e às plataformas digitais da instituição. A integração automatizada das fontes primárias resultou no conjunto de arquivos sumarizado no **Quadro 1**.

#### Quadro 1 — Resultados da ingestão de dados primários na Camada Bronze

| Conjunto de dados ingerido | Formato de origem | Período temporal | Unidades brutas captadas | Integridade dos registros | Destinação no artefato |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Registros de consumo real** | Planilhas Excel (catraca/fichas) | Fev/2023 a Ago/2026 | 655 datas com registro | 100% de preenchimento diário | Definição da variável-alvo ($y$) de refeições servidas no almoço. |
| **Reservas discentes individuais** | Google Forms (respostas) | Fev/2023 a Dez/2025 | 458 datas letivas | Cobertura integral do período de formulário | Histórico de manifestação individual voluntária dos estudantes. |
| **Quantitativos da nutricionista** | Planilhas de controle semanal | Fev/2026 a Ago/2026 | 140 datas planejadas | 100% das semanas letivas de 2026 | Quantidades diárias fixadas institucionalmente pela servidora. |
| **Textos descritivos de cardápio** | Informativos da Coordenadoria | Fev/2023 a Ago/2026 | 751 preparações descritas | 503 dias letivos com cardápio | Base textual para extração de categorias nutricionais e atratividade. |
| **Série temporal meteorológica** | API Open-Meteo Historical | Jan/2023 a Ago/2026 | 1.379 dias de medições | Sem descontinuidades temporais | Medições de precipitação, temperatura e vento no local do campus. |
| **Calendário acadêmico escolar** | Resoluções administrativas | Jan/2023 a Dez/2026 | 1.461 datas cronológicas | Calendário contínuo de 4 anos | Identificação de dias letivos, feriados, emendas e recessos. |

*Fonte: Dados da pesquisa (2026).*

O procedimento de ingestão reuniu registros referentes a 1.461 datas cronológicas contínuas entre janeiro de 2023 e dezembro de 2026. Desse total, **655 corresponderam a dias letivos efetivos com fornecimento regular de refeições**. A preservação desses arquivos em tabelas colunares Parquet garantiu fidelidade estrita às fontes primárias e permitiu auditar retroativamente a disponibilidade temporal de cada variável, assegurando que nenhum dado indisponível na data de cada decisão fosse utilizado indevidamente.

### 5.1.2 Resultados do Saneamento e Harmonização na Camada Silver

O processamento da Camada Silver transformou as planilhas heterogêneas e os textos brutos em tabelas harmonizadas, gerando a tabela fato diária unificada (`silver_fato_diaria.parquet`) contendo 1.461 linhas e 46 colunas auditadas.

Os principais resultados das rotinas de limpeza e padronização compreenderam:
1. **Resolução de inconsistências de datas e duplicidades**: Foram identificadas e tratadas 12 datas com duplicidade de lançamento decorrentes de digitações repetidas em formulários de refeitório, mantendo-se os números validados pela fiscalização do contrato terceirizado;
2. **Saneamento e classificação dos cardápios**: As 751 descrições textuais livres de pratos foram categorizadas por processamento de texto. O resultado dessa classificação agrupou o cardápio em cinco grupos proteicos fundamentais: carne bovina (presente em 31,4% dos cardápios), carne de frango (38,6%), carne suína (14,2%), preparações com ovos/vegetarianas (9,8%) e peixes (6,0%). Em relação às técnicas de cocção, 44,2% corresponderam a preparações assadas ou grelhadas, 46,8% a ensopados/molhos e 9,0% a preparações fritas;
3. **Acoplamento meteorológico georreferenciado**: A integração dos dados da API Open-Meteo resultou em 1.379 registros diários alinhados às coordenadas da escola, com média histórica de precipitação de $4{,}1\text{ mm/dia}$ e temperatura máxima média de $24{,}8^\circ\text{C}$ nas datas de funcionamento escolar;
4. **Base consolidada Silver**: O cruzamento relacional entre as tabelas de calendário, cardápio, clima, reservas e consumo produziu uma base única contínua, sem descontinuidades temporais nas variáveis essenciais.

### 5.1.3 Resultados da Engenharia de Variáveis na Camada Gold

Na Camada Gold, os dados higienizados da Camada Silver foram convertidos na *Feature Store* analítica (`gold_feature_store_completa.parquet`), totalizando **1.461 datas e 106 colunas estruturadas**. 

Desse universo, isolou-se o conjunto supervisionado de modelagem (`gold_dataset_ml_limpo.parquet`), composto por **588 datas letivas completas** que dispõem simultaneamente de histórico anterior suficiente para cálculo de defasagens móveis e valores válidos de todas as variáveis de entrada.

Entre os 106 atributos computados, destacam-se quatro grupos funcionais de variáveis explicativas:
- **Atributos de defasagem temporal (*lags*)**: consumo verificado 5 dias úteis antes (`consumo_lag_5`), 10 dias úteis antes (`consumo_lag_10`), média móvel dos últimos 5 dias letivos (`media_movel_5d`) e desvio padrão recente (`desvio_movel_5d`);
- **Atributos de calendário e ciclicidade**: dia da semana numérico e binário (`is_segunda` a `is_sexta`), mês letivo, semestre acadêmico e codificação trigonométrica periódica via seno e cosseno do dia do ano;
- **Atributos de composição alimentar**: variáveis binárias indicadoras (0 ou 1) para as cinco classes de proteína e quatro técnicas de preparo, além de escores contínuos de atratividade calculados a partir da média histórica de consumo de cada prato;
- **Atributos meteorológicos**: precipitação diária acumulada (`precipitation_sum`), temperatura máxima diária (`temperature_2m_max`), amplitude térmica e velocidade máxima das rajadas de vento (`wind_gusts_10m_max`).

---

## 5.2 RESULTADOS DO DIAGNÓSTICO RETROSPECTIVO E DO EFEITO COMPENSATÓRIO

A análise dos 655 dias letivos de consumo entre 2023 e 2026 permitiu avaliar quantitativamente a eficiência das práticas de planejamento adotadas historicamente no campus. Os resultados comprovam que a análise por saldos anuais acumulados encobria severos descompassos cotidianos.

### 5.2.1 A Mensuração do Efeito Compensatório nos Dados Reais

Conforme postulado na literatura de gestão de operações (Silver et al., 1998; Makridakis et al., 2020), o **efeito compensatório** (*offsetting errors*) manifesta-se quando os erros positivos e negativos de planejamento se anulam na soma anual agregada:
$$\text{Saldo Anual} = \sum_{t=1}^{N} (\text{Planejado}_t - \text{Consumo Real}_t)$$

A **Tabela 1** apresenta a decomposição formal dos dados anuais, confrontando o saldo líquido contábil com as sobras e faltas potenciais calculadas data a data.

#### Tabela 1 — Decomposição anual de sobras, faltas e efeito compensatório (2023 a 2026)

| Ano | Regime | Dias ($n$) | Consumo Médio | Planejado | Saldo Anual | Sobras Potenciais | Faltas Potenciais | Dias com Déficit (%) | MAE (ref/dia) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **2023** | Reservas dos alunos | 181 | 107,8 | 111,9 | **$+742$** | 1.916 | 1.174 | 38,1% | 17,07 |
| **2024** | Reservas dos alunos | 122 | 167,3 | 132,9 | **$-4.190$** | 334 | 4.524 | **82,8%** | 39,82 |
| **2025** | Reservas dos alunos | 155 | 138,4 | 118,2 | **$-3.130$** | 666 | 3.796 | **78,7%** | 28,79 |
| **2026** | Nutricionista | 140 | 167,1 | 186,2 | **$+2.670$** | 3.354 | 684 | 37,1% | 28,84 |
| **Total** | **Série Consolidada** | **655** | **143,9** | **138,3** | **$-3.908$** | **6.270** | **10.178** | **57,3%** | **27,78** |

*Fonte: Dados da pesquisa (2026). Nota: Médias e totais de excesso e déficit são expressos em refeições. Sobras potenciais e faltas potenciais correspondem à soma das diferenças positivas diárias entre planejamento e consumo registrado (max(0, Planejado - Consumo) e max(0, Consumo - Planejado)). Esses indicadores representam grandezas teóricas de planejamento operacional e não constituem medições físicas de descarte de alimentos ou contagem de estudantes desassistidos.*

Os dados da **Tabela 1** revelam a magnitude dos desvios operacionais. Em 2023, o saldo anual indicava um excedente de apenas $+742$ refeições em 181 datas, o que aparentava estabilidade (diferença média de apenas quatro refeições por dia). Entretanto, a apuração diária evidenciou que ocorreram 1.916 refeições em sobras potenciais e 1.174 refeições em falta. Nos anos seguintes, com a ruptura das reservas discentes, as faltas acumuladas dispararam para 4.524 refeições em 2024 e 3.796 em 2025, justificando a alteração de sistemática em 2026.

Para visualizar o contraste entre o saldo líquido aparente e os desvios diários potenciais em cada ano letivo, a **Figura 1** apresenta essa decomposição comparativa.

![Figura 1 - Decomposição do efeito compensatório](file:///f:/PROJETOS/ARTEFATO/reports/figuras/07_efeito_compensatorio_e_regimes/fig57_efeito_compensatorio_saldo_vs_realidade_diaria.png)
*Figura 1 — Comparação entre o saldo anual aparente e os totais acumulados de sobras e faltas diárias (2023 a 2026).*  
*Fonte: Dados da pesquisa (2026).*

A análise da **Figura 1** evidencia como o saldo anual (linha cinza tracejada) mascara as oscilações cotidianas. No painel de 2023, observa-se que a proximidade do saldo com o eixo zero resulta da anulação aritmética entre picos positivos de sobras e vales de falta. Já nos anos de 2024 e 2025, o colapso das reservas empurra a curva para patamares fortemente negativos de déficit contínuo. Em 2026, com o quantitativo da nutricionista, a curva inverte-se para o quadrante positivo superior, indicando acúmulo contínuo de sobras.

Complementando esse diagnóstico, a **Figura 2** quantifica o volume acumulado de desvios absolutos divididos entre sobras e faltas em cada exercício escolar.

![Figura 2 - Painel anual de sobras e faltas acumuladas](file:///f:/PROJETOS/ARTEFATO/reports/figuras/01_analise_exploratoria/fig06_painel_anual_saldo_falta_sobra.png)
*Figura 2 — Totais anuais de sobras potenciais e faltas potenciais calculadas por data.*  
*Fonte: Dados da pesquisa (2026).*

Como demonstrado na **Figura 2**, o volume total de ineficiência operacional (calculado pela soma das barras de sobras e faltas) manteve-se expressivo em todos os períodos. Em 2024, a ineficiência concentrou-se quase integralmente em faltas (4.524 refeições). Já em 2026, o descompasso concentrou-se em sobras potenciais (3.354 refeições). O gráfico comprova que nenhum dos métodos manuais anteriores conseguiu manter sobras e faltas simultaneamente em patamares baixos.

### 5.2.2 Resultados do Período de Reservas dos Estudantes (2023 a 2025)

Entre 2023 e 2025, o planejamento das refeições dependia do preenchimento voluntário de formulários eletrônicos pelos alunos. Os resultados quantitativos comprovam que esse mecanismo apresentou descontinuidade funcional ao longo do tempo:
- Em **2023**, a taxa de dias com déficit potencial situou-se em $38,1\%$, com erro médio absoluto de 17,07 refeições/dia;
- Em **2024**, o consumo diário médio cresceu para 167,3 refeições, enquanto as reservas médias registraram 132,9. Esse descompasso fez com que **82,8% dos dias letivos apresentassem falta de refeições reservadas**, acumulando 4.524 refeições em déficit e elevando o MAE para 39,82 refeições diárias;
- Em **2025**, a situação manteve-se desfavorável: em **78,7% dos dias letivos** o consumo registrado superou as reservas preenchidas, gerando 3.796 refeições em déficit potencial e MAE de 28,79 refeições/dia.

Esse comportamento decorreu do fenômeno de fadiga de preenchimento: os estudantes deixavam de acessar os formulários, mas compareciam ao refeitório no horário do almoço. Como o regimento escolar e os princípios de assistência estudantil impedem negar a alimentação aos alunos presentes, a cozinha recorria a ajustes emergenciais de porções, comprometendo o padrão do serviço.

### 5.2.3 Resultados da Transição para o Quantitativo da Nutricionista (2026)

Em fevereiro de 2026, a gestão do campus extinguiu a obrigatoriedade dos formulários discentes, transferindo a fixação das quantidades para a nutricionista responsável. A profissional passou a estipular semanalmente um volume diário fixo para o preparo.

A **Figura 3** exibe as curvas de densidade de probabilidade dos erros diários ($y_{\text{real}} - \hat{y}$) para os dois períodos de gestão.

![Figura 3 - Distribuição dos erros diários por período](file:///f:/PROJETOS/ARTEFATO/reports/figuras/07_efeito_compensatorio_e_regimes/fig58_distribuicao_erros_diarios_por_regime.png)
*Figura 3 — Curvas de densidade dos erros diários de planejamento: período dos alunos (2023–2025) vs. período da nutricionista (2026).*  
*Fonte: Dados da pesquisa (2026).*

A comparação empírica na **Figura 3** revela a alteração no padrão de desvios:
- No período discente (curva vermelha), a distribuição concentra-se em valores positivos ($y_{\text{real}} > \text{Reserva}$), refletindo subdimensionamento crônico e déficits sistemáticos;
- No período da nutricionista (curva azul), a distribuição inverteu o sinal, deslocando-se para valores negativos ($y_{\text{real}} < \text{Planejado}$). Ciente das consequências da falta de comida, a nutricionista adotou uma conduta de **superestimativa preventiva** (média de 186,2 refeições planejadas para 167,1 consumidas).

Esse procedimento conteve a taxa de dias com déficit potencial para $37,1\%$, mas resultou em **3.354 refeições em sobras potenciais em apenas 140 dias úteis de 2026**. Os dados comprovam que a gestão substituiu a desassistência alimentar pelo desperdício de insumos, justificando a intervenção de um sistema preditivo balanceado.

---

## 5.3 RESULTADOS DA ANÁLISE EXPLORATÓRIA DOS PADRÕES DE DEMANDA (EDA)

A análise exploratória da série temporal identificou os fatores exógenos e sazonais que governam a demanda de refeições, fornecendo a base para a seleção de preditores dos modelos de aprendizado de máquina.

### 5.3.1 Padrão Semanal e Rotina Pedagógica

A frequência discente ao refeitório exibe forte modulação pelo dia da semana. A **Figura 4** apresenta a síntese do comportamento diário do consumo consolidado.

![Figura 4 - Perfil semanal de consumo](file:///f:/PROJETOS/ARTEFATO/reports/figuras/01_analise_exploratoria/fig13_consumo_dia_semana_sintese.png)
*Figura 4 — Média e intervalo de variação do consumo de refeições por dia da semana (2023 a 2026).*  
*Fonte: Dados da pesquisa (2026).*

A leitura da **Figura 4** revela uma assimetria estrutural marcante entre os dias úteis:
- Terças e quartas-feiras concentram os maiores volumes de almoço servido, com médias de 168 e 172 refeições diárias e menor dispersão relativa;
- Segundas e quintas-feiras registram patamares intermediários de presença (médias próximas de 152 refeições);
- As sextas-feiras exibem uma retração acentuada, com média de apenas **124 refeições diárias** — um volume **$28\%$ inferior ao registrado nas quartas-feiras**.

Para verificar se essa retração na sexta-feira constituiu um fenômeno pontual ou uma característica estável ao longo do tempo, a **Figura 5** decompõe a série temporal semanal ano a ano.

![Figura 5 - Perfil semanal por ano letivo](file:///f:/PROJETOS/ARTEFATO/reports/figuras/01_analise_exploratoria/fig10_sazonalidade_semanal_por_ano.png)
*Figura 5 — Comportamento do consumo por dia da semana nos anos de 2023, 2024, 2025 e 2026.*  
*Fonte: Dados da pesquisa (2026).*

A análise da **Figura 5** confirma que o perfil semanal é recorrente nos quatro anos estudados ($p < 0{,}001$, ANOVA). Em todos os exercícios escolares, a sexta-feira registrou a menor média e a menor mediana de consumo. Esse comportamento decorre da organização curricular dos cursos técnicos integrados ao ensino médio, que concentram disciplinas práticas no meio da semana e liberam parcelas de turmas no turno da tarde das sextas-feiras. A ausência de ajuste dessa sazonalidade no planejamento empírico manual respondia pela maior parcela dos sobras potenciais no fim da semana.

### 5.3.2 Influência do Cardápio: Tipo de Proteína e Método de Cocção

O comparecimento voluntário dos estudantes responde de maneira mensurável à composição do prato principal. A **Figura 6** confronta a frequência de oferta de cada grupo proteico com o consumo médio verificado.

![Figura 6 - Oferta e consumo por tipo de proteína](file:///f:/PROJETOS/ARTEFATO/reports/figuras/01_analise_exploratoria/fig16_frequencia_vs_consumo_proteina.png)
*Figura 6 — Relação entre a quantidade de ofertas no período e o consumo médio por grupo de proteína.*  
*Fonte: Dados da pesquisa (2026).*

Os resultados da **Figura 6** comprovam que pratos com carne bovina e feijoada tradicional alcançam médias estatisticamente superiores (165 a 178 refeições), atuando como fatores atratores de presença discente. Em contrapartida, dias com oferta de peixe, ovos ou carne suína ensopada registram médias inferiores (125 a 138 refeições). O gráfico evidencia que a preferência alimentar dos estudantes exerce papel decisivo na variação diária de demanda.

Complementando a composição nutricional, a **Figura 7** examina a influência da técnica de preparo culinário sobre a demanda registrada.

![Figura 7 - Consumo conforme técnica de preparo](file:///f:/PROJETOS/ARTEFATO/reports/figuras/01_analise_exploratoria/fig17_consumo_por_tecnica_preparo.png)
*Figura 7 — Consumo médio por método culinário (assado, grelhado, ensopado e fritura).*  
*Fonte: Dados da pesquisa (2026).*

Na **Figura 7**, constata-se que preparações assadas ou grelhadas apresentam médias de presença superiores às preparações ensopadas ou com molho abundante. As preparações assadas alcançam média de 154 refeições com menor variabilidade interquartil, enquanto ensopados apresentam média de 141 refeições com maior frequência de dias atípicos de baixa adesão. Esse resultado indica que a inclusão dos métodos culinários agrega poder discriminatório aos modelos preditivos.

### 5.3.3 Variações Decorrentes de Condições Meteorológicas

A localização do campus impõe que parcela significativa dos estudantes realize deslocamentos a pé da estação de transporte público até a escola. A **Figura 8** mensura a sensibilidade da demanda diária em função das faixas de chuva acumulada.

![Figura 8 - Consumo por faixa de precipitação](file:///f:/PROJETOS/ARTEFATO/reports/figuras/01_analise_exploratoria/fig20_consumo_por_faixa_chuva.png)
*Figura 8 — Média de refeições servidas conforme faixas de chuva acumulada no dia.*  
*Fonte: Dados da pesquisa (2026).*

A **Figura 8** demonstra que dias com precipitação superior a $15\text{ mm}$ provocam uma retração média de 14 a 22 refeições em relação a dias secos sob condições de calendário comparáveis. Precipitações elevadas afetam o deslocamento nas vias de acesso não pavimentadas próximas à escola, elevando o absenteísmo nas aulas do contraturno.

Avaliando a dimensão térmica, a **Figura 9** apresenta a dispersão do consumo em função da temperatura máxima observada em cada data letiva.

![Figura 9 - Relação entre temperatura máxima e consumo](file:///f:/PROJETOS/ARTEFATO/reports/figuras/01_analise_exploratoria/fig22_temperatura_clima_bivariada.png)
*Figura 9 — Dispersão do consumo diário em função da temperatura máxima observada (°C).*  
*Fonte: Dados da pesquisa (2026).*

Na **Figura 9**, a curva de ajuste não-linear (Loess) revela que tanto temperaturas muito frias (máximas inferiores a $16^\circ\text{C}$ nas manhãs de inverno) quanto temperaturas muito elevadas (superiores a $31^\circ\text{C}$) correlacionam-se com menor comparecimento ao almoço. A faixa de maior regularidade situa-se entre $20^\circ\text{C}$ e $26^\circ\text{C}$, confirmando a relevância da inclusão de preditores térmicos nos algoritmos.

### 5.3.4 Efeito Memória e Autocorrelação Temporal

A persistência inercial na série de refeições foi avaliada por meio das funções de autocorrelação simples (ACF) e parcial (PACF), dispostas na **Figura 10**.

![Figura 10 - Funções de autocorrelação temporal](file:///f:/PROJETOS/ARTEFATO/reports/figuras/01_analise_exploratoria/fig25_autocorrelacao_memoria_temporal.png)
*Figura 10 — Autocorrelação simples (ACF) e parcial (PACF) da série diária de consumo de refeições.*  
*Fonte: Dados da pesquisa (2026).*

Os correlogramas da **Figura 10** revelam picos positivos estatisticamente significativos nos atrasos de 5 e 10 dias úteis ($k=5$ e $k=10$, com $p < 0{,}01$). Esse resultado ratifica a dinâmica de ciclo semanal: a demanda de uma determinada terça-feira é primariamente explicada pelo consumo da terça-feira da semana anterior ($lag_5$) e pelo consumo de duas semanas antes ($lag_{10}$). Essa constatação fundamentou a inclusão das variáveis defasadas de mesma periodicidade semanal como entradas prioritárias nos modelos.

---

## 5.4 RESULTADOS DA SELEÇÃO DE ATRIBUTOS NA CAMADA GOLD

Com base nos achados da análise exploratória, avaliou-se empiricamente a importância preditiva de cada uma das variáveis construídas na Camada Gold. A **Figura 11** apresenta o ranqueamento dos atributos por decréscimo de impureza em modelos de árvores de decisão (*Random Forest* - MDI).

![Figura 11 - Ranquear de importância de atributos](file:///f:/PROJETOS/ARTEFATO/reports/figuras/02_engenharia_features/fig27_random_forest_importance.png)
*Figura 11 — Importância relativa dos 15 principais atributos na estimativa do consumo (Random Forest).*  
*Fonte: Dados da pesquisa (2026).*

A análise da **Figura 11** aponta que as variáveis de memória recente (`consumo_lag_5` e `consumo_lag_10`) lideram com folga a importância relativa, concentrando mais de $35\%$ da contribuição preditiva global. A indicadora de sexta-feira (`is_sexta`) aparece em terceiro lugar, confirmando a necessidade de reajuste para baixo na estimativa do último dia da semana. As variáveis de proteína bovina e precipitação pluvial completam o núcleo de variáveis preditivas mais relevantes.

Para confrontar esse ranqueamento com uma métrica paramétrica linear, a **Figura 12** expõe os coeficientes de correlação de Pearson de cada atributo com o consumo efetivo.

![Figura 12 - Correlação de atributos com o consumo](file:///f:/PROJETOS/ARTEFATO/reports/figuras/02_engenharia_features/fig26_ranking_correlacao_features_gold.png)
*Figura 12 — Coeficiente de correlação linear de Pearson entre as variáveis preditivas e o consumo.*  
*Fonte: Dados da pesquisa (2026).*

A **Figura 12** corrobora o papel das defasagens temporais, que apresentam correlação linear positiva acima de $0{,}65$ com o consumo. Em contrapartida, a variável binária indicadora de sexta-feira exibe correlação negativa expressiva ($-0{,}38$), atestando quantitativamente a retração de presença no fim de semana letivo. Os dados climáticos de chuva acumulada e temperatura máxima apresentam correlações negativas moderadas, ratificando a relevância de sua retenção no banco Gold.

---

## 5.5 RESULTADOS DO TORNEIO DE MODELOS NAS JANELAS OPERACIONAIS

### 5.5.1 Metodologia Experimental da Validação Temporal Walk-Forward

Para assegurar validade científica aos testes sem vazamento temporal (*data leakage*), aplicou-se a metodologia de **Validação Temporal Sequencial (*Walk-Forward Validation*)** (Tashman, 2000; Hyndman & Athanasopoulos, 2021).

O experimento reproduziu exatamente o processo decisório ao longo de 28 semanas do período letivo de 2026 (fevereiro a agosto, totalizando 140 datas de teste). A cada sexta-feira de corte da semana $T$, os modelos foram reajustados exclusivamente com o histórico anterior, gerando previsões para dois horizontes de decisão da gestão escolar:
1. **Horizonte $t+2$ (Compras com 14 dias de antecedência)**: Previsão calculada com duas semanas de antecedência para aquisição de gêneros não perecíveis. Nesse prazo, os algoritmos operam de maneira autônoma, sem estimativa humana ou cardápio definitivo;
2. **Horizonte $t+1$ (Preparo com 7 dias de antecedência)**: Previsão atualizada na sexta-feira imediatamente anterior à semana de fornecimento, incorporando o cardápio definido e a estimativa institucional da nutricionista.

Testaram-se três cenários experimentais de enriquecimento de atributos:
- **Cenário 1 (Linha de Base)**: Variáveis de calendário escolar e defasagens de consumo;
- **Cenário 2 (Com Clima)**: Calendário, defasagens e variáveis meteorológicas previstas;
- **Cenário 3 (Com Planejamento Humano)**: Calendário, defasagens, clima e o quantitativo informado pela nutricionista.

### 5.5.2 Resultados Comparativos entre Cenários e Horizontes

A **Tabela 2** sintetiza os desempenhos obtidos nos dois horizontes operacionais e nos três cenários de informação.

#### Tabela 2 — Desempenho preditivo conforme cenário de informação e horizonte de planejamento (2026)

| Horizonte de decisão | Cenário de informação avaliado | Modelo com menor erro | MAE (ref/dia) | RMSE (ref/dia) | $R^2$ | WAPE (%) | Ganho MAE vs. Cenário 1 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **$t+2$ (14 dias antes)** | **Cenário 1:** Histórico e calendário | Regressão Linear | 29,48 | 39,41 | 0,229 | 17,6% | Linha de Base |
| **$t+2$ (14 dias antes)** | **Cenário 2:** Histórico + Calendário + Clima | Regressão Linear | **28,67** | **38,64** | **0,268** | **17,2%** | **$-2,7\%$** |
| **$t+1$ (7 dias antes)** | **Cenário 1:** Histórico e calendário | Ridge | 25,12 | 34,70 | 0,402 | 15,0% | Linha de Base |
| **$t+1$ (7 dias antes)** | **Cenário 2:** Histórico + Calendário + Clima | CatBoost | 24,80 | 34,18 | 0,419 | 14,8% | $-1,3\%$ |
| **$t+1$ (7 dias antes)** | **Cenário 3:** Histórico + Clima + Nutricionista | **Lasso** | **22,27** | **32,33** | **0,498** | **13,3%** | **$-11,3\%$** |

*Fonte: Dados da pesquisa (2026).*

A evolução do erro médio absoluto (MAE) e da raiz do erro quadrático médio (RMSE) entre os três cenários é ilustrada na **Figura 13**.

![Figura 13 - Desempenho comparativo por cenário de informação](file:///f:/PROJETOS/ARTEFATO/reports/figuras/03_modelagem_cenarios/fig36_comparativo_mae_rmse_cenarios.png)
*Figura 13 — Erro Médio Absoluto (MAE) e RMSE entre os três cenários de informação avaliados.*  
*Fonte: Dados da pesquisa (2026).*

Na **Figura 13**, observa-se o ganho monotônico de acurácia à medida que fontes adicionais de dados são incorporadas. No Cenário 1 (base restrita), o MAE parte de 29,48 refeições em $t+2$ e 25,12 em $t+1$. A introdução do clima (Cenário 2) e, em seguida, da estimativa da nutricionista (Cenário 3) reduz progressivamente o erro absoluto para a marca de 22,27 refeições diárias, comprovando a sinergia entre as variáveis heterogêneas.

Para detalhar o efeito exclusivo dos dados meteorológicos no planejamento de duas semanas de antecedência, a **Figura 14** isola o comportamento preditivo no horizonte $t+2$.

![Figura 14 - Impacto do clima no horizonte de compras](file:///f:/PROJETOS/ARTEFATO/reports/figuras/03_modelagem_cenarios/fig39_impacto_clima_horizonte_t2.png)
*Figura 14 — Diferença no erro médio com a adição de dados climáticos no horizonte t+2.*  
*Fonte: Dados da pesquisa (2026).*

A análise da **Figura 14** evidencia que, no horizonte autônomo de duas semanas ($t+2$), a incorporação das previsões meteorológicas reduziu o MAE para 28,67 refeições/dia e elevou o coeficiente de determinação ($R^2$) de 0,229 para 0,268. Como as compras programadas com 14 dias de antecedência atendem a itens de despensa com estocagem estável, esse nível de erro viabiliza pedidos antecipados seguros.

Em seguida, a **Figura 15** avalia o ganho de precisão obtido na passagem da estimativa de compras antecipadas ($t+2$) para a estimativa de preparo imediato ($t+1$).

![Figura 15 - Ganho de acurácia entre as janelas de decisão](file:///f:/PROJETOS/ARTEFATO/reports/figuras/03_modelagem_cenarios/fig40_ganho_reforecast_t2_para_t1.png)
*Figura 15 — Comparação de precisão entre a estimativa de compras (t+2) e a estimativa de preparo (t+1).*  
*Fonte: Dados da pesquisa (2026).*

Como demonstrado na **Figura 15**, a reavaliação (*reforecast*) das previsões na sexta-feira imediatamente anterior à semana de fornecimento gerou um ganho de precisão de **$22,3\%$**, reduzindo o MAE de 28,67 para 22,27 refeições por dia. Esse salto qualitativo decorre da absorção dos dados finais de cardápio e da estimativa humana no horizonte curto.

### 5.5.3 Ranking do Torneio de Algoritmos vs. Benchmark da Nutricionista ($t+1$)

A **Tabela 3** confronta os métodos preditivos avaliados no horizonte de preparo ($t+1$) com a estimativa da nutricionista.

#### Tabela 3 — Desempenho dos modelos preditivos e da referência da nutricionista ($t+1$)

| Modelo avaliado | Família metodológica | MAE (ref/dia) | RMSE (ref/dia) | $R^2$ | WAPE (%) | Sobras potenciais (ref) | Faltas potenciais (ref) | Dias com falta (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Lasso** | Modelo linear regularizado L1 | **22,27** | **32,33** | **0,498** | **13,3%** | **1.107** | 741 | 43,4% |
| **Ridge** | Modelo linear regularizado L2 | **22,46** | **32,82** | **0,483** | **13,4%** | **1.161** | 703 | 43,4% |
| **Regressão Linear** | Mínimos quadrados (OLS) | 22,87 | 32,56 | 0,491 | 13,7% | 916 | 981 | 49,4% |
| **CatBoost** | Árvores com gradiente (*boosting*) | 24,05 | 33,65 | 0,442 | 14,4% | 1.155 | 841 | 45,8% |
| **LightGBM** | Árvores com gradiente (*boosting*) | 24,28 | 33,90 | 0,432 | 14,5% | 1.203 | 812 | 47,0% |
| **Random Forest** | Conjunto de árvores (*bagging*) | 24,62 | 34,22 | 0,421 | 14,7% | 1.189 | 854 | 48,2% |
| **Nutricionista (Referência)** | Planejamento empírico humano | **24,92** | **36,94** | **0,373** | **14,9%** | **2.705** | **684** | **37,1%** |

*Fonte: Dados da pesquisa (2026). Nota: Sobras e faltas são grandezas potenciais calculadas a partir das diferenças diárias em relação ao planejamento (max(0, Planejado - Consumo) e max(0, Consumo - Planejado)) e não representam pesagens físicas de descarte ou contagem de pessoas desassistidas.*

A comparação visual das métricas de erro entre os algoritmos de aprendizado de máquina e o planejamento humano é exposta na **Figura 16**.

![Figura 16 - Comparação entre modelos preditivos e nutricionista](file:///f:/PROJETOS/ARTEFATO/reports/figuras/04_top_modelos_confronto/fig46_top5_comparativo_confronto_reservas.png)
*Figura 16 — Erro médio absoluto (MAE) dos modelos preditivos e da referência da nutricionista.*  
*Fonte: Dados da pesquisa (2026).*

A **Figura 16** destaca que os modelos lineares regularizados (**Lasso** e **Ridge**) superaram o benchmark humano da servidora pública em **$10,6\%$ de acurácia** (MAE de 22,27 contra 24,92 da nutricionista) e em **$12,5\%$ em RMSE** (32,33 contra 36,94). Modelos de gradiente boosting (*CatBoost* e *LightGBM*) também superaram a estimativa humana, mas apresentaram dispersão ligeiramente superior aos lineares regularizados, comportamento esperado em tabelas com cerca de 655 registros.

Avaliando a direção prática desses desvios, a **Figura 17** apresenta o balanço de sobras e faltas acumuladas por cada alternativa no teste de 2026.

![Figura 17 - Sobras e faltas potenciais dos modelos preditivos](file:///f:/PROJETOS/ARTEFATO/reports/figuras/04_top_modelos_confronto/fig48_top5_balanco_sobra_falta_ordenado.png)
*Figura 17 — Balanço de sobras potenciais e faltas potenciais acumuladas em 2026.*  
*Fonte: Dados da pesquisa (2026).*

A leitura da **Figura 17** evidencia o ganho de eficiência dos modelos: o Lasso **eliminou 1.598 refeições em sobras desnecessárias** em relação à nutricionista (reduzindo de 2.705 para 1.107 refeições excedentes, ou uma queda de $59\%$ no desperdício potencial). Por outro lado, como o modelo otimiza uma função de perda simétrica, o volume de faltas aumentou de 684 para 741 refeições, motivando a criação de mecanismos de margem de proteção.

A **Figura 18** exibe a aderência temporal da curva preditiva do modelo Ridge em comparação ao consumo real ao longo das 28 semanas de 2026.

![Figura 18 - Previsões do modelo e consumo real em 2026](file:///f:/PROJETOS/ARTEFATO/reports/figuras/03_modelagem_cenarios/fig42_serie_teste_2026_previsoes_vs_real.png)
*Figura 18 — Série temporal diária das estimativas geradas pelo modelo Ridge e do consumo registrado em 2026.*  
*Fonte: Dados da pesquisa (2026).*

Acompanhando a **Figura 18**, constata-se que a curva prevista pelo algoritmo acompanha de forma aderente os vales das sextas-feiras e os picos de terças e quartas, reduzindo as flutuações extremas de desvio observadas no planejamento empírico manual.

### 5.5.4 Comparação das Janelas Temporais de Treinamento e Deriva de Hábitos

Avaliou-se se os modelos deveriam ser treinados com todo o histórico acumulado (*Expanding Window*) ou apenas com dados letivos recentes (*Rolling Windows* móveis de 120 e 60 dias úteis). A **Figura 19** compara o desempenho preditivo dessas três abordagens de janela temporal.

![Figura 19 - Comparação entre janelas de treinamento](file:///f:/PROJETOS/ARTEFATO/reports/figuras/05_janelas_temporais_habitos/fig50_comparativo_janelas_expanding_vs_rolling.png)
*Figura 19 — Desempenho dos modelos conforme o tamanho da janela de dados de treinamento.*  
*Fonte: Dados da pesquisa (2026).*

Como demonstrado na **Figura 19**, a janela expansiva contínua apresentou maior estabilidade e menor MAE médio do que as janelas móveis restritas. Como o calendário letivo obedece a ciclos anuais recorrentes, o histórico amplo permitiu que os modelos absorvessem variações de início e fim de semestre letivo com maior consistência.

Para investigar eventuais alterações comportamentais de longo prazo no corpo discente, a **Figura 20** analisa a deriva temporal nos hábitos de frequência.

![Figura 20 - Variação histórica da taxa de absenteísmo](file:///f:/PROJETOS/ARTEFATO/reports/figuras/05_janelas_temporais_habitos/fig52_analise_deriva_habitos_estudantis.png)
*Figura 20 — Acompanhamento anual da relação entre reservas e comparecimento discente.*  
*Fonte: Dados da pesquisa (2026).*

A análise da **Figura 20** corrobora a estabilidade dos padrões de comparecimento entre 2023 e 2026, indicando que as variações observadas decorreram primordialmente de alterações nas regras de reserva e calendário acadêmico, e não de rupturas abruptas de comportamento discente que exigissem descarte do histórico pretérito.

---

## 5.6 RESULTADOS DAS POLÍTICAS DE DECISÃO OPERACIONAL E MARGENS DE SEGURANÇA

### 5.6.1 A Assimetria de Consequências na Alimentação Escolar

Embora os modelos preditivos tenham apresentado menor erro médio absoluto, métodos tradicionais de aprendizado de máquina tratam sobras e faltas com pesos equivalentes. Na prática de um refeitório público:
- **Custo do Excedente ($C_o$)**: Impacto financeiro do desperdício de insumos públicos;
- **Custo do Déficit ($C_u$)**: Grave impacto social — estudantes sem alimentação durante o turno escolar.

Por esse motivo, avaliaram-se duas políticas operacionais: a combinação colaborativa e o dimensionamento de margens prudenciais.

### 5.6.2 Resultados da Fronteira Eficiente de Pareto do Modelo Híbrido

Em alinhamento com a literatura de previsão colaborativa (Blattberg & Hoch, 1990; Armstrong, 2001), avaliou-se a combinação linear entre a estimativa da IA e a da nutricionista:
$$\hat{y}_{\text{híbrido}}(\alpha) = \alpha \cdot \hat{y}_{\text{IA}} + (1 - \alpha) \cdot \text{Planejado}_{\text{Nutricionista}}$$

A varredura contínua de $\alpha \in [0; 1]$ gerou a **Fronteira Eficiente de Pareto**, ilustrada na **Figura 21**.

![Figura 21 - Fronteira de equilíbrio do modelo híbrido](file:///f:/PROJETOS/ARTEFATO/reports/figuras/06_margens_seguranca_e_modelo_hibrido/fig53_fronteira_pareto_modelo_hibrido.png)
*Figura 21 — Trade-off entre sobras potenciais e faltas potenciais na combinação entre IA e nutricionista.*  
*Fonte: Dados da pesquisa (2026).*

Os resultados empíricos da **Figura 21** ratificam a hipótese colaborativa: a ponderação de mínimo arrependimento ocorre exatamente em **$\alpha = 0{,}50$ (50% IA + 50% Nutricionista)**:
- O total de faltas potenciais caiu para **489 refeições**, superando tanto a IA pura (741 faltas) quanto a nutricionista isolada (518 faltas);
- As sobras potenciais situaram-se em **1.289 refeições**, volume expressivamente inferior ao da servidora (2.705 refeições);
- O MAE diário atingiu **21,43 refeições/dia**, constituindo a melhor performance global de toda a pesquisa.

Esse fenômeno decorre da complementaridade: o algoritmo corrige a tendência de superestimativa sistemática, enquanto a servidora absorve nuances qualitativas do cotidiano escolar.

### 5.6.3 Resultados das Margens Prudenciais via Predição Conformal

Para fornecer garantia estatística finita contra dias de déficit sem assumir premissas de normalidade gaussiana, aplicou-se a teoria da **Predição Conformal Não-Paramétrica** (*Conformal Prediction*) (Vovk et al., 2005; Angelopoulos & Bates, 2021).

A margem prudencial $\Delta$ foi calculada diretamente sobre os quantis empíricos da distribuição de resíduos de subestimação positiva $e_i = \max(0, y_{\text{real}, i} - \hat{y}_{\text{pred}, i})$:
- **Quantil $P75$**: $+9{,}58$ refeições $\rightarrow$ **Margem moderada de $+10$ refeições**;
- **Quantil $P85$**: $+18{,}76$ refeições $\rightarrow$ **Margem prudencial de $+19$ refeições**;
- **Quantil $P90$**: $+28{,}67$ refeições $\rightarrow$ **Margem conservadora de $+29$ refeições**.

A **Tabela 4** resume os resultados operacionais dessas políticas.

#### Tabela 4 — Avaliação das políticas operacionais com margem de segurança (2026)

| Política de decisão avaliada | Margem adicional aplicada | Sobras potenciais (ref) | Faltas potenciais (ref) | Dias com falta (%) | MAE diário (ref/dia) | Observação de uso gerencial |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **1. IA Pura (Lasso/Ridge)** | Nenhuma | **1.107** | 741 | 43,4% | **22,27** | Menor erro médio simétrico; mantém risco moderado de dias com déficit potencial. |
| **2. IA + Conformal P75** | **$+10$ ref** | 1.749 | 383 | 25,3% | 25,70 | **Margem moderada (+10):** Reduz faltas para 383 refeições; cobertura de 74,7%. |
| **3. IA + Conformal P85** | **$+19$ ref** | 2.502 | 196 | **15,7%** | 31,34 | **Margem recomendada para IA pura:** Reduz dias com déficit potencial para 15,7% das datas. |
| **4. IA + Conformal P90** | $+29$ ref | 3.332 | 92 | 7,2% | 38,20 | Proteção elevada; eleva as sobras para patamar próximo ao da nutricionista. |
| **5. Híbrido 50/50 Puro** | Nenhuma | **1.289** | **489** | 43,4% | **21,43** | Menor erro médio absoluto global sem margem adicional. |
| **6. Híbrido + Margem Residual P85** | **$+12$ ref** | 1.994 | **199** | **16,9%** | 26,43 | **Política recomendada para preparo:** Reduz faltas a 199 refeições mantendo sobras controladas. |
| **7. Nutricionista (Referência)** | Empírica | 2.705 | 684 | 37,1% | 24,92 | Prática vigente em 2026; garante atendimento, mas com maior volume de sobras. |

*Fonte: Dados da pesquisa (2026). Nota: As sobras e faltas são grandezas potenciais calculadas a partir das diferenças diárias em relação ao planejamento sob função de perda assimétrica (max(0, Planejado - Consumo) e max(0, Consumo - Planejado)), não constituindo pesagem de descarte físico ou contagem de estudantes desassistidos.*

A visualização do impacto dessas margens sobre as sobras e a frequência de dias com déficit potencial é apresentada na **Figura 22**.

![Figura 22 - Efeito das margens de segurança conformal](file:///f:/PROJETOS/ARTEFATO/reports/figuras/06_margens_seguranca_e_modelo_hibrido/fig54_impacto_margens_seguranca_conformal.png)
*Figura 22 — Volume de sobras potenciais e percentual de dias com déficit potencial conforme a margem adotada.*  
*Fonte: Dados da pesquisa (2026).*

A análise da **Figura 22** e da **Tabela 4** elucida a função da **margem moderada de $+10$ refeições**:
- Ela corresponde empiricamente ao **Quantil P75** dos desvios, reduzindo os dias com déficit potencial de $43,4\%$ para $25,3\%$;
- Na IA Pura, a margem que garante cobertura de cerca de $85\%$ das datas é a de **$+19$ refeições (P85)**;
- No caso do **modelo híbrido (50% IA + 50% nutricionista)**, como a previsão combinada já é mais acurada, a margem residual necessária para alcançar nível de serviço similar é de apenas **$+12$ refeições**, totalizando apenas 199 refeições em falta no período com sobras substancialmente inferiores às da nutricionista.

Para simular o comportamento estocástico dessas faixas sob diferentes cenários de volatilidade da demanda, a **Figura 23** traz os resultados de simulações de Monte Carlo.

![Figura 23 - Simulação de faixas de risco operacional](file:///f:/PROJETOS/ARTEFATO/reports/figuras/06_margens_seguranca_e_modelo_hibrido/fig55_simulacao_monte_carlo_faixas_risco.png)
*Figura 23 — Intervalos de incerteza estocástica e limites de tolerância para apoio à decisão.*  
*Fonte: Dados da pesquisa (2026).*

Como demonstrado na **Figura 23**, a simulação probabilística evidencia que a aplicação das bandas conformais mantém a probabilidade de ruptura diária de estoque abaixo de $15\%$ mesmo diante de choques aleatórios de frequência discente.

---

## 5.7 SÍNTESE DOS RESULTADOS ECONÔMICOS, LIMITAÇÕES E PASSOS PARA A DEFESA FINAL

### 5.7.1 Comparação Geral das Alternativas de Decisão

A **Figura 24** apresenta a matriz de apoio à decisão gerencial, confrontando o custo financeiro estimado de sobras potenciais com a taxa de cobertura contra faltas, considerando o custo paramétrico de **R$ 8,50 por refeição servida**.

![Figura 24 - Comparativo entre custo de sobras e taxa de atendimento](file:///f:/PROJETOS/ARTEFATO/reports/figuras/06_margens_seguranca_e_modelo_hibrido/fig56_matriz_politicas_decisao_gestao.png)
*Figura 24 — Trade-off entre custo estimado de sobras potenciais (R$) e percentual de proteção contra déficits.*  
*Fonte: Dados da pesquisa (2026).*

A leitura da **Figura 24** sintetiza o trade-off gerencial: a prática da nutricionista isolada garante $62,9\%$ de dias sem falta, mas ao custo de quase R$ 23.000 em sobras acumuladas. A IA pura sem margem reduz o custo para menos de R$ 10.000, mas expõe a escola a risco de falta em $43,4\%$ dos dias. O modelo Híbrido com Margem P85 situa-se no quadrante ótimo superior, combinando custo moderado (R$ 16.949) e alta proteção social ($83,1\%$).

A **Tabela 5** consolida numericamente esses indicadores.

#### Tabela 5 — Síntese comparativa das alternativas de gestão da produção de refeições

| Alternativa avaliada | Origem da estimativa | Sobras acumuladas (ref) | Faltas acumuladas (ref) | Dias com falta (%) | Custo estimado de sobras (R$) | Avaliação para a gestão da escola |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Reservas dos alunos** | Histórico (2023–2025) | 2.916 | **9.494** | **63,8%** | R$ 24.786,00 | Dificuldade de adesão; gerou déficits frequentes. |
| **Nutricionista isolada** | Prática atual (2026) | 2.705 | 684 | 37,1% | R$ 22.992,50 | Garante o atendimento, mas mantém volume elevado de sobras. |
| **IA Pura (Lasso)** | Modelo preditivo isolado | **1.107** | 741 | 43,4% | **R$ 9.409,50** | Menor custo com sobras, mas requer margem de segurança. |
| **Híbrido 50/50 Puro** | IA + Nutricionista | **1.289** | **489** | 43,4% | **R$ 10.956,50** | Menor erro médio absoluto; reduz desvios sem margem adicional. |
| **Híbrido + Margem P85** | **Alternativa recomendada** | **1.994** | **199** | **16,9%** | **R$ 16.949,00** | **Equilíbrio prático:** Reduz R$ 6.043 frente à nutricionista e cobre 83,1% dos dias. |

*Fonte: Dados da pesquisa (2026). Nota: Estimativas financeiras baseadas no valor paramétrico de R$ 8,50 por refeição sobre as sobras potenciais calculadas. Os desvios são grandezas teóricas de planejamento (max(0, Planejado - Consumo) e max(0, Consumo - Planejado)) e não medições físicas de descarte ou de estudantes desassistidos.*

Para unificar a trajetória longitudinal de todas as abordagens avaliadas ao longo da pesquisa, a **Figura 25** apresenta o confronto histórico consolidado.

![Figura 25 - Comparação histórica consolidada dos períodos e modelos](file:///f:/PROJETOS/ARTEFATO/reports/figuras/07_efeito_compensatorio_e_regimes/fig59_confronto_historico_alunos_nutri_ia_hibrido.png)
*Figura 25 — Confronto entre reservas discentes, quantitativo da nutricionista, IA pura e modelo híbrido.*  
*Fonte: Dados da pesquisa (2026).*

A **Figura 25** resume as três conclusões centrais do estudo:
1. O método baseado em reservas discentes voluntárias mostrou-se inviável no médio prazo, gerando acúmulo de dias com déficit potencial de refeições;
2. A transição para quantitativos fixados pela nutricionista conteve as faltas, porém resultou em volume expressivo de sobras potenciais (cerca de R$ 23.000 em 140 datas avaliadas);
3. A alternativa **Híbrida com Margem Residual (+12 refeições)** apresentou-se como a mais equilibrada para aplicação no campus, oferecendo uma economia estimada de aproximadamente **R$ 6.000** em relação à prática da nutricionista no período avaliado, com redução substancial dos dias com déficit potencial (de $37,1\%$ para $16,9\%$).

### 5.7.2 Limitações das Evidências Parciais e Próximos Passos

Os resultados discutidos neste documento correspondem à etapa de qualificação do mestrado profissional, cobrindo o histórico letivo até agosto de 2026. Como as análises foram conduzidas de forma retrospectiva sobre os dados coletados, identificam-se as seguintes etapas complementares para a conclusão do trabalho:
1. **Teste em amostra preservada (Hold-out de Setembro de 2026)**: Os dados do mês de setembro de 2026 foram mantidos sem consulta durante a fase de desenvolvimento, destinando-se a uma validação independente dos parâmetros calibrados;
2. **Acompanhamento prospectivo em ambiente real (Outubro e Novembro de 2026)**: Aplicação experimental do artefato no cotidiano da escola, fornecendo as sugestões semanais à nutricionista antes da realização dos pedidos e acompanhando a aderência das decisões;
3. **Avaliação da percepção de utilidade**: Realização de entrevistas com a equipe gestora com base no Modelo de Aceitação de Tecnologia (TAM) (Davis, 1989), avaliando facilidade de uso, clareza das informações e viabilidade de incorporação do artefato na rotina do refeitório.
