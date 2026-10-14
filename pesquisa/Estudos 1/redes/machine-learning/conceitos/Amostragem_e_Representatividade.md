---
title: "Amostragem e Representatividade"
type: "conceito"
network: "machine-learning"
area: "EDA e desenho de dados"
status: "rascunho"
source_ids:
  - "CASTRO-2026"
tags:
  - conceito
  - eda
  - amostragem
---

# Amostragem e Representatividade

## Definição

Amostragem é a seleção de observações de uma população para estudar suas características com custo menor do que observar toda a população. Representatividade descreve o quanto a amostra contempla a população e os contextos relevantes para a pergunta; ela depende do processo de seleção e da cobertura, não apenas do tamanho da amostra.

## Problema que resolve

EDA em dados amostrados pode ser mais rápida e legível, mas uma amostra inadequada esconde segmentos, eventos raros ou mudanças temporais. Uma grande amostra de origem enviesada continua podendo representar mal a população-alvo.

## Como aplicar

1. Definir população, unidade amostral, quadro de seleção, período e critérios de inclusão.
2. Conferir volumes, taxas de participação e composição por segmentos importantes.
3. Para diagnóstico visual, usar amostra reproduzível quando o conjunto for muito grande; preservar estratos ou eventos raros quando a pergunta depender deles.
4. Separar amostra exploratória, treino e avaliação. Documentar seed, filtros e pesos se usados.
5. Comparar atributos da amostra com dados externos/conhecidos da população, quando disponíveis.

## Limitações e armadilhas

O resumo de uma amostra não revela segmentos excluídos do quadro amostral. Amostragem conveniente pode distorcer prevalência e relações. Oversampling de classes raras pode ajudar a visualizar e treinar, mas muda a prevalência e não deve contaminar avaliação representativa. A amostragem visual não substitui o split de validação.

## Relações

- [[redes/machine-learning/conceitos/Analise_Exploratoria_de_Dados|Análise Exploratória de Dados]]
- [[redes/machine-learning/conceitos/Imbalanced_Data|Imbalanced Data]]
- [[redes/machine-learning/conceitos/Cross-Validation|Cross-Validation]]
- [[redes/machine-learning/conceitos/Perfilamento_e_EDA_Automatizada|Perfilamento e EDA Automatizada]]

## Evidência nas fontes

Castro (2026), capítulo 2, seção 2.5.1, inclui amostragem entre as etapas de preparação dos dados. Aplicações específicas a conjuntos muito grandes são uma recomendação de trabalho a adaptar ao desenho amostral real.

## Perguntas de revisão

1. Qual população e unidade a amostra representa?
2. Que grupo pode ter baixa cobertura ou estar ausente?
3. A amostra usada para visualizar preserva os casos raros relevantes?
4. O conjunto de avaliação mantém a prevalência e o desenho de uso?
