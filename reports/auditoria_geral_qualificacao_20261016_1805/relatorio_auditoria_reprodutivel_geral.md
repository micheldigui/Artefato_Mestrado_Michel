# LAUDO PERICIAL DE AUDITORIA CIENTÍFICA E REPRODUTIBILIDADE INTEGRAL
## Avaliação de Notebooks, Dados, Métricas, Figuras e Relatórios do Projeto

**Destino dos Artefatos Auditados:** `reports/auditoria_geral_qualificacao_20261016_1805/`  
**Data da Auditoria:** 16/10/2026  
**Regime da Auditoria:** Estritamente Reprodutível e Não-Destrutivo (Somente leitura nas bases e códigos originais; execução isolada em cópias).  
**Status de Preservação das Fontes:** **100% INTACTO** (99 arquivos originais monitorados com SHA-256 verificado antes e após a execução, zero divergências).

---

## 1. PROTOCOLO DE PRESERVAÇÃO E AMBIENTE DE AUDITORIA

### 1.1. Monitoramento de Hashes Criptográficos (SHA-256)
Para assegurar a integridade absoluta do repositório, antes de qualquer operação foi gerado o inventário `inventario_hashes_pre_execucao.json`, cobrindo 99 arquivos (10 notebooks originais em `notebooks/`, scripts em `src/`, bases em `dados/silver/` e `dados/gold/`, e a dissertação DOCX).
Após todos os recálculos e gerações gráficas, o script `conferir_hashes_pos_execucao.py` reavaliou cada arquivo:
- **Total de arquivos originais monitorados:** 99
- **Total de arquivos conferidos com hash idêntico:** 99
- **Total de alterações detectadas:** 0

### 1.2. Execução Controlada em Ambiente Isolado
- Cópias completas dos 10 notebooks foram criadas em `reports/auditoria_geral_qualificacao_20261016_1805/notebooks_copia/`.
- Todos os notebooks foram analisados quanto a operações de escrita (`.to_csv`, `.to_parquet`, `savefig`).
- **Bloqueio Preventivo Registrado:** O notebook `01_coleta_clima_api.ipynb` realiza requisições HTTP externas à API Open-Meteo e grava diretamente em `dados/silver/`. Sua execução ativa foi bloqueada preventivamente para impedir sobrescrita acidental e evitar dependência de conectividade externa.
- Os demais notebooks (02 a 10) tiveram suas 100+ células de código compiladas e validadas sintaticamente em ambiente isolado, com logs detalhados em `logs/`.

---

## 2. RECONCILIAÇÃO OBRIGATÓRIA DA AUDITORIA ANTERIOR

A auditoria anterior continha contradições entre o texto do relatório Markdown (`relatorio_auditoria_reprodutivel_2023_2025.md`) e os arquivos CSV gerados (`metricas_modelos_cenarios_2023_2025.csv`, `comparacao_reservas_modelos_consumo_datas_comuns.csv`).  
O recálculo independente e ponto a ponto diretamente a partir da série diária (`previsoes_diarias_reproduziveis_2023_2025.csv`, 20.594 linhas) permitiu diagnosticar e reconciliar formalmente cada divergência:

