---
title: "Back Translation (Retrotradução)"
type: "conceito"
network: "machine-learning"
area: "Aumento de Dados"
status: "canônico"
source_ids:
  - "Artificial Intelligence for Engineers"
  - "AI_and_ML_for_Coders_Applying_Core_ML_-_Suddhasatwa_Bhaumik"
tags: [conceito, rede/machine-learning, data-augmentation, texto, NLP]
---

# Back Translation (Retrotradução)

## Definição
Técnica de aumento textual que traduz uma frase para outro idioma e depois a traduz de volta ao idioma original, gerando uma paráfrase potencialmente diferente na superfície.

## Como funciona
Para cada texto, usa-se uma tradução de ida e volta; a variante resultante precisa manter conteúdo, entidades, negações e rótulo. A geração deve ocorrer somente no treino.

## Quando usar
Quando tradução automática de qualidade está disponível e paráfrases são aceitáveis para a tarefa, sobretudo para ampliar variação lexical e sintática em NLP.

## Limitações
A tradução pode perder nuance, nomes, números, terminologia, negação ou polaridade. Erros sistemáticos do tradutor podem introduzir rótulos errados; auditar amostras e comparar modelo treinado com e sem variantes.

## Relações
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados]]
- [[redes/machine-learning/conceitos/Aumento_de_Dados_Textuais_EDA|Aumento de dados textuais (EDA)]]
- [[redes/machine-learning/conceitos/Representacao_de_Texto_para_ML|Representação de texto para ML]]
- [[redes/machine-learning/conceitos/Pipelines_de_Feature_Engineering|Pipeline sem vazamento]]

## Evidências
*Artificial Intelligence for Engineers*, seção de augmentation em NLP, descreve retraduzir do idioma-alvo para o original; Bhaumik, *AI and ML for Coders*, menciona back-translation para aumentar tamanho e diversidade dos dados usados no treino de transformers.
