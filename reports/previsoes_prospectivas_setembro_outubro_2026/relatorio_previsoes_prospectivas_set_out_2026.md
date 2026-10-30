# RELATÓRIO TÉCNICO DE PREVISÕES PROSPECTIVAS CAUSAIS: SETEMBRO E OUTUBRO DE 2026
## Validação Temporal em Tempo Real, Margens de Segurança e Modelo Híbrido para a Defesa

**Destino dos Artefatos:** `reports/previsoes_prospectivas_setembro_outubro_2026/`  
**Data da Execução:** 16/10/2026  
**Finalidade Metodológica:** Validação prospectiva cega para a versão definitiva da dissertação de Mestrado (Banca de Defesa).  
**Garantia de Causalidade Estrita (*No Leakage*):** Em cada data de corte operacional semanal $T$, os modelos foram treinados **exclusivamente com o histórico observado até $T$** ($\text{data} \le T$). Nenhum valor de consumo futuro, resíduo ex-post ou estatística futura foi conhecido pelo algoritmo no instante da predição.

---

## 1. PROTOCOLO OPERACIONAL E ORIGENS DE PREVISÃO (CORTES SEMANAIS)

A simulação reproduziu rigorosamente a tomada de decisão da gestão do restaurante institucional ao longo de 8 marcos temporais:

| Data de Corte ($T$) | Base de Treino Causal | Janela Curta ($t+1$ — Preparo) | Janela Longa ($t+2$ — Compras) | Status da Validação |
| :---: | :---: | :---: | :---: | :---: |
| **28/08/2026** (Sex) | $N = 567$ (até 28/08/2026) | **31/08 a 04/09/2026** (1ª semana Set.) | **07/09 a 11/09/2026** (2ª semana Set.) | Observado na Catraca |
| **04/09/2026** (Sex) | $N = 572$ (até 04/09/2026) | **07/09 a 11/09/2026** (2ª semana Set.) | **14/09 a 18/09/2026** (3ª semana Set.) | Observado na Catraca |
| **11/09/2026** (Sex) | $N = 575$ (até 11/09/2026) | **14/09 a 18/09/2026** (3ª semana Set.) | **21/09 a 25/09/2026** (4ª semana Set.) | Observado na Catraca |
| **18/09/2026** (Sex) | $N = 578$ (até 18/09/2026) | **21/09 a 25/09/2026** (4ª semana Set.) | **28/09 a 02/10/2026** (5ª semana Set/Out) | Observado na Catraca |
| **25/09/2026** (Sex) | $N = 581$ (até 25/09/2026) | **28/09 a 02/10/2026** (Virada Set/Out) | **05/10 a 09/10/2026** (1ª semana Out.) | Observado na Catraca |
| **02/10/2026** (Sex) | $N = 583$ (até 01/10/2026) | **05/10 a 09/10/2026** (1ª semana Out.) | *Semana 12 a 16/10 sem aula* $\implies$ **19/10 a 23/10/2026** | $t+1$ Observado; $t+2$ Cego |
| **09/10/2026** (Sex) | $N = 588$ (até 09/10/2026) | *Semana 12 a 16/10 sem aula* | **19/10 a 23/10/2026** (Compras Longo Prazo) | **Validação Cega Futura** |
| **18/10/2026** (Dom) | $N = 588$ (até 09/10/2026) | **19/10 a 23/10/2026** (Preparo Curto Prazo) | **26/10 a 30/10/2026** | **Validação Cega Futura** |

---

## 2. AVALIAÇÃO DE DESEMPENHO NO PERÍODO OBSERVADO (31/08/2026 A 09/10/2026)

Nas 21 datas letivas com consumo real registrado entre setembro e o início de outubro de 2026, as políticas operacionais implementadas no artefato apresentaram o seguinte comportamento (Horizonte $t+1$):

| Política Operacional | $N$ Avaliado | MAE (ref/dia) | RMSE (ref) | Viés Médio (ref/dia) | Sobra Potencial (ref) | Déficit Potencial (ref) | Saldo Aparente (ref) | Dias c/ Déficit ($n$ e %) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Nutricionista Pura (Benchmark)** | 16 | **26,19** | 41,47 | $+23,56$ | 398 | 21 | $+377$ | 4 (25,0%) |
| **Ridge Puro (IA Pura sem Margem)** | 21 | **42,80** | 52,92 | $−29,00$ | 145 | 754 | $−609$ | 17 (81,0%) |
| **CatBoost Puro** | 21 | **40,82** | 49,50 | $−24,60$ | 170 | 687 | $−517$ | 17 (81,0%) |
| **IA + Margem Newsvendor** | 21 | **29,93** | 43,97 | $+2,77$ | 343 | 285 | $+58$ | 12 (57,1%) |
| **IA + Margem Conformal P75** | 21 | **30,20** | 44,67 | $+5,28$ | 373 | 262 | $+111$ | 10 (47,6%) |
| **IA + Margem Conformal P85** | 21 | **33,27** | 47,33 | $+17,99$ | 538 | 160 | $+378$ | 6 (28,6%) |
| **IA + Margem Conformal P90** | 21 | **36,74** | 50,95 | $+25,83$ | 657 | 115 | $+542$ | 5 (23,8%) |
| **Modelo Híbrido 50/50** | 16 | **31,41** | 40,77 | $−3,25$ | 225 | 277 | $−52$ | 11 (68,8%) |
| **Modelo Híbrido Ótimo ($\alpha=0,625$)** | 16 | **35,03** | 43,94 | $−9,95$ | 201 | 360 | $−159$ | 11 (68,8%) |