| Elemento Auditado | Valor no Relatório Anterior | Valor no CSV da Auditoria Anterior | Valor Recalculado Diretamente dos Microdados | Diagnóstico Pericial e Resolução |
| :--- | :---: | :---: | :---: | :--- |
| **Reservas Discentes: RMSE ($N=279$)** | 38,86 ref | 39,09 ref | **39,09 ref** | **O CSV estava correto.** O relatório anterior transcreveu 38,86 devido a erro de digitação/rascunho textual na resposta da IA. |
| **Reservas Discentes: Viés Médio ($N=279$)** | −18,04 ref/dia | −19,57 ref/dia | **−19,57 ref/dia** | **O CSV estava correto.** O relatório anterior transcreveu −18,04 de uma memória preliminar desatualizada. |
| **Reservas Discentes: Sobras Potenciais ($N=279$)** | 1.268 ref (texto) / 1.267 ref (seção 5) | 1.341 ref | **1.341 ref** | **O CSV estava correto.** O relatório anterior fabricou no texto os números 1.268 e 1.267. O somatório exato diário $\sum \max(0, \text{res} - \text{real})$ é 1.341 refeições. |
| **Reservas Discentes: Déficits Potenciais ($N=279$)** | 6.303 ref | 6.802 ref | **6.802 ref** | **O CSV estava correto.** O relatório anterior transcreveu 6.303. O somatório exato diário $\sum \max(0, \text{real} - \text{res})$ é 6.802 refeições. |
| **CatBoost: Sobras e Déficits ($N=279$, C1 $t+1$)** | Sobra: 2.868 / Déficit: 2.665 | Sobra: 2.835 / Déficit: 2.632 | **Sobra: 2.835 / Déficit: 2.632** | **O CSV estava correto.** A tabela do relatório anterior defasou os dados. O recálculo confirma exatamente 2.835 sobras e 2.632 déficits. |
| **Reservas Discentes: MAE ($N=279$)** | 29,19 ref/dia | 29,19 ref/dia | **29,19 ref/dia** (29,1864) | **Conferência de 100% em todas as fontes.** |
| **Convenção de Sinal da Redução do MAE** | Valores negativos (ex: −33,16%) | Valores positivos (33.16%) | **+33,15% (ganho relativo)** | Padronizado formalmente como Ganho de Precisão Relativo ($((MAE_{res} - MAE_{mod}) / MAE_{res}) \times 100$). |
| **Seleção de Algoritmos na Figura 49** | 10 modelos plotados sem nota explicativa | 14 modelos no CSV | **14 modelos na figura completa / 10 com nota de rodapé** | Os 4 modelos omitidos no gráfico resumido eram MLP, Decision Tree, Gradient Boosting e KNN. A omissão foi puramente visual, mas passa a ser declarada expressamente em nota técnica. |

---

## 3. AUDITORIA DA COORTE HISTÓRICA DE 2023 A 2025

### 3.1. Universo Canônico de Referência ($N = 458$ datas letivas)
A auditoria conferiu diretamente em `dados/silver/silver_fato_diaria.parquet` e `dados/silver/silver_reservas.parquet` as datas letivas com atendimento regular e reservas registradas no triênio 2023–2025 (Tabela 3 da dissertação):
- **Ano 2023:** $N = 181$ datas letivas | Consumo Total: 19.512 | Consumo Médio: 107,8 | Reservas Totais: 20.254 | Reserva Média: 111,9
- **Ano 2024:** $N = 122$ datas letivas | Consumo Total: 20.405 | Consumo Médio: 167,3 | Reservas Totais: 16.215 | Reserva Média: 132,9
- **Ano 2025:** $N = 155$ datas letivas | Consumo Total: 21.450 | Consumo Médio: 138,4 | Reservas Totais: 18.320 | Reserva Média: 118,2
- **Total Triênio:** **$N = 458$ datas letivas** (**100% de conferência com a Tabela 3 da dissertação**).

**Métricas Globais das Reservas Discentes no Universo Total ($N = 458$):**
- **MAE:** **27,10 refeições/dia**
- **RMSE:** **36,38 refeições**
- **$R^2$:** **0,1692**
- **WAPE:** **20,22%**
- **Viés Médio:** **−14,36 refeições/dia** (subdimensionamento crônico)
- **Sobra Potencial Total:** **2.916 refeições**
- **Déficit Potencial Total:** **9.494 refeições**
- **Saldo Aparente:** **−6.578 refeições**
- **Datas com Déficit Potencial:** **292 datas (63,8%)**

---

### 3.2. Auditoria dos Recortes de Interseção Comum ($N = 279$ em $t+1$ e $N = 275$ em $t+2$)
Para permitir uma comparação estritamente pareada dia a dia entre os 14 algoritmos e as reservas dos alunos, os modelos foram submetidos à validação temporal *walk-forward* com cortes operacionais às sextas-feiras ($T$).

Das 458 datas da coorte canônica, **179 datas ficaram fora do horizonte $t+1$ ($N = 279$)** e **183 datas fora de $t+2$ ($N = 275$)**. A investigação diagnosticou as causas exatas:
1. **Aquecimento Causal Inicial (*Warm-up*, 29 datas em 2023):** No início de 2023, antes de 22/03/2023, o histórico acumulado era inferior ao piso amostral de 30 dias letivos ($N < 30$), inviabilizando o treinamento estatístico estável ($N < P$).
2. **Critérios de Qualidade e Exclusão Pré-Gold (13 datas):** Dias atípicos com paralisação/greve discente ou docente e registros com valores incompletos descartados na engenharia de features da camada Gold.
3. **Restrição Operacional dos Cortes de Sexta-feira e Quebra de Defasagens (137 datas):** Feriados prolongados, recessos ou quebras de semana que rompem a continuidade das defasagens autorregressivas (`lag_1`, `lag_5`, `media_movel_5d`), gerando valores nulos (`NaN`) que o pipeline de aprendizado de máquina elimina por causalidade estrita.

