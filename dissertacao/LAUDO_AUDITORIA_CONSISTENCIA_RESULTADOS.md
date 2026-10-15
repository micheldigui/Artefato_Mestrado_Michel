# LAUDO COMPLEMENTAR DE AUDITORIA DE CONSISTÊNCIA METODOLÓGICA E NUMÉRICA (SOMENTE LEITURA)

**Documento Auditado:** `F:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_resultados_parciais_20261013_entrega.docx`  
**Data da Auditoria:** 14/10/2026  
**Regime da Auditoria:** Estritamente Leitura / Reproducibilidade Analítica em Memória (sem alteração em scripts, notebooks, bases de dados ou DOCX).  
**Regra Mandatória de Qualificação:** O período retrospectivo de avaliação encerra-se formal e estritamente em **31/08/2026**. Qualquer dado, simulação ou resultado contendo datas de setembro, outubro ou novembro de 2026 pertence à validação prospectiva da defesa e **não pode integrar a versão de qualificação**.

---

## 1. RASTREABILIDADE DAS FONTES FÍSICAS DE DADOS DO REPOSITÓRIO

| Camada / Artefato | Caminho Físico Realmente Existente | Granularidade / Chave | Extensão Temporal Real | Total Registros |
| :--- | :--- | :--- | :--- | :--- |
| **Silver (Fato Diária)** | `F:\PROJETOS\ARTEFATO\dados\silver\silver_fato_diaria.parquet` | Diária (`data`) | 01/01/2023 a 31/12/2026 | 1.461 linhas (648 consumo > 0; 640 letivas) |
| **Silver (Consumo)** | `F:\PROJETOS\ARTEFATO\dados\silver\silver_consumo.parquet` | Diária (`data`) | 01/02/2023 a 09/10/2026 | 655 registros brutos de catraca |
| **Gold (Limpa ML)** | `F:\PROJETOS\ARTEFATO\dados\gold\gold_dataset_ml_limpo.parquet` | Diária supervisionada | 06/02/2023 a 09/10/2026 | 588 linhas $\times$ 106 atributos |
| **Gold (Métricas Cenários)** | `F:\PROJETOS\ARTEFATO\dados\gold\metricas_modelos_cenarios.csv` | Cenário $\times$ Horiz $\times$ Algoritmo | Validação em Janela Expansiva | 61 linhas (separador `;`) |
| **Gold (Predições Walk-Forward)**| `F:\PROJETOS\ARTEFATO\dados\gold\predicoes_detalhadas_walk_forward.parquet` | Data $\times$ Modelo $\times$ Horizonte | 09/02/2026 a 09/10/2026 | Predições ponto a ponto |
| **Reports (Monte Carlo)** | `F:\PROJETOS\ARTEFATO\reports\tabelas\previsoes_diarias_2026_monte_carlo.parquet` | Diária 2026 | 26/02/2026 a 25/09/2026 | 83 linhas (73 até 31/08 e 10 em setembro) |
| **Reports (Políticas Margens)** | `F:\PROJETOS\ARTEFATO\reports\tabelas\comparativo_politicas_margens_seguranca.csv` | Política operacional | Coorte 2026 ($N=83$) | 7 políticas simuladas |
| **Reports (Confronto Regimes)** | `F:\PROJETOS\ARTEFATO\reports\tabelas\tabela_confronto_regimes_com_artefato.csv` | Estratégia institucional | 2023–2025 ($N=458$) e 2026 ($N=83$) | 5 estratégias consolidadas |
| **Reports (Efeito Compensatório)**| `F:\PROJETOS\ARTEFATO\reports\tabelas\tabela_efeito_compensatorio_anual.csv` | Ano letivo | 2023 a 2026 | 4 linhas (2023: 181, 2024: 122, 2025: 155, 2026: 140) |
| **Reports (Fronteira Híbrida)** | `F:\PROJETOS\ARTEFATO\reports\tabelas\fronteira_pareto_modelo_hibrido.csv` | Ponderação $\alpha$ (0 a 1) | Coorte 2026 ($N=83$) | 41 pontos amostrais de $\alpha$ |

---

## 2. AUDITORIA ITEM A ITEM DOS CONFLITOS E CONTRADIÇÕES

### Item 1: Figura 7 — Perfil Semanal de Consumo (2023 a 2025)
- **Código Fonte:** `src/gerar_todas_figuras_dissertacao.py:57-95` (`gerar_figura_07_perfil_semanal_consumo`).
- **Base Lida e Filtro:** `silver_fato_diaria.parquet`, filtrando `ano.isin([2023, 2024, 2025]) & (consumo > 0) & (is_dia_letivo == 1)`.
- **Estatísticas Reproduzidas no Filtro Silver ($N=495$ dias letivos totais no triênio):**
  - **Segunda-feira:** Média = **140,03** refeições ($N=100$, erro padrão = 4,75)
  - **Terça-feira:** Média = **133,25** refeições ($N=96$, erro padrão = 3,24)
  - **Quarta-feira:** Média = **143,01** refeições ($N=100$, erro padrão = 3,97)
  - **Quinta-feira:** Média = **122,22** refeições ($N=99$, erro padrão = 3,19)
  - **Sexta-feira:** Média = **131,31** refeições ($N=97$, erro padrão = 4,17)
  - **Sábado letivo:** Média = **36,33** refeições ($N=3$, erro padrão = 8,35) — *não plotado no gráfico semanal, mas presente no filtro*.
  - **Média Geral da Imagem (Segunda a Sexta, $N=492$):** **134,01** refeições.
  - **Média Geral Total (incluindo os 3 sábados letivos, $N=495$):** **133,42** refeições.
