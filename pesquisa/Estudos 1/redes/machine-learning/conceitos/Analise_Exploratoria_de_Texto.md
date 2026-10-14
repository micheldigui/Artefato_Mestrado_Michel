---
title: "Análise Exploratória de Texto"
type: "conceito"
network: "machine-learning"
area: "EDA de dados não estruturados"
status: "rascunho"
source_ids:
  - "CASTRO-2026"
  - "OLULEYE-2023"
tags:
  - conceito
  - eda
  - texto
---

# Análise Exploratória de Texto

## Definição

EDA de texto caracteriza documentos e corpus antes de treinar modelos linguísticos ou de classificação: estrutura, cobertura, comprimento, idioma, duplicatas, qualidade da extração, vocabulário, frequências e padrões semânticos básicos.

## Técnicas

- Medir documentos vazios, duplicados, comprimento em caracteres/tokens, idioma e distribuição por fonte, classe, autor ou período.
- Inspecionar exemplos curtos, longos, truncados, com encoding ruim ou artefatos de OCR.
- Após definir tokenização, contar termos e n-gramas; revisar stopwords, stemming/lemmatização e POS conforme o objetivo.
- Examinar sentimento ou tópicos como ferramentas de sumarização/triagem; revisar amostras manualmente e observar erros por subgrupo.
- Comparar vocabulário e distribuição de comprimento entre treino, validação e períodos para encontrar mismatch ou vazamento por duplicatas.

## Como usar para ML

Diagnósticos podem orientar classificação lexical com modelos esparsos, embeddings, topic modeling ou busca. Divida por documento/autor/tempo conforme a aplicação; parágrafos do mesmo documento em ambos os conjuntos podem vazar estilo e conteúdo. Faça preprocessing depois do split quando a operação aprender vocabulário ou estatísticas do corpus.

## Limitações

N-gramas frequentes não são necessariamente tópicos, sentimento ou causalidade. Wordcloud privilegia frequência e forma gráfica, não importância. Remoção de stopwords pode eliminar negação; normalização pode fundir sentidos. Tópicos automáticos exigem validação humana.

## Relações

- [[redes/machine-learning/conceitos/Analise_Exploratoria_de_Dados|Análise Exploratória de Dados]]
- [[redes/machine-learning/conceitos/Visualizacao_Exploratoria_e_Codificacao_Visual|Visualização Exploratória e Codificação Visual]]
- [[redes/machine-learning/conceitos/Imbalanced_Data|Imbalanced Data]]
- [[redes/machine-learning/conceitos/Cross-Validation|Cross-Validation]]
- [[redes/machine-learning/conceitos/Selecao_de_Modelos_Orientada_pelo_EDA|Seleção de Modelos Orientada pelo EDA]]

## Evidência nas fontes

Castro (2026), capítulo 6.2: estruturação, análise descritiva e visualização de texto/documentos. Oluleye (2023), capítulo 8: tokenização/preparação, stopwords, POS, stemming/lemmatização, n-gramas, frequência, sentimento e modelagem de tópicos.

## Perguntas de revisão

1. Como documentos duplicados ou do mesmo autor podem contaminar a avaliação?
2. Que informação se perde na limpeza/normalização?
3. O vocabulário ou comprimento muda entre fontes, classes ou períodos?
4. Como validar uma conclusão obtida por sentimento ou tópicos?