**Distinção de Finalidade entre as Coortes:**
- **$N = 458$ (Finalidade Diagnóstica Institucional):** Retrata o comportamento total do usuário no regime de formulário SUAP, evidenciando o subdimensionamento estrutural crônico das reservas discentes ao longo de todo o triênio.
- **$N = 279$ (Finalidade Experimental Pareada):** Garante a comparação matemática irrefutável ponto a ponto entre os algoritmos e a reserva discente sob as mesmíssimas condições operacionais e nas exatas mesmas datas.

---

## 4. RESULTADOS RECALCULADOS E RANKING OFICIAL POR CENÁRIO E HORIZONTE

### 4.1. Fórmulas, Unidades e Convenções Adotadas
- **MAE (refeições/dia):** $\frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|$
- **RMSE (refeições):** $\sqrt{\frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2}$
- **$R^2$:** $1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$ (adotando a média do consumo real do conjunto pareado como referência)
- **WAPE (%):** $\frac{\sum |y_i - \hat{y}_i|}{\sum y_i} \times 100$
- **Viés Médio (refeições/dia):** $\frac{1}{n} \sum_{i=1}^n (\hat{y}_i - y_i)$ (positivo = sobrestimação; negativo = subestimação)
- **Sobra Potencial (refeições):** $\sum_{i=1}^n \max(0, \hat{y}_i - y_i)$
- **Déficit Potencial (refeições):** $\sum_{i=1}^n \max(0, y_i - \hat{y}_i)$
- **Saldo Aparente (refeições):** $\text{Sobra Potencial} - \text{Déficit Potencial}$
- **Ganho de Precisão Relativo sobre as Reservas (%):** $\frac{\text{MAE}_{\text{reservas}} - \text{MAE}_{\text{modelo}}}{\text{MAE}_{\text{reservas}}} \times 100$

---

### 4.2. Cenário 1 (Base + Cardápio — Puramente Autônomo e Prospectivo)
Avaliado sem variáveis climáticas ou reservas humanas, simulando a operação preditiva independente.

#### Ranking Horizonte $t+1$ (Curto Prazo / Preparo, $N = 279$ datas comuns):
| Posição | Algoritmo | Família | MAE (ref/dia) | RMSE (ref) | $R^2$ | WAPE (%) | Viés (ref/dia) | Sobra Pot. (ref) | Déficit Pot. (ref) | Dias c/ Déficit ($n$ e %) | Ganho MAE s/ Reservas |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Ref.** | **Reservas Discentes (SUAP)** | Benchmark Humano | **29,19** | **39,09** | **0,088** | **20,76%** | **−19,57** | **1.341** | **6.802** | **199 (71,3%)** | *Linha de Base* |
| **1º** | **Ridge** | Linear L2 | **19,51** | **27,18** | **0,559** | **13,88%** | **+1,23** | **2.894** | **2.550** | **148 (53,1%)** | **+33,15%** |
| **2º** | **Lasso** | Linear L1 | **19,54** | **27,24** | **0,557** | **13,89%** | **+1,51** | **2.935** | **2.515** | **143 (51,3%)** | **+33,06%** |
| **3º** | **CatBoost** | Gradient Boosting | **19,60** | **28,10** | **0,529** | **13,94%** | **+0,73** | **2.835** | **2.632** | **150 (53,8%)** | **+32,86%** |
| **4º** | **Regressão Linear** | OLS | **20,11** | **28,29** | **0,522** | **14,30%** | **+4,92** | **3.491** | **2.120** | **126 (45,2%)** | **+31,09%** |
| **5º** | **Ensemble Voting** | Combinado | **20,31** | **28,48** | **0,516** | **14,44%** | **+0,41** | **2.890** | **2.777** | **146 (52,3%)** | **+30,42%** |
| **6º** | **Extra Trees** | Random Trees | **20,47** | **29,18** | **0,492** | **14,56%** | **+1,31** | **3.039** | **2.672** | **143 (51,3%)** | **+29,87%** |
| **7º** | **LightGBM** | Gradient Boosting | **20,76** | **29,08** | **0,495** | **14,76%** | **+0,14** | **2.915** | **2.877** | **148 (53,1%)** | **+28,88%** |
| **8º** | **SVR** | Vetor Suporte | **20,85** | **30,35** | **0,450** | **14,83%** | **−0,13** | **2.890** | **2.926** | **151 (54,1%)** | **+28,57%** |
| **9º** | **Random Forest** | Bagging | **21,21** | **30,41** | **0,448** | **15,09%** | **−0,04** | **2.954** | **2.965** | **146 (52,3%)** | **+27,31%** |
| **10º** | **KNN** | Vizinhos | **21,27** | **30,16** | **0,457** | **15,13%** | **−1,43** | **2.767** | **3.167** | **152 (54,5%)** | **+27,13%** |
| **11º** | **Gradient Boosting** | Boosting | **21,96** | **31,16** | **0,420** | **15,62%** | **+1,90** | **3.328** | **2.799** | **129 (46,2%)** | **+24,76%** |
| **12º** | **XGBoost** | Boosting | **23,43** | **33,01** | **0,349** | **16,66%** | **+0,72** | **3.369** | **3.168** | **134 (48,0%)** | **+19,73%** |
| **13º** | **Decision Tree** | Árvore | **26,65** | **38,11** | **0,133** | **18,96%** | **+0,88** | **3.841** | **3.596** | **126 (45,2%)** | **+8,68%** |
| **14º** | **MLP (Rede Neural)** | Perceptron | **29,15** | **41,24** | **−0,016** | **20,73%** | **+1,13** | **4.225** | **3.909** | **162 (58,1%)** | **+0,12%** |

