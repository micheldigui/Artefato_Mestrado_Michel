---
title: "Visualização Exploratória e Codificação Visual"
type: "conceito"
network: "machine-learning"
area: "EDA e comunicação visual"
status: "rascunho"
source_ids:
  - "CASTRO-2026"
  - "OLULEYE-2023"
  - "GARG-2018"
tags:
  - conceito
  - eda
  - visualizacao
---

# Visualização Exploratória e Codificação Visual

## Definição

Visualização exploratória representa dados por posição, comprimento, cor, forma, área ou conexão para facilitar a percepção de distribuição, comparação, associação, evolução ou estrutura. Uma codificação bem escolhida responde uma pergunta analítica com uma leitura visual que não distorce o denominador ou a escala.

## Escolha inicial pelo tipo de pergunta

- **Distribuição numérica:** histograma, ECDF, boxplot/letter values; violin como visão de densidade com ressalvas.
- **Distribuição categórica:** barras com contagens ou proporções explicitamente identificadas; muitas categorias podem exigir agrupamento justificado.
- **Relação numérica-numérica:** scatterplot; transparência/jitter ou amostragem para sobreposição; linha/suavizador exploratório quando ordem ou tendência for relevante.
- **Numérica por grupos:** boxplot, violin, ECDF ou pontos agregados com tamanho de amostra.
- **Categórica-categórica:** tabela de contingência/heatmap de contagens ou proporções, indicando o denominador.
- **Múltiplas variáveis:** pairplot/matriz de dispersão para poucas variáveis; heatmap/correlograma para matriz com escala e relação declaradas.
- **Tempo:** linha, facets por grupo e decomposição; mapa para evolução espacial quando necessário.
- **Localização:** mapas de pontos ou coropléticos, respeitando projeção, unidade territorial e normalização.

## Princípios e processo

Declare a pergunta antes de escolher gráfico; selecione uma marca visual apropriada ao tipo da variável; use cor/forma com semântica consistente; identifique unidades, período, grupo e denominador; examine escalas truncadas, bins, sobreposição e dados ausentes. Aplique princípios preatentivos e Gestalt para hierarquia e agrupamento, não para decorar.

## Limitações

Gráficos podem ocultar tamanhos amostrais pequenos, padrões locais, valores extremos e dependências. Gráficos de pizza/doughnut dificultam comparação de partes próximas; dashboards podem reduzir uma análise complexa a métricas sem contexto. Exploração visual gera hipótese; teste formal ou validação pode ser necessário.

## Relações

- [[redes/machine-learning/conceitos/Analise_Exploratoria_de_Dados|Análise Exploratória de Dados]]
- [[redes/machine-learning/conceitos/Estatisticas_Resistentes_e_Formas_de_Distribuicao|Estatísticas Resistentes e Formas de Distribuição]]
- [[redes/machine-learning/conceitos/Analise_Bivariada_e_Tabelas_de_Contingencia|Análise Bivariada e Tabelas de Contingência]]
- [[redes/machine-learning/conceitos/Analise_Multivariada_Exploratoria|Análise Multivariada Exploratória]]
- [[redes/machine-learning/conceitos/Diagnostico_Exploratorio_de_Series_Temporais|Diagnóstico Exploratório de Séries Temporais]]
- [[redes/machine-learning/conceitos/Analise_Exploratoria_Geoespacial|Análise Exploratória Geoespacial]]

## Evidência nas fontes

Castro (2026), capítulos 4–5, cobre percepção visual, Gestalt, design e métodos para distribuições, associações, evolução e mapas. Oluleye (2023), capítulos 3–6, traz gráficos univariados, bivariados e multivariados. Garg (2018), capítulo 4, cobre gráficos categóricos e numéricos como scatter, box, violin, swarm e grades facetadas.

## Perguntas de revisão

1. Qual pergunta este gráfico responde e qual comparação facilita?
2. Qual é o denominador de cada barra, cor ou área?
3. A escala, os bins ou a sobreposição escondem parte da distribuição?
4. Uma codificação alternativa mudaria a conclusão visual?
