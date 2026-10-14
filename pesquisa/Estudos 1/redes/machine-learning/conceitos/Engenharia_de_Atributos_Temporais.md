---
title: "Engenharia de Atributos Temporais"
type: "conceito"
network: "machine-learning"
area: "Feature Engineering"
status: "rascunho"
source_ids:
  - "OZDEMIR-2022"
  - "DUBOUE-2020"
  - "BARDOL-2025"
  - "CAMPESATO-2024"
tags:
  - conceito
  - feature-engineering
  - series-temporais
---

# Engenharia de Atributos Temporais

## Definição

Representação de datas, eventos e histórico como atributos disponíveis no instante em que a previsão será feita. O ponto central é respeitar a ordem temporal e o histórico realmente acessível.

## Técnicas

- Partes de calendário: hora, dia, semana, mês, feriado e tempo desde evento; codificar ciclos com seno/cosseno quando a continuidade do ciclo for útil.
- Defasagens (lags) de alvo ou preditores, sempre deslocadas para trás em relação ao instante de previsão.
- Janelas móveis, expansivas e médias exponencialmente ponderadas (EMA) para resumos de tendência e variabilidade.
- Agregações históricas por entidade, com corte temporal explícito, além de indicadores de recência, frequência e intervalo entre eventos.
- Atributos de tendência, sazonalidade e domínio, avaliados junto aos diagnósticos em [[redes/machine-learning/conceitos/Diagnostico_Exploratorio_de_Series_Temporais|EDA de séries temporais]].

## Regras contra vazamento temporal

- Para cada linha, use somente registros ocorridos até o corte da previsão.
- Gere janelas depois da separação temporal, mantendo as transformações dentro do pipeline e o histórico de cada entidade corretamente ordenado.
- Considere sobreposição de janelas e intervalo entre treino/validação; a avaliação deve imitar horizonte e latência reais.
- Compare com baseline temporal simples; atributos mais complexos não garantem ganho.

## Conexões

- [[redes/machine-learning/conceitos/Feature_Engineering|Feature Engineering]]
- [[redes/machine-learning/conceitos/Diagnostico_Exploratorio_de_Series_Temporais|Análise Exploratória de Séries Temporais]]
- [[redes/machine-learning/conceitos/Selecao_de_Modelos_Orientada_pelo_EDA|Seleção de Modelos Orientada pelo EDA]]
- [[redes/machine-learning/conceitos/Cross-Validation|Cross-Validation]]
- [[redes/machine-learning/conceitos/Pipelines_de_Feature_Engineering|Pipelines de Feature Engineering sem Vazamento]]

## Evidências nas fontes

Ozdemir (2022), cap. 7; Duboue (2020), cap. 7; Bardol (2025), cap. 6; Campesato (2024), cap. 1 para datas, divisão e vazamento.

