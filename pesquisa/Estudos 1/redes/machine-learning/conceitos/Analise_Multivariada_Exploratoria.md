---
title: "Análise Multivariada Exploratória"
type: "conceito"
network: "machine-learning"
area: "EDA multivariada"
status: "rascunho"
source_ids:
  - "CASTRO-2026"
  - "OLULEYE-2023"
  - "AYD-HARRISON-2024"
tags:
  - conceito
  - eda
  - analise-multivariada
---

# Análise Multivariada Exploratória

## Definição

Análise multivariada explora padrões conjuntos em três ou mais variáveis: redundância, grupos, covariação, dimensão latente, interação e estrutura condicional. Ela estende gráficos de pares com métodos de projeção, fatoração e agrupamento; não substitui definir a unidade, o alvo ou as dependências.

## Técnicas e perguntas

- Matriz de dispersão/pairplot: que pares mostram forma, grupos ou extremos? Limite o número de variáveis ou use amostragem.
- Heatmap/correlograma: há pares com associação ou redundância? Informe qual correlação e como foi calculada.
- PCA: que combinações lineares resumem variação numérica? Examine variância explicada, cargas e escala antes de interpretar componentes.
- Análise fatorial: há fatores latentes que podem explicar covariação? Defina hipótese, adequação e número de fatores; a técnica não prova construtos.
- Clustering e profiling: que grupos aparecem em features selecionadas? Descreva perfil e estabilidade, além de uma visualização da projeção.
- Análise por grupos/estratos: uma associação agregada se mantém dentro de segmentos relevantes?

## Fluxo

Revise tipos e escalas, trate nulos dentro do protocolo, escolha variáveis com justificativa, examine redundância e só então aplique PCA/fatores/agrupamento. Compare resultados com dados originais e conhecimento do domínio. Para modelos preditivos, ajuste transformação e redução de dimensão somente no treino de cada fold.

## Limitações

Pairplots crescem quadraticamente com número de variáveis; correlação não representa dependência geral; PCA prioriza variância e pode descartar sinal preditivo; fatoração depende de hipóteses; projeções não preservam toda distância e podem criar separações visuais. Agrupamentos são sensíveis à escala, medida, variáveis e parâmetros.

## Relações

- [[redes/machine-learning/conceitos/Analise_Bivariada_e_Tabelas_de_Contingencia|Análise Bivariada e Tabelas de Contingência]]
- [[redes/machine-learning/conceitos/Visualizacao_Exploratoria_e_Codificacao_Visual|Visualização Exploratória e Codificação Visual]]
- [[redes/machine-learning/conceitos/PCA__Principal_Component_Analysis_|PCA]]
- [[redes/machine-learning/conceitos/K-Means_Clustering|K-Means]]
- [[redes/machine-learning/conceitos/Clustering_Hierárquico|Clustering Hierárquico]]
- [[redes/machine-learning/conceitos/Normalização_e_Padronização|Normalização e Padronização]]
- [[redes/machine-learning/conceitos/Selecao_de_Modelos_Orientada_pelo_EDA|Seleção de Modelos Orientada pelo EDA]]

## Evidência nas fontes

Castro (2026), capítulos 5–6, inclui scatterplot matrix, heatmap/correlograma e análise de dados temporais, textuais, árvores e redes. Oluleye (2023), capítulo 6, cobre K-Means e perfil de clusters, PCA e análise fatorial. Pandas Cookbook (2024), capítulos 6–9, documenta visualização, reshape, groupby e algoritmos temporais como ferramentas de análise.

## Perguntas de revisão

1. Que estrutura não é visível em análises de uma variável ou de pares?
2. A escala influencia distância, componente ou fator?
3. A projeção conserva a propriedade que quero interpretar?
4. Como avaliar estabilidade e utilidade dos grupos além de desenhá-los?