- **Rastreamento dos Valores Conflitantes:**
  - **Valores da Imagem Incorporada (`media/image7.png`):** Exibe exatamente **140,0**, **133,2**, **143,0**, **122,2** e **131,3**. A imagem foi gerada com a base **Silver** e está matematicamente confirmada.
  - **Origem dos Valores Alternativos (139,6; 135,4; 138,1; 122,3; 116,6):** Foram gerados a partir da base **Gold** (`gold_dataset_ml_limpo.parquet`, $N=446$ no triênio: Seg 139,59, N=93; Ter 135,36, N=91; Qua 138,11, N=90; Qui 122,31, N=94; Sex 116,56, N=78).
  - **Origem do Texto Legado (168, 172, 152, 124):** Resíduo textual de versão anterior que usava amostragem restrita sem filtros de greve.
- **Conclusão:** **CONFIRMADO NA IMAGEM; DIVERGENTE NO TEXTO**. O texto após a Figura 7 (parágrafos P627 a P630) deve ser corrigido para adotar estritamente os valores da base Silver exibidos na imagem: segunda 140,0; terça 133,2; quarta 143,0; quinta 122,2; sexta 131,3.

---

### Item 2: Figura 8 — Médias Anuais e Recorte Temporal de 2026
- **Código Fonte:** `src/gerar_todas_figuras_dissertacao.py:96-128` (`gerar_figura_08_perfil_semanal_por_ano`).
- **Base Lida e Filtro:** `silver_fato_diaria.parquet`, filtrando `consumo > 0 & is_dia_letivo == 1`.
- **Estatísticas Reproduzidas no Código:**
  - **Ano 2023:** Média = **107,80** refeições ($N=181$ datas letivas, 06/02/2023 a 11/12/2023)
  - **Ano 2024:** Média = **157,70** refeições ($N=145$ datas letivas, 15/02/2024 a 20/12/2024)
  - **Ano 2025:** Média = **140,02** refeições ($N=169$ datas letivas, 19/02/2025 a 11/12/2025)
  - **Ano 2026 (Código sem corte):** Média = **168,09** refeições ($N=145$ datas letivas, 04/02/2026 a **09/10/2026**)
- **Impacto do Corte Temporal em 31/08/2026 em 2026:**
  - **2026 até 31/08/2026 ($N=123$ datas letivas com consumo):** Média = **167,24** refeições.
  - **2026 após 31/08/2026 ($N=22$ datas letivas em set/out):** Média = **172,86** refeições.
  - **Vazamento Identificado:** A Figura 8 incorporada exibe $2026 = \mathbf{168,1}$, comprovando que **incluiu 22 datas de setembro e outubro de 2026**.
- **Distinção entre 655, 640 e 588:**
  - **655:** Total bruto de dias com registro na catraca em `silver_consumo.parquet`.
  - **640:** Datas letivas com consumo positivo em `silver_fato_diaria.parquet` ($181 + 145 + 169 + 145 = 640$).
  - **588:** População supervisionada final da Camada **Gold** (`gold_dataset_ml_limpo.parquet`), que exige 10 defasagens contínuas completas e exclui feriados emendados, recessos e anomalias de greve ($174 + 113 + 160 + 141 = 588$).
- **Conclusão:** **DIVERGENTE (VIOLAÇÃO DO RECORTE TEMPORAL)**. A Figura 8 inclui dados até 09/10/2026. A qualificação exige truncar 2026 em 31/08/2026 ($N=123$, média 167,2). O texto deve parar de chamar $N=588$ de "todos os registros da catraca", designando-o como "conjunto supervisionado limpo da Camada Gold".

---

### Item 3: Figuras 9 e 10 — Oferta e Consumo por Proteína e Técnica de Preparo
- **Código Fonte:** `src/gerar_todas_figuras_dissertacao.py:130-196`.
- **Base Lida e Filtro:** `silver_fato_diaria.parquet` (2023–2025, letivo, consumo > 0).
- **Estatísticas Reproduzidas da Figura 9 (Proteína Principal):**
  - Mista: Média = **141,0** ($n=23$)
  - Feijoada: Média = **137,9** ($n=17$)
  - Suína: Média = **135,3** ($n=83$)
  - Frango: Média = **134,2** ($n=174$)
  - Bovina: Média = **133,5** ($n=166$)
  - Peixe: Média = **126,0** ($n=23$)
  - Descrições ausentes/não categorizadas: $n=9$ (consumo médio 89,0 — excluídas do gráfico).
  - *Total com proteína identificada:* $N = 486$ datas.
- **Estatísticas Reproduzidas da Figura 10 (Técnica de Preparo — 9 Categorias Exatas):**
  - Frito: Média = **164,5** ($n=4$)
  - Assado: Média = **142,8** ($n=84$)
  - Churrasco/espeto: Média = **140,8** ($n=26$)
  - Ao molho/refogado: Média = **135,8** ($n=125$)
  - Grelhado: Média = **133,9** ($n=35$)
  - Cozido/refogado: Média = **133,7** ($n=57$)
  - Empanado/à milanesa: Média = **128,3** ($n=40$)
  - Massa/montado: Média = **127,0** ($n=52$)
  - Cremoso/ensopado: Média = **125,4** ($n=63$)
  - Ausentes: $n=9$ (média 89,0).
- **Confronto:** As imagens incorporadas no DOCX (`media/image9.png` e `media/image10.png`) exibem exatamente estas **6 proteínas** e **9 técnicas de preparo**. O texto do parágrafo P643 do DOCX cita incorretamente "165 a 178 refeições" e menciona "ovos", que não constam na figura.
- **Conclusão:** **CONFIRMADO NAS IMAGENS; DIVERGENTE NO TEXTO**. Os valores exatos das 6 proteínas e 9 preparações são os reproduzidos acima. O parágrafo P643 deve ser corrigido para refletir a amplitude real (126,0 a 141,0 na proteína; 125,4 a 164,5 no preparo), expurgando a menção a ovos.

---

