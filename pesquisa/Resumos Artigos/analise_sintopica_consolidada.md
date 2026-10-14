# Análise Sintópica Consolidada (Lotes 01 a 07)
**Data:** 20 de Abril de 2026 — **Atualizado:** 20 de Abril de 2026 (Lote 07)
**Objetivo:** Sintetizar o conhecimento de toda a literatura processada (artigos científicos + documentação técnica interna) para fundamentar o projeto de Dissertação (DSR) de predição de demanda em refeitórios universitários.

---

## 1. Convergências Teóricas
- **Importância do Cardápio:** Múltiplos estudos (Chaudhari, 2025; Turker, 2025) confirmam que a composição do menu é um dos preditores mais fortes. Turker (2025) demonstra que pratos específicos (ex: sopas, preparos principais) têm impactos distintos na demanda.
- **Variáveis Exógenas:** A inclusão de dados climáticos e de calendário é unânime para séries temporais de alta variabilidade.
- **Modelagem Avançada:** O uso de algoritmos de *Boosting* (LightGBM, XGBoost) e Regressão Regularizada (Lasso) apresenta os melhores resultados de acurácia (R² > 0.9).
- **Validação Interna ↔ Literatura:** A documentação técnica do projeto (Lote 07) confirma **convergência total** com a literatura: as escolhas de `day_of_week`, `event_type`, `lag_1d–lag_7d` e `main_dish` como preditores são explicitamente recomendadas pelos artigos revisados.

## 2. Inovações Identificadas (Gap de Pesquisa)
- **Mobilidade no Campus:** Turker (2025) introduziu o uso de fluxo de entrada nos portões do campus como variável preditiva, com sucesso extraordinário (R² = 0.999). Isso valida o uso da variável "reservas" e "calendário letivo" no projeto atual.
- **Explicabilidade (XAI):** Ipkovich (2024) enfatiza o uso de SHAP para modelos de sustentabilidade. Isso pode ser um diferencial no projeto: não apenas prever, mas explicar as oscilações de demanda aos gestores do RU.
- **Simulação de Monte Carlo:** Kodors (2022) sugere que, na ausência de Big Data histórico, simulações estatísticas podem prover insights valiosos sobre o desperdício de prato.
- **Arquitetura Desacoplada (Produto Tecnológico):** A documentação interna (Doc. 04 do Lote 07) registra formalmente a arquitetura Flask + ML adotada, configurando o sistema como **produto tecnológico** da Dissertação — componente exigido em Programas de Mestrado Profissional.

## 3. Implicações para o Projeto (RU IF)
- **Feature Engineering:** O uso de BERTimbau (Notebook 05) para cardápios está alinhado com a tendência de capturar o contexto semântico das refeições (Turker, 2025).
- **Rigor Técnico:** O projeto já contempla seleção de variáveis (Notebook 06) e uso de algoritmos de ponta, atendendo aos requisitos de uma dissertação de alto nível.
- **Impacto Social:** A bibliografia reforça que cada 1% de aumento na acurácia pode representar toneladas de alimentos salvos anualmente.
- **Estratégia de Algoritmos Confirmada:** Documentação interna (Doc. 06) recomenda Tier 1 = XGBoost/LightGBM/RF → Tier 2 = SARIMA/Prophet → Tier 3 = LSTM, exatamente o pipeline implementado nos Notebooks 07a–07i.

## 4. Lote 07 — Achados da Documentação Técnica Interna
> **Natureza:** 13 documentos técnicos internos produzidos pelo pesquisador entre 2023–2025. Registram o histórico de desenvolvimento do pipeline e as decisões metodológicas tomadas antes da execução dos experimentos.

| Grupo | Documentos | Valor para a Dissertação |
|-------|-----------|--------------------------|
| **A — Dataset** | Docs. 01–03 | Capítulo Metodologia: dicionário de dados, regras v1/v2 do `dref_adaptado` |
| **B — Arquitetura** | Docs. 04, 11, 12 | Capítulo Metodologia: produto tecnológico Flask + ML |
| **C — Bibliográfico** | Docs. 08, 09, Síntese | Capítulo Método: triagem e seleção de artigos (Scopus/WoS) |
| **D — Recomendações** | Docs. 05–07, 10 | Capítulo Referencial Teórico: valida escolhas de variáveis e algoritmos |

**Conclusão do Lote 07:** Alta pertinência como registro interno; não geram referências ABNT individuais, mas são fontes primárias para os Capítulos de Metodologia e Método de Pesquisa da Dissertação.

---

## 5. Referências Sintetizadas (Literatura Científica)
1. **Turker (2025):** Reducing Food Waste in Campus Dining (Lasso R² 0.999).
2. **Chaudhari (2025):** Forecasting demand with LightGBM.
3. **Ipkovich (2024):** XAI and Sustainability (SHAP values).
4. **Kodors (2022):** Monte Carlo for Plate Waste.
5. **Elnakib (2021):** Training and Smarter Lunchrooms interventions.
6. **Onyeaka (2025):** AI in Food Systems.
7. **Clark (2025):** AI in Hospitality and Waste Management.
8. **Olawale (2025):** ML for Sustainable Farming.
9. **Rajendran (2025):** Consumer intention and Random Forest.
10. **Rodrigues (2024):** ML em refeitórios escolares (Essencial — Random Forest + XGBoost).
11. **Kim (2023):** NLP + Word2Vec para previsão de frequentadores em refeitório.
12. **Wicaksono (2025):** ML + Circular Economy — Random Forest em RU universitário.
13. **Souza & Orsi (2024):** Relato técnico SIMPROFI — Regressão Linear como baseline.
14. **Souza (2025 SIMPROF):** EDA + Previsão de Demanda — dados reais IFSP-ITQ.
