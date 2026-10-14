# Memorial Metodológico e Trajetória Evolutiva do Artefato Técnico

**Projeto:** Sistema de Apoio à Decisão Operacional para Previsão de Demanda de Refeições  
**Instituição:** Instituto Federal de Educação, Ciência e Tecnologia de São Paulo (IFSP) — Campus Itaquaquecetuba  
**Programa:** Mestrado Profissional em Educação Profissional e Tecnológica (ProfEPT / Linha de Gestão Pública)  
**Localização:** Pasta `docs/`  
**Data de Consolidação:** Outubro de 2026  

---

## 1. Visão Geral e Propósito do Artefato

O presente produto técnico foi concebido para solucionar um dos maiores dilemas de gestão pública no ambiente escolar e universitário: **como dimensionar a produção diária de refeições perecíveis de modo a evitar simultaneamente o desperdício de recursos orçamentários (Potencial de Sobra) e a desassistência de estudantes em situação de vulnerabilidade socioeconômica (Potencial de Falta)**.

No IFSP Campus Itaquaquecetuba, o serviço de alimentação coletiva atende centenas de estudantes dos cursos técnicos integrados, Proeja e graduações. Historicamente, a operação oscilava entre a subnotificação das reservas individuais e a superestimativa cautelar da gestão. Este artefato integra técnicas de **Ciência de Dados**, **Pesquisa Operacional**, **Machine Learning** e **Inteligência Artificial Centrada no Humano (*Human-in-the-Loop*)** para fornecer suporte quantitativo robusto à nutricionista e à direção do campus.

---

