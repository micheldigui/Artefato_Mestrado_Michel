---
title: "Análise Exploratória Geoespacial"
type: "conceito"
network: "machine-learning"
area: "EDA de dados espaciais"
status: "rascunho"
source_ids:
  - "CASTRO-2026"
tags:
  - conceito
  - eda
  - geoespacial
---

# Análise Exploratória Geoespacial

## Definição

EDA geoespacial examina onde as observações ocorrem e como medidas variam no espaço. Coordenadas, geometrias, sistema de referência, unidade territorial e escala espacial fazem parte da interpretação dos dados.

## Técnicas

- Validar latitude/longitude, geometria, sistema de coordenadas, duplicatas e cobertura do território.
- Mapear observações pontuais para detectar concentração, buracos e artefatos de geocodificação.
- Usar mapas coropléticos para medidas agregadas por área; comparar taxas/valores normalizados quando o tamanho da população varia, não apenas contagens brutas.
- Usar mapas de bolhas quando posição e magnitude importam; registrar sobreposição e escala.
- Comparar mapa com tabela/gráfico e resumir por regiões ou períodos para verificar padrões e denominadores.

## Relação com ML

Estrutura espacial pode exigir agregação por região, features de vizinhança, validação espacial ou blocos geográficos. Isso evita que locais adjacentes/dependentes apareçam dos dois lados de uma avaliação quando o uso será em áreas novas. Modelos de distância ou coordenadas precisam respeitar projeção e métrica espacial apropriada.

## Limitações

Escolhas de fronteira e agregação alteram padrões (problema da unidade espacial modificável); mapas coropléticos de contagem favorecem áreas/populações grandes; coordenadas podem carregar risco de privacidade. Proximidade visual não demonstra interação causal.

## Relações

- [[redes/machine-learning/conceitos/Analise_Exploratoria_de_Dados|Análise Exploratória de Dados]]
- [[redes/machine-learning/conceitos/Visualizacao_Exploratoria_e_Codificacao_Visual|Visualização Exploratória e Codificação Visual]]
- [[redes/machine-learning/conceitos/Analise_Multivariada_Exploratoria|Análise Multivariada Exploratória]]
- [[redes/machine-learning/conceitos/Selecao_de_Modelos_Orientada_pelo_EDA|Seleção de Modelos Orientada pelo EDA]]

## Evidência nas fontes

Castro (2026), capítulo 5.6, identifica coroplético e mapa de bolhas; capítulo 2 discute tipos/dimensões dos dados. A validação espacial é uma implicação para modelos em que a dependência geográfica afeta a generalização.

## Perguntas de revisão

1. Qual é o sistema de coordenadas e a unidade espacial?
2. As contagens precisam ser convertidas em taxas ou normalizadas?
3. Que dependência espacial tornaria split aleatório otimista?
4. A agregação regional esconde variação interna?