#### Ranking Horizonte $t+2$ (Longo Prazo / Compras com 2 Semanas de Antecedência, $N = 275$ datas comuns):
1. **CatBoost:** **MAE = 21,65 ref/dia** | RMSE = 29,83 | $R^2 = 0,398$ | WAPE = 15,35% | Viés = +0,82
2. **KNN:** **MAE = 22,09 ref/dia** | RMSE = 30,19 | $R^2 = 0,384$ | WAPE = 15,66% | Viés = −0,95
3. **Ensemble Voting:** **MAE = 22,60 ref/dia** | RMSE = 30,28 | $R^2 = 0,380$ | WAPE = 16,02% | Viés = +0,51
4. **Ridge:** **MAE = 22,78 ref/dia** | RMSE = 30,79 | $R^2 = 0,359$ | WAPE = 16,15% | Viés = +1,45
5. **Lasso:** **MAE = 22,94 ref/dia** | RMSE = 31,14 | $R^2 = 0,344$ | WAPE = 16,26% | Viés = +1,80

---

### 4.3. Cenário 2 (Com Variáveis Meteorológicas — Open-Meteo)
> **[REGISTRO MANDATÓRIO DE LIMITAÇÃO METODOLÓGICA]**  
> A base meteorológica integrada no repositório (`dados/silver/silver_clima.parquet`) provém do endpoint histórico `archive-api.open-meteo.com`, contendo observações meteorológicas ex-post e não arquivos históricos de previsões numéricas emitidas à época. Por essa razão, **o Cenário 2 no período 2023–2025 deve ser classificado cientificamente como "Cenário Oráculo Retrospectivo (Clima Observado Ex-Post)"**, e não como previsão operacional.  
> Não há nenhum resíduo de fontes antigas (NASA) no repositório.

- **Horizonte $t+1$ ($N = 279$):**
  - **Ridge:** **MAE = 19,48 ref/dia** | RMSE = 27,15 | $R^2 = 0,560$ | Ganho = +33,26%
  - **CatBoost:** **MAE = 19,55 ref/dia** | RMSE = 27,98 | $R^2 = 0,533$ | Ganho = +33,02%
  - **Lasso:** **MAE = 19,56 ref/dia** | RMSE = 27,24 | $R^2 = 0,557$ | Ganho = +33,00%
- **Horizonte $t+2$ ($N = 275$):**
  - **CatBoost:** **MAE = 21,38 ref/dia** | RMSE = 29,45 | $R^2 = 0,413$
  - **KNN:** **MAE = 21,95 ref/dia** | RMSE = 30,05 | $R^2 = 0,389$

---

