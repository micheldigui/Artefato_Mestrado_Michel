# Resumo do Item de Conteúdo: Forecasting and Modelling of Food Demand Supply Chain using Machine Learning

## Referência
CHAUDHARI, M. A. et al. Forecasting and Modelling of Food Demand Supply Chain using Machine Learning. **International Journal of Innovative Research in Multidisciplinary Physical Sciences (IJIRMPS)**, v. 13, n. 2, Mar-Apr 2025. ISSN: 2349-7300.
**Local:** `docs/artigos/Artigos Dissertação/Forecasting and Modelling of Food Demand Supply Chain using Machine Learning.pdf`

## Resumo
O artigo propõe uma solução de software baseada em Machine Learning para prever a demanda de alimentos em ambientes dinâmicos, visando a otimização de estoques e a redução de desperdícios. Através de uma abordagem comparativa, os autores testam modelos de boosting (XGBoost, LightGBM e Gradient Boosting) e o modelo estatístico SARIMA sobre um dataset de 145 semanas de pedidos. O LightGBM apresentou a melhor performance preditiva, superando o XGBoost em termos de MAE e RMSE.

## Tópicos Principais
1. **Motivação e Problema:** O foco central é a redução de "food waste" e custos de inventário em serviços de entrega e restaurantes. A predição precisa é vista como essencial para o planejamento estratégico e operacional (compras e pessoal).
2. **Abordagem Metodológica:**
   - **Engenharia de Features:** Exploração inovadora de *lag features* e Médias Móveis Ponderadas Exponencialmente (EWMA).
   - **Modelagem:** Comparação entre modelos de base árvore (XGBoost, LightGBM) que lidam bem com dados categóricos e numéricos, e o modelo estatístico SARIMA para séries temporais.
   - **Data Cleaning:** O trabalho destaca a importância da padronização e do tratamento de skewness (assimetria) dos dados de pedidos.
3. **Arquitetura da Solução:** O sistema é estruturado como uma aplicação web com módulos de dashboard de predição e gestão de inventário.
4. **Principais Resultados:**
   - O LightGBM demonstrou ser o modelo mais robusto para a base testada (RMSE 158.48 vs 172.37 do XGBoost).
   - Identificou-se que a falta de dados exógenos (como feriados e eventos especiais) limita a captura de picos repentinos na série temporal.

## Conclusão Final
O artigo reforça a superioridade de modelos baseados em gradiente (LightGBM) para problemas complexos de demanda alimentar com muitas variáveis. Para o projeto de mestrado em questão (RU), o artigo valida a relevância do uso de algoritmos de Machine Learning frente aos estatísticos puros, mas alerta que a inclusão de fatores externos (calendário e clima, como está sendo feito nos notebooks 01d e 01e) é o próximo passo crítico para melhorar a precisão em picos e anomalias.
