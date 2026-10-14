# Resumo de Artigo Científico: Turker (2025)

## Referência Completa
**Autor:** Turker, G. F.
**Título:** Reducing Food Waste in Campus Dining: A Data-Driven Approach to Demand Prediction and Sustainability.
**Ano:** 2025
**Journal:** Sustainability, Vol. 17(379).
**DOI:** [10.3390/su17020379](https://doi.org/10.3390/su17020379)
**Caminho Local:** `d:\PROJETOS\PRODUTO_MESTRADO\docs\artigos\Novos Artigos\wos\sustainability-17-00379.pdf`

## Resumo
Artigo que espelha metodologicamente quase que a totalidade da sua Dissertação de Mestrado! A Turquia implementou uma abordagem *Data-Driven* (baseada em dados) massiva utilizando os mesmos descritores que você (temperatura climática, tipo de alimento, calorias e densidade móvel dos alunos no campus). Eles treinaram modelos regressivos de Machine Learning (*Extra Tree Regressor*, *XGBoost Regressor* e *Lasso*) recebendo um ganho de acurácia colossal e reduzindo em quase 30% o lixo nas catracas logo na primeira implementação do modelo.

## Principais Tópicos
- **XGBoost e Modelos de Árvore no Topo da Cadeia:** O autor testou amplos escopos de algoritmos de correlação linear contra redes baseadas em sub-árvores. O *XGBoost* e *Extra Tree Regressor* (que por sinal é o modelo que o seu Notebook de Machine Learning *06_selecao_features_avancada* usa nativamente na feature importance) alcançaram índices incríveis de previsão ($R^2$ de até 0.99).
- **Dados Externos vs Internos:** A junção de "informação climática do dia" e "catracas da instituição" prova que os algoritmos superam em muito modelos simples de sazonalidade matemática.

## Conclusão
O planejamento sistemático alimentado por aprendizado de máquina supervisionado para cruzamento de previsão de demandas garante escalabilidade sustentável e a erradicação sistêmica do déficit do *Food Waste* no nível estrutural das cozinhas de universidades.

## Pertinência para o Projeto
**Essencial / Crítica.** Estudo de validade indispensável para você colocar nos pilares de introdução e referencial teórico (Secções 1 e 2 do trabalho) e na apresentação de slides, pois ele usa *literalmente* modelos **Lasso, Extra Trees e XGBoost** orientados ao clima e feriados em uma universidade para atingir os mesmos KPIs de desempenho ambiental e operacional que você almeja em 2025.