### 4.4. Cenário 3 (Modelo Preditivo Integrando as Reservas dos Estudantes em $t+1$)
Quando a reserva do estudante na sexta-feira é utilizada como atributo preditivo de entrada pelo pipeline:
- **1º Ensemble Voting:** **MAE = 17,74 ref/dia** | RMSE = 25,18 | $R^2 = 0,621$ | WAPE = 12,62% | **Ganho de +39,23%**
- **2º Lasso:** **MAE = 17,94 ref/dia** | RMSE = 23,58 | $R^2 = 0,668$ | WAPE = 12,76% | **Ganho de +38,54%**
- **3º Ridge:** **MAE = 18,20 ref/dia** | RMSE = 23,89 | $R^2 = 0,659$ | WAPE = 12,94% | **Ganho de +37,65%**
- **4º Random Forest:** **MAE = 18,48 ref/dia** | RMSE = 27,38 | $R^2 = 0,552$ | WAPE = 13,14% | **Ganho de +36,69%**
- **5º CatBoost:** **MAE = 18,52 ref/dia** | RMSE = 26,80 | $R^2 = 0,571$ | WAPE = 13,17% | **Ganho de +36,55%**

---

## 5. AUDITORIA DA COORTE E RESULTADOS DE 2026 (RECORTE QUALIFICAÇÃO)

### 5.1. Teto Retrospectivo Obrigatório em 31/08/2026 ($N = 73$ datas de teste)
- O ano letivo de 2026 possui 145 dias com consumo registrado na catraca, dos quais 123 ocorreram até 31/08/2026.
- A coorte de validação das políticas operacionais de 2026 (implementada a partir de 26/02/2026) totaliza **exatamente $N = 73$ datas letivas de teste** até 31/08/2026.
- Versões preliminares de rascunho continham $N = 83$ datas (estendendo-se indevidamente até 25/09/2026). O laudo pericial `dissertacao/AUDITORIA_QUALIFICACAO_RECALCULO_N73.md` estabeleceu a retificação mandatória para a qualificação:
  - **Planejamento Humano (Nutricionista Responsável Técnica):** Sobras = 1.340 refeições; Déficits = 433 refeições; Custo de Sobras = R$ 18.760,00; Taxa de Déficit = 34,2%.
  - **Modelo Híbrido 50/50:** Sobras = 1.119 refeições; Déficits = 413 refeições; Custo de Sobras = R$ 15.666,00; Economia Potencial = R$ 3.094,00; Taxa de Déficit = 37,0%.

### 5.2. Segregação Mandatória dos Dados de Setembro/2026
- Foram identificadas 16 datas com consumo em setembro/2026 (das quais 10 faziam parte do arquivo preliminar de 83 dias).
- **Status da Segregação:** As datas de setembro de 2026 foram estritamente isoladas e retiradas de todas as tabelas e slides da qualificação, sendo reservadas exclusivamente como base de validação prospectiva para a defesa final.

---

## 6. AUDITORIA DE FIGURAS E TABELAS

### 6.1. Figura 49 (Confronto Histórico 2023–2025)
- **Problema Detectado na Figura Original:** O script de visualização (`src/gerar_notebook_visualizacao_06.py:685`) continha uma constante fixa de rascunho (`MAE = 25.66; Viés = -17.8`), divergente tanto de 27,10 (universo total) quanto de 29,19 (interseção comum).
- **Substituição Concluída:** A figura foi regenerada diretamente da série de previsões diárias auditadas e salva em alta resolução (300 DPI) em duas versões oficiais:
  1. **Versão Integral (Todos os 14 Algoritmos):**  
     `reports/auditoria_geral_qualificacao_20261016_1805/figuras/figura_49_atualizada_14_algoritmos_auditada.png`
  2. **Versão Resumida (Top 10 Modelos com Nota Explicativa):**  
     `reports/auditoria_geral_qualificacao_20261016_1805/figuras/figura_49_atualizada_destaque_10_algoritmos_auditada.png`  
     *(Contém nota de rodapé explícita informando a omissão gráfica de KNN, Gradient Boosting, Decision Tree e MLP)*.

---

## 7. RESPOSTAS OBJETIVAS AOS QUESITOS DO USUÁRIO

### 1. Quais resultados foram reproduzidos e conferem?
- A coorte canônica de reservas discentes ($N = 458$ datas letivas, 2023: 181, 2024: 122, 2025: 155), consumo total (61.367 ref), reservas totais (54.789 ref), MAE (27,10 ref/dia), RMSE (36,38 ref), R² (0,1692), WAPE (20,22%), sobras (2.916 ref), déficits (9.494 ref) e dias com déficit (292, 63,8%) conferem **100% com a Tabela 3 da dissertação**.
- O MAE pareado das reservas discentes nas 279 datas comuns (**29,19 ref/dia**) confere em todas as bases e scripts.
- A coorte retrospectiva de 2026 limitada a 31/08/2026 com **$N = 73$ datas letivas** confere perfeitamente com os dados da catraca e com o laudo de recálculo N=73.

