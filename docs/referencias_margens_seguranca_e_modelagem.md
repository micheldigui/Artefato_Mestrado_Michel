# Referencial Teórico e Bibliográfico: Margens de Segurança, Perda Assimétrica e Modelos Híbridos em Alimentação Coletiva

**Projeto:** Artefato Analítico-Preditivo de Demanda de Refeições — IFSP Campus Itaquaquecetuba  
**Programa:** Mestrado Profissional em Gestão e Tecnologia em Sistemas Produtivos (PPG-GTSP)  
**Instituição Mantenedora:** Centro Estadual de Educação Tecnológica Paula Souza (CEETEPS)  
**Data de Consolidação:** Outubro de 2026  

---

## 1. Contexto e Motivação Operacional na Gestão Pública

Na gestão de serviços de alimentação coletiva institucional (especialmente no Programa Nacional de Alimentação Escolar - PNAE e na alimentação de institutos federais), a previsão de demanda lida com **perecibilidade imediata** e **fortes assimetrias de impacto**:

1. **Potencial de Sobra ($C_o$ — *Overage Cost*):** Gera descarte físico de alimentos prontos e desperdício financeiro de verba pública.
2. **Potencial de Falta ($C_u$ — *Underage Cost*):** Na escola pública, a falta de refeição transcende a dimensão contábil: compromete o rendimento cognitivo e pedagógico dos estudantes, eleva o risco de evasão escolar e atinge estudantes em situação de vulnerabilidade nutricional e socioeconômica.

Por essa razão, métricas simétricas tradicionais de Machine Learning (como MAE e RMSE), que penalizam desvios positivos e negativos com o mesmo peso, são insuficientes para a tomada de decisão final. É imperativo adotar mecanismos de **reserva prudencial (margem de segurança)** e **calibração colaborativa (modelos híbridos)**.

---

## 2. As Quatro Abordagens Científicas Adotadas no Artefato

### Abordagem 1: O Modelo do *Newsvendor* com Função de Perda Assimétrica

* **Princípio Teórico:** O problema de dimensionar refeições perecíveis sob demanda incerta diária/semanal é formulado na Pesquisa Operacional pelo **Modelo do Vendedor de Jornais (*Newsvendor Problem*)**.
* **Equação da Fração Crítica (*Critical Fractile / Service Level*):**
  $$SL^* = \frac{C_u}{C_u + C_o}$$
  Quando a falta é considerada substancialmente mais prejudicial do que a sobra ($C_u > C_o$), o nível de atendimento ótimo deve situar-se entre $75\%$ e $90\%$.
* **Margem Paramétrica Gaussiana:**
  $$Q^* = \hat{y}_{\text{modelo}} + z^* \cdot \sigma_e$$
  Onde $\sigma_e$ é o desvio padrão dos resíduos históricos (ou RMSE do modelo) e $z^* = \Phi^{-1}(SL^*)$ é o escore z da distribuição normal acumulada ($z=0{,}67$ para $75\%$; $z=1{,}28$ para $90\%$).

#### Referências Centrais:
* **Arrow, K. J., Karlin, S., & Scarf, H. (1958).** *Studies in the Mathematical Theory of Inventory and Production*. Stanford University Press. (Obra pioneira da teoria estocástica de estoques e Newsvendor).
* **Khouja, M. (1999).** The single-period (news-vendor) problem: literature review and suggestions for future research. *Omega - International Journal of Management Science*, 27(5), 537-553. https://doi.org/10.1016/S0305-0483(99)00017-1
* **Silver, E. A., Pyke, D. F., & Peterson, R. (1998).** *Inventory Management and Production Planning and Scheduling* (3rd ed.). John Wiley & Sons. (Referência canônica de cálculo de estoque e margem de segurança).
* **Petropoulos, F., et al. (2022).** Forecasting: theory and practice. *International Journal of Forecasting*, 38(3), 705-871. (Seção dedicada a previsão sob perdas assimétricas em cadeias de suprimentos).

---

### Abordagem 2: Predição Conformal Não-Paramétrica (*Conformal Prediction*)

* **Princípio Teórico:** Em séries reais de consumo escolar, os resíduos raramente seguem uma distribuição normal perfeita, apresentando assimetria e caudas pesadas decorrentes de clima e eventos atípicos. A **Predição Conformal** é o método de ponta em Machine Learning para quantificação de incerteza livre de hipóteses distributivas (*distribution-free*).
* **Garantia Matemática:** A técnica oferece garantia formal de cobertura para amostras finitas sob permutabilidade (*exchangeability*).
* **Cálculo da Margem Conformal:**
  Calcula-se o quantil $(1 - \alpha)$ da distribuição empírica dos resíduos de subestimação $e_i = (y_i - \hat{y}_i)$:
  $$Q^* = \hat{y}_{\text{modelo}} + \text{Quantil}_{1-\alpha}(y - \hat{y})$$
  Se for estipulado um nível de confiança de $85\%$ ou $90\%$, o algoritmo garante que o consumo real não superará a estimativa ajustada nessa exata proporção de dias letivos.