### Item 4: Figura 11 — Precipitação e Faixas de Chuva
- **Código Fonte:** `src/gerar_todas_figuras_dissertacao.py:197-240`.
- **Coluna Utilizada:** `precipitation_sum` de `silver_fato_diaria.parquet` (janela 2023–2025, letivo, consumo > 0, $N=495$).
- **Estatísticas Reproduzidas Diretamente no Dataset:**
  - **Sem chuva ($p = 0$ mm):** Média = **138,8** refeições ($n = 213$)
  - **Chuva fraca ($0 < p \le 5$ mm):** Média = **131,4** refeições ($n = 192$)
  - **Chuva moderada ($5 < p \le 15$ mm):** Média = **128,7** refeições ($n = 58$)
  - **Chuva forte ($p > 15$ mm):** Média = **118,1** refeições ($n = 32$)
  - **Diferença Bivariada Bruta:** $138,85 - 118,12 = \mathbf{20,72}$ refeições/dia.
- **Confronto:** A imagem incorporada (`media/image11.png`) exibe com exatidão $n=213$, $n=192$, $n=58$ e $n=32$, com as médias 138,8, 131,4, 128,7 e 118,1. O parágrafo P654 do DOCX omitia a faixa de chuva moderada e citava 131,2.
- **Conclusão:** **CONFIRMADO NA IMAGEM; DIVERGENTE NO TEXTO**. O texto deve ser corrigido para citar as 4 faixas exatas e ressaltar que a redução de 20,7 refeições é descritiva/marginal, sem controle multivariado.

---

### Item 5: Figura 12 — Temperatura Máxima e Consumo
- **Código Fonte:** `src/gerar_todas_figuras_dissertacao.py:241-272`.
- **Coluna Utilizada:** `temperature_2m_max` em `silver_fato_diaria.parquet` (2023–2025, $N=495$).
- **Métrica Reproduzida:** Pearson $r = \mathbf{+0,0260}$ ($p = 0,564$).
- **Tipo de Ajuste no Código:** O script executa:
  ```python
  sns.regplot(x='temperature_2m_max', y='consumo', data=df_hist, ax=ax, ...)
  ```
  O `sns.regplot` desenha uma **regressão linear simples de 1º grau** ($y = ax + b$) com banda de 95% de confiança por bootstrap. **Não há curva polinomial nem ajuste Loess no código**.
- **Origem dos Dados Meteorológicos:**
  - Na Camada Silver (`silver_clima.parquet`), os dados foram baixados via API histórica diária da Open-Meteo.
  - Para a modelagem preditiva em $t+1$ e $t+2$ na Camada Gold, foi utilizada a **Previous Runs API da Open-Meteo**, que recupera previsões meteorológicas arquivadas geradas previamente ao evento, evitando vazamento retrospectivo.
- **Conclusão:** **CONFIRMADO NA IMAGEM (AJUSTE LINEAR COM $r=0,026$); DIVERGENTE NO TEXTO**. O texto do parágrafo P660 deve declarar ajuste linear e ausência de correlação linear relevante ($r = 0,026$), sem especular efeitos quadráticos não comprovados.

---

### Item 6: Figuras 13 e 15 — Autocorrelação Temporal (ACF) vs. Correlação entre Atributos
- **Figura 13 (Autocorrelação Serial do Consumo na Silver 2023–2025, $N=495$):**
  - Calculada pela função ACF sobre a série ordenada de consumo diário:
    - Lag 1: **0,590** | Lag 2: **0,542** | Lag 3: **0,465** | Lag 4: **0,403** | Lag 5: **0,469** | Lag 10: **0,390**.
  - A imagem incorporada (`media/image13.png`) destaca os picos da sazonalidade semanal em Lag 5 e Lag 10.
- **Figura 15 (Correlação de Pearson com a Variável-Alvo na Gold, $N=588$):**
  - Consumo mesmo dia semana passada (Lag 5): **+0,592**
  - Média móvel 5 dias: **+0,566**
  - Média móvel 10 dias: **+0,528**
  - Lag 1 dia letivo: **+0,485**
  - Lag 5 dias letivos: **+0,477**
  - Lag 2 dias letivos: **+0,453**
  - Variável temporal Dia da semana numérico / Sexta-feira: **−0,280**
- **Confronto:** O parágrafo P666 misturou a ACF com correlação de atributos. O parágrafo P687 citava generalização espúria de "Spearman > 0,65".
- **Conclusão:** **DIVERGENTE NO TEXTO**. O texto de P666 deve tratar unicamente da inércia serial da demanda (ACF com picos em 5 e 10 dias). O texto de P687 deve tratar da matriz de correlação de Pearson na Gold, indicando que as maiores associações estão nas médias móveis e defasagens de 5 dias (~0,57 a 0,59).

---

### Item 7: Figura 17 — Painel Anual de Sobras e Faltas (Reservas 2023–2025)
- **Tabela Canônica:** `reports/tabelas/tabela_efeito_compensatorio_anual.csv` (e Tabela 3 do DOCX).
- **Valores Canônicos Auditados:**
  - **2023:** $N = \mathbf{181}$ datas letivas | Sobras = **1.916** | Faltas = **1.174** | Saldo = $+742$
  - **2024:** $N = \mathbf{122}$ datas letivas | Sobras = **334** | Faltas = **4.524** | Saldo = $-4.190$
  - **2025:** $N = \mathbf{155}$ datas letivas | Sobras = **666** | Faltas = **3.796** | Saldo = $-3.130$
  - **Total Triênio:** $N = \mathbf{458}$ datas | Sobras = **2.916** | Faltas = **9.494** | Saldo = $-6.578$
- **Origem do Erro nos Rótulos da Imagem:**
  - O script `src/gerar_todas_figuras_dissertacao.py:400-435` continha listas manuais onde 2024 e 2025 foram inadvertidamente invertidos nos rótulos de texto: gerou a imagem com rótulo $2024 = 157$ e $2025 = 120$.
- **Conclusão:** **DIVERGENTE NA IMAGEM (ERRO DE RÓTULO)**. A Tabela 3 e o texto do parágrafo P710 estão corretos ($2023=181, 2024=122, 2025=155$). A imagem incorporada da Figura 17 precisa ser corrigida nos rótulos do eixo X.

