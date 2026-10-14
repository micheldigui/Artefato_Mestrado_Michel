---
title: "Estatísticas Resistentes e Formas de Distribuição"
type: "conceito"
network: "machine-learning"
area: "EDA e estatística descritiva"
status: "rascunho"
source_ids:
  - "TUKEY-1977"
  - "CASTRO-2026"
  - "OLULEYE-2023"
tags:
  - conceito
  - eda
  - distribuicoes
---

# Estatísticas Resistentes e Formas de Distribuição

## Definição

É o conjunto de resumos e gráficos usado para descrever localização, dispersão, forma e caudas sem reduzir a distribuição a uma única média e desvio padrão. Mediana, quartis/hinges, amplitude interquartil, quantis e resumos de cinco números são menos dominados por observações extremas do que média e variância.

## Técnicas

- **Stem-and-leaf:** mostra valores ordenados preservando algarismos; útil em conjuntos pequenos e para ver concentração, lacunas e forma.
- **Resumo de cinco números/boxplot:** mínimo, quartis, mediana e máximo ou cercas/valores externos; compara centro, dispersão e extremos entre grupos.
- **Histograma e contagens em bins:** revela massa, assimetria, múltiplos picos e lacunas; escolha largura de classe com cuidado.
- **ECDF e letter values:** mostram quantis e caudas sem depender da escolha de bins; letter values detalham progressivamente os quantis.
- **Média, mediana, moda, variância, desvio, percentis e assimetria:** calculados juntos para diagnosticar quando diferentes resumos contam histórias diferentes.

## Como usar

Comece identificando tipo e unidade. Para cada medida numérica, compare histograma/ECDF com mediana, quartis, decis e faixa. Separe por grupos relevantes e preserve denominadores. Quando média e mediana divergem ou os gráficos exibem caudas/múltiplos picos, procure mistura de populações, limites físicos, erros ou escala; não “conserte” a distribuição automaticamente.

## Limitações

Boxplot resume e pode ocultar multimodalidade; histograma depende dos bins; resumo de cinco números não mostra dependência temporal; resistência não significa robustez a todo problema. Zeros podem representar processo específico e não apenas assimetria. Reúna resumo visual, conhecimento do domínio e inspeção dos casos.

## Relações

- [[redes/machine-learning/conceitos/Analise_Exploratoria_de_Dados|Análise Exploratória de Dados]]
- [[redes/machine-learning/conceitos/Visualizacao_Exploratoria_e_Codificacao_Visual|Visualização Exploratória e Codificação Visual]]
- [[redes/machine-learning/conceitos/Reexpressao_de_Variaveis|Reexpressão de Variáveis]]
- [[redes/machine-learning/conceitos/Outliers|Outliers]]
- [[redes/machine-learning/conceitos/Analise_Bivariada_e_Tabelas_de_Contingencia|Análise Bivariada e Tabelas de Contingência]]

## Evidência nas fontes

Tukey (1977), capítulos 1–2, 17 e 19–20: stem-and-leaf, extremos/mediana, hinges e boxplots, cercas, contagens por bins e formas de distribuições. Oluleye (2023), capítulo 1 e capítulo 4, trata estatísticas-resumo e exploração univariada. Castro (2026), capítulo 3, cobre distribuições, posição, variabilidade e forma.

## Perguntas de revisão

1. Média e mediana indicam o mesmo centro? O que explica a diferença?
2. O histograma muda muito quando os bins mudam?
3. Há grupos ou caudas diferentes escondidos pelo resumo agregado?
4. Que informação o boxplot esconde que uma ECDF ou stem-and-leaf revela?