#### Referências Centrais:
* **Vovk, V., Gammerman, A., & Shafer, G. (2005).** *Algorithmic Learning in a Random World*. Springer. https://doi.org/10.1007/b106715 (A obra seminal fundadora da Predição Conformal).
* **Angelopoulos, A. N., & Bates, S. (2021).** A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification. *arXiv preprint arXiv:2107.07511*. (Revisão contemporânea adotada como padrão na ciência de dados).
* **Shafer, G., & Vovk, V. (2008).** A Tutorial on Conformal Prediction. *Journal of Machine Learning Research*, 9, 371-421.
* **Romano, Y., Patterson, E., & Candès, E. (2019).** Conformalized Quantile Regression. *Advances in Neural Information Processing Systems (NeurIPS 2019)*, 32.

---

### Abordagem 3: O Modelo Híbrido Colaborativo (*Collaborative Forecasting: IA + Especialista*)

* **Princípio Teórico:** Em vez de opor a Inteligência Artificial ao julgamento da nutricionista, a literatura de tomada de decisão apoia a integração harmoniosa de ambos. A intuição do especialista captura sutilezas qualitativas (rotina do campus, alterações no fornecimento), enquanto o modelo algorítmico elimina vieses cognitivos sistemáticos de superestimativa.
* **Formulação Matemática Ponderada:**
  $$\hat{y}_{\text{híbrido}} = \alpha \cdot \hat{y}_{\text{IA}} + (1 - \alpha) \cdot \text{Quantitativo}_{\text{Nutricionista}}, \quad \alpha \in [0{,}0; 1{,}0]$$
* **Fronteira Eficiente de Pareto:** Otimiza o hiperparâmetro $\alpha$ gerando uma curva convexa entre Potencial de Sobra e Potencial de Falta, identificando o ponto de equilíbrio de *mínimo arrependimento* (*Minimax Regret*).

#### Referências Centrais:
* **Blattberg, R. C., & Hoch, S. J. (1990).** Database Models and Managerial Intuition: 50% Model + 50% Manager. *Management Science*, 36(8), 887-899. https://doi.org/10.1287/mnsc.36.8.887 (O artigo seminal que demonstrou que a combinação linear 50/50 entre intuição humana e modelo estatístico supera ambos isoladamente).
* **Armstrong, J. S. (2001).** Combining Forecasts. In *Principles of Forecasting: A Handbook for Researchers and Practitioners* (pp. 417-439). Springer.
* **Fildes, R., Goodwin, P., Lawrence, M., & Nikolopoulos, K. (2009).** Effective demand forecasting in supply chains: Extending the role of judgment. *International Journal of Forecasting*, 25(1), 3-23.
* **De-Arteaga, M., Fogliato, R., & Chouldechova, A. (2020).** A case for humans-in-the-loop: Decisions in the presence of algorithmic recommendations. *Human-Centered AI Workshop at NeurIPS*.

---

### Abordagem 4: Simulação de Monte Carlo e Bootstrap Residual para Análise de Risco

* **Princípio Teórico:** A simulação estocástica de Monte Carlo permite estressar a operação do restaurante universitário simulando milhares ($N = 1.000$ a $5.000$) de semanas possíveis através da amostragem das distribuições de erro residual e variáveis meteorológicas.
* **Aplicação Operacional:** Gera intervalos de predição empíricos (cenário moderado $P50$, cenário prudencial $P80$ e pior caso $P95$) que podem ser apresentados em painéis executivos à direção do campus e à nutricionista para planejamento financeiro e compras semanais.

#### Referências Centrais:
* **Metropolis, N., & Ulam, S. (1949).** The Monte Carlo Method. *Journal of the American Statistical Association*, 44(247), 335-341.
* **Efron, B., & Tibshirani, R. J. (1993).** *An Introduction to the Bootstrap*. Chapman and Hall/CRC. (Referência metodológica para reamostragem residual empírica em séries temporais).
* **Law, A. M. (2015).** *Simulation Modeling and Analysis* (5th ed.). McGraw-Hill Education.

---

### Abordagem 5: Aplicação Específica em Alimentação Escolar e Coletiva

* **Princípio Teórico:** A literatura voltada para restaurantes corporativos, escolares e hospitalares demonstra que sistemas automatizados com margens probabilísticas reduzem em média de $30\%$ a $60\%$ o desperdício de alimentos perecíveis mantendo índices de disponibilidade superiores a $98\%$.

#### Referências Centrais:
* **Derqui, B., Fayos, T., & Fernandez, V. (2016).** Towards a more sustainable food supply chain: opening up invisible waste in food service. *Sustainability*, 8(7), 693. (Estudo sobre desperdício oculto e superdimensionamento em cozinhas institucionais).
* **Falcone, P. M., et al. (2023).** Food waste reduction in public school catering: Challenges and opportunities for sustainable management. *Journal of Cleaner Production*, 385, 135702.
* **Eriksson, M., et al. (2018).** Food waste in school catering: An analysis of factors affecting food waste and its environmental impact. *Resources, Conservation and Recycling*, 137, 107-115.

---

### Conclusão e Enquadramento na Dissertação

Essas referências conferem respaldo científico e metodológico à tese de que:
1. O produto técnico não visa unicamente "prever números", mas sim **mitigar o risco de vulnerabilidade nutricional** através de um colchão de segurança estatisticamente calibrado.
2. O sistema funciona como um **Sistema de Apoio à Decisão (DSS)** que atua em simbiose com o conhecimento tácito da nutricionista responsável técnica.