---

### Item 8: Métricas dos Cenários Preditivos e Figuras 18, 19 e 20
- **Base Canônica:** `dados/gold/metricas_modelos_cenarios.csv` (61 linhas, separador `;`).
- **Definição dos Três Cenários Preditivos:**
  1. **Cenário 1 (`Cenario_1_Base_Cardapio`):** Calendário, defasagens (lags 1 a 10) e cardápio. Avaliado em $t+1$ e $t+2$.
  2. **Cenário 2 (`Cenario_2_Com_Clima`):** Incorpora as previsões meteorológicas da Open-Meteo. Avaliado em $t+1$ e $t+2$.
  3. **Cenário 3 (`Cenario_3_Com_Nutricionista`):** Incorpora a estimativa institucional da nutricionista. **Disponível unicamente em $t+1$**.
- **Gabarito Canônico da Tabela 5 (Métricas Auditadas do CSV):**
  - **Cenário 1, $t+2$:** Melhor = **XGBoost** ($\text{MAE} = \mathbf{29,50}$; $\text{RMSE} = 39,82$; $R^2 = 0,222$; $\text{WAPE} = 17,35\%$). Regressão Linear em $t+2$ obteve $\text{MAE} = \mathbf{30,01}$.
  - **Cenário 2, $t+2$:** Melhor = **Regressão Linear** ($\text{MAE} = \mathbf{28,67}$; $\text{RMSE} = 38,64$; $R^2 = 0,268$; $\text{WAPE} = 16,86\%$).
  - **Cenário 1, $t+1$:** Melhor = **XGBoost** ($\text{MAE} = \mathbf{27,81}$; $\text{RMSE} = 38,59$; $R^2 = 0,285$; $\text{WAPE} = 16,23\%$).
  - **Cenário 2, $t+1$:** Melhor = **Regressão Linear** ($\text{MAE} = \mathbf{27,39}$; $\text{RMSE} = 37,43$; $R^2 = 0,327$; $\text{WAPE} = 15,98\%$).
  - **Cenário 3, $t+1$:** Melhor = **Lasso** ($\text{MAE} = \mathbf{22,27}$; $\text{RMSE} = 32,33$; $R^2 = 0,498$; $\text{WAPE} = 12,99\%$) e **Ridge** ($\text{MAE} = \mathbf{22,46}$; $\text{RMSE} = 32,82$; $R^2 = 0,483$; $\text{WAPE} = 13,11\%$).
- **Origem dos Descompassos nas Figuras 18 a 20:**
  - `gerar_figura_16_melhor_mae_cenarios` (usada como Figura 18 no DOCX): continha listas fixas `[29.50, 29.10, 28.85, 28.67]` e `[25.80, 24.20, 22.80, 22.27]` divididas em 4 cenários artificiais.
  - `gerar_figura_18_ganho_reforecast` (usada como Figura 20 no DOCX): continha 5 algoritmos em $t+1$ e $t+2$, enquanto o título no DOCX chama "MAE do XGBoost".
- **Conclusão:** **CONFIRMADO NA TABELA 5; DIVERGENTE NAS FIGURAS 18 E 20**. A Tabela 5 está 100% aderente ao CSV canônico. As imagens das Figuras 18 e 20 devem ser geradas a partir do CSV `metricas_modelos_cenarios.csv`.

---

### Item 9: Tabela 6 e Figura 21 — Ranking Pareado de Modelos
- **Base Canônica:** `dados/gold/metricas_modelos_cenarios.csv` (filtrando `cenario == 'Cenario_3_Com_Nutricionista'` e `horizonte == 'Semana_t1 (Curto Prazo)'`, confrontado com `Benchmark_Humano`).
- **Ranking Completo dos 12 Modelos e Benchmark Institucional:**

| Posição | Algoritmo / Método | Família | $N$ | MAE | RMSE | $R^2$ | WAPE (%) | Sobra (ref) | Falta (ref) |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1º** | **Lasso** | Linear L1 | 83 | **22,27** | 32,33 | **0,498** | 12,99% | 1.107 | 741 |
| **2º** | **Ridge** | Linear L2 | 83 | **22,46** | 32,82 | **0,483** | 13,11% | 1.161 | 703 |
| **3º** | **Regressão Linear** | OLS | 83 | **22,87** | 32,56 | **0,491** | 13,34% | 916 | 981 |
| **Ref** | **Estimativa Institucional (Nutri)** | Benchmark Humano | 83 | **24,92** | 36,94 | **0,373** | 14,55% | 2.705 | 684 |
| **4º** | **LightGBM** | Gradient Boosting | 83 | **25,11** | 33,98 | **0,445** | 14,65% | 1.080 | 1.003 |
| **5º** | **ExtraTrees** | Ensembles / Random | 83 | **25,25** | 34,20 | **0,438** | 14,73% | 951 | 1.143 |
| **6º** | **Random Forest** | Bagging de Árvores | 83 | **25,27** | 35,24 | **0,403** | 14,74% | 1.051 | 1.045 |
| **7º** | **CatBoost** | Gradient Boosting | 83 | **25,65** | 35,17 | **0,406** | 14,96% | 971 | 1.157 |
| **8º** | **XGBoost** | Gradient Boosting | 83 | **26,02** | 35,42 | **0,397** | 15,18% | 1.094 | 1.064 |
| **9º** | **SVR** | Máquinas de Vetor de Suporte | 83 | **26,29** | 35,45 | **0,397** | 15,34% | 845 | 1.336 |
| **10º**| **KNN** | Baseado em Instâncias | 83 | **29,99** | 40,38 | **0,217** | 17,50% | 805 | 1.683 |
| **11º**| **Decision Tree** | Árvore de Decisão | 83 | **31,68** | 42,25 | **0,143** | 18,48% | 1.177 | 1.452 |
| **12º**| **MLP (Rede Neural)** | Perceptron Multicamadas | 83 | **34,58** | 46,52 | **−0,039**| 20,18% | 1.741 | 1.128 |

