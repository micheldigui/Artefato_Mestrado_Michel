# RELATÓRIO OFICIAL DE AUDITORIA, RECÁLCULO E CONFERÊNCIA PERICIAL
## Versão de Qualificação — Coorte Estrita até 31/08/2026

**Documento Objeto:** `F:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_resultados_parciais_20261013_entrega.docx`  
**Data da Emissão:** 14/10/2026  
**Regime Pericial:** Somente Leitura das Fontes Originais (Sem alteração de notebooks, scripts em `src/`, bases de dados ou no arquivo DOCX).  
**Regra Mandatória da Qualificação:** Exclusão estrita e total de setembro, outubro e novembro de 2026. Todos os recálculos encerram-se formalmente em **31/08/2026**.

---

## 1. DETALHAMENTO E ENTREGA DOS ITENS RECALCULADOS

### 1.1 Item 1: Recálculo da Tabela 4 e da Figura 16 até 31/08/2026 ($N=123$)

#### A. Conferência Metodológica, Filtros e Fórmulas
- **Bases-Fonte:** `dados/silver/silver_consumo.parquet` e `dados/silver/silver_reservas.parquet`.
- **Filtro Aplicado:** Registros operacionais de 2026 compreendidos entre a abertura do ano letivo (04/02/2026) e o marco de corte de qualificação (31/08/2026):
  $$\text{ano} = 2026 \quad \text{e} \quad \text{data\_iso} \le \text{'2026-08-31'}$$
- **Amostra Válida:** Resulta em **exatamente $N=123$ datas letivas** com consumo real registrado e quantitativo planejado pela nutricionista. O valor anterior de $N=140$ incluía indevidamente datas de setembro e outubro e foi totalmente expurgado.
- **Fórmulas e Resultados Numéricos Apurados:**
  1. **Consumo Médio Diário na Catraca:**
     $$\bar{y} = \frac{1}{123}\sum_{i=1}^{123} y_i = \mathbf{167,24}\text{ refeições/dia}$$
  2. **Planejamento Médio Diário Institucional:**
     $$\bar{p} = \frac{1}{123}\sum_{i=1}^{123} p_i = \mathbf{182,67}\text{ refeições/dia}$$
  3. **Sobras Potenciais Acumuladas:**
     $$\text{Sobras} = \sum_{i=1}^{123} \max(0, p_i - y_i) = \mathbf{2.561}\text{ refeições}$$
  4. **Déficits Potenciais Acumulados:**
     $$\text{Déficits} = \sum_{i=1}^{123} \max(0, y_i - p_i) = \mathbf{663}\text{ refeições}$$
  5. **Saldo Líquido Anual Aparente:**
     $$\text{Saldo} = \sum_{i=1}^{123} (p_i - y_i) = \text{Sobras} - \text{Déficits} = 2.561 - 663 = \mathbf{+1.898}\text{ refeições}$$
  6. **Desvios Diários Reais Mascarados:**
     $$\text{Desvios Absolutos} = \text{Sobras} + \text{Déficits} = 2.561 + 663 = \mathbf{3.224}\text{ refeições}$$
  7. **Erro Médio Absoluto Diário (MAE):**
     $$\text{MAE} = \frac{1}{123}\sum_{i=1}^{123} |p_i - y_i| = \mathbf{26,21}\text{ refeições/dia}$$
  8. **Distribuição das Ocorrências:**
     - Dias com Déficit Potencial ($y_i > p_i$): **48 datas** ($39,0\%$).
     - Dias com Sobra Potencial ($p_i > y_i$): **72 datas** ($58,5\%$).
     - Dias com Planejamento Exato ($p_i = y_i$): **3 datas** ($2,4\%$).

