# Catálogo de Referências Bibliográficas e Metodológicas (Normas ABNT)

**Projeto:** Artefato Técnico de Apoio à Decisão Operacional para Previsão de Demanda de Refeições  
**Instituição:** Instituto Federal de São Paulo (IFSP) — Campus Itaquaquecetuba  
**Programa:** Mestrado Profissional em Educação Profissional e Tecnológica (ProfEPT / Linha de Gestão Pública)  
**Localização no Projeto:** Pasta `docs/`  
**Última Atualização:** Outubro de 2026  

---

## Apresentação do Documento

Este catálogo reúne a fundamentação teórico-metodológica que sustenta as escolhas algorítmicas, os parâmetros estatísticos e as diretrizes operacionais implementadas no artefato técnico. 

Para cada trabalho selecionado, apresentam-se:
1. **A referência normalizada em padrão ABNT (NBR 6023:2018)**;
2. **O link oficial ou identificador digital (DOI / URL)**;
3. **A síntese do conceito teórico**;
4. **A transposição direta para o artefato do IFSP** (qual fórmula, notebook ou figura utiliza o conceito);
5. **Sugestão de redação/citação direta para a dissertação**.

---

## Sumário dos Eixos Temáticos

1. [Eixo 1 — Dimensionamento de Itens Perecíveis e Perda Assimétrica (Modelo Newsvendor)](#eixo-1--dimensionamento-de-itens-perecíveis-e-perda-assimétrica-modelo-newsvendor)
2. [Eixo 2 — Quantificação de Incerteza Não-Paramétrica (Predição Conformal)](#eixo-2--quantificação-de-incerteza-não-paramétrica-predição-conformal)
3. [Eixo 3 — Previsão Colaborativa e Modelos Híbridos (Especialista + Inteligência Artificial)](#eixo-3--previsão-colaborativa-e-modelos-híbridos-especialista--inteligência-artificial)
4. [Eixo 4 — Simulação Estocástica de Risco Operacional (Método de Monte Carlo e Bootstrap)](#eixo-4--simulação-estocástica-de-risco-operacional-método-de-monte-carlo-e-bootstrap)
5. [Eixo 5 — Alimentação Coletiva Escolar, Gestão Pública e Desperdício Sustentável](#eixo-5--alimentação-coletiva-escolar-gestão-pública-e-desperdício-sustentável)
6. [Eixo 6 — Aprendizado de Máquina em Séries Temporais e Prevenção de Data Leakage](#eixo-6--aprendizado-de-máquina-em-séries-temporais-e-prevenção-de-data-leakage)

---

## Eixo 1 — Dimensionamento de Itens Perecíveis e Perda Assimétrica (Modelo Newsvendor)

### 1.1. Artigo Canônico de Revisão do Problema do Vendedor de Jornais
* **Referência ABNT:**  
  KHOUJA, Moutaz. The single-period (news-vendor) problem: literature review and suggestions for future research. **Omega — International Journal of Management Science**, v. 27, n. 5, p. 537–553, 1999.
* **DOI/Link:**  
  [https://doi.org/10.1016/S0305-0483(99)00017-1](https://doi.org/10.1016/S0305-0483(99)00017-1)
* **Conceito Teórico:**  
  Estrutura clássica de Pesquisa Operacional para produtos de ciclo de vida de período único (perecíveis diários). Demonstra que, quando a penalidade da falta ($C_u$) supera o custo de estocagem/descarte de sobras ($C_o$), a quantidade ótima a produzir não é a média da demanda, mas sim o fractil crítico dado por:
  $$SL^* = \frac{C_u}{C_u + C_o}$$
* **Aplicação no Artefato:**  
  Fundamenta o cálculo de margens de segurança prudenciais nos Notebooks `05`, `06` e `08`. Explica por que um modelo puramente simétrico (focado apenas em minimizar MAE) gera faltas crônicas inaceitáveis na alimentação pública escolar.
* **Texto para a Dissertação:**  
  > "Conforme sintetizado por Khouja (1999), em contextos de perecibilidade imediata nos quais o custo de falta excede o de sobra, a quantidade ótima de produção afasta-se da média prevista e aproxima-se de uma fração crítica superior da distribuição de probabilidade da demanda."

---

### 1.2. Teoria Clássica de Estoques Estocásticos
* **Referência ABNT:**  
  ARROW, Kenneth J.; KARLIN, Samuel; SCARF, Herbert. **Studies in the Mathematical Theory of Inventory and Production**. Stanford: Stanford University Press, 1958.
* **Link:**  
  [Stanford University Press Record](https://www.sup.org/books/title/?id=4027)
* **Conceito Teórico:**  
  Marco fundacional que formalizou matematicamente a decisão ótima de inventário sob incerteza estocástica de demanda.
* **Aplicação no Artefato:**  
  Gênese do conceito de colchão de segurança de produção adicionado à estimativa pontual média.

---

### 1.3. Gestão e Planejamento de Produção e Estoques
* **Referência ABNT:**  
  SILVER, Edward A.; PYKE, David F.; PETERSON, Rein. **Inventory Management and Production Planning and Scheduling**. 3. ed. Nova York: John Wiley & Sons, 1998.
* **Conceito Teórico:**  
  Tratado clássico que formaliza o cálculo do *Safety Stock* (estoque de segurança) em função do desvio padrão do erro de previsão ($\sigma_e$) e do fator $z$ correspondente ao nível de serviço desejado:
  $$SS = z \cdot \sigma_e$$
* **Aplicação no Artefato:**  
  Utilizado no Notebook `08` e na [Figura 54](file:///f:/PROJETOS/ARTEFATO/reports/figuras/06_margens_seguranca_e_modelo_hibrido/fig54_impacto_margens_seguranca_conformal.png) para confrontar a margem gaussiana teórica com a margem conformal empírica.

---

## Eixo 2 — Quantificação de Incerteza Não-Paramétrica (Predição Conformal)

### 2.1. Obra Seminal de Predição Conformal
* **Referência ABNT:**  
  VOVK, Vladimir; GAMMERMAN, Alex; SHAFER, Glenn. **Algorithmic Learning in a Random World**. Nova York: Springer, 2005.
* **DOI/Link:**  
  [https://doi.org/10.1007/b106715](https://doi.org/10.1007/b106715)
* **Conceito Teórico:**  
  Introduz a teoria matemática da Predição Conformal (*Conformal Prediction*), permitindo transformar qualquer predição pontual de aprendizado de máquina em intervalos válidos com garantias finitas e não-paramétricas (sem pressupor distribuição normal).
* **Aplicação no Artefato:**  
  Garante que a margem conformal adotada para $85\%$ ou $90\%$ de nível de cobertura proteja o quantitativo de refeições contra caudas pesadas ou assimetrias da demanda real dos alunos do campus.

---

### 2.2. Guia Didático Contemporâneo de Predição Conformal
* **Referência ABNT:**  
  ANGELOPOULOS, Anastasios N.; BATES, Stephen. A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification. **arXiv preprint arXiv:2107.07511**, 2021.
* **DOI/Link:**  
  [https://arxiv.org/abs/2107.07511](https://arxiv.org/abs/2107.07511)
* **Conceito Teórico:**  
  Manual de referência moderno para cientistas de dados sobre calibração empírica de quantis e intervalos de predição *distribution-free*.
* **Aplicação no Artefato:**  
  Implementação das margens $P80$, $P85$ e $P90$ no Notebook `08` a partir da série residual de subestimação $e_i = (y_i - \hat{y}_i)$.

---

### 2.3. Regressão Quantílica Conformalizada
* **Referência ABNT:**  
  ROMANO, Yaniv; PATTERSON, Evan; CANDÈS, Emmanuel. Conformalized Quantile Regression. In: **Advances in Neural Information Processing Systems (NeurIPS 2019)**, v. 32, p. 3543–3553, 2019.
* **DOI/Link:**  
  [https://proceedings.neurips.cc/paper/2019/hash/5103c3584b063c431bce4e6b1f00390d-Abstract.html](https://proceedings.neurips.cc/paper/2019/hash/5103c3584b063c431bce4e6b1f00390d-Abstract.html)
* **Conceito Teórico:**  
  Mostra como adaptar quantis de aprendizado supervisionado para manter a calibração marginal exata mesmo sob heterocedasticidade temporal.

---

## Eixo 3 — Previsão Colaborativa e Modelos Híbridos (Especialista + Inteligência Artificial)

### 3.1. O Artigo Pioneiro "50% Modelo + 50% Gestor"
* **Referência ABNT:**  
  BLATTBERG, Robert C.; HOCH, Stephen J. Database Models and Managerial Intuition: 50% Model + 50% Manager. **Management Science**, v. 36, n. 8, p. 887–899, 1990.
* **DOI/Link:**  
  [https://doi.org/10.1287/mnsc.36.8.887](https://doi.org/10.1287/mnsc.36.8.887)
* **Conceito Teórico:**  
  Demonstração empírica de que combinar 50% da predição estatística com 50% da estimativa intuitiva do gestor profissional supera tanto o modelo isolado quanto o gestor isolado. O modelo corrige a variabilidade errática e os vieses de superdimensionamento humano, enquanto o especialista introduz conhecimento de contexto não codificado em tabelas.
* **Aplicação no Artefato:**  
  Base teórica direta para a formulação do modelo híbrido no Notebook `08`:
  $$\hat{y}_{\text{híbrido}} = \alpha \cdot \hat{y}_{\text{IA}} + (1 - \alpha) \cdot \text{Quantitativo}_{\text{Nutricionista}}$$
  Confirmado empiricamente na [Figura 53 (Fronteira de Pareto)](file:///f:/PROJETOS/ARTEFATO/reports/figuras/06_margens_seguranca_e_modelo_hibrido/fig53_fronteira_pareto_modelo_hibrido.png), onde $\alpha = 0{,}50$ atingiu a menor taxa de faltas e reduziu simultaneamente as sobras.
* **Texto para a Dissertação:**  
  > "A decisão de não substituir a nutricionista pelo algoritmo apoia-se no clássico experimento de Blattberg e Hoch (1990), que comprovou que o acoplamento linear equilibrado entre a modelagem de dados e a sensibilidade do tomador de decisão mitiga as fragilidades intrínsecas de ambos os polos."

---

### 3.2. Manual de Princípios de Previsão e Combinação de Modelos
* **Referência ABNT:**  
  ARMSTRONG, J. Scott. Combining Forecasts. In: ARMSTRONG, J. Scott (org.). **Principles of Forecasting: A Handbook for Researchers and Practitioners**. Boston: Springer, 2001. p. 417–439.
* **DOI/Link:**  
  [https://doi.org/10.1007/978-0-306-47630-3_19](https://doi.org/10.1007/978-0-306-47630-3_19)
* **Conceito Teórico:**  
  Estabelece diretrizes formais para combinação de previsões independentes, destacando ganhos de robustez e redução de variância de erro.

---

### 3.3. Papel do Julgamento Humano em Cadeias de Suprimentos
* **Referência ABNT:**  
  FILDES, Robert; GOODWIN, Paul; LAWRENCE, Michael; NIKOLOPOULOS, Konstantinos. Effective demand forecasting in supply chains: Extending the role of judgment. **International Journal of Forecasting**, v. 25, n. 1, p. 3–23, 2009.
* **DOI/Link:**  
  [https://doi.org/10.1016/j.ijforecast.2008.11.010](https://doi.org/10.1016/j.ijforecast.2008.11.010)
* **Conceito Teórico:**  
  Investiga quando e como ajustes manuais em previsões geradas por computador agregam valor real, recomendando que o modelo sirva como âncora estruturada e não como caixa-preta impositiva.

---

### 3.4. Inteligência Artificial Centrada no Humano (Human-in-the-Loop)
* **Referência ABNT:**  
  DE-ARTEAGA, Maria; FOGLIATO, Riccardo; CHOULDECHOVA, Alexandra. A case for humans-in-the-loop: Decisions in the presence of algorithmic recommendations. In: **NeurIPS Workshop on Human-Centered AI**, 2020.
* **Conceito Teórico:**  
  Reforça a necessidade de sistemas de apoio à decisão (DSS) na gestão pública que preservem a agência moral e operacional do servidor público responsável, fornecendo transparência e margens de incerteza em vez de imposições estáticas.

---

## Eixo 4 — Simulação Estocástica de Risco Operacional (Método de Monte Carlo e Bootstrap)

### 4.1. Fundamentação da Simulação de Monte Carlo
* **Referência ABNT:**  
  METROPOLIS, Nicholas; ULAM, Stanislaw. The Monte Carlo Method. **Journal of the American Statistical Association**, v. 44, n. 247, p. 335–341, 1949.
* **DOI/Link:**  
  [https://doi.org/10.1080/01621459.1949.10483310](https://doi.org/10.1080/01621459.1949.10483310)
* **Conceito Teórico:**  
  Metodologia baseada em amostragens pseudoaleatórias sucessivas para modelar o comportamento de sistemas complexos sob incerteza combinada.
* **Aplicação no Artefato:**  
  Utilizado para gerar as 1.000 trajetórias de consumo simuladas no Notebook `08` e na [Figura 55 (Faixas de Risco Monte Carlo)](file:///f:/PROJETOS/ARTEFATO/reports/figuras/06_margens_seguranca_e_modelo_hibrido/fig55_simulacao_monte_carlo_faixas_risco.png).

---

### 4.2. Teoria do Bootstrap e Reamostragem Residual
* **Referência ABNT:**  
  EFRON, Bradley; TIBSHIRANI, Robert J. **An Introduction to the Bootstrap**. Nova York: Chapman & Hall/CRC, 1993.
* **DOI/Link:**  
  [https://doi.org/10.1201/9780429246593](https://doi.org/10.1201/9780429246593)
* **Conceito Teórico:**  
  Reamostragem dos resíduos históricos para gerar cenários futuros sintéticos sem impor normalidade aos erros de predição.

---

## Eixo 5 — Alimentação Coletiva Escolar, Gestão Pública e Desperdício Sustentável

### 5.1. Desperdício Oculto em Serviços de Alimentação Coletiva
* **Referência ABNT:**  
  DERQUI, Belen; FAYOS, Teresa; FERNANDEZ, Vicenc. Towards a more sustainable food supply chain: opening up invisible waste in food service. **Sustainability**, v. 8, n. 7, p. 693, 2016.
* **DOI/Link:**  
  [https://doi.org/10.3390/su8070693](https://doi.org/10.3390/su8070693)
* **Conceito Teórico:**  
  Identifica que a maior fonte de sobras e desperdício em cozinhas institucionais provém da incerteza do número de comensais presentes e do superdimensionamento preventivo adotado por cozinheiros e nutricionistas para evitar que faltem refeições.

---

### 5.2. Redução de Desperdício na Alimentação Escolar Pública
* **Referência ABNT:**  
  FALCONE, Pasquale Marcello; CESARO, Alessandra; CASALINO, Nunzio. Food waste reduction in public school catering: Challenges and opportunities for sustainable management. **Journal of Cleaner Production**, v. 385, art. 135702, 2023.
* **DOI/Link:**  
  [https://doi.org/10.1016/j.jclepro.2022.135702](https://doi.org/10.1016/j.jclepro.2022.135702)
* **Conceito Teórico:**  
  Examina o equilíbrio entre exigências nutricionais obrigatórias em escolas públicas e políticas ativas de combate ao desperdício de recursos orçamentários, apontando ferramentas digitais preditivas como solução central.

---

### 5.3. Fatores de Variação de Demanda na Merenda Escolar
* **Referência ABNT:**  
  ERIKSSON, Mattias; OSOWSKI, Christine Persson; MALEFELT, Mikaela; MALBERT, Kerstin. Food waste in school catering: An analysis of factors affecting food waste and its environmental impact. **Resources, Conservation and Recycling**, v. 137, p. 107–115, 2018.
* **DOI/Link:**  
  [https://doi.org/10.1016/j.resconrec.2018.05.028](https://doi.org/10.1016/j.resconrec.2018.05.028)
* **Conceito Teórico:**  
  Analisa como fatores de calendário escolar (dias da semana, vésperas de feriados, sazonalidade e cardápio) influenciam a adesão dos estudantes, fundamentando a engenharia de atributos temporais.

---

## Eixo 6 — Aprendizado de Máquina em Séries Temporais e Prevenção de Data Leakage

### 6.1. Validação Temporal Rigorosa (Walk-Forward / TimeSeriesSplit)
* **Referência ABNT:**  
  HYNDMAN, Rob J.; ATHANASOPOULOS, George. **Forecasting: Principles and Practice**. 3. ed. Melbourne: OTexts, 2021.
* **Link Online:**  
  [https://otexts.com/fpp3/](https://otexts.com/fpp3/)
* **Conceito Teórico:**  
  Manual internacional de referência em séries temporais. Estabelece a obrigatoriedade da validação em janelas deslizantes (*Rolling Window / Walk-Forward Cross-Validation*) para impedir que informações futuras vazem para o conjunto de treinamento.
* **Aplicação no Artefato:**  
  Implementada a divisão estritamente sequencial nos Notebooks `05`, `06`, `07` e `08` (28 semanas de corte temporal sem embaralhamento aleatório).

---

### 6.2. Arquitetura de Pipelines e Prevenção de Vazamento no Scikit-Learn
* **Referência ABNT:**  
  PEDREGOSA, Fabian et al. Scikit-learn: Machine Learning in Python. **Journal of Machine Learning Research**, v. 12, p. 2825–2830, 2011.
* **Link:**  
  [https://jmlr.org/papers/v12/pedregosa11a.html](https://jmlr.org/papers/v12/pedregosa11a.html)
* **Aplicação no Artefato:**  
  Uso de `Pipeline(steps=[('scaler', StandardScaler()), ('model', ...)])` garantindo que médias e desvios sejam ajustados exclusivamente no fold de treino.

---

## Guia Rápido de Rastreabilidade no Projeto

| Conceito Operacional | Abordagem Científica | Referência Principal | Localização no Código / Figuras |
| :--- | :--- | :--- | :--- |
| **Margem Assimétrica P85 / P90** | Predição Conformal Não-Paramétrica | Vovk et al. (2005); Angelopoulos & Bates (2021) | `notebooks/08_margem_seguranca_e_modelo_hibrido.ipynb` \| [Fig 54](file:///f:/PROJETOS/ARTEFATO/reports/figuras/06_margens_seguranca_e_modelo_hibrido/fig54_impacto_margens_seguranca_conformal.png) |
| **Ponderação $\alpha=0{,}50$ (IA + Nutricionista)** | Previsão Colaborativa Híbrida | Blattberg & Hoch (1990); Fildes et al. (2009) | `notebooks/08_margem_seguranca_e_modelo_hibrido.ipynb` \| [Fig 53](file:///f:/PROJETOS/ARTEFATO/reports/figuras/06_margens_seguranca_e_modelo_hibrido/fig53_fronteira_pareto_modelo_hibrido.png) |
| **Faixas de Risco P10, P50, P80, P95** | Simulação de Monte Carlo & Bootstrap | Metropolis & Ulam (1949); Efron & Tibshirani (1993) | `notebooks/08_margem_seguranca_e_modelo_hibrido.ipynb` \| [Fig 55](file:///f:/PROJETOS/ARTEFATO/reports/figuras/06_margens_seguranca_e_modelo_hibrido/fig55_simulacao_monte_carlo_faixas_risco.png) |
| **Matriz Custo vs. Proteção** | Fractil Crítico / Newsvendor | Khouja (1999); Arrow et al. (1958) | `notebooks/08_margem_seguranca_e_modelo_hibrido.ipynb` \| [Fig 56](file:///f:/PROJETOS/ARTEFATO/reports/figuras/06_margens_seguranca_e_modelo_hibrido/fig56_matriz_politicas_decisao_gestao.png) |
| **Horizonte $t+2$ (Secos) e $t+1$ (Perecíveis)** | Validação Walk-Forward e Lead Times | Hyndman & Athanasopoulos (2021); Silver et al. (1998) | `notebooks/05_modelagem_cenarios_e_algoritmos.ipynb` \| `notebooks/06_avaliacao_visual_e_comparativo_modelos.ipynb` |