- **Conclusão:** **CONFIRMADO NO CSV; DIVERGENTE NA FIGURA 21 E INCOMPLETO NA TABELA 6**. O valor canônico do SVR é **26,29** (e não 23,10). A Tabela 6 pode ser expandida até o 9º colocado (SVR) e a Figura 21 deve ser gerada diretamente a partir do CSV canônico.

---

### Item 10: Figura 22, Tabela 7 e Quadro 13 — Políticas Operacionais e Margens
- **Bases Canônicas:** `reports/tabelas/comparativo_politicas_margens_seguranca.csv` e `reports/tabelas/previsoes_diarias_2026_monte_carlo.parquet`.
- **Reconciliação Exata das Políticas em $N=83$ (com set/2026) vs. $N=73$ (estrito até 31/08/2026):**

| Política Avaliada | Parâmetro | Coorte $N=83$ (Inclui Set/2026) | | | | Coorte $N=73$ (Qualificação até 31/08) | | | |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| | | **Sobra (ref)** | **Falta (ref)** | **Dias Falta** | **MAE** | **Sobra (ref)** | **Falta (ref)** | **Dias Falta** | **MAE** |
| **Nutricionista (Benchmark)** | Sem margem | **1.545** | **518** | **34 (41,0%)** | **24,86** | **1.198** | **508** | **32 (43,8%)** | **23,37** |
| **IA Pura (Ridge)** | Sem margem | **1.238** | **667** | **36 (43,4%)** | **22,97** | **1.057** | **529** | **31 (42,5%)** | **21,72** |
| **Ridge + Margem P75** | $+10$ ref | **1.749** | **383** | **21 (25,3%)** | **25,70** | **1.534** | **276** | **16 (21,9%)** | **24,80** |
| **Ridge + Margem P85** | $+19$ ref | **2.364** | **236** | **13 (15,7%)** | **31,34** | **2.072** | **157** | **10 (13,7%)** | **30,53** |
| **Ridge + Margem P90** | $+29$ ref | **3.074** | **123** | **9 (10,8%)** | **38,54** | **2.706** | **62** | **7 (9,6%)** | **37,92** |
| **Híbrido 50/50** | Sem margem | **1.289** | **489** | **36 (43,4%)** | **21,43** | **1.041** | **433** | **33 (45,2%)** | **20,19** |
| **Híbrido + Margem Fixa** | $+12$ ref | **1.994** | **199** | **14 (16,9%)** | **26,43** | **1.648** | **163** | **13 (17,8%)** | **24,81** |

- **Reconciliação das Tarifas:**
  - Nos arquivos `comparativo_politicas_margens_seguranca.csv` e `notebooks/06`, o custo foi programado com `CUSTO_POR_REFEICAO = 8.50`.
  - Na **Tabela 7** do DOCX, os custos foram multiplicados pela tarifa de contrato **R$ 14,00** ($1.545 \times 14 = \text{R\$} 21.630,00$; $1.289 \times 14 = \text{R\$} 18.046,00$).
  - Na ausência de cópia digitalizada do contrato, **R$ 14,00 deve ser classificado como "Tarifa Contratual Paramétrica Informada pela Gestão"**.
- **Duplicidades no Quadro 13:** A Tabela 15 do DOCX (Quadro 13) possui a primeira e a última linha idênticas (`Ridge sem margem`). A última linha deve ser deletada.
- **Conclusão:** **CONFIRMADO NA TABELA 7 (EM $N=83$); DIVERGENTE NA FIGURA 22 E NO QUADRO 13**. A Tabela 7 utilizou a coorte estendida $N=83$. A Figura 22 incorporada plota números fictícios (2.140 sobras / 295 faltas). Para a qualificação, a Tabela 7 e a Figura 22 devem ser recalculadas para $N=73$ (ou rotuladas explicitamente como teste estendido preliminar $N=83$).

---

### Item 11: Figura 23 — Curva do Modelo Híbrido e Ponderação $\alpha$
- **Base Canônica:** `reports/tabelas/fronteira_pareto_modelo_hibrido.csv` (41 pontos, $\alpha$ de 0,0 a 1,0 em passos de 0,025).
- **Mínimo Global:** $\alpha = 0,60$ atinge $\text{MAE} = \mathbf{21,28}$; $\alpha = 0,50$ atinge $\text{MAE} = \mathbf{21,43}$ (diferença de 0,15 ref/dia).
- **Eixos e Interpretação:** Eixo X = Ponderação da IA ($\alpha$); Eixo Y = MAE. Não é uma fronteira de Pareto de sobras vs. déficits.
- **Conclusão:** **CONFIRMADO NA BASE CANÔNICA; DIVERGENTE NO TEXTO**. O texto de P779 deve denominá-lo "Curva de Erro Médio Absoluto do Modelo Híbrido em função da ponderação da IA ($\alpha$)".

---

### Item 12: Figura 24 — Distribuição dos Erros Diários de Planejamento
- **Código Fonte:** `src/gerar_todas_figuras_dissertacao.py:768-793`.
- **Imagem Incorporada (`media/image24.png`):** Exibe as curvas KDE dos resíduos diários em 2026: Nutricionista (assimétrica à direita / superestimativa), Ridge (centrada em zero) e Híbrido 50/50 (compacta e menor variância).
- **Conclusão:** **CONFIRMADO NA IMAGEM; PARCIALMENTE DIVERGENTE NO TEXTO**. Ajustar parágrafos P793 e P794 para focar unicamente na distribuição de erros de 2026.

---