#### B. Arquivos Gerados
- 📄 CSV da Tabela 4: [`tabela_4_quantitativo_institucional_2026_recalculada_n123.csv`](file:///F:/PROJETOS/ARTEFATO/dissertacao/recalculos_qualificacao_20260831/tabela_4_quantitativo_institucional_2026_recalculada_n123.csv)
- 🖼️ PNG da Figura 16: [`figura_16_decomposicao_efeito_compensatorio_corrigida.png`](file:///F:/PROJETOS/ARTEFATO/dissertacao/figuras_corrigidas_20260831/figura_16_decomposicao_efeito_compensatorio_corrigida.png)

#### C. Redação Proposta para Atualização Manual no DOCX
- **Substituição da Tabela 4 no DOCX (Tabela 19, p. 74):**
  | Ano | Regime | n | Consumo médio | Planejado médio | Saldo | Sobra potencial | Déficit potencial | Dias c/ déficit | MAE |
  | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
  | **2026** | Estimativa institucional | **123** | **167,2** | **182,7** | **+1.898** | **2.561** | **663** | **39,0%** | **26,21** |

- **Atualização do Parágrafo P705 (após a Figura 16):**
  > *"A Figura 16 sintetiza o efeito compensatório confrontando o saldo líquido anual aparente com os desvios diários reais acumulados. No período de reservas discentes (2023 a 2025; N=458 datas), o saldo líquido foi de −6.578 refeições, mas a soma dos desvios diários potenciais atingiu 12.410 refeições (2.916 em sobras e 9.494 em déficits). No regime da nutricionista (fevereiro a agosto de 2026; N=123 datas), o saldo líquido positivo de +1.898 refeições mascarou 3.224 refeições em desvios diários reais (2.561 de sobras e 663 de déficit). Em contrapartida, na coorte pareada de qualificação (N=73 datas de 2026), o Modelo Híbrido 50/50 conteve o saldo acumulado em +608 refeições e limitou os desvios operacionais diários a 1.474 refeições (1.041 de sobra e 433 de déficit), evidenciando a estabilização matemática do planejamento."*

- **Atualização do Parágrafo P710 (após a Figura 17):**
  > *"...Já no regime seguinte de 2026 conduzido pela nutricionista, detalhado na Tabela 4, o perfil inverteu-se novamente, acumulando 2.561 refeições em sobras potenciais e 663 em déficit nas 123 datas letivas avaliadas até 31 de agosto."*

- **Atualização dos Parágrafos P718, P721 e P722:**
  > *[P718] "Em fevereiro de 2026, a gestão do campus substituiu o formulário discente pelo quantitativo informado pela nutricionista responsável. O recorte da análise compreende 123 datas letivas entre fevereiro e agosto de 2026, conforme a Tabela 4."*  
  > *[P721] "Nota: recorte de fevereiro a agosto de 2026, com 123 datas letivas. Sobras e déficits potenciais são diferenças teóricas de planejamento, não medições físicas de descarte ou de pessoas desassistidas."*  
  > *[P722] "No período do quantitativo da nutricionista entre fevereiro e agosto de 2026 (Tabela 4), a distribuição do erro de planejamento revelou um padrão consistente de superestimativa preventiva, com média planejada de 182,7 refeições para um consumo médio real de 167,2 refeições diárias. Esse procedimento esteve associado a déficit potencial em 39,0% das 123 datas letivas (48 dias), além de 2.561 refeições acumuladas em sobras potenciais e MAE de 26,21 refeições/dia. Como não houve pesagem de descarte nem contagem de estudantes sem atendimento, esses resultados refletem desvios de dimensionamento teórico e não comprovam desperdício físico ou desassistência."*

---

### 1.2 Item 2: Recálculo e Geração da Figura 19 (Regressão Linear em t+2 com e sem Open-Meteo)

#### A. Conferência Metodológica e Dados Verificáveis
- **Base-Fonte:** `dados/gold/predicoes_detalhadas_walk_forward.parquet`.
- **Filtro Aplicado:** `horizonte == 'Semana_t2'`, `algoritmo == 'Regressao_Linear'` e `data_iso <= '2026-08-31'`.
- **Amostra e Período:** Ambas as séries possuem exatamente **$N=73$ datas letivas** avaliadas no mesmo período temporal (**19/02/2026 a 31/08/2026**).
- **Métricas Auditadas:**
  1. **Cenário 1 (Base + Cardápio — Sem Dados Meteorológicos):**
     $$\text{MAE} = \mathbf{27,33}\text{ ref/dia} \quad | \quad \text{RMSE} = \mathbf{36,04}\text{ ref} \quad | \quad R^2 = \mathbf{0,371} \quad | \quad \text{WAPE} = \mathbf{16,11\%}$$
  2. **Cenário 2 (Com Variáveis Meteorológicas Open-Meteo):**
     $$\text{MAE} = \mathbf{25,86}\text{ ref/dia} \quad | \quad \text{RMSE} = \mathbf{35,38}\text{ ref} \quad | \quad R^2 = \mathbf{0,394} \quad | \quad \text{WAPE} = \mathbf{15,25\%}$$
  3. **Efeito da Inclusão do Clima em t+2:** Redução de **1,47 refeição/dia no MAE** (ganho relativo de $-5,4\%$) e elevação do coeficiente de determinação $R^2$ de $0,371$ para $0,394$.

#### B. Arquivos Gerados
- 📄 CSV da Figura 19: [`figura_19_regressao_linear_t2_com_sem_clima_n73.csv`](file:///F:/PROJETOS/ARTEFATO/dissertacao/recalculos_qualificacao_20260831/figura_19_regressao_linear_t2_com_sem_clima_n73.csv)
- 🖼️ PNG da Figura 19: [`figura_19_regressao_linear_t2_com_sem_clima_corrigida.png`](file:///F:/PROJETOS/ARTEFATO/dissertacao/figuras_corrigidas_20260831/figura_19_regressao_linear_t2_com_sem_clima_corrigida.png)

#### C. Redação Proposta para Atualização Manual no DOCX (Parágrafo P748)
> *"A comparação mantém a mesma família de modelo entre os cenários 1 e 2; ainda assim, o resultado não comprova efeito causal nem disponibilidade prospectiva das variáveis. No horizonte t+2 (10 a 14 dias de antecedência para compras), avaliado em 73 datas letivas de 2026 (19/02 a 31/08), a regressão linear apresentou MAE de 27,33 refeições/dia no cenário-base (sem clima) e 25,86 no cenário com variáveis do Open-Meteo (redução de 1,47 refeição/dia, ou -5,4%); o R² passou de 0,371 para 0,394. A comparação descreve o desempenho dessas configurações na avaliação retrospectiva. A utilidade para compras também depende de estoque, validade, prazo de reposição e decisões da equipe, aspectos não medidos neste experimento."*

---

### 1.3 Item 3: Recálculo e Geração da Figura 20 (Comparação t+1 vs. t+2 para os 5 Algoritmos)

#### A. Diagnóstico da Imagem Incorporada e Conteúdo Real
- **Incongruência no DOCX Original:** O título da Figura 20 (P750) e o texto de P749/P753 anunciavam *"MAE do XGBoost no cenário-base por horizonte"*, mas a imagem efetivamente incorporada no Word exibia **cinco algoritmos de Machine Learning** comparando o horizonte $t+2$ com $t+1$.
- **Recálculo sobre as 73 Datas Letivas até 31/08/2026:**
  A avaliação foi recalculada a partir de `dados/gold/predicoes_detalhadas_walk_forward.parquet` para os 5 algoritmos da figura nos dois horizontes ($t+2$ compras com $N=73$; $t+1$ preparo com $N=73$):

| Algoritmo | $N$ ($t+2$) | $N$ ($t+1$) | MAE $t+2$ Base (ref) | MAE $t+1$ Base (ref) | Variação no Cenário-Base (%) | MAE $t+2$ Clima C2 (ref) | MAE $t+1$ Nutri C3 (ref) | Ganho Reforecast Operacional (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Lasso** | 73 | 73 | **29,12** | **28,64** | **-1,7%** | 28,16 | 21,82 | **-22,5%** |
| **Ridge** | 73 | 73 | **28,38** | **27,82** | **-2,0%** | 26,96 | 21,72 | **-19,4%** |
| **SVR** | 73 | 73 | **26,82** | **25,26** | **-5,8%** | 28,02 | 24,26 | **-13,4%** |
| **XGBoost** | 73 | 73 | **28,47** | **27,46** | **-3,5%** | 28,94 | 24,59 | **-15,0%** |
| **CatBoost** | 73 | 73 | **28,55** | **27,57** | **-3,4%** | 28,52 | 23,97 | **-15,9%** |

#### B. Arquivos Gerados
- 📄 CSV da Figura 20: [`figura_20_comparacao_horizontes_5_algoritmos_n73.csv`](file:///F:/PROJETOS/ARTEFATO/dissertacao/recalculos_qualificacao_20260831/figura_20_comparacao_horizontes_5_algoritmos_n73.csv)
- 🖼️ PNG da Figura 20: [`figura_20_comparacao_horizontes_5_algoritmos_corrigida.png`](file:///F:/PROJETOS/ARTEFATO/dissertacao/figuras_corrigidas_20260831/figura_20_comparacao_horizontes_5_algoritmos_corrigida.png)

#### C. Redação Proposta para Atualização Manual no DOCX
- **Atualização do Parágrafo P749:**
  > *"A Figura 20 compara os erros médios absolutos (MAE) entre o horizonte inicial de compras (t+2, de 10 a 14 dias) e o horizonte de preparo (t+1, de 3 a 7 dias) no cenário-base para cinco algoritmos de aprendizado de máquina. Como cada horizonte possui conjunto próprio de datas no protocolo sequencial, a comparação é descritiva e não isola ganho causal de reforecast."*

- **Atualização da Legenda P750:**
  > *"Figura 20 - Comparação do MAE entre os horizontes t+2 e t+1 no cenário-base para cinco algoritmos (2026)"*

- **Atualização do Parágrafo P753:**
  > *"No cenário-base, todos os cinco algoritmos apresentaram redução descritiva do erro médio com a aproximação temporal do fornecimento: o SVR obteve MAE de 26,82 em t+2 e 25,26 em t+1 (-5,8%); o Ridge passou de 28,38 para 27,82 (-2,0%); o XGBoost variou de 28,47 para 27,46 (-3,5%); o CatBoost reduziu de 28,55 para 27,57 (-3,4%); e o Lasso passou de 29,12 para 28,64 (-1,7%). Quando se avalia o fluxo operacional completo — confrontando a previsão inicial de compras com clima (t+2) com a emissão final de preparo com quantitativo institucional (t+1) —, a incorporação do planejamento humano produz ganhos de reforecast expressivos, reduzindo o MAE do Lasso em 22,5% (28,16 para 21,82) e do Ridge em 19,4% (26,96 para 21,72), conforme detalhado na Tabela 5."*

---

### 1.4 Item 4: Recálculo e Geração da Figura 24 (Densidade de Resíduos em N=73 Datas Pareadas)

#### A. Conferência Metodológica e Equação dos Resíduos
- **Base-Fonte:** `reports/tabelas/previsoes_diarias_2026_monte_carlo.parquet`.
- **Filtro Aplicado:** Exclusivamente as **73 datas letivas pareadas** entre **26/02/2026 e 31/08/2026** onde coexistem catraca real ($y_i$), previsão da IA Ridge ($\hat{y}_{i,\text{Ridge}}$) e planejamento da nutricionista ($p_{i,\text{Nutri}}$).
- **Fórmula dos Erros/Resíduos Diários de Dimensionamento:**
  $$e_i = \text{Planejado}_i - \text{Consumo Real}_i$$
  - $e_i > 0 \implies$ **Sobra de Planejamento** (Sobredimensionamento preventivo).
  - $e_i < 0 \implies$ **Déficit de Planejamento** (Subdimensionamento / Risco de ruptura).
  - $e_i = 0 \implies$ **Dimensionamento Perfeito**.
- **Comportamento das Três Distribuições em $N=73$:**
  1. **Nutricionista Isolada:** Erro médio (viés) de $\mathbf{+9,5}\text{ refeições/dia}$ ($\text{MAE} = 23,37$). Distribuição fortemente assimétrica à direita, com cauda longa de superestimativa preventiva.
  2. **IA Ridge Pura:** Erro médio (viés) de $\mathbf{+7,2}\text{ refeições/dia}$ ($\text{MAE} = 21,72$). Distribuição unimodal centrada próxima ao zero, sem a assimetria humana, mas com caudas moderadas.
  3. **Modelo Híbrido 50/50:** Erro médio (viés) de $\mathbf{+8,3}\text{ refeições/dia}$ ($\text{MAE} = 20,19$). Apresenta o maior pico de densidade e menor variância dos resíduos diários, combinando a ausência de déficits extremos com menor volume de sobras.

#### B. Arquivos Gerados
- 📄 CSV da Figura 24: [`figura_24_residuos_diarios_n73.csv`](file:///F:/PROJETOS/ARTEFATO/dissertacao/recalculos_qualificacao_20260831/figura_24_residuos_diarios_n73.csv)
- 🖼️ PNG da Figura 24: [`figura_24_distribuicao_erros_diarios_recalculada_n73.png`](file:///F:/PROJETOS/ARTEFATO/dissertacao/figuras_corrigidas_20260831/figura_24_distribuicao_erros_diarios_recalculada_n73.png)

#### C. Redação Proposta para Atualização Manual no DOCX (Parágrafos P788 e P792)
- **Atualização do Parágrafo P788:**
  > *"A Figura 24 apresenta a densidade estimada dos erros diários de planejamento para os três paradigmas avaliados na coorte pareada de qualificação (73 datas letivas de 2026): a nutricionista isolada, o modelo preditivo puro (Ridge) e o modelo colaborativo híbrido 50/50."*

- **Atualização do Parágrafo P792:**
  > *"A Figura 24 compara visualmente a densidade de probabilidade (KDE) dos erros diários nas 73 datas pareadas de 2026 (26/02 a 31/08). A curva da nutricionista (em laranja) exibe nítida assimetria à direita (viés médio de +9,5 refeições), evidenciando a superestimativa preventiva orientada a evitar a ruptura do serviço. O modelo preditivo Ridge (em azul) centraliza a distribuição mais próximo ao erro zero (viés médio de +7,2 refeições), eliminando o descompasso sistemático. Por sua vez, o modelo híbrido 50/50 (em verde) reúne as qualidades de ambas as abordagens: alcança o pico de densidade mais elevado e base mais estreita, comprovando a redução da variância dos desvios diários e conferindo maior estabilidade operacional à produção do restaurante escolar."*

---

### 1.5 Item 5: Refinamento da Figura 28 (Eliminação Total de Sobreposições e Legibilidade no DOCX)

- **Ajustes de Design e Diagramação Implementados:**
  - Formato panorâmico proporcional de dois painéis lado a lado ($12,5 \times 5,2$ polegadas a 300 DPI).
  - Rótulos dos eixos categóricos simplificados e dispostos em duas linhas com espaçamento vertical generoso, eliminando colisões com a moldura:
    * `1. Reservas Discentes\n(2023–25; N=458)`
    * `2. Nutricionista\n(2026; N=73)`
    * `3. Híbrido +12\n(2026; N=73)`
  - Valores das barras fixados com tipografia em negrito e contraste elevado sobre fundo limpo:
    * **Painel A (Proteção Operacional):** $36,2\% \implies 56,2\% \implies \mathbf{82,2\%}$
    * **Painel B (MAE Diário):** $34,80\text{ ref} \implies 23,37\text{ ref} \implies \mathbf{24,81\text{ ref}}$
  - Nota de rodapé externa explicitando as coortes e seus respectivos denominadores amostrais.
- 🖼️ PNG Gerado: [`figura_28_comparacao_historica_consolidada_recalculada_n73.png`](file:///F:/PROJETOS/ARTEFATO/dissertacao/figuras_corrigidas_20260831/figura_28_comparacao_historica_consolidada_recalculada_n73.png)

---

### 1.6 Item 6: Tabela Comparativa de Substituição para o Resumo, Abstract e Considerações Parciais

A tabela abaixo relaciona os valores textuais antigos da versão preliminar e os valores exatos recalculados que devem figurar na dissertação de qualificação:

| Local no DOCX | Elemento / Métrica | Valor Antigo no DOCX (Preliminar c/ Set-Out) | Novo Valor Recalculado (Qualificação até 31/08/2026) | Justificativa Analítica da Substituição |
| :--- | :--- | :---: | :---: | :--- |
| **Resumo (P137) e Abstract (P142)** | Coorte de Modelagem em 2026 | 83 datas | **73 datas** | Expurgadas as 10 datas de setembro/2026 |
| **Resumo (P137) e Abstract (P142)** | MAE da Linha de Base (Cenário 1 t+2) | 29,50 (XGBoost) | **26,82 (SVR)** | Recálculo estrito da validação sequencial em $N=73$ |
| **Resumo (P137) e Abstract (P142)** | MAE da Linha de Base (Cenário 1 t+1) | 27,81 (XGBoost) | **25,26 (SVR)** | Recálculo estrito da validação sequencial em $N=73$ |
| **Resumo (P137) e Abstract (P142)** | MAE com Open-Meteo (Cenário 2 t+2) | 28,67 (Regressão Linear) | **25,86 (Regressão Linear)** | Recálculo estrito da validação sequencial em $N=73$ |
| **Resumo (P137) e Abstract (P142)** | MAE com Open-Meteo (Cenário 2 t+1) | 27,39 (Regressão Linear) | **24,75 (Regressão Linear)** | Recálculo estrito da validação sequencial em $N=73$ |
| **Resumo (P137) e Abstract (P142)** | MAE Cenário 3 t+1 (Melhor Modelo) | 22,27 (Lasso) | **21,72 (Ridge)** | Ridge superou Lasso no corte temporal de agosto |
| **Resumo (P137) e Abstract (P142)** | MAE Benchmark da Nutricionista | 24,92 | **23,37** | Exclusão de setembro reduz erro médio da nutricionista |
| **Resumo (P137) e Abstract (P142)** | MAE Modelo Híbrido 50/50 | 21,43 | **20,19** | Ganho preditivo em $N=73$ datas pareadas |
| **Resumo (P137) e Abstract (P142)** | Mínimo da Varredura Numérica | Não constava / 21,43 | **20,03 (em $\alpha \in [60\%; 62,5\%]$)** | Registro formal da fronteira de Pareto |
| **Resumo (P137) e Abstract (P142)** | Política Híbrido +12: Dias com Déficit | 16,9% (14 datas de 83) | **17,8% (13 datas de 73)** | Coorte pareada de qualificação ($N=73$) |
| **Tabela 4 e Parágrafo P705/P718** | $N$ de datas avaliadas em 2026 | 140 datas | **123 datas** | Limite do ano letivo até 31/08/2026 |
| **Tabela 4 e Parágrafos P705/P722** | Consumo Médio Diário em 2026 | 167,1 ref | **167,24 ref** | Censo de catraca até 31/08 ($N=123$) |
| **Tabela 4 e Parágrafos P705/P722** | Planejamento Médio Nutricionista | 186,2 ref | **182,67 ref** | Censo de reservas institucionais até 31/08 |
| **Tabela 4 e Parágrafos P705/P722** | Saldo Líquido Anual Mascarado | +2.670 ref | **+1.898 ref** | $2.561 - 663 = +1.898$ |
| **Tabela 4 e Parágrafos P705/P722** | Sobras Potenciais Acumuladas 2026 | 3.354 ref | **2.561 ref** | Exclusão de setembro/outubro |
| **Tabela 4 e Parágrafos P705/P722** | Déficits Potenciais Acumulados 2026 | 684 ref | **663 ref** | Exclusão de setembro/outubro |
| **Tabela 4 e Parágrafos P705/P722** | MAE Diário da Nutricionista (Censo) | 28,84 ref | **26,21 ref** | Base Silver completa até 31/08 ($N=123$) |
| **Tabela 4 e Parágrafos P705/P722** | Dias com Déficit na Nutricionista | 37,1% (52 dias de 140) | **39,0% (48 dias de 123)** | Base Silver completa até 31/08 ($N=123$) |
| **Parágrafo P748 (Figura 19)** | Regressão Linear t+2 Sem Clima (C1) | MAE 30,01; $R^2 = 0,230$ | **MAE 27,33; $R^2 = 0,371$** | Recálculo da série walk-forward em $N=73$ |
| **Parágrafo P748 (Figura 19)** | Regressão Linear t+2 Com Clima (C2) | MAE 28,67; $R^2 = 0,268$ | **MAE 25,86; $R^2 = 0,394$** | Recálculo da série walk-forward em $N=73$ |
| **Parágrafos P749/P750 (Figura 20)** | Identificação do Conteúdo do Gráfico | "MAE do XGBoost no cenário-base" | **"Comparação de 5 algoritmos entre t+2 e t+1"** | Alinhamento entre título e imagem real |
| **Parágrafo P792 (Figura 24)** | Denominador Amostral da Densidade | 83 datas pareadas | **73 datas pareadas** | Coorte de qualificação até 31/08 |
| **Considerações Parciais (P845)** | Métricas Finais da Coorte de 2026 | Coorte de 83 datas | **Coorte de 73 datas pareadas** | Parágrafo 845 já reconciliado com $N=73$ |

---

## 3. AUDITORIA PERICIAL E DESOBSTRUÇÃO VISUAL DAS FIGURAS 16 E 17

### 3.1 Figura 16: Decomposição do Efeito Compensatório nos Três Regimes

#### A. Conferência Metodológica e Recortes Amostrais Distintos
A Figura 16 sintetiza o comportamento do planejamento confrontando o **Saldo Líquido Anual Aparente** (soma algébrica onde sobras cancelam faltas) com os **Desvios Diários Reais Mascarados** (soma dos valores absolutos dos erros, representando o descompasso físico diário). Na versão de entrega, os três regimes avaliados possuem recortes e fontes estritamente definidos:

1. **Regime 1 — Reservas Discentes Voluntárias via SUAP (2023 a 2025):**
   - **Arquivo de Apoio:** `dados/silver/silver_fato_diaria.parquet` cruzado com `silver_reservas.parquet`.
   - **Recorte Amostral:** $N=458$ datas letivas com agendamento discente no triênio histórico (181 em 2023, 122 em 2024 e 155 em 2025).
   - **Saldo Líquido Anual Aparente:**
     $$\text{Saldo} = \sum (R_i - y_i) = \text{Sobras} - \text{Déficits} = 2.916 - 9.494 = \mathbf{-6.578}\text{ refeições}$$
   - **Desvios Diários Reais Acumulados:**
     $$\text{Desvios Absolutos} = \text{Sobras} + \text{Déficits} = 2.916 + 9.494 = \mathbf{12.410}\text{ refeições}$$
   - **Conclusão:** O saldo líquido negativo de $-6.578$ mascarou um descompasso físico de **12.410 refeições**, no qual o subdimensionamento crônico provocou faltas potenciais recorrentes.

2. **Regime 2 — Quantitativo Institucional pela Nutricionista (Fevereiro a Agosto/2026):**
   - **Arquivo de Apoio:** `dissertacao/recalculos_qualificacao_20260831/tabela_4_quantitativo_institucional_2026_recalculada_n123.csv`.
   - **Recorte Amostral:** Exatamente $N=123$ datas letivas da coorte de qualificação (04/02/2026 a 31/08/2026).
   - **Saldo Líquido Anual Aparente:**
     $$\text{Saldo} = \sum (P_i - y_i) = \text{Sobras} - \text{Déficits} = 2.561 - 663 = \mathbf{+1.898}\text{ refeições}$$
   - **Desvios Diários Reais Acumulados:**
     $$\text{Desvios Absolutos} = \text{Sobras} + \text{Déficits} = 2.561 + 663 = \mathbf{3.224}\text{ refeições}$$
   - **Conclusão:** Ao contrário do valor antigo baseado em $N=140$ (+2.670 de saldo e 4.038 de desvios), o corte rigoroso em 31/08/2026 estabelece saldo aparente de **+1.898 refeições** e desvios diários reais de **3.224 refeições**.

3. **Regime 3 — Avaliação Pareada do Modelo Híbrido 50/50 (Coorte 2026 até 31/08):**
   - **Arquivo de Apoio:** `dissertacao/recalculos_qualificacao_20260831/tabela_7_politicas_margens_recalculada_n73.csv`.
   - **Recorte Amostral:** Exatamente $N=73$ datas letivas pareadas (26/02/2026 a 31/08/2026) onde coexistem catraca, IA Ridge e nutricionista.
   - **Saldo Líquido Acumulado:**
     $$\text{Saldo} = \sum (\hat{y}_{i,\text{Híbrido}} - y_i) = 1.041 - 433 = \mathbf{+608}\text{ refeições}$$
   - **Desvios Diários Reais Acumulados:**
     $$\text{Desvios Absolutos} = 1.041 + 433 = \mathbf{1.474}\text{ refeições}$$
   - **Conclusão:** Na coorte estrita de qualificação ($N=73$), o Modelo Híbrido conteve os desvios operacionais em **1.474 refeições** (ante 1.778 no período que incluía setembro).

#### B. Solução Visual para Desobstrução do Rótulo "12.410"
- **Diagnóstico da Versão Anterior:** O topo da barra de desvios absolutos do Regime 1 alcança $y = 12.410$. Quando a legenda ficava posicionada no canto superior esquerdo (`loc='upper left'`), ela ficava sobreposta ou perigosamente próxima ao valor `12.410`.
- **Ajuste Geométrico Implementado:**
  - O eixo vertical foi expandido para $\text{ylim} = [-8.500; +16.000]$, proporcionando mais de 3.500 unidades de folga livre acima do maior valor da coluna.
  - A legenda foi realocada para o **canto superior direito (`loc='upper right'`)**, posicionando-se sobre a terceira categoria (Modelo Híbrido), cuja altura máxima é de apenas $1.474$.
  - Resultado: O rótulo **12.410** está completamente livre, destacado em negrito (#b45309) e sem nenhuma sobreposição por barra, linha ou caixa de legenda.
- **Arquivo de Imagem Gerado:** [`figura_16_decomposicao_efeito_compensatorio_corrigida.png`](file:///F:/PROJETOS/ARTEFATO/dissertacao/figuras_corrigidas_20260831/figura_16_decomposicao_efeito_compensatorio_corrigida.png).

---

### 3.2 Figura 17: Painel Anual de Sobras e Faltas Acumuladas no Regime de Reservas

#### A. Conferência com a Tabela de Origem (Tabela 3 da Dissertação / Tabela 18 do DOCX)
A Figura 17 detalha ano a ano o balanço de subdimensionamento e sobredimensionamento durante o regime de agendamento discente voluntário (2023 a 2025). O confronto minucioso com a Tabela 3 da dissertação revela:

| Ano Letivo | Amostra de Datas ($N$) | Faltas Potenciais (Déficit) | Sobras Potenciais (Excedente) | Saldo Anual Aparente | MAE (ref/dia) | Conformidade com Tabela 3 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **2023** | **$N=181$** | **1.174** | **1.916** | $+742$ | 17,07 | ✅ 100% Idêntico |
| **2024** | **$N=122$** | **4.524** | **334** | $-4.190$ | 39,82 | ✅ 100% Idêntico |
| **2025** | **$N=155$** | **3.796** | **666** | $-3.130$ | 28,79 | ✅ 100% Idêntico |
| **Total Triênio** | **$N=458$** | **9.494** | **2.916** | **$-6.578$** | **27,10** | ✅ 100% Idêntico |

- **Arquivo de Apoio:** `dados/silver/silver_fato_diaria.parquet` e Tabela 3 do DOCX (Tabela 18, p. 73).
- **Correção dos Rótulos do Eixo X:** A imagem anterior apresentava rótulos de amostra truncados (`Ano 2024 (N=157)` e `Ano 2025 (N=120)`). A nova imagem corrige os rótulos do eixo horizontal para espelhar exatamente a Tabela 3:
  * `Ano 2023 (N=181 datas)`
  * `Ano 2024 (N=122 datas)`
  * `Ano 2025 (N=155 datas)`

#### B. Solução Visual para Desobstrução do Rótulo "4.524"
- **Diagnóstico da Versão Anterior:** O pico anual de faltas ocorreu em 2024 com $4.524$ refeições. Na imagem anterior, o limite superior do eixo Y estava em 4.800 ou 5.200, comprimindo o número contra o teto e conflitando com a caixa de legenda quando posicionada à direita.
- **Ajuste Geométrico Implementado:**
  - O eixo vertical foi expandido para $\text{ylim} = [0; 5.800]$, garantindo mais de 1.200 unidades de headroom limpo acima da barra mais alta de 2024.
  - A legenda foi fixada no **canto superior esquerdo (`loc='upper left'`)**, flutuando com folga acima das barras de 2023 (cujo valor mais alto é 1.916).
  - O rótulo **4.524 ref** (vermelho escuro, negrito) localiza-se na coluna central, com visibilidade e legibilidade perfeitas.
- **Arquivo de Imagem Gerado:** [`figura_17_painel_anual_sobras_faltas_corrigida.png`](file:///F:/PROJETOS/ARTEFATO/dissertacao/figuras_corrigidas_20260831/figura_17_painel_anual_sobras_faltas_corrigida.png).

---

## 4. AUDITORIA PERICIAL DAS FIGURAS METEOROLÓGICAS E DE ASSOCIAÇÃO (FIGURAS 11, 12, 13 E 15)

### 4.1 Figura 11: Consumo por Faixa de Precipitação

#### A. Confronto Triplo: Dados Reais vs. Imagem no DOCX vs. Texto dos Parágrafos
- **Base e Fonte Utilizada:** `dados/silver/silver_fato_diaria.parquet` ($N=495$ datas letivas com registros meteorológicos válidos entre 2023 e 2025). Fonte climática: exclusivamente API **Open-Meteo** (coordenadas georreferenciadas do campus Jacareí/SP).
- **Valores Apurados na Base e na Imagem:**
  1. *Sem Chuva (0 mm):* Média = **138,8 refeições/dia** ($n = 213$ datas).
  2. *Chuva Fraca (0,1 a 5,0 mm):* Média = **131,4 refeições/dia** ($n = 192$ datas).
  3. *Chuva Moderada (5,1 a 15,0 mm):* Média = **128,7 refeições/dia** ($n = 58$ datas).
  4. *Chuva Forte (> 15,0 mm):* Média = **118,1 refeições/dia** ($n = 32$ datas).
  - Variação descritiva acumulada: Redução de **20,7 refeições/dia** (ou $-14,9\%$) entre dias secos e dias de precipitação intensa.
- **Diagnóstico das Diferenças:**
  - **Na Imagem (`image11.png`):** Exibe exatamente as 4 faixas com médias de 138,8 ($n=213$), 131,4 ($n=192$), 128,7 ($n=58$) e 118,1 ($n=32$). A figura está correta e alinhada à base.
  - **No Texto (Parágrafo P657):**
    > *"A Figura 11 apresenta o consumo médio conforme a intensidade da precipitação diária acumulada: dias secos apresentaram média de 138,8 refeições, caindo gradualmente para 131,2 em chuva fraca e atingindo 118,1 refeições em dias de chuva forte (redução média descritiva de aproximadamente 20 refeições/dia)."*
  - **Divergência Apontada:** O texto comete duas falhas:
    1. Informa $131,2$ para chuva fraca, enquanto os dados reais e a figura registram **131,4**.
    2. Omite completamente a categoria intermediária *"Chuva Moderada (5 a 15 mm: média de 128,7 refeições; n=58)"*, saltando direto de chuva fraca para forte.
- **Elemento que Precisa de Correção:** O **Texto (Parágrafo P657)**.
- **Redação Proposta para o Parágrafo P657:**
  > *"A Figura 11 apresenta o consumo médio conforme a intensidade da precipitação diária acumulada: dias secos apresentaram média de 138,8 refeições (n=213), caindo para 131,4 em chuva fraca (n=192), 128,7 em chuva moderada (n=58) e atingindo 118,1 refeições em dias de chuva forte (n=32), configurando uma redução descritiva de 20,7 refeições/dia entre os extremos."*

---

### 4.2 Figura 12: Relação entre Temperatura Máxima e Consumo

#### A. Confronto Triplo: Dados Reais vs. Imagem no DOCX vs. Texto dos Parágrafos
- **Base e Fonte Utilizada:** `dados/silver/silver_fato_diaria.parquet` ($N=495$ datas letivas com catraca e clima entre 2023 e 2025). Fonte climática: exclusivamente API **Open-Meteo** (`temperature_2m_max`).
- **Valores Apurados na Base e na Imagem:**
  - Correlação linear de Pearson: $r = \mathbf{+0,026}$ ($p > 0,05$).
  - A dispersão plota nuvem de pontos com reta de regressão linear ajustada ($y = 0,16x + 130,4$).
- **Diagnóstico das Diferenças:**
  - **Na Imagem (`image12.png`):** Mostra estritamente uma **regressão linear simples** com a reta tracejada vermelha e a caixa indicando *"Coeficiente de Pearson: r = 0,026"*. Não há nenhuma curva parabólica, polinomial ou spline não linear na imagem.
  - **No Texto (Parágrafo P662):**
    > *"A dispersão entre a temperatura máxima prevista (Open-Meteo) e o consumo diário (Figura 12) indica correlação linear praticamente nula ($r = 0,026$). O ajuste não linear sugere ligeira retração do comparecimento nos extremos térmicos (temperaturas abaixo de 16 °C e acima de 31 °C), embora a amplitude térmica isolada não seja suficiente para prever a oscilação da demanda."*
  - **Divergência Apontada:** O texto alega a existência de um *"ajuste não linear sugerindo ligeira retração nos extremos (<16°C e >31°C)"*. Contudo, o gráfico NÃO contém nenhum ajuste não linear traçado — apenas a reta linear. A menção a "ajuste não linear" é resquício conceitual de análises preliminares que não foi implementado graficamente.
- **Elemento que Precisa de Correção:** O **Texto (Parágrafo P662)**.
- **Redação Proposta para o Parágrafo P662:**
  > *"A dispersão entre a temperatura máxima observada via Open-Meteo e o consumo diário (Figura 12) indica correlação linear praticamente nula (r = 0,026). A reta de regressão linear ajustada apresenta inclinação residual, evidenciando que a variação térmica isolada não explica o volume de refeições servidas, embora haja dispersão empírica pontual nos extremos térmicos (dias com máxima abaixo de 16 °C ou acima de 31 °C)."*

---

### 4.3 Figura 13: Funções de Autocorrelação Temporal

#### A. Confronto Triplo: Dados Reais vs. Imagem no DOCX vs. Texto dos Parágrafos
- **Base e Fonte Utilizada:** Série temporal univariada do consumo diário em dias letivos de 2023 a 2025 ($N=495$ datas em `silver_fato_diaria.parquet`).
- **Valores Apurados na Base e na Imagem:**
  - Autocorrelações simples da série temporal ($\text{ACF}$):
    * $\text{Lag } 1 = \mathbf{0,593}$
    * $\text{Lag } 2 = \mathbf{0,547}$
    * $\text{Lag } 3 = \mathbf{0,488}$
    * $\text{Lag } 4 = \mathbf{0,469}$
    * $\text{Lag } 5 = \mathbf{0,479}$ (repique cíclico sazonal semanal)
    * $\text{Lag } 10 = \mathbf{0,399}$ (segundo repique semanal)
  - Limiar de significância assintótica assinalado: $\pm 1,96 / \sqrt{495} \approx \pm 0,088$.
- **Diagnóstico das Diferenças:**
  - **Na Imagem (`image13.png`):** Contém unicamente o correlograma da **Autocorrelação Simples (ACF)** para lags de 1 a 20, com destaque em vermelho para o Lag 5 (0,479) e Lag 10 (0,399). NÃO existe gráfico da PACF (autocorrelação parcial) na imagem.
  - **No Texto (Parágrafos P664 e P668):**
    * *P664 afirma:* *"A persistência inercial na série de refeições foi avaliada por meio das funções de autocorrelação simples (ACF) e parcial (PACF), dispostas na Figura 13."* $\implies$ **Incorreto:** a imagem não exibe PACF.
    * *P668 afirma:* *"A análise de correlação linear de Pearson (Figura 13) confirma que a sazonalidade semanal é o preditor isolado mais expressivo: a defasagem semanal de 5 dias úteis (Lag 5) registrou coeficiente de r = 0,654. Em contraste, as defasagens imediatamente anteriores (Lag 1 e Lag 2) apresentaram correlações mais moderadas (r = 0,38 e r = 0,31, respectivamente)."* $\implies$ **Incorreto e Invertido:** O texto transcreveu os coeficientes de correlação da matriz tabular da Camada Gold (que pertencem à Figura 15!) em vez de citar a ACF da série temporal. Na ACF real, o Lag 1 é 0,593 e o Lag 2 é 0,547.
- **Elemento que Precisa de Correção:** O **Texto (Parágrafos P664 e P668)** e o título da legenda P665.
- **Redação Proposta para Atualização Manual no DOCX:**
  - **Título da Legenda P665:**
    > *"Figura 13 - Função de autocorrelação simples (ACF) da série de consumo diário (2023 a 2025)"*
  - **Parágrafo P664:**
    > *"A persistência inercial na série de refeições foi avaliada por meio da função de autocorrelação simples (ACF), disposta na Figura 13."*
  - **Parágrafo P668:**
    > *"O correlograma da Figura 13 confirma a forte persistência temporal da demanda: a autocorrelação de primeira ordem (Lag 1) atinge r = 0,593, declinando gradualmente nos dias subsequentes até exibir um repique sazonal marcante na defasagem semanal de cinco dias úteis (Lag 5, r = 0,479) e seu múltiplo quinzenal (Lag 10, r = 0,399), comprovando que o mesmo dia da semana anterior constitui a principal âncora inercial do sistema."*

---

### 4.4 Figura 15: Correlação de Atributos com o Consumo (Diagnóstico da Diferença e Recálculo Oficial)

#### A. Diagnóstico Pericial: Origem da Diferença (+0,142 / -0,118 vs. -0,055 / -0,038)
A conferência pericial do código e dos dados identificou a causa raiz exata da discrepância apontada pelo pesquisador:

1. **Origem da Imagem Atual (`image15.png` / `figura_15_correlacao_atributos_consumo_pearson.png`):**
   - Os valores que aparecem na imagem incorporada no Word **não foram calculados dinamicamente em tempo de execução**.
   - Na função `gerar_figura_15_correlacao_atributos()` do script [`src/gerar_todas_figuras_dissertacao.py`](file:///f:/PROJETOS/ARTEFATO/src/gerar_todas_figuras_dissertacao.py#L354-L375), os coeficientes foram inseridos como uma lista estática (*hardcoded*):
     ```python
     atributos = [
         "Consumo lag 5 (mesmo dia sem. anterior)",
         "Média móvel 5 dias úteis",
         "Média móvel 10 dias úteis",
         "Consumo lag 1 (dia anterior)",
         "Dia da Semana: Quarta-feira",
         "Proteína: Carne Bovina",
         "Temperatura Máxima (°C)",
         "Precipitação Pluviométrica (mm)",
         "Proteína: Ovos / Vegetariano",
         "Dia da Semana: Sexta-feira",
     ]
     correlacoes = [
         0.654,
         0.612,
         0.548,
         0.534,
         0.228,
         0.165,
         0.142,
         -0.118,
         -0.185,
         -0.378,
     ]
```
   - O valor `+0,142` foi atribuído arbitrariamente à "Temperatura Máxima (°C)", plotando uma barra verde para a direita.
   - O valor `-0,118` foi herdado de uma rodada preliminar da precipitação (na Camada Silver histórica 2023–2025, a correlação da precipitação com o consumo é de $-0,114$).

2. **Conflito Interno entre a Imagem e o Texto no DOCX:**
   - O parágrafo **P689** da dissertação afirma textualmente:
     > *"Chuva acumulada e temperatura máxima também apresentam correlações negativas moderadas na amostra."*
   - O redator do texto presumiu ou pretendia descrever uma correlação **negativa** para a temperatura, mas a imagem incorporada exibia o valor **positivo (+0,142)**. Havia, portanto, um conflito frontal entre a imagem e o texto no próprio documento.

3. **Recálculo sobre a Base Real (`dados/gold/gold_dataset_ml_limpo.parquet` até 31/08/2026):**
   - Quando as correlações lineares de Pearson são calculadas matematicamente a partir da base Gold atualizada, com corte temporal estrito em **31/08/2026** ($N=568$ registros de modelagem), os valores reais apurados são:
     * **Temperatura Máxima Prevista (`temperature_2m_max`):** $r = \mathbf{-0,0551}$ ($n = 568$).
     * **Precipitação Pluviométrica Diária (`precipitation_sum`):** $r = \mathbf{-0,0375}$ ($n = 568$).
   - Ambas as variáveis meteorológicas apresentam associação linear residual/quase nula com o consumo ($|r| < 0,06$), e não "moderada".

#### B. Tabela Oficial de Recálculo da Figura 15 (Base Gold até 31/08/2026)
A tabela a seguir apresenta os coeficientes recalculados rigorosamente a partir da Feature Store da Camada Gold, utilizando todas as observações válidas pareadas por atributo até o marco de qualificação de 31/08/2026 ($N_{\text{total}} = 568$ datas letivas regulares):

| Atributo / Rótulo de Exibição | Variável na Camada Gold | Família Teórica | Coeficiente de Pearson ($r$) | $N$ Válido | Interpretação no Sistema |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **Consumo mesmo dia sem. anterior (Lag 5)** | `consumo_mesmo_dia_sem_passada` | Memória / Inércia Semanal | **+0,6383** | 464 | Forte persistência cíclica semanal |
| **Média móvel de consumo (5 dias úteis)** | `media_movel_5d` | Tendência de Curto Prazo | **+0,5658** | 563 | Forte âncora recente de produção |
| **Média móvel de consumo (10 dias úteis)** | `media_movel_10d` | Tendência de Médio Prazo | **+0,5245** | 558 | Suavização quinzenal de demanda |
| **Consumo do dia letivo anterior (Lag 1)** | `lag_1_dia_letivo` | Memória Imediata | **+0,4908** | 567 | Inércia do dia anterior |
| **Dia da Semana: Quarta-feira** | `is_quarta` | Calendário Escolar | **+0,1366** | 568 | Pico semanal de frequência discente |
| **Proteína do Cardápio: Carne Bovina** | `proteina_bovina` | Atratividade do Cardápio | **-0,0212** | 568 | Associação residual no consolidado |
| **Precipitação Pluviométrica Diária (mm)** | `precipitation_sum` | Meteorologia (Open-Meteo) | **-0,0375** | 568 | Efeito inibidor fraco/residual |
| **Proteína do Cardápio: Peixe** | `proteina_peixe` | Atratividade do Cardápio | **-0,0526** | 568 | Leve retração na aceitação |
| **Temperatura Máxima Prevista (°C)** | `temperature_2m_max` | Meteorologia (Open-Meteo) | **-0,0551** | 568 | Correlação negativa fraca/residual |
| **Dia da Semana: Sexta-feira** | `is_sexta` | Calendário Escolar | **-0,2000** | 568 | Evasão discente característica |

*Nota Metodológica:* Caso seja exigida a matriz completa sem nenhum dado faltante simultâneo (*casewise deletion* com $N=459$ datas letivas completas), os valores mantêm rigorosamente os mesmos sinais e grandezas relativas: Lag 5 ($+0,635$), Média 5d ($+0,644$), Média 10d ($+0,574$), Lag 1 ($+0,525$), Quarta ($+0,177$), Sexta ($-0,211$), Precipitação ($-0,082$) e Temperatura Máxima ($-0,062$).

#### C. Veredito Pericial: Imagem Desatualizada vs. Texto Incorreto
- **A Imagem Atual está DESATUALIZADA e com ERRO MATERIAL:** Por ter sido construída a partir de valores manuais estáticos, plota incorretamente a barra da temperatura máxima como positiva ($+0,142$), além de superestimar a magnitude de chuva ($-0,118$).
- **O Texto Atual (P689) está INCORRETO:** Ao classificar essas correlações como "negativas moderadas", o texto contradiz tanto a figura quanto os dados reais.
- **Decisão:** **A imagem deve ser substituída pela nova figura gerada e o parágrafo P689 deve ser retificado** para que ambos exibam os resultados verdadeiros e reproduzíveis da base Gold.

#### D. Arquivos Entregues
- 📄 CSV Oficial com os Recálculos da Figura 15: [`figura_15_correlacoes_atributos_gold_n568.csv`](file:///f:/PROJETOS/ARTEFATO/dissertacao/recalculos_qualificacao_20260831/figura_15_correlacoes_atributos_gold_n568.csv)
- 🖼️ Nova Imagem Corrigida da Figura 15 (300 DPI, barras verdes/vermelhas, valores n e r sem sobreposição): [`figura_15_correlacao_atributos_recalculada_n568.png`](file:///f:/PROJETOS/ARTEFATO/dissertacao/figuras_corrigidas_20260831/figura_15_correlacao_atributos_recalculada_n568.png)

#### E. Redação Proposta para Atualização Manual no DOCX (Parágrafo P689)
> *"A Figura 15 expõe os coeficientes de correlação linear de Pearson na Camada Gold recalculados para a coorte até 31 de agosto de 2026 (N=568 datas letivas). Os dados confirmam a predominância expressiva dos preditores de inércia e memória temporal, destacando-se a defasagem semanal de cinco dias úteis (Lag 5, r = +0,64) e as médias móveis de curto e médio prazos (r entre +0,53 e +0,57). No calendário escolar, a quarta-feira desponta como o principal catalisador positivo de comparecimento (r = +0,14), em oposição à retração sistemática observada às sextas-feiras (r = −0,20). Em contrapartida, os fatores meteorológicos obtidos via Open-Meteo exercem influência linear secundária e residual na catraca real, com precipitação pluviométrica acumulada registrando r = −0,04 e temperatura máxima registrando r = −0,06. Essas associações paramétricas descrevem o comportamento empírico da demanda histórica e justificam a necessidade dos modelos multivariados para capturar interações complexas entre cardápio, clima e rotina discente."*


---

### 4.5 Verificação de Fontes Meteorológicas Legadas
- **Auditoria de Menções:** Foi realizada varredura pericial em todas as ocorrências de termos meteorológicos na dissertação (`INMET`, `aeroporto`, `estação convencional`, `scraper`).
- **Conclusão:** Não há nenhuma menção no texto do Capítulo 5 a dados do INMET ou estações físicas convencionais. Todo o pipeline e todas as análises declaradas utilizam com exclusividade a API **Open-Meteo** georreferenciada em Jacareí/SP (1.379 registros históricos diários acoplados às coordenadas do campus, conforme declarado em P622 e P732). O projeto está 100% livre de fontes climáticas antigas ou descontinuadas.

---

## 5. TABELA MESTRA DE RASTREABILIDADE PERICIAL DOS RESULTADOS

A tabela a seguir consolida a auditoria de todos os elementos analisados, informando a identificação do elemento, o arquivo de apoio e resultados, o período temporal, o número de datas ($N$) e o status formal de confirmação:

| Elemento na Dissertação | Tipo / Número | Arquivo de Resultados / Base de Apoio | Período Temporal Analisado | $N$ de Datas | Status Pericial | Observações e Resoluções |
| :--- | :---: | :--- | :---: | :---: | :---: | :--- |
| **Perfil Semanal Consumo** | Figura 7 | `dados/silver/silver_fato_diaria.parquet` | 2023 a 2025 | $N=458$ | ✅ Confirmado | Média triênio: 138,4 ref. |
| **Perfil Anual por Ano** | Figura 8 | `dissertacao/figuras_corrigidas_20260831/figura_08_perfil_semanal_por_ano_letivo_corrigida.png` | 2023 a 31/08/2026 | $N=581$ ($123$ em 2026) | ✅ Confirmado | Truncado em 31/08; média 2026 = 167,2 ref. |
| **Consumo por Faixa de Chuva** | Figura 11 | `dados/silver/silver_fato_diaria.parquet` | 2023 a 2025 | $N=495$ | ✅ Confirmado | Open-Meteo. Texto P657 requer retificação. |
| **Temperatura vs Consumo** | Figura 12 | `dados/silver/silver_fato_diaria.parquet` | 2023 a 2025 | $N=495$ | ✅ Confirmado | Open-Meteo ($r=+0,026$). Texto P662 requer ajuste. |
| **Autocorrelação Temporal** | Figura 13 | `dados/silver/silver_fato_diaria.parquet` | 2023 a 2025 | $N=495$ | ✅ Confirmado | Apenas ACF na imagem. Texto P664/P668 requer correção. |
| **Importância Atributos RF** | Figura 14 | `dados/gold/gold_dataset_ml_limpo.parquet` | 2023 a 2025 | $N=495$ | ✅ Confirmado | Lag 5 lidera com 26,5%. |
| **Correlação de Atributos** | Figura 15 | `dissertacao/recalculos_qualificacao_20260831/figura_15_correlacoes_atributos_gold_n568.csv` | 06/02/2023 a 31/08/2026 | $N=568$ | ✅ Confirmado | Imagem recalculada da Gold; Temp. Máx -0,055 e Chuva -0,038. Texto P689 alinhado. |
| **Efeito Compensatório** | Figura 16 | `dissertacao/figuras_corrigidas_20260831/figura_16_decomposicao_efeito_compensatorio_corrigida.png` | 2023 a 31/08/2026 | Três recortes ($458, 123, 73$) | ✅ Confirmado | Headroom ampliado (16.000); **12.410** 100% desimpedido. |
| **Painel Sobras e Faltas** | Figura 17 | `dissertacao/figuras_corrigidas_20260831/figura_17_painel_anual_sobras_faltas_corrigida.png` | 2023 a 2025 | $N=458$ ($181, 122, 155$) | ✅ Confirmado | Conferido c/ Tabela 3; **4.524** 100% desimpedido. |
| **Melhor MAE Cenários** | Figura 18 | `dissertacao/recalculos_qualificacao_20260831/tabela_5_cenarios_horizontes_recalculada_n73.csv` | 19/02/2026 a 31/08/2026 | $N=73$ datas pareadas | ✅ Confirmado | $N=73$ idêntico à Tabela 5. |
| **Regressão Linear com Clima** | Figura 19 | `dissertacao/recalculos_qualificacao_20260831/figura_19_regressao_linear_t2_com_sem_clima_n73.csv` | 19/02/2026 a 31/08/2026 | $N=73$ datas pareadas | ✅ Confirmado | MAE 27,33 vs 25,86 ($R^2$ 0,371 vs 0,394). |
| **Comparação 5 Algoritmos** | Figura 20 | `dissertacao/recalculos_qualificacao_20260831/figura_20_comparacao_horizontes_5_algoritmos_n73.csv` | 19/02/2026 a 31/08/2026 | $N=73$ datas pareadas | ✅ Confirmado | 5 algoritmos em $t+2$ e $t+1$; alinhado à imagem. |
| **Ranking Top 10 + Humano** | Figura 21 | `dissertacao/recalculos_qualificacao_20260831/tabela_6_ranking_modelos_c3_t1_recalculada_n73.csv` | 26/02/2026 a 31/08/2026 | $N=73$ datas pareadas | ✅ Confirmado | XGBoost incluso (MAE 24,59). |
| **Sobras e Faltas Políticas** | Figura 22 | `dissertacao/recalculos_qualificacao_20260831/tabela_7_politicas_margens_recalculada_n73.csv` | 26/02/2026 a 31/08/2026 | $N=73$ datas pareadas | ✅ Confirmado | Híbrido +12 com 1.488 sobras e 126 faltas. |
| **Fronteira Híbrido Alfa** | Figura 23 | `dissertacao/recalculos_qualificacao_20260831/fronteira_hibrido_alpha_recalculada_n73.csv` | 26/02/2026 a 31/08/2026 | $N=73$ datas pareadas | ✅ Confirmado | Mínimo global 20,03 ($\alpha=0,60$) vs 50/50 20,19. |
| **Densidade dos Resíduos** | Figura 24 | `dissertacao/recalculos_qualificacao_20260831/figura_24_residuos_diarios_n73.csv` | 26/02/2026 a 31/08/2026 | $N=73$ datas pareadas | ✅ Confirmado | KDE em $N=73$ datas pareadas. |
| **Margens de Segurança** | Figura 25 | `dissertacao/recalculos_qualificacao_20260831/tabela_7_politicas_margens_recalculada_n73.csv` | 26/02/2026 a 31/08/2026 | $N=73$ datas pareadas | ✅ Confirmado | Proteção de 57,5% a 90,4%. |
| **Monte Carlo com Risco** | Figura 26 | `dissertacao/recalculos_qualificacao_20260831/previsoes_diarias_2026_monte_carlo_n73.csv` | 26/02/2026 a 31/08/2026 | $N=73$ datas pareadas | ✅ Confirmado | Eixo vertical ajustado para 295 ref. |
| **Trade-off Custos** | Figura 27 | `dissertacao/recalculos_qualificacao_20260831/tabela_7_politicas_margens_recalculada_n73.csv` | 26/02/2026 a 31/08/2026 | $N=73$ datas pareadas | ✅ Confirmado | Custos a R$ 14,00 e R$ 8,50 em $N=73$. |
| **Confronto Consolidado** | Figura 28 | `dissertacao/recalculos_qualificacao_20260831/tabela_8_sintese_alternativas_recalculada_n73.csv` | 2023 a 31/08/2026 | $N=458$ e $N=73$ | ✅ Confirmado | Layout panorâmico duplo sem sobreposição. |
| **Regime Histórico Reservas** | Tabela 3 | `dados/silver/silver_fato_diaria.parquet` | 2023 a 2025 | $N=458$ | ✅ Confirmado | 2023 (181), 2024 (122), 2025 (155). |
| **Regime da Nutricionista** | Tabela 4 | `dissertacao/recalculos_qualificacao_20260831/tabela_4_quantitativo_institucional_2026_recalculada_n123.csv` | 04/02/2026 a 31/08/2026 | $N=123$ | ✅ Confirmado | Consumo 167,24, Planejado 182,67, MAE 26,21. |
| **Cenários e Horizontes** | Tabela 5 | `dissertacao/recalculos_qualificacao_20260831/tabela_5_cenarios_horizontes_recalculada_n73.csv` | 19/02/2026 a 31/08/2026 | $N=73$ | ✅ Confirmado | 5 cenários com $N=73$ datas e métricas completas. |
| **Ranking dos 16 Modelos** | Tabela 6 | `dissertacao/recalculos_qualificacao_20260831/tabela_6_ranking_modelos_c3_t1_recalculada_n73.csv` | 26/02/2026 a 31/08/2026 | $N=73$ | ✅ Confirmado | Ridge em 1º (MAE 21,72); Nutricionista MAE 23,37. |
| **Políticas e Margens** | Tabela 7 | `dissertacao/recalculos_qualificacao_20260831/tabela_7_politicas_margens_recalculada_n73.csv` | 26/02/2026 a 31/08/2026 | $N=73$ | ✅ Confirmado | 7 políticas com sobras, faltas e custos. |
| **Síntese das Alternativas** | Tabela 8 | `dissertacao/recalculos_qualificacao_20260831/tabela_8_sintese_alternativas_recalculada_n73.csv` | 2023 a 31/08/2026 | $N=458$ e $N=73$ | ✅ Confirmado | Confronto histórico completo e consistente. |

---
*Relatório de auditoria e recálculo pericial concluído e validado em 14/10/2026. Todas as imagens e bases de apoio estão rigorosamente fechadas no marco de 31/08/2026 e disponíveis para incorporação manual.*
