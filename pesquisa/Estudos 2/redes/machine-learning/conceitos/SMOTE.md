---
title: "SMOTE (Synthetic Minority Over-sampling Technique)"
type: "conceito"
network: "machine-learning"
area: "Aumento de Dados"
status: "canônico"
source_ids:
  - "AI-Assisted_Statistics_for_Data_Scientists_3E_-_Peter_Bruce"
  - "AI_and_ML_for_Coders_Applying_Core_ML_-_Suddhasatwa_Bhaumik"
tags: [conceito, rede/machine-learning, data-augmentation, dados-desbalanceados]
---

# SMOTE (Synthetic Minority Over-sampling Technique)

## Definição
Método de oversampling para classificação que cria exemplos sintéticos da classe minoritária interpolando observações próximas no espaço de atributos.

## Como funciona
Escolhe um registro minoritário, encontra seus vizinhos mais próximos e seleciona um deles; cria-se um ponto em posição aleatória entre ambos. O número de pontos gerados depende da proporção de reamostragem desejada.

## Quando usar
Como candidato para classificação com dados numéricos e classe minoritária, quando a geometria local entre vizinhos tem significado. Compare com pesos de classe, oversampling simples e ajuste de limiar usando a métrica e o custo operacional adequados.

## Limitações
A interpolação pode atravessar fronteiras de classe, gerar combinações impossíveis ou perder significado com categorias codificadas numericamente, relações temporais e dados estruturados. Não aplicar antes da validação: SMOTE deve ser ajustado exclusivamente no treino de cada fold; manter validação e teste reais.

## Relações
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados]]
- [[redes/machine-learning/conceitos/Imbalanced_Data|Dados desbalanceados]]
- [[redes/machine-learning/conceitos/Oversampling_e_Bootstrap|Oversampling e bootstrap]]
- [[redes/machine-learning/conceitos/K-Nearest_Neighbors__KNN_|K-Nearest Neighbors]]
- [[redes/machine-learning/conceitos/Pipelines_de_Feature_Engineering|Pipeline sem vazamento]]
- [[redes/machine-learning/conceitos/Precision_e_Recall|Precision e Recall]]

## Evidências
Bruce et al., *AI-Assisted Statistics for Data Scientists*, 3ª ed., seção “Data Generation”; Bhaumik, *AI and ML for Coders*, seção sobre classes desbalanceadas e chamada a SMOTE em `x_train` antes do ajuste, mantendo teste separado. Bruce descreve a interpolação por vizinhos e alerta que sobreposição entre classes pode introduzir viés.