### Item 13: Figura 25 — Margens de Segurança Empíricas e Terminologia Conformal
- **Código Fonte:** `src/gerar_todas_figuras_dissertacao.py:794-835`.
- **Rastreamento dos Valores na Imagem:** O código continha `taxa_falta = [43.4, 25.3, 15.7, 9.6, 31.3, 14.5]`. O valor de 9,6% corresponde a $8 / 83 = 9,638\%$ em $N=83$.
- **Rigor Metodológico:** Como os quantis foram obtidos na distribuição residual histórica sem partição independente de calibração (*inductive conformal prediction*), o termo correto é **"Margens Empíricas de Segurança por Quantis de Resíduos"**.
- **Conclusão:** **DIVERGENTE EM VALORES E TERMINOLOGIA**. Retificar terminologia e adotar percentuais de $N=73$: Sem margem = 42,5% (31 dias); P75 (+10) = 21,9% (16 dias); P85 (+19) = 13,7% (10 dias); P90 (+29) = 9,6% (7 dias); Híbrido +12 = 17,8% (13 dias).

---

### Item 14: Figura 26 — Simulação de Monte Carlo e Eliminação de Setembro/2026
- **Base Canônica:** `reports/tabelas/previsoes_diarias_2026_monte_carlo.parquet` ($N=83$).
  - Linhas 0 a 72: **26/02/2026 a 31/08/2026** ($N = \mathbf{73}$ datas letivas).
  - Linhas 73 a 82: **01/09/2026 a 25/09/2026** ($N = \mathbf{10}$ datas de setembro).
- **Confronto:** A imagem da Figura 26 incorporada no DOCX plota o eixo temporal até 25/09/2026.
- **Conclusão:** **DIVERGENTE (BLOQUEADOR FORMAL DA QUALIFICAÇÃO)**. A série temporal da Figura 26 e a simulação de Monte Carlo devem ser truncadas em 31/08/2026 ($N=73$).

---

### Item 15: Figura 27, Tabela 8 e Figura 28 — Síntese Histórica, Custos e Taxas de Cobertura
- **Tabela 8 (Tabela 24 do Word):** Não possui coluna de custo calculada, contendo apenas a "Tarifa de referência" (R$ 17,36 e R$ 14,00).
- **Figura 28 (Síntese Geral dos Três Regimes):** A imagem (`media/image28.png`) plota cobertura de **80,7%** para a Nutricionista, enquanto a Tabela 4 do DOCX comprova que em todo o ano letivo de 2026 ($N=140$), a taxa de dias com déficit foi de **37,1%**, resultando em **62,9% de cobertura sem déficit**. Além disso, combina o MAE de 21,43 (do Híbrido puro) com a cobertura de 85,5% (do Híbrido com margem de segurança).
- **Conclusão:** **DIVERGENTE NA FIGURA 28**. A Figura 28 combina indicadores de coortes e políticas distintas em uma mesma barra. O visual deve discriminar os denominadores ou padronizar as políticas na coorte $N=73$.

---

## 3. TABELA PERICIAL COMPLETA DAS 28 FIGURAS DO DOCX