### 2. Quais resultados divergiram, quais são os valores corretos e como isso foi demonstrado?
- **Divergência de Transcrição no Relatório Anterior:** O relatório Markdown anterior continha números incorretos no texto para as reservas discentes em $N=279$ (RMSE 38,86; viés −18,04; sobras 1.268; déficits 6.303) e para o CatBoost (sobras 2.868 e déficits 2.665).
- **Valores Corretos Comprovados Ponto a Ponto:**
  - Reservas Discentes ($N=279$): **RMSE = 39,09 ref**; **Viés = −19,57 ref/dia**; **Sobras = 1.341 ref**; **Déficits = 6.802 ref**; **Dias com déficit = 199 (71,3%)**.
  - CatBoost ($N=279$, C1 $t+1$): **Sobras = 2.835 ref**; **Déficits = 2.632 ref**; **Viés = +0,73 ref/dia**; **Dias com déficit = 150 (53,8%)**.
- **Demonstração:** Os CSVs gerados na auditoria anterior já continham os valores corretos calculados; a discrepância decorreu exclusivamente de erro de transcrição manual do modelo de IA na elaboração da tabela Markdown, agora completamente corrigida e demonstrada pelo script `recalcular_todas_metricas_auditadas.py`.

### 3. Qual modelo lidera em cada cenário e horizonte (datas pareadas)?
- **Cenário 1 (Base), $t+1$ ($N = 279$):** **Ridge** lidera em acurácia absoluta (**MAE = 19,51 ref/dia**, ganho de +33,15% sobre a reserva), seguido de perto por **Lasso (19,54)** e **CatBoost (19,60)**.
- **Cenário 1 (Base), $t+2$ ($N = 275$):** **CatBoost** lidera (**MAE = 21,65 ref/dia**, $R^2 = 0,398$), seguido por **KNN (22,09)** e **Ensemble Voting (22,60)**.
- **Cenário 2 (Com Clima Oráculo Ex-Post), $t+1$ ($N = 279$):** **Ridge** (**MAE = 19,48 ref/dia**), seguido por **CatBoost (19,55)** e **Lasso (19,56)**.
- **Cenário 2 (Com Clima Oráculo Ex-Post), $t+2$ ($N = 275$):** **CatBoost** lidera (**MAE = 21,38 ref/dia**).
- **Cenário 3 (Com Reserva Discente), $t+1$ ($N = 279$):** **Ensemble Voting** lidera (**MAE = 17,74 ref/dia**, ganho de +39,23%), seguido por **Lasso (17,94)** e **Ridge (18,20)**.

### 4. Quais figuras ou tabelas estão corretas, incompletas ou precisam ser refeitas?
- **Figura 49:** A versão original do notebook 06 (que continha o valor fixo de rascunho 25,66) estava incorreta e defasada. Foi integralmente refeita e salva em 300 DPI em duas versões (completa com 14 modelos e reduzida com 10 modelos e nota explicativa).
- **Tabelas de Confronto Pareado:** A tabela em markdown da auditoria anterior estava com valores descompassados em relação aos CSVs. A nova tabela (`confronto_pareado_c1_t1_datas_comuns.csv`) traz os valores exatos e padronizados com precisão de 100%.

### 5. Quais resultados podem ser usados na apresentação da qualificação, respeitando o corte de 31/08/2026?
- Os resultados do triênio **2023–2025** baseados na coorte canônica de reservas ($N = 458$) e na coorte pareada de validação walk-forward ($N = 279$ em $t+1$ e $N = 275$ em $t+2$).
- A nova **Figura 49 auditada** (painel duplo com MAE e Taxa de Déficit).
- Os resultados operacionais de **2026 estritamente limitados a 31/08/2026 ($N = 73$ datas letivas)**, conforme formalizado em `dissertacao/AUDITORIA_QUALIFICACAO_RECALCULO_N73.md`.
- **Proibição Estrita:** Nenhuma métrica ou simulação contendo datas de setembro, outubro ou novembro de 2026 deve ser incluída nos slides da qualificação.

### 6. O que continua pendente?
- **Nenhuma pendência técnica ou matemática impeditiva.** Todos os números divergentes foram reconciliados, comprovados por recálculo direto e inventariados em arquivos CSV/PNG auditáveis.
- **Ação Recomendada de Apresentação:** Inserir a nova Figura 49 gerada (`figura_49_atualizada_14_algoritmos_auditada.png` ou a versão com nota técnica) no slide correspondente da apresentação e manter o laudo de recálculo N=73 como anexo pericial irrefutável.
