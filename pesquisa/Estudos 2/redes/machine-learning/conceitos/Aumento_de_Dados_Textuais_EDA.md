---
title: "Aumento de Dados Textuais (EDA)"
type: "conceito"
network: "machine-learning"
area: "Aumento de Dados"
status: "canônico"
source_ids:
  - "Artificial Intelligence for Engineers"
  - "AI_and_ML_for_Coders_Applying_Core_ML_-_Suddhasatwa_Bhaumik"
tags: [conceito, rede/machine-learning, data-augmentation, texto, NLP]
---

# Aumento de Dados Textuais (EDA)

## Definição
Em NLP, Easy Data Augmentation (EDA) é uma família de operações locais para produzir variantes de frases, usualmente por substituição de sinônimos, inserção, troca de posição e exclusão aleatória de palavras.

## Como funciona
As operações são sorteadas em tokens ou palavras, com regras que tentam manter a frase e seu rótulo. São aplicadas ao treino; as versões resultantes devem ser revisadas ou avaliadas automaticamente quanto a sentido e qualidade.

## Quando usar
Como baseline simples em classificação de texto com poucos exemplos, quando pequenas alterações lexicais e de ordem não alteram o rótulo.

## Limitações
Negação, entidades, números, termos técnicos e ordem sintática podem ser críticos. Substituições lexicais podem mudar sentimento, intenção ou significado; exclusão/troca aleatória pode gerar texto gramaticalmente inválido. Verifique preservação semântica e mantenha textos reais em validação/teste.

## Relações
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados]]
- [[redes/machine-learning/conceitos/Representacao_de_Texto_para_ML|Representação de texto para ML]]
- [[redes/machine-learning/conceitos/Analise_Exploratoria_de_Texto|Análise Exploratória de Texto]]
- [[redes/machine-learning/conceitos/Back_Translation|Back translation]]

## Evidências
*Artificial Intelligence for Engineers*, seção de augmentation em NLP: synonym replacement, word insertion, word swap e word deletion; Bhaumik, *AI and ML for Coders*, recomenda back-translation e synonym replacement para variar dados de treino de transformers.