| Elemento DOCX | Posição no DOCX | Imagem Incorporada DOCX | Arquivo Fonte / Script | População e $N$ | Status | Ação Recomendada |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Figura 1** | P459 | `media/image1.jpeg` | `figura_01_aplicacao_dsr_pesquisa.png` | Conceitual DSR | **CONFIRMADO** | Nenhuma |
| **Figura 2** | P469 | `media/image2.jpeg` | `figura_02_sintese_metodologica.png` | Fluxo metodológico | **CONFIRMADO** | Nenhuma |
| **Figura 3** | P499 | `media/image3.png` | `figura_03_pipeline_dados_camadas.png` | Arquitetura Medallion | **CONFIRMADO** | Nenhuma |
| **Figura 4** | P521 | `media/image4.jpeg` | `figura_04_protocolo_modelagem_validacao.png` | Janela temporal expansiva | **CONFIRMADO** | Nenhuma |
| **Figura 5** | P558 | `media/image5.png` | `figura_05_arquitetura_sistemica_artefato.png` | Diagrama ensemble híbrido | **CONFIRMADO** | Ajustar menção conformal |
| **Figura 6** | P583 | `media/image6.png` | `figura_06_fluxo_operacional_artefato.png` | Fluxo operacional | **CONFIRMADO** | Ajustar menção conformal |
| **Figura 7** | P628 | `media/image7.png` | `src/...:57-95` (`silver_fato_diaria.parquet`) | 2023–2025 Silver ($N=495$) | **DIVERGENTE NO TEXTO** | Atualizar P627 com as médias da imagem |
| **Figura 8** | P636 | `media/image8.png` | `src/...:96-128` (`silver_fato_diaria.parquet`) | Letivo 2023–2026 ($N=640$) | **DIVERGENTE (TEMPORAL)**| Truncar 2026 em 31/08/2026 ($N=123$) |
| **Figura 9** | P642 | `media/image9.png` | `src/...:130-165` (`silver_fato_diaria.parquet`)| Proteínas 2023–2025 ($N=486$) | **DIVERGENTE NO TEXTO** | Ajustar P643 para amplitude real e excluir ovos |
| **Figura 10** | P647 | `media/image10.png` | `src/...:166-196` (`silver_fato_diaria.parquet`)| 9 preparações 2023–2025 ($N=486$) | **CONFIRMADO** | Alinhar parágrafo contextual com as 9 categorias |
| **Figura 11** | P653 | `media/image11.png` | `src/...:197-240` (`silver_fato_diaria.parquet`)| Precipitação 2023–2025 ($N=495$) | **DIVERGENTE NO TEXTO** | Inserir 4 faixas no texto e destacar natureza marginal |
| **Figura 12** | P658 | `media/image12.png` | `src/...:241-272` (`silver_fato_diaria.parquet`)| Temp Máx ($r=0,026$; reg linear) | **DIVERGENTE NO TEXTO** | Declarar ajuste linear simples e associação nula |
| **Figura 13** | P664 | `media/image13.png` | `src/...:273-305` (`silver_fato_diaria.parquet`)| ACF temporal do consumo | **DIVERGENTE NO TEXTO** | Focar P666 exclusivamente na inércia serial |
| **Figura 14** | P680 | `media/image14.png` | `src/...:306-340` (`gold_dataset_ml_limpo.parquet`)| Feature importance RF ($N=588$) | **CONFIRMADO** | Alinhar texto destacando peso dos lags |
| **Figura 15** | P685 | `media/image15.png` | `src/...:341-385` (`gold_dataset_ml_limpo.parquet`)| Correlação de Pearson ($N=588$) | **DIVERGENTE NO TEXTO** | Retificar texto para correlação de Pearson |
| **Figura 16** | P701 | `media/image16.png` | `src/...:386-436` | Efeito compensatório (2023–2026) | **CONFIRMADO** | Manter discussão sobre efeito compensatório |
| **Figura 17** | P706 | `media/image17.png` | `src/...:400-435` (`tabela_efeito_compensatorio_anual.csv`)| Reservas 2023–2025 ($N=458$) | **DIVERGENTE NA IMAGEM**| Corrigir rótulos do eixo X ($2024=122, 2025=155$) |
| **Figura 18** | P738 | `media/image18.png` | `dados/gold/metricas_modelos_cenarios.csv` | Modelagem walk-forward 3 cenários | **DIVERGENTE NA IMAGEM**| Gerar visual a partir do CSV canônico |
| **Figura 19** | P744 | `media/image19.png` | `dados/gold/metricas_modelos_cenarios.csv` | Dispersão t+2 com e sem clima | **CONFIRMADO** | Alinhar parágrafo P748 |
| **Figura 20** | P749 | `media/image20.png` | `dados/gold/metricas_modelos_cenarios.csv` | Comparação t+1 vs t+2 (5 modelos) | **DIVERGENTE NO TÍTULO** | Ajustar legenda para "Comparação por Algoritmo" |
| **Figura 21** | P759 | `media/image21.png` | `dados/gold/metricas_modelos_cenarios.csv` | Ranking t+1 Cenário 3 ($N=83$) | **DIVERGENTE NA IMAGEM**| Gerar imagem do CSV canônico (SVR = 26,29) |
| **Figura 22** | P764 | `media/image22.png` | `reports/tabelas/tabela_confronto_regimes_com_artefato.csv` | Políticas simuladas 2026 | **DIVERGENTE NA IMAGEM**| Atualizar imagem com dados da Tabela 7 |
| **Figura 23** | P779 | `media/image23.png` | `reports/tabelas/fronteira_pareto_modelo_hibrido.csv` | Varredura de $\alpha$ (0 a 1) | **DIVERGENTE NO TEXTO** | Chamar de "Curva de Erro MAE vs. $\alpha$" |
| **Figura 24** | P788 | `media/image24.png` | `src/...:768-793` | Resíduos diários 2026 ($N=83$) | **CONFIRMADO C/ AJUSTE** | Limpar menções residuais em P793/P794 |
| **Figura 25** | P806 | `media/image25.png` | `reports/tabelas/comparativo_politicas_margens_seguranca.csv` | Margens empíricas por quantis | **DIVERGENTE (MÉTODO)** | Retificar terminologia para quantis empíricos |
| **Figura 26** | P813 | `media/image26.png` | `reports/tabelas/previsoes_diarias_2026_monte_carlo.parquet`| Monte Carlo 2026 | **DIVERGENTE (BLOQUEADOR)**| Truncar série temporal estritamente em 31/08/2026 |
| **Figura 27** | P820 | `media/image27.png` | `reports/tabelas/comparativo_politicas_margens_seguranca.csv`| Trade-off custos ($N=83$) | **CONFIRMADO C/ RESSALVA**| Explicitar caráter paramétrico da tarifa informada |
| **Figura 28** | P829 | `media/image28.png` | `src/...:911-942` | Síntese de 3 regimes | **DIVERGENTE** | Inserir nota discriminando as coortes de cada bloco |

---

## 4. TABELA PERICIAL COMPLETA DAS 8 TABELAS DO DOCX

| Elemento DOCX | Posição no DOCX | Arquivo Fonte Canônico | População, Período e $N$ | Status | Ação Recomendada |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tabela 1** | P215 / Tab. Word 1 | `dados/silver/silver_fato_diaria.parquet` | Dicionário Silver 2023–2026 | **CONFIRMADO** | Nenhuma |
| **Tabela 2** | P230 / Tab. Word 7 | `dados/gold/gold_dataset_ml_limpo.parquet` | Pipeline Gold (655 -> 588) | **DIVERGENTE (FORMATO)** | Deletar linha final duplicando cabeçalhos |
| **Tabela 3** | P700 / Tab. Word 19 | `reports/tabelas/tabela_efeito_compensatorio_anual.csv` | Reservas Discentes 2023–2025 ($N=458$) | **CONFIRMADO** | Nenhuma |
| **Tabela 4** | P715 / Tab. Word 20 | Dados Nutricionista 2026 | Período Nutricionista 2026 ($N=140$) | **CONFIRMADO** | Manter distinção entre $N=140$ e $N=83/73$ |
| **Tabela 5** | P737 / Tab. Word 21 | `dados/gold/metricas_modelos_cenarios.csv` | Cenários 1, 2, 3 em $t+1, t+2$ | **CONFIRMADO** | Usar como gabarito para as Figuras 18 e 20 |
| **Tabela 6** | P758 / Tab. Word 22 | `dados/gold/metricas_modelos_cenarios.csv` | Ranking pareado $N=83$ (Cenário 3 $t+1$) | **CONFIRMADO PARCIAL** | Inserir linha do SVR com $\text{MAE} = 26,29$ |
| **Tabela 7** | P767 / Tab. Word 23 | `reports/tabelas/tabela_confronto_regimes_com_artefato.csv` | Políticas operacionais ($N=83$) | **CONFIRMADO EM N=83** | Explicitar uso de $N=83$ ou recalcular para $N=73$ |
| **Tabela 8** | P826 / Tab. Word 24 | Síntese Comparativa | Coortes 2023–2025 e 2026 | **DIVERGENTE NO TEXTO** | Ajustar texto para não prometer coluna de custo |