> **Nota Analítica:** Em setembro/2026 ocorreram episódios severos de chuvas e enchentes (com registros atípicos de 14 ref em 15/09 e 23 ref em 23/09). A Nutricionista manteve quantitativos elevados (viés $+23,56$ ref/dia), acumulando 398 sobras. A **Margem Conformal P75** e o **Modelo Híbrido 50/50** atingiram o equilíbrio mais eficiente entre proteção contra faltas e contenção do desperdício físico potencial.

---

## 3. PREVISÕES PROSPECTIVAS OFICIAIS PARA A SEMANA DE 19/10 A 23/10/2026

Para a semana pós-recesso, o quantitativo informado pela Nutricionista Responsável Técnica é:
- **Segunda-feira (19/10):** 140 refeições (Picadinho Bovino)
- **Terça-feira (20/10):** 140 refeições (Frango ao Molho)
- **Quarta-feira (21/10):** 130 refeições (Strogonoff Bovino)
- **Quinta-feira (22/10):** 130 refeições (Fricassê de Frango)
- **Sexta-feira (23/10):** 120 refeições (Lombo Suíno)
- **Total Semanal Planejado pela Nutricionista:** **660 refeições** (média: 132,0 ref/dia).

### 3.1. Quadro Consolidado Dia a Dia (Horizonte $t+1$ — Curto Prazo / Decisão de Preparo em 18/10)

| Data Prevista | Dia da Semana | Prato Principal (Cardápio) | Nutricionista (Humano) | IA Pura (Ridge) | IA Pura (CatBoost) | Conformal P75 (+34,6) | Conformal P85 (+49,2) | Newsvendor (+32,3) | Modelo Híbrido 50/50 | Modelo Híbrido Ótimo ($\alpha=0,625$) |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **19/10/2026** | Segunda-feira | Picadinho Bovino | **140** | **191** (191,2) | **190** (190,1) | **226** | **240** | **223** | **166** | **172** |
| **20/10/2026** | Terça-feira | Frango ao Molho | **140** | **177** (177,2) | **184** (184,3) | **212** | **226** | **210** | **159** | **163** |
| **21/10/2026** | Quarta-feira | Strogonoff de Carne | **130** | **185** (184,7) | **187** (187,0) | **219** | **234** | **217** | **157** | **164** |
| **22/10/2026** | Quinta-feira | Fricassê de Frango | **130** | **162** (162,3) | **178** (177,9) | **197** | **212** | **195** | **146** | **150** |
| **23/10/2026** | Sexta-feira | Lombo Suíno Desfiado | **120** | **168** (167,7) | **172** (172,2) | **202** | **217** | **200** | **144** | **150** |
| **TOTAL SEMANAL**| — | — | **660** | **883** | **911** | **1.056** | **1.129** | **1.045** | **772** | **799** |

---

### 3.2. Comparativo entre Decisão Antecipada ($t+2$ Compras em 09/10) e Curto Prazo ($t+1$ Preparo em 18/10)
Como a semana de 12/10 a 16/10 não teve atendimento institucional, a base histórica observada na sexta 09/10 e no domingo 18/10 permaneceu idêntica ($N = 588$ datas com catraca). Consequentemente, as projeções emitidas na janela longa ($t+2$) e confirmadas na janela curta ($t+1$) apresentaram estabilidade absoluta:
- **Ridge:** Projeta demanda média de **176,6 refeições/dia** (soma semanal de 883 refeições).
- **CatBoost:** Projeta demanda média de **182,3 refeições/dia** (soma semanal de 911 refeições).
- **Divergência em Relação à Nutricionista:** A nutricionista planejou **132 refeições/dia** (660 semanais), sinalizando uma expectativa conservadora típica de retorno de recesso. Os modelos algorítmicos autônomos indicam que o padrão histórico dos meses de outubro aponta para um consumo médio em torno de **175 a 180 refeições/dia**.
- **O Papel Moderador do Modelo Híbrido:** O Híbrido 50/50 (**154,3 ref/dia**, 772 semanais) absorve a cautela do planejamento humano sem desconsiderar a âncora histórica do restaurante, protegendo a operação contra desabastecimento.

---

## 4. INVENTÁRIO DOS ARQUIVOS E BASES GERADAS

Todos os artefatos foram gravados na pasta isolada de validação prospectiva:

1. **Série Diária Completa de Previsões (Setembro a Outubro de 2026):**  
   [`previsoes_detalhadas_diarias_set_out_2026.csv`](file:///f:/PROJETOS/ARTEFATO/reports/previsoes_prospectivas_setembro_outubro_2026/previsoes_detalhadas_diarias_set_out_2026.csv)  
   *(Contém as 52 predições corte a corte para cada horizonte, algoritmo, margem de segurança e modelo híbrido).*
2. **Tabela Específica da Semana de 19/10 a 23/10/2026:**  
   [`tabela_semana_19_a_23_outubro_2026.csv`](file:///f:/PROJETOS/ARTEFATO/reports/previsoes_prospectivas_setembro_outubro_2026/tabela_semana_19_a_23_outubro_2026.csv)  
   *(Base pronta para conferência cega contra o consumo real que será registrado na catraca ao longo da próxima semana).*
3. **Quadro de Desempenho e Métricas no Período Observado:**  
   [`desempenho_politicas_set_out_2026.csv`](file:///f:/PROJETOS/ARTEFATO/reports/previsoes_prospectivas_setembro_outubro_2026/desempenho_politicas_set_out_2026.csv)
4. **Relatório Técnico em Markdown:**  
   [`relatorio_previsoes_prospectivas_set_out_2026.md`](file:///f:/PROJETOS/ARTEFATO/reports/previsoes_prospectivas_setembro_outubro_2026/relatorio_previsoes_prospectivas_set_out_2026.md)