## 2. A Trajetória de Desenvolvimento: Fases e Marcos

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                LINHA DO TEMPO DO ARTEFATO TÉCNICO                               │
├─────────────────────┬──────────────────────────┬───────────────────────┬────────────────────────┤
│ FASE 1: FUNDAÇÃO    │ FASE 2: ENGENHARIA       │ FASE 3: EXPERIMENTOS  │ FASE 4: DECISÃO &      │
│                     │                          │                       │         CALIBRAÇÃO     │
│ • Coleta Clima API  │ • Camada Gold            │ • 11 Algoritmos de ML │ • Margens Conformal    │
│ • Camada Silver     │ • 60+ Features           │ • Ablation Study (1-3)│ • Modelo Híbrido 50/50 │
│ • Saneamento 23-26  │ • Lags e Calendário      │ • Walk-Forward t+1/t+2│ • Monte Carlo (P10-P95)│
│ • EDA Preliminar    │ • Scores de Cardápio     │ • Top Modelos vs Nutri│ • Efeito Compensatório │
└─────────────────────┴──────────────────────────┴───────────────────────┴────────────────────────┘
```

### Marco 1: Coleta e Integração Climática (`notebooks/01_coleta_clima_api.ipynb`)
* **Problema:** O clima em Itaquaquecetuba (chuvas torrenciais de verão, quedas bruscas de temperatura no outono/inverno paulista) impacta diretamente a mobilidade discente até a Estação de Trem da CPTM (Linha 12-Safira, a 500m do campus) e a permanência no contraturno escolar.
* **Solução:** Integração automatizada com a API Open-Meteo via coordenadas geográficas exatas do campus (Latitude -23.4864, Longitude -46.3486). Extração de séries diárias de precipitação (mm), horas de chuva, temperaturas máxima/mínima/média e rajadas de vento.
* **Resultado:** Camada de dados meteorológicos limpa e auditada para todo o período letivo de 2023 a 2026.

### Marco 2: Higienização e Camada Silver dos Registros de Atendimento (`notebooks/02_camada_silver_qualidade_dados.ipynb`)
* **Problema:** Planilhas históricas heterogêneas, duplicadas, com inconsistências de digitação, registros em dias não letivos, feriados móveis municipais e anotações manuais na coluna de observações.
* **Solução:** Construção da Camada Silver com padronização de datas ISO, normalização fonética e léxica do cardápio escolar, classificação dos pratos principais (proteínas e métodos de cocção) e separação clara dos regimes operacionais:
  * **2023 a 2025:** Regime de *Manifestação Prévia dos Alunos*;
  * **2026:** Regime de *Estimativa Institucional da Nutricionista*.
* **Resultado:** Base analítica fidedigna (`silver_fato_diaria.parquet`) com 655 registros letivos higienizados.

### Marco 3: Análise Exploratória e Diagnóstico de Padrões (`notebooks/03_analise_exploratoria_eda.ipynb`)
* **Problema:** Desconhecimento do comportamento intra-semanal e dos principais direcionadores da adesão às refeições.
* **Solução:** Elaboração de 25 figuras analíticas com resolução de 300 DPI, investigando sazonalidade mensal, curvas de consumo por dia da semana, dias de greve, impactos de pratos favoritos e influência de chuvas torrenciais.
* **Achados Centrais:** Identificação de que as sextas-feiras apresentam queda natural de consumo de cerca de 25% a 30%, e que pratos com alta atratividade (ex: feijoada, strogonoff) causam picos que sobrecarregavam a cozinha.

### Marco 4: Feature Store e Engenharia de Atributos (`notebooks/04_camada_gold_engenharia_features.ipynb`)
* **Problema:** Modelos de machine learning requerem variáveis numéricas e tabulares estruturadas para capturar padrões temporais complexos.
* **Solução:** Criação da Camada Gold com mais de 60 atributos distribuídos em 5 blocos funcionais:
  1. *Memória e Histórico Recente:* Consumos no mesmo dia da semana anterior e retrasada, médias móveis;
  2. *Calendário e Sazonalidade:* Dummies de dias úteis, semana do ano, transformações trigonométricas de Fourier/cíclicas;
  3. *Engenharia de Cardápio:* Categorização de proteínas (bovina, frango, suína, peixe) e modos de preparo;
  4. *Variáveis Meteorológicas:* Índices de adversidade climática e dias de chuva persistente;
  5. *Regime de Demanda:* Histórico de reservas dos alunos e estimativas da nutricionista.

### Marco 5: Modelagem Preditiva Multi-Estágio (`notebooks/05_modelagem_cenarios_e_algoritmos.ipynb`)
* **Problema:** A decisão de compras possui lead times diferentes: compras de secos ocorrem 14 dias antes ($t+2$), enquanto compras de hortifrúti/perecíveis ocorrem na semana anterior ($t+1$). Modelos tradicionais não refletem essa janela.
* **Solução:** Implementação da validação temporal estritamente sequencial (*Walk-Forward Validation*) simulando a decisão a cada sexta-feira de corte em 2026 ao longo de 28 semanas:
  * **Horizonte $t+2$ (Secos — 14 dias antes):** Previsão puramente autônoma (sem interferência humana);
  * **Horizonte $t+1$ (Perecíveis — 7 dias antes):** Previsão com a calibragem da estimativa institucional da nutricionista;
  * **Estudo de Ablação (3 Cenários):** Teste de 11 algoritmos (Regressão Linear, Ridge, Lasso, KNN, SVR, Decision Tree, Random Forest, Extra Trees, LightGBM, XGBoost, CatBoost e MLP) sob diferentes combinações de features.

### Marco 6: Avaliação Visual e Confronto de Modelos (`notebooks/06_avaliacao_visual_e_comparativo_modelos.ipynb`)
* **Problema:** Determinar o algoritmo campeão em termos de generalização e estabilidade.
* **Resultado:** Modelos lineares regularizados (destaque para **Ridge**) e ensembles baseados em árvores (**LightGBM**) demonstraram maior robustez para dados tabulares com amostras moderadas, superando o benchmark humano da nutricionista em erro médio absoluto (MAE de 22,9 contra 24,8).

### Marco 7: Experimentos com Janelas Temporais de Hábitos (`notebooks/07_experimentos_janelas_temporais_e_habitos.ipynb`)
* **Problema:** A demanda dos estudantes muda ao longo do semestre (provas, início de ano letivo, cansaço no final do período).
* **Solução:** Teste de janelas móveis de memória de curto (4 semanas), médio (12 semanas) e longo prazo (série completa).
* **Resultado:** A janela de médio prazo (8 a 12 semanas) e a ponderação exponencial apresentaram o melhor equilíbrio entre adaptação a novos hábitos e resistência a ruídos atípicos.

### Marco 8: Perda Assimétrica, Predição Conformal e Modelo Híbrido (`notebooks/08_margem_seguranca_e_modelo_hibrido.ipynb`)
* **Problema:** MAE e RMSE tratam faltas e sobras de forma idêntica. Mas na escola pública, a falta de comida ao estudante vulnerável é inadmissível.
* **Solução e Fundamentação:**
  * **Predição Conformal Não-Paramétrica (*Conformal Prediction*):** Cálculo de quantis empíricos $P75$, $P85$ e $P90$ garantindo cobertura estatística sem pressupor distribuição normal;
  * **Fronteira Eficiente de Pareto:** Otimização do peso $\alpha$ entre a IA e a nutricionista, comprovando empiricamente que a combinação 50% IA + 50% Nutricionista atinge o menor volume de faltas da pesquisa (489 refeições);
  * **Simulação de Monte Carlo:** 1.000 trajetórias estocásticas de estresse diário definindo cenários neutro ($P50$), prudencial ($P80$) e de pior caso ($P95$).

### Marco 9: Decomposição do Efeito Compensatório (`notebooks/09_analise_efeito_compensatorio_e_regimes.ipynb`)
* **Problema:** O saldo líquido acumulado em um ano esconde a ineficiência diária por cancelamento aritmético.
* **Solução:** Auditoria minuciosa dia a dia de 2023 a 2026:
  * Em 2023, o saldo anual parecia perfeito (+742 refeições), mas no dia a dia ocorreram 1.916 sobras e 1.174 faltas!
  * Em 2024 e 2025, os alunos não reservavam (82,8% de dias em falta).
  * Em 2026, a nutricionista superestimava preventivamente (60,7% de dias com sobras).
  * O **Modelo Híbrido do Artefato** estabiliza os desvios diários na faixa ideal de $\pm 15$ refeições.

---

## 3. Síntese dos Resultados Técnicos Alcançados

| Dimensão de Avaliação | Regime Anterior (Alunos 2023-2025) | Gestão Humana (Nutricionista 2026) | Algoritmo Puro (IA Ridge) | Artefato Híbrido Calibrado (50/50 + P85) |
| :--- | :---: | :---: | :---: | :---: |
| **Taxa de Dias com Falta** | 63,8% dos dias | 41,0% dos dias | 43,4% dos dias | **16,9% dos dias** *(Proteção de 83%)* |
| **Potencial de Sobras (Desperdício)** | 2.916 ref | 1.545 ref | **1.238 ref** | **1.994 ref** |
| **Erro Médio Diário (MAE)** | 27,1 ref/dia | 24,9 ref/dia | 23,0 ref/dia | **21,4 ref/dia** *(Menor da pesquisa)* |
| **Custo Anual de Sobras** | R$ 24.786,00 | R$ 13.132,50 | R$ 10.530,71 | R$ 16.952,79 |
| **Pior Falta em 1 Único Dia** | 133 ref | 58 ref | 87 ref | **47 ref** *(Melhor contenção de crise)* |

---

## 4. Estrutura de Pastas e Rastreabilidade do Projeto

* `dados/bronze/`: Planilhas originais brutas recebidas da gestão e registros brutos da API.
* `dados/silver/`: Tabelas saneadas e padronizadas em Parquet e CSV.
* `dados/gold/`: Feature store de modelagem e resultados das predições walk-forward.
* `notebooks/`: 9 cadernos Jupyter numerados sequencialmente, totalmente documentados e executáveis.
* `reports/figuras/`: 59 figuras em alta resolução (300 DPI) organizadas em 7 subpastas temáticas.
* `reports/tabelas/`: Arquivos tabulares em CSV e Parquet espelhados para importação em ferramentas BI.
* `docs/`: Catálogo de referências em normas ABNT, memorial teórico e trajetória evolutiva.

---

## 5. Auditoria Adversarial e Certificação de Quality Gates

Em outubro de 2026, foi conduzida uma auditoria adversarial rigorosa multidisciplinar (mobilizando diretrizes de Engenharia de Testes, Arquitetura de Banco de Dados, Segurança e Validação Estática) sobre todo o pipeline de dados e os 9 cadernos de experimentos:

1. **Eliminação de Target Leakage:** A codificação de atratividade de cardápio foi estritamente restringida aos dados históricos de treino (2023 a 2025), garantindo que a base de teste cego de 2026 permaneça 100% isolada e imaculada.
2. **Blindagem de Lags Temporais em Previsões Multi-Step:** As variáveis de defasagem utilizadas no horizonte semanal $t+1$ foram reancoradas na data de corte da sexta-feira $T$, garantindo que nenhuma medição intradiária futura seja consultada.
3. **Reprodutibilidade Integral:** Todos os 9 notebooks foram reexecutados sequencialmente de ponta a ponta, com código de retorno 0 e geração das 59 figuras oficiais em 300 DPI e tabelas em CSV/Parquet.
4. **Isolamento de Anomalias:** As anomalias severas decorrentes da greve federal de 2024 foram devidamente tratadas por meio de flags de controle na Camada Silver e Gold.
5. **Conformidade Terminológica:** Todo o texto e documentação utilizam a nomenclatura metodologicamente correta: **Potencial de Sobra**, **Potencial de Falta**, **Reserva dos Alunos** (2023-2025) e **Quantitativo da Nutricionista** (2026).