---

## 5. TABELA PERICIAL COMPLETA DOS 16 QUADROS DO DOCX

| Elemento DOCX | Posição no DOCX | Objeto Técnico / Conteúdo | Arquivo de Código / Script de Apoio | Status | Ação Recomendada |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Quadro 1** | P75 / Tab. Word 2 | Questões de pesquisa e objetivos | Metodologia DSR | **CONFIRMADO** | Nenhuma |
| **Quadro 2** | P95 / Tab. Word 3 | Revisão sistemática sobre UANs | Fundamentação teórica | **CONFIRMADO** | Nenhuma |
| **Quadro 3** | P112 / Tab. Word 4 | Comparativo de abordagens preditivas | Séries temporais vs. ML | **CONFIRMADO** | Nenhuma |
| **Quadro 4** | P145 / Tab. Word 5 | Mapeamento das 6 etapas da DSR | Ciclo DSR aplicado | **CONFIRMADO** | Nenhuma |
| **Quadro 5** | P195 / Tab. Word 6 | Fontes de dados primárias integradas | `notebooks/01_ingestao_dados.ipynb` | **CONFIRMADO** | Nenhuma |
| **Quadro 6** | P215 / Tab. Word 8 | Regras de tratamento e imputação na Silver | `notebooks/02_engenharia_features.ipynb` | **CONFIRMADO** | Nenhuma |
| **Quadro 7** | P230 / Tab. Word 9 | Critérios de exclusão e filtragem na Gold | `notebooks/02_engenharia_features.ipynb` | **CONFIRMADO** | Nenhuma |
| **Quadro 8** | P255 / Tab. Word 10 | Definição das variáveis de entrada por grupo| `dados/gold/gold_dataset_ml_limpo.parquet` | **CONFIRMADO** | Nenhuma |
| **Quadro 9** | P275 / Tab. Word 11 | Hiperparâmetros e grade de sintonização | `notebooks/04_modelagem_cenarios.ipynb` | **CONFIRMADO** | Nenhuma |
| **Quadro 10**| P295 / Tab. Word 12 | Relação de algoritmos preditivos avaliados | `notebooks/04_modelagem_cenarios.ipynb` | **CONFIRMADO C/ AJUSTE** | Explicitar papel exploratório de SARIMAX/Prophet |
| **Quadro 11**| P325 / Tab. Word 13 | Formulação matemática do ensemble híbrido | `notebooks/05_margens_seguranca_e_hibrido.ipynb` | **CONFIRMADO** | Nenhuma |
| **Quadro 12**| P345 / Tab. Word 14 | Métricas de avaliação operacional e negócio | `src/metricas_avaliacao.py` | **CONFIRMADO** | Nenhuma |
| **Quadro 13**| P780 / Tab. Word 15 | Consolidação das políticas de margens e MAE | `reports/tabelas/comparativo_politicas_margens_seguranca.csv` | **DIVERGENTE (FORMATO)** | Deletar linha final duplicada |
| **Quadro 14**| P835 / Tab. Word 16 | Parâmetros da simulação estocástica | `reports/tabelas/previsoes_diarias_2026_monte_carlo.parquet` | **DIVERGENTE** | Restringir formalmente até 31/08/2026 ($N=73$) |
| **Quadro 15**| P920 / Tab. Word 17 | Estrutura de artefatos computacionais | Árvore de diretórios | **DIVERGENTE** | Atualizar para `reports/tabelas/` e `reports/figuras/` |
| **Quadro 16**| P205 / Tab. Word 18 | Especificação da API Open-Meteo | `src/extracao_open_meteo.py` | **DIVERGENTE** | Declarar formalmente o uso da Previous Runs API |

---

## 6. LISTA CONSOLIDADA DOS 6 ITENS IMPEDITIVOS PARA A SUBMISSÃO (BLOQUEADORES)

1. **[IMPEDITIVO 1 - CORTE TEMPORAL] Truncar a Simulação Estocástica em 31/08/2026 ($N=73$):**  
   A Figura 26 e o arquivo `previsoes_diarias_2026_monte_carlo.parquet` invadem setembro de 2026 em 10 datas (até 25/09/2026). A qualificação encerra formalmente em 31/08/2026 ($N=73$). Truncar a série temporal e ajustar os textos das seções 3.1.2 e 5.6.1.
2. **[IMPEDITIVO 2 - CONTRADIÇÃO TEXTO VS. IMAGEM] Figura 7 e Parágrafo P627 (Perfil Semanal):**  
   O texto cita médias legadas de 168, 172, 152 e 124. Substituir pelos valores exatos da imagem incorporada (140,0; 133,2; 143,0; 122,2; 131,3).
3. **[IMPEDITIVO 3 - RÓTULOS INVERTIDOS] Figura 17 (Balanço Anual de Reservas):**  
   A imagem inverteu a identificação de 2024 ($N=157$) e 2025 ($N=120$). O gabarito canônico da Tabela 3 é $2024 = 122$ e $2025 = 155$.
4. **[IMPEDITIVO 4 - DADOS PROTOTIPAIS] Figuras 18 e 22 (Modelagem e Políticas):**  
   A Figura 18 plota valores arbitrários de rascunho (25,80/29,50 etc.), e a Figura 22 plota 2.140 sobras e 295 faltas (conflitando com a Tabela 7). Devem ser geradas diretamente dos dados da Tabela 5 e da Tabela 7.
5. **[IMPEDITIVO 5 - RIGOR METODOLÓGICO] Terminologia das Margens de Segurança:**  
   Substituir *conformal prediction* por **"margens empíricas de segurança por quantis residuais"** nas Figuras 5, 6, 25, Quadro 13 e nos textos correspondentes.
6. **[IMPEDITIVO 6 - FORMATAÇÃO EDITORIAL] Eliminação de Linhas Duplicadas:**  
   Excluir a linha final da Tabela 2 que duplica cabeçalhos e a linha final do Quadro 13 que repete `Ridge sem margem`.
