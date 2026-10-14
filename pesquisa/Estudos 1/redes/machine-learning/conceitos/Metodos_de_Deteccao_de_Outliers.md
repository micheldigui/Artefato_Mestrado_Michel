---
title: "Métodos de Detecção de Outliers"
type: "conceito"
network: "machine-learning"
area: "EDA e qualidade dos dados"
status: "rascunho"
source_ids:
  - "TUKEY-1977"
  - "OLULEYE-2023"
  - "ATWAN-2022"
tags:
  - conceito
  - eda
  - outliers
---

# Métodos de Detecção de Outliers

## Definição

Métodos de detecção sinalizam observações que se afastam de um padrão de referência univariado, condicional ou multivariado. Um sinal é uma hipótese para inspeção; não prova erro, fraude ou evento anômalo, nem decide sozinho a remoção.

## Famílias de método

- **Univariados resistentes:** cercas de Tukey usando quartis/IQR; úteis para triagem por variável e grupo.
- **Z-score:** distância em desvios-padrão da média; funciona melhor como regra simples quando forma e escala justificam a referência.
- **Z-score modificado:** usa mediana/MAD para reduzir influência de extremos na própria estimativa do centro/escala.
- **Bivariados/condicionais:** dispersões, resíduos e comparação com tendência/grupo; um valor pode ser incomum apenas condicionado a outra variável.
- **Multivariados:** distância de vizinhos/KNN, Local Outlier Factor, Isolation Forest, One-Class SVM/OCSVM e COPOD; cada um define raridade de forma diferente.
- **Temporais:** regras estatísticas, resíduos ou detectores não supervisionados para localizar desvios na sequência, respeitando frequência e sazonalidade.

## Processo

1. Defina unidade, população/base de comparação e período.
2. Escolha método univariado, condicional, multivariado ou temporal conforme o padrão procurado.
3. Verifique sensibilidade aos parâmetros e à escala; compare métodos sem tratá-los como votos independentes.
4. Inspecione casos por fonte, grupo e contexto do domínio.
5. Decida manter, corrigir, limitar, investigar ou modelar explicitamente como evento raro; registre justificativa.

## Limitações

Thresholds são convenções, não leis universais. Métodos multivariados sofrem com escala, dimensão, densidade variável e contaminação. Se o desvio for alvo do estudo, excluí-lo elimina o fenômeno. Ajustes aprendidos usam somente treino para evitar vazamento.

## Relações

- [[redes/machine-learning/conceitos/Outliers|Outliers]]
- [[redes/machine-learning/conceitos/Estatisticas_Resistentes_e_Formas_de_Distribuicao|Estatísticas Resistentes e Formas de Distribuição]]
- [[redes/machine-learning/conceitos/Diagnostico_Exploratorio_de_Series_Temporais|Diagnóstico Exploratório de Séries Temporais]]
- [[redes/machine-learning/conceitos/Detecção_de_Anomalias|Detecção de Anomalias]]
- [[redes/machine-learning/conceitos/DBSCAN|DBSCAN]]
- [[redes/machine-learning/conceitos/Selecao_de_Modelos_Orientada_pelo_EDA|Seleção de Modelos Orientada pelo EDA]]

## Evidência nas fontes

Oluleye (2023), capítulo 9, cobre outliers univariados, bivariados e multivariados, cap/floor, remoção e substituição. Atwan (2022), capítulos 8 e 14, inclui visualização, z-score, z-score modificado, Tukey, KNN, LOF, Isolation Forest, OCSVM e COPOD. Tukey (1977), capítulo 2, descreve boxplot, cercas e valores externos.

## Perguntas de revisão

1. Qual é a população de referência para chamar um caso de raro?
2. A anomalia é univariada, condicional, multivariada ou temporal?
3. O resultado muda com escala, grupo ou parâmetro?
4. Remover o caso apagaria o evento que o problema precisa encontrar?
